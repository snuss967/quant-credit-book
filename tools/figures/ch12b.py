"""Figures for Chapter 12-B (The Restructuring Process as a State Machine).

Run:  python3 tools/figures/ch12b.py   -> assets/figures/ch12b_*.png

Colour use in this chapter: BLUE is the senior class or the instrument the figure is about (the first lien in the
Halvorsen figure), ORANGE is the junior class or the comparison case; in the state-machine figure the node border
carries the kind of state (grey economic, orange contract clock, blue out-of-court LMT, violet agreement or court).
Every colour that has low contrast on white (aqua, yellow, magenta) is direct-labelled.
"""
import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from style import *  # noqa: E402,F401,F403  (applies the rcParams on import)

import numpy as np  # noqa: E402
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Polygon, Rectangle  # noqa: E402
from scipy.stats import norm  # noqa: E402

TINT = "#f5f5f3"      # very light surface for grouping regions (not a data colour)


# --------------------------------------------------------------------------------------------------
# Figure 12-B.1: the out-of-court menu as a state machine (section 12B.4)
# --------------------------------------------------------------------------------------------------
class Node:
    def __init__(self, cx, cy, w, h):
        self.cx, self.cy, self.w, self.h = cx, cy, w, h

    def L(self, dy=0): return (self.cx - self.w / 2, self.cy + dy)
    def R(self, dy=0): return (self.cx + self.w / 2, self.cy + dy)
    def T(self, dx=0): return (self.cx + dx, self.cy + self.h / 2)
    def B(self, dx=0): return (self.cx + dx, self.cy - self.h / 2)


def draw_node(ax, cx, cy, w, h, title, sub=None, ec=NEUTRAL, fc=SURFACE):
    ax.add_patch(FancyBboxPatch((cx - w / 2, cy - h / 2), w, h, boxstyle="round,pad=0,rounding_size=1.4",
                                fc=fc, ec=ec, linewidth=1.7, zorder=3))
    if sub:
        ax.text(cx, cy + 1.35, title, ha="center", va="center", fontsize=9, fontweight="bold", color=INK, zorder=4)
        ax.text(cx, cy - 2.0, sub, ha="center", va="center", fontsize=7.4, color=INK_2, zorder=4)
    else:
        ax.text(cx, cy, title, ha="center", va="center", fontsize=9, fontweight="bold", color=INK, zorder=4)
    return Node(cx, cy, w, h)


def draw_arrow(ax, p0, p1, rad=0.0, color=INK_2, lw=1.2, ls="-"):
    ax.add_patch(FancyArrowPatch(p0, p1, arrowstyle="-|>", mutation_scale=9, connectionstyle=f"arc3,rad={rad}",
                                 color=color, linewidth=lw, linestyle=ls, shrinkA=0, shrinkB=0, zorder=2))


def edge_label(ax, x, y, text, ha="center", va="center", bg=SURFACE, **kw):
    ax.text(x, y, text, ha=ha, va=va, fontsize=7.6, color=INK_2, linespacing=1.18, zorder=5,
            bbox=dict(fc=bg, ec="none", pad=0.9), **kw)


