"""Figures for Chapter 4-C (Other Seats at the Table: One Bond, Seven Owners).

Run:  python3 tools/figures/ch04c.py   -> assets/figures/ch04c_*.png

Everything in this chapter is a fictional composite (Halvorsen and its seven seats), so every figure is
"Illustrative": the numbers are the ones the chapter text states, the 12-B cap table, or the stated random-walk model.

Colour use in this chapter: a SEAT keeps one colour in every figure (SEAT below, in the order the chapter meets them:
dealer, systematic fund, pod, CLO manager, insurer, direct lender, opportunistic fund). The desk (Theo) is ink, because
it is the reference seat and not one of the seven. Aqua, yellow and magenta are low contrast on white, so each seat is
also direct-labelled wherever its colour is used. Neutral grey is the comparison case or the cost.
"""
import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from style import *  # noqa: E402,F401,F403  (applies the rcParams on import)

import numpy as np  # noqa: E402
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch, Rectangle  # noqa: E402
from scipy.stats import norm  # noqa: E402

SEAT = {"dealer": BLUE, "systematic": ORANGE, "pod": AQUA, "clo": YELLOW, "insurer": MAGENTA,
        "direct": GREEN, "opp": VIOLET, "desk": INK}
TINT = "#f5f5f3"      # very light surface for grouping bands (not a data colour)

# Halvorsen's seven prints (chapter text): Friday close, Monday gap, Wednesday bounce, then days 12, 16, 23, 30.
PRINT_DAYS = np.array([1, 2, 4, 12, 16, 23, 30])
PRINT_PX = np.array([92.0, 78.0, 81.0, 74.0, 72.0, 76.0, 70.0])


# --------------------------------------------------------------------------------------------------
# Figure 4-C.1: seven clocks (cold open)
# --------------------------------------------------------------------------------------------------
def fig_seven_clocks():
    D = 1.0
    mins, hour, week, month, year = 1 / 1440, 1 / 24, 7.0, 30.0, 365.0
    # key, name, binding rule, horizon low, high (days), check interval (days) or None, trigger
    rows = [
        ("desk", "The desk (Theo)", "limit sheet, 5-point stop", 2, 20, 1, "a price"),
        ("dealer", "Dealer desk", "inventory and loss limits", 10 * mins, 5, 1, "two days in inventory after a gap"),
        ("systematic", "Systematic fund", "risk budget, default guard", month, 6 * month, 1, "the guard flags the name"),
        ("pod", "RV pod", "pod-level drawdown", 3 * month, year, 1, "drawdown on the whole pod"),
        ("clo", "CLO manager", "CCC bucket, OC and IC tests", 2 * year, 5 * year, month, "a downgrade before the test date"),
        ("direct", "Direct lender", "redemption cap on tenders", 3 * year, 5 * year, 91, "a queue above the 5% cap"),
        ("opp", "Opportunistic fund", "return on its funding", 1 * year, 5 * year, None, "forced supply at a discount"),
        ("insurer", "Life insurer", "NAIC designation, C-1 factor", 10 * year, 30 * year, year, "a rating change before 31 Dec"),
    ]
    ys = [8.1, 6.4, 5.3, 4.2, 3.1, 2.0, 0.9, -0.2]
    fig, ax = new_figure((7.0, 4.7))
    ax.set_xscale("log")
    ax.set_xlim(0.6 * mins, 70 * year)
    ax.set_ylim(-0.95, 9.05)
    ax.grid(False, axis="y")
    ax.grid(True, axis="x", color=GRID, linewidth=0.7)
    ax.set_axisbelow(True)
    ax.spines["left"].set_visible(False)
    ax.tick_params(axis="y", left=False, labelleft=False)
    ticks = [mins, 1 / 24, 1, 30, 365, 3650]
    ax.set_xticks(ticks)
    ax.set_xticklabels(["1 min", "1 hr", "1 day", "1 mo", "1 yr", "10 yr"], fontsize=8)
    ax.minorticks_off()
    ax.set_xlabel("Horizon (log scale).  Bar = how long the seat expects to hold;  ◆ = how often its rule is checked")

    yt = ax.get_yaxis_transform()
    ax.text(-0.02, 8.95, "Seat and its binding rule", transform=yt, ha="right", va="center", fontsize=7.6, color=MUTED)
    ax.text(1.02, 8.95, "What moves it", transform=yt, ha="left", va="center", fontsize=7.6, color=MUTED)
    ax.axhline(7.25, color=GRID, linewidth=1.0, zorder=1)
    for (key, name, rule, lo, hi, chk, trig), y in zip(rows, ys):
        c = SEAT[key]
        ax.barh(y, hi - lo, left=lo, height=0.46, color=c, zorder=3)
        if chk is not None:
            ax.plot([chk], [y], "D", color=INK, markersize=5.2, zorder=5, markeredgewidth=0)
        ax.text(-0.02, y + 0.17, name, transform=yt, ha="right", va="center", fontsize=8.6, color=INK,
                fontweight="bold" if key == "desk" else "normal")
        ax.text(-0.02, y - 0.22, rule, transform=yt, ha="right", va="center", fontsize=7.4, color=MUTED)
        ax.text(1.02, y, trig, transform=yt, ha="left", va="center", fontsize=8.2,
                color=INK if key == "desk" else INK_2, fontweight="bold" if key == "desk" else "normal")
    # the one trigger that is a price
    ax.annotate("", xy=(1.0, 8.1), xycoords=yt, xytext=(1.0, 8.1), textcoords=yt)
    ax.text(0.85 * year, 0.9, "no ◆: it checks deal by deal", ha="right", va="center", fontsize=7.6, color=MUTED)
    return finish(fig, "ch04c_seven_clocks")


