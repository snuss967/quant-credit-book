"""Figures for Chapter 2-B (Transaction Cost Analysis for Credit).

Run:  python3 tools/figures/ch02b.py   -> assets/figures/ch02b_*.png   (five figures)

Colour roles, held fixed across the chapter's figures (identity is also always carried by a direct label or legend):
  BLUE   = a cost the execution system's report shows (executed fills, the legs it ticketed); in Figure 2-B.1 the
           delay / drift / half-spread shades of the executed part
  ORANGE = a cost that report does not show (the unfilled remainder, legging, the bridge and the CDX leg, the stress regime)
  INK_2  = the full measured total; NEUTRAL grey = the execution report's own number, or a benchmark line
Aqua, yellow and magenta are not used (below 3:1 contrast on white).

Data. Every figure here is Illustrative: the desk, its log, its dealers A to K, its fills and PB-01 are fictional
composites in the chapter. All numbers are the chapter's own (Math, Gently box of 2B.1.1; the shortfall table of 2B.2;
the cost-curve table of 2B.5; the PB-01 arithmetic of 2B.7) and are recomputed here from the formulas the chapter
states. Where a figure needs a number the chapter does not give (the stamp clock times and the one-hour and one-day
mids in Figure 2-B.1; the dealer cells in Figure 2-B.2, other than the ones the text fixes: K's 11% response rate,
C's 41% hit rate, C's -4.2 bp winners-only markout, F worst on every-quote markout, K and one other answering on
9 April 2025; the bucket mid-sizes in Figure 2-B.3) it is assumed here and says so in the figure or its note.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
import numpy as np  # noqa: E402
from matplotlib.lines import Line2D  # noqa: E402
from matplotlib.patches import Patch, Rectangle  # noqa: E402

from style import *  # noqa: E402,F401,F403  (applies the rcParams on import)

plt.rcParams["text.parse_math"] = False      # "$" is always a dollar sign in these figures

ORANGE_TINT = "#f6b99c"
BLUE_TINT = "#dbe8f9"
GREY_TINT = "#f4f3f0"
TOTAL = INK_2


# --------------------------------------------------------------------------------------------------
# Figure 2-B.1 (2B.2): one fill on four benchmarks; the rebalance's shortfall by date
# --------------------------------------------------------------------------------------------------
def fig_benchmark_ladder():
    fig = plt.figure(figsize=(7.0, 7.0), layout="constrained")
    gs = fig.add_gridspec(2, 2, height_ratios=[1.3, 1.0], width_ratios=[3.7, 2.2])
    ax = fig.add_subplot(gs[0, 0])
    tb = fig.add_subplot(gs[0, 1], sharey=ax)
    ax2 = fig.add_subplot(gs[1, :])

    # ---- top left: the timeline and the levels (spacing is ordinal, not to scale) ----
    xs = {"NEW": 0.0, "ROUTED": 1.55, "QUOTED": 3.1, "FILLED": 4.55, "PRINT": 6.15, "H1": 7.75, "D1": 9.3}
    ticks = [xs["NEW"], xs["ROUTED"], xs["QUOTED"], xs["FILLED"], xs["PRINT"], xs["H1"], xs["D1"]]
    tlabels = ["NEW\n9:00", "ROUTED\n9:04", "QUOTED\n9:06", "FILLED\n9:07", "TRACE\n9:29", "+1 hour\n10:07", "+1 day"]
    fill = 98.42
    levels = [  # (name, price, stamp key)
        ("Next print", 98.47, "PRINT"),
        ("Cover", 98.45, "QUOTED"),
        ("Composite offer", 98.43, "ROUTED"),
        ("RFQ-time mid", 98.40, "ROUTED"),
        ("Arrival mid", 98.38, "NEW"),
    ]
    ax.set_xlim(-0.6, 9.85)
    ax.set_ylim(98.355, 98.495)
    ax.grid(False)
    ax.set_xticks(ticks)
    ax.set_xticklabels(tlabels, fontsize=7.8)
    ax.set_yticks([98.40, 98.45])
    ax.set_yticklabels(["98.40", "98.45"])
    ax.set_ylabel("Price (per 100 face)")
    ax.set_xlabel("Stamps not to scale. Clock times and the later mids are assumed.", fontsize=7.8, color=MUTED)

    for key in ["NEW", "ROUTED", "QUOTED", "FILLED"]:
        ax.axvline(xs[key], color=GRID, linewidth=1.0, zorder=0)
    for name, p, key in levels:          # faint rule from the stamp across to the table
        ax.plot([xs[key], 9.85], [p, p], color=GRID, linewidth=0.9, zorder=1, clip_on=False)
    ax.plot([xs["FILLED"], 9.85], [fill, fill], color=BLUE_TINT, linewidth=1.2, zorder=1)
    for name, p, key in levels:
        end = xs["PRINT"] if key == "PRINT" else xs["FILLED"]
        ax.plot([xs[key], end], [p, p], color=INK_2, linewidth=1.5, solid_capstyle="butt", zorder=3)
        ax.plot([xs[key]], [p], "o", color=INK_2, markersize=5, zorder=4)
    ax.plot([xs["FILLED"], xs["PRINT"]], [fill, 98.47], color=NEUTRAL, linewidth=0.9, linestyle=(0, (2, 2)), zorder=2)
    ax.plot([xs["FILLED"]], [fill], "o", color=BLUE, markersize=9, zorder=6)
    for key, p in [("H1", 98.46), ("D1", 98.44)]:
        ax.plot([xs[key], xs[key]], [fill, p], color=BLUE, linewidth=1.0, zorder=2)
        ax.plot([xs[key]], [p], "o", markerfacecolor=SURFACE, markeredgecolor=INK_2, markersize=6, zorder=5)
        ax.plot([xs[key]], [fill], "o", color=BLUE, markersize=4, zorder=5)
        ax.annotate(f"mid {p:.2f}", (xs[key], p), xytext=(0, 7), textcoords="offset points", ha="center", fontsize=7.6,
                    color=INK_2)
    xb = (xs["H1"] + xs["D1"]) / 2          # axis-break marks between 1 hour and 1 day
    for dx in (-0.09, 0.09):
        ax.plot([xb + dx - 0.07, xb + dx + 0.07], [98.3535, 98.3585], color=INK_2, linewidth=1.0, clip_on=False, zorder=7)

    # ---- top right: the table of levels and costs, aligned on the same price axis ----
    for s_ in tb.spines.values():
        s_.set_visible(False)
    tb.grid(False)
    tb.set_xticks([]); tb.tick_params(axis="y", left=False, labelleft=False)
    tb.set_xlim(0, 1)
    tb.text(0.0, 98.4905, "Benchmark", fontsize=7.8, color=MUTED, va="top", ha="left")
    tb.text(1.0, 98.4905, "Cost of the fill\n(bp, positive is bad)", fontsize=7.8, color=MUTED, va="top", ha="right")
    for name, p, key in levels:
        cost = (fill - p) / p * 1e4          # buy, positive is bad
        tb.text(0.0, p, f"{name}  {p:.2f}", fontsize=8.3, color=INK_2, va="center", ha="left")
        tb.text(1.0, p, f"{cost:+.1f}".replace("-", "\u2212"), fontsize=8.8, color=INK, va="center", ha="right")
    tb.text(0.0, fill, f"Fill (buy $2mm)  {fill:.2f}", fontsize=8.3, color=BLUE, va="center", ha="left", fontweight="bold")

    # ---- bottom: the rebalance shortfall by date ----
    comps = [  # label, colour, Wednesday $k, Friday $k
        ("Delay (NEW to ROUTED)", SEQ_BLUE_STEPS[2], 9.765, 9.765),
        ("Drift while quoting", SEQ_BLUE_STEPS[5], 6.975, 6.975),
        ("Half-spread", SEQ_BLUE_STEPS[8], 72.54, 72.54),
        ("Unfilled: market part", ORANGE, -60.75, 44.55),
        ("Unfilled: IDO part", ORANGE_TINT, 24.30, 68.85),
    ]
    rows = {"Wednesday evening": 1.0, "Friday retry": 0.0}
    height = 0.52
    nets = {}
    for col, (ylab, yv) in enumerate(rows.items()):
        pos_left, neg_left = 0.0, 0.0
        for lab, c, w, f in comps:
            v = w if col == 0 else f
            if v >= 0:
                ax2.barh(yv, v, left=pos_left, height=height, color=c, edgecolor=SURFACE, linewidth=0.9, zorder=3)
                pos_left += v
            else:
                ax2.barh(yv, v, left=neg_left, height=height, color=c, edgecolor=SURFACE, linewidth=0.9, zorder=3)
                neg_left += v
        net = pos_left + neg_left
        nets[yv] = (net, pos_left)
        ax2.plot([net], [yv], "D", color=INK, markersize=6.5, zorder=6)
    ax2.axvline(0, color=INK_2, linewidth=0.9, zorder=4)
    ax2.set_yticks(list(rows.values()))
    ax2.set_yticklabels(["Wednesday evening\n(nine bonds marked\nat the close)", "Friday retry\n(nine bonds filled)"])
    ax2.set_ylim(-0.5, 1.5)
    ax2.set_xlim(-85, 360)
    ax2.grid(False)
    ax2.grid(True, axis="x")
    ax2.spines["left"].set_visible(False)
    ax2.tick_params(axis="y", length=0)
    ax2.set_xlabel("Shortfall on the $180mm rebalance ($ thousand; positive is a cost; diamond = net)")
    net_w, end_w = nets[1.0]
    ax2.text(end_w + 9, 1.0, f"net ${net_w:,.1f}k: the unfilled lines\nnet to a $36.45k gain, so the failures\nlook like savings", va="center",
             ha="left", fontsize=8.1, color=INK_2)
    net_f, end_f = nets[0.0]
    ax2.text(end_f + 11, 0.0, f"net ${net_f:,.1f}k = 11.3 bp of\nthe $180mm target; unfilled\nlines are $113.4k of it (56%)",
             va="center", ha="left", fontsize=8.1, color=INK_2)
    handles = [Patch(facecolor=c, label=lab) for lab, c, _, _ in comps]
    ax2.legend(handles=handles, loc="upper center", bbox_to_anchor=(0.45, -0.2), ncol=3, fontsize=8, columnspacing=1.2,
               handlelength=1.2)
    return finish(fig, "ch02b_benchmark_ladder")


# --------------------------------------------------------------------------------------------------
# Figure 2-B.2 (2B.4): the dealer scorecard as a heatmap
# --------------------------------------------------------------------------------------------------
def fig_scorecard():
    dealers = list("ABCDEFGHIJK")
    resp = np.array([58, 49, 66, 44, 38, 71, 35, 41, 28, 22, 11], float)       # response rate, %   (K = 11 per text)
    hit = np.array([33, 36, 41, 31, 34, 39, 30, 35, 28, 32, 37], float)        # hit rate, % of quotes (C = 41 per text)
    cover = np.array([3.1, 3.8, 2.4, 4.6, 4.2, 2.7, 5.1, 3.9, 5.6, 6.3, 4.4])   # bp behind the winner when a quote loses
    mk = np.array([0.6, 0.3, -0.2, -0.4, 0.8, -3.6, -1.1, 0.2, -0.7, -1.6, 0.9])  # 5-day residualised markout, every quote
    away = np.array([13, 11, 16, 9, 8, 15, 6, 8, 6, 5, 3], float)              # share of the desk's DONE_AWAY outcomes, %
    answered = {"E": True, "K": True}                                           # 9 Apr 2025, 10:40, high-yield panel

    cols = [
        ("Response\nrate\n(%)", resp, +1, "{:.0f}"),
        ("Hit rate\n(% of\nquotes)", hit, +1, "{:.0f}"),
        ("Cover\ndistance\n(bp)", cover, -1, "{:.1f}"),
        ("5-day\nmarkout\n(bp)", mk, +1, "{:+.1f}"),
        ("Done-away\nshare\n(%)", away, -1, "{:.0f}"),
    ]
    fig, ax = new_figure((7.4, 5.9))
    ax.grid(False)
    for s in ax.spines.values():
        s.set_visible(False)
    ncols = len(cols)
    gap = 0.5
    cw, ch = 1.2, 1.0
    cmap = DIVERGING

    def shade(z):   # z > 0 = worse for the desk
        return cmap(0.5 + np.clip(z, -2, 2) / 4.0)

    for j, (name, v, better, fmt) in enumerate(cols):
        z = -better * (v - v.mean()) / v.std()          # +1 = one s.d. worse than the panel
        for i, d in enumerate(dealers):
            c = shade(z[i])
            ax.add_patch(Rectangle((j * cw, -i * ch), cw, ch, facecolor=c, edgecolor=SURFACE, linewidth=1.5))
            lum = 0.299 * c[0] + 0.587 * c[1] + 0.114 * c[2]
            txt = fmt.format(v[i]).replace("-", "−")
            ax.text(j * cw + cw / 2, -i * ch + ch / 2, txt, ha="center", va="center", fontsize=8.5,
                    color="white" if lum < 0.5 else INK)
        ax.text(j * cw + cw / 2, ch + 0.12, name, ha="center", va="bottom", fontsize=7.9, color=INK_2)
    # the 9 April column
    x0 = ncols * cw + gap
    for i, d in enumerate(dealers):
        ok = answered.get(d, False)
        ax.add_patch(Rectangle((x0, -i * ch), cw * 1.25, ch, facecolor=BLUE if ok else GREY_TINT, edgecolor=SURFACE,
                               linewidth=1.5))
        ax.text(x0 + cw * 1.25 / 2, -i * ch + ch / 2, "answered" if ok else "silent", ha="center", va="center",
                fontsize=8.5, color="white" if ok else MUTED, fontweight="bold" if ok else "normal")
    ax.text(x0 + cw * 1.25 / 2, ch + 0.12, "9 April 2025:\nstill answering\nat 10:40?", ha="center", va="bottom",
            fontsize=8.0, color=INK_2)
    for i, d in enumerate(dealers):
        ax.text(-0.15, -i * ch + ch / 2, f"Dealer {d}", ha="right", va="center", fontsize=8.8,
                color=INK, fontweight="bold" if d in "CFK" else "normal")
    # callouts for the three dealers the text discusses
    ax.text(x0 + cw * 1.25 + 0.15, -2 * ch + ch / 2, "C: top hit rate, but −4.2 bp\nwhen only wins are marked", ha="left",
            va="center", fontsize=7.8, color=INK_2)
    ax.text(x0 + cw * 1.25 + 0.15, -5 * ch + ch / 2, "F: tier one on calm days;\nworst once every quote counts", ha="left",
            va="center", fontsize=7.8, color=INK_2)
    ax.text(x0 + cw * 1.25 + 0.15, -10 * ch + ch / 2, "K: 11% response rate,\nbut answering on 9 April", ha="left",
            va="center", fontsize=7.8, color=INK_2)
    ax.set_xlim(-1.35, x0 + cw * 1.25 + 3.35)
    ax.set_ylim(-len(dealers) * ch - 2.5, ch + 1.65)
    ax.set_xticks([]); ax.set_yticks([])
    ax.set_aspect("auto")
    # colour key
    kx, ky = 0.0, -len(dealers) * ch - 0.55
    n = 41
    for t in range(n):
        ax.add_patch(Rectangle((kx + t * 0.07, ky), 0.07, 0.32, facecolor=cmap(t / (n - 1)), linewidth=0))
    ax.text(kx - 0.1, ky + 0.16, "better for the desk", ha="right", va="center", fontsize=7.8, color=INK_2)
    ax.text(kx + n * 0.07 + 0.1, ky + 0.16, "worse for the desk (within each column; ±2 s.d.)", ha="left", va="center",
            fontsize=7.8, color=INK_2)
    ax.text(-1.2, ky - 0.5, "Cover distance: how far behind the winner a losing quote sat. Markout: residualised, marks every quote,\n"
            "not only wins. Done-away share: the dealer's share of the desk's DONE_AWAY outcomes. A longer cover\n"
            "distance and a larger done-away share are shaded worse. Every cell except the ones the chapter's text fixes is assumed.",
            ha="left", va="top", fontsize=7.8, color=MUTED)
    return finish(fig, "ch02b_dealer_scorecard_heatmap")


# --------------------------------------------------------------------------------------------------
# Figure 2-B.3 (2B.5): cost curves by regime, with counts, and the prior that replaces the thin bucket
# --------------------------------------------------------------------------------------------------
def fig_cost_curves():
    q = np.array([0.5, 2.2, 7.1, 15.0])          # $mm, geometric mid-sizes of the four buckets (assumed)
    calm = np.array([4.1, 6.0, 9.8, 14.0]); n_calm = [3812, 2407, 311, 38]
    stress = np.array([11.2, 17.5, 26.0, -3.0]); n_stress = [402, 188, 19, 4]
    s = np.sqrt(q)

    def fit(x, y):
        k, a = np.polyfit(x, y, 1)
        return a, k

    a_c, k_c = fit(s, calm)                       # calm: all four buckets
    a_s, k_s = fit(s[:3], stress[:3])             # April 2025: the three buckets above the minimum count
    grid = np.logspace(np.log10(0.3), np.log10(30), 200)
    curve_c = a_c + k_c * np.sqrt(grid)
    curve_s = a_s + k_s * np.sqrt(grid)
    env = 3.0 * curve_c
    prior = 3.0 * calm[3]                         # 3 x 14 = 42, the chapter's table

    fig, ax = new_figure((7.0, 4.2))
    ax.set_xscale("log")
    ax.set_xlim(0.3, 120)
    ax.set_ylim(-9, 66)
    # bucket bands
    edges = [0.3, 1, 5, 10, 30]
    names = ["under $1mm", "$1–5mm", "$5–10mm", "$10mm and up"]
    for i in range(4):
        if i % 2 == 0:
            ax.axvspan(edges[i], edges[i + 1], color=GREY_TINT, zorder=0, linewidth=0)
        ax.text(np.sqrt(edges[i] * edges[i + 1]), 64.2, names[i], ha="center", va="top", fontsize=8, color=MUTED)
    ax.axhline(0, color=NEUTRAL, linewidth=0.8, zorder=1)
    ax.spines["bottom"].set_position(("data", -9))
    ax.spines["bottom"].set_bounds(0.3, 30)
    ax.set_xticks([0.5, 1, 2, 5, 10, 20])
    ax.set_xticklabels(["0.5", "1", "2", "5", "10", "20"])
    ax.minorticks_off()
    ax.set_xlabel("Clip size ($mm, log scale; points at each bucket's assumed mid-size)")
    ax.set_ylabel("Half-spread plus impact vs arrival (bp per side)")

    ax.plot(grid, curve_c, color=BLUE, linewidth=LW, zorder=3)
    ax.plot(grid, curve_s, color=ORANGE, linewidth=LW, zorder=3)
    ax.plot(grid, env, color=ORANGE, linewidth=1.2, linestyle=(0, (4, 3)), zorder=2)
    label_end(ax, 30, curve_c[-1], "Calm 2024 fit", BLUE, dx=5)
    label_end(ax, 30, curve_s[-1], "April 2025 fit", ORANGE, dx=5)
    label_end(ax, 30, env[-1], "March 2020 envelope\n(3× calm spread,\nhalf the responses)", ORANGE, dx=5)

    ax.plot(q, calm, "o", color=BLUE, markersize=7, zorder=5)
    ax.plot(q[:3], stress[:3], "o", color=ORANGE, markersize=7, zorder=5)
    offs_c = [(7, -11), (7, -11), (7, -11), (7, -11)]
    for x, y, n, o in zip(q, calm, n_calm, offs_c):
        ax.annotate(f"n={n:,}", (x, y), xytext=o, textcoords="offset points", fontsize=7.8, color=INK_2,
                    ha="left", va="center")
    for x, y, n in zip(q[:3], stress[:3], n_stress[:3]):
        ax.annotate(f"n={n:,}", (x, y), xytext=(8, -11), textcoords="offset points", fontsize=7.8, color=INK_2,
                    ha="left", va="center")
    # the thin top stress bucket: raw point greyed, prior drawn in its place
    ax.plot([q[3]], [stress[3]], "X", color=NEUTRAL, markersize=8, zorder=5)
    ax.annotate("raw mean −3 (n=4):\ntwo PT lines, one rally", (q[3], stress[3]), xytext=(-8, 0), textcoords="offset points",
                fontsize=7.8, color=MUTED, ha="right", va="center")
    ax.plot([q[3]], [prior], "o", markerfacecolor=SURFACE, markeredgecolor=ORANGE, markeredgewidth=1.8, markersize=8, zorder=6)
    ax.annotate("", (q[3], prior - 2.0), (q[3], stress[3] + 2.0),
                arrowprops=dict(arrowstyle="-|>", color=NEUTRAL, linewidth=0.9, linestyle=(0, (2, 2)), mutation_scale=9),
                zorder=4)
    ax.annotate(f"prior {prior:.0f}: 3 × 14,\nnot data", (q[3], prior), xytext=(-9, 3), textcoords="offset points",
                fontsize=7.8, color=INK_2, ha="right", va="bottom")
    return finish(fig, "ch02b_cost_curves_by_regime")


# --------------------------------------------------------------------------------------------------
# Figure 2-B.4 (2B.7): PB-01's two-leg shortfall as a waterfall, beside the single-ticket report
# --------------------------------------------------------------------------------------------------
def _waterfall(ax, steps, total_label, report, report_label, fmt, ymax):
    """steps: (label, value, colour). Draws floating bars, a total, a gap, then the execution report's bar."""
    x = 0
    run = 0.0
    xt, lab = [], []
    for name, v, c in steps:
        ax.bar(x, v, bottom=run, width=0.7, color=c, zorder=3)
        ax.text(x, run + v + ymax * 0.015, fmt(v), ha="center", va="bottom", fontsize=8, color=INK_2)
        if x > 0:
            ax.plot([x - 1 + 0.36, x - 0.36], [run, run], color=NEUTRAL, linewidth=0.8, zorder=2)
        run += v
        xt.append(x); lab.append(name)
        x += 1
    ax.plot([x - 1 + 0.36, x - 0.36], [run, run], color=NEUTRAL, linewidth=0.8, zorder=2)
    ax.bar(x, run, width=0.72, color=TOTAL, zorder=3)
    ax.text(x, run + ymax * 0.015, fmt(run), ha="center", va="bottom", fontsize=8.3, color=INK, fontweight="bold")
    xt.append(x); lab.append(total_label)
    xr = x + 1.25
    ax.bar(xr, report, width=0.72, color=NEUTRAL, zorder=3)
    ax.text(xr, report + ymax * 0.015, fmt(report), ha="center", va="bottom", fontsize=8.3, color=INK_2)
    xt.append(xr); lab.append(report_label)
    # the gap
    ax.plot([xr - 0.36, xr + 0.62], [run, run], color=INK_2, linewidth=0.9, linestyle=(0, (3, 2)), zorder=2)
    ax.annotate("", (xr + 0.5, run), (xr + 0.5, report), arrowprops=dict(arrowstyle="<->", color=INK_2, linewidth=0.9,
                                                                         shrinkA=0, shrinkB=0))
    ax.set_xticks(xt); ax.set_xticklabels(lab, fontsize=7.1)
    ax.set_xlim(-0.55, xr + 0.95)
    ax.set_ylim(0, ymax)
    return run, xr


