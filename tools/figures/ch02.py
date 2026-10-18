"""Figures for Chapter 2 (The Revolutions in Credit Trading).

Run:  python3 tools/figures/ch02.py   -> assets/figures/ch02_*.png   (five figures)

Colour roles, held fixed across the chapter's figures (identity is also carried by direct labels):
  BLUE   = US investment grade (Figures 2.1, 2.2 and the Baa spread of 2.5)
  ORANGE = US high yield (Figures 2.1, 2.2)
  SEQ_BLUE shades = the anchoring share phi (Figure 2.3; darker = more anchored); NEUTRAL = independent dealers
  VIOLET = the old cost level, 12 bp; GREEN = the cheaper plumbing, 7.5 bp (Figure 2.4)
  RED    = ROBO's constant-growth line (Figure 2.2 only)
  Aqua, yellow and magenta are not used (below 3:1 contrast on white).

Data.
  Real:  FRED BAA10Y (Moody's Baa yield less 10-year Treasury, daily), fetched from
         https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAA10Y and cached for the two windows used in
         tools/figures/data/ch02_BAA10Y.csv; the dated events of Figure 2.5 and the Greenwich e-share readings of
         Figure 2.2, each as the chapter sources them (Trend Watch table in 2.3; 2.7.1; 2.9.3) and as
         state/research/trend_figure_data_series.md has them (Greenwich 2025: IG just under 50%, HY 32%, The DESK
         30 Jan 2026; iShares LQD premium/discount on 8 Apr 2025: -0.22%).
  Illustrative (recomputed here from the formulas and inputs stated in the chapter): the Pareto tails implied by Ben Dor's
         imputed limits (2.2.2), the logistic fits (2.3.1 derivation), n_eff and the expected best quote (2.3.2
         derivation) and the data-exhaust curves (2.9.2 derivation).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402
import matplotlib.dates as mdates  # noqa: E402
from matplotlib.ticker import FuncFormatter  # noqa: E402

from style import *  # noqa: E402,F401,F403  (applies the rcParams on import)

plt.rcParams["text.parse_math"] = False      # "$" is always a dollar sign in these figures

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")

IG, HY = BLUE, ORANGE
OLD_COST, NEW_COST = VIOLET, GREEN
LEADER = dict(arrowstyle="-", color=NEUTRAL, linewidth=0.8, shrinkA=1, shrinkB=3)


def matplotlib_fixed(days):
    from matplotlib.ticker import FixedLocator
    return FixedLocator([mdates.date2num(pd.Timestamp(x)) for x in days])


def pct(x, _pos=None):
    return f"{100 * x:.0f}%"


# --------------------------------------------------------------------------------------------------
# Figure 2.1: what 5MM+ and 1MM+ hide (illustrative: Pareto tails implied by Ben Dor's imputed limits)
# --------------------------------------------------------------------------------------------------
def fig_trace_censoring_pareto():
    fig, axs = new_figure("wide", ncols=2, sharey=True)
    specs = [(axs[0], "Investment grade", IG, 5.0, 12.5, "5MM+", [5, 10, 20, 30, 40]),
             (axs[1], "High yield", HY, 1.0, 4.0, "1MM+", [1, 2, 4, 6, 8])]
    for ax, name, col, cap, m, tag, ticks in specs:
        alpha = m / (m - cap)                                    # the tail index implied by the imputed mean
        x = np.linspace(cap, 8 * cap, 500)
        surv = (x / cap) ** (-alpha)                             # Pr(X > x | X > cap)
        ax.fill_between(x, surv, color=col, alpha=0.16, linewidth=0, zorder=2)
        ax.plot(x, surv, color=col, linewidth=LW, zorder=3)
        s_mean = (m / cap) ** (-alpha)
        # the cap: every size from here up prints as the cap
        ax.plot([cap], [1.0], "o", color=col, markersize=5.5, zorder=5, clip_on=False)
        ax.annotate(f"every size from here up\nprints as {tag}", (cap, 1.0), xytext=(0.20, 0.90),
                    textcoords="axes fraction", ha="left", va="top", fontsize=8.2, color=INK_2,
                    arrowprops=dict(arrowstyle="-", color=NEUTRAL, linewidth=0.8, shrinkA=1, shrinkB=4))
        # the mean of the hidden blocks
        ax.plot([m, m], [0, s_mean], color=col, linewidth=0.9, linestyle=(0, (3, 3)), zorder=3)
        ax.plot([m], [s_mean], "o", color=col, markersize=5.5, zorder=5)
        ax.annotate(f"mean of the hidden blocks:\n${m:g}mm = {m / cap:g} × the cap;\n"
                    f"{100 * s_mean:.0f}% of capped prints\nare larger than that",
                    (m, s_mean), xytext=(0.42, 0.50), textcoords="axes fraction", ha="left", va="center",
                    fontsize=8.2, color=INK_2,
                    arrowprops=dict(arrowstyle="-", color=NEUTRAL, linewidth=0.8, shrinkA=1, shrinkB=4))
        ax.set_xlim(cap, 8 * cap)
        ax.set_ylim(0, 1.05)
        ax.set_xticks(ticks)
        ax.set_title(f"{name}: tail index α = {alpha:.2f}")
        ax.set_xlabel("True trade size ($mm)")
        ax.yaxis.set_major_formatter(FuncFormatter(pct))
    axs[0].set_ylabel("Share of capped prints larger")
    return finish(fig, "ch02_trace_censoring_pareto")


# --------------------------------------------------------------------------------------------------
# Figure 2.2: the ceiling is not identified (Greenwich readings; logistic fits per the 2.3.1 derivation)
# --------------------------------------------------------------------------------------------------
def logit_fit(t1, e1, t2, e2, K):
    z = lambda e: np.log(e / (K - e))                            # generalized logit, linear in time
    r = (z(e2) - z(e1)) / (t2 - t1)
    t0 = t1 - z(e1) / r
    return r, t0


def logistic(t, K, r, t0):
    return K / (1.0 + np.exp(-r * (t - t0)))


def fig_adoption_ceiling():
    # (year, share, kind): "num" = a number the Trend Watch table states, "chart" = a chart reading
    obs = {
        "IG": [(2015, .20, "num"), (2021, .34, "chart"), (2022, .41, "chart"), (2023, .45, "num"),
               (2024, .48, "num"), (2025, .48, "num")],
        "HY": [(2015, .06, "num"), (2021, .25, "chart"), (2022, .31, "chart"), (2023, .33, "num"),
               (2024, .33, "num"), (2025, .32, "num")],
    }
    # the chapter's checks (2.3.1 derivation): K = 1 and K = 0.8 projections to 2030
    chk = {}
    for seg in ("IG", "HY"):
        for K in (1.0, 0.8):
            r, t0 = logit_fit(2015, obs[seg][0][1], 2025, obs[seg][-1][1], K)
            chk[(seg, K)] = (r, t0, logistic(2030, K, r, t0))
    assert abs(chk[("IG", 1.0)][0] - 0.131) < 5e-4 and abs(chk[("IG", 1.0)][2] - 0.64) < 0.005
    assert abs(chk[("HY", 1.0)][0] - 0.200) < 5e-4 and abs(chk[("HY", 1.0)][2] - 0.56) < 0.005
    assert abs(chk[("IG", 0.8)][0] - 0.150) < 5e-4 and abs(chk[("IG", 0.8)][2] - 0.61) < 0.005
    assert abs(chk[("HY", 0.8)][0] - 0.211) < 5e-4 and abs(chk[("HY", 0.8)][2] - 0.53) < 0.005
    robo = lambda t: 0.33 * (0.33 / 0.06) ** ((t - 2024) / 9.0)
    assert abs(robo(2030) - 1.03) < 0.005

    fig, axs = new_figure("wide", ncols=2, sharey=True)
    t = np.linspace(2012, 2040, 400)
    for ax, seg, name, col in ((axs[0], "IG", "US investment grade", IG), (axs[1], "HY", "US high yield", HY)):
        ax.axhline(1.0, color=NEUTRAL, linewidth=0.9, zorder=1)
        ax.text(2012.3, 1.015, "all trading = 100%", fontsize=8, color=INK_2, ha="left", va="bottom")
        ax.axhline(0.8, color=NEUTRAL, linewidth=0.8, linestyle=(0, (3, 3)), zorder=1)
        ax.text(2012.3, 0.815, "ceiling if K = 0.8", fontsize=8, color=INK_2, ha="left", va="bottom")
        ax.axvline(2030, color=NEUTRAL, linewidth=0.8, linestyle=(0, (3, 3)), zorder=1)
        ax.text(2029.7, 0.03, "2030", fontsize=8, color=INK_2, ha="right", va="bottom")
        for K, ls in ((1.0, "-"), (0.8, (0, (5, 2.5)))):
            r, t0, _ = chk[(seg, K)]
            ax.plot(t, logistic(t, K, r, t0), color=col, linewidth=LW, linestyle=ls, zorder=3)
        # the observations
        for yr, e, kind in obs[seg]:
            anchor = yr in (2015, 2025)
            ax.plot([yr], [e], "o", markersize=6.5 if anchor else 5, zorder=6, clip_on=False,
                    markerfacecolor="white" if kind == "chart" else col,
                    markeredgecolor=INK if anchor else col, markeredgewidth=1.2 if anchor else 1.0)
        # direct labels for the two ceilings, set on the curves around 2036
        for K, dy, txt in ((1.0, 10, "K = 1"), (0.8, -11, "K = 0.8")):
            r, t0, _ = chk[(seg, K)]
            y = logistic(2036.5, K, r, t0)
            ax.plot([2036.5], [y], "o", color=col, markersize=4, zorder=5)
            ax.annotate(txt, (2036.5, y), xytext=(0, dy), textcoords="offset points", ha="center",
                        va="bottom" if dy > 0 else "top", fontsize=8.5, color=INK_2)
        ax.set_xlim(2012, 2040)
        ax.set_ylim(0, 1.24)
        ax.set_yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
        ax.set_xticks([2015, 2020, 2025, 2030, 2035, 2040])
        ax.set_title(name)
        ax.yaxis.set_major_formatter(FuncFormatter(pct))
        r1, r8 = chk[(seg, 1.0)][2], chk[(seg, 0.8)][2]
        ax.text(0.99, 0.10, f"in 2030: {100 * r1:.0f}% if K = 1,\n{100 * r8:.0f}% if K = 0.8", transform=ax.transAxes,
                ha="right", va="bottom", fontsize=8.2, color=INK_2)
        ax.set_xlabel("Year")
    axs[0].set_ylabel("Electronic share of notional")
    # ROBO's constant-growth rule, high yield only
    ax = axs[1]
    tr = np.linspace(2024, 2030, 60)
    ax.plot(tr, robo(tr), color=RED, linewidth=LW, linestyle=(0, (1.5, 2)), zorder=4)
    ax.plot([2030], [robo(2030)], "o", color=RED, markersize=5.5, zorder=6)
    ax.annotate("ROBO's constant growth:\n103% in 2030", (2030, robo(2030)), xytext=(-8, 9),
                textcoords="offset points", ha="right", va="bottom", fontsize=8.2, color=INK_2)
    # note on the fitted points
    axs[0].annotate("ringed: the 2015 and\n2025 points that pin\nboth curves", (2015, .20), xytext=(2012.8, 0.60),
                    textcoords="data", ha="left", va="center", fontsize=8.2, color=INK_2, arrowprops=LEADER)
    axs[1].annotate("hollow: chart readings", (2021, .25), xytext=(2013.2, 0.46), textcoords="data",
                    ha="left", va="center", fontsize=8.2, color=INK_2, arrowprops=LEADER)
    return finish(fig, "ch02_adoption_ceiling")


# --------------------------------------------------------------------------------------------------
# Figure 2.3: eleven anchored dealers are worth about two (illustrative; 2.3.2 derivation)
# --------------------------------------------------------------------------------------------------
def fig_rfq_neff():
    neff = lambda n, phi: n / (1.0 + (n - 1.0) * phi)
    best = lambda n, phi: phi + (1.0 - phi) / n                    # E[best quote] / theta
    assert abs(neff(11, 0.45) - 2.0) < 1e-12
    shade = {0.10: SEQ_BLUE(0.50), 0.25: SEQ_BLUE(0.75), 0.45: SEQ_BLUE(1.0)}

    fig, axs = new_figure("wide", ncols=2)
    axl, axr = axs
    n = np.linspace(1, 20, 191)

    # left: effective number of independent dealers
    axl.plot(n, neff(n, 0.0), color=NEUTRAL, linewidth=LW, linestyle=(0, (4, 3)), zorder=2)
    axl.text(12.4, 11.3, "independent dealers:\nn_eff = n", ha="left", va="center", fontsize=8.2, color=INK_2)
    for phi, col in shade.items():
        axl.plot(n, neff(n, phi), color=col, linewidth=LW, zorder=3)
        axl.plot([0.5, 20], [1 / phi, 1 / phi], color=col, linewidth=0.8, linestyle=(0, (1.5, 2.5)), zorder=1)
        label_end(axl, 20, neff(20, phi), f"φ = {phi:g}", col, dx=5)
    axl.text(1.0, 10.15, "ceiling 1/φ = 10", fontsize=8, color=INK_2, ha="left", va="bottom")
    axl.text(12.5, 4.15, "ceiling 1/φ = 4", fontsize=8, color=INK_2, ha="left", va="bottom")
    axl.text(12.5, 2.35, "ceiling 1/φ = 2.2", fontsize=8, color=INK_2, ha="left", va="bottom")
    axl.plot([11], [2.0], "o", color=shade[0.45], markersize=6.5, zorder=6, markeredgecolor=INK, markeredgewidth=1.0)
    axl.annotate("Theo's 11 responders at\nφ = 0.45 are worth 2", (11, 2.0), xytext=(6.3, 0.62),
                 textcoords="data", ha="left", va="center", fontsize=8.2, color=INK_2, arrowprops=LEADER)
    axl.set_xlim(0.5, 24.5)
    axl.set_ylim(0, 12.2)
    axl.set_xticks([1, 5, 10, 15, 20])
    axl.set_xlabel("Dealers responding, n")
    axl.set_ylabel("Effective number of independent dealers")

    # right: how far the best quote sits from fair, as a share of theta, and 9 April 2025
    n_hi, n_lo = 13.2, 6.6
    for phi, col, ls in ((0.0, NEUTRAL, (0, (4, 3))), (0.45, shade[0.45], "-")):
        axr.plot(n, best(n, phi), color=col, linewidth=LW, linestyle=ls, zorder=3)
        for nn in (n_hi, n_lo):
            axr.plot([nn], [best(nn, phi)], "o", color=col if phi else INK_2, markersize=5.5, zorder=6,
                     markeredgecolor=INK_2 if phi == 0 else INK, markeredgewidth=0.8)
    up0, up45 = best(n_lo, 0) / best(n_hi, 0), best(n_lo, 0.45) / best(n_hi, 0.45)
    assert abs(up0 - 2.0) < 1e-9 and abs(up45 - 1.085) < 0.001
    axr.text(10.4, 0.30, f"independent: halving the\nresponders doubles the best\nquote's distance (×{up0:.1f}, θ fixed)",
             ha="left", va="center", fontsize=8.2, color=INK_2)
    axr.text(8.5, 0.68, f"φ = 0.45: it moves {100 * (up45 - 1):.0f}%\n(θ and φ held fixed)",
             ha="left", va="center", fontsize=8.2, color=INK_2)
    axr.text(7.0, 0.93, "dots: 13.2 and 6.6 prices per RFQ\n(US high grade, 9 Apr 2025)", ha="left", va="center",
             fontsize=8.2, color=INK_2)
    axr.set_xlim(0.5, 20)
    axr.set_ylim(0, 1.05)
    axr.set_xticks([1, 5, 10, 15, 20])
    axr.set_xlabel("Dealers responding, n")
    axr.set_ylabel("Expected best quote ÷ θ")
    return finish(fig, "ch02_rfq_neff")


# --------------------------------------------------------------------------------------------------
# Figure 2.4: the same signal on cheaper plumbing (illustrative; 2.9.2 derivation, Man's 12 -> 7.5 bp)
# --------------------------------------------------------------------------------------------------
def fig_data_exhaust_curve():
    k = 0.0048
    x = np.linspace(0.0, 17.0, 600)
    gross = k * np.sqrt(x) * 1e4                                  # bp
    peaks = {}
    for c_bp in (12.0, 7.5):
        c = c_bp * 1e-4
        to_star, a_star = k**2 / (4 * c**2), k**2 / (4 * c) * 1e4
        peaks[c_bp] = (to_star, a_star)
    assert abs(peaks[12.0][0] - 4.0) < 1e-9 and abs(peaks[12.0][1] - 48.0) < 1e-9
    assert abs(peaks[7.5][0] - 10.24) < 1e-9 and abs(peaks[7.5][1] - 76.8) < 1e-9
    assert abs(peaks[7.5][0] / peaks[12.0][0] - 2.56) < 1e-9 and abs(peaks[7.5][1] / peaks[12.0][1] - 1.6) < 1e-9

    fig, ax = new_figure("wide")
    ax.axhline(0, color=INK_2, linewidth=0.9, zorder=2)
    ax.plot(x, gross, color=NEUTRAL, linewidth=LW, zorder=2)
    ax.text(10.6, 160, "gross alpha, k√TO", fontsize=8.2, color=INK_2, ha="left", va="center")
    for c_bp, col in ((12.0, OLD_COST), (7.5, NEW_COST)):
        net = gross - c_bp * x
        ax.plot(x, net, color=col, linewidth=LW, zorder=4)
        to_star, a_star = peaks[c_bp]
        ax.plot([to_star, to_star], [0, a_star], color=col, linewidth=0.9, linestyle=(0, (3, 3)), zorder=3)
        ax.plot([to_star], [a_star], "o", color=col, markersize=6.5, zorder=6, markeredgecolor=INK, markeredgewidth=0.8)
    ax.annotate("c = 12 bp: best is 4.0 turns,\n48 bp of net alpha", (4.0, 48.0), xytext=(4.7, 16),
                textcoords="data", ha="left", va="center", fontsize=8.5, color=INK_2, arrowprops=LEADER)
    ax.annotate("c = 7.5 bp: best is 10.2 turns,\n77 bp of net alpha", (10.24, 76.8), xytext=(11.0, 108),
                textcoords="data", ha="left", va="center", fontsize=8.5, color=INK_2, arrowprops=LEADER)
    ax.annotate("", xy=(10.0, 70.5), xytext=(4.25, 51.0),
                arrowprops=dict(arrowstyle="-|>", color=INK_2, linewidth=1.1, mutation_scale=9, shrinkA=0, shrinkB=0))
    ax.text(1.0, 98, "cutting the cost from 12 to 7.5 bp\nmultiplies the best turnover by 2.56\nand the net alpha by 1.6",
            fontsize=8.5, color=INK_2, ha="left", va="center")
    ax.set_xlim(0, 17)
    ax.set_ylim(-14, 175)
    ax.set_xlabel("Turnover (one-way turns of the book per year)")
    ax.set_ylabel("Alpha (bp per year)")
    note(ax, "k = 0.0048", loc="upper left")
    return finish(fig, "ch02_data_exhaust_curve")


# --------------------------------------------------------------------------------------------------
# Figure 2.5: two shocks, five years apart (real: FRED BAA10Y; dated events as sourced in 2.7.1 and 2.9.3)
# --------------------------------------------------------------------------------------------------
def fig_two_shocks_timeline():
    df = pd.read_csv(os.path.join(DATA, "ch02_BAA10Y.csv"), parse_dates=["observation_date"])
    s = df.dropna().set_index("observation_date")["BAA10Y"]
    d = pd.Timestamp
    assert abs(s[d("2020-03-23")] - 4.31) < 1e-9 and abs(s[d("2020-02-20")] - 2.05) < 1e-9
    assert abs(s[d("2025-04-07")] - 2.02) < 1e-9 and abs(s[d("2025-04-02")] - 1.73) < 1e-9
    up20 = round(100 * (s[d("2020-03-23")] - s[d("2020-02-20")]))
    up25 = round(100 * (s[d("2025-04-07")] - s[d("2025-04-02")]))
    assert up20 == 226 and up25 == 29

    ev20 = [("2020-03-12", 4.95, "12 Mar: LQD closes 5.0% below NAV"),
            ("2020-03-23", 4.58, "23 Mar: Fed announces the SMCCF and PMCCF"),
            ("2020-04-09", 4.21, "9 Apr: facilities expanded to up to $850bn with TALF"),
            ("2020-05-12", 3.84, "12 May: first purchases, of ETFs"),
            ("2020-06-16", 3.47, "16 Jun: first purchases of bonds")]
    ev25 = [("2025-04-07", 4.95, "7 Apr: US fixed-income ETFs trade a record $98.9bn at one-cent spreads"),
            ("2025-04-08", 4.58, "8 Apr: $89.7bn of corporates trade, 12% by portfolio trade; LQD 0.22% below NAV"),
            ("2025-04-09", 4.21, "9 Apr: prices per RFQ fall from 13.2 to 6.6; tariff pause that afternoon"),
            ("2025-04-16", 3.84, "within a week: back to 11.3 prices per RFQ"),
            ("2025-04-30", 3.47, "30 Apr: about $92bn record day;\nportfolio trades 22.4% of IG")]

    fig, axs = new_figure((7.0, 6.1), nrows=2, sharey=True)
    for ax, (a, b), events, title, loc, fmt in (
            (axs[0], ("2020-02-18", "2020-07-31"), ev20, "March 2020", mdates.MonthLocator(), "%-d %b"),
            (axs[1], ("2025-03-31", "2025-05-14"), ev25, "April 2025",
             matplotlib_fixed(["2025-04-01", "2025-04-08", "2025-04-15", "2025-04-22", "2025-04-29", "2025-05-06",
                               "2025-05-13"]), "%-d %b")):
        seg = s[(s.index >= a) & (s.index <= b)]
        ax.plot(seg.index, seg.values, color=IG, linewidth=LW, zorder=3)
        ax.set_xlim(d(a), d(b))
        for day, y, txt in events:
            ts = d(day)
            ax.plot([ts, ts], [seg[seg.index <= ts].iloc[-1] + 0.06, y], color=NEUTRAL, linewidth=0.9,
                    linestyle=(0, (3, 3)), zorder=1)
            ax.annotate(txt, (ts, y), xytext=(3, 0), textcoords="offset points", ha="left", va="center",
                        fontsize=8.2, color=INK_2)
        ax.set_title(title)
        ax.xaxis.set_major_locator(loc)
        ax.xaxis.set_major_formatter(mdates.DateFormatter(fmt))
        ax.set_ylabel("Baa less 10-year Treasury (%)")
    axs[0].set_ylim(1.4, 5.2)
    # the spread's own move, marked at its peak
    pk20 = d("2020-03-23")
    axs[0].plot([pk20], [s[pk20]], "o", color=IG, markersize=5.5, zorder=6)
    note(axs[0], f"+{up20} bp from 20 Feb (2.05%) to the 23 Mar peak (4.31%)", loc="lower right")
    pk25 = d("2025-04-07")
    axs[1].plot([pk25], [s[pk25]], "o", color=IG, markersize=5.5, zorder=6)
    note(axs[1], f"+{up25} bp from 2 Apr (1.73%) to the 7 Apr peak (2.02%)", loc="lower right")
    return finish(fig, "ch02_two_shocks_timeline")


if __name__ == "__main__":
    fig_trace_censoring_pareto()
    fig_adoption_ceiling()
    fig_rfq_neff()
    fig_data_exhaust_curve()
    fig_two_shocks_timeline()
