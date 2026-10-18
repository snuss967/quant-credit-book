"""Figures for Chapter 4-D (Getting the Seat: Interviews for Market-Making and Systematic Credit).

Run:  python3 tools/figures/ch04d.py   -> assets/figures/ch04d_*.png

Every figure is "Illustrative": Theo, the five rooms and every question are fictional composites, and each figure is
drawn from numbers the chapter states or from the stated model (Bayes with one seller in five informed; Kelly with
a trapdoor; a two-clock join; a 16x turnover cost model).  No real series is used, so there is no data file.

Figures (in order of appearance in the chapter):
  4-D.1 ch04d_interview_funnel          the funnel by business (section 4D.1)
  4-D.2 ch04d_one_price_three_worlds    one price, two measures, three doors (section 4D.2)
  4-D.3 ch04d_live_counterparty_update  Bayes against a live counterparty (section 4D.3)
  4-D.4 ch04d_kelly_trapdoor            Kelly with a trapdoor (section 4D.5)
  4-D.5 ch04d_two_clocks_join           the point-in-time join (section 4D.8)
  4-D.6 ch04d_sharpe_vs_cost            Kaz's Sharpe 3.1 against the cost per dollar traded (section 4D.9)

Colour roles in this chapter: the measure Q = BLUE and the measure P = ORANGE wherever they appear together; the third
world (three doors) = AQUA, direct-labelled because AQUA is below 3:1 on white.  In the Bayes figure the informed path is
ORANGE and the noise path BLUE.  In the Kelly figure the default probability is one hue (SEQ_BLUE, light = low).
In the join figure the as-of join is BLUE and the naive merge ORANGE.  Reference lines (stops, ruin line, price) are
NEUTRAL or ink.  Status colours are not used.
"""
import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from style import *  # noqa: E402,F401,F403  (applies the rcParams on import)

import textwrap  # noqa: E402

import numpy as np  # noqa: E402
from matplotlib.patches import Rectangle  # noqa: E402

Q_COLOR, P_COLOR, THIRD_COLOR = BLUE, ORANGE, AQUA


