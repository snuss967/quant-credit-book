"""Figures for Chapter 25 (NLP for Credit Agreements, Indentures & PACER Dockets).

Run:  python3 tools/figures/ch25.py   -> assets/figures/ch25_*.png

Colour use in this chapter: BLUE is the object the figure is about (the amended term, the flow that goes
through, the observed docket path, the true capacity); ORANGE is the contrast case or the structure to
notice (the "after giving effect" reading, the loops, the min cut); NEUTRAL carries everything inactive.
"""
import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from style import *  # noqa: E402,F401,F403  (applies the rcParams on import)

import math  # noqa: E402
from collections import defaultdict, deque  # noqa: E402

import numpy as np  # noqa: E402
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch  # noqa: E402


# --------------------------------------------------------------------------------------------------
# Shared drawing helpers (boxes and arrows in a unit-free data frame; graphviz is not installed)
# --------------------------------------------------------------------------------------------------
def _box(ax, x, y, w, h, text, face="white", edge=NEUTRAL, lw=0.9, fs=7.2, ls="-", weight="normal",
         color=INK, z=3, rounding=1.0):
    ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h, boxstyle=f"round,pad=0,rounding_size={rounding}",
                                linewidth=lw, edgecolor=edge, facecolor=face, linestyle=ls, zorder=z))
    if text:
        ax.text(x, y, text, ha="center", va="center", fontsize=fs, color=color, fontweight=weight,
                zorder=z + 1, linespacing=1.15)


def _edge_point(c, o, hw, hh):
    """Point on the boundary of the box centred c (half sizes hw, hh) in the direction of o."""
    dx, dy = o[0] - c[0], o[1] - c[1]
    s = min(hw / abs(dx) if dx else math.inf, hh / abs(dy) if dy else math.inf)
    return (c[0] + dx * s, c[1] + dy * s)


def _arrow(ax, p0, p1, color=MUTED, lw=1.0, ls="-", rad=0.0, head=True, z=2, ms=8, sa=0, sb=0):
    ax.add_patch(FancyArrowPatch(p0, p1, arrowstyle="-|>" if head else "-", mutation_scale=ms, linewidth=lw,
                                 color=color, linestyle=ls, zorder=z, shrinkA=sa, shrinkB=sb,
                                 connectionstyle=f"arc3,rad={rad}"))


# --------------------------------------------------------------------------------------------------
# Figure 25.1: the definition graph of Listing 25.1 with its two loops and a blast radius (section 25.2.3)
# --------------------------------------------------------------------------------------------------
# Edges u -> v mean "the definition of u uses v". They are what Listing 25.1's matcher returns on its
# synthetic Section 1.01 once the `means` pattern accepts "means," (as in "Pro Forma Basis").
DEFINITION_EDGES = {
    "First Lien Net Leverage Ratio": ["Consolidated EBITDA", "Consolidated First Lien Net Debt"],
    "Consolidated EBITDA": ["Consolidated Net Income", "Pro Forma Basis", "Run-Rate Cost Savings"],
    "Run-Rate Cost Savings": ["Consolidated EBITDA"],
    "Pro Forma Basis": ["Consolidated EBITDA", "Specified Transaction"],
    "Specified Transaction": ["Indebtedness"],
    "Consolidated Net Income": ["Restricted Subsidiary"],
    "Consolidated First Lien Net Debt": ["Collateral", "Indebtedness", "Lien"],
    "Collateral": ["Lenders", "Lien"],
    "Excluded Taxes": ["Lenders"],
    "Restricted Subsidiary": ["Subsidiary", "Unrestricted Subsidiary"],
    "Unrestricted Subsidiary": ["Material Intellectual Property", "Subsidiary"],
    "Material Intellectual Property": ["Restricted Subsidiary"],
    "Indebtedness": [], "Lien": [], "Lenders": [], "Subsidiary": [],
}


def _blast_radius(v, edges):
    rev = defaultdict(set)
    for u, vs in edges.items():
        for w in vs:
            rev[w].add(u)
    seen, q = set(), deque([v])
    while q:
        for u in rev[q.popleft()]:
            if u not in seen:
                seen.add(u)
                q.append(u)
    seen.discard(v)
    return seen


