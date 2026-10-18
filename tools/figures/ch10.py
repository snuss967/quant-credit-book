"""Chapter 10 figures: Trend-Following & Time-Series Momentum in Credit.

Run from anywhere:  python3 tools/figures/ch10.py
Writes assets/figures/ch10_*.png (five figures, in order of appearance in the chapter):
  10.1 ch10_carry_hurdle         s10.1.2  carry hurdle: formula (illustrative) + real ICE BofA HY OAS, 12-month window
  10.2 ch10_dts_vol_scaling      s10.3.1  DTS law on ICE BofA rating buckets + April 2025 sizing (DTS vs EWMA forecast)
  10.3 ch10_trend_smile          s10.6.1  trend payoff is a smile: conditional payoff curves + simulated outcomes
  10.4 ch10_whipsaw_capture      s10.6.2  the stylized V, two lags, and the capture ratio against V duration
  10.5 ch10_episodes_baa_spread  s10.7    the four case-study episodes on one axis, FRED BAA10Y

Data policy (see style.py):
  10.1 right, 10.2    real data: ICE BofA OAS series via FRED (BAMLH0A0HYM2, BAMLC0A1CAAA, BAMLC0A2CAA, BAMLC0A3CA,
                      BAMLC0A4CBBB, BAMLH0A1HYBB, BAMLH0A2HYB, BAMLH0A3HYC). FRED serves only the last ~3 years of
                      these, and ICE restricts redistribution, so the caches hold only what the figures plot: derived
                      statistics (12-month changes and hurdles, quarterly volatilities, relative notionals), never the
                      raw OAS history. Pass --refresh to rebuild them from FRED (the window will have moved).
  10.5                real data: FRED BAA10Y (Moody's Baa yield less 10-year Treasury), cached from 2007 in
                      tools/figures/data/ch10_BAA10Y.csv.
  10.1 left, 10.3, 10.4  models stated in the chapter (carry hurdle, bivariate-normal payoff, V-shaped round trip);
                      captions say "Illustrative".
"""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from style import *  # noqa: F401,F403,E402  (applies the rcParams on import)

import matplotlib.dates as mdates  # noqa: E402
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402
from matplotlib.lines import Line2D  # noqa: E402
from matplotlib.patches import Patch  # noqa: E402
from scipy.stats import norm  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")
FRED = "https://fred.stlouisfed.org/graph/fredgraph.csv?id={}"
P_HURDLE = os.path.join(DATA, "ch10_hy_hurdle.csv")
P_DTS = os.path.join(DATA, "ch10_dts_law.csv")
P_SIZING = os.path.join(DATA, "ch10_hy_sizing_2025.csv")
P_BAA = os.path.join(DATA, "ch10_BAA10Y.csv")

# Chapter-wide colour roles. A role keeps its colour in every figure of the chapter.
C_SPREAD = BLUE      # anything built from the spread level (spread-change rule, DTS forecast, 3-month signal)
C_RETURN = ORANGE    # anything built from returns (return rule, EWMA forecast, 12-month signal)
C_IG, C_HY, C_CCC = GREEN, VIOLET, RED
TINT_ORANGE = "#fadccd"
TINT_BLUE = "#cde2fb"
D_HY = 4.0           # spread duration used by the chapter's HY examples


# --------------------------------------------------------------------------------------------------------------
# Data: FRED pulls and the derived caches
# --------------------------------------------------------------------------------------------------------------
def fred(series_id):
    """One FRED series as a float Series indexed by date; '.' (missing) is dropped."""
    import io
    import ssl
    import urllib.request
    ca = os.environ.get("SSL_CERT_FILE") or "/root/.ccr/ca-bundle.crt"
    ctx = ssl.create_default_context(cafile=ca) if os.path.exists(ca) else None
    with urllib.request.urlopen(FRED.format(series_id), timeout=90, context=ctx) as r:
        df = pd.read_csv(io.BytesIO(r.read()), index_col=0, parse_dates=True, na_values=".")
    return df.iloc[:, 0].dropna().astype(float)


