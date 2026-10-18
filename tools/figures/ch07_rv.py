"""Relative-value figure for Chapter 7 (ML on Small-Sample Credit Data), the Pair Book panel in section 7.4.

Run:  python3 tools/figures/ch07_rv.py   -> assets/figures/ch07_pair_corridor.png

Kept apart from any later tools/figures/ch07.py so the chapter's other figures can be drawn without touching it.

What it draws. One 13-week corridor from the platform pair screen's six-year panel (fictional), for a pair with
PB-19's sizes: long DTS 0.081 (spread duration 4.5 at 180 bp), short sized 1.50x by market-value DTS (4.5 at
120 bp), so the pair carries nothing and its spread return per dollar of long is -DTS_L * (dlog s_L - dlog s_S).
Barriers: +/- DTS_L * sigma_diff * sqrt(h) with sigma_diff = 9% * sqrt(2 * (1 - 0.8)) = 5.7% a month (two legs
at the book's 9% prior, correlated 0.8) and h = 3 months: +/- 0.80% of long market value, about $320k on $40mm.
Vertical barrier at 63 trading days; dead zone +/- 0.25% of the long at the wall.

Two residual definitions of the same simulated pair:
  ORANGE = research's residual (market beta, DTS-scaled market move and carry stripped): the naive label;
  BLUE   = the residual of the risk manager's whole factor sheet (adds rating bucket and sector): the honest label;
  NEUTRAL dashed = their difference, the rating-bucket factor the first label called idio.
The path is simulated (seed chosen so the two labels differ as the scene describes); nothing here is market data.
Colour roles follow tools/figures/ch07b.py: ORANGE naive, BLUE corrected, NEUTRAL reference.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
import numpy as np  # noqa: E402

from style import *  # noqa: E402,F401,F403

plt.rcParams["text.parse_math"] = False      # "$" is a dollar sign here

H_DAYS = 63
BARRIER = 0.081 * 0.057 * np.sqrt(3) * 100     # half-width, % of long market value (about 0.80)
DEAD = 0.25                                    # dead zone at the wall, % of long
SIG_SHEET = 0.090                              # daily s.d. of the whole-sheet residual, % of long
SIG_BUCKET = 0.040                             # daily s.d. of the rating-bucket factor's contribution
MU_BUCKET = 0.0095                             # daily drift of the bucket factor in the sample window


def find_path():
    """Search seeds for a path on which the two residual definitions give the labels the scene describes."""
    for seed in range(20260902, 20260902 + 20000):
        rng = np.random.default_rng(seed)
        sheet = np.concatenate([[0.0], np.cumsum(rng.normal(0.0, SIG_SHEET, H_DAYS))])
        bucket = np.concatenate([[0.0], np.cumsum(rng.normal(MU_BUCKET, SIG_BUCKET, H_DAYS))])
        research = sheet + bucket
        up = np.nonzero(research >= BARRIER)[0]
        if len(up) == 0 or not (30 <= up[0] <= 36):
            continue
        if research[: up[0]].min() <= -0.45:
            continue
        if sheet.max() >= BARRIER - 0.20 or sheet.min() <= -BARRIER + 0.25:
            continue
        if not (0.08 <= sheet[-1] <= 0.20):
            continue
        if not (0.30 <= bucket[up[0]] <= 0.40):
            continue
        return seed, research, sheet, bucket, int(up[0])
    raise SystemExit("no seed found")


def fig_pair_corridor():
    seed, research, sheet, bucket, t_up = find_path()
    days = np.arange(H_DAYS + 1)
    fig, ax = new_figure("wide")

    for y in (BARRIER, -BARRIER):
        ax.axhline(y, color=INK_2, linewidth=0.9, linestyle=(0, (4, 3)), zorder=1)
    ax.axvline(H_DAYS, color=INK_2, linewidth=0.9, linestyle=(0, (4, 3)), zorder=1)
    ax.plot([H_DAYS, H_DAYS], [-DEAD, DEAD], color=MUTED, linewidth=4.0, alpha=0.6, solid_capstyle="butt", zorder=2)
    ax.annotate("dead zone", (H_DAYS, -DEAD), xytext=(-6, -2), textcoords="offset points",
                ha="right", va="top", fontsize=8, color=INK_2)

    ax.plot(days, bucket, color=NEUTRAL, linewidth=1.2, linestyle=(0, (2, 2)), zorder=2)
    ax.plot(days[: t_up + 1], research[: t_up + 1], color=ORANGE, zorder=3)
    ax.plot(days[t_up:], research[t_up:], color=ORANGE, alpha=0.25, zorder=2)
    ax.plot(days, sheet, color=BLUE, zorder=4)

    ax.plot([t_up], [research[t_up]], "o", color=ORANGE, markersize=6, zorder=5)
    ax.annotate("research's residual touches the ceiling\nin week %d: label +1" % (t_up // 5 + 1),
                (t_up, research[t_up]), xytext=(-8, 10), textcoords="offset points",
                ha="right", va="bottom", fontsize=8, color=INK_2)
    ax.plot([H_DAYS], [sheet[-1]], "o", color=BLUE, markersize=6, zorder=5)
    ax.annotate("whole-sheet residual reaches\nthe wall inside the dead zone: label 0",
                (H_DAYS, sheet[-1]), xytext=(H_DAYS - 2, -0.50), textcoords="data",
                ha="right", va="top", fontsize=8, color=INK_2,
                arrowprops=dict(arrowstyle="-", color=MUTED, linewidth=0.7))
    ax.annotate("rating-bucket factor\n(the difference)", (54, bucket[54]), xytext=(40, -0.30),
                textcoords="data", ha="center", va="top", fontsize=8, color=INK_2,
                arrowprops=dict(arrowstyle="-", color=MUTED, linewidth=0.7))

    ax.text(1, BARRIER + 0.04, "ceiling  +%.2f%% of the long (about $320k)" % BARRIER,
            fontsize=8, color=INK_2, va="bottom")
    ax.text(1, -BARRIER - 0.04, "floor  %s%.2f%%" % ("−", BARRIER), fontsize=8, color=INK_2, va="top")
    ax.text(H_DAYS - 1, 1.12, "wall, 13 weeks", fontsize=8, color=INK_2, ha="right", va="bottom")

    ax.set_xlim(0, H_DAYS + 1)
    ax.set_ylim(-1.2, 1.3)
    ax.set_xticks([0, 10, 20, 30, 40, 50, 60])
    ax.set_xticklabels(["0", "2", "4", "6", "8", "10", "12"])
    ax.set_xlabel("Weeks since formation")
    ax.set_ylabel("Cumulative residual differential\n(% of long market value)")
    ax.axhline(0, color=GRID, linewidth=0.8, zorder=0)
    print(f"seed {seed}: touch day {t_up} (week {t_up // 5 + 1}), research {research[t_up]:.3f}, "
          f"bucket at touch {bucket[t_up]:.3f}, sheet at touch {sheet[t_up]:.3f}, sheet at wall {sheet[-1]:.3f}, "
          f"sheet range [{sheet.min():.3f}, {sheet.max():.3f}], barrier {BARRIER:.3f}")
    return finish(fig, "ch07_pair_corridor")


if __name__ == "__main__":
    fig_pair_corridor()
