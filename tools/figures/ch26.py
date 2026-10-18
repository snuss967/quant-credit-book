"""Chapter 26 figures: AI agents and LLMs on the credit desk.

Run from anywhere:  python3 tools/figures/ch26.py   (writes assets/figures/ch26_*.png)

Figures
  ch26_citation_contract      the (V, S, A) sorting of a claim into four named cells (section 26.4)
  ch26_calibration_power      reliability diagram and risk-coverage curve of three simulated readers (section 26.4)
  ch26_abstention_threshold   expected cost of answering vs abstaining, and p* and coverage vs the cost ratio (section 26.5)
  ch26_chain_reliability      reliability of an n-step chain, and pass@k vs pass^k (section 26.6)
  ch26_luck_hurdle            expected best Sharpe ratio of N zero-alpha trials (section 26.7)

Data
  Nothing here is observed data. The chapter's quantities are all closed forms (chain product, pass^k,
  p* = 1 - C_abs/C_FP, expected maximum Sharpe) or the §26.12 stochastic reader, which is re-created
  here from its stated model: p_true = logistic(N(1.4, 0.9^2)), the reader is right with probability
  p_true, stated confidence = 1 - (1 - p)(1 - overconf), 20,000 questions, seeded.
  Every caption says "Illustrative".
"""
import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from style import *            # applies the rcParams on import

import numpy as np
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Polygon
from scipy.stats import norm

SEED = 26


# --------------------------------------------------------------------------------------------------
# helpers
# --------------------------------------------------------------------------------------------------
def tint(hex_color, a=0.16):
    """Blend a hex color toward white (a = weight of the color)."""
    h = hex_color.lstrip("#")
    r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    return "#%02x%02x%02x" % tuple(int(round(255 - (255 - c) * a)) for c in (r, g, b))


def simulate_readers(n=20_000, seed=SEED):
    """The section 26.12 reader: right with probability p_true; confidence = 1-(1-p)(1-overconf)."""
    rng = np.random.default_rng(seed)
    p = 1.0 / (1.0 + np.exp(-rng.normal(1.4, 0.9, n)))
    correct = rng.random(n) < p
    conf_cal = p
    conf_over = 1.0 - (1.0 - p) * (1.0 - 0.6)
    conf_flat = rng.permutation(conf_cal)          # confidence with zero power
    return p, correct.astype(float), conf_cal, conf_over, conf_flat


def risk_coverage(conf, correct):
    order = np.argsort(-conf, kind="stable")
    err = 1.0 - correct[order]
    k = np.arange(1, len(err) + 1)
    return k / len(err), np.cumsum(err) / k


def reliability(conf, correct, bins=10):
    idx = np.minimum((conf * bins).astype(int), bins - 1)
    xs, ys = [], []
    for b in range(bins):
        m = idx == b
        if m.sum() >= 30:
            xs.append(conf[m].mean())
            ys.append(correct[m].mean())
    ece = sum((idx == b).mean() * abs(correct[idx == b].mean() - conf[idx == b].mean())
              for b in range(bins) if (idx == b).any())
    return np.array(xs), np.array(ys), float(ece)


