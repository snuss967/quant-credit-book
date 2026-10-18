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
