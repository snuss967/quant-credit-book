"""Chapter 9-B figures: The Bond Data Problem and the Replication Crisis.

Run:  python3 tools/figures/ch09b.py      (writes assets/figures/ch09b_*.png; no network needed)

Order of appearance in the chapter (the numbers in the captions follow this order):
  9-B.1  ch09b_stage0_pipeline   The Stage 0 order as a flow graph, with the Brambleworth Monday threaded through   (9B.2)
  9-B.2  ch09b_two_prices        One bond, one month-end, two prices (existing embed)                               (9B.3)
  9-B.3  ch09b_lib_waterfall     Table 1 premia: unadjusted, signal gap, return gap (existing embed)                (9B.4)
  9-B.4  ch09b_mom6_trimming     Six-month momentum alpha against the trimming threshold (existing embed)           (9B.5)
  9-B.5  ch09b_two_leg_bounce    A two-leg pair's P&L from raw prints and from filtered prints (existing embed)     (9B.7)

Data.
  9-B.3 is REAL: Dickerson, Robotti and Rossetti (2026), arXiv:2604.07880v1, Table 1 Panel A (value-weighted decile
    long-short premia, monthly %, 2002-09 to 2024-12, T = 268; t-statistics Newey-West).  The numbers were read from the
    arXiv PDF and agree with state/research/papers_factor_replication_crisis_and_bond_data.md section 3.2.
  9-B.4 is REAL: the alphas and 95% intervals of the paper's Figure 6 (p. 26), read from the vector graphics of the PDF
    and stored in tools/figures/data/ch09b_drr_fig6_mom6_alpha.csv.  The anchor points the chapter states (about 0.60%
    at a 10% right-tail cut, zero near -40% on the left) are asserted against it.
  9-B.1 draws the pipeline from the chapter's own Stage 0 description (README_stage0 of the OBAP trace-data-pipeline,
    v4.2.1, as summarised in the dossier, section 3.1); the Brambleworth counts are the chapter's illustrative example.
  9-B.2 and 9-B.5 are ILLUSTRATIVE (stated model in each function; not real prints).

Colour roles, fixed across the chapter's figures:
  Price variants (9-B.2, 9-B.3):  MUTED gray = unadjusted (signal and return share the month-end price),
                                  BLUE = signal gap (signal read from an earlier price), ORANGE = return gap (month-begin price)
  Tails (9-B.4):                  BLUE = left tail trimmed, ORANGE = right tail trimmed; dashed with open markers = ex ante,
                                  solid with filled markers = ex post
  Pipeline stripe (9-B.1):        BLUE = rewrites a price, ORANGE = deletes or flags rows, gray = input or builds the panel
  Raw vs clean (9-B.5):           MUTED gray = raw prints, INK black = bounce-filtered prices
"""
import csv
import os
import sys
import textwrap

sys.path.insert(0, os.path.dirname(__file__))
from style import *  # noqa: E402,F401,F403
import numpy as np  # noqa: E402
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Rectangle  # noqa: E402

plt.rcParams["text.parse_math"] = False      # dollar signs in labels are literal
plt.rcParams["axes.axisbelow"] = True        # grid lines sit behind the bars

MINUS = "−"
HERE = os.path.dirname(os.path.abspath(__file__))


def sgn(v, d=2):
    """Signed number with a true minus sign."""
    s = f"{abs(v):.{d}f}"
    return (MINUS + s) if v < 0 and float(s) != 0 else s


