"""Chapter 8 figures: Stripping Beta to Isolate Pure IDO.

Run from anywhere:  python3 tools/figures/ch08.py          (writes assets/figures/ch08_*.png, five figures)
                    python3 tools/figures/ch08.py --refresh  (re-download FRED and rebuild the derived cache)

Data policy (see style.py):
  fig 1  ch08_hedge_ratio_by_rating   REAL: the regression coefficients of Ben Dor et al., Table 7.1 (book Table 8.1).
  fig 2  ch08_recovery_route          ILLUSTRATIVE: the perpetuity of section 8.3 (c = 9%, R = 40%, r = 4%).
  fig 3  ch08_stale_marks_beta        ILLUSTRATIVE: executes Listings 8.1-8.4 of Appendix F (seed 8), so the bars
                                      are the numbers section 8.5 and 8.9 print (OLS 0.49, S-W 0.81, Dimson 1.005).
  fig 4  ch08_rolling_hedge_ratio     REAL: FRED BAMLH0A0HYM2, BAMLH0A3HYC, BAMLC0A0CM, DGS10. ICE BofA series may not
                                      be redistributed, so the raw CSVs are cached under .scratch/ (git-ignored) and
                                      only the derived rolling estimate is stored in tools/figures/data/.
  fig 5  ch08_thirty_seven_cents      ILLUSTRATIVE: the cold-open bond of sections 8.1 and 8.8 (the chapter's table).
"""
import contextlib
import csv
import datetime as dt
import io
import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))
from style import *  # noqa: E402,F401,F403  (applies the rcParams on import)

import matplotlib.dates as mdates  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib.patches import Rectangle  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
APPENDIX = os.path.join(ROOT, "book_src", "95_appF_code_companion.md")
DERIVED = os.path.join(HERE, "data", "ch08_rolling_hedge_ratio.csv")
RAW_CACHE = os.path.join(ROOT, ".scratch", "ch08_fred")
FRED = "https://fred.stlouisfed.org/graph/fredgraph.csv?id={}"
MINUS = "−"

# Chapter-wide colour roles: a rating tier keeps its colour in every figure.
C_IG, C_HY, C_B, C_CCC = BLUE, ORANGE, GREEN, VIOLET     # Baa/IG, Ba/HY, B, Caa/CCC
C_SCREEN, C_TRUE = ORANGE, BLUE                           # fig 2: what the screen says vs the truth
GAIN, LOSS = "#3987e5", "#e66767"                         # ends of the book's diverging ramp
BETA_TINT, IDO_DARK = "#9ec5f4", "#104281"


def signed(v, nd=2):
    return f"{v:+.{nd}f}".replace("-", MINUS)


# --------------------------------------------------------------------------------------------------------------
# Figure 8.1 (section 8.2): empirical hedge ratio against spread, by rating (Ben Dor, Table 7.1 = Table 8.1)
# --------------------------------------------------------------------------------------------------------------
# rating: (H as s -> 0, slope per 100 bp, H at the maximum sample OAS)
BEN_DOR = {"Baa": (0.85, -0.02, 0.67), "Ba": (0.41, -0.05, -0.26),
           "B": (0.15, -0.03, -0.42), "Caa": (0.07, -0.02, -0.52)}
RATING_COLOR = {"Baa": C_IG, "Ba": C_HY, "B": C_B, "Caa": C_CCC}


