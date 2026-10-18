"""Figures for the front matter "How to Use This Book" (book_src/00_02_how_to_use_this_book.md).

Run:  python3 tools/figures/00_02_.py   -> assets/figures/00_02__*.png   (five figures)

Colour roles, fixed per figure and listed here so the five read as one set (identity is always also direct-labelled):
  Fig 1 dependency map : BLUE   = a module import (primer -> chapter);  ORANGE = the RV path of section 0.9 (thinner);
                         VIOLET = second-generation import (one chapter's module imports another's)
  Fig 2 volatility tax : BLUE   = the average path / mean;  ORANGE = the median path / median
  Fig 3 seat paths     : BLUE, ORANGE, AQUA, YELLOW = seats 1-4 in the order of the chapter's seat table
  Fig 4 ninety days    : BLUE = Tier 1 (read), ORANGE = Tier 2 (derive), AQUA = Tier 3 (build), grey = tier not stated
  Fig 5 hand history   : BLUE = Theo's hit rate and the band around it;  grey = the "perfectly calibrated" diagonal

Data. Nothing here is a market quotation. Figures 1, 3 and 4 draw the chapter's own tables (the primer/import table in
section 0.2, the seat table in section 0.4, the 30/60/90 table in section 0.6); the module names, chapter numbers, hours
and days are copied from them and nothing is added. Figures 2 and 5 are Illustrative: Figure 2 is a Monte Carlo of
geometric Brownian motion with the box's mu = 5% and sigma = 40%; Figure 5 uses the rows of the chapter's own
hand_history listing (Theo's July) and the standard-error formula sqrt(p(1-p)/n) stated in section 0.6.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
import numpy as np  # noqa: E402
from matplotlib.lines import Line2D  # noqa: E402
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Rectangle, Circle, Polygon  # noqa: E402
from matplotlib.path import Path  # noqa: E402

from style import *  # noqa: E402,F401,F403  (applies the rcParams on import)

plt.rcParams["text.parse_math"] = False      # "$" is always a dollar sign in these figures

BLUE_TINT = "#dbe8f9"
ORANGE_TINT = "#fbe6dc"
GREY_TINT = "#f1f0ed"
MONO = "DejaVu Sans Mono"


def rbox(ax, x, y, w, h, fc="white", ec=NEUTRAL, lw=0.9, r=0.8, z=3, ls="-"):
    """Rounded box with its lower-left corner at (x, y), in data units."""
    p = FancyBboxPatch((x + r, y + r), w - 2 * r, h - 2 * r, boxstyle=f"round,pad={r}", fc=fc, ec=ec,
                       lw=lw, zorder=z, linestyle=ls)
    ax.add_patch(p)
    return p


def curve(ax, p0, p1, color, lw=1.0, alpha=1.0, z=2, head=True, ls="-", bend=0.5, ms=6):
    """Cubic edge leaving p0 horizontally and arriving at p1 horizontally."""
    (x0, y0), (x1, y1) = p0, p1
    dx = (x1 - x0) * bend
    path = Path([(x0, y0), (x0 + dx, y0), (x1 - dx, y1), (x1, y1)],
                [Path.MOVETO, Path.CURVE4, Path.CURVE4, Path.CURVE4])
    ax.add_patch(FancyArrowPatch(path=path, arrowstyle="-|>" if head else "-", mutation_scale=ms, color=color,
                                 lw=lw, alpha=alpha, zorder=z, linestyle=ls, shrinkA=0, shrinkB=0))


def arrow(ax, p0, p1, color, lw=1.0, ls="-", z=4, ms=6, alpha=1.0, style="-|>"):
    ax.add_patch(FancyArrowPatch(p0, p1, arrowstyle=style, mutation_scale=ms, color=color, lw=lw, linestyle=ls,
                                 zorder=z, shrinkA=0, shrinkB=0, alpha=alpha))


def badge(ax, x, y, text, color=ORANGE, r=1.55, fs=7.0, z=6):
    ax.add_patch(Circle((x, y), r, fc=color, ec="white", lw=0.8, zorder=z))
    ax.text(x, y - 0.1, text, ha="center", va="center", fontsize=fs, color=INK, fontweight="bold", zorder=z + 1)


# --------------------------------------------------------------------------------------------------
# Figure 1 (section 0.2): the dependency map
# --------------------------------------------------------------------------------------------------
def fig_dependency_map():
    fig, ax = new_figure((7.0, 7.5))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 102.5)
    ax.axis("off")

    # --- primers (left column) -------------------------------------------------------------------
    PX, PW, PH = 0.5, 31.0, 11.0
    primers = {  # key: (y centre, name, module)
        "4B": (78.0, "4-B  Bond math", "bondmath.py"),
        "7B": (57.5, "7-B  Statistics for panels", "creditstats.py"),
        "6B": (37.0, "6-B  Options, two measures", "credit_options.py"),
        "12B": (17.0, "12-B  Restructuring process", "restructuring_state_machine.py"),
    }
    for k, (yc, name, mod) in primers.items():
        rbox(ax, PX, yc - PH / 2, PW, PH, fc=BLUE_TINT, ec=BLUE, lw=1.2)
        ax.text(PX + 1.6, yc + 2.4, name, fontsize=7.8, fontweight="bold", color=INK, va="center")
        ax.text(PX + 1.6, yc - 2.3, mod, fontsize=7.0, family=MONO, color=INK_2, va="center")

    # Chapter 1-B: the first station of the RV path, above 4-B
    ybx = 94.6
    rbox(ax, PX, ybx - 2.6, PW, 5.2, fc="white", ec=NEUTRAL, lw=0.9)
    ax.text(PX + 1.6, ybx, "1-B  A week in five quant shops", fontsize=7.4, color=INK, va="center")

    # --- consumers (middle column), in dependency order, not page order -------------------------
    CX, CW, CH = 51.0, 27.0, 4.0
    rows = [  # key, label, module, part tag, y
        ("c5", "Ch 5", "", "II"),
        ("c8", "Ch 8", "", "III"),
        ("c8D", "Ch 8-D", "pair_book.py", "III"),
        ("c8B", "Ch 8-B", "risk_model.py", "III"),
        ("c8C", "Ch 8-C", "pnl_explain.py", "III"),
        ("c24", "Ch 24", "", "VI"),
        ("c28", "Ch 28", "", "VIII"),
        ("c19", "Ch 19", "", "V"),
        ("c912", "Ch 9–12", "", "III"),
        ("c6", "Ch 6", "", "II"),
        ("c23", "Ch 23", "", "VI"),
        ("c12C", "Ch 12-C", "", "III"),
        ("c1317", "Part IV, Ch 13–17", "", "IV"),
        ("c3B", "Ch 3-B", "desk_calendar.py", "I"),
    ]
    top, bot = 91.0, 6.0
    pitch = (top - bot) / (len(rows) - 1)
    Y = {}
    for i, (k, lab, mod, part) in enumerate(rows):
        yc = top - i * pitch
        Y[k] = yc
        heavy = k == "c1317"
        rbox(ax, CX, yc - CH / 2, CW, CH, fc="white", ec=INK_2 if heavy else NEUTRAL, lw=1.4 if heavy else 0.9)
        ax.text(CX + 1.3, yc, lab, fontsize=7.8, fontweight="bold" if heavy else "normal", color=INK, va="center")
        if mod:
            ax.text(CX + 10.4, yc - 0.1, mod, fontsize=7.0, family=MONO, color=INK_2, va="center")
        ax.text(CX + CW - 1.0, yc, part, fontsize=7.0, color=MUTED, va="center", ha="right")

    # --- first-generation imports: primer -> chapters (table of section 0.2) ---------------------
    imports = {
        "4B": ["c5", "c8", "c8D", "c8B", "c8C", "c24", "c19"],
        "7B": ["c8", "c912", "c1317"],
        "6B": ["c6", "c23", "c12C", "c1317"],
        "12B": ["c12C", "c1317"],
    }
    x0, x1 = PX + PW, CX
    for pk, targets in imports.items():
        yc = primers[pk][0]
        tg = sorted(targets, key=lambda t: -Y[t])
        n = len(tg)
        for j, t in enumerate(tg):
            ys = yc + 4.3 - j * (8.6 / max(n - 1, 1)) if n > 1 else yc
            heavy = pk == "12B" and t == "c1317"
            curve(ax, (x0, ys), (x1 - 0.1, Y[t]), BLUE, lw=2.6 if heavy else 1.15, alpha=0.62 if not heavy else 0.8,
                  z=2, ms=5.5)

    # --- RV path (section 0.9): 1-B -> 4-B -> 5 -> 8 -> 8-D -> 8-B -> 8-C -> 24 -> 28 -------------
    # 1-B -> 4-B
    arrow(ax, (PX + PW / 2, ybx - 2.6), (PX + PW / 2, primers["4B"][0] + PH / 2), ORANGE, lw=1.0, ms=6, z=5)
    # 4-B -> Ch 5 overlay on its blue import edge (the first edge of the 4-B fan)
    curve(ax, (x0, primers["4B"][0] + 4.3), (x1 - 0.1, Y["c5"]), ORANGE, lw=0.9, z=3, ms=5.5)
    # rail on the right with stations
    RX = 85.0
    rv = ["c5", "c8", "c8D", "c8B", "c8C", "c24", "c28"]
    for a, b in zip(rv[:-1], rv[1:]):
        arrow(ax, (RX, Y[a] - 1.6), (RX, Y[b] + 1.6), ORANGE, lw=1.0, ms=6, z=4)
    for n, k in enumerate(rv, start=3):
        ax.plot([CX + CW, RX - 1.5], [Y[k], Y[k]], color=ORANGE, lw=0.9, zorder=2)
        badge(ax, RX, Y[k], str(n))
    badge(ax, PX + PW, ybx, "1")
    badge(ax, PX + PW, primers["4B"][0] + 4.3, "2")
    ax.text(RX + 3.0, Y["c5"], "RV path\n(section 0.9)", fontsize=7.4, color=INK_2, va="center",
            linespacing=1.15)
    ax.text(CX + CW + 2.0, Y["c1317"], "every chapter of\nPart IV sits behind 12-B", fontsize=7.2, color=MUTED,
            va="center", linespacing=1.15)

    # --- second generation: module sits on a module (violet dashed, in the gaps) ------------------
    gx = CX + 4.0
    for a, b in (("c8", "c8D"), ("c8B", "c8D"), ("c8B", "c8C")):
        down = Y[a] > Y[b]
        ya = Y[a] - CH / 2 - 0.15 if down else Y[a] + CH / 2 + 0.15
        yb = Y[b] + CH / 2 + 0.15 if down else Y[b] - CH / 2 - 0.15
        arrow(ax, (gx, ya), (gx, yb), VIOLET, lw=1.3, ls=(0, (2, 1.4)), ms=5.5, z=5)
    # 3-B <- section 3B.4
    rbox(ax, 24.0, Y["c3B"] - 2.7, 20.0, 5.4, fc=GREY_TINT, ec=NEUTRAL, lw=0.8)
    ax.text(25.2, Y["c3B"], "§3B.4 contract clocks", fontsize=7.0, color=INK_2, va="center")
    arrow(ax, (44.1, Y["c3B"]), (CX - 0.1, Y["c3B"]), VIOLET, lw=1.3, ls=(0, (2, 1.4)), ms=5.5, z=5)

    # --- legend (right, below the rail) ------------------------------------------------------------
    lx = CX + CW + 2.0
    items = [
        (BLUE, "-", 1.5, "a chapter imports\na primer's module"),
        (VIOLET, (0, (2, 1.4)), 1.5, "a module builds on\nother work in the book\n(second generation)"),
        (ORANGE, "-", 1.0, "the RV path, in order\n(thinner)"),
    ]
    yy = 43.0
    for c, ls, lw, txt in items:
        nl = txt.count("\n") + 1
        ym = yy - 1.3 * nl
        ax.plot([lx, lx + 3.6], [ym, ym], color=c, lw=lw, linestyle=ls, solid_capstyle="butt")
        ax.text(lx + 5.0, ym, txt, fontsize=7.2, color=INK_2, va="center", linespacing=1.15)
        yy -= 2.6 * nl + 2.2
    # column heads
    ax.text(PX, 101.0, "Primers, with the module each one ends in", fontsize=7.4, color=MUTED, va="center")
    ax.text(CX, 101.0, "Chapters that import them (Roman numeral: the Part of the book)", fontsize=7.4, color=MUTED, va="center")

    finish(fig, "00_02__dependency_map")


# --------------------------------------------------------------------------------------------------
# Figure 2 (section 0.3): the volatility tax at all three tiers
# --------------------------------------------------------------------------------------------------
def fig_volatility_tax():
    mu, sig = 0.05, 0.40
    rng = np.random.default_rng(20260628)
    big = np.exp((mu - 0.5 * sig**2) + sig * rng.standard_normal(100_000))      # one-year ending prices
    exact_mean, exact_med = np.exp(mu), np.exp(mu - 0.5 * sig**2)
    below = (big < 1.0).mean()

    fig, (ax, bx) = new_figure("wide", ncols=2, gridspec_kw={"width_ratios": [1.0, 1.15]})

    # left: one year, the ending price of 100,000 paths
    bins = np.arange(0.1, 3.3, 0.1)
    h, edges = np.histogram(big, bins=bins)
    share = 100 * h / len(big)
    colors = ["#bdbeb8" if e + 0.05 < 1.0 else "#dcdcd7" for e in edges[:-1]]
    ax.bar(edges[:-1] + 0.05, share, width=0.085, color=colors, zorder=2)
    ax.plot([exact_med, exact_med], [0, 11.9], color=ORANGE, lw=2.0, zorder=4)
    ax.plot([exact_mean, exact_mean], [0, 11.9], color=BLUE, lw=2.0, zorder=4)
    ax.text(exact_med - 0.07, 12.15, "median\n0.97", fontsize=8.5, color=INK_2, ha="right", va="bottom",
            linespacing=1.15)
    ax.text(exact_mean + 0.07, 12.15, "mean\n1.05", fontsize=8.5, color=INK_2, ha="left", va="bottom",
            linespacing=1.15)
    ax.text(3.15, 9.2, f"{below:.0%} of paths end\nbelow 1.00 (darker\nbars), though the\naverage is +5%", fontsize=8.3,
            color=INK_2, va="top", ha="right", linespacing=1.2)
    ax.set_xlim(0.0, 3.2)
    ax.set_ylim(0, 14.0)
    ax.set_xlabel("Price after one year (start = 1.00)")
    ax.set_ylabel("Share of 100,000 paths (%)")
    print(f"vol tax: sim mean {big.mean():.3f} (exact {exact_mean:.3f}), sim median {np.median(big):.3f} "
          f"(exact {exact_med:.3f}), share below 1: {below:.3f}")

    # right: the same model for ten years, log axis; the gap compounds
    T, steps = 10.0, 520
    t = np.linspace(0.0, T, steps + 1)
    dt = T / steps
    z = rng.standard_normal((40, steps))
    logs = np.concatenate([np.zeros((40, 1)), np.cumsum((mu - 0.5 * sig**2) * dt + sig * np.sqrt(dt) * z, axis=1)],
                          axis=1)
    for lp in logs:
        bx.plot(t, np.exp(lp), color=NEUTRAL, lw=0.55, alpha=0.7, zorder=1)
    bx.plot(t, np.exp(mu * t), color=BLUE, lw=2.2, zorder=4)
    bx.plot(t, np.exp((mu - 0.5 * sig**2) * t), color=ORANGE, lw=2.2, zorder=4)
    bx.axhline(1.0, color=INK_2, lw=0.8, ls=(0, (1.5, 2.5)), zorder=2)
    bx.set_yscale("log")
    bx.set_ylim(0.035, 45)                     # wide enough that no simulated path (0.04 to 27) is cut off
    bx.set_xlim(0, 10.0)
    bx.set_yticks([0.1, 0.25, 0.5, 1, 2, 4, 8, 16, 32])
    bx.set_yticklabels(["0.1", "0.25", "0.5", "1", "2", "4", "8", "16", "32"])
    bx.minorticks_off()
    bx.set_xlabel("Years")
    bx.set_ylabel("Price, log scale (start = 1.00)")
    label_end(bx, 10.0, np.exp(mu * 10), "average\n1.65", BLUE, dx=5)
    label_end(bx, 10.0, np.exp((mu - 0.5 * sig**2) * 10), "median\n0.74", ORANGE, dx=5)
    bx.set_xlim(0, 10.0)
    note(bx, "40 simulated paths, same mu and sigma", loc="upper left")
    assert logs.min() > np.log(0.035) and logs.max() < np.log(45)    # nothing clipped by the axis limits
    finish(fig, "00_02__volatility_tax")


# --------------------------------------------------------------------------------------------------
# Figure 3 (section 0.4): the four seat paths as transit lines
# --------------------------------------------------------------------------------------------------
def fig_seat_paths():
    W, H = 7.0, 5.95
    YO = 0.27
    fig, ax = new_figure((W, H))
    fig.set_layout_engine("none")
    ax.set_position([0, 0, 1, 1])
    ax.set_xlim(0, W)
    ax.set_ylim(0, H)
    ax.axis("off")

    X0, DX = 1.74, 0.288
    cx = lambda c: X0 + DX * c
    # strip order is chosen so that every interchange joins adjacent strips; colour follows the seat number
    strips = [  # seat no., name lines, hours, colour, y
        (1, "Market maker", "180\u2013220 hours", BLUE, 4.20 + YO),
        (4, "Risk and strat", "160\u2013200 hours", YELLOW, 3.10 + YO),
        (3, "Event and\ndistressed quant", "210\u2013250 hours", AQUA, 2.00 + YO),
        (2, "Systematic HY or\nIG PM", "230\u2013280 hours", ORANGE, 0.90 + YO),
    ]
    Ys = {s_[0]: s_[4] for s_ in strips}
    # stations: (column, label, side)  side +1 above, -1 below;  None label = interchange stop (named in the header)
    IX = {"1B": 0, "4B": 3, "6B": 7, "7B": 9, "12B": 14}
    st = {
        1: [(0, None, 1), (1, "Part I", 1), (2, "2-B", 1), (3, None, 1), (4, "3-B", 1), (10, "8", 1),
            (11, "8-B", 1), (12, "8-C", 1), (13, "Part V\n18\u201322", 1)],
        4: [(0, None, 1), (3, None, 1), (7, None, 1), (9, None, 1), (10, "8", 1), (11, "8-B", 1), (12, "8-C", 1),
            (15, "22", 1), (16, "Part VI\n23\u201324", 1), (17, "27", 1)],
        3: [(0, None, 1), (1, "Part I", 1), (3, None, 1), (4, "4-C", 1), (5, "5", 1), (6, "6", 1),
            (7, None, 1), (9, None, 1), (14, None, 1), (15, "12-C", 1), (16, "8-D", 1),
            (17, "Part IV\n13\u201317", 1)],
        2: [(0, None, 1), (1, "Part I", 1), (4, "4-C", 1), (5, "5", 1), (6, "6", 1), (7, None, 1),
            (8, "7", 1), (9, None, 1), (10, "Part III\n8\u201312", 1), (11, "Part VIII\n28", -1),
            (14, None, 1), (15, "Part IV\n13\u201317", 1)],
    }
    last_col = {1: 13, 4: 17, 3: 17, 2: 15}

    # interchange rails (behind the lines): the strips that stop there
    stops = {"1B": [1, 4, 3, 2], "4B": [1, 4, 3], "6B": [4, 3, 2], "7B": [1, 4, 3, 2], "12B": [3, 2]}
    for k, seats in stops.items():
        ys = [Ys[n] for n in seats]
        x = cx(IX[k])
        ax.add_patch(FancyBboxPatch((x - 0.075, min(ys) - 0.075), 0.15, max(ys) - min(ys) + 0.15,
                                    boxstyle="round,pad=0.0,rounding_size=0.075", fc="#ececE8", ec=NEUTRAL, lw=0.9,
                                    zorder=1))

    # lines
    for n, nm, hrs, col, y in strips:
        ax.plot([cx(0), cx(last_col[n])], [y, y], color=col, lw=4.6, solid_capstyle="round", zorder=2)
        # feeder stub from the 4-D line
        ax.annotate("", xy=(cx(0) - 0.09, y), xytext=(1.55, y),
                    arrowprops=dict(arrowstyle="-|>", color=MUTED, lw=1.0, mutation_scale=6), zorder=3)
        # name block
        ax.add_patch(Circle((0.17, y + 0.12), 0.115, fc=col, ec="white", lw=0.8, zorder=4))
        ax.text(0.17, y + 0.11, str(n), ha="center", va="center", fontsize=8.0, fontweight="bold", color=INK,
                zorder=5)
        ax.text(0.37, y + 0.22, nm, fontsize=7.8, fontweight="bold", color=INK, va="center", linespacing=1.15)
        ax.text(0.37, y - 0.2 if "\n" in nm else y - 0.12, hrs, fontsize=7.4, color=INK_2, va="center")
        for c, lab, side in st[n]:
            x = cx(c)
            if lab is None:
                ax.add_patch(Circle((x, y), 0.082, fc="white", ec=INK, lw=1.5, zorder=5))
            else:
                ax.add_patch(Circle((x, y), 0.06, fc="white", ec=INK, lw=1.2, zorder=5))
                ax.text(x, y + side * 0.15, lab, ha="center", va="bottom" if side > 0 else "top", fontsize=7.0,
                        color=INK, linespacing=1.05, zorder=6)

    # interchange headers
    def head(col_key, level_y, name, mod, ha="center", dx=0.0):
        x = cx(IX[col_key])
        ax.text(x + dx, level_y + 0.15, name, ha=ha, va="bottom", fontsize=7.6, fontweight="bold", color=INK)
        ax.text(x + dx, level_y + 0.15, mod, ha=ha, va="top", fontsize=7.0, family=MONO, color=INK_2)

    head("4B", 4.62 + YO, "4-B  Bond math", "bondmath.py")
    head("7B", 4.62 + YO, "7-B  Statistics", "creditstats.py")
    head("6B", 3.68 + YO, "6-B  Options", "credit_options.py")
    head("12B", 2.57 + YO, "12-B  Restructuring", "restructuring_state_machine.py", dx=-0.1)
    # 1-B header
    ax.text(cx(0) + 0.0, 5.05 + YO, "1-B  A week in five quant shops", ha="left", va="center", fontsize=7.6,
            fontweight="bold", color=INK)
    ax.plot([cx(0), cx(0)], [Ys[1] + 0.09, 4.95 + YO], color=NEUTRAL, lw=0.9, zorder=1)
    for k in ("4B", "7B"):
        ax.plot([cx(IX[k])] * 2, [Ys[1] + 0.09, 4.62 + YO + 0.04], color=NEUTRAL, lw=0.9, zorder=1)
    ax.plot([cx(IX["6B"])] * 2, [Ys[4] + 0.09, 3.68 + YO + 0.04], color=NEUTRAL, lw=0.9, zorder=1)
    ax.plot([cx(IX["12B"])] * 2, [Ys[3] + 0.09, 2.57 + YO + 0.04], color=NEUTRAL, lw=0.9, zorder=1)

    # 4-D feeder
    rbox(ax, 0.05, 4.78 + YO, 1.42, 0.62, fc=GREY_TINT, ec=NEUTRAL, lw=0.8, r=0.06)
    ax.text(0.14, 5.22 + YO, "4-D  Getting the seat", fontsize=7.4, fontweight="bold", color=INK, va="center")
    ax.text(0.14, 4.97 + YO, "feeder line: first, if you\nhave no offer yet", fontsize=7.0, color=INK_2, va="center",
            linespacing=1.1)
    ax.plot([1.47, 1.55], [5.0 + YO, 5.0 + YO], color=MUTED, lw=1.0, zorder=1)
    ax.plot([1.55, 1.55], [5.0 + YO, Ys[2]], color=MUTED, lw=1.0, zorder=1)

    # MM: the return to 7-B, drawn as a dashed arc under the line
    y1 = Ys[1]
    ax.add_patch(Circle((cx(9), y1), 0.082, fc="white", ec=INK, lw=1.3, ls=(0, (1.5, 1.2)), zorder=5))
    path = Path([(cx(13), y1 - 0.06), (cx(13) - 0.15, y1 - 0.5), (cx(9) + 0.15, y1 - 0.5), (cx(9), y1 - 0.09)],
                [Path.MOVETO, Path.CURVE4, Path.CURVE4, Path.CURVE4])
    ax.add_patch(FancyArrowPatch(path=path, arrowstyle="-|>", mutation_scale=6, color=INK_2, lw=1.0,
                                 linestyle=(0, (3, 2)), zorder=4, shrinkA=0, shrinkB=0))
    ax.text(cx(12) + 0.1, y1 - 0.43, "last, back to 7-B,\nwhen Chapter 18 calls on it", ha="center", va="top",
            fontsize=7.0, color=INK_2, linespacing=1.1)
    # DQ: Chapter 25 read back to back with 13
    y3 = Ys[3]
    ax.plot([cx(17), cx(17)], [y3 - 0.06, y3 - 0.33], color=AQUA, lw=2.2, ls=(0, (2, 1.4)), zorder=2)
    ax.add_patch(Circle((cx(17), y3 - 0.36), 0.06, fc="white", ec=INK, lw=1.2, zorder=5))
    ax.text(cx(17) - 0.11, y3 - 0.36, "25, read back to back with 13", ha="right", va="center", fontsize=7.0,
            color=INK_2)

    # key
    ky = 0.40
    ax.add_patch(Circle((0.17, ky), 0.06, fc="white", ec=INK, lw=1.2, zorder=5))
    ax.text(0.30, ky, "a chapter or Part", fontsize=7.0, color=INK_2, va="center")
    ax.add_patch(FancyBboxPatch((1.74, ky - 0.08), 0.16, 0.16, boxstyle="round,pad=0,rounding_size=0.08",
                                fc="#ececE8", ec=NEUTRAL, lw=0.9, zorder=1))
    ax.add_patch(Circle((1.82, ky), 0.07, fc="white", ec=INK, lw=1.5, zorder=5))
    ax.text(2.0, ky, "an interchange (a primer): every line that stops there imports its module", fontsize=7.0,
            color=INK_2, va="center")
    ax.text(0.05, 0.14, "Left to right is reading order, not page order. A dashed ring is a stop made later.",
            fontsize=7.0, color=MUTED, va="center")
    finish(fig, "00_02__seat_paths")


# --------------------------------------------------------------------------------------------------
# Figure 4 (section 0.6): the ninety days
# --------------------------------------------------------------------------------------------------
def fig_ninety_days():
    W, H = 7.0, 5.7
    fig, ax = new_figure((W, H))
    fig.set_layout_engine("none")
    ax.set_position([0, 0, 1, 1])
    ax.set_xlim(0, W)
    ax.set_ylim(0, H)
    ax.axis("off")

    XL, DAYW = 0.30, 0.0640
    X = lambda d: XL + DAYW * d
    T1, T2, T3, NA, PR = BLUE, ORANGE, AQUA, NEUTRAL, INK_2

    def chip(d0, d1, row, text, kind, top, pitch=0.30, h=0.255, direction=-1):
        x0, x1 = X(d0) + 0.05, X(d1) - 0.05
        y1 = top + direction * pitch * row
        y0 = y1 - h
        ax.add_patch(Rectangle((x0, y0), x1 - x0, h, fc="white", ec="#d6d5d0", lw=0.8, zorder=2))
        ax.add_patch(Rectangle((x0, y0), 0.065, h, fc=kind, ec="none", zorder=3))
        ax.text(x0 + 0.12, y0 + h / 2 - 0.005, text, fontsize=7.0, color=INK, va="center", zorder=4)

    ytop, yspine = 5.10, 2.20
    wins = [(0, 30, "Days 1\u201330", "55\u201360 hours"), (30, 60, "Days 31\u201360", "55\u201360 hours"),
            (60, 86, "Days 61\u201386", "45\u201355 hours")]
    for d0, d1, nm, hrs in wins:
        ax.text(X(d0) + 0.05, 5.46, nm, fontsize=8.2, fontweight="bold", color=INK, va="center")
        ax.text(X(d1) - 0.05, 5.46, hrs, fontsize=7.6, color=INK_2, va="center", ha="right")
    for d in (30, 60, 86):
        ax.plot([X(d), X(d)], [0.95, 5.62], color="#dcdbd6", lw=0.8, ls=(0, (3, 3)), zorder=1)

    # chapters above the line, coloured by tier
    w1 = [("Ch 1-B, in full", NA), ("Ch 1, 2, 4: cases, Trend Watches", T1), ("Ch 3: \u00a73.1\u20133.3", T2),
          ("Ch 3-B", NA), ("Ch 4-B", T2), ("build bondmath.py", T3), ("Ch 5: \u00a75.1\u20135.3", T2),
          ("App. A phrasebook (\u00a7A.10), open", NA)]
    w2 = [("Ch 6: \u00a76.1, 6.2, 6.4, 6.8", T2), ("build the \u00a76.11 engine", T3), ("Ch 6-B", NA),
          ("Ch 7, except \u00a77.7", T1), ("Ch 7-B", T2), ("Ch 8 through \u00a78.4", NA)]
    w3 = [("Ch 12-B", NA), ("Ch 13, 14", T1), ("\u00a713.3, \u00a713.8, \u00a714.2", T2),
          ("Ch 18 through \u00a718.6", NA)]
    for (d0, d1, _, _), items in zip(wins, (w1, w2, w3)):
        for r, (txt, kind) in enumerate(items):
            chip(d0, d1, r, txt, kind, ytop)

    # the strip of 90 days
    sh = 0.15
    for i in range(1, 91):
        a, b = X(i - 1), X(i)
        if i <= 86:
            fc = "#cfd9e6" if i % 7 else "#b3c4da"
            ax.add_patch(Rectangle((a + 0.004, yspine - sh / 2), b - a - 0.008, sh, fc=fc, ec="none", zorder=2))
        else:
            ax.add_patch(Rectangle((a + 0.004, yspine - sh / 2), b - a - 0.008, sh, fc="white", ec=MUTED, lw=0.6,
                                   hatch="/////", zorder=2))
    ax.text(X(0), yspine - 0.15, "day 0: Sun 28 Jun", fontsize=7.0, color=INK_2, va="top", ha="left")
    ax.text(X(86) - 0.04, yspine - 0.15, "day 86: Tue 22 Sep,\nfirst day on the desk", fontsize=7.0, color=INK_2, va="top",
            ha="right", linespacing=1.1)
    ax.text(X(86) + 0.06, yspine - 0.15, "days 87\u201390:\nfunded by sleep", fontsize=7.0, color=INK_2, va="top",
            ha="left", linespacing=1.1)
    arrow(ax, (X(90) + 0.07, yspine), (X(90) + 0.62, yspine), INK_2, lw=1.2, ms=8, z=3)
    ax.text(X(90) + 0.08, yspine + 0.1, "\u00a73B.8:\nthe ninety\ndays after", fontsize=7.0, color=INK_2,
            va="bottom", ha="left", linespacing=1.1)

    # checkpoints on the spine
    def diamond(x, y, r=0.095, fc=INK):
        ax.add_patch(Polygon([(x, y + r), (x + r, y), (x, y - r), (x - r, y)], fc=fc, ec="white", lw=0.8, zorder=6))

    diamond(X(30), yspine)
    diamond(X(60), yspine)
    ax.text(X(30), yspine + 0.16, "Part I gate\nday 30", fontsize=7.0, color=INK, ha="center", va="bottom",
            linespacing=1.1, fontweight="bold")
    ax.text(X(60), yspine + 0.16, "Part II gate\nday 60", fontsize=7.0, color=INK, ha="center", va="bottom",
            linespacing=1.1, fontweight="bold")
    # mock interview / mock morning at day 86 (a star)
    sx = X(86) - 0.04
    ax.plot([sx], [yspine], marker="*", markersize=11, color=INK, markeredgecolor="white", markeredgewidth=0.6,
            zorder=6)
    ax.plot([sx, sx], [yspine + 0.1, yspine + 0.52], color=INK_2, lw=0.8, zorder=5)
    ax.text(sx + 0.02, yspine + 0.55, "ends the last stretch:\nmock interview, or a\nmock morning if you\nhave the seat", fontsize=7.0,
            color=INK, ha="right", va="bottom", linespacing=1.1, fontweight="bold")

    # projects and checkpoints below the line
    low_top = 1.70
    l1 = ["Edge Ledger rows drafted (\u00a73.5)"]
    l2 = ["Project 1: TRACE, Roll spread", "Project 6: DD-to-PD map"]
    l3 = ["Project 2: Priming Risk Score", "Project 4: RFQ quoting game", "4-D's sixty tagged problems"]
    for (d0, d1, _, _), items in zip(wins, (l1, l2, l3)):
        for r, txt in enumerate(items):
            chip(d0, d1, r, txt, PR, low_top)

    # key
    ky = 0.62
    kx = 0.30
    for kind, lab in ((T1, "Tier 1: read"), (T2, "Tier 2: derive"), (T3, "Tier 3: build"), (NA, "tier not stated"),
                      (PR, "project or exercise set")):
        ax.add_patch(Rectangle((kx, ky - 0.07), 0.065, 0.14, fc=kind, ec="none"))
        ax.text(kx + 0.11, ky, lab, fontsize=7.0, color=INK_2, va="center")
        kx += 0.11 + 0.056 * len(lab) + 0.2
    ax.text(0.30, 0.30, "Chips show what the plan assigns to each stretch; the table gives no day-by-day order inside one. Darker cells: every seventh day.",
            fontsize=7.0, color=MUTED, va="center")
    finish(fig, "00_02__ninety_days")


# --------------------------------------------------------------------------------------------------
# Figure 5 (section 0.6): the hand history, calibration and how many exercises it takes
# --------------------------------------------------------------------------------------------------
def fig_hand_history():
    fig, (ax, bx) = new_figure("wide", ncols=2, sharey=True)

    # left: Theo's July, from the rows of the chapter's hand_history listing (checked rows only)
    buckets = [(0.5, 7, 10), (0.7, 2, 3), (0.9, 9, 12)]       # stated confidence, right, checked
    ax.plot([0.4, 1.0], [0.4, 1.0], color=NEUTRAL, lw=1.2, ls=(0, (4, 3)), zorder=1)
    ax.text(0.405, 0.37, "dashed: right as often\nas he said", fontsize=8, color=MUTED, rotation=0, va="top", ha="left",
            linespacing=1.1)
    for conf, k, n in buckets:
        p = k / n
        se = np.sqrt(p * (1 - p) / n)
        ax.errorbar([conf], [p], yerr=[se], fmt="o", color=BLUE, ecolor=BLUE, elinewidth=1.3, capsize=3.5,
                    markersize=7, zorder=4)
    ax.text(0.405, 1.0, "said 50%, right 7 of 10:\nunderconfident", fontsize=8, color=INK_2, ha="left", va="center",
            linespacing=1.15)
    ax.text(0.63, 0.22, "said 70%, right 2 of 3:\ntoo few to say", fontsize=8, color=INK_2, ha="left", va="center",
            linespacing=1.15)
    ax.text(0.998, 0.46, "said 90%, right 9 of 12:\noverconfident", fontsize=8, color=INK_2, ha="right",
            va="center", linespacing=1.15)
    ax.set_xlim(0.4, 1.0)
    ax.set_ylim(0.1, 1.08)
    ax.set_xticks([0.5, 0.7, 0.9])
    ax.set_xticklabels(["50%", "70%", "90%"])
    ax.set_yticks([0.2, 0.4, 0.6, 0.8, 1.0])
    ax.set_yticklabels(["20%", "40%", "60%", "80%", "100%"])
    ax.set_xlabel("Confidence written down before checking")
    ax.set_ylabel("Share right within the check")
    ax.set_title("Theo's July, by stated confidence", fontsize=8.6, loc="left")
    note(ax, "bars: one standard error", loc="lower left")

    # right: the 95% band on a hit rate of 0.72 as the number of checked exercises grows
    p = 0.72
    n = np.linspace(8, 160, 300)
    half = 2 * np.sqrt(p * (1 - p) / n)
    lo, hi = np.maximum(p - half, 0), np.minimum(p + half, 1)
    bx.fill_between(n, lo, hi, color=BLUE, alpha=0.16, lw=0, zorder=1)
    bx.plot(n, lo, color=BLUE, lw=LW, zorder=3)
    bx.plot(n, hi, color=BLUE, lw=LW, zorder=3)
    bx.axhline(p, color=BLUE, lw=0.9, ls=(0, (1.5, 2.5)), zorder=2)
    bx.axhline(0.60, color=INK_2, lw=0.9, ls=(0, (4, 3)), zorder=2)
    bx.text(158, 0.60 - 0.012, "0.60", fontsize=8, color=INK_2, ha="right", va="top")
    bx.text(158, p + 0.012, "hit rate 0.72", fontsize=8, color=INK_2, ha="right", va="bottom")
    for nn, tag in ((25, "a month"), (100, "a quarter")):
        h = 2 * np.sqrt(p * (1 - p) / nn)
        bx.plot([nn, nn], [p - h, p + h], color=INK, lw=1.2, zorder=4)
        bx.plot([nn, nn], [p - h, p + h], "o", color=INK, markersize=3.5, zorder=4)
    bx.annotate("25 exercises, a month:\n0.54 to 0.90", (25, 0.90), xytext=(34, 0.985), fontsize=8, color=INK_2,
                ha="left", va="center", linespacing=1.15, arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.8))
    bx.annotate("100, a quarter:\n0.63 to 0.81", (100, 0.81), xytext=(104, 0.93), fontsize=8, color=INK_2,
                ha="left", va="center", linespacing=1.15, arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.8))
    n_clear = (2 * np.sqrt(p * (1 - p)) / (p - 0.60)) ** 2
    bx.plot([n_clear], [0.60], "o", color=BLUE, markersize=5, zorder=5)
    bx.annotate(f"the band clears 0.60\nfrom about {n_clear:.0f} exercises", (n_clear, 0.60), xytext=(70, 0.34),
                fontsize=8, color=INK_2, ha="left", va="center", linespacing=1.15,
                arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.8))
    bx.set_xlim(0, 160)
    bx.set_xlabel("Checked exercises (hit rate held at 0.72)")
    bx.set_title("The 95% band around a hit rate", fontsize=8.6, loc="left")
    print(f"hand history: n at which band clears 0.60 = {n_clear:.1f}")
    finish(fig, "00_02__hand_history")


FIGS = {
    "dependency_map": fig_dependency_map,
    "volatility_tax": fig_volatility_tax,
    "seat_paths": fig_seat_paths,
    "ninety_days": fig_ninety_days,
    "hand_history": fig_hand_history,
}

if __name__ == "__main__":
    which = sys.argv[1:] or list(FIGS)
    for k in which:
        FIGS[k]()
