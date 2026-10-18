"""Chapter 13 figures (Codifying Liability Management Transactions).

Every figure here is Illustrative: it evaluates the chapter's own formulas (Sections 13.3-13.7) at
parameters the chapter states (Serta Simmons deal terms from the Fifth Circuit opinion; the Listing 13.2
nine-holder register; the Section 13.7 double-dip example). No market data series is used.

Role colors, fixed across the chapter: BLUE = the existing / excluded lender who loses (also the co-op of
existing lenders in Fig 13.3); ORANGE = the beneficiary (participant, new money, double-dipper, the coalition
the sponsor invites in Fig 13.2); gray = the pre-deal or pro rata baseline. Fig 13.4 compares two transactions
on one axis, so it takes SERIES[0] (uptier) and SERIES[1] (drop-down) in order.
"""
import itertools
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from style import *  # noqa: F401,F403,E402  (applies the rcParams on import)
import numpy as np  # noqa: E402
from matplotlib.patches import FancyBboxPatch  # noqa: E402
from matplotlib.ticker import FuncFormatter  # noqa: E402

usd = FuncFormatter(lambda v, pos: f"{v:,.0f}")


def dot_label(ax, x, y, text, color, dx=6, dy=0, ha="left", va="center", fs=8.5):
    """Direct label with a small colored dot on the mark; the text stays ink."""
    ax.plot([x], [y], "o", color=color, markersize=4, zorder=6, clip_on=False)
    ax.annotate(text, (x, y), xytext=(dx, dy), textcoords="offset points", ha=ha, va=va,
                fontsize=fs, color=INK_2, annotation_clip=False)


# --------------------------------------------------------------------------------------------
# Figure 13.1: the Serta uptier as a recovery transfer (Section 13.3)
# --------------------------------------------------------------------------------------------
def fig_uptier():
    F, N, p = 2400.0, 200.0, 0.5
    x = 875.0 / 1200.0
    K1 = N + x * p * F
    K2 = K1 + (1 - p) * F
    V = np.linspace(0, 2800, 2801)
    fo = np.minimum(V, N)
    so = np.minimum(np.maximum(V - N, 0), x * p * F)
    ex = np.minimum(np.maximum(V - K1, 0), (1 - p) * F)
    assert np.allclose(fo + so + ex, np.minimum(V, K2))          # conservation
    assert all(np.all(np.diff(t) >= -1e-9) for t in (fo, so, ex))  # every tranche is nondecreasing in V
    pre_ex = (1 - p) * F * np.minimum(V, F) / F                  # excluded lenders' dollars with no deal
    loss = 100 * (np.minimum(V, F) / F - ex / ((1 - p) * F))     # priming loss, points of par
    assert abs(loss[int(K1)] - 100 * K1 / F) < 0.05              # 44.8 points at V = K1

    fig, (a, b) = new_figure("wide", ncols=2)
    a.stackplot(V, fo, so, ex, colors=[AQUA, ORANGE, BLUE], edgecolor="white", linewidth=0.6, zorder=2)
    a.plot(V, pre_ex, color=INK_2, linewidth=1.2, linestyle=(0, (4, 3)), zorder=4)
    a.set_xlim(0, 2800)
    a.set_ylim(0, 2500)
    a.set_xlabel("Enterprise value V ($mm)")
    a.set_ylabel("Dollars recovered ($mm)")
    a.xaxis.set_major_formatter(usd)
    a.yaxis.set_major_formatter(usd)
    a.set_xticks([0, 1000, 2000])
    a.set_title("(a) Who gets each dollar")
    # direct labels, right edge, at band mid-heights
    for y, t, c in [(100, "First-out", AQUA), (640, "Second-out", ORANGE), (1680, "Excluded", BLUE)]:
        dot_label(a, 2800, y, t, c, dx=5)
    a.annotate("Dashed: excluded lenders'\nno-deal recovery\n(pro rata)", (700, 350),
               xytext=(90, 1780), fontsize=8, color=INK_2, ha="left", va="center",
               arrowprops=dict(arrowstyle="-", color=INK_2, lw=0.7), zorder=7)

    b.plot(V, loss, color=BLUE, zorder=3)
    b.fill_between(V, 0, loss, where=loss >= 0, color=BLUE, alpha=0.12, linewidth=0)
    b.axhline(0, color=NEUTRAL, linewidth=0.8, zorder=1)
    b.set_xlim(0, 2800)
    b.set_ylim(-10, 52)
    b.set_xlabel("Enterprise value V ($mm)")
    b.set_ylabel("Excluded lender's loss (points of par)")
    b.xaxis.set_major_formatter(usd)
    b.set_xticks([0, 1000, 2000])
    b.set_title("(b) The excluded lender\u2019s loss")
    mark_event(b, K1, "K₁ = 1,075", y_frac=0.995)
    mark_event(b, K2, "K₂", y_frac=0.995)
    b.annotate("44.8 points: the whole\npre-deal recovery", (K1, 44.8), xytext=(1330, 37),
               fontsize=8, color=INK_2, ha="left", va="center",
               arrowprops=dict(arrowstyle="-", color=INK_2, lw=0.7))
    return finish(fig, "ch13_serta_uptier_waterfall")


