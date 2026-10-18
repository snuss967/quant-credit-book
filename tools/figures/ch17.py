"""Figures for Chapter 17 (Private Credit & the Public-Private Convergence).

Run:  python3 tools/figures/ch17.py   -> assets/figures/ch17_*.png

Colour use in this chapter: BLUE is the reported, marked or private-side series; ORANGE is the true value,
the market observation or the comparison group; NEUTRAL carries reference lines. Time-ordered bars use one
blue hue, light to dark (SEQ_BLUE).
"""
import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from style import *  # noqa: E402,F401,F403  (applies the rcParams on import)

import datetime as dt  # noqa: E402

import matplotlib.dates as mdates  # noqa: E402
import numpy as np  # noqa: E402


# --------------------------------------------------------------------------------------------------
# Figure 17.1: US private-credit loans by holder, Z.1 (section 17.1.1)
# Source: Brinkman et al., FEDS Note, 16 Oct 2026, Table F4.4.s ($B, end of period)
# --------------------------------------------------------------------------------------------------
def fig_z1_holders():
    holders = [
        ("Private debt funds", (432.5, 480.6, 532.2)),
        ("Business development\ncompanies (BDCs)", (238.1, 340.8, 455.9)),
        ("Rest of world", (306.4, 336.2, 375.5)),
        ("Interval and tender-\noffer funds", (34.0, 53.1, 76.3)),
        ("Middle-market CLOs", (31.7, 42.9, 53.7)),
    ]
    totals = (1042.6, 1253.6, 1493.5)
    years = ("2023", "2024", "2025")
    shades = [SEQ_BLUE_STEPS[2], SEQ_BLUE_STEPS[6], SEQ_BLUE_STEPS[10]]

    fig, ax = new_figure((7.0, 3.9))
    n = len(holders)
    h = 0.24
    for i, (name, vals) in enumerate(holders):
        y0 = n - 1 - i
        for k, v in enumerate(vals):
            yy = y0 + (1 - k) * (h + 0.03)
            ax.barh(yy, v, height=h, color=shades[k], zorder=3)
        # direct label on the 2025 bar: value and growth multiple since 2023
        ax.annotate(f"\\${vals[2]:,.0f}B, {vals[2] / vals[0]:.1f}x since 2023", (vals[2], y0 - (h + 0.03)),
                    xytext=(5, 0), textcoords="offset points", va="center", fontsize=8.5, color=INK_2)
    ax.set_yticks(range(n))
    ax.set_yticklabels([name for name, _ in holders][::-1])
    ax.tick_params(axis="y", length=0)
    ax.grid(axis="y", visible=False)
    ax.grid(axis="x", visible=True)
    ax.set_xlim(0, 780)
    ax.set_ylim(-0.55, n - 0.45)
    ax.set_xlabel("US private-credit loans held (\\$ billions, end of year)")
    # legend by year, light to dark
    from matplotlib.patches import Patch
    ax.legend(handles=[Patch(facecolor=shades[k], label=f"{years[k]}  (total \\${totals[k]:,.1f}B)") for k in (0, 1, 2)],
              loc="lower right", frameon=True, framealpha=1.0, facecolor=SURFACE, edgecolor="none", borderpad=0.4)
    return finish(fig, "ch17_z1_holders")


# --------------------------------------------------------------------------------------------------
# Figure 17.2: the mark as a moving average (section 17.2.2)
# --------------------------------------------------------------------------------------------------
THETA = np.array([0.5, 0.3, 0.2])


def smooth(x, theta=THETA):
    """x^o_t = sum_k theta_k x_{t-k}; x holds the true returns including K pre-sample quarters."""
    K = len(theta) - 1
    return np.array([sum(theta[k] * x[t - k] for k in range(K + 1)) for t in range(K, len(x))])


