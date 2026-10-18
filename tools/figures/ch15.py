"""Chapter 15 figures: Event-Driven M&A, Regulatory Spreads & Change-of-Control.

Run:  python3 tools/figures/ch15.py      (writes assets/figures/ch15_*.png)

Color map used across this chapter (fixed order, SERIES slots):
  deal closes = BLUE, deal abandoned = ORANGE, litigated block = AQUA   (Figures 15.1, 15.4)
  strategic acquirer = BLUE, sponsor LBO = ORANGE                       (Figure 15.2)
  legacy bonds = BLUE, deal events = ORANGE, loans and financing = AQUA (Figure 15.5)
"""
import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from style import *  # noqa: F401,F403  (applies the rcParams on import)
import datetime as dt

import numpy as np
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle
import matplotlib.dates as mdates

CLOSE_C, ABANDON_C, BLOCK_C = BLUE, ORANGE, AQUA


# ---------------------------------------------------------------------------------------------
# Figure 15.1: the clause map (schematic)
# ---------------------------------------------------------------------------------------------
def _box(ax, x, y, w, h, text_lines, edge=NEUTRAL, face="white", ls="-", strip=None, fs=7.6,
         styles=None, pad_x=1.6):
    """Rounded box centred on (x, y); text_lines top to bottom. styles: per-line (color, weight, fontstyle)."""
    p = FancyBboxPatch((x - w / 2, y - h / 2), w, h, boxstyle="round,pad=0,rounding_size=1.2",
                       linewidth=0.9, edgecolor=edge, facecolor=face, linestyle=ls, zorder=2)
    ax.add_patch(p)
    if strip is not None:
        ax.add_patch(Rectangle((x - w / 2, y - h / 2 + 0.9), 1.1, h - 1.8, facecolor=strip, linewidth=0, zorder=3))
    n = len(text_lines)
    step = h / (n + 0.5)
    for i, t in enumerate(text_lines):
        yy = y + h / 2 - (i + 0.75) * step
        col, wt, fst = (styles[i] if styles else ((INK, "bold", "normal") if i == 0 else (INK_2, "normal", "normal")))
        ax.text(x - w / 2 + pad_x + (1.0 if strip is not None else 0), yy, t, fontsize=fs, color=col,
                fontweight=wt, fontstyle=fst, va="center", ha="left", zorder=4)


def _arrow(ax, p0, p1, color=MUTED, ls="-", lw=1.0, zorder=1, head=True):
    a = FancyArrowPatch(p0, p1, arrowstyle="-|>" if head else "-", mutation_scale=8, linewidth=lw, color=color,
                        linestyle=ls, zorder=zorder, shrinkA=0, shrinkB=0)
    ax.add_patch(a)