# --------------------------------------------------------------------------------------------
# Figure 13.2: the sponsor's knapsack (Section 13.4), Listing 13.2 register
# --------------------------------------------------------------------------------------------
def min_cost_coalition(w, c, theta, eps=0.01, coop=()):
    cand = [i for i in range(len(w)) if i not in set(coop)]
    if w[cand].sum() < theta + eps:
        return None
    feas = (list(S) for k in range(1, len(cand) + 1) for S in itertools.combinations(cand, k)
            if w[list(S)].sum() >= theta + eps)
    return min(feas, key=lambda S: float(c[S] @ w[S]))


def fig_knapsack():
    w = np.array([0.22, 0.18, 0.15, 0.12, 0.10, 0.08, 0.06, 0.05, 0.04])
    c = np.array([0.02, 0.08, 0.03, 0.08, 0.15, 0.03, 0.08, 0.02, 0.08])
    kind = ["Fund", "CLO", "Fund", "CLO", "Litigator", "Fund", "CLO", "Fund", "CLO"]
    S = min_cost_coalition(w, c, theta=0.5)
    assert 4 not in S and abs(w[S].sum() - 0.54) < 1e-9 and len(S) == 5     # matches the chapter text
    # display order = cheapest first, larger holding first; names number within type in that order
    order = sorted(range(len(w)), key=lambda i: (c[i], -w[i]))
    counts, labels = {}, []
    for i in order:
        counts[kind[i]] = counts.get(kind[i], 0) + 1
        labels.append(kind[i] if kind[i] == "Litigator" else f"{kind[i]} {counts[kind[i]]}")
    ypos = np.arange(len(order))[::-1]
    inv = [i in S for i in order]

    fig, (a, b) = new_figure("wide", ncols=2, sharey=True)
    colors = [ORANGE if f else BLUE for f in inv]       # ORANGE = invited (beneficiary), BLUE = left out (excluded)
    a.barh(ypos, [100 * c[i] for i in order], color=colors, height=0.68)
    b.barh(ypos, [100 * w[i] for i in order], color=colors, height=0.68)
    for ax in (a, b):
        ax.grid(False)
        ax.grid(axis="x", color=GRID, linewidth=0.7)
        ax.set_axisbelow(True)
        ax.spines["left"].set_visible(False)
        ax.tick_params(axis="y", length=0)
    a.set_yticks(ypos)
    a.set_yticklabels(labels)
    a.set_xlabel("Concession to bring in, c (cents per $ held)")
    b.set_xlabel("Holding w (% of class)")
    a.set_xlim(0, 17)
    a.set_xticks([0, 5, 10, 15])
    b.set_xlim(0, 26)
    a.set_title("(a) What each holder costs")
    b.set_title("(b) What each holder brings")
    for yy, i in zip(ypos, order):
        a.text(100 * c[i] + 0.3, yy, f"{100 * c[i]:.0f}", va="center", fontsize=8, color=INK_2)
        b.text(100 * w[i] + 0.4, yy, f"{100 * w[i]:.0f}", va="center", fontsize=8, color=INK_2)
    from matplotlib.patches import Patch
    b.legend(handles=[Patch(color=ORANGE, label="Invited coalition (54% of class)"),
                      Patch(color=BLUE, label="Left out (bar to clear: > 50%)")],
             loc="center right", bbox_to_anchor=(1.0, 0.26), fontsize=8, handlelength=1.0)
    return finish(fig, "ch13_sponsor_knapsack")