def _sccs(edges):
    """Tiny Tarjan, only to check the loops drawn below are the ones the graph really has."""
    index, low, onst, stack, comps, c = {}, {}, set(), [], [], [0]

    def strong(v):
        index[v] = low[v] = c[0]; c[0] += 1
        stack.append(v); onst.add(v)
        for w in edges[v]:
            if w not in index:
                strong(w); low[v] = min(low[v], low[w])
            elif w in onst:
                low[v] = min(low[v], index[w])
        if low[v] == index[v]:
            comp = set()
            while True:
                w = stack.pop(); onst.discard(w); comp.add(w)
                if w == v:
                    break
            comps.append(frozenset(comp))

    for v in edges:
        if v not in index:
            strong(v)
    return comps


def fig_definition_graph():
    pos = {
        "First Lien Net Leverage Ratio": (50, 93),
        "Run-Rate Cost Savings": (8, 74), "Consolidated EBITDA": (27, 74), "Pro Forma Basis": (46, 74),
        "Consolidated First Lien Net Debt": (70, 74), "Excluded Taxes": (94, 74),
        "Consolidated Net Income": (27, 55), "Specified Transaction": (46, 55), "Collateral": (84, 55),
        "Restricted Subsidiary": (27, 38), "Unrestricted Subsidiary": (27, 24),
        "Material Intellectual Property": (27, 10), "Subsidiary": (7, 24),
        "Indebtedness": (58, 36), "Lien": (75, 36), "Lenders": (94, 36),
    }
    label = {
        "First Lien Net Leverage Ratio": "First Lien Net\nLeverage Ratio", "Consolidated EBITDA": "Consolidated\nEBITDA",
        "Run-Rate Cost Savings": "Run-Rate\nCost Savings", "Pro Forma Basis": "Pro Forma\nBasis",
        "Consolidated First Lien Net Debt": "Consolidated\nFirst Lien\nNet Debt", "Excluded Taxes": "Excluded\nTaxes",
        "Consolidated Net Income": "Consolidated\nNet Income", "Specified Transaction": "Specified\nTransaction",
        "Restricted Subsidiary": "Restricted\nSubsidiary", "Unrestricted Subsidiary": "Unrestricted\nSubsidiary",
        "Material Intellectual Property": "Material\nIntellectual\nProperty",
    }
    amended = "Consolidated EBITDA"
    blast = _blast_radius(amended, DEFINITION_EDGES)
    loops = sorted(sorted(c) for c in _sccs(DEFINITION_EDGES) if len(c) > 1)
    assert len(blast) == 3 and not _blast_radius("Excluded Taxes", DEFINITION_EDGES)
    assert loops == [["Consolidated EBITDA", "Pro Forma Basis", "Run-Rate Cost Savings"],
                     ["Material Intellectual Property", "Restricted Subsidiary", "Unrestricted Subsidiary"]]

    W, H = 14.0, 9.0
    fig, ax = new_figure((7.2, 5.4))
    ax.set_xlim(-1, 102)
    ax.set_ylim(-3, 99)
    ax.axis("off")
    ax.grid(False)

    # loop outlines first (behind everything)
    for (x0, y0, x1, y1) in [(0.5, 68.5, 53.5, 79.5), (15.5, 4.5, 46.0, 43.5)]:
        ax.add_patch(FancyBboxPatch((x0, y0), x1 - x0, y1 - y0, boxstyle="round,pad=0,rounding_size=1.8",
                                    linewidth=1.2, edgecolor=ORANGE, facecolor="none", linestyle=(0, (4, 2.5)),
                                    zorder=1))
    ax.text(1.0, 82.0, "loop 1: the add-back cap", fontsize=7.6, color=INK_2, va="center")
    ax.text(32.0, 1.2, "loop 2: the J.Crew blocker", fontsize=7.6, color=INK_2, va="center", ha="center")

    # edges
    drawn = set()
    for u, vs in DEFINITION_EDGES.items():
        for v in vs:
            pu, pv = pos[u], pos[v]
            if (v, u) in drawn:
                continue                       # mutual pairs are drawn once, as a pair of offset arrows
            mutual = u in DEFINITION_EDGES[v]
            if mutual and pu[1] == pv[1]:      # side by side: two parallel arrows
                for a, b, off in ((u, v, 1.5), (v, u, -1.5)):
                    p0 = (pos[a][0] + math.copysign(W / 2, pos[b][0] - pos[a][0]), pos[a][1] + off)
                    p1 = (pos[b][0] - math.copysign(W / 2, pos[b][0] - pos[a][0]), pos[b][1] + off)
                    _arrow(ax, p0, p1, color=INK_2, lw=1.0, ms=7)
            elif (u, v) == ("Material Intellectual Property", "Restricted Subsidiary"):
                p0 = (pu[0] + W / 2, pu[1] + 1.5)
                p1 = (pv[0] + W / 2, pv[1] - 1.5)
                _arrow(ax, p0, p1, color=INK_2, lw=1.0, rad=0.6, ms=7)
            else:
                p0 = _edge_point(pu, pv, W / 2, H / 2)
                p1 = _edge_point(pv, pu, W / 2, H / 2)
                _arrow(ax, p0, p1, color=INK_2, lw=1.0, ms=7)
            drawn.add((u, v))

    # nodes
    for t, (x, y) in pos.items():
        face, edge, wt = "white", NEUTRAL, "normal"
        if t == amended:
            face, edge, wt = SEQ_BLUE_STEPS[4], BLUE, "bold"
        elif t in blast:
            face, edge = SEQ_BLUE_STEPS[0], BLUE
        _box(ax, x, y, W, H, label.get(t, t), face=face, edge=edge, weight=wt, fs=7.8, lw=1.1 if t in blast or t == amended else 0.9)

    ax.text(94, 83.6, "β = 0: nothing\ndepends on it", fontsize=7.4, color=INK_2, ha="center", va="center",
            linespacing=1.15)
    # legend
    lx, ly = 62.0, 21.0
    _box(ax, lx, ly, 6.5, 4.2, "", face=SEQ_BLUE_STEPS[4], edge=BLUE, lw=1.1, rounding=0.8)
    ax.text(lx + 5, ly, "amended term", fontsize=7.6, color=INK_2, va="center")
    _box(ax, lx, ly - 7, 6.5, 4.2, "", face=SEQ_BLUE_STEPS[0], edge=BLUE, lw=1.1, rounding=0.8)
    ax.text(lx + 5, ly - 7, f"its blast radius, β = {len(blast)}", fontsize=7.6, color=INK_2, va="center")
    ax.add_patch(FancyBboxPatch((lx - 3.25, ly - 14 - 2.1), 6.5, 4.2, boxstyle="round,pad=0,rounding_size=0.8",
                                linewidth=1.2, edgecolor=ORANGE, facecolor="none", linestyle=(0, (4, 2.5))))
    ax.text(lx + 5, ly - 14, "cycle (strongly connected\ncomponent)", fontsize=7.6, color=INK_2, va="center",
            linespacing=1.15)
    ax.text(lx - 3.25, ly - 21.6, "Arrow: the definition of the tail uses the head.\nEvaluate against the arrows.",
            fontsize=7.4, color=MUTED, va="center", linespacing=1.15)
    return finish(fig, "ch25_definition_graph")