# --------------------------------------------------------------------------------------------------
# Figure 4-C.2: horizon can change the sign of a trade (Math, Gently in 4C.1)
# --------------------------------------------------------------------------------------------------
MU, SIG = 9.0 / 252.0, 1.5      # points per trading day: drift of 9 points a year, daily noise of 1.5 points
EXIT_COST = 3.0                 # points of bid-ask paid on each forced exit in a stressed name


def p_touch(T, a, mu=MU, sig=SIG):
    """Probability a Brownian path with drift mu and vol sig touches -a before T (reflection principle with drift)."""
    T = np.asarray(T, dtype=float)
    s = sig * np.sqrt(T)
    return norm.cdf((-a - mu * T) / s) + np.exp(-2 * mu * a / sig ** 2) * norm.cdf((-a + mu * T) / s)


def seat_economics(stop, horizon):
    """Expected drift collected before the stop or the horizon, expected exit cost, and the net, in points."""
    t = np.linspace(1e-6, horizon, 4001)
    surv = 1.0 - p_touch(t, stop)
    drift = MU * np.trapezoid(surv, t)           # E[min(tau, T)] = integral of survival
    cost = EXIT_COST * float(p_touch(horizon, stop))
    return drift, cost, drift - cost


def fig_horizon_flips_sign():
    fig, (a1, a2) = new_figure("wide", ncols=2)
    T = np.linspace(0, 260, 400)
    gain, swing = MU * T, SIG * np.sqrt(T)
    a1.plot(T, swing, color=INK_2, linewidth=LW)
    a1.plot(T, gain, color=NEUTRAL, linewidth=LW + 0.4)
    a1.set_xlim(0, 262)
    a1.set_ylim(0, 27)
    a1.set_xlabel("Horizon (trading days)")
    a1.set_ylabel("Points")
    a1.annotate("typical swing  1.5\u221aT", (90, SIG * np.sqrt(90)), xytext=(40, 20.8), ha="left", va="center",
                fontsize=8.2, color=INK_2, arrowprops=dict(arrowstyle="-", color=NEUTRAL, linewidth=0.8))
    a1.text(190, MU * 190 - 2.0, "expected gain  0.036T", ha="center", va="top", fontsize=8.2, color=INK_2)
    for x, key in [(20, "dealer"), (252, "pod")]:
        a1.axvline(x, color=NEUTRAL, linewidth=0.9, linestyle=(0, (3, 3)), zorder=1)
        a1.plot([x, x], [MU * x, SIG * np.sqrt(x)], "o", color=SEAT[key], markersize=6, zorder=5, clip_on=False)
    a1.text(25, 3.8, "Dana, 20 days\ngain 0.7, swing 6.7", fontsize=8, color=INK_2, va="center", ha="left")
    a1.text(247, 15.5, "Pod, 1 year\ngain 9, swing 24", fontsize=8, color=INK_2, va="center", ha="right")
    a1.text(26, 26.6, "Gain catches one swing only\nafter about 1,760 days (7 years)", fontsize=7.8, color=MUTED, va="top", ha="left")

    # right: expected value of holding, by seat (the stop and the clock differ)
    seats = [("dealer", "Dana\n5-point stop,\n20 days", 5, 20), ("pod", "Pod\n15-point stop,\n1 year", 15, 252)]
    ticks, tlabels = [], []
    for i, (key, lab, stop, hor) in enumerate(seats):
        d, c, n = seat_economics(stop, hor)
        x0 = i * 1.3
        for dx, v, col in [(-0.3, d, SEAT[key]), (0.0, -c, NEUTRAL), (0.3, n, INK_2)]:
            a2.bar(x0 + dx, v, width=0.25, color=col, zorder=3)
            txt = f"{v:+.1f}".replace("-", "\u2212")
            a2.annotate(txt, (x0 + dx, v), xytext=(0, 3 if v >= 0 else -3), textcoords="offset points", ha="center",
                        va="bottom" if v >= 0 else "top", fontsize=8, color=INK_2)
        ticks += [x0 - 0.3, x0, x0 + 0.3]
        tlabels += ["drift", "exit\ncost", "net"]
        a2.text(x0, -0.2, lab, transform=a2.get_xaxis_transform(), ha="center", va="top", fontsize=8.2, color=INK, linespacing=1.15)
        print(f"  seat {key}: drift {d:.2f}, cost {c:.2f}, net {n:.2f}, P(stop) {float(p_touch(hor, stop)):.2f}")
    a2.axhline(0, color=INK_2, linewidth=0.8, zorder=4)
    a2.set_xticks(ticks)
    a2.set_xticklabels(tlabels, fontsize=7.8)
    a2.set_xlim(-0.7, 2.0)
    a2.set_ylim(-2.7, 8.2)
    a2.set_ylabel("Expected points per trade")
    return finish(fig, "ch04c_horizon_flips_sign")


