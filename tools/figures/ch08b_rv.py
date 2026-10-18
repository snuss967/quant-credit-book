"""Relative-value figure for Chapter 8-B (The Risk Model and the Limit Sheet), the Pair Book beat in section 8B.9.

Run:  python3 tools/figures/ch08b_rv.py   -> assets/figures/ch08b_stopout_heatmap.png

Kept apart from tools/figures/ch08b.py so the chapter's five other figures can be redrawn without touching it.

What it draws. The probability that a pod touches a drawdown line, measured peak to trough on allocated capital,
at least once within one year (252 trading days), starting at its high-water mark, as a heat map over the
book's Sharpe ratio (rows) and its annual volatility on allocated capital (columns). Left panel: Dov Adler's
first line, 6% of allocation ($24mm on $400mm, Ch 1-B canon), where capital is halved. Right panel: his second
line, 9% ($36mm), where the pod is closed; the 1.5x spacing is the press-reported 5% / 7.5% shape scaled to
his first line (illustrative composite; no platform publishes its rule). The outlined column is Dov's book at
6.3% (a typical daily swing of $1.6mm, Ch 1-B, times the square root of 252, over $400mm).

Model: daily P&L normal with mean Sharpe x vol / 252 and s.d. vol / sqrt(252); the drawdown is measured from the
running peak (the line ratchets up with every new high). The probability depends only on line / vol and the
Sharpe ratio, so each Sharpe row is simulated once in volatility units (200,000 paths, common random numbers)
and read at every column. Check: Sharpe 1, vol 6%, line 5% gives about 43% and Sharpe 0 about 72%, the
rv_pod_platforms_and_risk dossier's section 4.3 table (42.6% and 71.9%). Nothing here is market data.
Colours: SEQ_BLUE for probability (one hue, light to dark); INK outline for Dov's column.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
import numpy as np  # noqa: E402
from matplotlib.patches import Rectangle  # noqa: E402

from style import *  # noqa: E402,F401,F403

plt.rcParams["text.parse_math"] = False      # "$" is a dollar sign here

RNG = np.random.default_rng(20261030)
N_PATHS, CHUNK, DAYS = 200_000, 20_000, 252
SHARPES = [0.0, 0.5, 1.0, 1.5, 2.0]
VOLS = [0.03, 0.04, 0.05, 0.063, 0.08, 0.10]
DOV_COL = 3
LINES = [(0.06, "First line, 6% ($24mm): capital halved"), (0.09, "Second line, 9% ($36mm): pod closed")]


def max_drawdown_in_vol_units(sharpe):
    """Maximum peak-to-trough drawdown over one year for each path, in units of annual volatility."""
    out = np.empty(N_PATHS)
    mu, s = sharpe / DAYS, 1.0 / np.sqrt(DAYS)
    for i in range(N_PATHS // CHUNK):
        z = RNG.standard_normal((CHUNK, DAYS))
        x = np.cumsum(mu + s * z, axis=1)
        peak = np.maximum.accumulate(np.maximum(x, 0.0), axis=1)
        out[i * CHUNK:(i + 1) * CHUNK] = (peak - x).max(axis=1)
    return out


def main():
    mdd = {sr: max_drawdown_in_vol_units(sr) for sr in SHARPES}
    grids = []
    for line, _ in LINES:
        g = np.array([[np.mean(mdd[sr] >= line / v) for v in VOLS] for sr in SHARPES])
        grids.append(g)
    check_72 = np.mean(mdd[0.0] >= 0.05 / 0.06)
    check_43 = np.mean(mdd[1.0] >= 0.05 / 0.06)
    print(f"check: Sharpe 0, 6% vol, 5% line {check_72:.3f}; Sharpe 1 {check_43:.3f}")
    for (line, _), g in zip(LINES, grids):
        print(f"line {line:.0%}:")
        for sr, row in zip(SHARPES, g):
            print("  Sharpe", sr, " ".join(f"{p:6.1%}" for p in row))

    fig, axes = new_figure((7.0, 3.5), ncols=2)
    for ax, (line, title), g in zip(axes, LINES, grids):
        ax.imshow(g, cmap=SEQ_BLUE, vmin=0, vmax=1, aspect="auto", origin="lower")
        ax.grid(False)
        for spine in ax.spines.values():
            spine.set_visible(False)
        for r in range(len(SHARPES)):
            for c in range(len(VOLS)):
                p = g[r, c]
                ax.text(c, r, f"{p:.0%}" if p >= 0.005 else "<1%", ha="center", va="center", fontsize=8,
                        color=SURFACE if p > 0.55 else INK)
        ax.add_patch(Rectangle((DOV_COL - 0.5, -0.5), 1, len(SHARPES), fill=False, edgecolor=INK,
                               linewidth=1.4, zorder=4))
        ax.set_xticks(range(len(VOLS)))
        ax.set_xticklabels([f"{v * 100:g}" if i != DOV_COL else "6.3\nDov" for i, v in enumerate(VOLS)])
        ax.set_yticks(range(len(SHARPES)))
        ax.set_yticklabels([f"{s:g}" for s in SHARPES])
        ax.set_xlabel("Volatility on allocated capital (% a year)")
        ax.set_title(title, fontsize=9, loc="left")
        ax.tick_params(length=0)
    axes[0].set_ylabel("Sharpe ratio of the book")
    finish(fig, "ch08b_stopout_heatmap")


if __name__ == "__main__":
    main()