# --------------------------------------------------------------------------------------------------
# Figure 25.2: "after giving effect" and capacity levered to add-backs (sections 25.3.3 and 25.3.4)
# --------------------------------------------------------------------------------------------------
def capacity(E, m=4.5, F=900.0, X=75.0, p=0.35):
    return np.maximum(0.0, m * E - F) + np.maximum(X, p * E)


def fig_addback_capacity():
    fig, (a, b) = new_figure("wide", ncols=2)

    # (a) one cap, two readings
    c = np.linspace(0, 0.5, 300)
    before, after = c, c / (1 - c)
    a.fill_between(c * 100, before * 100, after * 100, color=SEQ_BLUE_STEPS[0], linewidth=0, zorder=1)
    a.plot(c * 100, before * 100, color=BLUE, linewidth=LW, zorder=3)
    a.plot(c * 100, after * 100, color=ORANGE, linewidth=LW, zorder=3)
    label_end(a, 50, 50, "Cap on \u2130\u2080 (before)", BLUE, dx=-5, dy=11, ha="right")
    label_end(a, 50, 100, "Cap on \u2130\u2080 + A (after)", ORANGE, dx=-5, dy=-1, ha="right")
    c0 = 0.25
    a.plot([c0 * 100] * 2, [c0 * 100, c0 / (1 - c0) * 100], color=INK_2, linewidth=0.9, zorder=4)
    for yy, col in ((c0 * 100, BLUE), (c0 / (1 - c0) * 100, ORANGE)):
        a.plot([c0 * 100], [yy], "o", color=col, markersize=6, zorder=5)
    a.annotate("25.0% of \u2130\u2080", (c0 * 100, c0 * 100), xytext=(10, -10), textcoords="offset points",
               fontsize=8.5, color=INK_2, ha="left", va="center")
    a.annotate("33.3% of \u2130\u2080:\n8.3 points from\nfour words", (c0 * 100, c0 / (1 - c0) * 100),
               xytext=(2.0, 66), textcoords="data", fontsize=8.5, color=INK_2, ha="left", va="center",
               arrowprops=dict(arrowstyle="-", color=NEUTRAL, linewidth=0.8, shrinkA=2, shrinkB=5))
    a.set_xlim(0, 50)
    a.set_ylim(0, 108)
    a.set_xlabel("Stated cap, c (% of EBITDA)")
    a.set_ylabel("Allowed add-back (% of \u2130\u2080)")
    a.set_title("One cap, two readings")
    note(a, "gap = c²/(1−c)", loc="lower right")

    # (b) capacity vs covenant EBITDA (Halyard)
    E = np.linspace(160, 300, 600)
    K = capacity(E)
    b.plot(E, K, color=BLUE, linewidth=LW, zorder=3)
    E0, A = 200.0, 200.0 * 0.25 / 0.75
    E1 = E0 + A
    # claimed add-backs are 80, the 25% "after" cap binds at 66.7 (Listing 25.2)
    assert abs(E1 - 266.667) < 1e-3
    K0, K1 = float(capacity(E0)), float(capacity(E1))
    assert abs(K0 - 75.0) < 1e-9 and abs(K1 - 393.333) < 1e-3
    for xx, yy in ((E0, K0), (E1, K1)):
        b.plot([xx, xx], [0, yy], color=NEUTRAL, linewidth=0.9, linestyle=(0, (3, 3)), zorder=1)
        b.plot([xx], [yy], "o", color=BLUE, markersize=6, zorder=5)
    b.annotate(f"No add-backs: \\${K0:.0f}mm", (E0, K0), xytext=(163, 150), textcoords="data",
               fontsize=8.5, color=INK_2, ha="left", va="center",
               arrowprops=dict(arrowstyle="-", color=NEUTRAL, linewidth=0.8, shrinkA=2, shrinkB=5))
    b.annotate(f"With \\$66.7mm of add-backs:\n\\${K1:.1f}mm", (E1, K1), xytext=(163, 330), textcoords="data",
               fontsize=8.5, color=INK_2, ha="left", va="center",
               arrowprops=dict(arrowstyle="-", color=NEUTRAL, linewidth=0.8, shrinkA=2, shrinkB=5))
    note(b, "slope 4.85 per \\$1 of \u2130\nabove \\$214mm", loc="upper left")
    b.set_xlim(160, 290)
    b.set_ylim(0, 600)
    b.set_xlabel("Covenant EBITDA, ℰ (\\$mm)")
    b.set_ylabel("Incremental debt capacity, K (\\$mm)")
    b.set_title("Capacity accelerates with EBITDA")
    b.set_xticks([160, 200, 240, 280])
    return finish(fig, "ch25_addback_capacity")


