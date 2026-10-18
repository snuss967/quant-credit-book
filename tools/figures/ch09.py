"""Figures for Chapter 9 (Factor Investing in Corporate Credit).

Run:  python3 tools/figures/ch09.py      -> assets/figures/ch09_*.png  (five figures, in order of appearance)

Colour roles held fixed across the chapter's figures:
  ORANGE = the naive, dollar-neutral construction;  BLUE = the DTS-neutral construction (fig 1)
  VIOLET = equity momentum in credit (EMC) (figs 2-3)
  BLUE / GREEN = Israel-Palhares-Richardson / Man factor sets (fig 4)
Data policy (see style.py): figs 2-4 use only numbers quoted in the chapter text from the shelf sources
(Dynkin et al., Man Group, Israel-Palhares-Richardson); fig 4's curves apply equation (9.5) to those numbers.
Figs 1 and 5 are generated from the models stated in their captions and are labelled Illustrative.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
import numpy as np  # noqa: E402
from matplotlib.lines import Line2D  # noqa: E402
from matplotlib.patches import FancyArrowPatch  # noqa: E402
from matplotlib.ticker import FuncFormatter, PercentFormatter  # noqa: E402

from style import *  # noqa: E402,F401,F403

VIOLET_TINT = "#d5cff3"


# ---------------------------------------------------------------------------------------------
# 9.2.3  Kaz's book, dollar-neutral vs DTS-neutral (illustrative; the numbers are the chapter's worked example)
# ---------------------------------------------------------------------------------------------
def fig_kaz_book():
    dts_l, dts_s, dts_m = 12.0, 7.2, 8.0          # years x percent, per leg (chapter 9.2.2)
    short_notional = 100 * dts_l / dts_s          # 166.7 ($mm) to match the long leg's DTS
    carry_l, carry_s = 2.0, 1.2                   # % a year

    fig, (a, b) = new_figure(ncols=2)

    # (a) leg DTS per $100mm of long
    vals = [dts_l, dts_s, dts_s * short_notional / 100]
    cols = [NEUTRAL, ORANGE, BLUE]
    x = np.arange(3)
    a.bar(x, vals, 0.66, color=cols)
    for xi, v in zip(x, vals):
        a.text(xi, v - 0.35, f"{v:.1f}", ha="center", va="top", fontsize=9, color=INK, fontweight="bold")
    a.axhline(dts_l, color=MUTED, linewidth=0.9, linestyle=(0, (3, 3)), zorder=1)
    # the gap that becomes beta
    a.add_patch(FancyArrowPatch((1, dts_s + 0.15), (1, dts_l - 0.1), arrowstyle="<|-|>", mutation_scale=8,
                                linewidth=1.1, color=INK_2, shrinkA=0, shrinkB=0, zorder=4))
    a.text(1.08, 0.5 * (dts_s + dts_l) + 0.05, "gap 4.8", ha="left", va="center", fontsize=8, color=INK)
    a.text(-0.5, 14.9, "$\\beta$ = gap ÷ market DTS (8.0):\n0.6 dollar-neutral, 0 DTS-neutral", ha="left", va="top",
           fontsize=8, color=INK)
    a.set_xticks(x)
    a.set_xticklabels(["Long leg\n$100mm", "Short leg,\ndollar-neutral\n$100mm", "Short leg,\nDTS-neutral\n$166.7mm"],
                      fontsize=8)
    a.set_ylim(0, 15.2)
    a.set_xlim(-0.55, 2.55)
    a.set_ylabel("Leg DTS per $100mm long (years × %)")
    a.tick_params(axis="x", length=0)

    # (b) monthly book return against the index's excess return
    rng = np.random.default_rng(90210)
    n = 84
    m = rng.normal(0.10, 1.45, n)                                  # index excess return, % per month
    e1 = rng.normal(0, 0.28, n)
    e2 = rng.normal(0, 0.28, n)
    beta_dn = (dts_l - dts_s) / dts_m
    carry_dn = (carry_l - carry_s) / 12                           # % per month, per $ long
    carry_dts = (carry_l - carry_s * short_notional / 100) / 12   # exactly 0
    y_dn = beta_dn * m + carry_dn + e1
    y_dts = 0.0 * m + carry_dts + e2
    xs = np.array([-4.2, 4.2])
    b.axhline(0, color=NEUTRAL, linewidth=0.8, zorder=1)
    b.plot(m, y_dn, "o", color=ORANGE, markersize=4.2, alpha=0.75, markeredgewidth=0, zorder=3)
    b.plot(m, y_dts, "o", color=BLUE, markersize=4.2, alpha=0.75, markeredgewidth=0, zorder=3)
    b.plot(xs, beta_dn * xs + carry_dn, color=ORANGE, linewidth=LW, zorder=4)
    b.plot(xs, 0 * xs + carry_dts, color=BLUE, linewidth=LW, zorder=4)
    b.set_xlim(-4.2, 4.2)
    b.set_ylim(-3.2, 3.2)
    b.set_xlabel("Index excess return in the month (%)")
    b.set_ylabel("Book return, % of long notional")
    b.legend(handles=[Line2D([0], [0], color=ORANGE, marker="o", markersize=4.5, linewidth=LW,
                             label="Dollar-neutral: slope 0.6, carry +0.8%/yr"),
                      Line2D([0], [0], color=BLUE, marker="o", markersize=4.5, linewidth=LW,
                             label="DTS-neutral: slope 0.0, carry 0.0%/yr")],
             loc="upper left", fontsize=7.6, handlelength=1.6, borderaxespad=0.2)
    note(b, "No signal assumed: only beta and carry", loc="lower right")
    return finish(fig, "ch09_kaz_book_dts_neutral")


# ---------------------------------------------------------------------------------------------
# 9.4.1  The decay clock (Dynkin p.610-611, as quoted in the chapter)
# ---------------------------------------------------------------------------------------------
def fig_decay_clock():
    stay3 = 0.17                                   # P(top decile after 3 months), Dynkin p.610
    p1 = stay3 ** (1 / 3)                          # monthly stay probability implied by the Markov chain
    half_life = np.log(0.5) / np.log(p1)           # 1.17 months
    out_bp = [35, 22, 19]                          # months 1, 2, 3 (Dynkin p.611)
    out6 = 95                                      # six-month total
    rest = out6 - sum(out_bp)                      # months 4-6 combined: 19bp

    fig, (a, b) = new_figure(ncols=2)

    t = np.linspace(0, 6, 241)
    a.plot(t, 100 * p1 ** t, color=VIOLET, linewidth=LW, zorder=3)
    tk = np.arange(0, 7)
    a.plot(tk, 100 * p1 ** tk, "o", color=VIOLET, markersize=5, zorder=4)
    a.plot([3], [100 * stay3], "o", color=VIOLET, markersize=8, markerfacecolor="white", markeredgewidth=1.8,
           zorder=5)
    a.annotate("17% after 3 months\n(Dynkin p.610)", (3, 17), xytext=(3.3, 38), fontsize=8, color=INK_2,
               va="center", arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.8, shrinkA=2, shrinkB=5))
    a.plot([0, half_life], [50, 50], color=MUTED, linewidth=0.9, linestyle=(0, (3, 3)), zorder=2)
    a.plot([half_life, half_life], [0, 50], color=MUTED, linewidth=0.9, linestyle=(0, (3, 3)), zorder=2)
    a.text(half_life + 0.12, 52.5, f"half-life {half_life:.1f} months", fontsize=8, color=INK_2, va="bottom")
    a.set_xlim(0, 6)
    a.set_ylim(0, 105)
    a.set_xticks(range(7))
    a.yaxis.set_major_formatter(PercentFormatter(100, decimals=0))
    a.set_xlabel("Months since entering the top decile")
    a.set_ylabel("Still ranked in the top decile")
    note(a, f"Markov chain: stay probability {p1:.2f} a month", loc="upper right")

    # (b) outperformance per month: bars span the months they cover
    for i, v in enumerate(out_bp):
        b.bar(i + 0.5, v, 0.9, color=VIOLET)
        b.text(i + 0.5, v + 1.2, f"{v}", ha="center", va="bottom", fontsize=9, color=INK, fontweight="bold")
    b.bar(4.5, rest / 3, 2.9, color=VIOLET_TINT)
    b.text(4.5, rest / 3 + 1.2, f"{rest}bp in total,\n≈{rest / 3:.1f} a month", ha="center", va="bottom", fontsize=8.2,
           color=INK_2)
    b.set_xlim(0, 6)
    b.set_ylim(0, 44)
    b.set_xticks([0.5, 1.5, 2.5, 4.5])
    b.set_xticklabels(["1", "2", "3", "4–6"])
    b.set_xlabel("Months after the signal")
    b.tick_params(axis="x", length=0)
    b.set_ylabel("Outperformance per month (bp)")
    b.text(1.2, 41.5, f"{sum(out_bp)} of {out6}bp over six months\n({100 * sum(out_bp) / out6:.0f}%) arrives in the first quarter",
           ha="left", va="top", fontsize=8.2, color=INK_2)
    return finish(fig, "ch09_momentum_decay_clock")


# ---------------------------------------------------------------------------------------------
# 9.4.2  Break-even cost (Dynkin p.633 and p.703, as quoted in the chapter)
# ---------------------------------------------------------------------------------------------
def fig_breakeven_cost():
    gross = 6.34                                   # % a year over the index, top-decile EMC (Dynkin p.633)
    to_barclays = 73.0                             # % a month, one-way
    c_star = gross / 12 / (to_barclays / 100)      # 0.72 %
    gross2, c2, to2 = 2.5, 0.6, 100 * (2.5 / 12) / 0.6   # the chapter's worked example: 35% a month

    fig, ax = new_figure("wide")
    fig.get_layout_engine().set(rect=(0, 0, 0.84, 1))
    to = np.linspace(14, 100, 400)
    curve = gross / 12 / (to / 100)
    ax.fill_between(to, 0, np.minimum(curve, 3.4), color=VIOLET, alpha=0.10, linewidth=0, zorder=1)
    ax.plot(to, curve, color=VIOLET, linewidth=LW, zorder=4)
    ax.plot(to, gross2 / 12 / (to / 100), color=MUTED, linewidth=1.2, linestyle=(0, (4, 2.5)), zorder=3)

    # cost levels (right margin labels)
    levels = [(2.8, "IG average cost,\n2008: 2.8%"), (0.941, "HY average,\nJuly 2019: 0.94%"), (0.6, "IG average,\n2018–19: 0.6%")]
    for y, txt in levels:
        ax.axhline(y, color=NEUTRAL, linewidth=0.9, zorder=1)
        ax.annotate(txt, (100, y), xytext=(6, 0), textcoords="offset points", va="center", ha="left", fontsize=8,
                    color=INK_2, annotation_clip=False)

    ax.plot([to_barclays], [c_star], "o", color=VIOLET, markersize=8, zorder=6)
    ax.annotate("Barclays top-decile EMC:\n73% a month, 6.34% a year\nbreak-even cost 0.72%",
                (to_barclays, c_star), xytext=(62, 1.62), fontsize=8.2, color=INK, ha="center", va="center",
                arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.8, shrinkA=2, shrinkB=5))
    ax.plot([to2], [c2], "o", color="white", markeredgecolor=INK_2, markeredgewidth=1.5, markersize=7, zorder=6)
    ax.annotate("2.5% a year gross, 0.6% cost:\n35% a month is the limit", (to2, c2), xytext=(23, 0.2),
                fontsize=8, color=INK_2, ha="left", va="center",
                arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.8, shrinkA=2, shrinkB=5))
    ax.text(20, 3.15, "Loses money after costs", fontsize=8.5, color=INK_2, ha="left", va="center")
    ax.text(86, 0.075, "Profitable after costs", fontsize=8.5, color=INK_2, ha="center", va="center")
    ax.set_xlim(14, 100)
    ax.set_ylim(0, 3.4)
    ax.set_xlabel("One-way turnover (% of the portfolio per month)")
    ax.set_ylabel("Round-trip cost (% of value)")
    ax.xaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{v:.0f}%"))
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{v:.1f}%"))
    return finish(fig, "ch09_breakeven_cost")


# ---------------------------------------------------------------------------------------------
# 9.7.1  Equal-risk combination vs the best single factor (equation 9.5, published IRs)
# ---------------------------------------------------------------------------------------------
def fig_equal_risk():
    sets = [
        ("Israel–Palhares–Richardson", BLUE, [0.35, 1.11, 0.85, 1.75], 2.19),     # quintile-spread Sharpe ratios
        ("Man (simulated IRs)", GREEN, [2.15, 1.69, 1.55, 0.79], 2.35),
    ]
    K = 4
    rho = np.linspace(-0.2, 0.8, 400)
    fig, ax = new_figure("wide")
    fig.get_layout_engine().set(rect=(0, 0, 0.86, 1))
    for name, col, irs, combo in sets:
        s = sum(irs)
        best = max(irs)
        f = lambda r: s / np.sqrt(K + K * (K - 1) * r)                          # noqa: E731
        ax.plot(rho, f(rho), color=col, linewidth=LW, zorder=4)
        ax.axhline(best, color=col, linewidth=1.0, linestyle=(0, (4, 2.5)), zorder=2)
        rho_imp = ((s / combo) ** 2 - K) / (K * (K - 1))
        rho_x = ((s / best) ** 2 - K) / (K * (K - 1))
        ax.plot([rho_imp], [combo], "o", color=col, markersize=8, markerfacecolor="white", markeredgewidth=1.8,
                zorder=6)
        ax.plot([rho_x], [best], "D", color=col, markersize=6, zorder=6)
        print(f"{name}: sum IR {s:.2f}, best {best}, published combo {combo}, implied rho {rho_imp:.3f}, "
              f"break-even rho {rho_x:.3f}")
        label_end(ax, rho[-1], f(rho[-1]), name.replace(" (simulated IRs)", ""), col, dx=6, annotation_clip=False)
        if name.startswith("Israel"):       # best-single label below its line, right of centre (both curves are clear of it)
            ax.text(0.66, best - 0.04, f"best single factor {best:.2f}", fontsize=8, color=INK_2,
                    va="top", ha="right")
        else:                                # best-single label above its line, on the right (the curve is below it)
            ax.text(rho[-1] - 0.01, best + 0.05, f"best single factor {best:.2f}", fontsize=8, color=INK_2,
                    va="bottom", ha="right")
    ax.legend(handles=[
        Line2D([0], [0], marker="o", color="white", markeredgecolor=INK_2, markeredgewidth=1.6, markersize=7,
               linewidth=0, label="Published blend, plotted at the correlation\nit implies (IPR −0.05, Man 0.24)"),
        Line2D([0], [0], marker="D", color=INK_2, markersize=5.5, linewidth=0,
               label="Correlation at which the blend only ties the\nbest single factor (IPR 0.12, Man 0.36)")],
        loc="lower left", fontsize=7.8, borderaxespad=0.2, handletextpad=0.5, labelspacing=0.8)
    ax.set_xlim(-0.2, 0.8)
    ax.set_ylim(0, 3.5)
    ax.set_xlabel("Average pairwise correlation between the four factors")
    ax.set_ylabel("Information ratio of the equal-risk blend")
    return finish(fig, "ch09_equal_risk_vs_best_single")


# ---------------------------------------------------------------------------------------------
# 9.9  Noisy prices manufacture a premium (illustrative simulation of the section's model)
# ---------------------------------------------------------------------------------------------
def fig_noisy_price():
    rng = np.random.default_rng(1983)
    fig, (a, b) = new_figure(ncols=2)

    # (a) Blume-Stambaugh bias: mean computed return minus true return, vs the pricing-error size
    r_true = 0.004
    sig = np.linspace(0, 0.05, 11)
    n = 2_000_000
    bias_bp = []
    for s in sig:
        u0 = rng.normal(0, s, n)
        u1 = rng.normal(0, s, n)
        rc = (1 + r_true) * (1 + u1) / (1 + u0) - 1
        bias_bp.append(1e4 * (rc.mean() - r_true))
    fine = np.linspace(0, 0.05, 200)
    a.plot(100 * fine, 1e4 * fine ** 2, color=NEUTRAL, linewidth=LW, zorder=2)
    a.plot(100 * sig, bias_bp, "o", color=BLUE, markersize=5.5, zorder=4)
    a.annotate("$\\sigma_u$ = 3%: 9bp a month\n≈ 1.1% a year", (3.0, 9.0), xytext=(0.35, 19.5), fontsize=8.2,
               color=INK_2, ha="left", va="center",
               arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.8, shrinkA=2, shrinkB=5))
    a.set_xlim(0, 5.2)
    a.set_ylim(0, 28)
    a.set_xlabel("Pricing error $\\sigma_u$ (% of price)")
    a.set_ylabel("Upward bias in mean return (bp a month)")
    a.legend(handles=[Line2D([0], [0], color=BLUE, marker="o", linewidth=0, markersize=5.5, label="Simulated"),
                      Line2D([0], [0], color=NEUTRAL, linewidth=LW, label="$\\sigma_u^{2}$, equation (9.6)")],
             loc="lower right", fontsize=8, borderaxespad=0.2)

    # (b) a reversal sort on noisy marks: lag one shares a price with the return it forecasts; lag two does not
    N, T, sig_u, sig_r = 1000, 244, 0.01, 0.03
    r = rng.normal(0.004, sig_r, (T, N))                        # true returns: i.i.d., no reversal built in
    P = 100 * np.cumprod(1 + r, axis=0)
    Pn = P * (1 + rng.normal(0, sig_u, (T, N)))
    R = Pn[1:] / Pn[:-1] - 1                                    # computed returns, month t = row t-1 .. t
    lags = [1, 2, 3, 4]
    mean_ls, se_ls = [], []
    k = max(lags)
    for lag in lags:
        ls = []
        for t in range(k, R.shape[0]):
            sig_t = R[t - lag]                                  # lag 1 = last month's computed return
            lo, hi = np.quantile(sig_t, [0.1, 0.9])
            ls.append(R[t][sig_t <= lo].mean() - R[t][sig_t >= hi].mean())   # buy losers, short winners
        ls = 100 * np.array(ls)
        mean_ls.append(ls.mean())
        se_ls.append(ls.std(ddof=1) / np.sqrt(len(ls)))
    print("reversal L/S (% a month):", [f"{m:.3f} +/- {2 * s:.3f}" for m, s in zip(mean_ls, se_ls)])
    x = np.arange(len(lags))
    cols = [BLUE if lag == 1 else NEUTRAL for lag in lags]
    b.bar(x, mean_ls, 0.62, color=cols)
    b.errorbar(x, mean_ls, yerr=2 * np.array(se_ls), fmt="none", ecolor=INK_2, elinewidth=1.0, capsize=3, zorder=5)
    b.text(0, mean_ls[0] + 0.14, f"{mean_ls[0]:.2f}%", ha="center", va="bottom", fontsize=9, color=INK,
           fontweight="bold")
    b.axhline(0, color=NEUTRAL, linewidth=0.8, zorder=1)
    b.set_xticks(x)
    b.set_xticklabels(["Lag 1", "Lag 2", "Lag 3", "Lag 4"])
    b.text(1, 0.2, "no shared\nprice", ha="center", va="bottom", fontsize=7.8, color=INK_2)
    b.tick_params(axis="x", length=0)
    b.set_ylim(-0.25, 1.55)
    b.set_ylabel("Long–short return of the sort (% a month)")
    note(b, "True returns are i.i.d.: any 'alpha' is\nthe pricing error ($\\sigma_u$ = 1%) giving itself back",
         loc="upper right")
    return finish(fig, "ch09_noisy_price_premium")


if __name__ == "__main__":
    fig_kaz_book()
    fig_decay_clock()
    fig_breakeven_cost()
    fig_equal_risk()
    fig_noisy_price()
