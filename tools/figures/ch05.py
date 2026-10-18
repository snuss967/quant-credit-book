"""Chapter 5 figures: Probability Distributions in Distressed & High-Yield Credit.

Run from anywhere:  python3 tools/figures/ch05.py
Writes assets/figures/ch05_*.png (five figures). The chapter's sixth figure, ch05_pair_two_spikes.png (the Pair Book
beat in 5.1.4), is drawn by the separate script tools/figures/ch05_rv.py and is not touched here.

Data policy (see style.py):
  Fig 1  ch05_skew_vs_pd             Illustrative: the closed-form Bernoulli skeleton of 5.1.3 (no data).
  Fig 2  ch05_two_worlds_mixture     Illustrative: the 5.1.4 mixture, exact densities (survival leg N(7%, 4.1%); default leg
                                     R/0.92 - 1 with R ~ Beta matched to Moody's 40.07% / 27.50%, Schmid p.103); asserts that
                                     every number the 5.1.4 table prints for the mixture is reproduced.
  Fig 3  ch05_recovery_beta_shapes   Method-of-moments Betas of the 5.5.2 table (Moody's 40.07/27.50, Schmid p.103; the
                                     70/30 first-lien book is illustrative; Moody's 2006 family recovery 50.21/26.46 on [0, 1.2]).
  Fig 4  ch05_carvana_stack          Real: Carvana 10-K/10-Q Level 2 fair value over carrying amount, the Bloomberg quote range of
                                     18 Nov 2022, and the per-series exchange ratios computed from the 10-Q (dossier
                                     case_carvana_svb_wolfspeed_capital_structure.md sections 1.2-1.3).
  Fig 5  ch05_serta_recovery_fork    Real: the plan ranges (Norton Rose Fulbright, Q3 2023), the 2020 exchange prices and the
                                     July 2026 remand valuation, with the dates the chapter's Docket Diary and 5.6.2 cite.
Colour roles in this chapter (a role keeps its colour across the figures): BLUE = the survive-or-jump mixture / the main series;
ORANGE = the comparison (Theo's Gaussian; the bond in the chair; the non-participants); NEUTRAL = reference marks.
"""
import datetime as dt
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
import numpy as np  # noqa: E402
from scipy import stats  # noqa: E402

from style import *  # noqa: E402,F401,F403  (applies the rcParams on import)

import matplotlib.dates as mdates  # noqa: E402
from matplotlib.ticker import FixedLocator, FuncFormatter, NullLocator  # noqa: E402

plt.rcParams["text.parse_math"] = False      # "$" is a dollar sign here

NEG_TINT = "#e66767"      # DIVERGING red end, used as a light tint for a loss region
MINUS = "−"


def pct(x, d=1):
    s = f"{abs(x):.{d}f}%"
    return (MINUS + s) if x < 0 else s


# ----------------------------------------------------------------------------------------------------------------
# Figure 1: skew against default probability (5.1.3)
# ----------------------------------------------------------------------------------------------------------------
def skew_skeleton(q):
    return -(1 - 2 * q) / np.sqrt(q * (1 - q))


