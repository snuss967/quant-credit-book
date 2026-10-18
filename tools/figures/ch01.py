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
         derivation), the price-pressure curves (eq. 1.7, Listing 1.4 demo) and the flow graph (eq. 1.6, Listing 1.4 demo).
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


def note_ink(ax, text, loc="lower left"):
    """Like style.note() but in INK_2 (MUTED is only 3.5:1 on white, too faint for 8 pt text that carries a claim)."""
    x, ha = (0.01, "left") if "left" in loc else (0.99, "right")
    y, va = (0.02, "bottom") if "lower" in loc else (0.98, "top")
    ax.text(x, y, text, transform=ax.transAxes, ha=ha, va=va, fontsize=8, color=INK_2)


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
            ha="center", va="center", fontsize=8.2, color=INK_2)
    ax.text(2.85, 82.4, "one step more than ten times\nthe other two combined", ha="center", va="center",
            fontsize=8.2, color=INK_2)

    # Monday's open
    ax.axhline(78, color=INK_2, linewidth=1.1, linestyle=(0, (4, 3)), zorder=1)
    ax.text(-0.5, 78.15, "Monday's open: 78", ha="left", va="bottom", fontsize=8.5, color=INK_2)
    ax.text(5.72, 78.15, "πJ is an expectation;\nFriday was the bad draw", ha="right", va="bottom", fontsize=8,
            color=INK_2)
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
    axl.annotate("", (L, norm.sf((L - mean_loss) / 7.0)), xytext=(37.5, 6e-12), textcoords="data",
                 arrowprops=dict(arrowstyle="-", color=NEUTRAL, linewidth=0.8))
    axl.plot([1.6], [2e-11], "o", color=GAUSS, markersize=4)
    axl.text(3.3, 2e-11, "Gaussian bag: losing 50\nis a 7-sd event, about\n1 in 800 billion",
             va="center", ha="left", fontsize=8.2, color=INK_2)
    axl.plot([19.6], [0.62], "o", color=TOXIC, markersize=4)
    axl.text(21.3, 0.05, "Jump bag: nothing, nothing,\nthen a loss of 50: 1 in 50", va="bottom", ha="left",
             fontsize=8.2, color=INK_2)
    note_ink(axl, "both bags: mean loss 1, sd 7", loc="lower left")

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
    axr.annotate(f"at 0.6 the Gaussian\ncharge is {100 * (1 - 1 / r06):.0f}% short\n(exact is {r06:.2f}\u00d7 as large)", (0.6, r06),
                 xytext=(2.05, 1.72), textcoords="data", ha="left", va="center", fontsize=8.2, color=INK_2,
                 arrowprops=dict(arrowstyle="-", color=NEUTRAL, linewidth=0.8, shrinkA=1, shrinkB=4))
    axr.annotate(f"at 3 the exact charge is\n{r3:.1f}× the Gaussian one", (3.0, r3), xytext=(-8, 8),
                 textcoords="offset points", ha="right", va="bottom", fontsize=8.2, color=INK_2)
    axr.text(3.95, 1.0, "quadratic = 1", ha="right", va="bottom", fontsize=8, color=INK_2)
    axr.set_xlim(0, 4.0)
    axr.set_ylim(0.5, 5.6)
    axr.set_xlabel("Position times jump times risk aversion, γqℓ")
    axr.set_ylabel("Exact jump charge ÷ Gaussian charge")
    return finish(fig, "ch01_gauss_vs_jump")


# --------------------------------------------------------------------------------------------------
# Figure 1.3: forced sellers leave a dent that heals; informed sellers leave one that does not
# (illustrative; eq. 1.7 with the Listing 1.4 demo inputs)
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
    ax.set_ylim(-10.0, 1.8)
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
    ax.plot([63.3], [1.05], "o", color=FORCED, markersize=4)
    ax.text(65.0, 1.05, "Forced seller (\u03c0 = 0):\nthe dent heals", ha="left", va="center", fontsize=8.5, color=INK_2)
    ax.plot([57.6], [-4.45], "o", color=TOXIC, markersize=4)
    ax.text(59.3, -4.45, f"A quarter informed (\u03c0 = 0.25):\n\u2212{perm:.2f} never comes back", ha="left",
            va="center", fontsize=8.5, color=INK_2)
    note_ink(ax, "\u03ba = 0.4, I/ADV = 12.8, \u03b8 = 1/20 per day, J = 13", loc="lower right")
    return finish(fig, "ch01_price_pressure_decay")


