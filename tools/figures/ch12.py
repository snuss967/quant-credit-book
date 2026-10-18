"""Chapter 12 figures: Multi-Asset Credit Allocation.

Run from anywhere:  python3 tools/figures/ch12.py
Writes assets/figures/ch12_*.png (five figures, in order of appearance in the chapter).

Data policy (see style.py):
  Fig 1  schematic (ownership graph); post-default values are the Cai and Haque (FEDS Notes, 2024) numbers the chapter cites.
  Fig 2  Nuveen's printed numbers (Figures 3 and 6 of the Nuveen paper), as quoted in the chapter.
  Fig 3  Illustrative: the engine of Listings 12.1, 12.3 and 12.5 (Appendix F), re-run with random input error.
  Fig 4  real data: ICE BofA US High Yield indices via FRED (daily OAS and total-return index values).
  Fig 5  real data: ICE BofA US High Yield bucket OAS and total-return indices via FRED.
FRED rolls the ICE BofA window (about three years), so the plotted slice is cached in
tools/figures/data/ch12_ice_fred.csv; pass --refresh to download it again (the window will then have moved).
The cache holds only what the figures plot (daily OAS over the window; total-return values for the dates used).
"""
import csv
import datetime as dt
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from style import *  # noqa: F401,F403,E402  (applies the rcParams on import)

import matplotlib.dates as mdates  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib.lines import Line2D  # noqa: E402
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Patch  # noqa: E402
from scipy.optimize import minimize  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "data", "ch12_ice_fred.csv")
FRED = "https://fred.stlouisfed.org/graph/fredgraph.csv?id="
OAS_IDS = {"HY": "BAMLH0A0HYM2", "BB": "BAMLH0A1HYBB", "B": "BAMLH0A2HYB", "CCC": "BAMLH0A3HYC"}
TR_IDS = {"HY": "BAMLHYH0A0HYM2TRIV", "BB": "BAMLHYH0A1BBTRIV", "B": "BAMLHYH0A2BTRIV", "CCC": "BAMLHYH0A3CMTRIV"}
TR_KEEP = [("2025-02-01", "2025-05-15"), ("2025-12-31", "2025-12-31"), ("2026-10-15", "2026-10-15")]

# Chapter-wide colour roles (a role keeps its colour in every figure): rating buckets in rating order.
C_BB, C_B, C_CCC, C_HY = BLUE, ORANGE, AQUA, MUTED   # the HY index is the de-emphasised grey
NEG = "#e66767"      # drag / loss (DIVERGING, red end)
TINT_BLUE = "#cde2fb"
TINT_ORANGE = "#fadccd"
BOX_FILL = "#f4f3f0"
BAND = "#ecebe7"
MINUS = "−"


# ----------------------------------------------------------------------------------------------------------------
# Data: FRED cache
# ----------------------------------------------------------------------------------------------------------------
def _download(series_id):
    import urllib.request
    with urllib.request.urlopen(FRED + series_id, timeout=90) as r:
        text = r.read().decode()
    out = {}
    for row in csv.reader(text.strip().splitlines()[1:]):
        if len(row) == 2 and row[1].strip() not in ("", "."):
            out[row[0]] = float(row[1])
    return out


def build_cache():
    oas = {k: _download(v) for k, v in OAS_IDS.items()}
    tr = {k: _download(v) for k, v in TR_IDS.items()}
    dates = sorted(set.intersection(*[set(s) for s in oas.values()]))
    keep_tr = lambda d: any(a <= d <= b for a, b in TR_KEEP)
    os.makedirs(os.path.dirname(CACHE), exist_ok=True)
    with open(CACHE, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["date"] + [f"oas_{k}" for k in OAS_IDS] + [f"tr_{k}" for k in TR_IDS])
        for d in dates:
            w.writerow([d] + [oas[k][d] for k in OAS_IDS]
                       + [(tr[k].get(d, "") if keep_tr(d) else "") for k in TR_IDS])
    print(f"cached {len(dates)} rows -> {os.path.relpath(CACHE, os.path.join(HERE, '..', '..'))}")


