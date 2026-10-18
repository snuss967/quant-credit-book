"""Chapter 6-B figures: Options for Credit People (replication, Greeks, jump-to-default, two measures).

Run:  python3 tools/figures/ch06b.py      (writes assets/figures/ch06b_*.png)

Every number is ILLUSTRATIVE: it is generated from a stated model (Black-Scholes, Merton debt,
Merton-1976 jump to zero) with the chapter's own parameters. The script executes Listing 6-B.1
(credit_options.py, Appendix F, book_src/95_appF_code_companion.md) unchanged, in one namespace, so the
figures cannot drift from the tables and worked examples the chapter prints. Halvorsen is fictional.

Figure numbering: the chapter already carries a text-art block "Figure 6-B.1" (the capital-structure
ladder, section 6-B.1.4), so the new figures are 6-B.2 to 6-B.6.

Color roles are fixed across the chapter:
  measures       : physical P = BLUE, risk-neutral Q = ORANGE (hazard premium ORANGE, recovery premium VIOLET)
  firms          : the 216 bp firm = BLUE, its CCC cousin = ORANGE
  jump or not    : diffusion only = BLUE, with jump to default = ORANGE, the wing bound = INK_2 dashed
  time to expiry : one hue (SEQ_BLUE), dark = short-dated
  P&L polarity   : gain = DIVERGING blue, loss = DIVERGING red
"""
import contextlib
import io
import math
import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))
from style import *  # noqa: E402,F401,F403
import numpy as np  # noqa: E402
from matplotlib.ticker import FuncFormatter  # noqa: E402
from scipy.special import ndtr  # noqa: E402  (vectorised N(x) for the hedging simulation only)

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
APPENDIX = os.path.join(ROOT, "book_src", "95_appF_code_companion.md")

C_P, C_Q, C_REC = BLUE, ORANGE, VIOLET
GAIN, LOSS = "#3987e5", "#e66767"          # the two ends of the book's diverging ramp
NET = SEQ_BLUE_STEPS[10]
MINUS = "−"


def load_engine():
    """Execute Listing 6-B.1 (credit_options.py and its self-test) in one namespace and return it."""
    with open(APPENDIX, encoding="utf-8") as fh:
        src = fh.read()
    m = re.search(r"\{#code-6b-1\}\s*```python\n(.*?)```", src, re.S)
    if m is None:
        raise SystemExit(f"Listing 6-B.1 not found in {APPENDIX}")
    ns = {"__name__": "ch06b_engine"}
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(m.group(1), "listing_6B_1", "exec"), ns)
    return ns


E = load_engine()
R_FREE = 0.04


# --------------------------------------------------------------------------------------------
# Figure 6-B.2  The gamma rent (section 6-B.2.4)
# --------------------------------------------------------------------------------------------
def hedged_pnl(sigma_real, sigma_imp, z, S0=100.0, K=100.0, T=0.25, r=R_FREE):
    """P&L at expiry of a long call, delta-hedged daily at the implied vol, paths scaled by sigma_real.

    z is an (n_paths, n_steps) array of standard normals, reused across sigma_real (common random
    numbers), so the curve of mean P&L against realized vol is smooth.
    """
    n, steps = z.shape
    dt = T / steps
    growth = math.exp(r * dt)
    S = np.full(n, S0)
    tau = T

    def delta(S, tau):
        d1 = (np.log(S / K) + (r + 0.5 * sigma_imp ** 2) * tau) / (sigma_imp * math.sqrt(tau))
        return ndtr(d1)

    c0 = E["bs_price"](S0, K, T, sigma_imp, r, "call")
    dlt = delta(S, tau)
    cash = dlt * S0 - c0                      # short dlt shares, long one call, financed at r
    for i in range(steps):
        S = S * np.exp((r - 0.5 * sigma_real ** 2) * dt + sigma_real * math.sqrt(dt) * z[:, i])
        tau -= dt
        cash = cash * growth
        if i < steps - 1:
            new = delta(S, tau)
            cash += (new - dlt) * S
            dlt = new
    return np.maximum(S - K, 0.0) - dlt * S + cash


