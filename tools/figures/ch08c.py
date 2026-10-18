"""Chapter 8-C figures: The Morning Explain (P&L attribution that foots).

Run:  python3 tools/figures/ch08c.py      (writes assets/figures/ch08c_*.png)

Order of appearance in the chapter (figure numbers in the captions follow this order):
  8-C.1  ch08c_explain_waterfall   Monday's explain as a waterfall to the official -$399k      (8C.4)
  8-C.2  ch08c_signal_split        Which signal made the money: alone, sequential, Shapley      (8C.5)
  8-C.3  ch08c_two_mornings        The stale series before/after; the Corriveau true-up dispute (8C.6)
  8-C.4  ch08c_whale_shadow        The Senate report's shadow explain and the mark timeline     (8C.7)
  8-C.5  ch08c_unexplained_by_day  The unexplained by day over the third quarter                 (8C.9)

Data. Figures 1, 2, 3 and 5 are drawn from the chapter's own illustrative numbers (its Monday table,
its September signal numbers, its Corriveau dates, its quarterly ledger), so they are captioned
"Illustrative". Figure 5's 63 daily values are generated here: the 12 breaches are set to the ledger
table's cause totals (410, 260, 120, 95, 18 = 903 $k) and the quiet days are drawn from a seeded
Beta distribution scaled to the table's 290 $k. Figure 4 uses the numbers the chapter quotes from the
U.S. Senate PSI staff report on JPMorgan's CIO (15 March 2013), with the report's page numbers.

Colour roles, fixed across the explain figures (1, 3, 4); Figures 2 and 5 use BLUE and ORANGE only as the
first two categorical slots (momentum and value; calendar-day and other-day breaches), each named in its legend
or direct labels:
  BLUE   = the desk's own numbers: facts from custodian, clearing, blotter; the composite mark; the desk's marks
  ORANGE = a model's forecast: risk-model lines, the vendor's evaluated price
  AQUA   = an outside or corrected number: product control's correction, TRACE and dealer evidence,
           a price the desk did not choose (mids, an independent service) (slot 3, so every use is direct-labelled)
  INK_2  = the unexplained (no source), always
  pale blue band = the tolerance (+-$10k)
"""
import os
import sys
from datetime import date

sys.path.insert(0, os.path.dirname(__file__))
from style import *  # noqa: E402,F401,F403
import matplotlib.dates as mdates  # noqa: E402
import matplotlib.patheffects as pe  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib.ticker import FixedLocator  # noqa: E402
from matplotlib.patches import FancyBboxPatch, Rectangle  # noqa: E402

MINUS = "−"
C_FACT, C_MODEL, C_PC, C_U = BLUE, ORANGE, AQUA, INK_2
C_TOL = SEQ_BLUE_STEPS[0]
TOL = 10.0   # $k, the desk's tolerance min(1 bp of NAV, 5% of 1-day ES) on a $100mm book


def sgn(v, d=1, plus=True):
    """Signed number with a true minus sign."""
    s = f"{abs(v):,.{d}f}"
    if v < 0:
        return MINUS + s
    return ("+" if plus else "") + s