# --------------------------------------------------------------------------------------------------
# Figure 1: the citation contract as a decision path
# --------------------------------------------------------------------------------------------------
def fig_citation_contract():
    fig, ax = new_figure((7.0, 4.3))
    ax.grid(False)
    for s in ax.spines.values():
        s.set_visible(False)
    ax.set_xticks([]); ax.set_yticks([])
    ax.set_xlim(0, 100); ax.set_ylim(0, 58)

    def arrow(p0, p1, color=INK_2):
        ax.add_patch(FancyArrowPatch(p0, p1, arrowstyle="-|>", mutation_scale=9, lw=1.1,
                                     color=color, shrinkA=0, shrinkB=0, zorder=3))

    def diamond(cx, cy, w, h, line1, line2):
        ax.add_patch(Polygon([(cx - w / 2, cy), (cx, cy + h / 2), (cx + w / 2, cy), (cx, cy - h / 2)],
                             closed=True, fc="#f3f2ee", ec=NEUTRAL, lw=1.1, zorder=2))
        ax.text(cx, cy + 2.0, line1, ha="center", va="center", fontsize=8.2, color=INK, fontweight="bold")
        ax.text(cx, cy - 1.6, line2, ha="center", va="center", fontsize=7.4, color=INK_2)

    def box(cx, cy, w, h, color, title, body, bold_title=True, tint_a=0.16):
        ax.add_patch(FancyBboxPatch((cx - w / 2, cy - h / 2), w, h, boxstyle="round,pad=0,rounding_size=1.2",
                                    fc=tint(color, tint_a), ec=color, lw=1.4, zorder=2))
        ax.text(cx, cy + h / 2 - 1.8, title, ha="center", va="top", fontsize=7.7, color=INK,
                fontweight="bold" if bold_title else "normal")
        ax.text(cx, cy + h / 2 - 5.2, body, ha="center", va="top", fontsize=7.1, color=INK_2,
                linespacing=1.35)

    y_main = 43.0
    # claim
    ax.add_patch(FancyBboxPatch((0.6, y_main - 8), 13.0, 16, boxstyle="round,pad=0,rounding_size=1.2",
                                fc="#f3f2ee", ec=NEUTRAL, lw=1.1, zorder=2))
    ax.text(7.1, y_main + 4.6, "A claim", ha="center", va="center", fontsize=8.2, color=INK, fontweight="bold")
    ax.text(7.1, y_main - 1.0, r"text, $d$, $\pi$," + "\n" + r"$[a,b)$, $\hat{p}$", ha="center", va="center",
            fontsize=7.6, color=INK_2, linespacing=1.4)

    xs = [26.0, 49.5, 73.0]
    names = [("V", "pointer resolves?", "valid = mean V"),
             ("S", "span supports it?", "support = mean S"),
             ("A", "assertion correct?", "acc = mean A")]
    for x, (a, b, rate) in zip(xs, names):
        diamond(x, y_main, 18.0, 19.0, a, b)
        ax.text(x, y_main + 11.4, rate, ha="center", va="bottom", fontsize=7.2, color=MUTED)

    # main-row arrows (yes)
    arrow((13.6, y_main), (xs[0] - 9.0, y_main))
    for i in range(2):
        x0, x1 = xs[i] + 9.0, xs[i + 1] - 9.0
        arrow((x0, y_main), (x1, y_main))
        ax.text((x0 + x1) / 2, y_main + 1.3, "yes", ha="center", va="bottom", fontsize=7.4, color=INK_2)
    # good claim
    xg = 92.6
    arrow((xs[2] + 9.0, y_main), (xg - 6.8, y_main))
    ax.text((xs[2] + 9.0 + xg - 6.8) / 2, y_main + 1.3, "yes", ha="center", va="bottom", fontsize=7.4, color=INK_2)
    box(xg, y_main, 13.4, 17.0, STATUS["good"], "Good claim",
        "V = S = A = 1:\nright number,\nright span,\nright date")

    # failure boxes
    y_fail, h_fail, w_fail = 16.2, 22.0, 22.4
    fails = [
        (xs[0], STATUS["serious"], "Fabricated pointer",
         "V = 0, e.g. §6.08(b)(xiv),\na clause that does not\nexist\n\nCaught by: code\n(pointer resolution)"),
        (xs[1], STATUS["critical"], "Footnoted hallucination",
         "V = 1, S = 0: a real clause\ncited for what it does not\nsay. FH = mean of V(1 - S)\n\nCaught by: code, if the\nsupport test is good"),
        (xs[2], STATUS["warning"], "Stale support",
         "V = S = 1, A = 0: quotes the\nbasket that Amendment\nNo. 2 replaced\n\nCaught by: point-in-time\nstore, \"as amended through\""),
    ]
    for x, col, title, body in fails:
        top = y_fail + h_fail / 2
        arrow((x, y_main - 9.5), (x, top), color=INK_2)
        ax.text(x + 1.0, (y_main - 9.5 + top) / 2, "no", ha="left", va="center", fontsize=7.4, color=INK_2)
        box(x, y_fail, w_fail, h_fail, col, title, body, tint_a=0.18)

    ax.text(0.6, 0.2, "S = 1 implies V = 1.  A claim with no citation is V = 0, never neutral.",
            ha="left", va="bottom", fontsize=7.4, color=MUTED)
    return finish(fig, "ch26_citation_contract")