def load_data(refresh=False):
    if refresh or not os.path.exists(CACHE):
        build_cache()
    dates, cols = [], {}
    with open(CACHE) as f:
        for row in csv.DictReader(f):
            dates.append(dt.datetime.strptime(row["date"], "%Y-%m-%d"))
            for k, v in row.items():
                if k != "date":
                    cols.setdefault(k, []).append(float(v) if v != "" else np.nan)
    return np.array(dates), {k: np.array(v) for k, v in cols.items()}


def _box(ax, cx, cy, w, h, text, sub=None, fill=BOX_FILL, edge=NEUTRAL, fs=9.2, subfs=8.0):
    ax.add_patch(FancyBboxPatch((cx - w / 2, cy - h / 2), w, h, boxstyle="round,pad=0,rounding_size=0.12",
                                facecolor=fill, edgecolor=edge, linewidth=1.1, zorder=2))
    two = bool(sub) and "\n" in sub
    ax.text(cx, cy + ((0.25 if two else 0.17) if sub else 0), text, ha="center", va="center", fontsize=fs,
            color=INK, fontweight="bold", zorder=3, linespacing=1.15)
    if sub:
        ax.text(cx, cy - (0.21 if two else 0.20), sub, ha="center", va="center", fontsize=subfs, color=INK_2,
                zorder=3, linespacing=1.2)


def _arrow(ax, p0, p1, color=INK_2, lw=1.4):
    ax.add_patch(FancyArrowPatch(p0, p1, arrowstyle="-|>", mutation_scale=10, linewidth=lw, color=color,
                                 shrinkA=0, shrinkB=0, zorder=4))


# ----------------------------------------------------------------------------------------------------------------
# Figure 12.1: five tabs, one population of borrowers (schematic)
# ----------------------------------------------------------------------------------------------------------------
def fig_same_bet_ownership():
    fig, ax = new_figure("wide")
    ax.set_xlim(0, 10)
    ax.set_ylim(0.3, 5.15)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.grid(False)

    xb, xc, xw = 1.35, 5.0, 8.65
    bw, cw, ww, bh = 2.35, 2.75, 2.7, 1.12
    yh, yt, yd = 3.95, 2.60, 1.20     # HY bond, term loan, direct loan rows
    yb1, yb2 = (yh + yt) / 2, yd

    for x, t in ((xb, "BORROWER"), (xc, "CLAIM ON THE BORROWER"), (xw, "WRAPPER THAT OWNS THE CLAIM")):
        ax.text(x, 4.95, t, ha="center", va="center", fontsize=7.6, color=MUTED, fontweight="bold")

    _box(ax, xb, yb1, bw, bh + 0.1, "Sponsor-backed\nsingle-B company")
    _box(ax, xb, yb2, bw, bh + 0.1, "Smaller company,\none size down")
    _box(ax, xc, yh, cw, bh, "HY bond", "senior notes\npost-default value ~39%", TINT_BLUE, BLUE)
    _box(ax, xc, yt, cw, bh, "Term loan B", "first lien\npost-default value ~52%", TINT_BLUE, BLUE)
    _box(ax, xc, yd, cw, bh, "Direct loan", "unitranche\npost-default value ~33%", TINT_BLUE, BLUE)
    _box(ax, xw, yt, ww, bh, "CLO BBB to B tranche", "owns pools of term loans", TINT_ORANGE, ORANGE)
    _box(ax, xw, yd, ww, bh, "Perpetual BDC", "owns direct loans; gates exits\nat 5% of NAV a quarter",
         TINT_ORANGE, ORANGE)

    # borrower -> claim ("issues")
    for yc in (yh, yt):
        _arrow(ax, (xb + bw / 2, yb1), (xc - cw / 2, yc))
    _arrow(ax, (xb + bw / 2, yb2), (xc - cw / 2, yd))
    # claim -> wrapper ("is owned by")
    for yc in (yt, yd):
        _arrow(ax, (xc + cw / 2, yc), (xw - ww / 2, yc))
        ax.text((xc + cw / 2 + xw - ww / 2) / 2, yc + 0.17, "held by", ha="center", va="bottom", fontsize=7.6,
                color=INK_2)
    ax.text(xb + bw / 2 + 0.2, yh + 0.12, "issues", ha="left", va="center", fontsize=7.6, color=INK_2)
    return finish(fig, "ch12_same_bet_ownership")


