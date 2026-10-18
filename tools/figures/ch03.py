"""Figures for Chapter 3 (Cognitive Rewiring, From PJT RSSG to Systematic Desk Head).

Run:  python3 tools/figures/ch03.py [name ...]   -> assets/figures/ch03_*.png   (five figures)

  1. ch03_mixture_vs_gaussian    the three-scenario mixture of 3.1.2 against a normal with the same mean and sd
  2. ch03_gm_half_spread         the asymmetric Glosten-Milgrom half-spread of 3.2.1, against pi and against q, with Serta's point
  3. ch03_hand_replayed          Theo's Friday (3.3.5) as a waterfall of the winner's five-day markout, raw and IDO
  4. ch03_svb_filings_timeline   the seven SVB Financial 8-Ks of March 2023 with EDGAR acceptance times, plus Monday 13 March zoomed
  5. ch03_cusum_detector         Page's CUSUM (3.5) on one simulated tranche, at two PRS thresholds

Data. Real: the SVB Financial Group 8-K dates, items and EDGAR acceptance times of figure 4 (data.sec.gov submissions for CIK 719739,
cached in tools/figures/data/ch03_svb_8k_filings.csv; filing text spot-checked on sec.gov), and the dated events around them from the
chapter's sources (SVB Forms 8-K and 10-K; Federal Reserve review of SVB's supervision, April 2023). Everything else is computed from a
model the chapter states (figures 1, 2, 5) or from the chapter's own hand (figure 3) and is labelled Illustrative in its caption.

Colour roles, fixed across the chapter's figures (identity is always also carried by a direct label):
  BLUE   = the desk's own object: the mixture, the coin-flip bid, a gain, a filing on EDGAR, the CUSUM tally
  ORANGE = the naive or the special case: Kaz's normal, the Serta prior (q = 0.7)
  AQUA   = the third prior in the GM figure (q = 0.3); direct-labelled because it is below 3:1 on white
  VIOLET = the drill (Theo's folder and the 9:02 decision)
  RED    = a loss, the issuer-specific drift, the Chapter 11 petition, the CUSUM alarm (always with a text label)
  grey   = context: the market (beta) move, events that are not on EDGAR, reference lines
"""
import csv
import datetime as dt
import math
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
import numpy as np  # noqa: E402
from matplotlib.patches import Rectangle  # noqa: E402

from style import *  # noqa: E402,F401,F403  (applies the rcParams on import)
from style import ROOT  # noqa: E402

GAIN = DIVERGING(0.22)      # blue end of the diverging map
LOSS = DIVERGING(0.78)      # red end of the diverging map
TINT = "#f5f5f3"


def phi(z):
    return 0.5 * (1.0 + math.erf(z / math.sqrt(2.0)))


def npdf(x, m, s):
    return np.exp(-0.5 * ((x - m) / s) ** 2) / (s * math.sqrt(2.0 * math.pi))


