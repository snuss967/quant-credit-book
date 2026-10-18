"""Figures for Chapter 3-B (Your First Year on the Desk).

Run:  python3 tools/figures/ch03b.py   -> assets/figures/ch03b_*.png   (eight figures)

Colour roles, held fixed across the chapter's figures (identity is always also carried by a direct label):
  BLUE   = the desk's own object: the yield path, the systems that fire, the measured hit rate, lambda^P, the JTD-neutral hedge
  ORANGE = the clock or number that is somebody else's or is wrong: vendor and venue clocks, the phantom P&L, the straight-line
           guess, the face hedge
  VIOLET = a clock with a contract attached (a date written in a document: grace, consent, RSA, NDA outside date, ABL covenant)
  RED    = default and the critical event (missed payment, petition)
  NEUTRAL / MUTED grey = context and reference lines.
Aqua, yellow and magenta are not used (below 3:1 contrast on white).

Data. Real: the daily standard deviation of 10-year Treasury yield changes behind the "6 bp a day" scale of Figure 3-B.1
(FRED DGS10, 15 Oct 2021 to 15 Oct 2026, cached in tools/figures/data/ch03b_DGS10.csv); the 2026 FOMC meeting dates (federalreserve.gov
FOMC calendar); the Saks Global dates (state/research/case_lmt_autopsies_us_2020_2026.md section 8, as the chapter cites it); the
settlement and index-roll dates computed by the chapter's own Listing (desk_calendar.py, executed unchanged below).
Everything else is generated from the model stated in its caption and is labelled Illustrative there.
"""
import csv
import datetime as dt
import math
import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))
import numpy as np  # noqa: E402
from matplotlib.patches import FancyBboxPatch, Rectangle, Wedge  # noqa: E402

from style import *  # noqa: E402,F401,F403  (applies the rcParams on import)
from style import ROOT  # noqa: E402

TINT = "#f5f5f3"        # very light surface for grouping bands (not a data colour)
VIOLET_TINT = "#e8e4f8"
ORANGE_TINT = "#fbe6dc"
BLUE_TINT = "#dbe8f9"


# --------------------------------------------------------------------------------------------------
# The chapter's Listing (desk_calendar.py), executed unchanged so the dates in the figures are the dates the chapter computes.
# --------------------------------------------------------------------------------------------------
def load_listing():
    path = os.path.join(ROOT, "book_src", "03_ch03b_your_first_year_on_the_desk.md")
    txt = open(path, encoding="utf-8").read()
    code = re.search(r"```python\n(.*?)```", txt, re.S).group(1)
    ns = {"__name__": "desk_calendar"}      # not "__main__": the listing's own tests are not rerun here
    exec(compile(code, "desk_calendar.py", "exec"), ns)
    return ns


def dgs10_daily_sigma_bp():
    rows = list(csv.reader(open(os.path.join(ROOT, "tools", "figures", "data", "ch03b_DGS10.csv"))))[1:]
    y = np.array([float(r[1]) for r in rows])
    d = np.diff(y) * 100.0
    return float(d.std(ddof=1)), len(d), rows[0][0], rows[-1][0]


def fmt_hhmm(h):
    hh = int(h)
    mm = int(round((h - hh) * 60))
    return f"{hh}:{mm:02d}"


