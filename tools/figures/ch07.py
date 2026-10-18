"""Chapter 7 figures (Machine Learning on Small-Sample, Non-Stationary Credit Data), Edition 2, task U4.

Run:  python3 tools/figures/ch07.py      (writes assets/figures/ch07_*.png, except ch07_pair_corridor)

ch07_pair_corridor.png (section 7.4, Figure 7.2) is drawn by tools/figures/ch07_rv.py and is not touched here.

  1. ch07_ffd_weights        section 7.3  fractional-differentiation weights and the memory they keep (model, exact recursion)
  2. ch07_hat_count          section 7.6  from 212,000 bond-months to 24,000 hats to 79 regime windows (illustrative arithmetic)
  3. ch07_purged_folds       section 7.7  purged, embargoed, parent-grouped split: the grid and one parent's labels (schematic)
  4. ch07_dsr_noise_max      section 7.8  expected best Sharpe of N pure-noise strategies (formula of 7.8, plus a simulation check)
  5. ch07_reversal_gap       section 7.9  short-term reversal, textbook vs signal gap vs return gap (REAL: Dickerson-Robotti-Rossetti 2026)

Colour roles, fixed across this chapter's figures (same as ch07_rv.py and ch07b.py):
  ORANGE = the naive / textbook answer (212,000 rows, same-price signal and return, the measured Sharpe, the test cell)
  BLUE   = the honest / corrected answer (hats, signal gap, noise-max curve, training labels)
  NEUTRAL / INK_2 = reference levels and set-aside material; hatching = removed (purged, embargoed)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
import numpy as np  # noqa: E402
from matplotlib.patches import Patch, Rectangle  # noqa: E402
from matplotlib.ticker import FuncFormatter  # noqa: E402
from scipy.stats import norm  # noqa: E402

from style import *  # noqa: E402,F401,F403

plt.rcParams["text.parse_math"] = False      # "$" is a dollar sign in these figures
MINUS = "−"
C_NAIVE, C_FIX = ORANGE, BLUE
HATCH_PURGE, HATCH_EMBARGO = "////", "xxxx"


# --------------------------------------------------------------------------------------------
# 1. Fractional-differentiation weights (section 7.3)
# --------------------------------------------------------------------------------------------
def ffd_weights(d, n):
    """w_0..w_n by the recursion of section 7.3: w_0 = 1, w_k = -w_{k-1} (d - k + 1) / k."""
    w = np.empty(n + 1)
    w[0] = 1.0
    for k in range(1, n + 1):
        w[k] = -w[k - 1] * (d - k + 1) / k
    return w


SUP = {"0": "\u2070", "1": "\u00b9", "2": "\u00b2", "3": "\u00b3", "4": "\u2074", "5": "\u2075", "6": "\u2076",
       "-": "\u207b"}


def pow10_label(v, _=None):
    """10^e as 10 with a unicode superscript (mathtext is off)."""
    e = int(round(np.log10(v)))
    return "1" if e == 0 else "10" + "".join(SUP[ch] for ch in str(e))


def fig_ffd_weights():
    n = 1000
    ds = [(0.2, SERIES[0]), (0.4, SERIES[1]), (0.6, SERIES[2])]
    tau = 1e-4
    fig, (a, b) = new_figure("wide", ncols=2, gridspec_kw={"width_ratios": [1, 1]})
    ks = np.arange(1, n + 1)
    w04 = np.abs(ffd_weights(0.4, n))
    K04 = int(np.argmax(w04[1:] < tau)) + 1          # the warm-up of section 7.3: about 280 days
    s04 = np.cumsum(ffd_weights(0.4, n))

    # Panel A: |w_k| against lag, log-log; each line has slope -(d + 1)
    a.set_axisbelow(True)
    a.set_xscale("log")
    a.set_yscale("log")
    for d, col in ds:
        a.plot(ks, np.abs(ffd_weights(d, n))[1:], color=col)
    a.plot([1], [1], "o", color=INK_2, markersize=6, zorder=5, markerfacecolor="white", markeredgewidth=1.4)
    a.annotate("d = 1: one lag at weight 1,\nthen exactly zero", (1, 1), xytext=(2.0, 0.35),
               textcoords="data", fontsize=8, color=INK_2, va="center",
               arrowprops=dict(arrowstyle="-", color=MUTED, linewidth=0.7))
    a.axhline(tau, color=INK_2, linewidth=0.9, linestyle=(0, (4, 3)), zorder=1)
    a.text(1.3, tau * 1.3, "tolerance \u03c4 = 10\u207b\u2074", fontsize=8, color=INK_2, va="bottom")
    a.plot([K04, K04], [1e-6, w04[K04]], color=NEUTRAL, linewidth=0.9, linestyle=(0, (3, 3)), zorder=1)
    a.plot([K04], [w04[K04]], "o", color=ORANGE, markersize=6, zorder=6)
    a.text(K04 * 1.08, 1.6e-6, f"lag {K04}", fontsize=8, color=INK_2, va="bottom", ha="left")
    for d, col in ds:
        label_end(a, n, np.abs(ffd_weights(d, n))[n], f"d = {d:g}", col, dx=5)
    note(a, "d = 0.4 meets \u03c4 at lag 282:\nthe 280-day warm-up", loc="lower left")
    a.set_xlim(1, 5000)
    a.set_ylim(1e-6, 2)
    a.set_xticks([1, 10, 100, 1000])
    a.set_xticklabels(["1", "10", "100", "1,000"])
    a.set_yticks([10.0 ** e for e in range(-6, 1)])
    a.yaxis.set_major_formatter(FuncFormatter(pow10_label))
    a.minorticks_off()
    a.set_xlabel("Lag k (trading days)")
    a.set_ylabel("Weight size |w_k|")
    a.set_title("Weights fade like a power of age", fontsize=9.5)

    # Panel B: share of the level still inside the feature, S_K = sum_{k<=K} w_k = (-1)^K C(d-1, K)
    b.set_axisbelow(True)
    b.set_xscale("log")
    for d, col in ds:
        s = np.cumsum(ffd_weights(d, n))
        b.plot(np.arange(1, n + 1), s[1:], color=col)
    b.plot([1, n], [0, 0], color=INK_2, linewidth=LW, zorder=3)
    b.plot([K04], [s04[K04]], "o", color=ORANGE, markersize=6, zorder=6)
    b.annotate(f"d = 0.4 at lag {K04}:\n{100 * s04[K04]:.0f}% of the level left", (K04, s04[K04]),
               xytext=(110, 0.58), textcoords="data", fontsize=8, color=INK_2, ha="center", va="center",
               arrowprops=dict(arrowstyle="-", color=MUTED, linewidth=0.7))
    for d, col in ds:
        s = np.cumsum(ffd_weights(d, n))
        label_end(b, n, s[n], f"d = {d:g}", col, dx=5, dy={0.2: 0, 0.4: 9, 0.6: 3}[d])
    b.text(1.4, 0.03, "d = 1: none left", fontsize=8, color=INK_2, va="bottom", ha="left")
    b.set_xlim(1, 5000)
    b.set_ylim(-0.04, 0.85)
    b.set_xticks([1, 10, 100, 1000])
    b.set_xticklabels(["1", "10", "100", "1,000"])
    b.minorticks_off()
    b.set_xlabel("Window length K (trading days)")
    b.set_ylabel("Share of the level kept")
    b.set_title("Memory left after K lags", fontsize=9.5)
    b.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{100 * v:.0f}%"))
    print("ffd: d=0.4 crosses tau at lag", K04, "sum there", round(s04[K04], 4),
          "| d=0.5 sum to 4 lags", round(np.cumsum(ffd_weights(0.5, 4))[4], 3),
          "to 200 lags", round(np.cumsum(ffd_weights(0.5, 200))[200], 4))
    return finish(fig, "ch07_ffd_weights")


# --------------------------------------------------------------------------------------------
# 2. Hat count (section 7.6): 212,000 bond-months -> about 24,000 hats -> 79 regime windows
# --------------------------------------------------------------------------------------------
def fig_hat_count():
    rows = 212_000
    bonds_per_parent = 3          # section 7.6: "about three bonds each"
    months_per_window = 3         # a 13-week label overlaps three monthly formation dates
    parent_months = rows / bonds_per_parent
    hats = parent_months / months_per_window
    regime = 79                   # section 7.6: non-overlapping 13-week windows in twenty years
    vals = [rows, parent_months, hats, regime]
    labels = ["Bond-months\n(what the slide counted)",
              "Parent-months\n(siblings collapsed)",
              "Hats, N_eff\n(overlapping windows collapsed)",
              "Regime windows\n(non-overlapping 13 weeks, 20 yrs)"]
    colors = [C_NAIVE, C_FIX, C_FIX, C_FIX]
    texts = [f"{rows:,.0f}", f"about {round(parent_months, -2):,.0f}", f"about {round(hats, -3):,.0f}", f"{regime}"]

    fig, ax = new_figure("wide")
    ypos = np.arange(len(vals))[::-1]
    ax.set_axisbelow(True)
    ax.set_xscale("log")
    ax.barh(ypos, vals, left=1, height=0.58, color=colors, edgecolor="white")
    ax.set_xlim(1, 3e6)
    ax.set_yticks(ypos)
    ax.set_yticklabels(labels, fontsize=8.5)
    for yy, v, t in zip(ypos, vals, texts):
        ax.annotate(t, (v, yy), xytext=(5, 0), textcoords="offset points", va="center", fontsize=9, color=INK)
    steps = [("÷ 3 bonds per parent: siblings share one balance sheet", rows, parent_months),
             ("÷ 3 monthly dates per 13-week label: neighbors share the window", parent_months, hats),
             ("÷ about 300: every issuer lives through the same 79 windows", hats, regime)]
    for i, (txt, hi, lo) in enumerate(steps):
        ymid = (ypos[i] + ypos[i + 1]) / 2
        ax.annotate(txt, (hi, ymid), xytext=(0, 0), textcoords="offset points", ha="right", va="center",
                    fontsize=8, color=INK_2)
    ax.set_xlabel("Count (log scale)")
    ax.xaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{v:,.0f}"))
    ax.grid(False)
    ax.grid(True, axis="x")
    ax.tick_params(axis="y", length=0)
    ax.spines["left"].set_visible(False)
    print("hat count:", [round(v) for v in vals], "ratio rows/hats", round(rows / hats, 1), "hats/regime", round(hats / regime))
    return finish(fig, "ch07_hat_count")


# --------------------------------------------------------------------------------------------
# 3. Purged, embargoed, parent-grouped split (section 7.7)
# --------------------------------------------------------------------------------------------
def fig_purged_folds():
    K, M = 4, 5                       # parent groups, time blocks
    test_row, test_col = 1, 2         # zero-based: group 2, block 3
    H = 13                            # label horizon, weeks
    ETA = 56                          # embargo = FFD window of 280 trading days = 56 weeks
    L = 26                            # test block length in the zoom panel (shortened), weeks

    fig, (a, b) = new_figure("wide", ncols=2, gridspec_kw={"width_ratios": [1, 1.12]})

    # ---- Left: the grid of parent groups by time blocks
    gap = 0.07
    pur, emb = 0.10, 0.30            # strip widths in block units (exaggerated: true purge is 13 weeks of a 4-year block)
    for r in range(K):
        for c in range(M):
            x0, y0 = c + gap, (K - 1 - r) + gap
            w, h = 1 - 2 * gap, 1 - 2 * gap
            if r == test_row and c == test_col:
                a.add_patch(Rectangle((x0, y0), w, h, facecolor=C_NAIVE))
                a.text(c + 0.5, K - 1 - r + 0.5, "test", ha="center", va="center", fontsize=8.5, color="white", fontweight="bold")
            elif r == test_row or c == test_col:
                a.add_patch(Rectangle((x0, y0), w, h, facecolor=GRID))
            else:
                a.add_patch(Rectangle((x0, y0), w, h, facecolor=C_FIX))
                if c == test_col - 1:      # purge strip at the right edge of the block before the test block
                    a.add_patch(Rectangle((c + 1 - gap - pur, y0), pur, h, facecolor="white", edgecolor=INK_2,
                                          hatch=HATCH_PURGE, linewidth=0.5))
                if c == test_col + 1:      # purge, then embargo, at the left edge of the block after it
                    a.add_patch(Rectangle((x0, y0), pur, h, facecolor="white", edgecolor=INK_2,
                                          hatch=HATCH_PURGE, linewidth=0.5))
                    a.add_patch(Rectangle((x0 + pur, y0), emb, h, facecolor="white", edgecolor=INK_2,
                                          hatch=HATCH_EMBARGO, linewidth=0.5))
    a.set_xlim(0, M)
    a.set_ylim(0, K)
    a.set_xticks(np.arange(M) + 0.5)
    a.set_xticklabels(["2004–08", "2008–12", "2012–16", "2016–20", "2020–24"], fontsize=8)
    a.set_yticks(np.arange(K) + 0.5)
    a.set_yticklabels([f"Group {K - i}" for i in range(K)], fontsize=8.5)
    a.set_xlabel("Time block (4 years each)")
    a.set_ylabel("Ultimate-parent group")
    a.grid(False)
    a.spines["left"].set_visible(False)
    a.spines["bottom"].set_visible(False)
    a.tick_params(length=0)
    a.set_title("Which cells train", fontsize=9.5)

    # ---- Right: one training parent's labels at the edges of the test block (weeks from block start)
    T0, T1 = 0, L + H
    fs = np.arange(-40, 120, 5)
    ypos = np.arange(len(fs))
    b.axvspan(T0, L, color=C_NAIVE, alpha=0.14, linewidth=0, zorder=0)
    counts = dict(train=0, aside=0, purge=0, embargo=0)
    for y, f in zip(ypos, fs):
        t0, t1 = f, f + H
        if T0 <= f <= L:
            kind = "aside"
        elif t0 <= T1 and t1 >= T0:
            kind = "purge"
        elif T1 < t0 <= T1 + ETA:
            kind = "embargo"
        else:
            kind = "train"
        counts[kind] += 1
        if kind == "train":
            b.barh(y, H, left=t0, height=0.62, color=C_FIX)
        elif kind == "aside":
            b.barh(y, H, left=t0, height=0.62, color=GRID)
        else:
            b.barh(y, H, left=t0, height=0.62, facecolor="white", edgecolor=INK_2, linewidth=0.5,
                   hatch=HATCH_PURGE if kind == "purge" else HATCH_EMBARGO)
    for x in (T0, T1, T1 + ETA):
        b.axvline(x, color=INK_2, linewidth=0.9, linestyle=(0, (3, 3)), zorder=1)
    ytop = -1.2
    b.text(T0 - 1, ytop, "T0", fontsize=8, color=INK_2, ha="right", va="center")
    b.text(T1 + 1, ytop, "T1", fontsize=8, color=INK_2, ha="left", va="center")
    b.text(T1 + ETA + 1, ytop, "T1 + η", fontsize=8, color=INK_2, ha="left", va="center")
    b.text(L / 2, 25.5, "test block:\nset aside", fontsize=8, color=INK_2, ha="center", va="center")
    b.annotate("", xy=(T1, len(fs) - 0.2), xytext=(T1 + ETA, len(fs) - 0.2),
               arrowprops=dict(arrowstyle="<->", color=INK_2, linewidth=0.9, shrinkA=0, shrinkB=0))
    b.text(T1 + ETA / 2, len(fs) + 0.9, "embargo η: the FFD window,\nabout 280 days at τ = 10⁻⁴", fontsize=8, color=INK_2,
           ha="center", va="top", zorder=6,
           bbox=dict(facecolor="white", edgecolor="none", pad=1.5))
    b.set_ylim(len(fs) + 7.6, -2.2)
    b.set_xlim(-46, 136)
    b.set_yticks([])
    b.set_xticks([-40, 0, 40, 80, 120])
    b.set_xlabel("Weeks from test-block start (block shortened)")
    b.grid(False)
    b.spines["left"].set_visible(False)
    b.set_title("One training parent's 13-week labels", fontsize=9.5)

    handles = [Patch(facecolor=C_NAIVE, label="test cell"),
               Patch(facecolor=C_FIX, label="training"),
               Patch(facecolor=GRID, label="set aside (shares the test row or column)"),
               Patch(facecolor="white", edgecolor=INK_2, hatch=HATCH_PURGE, linewidth=0.5, label="purged"),
               Patch(facecolor="white", edgecolor=INK_2, hatch=HATCH_EMBARGO, linewidth=0.5, label="embargoed")]
    fig.legend(handles=handles, loc="outside lower center", ncol=5, fontsize=8, handlelength=1.3,
               handleheight=1.0, columnspacing=1.2, handletextpad=0.5)
    print("purged folds, labels on the zoom:", counts)
    return finish(fig, "ch07_purged_folds")


# --------------------------------------------------------------------------------------------
# 4. Expected best Sharpe of N pure-noise strategies (section 7.8)
# --------------------------------------------------------------------------------------------
def sr_star(N, T=240):
    """SR* = sqrt(V) [(1 - g) Phi^-1(1 - 1/N) + g Phi^-1(1 - 1/(N e))], V = 1/T, per month."""
    g = 0.5772156649015329
    N = np.asarray(N, dtype=float)
    return np.sqrt(1.0 / T) * ((1 - g) * norm.ppf(1 - 1 / N) + g * norm.ppf(1 - 1 / (N * np.e)))


def fig_dsr_noise_max():
    T = 240
    ann = np.sqrt(12)
    Ns = np.logspace(np.log10(2), 5, 300)
    curve = sr_star(Ns, T) * ann
    rng = np.random.default_rng(7)
    sim_N = [2, 10, 100, 1_000, 10_000, 100_000]
    sim = []
    for n in sim_N:
        reps = 300 if n >= 100_000 else 2_000
        m = [rng.standard_normal(n).max() for _ in range(reps)]
        sim.append(np.mean(m) * np.sqrt(1.0 / T) * ann)

    fig, ax = new_figure("wide")
    ax.set_xscale("log")
    ax.fill_between(Ns, 0, curve, color=SEQ_BLUE_STEPS[0], linewidth=0, zorder=1)
    ax.plot(Ns, curve, color=C_FIX, zorder=3)
    ax.plot(sim_N, sim, "o", color=INK_2, markersize=5, markerfacecolor="white", markeredgewidth=1.2, zorder=4)
    ax.set_axisbelow(True)
    ax.text(4.0, 0.04, "what pure noise delivers\nbefore the model has done anything", fontsize=8.5, color=INK_2,
            ha="left", va="bottom")

    for n, txt, xt, yt, ha in [(400, "N = 400 effectively distinct trials", 360, 0.27, "right"),
                               (3000, "N = 3,000 trials", 3300, 0.50, "left")]:
        v = float(sr_star(n, T)) * ann
        ax.plot([n, n], [0, v], color=NEUTRAL, linewidth=0.9, linestyle=(0, (3, 3)), zorder=2)
        ax.plot([n], [v], "o", color=C_FIX, markersize=7, zorder=5)
        ax.text(xt, yt, f"{txt}\n{float(sr_star(n, T)):.2f} a month, {v:.2f} annualized", ha=ha, va="center",
                fontsize=8, color=INK_2)
    oos = 0.30 * ann
    ax.axhline(oos, color=C_NAIVE, linewidth=LW, zorder=3)
    ax.annotate("Kaz's purged out-of-sample Sharpe: 0.30 a month, %.2f annualized" % oos, (2.2, oos),
                xytext=(0, 5), textcoords="offset points", fontsize=8.5, color=INK_2, ha="left", va="bottom")
    ax.plot([2.2], [oos], "o", color=C_NAIVE, markersize=4, zorder=5, clip_on=False)
    ax.set_xlim(2, 1.6e5)
    ax.set_ylim(0, 1.3)
    ax.set_xticks([10, 100, 1000, 10000, 100000])
    ax.xaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{v:,.0f}"))
    ax.set_xlabel("Number of trials N (log scale)")
    ax.set_ylabel("Expected best Sharpe of pure noise\n(annualized)")
    ax.text(0.99, 0.98, "T = 240 months; every trial has true Sharpe 0.\nOpen dots: simulated mean of the maximum.",
            transform=ax.transAxes, ha="right", va="top", fontsize=8, color=MUTED)
    print("dsr: SR*(3000) %.3f/month %.3f annualized; SR*(400) %.3f; sim dots %s | formula at sim_N %s" % (
        sr_star(3000, T), sr_star(3000, T) * ann, sr_star(400, T), [round(s, 3) for s in sim],
        [round(float(sr_star(n, T)) * ann, 3) for n in sim_N]))
    return finish(fig, "ch07_dsr_noise_max")


# --------------------------------------------------------------------------------------------
# 5. Short-term reversal: textbook vs gap constructions (section 7.9). REAL data, from the dossier.
# --------------------------------------------------------------------------------------------
def fig_reversal_gap():
    # Dickerson, Robotti, Rossetti (2026), Table 1, value-weighted decile, monthly %, 2002-2024
    # (state/research/papers_factor_replication_crisis_and_bond_data.md section 3.2).
    prem = [-0.99, -0.09, -0.17]
    tstat = [-4.46, -0.51, None]
    names = ["Textbook:\nmonth-end price\nin both", "Signal gap:\nsignal 1\u201310 days\nbefore month-end",
             "Return gap:\nreturn starts at\nmonth-begin"]
    cols = [C_NAIVE, C_FIX, C_FIX]

    fig, (a, b) = new_figure("wide", ncols=2, gridspec_kw={"width_ratios": [1.35, 1]})
    x = np.arange(3)
    a.bar(x, prem, width=0.6, color=cols, edgecolor="white")
    a.axhline(0, color=INK_2, linewidth=0.9, zorder=3)
    for xi, p, t in zip(x, prem, tstat):
        txt = f"{p:.2f}%".replace("-", MINUS)
        if t is not None:
            txt += f"\nt = {t:.2f}".replace("-", MINUS)
        a.annotate(txt, (xi, p), xytext=(0, -4), textcoords="offset points", ha="center", va="top", fontsize=8.5, color=INK_2)
    a.set_xticks(x)
    a.set_xticklabels(names, fontsize=8)
    a.set_ylim(-1.45, 0.12)
    a.set_xlim(-0.55, 2.55)
    a.set_ylabel("Winners minus losers\n(% a month)")
    a.set_title("Premium by construction", fontsize=9.5)
    a.grid(True, axis="y")
    a.set_axisbelow(True)
    b.set_axisbelow(True)
    a.tick_params(axis="x", length=0)
    a.spines["bottom"].set_visible(False)

    # Right: what $1 became, August 2002 to December 2024
    b.bar([0], [12.0], width=0.55, color=C_NAIVE, edgecolor="white")
    b.bar([1], [0.30], bottom=1.10, width=0.55, color=C_FIX, edgecolor="white")
    b.axhline(1.0, color=INK_2, linewidth=0.9, linestyle=(0, (4, 3)), zorder=1)
    b.annotate("about $12", (0, 12.0), xytext=(0, 4), textcoords="offset points", ha="center", va="bottom", fontsize=8.5, color=INK_2)
    b.annotate("$1.10 to $1.40", (1, 1.40), xytext=(0, 4), textcoords="offset points", ha="center", va="bottom", fontsize=8.5, color=INK_2)
    b.annotate("the starting $1", (1.45, 1.0), xytext=(0, -4), textcoords="offset points", ha="right", va="top", fontsize=8, color=INK_2)
    b.set_xticks([0, 1])
    b.set_xticklabels(["Textbook:\nmonth-end price\nin both", "Adjusted:\neither gap"], fontsize=8)
    b.set_xlim(-0.55, 1.55)
    b.set_ylim(0, 14)
    b.set_ylabel("Value of $1, Aug 2002 to Dec 2024")
    b.set_title("What a dollar became", fontsize=9.5)
    b.tick_params(axis="x", length=0)
    return finish(fig, "ch07_reversal_gap")


if __name__ == "__main__":
    fig_ffd_weights()
    fig_hat_count()
    fig_purged_folds()
    fig_dsr_noise_max()
    fig_reversal_gap()