def fig_skew_vs_pd():
    assert abs(skew_skeleton(0.01) + 9.8) < 0.05          # 5.1.3: "about -9.8" at 1%
    assert abs(skew_skeleton(0.04) + 4.7) < 0.05          # "-4.7" at 4%
    assert abs(skew_skeleton(0.0005) + 45) < 1.0          # "roughly -45" at 0.05%
    assert abs(skew_skeleton(0.12) + 2.34) < 0.01         # Exercise 1 check, CCC
    assert abs(skew_skeleton(0.008) + 11.0) < 0.05        # Exercise 1 check, BB
    assert abs(skew_skeleton(0.77) - 1.3) < 0.05          # 5.2.4: "+1.3" at q = 0.77

    q = np.logspace(np.log10(0.0002), np.log10(0.95), 800)
    fig, ax = new_figure("wide")
    ax.set_xscale("log")
    ax.axhspan(0, 8, color="#f4f3f0", zorder=0)
    ax.axhline(0, color=INK_2, linewidth=0.9, zorder=2)
    ax.plot(q * 100, -1 / np.sqrt(q), color=NEUTRAL, linewidth=1.2, linestyle=(0, (3, 3)), zorder=2)
    ax.plot(q * 100, skew_skeleton(q), color=BLUE, linewidth=2.0, zorder=3)
    ax.axvline(50, color=NEUTRAL, linewidth=0.9, linestyle=(0, (3, 3)), zorder=1)

    pts = [("A", 0.05, (7, -2)), ("BB", 0.8, (7, -3)), ("B3", 4.0, (7, -3)), ("CCC", 12.0, (7, -3))]
    for name, qq, off in pts:
        s = skew_skeleton(qq / 100)
        ax.plot([qq], [s], "o", color=BLUE, markersize=6, zorder=5, markeredgecolor="white", markeredgewidth=0.8)
        ax.annotate(f"{name}, q = {qq:g}%\nskew {pct(s, 1 if abs(s) < 20 else 0)}", (qq, s), xytext=off,
                    textcoords="offset points", va="top", fontsize=8.3, color=INK_2)
    s77 = skew_skeleton(0.77)
    ax.plot([77], [s77], "o", color=ORANGE, markersize=6.5, zorder=5, markeredgecolor="white", markeredgewidth=0.8)
    ax.annotate("Carvana, 2 Jun 2023\nq ≈ 0.77, skew +1.3", (77, s77), xytext=(-9, 11), textcoords="offset points",
                ha="right", va="bottom", fontsize=8.3, color=INK_2)
    ax.annotate("q = ½: skew 0,\nthe sign flips", (50, -47), xytext=(-6, 0), textcoords="offset points",
                ha="right", va="center", fontsize=8.3, color=INK_2)
    ax.text(0.0215, 0.5, "Gaussian: skew 0 at every q", fontsize=8.3, color=INK_2, va="bottom", ha="left")
    ax.text(0.0215, 6.6, "right-skewed: price near recovery", fontsize=8.3, color=MUTED, va="top", ha="left")
    ax.annotate("−1/√q", (0.0215, -1 / np.sqrt(0.000215)), xytext=(6, 0), textcoords="offset points",
                fontsize=8.3, color=MUTED, va="center", ha="left")

    ax.set_xlim(0.02, 95)
    ax.set_ylim(-72, 8)
    ticks = [0.02, 0.05, 0.1, 0.5, 1, 5, 10, 50, 90]
    ax.xaxis.set_major_locator(FixedLocator(ticks))
    ax.xaxis.set_minor_locator(NullLocator())
    ax.xaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{v:g}%"))
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: MINUS + f"{abs(v):g}" if v < 0 else f"{v:g}"))
    ax.set_xlabel("One-year default probability q (log scale)")
    ax.set_ylabel("Skew of the one-year return")
    return finish(fig, "ch05_skew_vs_pd")


# ----------------------------------------------------------------------------------------------------------------
# Figure 2: the two worlds, priced (5.1.4)
# ----------------------------------------------------------------------------------------------------------------
P0, Q_DEF, MU_X, SD_X = 0.92, 0.04, 0.07, 0.041
R_MEAN, R_SD = 0.4007, 0.2750           # Moody's senior unsecured recoveries (Schmid p.103)


def beta_mom(m, s):
    k = m * (1 - m) / s ** 2 - 1
    return m * k, (1 - m) * k


def mixture_cdf(x):
    a, b = beta_mom(R_MEAN, R_SD)
    surv = stats.norm.cdf(x, MU_X, SD_X)
    dflt = stats.beta.cdf(np.clip((np.asarray(x) + 1) * P0, 0, 1), a, b)
    return (1 - Q_DEF) * surv + Q_DEF * dflt