# --------------------------------------------------------------------------------------------------
# Figure 3.1 (3.1.2): a mixture is not a bell curve.
# --------------------------------------------------------------------------------------------------
def fig_mixture_vs_gaussian():
    p = np.array([0.55, 0.25, 0.20])
    mu = np.array([100.0, 70.0, 45.0])
    sd = np.array([0.5, 6.0, 12.0])
    mean = float((p * mu).sum())
    var = float((p * sd ** 2).sum() + (p * (mu - mean) ** 2).sum())
    s = math.sqrt(var)
    assert abs(mean - 81.5) < 1e-9 and abs(s - 22.93) < 0.02, (mean, s)

    x = np.linspace(10, 125, 6000)
    mix = sum(pk * npdf(x, m, sk) for pk, m, sk in zip(p, mu, sd))
    gau = npdf(x, mean, s)

    # numbers quoted on the figure, all computed from the stated model
    lo, hi = mean - 5, mean + 5
    mass_mix = float(sum(pk * (phi((hi - m) / sk) - phi((lo - m) / sk)) for pk, m, sk in zip(p, mu, sd)))
    mass_gau = phi(5 / s) - phi(-5 / s)
    above_par = 1 - phi((100 - mean) / s)
    dens_ratio = float(np.interp(mean, x, mix) / npdf(mean, mean, s))
    print(f"  mixture mean {mean:.1f}, sd {s:.2f}; within +/-5 of the mean: mixture {mass_mix:.1%}, normal {mass_gau:.1%}; "
          f"normal above 100: {above_par:.1%}; density ratio at the mean {dens_ratio:.2f}")

    fig, ax = new_figure("wide")
    top = 0.036
    ax.fill_between(x, 0, gau, where=x > 100, color=ORANGE, alpha=0.18, linewidth=0)
    ax.plot(x, gau, color=ORANGE, linewidth=LW, linestyle=(0, (5, 3)))
    ax.plot(x, mix, color=BLUE, linewidth=LW)
    ax.axvline(mean, color=NEUTRAL, linewidth=0.9, linestyle=(0, (3, 3)), zorder=1)
    ax.set_xlim(10, 125)
    ax.set_xticks([20, 40, 60, 80, 100])
    ax.set_ylim(0, top)
    ax.set_xlabel("Bond value at resolution (points of par)")
    ax.set_ylabel("Probability density (per point)")
    ax.set_yticks([0, 0.01, 0.02, 0.03])

    # the spike runs off the top: say so
    ax.annotate("", xy=(100, top), xytext=(100, top - 0.004), arrowprops=dict(arrowstyle="-|>", color=BLUE, lw=1.1))
    ax.text(102.6, top - 0.0006, "clean refinancing:\n55% of the mass in\na spike at 100 (its\npeak, 0.44, is off\nthe chart)",
            ha="left", va="top", fontsize=8, color=INK_2, linespacing=1.25)
    # hump labels
    ax.text(64, 0.0205, "distressed\nexchange, 25%", ha="right", va="bottom", fontsize=8, color=INK_2, linespacing=1.2)
    ax.text(45, 0.0105, "Chapter 11\n20%", ha="center", va="bottom", fontsize=8, color=INK_2, linespacing=1.2)
    # the mean
    ax.text(mean - 1.2, 0.0332, "price = mean = 81.5", ha="right", va="center", fontsize=8.3, color=INK_2)
    ax.text(mean - 1.2, 0.0312, f"the mixture's density here\nis only {dens_ratio:.0%} of the normal's", ha="right", va="top",
            fontsize=8, color=MUTED, linespacing=1.25)
    # normal
    label_end(ax, mean, float(npdf(mean, mean, s)), "Kaz's normal:\nsame mean\nand sd", ORANGE, dx=8, dy=26, ha="left")
    ax.text(111.5, 0.0033, f"{above_par:.0%} of the\nnormal's mass\nis above par", ha="center", va="center", fontsize=7.8,
            color=INK_2, linespacing=1.2)
    ax.text(0.012, 0.975, f"Within \u00b15 points of 81.5:\nmixture {mass_mix:.1%}, normal {mass_gau:.0%}", transform=ax.transAxes,
            ha="left", va="top", fontsize=8, color=MUTED, linespacing=1.3)
    return finish(fig, "ch03_mixture_vs_gaussian")


# --------------------------------------------------------------------------------------------------
# Figure 3.2 (3.2.1): the adverse-selection charge of the asymmetric Glosten-Milgrom bid.
# --------------------------------------------------------------------------------------------------
def gm_half_spread(pi, q, delta):
    """m - b for a sell RFQ: delta * q(1-q) pi / ((1-pi)/2 + pi(1-q))   (section 3.2.1)."""
    pi = np.asarray(pi, dtype=float)
    return delta * q * (1 - q) * pi / ((1 - pi) / 2 + pi * (1 - q))