# ---------------------------------------------------------------------------------------------------------------
# 9-B.1  The Stage 0 order as a flow graph
# ---------------------------------------------------------------------------------------------------------------
def fig_stage0_pipeline():
    UNIT = 0.0695                      # inches per data unit, the same in x and y (100 units across 6.95 in)
    W = 22.6
    GAP = (100 - 4 * W) / 3
    col_x = [i * (W + GAP) for i in range(4)]
    stripe = {"input": MUTED, "rewrite": BLUE, "delete": ORANGE, "build": MUTED}
    L_TITLE, L_BODY, PAD = 1.95, 1.75, 1.6
    WT, WB = 20, 26                    # wrap widths (characters) for titles and body lines

    # (row, col, kind, title, body, risk, tag); rows 1 and 2 run right to left in the reading order
    nodes = [
        (0, 0, "input", "Raw TRACE tape",
         "Every report: status T, X, C, R or Y, capacity A or P, sizes capped at 1MM+ and 5MM+.",
         None, "Brambleworth: 8 rows"),
        (0, 1, "rewrite", "Step 0  Price scale",
         "Puts quotes per $1,000 or as a decimal of par on one scale, so 850 and 0.85 both become 85.",
         None, None),
        (0, 2, "delete", "Step 1  Dick-Nielsen clean-up",
         "Removes cancels, corrections and reversals, and keeps one row for an agency pass.",
         None, "8 rows become 3"),
        (0, 3, "rewrite", "Step 2  Decimal-shift corrector",
         "A print over 5% off the median of the last 11 prices is tried at \u00d70.1, \u00d70.01, \u00d710 and "
         "\u00d7100, and kept if within 2%.",
         "a real crash (90 to 9) read as a typo.", "8.5125 becomes 85.125"),
        (1, 3, "delete", "Steps 3-6  Calendar and range",
         "Keeps NYSE business days and prices above 0 and up to 1,000. The intraday window is off.",
         "the volume screen (off) would drop small trades, a choice with a sign.", None),
        (1, 2, "delete", "Step 7  Bounce-back filter",
         "Drops a print 35 points from the median of the last 5 prices that returns within 5 rows. "
         "Flags 3 or more prints at par.",
         "a liability-management gap that is partly walked back.", None),
        (1, 1, "delete", "Steps 8-11  Booking errors",
         "Drops a price equal to the yield, a trade over half the offering, a trade after maturity, "
         "a bond with a 50-point move after 3 prints.",
         "a rare genuine block.", None),
        (1, 0, "delete", "Daily stage  Distressed bonds",
         "Over 5-day windows, flags prices under 0.10, spikes above 5.0 that fall back and "
         "plateaus of identical days under 0.15.",
         "a real two-cent bond looks like a typo.", None),
        (2, 0, "build", "Month price",
         "The last daily VWAP in the final 5 NYSE business days. No print in the window, no return that month.",
         None, None),
        (2, 1, "build", "Two returns",
         "r_End starts from the month-end price, r_Bgn from the first price of the next month. "
         "Their difference is the gap (9B.3).", None, None),
        (2, 2, "build", "Bond-month panel",
         "Defaults stay in: no coupon in the default month, then the bond trades flat. "
         "Every filter is dated before the first return.", None, None),
    ]

    def lay(node):
        row, col, kind, title, body, risk, tag = node
        t = textwrap.fill(title, WT)
        b = textwrap.fill(body, WB)
        r = textwrap.fill("Risk: " + risk, WB) if risk else ""
        h = (PAD + L_TITLE * len(t.split("\n")) + 1.0 + L_BODY * len(b.split("\n"))
             + (1.2 + L_BODY * len(r.split("\n")) if r else 0) + (1.2 + L_BODY if tag else 0) + PAD)
        return t, b, r, h

    laid = [lay(n) for n in nodes]
    row_h = [max(l[3] for n, l in zip(nodes, laid) if n[0] == r) for r in range(3)]
    ROW_GAP = 5.0
    total = sum(row_h) + 2 * ROW_GAP
    row_top = [total, total - row_h[0] - ROW_GAP, total - row_h[0] - row_h[1] - 2 * ROW_GAP]

    fig, ax = new_figure((7.0, (total + 2.4) * UNIT + 0.15))
    ax.set_xlim(-1.2, 101.2)
    ax.set_ylim(-1.2, total + 1.2)
    ax.axis("off")
    ax.grid(False)

    for node, (t, b, r, _) in zip(nodes, laid):
        row, col, kind, _t, _b, risk, tag = node
        x, ytop, H = col_x[col], row_top[row], row_h[row]
        y = ytop - H
        ax.add_patch(FancyBboxPatch((x, y), W, H, boxstyle="round,pad=0,rounding_size=0.9", fc=SURFACE,
                                    ec=NEUTRAL, lw=0.9, zorder=2))
        ax.add_patch(Rectangle((x + 0.9, y + 0.9), 1.1, H - 1.8, fc=stripe[kind], ec="none", zorder=3))
        tx = x + 3.3
        ax.text(tx, ytop - PAD, t, ha="left", va="top", fontsize=7.6, fontweight="bold", color=INK, zorder=4,
                linespacing=1.15)
        yb = ytop - PAD - L_TITLE * len(t.split("\n")) - 1.0
        ax.text(tx, yb, b, ha="left", va="top", fontsize=6.7, color=INK_2, zorder=4, linespacing=1.2)
        if r:
            yr = yb - L_BODY * len(b.split("\n")) - 1.2
            ax.text(tx, yr, r, ha="left", va="top", fontsize=6.7, color=INK, zorder=4, linespacing=1.2,
                    fontstyle="italic")
        if tag:
            ax.text(tx, y + PAD, tag, ha="left", va="bottom", fontsize=6.7, color=INK, fontweight="bold",
                    zorder=4)

    def arrow(p, q):
        ax.add_patch(FancyArrowPatch(p, q, arrowstyle="-|>", mutation_scale=8, lw=1.1, color=INK_2, zorder=5,
                                     shrinkA=0, shrinkB=0))

    for row, going_right, n_arrows in ((0, True, 3), (1, False, 3), (2, True, 2)):
        ymid = row_top[row] - row_h[row] / 2
        for c in range(n_arrows):
            if going_right:
                arrow((col_x[c] + W + 0.15, ymid), (col_x[c + 1] - 0.15, ymid))
            else:
                arrow((col_x[3 - c] - 0.15, ymid), (col_x[2 - c] + W + 0.15, ymid))
    arrow((col_x[3] + W / 2, row_top[0] - row_h[0] - 0.1), (col_x[3] + W / 2, row_top[1] + 0.1))
    arrow((col_x[0] + W / 2, row_top[1] - row_h[1] - 0.1), (col_x[0] + W / 2, row_top[2] + 0.1))

    # key, in the empty fourth slot of row 3
    lx = col_x[3] + 1.0
    ax.text(lx, row_top[2] - PAD, "What a step does", fontsize=7.6, fontweight="bold", color=INK, va="top")
    for i, (k, lab) in enumerate((("rewrite", "Rewrites a price"), ("delete", "Deletes or flags rows"),
                                  ("input", "Input, or builds the panel"))):
        yy = row_top[2] - PAD - 4.6 - i * 3.5
        ax.add_patch(Rectangle((lx, yy - 1.3), 1.1, 2.7, fc=stripe[k], ec="none"))
        ax.text(lx + 2.4, yy, lab, fontsize=6.9, color=INK_2, va="center")
    ax.text(lx, row_top[2] - row_h[2] + 1.0, "Italic lines: what the step could\nremove or rewrite by mistake.",
            fontsize=6.7, color=MUTED, va="bottom", linespacing=1.2)
    return finish(fig, "ch09b_stage0_pipeline")