def fig_clause_map():
    fig, ax = new_figure((7.0, 5.2))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 82)
    ax.axis("off")
    ax.grid(False)
    I, M = (INK, "bold", "normal"), (INK_2, "normal", "normal")
    F = (INK_2, "normal", "italic")

    # left: signing -> clock -> outcomes (bus at x = 35)
    _box(ax, 5.8, 28, 11, 10, ["Deal signed", "(date t\u2080)"], fs=7.6, styles=[I, M])
    _box(ax, 22.5, 28, 17.5, 19, ["Regulatory clock", "HSR wait,", "Second Request,", "EC Phase I/II,", "CFIUS, STB, court"],
         fs=7.0)
    _arrow(ax, (11.4, 28), (13.6, 28))
    outs = [("Closes at \u03c4$_c$", "hazard $h_c(t)$", 42.0, CLOSE_C), ("Abandoned", "hazard $h_a(t)$", 18.5, ABANDON_C),
            ("Litigated block", "hazard $h_b(t)$", 6.5, BLOCK_C)]
    bus_x, ox, ow = 34.6, 45.9, 16.8
    _arrow(ax, (31.3, 28), (bus_x, 28), head=False)
    _arrow(ax, (bus_x, 6.5), (bus_x, 42.0), head=False)
    for lab, hz, y, c in outs:
        _box(ax, ox, y, ow, 8.4, [lab, hz], strip=c, fs=7.4, styles=[I, M])
        _arrow(ax, (bus_x, y), (ox - ow / 2 - 0.2, y))

    # right: clause boxes; closes bus at x = 56
    cx, cw, ch, bus2 = 79.5, 41.0, 8.6, 56.6
    close_rows = [
        (62.0, "1  Change-of-control put", "Holder: (101 + AI \u2212 P)\u207a by repurchase offer",
         "IG funds sell fallen angels; HY tender"),
        (52.0, "3  Make-whole / optional call", "Issuer pays max(PV at UST + spread, 100)",
         "Acquirer refinances target debt"),
        (42.0, "4  Convert fundamental-change put", "Par put plus a table conversion-rate bump",
         "Convert-arb unwind; delta collapses"),
        (32.0, "5  Loan change-of-control default", "Repaid at par, or refinanced as a consent",
         "CLO cash to reinvest; repricing"),
        (22.0, "6  CDS successor determination", "Reference entity reassigned, or orphaned",
         "Basis dislocation"),
    ]
    _arrow(ax, (ox + ow / 2, 42.0), (bus2, 42.0), color=CLOSE_C, head=False, lw=1.0)
    _arrow(ax, (bus2, 22.0), (bus2, 62.0), color=CLOSE_C, head=False, lw=1.0)
    for y, t0, t1, t2 in close_rows:
        _box(ax, cx, y, cw, ch, [t0, t1, t2], strip=CLOSE_C, fs=6.9, styles=[I, M, F])
        _arrow(ax, (bus2, y), (cx - cw / 2 - 0.2, y), color=CLOSE_C, lw=1.0)
    # break: abandoned and block feed the SMR
    _arrow(ax, (ox + ow / 2, 18.5), (bus2, 18.5), color=ABANDON_C, head=False)
    _arrow(ax, (ox + ow / 2, 6.5), (bus2, 6.5), color=BLOCK_C, head=False)
    _arrow(ax, (bus2, 6.5), (bus2, 18.5), color=MUTED, head=False)
    _box(ax, cx, 11.0, cw, ch, ["2  Special mandatory redemption", "Holder gets 101 + AI in cash within days",
                                 "Tranche holders reinvest; issuer funds"], strip=ABANDON_C, fs=6.9, styles=[I, M, F])
    _arrow(ax, (bus2, 11.0), (cx - cw / 2 - 0.2, 11.0), color=MUTED, lw=1.0)

    # issuer counter-options: dashed, can knock out entry 1
    _box(ax, cx, 73.6, cw, 6.4, ["Issuer counter-options", "Consent strip or defeasance, before the trigger"],
         edge=INK_2, ls=(0, (4, 3)), fs=6.9, styles=[I, M])
    _arrow(ax, (cx, 70.4), (cx, 66.5), color=INK_2, ls=(0, (3, 2)), lw=1.1, zorder=5)
    ax.text(cx + 1.4, 68.5, "can knock out clause 1", fontsize=6.8, color=INK_2, va="center", ha="left")

    ax.text(0.5, 79.8, "Deal outcome and clock", fontsize=7.6, color=MUTED, ha="left", va="center")
    ax.text(59.0, 79.8, "Cash flows that fire (italic: forced flow)", fontsize=7.6, color=MUTED, ha="left", va="center")
    ax.text(0.5, 1.2, "Clause numbers follow the table in Section 15.1.2", fontsize=7, color=MUTED, ha="left", va="center")
    return finish(fig, "ch15_deal_clause_map")


# ---------------------------------------------------------------------------------------------
# Figure 15.2: coupon vintage and CoC put intrinsic value
# ---------------------------------------------------------------------------------------------
def _bond_price(coupon, T, y):
    """Continuously compounded flat yield y, semiannual coupons (percent of par p.a.), valued on a coupon date."""
    t = np.arange(0.5, T + 1e-9, 0.5)
    return float(np.sum(coupon / 2.0 * np.exp(-y * t)) + 100.0 * np.exp(-y * T))