# --------------------------------------------------------------------------------------------
# 8-C.1  Monday's explain as a waterfall
# --------------------------------------------------------------------------------------------
def fig_waterfall():
    steps = [  # label, $k, class (fact / model); every number is the chapter's Monday table (8C.6)
        ("Coupon accrual, bonds (3 days)", 75.8, "fact"),
        ("Pull-to-par and roll-down", 12.4, "model"),
        ("Rates, bonds (key rates)", -52.0, "model"),
        ("Rates, Treasury futures", 40.0, "fact"),
        ("Spread factors, bonds", -338.0, "model"),
        ("CDX HY protection, price from factor", 110.0, "model"),
        ("CDX HY protection, coupon (3 days)", -16.7, "fact"),
        ("Idiosyncratic, bonds", -96.3, "model"),
        ("Convexity", 0.3, "model"),
        ("Financing", -15.0, "fact"),
        ("Fees and commissions", -4.0, "fact"),
        ("Day-one, fill vs composite", 3.5, "fact"),
    ]
    col = {"fact": C_FACT, "model": C_MODEL, "pc": C_PC, "u": C_U}
    rows = []   # (label, start, end, kind)
    cum = 0.0
    for lab, v, k in steps:
        rows.append((lab, cum, round(cum + v, 1), k))
        cum = round(cum + v, 1)
    assert abs(cum - (-280.0)) < 1e-6, cum
    rows.append(("Sum of named lines", 0.0, cum, "sub"))
    rows.append(("Mark correction pending: CDX old series", cum, round(cum - 110.0, 1), "pc"))
    cum = round(cum - 110.0, 1)
    rows.append(("Unexplained", cum, round(cum - 9.0, 1), "u"))
    cum = round(cum - 9.0, 1)
    assert abs(cum - (-399.0)) < 1e-6, cum
    rows.append(("Official P&L as booked", 0.0, cum, "tot"))
    n = len(rows)

    fig, ax = new_figure((7.2, 5.3))
    ax.set_axisbelow(True)
    for i, (lab, a, b, k) in enumerate(rows):
        if k == "sub":
            c = NEUTRAL
        elif k == "tot":
            c = INK
        else:
            c = col[k]
        ax.barh(i, b - a, left=a, height=0.66, color=c, zorder=3)
        # connector to the next step
        if k not in ("sub", "tot") and i + 1 < n and rows[i + 1][3] not in ("tot",):
            nxt = rows[i + 1]
            x = b if nxt[3] != "sub" else b
            ax.plot([x, x], [i + 0.33, i + 1 - 0.33], color=NEUTRAL, lw=0.7, zorder=2)
        if k == "sub":
            ax.plot([b, b], [i - 1 + 0.33, i - 0.33], color=NEUTRAL, lw=0.7, zorder=2)
        # value label at the end of the move, in its direction
        v = b - a
        if k in ("sub", "tot"):
            ax.text(b - 5, i, sgn(b), va="center", ha="right", fontsize=8.5, color=INK, fontweight="bold")
        elif v >= 0:
            ax.text(max(a, b) + 5, i, sgn(v), va="center", ha="left", fontsize=8.5, color=INK_2)
        else:
            ax.text(min(a, b) - 5, i, sgn(v), va="center", ha="right", fontsize=8.5, color=INK_2)

    # tolerance band around the explained total (the official number must land inside it)
    explained = -390.0
    ax.add_patch(Rectangle((explained - TOL, n - 3 - 0.45), 2 * TOL, 3 * 1.0 - 0.1, color=C_TOL, zorder=1, lw=0))
    ax.text(explained + TOL + 8, n - 2, "tolerance band " + "\u00b1" + "$10k around the explained total", va="center",
            ha="left", fontsize=8, color=MUTED)

    ax.set_yticks(range(n))
    ax.set_yticklabels([r[0] for r in rows], fontsize=8.5)
    for t, r in zip(ax.get_yticklabels(), rows):
        if r[3] in ("sub", "tot"):
            t.set_fontweight("bold")
            t.set_color(INK)
    ax.set_ylim(n - 0.4, -0.7)
    ax.set_xlim(-492, 138)
    ax.axvline(0, color=INK_2, lw=0.8, zorder=2)
    ax.set_xlabel("Cumulative P&L, three-day Monday ($ thousands)")
    ax.grid(axis="y", visible=False)
    ax.grid(axis="x", visible=True)
    ax.tick_params(axis="y", length=0)

    # zoom: the unexplained against the tolerance, in the empty lower right of the plot
    ins = ax.inset_axes([0.70, 0.30, 0.285, 0.265])
    ins.axhspan(-0.5, 0.5, xmin=0, xmax=1, color="white")
    ins.add_patch(Rectangle((-TOL, -0.5), 2 * TOL, 1.0, color=C_TOL, lw=0, zorder=1))
    ins.barh(0, -9.0, height=0.5, color=C_U, zorder=3)
    ins.set_xlim(-26, 26)
    ins.set_ylim(-0.5, 0.5)
    ins.set_yticks([])
    ins.set_xticks([-20, -10, 0, 10, 20])
    ins.tick_params(labelsize=8, length=2)
    ins.grid(False)
    ins.spines["left"].set_visible(False)
    ins.text(-9.0, 0.36, "U = " + MINUS + "9.0", fontsize=8, color=INK, ha="center", va="center")
    ins.text(TOL - 0.8, -0.36, "inside \u00b110", fontsize=8, color=MUTED, ha="right", va="center")
    ttl = ins.set_title("Zoom: unexplained\nvs tolerance ($k)", fontsize=8, loc="left", fontweight="normal", color=INK_2, linespacing=1.15)
    ttl.set_bbox(dict(facecolor="white", edgecolor="none", pad=1.5))

    from matplotlib.patches import Patch
    handles = [Patch(color=C_FACT, label="Fact (custodian, exchange, clearing, treasury, blotter)"),
               Patch(color=C_MODEL, label="Model forecast (risk model x market moves)"),
               Patch(color=C_PC, label="Product control correction"),
               Patch(color=C_U, label="Unexplained (no source)")]
    fig.legend(handles=handles, loc="outside lower center", ncol=2, fontsize=8, handlelength=1.2,
               columnspacing=1.5)
    return finish(fig, "ch08c_explain_waterfall")


