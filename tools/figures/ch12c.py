"""Figures for Chapter 12-C (Plan Value Is a Negotiated Random Variable).

Run:  python3 tools/figures/ch12c.py   -> assets/figures/ch12c_*.png

Every figure here is Illustrative: Halvorsen Packaging is fictional and every number is the chapter's own
(12-B section 12B.9 for the structure; 12C.1, 12C.2 and 12C.10 for the plan-value mixture and the class
formulas). No external data series are used.

Model (the chapter's, restated once so each figure draws from the same functions):
  plan value V ~ 0.7 LN(median 1,300, sigma 0.10) + 0.3 LN(median 1,900, sigma 0.12)   [$mm]
  silos: ABL collateral 250, then V - 250 split 32:3 between term collateral and unencumbered value
  ABL 150, DIP 300 (new money M = 150 plus a 1:1 roll-up), administrative claims 75, first lien left behind
  1,250, unsecured pool 1,020, a 20 settlement from the first lien to the administrative class.

Colour use in this chapter: BLUE is the first lien (the senior, fulcrum-most class) and ORANGE is the unsecured
pool in every figure that shows both; grey is everything that is not one of the two. In the figures that compare
a baseline with a variant, grey is the baseline. Aqua, yellow and magenta are not used.
"""
import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from style import *  # noqa: E402,F401,F403  (applies the rcParams on import)

import numpy as np  # noqa: E402
from scipy.stats import norm  # noqa: E402
from matplotlib.patches import Patch  # noqa: E402

# --------------------------------------------------------------------------------------------------
# The chapter's model
# --------------------------------------------------------------------------------------------------
W_DEBTOR = 0.7
M1, S1 = 1300.0, 0.10      # debtor's expert: median and log-vol of plan value
M2, S2 = 1900.0, 0.12      # committee's expert
ABL, DIP_NEW, ADMIN, FL_LEFT, UNSEC = 150.0, 150.0, 75.0, 1250.0, 1020.0
VSTAR = 250.0 + (1320.0 + DIP_NEW) * 35.0 / 32.0       # first lien whole: 1,857.8
VTOP = 2645.0 + DIP_NEW                                 # unsecured pool whole: 2,795
LIGHT = "#dcdbd6"          # very light grey for the residual (old equity) band
TINT_ALPHA = 0.35


def mix_cdf(x, w=W_DEBTOR):
    x = np.asarray(x, dtype=float)
    return (w * norm.cdf((np.log(x) - np.log(M1)) / S1) + (1 - w) * norm.cdf((np.log(x) - np.log(M2)) / S2))


def comp_pdf(x, m, s):
    x = np.asarray(x, dtype=float)
    return norm.pdf((np.log(x) - np.log(m)) / s) / (x * s)


def mix_pdf(x, w=W_DEBTOR):
    return w * comp_pdf(x, M1, S1) + (1 - w) * comp_pdf(x, M2, S2)


def alloc(V):
    """Dollars paid to each class at plan value V (the chapter's silo waterfall, 12B.9 and 12C.10). Sums to V."""
    V = np.asarray(V, dtype=float)
    T = (32 / 35) * np.clip(V - 250, 0, None)          # term-loan collateral
    U = (3 / 35) * np.clip(V - 250, 0, None)           # unencumbered value
    abl = np.minimum(V, ABL)
    resid = np.clip(np.minimum(V, 250) - ABL, 0, 100)  # ABL collateral surplus, to the DIP
    dip = resid + np.minimum(T, 200)
    settle = np.clip(T - 200, 0, 20)
    first = np.clip(T - 220, 0, FL_LEFT)
    admin = np.minimum(U, 55) + settle
    unsec = np.minimum(np.clip(U - 55, 0, None) + np.clip(T - 1470, 0, None), UNSEC)
    equity = np.clip(V - VTOP, 0, None)
    return dict(abl=abl, dip=dip, admin=admin, first=first, unsec=unsec, equity=equity)


def r_first(V): return alloc(V)["first"] / FL_LEFT
def r_unsec(V): return alloc(V)["unsec"] / UNSEC