# --------------------------------------------------------------------------------------------------
# Figure 2: calibration vs power
# --------------------------------------------------------------------------------------------------
def fig_calibration_power():
    p, correct, c_cal, c_over, c_flat = simulate_readers()
    fig, (axl, axr) = new_figure("wide", ncols=2)

    # left: reliability diagram
    axl.plot([0, 1], [0, 1], color=NEUTRAL, lw=1.0, linestyle=(0, (3, 3)), zorder=1)
    x1, y1, e1 = reliability(c_cal, correct)
    x2, y2, e2 = reliability(c_over, correct)
    axl.plot(x1, y1, "-o", color=BLUE, zorder=3)
    axl.plot(x2, y2, "-o", color=ORANGE, zorder=3)
    axl.set_xlim(0.0, 1.0); axl.set_ylim(0.0, 1.0)
    axl.set_xlabel("Stated confidence"); axl.set_ylabel("Share of claims actually right")
    axl.set_title("Calibration: does 90% mean 90%?")
    axl.text(0.17, 0.66, "Calibrated reader\nECE = %.3f" % e1, fontsize=8, color=INK_2, ha="left", va="center")
    axl.plot([0.13], [0.66], "o", color=BLUE, markersize=4)
    axl.text(0.52, 0.12, "Overconfident reader\nECE = %.3f" % e2, fontsize=8, color=INK_2, ha="left", va="center")
    axl.plot([0.48], [0.12], "o", color=ORANGE, markersize=4)

    # right: risk-coverage
    cov, r_cal = risk_coverage(c_cal, correct)
    _, r_over = risk_coverage(c_over, correct)
    _, r_flat = risk_coverage(c_flat, correct)
    m = cov >= 0.02
    axr.plot(cov[m], r_cal[m], color=BLUE, lw=2.6, zorder=2)
    axr.plot(cov[m], r_over[m], color=ORANGE, lw=1.4, linestyle=(0, (4, 3)), zorder=3)
    axr.plot(cov[m], r_flat[m], color=AQUA)
    axr.set_xlim(0, 1.0); axr.set_ylim(0, 0.34)
    axr.set_xlabel("Coverage (share of claims answered)"); axr.set_ylabel("Error rate on answered claims")
    axr.set_title("Power: does abstaining help?")
    aurc = lambda r: float(r.mean())
    i40 = int(np.searchsorted(cov, 0.40))
    i80 = int(np.searchsorted(cov, 0.78))
    axr.annotate("Calibrated and overconfident:\nsame ranking, same curve\n(AURC %.3f)" % aurc(r_cal),
                 (0.40, r_cal[i40]), xytext=(0.34, 0.02), textcoords="data",
                 fontsize=8, color=INK_2, ha="left", va="bottom",
                 arrowprops=dict(arrowstyle="-", color=NEUTRAL, lw=0.8, shrinkA=2, shrinkB=3))
    axr.annotate("Confidence shuffled:\nno power (AURC %.3f)" % aurc(r_flat),
                 (0.78, r_flat[i80]), xytext=(0.40, 0.295), textcoords="data",
                 fontsize=8, color=INK_2, ha="left", va="center",
                 arrowprops=dict(arrowstyle="-", color=NEUTRAL, lw=0.8, shrinkA=2, shrinkB=3))
    axr.plot([0.78], [r_flat[i80]], "o", color=AQUA, markersize=4, zorder=5)
    axr.plot([0.40], [r_cal[i40]], "o", color=BLUE, markersize=4, zorder=5)
    return finish(fig, "ch26_calibration_power")


# --------------------------------------------------------------------------------------------------
# Figure 3: the abstention threshold
# --------------------------------------------------------------------------------------------------
def coverage_at(pstar):
    """Share of questions whose true probability exceeds p* (p_true = logistic(N(1.4, 0.9^2)))."""
    if pstar <= 0:
        return 1.0
    return float(1 - norm.cdf((np.log(pstar / (1 - pstar)) - 1.4) / 0.9))