def fig_smoothing_staircase():
    rng = np.random.default_rng(17)
    N, K = 24, len(THETA) - 1
    x = rng.normal(0.018, 0.012, N + K)          # true quarterly returns incl. 2 pre-sample quarters
    shock_t = {10: -0.060, 11: -0.040}            # two stress quarters (index in 0..N-1)
    for t, v in shock_t.items():
        x[t + K] = v
    xo = smooth(x)
    xt = x[K:]
    q = np.arange(N + 1)
    true_idx = 100 * np.concatenate([[1.0], np.cumprod(1 + xt)])
    mark_idx = 100 * np.concatenate([[1.0], np.cumprod(1 + xo)])

    fig, (a1, a2) = new_figure("wide", ncols=2, gridspec_kw={"width_ratios": [1.35, 1]})

    # (a) simulated path
    a1.plot(q, mark_idx, color=BLUE, linewidth=LW, label="Reported mark")
    a1.plot(q, true_idx, color=ORANGE, linewidth=LW, label="True value")
    a1.set_xlim(0, N)
    a1.set_xlabel("Quarter")
    a1.set_ylabel("Value of 100 invested")
    mark_event(a1, 10.0, "Stress", y_frac=0.97)
    a1.legend(loc="upper left", bbox_to_anchor=(0.0, 0.93))
    a1.set_title("A mark lags and is shallower", fontsize=9.5)

    # (b) one shock, recognised over three quarters
    shock = 4.0
    rec = np.cumsum(THETA) * shock                 # 2.0, 3.2, 4.0
    xs = np.arange(3)
    a2.bar(xs, rec, width=0.55, color=BLUE, zorder=3)
    a2.hlines(shock, -0.45, 2.45, color=ORANGE, linewidth=LW, zorder=4)
    a2.annotate("True loss: 4.0", (2.45, shock), xytext=(0, 5), textcoords="offset points", ha="right",
                fontsize=8.5, color=INK_2)
    for i in range(2):
        a2.annotate(f"{shock - rec[i]:.1f} still\nto come", (i, (shock + rec[i]) / 2), ha="center", va="center",
                    fontsize=8.2, color=INK_2)
    for i in range(3):
        a2.annotate(f"{rec[i]:.1f}", (i, rec[i]), xytext=(0, -11), textcoords="offset points", ha="center",
                    fontsize=8.5, color=SURFACE)
    a2.set_xticks(xs)
    a2.set_xticklabels(["Shock\nquarter", "+1", "+2"])
    a2.set_xlim(-0.6, 2.6)
    a2.set_ylim(0, 4.9)
    a2.set_ylabel("Write-down in the mark (% of NAV)")
    a2.set_title("A 4% shock, θ = (0.5, 0.3, 0.2)", fontsize=9.5)
    return finish(fig, "ch17_smoothing_staircase")


# --------------------------------------------------------------------------------------------------
# Figure 17.3: implied asset markdown from the equity discount (section 17.3.2)
# --------------------------------------------------------------------------------------------------
def implied_markdown(disc, ell, phi=0.05):
    """m = ((1 - phi) - P/NAV) / (1 + ell), floored at zero; disc = 1 - P/NAV."""
    return np.maximum(0.0, ((1 - phi) - (1 - disc)) / (1 + ell))


def fig_implied_markdown():
    d = np.linspace(-0.05, 0.56, 300)
    fig, ax = new_figure("wide")
    ax.plot(d * 100, d * 100, color=NEUTRAL, linewidth=1.2, linestyle=(0, (3, 3)), zorder=2)
    ax.text(36.5, 33.6, "1 for 1: a 20% discount would\nmean 20% off the loans", ha="left", va="center",
            fontsize=8.2, color=INK_2)
    cols = {0.6: SEQ_BLUE_STEPS[5], 1.1: SEQ_BLUE_STEPS[8], 1.6: SEQ_BLUE_STEPS[11]}
    for ell, c in cols.items():
        ax.plot(d * 100, implied_markdown(d, ell) * 100, color=c, linewidth=LW, zorder=3)
    for ell, c in cols.items():
        yend = implied_markdown(0.56, ell) * 100
        ax.plot([56], [yend], "o", color=c, markersize=4, zorder=5, clip_on=False)
        ax.annotate(f"leverage {ell:.1f}x", (56, yend), xytext=(5, 0), textcoords="offset points", va="center",
                    fontsize=8.5, color=INK_2)
    # sourced price points (orange = market observations), labelled below the curves
    pts = [
        (14.0, implied_markdown(0.14, 1.19) * 100, "OBDC buyback at 86% of book,\nleverage 1.19x: 4.1%", (17.0, 1.2)),
        (20.0, implied_markdown(0.20, 1.1) * 100, "'Nearly 20%' discount\n(Octus): 7.1%", (33.0, 5.6)),
        (50.0, implied_markdown(0.50, 1.1) * 100, "'Approaching 50%'\n(Octus): 21.4%", (44.0, 11.0)),
    ]
    for x0, y0, txt, (tx, ty) in pts:
        ax.plot([x0], [y0], "o", color=ORANGE, markersize=6, zorder=6)
        ax.annotate(txt, (x0, y0), xytext=(tx, ty), textcoords="data", ha="left", va="center", fontsize=8.2,
                    color=INK_2, arrowprops=dict(arrowstyle="-", color=NEUTRAL, linewidth=0.8, shrinkA=1, shrinkB=4))
    ax.axvline(0, color=NEUTRAL, linewidth=0.9, zorder=1)
    ax.set_xlim(-5, 56)
    ax.set_ylim(-1.5, 36.5)
    ax.set_xlabel("Discount of share price to NAV, 1 \u2212 P/NAV (%)")
    ax.set_ylabel("Implied markdown on the loans (%)")
    note(ax, "fee drag \u03c6 = 5%:\nno markdown until the\ndiscount exceeds 5%", loc="upper left")
    return finish(fig, "ch17_implied_markdown")