def fig_vintage():
    T, ust, K = 4.5, 0.044, 101.0
    cases = {"Strategic buyer, 60bp": (ust + 0.0060, BLUE), "Sponsor LBO, 350bp": (ust + 0.0350, ORANGE)}
    cs = np.linspace(0.0, 9.0, 361)
    fig, ax = new_figure("wide")
    ends = {}
    for name, (y, col) in cases.items():
        intrinsic = np.array([max(K - _bond_price(c, T, y), 0.0) for c in cs])
        ax.plot(cs, intrinsic, color=col)
        ends[name] = (y, col, intrinsic)
        # break-even coupon c*
        ann = 0.5 * np.sum(np.exp(-y * np.arange(0.5, T + 1e-9, 0.5)))
        cstar = (K - 100.0 * np.exp(-y * T)) / ann
        ax.plot([cstar], [0], "o", color=col, markersize=6, clip_on=False, zorder=5)
        right = col == ORANGE
        ax.annotate("$c^*$", (cstar, 0), xytext=(0, 9), textcoords="offset points", ha="center", fontsize=9,
                    color=INK_2)
    # vintages (the three bonds of the grid in Section 15.2.2)
    y_lbo = cases["Sponsor LBO, 350bp"][0]
    for c, lab, dx in [(1.85, "2021 vintage\n1.85%", 0), (5.00, "2023 vintage\n5.00%", 0), (6.875, "2009-style\n6.875%", 0)]:
        ax.axvline(c, color=NEUTRAL, linewidth=0.9, linestyle=(0, (3, 3)), zorder=1)
        v = max(K - _bond_price(c, T, y_lbo), 0.0)
        ax.plot([c], [v], "o", color=ORANGE, markersize=6, zorder=6, markeredgecolor="white")
        ax.annotate(f"\u2248{v:.0f}", (c, v), xytext=(6, 4), textcoords="offset points", fontsize=8.5,
                    color=INK, fontweight="bold", ha="left", va="bottom")
        ax.annotate(lab, (c, 1.0), xycoords=("data", "axes fraction"), xytext=(4, -2), textcoords="offset points",
                    fontsize=8, color=INK_2, va="top", ha="left")
    # direct line labels
    ax.annotate("Sponsor LBO (350bp)", (3.15, ends["Sponsor LBO, 350bp"][2][int(3.15 / 9 * 360)]),
                xytext=(8, 10), textcoords="offset points", fontsize=8.5, color=INK_2, ha="left", va="bottom")
    ax.plot([3.15], [ends["Sponsor LBO, 350bp"][2][int(3.15 / 9 * 360)]], "o", color=ORANGE, markersize=4, zorder=5)
    ax.annotate("Strategic buyer (60bp)", (2.8, ends["Strategic buyer, 60bp"][2][int(2.8 / 9 * 360)]),
                xytext=(-6, -10), textcoords="offset points", fontsize=8.5, color=INK_2, ha="right", va="top")
    ax.plot([2.8], [ends["Strategic buyer, 60bp"][2][int(2.8 / 9 * 360)]], "o", color=BLUE, markersize=4, zorder=5)
    ax.set_xlim(0, 9)
    ax.set_ylim(0, 36)
    ax.set_xlabel("Coupon (% of par)")
    ax.set_ylabel("Put intrinsic value if triggered (points per 100)")
    ax.text(0.99, 0.55, "$c^*$ = break-even coupon\n4.5 years left\nTreasury zero 4.4%, flat\nstrike 101", transform=ax.transAxes,
            ha="right", va="center", fontsize=8, color=MUTED, linespacing=1.3)
    return finish(fig, "ch15_coupon_vintage_put")


