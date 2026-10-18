"""Chapter 22 figures: market-structure regulation and the forces reshaping liquidity.

Run from anywhere:  python3 tools/figures/ch22.py   (writes assets/figures/ch22_*.png)

Figures
  ch22_rule_timeline          dated rule changes on the three inputs a dealer sells (section 22.1)
  ch22_regulatory_rent        eq. (22.1) rent vs risk weight and eq. (22.4) breakeven hold (section 22.1.1)
  ch22_dealer_inventory       NY Fed primary-dealer net corporate-bond positions, 2015-2026 (section 22.1)
  ch22_block_spread_delay     eq. (22.6) block half-spread vs reporting delay (section 22.2.1)
  ch22_netting_factor         eq. (22.10)-(22.11) netting factor vs number of counterparties (section 22.4.1)

Data
  Real: NY Fed Primary Dealer Statistics (FR 2004), series PDPOSCSBND-* (net = long minus short, $mm,
  weekly). A cached copy lives in tools/figures/data/; delete it to re-download.
  Everything else is generated from the closed forms and parameters stated in the chapter (illustrative),
  or from dates quoted in the chapter.
"""
import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from style import *            # applies the rcParams on import

import datetime as dt
import math
import subprocess

import matplotlib.dates as mdates
import numpy as np
import pandas as pd
from matplotlib.lines import Line2D

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
PD_CSV = os.path.join(DATA_DIR, "ch22_nyfed_pd_corp_bond_net.csv")
PD_IG = ["L13", "G13", "G5L10", "G10"]
PD_HY = ["BELL13", "BELG13", "BELG5L10", "BELG10"]

# The three inputs a dealer sells (the chapter's organizing idea) keep one color in every figure:
C_BALANCE, C_TIME, C_INFO = BLUE, ORANGE, AQUA


def D(s):
    return dt.datetime.strptime(s, "%Y-%m-%d")


