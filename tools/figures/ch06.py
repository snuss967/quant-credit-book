"""Chapter 6 figures: Stochastic Calculus, Intensity Models & Structural Frameworks.

Run:  python3 tools/figures/ch06.py      (writes assets/figures/ch06_*.png)

  6.1  ch06_volatility_tax            ILLUSTRATIVE: the 6.1.1 two-step tree and the 6.1.2 lognormal (V0 = 100, mu = 8%, sigma_V = 25%)
  6.2  ch06_merton_payoff_fulcrum     ILLUSTRATIVE: F = 80 payoffs with the 6.2.4 density; the 6.2.1 capital structure as call spreads
  6.3  ch06_merton_spread_short_end   ILLUSTRATIVE model (6.2.4 firm at three volatilities) against a REAL range:
                                      ICE BofA CCC & Lower OAS, FRED BAMLH0A3HYC, 690 to 1,282 bp over 17 Oct 2023 to 15 Oct 2026
                                      (state/research/trend_figure_data_series.md; re-checked on FRED 18 Oct 2026; only the two
                                      range ends are used, no ICE series is stored)
  6.4  ch06_svb_holdco_waterfall      REAL: SVB Financial Group FY2022 10-K (HTM note; parent-only statements), as compiled in
                                      state/research/case_carvana_svb_wolfspeed_capital_structure.md, sections 2.2 and 2.3
  6.5  ch06_carvana_pair              REAL marks, ILLUSTRATIVE sizing: CVNA daily closes (Yahoo Finance, restated to as-traded prices,
                                      cached in tools/figures/data/ch06_CVNA.csv) and Carvana's own fair-value-to-carrying-value ratios
                                      for its senior notes (10-K and 10-Qs, dossier section 1.3); pair sizing as in 6.10.1 Beat 5

Colour roles, fixed across this chapter's figures:
  debt, bonds, the bondholder's claim   BLUE (seniority within debt: SEQ_BLUE, dark = most senior)
  equity, the call, the short stock     ORANGE
  the market's number (CCC index)       ORANGE band; the model's curves are SEQ_BLUE
  losses                                DIVERGING red (hatched = not yet marked)
  the density of V_T                    light grey, with the band that matters filled in the colour of the claim it belongs to
"""
import csv
import datetime as dt
import json
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(__file__))
from style import *  # noqa: E402,F401,F403  (applies the rcParams on import)

import numpy as np  # noqa: E402
from matplotlib.dates import date2num  # noqa: E402
from matplotlib.ticker import FuncFormatter, NullFormatter  # noqa: E402
from scipy.stats import norm  # noqa: E402

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DATA = os.path.join(os.path.dirname(__file__), "data")
LOSS = "#e66767"          # the red end of the book's diverging ramp (loss polarity)
DENS = "#dcdbd6"          # density of V_T, a recessive grey
DENS_DARK = "#b9b8b2"
MINUS = "\u2212"


# --------------------------------------------------------------------------------------------
# Merton engine (closed forms of section 6.2.3), checked against the worked example of 6.2.4
# --------------------------------------------------------------------------------------------
def merton(V0, F, r, sig, T, mu=None):
    T = np.asarray(T, dtype=float)
    d1 = (np.log(V0 / F) + (r + 0.5 * sig ** 2) * T) / (sig * np.sqrt(T))
    d2 = d1 - sig * np.sqrt(T)
    E = V0 * norm.cdf(d1) - F * np.exp(-r * T) * norm.cdf(d2)
    B = V0 - E
    s = -np.log(B / (F * np.exp(-r * T))) / T
    out = {"E": E, "B": B, "s_bp": s * 1e4, "pd_q": norm.cdf(-d2), "d1": d1, "d2": d2}
    if mu is not None:
        dd = (np.log(V0 / F) + (mu - 0.5 * sig ** 2) * T) / (sig * np.sqrt(T))
        out["dd"], out["pd_p"] = dd, norm.cdf(-dd)
    return out


