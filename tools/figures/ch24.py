"""Chapter 24 figures: Bond-to-CDS Basis & Deliverable Obligation Mechanics.

Run from anywhere:  python3 tools/figures/ch24.py      (writes assets/figures/ch24_*.png)

Figures
  ch24_z_basis_vintage        Z-spread basis vs PECS basis and the JTD hedge ratio, against bond price (section 24.3.1)
  ch24_haircut_roe_mtm        ROE of a negative-basis package vs haircut; equity mark-to-market vs basis move (24.4.1)
  ch24_ctd_deliverable_prices post-event deliverable prices in the two default regimes (24.5.1)
  ch24_auction_final_price    stage-2 final price vs net open interest, with the Cap Amount (24.6.1)
  ch24_successor_cliffs       successor thresholds: one new entity, and two new entities (24.8.1)

Data: everything is ILLUSTRATIVE. The script executes Listings 24.1-24.7 of Appendix F
(book_src/95_appF_code_companion.md) unchanged in one namespace, so the figures use the chapter's own
functions and cannot drift from the numbers the chapter quotes (including their built-in asserts).
Color roles are fixed across the chapter:
  Z-spread basis = BLUE, par-equivalent (PECS) basis = ORANGE
  base case = BLUE, stressed haircut / rogue bid / the two bonds the text compares = ORANGE
  coupon level (3%, 5%, 8%) = sequential blue shades, darker for higher coupon
"""
import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from style import *            # applies the rcParams on import

import re

import numpy as np
from matplotlib.colors import ListedColormap
from matplotlib.lines import Line2D

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
APPENDIX = os.path.join(ROOT, "book_src", "95_appF_code_companion.md")


def load_listings():
    """Execute Listings 24.1-24.7 (the chapter's code) in one namespace and return it."""
    with open(APPENDIX, encoding="utf-8") as fh:
        src = fh.read()
    ns = {"__name__": "ch24_listings"}
    for k in range(1, 8):
        m = re.search(r"\{#code-24-%d\}\s*```python\n(.*?)```" % k, src, re.S)
        if m is None:
            raise SystemExit(f"Listing 24.{k} not found in {APPENDIX}")
        exec(compile(m.group(1), f"listing_24_{k}", "exec"), ns)
    return ns


E = load_listings()