# ---------------------------------------------------------------------------------------------
# Figure 15.3: the SMR gauge
# ---------------------------------------------------------------------------------------------
def fig_smr_gauge():
    # worked example of Section 15.4.2: 4.60% tranche, T_f = 0.25, y_f = 4.60%
    c, Tf, yf = 4.60, 0.25, 0.046
    g_f = (100.0 + 1.0 + c * Tf) * np.exp(-yf * Tf)          # 102.15 * exp(-0.0115)
    pi = np.linspace(0, 1, 101)
    fig, axs = new_figure("wide", ncols=2)
    ax = axs[0]
    scen = [(103.0, ORANGE, "Rates fell, $P^{close}$ = 103.0"),
            (100.98, NEUTRAL, None),
            (99.0, BLUE, "Rates rose, $P^{close}$ = 99.0")]
    for pc, col, lab in scen:
        ax.plot(100 * pi, pi * g_f + (1 - pi) * pc, color=col)
    ax.annotate("Rates fell ($P^{close}$ = 103.0):\nholder is short a digital", (0, 103.0), xytext=(8, 7),
                textcoords="offset points", ha="left", va="bottom", fontsize=8.2, color=INK_2)
    ax.annotate("$P^{close}$ = $G_f$: no information", (3, g_f), xytext=(0, 4),
                textcoords="offset points", ha="left", va="bottom", fontsize=8.0, color=INK_2)
    ax.annotate("Rates rose ($P^{close}$ = 99.0):\nfree put on the deal", (97, 0.97 * g_f + 0.03 * 99.0),
                xytext=(0, -22), textcoords="offset points", ha="right", va="top", fontsize=8.2, color=INK_2)
    # worked example: P0 = 99.40 at pi = 0.20
    p_ex = 0.20 * g_f + 0.80 * 99.0
    ax.plot([20], [p_ex], "o", color=BLUE, markersize=7, markeredgecolor="white", zorder=6)
    ax.annotate("Quoted at 99.40:\n20% break probability", (20, p_ex), xytext=(6, -34), textcoords="offset points",
                fontsize=8.2, color=INK, fontweight="bold", ha="left", va="top",
                arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.7))
    ax.set_xlim(0, 100)
    ax.set_ylim(96.5, 105)
    ax.set_xlabel("Break probability $\\pi_f$ (%)")
    ax.set_ylabel("SMR tranche price (per 100)")

    ax = axs[1]
    gap = np.logspace(np.log10(0.02), np.log10(6), 300)
    err = np.minimum(0.10 / gap, 1.0)
    ax.plot(gap, 100 * err, color=BLUE)
    ax.set_xscale("log")
    ax.set_xlim(0.02, 6)
    ax.set_ylim(0, 105)
    ax.set_xticks([0.03, 0.1, 0.3, 1, 3])
    ax.set_xticklabels(["0.03", "0.1", "0.3", "1", "3"])
    ax.set_xlabel("$|P^{close} - G_f|$ (points, log scale)")
    ax.set_ylabel("Error in implied $\\hat\\pi_f$ (pp)")
    g_ex = 1.98
    ax.plot([g_ex], [100 * 0.10 / g_ex], "o", color=BLUE, markersize=7, markeredgecolor="white", zorder=6)
    ax.annotate("Worked example:\n1.98 apart, about 5 pp", (g_ex, 100 * 0.10 / g_ex), xytext=(-16, 34),
                textcoords="offset points", ha="center", va="bottom", fontsize=8.2, color=INK,
                arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.7))
    ax.axvspan(0.02, 0.1, color=GRID, zorder=0)
    ax.text(0.0425, 56, "switched off:\nreport 'no\ninformation'", fontsize=8.2, color=INK_2, ha="center", va="center")
    ax.text(0.99, 0.97, "from a 0.10-point price error", transform=ax.transAxes, ha="right", va="top",
            fontsize=8, color=MUTED)
    return finish(fig, "ch15_smr_gauge")


# ---------------------------------------------------------------------------------------------
# Figure 15.4: competing risks (seeded synthetic cohort of Listing 15.4)
# ---------------------------------------------------------------------------------------------
BETA_TRUE = {1: np.array([-1.20, -0.30, -0.15, -0.10, 0.20, -0.40]),
             2: np.array([0.60, 0.20, -0.10, 0.05, 0.30, 0.30]),
             3: np.array([1.50, 1.00, 0.20, 0.00, -0.50, 0.80])}
WEIBULL = {1: (1.6, 0.55), 2: (1.1, 6.0), 3: (1.3, 12.0)}


def _synthetic_cohort(n=600, seed=11):
    """Same generator as synthetic_deal_cohort in Listing 15.4 (Appendix F): returns time, cause (0 = pending)."""
    rng = np.random.default_rng(seed)
    X = np.column_stack([rng.binomial(1, 0.15, n), rng.binomial(1, 0.40, n), rng.standard_normal(n),
                         rng.poisson(2.0, n), rng.binomial(1, 0.30, n), rng.binomial(1, 0.50, n)]).astype(float)
    latent = np.column_stack([b * (rng.exponential(size=n) / np.exp(X @ BETA_TRUE[k])) ** (1.0 / a)
                              for k, (a, b) in WEIBULL.items()])
    t_event, cause = latent.min(axis=1), latent.argmin(axis=1) + 1
    t_cens = rng.uniform(0.5, 4.0, n)
    return np.minimum(t_event, t_cens), np.where(t_event <= t_cens, cause, 0)


def _risk_table(times, events):
    ut, d = np.unique(times[events == 1], return_counts=True)
    n_risk = times.size - np.searchsorted(np.sort(times), ut, side="left")
    return ut, n_risk, d


def _aalen_johansen(times, cause, n_causes=3):
    ut, n, d = _risk_table(times, (cause > 0).astype(int))
    S = np.cumprod(1.0 - d / n)
    S_minus = np.concatenate(([1.0], S[:-1]))
    out = {"t": ut, "S": S}
    for k in range(1, n_causes + 1):
        tk, ck = np.unique(times[cause == k], return_counts=True)
        dk = np.zeros(ut.size)
        dk[np.searchsorted(ut, tk)] = ck
        out[k] = np.cumsum(S_minus * dk / n)
    return out


