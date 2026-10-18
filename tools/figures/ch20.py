"""Chapter 20 figures: Credit ETF Creation/Redemption Arbitrage.

Run from anywhere:  python3 tools/figures/ch20.py
Writes assets/figures/ch20_*.png (five figures, in order of appearance in the chapter).

Data policy (see style.py): fig 4 uses real data (FRED BAA10Y, cached in tools/figures/data/ch20_BAA10Y.csv;
pass --refresh to re-download it) plus ETF premiums/discounts exactly as the chapter cites them. Figs 1-3 and 5 are
schematic or generated from the models stated in the chapter text, and their captions say "Illustrative".
"""
import csv
import datetime as dt
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from style import *  # noqa: F401,F403,E402  (applies the rcParams on import)

import matplotlib.dates as mdates  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Rectangle  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data", "ch20_BAA10Y.csv")
FRED_URL = "https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAA10Y&cosd=2020-02-01&coed=2020-06-30"

# Chapter-wide colour roles. A role keeps its colour in every figure.
C_CREATE = BLUE        # creation: ETF rich, new shares
C_REDEEM = ORANGE      # redemption: ETF cheap, shares retired; also the stressed state
C_CALM = MUTED         # calm state
C_SPREAD = VIOLET      # the Baa-Treasury spread series (fig 4)
TINT_CREATE = "#cde2fb"
TINT_REDEEM = "#fadccd"
TINT_BAND = "#ecebe7"
BOX_FILL = "#f4f3f0"
POS_COL = "#3987e5"    # premium (DIVERGING, blue end)
NEG_COL = "#e66767"    # discount (DIVERGING, red end)


# --------------------------------------------------------------------------------------------------------------
# Figure 20.1: the wrapper's flows (schematic)
# --------------------------------------------------------------------------------------------------------------
def _box(ax, cx, cy, w, h, text, sub=None, fs=9.5):
    ax.add_patch(FancyBboxPatch((cx - w / 2, cy - h / 2), w, h, boxstyle="round,pad=0,rounding_size=0.12",
                                facecolor=BOX_FILL, edgecolor=NEUTRAL, linewidth=1.0, zorder=2))
    ax.text(cx, cy + (0.12 if sub else 0), text, ha="center", va="center", fontsize=fs, color=INK,
            fontweight="bold", zorder=3)
    if sub:
        ax.text(cx, cy - 0.27, sub, ha="center", va="center", fontsize=8, color=INK_2, zorder=3)


def _arrow(ax, p0, p1, color):
    ax.add_patch(FancyArrowPatch(p0, p1, arrowstyle="-|>", mutation_scale=10, linewidth=1.5, color=color,
                                 shrinkA=0, shrinkB=0, zorder=4))