def expected_recovery(fn, m, s):
    z = np.linspace(-7, 7, 200001)
    return float((fn(m * np.exp(s * z)) * norm.pdf(z)).sum() * (z[1] - z[0]))


def fulcrum_probs(new_money):
    """P(first lien is the fulcrum), P(unsecured is), P(old equity is), with DIP new money M and any roll-up ratio."""
    v_star = 250.0 + (1320.0 + new_money) * 35.0 / 32.0
    v_top = 2645.0 + new_money
    p_fl = float(mix_cdf(v_star))
    p_un = float(mix_cdf(v_top) - mix_cdf(v_star))
    return p_fl, p_un, 1.0 - p_fl - p_un


def check_model():
    """The chapter's printed numbers, recomputed. A mismatch stops the script."""
    p_fl, p_un, p_eq = fulcrum_probs(150)
    assert abs(p_fl - 0.828) < 0.001 and abs(p_un - 0.172) < 0.001, (p_fl, p_un)
    assert abs(r_first(1300.0) - 0.592) < 0.001 and abs(r_unsec(1300.0) - 0.0343) < 0.0005
    assert abs(VSTAR - 1857.8) < 0.1
    ef = [expected_recovery(r_first, M1, S1), expected_recovery(r_first, M2, S2)]
    eu = [expected_recovery(r_unsec, M1, S1), expected_recovery(r_unsec, M2, S2)]
    assert abs(ef[0] - 0.597) < 0.001 and abs(ef[1] - 0.952) < 0.001
    assert abs(eu[0] - 0.035) < 0.001 and abs(eu[1] - 0.194) < 0.001
    assert abs(W_DEBTOR * ef[0] + (1 - W_DEBTOR) * ef[1] - 0.703) < 0.001
    assert abs(W_DEBTOR * eu[0] + (1 - W_DEBTOR) * eu[1] - 0.083) < 0.001
    # roll-up arithmetic of 12C.4
    F, Wv, M = 1400.0, 910.0, 150.0
    assert abs(M * (F - Wv) / (F * (F - M)) - 0.042) < 0.0005
    assert abs(300 * (F - Wv) / (F * (F - 300)) - 0.0955) < 0.0005
    # take-back of 12C.5
    a5 = (1 - 1.10 ** -5) / 0.10
    assert abs(350 * 0.02 * a5 - 26.5) < 0.05 and abs(350 * 0.01 * a5 - 13.3) < 0.05