# --------------------------------------------------------------------------------------------
# Figure 24.1  The same CDS hazard prices every bond; the Z basis still drifts with price (24.3.1)
# --------------------------------------------------------------------------------------------
def fig_z_basis_vintage():
    r, lam, R, T = E["r0"], E["lam0"], E["R0"], E["T0"]
    s_cds = E["par_spread"](lam, r, T, R)
    coupons = np.linspace(0.02, 0.12, 41)
    price, zb, pb = [], [], []
    for c in coupons:
        P = E["bond_price_hazard"](c, T, lam, r, R)
        z = E["z_spread"](P, c, T, r)
        s_pe, _ = E["pecs"](P, c, T, r, R)
        price.append(100.0 * P)
        zb.append(1e4 * (s_cds - z))
        pb.append(1e4 * (s_cds - s_pe))
    price, zb, pb = map(np.array, (price, zb, pb))

    fig, (a, b) = new_figure("panel2", ncols=2)

    # (a) the two bases against price
    a.axhline(0, color=NEUTRAL, linewidth=0.9, zorder=1)
    a.plot(price, zb, color=BLUE)
    a.plot(price, pb, color=ORANGE)
    a.set_xlim(price.min() - 1, price.max() + 15)
    a.set_xlabel("Bond price (points of face)")
    a.set_ylabel("Basis, CDS minus bond (bp)")
    label_end(a, price[-1], zb[-1], "Z-spread basis", BLUE, dx=5)
    label_end(a, price[-1], pb[-1], "PECS basis", ORANGE, dx=5, dy=7)
    # the three bonds of the chapter table (4%, 7%, 10% coupon)
    for c in (0.04, 0.07, 0.10):
        P = 100.0 * E["bond_price_hazard"](c, T, lam, r, R)
        z = E["z_spread"](P / 100.0, c, T, r)
        yv = 1e4 * (s_cds - z)
        a.plot([P], [yv], "o", color=BLUE, markersize=6, markeredgecolor="white", zorder=6)
        a.annotate(f"{c * 100:.0f}% coupon, {P:.0f}", (P, yv), xytext=(8, 2), textcoords="offset points",
                   va="center", ha="left", fontsize=8, color=INK_2)
    a.grid(axis="x", visible=False)
    a.set_title("(a) Two bases for one correctly priced bond")

    # (b) the JTD-neutral hedge ratio
    p = np.linspace(price.min(), price.max(), 50)
    ratio = [E["jtd_hedge_ratio"](x / 100.0, R) for x in p]
    b.axhline(1.0, color=NEUTRAL, linewidth=0.9, zorder=1)
    b.plot(p, ratio, color=BLUE)
    b.set_xlim(a.get_xlim()[0], price.max() + 2)
    b.set_xlabel("Bond price (points of face)")
    b.set_ylabel("CDS notional per unit of bond face")
    b.plot([88], [0.80], "o", color=ORANGE, markersize=7, markeredgecolor="white", zorder=6)
    b.annotate("Halvorsen at 88:\n$8mm of protection\nper $10mm of bonds", (88, 0.80), xytext=(8, -2),
               textcoords="offset points", va="top", fontsize=8, color=INK_2)
    b.annotate("par bond: 1.0", (price.max(), 1.0), xytext=(-2, -9), textcoords="offset points", ha="right",
               va="top", fontsize=8, color=MUTED)
    b.grid(axis="x", visible=False)
    b.set_title("(b) Jump-to-default hedge ratio")
    return finish(fig, "ch24_z_basis_vintage")


# --------------------------------------------------------------------------------------------
# Figure 24.2  ROE falls as the haircut rises; the equity mark-to-market is divided by h (24.4.1)
# --------------------------------------------------------------------------------------------
def fig_haircut_roe_mtm():
    roe, mtm = E["basis_package_roe"], E["basis_mtm_on_equity"]
    fig, (a, b) = new_figure("panel2", ncols=2)

    # (a) ROE vs haircut for three entry bases, repo spread 40bp
    h = np.linspace(0.08, 0.40, 200)
    phi = 40.0
    a.axhline(0, color=NEUTRAL, linewidth=0.9, zorder=1)
    shades = {-150.0: SEQ_BLUE_STEPS[11], -100.0: SEQ_BLUE_STEPS[7], -60.0: SEQ_BLUE_STEPS[3]}
    for bb, col in shades.items():
        y = np.array([100.0 * roe(bb, phi, x) for x in h])
        a.plot(h * 100.0, y, color=col)
        label_end(a, h[-1] * 100.0, y[-1], f"b = \u2212{abs(bb):.0f} bp", col, dx=5)
    # worked points: base haircut = BLUE, stressed (doubled) haircut = ORANGE, as in panel (b); the labels
    # sit left of / above the points so they clear the curves and the dashed lines
    for hh, txt, col, off, ha in ((0.15, "h = 15%", BLUE, (-7, -11), "right"),
                                  (0.30, "h = 30%", ORANGE, (-5, 9), "right")):
        mark_event(a, hh * 100.0, txt)
        v = 100.0 * roe(-100.0, phi, hh)
        a.plot([hh * 100], [v], "o", color=col, markersize=6.5, markeredgecolor="white", zorder=6)
        a.annotate(f"{v:.1f}%", (hh * 100, v), xytext=off, textcoords="offset points", fontsize=8.5,
                   color=INK_2, va="center", ha=ha)
    a.set_xlabel("Repo haircut h (% of position)")
    a.set_ylabel("Excess return on equity (% a year)")
    a.set_xlim(6, 52)
    a.grid(axis="x", visible=False)
    a.text(0.99, 0.56, "repo spread 40 bp", transform=a.transAxes, ha="right", va="center", fontsize=8,
           color=MUTED)
    a.set_title("(a) Return on equity vs haircut")

    # (b) mark-to-market on equity vs widening of the basis, two haircuts
    d = np.linspace(0.0, -300.0, 100)
    D = 4.5
    for hh, col in ((0.15, BLUE), (0.30, ORANGE)):
        y = np.array([100.0 * mtm(x, D, hh) for x in d])
        b.plot(-d, y, color=col)
        label_end(b, 300.0, y[-1], f"h = {hh * 100:.0f}%", col, dx=5)
    b.axhline(-100.0, color=NEUTRAL, linewidth=0.9, linestyle=(0, (3, 3)), zorder=1)
    b.annotate("equity gone", (2, -100), xytext=(0, 4), textcoords="offset points", ha="left",
               fontsize=8, color=INK_2)
    pt = 100.0 * mtm(-150.0, D, 0.15)
    b.plot([150], [pt], "o", color=BLUE, markersize=6.5, markeredgecolor="white", zorder=6)
    b.annotate("basis \u2212100 \u2192 \u2212250 bp:\n\u221245% of equity at h = 15%", (150, pt), xytext=(14, -80),
               textcoords="data", fontsize=8, color=INK_2, va="center", ha="left",
               arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.8, shrinkA=2, shrinkB=4))
    b.set_xlim(0, 300)
    b.set_ylim(-108, 5)
    b.set_xlabel("Widening of the basis (bp)")
    b.set_ylabel("Mark-to-market on equity (%)")
    b.grid(axis="x", visible=False)
    note(b, "spread duration 4.5", "upper right")
    b.set_title("(b) Equity mark-to-market")
    return finish(fig, "ch24_haircut_roe_mtm")


