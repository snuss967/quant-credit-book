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
    ticks = [10, 40, 100, 400, 1000]
    tick_labels = ["10", "40", "100", "400", "1,000"]

    lo, hi = 100 * (P - 2 * se), 100 * (P + 2 * se)
    a.fill_between(n, lo, hi, color=BLUE_TINT, linewidth=0)
    a.plot(n, 100 * np.full_like(n, P), color=BLUE, linewidth=LW)
    a.plot(n, lo, color=BLUE, linewidth=0.8)
    a.plot(n, hi, color=BLUE, linewidth=0.8)
    a.axhline(50, color=MUTED, linewidth=0.9, linestyle=(0, (4, 3)), zorder=1)
    a.set_xscale("log")
    a.set_xlim(10, 2000)
    a.set_ylim(25, 85)
    a.text(10.8, 49.2, "coin flip", fontsize=8.5, color=INK_2, ha="left", va="top")
    a.text(55, 55.8, "true hit rate 55%", fontsize=8.5, color=INK_2, ha="left", va="bottom")
    n40 = 40
    se40 = math.sqrt(P * (1 - P) / n40)
    a.plot([n40, n40], [100 * (P - 2 * se40), 100 * (P + 2 * se40)], color=INK_2, linewidth=1.6, solid_capstyle="butt")
    a.plot([n40], [100 * P], "o", color=BLUE, markersize=5)
    a.annotate(f"40 views:\n{100*(P-2*se40):.0f}% to {100*(P+2*se40):.0f}%", (n40, 100 * (P + 2 * se40)),
               xytext=(6, 2), textcoords="offset points", fontsize=8.5, color=INK_2, va="bottom")
    n_x = 4 * P * (1 - P) / 0.05 ** 2                       # 2 SE = 5 points -> about 396 views
    a.plot([n_x], [50], "o", color=INK, markersize=5, zorder=5)
    a.annotate(f"band clears 50%\nat about {n_x:.0f} views", (n_x, 50), xytext=(-6, -34), textcoords="offset points",
               ha="center", fontsize=8.5, color=INK_2, arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.7))
    a.set_xlabel("Logged views (log scale)")
    a.set_ylabel("Measured hit rate (%), band = $\\pm$2 SE")
    a.set_xticks(ticks)
    a.set_xticklabels(tick_labels)
    a.minorticks_off()

    b.plot(n, 100 * se, color=BLUE, linewidth=LW)
    b.plot(n, 200 * se, color=BLUE, linewidth=LW, linestyle=(0, (4, 3)))
    b.axhline(5, color=ORANGE, linewidth=1.3)
    b.set_xscale("log")
    b.set_xlim(10, 2000)
    b.set_ylim(0, 18)
    b.text(10.5, 4.6, "the edge: 5 points", ha="left", va="top", fontsize=8.5, color=INK_2)
    b.annotate("2 SE", (40, 200 * se40), xytext=(7, 0), textcoords="offset points", fontsize=8.5, color=INK_2,
               va="center")
    b.plot([40], [200 * se40], "o", color=BLUE, markersize=4, zorder=5)
    b.annotate("1 SE", (13, 100 * math.sqrt(P * (1 - P) / 13)), xytext=(7, 4), textcoords="offset points",
               fontsize=8.5, color=INK_2)
    b.plot([n_x], [5], "o", color=INK, markersize=5, zorder=5)
    b.annotate(f"2 SE meets the edge\nat about {n_x:.0f} views", (n_x, 5), xytext=(10, 14), textcoords="offset points",
               fontsize=8.5, color=INK_2, arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.7))
    b.plot([40], [100 * se40], "o", color=BLUE, markersize=5, zorder=5)
    b.annotate(f"40 views:\n{100*se40:.1f} points", (40, 100 * se40), xytext=(-8, -16), textcoords="offset points",
               ha="right", va="center", fontsize=8.5, color=INK_2)
    se400 = 100 * math.sqrt(P * (1 - P) / 400)
    b.plot([400], [se400], "o", color=BLUE, markersize=5, zorder=5)
    b.annotate(f"400 views: {se400:.1f} points", (400, se400), xytext=(-8, -12), textcoords="offset points",
               ha="right", fontsize=8.5, color=INK_2)
    b.set_xlabel("Logged views (log scale)")
    b.set_ylabel("Standard error of the hit rate (points)")
    b.set_xticks(ticks)
    b.set_xticklabels(tick_labels)
    b.minorticks_off()
    return finish(fig, "ch03b_hit_rate_se")


