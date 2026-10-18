"""Figures for Chapter 1-B (A Week in Five Quant Shops).

Run:  python3 tools/figures/ch01b.py   -> assets/figures/ch01b_*.png   (five figures)

Colour roles, held fixed across the chapter's figures (identity is always also carried by a direct label):
  BLUE   = a rule or an official record (regulation); the corrected / better number; the desk's own long leg
  ORANGE = a routine real firms describe in public (sourced practice); the wrong / retracted / booked-by-choice number;
           the short leg
  MUTED grey = composite (the chapter's invented scene); context
  VIOLET = the index overlay (CDX) and the "in private talks" state in the last figure is BLUE, not violet
Aqua, yellow and magenta are not used (below 3:1 contrast on white).

Data. Real: the Senate Permanent Subcommittee on Investigations report on JPMorgan's Chief Investment Office
(15 Mar 2013) pages 5, 6 and 98, as quoted in state/research/life_quant_shop_daily_life.md and in the chapter; the rule
names and numbers (FINRA Rules 6730 and 5310, SEC Rule 15c3-5). Everything else is the chapter's own fictional
Halvorsen arithmetic, recomputed here from the formulas stated in the chapter, and is labelled Illustrative in the captions.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
import numpy as np  # noqa: E402
from matplotlib.lines import Line2D  # noqa: E402
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Rectangle  # noqa: E402

from style import *  # noqa: E402,F401,F403  (applies the rcParams on import)

plt.rcParams["text.parse_math"] = False      # "$" is always a dollar sign in these figures

BLUE_TINT = "#dbe8f9"
ORANGE_TINT = "#fbe6dc"
GREY_TINT = "#f1f0ed"

REG, SRC, COMP = BLUE, ORANGE, MUTED     # colours for the three kinds of clock


# --------------------------------------------------------------------------------------------------
# Figure 1-B.1 (Cold Open): the week as five clock strips
# --------------------------------------------------------------------------------------------------
def fig_five_clocks():
    fig, ax = new_figure((7.0, 6.1))
    rows = ["Monday\nmarket maker", "Tuesday\nmulti-strategy pod", "Wednesday\nsystematic manager",
            "Thursday\nbank desk", "Friday\ndistressed fund"]
    n = len(rows)
    ypos = [n - 1 - i for i in range(n)]
    xmin, xmax = 5.4, 18.7

    # (hour, kind, label, side (+1 above / -1 below), ha)
    ev = {
        0: [(7 + 40 / 60, COMP, "7:40 vendor file restates\n1,900 CUSIPs", +1, "left"),
            (8.0, REG, "8:00 TRACE opens\n(15-min clock, 6730)", -1, "left"),
            (11 + 10 / 60, COMP, "11:10 fat-finger band\nrejects a 9-cent quote", +1, "left"),
            (11 + 25 / 60, REG, "11:25 rollback goes in the\n15c3-5 folder (annual)", -1, "left"),
            (16.5, SRC, "4:30 review of trades\ndone and not done", +1, "center")],
        1: [(5 + 55 / 60, COMP, "5:55 distance to\nthe stop line", +1, "left"),
            (7.25, SRC, "7:15 factor-model\n'x-ray' on the screen", -1, "left"),
            (10.25, "span", "9:30 CDX roll break, found\nby 11:00: about $140k", +1, "center"),
            (14 + 40 / 60, COMP, "2:40 trim; 3:00 risk call\n('which is the strategy?')", -1, "left"),
            (17 + 10 / 60, COMP, "5:10 x-ray\nrefreshes grey", +1, "right")],
        2: [(6 + 10 / 60, COMP, "6:10 load log: 312\ncorrections, 19 cancels", +1, "left"),
            (8.0, REG, "8:00 amber line: as/of\nvolume (Rule 6730)", -1, "left"),
            (11.0, COMP, "11:00 review: why did\nrank move 206 to 41?", +1, "left"),
            (13.5, COMP, "1:30 cause found:\na cancelled print", -1, "left"),
            (14.5, SRC, "2:30 $20mm sale: clips\nplus portfolio trade", +1, "left")],
        3: [(7 + 40 / 60, COMP, "7:40 unexplained \u2212$38k:\nwrong settlement date", +1, "left"),
            (9.0, REG, "9:00 best-ex review due\nin 2 weeks (Rule 5310)", -1, "left"),
            (12.25, SRC, "12:15 auto-quoter carries\nthe lunch hour", +1, "left"),
            (15.75, COMP, "", -1, "right"),
            (16 + 20 / 60, COMP, "", -1, "right"),
            (16 + 40 / 60, COMP, "3:45 'mark them at 79'; 4:20\nvaluation control rejects it;\n4:40 P&L email ties", -1, "right")],
        4: [(6.75, COMP, "6:45 restricted list:\nstill green", +1, "left"),
            (10 + 40 / 60, SRC, "10:40 signs the confi;\n10:52 list turns red", +1, "left"),
            (11.5, SRC, "11:30 sponsor call:\npass goes in the log", -1, "left"),
            (17 + 45 / 60, COMP, "5:45 Ad Hoc Group asks:\nhas anyone seen the 8-K?", +1, "right")],
    }

    for i, y in enumerate(ypos):
        ax.plot([xmin, xmax], [y, y], color=GRID, linewidth=2.0, zorder=1, solid_capstyle="round")
    # spans
    y_tue = ypos[1]
    ax.plot([9.5, 11.0], [y_tue, y_tue], color=COMP, linewidth=5.0, solid_capstyle="butt", zorder=3)
    y_fri = ypos[4]
    ax.add_patch(Rectangle((10 + 52 / 60, y_fri - 0.13), xmax - (10 + 52 / 60), 0.26, facecolor=ORANGE_TINT,
                           edgecolor="none", zorder=2))
    ax.annotate("", xy=(xmax + 0.15, y_fri), xytext=(xmax - 0.7, y_fri),
                arrowprops=dict(arrowstyle="-|>", color=ORANGE, lw=1.2), zorder=4, annotation_clip=False)
    ax.text(12.1, y_fri - 0.005, "restricted until the next 8-K (no date)", fontsize=7.5, color=INK, va="center",
            ha="left", zorder=4)

    for i, y in enumerate(ypos):
        for (h, kind, label, side, ha) in ev[i]:
            if kind != "span":
                ax.plot([h], [y], "o", color=kind, markersize=6.5, markeredgecolor="white", markeredgewidth=0.8,
                        zorder=6)
            if label:
                dy = 7 * side
                ax.annotate(label, (h, y), xytext=(0 if ha == "center" else (-2 if ha == "right" else 2), dy),
                            textcoords="offset points", ha=ha, va="bottom" if side > 0 else "top",
                            fontsize=7.5, color=INK_2, linespacing=1.15, zorder=6)

    ax.set_xlim(xmin, xmax)
    ax.set_ylim(-0.62, n - 1 + 0.62)
    ax.set_yticks(ypos)
    ax.set_yticklabels(rows, fontsize=8.5, color=INK, linespacing=1.2)
    ax.tick_params(axis="y", length=0)
    ax.set_xticks([6, 8, 10, 12, 14, 16, 18])
    ax.set_xticklabels(["6 a.m.", "8", "10", "noon", "2 p.m.", "4", "6"])
    ax.set_xlabel("Time of day (New York)")
    ax.grid(False)
    ax.spines["left"].set_visible(False)

    handles = [Line2D([], [], marker="o", color="none", markerfacecolor=REG, markersize=7, label="set by a rule"),
               Line2D([], [], marker="o", color="none", markerfacecolor=SRC, markersize=7,
                      label="routine from a public account"),
               Line2D([], [], marker="o", color="none", markerfacecolor=COMP, markersize=7, label="composite (the story)")]
    ax.legend(handles=handles, loc="lower left", bbox_to_anchor=(0.0, 1.0), ncol=3, columnspacing=1.4,
              handletextpad=0.3, borderaxespad=0.2, fontsize=8.5)
    return finish(fig, "ch01b_five_clocks")


# --------------------------------------------------------------------------------------------------
# Figure 1-B.2 (1B.2): the pair's ruler drifts
# --------------------------------------------------------------------------------------------------
def dts(face_mm, price, sd, spread_bp):
    """Market-value DTS in the chapter's units: face ($mm) x price/100 x spread duration x spread (bp)."""
    return face_mm * price / 100.0 * sd * spread_bp