# --------------------------------------------------------------------------------------------------
# Figure 12-C.1 (section 12C.2): the waterfall as stacked call spreads, with the mixture and fulcrum probabilities
# --------------------------------------------------------------------------------------------------
def fig_call_spreads():
    fig, (ax1, ax2) = new_figure((7.0, 6.0), nrows=2, sharex=True, gridspec_kw=dict(height_ratios=[1.6, 1]))
    v = np.linspace(300, 3400, 1551)
    a = alloc(v)
    prior = a["abl"] + a["dip"] + a["admin"]
    bands = [prior, a["first"], a["unsec"], a["equity"]]
    cols = [NEUTRAL, BLUE, ORANGE, LIGHT]
    ax1.stackplot(v, *bands, colors=cols, edgecolor=SURFACE, linewidth=0.6)
    ax1.set_axisbelow(True)
    ax1.set_ylim(0, 3400)
    ax1.set_xlim(300, 3400)
    ax1.set_ylabel(r"Dollars paid to the class (\$mm)")
    for x0 in (VSTAR, VTOP):
        ax1.axvline(x0, color=INK_2, linewidth=0.9, linestyle=(0, (3, 3)), zorder=4)
    ax1.annotate("first lien whole\nV = 1,858", (VSTAR, 3150), xytext=(-5, 0), textcoords="offset points",
                 ha="right", va="top", fontsize=8, color=INK_2)
    ax1.annotate("unsecured pool whole\nV = 2,795", (VTOP, 3150), xytext=(-5, 0), textcoords="offset points",
                 ha="right", va="top", fontsize=8, color=INK_2)
    # direct labels inside the bands, at x = 3,000 where every band has height
    stack_at = lambda x: [float(b[np.argmin(abs(v - x))]) for b in bands]
    names = ["ABL, DIP, admin (525)", "First lien (1,250)", "Unsecured pool (1,020)", "Old equity"]
    xls = [3000, 3000, 3000, 3200]
    for k, (name, xl) in enumerate(zip(names, xls)):
        h = stack_at(xl)
        lo = sum(h[:k])
        ax1.annotate(name, (xl, lo + (h[k] / 2 if k < 3 else 0.4 * h[k])), ha="center", va="center", fontsize=8.5 if k < 3 else 8,
                     color=INK if k < 3 else INK_2)
    ax1.text(310, 2600, "Each band's thickness is one class's call spread:\nzero below its attachment point, a ramp,\nthen flat at its claim above its detachment point.",
             fontsize=8, color=MUTED, va="top", ha="left")

    # bottom panel: the mixture density with fulcrum probabilities shaded
    d = mix_pdf(v)
    p_fl, p_un, p_eq = fulcrum_probs(150)
    ax2.plot(v, d, color=INK_2, linewidth=LW, zorder=3)
    m_fl = v <= VSTAR
    m_un = (v >= VSTAR) & (v <= VTOP)
    ax2.fill_between(v, 0, d, where=m_fl, color=BLUE, alpha=0.45, linewidth=0)
    ax2.fill_between(v, 0, d, where=m_un, color=ORANGE, alpha=0.55, linewidth=0)
    for x0 in (VSTAR, VTOP):
        ax2.axvline(x0, color=INK_2, linewidth=0.9, linestyle=(0, (3, 3)), zorder=4)
    ax2.set_yticks([])
    ax2.set_ylabel("Density of plan value")
    ax2.grid(False)
    ax2.set_xlabel(r"Confirmed plan value $V$ (\$mm)")
    ym = d.max()
    ax2.annotate("debtor's expert\n1,300 (weight 0.7)", (1150, 0.92 * ym), ha="right", va="center", fontsize=8,
                 color=INK_2)
    ax2.annotate(f"{p_fl * 100:.1f}%: the first lien\nis the fulcrum", (1120, 0.52 * ym), ha="right", va="center",
                 fontsize=8.5, color=INK)
    ax2.annotate("committee's expert\n1,900 (weight 0.3)", (1960, 0.56 * ym), ha="left", va="center", fontsize=8,
                 color=INK_2)
    ax2.annotate(f"{p_un * 100:.1f}%: the unsecured\npool is the fulcrum", (1960, 0.37 * ym), ha="left", va="center",
                 fontsize=8.5, color=INK)
    return finish(fig, "ch12c_call_spreads")


