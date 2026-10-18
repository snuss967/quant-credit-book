"""Relative-value figure for Chapter 9 (Factor Investing in Corporate Credit), the Pair Book beat in section 9.7.2.

Run:  python3 tools/figures/ch09_rv.py   -> assets/figures/ch09_pair_book_value_loading.png

Kept apart from tools/figures/ch09.py so the chapter's other figures can be redrawn without touching it.

What it draws. Dov Adler's twelve-pair book (Vantress, a fictional composite) on Marcus Oyelaran's second x-ray,
the evening of Tue 29 Sep 2026 (before) and after Dov's resize on Wed 30 Sep (after). Every number is
illustrative and is set by hand below; nothing here is market data or a simulation.

Left panel: the book's P&L for a one-standard-deviation month of each of the chapter's five DTS-neutral factors,
as a percentage of the book's September monthly P&L volatility. Value 70 -> 13; carry falls with it (30 -> 22)
because value and carry are correlated (+0.52 in the Henke et al. matrix quoted in section 9.7.1); the other
three barely move.

Right panel: the book's P&L variance in units of its September variance (= 100), split into value, the other
four factors together, and the residual (idio). Before 49 / 17 / 34; after 1.7 / 10 / 27 (total 38.7).

Checks the text relies on: standardized value loading 70/100 = 0.70 before and 13/sqrt(38.7)/10 = 0.21 after
("0.2"); idio share 34% -> 70%; book volatility falls to sqrt(0.387) = 0.62 of September's (more than a third
off); idio volatility to sqrt(27/34) = 0.89 (about a tenth off).
Colours: NEUTRAL for before, SERIES[0] for after (left); SERIES[1] value, NEUTRAL other factors, SERIES[0] idio
(right), direct-labelled.
"""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
import numpy as np  # noqa: E402
from matplotlib.patches import Patch  # noqa: E402

from style import *  # noqa: E402,F401,F403

plt.rcParams["text.parse_math"] = False

FACTORS = ["Value", "Carry", "Momentum", "Low-risk", "Quality"]
BEFORE = [70, 30, -10, -15, 15]
AFTER = [13, 22, -10, -14, 15]

VAR_BEFORE = {"Value": 49.0, "Other four factors": 17.0, "Idio (residual)": 34.0}
VAR_AFTER = {"Value": 1.7, "Other four factors": 10.0, "Idio (residual)": 27.0}
VAR_COLORS = {"Value": SERIES[1], "Other four factors": NEUTRAL, "Idio (residual)": SERIES[0]}


def main():
    tot_b, tot_a = sum(VAR_BEFORE.values()), sum(VAR_AFTER.values())
    std_after = AFTER[0] / (math.sqrt(tot_a) * 10)
    print(f"value loading before {BEFORE[0] / 100:.2f}, after {std_after:.2f}")
    print(f"idio share before {VAR_BEFORE['Idio (residual)'] / tot_b:.0%}, after {VAR_AFTER['Idio (residual)'] / tot_a:.0%}")
    print(f"book vol after / before {math.sqrt(tot_a / tot_b):.2f}; idio vol {math.sqrt(27 / 34):.2f}")

    fig, (ax1, ax2) = new_figure((7.0, 3.4), ncols=2)

    y = np.arange(len(FACTORS))[::-1]
    h = 0.36
    ax1.barh(y + h / 2, BEFORE, height=h, color=NEUTRAL, label="Tue 29 Sep (before)")
    ax1.barh(y - h / 2, AFTER, height=h, color=SERIES[0], label="Wed 30 Sep (after)")
    ax1.axvline(0, color=INK_2, linewidth=0.8)
    ax1.set_yticks(y)
    ax1.set_yticklabels(FACTORS)
    ax1.set_xlim(-25, 80)
    ax1.set_xlabel("P&L per one-sigma month of the factor\n(% of September's monthly book volatility)")
    ax1.grid(axis="x", color=GRID, linewidth=0.7)
    ax1.grid(axis="y", visible=False)
    ax1.legend(loc="lower right", fontsize=8)
    ax1.annotate("loading 0.7", (BEFORE[0], y[0] + h / 2), xytext=(-4, 0), textcoords="offset points",
                 ha="right", va="center", fontsize=8, color=INK)
    ax1.annotate("0.2", (AFTER[0], y[0] - h / 2), xytext=(4, 0), textcoords="offset points",
                 ha="left", va="center", fontsize=8, color=INK_2)

    xs = [0, 1]
    bottoms = [0.0, 0.0]
    for key in ["Idio (residual)", "Other four factors", "Value"]:
        vals = [VAR_BEFORE[key], VAR_AFTER[key]]
        ax2.bar(xs, vals, bottom=bottoms, width=0.55, color=VAR_COLORS[key], edgecolor=SURFACE, linewidth=1.0)
        for i, (v, b) in enumerate(zip(vals, bottoms)):
            share = v / (tot_b if i == 0 else tot_a)
            if v >= 6:
                ax2.text(xs[i], b + v / 2, f"{share:.0%}", ha="center", va="center", fontsize=8,
                         color=SURFACE if key != "Other four factors" else INK)
        bottoms = [b + v for b, v in zip(bottoms, vals)]
    ax2.annotate("value 4%", (1.28, tot_a - 0.8), xytext=(4, 0), textcoords="offset points", va="center",
                 fontsize=8, color=INK_2)
    handles = [Patch(color=VAR_COLORS[k], label=k) for k in ["Value", "Other four factors", "Idio (residual)"]]
    ax2.legend(handles=handles, loc="upper right", fontsize=8)
    ax2.set_xticks(xs)
    ax2.set_xticklabels(["Before", "After"])
    ax2.set_xlim(-0.5, 2.2)
    ax2.set_ylim(0, 105)
    ax2.set_ylabel("Book P&L variance (September = 100)")
    finish(fig, "ch09_pair_book_value_loading")


if __name__ == "__main__":
    main()