def build_ice_caches():
    """Rebuild the derived caches of Figures 10.1 and 10.2 from FRED."""
    os.makedirs(DATA, exist_ok=True)
    hy = fred("BAMLH0A0HYM2") * 100.0                      # bp
    # ---- 10.1: 12-month change in OAS against the carry hurdle (252 trading days, D = 4)
    h = 252
    d12 = hy - hy.shift(h)
    hurdle = hy.rolling(h).mean() / D_HY                   # bp: average OAS (bp) * 1 year / D
    out = pd.DataFrame({"d12_bp": d12, "hurdle_bp": hurdle}).dropna()
    out.round(2).to_csv(P_HURDLE, index_label="date")
    # ---- 10.2 left: volatility of daily OAS changes against OAS level, rating bucket x calendar quarter
    ids = {"AAA": "BAMLC0A1CAAA", "AA": "BAMLC0A2CAA", "A": "BAMLC0A3CA", "BBB": "BAMLC0A4CBBB",
           "BB": "BAMLH0A1HYBB", "B": "BAMLH0A2HYB", "CCC": "BAMLH0A3HYC"}
    rows = []
    for name, sid in ids.items():
        s = fred(sid) * 100.0
        for q, g in s.groupby(pd.Grouper(freq="QS")):
            if len(g) < 50:
                continue
            rows.append((name, q.date().isoformat(), round(g.mean(), 2),
                         round(g.diff().dropna().std() * math.sqrt(252), 2), len(g)))
    pd.DataFrame(rows, columns=["bucket", "quarter", "mean_oas_bp", "vol_bp_per_yr", "n_days"]).to_csv(P_DTS, index=False)
    # ---- 10.2 right: notional that holds risk constant through April 2025, relative to 2 April 2025
    s = hy / 1e4
    r = s.shift(1) / 252 - D_HY * s.diff()                 # approximate daily excess return, decimal
    delta = 60 / 61                                        # centre of mass 60 days
    v = (r ** 2).ewm(alpha=1 - delta, adjust=False).mean()
    sig_ewma = np.sqrt(252 * v)
    pre = hy[:"2024-12-31"]                                # beta estimated before the episode: no look-ahead
    b = [(g.mean(), g.diff().dropna().std() * math.sqrt(252)) for _, g in pre.groupby(pd.Grouper(freq="QS")) if len(g) >= 50]
    b = np.array(b)
    beta = float((b[:, 0] * b[:, 1]).sum() / (b[:, 0] ** 2).sum())
    sig_dts = beta * D_HY * s
    w = pd.DataFrame({"dts_notional": 1 / sig_dts, "ewma_notional": 1 / sig_ewma})
    w = (w / w.loc["2025-04-02"]).loc["2025-02-18":"2025-06-30"]
    w.round(4).to_csv(P_SIZING, index_label="date")
    # ---- 10.5: Moody's Baa less 10y Treasury, daily from 2007
    fred("BAA10Y").loc["2007-01-01":].to_csv(P_BAA, index_label="observation_date", header=["BAA10Y"])
    print("rebuilt caches (beta pre-2025 = %.3f)" % beta)


def load(path, **kw):
    return pd.read_csv(path, **kw)


def ensure_caches(refresh=False):
    need = [P_HURDLE, P_DTS, P_SIZING, P_BAA]
    if refresh or not all(os.path.exists(p) for p in need):
        build_ice_caches()