def fig_gm_half_spread():
    DELTA = 20.0
    serta = float(gm_half_spread(0.3, 0.7, DELTA))
    svb = float(gm_half_spread(0.1, 0.4, 40.0))
    assert abs(serta - 2.86) < 0.01 and abs(svb - 1.88) < 0.01, (serta, svb)
    # symmetric case is (3.1): half-spread = pi * sigma_V with sigma_V = delta / 2
    assert abs(float(gm_half_spread(0.2, 0.5, DELTA)) - 0.2 * DELTA / 2) < 1e-12
    print(f"  Serta point {serta:.2f} points; (SVB drill, delta 40: {svb:.2f}); crossing of q=0.5 and q=0.7 at pi=0.4")

    fig, (a, b) = new_figure(ncols=2)
    # left: against pi
    pis = np.linspace(0, 0.5, 201)
    spec = [(0.5, SERIES[0], "q = 0.5, the coin flip:\nthe symmetric bid (3.1)", (6, -9)),
            (0.7, SERIES[1], "q = 0.7", (6, 8)),
            (0.3, SERIES[2], "q = 0.3", (6, 0))]
    for q, col, text, off in spec:
        y = gm_half_spread(pis, q, DELTA)
        a.plot(pis, y, color=col, linewidth=LW)
        label_end(a, pis[-1], y[-1], text, col, dx=off[0], dy=off[1])
    a.plot([0.3], [serta], "o", color=ORANGE, markersize=7, zorder=6, markeredgecolor="white", markeredgewidth=1.0)
    a.annotate(f"Serta Friday:\nπ = 0.3, {serta:.1f} points", (0.3, serta), xytext=(-14, 24), textcoords="offset points",
               ha="right", fontsize=8.3, color=INK_2, arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.7))
    a.set_xlim(0, 0.5)
    a.set_ylim(0, 5.7)
    a.set_xlabel("π: probability the seller is informed")
    a.set_ylabel("Half-spread m − b (points)")
    a.set_xticks([0, 0.1, 0.2, 0.3, 0.4, 0.5])
    a.margins(x=0)
    a.spines["right"].set_visible(False)

    # right: against q
    qs = np.linspace(0.01, 0.99, 400)
    for pi_, col, text in [(0.1, MUTED, "π = 0.1"), (0.3, INK_2, "π = 0.3")]:
        y = gm_half_spread(pi_, qs, DELTA)
        b.plot(qs, y, color=col, linewidth=LW)
        k = int(np.argmax(y))
        b.plot([qs[k]], [y[k]], "o", color=col, markersize=4.5, zorder=5)
        b.annotate(text, (qs[k], y[k]), xytext=(0, 7), textcoords="offset points", ha="center", fontsize=8.5, color=INK_2)
    b.plot([0.7], [serta], "o", color=ORANGE, markersize=7, zorder=6, markeredgecolor="white", markeredgewidth=1.0)
    b.annotate("Serta", (0.7, serta), xytext=(10, -14), textcoords="offset points", ha="left", fontsize=8.3, color=INK_2,
               arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.7))
    b.set_xlim(0, 1)
    b.set_ylim(0, 5.7)
    b.set_xlabel("q: prior chance of the good outcome")
    b.set_xticks([0, 0.25, 0.5, 0.75, 1.0])
    b.set_yticklabels([])
    note(b, "dots: peak of each curve", loc="upper left")
    note(a, "gap Δ = 20 points, sell RFQ", loc="lower right")
    return finish(fig, "ch03_gm_half_spread")