# --------------------------------------------------------------------------------------------------
# Figure 17.4: one loan, seven marks (section 17.3.3)
# Source: fair value / par from each BDC's 10-Q schedule of investments (Medallia first-lien term loan)
# --------------------------------------------------------------------------------------------------
MEDALLIA_DATES = [dt.date(2024, 12, 31), dt.date(2025, 6, 30), dt.date(2025, 9, 30), dt.date(2025, 12, 31),
                  dt.date(2026, 3, 31), dt.date(2026, 6, 30)]
MEDALLIA = {
    "BCRED": [94.0, 86.8, 82.3, 77.8, 60.2, 49.5],
    "BXSL": [94.0, 86.7, 82.2, 77.7, 60.3, 49.5],
    "HLEND": [94.4, 89.4, 85.0, 78.0, 60.2, 49.2],
    "FS KKR": [97.7, 91.3, 91.2, 78.7, 54.1, 50.1],
    "Apollo ADS": [86.8, 86.8, 77.3, 73.0, 58.0, 40.7],
    "Onex": [96.2, 92.0, 81.4, 79.2, 55.7, 39.0],
    "Monroe": [98.8, 89.2, 84.2, 77.6, 64.9, 41.3],
}


def fig_medallia_marks():
    fig, ax = new_figure("wide")
    d = mdates.date2num(MEDALLIA_DATES)
    upper = ("BCRED", "BXSL", "HLEND", "FS KKR")
    for name, ys in MEDALLIA.items():
        c = BLUE if name in upper else ORANGE
        ax.plot(d, ys, color=c, linewidth=1.3, marker="o", markersize=4.5, zorder=3, alpha=0.9)
    arr = np.array(list(MEDALLIA.values()))
    rng = arr.max(axis=0) - arr.min(axis=0)
    ax.set_xticks(d)
    ax.set_xticklabels([f"{x:%b %Y}\nrange {r:.0f}" for x, r in zip(MEDALLIA_DATES, rng)])
    ax.set_xlim(d[0] - 25, d[-1] + 215)
    ax.set_ylim(34, 102)
    ax.set_ylabel("Fair value as % of par")
    ax.set_xlabel("Quarter end (range = highest minus lowest mark, in points)")
    ax.annotate("BCRED, BXSL, HLEND, FS KKR:\n49 to 50", (d[-1], 49.8), xytext=(8, 0), textcoords="offset points",
                va="center", fontsize=8.3, color=INK_2)
    ax.plot([d[-1] + 4], [49.8], "o", color=BLUE, markersize=4, clip_on=False, zorder=6)
    ax.annotate("Apollo ADS, Monroe, Onex:\n39 to 41", (d[-1], 40.0), xytext=(8, 0), textcoords="offset points",
                va="center", fontsize=8.3, color=INK_2)
    ax.plot([d[-1] + 4], [40.0], "o", color=ORANGE, markersize=4, clip_on=False, zorder=6)
    return finish(fig, "ch17_medallia_marks")


# --------------------------------------------------------------------------------------------------
# Figure 17.5: tender requests against the 5% cap, and the backlog recursion (section 17.6.2)
# Source: Schedule TO-I/A filings (requests as % of shares outstanding); model: section 17.6.2
# --------------------------------------------------------------------------------------------------
REQUESTS = [  # fund, Q1 2026, Q2 2026, Q3 2026 (preliminary or None), Q2 fill rate (% of tendered shares)
    ("Blue Owl Tech Income (OTIC)", 40.4, 38.1, None, 13.1),
    ("Blue Owl Credit Income (OCIC)", 21.9, 18.8, 16.8, 26.6),
    ("Apollo Debt Solutions (ADS)", 11.0, 16.8, None, 29.8),
    ("Ares Strategic Income (ASIF)", 11.6, 14.4, 13.1, 34.7),
    ("HPS Corporate Lending (HLEND)", 9.2, 13.3, None, 37.6),
    ("Barings Private Credit (BPCC)", 11.3, 10.9, 10.7, 46.0),
    ("Blackstone (BCRED)", None, 10.0, 10.0, 50.0),
]