# --------------------------------------------------------------------------------------------------
# Figure: timeline of rule changes
# --------------------------------------------------------------------------------------------------
def fig_rule_timeline():
    fig, ax = new_figure((7.0, 5.6))
    ax.grid(False)
    ax.spines["left"].set_visible(False)
    ax.set_yticks([])
    x0, x1 = D("2018-03-01"), D("2030-03-01")
    ax.set_xlim(x0, x1)
    ax.set_ylim(-3.55, 9.0)
    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))

    lanes = {  # center y, color, name
        "balance": (6.0, C_BALANCE, "Balance sheet"),
        "time": (2.8, C_TIME, "Time"),
        "info": (0.0, C_INFO, "Information"),
    }
    today = D("2026-10-18")
    ax.axvspan(today, x1, color="#f1f0ec", zorder=0)
    ax.text(today, 8.75, " Oct 2026", fontsize=7.5, color=MUTED, va="top", ha="left")

    for key, (y, col, name) in lanes.items():
        ax.plot([x0, x1], [y, y], color=col, linewidth=1.2, alpha=0.55, zorder=2, solid_capstyle="butt")
        ax.text(D("2018-04-15"), y + 0.12, name, fontsize=8.5, color=INK, va="bottom", ha="left",
                fontweight="bold")

    # Market stresses that hit every bond at once (the confounders of section 22.8)
    for a, b, lab in [("2020-03-09", "2020-03-31", "Mar 2020\ndash for cash"),
                      ("2023-03-08", "2023-03-31", "Mar 2023\nbank failures"),
                      ("2025-04-02", "2025-04-30", "Apr 2025\ntariff shock")]:
        ax.axvspan(D(a), D(b), ymin=0, ymax=1, color=NEUTRAL, alpha=0.35, zorder=0.5, linewidth=0)
        ax.text(D(a) + (D(b) - D(a)) / 2, -3.45, lab, fontsize=7, color=MUTED, ha="center", va="bottom")

    def ev(date, lane, text, dy, status="live", ha="left", dx=0):
        y0, col, _ = lanes[lane]
        x = D(date)
        ytxt = y0 + dy
        ax.plot([x, x], [y0, ytxt - (0.05 if dy > 0 else -0.05)], color=col, linewidth=0.8, zorder=2)
        if status == "live":
            ax.plot([x], [y0], "o", color=col, markersize=6, zorder=4)
        elif status == "pending":
            ax.plot([x], [y0], "o", markerfacecolor="white", markeredgecolor=col, markeredgewidth=1.6,
                    markersize=6, zorder=4)
        else:  # never in force
            ax.plot([x], [y0], "X", color=INK_2, markersize=7, zorder=4)
        va = "bottom" if dy > 0 else "top"
        off = (2 if ha == "left" else -2) + dx
        ax.annotate(text, (x, ytxt), xytext=(off, 0), textcoords="offset points", ha=ha, va=va,
                    fontsize=7.4, color=INK_2, linespacing=1.15)

    # Balance sheet lane
    y0, col, _ = lanes["balance"]
    ax.plot([D("2020-04-01"), D("2021-03-31")], [y0, y0], color=col, linewidth=6, solid_capstyle="butt",
            zorder=3)
    ax.plot([D("2020-04-01"), D("2020-04-01")], [y0, y0 + 0.55], color=col, linewidth=0.8, zorder=2)
    ax.annotate("Apr 2020 to Mar 2021:\nSLR excludes Treasuries", (D("2020-04-01"), y0 + 0.55), xytext=(2, 0),
                textcoords="offset points", ha="left", va="bottom", fontsize=7.4, color=INK_2, linespacing=1.15)
    ev("2023-07-27", "balance", "Jul 2023: Basel III endgame\nproposed (+16% CET1)", 0.55, "pending")
    ev("2024-09-10", "balance", "Sep 2024: re-proposal\n(+9% for G-SIBs)", -0.55, "pending", ha="right")
    ev("2026-03-19", "balance", "Mar 2026: re-proposal,\ncapital \"modestly\" lower", 1.55, "pending", ha="right")
    ev("2026-04-01", "balance", "Apr 2026: eSLR in force\n(final Nov 2025)", -0.55, "live")
    ev("2026-12-31", "balance", "Treasury clearing due:\ncash Dec 2026, repo Jun 2027", 0.55, "pending")
    ax.plot([D("2026-12-31"), D("2027-06-30")], [y0, y0], color=col, linewidth=1.2, zorder=3)
    ax.plot([D("2027-06-30")], [y0], "o", markerfacecolor="white", markeredgecolor=col, markeredgewidth=1.6,
            markersize=6, zorder=4)

    # Time lane
    ev("2020-01-01", "time", "Jan 2020: Volcker 2.0\ntakes effect", 0.55, "live")
    ev("2024-05-28", "time", "May 2024: T+1\nsettlement", 0.55, "live")
    ev("2027-10-11", "time", "Oct 2027: EU and UK\nT+1 (approx.)", 0.55, "pending")

    # Information lane
    ev("2022-02-14", "info", "Feb 2022: SBSR\npublic CDS prints", 0.55, "live")
    ev("2023-05-15", "info", "May 2023: portfolio-trade\nmodifier mandatory", -0.55, "live")
    ev("2024-03-25", "info", "Mar 2024: Treasury EOD\ndissemination (approx.)", 1.55, "live")
    ev("2025-12-04", "info", "Dec 2025: 1-minute rule\ndropped (placebo)", -1.55, "never", ha="right")
    ev("2026-06-08", "info", "Jun 2026: allocation\nreports (optional)", 0.55, "live", ha="right")
    ev("2027-08-02", "info", "Aug 2027: affiliate\nindicator mandatory", 0.55, "pending", ha="left")

    handles = [
        Line2D([], [], marker="o", linestyle="", color=INK_2, markersize=6, label="in force"),
        Line2D([], [], marker="o", linestyle="", markerfacecolor="white", markeredgecolor=INK_2,
               markeredgewidth=1.6, markersize=6, label="proposed, adopted or scheduled"),
        Line2D([], [], marker="X", linestyle="", color=INK_2, markersize=7, label="approved, never in force"),
    ]
    fig.legend(handles=handles, loc="outside lower center", ncol=3, fontsize=8)
    return finish(fig, "ch22_rule_timeline")