# ---------------------------------------------------------------------------------------------------------------
# 9-B.2  One bond, one month-end, two prices (illustrative prints)
# ---------------------------------------------------------------------------------------------------------------
def fig_two_prices():
    days = ["16", "17", "18", "21", "22", "23", "24", "25", "28", "29", "30", "1", "2", "5", "6", "7", "8"]
    # daily VWAPs of an illustrative, sparsely traded bond (Sep 16 to Oct 8): index -> VWAP.  Sep 30 is the last
    # business day of September; Oct 1 the first of October.  Days not listed have no print.
    vwap = {0: 91.15, 1: 91.05, 3: 90.95, 5: 91.10, 6: 91.00, 8: 90.70, 10: 90.20, 11: 91.00, 12: 91.10,
            14: 91.20, 16: 91.30}
    offsets = {2: [-0.06, 0.06], 3: [-0.09, 0.02, 0.07], 4: [-0.10, -0.03, 0.04, 0.09]}
    i_sig, i_end, i_bgn = 5, 10, 11
    p_sig, p_end, p_bgn = vwap[i_sig], vwap[i_end], vwap[i_bgn]
    gap = p_bgn / p_end - 1
    assert 0.0085 < gap < 0.0092, gap

    fig, ax = new_figure("wide")
    ax.set_xlim(-0.6, 16.6)
    ax.set_ylim(89.72, 91.78)
    ax.axvspan(5.5, 10.5, color=BLUE, alpha=0.09, lw=0, zorder=0)
    ax.axvspan(10.5, 15.5, color=ORANGE, alpha=0.09, lw=0, zorder=0)
    ax.text(8.0, 91.74, "Last 5 NYSE business days of September:\nthe month-end price window", ha="center",
            va="top", fontsize=7.8, color=INK_2, linespacing=1.15)
    ax.text(13.0, 91.74, "First 5 business days of October:\nthe month-begin window", ha="center", va="top",
            fontsize=7.8, color=INK_2, linespacing=1.15)

    xs = sorted(vwap)
    ax.plot(xs, [vwap[i] for i in xs], color=NEUTRAL, lw=1.0, zorder=2)
    n_prints = {0: 3, 1: 2, 3: 3, 5: 3, 6: 2, 8: 3, 10: 1, 11: 2, 12: 3, 14: 2, 16: 3}
    for i in xs:
        n = n_prints[i]
        offs = [0.0] if n == 1 else offsets[n]
        xx = np.linspace(-0.2, 0.2, n) + i if n > 1 else [i]
        ax.plot(xx, [vwap[i] + o for o in offs], "o", color=NEUTRAL, ms=3.2, zorder=3, mew=0)
    ax.plot(xs, [vwap[i] for i in xs], "o", color=MUTED, ms=5.5, zorder=4, mew=0, label="Daily VWAP")
    # the three prices
    ax.plot([i_sig], [p_sig], "D", color=BLUE, ms=8, zorder=6, mew=1.0, mec=SURFACE)
    ax.plot([i_end], [p_end], "s", color=INK_2, ms=8, zorder=6, mew=1.0, mec=SURFACE)
    ax.plot([i_bgn], [p_bgn], "o", color=ORANGE, ms=8.5, zorder=6, mew=1.0, mec=SURFACE)
    # the gap wedge
    ax.add_patch(Rectangle((i_end, p_end), i_bgn - i_end, p_bgn - p_end, fc=ORANGE, ec="none", alpha=0.35,
                           zorder=1))
    ax.plot([i_end - 0.4, i_bgn + 0.4], [p_end, p_end], color=INK_2, lw=0.8, ls=(0, (3, 3)), zorder=2)
    ax.plot([i_end - 0.4, i_bgn + 0.4], [p_bgn, p_bgn], color=ORANGE, lw=0.8, ls=(0, (3, 3)), zorder=2)

    arrow_kw = dict(arrowstyle="-", color=INK_2, lw=0.7, shrinkA=0, shrinkB=4)
    ax.annotate("Signal price in the gap version:\nread 5 business days before month-end",
                (i_sig, p_sig), xytext=(0.2, 91.50), fontsize=7.8, color=INK, va="center",
                arrowprops=arrow_kw, linespacing=1.15)
    ax.annotate("Month-end price: the last daily VWAP in the window.\nIn the unadjusted version it sets the "
                "signal\nand starts the return, so its noise is both.",
                (i_end, p_end), xytext=(9.65, 89.89), fontsize=7.8, color=INK, va="center", ha="right",
                arrowprops=dict(arrow_kw, shrinkB=5), linespacing=1.15)
    ax.annotate("Month-begin price: the first print of the new month\n(a median of 1 business day later)",
                (i_bgn, p_bgn), xytext=(11.35, 90.37), fontsize=7.8, color=INK, va="center",
                arrowprops=dict(arrow_kw, shrinkB=5), linespacing=1.15)
    ax.text(10.5, 90.62, "gap\n" + f"+{gap * 100:.2f}%", ha="center", va="center", fontsize=7.8,
            fontweight="bold", color=INK, linespacing=1.1, zorder=7)

    ax.set_xticks(range(len(days)))
    ax.set_xticklabels(days)
    ax.text(0.0, -0.17, "Sep", transform=ax.get_xaxis_transform(), fontsize=8, color=MUTED, ha="center")
    ax.text(11.0, -0.17, "Oct", transform=ax.get_xaxis_transform(), fontsize=8, color=MUTED, ha="center")
    ax.set_xlabel("NYSE business day", labelpad=11)
    ax.set_ylabel("Price (% of par)")
    note(ax, "Illustrative prints; small dots are individual trades", "lower left")
    return finish(fig, "ch09b_two_prices")