def check_worked_example():
    """The chapter's printed numbers (6.2.4): E0 24.78, B0 75.22, 216 bp, Q-PD 17.7%, DD 1.09, P-PD 13.8%,
    three-month spread about 70 bp, two-and-a-half-week spread under 1 bp."""
    m = merton(100, 80, 0.04, 0.25, 1.0, mu=0.08)
    assert abs(float(m["E"]) - 24.78) < 0.01 and abs(float(m["B"]) - 75.22) < 0.01
    assert abs(float(m["s_bp"]) - 216) < 0.5 and abs(float(m["pd_q"]) - 0.177) < 0.001
    assert abs(float(m["dd"]) - 1.09) < 0.005 and abs(float(m["pd_p"]) - 0.138) < 0.001
    assert abs(float(merton(100, 80, 0.04, 0.25, 0.25)["s_bp"]) - 70) < 3
    assert float(merton(100, 80, 0.04, 0.25, 2.5 / 52)["s_bp"]) < 1
    assert abs(float(merton(100, 80, 0.04, 0.15, 1.0)["s_bp"]) - 30) < 4        # Exercise 1 check: "near 30 bp"


def lognorm_pdf(x, median, sig):
    """Density of a lognormal with the given median and log-volatility."""
    x = np.asarray(x, dtype=float)
    out = np.zeros_like(x)
    pos = x > 0
    z = np.log(x[pos] / median) / sig
    out[pos] = np.exp(-0.5 * z ** 2) / (x[pos] * sig * np.sqrt(2 * np.pi))
    return out


def lognorm_cdf(x, median, sig):
    return norm.cdf(np.log(x / median) / sig)


def strip_axis(ax):
    """A density strip: no y ticks, no grid, a light baseline."""
    ax.set_yticks([])
    ax.grid(False)
    ax.spines["left"].set_visible(False)


# --------------------------------------------------------------------------------------------
# Figure 6.1  The volatility tax (6.1.1)
# --------------------------------------------------------------------------------------------
def fig_volatility_tax():
    mu, sig, T, V0 = 0.08, 0.25, 1.0, 100.0
    fig, (a, b) = new_figure("panel2", ncols=2)

    # left: the two-step +-10% tree of the first Math, Gently box
    ends = np.array([81.0, 99.0, 121.0])
    prob = np.array([25.0, 50.0, 25.0])
    mean, median = 100.0, 99.0
    assert abs((121 + 99 + 99 + 81) / 4 - mean) < 1e-9
    a.set_axisbelow(True)
    a.bar(ends, prob, width=3.4, color=SEQ_BLUE_STEPS[2])
    a.axvline(median, color=INK, linewidth=1.2, ymax=0.84)
    a.axvline(mean, color=ORANGE, linewidth=1.2, ymax=0.84)
    a.text(median - 0.9, 56.5, "median 99", ha="right", va="bottom", fontsize=8.5, color=INK_2)
    a.text(mean + 0.9, 56.5, "mean 100", ha="left", va="bottom", fontsize=8.5, color=INK_2)
    a.annotate("the 121 branch\npulls the mean up", (121, 25.8), xytext=(113.5, 41), fontsize=8, color=MUTED,
               ha="center", arrowprops=dict(arrowstyle="-", color=NEUTRAL, lw=0.8))
    a.set_xticks(ends)
    a.set_xlim(72, 130)
    a.set_ylim(0, 68)
    a.set_xlabel("Value after two \u00b110% steps (start = 100)")
    a.set_ylabel("Probability (%)")

    # right: the one-year lognormal of 6.1.2
    med = V0 * np.exp((mu - 0.5 * sig ** 2) * T)
    mean_v = V0 * np.exp(mu * T)
    below = float(lognorm_cdf(V0, med, sig * np.sqrt(T)))
    assert abs(med - 105.0) < 0.05 and abs(mean_v - 108.33) < 0.01 and abs(below - 0.423) < 0.001
    b.set_axisbelow(True)
    x = np.linspace(30, 260, 1200)
    y = lognorm_pdf(x, med, sig * np.sqrt(T)) * 100
    b.fill_between(x, y, color=SEQ_BLUE_STEPS[0])
    b.fill_between(x, y, where=x <= V0, color=SEQ_BLUE_STEPS[3])
    b.plot(x, y, color=BLUE, linewidth=LW)
    top = float(y.max())
    b.vlines(med, 0, top * 1.12, color=INK, linewidth=1.2)
    b.vlines(mean_v, 0, top * 1.12, color=ORANGE, linewidth=1.2)
    b.text(med - 2, top * 1.15, f"median {med:.1f}", ha="right", va="bottom", fontsize=8.5, color=INK_2)
    b.text(mean_v + 2, top * 1.15, f"mean {mean_v:.1f}", ha="left", va="bottom", fontsize=8.5, color=INK_2)
    b.text(77, top * 0.34, f"{below:.0%} end\nbelow 100", fontsize=8.5, color=INK, ha="center", va="center")
    b.set_xlim(40, 220)
    b.set_ylim(0, top * 1.38)
    b.set_xlabel("Asset value after one year (start = 100)")
    b.set_ylabel("Probability density (% per $1)")
    return finish(fig, "ch06_volatility_tax")