# --------------------------------------------------------------------------------------------------
# Figure 4-D.1: the funnel by business (section 4D.1)
# --------------------------------------------------------------------------------------------------
def fig_interview_funnel():
    cols = [("Market maker", "Thursday"), ("Multi-strategy pod", "Tuesday"), ("Systematic manager", "Wednesday"),
            ("Bank desk", "Monday"), ("Distressed fund", "Friday")]
    head = {"Market maker": "Market\nmaker", "Multi-strategy pod": "Multi-strategy\npod",
            "Systematic manager": "Systematic\nmanager", "Bank desk": "Bank\ndesk",
            "Distressed fund": "Distressed\nfund"}
    stages = ["Screen", "Puzzles", "Coding", "Pitch", "Portfolio", "Offer"]
    # business -> six stages, each (what the stage screens for, where the book trains it, weight 0..3)
    table = {
        "Market maker": [("A document reader who can learn to quote", "§3.7, §4D.1", 2),
                         ("Update against a live counterparty", "§3.2, §4D.3", 3),
                         ("Replay a hand history; tidy a tape", "§3.3, §4D.8", 3),
                         ("Break my backtest: why is the Sharpe 3.1?", "§4D.9", 2),
                         ("RFQ game, TRACE spreads, ETF premium", "Projects 1, 4, 5", 3),
                         ("Hiring note: moved late, moved right", "§4D.4", 2)],
        "Multi-strategy pod": [("Idio view; never stopped out, no P&L yet", "§4D.5", 2),
                               ("Kelly, then the stop: size to the loss", "§4D.5", 2),
                               ("Rarely tested; size a pair in a sheet", "§8.6", 1),
                               ("Name the short leg and the ruler", "§4D.6, Ch 8-D", 3),
                               ("Projects 8, 12, or a pair from 2 or 11", "§4D.11", 2),
                               ("Platform risk: what is it long that it did not mean to be?", "§4D.6", 2)],
        "Systematic manager": [("Python, SQL, single-name credit on the posting", "§4D.1", 2),
                               ("Fermi chain with error bars", "§4D.7, §28.2", 2),
                               ("As-of joins, purged CV, issuer groups", "§4D.8, §7.7", 3),
                               ("Defend the costs and the issuer count", "§4D.9, §7.6", 1),
                               ("Projects 1, 6, 9", "§4D.11", 2),
                               ("Scorecard of 1 to 4; calibration meeting", "§4D.8", 1)],
        "Bank desk": [("Credit-trading résumé; can price a list fast", "§4D.1", 1),
                      ("“In which measure?” Q or P", "§4D.2", 3),
                      ("DV01 and DTS by hand, then a price list", "Ch 4-B", 1),
                      ("Price a portfolio trade", "Ch 2, Ch 19", 1),
                      ("Projects 1, 5, 8", "§4D.11", 2),
                      ("A seat on the risk-pricing desk", "Ch 18", 1)],
        "Distressed fund": [("Résumé is already the native language", "§4D.1", 3),
                            ("The restricted list: your legal state", "§4D.10", 1),
                            ("Rarely tested; show the 13-week model", "§5.1.5", 0),
                            ("The plan as a distribution, not a memo", "§4D.10", 3),
                            ("Projects 2, 3, 10, 11", "§4D.11", 2),
                            ("Seat offered in the room; declined", "§4D.10", 1)],
    }
    shades = ["#f3f2ef", "#d6e6fa", "#a9cbf5", "#6da7ec"]

    fig, ax = new_figure((7.0, 8.0))
    ax.axis("off")
    ax.set_xlim(-0.95, 5.0)
    ax.set_ylim(7.0, -0.9)
    gap = 0.045
    for j, (bname, day) in enumerate(cols):
        ax.text(j + 0.5, -0.52, head[bname], ha="center", va="center", fontsize=8.4, color=INK, fontweight="bold",
                linespacing=1.15)
        ax.text(j + 0.5, -0.12, day, ha="center", va="center", fontsize=7.4, color=MUTED)
    for i, st in enumerate(stages):
        ax.text(-0.06, i + 0.5, st, ha="right", va="center", fontsize=8.4, color=INK, fontweight="bold")
        ax.text(-0.06, i + 0.5 + 0.17, f"stage {i + 1}", ha="right", va="center", fontsize=7, color=MUTED)
        for j, (bname, _) in enumerate(cols):
            what, where, w = table[bname][i]
            ax.add_patch(Rectangle((j + gap, i + gap), 1 - 2 * gap, 1 - 2 * gap, facecolor=shades[w], zorder=1))
            body = "\n".join(textwrap.wrap(what, 19))
            ax.text(j + 0.5, i + 0.42, body, ha="center", va="center", fontsize=7.0, color=INK, zorder=3,
                    linespacing=1.22)
            ax.text(j + 0.5, i + 0.89, where, ha="center", va="center", fontsize=7.0, color=INK_2, zorder=3,
                    fontstyle="italic")
    # arrow down the left margin: the order of the stages
    ax.annotate("", xy=(-0.82, 5.95), xytext=(-0.82, 0.05),
                arrowprops=dict(arrowstyle="-|>", color=NEUTRAL, linewidth=1.0, mutation_scale=9))
    # legend
    ax.text(0.0, 6.5, "How heavily the business weighs the stage:", ha="left", va="center", fontsize=7.6, color=INK_2)
    labels = ["rarely", "lightly", "fairly", "most"]
    x0 = 2.05
    for k, lab in enumerate(labels):
        ax.add_patch(Rectangle((x0 + k * 0.72, 6.38), 0.2, 0.25, facecolor=shades[k], zorder=2,
                               edgecolor=NEUTRAL, linewidth=0.5))
        ax.text(x0 + k * 0.72 + 0.25, 6.505, lab, ha="left", va="center", fontsize=7.4, color=INK_2)
    return finish(fig, "ch04d_interview_funnel")


