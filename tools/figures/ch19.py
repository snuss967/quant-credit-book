"""Chapter 19 figures: Portfolio Trading & Basket Pricing Engines.

Run:  python3 tools/figures/ch19.py      (writes assets/figures/ch19_*.png)

Every number is ILLUSTRATIVE: it comes from the chapter's own synthetic cold-open basket (150 HY
lines, $212mm) and the engine in Listings 19.1-19.8 of Appendix F (book_src/95_appF_code_companion.md).
The script executes those listings, unchanged, in one namespace, so the figures can never drift from
the numbers the chapter quotes. Color roles are fixed across the chapter:
  terms of eq. 19.2 : handling = BLUE, residual risk = GREEN, adverse selection = VIOLET, hedge cost = YELLOW
  lines             : L042 (stale, $18mm) = ORANGE, L117 (the mystery box) = VIOLET
  scenarios         : calm = the term colors, stress = RED
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))
from style import *  # noqa: E402,F401,F403
import numpy as np  # noqa: E402
from matplotlib.patches import Patch  # noqa: E402

C_HANDLING, C_RISK, C_AS, C_HEDGE = BLUE, GREEN, VIOLET, YELLOW
C_L042, C_L117, C_STRESS = ORANGE, VIOLET, RED

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
APPENDIX = os.path.join(ROOT, "book_src", "95_appF_code_companion.md")


def load_engine():
    """Execute Listings 19.1-19.8 (the chapter's engine) in one namespace and return it."""
    with open(APPENDIX, encoding="utf-8") as fh:
        src = fh.read()
    ns = {"__name__": "ch19_engine"}
    for k in range(1, 9):
        m = re.search(r"\{#code-19-%d\}\s*```python\n(.*?)```" % k, src, re.S)
        if m is None:
            raise SystemExit(f"Listing 19.{k} not found in {APPENDIX}")
        exec(compile(m.group(1), f"listing_19_{k}", "exec"), ns)
    return ns


E = load_engine()
b0, c0 = E["b0"], E["c0"]
MV = b0.mv()
L42, L117 = 41, 116   # zero-based indices of lines 42 and 117


# --------------------------------------------------------------------------------------------
# Figure 19.1  The fat tail of handling cost (section 19.3)
# --------------------------------------------------------------------------------------------
def fig_handling_fat_tail():
    fig, (a, b) = new_figure("panel2", ncols=2)

    # (a) the size multiplier of eq. 19.3 for the three exponents
    x = np.linspace(0.0, 25.0, 300)
    shades = {0.5: SEQ_BLUE_STEPS[4], 0.75: SEQ_BLUE_STEPS[8], 1.0: SEQ_BLUE_STEPS[12]}
    for eta, col in shades.items():
        y = np.maximum(1.0, x / 4.0) ** eta
        a.plot(x, y, color=col)
        label_end(a, 25.0, y[-1], f"\u03b7 = {eta:g}", col, dx=5)
    a.axvline(4.0, color=NEUTRAL, linewidth=0.9, linestyle=(0, (3, 3)), zorder=1)
    a.annotate("standard size \\$4mm", (4.0, 0.97), xycoords=("data", "axes fraction"),
               xytext=(4, 0), textcoords="offset points", fontsize=8, color=INK_2, va="top")
    m42 = (18.0 / 4.0) ** 0.75
    a.plot([18.0], [m42], "o", color=C_L042, markersize=6.5, zorder=6)
    a.annotate("L042: \\$18mm, 3.1\u00d7\nat \u03b7 = 0.75 (2.1\u00d7 to 4.5\u00d7\nacross the range)", (18.0, m42), xytext=(5.3, 5.3),
               textcoords="data", ha="left", va="center", fontsize=8.5, color=INK_2,
               arrowprops=dict(arrowstyle="-", color=NEUTRAL, lw=0.8))
    a.set_xlim(0, 25)
    a.set_ylim(0.5, 7.2)
    a.set_xlabel("Ticket size (\\$mm par)")
    a.set_ylabel("Cost per dollar vs. standard size (\u00d7)")
    a.set_title("Size steepens the rake", fontsize=9.5)

    # (b) the ten most expensive lines by handling cost
    order = np.argsort(-c0)[:10][::-1]
    cols = [C_L042 if i == L42 else NEUTRAL for i in order]
    ypos = np.arange(len(order))
    b.barh(ypos, c0[order] / 1e3, color=cols, height=0.72)
    b.set_yticks(ypos)
    b.set_yticklabels([str(b0.ids[i]) for i in order], fontsize=8)
    b.set_axisbelow(True)
    b.grid(axis="y", visible=False)
    b.grid(axis="x", visible=True)
    b.set_xlabel("Handling cost (\\$k)")
    b.set_title("One line carries the tail", fontsize=9.5)
    share_mv = MV[L42] / MV.sum()
    share_c = c0[L42] / c0.sum()
    b.text(0.98, 0.34, f"L042: {share_mv:.0%} of notional,\n{share_c:.0%} of handling cost",
           transform=b.transAxes, ha="right", va="center", fontsize=8.5, color=INK_2)
    finish(fig, "ch19_handling_cost_fat_tail")


# --------------------------------------------------------------------------------------------
# Figure 19.2  The hedge: one lump, one residual (section 19.4)
# --------------------------------------------------------------------------------------------
def fig_hedge_bowl():
    d_naive = b0.sig_idio ** 2 * E["T_DAYS"]
    x = b0.x
    lam = np.linspace(0.0, 2.0, 201)
    out = {}
    h_calm = None
    for name, scale in (("calm", 1.0), ("stress", 3.0)):
        Sxx, Sxf, Sff = E["joint_cov"](b0, d_naive, basis_scale=scale)
        h_star = E["min_var_hedge"](x, Sxf, Sff)
        if name == "calm":
            h_calm = h_star
        v0 = x @ Sxx @ x
        cross = h_calm @ (Sxf.T @ x)
        quad = h_calm @ Sff @ h_calm
        sd = np.sqrt(np.maximum(v0 - 2 * lam * cross + lam ** 2 * quad, 0.0)) / 1e6
        out[name] = (sd, cross / quad, (v0 - cross ** 2 / quad) ** 0.5 / 1e6)

    fig, (a, b) = new_figure("panel2", ncols=2)
    sd_c, lam_c, min_c = out["calm"]
    sd_s, lam_s, min_s = out["stress"]
    a.plot(lam, sd_c, color=C_RISK)
    a.plot(lam, sd_s, color=C_STRESS)
    a.plot([lam_c], [min_c], "o", color=C_RISK, markersize=6, zorder=6)
    a.plot([lam_s], [min_s], "o", color=C_STRESS, markersize=6, zorder=6)
    a.plot([0.0], [sd_c[0]], "s", color=INK_2, markersize=5, zorder=6, clip_on=False)
    label_end(a, 2.0, sd_c[-1], "calm basis", C_RISK, dx=5)
    label_end(a, 2.0, sd_s[-1], "stress basis", C_STRESS, dx=5)
    a.annotate(f"unhedged: \\${sd_c[0]:.2f}mm", (0.0, sd_c[0]), xytext=(0.08, 1.9), textcoords="data",
               fontsize=8.5, color=INK_2, ha="left", va="center",
               arrowprops=dict(arrowstyle="-", color=NEUTRAL, lw=0.8, shrinkA=2, shrinkB=4))
    a.annotate(f"min \\${min_c:.2f}mm\nat 1\u00d7", (lam_c, min_c), xytext=(0, -9), textcoords="offset points",
               fontsize=8.5, color=INK_2, ha="center", va="top")
    a.annotate(f"min \\${min_s:.2f}mm\nat {lam_s:.1f}\u00d7", (lam_s, min_s), xytext=(0, 9),
               textcoords="offset points", fontsize=8.5, color=INK_2, ha="center", va="bottom")
    a.set_xlim(0, 2.0)
    a.set_ylim(0, max(sd_c[-1], sd_s[-1]) * 1.06)
    a.set_xlabel("Hedge size (\u00d7 the calm-basis optimum)")
    a.set_ylabel("Std. dev. of 5-day P&L (\\$mm)")
    a.set_title("Hedged risk is a bowl", fontsize=9.5)
    a.margins(x=0)

    # (b) one factor, one hedge with basis noise: attenuation and the surviving systematic residual
    rho = np.logspace(-1, 1, 300)          # basis noise / hedge's factor risk
    r2 = 1.0 / (1.0 + rho ** 2)            # = h* / h_DTS-matched = share of systematic variance removed
    b.fill_between(rho, 0, r2, color=C_HEDGE, alpha=0.35, linewidth=0)
    b.fill_between(rho, r2, 1.0, color=C_RISK, alpha=0.30, linewidth=0)
    b.plot(rho, r2, color=INK_2)
    b.set_xscale("log")
    b.set_xlim(0.1, 10)
    b.set_xticks([0.1, 1, 10])
    b.set_xticklabels(["0.1", "1", "10"])
    b.minorticks_off()
    b.set_ylim(0, 1)
    b.grid(axis="y", visible=True)
    b.text(0.13, 0.20, "hedge ratio kept\n(share of DTS-matched)", fontsize=8.5, color=INK_2,
           va="center", ha="left")
    b.text(1.5, 0.90, "systematic variance\nthat survives", fontsize=8.5, color=INK_2, va="center", ha="left")
    b.set_xlabel("Basis noise \u00f7 the hedge's factor risk")
    b.set_ylabel("Fraction")
    b.set_title("Basis shrinks the hedge", fontsize=9.5)
    finish(fig, "ch19_hedge_bowl_and_basis")


# --------------------------------------------------------------------------------------------
# Figure 19.3  Stress commonality: one score, and a risk that does not diversify (section 19.7)
# --------------------------------------------------------------------------------------------
def fig_stress_commonality():
    fig, (a, b) = new_figure("panel2", ncols=2)

    # (a) the regime map: one score s drives three multipliers
    s = np.linspace(0.0, 2.0, 100)
    reg = [E["regime"](etf_disc_z=-1.0 - 3.0 * min(si, 1.0), bidask_pct=0.8 + 0.2 * max(si - 1.0, 0.0))
           for si in s]    # any path that reproduces s; the multipliers are straight lines in s
    s_chk = np.array([r["s"] for r in reg])
    assert np.allclose(s_chk, s, atol=1e-9)
    lines = [("m", "liquidity m", C_HANDLING), ("basis_mult", "ETF basis", C_HEDGE),
             ("gamma_mult", "risk aversion \u03b3", C_RISK)]
    for key, lab, col in lines:
        y = np.array([r[key] for r in reg])
        a.plot(s, y, color=col)
        label_end(a, 2.0, y[-1], f"{lab}  {y[-1]:.1f}\u00d7", col, dx=5)
    a.axvline(1.0, color=NEUTRAL, linewidth=0.9, linestyle=(0, (3, 3)), zorder=1)
    a.annotate("s = 1: ETF at \u22122.5\u03c3,\nspread at 90th pct", (1.0, 0.04), xycoords=("data", "axes fraction"),
               xytext=(4, 0), textcoords="offset points", ha="left", va="bottom", fontsize=8, color=INK_2)
    a.set_xlim(0, 2.0)
    a.set_ylim(0.8, 6.4)
    a.set_xlabel("Stress score s")
    a.set_ylabel("Multiplier on the calm value (\u00d7)")
    a.set_title("One score, three dials", fontsize=9.5)

    # (b) risk per dollar vs. number of lines: idiosyncratic residual diversifies, the liquidity spike does not
    rng = np.random.default_rng(1902)
    ordinary = np.setdiff1d(np.arange(b0.n), [L42, L117])
    Sres = E["Sres"]
    g = -E["THETA_LIQ"] * b0.lcs * b0.mid
    s_ex = 1.0
    d_idio = E["idio_var"](b0)
    ns = np.array([4, 8, 16, 32, 64, 100, 148])
    idio, spike = [], []
    for n in ns:
        vi, vs = [], []
        for _ in range(300):
            idx = rng.choice(ordinary, size=n, replace=False)
            xx = b0.x[idx]
            gross = np.abs(xx).sum()
            vi.append(np.sum(xx ** 2 * d_idio[idx]) / gross ** 2)
            vs.append(((0.25 * s_ex) * (g[idx] @ xx) / gross) ** 2)
        idio.append(np.sqrt(np.mean(vi)) * 1e4)
        spike.append(np.sqrt(np.mean(vs)) * 1e4)
    idio, spike = np.array(idio), np.array(spike)
    total = np.sqrt(idio ** 2 + spike ** 2)
    b.plot(ns, idio, color=C_RISK, marker="o", markersize=5)
    b.plot(ns, spike, color=C_STRESS, marker="o", markersize=5)
    b.plot(ns, total, color=INK_2, linestyle=(0, (4, 2)))
    b.set_xscale("log")
    b.set_xticks([4, 8, 16, 32, 64, 148])
    b.set_xticklabels(["4", "8", "16", "32", "64", "148"])
    b.minorticks_off()
    b.set_xlim(3.5, 148 * 1.02)
    b.set_ylim(0, None)
    label_end(b, 148, idio[-1], "idiosyncratic", C_RISK, dx=-4, dy=-10, ha="right")
    label_end(b, 148, spike[-1], "liquidity spike", C_STRESS, dx=-4, dy=-10, ha="right")
    b.annotate("total", (ns[1], total[1]), xytext=(10, 6), textcoords="offset points", fontsize=8.5, color=INK_2)
    b.set_xlabel("Lines in the basket (log scale)")
    b.set_ylabel("5-day risk per \\$ of par (bp)")
    b.set_title("The spike does not diversify", fontsize=9.5)
    finish(fig, "ch19_stress_commonality")
    return ns, idio, spike


# --------------------------------------------------------------------------------------------
# Figure 19.4  Two rankings: liquidity alone evicts L042, the AS term evicts L117 (section 19.8)
# --------------------------------------------------------------------------------------------
def fig_eviction_ranking():
    gam = 1e-6
    Sres, x = E["Sres"], b0.x
    Sx = Sres @ x
    base = c0 + gam * x * Sx - 0.5 * gam * np.diag(Sres) * x ** 2
    panels = [("Liquidity and risk only", np.zeros(b0.n)), ("With the adverse-selection term", E["as0"])]
    fig, axes = new_figure("panel2", ncols=2, sharex=True)
    xmax = 0
    for ax, (title, av) in zip(axes, panels):
        ratio = 1e4 * (base + av) / MV
        cost = (c0 + av).sum() + 0.5 * gam * x @ Sres @ x
        avg = 1e4 * cost / MV.sum()
        top = np.argsort(-ratio)[:8][::-1]
        cols = [C_L042 if i == L42 else C_L117 if i == L117 else NEUTRAL for i in top]
        ypos = np.arange(len(top))
        ax.barh(ypos, ratio[top], color=cols, height=0.72)
        ax.set_yticks(ypos)
        ax.set_yticklabels([str(b0.ids[i]) for i in top], fontsize=8)
        ax.axvline(avg, color=INK_2, linewidth=0.9, linestyle=(0, (3, 3)), zorder=1)
        ax.text(0.98, 0.64, f"dashed: basket average,\n{avg:.0f}bp per \\$ of MV", transform=ax.transAxes,
                ha="right", va="center", fontsize=8, color=INK_2)
        ax.set_axisbelow(True)
        ax.grid(axis="y", visible=False)
        ax.grid(axis="x", visible=True)
        ax.set_title(title, fontsize=9.5)
        ax.set_xlabel("Removal saving per \\$ of MV (bp)")
        for k, i in enumerate(top):
            if i in (L42, L117):
                rank = int(np.sum(ratio > ratio[i])) + 1
                ax.text(ratio[i] + 18, k, f"rank {rank}", va="center", fontsize=8, color=INK_2)
        if title.startswith("Liquidity"):
            r117 = 1e4 * (base[L117]) / MV[L117]
            rank117 = int(np.sum(ratio > ratio[L117])) + 1
        xmax = max(xmax, ratio.max())
    axes[0].set_xlim(0, xmax * 1.12)
    handles = [Patch(color=C_L042, label="L042: stale, \\$18mm"), Patch(color=C_L117, label="L117: ad hoc group, lender call")]
    axes[1].legend(handles=handles, loc="lower right", bbox_to_anchor=(1.0, 0.0), fontsize=8, handlelength=1.0)
    finish(fig, "ch19_eviction_ranking_flip")
    return rank117, r117


# --------------------------------------------------------------------------------------------
# Figure 19.5  The cost of the same basket in four situations (section 19.10)
# --------------------------------------------------------------------------------------------
def fig_cost_stack():
    pp = E["price_pt"]
    runs = [
        ("Full list\ncalm", pp(b0, evict=False)),
        ("Counter-proposal\ncalm (L117, L042 out)", pp(b0)),
        ("Full list\nstress, s = 1", pp(b0, etf_disc_z=-2.5, bidask_pct=0.9, evict=False)),
        ("Counter-proposal\nstress (10 lines out)", pp(b0, etf_disc_z=-2.5, bidask_pct=0.9)),
    ]
    gross = [None] * 4
    keep_mv = []
    for (_, r) in runs:
        ev = [int(i[1:]) - 1 for i in r["evicted"]]
        keep_mv.append(MV[np.setdiff1d(np.arange(b0.n), ev)].sum())
    terms = [("handling", "Handling", C_HANDLING), ("risk", "Residual risk", C_RISK),
             ("adv", "Adverse selection", C_AS), ("hedge_cost", "Hedge half-spread (under 1bp)", C_HEDGE)]
    fig, ax = new_figure("wide")
    xs = np.arange(len(runs))
    bottoms = np.zeros(len(runs))
    for key, lab, col in terms:
        vals = np.array([1e4 * r[key] / mv for (_, r), mv in zip(runs, keep_mv)])
        ax.bar(xs, vals, bottom=bottoms, color=col, width=0.62, edgecolor="white", linewidth=0.8, label=lab)
        bottoms += vals
    ax.axhline(45, color=INK, linewidth=0.9, linestyle=(0, (3, 3)), zorder=4)
    for xi, tot in zip(xs, bottoms):   # white backing lets a total sit on the dashed target line
        ax.text(xi, tot + 3, f"{tot:.0f}bp", ha="center", va="bottom", fontsize=9, color=INK, zorder=6,
                bbox=dict(facecolor="white", edgecolor="none", pad=1.2))
    ax.annotate("45bp target", (3.97, 45), xytext=(0, 2), textcoords="offset points", fontsize=8,
                color=INK_2, ha="right", va="bottom")
    ax.set_xticks(xs)
    ax.set_xticklabels([n for n, _ in runs], fontsize=8.5)
    ax.set_xlim(-0.55, 4.0)
    ax.set_ylim(0, bottoms.max() * 1.12)
    ax.set_ylabel("Cost, bp of kept gross market value")
    hh, ll = ax.get_legend_handles_labels()   # legend reads top-down like the stack
    ax.legend(hh[::-1], ll[::-1], loc="upper right", ncols=1, fontsize=8.5, handlelength=1.0)
    ax.set_axisbelow(True)
    ax.grid(axis="y", visible=True)
    finish(fig, "ch19_cost_stack_by_scenario")
    return runs, bottoms


if __name__ == "__main__":
    fig_handling_fat_tail()
    fig_hedge_bowl()
    fig_stress_commonality()
    fig_eviction_ranking()
    fig_cost_stack()
