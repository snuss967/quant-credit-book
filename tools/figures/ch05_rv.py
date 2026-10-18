"""Relative-value figure for Chapter 5 (Probability Distributions), the Pair Book beat in section 5.1.4.

Run:  python3 tools/figures/ch05_rv.py   -> assets/figures/ch05_pair_two_spikes.png

Kept apart from any later tools/figures/ch05.py so the chapter's other figures can be drawn without touching it.

What it draws. Pair Book entry PB-01 (Dov Adler's pod, fictional; Kestrel Roofing invented, Halvorsen the book's
fictional issuer) as it stood in April: long $60mm Kestrel 6% 2030 at 96 (350 bp, spread duration 3.6), short
$39mm Halvorsen 7.25% 2029 at 90 (600 bp, 3.4), matched on market-value DTS. One-year P&L, simulated leg by leg
with the chapter's survive-or-jump mixture (section 5.1.2):
  - default odds = spread / (1 - 0.40), read as one-year probabilities: Kestrel 5.8%, Halvorsen 10%; independent;
  - a leg that survives contributes its idio wobble, normal with 30% relative spread volatility a year
    (Kestrel s.d. $2.18mm; Halvorsen s.d. $2.15mm and a +$1.19mm thesis drift, 100 bp of underperformance);
  - a leg that defaults contributes face x (price - recovery), signed: left panel at recovery 40 on both,
    right panel with recovery drawn from Beta(mean 0.40, s.d. 0.275), the section 5.1.4 Moody's moments.
All inputs are the chapter's illustrative numbers; nothing here is market data.
Colours: BLUE = the pair's P&L (the only series); NEUTRAL dashed line = Dov's first line from the high-water mark.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
import numpy as np  # noqa: E402
from matplotlib.ticker import FixedLocator, FuncFormatter, NullLocator  # noqa: E402

from style import *  # noqa: E402,F401,F403

plt.rcParams["text.parse_math"] = False      # "$" is a dollar sign here

RNG = np.random.default_rng(20260922)
N_SIMS = 2_000_000

K_FACE, K_PX, K_SD, K_S = 60.0, 0.96, 3.6, 0.0350      # long Kestrel
H_FACE, H_PX, H_SD, H_S = 39.0, 0.90, 3.4, 0.0600      # short Halvorsen
R_MEAN, R_SDEV = 0.40, 0.275
REL_VOL = 0.30                                         # idio relative spread volatility, a year
THESIS = H_FACE * H_PX * H_SD * 0.01                   # 100 bp of Halvorsen underperformance, about $1.19mm
FIRST_LINE = -24.0                                     # high-water mark to the first line, section 1B.2


def beta_params(m, s):
    k = m * (1 - m) / s ** 2 - 1
    return m * k, (1 - m) * k


def simulate(beta_recovery):
    q_k = K_S / (1 - R_MEAN)
    q_h = H_S / (1 - R_MEAN)
    d_k = RNG.random(N_SIMS) < q_k
    d_h = RNG.random(N_SIMS) < q_h
    if beta_recovery:
        a, b = beta_params(R_MEAN, R_SDEV)
        r_k = RNG.beta(a, b, N_SIMS)
        r_h = RNG.beta(a, b, N_SIMS)
    else:
        r_k = np.full(N_SIMS, R_MEAN)
        r_h = np.full(N_SIMS, R_MEAN)
    wob_k = RNG.normal(0.0, K_FACE * K_PX * K_SD * K_S * REL_VOL, N_SIMS)
    wob_h = RNG.normal(THESIS, H_FACE * H_PX * H_SD * H_S * REL_VOL, N_SIMS)
    long_leg = np.where(d_k, -K_FACE * (K_PX - r_k), wob_k)
    short_leg = np.where(d_h, H_FACE * (H_PX - r_h), wob_h)
    return long_leg + short_leg


def panel(ax, pnl, show_ylabel, labels):
    bins = np.arange(-62, 46, 1.0)
    hist, edges = np.histogram(pnl, bins=bins)
    prob = hist / len(pnl)
    centers = 0.5 * (edges[:-1] + edges[1:])
    ax.bar(centers, np.where(prob > 0, prob, np.nan), width=0.9, color=BLUE, zorder=3)
    ax.set_yscale("log")
    ax.set_ylim(1e-5, 0.4)
    ax.yaxis.set_major_locator(FixedLocator([1e-5, 1e-4, 1e-3, 1e-2, 1e-1]))
    ax.yaxis.set_minor_locator(NullLocator())
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{100 * v:g}%"))
    ax.set_xlim(-62, 45)
    ax.set_xlabel("One-year pair P&L ($mm)")
    if show_ylabel:
        ax.set_ylabel("Probability per $1mm bin (log scale)")
    ax.axvline(FIRST_LINE, color=NEUTRAL, linewidth=0.9, linestyle=(0, (3, 3)), zorder=1)
    ax.annotate("first line,\n−$24mm", (FIRST_LINE, 0.98), xycoords=("data", "axes fraction"), xytext=(-3, 0),
                textcoords="offset points", fontsize=8, color=INK_2, va="top", ha="right")
    for x, y, text, ha in labels:
        ax.annotate(text, (x, y), fontsize=8, color=INK_2, ha=ha, va="bottom")


def fig_pair_two_spikes():
    fixed = simulate(beta_recovery=False)
    smear = simulate(beta_recovery=True)
    fig, axes = new_figure("wide", ncols=2, sharey=True)
    panel(axes[0], fixed, True, [
        (-43.0, 1.6e-2, "Kestrel defaults\n5.8%: −$33.6mm", "center"),
        (33.0, 3.0e-2, "Halvorsen defaults\n10%: +$19.5mm", "center"),
        (6.0, 0.14, "both survive, 85%", "left"),
        (-14.1, 8e-3, "both\n0.6%", "center"),
    ])
    axes[0].set_title("Recovery fixed at 40", fontsize=9, fontweight="normal", color=INK_2)
    panel(axes[1], smear, False, [
        (-45.0, 3.0e-3, "Kestrel defaults:\nlands anywhere", "center"),
        (27.0, 1.1e-2, "Halvorsen defaults:\nlands anywhere", "center"),
    ])
    axes[1].set_title("Recovery Beta, mean 40, s.d. 27.5", fontsize=9, fontweight="normal", color=INK_2)
    print(f"fixed: mean {fixed.mean():.3f} sd {fixed.std():.3f} P(<-24) {np.mean(fixed < FIRST_LINE):.4f}")
    print(f"beta:  mean {smear.mean():.3f} sd {smear.std():.3f} P(<-24) {np.mean(smear < FIRST_LINE):.4f}")
    return finish(fig, "ch05_pair_two_spikes")


if __name__ == "__main__":
    fig_pair_two_spikes()