def fig_wrapper_flows():
    fig, ax = new_figure("wide")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5.15)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.grid(False)

    bw, bh = 1.85, 1.15
    yc = 3.45
    xb, xa, xf = 1.0, 4.9, 8.95   # bond market, AP, fund
    xe, ye = 4.9, 0.78            # exchange

    # market shading
    ax.add_patch(Rectangle((3.7, 2.5), 6.3, 2.6, facecolor="#f9f8f6", edgecolor="none", zorder=0))
    ax.text(9.92, 5.02, "Primary market: creation units, in kind or cash", ha="right", va="top", fontsize=8.2,
            color=MUTED, style="italic")
    ax.add_patch(Rectangle((3.7, 0.05), 6.3, 2.35, facecolor="#f9f8f6", edgecolor="none", zorder=0))
    ax.text(9.92, 0.12, "Secondary market: shares among investors", ha="right", va="bottom", fontsize=8.2,
            color=MUTED, style="italic")

    _box(ax, xb, yc, bw, bh, "Bond market", "dealers, RFQ, TRACE")
    _box(ax, xa, yc, bw, bh, "Authorized\nparticipant (AP)")
    _box(ax, xf, yc, bw, bh, "ETF (the fund)", "issues, retires units")
    _box(ax, xe, ye, 2.6, 0.95, "Exchange", "investors, market makers")

    # Bond market <-> AP
    x0, x1 = xb + bw / 2 + 0.08, xa - bw / 2 - 0.08
    _arrow(ax, (x0, yc + 0.28), (x1, yc + 0.28), C_CREATE)
    ax.text((x0 + x1) / 2, yc + 0.40, "buy bonds\nat the offer", ha="center", va="bottom", fontsize=8.2, color=INK_2)
    _arrow(ax, (x1, yc - 0.28), (x0, yc - 0.28), C_REDEEM)
    ax.text((x0 + x1) / 2, yc - 0.40, "sell bonds\nat the bid", ha="center", va="top", fontsize=8.2, color=INK_2)

    # AP <-> Fund: creation (blue) on top, redemption (orange) below; each label sits just above its arrow
    x0, x1 = xa + bw / 2 + 0.08, xf - bw / 2 - 0.08
    xm = (x0 + x1) / 2
    lanes = [(yc + 0.86, "bonds + cash balancing amount", True, C_CREATE),
             (yc + 0.34, "new shares", False, C_CREATE),
             (yc - 0.28, "creation unit of shares", True, C_REDEEM),
             (yc - 0.80, "redemption basket", False, C_REDEEM)]
    for y, txt, to_fund, col in lanes:
        _arrow(ax, (x0, y) if to_fund else (x1, y), (x1, y) if to_fund else (x0, y), col)
        ax.text(xm, y + 0.07, txt, ha="center", va="bottom", fontsize=8.2, color=INK_2)

    # AP <-> Exchange (vertical)
    y0, y1 = yc - bh / 2 - 0.08, ye + 0.95 / 2 + 0.08
    _arrow(ax, (xa - 0.45, y0), (xa - 0.45, y1), C_CREATE)
    ax.text(xa - 0.60, (y0 + y1) / 2, "sell the new\nshares", ha="right", va="center", fontsize=8.2, color=INK_2)
    _arrow(ax, (xa + 0.45, y1), (xa + 0.45, y0), C_REDEEM)
    ax.text(xa + 0.60, (y0 + y1) / 2, "buy shares\nthat are cheap", ha="left", va="center", fontsize=8.2, color=INK_2)

    # legend (patches)
    ax.add_patch(Rectangle((0.2, 1.72), 0.32, 0.14, facecolor=C_CREATE, zorder=3))
    ax.text(0.62, 1.79, "Creation: ETF rich", va="center", fontsize=8.3, color=INK_2)
    ax.add_patch(Rectangle((0.2, 1.35), 0.32, 0.14, facecolor=C_REDEEM, zorder=3))
    ax.text(0.62, 1.42, "Redemption: ETF cheap", va="center", fontsize=8.3, color=INK_2)
    return finish(fig, "ch20_wrapper_flows")


# --------------------------------------------------------------------------------------------------------------
# Figure 20.2: the static arbitrage band, with the chapter's worked numbers
# --------------------------------------------------------------------------------------------------------------
def fig_arbitrage_band():
    from matplotlib.patches import Patch
    fig, ax = new_figure("wide")
    xmin, xmax = -118, 92
    rows = [
        # y, label, lo, hi
        (0.9, "High-yield fund\n($\\bar{c}$ = 30 bp, $c^R$ = 45 bp)", -21, 66),
        (0.0, "Investment-grade fund\n($\\bar{c}$ = 8 bp, $c^R$ = 10 bp)", -6, 20),
    ]
    h = 0.34
    for y, _lab, lo, hi in rows:
        ax.add_patch(Rectangle((xmin, y - h / 2), lo - xmin, h, facecolor=TINT_REDEEM, edgecolor="none", zorder=1))
        ax.add_patch(Rectangle((lo, y - h / 2), hi - lo, h, facecolor=TINT_BAND, edgecolor="none", zorder=1))
        ax.add_patch(Rectangle((hi, y - h / 2), xmax - hi, h, facecolor=TINT_CREATE, edgecolor="none", zorder=1))
        for edge in (lo, hi):
            ax.plot([edge, edge], [y - h / 2 - 0.04, y + h / 2 + 0.04], color=INK_2, linewidth=1.3, zorder=3)
        ax.text(lo - 2, y - h / 2 - 0.07, f"{lo:+d} bp".replace("-", "\u2212"), ha="right", va="top", fontsize=8.3,
                color=INK_2)
        ax.text(hi + 2, y - h / 2 - 0.07, f"{hi:+d} bp", ha="left", va="top", fontsize=8.3, color=INK_2)

    ax.axvline(0, color=NEUTRAL, linewidth=0.9, linestyle=(0, (3, 3)), zorder=0)
    ax.annotate("NAV", (0, 1.58), ha="center", va="bottom", fontsize=8, color=MUTED)

    # observations: issuer pages, mid-Oct 2026 (HYG +0.02%, JNK +0.15%, LQD +0.04%) and the cold-open scene
    def dot(x, y, txt, dx, dy, ha):
        ax.plot([x], [y], "o", color=INK, markersize=5.5, zorder=5)
        ax.annotate(txt, (x, y), xytext=(dx, dy), textcoords="offset points", ha=ha, va="bottom", fontsize=8.3,
                    color=INK, zorder=6)

    dot(2, 0.9, "HYG +2", -3, 24, "right")
    dot(15, 0.9, "JNK +15", 3, 24, "left")
    dot(4, 0.0, "LQD +4", 3, 24, "left")
    dot(-93, 0.9, "Cold open: HYG \u221293", 0, 24, "center")

    ax.legend(handles=[Patch(facecolor=TINT_REDEEM, label="redemption pays (ETF cheap)"),
                       Patch(facecolor=TINT_BAND, label="no arbitrage"),
                       Patch(facecolor=TINT_CREATE, label="creation pays (ETF rich)")],
              loc="lower center", bbox_to_anchor=(0.5, 1.0), ncol=3, fontsize=8.3, handlelength=1.2, columnspacing=1.6)

    ax.set_xlim(xmin, xmax)
    ax.set_ylim(-0.5, 1.62)
    ax.set_yticks([r[0] for r in rows])
    ax.set_yticklabels([r[1] for r in rows])
    ax.tick_params(axis="y", length=0)
    ax.grid(False)
    ax.spines["left"].set_visible(False)
    ax.set_xlabel("Premium to NAV (bp of NAV)")
    return finish(fig, "ch20_arbitrage_band")