# --------------------------------------------------------------------------------------------------
# Figure 25.3: the J.Crew trapdoor as a minimum cut (section 25.4.2)
# --------------------------------------------------------------------------------------------------
def max_flow_min_cut(arcs, s, t):
    """Edmonds-Karp, as in Listing 25.3. arcs: (u, v, name, capacity). Returns (value, cut arcs)."""
    cap = defaultdict(lambda: defaultdict(float))
    for u, v, _, c in arcs:
        cap[u][v] += c
        cap[v][u] += 0.0
    res = {u: dict(vs) for u, vs in cap.items()}
    value = 0.0
    while True:
        parent, q = {s: None}, deque([s])
        while q and t not in parent:
            u = q.popleft()
            for v, c in res[u].items():
                if c > 1e-12 and v not in parent:
                    parent[v] = u
                    q.append(v)
        if t not in parent:
            break
        path, v = [], t
        while parent[v] is not None:
            path.append((parent[v], v))
            v = parent[v]
        push = min(res[u][v] for u, v in path)
        if math.isinf(push):
            return math.inf, []
        for u, v in path:
            res[u][v] -= push
            res[v][u] += push
        value += push
    reach, q = {s}, deque([s])
    while q:
        u = q.popleft()
        for v, c in res[u].items():
            if c > 1e-12 and v not in reach:
                reach.add(v)
                q.append(v)
    return value, [a for a in arcs if a[0] in reach and a[1] not in reach]


