"""Chapter 27 figures: System Construction, Low-Latency Infrastructure & ASICs/FPGAs.

Run from anywhere:  python3 tools/figures/ch27.py
Writes assets/figures/ch27_*.png (five figures, in order of appearance in the chapter).

Data policy (see style.py): this chapter is about architecture and derived formulas, so every figure is either a
schematic of a structure the text describes or a plot of a formula the text states (parameters are the chapter's
own, and the captions say "Illustrative"). No real time series is used, and no number is presented as real data.

Chapter-wide colour roles (a role keeps its colour in every figure):
  BLUE   = the slow path / the quote clock / the baseline model
  ORANGE = the fast path / the hedge clock / the stressed or cheaper alternative
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from style import *  # noqa: F401,F403,E402  (applies the rcParams on import)

import numpy as np  # noqa: E402
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Patch, Rectangle  # noqa: E402

TINT_SLOW = "#e6f0fc"
TINT_FAST = "#fdebe3"
BOX_FILL = "#ffffff"


def lighten(hex_color, f):
    """Blend a hex colour toward white; f = share of white (0 = unchanged)."""
    h = hex_color.lstrip("#")
    rgb = [int(h[i:i + 2], 16) for i in (0, 2, 4)]
    return "#%02x%02x%02x" % tuple(round(c + (255 - c) * f) for c in rgb)


# --------------------------------------------------------------------------------------------------------------
# Figure 27.1: the two-speed architecture (schematic of the diagram in section 27.1)
# --------------------------------------------------------------------------------------------------------------
def _box(ax, x0, x1, yc, h, title, sub, edge, fs=8.4, sfs=7.6):
    ax.add_patch(FancyBboxPatch((x0, yc - h / 2), x1 - x0, h, boxstyle="round,pad=0,rounding_size=1.2",
                                facecolor=BOX_FILL, edgecolor=edge, linewidth=1.2, zorder=2))
    ax.text((x0 + x1) / 2, yc + (2.0 if sub else 0), title, ha="center", va="center", fontsize=fs, color=INK,
            fontweight="bold", zorder=3)
    if sub:
        ax.text((x0 + x1) / 2, yc - 1.9, sub, ha="center", va="center", fontsize=sfs, color=INK_2, zorder=3,
                linespacing=1.15)


def _arrow(ax, p0, p1, color, lw=1.4):
    ax.add_patch(FancyArrowPatch(p0, p1, arrowstyle="-|>", mutation_scale=9, linewidth=lw, color=color,
                                 shrinkA=0, shrinkB=0, zorder=4))


def fig_two_clocks():
    fig, ax = new_figure("tall")
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 112)
    ax.axis("off")
    ax.grid(False)

    # lanes
    ax.add_patch(FancyBboxPatch((1, 0.5), 46.5, 110, boxstyle="round,pad=0,rounding_size=1.5", facecolor=TINT_SLOW,
                                edgecolor="none", zorder=0))
    ax.add_patch(FancyBboxPatch((52.5, 0.5), 46.5, 110, boxstyle="round,pad=0,rounding_size=1.5", facecolor=TINT_FAST,
                                edgecolor="none", zorder=0))
    ax.text(24, 107, "SLOW PATH", ha="center", va="center", fontsize=10, fontweight="bold", color=INK)
    ax.text(24, 102.6, "milliseconds to minutes\nrich, auditable; the only path that may say yes", ha="center",
            va="center", fontsize=7.8, color=INK_2, linespacing=1.2)
    ax.text(76, 107, "FAST PATH", ha="center", va="center", fontsize=10, fontweight="bold", color=INK)
    ax.text(76, 102.6, "nanoseconds to microseconds\nthin, provably bounded; may only say no", ha="center",
            va="center", fontsize=7.8, color=INK_2, linespacing=1.2)

    h = 11.5
    ys = [88, 72, 56, 40, 24, 8]
    lx0, lx1 = 2.5, 45
    left = [
        ("Feeds", "venue RFQ, TRACE, composites, dealer runs"),
        ("Normaliser and price store", "each record: price_kind, known_at (27.2)"),
        ("Security master", "bitemporal, internal surrogate keys (27.3)"),
        ("Fair value and quote model", "inventory skew and margin (Ch. 18)"),
        ("Pre-trade risk, then OMS/EMS", "limits and the order state machine (27.4)"),
        ("Venues", "RFQ, all-to-all, portfolio trade, streaming"),
    ]
    for y, (t, s) in zip(ys, left):
        _box(ax, lx0, lx1, y, h, t, s, BLUE)
    for y0, y1 in zip(ys[:-1], ys[1:]):
        _arrow(ax, (25, y0 - h / 2 - 0.4), (25, y1 + h / 2 + 0.4), INK_2)

    # fast lane: trigger table + hedge data -> comparator -> pull
    rx0, rx1 = 55, 97.5
    _box(ax, rx0, 75, ys[3], h + 1, "Trigger table", "rows: H_ref, beta,\nthreshold per quote", ORANGE, fs=8.2,
         sfs=7.2)
    _box(ax, 78, rx1, ys[3], h + 1, "Hedge data", "TY, HYG/LQD, CDX,\ncredit futures", ORANGE, fs=8.2, sfs=7.2)
    _box(ax, rx0, rx1, ys[4], h, "Comparator (fixed point)", "pull if any |move| > row threshold",
         ORANGE)
    _box(ax, rx0, rx1, ys[5], h, "Pull or widen exposed quotes", "limits, kill switch, cancel-on-disconnect",
         ORANGE)
    _arrow(ax, (65, ys[3] - (h + 1) / 2 - 0.4), (65, ys[4] + h / 2 + 0.4), ORANGE)
    _arrow(ax, (87.75, ys[3] - (h + 1) / 2 - 0.4), (87.75, ys[4] + h / 2 + 0.4), ORANGE)
    _arrow(ax, (75, ys[4] - h / 2 - 0.4), (75, ys[5] + h / 2 + 0.4), ORANGE)

    # slow -> fast: the builder writes rows; fast -> venues: cancel
    _arrow(ax, (lx1 + 0.4, ys[3]), (rx0 - 0.4, ys[3]), BLUE, lw=1.8)
    ax.text((lx1 + rx0) / 2, ys[3] + 2.4, "writes\nrows", ha="center", va="bottom", fontsize=7.4, color=INK_2,
            linespacing=1.1)
    _arrow(ax, (rx0 - 0.4, ys[5]), (lx1 + 0.4, ys[5]), ORANGE, lw=1.8)
    ax.text((lx1 + rx0) / 2, ys[5] + 2.4, "cancel", ha="center", va="bottom", fontsize=7.4, color=INK_2)

    # notes in the empty upper-right of the fast lane
    notes = [
        "The FPGA does not price bonds.",
        "It compares numbers the slow path\ncomputed and wrote into a table.",
        "It may only pull. A pulled quote\ncomes back only when the slow path\nwrites a new row.",
    ]
    ytxt = [86, 79.5, 68]
    for y, t in zip(ytxt, notes):
        ax.text(56, y, t, ha="left", va="center", fontsize=7.9, color=INK_2, linespacing=1.25, style="italic")
    return finish(fig, "ch27_two_clocks")


# --------------------------------------------------------------------------------------------------------------
# Figure 27.2: the value of a latency improvement, edge retained = exp(-lag / T), from section 27.1.1
# --------------------------------------------------------------------------------------------------------------
def fig_edge_decay():
    DAY = 23400.0  # one trading session in seconds (the chapter's 23,400-second session)
    curves = [
        # label, T seconds, colour
        ("Value or carry signal\nT = 63 trading days", 63 * DAY, BLUE),
        ("Trend signal\nT = 42 trading days", 42 * DAY, ORANGE),
        ("Client RFQ\nT = 100 s", 100.0, AQUA),
        ("Hedge-instrument jump\nT = 79 µs", 79e-6, YELLOW),
    ]
    fig, ax = new_figure("wide")
    lag = np.logspace(-7, 8, 1200)
    for name, T, col in curves:
        ax.plot(lag, np.exp(-lag / T), color=col, linewidth=LW, zorder=3)
        # the lag that costs 1% of the edge (0.01 T), as in the table of section 27.1.1
        ax.plot([0.01 * T], [np.exp(-0.01)], "o", color=col, markersize=5, zorder=4)
    ax.set_xscale("log")
    ax.set_xlim(1e-7, 1e8)
    ax.set_ylim(-0.03, 1.06)
    ax.set_ylabel("Share of the edge retained")
    ax.set_xlabel("Reaction lag (log scale; trading time, 1 day = 23,400 s)")
    ax.set_xticks([1e-6, 1e-3, 1, 60, DAY, 21 * DAY])
    ax.set_xticklabels(["1 µs", "1 ms", "1 s", "1 min", "1 day", "1 month"])
    ax.minorticks_off()
    ax.set_yticks([0, 0.25, 0.5, 0.75, 1.0])
    ax.set_yticklabels(["0%", "25%", "50%", "75%", "100%"])

    # Kaz's p99
    ax.axvline(1.5, color=NEUTRAL, linewidth=0.9, linestyle=(0, (3, 3)), zorder=1)
    ax.annotate("1.5 s: the p99\nof the cold open", (1.5, 0.04), xytext=(-4, 0), textcoords="offset points",
                ha="right", va="bottom", fontsize=8, color=INK_2)

    # direct labels (aqua and yellow are low-contrast, so every curve is named beside the curve itself)
    def lab(x, y, text, ha, col):
        ax.annotate(text, (x, y), xytext=(8 if ha == "left" else -6, 0), textcoords="offset points", ha=ha,
                    va="center", fontsize=8, color=INK_2, linespacing=1.15)

    lab(-np.log(0.7) * curves[3][1], 0.7, curves[3][0], "left", curves[3][2])
    lab(-np.log(0.7) * curves[2][1], 0.7, curves[2][0], "left", curves[2][2])   # right of its curve, clear of the 1.5 s line
    lab(-np.log(0.5) * curves[1][1], 0.5, curves[1][0], "right", curves[1][2])
    lab(-np.log(0.5) * curves[0][1], 0.5, curves[0][0], "left", curves[0][2])
    ax.text(10 ** -3.4, 0.30, "Dots: the lag that\ncosts 1% of the edge", fontsize=8, color=MUTED, ha="left",
            va="center", linespacing=1.15)
    return finish(fig, "ch27_edge_decay")


# --------------------------------------------------------------------------------------------------------------
# Figure 27.3: the Serta rows on the two time axes (section 27.3.3)
# --------------------------------------------------------------------------------------------------------------
def fig_bitemporal_serta():
    fig, ax = new_figure("wide")
    X = {"2016": 0.0, "2019": 1.0, "exch": 2.2, "d23": 3.1, "inf": 4.0}
    Y = {"2016": 0.0, "mid": 1.15, "close": 1.9, "now": 3.0, "top": 3.4}
    g = 0.025  # white gap between rectangles
    pari = lighten(BLUE, 0.45)
    pari_closed = lighten(BLUE, 0.78)
    prio = lighten(ORANGE, 0.45)

    def rect(x0, x1, y0, y1, col):
        ax.add_patch(Rectangle((x0 + g, y0 + g), x1 - x0 - 2 * g, y1 - y0 - 2 * g, facecolor=col, edgecolor="none",
                               zorder=2))

    rect(X["2016"], X["inf"], Y["2016"], Y["close"], pari_closed)   # row 1: closed in knowledge time
    rect(X["2016"], X["exch"], Y["close"], Y["top"], pari)          # row 2: re-inserted, valid to 22 Jun
    rect(X["exch"], X["inf"], Y["close"], Y["top"], prio)           # row 3: the new ranking

    ax.text(2.0, 0.78, "first_lien_pari\nbelieved from onboarding until 6 p.m., 22 Jun 2020;\nclosed in knowledge time, never deleted",
            ha="center", va="center", fontsize=8, color=INK, linespacing=1.25, zorder=4)
    ax.text(1.1, 2.35, "first_lien_pari\ntrue until 22 Jun 2020", ha="center", va="center", fontsize=8, color=INK,
            linespacing=1.25, zorder=4)
    ax.text(3.1, 2.35, "first_lien_behind_\nsuper_priority\ntrue from 22 Jun 2020", ha="center", va="center",
            fontsize=8, color=INK, linespacing=1.25, zorder=4)

    def query(x, y, n, label, dx=0.1, ha="left"):
        ax.text(x, y, str(n), ha="center", va="center", fontsize=8, color="white", fontweight="bold", zorder=6,
                bbox=dict(boxstyle="circle,pad=0.25", facecolor=INK, edgecolor="none"))
        ax.text(x + (dx if ha == "left" else -dx), y, label, ha=ha, va="center", fontsize=8, color=INK_2,
                linespacing=1.15, zorder=6)

    query(X["d23"], Y["now"] + 0.0, 1, "live risk,\ntoday")
    query(X["d23"], Y["mid"], 2, "backtest at\nmidnight 22 Jun")
    query(X["2019"], Y["now"], 3, "2019 study,\nrun today")

    ax.set_xlim(0, X["inf"])
    ax.set_ylim(0, Y["top"])
    ax.grid(False)
    ax.set_xticks([X["2016"], X["2019"], X["exch"], X["d23"], X["inf"]])
    ax.set_xticklabels(["1 Nov 2016", "1 Jun 2019", "22 Jun 2020", "23 Jun 2020", "∞"])
    ax.set_yticks([Y["2016"], Y["mid"], Y["close"], Y["now"]])
    ax.set_yticklabels(["1 Nov 2016", "22 Jun 2020\n00:00", "22 Jun 2020\n18:00", "now"])
    ax.set_xlabel("Valid time: when the fact was true in the world")
    ax.set_ylabel("Knowledge time: when the desk believed it")
    note(ax, "axes not to scale", loc="lower right")
    return finish(fig, "ch27_bitemporal_serta")


# --------------------------------------------------------------------------------------------------------------
# Figure 27.4: Kaz's engine, the p99 against utilisation (27.5.1) and the fan-out penalty
# --------------------------------------------------------------------------------------------------------------
def pk_wait(rho, cs2, ES):
    return rho / (1 - rho) * (1 + cs2) / 2 * ES


def p99_wait(rho, cs2, ES, q=0.99):
    return pk_wait(rho, cs2, ES) / rho * np.log(rho / (1 - q))


def fig_queue_tail():
    ES = 0.040  # seconds
    fig, (a, b) = new_figure(ncols=2)

    rho = np.linspace(0.05, 0.95, 400)
    p4 = p99_wait(rho, 4.0, ES) + ES
    p1 = p99_wait(rho, 1.0, ES) + ES
    m4 = pk_wait(rho, 4.0, ES) + ES
    a.plot(rho, p4, color=BLUE, linewidth=LW, zorder=3)
    a.plot(rho, p1, color=ORANGE, linewidth=LW, zorder=3)
    a.plot(rho, m4, color=NEUTRAL, linewidth=LW, linestyle=(0, (4, 2)), zorder=2)
    for r, dx, dy in [(0.5, -6, 9), (0.7, -6, 9), (0.9, -8, 9)]:
        y = p99_wait(r, 4.0, ES) + ES
        a.plot([r], [y], "o", color=BLUE, markersize=5, zorder=5)
        a.annotate(f"{y:.1f} s", (r, y), xytext=(dx, dy), textcoords="offset points", ha="right", va="center",
                   fontsize=8, color=INK_2)
    a.set_xlim(0.05, 0.95)
    a.set_ylim(0, 9.8)
    a.set_xlabel("Utilisation ρ")
    a.set_ylabel("Time in the building (s)")
    a.set_title("p99 versus mean, 40 ms mean service", fontsize=9)
    from matplotlib.lines import Line2D
    a.legend(handles=[Line2D([], [], color=BLUE, linewidth=LW, label="p99, c\u00b2 = 4 (Kaz's engine)"),
                      Line2D([], [], color=ORANGE, linewidth=LW, label="p99, c\u00b2 = 1"),
                      Line2D([], [], color=NEUTRAL, linewidth=LW, linestyle=(0, (4, 2)), label="mean, c\u00b2 = 4")],
             loc="upper left", fontsize=8, borderaxespad=0.2)

    n = np.logspace(0, 3, 300)
    for p, col, name, ypos in [(0.01, BLUE, "1 in 100 calls slow", None),
                               (0.001, ORANGE, "1 in 1,000", None),
                               (0.0001, AQUA, "1 in 10,000", None)]:
        b.plot(n, 1 - (1 - p) ** n, color=col, linewidth=LW, zorder=3)
    b.set_xscale("log")
    b.set_xlim(1, 1000)
    b.set_ylim(0, 1.04)
    b.set_xticks([1, 10, 100, 1000])
    b.set_xticklabels(["1", "10", "100", "1,000"])
    b.minorticks_off()
    b.set_yticks([0, 0.25, 0.5, 0.75, 1.0])
    b.set_yticklabels(["0%", "25%", "50%", "75%", "100%"])
    b.set_xlabel("Fan-out: pricing calls the request waits for")
    b.set_ylabel("Share of requests that are slow")
    b.set_title("The tail at scale", fontsize=9)
    for nn, pp in [(100, 0.63), (150, 0.78)]:
        b.plot([nn], [1 - 0.99 ** nn], "o", color=BLUE, markersize=5, zorder=5)
    b.annotate("100-way: 63%", (100, 1 - 0.99 ** 100), xytext=(-7, 7), textcoords="offset points", ha="right",
               va="bottom", fontsize=8, color=INK_2)
    b.annotate("150-line PT: 78%", (150, 1 - 0.99 ** 150), xytext=(-7, 7), textcoords="offset points", ha="right",
               va="bottom", fontsize=8, color=INK_2)
    label_end(b, 1000, 1.0, "1 in 100", BLUE, dx=-8, dy=-11, ha="right")
    label_end(b, 1000, 1 - (1 - 0.001) ** 1000, "1 in 1,000", ORANGE, dx=-8, dy=11, ha="right")
    label_end(b, 1000, 1 - (1 - 0.0001) ** 1000, "1 in 10,000", AQUA, dx=-8, dy=11, ha="right")
    b.legend(handles=[Line2D([], [], color=BLUE, linewidth=LW, label="1 call in 100 slow"),
                      Line2D([], [], color=ORANGE, linewidth=LW, label="1 in 1,000"),
                      Line2D([], [], color=AQUA, linewidth=LW, label="1 in 10,000")],
             loc="center left", bbox_to_anchor=(0.0, 0.40), fontsize=8, borderaxespad=0.2)
    return finish(fig, "ch27_queue_tail")


# --------------------------------------------------------------------------------------------------------------
# Figure 27.5: the trigger rule in the (TY, HYG) plane (section 27.6.1)
# --------------------------------------------------------------------------------------------------------------
def fig_trigger_geometry():
    from matplotlib.colors import ListedColormap
    from matplotlib.lines import Line2D
    b_ty, b_hyg, theta = 1.05, 1.27, 0.14
    s_ty, s_hyg = 0.06, 0.05                      # illustrative short-horizon volatilities of the two hedges
    c = theta / (abs(b_ty) * s_ty + abs(b_hyg) * s_hyg)
    tau_ty, tau_hyg = c * s_ty, c * s_hyg         # per-instrument thresholds in each hedge's own units

    fig, ax = new_figure((5.2, 6.1))
    lim = 0.34
    xs = np.linspace(-lim, lim, 700)
    X, Y = np.meshgrid(xs, xs)
    dP = b_ty * X + b_hyg * Y                     # fair-value move of the bond, in points
    joint = np.abs(dP) > theta                    # exact rule: pull the bid (dP < -theta) or the offer (dP > theta)
    box = (np.abs(X) > tau_ty) | (np.abs(Y) > tau_hyg)
    cls = np.zeros_like(X)
    cls[box & ~joint] = 1   # only the cheap rule pulls: a false pull
    cls[joint] = 2          # the exact rule pulls (the cheap rule always does too, by the triangle inequality)
    assert not np.any(joint & ~box)               # the safety theorem, on the grid
    cmap = ListedColormap(["#ffffff", lighten(ORANGE, 0.72), lighten(BLUE, 0.62)])
    ax.pcolormesh(X, Y, cls, cmap=cmap, vmin=0, vmax=2, shading="auto", zorder=1, rasterized=True)

    xl = np.array([-lim, lim])
    for sgn in (-1, 1):
        ax.plot(xl, (sgn * theta - b_ty * xl) / b_hyg, color=BLUE, linewidth=LW, zorder=3)
    ax.add_patch(Rectangle((-tau_ty, -tau_hyg), 2 * tau_ty, 2 * tau_hyg, facecolor="none", edgecolor=ORANGE,
                           linewidth=LW, zorder=3))
    ax.axhline(0, color=NEUTRAL, linewidth=0.7, zorder=2)
    ax.axvline(0, color=NEUTRAL, linewidth=0.7, zorder=2)

    cold = (-6 / 32, -0.14)
    ftq = (0.15, -0.12)
    for (px, py), n in [(cold, "A"), (ftq, "B")]:
        ax.text(px, py, n, ha="center", va="center", fontsize=8, color="white", fontweight="bold", zorder=6,
                bbox=dict(boxstyle="circle,pad=0.25", facecolor=INK, edgecolor="none"))
    ax.text(0.325, 0.325, "both rules\npull the offer", ha="right", va="top", fontsize=8, color=INK_2,
            linespacing=1.15, zorder=6)
    ax.text(-0.325, -0.325, "both rules\npull the bid", ha="left", va="bottom", fontsize=8, color=INK_2,
            linespacing=1.15, zorder=6)

    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)
    ax.set_aspect("equal")
    ax.grid(False)
    ax.set_xlabel(r"TY futures move $\Delta H_{\mathrm{TY}}$ (points)")
    ax.set_ylabel(r"HYG move $\Delta H_{\mathrm{HYG}}$ (dollars)")
    ax.legend(handles=[Line2D([], [], color=BLUE, linewidth=LW, label=r"exact rule boundary, $|\beta\cdot\Delta H| = \theta$"),
                       Line2D([], [], color=ORANGE, linewidth=LW, label="cheap rule: no-pull box (|moves| within thresholds)"),
                       Patch(facecolor=lighten(ORANGE, 0.72), label="false pull: cheap rule fires, exact rule does not"),
                       Line2D([], [], color=INK, marker="o", markersize=7, linestyle="",
                              label="A: the cold open, TY \u22126/32 and HYG \u221214 cents; both pull the bid"),
                       Line2D([], [], color=INK, marker="o", markersize=7, linestyle="",
                              label="B: flight to quality, TY up and HYG down; only the cheap rule pulls")],
              loc="upper center", bbox_to_anchor=(0.5, -0.12), fontsize=7.6, ncol=1, borderaxespad=0.0)
    return finish(fig, "ch27_trigger_geometry")


if __name__ == "__main__":
    fig_two_clocks()
    fig_edge_decay()
    fig_bitemporal_serta()
    fig_queue_tail()
    fig_trigger_geometry()