def fig_dts_drift():
    k_apr = dts(60, 96, 3.6, 350)                 # long Kestrel at inception (about 72,600)
    h_face = dts(60, 90, 3.4, 600)                # $60mm Halvorsen matched on face (about 110,200)
    h_apr = dts(39, 90, 3.4, 600)                 # $39mm Halvorsen matched on DTS (about 71,600)
    k_tue = dts(60, 97, 3.6, 335)                 # Kestrel Tuesday morning (about 70,200)
    h_tue = dts(39, 78, 2.3, 1400)                # Halvorsen Tuesday morning (about 98,000)
    h_trim = dts(35, 78, 2.3, 1400)               # after cutting the short to $35mm (about 87,900)
    cdx = h_trim - k_tue                          # CDX HY protection sold to close the gap (about 17,700)

    groups = [
        ("April, face-matched\n$60mm vs $60mm", [k_apr], h_face),
        ("April, DTS-matched\n$60mm vs $39mm", [k_apr], h_apr),
        ("Tuesday morning,\nafter Friday's 83 to 78", [k_tue], h_tue),
        ("Tuesday 2:40: short cut\nto $35mm, CDX sold", [k_tue, cdx], h_trim),
    ]
    fig, ax = new_figure((7.0, 3.9))
    w, gap = 0.36, 0.04
    for g, (lab, longs, short) in enumerate(groups):
        x_long, x_short = g - (w + gap) / 2, g + (w + gap) / 2
        ax.bar(x_long, longs[0] / 1000, w, color=BLUE, zorder=3)
        if len(longs) > 1:
            ax.bar(x_long, longs[1] / 1000, w, bottom=longs[0] / 1000, color=VIOLET, zorder=3)
        ax.bar(x_short, short / 1000, w, color=ORANGE, zorder=3)
        tot_long = sum(longs)
        net = short - tot_long
        top = max(tot_long, short) / 1000
        if abs(net) < 1500:
            txt = "matched"
        else:
            txt = f"net short market\n{net / 1000:.0f}k ({100 * net / tot_long:.0f}% of a leg)"
        ax.annotate(txt, (g, top), xytext=(0, 5), textcoords="offset points", ha="center", va="bottom", fontsize=8,
                    color=INK if abs(net) >= 1500 else INK_2, fontweight="bold" if abs(net) >= 1500 else "normal")
        if len(longs) == 1:
            ax.annotate(f"{tot_long / 1000:.1f}", (x_long, tot_long / 1000), xytext=(0, -2), textcoords="offset points",
                        ha="center", va="top", fontsize=7.5, color="white", zorder=5)
        else:
            ax.annotate(f"{longs[0] / 1000:.1f}", (x_long, longs[0] / 1000), xytext=(0, -2), textcoords="offset points",
                        ha="center", va="top", fontsize=7.5, color="white", zorder=5)
            ax.annotate(f"+{longs[1] / 1000:.1f}", (x_long, tot_long / 1000), xytext=(0, -2), textcoords="offset points",
                        ha="center", va="top", fontsize=7.5, color="white", zorder=5)
        ax.annotate(f"{short / 1000:.1f}", (x_short, short / 1000), xytext=(0, -2), textcoords="offset points",
                    ha="center", va="top", fontsize=7.5, color="white", zorder=5)
    ax.set_xticks(range(len(groups)))
    ax.set_xticklabels([g[0] for g in groups], fontsize=8.5)
    ax.tick_params(axis="x", length=0)
    ax.set_ylim(0, 150)
    ax.set_ylabel("Market-value DTS (thousands)")
    ax.legend(handles=[Rectangle((0, 0), 1, 1, color=BLUE, label="long Kestrel 6% 2030"),
                       Rectangle((0, 0), 1, 1, color=VIOLET, label="CDX HY protection sold"),
                       Rectangle((0, 0), 1, 1, color=ORANGE, label="short Halvorsen 7.25% 2029")],
              loc="upper left", ncol=3, columnspacing=1.2, handlelength=1.0, handletextpad=0.5, fontsize=8.5,
              bbox_to_anchor=(0.0, 1.02))
    return finish(fig, "ch01b_dts_drift")


