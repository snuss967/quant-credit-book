"""Figures for Chapter 16 (Post-Reorganization Equities, Rights Offerings & Bankruptcy Claims).

Run:  python3 tools/figures/ch16.py   -> assets/figures/ch16_*.png

Colour use in this chapter: BLUE is the instrument or path the figure is about, ORANGE is the comparison
case; NEUTRAL carries reference lines and the no-uncertainty benchmark.
"""
import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from style import *  # noqa: E402,F401,F403  (applies the rcParams on import)

import datetime as dt  # noqa: E402

import numpy as np  # noqa: E402
from matplotlib.patches import FancyArrowPatch  # noqa: E402
from scipy.stats import norm  # noqa: E402


# --------------------------------------------------------------------------------------------------
# Figure 16.1: forced-seller overhang, instant release vs staggered delivery (section 16.2.2)
# --------------------------------------------------------------------------------------------------
def fig_overhang_delivery_lag():
    theta, alpha, A = 3.4, 5.0, 0.15          # per year; A = kappa*Q0/M = 15% (the Poker Table values)
    s = np.linspace(0, 1.0, 600)               # years since the event
    months = s * 12
    inst = -A * np.exp(-theta * s) * 100
    q = alpha / (theta - alpha) * (np.exp(-alpha * s) - np.exp(-theta * s))   # Q_s / Q_0
    stag = -A * q * 100
    s_star = np.log(theta / alpha) / (theta - alpha)                          # 0.241 y
    q_star = alpha / (theta - alpha) * (np.exp(-alpha * s_star) - np.exp(-theta * s_star))
    trough = -A * q_star * 100
    half = np.log(2) / theta

    fig, ax = new_figure("wide")
    ax.axhline(0, color=NEUTRAL, linewidth=0.9, zorder=1)
    ax.plot(months, inst, color=ORANGE, linewidth=LW, label="All shares in constrained hands on day 0")
    ax.plot(months, stag, color=BLUE, linewidth=LW, label="Shares delivered over weeks (mean lag 2.4 months)")

    # trough of the staggered path
    ax.plot([s_star * 12], [trough], "o", color=BLUE, markersize=6, zorder=5)
    ax.annotate(f"Trough \u2212{abs(trough):.1f}% at {s_star*12:.1f} months:\nafter the event, not at it",
                (s_star * 12, trough), xytext=(4.1, -9.6), textcoords="data", fontsize=8.5,
                color=INK_2, va="center",
                arrowprops=dict(arrowstyle="-", color=NEUTRAL, linewidth=0.8, shrinkA=2, shrinkB=4))
    # half-life of the instant-release path
    ax.plot([half * 12], [-A * 50], "o", color=ORANGE, markersize=6, zorder=5)
    ax.annotate(f"Half the discount gone after\n{half*12:.1f} months (ln 2 / 3.4)", (half * 12, -A * 50),
                xytext=(0.55, -11.0), textcoords="data", fontsize=8.5, color=INK_2, va="center",
                arrowprops=dict(arrowstyle="-", color=NEUTRAL, linewidth=0.8, shrinkA=2, shrinkB=4))
    # 200 trading days
    mark_event(ax, 200 / 252 * 12, "200 trading days", y_frac=0.97)

    ax.set_xlim(0, 12)
    ax.set_ylim(-16.5, 1.5)
    ax.set_xticks(range(0, 13, 2))
    ax.set_xlabel("Months since the effective date or lock-up expiry")
    ax.set_ylabel("Liquidity discount, p − v (log %)")
    ax.legend(loc="lower right", bbox_to_anchor=(1.0, 0.04))
    note(ax, "θ = 3.4 per year, α = 5 per year, κ Q₀ / M = 15%", loc="lower left")
    return finish(fig, "ch16_overhang_delivery_lag")