# --------------------------------------------------------------------------------------------
# Figure 24.3  Cheapest to deliver: the two default regimes (24.5.1)
# --------------------------------------------------------------------------------------------
def fig_ctd_deliverable_prices():
    price_at_yield = E["price_at_yield"]
    y_event, R_claim = 0.11, 0.30
    mats = np.arange(1.0, 30.01, 0.5)
    cpns = {0.03: SEQ_BLUE_STEPS[4], 0.05: SEQ_BLUE_STEPS[8], 0.08: SEQ_BLUE_STEPS[12]}

    fig, (a, b) = new_figure("panel2", ncols=2, sharey=True)

    # (a) regime 1: every claim is par + accrued, so prices differ only by accrued interest
    for c, col in cpns.items():
        a.plot(mats, np.full(mats.size, 100.0 * R_claim * (1.0 + c * 0.25)), color=col)
    p8 = 100.0 * R_claim * (1.0 + 0.08 * 0.25)
    p5 = 100.0 * R_claim * (1.0 + 0.05 * 0.25)
    a.plot([1.5], [p8], "o", color=ORANGE, markersize=7, markeredgecolor="white", zorder=6)
    a.plot([22.0], [p5], "o", color=ORANGE, markersize=7, markeredgecolor="white", zorder=6)
    a.annotate("8% due 1.5y", (1.5, p8), xytext=(8, -9), textcoords="offset points", ha="left", va="top",
               fontsize=8, color=INK_2)
    a.annotate("5% due 22y", (22.0, p5), xytext=(0, -9), textcoords="offset points", ha="center", va="top",
               fontsize=8, color=INK_2)
    a.set_ylim(0, 118)
    a.set_xlim(0, 30)
    a.set_xlabel("Remaining maturity (years)")
    a.set_ylabel("Post-event price (points of face)")
    a.annotate(f"every deliverable recovers\nabout 30 per 100 of claim\nswap pays {100 - p8:.1f} or {100 - p5:.1f}",
               (15, p8), xytext=(0, 14), textcoords="offset points", ha="center", va="bottom", fontsize=8,
               color=INK_2)
    a.grid(axis="x", visible=False)
    a.set_title("(a) Bankruptcy: claims accelerate")

    # (b) regime 2: performing bonds priced at the event yield
    ends = {}
    for c, col in cpns.items():
        y = np.array([100.0 * price_at_yield(c, m, y_event) for m in mats])
        b.plot(mats, y, color=col)
        ends[c] = (mats[-1], y[-1], col)
    for c, (x, y, col) in ends.items():
        label_end(b, x, y, f"{c * 100:.0f}% coupon", col, dx=5)
    short = 100.0 * price_at_yield(0.08, 1.5, y_event)
    longb = 100.0 * price_at_yield(0.05, 22.0, y_event)
    b.plot([1.5], [short], "o", color=ORANGE, markersize=7, markeredgecolor="white", zorder=6)
    b.plot([22.0], [longb], "o", color=ORANGE, markersize=7, markeredgecolor="white", zorder=6)
    b.annotate(f"8% due 1.5y: {short:.1f}\nswap pays {100 - short:.0f}", (1.5, short), xytext=(14, 7),
               textcoords="offset points", va="bottom", fontsize=8, color=INK_2)
    b.annotate(f"5% due 22y: {longb:.1f}\nswap pays {100 - longb:.1f}", (22.0, longb), xytext=(0, 10),
               textcoords="offset points", va="bottom", ha="center", fontsize=8, color=INK_2)
    b.axvline(30, color=NEUTRAL, linewidth=0.9, linestyle=(0, (3, 3)), zorder=1)
    b.annotate("30-year\nlimit", (30, 117), xytext=(-3, 0), textcoords="offset points", ha="right", va="top",
               fontsize=8, color=MUTED)
    b.set_xlim(0, 37.5)
    b.set_xlabel("Remaining maturity (years)")
    b.grid(axis="x", visible=False)
    b.set_title("(b) Failure to pay: no acceleration")
    note(b, "event yield y = 11%", "lower left")
    return finish(fig, "ch24_ctd_deliverable_prices")