def fig_two_worlds_mixture():
    a, b = beta_mom(R_MEAN, R_SD)
    # Reproduce the 5.1.4 table's mixture column before drawing anything.
    thr = -15 / 92
    assert 28 < 1 / float(mixture_cdf(thr)) < 29.5                      # "1 in 29"
    assert abs(float(mixture_cdf(-0.0224)) - 0.05) < 0.001              # 95% VaR -2.2%
    from scipy.optimize import brentq
    v99 = brentq(lambda x: mixture_cdf(x) - 0.01, -0.999, 0.2)
    assert abs(v99 + 0.83) < 0.005                                      # 99% VaR -83%
    # 99% ES by integration of the quantile function
    grid = np.linspace(0, 0.01, 4001)[1:]
    qs = np.array([brentq(lambda x, p=p: mixture_cdf(x) - p, -0.99999, 0.2) for p in grid[::40]])
    assert abs(qs.mean() + 0.92) < 0.01                                 # 99% ES -92%

    edges = np.arange(-1.0, 0.2001, 0.02)
    centers = (edges[:-1] + edges[1:]) / 2
    mix = np.diff(mixture_cdf(edges))
    gau = np.diff(stats.norm.cdf(edges, MU_X, SD_X))
    gau = np.where(gau < 3e-8, np.nan, gau)
    mix = np.where(mix < 3e-8, np.nan, mix)

    fig, ax = new_figure("wide")
    ax.set_yscale("log")
    ax.axvspan(-100, thr * 100, color=NEG_TINT, alpha=0.10, zorder=0)
    ax.plot(centers * 100, gau, color=ORANGE, linewidth=1.5, linestyle=(0, (4, 2)), zorder=4)
    ax.plot(centers * 100, mix, color=BLUE, linewidth=LW, zorder=3)

    ax.axvline(-2.2, color=NEUTRAL, linewidth=0.9, linestyle=(0, (3, 3)), zorder=1)
    ax.axvline(-83, color=NEUTRAL, linewidth=0.9, linestyle=(0, (3, 3)), zorder=1)
    ax.annotate("95% VaR\n" + MINUS + "2.2%", (-2.2, 1.6e-6), xytext=(-4, 0), textcoords="offset points",
                ha="right", va="bottom", fontsize=8.2, color=INK_2)
    ax.annotate("99% VaR " + MINUS + "83%\n99% ES " + MINUS + "92%", (-83, 1.6e-6), xytext=(4, 0),
                textcoords="offset points", ha="left", va="bottom", fontsize=8.2, color=INK_2)
    ax.annotate("Survival world: 96% of the mass,\nTheo's 4.1% wobble", (7, 0.19), xytext=(46, 6),
                textcoords="offset points", ha="left", va="center", fontsize=8.3, color=INK_2,
                arrowprops=dict(arrowstyle="-", color=MUTED, linewidth=0.8, shrinkA=0, shrinkB=2))
    ax.annotate("Default world: 4% of the mass,\nspread over 100 points of return", (-45, 1.0e-3), xytext=(0, 36),
                textcoords="offset points", ha="center", va="bottom", fontsize=8.3, color=INK_2,
                arrowprops=dict(arrowstyle="-", color=MUTED, linewidth=0.8, shrinkA=0, shrinkB=2))
    ax.text(-98, 0.5, "Lose more than 15 points\n(price below 77)\nmixture: 1 in 29\nGaussian: rarer than 1 in 29,000",
            fontsize=8.3, color=INK_2, ha="left", va="top")
    ax.plot([], [], color=BLUE, linewidth=LW, label="Survive-or-jump mixture")
    ax.plot([], [], color=ORANGE, linewidth=1.5, linestyle=(0, (4, 2)), label="Theo's Gaussian N(7%, 4.1%)")
    ax.legend(loc="upper right", bbox_to_anchor=(1.0, 1.0), fontsize=8.3)

    ax.set_xlim(-100, 20)
    ax.set_ylim(2e-7, 1.2)
    levels = [1e-1, 1e-2, 1e-3, 1e-4, 1e-5, 1e-6]
    ax.yaxis.set_major_locator(FixedLocator(levels))
    ax.yaxis.set_minor_locator(NullLocator())
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: "1 in " + f"{1 / v:,.0f}"))
    ax.xaxis.set_major_formatter(FuncFormatter(lambda v, _: (MINUS if v < 0 else "") + f"{abs(v):g}%"))
    ax.set_xlabel("One-year return on the 92-priced bond")
    ax.set_ylabel("Chance of landing in each\n2-point bin (log scale)")
    return finish(fig, "ch05_two_worlds_mixture")