# --------------------------------------------------------------------------------------------
# Figure 6.2  Payoff diagram and fulcrum (6.2.1)
# --------------------------------------------------------------------------------------------
def fig_merton_payoff_fulcrum():
    fig, ax = new_figure((7.0, 4.7), nrows=2, ncols=2, gridspec_kw={"height_ratios": [3.1, 1.25]}, sharex="col")
    a, b = ax[0, 0], ax[0, 1]
    sa, sb = ax[1, 0], ax[1, 1]

    # ---- left: F = 80, equity is a call, debt is par minus a put, density of V_T from the 6.2.4 firm
    F = 80.0
    V = np.linspace(0, 160, 641)
    debt, eq = np.minimum(V, F), np.maximum(V - F, 0)
    a.plot(V, V, color=NEUTRAL, linewidth=1.0, linestyle=(0, (3, 3)), zorder=1)
    a.plot(V, debt, color=BLUE, linewidth=LW + 0.4, zorder=3)
    a.plot(V, eq, color=ORANGE, linewidth=LW + 0.4, zorder=3)
    a.text(96, 118, "firm value V", rotation=40, fontsize=8, color=MUTED, ha="center", va="center")
    a.text(158, 84.5, "Debt = min(V, F)", fontsize=8.5, color=INK_2, ha="right", va="bottom")
    a.text(124, 19, "Equity =\nmax(V \u2212 F, 0)", fontsize=8.5, color=INK_2, ha="left", va="center")
    a.axhline(F, color=NEUTRAL, linewidth=0.8, zorder=1)
    a.annotate("", (70, 80), (70, 70), arrowprops=dict(arrowstyle="<->", color=INK_2, lw=1.0, shrinkA=0, shrinkB=0))
    a.plot([70], [70], "o", color=BLUE, markersize=5, zorder=4)
    a.annotate("at V = 70 the debt is\n10 short of par: the put", (68, 76), xytext=(6, 112), fontsize=8, color=INK_2,
               ha="left", arrowprops=dict(arrowstyle="-", color=NEUTRAL, lw=0.8))
    a.text(2, F + 2, "F = 80", fontsize=8, color=MUTED, ha="left", va="bottom")
    a.set_ylim(0, 170)
    a.set_ylabel("Payoff at maturity")

    mu, sig, V0, T = 0.08, 0.25, 100.0, 1.0
    med = V0 * np.exp((mu - 0.5 * sig ** 2) * T)
    pd_p = float(lognorm_cdf(F, med, sig))
    assert abs(pd_p - 0.138) < 0.001
    x = np.linspace(1, 160, 800)
    y = lognorm_pdf(x, med, sig)
    sa.fill_between(x, y, color=DENS)
    sa.fill_between(x, y, where=x <= F, color=DENS_DARK)
    sa.plot(x, y, color=MUTED, linewidth=1.0)
    sa.axvline(F, color=NEUTRAL, linewidth=0.8)
    sa.annotate(f"{pd_p:.1%} of the\nmass is below\nF: default", (66, float(y.max()) * 0.12), xytext=(3, float(y.max()) * 0.62),
                fontsize=8, color=INK_2, ha="left", va="center", arrowprops=dict(arrowstyle="-", color=NEUTRAL, lw=0.8))
    strip_axis(sa)
    sa.set_ylim(0, float(y.max()) * 1.08)
    sa.set_xlim(0, 160)
    sa.set_xlabel("Firm value at maturity, $V_T$")
    sa.set_ylabel("Density")

    # ---- right: the 6.2.1 capital structure as call spreads (400 first lien, 300 second lien, 250 unsecured)
    K1, K2, K3 = 400.0, 700.0, 950.0
    V = np.linspace(0, 1150, 1151)
    first = np.minimum(V, K1)
    second = np.clip(V - K1, 0, K2 - K1)
    unsec = np.clip(V - K2, 0, K3 - K2)
    equity = np.maximum(V - K3, 0)
    assert np.allclose(first + second + unsec + equity, V)
    cols = [SEQ_BLUE_STEPS[11], SEQ_BLUE_STEPS[7], SEQ_BLUE_STEPS[2], ORANGE]
    b.stackplot(V, first, second, unsec, equity, colors=cols, edgecolor=SURFACE, linewidth=0.7)
    for k in (K1, K2, K3):
        b.axvline(k, color=SURFACE, linewidth=0.0)
    b.text(930, 200, "First lien\n$400mm", fontsize=8.5, color="white", ha="center", va="center")
    b.text(930, 555, "Second lien\n$300mm", fontsize=8.5, color="white", ha="center", va="center")
    b.text(900, 790, "Unsecured\n$250mm", fontsize=8.5, color=INK, ha="center", va="center")
    b.annotate("Equity: a call\nstruck at 950", (1050, 1005), xytext=(560, 1040), fontsize=8.5, color=INK_2, ha="center",
               va="center", arrowprops=dict(arrowstyle="-", color=NEUTRAL, lw=0.8))
    b.set_ylim(0, 1150)
    b.set_ylabel("Recovery by class ($mm)")

    med2, sig2 = 530.0, 0.22
    m_second = float(lognorm_cdf(K2, med2, sig2) - lognorm_cdf(K1, med2, sig2))
    m_below = float(lognorm_cdf(K1, med2, sig2))
    m_above = 1 - float(lognorm_cdf(K2, med2, sig2))
    assert abs(m_second - 0.80) < 0.005
    x = np.linspace(1, 1150, 1500)
    y = lognorm_pdf(x, med2, sig2)
    sb.fill_between(x, y, color=DENS)
    sb.fill_between(x, y, where=(x >= K1) & (x <= K2), color=SEQ_BLUE_STEPS[7])
    sb.plot(x, y, color=MUTED, linewidth=1.0)
    for k in (K1, K2):
        sb.axvline(k, color=SURFACE, linewidth=1.0)
    sb.text(550, float(y.max()) * 0.3, "fulcrum", fontsize=8.5, color="white", ha="center", va="center", fontweight="bold")
    sb.text(1140, float(y.max()) * 0.62, f"{m_second:.0%} of the mass lies\nbetween the second\nlien's two strikes", fontsize=8,
            color=INK_2, ha="right", va="center")
    strip_axis(sb)
    sb.set_ylim(0, float(y.max()) * 1.08)
    sb.set_xlim(0, 1150)
    sb.set_xticks([0, 400, 700, 950])
    sb.set_xlabel("Enterprise value, V ($mm)")
    sb.set_ylabel("Density")
    for axis in (a, b):
        axis.tick_params(labelbottom=False)
    a.set_xlim(0, 160)
    return finish(fig, "ch06_merton_payoff_fulcrum"), (m_below, m_second, m_above, pd_p)