# --------------------------------------------------------------------------------------------------------------
# Figure 10.1: the carry hurdle
# --------------------------------------------------------------------------------------------------------------
def fig_carry_hurdle():
    fig, (a, b) = plt.subplots(1, 2, figsize=(7.0, 3.6), layout="constrained", gridspec_kw={"width_ratios": [1, 1.5]})

    # Left: the hurdle of a 12-month return rule, s_bar / D, for an HY-like and an IG-like book (illustrative)
    sh = np.linspace(2.0, 8.0, 50)
    si = np.linspace(0.4, 2.0, 50)
    a.plot(sh, sh * 100 / 4.0, color=C_HY, linewidth=LW, label="HY-like, D = 4")
    a.plot(si, si * 100 / 7.0, color=C_IG, linewidth=LW, label="IG-like, D = 7")
    a.plot([4.5], [112.5], "o", color=C_HY, markersize=6, zorder=5)
    a.plot([1.0], [100 / 7.0], "o", color=C_IG, markersize=6, zorder=5)
    a.annotate("4.5% spread:\n112.5 bp", (4.5, 112.5), xytext=(-8, 6), textcoords="offset points",
               ha="right", va="bottom", fontsize=8.3, color=INK_2)
    a.annotate("1.0%: 14 bp", (1.0, 100 / 7.0), xytext=(2, 12), textcoords="offset points",
               ha="left", va="bottom", fontsize=8.3, color=INK_2)
    a.set_xlim(0, 8.4)
    a.set_ylim(0, 215)
    a.set_xlabel("Average spread over the window (%)")
    a.set_ylabel("Carry hurdle $\\Delta s^*_{12}$ (bp)")
    a.legend(loc="upper left", fontsize=8.3, handlelength=1.4)

    # Right: real HY OAS, the last two years FRED serves
    h = load(P_HURDLE, parse_dates=["date"])
    x, d12, hur = h["date"].values, h["d12_bp"].values, h["hurdle_bp"].values
    b.axhline(0, color=NEUTRAL, linewidth=0.9, zorder=1)
    # shade the days by regime, from zero up to the curve: a light tint where only the spread rule is short, a
    # darker one where both rules are short (a few days, so a thin sliver above the hurdle line would be invisible)
    b.fill_between(x, 0, d12, where=(d12 > 0) & (d12 <= hur), color=TINT_ORANGE, linewidth=0, zorder=1,
                   interpolate=True)
    b.fill_between(x, 0, d12, where=d12 > hur, color=C_RETURN, alpha=0.55, linewidth=0, zorder=1, interpolate=True)
    b.plot(x, hur, color=C_RETURN, linewidth=1.3, linestyle=(0, (4, 2)), zorder=3)
    b.plot(x, d12, color=C_SPREAD, linewidth=LW, zorder=4)
    n = len(h)
    n_spread = int((d12 > 0).sum())
    n_return = int((d12 > hur).sum())
    print(f"fig 10.1: {n} days, spread rule short {n_spread}, return rule short {n_return}, "
          f"disagree {n_spread - n_return}")
    b.set_ylim(-185, 160)
    b.set_ylabel("Change in HY OAS over 12 months (bp)")
    b.xaxis.set_major_locator(mdates.MonthLocator(bymonth=[1, 7]))
    b.xaxis.set_major_formatter(mdates.DateFormatter("%b\n%Y"))
    handles = [Line2D([0], [0], color=C_SPREAD, linewidth=LW, label="12-month change in OAS"),
               Line2D([0], [0], color=C_RETURN, linewidth=1.3, linestyle=(0, (4, 2)),
                      label="carry hurdle (252-day mean OAS / 4)"),
               Patch(facecolor=TINT_ORANGE, label="spread rule short, return rule long"),
               Patch(facecolor=C_RETURN, alpha=0.55, label="both rules short")]
    fig.legend(handles=handles, loc="outside lower center", ncol=2, fontsize=8, handlelength=1.6, frameon=False)
    return finish(fig, "ch10_carry_hurdle")