# ----------------------------------------------------------------------------------------------------------------
# Figure 12.2: the return identity as a waterfall (Nuveen Figure 3, with the cash rate implied by Figure 6)
# ----------------------------------------------------------------------------------------------------------------
def fig_identity_waterfall():
    fig, ax = new_figure("wide")
    yld, ecl, rates, spr = 6.97, 2.55, 0.37, 0.49
    ret = yld - ecl - rates - spr
    assert abs(ret - 3.56) < 1e-9
    fig6 = np.array([[5.11, 5.50, .26], [5.25, 5.52, .28], [5.50, 5.60, .33],
                     [5.75, 5.76, .36], [6.00, 6.05, .38], [6.20, 6.29, .40]])   # return, vol, Sharpe (Nuveen Fig. 6)
    cash = float(np.mean(fig6[:, 0] - fig6[:, 2] * fig6[:, 1]))
    assert 3.65 < cash < 3.72
    cash = 3.68

    names = ["Yield", "Expected\ncredit loss", "Rates\nmark-to-market", "Spread\nmark-to-market", "Forward\nreturn"]
    bottoms = [0, yld - ecl, yld - ecl - rates, ret, 0]
    heights = [yld, ecl, rates, spr, ret]
    colors = [BLUE, NEG, NEG, NEG, BLUE]
    x = np.arange(5)
    ax.hlines(cash, -0.55, 4.42, color=MUTED, linewidth=1.2, linestyle=(0, (4, 3)), zorder=1)
    ax.bar(x, heights, bottom=bottoms, width=0.62, color=colors, zorder=2)
    # connectors
    levels = [yld, yld - ecl, yld - ecl - rates, ret]
    for i, lv in enumerate(levels):
        ax.plot([i + 0.31, i + 1 - 0.31], [lv, lv], color=NEUTRAL, linewidth=0.9, zorder=1)
    labels = ["6.97", f"{MINUS}2.55", f"{MINUS}0.37", f"{MINUS}0.49"]
    tops = [yld, yld, yld - ecl, yld - ecl - rates]
    for i, (t, v) in enumerate(zip(tops, labels)):
        ax.text(i, t + 0.14, v, ha="center", va="bottom", fontsize=9, color=INK_2)
    ax.text(4, ret - 0.2, "3.56", ha="center", va="top", fontsize=9.5, color="white", fontweight="bold")
    ax.text(4.5, cash, "Implied cash rate\n(Nuveen Fig. 6)\nabout 3.68%", ha="left", va="center",
            fontsize=8, color=INK_2, linespacing=1.15)
    ax.set_xlim(-0.55, 5.6)
    ax.set_ylim(0, 7.8)
    ax.set_xticks(x)
    ax.set_xticklabels(names)
    ax.tick_params(axis="x", length=0)
    ax.set_ylabel("Annualized, five-year horizon (%)")
    return finish(fig, "ch12_return_identity_waterfall")


# ----------------------------------------------------------------------------------------------------------------
# Figure 12.3: the same optimizer with and without the constraints (Illustrative; Listings 12.1, 12.3, 12.5)
# ----------------------------------------------------------------------------------------------------------------
SECTORS = ["HY corp", "EM sov BB-B", "EM corp HY BB-B", "Lev loans", "CoCos", "Pref HY",
           "ABS other", "CMBS BBB", "CLO BBB-B", "MBS CRT", "MM direct lending"]