# --------------------------------------------------------------------------------------------------
# Figure: regulatory rent kink (22.1) and breakeven holding period (22.4)
# --------------------------------------------------------------------------------------------------
def fig_regulatory_rent():
    h, k_rwa = 0.12, 0.105

    def rent_bp(rw, k_lr):
        return 1e4 * h * np.maximum(k_rwa * np.asarray(rw), k_lr)

    fig, (a, b) = new_figure(ncols=2, gridspec_kw={"width_ratios": [1.3, 1]})
    rw = np.linspace(0, 1.5, 301)
    a.plot(rw * 100, rent_bp(rw, 0.05), color=NEUTRAL, linewidth=2.2, zorder=2)
    a.plot(rw * 100, rent_bp(rw, 0.0375), color=BLUE, linewidth=LW, zorder=3)
    for k_lr, col in [(0.05, NEUTRAL), (0.0375, BLUE)]:
        sw = k_lr / k_rwa * 100
        a.plot([sw], [rent_bp(sw / 100, k_lr)], "o", color=col, markeredgecolor="white", markersize=6, zorder=5)
    a.annotate("Switching point:\n47.6% before, 35.7% after", (47.6, 60), xytext=(63, 36), textcoords="data",
               fontsize=8, color=INK_2, va="center",
               arrowprops=dict(arrowstyle="-", color=MUTED, linewidth=0.7, shrinkA=0, shrinkB=3))
    a.text(2, 64, "Before: $\\kappa_{LR}$ = 5%", fontsize=8, color=INK_2, ha="left", va="bottom")
    a.text(2, 40, "After: $\\kappa_{LR}$ = 3.75%", fontsize=8, color=BLUE, ha="left", va="top")
    a.plot([100], [rent_bp(1.0, 0.0375)], "o", color=BLUE, markeredgecolor="white", markersize=6, zorder=5)
    a.annotate("10-yr BBB, RW 100%: 126bp", (100, 126), xytext=(-8, 6), textcoords="offset points", fontsize=8,
               color=INK_2, ha="right", va="bottom")
    a.text(2, 12, "2-yr Treasury (RW near 0):\n60bp before, 45bp after", fontsize=8, color=INK_2, va="center")
    a.set_xlabel("Equivalent risk weight (%)")
    a.set_ylabel("Rent $c_{reg}$ (bp per year)")
    a.set_xlim(0, 150)
    a.set_ylim(0, 200)

    labels = ["2-yr Treasury,\nbefore 2026", "2-yr Treasury,\nafter 2026", "10-yr BBB"]
    half = [0.5, 0.5, 12.5]
    c = [rent_bp(0, 0.05), rent_bp(0, 0.0375), rent_bp(1.0, 0.0375)]
    days = [hs / cc * 365 for hs, cc in zip(half, c)]
    ypos = [2, 1, 0]
    b.barh(ypos, days, height=0.6, color=[NEUTRAL, BLUE, BLUE], zorder=3)
    for yp, d in zip(ypos, days):
        b.text(d + 0.8, yp, f"{d:.0f} days" if d > 10 else f"{d:.1f} days", va="center", fontsize=8.5, color=INK_2,
               zorder=6, bbox=dict(boxstyle="square,pad=0.15", fc="white", ec="none"))
    b.axvline(7, color=NEUTRAL, linewidth=0.9, linestyle=(0, (3, 3)), zorder=1)
    b.text(7.6, 2.62, "1-week hold", fontsize=8, color=INK_2, va="center")
    b.set_yticks(ypos)
    b.set_yticklabels(labels, fontsize=8.5)
    b.tick_params(axis="y", length=0)
    b.grid(axis="y", visible=False)
    b.grid(axis="x", visible=True)
    b.set_xlim(0, 48)
    b.set_ylim(-0.55, 2.95)
    b.set_xlabel("Breakeven holding period $\\tau^*$ (days)")
    return finish(fig, "ch22_regulatory_rent")