# --------------------------------------------------------------------------------------------------------------
# Figure 10.2: volatility scaling is DTS scaling
# --------------------------------------------------------------------------------------------------------------
def fig_dts_vol_scaling():
    fig, (a, b) = plt.subplots(1, 2, figsize=(7.0, 3.6), layout="constrained", gridspec_kw={"width_ratios": [1, 1.05]})

    d = load(P_DTS)
    grp = {"AAA": C_IG, "AA": C_IG, "A": C_IG, "BBB": C_IG, "BB": C_HY, "B": C_HY, "CCC": C_CCC}
    x = d["mean_oas_bp"].values
    y = d["vol_bp_per_yr"].values
    beta = float((x * y).sum() / (x ** 2).sum())
    slope = float(np.polyfit(np.log(x), np.log(y), 1)[0])
    r2 = 1 - float(((y - beta * x) ** 2).sum() / ((y - y.mean()) ** 2).sum())
    print(f"fig 10.2: {len(d)} points, beta through origin {beta:.3f}, log-log slope {slope:.2f}, R2 {r2:.2f}")
    xs = np.array([25.0, 1300.0])
    a.plot(xs, beta * xs, color=INK_2, linewidth=1.1, linestyle=(0, (4, 2)), zorder=1)
    for g, col in grp.items():
        m = (d["bucket"] == g).values
        a.plot(x[m], y[m], "o", color=col, markersize=5.2, alpha=0.9, markeredgewidth=0, zorder=3)
    gap = (d["quarter"] == "2025-04-01").values
    a.plot(x[gap], y[gap], "o", markerfacecolor="none", markeredgecolor=INK, markeredgewidth=1.0, markersize=9, zorder=4)
    a.set_xscale("log")
    a.set_yscale("log")
    a.set_xlim(25, 1300)
    a.set_ylim(8, 520)
    a.set_xticks([30, 100, 300, 1000])
    a.set_xticklabels(["30", "100", "300", "1,000"])
    a.set_yticks([10, 30, 100, 300])
    a.set_yticklabels(["10", "30", "100", "300"])
    a.minorticks_off()
    a.set_xlabel("Average OAS in the quarter (bp, log)")
    a.set_ylabel("Volatility of daily OAS changes (bp a year, log)")
    dot = lambda col: Line2D([0], [0], marker="o", color="none", markerfacecolor=col, markeredgewidth=0, markersize=6)  # noqa: E731
    handles = [dot(C_IG), dot(C_HY), dot(C_CCC),
               Line2D([0], [0], marker="o", color="none", markerfacecolor="none", markeredgecolor=INK, markersize=8),
               Line2D([0], [0], color=INK_2, linewidth=1.1, linestyle=(0, (4, 2)))]
    labels = ["IG: AAA, AA, A, BBB", "HY: BB, B", "CCC", "Q2 2025 (April gap)",
              f"vol = {beta:.2f} × OAS"]
    a.legend(handles, labels, loc="lower right", fontsize=7.8, handlelength=1.3, labelspacing=0.35,
             borderaxespad=0.2)

    # Right: April 2025, the notional that keeps risk constant under two forecasts
    s = load(P_SIZING, parse_dates=["date"])
    t = s["date"].values
    b.axhline(1.0, color=NEUTRAL, linewidth=0.9, zorder=1)
    b.plot(t, s["dts_notional"], color=C_SPREAD, linewidth=LW, zorder=3)
    b.plot(t, s["ewma_notional"], color=C_RETURN, linewidth=LW, zorder=3)
    ev = np.datetime64("2025-04-02")
    mark_event(b, ev, "2 Apr: OAS 3.42%", y_frac=0.97)   # label to the right of the line, in the empty top band
    ev2 = np.datetime64("2025-04-07")
    row7 = s[s["date"] == "2025-04-07"].iloc[0]
    b.plot([ev2], [row7["dts_notional"]], "o", color=C_SPREAD, markersize=5, zorder=5)
    b.annotate(f"7 Apr: DTS {row7['dts_notional']:.2f}", (ev2, row7["dts_notional"]),
               xytext=(8, -16), textcoords="offset points", ha="left", va="top", fontsize=8, color=INK_2)
    t_end = np.datetime64("2025-06-30")
    label_end(b, t_end, s["dts_notional"].iloc[-1], "DTS forecast", C_SPREAD, dx=5)
    label_end(b, t_end, s["ewma_notional"].iloc[-1], "EWMA-60", C_RETURN, dx=5)
    b.set_xlim(t[0], np.datetime64("2025-08-05"))
    b.set_ylim(0.45, 1.55)
    b.xaxis.set_major_locator(mdates.MonthLocator())
    b.xaxis.set_major_formatter(mdates.DateFormatter("%b"))
    b.set_ylabel("Notional for constant risk (2 Apr 2025 = 1.0)")
    b.set_xlabel("2025")
    return finish(fig, "ch10_dts_vol_scaling")


# --------------------------------------------------------------------------------------------------------------
# Figure 10.3: trend is a straddle, and the smile is the receipt for momentum
# --------------------------------------------------------------------------------------------------------------
def smile(z, rho):
    """E[r_TF | r] / sigma_r for r = z sigma_r under the bivariate normal of section 10.6.1."""
    return z * (2 * norm.cdf(rho * z / math.sqrt(1 - rho ** 2)) - 1)