def fig_gamma_rent():
    fig, axes = new_figure("panel2", ncols=2)
    sig_i, sig_r, K = 0.30, 0.40, 100.0

    # Left: where the rent is earned. Daily rent = (1/2) Gamma S^2 (sig_r^2 - sig_i^2) / 365.
    ax = axes[0]
    S = np.linspace(65.0, 135.0, 500)
    gap = sig_r ** 2 - sig_i ** 2
    cases = [(1.0, "1 year", SEQ_BLUE_STEPS[4], 67.5),
             (0.25, "3 months", SEQ_BLUE_STEPS[8], 114.0),
             (1.0 / 52.0, "1 week", SEQ_BLUE_STEPS[12], 105.5)]
    # (1 year at spot 67.5, not 122: the 1-year and 3-month curves cross near 122, which made that label ambiguous)
    for T, label, col, xl in cases:
        d1 = (np.log(S / K) + (R_FREE + 0.5 * sig_i ** 2) * T) / (sig_i * math.sqrt(T))
        rent = S * np.exp(-0.5 * d1 ** 2) / math.sqrt(2.0 * math.pi) / (2.0 * sig_i * math.sqrt(T)) * gap / 365.0
        ax.plot(S, rent, color=col, linewidth=LW + 0.4)
        yl = float(np.interp(xl, S, rent))
        ax.plot([xl], [yl], "o", color=col, markersize=5, zorder=5)
        ax.annotate(label, (xl, yl), xytext=(4, 8), textcoords="offset points", fontsize=8.5, color=INK_2,
                    ha="left", va="bottom")
    ax.plot([K, K], [0, 0.098], color=NEUTRAL, linewidth=0.9, linestyle=(0, (3, 3)), zorder=1)
    ax.set_xlabel("Spot price of the underlying (strike = 100)")
    ax.set_ylabel(r"Rent per day (\$ per option)")
    ax.set_ylim(0, 0.115)
    ax.set_xlim(65, 135)
    note(ax, "if realized vol is 40%\nand implied vol 30%", "upper right")

    # Right: the sign of the rent is the sign of (realized - implied).
    ax = axes[1]
    rng = np.random.default_rng(66)
    z = rng.standard_normal((20000, 63))
    vols = np.arange(0.10, 0.5001, 0.05)
    mean, lo, hi = [], [], []
    for v in vols:
        pnl = hedged_pnl(v, sig_i, z)
        mean.append(pnl.mean())
        lo.append(np.percentile(pnl, 5))
        hi.append(np.percentile(pnl, 95))
    x = vols * 100.0
    assert all(b_ > a_ for a_, b_ in zip(mean, mean[1:]))                 # vega > 0: mean P&L rises with realized vol
    assert abs(mean[int(round((sig_i - 0.10) / 0.05))]) < 0.15            # and is ~0 where realized = implied (30%)
    ax.fill_between(x, lo, hi, color=SEQ_BLUE_STEPS[1], zorder=1)
    ax.axhline(0, color=NEUTRAL, linewidth=0.9, zorder=2)
    ax.plot(x, mean, color=BLUE, linewidth=LW + 0.4, zorder=3)
    mark_event(ax, sig_i * 100.0, "implied 30%")
    ax.set_xlabel("Realized volatility over the option's life (%)")
    ax.set_ylabel(r"Hedged P&L at expiry (\$ per option)")
    label_end(ax, x[-1], mean[-1], "mean", BLUE, dx=6)
    ax.text(10.8, 7.7, "shaded: 5th to 95th\npercentile of paths", color=INK_2, fontsize=8, ha="left", va="top")
    note(ax, "3-month at-the-money option,\ndaily hedging at the 30% delta", "lower right")
    ax.set_xlim(10, 50)
    fig.get_layout_engine().set(w_pad=0.1)
    finish(fig, "ch06b_gamma_rent")
    return mean