def fig_two_leg():
    fig, axs = plt.subplots(1, 2, figsize=(7.6, 4.0), layout="constrained", gridspec_kw={"width_ratios": [6.5, 5.2]})
    a1, a2 = axs
    # April opening ($ thousand)
    steps1 = [("Kestrel\nleg", 120.0, BLUE), ("Halvorsen\nleg (own\nstamp)", 140.0, BLUE),
              ("Legging,\nnet of\nbridge", 21.0, ORANGE), ("Bridge\nhalf-\nspreads", 16.0, ORANGE)]
    tot1, xr1 = _waterfall(a1, steps1, "Two-leg\ntotal", 260.0, "Execution\nreport", lambda v: f"{v:,.0f}", 372)
    a1.set_title("April opening of PB-01 ($ thousand)", fontsize=9)
    a1.text(xr1 + 0.1, tot1 + 14, "37 exists only\nbecause of\ntwo legs", fontsize=7.6, color=INK_2,
            ha="center", va="bottom")
    a1.set_ylabel("Shortfall ($ thousand)")
    # the 2:40 trim ($ thousand)
    steps2 = [("Bond\nleg", 14.0, BLUE), ("CDX leg\n(other\nsystem)", 1.938, ORANGE),
              ("Legging,\n12 min", 4.425, ORANGE)]
    tot2, xr2 = _waterfall(a2, steps2, "Two-leg\ntotal", 14.0, "Execution\nreport", lambda v: f"{v:,.1f}", 28.5)
    a2.set_title("The 2:40 trim of 13 October ($ thousand)", fontsize=9)
    a2.text(xr2 + 0.42, (tot2 + 14) / 2, "6.4", fontsize=7.8, color=INK_2, ha="right", va="center")
    a1.legend(handles=[Patch(color=BLUE, label="in the execution report"), Patch(color=ORANGE, label="not in it")],
              loc="upper left", fontsize=7.8, handlelength=1.1)
    return finish(fig, "ch02b_two_leg_shortfall")