# --------------------------------------------------------------------------------------------------
# Figure: NY Fed primary dealer net corporate bond positions (real data)
# --------------------------------------------------------------------------------------------------
def _fetch_pd():
    frames = {}
    for k in PD_IG + PD_HY:
        url = f"https://markets.newyorkfed.org/api/pd/get/PDPOSCSBND-{k}.json"
        raw = subprocess.run(["curl", "-sS", "-m", "90", url], capture_output=True, text=True, check=True).stdout
        import json
        rows = json.loads(raw)["pd"]["timeseries"]
        frames[k] = pd.Series({pd.Timestamp(r["asofdate"]): float(r["value"]) for r in rows
                               if r["value"] not in ("*", "")})
    df = pd.DataFrame(frames).sort_index().dropna()
    out = pd.DataFrame({"ig_net_mm": df[PD_IG].sum(axis=1), "hy_net_mm": df[PD_HY].sum(axis=1)})
    out["total_net_mm"] = out.ig_net_mm + out.hy_net_mm
    out.index.name = "asofdate"
    os.makedirs(DATA_DIR, exist_ok=True)
    out.to_csv(PD_CSV)
    return out


def load_pd():
    if not os.path.exists(PD_CSV):
        return _fetch_pd()
    return pd.read_csv(PD_CSV, parse_dates=["asofdate"], index_col="asofdate")


def fig_dealer_inventory():
    df = load_pd() / 1000.0                           # $bn
    ma = df.rolling(13, min_periods=13).mean()
    fig, ax = new_figure()
    ax.plot(df.index, df.total_net_mm, color=NEUTRAL, linewidth=0.8, zorder=2)
    ax.plot(ma.index, ma.total_net_mm, color=BLUE, linewidth=LW, zorder=4)
    ax.plot(ma.index, ma.ig_net_mm, color=ORANGE, linewidth=LW, zorder=3)
    ax.axhline(0, color=INK_2, linewidth=0.8, zorder=1)
    ax.set_ylim(-14, 28)
    ax.set_xlim(D("2015-01-01"), D("2028-03-01"))
    ax.set_ylabel("Net position, long minus short ($bn)")

    mark_event(ax, D("2020-03-23"), "Mar 2020: SMCCF,\nSLR exclusion", y_frac=0.985)
    mark_event(ax, D("2023-07-27"), "Endgame\nproposed", y_frac=0.985)
    mark_event(ax, D("2025-11-25"), "eSLR\nfinal", y_frac=0.985)

    y17 = df.loc["2017", "total_net_mm"].mean()
    y26 = df.loc["2026", "total_net_mm"].mean()
    i26 = df.loc["2026", "ig_net_mm"].mean()
    ax.annotate(f"2017 average: +${y17:.1f}bn", (D("2017-07-01"), y17), xytext=(0, 24),
                textcoords="offset points", fontsize=8, color=INK_2, ha="center",
                arrowprops=dict(arrowstyle="-", color=MUTED, linewidth=0.7, shrinkA=0, shrinkB=2))
    ax.plot([D("2017-01-01"), D("2017-12-31")], [y17, y17], color=INK_2, linewidth=1.0, zorder=5)
    ax.plot([D("2026-01-01"), df.index[-1]], [y26, y26], color=INK_2, linewidth=1.0, zorder=5)
    ax.annotate(f"2026 to date: {y26:+.1f}bn\n(IG only {i26:+.1f}bn)".replace("+", "+$").replace("-", "-$"),
                (D("2026-05-15"), y26), xytext=(-8, -52), textcoords="offset points", fontsize=8,
                color=INK_2, ha="center",
                arrowprops=dict(arrowstyle="-", color=MUTED, linewidth=0.7, shrinkA=0, shrinkB=2))

    last = ma.index[-1]
    ax.text(D("2015-03-01"), 24.2, "Weekly total", fontsize=8, color=MUTED, va="center")
    label_end(ax, last, ma.total_net_mm.iloc[-1], "All corp. bonds\n(13-wk avg)", BLUE, dx=5, dy=9)
    label_end(ax, last, ma.ig_net_mm.iloc[-1], "IG only\n(13-wk avg)", ORANGE, dx=5, dy=-11)
    return finish(fig, "ch22_dealer_inventory")