# --------------------------------------------------------------------------------------------------
# Figure 4-C.3: the cheapest cure sells the best loan (Math, Gently in 4C.4)
# --------------------------------------------------------------------------------------------------
def fig_cheapest_cure():
    fig, (a1, a2) = new_figure("wide", ncols=2, gridspec_kw={"width_ratios": [1.05, 1.0]})
    excess = 2.0   # $mm of CCC excess over the 7.5% limit in Rachel's flagship pool
    p = np.linspace(50, 100, 100)
    a1.plot(p, excess * (1 - p / 100), color=INK_2, linewidth=LW)
    a1.axhline(excess * (1 - 0.58), color=NEUTRAL, linewidth=1.0, linestyle=(0, (4, 3)), zorder=1)
    a1.text(99.5, excess * 0.42 - 0.03, "do nothing: excess counted\nat the lowest price, 58: 0.84", ha="right", va="top",
            fontsize=7.8, color=INK_2)
    pts = [(58, "Sell the dentist loan", (7, 7), "left", "bottom"), (77, "Sell Halvorsen", (7, 7), "left", "bottom"),
           (86, "Sell the software loan", (-7, -7), "right", "top")]
    for px, lab, off, ha, va in pts:
        cost = excess * (1 - px / 100)
        a1.plot([px], [cost], "o", color=SEAT["clo"], markersize=7.5, zorder=5, markeredgecolor=INK_2, markeredgewidth=0.7)
        a1.annotate(f"{lab} at {px}\ncosts {cost:.2f}", (px, cost), xytext=off, textcoords="offset points", ha=ha,
                    va=va, fontsize=8, color=INK_2)
    a1.set_xlim(50, 100)
    a1.set_ylim(0, 1.05)
    a1.set_xlabel("Price of the loan sold (cents on the dollar)")
    a1.set_ylabel("Cost to the OC numerator (\\$mm)")

    # right: the same rule in two pools
    pools = [("Rachel's pool", [("software loan (86)", 86), ("Halvorsen (77)", 77), ("dentist loan (58)", 58)]),
             ("Another manager's pool (illustrative)", [("Halvorsen (77)", 77), ("CCC loan (66)", 66), ("CCC loan (54)", 54)])]
    y = 0.0
    yt, yl = [], []
    for pname, loans in pools:
        a2.text(0.0, y + 0.95, pname, ha="left", va="center", fontsize=8.2, color=INK)
        for j, (nm, px) in enumerate(loans):
            cost = excess * (1 - px / 100)
            best = j == 0
            a2.barh(y, cost, height=0.72, color=SEAT["clo"] if best else NEUTRAL, zorder=3,
                    edgecolor=INK_2 if best else "none", linewidth=0.7 if best else 0)
            a2.text(cost + 0.015, y, f"{cost:.2f}" + ("   cheapest cure" if best else ""), va="center", fontsize=8,
                    color=INK_2)
            yt.append(y); yl.append(nm)
            y -= 1.0
        y -= 1.0
    a2.set_yticks(yt)
    a2.set_yticklabels(yl, fontsize=8)
    a2.set_xlim(0, 1.3)
    a2.set_ylim(y + 0.9, 1.6)
    a2.grid(True, axis="x")
    a2.grid(False, axis="y")
    a2.set_xlabel("Cost of curing the \\$2mm excess (\\$mm)")
    return finish(fig, "ch04c_cheapest_cure")