# ---------------------------------------------------------------------------------------------------------------
# 9-B.3  Table 1 of Dickerson, Robotti and Rossetti (2026): three versions of seven factors
# ---------------------------------------------------------------------------------------------------------------
# (label, [(mu, t_mu) unadjusted, signal gap, return gap]); Panel A, value-weighted deciles, T = 268.
TABLE1_PANEL_A = [
    ("Yield to\nmaturity (ytm)",        [(1.20, 2.97), (1.05, 2.63), (0.92, 2.64)]),
    ("Credit\nspread (cs)",             [(1.13, 2.89), (0.96, 2.52), (0.82, 2.45)]),
    ("Book-to-\nmarket (bbtm)",         [(0.93, 2.19), (0.75, 1.80), (0.66, 1.80)]),
    ("6-month spread\nchange (dcs6)",   [(-1.02, -4.58), (-0.50, -2.52), (-0.46, -2.50)]),
    ("Residual spread\nvalue (val_ipr)", [(0.96, 4.82), (0.51, 2.68), (0.51, 3.05)]),
    ("HvZ value\n(val_hz)",             [(0.81, 3.80), (0.45, 2.29), (0.43, 2.32)]),
    ("Short-term\nreversal (str)",      [(-0.99, -4.46), (-0.09, -0.51), (-0.17, -0.98)]),
]


