"""Chapter 21 figures: Leveraged Loans, CLOs & Loan-Market Microstructure.

Run from anywhere:  python3 tools/figures/ch21.py
Writes assets/figures/ch21_*.png (five figures, in order of appearance in the chapter).

Data policy (see style.py). Fig 1 plots settlement conventions and observed medians exactly as the chapter cites them
(Moyer 2004; LSTA delayed-comp protocol via Markets Media, 2016; an LSTA ten-year average read off a chart, which the
chapter itself flags as approximate). Figs 2-5 are generated from the models and worked examples stated in the chapter
(eqs 21.3, 21.5-21.9 and the synthetic deal of Listing 21.1) and their captions say "Illustrative".
No external download is needed.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from style import *  # noqa: F401,F403,E402  (applies the rcParams on import)

import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402
from matplotlib.patches import FancyArrowPatch, Rectangle  # noqa: E402

# Chapter-wide colour roles. A role keeps its colour in every figure.
C_LOAN = BLUE            # the loan / the performing asset / the "now" observation
C_COST = ORANGE          # the penalty, the loss, the stressed state, equity
C_OLD = NEUTRAL          # superseded or reference marks
NEG = "#e66767"          # DIVERGING red end: a negative number
TINT_DEAD = "#efeeea"
TINT_DC = "#fbe6dc"


# --------------------------------------------------------------------------------------------------------------
# Figure 21.1: the settlement clock (conventions and observations, in business days)
# --------------------------------------------------------------------------------------------------------------
def fig_settlement_clock():
    fig, ax = new_figure("wide")
    xmax = 25.5
    ax.axvspan(0, 7, color=TINT_DEAD, zorder=0)
    ax.axvspan(7, xmax, color=TINT_DC, zorder=0)
    ax.text(3.5, 3.62, "dead zone: nobody\nis compensated", ha="center", va="bottom", fontsize=8.2, color=INK_2)
    ax.text(16.2, 3.62, "delayed compensation: the seller carries the loan\nand the buyer owes base rate on price (a forced repo)",
            ha="center", va="bottom", fontsize=8.2, color=INK_2)

    rows = {"Bonds": 3.0, "Loans: convention": 2.0, "Loans: observed": 1.0}

    def dot(x, y, txt, color, dx=0, dy=9, ha="center", va="bottom", strong=False):
        ax.plot([x], [y], "o", color=color, markersize=7 if strong else 5.5, zorder=5)
        if txt:
            ax.annotate(txt, (x, y), xytext=(dx, dy), textcoords="offset points", ha=ha, va=va, fontsize=8.2,
                        color=INK if strong else INK_2, zorder=6)

    # bonds: T+3 -> T+2 -> T+1
    y = rows["Bonds"]
    ax.plot([3, 1], [y, y], color=C_OLD, linewidth=1.0, zorder=3)
    dot(3, y, "T+3 (to 2017)", C_OLD, dx=6, dy=0, ha="left", va="center")
    dot(2, y, "T+2 (2017)", C_OLD, dy=-9, va="top")
    dot(1, y, "T+1 (28 May 2024)", C_LOAN, strong=True, dx=-4, ha="left")

    # loan conventions: T+10 par in 2004 -> T+7 today
    y = rows["Loans: convention"]
    ax.plot([10, 7], [y, y], color=C_OLD, linewidth=1.0, zorder=3)
    dot(10, y, "T+10 par (Moyer, 2004)", C_OLD, dy=-9, va="top")
    dot(7, y, "T+7 par (LSTA convention)", C_LOAN, strong=True, dx=-4, ha="left")
    ax.plot([5, 5], [y - 0.14, y + 0.14], color=INK_2, linewidth=1.2, zorder=4)
    ax.annotate("T+5: buyer's\npapers due", (5, y), xytext=(-5, 0), textcoords="offset points", ha="right",
                va="center", fontsize=8.0, color=INK_2)

    # loans observed: median 12 -> 9 (Sept 2016 protocol), average about 20 (2015-2025)
    y = rows["Loans: observed"]
    ax.add_patch(FancyArrowPatch((11.6, y), (9.4, y), arrowstyle="-|>", mutation_scale=9, linewidth=1.1,
                                 color=C_OLD, shrinkA=0, shrinkB=0, zorder=3))
    dot(12, y, "T+12 median\n(Jan\u2013Aug 2016)", C_OLD, dx=-4, ha="left")
    dot(9, y, "T+9 median (Sep 2016,\nafter the protocol)", C_OLD, dx=-4, dy=-9, ha="left", va="top")
    dot(20, y, "about T+20\n(average, 2015\u20132025)", C_COST, strong=True)

    ax.set_xlim(0, xmax)
    ax.set_ylim(0.35, 4.35)
    ax.set_yticks(list(rows.values()))
    ax.set_yticklabels(list(rows.keys()))
    ax.tick_params(axis="y", length=0)
    ax.set_xticks([0, 5, 10, 15, 20, 25])
    ax.set_xticklabels(["T", "T+5", "T+10", "T+15", "T+20", "T+25"])
    ax.grid(False)
    ax.spines["left"].set_visible(False)
    ax.set_xlabel("Business days from trade date to settlement")
    return finish(fig, "ch21_settlement_clock")


# --------------------------------------------------------------------------------------------------------------
# Figure 21.2: the CLO stack and the excess-spread waterfall, with the chapter's worked 2025 deal (eq 21.3)
# --------------------------------------------------------------------------------------------------------------
def fig_clo_arbitrage():
    fig, (a, b) = new_figure("wide", ncols=2, gridspec_kw={"width_ratios": [1.0, 1.45]})
    fig.set_size_inches(7.0, 3.7)

    # Left: the liabilities as a share of collateral par, senior at the top
    classes = [("Equity", 9, None), ("BB", 5, 575), ("BBB", 5, 310), ("A", 8, 210), ("AA", 11, 175), ("AAA", 62, 130)]
    cols = [C_COST, SEQ_BLUE_STEPS[3], SEQ_BLUE_STEPS[5], SEQ_BLUE_STEPS[7], SEQ_BLUE_STEPS[10], SEQ_BLUE_STEPS[12]]
    bottom = 0.0
    for (name, w, spr), col in zip(classes, cols):
        a.bar([0], [w], bottom=bottom, width=0.55, color=col, edgecolor="white", linewidth=1.2, zorder=3)
        label = f"{name}  {w}%" + (f"  ·  SOFR + {spr} bp" if spr else "  ·  residual")
        a.text(0.34, bottom + w / 2, label, va="center", ha="left", fontsize=8.3, color=INK_2)
        bottom += w
    a.set_xlim(-0.35, 1.75)
    a.set_ylim(0, 100)
    a.set_xticks([])
    a.set_ylabel("Share of collateral par (%)")
    a.grid(False)
    a.spines["bottom"].set_visible(False)

    # Right: where the 319 bp of collateral spread goes (bp of collateral par per year)
    was, liab, fees, el = 319.0, 160.9, 45.0, 75.0
    left = was - liab - fees - el          # 38.1
    steps = [
        ("Asset\nspread\n(WAS)", 0.0, was, C_LOAN, f"{was:.0f}"),
        ("Pays the\nnotes", was - liab, was, C_OLD, f"−{liab:.0f}"),
        ("Fees", was - liab - fees, was - liab, C_OLD, f"−{fees:.0f}"),
        ("Expected\nloss", left, was - liab - fees, C_OLD, f"−{el:.0f}"),
        ("Left for\nequity", 0.0, left, C_COST, f"{left:.0f}"),
        ("After a\n50 bp\nrepricing", left - 50.0, 0.0, NEG, f"{left - 50:.0f}".replace("-", "−")),
    ]
    xs = np.arange(len(steps))
    for x, (_t, lo, hi, col, txt) in zip(xs, steps):
        b.bar([x], [hi - lo], bottom=lo, width=0.62, color=col, zorder=3)
        if hi - lo and lo < 0:
            b.annotate(txt, (x, lo), xytext=(0, -3), textcoords="offset points", ha="center", va="top", fontsize=8.6,
                       color=INK)
        else:
            b.annotate(txt, (x, hi), xytext=(0, 3), textcoords="offset points", ha="center", va="bottom", fontsize=8.6,
                       color=INK)
    # connectors
    levels = [was, was - liab, was - liab - fees, left]
    for i, lv in enumerate(levels):
        b.plot([i + 0.31, i + 1 - 0.31], [lv, lv], color=NEUTRAL, linewidth=0.8, zorder=2)
    b.axhline(0, color=INK_2, linewidth=0.9, zorder=2)
    for yy, col, l1, l2 in ((352, C_COST, "Left for equity: 38 bp", "÷ 9% equity = +4.2% over SOFR"),
                            (292, NEG, "After a 50 bp repricing: −12 bp", "÷ 9% equity = −1.3%, a 5.6-pt fall")):
        b.add_patch(Rectangle((1.72, yy - 30), 0.14, 40, facecolor=col, edgecolor="none", zorder=3))
        b.text(2.0, yy, l1, ha="left", va="center", fontsize=8.2, color=INK_2)
        b.text(2.0, yy - 22, l2, ha="left", va="center", fontsize=8.2, color=INK_2)
    b.set_xticks(xs)
    b.set_xticklabels([s_[0] for s_ in steps], fontsize=7.8)
    b.tick_params(axis="x", length=0)
    b.set_ylim(-40, 375)
    b.set_xlim(-0.55, len(steps) - 0.45)
    b.set_ylabel("bp of collateral par per year")
    return finish(fig, "ch21_clo_arbitrage")


# --------------------------------------------------------------------------------------------------------------
# Figure 21.3: the CCC cliff and the cure trade, on the synthetic deal of Listing 21.1 (eqs 21.5, 21.6)
# --------------------------------------------------------------------------------------------------------------
CCC_LIMIT = 0.075
TOL = 1e-9


def ccc_excess_haircut(par_ccc, px_ccc, limit_par):
    """Listing 21.1: haircut (par minus market value) on the CCC excess, cheapest CCC loans first."""
    par_ccc = np.asarray(par_ccc, dtype=float)
    px_ccc = np.asarray(px_ccc, dtype=float)
    excess = max(0.0, float(par_ccc.sum()) - limit_par)
    if excess <= TOL:
        return 0.0, 0.0, float("nan")
    order = np.argsort(px_ccc, kind="stable")
    haircut, remaining, p_marg = 0.0, excess, float("nan")
    for p, n in zip(px_ccc[order], par_ccc[order]):
        take = min(n, remaining)
        haircut += max(0.0, 1.0 - p) * take
        remaining -= take
        p_marg = float(p)
        if remaining <= TOL:
            break
    return haircut, excess, p_marg


def acpa(pool, cash=0.0, ccc_limit=CCC_LIMIT):
    """Listing 21.1: adjusted collateral principal amount, eq (21.5)."""
    par = pool["par"].to_numpy(float)
    px = pool["price"].to_numpy(float)
    rec = pool["agency_rec"].to_numpy(float)
    p0 = pool["purchase_px"].to_numpy(float)
    dflt = pool["is_default"].to_numpy(bool)
    disc = pool["is_discount"].to_numpy(bool) & ~dflt
    ccc = pool["is_ccc"].to_numpy(bool) & ~dflt & ~disc
    h_def = float(np.sum(par[dflt] * (1.0 - np.minimum(px[dflt], rec[dflt]))))
    h_disc = float(np.sum(par[disc] * (1.0 - np.minimum(p0[disc], 1.0))))
    base = float(par[~dflt].sum())
    h_ccc, x_ccc, p_marg = ccc_excess_haircut(par[ccc], px[ccc], ccc_limit * base)
    value = float(par.sum()) + cash - h_def - h_disc - h_ccc
    return {"acpa": value, "h_ccc": h_ccc, "ccc_excess": x_ccc, "p_marg": p_marg}


def make_pool(n_loans=250, par_each=2.0, n_ccc=21, n_default=2, n_disc=3, seed=21):
    """Synthetic 500mm pool of Listing 21.1: CCC prices span 50-92 cents (illustrative)."""
    rng = np.random.default_rng(seed)
    price = np.clip(rng.normal(0.985, 0.012, n_loans), 0.93, 1.005)
    is_ccc = np.zeros(n_loans, bool)
    is_default = np.zeros(n_loans, bool)
    is_disc = np.zeros(n_loans, bool)
    is_ccc[:n_ccc] = True
    price[:n_ccc] = np.linspace(0.50, 0.92, n_ccc)
    is_default[n_ccc:n_ccc + n_default] = True
    price[n_ccc:n_ccc + n_default] = 0.40
    d0 = n_ccc + n_default
    is_disc[d0:d0 + n_disc] = True
    price[d0:d0 + n_disc] = 0.86
    return pd.DataFrame({
        "par": np.full(n_loans, par_each), "price": price, "is_ccc": is_ccc, "is_default": is_default,
        "agency_rec": np.full(n_loans, 0.45), "is_discount": is_disc,
        "purchase_px": np.where(is_disc, 0.80, 1.0)})


def sell_and_rebuy_par(pool, idx):
    row = pool.loc[idx]
    new = pd.DataFrame({"par": [row["par"] * row["price"]], "price": [1.0], "is_ccc": [False], "is_default": [False],
                        "agency_rec": [0.45], "is_discount": [False], "purchase_px": [1.0]})
    return pd.concat([pool.drop(index=idx), new], ignore_index=True)


def fig_ccc_cliff_and_cure():
    fig, (a, b) = new_figure("wide", ncols=2, gridspec_kw={"width_ratios": [1.0, 1.05]})
    fig.set_size_inches(7.0, 3.5)

    # Left: haircut as CCC par grows. A $500mm deal with no defaults; CCC loans of $2mm with prices on a ladder
    # from 50 to 92 cents, arriving cheapest first (old CCCs sit in the book, fresh downgrades arrive richest).
    base_par = 500.0
    limit_par = CCC_LIMIT * base_par
    ladder = np.linspace(0.50, 0.92, 30)
    C = np.linspace(0.0, 60.0, 601)
    H = []
    for c in C:
        k = int(c // 2.0)
        par = np.r_[np.full(k, 2.0), [c - 2.0 * k]] if c - 2.0 * k > 1e-12 else np.full(k, 2.0)
        px = ladder[: len(par)]
        H.append(ccc_excess_haircut(par, px, limit_par)[0] if len(par) else 0.0)
    H = np.array(H)
    share = 100.0 * C / base_par
    a.axvspan(7.5, share[-1] + 0.4, color=TINT_DC, zorder=0)
    a.plot(share, H, color=C_COST, linewidth=LW, zorder=3)
    a.axvline(7.5, color=NEUTRAL, linewidth=0.9, linestyle=(0, (3, 3)), zorder=1)
    a.annotate("7.5% bucket limit", (7.5, 0.97), xycoords=("data", "axes fraction"), xytext=(-3, 0),
               textcoords="offset points", ha="right", va="top", fontsize=8.2, color=INK_2)
    a.text(3.75, 1.3, "bucket not full:\na new CCC\ncosts nothing", ha="center", va="bottom", fontsize=8.2, color=INK_2)
    xi = 10.1
    yi = float(np.interp(xi, share, H))
    a.annotate("bucket full: each\nextra $1 of CCC par\ncosts 1 − p*, about\n35–50 cents, charged\nto the cheapest CCCs\nalready held",
               (xi, yi), xytext=(0.3, 5.0), textcoords="data", ha="left", va="bottom", fontsize=8.0, color=INK_2,
               arrowprops=dict(arrowstyle="-", color=NEUTRAL, linewidth=0.8, shrinkA=2))
    a.plot([share[-1]], [H[-1]], "o", color=C_COST, markersize=4, zorder=5, clip_on=False)
    a.set_xlim(0, share[-1] + 0.4)
    a.set_ylim(0, 11)
    a.set_xlabel("CCC par (% of non-defaulted par)")
    a.set_ylabel("Haircut taken off ACPA ($mm)")

    # Right: the cure trade on the chapter's synthetic deal. Sell one $2mm CCC at market, buy a performing loan at par.
    pool = make_pool()
    res = acpa(pool)
    ccc_idx = list(pool.index[pool.is_ccc])
    px = pool.loc[ccc_idx, "price"].to_numpy()
    d = np.array([acpa(sell_and_rebuy_par(pool, i))["acpa"] - res["acpa"] for i in ccc_idx])
    p_star, n_i = res["p_marg"], 2.0
    # the excess set: cheapest loans whose par adds up to the excess
    n_in = int(np.ceil(res["ccc_excess"] / n_i - 1e-9))
    inside = np.zeros(len(px), bool)
    inside[np.argsort(px)[:n_in]] = True
    pp = np.linspace(p_star, 0.93, 50)
    bound = n_i * ((pp - p_star) - CCC_LIMIT * (1 - p_star) * (1 - pp))
    b.axhline(0, color=INK_2, linewidth=0.9, zorder=2)
    b.plot(pp * 100, bound, color=NEUTRAL, linewidth=1.2, linestyle=(0, (4, 3)), zorder=2)
    b.plot(px[~inside] * 100, d[~inside], "o", color=C_LOAN, markersize=5.5, zorder=4)
    b.plot(px[inside] * 100, d[inside], "o", color=C_COST, markersize=5.5, zorder=4)
    b.annotate(f"sell the richest:\n{d.max():+.2f} $mm", (92.4, d.max() - 0.03), xytext=(95.5, 0.42), textcoords="data",
               ha="right", va="top", fontsize=8.2, color=INK_2,
               arrowprops=dict(arrowstyle="-", color=NEUTRAL, linewidth=0.8, shrinkA=1, shrinkB=0,
                               connectionstyle="arc3,rad=0"))
    b.text(57.0, -0.10, "sell the cheapest: about zero. It turns a\nhaircut into a realized loss, and cures nothing",
           ha="left", va="center", fontsize=8.2, color=INK_2)
    b.plot([], [], "o", color=C_COST, markersize=5.5, linestyle="none", label="inside the excess set")
    b.plot([], [], "o", color=C_LOAN, markersize=5.5, linestyle="none", label="above it")
    b.plot([], [], color=NEUTRAL, linewidth=1.2, linestyle=(0, (4, 3)), label="lower bound (21.6)")
    b.legend(loc="upper left", fontsize=8.0, handletextpad=0.2, borderaxespad=0.3)
    b.set_xlim(47, 96)
    b.set_ylim(-0.2, 0.98)
    b.set_xlabel("Price of the CCC loan sold (cents)")
    b.set_ylabel("Change in ACPA ($mm)")
    return finish(fig, "ch21_ccc_cliff_and_cure")


# --------------------------------------------------------------------------------------------------------------
# Figure 21.4: a par loan is a floater that is short a call (eqs 21.2, 21.7)
# --------------------------------------------------------------------------------------------------------------
def annuity(T, rate):
    return (1.0 - np.exp(-rate * T)) / rate


def fig_loan_short_call():
    fig, ax = new_figure("wide")
    y, T = 0.0665, 3.0                       # flat discount rate and expected life of the chapter's example
    gap = np.linspace(-120, 150, 271)        # s - m in bp: negative = market spread tighter than the margin
    mm = -gap / 1e4                          # m - s as a decimal

    def price(h):
        # eq (21.7) while the call is in the money (m > s); eq (21.2) otherwise
        return 100.0 * (1.0 + mm * np.where(mm > 0, annuity(T, y + h), annuity(T, y)))

    ax.axhline(100.0, color=INK_2, linewidth=0.9, zorder=2)
    ax.axvline(0, color=NEUTRAL, linewidth=0.9, linestyle=(0, (3, 3)), zorder=1)
    ax.axhline(101.0, color=NEUTRAL, linewidth=0.9, linestyle=(0, (1, 3)), zorder=1)
    ax.text(147, 101.06, "101: cap inside the soft call", ha="right", va="bottom", fontsize=8.0, color=MUTED)

    ax.plot(gap, price(0.0), color=C_OLD, linewidth=LW, linestyle=(0, (4, 3)), zorder=3,
            label="no call, eq. (21.2): 2.7  (101.36)")
    ax.plot(gap, price(1.0), color=C_LOAN, linewidth=LW, zorder=4,
            label="h = 1, repricing expected within a year: 0.9  (100.45)")
    ax.plot(gap, price(4.0), color=C_COST, linewidth=LW, zorder=5, label="h = 4, window open: 0.25  (100.12)")
    ax.legend(loc="lower left", bbox_to_anchor=(0.0, 0.03), fontsize=8.2, handlelength=2.2, borderaxespad=0.3,
              title="Points gained per 100 bp of tightening (dot: price at m \u2212 s = 50 bp)", title_fontsize=8.2, alignment="left")

    # the three prices quoted in the chapter at m - s = 50 bp
    for h in (0.0, 1.0, 4.0):
        pv = float(100.0 * (1.0 + 0.005 * annuity(T, y + h)))
        ax.plot([-50], [pv], "o", color=INK_2, markersize=3.8, zorder=6)
    ax.annotate("m \u2212 s = 50 bp", (-50, 103.55), ha="center", va="top", fontsize=7.8, color=MUTED)
    ax.plot([-50, -50], [100.0, 103.2], color=GRID, linewidth=0.8, zorder=0)

    ax.annotate("widening: the three lines coincide,\n2.7 points per 100 bp whatever h is", (148, 100.12),
                ha="right", va="bottom", fontsize=8.2, color=INK_2)
    ax.set_xlim(-120, 150)
    ax.set_ylim(95.5, 103.8)
    ax.set_xlabel("Market spread s minus contractual margin m (bp); left of zero the borrower's call is in the money")
    ax.set_ylabel("Loan price (points of par)")
    return finish(fig, "ch21_loan_short_call")


# --------------------------------------------------------------------------------------------------------------
# Figure 21.5: the redemption buffer as a queue (eq 21.9)
# --------------------------------------------------------------------------------------------------------------
def window_var(ell, sigma_f, phi):
    """Eq (21.9) with the stationary variance sigma_f**2 given directly."""
    k = np.arange(1, ell)
    return sigma_f ** 2 * (ell + 2.0 * np.sum((ell - k) * phi ** k))


def buffer_needed(ell, mu, sigma_f, phi, z=2.326):
    return ell * mu + z * np.sqrt(window_var(ell, sigma_f, phi))


def fig_buffer_queue():
    fig, ax = new_figure((7.0, 3.7))
    mu = 0.05                                   # % of NAV per day: mean net redemption
    sig_innov = 0.40                            # % of NAV per day: innovation s.d. at phi = 0.4
    sigma_f = sig_innov / np.sqrt(1 - 0.4 ** 2)  # same daily volatility for every phi
    ells = np.arange(1, 26)
    specs = [(0.0, SEQ_BLUE_STEPS[4], "\u03c6 = 0: independent\ndays, grows like \u221a\u2113"),
             (0.4, SEQ_BLUE_STEPS[7], "\u03c6 = 0.4: the\nchapter's calibration"),
             (0.7, SEQ_BLUE_STEPS[11], "\u03c6 = 0.7: persistent\noutflows, a sell-off")]
    for phi, col, txt in specs:
        v = np.array([buffer_needed(int(l), mu, sigma_f, phi) for l in ells])
        ax.plot(ells, v, color=col, linewidth=LW, zorder=3)
        ax.plot([ells[-1]], [v[-1]], "o", color=col, markersize=4, zorder=5, clip_on=False)
        ax.annotate(txt, (ells[-1], v[-1]), xytext=(6, 0), textcoords="offset points", va="center", fontsize=8.2,
                    color=INK_2)

    ax.axhline(4.5, color=C_COST, linewidth=1.2, linestyle=(0, (4, 3)), zorder=2)
    ax.annotate("median bank-loan\nfund liquidity ratio,\nabout 4.5%", (25, 4.5), xytext=(6, 0), textcoords="offset points",
                ha="left", va="center", fontsize=8.2, color=INK_2)
    for l, lab in ((1, "bond fund\nT+1"), (7, "loan convention\nT+7"), (20, "observed\nabout T+20")):
        ax.axvline(l, color=NEUTRAL, linewidth=0.9, linestyle=(0, (3, 3)), zorder=1)
        ax.annotate(lab, (l, 0.995), xycoords=("data", "axes fraction"), xytext=(3, 0), textcoords="offset points",
                    ha="left", va="top", fontsize=8.0, color=INK_2)
    spots = {1: (8, -12, "left", "top"), 7: (8, -3.5, "left", "center"), 20: (-8, 7, "right", "bottom")}
    for l, (dx, dy, ha, va) in spots.items():
        v = buffer_needed(l, mu, sigma_f, 0.4)
        ax.plot([l], [v], "o", markerfacecolor="white", markeredgecolor=SEQ_BLUE_STEPS[7], markeredgewidth=1.5,
                markersize=6, zorder=6)
        ax.annotate(f"{v:.2f}%", (l, v), xytext=(dx, dy), textcoords="offset points", ha=ha, va=va, fontsize=8.2,
                    color=INK, bbox=dict(facecolor="white", edgecolor="none", pad=0.8, alpha=0.85), zorder=7)
    ax.set_xlim(0, 25)
    ax.set_ylim(0, 14)
    ax.set_xticks([1, 5, 7, 10, 15, 20, 25])
    ax.set_xlabel("Settlement lag \u2113 (business days between selling a loan and receiving the cash)")
    ax.set_ylabel("Cash buffer for the 99% window (% of NAV)")
    return finish(fig, "ch21_buffer_queue")


if __name__ == "__main__":
    fig_settlement_clock()
    fig_clo_arbitrage()
    fig_ccc_cliff_and_cure()
    fig_loan_short_call()
    fig_buffer_queue()
