"""Chapter 4-B figures: Bond Math for the Desk.

Run:  python3 tools/figures/ch04b.py      (writes assets/figures/ch04b_*.png)

Every bond number is ILLUSTRATIVE: it comes from the chapter's stylized ten-year 4.50% fallen-angel
note and from Listing 4-B.1 (bondmath.py) in Appendix F (book_src/95_appF_code_companion.md). The
script executes that listing, unchanged, in one namespace, so the figures can never drift from the
numbers the chapter quotes. The Treasury yields behind Table 4B.1 are real (FRED DGS10: 1.52% on
20 Feb 2020, 0.76% on 23 Mar 2020, 0.66% on 30 Jun 2020; checked against the FRED CSV download).

Color roles are fixed across the chapter:
  dates      : 20 Feb 2020 = BLUE, 23 Mar 2020 = ORANGE, 30 Jun 2020 = GREEN
  Taylor lines: actual price = INK_2, duration only = VIOLET, duration + convexity = RED
  P&L explain : gain = DIVERGING blue, loss = DIVERGING red, price levels = NEUTRAL
"""
import contextlib
import io
import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))
from style import *  # noqa: E402,F401,F403
import numpy as np  # noqa: E402
from matplotlib.ticker import FuncFormatter  # noqa: E402

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
APPENDIX = os.path.join(ROOT, "book_src", "95_appF_code_companion.md")

C_FEB, C_MAR, C_JUN = BLUE, ORANGE, GREEN
C_ACTUAL, C_DUR, C_CONV = INK_2, VIOLET, RED
GAIN, LOSS = "#3987e5", "#e66767"          # the two ends of the book's diverging ramp
DATES = [("20 Feb 2020", "2020-02-20", C_FEB), ("23 Mar 2020", "2020-03-23", C_MAR),
         ("30 Jun 2020", "2020-06-30", C_JUN)]
MINUS = "−"


def load_engine():
    """Execute Listing 4-B.1 (bondmath.py and its assertions) in one namespace and return it."""
    with open(APPENDIX, encoding="utf-8") as fh:
        src = fh.read()
    m = re.search(r"\{#code-4b-1\}\s*```python\n(.*?)```", src, re.S)
    if m is None:
        raise SystemExit(f"Listing 4-B.1 not found in {APPENDIX}")
    ns = {"__name__": "ch04b_engine"}
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(m.group(1), "listing_4B_1", "exec"), ns)
    return ns


E = load_engine()
C0, N0 = 0.045, 20
TABLE = E["table"]                                  # Table 4B.1, computed by the listing
YIELD = {"2020-02-20": 0.035, "2020-03-23": 0.09, "2020-06-30": 0.055}
TSY = {"2020-02-20": 0.0152, "2020-03-23": 0.0076, "2020-06-30": 0.0066}
FEB, MAR = TABLE["2020-02-20"], TABLE["2020-03-23"]


def pct_fmt(v, _):
    return f"{v:.0f}%"


# --------------------------------------------------------------------------------------------
# Figure 4-B.1  The Macaulay balance point (section 4B.3)
# --------------------------------------------------------------------------------------------
def fig_duration_beam():
    fig, axes = new_figure("panel2", ncols=2, sharey=True)
    t, cf = E["cashflows"](C0, N0)
    for ax, (label, key, col) in zip(axes, DATES[:2]):
        y = YIELD[key]
        pv = cf * (1.0 + y / 2.0) ** (-2.0 * t)
        w = 100.0 * pv / pv.sum()
        d_mac = E["risk_at_yield"](y, C0, N0)["D_mac"]
        ax.set_axisbelow(True)
        ax.bar(t, w, width=0.34, color=col)
        ax.vlines(d_mac, 0, 45, color=INK_2, linewidth=0.9, linestyle=(0, (3, 3)), zorder=2)
        ax.plot([d_mac], [0], "^", color=INK, markersize=10, clip_on=False, zorder=6)
        ax.text(d_mac - 0.15, 47, f"balance point\n{d_mac:.2f} years", ha="right", va="center",
                fontsize=8.5, color=INK_2)
        ax.annotate("principal + last coupon", (10.0, w[-1] * 0.98), xytext=(-8, 0),
                    textcoords="offset points", ha="right", va="center", fontsize=8, color=INK_2)
        ax.set_xlim(0, 10.7)
        ax.set_ylim(0, 74)
        ax.set_xticks([0, 2, 4, 6, 8, 10])
        ax.yaxis.set_major_formatter(FuncFormatter(pct_fmt))
        ax.set_xlabel("Years to payment")
        ax.set_title(f"{label}: yield {100 * y:.2f}%", fontsize=9.5)
    axes[0].set_ylabel("Share of the bond's present value")
    return finish(fig, "ch04b_duration_balance_point")


