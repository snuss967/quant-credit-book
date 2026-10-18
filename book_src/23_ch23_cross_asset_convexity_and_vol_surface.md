# Chapter 23: Cross-Asset Convexity & the Volatility Surface

6:40 a.m., Thursday, March 9, 2023. Theo Marsh has been on the systematic credit desk for three weeks and still reads bank filings for fun, which is how he knows things nobody has asked him yet. Last night SVB Financial Group announced that it had sold \$21 billion of available-for-sale securities, was booking a \$1.8 billion after-tax loss, and wanted to raise \$2.25 billion of capital (Federal Reserve, *Review of the Federal Reserve's Supervision and Regulation of Silicon Valley Bank*, April 28, 2023). The stock is indicated sharply lower.

Kaz has the SIVB listed put surface on the big screen. "The one-month low-strike puts are bid at an implied vol that makes no sense," they say, "unless the stock is going to zero."

"It can go to zero by lunch," Theo says. "At year-end about 94 percent of the deposits were uninsured, and the held-to-maturity book had a weighted-average duration of 6.2 years. The equity is a call option on whether the depositors read the same footnote I did."

Ines does not look up from her markouts. "So what's the pot, what are the odds, and who at this table knows more than you? Somebody is lifting every put we show, and it isn't a pension fund rebalancing."

"Merton says the distance to default is fine," Kaz offers. "Bank asset volatility is tiny."

"Bank asset volatility is tiny right up until the assets are on the other side of the street," says Mags, from the distressed corner, where the screens are older and the opinions are firmer. "The holdco notes were mid-80s on Monday. Price is what you pay. Recovery is what you get, eventually, after the FDIC."

ROBO's overnight batch, asked to "compute the equity-implied CDS spread for every bank in the book," has helpfully populated a column. SVB Financial Group: 12bp. Nobody has the heart to tell it.

The question this chapter answers is the one Ines is really asking: *when the equity-volatility surface and the credit curve disagree, which one is lying, and how do you size the bet that it's the other one?*

By the end of this chapter you will be able to: translate an equity price and volatility into a model credit spread with Merton and CreditGrades, and invert a CDS quote into an implied asset volatility; extract a model-free unit recovery claim from a listed put spread (Carr–Wu) and trade it against CDS; read the low-strike skew as a hazard rate; express credit Greeks in spread units and build a delta-hedged capital-structure book; run Yu's convergence trade and explain why single trades lose while portfolios earn; and say precisely why the surface broke in May 2005, March 2023, and the 2025–26 cycle.

## 23.1 One Distribution, Many Strikes: The Capital Structure as a Vol Surface

In RSSG, Theo built waterfalls. A waterfall takes an enterprise value and hands it out by priority: the first-lien gets paid until it is whole, then the second-lien, then the unsecureds, then whatever is left falls to equity. He thought of it as a legal object. It is also a payoff diagram. If tranche $k$ attaches at claim level $a_k$ and detaches at $b_k$ (cumulative claims senior to it, and senior plus itself), then at resolution it receives

$$
\text{Payoff}_k(V_T) = (V_T - a_k)^+ - (V_T - b_k)^+ ,
$$

a call spread on firm value $V_T$ struck at its attachment and detachment points. Equity is the call struck at total debt $F$. The fulcrum security is the tranche whose strike interval contains the value: the at-the-money strike. When Kaz first heard the term they asked whether "the fulcrum" was the security with the most leverage, which is exactly right and is the annoying thing about Kaz.

What RSSG never priced is the *distribution* of $V_T$. Theo ran three EV cases, called them low, mid, and high, and wrote a recovery under each. The systematic desk prices the whole distribution, and the market reveals that distribution one strike at a time: the stock is the high strike, the bonds are the middle strikes, CDS is the middle strike stripped of rates, and a deep out-of-the-money equity put is a bet on the low tail that happens to trade on an exchange. A CCC bond is an equity option that wears a tie to work; a 20-delta put is a CDS that forgot to wear one. Every slice is priced off the same risk-neutral law of $V_T$, so the volatility surface of one slice is a forecast of the spread of another. This chapter builds that translation layer.

### The Merton identity: equity vol is leveraged asset vol

Recall the setup from Chapter 6. Under $\mathbb{P}$ firm assets follow $dV_t = \mu V_t\,dt + \sigma_V V_t\,dW_t$; under $\mathbb{Q}$ the drift is $r$. Debt is a single zero-coupon claim of face $F$ due at $T$, so $E_T = (V_T - F)^+$ and

$$
E_0 = V_0 N(d_1) - F e^{-rT} N(d_2), \qquad d_{1,2} = \frac{\ln(V_0/F) + (r \pm \tfrac12\sigma_V^2)T}{\sigma_V\sqrt{T}} .
$$

Here $N(\cdot)$ is the standard normal CDF. Equity is a smooth function $E(V,t)$, so Itô's lemma gives

$$
dE_t = \frac{\partial E}{\partial V}\,dV_t + \Big(\frac{\partial E}{\partial t} + \tfrac12 \sigma_V^2 V_t^2 \frac{\partial^2 E}{\partial V^2}\Big)dt .
$$

Only the first term carries a $dW_t$, and its coefficient is $\frac{\partial E}{\partial V}\sigma_V V_t$. Writing the equity dynamics as $dE_t = (\cdot)\,dt + \sigma_E E_t\,dW_t$ and matching diffusion coefficients, with the call delta $\partial E/\partial V = N(d_1)$:

$$
\sigma_E E = \sigma_V V N(d_1) \quad\Longleftrightarrow\quad \sigma_E = \sigma_V \cdot \underbrace{\frac{V\,N(d_1)}{E}}_{\Omega\ \ge\ 1} . \tag{23.1}
$$

The identity holds under either measure, because Girsanov changes drifts and leaves volatilities alone. The factor $\Omega$ is the elasticity of a call with respect to its underlying, which is at least 1, so equity vol is asset vol times a leverage multiplier. Bohn and Stein write the same identity as $\sigma_E E = \sigma_A A\,\partial E/\partial A$ and build the KMV-style iteration on it (Bohn_Stein_Active_Credit_Portfolio_Management p.169).

The model debt is $B_0 = V_0 - E_0 = F e^{-rT}N(d_2) + V_0 N(-d_1)$, so the model credit spread, continuously compounded, is

$$
s^{\text{M}}(T) = -\frac{1}{T}\ln\!\Big[N(d_2) + \frac{V_0}{F e^{-rT}}N(-d_1)\Big]. \tag{23.2}
$$

Three consequences matter on the desk.

**Consequence 1: cheap stocks are mechanically high-vol stocks.** Hold asset vol fixed at 25%, set $F = 70$, $T = 1$, $r = 3\%$, and slide assets down *(illustrative)*:

| Assets $V$ | Equity $E$ | $N(d_1)$ | Equity vol $\sigma_E$ |
| :-- | :-- | :-- | :-- |
| 150 | 82.1 | 0.999 | 46% |
| 100 | 32.6 | 0.953 | 73% |
| 75 | 11.2 | 0.699 | 117% |

Nothing about the business got riskier. Asset vol never moved. Equity vol went from 46% to 117% because the equity cushion got thinner. This is why a vol-targeting overlay shorts distressed equity at exactly the wrong time: it reads leverage as risk appetite.

**Consequence 2: the skew is built in.** The elasticity of a call falls as the call moves into the money, so $\partial \sigma_E/\partial E < 0$ with $\sigma_V$ constant. Equity vol rises as the stock falls, which is a negative skew in the option surface before anyone has said "crash risk" or "jumps." Section 23.4 adds a jump to default, which steepens the low-strike wing far beyond what leverage alone produces.

**Consequence 3: the inverse problem.** Observe $(E_0, \sigma_E)$ from the market, solve (23.1) and the call-price equation jointly for $(V_0, \sigma_V)$, and read off (23.2). That is the equity-implied spread. The classic error is to skip the inversion and plug $\sigma_E$ in as $\sigma_V$, which overstates default probability by roughly a factor of leverage. The second classic error is ROBO's from the cold open, which we will autopsy in the spec.

> **[SOURCE EXTRACTION]** *Dynkin_Systematic_Investing_in_Credit p.93:* "In the Merton model (1974), a corporate bond is a short put on the underlying asset plus a risk‐free asset, while the company's stock is a call option on the underlying asset. The short put on the underlying asset also can be decomposed into a stock (call) plus a short straddle (a call and put at‐the‐money (ATM)) position on the underlying asset."
>
> **Annotation.** This is the sentence to tape above the cross-asset screen. If a bond is a Treasury plus some stock plus a short straddle on firm assets, then a long-credit book is short volatility, and it should earn the variance risk premium that option sellers earn; Dynkin's team tests exactly that and finds the bond-over-equity-replication return loads on the equity VRP. Two desk consequences follow. First, "bonds beat risk-matched equity" is partly a short-vol carry, so it will lose in vol spikes, which is when your equity hedge also misbehaves. Second, a capital-structure trade that is long the bond and short the stock is *not* flat vol: you have hedged the delta and kept the short straddle. Where the 2026 desk departs from the 1974 picture is that we no longer pretend the straddle is on a single lognormal asset; we read it off the listed surface strike by strike.

> **Desk Myth vs. Desk Reality.** *Myth:* Equity and credit are different markets with different investors, so their prices can disagree indefinitely and that is nobody's problem. *Reality:* They are different strikes on the same distribution, so a disagreement is a trade. The catch, which we will spend Section 23.6 on, is that at daily and weekly horizons the two markets are only weakly integrated (Kapadia and Pu, 2012), so the trade converges on the portfolio's schedule, not yours.

## 23.2 From Equity Vol to a Spread: CreditGrades in Production

Merton is the right picture and the wrong production model. It needs a single debt maturity, it puts default only at $T$, and short-dated spreads in it go to zero for any firm not already insolvent, which is not what the CDS market says. In May 2002 RiskMetrics Group, working with Goldman Sachs, JPMorgan, and Deutsche Bank, published the *CreditGrades Technical Document* (Finger, Finkelstein, Lardy, Pan, Ta and Tierney, 2002): a first-passage barrier model whose inputs are the stock price, an equity volatility, debt per share, and three constants. You can calibrate it before the coffee is ready, and two decades later it is still the default equity-to-credit bridge on many desks.

**Notation, renamed.** CreditGrades writes $S$ for the stock (we use $S_t$, as in the market-making chapters), $D$ for debt per share (we use $F^{\text{ps}}$, since $D$ is duration in this book), $\bar L$ for the mean global recovery (we use $\bar\ell$, since $L = 1-R$ is loss given default), and $\lambda$ for the dispersion of the barrier (we use $\nu$, since $\lambda$ is reserved for the hazard rate). Survival is written $\mathcal{S}(t) = \mathbb{Q}(\tau > t)$ in calligraphic type in this chapter, because the stock price $S_t$ is on every line.

### The model

Assets per share follow a driftless lognormal, $V_t = V_0 e^{\sigma_V W_t - \sigma_V^2 t/2}$ (the document argues on p.11 that zero drift relative to the barrier is the right compromise). Default is the first time assets touch the barrier $\ell F^{\text{ps}}$, where the global recovery fraction $\ell$ is itself uncertain:

$$
\ell = \bar\ell\, e^{\nu Z - \nu^2/2}, \qquad Z \sim N(0,1) \text{ independent of } W .
$$

The barrier uncertainty is the whole trick. A known barrier with continuous asset paths gives zero short-dated spreads; an uncertain barrier means you might already be closer to it than you think.

**Step 1 (rewrite the default event).** Default by $t$ means $V_0 e^{\sigma_V W_s - \sigma_V^2 s/2} \le \bar\ell F^{\text{ps}} e^{\nu Z - \nu^2/2}$ for some $s \le t$. Take logs and move everything random to the left:

$$
X_s := \sigma_V W_s - \nu Z - \tfrac12\sigma_V^2 s - \tfrac12 \nu^2 \;\le\; \ln\frac{\bar\ell F^{\text{ps}}}{V_0} - \nu^2 =: y .
$$

**Step 2 (the approximation).** $X_s$ is Gaussian with mean $-\tfrac12\sigma_V^2(s + \xi)$ and variance $\sigma_V^2(s + \xi)$, where $\xi = \nu^2/\sigma_V^2$. Those are exactly the moments of a Brownian motion with drift $a = -\tfrac12\sigma_V^2$ and volatility $b = \sigma_V$ that *started at time $-\xi$*. CreditGrades replaces $X$ by that process. In the document's words, the approximation "replaces the uncertainty in the default barrier with an uncertainty in the level of the asset value at time 0."

**Step 3 (reflection principle).** For $Y_u = a u + b W_u$ started at zero and a barrier $y < 0$,

$$
\mathbb{Q}\Big\{\min_{v \le u} Y_v > y\Big\} = N\!\Big(\frac{a u - y}{b\sqrt{u}}\Big) - e^{2 a y / b^2}\, N\!\Big(\frac{a u + y}{b\sqrt{u}}\Big).
$$

**Step 4 (substitute).** Set $u = t + \xi$, so $b\sqrt{u} = \sqrt{\sigma_V^2 t + \nu^2} =: \Sigma_t$ and $a u = -\Sigma_t^2/2$. Define $d = V_0 e^{\nu^2}/(\bar\ell F^{\text{ps}})$, so $y = -\ln d$ and $e^{2ay/b^2} = e^{-y} = d$. Then

$$
\mathcal{S}(t) = N\!\Big(-\frac{\Sigma_t}{2} + \frac{\ln d}{\Sigma_t}\Big) - d\, N\!\Big(-\frac{\Sigma_t}{2} - \frac{\ln d}{\Sigma_t}\Big), \qquad \Sigma_t^2 = \sigma_V^2 t + \nu^2 . \tag{23.3}
$$

This is the document's equation (2.11) in our notation. Boundary check: as $\nu \to 0$ it collapses to the standard first-passage survival of a driftless lognormal against a known barrier; as $t \to \infty$ it goes to zero; and at $t = 0$, $\Sigma_0 = \nu > 0$ and $\mathcal{S}(0) < 1$. That last fact is not a typo. The time shift puts probability mass on "already defaulted at inception," and the document itself flags the "counterintuitive result that there is a non-zero probability of default at t = 0."

**Step 5 (calibration).** CreditGrades links the unobservable $(V_0, \sigma_V)$ to the stock through $\sigma_E = \sigma_V \frac{V}{S}\frac{\partial S}{\partial V}$, the same identity as (23.1). Far from default, $S \approx V - \bar\ell F^{\text{ps}}$ and $\partial S/\partial V \approx 1$; the document shows (pp.10–11) that the choice

$$
V_0 = S_0 + \bar\ell F^{\text{ps}}, \qquad \sigma_V = \sigma_E\,\frac{S_0}{S_0 + \bar\ell F^{\text{ps}}} \tag{23.4}
$$

satisfies both the near-default and far-from-default boundary conditions. Read (23.4) backwards and you have Section 23.1's leverage skew in one line: for fixed $\sigma_V$, $\sigma_E = \sigma_V (S_0 + \bar\ell F^{\text{ps}})/S_0$ rises as $S_0$ falls. The document says it plainly: "This dependence of equity volatility on the stock price is evident in a pronounced volatility skew in equity option markets, especially for high yield names" (Finger et al., 2002, p.11).

**Step 6 (the CDS spread).** With constant $r$ and instrument recovery $R$, the par spread equates the premium leg (an annuity paid while alive) and the protection leg (loss paid at default, including the time-zero mass):

$$
s^{\text{CG}}(T) = \frac{(1-R)\Big[1 - \mathcal{S}(0) + \int_0^T e^{-ru}\,\big(-d\mathcal{S}(u)\big)\Big]}{\int_0^T e^{-ru}\,\mathcal{S}(u)\,du} . \tag{23.5}
$$

The document gives a closed form for (23.5) built on Rubinstein and Reiner's barrier integrals. We integrate (23.5) numerically on a monthly grid instead, for a reason in the next box.

**Parameters and empirics.** The document's defaults are $\bar\ell = 0.5$ and $\nu = 0.3$, the latter estimated from roughly 300 U.S. non-financial defaults over 1987–1997, with the note that "a lower λ is expected for the financial sector" (their $\lambda$ is our $\nu$). Debt per share includes financial debt, capital leases, under-funded pensions, and preferreds, and excludes payables and deferred taxes. On 6,194 CDS quotes for 122 U.S. firms through August 2001, the implied asset volatility was "quite stable," and "a simple measure of volatility based on the last 1000 days of equity returns produces good estimates of the volatility implied by the 5-year CDS quotes," with 88% within 10%. The document also tests at-the-money implied vol of the longest listed tenor. Kaz's instinct is to use one-month implied vol because it is "the market's view." It is the market's view of the next month, and you are pricing a five-year claim.

> **Ways This Blows Up.** *The time-zero ghost.* For a healthy name the mass $1 - \mathcal{S}(0)$ is negligible (about $10^{-4}$ for $S_0 = 30$, $\sigma_E = 40\%$, $F^{\text{ps}} = 30$). For a stressed name with $S_0 = 5$ and the same debt, it is about 25%: the model says a quarter of the default probability happened before you finished reading the screen, which inflates short-tenor spreads and makes the curve too flat. *The published closed form.* A later paper in the *Journal of Credit Risk* by Kiesel and Veraart has been reported to identify an error in the document's closed-form spread; we have not verified the details, so the reference engine integrates (23.5) directly and checks (23.3) against Monte Carlo. *Financials.* $\nu = 0.3$ was fitted on non-financials, and debt per share for a bank is mostly deposits, at which point the model is pricing a run with a diffusion (Section 23.8). *Two recoveries.* $\bar\ell$ is the global recovery that sets the barrier; $R$ is the recovery on the CDS reference obligation. Setting them equal by habit is a silent error. *The inversion floor.* Implied asset vol from a CDS quote is well posed only if the quote sits above the spread the model produces at near-zero vol; below that floor there is no answer, and the solver should say so rather than return its bracket endpoint.

> **Trend Watch.** *The equity-implied PD moved onto the systematic desk.* In 2002 CreditGrades was a dealer-consortium product sold as a screen. The academic evidence then hardened: Cremers, Driessen, Maenhout and Weinbaum (2008, *Journal of Banking & Finance*) found that option-implied volatility beats historical volatility in explaining both the cross-section and the time series of corporate spreads, with the level mattering most and the skew "to a lesser extent"; Zhang, Zhou and Zhu (2009, *Review of Financial Studies*) found that high-frequency equity volatility alone explains 48% of the variation in CDS levels, jump risk alone 19%, and 73% with ratings, macro and balance-sheet controls. By the 2020s, equity-market inputs were ordinary features in systematic credit engines: Blackstone describes a default-probability model that uses "real-time equity market signals" (Blackstone_Systematic_Credit p.1), and BlackRock's PD model uses "market data of equity and bond instruments" (BlackRock_Systematic_High_Yield_Credit p.6). *What it means:* the equity-implied spread is no longer an edge by itself; it is a baseline feature, and the edge is knowing when it is wrong (Sections 23.6 and 23.8).

### Specification for AI Implementation

**The Spec You Hand the Robot (what ROBO built from the vague version).** Asked to "compute the equity-implied CDS spread," ROBO used one-month at-the-money implied vol as asset vol, treated deposits as equity, and reported SVB Financial Group at 12bp on March 8, 2023. Every one of those choices was permitted by the sentence it was given. The precise version follows.

**Schemas.**

- `EquityState`: `S0: float` (last trade, \$ per share), `sigma_E: float` (annualized decimal, tagged `"hist1000d"` or `"atm_impl_longest"`), `q: float` (dividend yield), `shares_out: float`.
- `DebtPerShare`: `F_ps: float` (\$ per share) with components `{financial_debt, capital_leases, pension_deficit, preferred}` and an `asof` date. Deposits are **not** a component; banks route to the Section 23.8 engine.
- `CGParams`: `ell_bar = 0.5`, `nu = 0.3` (flag any override; financials require an explicit override and a reason), `R: float` (reference-obligation recovery), `r: float` (continuous, decimal).
- `CDSQuote`: `tenor_years`, `par_spread_bp` or (`upfront_pct`, `coupon_bp`), `recovery`, `curve_date`.

**Guards.** Raise on `S0 <= 0`, `sigma_E <= 0`, or `F_ps <= 0` (no debt, no CDS). Clip $d_{1,2}$ to $\pm 40$ before `norm.cdf`; compute $d\,N(\cdot)$ in (23.3) through `norm.logcdf` so large $d$ does not overflow. Times in years (ACT/365), spreads decimal internally and bp only in printouts. Return `nan` from the implied-vol inverter outside the model's range. The code blocks in this chapter run in order in one interpreter.

```python
import numpy as np
import pandas as pd
from scipy.stats import norm
from scipy.optimize import brentq, fsolve, least_squares

RNG_SEED = 23

# ---------- Merton (1974): the identity behind the whole chapter ----------
def merton_equity(V, F, r, sigma_V, T):
    """Equity as a call on assets. Returns (E, d1, d2)."""
    srt = sigma_V * np.sqrt(T)
    d1 = np.clip((np.log(V / F) + (r + 0.5 * sigma_V**2) * T) / srt, -40, 40)
    d2 = d1 - srt
    E = V * norm.cdf(d1) - F * np.exp(-r * T) * norm.cdf(d2)
    return E, d1, d2

def merton_equity_vol(V, F, r, sigma_V, T):
    """Eq. (23.1): sigma_E = sigma_V * V * N(d1) / E."""
    E, d1, _ = merton_equity(V, F, r, sigma_V, T)
    return sigma_V * V * norm.cdf(d1) / E

def merton_spread(V, F, r, sigma_V, T):
    """Eq. (23.2): model credit spread, decimal, continuously compounded."""
    _, d1, d2 = merton_equity(V, F, r, sigma_V, T)
    return -np.log(norm.cdf(d2) + V / (F * np.exp(-r * T)) * norm.cdf(-d1)) / T

def merton_solve_V_sigma(E, sigma_E, F, r, T):
    """Invert (E, sigma_E) -> (V, sigma_V); same contract as the Chapter 6 solver."""
    def eqs(x):
        V, sV = np.exp(x[0]), np.exp(x[1])          # log-parametrized: stays positive
        Em, d1, _ = merton_equity(V, F, r, sV, T)
        return [Em / E - 1.0, sV * V * norm.cdf(d1) / (sigma_E * E) - 1.0]
    V0 = E + F * np.exp(-r * T)
    x0 = [np.log(V0), np.log(sigma_E * E / V0)]
    sol, info, ier, msg = fsolve(eqs, x0, full_output=True, xtol=1e-12)
    if ier != 1:
        raise RuntimeError(f"Merton inversion failed: {msg}")
    return float(np.exp(sol[0])), float(np.exp(sol[1]))

# ---------- CreditGrades (Finger et al. 2002) in book notation ----------
# CG's lambda (barrier dispersion) -> nu ; CG's L-bar -> ell_bar ; CG's D -> F_ps.
def cg_asset_state(S0, sigma_E, F_ps, ell_bar=0.5):
    """Eq. (23.4): V0 = S0 + ell_bar*F_ps and sigma_V = sigma_E*S0/V0."""
    S0 = np.asarray(S0, dtype=float)
    if np.any(S0 <= 0) or np.any(np.asarray(sigma_E) <= 0):
        raise ValueError("S0 and sigma_E must be positive")
    if np.any(np.asarray(F_ps) <= 0):
        raise ValueError("F_ps must be positive: no debt, no CDS, no chapter")
    V0 = S0 + ell_bar * F_ps
    return V0, sigma_E * S0 / V0

def cg_survival(t, S0, sigma_E, F_ps, ell_bar=0.5, nu=0.3):
    """Eq. (23.3): CreditGrades survival curve; broadcasts over t and S0."""
    t = np.asarray(t, dtype=float)
    V0, sigma_V = cg_asset_state(S0, sigma_E, F_ps, ell_bar)
    log_d = np.log(V0 / (ell_bar * F_ps)) + nu**2
    Sig = np.maximum(np.sqrt(sigma_V**2 * t + nu**2), 1e-12)
    first = norm.cdf(-Sig / 2 + log_d / Sig)
    second = np.exp(log_d + norm.logcdf(-Sig / 2 - log_d / Sig))    # d * N(.), in logs
    return first - second

def cg_cds_spread(T, S0, sigma_E, F_ps, R=0.4, r=0.03, ell_bar=0.5, nu=0.3, dt=1/12):
    """Eq. (23.5) by direct integration of both legs; includes CG's time-zero mass.
    S0 may be a scalar (returns float) or a 1-D array (returns array)."""
    S0_arr = np.atleast_1d(np.asarray(S0, dtype=float))[:, None]
    n = max(int(round(T / dt)), 1)
    t = np.linspace(0.0, T, n + 1)[None, :]
    surv = cg_survival(t, S0_arr, sigma_E, F_ps, ell_bar, nu)
    h = np.diff(t, axis=1)
    rpv01 = np.sum(h * np.exp(-r * t[:, 1:]) * 0.5 * (surv[:, :-1] + surv[:, 1:]), axis=1)
    t_mid = 0.5 * (t[:, :-1] + t[:, 1:])
    prot = (1 - R) * ((1 - surv[:, 0])
                      + np.sum(np.exp(-r * t_mid) * (surv[:, :-1] - surv[:, 1:]), axis=1))
    s = prot / rpv01
    return float(s[0]) if np.ndim(S0) == 0 else s

def cg_implied_vol(spread_mkt, T, S0, F_ps, R=0.4, r=0.03, ell_bar=0.5, nu=0.3, lo=0.02, hi=5.0):
    """Invert a market CDS spread for (sigma_E, sigma_V); (nan, nan) outside the model's range."""
    f = lambda v: cg_cds_spread(T, S0, v, F_ps, R, r, ell_bar, nu) - spread_mkt
    if f(lo) > 0 or f(hi) < 0:
        return np.nan, np.nan            # below the low-vol floor, or beyond any vol
    sE = brentq(f, lo, hi, xtol=1e-12)
    return sE, sE * S0 / (S0 + ell_bar * F_ps)

def cg_survival_mc(t, S0, sigma_E, F_ps, ell_bar=0.5, nu=0.3,
                   n_paths=100_000, steps_per_year=252, seed=RNG_SEED):
    """Monte Carlo of the time-shifted Brownian motion that Eq. (23.3) is exact for,
    with a Brownian-bridge correction for barrier touches between grid dates."""
    rng = np.random.default_rng(seed)
    V0, sigma_V = cg_asset_state(S0, sigma_E, F_ps, ell_bar)
    V0, sigma_V = float(V0), float(sigma_V)
    xi = nu**2 / sigma_V**2                         # process 'started' at time -xi
    y = np.log(ell_bar * F_ps / V0) - nu**2         # barrier for X (negative)
    a, b = -0.5 * sigma_V**2, sigma_V
    horizon = t + xi
    n = int(np.ceil(horizon * steps_per_year))
    dt = horizon / n
    x = np.zeros(n_paths)
    alive = np.ones(n_paths, dtype=bool)
    for _ in range(n):
        x_new = x + a * dt + b * np.sqrt(dt) * rng.standard_normal(n_paths)
        gap0, gap1 = np.maximum(x - y, 0.0), np.maximum(x_new - y, 0.0)
        p_touch = np.exp(-2.0 * gap0 * gap1 / (b * b * dt))
        alive &= ~((x_new <= y) | (rng.random(n_paths) < p_touch))
        x = x_new
    p = alive.mean()
    return p, np.sqrt(p * (1 - p) / n_paths)

# ---------- sanity checks, block 1 ----------
# (a0) Merton round trip, and the leverage skew of Eq. (23.1)
V_true, sV_true, F_m, r_m, T1 = 100.0, 0.25, 70.0, 0.03, 1.0
E0, _, _ = merton_equity(V_true, F_m, r_m, sV_true, T1)
sE0 = merton_equity_vol(V_true, F_m, r_m, sV_true, T1)
V_hat, sV_hat = merton_solve_V_sigma(float(E0), float(sE0), F_m, r_m, T1)
assert abs(V_hat - V_true) < 1e-5 and abs(sV_hat - sV_true) < 1e-6
V_grid = np.array([75.0, 100.0, 150.0])
sig_E_grid = np.array([merton_equity_vol(v, F_m, r_m, sV_true, T1) for v in V_grid])
assert np.all(np.diff(sig_E_grid) < 0), "equity vol must fall as assets (and the stock) rise"
print("Merton sigma_E at V = 75, 100, 150:", np.round(sig_E_grid, 3))
print("Merton 1y spread at V = 100 (bp):", round(1e4 * float(merton_spread(V_true, F_m, r_m, sV_true, T1)), 1))

# (a) CG survival is non-increasing, and Eq. (23.3) matches Monte Carlo of its own process
S_ex, sE_ex, F_ex = 30.0, 0.40, 30.0
surv_curve = cg_survival(np.linspace(0.01, 10.0, 400), S_ex, sE_ex, F_ex)
assert np.all(np.diff(surv_curve) <= 1e-14)
p_cf = float(cg_survival(2.0, S_ex, sE_ex, F_ex))
p_mc, se_mc = cg_survival_mc(2.0, S_ex, sE_ex, F_ex)
assert abs(p_cf - p_mc) < 4 * se_mc, (p_cf, p_mc, se_mc)
print(f"CG 2y survival: closed form {p_cf:.5f}, MC {p_mc:.5f} +/- {se_mc:.5f}  PASS")
print("time-zero ghost 1 - S(0):  S0=30 ->", round(1 - float(cg_survival(0.0, 30.0, 0.4, 30.0)), 6),
      "  S0=5 ->", round(1 - float(cg_survival(0.0, 5.0, 0.4, 30.0)), 3))

# (b) leg integration vs. the average hazard (R = ell_bar, r = 0, a safer name)
T5 = 5.0
s_b = cg_cds_spread(T5, 50.0, 0.30, 30.0, R=0.5, r=0.0)
h_bar = -np.log(float(cg_survival(T5, 50.0, 0.30, 30.0))) / T5
assert abs(s_b / ((1 - 0.5) * h_bar) - 1) < 0.05

# (b2) the implied-vol inverter round-trips, and refuses quotes below the floor
s_mkt = cg_cds_spread(T5, 30.0, 0.45, 30.0)
sE_imp, sV_imp = cg_implied_vol(s_mkt, T5, 30.0, 30.0)
assert abs(sE_imp - 0.45) < 1e-6
assert np.isnan(cg_implied_vol(1e-6, T5, 30.0, 30.0)[0])
print(f"5y CG spread at sigma_E = 45%: {1e4 * s_mkt:.0f}bp; implied asset vol {sV_imp:.3f}  PASS")
```

The Monte Carlo check is deliberately honest about what it verifies: it simulates the time-shifted Brownian motion for which (23.3) is exact, so agreement tests the algebra and the code, not the approximation. If you simulate the "true" model instead, a lognormal against a barrier drawn once at time zero, you get a different time-zero mass, and the difference is the price of a closed form. Exercise 2 asks you to measure it.

## 23.3 Puts vs. CDS: Carr–Wu and the Default Corridor

Ines has a line she uses on every new hire who arrives from a restructuring shop: "The put is the CDS that forgot to tell anyone." She means it literally. For most of the names an ex-RSSG analyst knows best, the single-name CDS is either untraded or traded by four people who all know each other; by one 2025 count of cleared volumes, single names were on the order of 6% of index notional *(approx.)*. The listed put chain, meanwhile, is on OPRA, prints all day, and quotes strikes down to a few dollars. If you can turn a put spread into a default claim, you have a tradable single-name credit instrument for names where none exists.

Carr and Wu (2011, *Review of Financial Studies* 24(2), 473–505) showed that you can, under one assumption and no model.

**The claim to be priced.** The *unit recovery claim* pays \$1 at default if default happens before $T$:

$$
U(t,T) = \mathbb{E}^{\mathbb{Q}}_t\Big[e^{-r(\tau - t)}\,\mathbf{1}_{\{\tau \le T\}}\Big].
$$

**The assumption (the default corridor).** There are levels $0 \le A < B$ such that the stock stays above $B$ before default and below $A$ from default onward. The stock never trades inside $[A, B]$. That is the whole assumption; nothing is said about volatility, jumps above $B$, or dynamics after default.

**The result.** For co-terminal American puts $P^{\text{Am}}(K)$ with expiry $T$,

$$
U(t,T) = \frac{P^{\text{Am}}(B) - P^{\text{Am}}(A)}{B - A}, \qquad \text{and with } A = 0:\quad U(t,T) = \frac{P^{\text{Am}}(B)}{B}. \tag{23.6}
$$

**Proof.** Hold one put struck at $B$ long and one struck at $A$ short. *Before default*, $S_t > B > A$, so both puts are out of the money; nobody exercises an out-of-the-money put early, and if there is no default by $T$ both expire worthless. *At default*, $S_\tau < A$ and both are in the money. Exercising both immediately pays $(B - S_\tau) - (A - S_\tau) = B - A$, so the spread is worth at least $B - A$ at $\tau$. No-arbitrage also caps an American put spread at the strike difference, so it is worth at most $B - A$. Pinned from both sides, the spread is worth exactly $B - A$ at $\tau$ and zero if $\tau > T$, which is $(B - A)$ unit recovery claims. $\square$

The proof never mentions a diffusion, a hazard, or a recovery rate. It needs only that the stock jumps through the corridor, which is how equity behaves when a firm files: SVB's stock fell about 60% on March 9, 2023 and was halted on March 10. It fails for slow bleeds. GM drifted from 2005 to 2009 through every corridor you could have drawn, which is a hint that the corridor is a statement about *how* a name defaults, and an ex-RSSG analyst usually has a view on that.

**The CDS side.** With a flat hazard $\lambda$ and recovery $R$, the credit triangle gives $s = \lambda(1 - R)$, and the same claim implied by CDS is

$$
U^{\text{CDS}}(T) = \int_0^T e^{-ru}\,\lambda e^{-\lambda u}\,du = \frac{\lambda}{r + \lambda}\Big(1 - e^{-(r+\lambda)T}\Big), \qquad \lambda = \frac{s}{1-R}. \tag{23.7}
$$

For a European put the payment comes at $T$ instead of at $\tau$, so the matching claim is $e^{-rT}(1 - e^{-\lambda T})$. With $\lambda = 5\%$, $r = 3\%$ and $T = 1$ the two are 0.0481 and 0.0473 *(illustrative)*; mixing them is a 7bp-of-URC error, which is the time value of getting your recovery at default rather than at expiry. For standard-coupon CDS, use the bootstrapped hazard curve from Chapter 24 rather than the triangle.

**The signal.** Define the basis in claim units, $\text{basis}_U = U^{\text{opt}} - U^{\text{CDS}}$, and convert it back into spread units by inverting (23.7). When the put spread is cheap to CDS, buy the put spread and sell CDS protection, sized so the default payoffs match: $n(B - A) = (1 - R)\times\text{CDS notional}$. The position is default-neutral by construction; what is left is a pre-default MTM spread between two markets with different investors, which is the trade.

Cruz López and Ibáñez (2021, *Quarterly Journal of Finance*) show a European version under endogenous default, with a corridor that forms at cash-outflow dates, and a moral that RSSG people will enjoy: "no equityholders' fresh money, no endogenous corridor." Whether the corridor exists depends on whether equity will fund the next coupon, which is a negotiation, not a parameter.

> **[SOURCE EXTRACTION]** *Schmid_Credit_Risk_Pricing_Models p.154:* "at least as expensive as the corresponding default swap premium"
>
> **Annotation.** Schmid's context is credit spread options: a spread option that can be exercised on default carries the default payoff inside it, so its price is bounded below by the matching default-swap premium. The same dominance logic is what drives Carr–Wu. Any instrument that pays at least the default leg in every default state cannot be cheaper than the default leg; the put spread pays *exactly* the default leg and nothing else, so it is priced at it. On a 2026 desk the bound is a screening rule: if a listed put spread with $B$ comfortably below the post-default trading level is offered *below* the CDS-implied claim, either the corridor is wrong (a slow-bleed name), the borrow is distorting the chain, or someone is selling you default protection too cheaply. Check those three in that order.

> **Poker Table.** *Who is lifting your puts?* Ines, on the hand history: "In single-name low-strike puts, the bid side is a crowd and the offer side is a person." Low-delta puts are where informed flow goes when it cannot get into the CDS, because the options are listed, small, and anonymous. Around earnings, a missed coupon, or a liability-management rumor, the markouts on puts you sold are the worst on the sheet. Replay the hand: you sold 20-delta puts at a vol that looked rich by your skew model; two days later the company announced a drop-down financing and the puts were worth five times what you sold them for. The skew was not rich. Your model did not know the credit agreement had a basket for it, and the buyer did. Chapter 13's Priming Risk Score belongs in your put-quoting engine, not just in your bond book.

## 23.4 Skew as Jump-to-Default

Section 23.1 produced a skew from leverage. Real high-yield surfaces have a low-strike wing far steeper than leverage alone can make, and the cleanest explanation is that the stock can jump to zero. Write the simplest model that says so: Merton's (1976) jump-diffusion with one possible jump, to zero, at a constant risk-neutral hazard $\lambda$. Under $\mathbb{Q}$,

$$
\frac{dS_t}{S_{t^-}} = (r - q + \lambda)\,dt + \sigma\,dW_t - dN_t, \qquad N_t \sim \text{Poisson}(\lambda),
$$

where $q$ is the dividend yield and $\sigma$ is the pre-default diffusive volatility. The extra drift $\lambda$ compensates the jump, so that $e^{-(r-q)t}S_t$ is a $\mathbb{Q}$-martingale: alive stocks must grow faster to pay for the dead ones. This is the pre-default dynamics of Carr and Wu (2010) with constant hazard and no stochastic volatility.

**Step 1 (condition on survival).** If $\tau > T$, $S_T = S_0 \exp\{(r - q + \lambda - \tfrac12\sigma^2)T + \sigma W_T\}$; if $\tau \le T$, $S_T = 0$. A call pays only on survival, so

$$
C = e^{-rT}e^{-\lambda T}\,\mathbb{E}\big[(S_T - K)^+ \mid \tau > T\big] = S_0 e^{-qT}N(d_1) - K e^{-(r+\lambda)T}N(d_2),
$$

$$
d_{1,2} = \frac{\ln(S_0/K) + (r - q + \lambda \pm \tfrac12\sigma^2)T}{\sigma\sqrt{T}} .
$$

This is Black–Scholes with the discount rate on the strike bumped by the hazard. Credit spreads, it turns out, were hiding in the risk-free rate the whole time.

**Step 2 (put–call parity).** Parity holds because the forward is unchanged, $P = C - S_0 e^{-qT} + K e^{-rT}$, so

$$
P^{\text{JTD}}(K) = K e^{-rT}\Big[1 - e^{-\lambda T}N(d_2)\Big] - S_0 e^{-qT}N(-d_1) \;\xrightarrow{\;K \to 0\;}\; K e^{-rT}\big(1 - e^{-\lambda T}\big). \tag{23.8}
$$

As $K \to 0$, $d_2 \to \infty$ and $N(-d_1)$ vanishes faster than $K$, leaving a floor *linear in the strike*. Three readings follow.

1. **The floor is the hazard.** $P(K)/K \to e^{-rT}(1 - e^{-\lambda T}) \approx \lambda T e^{-rT}$, which is exactly the European unit recovery claim of Section 23.3 with $A = 0$. The skew model and the corridor theorem agree, and the code checks it to four decimals. With $\lambda = 5\%$ a \$5-strike put on a \$100 stock costs about 24 cents; Black–Scholes at 30% vol prices it at about $10^{-11}$ dollars. Black–Scholes prices it at a rounding error; the market prices it at a hazard rate.
2. **The wing must blow up.** A pure diffusion cannot produce a positive floor in $P(K)/K$, so the Black–Scholes implied vol that matches (23.8) must go to infinity as $K \to 0$. With $\sigma = 30\%$, $\lambda = 5\%$, $T = 1$, the implied vol is roughly 36% at the money, 41% at 80% moneyness, 52% at 60%, 72% at 40%, and about 100% at 20% *(illustrative; the code prints the exact values)*. That steep left wing is the signature of every HY name's surface.
3. **The skew's term structure is a hazard term structure.** The floor grows like $\lambda T$, so the low-strike wing at each expiry gives a point on the cumulative default curve. Fit expiry by expiry and you have a hazard term structure from the equity surface, ready to set beside the CDS curve.

**Telling jumps from stochastic volatility.** Stochastic-vol skew and jump-to-default skew both steepen the wing, so do not diagnose from the implied-vol picture. Use the price ratio: under stochastic volatility $P(K)/K \to 0$ as $K \to 0$; under jump-to-default it flattens to a positive constant. The `floor_ratio` diagnostic in the spec is that test.

**Making the hazard depend on the stock.** A constant $\lambda$ is a first draft. Convertible-bond models use $\lambda(S) = \lambda_0 (S_0/S)^p$, so the hazard rises as the stock falls (Andersen and Buffum, 2003, for convertibles); Linetsky (2006) derives closed forms for a CEV diffusion with this kind of default. Carr and Wu (2010, *Journal of Financial Econometrics*) estimate a joint model with stochastic volatility and a Cox default arrival on eight firms rated from B to AAA, jointly fitting options and CDS. The $p > 0$ version is the one to use when the name is near the fulcrum, because the market's hazard is not constant when the equity cushion is the thing being negotiated.

> **Ways This Blows Up.** *One strike, one lambda.* Fitting $\lambda$ from a single low strike turns bid–ask noise into hazard noise; at 5–10 delta the spread can be half the premium. Fit across strikes and expiries with bid and ask as bounds, not mid as truth. *Borrow masquerading as default.* In hard-to-borrow names puts are the synthetic short, so low-strike puts are rich because borrow is expensive, not because default is likely. Back the borrow fee out of at-the-money parity first and put it in $q$. *American exercise.* Listed single-stock puts are American. At default the holder exercises at once, so the American floor is $K\,\frac{\lambda}{r+\lambda}(1 - e^{-(r+\lambda)T})$, not the European $K e^{-rT}(1 - e^{-\lambda T})$. The engine tags every chain with its convention and refuses to compare across them. *Dividends.* A name about to cut its dividend has a forward that is about to jump, and the low strikes know it before the board does.

### Specification for AI Implementation (continued): the put-surface engine

**Schema.** `OptionChain` is a pandas DataFrame with columns `T` (years, ACT/365), `K` (\$), `cp` (`"P"` or `"C"`), `bid`, `ask` (\$ per share), and `american` (bool), plus optional `open_interest`. Pivoting by expiry gives bid and ask tensors of shape `(n_expiries, n_strikes)`, kept separate. Interpolate missing strikes linearly in *price*, never in vol, and never extrapolate outside the listed strikes. Every unit recovery claim carries a `convention` tag (`"at_default"` for American, `"at_expiry"` for European), and comparisons across conventions raise an error.

```python
# ---------- block 2: Carr-Wu claims and the jump-to-default put ----------
def bs_put(S0, K, T, r, q, sigma):
    """Textbook Black-Scholes put (independent reference for the lam = 0 check)."""
    d1 = (np.log(S0 / K) + (r - q + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return K * np.exp(-r * T) * norm.cdf(-d2) - S0 * np.exp(-q * T) * norm.cdf(-d1)

def jtd_put_price(S0, K, T, r, q, sigma, lam):
    """Eq. (23.8): European put when the stock diffuses at sigma and jumps to zero at rate lam (Q)."""
    K = np.asarray(K, dtype=float)
    srt = sigma * np.sqrt(T)
    d1 = np.clip((np.log(S0 / K) + (r - q + lam + 0.5 * sigma**2) * T) / srt, -40, 40)
    d2 = d1 - srt
    pays_K = -np.expm1(-lam * T) + np.exp(-lam * T) * norm.cdf(-d2)   # = 1 - e^{-lam T} N(d2), stably
    return K * np.exp(-r * T) * pays_K - S0 * np.exp(-q * T) * norm.cdf(-d1)

def bs_implied_vol_put(price, S0, K, T, r, q):
    return brentq(lambda v: float(bs_put(S0, K, T, r, q, v)) - price, 1e-4, 5.0, xtol=1e-12)

def make_put_chain(S0, strikes, T, r, q, sigma, lam, half_spread=0.0, american=False):
    mid = jtd_put_price(S0, strikes, T, r, q, sigma, lam)
    return pd.DataFrame({"T": T, "K": np.asarray(strikes, dtype=float), "cp": "P",
                         "bid": mid * (1 - half_spread), "ask": mid * (1 + half_spread),
                         "american": american})

def urc_from_puts(chain, T, A, B):
    """Eq. (23.6): unit recovery claim from a put spread struck inside the default corridor.
    Returns (U_bid, U_ask, convention)."""
    puts = chain[(chain["cp"] == "P") & np.isclose(chain["T"], T)].sort_values("K")
    if puts.empty:
        raise ValueError("no puts at this expiry")
    K = puts["K"].to_numpy()
    if not (0.0 <= A < B) or B > K.max() or (A > 0 and A < K.min()):
        raise ValueError("need 0 <= A < B inside the listed strikes; never extrapolate")
    bid = lambda k: float(np.interp(k, K, puts["bid"].to_numpy()))
    ask = lambda k: float(np.interp(k, K, puts["ask"].to_numpy()))
    if A == 0.0:
        U_bid, U_ask = bid(B) / B, ask(B) / B
    else:
        U_bid = (bid(B) - ask(A)) / (B - A)      # sell the spread: hit B's bid, lift A's offer
        U_ask = (ask(B) - bid(A)) / (B - A)
    convention = "at_default" if bool(puts["american"].all()) else "at_expiry"
    return U_bid, U_ask, convention

def urc_from_cds(spread, R, r, T, payment="at_default"):
    """Eq. (23.7): the same claim implied by a flat-hazard CDS (lam = s / (1 - R))."""
    lam = spread / (1.0 - R)
    if payment == "at_default":
        return lam / (r + lam) * (-np.expm1(-(r + lam) * T))
    if payment == "at_expiry":
        return np.exp(-r * T) * (-np.expm1(-lam * T))
    raise ValueError("payment must be 'at_default' or 'at_expiry'")

def jtd_fit(chain, S0, T, r, q, x0=(0.3, 0.02)):
    """Fit (sigma, lam) jointly on mid P(K)/K: low strikes pin lam, the money pins sigma."""
    puts = chain[(chain["cp"] == "P") & np.isclose(chain["T"], T)]
    K = puts["K"].to_numpy()
    mid = (0.5 * (puts["bid"] + puts["ask"])).to_numpy()
    resid = lambda x: jtd_put_price(S0, K, T, r, q, x[0], x[1]) / K - mid / K
    fit = least_squares(resid, x0, bounds=([1e-3, 0.0], [3.0, 3.0]),
                        xtol=1e-12, ftol=1e-12, gtol=1e-12)
    sig_hat, lam_hat = fit.x
    i_min = int(np.argmin(K))
    floor_ratio = ((mid[i_min] / K[i_min]) / (np.exp(-r * T) * -np.expm1(-lam_hat * T))
                   if lam_hat > 0 else np.inf)
    return {"sigma": float(sig_hat), "lam": float(lam_hat), "floor_ratio": float(floor_ratio)}

# ---------- sanity checks, block 2 ----------
S0p, Tp, rp, qp = 100.0, 1.0, 0.03, 0.0
lam_true, sig_true, R_cds = 0.05, 0.30, 0.40
# (c) lam = 0 is Black-Scholes; the deep-OTM floor is the hazard
assert abs(float(jtd_put_price(100.0, 90.0, 1.0, 0.03, 0.01, 0.3, 0.0))
           - float(bs_put(100.0, 90.0, 1.0, 0.03, 0.01, 0.3))) < 1e-10
K_low = 0.05 * S0p
floor = float(jtd_put_price(S0p, K_low, Tp, rp, qp, sig_true, lam_true)) / K_low
assert abs(floor / (np.exp(-rp * Tp) * -np.expm1(-lam_true * Tp)) - 1) < 0.01
# the skew: Black-Scholes implied vol of jump-to-default prices falls with strike
K_skew = np.array([20.0, 40.0, 60.0, 80.0, 100.0])
iv = np.array([bs_implied_vol_put(float(jtd_put_price(S0p, k, Tp, rp, qp, sig_true, lam_true)),
                                  S0p, k, Tp, rp, qp) for k in K_skew])
assert np.all(np.diff(iv) < 0)
print("JTD implied vols by strike:", dict(zip(K_skew.tolist(), np.round(iv, 3).tolist())))
# (d) Carr-Wu on a synthetic European chain equals the CDS claim with matching payment timing
strikes = np.arange(10.0, 155.0, 5.0)
chain = make_put_chain(S0p, strikes, Tp, rp, qp, sig_true, lam_true)
U_bid, U_ask, conv = urc_from_puts(chain, Tp, 0.0, 0.2 * S0p)
U_cds = urc_from_cds(lam_true * (1 - R_cds), R_cds, rp, Tp, payment=conv)
assert conv == "at_expiry" and abs(0.5 * (U_bid + U_ask) - U_cds) < 5e-5
gap = urc_from_cds(lam_true * (1 - R_cds), R_cds, rp, Tp, "at_default") - U_cds
print(f"URC from puts {U_bid:.5f}, from CDS {U_cds:.5f}; American-minus-European {gap:.5f}  PASS")
# the fit recovers the hazard; a pure diffusion has no floor
chain2 = make_put_chain(S0p, strikes, Tp, rp, 0.01, 0.35, 0.08)
fit = jtd_fit(chain2, S0p, Tp, rp, 0.01)
assert abs(fit["lam"] - 0.08) < 1e-4 and abs(fit["sigma"] - 0.35) < 1e-4
assert abs(fit["floor_ratio"] - 1) < 0.01
assert float(bs_put(S0p, 10.0, Tp, rp, qp, 0.35)) / 10.0 < 1e-6
print(f"fitted lam {fit['lam']:.4f}, sigma {fit['sigma']:.4f}, floor ratio {fit['floor_ratio']:.4f}  PASS")
```

## 23.5 Greeks in Spread Terms: Natenberg for the Credit Desk

An options trader runs a book on four numbers: delta, gamma, vega, theta. A credit trader runs a book on CS01 and a feeling. This section gives the feeling a Greek letter.

**Bonds.** Expand a bond's price in its spread, holding rates fixed:

$$
\frac{dP}{P} \approx -D^{\text{spr}}\,ds + \tfrac12 C^{\text{spr}}\,ds^2, \qquad \text{CS01} = D^{\text{spr}}\,P \times 10^{-4}. \tag{23.9}
$$

This is the duration–convexity identity with the yield replaced by the spread (Veronesi_Fixed_Income_Securities p.152 gives the rate version). Now write $ds = s\,(ds/s)$:

$$
\frac{dP}{P} \approx -\underbrace{D^{\text{spr}} s}_{\text{DTS}} \cdot \frac{ds}{s} .
$$

DTS is the exposure to *relative* spread changes, and relative spread volatility is roughly stable across spread levels, which is why DTS behaves like a vega-scaled delta. Ben Dor's team makes the point that spread volatility itself is unobservable and estimates it by maximum likelihood with $\sigma_t(s) = \alpha + \beta s_{t-1} + \gamma \hat{s}^2_{t-1}$ (Ben_Dor_Quantitative_Credit_Portfolio_Management p.70). Credit had no implied vol to read, so it built one out of a regression. Section 23.6 shows that it now has a listed one.

**CDS.** Bought protection with running coupon $c$, marked at market spread $s$, is worth per unit notional

$$
\text{MTM}^{\text{buy}}(s) = (s - c)\,\text{RPV01}(s), \qquad \text{RPV01}(s) \approx \frac{1 - e^{-(r+\lambda)T}}{r + \lambda}, \quad \lambda = \frac{s}{1-R}.
$$

Differentiating, the spread delta is $\text{RPV01} + (s - c)\,\text{RPV01}'$, which equals RPV01 at inception. The spread gamma at $s = c$ is $2\,\text{RPV01}'(c) < 0$, because a wider spread means a shorter expected premium stream. So bought protection is *short* spread convexity, and the bondholder, who is long credit, is long it.

Kaz once spent an afternoon arguing with Ines over whether long protection is long or short gamma. They were both right, in different coordinates. In *spread* space bought protection is short convexity; in *stock* space it behaves like a long put, because the model spread is a convex, decreasing function of the stock. Which gamma you report depends on which risk you hedge with: CDX if you hedge in spread, stock if you hedge in equity. A cross-asset book reports both and labels them.

**The Natenberg map.**

| Options Greek | Credit translation | What hedges it |
| :-- | :-- | :-- |
| Delta | CS01 (spread space) or shares per notional (stock space) | Index CDS; the stock |
| Gamma | Spread convexity; stock-space convexity of the model spread | Options on CDX; listed puts |
| Vega | Sensitivity to $\sigma_V$ through the model spread; CDX swaption vega | Swaptions; the equity surface |
| Theta | Carry plus roll-down | Nothing; it is why you are there |
| Jump | JTD: $(1-R)$ per unit notional, minus the hedge's jump | Put spreads (23.6); not the stock |

**Equity Greeks of a credit instrument.** Use the chain rule through firm value. In Merton, $\partial B/\partial V = N(-d_1)$ and $\partial E/\partial V = N(d_1)$, so $\partial B/\partial S = N(-d_1)/N(d_1)$ and the elasticity hedge ratio is

$$
h = \frac{\partial B / B}{\partial E / E} = \frac{N(-d_1)}{N(d_1)} \cdot \frac{E}{B}. \tag{23.10}
$$

For the illustrative firm of Section 23.1 ($V = 100$, $F = 70$), $h \approx 0.024$: a 1% stock move is a 2.4bp bond move. For a stressed firm $N(d_1)$ falls, $E/B$ falls, and the ratio of the two decides; the elasticity rises sharply as the name approaches the fulcrum, which is when bonds start trading like equity. In CreditGrades the corresponding "delta" is, in the document's words, the "number of shares of the equity required to offset small price moves" of a CDS position (Finger et al., 2002, p.14); its gamma rises as the stock falls, and its asset vega converts to equity vega through (23.4), $\partial/\partial\sigma_V = (V_0/S_0)\,\partial/\partial\sigma_E$.

**JTD: the Greek that is not a derivative.** At default the stock falls to roughly nothing, so a protection buyer hedged with $\delta$ long shares collects $(1 - R)N$ on the CDS and loses about $\delta S_{\tau^-}$ on the stock. For \$10mm notional at a \$30 stock, the CreditGrades delta is on the order of 20,000–25,000 shares, roughly \$0.7mm of stock *(illustrative)*, against a \$6mm protection payout at 40% recovery. Delta hedging a CDS with stock leaves almost all of the jump on the table. That is not a flaw in the hedge; it is the reason the stock is the wrong instrument for JTD. The stock hedges delta, the put spread of (23.6) hedges the jump, and a complete capital-structure book holds both.

> **[SOURCE EXTRACTION]** *Dynkin_Systematic_Investing_in_Credit p.87:* "Research has shown that analytical equity hedge ratios based on the Merton model make reasonably accurate predictions of how corporate bond returns vary given the corresponding equity returns (Schaefer and Strebulaev 2008)"
>
> **Annotation.** This is the most useful sentence about structural models ever written, because it separates the part that works from the part that doesn't. Schaefer and Strebulaev (2008, *Journal of Financial Economics*) find that Merton predicts spread *levels* badly but bond-to-equity *sensitivities* well, and Dynkin's team reports analytical hedge ratios only about 5% below empirical ones in both IG and HY. Capital-structure arbitrage is therefore a bet that the hedge ratio is right and the price is wrong, which is a coherent bet. The page that follows supplies the caveat: for high-equity, low-debt growth names (Dynkin's example is a Netflix-type HY issuer), the Merton ratio comes out far too low because "it uses the leverage ratio as one of the few inputs" (Dynkin_Systematic_Investing_in_Credit p.88). The 2026 fix is an empirical overlay: shrink the model hedge ratio toward a rolling regression elasticity, with the shrinkage weight a function of how far leverage is from the training sample.

> **Ways This Blows Up.** *The sign flip.* A long-bond, short-stock book assumes bonds and stock move together. On a liability-management rumor, or a takeover bid, the stock rallies while the excluded creditors' bonds drop, and you lose on both legs; Section 23.6's May 2005 autopsy is the canonical case. *Gamma near the barrier.* As the stock approaches the default region the CreditGrades delta changes fastest, so daily rebalancing turns into rebalancing every hour, at the bid–ask of a stock that is gapping. *Wrong duration.* Using modified duration where spread duration is needed (floaters, callables, loans) mislabels rate risk as credit risk, and the hedge ratio inherits the mistake.

### Specification for AI Implementation (continued): spread Greeks

```python
# ---------- block 3: Greeks in spread terms ----------
def cds_rpv01(s, R=0.4, r=0.03, T=5.0):
    lam = np.asarray(s, dtype=float) / (1.0 - R)
    return -np.expm1(-(r + lam) * T) / (r + lam)

def cds_mtm_buyer(s, c, R=0.4, r=0.03, T=5.0):
    """MTM per unit notional of bought protection, running coupon c, market spread s."""
    return (s - c) * cds_rpv01(s, R, r, T)

def bond_price_flat(s, cpn=0.06, T=5.0, r=0.03, freq=2):
    t = np.arange(1, int(round(T * freq)) + 1) / freq
    cf = np.full(t.shape, cpn / freq)
    cf[-1] += 1.0
    return float(np.sum(cf * np.exp(-(r + s) * t)))

def spread_greeks(price_fn, s, bump_bp=1.0):
    """Eq. (23.9) by central differences: spread duration, convexity, CS01, DTS."""
    h = bump_bp * 1e-4
    p0, pu, pd = price_fn(s), price_fn(s + h), price_fn(s - h)
    D = -(pu - pd) / (2 * h * p0)
    C = (pu - 2 * p0 + pd) / (h * h * p0)
    return {"price": p0, "D_spr": D, "convexity": C, "cs01": D * p0 * 1e-4, "dts": D * s}

def merton_elasticity(V, F, r, sigma_V, T):
    """Eq. (23.10): % bond move per % equity move."""
    E, d1, _ = merton_equity(V, F, r, sigma_V, T)
    return float(norm.cdf(-d1) / norm.cdf(d1) * E / (V - E))

def cg_greeks(S0, sigma_E, F_ps, R=0.4, r=0.03, T=5.0, ell_bar=0.5, nu=0.3, notional=1e7):
    """Greeks of BOUGHT protection per `notional`, coupon struck at today's model spread."""
    s0 = cg_cds_spread(T, S0, sigma_E, F_ps, R, r, ell_bar, nu)
    def mtm(S, sE=sigma_E):
        s = cg_cds_spread(T, S, sE, F_ps, R, r, ell_bar, nu)
        return notional * float(cds_mtm_buyer(s, s0, R, r, T))
    h = 0.01 * S0
    m0, mu, md = mtm(S0), mtm(S0 + h), mtm(S0 - h)
    vega_E = 0.5 * (mtm(S0, sigma_E + 0.01) - mtm(S0, sigma_E - 0.01))   # per 1 vol pt of sigma_E
    V0 = S0 + ell_bar * F_ps
    return {"spread_bp": 1e4 * s0,
            "delta_shares": -(mu - md) / (2 * h),   # shares to BUY against bought protection
            "gamma": (mu - 2 * m0 + md) / h**2,     # stock-space convexity, $ per $^2
            "vega_equity": vega_E,
            "vega_asset": vega_E * V0 / S0}         # per 1 vol pt of sigma_V, via Eq. (23.4)

# ---------- sanity checks, block 3 ----------
s_hy = 0.035
g = spread_greeks(lambda s: bond_price_flat(s), s_hy)
ds = 0.005
actual = bond_price_flat(s_hy + ds) / g["price"] - 1
approx = -g["D_spr"] * ds + 0.5 * g["convexity"] * ds**2
assert abs(actual - approx) < 2e-5, "duration-convexity should explain a 50bp move"
hs = 1e-4
gam_cds = (float(cds_mtm_buyer(0.03 + hs, 0.03)) - 2 * float(cds_mtm_buyer(0.03, 0.03))
           + float(cds_mtm_buyer(0.03 - hs, 0.03))) / hs**2
assert gam_cds < 0, "bought protection is short spread convexity"
el = merton_elasticity(100.0, 70.0, 0.03, 0.25, 1.0)
assert 0 < el < 1
gk30, gk15 = cg_greeks(30.0, 0.40, 30.0), cg_greeks(15.0, 0.40, 30.0)
assert gk15["delta_shares"] > gk30["delta_shares"] > 0, "hedge ratio rises as the stock falls"
print(f"bond D_spr {g['D_spr']:.3f}, DTS {g['dts']:.3f}; CDS spread gamma {gam_cds:.2f}; "
      f"Merton elasticity {el:.4f}")
print(f"CG per $10mm: S=30 -> {gk30['spread_bp']:.0f}bp, {gk30['delta_shares']:,.0f} sh; "
      f"S=15 -> {gk15['spread_bp']:.0f}bp, {gk15['delta_shares']:,.0f} sh  PASS")
```

## 23.6 Capital-Structure Arbitrage: Rules, Returns, and Why Single Trades Lose

Theo's first question about any cap-structure trade is "but what does the indenture say about the fulcrum?", and it is the right first question for a reason the model cannot see: the trade assumes the stock and the CDS are claims on the same value under the same rules. The second question is the model's: how far apart are they, and how fast do they come back together?

**The rule (Yu, 2006, adapted).** Compute the CreditGrades spread $s^{\text{CG}}_t$ from (23.3)–(23.5) using 1000-day or longest-tenor implied equity vol, and define the relative mispricing

$$
z_t = \frac{s^{\text{mkt}}_t - s^{\text{CG}}_t}{s^{\text{CG}}_t}. \tag{23.11}
$$

If $z_t > \alpha$, the market spread is rich to the equity: sell protection and short $\delta_t$ shares. If $z_t < -\alpha$: buy protection and buy $\delta_t$ shares. Here $\delta_t$ is the CreditGrades delta from Section 23.5, rebalanced daily, and Yu tests $\alpha \in \{0.5, 1, 2\}$. Exit on convergence ($|z_t| < \epsilon$), at a 180-day limit, or at a stop. Ex post, decompose the P&L as

$$
\Delta\Pi = \underbrace{-\,\text{RPV01}\cdot\Delta(s^{\text{mkt}} - s^{\text{CG}})}_{\text{convergence}} \;+\; \underbrace{c\,\Delta t}_{\text{carry}} \;+\; \underbrace{\tfrac12\Gamma_S\,(\Delta S)^2}_{\text{gamma}} \;+\; \underbrace{\text{JTD}\cdot\Delta N}_{\text{jump}} \;-\; \text{costs},
$$

for a protection seller, with signs flipped for a buyer. Only the first term is the thesis. "IDO or it didn't happen" applies here with force: carry is compensation for the jump term, and a backtest that books the carry and simulates no defaults has discovered that selling insurance is profitable in years without fires.

**What the evidence says.** Yu (2006, *Financial Analysts Journal*) runs the rule on 135,759 daily CDS spreads for 261 North American obligors over 2001–2004. Individual trades can lose heavily, because at short horizons CDS and equity are weakly correlated; an equally weighted portfolio of trades earns Sharpe ratios comparable to other fixed-income arbitrage strategies, and the speculative-grade monthly index has a Sharpe ratio of 0.75, uncorrelated with equity and bond factors. Kapadia and Pu (2012, *Journal of Financial Economics*) explain why: short-horizon pricing discrepancies are common, a significant fraction are anomalous rather than mean-reverting, and the degree of integration varies with frictions such as liquidity in both markets and idiosyncratic risk. Duarte, Longstaff and Yu (2007, *Review of Financial Studies*), asking whether fixed-income arbitrage is "nickels in front of a steamroller," find that strategies requiring more "intellectual capital," capital-structure arbitrage among them, earn significant alphas after factors and fees, with positively skewed returns. The single trade is a coin flip with a thesis attached; the portfolio is the edge.

> **Poker Table.** Ines: "A convergence trade is short a straddle on time." You are paid if the gap closes before your patience, your capital, or your risk manager runs out, and you lose if it widens first, which in this market is the more common short-horizon outcome. Size so that a 2x widening is a bad day, not a career event. Then replay the hand: on the trades that lost, did the gap widen because the model was wrong (a hedge ratio problem), because the market was wrong for longer (a capital problem), or because the rules changed (a credit-agreement problem)? Only the first is fixable with math.

### Case Study A: May 2005, GM and Ford, or How to Lose on Both Legs

**The setup.** By spring 2005 General Motors and Ford were investment-grade issuers drifting toward high yield, and GM was one of the largest names in both the convertible market and the CDS index tranches. Hedge funds held two popular structures on it. Convertible arbitrage: long GM convertibles, short GM stock, a trade "motivated by discrepancies between the price at which convertible bonds issued by GM were trading and the price of a replicating portfolio (consisting of regular bonds plus equity call options)" (BIS *Quarterly Review*, June 2005, p.6). Correlation: sell protection on the equity tranche of the iTraxx Europe index and buy index protection as a hedge, which "would have earned a spread of 300 to 400 basis points" and is "commonly referred to as a long correlation position" (ibid.).

**The timeline.**

| Date (2005) | Event | Equity | Credit |
| :-- | :-- | :-- | :-- |
| May 3 | Last trading day before Tracinda's announcement (Schedule 14D-9) | | |
| May 4 | Kirk Kerkorian's Tracinda offers to buy up to 28mm GM shares (about 4.95%) at \$31.00 cash; it already holds 22mm (about 3.89%) | GM up about 18% | |
| May 5 | S&P downgrades GM two notches to BB and Ford one notch to BB+ | Falls back | Bond and CDS spreads gap wider |
| May 9 | Tender offer commences; expires June 7 | | |
| June 1 | Both names leave the CDX and iTraxx indices at the roll | | |

**What broke.** The BIS put it in one sentence that every cap-structure desk should frame: investors "lost money on both legs of the trade: on 4 May GM's stock price increased by 18% after an offer from turnaround specialist Kirk Kerkorian to buy a large stake in the company, and then on 5 May the company's bond and CDS spreads increased after S&P's downgrade" (BIS *Quarterly Review*, June 2005, p.6). The short stock lost on the bid. The long credit lost on the downgrade. The correlation book lost separately: "Investors expecting default correlations to remain stable or increase were surprised in May when they instead fell sharply," and "at times in early May the two moved in opposite directions," meaning the mezzanine tranche and the index (ibid.). The BIS judged the episode "similar in nature, albeit certainly not in magnitude" to 1998. Convertible-arbitrage funds lost about 8% in early 2005, in what one later retrospective called "the worst environment since 1994" (Resonanz Capital, July 10, 2025). Specific fund-loss rumors at the time were denied and are not repeated here.

**Why the model could not see it.** Both legs were hedged against *the same* shock to firm value. May 4 and May 5 were two different shocks: a large shareholder bidding for equity (an equity-holder event that did nothing for creditors) and a ratings action with forced-selling consequences (a creditor event that did nothing for the bid). In Merton language, $\sigma_V$ did not change; the claim structure did, because a buyer of a control-sized equity stake and an index-eligibility cliff are not in the model. In RSSG language, Theo would have asked who benefits from Kerkorian's stake, and the answer, "not the bonds," is the hedge ratio flipping sign.

**How a systematic desk flags it now.** (1) *Event-sign stress:* shock the book to stock up 20% and spread up 30% at once, the May 2005 vector, and cap the loss. (2) *Fallen-angel cliff:* for issuers within a notch of high yield, model the forced-selling demand from index exits. GM and Ford were about 3% of the investment-grade bond market and potentially up to 15% of global high yield (BIS, June 2005), and index providers' average-of-three-ratings rule meant the exits were scheduled, not surprising. (3) *Concentration:* a single name that is simultaneously your largest convert hedge, a large tranche exposure, and an index constituent is one trade wearing three hats. (4) *Equity-event flags:* 13D filings, tender offers, and activist stakes route the name to a "hedge ratio unreliable" state in which the z-signal is suspended.

> **Trend Watch.** *Credit got its own volatility surface.* Until recently a credit desk inferred spread volatility from regressions (Section 23.5); now it can read it off a listed index. On October 13, 2023, Cboe launched four Credit VIX indices, VIXIG (CDX North America IG), VIXHY (CDX North America HY), VIXIE (iTraxx Europe Main) and VIXXO (iTraxx Crossover), built from CDX and iTraxx swaption prices using the VIX methodology and co-developed with S&P Dow Jones Indices (Cboe press release, October 3, 2023). The pre-launch back-test shows VIXHY rising from 240.09 to 394.15 between March 2 and March 20, 2023, during the bank failures (hypothetical back-tested data, per Cboe). Volumes followed: cleared CDX swaptions were about \$107bn in Q2 2025, up 103% year on year from \$52.8bn (ION/Clarus analysis of LSEG CCPView data, one scope; approx.), and ICE cleared a record \$19.3bn of index-option notional exercised on April 16, 2025, against a prior record of \$17.7bn on October 18, 2023. *What it means:* the cross-asset trade no longer has to be level against level. The desk can trade implied against implied, equity-surface hazard against CDX swaption vol, and hedge credit vega with an instrument rather than a hope.

### Specification for AI Implementation (continued): the cap-structure backtester

**What ROBO built from the vague version.** Told to "backtest capital-structure arbitrage," ROBO sold protection on every name, booked the carry, simulated no defaults, and reported a Sharpe ratio of 4. It was correct about the simulation it was given. The spec below strips carry from the convergence P&L, reports it separately, and states the noise model.

**Inputs.** `panel`: long DataFrame with `issuer`, `day`, `S`, `sigma_E`, `F_ps`, `s_model` (decimal, from CreditGrades), `ds_dS` (decimal per \$), `s_mkt`. Parameters: `alpha` (entry threshold on $z$), `eps` (exit), `hold_max_days = 180`, `cost_bp_cds` (running-spread equivalent, converted to upfront with RPV01), `cost_bp_eq` (bp of traded stock notional). Unit CDS notional per trade. Output: daily portfolio P&L, per-trade P&L, Sharpe, hit rate, and carry reported separately.

```python
# ---------- block 4: Yu-style capital-structure arbitrage on a synthetic panel ----------
def simulate_cg_panel(n_issuers=20, n_days=500, T=5.0, R=0.4, r=0.03, seed=RNG_SEED):
    """GBM equity paths (no defaults) and CreditGrades model spreads with stock-space slopes."""
    rng = np.random.default_rng(seed)
    dt = 1 / 252
    frames = []
    for i in range(n_issuers):
        S0, sE, F_ps = rng.uniform(15, 60), rng.uniform(0.25, 0.60), rng.uniform(10, 60)
        steps = -0.5 * sE**2 * dt + sE * np.sqrt(dt) * rng.standard_normal(n_days - 1)
        S = S0 * np.exp(np.concatenate([[0.0], np.cumsum(steps)]))
        s_mod = cg_cds_spread(T, S, sE, F_ps, R, r)
        ds_dS = (cg_cds_spread(T, 1.01 * S, sE, F_ps, R, r)
                 - cg_cds_spread(T, 0.99 * S, sE, F_ps, R, r)) / (0.02 * S)
        frames.append(pd.DataFrame({"issuer": i, "day": np.arange(n_days), "S": S, "sigma_E": sE,
                                    "F_ps": F_ps, "s_model": s_mod, "ds_dS": ds_dS}))
    return pd.concat(frames, ignore_index=True)

def add_market_noise(panel, phi, sd_u=0.30, seed=RNG_SEED):
    """s_mkt = s_model * exp(u), u an AR(1) with persistence phi and stationary sd sd_u."""
    rng = np.random.default_rng(seed)
    u_all = []
    for _, g in panel.groupby("issuer", sort=True):
        eta = rng.standard_normal(len(g))
        u = np.empty(len(g))
        u[0] = sd_u * eta[0]
        for t in range(1, len(g)):
            u[t] = phi * u[t - 1] + sd_u * np.sqrt(1 - phi**2) * eta[t]
        u_all.append(u)
    out = panel.copy()
    out["s_mkt"] = out["s_model"] * np.exp(np.concatenate(u_all))
    return out

def capstruct_backtest(panel, alpha=0.5, eps=0.1, hold_max_days=180,
                       cost_bp_cds=5.0, cost_bp_eq=10.0, R=0.4, r=0.03, T=5.0):
    """Eq. (23.11) rules. pos = +1 sold protection (short stock hedge), -1 bought (long stock)."""
    n_days = int(panel["day"].max()) + 1
    pnl, carry, trades = np.zeros(n_days), np.zeros(n_days), []
    for iss, g in panel.groupby("issuer", sort=True):
        S, sm, smod = g["S"].to_numpy(), g["s_mkt"].to_numpy(), g["s_model"].to_numpy()
        dsdS_mkt = g["ds_dS"].to_numpy() * sm / smod          # market-spread slope in the stock
        z = sm / smod - 1.0
        pos, c, hedge, mtm_prev, t0, trade_pnl = 0, 0.0, 0.0, 0.0, 0, 0.0
        for t in range(n_days):
            exited = False
            if pos != 0:
                rpv = float(cds_rpv01(sm[t], R, r, T))
                mtm = pos * (c - sm[t]) * rpv
                step = (mtm - mtm_prev) + hedge * (S[t] - S[t - 1])
                mtm_prev = mtm
                carry[t] += pos * c / 252                          # reported, not in pnl
                closing = abs(z[t]) < eps or (t - t0) >= hold_max_days or t == n_days - 1
                if closing:
                    step -= cost_bp_cds * 1e-4 * rpv + abs(hedge) * S[t] * cost_bp_eq * 1e-4
                else:
                    new_hedge = pos * rpv * dsdS_mkt[t]
                    step -= abs(new_hedge - hedge) * S[t] * cost_bp_eq * 1e-4
                    hedge = new_hedge
                pnl[t] += step
                trade_pnl += step
                if closing:
                    trades.append({"issuer": iss, "entry": t0, "exit": t, "side": pos, "pnl": trade_pnl})
                    pos, hedge, exited = 0, 0.0, True
            if pos == 0 and not exited and abs(z[t]) > alpha and t < n_days - 1:
                pos = 1 if z[t] > 0 else -1
                rpv = float(cds_rpv01(sm[t], R, r, T))
                c, mtm_prev, t0 = sm[t], 0.0, t
                hedge = pos * rpv * dsdS_mkt[t]
                entry_cost = cost_bp_cds * 1e-4 * rpv + abs(hedge) * S[t] * cost_bp_eq * 1e-4
                pnl[t] -= entry_cost
                trade_pnl = -entry_cost
    daily = pd.Series(pnl, name="pnl")
    sd = float(daily.std())
    tr = pd.DataFrame(trades)
    return {"sharpe": float(np.sqrt(252) * daily.mean() / sd) if sd > 0 else 0.0,
            "n_trades": len(tr),
            "hit_rate": float((tr["pnl"] > 0).mean()) if len(tr) else float("nan"),
            "carry_total": float(carry.sum()), "daily": daily, "trades": tr}

# ---------- sanity checks, block 4 ----------
# (e) a delta-hedged protection seller is not JTD-hedged: at default the short stock covers little
jtd_gap = -(1 - 0.4) * 1e7 + gk30["delta_shares"] * 30.0
assert jtd_gap < -0.7 * (1 - 0.4) * 1e7
print(f"JTD on $10mm sold protection, delta-hedged at S=30: {jtd_gap:,.0f} USD")
# (f) the Kapadia-Pu lesson: convergence Sharpe falls as mispricings become persistent
panel = simulate_cg_panel()
bt = {}
for phi in (0.90, 0.98, 0.995):
    bt[phi] = capstruct_backtest(add_market_noise(panel, phi))
    print(f"phi={phi}: Sharpe {bt[phi]['sharpe']:.2f}, trades {bt[phi]['n_trades']}, "
          f"hit rate {bt[phi]['hit_rate']:.2f}, carry (excluded) {bt[phi]['carry_total']:.3f}")
assert bt[0.90]["sharpe"] > 0
assert bt[0.90]["sharpe"] > bt[0.995]["sharpe"], "persistence should erode convergence Sharpe"
```

The Sharpe ratios this prints are large, and they are large because the only thing in the synthetic market is mean-reverting noise around a correct model. That is the point of the exercise and the reason not to put the number in a pitch book. The useful output is the *shape*: as the persistence $\phi$ of the mispricing rises toward one, the expected daily convergence per unit of noise scales like $\sqrt{(1-\phi)/(1+\phi)}$ and the Sharpe ratio decays toward zero. Kapadia and Pu's weak integration is a statement that real $\phi$ is high and varies by name.

## 23.7 Convertible Arbitrage: The Original Cap-Structure Trade

Mags has a word for every strategy that got a Greek letter after she was already doing it. "Back in my day we called it buying the bond and shorting the stock. We sized the short by phone and by grudge. Now it has a gamma." Then, grudgingly: "The gamma is better than the grudge."

> **[SOURCE EXTRACTION]** *Moyer_Distressed_Debt_Analysis p.260:* "The classic example of a capital structure arbitrage is a hedged convertible bond trade. A convertible arbitraguer that arranges a capital structure arbitrage, which is called "putting on the trade," will purchase the convertible bond and then sell short an appropriate amount of stock."
>
> **Annotation.** Moyer is writing from the distressed seat, where the point of the hedge is to "lock in" the coupon with little net capital, because the short-sale proceeds fund much of the convertible. That framing is still correct about the economics and silent about the risk. The modern decomposition is that a hedged convertible is long credit (the bond floor), long equity volatility (the embedded call, which the delta hedge turns into gamma), and short borrow (the stock loan). "An appropriate amount of stock" is the delta, which depends on the hazard, which depends on the stock: the $\lambda(S)$ of Section 23.4. In 2005 the credit leg broke; in 2008 the borrow leg broke as well. A 2026 desk reports the three legs separately and stresses them jointly.

**The P&L of a delta-hedged convertible.** Let $\text{CB}(S, t)$ be the convertible's value with a stock-dependent hazard, $\Delta = \partial\text{CB}/\partial S$ and $\Gamma = \partial^2\text{CB}/\partial S^2$. Over $dt$, long one bond and short $\Delta$ shares earns, before default,

$$
d\Pi \approx \tfrac12\,\Gamma\,S^2\big(\sigma_{\text{real}}^2 - \sigma_{\text{impl}}^2\big)\,dt \;+\; \big(\text{coupon} + \text{short rebate} - \text{borrow fee}\big)\,dt \;-\; \lambda(S)\,\text{JTD}\,dt ,
$$

where JTD is the loss at default net of the stock hedge's gain. The first term is the gamma trade, the second is carry, and the third is why the carry exists. Convert arb loses when realized vol undershoots implied while credit widens (2005), or when the borrow disappears and liquidity goes with it (2008, when emergency short-sale restrictions on financial stocks removed the hedge for part of the market).

**Case note: Wolfspeed, 2025, when the convertible is the fulcrum.** Wolfspeed's restructuring support agreement of June 22, 2025 was signed by holders of more than 97% of its senior secured notes, more than 67% of its convertible notes, and Renesas's U.S. subsidiary; the company filed a prepackaged Chapter 11 late in June 2025, targeting roughly \$4.6bn (about 70%) of debt reduction and about a 60% cut in annual cash interest, and the plan was reported effective on September 29, 2025 *(terms as reported; approx.)*. Under the reported terms the convertible holders took new notes and the bulk of the reorganized equity, shared with Renesas. For a convert-arb book, that is the trade's endgame inverted: the "bond floor" was not a floor, the convertible *was* the equity of the new company, and the short in the old stock was the profitable leg. The flags a systematic desk would watch in a name like this are the ones this chapter builds: convertibles trading below the straight-debt floor implied by the secured curve (the market pricing them as the fulcrum), a low-strike put floor in (23.8) implying a hazard far above the CDS-free model, and a CreditGrades $z$ that disagrees with the converts' price about how much option value the old equity will keep. We have not reconstructed those series for Wolfspeed; Exercise 5 asks you to.

> **Trend Watch.** *The convertible comeback.* After a lean 2022, the strategy and the market both revived. The HFRX Convertible Arbitrage index returned 10.1% in 2023, global issuance was about \$90bn that year (US about \$57bn), and issuers' effective cost through converts was roughly 3–4% against 7–9% in high yield over 2023–24, with short-sale rebates of 5% or more (Resonanz Capital, "Convertible Arbitrage: The 2023–2025 Comeback," July 10, 2025). Global issuance reached \$167.1bn across 264 deals in 2025, which Numerix called the strongest year on record, and 2026 issuance was reported at about \$131bn in the US through early September, about half from AI-linked issuers *(approx.; secondary reporting)*. *What it means:* the AI capex cycle is financing itself partly by selling volatility to convert-arb funds, so convertible supply is now a driver of single-name implied vol in the issuers' equity surfaces. If you trade those surfaces against CDS, the converts are a third leg you have to model.

## 23.8 When the Surface Lies: Banks, Runs, and Contractual Inversions

Everything so far assumes that default is a firm-value diffusion crossing a barrier, so that the equity surface and the credit curve are two views of one process. The surface lies exactly where that is false. There are three ways it fails, and an ex-RSSG analyst has an edge in all three, because in each one the contract or the run decides who gets paid, not the diffusion.

### Case Study B: SVB, March 8–10, 2023

**The facts.** On March 8, 2023, SVB Financial Group announced the balance-sheet restructuring from the cold open. In the Federal Reserve's words, "the bank faced a run by depositors on March 9. Deposit outflows were over \$40 billion on March 9, and management expected \$100 billion more" on March 10 (Federal Reserve, April 28, 2023). At year-end 2022, about 94% of deposits were uninsured, and the HTM portfolio had a weighted-average duration of 6.2 years. On March 10 the California Department of Financial Protection and Innovation closed Silicon Valley Bank and appointed the FDIC as receiver; at December 31, 2022 the bank had about \$209.0bn of assets and \$175.4bn of deposits (FDIC press release PR-23-016, March 10, 2023). The Fed's review notes that the stock had been "relatively stable" until March 8 "before deteriorating sharply," and that as of March 1 analysts had 12 Buy, 11 Hold, and 1 Sell ratings on it.

**The price path** *(approx.; secondary press reports of TRACE prints)*:

| Date (2023) | Equity | Holdco senior notes (cents) |
| :-- | :-- | :-- |
| Week of March 6 | Stable until the March 8 announcement | Mid-80s |
| March 9 | Down about 60% | 1.8% 2026s reportedly 115bp wider, to 241bp |
| March 10 | Halted; bank closed | About 37–42 at the close |
| March 13 | Delisted path; holdco equity effectively gone | About 47–50 after the deposit guarantee |
| March 17 | Holdco files Chapter 11 | About 60 by that week's end |

**Why the surface was wrong.** Three reasons, in increasing order of importance. First, the asset vol was wrong: Nagel and Purnanandam (2020, *Review of Financial Studies*) show that bank assets are themselves loans, short puts on borrowers' assets, so the bank's asset payoff is concave and its asset volatility *rises* after bad shocks; constant-volatility structural models "can seriously understate banks' default risk" in good times. Second, the leverage was wrong: for a bank, debt per share is mostly deposits, and ROBO's 12bp came from treating them as equity. Third, and decisively, the default event was wrong. SVB did not fail because $V_t$ crossed $F$; the HTM book was never marked to market before the closure. It failed because liquidity went negative:

$$
\text{default at } \tau = \inf\Big\{t : \text{outflows}_t > \text{cash}_t + \text{monetizable}_t\Big\}, \qquad \text{outflow rate}_t = \kappa\,\max(0, -r^E_t) + \rho\,\frac{D^{u}_0 - D^{u}_t}{D^{u}_0},
$$

where $D^u_t$ is uninsured deposits, $r^E_t$ is the equity return, and the second term is the panic feedback: depositors leave faster when other depositors have left. Equity vol in this model is an *output* of the run, not an input to it. A put surface that "makes no sense unless the stock is going to zero" was the only instrument pricing the run correctly.

Theo's 13-week cash flow model, which has followed him through this book on a USB stick, finally meets its natural habitat. A bank's default model *is* a liquidity runway: sources, uses, and the day the line crosses zero. For SVB the 13 weeks were two days.

> **[SOURCE EXTRACTION]** *Bohn_Stein_Active_Credit_Portfolio_Management p.198:* "the assumption that equity prices are only affected by changes in the firm's underlying asset value may lead an analyst astray when the equity price becomes overwhelmed by liquidity or market bubble issues or when the information that informs the prices (e.g., the value of inventories, etc.) is observed imperfectly by market participants."
>
> **Annotation.** Bohn and Stein wrote this about the 1987, 2007, and 2008 sell-offs, and recommended hybrid models that add non-asset-value factors. For banks in 2023 the warning applies in the opposite direction: the equity price was *not* overwhelmed by noise, it was the first market to process a liquidity fact (uninsured, concentrated, networked depositors) that the asset-value model had no state variable for. The modern desk's fix is the hybrid they describe, specialized: for financials, route the name out of CreditGrades entirely and into a liquidity model whose state includes the uninsured share, HTM unrealized losses relative to CET1, the duration gap, and deposit beta, and let the equity surface be a check on that model rather than its input.

> **Docket Diary.** *SVB Financial Group, Chapter 11, filed March 17, 2023 (S.D.N.Y.).* The holding company, no longer owning the bank, filed with \$3,279mm of senior notes outstanding across seven series, and about \$2bn of its cash in accounts at the FDIC's bridge bank, which the FDIC froze; an interim order later gave limited access. Bond prices around 60 cents in the following week said the market expected the holdco's creditors to recover a large fraction of par from cash and non-bank businesses, not from the bank. The Ad Hoc Group, represented by counsel, would like to note for the record that it would like its \$2bn back.

### Case Study C: Credit Suisse AT1, March 19, 2023

On March 19, 2023, FINMA ordered "a complete write-down of the nominal value of all AT1 debt of Credit Suisse in the amount of around CHF 16 billion," triggered by extraordinary government support, as UBS agreed to acquire the bank (FINMA press release, March 19, 2023). Shareholders received 1 UBS share per 22.48 Credit Suisse shares, CHF 0.76 per share, "a total consideration of CHF 3 billion" (UBS media release, March 19, 2023). A claim senior to equity received zero while equity received CHF 3bn. No Merton diagram, no CreditGrades barrier, and no Carr–Wu corridor produces that outcome, because all of them assume the waterfall is ordered by priority. The contract had a viability trigger, and the trigger reordered the waterfall.

> **Desk Myth vs. Desk Reality.** *Myth:* AT1 is senior to equity, so an AT1 trading below the equity-implied recovery is an arbitrage. *Reality:* AT1 is senior to equity in liquidation. Before liquidation, its write-down clause lets a regulator's viability determination zero it while the equity is sold for consideration. Kaz, reading the prospectus, asked whether "point of non-viability" was a topology term. It is a legal one, and it is a strike the regulator sets.

### Case Study D: Hertz, 2020–21, the Happy Inversion

Hertz filed for Chapter 11 on May 22, 2020, with an equity that every model said was worthless; in June 2020 it announced, and then shelved, a \$500mm at-the-money stock offering into a market that kept bidding for its shares. Used-car prices and a bidding war among plan sponsors then raised the value of the estate. The plan, confirmed June 10, 2021 and effective June 30, 2021, repaid the unsecured notes in full in cash, and gave existing shareholders 14,133,075 shares of new common, about 3% of 471,102,514, plus, for those not in the rights offering, 89,049,029 warrants exercisable until June 30, 2051 at an initial \$13.80 (Hertz Form 8-K filed July 7, 2021); secondary reporting adds about \$239mm of cash to old equity *(approx.)*. The sponsors (Knighthead, Certares, Apollo) put in \$2.781bn of new common, \$1.5bn of Apollo preferred, and a \$1.635bn backstopped rights offering. The equity was a call on enterprise value that finished in the money. The surface that priced Hertz equity above zero in bankruptcy was not irrational; it was long volatility on an estate whose value distribution had a fat right tail. Mags's verdict: "Recovery is what you get, eventually, after the lawyers. Sometimes the lawyers are on your side."

### Specification for AI Implementation (continued): the bank override

**Rule.** Any issuer with deposits above 50% of liabilities, or any instrument with a contractual write-down or conversion trigger, is routed out of the CreditGrades engine. Banks go to a liquidity-runway model; trigger instruments carry a `contractual_waterfall_override = True` flag, and the risk system refuses to net them against equity as if priority held. The code is purely illustrative: inputs are round numbers loosely scaled to a \$200bn bank, not SVB's balance sheet.

```python
# ---------- block 5: illustrative bank-run default vs. a Merton PD ----------
def bank_run_dd(cash, securities, haircut, max_monetize_per_day, uninsured, kappa, rho, equity_rets):
    """Liquidity default day under a run whose outflow rate rises with equity losses (kappa)
    and with cumulative outflows (rho, the panic feedback). All amounts in $bn; illustrative."""
    dep_u, liquid, sec = float(uninsured), float(cash), float(securities)
    path = []
    for day, ret in enumerate(equity_rets, start=1):
        rate = min(1.0, kappa * max(0.0, -ret) + rho * (1.0 - dep_u / uninsured))
        outflow = rate * dep_u
        raised = min(sec * (1.0 - haircut), max_monetize_per_day)
        sec -= raised / (1.0 - haircut)
        liquid += raised
        path.append({"day": day, "outflow": outflow, "liquidity": liquid})
        if outflow > liquid:
            return {"default_day": day, "path": pd.DataFrame(path)}
        liquid -= outflow
        dep_u -= outflow
    return {"default_day": None, "path": pd.DataFrame(path)}

run = bank_run_dd(cash=13.0, securities=115.0, haircut=0.10, max_monetize_per_day=30.0,
                  uninsured=165.0, kappa=0.42, rho=2.0, equity_rets=[-0.60, -0.30, -0.10])
_, _, d2_bank = merton_equity(212.0, 196.0, 0.03, 0.04, 1.0)
merton_pd_bank = float(norm.cdf(-d2_bank))
assert run["default_day"] == 2 and merton_pd_bank < 0.01
print(f"liquidity default on day {run['default_day']}; Merton 1y PD on the same bank {merton_pd_bank:.2%}")
print(run["path"].round(1).to_string(index=False))
```

## 23.9 Cross-Asset Trend: Does the Surface Lead the Spread?

The last use of the surface is as a clock. If equity and credit are two strikes on one distribution but different investors trade them at different speeds, the faster market leads. The evidence says equity usually does: Dynkin's team finds that each +1% per month of sector equity momentum predicts about +5–8bp of subsequent bond excess return, stronger in US high yield (Dynkin_Systematic_Investing_in_Credit p.644). The specification is a panel lead–lag regression,

$$
r^{\text{xs}}_{i,t+1} = a + b\,r^{E}_{i,t} + c\,\Delta\sigma^{\text{impl}}_{i,t} + d\,\Delta\widehat{\lambda}^{\text{put}}_{i,t} + \epsilon_{i,t+1},
$$

where $r^{\text{xs}}$ is bond excess return over duration-matched Treasuries, $r^E$ the equity return, $\Delta\sigma^{\text{impl}}$ the change in implied vol, and $\Delta\widehat\lambda^{\text{put}}$ the change in the put-floor hazard from (23.8). Use Chapter 10's overlapping-window corrections and Chapter 8's IDO residuals for the left side, or you will rediscover beta.

> **[SOURCE EXTRACTION]** *Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.25:* "equity performance often has a spillover into bond pricing."
>
> **Annotation.** Man's framing is the practical one: equity momentum in credit (the EMC factor of Ben Dor and co-authors, 2021) is a factor you can harvest because bond investors update slowly. The cross-asset surface sharpens it. Equity returns tell you the stock moved; the change in the put floor tells you whether the move was about the *tail*. A 10% stock drop with no change in the low-strike wing is a valuation event; a 10% drop with the wing doubling is a credit event that the bond market has not priced yet.

> **Trend Watch.** *Equity first, high yield second, private marks last (early 2026).* iCapital's February 6, 2026 *Market Pulse* dates the trigger to an AI product rollout by Anthropic on January 30, 2026: software stocks fell about 10% after it and were about 20% down year to date as of February 4, "the worst start to the year in history," with no software index member above its 200-day moving average. In credit, software high-yield spreads were about 400bp and technology about 340bp (iBoxx, February 4, 2026), against 264bp for broad high yield; software was about 20% of public BDC loans (LSEG/Bloomberg, September 30, 2025), and no loan-mark changes had been reported. *What it means:* this is the lead–lag in three speeds. Public equity repriced in days, public high yield in weeks, and private marks had not moved. For the desk, equity and put-surface signals are the earliest read on private-credit marks (Chapter 17), and the gap between them is a forecast of the next round of valuations.

## 23.10 Desk Debrief

- **The capital structure is one distribution sliced at different strikes.** Equity is the call, bonds are short puts, CDS is the put without rates, and a low-strike equity put is a CDS that forgot to tell anyone.
- **Equity vol is leveraged asset vol** ($\sigma_E E = \sigma_V V N(d_1)$). Cheap stocks are mechanically high-vol stocks, the skew is built in, and plugging $\sigma_E$ in for $\sigma_V$ overstates default risk by the leverage.
- **CreditGrades is the production bridge**, with honest warts: the time-zero ghost, a reported error in the published closed form, two different recoveries, and $\nu$ fitted on non-financials. Integrate the legs yourself and test against Monte Carlo.
- **A put spread inside the default corridor is a model-free default claim** (Carr–Wu). Match the payment convention (American pays at default, European at expiry) before you trade the basis against CDS.
- **The low-strike floor $P(K)/K$ is the hazard.** Jumps make it flatten to a constant; stochastic vol sends it to zero. Diagnose with prices, not implied vols.
- **Hedge ratios are the part of Merton that works.** Cap-structure arbitrage bets the ratio is right and the price is wrong; single trades lose, portfolios earn. Strip carry, simulate defaults, and stress the May 2005 vector (stock up, spread up).
- **The surface breaks where the process is not a diffusion:** runs (SVB), contractual triggers (Credit Suisse AT1), and estates whose value tail was fatter than anyone modeled (Hertz). The credit agreement, the prospectus, and the deposit base decide those cases, and reading them is the ex-RSSG analyst's edge.

**The Spec You Hand the Robot.** Build `ch23_cross_asset_surface`, numpy/scipy/pandas only, seeded RNG (`seed=23`), no network. (1) `cg_survival`, `cg_cds_spread`, `cg_implied_vol` per (23.3)–(23.5), with the leg integration monthly, the time-zero mass in the protection leg, `nan` outside the inversion range, and a Monte Carlo check with a Brownian-bridge correction. (2) `urc_from_puts` per (23.6), returning bid and ask bounds and a payment `convention`, and `urc_from_cds` per (23.7) with a matching `payment` argument; raise on convention mismatch. (3) `jtd_put_price` and `jtd_fit` per (23.8), fitting $(\sigma, \lambda)$ jointly on $P(K)/K$, with borrow backed out of at-the-money parity first and the `floor_ratio` diagnostic. (4) `spread_greeks` (CS01, convexity, DTS) and `cg_greeks` (shares per \$10mm, stock-space gamma, equity and asset vega), plus JTD per notional reported as its own line. (5) `capstruct_backtest` with Yu's rules, carry reported separately from convergence, defaults simulated at the CDS-implied hazard in production runs, and an event-sign stress (stock +20%, spread +30%). (6) A router that sends any issuer with deposits above 50% of liabilities to `bank_run_dd`, and flags any instrument with a contractual write-down trigger as `contractual_waterfall_override`. Inputs in decimals and years; outputs in bp, \$, and shares, with units in every column name. Every function raises on non-positive prices, vols, or debt.

### Exercises

1. **ROBO targets volatility.** ROBO is told to "keep each position at 10% annualized vol" and holds a stock whose asset vol is constant at 25%. Using (23.1) and the table in Section 23.1, compute how much ROBO sells as assets fall from 150 to 75. Explain in one sentence to the risk committee why the strategy is short the fulcrum.
2. **Chase the ghost.** Simulate the *true* CreditGrades model, a lognormal against a barrier drawn once at $t = 0$, and compare its $1 - \mathcal{S}(0)$ and 1- and 5-year spreads with (23.3) for $S_0 \in \{5, 30\}$, $\sigma_E = 40\%$, $F^{\text{ps}} = 30$. At what stock price does the time-shift approximation move the 1-year spread by more than 50bp?
3. **Trade the basis.** Given a European put chain generated by `jtd_put_price` with $\lambda = 6\%$ and a CDS quote of 250bp at 40% recovery, compute $\text{basis}_U$ in claim units and in bp, size a default-neutral put-spread-versus-CDS trade for \$10mm CDS notional, and explain what happens to it if the stock drifts slowly into the corridor, GM-style, instead of jumping through it.
4. **Kaz and the prospectus.** Kaz argues that an AT1 trading at 40 while the equity trades at a positive price is an arbitrage "because seniority." Write the `contractual_waterfall_override` logic, list the three prospectus fields it must parse, and show what CreditGrades would have said about Credit Suisse AT1 recovery on March 17, 2023 (use illustrative inputs and say so).
5. **Both legs, again.** Build a book that is long \$10mm of a convertible (approximated as a 5-year bond plus calls) and short delta in stock, plus \$10mm of sold CDS protection hedged with stock, on a \$30 name. Apply the May 2005 vector, stock +18% then spread +30%, using the block 3 Greeks, and decompose the loss by leg. Then reconstruct the convertible-floor, put-floor, and $z$ series a desk would have watched for Wolfspeed in the first half of 2025 from public data, and say which flag fired first.
6. **Three speeds.** Using the iCapital February 2026 figures, estimate the high-yield spread move per 10% of software equity drawdown, then state the private-mark markdown your lead–lag model would forecast for a software loan book at 97.8% of par, and the one assumption that would make your forecast wrong.

### Deep-Dive Resource Graph

**Podcasts**

- *Bloomberg Odd Lots* (Joe Weisenthal and Tracy Alloway): episodes on the March 2023 bank failures, on Credit Suisse AT1s, and on convertible bonds. Search the show archive by topic; episode numbers are not given here.
- *Flirting with Models* (Corey Hoffstein): conversations with volatility and convertible-arbitrage managers on carry, skew, and short-vol risk.

**Practitioner Writing**

- Matt Levine, *Money Stuff* (Bloomberg Opinion): the March 2023 columns on SVB's deposit run and on the Credit Suisse AT1 write-down, and his recurring explanations of capital-structure seniority.
- BIS *Quarterly Review*, June 2005, the overview and the box on the GM and Ford downgrades and CDS index tranches (pp.4–6).
- Board of Governors of the Federal Reserve System, *Review of the Federal Reserve's Supervision and Regulation of Silicon Valley Bank* (April 28, 2023). Root: https://www.federalreserve.gov
- FDIC press releases PR-23-016 (March 10, 2023, SVB) and PR-23-034 (May 1, 2023, First Republic). Root: https://www.fdic.gov
- FINMA press release and UBS media release, March 19, 2023, on Credit Suisse.
- Cboe press release, October 3, 2023, on the Credit VIX indices.
- Resonanz Capital, "Convertible Arbitrage: The 2023–2025 Comeback" (July 10, 2025); iCapital, "Market Pulse: Surveying the Software Space" (February 6, 2026).
- Finger, C. C. (ed.), V. Finkelstein, J.-P. Lardy, G. Pan, T. Ta, and J. Tierney (2002), *CreditGrades Technical Document*, RiskMetrics Group (hosted by MSCI).

**Academic Papers**

- Carr, P., and L. Wu (2011), "A Simple Robust Link Between American Puts and Credit Protection," *Review of Financial Studies* 24(2), 473–505. DOI 10.1093/rfs/hhq129.
- Carr, P., and L. Wu (2010), "Stock Options and Credit Default Swaps: A Joint Framework for Valuation and Estimation," *Journal of Financial Econometrics* 8(4), 409–449. DOI 10.1093/jjfinec/nbp010.
- Cruz López, J., and A. Ibáñez (2021), "European Puts, Credit Protection, and Endogenous Default," *Quarterly Journal of Finance* 11(1). DOI 10.1142/S2010139221500014.
- Yu, F. (2006), "How Profitable Is Capital Structure Arbitrage?" *Financial Analysts Journal* 62(5), 47–62. DOI 10.2469/faj.v62.n5.4282.
- Kapadia, N., and X. Pu (2012), "Limited Arbitrage between Equity and Credit Markets," *Journal of Financial Economics* 105(3), 542–564. DOI 10.1016/j.jfineco.2011.10.014.
- Duarte, J., F. A. Longstaff, and F. Yu (2007), "Risk and Return in Fixed-Income Arbitrage: Nickels in Front of a Steamroller?" *Review of Financial Studies* 20(3), 769–811. DOI 10.1093/rfs/hhl026.
- Schaefer, S. M., and I. A. Strebulaev (2008), "Structural Models of Credit Risk Are Useful: Evidence from Hedge Ratios on Corporate Bonds," *Journal of Financial Economics* 90(1), 1–19.
- Zhang, B. Y., H. Zhou, and H. Zhu (2009), "Explaining Credit Default Swap Spreads with the Equity Volatility and Jump Risks of Individual Firms," *Review of Financial Studies* 22(12), 5099–5131. DOI 10.1093/rfs/hhp004.
- Cremers, M., J. Driessen, P. Maenhout, and D. Weinbaum (2008), "Individual Stock-Option Prices and Credit Spreads," *Journal of Banking & Finance* 32(12), 2706–2715.
- Culp, C. L., Y. Nozawa, and P. Veronesi (2018), "Option-Based Credit Spreads," *American Economic Review* 108(2), 454–488. DOI 10.1257/aer.20151606.
- Nagel, S., and A. Purnanandam (2020), "Banks' Risk Dynamics and Distance to Default," *Review of Financial Studies* 33(6), 2421–2467. DOI 10.1093/rfs/hhz125.
- Collin-Dufresne, P., R. S. Goldstein, and F. Yang (2012), "On the Relative Pricing of Long-Maturity Index Options and Collateralized Debt Obligations," *Journal of Finance* 67(6), 1983–2014. DOI 10.1111/j.1540-6261.2012.01779.x.
- Linetsky, V. (2006), on pricing equity derivatives subject to bankruptcy in a CEV-with-default model; Andersen, L., and D. Buffum (2003), on calibrating and implementing convertible-bond models with stock-dependent hazard (titles not verified here).

**Data & Code**

- SEC EDGAR (Schedule 14D-9 and 13D filings for tender offers and activist stakes; Form 8-K for plan effectiveness): https://www.sec.gov/edgar
- CourtListener REST API, for Chapter 11 dockets such as SVB Financial Group (S.D.N.Y., 2023): https://www.courtlistener.com/help/api/
- FINRA TRACE, for corporate bond prints (price paths in Case Study B).
- OPRA consolidated options data, for listed put chains (the `OptionChain` schema).
- DTCC and clearing-house public CDS volume reports, and Cboe's Credit VIX index data, for the credit vol surface.
- Shelf cross-references: Dynkin_Systematic_Investing_in_Credit pp.87–88, 93, 644; Bohn_Stein_Active_Credit_Portfolio_Management pp.169, 198; Ben_Dor_Quantitative_Credit_Portfolio_Management p.70; Schmid_Credit_Risk_Pricing_Models p.154; Moyer_Distressed_Debt_Analysis p.260; Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.25.

<!-- STATUS: COMPLETE -->