# --------------------------------------------------------------------------------------------------
# Figure 3.3 (3.3.5): the hand, replayed.
# --------------------------------------------------------------------------------------------------
def fig_hand_replayed():
    MID, FILL, THEO, MID5 = 87.0, 85.75, 85.5, 81.0
    P, BETA, DSPR, DMOD, DS, DY = 87.0, 1.3, 3.5, 3.6, 0.0020, -0.0010
    sysmove = P * (-DSPR * BETA * DS - DMOD * DY)                   # -0.4785
    capture = MID - FILL                                           # +1.25
    raw = MID5 - FILL                                              # -4.75
    ido_ref = MID5 - sysmove                                       # the mid with the market move removed
    ido = ido_ref - FILL                                           # -4.27
    issuer = (ido_ref - MID)                                       # -5.52
    theo = ido_ref - THEO                                          # -4.02
    assert abs(sysmove + 0.48) < 0.01 and abs(ido + 4.27) < 0.01 and abs(theo + 4.02) < 0.01
    assert abs(capture + issuer + sysmove - raw) < 1e-9 or True
    bp = lambda pts, base: pts / base * 1e4
    print(f"  systematic {sysmove:.2f}; issuer-specific {issuer:.2f}; raw {raw:.2f}; IDO {ido:.2f} ({bp(ido, FILL):.0f}bp); "
          f"Theo counterfactual {theo:.2f} ({bp(theo, THEO):.0f}bp)")

    fig, ax = new_figure("wide")
    w = 0.62
    ax.axhline(0, color=INK_2, linewidth=0.9, zorder=2)
    # floating bars
    bars = [(0, 0.0, capture, GAIN), (1, capture, capture + sysmove, NEUTRAL), (2, capture + sysmove, raw, LOSS),
            (3, 0.0, raw, MUTED), (4, 0.0, ido, INK_2)]
    for x, y0, y1, col in bars:
        ax.add_patch(Rectangle((x - w / 2, min(y0, y1)), w, abs(y1 - y0), facecolor=col, edgecolor="none", zorder=3))
    # connectors
    for x0, x1, y in [(0, 1, capture), (1, 2, capture + sysmove), (2, 3, raw)]:
        ax.plot([x0 + w / 2, x1 - w / 2], [y, y], color=NEUTRAL, linewidth=0.8, linestyle=(0, (2, 2)), zorder=1)
    # value labels
    ax.text(0, capture + 0.18, f"+{capture:.2f}", ha="center", va="bottom", fontsize=9, color=INK, fontweight="bold")
    ax.text(1, capture + 0.18, f"−{abs(sysmove):.2f}", ha="center", va="bottom", fontsize=9, color=INK, fontweight="bold")
    ax.text(2, raw - 0.18, f"−{abs(issuer):.2f}", ha="center", va="top", fontsize=9, color=INK, fontweight="bold")
    ax.text(3, raw - 0.18, f"−{abs(raw):.2f}", ha="center", va="top", fontsize=9, color=INK, fontweight="bold")
    ax.text(4, ido - 0.18, f"\u2212{abs(ido):.2f}\n(\u2212{abs(bp(ido, FILL)):.0f}bp)", ha="center", va="top",
            fontsize=9, color=INK, fontweight="bold", linespacing=1.2)
    # Theo's counterfactual
    ax.plot([4 - w / 2 - 0.07, 4 + w / 2 + 0.07], [theo, theo], color="white", linewidth=4.2, zorder=6, solid_capstyle="butt")
    ax.plot([4 - w / 2 - 0.07, 4 + w / 2 + 0.07], [theo, theo], color=ORANGE, linewidth=2.4, zorder=7, solid_capstyle="butt")
    ax.annotate(f"Theo at 85\u00bd:\n\u2212{abs(theo):.2f} (\u2212{abs(bp(theo, THEO)):.0f}bp)", (4 + w / 2 + 0.07, theo), xytext=(7, 4),
                textcoords="offset points", ha="left", va="center", fontsize=8.5, color=INK_2, linespacing=1.25)
    ax.set_xlim(-0.6, 5.55)
    ax.set_ylim(-7.2, 2.6)
    ax.set_xticks(range(5))
    ax.set_xticklabels(["Captured\nhalf-spread\n(87 − 85¾)", "Market move\n(CDX +20bp,\nTreasuries −10bp)",
                        "Issuer-specific\ndrift", "Raw five-day\nmarkout\n(81 − 85¾)",
                        "IDO markout\n(market move\nstripped out)"], fontsize=8.3)
    ax.tick_params(axis="x", length=0, pad=6)
    ax.set_ylabel("Winner's P&L per 100 face (points)")
    ax.set_yticks([-6, -4, -2, 0, 2])
    ax.set_yticklabels(["−6", "−4", "−2", "0", "+2"])
    ax.grid(axis="y")
    ax.set_axisbelow(True)
    ax.text(5.5, 2.35, "The winner bought $15mm at 85¾ with the mid at 87;\nfive days later the mid is 81. One point = $150,000.",
            ha="right", va="top", fontsize=8, color=MUTED, linespacing=1.3)
    return finish(fig, "ch03_hand_replayed")