# --------------------------------------------------------------------------------------------
# Figure 4-B.2  The price-yield curve and its two-term Taylor expansion (section 4B.4)
# --------------------------------------------------------------------------------------------
def fig_taylor():
    fig, (a, b) = new_figure("panel2", ncols=2)
    y0 = YIELD["2020-02-20"]
    rk = E["risk_at_yield"](y0, C0, N0)
    P0, D, C = rk["price"], rk["D_mod"], rk["C_mod"]
    ys = np.linspace(0.01, 0.125, 240)
    actual = np.array([E["price"](y, C0, N0) for y in ys])
    dy = ys - y0
    lin = P0 - D * P0 * dy
    quad = lin + 0.5 * C * P0 * dy ** 2

    a.plot(100 * ys, actual, color=C_ACTUAL, linewidth=2.0, label="actual price", zorder=4)
    a.plot(100 * ys, lin, color=C_DUR, label="duration only (tangent)", zorder=3)
    a.plot(100 * ys, quad, color=C_CONV, label="duration + convexity", zorder=3)
    y1 = YIELD["2020-03-23"]
    p_act = E["price"](y1, C0, N0)
    p_lin = P0 - D * P0 * (y1 - y0)
    p_quad = p_lin + 0.5 * C * P0 * (y1 - y0) ** 2
    a.plot([100 * y0], [P0], "o", color=C_FEB, markersize=7, zorder=6)
    for val, col in [(p_act, C_ACTUAL), (p_lin, C_DUR), (p_quad, C_CONV)]:
        a.plot([100 * y1], [val], "o", color=col, markersize=5.5, zorder=6)
    mark_event(a, 100 * y0, "20 Feb: 3.50%")
    mark_event(a, 100 * y1, "23 Mar: 9.00%")
    a.set_xlim(1, 12.5)
    a.set_ylim(15, 138)
    a.set_xlabel("Yield (%)")
    a.set_ylabel("Price (per 100 face)")
    a.legend(loc="lower left", fontsize=8)
    a.grid(axis="x", visible=False)

    bp = 1e4 * dy
    err_lin, err_quad = lin - actual, quad - actual
    e_lin550, e_quad550 = p_lin - p_act, p_quad - p_act        # exact at +550 bp, not at the nearest grid point
    halo = dict(boxstyle="square,pad=0.15", fc=SURFACE, ec="none")
    b.axhline(0, color=NEUTRAL, linewidth=0.9, zorder=1)
    b.plot(bp, err_lin, color=C_DUR)
    b.plot(bp, err_quad, color=C_CONV)
    mark_event(b, 550, "+550 bp", y_frac=0.075)
    b.plot([550], [e_lin550], "o", color=C_DUR, markersize=5.5, zorder=6)
    b.plot([550], [e_quad550], "o", color=C_CONV, markersize=5.5, zorder=6)
    b.annotate(f"{e_lin550:+.1f}".replace("-", MINUS), (550, e_lin550), xytext=(-7, -3),
               textcoords="offset points", ha="right", va="top", fontsize=8.5, color=INK_2)
    b.annotate(f"{e_quad550:+.1f}", (550, e_quad550), xytext=(-7, 3), textcoords="offset points",
               ha="right", va="bottom", fontsize=8.5, color=INK_2)
    j = int(np.argmin(np.abs(bp - 760)))
    b.annotate("duration only", (bp[j], err_lin[j]), xytext=(-10, -12), textcoords="offset points",
               ha="right", va="top", fontsize=8.5, color=INK_2, bbox=halo, zorder=7)
    k = int(np.argmin(np.abs(bp - 800)))
    b.annotate("duration + convexity", (bp[k], err_quad[k]), xytext=(-10, 13),
               textcoords="offset points", ha="right", va="bottom", fontsize=8.5, color=INK_2,
               bbox=halo, zorder=7)
    b.plot([bp[j]], [err_lin[j]], "o", color=C_DUR, markersize=4, zorder=6)
    b.plot([bp[k]], [err_quad[k]], "o", color=C_CONV, markersize=4, zorder=6)
    b.set_ylim(-31, 13)
    b.set_xlim(-250, 910)
    b.set_xlabel("Yield change from 3.50% (bp)")
    b.set_ylabel("Approximation minus actual price")
    b.set_title("Convexity removes most of the error", fontsize=9.5)
    a.set_title("Price against yield", fontsize=9.5)
    return finish(fig, "ch04b_price_yield_taylor")