# ----------------------------------------------------------------------------------------------------------------
# Figure 3: recovery shapes (5.5.2)
# ----------------------------------------------------------------------------------------------------------------
def fig_recovery_beta_shapes():
    a1, b1 = beta_mom(0.4007, 0.2750)
    a2, b2 = beta_mom(0.70, 0.30)
    a3, b3 = beta_mom(0.5021 / 1.2, 0.2646 / 1.2)
    assert abs(a1 - 0.87) < 0.01 and abs(b1 - 1.30) < 0.01
    assert abs(a2 - 0.93) < 0.01 and abs(b2 - 0.40) < 0.01
    assert abs(a3 - 1.68) < 0.01 and abs(b3 - 2.33) < 0.01

    fig, ax = new_figure("wide")
    ymax = 3.6
    r = np.linspace(0.0005, 0.9995, 2000)
    r3 = np.linspace(0.0005, 1.1994, 2000)
    d1 = stats.beta.pdf(r, a1, b1)
    d2 = stats.beta.pdf(r, a2, b2)
    d3 = stats.beta.pdf(r3 / 1.2, a3, b3) / 1.2
    ax.plot(r, np.minimum(d1, ymax * 2), color=BLUE, linewidth=LW, clip_on=True)
    ax.plot(r, np.minimum(d2, ymax * 2), color=ORANGE, linewidth=LW, clip_on=True)
    ax.plot(r3, d3, color=AQUA, linewidth=LW)
    ax.axvline(1.0, color=NEUTRAL, linewidth=0.9, linestyle=(0, (3, 3)), zorder=1)
    ax.set_ylim(0, ymax)
    ax.set_xlim(0, 1.25)

    ax.annotate("Senior unsecured bonds\n(a, b) = (0.87, 1.30): a spike at zero", (0.04, 2.2), xytext=(46, 18),
                textcoords="offset points", ha="left", va="bottom", fontsize=8.3, color=INK_2,
                arrowprops=dict(arrowstyle="-", color=MUTED, linewidth=0.8, shrinkA=0, shrinkB=2))
    ax.plot([0.04], [stats.beta.pdf(0.04, a1, b1)], "o", color=BLUE, markersize=5, zorder=5)
    ax.annotate("First-lien loan book\n(0.93, 0.40): a U, heavy at par", (0.93, stats.beta.pdf(0.93, a2, b2)),
                xytext=(-10, 6), textcoords="offset points", ha="right", va="bottom", fontsize=8.3, color=INK_2)
    ax.plot([0.93], [stats.beta.pdf(0.93, a2, b2)], "o", color=ORANGE, markersize=5, zorder=5)
    label_end(ax, 1.2, d3[-1] if d3[-1] > 0.02 else 0.0, "", AQUA)
    ax.annotate("Moody's family recovery, rescaled\nfrom [0, 1.2]: (1.68, 2.33), an interior hump", (0.42, stats.beta.pdf(0.42 / 1.2, a3, b3) / 1.2),
                xytext=(30, 40), textcoords="offset points", ha="left", va="bottom", fontsize=8.3, color=INK_2,
                arrowprops=dict(arrowstyle="-", color=MUTED, linewidth=0.8, shrinkA=0, shrinkB=2))
    ax.plot([0.42], [stats.beta.pdf(0.42 / 1.2, a3, b3) / 1.2], "o", color=AQUA, markersize=5, zorder=5)
    ax.annotate("density → ∞ at 0", (0.0, ymax), xytext=(4, -9), textcoords="offset points", ha="left",
                va="top", fontsize=8, color=MUTED)
    ax.annotate("density → ∞ at par", (1.0, ymax), xytext=(-4, -9), textcoords="offset points", ha="right",
                va="top", fontsize=8, color=MUTED)
    ax.text(1.005, 0.05, "par", fontsize=8, color=MUTED, ha="left", va="bottom")
    ax.set_xlabel("Recovery (fraction of par)")
    ax.set_ylabel("Probability density")
    return finish(fig, "ch05_recovery_beta_shapes")


# ----------------------------------------------------------------------------------------------------------------
# Figure 4: the Carvana stack, 2022-2023 (5.6.2)
# ----------------------------------------------------------------------------------------------------------------
STACK_MARKS = [(dt.date(2022, 12, 30), 44.8), (dt.date(2023, 3, 31), 53.8), (dt.date(2023, 6, 30), 74.0),
               (dt.date(2023, 9, 29), 77.7), (dt.date(2023, 12, 29), 84.7)]
# New secured par per $1 of old face (10-Q, ratios in the dossier), by old series; the 2025s were bought for cash at 85.
SERIES_RECOVERY = [("2025s\n5.625%", 85.0, "cash"), ("2027s\n5.500%", 76.8, "new"), ("2028s\n5.875%", 66.6, "chair"),
                   ("2029s\n4.875%", 64.9, "new"), ("2030s\n10.250%", 89.3, "new")]