# --------------------------------------------------------------------------------------------------
# Figure: block half-spread vs reporting delay (22.6)
# --------------------------------------------------------------------------------------------------
def block_half_spread(delay, t_unwind, lam=0.5, q=15.0, sigma=2.5, gamma=0.001):
    leak = lam * q * np.maximum(1.0 - np.asarray(delay, dtype=float) / t_unwind, 0.0)
    return leak + gamma * sigma ** 2 * q * t_unwind / 6.0


def fig_block_spread_delay():
    delay = np.logspace(np.log10(0.5), np.log10(3500), 500)
    fig, ax = new_figure()
    shades = {15: SEQ_BLUE_STEPS[5], 120: SEQ_BLUE_STEPS[7], 600: SEQ_BLUE_STEPS[10]}
    for tu, col in shades.items():
        ax.plot(delay, block_half_spread(delay, tu), color=col, linewidth=LW, zorder=3)
    ax.set_xscale("log")
    ax.set_xlim(0.5, 3500)
    ax.set_ylim(0, 21)
    ax.set_yticks([0, 5, 10, 15, 20])
    ax.set_xticks([1, 15, 60, 600, 2880])
    ax.set_xticklabels(["1 min", "15 min", "1 hour", "10 hours", "48 hours"])
    ax.xaxis.set_minor_locator(matplotlib_ticker_null())
    ax.set_xlabel("Reporting delay $\\Delta$ (log scale)")
    ax.set_ylabel("Competitive block half-spread (bp)")

    mark_event(ax, 1, "1-minute rule\n(never in force)", y_frac=0.985)
    mark_event(ax, 15, "Today: 15 min", y_frac=0.985)
    ax.axvline(2880, color=NEUTRAL, linewidth=0.9, linestyle=(0, (3, 3)), zorder=1)
    ax.annotate("2019 pilot:\n48 hours", (2880, 0.985), xycoords=("data", "axes fraction"), xytext=(-3, 0),
                textcoords="offset points", fontsize=8, color=INK_2, va="top", ha="right")

    lab = dict(fontsize=8, color=INK_2, va="bottom", ha="left",
               bbox=dict(boxstyle="square,pad=0.1", fc="white", ec="none"))
    ax.text(0.6, 5.7, "$T_u$ = 15 min:\nzero leak once $\\Delta \\geq T_u$", **{**lab, "va": "top"})
    ax.text(0.6, 9.9, "$T_u$ = 2 hours", **lab)
    ax.text(0.6, 17.3, "$T_u$ = 10 hours", **lab)
    pts = [(1, block_half_spread(1, 120)), (15, block_half_spread(15, 120))]
    for x, y in pts:
        ax.plot([x], [y], "o", color=shades[120], markeredgecolor="white", markersize=6, zorder=5)
    ax.annotate("9.31bp at 1 min,\n8.44bp at 15 min", (15, pts[1][1]), xytext=(34, 12.2), fontsize=8,
                color=INK_2, ha="left", va="center",
                arrowprops=dict(arrowstyle="-", color=MUTED, linewidth=0.7, shrinkA=0, shrinkB=4))
    ax.text(3300, 4.3, "Flat segments: inventory floor\n$\\gamma\\sigma^2 Q T_u/6$, untouched by the delay",
            fontsize=8, color=MUTED, ha="right", va="bottom")
    return finish(fig, "ch22_block_spread_delay")