def _jcrew_panel(ax, trapdoor, title):
    arcs = [("s", "N", "non-guarantor investments", 150.0), ("s", "N", "general investments", 100.0),
            ("N", "t", "trapdoor", trapdoor)]
    phi, cut = max_flow_min_cut(arcs, "s", "t")
    open_ = math.isinf(trapdoor)
    if open_:
        assert phi == 250.0 and sorted(a[2] for a in cut) == ["general investments", "non-guarantor investments"]
    else:
        assert phi == 0.0 and [a[2] for a in cut] == ["trapdoor"]

    ax.set_xlim(0, 100)
    ax.set_ylim(0, 40)
    ax.axis("off")
    ax.grid(False)
    ax.set_title(title, loc="left", pad=2)
    xs, xn, xt, y = 11, 50, 89, 20
    bw, bh = 20, 13
    for x, txt in ((xs, "Loan parties\n(source s)"), (xn, "Non-guarantor\nrestricted subs (N)"),
                   (xt, "Unrestricted\nsubs (sink t)")):
        _box(ax, x, y, bw, bh, txt, fs=7.8, lw=1.0, rounding=1.6)

    flow_c = BLUE if open_ else NEUTRAL
    lw1, lw2, lw3 = (3.2, 2.2, 5.4) if open_ else (1.6, 1.6, 1.6)
    gx = (xs + xn) / 2                                    # centre of the s -> N gap
    for rad, lw, yy, txt in ((-0.30, lw1, 34.5, "Non-guarantor investments basket: \\$150mm"),
                             (0.30, lw2, 5.5, "General investments basket: \\$100mm")):
        yo = y + (3.5 if rad < 0 else -3.5)
        _arrow(ax, (xs + bw / 2, yo), (xn - bw / 2, yo), color=flow_c, lw=lw, rad=rad, ms=10)
        ax.text(gx, yy, txt, fontsize=7.8, color=INK_2, ha="center", va="center")
    tx = (xn + xt) / 2                                    # centre of the N -> t gap
    _arrow(ax, (xn + bw / 2, y), (xt - bw / 2, y), color=flow_c, lw=lw3, ms=11)
    ax.text(tx + 3.5, y + 3.2, "Trapdoor", fontsize=7.8, color=INK_2, ha="center", va="bottom", fontweight="bold")
    ax.text(tx + 3.5, y - 3.2, "capacity \u221e" if open_ else "capacity 0", fontsize=7.8, color=INK_2,
            ha="center", va="top")
    # the minimum cut, drawn only across the arcs it severs
    if open_:
        cx, y0, y1, lab_y = gx - 1.8, 9.0, 31.0, 20.0
        ax.plot([cx, cx], [y0, y1], color=ORANGE, linewidth=1.7, linestyle=(0, (4, 2.5)), zorder=6)
        ax.text(cx + 1.6, lab_y, "min cut", fontsize=8, color=INK_2, va="center", ha="left", fontweight="bold")
        ax.text(99, 5.5, "\u03a6 = 150 + 100 = \\$250mm", fontsize=9, color=INK, ha="right", va="center",
                fontweight="bold")
    else:
        cx = xn + bw / 2 + 4.5
        ax.plot([cx, cx], [11.0, 29.0], color=ORANGE, linewidth=1.7, linestyle=(0, (4, 2.5)), zorder=6)
        ax.text(cx, 8.0, "min cut", fontsize=8, color=INK_2, va="center", ha="center", fontweight="bold")
        ax.text(99, 5.5, "\u03a6 = 0", fontsize=9, color=INK, ha="right", va="center", fontweight="bold")


def fig_jcrew_mincut():
    fig, (a, b) = new_figure((7.0, 4.9), nrows=2)
    _jcrew_panel(a, 0.0, "Trapdoor read as zero: the cut sits on the trapdoor")
    _jcrew_panel(b, math.inf, "Trapdoor read as unbounded: the cut moves upstream onto the two baskets")
    return finish(fig, "ch25_jcrew_mincut")


# --------------------------------------------------------------------------------------------------
# Figure 25.4: one token versus $200mm (sections 25.5.1, Listing 25.4, Exercise 4)
# --------------------------------------------------------------------------------------------------
def _sci(v):
    mant, exp = f"{v:.1e}".split("e")
    sup = str.maketrans("-0123456789", "\u207b\u2070\u00b9\u00b2\u00b3\u2074\u2075\u2076\u2077\u2078\u2079")
    return f"{mant} \u00d7 10{str(int(exp)).translate(sup)}"