# --------------------------------------------------------------------------------------------
# Figure 6.3  The short-end embarrassment (6.2.4)
# --------------------------------------------------------------------------------------------
CCC_LOW_BP, CCC_HIGH_BP, CCC_LAST_BP = 690.0, 1282.0, 1278.0     # FRED BAMLH0A3HYC, window 17 Oct 2023 to 15 Oct 2026


def fig_merton_spread_short_end():
    fig, ax = new_figure((7.0, 3.9))
    T = np.geomspace(1 / 52 * 0.8, 10, 500)
    ax.axhspan(CCC_LOW_BP, CCC_HIGH_BP, color=ORANGE, alpha=0.16, linewidth=0, zorder=1)
    ax.axhline(CCC_LOW_BP, color=ORANGE, linewidth=0.8, zorder=2)
    ax.axhline(CCC_HIGH_BP, color=ORANGE, linewidth=0.8, zorder=2)
    ax.text(0.0145, 990, "CCC & Lower index OAS, any tenor:\nbetween 690 and 1,282 bp over the last three years",
            fontsize=8.5, color=INK_2, ha="left", va="center")
    shades = {0.15: SEQ_BLUE_STEPS[4], 0.25: SEQ_BLUE_STEPS[8], 0.35: SEQ_BLUE_STEPS[11]}
    for sig, col in shades.items():
        s = merton(100, 80, 0.04, sig, T)["s_bp"]
        ax.plot(T, s, color=col, linewidth=LW + 0.2, zorder=3)
        label_end(ax, T[-1], float(s[-1]), f"$\\sigma_V$ = {sig:.0%}", col, dx=5)
    # the three numbers printed in 6.2.4 for the 25% firm, each with a leader line into the empty space above the curves
    pts = [(1.0, "216 bp at one year", dict(xytext=(1.0, 330), ha="center")),
           (0.25, "about 70 bp\nat three months", dict(xytext=(0.27, 215), ha="left")),
           (2.5 / 52, "under 1 bp at two\nand a half weeks", dict(xytext=(0.0145, 215), ha="left"))]
    for t, text, kw in pts:
        sv = float(merton(100, 80, 0.04, 0.25, t)["s_bp"])
        ax.plot([t], [sv], "o", color=shades[0.25], markersize=5.5, zorder=5, markeredgecolor="white", markeredgewidth=0.8)
        ax.annotate(text, (t, sv), va="center", fontsize=8, color=INK_2, zorder=6,
                    arrowprops=dict(arrowstyle="-", color=NEUTRAL, lw=0.8, shrinkA=2, shrinkB=4), **kw)
    ax.set_xscale("log")
    ax.set_xlim(0.0125, 10)
    ticks = [1 / 52, 1 / 12, 0.25, 0.5, 1, 2, 5, 10]
    ax.set_xticks(ticks)
    ax.set_xticklabels(["1w", "1m", "3m", "6m", "1y", "2y", "5y", "10y"])
    ax.xaxis.set_minor_formatter(NullFormatter())
    ax.set_ylim(0, 1400)
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{v:,.0f}"))
    ax.set_xlabel("Time to maturity (log scale)")
    ax.set_ylabel("Credit spread (bp)")
    ax.text(0.01, 0.985, "Merton firm: V$_0$ = 100, F = 80, r = 4%", transform=ax.transAxes, ha="left", va="top", fontsize=8,
            color=MUTED)
    fig.get_layout_engine().set(rect=(0, 0, 0.93, 1))
    return finish(fig, "ch06_merton_spread_short_end")