def _naive_cumulative(times, cause, k):
    """1 - exp(-Lambda_k): cause-specific Nelson-Aalen hazard, other causes treated as if they never happen."""
    ut, n, d = _risk_table(times, (cause == k).astype(int))
    return ut, 1.0 - np.exp(-np.cumsum(d / n))


def fig_competing_risks():
    times, cause = _synthetic_cohort()
    aj = _aalen_johansen(times, cause)
    # identities as a built-in check
    tot = aj[1] + aj[2] + aj[3]
    assert np.max(np.abs(tot - (1.0 - aj["S"]))) < 1e-12
    tn, Fn = _naive_cumulative(times, cause, 1)

    fig, ax = new_figure("wide")
    tmax = 3.5
    t = np.concatenate(([0.0], aj["t"]))

    def step(y):
        return np.concatenate(([0.0], y))

    cols = {1: CLOSE_C, 2: ABANDON_C, 3: BLOCK_C}
    for k in (1, 2, 3):
        ax.step(t, 100 * step(aj[k]), where="post", color=cols[k])
    ax.step(np.concatenate(([0.0], tn)), 100 * np.concatenate(([0.0], Fn)), where="post", color=BLUE,
            linestyle=(0, (4, 2.5)), linewidth=1.3)
    ax.step(t, 100 * step(1.0 - aj["S"]), where="post", color=NEUTRAL, linestyle="-", linewidth=1.3)
    ax.set_xlim(0, tmax)
    ax.set_ylim(0, 100)

    def at(arr_t, arr_y, x):
        i = np.searchsorted(arr_t, x, side="right") - 1
        return 100 * (arr_y[i] if i >= 0 else 0.0)

    xe = tmax
    yc, ya, yb = at(aj["t"], aj[1], xe), at(aj["t"], aj[2], xe), at(aj["t"], aj[3], xe)
    yn = at(tn, Fn, xe)
    ytot = at(aj["t"], 1 - aj["S"], xe)
    label_end(ax, xe, yc, "Closes, $\\hat F_c$", CLOSE_C, dx=6)
    label_end(ax, xe, ya + 1.2, "Abandoned, $\\hat F_a$", ABANDON_C, dx=6, dy=3)
    label_end(ax, xe, yb - 1.2, "Litigated block, $\\hat F_b$", BLOCK_C, dx=6, dy=-3)
    ax.plot([xe], [yn], "o", color=BLUE, markersize=4, clip_on=False, zorder=5)
    ax.annotate("1 − exp(−Λ$_c$): ignores the other\nexits, overstates closing", (1.55, at(tn, Fn, 1.55)), xytext=(0.0, 14),
                textcoords="offset points", fontsize=8.2, color=INK_2, ha="left", va="bottom")
    ax.annotate("Total exits $1-\\hat S$ = sum of the three", (1.0, at(aj["t"], 1 - aj["S"], 1.0)), xytext=(-2, -16),
                textcoords="offset points", fontsize=8.2, color=INK_2, ha="right", va="top")
    ax.set_xlabel("Years since signing")
    ax.set_ylabel("Probability of exit by time t (%)")
    ax.text(0.01, 0.98, "Seeded 600-deal cohort, Listing 15.4", transform=ax.transAxes, fontsize=8, color=MUTED,
            ha="left", va="top")
    print(f"  competing risks: F_c={yc:.1f} F_a={ya:.1f} F_b={yb:.1f} tot={ytot:.1f} naive={yn:.1f} at {xe} yr; "
          f"pending share={np.mean(cause == 0):.2f}")
    return finish(fig, "ch15_competing_risks_incidence")