def fig_out_of_court_machine():
    W, H = 100.0, 82.0
    fig, ax = new_figure((7.0, 7.0 * H / W))
    ax.set_xlim(0, W); ax.set_ylim(0, H)
    ax.set_aspect("equal"); ax.axis("off"); ax.grid(False)

    # region: any distressed state
    ax.add_patch(FancyBboxPatch((3, 26), 94, 41, boxstyle="round,pad=0,rounding_size=2", fc=TINT, ec="none", zorder=1))
    ax.text(5, 28.4, "Any distressed state", fontsize=7.6, color=MUTED, ha="left", va="center", zorder=2)

    perf = draw_node(ax, 22, 75, 19, 8, "Performing", "runway above ~12 months", ec=NEUTRAL)
    stre = draw_node(ax, 22, 58, 19, 8, "Stressed", "runway below ~12 months", ec=NEUTRAL, fc=TINT)
    grace = draw_node(ax, 51, 58, 17, 8, "Grace", "invariant c \u2264 30 days", ec=ORANGE, fc=TINT)
    eod = draw_node(ax, 78, 58, 19, 8, "Event of default", "cross-default fans out", ec=ORANGE, fc=TINT)
    forb = draw_node(ax, 78, 41, 19, 8, "Forbearance", "clock of weeks", ec=ORANGE, fc=TINT)
    lmt = draw_node(ax, 22, 37, 27, 11, "Post-LMT", "A&E, exchange, uptier,\ndrop-down, double-dip", ec=BLUE, fc=TINT)

    rsa = draw_node(ax, 24, 11, 19, 8, "RSA signed", "milestone clocks", ec=VIOLET)
    pet = draw_node(ax, 62, 11, 19, 8, "Petition", "automatic stay begins", ec=VIOLET)
    ch11 = draw_node(ax, 89, 11, 17, 8, "Chapter 11", "Figure 12-B.2", ec=VIOLET)

    # spine
    draw_arrow(ax, perf.B(), stre.T())
    edge_label(ax, 24.0, 69.2, "liquidity runway falls", ha="left", bg=SURFACE)
    # missed interest, grace expiry
    draw_arrow(ax, stre.R(), grace.L())
    edge_label(ax, 37.0, 64.3, "missed\ninterest", bg=TINT)
    draw_arrow(ax, grace.R(), eod.L())
    edge_label(ax, 64.5, 64.3, "grace expires,\nforced", bg=TINT)
    # forbearance from EoD and from Grace
    draw_arrow(ax, eod.B(), forb.T())
    edge_label(ax, 80.0, 49.5, "forbearance: Required\nLenders (loans) or\nmajority (bonds)", ha="left", bg=TINT)
    draw_arrow(ax, grace.B(dx=4), forb.L(dy=2), lw=1.0, ls=(0, (4, 3)))
    # LMT edges and the re-default edge
    draw_arrow(ax, stre.B(dx=-4), lmt.T(dx=-4))
    edge_label(ax, 16.0, 48.2, "five LMT edges;\nguard: s \u2265 \u03b8$_{\\mathrm{eff}}$;\ntender \u2265 90%", ha="right", bg=TINT)
    draw_arrow(ax, lmt.T(dx=6), stre.B(dx=6), color=BLUE, lw=1.5)
    edge_label(ax, 30.0, 48.2, "re-default:\nparole, not\nimmunity", ha="left", bg=TINT)
    ax.text(42, 35.5, "Clocks: grace 30 days;\nexchange offer open at least\n20 business days (Rule 14e-1)",
            fontsize=7.4, color=MUTED, ha="left", va="center", linespacing=1.18, zorder=2)

    # from the region to RSA and to the petition
    draw_arrow(ax, (24, 26), rsa.T(), color=VIOLET, lw=1.4)
    edge_label(ax, 26.0, 21.0, "RSA: \u2265 \u2154 in amount and > \u00bd in number\nof each class the plan impairs", ha="left")
    draw_arrow(ax, (62, 26), pet.T(), color=VIOLET, lw=1.4)
    edge_label(ax, 64.0, 21.0, "free-fall filing:\nboard resolution", ha="left")
    draw_arrow(ax, rsa.R(), pet.L(), color=VIOLET, lw=1.4)
    edge_label(ax, 43.0, 15.6, "prepack: votes solicited\nbefore the petition", bg=SURFACE)
    draw_arrow(ax, pet.R(), ch11.L(), color=VIOLET, lw=1.4)

    # legend of border colours
    ly = 1.2
    items = [(NEUTRAL, "economic state"), (ORANGE, "contract clock"), (BLUE, "out-of-court LMT"), (VIOLET, "agreement or court")]
    xs = [3.0, 22.0, 40.0, 61.0]
    for (c, t), x in zip(items, xs):
        ax.add_patch(Rectangle((x, ly - 0.9), 2.6, 1.8, fc=SURFACE, ec=c, linewidth=1.7, zorder=3))
        ax.text(x + 3.6, ly, t, fontsize=7.4, color=INK_2, va="center", ha="left")
    return finish(fig, "ch12b_out_of_court_machine")