# --------------------------------------------------------------------------------------------
# Figure 4-B.3  The same bond in DV01 and in DTS (section 4B.5)
# --------------------------------------------------------------------------------------------
def fig_dv01_dts():
    fig, (a, b) = new_figure("panel2", ncols=2)
    dv = [TABLE[k]["DV01"] for _, k, _ in DATES]
    dts = [TABLE[k]["DTS"] for _, k, _ in DATES]
    cols = [c for _, _, c in DATES]
    names = ["20 Feb", "23 Mar", "30 Jun"]
    x = np.arange(3)

    a.bar(x, dv, color=cols, width=0.62)
    for xi, v in zip(x, dv):
        extra = "" if xi == 0 else f"\n{MINUS}{100 * (1 - v / dv[0]):.0f}%"
        a.annotate(f"\\${v:,.0f}{extra}", (xi, v), xytext=(0, 3), textcoords="offset points",
                   ha="center", va="bottom", fontsize=8.5, color=INK_2)
    a.set_axisbelow(True)
    b.set_axisbelow(True)
    a.set_ylim(0, 1.28 * max(dv))
    a.set_xticks(x, names)
    a.set_ylabel("DV01 = CS01 per \\$10mm face (\\$)")
    a.set_title("Per basis point: safer on 23 March", fontsize=9.5)
    a.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{v:,.0f}"))

    b.bar(x, dts, color=cols, width=0.62)
    for xi, v in zip(x, dts):
        extra = "" if xi == 0 else f"\n×{v / dts[0]:.1f}"
        b.annotate(f"{v:,.0f}{extra}", (xi, v), xytext=(0, 3), textcoords="offset points",
                   ha="center", va="bottom", fontsize=8.5, color=INK_2)
    b.set_ylim(0, 1.28 * max(dts))
    b.set_xticks(x, names)
    b.set_ylabel("DTS = modified duration × G-spread (bp)")
    b.set_title(f"Per percent: {dts[1] / dts[0]:.1f}\u00d7 riskier", fontsize=9.5)
    b.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{v:,.0f}"))
    return finish(fig, "ch04b_dv01_vs_dts")


# --------------------------------------------------------------------------------------------
# Figure 4-B.4  Five rulers, one bond (section 4B.8)
# --------------------------------------------------------------------------------------------
def fig_rulers():
    fig, (a, b) = new_figure((7.0, 3.5), ncols=2, sharey=True,
                             gridspec_kw={"width_ratios": [1.55, 1.0]})
    rows = [("Asset swap, market value", "ASW_mm"), ("PECS (R = 40%)", "PECS"), ("G-spread", "G"),
            ("Z-spread = OAS", "Z"), ("Asset swap, par-par", "ASW_par")]
    ypos = np.arange(len(rows))[::-1]
    mar_vals = [MAR[k] for _, k in rows]
    lo, hi = min(mar_vals), max(mar_vals)
    a.axvspan(lo, hi, color=C_MAR, alpha=0.10, linewidth=0, zorder=0)
    a.text(0.5 * (lo + hi), len(rows) - 0.42, f"about {int(round((hi - lo) / 10.0)) * 10} bp\napart on 23 Mar",
           ha="center", va="bottom", fontsize=8, color=INK_2)
    for yp, (_, k) in zip(ypos, rows):
        vals = [TABLE[d][k] for _, d, _ in DATES]
        a.plot([min(vals), max(vals)], [yp, yp], color=NEUTRAL, linewidth=1.4, zorder=1)
        for v, (_, _, col) in zip(vals, DATES):
            a.plot([v], [yp], "o", color=col, markersize=7, zorder=4)
    for (lab, _, col), dy_ in zip(DATES, [0, 1, 2]):
        a.plot([], [], "o", color=col, markersize=6, label=lab)
    a.legend(loc="upper left", fontsize=8, handletextpad=0.2, labelspacing=0.3)
    a.set_yticks(ypos, [r[0] for r in rows])
    a.set_xlim(0, 1080)
    a.set_ylim(-0.55, len(rows) + 0.45)
    a.set_xlabel("Spread (bp)")
    a.grid(axis="y", visible=False)
    a.grid(axis="x", visible=True)
    a.set_title("Level on each date", fontsize=9.5)

    ratios = [MAR[k] / FEB[k] for _, k in rows]
    b.set_axisbelow(True)
    b.barh(ypos, ratios, color=SEQ_BLUE_STEPS[11], height=0.58)
    for yp, r in zip(ypos, ratios):
        b.annotate(f"{r:.1f}×", (r, yp), xytext=(4, 0), textcoords="offset points",
                   ha="left", va="center", fontsize=8.5, color=INK_2)
    b.set_xlim(0, 6.4)
    b.set_xlabel("23 Mar spread ÷ 20 Feb spread")
    b.grid(axis="y", visible=False)
    b.grid(axis="x", visible=True)
    b.tick_params(axis="y", length=0)
    b.set_title("Widening, as a multiple", fontsize=9.5)
    return finish(fig, "ch04b_five_rulers")


