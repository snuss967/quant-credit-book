"""Figures for Chapter 11 (Defensive Systematic High Yield).

Run:  python3 tools/figures/ch11.py   -> assets/figures/ch11_*.png   (five figures, in order of appearance)

Colour roles in this chapter (a role keeps its colour in every figure):
  BLUE   = the object we are studying and trust: the surviving bond, the empirical DD map, the managers, the BB tier
  ORANGE = the adverse side or the comparison: the default jump, the Gaussian trap, the spread given up, the CCC tier
  AQUA   = the B tier (figure 5 only; direct-labelled because aqua is below 3:1 contrast on white)
  NEUTRAL / INK_2 carry reference lines, the diagonal and the index.

Data policy (see style.py):
  Figure 11.1  Illustrative: the mixture return of section 11.1.1 (B-tier inputs stated in the caption).
  Figure 11.2  Source: BlackRock (2025) p.3 capture ratios; the alpha/beta split uses the section 11.2.1 identity with
               the chapter's illustrative regime means (+1.6% up, -2.0% down).
  Figure 11.3  Illustrative: the placeholder DD -> PD map of Listing 11.2 against N(-DD); the DD of the sponsor-levered
               B issuer is recomputed here with the listing's own solver.
  Figure 11.4  Illustrative: the credit-triangle arithmetic of section 11.5.2.
  Figure 11.5  Real: FRED BAMLH0A0HYM2, BAMLH0A1HYBB, BAMLH0A2HYB, BAMLH0A3HYC (ICE BofA indices). FRED carries only a
               rolling three-year window of these series and marks them "internal use only; reproduction prohibited
               without ICE's written permission" (state/research/trend_figure_data_series.md). The raw files are therefore
               fetched on demand into ~/.cache/quant-credit-book/ and are NOT stored in the repository.
"""
import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from style import *  # noqa: E402,F401,F403  (applies the rcParams on import)

import datetime as dt  # noqa: E402
import urllib.request  # noqa: E402

import matplotlib.dates as mdates  # noqa: E402
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402
from matplotlib.patches import FancyArrowPatch  # noqa: E402
from matplotlib.ticker import FuncFormatter  # noqa: E402
from scipy import optimize, stats  # noqa: E402

C_SURVIVE = BLUE
C_JUMP = ORANGE
TINT_BLUE = "#e3eefb"
TINT_GRAY = "#f1f0ed"


def pct_fmt(decimals=0):
    return FuncFormatter(lambda v, _: f"{v:.{decimals}f}%".replace("-", "\u2212"))