def fig_abstention_threshold():
    from matplotlib.lines import Line2D
    fig, (axl, axr) = new_figure("wide", ncols=2)

    # left: expected cost per claim of answering vs abstaining, C_abs = 1
    p = np.linspace(0.6, 1.0, 200)
    c_abs = 1.0
    for c_fp, col in [(20.0, BLUE), (5.0, ORANGE)]:
        axl.plot(p, (1 - p) * c_fp, color=col)
        ps = 1 - c_abs / c_fp
        axl.plot([ps], [c_abs], "o", color=col, markersize=5.5, zorder=5)
        axl.plot([ps, ps], [0, c_abs], color=col, lw=0.9, linestyle=(0, (2, 2)), zorder=1)
    axl.axhline(c_abs, color=NEUTRAL, lw=1.2, zorder=1)
    axl.set_xlim(0.6, 1.0); axl.set_ylim(0, 8.2)
    axl.set_xlabel("Calibrated probability the claim is right, $p$")
    axl.set_ylabel("Expected cost (analyst checks)")
    axl.set_title("Answer vs abstain: expected cost")
    axl.legend(handles=[Line2D([], [], color=BLUE, lw=LW, label="Answer; a wrong claim costs 20 checks"),
                        Line2D([], [], color=ORANGE, lw=LW, label="Answer; a wrong claim costs 5 checks"),
                        Line2D([], [], color=NEUTRAL, lw=1.2, label="Abstain: one check")],
               loc="upper right", fontsize=7.6, handlelength=1.6, borderaxespad=0.2)
    axl.text(0.80, 1.75, "$p^* = 0.80$", fontsize=8, color=INK_2, ha="center", va="center")
    axl.text(0.952, 2.0, "$p^* = 0.95$", fontsize=8, color=INK_2, ha="center", va="center")

    # right: p* and the share of claims a calibrated reader can answer
    r = np.logspace(0, np.log10(200), 300)
    pstar = np.maximum(0.0, 1 - 1 / r)
    cover = np.array([coverage_at(x) for x in pstar])
    axr.plot(r, pstar, color=BLUE)
    axr.plot(r, cover, color=ORANGE)
    axr.set_xscale("log")
    axr.set_xlim(1, 200); axr.set_ylim(0, 1.1)
    axr.set_yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
    axr.set_xticks([1, 2, 5, 10, 20, 50, 100, 200])
    axr.set_xticklabels(["1", "2", "5", "10", "20", "50", "100", "200"])
    axr.minorticks_off()
    axr.set_xlabel(r"Cost ratio $C_{FP}/C_{abs}$")
    axr.set_ylabel("Probability / share of claims")
    axr.set_title("Stakes raise the bar")
    for rr in (5, 20):
        ps = 1 - 1 / rr
        cv = coverage_at(ps)
        axr.plot([rr], [ps], "o", color=BLUE, markersize=5.5, zorder=5)
        axr.plot([rr], [cv], "o", color=ORANGE, markersize=5.5, zorder=5)
        axr.plot([rr, rr], [cv, ps], color=NEUTRAL, lw=0.8, linestyle=(0, (2, 2)), zorder=1)
    axr.text(5.6, 0.66, "%.0f%% answered" % (100 * coverage_at(0.8)), fontsize=8, color=INK_2, ha="left", va="center")
    axr.text(22.0, 0.30, "%.0f%% answered" % (100 * coverage_at(0.95)), fontsize=8, color=INK_2, ha="left", va="center")
    axr.text(5.0, 0.93, "$p^* = 0.80$", fontsize=8, color=INK_2, ha="center", va="center")
    axr.text(20.0, 1.045, "$p^* = 0.95$", fontsize=8, color=INK_2, ha="center", va="center")
    label_end(axr, 100, float(1 - 1 / 100), "Threshold $p^*$", BLUE, dx=-6, dy=-13, ha="center")
    label_end(axr, 1.0, 1.0, "Share answered", ORANGE, dx=6, dy=9)
    return finish(fig, "ch26_abstention_threshold")


# --------------------------------------------------------------------------------------------------
# Figure 4: reliability multiplies
# --------------------------------------------------------------------------------------------------
def fig_chain_reliability():
    fig, (axl, axr) = new_figure("wide", ncols=2)

    n = np.arange(1, 21)
    shades = [SEQ_BLUE(0.55), SEQ_BLUE(0.78), SEQ_BLUE(1.0)]
    for pj, col in zip([0.99, 0.95, 0.90], shades):
        axl.plot(n, pj ** n, color=col)
        label_end(axl, 20, pj ** 20, "$p$ = %.2f" % pj, col, dx=5)
        axl.plot([10], [pj ** 10], "o", color=col, markersize=5, zorder=5)
    mark_event(axl, 10, "n = 10", y_frac=0.985)
    axl.annotate("0.90", (10, 0.99 ** 10), xytext=(10.8, 0.945), fontsize=8, color=INK_2, va="center")
    axl.annotate("0.60", (10, 0.95 ** 10), xytext=(10.8, 0.64), fontsize=8, color=INK_2, va="center")
    axl.annotate("0.35", (10, 0.90 ** 10), xytext=(10.8, 0.385), fontsize=8, color=INK_2, va="center")
    axl.set_xlim(1, 20); axl.set_ylim(0, 1.04)
    axl.set_xticks([1, 5, 10, 15, 20])
    axl.set_xlabel("Steps in the chain, $n$"); axl.set_ylabel("Probability the chain succeeds")
    axl.set_title("Reliability multiplies")
    axl.margins(x=0.0)

    k = np.arange(1, 11)
    p = 0.7
    at_k = 1 - (1 - p) ** k
    hat_k = p ** k
    axr.plot(k, at_k, color=BLUE)
    axr.plot(k, hat_k, color=ORANGE)
    label_end(axr, 10, at_k[-1], "pass@$k$", BLUE, dx=5)
    label_end(axr, 10, hat_k[-1], "pass$^k$", ORANGE, dx=5)
    axr.plot([5, 5], [hat_k[4], at_k[4]], color=NEUTRAL, lw=1.0, zorder=1)
    axr.plot([5], [at_k[4]], "o", color=BLUE, markersize=5, zorder=5)
    axr.plot([5], [hat_k[4]], "o", color=ORANGE, markersize=5, zorder=5)
    axr.annotate("0.998: at least one of 5 works\n(the demo)", (5, at_k[4]), xytext=(5.3, 0.89), fontsize=8,
                 color=INK_2, va="center")
    axr.annotate("0.168: all 5 work\n(what you can size off)", (5, hat_k[4]), xytext=(5.4, 0.36), fontsize=8,
                 color=INK_2, va="center")
    axr.set_xlim(1, 10); axr.set_ylim(0, 1.04)
    axr.set_xticks(list(range(1, 11)))
    axr.set_xlabel("Attempts, $k$ (per-attempt success $p$ = 0.7)")
    axr.set_ylabel("Probability")
    axr.set_title("The demo and the desk")
    axr.margins(x=0.0)
    return finish(fig, "ch26_chain_reliability")


