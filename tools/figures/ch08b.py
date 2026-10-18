"""Chapter 8-B figures: The Risk Model You Run Every Morning.

Run:  python3 tools/figures/ch08b.py      (writes assets/figures/ch08b_*.png)

Nothing here is market data. Every figure is computed from a model the chapter states, or drawn from
the chapter's own numbers, so every caption says "Illustrative":
  1. ch08b_factor_tree          the factor tree with Tuesday's exposures on each branch (8B.2)
  2. ch08b_mixture_traps        Halvorsen's one-day loss as a mixture; the sqrt(h) shortcut (8B.6)
  3. ch08b_stress_library       the seven scenarios, factor-and-idiosyncratic bar and jump bar (8B.7)
  4. ch08b_backtest_exceptions  exceptions as coin flips, and the clustering (8B.8)
  5. ch08b_limit_sheet          Tuesday's report against the soft and hard thresholds (8B.9)

Colour roles are fixed across the chapter:
  BLUE   = the Gaussian layer (factors and idiosyncratic residuals)
  ORANGE = the jump layer (JTD)
  VIOLET = the shortcut / the folded-in alternative (one Gaussian with the jump's variance; sqrt(h))
  INK / NEUTRAL = the honest total, thresholds and reference levels
  STATUS (grey / amber / red) = limit state, always with a text label

The Tuesday book (section 8B.9's illustrative $400mm high-yield book) is defined once, below, and
feeds the tree, the stress library and the limit sheet, so the three figures agree with each other.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from style import *  # noqa: E402,F401,F403
import numpy as np  # noqa: E402
from matplotlib.lines import Line2D  # noqa: E402
from matplotlib.patches import FancyBboxPatch, Rectangle  # noqa: E402
from matplotlib.ticker import FuncFormatter  # noqa: E402
from scipy.optimize import brentq  # noqa: E402
from scipy.stats import beta as beta_dist, binom, norm  # noqa: E402

MINUS = "−"
C_GAUSS, C_JUMP, C_SHORT = BLUE, ORANGE, VIOLET
C_IDIO = SEQ_BLUE_STEPS[2]          # lighter blue: Gaussian layer, idiosyncratic leaf
C_OK, C_SOFT, C_HARD = NEUTRAL, STATUS["warning"], STATUS["critical"]

# --------------------------------------------------------------------------------------------
# Tuesday's book (illustrative $400mm high-yield book). Units: $mm unless stated.
# --------------------------------------------------------------------------------------------
KEYS = ["2y", "5y", "10y", "30y"]
DV01_BOND = dict(zip(KEYS, [10, 18, 22, 6]))        # $k per bp, the long bonds
DV01_FUT = dict(zip(KEYS, [16, 9, 9, 8]))           # $k per bp, Treasury-futures hedge
DV01_NET = {m: DV01_BOND[m] - DV01_FUT[m] for m in KEYS}   # -6, +9, +13, -2 (band +-15 soft, +-25 hard)

# loss for a +10% relative widening of the cell (the limit sheet's DTS line); soft 1.2, hard 1.5
CELLS = [("B Industrials", "B", 1.62), ("B Consumer", "B", 0.98), ("B Healthcare", "B", 0.58),
         ("BB Energy", "BB", 0.77), ("BB Industrials", "BB", 0.71),
         ("CCC Retail", "CCC", 0.36), ("CCC Industrials", "CCC", 0.21)]
E_RATING = {r: sum(v for _, g, v in CELLS if g == r) for r in ("BB", "B", "CCC")}   # 1.48, 3.18, 0.57
E_HEDGE = 4.8          # CDX HY and HY-ETF shorts: gain per +10% move of the HY index factor
E_LIQ = 0.35           # per 1 sigma adverse liquidity-factor day
E_PC1 = 0.30           # per 1 sigma adverse common-residual day
E_ETF, E_STRUCT, E_CDX = 0.14, 0.06, 0.025   # basis: $mm per ETF-NAV point, structured point, CDX-cash bp
SIGMA_IDIO = 0.38      # one-day sigma of the book's idiosyncratic P&L
JTD_CLASS = {"sub80": 9.0, "cb": 14.0, "bb": 6.0, "bank": 4.15}   # issuer JTD by class (Halvorsen is 7.56 of sub80)


def gaussian_book_loss(sc):
    """Factor-and-idiosyncratic loss of Tuesday's book under a scenario's factor shocks ($mm)."""
    sbb, sb, sccc = sc["s"]
    spread = (E_RATING["BB"] * sbb + E_RATING["B"] * sb + E_RATING["CCC"] * sccc) / 10
    s_hy = (E_RATING["BB"] * sbb + E_RATING["B"] * sb) / (E_RATING["BB"] + E_RATING["B"])
    hedge = E_HEDGE * s_hy / 10 * sc["rho"]
    rates = sum((sc["H"] * DV01_BOND[m] - DV01_FUT[m]) * dy for m, dy in zip(KEYS, sc["dy"])) / 1000
    liq = E_LIQ * sc["liq"]
    basis = E_ETF * sc["etf"] + E_STRUCT * sc["struct"] + E_CDX * sc["cdx"]
    idio = 2.33 * SIGMA_IDIO * sc["idio"]
    return spread - hedge + rates + liq + basis + idio


def jump_overlay(sc):
    return sum(JTD_CLASS[c] * q for c, q in sc["q"].items())


# the seven scenarios (Table 8-B.3's factor translations; the numbers are the desk's illustrative calibration)
SCENARIOS = [
    dict(name="March 2020", s=(100, 110, 120), rho=1.0, H=1.0, dy=(0, 0, 0, 0), liq=6, etf=5, struct=0, cdx=0,
         idio=3.0, q=dict(sub80=.06, cb=.02, bb=.005, bank=.005)),
    dict(name="2022 rates year", s=(60, 60, 60), rho=1.0, H=1.1, dy=(250, 245, 236, 230), liq=1, etf=0, struct=0,
         cdx=0, idio=1.5, q=dict(sub80=.03, cb=.01, bb=.002, bank=.002)),
    dict(name="LDI BWIC week (Oct 2022)", s=(10, 10, 10), rho=1.0, H=1.0, dy=(0, 0, 0, 0), liq=5, etf=0, struct=8,
         cdx=0, idio=1.5, q=dict(sub80=.01, cb=.005, bb=.001, bank=.001)),
    dict(name="SVB (Mar 2023)", s=(10, 10, 10), rho=1.0, H=0.7, dy=(-100, -85, -70, -35), liq=2, etf=0, struct=0,
         cdx=0, idio=1.8, q=dict(sub80=.02, cb=.01, bb=.002, bank=1.0)),
    dict(name="April 2025", s=(35, 35, 23), rho=1.0, H=1.0, dy=(0, 0, 0, 0), liq=3, etf=0, struct=0, cdx=15,
         idio=2.5, q=dict(sub80=.08, cb=.025, bb=.005, bank=.005)),
    dict(name="2026 CCC decompression", s=(0, 0, 30), rho=1.0, H=1.0, dy=(0, 0, 0, 0), liq=1, etf=0, struct=0,
         cdx=0, idio=1.18, q=dict(sub80=.35, cb=.04, bb=.002, bank=.002)),
    dict(name="Hedge basis widens with spreads\n(constructed)", s=(40, 40, 40), rho=0.5, H=0.5,
         dy=(-100, -100, -100, -100), liq=1, etf=0, struct=0, cdx=0, idio=1.5,
         q=dict(sub80=0, cb=0, bb=0, bank=0)),
]
for _sc in SCENARIOS:
    _sc["gauss"], _sc["jump"] = gaussian_book_loss(_sc), jump_overlay(_sc)
    _sc["total"] = _sc["gauss"] + _sc["jump"]
WORST_STRESS = max(sc["total"] for sc in SCENARIOS)


def _chip(ax, x, y, text, fill, fg, w=9.5, h=3.6, fs=7.5):
    ax.add_patch(FancyBboxPatch((x, y - h / 2), w, h, boxstyle="round,pad=0,rounding_size=0.8",
                                facecolor=fill, edgecolor="none", zorder=4))
    ax.text(x + w / 2, y, text, ha="center", va="center", fontsize=fs, color=fg, fontweight="bold", zorder=5)


# --------------------------------------------------------------------------------------------
# Figure 1  The factor tree (8B.2)
# --------------------------------------------------------------------------------------------
def fig_factor_tree():
    fig, ax = new_figure((7.0, 5.6))
    fig.set_layout_engine("none")
    ax.set_position([0.0, 0.0, 1.0, 1.0])
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis("off")
    ax.grid(False)

    rows = [
        # (name, loading, colour, height, exposure lines)
        ("Key-rate DV01s", r"$-\,\mathrm{KRD}_{i,m}\,\Delta y_m$", C_GAUSS, 11,
         ["Net DV01, $k per bp (band ±15 soft, ±25 hard):",
          f"2y {MINUS}6    5y +9    10y +13    30y {MINUS}2"]),
        ("Rating × sector spread cells", r"$-\,\mathrm{DTS}_i\,b_{g(i),k}\,F_k$", C_GAUSS, 17,
         ["$mm lost if the cell widens 10% (soft 1.2, hard 1.5):",
          ("B Industrials 1.62", "HARD", C_HARD, "white"),
          "B Consumer 0.98    B Healthcare 0.58",
          "BB Energy 0.77    BB Industrials 0.71",
          "CCC Retail 0.36    CCC Industrials 0.21"]),
        ("Liquidity", r"$\beta^{L}_i\,F^{L}$", C_GAUSS, 8,
         ["$0.35mm per 1σ day of the liquidity factor"]),
        ("Common residual (§8.8)", r"$\beta^{C}_i\,F^{C}$", C_GAUSS, 8,
         ["$0.30mm per 1σ day of the first residual component"]),
        ("Basis: CDX, ETF, futures", r"$\sum_j \beta^{B}_{i,j}\,F^{B}_j$", C_GAUSS, 11,
         ["CDX–cash \\$25k per bp    ETF–NAV \\$140k per point",
          "Treasury futures–cash curve $40k per bp"]),
        ("Issuer residual", r"$\epsilon_{i}$, by rating × price bucket", C_IDIO, 8,
         ["Book's one-day idiosyncratic σ: $0.38mm"]),
        ("Jump layer", r"$\mathbf{1}\{\tau_i\leq h\}\,\mathrm{JTD}_i$, path by path", C_JUMP, 14,
         ["Issuer JTD, top ten ($mm):",
          ("Halvorsen 7.56", "SOFT", C_SOFT, INK),
          "bank holdco 4.15    Brambleworth 2.20",
          "seven more, each \u2264 1.9"]),
    ]
    gap, gap_group, top = 2.0, 3.0, 96.0
    y = top
    centers = []
    for k, (name, loading, col, h, lines) in enumerate(rows):
        if k == 5:
            y -= gap_group - gap
        y0 = y - h
        ax.add_patch(FancyBboxPatch((19, y0), 31, h, boxstyle="round,pad=0,rounding_size=0.8",
                                    facecolor="#f6f5f2", edgecolor=NEUTRAL, linewidth=0.8, zorder=2))
        ax.add_patch(Rectangle((19, y0), 2.0, h, facecolor=col, edgecolor="none", zorder=3))
        ax.text(22.4, y - h * 0.30, name, fontsize=8.6, color=INK, fontweight="bold", va="center", zorder=4)
        ax.text(22.4, y - h * 0.70, loading, fontsize=8.3, color=INK_2, va="center", zorder=4)
        n = len(lines)
        for j, ln in enumerate(lines):
            yy = y - h / 2 + (n - 1) * 1.55 - j * 3.1 if n > 1 else y - h / 2
            chip = None
            if isinstance(ln, tuple):
                ln, *chip = ln
            t = ax.text(53, yy, ln, fontsize=8, color=INK, va="center", zorder=4)
            if chip:
                bb = t.get_window_extent(fig.canvas.get_renderer()).transformed(ax.transData.inverted())
                _chip(ax, bb.x1 + 1.2, yy, chip[0], chip[1], chip[2], w=6.8, h=3.0)
        centers.append(y - h / 2)
        y = y0 - gap
    # connectors from the root to every row
    trunk_x, root_x1 = 15.5, 12.5
    mid = (centers[0] + centers[-1]) / 2
    ax.add_patch(FancyBboxPatch((1, mid - 7), root_x1 - 1, 14, boxstyle="round,pad=0,rounding_size=0.8",
                                facecolor="#f6f5f2", edgecolor=INK_2, linewidth=1.0, zorder=2))
    ax.text((1 + root_x1) / 2, mid + 2.2, r"$r_{i,t}$", fontsize=10.5, ha="center", va="center", color=INK, zorder=4)
    ax.text((1 + root_x1) / 2, mid - 2.6, "daily return\nof bond i", fontsize=7.6, ha="center", va="center",
            color=INK_2, zorder=4, linespacing=1.15)
    ax.plot([root_x1, trunk_x], [mid, mid], color=INK_2, lw=1.0, zorder=1)
    ax.plot([trunk_x, trunk_x], [centers[0], centers[-1]], color=INK_2, lw=1.0, zorder=1)
    for c in centers:
        ax.plot([trunk_x, 19], [c, c], color=INK_2, lw=1.0, zorder=1)
    # legend
    ly = 1.6
    for x0, col, txt in [(1.0, C_GAUSS, "Gaussian layer: factors shared by every bond"),
                         (44.5, C_IDIO, "Gaussian layer: leftover"),
                         (70.0, C_JUMP, "Jump layer: charged once")]:
        ax.add_patch(Rectangle((x0, ly - 1.0), 2.0, 2.0, facecolor=col, edgecolor="none"))
        ax.text(x0 + 3.0, ly, txt, fontsize=8, color=INK_2, va="center")
    return finish(fig, "ch08b_factor_tree")


# --------------------------------------------------------------------------------------------
# Figure 2  The mixture and the square-root-of-time shortcut (8B.6)
# --------------------------------------------------------------------------------------------
def _halvorsen_J(n=800):
    u = (np.arange(n) + 0.5) / n
    return 12 * (0.78 - beta_dist.ppf(u, 0.6, 3.4))        # $mm loss given default, recovery ~ Beta(0.6, 3.4)


def _mix_sf(x, sd, p, J):
    """P(L > x) for L = N(0, sd^2) + 1{default} * J, J a fixed number or an equally weighted sample."""
    x = np.asarray(x, dtype=float)
    J = np.atleast_1d(J)
    d = norm.sf((x[..., None] - J) / sd).mean(axis=-1)
    return (1 - p) * norm.sf(x / sd) + p * d


def _var_es(sd, p, J, alpha=0.99, hi=60.0):
    f = lambda x: float(_mix_sf(x, sd, p, J))
    q = brentq(lambda x: f(x) - (1 - alpha), 0.0, hi)
    xs = np.linspace(q, q + 12 * sd + J.max() * 1.0 + 5, 4001)
    es = q + np.trapezoid(_mix_sf(xs, sd, p, J), xs) / (1 - alpha)
    return q, es


def fig_mixture_traps():
    fig, (a, b) = new_figure((7.0, 3.7), ncols=2, gridspec_kw={"width_ratios": [1.05, 1]})
    # ---- left: Halvorsen's one-day loss, exceedance probability on log-log axes
    p1 = 1 - np.exp(-0.25 / 252)                       # 0.099%
    J = _halvorsen_J()
    sd_g = 0.12
    sd_blend = float(np.sqrt(0.12 ** 2 + 0.2378 ** 2))  # chapter: sqrt(0.12^2 + 0.24^2), about 0.27
    sd_blend = float(np.sqrt(sd_g ** 2 + (np.sqrt(p1 * (1 - p1)) * 7.56) ** 2))
    x = np.logspace(np.log10(0.04), np.log10(12), 500)
    sf_mix = _mix_sf(x, sd_g, p1, J)
    sf_blend = norm.sf(x / sd_blend)
    a.plot(x, sf_blend, color=C_SHORT, linewidth=LW, linestyle=(0, (4, 2.5)), zorder=3)
    a.plot(x, sf_mix, color=INK, linewidth=LW + 0.3, zorder=4)
    a.axhline(0.01, color=NEUTRAL, linewidth=0.9, zorder=1)
    a.set_xscale("log")
    a.set_yscale("log")
    a.set_xlim(0.04, 14)
    a.set_ylim(2e-5, 1.0)
    a.set_xticks([0.1, 0.3, 1, 3, 10])
    a.set_xticklabels(["0.1", "0.3", "1", "3", "10"])
    a.xaxis.set_minor_formatter(FuncFormatter(lambda v, _: ""))
    a.set_yticks([1, 0.1, 0.01, 0.001, 0.0001])
    a.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{100 * v:g}%"))
    a.yaxis.set_minor_formatter(FuncFormatter(lambda v, _: ""))
    a.set_xlabel("One-day loss on Halvorsen ($mm)")
    a.set_ylabel("Probability the loss exceeds x")
    var_h, es_h = _var_es(sd_g, p1, J)
    var_b = norm.isf(0.01) * sd_blend
    a.plot([var_h], [0.01], "o", color=INK, markersize=6, markerfacecolor="white", markeredgewidth=1.5, zorder=6)
    a.plot([var_b], [0.01], "o", color=C_SHORT, markersize=6, markerfacecolor="white", markeredgewidth=1.5, zorder=6)
    a.annotate(f"VaR {var_h:.2f}\nES {es_h:.2f}", (var_h, 0.01), xytext=(-6, -6), textcoords="offset points",
               ha="right", va="top", fontsize=8.3, color=INK_2)
    a.annotate(f"VaR {var_b:.2f}", (var_b, 0.01), xytext=(7, 7), textcoords="offset points",
               ha="left", va="bottom", fontsize=8.3, color=INK_2)
    a.annotate("1% line", (0.045, 0.01), xytext=(0, 3), textcoords="offset points", ha="left", va="bottom",
               fontsize=8, color=MUTED)
    a.plot([2.6], [p1], "o", color=INK, markersize=4, zorder=6)
    a.annotate("default plateau:\n0.099% of days,\nmean loss $7.56mm", (2.6, p1), xytext=(0, -8),
               textcoords="offset points", ha="center", va="top", fontsize=8.3, color=INK_2)
    x_dot = 1.07
    a.plot([x_dot], [3e-5], "o", color=C_SHORT, markersize=4, zorder=6)
    a.annotate("one Gaussian,\nvariance folded in", (x_dot, 3e-5), xytext=(-6, 0),
               textcoords="offset points", ha="right", va="center", fontsize=8.3, color=INK_2)
    # ---- right: ES on the mixture divided by sqrt(h) times the one-day ES
    hs = np.arange(1, 15.01, 0.25)
    books = [("A", 20.0, 0.0015, "Table 8-B.2 book\n(JTD $20mm, 0.15% a day)", "-", 1.9),
             ("B", 8.0, 0.0020, "Exercise 2 book\n(JTD $8mm, 0.2% a day)", (0, (4, 2.5)), 1.9)]
    res = {}
    for key, jtd, pd1, label, ls, lw in books:
        es_r, var_r = [], []
        base = None
        for h in hs:
            ph = 1 - np.exp(-pd1 * h)
            v, e = _var_es(np.sqrt(h), ph, np.array([jtd]), hi=jtd + 20)
            if base is None:
                base = (v, e)
            es_r.append(e / (np.sqrt(h) * base[1]))
            var_r.append(v / (np.sqrt(h) * base[0]))
        res[key] = (np.array(es_r), np.array(var_r))
        b.plot(hs, res[key][0], color=C_JUMP, linewidth=lw, linestyle=ls, zorder=4)
    b.plot(hs, res["A"][1], color=C_JUMP, linewidth=1.1, linestyle=(0, (1, 1.6)), zorder=3)
    b.axhline(1.0, color=C_SHORT, linewidth=1.2, linestyle=(0, (4, 2.5)), zorder=2)
    b.set_xlim(1, 15)
    b.set_ylim(0.6, 3.6)
    b.set_xticks([1, 5, 10, 15])
    b.set_xlabel("Horizon h (days)")
    b.set_ylabel("Mixture \u00f7 (\u221ah \u00d7 one-day figure)")
    b.axvline(10, color=NEUTRAL, linewidth=0.8, zorder=1)
    b.annotate("10 days", (10, 0.62), xytext=(3, 0), textcoords="offset points", fontsize=8, color=MUTED, va="bottom")
    iA = int(np.where(hs == 10)[0][0])
    eA, eB = res["A"][0], res["B"][0]
    for arr, dy in ((eA, 7), (eB, -8)):
        b.plot([10], [arr[iA]], "o", color=C_JUMP, markersize=5, zorder=6)
        b.annotate(f"{arr[iA]:.2f}\u00d7", (10, arr[iA]), xytext=(6, dy), textcoords="offset points",
                   ha="left", va="center", fontsize=8.3, color=INK_2)
    handles = [Line2D([0], [0], color=C_JUMP, linewidth=1.9),
               Line2D([0], [0], color=C_JUMP, linewidth=1.9, linestyle=(0, (4, 2.5))),
               Line2D([0], [0], color=C_JUMP, linewidth=1.1, linestyle=(0, (1, 1.6))),
               Line2D([0], [0], color=C_SHORT, linewidth=1.2, linestyle=(0, (4, 2.5)))]
    b.legend(handles, ["ES, Table 8-B.2 book", "ES, Exercise 2 book", "VaR, Table 8-B.2 book", "\u221ah rule (ratio = 1)"],
             loc="upper left", frameon=False, fontsize=8.3, handlelength=2.4, borderaxespad=0.2, labelspacing=0.3)
    print("mixture figure:", f"Halvorsen VaR {var_h:.3f}, ES {es_h:.3f}, folded sd {sd_blend:.3f}, folded VaR {var_b:.3f};",
          f"ES ratio at 10d: A {res['A'][0][iA]:.2f}, B {res['B'][0][iA]:.2f}; VaR ratio A {res['A'][1][iA]:.2f}")
    return finish(fig, "ch08b_mixture_traps")


# --------------------------------------------------------------------------------------------
# Figure 3  The stress library (8B.7)
# --------------------------------------------------------------------------------------------
def fig_stress_library():
    fig, ax = new_figure((7.0, 4.1))
    n = len(SCENARIOS)
    ypos = np.arange(n)[::-1].astype(float)
    ypos[-1] -= 0.45                          # set the constructed scenario slightly apart
    bw = 0.34
    for sc, y in zip(SCENARIOS, ypos):
        ax.barh(y + bw / 2 + 0.02, sc["gauss"], height=bw, color=C_GAUSS, zorder=3)
        ax.barh(y - bw / 2 - 0.02, sc["jump"], height=bw, color=C_JUMP, zorder=3)
        ax.text(sc["gauss"] + 0.2, y + bw / 2 + 0.02, f"{sc['gauss']:.1f}", va="center", fontsize=8.3, color=INK_2)
        ax.text(sc["jump"] + 0.2, y - bw / 2 - 0.02, f"{sc['jump']:.1f}" if sc["jump"] > 0 else "0", va="center",
                fontsize=8.3, color=INK_2)
        ax.text(20.0, y, f"total {sc['total']:.1f}", va="center", ha="right", fontsize=8.5, color=INK)
    ax.set_yticks(ypos)
    ax.set_yticklabels([sc["name"] for sc in SCENARIOS])
    ax.tick_params(axis="y", length=0)
    ax.set_xlim(0, 20)
    ax.set_xticks(range(0, 17, 2))
    ax.set_ylim(ypos.min() - 0.6, ypos.max() + 0.6)
    ax.set_xlabel("Loss on Tuesday's book ($mm)")
    ax.grid(axis="y", visible=False)
    ax.grid(axis="x", visible=True)
    ax.set_axisbelow(True)
    ax.axvline(0, color=NEUTRAL, linewidth=0.8)
    ax.legend(handles=[Rectangle((0, 0), 1, 1, color=C_GAUSS), Rectangle((0, 0), 1, 1, color=C_JUMP)],
              labels=["Factors and idiosyncratic (Gaussian layer)", "Jump-to-default overlay"],
              loc="lower center", bbox_to_anchor=(0.45, 1.0), ncol=2, frameon=False, fontsize=8.3,
              handlelength=1.1, handleheight=0.9, columnspacing=1.8)
    ax.spines["left"].set_visible(False)
    print("stress library:")
    for sc in SCENARIOS:
        print(f"   {sc['name'].splitlines()[0]:28s} gauss {sc['gauss']:5.2f}  jump {sc['jump']:5.2f}  total {sc['total']:5.2f}")
    return finish(fig, "ch08b_stress_library")


# --------------------------------------------------------------------------------------------
# Figure 4  The backtest (8B.8)
# --------------------------------------------------------------------------------------------
def fig_backtest():
    n, p = 250, 0.01
    fig = plt.figure(figsize=(7.0, 4.9), layout="constrained")
    gs = fig.add_gridspec(2, 2, height_ratios=[1, 3.1])
    top = fig.add_subplot(gs[0, :])
    a = fig.add_subplot(gs[1, 0])
    b = fig.add_subplot(gs[1, 1])
    # ---- top: the seven exceptions on the 250-day calendar (three in a row, two in a row, two isolated)
    days = {"isolated": [71, 152], "three in a row": [235, 236, 237], "two in a row": [243, 244]}
    top.set_xlim(0, 250)
    top.set_ylim(0, 1)
    top.hlines(0.12, 0, 250, color=NEUTRAL, linewidth=1.0)
    for k, ds in days.items():
        for d in ds:
            top.vlines(d, 0.12, 0.62, color=C_HARD, linewidth=2.2)
    top.annotate("isolated", (71, 0.62), xytext=(0, 4), textcoords="offset points", ha="center", fontsize=8.3,
                 color=INK_2)
    top.annotate("isolated", (152, 0.62), xytext=(0, 4), textcoords="offset points", ha="center", fontsize=8.3,
                 color=INK_2)
    top.annotate("3 in a row (the Halvorsen gap),\nthen 2 in a row", (244, 0.62), xytext=(4, 4),
                 textcoords="offset points", ha="right", fontsize=8.3, color=INK_2)
    top.set_yticks([])
    top.grid(False)
    top.spines["left"].set_visible(False)
    top.set_xlabel("Trading day in the trailing 250 (red = a day the loss exceeded the 99% VaR)")
    # ---- bottom left: the count under a correct model
    xs = np.arange(0, 13)
    pm = binom.pmf(xs, n, p)
    cols = [C_OK if x <= 6 else C_HARD for x in xs]
    a.bar(xs, 100 * pm, color=cols, width=0.78, zorder=3)
    a.set_xlim(-0.7, 12.7)
    a.set_xticks(range(0, 13, 2))
    a.set_xlabel("Exceptions in 250 days if the model is right")
    a.set_ylabel("Probability (%)")
    a.annotate("Theo: 7", (7, 100 * pm[7]), xytext=(3, 38), textcoords="offset points", ha="left", va="bottom",
               fontsize=8.5, color=INK_2, arrowprops=dict(arrowstyle="-", color=NEUTRAL, linewidth=0.8, shrinkA=0,
                                                          shrinkB=1))
    a.set_ylim(0, 31)
    a.annotate("expected 2.5", (2.5, 100 * pm[2]), xytext=(0, 4), textcoords="offset points", ha="center",
               va="bottom", fontsize=8.3, color=INK_2)
    p7 = binom.sf(6, n, p)
    a.annotate(f"7 or more happens\n{100 * p7:.1f}% of the time:\nrejected at 5%\n(LR 5.50 > 3.84)", (12.5, 14.5),
               ha="right", va="top", fontsize=8.3, color=INK_2)
    # ---- bottom right: do the misses arrive alone or in bunches?
    n00, n01, n10, n11 = 238, 4, 4, 3
    pi01, pi11 = n01 / (n00 + n01), n11 / (n10 + n11)
    b.bar([0, 1], [100 * pi01, 100 * pi11], width=0.62, color=C_GAUSS, zorder=3)
    b.axhline(1.0, color=INK_2, linewidth=1.0, linestyle=(0, (4, 2.5)), zorder=4)
    b.set_xlim(-0.6, 1.6)
    b.set_ylim(0, 55)
    b.set_xticks([0, 1])
    b.set_xticklabels(["after a quiet day\n(4 of 242)", "after an exception\n(3 of 7)"])
    b.set_ylabel("Chance of an exception today (%)")
    b.annotate("the model\nclaims 1%", (-0.08, 1.0), xytext=(0, 24), textcoords="offset points", ha="center",
               va="bottom", fontsize=8.3, color=INK_2,
               arrowprops=dict(arrowstyle="-", color=NEUTRAL, linewidth=0.8, shrinkA=1, shrinkB=0))
    b.annotate(f"{100 * pi01:.1f}%", (0, 100 * pi01), xytext=(0, 3), textcoords="offset points", ha="center",
               va="bottom", fontsize=8.5, color=INK_2)
    b.annotate(f"{100 * pi11:.0f}%: 26 times as likely\nLR_ind 13.49 > 6.63", (1, 100 * pi11), xytext=(0, 4),
               textcoords="offset points", ha="center", va="bottom", fontsize=8.5, color=INK_2)
    b.grid(axis="x", visible=False)
    return finish(fig, "ch08b_backtest_exceptions")


# --------------------------------------------------------------------------------------------
# Figure 5  The limit sheet (8B.9)
# --------------------------------------------------------------------------------------------
def fig_limit_sheet():
    # (label, value, soft, hard, text for the value)
    lines = [
        ("DTS, B Industrials cell", 1.62, 1.2, 1.5, "$1.62mm"),
        ("CS01 ladder, 3–7y", 71, 90, 120, "$71k/bp"),
        ("Key-rate DV01, 10y", 13, 15, 25, "+$13k/bp"),
        ("Issuer JTD, Halvorsen", 7.56, 7.0, 9.0, "$7.56mm"),
        ("ES 99%, 1-day", 2.7, 2.5, 3.0, "$2.7mm"),
        ("ES 99%, 10-day", 8.1, 9.0, 11.0, "$8.1mm"),
        ("Stress loss, worst scenario", WORST_STRESS, 15, 20, f"${WORST_STRESS:.1f}mm"),
        ("Days to liquidate", 4.1, 5, 10, "4.1 days"),
        ("Share of an issue", 6.2, 7.5, 10, "6.2%"),
        ("Backtest exceptions (250 d)", 3, 5, 10, "3"),
    ]
    fig, (a, b) = new_figure((7.0, 4.3), ncols=2, gridspec_kw={"width_ratios": [1.5, 1]})
    n = len(lines)
    ypos = np.arange(n)[::-1]
    for (lab, val, soft, hard, txt), y in zip(lines, ypos):
        u, us = 100 * val / hard, 100 * soft / hard
        if val >= hard:
            col, state = C_HARD, "HARD"
        elif val >= soft:
            col, state = C_SOFT, "SOFT"
        else:
            col, state = C_OK, ""
        a.barh(y, u, height=0.58, color=col, zorder=3)
        a.vlines(us, y - 0.38, y + 0.38, color=INK, linewidth=1.3, zorder=5)
        a.text(max(u, 100) + 2.5, y, f"{txt}  {state}".strip(), va="center", fontsize=8.3,
               color=INK if state else INK_2, fontweight="bold" if state else "normal")
    a.axvline(100, color=INK_2, linewidth=1.0, linestyle=(0, (4, 2.5)), zorder=4)
    a.set_yticks(ypos)
    a.set_yticklabels([ln[0] for ln in lines])
    a.tick_params(axis="y", length=0)
    a.set_xlim(0, 150)
    a.set_ylim(-0.7, n - 0.3)
    a.set_xticks([0, 25, 50, 75, 100])
    a.set_xlabel("Exposure as % of the hard limit")
    a.grid(axis="y", visible=False)
    a.grid(axis="x", visible=True)
    a.set_axisbelow(True)
    a.spines["left"].set_visible(False)
    a.annotate("hard", (100, n - 0.35), xytext=(0, 1), textcoords="offset points", ha="center", va="bottom",
               fontsize=8, color=INK_2)
    a.annotate("black tick = soft", (0, n - 0.35), xytext=(0, 1), textcoords="offset points", ha="left", va="bottom",
               fontsize=8, color=INK_2)
    # ---- right: the forty-bond migration, nothing traded
    cells = ["B\nIndustrials", "CCC\nIndustrials"]
    fri, mon = [1.08, 0.22], [0.60, 0.70]
    xs = np.arange(2)
    w = 0.34
    b.bar(xs - w / 2 - 0.02, fri, width=w, color=NEUTRAL, zorder=3)
    b.bar(xs + w / 2 + 0.02, mon, width=w, color=C_SHORT, zorder=3)
    for x, f, m in zip(xs, fri, mon):
        b.text(x - w / 2 - 0.02, f + 0.03, f"{f:.2f}", ha="center", va="bottom", fontsize=8.3, color=INK_2)
        b.text(x + w / 2 + 0.02, m + 0.03, f"{m:.2f}", ha="center", va="bottom", fontsize=8.3, color=INK_2)
    b.axhline(1.2, color=INK, linewidth=1.0, linestyle=(0, (1, 1.5)), zorder=2)
    b.axhline(1.5, color=INK_2, linewidth=1.0, linestyle=(0, (4, 2.5)), zorder=2)
    b.annotate("soft 1.2", (1.55, 1.2), xytext=(0, 2), textcoords="offset points", ha="right", va="bottom",
               fontsize=8, color=INK_2)
    b.annotate("hard 1.5", (1.55, 1.5), xytext=(0, 2), textcoords="offset points", ha="right", va="bottom",
               fontsize=8, color=INK_2)
    b.set_xlim(-0.6, 1.6)
    b.set_ylim(0, 1.75)
    b.set_xticks(xs)
    b.set_xticklabels(cells, fontsize=8.2)
    b.set_ylabel("DTS cell exposure ($mm)")
    b.grid(axis="x", visible=False)
    b.legend(handles=[Rectangle((0, 0), 1, 1, color=NEUTRAL), Rectangle((0, 0), 1, 1, color=C_SHORT)],
             labels=["Friday", "Monday"], loc="upper left", bbox_to_anchor=(0.0, 1.0), frameon=False,
             fontsize=8.3, handlelength=1.1, handleheight=0.9)
    b.annotate("40 bonds, 12 issuers\nmoved, nothing traded;\n10-day ES +11%",
               (0.36, 0.98), ha="left", va="center", fontsize=8.3, color=INK_2)
    return finish(fig, "ch08b_limit_sheet")


if __name__ == "__main__":
    for fn in (fig_factor_tree, fig_mixture_traps, fig_stress_library, fig_backtest, fig_limit_sheet):
        fn()