# --------------------------------------------------------------------------------------------------
# Figure 3-B.1 (3B.1): the snap. Two photographs an hour apart manufacture a P&L nobody earned.
# --------------------------------------------------------------------------------------------------
def fig_snap_phantom():
    DV01, SIG_DAY, MIN_DAY = 22_000.0, 6.0, 390.0          # $ per bp, bp per day, minutes in 9:30-16:00
    fig, (a, b) = new_figure(ncols=2)

    # left: one simulated day of the yield (5-minute steps), conditioned so the last hour falls 4 bp (a rally between the photographs)
    rng = np.random.default_rng(11)
    STEP = 5.0
    nstep = int(MIN_DAY / STEP)
    steps = rng.normal(0.0, SIG_DAY * math.sqrt(STEP / MIN_DAY), nstep)
    k = int(60 / STEP)
    steps[-k:] += (-4.0 - steps[-k:].sum()) / k
    path = np.concatenate([[0.0], np.cumsum(steps)])
    hrs = 9.5 + np.arange(len(path)) * STEP / 60.0
    a.plot(hrs, path, color=BLUE, linewidth=LW)
    i3 = len(path) - 1 - k
    y3, y4 = path[i3], path[-1]
    a.axvspan(15.0, 16.0, color=ORANGE_TINT, zorder=0)
    a.plot([15.0], [y3], "o", color=ORANGE, markersize=6, zorder=5)
    a.plot([16.0], [y4], "o", color=BLUE, markersize=6, zorder=5, clip_on=False)
    a.set_xlim(9.5, 16.25)
    a.set_xticks([10, 12, 14, 16])
    a.set_xticklabels(["10:00", "12:00", "2:00", "4:00"])
    a.set_xlabel("Time of day (New York)")
    a.set_ylabel("10-year yield since yesterday's snap (bp)")
    lo, hi = path.min(), path.max()
    a.set_ylim(lo - 3.4, hi + 2.2)
    lo, hi = a.get_ylim()
    a.annotate("futures marked\n3:00 p.m.", (15.0, y3), xytext=(-14, -44), textcoords="offset points", ha="right",
               fontsize=8, color=INK_2, arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.7))
    a.annotate("bond marked 4:00 p.m.", (16.0, y4), xytext=(0, -20), textcoords="offset points", ha="right",
               fontsize=8, color=INK_2, arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.7))
    a.text(14.9, hi - 0.03 * (hi - lo), "yields fall 4 bp between\nthe marks: phantom +$88,000", ha="right", va="top",
           fontsize=8, color=INK, fontweight="bold")

    # right: typical size of the phantom against the gap between the two photographs
    gap = np.linspace(0, 120, 241)
    sd = DV01 * SIG_DAY * np.sqrt(gap / MIN_DAY) / 1000.0
    lin = DV01 * SIG_DAY * (gap / MIN_DAY) / 1000.0
    b.plot(gap, lin, color=MUTED, linewidth=LW, linestyle=(0, (4, 3)))
    b.plot(gap, sd, color=ORANGE, linewidth=LW)
    g60 = 60
    s60 = DV01 * SIG_DAY * math.sqrt(g60 / MIN_DAY) / 1000.0
    l60 = DV01 * SIG_DAY * (g60 / MIN_DAY) / 1000.0
    b.plot([g60], [s60], "o", color=ORANGE, markersize=6, zorder=5)
    b.plot([g60], [l60], "o", color=MUTED, markersize=5, zorder=5)
    b.annotate(f"one hour: ${s60:.0f}k", (g60, s60), xytext=(-8, 12), textcoords="offset points", ha="right",
               fontsize=8.5, color=INK_2)
    b.annotate(f"straight-line guess: ${l60:.0f}k", (g60, l60), xytext=(8, -10), textcoords="offset points",
               fontsize=8.5, color=INK_2)
    b.set_xlim(0, 120)
    b.set_ylim(0, 85)
    b.set_xlabel("Minutes between the two photographs")
    b.set_ylabel("Typical phantom P&L ($ thousand)")
    b.text(118, 57, "square-root rule", ha="right", va="top", fontsize=8.5, color=INK_2)
    return finish(fig, "ch03b_snap_phantom")