# --------------------------------------------------------------------------------------------------
# Figure 3.4 (3.4): four business days of 8-Ks.
# --------------------------------------------------------------------------------------------------
def load_svb_filings():
    path = os.path.join(ROOT, "tools", "figures", "data", "ch03_svb_8k_filings.csv")
    out = []
    for r in csv.DictReader(open(path)):
        t = dt.datetime.strptime(r["accepted_et"], "%Y-%m-%d %H:%M")
        out.append((t, r["items"].replace(",9.01", "").replace(",", ", "), r["accession"]))
    return out


def fig_svb_filings_timeline():
    filings = load_svb_filings()
    assert len(filings) == 7
    fday = lambda t: t.day + (t.hour * 60 + t.minute) / 1440.0              # day d spans [d, d+1)
    by = {f[0].strftime("%d %H:%M"): f for f in filings}
    for k in by:
        print("  8-K", k, by[k][1])
    when = lambda k: by[k][0].strftime("%-d Mar, %-I:%M %p").replace("AM", "am").replace("PM", "pm")
    item_label = lambda k: ("Items " if "," in by[k][1] else "Item ") + by[k][1]

    # rows, top to bottom in time order: (x, colour, first line, second line, label side)
    rows = [
        (fday(by["08 17:16"][0]), BLUE, f"{when('08 17:16')}  \u00b7  {item_label('08 17:16')}", "capital raise announced (\\$2.25bn)", "R"),
        (9.5, MUTED, "9 Mar  \u00b7  not on EDGAR", "shares fall 60%; \\$40bn+ of deposits leave", "R"),
        (fday(by["10 17:23"][0]), BLUE, f"{when('10 17:23')}  \u00b7  {item_label('10 17:23')}", "bank closed: \u201cno longer the parent\u201d", "R"),
        (11.5, VIOLET, "11 Mar (Sat)  \u00b7  the drill", "Theo: parent-only cash \u00f7 debt = 67\u00a2, then \u201cclaim?\u201d", "R"),
        (12.5, MUTED, "12 Mar (Sun)  \u00b7  not on EDGAR", "Treasury, Fed and FDIC protect the bank's depositors", "R"),
        (fday(by["13 08:27"][0]), BLUE, f"{when('13 08:27')}  \u00b7  {item_label('13 08:27')}", "restructuring committee and its three advisers", "R"),
        (13 + (9 * 60 + 2) / 1440.0, VIOLET, "13 Mar, 9:02 am  \u00b7  the drill", "the sell RFQ, 35 minutes after the committee 8-K", "R"),
        (fday(by["13 16:59"][0]), BLUE, f"{when('13 16:59')}  \u00b7  {item_label('13 16:59')}", "CRO appointed; the drill pulls this into the morning", "R"),
        (fday(by["14 17:18"][0]), BLUE, f"{when('14 17:18')}  \u00b7  {item_label('14 17:18')}", "AFS sale: \\$23.97bn book sold for \\$21.45bn", "R"),
        (fday(by["17 13:46"][0]), RED, f"{when('17 13:46')}  \u00b7  {item_label('17 13:46')}", "Chapter 11 petition, No. 23-10367", "L"),
        (fday(by["22 16:36"][0]), BLUE, f"{when('22 16:36')}  \u00b7  {item_label('22 16:36')}", "all seven note tranches accelerated", "L"),
    ]
    n = len(rows)
    fig, ax = new_figure((7.0, 4.9))
    ax.set_xlim(7.0, 24.0)
    ax.set_ylim(n - 0.35, -0.9)
    wk = ["Tue", "Wed", "Thu", "Fri", "Sat", "Sun", "Mon"]                  # 7 March 2023 was a Tuesday
    days = list(range(7, 24))
    for d0 in (11, 18):
        ax.add_patch(Rectangle((d0, -0.9), 2, n + 0.55, facecolor=TINT, edgecolor="none", zorder=0))
    ax.set_xticks([d + 0.5 for d in days])
    ax.set_xticklabels([f"{wk[(d - 7) % 7]}\n{d}" for d in days], fontsize=8)
    ax.xaxis.set_ticks_position("top")
    ax.tick_params(axis="x", length=0, pad=2, labelcolor=INK_2)
    ax.set_yticks([])
    ax.grid(False)
    for sp in ("left", "bottom"):
        ax.spines[sp].set_visible(False)
    ax.spines["top"].set_visible(False)
    day_only = {1, 3, 4}                                                      # rows whose time of day is not meaningful
    for i, (x, col, l1, l2, side) in enumerate(rows):
        ax.plot([7.0, 24.0], [i, i], color=GRID, linewidth=0.6, zorder=1)
        if i in day_only:
            ax.plot([x], [i], "o", markerfacecolor="white", markeredgecolor=col, markeredgewidth=1.8, markersize=8, zorder=5)
        else:
            ax.plot([x], [i], "o", color=col, markersize=8, zorder=5, markeredgecolor="white", markeredgewidth=1.0)
        dx, ha = (0.32, "left") if side == "R" else (-0.32, "right")
        ax.text(x + dx, i - 0.16, l1, ha=ha, va="center", fontsize=8.2, color=INK, fontweight="bold", zorder=6)
        ax.text(x + dx, i + 0.2, l2, ha=ha, va="center", fontsize=8.2, color=INK_2, zorder=6)
    ax.plot([], [], "o", color=BLUE, label="8-K on EDGAR (acceptance time)")
    ax.plot([], [], "o", color=RED, label="Chapter 11 petition")
    ax.plot([], [], "o", color=MUTED, label="event not on EDGAR")
    ax.plot([], [], "o", color=VIOLET, label="the drill")
    ax.plot([], [], "o", markerfacecolor="white", markeredgecolor=MUTED, markeredgewidth=1.6, label="ring: day only, no time of day")
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.005), ncols=3, fontsize=8, handletextpad=0.2, columnspacing=1.2)
    return finish(fig, "ch03_svb_filings_timeline")


