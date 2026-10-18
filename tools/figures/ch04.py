"""Figures for Chapter 4 (Inside the Systematic Credit Industry).

Run:  python3 tools/figures/ch04.py      -> assets/figures/ch04_*.png  (five figures, in order of appearance)

Data policy (see style.py):
  4.1 effective_breadth    Illustrative: equation (4.1) evaluated on a grid (no data).
  4.2 truncation_bias      Illustrative: the normal case is the closed form of section 4.5 (phi(z_q)/(1-q));
                           the fat-tailed and left-skewed cases are stated models (see the caption).
  4.3 factor_zoo_survivors Source: Dickerson-Robotti-Rossetti (2026), arXiv:2604.07880, Internet Appendix IA.3,
                           counts as quoted in section 4.5 and in state/research/papers_factor_replication_crisis_and_bond_data.md 3.4.
  4.4 capacity_hot_tub     Illustrative: equation (4.2) at the section 4.8 worked-example parameters.
  4.5 empty_cells_map      Source: the section 4.3 table; the shading is the book's own reading of each cell.

Colour roles held fixed across the chapter's figures:
  BLUE   = the baseline or "within-firm" case (breadth m = 2.25 highlight, normal bell, HY long/short book)
  ORANGE = the contrast case (single-sort survivor, fat-tailed bell, equity-momentum book)
  AQUA   = the third case (left-skewed credit returns)
  INK_2 / NEUTRAL = reference lines and de-emphasised stages
"""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
import numpy as np  # noqa: E402
from matplotlib.patches import FancyArrowPatch, Rectangle  # noqa: E402
from scipy import optimize, stats  # noqa: E402

from style import *  # noqa: E402,F401,F403

BACK = dict(boxstyle="square,pad=0.15", fc="white", ec="none")   # hides gridlines behind a text label
MINUS = "−"


# ---------------------------------------------------------------------------------------------
# 4.3  Effective breadth under issuer clustering, equation (4.1)
# ---------------------------------------------------------------------------------------------
def fig_effective_breadth():
    fig, ax = new_figure()
    rho = np.linspace(0, 1, 201)
    ms = [(1.5, 0.30), (2.25, 0.55), (4.0, 0.78), (8.0, 1.0)]       # (bonds per issuer, SEQ_BLUE position)
    for m, pos in ms:
        col = SEQ_BLUE(pos)
        lw = 2.4 if m == 2.25 else LW
        ax.plot(rho, 1 / (1 + (m - 1) * rho), color=col, linewidth=lw, zorder=3)
        label_end(ax, 1.0, 1 / m, f"m = {m:g}", col, dx=6)
    ax.plot(rho, 1 / (1 + 46 * rho), color=INK_2, linewidth=LW, linestyle=(0, (4, 3)), zorder=3)
    label_end(ax, 1.0, 1 / 47, "m = 47 (ROBO's issuer)", INK_2, dx=6)

    # the chapter's worked example: N = 1,800, M = 800 (m = 2.25), rho = 0.7 -> 960 independent bets
    m0, r0 = 2.25, 0.7
    y0 = 1 / (1 + (m0 - 1) * r0)
    assert abs(y0 * 1800 - 960) < 1e-9
    ax.plot([r0], [y0], "o", color="white", markeredgecolor=INK, markeredgewidth=1.6, markersize=9, zorder=6)
    ax.annotate("1,800 bonds are worth 960 independent bets\n(m = 2.25, ρ = 0.7): IR 0.64 falls to 0.46",
                (r0, y0), xytext=(0.30, 0.955), textcoords="data", ha="left", va="top", fontsize=8.5, color=INK,
                arrowprops=dict(arrowstyle="-", color=INK_2, linewidth=0.9, shrinkA=2, shrinkB=6,
                                connectionstyle="arc3,rad=0"), bbox=BACK, zorder=7)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1.0)
    ax.set_xlabel("Within-issuer residual correlation ρ")
    ax.set_ylabel("Effective breadth, as a share of bond count\n(BR$_{\\mathrm{eff}}$ / N)")
    ax.yaxis.set_major_formatter(lambda v, _: f"{v:.1f}")
    ax.text(0.01, 0.03, "bonds per issuer m;  ρ = 0: every bond is a bet;  ρ = 1: one bet per issuer",
            transform=ax.transAxes, fontsize=8, color=INK_2, ha="left", va="bottom", bbox=BACK, zorder=6)
    return finish(fig, "ch04_effective_breadth")