# --------------------------------------------------------------------------------------------
# Figure 24.4  The auction's final price vs the net open interest (24.6.1)
# --------------------------------------------------------------------------------------------
def fig_auction_final_price():
    final_price, inside_market = E["final_price"], E["inside_market"]
    bids, offers = E["bids"], E["offers"]
    lim_bids, lim_offers = E["lim_bids"], E["lim_offers"]
    imm, _, _ = inside_market(bids, offers)
    cap = 1.0
    rogue = [(30.0, 10.0)] + lim_bids

    fig, (a, b) = new_figure("panel2", ncols=2, gridspec_kw={"width_ratios": [1.45, 1.0]})

    # (a) the chapter's book over the whole range of open interest
    oi = np.linspace(-130.0, 60.0, 1901)
    base = np.array([final_price(imm, x, lim_bids, lim_offers, cap) for x in oi])
    a.axhspan(imm - cap, imm + cap, color=SEQ_BLUE_STEPS[0], alpha=0.6, zorder=0, linewidth=0)
    a.axhline(imm, color=NEUTRAL, linewidth=0.9, zorder=1)
    a.axvline(0, color=NEUTRAL, linewidth=0.9, linestyle=(0, (3, 3)), zorder=1)
    a.step(oi, base, where="post", color=BLUE, zorder=5)
    a.set_xlim(-130, 60)
    a.set_ylim(-2, 40)
    a.set_xlabel("Net open interest ($mm)")
    a.set_ylabel("Final price (points)")
    a.grid(axis="x", visible=False)
    a.annotate(f"IMM {imm:.3f}", (-129, imm), xytext=(2, 9), textcoords="offset points", fontsize=8,
               color=INK_2, va="bottom")
    a.annotate("shaded: IMM ± 1-point Cap", (-129, imm - cap), xytext=(2, -4), textcoords="offset points",
               fontsize=8, color=INK_2, va="top")
    a.annotate("net forced sellers:\nprice walks down the bids\nuntil the bids run out", (-128, 38.5), ha="left",
               va="top", fontsize=8, color=INK_2)
    a.annotate("net forced buyers:\nprice walks up\nthe offers", (8, 12), ha="left", va="center", fontsize=8,
               color=INK_2)
    a.annotate("offers run out\n(price 100)", (51, 40), xytext=(-4, -2), textcoords="offset points", ha="right",
               va="top", fontsize=8, color=INK_2)
    a.annotate("bids\nrun out:\nprice 0", (-128, 1.5), ha="left", va="bottom", fontsize=8, color=INK_2)
    a.set_title("(a) The chapter's book")

    # (b) zoom on small selling open interest: a rogue high bid, with and without the cap
    oi2 = np.linspace(-26.0, 8.0, 1701)
    uncapped = np.array([final_price(imm, x, rogue, lim_offers, 1e6) for x in oi2])
    capped = np.array([final_price(imm, x, rogue, lim_offers, cap) for x in oi2])
    base2 = np.array([final_price(imm, x, lim_bids, lim_offers, cap) for x in oi2])
    b.axhspan(imm - cap, imm + cap, color=SEQ_BLUE_STEPS[0], alpha=0.6, zorder=0, linewidth=0)
    b.axhline(imm, color=NEUTRAL, linewidth=0.9, zorder=1)
    b.axvline(0, color=NEUTRAL, linewidth=0.9, linestyle=(0, (3, 3)), zorder=1)
    b.step(oi2, uncapped, where="post", color=ORANGE, linewidth=1.1, linestyle=(0, (2, 2)), zorder=3)
    b.step(oi2, capped, where="post", color=ORANGE, zorder=4)
    b.step(oi2, base2, where="post", color=BLUE, zorder=5)
    b.set_xlim(-26, 8)
    b.set_ylim(23.5, 31.5)
    b.set_xlabel("Net open interest ($mm)")
    b.grid(axis="x", visible=False)
    handles = [Line2D([0], [0], color=BLUE, lw=LW), Line2D([0], [0], color=ORANGE, lw=LW),
               Line2D([0], [0], color=ORANGE, lw=1.1, linestyle=(0, (2, 2)))]
    b.legend(handles, ["Chapter's book", "Plus rogue 30.0 bid, cap on", "Plus rogue 30.0 bid, no cap"],
             loc="lower right", fontsize=8, handlelength=1.8, borderaxespad=0.2)
    b.set_title("(b) Zoom: a rogue bid")
    return finish(fig, "ch24_auction_final_price")


