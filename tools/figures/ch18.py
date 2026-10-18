"""Figures for Chapter 18 (OTC credit microstructure and the market maker's equations).

Run:  python3 tools/figures/ch18.py      -> assets/figures/ch18_*.png

Figures (in order of appearance in the chapter):
  ch18_roll_splitting_momentum      s18.2  Roll's estimator under order splitting and informed drift (simulated)
  ch18_quote_ladder_glft_horizon    s18.5  AS vs GLFT quote ribbon by inventory, and the effective horizon vs A (model)
  ch18_dealer_net_inventory_nyfed   s18.5  Primary dealers' net corporate-bond positions (NY Fed, real data)
  ch18_jtd_reservation_price        s18.6  Reservation price vs inventory with jump-to-default (Altice numbers, model)
  ch18_cold_open_bid_waterfall      s18.7  The cold-open bid, term by term (eq. 18.9, model)

Real data: tools/figures/data/ch18_nyfed_pd_corp_bonds.csv (NY Fed Primary Dealer Statistics, fetched 2026-10-18).
It is rebuilt from the NY Fed API if the CSV is missing.
"""
import csv
import datetime as dt
import json
import os
import sys
import warnings

import numpy as np
from scipy import signal

sys.path.insert(0, os.path.dirname(__file__))
from style import *  # noqa: E402,F401,F403  (applies the rcParams on import)
from style import plt  # noqa: E402

import matplotlib.dates as mdates  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
DATA_CSV = os.path.join(HERE, "data", "ch18_nyfed_pd_corp_bonds.csv")


# ---------------------------------------------------------------------------------------------
# Figure 18.1: Roll's estimator, order splitting and informed drift (s18.2)
# ---------------------------------------------------------------------------------------------
def roll_spread(prices, min_obs=20):
    """Roll (1984) spread, as in Listing 18.1: NaN when the autocovariance is non-negative."""
    p = np.asarray(prices, dtype=float)
    p = p[np.isfinite(p)]
    if p.size < min_obs + 2:
        return np.nan
    dp = np.diff(p)
    c = np.cov(dp[1:], dp[:-1], ddof=1)[0, 1]
    return np.nan if c >= 0.0 else 2.0 * np.sqrt(-c)


def simulate_roll(n, spread, sigma_mid, rng, rho=0.0, phi_mid=0.0):
    """Listing 18.1's simulator: random-walk mid (AR(1) increments) plus half a spread times a Markov trade sign."""
    stay = 0.5 * (1.0 + rho)
    flips = rng.random(n) >= stay
    flips[0] = False
    sign = rng.choice([-1.0, 1.0]) * np.where(np.cumsum(flips) % 2 == 0, 1.0, -1.0)
    eps = rng.normal(0.0, sigma_mid, n)
    dm = signal.lfilter([1.0], [1.0, -phi_mid], eps)
    return 90.0 + np.cumsum(dm) + 0.5 * spread * sign


