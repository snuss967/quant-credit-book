"""Chapter 23 figures: cross-asset convexity and the volatility surface.

Run from anywhere:  python3 tools/figures/ch23.py   (writes assets/figures/ch23_*.png)

Figures
  ch23_waterfall_call_spreads   tranche payoffs as call spreads on firm value, and where the value sits (section 23.1)
  ch23_leverage_skew            eq. (23.1)/(23.2): equity vol and model spread as assets fall (section 23.1)
  ch23_creditgrades_ghost       eq. (23.3)/(23.5): survival curve with its time-zero mass, and spread curves (section 23.2)
  ch23_jtd_skew_floor           eq. (23.8): jump-to-default skew and the P(K)/K floor (section 23.4)
  ch23_bank_run_runway          the liquidity-runway default clock of Listing 23.5 (section 23.8)

Data
  Every figure is Illustrative: closed forms and parameters stated in the chapter. The pricing functions below are
  copies of the reference listings in Appendix F (Listings 23.1, 23.2 and 23.5), so the figures reproduce the
  chapter's own numbers (Merton table, CreditGrades ghost, JTD implied vols, the day-2 bank default).

Colors (fixed for the chapter)
  Capital-structure claims: first lien BLUE, second lien ORANGE, unsecured AQUA, equity VIOLET.
  Magnitudes that are not claims (stock price level, hazard level) use the sequential blue ramp, dark = stressed.
"""
import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from style import *            # applies the rcParams on import

import numpy as np
import pandas as pd
from matplotlib.patches import Rectangle
from scipy.optimize import brentq
from scipy.stats import norm

C_1L, C_2L, C_UNS, C_EQ = BLUE, ORANGE, AQUA, VIOLET
RAMP = {"light": SEQ_BLUE_STEPS[5], "mid": SEQ_BLUE_STEPS[8], "dark": SEQ_BLUE_STEPS[12]}


# --------------------------------------------------------------------------------------------------
# Pricing functions (copies of Appendix F, Listings 23.1, 23.2, 23.5)
# --------------------------------------------------------------------------------------------------
def merton_equity(V, F, r, sigma_V, T):
    srt = sigma_V * np.sqrt(T)
    d1 = np.clip((np.log(V / F) + (r + 0.5 * sigma_V**2) * T) / srt, -40, 40)
    d2 = d1 - srt
    E = V * norm.cdf(d1) - F * np.exp(-r * T) * norm.cdf(d2)
    return E, d1, d2


def merton_equity_vol(V, F, r, sigma_V, T):
    E, d1, _ = merton_equity(V, F, r, sigma_V, T)
    return sigma_V * V * norm.cdf(d1) / E


def merton_spread(V, F, r, sigma_V, T):
    _, d1, d2 = merton_equity(V, F, r, sigma_V, T)
    return -np.log(norm.cdf(d2) + V / (F * np.exp(-r * T)) * norm.cdf(-d1)) / T


def cg_asset_state(S0, sigma_E, F_ps, ell_bar=0.5):
    V0 = S0 + ell_bar * F_ps
    return V0, sigma_E * S0 / V0


def cg_survival(t, S0, sigma_E, F_ps, ell_bar=0.5, nu=0.3):
    t = np.asarray(t, dtype=float)
    V0, sigma_V = cg_asset_state(S0, sigma_E, F_ps, ell_bar)
    log_d = np.log(V0 / (ell_bar * F_ps)) + nu**2
    Sig = np.maximum(np.sqrt(sigma_V**2 * t + nu**2), 1e-12)
    first = norm.cdf(-Sig / 2 + log_d / Sig)
    second = np.exp(log_d + norm.logcdf(-Sig / 2 - log_d / Sig))
    return first - second


def cg_cds_spread(T, S0, sigma_E, F_ps, R=0.4, r=0.03, ell_bar=0.5, nu=0.3, dt=1 / 12):
    n = max(int(round(T / dt)), 1)
    t = np.linspace(0.0, T, n + 1)
    surv = cg_survival(t, S0, sigma_E, F_ps, ell_bar, nu)
    h = np.diff(t)
    rpv01 = np.sum(h * np.exp(-r * t[1:]) * 0.5 * (surv[:-1] + surv[1:]))
    t_mid = 0.5 * (t[:-1] + t[1:])
    prot = (1 - R) * ((1 - surv[0]) + np.sum(np.exp(-r * t_mid) * (surv[:-1] - surv[1:])))
    return float(prot / rpv01)