# --------------------------------------------------------------------------------------------------
# Figure 16.2: rights and backstop payoffs, and the fair fee against the discount (section 16.3.2)
# --------------------------------------------------------------------------------------------------
def bs_put_zero_rate(x0, K, sigma, T):
    d1 = (np.log(x0 / K) + 0.5 * sigma ** 2 * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return K * norm.cdf(-d2) - x0 * norm.cdf(-d1)


def fair_fee(discount, T, sigma=0.70, dilution=0.64):
    K = 1.0 - discount
    return dilution * bs_put_zero_rate(1.0, K, sigma, T) / K * 100


def fig_backstop_put_and_fee():
    K, x0 = 0.75, 1.0
    f = 163.5 / (291.25 + 163.5)                # m / (n0 + m) for Hertz = 0.36
    x = np.linspace(0.3, 1.6, 400)
    right = f * np.maximum(x - K, 0)
    backstop = -f * np.maximum(K - x, 0)

    fig, (a1, a2) = new_figure("wide", ncols=2)

    # left: payoffs at funding
    a1.axhline(0, color=NEUTRAL, linewidth=0.9, zorder=1)
    a1.plot(x, right, color=BLUE, linewidth=LW)
    a1.plot(x, backstop, color=ORANGE, linewidth=LW)
    a1.axvline(K, color=NEUTRAL, linewidth=0.9, linestyle=(0, (3, 3)), zorder=1)
    a1.axvline(x0, color=NEUTRAL, linewidth=0.9, linestyle=(0, (3, 3)), zorder=1)
    a1.annotate("K = 0.75", (K, 0.98), xycoords=("data", "axes fraction"), xytext=(-3, 0),
                textcoords="offset points", ha="right", fontsize=8, color=INK_2, va="top")
    a1.annotate("fair value\nx\u2080 = 1.00", (x0, 0.98), xycoords=("data", "axes fraction"), xytext=(3, 0),
                textcoords="offset points", ha="left", fontsize=8, color=INK_2, va="top")
    a1.plot([1.45], [f * (1.45 - K)], "o", color=BLUE, markersize=5, zorder=5)
    a1.plot([0.38], [-f * (K - 0.38)], "o", color=ORANGE, markersize=5, zorder=5)
    a1.plot([0.035], [0.77], "o", color=BLUE, markersize=6, transform=a1.transAxes, clip_on=False)
    a1.text(0.07, 0.77, "Rights holder:\na call on x", transform=a1.transAxes,
            color=INK_2, fontsize=8.5, va="center")
    a1.plot([0.60], [0.13], "o", color=ORANGE, markersize=6, transform=a1.transAxes, clip_on=False)
    a1.text(0.635, 0.13, "Backstop party:\nshort put at K", transform=a1.transAxes, color=INK_2,
            fontsize=8.5, va="center")
    a1.set_xlim(0.3, 1.6)
    a1.set_ylim(-0.20, 0.34)
    a1.set_xlabel("Pre-money value per plan share at funding, x")
    a1.set_ylabel("Payoff per plan share, before the fee")
    a1.set_title("Payoffs at funding", fontsize=9.5)

    # right: fair fee vs discount
    d = np.linspace(0, 0.60, 241)
    a2.axhline(6, color=NEUTRAL, linewidth=0.9, linestyle=(0, (3, 3)), zorder=1)
    a2.annotate("6%: Seth average", (59, 6), xytext=(0, 4),
                textcoords="offset points", ha="right", fontsize=7.5, color=INK_2)
    a2.axhline(10, color=NEUTRAL, linewidth=0.9, linestyle=(0, (3, 3)), zorder=1)
    a2.annotate("10%: Hertz fee", (59, 10), xytext=(0, 4), textcoords="offset points", ha="right",
                fontsize=7.5, color=INK_2)
    a2.plot(d * 100, fair_fee(d, 0.50), color=BLUE, linewidth=LW, label="Commitment window T = 0.50 y")
    a2.plot(d * 100, fair_fee(d, 0.25), color=ORANGE, linewidth=LW, label="Commitment window T = 0.25 y")
    for dd in (0.0, 0.25, 0.50):
        a2.plot([dd * 100], [fair_fee(dd, 0.50)], "o", color=BLUE, markersize=5, zorder=5)
        a2.plot([dd * 100], [fair_fee(dd, 0.25)], "o", color=ORANGE, markersize=5, zorder=5)
    a2.legend(loc="lower left", bbox_to_anchor=(0.0, 0.0), fontsize=8)
    a2.set_xlim(0, 60)
    a2.set_ylim(0, 14.5)
    a2.set_xlabel("Rights-price discount to fair value (%)")
    a2.set_ylabel("Fair backstop fee (% of raise)")
    a2.set_title("Fee and discount are substitutes", fontsize=9.5)
    note(a2, "σ = 70%, dilution factor 0.64, zero rate", loc="upper right")
    a2.texts[-1].set_position((0.99, 0.80))
    return finish(fig, "ch16_backstop_put_and_fee")


# --------------------------------------------------------------------------------------------------
# Figure 16.3: expected recovery with a random claims pool (section 16.5.3)
# --------------------------------------------------------------------------------------------------
def expected_recovery(v_over_m, s):
    """E[min(1, V/C)] with ln C ~ N(ln m - s^2/2, s^2) and V fixed (section 16.5.3, special case)."""
    v = np.asarray(v_over_m, dtype=float)
    a = (np.log(v) + s ** 2 / 2) / s
    return norm.cdf(a) + v * np.exp(s ** 2) * norm.cdf(-a - s)


def fig_claim_recovery_pool_risk():
    v = np.linspace(0.05, 2.0, 600)
    fig, ax = new_figure("wide")
    ax.axvline(1.0, color=NEUTRAL, linewidth=0.9, linestyle=(0, (3, 3)), zorder=1)
    ax.plot(v, np.minimum(1, v), color=NEUTRAL, linewidth=LW, linestyle=(0, (4, 2)),
            label="No pool uncertainty: min(1, V / m)")
    ax.plot(v, expected_recovery(v, 0.30), color=BLUE, linewidth=LW, label="Pool log-sd s = 0.30")
    ax.plot(v, expected_recovery(v, 0.60), color=ORANGE, linewidth=LW, label="Pool log-sd s = 0.60")

    r_par = float(expected_recovery(1.0, 0.30))
    r_deep = float(expected_recovery(0.30, 0.30))
    ax.plot([1.0], [r_par], "o", color=BLUE, markersize=6, zorder=5)
    ax.annotate(f"Covered on average: E[R] = {r_par:.3f},\n{(1-r_par)*100:.1f} points lost to the cap",
                (1.0, r_par), xytext=(14, -34), textcoords="offset points", fontsize=8.5, color=INK_2,
                va="center", arrowprops=dict(arrowstyle="-", color=NEUTRAL, linewidth=0.8))
    ax.plot([0.30], [r_deep], "o", color=BLUE, markersize=6, zorder=5)
    ax.annotate(f"Deeply impaired: E[R] = {r_deep:.3f}\nbeats 0.300, variance helps",
                (0.30, r_deep), xytext=(0.47, 0.13), textcoords="data", fontsize=8.5, color=INK_2,
                va="center", arrowprops=dict(arrowstyle="-", color=NEUTRAL, linewidth=0.8))
    ax.set_xlim(0, 2.0)
    ax.set_ylim(0, 1.08)
    ax.set_xlabel("Distributable value ÷ expected allowed claims, V / m")
    ax.set_ylabel("Expected recovery per $ of face, E[R]")
    ax.legend(loc="lower right")
    return finish(fig, "ch16_claim_recovery_pool_risk")


# --------------------------------------------------------------------------------------------------
# Figure 16.4: Hertz 2020-2026 timeline with the sourced price points (section 16.6)
# --------------------------------------------------------------------------------------------------
def fig_hertz_timeline():
    D = dt.date
    fig, (ax, bx) = new_figure((7.0, 5.4), nrows=2, sharex=True,
                               gridspec_kw={"height_ratios": [1.9, 1.0]})
    x0, x1 = D(2020, 3, 1), D(2027, 1, 15)

    # --- top: events
    ax.grid(False)
    for sp in ("left", "bottom"):
        ax.spines[sp].set_visible(False)
    ax.set_yticks([])
    ax.tick_params(axis="x", length=0)
    ax.axhline(0, color=NEUTRAL, linewidth=1.2, zorder=1)
    ax.set_ylim(-4.9, 5.4)

    ticks = [D(2020, 5, 22), D(2020, 6, 12), D(2021, 5, 11), D(2021, 6, 10), D(2021, 6, 15), D(2021, 6, 30),
             D(2021, 11, 8), D(2024, 9, 10), D(2026, 6, 15), D(2026, 10, 16)]
    ax.plot(ticks, [0] * len(ticks), "o", color=BLUE, markersize=5, zorder=4)

    # (anchor date, y of label, ha, text, unused)
    labels = [
        (D(2020, 5, 22), 3.0, "left", "22 May 2020: Chapter 11 filed.\n12 Jun: $1bn stock program\nauthorized, then suspended\nafter ~$29mm sold", 0),
        (D(2021, 5, 11), -1.3, "right", "11 May 2021: sponsor auction ends;\nold holders get $1.53 cash,\n3% of the stock, and a choice of\nwarrants or rights at $10", 0),
        (D(2021, 6, 20), -3.0, "left", "Jun 2021: plan confirmed (10th),\nrights expire (15th), effective\ndate (30th); $1.635bn raised", 0),
        (D(2021, 11, 8), 1.0, "left", "8 Nov 2021: re-IPO at $29.00;\nHTZ and warrants list", 0),
        (D(2024, 9, 10), 1.3, "center", "10 Sep 2024: Third Circuit\nholds solvent debtor owes\nnoteholders contract-rate\ninterest (>$270mm)", 0),
        (D(2026, 6, 15), -1.5, "right", "Jun 2026 (approx.): profit warning,\n$350mm PIK exchangeables,\nstock down 41% in a day to ~$3", 0),
        (D(2026, 10, 16), 3.7, "right", "16 Oct 2026: revolver and secured\ngroups hire counsel; Hertz\nworks with PJT Partners", 0),
    ]
    for d, y, ha, text, _ in labels:
        ax.plot([d, d], [0, y * 0.92 if y > 0 else y * 0.92], color=NEUTRAL, linewidth=0.8, zorder=2)
        ax.annotate(text, (d, y), xytext=(0, 0), textcoords="offset points", ha=ha,
                    va="bottom" if y > 0 else "top", fontsize=7.5, color=INK, linespacing=1.25)
    ax.set_xlim(x0, x1)

    # --- bottom: sourced price points and the warrant strike
    bx.axhline(13.80, color=NEUTRAL, linewidth=0.9, linestyle=(0, (3, 3)), zorder=1)
    bx.annotate("Warrant strike $13.80 (expire 30 Jun 2051)", (D(2022, 3, 1), 13.80), xytext=(0, 4),
                textcoords="offset points", fontsize=7.5, color=INK_2, ha="left")
    pts = [(D(2021, 6, 30), 10.00, "$10.00 rights price", (6, -4), "left", "top"),
           (D(2021, 11, 8), 29.00, "$29.00 re-IPO", (-6, -2), "right", "top"),
           (D(2026, 6, 15), 3.0, "~$3 (approx.)", (-8, 8), "right", "bottom")]
    for d, p, t, off, ha, va in pts:
        bx.plot([d], [p], "o", color=BLUE, markersize=6, zorder=5)
        bx.annotate(t, (d, p), xytext=off, textcoords="offset points", ha=ha, va=va, fontsize=8,
                    color=INK_2)
    bx.set_ylim(0, 35)
    bx.set_ylabel("Share price (USD)")
    bx.set_xlim(x0, x1)
    bx.xaxis.set_major_locator(matplotlib_dates().YearLocator())
    bx.xaxis.set_major_formatter(matplotlib_dates().DateFormatter("%Y"))
    note(bx, "Dots are the only prices in the record cited here; no path is implied between them.",
         loc="upper left")
    bx.texts[-1].set_position((0.01, 0.97))
    return finish(fig, "ch16_hertz_timeline")


def matplotlib_dates():
    import matplotlib.dates as mdates
    return mdates


# --------------------------------------------------------------------------------------------------
# Figure 16.5: the distribution being traded, single name vs 20-name book (section 16.8.1)
# --------------------------------------------------------------------------------------------------
def fig_post_reorg_return_distribution():
    rng = np.random.default_rng(16)
    p_j = 0.05
    s = np.sqrt(2 * np.log(1.4))
    n_names, n_books = 20, 20000

    def draw(n):
        x = rng.normal(0.0, s, n)
        j = rng.random(n) < p_j
        return np.where(j, -1.0, np.exp(x) - 1.0)

    single = draw(400_000)
    book = draw(n_books * n_names).reshape(n_books, n_names).mean(axis=1)
    stats = {k: (v.mean() * 100, np.median(v) * 100) for k, v in (("single", single), ("book", book))}
    print("single mean/median %:", [round(z, 1) for z in stats["single"]],
          "| book mean/median %:", [round(z, 1) for z in stats["book"]],
          "| P(single > +300 pct): {:.1f}".format((single > 3).mean() * 100),
          "| P(book < 0) pct: {:.1f}".format((book < 0).mean() * 100))

    fig, (a1, a2) = new_figure("wide", ncols=2)

    def panel(ax, data, lo, hi, width, color, title, mean_med, label_dy):
        edges = np.arange(lo, hi + width, width)
        h, _ = np.histogram(data * 100, bins=edges)
        h = h / len(data) * 100
        ax.bar(edges[:-1] + width / 2, h, width=width * 0.88, color=color)
        mean, med = mean_med
        top = h.max()
        ax.axvline(med, color=INK_2, linewidth=1.0, linestyle=(0, (3, 3)), zorder=3)
        ax.axvline(mean, color=INK, linewidth=1.0, zorder=3)
        ax.set_title(title, fontsize=9.5)
        ax.set_ylabel("Share of outcomes per bin (%)")
        ax.set_xlim(lo, hi)
        return top, mean, med

    top, mean, med = panel(a1, single, -100, 300, 10, BLUE, "One post-reorg name", stats["single"], 0)
    a1.set_ylim(0, top * 1.45)
    a1.annotate(f"mean {mean:+.0f}%", (mean, top * 1.36), xytext=(5, 0), textcoords="offset points",
                fontsize=8.5, color=INK, va="center")
    a1.annotate(f"median {med:+.0f}%".replace("-", "\u2212"), (med, top * 1.36), xytext=(-5, 0), textcoords="offset points",
                fontsize=8.5, color=INK_2, va="center", ha="right")
    a1.text(-98, top * 1.16, "5% of names jump to \u2212100%\n(the Spirit shape)", fontsize=8, color=INK_2, va="center")
    a1.plot([-95, -95], [top * 0.84, top * 1.06], color=NEUTRAL, linewidth=0.8, zorder=2)
    a1.set_xlabel("200-day return (%); axis cut at +300%")
    a1.text(0.99, 0.62, f"{(single > 3).mean()*100:.1f}% of outcomes\nlie beyond +300%", transform=a1.transAxes,
            ha="right", va="top", fontsize=8, color=MUTED)

    top2, mean2, med2 = panel(a2, book, -60, 160, 5, ORANGE, "Equal-weighted book of 20 names",
                              stats["book"], 0)
    a2.set_ylim(0, top2 * 1.45)
    a2.annotate(f"mean {mean2:+.0f}%", (mean2, top2 * 1.36), xytext=(5, 0), textcoords="offset points",
                fontsize=8.5, color=INK, va="center")
    a2.annotate(f"median {med2:+.0f}%", (med2, top2 * 1.36), xytext=(-5, 0), textcoords="offset points",
                fontsize=8.5, color=INK_2, va="center", ha="right")
    a2.set_xlabel("200-day book return (%)")
    a2.text(0.99, 0.62, f"{(book < 0).mean()*100:.0f}% of simulated\nbooks lose money", transform=a2.transAxes,
            ha="right", va="top", fontsize=8, color=MUTED)
    return finish(fig, "ch16_post_reorg_return_distribution")


if __name__ == "__main__":
    fig_overhang_delivery_lag()
    fig_backstop_put_and_fee()
    fig_claim_recovery_pool_risk()
    fig_hertz_timeline()
    fig_post_reorg_return_distribution()