# --------------------------------------------------------------------------------------------
# Figure 13.3: Nash bargaining and Shapley carve-outs (Section 13.5)
# --------------------------------------------------------------------------------------------
def shapley(w, quota):
    phi, orders = np.zeros(len(w)), list(itertools.permutations(range(len(w))))
    for order in orders:
        acc = 0.0
        for i in order:
            if acc <= quota < acc + w[i]:
                phi[i] += 1.0
                break
            acc += w[i]
    return phi / len(orders)


def fig_coop():
    Pi, dC = 100.0, 20.0
    dsp = np.linspace(0, 80, 81)
    fig, (a, b) = new_figure("wide", ncols=2)
    shades = {0.3: SEQ_BLUE_STEPS[4], 0.5: SEQ_BLUE_STEPS[7], 0.7: SEQ_BLUE_STEPS[11]}
    for eta, col in shades.items():
        PiC = dC + eta * (Pi - dC - dsp)
        a.plot(dsp, PiC, color=col)
        dot_label(a, 0, PiC[0], f"η={eta}", col, dx=-5, dy=0, ha="right", fs=8)
    a.axhline(dC, color=NEUTRAL, linewidth=0.9, linestyle=(0, (4, 3)))
    a.text(1.5, dC - 1.5, "co-op's outside option $d_C$ = 20", ha="left", va="top", fontsize=8, color=INK_2)
    a.axvspan(80, 112, color=GRID, alpha=0.7, linewidth=0)
    a.text(96, 80, "no deal:\noutside\noptions\nexceed\nsurplus", ha="center", va="top", fontsize=8, color=INK_2)
    a.set_xlim(-21, 112)
    a.set_xticks([0, 20, 40, 60, 80, 100])
    a.set_ylim(0, 85)
    a.set_xlabel("Sponsor's outside option $d_{sp}$ (\\$mm)")
    a.set_ylabel("Co-op's payoff $\\Pi_C$ (\\$mm)")
    a.set_title("(a) Each outside dollar costs η")
    a.annotate("slope = −η", (40, dC + 0.5 * 40), xytext=(46, 62), fontsize=8, color=INK_2,
               arrowprops=dict(arrowstyle="-", color=INK_2, lw=0.7))

    w = np.array([0.25, 0.06, 0.03, 0.03])
    phi = shapley(w, 1 / 3)
    assert np.allclose(phi, [5 / 12, 5 / 12, 1 / 12, 1 / 12])
    share = w / w.sum()
    names = ["A", "B", "C", "D"]
    xs = np.arange(4)
    bw = 0.38
    b.bar(xs - bw / 2 - 0.02, 100 * share, width=bw, color=NEUTRAL)
    b.bar(xs + bw / 2 + 0.02, 100 * phi, width=bw, color=BLUE)          # co-op members = existing lenders
    for xi, s, f in zip(xs, share, phi):
        b.text(xi - bw / 2 - 0.02, 100 * s + 1.5, f"{100 * s:.0f}", ha="center", fontsize=8, color=INK_2)
        b.text(xi + bw / 2 + 0.02, 100 * f + 1.5, f"{100 * f:.0f}", ha="center", fontsize=8, color=INK_2)
    b.set_xticks(xs)
    b.set_xticklabels([f"{n}\n{100 * x:.0f}%" for n, x in zip(names, w)])
    b.set_xlabel("Co-op member (holding, % of class)")
    b.set_ylim(0, 85)
    b.set_ylabel("Share of co-op total (%)")
    b.set_title("(b) Veto power vs. loans held")
    from matplotlib.patches import Patch
    b.legend(handles=[Patch(color=NEUTRAL, label="Share of the co-op's loans"),
                      Patch(color=BLUE, label="Shapley value (blocking power)")],
             loc="upper right", fontsize=8, handlelength=1.0)
    return finish(fig, "ch13_coop_bargaining_shapley")