# ---------------------------------------------------------------------------------------------
# 4.5  Deleting the worst months manufactures a premium
# ---------------------------------------------------------------------------------------------
def shift_normal(q):
    z = stats.norm.ppf(q)
    return stats.norm.pdf(z) / (1 - q)


def shift_student(q, nu=4):
    """Mean shift (in sigma units) of a unit-variance Student t after deleting the lowest fraction q."""
    s = math.sqrt(nu / (nu - 2.0))
    c = stats.t.ppf(q, nu)
    return stats.t.pdf(c, nu) * (nu + c * c) / (nu - 1.0) / (1 - q) / s


MIX_W, MIX_MU, MIX_SD = (0.98, 0.02), (0.5, -12.0), (2.0, 6.0)      # % a month: ordinary months, distress months


def shift_mixture(q):
    mean = sum(w * m for w, m in zip(MIX_W, MIX_MU))
    var = sum(w * (s * s + m * m) for w, m, s in zip(MIX_W, MIX_MU, MIX_SD)) - mean * mean
    cdf = lambda x: sum(w * stats.norm.cdf((x - m) / s) for w, m, s in zip(MIX_W, MIX_MU, MIX_SD))
    cut = optimize.brentq(lambda x: cdf(x) - q, -80.0, 20.0)
    part = sum(w * (m * (1 - stats.norm.cdf((cut - m) / s)) + s * stats.norm.pdf((cut - m) / s))
               for w, m, s in zip(MIX_W, MIX_MU, MIX_SD))
    return (part / (1 - q) - mean) / math.sqrt(var)