def fig_token_vs_capacity():
    d, n = 10_000, 150_000
    lam = n / d
    xx = d * (lam ** 2 + lam)                  # E ||x||^2 for 150,000 tokens spread uniformly over 10,000 words
    fig, (a, b) = new_figure("wide", ncols=2)

    k = np.logspace(0, 3, 300)
    a.loglog(k, k ** 2 / xx, color=ORANGE, linewidth=LW, zorder=3)
    a.axhline(0.01, color=NEUTRAL, linewidth=0.9, linestyle=(0, (3, 3)), zorder=1)
    a.annotate("1% move in cosine", (1.2, 0.01), xytext=(0, -4), textcoords="offset points", fontsize=8,
               color=INK_2, ha="left", va="top")
    k1 = 1.0
    a.plot([k1], [k1 ** 2 / xx], "o", color=ORANGE, markersize=6, zorder=5)
    a.annotate("One swapped ratio:\n1 \u2212 cos = " + _sci(1 / xx), (k1, 1 / xx), xytext=(12, -4),
               textcoords="offset points", fontsize=8.5, color=INK_2, ha="left", va="top")
    kc = math.sqrt(0.01 * xx)
    a.plot([kc], [0.01], "o", color=ORANGE, markersize=6, zorder=5)
    a.annotate(f"{kc:.0f} occurrences\nall amended", (kc, 0.01), xytext=(-8, 8), textcoords="offset points",
               fontsize=8.5, color=INK_2, ha="right", va="bottom")
    a.set_xlim(0.8, 1000)
    a.set_ylim(1e-8, 1.5)
    a.set_xlabel("Occurrences of “4.50” that are amended, k")
    a.set_ylabel("Token diff: 1 − cosine similarity")
    a.set_title("What a bag-of-words diff sees")
    a.grid(axis="y")

    # (b) what the capacity vector sees
    E, F = 266.667, 900.0
    m = np.linspace(4.0, 6.0, 200)
    cap_ratio = np.maximum(0.0, m * E - F)
    b.plot(m, cap_ratio, color=BLUE, linewidth=LW, zorder=3)
    c0, c1 = 4.5 * E - F, 5.25 * E - F
    assert abs(c0 - 300.0) < 0.1 and abs(c1 - c0 - 200.0) < 0.1
    for mm, cc in ((4.5, c0), (5.25, c1)):
        b.plot([mm, mm], [0, cc], color=NEUTRAL, linewidth=0.9, linestyle=(0, (3, 3)), zorder=1)
        b.plot([mm], [cc], "o", color=BLUE, markersize=6, zorder=5)
    b.annotate("4.50x:\n\\$300mm", (4.5, c0), xytext=(9, -9), textcoords="offset points", fontsize=8.5,
               color=INK_2, ha="left", va="top")
    b.annotate("5.25x:\n\\$500mm", (5.25, c1), xytext=(-8, 8), textcoords="offset points", fontsize=8.5,
               color=INK_2, ha="right", va="bottom")
    _arrow(b, (4.95, c0), (4.95, c1), color=INK_2, lw=1.1, ms=8, sa=1, sb=1)
    b.text(4.99, (c0 + c1) / 2, "+\\$200mm", fontsize=9, color=INK, fontweight="bold", ha="left", va="center")
    b.set_xlim(4.0, 6.0)
    b.set_ylim(0, 770)
    b.set_xlabel("Permitted first-lien net leverage, m (x)")
    b.set_ylabel("Ratio-basket capacity (\\$mm)")
    b.set_title("What the capacity vector sees")
    note(b, "ℰ = \\$266.7mm, first-lien net debt \\$900mm", loc="upper left")
    return finish(fig, "ch25_token_vs_capacity")