# --------------------------------------------------------------------------------------------------
# Figure 12-C.2 (section 12C.4): the roll-up as a transfer inside the tranche
# --------------------------------------------------------------------------------------------------
def fig_rollup_transfer():
    F, Wv = 1400.0, 910.0
    fig, (axl, axr) = new_figure("wide", ncols=2, gridspec_kw=dict(width_ratios=[1, 1.25]))

    # left: recovery by holder, before and after the 1:1 roll-up
    base = Wv / F * 100                          # 65.0
    after_left = (Wv - 150) / (F - 150) * 100    # 60.8
    xs = np.array([0.0, 1.0])
    bw = 0.34
    xa, xb = xs - bw / 2 - 0.01, xs + bw / 2 + 0.01
    axl.bar(xa, [base, base], width=bw, color=NEUTRAL, label="No roll-up")
    axl.bar(xb, [100.0, after_left], width=bw, color=BLUE, label="With 1:1 roll-up")
    for x, val in zip(np.concatenate([xa, xb]), [base, base, 100.0, after_left]):
        axl.annotate(f"{val:.1f}", (x, val), xytext=(0, 3), textcoords="offset points", ha="center", va="bottom",
                     fontsize=8.5, color=INK_2)
    axl.set_xticks(xs)
    axl.set_xticklabels(["Rolled paper\n(150 of face)", "Left behind\n(1,250 of face)"])
    axl.set_ylim(0, 132)
    axl.set_yticks([0, 25, 50, 75, 100])
    axl.set_ylabel("Recovery (% of face)")
    axl.legend(loc="upper center", ncols=2, bbox_to_anchor=(0.5, 1.03), handlelength=1.2, columnspacing=1.0,
               fontsize=8)
    axl.annotate("gains \\$52.5mm", (xb[0], 100), xytext=(0, 17), textcoords="offset points", ha="center",
                 fontsize=8, color=INK_2)
    axl.annotate("lose \\$52.5mm in all\n(4.2 pts × 1,250)", (xs[1], base), xytext=(0, 15),
                 textcoords="offset points", ha="center", va="bottom", fontsize=8, color=INK_2)

    # right: recovery of the non-participants against the size of the roll-up
    x = np.linspace(0, Wv - 1, 600)
    rec = (Wv - x) / (F - x) * 100
    axr.axhline(base, color=NEUTRAL, linewidth=LW)
    axr.fill_between(x, rec, base, color=BLUE, alpha=TINT_ALPHA, linewidth=0)
    axr.plot(x, rec, color=BLUE, linewidth=LW)
    spots = ((150, "1:1 roll-up (150)", (30, 44)), (300, "2:1 roll-up (300)", (345, 20)))
    for xm, name, (tx, ty) in spots:
        yv = (Wv - xm) / (F - xm) * 100
        axr.plot([xm], [yv], "o", color=BLUE, markersize=5.5, zorder=5)
        axr.annotate(f"{name}:\n{yv:.1f}% ({yv - base:+.1f} pts)".replace("(-", "(−"), (xm, yv), xytext=(tx, ty),
                     textcoords="data", ha="left", va="center", fontsize=8, color=INK,
                     arrowprops=dict(arrowstyle="-", color=INK_2, lw=0.7, shrinkA=2, shrinkB=3))
    axr.axvline(Wv, color=INK_2, linewidth=0.9, linestyle=(0, (3, 3)))
    axr.annotate("roll-up = W = 910:\nformula refused", (Wv, 42), xytext=(-5, 0), textcoords="offset points",
                 ha="right", va="center", fontsize=8, color=INK_2)
    axr.annotate("no roll-up: 65.0%", (0, base), xytext=(4, 4), textcoords="offset points", ha="left", va="bottom",
                 fontsize=8, color=INK_2)
    axr.annotate("shaded gap =\nloss per 100 of\nface left behind", (640, 57), ha="center", va="center", fontsize=8,
                 color=INK_2)
    axr.set_xlim(0, 960)
    axr.set_ylim(0, 75)
    axr.set_xlabel(r"Prepetition paper rolled up, $\kappa M$ (\$mm)")
    axr.set_ylabel("Left-behind recovery (% of face)")
    note(axr, "tranche face 1,400; value W = 910", loc="lower left")
    return finish(fig, "ch12c_rollup_transfer")


# --------------------------------------------------------------------------------------------------
# Figure 12-C.3 (section 12C.10): recovery distributions by class under the mixture
# --------------------------------------------------------------------------------------------------
def _recovery_bins(fn, edges, vgrid):
    """Probability that recovery lands in each [edge_k, edge_k+1), by expert component (unweighted by w)."""
    r = fn(vgrid)
    out = []
    for m, s in ((M1, S1), (M2, S2)):
        cdf = norm.cdf((np.log(vgrid) - np.log(m)) / s)
        idx = np.clip(np.searchsorted(r, edges, side="left"), 0, len(vgrid) - 1)   # smallest V reaching each level
        c = cdf[idx]
        c[edges <= r[0]] = 0.0
        out.append(np.diff(c))
    return out