# --------------------------------------------------------------------------------------------------
# Figure 3-B.7 (3B.6 mistake 2): hedge to jump-to-default, not to face
# --------------------------------------------------------------------------------------------------
def fig_jtd_hedge():
    FACE = 10.0
    fig, (a, b) = new_figure(ncols=2)
    P = np.linspace(30, 100, 281)
    for R in (30, 50):                                           # the family: thin lines, unlabelled, named in the note
        x = P[P >= R]
        a.plot(x, FACE * (x - R) / (100 - R), color=SEQ_BLUE(0.35), linewidth=1.0)
    x = P[P >= 40]
    a.plot(x, FACE * (x - 40) / 60.0, color=BLUE, linewidth=LW)
    a.axhline(FACE, color=ORANGE, linewidth=1.4)
    a.text(31, FACE + 0.25, "face hedge: ten matches ten", fontsize=8.5, color=INK_2, va="bottom")
    # the extra bet Theo holds at 88 and at 70 (recovery 40)
    for price in (88, 70):
        j = FACE * (price - 40) / 60.0
        a.plot([price, price], [j, FACE], color=ORANGE, linewidth=3.0, solid_capstyle="butt", alpha=0.55)
        a.plot([price], [j], "o", color=BLUE, markersize=6, zorder=5)
    a.annotate("at 88: $8.0mm\nleaves $2.0mm\nof extra bet", (88, 8.0), xytext=(99, 3.3), ha="right", va="center",
               fontsize=8.5, color=INK_2, arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.7))
    a.annotate("at 70: $5.0mm\nleaves $5.0mm\nof extra bet", (70, 5.0), xytext=(62, 7.9), ha="right", va="center",
               fontsize=8.5, color=INK_2, arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.7))
    a.set_xlim(30, 100)
    a.set_ylim(0, 11.5)
    a.set_xlabel("Bond price (% of par)")
    a.set_ylabel("Protection that leaves the book\nflat on default ($mm)")
    note(a, "thick: recovery R = 40\nthin: R = 30 and 50", loc="lower right")

    pnl = FACE * (1 - P / 100.0)
    b.plot(P, pnl, color=ORANGE, linewidth=LW)
    b.set_xlim(30, 100)
    b.set_ylim(0, 8)
    for price in (88, 70):
        v = FACE * (1 - price / 100.0)
        b.plot([price], [v], "o", color=ORANGE, markersize=6, zorder=5)
        b.annotate(f"at {price}: ${v:.1f}mm", (price, v), xytext=(8, 8), textcoords="offset points", fontsize=8.5,
                   color=INK_2, ha="left" if price == 70 else "right")
    b.set_xlabel("Bond price (% of par)")
    b.set_ylabel("Face-hedged book's P&L if the\nissuer defaults tomorrow ($mm)")
    note(b, "any recovery: the discount to par is the bet", loc="upper right")
    return finish(fig, "ch03b_jtd_hedge")


# --------------------------------------------------------------------------------------------------
# Figure 3-B.6 (3B.5): the wall is a dated interval
# --------------------------------------------------------------------------------------------------
def fig_wall_interval():
    MU, H, DEAL_DAY, LIFT_DAY = 1 / 20.0, 30.0, 19, 20
    fig = plt.figure(figsize=(7.0, 4.9), layout="constrained")
    gs = fig.add_gridspec(2, 1, height_ratios=[1.0, 2.3])
    top = fig.add_subplot(gs[0])
    bot = fig.add_subplot(gs[1], sharex=top)

    # top: Brambleworth's wall as the chapter tells it
    top.set_ylim(0, 1.3)
    top.set_yticks([])
    top.grid(False)
    top.spines["left"].set_visible(False)
    top.spines["bottom"].set_visible(False)
    top.tick_params(labelbottom=False, bottom=False)
    top.add_patch(Rectangle((0, 0.28), LIFT_DAY, 0.30, fc=BLUE_TINT, ec=BLUE, linewidth=1.2, zorder=3))
    top.text(LIFT_DAY / 2, 0.43, "restricted: every Brambleworth RFQ auto-declined", ha="center", va="center", fontsize=8.2,
             color=INK, zorder=4)
    top.plot([0, 0], [0.18, 0.98], color=INK_2, linewidth=0.9, zorder=2)
    top.text(0.4, 1.0, "Day 0, Thursday 10:14: on the restricted list", ha="left", va="bottom", fontsize=8.2, color=INK_2)
    top.plot([LIFT_DAY, LIFT_DAY], [0.18, 0.68], color=INK_2, linewidth=0.9, zorder=4)
    top.text(LIFT_DAY + 0.7, 0.43, "Day 19: deal\nDay 20, 7:05: 8-K filed\n7:40: restriction lifted", ha="left",
             va="center", fontsize=8.2, color=INK_2, linespacing=1.25)
    top.plot([H, H], [0.18, 0.98], color=VIOLET, linewidth=1.3, linestyle=(0, (3, 2)), zorder=2)
    top.text(H + 0.0, 1.0, "NDA outside date,\nday 30", ha="center", va="bottom", fontsize=8.2, color=INK_2)
    top.set_xlim(-1.0, 33.5)
    top.set_ylim(0, 1.55)

    # bottom: the chance the name is still restricted, and why its area is the expected length
    t = np.linspace(0, H, 301)
    S = np.exp(-MU * t)
    bot.fill_between(t, 0, S * 100, color=BLUE_TINT, linewidth=0)
    bot.plot(t, S * 100, color=BLUE, linewidth=LW)
    s_cliff = math.exp(-MU * H) * 100
    bot.plot([H, H], [s_cliff, 0], color=VIOLET, linewidth=1.6)
    bot.plot([H], [s_cliff], "o", color=BLUE, markersize=5, zorder=5)
    expected = (1 - math.exp(-MU * H)) / MU
    bot.text(2.0, 12, f"shaded area = expected restriction = {expected:.1f} days", fontsize=8.5, color=INK_2, ha="left",
             va="center")
    s20 = math.exp(-MU * LIFT_DAY) * 100
    bot.plot([LIFT_DAY], [s20], "o", color=INK, markersize=5, zorder=5)
    bot.annotate("Brambleworth: restriction\nlifted on day 20", (LIFT_DAY, s20), xytext=(LIFT_DAY - 0.4, 78),
                 textcoords="data", ha="right", va="center", fontsize=8.5, color=INK_2,
                 arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.7, shrinkA=2))
    bot.annotate(f"{s_cliff:.0f}% of the time no deal comes:\nthe outside date ends it", (H, s_cliff),
                 xytext=(H - 0.8, 47), textcoords="data", ha="right", va="center", fontsize=8.5, color=INK_2,
                 arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.7, shrinkA=2))
    bot.set_ylim(0, 108)
    bot.set_yticks([0, 25, 50, 75, 100])
    bot.set_xlabel("Days since the wall-cross")
    bot.set_ylabel("Chance the name is still\nrestricted (%)")
    note(bot, "model: deal after an exponential wait, mean 20 days; outside date at day 30", loc="upper right")
    return finish(fig, "ch03b_wall_interval")