# --------------------------------------------------------------------------------------------
# Figure 24.5  Successor arithmetic: thresholds and cliffs (24.8.1)
# --------------------------------------------------------------------------------------------
def fig_successor_cliffs():
    succ = E["successors"]
    fig, (a, b) = new_figure((7.0, 3.7), ncols=2, gridspec_kw={"width_ratios": [1.0, 1.1]})

    # (a) one new entity takes a share w; the original keeps 1 - w
    w = np.linspace(0.0, 1.0, 2001)
    orig, new = [], []
    for x in w:
        res = succ({"NEWCO": x}) if x > 0 else {"REFERENCE ENTITY": 1.0}
        orig.append(100.0 * res.get("REFERENCE ENTITY", 0.0))
        new.append(100.0 * res.get("NEWCO", 0.0))
    orig, new = np.array(orig), np.array(new)
    a.step(w * 100, orig, where="post", color=BLUE)
    a.step(w * 100, new, where="post", color=ORANGE)
    a.set_xlim(0, 100)
    a.set_ylim(-3, 134)
    a.set_xlabel("Share of debt moved to the new entity (%)")
    a.set_ylabel("Share of each CDS (%)")
    a.axvline(25, color=NEUTRAL, linewidth=0.9, linestyle=(0, (3, 3)), zorder=1)
    a.axvline(75, color=NEUTRAL, linewidth=0.9, linestyle=(0, (3, 3)), zorder=1)
    a.annotate("above 25%:\nswap splits 50/50", (25, 133), xytext=(3, 0), textcoords="offset points", va="top",
               fontsize=8, color=INK_2)
    a.annotate("75% or more:\nsole\nSuccessor", (75, 133), xytext=(3, 0), textcoords="offset points", va="top",
               fontsize=8, color=INK_2)
    label_end(a, 12, 100, "original", BLUE, dx=0, dy=-9, ha="center")
    label_end(a, 88, 100, "new entity", ORANGE, dx=0, dy=-9, ha="center")
    a.set_yticks([0, 25, 50, 75, 100])
    a.grid(axis="x", visible=False)
    a.set_title("(a) One new entity")

    # (b) two new entities A and B: how many pieces does one swap become?
    n = 400
    g = (np.arange(n) + 0.5) / n
    W1, W2 = np.meshgrid(g, g)
    m = np.full(W1.shape, np.nan)
    cat = np.full(W1.shape, np.nan)
    labels = {}
    for i in range(n):
        for j in range(n):
            x1, x2 = W1[i, j], W2[i, j]
            if x1 + x2 > 1.0:
                continue
            res = succ({"A": x1, "B": x2})
            key = tuple(sorted(res))
            labels.setdefault(key, len(labels))
            m[i, j] = len(res)
            cat[i, j] = labels[key]
    cmap = ListedColormap([SEQ_BLUE_STEPS[0], SEQ_BLUE_STEPS[5], SEQ_BLUE_STEPS[10]])
    b.pcolormesh(W1 * 100, W2 * 100, np.ma.masked_invalid(m), cmap=cmap, vmin=0.5, vmax=3.5, shading="auto",
                 rasterized=True)
    b.contour(W1 * 100, W2 * 100, np.ma.masked_invalid(cat), levels=[i + 0.5 for i in range(len(labels))],
              colors="white", linewidths=1.0)
    b.fill([100, 100, 0], [0, 100, 100], color=SURFACE, zorder=3, linewidth=0)      # clean hypotenuse
    b.plot([0, 100], [100, 0], color=NEUTRAL, linewidth=0.8, zorder=4)
    b.set_xlim(0, 100)
    b.set_ylim(0, 100)
    b.set_aspect("equal", adjustable="box")
    b.set_xlabel("Share moved to entity A (%)")
    b.set_ylabel("Share moved to entity B (%)")
    b.set_xticks([0, 25, 50, 75, 100])
    b.set_yticks([0, 25, 50, 75, 100])
    b.grid(False)
    b.spines["left"].set_visible(True)
    b.spines["bottom"].set_visible(True)

    def lab(x, y, txt, dark=False, fs=8):
        b.text(x, y, txt, ha="center", va="center", fontsize=fs, color="white" if dark else INK)

    lab(12.5, 12.5, "unchanged")
    lab(50, 11, "original\n+ A")
    lab(12.5, 50, "original\n+ B")
    lab(32.5, 33, "orig.\n+A+B", dark=True, fs=7)
    lab(50, 38, "A + B", dark=True)
    lab(86, 8, "A\nonly")
    lab(8, 86, "B\nonly")
    handles = [plt.Rectangle((0, 0), 1, 1, color=SEQ_BLUE_STEPS[0]), plt.Rectangle((0, 0), 1, 1, color=SEQ_BLUE_STEPS[5]),
               plt.Rectangle((0, 0), 1, 1, color=SEQ_BLUE_STEPS[10])]
    b.legend(handles, ["1 swap", "2 swaps", "3 swaps"], title="One swap becomes", title_fontsize=8, loc="upper right",
             fontsize=8, frameon=False, borderaxespad=0.2, handlelength=1.2)
    b.set_title("(b) Two new entities")
    return finish(fig, "ch24_successor_cliffs")


if __name__ == "__main__":
    fig_z_basis_vintage()
    fig_haircut_roe_mtm()
    fig_ctd_deliverable_prices()
    fig_auction_final_price()
    fig_successor_cliffs()