def fig_roll():
    rng = np.random.default_rng(1802)
    S, sig, n, reps = 0.20, 0.10, 200_000, 5          # spread (pts), mid-increment vol (pts), prints, replications
    rhos = np.linspace(0.0, 0.9, 10)
    phis = np.linspace(0.0, 0.9, 13)

    est_rho = np.array([[roll_spread(simulate_roll(n, S, sig, rng, rho=r)) for _ in range(reps)] for r in rhos])
    est_phi = np.array([[roll_spread(simulate_roll(n, S, sig, rng, phi_mid=f)) for _ in range(reps)] for f in phis])
    m_rho = np.nanmean(est_rho, axis=1) / S
    # Mean over replications that returned an estimate; NaN if the majority returned NaN.
    nan_share = np.isnan(est_phi).mean(axis=1)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", RuntimeWarning)          # all-NaN rows are expected beyond phi*
        m_phi = np.where(nan_share > 0.5, np.nan, np.nanmean(est_phi, axis=1) / S)

    fig, (a1, a2) = new_figure("wide", ncols=2)

    # Left: order splitting, S_hat / S = 1 - rho
    r_f = np.linspace(0, 0.9, 100)
    a1.plot(r_f, 1 - r_f, color=SERIES[0], lw=LW, zorder=2)
    a1.plot(rhos, m_rho, "o", color=SERIES[0], markerfacecolor="white", markeredgewidth=1.4, markersize=6, zorder=3)
    a1.axhline(1.0, color=NEUTRAL, lw=0.9, ls=(0, (3, 3)), zorder=1)
    a1.annotate("True spread S", (0.9, 1.0), xytext=(0, 4), textcoords="offset points", ha="right", fontsize=8,
                color=INK_2)
    a1.annotate("Theory: S(1 − ρ)", (0.3, 0.7), xytext=(8, 8), textcoords="offset points", fontsize=8.5,
                color=INK_2)
    a1.annotate("Simulated", (0.6, m_rho[6]), xytext=(8, 6), textcoords="offset points", fontsize=8.5, color=INK_2)
    a1.set_xlabel("Order-splitting persistence ρ")
    a1.set_ylabel("Roll estimate as a share of true S")
    a1.set_ylim(-0.05, 1.12)
    a1.set_xlim(-0.02, 0.92)
    a1.set_title("Split orders shrink the estimate")

    # Right: informed drift, theory sqrt(1 - phi/(1-phi^2)) until phi* = 0.618, then NaN
    phi_star = (np.sqrt(5) - 1) / 2
    p_f = np.linspace(0, phi_star, 200)
    theory = np.sqrt(np.clip(1 - p_f / (1 - p_f**2), 0, None))
    a2.axvspan(phi_star, 0.92, color=GRID, alpha=0.8, zorder=0, lw=0)
    a2.plot(p_f, theory, color=SERIES[0], lw=LW, zorder=2)
    ok = ~np.isnan(m_phi)
    a2.plot(phis[ok], m_phi[ok], "o", color=SERIES[0], markerfacecolor="white", markeredgewidth=1.4, markersize=6,
            zorder=3)
    bad = np.isnan(m_phi)
    a2.plot(phis[bad], np.zeros(bad.sum()), "x", color=INK_2, markersize=6, markeredgewidth=1.4, zorder=3)
    a2.annotate("NaN:\ncovariance\nturns positive", (0.77, 0.30), ha="center", va="bottom", fontsize=8.5,
                color=INK_2)
    a2.annotate("no spread\nreported", (0.77, 0.07), ha="center", va="bottom", fontsize=8, color=MUTED)
    a2.set_xlabel("Informed drift φ")
    a2.set_ylim(-0.05, 1.12)
    a2.set_xlim(-0.02, 0.92)
    a2.set_yticklabels([])
    a2.set_title("Drift shrinks it, then flips the sign")
    a2.text(0.01, 0.02, f"S = {S:.2f}, σ = {sig:.2f}", transform=a2.transAxes, fontsize=8, color=MUTED)
    return finish(fig, "ch18_roll_splitting_momentum")


# ---------------------------------------------------------------------------------------------
# Figure 18.2: AS vs GLFT quote ribbon and the effective horizon (s18.4-18.5)
# ---------------------------------------------------------------------------------------------
SIG_DAY = 8.0 / np.sqrt(252.0)      # points per sqrt(trading day)
GAMMA, K = 0.005, 3.0


def glft_params(A):
    eta = A * (1 + GAMMA / K) ** (-(1 + K / GAMMA))
    alpha = 0.5 * K * GAMMA * SIG_DAY**2
    return alpha, eta


def glft_stationary_quotes(A, Q=30):
    """Bid and ask distances (points from mid) per inventory level, from the ground state of M (eq. 18.5)."""
    alpha, eta = glft_params(A)
    q = np.arange(-Q, Q + 1)
    M = np.diag(alpha * q**2.0) - eta * (np.eye(2 * Q + 1, k=1) + np.eye(2 * Q + 1, k=-1))
    w, v = np.linalg.eigh(M)
    f = np.abs(v[:, 0])
    greed1 = np.log1p(GAMMA / K) / GAMMA
    db = np.full(q.shape, np.nan)
    da = np.full(q.shape, np.nan)
    db[:-1] = np.log(f[:-1] / f[1:]) / K + greed1
    da[1:] = np.log(f[1:] / f[:-1]) / K + greed1
    return q, db, da


def tau_eff(A):
    alpha, eta = glft_params(A)
    return 1.0 / (2.0 * np.sqrt(alpha * eta))