# --------------------------------------------------------------------------------------------------
# Figure 25.5: the docket as a state machine, with the Hughes path (section 25.7.2)
# --------------------------------------------------------------------------------------------------
def fig_docket_state_machine():
    fig, ax = new_figure((7.0, 4.0))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 62)
    ax.axis("off")
    ax.grid(False)

    states = ["Quiet", "Organized", "Contested", "Standstill", "Plan", "Confirmed"]
    triggers = ["first Rule 2019\nstatement", "exclusivity,\nstanding, or\nlien challenge",
                "stipulated stay\nor mediation", "plan filed", "confirmation\norder"]
    bw, bh, gap = 13.6, 11.0, 3.5
    step = bw + gap
    xs = [bw / 2 + 0.6 + i * step for i in range(6)]
    y = 54.0
    hughes = {1, 2, 3}                                 # states Hughes passed through
    for i, (x, st) in enumerate(zip(xs, states)):
        on = i in hughes
        _box(ax, x, y, bw, bh, st, face=SEQ_BLUE_STEPS[0] if on else "white", edge=BLUE if on else NEUTRAL,
             lw=1.3 if on else 0.9, fs=8.6, weight="bold" if on else "normal", rounding=1.6)
        if st == "Confirmed":                          # absorbing state: second outline
            _box(ax, x, y, bw - 1.6, bh - 1.6, "", edge=NEUTRAL, lw=0.8, z=2, rounding=1.2, face="none")
    for i in range(5):
        on = i in (1, 2)                               # Organized->Contested and Contested->Standstill observed
        x0, x1 = xs[i] + bw / 2, xs[i + 1] - bw / 2
        _arrow(ax, (x0, y), (x1, y), color=BLUE if on else MUTED, lw=2.2 if on else 1.1, ms=9 if on else 7)
        ax.text(xs[i] + 8.6, y - bh / 2 - 1.6, triggers[i], fontsize=7.6, color=INK_2, ha="center",
                va="top", fontstyle="italic", linespacing=1.15)

    # Hughes docket entries as cards under the three states it passed through
    cy, ch, cw = 22.0, 17.0, 16.0
    cards = [(1, "Doc. 154\n2026-08-10", "Verified Statement\nof Noteholders\n(Rule 2019)"),
             (2, "Doc. 320\n2026-09-10", "Emergency motion\nto terminate\nexclusive periods"),
             (3, "Doc. 369\n2026-09-20", "Stipulated order\nstaying litigation\nand investigations")]
    for i, head, body in cards:
        x = xs[i]
        ax.plot([x, x], [y - bh / 2, cy + ch / 2], color=BLUE, linewidth=0.9, zorder=1)
        _box(ax, x, cy, cw, ch, "", edge=BLUE, lw=0.9, rounding=1.2)
        ax.text(x, cy + 4.6, head, fontsize=7.6, color=INK, fontweight="bold", ha="center", va="center",
                linespacing=1.15, zorder=5)
        ax.text(x, cy - 3.6, body, fontsize=7.4, color=INK_2, ha="center", va="center", linespacing=1.15, zorder=5)
    # dwell brackets
    for (i, j, txt) in ((1, 2, "31 days"), (2, 3, "10 days")):
        yb = 8.4
        ax.annotate("", (xs[j], yb), (xs[i], yb), arrowprops=dict(arrowstyle="<|-|>", color=BLUE, linewidth=1.3,
                                                                  mutation_scale=7, shrinkA=0, shrinkB=0))
        ax.text((xs[i] + xs[j]) / 2, yb, txt, fontsize=8.4, color=INK, fontweight="bold", ha="center",
                va="center", bbox=dict(boxstyle="round,pad=0.2", facecolor="white", edgecolor="none"))
        for xx in (xs[i], xs[j]):
            ax.plot([xx, xx], [cy - ch / 2, yb + 1.5], color=NEUTRAL, linewidth=0.8, linestyle=(0, (2, 2)), zorder=1)
    ax.text(0.6, 1.2, "Hughes Satellite Systems Corp., Bankr. S.D. Tex. No. 26-90739", fontsize=7.6, color=INK_2,
            fontweight="bold", va="center", ha="left")
    ax.text(99.4, 27.5, "Blue: the path the three entries show.\nGray: states before or after it.", fontsize=7.6,
            color=INK_2, ha="right", va="center", linespacing=1.2)
    ax.text(99.4, 12.5, r"Rate estimate: $\hat{q}_{ab} = N_{ab}\,/\,T_a$," + "\nunfinished spells count in $T_a$",
            fontsize=7.6, color=INK_2, ha="right", va="center", linespacing=1.2)
    return finish(fig, "ch25_docket_state_machine")


if __name__ == "__main__":
    fig_definition_graph()
    fig_addback_capacity()
    fig_jcrew_mincut()
    fig_token_vs_capacity()
    fig_docket_state_machine()