# --------------------------------------------------------------------------------------------------
# Figure 12-B.2: the Chapter 11 clocks on one day axis (section 12B.5)
# --------------------------------------------------------------------------------------------------
def fig_chapter11_clocks():
    # (label, group colour, [(start, end, kind)], end label, marker)
    BL, OR, VI = BLUE, ORANGE, VIOLET
    rows = [
        ("Automatic stay (§362)",                       BL, [(0, 640, "solid")], "until relief or case end", "arrow"),
        ("Interim-relief window (Rule 6003)",               BL, [(0, 21, "solid")], "21 d", None),
        ("Schedules due (Rule 1007(c))",                    BL, [(0, 14, "solid")], "14 d, usually extended", None),
        ("Final DIP hearing notice (Rule 4001(c)(2))",      BL, [(0, 14, "solid")], "at least 14 d", None),
        ("§341 meeting (Rule 2003(a))",                 BL, [(21, 40, "solid")], "day 21–40", None),
        ("Lien-challenge period (DIP order)",               OR, [(0, 60, "mid"), (60, 75, "solid")], "60–75 d", None),
        ("Exclusivity to file (§1121(b), (d)(2))",      OR, [(0, 120, "solid"), (120, 548, "light")], "120 d; cap 18 mo", None),
        ("Exclusivity to solicit (§1121(c)(3), (d)(2))", OR, [(0, 180, "solid"), (180, 608, "light")], "180 d; cap 20 mo", None),
        ("Real-property leases (§365(d)(4))",           VI, [(0, 120, "solid"), (120, 210, "mid")], "120 + 90 d", None),
        ("Governmental bar date (§502(b)(9))",          VI, [(0, 180, "solid")], "180 d", None),
        ("Avoidance actions (§546(a))",                 VI, [(0, 640, "solid")], "2 years (730 d)", "arrow"),
        ("Preference look-back (§547(b)(4))",           VI, [(-365, -90, "light"), (-90, 0, "solid")], "90 d; insiders 1 year", None),
        ("503(b)(9) goods look-back (§503(b)(9))",      VI, [(-20, 0, "solid")], "20 d", None),
    ]
    n = len(rows)
    fig, ax = new_figure((7.0, 5.0))
    ax.grid(False)
    ax.grid(axis="x", color=GRID, linewidth=0.7)
    ax.set_axisbelow(True)
    xmin, xmax = -140, 650
    bar_h = 0.58
    alpha = {"solid": 1.0, "mid": 0.55, "light": 0.28}
    for i, (label, col, segs, endlab, mk) in enumerate(rows):
        y = n - 1 - i
        for (a, b, kind) in segs:
            a_c = max(a, xmin); b_c = min(b, xmax - 8)
            ax.barh(y, b_c - a_c, left=a_c, height=bar_h, color=col, alpha=alpha[kind], linewidth=0, zorder=3)
        a_last, b_last = segs[-1][0], segs[-1][1]
        start_first = segs[0][0]
        if mk == "arrow":
            ax.annotate("", xy=(xmax - 1, y), xytext=(xmax - 30, y),
                        arrowprops=dict(arrowstyle="-|>", color=col, lw=1.4, shrinkA=0, shrinkB=0), zorder=4)
            ax.text(xmax - 36, y, endlab, ha="right", va="center", fontsize=7.6, color=INK, zorder=5,
                    bbox=dict(fc=SURFACE, ec="none", pad=0.8, alpha=0.9))
        else:
            ax.text(min(b_last, xmax) + 7, y, endlab, ha="left", va="center", fontsize=7.6, color=INK_2, zorder=5)
    # the petition date and the stated caps
    ax.axvline(0, color=INK_2, linewidth=1.0, zorder=4)
    ax.annotate("petition (order for relief)", (0, n - 0.45), xytext=(6, 0), textcoords="offset points",
                fontsize=7.8, color=INK_2, va="bottom", ha="left", annotation_clip=False)
    ax.set_yticks(range(n))
    ax.set_yticklabels([r[0] for r in rows][::-1], fontsize=8)
    ax.tick_params(axis="y", length=0)
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(-0.7, n - 0.2)
    ax.set_xticks([-100, 0, 100, 200, 300, 400, 500, 600])
    ax.set_xlabel("Days from the petition (negative = look-back before it)")
    # key for the three bar weights
    kx = 292
    ky = -0.15
    ax.text(kx, 4.35, "Bar weight", fontsize=7.6, color=INK_2, ha="left", va="center", zorder=6)
    for j, (kind, txt) in enumerate([("solid", "fixed period"), ("mid", "extension or range"), ("light", "court may extend to the cap")]):
        yy = 3.6 - 0.75 * j
        ax.add_patch(Rectangle((kx, yy - 0.2), 28, 0.4, fc=BLUE, alpha=alpha[kind], ec="none", zorder=6))
        ax.text(kx + 36, yy, txt, fontsize=7.6, color=INK_2, ha="left", va="center", zorder=6)
    return finish(fig, "ch12b_chapter11_clocks")