def fig_trend_smile():
    # guard: the closed form against a brute-force simulation (rho = 0.25)
    rng = np.random.default_rng(10)
    rho = 0.25
    big = 2_000_000
    m = rng.standard_normal(big)
    r = rho * m + math.sqrt(1 - rho ** 2) * rng.standard_normal(big)
    tf = np.sign(m) * r
    for z0 in (-2.5, -1.0, 1.0, 2.5):
        sel = np.abs(r - z0) < 0.05
        se = tf[sel].std() / math.sqrt(sel.sum())
        assert abs(tf[sel].mean() - smile(z0, rho)) < 4 * se + 0.01, (z0, tf[sel].mean(), smile(z0, rho))

    fig, (a, b) = plt.subplots(1, 2, figsize=(7.0, 3.5), layout="constrained")
    z = np.linspace(-3.4, 3.4, 400)
    a.plot(z, np.abs(z), color=NEUTRAL, linewidth=1.0, linestyle=(0, (4, 2)), zorder=1)
    rhos = [(0.5, SEQ_BLUE_STEPS[11]), (0.25, SEQ_BLUE_STEPS[8]), (0.1, SEQ_BLUE_STEPS[4])]
    for rho_i, col in rhos:
        a.plot(z, smile(z, rho_i), color=col, linewidth=LW, zorder=3)
        a.annotate(f"$\\rho$ = {rho_i:g}", (3.4, smile(3.4, rho_i)), xytext=(4, 0), textcoords="offset points",
                   ha="left", va="center", fontsize=8.5, color=INK_2)
    a.plot(z, 0 * z, color=MUTED, linewidth=LW, zorder=3)
    a.annotate("$\\rho$ = 0", (3.4, 0), xytext=(4, 0), textcoords="offset points", ha="left", va="center",
               fontsize=8.5, color=INK_2)
    zz = np.linspace(-1.6, 1.6, 60)
    a.plot(zz, math.sqrt(2 / math.pi) * 0.25 / math.sqrt(1 - 0.25 ** 2) * zz ** 2, color=INK, linewidth=1.0,
           linestyle=(0, (1, 2)), zorder=4)
    a.text(0, 3.45, "dashed: straddle limit $|r|$\ndotted: small-move parabola\nfor $\\rho$ = 0.25", ha="center",
           va="top", fontsize=7.8, color=INK_2, linespacing=1.25)
    a.set_xlim(-3.5, 4.5)
    a.set_ylim(-0.35, 3.5)
    a.set_xlabel("Next-period market return $r_{t+1}$ ($\\sigma_r$ units)")
    a.set_ylabel("Expected trend P&L given $r_{t+1}$ ($\\sigma_r$)")

    # Right: 400 simulated rounds at rho = 0.25. Every round pays +|r| (right call) or -|r| (wrong call);
    # the smile is the tilt toward right calls when the move is large.
    n = 400
    rng2 = np.random.default_rng(1012)
    m2 = rng2.standard_normal(n)
    r2 = 0.25 * m2 + math.sqrt(1 - 0.25 ** 2) * rng2.standard_normal(n)
    tf2 = np.sign(m2) * r2
    zz = np.linspace(-3.4, 3.4, 200)
    b.plot(zz, np.abs(zz), color=NEUTRAL, linewidth=1.0, linestyle=(0, (4, 2)), zorder=1)
    b.plot(zz, -np.abs(zz), color=NEUTRAL, linewidth=1.0, linestyle=(0, (4, 2)), zorder=1)
    b.plot(r2, tf2, "o", color=MUTED, markersize=3.8, alpha=0.5, markeredgewidth=0, zorder=2)
    b.plot(zz, smile(zz, 0.25), color=C_SPREAD, linewidth=2.0, zorder=4)
    edges = np.quantile(r2, np.linspace(0, 1, 9))
    bx, by, be = [], [], []
    for lo, hi in zip(edges[:-1], edges[1:]):
        sel = (r2 >= lo) & (r2 <= hi)
        bx.append(r2[sel].mean())
        by.append(tf2[sel].mean())
        be.append(tf2[sel].std(ddof=1) / math.sqrt(sel.sum()))
    b.errorbar(bx, by, yerr=be, fmt="D", color=C_RETURN, markersize=5.5, capsize=2.2, linewidth=1.1, zorder=5,
               markeredgewidth=0)
    b.text(3.2, 3.45, "right call: pays $+|r|$", ha="right", va="bottom", fontsize=8, color=INK_2)
    b.text(3.2, -3.45, "wrong call: pays $-|r|$", ha="right", va="top", fontsize=8, color=INK_2)
    b.text(-2.45, -0.4, "bin means\n$\\pm$ 1 s.e.\n(8 bins)", ha="center", va="center", fontsize=8, color=INK_2)
    b.text(3.3, -0.1, "closed form,\n$\\rho$ = 0.25", ha="right", va="center", fontsize=8, color=INK_2)
    b.set_xlim(-3.4, 3.4)
    b.set_ylim(-3.9, 3.9)
    b.set_xlabel("Next-period market return $r_{t+1}$ ($\\sigma_r$ units)")
    b.set_ylabel("Trend P&L in one round ($\\sigma_r$)")
    return finish(fig, "ch10_trend_smile")