def fig_carvana_stack():
    fig, (a1, a2) = new_figure("wide", ncols=2, gridspec_kw={"width_ratios": [1.6, 1]})
    # Left: marks through time.
    xs = [d for d, _ in STACK_MARKS]
    ys = [v for _, v in STACK_MARKS]
    a1.plot(xs, ys, color=BLUE, linewidth=LW, marker="o", markersize=5.5, zorder=4)
    for d, v in STACK_MARKS:
        a1.annotate(f"{v:g}", (d, v), xytext=(0, 7), textcoords="offset points", ha="center", va="bottom",
                    fontsize=8.3, color=INK_2)
    d18 = dt.date(2022, 11, 18)
    a1.plot([d18, d18], [37, 48], color=NEUTRAL, linewidth=3.2, solid_capstyle="butt", zorder=3)
    a1.annotate("quoted 37–48 on 18 Nov", (d18, 37), xytext=(-2, -9), textcoords="offset points", ha="left",
                va="top", fontsize=8.0, color=MUTED)
    a1.annotate("A year earlier\n(31 Dec 2021): 99.5", (dt.date(2022, 11, 4), 88), ha="left", va="center",
                fontsize=8.3, color=INK_2)
    events = [(dt.date(2023, 3, 22), 128, "22 Mar: exchange offered"),
              (dt.date(2023, 6, 2), 118, "2 Jun: exchange fails (the decision)"),
              (dt.date(2023, 7, 17), 108, "17 Jul: deal signed, over 90%"),
              (dt.date(2023, 9, 1), 98, "1 Sep: settled")]
    for d, h, txt in events:
        a1.plot([d, d], [30, h], color=NEUTRAL, linewidth=0.9, linestyle=(0, (3, 3)), zorder=1)
        a1.annotate(txt, (d, h), xytext=(3, 0), textcoords="offset points", ha="left", va="center", fontsize=8.0,
                    color=INK_2)
    a1.set_ylim(30, 135)
    a1.set_xlim(dt.date(2022, 11, 1), dt.date(2024, 1, 20))
    a1.set_yticks([40, 50, 60, 70, 80, 90, 100])
    a1.xaxis.set_major_locator(FixedLocator(mdates.date2num([d for d, _ in STACK_MARKS])))
    a1.xaxis.set_major_formatter(mdates.DateFormatter("%b %y"))
    a1.set_ylabel("Notes' fair value, % of carrying amount")
    a1.tick_params(axis="x", labelsize=8)

    # Right: what each series received.
    names = [n for n, _, _ in SERIES_RECOVERY]
    vals = [v for _, v, _ in SERIES_RECOVERY]
    cols = [NEUTRAL if k == "cash" else (ORANGE if k == "chair" else BLUE) for _, _, k in SERIES_RECOVERY]
    a2.bar(range(len(vals)), vals, color=cols, width=0.72)
    for i, v in enumerate(vals):
        a2.annotate(f"{v:g}", (i, v), xytext=(0, 3), textcoords="offset points", ha="center", va="bottom",
                    fontsize=8.3, color=INK_2)
    a2.set_xticks(range(len(vals)), names)
    a2.tick_params(axis="x", labelsize=7.8)
    a2.set_ylim(0, 112)
    a2.set_yticks([0, 20, 40, 60, 80, 100])
    a2.set_ylabel("Cents per $1 of old face")
    a2.annotate("bond in the\ncold open's chair", (2, 66.6), xytext=(0, 28), textcoords="offset points", ha="center",
                va="bottom", fontsize=7.8, color=INK_2,
                arrowprops=dict(arrowstyle="-", color=MUTED, linewidth=0.8, shrinkA=0, shrinkB=2))
    a2.annotate("cash tender", (0, 85), xytext=(0, 14), textcoords="offset points", ha="center", va="bottom",
                fontsize=7.8, color=INK_2)
    return finish(fig, "ch05_carvana_stack")


# ----------------------------------------------------------------------------------------------------------------
# Figure 5: Serta, recovery conditioned on a signature (5.6.2)
# ----------------------------------------------------------------------------------------------------------------
def yfrac(d):
    return d.year + (d.timetuple().tm_yday - 1) / 365.25


