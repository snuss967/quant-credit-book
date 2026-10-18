"""Figures for Chapter 1 (The Anthology of the Desk & The Modern Quant Credit Landscape).

Run:  python3 tools/figures/ch01.py   -> assets/figures/ch01_*.png   (five figures)

Colour roles, held fixed across the chapter's figures (identity is also carried by direct labels):
  BLUE   = fair value / the Gaussian bag / natural absorbers (money that arrives by rule)
  ORANGE = inventory and cost / the forced seller / the dealer residual (what the price has to pay for)
  VIOLET = toxicity / the jump bag / the informed seller / the permanent component
  Aqua, yellow and magenta are not used (below 3:1 contrast on white).

Data.
  Real:  FRED BAA10Y (Moody's Baa yield less 10-year Treasury, daily), fetched from
         https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAA10Y and cached in tools/figures/data/ch01_BAA10Y.csv;
         the dated March-December 2020 events in the timeline, each as the chapter sources it in section 1.8
         (WealthManagement.com 16 Mar 2020; Federal Reserve; New York Fed 11 May 2020; Bloomberg and T. Rowe Price
         for Ford; the 9 Apr 2020 expansion from state/research/perspectives_dealers_and_systematic_shops.md).
  Illustrative (recomputed here from the formulas and inputs stated in the chapter): the bid waterfall (cold open,
         eq. 1.2), the Gaussian-versus-jump bag and the exact-to-quadratic penalty ratio (the Ways This Blows Up
         derivation), the price-pressure curves (eq. 1.7, Listing 1.3 demo) and the flow graph (eq. 1.6, Listing 1.3 demo).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402
from scipy.stats import norm  # noqa: E402
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Rectangle  # noqa: E402
from matplotlib.lines import Line2D  # noqa: E402

from style import *  # noqa: E402,F401,F403  (applies the rcParams on import)

plt.rcParams["text.parse_math"] = False      # "$" is always a dollar sign in these figures

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")

GAUSS, FORCED, TOXIC = BLUE, ORANGE, VIOLET
BLUE_TINT = "#dbe8f9"
ORANGE_TINT = "#fbe6dc"
VIOLET_TINT = "#e6e2f8"
GREY_TINT = "#f1f0ed"


# --------------------------------------------------------------------------------------------------
# Figure 1.1: the cold open as a waterfall (illustrative; eq. 1.2 with the chapter's inputs)
# --------------------------------------------------------------------------------------------------
def fig_bid_decomposition():
    S, q, dq, sig, gam, c, pi, J = 91.97, 5.0, 15.0, 8.0, 0.02, 0.25, 0.6, 13.0
    h = 5 / 252
    inv = 0.5 * gam * sig**2 * h * (2 * q + dq)           # 0.317
    tox = pi * J                                          # 7.8
    engine = S - inv - c                                  # 91.40
    bid = engine - tox                                    # 83.60
    assert abs(inv - 0.317) < 5e-4 and abs(engine - 91.40) < 5e-3 and abs(bid - 83.60) < 5e-3

    fig, ax = new_figure((7.0, 3.9))
    ax.grid(False)
    ax.yaxis.grid(True)
    ax.set_ylim(76, 93.6)
    ax.set_xlim(-0.55, 5.75)
    ax.set_xticks([])
    ax.spines["bottom"].set_visible(False)
    ax.set_ylabel("Price (points per 100 par); axis starts at 76")

    bw = 0.62
    # levels (the three prices that matter): thick ticks, labelled above
    levels = [(0, S, "Composite mid\n91.97", GAUSS), (3, engine, "Kaz's engine\nbids 91.40", GAUSS),
              (5, bid, "Theo's bid B*\n83.60", TOXIC)]
    for x, y, txt, col in levels:
        ax.plot([x - bw / 2, x + bw / 2], [y, y], color=col, linewidth=4.2, solid_capstyle="butt", zorder=4)
        ax.text(x, y + 0.45, txt, ha="center", va="bottom", fontsize=8.5, color=INK, fontweight="bold")

    # steps (floating bars)
    steps = [(1, S, S - inv, FORCED, "−0.317\ninventory", "(1.2) middle term"),
             (2, S - inv, engine, FORCED, "−0.25\ncost c", ""),
             (4, engine, bid, TOXIC, "−7.8 = π × J\ntoxicity", "0.6 × 13")]
    for x, top, bot, col, txt, _ in steps:
        ax.add_patch(Rectangle((x - bw / 2, bot), bw, top - bot, facecolor=col, edgecolor="none", zorder=3))
    # connectors
    for x0, x1, y in [(0, 1, S), (1, 2, S - inv), (2, 3, engine), (3, 4, engine), (4, 5, bid)]:
        ax.plot([x0 + bw / 2, x1 - bw / 2], [y, y], color=NEUTRAL, linewidth=0.9, zorder=2)

    ax.text(1, S - inv - 0.55, "−0.317\ninventory", ha="center", va="top", fontsize=8.5, color=INK_2)
    ax.text(2, engine - 0.55, "−0.25\ncost", ha="center", va="top", fontsize=8.5, color=INK_2)
    ax.text(4 + bw / 2 + 0.08, (engine + bid) / 2, "−7.8 = π × J\n= 0.6 × 13\ntoxicity", ha="left",
            va="center", fontsize=8.5, color=INK_2)

    # bracket for "more than ten times the other two combined"
    ax.annotate("", xy=(1.5, 89.0), xytext=(1.5, 89.0))
    ax.text(1.5, 86.6, "two small steps that every\nengine on the Street computes",
            ha="center", va="center", fontsize=8.2, color=MUTED)
    ax.text(2.85, 82.4, "one step more than ten times\nthe other two combined", ha="center", va="center",
            fontsize=8.2, color=MUTED)

    # Monday's open
    ax.axhline(78, color=INK_2, linewidth=1.1, linestyle=(0, (4, 3)), zorder=1)
    ax.text(-0.5, 78.15, "Monday's open: 78", ha="left", va="bottom", fontsize=8.5, color=INK_2)
    ax.text(5.72, 78.15, "πJ is an expectation;\nFriday was the bad draw", ha="right", va="bottom", fontsize=8,
            color=MUTED)
    return finish(fig, "ch01_bid_decomposition")


# --------------------------------------------------------------------------------------------------
# Figure 1.2: same mean, different bag (illustrative; the Math, Gently example and the Full Derivation)
# --------------------------------------------------------------------------------------------------
def fig_gauss_vs_jump():
    p, L = 0.02, 50.0
    mean_loss = p * L                                     # 1 point
    sd = np.sqrt(p * (1 - p)) * L                         # 7 points
    assert abs(mean_loss - 1.0) < 1e-12 and abs(sd - 7.0) < 0.01

    fig, axs = new_figure("wide", ncols=2)
    axl, axr = axs

    # left: exceedance curves on a log axis
    x = np.linspace(0.0, 62, 600)
    gauss = norm.sf((x - mean_loss) / 7.0)                # N(1, 7) loss
    axl.set_yscale("log")
    axl.set_ylim(1e-13, 2.0)
    axl.set_xlim(0, 66)
    axl.plot(x, gauss, color=GAUSS, linewidth=LW, zorder=3)
    axl.plot([0, L], [p, p], color=TOXIC, linewidth=LW, zorder=3)
    axl.plot([L, L], [p, 1e-13], color=TOXIC, linewidth=1.0, linestyle=(0, (2, 2)), zorder=2)
    axl.plot([L], [p], "o", color=TOXIC, markersize=5, zorder=5)
    axl.plot([L], [norm.sf((L - mean_loss) / 7.0)], "o", color=GAUSS, markersize=5, zorder=5)
    axl.set_xlabel("Loss over five days (points)")
    axl.set_ylabel("Probability of losing at least this much")
    axl.set_yticks([1e-12, 1e-9, 1e-6, 1e-3, 1])
    axl.set_yticklabels(["10⁻¹²", "10⁻⁹", "10⁻⁶", "10⁻³", "1"])
    axl.minorticks_off()
    axl.annotate("", (L, norm.sf((L - mean_loss) / 7.0)), xytext=(18, 3e-11), textcoords="data",
                 arrowprops=dict(arrowstyle="-", color=NEUTRAL, linewidth=0.8))
    axl.plot([1.6], [3e-11], "o", color=GAUSS, markersize=4)
    axl.text(3.3, 3e-11, "Gaussian bag: mean loss 1, sd 7;\nlosing 50 is a 7-sd event,\nabout 1 in 800 billion",
             va="center", ha="left", fontsize=8.2, color=INK_2)
    axl.plot([22.6], [0.1], "o", color=TOXIC, markersize=4)
    axl.text(24.3, 0.1, "Jump bag: mean loss 1, sd 7;\nnothing, nothing, then 50:\n1 in 50", va="center", ha="left",
             fontsize=8.2, color=INK_2)

    # right: exact CARA jump charge divided by the quadratic charge
    xs = np.linspace(0.02, 4.0, 400)
    ratio = 2 * (np.expm1(xs) - xs) / xs**2
    axr.axhline(1, color=NEUTRAL, linewidth=1.0, linestyle=(0, (3, 3)), zorder=1)
    axr.plot(xs, ratio, color=TOXIC, linewidth=LW, zorder=3)
    for x0 in (0.6, 3.0):
        y0 = 2 * (np.expm1(x0) - x0) / x0**2
        axr.plot([x0], [y0], "o", color=TOXIC, markersize=5.5, zorder=5)
    r06, r3 = 2 * (np.expm1(0.6) - 0.6) / 0.36, 2 * (np.expm1(3.0) - 3.0) / 9.0
    assert abs((1 - 1 / r06) - 0.19) < 0.01 and abs(r3 - 3.6) < 0.1
    axr.annotate(f"at 0.6 the Gaussian charge\nis {100 * (1 - 1 / r06):.0f}% short", (0.6, r06), xytext=(10, 22),
                 textcoords="offset points", ha="left", va="bottom", fontsize=8.2, color=INK_2,
                 arrowprops=dict(arrowstyle="-", color=NEUTRAL, linewidth=0.8))
    axr.annotate(f"at 3 the exact charge is\n{r3:.1f}× the Gaussian one", (3.0, r3), xytext=(-8, 8),
                 textcoords="offset points", ha="right", va="bottom", fontsize=8.2, color=INK_2)
    axr.text(3.95, 1.0, "quadratic = 1", ha="right", va="bottom", fontsize=8, color=MUTED)
    axr.set_xlim(0, 4.0)
    axr.set_ylim(0.5, 5.6)
    axr.set_xlabel("Position times jump times risk aversion, γqℓ")
    axr.set_ylabel("Exact jump charge ÷ Gaussian charge")
    return finish(fig, "ch01_gauss_vs_jump")


# --------------------------------------------------------------------------------------------------
# Figure 1.3: forced sellers leave a dent that heals; informed sellers leave one that does not
# (illustrative; eq. 1.7 with the Listing 1.3 demo inputs)
# --------------------------------------------------------------------------------------------------
def fig_price_pressure_decay():
    kappa, imb, adv, theta = 0.4, 6.4, 0.5, 1 / 20
    dent = kappa * imb / adv                              # 5.12 points
    assert abs(dent - 5.12) < 1e-9
    t = np.linspace(0, 90, 361)
    forced = -dent * np.exp(-theta * t)
    pi_, J = 0.25, 13.0
    perm = pi_ * J                                         # 3.25 points that never come back
    informed = -perm - dent * np.exp(-theta * t)

    fig, ax = new_figure("wide")
    ax.axhline(0, color=INK_2, linewidth=0.9, zorder=2)
    ax.plot(t, forced, color=FORCED, linewidth=LW, zorder=4)
    ax.plot(t, informed, color=TOXIC, linewidth=LW, zorder=4)
    ax.axhline(-perm, color=TOXIC, linewidth=0.9, linestyle=(0, (3, 3)), zorder=1)
    ax.set_xlim(0, 90)
    ax.set_ylim(-10.0, 1.0)
    ax.set_xlabel("Days since the trigger date")
    ax.set_ylabel("Price minus fair value p* (points)")
    leader = dict(arrowstyle="-", color=NEUTRAL, linewidth=0.8)

    half = np.log(2) / theta
    ax.plot([half], [-dent / 2], "o", color=FORCED, markersize=5.5, zorder=5)
    ax.annotate(f"half-life {half:.0f} days:\nhalf the dent is gone", (half, -dent / 2), xytext=(2, -0.6),
                textcoords="data", fontsize=8.2, color=INK_2, ha="left", va="center", arrowprops=leader)
    rec = dent * (1 - np.exp(-theta * 60))
    y60 = forced[np.searchsorted(t, 60)]
    ax.plot([60], [y60], "o", color=FORCED, markersize=5.5, zorder=5)
    ax.annotate(f"day 60: {rec:.2f} of the {dent:.2f} points\nhave come back; that is\nthe absorber's pay", (60, y60),
                xytext=(52, -1.75), textcoords="data", fontsize=8.2, color=INK_2, ha="center", va="center",
                arrowprops=leader)
    ax.plot([0], [-dent], "o", color=FORCED, markersize=5.5, zorder=5)
    ax.text(2.5, -5.6, f"day 0: dent of {dent:.2f}", fontsize=8.2, color=INK_2, ha="left", va="center")
    ax.plot([0], [-perm - dent], "o", color=TOXIC, markersize=5.5, zorder=5)
    ax.text(2.5, -8.9, f"day 0: {perm + dent:.2f} below fair value", fontsize=8.2, color=INK_2, ha="left", va="center")
    ax.plot([89], [0.55], "o", color=FORCED, markersize=4, clip_on=False)
    ax.text(87.2, 0.55, "Forced seller (\u03c0 = 0): the dent heals", ha="right", va="center", fontsize=8.5, color=INK_2)
    ax.plot([89], [-4.4], "o", color=TOXIC, markersize=4, clip_on=False)
    ax.text(87.2, -4.4, f"A quarter informed (\u03c0 = 0.25):\n\u2212{perm:.2f} never comes back", ha="right",
            va="center", fontsize=8.5, color=INK_2)
    note(ax, "\u03ba = 0.4, I/ADV = 12.8, \u03b8 = 1/20 per day, J = 13", loc="lower right")
    return finish(fig, "ch01_price_pressure_decay")


if __name__ == "__main__":
    fig_bid_decomposition()
    fig_gauss_vs_jump()
    fig_price_pressure_decay()