# --------------------------------------------------------------------------------------------------------------
# Figure 11.1: the mixture return and the skew of its jump component (section 11.1.1)
# --------------------------------------------------------------------------------------------------------------
def fig_mixture_skew():
    p, m, sd, L = 0.03, 3.26, 4.0, 60.0          # percent units; m = B-tier OAS of 15 Oct 2026 (326bp)
    mean = (1 - p) * m - p * L
    var = (1 - p) * sd ** 2 + p * (1 - p) * (m + L) ** 2
    jump_share = p * (1 - p) * (m + L) ** 2 / var

    fig, (a, b) = new_figure("wide", ncols=2, gridspec_kw={"width_ratios": [1.3, 1]})

    # left: the distribution, probability per one-point bin
    x = np.linspace(-14, 22, 600)
    dens = (1 - p) * stats.norm.pdf(x, m, sd) * 100
    a.fill_between(x, dens, color=C_SURVIVE, alpha=0.22, linewidth=0)
    a.plot(x, dens, color=C_SURVIVE, linewidth=LW)
    a.bar([-L], [p * 100], width=1.0, color=C_JUMP, zorder=3)
    a.axvline(mean, ymax=0.87, color=INK_2, linewidth=0.9, linestyle=(0, (3, 3)), zorder=1)
    a.annotate(f"Mean {mean:+.1f}%", (mean, 10.9), xytext=(-4, 0), textcoords="offset points", ha="right",
               va="center", fontsize=8.5, color=INK_2)
    a.annotate("Survive, 97%:\ncoupon less the\nspread move", (m + 6.2, 6.3), fontsize=8.5, color=INK_2,
               ha="left", va="center")
    a.annotate("Default, 3%:\nlose 60% of price", (-L + 1.4, 5.9), fontsize=8.5, color=INK_2, ha="left",
               va="center")
    a.set_xlim(-68, 24)
    a.set_ylim(0, 12)
    a.set_xticks([-60, -40, -20, 0, 20])
    a.xaxis.set_major_formatter(pct_fmt())
    a.set_xlabel("One-year excess return")
    a.set_ylabel("Probability per 1-point bin (%)")
    note(a, f"Std. dev. {np.sqrt(var):.1f}%; the jump is\n{jump_share:.0%} of the variance", loc="upper left")

    # right: skewness of the Bernoulli jump component against p
    pp = np.logspace(np.log10(0.005), np.log10(0.5), 300)
    sk = -(1 - 2 * pp) / np.sqrt(pp * (1 - pp))
    b.axhline(0, color=NEUTRAL, linewidth=0.9, zorder=1)
    b.plot(pp * 100, sk, color=C_SURVIVE, linewidth=LW)
    for pv, dx, dy, ha in [(0.02, 8, -9, "left"), (0.05, 8, -9, "left"), (0.20, -4, 11, "right")]:
        sv = -(1 - 2 * pv) / np.sqrt(pv * (1 - pv))
        b.plot([pv * 100], [sv], "o", color=C_SURVIVE, markersize=6, zorder=5)
        b.annotate(f"p = {pv:.0%}: {sv:.1f}".replace("-", "−"), (pv * 100, sv), xytext=(dx, dy),
                   textcoords="offset points", fontsize=8.5, color=INK_2, va="center", ha=ha)
    b.set_xscale("log")
    b.set_xlim(0.5, 50)
    b.set_ylim(-15, 1)
    b.set_xticks([0.5, 1, 2, 5, 10, 20, 50])
    b.xaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{v:g}%"))
    b.xaxis.set_minor_formatter(FuncFormatter(lambda v, _: ""))
    b.set_xlabel("Default probability p (log scale)")
    b.set_ylabel("Skewness of the jump")
    b.annotate("Safer bond:\nrarer, more\nskewed jump", (0.62, -3.2), fontsize=8.5, color=INK_2, ha="left", va="center")
    b.annotate("Riskier bond:\njump is the\nbase case", (10, -11.3), fontsize=8.5, color=INK_2, ha="left", va="center")
    return finish(fig, "ch11_mixture_skew")