# --------------------------------------------------------------------------------------------
# 8-C.2  Which signal made the money?
# --------------------------------------------------------------------------------------------
def fig_signal_split():
    M_alone, V_alone, book = 3.0, 2.0, 2.4
    inter = book - M_alone - V_alone                    # -2.6
    shap_M = 0.5 * (M_alone + (book - V_alone))         # 1.7
    shap_V = 0.5 * (V_alone + (book - M_alone))         # 0.7
    assert abs(inter + 2.6) < 1e-9 and abs(shap_M - 1.7) < 1e-9 and abs(shap_V - 0.7) < 1e-9
    groups = [
        ("Run alone\n(books that\nnever existed)", [("M", M_alone), ("V", V_alone)]),
        ("Sequential,\nmomentum first", [("M", M_alone), ("V", book - M_alone)]),
        ("Sequential,\nvalue first", [("V", V_alone), ("M", book - V_alone)]),
        ("Equal split\n= Shapley", [("M", shap_M), ("V", shap_V)]),
    ]
    col = {"M": BLUE, "V": ORANGE}
    name = {"M": "Momentum", "V": "Value"}

    fig, ax = new_figure((7.0, 3.9))
    ax.set_axisbelow(True)
    w = 0.40
    halo = [pe.withStroke(linewidth=3, foreground='white')]
    for gi, (lab, parts) in enumerate(groups):
        pos, neg = 0.0, 0.0
        for key, v in parts:
            if v >= 0:
                bottom = pos
                pos += v
            else:
                bottom = neg + v
                neg += v
            ax.bar(gi, abs(v), bottom=bottom, width=w, color=col[key], zorder=3,
                   edgecolor="white", linewidth=1.2)
            ymid = bottom + abs(v) / 2
            ax.plot([gi + w / 2], [ymid], "o", color=col[key], markersize=4, zorder=5)
            dy = -5 if abs(v) < 0.5 else 0   # a short top segment: label nudged down so the 2.4 line does not cross it
            ax.annotate(f"{name[key]}\n{sgn(v, plus=False)}", (gi + w / 2, ymid), xytext=(5, dy), textcoords="offset points",
                        va="center", fontsize=8, color=INK_2, path_effects=halo, zorder=6, linespacing=1.15)
        if gi == 0:
            # the interaction: the gap between the sum of the standalone books and the book that was held
            ax.add_patch(Rectangle((gi - w / 2, book), w, M_alone + V_alone - book, fill=False,
                                   edgecolor=INK_2, linestyle=(0, (3, 2)), linewidth=1.1, zorder=4))
            ax.annotate("interaction\n" + MINUS + "2.6", (gi + w / 2, 2.85), xytext=(5, 0),
                        textcoords="offset points", ha="left", va="center", fontsize=8, color=INK, zorder=5,
                        linespacing=1.15, fontweight="bold")
            ax.text(gi, M_alone + V_alone + 0.12, "sum 5.0", ha="center", va="bottom", fontsize=8.5, color=INK_2)
        else:
            ax.text(gi, max(pos, 0) + 0.12, "= 2.4", ha="center", va="bottom", fontsize=8.5, color=INK_2)
    ax.axhline(book, color=INK_2, lw=0.9, linestyle=(0, (4, 3)), zorder=2)
    ax.text(4.1, book + 0.1, "the book that held\nboth made $2.4mm", ha="right", va="bottom", fontsize=8,
            color=MUTED, linespacing=1.15)
    ax.axhline(0, color=INK_2, lw=0.8, zorder=2)
    ax.set_xticks(range(len(groups)))
    ax.set_xticklabels([g[0] for g in groups], fontsize=8.5)
    ax.tick_params(axis="x", length=0)
    ax.set_ylim(-1.1, 5.9)
    ax.set_xlim(-0.55, 4.15)
    ax.set_ylabel("Attributed P&L, September ($mm)")
    return finish(fig, "ch08c_signal_split")