# --------------------------------------------------------------------------------------------
# Figure 6-B.3  Merton debt, Greek by Greek (section 6-B.3.4)
# --------------------------------------------------------------------------------------------
def fig_merton_bond_greeks():
    fig, axes = new_figure("panel2", ncols=2)
    firms = [(80.0, 0.25, C_P, "216 bp firm (F = 80, vol 25%)"),
             (95.0, 0.40, C_Q, "CCC cousin (F = 95, vol 40%)")]
    V = np.linspace(40.0, 170.0, 261)
    for k, (ax, key, ylab) in enumerate(zip(axes, ["bond_delta", "bond_gamma"],
                                            ["Bond delta  ∂B/∂V", "Bond gamma  ∂²B/∂V²"])):
        for F, sv, col, label in firms:
            y = [E["merton"](v, F, 1.0, sv, R_FREE)[key] for v in V]
            if key == "bond_delta":
                assert all(b_ <= a_ + 1e-12 for a_, b_ in zip(y, y[1:])) and 0.0 <= min(y) and max(y) <= 1.0
            else:
                assert max(y) < 0.0                                    # short gamma on assets at every V
            ax.plot(V, y, color=col, linewidth=LW + 0.2, label=label if k == 0 else None)
            m0 = E["merton"](100.0, F, 1.0, sv, R_FREE)
            ax.plot([100.0], [m0[key]], "o", color=col, markersize=6, zorder=5, markeredgecolor="white")
            txt = f"{m0[key]:.2f}" if k == 0 else f"{MINUS}{abs(m0[key]):.4f}"
            if k == 0:
                ax.annotate(txt, (100.0, m0[key]), xytext=(7, 5), textcoords="offset points", fontsize=8.5,
                            color=INK_2, ha="left", va="bottom")
            else:
                if F == 80.0:
                    ax.annotate(txt, (100.0, m0[key]), xytext=(-8, 4), textcoords="offset points",
                                fontsize=8.5, color=INK_2, ha="right", va="bottom")
                else:
                    ax.annotate(txt, (100.0, m0[key]), xytext=(8, -4), textcoords="offset points",
                                fontsize=8.5, color=INK_2, ha="left", va="top")
        ax.axvline(100.0, color=NEUTRAL, linewidth=0.9, linestyle=(0, (3, 3)), zorder=1)
        ax.set_xlabel("Asset value V (today V = 100)")
        ax.set_ylabel(ylab)
        ax.set_xlim(40, 170)
    axes[0].set_ylim(0, 1.0)
    axes[0].legend(loc="upper right", handlelength=1.4, borderaxespad=0.2)
    axes[1].set_ylim(-0.0245, 0.0)
    axes[1].yaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{v:.3f}".replace("-", MINUS)))
    axes[0].text(42, 0.045, "long a little of the firm", color=MUTED, fontsize=8, ha="left", va="bottom")
    axes[1].text(168, -0.0236, "short gamma on assets, everywhere", color=MUTED, fontsize=8, ha="right", va="bottom")
    finish(fig, "ch06b_merton_bond_greeks")


# --------------------------------------------------------------------------------------------
# Figure 6-B.4  Jump to default: the put floor and the wing (sections 6-B.5.3 to 6-B.5.5)
# --------------------------------------------------------------------------------------------
def fig_jtd_put_floor_and_wing():
    S0, sigma, r, lam, T = 100.0, 0.40, R_FREE, 0.05, 1.0
    F0 = S0 * math.exp(r * T)
    floor = E["urc_eur"](T, r, lam)

    fig, axes = new_figure("panel2", ncols=2)
    m = np.linspace(0.03, 1.2, 240)
    K = m * F0
    diff = np.array([E["bs_price"](S0, k, T, sigma, r, "put") / k for k in K])
    jump = np.array([E["jtd_price"](S0, k, T, sigma, r, lam, "put") / k for k in K])

    ax = axes[0]
    ax.set_yscale("log")
    ax.plot(m, diff, color=C_P, linewidth=LW + 0.2, label="diffusion only")
    ax.plot(m, jump, color=C_Q, linewidth=LW + 0.2, label="with jump to default")
    ax.axhline(floor, color=INK_2, linewidth=0.9, linestyle=(0, (3, 3)), zorder=1)
    assert float(jump.min()) >= floor - 1e-12 and all(b_ >= a_ for a_, b_ in zip(jump, jump[1:]))
    ax.text(0.03, floor * 0.80, "floor: the unit\nrecovery claim", color=INK_2, fontsize=8, ha="left", va="top")
    ax.legend(loc="lower right", handlelength=1.4, borderaxespad=0.2)
    ax.set_ylim(1e-4, 0.5)
    ax.set_xlim(0, 1.2)
    ax.set_xlabel("Strike K as a fraction of the forward")
    ax.set_ylabel(r"Put price per \$1 of strike (log scale)")
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{v:g}"))
    ax.grid(axis="y", which="major")

    ax = axes[1]
    m2 = np.unique(np.append(np.linspace(0.06, 0.99, 120), 0.20))
    iv = []
    for mm in m2:
        k = mm * F0
        px = E["jtd_price"](S0, k, T, sigma, r, lam, "put")
        v, status = E["implied_vol"](px, S0, k, T, r, "put", tol_price=1e-10)
        assert status == "ok", (mm, status)
        iv.append(v * 100.0)
    bound = [E["wing_floor_vol"](S0, mm * F0, T, r, lam) * 100.0 for mm in m2]
    assert all(i >= b_ - 1e-6 for i, b_ in zip(iv, bound))          # (6B.3) holds at every strike drawn
    ax.plot(m2, iv, color=C_Q, linewidth=LW + 0.2, label="with jump to default")
    ax.plot(m2, bound, color=INK_2, linewidth=1.2, linestyle=(0, (4, 2)), label="lower bound (6B.3)")
    ax.axhline(sigma * 100.0, color=C_P, linewidth=LW, label="diffusion only")
    i20 = int(np.argmin(abs(m2 - 0.20)))
    ax.plot([m2[i20]], [bound[i20]], "o", color=INK_2, markersize=5, zorder=5)
    ax.annotate(f"bound {bound[i20]:.1f}%\nat K/F = 0.2", (m2[i20], bound[i20]), xytext=(0.02, 57.0),
                fontsize=8, color=INK_2, ha="left", va="top",
                arrowprops=dict(arrowstyle="-", color=MUTED, linewidth=0.7, shrinkA=2, shrinkB=3))
    ax.set_xlim(0.0, 1.0)
    ax.set_ylim(0, 150)
    ax.set_xlabel("Strike K as a fraction of the forward")
    ax.set_ylabel("Black\u2013Scholes implied vol (%)")
    ax.legend(loc="upper right", handlelength=1.8, borderaxespad=0.2)
    note(ax, "S\u2080 = 100, vol 40%, r = 4%,\n\u03bb = 5%, T = 1", "lower left")
    finish(fig, "ch06b_jtd_put_floor_and_wing")
    return floor, bound[i20], iv[i20]