def fig_truncation_bias():
    fig, (a, b) = new_figure("panel2", ncols=2)

    # (a) the bell, the scissors and the balance points
    zq = stats.norm.ppf(0.01)
    u = np.linspace(-4, 4, 600)
    f = stats.norm.pdf(u)
    a.plot(u, f, color=INK_2, linewidth=LW, zorder=3)
    cut = u <= zq
    a.fill_between(u[cut], 0, f[cut], color=DIVERGING(0.82), zorder=2)
    a.fill_between(u[~cut], 0, f[~cut], color=SEQ_BLUE(0.12), zorder=1)
    a.annotate("worst 1% of months,\ndeleted ($u < -2.33$)", (zq - 0.15, 0.012), xytext=(-3.9, 0.20),
               ha="left", va="center", fontsize=8.5, color=INK,
               arrowprops=dict(arrowstyle="-", color=INK_2, linewidth=0.9, shrinkA=1, shrinkB=1))
    a.annotate("what is left:\n99% of months", (1.0, 0.24), ha="left", va="center", fontsize=8.5, color=INK)
    a.set_ylim(0, 0.43)
    a.set_xlim(-4, 4)
    a.set_xlabel("Monthly return, in standard deviations from the mean")
    a.set_ylabel("Density")
    a.yaxis.set_major_formatter(lambda v, _: f"{v:.1f}")
    # balance points, zoomed in on an inset: they sit only 0.027 sigma apart
    ins = a.inset_axes([0.62, 0.50, 0.36, 0.30])
    ins.set_xlim(-0.03, 0.06)
    ins.set_ylim(0, 1)
    ins.grid(False)
    ins.set_yticks([])
    ins.set_xticks([0, 0.027])
    ins.set_xticklabels(["0", "0.027"], fontsize=8)
    for sp in ("left",):
        ins.spines[sp].set_visible(False)
    ins.plot([0], [0.12], "^", color=INK_2, markersize=8, clip_on=False, zorder=4)
    ins.plot([0.027], [0.12], "^", color=BLUE, markersize=8, clip_on=False, zorder=4)
    ins.text(0.0, 0.46, "before", ha="right", va="bottom", fontsize=8, color=INK_2)
    ins.text(0.027, 0.46, "after", ha="left", va="bottom", fontsize=8, color=INK_2)
    ins.set_title("balance point (zoom, $\\sigma$)", fontsize=8, color=INK_2, fontweight="normal", pad=3)

    # (b) the manufactured premium against the fraction deleted
    qs = np.linspace(0.001, 0.05, 80)
    cases = [("normal", BLUE, shift_normal, "-"),
             ("fat-tailed (Student t, 4 d.f.)", ORANGE, shift_student, "-"),
             ("left-skewed (2% distress months)", AQUA, shift_mixture, "-")]
    vals = {}
    for name, col, fn, ls in cases:
        y = np.array([fn(q) for q in qs])
        b.plot(100 * qs, y, color=col, linewidth=LW, linestyle=ls, zorder=3)
        v1 = fn(0.01)
        vals[name] = v1
        b.plot([1.0], [v1], "o", color=col, markersize=6, zorder=5)
    assert abs(vals["normal"] - 0.027) < 5e-4
    b.axvline(1.0, color=NEUTRAL, linewidth=0.9, linestyle=(0, (3, 3)), zorder=1)
    b.text(1.12, 0.168, "q = 1%", fontsize=8, color=INK_2, ha="left", va="center")
    b.set_xlim(0, 5)
    b.set_ylim(0, 0.19)
    b.set_xlabel("Share of worst months deleted, q (%)")
    b.set_ylabel("Premium manufactured per month ($\\sigma$)")
    b.yaxis.set_major_formatter(lambda v, _: f"{v:.2f}")
    # direct labels at the right-hand end (the curves fan out there)
    ends = {name: fn(0.05) for name, _c, fn, _l in cases}
    b.annotate("left-skewed", (5.0, ends["left-skewed (2% distress months)"]), xytext=(-5, 7),
               textcoords="offset points", ha="right", va="bottom", fontsize=8.5, color=INK_2)
    b.annotate("fat-tailed", (5.0, ends["fat-tailed (Student t, 4 d.f.)"]), xytext=(-5, 7),
               textcoords="offset points", ha="right", va="bottom", fontsize=8.5, color=INK_2)
    b.annotate("normal", (5.0, ends["normal"]), xytext=(-5, -9), textcoords="offset points", ha="right",
               va="top", fontsize=8.5, color=INK_2)
    # the q = 1% values, in basis points a month at 4% monthly volatility
    txt = "\n".join(f"{n.split(' (')[0]:<12} {v:.3f}σ = {v * 4 * 100:.0f}bp a month".replace("  ", " ")
                    for n, v in vals.items())
    b.text(0.02, 0.97, "At q = 1%, on 4% monthly volatility:\n" + txt, transform=b.transAxes, ha="left", va="top",
           fontsize=7.8, color=INK_2, bbox=BACK, zorder=7)
    return finish(fig, "ch04_truncation_bias")