# --------------------------------------------------------------------------------------------------------------
# Figure 20.3: AP price impact, calm vs stress (model of section 20.3.2)
# --------------------------------------------------------------------------------------------------------------
def fig_ap_price_impact():
    fig, (a, b) = new_figure("wide", ncols=2, gridspec_kw={"width_ratios": [1.15, 1]})

    # Left: discount psi*F against net selling F. Calm slope is set so that $1bn costs 1 bp; stress is 288x steeper.
    psi_calm = 1.0                       # bp of NAV per $1bn of net selling
    mult = 2 * (12 / 2) ** 2 * (8 / 2)   # 2 x 36 x 4 = 288
    F = np.linspace(0, 1.5, 100)
    a.plot(F, psi_calm * F, color=C_CALM, linewidth=LW)
    a.plot(F, psi_calm * mult * F, color=C_REDEEM, linewidth=LW)
    a.plot([F[-1]], [psi_calm * F[-1]], "o", color=C_CALM, markersize=4, zorder=5)
    a.plot([F[-1]], [psi_calm * mult * F[-1]], "o", color=C_REDEEM, markersize=4, zorder=5)
    a.annotate("Stress: 288 bp per $1bn", (F[-1], psi_calm * mult * F[-1]), xytext=(-6, 10), textcoords="offset points",
               ha="right", va="bottom", fontsize=8.5, color=INK_2)
    a.annotate("Calm: 1 bp per $1bn", (1.05, 22), ha="left", va="bottom", fontsize=8.5, color=INK_2)
    a.plot([1.0, 1.0], [1, mult], color=NEUTRAL, linewidth=0.9, linestyle=(0, (3, 3)), zorder=1)
    a.annotate("the same $1bn of selling:\n1 bp becomes about 2.9%", (1.0, 170), xytext=(6, 0),
               textcoords="offset points", ha="left", va="center", fontsize=8.3, color=INK_2)
    a.set_xlim(0, 1.78)
    a.set_ylim(0, 520)
    a.set_xticks([0, 0.5, 1.0, 1.5])
    a.set_xlabel("Net ETF selling to be redeemed, F ($bn)")
    a.set_ylabel("Discount from AP price impact, \u03c8F (bp)")

    # Right: the multiplier builds up as a product
    steps = [("Calm", 1), ("Risk\naversion\n\u00d72", 2), ("Basis vol\n2%\u219212%\n\u00d736", 72),
             ("Hold time\n2\u21928 days\n\u00d74", 288)]
    xs = np.arange(len(steps))
    cols = [C_CALM, C_REDEEM, C_REDEEM, C_REDEEM]
    b.bar(xs, [s_[1] for s_ in steps], width=0.66, color=cols)
    for x, (_t, v) in zip(xs, steps):
        b.annotate(f"{v}\u00d7", (x, v), xytext=(0, 3), textcoords="offset points", ha="center",
                   va="bottom", fontsize=8.6, color=INK)
    b.set_xticks(xs)
    b.set_xticklabels([s_[0] for s_ in steps], fontsize=7.8)
    b.set_ylim(0, 335)
    b.set_ylabel("Price impact \u03c8 (multiple of calm)")
    b.tick_params(axis="x", length=0)
    return finish(fig, "ch20_ap_price_impact")