N = len(SECTORS)
TAB = dict(   # Listing 12.1 (illustrative inputs, decimals per year; bounds are Nuveen Figure 5)
    yld=np.array([.0697, .0750, .0720, .0800, .0680, .0700, .0600, .0850, .0950, .0780, .0975]),
    pd=np.array([.0425, .0300, .0350, .0400, .0150, .0180, .0100, .0350, .0380, .0230, .0500]),
    rec=np.array([.40, .40, .40, .52, .20, .30, .40, .30, .35, .35, .33]),
    dmod=np.array([3.2, 6.0, 3.8, .25, 4.5, 5.0, 2.5, 4.5, .25, .5, .25]),
    dspr=np.array([3.2, 6.0, 3.8, 4.0, 4.5, 5.0, 2.5, 4.5, 4.0, 3.5, 3.0]),
    spread=np.array([.030, .033, .034, .035, .030, .031, .015, .042, .055, .038, .060]),
    dspread_h=np.array([.0075, .003, .004, .005, .004, .004, .002, .006, .006, .004, .004]),
    tier=np.array(["ML", "ML", "LL", "LL", "ML", "ML", "LL", "LL", "LL", "LL", "IL"]),
    days=np.array([3, 3, 5, 10, 2, 4, 5, 10, 7, 5, 180], float),
    w_min=np.array([.20, .02, .02, .05, .02, .02, 0, 0, 0, 0, 0]),
    w_max=np.array([.60, .15, .15, .25, .10, .10, .10, .10, .10, .10, .35]),
)
HORIZON, D_RATES_H, CASH, GAMMA = 5.0, 0.0050, 0.0368, 8.0
SIG_U = np.array([.35, .40, .40, .35, .45, .40, .30, .45, .45, .40, .35])
B_LOAD = np.array([.90, .80, .85, .90, .80, .85, .70, .80, .85, .80, .90])
SIG_Y = 0.0080
BUDGET = {"type": "eq", "fun": lambda w: w.sum() - 1.0, "jac": lambda w: np.ones_like(w)}
OPTS = {"ftol": 1e-12, "maxiter": 2000}


def _engine_inputs():
    el = TAB["pd"] * (1 - TAB["rec"])                                            # eq. (12.1) loss term
    mu = (TAB["yld"] - el - TAB["dmod"] * D_RATES_H / HORIZON
          - TAB["dspr"] * TAB["dspread_h"] / HORIZON)
    dts = TAB["dspr"] * TAB["spread"]
    c1 = np.outer(B_LOAD, B_LOAD)
    np.fill_diagonal(c1, 1.0)
    sigma = np.outer(dts, dts) * np.outer(SIG_U, SIG_U) * c1 + SIG_Y ** 2 * np.outer(TAB["dmod"], TAB["dmod"])
    return mu, sigma


def _feasible_start(lo, hi):
    return lo + (1.0 - lo.sum()) / (hi - lo).sum() * (hi - lo)


def _mv(mu, sigma, lo, hi, tier=None):
    """Mean-variance: max w'mu - gamma/2 w'Sigma w; budget and bounds, plus (tier) the liquidity constraints."""
    cons = [BUDGET]
    if tier:
        il = (TAB["tier"] == "IL").astype(float)
        lq = np.isin(TAB["tier"], ["HL", "ML"]).astype(float)
        days = TAB["days"]
        cons += [{"type": "ineq", "fun": lambda w: 0.15 - il @ w, "jac": lambda w: -il},
                 {"type": "ineq", "fun": lambda w: lq @ w - 0.35, "jac": lambda w: lq},
                 {"type": "ineq", "fun": lambda w: 32.0 - days @ w, "jac": lambda w: -days}]
        x0 = _feasible_start(lo, np.where(il > 0, np.minimum(hi, 0.15), hi))
    else:
        x0 = np.full(N, 1.0 / N)
    f = lambda w: -(w @ mu - 0.5 * GAMMA * w @ sigma @ w)
    g = lambda w: -(mu - GAMMA * sigma @ w)
    res = minimize(f, x0, jac=g, bounds=list(zip(lo, hi)), constraints=cons, method="SLSQP", options=OPTS)
    w = res.x
    assert abs(w.sum() - 1) < 1e-7 and np.all(w >= lo - 1e-8) and np.all(w <= hi + 1e-8)
    if tier:
        assert w[TAB["tier"] == "IL"].sum() <= 0.15 + 1e-7 and w @ TAB["days"] <= 32 + 1e-6
    return w