# ---------------------------------------------------------------------------------------------
# 4.5  The 2026 audit: 432 specifications, 65 pass a t-test, 26 survive the false-discovery correction
# ---------------------------------------------------------------------------------------------
def fig_factor_zoo():
    n_spec, n_t, n_fdr = 108 * 2 * 2, 65, 26
    panels = [("Equal-weighted, within-firm", 16, "within"), ("Value-weighted, within-firm", 9, "within"),
              ("Equal-weighted, single-sort", 1, "single"), ("Value-weighted, single-sort", 0, "single")]
    assert n_spec == 432 and sum(p[1] for p in panels) == n_fdr
    assert round(100 * n_t / n_spec, 1) == 15.0 and round(100 * n_fdr / n_spec, 1) == 6.0
    assert sum(p[1] for p in panels if p[2] == "within") == 25

    fig, (a, b) = new_figure("panel2", ncols=2, gridspec_kw=dict(width_ratios=[1.05, 1]))
    # (a) the funnel
    labels = ["Tested\n(108 signals × 2 weightings\n× 2 sort types)", "t > 1.96 on\nCAPM-B alpha", "Survive the\nfalse-discovery\ncorrection (5%)"]
    vals = [n_spec, n_t, n_fdr]
    cols = [NEUTRAL, MUTED, INK_2]
    y = np.arange(3)[::-1]
    a.barh(y, vals, height=0.62, color=cols, zorder=3)
    a.set_yticks(y)
    a.set_yticklabels(labels, fontsize=8)
    for yi, v, extra in zip(y, vals, ["", "  (15.0%)", "  (6.0%)"]):
        a.text(v + 8, yi, f"{v}{extra}", va="center", ha="left", fontsize=9, color=INK, fontweight="bold")
    a.set_xlim(0, 540)
    a.set_xlabel("Specifications")
    a.grid(axis="y", visible=False)
    a.grid(axis="x", visible=True)
    a.set_axisbelow(True)

    # (b) the 26 survivors by panel
    names = [p[0].replace(", ", ",\n") for p in panels]
    yy = np.arange(4)[::-1]
    for yi, (nm, v, kind) in zip(yy, panels):
        col = BLUE if kind == "within" else ORANGE
        b.barh([yi], [v], height=0.62, color=col, zorder=3)
    b.set_yticks(yy)
    b.set_yticklabels(names, fontsize=8)
    for yi, (nm, v, kind) in zip(yy, panels):
        if nm.startswith("Equal-weighted, single"):
            s = f"{v}  bond age, the only one"
        else:
            s = f"{v}"
        b.text(v + 0.35, yi, s, va="center", ha="left", fontsize=9, color=INK, fontweight="bold" if v else "normal")
    b.set_xlim(0, 24)
    b.set_xlabel("Survivors (26 in all)")
    b.grid(axis="y", visible=False)
    b.grid(axis="x", visible=True)
    b.set_axisbelow(True)
    b.plot([0.9], [3.52], "s", color=BLUE, markersize=6, clip_on=False)
    b.text(1.4, 3.52, "within-firm: 25 of 26", fontsize=8.5, color=INK_2, va="center", ha="left")
    b.plot([13.0], [3.52], "s", color=ORANGE, markersize=6, clip_on=False)
    b.text(13.5, 3.52, "single-sort: 1", fontsize=8.5, color=INK_2, va="center", ha="left")
    b.set_ylim(-0.55, 3.8)
    return finish(fig, "ch04_factor_zoo_survivors")


# ---------------------------------------------------------------------------------------------
# 4.8  The hot tub: dollar alpha against AUM, equation (4.2)
# ---------------------------------------------------------------------------------------------
def capacity(alpha0, T, c0, eta, L):
    g = alpha0 - 2 * T * c0
    a_star = L * g ** 2 / (18 * T ** 3 * eta ** 2)
    return g, a_star, 9.0 / 4.0 * a_star