# --------------------------------------------------------------------------------------------------------------
# Figure 11.2: the capture-ratio plane (section 11.2.1)
# --------------------------------------------------------------------------------------------------------------
def fig_capture_plane():
    up_mean, dn_mean = 1.6, -2.0                 # illustrative regime means, % per month (section 11.2.1)
    k = 100 / up_mean + 100 / abs(dn_mean)       # 112.5, the identity's 1/ubar + 1/|dbar| with means in decimals
    mgrs = [("Average manager", 89.56, 92.24), ("Top-quartile manager", 92.00, 99.00)]

    fig, ax = new_figure("square")
    lo, hi = 85.5, 101.5
    ax.set_xlim(lo, hi)
    ax.set_ylim(lo, hi)
    ax.set_aspect("equal")
    ax.grid(axis="both")
    ax.fill([lo, hi, lo], [lo, hi, hi], color=TINT_BLUE, zorder=0, linewidth=0)
    ax.fill([lo, hi, hi], [lo, lo, hi], color=TINT_GRAY, zorder=0, linewidth=0)
    ax.plot([lo, hi], [lo, hi], color=INK_2, linewidth=1.0, zorder=2)
    ax.text(86.0, 101.0, "Upside capture above downside:\nalpha, the convexity you pay for", fontsize=8.2,
            color=INK_2, va="top", ha="left")
    ax.text(100.8, 87.0, "Gives up more upside\nthan it saves", fontsize=8.2, color=INK_2, va="center", ha="right")
    ax.text(90.6, 88.9, "Pure beta tilt: U = D = \u03b2", fontsize=8.2, color=INK_2, rotation=45, ha="center",
            va="center", rotation_mode="anchor")

    # the dimmer switch: slide down the diagonal from the benchmark (drawn just below the line so it stays visible)
    ax.add_patch(FancyArrowPatch((99.6, 98.4), (96.6, 95.4), arrowstyle="-|>", mutation_scale=10, linewidth=1.3,
                                 color=INK_2, zorder=4, shrinkA=0, shrinkB=0))
    ax.text(98.0, 94.7, "Dimmer switch:\nlower \u03b2", fontsize=8.2, color=INK_2, ha="center", va="top")

    for name, D, U in mgrs:
        alpha_m = (U - D) / 100 / k              # per month, decimal
        beta = U / 100 - alpha_m / (up_mean / 100)
        ax.plot([beta * 100], [beta * 100], "o", markerfacecolor=SURFACE, markeredgecolor=C_SURVIVE,
                markeredgewidth=1.6, markersize=7, zorder=5)
        ax.add_patch(FancyArrowPatch((beta * 100, beta * 100), (D, U), arrowstyle="-|>", mutation_scale=9,
                                     linewidth=1.3, color=C_SURVIVE, zorder=4, shrinkA=4, shrinkB=5))
        ax.plot([D], [U], "o", color=C_SURVIVE, markersize=8, zorder=6)
    ax.text(86.2, 94.2, "Average manager\nD 89.56%, U 92.24%\n\u03b2 \u2248 0.91, \u03b1 \u2248 29bp", fontsize=8.5,
            color=INK_2, ha="left", va="center")
    ax.text(93.5, 99.8, "Top quartile\nD 92.00%, U 99.00%\n\u03b2 \u2248 0.95, \u03b1 \u2248 75bp", fontsize=8.5,
            color=INK_2, ha="left", va="top")
    note(ax, "Hollow dot: same \u03b2 with \u03b1 = 0. Arrow: the alpha.", loc="lower right")
    ax.plot([100], [100], "s", color=INK, markersize=7, zorder=6)
    ax.annotate("Benchmark", (100, 100), xytext=(-7, 5), textcoords="offset points", ha="right", va="bottom",
                fontsize=8.5, color=INK_2)
    ax.set_xlabel("Downside capture (% of the benchmark's loss in down months)")
    ax.set_ylabel("Upside capture (% of the benchmark's gain in up months)")
    ax.xaxis.set_major_formatter(pct_fmt())
    ax.yaxis.set_major_formatter(pct_fmt())
    ax.set_xticks(range(86, 102, 2))
    ax.set_yticks(range(86, 102, 2))
    return finish(fig, "ch11_capture_plane")


# --------------------------------------------------------------------------------------------------------------
# Figure 11.3: the normal-distribution trap, DD -> PD (section 11.3.2)
# --------------------------------------------------------------------------------------------------------------
def _merton_call(V, sigma_V, F, r, T):
    sq = sigma_V * np.sqrt(T)
    d1 = (np.log(V / F) + (r + 0.5 * sigma_V ** 2) * T) / sq
    d2 = d1 - sq
    return V * stats.norm.cdf(d1) - F * np.exp(-r * T) * stats.norm.cdf(d2), d1


def _merton_solve(E, sigma_E, F, r, T=1.0):
    v_hi = E + 2.0 * F * max(1.0, np.exp(-r * T))

    def V_of(sV):
        return optimize.brentq(lambda V: _merton_call(V, sV, F, r, T)[0] - E, E, v_hi, xtol=1e-12, rtol=1e-14)

    def gap(sV):
        V = V_of(sV)
        return sV * V * stats.norm.cdf(_merton_call(V, sV, F, r, T)[1]) - sigma_E * E

    sV = optimize.brentq(gap, 1e-6, sigma_E, xtol=1e-14, rtol=1e-14)
    return V_of(sV), sV