# --------------------------------------------------------------------------------------------------
# Figure 4-C.4: one path, seven ledgers (4C.5)
# --------------------------------------------------------------------------------------------------
def step_xy(days, vals, x_end=31.0):
    """Post-step (value holds until the next date) as plotting arrays."""
    xs, ys = [], []
    for i, (d, v) in enumerate(zip(days, vals)):
        xs.append(d); ys.append(v)
        nxt = days[i + 1] if i + 1 < len(days) else x_end
        xs.append(nxt); ys.append(v)
    return np.array(xs), np.array(ys)


def fig_one_path_seven_ledgers():
    fig, axes = new_figure((7.0, 7.1), nrows=4, ncols=2, sharex=True)
    axes = axes.ravel()
    xe = 31.0
    d, px = PRINT_DAYS, PRINT_PX

    def base(ax, title, ylab=None):
        ax.set_title(title, fontsize=8.2, pad=3)
        ax.set_xlim(0, xe)
        ax.axvline(9, color=NEUTRAL, linewidth=0.8, linestyle=(0, (3, 3)), zorder=1)
        if ylab:
            ax.set_ylabel(ylab, fontsize=8)
        ax.tick_params(labelsize=8)

    # 0. the price path
    ax = axes[0]
    base(ax, "The seven prints of the 7.25% notes", "Price (points)")
    ax.plot(d, px, color=INK_2, linewidth=LW, zorder=3)
    ax.plot(d, px, "o", color=INK_2, markersize=4.5, zorder=4)
    for dd, pp, dx, dy in [(1, 92, 0, 6), (2, 78, 5, -9), (4, 81, 6, 4), (12, 74, 3, 6), (16, 72, 0, -11), (23, 76, 0, 6), (30, 70, 0, -11)]:
        ax.annotate(f"{pp:.0f}", (dd, pp), xytext=(dx, dy), textcoords="offset points", ha="center", va="center", fontsize=8, color=INK_2)
    ax.set_ylim(64, 98)
    ax.text(9.5, 96.6, "day 9: Caa1", fontsize=7.6, color=MUTED, va="top")

    # 1. desk, mark to market on 12mm face
    ax = axes[1]
    base(ax, "Desk: mark-to-market P&L (\\$mm)")
    pl = 12 * (px - 92) / 100.0
    ax.plot(d, pl, color=SEAT["desk"], linewidth=LW, zorder=3)
    ax.plot(d, pl, "o", color=SEAT["desk"], markersize=4, zorder=4)
    ax.axhline(0, color=NEUTRAL, linewidth=0.8)
    ax.text(2.4, -2.55, "12mm face: −1.68 on day 2", fontsize=7.6, color=INK_2, va="center")
    ax.set_ylim(-3.1, 0.35)

    # 2. dealer inventory
    ax = axes[2]
    base(ax, "Dealer: inventory (\\$mm face)")
    ax.step([0, 1, 3, 16, 16.45, xe], [0, 15, 0, 40, 0, 0], where="post", color=SEAT["dealer"], linewidth=LW, zorder=3)
    ax.vlines(16, 0, 40, color=SEAT["dealer"], linewidth=LW)
    ax.text(3.3, 15.2, "bought 15 at 91.25, sold at 79:\nrealized −1.84", fontsize=7.6, color=INK_2, va="center")
    ax.text(15.5, 40, "block of 40, sold\nto the fund at 72", fontsize=7.6, color=INK_2, va="top", ha="right")
    ax.set_ylim(-3, 46)

    # 3. systematic fund
    ax = axes[3]
    base(ax, "Systematic fund: holding (\\$mm face)")
    ax.step([0, 1, 2, xe], [8, 8, 0, 0], where="post", color=SEAT["systematic"], linewidth=LW, zorder=3)
    ax.text(3.0, 4.2, "guard binds on day 2: sold 8 at 77;\nbonds are 81 two days later", fontsize=7.6, color=INK_2, va="center")
    ax.set_ylim(-0.6, 9.6)

    # 4. pod
    ax = axes[4]
    base(ax, "RV pod: P&L on 10mm long from 79 (\\$mm)")
    pd_days = np.array([3, 4, 12, 16, 23, 30])
    pod_pl = 10 * (np.array([79, 81, 74, 72, 76, 70]) - 79) / 100.0
    xs, ys = step_xy(pd_days, pod_pl)
    ax.plot(xs, ys, color=SEAT["pod"], linewidth=LW + 0.4, zorder=3)
    ax.axhline(0, color=NEUTRAL, linewidth=0.8)
    ax.text(3.0, -0.93, "−0.5 on day 12: booked,\nnot acted on", fontsize=7.6, color=INK_2, va="center")
    ax.set_ylim(-1.15, 0.45)

    # 5. CLO OC numerator
    ax = axes[5]
    base(ax, "CLO manager: OC numerator (\\$mm vs day 1)")
    xs, ys = step_xy(np.array([0, 9, 11]), np.array([0.0, -0.84, -0.28]))
    ax.plot(xs, ys, color=SEAT["clo"], linewidth=LW + 0.4, zorder=3)
    ax.axhline(0, color=NEUTRAL, linewidth=0.8)
    ax.text(9.4, -0.97, "excess of 2 counted at the lowest\nprice, 58: −0.84", fontsize=7.6, color=INK_2, va="top", ha="left")
    ax.text(11.4, -0.18, "sells the 86 loan: −0.28", fontsize=7.6, color=INK_2, va="center", ha="left")
    ax.set_ylim(-1.4, 0.25)

    # 6. insurer, amortized cost
    ax = axes[6]
    base(ax, "Insurer: amortized cost (per 100 face)")
    ax.plot(d, px, color=NEUTRAL, linewidth=1.0, zorder=2)
    ax.plot([0, xe], [99, 99], color=SEAT["insurer"], linewidth=LW + 0.4, zorder=3)
    ax.text(3.5, 95.6, "book stays 99 until impairment", fontsize=7.6, color=INK_2, va="top")
    ax.text(30.6, 71.4, "market", fontsize=7.6, color=MUTED, ha="right", va="top")
    ax.set_ylim(64, 101)
    ax.set_xlabel("Trading day", fontsize=8.5)

    # 7. direct lender, quarterly mark
    ax = axes[7]
    base(ax, "Direct lender: quarterly mark (per 100 face)")
    ax.plot(d, px, color=NEUTRAL, linewidth=1.0, zorder=2)
    xs, ys = step_xy(np.array([0, 30]), np.array([92.0, 81.0]), x_end=xe)
    ax.plot(xs, ys, color=SEAT["direct"], linewidth=LW + 0.4, zorder=3)
    ax.text(5.0, 88.5, "92 until the quarter-end mark\n(assumed day 30): half the move, 81", fontsize=7.6, color=INK_2, va="top")
    ax.text(30.6, 71.4, "market", fontsize=7.6, color=MUTED, ha="right", va="top")
    ax.set_ylim(64, 101)
    ax.set_xlabel("Trading day", fontsize=8.5)
    return finish(fig, "ch04c_one_path_seven_ledgers")