def fig_capacity():
    c0, eta, L = 0.0025, 0.02, 20.0           # 25bp half-spread, impact coefficient, USD 20bn of liquidity a year
    cases = [dict(name="HY long/short multi-factor", alpha0=0.015, T=0.6, col=BLUE, unit="bn", scale=1.0, xmax=4.6),
             dict(name="Equity-momentum signal", alpha0=0.04, T=2.5, col=ORANGE, unit="mm", scale=1000.0, xmax=0.34)]
    fig, axes = new_figure("panel2", ncols=2)
    out = {}
    for ax, c in zip(axes, cases):
        g, a_star, a0 = capacity(c["alpha0"], c["T"], c0, eta, L)
        out[c["name"]] = (g, a_star, a0)
        A = np.linspace(0, c["xmax"], 500)
        net = g - 2 * c["T"] * eta * np.sqrt(2 * c["T"] * A / L)
        pi = A * net * 1000.0                  # USD mm a year (A in bn)
        edge = A * g * 1000.0                  # the straight line: the spread-net edge on every dollar, before impact
        ax.plot(A * c["scale"], edge, color=NEUTRAL, linewidth=LW, linestyle=(0, (4, 3)), zorder=2)
        ax.plot(A * c["scale"], pi, color=c["col"], linewidth=2.2, zorder=4)
        ax.fill_between(A * c["scale"], 0, np.maximum(pi, 0), color=c["col"], alpha=0.10, linewidth=0, zorder=1)
        p_star = a_star * (g / 3) * 1000.0
        e_star = a_star * g * 1000.0
        ax.plot([a_star * c["scale"]], [p_star], "o", color=c["col"], markersize=7, zorder=6)
        ax.plot([a0 * c["scale"]], [0], "o", color="white", markeredgecolor=c["col"], markeredgewidth=1.6,
                markersize=7, zorder=6, clip_on=False)
        # the one-third rule at the top of the hill
        ax.add_patch(FancyArrowPatch((a_star * c["scale"], p_star), (a_star * c["scale"], e_star),
                                     arrowstyle="<|-|>", mutation_scale=8, linewidth=1.0, color=INK_2,
                                     shrinkA=3, shrinkB=0, zorder=5))
        ax.set_xlabel(f"Assets under management (USD {c['unit']})")
        ax.set_title(f"{c['name']}:  α₀ = {c['alpha0'] * 1e4:.0f}bp,  T = {c['T']:g}", fontsize=9, pad=6)
        c["g"], c["a_star"], c["a0"], c["p_star"], c["e_star"] = g, a_star, a0, p_star, e_star

    a, b = axes
    # left panel annotations
    c = cases[0]
    a.set_xlim(0, c["xmax"])
    a.set_ylim(0, 27)
    a.set_ylabel("Dollar alpha (USD mm a year)")
    a.text(c["a_star"] + 0.12, c["p_star"] * 0.55, f"top at A* ≈ ${c['a_star']:.2f}bn\nclient keeps {c['g'] * 1e4 / 3:.0f}bp\n= g/3, a third of {c['g'] * 1e4:.0f}bp",
           ha="left", va="center", fontsize=8.2, color=INK, bbox=BACK, zorder=7)
    a.text(c["a_star"] - 0.1, (c["p_star"] + c["e_star"]) / 2, "impact takes\ntwo thirds", ha="right", va="center",
           fontsize=8.2, color=INK_2, bbox=BACK, zorder=7)
    a.annotate(f"edge gone at A₀ = 9/4 A* ≈ ${c['a0']:.1f}bn", (c["a0"], 0), xytext=(c["a0"] - 0.1, 3.3),
               ha="right", va="bottom", fontsize=8.2, color=INK, bbox=BACK, zorder=7,
               arrowprops=dict(arrowstyle="-", color=INK_2, linewidth=0.9, shrinkA=0, shrinkB=5))
    a.text(0.07, 25.8, "before impact: g × A", fontsize=8.2, color=INK_2, ha="left", va="top", rotation=0, bbox=BACK, zorder=7)
    # right panel annotations
    c = cases[1]
    b.set_xlim(0, c["xmax"] * c["scale"])
    b.set_ylim(0, 4.6)
    b.set_ylabel("Dollar alpha (USD mm a year)")
    b.text(c["a_star"] * c["scale"] + 18, c["p_star"] * 0.52,
           f"top at A* ≈ ${c['a_star'] * 1000:.0f}mm\nclient keeps {c['g'] * 1e4 / 3:.0f}bp = g/3,\na third of {c['g'] * 1e4:.0f}bp",
           ha="left", va="center", fontsize=8.2, color=INK, bbox=BACK, zorder=7)
    b.text(c["a_star"] * c["scale"] - 6, (c["p_star"] + c["e_star"]) / 2, "impact takes\ntwo thirds", ha="right",
           va="center", fontsize=8.2, color=INK_2, bbox=BACK, zorder=7)
    b.annotate(f"edge gone at ${c['a0'] * 1000:.0f}mm", (c["a0"] * c["scale"], 0),
               xytext=(c["a0"] * c["scale"] - 10, 1.55), ha="right", va="bottom", fontsize=8.2, color=INK, bbox=BACK, zorder=7,
               arrowprops=dict(arrowstyle="-", color=INK_2, linewidth=0.9, shrinkA=0, shrinkB=5))
    # the chapter's published numbers
    g0, as0, a00 = out[cases[0]["name"]]
    g1, as1, a01 = out[cases[1]["name"]]
    assert abs(as0 - 1.852) < 0.005 and abs(a00 - 4.167) < 0.005 and abs(as1 * 1000 - 134.4) < 0.5
    return finish(fig, "ch04_capacity_hot_tub")