def fig_quote_ladder():
    greed1 = np.log1p(GAMMA / K) / GAMMA
    q, db, da = glft_stationary_quotes(A=2.0)
    ok = (q >= -20) & (q <= 20)
    # consistency check against the chapter: eta ~ 0.735, omega ~ 0.017, tau_eff ~ 13 trading days
    alpha, eta = glft_params(2.0)
    omega = np.sqrt(alpha / eta) / K
    assert abs(eta - 0.735) < 0.002 and abs(omega - 0.017) < 0.0005 and abs(tau_eff(2.0) - 13.4) < 0.2, (eta, omega)

    fear_as = GAMMA * SIG_DAY**2 * 5.0                # AS skew per lot with a one-week (5-day) horizon
    qa = np.arange(-20, 21)
    as_bid = -(greed1 + (qa + 0.5) * fear_as)         # price relative to mid
    as_ask = greed1 - (qa - 0.5) * fear_as

    fig, (a1, a2) = new_figure("wide", ncols=2)
    a1.fill_between(qa, as_bid, as_ask, color=SERIES[0], alpha=0.22, lw=0, zorder=2)
    a1.plot(qa, as_bid, color=SERIES[0], lw=1.0, zorder=3)
    a1.plot(qa, as_ask, color=SERIES[0], lw=1.0, zorder=3)
    a1.plot(q[ok], -db[ok], color=SERIES[1], lw=LW, zorder=4)
    a1.plot(q[ok], da[ok], color=SERIES[1], lw=LW, zorder=4)
    a1.axhline(0, color=NEUTRAL, lw=0.9, zorder=1)
    a1.annotate("Composite mid", (-20, 0), xytext=(2, 4), textcoords="offset points", fontsize=8, color=MUTED)
    from matplotlib.lines import Line2D
    from matplotlib.patches import Patch
    a1.legend(handles=[Patch(facecolor=SERIES[0], alpha=0.35, label="AS, one-week horizon"),
                       Line2D([0], [0], color=SERIES[1], lw=LW, label="GLFT, stationary")],
              loc="upper right", fontsize=8.5, handlelength=1.6)
    a1.set_xlabel("Inventory q (lots of $1mm; positive = long)")
    a1.set_ylabel("Quote relative to mid (points)")
    a1.set_xlim(-20, 20)
    a1.set_ylim(-0.75, 0.75)
    a1.set_title("Quotes slide down as you get long")
    a1.text(0.99, 0.02, "A = 2 fills/day/side, γ = 0.005, k = 3", transform=a1.transAxes, ha="right", fontsize=8,
            color=MUTED)

    A = np.logspace(-1.3, 2.0, 200)
    a2.loglog(A, tau_eff(A), color=SERIES[1], lw=LW, zorder=3)
    a2.axhline(5.0, color=SERIES[0], lw=1.2, zorder=2)
    a2.annotate("AS horizon in §18.4 (one week)", (0.06, 5.0), xytext=(0, -4), textcoords="offset points",
                fontsize=8.5, color=INK_2, va="top")        # below the line: above it the text hits the GLFT curve
    a2.plot([2.0], [tau_eff(2.0)], "o", color=SERIES[1], markersize=6, zorder=5)
    a2.annotate("A = 2: about 13 days", (2.0, tau_eff(2.0)), xytext=(8, 8), textcoords="offset points", fontsize=8.5,
                color=INK_2)
    a2.annotate("Friday night:\nA → 0, horizon → ∞", (0.07, tau_eff(0.07)), xytext=(0.07, 14),
                textcoords="data", fontsize=8.5, color=INK_2, va="center",
                arrowprops=dict(arrowstyle="->", color=INK_2, lw=0.9))
    a2.set_xlim(0.05, 100)
    a2.set_ylim(1, 100)
    a2.set_xlabel("Arrival rate A (fills/day/side at zero distance)")
    a2.set_ylabel(r"Effective horizon $\tau_{\mathrm{eff}}$ (trading days)")
    a2.grid(True, axis="y")
    a2.set_title("Busier bonds forget faster")
    return finish(fig, "ch18_quote_ladder_glft_horizon")


# ---------------------------------------------------------------------------------------------
# Figure 18.3: Primary dealers' net corporate-bond positions (NY Fed, real data) (s18.5 Trend Watch)
# ---------------------------------------------------------------------------------------------
NYFED_KEYS_LE5 = ["L13", "G13", "BELL13", "BELG13"]
NYFED_KEYS_GT5 = ["G5L10", "G10", "BELG5L10", "BELG10"]