# --------------------------------------------------------------------------------------------
# Figure 13.4: digital put versus forward (Section 13.6)
# --------------------------------------------------------------------------------------------
def fig_payoff_shapes():
    F, N, p = 2400.0, 200.0, 0.5
    x = 875.0 / 1200.0
    K1 = N + x * p * F
    K2 = K1 + (1 - p) * F
    T = 480.0                                                   # J.Crew corner: phi = 0, D_u = T
    V = np.linspace(0, 3000, 3001)
    R0 = np.minimum(V, F) / F
    ex = np.minimum(np.maximum(V - K1, 0), (1 - p) * F) / ((1 - p) * F)
    up = 100 * (R0 - ex)
    dd = 100 * (np.minimum(V, F) - np.minimum(np.maximum(V - T, 0), F)) / F
    assert dd.max() <= 100 * T / F + 1e-9
    fig, ax = new_figure("wide")
    ax.axhline(0, color=NEUTRAL, linewidth=0.8)
    ax.plot(V, up, color=BLUE)
    ax.plot(V, dd, color=ORANGE)
    ax.axhline(100 * T / F, color=NEUTRAL, linewidth=0.9, linestyle=(0, (4, 3)), zorder=1)
    ax.text(2990, 100 * T / F + 1.5, "cap: T/F = 20 points", ha="right", va="bottom", fontsize=8, color=INK_2)
    ax.set_xlim(0, 3000)
    ax.set_ylim(-9, 52)
    ax.set_xlabel("Enterprise value V ($mm)")
    ax.set_ylabel("Existing lender's loss (points of par)")
    ax.xaxis.set_major_formatter(usd)
    mark_event(ax, K1, "K₁", y_frac=0.995)
    mark_event(ax, K2, "K₂", y_frac=0.995)
    dot_label(ax, K1, 44.8, "Uptier (excluded lender):\nloss peaks at K₁, fades by K₂", BLUE, dx=8, dy=6)
    dot_label(ax, 800, 20, "Drop-down (existing lender):\n20 points in almost every state", ORANGE, dx=-4, dy=-18, ha="left")
    return finish(fig, "ch13_digital_put_vs_forward")


# --------------------------------------------------------------------------------------------
# Figure 13.5: double-dip structure and recoveries (Section 13.7)
# --------------------------------------------------------------------------------------------
def box(ax, cx, cy, w, h, text, edge=NEUTRAL, ls="-", fs=8):
    ax.add_patch(FancyBboxPatch((cx - w / 2, cy - h / 2), w, h, boxstyle="round,pad=0,rounding_size=0.2",
                                fc="white", ec=edge, lw=1.4, ls=ls, zorder=3))
    ax.text(cx, cy, text, ha="center", va="center", fontsize=fs, color=INK, zorder=4)


def arrow(ax, p0, p1, rad=0.0, ls="-", color=INK_2):
    ax.annotate("", xy=p1, xytext=p0, zorder=2,
                arrowprops=dict(arrowstyle="-|>", color=color, lw=1.1, shrinkA=0, shrinkB=0, ls=ls,
                                connectionstyle=f"arc3,rad={rad}", mutation_scale=9))


def dd_recoveries(V, F1, F2):
    V = np.asarray(V, dtype=float)
    den = F1 + 2 * F2
    low = V < den / 2
    dd = np.where(low, 2 * V / den, 1.0)
    first = np.where(low, V / den, np.minimum((V - F2) / F1, 1.0))
    return dd, first