# --------------------------------------------------------------------------------------------
# Figure 6-B.5  Halvorsen: two measures, one spread (section 6-B.8, steps 1 to 4)
# --------------------------------------------------------------------------------------------
HALV = dict(spread=0.115, lam_q=0.145, pd_p=0.06, L_p=0.60)


def fig_halvorsen_two_measures():
    lam_p = E["MeasuredPD"](HALV["pd_p"], "P", 1.0).hazard()
    dec = E["spread_decomposition"](HALV["spread"], HALV["lam_q"], lam_p, HALV["L_p"])
    fig, axes = new_figure("panel2", ncols=2)

    ax = axes[0]
    t = np.linspace(0, 5, 200)
    sp, sq = np.exp(-lam_p * t), np.exp(-HALV["lam_q"] * t)
    ax.fill_between(t, sq, sp, color=SEQ_BLUE_STEPS[0], zorder=1)
    ax.plot(t, sp, color=C_P, linewidth=LW + 0.2, zorder=3, label=f"physical (P), hazard {lam_p * 100:.2f}%")
    ax.plot(t, sq, color=C_Q, linewidth=LW + 0.2, zorder=3, label=f"risk-neutral (Q), hazard {HALV['lam_q'] * 100:.1f}%")
    ax.plot([1.0], [math.exp(-lam_p)], "o", color=C_P, markersize=6, zorder=5, markeredgecolor="white")
    ax.annotate(f"{math.exp(-lam_p) * 100:.1f}%", (1.0, math.exp(-lam_p)), xytext=(6, 4),
                textcoords="offset points", fontsize=8.5, color=INK_2, ha="left", va="bottom")
    ax.plot([1.0], [math.exp(-HALV["lam_q"])], "o", color=C_Q, markersize=6, zorder=5, markeredgecolor="white")
    ax.annotate(f"{math.exp(-HALV['lam_q']) * 100:.1f}%", (1.0, math.exp(-HALV["lam_q"])), xytext=(-7, -3),
                textcoords="offset points", fontsize=8.5, color=INK_2, ha="right", va="top")
    ax.legend(loc="lower left", handlelength=1.6, borderaxespad=0.2)
    ax.text(3.25, 0.68, r"$\xi$ = %.2f" "\n" r"$S^Q = (S^P)^{\xi}$" % dec["xi"], color=INK_2, fontsize=9,
            ha="left", va="center")
    ax.set_xlim(0, 5)
    ax.set_ylim(0.40, 1.0)
    ax.set_xlabel("Years")
    ax.set_ylabel("Probability of surviving")
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{v * 100:.0f}%"))

    ax = axes[1]
    parts = [("Expected\nloss", dec["expected_loss"] * 1e4, C_P),
             ("Hazard\npremium", dec["hazard_premium"] * 1e4, C_Q),
             ("Recovery\npremium", dec["recovery_premium"] * 1e4, C_REC)]
    base = 0.0
    xs = np.arange(4)
    ax.set_axisbelow(True)
    for i, (lab, val, col) in enumerate(parts):
        ax.bar(i, val, bottom=base, width=0.62, color=col, zorder=3)
        ax.text(i, base + val + 22, f"{val:,.0f}", ha="center", va="bottom", fontsize=8.5, color=INK_2)
        ax.plot([i + 0.31, i + 0.69], [base + val, base + val], color=NEUTRAL, linewidth=0.8, zorder=2)
        base += val
    assert abs(base - HALV["spread"] * 1e4) < 1e-6                     # the three steps sum to the spread
    ax.bar(3, base, width=0.62, color=NEUTRAL, zorder=3)
    ax.text(3, base + 22, f"{base:,.0f}", ha="center", va="bottom", fontsize=8.5, color=INK_2)
    ax.set_xticks(xs, [p[0] for p in parts] + ["Spread"])
    ax.tick_params(axis="x", length=0)
    ax.set_ylabel("bp of the notes' spread")
    ax.set_ylim(0, 1300)
    ax.set_xlim(-0.55, 3.55)
    finish(fig, "ch06b_halvorsen_two_measures")
    return dec