# --------------------------------------------------------------------------------------------
# 8-C.3  The two mornings
# --------------------------------------------------------------------------------------------
def fig_two_mornings():
    fig = plt.figure(figsize=(7.4, 3.9), layout="constrained")
    gs = fig.add_gridspec(1, 2, width_ratios=[1.0, 1.7])
    axL = fig.add_subplot(gs[0])
    axR = fig.add_subplot(gs[1])

    # ---- left: morning (a), the unexplained before and after the 9:40 correction ($k)
    axL.set_axisbelow(True)
    axL.axhspan(-TOL, TOL, color=C_TOL, zorder=1, lw=0)
    w = 0.5
    # as found: bond residuals -9 (just below zero), the stale-series signature -110 below that
    axL.bar(0, -9.0, width=w, color=C_U, zorder=3, edgecolor="white", linewidth=1.0)
    axL.bar(0, -110.0, bottom=-9.0, width=w, color=C_PC, zorder=3, edgecolor="white", linewidth=1.0)
    axL.bar(1, -9.0, width=w, color=C_U, zorder=3, edgecolor="white", linewidth=1.0)
    axL.text(0, -119 - 5, MINUS + "119", ha="center", va="top", fontsize=9, color=INK, fontweight="bold")
    axL.text(1, -9 - 5, MINUS + "9", ha="center", va="top", fontsize=9, color=INK, fontweight="bold")
    # direct labels (right of the bars)
    label_end(axL, 0 + w / 2, -9.0 - 55, "stale-series\nsignature\n" + MINUS + "110", C_PC, dx=5)
    label_end(axL, 1 + w / 2, -4.5, "bond\nresiduals", C_U, dx=5)
    axL.text(-0.45, 12, "tolerance \u00b110", fontsize=8, color=MUTED, ha="left", va="bottom")
    axL.axhline(0, color=INK_2, lw=0.8, zorder=2)
    axL.set_xticks([0, 1])
    axL.set_xticklabels(["As found\n7:15", "Corrected\n9:40"], fontsize=8.5)
    axL.tick_params(axis="x", length=0)
    axL.set_xlim(-0.55, 2.3)
    axL.set_ylim(-146, 24)
    axL.set_ylabel("Unexplained U, Monday ($ thousands)")
    axL.set_title("Morning (a): the stale series", fontsize=9.5)

    # ---- right: morning (b), the Corriveau true-up on a timeline of the evidence
    ax = axR
    def D(day, month=10):
        return mdates.date2num(date(2026, month, 1)) + day - 1
    ax.set_axisbelow(True)
    # composite history, nine days between 84.2 and 84.6, ending in the 84.50 carry
    ax.add_patch(Rectangle((D(21), 84.2), D(30) - D(21), 0.4, color=SEQ_BLUE_STEPS[3], zorder=2, lw=0))
    ax.plot([D(30), D(3, 11)], [84.5, 84.5], color=C_FACT, lw=1.0, linestyle=(0, (3, 2)), zorder=2)
    ax.text(D(21), 84.78, "composite history\n84.2–84.6 (nine days)", ha="left", va="bottom", fontsize=8,
            color=INK_2, linespacing=1.15)
    ax.text(D(3, 11) + 0.25, 84.5, "carried at 84.50", ha="left", va="center", fontsize=8, color=INK_2)
    ax.plot([D(30)], [84.5], marker="o", color=C_FACT, markersize=4, zorder=5)
    # evidence: the TRACE print and the two dealer runs
    ax.plot([D(21)], [84.25], marker="D", color=C_PC, markersize=6, zorder=5, markeredgecolor="white")
    ax.annotate("TRACE print\n84.25, $2mm, 21 Oct", (D(21), 84.25), xytext=(2, -26), textcoords="offset points",
                ha="left", va="top", fontsize=8, color=INK_2)
    for off, lo, hi in [(-0.22, 84.0, 85.0), (0.22, 83.75, 85.0)]:
        ax.plot([D(30) + off, D(30) + off], [lo, hi], color=C_PC, lw=3.2, solid_capstyle="butt", zorder=4)
    ax.annotate("dealer runs, 30 Oct\n84–85 and 83¾–85", (D(30) + 0.22, 85.0), xytext=(6, 2),
                textcoords="offset points", ha="left", va="bottom", fontsize=8, color=INK_2, linespacing=1.15)
    # the neighbour's news
    ax.axvline(D(29), color=NEUTRAL, lw=0.9, linestyle=(0, (3, 3)), zorder=1)
    ax.annotate("29 Oct: a neighbour's\nliability-management deal,\n" + MINUS + "9 points", (D(29), 82.3),
                xytext=(-3, 0), textcoords="offset points", ha="right", va="center", fontsize=8, color=INK_2)
    # vendor's evaluated price and the revision
    ax.plot([D(2, 11), D(3, 11)], [81.5, 84.0], color=C_MODEL, lw=LW, zorder=3)
    ax.plot([D(2, 11), D(3, 11)], [81.5, 84.0], "o", color=C_MODEL, markersize=6, zorder=5, markeredgecolor="white")
    ax.annotate("evaluated 81.50\ntrue-up " + MINUS + "$240k", (D(2, 11), 81.5), xytext=(-8, -2), textcoords="offset points",
                ha="right", va="center", fontsize=8.5, color=INK, fontweight="bold")
    ax.annotate("revised 84.00\n(3 Nov)\ntrue-up " + MINUS + "$40k", (D(3, 11), 84.0), xytext=(8, -14),
                textcoords="offset points", ha="left", va="center", fontsize=8.5, color=INK, fontweight="bold")
    ax.annotate("", xy=(D(2, 11), 81.62), xytext=(D(2, 11), 84.5),
                arrowprops=dict(arrowstyle="-|>", color=INK_2, lw=0.9, linestyle=(0, (2, 2)), shrinkA=0, shrinkB=0))
    ax.annotate("challenge\nfiled 2 Nov,\n11:00", (D(2, 11), 83.2), xytext=(-4, 0), textcoords="offset points",
                ha="right", va="center", fontsize=8, color=INK_2, linespacing=1.15)
    ax.set_xlim(D(19.6), D(9, 11))
    ax.set_ylim(80.9, 86.2)
    ax.set_yticks([81, 82, 83, 84, 85, 86])
    ax.xaxis.set_major_locator(FixedLocator([D(21), D(26), D(30), D(2, 11)]))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%-d %b"))
    ax.set_ylabel("Corriveau 9.5% notes (price, points of par)")
    ax.set_title("Morning (b): the Corriveau true-up", fontsize=9.5)
    return finish(fig, "ch08c_two_mornings")