def fig_hedge_ratio_by_rating():
    fig, ax = new_figure("wide")
    ax.axhline(1.0, color=NEUTRAL, linewidth=1.0, linestyle=(0, (4, 3)), zorder=1)
    ax.axhline(0.0, color=NEUTRAL, linewidth=1.0, zorder=1)
    ax.text(3170, 1.02, "analytical duration (H = 1)", ha="right", va="bottom", fontsize=8, color=MUTED)
    ax.text(3170, 0.02, "no rate sensitivity (H = 0)", ha="right", va="bottom", fontsize=8, color=MUTED)
    at700 = {}
    for rating, (beta, gamma, h_max) in BEN_DOR.items():
        s_max = 100.0 * (beta - h_max) / (-gamma)          # bp at which the line reaches the reported H at max OAS
        s = np.linspace(0.0, s_max, 60)
        h = beta + gamma * s / 100.0
        col = RATING_COLOR[rating]
        ax.plot(s, h, color=col, linewidth=LW, zorder=3)
        label_end(ax, s_max, h_max, rating, col, dx=(3 if rating == "Ba" else 6), dy=(-12 if rating == "Ba" else 0))
        at700[rating] = beta + gamma * 7.0
    for rating, v, ms, z in (("Baa", at700["Baa"], 6, 6), ("Ba", at700["Ba"], 6, 6),
                             ("Caa", at700["Caa"], 7.5, 6), ("B", at700["B"], 3.5, 7)):
        ax.plot([700], [v], "o", color=RATING_COLOR[rating], markersize=ms, zorder=z,
                markeredgecolor="white", markeredgewidth=(0.8 if rating != "B" else 0.0))
    mark_event(ax, 700, "700 bp", y_frac=0.985)
    ax.annotate(f"Baa at 700 bp: {at700['Baa']:.2f}", (700, at700["Baa"]), xytext=(34, 18),
                textcoords="offset points", fontsize=8.5, color=INK_2,
                arrowprops=dict(arrowstyle="-", color=NEUTRAL, linewidth=0.8, shrinkA=0, shrinkB=4))
    ax.annotate(f"Ba {signed(at700['Ba'])}, B {signed(at700['B'])}, Caa {signed(at700['Caa'])}\n"
                "(near zero or negative at the same spread)", (700, 0.0), xytext=(38, 44),
                textcoords="offset points", fontsize=8.5, color=INK_2,
                arrowprops=dict(arrowstyle="-", color=NEUTRAL, linewidth=0.8, shrinkA=0, shrinkB=4))
    ax.set_xlim(0, 3250)
    ax.set_ylim(-0.7, 1.12)
    ax.set_xlabel("Option-adjusted spread (bp)")
    ax.set_ylabel("Empirical / analytical duration, H")
    note(ax, "Dots at line ends: H at the maximum sample OAS, as reported", loc="lower left")
    return finish(fig, "ch08_hedge_ratio_by_rating")


