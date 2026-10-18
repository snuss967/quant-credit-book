"""Chapter 7-B figures: The Statistician's Toolbox for Credit Panels.

Run:  python3 tools/figures/ch07b.py      (writes assets/figures/ch07b_*.png)

Nothing here is market data. Every figure is computed from a model the chapter states, so each
caption says "Illustrative":
  1. ch07b_moulton_breadth        eq. 7B.3 and the effective-breadth form (section 7-B.1)
  2. ch07b_newey_west_shortfall   eq. 7B.4 Bartlett weights against the overlap triangle (7-B.2)
  3. ch07b_km_practice_cohort     the six-issuer practice cohort, Kaplan-Meier + Greenwood (7-B.4)
  4. ch07b_mp_edge                simulated noise + planted factors, Marchenko-Pastur edge (7-B.5)
  5. ch07b_first_passage_bridge   one-year barrier hit probability, grid vs Brownian bridge (7-B.8)

Color roles are fixed across the chapter:
  ORANGE = the textbook / naive answer (classical SE, L = h-1, grid-only monitoring, censored-as-survivors)
  BLUE   = the corrected / honest answer (clustered, L = 2h-1, bridge, Kaplan-Meier, real components)
  INK_2 / NEUTRAL = the truth or a reference level (dashed)
  Magnitude (sibling correlation) = SEQ_BLUE shades
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from style import *  # noqa: E402,F401,F403
import numpy as np  # noqa: E402
from matplotlib.ticker import FuncFormatter  # noqa: E402
from scipy.stats import norm  # noqa: E402

MINUS = "−"
C_NAIVE, C_FIX = ORANGE, BLUE


# --------------------------------------------------------------------------------------------
# Figure 7-B.1  The Moulton factor and effective breadth (section 7-B.1)
# --------------------------------------------------------------------------------------------
def fig_moulton_breadth():
    fig, (a, b) = new_figure("panel2", ncols=2)
    m = np.linspace(1, 20, 191)
    rhos = [(0.2, SEQ_BLUE_STEPS[4]), (0.4, SEQ_BLUE_STEPS[7]), (0.6, SEQ_BLUE_STEPS[11])]
    for rho, col in rhos:
        a.plot(m, np.sqrt(1 + (m - 1) * rho), color=col, linewidth=2.0)
        b.plot(m, m / (1 + (m - 1) * rho), color=col, linewidth=2.0)
        b.hlines(1 / rho, 1, 20, color=col, linewidth=0.9, linestyle=(0, (3, 3)), zorder=1)
    # direct labels at the right end of each curve
    for rho, col in rhos:
        label_end(a, 20, np.sqrt(1 + 19 * rho), f"ρ = {rho:.1f}", col, dx=5)
        label_end(b, 20, 20 / (1 + 19 * rho), f"ρ = {rho:.1f}", col, dx=5)
    # Halvorsen: eleven bonds, sibling correlation 0.6
    mh, rh = 11, 0.6
    fa, fb = np.sqrt(1 + (mh - 1) * rh), mh / (1 + (mh - 1) * rh)
    for ax, val, txt, off, ha, va in [(a, fa, f"Halvorsen: ×{fa:.2f}", (-9, 7), "right", "bottom"),
                                      (b, fb, f"Halvorsen: {fb:.2f} bonds", (0, -22), "center", "top")]:
        ax.plot([mh], [val], "o", color=INK, markersize=6.5, zorder=7, markerfacecolor="white", markeredgewidth=1.6)
        ax.annotate(txt, (mh, val), xytext=off, textcoords="offset points", ha=ha, va=va,
                    fontsize=8.5, color=INK_2)
    a.set_xlim(1, 20)
    b.set_xlim(1, 20)
    a.set_ylim(0.8, 4.0)
    b.set_ylim(0, 5.4)
    a.set_xticks([1, 5, 10, 15, 20])
    b.set_xticks([1, 5, 10, 15, 20])
    for ax in (a, b):
        ax.set_xlabel("Bonds per issuer, m")
        ax.grid(axis="x", visible=False)
    a.set_ylabel("Standard error vs classical (×)")
    b.set_ylabel("Effective independent bonds per issuer")
    a.set_title("Error bars inflate", fontsize=9.5)
    b.set_title("Rows add less than they appear to", fontsize=9.5)
    for rho, _ in rhos:
        b.text(19.4, 1 / rho + 0.06, f"ceiling 1/ρ = {1 / rho:.1f}", ha="right", va="bottom", fontsize=8,
               color=MUTED)
    # make room on the right for the end labels
    for ax in (a, b):
        ax.margins(x=0)
    return finish(fig, "ch07b_moulton_breadth")


# --------------------------------------------------------------------------------------------
# Figure 7-B.2  The Newey-West shortfall (section 7-B.2)
# --------------------------------------------------------------------------------------------
def nw_multiplier(L, h=12):
    k = np.arange(1, L + 1)
    return 1 + 2 * np.sum((1 - k / (L + 1)) * np.clip(1 - k / h, 0, None))


def fig_newey_west():
    h = 12
    fig, (a, b) = new_figure("panel2", ncols=2)
    k = np.arange(0, 26)
    tri = np.clip(1 - k / h, 0, None)
    a.fill_between(k, 0, tri, color=GRID, step=None, zorder=1)
    a.plot(k, tri, color=INK_2, linewidth=LW, zorder=3)
    for L, col in [(11, C_NAIVE), (23, C_FIX)]:
        w = np.where(k <= L, 1 - k / (L + 1), 0.0)
        a.plot(k, w * tri, color=col, linewidth=2.0, zorder=4)
    a.annotate("true overlap correlation 1 − k/12", (1.0, 11 / 12), xytext=(5, 12), textcoords="offset points",
               ha="left", va="bottom", fontsize=8.5, color=INK_2)
    kk = {23: 4.0, 11: 5.0}
    y23 = (1 - 4 / 24) * (1 - 4 / 12)
    y11 = (1 - 5 / 12) ** 2
    a.plot([4.0], [y23], "o", color=C_FIX, markersize=4.5, zorder=6)
    a.plot([5.0], [y11], "o", color=C_NAIVE, markersize=4.5, zorder=6)
    arrow = dict(arrowstyle="-", color=MUTED, linewidth=0.8, shrinkA=0, shrinkB=3)
    a.annotate("L = 23 (desk rule)", (4.0, y23), xytext=(8.5, 0.80), textcoords="data", ha="left", va="center",
               fontsize=8.5, color=INK_2, arrowprops=arrow)
    a.annotate("L = 11 (textbook)", (5.0, y11), xytext=(8.5, 0.62), textcoords="data", ha="left", va="center",
               fontsize=8.5, color=INK_2, arrowprops=arrow)
    a.set_xlim(0, 25)
    a.set_ylim(0, 1.1)
    a.set_xlabel("Lag k (months)")
    a.set_ylabel("Weight on the lag-k autocovariance")
    a.set_title("What Newey–West counts of the overlap", fontsize=9.5)
    a.grid(axis="x", visible=False)

    Ls = np.arange(0, 48)
    mult = np.array([nw_multiplier(L, h) for L in Ls])
    b.axhline(h, color=INK_2, linewidth=1.0, linestyle=(0, (3, 3)), zorder=1)
    b.axhline(1, color=NEUTRAL, linewidth=0.9, zorder=1)
    b.plot(Ls, mult, color=NEUTRAL, linewidth=LW, zorder=2)
    for L, col in [(11, C_NAIVE), (23, C_FIX)]:
        v = nw_multiplier(L, h)
        b.plot([L], [v], "o", color=col, markersize=7, zorder=6)
    v11, v23 = nw_multiplier(11, h), nw_multiplier(23, h)
    b.annotate(f"L = 11: {v11:.1f}\nt still {100 * (np.sqrt(h / v11) - 1):.0f}% too large", (11, v11), xytext=(9, -9),
               textcoords="offset points", ha="left", va="top", fontsize=8.5, color=INK_2)
    b.annotate(f"L = 23: {v23:.1f}", (23, v23), xytext=(8, -9), textcoords="offset points",
               ha="left", va="top", fontsize=8.5, color=INK_2)
    b.text(47, h + 0.35, "truth: 12 (= h)", ha="right", va="bottom", fontsize=8.5, color=INK_2)
    b.text(47, 1 + 0.35, "naive: 1", ha="right", va="bottom", fontsize=8.5, color=MUTED)
    b.set_xlim(0, 47)
    b.set_ylim(0, 14)
    b.set_xlabel("Newey–West lags, L")
    b.set_ylabel("Variance multiplier recovered")
    b.set_title("Under-correction, by lag choice", fontsize=9.5)
    b.grid(axis="x", visible=False)
    return finish(fig, "ch07b_newey_west_shortfall")


# --------------------------------------------------------------------------------------------
# Figure 7-B.3  The practice cohort through Kaplan-Meier (section 7-B.4)
# --------------------------------------------------------------------------------------------
COHORT = [  # (issuer, exit month, event?, what happened)
    ("Calloway", 9, False, "make-whole call"),
    ("Quillfeather", 14, True, "distressed exchange"),
    ("Larkspur Foam", 22, True, "distressed exchange"),
    ("Halvorsen", 27, True, "default"),
    ("Halyard", 30, False, "acquired"),
    ("Brambleworth", 36, False, "window closes"),
]


def kaplan_meier(cohort):
    """Product-limit estimate with Greenwood variance, exactly as in equations 7B.5-7B.6."""
    times = sorted({t for _, t, e, _ in cohort if e})
    out = [(0.0, 1.0, 0.0, 0.0)]  # time, S, greenwood sum, nelson-aalen H
    s, gsum, hsum = 1.0, 0.0, 0.0
    for t in times:
        n = sum(1 for _, ti, _, _ in cohort if ti >= t)
        d = sum(1 for _, ti, e, _ in cohort if ti == t and e)
        s *= 1 - d / n
        gsum += d / (n * (n - d)) if n > d else np.inf
        hsum += d / n
        out.append((float(t), s, gsum, hsum))
    return out


def fig_km_cohort():
    km = kaplan_meier(COHORT)
    fig, (a, b) = new_figure((7.0, 3.75), ncols=2)
    # left: swimlanes
    n = len(COHORT)
    for i, (name, t, ev, why) in enumerate(COHORT):
        y = n - 1 - i
        a.hlines(y, 0, t, color=NEUTRAL, linewidth=2.2, zorder=2)
        if ev:
            a.plot([t], [y], "o", color=RED, markersize=8, zorder=5)
        else:
            a.plot([t], [y], "o", markerfacecolor="white", markeredgecolor=BLUE, markeredgewidth=1.8, markersize=8,
                   zorder=5)
        a.annotate(f"{why}, month {t}", (t, y), xytext=(8, 0), textcoords="offset points", va="center",
                   fontsize=8, color=INK_2)
    a.set_yticks(range(n))
    a.set_yticklabels([c[0] for c in COHORT][::-1])
    a.set_xlim(0, 52)
    a.set_ylim(-0.6, n - 0.4)
    a.set_xticks([0, 12, 24, 36])
    a.set_xlabel("Months in the window")
    a.grid(axis="y", visible=False)
    a.tick_params(axis="y", length=0)
    a.spines["left"].set_visible(False)
    a.plot([], [], "o", color=RED, markersize=7, label="event (default or exchange)")
    a.plot([], [], "o", markerfacecolor="white", markeredgecolor=BLUE, markeredgewidth=1.8, markersize=7,
           label="censored (left for another reason)")
    a.legend(loc="upper center", bbox_to_anchor=(0.45, -0.17), fontsize=8, ncol=1, handletextpad=0.3)

    # right: the Kaplan-Meier curve with a Greenwood log-log band
    xs, ss, lo, hi = [], [], [], []
    for (t, s, g, _) in km:
        xs.append(t)
        ss.append(s)
        if s >= 1.0 or s <= 0.0:
            lo.append(s)
            hi.append(s)
        else:
            se_cll = np.sqrt(g) / abs(np.log(s))
            lo.append(s ** np.exp(1.96 * se_cll))
            hi.append(s ** np.exp(-1.96 * se_cll))
    T = 36
    xs.append(T)
    ss.append(ss[-1])
    lo.append(lo[-1])
    hi.append(hi[-1])
    b.fill_between(xs, lo, hi, step="post", color=BLUE, alpha=0.16, zorder=1)
    b.step(xs, ss, where="post", color=C_FIX, linewidth=2.2, zorder=4)
    for name, t, ev, _ in COHORT:
        if not ev and t < 36:
            s_here = [s for (tt, s, _, _) in km if tt <= t][-1]
            b.plot([t], [s_here], "|", color=C_FIX, markersize=11, markeredgewidth=1.8, zorder=6)
    s_end = km[-1][1]
    na_end = float(np.exp(-km[-1][3]))
    b.axhline(0.5, color=C_NAIVE, linewidth=1.2, linestyle=(0, (4, 3)), zorder=2)
    b.axhline(0.25, color=C_NAIVE, linewidth=1.2, linestyle=(0, (4, 3)), zorder=2)
    b.text(0.8, 0.5 + 0.015, "censored as survivors: 0.50", fontsize=8, color=INK_2, ha="left", va="bottom")
    b.text(0.8, 0.25 - 0.015, "censored dropped: 0.25", fontsize=8, color=INK_2, ha="left", va="top")
    b.plot([T], [s_end], "o", color=C_FIX, markersize=6, zorder=7, clip_on=False)
    b.plot([T], [na_end], "D", color=VIOLET, markersize=5.5, zorder=7, clip_on=False)
    from matplotlib.lines import Line2D
    from matplotlib.patches import Patch
    handles = [
        Line2D([], [], color=C_FIX, linewidth=2.2, marker="|", markersize=10, markeredgewidth=1.8,
               label=f"Kaplan–Meier, S(36) = {s_end:.2f} (ticks: censoring)"),
        Patch(facecolor=BLUE, alpha=0.16, label=f"95% Greenwood band at 36: {lo[-1]:.2f}–{hi[-1]:.2f}"),
        Line2D([], [], color=VIOLET, marker="D", linestyle="", markersize=5.5, label=f"Nelson–Aalen: {na_end:.2f}"),
    ]
    b.legend(handles=handles, loc="upper center", bbox_to_anchor=(0.5, -0.17), fontsize=8, ncol=1, handletextpad=0.5)
    b.set_xlim(0, T)
    b.set_ylim(0, 1.04)
    b.set_xticks([0, 12, 24, 36])
    b.set_xlabel("Months in the window")
    b.set_ylabel("Survival probability  S(t)")
    b.grid(axis="x", visible=False)
    return finish(fig, "ch07b_km_practice_cohort")


# --------------------------------------------------------------------------------------------
# Figure 7-B.4  Marchenko-Pastur: which components are real (section 7-B.5)
# --------------------------------------------------------------------------------------------
def mp_density(lam, q):
    lo, hi = (1 - np.sqrt(q)) ** 2, (1 + np.sqrt(q)) ** 2
    out = np.zeros_like(lam)
    ok = (lam > lo) & (lam < hi)
    out[ok] = np.sqrt((hi - lam[ok]) * (lam[ok] - lo)) / (2 * np.pi * q * lam[ok])
    return out


def simulate_panel(rng, N, T, a=0.04, c=0.017, sector=100):
    """Unit-variance returns: a market-wide factor (variance share a) and a sector factor on `sector` bonds."""
    f1 = rng.standard_normal((T, 1))
    f2 = rng.standard_normal((T, 1))
    load2 = np.zeros(N)
    load2[:sector] = np.sqrt(c)
    e_var = 1 - a - load2 ** 2
    return np.sqrt(a) * f1 + f2 * load2 + rng.standard_normal((T, N)) * np.sqrt(e_var)


def eigvals_corr(X):
    T, N = X.shape
    if T < N:
        ev = np.linalg.eigvalsh(X @ X.T / T)
    else:
        ev = np.linalg.eigvalsh(X.T @ X / T)
    return np.sort(ev)[::-1]


def fig_mp_edge():
    N = 400
    rng = np.random.default_rng(np.random.SeedSequence(7041).spawn(1)[0])
    fig, axes = new_figure("panel2", ncols=2)
    cases = [("Five years of daily data", 1260), ("Ten years of monthly data", 120)]
    edge_marks = {}
    for ax, (ttl, T) in zip(axes, cases):
        q = N / T
        X = simulate_panel(rng, N, T)
        ev = eigvals_corr(X)
        edge = (1 + np.sqrt(q)) ** 2
        edge_marks[T] = edge
        bulk = ev[ev <= edge * 1.02]
        out = ev[ev > edge * 1.02]
        bw = 0.25
        bins = np.arange(0, 8.5 + bw, bw)
        ax.hist(bulk, bins=bins, color=NEUTRAL, edgecolor="white", linewidth=0.8, zorder=2)
        lam = np.linspace(0.01, edge, 400)
        ax.plot(lam, N * mp_density(lam, q) * bw, color=INK_2, linewidth=1.3, zorder=4)
        ax.axvline(edge, color=C_NAIVE, linewidth=1.3, linestyle=(0, (4, 3)), zorder=3)
        ymax = ax.get_ylim()[1]
        ax.annotate(f"edge {edge:.1f}", (edge, ymax * 0.97), xytext=(5, 0), textcoords="offset points",
                    ha="left", va="top", fontsize=8.5, color=INK_2)
        # eigenvalues above the edge: stems with dots, so a single eigenvalue is visible
        for j, v in enumerate(out):
            ax.vlines(v, 0, ymax * 0.20, color=C_FIX, linewidth=1.6, zorder=5)
            ax.plot([v], [ymax * 0.20], "o", color=C_FIX, markersize=6, zorder=6)
            name = "market factor" if v > 10 else "sector factor"
            left = v < 10
            ax.annotate(f"{v:.1f}\n{name}", (v, ymax * 0.20), xytext=(4 if left else 0, 6),
                        textcoords="offset points", ha="left" if left else "center", va="bottom",
                        fontsize=8.5, color=INK_2)
        ax.set_xlim(0, 24)
        ax.set_ylim(0, ymax)
        ax.set_xlabel("Eigenvalue of the correlation matrix")
        ax.set_title(f"{ttl}: q = {q:.2f}", fontsize=9.5)
        ax.grid(axis="x", visible=False)
        print(f"  T={T}: edge {edge:.2f}, eigenvalues above edge: {np.round(out, 2)}, "
              f"largest in bulk {bulk.max():.2f}")
    axes[0].set_ylabel("Number of eigenvalues")
    axes[0].text(0.985, 0.80, "line: Marchenko–Pastur\nbars: simulated eigenvalues", transform=axes[0].transAxes,
                 ha="right", va="top", fontsize=8, color=MUTED)
    axes[1].text(0.985, 0.50, "the planted sector factor\nis lost somewhere in the bulk", transform=axes[1].transAxes,
                 ha="right", va="top", fontsize=8, color=MUTED)
    return finish(fig, "ch07b_mp_edge")


# --------------------------------------------------------------------------------------------
# Figure 7-B.5  First passage on a grid, with and without the Brownian bridge (section 7-B.8)
# --------------------------------------------------------------------------------------------
def first_passage_mc(rng, n_steps, n_paths, dist=0.30, sigma=0.25, T=1.0, chunk=20000):
    dt = T / n_steps
    hit_grid, hit_bridge = 0.0, 0.0
    done = 0
    while done < n_paths:
        m = min(chunk, n_paths - done)
        z = rng.standard_normal((m, n_steps))
        x = dist + np.cumsum(sigma * np.sqrt(dt) * z, axis=1)       # log distance above the barrier
        x = np.concatenate([np.full((m, 1), dist), x], axis=1)
        grid_hit = (x[:, 1:] <= 0).any(axis=1)
        a_, b_ = x[:, :-1], x[:, 1:]
        both_above = (a_ > 0) & (b_ > 0)
        p = np.where(both_above, np.exp(-2.0 * np.where(both_above, a_ * b_, 0.0) / (sigma ** 2 * dt)), 1.0)
        # a step that ends at or below the barrier is a certain hit (p = 1); a step that starts below
        # can only follow an earlier hit, so its factor is irrelevant once the survival product is 0
        surv = np.prod(1.0 - np.clip(p, 0, 1), axis=1)
        hit_grid += grid_hit.sum()
        hit_bridge += (1.0 - surv).sum()
        done += m
    return hit_grid / n_paths, hit_bridge / n_paths


def fig_first_passage():
    dist, sigma = 0.30, 0.25
    exact = 2 * norm.cdf(-dist / sigma)
    grids = [1, 2, 4, 12, 26, 52, 252]
    ss = np.random.SeedSequence(7081).spawn(len(grids))
    naive, bridge = [], []
    for g, s in zip(grids, ss):
        rng = np.random.default_rng(s)
        a_, b_ = first_passage_mc(rng, g, 200_000)
        naive.append(a_)
        bridge.append(b_)
    naive, bridge = np.array(naive), np.array(bridge)
    bgk = np.array([2 * norm.cdf(-(dist + 0.5826 * sigma * np.sqrt(1.0 / g)) / sigma) for g in grids])
    print("  exact", round(exact, 4), "naive", np.round(naive, 4), "bridge", np.round(bridge, 4),
          "bgk", np.round(bgk, 4))

    fig, ax = new_figure("wide")
    xmax = 252 * 3.4
    ax.hlines(100 * exact, 0.8, 252, color=INK_2, linewidth=1.1, linestyle=(0, (4, 3)), zorder=1)
    ax.plot(grids, 100 * naive, "-o", color=C_NAIVE, linewidth=LW, markersize=6, zorder=4)
    ax.plot(grids, 100 * bridge, "-o", color=C_FIX, linewidth=LW, markersize=6, zorder=5)
    ax.set_xscale("log")
    ax.set_xticks(grids)
    ax.set_xticklabels([str(g) for g in grids])
    ax.minorticks_off()
    ax.set_xlim(0.8, xmax)
    ax.set_ylim(0, 27)
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{v:.0f}%"))
    ax.set_xlabel("Monitoring dates in the year (1 = annual, 12 = monthly, 252 = daily)")
    ax.set_ylabel("Probability the barrier is hit in one year")
    ax.grid(axis="x", visible=False)
    ax.annotate(f"exact, continuous monitoring: {100 * exact:.1f}%", (0.9, 100 * exact), xytext=(0, 6),
                textcoords="offset points", ha="left", va="bottom", fontsize=8.5, color=INK_2)
    i12 = grids.index(12)
    gap = 100 * (exact - naive[i12])
    ax.annotate("", xy=(12, 100 * exact - 0.25), xytext=(12, 100 * naive[i12] + 0.25),
                arrowprops=dict(arrowstyle="<->", color=INK_2, linewidth=1.0, shrinkA=0, shrinkB=0))
    ax.annotate(f"monthly grid: {100 * naive[i12]:.1f}% vs {100 * exact:.1f}%\nmisses {gap:.1f} points, about a quarter\nof the defaults",
                (12, 100 * (exact + naive[i12]) / 2), xytext=(-8, 0), textcoords="offset points", ha="right",
                va="center", fontsize=8.5, color=INK_2)
    label_end(ax, 252, 100 * bridge[-1], "bridge, any grid", C_FIX, dx=6, dy=2)
    label_end(ax, 252, 100 * naive[-1], "grid only", C_NAIVE, dx=6, dy=-2)
    note(ax, "σ = 0.25, barrier 0.30 below the start in logs, zero drift; 200,000 paths per point",
         loc="lower left")
    return finish(fig, "ch07b_first_passage_bridge")


if __name__ == "__main__":
    for fn in (fig_moulton_breadth, fig_newey_west, fig_km_cohort, fig_mp_edge, fig_first_passage):
        fn()