# --------------------------------------------------------------------------------------------------
# Figure 2-B.5 (2B.7, new): the conviction a pair needs to pay for its round trip
# --------------------------------------------------------------------------------------------------
def fig_roundtrip():
    thesis_per_year = 1200.0      # $ thousand a year (about 100 bp, 2B.7)
    cost_two_leg = 2 * 297.0      # open now, close "something similar"
    cost_report = 2 * 260.0       # what the execution report showed, each way
    w = np.linspace(2, 56, 300)
    accrual = thesis_per_year * w / 52.0
    m_two = cost_two_leg / accrual
    m_rep = cost_report / accrual

    fig, ax = new_figure((7.0, 3.9))
    ax.set_yscale("log")
    ax.set_xlim(0, 76)
    ax.set_ylim(0.29, 18)
    ax.set_yticks([0.5, 1, 2, 4, 8, 16])
    ax.set_yticklabels(["0.5\u00d7", "1\u00d7", "2\u00d7", "4\u00d7", "8\u00d7", "16\u00d7"])
    ax.minorticks_off()
    ax.spines["bottom"].set_bounds(0, 56)
    ax.set_xticks([0, 6, 13, 26, 39, 52])
    ax.set_xticklabels(["0", "6", "13\n(a quarter)", "26", "39\n(nine months)", "52"])
    ax.set_xlabel("Weeks the desk expects to hold the pair")
    ax.set_ylabel("Round-trip cost as a multiple of the\nthesis earned over the hold")
    ax.axhline(1, color=INK_2, linewidth=0.9, zorder=2)
    ax.text(75, 1.07, "above the line, the thesis as sized does not pay for the trades", fontsize=7.8, color=INK_2,
            va="bottom", ha="right")
    ax.plot(w, m_rep, color=NEUTRAL, linewidth=LW, linestyle=(0, (4, 2.5)), zorder=3)
    ax.plot(w, m_two, color=TOTAL, linewidth=LW, zorder=4)
    label_end(ax, w[-1], m_two[-1], "Two-leg cost\n($297k each way)", TOTAL, dx=5, dy=13)
    label_end(ax, w[-1], m_rep[-1], "Execution report\n($260k each way)", NEUTRAL, dx=5, dy=-13)
    for wk, txt, dx, dy, ha in [(6, "6 weeks: {:.1f}\u00d7", 9, 12, "left"), (39, "9 months: {:.2f}\u00d7", 7, 13, "left")]:
        m = cost_two_leg / (thesis_per_year * wk / 52.0)
        ax.plot([wk], [m], "o", color=TOTAL, markersize=7, zorder=6)
        ax.annotate(txt.format(m), (wk, m), xytext=(dx, dy), textcoords="offset points", fontsize=8.5, color=INK,
                    ha=ha, va="center")
    be_two = cost_two_leg / thesis_per_year * 52
    be_rep = cost_report / thesis_per_year * 52
    ax.plot([be_two], [1], "|", color=TOTAL, markersize=11, markeredgewidth=1.8, zorder=6)
    ax.annotate(f"breaks even at {be_two:.0f} weeks\n(execution report's view: {be_rep:.0f})", (be_two, 0.97), xytext=(-8, -22),
                textcoords="offset points", fontsize=8, color=INK_2, ha="right", va="center",
                arrowprops=dict(arrowstyle="-", color=NEUTRAL, linewidth=0.8, shrinkA=0, shrinkB=2))
    note(ax, "Thesis $1.2mm a year (about 100 bp); closing costs the same as opening;\nborrow not included.",
         loc="lower left")
    return finish(fig, "ch02b_roundtrip_conviction")


if __name__ == "__main__":
    fig_benchmark_ladder()
    fig_scorecard()
    fig_cost_curves()
    fig_two_leg()
    fig_roundtrip()
