"""Chapter 28 figures (What a Desk Head / Senior PM Must Know to Extract Maximum Alpha).

Run from anywhere: python3 tools/figures/ch28.py   (writes assets/figures/ch28_*.png)

Data policy (see style.py):
- ch28_ccc_decompression is REAL data: FRED series BAMLH0A0HYM2 (US HY OAS), BAMLH0A3HYC (CCC and lower OAS) and
  BAMLC0A0CM (US IG OAS), ICE BofA indices, 2026 observations through 15 October 2026, fetched 18 October 2026 and
  cached in tools/figures/data/ch28_ice_oas_2026ytd.csv. FRED serves only a rolling three-year window of these
  series and flags them "for internal use only", so only the 2026 rows already quoted in the section 28.4
  Trend Watch are cached and drawn.
- Every other figure is Illustrative: it evaluates the chapter's own closed forms ((28.2)-(28.5), (28.9)-(28.11),
  (28.19)-(28.23)) at the parameters the chapter states, and the asserts below reproduce the chapter's numbers.

Role colors, fixed per figure and direct-labelled (slots 3-5 are below 3:1 contrast on white): see each function.
"""
import csv
import os
import sys
from datetime import date, datetime, timedelta

sys.path.insert(0, os.path.dirname(__file__))
from style import *  # noqa: F401,F403,E402  (applies the rcParams on import)
import matplotlib.dates as mdates  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib.lines import Line2D  # noqa: E402
from scipy.stats import norm  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data", "ch28_ice_oas_2026ytd.csv")
FRED = "https://fred.stlouisfed.org/graph/fredgraph.csv?id={}"
SERIES_IDS = ["BAMLH0A0HYM2", "BAMLH0A3HYC", "BAMLC0A0CM"]  # HY, CCC and lower, IG


def dot_label(ax, x, y, text, color, dx=6, dy=0, ha="left", va="center", fs=8.5):
    """Direct label with a small colored dot on the mark; the text stays ink."""
    ax.plot([x], [y], "o", color=color, markersize=4.5, zorder=6, clip_on=False)
    ax.annotate(text, (x, y), xytext=(dx, dy), textcoords="offset points", ha=ha, va=va,
                fontsize=fs, color=INK_2, annotation_clip=False)


def text_in(ax, x, y, s, ha="left", va="center", fs=8.5, color=INK_2, **kw):
    ax.annotate(s, (x, y), ha=ha, va=va, fontsize=fs, color=color, annotation_clip=False, **kw)


# --------------------------------------------------------------------------------------------
# Figure 28.1: effective breadth and the information ratio (Section 28.2)
# --------------------------------------------------------------------------------------------
def neff_blocks(N, m, rho_w, rho_a):
    """Equation (28.5): equal blocks of m bonds per issuer."""
    return N / (1 + (m - 1) * rho_w + (N - m) * rho_a)


def ir_hit(p, n):
    """Equation (28.3), exact form."""
    ic = 2 * p - 1
    return ic * np.sqrt(252 * n) / np.sqrt(1 - ic ** 2)