# --------------------------------------------------------------------------------------------------
# Figure 5: the luck hurdle
# --------------------------------------------------------------------------------------------------
def fig_luck_hurdle():
    from matplotlib.lines import Line2D
    gamma_e = 0.5772156649015329
    sd = 0.5

    def hurdle(N):
        N = np.asarray(N, float)
        return sd * ((1 - gamma_e) * norm.ppf(1 - 1 / N) + gamma_e * norm.ppf(1 - 1 / (N * np.e)))

    fig, ax = new_figure("wide")
    N = np.logspace(np.log10(2), 4, 300)
    ax.plot(N, hurdle(N), color=BLUE, zorder=3)

    rng = np.random.default_rng(SEED)
    grid = np.array([2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000])
    sims = []
    for n in grid:
        reps = 4000 if n <= 1000 else 1500
        draws = rng.normal(0.0, sd, size=(reps, n))
        sims.append(draws.max(axis=1).mean())
    ax.plot(grid, sims, "o", color=ORANGE, markersize=5, zorder=4, linestyle="none", clip_on=False)

    for n, txt, xy_text, ha in [(20, "A human tries 20 variants:\nluck hurdle 0.95", (3.0, 1.55), "left"),
                                (2000, "An agent tries 2,000 overnight:\nluck hurdle 1.72", (1300.0, 2.03), "right")]:
        h = float(hurdle(n))
        ax.plot([n, n], [0, h], color=NEUTRAL, lw=0.9, linestyle=(0, (3, 3)), zorder=1)
        ax.plot([n], [h], "o", color=BLUE, markersize=8, markerfacecolor="white", markeredgewidth=1.6, zorder=6)
        ax.annotate(txt, (n, h), xytext=xy_text, textcoords="data", fontsize=8, color=INK_2, ha=ha, va="center",
                    arrowprops=dict(arrowstyle="-", color=NEUTRAL, lw=0.8, shrinkA=2, shrinkB=6))
    ax.set_xscale("log")
    ax.set_xlim(2, 10000); ax.set_ylim(0, 2.2)
    ax.set_xticks([2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000])
    ax.set_xticklabels(["2", "5", "10", "20", "50", "100", "200", "500", "1k", "2k", "5k", "10k"])
    ax.minorticks_off()
    ax.set_xlabel("Trials tried, $N$ (including the ones the agent discarded)")
    ax.set_ylabel("Expected best Sharpe ratio\nunder zero true alpha")
    ax.legend(handles=[Line2D([], [], color=BLUE, lw=LW, label=r"Formula of §26.7, $\sigma_{SR}$ = 0.5"),
                       Line2D([], [], color=ORANGE, marker="o", markersize=5, linestyle="none",
                              label="Simulated: mean best of $N$ draws")],
              loc="lower right", fontsize=8, borderaxespad=0.3)
    return finish(fig, "ch26_luck_hurdle")


if __name__ == "__main__":
    fig_citation_contract()
    fig_calibration_power()
    fig_abstention_threshold()
    fig_chain_reliability()
    fig_luck_hurdle()