def fig_recovery_distributions():
    fig, (axa, axb) = new_figure("wide", ncols=2)
    vgrid = np.exp(np.linspace(np.log(300), np.log(6000), 400001))
    w2 = 1 - W_DEBTOR
    mean = lambda fn: W_DEBTOR * expected_recovery(fn, M1, S1) + w2 * expected_recovery(fn, M2, S2)

    # first lien: linear axis, 2.5-point bins, plus the point mass at par
    bw = 2.5
    pct = np.arange(0, 100 + 1e-9, bw)
    d, c = _recovery_bins(r_first, pct / 100.0, vgrid)
    mids, wd = pct[:-1] + bw / 2, bw * 0.9
    axa.bar(mids, W_DEBTOR * d * 100, width=wd, color=BLUE, label="Debtor's expert (0.7)")
    axa.bar(mids, w2 * c * 100, width=wd, bottom=W_DEBTOR * d * 100, color=BLUE, alpha=0.38,
            label="Committee's expert (0.3)")
    p_par = 1 - float(mix_cdf(VSTAR))
    axa.bar([100.9], [p_par * 100], width=1.6, color=BLUE, alpha=0.38, zorder=3)   # point mass at par, beside the last bin
    axa.annotate(f"{p_par * 100:.1f}%\npaid in full", (100.9, p_par * 100), xytext=(-5, -2), textcoords="offset points",
                 ha="right", va="top", fontsize=8.5, color=INK)
    axa.set_xlim(0, 103)
    axa.set_ylim(0, 22)
    axa.set_title("First lien (left behind)")
    axa.set_xlabel("Recovery (% of allowed claim)")
    axa.set_ylabel("Probability per 2.5-point bin (%)")
    axa.axvline(mean(r_first) * 100, color=INK_2, linewidth=0.9, linestyle=(0, (3, 3)), zorder=4)
    axa.annotate(f"mean {mean(r_first) * 100:.1f}", (mean(r_first) * 100, 0.62), xycoords=("data", "axes fraction"),
                 xytext=(-4, 0), textcoords="offset points", ha="right", va="center", fontsize=8, color=INK_2)
    axa.legend(loc="upper left", fontsize=8, handlelength=1.2)

    # unsecured pool: log axis so the hump near 3 and the tail to 100 share one picture
    edges_pct = np.logspace(np.log10(0.5), 2.0, 38)
    d, c = _recovery_bins(r_unsec, edges_pct / 100.0, vgrid)
    lefts, widths = edges_pct[:-1], np.diff(edges_pct)
    axb.bar(lefts, W_DEBTOR * d * 100, width=widths * 0.92, align="edge", color=ORANGE)
    axb.bar(lefts, w2 * c * 100, width=widths * 0.92, align="edge", bottom=W_DEBTOR * d * 100, color=ORANGE, alpha=0.38)
    axb.set_xscale("log")
    axb.set_xlim(0.5, 100)
    axb.set_xticks([1, 2, 5, 10, 20, 50, 100])
    axb.set_xticklabels(["1", "2", "5", "10", "20", "50", "100"])
    axb.minorticks_off()
    axb.set_title("Unsecured pool")
    axb.set_xlabel("Recovery (% of allowed claim, log scale)")
    axb.set_ylabel("Probability per bin (%)")
    mu = mean(r_unsec) * 100
    axb.axvline(mu, color=INK_2, linewidth=0.9, linestyle=(0, (3, 3)), zorder=4)
    axb.annotate(f"mean {mu:.1f}", (mu, 0.80), xycoords=("data", "axes fraction"), xytext=(5, 0),
                 textcoords="offset points", ha="left", va="center", fontsize=8, color=INK_2)
    axb.annotate("tail: almost all\ncommittee's expert", (22, 0.30), xycoords=("data", "axes fraction"),
                 ha="left", va="center", fontsize=8, color=INK_2)
    axb.text(0.99, 0.97, "37 bins, equal in\nlog recovery", transform=axb.transAxes, ha="right", va="top",
             fontsize=8, color=MUTED)
    axb.legend(handles=[Patch(facecolor=ORANGE, label="Debtor's"),
                        Patch(facecolor=ORANGE, alpha=0.38, label="Committee's")],
               title="Expert adopted", title_fontsize=8, alignment="left",
               loc="center right", bbox_to_anchor=(1.0, 0.57), fontsize=8, handlelength=1.2)
    return finish(fig, "ch12c_recovery_distributions")