# --------------------------------------------------------------------------------------------------
# Figure 3-B.8 (3B.7): the standard error of a hit rate
# --------------------------------------------------------------------------------------------------
def fig_hit_rate_se():
    P = 0.55
    n = np.logspace(np.log10(10), np.log10(2000), 300)
    se = np.sqrt(P * (1 - P) / n)
    fig, (a, b) = new_figure(ncols=2)

    lo, hi = 100 * (P - 2 * se), 100 * (P + 2 * se)
    a.fill_between(n, lo, hi, color=BLUE_TINT, linewidth=0)
    a.plot(n, 100 * np.full_like(n, P), color=BLUE, linewidth=LW)
    a.plot(n, lo, color=BLUE, linewidth=0.8)
    a.plot(n, hi, color=BLUE, linewidth=0.8)
    a.axhline(50, color=MUTED, linewidth=0.9, linestyle=(0, (4, 3)), zorder=1)
    a.set_xscale("log")
    a.set_xlim(10, 2000)
    a.set_ylim(25, 85)
    a.text(11, 50.8, "coin flip, 50%", fontsize=8.5, color=INK_2, va="bottom")
    a.text(1900, 55.8, "true hit rate 55%", fontsize=8.5, color=INK_2, ha="right", va="bottom")
    n40 = 40
    se40 = math.sqrt(P * (1 - P) / n40)
    a.plot([n40, n40], [100 * (P - 2 * se40), 100 * (P + 2 * se40)], color=INK_2, linewidth=1.6, solid_capstyle="butt")
    a.plot([n40], [100 * P], "o", color=BLUE, markersize=5)
    a.annotate(f"40 views:\n{100*(P-2*se40):.0f}% to {100*(P+2*se40):.0f}%", (n40, 100 * (P + 2 * se40)),
               xytext=(6, 2), textcoords="offset points", fontsize=8.5, color=INK_2, va="bottom")
    n_x = 4 * P * (1 - P) / 0.05 ** 2                       # 2 SE = 5 points -> about 396 views
    a.plot([n_x], [50], "o", color=INK, markersize=5, zorder=5)
    a.annotate(f"band clears 50%\nat about {n_x:.0f} views", (n_x, 50), xytext=(8, -28), textcoords="offset points",
               fontsize=8.5, color=INK_2, arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.7))
    a.set_xlabel("Logged views (log scale)")
    a.set_ylabel("Measured hit rate (%), band = $\\pm$2 SE")
    a.set_xticks([10, 40, 100, 400, 1000, 2000])
    a.set_xticklabels(["10", "40", "100", "400", "1,000", "2,000"])
    a.minorticks_off()

    b.plot(n, 100 * se, color=BLUE, linewidth=LW)
    b.plot(n, 200 * se, color=BLUE, linewidth=LW, linestyle=(0, (4, 3)))
    b.axhline(5, color=ORANGE, linewidth=1.3)
    b.set_xscale("log")
    b.set_xlim(10, 2000)
    b.set_ylim(0, 18)
    b.text(1950, 5.5, "the edge: 5 points", ha="right", va="bottom", fontsize=8.5, color=INK_2)
    b.annotate("2 SE", (14, 200 * math.sqrt(P * (1 - P) / 14)), xytext=(6, 4), textcoords="offset points",
               fontsize=8.5, color=INK_2)
    b.annotate("1 SE", (14, 100 * math.sqrt(P * (1 - P) / 14)), xytext=(6, 4), textcoords="offset points",
               fontsize=8.5, color=INK_2)
    b.plot([n_x], [5], "o", color=INK, markersize=5, zorder=5)
    b.plot([40], [100 * se40], "o", color=BLUE, markersize=5, zorder=5)
    b.annotate(f"40 views: {100*se40:.1f} points", (40, 100 * se40), xytext=(8, -14), textcoords="offset points",
               fontsize=8.5, color=INK_2)
    se400 = 100 * math.sqrt(P * (1 - P) / 400)
    b.plot([400], [se400], "o", color=BLUE, markersize=5, zorder=5)
    b.annotate(f"400 views: {se400:.1f} points", (400, se400), xytext=(-6, -16), textcoords="offset points",
               fontsize=8.5, color=INK_2, ha="center")
    b.set_xlabel("Logged views (log scale)")
    b.set_ylabel("Standard error of the hit rate (points)")
    b.set_xticks([10, 40, 100, 400, 1000, 2000])
    b.set_xticklabels(["10", "40", "100", "400", "1,000", "2,000"])
    b.minorticks_off()
    return finish(fig, "ch03b_hit_rate_se")