def empirical_pd(dd, a=-0.718, b=0.9718, pd_floor=1e-4, pd_cap=0.35):
    """Listing 11.2's illustrative monotone map: PD(4) ~ 1%, capped at 35%."""
    return np.clip(np.exp(a - b * np.asarray(dd, dtype=float)), pd_floor, pd_cap)


def fig_dd_pd_map():
    # the chapter's sponsor-levered B issuer: E = 2,000, sigma_E = 55%, STD = 600, LTD = 3,000, r = 4%, mu = 6%
    F = 600.0 + 0.5 * 3000.0
    V, sV = _merton_solve(2000.0, 0.55, F, 0.04)
    dd_iss = (np.log(V / F) + (0.06 - 0.5 * sV ** 2)) / sV
    assert abs(dd_iss - 2.44) < 0.01 and abs(float(empirical_pd(dd_iss)) - 0.046) < 0.001
    pd_e_iss, pd_g_iss = float(empirical_pd(dd_iss)), stats.norm.cdf(-dd_iss)

    dd = np.linspace(0, 8, 800)
    gauss = stats.norm.cdf(-dd)
    emp = empirical_pd(dd)

    fig, ax = new_figure("wide")
    ax.axvspan(4, 8, color=TINT_GRAY, zorder=0, linewidth=0)
    ax.text(7.9, 0.55, "Most listed firms have DD > 4\n(Bohn–Stein, p.138)", fontsize=8.5, color=INK_2,
            ha="right", va="center")
    ax.plot(dd, emp, color=C_SURVIVE, linewidth=LW, zorder=3)
    ax.plot(dd, gauss, color=C_JUMP, linewidth=LW, zorder=3)
    ax.set_yscale("log")
    ax.set_ylim(1e-5, 1.0)
    ax.set_xlim(0, 8)
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: (f"{v*100:g}%")))
    ax.yaxis.set_minor_formatter(FuncFormatter(lambda v, _: ""))
    ax.set_xticks(range(0, 9))
    ax.set_xlabel("Distance-to-default, DD (asset standard deviations)")
    ax.set_ylabel("12-month default probability")

    # DD = 4: the 300x gap
    e4, g4 = float(empirical_pd(4.0)), float(stats.norm.cdf(-4.0))
    ax.plot([4, 4], [g4, e4], color=INK_2, linewidth=1.0, zorder=4)
    ax.plot([4], [e4], "o", color=C_SURVIVE, markersize=6, zorder=5)
    ax.plot([4], [g4], "o", color=C_JUMP, markersize=6, zorder=5)
    ax.annotate(f"DD = 4: empirical {e4:.1%}, Gaussian {g4*100:.3f}%\n(about {e4/g4:.0f}\u00d7 apart)", (4, g4),
                xytext=(8, 30), textcoords="offset points", fontsize=8.5, color=INK_2, va="center", ha="left",
                arrowprops=dict(arrowstyle="-", color=NEUTRAL, linewidth=0.8, shrinkA=2, shrinkB=4))

    # the sponsor-levered B issuer
    ax.plot([dd_iss, dd_iss], [pd_g_iss, pd_e_iss], color=INK_2, linewidth=1.0, zorder=4)
    ax.plot([dd_iss], [pd_e_iss], "o", color=C_SURVIVE, markersize=6, zorder=5)
    ax.plot([dd_iss], [pd_g_iss], "o", color=C_JUMP, markersize=6, zorder=5)
    ax.annotate(f"Sponsor-levered B issuer,\nDD {dd_iss:.2f}: empirical {pd_e_iss:.1%},\nGaussian {pd_g_iss:.2%}",
                (dd_iss, pd_g_iss), xytext=(-12, -38), textcoords="offset points", fontsize=8.5,
                color=INK_2, va="center", ha="right",
                arrowprops=dict(arrowstyle="-", color=NEUTRAL, linewidth=0.8, shrinkA=2, shrinkB=4))

    label_end(ax, 4.5, float(empirical_pd(4.5)), "Empirical map (Listing 11.2):\nPD = exp(\u22120.718 \u2212 0.9718 DD), cap 35%", C_SURVIVE, dx=6, dy=15)
    label_end(ax, 1.5, float(stats.norm.cdf(-1.5)), "Gaussian N(\u2212DD)", C_JUMP, dx=-8, dy=-12, ha="right")
    return finish(fig, "ch11_dd_pd_map")