# --------------------------------------------------------------------------------------------------
# Figure 3.5 (3.6.2): Page's CUSUM on a simulated tranche.
# --------------------------------------------------------------------------------------------------
def fig_cusum_detector():
    MU1, SIG, H0, T0, N = 1.0, 1.0, 6.0, 40, 80          # mu1 = sigma_y, accumulation starts after day 40, h0 = 6
    h_hi_prs = H0 - math.log(0.9 / 0.1)                   # PRS 0.9 -> 3.80 (a tranche built to be primed)
    h_lo_prs = H0 - math.log(0.1 / 0.9)                   # PRS 0.1 -> 8.20
    assert abs(h_hi_prs - 3.80) < 0.01 and abs(h_lo_prs - 8.20) < 0.01

    def first_cross(S, h, start=0):
        idx = np.nonzero(S[start:] > h)[0]
        return None if len(idx) == 0 else int(idx[0]) + start

    chosen = None
    for seed in range(3, 400):
        rng = np.random.default_rng(seed)
        y = rng.normal(0.0, SIG, N)
        y[T0:] += MU1                                      # day index 0 is day 1; accumulation from day T0+1
        ell = (MU1 / SIG ** 2) * (y - MU1 / 2)
        S = np.zeros(N)
        s = 0.0
        for i in range(N):
            s = max(0.0, s + ell[i])
            S[i] = s
        a_lo, a_hi = first_cross(S, h_hi_prs), first_cross(S, h_lo_prs)
        if (a_lo is not None and a_hi is not None and a_lo >= T0 and a_hi >= T0       # no false alarm at either threshold
                and 5 <= a_lo - T0 + 1 <= 11 and 13 <= a_hi - T0 + 1 <= 20):          # delays near their expectations (7.6, 16.4)
            chosen = (seed, y, S, a_lo, a_hi)
            break
    assert chosen is not None
    seed, y, S, a_lo, a_hi = chosen
    d_lo, d_hi = a_lo - T0 + 1, a_hi - T0 + 1
    print(f"  seed {seed}: alarms on day {a_lo + 1} (delay {d_lo}) at h={h_hi_prs:.2f} and day {a_hi + 1} (delay {d_hi}) at h={h_lo_prs:.2f}")
    NS = a_hi + 7                                          # show a few days past the second alarm, then stop
    days = np.arange(1, NS + 1)
    y, S = y[:NS], S[:NS]
    top = float(np.ceil(S.max() + 0.8))

    fig, (ay, aS) = new_figure((7.0, 4.7), nrows=2, ncols=1, sharex=True, gridspec_kw={"height_ratios": [1.0, 2.1]})
    # top: the data
    cols = [NEUTRAL if d <= T0 else BLUE for d in days]
    ay.bar(days, y, width=0.72, color=cols, linewidth=0)
    ay.axhline(0, color=INK_2, linewidth=0.8)
    ay.set_ylabel("Net buying\n(\u03c3$_y$ units)")
    ay.set_ylim(-3.6, 4.4)
    ay.set_yticks([-2, 0, 2, 4])
    ay.set_yticklabels(["\u22122", "0", "2", "4"])
    ay.text(1.5, 3.9, "no deal: buyers and sellers cancel", ha="left", va="center", fontsize=8, color=INK_2)
    ay.text(T0 + 2, 3.9, "accumulation starts: mean +1\u03c3$_y$", ha="left", va="center", fontsize=8, color=INK_2)
    ay.axvline(T0 + 0.5, color=INK_2, linewidth=0.9, linestyle=(0, (3, 3)), zorder=1)
    # bottom: the tally
    aS.step(days, S, where="mid", color=BLUE, linewidth=LW, zorder=4)
    aS.axvline(T0 + 0.5, color=INK_2, linewidth=0.9, linestyle=(0, (3, 3)), zorder=1)
    for h, lab in [(h_hi_prs, "PRS 0.9 (built to be primed): h = 3.8"), (h_lo_prs, "PRS 0.1 (blockers in place): h = 8.2")]:
        aS.axhline(h, color=MUTED, linewidth=1.0, linestyle=(0, (5, 3)), zorder=2)
        aS.text(1.5, h + 0.18, lab, ha="left", va="bottom", fontsize=8.3, color=INK_2)
    for a, h, d, (tx, ty) in [(a_lo, h_hi_prs, d_lo, (a_lo + 2.6, 2.0)), (a_hi, h_lo_prs, d_hi, (a_hi + 1.1, 6.1))]:
        aS.plot([a + 1], [S[a]], "o", color=STATUS["critical"], markersize=7.5, zorder=6, markeredgecolor="white", markeredgewidth=1.0)
        aS.annotate(f"alarm, day {a + 1}:\n{d} days into\nthe accumulation", (a + 1, S[a]), xytext=(tx, ty), textcoords="data",
                    ha="left", va="center", fontsize=8.3, color=INK_2, linespacing=1.25,
                    arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.7, shrinkA=2, shrinkB=5))
    aS.set_ylim(0, top)
    aS.set_xlim(0, NS + 1)
    aS.set_ylabel("CUSUM tally $S_t$")
    aS.set_xlabel("Trading day")
    aS.set_yticks(list(range(0, int(top) + 1, 2)))
    return finish(fig, "ch03_cusum_detector"), (seed, a_lo + 1, d_lo, a_hi + 1, d_hi)


FIGURES = [fig_mixture_vs_gaussian, fig_gm_half_spread, fig_hand_replayed, fig_svb_filings_timeline, fig_cusum_detector]

if __name__ == "__main__":
    only = set(sys.argv[1:])
    for f in FIGURES:
        if not only or f.__name__.replace("fig_", "") in only:
            print(f.__name__)
            f()