# --------------------------------------------------------------------------------------------------
# Figure 1.4: March 2020 on one page (real: FRED BAA10Y; dated events as sourced in section 1.8)
# --------------------------------------------------------------------------------------------------
def fig_march2020_timeline():
    import matplotlib.dates as mdates
    df = pd.read_csv(os.path.join(DATA, "ch01_BAA10Y.csv"), parse_dates=["observation_date"])
    df = df.dropna().set_index("observation_date")["BAA10Y"]
    d = pd.Timestamp
    left0, left1 = d("2020-03-02"), d("2020-04-30")
    right0, right1 = d("2020-05-01"), d("2020-12-31")
    assert abs(df[d("2020-03-23")] - 4.31) < 1e-9
    num = mdates.date2num

    fig = plt.figure(figsize=(7.0, 5.5), layout="constrained")
    gs = fig.add_gridspec(4, 2, width_ratios=[2.45, 1.15], height_ratios=[2.4, 0.8, 0.8, 1.2])
    axl = fig.add_subplot(gs[0, 0])
    axr = fig.add_subplot(gs[0, 1], sharey=axl)
    lanes = [fig.add_subplot(gs[i, 0], sharex=axl) for i in (1, 2, 3)]
    axf = fig.add_subplot(gs[3, 1], sharex=axr)
    note_ax = fig.add_subplot(gs[1:3, 1])

    # the two stretches of the one series
    for ax, a, b in ((axl, left0, left1), (axr, right0, right1)):
        seg = df[(df.index >= a) & (df.index <= b)]
        ax.plot(seg.index, seg.values, color=BLUE, linewidth=LW, zorder=3)
        ax.set_xlim(a, b)
    axl.set_ylim(1.7, 4.9)
    axl.set_ylabel("Baa less 10-yr Treasury\n(percentage points)")
    plt.setp(axr.get_yticklabels(), visible=False)
    axr.tick_params(left=False)
    peak = df[d("2020-03-23")]
    axl.plot([d("2020-03-23")], [peak], "o", color=BLUE, markersize=5.5, zorder=5)
    axl.annotate(f"23 Mar: {peak:.2f}, the peak", (d("2020-03-23"), peak), xytext=(8, 5), textcoords="offset points",
                 ha="left", va="bottom", fontsize=8.2, color=INK_2)
    axl.annotate("2 Mar: 2.44", (left0, df[left0]), xytext=(4, -12), textcoords="offset points", ha="left", va="top",
                 fontsize=8.2, color=INK_2)
    last = df[right1]
    axr.annotate(f"31 Dec: {last:.2f}", (right1, last), xytext=(-2, -9), textcoords="offset points", ha="right",
                 va="top", fontsize=8.2, color=INK_2)
    axl.tick_params(labelbottom=False)
    axr.tick_params(labelbottom=False)

    # lane styling
    for ax, name in zip(lanes, ["ETF wrappers", "Ford, the index", "The Fed"]):
        ax.set_ylim(0, 1)
        ax.set_yticks([])
        ax.grid(False)
        ax.set_facecolor(GREY_TINT)
        for sp in ("left", "bottom"):
            ax.spines[sp].set_visible(False)
        ax.set_ylabel(name, rotation=0, ha="right", va="center", fontsize=8.5, color=INK_2)
        ax.tick_params(labelbottom=False, bottom=False)
    axf.set_ylim(0, 1)
    axf.set_yticks([])
    axf.grid(False)
    axf.set_facecolor(GREY_TINT)
    for sp in ("left", "bottom"):
        axf.spines[sp].set_visible(False)

    # event verticals through the whole left stack
    ev = {"12": d("2020-03-12"), "13": d("2020-03-13"), "23": d("2020-03-23"), "25": d("2020-03-25"),
          "31": d("2020-03-31"), "9": d("2020-04-09")}
    for ax in [axl] + lanes:
        for k in ev.values():
            ax.axvline(k, color=NEUTRAL, linewidth=0.8, linestyle=(0, (3, 3)), zorder=1)

    def dot(ax, when, color, y=0.5):
        ax.plot([when], [y], "o", color=color, markersize=5.5, zorder=5, clip_on=False)

    def lab(ax, when, text, ha, y=0.5, dx=7):
        t = ax.annotate(text, (when, y), xytext=(dx if ha == "left" else -dx, 0), textcoords="offset points",
                        ha=ha, va="center", fontsize=8.2, color=INK_2, linespacing=1.15, zorder=6,
                        bbox=dict(facecolor=GREY_TINT, edgecolor="none", pad=1.2))
        t.set_in_layout(False)

    # lane 1: ETF wrappers (WealthManagement.com, 16 Mar 2020)
    dot(lanes[0], ev["12"], FORCED)
    dot(lanes[0], ev["13"], FORCED)
    lab(lanes[0], ev["13"], "12 Mar close: LQD 5.0% below NAV,\nVCIT 3.2%, SPIB 3.1%\n13 Mar: LQD discount 0.19%", "left")
    # lane 2: Ford and the index (Bloomberg; T. Rowe Price, Nov 2020)
    dot(lanes[1], ev["25"], FORCED)
    dot(lanes[1], ev["31"], FORCED)
    lab(lanes[1], ev["25"], "25 Mar: S&P cuts\nFord to BB+", "right")
    lab(lanes[1], ev["31"], "31 Mar: month-end rebalance;\n~$36bn of Ford debt leaves\nthe IG index", "left")
    # lane 3: the Fed (Federal Reserve; dossier for 9 Apr)
    dot(lanes[2], ev["23"], BLUE)
    dot(lanes[2], ev["9"], BLUE)
    lab(lanes[2], ev["23"], "23 Mar: SMCCF\nestablished", "right")
    lab(lanes[2], ev["9"], "9 Apr: facilities\nexpanded; issuers IG\non 22 Mar eligible", "left")

    # right column: purchase windows
    etf0, bond0 = d("2020-05-12"), d("2020-06-01")
    axf.set_ylim(0, 1)
    axf.add_patch(Rectangle((num(etf0), 0.64), num(right1) - num(etf0), 0.15, facecolor=BLUE, edgecolor="none", zorder=3))
    axf.add_patch(Rectangle((num(bond0), 0.26), num(right1) - num(bond0), 0.15, facecolor=BLUE, alpha=0.5,
                            edgecolor="none", zorder=3))
    for y, txt, ha, x in ((0.90, "ETF buying from 12 May", "left", num(etf0) - 2),
                          (0.52, "bonds from June", "left", num(bond0)),
                          (0.10, "all end 31 Dec", "right", num(right1))):
        t = axf.text(x, y, txt, ha=ha, va="center", fontsize=8.0, color=INK_2)
        t.set_in_layout(False)
    axr.axvline(etf0, color=NEUTRAL, linewidth=0.8, linestyle=(0, (3, 3)), zorder=1)
    axf.axvline(etf0, color=NEUTRAL, linewidth=0.8, linestyle=(0, (3, 3)), zorder=1)

    # time axes
    lanes[2].xaxis.set_major_locator(mdates.WeekdayLocator(byweekday=mdates.MO, interval=2))
    lanes[2].xaxis.set_major_formatter(mdates.DateFormatter("%-d %b"))
    lanes[2].tick_params(labelbottom=True, bottom=True)
    axf.xaxis.set_major_locator(mdates.MonthLocator(bymonth=[6, 9, 12]))
    axf.xaxis.set_major_formatter(mdates.DateFormatter("%b"))
    axf.tick_params(labelbottom=True, bottom=True)
    axf.set_xlabel("2020", fontsize=8.5)
    lanes[2].set_xlabel("2020")

    note_ax.axis("off")
    t = note_ax.text(0.0, 0.75, "Orange: forced-seller\nevents. Blue: the Fed.\nThe line is a market-\nwide stress gauge,\nnot a Ford series.",
                     transform=note_ax.transAxes, ha="left", va="top", fontsize=8.0, color=INK_2, linespacing=1.25)
    t.set_in_layout(False)
    return finish(fig, "ch01_march2020_timeline")