def bs_put(S0, K, T, r, q, sigma):
    d1 = (np.log(S0 / K) + (r - q + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return K * np.exp(-r * T) * norm.cdf(-d2) - S0 * np.exp(-q * T) * norm.cdf(-d1)


def jtd_put_price(S0, K, T, r, q, sigma, lam):
    K = np.asarray(K, dtype=float)
    srt = sigma * np.sqrt(T)
    d1 = np.clip((np.log(S0 / K) + (r - q + lam + 0.5 * sigma**2) * T) / srt, -40, 40)
    d2 = d1 - srt
    pays_K = -np.expm1(-lam * T) + np.exp(-lam * T) * norm.cdf(-d2)
    return K * np.exp(-r * T) * pays_K - S0 * np.exp(-q * T) * norm.cdf(-d1)


def bs_implied_vol_put(price, S0, K, T, r, q):
    return brentq(lambda v: float(bs_put(S0, K, T, r, q, v)) - price, 1e-4, 5.0, xtol=1e-12)


def bank_run_dd(cash, securities, haircut, max_monetize_per_day, uninsured, kappa, rho, equity_rets):
    """Listing 23.5, returning also the proceeds of securities sold and the run rate each day."""
    dep_u, liquid, sec = float(uninsured), float(cash), float(securities)
    path = []
    for day, ret in enumerate(equity_rets, start=1):
        rate = min(1.0, kappa * max(0.0, -ret) + rho * (1.0 - dep_u / uninsured))
        outflow = rate * dep_u
        raised = min(sec * (1.0 - haircut), max_monetize_per_day)
        sec -= raised / (1.0 - haircut)
        before = liquid
        liquid += raised
        path.append({"day": day, "rate": rate, "start": before, "raised": raised,
                     "outflow": outflow, "liquidity": liquid})
        if outflow > liquid:
            return {"default_day": day, "path": pd.DataFrame(path)}
        liquid -= outflow
        dep_u -= outflow
    return {"default_day": None, "path": pd.DataFrame(path)}


def lognormal_pdf(x, V0, sigma, r, T):
    """Risk-neutral density of V_T: ln V_T ~ N(ln V0 + (r - sigma^2/2) T, sigma^2 T)."""
    m, s = np.log(V0) + (r - 0.5 * sigma**2) * T, sigma * np.sqrt(T)
    x = np.asarray(x, dtype=float)
    out = np.zeros_like(x)
    pos = x > 0
    out[pos] = np.exp(-0.5 * ((np.log(x[pos]) - m) / s) ** 2) / (x[pos] * s * np.sqrt(2 * np.pi))
    return out


def lognormal_cdf(x, V0, sigma, r, T):
    if x <= 0:
        return 0.0
    m, s = np.log(V0) + (r - 0.5 * sigma**2) * T, sigma * np.sqrt(T)
    return float(norm.cdf((np.log(x) - m) / s))


# --------------------------------------------------------------------------------------------------
# Figure 1: the waterfall is a stack of call spreads
# --------------------------------------------------------------------------------------------------
def fig_waterfall_call_spreads():
    fig, (ax1, ax2) = new_figure("wide", ncols=2)
    tranches = [("First lien", 0.0, 40.0, C_1L), ("Second lien", 40.0, 55.0, C_2L),
                ("Unsecured", 55.0, 70.0, C_UNS), ("Equity", 70.0, np.inf, C_EQ)]
    V = np.linspace(0, 130, 1041)

    # left: tranche payoffs, stacked (the stack's top edge is the 45-degree line V_T)
    base = np.zeros_like(V)
    for name, a, b, col in tranches:
        pay = np.maximum(V - a, 0.0) - (np.maximum(V - b, 0.0) if np.isfinite(b) else 0.0)
        ax1.fill_between(V, base, base + pay, color=col, alpha=0.88, linewidth=0, zorder=2)
        base = base + pay
    ax1.plot(V, V, color=INK_2, linewidth=0.9, zorder=3)
    for k in (40, 55, 70):
        ax1.plot([k, k], [0, k], color="white", linewidth=0.8, zorder=4)
    ax1.set_xlim(0, 130)
    ax1.set_ylim(0, 130)
    ax1.set_xticks([0, 40, 55, 70, 100, 130])
    ax1.grid(False)
    ax1.set_xlabel(r"Firm value at resolution, $V_T$")
    ax1.set_ylabel("Payoff to each claim")
    kw = dict(fontsize=8, fontweight="bold", va="center", ha="center", zorder=6)
    ax1.text(100, 20, "1st lien\n0 to 40", color="white", **kw)
    ax1.text(100, 47.5, "2nd lien: 40 to 55", color=INK, **kw)
    ax1.text(100, 62.5, "Unsecured: 55 to 70", color=INK, **kw)
    ax1.text(115, 88, "Equity:\ncall at\nF = 70", color="white", **kw)
    ax1.text(3, 121, r"Each band is $(V_T-a_k)^+ - (V_T-b_k)^+$", fontsize=8, color=INK_2, va="center",
             ha="left", zorder=6)

    # right: the risk-neutral law of V_T with the same strikes; V0 = 62 sits inside the unsecured interval
    V0, sig, r, T = 62.0, 0.25, 0.03, 1.0
    x = np.linspace(0.5, 130, 1500)
    pdf = lognormal_pdf(x, V0, sig, r, T)
    edges = [0.0, 40.0, 55.0, 70.0, 130.0]
    probs = []
    for (name, a, b, col), lo, hi in zip(tranches, edges[:-1], edges[1:]):
        m = (x >= lo) & (x <= hi)
        ax2.fill_between(x[m], 0, pdf[m], color=col, alpha=0.88, linewidth=0, zorder=2)
        p = lognormal_cdf(hi if np.isfinite(b) else 1e9, V0, sig, r, T) - lognormal_cdf(lo, V0, sig, r, T)
        probs.append(p)
    ax2.plot(x, pdf, color=INK_2, linewidth=0.9, zorder=3)
    for k in (40, 55, 70):
        ax2.plot([k, k], [0, float(lognormal_pdf(np.array([k]), V0, sig, r, T)[0])], color="white", linewidth=0.8,
                 zorder=4)
    ymax = pdf.max() * 1.7
    ax2.plot([V0, V0], [0, ymax * 0.84], color=INK, linewidth=1.0, linestyle=(0, (3, 2)), zorder=5)
    ax2.set_xlim(0, 130)
    ax2.set_ylim(0, ymax)
    ax2.set_yticks([])
    ax2.grid(False)
    ax2.set_xticks([0, 40, 55, 70, 100, 130])
    ax2.set_xlabel(r"Firm value at resolution, $V_T$")
    ax2.set_ylabel("Risk-neutral density")
    ax2.text(V0 + 2.5, ymax * 0.73, r"Today: $V_0 = 62$" + "\nunsecured is\nthe fulcrum", fontsize=8, color=INK,
             ha="left", va="center")
    # probability of ending in each interval, as a strip along the top that names each claim
    xs = [19.0, 41.0, 68.0, 100.0]
    short_names = ["1st lien", "2nd lien", "Unsecured", "Equity"]
    for xc, p, name in zip(xs, probs, short_names):
        ax2.text(xc, ymax * 0.955, f"{100 * p:.0f}%", fontsize=8.5, fontweight="bold", color=INK, ha="center",
                 va="center", zorder=6)
        ax2.text(xc, ymax * 0.895, name, fontsize=8, color=INK_2, ha="center", va="center", zorder=6)
    ax2.text(2, ymax * 0.72, "Chance $V_T$ lands\nin each claim's\ninterval = chance\nit is the fulcrum", fontsize=8,
             color=INK_2, ha="left", va="center")
    return finish(fig, "ch23_waterfall_call_spreads")


# --------------------------------------------------------------------------------------------------
# Figure 2: leverage skew and the model spread
# --------------------------------------------------------------------------------------------------
def fig_leverage_skew():
    F, r, sV, T = 70.0, 0.03, 0.25, 1.0
    V = np.linspace(56, 160, 400)
    sE = merton_equity_vol(V, F, r, sV, T)
    spr = merton_spread(V, F, r, sV, T) * 1e4
    pts = np.array([150.0, 100.0, 75.0])
    sE_pts = merton_equity_vol(pts, F, r, sV, T)
    spr_pts = merton_spread(pts, F, r, sV, T) * 1e4

    fig, (ax1, ax2) = new_figure("wide", ncols=2)
    # left: equity vol vs assets
    ax1.axhline(100 * sV, color=NEUTRAL, linewidth=1.2, linestyle=(0, (4, 3)), zorder=1)
    ax1.text(157, 100 * sV - 3, r"Asset vol $\sigma_V$ = 25%, never moves", fontsize=8, color=MUTED, ha="left",
             va="top")
    ax1.plot(V, 100 * sE, color=C_EQ, linewidth=LW, zorder=3)
    ax1.plot(pts, 100 * sE_pts, "o", color=C_EQ, markersize=5, zorder=4)
    for v, s in zip(pts, sE_pts):
        if v == 75.0:
            ax1.annotate(f"{100 * s:.0f}%", (v, 100 * s), xytext=(-8, 6), textcoords="offset points", fontsize=8.5,
                         color=INK_2, ha="right", va="bottom")
        else:
            ax1.annotate(f"{100 * s:.0f}%", (v, 100 * s), xytext=(8, -7), textcoords="offset points", fontsize=8.5,
                         color=INK_2, ha="left", va="top")
    ax1.axvline(F, color=NEUTRAL, linewidth=0.9, linestyle=(0, (3, 3)), zorder=1)
    ax1.text(F + 1.5, 6, "debt F = 70", fontsize=8, color=INK_2, ha="right", va="bottom")
    ax1.set_xlim(55, 160)
    ax1.set_ylim(0, 200)
    ax1.invert_xaxis()
    ax1.set_xlabel(r"Firm assets $V$ (falling to the right)")
    ax1.set_ylabel(r"Equity vol $\sigma_E$ (%)")
    ax1.text(0.03, 0.97, "Equity vol", transform=ax1.transAxes, fontsize=8.5, fontweight="bold", color=INK_2,
             va="top")

    # right: model credit spread vs assets (log scale)
    ax2.plot(V, spr, color=C_1L, linewidth=LW, zorder=3)
    ax2.plot(pts, spr_pts, "o", color=C_1L, markersize=5, zorder=4)
    for v, s, dx, dy, ha in zip(pts, spr_pts, (8, 8, 8), (-6, -6, -6), ("left", "left", "left")):
        txt = f"{s:.0f}bp" if s >= 10 else f"{s:.1f}bp"
        if v == 75.0:
            ax2.annotate(txt, (v, s), xytext=(-8, 6), textcoords="offset points", fontsize=8.5, color=INK_2,
                         ha="right", va="bottom")
        else:
            ax2.annotate(txt, (v, s), xytext=(dx, dy), textcoords="offset points", fontsize=8.5, color=INK_2,
                         ha=ha, va="top")
    ax2.axvline(F, color=NEUTRAL, linewidth=0.9, linestyle=(0, (3, 3)), zorder=1)
    ax2.set_yscale("log")
    ax2.set_xlim(55, 160)
    ax2.invert_xaxis()
    ax2.set_ylim(0.3, 8000)
    ax2.set_xlabel(r"Firm assets $V$ (falling to the right)")
    ax2.set_ylabel("Model 1-year spread (bp, log scale)")
    ax2.text(0.03, 0.97, "Merton credit spread", transform=ax2.transAxes, fontsize=8.5, fontweight="bold",
             color=INK_2, va="top")
    ax2.text(0.03, 0.89, r"$F=70$, $r=3\%$, $T=1$, $\sigma_V=25\%$", transform=ax2.transAxes, fontsize=8,
             color=MUTED, va="top")
    return finish(fig, "ch23_leverage_skew")


# --------------------------------------------------------------------------------------------------
# Figure 3: CreditGrades survival with its time-zero mass, and the spread curves it produces
# --------------------------------------------------------------------------------------------------
def fig_creditgrades_ghost():
    sE, F_ps = 0.40, 30.0
    names = [(30.0, RAMP["light"], r"$S_0=\$30$"), (15.0, RAMP["mid"], r"$S_0=\$15$"),
             (5.0, RAMP["dark"], r"$S_0=\$5$")]
    fig, (ax1, ax2) = new_figure("wide", ncols=2)

    t = np.linspace(0.0, 5.0, 301)
    for S0, col, lab in names:
        surv = cg_survival(t, S0, sE, F_ps)
        ax1.plot(t, surv, color=col, linewidth=LW, zorder=3)
        ax1.plot([0], [surv[0]], "o", color=col, markersize=5, zorder=5, clip_on=False)
    s5 = float(cg_survival(0.0, 5.0, sE, F_ps))
    s30 = float(cg_survival(0.0, 30.0, sE, F_ps))
    ax1.set_xlim(0, 5)
    ax1.set_ylim(0.55, 1.02)
    ax1.set_xlabel("Years")
    ax1.set_ylabel(r"Survival probability $\mathcal{S}(t)$")
    ax1.annotate(f"At $S_0=\\$5$, a {100 * (1 - s5):.0f}% default\nprobability is booked at\nt = 0: the time-zero ghost", (0.0, s5),
                 xytext=(0.45, 0.805), textcoords="data", fontsize=8, color=INK, ha="left", va="center",
                 arrowprops=dict(arrowstyle="-", color=INK_2, lw=0.8, shrinkA=2, shrinkB=4))
    label_end(ax1, 5.0, float(cg_survival(5.0, 30.0, sE, F_ps)), r"\$30", RAMP["light"])
    label_end(ax1, 5.0, float(cg_survival(5.0, 15.0, sE, F_ps)), r"\$15", RAMP["mid"])
    label_end(ax1, 5.0, float(cg_survival(5.0, 5.0, sE, F_ps)), r"\$5", RAMP["dark"])

    tenors = np.array([0.25, 0.5, 1, 2, 3, 4, 5, 7, 10], dtype=float)
    end_lab = {30.0: r"\$30", 15.0: r"\$15", 5.0: r"\$5"}
    for S0, col, lab in names:
        sp = np.array([cg_cds_spread(T, S0, sE, F_ps) for T in tenors]) * 1e4
        ax2.plot(tenors, sp, color=col, linewidth=LW, marker="o", markersize=4, zorder=3)
        label_end(ax2, tenors[-1], sp[-1], end_lab[S0], col, dy={30.0: -4, 15.0: 4, 5.0: 0}[S0])
    ax2.set_yscale("log")
    ax2.set_xlim(0, 10)
    ax2.set_ylim(10, 12000)
    ax2.set_xlabel("CDS tenor (years)")
    ax2.set_ylabel("CreditGrades par spread (bp, log scale)")
    ax2.text(0.97, 0.97, "healthy: upward-sloping\nstressed: inverted", transform=ax2.transAxes, fontsize=8,
             color=MUTED, ha="right", va="top")
    note(ax2, r"$\sigma_E=40\%$, $F^{ps}=\$30$, $R=40\%$", loc="lower right")
    return finish(fig, "ch23_creditgrades_ghost")


# --------------------------------------------------------------------------------------------------
# Figure 4: jump-to-default skew and the low-strike floor
# --------------------------------------------------------------------------------------------------
def fig_jtd_skew_floor():
    S0, T, r, q, sig = 100.0, 1.0, 0.03, 0.0, 0.30
    lams = [(0.025, RAMP["light"]), (0.05, RAMP["mid"]), (0.10, RAMP["dark"])]
    m = np.linspace(0.20, 1.20, 201)          # moneyness K / S0
    K = m * S0
    halo = dict(boxstyle="square,pad=0.12", fc="white", ec="none", alpha=0.9)

    fig, (ax1, ax2) = new_figure("wide", ncols=2)

    # left: Black-Scholes implied vol of the JTD put prices
    ax1.axhline(100 * sig, color=NEUTRAL, linewidth=1.2, linestyle=(0, (4, 3)), zorder=1)
    ax1.text(1.19, 100 * sig - 3, "30%: pure diffusion, no skew", fontsize=8, color=MUTED, ha="right", va="top")
    lam, col = 0.05, RAMP["mid"]
    iv = np.array([bs_implied_vol_put(float(jtd_put_price(S0, k, T, r, q, sig, lam)), S0, k, T, r, q) for k in K])
    ax1.plot(m, 100 * iv, color=col, linewidth=LW, zorder=3)
    qs = [0.2, 0.4, 0.6, 0.8, 1.0]
    qv = [bs_implied_vol_put(float(jtd_put_price(S0, x * S0, T, r, q, sig, lam)), S0, x * S0, T, r, q) for x in qs]
    ax1.plot(qs, 100 * np.array(qv), "o", color=col, markersize=5, zorder=4)
    for x, v in zip(qs, qv):
        ax1.annotate(f"{100 * v:.0f}%", (x, 100 * v), xytext=(8, 6), textcoords="offset points",
                     fontsize=8.5, color=INK, ha="left", va="bottom")
    ax1.text(0.97, 0.97, r"$\lambda$ = 5%, $\sigma$ = 30%, $T$ = 1", transform=ax1.transAxes, fontsize=8,
             color=MUTED, ha="right", va="top")
    ax1.set_xlim(0.1, 1.25)
    ax1.set_ylim(20, 140)
    ax1.set_xticks([0.2, 0.4, 0.6, 0.8, 1.0, 1.2])
    ax1.set_xlabel(r"Strike / spot, $K/S_0$")
    ax1.set_ylabel("Black-Scholes implied vol (%)")

    # right: P(K)/K, which is flat at the hazard under JTD and goes to zero under a pure diffusion
    kk = np.linspace(2.0, 100.0, 300)
    mm = kk / S0
    bsr = np.array([float(bs_put(S0, k, T, r, q, sig)) / k for k in kk])
    ax2.plot(mm, 100 * bsr, color=NEUTRAL, linewidth=1.8, linestyle=(0, (4, 3)), zorder=2)
    for lam, col in lams:
        pk = np.asarray(jtd_put_price(S0, kk, T, r, q, sig, lam)) / kk
        ax2.plot(mm, 100 * pk, color=col, linewidth=LW, zorder=3)
        floor = np.exp(-r * T) * (1 - np.exp(-lam * T))
        ax2.text(0.02, 100 * floor + 0.35, f"$\\lambda$={100 * lam:g}%: floor {100 * floor:.1f}%", fontsize=8,
                 color=INK_2, ha="left", va="bottom")
    ax2.text(0.02, 0.45, "no jump: falls to 0", fontsize=8, color=MUTED, ha="left", va="bottom")
    ax2.set_xlim(0.0, 1.0)
    ax2.set_ylim(0, 16.5)
    ax2.set_xlabel(r"Strike / spot, $K/S_0$")
    ax2.set_ylabel(r"Put price per dollar of strike, $P(K)/K$ (%)")
    note(ax2, r"$\sigma=30\%$, $T=1$, $r=3\%$", loc="upper left")
    return finish(fig, "ch23_jtd_skew_floor")


# --------------------------------------------------------------------------------------------------
# Figure 5: the liquidity runway of a deposit-funded bank
# --------------------------------------------------------------------------------------------------
def fig_bank_run_runway():
    run = bank_run_dd(cash=13.0, securities=115.0, haircut=0.10, max_monetize_per_day=30.0,
                      uninsured=165.0, kappa=0.42, rho=2.0, equity_rets=[-0.60, -0.30, -0.10])
    assert run["default_day"] == 2
    p = run["path"]
    d1, d2 = p.iloc[0], p.iloc[1]
    _, _, d2_bank = merton_equity(212.0, 196.0, 0.03, 0.04, 1.0)
    merton_pd = float(norm.cdf(-d2_bank))
    carried = d1["start"] + d1["raised"] - d1["outflow"]
    short = d2["liquidity"] - d2["outflow"]

    def num(v):                      # whole bn when exact, else two decimals, so every bar adds up on the page
        return f"{v:.0f}" if abs(v - round(v)) < 1e-9 else f"{v:.2f}"
    steps = [("Opening\ncash", d1["start"], "total", num(d1["start"])),
             ("Sell\nsecurities", d1["raised"], "in", "+" + num(d1["raised"])),
             ("Day-1\nliquidity", d1["liquidity"], "total", num(d1["liquidity"])),
             ("Day-1\noutflow", -d1["outflow"], "out", "−" + num(d1["outflow"])),
             ("Carried\nto day 2", carried, "total", num(carried)),
             ("Sell\nsecurities", d2["raised"], "in", "+" + num(d2["raised"])),
             ("Day-2\nliquidity", d2["liquidity"], "total", num(d2["liquidity"])),
             ("Day-2\noutflow", -d2["outflow"], "out", "−" + num(d2["outflow"])),
             ("Shortfall:\ndefault", short, "default", "−" + num(-short))]
    fig, ax = new_figure((7.0, 3.9))
    ax.grid(False)
    cum = 0.0
    prev_top = None
    for i, (lab, val, kind, txt) in enumerate(steps):
        if kind == "total":
            lo, hi, col = min(0.0, val), max(0.0, val), NEUTRAL
            cum = val
        elif kind == "in":
            lo, hi, col = cum, cum + val, C_1L
            cum += val
        elif kind == "out":
            lo, hi, col = cum + val, cum, C_2L
            cum += val
        else:
            lo, hi, col = val, 0.0, STATUS["critical"]
        ax.add_patch(Rectangle((i - 0.36, lo), 0.72, hi - lo, facecolor=col, edgecolor="none", zorder=3))
        if i + 1 < len(steps):          # connector to the next bar at the running total
            ax.plot([i + 0.36, i + 1 - 0.36], [cum, cum], color=INK_2, linewidth=0.7, zorder=2)
        ytxt = hi + 2.0 if kind in ("total", "in") else lo - 2.0
        va = "bottom" if kind in ("total", "in") else "top"
        if kind == "out" and hi > 0 and lo < 0:
            ytxt, va = hi + 2.0, "bottom"
        if kind == "default":
            ytxt, va = lo - 2.0, "top"
        ax.text(i, ytxt, txt, ha="center", va=va, fontsize=8.5, color=INK, fontweight="bold", zorder=5)
    ax.axhline(0, color=INK_2, linewidth=0.9, zorder=4)
    ax.set_xlim(-0.7, len(steps) - 0.3)
    ax.set_ylim(-68, 84)
    ax.set_xticks(range(len(steps)))
    ax.set_xticklabels([s[0] for s in steps], fontsize=8)
    ax.tick_params(axis="x", length=0)
    ax.set_ylabel("Liquidity ($bn)")
    ax.text(3, -12, f"run rate {100 * d1['rate']:.0f}% of uninsured\ndeposits (equity \u221260%)",
            ha="center", va="top", fontsize=8, color=INK_2)
    ax.text(6.55, -12, f"run rate {100 * d2['rate']:.0f}%\n(panic feedback)", ha="right",
            va="top", fontsize=8, color=INK_2)
    ax.text(0.01, 0.03, f"Merton 1-year default probability on\nthe same balance sheet: {100 * merton_pd:.1f}%",
            transform=ax.transAxes, ha="left", va="bottom", fontsize=8.5, color=INK_2)
    # legend by colored swatches
    import matplotlib.patches as mpatches
    ax.legend(handles=[mpatches.Patch(color=NEUTRAL, label="Liquidity on hand"),
                       mpatches.Patch(color=C_1L, label="Securities sold (after 10% haircut)"),
                       mpatches.Patch(color=C_2L, label="Uninsured deposits leaving")],
              loc="upper right", fontsize=8, handlelength=1.2, borderaxespad=0.2)
    return finish(fig, "ch23_bank_run_runway")


if __name__ == "__main__":
    fig_waterfall_call_spreads()
    fig_leverage_skew()
    fig_creditgrades_ghost()
    fig_jtd_skew_floor()
    fig_bank_run_runway()