# --------------------------------------------------------------------------------------------------------------
# Figure 20.4: March 2020 tape (real data: FRED BAA10Y; ETF discounts as cited in section 20.5.1)
# --------------------------------------------------------------------------------------------------------------
def load_baa10y(refresh=False):
    if refresh or not os.path.exists(DATA):
        import urllib.request
        os.makedirs(os.path.dirname(DATA), exist_ok=True)
        with urllib.request.urlopen(FRED_URL, timeout=60) as r, open(DATA, "wb") as f:
            f.write(r.read())
    d, v = [], []
    with open(DATA) as f:
        for row in csv.DictReader(f):
            if row["BAA10Y"].strip() in ("", "."):
                continue
            d.append(dt.datetime.strptime(row["observation_date"], "%Y-%m-%d"))
            v.append(float(row["BAA10Y"]))
    return np.array(d), np.array(v)


def fig_march2020_tape(refresh=False):
    d, v = load_baa10y(refresh)
    lo, hi = dt.datetime(2020, 2, 10), dt.datetime(2020, 5, 22)
    m = (d >= lo) & (d <= hi)
    d, v = d[m], v[m]
    fig, (a, b) = plt.subplots(2, 1, figsize=(7.0, 4.9), layout="constrained", sharex=True,
                               gridspec_kw={"height_ratios": [1.75, 1.15]})

    a.plot(d, v, color=C_SPREAD, linewidth=LW)
    i = int(np.argmax(v))
    a.plot([d[i]], [v[i]], "o", color=C_SPREAD, markersize=5)
    a.annotate(f"peak {v[i]:.2f} on Mar 23", (d[i], v[i]), xytext=(-6, 9), textcoords="offset points", ha="right",
               va="bottom", fontsize=8.3, color=INK_2)
    a.set_ylabel("Baa yield minus 10-yr Treasury (pp)")
    a.set_ylim(1.8, 5.9)

    events = [(dt.datetime(2020, 3, 23), "Mar 23\nSMCCF announced", "right"),
              (dt.datetime(2020, 4, 9), "Apr 9\nHY ETFs added", "left"),
              (dt.datetime(2020, 5, 12), "May 12\nETF buying starts", "right")]
    for x, txt, ha in events:
        for ax_ in (a, b):
            ax_.axvline(x, color=NEUTRAL, linewidth=0.9, linestyle=(0, (3, 3)), zorder=1)
        a.annotate(txt, (x, 0.98), xycoords=("data", "axes fraction"), xytext=(-3 if ha == "right" else 3, 0),
                   textcoords="offset points", fontsize=8, color=INK_2, va="top", ha=ha)

    # reported closing premium/discount to NAV (percent), as cited in the chapter
    pts = [(dt.datetime(2020, 3, 12), -7.5), (dt.datetime(2020, 3, 12), -8.0),
           (dt.datetime(2020, 3, 19), -5.08), (dt.datetime(2020, 3, 19), 0.85)]
    b.axhline(0, color=INK_2, linewidth=0.9, zorder=2)
    for x, y in pts:
        col = POS_COL if y > 0 else NEG_COL
        b.plot([x, x], [0, y], color=col, linewidth=1.2, zorder=3)
        b.plot([x], [y], "o", color=col, markersize=6, zorder=4)
    b.annotate("UCITS USD IG ETF −7.5%\nUS floating-rate ETF −8.0%", (dt.datetime(2020, 3, 12), -7.75),
               xytext=(-7, 0), textcoords="offset points", ha="right", va="center", fontsize=8.3, color=INK_2)
    b.annotate("LQD −5.08%", (dt.datetime(2020, 3, 19), -5.08), xytext=(7, 0), textcoords="offset points",
               ha="left", va="center", fontsize=8.3, color=INK_2)
    b.annotate("HYG +0.85%", (dt.datetime(2020, 3, 19), 0.85), xytext=(7, 1), textcoords="offset points",
               ha="left", va="center", fontsize=8.3, color=INK_2)
    b.set_ylim(-10.2, 3.2)
    b.set_ylabel("ETF close vs NAV (%)")
    b.xaxis.set_major_locator(mdates.WeekdayLocator(byweekday=mdates.MO, interval=2))
    b.xaxis.set_major_formatter(mdates.DateFormatter("%b %d"))
    b.set_xlim(lo, hi)
    for lab in b.get_xticklabels():
        lab.set_fontsize(8)
    b.set_xlabel("Date, 2020")
    return finish(fig, "ch20_march2020_tape")