# --------------------------------------------------------------------------------------------------------------
# Figure 11.4: the same 77% hit rate, two exclusion fractions (section 11.5.2)
# --------------------------------------------------------------------------------------------------------------
def fig_exclusion_pays():
    h, pi, L = 0.77, 3.0, 0.60                   # hit rate, universe default rate (%), loss given default

    def excess_default_loss(q):
        pi_x = h * pi / q
        pi_k = (1 - h) * pi / (1 - q)
        return (pi_x - pi_k) * L

    q = np.linspace(0.13, 0.55, 300)
    cases = [(0.20, 4.20), (0.40, 3.00)]         # (exclusion fraction, excess spread of the flagged set, %)

    fig, ax = new_figure("wide")
    ax.plot(q * 100, excess_default_loss(q), color=C_SURVIVE, linewidth=LW, zorder=3,
            label="Default loss avoided, (π$_X$ − π$_K$)L")
    for qc, s in cases:
        loss = excess_default_loss(qc)
        active_bp = qc * (loss - s) * 100
        ax.plot([qc * 100, qc * 100], [s, loss], color=INK_2, linewidth=1.0, zorder=4)
        ax.plot([qc * 100], [loss], "o", color=C_SURVIVE, markersize=6, zorder=5)
        ax.plot([qc * 100], [s], "D", color=C_JUMP, markersize=6, zorder=5)
        sign = "+" if active_bp > 0 else "\u2212"
        txt = (f"Flag {qc:.0%}: avoid {loss:.1f}%,\ngive up {s:.1f}% of spread\n"
               f"= {sign}{abs(active_bp):.0f}bp a year")
        if qc < 0.3:
            ax.annotate(txt, (qc * 100, s), xytext=(-8, -30), textcoords="offset points", fontsize=8.5, color=INK_2,
                        va="center", ha="right",
                        arrowprops=dict(arrowstyle="-", color=NEUTRAL, linewidth=0.8, shrinkA=2, shrinkB=4))
        else:
            ax.annotate(txt, (qc * 100, loss), xytext=(14, 52), textcoords="offset points", fontsize=8.5,
                        color=INK_2, va="center", ha="left",
                        arrowprops=dict(arrowstyle="-", color=NEUTRAL, linewidth=0.8, shrinkA=2, shrinkB=4))
    ax.plot([], [], "D", color=C_JUMP, markersize=6, linestyle="none",
            label="Excess spread, s$_X$ − s$_K$ (inputs)")
    ax.set_xlim(8, 56)
    ax.set_ylim(0, 10)
    ax.xaxis.set_major_formatter(pct_fmt())
    ax.yaxis.set_major_formatter(pct_fmt())
    ax.set_xlabel("Share of the index flagged and excluded, q")
    ax.set_ylabel("Per year, flagged set minus kept set")
    ax.legend(loc="upper right")
    note(ax, "Hit rate 77%, universe default rate 3%, L = 0.6", loc="lower left")
    return finish(fig, "ch11_exclusion_pays")


# --------------------------------------------------------------------------------------------------------------
# Figure 11.5: the bow tie and the necktie, ICE BofA tier spreads from FRED (section 11.6.2)
# --------------------------------------------------------------------------------------------------------------
FRED_URL = "https://fred.stlouisfed.org/graph/fredgraph.csv?id={}"
CACHE = os.path.join(os.path.expanduser("~"), ".cache", "quant-credit-book")


def fred(series):
    os.makedirs(CACHE, exist_ok=True)
    path = os.path.join(CACHE, f"{series}.csv")
    if not os.path.exists(path):
        with urllib.request.urlopen(FRED_URL.format(series), timeout=60) as r, open(path, "wb") as f:
            f.write(r.read())
    s = pd.read_csv(path, parse_dates=["observation_date"], index_col=0).iloc[:, 0]
    return pd.to_numeric(s, errors="coerce").dropna()