def fig_breadth():
    m, rw = 5, 0.9
    assert abs(neff_blocks(300, m, rw, 0.01) - 39.7) < 0.05           # Theo's book
    assert abs(300 / (1 + (m - 1) * rw) - 65.2) < 0.1                  # rho_a = 0: the issuer count, inflated
    assert abs(neff_blocks(1e9, m, rw, 0.01) - 100) < 0.01             # the 1/rho_a ceiling
    assert abs(ir_hit(0.505, 300) - 2.7) < 0.06 and abs(ir_hit(0.505, 40) - 1.0) < 0.02
    assert abs(ir_hit(0.52, 300) - 11.0) < 0.05 and abs(ir_hit(0.52, 40) - 4.0) < 0.05

    fig, (a, b) = new_figure("wide", ncols=2)

    # (a) N_eff against the number of bonds
    N = np.linspace(5, 1000, 500)
    for rho_a, col in [(0.01, BLUE), (0.03, ORANGE)]:
        a.plot(N, neff_blocks(N, m, rw, rho_a), color=col, zorder=3)
    for ceil, col in [(100, BLUE), (1 / 0.03, ORANGE)]:
        a.axhline(ceil, color=col, linewidth=0.9, linestyle=(0, (1, 3)), zorder=1)
    a.set_xlim(0, 1000)
    a.set_ylim(0, 112)
    a.set_xlabel("Bonds in the book (N)")
    a.set_ylabel(r"Effective bets $N_{\mathrm{eff}}$")
    a.set_xticks([0, 250, 500, 750, 1000])
    text_in(a, 990, 100 + 3, r"$\rho_a=0.01$: ceiling 100", ha="right", va="bottom")
    text_in(a, 990, 33.3 + 3, r"$\rho_a=0.03$: ceiling 33", ha="right", va="bottom")
    a.plot([300], [neff_blocks(300, m, rw, 0.01)], "o", color=INK, markersize=6, zorder=7)
    a.plot([300, 300], [0, neff_blocks(300, m, rw, 0.01)], color=INK_2, linewidth=0.8,
           linestyle=(0, (3, 3)), zorder=2)
    text_in(a, 318, 12, "Theo: 300 bonds,\n$N_{\\mathrm{eff}}$ = 39.7", ha="left", va="center")
    a.set_title("(a) Breadth saturates", fontsize=9.5)

    # (b) IR against independent bets, at two hit rates
    n = np.linspace(1, 320, 400)
    b.plot(n, ir_hit(0.52, n), color=ORANGE, zorder=3)
    b.plot(n, ir_hit(0.505, n), color=BLUE, zorder=3)
    for xv in (40, 300):
        b.axvline(xv, color=NEUTRAL, linewidth=0.9, linestyle=(0, (3, 3)), zorder=1)
    for p, col in [(0.52, ORANGE), (0.505, BLUE)]:
        for xv in (40, 300):
            b.plot([xv], [ir_hit(p, xv)], "o", color=col, markersize=5.5, zorder=6)
    b.set_xlim(0, 320)
    b.set_ylim(0, 12.5)
    b.set_xlabel(r"Independent bets ($N$ or $N_{\mathrm{eff}}$)")
    b.set_ylabel("Information ratio")
    b.set_xticks([0, 40, 100, 200, 300])
    text_in(b, 292, ir_hit(0.52, 300) + 0.3, "11.0", ha="right", va="bottom", fs=8)
    text_in(b, 44, ir_hit(0.52, 40) + 0.9, "4.0", ha="left", va="bottom", fs=8)
    text_in(b, 292, ir_hit(0.505, 300) + 0.5, "2.7", ha="right", va="bottom", fs=8)
    text_in(b, 44, ir_hit(0.505, 40) - 0.5, "1.0", ha="left", va="top", fs=8)
    text_in(b, 175, ir_hit(0.52, 175) - 0.8, "hit rate 52%", ha="center", va="top")
    text_in(b, 150, ir_hit(0.505, 150) - 0.9, "hit rate 50.5%", ha="center", va="top")
    b.set_title("(b) The IR the book can claim", fontsize=9.5)
    return finish(fig, "ch28_breadth_ceiling")