def fig_constraints_decide():
    mu, sigma = _engine_inputs()
    assert abs(mu[0] - 0.0362) < 5e-5 and abs(mu[8] - 0.0653) < 5e-5            # Listing 12.1 output quoted in 12.10
    assert abs(np.sqrt(sigma[10, 10]) - 0.0630) < 5e-4                          # direct-lending vol, Listing 12.3
    lo, hi = TAB["w_min"], TAB["w_max"]
    rng = np.random.default_rng(12)
    n_draw, sd = 400, 0.0025                                                    # 25 bp of error per sector
    free, tiered = [], []
    for _ in range(n_draw):
        m = mu + rng.normal(0.0, sd, N)
        free.append(_mv(m, sigma, np.zeros(N), np.ones(N)))
        tiered.append(_mv(m, sigma, lo, hi, tier=True))
    free, tiered = np.array(free) * 100, np.array(tiered) * 100
    mean_move = lambda W: float((np.abs(W - np.median(W, 0)).sum(1) / 2).mean())
    print(f"  mean one-way weight move: free {mean_move(free):.1f} pp, constrained {mean_move(tiered):.1f} pp")

    fig, axs = new_figure("wide", ncols=2)
    y = np.arange(N)[::-1]
    for ax, W, col, ttl in ((axs[0], free, BLUE, "Budget and long-only"),
                            (axs[1], tiered, ORANGE, "Plus bounds and liquidity tiers")):
        ax.set_title(f"{ttl}\n{mean_move(W):.1f}% of NAV moves on average".replace(".0%", "%"), fontsize=9,
                     loc="left", linespacing=1.3)
        ax.grid(False)
        ax.grid(axis="x")
        if ax is axs[1]:
            for yi, a, b in zip(y, lo * 100, hi * 100):
                ax.barh(yi, b - a, left=a, height=0.62, color=BAND, zorder=1)
        p5, p50, p95 = (np.percentile(W, q, axis=0) for q in (5, 50, 95))
        for yi, a, m_, b in zip(y, p5, p50, p95):
            ax.plot([a, b], [yi, yi], color=col, linewidth=3.0, solid_capstyle="butt", zorder=3)
            ax.plot([m_], [yi], "o", color="white", markeredgecolor=col, markeredgewidth=1.6, markersize=6, zorder=4)
        ax.set_xlim(-2, 75)
        ax.set_xlabel("Weight (% of NAV)")
        ax.set_ylim(-0.7, N - 0.3)
        ax.set_yticks(y)
        ax.set_yticklabels(SECTORS)
        ax.tick_params(axis="y", length=0, labelsize=8, labelleft=(ax is axs[0]))
        ax.spines["left"].set_visible(False)
    axs[1].legend(handles=[Patch(facecolor=BAND, label="allowed range"),
                           Line2D([0], [0], color=ORANGE, lw=3, label="5th to 95th percentile"),
                           Line2D([0], [0], marker="o", color="none", markerfacecolor="white",
                                  markeredgecolor=ORANGE, markeredgewidth=1.6, markersize=6, label="median")],
                  loc="lower right", fontsize=7.6, handlelength=1.4, borderaxespad=0.2)
    return finish(fig, "ch12_constraints_decide")


# ----------------------------------------------------------------------------------------------------------------
# Figure 12.4: April 2025, daily versus month-end (real data)
# ----------------------------------------------------------------------------------------------------------------
def _month_end_idx(dates, lo, hi):
    """Index of the last observation of each calendar month with lo <= date <= hi."""
    idx = [i for i, d in enumerate(dates) if lo <= d <= hi]
    out = []
    for i in idx:
        nxt = dates[i + 1] if i + 1 < len(dates) else None
        if nxt is None or nxt.month != dates[i].month:
            out.append(i)
    return out


def _drawdown(dates, tr, lo, hi):
    """Peak-to-trough return (%) of an index within [lo, hi] and the dates."""
    sel = [i for i, d in enumerate(dates) if lo <= d <= hi]
    s = tr[sel]
    dd = s / np.maximum.accumulate(s) - 1.0
    k = int(np.argmin(dd))
    pk = int(np.argmax(s[:k + 1]))
    return 100 * dd[k], dates[sel[pk]], dates[sel[k]]