# --------------------------------------------------------------------------------------------
# Figure 4-B.5  The 20 Feb to 23 Mar P&L explain (section 4B.8)
# --------------------------------------------------------------------------------------------
def fig_pnl_waterfall():
    fig, ax = new_figure("wide")
    p0, p1 = FEB["price"], MAR["price"]
    ex = E["explain"](p0, FEB["D_mod"], FEB["C_mod"], TSY["2020-03-23"] - TSY["2020-02-20"],
                      MAR["G"] / 1e4 - FEB["G"] / 1e4, p1)
    d_tsy = 1e4 * (TSY["2020-03-23"] - TSY["2020-02-20"])
    d_spr = MAR["G"] - FEB["G"]
    steps = [("Treasury rally\n" + f"({d_tsy:+.0f} bp)".replace("-", MINUS), ex["rates"]),
             ("Spread widening\n" + f"({d_spr:+.0f} bp)", ex["spread"]),
             ("Convexity\n" + f"(on {d_tsy + d_spr:+.0f} bp)", ex["convexity"]),
             ("Residual\n(third order)", ex["residual"])]
    labels = ["20 Feb\nprice"] + [s[0] for s in steps] + ["23 Mar\nprice"]
    x = np.arange(len(labels))
    ax.bar(x[0], p0, color=NEUTRAL, width=0.62)
    ax.bar(x[-1], p1, color=NEUTRAL, width=0.62)
    ax.annotate(f"{p0:.2f}", (x[0], p0), xytext=(0, 3), textcoords="offset points", ha="center",
                va="bottom", fontsize=8.5, color=INK_2)
    ax.annotate(f"{p1:.2f}", (x[-1], p1), xytext=(0, 3), textcoords="offset points", ha="center",
                va="bottom", fontsize=8.5, color=INK_2)
    level = p0
    ax.plot([x[0] + 0.31, x[1] - 0.31], [p0, p0], color=NEUTRAL, linewidth=0.8, zorder=1)
    for i, (_, v) in enumerate(steps, start=1):
        lo, hi = min(level, level + v), max(level, level + v)
        ax.bar(x[i], hi - lo, bottom=lo, color=GAIN if v >= 0 else LOSS, width=0.62)
        txt = f"{v:+.1f}".replace("-", MINUS)
        ax.annotate(txt, (x[i], hi), xytext=(0, 3), textcoords="offset points", ha="center",
                    va="bottom", fontsize=8.5, color=INK_2)
        level += v
        ax.plot([x[i] + 0.31, x[i + 1] - 0.31], [level, level], color=NEUTRAL, linewidth=0.8,
                zorder=1)
    assert abs(level - p1) < 1e-9
    ax.set_xticks(x, labels)
    ax.tick_params(axis="x", labelsize=8)
    ax.set_ylim(0, 128)
    ax.set_ylabel("Price (per 100 face)")
    ax.set_axisbelow(True)
    ax.text(0.19, 0.04, f"Risk numbers at 20 Feb: D = {FEB['D_mod']:.2f}, C = {FEB['C_mod']:.1f}",
            transform=ax.transAxes, ha="left",
            va="bottom", fontsize=8, color=MUTED)
    return finish(fig, "ch04b_pnl_explain_waterfall")


if __name__ == "__main__":
    fig_duration_beam()
    fig_taylor()
    fig_dv01_dts()
    fig_rulers()
    fig_pnl_waterfall()