# --------------------------------------------------------------------------------------------
# Figure 28.2: the 2026 CCC decompression, real data (Section 28.4 Trend Watch)
# --------------------------------------------------------------------------------------------
def load_oas():
    if not os.path.exists(DATA):
        import urllib.request
        rows = {}
        for sid in SERIES_IDS:
            with urllib.request.urlopen(FRED.format(sid), timeout=60) as r:
                lines = r.read().decode().splitlines()
            for rec in csv.DictReader(lines):
                if rec["observation_date"].startswith("2026") and rec[sid] not in ("", "."):
                    rows.setdefault(rec["observation_date"], {})[sid] = rec[sid]
        os.makedirs(os.path.dirname(DATA), exist_ok=True)
        with open(DATA, "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["observation_date"] + SERIES_IDS)
            for k in sorted(rows):
                w.writerow([k] + [rows[k].get(s, "") for s in SERIES_IDS])
    d, hy, ccc, ig = [], [], [], []
    with open(DATA) as f:
        for rec in csv.DictReader(f):
            if all(rec[s] not in ("", ".") for s in SERIES_IDS):
                d.append(datetime.strptime(rec["observation_date"], "%Y-%m-%d"))
                hy.append(float(rec["BAMLH0A0HYM2"]))
                ccc.append(float(rec["BAMLH0A3HYC"]))
                ig.append(float(rec["BAMLC0A0CM"]))
    return d, np.array(hy), np.array(ccc), np.array(ig)


def fig_ccc_decompression():
    d, hy, ccc, ig = load_oas()
    ratio = ccc / hy
    idx = {x.strftime("%Y-%m-%d"): i for i, x in enumerate(d)}
    # asserts reproduce the Trend Watch numbers
    assert (hy[idx["2026-01-02"]], ccc[idx["2026-01-02"]], ig[idx["2026-01-02"]]) == (2.83, 8.88, 0.79)
    assert hy.min() == 2.60 or hy[idx["2026-01-22"]] == 2.64
    assert hy[idx["2026-03-30"]] == 3.46 and ccc[idx["2026-03-30"]] == 10.20
    assert (hy[idx["2026-10-15"]], ccc[idx["2026-10-15"]], ig[idx["2026-10-15"]]) == (3.23, 12.78, 0.84)
    assert ccc[idx["2026-10-14"]] == 12.82 and ccc[idx["2026-01-28"]] == 8.38
    assert abs(ratio[idx["2026-01-02"]] - 3.1) < 0.1 and abs(ratio[idx["2026-10-15"]] - 4.0) < 0.1

    fig, (a, b) = new_figure("wide", ncols=2)
    ev = datetime(2026, 3, 30)
    xr = (datetime(2026, 1, 1), datetime(2026, 12, 8))

    a.plot(d, ccc, color=ORANGE, zorder=3)
    a.plot(d, hy, color=BLUE, zorder=3)
    a.plot(d, ig, color=AQUA, zorder=3)
    mark_event(a, ev, "30 Mar", y_frac=0.50)
    a.set_xlim(*xr)
    a.set_ylim(0, 14.5)
    a.set_ylabel("Option-adjusted spread (%)")
    label_end(a, d[-1], ccc[-1], "CCC 12.78", ORANGE)
    label_end(a, d[-1], hy[-1], "HY 3.23", BLUE)
    label_end(a, d[-1], ig[-1], "IG 0.84", AQUA, dy=-1)
    a.set_title("(a) The index is bored", fontsize=9.5)

    b.plot(d, ratio, color=ORANGE, zorder=3)
    mark_event(b, ev, "30 Mar", y_frac=0.95)
    b.set_xlim(*xr)
    b.set_ylim(2.5, 4.3)
    b.set_ylabel("CCC OAS / HY OAS (×)")
    label_end(b, d[0], ratio[0], "3.1×", ORANGE, dx=1, dy=15, ha="left")
    label_end(b, d[-1], ratio[-1], "4.0×", ORANGE)
    b.set_title("(b) The basement is not", fontsize=9.5)

    for ax in (a, b):
        ax.xaxis.set_major_locator(mdates.MonthLocator(bymonth=(1, 3, 5, 7, 9)))
        ax.xaxis.set_major_formatter(mdates.DateFormatter("%b"))
        ax.set_xlabel("2026")
    return finish(fig, "ch28_ccc_decompression")


# --------------------------------------------------------------------------------------------
# Figure 28.3: Kelly with a jump and a ruin boundary (Section 28.4)
# --------------------------------------------------------------------------------------------
def g_disc(f, c, L, q):
    """One-period expected log growth, equation after (28.8)."""
    return (1 - q) * np.log1p(f * c) + q * np.log1p(-f * L)


def g_cont(f, c, lam, L):
    """Equation (28.10) with sigma = 0."""
    return f * c + lam * np.log1p(-f * L)


def fig_kelly_ruin():
    c, q, L = 0.045, 0.031, 0.6
    fk = (1 - q) / L - q / c
    assert abs(fk - 0.926) < 0.001 and abs(1 / L - 1.667) < 0.001
    lam_m, c_m, L_m = 0.031, 0.045, 0.6
    sigma = 0.05
    f_merton = (c_m - lam_m * L_m) / (sigma ** 2 + lam_m * L_m ** 2)
    assert abs(f_merton - 1.93) < 0.01

    jan = dict(c=0.084, lam=0.06, L=0.55)
    octo = dict(c=0.128, lam=0.10, L=0.70)
    fj = 1 / jan["L"] - jan["lam"] / jan["c"]
    fo = 1 / octo["L"] - octo["lam"] / octo["c"]
    assert abs(fj - 1.10) < 0.01 and abs(fo - 0.65) < 0.01
    assert abs((jan["c"] - jan["lam"] * jan["L"]) - 0.051) < 1e-3 and abs((octo["c"] - octo["lam"] * octo["L"]) - 0.058) < 1e-3
    gj, go = g_cont(fj, **jan) * 100, g_cont(fo, **octo) * 100

    fig, (a, b) = new_figure("wide", ncols=2)

    # (a) Kaz's B3 bond
    f = np.linspace(0, 1 / L - 1e-4, 800)
    g = g_disc(f, c, L, q) * 100
    a.axhline(0, color=NEUTRAL, linewidth=0.9, zorder=1)
    a.axvspan(1 / L, 2.15, color=GRID, zorder=0)
    a.axvline(1 / L, color=INK_2, linewidth=0.9, linestyle=(0, (3, 3)), zorder=2)
    a.plot(f, g, color=BLUE, zorder=4)
    gk = g_disc(fk, c, L, q) * 100
    a.plot([fk], [gk], "o", color=BLUE, markersize=6, zorder=6)
    a.plot([fk / 2], [g_disc(fk / 2, c, L, q) * 100], "o", color=BLUE, markersize=5, markerfacecolor="white",
           markeredgewidth=1.4, zorder=6)
    a.set_xlim(0, 2.15)
    a.set_ylim(-4, 2.2)
    a.set_xlabel("Position as a multiple of NAV, $f$")
    a.set_ylabel("Expected log growth (% per year)")
    text_in(a, fk, gk + 0.30, "Kelly 0.93", ha="center", va="bottom")
    text_in(a, fk / 2 - 0.02, g_disc(fk / 2, c, L, q) * 100 + 0.4, "half\nKelly", ha="center", va="bottom")
    text_in(a, 1 / L + 0.04, 1.25, "ruin\nboundary\n$1/L$ = 1.67", ha="left", va="center", fs=8)
    a.annotate("", xy=(f_merton, -3.75), xytext=(f_merton, -2.85),
               arrowprops=dict(arrowstyle="-|>", color=INK_2, lw=1.0), annotation_clip=False)
    text_in(a, f_merton, -2.65, "Merton's\nfraction\n1.93", ha="center", va="bottom", fs=8)
    a.set_title("(a) Kaz's B3 bond", fontsize=9.5)

    # (b) CCC bucket, January versus October
    for p, col, fs_, gs_ in [(jan, BLUE, fj, gj), (octo, ORANGE, fo, go)]:
        rb = 1 / p["L"]
        ff = np.linspace(0, rb - 1e-4, 800)
        b.plot(ff, g_cont(ff, **p) * 100, color=col, zorder=4)
        b.axvline(rb, color=col, linewidth=0.9, linestyle=(0, (3, 3)), zorder=2)
        b.plot([fs_], [gs_], "o", color=col, markersize=6, zorder=6)
    b.axhline(0, color=NEUTRAL, linewidth=0.9, zorder=1)
    b.set_xlim(0, 2.0)
    b.set_ylim(-6, 5)
    b.set_xlabel("Position as a multiple of NAV, $f$")
    b.set_ylabel("Expected log growth (% per year)")
    text_in(b, fj, gj + 0.45, "Jan: $f^*$ = 1.10", ha="center", va="bottom")
    text_in(b, fo, 0.75, "Oct: $f^*$ = 0.65", ha="center", va="center")
    b.annotate("", xy=(fo, go - 0.25), xytext=(fo, 1.15), arrowprops=dict(arrowstyle="-", color=INK_2, lw=0.8),
               annotation_clip=False)
    text_in(b, 1 / jan["L"] + 0.03, -1.7, "ruin\n1.82", ha="left", va="center", fs=8)
    text_in(b, 1 / octo["L"] - 0.03, -3.9, "ruin\n1.43", ha="right", va="center", fs=8)
    note(b, "edge $c-\\lambda L$: 5.1% (Jan), 5.8% (Oct)", loc="lower left")
    b.set_title("(b) CCC bucket: edge up, Kelly down", fontsize=9.5)
    return finish(fig, "ch28_kelly_ruin")


# --------------------------------------------------------------------------------------------
# Figure 28.4: the mark is a stop-loss you did not set (Section 28.6)
# --------------------------------------------------------------------------------------------
def prob_life(x, sr, sigma):
    return np.exp(-2 * sr * x / sigma)


def fig_mark_to_bid_stop():
    lcs, G, sigma = 0.006, 5.0, 0.06
    ms = [1.64, 3.0, 5.8, 6.0]
    shocks = [0.5 * (m - 1) * lcs * G * 100 for m in ms]
    assert abs(shocks[2] - 7.2) < 1e-9 and abs(shocks[3] - 7.5) < 1e-9
    assert abs(prob_life(0.075, 1, sigma) - 0.082) < 0.001 and abs(prob_life(0.075, 0.5, sigma) - 0.29) < 0.005
    x_eff = 0.075 - shocks[2] / 100
    assert abs(x_eff - 0.003) < 1e-9

    fig, (a, b) = new_figure("wide", ncols=2)

    # (a) mark-to-bid shock against the two thresholds
    xs = np.arange(4)
    a.bar(xs, shocks, width=0.62, color=BLUE, zorder=3)
    for lvl, lab in [(5.0, "first cut, 5%"), (7.5, "exit, 7.5%")]:
        a.axhline(lvl, color=INK_2, linewidth=0.9, linestyle=(0, (3, 3)), zorder=4)
    text_in(a, -0.45, 5.0 + 0.2, "first cut 5%", ha="left", va="bottom", fs=8)
    text_in(a, -0.45, 7.5 + 0.2, "exit 7.5%", ha="left", va="bottom", fs=8)
    for x, s in zip(xs, shocks):
        text_in(a, x, s - 0.25, f"{s:.1f}", ha="center", va="top", fs=8, color="white")
    a.set_xticks(xs)
    a.set_xticklabels(["EUR IG\nMar 2026\n$m$ = 1.64", "IG\nMar 2020\n$m$ = 3", "IG index\n2007-08\n$m$ = 5.8",
                       "IG blocks\nMar 2020\n$m$ = 6"], fontsize=8)
    a.set_xlim(-0.5, 3.5)
    a.set_ylim(0, 9)
    a.set_ylabel("Mark-to-bid shock (% of NAV)")
    a.grid(False)
    a.yaxis.grid(True)
    a.set_title("(a) No issuer has moved", fontsize=9.5)

    # (b) lifetime stop-out probability against stop distance (log axis: each curve is a straight line)
    x = np.linspace(0, 0.12, 400)
    curves = [(0.5, BLUE, "Sharpe 0.5"), (1.0, ORANGE, "Sharpe 1"), (2.0, AQUA, "Sharpe 2")]
    for sr, col, _ in curves:
        b.plot(x * 100, prob_life(x, sr, sigma) * 100, color=col, zorder=3)
    b.axvline(7.5, color=NEUTRAL, linewidth=0.9, linestyle=(0, (3, 3)), zorder=1)
    for sr, col, lab in curves:
        pv = prob_life(0.075, sr, sigma) * 100
        b.plot([7.5], [pv], "o", color=col, markersize=5.5, zorder=6)
        label_end(b, 12, prob_life(0.12, sr, sigma) * 100, lab, col)
    for pv, txt in [(prob_life(0.075, 0.5, sigma) * 100, "29%"), (prob_life(0.075, 1.0, sigma) * 100, "8%"),
                    (prob_life(0.075, 2.0, sigma) * 100, "0.7%")]:
        text_in(b, 7.7, pv * 1.75, txt, ha="left", va="center", fs=8)
    b.plot([x_eff * 100], [prob_life(x_eff, 1.0, sigma) * 100], "o", color=ORANGE, markersize=6.5,
           markerfacecolor="white", markeredgewidth=1.6, zorder=7)
    b.set_yscale("log")
    b.set_xlim(0, 12)
    b.set_ylim(0.03, 140)
    b.set_xticks([0, 2, 4, 6, 8, 10, 12])
    b.set_yticks([0.1, 1, 10, 100])
    b.set_yticklabels(["0.1%", "1%", "10%", "100%"])
    b.minorticks_off()
    b.set_xlabel("Distance to the stop (% of allocated capital)")
    b.set_ylabel("Lifetime stop-out probability")
    text_in(b, 0.75, 0.2, "after a 7.2% mark shock\nthe stop is 0.3% away: a\nSharpe-1 PM now stops\nout with probability 90%",
            ha="left", va="center", fs=8)
    b.annotate("", xy=(x_eff * 100 + 0.02, prob_life(x_eff, 1.0, sigma) * 100 * 0.72), xytext=(0.55, 0.6),
               arrowprops=dict(arrowstyle="-|>", color=INK_2, lw=0.9), annotation_clip=False)
    b.set_title("(b) What the cushion buys", fontsize=9.5)
    return finish(fig, "ch28_mark_to_bid_stop")


# --------------------------------------------------------------------------------------------
# Figure 28.5: the leverage band and its liquidity speed limit (Section 28.7)
# --------------------------------------------------------------------------------------------
def band(lcs, r_min, n_eff=40, sig=0.05, sr=2.0, kz=4.0, dd=0.075, m=5.8):
    floor = np.sqrt(n_eff) / sig * r_min / sr
    A = np.sqrt(n_eff) / (sig * (kz - sr))
    c1 = 0.5 * (m - 1) * lcs
    ceil = A * dd / (1 + A * c1)
    speed = np.where(c1 > 0, dd / np.where(c1 > 0, c1, 1), np.inf)
    return floor, ceil, speed


def fig_leverage_band():
    f5, c0, _ = band(0.0, 0.05)
    assert abs(f5 - 3.16) < 0.01 and abs(c0 - 4.74) < 0.01
    _, c8, s8 = band(0.008, 0.05)
    assert abs(c8 - 2.14) < 0.01 and abs(s8 - 3.9) < 0.05 and c8 < f5
    f4, c4, _ = band(0.004, 0.04)
    assert abs(f4 - 2.53) < 0.01 and abs(c4 - 2.95) < 0.01 and f4 < c4

    lcs = np.linspace(0, 0.012, 600)
    _, ceil, speed = band(lcs, 0.05)
    x = lcs * 100
    fig, ax = new_figure("wide")
    ax.fill_between(x, f5, ceil, where=ceil >= f5, color=SEQ_BLUE(0.25), zorder=1, linewidth=0)
    ax.plot(x, speed, color=INK_2, linewidth=1.1, linestyle=(0, (4, 3)), zorder=2)
    ax.plot(x, ceil, color=ORANGE, zorder=4)
    ax.axhline(f5, color=BLUE, zorder=4, linewidth=LW)
    ax.axhline(f4, color=BLUE, zorder=3, linewidth=1.2, linestyle=(0, (2, 2)))
    ax.set_xlim(0, 1.2)
    ax.set_ylim(0, 6.2)
    ax.set_xlabel("Average round-trip liquidity cost, $\\overline{\\mathrm{LCS}}$ (% of price)")
    ax.set_ylabel("Gross leverage $G$ (× NAV)")

    text_in(ax, 1.18, f5 + 0.12, "floor, hurdle 5%", ha="right", va="bottom")
    text_in(ax, 1.18, f4 - 0.12, "floor, hurdle 4%", ha="right", va="top")
    text_in(ax, 1.18, ceil[-1] - 0.12, "ceiling with mark-to-bid cost", ha="right", va="top")
    text_in(ax, 0.66, 5.6, "speed limit $2\\,\\mathrm{DD}_{\\max}/((m-1)\\,\\overline{\\mathrm{LCS}})$", ha="left", va="center")

    # the three cases worked in the text
    ax.plot([0, 0], [f5, c0], "o", color=INK, markersize=5.5, zorder=7, clip_on=False)
    text_in(ax, 0.04, 5.45, "no liquidity charge: band 3.2 to 4.7", ha="left", va="center", fs=8)
    ax.plot([0.8, 0.8], [c8, f5], color=INK, linewidth=1.4, zorder=6)
    ax.plot([0.8], [c8], "o", color=ORANGE, markeredgecolor=INK, markersize=6, zorder=7)
    text_in(ax, 0.78, 3.62, "LCS 0.8%: ceiling 2.1 below\nfloor 3.2, band empty", ha="right", va="center", fs=8)
    ax.plot([0.4, 0.4], [f4, c4], color=INK, linewidth=2.4, zorder=6, solid_capstyle="butt")
    text_in(ax, 0.37, 1.45, "LCS 0.4%, hurdle 4%:\nband reopens, 2.5 to 3.0", ha="right", va="center", fs=8)
    ax.annotate("", xy=(0.4, f4 - 0.06), xytext=(0.385, 1.75),
                arrowprops=dict(arrowstyle="-|>", color=INK_2, lw=0.9), annotation_clip=False)
    return finish(fig, "ch28_leverage_band")


if __name__ == "__main__":
    fig_breadth()
    fig_ccc_decompression()
    fig_kelly_ruin()
    fig_mark_to_bid_stop()
    fig_leverage_band()