def _build_nyfed_csv():
    """Fetch the eight NY Fed weekly net-position series and write the aggregate CSV (needs network)."""
    import urllib.request
    data = {}
    for k in NYFED_KEYS_LE5 + NYFED_KEYS_GT5:
        url = f"https://markets.newyorkfed.org/api/pd/get/PDPOSCSBND-{k}.json"
        rows = json.load(urllib.request.urlopen(url, timeout=60))["pd"]["timeseries"]
        data[k] = {r["asofdate"]: float(r["value"]) for r in rows}
    dates = sorted(set.intersection(*[set(v) for v in data.values()]))
    os.makedirs(os.path.dirname(DATA_CSV), exist_ok=True)
    with open(DATA_CSV, "w") as f:
        f.write("# NY Fed Primary Dealer Statistics, weekly net positions (long minus short), USD millions.\n")
        f.write("# Source: https://markets.newyorkfed.org/api/pd/get/<keyid>.json ; keyids PDPOSCSBND-"
                "{L13,G13,BELL13,BELG13} (<=5y) and PDPOSCSBND-{G5L10,G10,BELG5L10,BELG10} (>5y); "
                "IG and below-IG bonds, notes, debentures.\n")
        f.write("date,le5y_mm,gt5y_mm\n")
        for d in dates:
            f.write(f"{d},{sum(data[k][d] for k in NYFED_KEYS_LE5):.0f},{sum(data[k][d] for k in NYFED_KEYS_GT5):.0f}\n")


def load_nyfed():
    if not os.path.exists(DATA_CSV):
        _build_nyfed_csv()
    d, le, gt = [], [], []
    with open(DATA_CSV) as f:
        rows = csv.reader(line for line in f if not line.startswith("#"))
        next(rows)
        for r in rows:
            d.append(dt.datetime.strptime(r[0], "%Y-%m-%d"))
            le.append(float(r[1]) / 1000.0)
            gt.append(float(r[2]) / 1000.0)
    return np.array(d), np.array(le), np.array(gt)


def fig_dealer_inventory():
    d, le, gt = load_nyfed()
    w = 13
    ma = lambda x: np.convolve(x, np.ones(w) / w, mode="valid")
    dm = d[w - 1:]
    fig, ax = new_figure("wide")
    ax.axhline(0, color=INK_2, lw=0.9, zorder=2)
    ax.plot(dm, ma(le), color=SERIES[1], lw=LW, zorder=3)
    ax.plot(dm, ma(gt), color=SERIES[0], lw=LW, zorder=4)
    label_end(ax, dm[-1], ma(le)[-1], "Due in ≤ 5 years", SERIES[1], dx=6)
    label_end(ax, dm[-1], ma(gt)[-1], "Due in > 5 years", SERIES[0], dx=6)
    mark_event(ax, dt.datetime(2020, 3, 18), "Mar 2020", y_frac=0.97)
    ax.set_ylabel("Net position, long minus short (USD bn)")
    ax.xaxis.set_major_locator(mdates.YearLocator(base=1))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    ax.set_xlim(dm[0], dm[-1] + dt.timedelta(days=45))
    ax.tick_params(axis="x", labelsize=8.5)
    note(ax, "13-week average of weekly data; IG and below-IG bonds, notes and debentures", loc="lower left")
    # print the numbers the caption and log quote
    for y in (2017, 2026):
        sel = np.array([x.year == y for x in d])
        print(f"  NY Fed {y}: >5y avg {gt[sel].mean():+.1f} bn, <=5y avg {le[sel].mean():+.1f} bn ({sel.sum()} weeks)")
    return finish(fig, "ch18_dealer_net_inventory_nyfed")