# --------------------------------------------------------------------------------------------
# Figure 6.4  SVB: the hole and the holdco waterfall (6.4.4)
# --------------------------------------------------------------------------------------------
# $bn unless noted. HTM: amortized cost 91.3, fair value 76.2, unrealized loss 15.2 (computed from the 10-K), total stockholders'
# equity 16.0; after-tax loss on the 8 March AFS sale 1.8. Parent-only, 31 Dec 2022 ($mm): total assets 19,679, of which
# investment in the Bank 15,456 and cash and equivalents 2,258 (on deposit at the Bank); long-term debt 3,370 plus about 305 of
# lease and other liabilities.
HTM_LOSS, EQUITY, AFS_LOSS = 15.2, 16.0, 1.8
P_ASSETS, P_BANK, P_CASH, P_LTD, P_OTHER = 19.679, 15.456, 2.258, 3.370, 0.305


def fig_svb_holdco_waterfall():
    fig, (a, b) = new_figure("panel2", ncols=2, gridspec_kw={"width_ratios": [1, 1.25]})

    # left: the loss nobody had to mark against the equity that was supposed to absorb it
    labels = ["Unrealized\nloss on HTM\nbonds", "Total\nstockholders'\nequity", "Loss booked\non the 8 March\nsale, after tax"]
    vals = [HTM_LOSS, EQUITY, AFS_LOSS]
    cols = [LOSS, ORANGE, LOSS]
    xs = np.arange(3)
    a.set_axisbelow(True)
    bars = a.bar(xs, vals, width=0.62, color=cols)
    bars[0].set_hatch("////")
    bars[0].set_edgecolor("white")
    bars[0].set_linewidth(0)
    for x, v in zip(xs, vals):
        a.text(x, v + 0.4, f"{v:.1f}", ha="center", va="bottom", fontsize=9, color=INK_2)
    a.set_xticks(xs)
    a.set_xticklabels(labels, fontsize=8)
    a.set_ylim(0, 19.5)
    a.set_ylabel("$ billions, 31 Dec 2022")

    # right: the holdco's parent-only waterfall, assets down to what is left once the bank is worth nothing
    ex_bank = P_ASSETS - P_BANK
    left_after_cash = ex_bank - P_CASH
    liab = P_LTD + P_OTHER
    assert abs(ex_bank - 4.2) < 0.05 and abs(liab - 3.7) < 0.05
    cov_book, cov_ex_cash = ex_bank / liab, left_after_cash / liab
    assert abs(cov_book - 1.15) < 0.01 and abs(cov_ex_cash - 0.53) < 0.01        # "a little over half"
    xs = np.arange(5)
    tot = [(0, P_ASSETS, MUTED), (ex_bank, P_ASSETS, LOSS), (0, ex_bank, SEQ_BLUE_STEPS[7]), (left_after_cash, ex_bank, LOSS),
           (0, left_after_cash, SEQ_BLUE_STEPS[11])]
    b.set_axisbelow(True)
    for x, (lo, hi, col) in zip(xs, tot):
        b.bar(x, hi - lo, bottom=lo, width=0.62, color=col)
    for i in (1, 3):
        b.patches[i].set_hatch("////")
        b.patches[i].set_edgecolor("white")
        b.patches[i].set_linewidth(0)
    # connectors between the steps
    for x0, y0 in [(0, P_ASSETS), (1, ex_bank), (2, ex_bank), (3, left_after_cash)]:
        b.plot([x0 + 0.31, x0 + 1 - 0.31], [y0, y0], color=MUTED, linewidth=0.7, zorder=2)
    b.plot([-0.45, 5.35], [liab, liab], color=INK, linewidth=1.1, linestyle=(0, (4, 3)), zorder=5)
    b.text(5.4, liab, "parent\nliabilities\n3.7", ha="left", va="center", fontsize=8, color=INK_2, clip_on=False)
    b.text(0, P_ASSETS + 0.4, f"{P_ASSETS:.1f}", ha="center", va="bottom", fontsize=9, color=INK_2)
    b.text(1, P_ASSETS + 0.4, f"{MINUS}{P_BANK:.1f}", ha="center", va="bottom", fontsize=9, color=INK_2)
    b.text(2, ex_bank + 0.4, f"{ex_bank:.1f}", ha="center", va="bottom", fontsize=9, color=INK_2)
    b.text(3, ex_bank + 0.4, f"{MINUS}{P_CASH:.1f}", ha="center", va="bottom", fontsize=9, color=INK_2)
    b.text(4, left_after_cash - 0.35, f"{left_after_cash:.1f}", ha="center", va="top", fontsize=9, color="white")
    b.text(2.0, 17.8, f"Ex-bank assets cover {cov_book:.0%} of\nthe parent's liabilities at book,\nbut only {cov_ex_cash:.0%} if the cash is\n"
           "a claim on the receivership", fontsize=8, color=INK_2, ha="left", va="top", linespacing=1.3)
    b.set_xticks(xs)
    b.set_xticklabels(["Parent\nassets", "Stake in\nthe bank", "Assets\nex-bank", "Cash held\nat the bank", "Left\nover"], fontsize=7.8)
    b.set_xlim(-0.55, 4.55)
    b.set_ylim(0, 21.5)
    b.set_ylabel("$ billions, parent only")
    fig.get_layout_engine().set(rect=(0, 0, 0.93, 1))
    return finish(fig, "ch06_svb_holdco_waterfall"), (cov_book, cov_ex_cash)