# --------------------------------------------------------------------------------------------------
# Figure 3-B.4 (3B.4): contract clocks as event windows x_k(t), and the intensity they imply
# --------------------------------------------------------------------------------------------------
def fig_event_windows():
    import matplotlib.dates as mdates
    L = load_listing()
    add_bd, grace_end = L["add_business_days"], L["grace_end"]
    D = dt.date
    missed = D(2026, 11, 13)                                  # the chapter's Halvorsen date (Friday)
    grace_raw, _ = grace_end(missed)                          # Sunday 13 Dec 2026 (the listing also returns the rolled date)
    day28 = missed + dt.timedelta(days=28)                    # Friday 11 Dec 2026: RSA and petition (12B.9)
    consent = D(2026, 11, 5)                                  # the last version of the consent deadline
    assert grace_raw == D(2026, 12, 13) and day28 == D(2026, 12, 11)
    W = 10                                                    # business days before the event for the pre-event windows
    rows = [("Consent deadline", add_bd(consent, -W, "SIFMA"), consent, 0.4, "5 Nov"),
            ("Coupon due", add_bd(missed, -W, "SIFMA"), missed, 0.6, "13 Nov"),
            ("Grace period", missed, grace_raw, 1.2, "13 Dec"),
            ("RSA milestone", add_bd(day28, -W, "SIFMA"), day28, 0.8, "11 Dec")]
    LAM0 = 4.0                                                # percent a year, the chapter's 4% example
    days = [D(2026, 10, 1) + dt.timedelta(days=i) for i in range((day28 - D(2026, 10, 1)).days + 1)]
    lam = np.array([LAM0 * math.exp(sum(beta for _, s0, t1, beta, _ in rows if s0 <= d0 <= t1)) for d0 in days])

    fig = plt.figure(figsize=(7.0, 4.6), layout="constrained")
    gs = fig.add_gridspec(2, 1, height_ratios=[1.0, 1.25])
    top = fig.add_subplot(gs[0])
    bot = fig.add_subplot(gs[1], sharex=top)

    num = mdates.date2num
    top.set_ylim(-0.7, len(rows) - 0.3)
    top.invert_yaxis()
    top.grid(False)
    top.set_yticks(range(len(rows)))
    top.set_yticklabels([r[0] for r in rows])
    top.tick_params(axis="y", length=0, labelsize=8.5)
    top.tick_params(labelbottom=False)
    top.spines["left"].set_visible(False)
    for i, (name, s0, t1, beta, lab) in enumerate(rows):
        top.add_patch(Rectangle((num(s0), i - 0.28), num(t1) - num(s0), 0.56, fc=VIOLET_TINT, ec=VIOLET, linewidth=1.0,
                                zorder=3))
        top.plot([num(t1)], [i], "D", color=VIOLET, markersize=5.5, zorder=5)
        top.annotate(f"$\\times${math.exp(beta):.1f}  (due {lab})", (num(t1), i), xytext=(8, 0), textcoords="offset points",
                     va="center", fontsize=8.2, color=INK_2)
    top.set_xlim(num(D(2026, 10, 1)), num(D(2026, 12, 30)))

    bot.step([num(x) for x in days], lam, where="post", color=BLUE, linewidth=LW)
    bot.axhline(LAM0, color=MUTED, linewidth=0.9, linestyle=(0, (4, 3)), zorder=1)
    bot.set_ylim(0, 38)
    bot.text(num(D(2026, 10, 2)), LAM0 - 0.7, "baseline $\\lambda_0$ = 4% a year", fontsize=8.5, color=INK_2, va="top")
    bot.axvline(num(day28), color=RED, linewidth=1.1, linestyle=(0, (3, 2)))
    bot.annotate("day 28: RSA signed,\npetition filed", (num(day28), 36), xytext=(6, 0), textcoords="offset points", va="top",
                 fontsize=8.2, color=INK_2)
    both = LAM0 * math.exp(1.2 + 0.8)
    bot.annotate(f"grace + RSA windows open:\n$4\\% \\times e^{{2.0}}$ = {both:.1f}% a year", (num(day28), both),
                 xytext=(-4, 7), textcoords="offset points", ha="right", va="bottom", fontsize=8.5, color=INK_2)
    g = LAM0 * math.exp(1.2)
    bot.annotate(f"grace alone: {g:.1f}%", (num(D(2026, 11, 22)), g), xytext=(0, -4), textcoords="offset points",
                 ha="center", va="top", fontsize=8.5, color=INK_2)
    bot.annotate(f"consent + coupon\nwindows: {LAM0*math.exp(1.0):.1f}%", (num(D(2026, 11, 2)), LAM0 * math.exp(1.0)),
                 xytext=(-4, 6), textcoords="offset points", ha="center", va="bottom", fontsize=8.5, color=INK_2)
    spike = LAM0 * math.exp(0.6 + 1.2)
    bot.annotate("13 Nov: coupon missed", (num(D(2026, 11, 13)), spike), xytext=(-5, 0), textcoords="offset points",
                 ha="right", va="center", fontsize=8.5, color=INK_2)
    bot.xaxis.set_major_locator(mdates.WeekdayLocator(byweekday=0, interval=2))
    bot.xaxis.set_major_formatter(mdates.DateFormatter("%-d %b"))
    bot.set_xlabel("2026")
    bot.set_ylabel("Default intensity $\\lambda^P$\n(% a year)")
    return finish(fig, "ch03b_event_windows")