# --------------------------------------------------------------------------------------------------
# Figure 4-C.5: the coalition map (4C.8)
# --------------------------------------------------------------------------------------------------
def fig_coalition_map():
    W, H = 100.0, 85.5
    fig, ax = new_figure((7.0, 7.0 * H / W))
    ax.set_xlim(0, W); ax.set_ylim(0, H)
    ax.set_aspect("equal"); ax.axis("off"); ax.grid(False)

    cols = [("systematic", "Systematic\nfund"), ("clo", "CLO\nmanager"), ("dealer", "Dealer"), ("pod", "RV pod"),
            ("opp", "Opportunistic\nfund"), ("insurer", "Life\ninsurer"), ("direct", "Direct\nlender")]
    cx = {k: 51.0 + 7.2 * i for i, (k, _) in enumerate(cols)}
    # class rows: name, face, group; y centres
    rows = [("ABL revolver", 150, "abl"), ("First-lien term loan B", 900, "fl"), ("7.25% secured notes 2029", 500, "fl"),
            ("6% unsecured notes 2031", 600, "un"), ("3% unsecured notes 2045", 250, "un"),
            ("Trade payables", 150, "un"), ("Lease rejection claim", 60, "un")]
    ry = {i: 49.0 - 5.6 * i for i in range(len(rows))}          # 49.0 ... 15.4
    ip_y = 7.4
    bar_x0, scale = 27.5, 16.5 / 900.0
    fill = {"abl": MUTED, "fl": INK_2, "un": NEUTRAL}

    # background bands for the two classes
    ax.add_patch(Rectangle((0, ry[2] - 2.8), W, 11.2, fc="#ecebe7", ec="none", zorder=0))
    ax.add_patch(Rectangle((0, ry[6] - 2.8), W, 22.4, fc=TINT, ec="none", zorder=0))
    ax.text(1.0, (ry[1] + ry[2]) / 2, "FIRST LIEN", rotation=90, ha="center", va="center", fontsize=6.6, color=MUTED)
    ax.text(1.0, (ry[3] + ry[6]) / 2, "UNSECURED", rotation=90, ha="center", va="center", fontsize=6.6, color=MUTED)

    # headers in two tiers so the names do not collide; the colour dot under each name is the seat's key
    for i, (k, lab) in enumerate(cols):
        upper = i % 2 == 0
        y_dot = 79.6 if upper else 74.8
        y_lab = y_dot + 3.5
        ax.text(cx[k], y_lab, lab, ha="center", va="center", fontsize=7.8, color=INK, linespacing=1.1)
        ax.add_patch(Circle((cx[k], y_dot), 1.25, fc=SEAT[k], ec="none", zorder=4))
        ax.plot([cx[k], cx[k]], [ip_y - 2.8, y_dot - 1.4], color=GRID, linewidth=0.9, zorder=1)

    # flow ladder (chronological, top to bottom)
    lanes = [(70.2, "systematic", "dealer", "8", "Day 2: the guard sells 8 into dealers' bids (best 77)"),
             (67.0, "dealer", "pod", "10", "Day 3: Dana sells 10 to the pod at 79 (5 more elsewhere)"),
             (63.8, "clo", "dealer", "40", "Day 16: a CLO and a separate account send Dana a 40 block"),
             (60.6, "dealer", "opp", "40", "Day 16: Dana sells all 40 at 72")]
    ax.text(1.0, 74.8, "The month's flows (\\$mm face)", ha="left", va="center", fontsize=7.6, color=MUTED)
    for y, a_, b_, sz, txt in lanes:
        fwd = cx[b_] > cx[a_]
        ax.add_patch(Circle((cx[a_], y), 0.95, fc=SEAT[a_], ec="none", zorder=5))
        ax.add_patch(FancyArrowPatch((cx[a_] + (1.0 if fwd else -1.0), y), (cx[b_] - (0.8 if fwd else -0.8), y),
                                     arrowstyle="-|>", mutation_scale=9, color=INK_2, linewidth=1.2, zorder=4))
        ax.text((cx[a_] + cx[b_]) / 2, y + 1.0, sz, ha="center", va="bottom", fontsize=7.8, color=INK_2, zorder=6)
        ax.text(1.0, y, txt, ha="left", va="center", fontsize=6.9, color=INK_2)
    ax.plot([0, W], [57.4, 57.4], color=GRID, linewidth=1.0, zorder=1)

    # cap table
    ax.text(1.0, 55.0, "Capital structure (\\$mm; bar = face) and who holds it on day 30", ha="left", va="center", fontsize=7.6, color=MUTED)
    for i, (name, face, grp) in enumerate(rows):
        y = ry[i]
        ax.text(3.4, y, name, ha="left", va="center", fontsize=7.7, color=INK)
        ax.add_patch(Rectangle((bar_x0, y - 1.5), face * scale, 3.0, fc=fill[grp], ec="none", zorder=3))
        ax.text(bar_x0 + face * scale + 0.9, y, f"{face:,}", ha="left", va="center", fontsize=7.4, color=INK_2)

    def dot(k, i, kind="held", label=None, above=False):
        x, y = cx[k], ry[i]
        c = SEAT[k]
        if kind == "held":
            ax.add_patch(Circle((x, y), 1.45, fc=c, ec="none", zorder=5))
        elif kind == "out":
            ax.add_patch(Circle((x, y), 1.45, fc=SURFACE, ec=c, linewidth=1.6, zorder=5))
        elif kind == "via":
            ax.add_patch(Circle((x, y), 1.45, fc=SURFACE, ec=c, linewidth=1.6, linestyle=(0, (1.6, 1.2)), zorder=5))
        if label:
            ax.text(x, y + (2.2 if above else -2.2), label, ha="center", va="bottom" if above else "top", fontsize=6.9,
                    color=INK_2, zorder=6, linespacing=1.1)

    dot("systematic", 2, "out", "out at 77")
    dot("clo", 1, "held", "Caa1 loan")
    dot("dealer", 2, "out", "flat")
    dot("pod", 2, "held", "long 10")
    dot("pod", 3, "held", "short 3.8")
    dot("opp", 2, "held", "40")
    dot("insurer", 1, "via", "via CLO\ntranche")
    dot("direct", 1, "held", "15, liquid\nsleeve", above=True)

    # the IP subsidiary row and the declined arrow
    ax.plot([0, W], [12.4, 12.4], color=GRID, linewidth=1.0, zorder=1)
    ax.text(3.4, ip_y + 0.3, "IP subsidiary: the patents", ha="left", va="center", fontsize=7.7, color=INK)
    ax.text(3.4, ip_y - 2.6, "new money asked for: \\$200mm", ha="left", va="center", fontsize=6.9, color=MUTED)
    ax.add_patch(Rectangle((bar_x0, ip_y - 1.5 + 0.3), 200 * scale, 3.0, fc=SURFACE, ec=NEUTRAL, linewidth=1.2,
                           linestyle=(0, (3, 2)), zorder=3))
    ax.text(bar_x0 + 200 * scale + 0.9, ip_y + 0.3, "200", ha="left", va="center", fontsize=7.4, color=INK_2)
    ax.add_patch(FancyArrowPatch((cx["direct"], ry[1] - 2.0), (cx["direct"], ip_y + 2.6), arrowstyle="-|>", mutation_scale=9,
                                 color=SEAT["direct"], linewidth=1.4, linestyle=(0, (3, 2)), zorder=4))
    ax.text(cx["direct"], ip_y + 0.3, "✕", ha="center", va="center", fontsize=10, color=INK, fontweight="bold", zorder=7)
    ax.text(cx["direct"] - 2.0, ip_y + 0.3, "declined on day 16", ha="right", va="center", fontsize=7.2, color=INK_2)

    # key
    kx, ky = 1.0, 1.6
    ax.add_patch(Circle((kx + 1.2, ky), 0.95, fc=INK_2, ec="none"))
    ax.text(kx + 3.0, ky, "holds on day 30", fontsize=6.9, color=MUTED, va="center")
    ax.add_patch(Circle((kx + 24.0, ky), 0.95, fc=SURFACE, ec=INK_2, linewidth=1.3))
    ax.text(kx + 25.8, ky, "sold out or flat", fontsize=6.9, color=MUTED, va="center")
    ax.add_patch(Circle((kx + 45.0, ky), 0.95, fc=SURFACE, ec=INK_2, linewidth=1.3, linestyle=(0, (1.6, 1.2))))
    ax.text(kx + 46.8, ky, "holds through a vehicle", fontsize=6.9, color=MUTED, va="center")
    return finish(fig, "ch04c_coalition_map")


if __name__ == "__main__":
    fig_seven_clocks()
    fig_horizon_flips_sign()
    fig_cheapest_cure()
    fig_one_path_seven_ledgers()
    fig_coalition_map()