# --------------------------------------------------------------------------------------------------------------
# Figure 8.2 (section 8.3): the recovery route to zero duration
# --------------------------------------------------------------------------------------------------------------
def fig_recovery_route():
    c, R0, r = 0.09, 0.40, 0.04
    lam = np.linspace(0.0, 0.60, 241)

    def price(l, R):
        return (c + l * R) / (r + l)

    d_haz = 1.0 / (r + lam)                                   # true rate sensitivity, hazard held fixed
    d_yld = price(lam, R0) / c                                # 1 / yield, what the risk screen computes
    fig, (a, b) = new_figure("wide", ncols=2)

    a.fill_between(lam * 100, d_haz, d_yld, color="#ecebe7", linewidth=0, zorder=1)
    a.plot(lam * 100, d_yld, color=C_SCREEN, linewidth=LW, zorder=3)
    a.plot(lam * 100, d_haz, color=C_TRUE, linewidth=LW, zorder=3)
    l21 = 0.21
    y_yld, y_haz = price(l21, R0) / c, 1.0 / (r + l21)
    mark_event(a, 21, "\u03bb = 21%", y_frac=0.985)
    for yv, col in ((y_yld, C_SCREEN), (y_haz, C_TRUE)):
        a.plot([21], [yv], "o", color=col, markersize=6, zorder=6, markeredgecolor="white", markeredgewidth=0.8)
    a.annotate(f"{y_yld:.1f} yr", (21, y_yld), xytext=(8, 6), textcoords="offset points", fontsize=8.5, color=INK_2)
    a.annotate(f"{y_haz:.1f} yr", (21, y_haz), xytext=(-5, -13), textcoords="offset points", fontsize=8.5,
               color=INK_2, ha="right")
    label_end(a, 60, d_yld[-1], "screen:\n1/yield", C_SCREEN, dx=5)
    label_end(a, 60, d_haz[-1], "true:\n1/(r + \u03bb)", C_TRUE, dx=5)
    a.text(41, (d_yld[164] + d_haz[164]) / 2, "fiction", ha="center", va="center", fontsize=8.5,
           color=MUTED, style="italic")
    a.set_xlim(0, 84)
    a.set_xticks([0, 10, 20, 30, 40, 50, 60])
    a.set_ylim(0, 26)
    a.set_xlabel("Default intensity λ (% per year)")
    a.set_ylabel("Duration (years)")
    note(a, "c = 9%, R = 40%, r = 4%", loc="upper right")

    shades = {0.20: SEQ_BLUE_STEPS[4], 0.40: SEQ_BLUE_STEPS[7], 0.60: SEQ_BLUE_STEPS[10]}
    for R, col in shades.items():
        h = c / (c + lam * R)
        b.plot(lam * 100, h, color=col, linewidth=LW, zorder=3)
        label_end(b, 60, h[-1], f"R = {R:.0%}", col, dx=5)
    h21 = c / (c + 0.21 * R0)
    b.plot([21], [h21], "o", color=shades[0.40], markersize=6, zorder=6, markeredgecolor="white",
           markeredgewidth=0.8)
    mark_event(b, 21, "\u03bb = 21%", y_frac=0.985)
    b.annotate(f"{h21:.2f}", (21, h21), xytext=(7, 7), textcoords="offset points", fontsize=8.5, color=INK_2)
    b.axhline(0.0, color=NEUTRAL, linewidth=0.9, zorder=1)
    b.set_xlim(0, 74)
    b.set_xticks([0, 10, 20, 30, 40, 50, 60])
    b.set_ylim(-0.03, 1.05)
    b.set_xlabel("Default intensity λ (% per year)")
    b.set_ylabel("Recovery-route hedge ratio, H$^{rec}$")
    note(b, "c = 9%; independent of r", loc="upper right")
    return finish(fig, "ch08_recovery_route")


# --------------------------------------------------------------------------------------------------------------
# Figure 8.3 (section 8.5): stale marks shrink beta; Dimson sums it back (executes Listings 8.1-8.4)
# --------------------------------------------------------------------------------------------------------------
def load_listings(ids):
    """Execute the Appendix F listings for chapter 8 cumulatively in one namespace (the chapter's own code)."""
    with open(APPENDIX, encoding="utf-8") as fh:
        src = fh.read()
    ns = {"__name__": "ch08_engine"}
    for i in ids:
        m = re.search(r"\{#code-8-%d\}\s*```python\n(.*?)```" % i, src, re.S)
        if m is None:
            raise SystemExit(f"Listing 8.{i} not found in {APPENDIX}")
        with contextlib.redirect_stdout(io.StringIO()):
            exec(compile(m.group(1), f"listing_8_{i}", "exec"), ns)
    return ns