# --------------------------------------------------------------------------------------------------
# Figure 3-B.5 (3B.4 case study): Saks Global seen from the calendar
# --------------------------------------------------------------------------------------------------
def fig_saks_calendar():
    import matplotlib.dates as mdates
    D = dt.date
    num = mdates.date2num
    fig = plt.figure(figsize=(7.0, 5.1), layout="constrained")
    gs = fig.add_gridspec(2, 1, height_ratios=[1.45, 1.0])
    top = fig.add_subplot(gs[0])
    bot = fig.add_subplot(gs[1])

    def stem(ax, d, y, color, marker, text, dy, ha="center", dx=0, size=6.5, y0=None, fs=8.0):
        ax.plot([num(d), num(d)], [y if y0 is None else y0, y + dy * 0.0], color=color, linewidth=0.0)
        ax.plot([num(d)], [y], marker, color=color, markersize=size, zorder=5, markeredgewidth=0)
        ax.annotate(text, (num(d), y), xytext=(dx, dy), textcoords="offset points", ha=ha, va="bottom" if dy > 0 else "top",
                    fontsize=fs, color=INK_2, linespacing=1.2,
                    arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.6, shrinkA=0, shrinkB=3))

    # ---- top: the whole life of the 11% 2029 notes
    lanes = {"Contract clocks": 2, "Events and prices": 1, "Processes": 0}
    top.set_ylim(-0.75, 2.9)
    top.grid(False)
    top.set_yticks(list(lanes.values()))
    top.set_yticklabels(list(lanes.keys()))
    top.tick_params(axis="y", length=0, labelsize=8.5)
    top.spines["left"].set_visible(False)
    top.set_xlim(num(D(2024, 11, 20)), num(D(2026, 7, 25)))
    for y in lanes.values():
        top.axhline(y, color=GRID, linewidth=0.8, zorder=0)

    # processes
    top.add_patch(Rectangle((num(D(2025, 7, 21)), -0.17), num(D(2025, 8, 8)) - num(D(2025, 7, 21)), 0.34, fc=BLUE_TINT, ec=BLUE,
                            linewidth=1.0, zorder=3))
    top.annotate("exchange offer\n21 Jul to 8 Aug 2025", (num(D(2025, 7, 30)), -0.17), xytext=(0, -5), textcoords="offset points",
                 ha="center", va="top", fontsize=8.0, color=INK_2, linespacing=1.2)
    top.add_patch(Rectangle((num(D(2026, 1, 13)), -0.17), num(D(2026, 6, 26)) - num(D(2026, 1, 13)), 0.34, fc=BLUE_TINT, ec=BLUE,
                            linewidth=1.0, zorder=3))
    top.annotate("Chapter 11, 13 Jan to 26 Jun 2026:\nRSA 2 Apr, plan 5 Jun, exit 26 Jun",
                 (num(D(2026, 4, 1)), -0.17), xytext=(0, -5), textcoords="offset points", ha="center", va="top", fontsize=8.0,
                 color=INK_2, linespacing=1.2)
    for d0 in (D(2026, 4, 2), D(2026, 6, 5)):
        top.plot([num(d0)], [0], "|", color=BLUE, markersize=9, markeredgewidth=1.4, zorder=5)
    # events and prices
    stem(top, D(2024, 12, 23), 1, BLUE, "o", "23 Dec 2024: Neiman Marcus closes;\n$2.2bn 11% 2029 notes issued", 15, ha="left", dx=-6)
    stem(top, D(2025, 5, 16), 1, BLUE, "o", "16 May 2025: notes quoted at 47.5\n(144 days after issue)", -14, ha="center", dx=-8)
    top.plot([num(D(2026, 1, 13))], [1], "o", color=RED, markersize=6.5, zorder=5, markeredgewidth=0)
    top.annotate("13 Jan 2026:\npetition", (num(D(2026, 1, 25)), 1), xytext=(0, 0), textcoords="offset points", ha="left",
                 va="center", fontsize=8.0, color=INK_2, linespacing=1.2)
    # contract clocks
    stem(top, D(2025, 6, 30), 2, VIOLET, "D", "end-June 2025: first coupon,\nabout $121mm", 12, ha="center", dx=-24)
    top.plot([num(D(2025, 12, 1)), num(D(2025, 12, 16))], [2, 2], "D", color=VIOLET, markersize=6.0, zorder=5, markeredgewidth=0)
    top.annotate("ABL minimum-availability\nsteps, 1 and 16 Dec 2025", (num(D(2026, 1, 25)), 2), xytext=(0, 0),
                 textcoords="offset points", ha="left", va="center", fontsize=8.0, color=INK_2, linespacing=1.2)
    # zoom window outline
    z0, z1 = D(2025, 11, 24), D(2026, 1, 20)
    top.add_patch(Rectangle((num(z0), 0.62), num(z1) - num(z0), 1.62, fc="none", ec=NEUTRAL, linewidth=0.9, linestyle=(0, (3, 2)),
                            zorder=2))
    top.xaxis.set_major_locator(mdates.MonthLocator(bymonth=[1, 4, 7, 10]))
    top.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
    top.tick_params(axis="x", labelsize=8)

    # ---- bottom: the collapse, December 2025 to January 2026
    bot.set_xlim(num(z0), num(z1))
    bot.set_ylim(0.05, 2.9)
    bot.grid(False)
    bot.set_yticks([2, 1])
    bot.set_yticklabels(["Contract clocks", "Events"])
    bot.tick_params(axis="y", length=0, labelsize=8.5)
    bot.spines["left"].set_visible(False)
    for y in (2, 1):
        bot.axhline(y, color=GRID, linewidth=0.8, zorder=0)
    bot.plot([num(D(2025, 12, 1))], [2], "D", color=VIOLET, markersize=6.5, zorder=5, markeredgewidth=0)
    bot.annotate("1 Dec: availability minimum\n\\$200mm to \\$375mm", (num(D(2025, 12, 1)), 2), xytext=(-4, 12), textcoords="offset points",
                 ha="center", va="bottom", fontsize=8.0, color=INK_2, linespacing=1.2,
                 arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.6, shrinkA=0, shrinkB=3))
    bot.plot([num(D(2025, 12, 16))], [2], "D", color=VIOLET, markersize=6.5, zorder=5, markeredgewidth=0)
    bot.annotate("16 Dec: to $500mm", (num(D(2025, 12, 16)), 2), xytext=(20, 12), textcoords="offset points",
                 ha="center", va="bottom", fontsize=8.0, color=INK_2, linespacing=1.2,
                 arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.6, shrinkA=0, shrinkB=3))
    bot.add_patch(Rectangle((num(D(2025, 12, 1)), 0.82), 31, 0.36, fc=ORANGE_TINT, ec=RED, linewidth=1.0, zorder=3))
    bot.annotate("December: about $126mm of\ninterest unpaid (date: see indenture)", (num(D(2025, 12, 16)), 0.82), xytext=(0, -5),
                 textcoords="offset points", ha="center", va="top", fontsize=8.0, color=INK_2, linespacing=1.2)
    bot.plot([num(D(2026, 1, 7))], [1], "o", color=RED, markersize=6.5, zorder=5, markeredgewidth=0)
    bot.annotate("7 Jan: S&P\nmoves to SD", (num(D(2026, 1, 7)), 1), xytext=(-8, 12), textcoords="offset points",
                 ha="center", va="bottom", fontsize=8.0, color=INK_2, linespacing=1.2,
                 arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.6, shrinkA=0, shrinkB=3))
    bot.plot([num(D(2026, 1, 13))], [1], "o", color=RED, markersize=6.5, zorder=5, markeredgewidth=0)
    bot.annotate("13 Jan:\nChapter 11", (num(D(2026, 1, 13)), 1), xytext=(12, -8), textcoords="offset points",
                 ha="center", va="top", fontsize=8.0, color=INK_2, linespacing=1.2)
    bot.xaxis.set_major_locator(mdates.WeekdayLocator(byweekday=0, interval=2))
    bot.xaxis.set_major_formatter(mdates.DateFormatter("%-d %b"))
    bot.tick_params(axis="x", labelsize=8)
    note(bot, "zoom on the dashed box above", loc="lower right")
    return finish(fig, "ch03b_saks_calendar")


