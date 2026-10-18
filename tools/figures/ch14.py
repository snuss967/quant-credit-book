"""Figures for Chapter 14 (The Default & Recovery Cycle in the LMT Era).

Run:  python3 tools/figures/ch14.py      -> assets/figures/ch14_*.png

Colour roles held fixed across the chapter's figures:
  BLUE   = hard default (and the ex-DE measure);  ORANGE = distressed exchange (and the headline, DE-inclusive measure)
  VIOLET = participating (inside) lenders;        RED    = excluded (outside) lenders
Real data: numbers quoted in the chapter text and the sourced dossier state/research/trend_lmt_default_recovery_cycle.md.
Everything else is generated from the model stated in the caption and is labelled Illustrative.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
import numpy as np  # noqa: E402
from matplotlib.lines import Line2D  # noqa: E402
from matplotlib.patches import Patch  # noqa: E402
from matplotlib.ticker import FuncFormatter  # noqa: E402
from scipy import stats  # noqa: E402

from style import *  # noqa: E402,F401,F403

LIGHT_GRAY = "#ecebe7"


# ---------------------------------------------------------------------------------------------
# 14.1  Two default rates (real data)
# ---------------------------------------------------------------------------------------------
def fig_two_default_rates():
    fig, (a, b) = new_figure(ncols=2)

    # (a) headline vs ex-DE default rate. Moody's (7 Aug 2025): 5.8% incl., 2.1% excl. (TTM June 2025, bonds + loans);
    # Moody's direct-lending proxy for 2025 (28 Apr / 18 May 2026): 4.7% incl., 1.6% excl.
    groups = ["Spec-grade bonds\n+ loans, TTM Jun 2025", "Direct-lending\nproxy, 2025"]
    incl = np.array([5.8, 4.7])
    excl = np.array([2.1, 1.6])
    x = np.arange(2)
    w = 0.34
    a.bar(x - 0.19, incl, w, color=ORANGE)
    a.bar(x + 0.19, excl, w, color=BLUE)
    for xi, v in zip(x - 0.19, incl):
        a.text(xi, v + 0.15, f"{v:.1f}%", ha="center", va="bottom", fontsize=8.5, color=INK_2)
    for xi, v in zip(x + 0.19, excl):
        a.text(xi, v + 0.15, f"{v:.1f}%", ha="center", va="bottom", fontsize=8.5, color=INK_2)
    for xi, r in zip(x, incl / excl):
        a.text(xi, 6.65, f"{r:.1f}x the\nex-DE rate", ha="center", va="bottom", fontsize=8.5, color=INK, fontweight="bold",
               linespacing=1.15)
    a.set_xticks(x, groups)
    a.set_ylim(0, 9.3)
    a.set_xlim(-0.6, 1.6)
    a.set_ylabel("Default rate (%)")
    a.legend(handles=[Patch(color=ORANGE, label="Including distressed exchanges"),
                      Patch(color=BLUE, label="Excluding distressed exchanges")],
             loc="upper center", bbox_to_anchor=(0.5, 1.0), fontsize=8)

    # (b) distressed exchanges as a share of defaults, as quoted in section 14.1 (rounded as published)
    labels = ["S&P\n2010-23", "S&P\n3 yrs to\nmid-2024", "Moody's\n2024", "Moody's\nH1 2025", "Moody's\n2025"]
    vals = np.array([32, 50, 60, 60, 65])
    txt = ["32%", "~50%", "~60%", "~60%", "~65%"]
    xs = np.arange(len(vals))
    b.vlines(xs, 0, vals, color=ORANGE, linewidth=LW)
    b.plot(xs, vals, "o", color=ORANGE, markersize=7)
    for xi, v, t in zip(xs, vals, txt):
        b.text(xi, v + 3.5, t, ha="center", va="bottom", fontsize=8.5, color=INK_2)
    b.set_xticks(xs, labels)
    b.tick_params(axis="x", labelsize=7.5)
    b.set_ylim(0, 82)
    b.set_xlim(-0.6, 4.6)
    b.set_ylabel("Distressed exchanges, % of defaults")
    return finish(fig, "ch14_two_default_rates")


# ---------------------------------------------------------------------------------------------
# 14.2  Competing risks: cumulative incidence and the Kaplan-Meier overstatement (illustrative)
# ---------------------------------------------------------------------------------------------
def fig_competing_risks_cif():
    lam_h, lam_d = 0.022, 0.038     # per year, section 14.2.1 (two-cause conversion of Moody's June 2025 rates)
    lam = lam_h + lam_d
    t = np.linspace(0, 15, 301)
    S = np.exp(-lam * t)
    F_h = lam_h / lam * (1 - S)
    F_d = lam_d / lam * (1 - S)
    km_d = 1 - np.exp(-lam_d * t)   # hard defaults treated as censoring

    fig, (a, b) = new_figure(ncols=2)

    a.stackplot(t, F_h, F_d, S, colors=[BLUE, ORANGE, LIGHT_GRAY], linewidth=0)
    a.set_xlim(0, 15)
    a.set_ylim(0, 1)
    a.set_xlabel("Years since cohort start")
    a.set_ylabel("Share of the cohort")
    a.text(13.6, 0.025 + 0.5 * F_h[-1] - 0.025, "Hard default, $F_H$", ha="right", va="center", fontsize=8.2, color="white")
    a.text(13.6, F_h[-1] + 0.5 * F_d[-1], "Soft default, $F_D$", ha="right", va="center", fontsize=8.2, color=INK)
    a.text(9.0, 0.76, "No event yet, $S$", ha="center", va="center", fontsize=8.5, color=INK_2)
    a.text(0.4, 0.95, "$S + F_H + F_D = 1$\nat every date", ha="left", va="top", fontsize=8, color=INK_2)
    a.set_xticks([0, 3, 6, 9, 12, 15])
    a.grid(False)

    b.fill_between(t, F_d, km_d, color=ORANGE, alpha=0.18, linewidth=0)
    b.plot(t, F_d, color=ORANGE, linewidth=LW)
    b.plot(t, km_d, color=ORANGE, linewidth=LW, linestyle=(0, (4, 2.5)))
    b.set_xlim(0, 15)
    b.set_ylim(0, 0.5)
    b.set_xlabel("Years since cohort start")
    b.set_xticks([0, 3, 6, 9, 12, 15])
    b.set_ylabel("Probability of a distressed exchange")
    label_end(b, 15, km_d[-1], "1 − KM", ORANGE, dy=7)
    label_end(b, 15, F_d[-1], "$F_D$", ORANGE, dy=-6)
    b.annotate("Overstatement grows\nwith the horizon", (11.2, 0.5 * (F_d[224] + km_d[224])), xytext=(2.0, 0.40),
               fontsize=8, color=INK_2, ha="left", va="center",
               arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.8, shrinkA=2, shrinkB=2))
    note(b, "$\\lambda_H$ = 2.2%/yr, $\\lambda_D$ = 3.8%/yr", loc="lower right")
    return finish(fig, "ch14_competing_risks_cif")


# ---------------------------------------------------------------------------------------------
# 14.3  The re-default clock: mixture-cure Weibull vs ROBO's exponential (illustrative)
# ---------------------------------------------------------------------------------------------
def cure_curves(k, p=0.25, frac2=0.70):
    eta = 2.0 / ((-np.log(1 - frac2)) ** (1.0 / k))
    S0 = lambda u: np.exp(-(u / eta) ** k)                                    # noqa: E731
    f0 = lambda u: (k / eta) * (u / eta) ** (k - 1) * S0(u)                   # noqa: E731
    F = lambda u: p * (1 - S0(u))                                             # noqa: E731
    h = lambda u: p * f0(u) / ((1 - p) + p * S0(u))                           # noqa: E731
    return eta, F, h


def fig_redefault_clock():
    cols = {0.7: RED, 1.0: GREEN, 1.2: BLUE}
    fig, (a, b) = new_figure(ncols=2)
    u = np.linspace(0.02, 10, 500)
    lam_robo = 0.11

    a.plot(u, 1 - np.exp(-lam_robo * u), color=MUTED, linewidth=LW, linestyle=(0, (4, 2.5)))
    for k in (0.7, 1.0, 1.2):
        _, F, _ = cure_curves(k)
        a.plot(u, F(u), color=cols[k], linewidth=LW + (0.4 if k == 1.2 else 0))
    a.axhline(0.25, color=NEUTRAL, linewidth=0.9, linestyle=(0, (1, 2)))
    a.plot([2], [0.175], "o", color=INK, markersize=5.5, zorder=6)
    a.annotate("Moody's anchor:\n70% of the eventual 25%\nby year 2", (2, 0.175), xytext=(2.9, 0.062),
               fontsize=8, color=INK_2, ha="left", va="center",
               arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.8, shrinkA=2, shrinkB=3))
    a.text(9.9, 0.262, "cure ceiling $p$ = 25%", ha="right", va="bottom", fontsize=8, color=INK_2)
    a.text(9.9, 0.60, "ROBO's exponential\n(0.11/yr)", ha="right", va="top", fontsize=8, color=INK_2)
    a.set_xlim(0, 10)
    a.set_ylim(0, 0.72)
    a.set_xlabel("Years since the exchange")
    a.set_ylabel("Cumulative probability of hard default")
    a.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{v:.0%}"))
    a.legend(handles=[Line2D([], [], color=cols[0.7], linewidth=LW, label="k = 0.7"),
                      Line2D([], [], color=cols[1.0], linewidth=LW, label="k = 1.0"),
                      Line2D([], [], color=cols[1.2], linewidth=LW + 0.4, label="k = 1.2 (preferred)")],
             loc="lower right", bbox_to_anchor=(1.0, 0.43), fontsize=8, handlelength=1.6)

    ub = np.linspace(0.1, 7, 400)
    b.plot(ub, np.full_like(ub, lam_robo), color=MUTED, linewidth=LW, linestyle=(0, (4, 2.5)))
    for k in (0.7, 1.0, 1.2):
        _, _, h = cure_curves(k)
        b.plot(ub, h(ub), color=cols[k], linewidth=LW + (0.4 if k == 1.2 else 0))
    b.set_yscale("log")
    b.set_xlim(0, 7)
    b.set_ylim(0.0008, 0.4)
    b.set_xlabel("Years since the exchange")
    b.set_ylabel("Hazard per year (log scale)")
    b.set_yticks([0.001, 0.003, 0.01, 0.03, 0.1, 0.3])
    b.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{v:.1%}".replace(".0%", "%")))
    b.minorticks_off()
    ends = {0.7: 0.0, 1.0: 0.0, 1.2: 0.0}
    for k in (0.7, 1.0, 1.2):
        _, _, h = cure_curves(k)
        label_end(b, 7, float(h(7.0)), f"k = {k}", cols[k], dy=ends[k])
    label_end(b, 7, lam_robo, "exponential", MUTED, dy=0)
    return finish(fig, "ch14_redefault_clock")


# ---------------------------------------------------------------------------------------------
# 14.4  Two humps, not one bell (illustrative; Serta numbers from the remand facts)
# ---------------------------------------------------------------------------------------------
def fig_two_humps():
    pi = 0.526
    a_in, b_in = 74.0, 26.0     # participants: mean 0.74
    a_out, b_out = 25.0, 75.0   # excluded: mean 0.25
    mu_in, mu_out = a_in / (a_in + b_in), a_out / (a_out + b_out)
    v_in = mu_in * (1 - mu_in) / (a_in + b_in + 1)
    v_out = mu_out * (1 - mu_out) / (a_out + b_out + 1)
    mean = pi * mu_in + (1 - pi) * mu_out
    var = pi * v_in + (1 - pi) * v_out + pi * (1 - pi) * (mu_in - mu_out) ** 2
    s = mean * (1 - mean) / var - 1                    # moment-matched single Beta
    a_m, b_m = mean * s, (1 - mean) * s

    x = np.linspace(0.0005, 0.9995, 1500)
    d_in = pi * stats.beta.pdf(x, a_in, b_in) / 100.0
    d_out = (1 - pi) * stats.beta.pdf(x, a_out, b_out) / 100.0
    d_one = stats.beta.pdf(x, a_m, b_m) / 100.0
    xp = x * 100

    fig, ax = new_figure("wide")
    ax.fill_between(xp, d_in, color=VIOLET, alpha=0.30, linewidth=0)
    ax.plot(xp, d_in, color=VIOLET, linewidth=LW)
    ax.fill_between(xp, d_out, color=RED, alpha=0.30, linewidth=0)
    ax.plot(xp, d_out, color=RED, linewidth=LW)
    ax.plot(xp, d_one, color=MUTED, linewidth=LW, linestyle=(0, (4, 2.5)))
    ax.axvline(mean * 100, color=NEUTRAL, linewidth=0.9, linestyle=(0, (1, 2)))

    ax.text(mu_in * 100 + 5.5, 0.036, "Participants, 52.6%\nexchanged at 74", ha="left", va="center", fontsize=8.5, color=INK_2)
    ax.text(mu_out * 100 - 5.5, 0.036, "Excluded, 47.4%\nvalued at 25", ha="right", va="center", fontsize=8.5, color=INK_2)
    ax.annotate("one Beta with the same mean (51)\nand s.d. (25 points)", (mean * 100, 0.0128), xytext=(mean * 100, 0.0295),
                ha="center", va="center", fontsize=8, color=INK_2,
                bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none"),
                arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.8, shrinkA=2, shrinkB=2))
    ax.annotate("", xy=(mu_in * 100 - 2, 0.0525), xytext=(mu_out * 100 + 2, 0.0525),
                arrowprops=dict(arrowstyle="<->", color=INK_2, lw=0.9, shrinkA=0, shrinkB=0))
    ax.text(mean * 100, 0.0535, "49 points apart", ha="center", va="bottom", fontsize=8, color=INK_2)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 0.0585)
    ax.set_xlabel("Recovery (cents per dollar of par)")
    ax.set_ylabel("Probability density (per point)")
    return finish(fig, "ch14_two_humps")


# ---------------------------------------------------------------------------------------------
# 14.6  Timeline: LME to filing for four names, and the court rulings (dates from the chapter)
# ---------------------------------------------------------------------------------------------
def yr(y, m=1, d=1):
    """Decimal year, accurate to a few days (enough for a six-year axis)."""
    return y + (m - 1) / 12 + (d - 1) / 365.0


def fig_lme_timeline():
    fig, ax = new_figure((7.0, 5.0))
    cases = [  # name, LME date, filing date, months (chapter text)
        ("Serta", yr(2020, 6, 22), yr(2023, 1, 23), 31),
        ("Wesco/Incora", yr(2022, 3), yr(2023, 6, 1), 15),
        ("Mitel", yr(2022, 10), yr(2025, 3, 10), 29),
        ("Del Monte", yr(2024, 8), yr(2025, 7, 1), 11),
    ]
    ys = [6.0, 5.0, 4.0, 3.0]
    for (name, t0, t1, mo), y in zip(cases, ys):
        ax.plot([t0, t1], [y, y], color=NEUTRAL, linewidth=2.2, solid_capstyle="butt", zorder=2)
        ax.plot([t0 + 2.0, t0 + 2.0], [y - 0.2, y + 0.2], color=INK_2, linewidth=1.3, zorder=3)
        ax.plot([t0], [y], "o", color=ORANGE, markersize=8, zorder=4)
        ax.plot([t1], [y], "s", color=BLUE, markersize=8, zorder=4)
        xm = 0.5 * (t0 + t1)
        ax.text(xm, y + 0.3, f"{mo} months", ha="center", va="bottom", fontsize=8.5, color=INK_2)
    ax.set_yticks(ys + [1.0], [c[0] for c in cases] + ["Court rulings"])
    ax.tick_params(axis="y", length=0, labelsize=9)
    ax.grid(False)
    ax.grid(True, axis="x", color=GRID, linewidth=0.7)
    ax.set_axisbelow(True)

    # rulings, numbered; key printed in the empty left part of the lane
    rulings = [  # n, date, row y, key text
        (1, yr(2024, 6, 20), 1.55, "20 Jun 2024  Robertshaw: breach found, damages only"),
        (2, yr(2024, 12, 31), 1.55, "31 Dec 2024  Serta (5th Cir.): not an \"open market purchase\""),
        (3, yr(2024, 12, 31), 0.75, "31 Dec 2024  Mitel (1st Dept): uptier permitted"),
        (4, yr(2025, 1, 17), 0.0, "17 Jan 2025  Wesco (Bankr.): 2022 deal unwound"),
        (5, yr(2025, 9, 1), 1.55, "Sep 2025  ConvergeOne (S.D. Tex.): majority backstop struck"),
        (6, yr(2025, 12, 8), 0.75, "8 Dec 2025  Wesco (Dist. Ct.): unwinding reversed"),
        (7, yr(2026, 7, 7), 1.55, "7 Jul 2026  Serta remand: \\$261mm + 9% interest"),
    ]
    ax.axhline(2.2, color=GRID, linewidth=0.9)
    for n, t, y, _ in rulings:
        ax.plot([t], [y], "o", color=INK_2, markersize=10.5, zorder=4)
        ax.text(t, y, str(n), ha="center", va="center", fontsize=7.5, color="white", zorder=5, fontweight="bold")
    for i, (n, _, _, key) in enumerate(rulings):
        ax.text(2020.0, 1.85 - 0.31 * i, f"{n}  {key}", ha="left", va="center", fontsize=7.6, color=INK_2)

    ax.set_xlim(2019.9, 2026.95)
    ax.set_ylim(-0.4, 7.5)
    ax.set_xticks(range(2020, 2027))
    ax.set_xlabel("Year")
    handles = [
        Line2D([], [], marker="o", color="none", markerfacecolor=ORANGE, markeredgecolor=ORANGE, markersize=7,
               label="LME closes (soft default)"),
        Line2D([], [], marker="s", color="none", markerfacecolor=BLUE, markeredgecolor=BLUE, markersize=7,
               label="Chapter 11 filing (hard default)"),
        Line2D([], [], marker="|", color=INK_2, linestyle="none", markersize=9, markeredgewidth=1.3,
               label="24 months after the LME"),
    ]
    ax.legend(handles=handles, loc="upper left", ncols=3, fontsize=8, bbox_to_anchor=(0.0, 1.0),
              handletextpad=0.3, columnspacing=1.2)
    return finish(fig, "ch14_lme_timeline")


if __name__ == "__main__":
    fig_two_default_rates()
    fig_competing_risks_cif()
    fig_redefault_clock()
    fig_two_humps()
    fig_lme_timeline()