def matplotlib_ticker_null():
    from matplotlib.ticker import NullLocator
    return NullLocator()


# --------------------------------------------------------------------------------------------------
# Figure: netting factor vs number of counterparties (22.10, 22.11)
# --------------------------------------------------------------------------------------------------
def folded_mean(a, b):
    """E|a + bZ| for standard normal Z."""
    return b * math.sqrt(2 / math.pi) * math.exp(-a * a / (2 * b * b)) + a * math.erf(a / (b * math.sqrt(2)))


def netting_factor(n, m_over_s):
    """Exact phi(N) of section 22.4.1 with sigma_x = 1 and common component m."""
    k = n - 1
    return folded_mean(k * m_over_s, math.sqrt(k)) / (k * folded_mean(m_over_s, 1.0))


def fig_netting_factor():
    n = np.logspace(np.log10(2), np.log10(200), 160)
    fig, ax = new_figure()
    cases = [(0.0, SEQ_BLUE_STEPS[5], "$m$ = 0: two-way market"),
             (0.5, SEQ_BLUE_STEPS[7], "$m$ = 0.5$\\sigma_x$"),
             (1.0, SEQ_BLUE_STEPS[10], "$m$ = $\\sigma_x$: one-way tilt")]
    for m, col, lab in cases:
        phi = np.array([netting_factor(k, m) for k in n])
        ax.plot(n, phi, color=col, linewidth=LW, zorder=3)
        if m > 0:
            floor = abs(m) / folded_mean(m, 1.0)
            ax.plot([2, 200], [floor, floor], color=col, linewidth=0.9, linestyle=(0, (1, 2)), zorder=2)
    ax.set_xscale("log")
    ax.set_xlim(2, 700)
    ax.set_ylim(0, 1.05)
    ax.set_xticks([2, 5, 10, 25, 50, 100, 200])
    ax.set_xticklabels(["2", "5", "10", "25", "50", "100", "200"])
    ax.xaxis.set_minor_locator(matplotlib_ticker_null())
    ax.set_xlabel("Number of dealers $N$ (log scale)")
    ax.set_ylabel("Netting factor $\\phi(N)$: net exposure / gross")

    ax.plot([25], [netting_factor(25, 0.0)], "o", color=SEQ_BLUE_STEPS[5], markeredgecolor="white", markersize=6,
            zorder=5)
    ax.annotate("0.204 at $N$ = 25", (25, netting_factor(25, 0.0)), xytext=(8, 0.07), textcoords="data",
                fontsize=8, color=INK_2, ha="left",
                arrowprops=dict(arrowstyle="-", color=MUTED, linewidth=0.7, shrinkA=0, shrinkB=4))
    ax.plot([2, 200], [0.54, 0.54], color=NEUTRAL, linewidth=0.9, linestyle=(0, (3, 3)), zorder=1)
    ax.text(200, 0.54 - 0.014, "DTCC Sponsored Service read: about 0.54", fontsize=8, color=INK_2, va="top", ha="right")
    label_end(ax, 200, netting_factor(200, 0.0), "$m$ = 0\n(two-way)", SEQ_BLUE_STEPS[5], dx=5)
    label_end(ax, 200, netting_factor(200, 0.5), "$m$ = 0.5$\\sigma_x$\nfloor 0.558", SEQ_BLUE_STEPS[7], dx=5, dy=4)
    label_end(ax, 200, netting_factor(200, 1.0), "$m$ = $\\sigma_x$\nfloor 0.857", SEQ_BLUE_STEPS[10], dx=5)
    return finish(fig, "ch22_netting_factor")


FIGS = [fig_rule_timeline, fig_regulatory_rent, fig_dealer_inventory, fig_block_spread_delay, fig_netting_factor]

if __name__ == "__main__":
    wanted = set(sys.argv[1:])
    for f in FIGS:
        if not wanted or f.__name__.replace("fig_", "") in wanted:
            f()