# --------------------------------------------------------------------------------------------------
# Figure 12-B.3: the waterfall as call spreads, and the fulcrum's expected delta (section 12B.6)
# --------------------------------------------------------------------------------------------------
def fig_waterfall_call_spreads():
    C = np.array([100.0, 300.0, 400.0, 200.0])
    K = np.concatenate([[0.0], np.cumsum(C)])               # 0, 100, 400, 800, 1000
    names = ["Class 1", "Class 2", "Class 3", "Class 4"]
    cols = [SERIES[0], SERIES[1], SERIES[2], SERIES[3]]

    fig, axes = new_figure("wide", ncols=2)
    ax, bx = axes

    # left: dollars paid to each class as V rises (each band is a call spread)
    V = np.linspace(0, 1250, 600)
    for j in range(4):
        lo = np.minimum(V, K[j]); hi = np.minimum(V, K[j + 1])
        ax.fill_between(V, lo, hi, color=cols[j], linewidth=0, zorder=2)
        # thin white gap between bands
        ax.plot(V, hi, color=SURFACE, linewidth=0.8, zorder=3)
    ax.fill_between(V, np.minimum(V, K[4]), V, color=NEUTRAL, alpha=0.55, linewidth=0, zorder=2)
    ax.plot(V, V, color=SURFACE, linewidth=0.8, zorder=3)
    ax.set_xlim(0, 1250); ax.set_ylim(0, 1250)
    ax.set_aspect("equal", adjustable="box")
    ax.grid(False)
    ax.set_xticks([0, 400, 800, 1200]); ax.set_yticks([0, 400, 800, 1200])
    ax.set_xlabel("Distributable value V ($mm)")
    ax.set_ylabel("Value paid, cumulative ($mm)")
    # band labels on the flat part, right side
    for j in range(4):
        mid = 0.5 * (K[j] + K[j + 1])
        ax.text(1235, mid, f"{names[j]}, {C[j]:.0f}", ha="right", va="center", fontsize=7.6, color=INK, zorder=5)
    ax.text(1235, 1125, "Old equity", ha="right", va="center", fontsize=7.6, color=INK, zorder=5)
    # the example value and its fulcrum
    v0 = 450
    ax.axvline(v0, color=INK_2, linewidth=0.9, linestyle=(0, (3, 3)), zorder=4)
    ax.annotate("V = 450: only Class 3\nis still filling", (v0, 1020), xytext=(v0 + 25, 1020), fontsize=7.6,
                color=INK_2, va="center", ha="left", zorder=5)

    # right: expected delta = pi_j / C_j under a lognormal V
    med, sig = 450.0, 0.40
    cdf = norm.cdf(np.log(K[1:] / med) / sig)
    cdf = np.concatenate([[0.0], cdf])
    pi = np.diff(cdf)                                   # P(K_{j-1} <= V < K_j)
    delta = pi / C * 1e4                                # points of recovery per +$100mm of V
    x = np.arange(4)
    bx.bar(x, delta, width=0.62, color=cols, zorder=3)
    for xi, d, p in zip(x, delta, pi):
        bx.text(xi, d + 0.5, f"{d:.1f}", ha="center", va="bottom", fontsize=8.2, color=INK, zorder=5)
        bx.text(xi, -0.4, f"π = {p:.2f}", ha="center", va="top", fontsize=7.6, color=INK_2, zorder=5, clip_on=False)
    bx.set_xticks(x); bx.set_xticklabels(names)
    bx.tick_params(axis="x", length=0, pad=14)
    bx.set_ylim(0, 19)
    bx.set_ylabel("Expected change in recovery\n(points per +$100mm of V)")
    note(bx, "π = P(class is the fulcrum)", loc="upper right")
    return finish(fig, "ch12b_waterfall_call_spreads")