# --------------------------------------------------------------------------------------------------
# Figure 12-C.4 (section 12C.10): fulcrum probability against DIP new money
# --------------------------------------------------------------------------------------------------
def fig_fulcrum_prob_vs_dip():
    fig, ax = new_figure("wide")
    m = np.linspace(0, 400, 401)
    pf = np.array([fulcrum_probs(x)[0] for x in m]) * 100
    pu = np.array([fulcrum_probs(x)[1] for x in m]) * 100
    ax.plot(m, pf, color=BLUE, linewidth=LW)
    ax.plot(m, pu, color=ORANGE, linewidth=LW)
    ax.set_xlim(0, 400)
    ax.set_ylim(0, 100)
    ax.set_xlabel(r"DIP new money $M$ (\$mm)")
    ax.set_ylabel("Fulcrum probability (%)")
    label_end(ax, m[-1], pf[-1], "First lien", BLUE, dx=6)
    label_end(ax, m[-1], pu[-1], "Unsecured pool", ORANGE, dx=6)
    for x0 in (0, 150, 280):
        p_f, p_u, _ = fulcrum_probs(x0)
        ax.plot([x0], [p_f * 100], "o", color=BLUE, markersize=5.5, zorder=5, clip_on=False)
        ax.plot([x0], [p_u * 100], "o", color=ORANGE, markersize=5.5, zorder=5, clip_on=False)
        ax.annotate(f"{p_f * 100:.0f}%", (x0, p_f * 100), xytext=(8, 7), textcoords="offset points", ha="left",
                    fontsize=8.5, color=INK_2)
        ax.annotate(f"{p_u * 100:.0f}%", (x0, p_u * 100), xytext=(8, 7), textcoords="offset points", ha="left",
                    fontsize=8.5, color=INK_2)
    mark_event(ax, 150, "actual DIP: 150", y_frac=0.60)
    ax.text(0.99, 0.40, "Roll-up ratio 1:1; the curves are the same for any ratio.\nOld equity's probability stays under 0.1%.",
            transform=ax.transAxes, ha="right", va="center", fontsize=8, color=MUTED)
    return finish(fig, "ch12c_fulcrum_prob_vs_dip")


# --------------------------------------------------------------------------------------------------
# Figure 12-C.5 (section 12C.10): the take-back transfer against the coupon gap
# --------------------------------------------------------------------------------------------------
def fig_takeback_transfer():
    F, c = 350.0, 0.08
    a5 = lambda y: (1 - (1 + y) ** -5) / y
    ds = np.linspace(0.0005, 0.04, 400)                  # coupon gap, decimal
    exact = F * ds * a5(c + ds)                          # plan coupon fixed at 8.0%; the market yield is c + gap
    first = F * a5(0.10) * ds                            # duration (annuity) at the plan's own 10% market yield
    fig, ax = new_figure("wide")
    bp = ds * 1e4
    ax.plot(bp, first, color=MUTED, linewidth=LW, linestyle=(0, (5, 3)))
    ax.plot(bp, exact, color=BLUE, linewidth=LW)
    ax.set_xlim(0, 400)
    ax.set_ylim(0, 58)
    ax.set_xlabel(r"Coupon gap $\Delta s$ = market yield $-$ plan coupon (bp)")
    ax.set_ylabel(r"Transfer to the equity electors (\$mm)")
    label_end(ax, bp[-1], exact[-1], "Exact price", BLUE, dx=6, dy=-3)
    label_end(ax, bp[-1], first[-1], "First order", MUTED, dx=6, dy=3)
    x200, y200 = 200, F * 0.02 * a5(0.10)
    ax.plot([x200], [y200], "o", color=INK, markersize=6.5, zorder=6)
    ax.annotate(f"the plan: 200bp gap, \\${y200:.1f}mm", (x200, y200), xytext=(-12, 10), textcoords="offset points",
                ha="right", va="bottom", fontsize=8.5, color=INK)
    ax.annotate(f"first-order slope: \\${F * a5(0.10) * 0.01:.1f}mm per 100bp", (300, 17), ha="center", va="center",
                fontsize=8.5, color=INK_2)
    note(ax, "Five-year annual-pay note, face \\$350mm, plan coupon 8.0%.\nFirst-order line: face × duration 3.79 (annuity at 10%) × gap.",
         loc="upper left")
    return finish(fig, "ch12c_takeback_transfer")


if __name__ == "__main__":
    check_model()
    fig_call_spreads()
    fig_rollup_transfer()
    fig_recovery_distributions()
    fig_fulcrum_prob_vs_dip()
    fig_takeback_transfer()