# --------------------------------------------------------------------------------------------------
# Figure 4-D.2: one price, two measures, three doors (section 4D.2)
# --------------------------------------------------------------------------------------------------
def fig_one_price_three_worlds():
    fig, (a1, a2) = new_figure("wide", ncols=2)
    w = 5.2

    def bars(ax, xs, ps, col, dx):
        for x, p in zip(xs, ps):
            ax.bar(x + dx, p, width=w, color=col, zorder=3)
            ax.annotate(f"{p:.0%}", (x + dx, p), xytext=(0, 3), textcoords="offset points", ha="center",
                        va="bottom", fontsize=8, color=INK_2)

    # left: the same two outcomes under Q and under P
    q_def, p_def = 0.25, 0.10
    bars(a1, [40, 100], [q_def, 1 - q_def], Q_COLOR, -3.2)
    bars(a1, [40, 100], [p_def, 1 - p_def], P_COLOR, +3.2)
    ev_q = 100 * (1 - q_def) + 40 * q_def
    ev_p = 100 * (1 - p_def) + 40 * p_def
    assert abs(ev_q - 85) < 1e-9 and abs(ev_p - 94) < 1e-9
    a1.plot([ev_q], [0], marker="^", color=Q_COLOR, markersize=9, zorder=6, clip_on=False, markeredgewidth=0)
    a1.plot([ev_p], [0], marker="^", color=P_COLOR, markersize=9, zorder=6, clip_on=False, markeredgewidth=0)
    a1.set_xlim(25, 114)
    a1.set_ylim(0, 1.32)
    a1.set_xticks([40, 100])
    a1.set_xticklabels(["40 (default)", "100 (par)"])
    a1.set_xlabel("Payoff in a year (points);  \u25b2 = expected payoff")
    a1.set_ylabel("Probability")
    a1.set_yticks([0, 0.25, 0.5, 0.75, 1.0])
    a1.set_yticklabels(["0", "25%", "50%", "75%", "100%"])
    a1.text(0.02, 0.98, "Same two outcomes, two sets of weights", transform=a1.transAxes, ha="left", va="top",
            fontsize=8.6, color=INK, fontweight="bold")
    a1.plot([29.0], [1.15], "s", color=Q_COLOR, markersize=5.5, clip_on=False, markeredgewidth=0)
    a1.plot([29.0], [1.06], "s", color=P_COLOR, markersize=5.5, clip_on=False, markeredgewidth=0)
    a1.text(32, 1.15, "Q, risk-neutral: 25% default, mean 85", ha="left", va="center", fontsize=7.9, color=INK_2)
    a1.text(32, 1.06, "P, physical (assumed): 10% default, mean 94", ha="left", va="center", fontsize=7.9,
            color=INK_2)

    # right: the same price, a different world (a third door)
    two = [0.25, 0.75]
    three = [0.10, 0.30, 0.60]
    mean2 = 40 * 0.25 + 100 * 0.75
    mean3 = 40 * 0.10 + 70 * 0.30 + 100 * 0.60
    assert abs(mean2 - 85) < 1e-9 and abs(mean3 - 85) < 1e-9
    sd2 = np.sqrt(0.25 * 0.75) * 60
    sd3 = np.sqrt(0.10 * 45 ** 2 + 0.30 * 15 ** 2 + 0.60 * 15 ** 2)
    print(f"  sd two-door {sd2:.1f}, sd three-door {sd3:.1f}")
    bars(a2, [40, 100], two, Q_COLOR, -3.2)
    bars(a2, [40, 70, 100], three, THIRD_COLOR, +3.2)
    a2.plot([85], [0], marker="^", color=INK_2, markersize=9, zorder=6, clip_on=False, markeredgewidth=0)
    # AQUA is below 3:1 on white, so the third world is also labelled directly (the bar at 70 exists only in it)
    a2.annotate("three doors", (70 + 3.2, 0.30), xytext=(0, 17), textcoords="offset points", ha="center",
                va="bottom", fontsize=8, color=INK_2)
    a2.set_xlim(25, 114)
    a2.set_ylim(0, 1.32)
    a2.set_xticks([40, 70, 100])
    a2.set_xticklabels(["40 (default)", "70 (exchange)", "100 (par)"])
    a2.set_xlabel("Payoff in a year (points);  \u25b2 = the price, 85")
    a2.set_yticks([0, 0.25, 0.5, 0.75, 1.0])
    a2.set_yticklabels(["0", "25%", "50%", "75%", "100%"])
    a2.text(0.02, 0.98, "Same price, a different bond", transform=a2.transAxes, ha="left", va="top",
            fontsize=8.6, color=INK, fontweight="bold")
    a2.plot([29.0], [1.15], "s", color=Q_COLOR, markersize=5.5, clip_on=False, markeredgewidth=0)
    a2.plot([29.0], [1.04], "s", color=THIRD_COLOR, markersize=5.5, clip_on=False, markeredgewidth=0)
    a2.text(32, 1.15, f"two doors: 25% default, sd {sd2:.0f}", ha="left", va="center", fontsize=7.9, color=INK_2)
    a2.text(32, 1.04, f"three doors: 10% default, 40% not paid\nin full, sd {sd3:.0f}", ha="left", va="center",
            fontsize=7.9, color=INK_2, linespacing=1.25)
    return finish(fig, "ch04d_one_price_three_worlds")