# --------------------------------------------------------------------------------------------------
# Figure 12-B.4: the plan value is a price (section 12B.6)
# --------------------------------------------------------------------------------------------------
def fig_plan_value_transfer():
    C1, C2, V = 800.0, 600.0, 1000.0
    vp = np.linspace(C1, C1 + C2, 400)
    R1 = V / vp * 100
    R2 = (vp - C1) * V / (C2 * vp) * 100

    fig, ax = new_figure("wide")
    ax.plot(vp, R1, color=BLUE, linewidth=LW, zorder=3)
    ax.plot(vp, R2, color=ORANGE, linewidth=LW, zorder=3)
    ax.axhline(100, color=NEUTRAL, linewidth=0.9, zorder=1)
    mark_event(ax, V, "plan value = true value", y_frac=0.97)
    ax.plot([V], [100], "o", color=BLUE, markersize=6, zorder=5)
    r2_at = (V - C1) * V / (C2 * V) * 100
    ax.plot([V], [r2_at], "o", color=ORANGE, markersize=6, zorder=5)
    # direct labels
    label_end(ax, vp[-1], R1[-1], "", BLUE, dx=0)
    label_end(ax, vp[-1], R2[-1], "", ORANGE, dx=0)
    ax.annotate("Senior (claim 800)", (vp[0], R1[0]), xytext=(812, 114), fontsize=8.5, color=INK_2, va="center")
    ax.annotate("Junior (claim 600)", (1180, (1180 - C1) * V / (C2 * 1180) * 100), xytext=(1140, 21), fontsize=8.5,
                color=INK_2, va="center")
    ax.annotate("At 1,000 the senior is paid in full\nand the junior gets one third", (V, 100),
                xytext=(1035, 90), fontsize=8, color=INK_2, va="center",
                arrowprops=dict(arrowstyle="-", color=NEUTRAL, linewidth=0.8, shrinkA=2, shrinkB=4))
    ax.annotate("Every dollar of plan value above 1,000\nmoves recovery from senior to junior", (1250, 77),
                xytext=(1115, 52), fontsize=8, color=INK_2, va="center", ha="left",
                arrowprops=dict(arrowstyle="-", color=NEUTRAL, linewidth=0.8, shrinkA=2, shrinkB=4))
    ax.set_xlim(C1, C1 + C2)
    ax.set_ylim(0, 132)
    ax.set_xlabel("Plan value V$^{\\mathrm{plan}}$ in the disclosure statement ($mm)")
    ax.set_ylabel("Realised recovery (% of claim)")
    note(ax, "Senior 800, junior 600, all-equity consideration; shares truly worth V = 1,000", loc="lower left")
    return finish(fig, "ch12b_plan_value_transfer")


# --------------------------------------------------------------------------------------------------
# Figure 12-B.5: where the 1,300 of Halvorsen plan value goes (section 12B.9)
# --------------------------------------------------------------------------------------------------
def ribbon(ax, x0, x1, y0t, y0b, y1t, y1b, color, alpha=0.55):
    t = np.linspace(0, 1, 60)
    s = 3 * t ** 2 - 2 * t ** 3
    xs = x0 + (x1 - x0) * t
    top = y0t + (y1t - y0t) * s
    bot = y0b + (y1b - y0b) * s
    pts = np.concatenate([np.column_stack([xs, top]), np.column_stack([xs[::-1], bot[::-1]])])
    ax.add_patch(Polygon(pts, closed=True, fc=color, ec=SURFACE, linewidth=0.6, alpha=alpha, zorder=2))