# --------------------------------------------------------------------------------------------------
# Figure 1-B.3 (1B.3): one cancelled print becomes a rank change
# --------------------------------------------------------------------------------------------------
def fig_trace_cascade():
    fig, ax = new_figure((7.0, 4.6))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 58)
    ax.axis("off")
    ax.grid(False)

    lane_x0 = 13.0
    colw = (100 - lane_x0) / 4.0
    bw, bh = colw - 2.2, 12.5
    cx = [lane_x0 + colw * (k + 0.5) for k in range(4)]
    lane_y = {"tape": 40.0, "model": 23.5, "arch": 7.0}       # centres of the three lanes
    heads = ["Monday", "Tuesday morning", "Tuesday evening", "Wednesday morning"]

    for k, h in enumerate(heads):
        ax.text(cx[k], 54.5, h, ha="center", va="center", fontsize=8.5, color=INK, fontweight="bold")
    for name, y in (("The tape\n(TRACE, the\npublic record)", lane_y["tape"]), ("The model\n(morning run)", lane_y["model"]),
                    ("The archive\n(point in time)", lane_y["arch"])):
        ax.text(0.5, y, name, ha="left", va="center", fontsize=8.5, color=INK_2, linespacing=1.2)
    for y in (lane_y["tape"], lane_y["model"], lane_y["arch"]):
        ax.plot([lane_x0 - 1.0, 100], [y - bh / 2 - 1.8] * 2, color=GRID, linewidth=0.7, zorder=0)

    def box(k, lane, text, edge, fill=GREY_TINT):
        x, y = cx[k], lane_y[lane]
        ax.add_patch(FancyBboxPatch((x - bw / 2, y - bh / 2), bw, bh, boxstyle="round,pad=0,rounding_size=1.2",
                                    facecolor=fill, edgecolor=edge, linewidth=1.1, zorder=2))
        ax.text(x, y, text, ha="center", va="center", fontsize=7.5, color=INK, linespacing=1.25, zorder=3)

    def arrow(p, q, color=INK_2, ls="-"):
        ax.add_patch(FancyArrowPatch(p, q, arrowstyle="-|>", mutation_scale=9, color=color, linewidth=1.1,
                                     linestyle=ls, zorder=4, shrinkA=0, shrinkB=0))

    # tape lane
    box(0, "tape", "A dealer reports a\nHalvorsen trade at 71\n(a keying error)", ORANGE, ORANGE_TINT)
    box(2, "tape", "The dealer cancels the\n71 and re-reports it\nas/of at 77", BLUE, BLUE_TINT)
    arrow((cx[0] + bw / 2, lane_y["tape"]), (cx[2] - bw / 2, lane_y["tape"]), color=MUTED, ls=(0, (4, 3)))
    ax.text((cx[0] + cx[2]) / 2, lane_y["tape"] + 1.6, "a day later", ha="center", va="bottom", fontsize=7.5, color=MUTED)

    # model lane
    box(1, "model", "Sees the 71:\nMonday  \u22129.0%\nTuesday +9.2%\nrank 206", ORANGE, ORANGE_TINT)
    box(3, "model", "Sees the 77:\nMonday  \u22121.3%\nTuesday +0.6%\nrank 41", BLUE, BLUE_TINT)
    arrow((cx[1] + bw / 2, lane_y["model"]), (cx[3] - bw / 2, lane_y["model"]), color=INK_2)
    xm = cx[2] + 0.12 * bw
    ax.text(xm, lane_y["model"] + 1.6, "moves 165\nplaces:", ha="center", va="bottom", fontsize=7.6, color=INK,
            fontweight="bold", linespacing=1.15)
    ax.text(xm, lane_y["model"] - 1.8, "nothing happened\nto the bond", ha="center", va="top", fontsize=7.6,
            color=INK, linespacing=1.2)

    # tape -> model
    arrow((cx[0] + bw * 0.25, lane_y["tape"] - bh / 2), (cx[1] - bw * 0.25, lane_y["model"] + bh / 2))
    arrow((cx[2] + bw * 0.25, lane_y["tape"] - bh / 2), (cx[3] - bw * 0.25, lane_y["model"] + bh / 2))

    # archive lane
    box(0, "arch", "Stores the 71\nknown at: Monday", NEUTRAL)
    box(2, "arch", "Stores the cancel\nand the 77\nknown at: Tue evening\nboth versions kept", NEUTRAL)
    box(3, "arch", "Back-test: reads what\nwas known Tuesday\n(rank 206).\nPerformance: reads\nthe corrected tape.", NEUTRAL)
    # tape -> archive, hugging the left edge of each column so nothing crosses the model lane's labels
    for k in (0, 2):
        arrow((cx[k] - bw * 0.40, lane_y["tape"] - bh / 2), (cx[k] - bw * 0.40, lane_y["arch"] + bh / 2), color=MUTED)
    return finish(fig, "ch01b_trace_cascade")