# --------------------------------------------------------------------------------------------
# 8-C.4  The Whale's shadow explain
# --------------------------------------------------------------------------------------------
def fig_whale():
    fig = plt.figure(figsize=(7.4, 4.6), layout="constrained")
    gs = fig.add_gridspec(1, 2, width_ratios=[1.0, 2.05])
    axL = fig.add_subplot(gs[0])
    axR = fig.add_subplot(gs[1])

    # ---- left: the shadow spreadsheet, 12-16 March 2012 (PSI report p.5)
    axL.set_axisbelow(True)
    w = 0.55
    axL.bar(0, 161, width=w, color=C_FACT, zorder=3)
    axL.bar(1, 593, width=w, color=C_PC, zorder=3)
    axL.plot([-0.45, 1.45], [161, 161], color=INK_2, lw=0.9, linestyle=(0, (4, 3)), zorder=4)
    axL.add_patch(Rectangle((1 - w / 2, 161), w, 432, facecolor="none", edgecolor=INK_2, hatch="////", lw=0,
                            zorder=4, alpha=0.9))
    axL.annotate("", xy=(1.42, 593), xytext=(1.42, 161), arrowprops=dict(arrowstyle="<->", color=INK_2, lw=1.0))
    axL.text(1.5, 377, "unexplained\n$432mm", ha="left", va="center", fontsize=8.5, color=INK, fontweight="bold")
    axL.text(0, 161 + 14, "161", ha="center", va="bottom", fontsize=9, color=INK, fontweight="bold")
    axL.text(1, 593 + 14, "593", ha="center", va="bottom", fontsize=9, color=INK, fontweight="bold")
    axL.set_xticks([0, 1])
    axL.set_xticklabels(["Reported\n(desk's\nmarks)", "At mids\n(shadow\nsheet)"], fontsize=8.5)
    axL.tick_params(axis="x", length=0)
    axL.set_xlim(-0.6, 2.35)
    axL.set_ylim(0, 690)
    axL.set_ylabel("Year-to-date loss, 12–16 March 2012 ($mm)")

    # ---- right: who set the price, as a dated list (ordinal spacing, not to scale)
    ax = axR
    ax.set_axis_off()
    events = [
        ("End 2011", "Net notional “over $51 billion” (p.185).", "own"),
        ("Early Jan", "Marks set “at or near the midpoint” of the daily range (p.5).", "own"),
        ("Later", "The book began to assign “more favorable prices within the daily price range” (p.5).", "own"),
        ("12–16 Mar", "Marker keeps a spreadsheet of the differences: $161mm reported, $593mm at mids (p.5).", "own"),
        ("30 Mar", "Reported daily loss $319mm; a $512mm gap later recorded by the Valuation Control Group (p.5). "
                   "Net notional now “over $157 billion” (p.185).", "own"),
        ("10 Apr", "Estimated daily loss of about $6mm re-issued 90 minutes later (p.5).", "own"),
        ("May", "CIO told to mark as the Investment Bank does, from an independent pricing service; "
                "collateral disputes (peak $690mm) resolve for the counterparties (p.6).", "out"),
        ("13 Jul", "Q1 restated for an additional $660mm of losses (p.98).", "out"),
    ]
    n = len(events)
    ys = np.linspace(0.95, 0.04, n)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    spine_x = 0.215
    # the line colours say whose price the P&L foots to
    ym = 0.5 * (ys[5] + ys[6])
    ax.plot([spine_x, spine_x], [ys[0], ym], color=C_FACT, lw=3.2, solid_capstyle="butt", zorder=2)
    ax.plot([spine_x, spine_x], [ym, ys[7]], color=C_PC, lw=3.2, solid_capstyle="butt", zorder=2)
    import textwrap
    for (when, what, who), y in zip(events, ys):
        c = C_FACT if who == "own" else C_PC
        ax.plot([spine_x], [y], "o", color="white", markersize=9, zorder=3, markeredgecolor=c, markeredgewidth=2)
        ax.text(spine_x - 0.035, y, when, ha="right", va="center", fontsize=8.5, color=INK, fontweight="bold")
        lines = []
        for para in what.split("\n"):
            lines += textwrap.wrap(para, 54) or [""]
        ax.text(spine_x + 0.04, y, "\n".join(lines).replace("$", "\\$"), ha="left", va="center", fontsize=8, color=INK_2,
                linespacing=1.2)
    ax.text(0.0, -0.005, "Dates and page numbers as quoted in section 8C.7; spacing is not to scale.", fontsize=8,
            color=MUTED, ha="left", va="top")
    from matplotlib.lines import Line2D
    handles = [Line2D([0], [0], color=C_FACT, lw=3.2, label="The desk's own marks"),
               Line2D([0], [0], color=C_PC, lw=3.2, label="A price the desk did not choose (mids; from May, an independent service)")]
    fig.legend(handles=handles, loc="outside lower center", ncol=2, fontsize=8, handlelength=1.8,
               columnspacing=1.6)
    return finish(fig, "ch08c_whale_shadow")