# --------------------------------------------------------------------------------------------
# Figure 6.5  Carvana: the pair that lost on the leg it was sure about (6.10.1)
# --------------------------------------------------------------------------------------------
CVNA_CSV = os.path.join(DATA, "ch06_CVNA.csv")
SPLIT = 5            # Yahoo restates CVNA for a later 5-for-1 split; x5 restores the as-traded close the dossier quotes
PEAK, LOW = 370.10, 3.72     # as-traded closes of 10 Aug 2021 and 27 Dec 2022 (dossier 1.1)
# Dossier 1.3: stack mark = fair value over carrying value of all senior notes (Level 2, 10-K and 10-Qs).
STACK_MARK = {"2022-12-30": 44.8, "2023-03-31": 53.8, "2023-06-30": 74.0, "2023-09-29": 77.7, "2023-12-29": 84.7}
EQUITY_CLOSE = {"2022-12-30": 4.74, "2023-03-31": 9.79, "2023-06-30": 25.92, "2023-09-29": 41.98, "2023-12-29": 52.94}


def load_cvna():
    """Daily as-traded closes, 2021-08-02 to 2024-12-31. Cached; downloaded from the Yahoo chart API if the cache is missing."""
    if not os.path.exists(CVNA_CSV):
        p1 = int(dt.datetime(2021, 8, 1, tzinfo=dt.timezone.utc).timestamp())
        p2 = int(dt.datetime(2025, 1, 6, tzinfo=dt.timezone.utc).timestamp())
        url = f"https://query2.finance.yahoo.com/v8/finance/chart/CVNA?period1={p1}&period2={p2}&interval=1d&events=history"
        raw = subprocess.run(["curl", "-sS", "-m", "60", "-A", "Mozilla/5.0", url], check=True, capture_output=True).stdout
        res = json.loads(raw)["chart"]["result"][0]
        off = res["meta"]["gmtoffset"]
        closes = res["indicators"]["quote"][0]["close"]
        rows = []
        for t, c in zip(res["timestamp"], closes):
            d = dt.datetime.fromtimestamp(t + off, dt.timezone.utc).date()
            if c is not None and d <= dt.date(2024, 12, 31):
                rows.append((d.isoformat(), round(c, 4), round(c * SPLIT, 2)))
        os.makedirs(DATA, exist_ok=True)
        with open(CVNA_CSV, "w", newline="") as fh:
            w = csv.writer(fh)
            w.writerow(["date", "close_vendor_split_adjusted", "close_as_traded"])
            w.writerows(rows)
    with open(CVNA_CSV) as fh:
        rows = list(csv.DictReader(fh))
    d = [dt.date.fromisoformat(r["date"]) for r in rows]
    c = np.array([float(r["close_as_traded"]) for r in rows])
    return d, c