# --------------------------------------------------------------------------------------------------------------
# Figure 20.5: the liquidity sleeve of a loan ETF, eq. (20.8)
# --------------------------------------------------------------------------------------------------------------
def fig_sleeve_runway():
    fig, axes = new_figure("wide", ncols=2, sharey=True)
    Lw = 2.4                                      # loan settlement lag in weeks (about 17 days, Markit Q2-2016)
    sleeves = [(3.0, SEQ_BLUE_STEPS[4], "3% sleeve"), (5.0, SEQ_BLUE_STEPS[7], "5% sleeve"),
               (10.0, SEQ_BLUE_STEPS[11], "10% sleeve")]
    t = np.linspace(0, 6, 301)
    for ax, R, ttl in ((axes[0], 2.1, "Steady outflow, 2.1% of fund a week\nsleeve must exceed 5.0%"),
                       (axes[1], 4.2, "Double the pace, 4.2% of fund a week\nsleeve must exceed 10.1%")):
        ax.axhspan(-9, 0, color="#faf0ed", zorder=0)
        ax.axhline(0, color=INK_2, linewidth=0.9, zorder=2)
        ax.axvline(Lw, color=NEUTRAL, linewidth=0.9, linestyle=(0, (3, 3)), zorder=1)
        for phi0, col, lab in sleeves:
            phi = phi0 - R * np.minimum(t, Lw)
            ax.plot(t, phi, color=col, linewidth=LW, zorder=3)
            ax.plot([t[-1]], [phi[-1]], "o", color=col, markersize=4, zorder=5, clip_on=False)
            near0 = abs(phi[-1]) < 0.8
            ax.annotate(lab, (t[-1], phi[-1]), xytext=(5, 7 if near0 else 0), textcoords="offset points",
                        va="center", fontsize=8, color=INK_2)
            if phi0 / R < Lw - 1e-9 or phi[-1] < 0:
                tx = phi0 / R
                ax.plot([tx], [0], "o", markerfacecolor="white", markeredgecolor=STATUS["critical"], markersize=6.5,
                        markeredgewidth=1.6, zorder=6)
        ax.set_title(ttl, fontsize=8.6, loc="left")
        ax.set_xlim(0, 7.3)
        ax.set_xticks([0, 1, 2, 3, 4, 5, 6])
        ax.set_ylim(-9, 10.8)
        ax.set_xlabel("Weeks after redemptions start")
        ax.annotate("loan sales\nsettle", (Lw, 10.6), xytext=(3, 0), textcoords="offset points", ha="left", va="top",
                    fontsize=8, color=MUTED)
        ax.text(0.08, -8.2, "shortfall: credit line draws", fontsize=8, color=INK_2, va="center")
    axes[0].set_ylabel("Liquidity sleeve left (% of fund)")
    axes[0].set_yticks([-5, 0, 5, 10])
    # legend for the marker, once
    axes[0].plot([], [], "o", markerfacecolor="white", markeredgecolor=STATUS["critical"], markeredgewidth=1.6,
                 markersize=6.5, linestyle="none", label="sleeve exhausted")
    axes[0].legend(loc="lower right", fontsize=7.8, handletextpad=0.2, borderaxespad=0.4)
    return finish(fig, "ch20_sleeve_runway")


if __name__ == "__main__":
    refresh = "--refresh" in sys.argv
    fig_wrapper_flows()
    fig_arbitrage_band()
    fig_ap_price_impact()
    fig_march2020_tape(refresh)
    fig_sleeve_runway()