# ---------------------------------------------------------------------------------------------
# 4.11  The six-axis map of section 4.3 as a picture: full, stated and silent cells
# ---------------------------------------------------------------------------------------------
F, S, X = 2, 1, 0       # F = specific feature or method; S = stated without a method; X = silent
COLS = ["Alpha\nfamilies", "Data\nstack", "Portfolio\nconstruction", "Execution", "Capacity", "Risk"]
ROWS = [
    ("Man 2022", [F, F, F, F, S, S], {}),
    ("Man 2023", [S, F, S, F, S, S], {}),
    ("Blackstone BCBS", [F, F, F, S, S, S], {}),
    ("BlackRock systematic HY", [F, F, S, X, X, F], {}),
    ("Nuveen MAC", [F, F, F, X, S, F], {3: "not modeled"}),
    ("Robeco multi-factor", [F, S, F, X, X, S], {}),
    ("Acadian", [F, F, S, X, X, X], {5: "not disclosed"}),
    ("Barclays QPS", [F, F, F, F, F, F], {}),
]
LEVEL_FILL = {F: BLUE, S: SEQ_BLUE_STEPS[1], X: "#f0efec"}


def fig_empty_cells():
    n_r, n_c = len(ROWS), len(COLS)
    fig, ax = new_figure((7.0, 4.75))
    ax.set_axis_off()
    ax.grid(False)
    gap = 0.07
    for i, (name, levels, words) in enumerate(ROWS):
        y = i
        ax.text(-0.12, y + 0.5, name, ha="right", va="center", fontsize=8.8, color=INK)
        for j, lv in enumerate(levels):
            ax.add_patch(Rectangle((j + gap, y + gap), 1 - 2 * gap, 1 - 2 * gap, facecolor=LEVEL_FILL[lv],
                                   edgecolor="none", zorder=2))
            if lv == X:
                ax.text(j + 0.5, y + 0.5, words.get(j, "silent"), ha="center", va="center", fontsize=7.6,
                        color=INK_2, style="italic", zorder=3)
    for j, h in enumerate(COLS):
        ax.text(j + 0.5, -0.12, h, ha="center", va="bottom", fontsize=8.8, color=INK, linespacing=1.05)
    # the dashed ninth row: no framework on the map has a feature for any of these
    y9 = n_r + 0.35
    ax.text(-0.12, y9 + 0.5, "LMT exposure, distressed,\nbond choice within an issuer", ha="right", va="center",
            fontsize=8.8, color=INK, linespacing=1.1)
    ax.add_patch(Rectangle((gap, y9 + gap), n_c - 2 * gap, 1 - 2 * gap, facecolor="white", edgecolor=INK_2,
                           linewidth=1.2, linestyle=(0, (4, 3)), zorder=2))
    ax.text(n_c / 2, y9 + 0.5, "no framework on the map has a feature for any of these", ha="center", va="center",
            fontsize=8.8, color=INK, style="italic", zorder=3)
    # legend
    ly = y9 + 1.55
    items = [(F, "specific feature or method"), (S, "stated, no method"), (X, "silent")]
    x = 0.0
    for lv, lab in items:
        ax.add_patch(Rectangle((x, ly), 0.3, 0.32, facecolor=LEVEL_FILL[lv], edgecolor=NEUTRAL if lv == X else "none",
                               linewidth=0.6, zorder=2))
        ax.text(x + 0.42, ly + 0.16, lab, ha="left", va="center", fontsize=8.2, color=INK_2)
        x += 2.0
    ax.set_xlim(-2.55, n_c)
    ax.set_ylim(ly + 0.5, -0.95)
    # silence tallies, asserted against the table
    silent = sum(lv == X for _, levels, _w in ROWS for lv in levels)
    assert silent == 8 and sum(levels[3] == X for _, levels, _w in ROWS) == 4 and sum(levels[4] == X for _, levels, _w in ROWS) == 3
    return finish(fig, "ch04_empty_cells_map")


if __name__ == "__main__":
    for fn in (fig_effective_breadth, fig_truncation_bias, fig_factor_zoo, fig_capacity, fig_empty_cells):
        fn()