# --------------------------------------------------------------------------------------------------
# Figure 4-D.3: the live-counterparty update (section 4D.3)
# --------------------------------------------------------------------------------------------------
LR_SELL = 0.6 / 0.4           # likelihood ratio of a sale for the bad state: P(sell|bad)/P(sell|good)
LR_BUY = 0.4 / 0.6


def update_path(trades):
    """Posterior P(worth 40) before any trade and after each trade; trades are 'S' (they sell to us) or 'B'."""
    odds, post = 1.0, [0.5]
    for t in trades:
        odds *= LR_SELL if t == "S" else LR_BUY
        post.append(odds / (1.0 + odds))
    return np.array(post)


def quotes(post):
    """Bid and ask for the next trade at a given posterior: the bond's value given a sale / given a purchase."""
    pi_s = 0.6 * post / (0.6 * post + 0.4 * (1 - post))
    pi_b = 0.4 * post / (0.4 * post + 0.6 * (1 - post))
    return 100 - 60 * pi_s, 100 - 60 * pi_b


def fig_live_counterparty_update():
    inf_path = "SSSSSS"
    noise_path = "SBSSBB"
    pi_inf, pi_noise = update_path(inf_path), update_path(noise_path)
    assert np.allclose(pi_inf[1:], [0.60, 0.69, 0.77, 0.84, 0.88, 0.92], atol=0.005)
    assert np.allclose(pi_noise[1:], [0.60, 0.50, 0.60, 0.69, 0.60, 0.50], atol=0.005)
    k = np.arange(7)
    fig, (a1, a2) = new_figure("wide", ncols=2)

    a1.plot([0, 6], [0.5, 0.5], color=NEUTRAL, linewidth=0.9, linestyle=(0, (3, 3)), zorder=1)
    a1.plot(k, pi_noise, "-o", color=BLUE, zorder=3)
    a1.plot(k, pi_inf, "-o", color=ORANGE, zorder=4)
    for i, t in enumerate(noise_path, start=1):
        if i in (1, 6):
            continue
        a1.annotate("sell" if t == "S" else "buy", (i, pi_noise[i]), xytext=(0, -12 if t == "B" else 9),
                    textcoords="offset points", ha="center", va="center", fontsize=7.4, color=MUTED)
    label_end(a1, 6, pi_inf[-1], "informed seller:\nsix sales in a row", ORANGE, dx=6, linespacing=1.15)
    label_end(a1, 6, pi_noise[-1], "noise path:\nsell, buy, sell,\nsell, buy, buy", BLUE, dx=6,
              linespacing=1.15)
    a1.set_xlim(-0.3, 8.7)
    a1.set_ylim(0.4, 1.0)
    a1.set_xlabel("Trades seen")
    a1.set_ylabel("Probability the bond is worth 40")
    a1.set_xticks(k)
    a1.set_yticks([0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
    a1.set_yticklabels(["40%", "50%", "60%", "70%", "80%", "90%", "100%"])
    a1.annotate("prior", (0, 0.5), xytext=(0, -11), textcoords="offset points", fontsize=7.6, color=MUTED, va="top",
                ha="center")

    for pi, col, nm in [(pi_noise, BLUE, "noise"), (pi_inf, ORANGE, "informed")]:
        bid, ask = quotes(pi)
        a2.fill_between(k, bid, ask, color=col, alpha=0.22, linewidth=0, zorder=2)
        a2.plot(k, bid, "-", color=col, linewidth=1.2, zorder=3)
        a2.plot(k, ask, "-", color=col, linewidth=1.2, zorder=3)
        print(f"  {nm}: spread at k=0 {ask[0]-bid[0]:.1f}, at k=6 {ask[-1]-bid[-1]:.1f}, mid at k=6 {(ask[-1]+bid[-1])/2:.1f}")
        if nm == "informed":
            mid = 0.5 * (bid + ask)
            a2.plot(k, mid, "--", color=col, linewidth=1.0, zorder=3)
            a2.annotate("informed path:\nmid falls toward 45", (4.0, mid[4]), xytext=(1.9, 41.5), textcoords="data",
                        ha="center", va="center", fontsize=8, color=INK_2, linespacing=1.15,
                        arrowprops=dict(arrowstyle="-", color=NEUTRAL, linewidth=0.8))
            a2.annotate("spread narrows\n12 \u2192 3.7", (6.0, mid[6]), xytext=(5.0, 38.5), ha="center", va="center",
                        fontsize=8, color=INK_2, linespacing=1.15,
                        arrowprops=dict(arrowstyle="-", color=NEUTRAL, linewidth=0.8))
    a2.text(0.55, 83.5, "noise path: quotes stay in 54\u201376", fontsize=7.9, color=INK_2, ha="left",
            va="center")
    a2.plot([0.3], [83.5], "s", color=BLUE, markersize=5.5, clip_on=False, markeredgewidth=0)
    a2.set_ylim(34, 88)
    a2.set_xlim(-0.3, 6.3)
    a2.set_xticks(k)
    a2.set_xlabel("Trades seen (quote for the next trade)")
    a2.set_ylabel("Bid and ask (points)")
    return finish(fig, "ch04d_live_counterparty_update")


# --------------------------------------------------------------------------------------------------
# Figure 4-D.4: Kelly with a trapdoor (section 4D.5)
# --------------------------------------------------------------------------------------------------
CARRY = 0.045


def kelly(q_d, L, c=CARRY):
    return (1 - q_d) / L - q_d / c


def fig_kelly_trapdoor():
    fig, ax = new_figure((7.0, 4.3))
    L = np.linspace(0.3, 1.0, 400)
    qs = [0.01, 0.02, 0.031, 0.045, 0.06]
    cols = [SEQ_BLUE(v) for v in np.linspace(0.22, 0.95, len(qs))]
    floor = 0.05      # a log axis cannot show zero: each curve is cut at 5% of capital
    ax.set_yscale("log")
    # ruin line
    ax.plot(L, 1 / L, color=INK_2, linewidth=1.2, linestyle=(0, (5, 3)), zorder=2)
    ax.annotate("ruin line  f = 1/L:  one default wipes out the fund", (0.44, 1 / 0.44), xytext=(0, 7),
                textcoords="offset points", ha="left", va="bottom", fontsize=8, color=INK_2)
    # pod stop and single-default line: a dollar loss limit divided by L, so both ceilings fall as L rises.
    # The chapter's $25.9mm (12.9%) and $8.6mm (4.3%) are their values at L = 0.58, the 98-dollar bond that
    # recovers 40; the dots mark that point.
    l_hy = 0.58
    assert abs(0.075 / l_hy - 25.9 / 200) < 5e-4 and abs(0.025 / l_hy - 8.6 / 200) < 5e-4
    for lim, txt in [(0.075, "pod stop: \\$15mm loss limit / L\n12.9% = \\$25.9mm at the dot"),
                     (0.025, "single-default line: \\$5mm / L\n4.3% = \\$8.6mm at the dot")]:
        ax.plot(L, lim / L, color=MUTED, linewidth=1.2, zorder=1)
        ax.plot([l_hy], [lim / l_hy], "o", color=MUTED, markersize=4.5, zorder=2)
        ax.annotate(txt, (1.0, lim / 1.0), xytext=(7, 0), textcoords="offset points", ha="left", va="center",
                    fontsize=8, color=INK_2, linespacing=1.15)
    # Kelly curves, one per default probability
    for q, col in zip(qs, cols):
        f = kelly(q, L)
        ok = f >= floor
        lw = LW + 0.9 if abs(q - 0.031) < 1e-9 else LW
        ax.plot(L[ok], f[ok], color=col, linewidth=lw, zorder=3, solid_capstyle="round")
        xe, ye = L[ok][-1], f[ok][-1]
        lab = f"$q_D$ = {q * 100:.1f}%".replace(".0%", "%")
        if ye > floor * 1.5:
            label_end(ax, xe, ye, lab, col, dx=12 if abs(q - 0.031) < 1e-9 else 5)
        else:
            label_end(ax, xe, ye, lab, col, dx=5)
    # Theo's dot and the document's dot
    th, doc = kelly(0.031, 0.6), kelly(0.031, 1.0)
    print(f"  Kelly at (3.1%, 0.6): {th:.3f}; at L=1: {doc:.3f}; ruin 1/L: {1/0.6:.2f} -> 1.00")
    ax.plot([0.6], [th], "o", color=INK, markersize=8, zorder=6, markeredgecolor="white", markeredgewidth=0.8)
    ax.annotate("Theo's 93%\nat L = 0.6", (0.6, th), xytext=(0.315, 0.42), textcoords="data", ha="left",
                va="center", fontsize=8.4, color=INK, linespacing=1.15,
                arrowprops=dict(arrowstyle="-", color=NEUTRAL, linewidth=0.8, shrinkA=2, shrinkB=5))
    ax.plot([1.0], [doc], "o", color="white", markersize=8, zorder=6, markeredgecolor=INK, markeredgewidth=1.4)
    ax.annotate("same bond after an uptier,\nL = 1: Kelly 28%,\nruin line 100%", (1.0, doc), xytext=(0.99, 0.158),
                textcoords="data", ha="left", va="center", fontsize=8.2, color=INK, linespacing=1.15,
                arrowprops=dict(arrowstyle="-", color=NEUTRAL, linewidth=0.8, shrinkA=2, shrinkB=6))
    ax.set_xlim(0.3, 1.36)
    ax.set_ylim(0.017, 5.0)
    ax.set_xlabel("Loss given default L (share of the position lost)")
    ax.set_ylabel("Position, % of capital (log scale)")
    ticks = [0.025, 0.05, 0.1, 0.25, 0.5, 1.0, 2.0, 4.0]
    ax.set_yticks(ticks)
    ax.set_yticklabels([f"{t * 100:g}%" for t in ticks])
    ax.minorticks_off()
    ax.set_xticks([0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
    note(ax, "Carry c = 4.5%.  Curves are cut at 5% of capital; a little further right f* is negative: no bet.",
         loc="upper right")
    return finish(fig, "ch04d_kelly_trapdoor")


# --------------------------------------------------------------------------------------------------
# Figure 4-D.5: the point-in-time join (section 4D.8)
# --------------------------------------------------------------------------------------------------
def fig_two_clocks_join():
    import datetime as dt
    d = dt.date
    level = {"BB": 3, "B+": 2, "CCC+": 1}
    # an invented issuer: each downgrade is effective on one day and on the screen a few days later
    changes = [("B+", d(2025, 3, 13), d(2025, 3, 18)), ("CCC+", d(2025, 9, 9), d(2025, 9, 11))]
    start, end = d(2024, 1, 1), d(2025, 12, 31)
    trades = [d(2024, 2, 12), d(2024, 6, 10), d(2024, 10, 7), d(2025, 3, 14), d(2025, 7, 1)]

    def asof(day):
        r = "BB"
        for new, _, pub in changes:
            if pub <= day:
                r = new
        return r

    def true_rating(day):
        r = "BB"
        for new, eff, _ in changes:
            if eff <= day:
                r = new
        return r

    def num(x):
        return x.toordinal()

    fig, (ax, bx) = new_figure((7.0, 5.7), nrows=2, gridspec_kw={"height_ratios": [1.0, 0.95]})

    # ---- top: the whole period -----------------------------------------------------------------
    xs, ys = [num(start)], [level["BB"]]
    for new, eff, pub in changes:
        xs += [num(pub), num(pub)]
        ys += [ys[-1], level[new]]
    xs.append(num(end))
    ys.append(ys[-1])
    ax.plot(xs, ys, color=BLUE, linewidth=LW + 0.4, zorder=4, solid_joinstyle="miter")
    ax.plot([num(start), num(end)], [1, 1], color=ORANGE, linewidth=LW + 0.4, zorder=3)
    ax.axvspan(num(d(2025, 3, 8)), num(d(2025, 3, 26)), color=GRID, zorder=0, linewidth=0)
    for t in trades:
        a, n = level[asof(t)], level["CCC+"]
        ax.plot([num(t), num(t)], [n, a], color=NEUTRAL, linewidth=0.9, zorder=2)
        ax.plot([num(t)], [a], "o", color=BLUE, markersize=7, zorder=6, markeredgecolor="white", markeredgewidth=0.8)
        ax.plot([num(t)], [n], "o", color=ORANGE, markersize=7, zorder=6, markeredgecolor="white", markeredgewidth=0.8)
        ax.plot([num(t)], [0.62], "|", color=INK_2, markersize=9, markeredgewidth=1.3, zorder=6)
        print(f"  trade {t}: as-of {asof(t)}, effective-date {true_rating(t)}, naive CCC+")
    ax.text(num(trades[0]) - 8, 0.62, "trades", ha="right", va="center", fontsize=8, color=INK_2)
    ax.annotate("As-of join (blue): the latest rating published\nbefore the trade", (num(d(2024, 3, 20)), 3.0),
                xytext=(0, 20), textcoords="offset points", ha="left", va="center", fontsize=8.2, color=INK_2)
    ax.annotate("Naive merge (orange): today's rating, CCC+,\non every row", (num(d(2024, 1, 20)), -0.1),
                xytext=(0, 0), textcoords="offset points", ha="left", va="center", fontsize=8.2, color=INK_2)
    ax.annotate("zoom below", (num(d(2025, 3, 26)), 2.5), xytext=(8, 0), textcoords="offset points", ha="left",
                va="center", fontsize=7.8, color=MUTED)
    ax.set_ylim(-0.5, 3.85)
    ax.set_xlim(num(start), num(end) + 30)
    ax.set_yticks([1, 2, 3])
    ax.set_yticklabels(["CCC+", "B+", "BB"])
    ax.set_xticks([num(x) for x in [d(2024, 1, 1), d(2024, 7, 1), d(2025, 1, 1), d(2025, 7, 1)]])
    ax.set_xticklabels(["Jan 2024", "Jul 2024", "Jan 2025", "Jul 2025"])
    ax.set_ylabel("Rating attached to the trade")
    ax.set_xlabel("Trade date")

    # ---- bottom: the two clocks around one downgrade ---------------------------------------------
    eff, pub, tr = d(2025, 3, 13), d(2025, 3, 18), d(2025, 3, 14)
    x0, x1 = num(d(2025, 3, 8)), num(d(2025, 3, 26))
    bx.axvspan(num(eff), num(pub), color=GRID, zorder=0, linewidth=0)
    bx.plot([x0, num(eff), num(eff), x1], [3, 3, 2, 2], color=INK_2, linewidth=1.4, linestyle=(0, (4, 2)), zorder=3)
    bx.plot([x0, num(pub), num(pub), x1], [3, 3, 2, 2], color=BLUE, linewidth=LW + 0.4, zorder=4)
    bx.plot([num(tr)], [3], "o", color=BLUE, markersize=8, zorder=6, markeredgecolor="white", markeredgewidth=0.8)
    bx.plot([num(tr)], [2], "o", color="white", markersize=8, zorder=6, markeredgecolor=INK, markeredgewidth=1.5)
    bx.annotate("14 Mar trade, as-of join (publication clock): BB, what was knowable", (num(tr), 3), xytext=(0, 14),
                textcoords="offset points", ha="left", va="bottom", fontsize=8, color=INK_2)
    bx.annotate("14 Mar trade, join on the effective date: B+,\nthe past reading the future by four days", (num(tr), 2),
                xytext=(0, -13), textcoords="offset points", ha="left", va="top", fontsize=8, color=INK_2,
                linespacing=1.2)
    bx.text(num(eff) - 0.25, 3.72, "13 Mar: downgrade\neffective", ha="right", va="top", fontsize=7.8, color=INK_2,
            linespacing=1.15)
    bx.text(num(pub) + 0.25, 3.72, "18 Mar: on the screen", ha="left", va="top", fontsize=7.8, color=INK_2)
    bx.text(0.5 * (num(eff) + num(pub)), 2.52, "true, not yet\nknowable", ha="center", va="center", fontsize=7.6,
            color=MUTED, linespacing=1.15)
    bx.set_ylim(1.25, 3.85)
    bx.set_xlim(x0, x1)
    bx.set_yticks([2, 3])
    bx.set_yticklabels(["B+", "BB"])
    bx.set_xticks([num(d(2025, 3, m)) for m in (10, 13, 14, 18, 21, 24)])
    bx.set_xticklabels(["10 Mar", "13", "14", "18", "21", "24"])
    bx.set_xlabel("Date, March 2025.  Dashed: the day the rating became true.  Blue: the day it could be known.")
    bx.set_ylabel("Rating")
    return finish(fig, "ch04d_two_clocks_join")


# --------------------------------------------------------------------------------------------------
# Figure 4-D.6: Kaz's Sharpe 3.1 against the cost per dollar traded (section 4D.9)
# --------------------------------------------------------------------------------------------------
def fig_sharpe_vs_cost():
    gross, te, turnover_each_way = 6.2, 2.0, 8       # % a year, % a year, times a year
    traded = 2 * turnover_each_way                   # dollars traded per dollar of book per year
    c = np.linspace(0, 48, 300)                      # bp per dollar traded

    def ir(cbp):
        return (gross - traded * cbp / 100.0) / te

    c_half, c_zero = (gross - 1.0) * 100 / traded, gross * 100 / traded
    assert abs(c_half - 32.5) < 1e-9 and abs(c_zero - 38.75) < 1e-9
    assert abs(ir(25) - 1.1) < 1e-9
    fig, ax = new_figure("wide")
    ax.axvspan(12.5, 25, color=GRID, alpha=0.85, zorder=0, linewidth=0)
    ax.text(18.75, -0.62, "half-spread of an eighth\nto a quarter point", ha="center", va="bottom", fontsize=7.8,
            color=INK_2, linespacing=1.15)
    ax.axhline(0, color=INK_2, linewidth=0.8, zorder=2)
    ax.plot(c, ir(c), color=BLUE, linewidth=LW + 0.4, zorder=4)
    pts = [(0, ir(0), "Kaz's slide: costs set to zero, IR 3.1", (8, 8), "left", "bottom"),
           (12.5, ir(12.5), "IR 2.1", (8, 6), "left", "bottom"),
           (25, ir(25), "IR 1.1", (9, 3), "left", "bottom"),
           (c_half, 0.5, "IR 0.5 survives\nonly to 32.5 bp", (10, 8), "left", "bottom"),
           (c_zero, 0, "all of the 6.2% gone\nat 38.75 bp", (-8, -10), "right", "top")]
    for x, y, txt, off, ha, va in pts:
        ax.plot([x], [y], "o", color=BLUE, markersize=6.5, zorder=6, markeredgecolor="white", markeredgewidth=0.8)
        ax.annotate(txt, (x, y), xytext=off, textcoords="offset points", ha=ha, va=va, fontsize=8.2, color=INK_2)
    ax.set_xlim(-1, 48)
    ax.set_ylim(-0.7, 3.7)
    ax.set_xlabel("Cost per dollar traded (bp of notional); the book trades 16 dollars per dollar of book a year")
    ax.set_ylabel("Net information ratio")
    note(ax, "Gross alpha 6.2% a year, tracking error 2%.", loc="upper right")
    return finish(fig, "ch04d_sharpe_vs_cost")


def main():
    fig_interview_funnel()
    fig_one_price_three_worlds()
    fig_live_counterparty_update()
    fig_kelly_trapdoor()
    fig_two_clocks_join()
    fig_sharpe_vs_cost()


if __name__ == "__main__":
    main()