# ---------------------------------------------------------------------------------------------
# Figure 18.4: Reservation price vs inventory with jump-to-default, Altice numbers (s18.6)
# ---------------------------------------------------------------------------------------------
def fig_jtd():
    gamma, sigma, tau, J = 0.005, 8.0, 1.0 / 252.0, 21.0
    lamP_tau, lamQ_tau = 0.10, 0.03
    q = np.linspace(-10, 10, 201)

    diff = -q * gamma * sigma**2 * tau                              # AS, Gaussian only
    jump = (lamP_tau / gamma) * np.exp(gamma * q * J) * np.sinh(gamma * J)
    premium = jump - lamP_tau * J                                   # q-dependent jump-risk premium (>0 for long)
    r_nocredit = diff - premium + 0.0                               # lambda^P = lambda^Q: no credit view
    credit_view = (lamP_tau - lamQ_tau) * J
    r_desk = r_nocredit - credit_view                               # eq. 18.7 with mu*tau = lamQ_tau*J

    # chapter check at q = 5: 2.9 points below the composite = 1.47 credit view + 1.46 jump premium
    i5 = np.argmin(np.abs(q - 5))
    assert abs(-r_desk[i5] - 2.93) < 0.02 and abs(credit_view - 1.47) < 0.005 and abs(-r_nocredit[i5] - 1.46) < 0.02

    fig, ax = new_figure("wide")
    ax.axhline(0, color=NEUTRAL, lw=0.9, zorder=1)
    ax.axvline(0, color=NEUTRAL, lw=0.9, ls=(0, (3, 3)), zorder=1)
    ax.plot(q, diff, color=SERIES[0], lw=LW, zorder=3)
    ax.plot(q, r_nocredit, color=SERIES[6], lw=LW, zorder=3)
    ax.plot(q, r_desk, color=SERIES[7], lw=LW, zorder=3)
    ax.annotate("Gaussian AS (diffusion only)", (-9.8, 0.0), xytext=(0, 5), textcoords="offset points",
                ha="left", fontsize=8.5, color=INK_2)
    ax.plot([q[0]], [diff[0]], "o", color=SERIES[0], markersize=4, zorder=5, clip_on=False)
    ax.annotate(r"+ jump-risk premium (no credit view, $\lambda^{P}=\lambda^{Q}$)", (-10, r_nocredit[0]),
                xytext=(0, 9), textcoords="offset points", ha="left", fontsize=8.5, color=INK_2)
    ax.plot([q[0]], [r_nocredit[0]], "o", color=SERIES[6], markersize=4, zorder=5)
    ax.annotate(r"+ desk's credit view ($\lambda^{P}\tau=0.10$, $\lambda^{Q}\tau=0.03$)", (q[-1], r_desk[-1]),
                xytext=(-2, -10), textcoords="offset points", ha="right", va="top", fontsize=8.5, color=INK_2)
    ax.plot([q[-1]], [r_desk[-1]], "o", color=SERIES[7], markersize=4, zorder=5)
    # the q = +5 position of the autopsy: three points on one vertical
    ax.plot([5, 5], [r_desk[i5], 0], color=INK_2, lw=0.9, zorder=2)
    ax.plot([5], [r_nocredit[i5]], "o", color=SERIES[6], markersize=6, markeredgecolor="white", zorder=6)
    ax.plot([5], [diff[i5]], "o", color=SERIES[0], markersize=6, markeredgecolor="white", zorder=6)
    ax.plot([5], [r_desk[i5]], "o", color=SERIES[7], markersize=7, markeredgecolor="white", zorder=6)
    ax.annotate("q = +5 (the Altice autopsy): 2.93 points below the composite\n= 1.47 credit view + 1.46 jump-risk premium",
                (5, r_desk[i5]), xytext=(-9.8, -4.9), textcoords="data", ha="left", va="center", fontsize=8.5, color=INK,
                arrowprops=dict(arrowstyle="->", color=INK_2, lw=0.9, shrinkA=2, shrinkB=5,
                                connectionstyle="arc3,rad=0.15"))
    ax.annotate("Reported one-day move on 20 March 2024: about −21 points (off scale)",
                (0.01, 0.02), xycoords="axes fraction", fontsize=8, color=MUTED, va="bottom", ha="left")
    ax.set_xlabel("Dealer inventory q (lots of $1mm; positive = long)")
    ax.set_ylabel("Reservation price minus composite (points)")
    ax.set_xlim(-10, 10)
    ax.set_ylim(-7.2, 3.0)
    return finish(fig, "ch18_jtd_reservation_price")