# --------------------------------------------------------------------------------------------------
# Figure 3-B.7 (3B.6 mistake 2): hedge to jump-to-default, not to face
# --------------------------------------------------------------------------------------------------
def fig_jtd_hedge():
    FACE = 10.0
    fig, (a, b) = new_figure(ncols=2)
    P = np.linspace(30, 100, 281)
    shades = {30: SEQ_BLUE(0.30), 40: BLUE, 50: SEQ_BLUE(0.90)}
    for R in (30, 40, 50):
        x = P[P >= R]
        y = FACE * (x - R) / (100 - R)
        a.plot(x, y, color=shades[R], linewidth=LW if R == 40 else 1.2)
    a.axhline(FACE, color=ORANGE, linewidth=1.4)
    a.text(31, FACE + 0.25, "face hedge: ten matches ten", fontsize=8.5, color=INK_2, va="bottom")
    # the extra bet Theo holds at 88 and at 70 (recovery 40)
    for price, tag in ((88, "88"), (70, "70")):
        j = FACE * (price - 40) / 60.0
        a.plot([price, price], [j, FACE], color=ORANGE, linewidth=3.0, solid_capstyle="butt", alpha=0.55)
        a.plot([price], [j], "o", color=BLUE, markersize=6, zorder=5)
    a.annotate("at 88: $8.0mm\n(extra bet $2.0mm)", (88, 8.0), xytext=(-10, -34), textcoords="offset points",
               ha="right", fontsize=8.5, color=INK_2, arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.7))
    a.annotate("at 70: $5.0mm\n(extra bet $5.0mm)", (70, 5.0), xytext=(-8, 26), textcoords="offset points",
               ha="right", fontsize=8.5, color=INK_2, arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.7))
    for R, yy, dx in ((30, 7.3, 0), (40, 6.0, 0), (50, 4.5, 0)):
        pass
    a.text(99, 8.25, "R = 30", fontsize=8, color=INK_2, ha="right", va="center")
    a.text(99, 5.7, "R = 50", fontsize=8, color=INK_2, ha="right", va="center")
    a.text(99, 6.95, "R = 40", fontsize=8, color=INK_2, ha="right", va="center", fontweight="bold")
    a.set_xlim(30, 100)
    a.set_ylim(0, 11.5)
    a.set_xlabel("Bond price (% of par)")
    a.set_ylabel("Protection to be flat on default ($mm)")

    pnl = FACE * (1 - P / 100.0)
    b.plot(P, pnl, color=ORANGE, linewidth=LW)
    b.set_xlim(30, 100)
    b.set_ylim(0, 8)
    for price in (88, 70):
        v = FACE * (1 - price / 100.0)
        b.plot([price], [v], "o", color=ORANGE, markersize=6, zorder=5)
        b.annotate(f"at {price}: ${v:.1f}mm", (price, v), xytext=(8, 6), textcoords="offset points", fontsize=8.5,
                   color=INK_2)
    b.set_xlabel("Bond price (% of par)")
    b.set_ylabel("Face-hedged book's P&L if the issuer\ndefaults tomorrow ($mm)")
    return finish(fig, "ch03b_jtd_hedge")


FIGURES = [fig_snap_phantom, fig_hit_rate_se, fig_jtd_hedge]

if __name__ == "__main__":
    only = set(sys.argv[1:])
    sig, nchg, d0, d1 = dgs10_daily_sigma_bp()
    print(f"DGS10 daily sigma {sig:.2f} bp over {nchg} changes, {d0} to {d1}")
    for f in FIGURES:
        if not only or f.__name__.replace("fig_", "") in only:
            f()