# --------------------------------------------------------------------------------------------------------------
# Figure 10.4: whipsaw arithmetic
# --------------------------------------------------------------------------------------------------------------
def capture(T, L):
    """Round-trip capture of a V of duration T by a signal that lags the turns by L (all in months).
    T > 2L is the chapter's (T - 4L)/T. For L < T <= 2L the signal flips after the trough: 2L/T - 2.
    For T <= L it never flips inside the V and the P&L is zero."""
    T = np.asarray(T, dtype=float)
    return np.where(T <= L, 0.0, np.where(T <= 2 * L, 2 * L / T - 2.0, 1.0 - 4.0 * L / T))


def capture_numeric(T, L, d=1.0, dt_=1e-3):
    """Brute force: integrate position x index slope over the V, position = +1, -1 on [L, T/2 + L], +1."""
    t = np.arange(0, T + 3 * L + 5, dt_)
    slope = np.where(t < T / 2, -d / (T / 2), np.where(t < T, d / (T / 2), 0.0))
    pos = np.where(t < L, 1.0, np.where(t < T / 2 + L, -1.0, 1.0))
    return float((pos * slope).sum() * dt_ / (2 * d))


def fig_whipsaw_capture():
    # guard: the closed form against brute force, on both sides of T = 2L
    for L in (0.5, 1.5, 6.0):
        for T in (1.0, 1.5, 2.0, 3.0, 5.0, 8.0, 12.0, 20.0, 24.0, 36.0, 48.0):
            assert abs(float(capture(T, L)) - capture_numeric(T, L)) < 5e-3, (T, L)
    assert abs(float(capture(20, 1.5)) - 0.70) < 1e-9 and abs(float(capture(20, 6.0)) + 0.20) < 1e-9

    fig = plt.figure(figsize=(7.0, 3.6), layout="constrained")
    gs = fig.add_gridspec(2, 2, width_ratios=[1.12, 1], height_ratios=[2.3, 1.0])
    av = fig.add_subplot(gs[0, 0])
    ap = fig.add_subplot(gs[1, 0], sharex=av)
    ac = fig.add_subplot(gs[:, 1])

    # Left top: the V (T = 20 months), preceded by a slow tightening so the signal starts long
    T = 20.0
    t = np.linspace(-6, 26, 321)
    idx = np.where(t < 0, 0.1 * t, np.where(t < T / 2, -0.1 * t, np.where(t < T, -1.0 + 0.1 * (t - T / 2), 0.0)))
    av.plot(t, idx, color=INK_2, linewidth=LW)
    av.set_ylabel("Excess-return\nindex")
    av.set_yticks([])
    av.grid(False)
    plt.setp(av.get_xticklabels(), visible=False)
    av.annotate("falls for 10 months,\nrecovers for 10", (10, -1.0), xytext=(0, -6), textcoords="offset points",
                ha="center", va="top", fontsize=8.2, color=INK_2)
    av.set_ylim(-1.55, 0.35)

    # Left bottom: positions of a 3-month signal (L = 1.5) and a 12-month signal (L = 6)
    # Colour carries the signal (blue 3-month, orange 12-month), as in the right panel: the short stretch is a tint of
    # the signal's colour and the long stretches are neutral, so blue/orange never mean long/short.
    LONG_FILL = "#e6e5e1"
    for ypos, L, col, lab, res, short_fill in ((1.0, 1.5, C_SPREAD, "3-month", capture(20, 1.5), TINT_BLUE),
                                               (0.0, 6.0, C_RETURN, "12-month", capture(20, 6.0), TINT_ORANGE)):
        ap.broken_barh([(-6, L + 6)], (ypos - 0.34, 0.68), facecolors=LONG_FILL, edgecolor="none")
        ap.broken_barh([(L, T / 2)], (ypos - 0.34, 0.68), facecolors=short_fill, edgecolor="none")
        ap.broken_barh([(T / 2 + L, 26 - (T / 2 + L))], (ypos - 0.34, 0.68), facecolors=LONG_FILL, edgecolor="none")
        ap.plot([L, L], [ypos - 0.34, ypos + 0.34], color=col, linewidth=1.6)
        ap.plot([T / 2 + L, T / 2 + L], [ypos - 0.34, ypos + 0.34], color=col, linewidth=1.6)
        ap.text(L + T / 4, ypos, "short", ha="center", va="center", fontsize=7.8, color=INK_2)
        ap.text(-5.6, ypos, "long", ha="left", va="center", fontsize=7.8, color=INK_2)
        pct = f"{res * 100:+.0f}%".replace("-", "\u2212")
        ap.text(26.4, ypos, f"{lab}\n{pct}", ha="left", va="center", fontsize=8.2, color=INK_2)
        ap.plot([25.4], [ypos], "o", color=col, markersize=5, zorder=5)
    ap.set_ylim(-0.55, 1.55)
    ap.set_yticks([])
    ap.grid(False)
    ap.set_xlim(-6, 26)
    ap.set_xlabel("Months (V of $T$ = 20)")
    ap.spines["left"].set_visible(False)
    av.spines["left"].set_visible(False)

    # Right: capture ratio against the duration of the V
    Ts = np.geomspace(1.0, 48.0, 400)
    lines = [(0.5, VIOLET, "2-week lag"), (1.5, C_SPREAD, "3-month signal"), (6.0, C_RETURN, "12-month signal")]
    ac.axhline(0, color=NEUTRAL, linewidth=0.9, zorder=1)
    ac.axvspan(1.5, 2.0, color="#ecebe7", linewidth=0, zorder=0)
    ac.axvline(24, color=NEUTRAL, linewidth=0.9, linestyle=(0, (3, 3)), zorder=1)
    for L, col, lab in lines:
        c = capture(Ts, L)
        ac.plot(Ts, c * 100, color=col, linewidth=LW, zorder=3)
    fig.legend(handles=[Line2D([0], [0], color=col, linewidth=LW) for _, col, _ in lines],
               labels=["2-week lag (L = 0.5 month)", "3-month signal (L = 1.5)", "12-month signal (L = 6)"],
               loc="outside lower center", ncol=3, fontsize=8, handlelength=1.6, frameon=False)
    for L, col, _ in lines:
        ac.plot([4 * L], [0], "o", color=col, markersize=5, zorder=5)
    ac.text(1.74, 102, "Apr 2025, Mar 2020", rotation=90, ha="center", va="top", fontsize=7.8, color=INK_2)
    ac.text(25.5, -118, "2007-09", rotation=90, ha="left", va="bottom", fontsize=7.8, color=INK_2)
    ac.set_xscale("log")
    ac.set_xlim(1.0, 48)
    ac.set_ylim(-120, 105)
    ac.set_xticks([1, 2, 3, 6, 12, 24, 48])
    ac.set_xticklabels(["1", "2", "3", "6", "12", "24", "48"])
    ac.minorticks_off()
    ac.set_xlabel("Duration of the V, $T$ (months, log)")
    ac.set_ylabel("Share of the round trip captured (%)")
    return finish(fig, "ch10_whipsaw_capture")


