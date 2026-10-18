"""Relative-value figure for Chapter 8-C (The Morning Explain), the Pair Book beat in section 8C.6, Morning (c).

Run:  python3 tools/figures/ch08c_rv.py   -> assets/figures/ch08c_pair_explain_waterfall.png

Kept apart from tools/figures/ch08c.py so the chapter's five other figures can be redrawn without touching it.

What it draws. One pair's day, PB-01 (Dov Adler's Kestrel/Halvorsen pair; fictional composite), Tuesday
13 October 2026, regrouped from the explain's lines into the four groups of a pair explain: idio (the thesis),
leak (what the hedge failed to remove), friction (what the pair paid to exist) and net. Left panel: the market
line priced with the start-of-day ratio, the one the 7:15 x-ray drew (long DTS 70,200 against short 98,000).
Right panel: the same day priced with the 4:00 ratio (short trimmed to $35mm face at 2:40 plus about $13mm of
CDX HY protection sold, so the ratio is flat), which moves the morning's -$55,600 market line into idio.
Net is identical in both panels; only the split, and so the capture ratio (net / idio), changes.

Inputs (all illustrative, the chapter's numbers): HY spreads 2% tighter, most of it before ten; Kestrel 3 bp
tighter and Halvorsen 10 bp wider on their own; Treasuries 0.5 bp higher against about $12,000 of net DV01;
carry = accrual +10,000, coupon owed -7,850, pull-to-par +1,170 and -5,970; borrow fee 300 bp on $30.42mm
(-2,540); financing net of rebate -1,670; day-one on the cover -16,000; CDX half-spread -4,000.
Colours: diverging blue for gains and red for losses (polarity), INK for the net bar.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from style import *  # noqa: E402,F401,F403

plt.rcParams["text.parse_math"] = False      # "$" is a dollar sign here

GAIN, LOSS = "#3987e5", "#e66767"            # DIVERGING endpoints at mid strength

# $ thousands
IDIO_LONG, IDIO_SHORT = 62.9, 70.0
MKT_LONG, MKT_SHORT = 140.4, -196.0
RATES = -6.0
CARRY = 10.0 - 7.85 + 1.17 - 5.97
FEE, FIN, DAY_ONE, CDX_HS = -2.54, -1.67, -16.0, -4.0


def groups(start_of_day=True):
    idio = IDIO_LONG + IDIO_SHORT
    market = MKT_LONG + MKT_SHORT
    leak = RATES + (market if start_of_day else 0.0)
    if not start_of_day:
        idio += market
    friction = CARRY + FEE + FIN + DAY_ONE + CDX_HS
    net = idio + leak + friction
    return idio, leak, friction, net


def draw(ax, start_of_day, title):
    idio, leak, friction, net = groups(start_of_day)
    labels = ["Idio", "Leak", "Friction", "Net"]
    steps = [idio, leak, friction]
    level = 0.0
    for i, v in enumerate(steps):
        bottom = level if v >= 0 else level + v
        ax.bar(i, abs(v), bottom=bottom, width=0.62, color=GAIN if v >= 0 else LOSS, zorder=3)
        ax.annotate(f"{v:+,.1f}", (i, level + v), xytext=(0, 3 if v >= 0 else -11),
                    textcoords="offset points", ha="center", fontsize=8.5, color=INK_2)
        if i < len(steps):
            ax.plot([i + 0.31, i + 0.69], [level + v, level + v], color=NEUTRAL, linewidth=0.8, zorder=2)
        level += v
    ax.bar(3, net, width=0.62, color=INK, zorder=3)
    ax.annotate(f"{net:+,.1f}", (3, net), xytext=(0, 3), textcoords="offset points", ha="center",
                fontsize=8.5, color=INK_2)
    ax.axhline(0, color=NEUTRAL, linewidth=0.8, zorder=2)
    ax.set_xticks(range(4))
    ax.set_xticklabels(labels)
    ax.set_ylim(0, 150)
    ax.set_title(title, fontsize=9, loc="left")
    note(ax, f"Capture = net / idio = {net / idio:.2f}", loc="upper right")
    return idio, leak, friction, net


def main():
    fig, axes = new_figure((7.0, 3.4), ncols=2, sharey=True)
    a = draw(axes[0], True, "Start-of-day ratio (the 7:15 x-ray)")
    b = draw(axes[1], False, "The 4:00 ratio (after the 2:40 trim)")
    axes[0].set_ylabel("PB-01, Tuesday 13 Oct 2026 ($ thousands)")
    print("start-of-day: idio %.1f leak %.1f friction %.2f net %.2f kappa %.3f" % (*a, a[3] / a[0]))
    print("4:00 ratio:   idio %.1f leak %.1f friction %.2f net %.2f kappa %.3f" % (*b, b[3] / b[0]))
    finish(fig, "ch08c_pair_explain_waterfall")


if __name__ == "__main__":
    main()