# --------------------------------------------------------------------------------------------------
# Figure 1-B.4 (1B.4): a tolerance in basis points is dollars; the Senate report's real figures
# --------------------------------------------------------------------------------------------------
def fig_tolerance_senate():
    fig, (a, b) = new_figure(ncols=2)

    # left: dollars the pen can move (chapter's CS01 arithmetic)
    cs01_halv = 6_000_000 * 0.78 * 2.3 * 0.0001           # about 1,080 per bp
    mid = 77.75
    dev_pts = 79 - mid                                     # 1.25 points
    dev_bp = dev_pts * 6_000_000 / 100 / cs01_halv         # about 70 bp
    rows = [
        ("Halvorsen $6mm,\nwithin a 6 bp tolerance", 6 * cs01_halv / 1000, BLUE),
        ("Halvorsen $6mm,\nmarked at 79\n(%d bp from mid)" % round(dev_bp), dev_pts * 6_000_000 / 100 / 1000, ORANGE),
        ("Index position,\nCS01 $50,000 per bp,\nwithin 6 bp", 6 * 50.0, BLUE),
    ]
    ys = np.arange(len(rows))[::-1]
    for y, (lab, v, c) in zip(ys, rows):
        a.barh(y, v, height=0.56, color=c, zorder=3)
        a.annotate(f"${v:,.1f}k" if v < 10 else f"${v:,.0f}k", (v, y), xytext=(4, 0), textcoords="offset points",
                   va="center", fontsize=8.5, color=INK)
    a.set_yticks(ys)
    a.set_yticklabels([r[0] for r in rows], fontsize=8)
    a.tick_params(axis="y", length=0)
    a.set_xlim(0, 380)
    a.set_xlabel("P&L a mark can move ($ thousand)")
    a.grid(False)
    a.spines["left"].set_visible(False)
    a.text(0.0, 1.02, "Basis points become dollars (illustrative)", transform=a.transAxes, fontsize=8.5, color=INK,
           fontweight="bold", ha="left", va="bottom")

    # right: the Senate report's figures (all real)
    def bar(y, v, c, txt):
        b.barh(y, v, height=0.62, color=c, zorder=3)
        b.annotate(txt, (v, y), xytext=(5, 0), textcoords="offset points", va="center", fontsize=8.5, color=INK)

    bar(5.8, 161, ORANGE, "Booked marks: $161mm")
    bar(5.0, 593, BLUE, "At mids: $593mm")
    bar(3.2, 690, NEUTRAL, "$690mm")
    yr = 1.0
    b.plot([719, 1200], [yr, yr], color=INK_2, linewidth=6.0, solid_capstyle="butt", zorder=3)
    b.annotate("$719mm to $1.2bn", ((719 + 1200) / 2, yr), xytext=(0, -7), textcoords="offset points", ha="center",
               va="top", fontsize=8.5, color=INK)
    b.text(0, 6.2, "Year-to-date loss, 12\u201316 Mar 2012", fontsize=8, color=INK_2, va="bottom")
    b.text(0, 3.75, "Peak collateral disputes:\ntwo marks on one position", fontsize=8, color=INK_2, va="bottom",
           linespacing=1.15)
    b.text(0, 1.45, "Controller: the book's value 'could\nlegitimately fall' within this range", fontsize=8,
           color=INK_2, va="bottom", linespacing=1.15)
    b.set_xlim(0, 1300)
    b.set_ylim(0.2, 7.0)
    b.set_yticks([])
    b.set_xlabel("$ million")
    b.grid(False)
    b.spines["left"].set_visible(False)
    b.text(0.0, 1.02, "Senate report figures (real)", transform=b.transAxes, fontsize=8.5, color=INK,
           fontweight="bold", ha="left", va="bottom")
    return finish(fig, "ch01b_tolerance_senate")