def fig_carvana_pair():
    dates, close = load_cvna()
    byd = dict(zip(dates, close))
    # the dossier's quoted as-traded closes must reproduce from the vendor bars
    for key, want in [("2021-08-10", PEAK), ("2022-12-27", LOW), ("2023-07-19", 55.80), ("2023-12-29", 52.94), ("2024-12-31", 203.36)]:
        got = byd[dt.date.fromisoformat(key)]
        assert abs(got - want) < 0.08, (key, got, want)
    for k, want in EQUITY_CLOSE.items():
        assert abs(byd[dt.date.fromisoformat(k)] - want) < 0.08, k

    fig, (a, b) = new_figure("panel2", ncols=2, gridspec_kw={"width_ratios": [1.75, 1]})
    x = date2num(dates)
    a.plot(x, close, color=ORANGE, linewidth=1.2)
    a.set_yscale("log")
    a.set_ylim(2.5, 1000)
    a.set_yticks([3, 10, 30, 100, 300])
    a.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f"${v:,.0f}"))
    a.yaxis.set_minor_formatter(NullFormatter())
    a.set_xlim(date2num(dt.date(2021, 7, 1)), date2num(dt.date(2025, 3, 1)))
    a.xaxis_date()
    a.set_xticks([date2num(dt.date(y, 1, 1)) for y in (2022, 2023, 2024, 2025)])
    a.set_xticklabels(["2022", "2023", "2024", "2025"])
    a.grid(axis="y")
    a.set_ylabel("CVNA close, as traded (log scale)")
    # peak, low and the last close
    a.plot([date2num(dt.date(2021, 8, 10))], [PEAK], "o", color=ORANGE, markersize=4.5, zorder=5)
    a.annotate("$370.10 peak, 10 Aug 2021", (date2num(dt.date(2021, 8, 10)), PEAK), xytext=(-2, 11), textcoords="offset points",
               fontsize=8, color=INK_2, ha="left", va="bottom")
    a.plot([date2num(dt.date(2022, 12, 27))], [LOW], "o", color=ORANGE, markersize=4.5, zorder=5)
    a.annotate("$3.72, 27 Dec 2022\n(down 99.0%)", (date2num(dt.date(2022, 12, 27)), LOW), xytext=(-8, -3), textcoords="offset points",
               fontsize=8, color=INK_2, ha="right", va="center")
    a.plot([date2num(dt.date(2024, 12, 31))], [203.36], "o", color=ORANGE, markersize=4.5, zorder=5, clip_on=False)
    a.annotate("$203.36, 31 Dec 2024", (date2num(dt.date(2024, 12, 31)), 203.36), xytext=(-6, 9), textcoords="offset points",
               fontsize=8, color=INK_2, ha="right", va="bottom")
    # the four 2023 exchange dates, numbered; alternate heights so the digits do not touch
    events = [("2023-03-22", "1", 560), ("2023-06-02", "2", 330), ("2023-07-19", "3", 560), ("2023-09-01", "4", 330)]
    for d, n, top in events:
        xd = date2num(dt.date.fromisoformat(d))
        a.vlines(xd, 2.5, top, color=NEUTRAL, linewidth=0.9, linestyle=(0, (3, 3)), zorder=1)
        a.text(xd, top * 1.12, n, ha="center", va="bottom", fontsize=8.5, color=INK, fontweight="bold")
    a.text(date2num(dt.date(2023, 9, 20)), 3.0, "1  22 Mar 2023: offer launched\n2  2 Jun: offer terminated\n"
           "3  19 Jul: support agreement\n4  1 Sep: exchange settles", fontsize=7.8, color=INK_2,
           ha="left", va="bottom", linespacing=1.4)

    # right: the illustrative pair, $10mm face of notes bought at 44.8 against a $1mm short of stock at 4.74 (6.10.1 Beat 5)
    face, short_notional = 10.0, 1.0
    keys = ["2023-03-31", "2023-06-30", "2023-09-29", "2023-12-29"]
    bond = np.array([face * (STACK_MARK[k] - STACK_MARK["2022-12-30"]) / 100 for k in keys])
    shortpl = np.array([-short_notional * (EQUITY_CLOSE[k] / EQUITY_CLOSE["2022-12-30"] - 1) for k in keys])
    net = bond + shortpl
    assert abs(bond[-1] - 3.99) < 0.02 and abs(shortpl[-1] + 10.17) < 0.02          # the chapter's "$4 million" and "$10.2 million"
    xs = np.arange(4)
    w = 0.36
    b.set_axisbelow(True)
    b.bar(xs - w / 2, bond, width=w, color=BLUE)
    b.bar(xs + w / 2, shortpl, width=w, color=ORANGE)
    b.plot(xs, net, "D", color=INK, markersize=5.5, zorder=5)
    b.axhline(0, color=NEUTRAL, linewidth=0.8)
    b.text(xs[-1] - w / 2, bond[-1] + 0.25, f"+{bond[-1]:.1f}", ha="center", va="bottom", fontsize=8.5, color=INK_2)
    b.text(xs[-1] + w / 2, shortpl[-1] - 0.3, f"{MINUS}{abs(shortpl[-1]):.1f}", ha="center", va="top", fontsize=8.5, color=INK_2)
    b.text(xs[-1] - w / 2 - 0.12, net[-1], f"net {MINUS}{abs(net[-1]):.1f}", ha="right", va="center", fontsize=8.5, color=INK_2)
    b.set_xticks(xs)
    b.set_xticklabels(["Mar", "Jun", "Sep", "Dec"])
    b.set_xlabel("2023 quarter-ends, since 30 Dec 2022")
    b.set_ylabel("Pair P&L ($mm, before coupons)")
    b.set_ylim(-12.5, 6.8)
    b.legend(handles=[plt.Line2D([], [], marker="s", linestyle="", color=BLUE, markersize=6, label="long $10mm notes"),
                      plt.Line2D([], [], marker="s", linestyle="", color=ORANGE, markersize=6, label="short $1mm stock"),
                      plt.Line2D([], [], marker="D", linestyle="", color=INK, markersize=5, label="net")],
             loc="upper left", fontsize=7.8, handletextpad=0.2, borderaxespad=0.1, labelspacing=0.3)
    return finish(fig, "ch06_carvana_pair"), (bond, shortpl, net)


def main():
    check_worked_example()
    out = {}
    out["vol"] = fig_volatility_tax()
    out["fulcrum"] = fig_merton_payoff_fulcrum()
    out["spread"] = fig_merton_spread_short_end()
    out["svb"] = fig_svb_holdco_waterfall()
    out["cvna"] = fig_carvana_pair()
    for k, v in out.items():
        print(k, v)


if __name__ == "__main__":
    main()