# --------------------------------------------------------------------------------------------------
# Figure 3-B.2 (3B.1): the desk's day as a timeline
# --------------------------------------------------------------------------------------------------
def fig_day_timeline():
    fig, ax = new_figure(size=(7.0, 4.9))
    ax.grid(False)
    ax.spines["left"].set_visible(False)
    X0, X1 = 6.0, 18.6
    ax.set_xlim(X0, X1)
    ax.set_ylim(-0.4, 10.9)
    ax.set_yticks([])
    ax.set_xticks([6, 8, 10, 12, 14, 16, 18])
    ax.set_xticklabels(["6 a.m.", "8", "10", "12 p.m.", "2", "4", "6"])
    ax.set_xlabel("Time of day (New York)")
    for h in range(7, 19):                                           # faint hour grid
        ax.axvline(h, color=GRID, linewidth=0.6, zorder=0)
    white = dict(boxstyle="square,pad=0.15", fc="white", ec="none")

    def band_label(y, text):
        ax.text(X0 - 0.12, y, text, ha="right", va="center", fontsize=8.5, color=INK_2, clip_on=False)

    # lane 1: scheduled jobs (cron-like), BLUE; labels climb a staircase so none collides
    yj = 7.6
    band_label(yj, "Scheduled jobs")
    jobs = [(6.75, "6:45 feed diff", 64), (7.25, "7:15 explain", 48), (7.5, "7:30 risk pack", 32),
            (8.5, "8:30 pre-open calendar", 16)]
    for h, txt, off in jobs:
        ax.plot([h], [yj], "o", color=BLUE, markersize=6.5, zorder=5, markeredgewidth=0)
        ax.annotate(txt, (h, yj), xytext=(3, off), textcoords="offset points", ha="left", va="center", fontsize=8.3,
                    color=INK_2, arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.6, shrinkA=0, shrinkB=3,
                                                 relpos=(0, 0.5)))

    # lane 2: intraday loops, BLUE tint bars
    loops = [(5.9, "fills loop: order, booking, risk, P&L"),
             (5.1, "hedge loop: DV01 and DTS drift vs. morning hedges"),
             (4.3, "RFQ loop: hit ratio, cover gaps, who we win too often")]
    band_label(5.1, "Intraday loops")
    for y, txt in loops:
        ax.add_patch(Rectangle((9.5, y - 0.32), 6.5, 0.64, fc=BLUE_TINT, ec=BLUE, linewidth=1.0, zorder=3))
        ax.text(9.62, y, txt, ha="left", va="center", fontsize=8.0, color=INK, zorder=4)

    # lane 3: after the close
    yc = 3.1
    band_label(yc, "After the close")
    ax.add_patch(Rectangle((16.0, yc - 0.36), 2.2, 0.72, fc=BLUE_TINT, ec=BLUE, linewidth=1.0, zorder=3))
    ax.text(16.1, yc, "marks, disputes,\nEOD risk", ha="left", va="center", fontsize=7.6, color=INK, zorder=4, linespacing=1.15)

    # lane 4: venue and vendor clocks (approximate), ORANGE
    band_label(1.25, "Venue and\nvendor clocks")
    ax.text(X0 - 0.12, 0.35, "(approximate)", ha="right", va="center", fontsize=7.2, color=MUTED, clip_on=False)
    ax.plot([15.0], [2.0], "s", color=ORANGE, markersize=6.5, zorder=5, markeredgewidth=0)
    ax.annotate("Treasury futures settle,\nabout 3:00", (15.0, 2.0), xytext=(-8, 0), textcoords="offset points", ha="right",
                va="center", fontsize=8.0, color=INK_2, linespacing=1.15, bbox=white)
    ax.plot([16.0], [2.0], "s", color=ORANGE, markersize=6.5, zorder=5, markeredgewidth=0)
    ax.annotate("equities close, 4:00", (16.0, 2.0), xytext=(8, 0), textcoords="offset points", ha="left",
                va="center", fontsize=8.0, color=INK_2, bbox=white)
    ax.add_patch(Rectangle((15.0, 1.0), 2.0, 0.5, fc=ORANGE_TINT, ec=ORANGE, linewidth=1.0, linestyle=(0, (3, 2)), zorder=3))
    ax.text(14.9, 1.25, "evaluated bond prices,\nmid-to-late afternoon", ha="right", va="center", fontsize=8.0, color=INK_2,
            linespacing=1.15, bbox=white)
    ax.add_patch(Rectangle((17.0, 0.1), 1.6, 0.5, fc=ORANGE_TINT, ec=ORANGE, linewidth=1.0, linestyle=(0, (3, 2)), zorder=3))
    ax.text(16.9, 0.35, "CDX end-of-day marks, later still", ha="right", va="center", fontsize=8.0, color=INK_2, bbox=white)

    # the snap: one timestamp
    ax.plot([15.0, 15.0], [-0.1, 6.5], color=INK_2, linewidth=1.1, linestyle=(0, (4, 3)), zorder=2)
    ax.annotate("3:00 p.m. snap:\none timestamp for\nrisk and P&L", (15.0, 6.5), xytext=(5, 20), textcoords="offset points",
                ha="left", va="center", fontsize=8.3, color=INK, fontweight="bold", linespacing=1.15)
    return finish(fig, "ch03b_day_timeline")