def fig_lib_waterfall():
    # the chapter's statements about the table
    byname = {lab.split("(")[-1].rstrip(")"): v for lab, v in TABLE1_PANEL_A}
    assert byname["str"][0][0] == -0.99 and byname["str"][1][0] == -0.09
    assert byname["ytm"][0][0] == 1.20 and byname["ytm"][2][0] == 0.92
    assert byname["val_ipr"][0][0] == 0.96 and byname["val_ipr"][1][0] == 0.51

    fig, ax = new_figure("wide")
    cols = [MUTED, BLUE, ORANGE]
    names = ["Unadjusted: signal and return share the month-end price", "Signal gap: signal read 1 to 10 days earlier",
             "Return gap: return starts at the month-begin price"]
    bw = 0.26
    for j, (col, nm) in enumerate(zip(cols, names)):
        xs = np.arange(len(TABLE1_PANEL_A)) + (j - 1) * (bw + 0.03)
        vals = [v[j][0] for _, v in TABLE1_PANEL_A]
        ax.bar(xs, vals, width=bw, color=col, ec=SURFACE, lw=0.8, label=nm, zorder=3)
        for x, (_, v) in zip(xs, TABLE1_PANEL_A):
            mu, t = v[j]
            off = 3 if mu >= 0 else -3
            ax.annotate(sgn(t), (x, mu), xytext=(0, off), textcoords="offset points", ha="center",
                        va="bottom" if mu >= 0 else "top", fontsize=6.4, color=INK_2)
    ax.axhline(0, color=INK_2, lw=0.8, zorder=4)
    ax.set_xticks(range(len(TABLE1_PANEL_A)))
    ax.set_xticklabels([lab for lab, _ in TABLE1_PANEL_A], fontsize=7.4)
    ax.tick_params(axis="x", length=0)
    ax.set_ylabel("Premium (% a month)")
    ax.set_ylim(-1.45, 1.85)
    ax.set_xlim(-0.55, 6.55)
    leg = ax.legend(loc="upper right", fontsize=7.4, handlelength=1.2, handleheight=0.9, borderaxespad=0.2,
                    labelspacing=0.35)
    # the chapter's remark on the one survivor, placed where there is room (below the zero line, centre)
    ax.annotate("val_ipr CAPM-B alpha: 0.76% falls to 0.31%\n(t 2.12) and 0.33% (t 2.61), still significant",
                (4.0, -0.04), xytext=(4.0, -0.62), ha="center", va="center", fontsize=7.4, color=INK,
                linespacing=1.15, arrowprops=dict(arrowstyle="-", color=INK_2, lw=0.7, shrinkA=0, shrinkB=1))
    note(ax, "Numbers beside the bars are the premium's t-statistic (Newey-West)", "lower left")
    return finish(fig, "ch09b_lib_waterfall")