# --------------------------------------------------------------------------------------------------
# Figure 1-B.5 (1B.5): silence versus a uniform "no comment"
# --------------------------------------------------------------------------------------------------
def fig_silence_odds():
    N, talks = 1000, 50
    quiet_talks, quiet_not = 40, 95
    rows = [
        ("Prior: all 1,000 issuers", talks / N, f"{talks} in talks of {N:,}", "5.0%"),
        ("Big holders go quiet:\nthe 135 quiet names", quiet_talks / (quiet_talks + quiet_not),
         f"{quiet_talks} in talks of {quiet_talks + quiet_not}", "29.6%"),
        ("The fund sends the same\n'no comment' about every name", talks / N, f"{talks} in talks of {N:,}", "5.0%"),
    ]
    fig, ax = new_figure((7.0, 3.0))
    ys = np.arange(len(rows))[::-1]
    for y, (lab, p, cnt, pct) in zip(ys, rows):
        ax.barh(y, 100, height=0.52, color=GRID, zorder=2)
        ax.barh(y, 100 * p, height=0.52, color=BLUE, zorder=3)
        ax.annotate(f"{cnt}: {pct}", (100 * p, y), xytext=(6, 0), textcoords="offset points", va="center", fontsize=8.5,
                    color=INK, zorder=5)
    ax.set_yticks(ys)
    ax.set_yticklabels([r[0] for r in rows], fontsize=8.5)
    ax.tick_params(axis="y", length=0)
    ax.set_xlim(0, 100)
    ax.set_xlabel("Share of names in private talks with a holder group (%)")
    ax.grid(False)
    ax.spines["left"].set_visible(False)
    # multiplier notes on the right
    ax.annotate("probability \u00d7 6\n(odds \u00d7 8)", (97, ys[1]), ha="right", va="center", fontsize=8.5, color=INK,
                fontweight="bold")
    ax.annotate("\u00d7 1: carries no information", (97, ys[2]), ha="right", va="center", fontsize=8.5, color=INK,
                fontweight="bold")
    return finish(fig, "ch01b_silence_odds")


if __name__ == "__main__":
    fig_five_clocks()
    fig_dts_drift()
    fig_trace_cascade()
    fig_tolerance_senate()
    fig_silence_odds()