def fig_serta_recovery_fork():
    fig = plt.figure(figsize=(7.0, 5.6), layout="constrained")
    gs = fig.add_gridspec(2, 1, height_ratios=[1.0, 1.05])
    a1 = fig.add_subplot(gs[0])
    a2 = fig.add_subplot(gs[1])

    # Top: what a first-lien dollar was worth, by signature.
    a1.grid(axis="y", visible=False)
    a1.grid(axis="x", visible=True)
    rows = ["Plan, participants", "Plan, everyone else", "Struck 22 Jun 2020", "Court's value, 7 Jul 2026"]
    ypos = [3, 2, 1, 0]
    a1.barh(3, 100 - 73.7, left=73.7, height=0.46, color=BLUE)
    a1.barh(2, 2.4 - 0.6, left=0.6, height=0.46, color=ORANGE)
    a1.annotate("73.7–100% in the plan", (73.7, 3), xytext=(-6, 0), textcoords="offset points", ha="right",
                va="center", fontsize=8.3, color=INK_2)
    a1.annotate("0.6–2.4% in the plan: a factor of thirty or more below", (2.4, 2), xytext=(6, 0),
                textcoords="offset points", ha="left", va="center", fontsize=8.3, color=INK_2)
    for x, lab, off in [(74, "first-lien paper at 74", (-7, 0)), (39, "second-lien at 39", (-7, 0))]:
        a1.plot([x], [1], "D", color=INK_2, markersize=6, zorder=5, markeredgecolor="white", markeredgewidth=0.8)
        a1.annotate(lab, (x, 1), xytext=off, textcoords="offset points", ha="right", va="center", fontsize=8.3,
                    color=INK_2)
    a1.plot([25], [0], "D", color=INK_2, markersize=6, zorder=5, markeredgecolor="white", markeredgewidth=0.8)
    a1.annotate("excluded loans valued at 25 cents", (25, 0), xytext=(8, 0), textcoords="offset points",
                ha="left", va="center", fontsize=8.3, color=INK_2)
    a1.set_yticks(ypos, rows)
    a1.set_ylim(-0.6, 3.6)
    a1.set_xlim(0, 100)
    a1.set_xlabel("Cents per dollar of first-lien claim")
    a1.tick_params(axis="y", length=0)
    a1.spines["left"].set_visible(False)

    # Bottom: the six-year timeline.
    a2.grid(False)
    for s in ("left",):
        a2.spines[s].set_visible(False)
    a2.set_yticks([])
    a2.spines["bottom"].set_position(("data", 0))
    a2.set_ylim(-3.3, 3.3)
    t0, t1 = 2020.3, 2027.05
    a2.set_xlim(t0, t1)
    ev = [
        (dt.date(2020, 6, 22), "22 Jun 2020\nUptier: $200mm new money,\nabout $875mm second-out", +1.0, "left"),
        (dt.date(2023, 1, 15), "Jan 2023\nChapter 11 filed", -1.0, "center"),
        (dt.date(2023, 3, 28), "28 Mar 2023\nSummary judgment:\n\"open market purchase\"", +1.0, "center"),
        (dt.date(2024, 12, 31), "31 Dec 2024\nFifth Circuit reverses;\nMitel upheld same day", -1.0, "center"),
        (dt.date(2025, 11, 10), "10 Nov 2025\nCertiorari denied", +1.0, "center"),
        (dt.date(2026, 7, 7), "7 Jul 2026, on remand\n$261.13mm plus 9% interest\nfrom 22 Jun 2020", +2.2, "right"),
    ]
    for d, txt, h, ha in ev:
        x = yfrac(d)
        a2.plot([x, x], [0, h * 0.98 if h > 0 else h * 0.98], color=NEUTRAL, linewidth=0.9, zorder=1)
        a2.plot([x], [0], "o", color=BLUE, markersize=6.5, zorder=4, markeredgecolor="white", markeredgewidth=0.8)
        a2.annotate(txt, (x, h), xytext=(0, 3 if h > 0 else -3), textcoords="offset points", ha=ha,
                    va="bottom" if h > 0 else "top", fontsize=8.0, color=INK_2, linespacing=1.25)
    a2.xaxis.set_major_locator(FixedLocator(list(range(2021, 2027))))
    a2.xaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{int(v)}"))
    a2.tick_params(axis="x", pad=2)
    return finish(fig, "ch05_serta_recovery_fork")


def main():
    fig_skew_vs_pd()
    fig_two_worlds_mixture()
    fig_recovery_beta_shapes()
    fig_carvana_stack()
    fig_serta_recovery_fork()


if __name__ == "__main__":
    main()
