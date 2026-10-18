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