# --------------------------------------------------------------------------------------------------
# Figure 1.5: the forced-seller flow graph of the Ford-sized demo (illustrative; eq. 1.6, Listing 1.4)
# --------------------------------------------------------------------------------------------------
def _ribbon(ax, x0, x1, y0a, y0b, y1a, y1b, color, alpha, zorder=2):
    t = np.linspace(0, 1, 80)
    sm = 3 * t**2 - 2 * t**3
    xs = x0 + (x1 - x0) * t
    top = y0a + (y1a - y0a) * sm
    bot = y0b + (y1b - y0b) * sm
    ax.fill_between(xs, bot, top, facecolor=color, alpha=alpha, edgecolor="none", zorder=zorder)


def fig_forced_seller_flow_graph():
    # the Listing 1.4 demo, recomputed (holdings x fraction forced to sell; capacity pro rata; the rest to dealers)
    holders = [("IG index funds & ETFs", 5.0, 1.00), ("IG active funds", 8.0, 0.50), ("Insurers", 12.0, 0.25),
               ("Banks, foreign, other", 9.0, 0.10)]
    sells = [h * f for _, h, f in holders]
    absorbers = [("HY index funds", 3.0, "forced to buy at index inclusion"), ("Fallen-angel programs", 1.5, ""),
                 ("Crossover / distressed", 2.0, "")]
    Q = sum(sells)
    cap = sum(c for _, c, _ in absorbers)
    resid = Q - min(Q, cap)
    assert abs(Q - 12.9) < 1e-12 and abs(cap - 6.5) < 1e-12 and abs(resid - 6.4) < 1e-9
    buys = [c for _, c, _ in absorbers] + [resid]                 # the last one is the dealer residual
    k, gap, top = 2.9, 1.6, 77.0                                   # units per $bn, gap between nodes, top of stack

    fig, ax = new_figure((7.0, 5.7))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 82)
    ax.axis("off")

    # node blocks
    def stack(vals):
        y, out = top, []
        for v in vals:
            out.append((y, y - v * k))
            y -= v * k + gap
        return out
    L = stack(sells)
    R = stack(buys)
    xl0, xl1, xr0, xr1 = 22.0, 25.0, 69.0, 72.0
    for (ya, yb) in L:
        ax.add_patch(Rectangle((xl0, yb), xl1 - xl0, ya - yb, facecolor=FORCED, edgecolor="none", zorder=4))
    for i, (ya, yb) in enumerate(R):
        ax.add_patch(Rectangle((xr0, yb), xr1 - xr0, ya - yb, facecolor=FORCED if i == 3 else BLUE, edgecolor="none",
                               zorder=4))

    # ribbons: each seller's sale split over the buyers in proportion to size (the listing's edges)
    cur_r = [r[0] for r in R]
    for i, (ya, yb) in enumerate(L):
        cur_l = ya
        for j, bz in enumerate(buys):
            size = sells[i] * bz / Q
            h = size * k
            _ribbon(ax, xl1, xr0, cur_l, cur_l - h, cur_r[j], cur_r[j] - h,
                    FORCED if j == 3 else BLUE, 0.55 if j == 3 else 0.30)
            cur_l -= h
            cur_r[j] -= h

    # labels
    for (name, hold, frac), (ya, yb), sz in zip(holders, L, sells):
        yc = (ya + yb) / 2
        ax.text(xl0 - 1.2, yc + 1.0, name, ha="right", va="center", fontsize=8.5, color=INK)
        ax.text(xl0 - 1.2, yc - 1.7, f"${sz:.1f}bn  ({frac * 100:.0f}% of {hold:.1f})", ha="right", va="center",
                fontsize=8.0, color=INK_2)
    for (name, cp, extra), (ya, yb) in zip(absorbers, R[:3]):
        yc = (ya + yb) / 2
        ax.text(xr1 + 1.2, yc + (1.0 if extra else 0.0), f"{name}  ${cp:.1f}bn", ha="left", va="center", fontsize=8.5,
                color=INK)
        if extra:
            ax.text(xr1 + 1.2, yc - 1.9, "forced to buy at inclusion", ha="left", va="center", fontsize=8.0, color=INK_2)
    yd = (R[3][0] + R[3][1]) / 2
    ax.text(xr1 + 1.2, yd + 6.5, f"Dealers' balance sheets  ${resid:.1f}bn", ha="left", va="center", fontsize=8.5,
            color=INK)
    ax.text(xr1 + 1.2, yd + 3.0, "the price must fall until\nsomeone holds it", ha="left", va="center", fontsize=8.0,
            color=INK_2, linespacing=1.15)
    ax.text(xl0, 80.0, f"Forced to sell: ${Q:.1f}bn", ha="left", va="center", fontsize=8.5, color=INK, fontweight="bold")
    ax.text(xr0, 80.0, f"Absorbed ${cap:.1f}bn; left ${resid:.1f}bn", ha="left", va="center", fontsize=8.5, color=INK,
            fontweight="bold")
    ax.text(57.5, 80.0, "downgrade to HY", ha="center", va="center", fontsize=8.0, color=INK_2)

    # the Fed: a dashed absorber that switches on at day 10 (Exercise 4's counterfactual, not a forecast)
    fed = FancyBboxPatch((79.5, 31.0), 19.5, 9.6, boxstyle="round,pad=0.0,rounding_size=1.2", facecolor="white",
                         edgecolor=BLUE, linewidth=1.4, linestyle=(0, (4, 3)), zorder=4)
    ax.add_patch(fed)
    ax.text(89.25, 35.8, "Fed, from day 10\n$5bn (Exercise 4)\nhypothetical", ha="center", va="center",
            fontsize=8.0, color=INK_2, linespacing=1.15, zorder=5)
    ax.add_patch(FancyArrowPatch((xr1 + 0.4, R[3][1] + 2.2), (79.2, 35.8), arrowstyle="-|>", mutation_scale=9,
                                 color=BLUE, linewidth=1.3, linestyle=(0, (4, 3)), zorder=5,
                                 connectionstyle="arc3,rad=0.0"))

    # the pod PB-01 (illustrative): a long edge from the dealers, a short edge from a lender, a recall edge back
    ax.add_patch(FancyBboxPatch((1.0, 1.0), 98.0, 27.6, boxstyle="round,pad=0.0,rounding_size=1.5", facecolor="none",
                                edgecolor=NEUTRAL, linewidth=1.0, linestyle=(0, (2, 3)), zorder=1))
    ax.text(2.6, 26.2, "Illustrative: one pod, Pair Book PB-01 (Chapter 1-B)", ha="left", va="center", fontsize=8.0,
            color=INK_2)
    box_kw = dict(boxstyle="round,pad=0.0,rounding_size=1.2", facecolor="white", edgecolor=INK_2, linewidth=1.2, zorder=4)
    ax.add_patch(FancyBboxPatch((4.0, 6.2), 21.0, 10.0, **box_kw))
    ax.text(14.5, 11.2, "Lender\n(an asset manager)", ha="center", va="center", fontsize=8.3, color=INK, linespacing=1.2,
            zorder=5)
    ax.add_patch(FancyBboxPatch((50.0, 6.2), 24.0, 10.0, **box_kw))
    ax.text(62.0, 11.2, "Pod PB-01\nlong one single-B,\nshort another", ha="center", va="center", fontsize=8.3, color=INK,
            linespacing=1.2, zorder=5)
    arrow = dict(arrowstyle="-|>", mutation_scale=9, color=INK_2, linewidth=1.3, zorder=5)
    ax.add_patch(FancyArrowPatch((25.4, 12.6), (49.6, 12.6), **arrow))
    ax.text(37.5, 14.0, "short $39mm Halvorsen:\nborrowed bonds", ha="center", va="bottom", fontsize=8.0, color=INK_2,
            linespacing=1.15)
    ax.add_patch(FancyArrowPatch((49.6, 8.8), (25.4, 8.8), linestyle=(0, (4, 3)), **arrow))
    ax.text(37.5, 7.4, "recall: f = 1, window one\nsettlement cycle", ha="center", va="top", fontsize=8.0, color=INK_2,
            linespacing=1.15)
    ax.add_patch(FancyArrowPatch((xr0 - 2.0, R[3][1] - 0.6), (62.0, 16.6), **arrow, connectionstyle="arc3,rad=0.0"))
    ax.text(xr0 - 1.2, 22.0, "long $60mm Kestrel,\nbought from dealers", ha="left", va="center", fontsize=8.0,
            color=INK_2, linespacing=1.15)
    return finish(fig, "ch01_forced_seller_flow_graph")


if __name__ == "__main__":
    fig_bid_decomposition()
    fig_gauss_vs_jump()
    fig_price_pressure_decay()
    fig_march2020_timeline()
    fig_forced_seller_flow_graph()