# --------------------------------------------------------------------------------------------
# Figure 6-B.6  Halvorsen: the recovery bet with the default probability hedged out (step 5)
# --------------------------------------------------------------------------------------------
def fig_halvorsen_recovery_bet():
    lam_p = E["MeasuredPD"](HALV["pd_p"], "P", 1.0).hazard()
    lam_q = HALV["lam_q"]
    price, r_q, r_p = 78.0, 21.0, 40.0
    put_pts = price - r_q                              # 57 points of put payout per 100 face
    fig, axes = new_figure("panel2", ncols=2)

    ax = axes[0]
    R = np.linspace(0, 60, 61)
    ax.axhline(0, color=NEUTRAL, linewidth=0.9, zorder=1)
    ax.plot(R, R - price, color=NEUTRAL, linewidth=LW + 0.4, zorder=2, label="notes alone")
    ax.plot(R, R - r_q, color=BLUE, linewidth=LW + 0.4, zorder=3, label="notes plus 57 points of puts")
    mark_event(ax, r_q, "market: 21")
    mark_event(ax, r_p, "Theo: 40")
    ax.plot([r_p], [r_p - r_q], "o", color=BLUE, markersize=6, zorder=5, markeredgecolor="white")
    ax.annotate(f"+{r_p - r_q:.0f}", (r_p, r_p - r_q), xytext=(-7, 3), textcoords="offset points",
                fontsize=8.5, color=INK_2, ha="right", va="bottom")
    ax.legend(loc="lower right", handlelength=1.6, borderaxespad=0.2)
    ax.set_xlim(0, 60)
    ax.set_ylim(-82, 42)
    ax.set_xlabel("Recovery at default (cents per dollar)")
    ax.set_ylabel("Payoff at default (points)")
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{v:.0f}".replace("-", MINUS)))

    ax = axes[1]
    notes = lam_q * (price - r_q) - lam_p * (price - r_p)
    puts = -(lam_q - lam_p) * put_pts
    net = notes + puts
    assert abs(net - lam_p * (r_p - r_q)) < 1e-9
    bars = [("Notes:\nspread over\nexpected loss", 0.0, notes, GAIN),
            ("Puts:\nprice over\nexpected payout", notes, puts, LOSS),
            ("Net:\nthe recovery\nview alone", 0.0, net, NET)]
    ax.set_axisbelow(True)
    ax.axhline(0, color=NEUTRAL, linewidth=0.9, zorder=1)
    for i, (lab, bottom, val, col) in enumerate(bars):
        ax.bar(i, val, bottom=bottom, width=0.62, color=col, zorder=3)
        top = max(bottom, bottom + val)
        sign = "+" if val > 0 else MINUS
        ax.text(i, top + 0.15, f"{sign}{abs(val):.1f}", ha="center", va="bottom", fontsize=8.5, color=INK_2)
    ax.plot([0.31, 0.69], [notes, notes], color=NEUTRAL, linewidth=0.8, zorder=2)
    ax.plot([1.31, 1.69], [net, net], color=NEUTRAL, linewidth=0.8, zorder=2)
    ax.set_xticks(range(3), [b[0] for b in bars], fontsize=8)
    ax.tick_params(axis="x", length=0)
    ax.set_xlim(-0.55, 2.55)
    ax.set_ylim(-0.6, 7.0)
    ax.set_ylabel("Excess return (points per year)")
    finish(fig, "ch06b_halvorsen_recovery_bet")
    return notes, puts, net


if __name__ == "__main__":
    mean = fig_gamma_rent()
    print("gamma rent mean P&L by realized vol 10..50:", [round(float(m), 2) for m in mean])
    fig_merton_bond_greeks()
    print("jtd floor, bound at K/F=0.2, implied vol there:", fig_jtd_put_floor_and_wing())
    print("decomposition:", fig_halvorsen_two_measures())
    print("recovery bet (notes, puts, net):", fig_halvorsen_recovery_bet())