# --------------------------------------------------------------------------------------------
# 8-C.5  The unexplained by day, third quarter
# --------------------------------------------------------------------------------------------
def quarter_series():
    """63 trading days (three 21-day months). Returns dict day -> list of (value $k, special?) breaches
    and the quiet-day array. Cause totals follow the ledger table of section 8C.9."""
    month_end = [21, 42, 63]
    roll_week = [56, 57, 58]          # Mon 21 - Wed 23 Sep when 30 Sep is day 63
    special = set(month_end + roll_week)
    breaches = {
        # month-end true-ups, 4 breaches, sum |U| = 410
        21: [-105.0], 42: [-95.0, -60.0], 63: [150.0],
        # stale or mismapped index marks in roll week, 3 breaches, sum |U| = 260 (Monday's -119 is the chapter's)
        56: [-119.0], 57: [-85.0], 58: [56.0],
        # booking errors 2 (120), corporate actions and identifiers 2 (95), timing and snap 1 (18)
        15: [-56.0], 48: [-64.0], 29: [-55.0], 51: [40.0], 33: [18.0],
    }
    tot = sum(abs(v) for vs in breaches.values() for v in vs)
    assert sum(len(v) for v in breaches.values()) == 12 and abs(tot - 903.0) < 1e-9, tot
    assert sum(len(breaches[d]) for d in special) == 7
    quiet_days = [d for d in range(1, 64) if d not in breaches]
    rng = np.random.default_rng(80)
    a = rng.beta(2.0, 1.5, len(quiet_days))
    for _ in range(200):
        a = np.clip(a * (290.0 / a.sum()), 0.4, 9.8)
    a = a * (290.0 / a.sum())
    assert a.max() < TOL and abs(a.sum() - 290.0) < 1e-9
    signs = rng.permutation(np.array([1.0, -1.0] * (len(a) // 2) + [1.0] * (len(a) % 2)))
    quiet = a * signs
    return breaches, special, dict(zip(quiet_days, quiet))


def fig_unexplained_by_day():
    breaches, special, quiet = quarter_series()
    fig, ax = new_figure("wide")
    ax.set_axisbelow(True)
    ax.axhspan(-TOL, TOL, color=C_TOL, zorder=1, lw=0)
    ax.axvspan(55.5, 58.5, color=GRID, zorder=0, lw=0)   # grey, so pale blue stays the tolerance only
    for xe in (55.5, 58.5):
        ax.axvline(xe, color=NEUTRAL, lw=0.9, linestyle=(0, (3, 3)), zorder=1)
    for d, v in quiet.items():
        ax.bar(d, v, width=0.78, color=NEUTRAL, zorder=3)
    for d, vs in breaches.items():
        c = C_FACT if d in special else C_MODEL
        pos = neg = 0.0
        for v in vs:
            bottom = pos if v >= 0 else neg
            ax.bar(d, v, bottom=bottom, width=0.78, color=c, zorder=3, edgecolor="white", linewidth=1.0)
            if v >= 0:
                pos += v
            else:
                neg += v
    ax.axhline(0, color=INK_2, lw=0.8, zorder=2)
    # month-end lines
    for d, nm in zip([21, 42], ["Jul month-end", "Aug month-end"]):
        mark_event(ax, d, nm, y_frac=0.99)
    ax.axvline(63, color=NEUTRAL, lw=0.9, linestyle=(0, (3, 3)), zorder=1)
    ax.annotate("Sep\nmonth-end", (63, 0.99), xycoords=("data", "axes fraction"), xytext=(-8, 0),
                textcoords="offset points", fontsize=8, color=INK_2, va="top", ha="right", linespacing=1.15)
    ax.text(55.0, 112, "roll week", ha="right", va="center", fontsize=8, color=INK_2)
    ax.annotate("Mon 21 Sep:\nstale CDX series,\n" + MINUS + "$119k as found", (55.6, -119), xytext=(-4, -2),
                textcoords="offset points", fontsize=8, color=INK_2, va="center", ha="right", linespacing=1.15)
    ax.annotate("two true-ups\non one day", (41.6, -105), xytext=(-2, 0), textcoords="offset points",
                fontsize=8, color=INK_2, va="center", ha="right", linespacing=1.15)
    ax.text(0.5, TOL + 3, "tolerance " + "±" + "$10k", fontsize=8, color=MUTED, ha="left", va="bottom")
    ax.set_xlim(0, 64)
    ax.set_ylim(-190, 175)
    ax.set_xticks([1, 11, 21, 31, 42, 52, 63])
    ax.set_xlabel("Trading day of the third quarter (63 days; three 21-day months)")
    ax.set_ylabel("Unexplained U ($ thousands)")
    from matplotlib.patches import Patch
    handles = [Patch(color=NEUTRAL, label="inside tolerance"),
               Patch(color=C_FACT, label="breach on a month-end or roll-week day (7)"),
               Patch(color=C_MODEL, label="breach on any other day (5)")]
    fig.legend(handles=handles, loc="outside lower center", ncol=3, fontsize=8, handlelength=1.2,
               columnspacing=1.5)
    return finish(fig, "ch08c_unexplained_by_day")


if __name__ == "__main__":
    fig_waterfall()
    fig_signal_split()
    fig_two_mornings()
    fig_whale()
    fig_unexplained_by_day()
