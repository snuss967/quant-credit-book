"""Chapter 8-D figures: The Pair Book: Long One Credit, Short Another.

Run:  python3 tools/figures/ch08d.py      (writes assets/figures/ch08d_*.png)

Order of appearance in the chapter (the numbers in the captions follow this order):
  8-D.1  ch08d_fee_flip            PB-19's expected year at a 25 bp fee and at 70 bp           (Cold Open)
  8-D.2  ch08d_borrow_fee          The loan-market slope and what signals do to the fee         (8D.2)
  8-D.3  ch08d_ruler_scenarios     Three rulers, four market states (existing embed)            (8D.3, after the table)
  8-D.4  ch08d_ben_dor_rulers      Ben Dor et al.: correlation vs systematic share, calm/crisis (8D.3, after the crisis box)
  8-D.5  ch08d_two_spikes          One year of jump P&L for the DTS-neutral Ford/GM pair        (8D.4)
  8-D.6  ch08d_stop_size_vs_recovery  The stop as a size (existing embed)                      (8D.5, after the sizing)
  8-D.7  ch08d_stop_out_odds       How often a 5% stop fires: fixed line vs drawdown            (8D.5, after the random-walk box)
  8-D.8  ch08d_pair_book_ledger    The Pair Book as a figure, twelve rows (existing embed)      (8D.6)

Data.  Figure 8-D.4 is REAL: Ben Dor, Dynkin, Hyman and Phelps, Quantitative Credit Portfolio Management,
Table 8.1 (Nov 2003 to Dec 2006, 392 same-industry CDX.NA.IG CDS pairs, 24-week betas) and Table 10.3
(2007-2008, 26-week betas), as transcribed in state/research/rv_credit_pairs_literature_and_mechanics.md (R7).
The right panel of 8-D.2 is REAL: Asquith, Au, Covert and Pathak (2013), same dossier (R11); the slope in
its left panel is the straight-line summary of that paper which the chapter states (30 bp flat to 70% on
loan, then 10 bp per further 10%), drawn as such, with PB-01 and PB-19 as the chapter's illustrative
observations.  All other figures are ILLUSTRATIVE and are computed from the chapter's own numbers:
8-D.1 (Cold Open), 8-D.3 (table in 8D.3), 8-D.5 (8D.4), 8-D.6 (8D.5) and 8-D.8 (8D.6); 8-D.7 simulates
200,000 years of 252 Gaussian daily steps (seed 4) for the bars, draws one path (seed 15) in its left panel, and
uses the reflection principle for the fixed line.
Figure 8-D.8: the chapter prints only four ledger rows (PB-01, PB-19, PB-03 and the PB-12 refusal).  Two more
(PB-09, PB-10) are drawn at the capture ratios state/rv_pair_book.md records (about 0.8 and 0.2); PB-02, PB-07 and
PB-11 are text rows because the ledger records no usable capture ratio for them; the last three (PB-08, PB-14,
PB-16) are generated here (seed 80) and the figure says so.

Colour roles, fixed across the chapter's figures:
  Rulers (8-D.3, 8-D.4):   BLUE = spread duration (DV01 / PV01), ORANGE = DTS, AQUA = empirical beta
  Money lines (8-D.1, 8-D.8):  BLUE = thesis / idio, ORANGE = leak, AQUA = friction
  Polarity of a jump P&L (8-D.5): dark blue = gain, dark red = loss (the DIVERGING end points)
  Stop figures (8-D.6, 8-D.7): BLUE = Dov's $13mm line and the equity path, ORANGE = the $15mm firing budget
                               and the stop line, AQUA = the capital-structure pair
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from style import *  # noqa: E402,F401,F403
import numpy as np  # noqa: E402
from math import erf, sqrt  # noqa: E402
from matplotlib.patches import Patch  # noqa: E402

plt.rcParams["text.parse_math"] = False      # dollar signs in labels are literal
plt.rcParams["axes.axisbelow"] = True        # grid lines sit behind the bars

MINUS = "−"
C_DV01, C_DTS, C_BETA = BLUE, ORANGE, AQUA
C_THESIS, C_LEAK, C_FRIC = BLUE, ORANGE, AQUA
C_GAIN, C_LOSS = DIVERGING(0.0), DIVERGING(1.0)


def sgn(v, d=0, plus=True):
    """Signed number with a true minus sign."""
    s = f"{abs(v):,.{d}f}"
    if abs(v) < 0.5 * 10 ** (-d):
        return s
    if v < 0:
        return MINUS + s
    return ("+" if plus else "") + s


def norm_cdf(z):
    return 0.5 * (1 + erf(z / sqrt(2)))


# --------------------------------------------------------------------------------------------
# 8-D.1  The lender changed, nothing else did
# --------------------------------------------------------------------------------------------
def fig_fee_flip():
    thesis = 4.5 * 0.0030 * 40_000        # $k a year: 4.5 x 30 bp x $40mm = 540
    fin, spreads = 160.0, 120.0           # financing the long; two legs' half-spreads over the hold
    borrow_old = 0.0025 * 60_000          # 25 bp on $60mm = 150
    borrow_new = 0.0070 * 60_000          # 70 bp on $60mm = 420
    assert abs(thesis - 540) < 1e-9 and abs(borrow_old - 150) < 1e-9 and abs(borrow_new - 420) < 1e-9
    assert abs((borrow_new + fin + spreads) - 700) < 1e-9          # the chapter's $700,000 of friction
    fig, axes = new_figure("wide", ncols=2, sharey=True)
    labels = ["Thesis:\n30 bp of gap", "Borrow\nfee", "Financing\nthe long", "Two half-\nspreads", "Net"]
    cols = [C_THESIS, C_FRIC, C_FRIC, C_FRIC, INK_2]
    for ax, borrow, ttl in zip(axes, (borrow_old, borrow_new), ("Fee at 25 bp (before the reset)",
                                                                 "Fee at 70 bp (Tuesday 6 October)")):
        deltas = [thesis, -borrow, -fin, -spreads]
        cum, level = 0.0, []
        for i, d in enumerate(deltas):
            lo, hi = (cum, cum + d) if d >= 0 else (cum + d, cum)
            ax.bar(i, hi - lo, bottom=lo, width=0.62, color=cols[i])
            cum += d
            level.append(cum)
            lab_y = hi + 12 if d >= 0 else lo - 20
            ax.text(i, lab_y, sgn(d), ha="center", va="bottom" if d >= 0 else "top", fontsize=8.5, color=INK_2)
        net = cum
        ax.bar(4, net, width=0.62, color=cols[4])
        ax.text(4, net + (12 if net >= 0 else -12), sgn(net), ha="center", va="bottom" if net >= 0 else "top",
                fontsize=9, color=INK, fontweight="bold")
        for i in range(4):          # connectors
            ax.plot([i + 0.31, i + 1 - 0.31], [level[i], level[i]], color=NEUTRAL, linewidth=0.8, zorder=1)
        ax.axhline(0, color=INK_2, linewidth=0.8, zorder=2)
        ax.set_xticks(range(5))
        ax.set_xticklabels(labels, fontsize=7.8)
        ax.set_title(ttl, fontsize=9.5)
        ax.set_ylim(-270, 650)
        ax.tick_params(axis="x", length=0)
    axes[0].set_ylabel("Expected P&L, $ thousands a year")
    fig.legend(handles=[Patch(color=C_THESIS, label="thesis"), Patch(color=C_FRIC, label="friction"),
                        Patch(color=INK_2, label="net")], loc="outside lower center", ncol=3, fontsize=8,
               handlelength=1.2, columnspacing=1.6)
    return finish(fig, "ch08d_fee_flip")


# --------------------------------------------------------------------------------------------
# 8-D.2  The loan-market slope, and the fee as a function of the signal
# --------------------------------------------------------------------------------------------
def fig_borrow_fee():
    fig, (a1, a2) = new_figure("wide", ncols=2)
    # left: Asquith et al. rule of thumb, as the chapter states it
    u = np.linspace(0, 100, 201)
    fee = np.where(u <= 70, 30.0, 30.0 + 1.0 * (u - 70.0))      # 10 bp per further 10% of inventory
    assert abs(float(np.interp(85, u, fee)) - 45.0) < 1e-9       # "something like 45 bp" at 85%
    a1.plot(u, fee, color=BLUE, linewidth=LW)
    a1.text(2, 26, "Asquith et al. slope: flat near 30 bp\nto 70% on loan, then 10 bp per\nfurther 10%", fontsize=8,
            color=INK_2, va="top", ha="left")
    a1.plot([85], [70], "o", color=ORANGE, markersize=6.5, zorder=5)
    a1.plot([85], [45], "o", color=BLUE, markersize=5, zorder=5)
    a1.annotate("", (85, 47.5), xytext=(85, 67.5), arrowprops=dict(arrowstyle="<->", color=INK_2, linewidth=0.9))
    a1.annotate("PB-19: 70 bp", (85, 70), xytext=(-8, 4), textcoords="offset points", ha="right", va="bottom",
                fontsize=8.5, color=INK_2)
    a1.annotate("slope says ~45", (85, 45), xytext=(6, -6), textcoords="offset points", ha="left", va="top",
                fontsize=8, color=INK_2)
    a1.plot([61], [50], "o", color=ORANGE, markersize=6.5, zorder=5)
    a1.annotate("PB-01: 50 bp", (61, 50), xytext=(-6, 5), textcoords="offset points", ha="right", va="bottom",
                fontsize=8.5, color=INK_2)
    a1.set_xlim(0, 102)
    a1.set_ylim(0, 90)
    a1.set_xlabel("Share of the lender's inventory on loan (%)")
    a1.set_ylabel("Annual borrow fee (bp)")
    # right: the fee as a function of the signal (Asquith et al. 2013)
    cats = [("Median bond", 18.0), ("Mean bond", 33.0), ("Before a one-letter\ndowngrade", 38.4),
            ("After it", 52.3), ("30 days before\nbankruptcy filing", 173.0), ("30 days after\nfiling", 245.0)]
    ypos = np.array([5.0, 4.0, 2.7, 1.7, 0.4, -0.6])
    a2.barh(ypos, [c[1] for c in cats], height=0.72, color=BLUE)
    for y, (lab, v) in zip(ypos, cats):
        a2.text(v + 5, y, f"{v:g}", va="center", ha="left", fontsize=8.5, color=INK_2)
    a2.set_yticks(ypos)
    a2.set_yticklabels([c[0] for c in cats], fontsize=8)
    a2.set_xlim(0, 285)
    a2.set_ylim(-1.2, 5.6)
    a2.grid(axis="y", visible=False)
    a2.grid(axis="x", visible=True)
    a2.set_xlabel("Annual borrow fee, 2004–07 (bp)")
    a2.tick_params(axis="y", length=0)
    return finish(fig, "ch08d_borrow_fee")


# --------------------------------------------------------------------------------------------
# 8-D.4  Ben Dor et al.: the beta hedge wins on correlation and loses on everything else
# --------------------------------------------------------------------------------------------
BEN_DOR = {   # PV01, DTS, 24/26-week beta; Table 8.1 (calm) and Table 10.3 (crisis, full set)
    "corr_calm": (0.37, 0.23, 0.11),
    "share_calm": (18.6, 12.6, 18.9), "share_crisis": (21.6, 25.6, 41.1),
    "vol_calm": (13.3, 11.2, 18.0), "vol_crisis": (159.1, 117.5, 137.3),
}


def fig_ben_dor():
    fig, axes = new_figure((7.7, 3.5), ncols=3)
    cols = [C_DV01, C_DTS, C_BETA]
    names = ["PV01", "DTS", "Beta"]

    def single(ax, vals, fmt, ttl, ylab, ymax):
        ax.bar(range(3), vals, width=0.68, color=cols)
        for i, v in enumerate(vals):
            ax.text(i, v + ymax * 0.02, fmt.format(v), ha="center", va="bottom", fontsize=8.5, color=INK_2)
        ax.set_xticks(range(3))
        ax.set_xticklabels(names, fontsize=8.5)
        ax.set_title(ttl, fontsize=9.2)
        ax.set_ylabel(ylab)
        ax.set_ylim(0, ymax)
        ax.tick_params(axis="x", length=0)

    def grouped(ax, calm, crisis, fmt, ttl, ylab, ymax):
        xs = [0, 1, 2, 3.6, 4.6, 5.6]
        ax.bar(xs, list(calm) + list(crisis), width=0.82, color=cols + cols)
        for x, v in zip(xs, list(calm) + list(crisis)):
            ax.text(x, v + ymax * 0.02, fmt.format(v), ha="center", va="bottom", fontsize=7.6, color=INK_2)
        ax.set_xticks(xs)
        ax.set_xticklabels(["PV01", "DTS", "Beta"] * 2, fontsize=7.6)
        ax.set_title(ttl, fontsize=9.2)
        ax.set_ylabel(ylab)
        ax.set_ylim(0, ymax)
        ax.tick_params(axis="x", length=0)
        ax.text(1, -0.15, "2003–06", transform=ax.get_xaxis_transform(), ha="center", va="top", fontsize=8,
                color=INK_2)
        ax.text(4.6, -0.15, "2007–08", transform=ax.get_xaxis_transform(), ha="center", va="top", fontsize=8,
                color=INK_2)

    single(axes[0], BEN_DOR["corr_calm"], "{:.2f}", "Correlation with the\nmarket, 2003–06", "Average |correlation|", 0.46)
    grouped(axes[1], BEN_DOR["share_calm"], BEN_DOR["share_crisis"], "{:.1f}", "Share of variance that\nis systematic",
            "Systematic share (%)", 50)
    grouped(axes[2], BEN_DOR["vol_calm"], BEN_DOR["vol_crisis"], "{:.1f}", "P&L volatility\nof the pairs", "Basis points a week",
            190)
    fig.legend(handles=[Patch(color=C_DV01, label="equal risky PV01"), Patch(color=C_DTS, label="DTS"),
                        Patch(color=C_BETA, label="empirical beta (24 weeks; 26 in 2007–08)")],
               loc="outside lower center", ncol=3, fontsize=8, handlelength=1.2, columnspacing=1.8)
    return finish(fig, "ch08d_ben_dor_rulers")


# --------------------------------------------------------------------------------------------
# 8-D.3  Three rulers, four market states (the existing embed)
# --------------------------------------------------------------------------------------------
def scenario_table():
    """The four-state P&L table of 8D.3 in $ thousands, recomputed from first principles."""
    sd, long_mm = 4.5, 40.0
    shorts = {"DV01": 40.0, "DTS": 60.0, "Beta": 85.6}
    moves = [   # (long bp, short bp)
        (18.0, 12.0),   # market widens 10% relative: Ford +18, GM +12
        (10.0, 10.0),   # both legs widen a parallel 10 bp
        (-15.0, 0.0),   # Ford tightens 15 bp on its own
        (0.0, 10.0),    # GM widens 10 bp on its own
    ]
    out = []
    for dl, ds in moves:
        row = []
        for k in ("DV01", "DTS", "Beta"):
            pnl = -sd * dl / 1e4 * long_mm * 1000 + sd * ds / 1e4 * shorts[k] * 1000
            row.append(pnl)
        out.append(row)
    return out


def fig_ruler_scenarios():
    table = scenario_table()
    expected = [(-108, 0, 138), (0, 90, 205), (270, 270, 270), (180, 270, 385)]
    for got, exp in zip(table, expected):
        assert all(abs(g - e) < 1.0 for g, e in zip(got, exp)), (got, exp)
    titles = ["Market widens 10%\n(Ford +18 bp, GM +12)", "Both legs widen\na parallel 10 bp",
              "Idio: Ford Credit\ntightens 15 bp", "Idio: GM Financial\nwidens 10 bp"]
    fig, axes = new_figure((7.4, 3.5), ncols=4, sharey=True)
    cols = [C_DV01, C_DTS, C_BETA]
    for ax, ttl, row in zip(axes, titles, expected):
        ax.bar(range(3), row, width=0.7, color=cols)
        ax.axhline(0, color=INK_2, linewidth=0.8, zorder=2)
        ax.axhline(270, color=NEUTRAL, linewidth=0.9, linestyle=(0, (3, 3)), zorder=1)
        for i, v in enumerate(row):
            ax.text(i, v + (14 if v >= 0 else -14), sgn(v), ha="center", va="bottom" if v >= 0 else "top",
                    fontsize=7.8, color=INK_2)
        ax.set_xticks(range(3))
        ax.set_xticklabels(["DV01", "DTS", "Beta"], fontsize=7.6)
        ax.set_title(ttl, fontsize=8.2, loc="center")
        ax.set_ylim(-180, 480)
        ax.tick_params(axis="x", length=0)
    axes[0].set_ylabel("Pair P&L, $40mm Ford long ($ thousands)")
    axes[0].text(-0.45, 285, "alpha = +270\n(15 bp of Ford news)", fontsize=7.8, color=MUTED, ha="left", va="bottom",
                 linespacing=1.15)
    return finish(fig, "ch08d_ruler_scenarios")


# --------------------------------------------------------------------------------------------
# 8-D.5  Two jump processes: one year of jump P&L
# --------------------------------------------------------------------------------------------
def fig_two_spikes():
    pL, pS = 0.03, 0.02                            # Ford Credit 180/0.60; GM Financial 120/0.60
    assert abs(0.0180 / 0.60 - pL) < 1e-12 and abs(0.0120 / 0.60 - pS) < 1e-12
    lossL = 40.0 * (95 - 40) / 95                   # -23.2: Ford Credit long defaults
    gainS = 60.0 * (98 - 40) / 98                   # +35.5: GM Financial short defaults
    assert abs(lossL - 23.16) < 0.01 and abs(gainS - 35.51) < 0.01
    ev = pS * gainS - pL * lossL                    # +0.015 ($mm), "+$15,000 a year"
    assert abs(ev * 1000 - 15.0) < 1.0
    states = [  # (x $mm, probability, label, colour, dx, dy, ha)  independent defaults
        (0.0, (1 - pL) * (1 - pS), "No default\n95.1%", NEUTRAL),
        (-lossL, pL * (1 - pS), None, C_LOSS),
        (gainS, pS * (1 - pL), None, C_GAIN),
        (gainS - lossL, pL * pS, None, C_GAIN),
    ]
    fig, ax = new_figure("wide")
    ymin = 0.02
    for x, p, lab, col in states:
        ax.vlines(x, ymin, p * 100, color=col, linewidth=2.6)
        ax.plot([x], [p * 100], "o", color=col, markersize=7, zorder=5)
    ax.set_yscale("log")
    ax.set_ylim(ymin, 400)
    ax.set_xlim(-42, 48)
    ax.annotate("No default\n95.1%", (0, 95.06), xytext=(8, -2), textcoords="offset points", fontsize=8.5,
                color=INK_2, va="center")
    ax.annotate("Ford Credit defaults\n" + MINUS + "$23.2mm, 2.9%", (-lossL, 2.94), xytext=(-8, 0),
                textcoords="offset points", fontsize=8.5, color=INK_2, va="center", ha="right")
    ax.annotate("GM Financial defaults\n+$35.5mm, 1.9%", (gainS, 1.94), xytext=(0, 9), textcoords="offset points",
                fontsize=8.5, color=INK_2, va="bottom", ha="center")
    ax.annotate("Both default\n+$12.3mm, 0.06%", (gainS - lossL, 0.0579), xytext=(-8, 0), textcoords="offset points",
                fontsize=8.5, color=INK_2, va="center", ha="right")
    ax.axvline(-20, color=NEUTRAL, linewidth=0.9, linestyle=(0, (3, 3)), zorder=1)
    ax.annotate("5% of a $400mm pod", (-20, 0.96), xycoords=("data", "axes fraction"), xytext=(-3, 0),
                textcoords="offset points", fontsize=8, color=INK_2, va="top", ha="right")
    ax.set_xlabel("Jump P&L over one year if that default happens ($mm)")
    ax.set_ylabel("Probability (%, log scale)")
    ax.set_yticks([0.1, 1, 10, 100])
    ax.set_yticklabels(["0.1", "1", "10", "100"])
    note(ax, f"Mean of the whole distribution: +${ev * 1000:.0f}k.  One year of the 30 bp thesis: +$540k.",
         loc="upper right")
    return finish(fig, "ch08d_two_spikes")


# --------------------------------------------------------------------------------------------
# 8-D.7  How often a 5% stop fires
# --------------------------------------------------------------------------------------------
def drawdown_hit(vol, sharpe, dd=0.05, n=252, paths=200_000, chunk=20_000, seed=4):
    rng = np.random.default_rng(seed)
    mu, sd = sharpe * vol / n, vol / np.sqrt(n)
    hits = 0
    for _ in range(paths // chunk):
        x = rng.normal(mu, sd, (chunk, n)).cumsum(axis=1)
        peak = np.maximum(np.maximum.accumulate(x, axis=1), 0.0)
        hits += int(((peak - x).max(axis=1) >= dd).sum())
    return hits / paths


def fig_stop_out_odds():
    n, vol, dd = 252, 0.06, 0.05
    r = np.random.default_rng(15)
    x = np.concatenate([[0.0], r.normal(0, vol / np.sqrt(n), n).cumsum()])
    peak = np.maximum.accumulate(x)
    stop_line = peak - dd
    hit = int(np.argmax(peak - x >= dd))
    assert (peak - x).max() >= dd and x.min() > -dd        # the stop fires; the fixed line never would
    fig, (a1, a2) = new_figure("wide", ncols=2, gridspec_kw={"width_ratios": [1.25, 1]})
    d = np.arange(n + 1)
    a1.plot(d, 100 * x, color=BLUE, linewidth=LW)
    a1.step(d, 100 * stop_line, where="post", color=ORANGE, linewidth=1.3)
    a1.axhline(-5, color=NEUTRAL, linewidth=1.0, linestyle=(0, (3, 3)))
    a1.plot([hit], [100 * x[hit]], "o", color=INK, markersize=6, zorder=6)
    a1.annotate(f"day {hit}: down 5% from the peak,\nstill up {100 * x[hit]:.1f}% from the start", (hit, 100 * x[hit]),
                xytext=(n - 2, -0.9), textcoords="data", fontsize=8, color=INK_2, ha="right", va="top",
                arrowprops=dict(arrowstyle="-", color=NEUTRAL, linewidth=0.8, shrinkA=1, shrinkB=3))
    a1.annotate("fixed line, 5% below the start", (n, -5), xytext=(0, 4), textcoords="offset points", fontsize=8,
                color=INK_2, ha="right", va="bottom")
    ia = int(np.argmax(x))
    a1.annotate("equity", (ia, 100 * x[ia]), xytext=(0, 8), textcoords="offset points", fontsize=8.5, color=INK_2,
                ha="center", va="bottom")
    a1.text(212, 2.3, "stop = peak " + MINUS + " 5%", fontsize=7.8, color=INK_2, ha="right", va="bottom")
    a1.set_xlim(0, n)
    a1.set_ylim(-6.5, 9.5)
    a1.set_xlabel("Trading day")
    a1.set_ylabel("Cumulative P&L (% of allocated capital)")
    a1.plot([], [])
    # right: probabilities
    fixed = 2 * norm_cdf(-dd / vol)                      # reflection principle: 2 x P(end below the line)
    probs = [fixed, drawdown_hit(0.06, 0.0), drawdown_hit(0.06, 1.0), drawdown_hit(0.04, 1.0)]
    print("stop-out odds:", [round(100 * p, 1) for p in probs])
    labs = ["Fixed line\nSharpe 0\n6% vol", "Drawdown\nSharpe 0\n6% vol", "Drawdown\nSharpe 1\n6% vol",
            "Drawdown\nSharpe 1\n4% vol"]
    a2.bar(range(4), [100 * p for p in probs], width=0.68, color=[NEUTRAL, BLUE, BLUE, BLUE])
    for i, p in enumerate(probs):
        a2.text(i, 100 * p + 1.5, f"{100 * p:.0f}%", ha="center", va="bottom", fontsize=9, color=INK_2)
    a2.set_xticks(range(4))
    a2.set_xticklabels(labs, fontsize=7.6)
    a2.set_ylim(0, 90)
    a2.set_ylabel("Chance a 5% stop fires in a year (%)")
    a2.tick_params(axis="x", length=0)
    return finish(fig, "ch08d_stop_out_odds")


# --------------------------------------------------------------------------------------------
# 8-D.6  The stop as a size (the existing embed)
# --------------------------------------------------------------------------------------------
def single_cap(budget, rec, price=0.95):
    return budget * price / (price - rec)


def pair_cap(budget, rec, e=0.10, price=0.95, junior_price=0.70):
    """Cap on the long (MV, $mm) for a jump-neutral first-lien / second-lien pair whose two recoveries are each
    wrong by e (senior recovers e less, junior e more).  Junior recovery = (2/7) x senior, the training sheet's
    70 / 20 ratio.  Residual default loss per $ of long MV = e (1 + F_J/F) / price."""
    rj = 2.0 / 7.0 * rec
    ratio = (price - rec) / (junior_price - rj)
    return budget / (e * (1 + ratio) / price)


def fig_stop_size():
    assert abs(single_cap(13, 0.40) - 22.45) < 0.01 and abs(single_cap(15, 0.40) - 25.91) < 0.01
    rec = np.linspace(0, 0.75, 301)
    s13 = single_cap(13, rec)
    s15 = single_cap(15, rec)
    p13 = pair_cap(13, rec)
    p15 = pair_cap(15, rec)
    fig, ax = new_figure("wide")
    ax.fill_between(100 * rec, p13, p15, color=AQUA, alpha=0.45, linewidth=0)
    ax.plot(100 * rec, s13, color=BLUE, linewidth=LW)
    ax.plot(100 * rec, s15, color=ORANGE, linewidth=LW)
    ax.axvline(40, ymax=0.62, color=NEUTRAL, linewidth=0.9, linestyle=(0, (3, 3)), zorder=1)
    ax.plot([40], [single_cap(13, 0.4)], "o", color=BLUE, markersize=6, zorder=6)
    ax.plot([40], [single_cap(15, 0.4)], "o", color=ORANGE, markersize=6, zorder=6)
    ax.annotate("$22.5mm at a recovery of 40", (40, single_cap(13, 0.4)), xytext=(8, -9), textcoords="offset points",
                fontsize=8.5, color=INK_2, va="top", ha="left")
    ax.annotate("$25.9mm", (40, single_cap(15, 0.4)), xytext=(-8, 6), textcoords="offset points", fontsize=8.5,
                color=INK_2, va="bottom", ha="right")
    label_end(ax, 75, float(s15[-1]), "$15mm budget", ORANGE)
    label_end(ax, 75, float(s13[-1]), "$13mm to Dov's line", BLUE)
    ax.annotate("capital-structure pair, same two budgets", (2, float(p13[0])), xytext=(0, -5),
                textcoords="offset points", fontsize=8.5, color=INK_2, ha="left", va="top")
    ax.set_xlim(0, 75)
    ax.set_ylim(0, 112)
    ax.set_xlabel("Assumed recovery (points of par)")
    ax.set_ylabel("Largest position ($mm market value)")
    note(ax, "Pair: long the 95 claim, short a second lien at 70, jump-neutral at the assumed recoveries;\n"
             "band = cap if both recoveries are 10 points off in opposite directions.", loc="upper left")
    return finish(fig, "ch08d_stop_size_vs_recovery")


# --------------------------------------------------------------------------------------------
# 8-D.8  The Pair Book as a figure (the existing embed)
# --------------------------------------------------------------------------------------------
def ledger_rows():
    """Twelve rows, $ thousands.  Statuses follow state/rv_pair_book.md: PB-01, PB-02 and PB-19 are open on 8 October;
    the rest are replays or a refusal.  Drawn at the figure's scale: PB-19 (8D.6's September), PB-01 (kappa 0.41),
    PB-03 (kappa 0.60, idio $0.75mm, net $0.45mm after financing), and, from the Pair Book's recorded capture ratios, PB-09 (0.8: idio +0.80mm,
    net +0.65mm) and PB-10 (0.2: idio about 0.9mm, net about 0.17mm).  Text rows (no bars): PB-02 (idio about 0, capture
    not defined), PB-07 (capture about 5, off the scale), PB-11 (idio flat, the P&L was the jump overhang), PB-12
    (refused).  Generated, seed 80: PB-08, PB-14, PB-16."""
    rng = np.random.default_rng(80)
    fixed = {
        "PB-01": (210.0, -66.0, -58.0), "PB-03": (750.0, -150.0, -150.0),
        "PB-09": (800.0, -100.0, -50.0), "PB-10": (900.0, -430.0, -300.0),
        "PB-19": (162.0, -(51.8 + 6.0), -(12.5 + 13.3 + 20.0)),
    }
    notes = {   # rows with no bars: the reason, in the bar panel
        "PB-02": "Idio about zero at the last explain, so\nthe capture ratio is not defined",
        "PB-07": "Idio +$0.81mm, net +$4.19mm: paid by a\nleak (capture about 5), off this scale",
        "PB-11": "Idio about flat; the P&L was the jump-\nto-default overhang: no capture ratio",
        "PB-12": "Declined: no short leg exists once\nthe credit event is manufactured (\u00a724.8.2)",
    }
    meta = [  # id, name, status
        ("PB-01", "Kestrel / Halvorsen", "live"), ("PB-02", "Halvorsen secured / unsecured", "live"),
        ("PB-03", "Ford Credit / GM Financial", "replay"), ("PB-07", "Hertz bonds / stock", "replay"),
        ("PB-08", "Level 3 / Lumen", "replay"), ("PB-09", "Kroger SMR / non-SMR", "replay"),
        ("PB-10", "EA put / defeasance", "replay"), ("PB-11", "Windstream bond / CDS", "replay"),
        ("PB-12", "Hovnanian", "refused"), ("PB-14", "Altice France sec. / unsec.", "replay"),
        ("PB-16", "OBDC / HYG", "replay"), ("PB-19", "Ford Credit / GM Financial", "live"),
    ]
    rows = []
    for pid, name, status in meta:
        note_txt = notes.get(pid)
        if pid in fixed:
            idio, leak, fric = fixed[pid]
            src = "chapter" if pid in ("PB-01", "PB-03", "PB-19") else "pair book"
        elif note_txt:
            idio = leak = fric = None
            src = "text"
        else:
            idio = float(5 * round(rng.uniform(70, 260) / 5))
            leak = -round(idio * rng.uniform(0.15, 0.45), 1)
            fric = -round(idio * rng.uniform(0.15, 0.35), 1)
            src = "generated"
        kappa = None if idio is None else (idio + leak + fric) / idio
        rows.append(dict(id=pid, name=name, status=status, idio=idio, leak=leak, fric=fric, kappa=kappa, src=src,
                         note=note_txt))
    return rows


def fig_ledger():
    rows = ledger_rows()
    by = {r["id"]: r for r in rows}
    assert abs(by["PB-19"]["kappa"] - 0.36) < 0.005 and abs(by["PB-01"]["kappa"] - 0.41) < 0.005
    assert abs(by["PB-03"]["kappa"] - 0.60) < 0.005
    assert abs(by["PB-09"]["kappa"] - 0.8) < 0.02 and abs(by["PB-10"]["kappa"] - 0.2) < 0.02   # the Pair Book's values
    assert abs(by["PB-19"]["idio"] + by["PB-19"]["leak"] + by["PB-19"]["fric"] - 58.4) < 0.05
    assert [r["status"] for r in rows].count("live") == 3 and [r["status"] for r in rows].count("refused") == 1
    assert all(0.25 < r["kappa"] < 0.7 for r in rows if r["src"] == "generated")
    n = len(rows)
    fig = plt.figure(figsize=(7.2, 7.4), layout="constrained")
    fig.get_layout_engine().set(rect=(0.0, 0.165, 1.0, 0.835))
    gs = fig.add_gridspec(1, 3, width_ratios=[4.0, 1.4, 0.62])
    ab = fig.add_subplot(gs[0, 0])
    ak = fig.add_subplot(gs[0, 1], sharey=ab)
    ast = fig.add_subplot(gs[0, 2], sharey=ab)
    ast.axis("off")
    ys = np.arange(n)[::-1].astype(float)      # first row at the top
    bh = 0.26
    for y, r in zip(ys, rows):
        if r["idio"] is None:
            ab.text(25, y, r["note"], ha="left", va="center", fontsize=7.8, color=INK_2, style="italic",
                    linespacing=1.2)
            continue
        ab.barh(y + bh, r["idio"], height=bh * 0.9, color=C_THESIS)
        ab.barh(y, r["leak"], height=bh * 0.9, color=C_LEAK)
        ab.barh(y - bh, r["fric"], height=bh * 0.9, color=C_FRIC)
    top = rows[0]          # direct labels on the first row (the aqua friction bars need them, as well as the legend)
    ab.text(top["idio"] + 14, ys[0] + bh, "idio", ha="left", va="center", fontsize=7.8, color=INK_2)
    ab.text(top["leak"] - 10, ys[0], "leak", ha="right", va="center", fontsize=7.8, color=INK_2)
    ab.text(top["fric"] - 10, ys[0] - bh, "friction", ha="right", va="center", fontsize=7.8, color=INK_2)
    ab.axvline(0, color=INK_2, linewidth=0.8, zorder=2)
    ab.set_yticks(ys)
    ab.set_yticklabels([f"{r['id']}  {r['name']}" for r in rows], fontsize=8)
    ab.set_xlim(-500, 1000)
    ab.set_ylim(-0.7, n - 0.3)
    ab.grid(axis="y", visible=False)
    ab.grid(axis="x", visible=True)
    ab.set_xlabel("P&L, $ thousands (September; a replay's own window)")
    ab.tick_params(axis="y", length=0)
    # capture ratio panel; the row status sits in its own column to the right
    for y, r in zip(ys, rows):
        ast.text(0.0, y, r["status"], transform=ast.get_yaxis_transform(), ha="left", va="center", fontsize=7.8,
                 color=MUTED)
        if r["kappa"] is None:
            if r["id"] == "PB-07":
                ak.text(0.04, y, "about 5 \u2192", ha="left", va="center", fontsize=8, color=INK_2)
            else:
                ak.text(0.5, y, "\u2014", ha="center", va="center", fontsize=9, color=MUTED)
            continue
        ak.plot([0, r["kappa"]], [y, y], color=NEUTRAL, linewidth=1.0, zorder=1)
        ak.plot([r["kappa"]], [y], "o", color=INK_2, markersize=6, zorder=3)
        ak.text(r["kappa"] + 0.09, y, f"{r['kappa']:.2f}", ha="left", va="center", fontsize=8, color=INK_2)
    ak.set_xlim(0, 1.25)
    ak.set_xticks([0, 0.5, 1.0])
    ak.set_xticklabels(["0", "0.5", "1"])
    ak.set_xlabel("Capture ratio\n(net / idio)")
    ak.grid(axis="y", visible=False)
    ak.grid(axis="x", visible=True)
    plt.setp(ak.get_yticklabels(), visible=False)
    ak.tick_params(axis="y", length=0)
    fig.legend(handles=[Patch(color=C_THESIS, label="idio"), Patch(color=C_LEAK, label="leak"),
                        Patch(color=C_FRIC, label="friction")], loc="outside upper center", ncol=3, fontsize=8.5,
               handlelength=1.2, columnspacing=1.8)
    foot = ("Book lines for all twelve live pairs, Thursday 8 October: mean pairwise idio correlation 0.28 (\u00a78.8 test);\n"
            "beta to CDX HY +0.04 of gross; rating bucket 0.08 (0.11 on Tuesday); largest jump-to-default long\n"
            "Kestrel (about $34mm), short GM Financial; borrow fee on the book 64 bp; distance to the first line $13mm.\n"
            "Bars: September for live rows, the replay's own window for replay rows. PB-01, PB-03, PB-12 and PB-19 follow\n"
            "the chapter; PB-09 and PB-10 use the capture ratios the Pair Book records (0.8, 0.2); PB-02, PB-07 and PB-11\n"
            "are text rows (no usable capture ratio); PB-08, PB-14 and PB-16 are generated for this figure (seed 80).")
    fig.text(0.012, 0.148, foot, ha="left", va="top", fontsize=7.8, color=INK_2, linespacing=1.4)
    return finish(fig, "ch08d_pair_book_ledger")


if __name__ == "__main__":
    fig_fee_flip()
    fig_borrow_fee()
    fig_ben_dor()
    fig_ruler_scenarios()
    fig_two_spikes()
    fig_stop_out_odds()
    fig_stop_size()
    fig_ledger()