def fig_stale_marks_beta():
    ns = load_listings([1, 2, 3, 4])
    r_true, r_obs, x, burn = ns["r_true"], ns["r_obs"], ns["x"], ns["burn"]
    ols_slope, lagged = ns["ols_slope"], ns["lagged"]
    beta_true, beta_ols, beta_dim = ns["beta_true"], ns["beta_ols"], ns["beta_dim"]
    b_lags = ns["b_lags"]
    xs, rs, ro = x[burn], r_true[burn], r_obs[burn]
    rho_f = np.corrcoef(xs[1:], xs[:-1])[0, 1]
    sw = {k: ols_slope(ro, lagged(xs, k)) / (1.0 + 2.0 * rho_f) / beta_true for k in (-1, 0, 1)}
    parts = {
        "OLS\n(same day)": {0: beta_ols / beta_true},
        "Scholes–Williams\n(lead + lag)": {0: sw[0], 1: sw[1]},
        "Dimson\n(two lags)": {k: b_lags[k] / beta_true for k in (0, 1, 2)},
    }
    sw_total = sum(sw.values())
    assert abs(sw_total - ns["beta_sw"] / beta_true) < 1e-9
    totals = {"OLS\n(same day)": beta_ols / beta_true, "Scholes–Williams\n(lead + lag)": sw_total,
              "Dimson\n(two lags)": beta_dim / beta_true}
    for nm, parts_nm in parts.items():
        assert abs(sum(parts_nm.values()) - totals[nm]) < 0.005        # drawn stack vs estimator: lead piece only

    fig, (a, b) = new_figure("wide", ncols=2)
    # left: a stretch of cumulative return, true against stale marks
    lo, hi = 330, 390
    t = np.arange(hi - lo)
    cum_true = 100 * np.cumsum(rs[lo:hi])
    cum_obs = 100 * np.cumsum(ro[lo:hi])
    a.plot(t, cum_true, color=C_TRUE, linewidth=LW, zorder=3)      # fig 2's roles: truth blue, stale/screen orange
    a.plot(t, cum_obs, color=C_SCREEN, linewidth=LW, zorder=4)
    label_end(a, t[-1], cum_true[-1], "true", C_TRUE, dx=5)
    label_end(a, t[-1], cum_obs[-1], "stale\nmarks", C_SCREEN, dx=5, dy=-4)
    a.set_xlim(0, hi - lo - 1)
    a.set_xticks([0, 10, 20, 30, 40, 50])
    a.set_xlabel("Trading day")
    a.set_ylabel("Cumulative return (%)")
    a.axhline(0, color=NEUTRAL, linewidth=0.8, zorder=1)

    # right: the beta, stacked by the lag that supplied each piece
    lag_col = {0: SEQ_BLUE_STEPS[10], 1: SEQ_BLUE_STEPS[6], 2: SEQ_BLUE_STEPS[2], -1: SEQ_BLUE_STEPS[4]}
    names = list(parts)
    xpos = np.arange(len(names))
    seen = set()
    for xi, nm in zip(xpos, names):
        bottom = 0.0
        for lag in sorted(parts[nm]):
            v = parts[nm][lag]
            b.bar(xi, v, bottom=bottom, width=0.58, color=lag_col[lag], zorder=3,
                  label=(None if lag in seen else {0: "same day", 1: "1-day lag", 2: "2-day lag"}[lag]))
            seen.add(lag)
            if v > 0.12:
                b.text(xi, bottom + v / 2, f"{v:.2f}", ha="center", va="center", fontsize=8,
                       color=("white" if lag == 0 else INK))
            bottom += v
        # the label is the estimator itself; for Scholes-Williams the (tiny, negative) lead piece is not drawn
        b.text(xi, bottom + 0.025, f"{totals[nm]:.3f}", ha="center", va="bottom", fontsize=9, color=INK,
               fontweight="bold")
    b.axhline(1.0, color=NEUTRAL, linewidth=1.0, linestyle=(0, (4, 3)), zorder=1)
    b.text(-0.5, 1.015, "true beta = 1", ha="left", va="bottom", fontsize=8, color=MUTED)
    b.set_xticks(xpos, names)
    b.tick_params(axis="x", length=0, labelsize=8)
    b.set_ylim(0, 1.36)
    b.set_xlim(-0.55, 2.55)
    b.set_ylabel("Estimated beta (true = 1)")
    b.legend(loc="upper center", ncols=3, handlelength=1.0, columnspacing=1.2, borderaxespad=0.1)
    return finish(fig, "ch08_stale_marks_beta")


# --------------------------------------------------------------------------------------------------------------
# Figure 8.4 (section 8.7): the rolling 60-day hedge ratio on FRED data
# --------------------------------------------------------------------------------------------------------------
SERIES_IDS = {"HY": "BAMLH0A0HYM2", "CCC": "BAMLH0A3HYC", "IG": "BAMLC0A0CM"}
WINDOW = 60