def fig_april_2025(dates, d):
    lo, hi = dt.datetime(2025, 1, 2), dt.datetime(2025, 6, 30)
    sel = np.array([lo <= x <= hi for x in dates])
    xs, hy = dates[sel], d["oas_HY"][sel] * 100
    me = _month_end_idx(dates, lo, hi)
    mx, my = dates[me], d["oas_HY"][me] * 100

    fig, axs = new_figure("wide", ncols=2, gridspec_kw={"width_ratios": [1.55, 1]})
    ax = axs[0]
    ax.plot(xs, hy, color=BLUE, linewidth=LW, zorder=3)
    ax.plot(mx, my, color=ORANGE, linewidth=1.1, linestyle=(0, (3, 2)), zorder=2)
    ax.plot(mx, my, "o", color=ORANGE, markersize=6.5, markeredgecolor="white", markeredgewidth=0.8, zorder=4)
    i7 = int(np.argmax(hy))
    assert xs[i7] == dt.datetime(2025, 4, 7) and round(hy[i7]) == 461
    ax.annotate("461 bp, April 7", (xs[i7], hy[i7]), xytext=(-24, -2), textcoords="offset points", ha="right",
                va="center", fontsize=8.3, color=INK_2, arrowprops=dict(arrowstyle="-", color=NEUTRAL, lw=0.8))
    i22 = int(np.argmin(np.abs(xs - dt.datetime(2025, 1, 22))))
    assert round(hy[i22]) == 259
    ax.annotate("259 bp\nJanuary 22", (xs[i22], hy[i22]), xytext=(-2, 42), textcoords="offset points", ha="center",
                va="bottom", fontsize=8.3, color=INK_2, arrowprops=dict(arrowstyle="-", color=NEUTRAL, lw=0.8))
    # label the month-end prints that matter
    for dd_, v, dx, dy, ha_ in ((dt.datetime(2025, 3, 31), 355, -6, 9, "right"),
                               (dt.datetime(2025, 4, 30), 394, 7, 8, "left")):
        j = [k for k, x in enumerate(mx) if x.date() == dd_.date()][0]
        assert round(my[j]) == v, (my[j], v)
        ax.annotate(f"{v}", (mx[j], my[j]), xytext=(dx, dy), textcoords="offset points", ha=ha_, va="center",
                    fontsize=8.3, color=INK_2)
    assert round(my.max()) == 394
    ax.set_ylim(200, 500)
    ax.set_xlim(lo - dt.timedelta(days=3), hi + dt.timedelta(days=3))
    ax.xaxis.set_major_locator(mdates.MonthLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b"))
    ax.set_ylabel("HY OAS (bp)")
    ax.set_xlabel("2025")
    ax.legend(handles=[Line2D([0], [0], color=BLUE, lw=LW, label="Daily"),
                       Line2D([0], [0], color=ORANGE, lw=1.1, ls=(0, (3, 2)), marker="o", markersize=6,
                              markeredgecolor="white", label="Month-end print")],
              loc="upper right", fontsize=8, handlelength=2.2)

    # right: peak-to-trough by bucket
    ax = axs[1]
    rows = []
    for k, lab, col in (("BB", "BB", C_BB), ("HY", "HY index", C_HY), ("B", "B", C_B), ("CCC", "CCC", C_CCC)):
        v, pk, tr_ = _drawdown(dates, d[f"tr_{k}"], dt.datetime(2025, 2, 1), dt.datetime(2025, 5, 15))
        print(f"  {k}: peak-to-trough {v:.2f}% ({pk.date()} to {tr_.date()})")
        rows.append((lab, v, col))
    assert [round(v, 2) for _, v, _ in rows] == [-2.83, -3.83, -4.21, -7.80]
    yy = np.arange(len(rows))[::-1]
    ax.grid(False)
    ax.grid(axis="x")
    for yi, (lab, v, col) in zip(yy, rows):
        ax.barh(yi, v, height=0.62, color=col, zorder=2)
        ax.text(v - 0.2, yi, f"{MINUS}{abs(v):.2f}%", ha="right", va="center", fontsize=8.5, color=INK_2)
    ax.set_yticks(yy)
    ax.set_yticklabels([r[0] for r in rows])
    ax.tick_params(axis="y", length=0)
    ax.spines["left"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.set_xlim(-9.6, 0)
    ax.xaxis.set_major_formatter(lambda x, _: f"{MINUS}{abs(x):.0f}" if x else "0")
    ax.set_xlabel("Peak-to-trough total return (%)")
    return finish(fig, "ch12_april_2025_daily_vs_month_end")


# ----------------------------------------------------------------------------------------------------------------
# Figure 12.5: the 2026 CCC/BB split (real data)
# ----------------------------------------------------------------------------------------------------------------
def fig_ccc_bb_split(dates, d):
    fig, axs = new_figure("wide", ncols=2, gridspec_kw={"width_ratios": [1.7, 1]})
    ax = axs[0]
    series = (("HY", "HY index", C_HY, 1.0), ("BB", "BB", C_BB, LW), ("B", "B", C_B, LW), ("CCC", "CCC", C_CCC, LW))
    last = {}
    for k, lab, col, lw in series:
        v = d[f"oas_{k}"] * 100
        ax.plot(dates, v, color=col, linewidth=lw, zorder=4 if k == "HY" else 3)
        last[k] = v[-1]
    assert round(last["CCC"]) == 1278 and round(last["BB"]) == 197 and round(last["HY"]) == 323
    xe = dates[-1]
    for k, lab, col, dy in (("CCC", "CCC 1,278", C_CCC, 0), ("B", "B 326", C_B, 6), ("HY", "HY 323", C_HY, -6),
                            ("BB", "BB 197", C_BB, -8)):
        label_end(ax, xe, last[k], lab, col, dx=5, dy=dy)
    mark_event(ax, dt.datetime(2025, 4, 7), "April 7, 2025", y_frac=0.95)
    ax.set_xlim(dates[0], xe)
    ax.set_ylim(0, 1400)
    ax.yaxis.set_major_formatter(lambda x, _: f"{x:,.0f}")
    ax.xaxis.set_major_locator(mdates.MonthLocator(bymonth=(1, 7)))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b\n%Y"))
    ax.set_ylabel("OAS (bp)")
    ax.margins(x=0)

    ax = axs[1]
    d0, d1 = dt.datetime(2025, 12, 31), dt.datetime(2026, 10, 15)
    i0, i1 = int(np.where(dates == d0)[0][0]), int(np.where(dates == d1)[0][0])
    rows = []
    for k, lab, col in (("BB", "BB", C_BB), ("HY", "HY index", C_HY), ("B", "B", C_B), ("CCC", "CCC", C_CCC)):
        s = d[f"tr_{k}"]
        rows.append((lab, 100 * (s[i1] / s[i0] - 1), col))
        print(f"  {k}: total return Dec 31 2025 to Oct 15 2026 = {rows[-1][1]:+.2f}%")
    assert [round(v, 2) for _, v, _ in rows] == [0.33, 0.15, 1.20, -5.21]
    yy = np.arange(len(rows))[::-1]
    ax.grid(False)
    ax.grid(axis="x")
    ax.axvline(0, color=NEUTRAL, linewidth=0.9, zorder=1)
    for yi, (lab, v, col) in zip(yy, rows):
        ax.barh(yi, v, height=0.62, color=col, zorder=2)
        txt = f"{MINUS if v < 0 else '+'}{abs(v):.2f}%"
        ax.text(v + (0.25 if v >= 0 else -0.25), yi, txt, ha="left" if v >= 0 else "right", va="center",
                fontsize=8.5, color=INK_2)
    ax.set_yticks(yy)
    ax.set_yticklabels([r[0] for r in rows])
    ax.tick_params(axis="y", length=0)
    ax.spines["left"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.set_xlim(-8.2, 3.6)
    ax.set_xticks([-6, -4, -2, 0, 2])
    ax.xaxis.set_major_formatter(lambda x, _: f"{MINUS}{abs(x):.0f}" if x < 0 else f"{x:.0f}")
    ax.set_xlabel("Total return, 2026 to date (%)")
    return finish(fig, "ch12_ccc_bb_split")


def main():
    refresh = "--refresh" in sys.argv
    dates, d = load_data(refresh)
    print(f"data: {dates[0].date()} to {dates[-1].date()}, {len(dates)} rows")
    fig_same_bet_ownership()
    fig_identity_waterfall()
    fig_constraints_decide()
    fig_april_2025(dates, d)
    fig_ccc_bb_split(dates, d)


if __name__ == "__main__":
    main()