def waterfall_clearing(ents, claims, tol=1e-10, max_iter=10_000):
    """Eisenberg-Noe clearing as in Listing 13.1 (Appendix F): used only to cross-check the closed form."""
    pay = {c["id"]: 0.0 for c in claims}
    res = {e: 0.0 for e in ents}
    for _ in range(max_iter):
        avail = {e: float(s["value"]) for e, s in ents.items()}
        for c in claims:
            if c["creditor"] != "ext":
                avail[c["creditor"]] += pay[c["id"]]
        for e, s in ents.items():
            if s["parent"] is not None:
                avail[s["parent"]] += res[e]
        new_pay, new_res = {}, {}
        for e in ents:
            left, mine = avail[e], [c for c in claims if c["debtor"] == e]
            for r in sorted({c["rank"] for c in mine}):
                cls = [c for c in mine if c["rank"] == r]
                owed = [max(c["face"] - sum(pay[k] for k in c.get("reduce_by", ())), 0.0) for c in cls]
                tot = sum(owed)
                frac = 1.0 if tot <= left else left / tot
                for c, o in zip(cls, owed):
                    new_pay[c["id"]] = frac * o
                left = max(left - frac * tot, 0.0)
            new_res[e] = left
        gap = max(max(abs(new_pay[k] - pay[k]) for k in pay), max(abs(new_res[e] - res[e]) for e in ents))
        pay, res = new_pay, new_res
        if gap < tol:
            return pay
    raise RuntimeError("clearing did not converge")


def clearing_check(V, F1, F2):
    ents = {"opco": {"value": V, "parent": None}, "spv": {"value": 0.0, "parent": "opco"}}
    cl = [dict(id="1L", creditor="ext", debtor="opco", face=F1, rank=1),
          dict(id="opco_guar", creditor="ext", debtor="opco", face=F2, rank=1),
          dict(id="interco", creditor="spv", debtor="opco", face=F2, rank=1),
          dict(id="spv_tl", creditor="ext", debtor="spv", face=F2, rank=1, reduce_by=["opco_guar"])]
    pay = waterfall_clearing(ents, cl)
    return (pay["opco_guar"] + pay["spv_tl"]) / F2, pay["1L"] / F1