def read_fred(sid, refresh=False):
    path = os.path.join(RAW_CACHE, f"{sid}.csv")
    if refresh or not os.path.exists(path):
        import urllib.request
        os.makedirs(RAW_CACHE, exist_ok=True)
        with urllib.request.urlopen(FRED.format(sid), timeout=60) as r, open(path, "wb") as f:
            f.write(r.read())
    out = {}
    with open(path) as f:
        for row in csv.reader(f):
            if row[0] == "observation_date" or row[1].strip() in ("", "."):
                continue
            out[row[0]] = float(row[1])
    return out


def rolling_hedge_ratio(refresh=False):
    """H = 1 + mean(OAS) * rho * sigma_s / sigma_y on a rolling 60-day window of daily changes.
    s = OAS (decimal), relative change = ds / s(t-1); dy = change in DGS10 (decimal). Common dates only."""
    ser = {k: read_fred(v, refresh) for k, v in SERIES_IDS.items()}
    ser["DGS10"] = read_fred("DGS10", refresh)
    dates = sorted(set.intersection(*[set(v) for v in ser.values()]))
    dates = [d for d in dates if d >= "2023-10-17"]
    lvl = {k: np.array([ser[k][d] for d in dates]) for k in ser}
    dy = np.diff(lvl["DGS10"]) / 100.0
    rows = []
    out = {k: [] for k in SERIES_IDS}
    for i in range(WINDOW - 1, len(dy)):
        sl = slice(i - WINDOW + 1, i + 1)
        for k in SERIES_IDS:
            s = lvl[k] / 100.0
            rel = np.diff(s) / s[:-1]
            sbar = s[1:][sl].mean()
            rho = np.corrcoef(rel[sl], dy[sl])[0, 1]
            out[k].append(1.0 + sbar * rho * rel[sl].std(ddof=1) / dy[sl].std(ddof=1))
        rows.append(dates[i + 1])
    os.makedirs(os.path.dirname(DERIVED), exist_ok=True)
    with open(DERIVED, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["date"] + list(SERIES_IDS))
        for j, d in enumerate(rows):
            w.writerow([d] + [f"{out[k][j]:.4f}" for k in SERIES_IDS])
    return rows, out


def load_rolling(refresh=False):
    if refresh or not os.path.exists(DERIVED):
        rows, out = rolling_hedge_ratio(refresh)
        return np.array([dt.datetime.strptime(d, "%Y-%m-%d") for d in rows]), {k: np.array(v) for k, v in out.items()}
    d, out = [], {k: [] for k in SERIES_IDS}
    with open(DERIVED) as f:
        for row in csv.DictReader(f):
            d.append(dt.datetime.strptime(row["date"], "%Y-%m-%d"))
            for k in SERIES_IDS:
                out[k].append(float(row[k]))
    return np.array(d), {k: np.array(v) for k, v in out.items()}


def fig_rolling_hedge_ratio(refresh=False):
    d, H = load_rolling(refresh)
    fig, ax = new_figure("wide")
    ax.axhline(1.0, color=NEUTRAL, linewidth=1.0, linestyle=(0, (4, 3)), zorder=1)
    ax.axhline(0.0, color=NEUTRAL, linewidth=1.0, zorder=1)
    ax.fill_between([d[0], d[-1]], -1.0, 0.0, color="#f4f3f0", linewidth=0, zorder=0)
    for k, col in (("IG", C_IG), ("HY", C_HY), ("CCC", C_CCC)):
        ax.plot(d, H[k], color=col, linewidth=LW, zorder=3)
    # direct labels in a right margin
    ends = {k: H[k][-1] for k in H}
    order = sorted(ends, key=ends.get)
    pos, gap = {}, 0.17
    last = -9
    for k in order:
        y = max(ends[k], last + gap) if last > -9 else ends[k]
        pos[k], last = y, y
    for k, col in (("IG", C_IG), ("HY", C_HY), ("CCC", C_CCC)):
        ax.plot([d[-1]], [ends[k]], "o", color=col, markersize=4, zorder=5, clip_on=False)
        ax.annotate({"IG": "IG", "HY": "HY", "CCC": "CCC"}[k], (d[-1], ends[k]), xytext=(7, (pos[k] - ends[k]) * 72),
                    textcoords="offset points", va="center", fontsize=8.5, color=INK_2, annotation_clip=False)
    mark_event(ax, dt.datetime(2025, 4, 2), "Apr 2, 2025\ntariff announcement", y_frac=0.985)
    i = int(np.argmin(H["CCC"]))
    ax.plot([d[i]], [H["CCC"][i]], "o", color=C_CCC, markersize=5.5, zorder=6, markeredgecolor="white",
            markeredgewidth=0.8)
    ax.annotate(f"CCC {signed(H['CCC'][i])} ({d[i]:%b} {d[i].day}, {d[i]:%Y})", (d[i], H["CCC"][i]),
                xytext=(7, -3), textcoords="offset points", ha="left", va="center", fontsize=8.5, color=INK_2)
    ax.text(d[2], -0.9, "H < 0: the minimum-variance\nhedge is long futures", fontsize=8, color=MUTED, va="center")
    note(ax, "dashed line: analytical duration (H = 1)", loc="upper left")
    ax.set_ylim(-1.0, 2.05)
    ax.set_xlim(d[0], d[-1])
    ax.xaxis.set_major_locator(mdates.MonthLocator(bymonth=(1, 4, 7, 10)))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b\n%Y"))
    ax.set_ylabel("Rolling 60-day hedge ratio, H")
    ax.set_xlabel("End of window")
    fig.get_layout_engine().set(rect=(0, 0, 0.95, 1))
    return finish(fig, "ch08_rolling_hedge_ratio")