def fig_tier_oas():
    ids = {"HY": "BAMLH0A0HYM2", "BB": "BAMLH0A1HYBB", "B": "BAMLH0A2HYB", "CCC": "BAMLH0A3HYC"}
    df = pd.concat({k: fred(v) for k, v in ids.items()}, axis=1).dropna() * 100.0      # basis points
    last = df.iloc[-1]
    assert df.index[-1] == pd.Timestamp("2026-10-15")
    assert (round(last.HY), round(last.BB), round(last.B), round(last.CCC)) == (323, 197, 326, 1278)
    me = df.resample("ME").last()
    ratio = me.CCC / me.HY
    chk = {"2025-01": 2.61, "2025-04": 2.54, "2025-12": 3.15, "2026-06": 3.53, "2026-08": 3.96, "2026-10": 3.96}
    for k, v in chk.items():
        assert abs(ratio[k].iloc[0] - v) < 0.006, (k, ratio[k].iloc[0], v)

    fig, (a, b) = new_figure("wide", ncols=2, gridspec_kw={"width_ratios": [1.55, 1]})
    fig.get_layout_engine().set(wspace=0.09)

    # left: daily OAS by tier
    a.plot(df.index, df.HY, color=NEUTRAL, linewidth=2.8, zorder=2)
    a.plot(df.index, df.CCC, color=ORANGE, linewidth=LW, zorder=3)
    a.plot(df.index, df.B, color=AQUA, linewidth=1.1, zorder=4)
    a.plot(df.index, df.BB, color=BLUE, linewidth=LW, zorder=3)
    x_end = df.index[-1]
    a.set_xlim(df.index[0], x_end + pd.Timedelta(days=210))
    a.set_ylim(0, 1450)
    label_end(a, x_end, last.CCC, f"CCC & lower\n{last.CCC:,.0f}bp", ORANGE, dx=6)
    label_end(a, x_end, last.B, f"B {last.B:,.0f}bp\nindex {last.HY:,.0f}bp", AQUA, dx=6, dy=9)
    label_end(a, x_end, last.BB, f"BB {last.BB:,.0f}bp", BLUE, dx=6, dy=-4)
    mark_event(a, pd.Timestamp("2025-04-07"), "Tariff shock\n7 Apr 2025", y_frac=0.43)
    a.set_xticks([pd.Timestamp(f"{y}-01-01") for y in (2024, 2025, 2026)])
    a.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    a.set_ylabel("Option-adjusted spread (bp)")
    a.set_xlabel("Daily, 17 Oct 2023 to 15 Oct 2026")
    a.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{v:,.0f}"))

    # right: month-end ratio of the CCC tier to the index
    b.plot(ratio.index, ratio.values, color=ORANGE, linewidth=LW)
    pts = [("2025-01", "2.61", (2, 16)), ("2025-04", "2.54", (4, -12)), ("2025-12", "3.15", (-4, 10)),
           ("2026-06", "3.53", (-12, 6)), ("2026-10", "3.96", (-4, 11))]
    for key, lab, off in pts:
        t = ratio[key].index[0]
        b.plot([t], [ratio[key].iloc[0]], "o", color=ORANGE, markersize=5.5, zorder=5)
        b.annotate(lab, (t, ratio[key].iloc[0]), xytext=off, textcoords="offset points", fontsize=8.5, color=INK_2,
                   ha="center", va="center")
    b.set_ylim(2.0, 4.4)
    b.set_xlim(ratio.index[0] - pd.Timedelta(days=20), ratio.index[-1] + pd.Timedelta(days=40))
    b.xaxis.set_major_locator(mdates.YearLocator())
    b.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    b.set_ylabel("CCC & lower OAS ÷ index OAS")
    b.set_xlabel("Month-end")
    return finish(fig, "ch11_tier_oas")


if __name__ == "__main__":
    fig_mixture_skew()
    fig_capture_plane()
    fig_dd_pd_map()
    fig_exclusion_pays()
    fig_tier_oas()