# ---------------------------------------------------------------------------------------------------------------
# 9-B.4  Six-month momentum alpha against the trimming threshold
# ---------------------------------------------------------------------------------------------------------------
def load_fig6():
    path = os.path.join(HERE, "data", "ch09b_drr_fig6_mom6_alpha.csv")
    rows = []
    with open(path, newline="") as f:
        lines = [ln for ln in f if not ln.startswith("#")]
    for r in csv.DictReader(lines):
        rows.append(dict(panel=r["panel"], timing=r["timing"], tail=r["tail"], tau=int(r["threshold_pct"]),
                         a=float(r["alpha_pct_monthly"]), lo=float(r["ci95_lo"]), hi=float(r["ci95_hi"])))
    return rows


def fig_mom6_trimming():
    rows = load_fig6()

    def series(panel):
        s = sorted((r for r in rows if r["panel"] == panel), key=lambda r: r["tau"])
        return (np.array([r["tau"] for r in s]), np.array([r["a"] for r in s]),
                np.array([r["lo"] for r in s]), np.array([r["hi"] for r in s]))

    tA, aA, loA, hiA = series("A")   # ex ante, left tail
    tB, aB, loB, hiB = series("B")   # ex post, left tail
    tC, aC, loC, hiC = series("C")   # ex ante, right tail
    tD, aD, loD, hiD = series("D")   # ex post, right tail
    # the chapter's claims, asserted against the paper's own figure
    assert (loA < 0).all() and (loC < 0).all() and (hiA > 0).all() and (hiC > 0).all()   # ex ante: interval spans 0
    assert abs(aD[0] - 0.60) < 0.03 and loD[0] > 0                                       # right tail at 10%: about 0.60
    assert aB[0] < 0 and aB[2] < 0 and abs(aB[3]) < 0.03 and aB[4] > 0                  # crosses zero at about -40%
    assert (np.diff(aD) < 0).all() and (np.diff(aB) > 0).all()                          # monotone, as the paper says

    fig, ax = new_figure("wide")
    # ex-ante 95% interval (the union of the two ex-ante panels)
    ax.fill_between(tA, np.minimum(loA, loC), np.maximum(hiA, hiC), color=GRID, lw=0, zorder=0)
    ax.axhline(0, color=INK_2, lw=0.8, zorder=1)
    ax.plot(tA, aA, color=BLUE, lw=LW, ls=(0, (4, 2)), marker="o", mfc=SURFACE, mec=BLUE, mew=1.3, ms=5,
            zorder=3)
    ax.plot(tC, aC, color=ORANGE, lw=LW, ls=(0, (4, 2)), marker="o", mfc=SURFACE, mec=ORANGE, mew=1.3, ms=5,
            zorder=3)
    ax.plot(tB, aB, color=BLUE, lw=LW, marker="o", ms=5, zorder=4)
    ax.plot(tD, aD, color=ORANGE, lw=LW, marker="o", ms=5, zorder=4)

    ax.annotate("Ex post, right tail trimmed:\nthe alpha reaches 0.62% at a 10% cut-off",
                (tD[0], aD[0]), xytext=(17, 0.66), fontsize=7.8, color=INK, va="center", linespacing=1.15,
                arrowprops=dict(arrowstyle="-", color=INK_2, lw=0.7, shrinkA=0, shrinkB=3))
    ax.annotate("Ex post, left tail trimmed:\nnegative, and back to zero only\nnear a " + MINUS + "40% cut-off",
                (tB[0], aB[0]), xytext=(16, -0.50), fontsize=7.8, color=INK, va="center", linespacing=1.15,
                arrowprops=dict(arrowstyle="-", color=INK_2, lw=0.7, shrinkA=0, shrinkB=3))
    ax.text(88.5, 0.27, "Ex ante, either tail: about 0.15%,\nand the 95% interval (shaded) spans zero",
            fontsize=7.8, color=INK, ha="right", va="center", linespacing=1.15)
    ax.set_xlim(7, 93)
    ax.set_ylim(-0.82, 1.22)
    ax.set_xticks(tA)
    ax.set_xticklabels([f"{int(t)}%" for t in tA])
    ax.set_xlabel("Trim threshold: monthly returns below " + MINUS + "x% (left tail) or above +x% (right tail) excluded")
    ax.set_ylabel("CAPM-B alpha (% a month)")
    # key: colour = tail, line style = timing
    from matplotlib.lines import Line2D
    h = [Line2D([0], [0], color=BLUE, lw=LW, marker="o", ms=5, label="Left tail"),
         Line2D([0], [0], color=ORANGE, lw=LW, marker="o", ms=5, label="Right tail"),
         Line2D([0], [0], color=INK_2, lw=LW, label="Ex post (look-ahead)"),
         Line2D([0], [0], color=INK_2, lw=LW, ls=(0, (4, 2)), marker="o", mfc=SURFACE, mec=INK_2, mew=1.3, ms=5,
                label="Ex ante (feasible)")]
    ax.legend(handles=h, loc="upper right", ncol=2, fontsize=7.6, columnspacing=1.2, handlelength=2.0,
              borderaxespad=0.2)
    return finish(fig, "ch09b_mom6_trimming")