# ---------------------------------------------------------------------------------------------
# Figure 15.5: WBD timeline
# ---------------------------------------------------------------------------------------------
def fig_wbd_timeline():
    D = dt.date
    lanes = ["Legacy bonds", "Deal", "Loans and financing"]
    lane_col = {"Legacy bonds": BLUE, "Deal": ORANGE, "Loans and financing": AQUA}
    fig, ax = new_figure((7.0, 4.5))
    x0, x1 = mdates.date2num(D(2025, 5, 15)), mdates.date2num(D(2026, 11, 20))
    ax.set_xlim(x0, x1)
    ax.set_ylim(0, 3)
    ax.grid(False)
    for s in ("left", "bottom"):
        ax.spines[s].set_visible(False)
    ax.set_yticks([])
    ax.xaxis.set_major_locator(mdates.MonthLocator(bymonth=[1, 4, 7, 10]))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b\n%Y"))
    ax.tick_params(axis="x", length=3, color=NEUTRAL)
    # lane geometry: bonds on top
    lane_y = {"Legacy bonds": 2.5, "Deal": 1.45, "Loans and financing": 0.45}
    for ln in lanes:
        ax.axhline(lane_y[ln], color=GRID, linewidth=1.0, zorder=0)
        ax.text(x0 - 4, lane_y[ln] + 0.07, ln.upper(), fontsize=7.2, color=MUTED, ha="left", va="bottom")
    # events: (date, lane, label lines, label offset in y, ha)
    ev = [
        (D(2025, 6, 9), "Legacy bonds", "Jun 9: tender offers and\nconsent solicitations launched", +0.42, "left"),
        (D(2025, 6, 16), "Legacy bonds", None, 0, None),
        (D(2025, 6, 26), "Loans and financing", "Jun 26: $15bn bridge, titled\n'Non-Investment Grade'", +0.38, "left"),
        (D(2025, 12, 4), "Deal", "Dec 4: Netflix signs", +0.50, "left"),
        (D(2026, 1, 19), "Deal", "Jan 19: Netflix bid\nbecomes $27.75 cash", -0.30, "left"),
        (D(2026, 2, 27), "Deal", "Feb 27: Paramount Skydance\nsigns, $31.00 cash + ticking", +0.28, "left"),
        (D(2026, 4, 23), "Deal", "Apr 23: stockholders\napprove", -0.48, "left"),
        (D(2026, 6, 4), "Loans and financing", "Jun 4: $13bn + €1.7bn term\nloans B refinance the bridge", +0.38, "left"),
        (D(2026, 10, 6), "Deal", "Oct 6: closes at $31.0167\n(6 days of ticking from Sep 30)", -0.50, "right"),
    ]
    for d, ln, text, dy, ha in ev:
        x = mdates.date2num(d)
        y = lane_y[ln]
        ax.plot([x], [y], "o", color=lane_col[ln], markersize=7, markeredgecolor="white", zorder=5)
        if text is None:
            continue
        ty = y + dy
        ax.plot([x, x], [y, ty - np.sign(dy) * 0.07], color=NEUTRAL, linewidth=0.8, zorder=2)
        ax.text(x + (-2 if ha == "right" else 2), ty, text, fontsize=7.8, color=INK, ha=ha,
                va="bottom" if dy > 0 else "top", linespacing=1.15)
    # June 16 consent (strip) emphasized with a second label in the bond lane
    x = mdates.date2num(D(2025, 6, 16))
    ax.plot([x, x], [lane_y["Legacy bonds"], lane_y["Legacy bonds"] - 0.38], color=NEUTRAL, linewidth=0.8, zorder=2)
    ax.text(x + 2, lane_y["Legacy bonds"] - 0.40, "Jun 16: requisite consents in; covenants\nstripped from the legacy notes",
            fontsize=7.8, color=INK, ha="left", va="top", linespacing=1.15)
    # the gap: strip -> buyer chosen, as a double arrow in the bond lane
    xa, xb = mdates.date2num(D(2025, 6, 16)), mdates.date2num(D(2026, 2, 27))
    ya = 2.02
    ax.annotate("", (xb, ya), (xa, ya), arrowprops=dict(arrowstyle="<->", color=INK_2, lw=1.0, shrinkA=0, shrinkB=0))
    ax.text((xa + xb) / 2 + 40, ya + 0.07, "8 months from the strip to the winning bidder", fontsize=8, color=INK_2,
            ha="center", va="bottom")
    # ticking window sliver
    ax.axvspan(mdates.date2num(D(2026, 9, 30)), mdates.date2num(D(2026, 10, 6)), color=ORANGE, alpha=0.25, zorder=1, lw=0)
    fig.autofmt_xdate(rotation=0, ha="center")
    return finish(fig, "ch15_wbd_timeline")


if __name__ == "__main__":
    which = set(sys.argv[1:])
    for name, fn in [("map", fig_clause_map), ("vintage", fig_vintage), ("smr", fig_smr_gauge),
                     ("risks", fig_competing_risks), ("wbd", fig_wbd_timeline)]:
        if not which or name in which:
            fn()