# ---------------------------------------------------------------------------------------------
# Figure 18.5: The cold-open bid, term by term (s18.7, eq. 18.9)
# ---------------------------------------------------------------------------------------------
def cold_open_terms():
    s, q, n = 91.25, 3, 8
    sigma, gamma, tau, J = 8.0, 0.005, 5.0 / 252.0, 20.0
    lamP_tau, lamQ_tau = 0.025, 0.02
    a_c, nu, beta0, beta1 = 0.15, 0.05, 0.0, 4.0

    def theta(qq):
        mu_tau = lamQ_tau * J
        return (qq * (s + mu_tau) - 0.5 * gamma * qq**2 * sigma**2 * tau
                - (lamP_tau / gamma) * np.expm1(gamma * qq * J))

    r_b = (theta(q + n) - theta(q)) / n
    credit = (lamP_tau - lamQ_tau) * J
    fear = (s - r_b) - credit
    d = (s - r_b) + a_c

    def P(x):
        return 1.0 / (1.0 + np.exp(-(beta0 - beta1 * x)))

    def greed(x):
        return np.log1p(gamma * n / (beta1 * (1 - P(x)))) / (gamma * n)

    lo, hi = 0.0, 5.0
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if mid - (d - nu + greed(mid)) < 0:
            lo = mid
        else:
            hi = mid
    x = 0.5 * (lo + hi)
    terms = dict(credit=credit, fear=fear, suspicion=a_c, greed=greed(x), franchise=-nu)
    assert abs(sum(terms.values()) - x) < 1e-9
    return s, x, terms, P(x)


def fig_waterfall():
    s, x, t, p_win = cold_open_terms()
    # chapter table: 0.10, 0.58, 0.15, 0.25, -0.05; bid 90.22
    assert [round(v, 2) for v in t.values()] == [0.10, 0.58, 0.15, 0.25, -0.05], t
    assert abs(s - x - 90.22) < 0.005 and abs(p_win - 0.016) < 0.002, (s - x, p_win)

    labels = ["Credit view", "Fear (diffusive + jump)", "Suspicion", "Greed", "Franchise (subsidy)"]
    vals = [t["credit"], t["fear"], t["suspicion"], t["greed"], t["franchise"]]
    fig, ax = new_figure("wide")
    left = 0.0
    ypos = np.arange(len(labels) + 1)[::-1]            # top to bottom
    for yi, lab, v in zip(ypos, labels, vals):
        col = SERIES[0] if v > 0 else "#e66767"
        lft = left if v > 0 else left + v
        ax.barh(yi, abs(v), left=lft, height=0.62, color=col, zorder=3)
        txt = f"\u2212{abs(v):.2f}" if v < 0 else f"{v:.2f}"
        ax.annotate(txt, (lft + abs(v), yi), xytext=(5, 0), textcoords="offset points", va="center", fontsize=8.5,
                    color=INK_2)
        left += v
    ax.barh(ypos[-1], x, left=0, height=0.62, color=INK_2, zorder=3)
    ax.annotate(f"{x:.2f}  (bid {s - x:.2f}, quoted 90.25)", (x, ypos[-1]), xytext=(5, 0), textcoords="offset points",
                va="center", fontsize=8.5, color=INK_2)
    ax.set_yticks(ypos)
    ax.set_yticklabels(labels + ["Total distance"])
    ax.tick_params(axis="y", length=0, labelsize=9)
    ax.grid(False)
    ax.grid(True, axis="x")
    ax.set_xlabel(f"Points below the {s:.2f} composite")
    ax.set_xlim(0, 1.75)
    # reference quotes
    kaz_x, cover_x = s - 90.875, s - 90.50
    ax.axvline(x, color=NEUTRAL, lw=0.9, ls=(0, (3, 3)), zorder=1)
    for xv, lab in [(kaz_x, "Kaz 90.875"), (cover_x, "Cover 90.50")]:
        ax.axvline(xv, color=NEUTRAL, lw=0.9, ls=(0, (3, 3)), zorder=1)
        ax.annotate(lab, (xv, 1.0), xycoords=("data", "axes fraction"), xytext=(0, 3), textcoords="offset points",
                    fontsize=8, color=INK_2, ha="center", va="bottom")
    ax.annotate(f"Ines 90.22\nwins {p_win * 100:.1f}%", (x, 1.0), xycoords=("data", "axes fraction"), xytext=(0, 3),
                textcoords="offset points", fontsize=8, color=INK_2, ha="center", va="bottom")
    ax.set_ylim(-0.6, len(labels) + 0.6)
    return finish(fig, "ch18_cold_open_bid_waterfall")


if __name__ == "__main__":
    fig_roll()
    fig_quote_ladder()
    fig_dealer_inventory()
    fig_jtd()
    fig_waterfall()