# ---------------------------------------------------------------------------------------------------------------
# 9-B.5  The two-leg bounce artifact (illustrative)
# ---------------------------------------------------------------------------------------------------------------
def fig_two_leg_bounce():
    """Model: 30 trading days; two legs share a market factor (sd 0.45 point a day) plus idiosyncratic noise (sd 0.12
    point); long leg starts at 94, short leg at 84; $10mm of market value on each leg.  On day 14 a small lot prints
    3.0 points low on the long leg and 3.0 points high on the short leg, and both snap back on day 15.  Raw series use
    every print; the filtered series drops the two bounce prints and carries the previous clean price."""
    rng = np.random.default_rng(93)
    n, d_b = 30, 14
    mkt = rng.normal(0, 0.45, n)
    mkt[0] = 0
    long_true = 94 + np.cumsum(mkt + rng.normal(0, 0.12, n) * (np.arange(n) > 0))
    short_true = 84 + np.cumsum(mkt + rng.normal(0, 0.12, n) * (np.arange(n) > 0))
    long_raw, short_raw = long_true.copy(), short_true.copy()
    long_raw[d_b] -= 3.0
    short_raw[d_b] += 3.0
    long_flt, short_flt = long_true.copy(), short_true.copy()
    long_flt[d_b], short_flt[d_b] = long_flt[d_b - 1], short_flt[d_b - 1]       # bounce dropped, price carried
    N = 10_000.0                                                                  # $ thousand of market value per leg

    def pnl(lg, sh):
        return N * (np.diff(lg) / lg[:-1]) - N * (np.diff(sh) / sh[:-1])

    p_raw, p_flt = pnl(long_raw, short_raw), pnl(long_flt, short_flt)
    days = np.arange(1, n)
    # the chapter's claim: a sharp loss, then a full reversal; the filtered pair shows neither
    assert p_raw[d_b - 1] < -600 and p_raw[d_b] > 600 and abs(p_raw[d_b - 1] + p_raw[d_b]) < 120
    assert np.abs(p_flt).max() < 250

    fig, (axl, axr) = new_figure("wide", ncols=2)
    x = np.arange(n)
    for raw, flt, lab, dy in ((long_raw, long_flt, "Long leg", 0), (short_raw, short_flt, "Short leg", 0)):
        axl.plot(x, raw, color=MUTED, lw=LW, zorder=2)
        axl.plot(x, flt, color=INK, lw=1.0, zorder=3)
        axl.plot([d_b], [raw[d_b]], "o", color=MUTED, ms=6, zorder=4, mfc=SURFACE, mew=1.5)
    axl.text(n - 0.4, long_true[-1] + 1.0, "Long leg", fontsize=8.2, color=INK_2, ha="right", va="bottom")
    axl.text(n - 0.4, short_true[-1] - 1.3, "Short leg", fontsize=8.2, color=INK_2, ha="right", va="top")
    axl.annotate("Low print", (d_b, long_raw[d_b]), xytext=(d_b + 1.2, long_raw[d_b] - 2.2), fontsize=7.8,
                 color=INK, va="center", arrowprops=dict(arrowstyle="-", color=INK_2, lw=0.7, shrinkA=0, shrinkB=3))
    axl.annotate("High print", (d_b, short_raw[d_b]), xytext=(d_b + 1.2, short_raw[d_b] + 2.4), fontsize=7.8,
                 color=INK, va="center", arrowprops=dict(arrowstyle="-", color=INK_2, lw=0.7, shrinkA=0, shrinkB=3))
    axl.set_xlabel("Trading day")
    axl.set_ylabel("Price (% of par)")
    axl.set_xlim(0, n - 0.5)
    axl.set_ylim(min(long_raw.min(), short_raw.min()) - 6, max(long_true.max(), short_raw.max()) + 4)
    axl.plot([], [], color=MUTED, lw=LW, label="Raw prints")
    axl.plot([], [], color=INK, lw=1.0, label="Bounce-filtered")
    axl.legend(loc="upper left", fontsize=7.6, handlelength=1.6, borderaxespad=0.2, ncol=1)

    axr.axhline(0, color=INK_2, lw=0.8, zorder=1)
    axr.plot(days, p_raw, color=MUTED, lw=LW, marker="o", ms=3.5, zorder=3)
    axr.plot(days, p_flt, color=INK, lw=1.0, marker="o", ms=2.5, zorder=4)
    axr.annotate(f"{MINUS}${abs(p_raw[d_b - 1]) / 1000:.2f}mm", (days[d_b - 1], p_raw[d_b - 1]),
                 xytext=(-5, -2), textcoords="offset points", ha="right", va="center", fontsize=7.8, color=INK)
    axr.annotate(f"+${p_raw[d_b] / 1000:.2f}mm", (days[d_b], p_raw[d_b]), xytext=(5, 0), textcoords="offset points",
                 ha="left", va="center", fontsize=7.8, color=INK)
    axr.set_xlabel("Trading day")
    axr.set_ylabel("Pair P&L ($ thousand a day)")
    axr.set_xlim(0.5, n - 0.5)
    axr.set_ylim(-880, 880)
    note(axr, "Illustrative; $10mm on each leg", "lower right")
    return finish(fig, "ch09b_two_leg_bounce")


if __name__ == "__main__":
    fig_stage0_pipeline()
    fig_two_prices()
    fig_lib_waterfall()
    fig_mom6_trimming()
    fig_two_leg_bounce()