def fig_double_dip():
    F1, F2 = 1000.0, 500.0
    for v in (200, 600, 800, 1000, 1200, 1400):
        dd, fl = dd_recoveries(v, F1, F2)
        cd, cf = clearing_check(float(v), F1, F2)
        assert abs(dd - cd) < 1e-6 and abs(fl - cf) < 1e-6, (v, dd, cd, fl, cf)
    Vg = np.linspace(0, 1800, 1801)
    ddg, fg = dd_recoveries(Vg, F1, F2)
    assert np.all(np.diff(ddg) >= -1e-12) and np.all(np.diff(fg) >= -1e-12)   # monotone in V
    assert np.all(ddg >= fg - 1e-12) and abs(ddg[1000] - 1.0) < 1e-12 and abs(fg[1500] - 1.0) < 1e-12
    assert np.allclose(F2 * ddg + F1 * fg, np.minimum(Vg, F1 + F2))          # conservation: pays out min(V, F1+F2)
    fig, (a, b) = new_figure((7.2, 3.7), ncols=2, gridspec_kw={"width_ratios": [1.0, 1.1]})

    a.set_xlim(0, 10.6)
    a.set_ylim(0, 10)
    a.axis("off")
    a.grid(False)
    cx1, cx2 = 4.3, 9.1
    box(a, cx1, 8.7, 4.4, 1.3, "New-money lenders", edge=ORANGE)
    box(a, cx1, 5.3, 4.4, 1.3, "SPV\n(new borrower)")
    box(a, cx1, 1.9, 4.4, 1.3, "OpCo\n(existing borrower)")
    box(a, cx2, 1.9, 2.8, 1.3, "First-lien\nlenders", edge=BLUE)
    box(a, cx2, 5.3, 2.8, 1.3, "Foreign sub\n(pari-plus only)", ls=(0, (3, 2)))
    arrow(a, (cx1, 8.05), (cx1, 5.95))                      # loan to SPV
    a.text(cx1 + 0.25, 7.0, "loan $F_2$", fontsize=8, color=INK_2, va="center")
    arrow(a, (cx1, 4.65), (cx1, 2.55))                      # intercompany note
    a.text(cx1 + 0.25, 3.6, "interco note $F_2$", fontsize=8, color=INK_2, va="center")
    arrow(a, (2.5, 8.05), (2.5, 2.55), rad=0.35)            # guarantee, bypassing the SPV
    a.text(0.6, 5.3, "guarantee $F_2$", fontsize=8, color=INK_2, va="center", ha="center", rotation=90)
    arrow(a, (cx2 - 1.4, 1.9), (cx1 + 2.2, 1.9))            # first lien
    a.text((cx2 - 1.4 + cx1 + 2.2) / 2, 2.2, "$F_1$", fontsize=8, color=INK_2, ha="center", va="bottom")
    arrow(a, (cx1 + 2.2, 8.4), (cx2, 5.95), ls=(0, (3, 2)))  # foreign guarantee
    a.text(9.0, 7.75, "direct\nguarantee", fontsize=8, color=INK_2, ha="center", va="center")
    a.text(cx1, 0.4, "all three claims on OpCo rank pari passu:\n$F_1$, $F_2$ (guarantee), $F_2$ (note)",
           fontsize=8, color=INK_2, ha="center", va="center")
    a.set_title("(a) Who has a claim on whom")

    V = np.linspace(0, 1800, 1801)
    dd, first = dd_recoveries(V, F1, F2)
    base = np.minimum(V, F1 + F2) / (F1 + F2)
    b.plot(V, 100 * base, color=NEUTRAL, linestyle=(0, (4, 3)), zorder=2)
    b.plot(V, 100 * first, color=BLUE, zorder=3)
    b.plot(V, 100 * dd, color=ORANGE, zorder=4)
    b.set_xlim(0, 1800)
    b.set_ylim(0, 108)
    b.set_xlabel("OpCo value V ($mm)")
    b.set_ylabel("Recovery (cents per $ of face)")
    b.xaxis.set_major_formatter(usd)
    b.set_xticks([0, 500, 1000, 1500])
    b.set_title("(b) Counted twice, paid twice")
    for xv in (1000, 1500):
        b.axvline(xv, color=NEUTRAL, linewidth=0.9, linestyle=(0, (3, 3)), zorder=1)
    v0 = 800.0
    for val, col in [(100 * dd_recoveries(v0, F1, F2)[0], ORANGE), (100 * dd_recoveries(v0, F1, F2)[1], BLUE),
                     (100 * v0 / (F1 + F2), NEUTRAL)]:
        b.plot([v0], [val], "o", color=col, markersize=5.5, zorder=7)
    b.annotate("80", (v0, 80), xytext=(-6, 4), textcoords="offset points", ha="right", fontsize=8, color=INK_2)
    b.annotate("40", (v0, 40), xytext=(5, -9), textcoords="offset points", ha="left", fontsize=8, color=INK_2)
    b.annotate("53", (v0, 53.3), xytext=(7, 1), textcoords="offset points", ha="left", fontsize=8, color=INK_2)
    from matplotlib.lines import Line2D
    b.legend(handles=[Line2D([], [], color=ORANGE, lw=LW, label="New money (guarantee + note)"),
                      Line2D([], [], color=BLUE, lw=LW, label="First lien (diluted)"),
                      Line2D([], [], color=NEUTRAL, lw=LW, ls=(0, (4, 3)), label="No dip: same lenders pari passu")],
             loc="lower right", fontsize=8, handlelength=2.2, frameon=True, facecolor="white",
             edgecolor="none", framealpha=1.0)
    return finish(fig, "ch13_double_dip_structure_recovery")


if __name__ == "__main__":
    fig_uptier()
    fig_knapsack()
    fig_coop()
    fig_payoff_shapes()
    fig_double_dip()