# --------------------------------------------------------------------------------------------------------------
# Figure 8.5 (section 8.8): the thirty-seven cents, itemised
# --------------------------------------------------------------------------------------------------------------
def fig_thirty_seven_cents():
    steps = [("Carry", 3, GAIN), ("Rates\n(analytical)", -70, LOSS), ("Market\nspread beta", 28, BETA_TINT),
             ("Bond-specific\nspread (IDO)", 6, IDO_DARK), ("Decomposition\nresidual", -4, LOSS)]
    fig, ax = new_figure("wide")
    level, xs = 0.0, np.arange(len(steps) + 1)
    tops = []
    for i, (nm, v, col) in enumerate(steps):
        ax.bar(i, v, bottom=level, width=0.62, color=col, zorder=3)
        new = level + v
        ax.plot([i + 0.31, i + 1 - 0.31], [new, new], color=NEUTRAL, linewidth=0.9, zorder=2)
        up = v > 0
        ax.text(i, (new + 2.5) if up else (new - 2.5), signed(v, 0), ha="center", va=("bottom" if up else "top"),
                fontsize=9.5, color=INK, fontweight="bold")
        tops.append((level, new))
        level = new
    total = level
    n = len(steps)
    ax.bar(n, total, width=0.62, color=INK_2, zorder=3)
    ax.text(n, total - 3, signed(total, 0), ha="center", va="top", fontsize=9.5, color=INK, fontweight="bold")
    ax.axhline(0, color=INK_2, linewidth=0.9, zorder=2)
    # bracket over the two spread bars: Kaz's "alpha"
    y0 = -20
    ax.plot([1.69, 1.69, 3.31, 3.31], [y0 - 3, y0, y0, y0 - 3], color=INK_2, linewidth=1.0, zorder=4)
    ax.text(2.5, y0 + 2.5, "Kaz's “alpha”: +34 = 28 beta + 6 IDO", ha="center", va="bottom", fontsize=8.5,
            color=INK_2)
    ax.set_xticks(np.arange(n + 1), [s[0] for s in steps] + ["Total\nreturn"])
    ax.tick_params(axis="x", length=0, labelsize=8.5)
    ax.set_xlim(-0.55, n + 0.55)
    ax.set_ylim(-84, 14)
    ax.set_ylabel("Cents on a $95 bond price")
    return finish(fig, "ch08_thirty_seven_cents")


if __name__ == "__main__":
    refresh = "--refresh" in sys.argv
    fig_hedge_ratio_by_rating()
    fig_recovery_route()
    fig_stale_marks_beta()
    fig_rolling_hedge_ratio(refresh)
    fig_thirty_seven_cents()