# --------------------------------------------------------------------------------------------------------------
# Figure 10.5: the four episodes on one axis
# --------------------------------------------------------------------------------------------------------------
def fig_episodes():
    baa = load(P_BAA, parse_dates=["observation_date"], index_col="observation_date")["BAA10Y"].dropna()
    # title, panel start, episode window (as the case studies define it), descriptor, SG Trend result in the chapter
    eps = [
        ("A  2007-09", "2007-06-01", ("2007-07-01", "2009-12-31"), "slow ramp, then a cliff",
         "SG Trend 2008: +20.9%"),
        ("B  Feb-Jun 2020", "2019-12-01", ("2020-02-15", "2020-06-30"), "V in about two months",
         "SG Trend 2020: +6.24%"),
        ("C  2022", "2021-12-01", ("2022-01-01", "2022-12-31"), "a grind, mostly rates",
         "SG Trend 2022: +27.4%"),
        ("D  Apr 2025", "2024-05-01", ("2025-02-15", "2025-06-30"), "a gap that retraced",
         "SG Trend Apr 2025: \u22124.9%"),
    ]
    span = 30
    WINDOW_FILL = "#ecebe7"          # the same tint in the panels and in the legend swatch
    fig, axes = plt.subplots(1, 4, figsize=(7.0, 3.4), layout="constrained", sharey=True)
    for ax, (ttl, start, win, desc, sg) in zip(axes, eps):
        t0 = pd.Timestamp(start)
        t1 = t0 + pd.DateOffset(months=span)
        ax.axvspan(pd.Timestamp(win[0]), pd.Timestamp(win[1]), color=WINDOW_FILL, linewidth=0, zorder=0)
        g = baa.loc[t0:t1]
        ax.plot(g.index, g.values, color=C_SPREAD, linewidth=1.3, zorder=3)
        pk = g.idxmax()
        ax.plot([pk], [g.max()], "o", color=C_SPREAD, markersize=4.5, zorder=5)
        ax.annotate(f"{g.max():.2f}%", (pk, g.max()), xytext=(0, 7), textcoords="offset points", ha="center",
                    va="bottom", fontsize=8, color=INK_2)
        # lookback scale bars on the same time axis (months)
        for yb, mths, col in ((0.95, 12, C_RETURN), (0.62, 3, C_SPREAD)):   # below the data, which never drops under 1.4
            ax.plot([t0, t0 + pd.DateOffset(months=mths)], [yb, yb], color=col, linewidth=3.0, solid_capstyle="butt",
                    zorder=4)
        ax.set_title(ttl, fontsize=8.8)
        ax.text(0.03, 0.975, desc, transform=ax.transAxes, ha="left", va="top", fontsize=7.6, color=INK_2)
        ax.text(0.03, 0.915, sg, transform=ax.transAxes, ha="left", va="top", fontsize=7.6, color=INK_2)
        ax.set_xlim(t0, t1)
        ax.xaxis.set_major_locator(mdates.YearLocator())
        ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
        ax.tick_params(axis="x", labelsize=7.8)
    axes[0].set_ylim(0.35, 8.0)
    axes[0].set_yticks([1, 2, 3, 4, 5, 6])
    axes[0].set_ylabel("Baa less 10-year Treasury (%)")
    handles = [Line2D([0], [0], color=C_RETURN, linewidth=3.0, label="12-month lookback"),
               Line2D([0], [0], color=C_SPREAD, linewidth=3.0, label="3-month lookback"),
               Patch(facecolor=WINDOW_FILL, label="episode window")]
    fig.legend(handles=handles, loc="outside lower center", ncol=3, fontsize=8, handlelength=1.6, frameon=False)
    return finish(fig, "ch10_episodes_baa_spread")


def main():
    ensure_caches(refresh="--refresh" in sys.argv)
    fig_carry_hurdle()
    fig_dts_vol_scaling()
    fig_trend_smile()
    fig_whipsaw_capture()
    fig_episodes()


if __name__ == "__main__":
    main()