def fig_halvorsen_waterfall():
    # sources (top to bottom) and destinations (top to bottom), $mm; flows (source, dest, amount)
    src = [("ABL collateral", 250.0), ("Term-loan collateral", 960.0), ("Unencumbered value", 90.0)]
    dst = [("ABL revolver", 150.0, GREEN, "150 of 150 = 100%"),
           ("First lien (TLB + secured notes)", 760.0, BLUE, "760 of 1,250 = 60.8%"),
           ("DIP, taken out by exit term loan", 300.0, ORANGE, "300 of 300 = 100%"),
           ("Administrative and priority", 75.0, YELLOW, "75 of 75 = 100%"),
           ("Unsecured pool", 15.0, MAGENTA, "15 of 1,020 = 1.5%")]
    flows = [(0, 0, 150.0), (0, 1, 100.0), (1, 1, 660.0), (1, 2, 300.0), (2, 3, 75.0), (2, 4, 15.0)]
    total = 1300.0
    gap = 28.0
    scale = 1.0

    fig, ax = new_figure((7.0, 4.1))
    ax.grid(False); ax.axis("off")
    x_src, x_dst, bw = 0.0, 5.0, 0.28

    # node y-positions (bars stacked top-down with gaps)
    def stack(items):
        pos, y = [], 0.0
        for it in items:
            amt = it[1]
            pos.append((y - amt, y))      # (bottom, top)
            y = y - amt - gap
        return pos
    sp = stack(src)
    dp = stack(dst)
    # centre the two stacks vertically
    s_h = sp[0][1] - sp[-1][0]; d_h = dp[0][1] - dp[-1][0]
    off_s = (max(s_h, d_h) - s_h) / 2; off_d = (max(s_h, d_h) - d_h) / 2
    sp = [(b - off_s, t - off_s) for b, t in sp]
    dp = [(b - off_d, t - off_d) for b, t in dp]

    # flows: allocate ribbon slots inside each node in the order given
    s_cursor = [t for b, t in sp]
    d_cursor = [t for b, t in dp]
    for (si, di, amt) in flows:
        y0t = s_cursor[si]; y0b = y0t - amt; s_cursor[si] = y0b
        y1t = d_cursor[di]; y1b = y1t - amt; d_cursor[di] = y1b
        ribbon(ax, x_src + bw, x_dst, y0t, y0b, y1t, y1b, dst[di][2])

    for (name, amt), (b, t) in zip(src, sp):
        ax.add_patch(Rectangle((x_src, b), bw, t - b, fc=NEUTRAL, ec="none", zorder=3))
        ax.text(x_src - 0.12, 0.5 * (b + t) + 14, name, ha="right", va="center", fontsize=8.5, color=INK, zorder=5)
        ax.text(x_src - 0.12, 0.5 * (b + t) - 24, f"{amt:,.0f}", ha="right", va="center", fontsize=8.5, color=INK_2, zorder=5)
    for (name, amt, col, rec), (b, t) in zip(dst, dp):
        ax.add_patch(Rectangle((x_dst, b), bw, t - b, fc=col, ec="none", zorder=3))
        yc = 0.5 * (b + t)
        ax.text(x_dst + bw + 0.12, yc + 17, name, ha="left", va="center", fontsize=8.5, color=INK, zorder=5)
        ax.text(x_dst + bw + 0.12, yc - 21, rec, ha="left", va="center", fontsize=8.2, color=INK_2, zorder=5)
    # note on priming
    ax.text(2.5, dp[2][0] - 6, "the DIP primes the term-loan collateral", ha="center", va="top", fontsize=7.8, color=MUTED, zorder=5)
    ax.text(x_src + bw / 2, sp[0][1] + 40, "Where the value sits", ha="center", va="bottom", fontsize=8.2, color=MUTED)
    ax.text(x_dst + bw / 2, dp[0][1] + 40, "Who is paid", ha="center", va="bottom", fontsize=8.2, color=MUTED)
    ax.set_xlim(-1.9, 8.1)
    ax.set_ylim(min(sp[-1][0], dp[-1][0]) - 60, max(sp[0][1], dp[0][1]) + 110)
    return finish(fig, "ch12b_halvorsen_waterfall")


if __name__ == "__main__":
    fig_out_of_court_machine()
    fig_chapter11_clocks()
    fig_waterfall_call_spreads()
    fig_plan_value_transfer()
    fig_halvorsen_waterfall()
