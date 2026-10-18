"""Relative-value figure for Chapter 8 (Stripping Beta to Isolate Pure IDO), the Pair Book beat in section 8.8.

Run:  python3 tools/figures/ch08_rv.py   -> assets/figures/ch08_residual_heatmap.png

Kept apart from tools/figures/ch08.py so the chapter's five other figures can be redrawn without touching it.

What it draws. The Long Scene "Twelve Residuals" (Dov Adler's pod at Vantress, fictional composites, last week of
September 2026): Wen Zhao's panel of sixty common days on which all twelve open pairs had real marks, each pair's
idio P&L scaled by its DTS. Left panel: the 12 x 12 correlation matrix of the residuals the vendor's factor model
left, rows and columns sorted by the first principal component's loading (heaviest first). Right panel: the same
panel after step three of section 8.8's definition (the first principal component removed). The five heaviest pairs
are outlined; two ledgered pairs are labeled where they fall (PB-19 seventh, PB-01 last).

Model (illustrative; nothing here is market data): one common factor plus independent noise, 60 daily draws,
residual_i = v_i * g + sqrt(1 - v_i^2) * e_i, with population loadings chosen so that five pairs share most of the
factor. Pairs are ranked by their sample loading on the first principal component; the two ledgered pairs take the
places the scene gives them (PB-19 seventh, PB-01 last), and the rest are unnumbered. The script searches seeds from
a fixed base until the sample matches the numbers the scene prints: mean pairwise correlation 0.28 (within 0.004),
first principal component about a third of the residual variance (0.31 to 0.365), and the seven pairs left after
the five heaviest close at a mean correlation just under 0.15 (0.13 to 0.15). It prints every number it checks.
Colours: DIVERGING (blue, gray, red) for correlation polarity, scale -0.6 to +0.6; INK outline for the five.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
import numpy as np  # noqa: E402
from matplotlib.patches import Rectangle  # noqa: E402

from style import *  # noqa: E402,F401,F403

plt.rcParams["text.parse_math"] = False

DAYS, N = 60, 12
# Population loadings on the common component: five heavy pairs, then seven lighter ones.
V = np.array([0.76, 0.74, 0.72, 0.70, 0.68, 0.52, 0.48, 0.44, 0.40, 0.36, 0.32, 0.24])
PB19, PB01 = "PB-19", "PB-01"
BASE_SEED = 20260929


def mean_offdiag(c):
    m = c.shape[0]
    return (c.sum() - np.trace(c)) / (m * (m - 1))


def simulate(seed):
    rng = np.random.default_rng(seed)
    g = rng.standard_normal(DAYS)
    e = rng.standard_normal((DAYS, N))
    x = g[:, None] * V[None, :] + e * np.sqrt(1 - V ** 2)[None, :]
    x = (x - x.mean(0)) / x.std(0)
    c = np.corrcoef(x, rowvar=False)
    w, vecs = np.linalg.eigh(c)
    pc = vecs[:, -1] * np.sign(vecs[:, -1].sum())
    share = w[-1] / w.sum()
    order = np.argsort(-pc)
    scores = x @ pc
    x_perp = x - np.outer(scores, pc)
    c_perp = np.corrcoef(x_perp, rowvar=False)
    return c, c_perp, pc, share, order


def acceptable(c, share, order):
    if abs(mean_offdiag(c) - 0.28) > 0.004 or not 0.31 <= share <= 0.365:
        return False
    rest = list(order[5:])
    return 0.13 <= mean_offdiag(c[np.ix_(rest, rest)]) <= 0.15


def main():
    for seed in range(BASE_SEED, BASE_SEED + 20000):
        c, c_perp, pc, share, order = simulate(seed)
        if acceptable(c, share, order):
            break
    else:
        raise SystemExit("no seed met the scene's numbers")
    rest = list(order[5:])
    load2 = pc ** 2
    print(f"seed {seed}")
    print(f"mean pairwise residual correlation {mean_offdiag(c):.3f}")
    print(f"first PC share of residual variance {share:.3f}; all loadings same sign: {bool((pc > 0).all())}")
    print(f"five heaviest carry {load2[order[:5]].sum() / load2.sum():.0%} of the component's squared loadings")
    print(f"mean correlation of the remaining seven {mean_offdiag(c[np.ix_(rest, rest)]):.3f}")
    print(f"after removing the first PC, mean pairwise correlation {mean_offdiag(c_perp):.3f}")
    print("labels by loading rank: PB-19 seventh, PB-01 twelfth (the pairs are fictional; ranks are the scene's)")

    labels = [PB19 if k == 6 else PB01 if k == N - 1 else f"Pair {k + 1}" for k in range(N)]

    fig, axes = new_figure((7.0, 3.7), ncols=2)
    titles = [f"Vendor-model residuals: mean {mean_offdiag(c):.2f}",
              f"After step three: mean {mean_offdiag(c_perp):.2f}"]
    for ax, mat, title in zip(axes, [c, c_perp], titles):
        m = mat[np.ix_(order, order)].copy()
        np.fill_diagonal(m, np.nan)
        cmap = DIVERGING.copy()
        cmap.set_bad(GRID)
        im = ax.imshow(m, cmap=cmap, vmin=-0.6, vmax=0.6, aspect="equal")
        ax.grid(False)
        for spine in ax.spines.values():
            spine.set_visible(False)
        ax.add_patch(Rectangle((-0.5, -0.5), 5, 5, fill=False, edgecolor=INK, linewidth=1.3, zorder=4))
        ax.set_xticks(range(N))
        ax.set_xticklabels(labels, rotation=90, fontsize=7)
        ax.set_yticks(range(N))
        ax.set_yticklabels(labels, fontsize=7)
        ax.tick_params(length=0)
        ax.set_title(title, fontsize=8.5, loc="left")
    cb = fig.colorbar(im, ax=list(axes), fraction=0.025, pad=0.02)
    cb.set_label("Correlation of DTS-scaled idio P&L, 60 days", fontsize=8, color=INK_2)
    cb.ax.tick_params(labelsize=7.5, length=0)
    cb.outline.set_visible(False)
    finish(fig, "ch08_residual_heatmap")


if __name__ == "__main__":
    main()