def queue_path(a_new=0.10, c=0.05, T=8):
    """Backlog recursion of section 17.6.2: demand = B + a(S - B); paid = min(demand, cS)."""
    S, B = 1.0, 0.0
    rows = []
    for t in range(T):
        demand = B + a_new * (S - B)
        paid = min(demand, c * S)
        rows.append((S, demand, paid, demand - paid))
        B, S = demand - paid, S - paid
    return rows


def fig_redemption_queue():
    fig, (a1, a2) = new_figure((7.0, 3.9), ncols=2, gridspec_kw={"width_ratios": [1.5, 1]})
    qcol = [SEQ_BLUE_STEPS[2], SEQ_BLUE_STEPS[7], SEQ_BLUE_STEPS[11]]
    MS5 = (8.5, 7.0, 5.5)
    n = len(REQUESTS)
    a1.axvline(5, color=NEUTRAL, linewidth=0.9, linestyle=(0, (3, 3)), zorder=1)
    a1.annotate("5% cap", (5, n - 0.35), xytext=(3, 0), textcoords="offset points", fontsize=8, color=INK_2,
                va="center")
    for i, (name, q1, q2, q3, fill) in enumerate(REQUESTS):
        y = n - 1 - i
        vals = [(q1, 0), (q2, 1), (q3, 2)]
        have = [(v, k) for v, k in vals if v is not None]
        a1.plot([v for v, _ in have], [y] * len(have), color=NEUTRAL, linewidth=1.0, zorder=2)
        for v, k in have:   # nested sizes (Q1 largest, Q3 smallest) so coincident quarters stay visible
            a1.plot([v], [y], "o", color=qcol[k], markersize=MS5[k], zorder=4 + k * 0.1)
        a1.text(47.5, y, f"{fill:.0f}%", ha="center", va="center", fontsize=8.5, color=INK_2)
    a1.text(47.5, n - 0.35, "Q2 fill", ha="center", va="center", fontsize=8, color=MUTED)
    a1.set_yticks(range(n))
    a1.set_yticklabels([r[0] for r in REQUESTS][::-1], fontsize=8)
    a1.tick_params(axis="y", length=0)
    a1.grid(axis="y", visible=False)
    a1.grid(axis="x", visible=True)
    a1.set_xlim(0, 51)
    a1.set_ylim(-0.6, n - 0.1)
    a1.set_xticks(range(0, 41, 10))
    a1.set_xlabel("Tender requests (% of shares outstanding)")
    from matplotlib.lines import Line2D
    a1.legend(handles=[Line2D([], [], marker="o", linestyle="", color=qcol[k], markersize=MS5[k], label=l)
                       for k, l in enumerate(("Q1 2026", "Q2 2026", "Q3 2026 (prelim.)"))],
              loc="lower right", bbox_to_anchor=(0.86, 0.0), frameon=True, framealpha=1.0, facecolor=SURFACE,
              edgecolor="none", borderpad=0.3, fontsize=8, handletextpad=0.2, labelspacing=0.3)
    a1.set_title("Requests ran at 2 to 8 times the cap", fontsize=9.5)

    rows = queue_path()
    q = np.arange(1, len(rows) + 1)
    paid = np.array([r[2] / r[0] * 100 for r in rows])
    unf = np.array([r[3] / r[0] * 100 for r in rows])
    a2.bar(q, paid, width=0.62, color=BLUE, zorder=3)
    a2.bar(q, unf, width=0.62, bottom=paid, color=SEQ_BLUE_STEPS[1], zorder=3)
    for t in range(len(rows)):
        fill = rows[t][2] / rows[t][1] * 100
        a2.annotate(f"{fill:.0f}%", (q[t], paid[t] + unf[t]), xytext=(0, 3), textcoords="offset points",
                    ha="center", fontsize=8.2, color=INK_2)
    a2.set_xticks(q)
    a2.set_xlabel("Quarter")
    a2.set_ylabel("Demand (% of shares outstanding)")
    a2.set_ylim(0, 48)
    a2.set_title("A growing queue", fontsize=9.5)
    from matplotlib.patches import Patch
    a2.legend(handles=[Patch(facecolor=BLUE, label="Paid at the 5% cap"),
                       Patch(facecolor=SEQ_BLUE_STEPS[1], label="Unfilled, resubmitted")],
              loc="upper left", fontsize=8, handlelength=1.2, handletextpad=0.4, borderaxespad=0.2)
    a2.text(0.03, 0.835, "Labels: fill rate", transform=a2.transAxes, ha="left", va="top", fontsize=8, color=MUTED)
    return finish(fig, "ch17_redemption_queue")


if __name__ == "__main__":
    fig_z1_holders()
    fig_smoothing_staircase()
    fig_implied_markdown()
    fig_medallia_marks()
    fig_redemption_queue()