# --------------------------------------------------------------------------------------------------
# Figure 3-B.3 (3B.3): the year as four nested clocks, with contract clocks cutting across them
# --------------------------------------------------------------------------------------------------
def fig_year_clocks():
    from matplotlib.lines import Line2D
    from matplotlib.patches import PathPatch
    from matplotlib.path import Path
    fig, ax = plt.subplots(figsize=(7.0, 5.9), layout="constrained")
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_xlim(-6.4, 6.4)
    ax.set_ylim(-5.6, 4.75)
    RING = {"day": (0.95, 1.65), "week": (1.75, 2.45), "month": (2.55, 3.25), "year": (3.35, 4.05)}

    def pol(r, th):                                   # th: degrees clockwise from 12 o'clock
        t = math.radians(th)
        return r * math.sin(t), r * math.cos(t)

    def span(ring, a0, b0, **kw):                     # an arc of a ring between two clockwise angles
        r0, r1 = RING[ring]
        ax.add_patch(Wedge((0, 0), r1, 90 - b0, 90 - a0, width=r1 - r0, **kw))

    def radial(ring, th, f0=0.0, f1=1.0, **kw):
        r0, r1 = RING[ring]
        x0, y0 = pol(r0 + f0 * (r1 - r0), th)
        x1, y1 = pol(r0 + f1 * (r1 - r0), th)
        ax.plot([x0, x1], [y0, y1], **kw)

    def mid(ring, f=0.5):
        r0, r1 = RING[ring]
        return r0 + f * (r1 - r0)

    # ring faces and unit ticks
    for name, (r0, r1) in RING.items():
        ax.add_patch(Wedge((0, 0), r1, 0, 360, width=r1 - r0, fc=TINT, ec=NEUTRAL, linewidth=0.9, zorder=1))
    span("week", 5 * 360 / 7, 360, fc="#ecebe7", ec="none", zorder=1.5)          # the weekend
    for h in range(24):
        radial("day", h * 15, 0.8, 1.0, color=NEUTRAL, linewidth=0.7, zorder=2)
    for d in range(7):
        radial("week", d * 360 / 7, 0, 1, color=NEUTRAL, linewidth=0.7, zorder=2)
    for d, lab in enumerate("MTWTFSS"):
        x, y = pol(mid("week", 0.18), (d + 0.5) * 360 / 7)
        ax.text(x, y, lab, ha="center", va="center", fontsize=7.2, color=MUTED, zorder=3)
    for d in range(31):
        radial("month", d * 360 / 31, 0.86, 1.0, color=NEUTRAL, linewidth=0.6, zorder=2)
    for dom in (1, 8, 15, 22):
        x, y = pol(mid("month", 0.2), (dom - 0.5) * 360 / 31)
        ax.text(x, y, str(dom), ha="center", va="center", fontsize=7.0, color=MUTED, zorder=3)
    for m in range(12):
        radial("year", m * 30, 0, 1, color=NEUTRAL if m % 3 else MUTED, linewidth=0.7 if m % 3 else 1.4, zorder=2)
    for m, lab in enumerate("JFMAMJJASOND"):
        x, y = pol(mid("year", 0.16), (m + 0.5) * 30)
        ax.text(x, y, lab, ha="center", va="center", fontsize=7.2, color=MUTED, zorder=3)

    def dot(ring, th, f, color, marker="o", size=6.0, zorder=6, **kw):
        x, y = pol(mid(ring, f), th)
        ax.plot([x], [y], marker, color=color, markersize=size, zorder=zorder, **{"markeredgewidth": 0, **kw})
        return x, y

    # the desk's own clocks (BLUE)
    span("day", 6.75 * 15, 8.5 * 15, fc=BLUE, ec="none", zorder=4)                           # 6:45 to 8:30
    span("day", 16 * 15, 18 * 15, fc=BLUE, ec="none", zorder=4)                              # 4 to 6 p.m.
    p_jobs = pol(mid("day", 0.5), 114)
    p_marks = pol(mid("day", 0.5), 258)
    p_snap = dot("day", 15 * 15, 0.5, BLUE, size=7.5)
    p_mon = dot("week", 0.42 * 360 / 7, 0.62, BLUE, size=6.5)
    p_fri = dot("week", (4 + 15.5 / 24) * 360 / 7, 0.62, BLUE, size=6.5)
    # someone else's clocks (ORANGE)
    span("month", 27 * 360 / 31, 360, fc=ORANGE, ec="none", zorder=4)                        # month-end
    p_monthend = pol(mid("month", 0.5), (27 + 2) * 360 / 31)
    p_roll_mar = dot("year", 79 / 365 * 360, 0.68, ORANGE, "D", 6.5)
    p_roll_sep = dot("year", 263 / 365 * 360, 0.68, ORANGE, "D", 6.5)
    for doy in (90, 181, 273, 365):                                                          # quarter-ends
        dot("year", doy / 365 * 360, 0.68, SURFACE, "o", 6.5, markeredgecolor=ORANGE, markeredgewidth=1.6)
    p_q = pol(mid("year", 0.68), 90 / 365 * 360)
    fomc = [27.5, 76.5, 118.5, 167.5, 209.5, 255.5, 298.5, 342.5]                           # 2026 meetings' mid-dates, day of year
    for dy in fomc:
        radial("year", dy / 365 * 360, 0.32, 0.48, color=INK_2, linewidth=1.8, zorder=5, solid_capstyle="butt")
    p_fomc = pol(mid("year", 0.40), 118.5 / 365 * 360)

    # callouts
    def callout(point, text, xy, ha):
        ax.annotate(text, point, xytext=xy, textcoords="data", ha=ha, va="center", fontsize=8.0, color=INK_2,
                    linespacing=1.15, arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.6, shrinkA=1, shrinkB=2), zorder=11)

    callout(p_mon, "Monday:\nresearch meeting", (4.5, 3.05), "left")
    callout(p_roll_mar, "20 Mar index roll", (4.5, 1.15), "left")
    callout(p_q, "quarter-ends: BDC marks,\nredemption prints", (4.5, 0.0), "left")
    callout(p_jobs, "6:45 to 8:30: feed diff,\nexplain, risk pack,\ncalendar", (4.5, -1.15), "left")
    callout(p_fomc, "8 FOMC meetings\n(2026)", (4.5, -2.35), "left")
    callout(p_monthend, "month-end: index\nrebalance, true-up,\nfactor review", (-4.5, 2.45), "right")
    callout(p_roll_sep, "20 Sep index roll", (-4.5, -0.15), "right")
    callout(p_marks, "4 to 6 p.m.: marks,\ndisputes, EOD risk", (-4.5, -1.4), "right")
    callout(p_fri, "Friday: markouts", (-4.5, -2.25), "right")
    callout(p_snap, "3:00 snap", (-4.5, -3.0), "right")

    # contract clocks: curved hands that cut across all four rings
    def hand(th, label, side):
        sx, sy = pol(4.7, th)
        cx, cy = pol(2.9, th + 12)
        ex, ey = pol(0.5, th + 80)
        path = Path([(sx, sy), (cx, cy), (ex, ey)], [Path.MOVETO, Path.CURVE3, Path.CURVE3])
        ax.add_patch(PathPatch(path, fc="none", ec=VIOLET, linewidth=2.2, zorder=9, capstyle="round"))
        ax.plot([sx], [sy], "o", color=VIOLET, markersize=5.5, zorder=10, markeredgewidth=0)
        ax.plot([ex], [ey], "D", color=VIOLET, markersize=6.5, zorder=10, markeredgewidth=0)
        lx, ly = pol(5.05, th)
        ax.text(lx, ly, label, ha="right" if side < 0 else "left", va="center", fontsize=8.3, color=INK, linespacing=1.15)

    hand(322, "30-day grace\nperiod", -1)
    hand(38, "consent\ndeadline", 1)
    hand(142, "RSA\nmilestone", 1)
    hand(218, "NDA outside\ndate", -1)

    # key
    ax.text(0, -4.72, "Rings from the centre out: day, week, month, year (with its quarter-ends and half-year rolls).\n"
                      "Each starts at 12 o'clock: midnight, Monday, the 1st, 1 January.", ha="center", va="center",
            fontsize=8.0, color=MUTED, linespacing=1.3)
    handles = [Line2D([], [], marker="o", color=BLUE, linestyle="", markersize=6, label="the desk's own clock"),
               Line2D([], [], marker="D", color=ORANGE, linestyle="", markersize=6, label="someone else's clock"),
               Line2D([], [], color=VIOLET, linewidth=2.2, label="clock with a contract attached")]
    ax.legend(handles=handles, loc="lower center", bbox_to_anchor=(0.5, -0.02), ncols=3, fontsize=8.0, handletextpad=0.4,
              columnspacing=1.6, frameon=False)
    return finish(fig, "ch03b_year_clocks")


FIGURES = [fig_snap_phantom, fig_day_timeline, fig_year_clocks, fig_event_windows, fig_saks_calendar, fig_wall_interval, fig_jtd_hedge,
           fig_hit_rate_se]

if __name__ == "__main__":
    only = set(sys.argv[1:])
    sig, nchg, d0, d1 = dgs10_daily_sigma_bp()
    print(f"DGS10 daily sigma {sig:.2f} bp over {nchg} changes, {d0} to {d1}")
    for f in FIGURES:
        if not only or f.__name__.replace("fig_", "") in only:
            f()
