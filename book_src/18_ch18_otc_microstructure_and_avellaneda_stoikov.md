# Chapter 18: OTC Credit Microstructure & the Market Maker's Equations

*11:52 a.m.* The RFQ arrived the way bad news always arrives on a credit desk: politely, in a grey box, with a countdown timer. *Client sells \$8mm Halvorsen Packaging 7.25% Senior Secured Notes due 2029 (a fictional issuer; B2/B), disclosed, five dealers in competition, three minutes to respond.* The composite said 91.25.

Kaz's auto-quoter had already filled in a bid of 90.875. "Avellaneda–Stoikov," Kaz said, with the calm of someone whose model has never been subpoenaed. "We're long three million already. Twenty-day realized vol, half-spread from the fitted win curve, rounded to the nearest eighth, because this market is a medieval guild."

Theo had the indenture open on his second monitor, because he always had a credit document open on his second monitor. "Their lender call is at noon," he said. "And the indenture lets them buy back notes below par through open market purchases, with no cap. If they announce a discounted repurchase at noon, today's sellers are the people who were told first."

"Is an open market purchase like open outcry?" Kaz asked. "Do they have to shout?"

"They have to pay less than you," Theo said.

"So the seller may know something," said Ines, without looking up. "What's the pot, what are the odds, and who at this table knows more than you?"

"The client," Theo said. "Maybe four of the five dealers. Definitely not the auto-quoter."

From across the row, Mags did not look up either. "Back in my day we'd just not pick up the phone."

Ines dragged the bid to 90.25 and sent it. It did not trade; someone covered at 90.50. Twenty minutes later the bond was 86 bid, and the chat windows filled with the noise a market makes when it finds out who the patsy was. On \$8mm, the winner had just bought a \$360,000 lesson *(illustrative)*.

Kaz stared at the screen. "The model was right about the inventory."

"The model was right about the part you asked it about," Ines said. "A quote is four things glued together. You priced one."

That is the question this chapter answers: *what is the right bid, and how much of it is fear, how much greed, how much suspicion, and how much the price of being asked again tomorrow?*

By the end of this chapter you will be able to: map Harris's trader taxonomy onto the credit ecosystem and say who is a forced seller to whom; estimate an effective spread from TRACE prints with Roll's trick, and know when the estimator is lying; derive Kyle's $\lambda$ and estimate it from markouts; derive the Avellaneda–Stoikov (AS) quotes from the Hamilton–Jacobi–Bellman (HJB) equation without skipping steps; solve the Guéant–Lehalle–Fernandez-Tapia (GLFT) inventory-bounded problem as a linear ODE system; extend both to jump-to-default; fit an RFQ win curve and price a hit-ratio target; decode a TRACE file into features; and model a BWIC as a first-price auction with a leaky list. You will also be able to hand all of it to ROBO in a spec that leaves it nothing to guess.

## 18.1 Harris's Zoo, Relabeled for Credit

A restructuring banker learns to ask *who holds the paper and what are they forced to do*. A market maker asks the same question, but at the speed of a timer and about everyone at once. Larry Harris's *Trading and Exchanges* (2003), the standard practitioner text on market microstructure, sorts traders by *why* they trade. **Utilitarian traders** trade for some reason other than profiting from the trade itself: hedging, investing cash, meeting a redemption, or obeying a regulator. **Profit-motivated traders** trade because they think the price is wrong or about to move. These include the *informed*, who know something about value; *order anticipators*, who know something about other people's orders; and *bluffers*, who want you to believe they know something. Between them stand the **dealers**, who sell immediacy, and the **arbitrageurs**, who sell convergence. Harris adds four dimensions of liquidity: **immediacy** (how fast you can trade), **width** (the cost of a round trip), **depth** (how much size you can do at that cost), and **resiliency** (how fast the price recovers after you trade).

Relabeled for the credit ecosystem of Chapter 1, the zoo looks like this.

| Harris type | Credit population (2026) | What they want | What they cost the dealer |
| :--- | :--- | :--- | :--- |
| Utilitarian, uninformed | Insurers selling fallen angels for capital reasons; index funds at month-end; CLOs curing CCC buckets; LDI-linked holders meeting margin calls | Immediacy at a fair price, predictably timed | Little in expectation. This is the dealer's bread. |
| Utilitarian, arbitrage | ETF authorized participants (Chapter 20); portfolio-trade desks (Chapter 19); CDS–bond basis traders | Convergence of a basket to its NAV | Basket risk and the mystery-box problem, but rarely issuer-level information |
| Profit-motivated, mostly uninformed about issuers | Systematic factor pods trading momentum, value, and carry baskets (Chapters 9–11) | Factor exposure | Factor beta, which the dealer can hedge. IDO or it didn't happen: their markouts are mostly not toxic once you strip the factor. |
| Profit-motivated, informed | Distressed and crossover funds; LMT participants; anyone who has actually read the indenture | To trade before the information is in the price | The residual markout, which is the whole adverse-selection problem |
| Order anticipators | Anyone who has seen a BWIC list, a leaked run, or a large RFQ shopped to too many dealers (§18.9) | To trade ahead of known flow | Pre-auction drift, paid by the seller |
| Dealers | Bank dealers; non-bank liquidity providers, about 10% of credit market-making revenue in 2024 *(approx.; industry dossier)* | Spread, and future flow | Competition. Non-banks bring a different $\gamma$ and a different $k$ (§18.4). |

Harris's four liquidity dimensions turn into the four things an RFQ engine must estimate before it answers anything. Immediacy is the *win probability* within the timer. Width is the *reservation spread* plus the markup. Depth is how the reservation price changes with *block size*, not just with one more lot. Resiliency is the *impact decay* after a print, which is the spring Paleologo describes for equities (Paleologo p.152–153). In bonds the spring is the dealer's own inventory, and it relaxes only when the dealer finds the other side. The rest of the chapter derives a model for each.

> **Desk Myth vs. Desk Reality.** *Myth:* "The bid–ask spread is the dealer's profit." *Reality:* The quoted spread is four charges, and only one of them is profit. **Fear** is the inventory risk premium, $\gamma\sigma^2(T-t)$ in §18.4. **Greed** is the markup a dealer with some pricing power can charge, $\tfrac{2}{\gamma}\ln(1+\gamma/k)$. **Suspicion** is the expected adverse markout, $2\pi\sigma_V$ in Glosten–Milgrom (§18.3). **Franchise** is a *negative* charge: the subsidy a dealer pays to keep winning enough RFQs to stay on the client's list (§18.7). Realized profit is the spread minus the markout. On a toxic RFQ it is negative, which is why "the dealer made the spread" is something only people who have never been a dealer say.

> **[SOURCE EXTRACTION]** *Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.19:* "the bond market is structured around a Request for Quotation (RFQ) process that has hardly changed for decades. Corporate bond bid/ask prices are indicated by dealer runs that are not firm and actionable"
>
> **Annotation.** Our analysis: the Man authors are right about the *protocol* and, by 2026, wrong about the *responder*. The disclosed RFQ is still a sealed-bid auction among a handful of dealers. What changed between 2022 and 2026 is who answers it. Trumid reported 88% of eligible RFQ line items executed with no human touch in September 2025, and Tradeweb's AiEX handled more than 40% of its institutional trades in 2025 (sources in Trend Watch, §18.7). The runs are still "not firm and actionable", which is why §18.2 has to recover spreads from prints rather than quotes. The same page also complains about "if filled" trades. That complaint is the reason the modern engine treats fill probability as a modeled variable rather than as noise: in §18.7 the win curve $P(x)$ is a first-class input to the quote, not an afterthought in the backtest.

## 18.2 Roll's Trick: Seeing the Spread When No One Will Show You One

Equities show you a spread. Credit shows you a *print*, fifteen minutes late, with the size capped and the side sometimes ambiguous, and asks you to infer the spread from it, like a sommelier asked to name the vintage from the cork. Roll (1984), "A Simple Implicit Measure of the Effective Bid-Ask Spread in an Efficient Market" (*Journal of Finance* 39(4)), found that the spread leaves a fingerprint in the *autocovariance* of price changes. A trade at the bid tends to be followed by a trade at the ask, so prices bounce, and the bounce is negatively autocorrelated.

### 18.2.1 Derivation

Let $m_t$ be the efficient mid, a random walk $m_t = m_{t-1} + \varepsilon_t$ with $\varepsilon_t$ i.i.d., mean zero, variance $\sigma_\varepsilon^2$. Let $I_t \in \{-1,+1\}$ indicate whether print $t$ was a customer sell (at the bid) or a customer buy (at the ask). Let $c = S/2$ be the effective half-spread in price points. The print is

$$
p_t = m_t + c\,I_t .
$$

Then $\Delta p_t = \varepsilon_t + c\,(I_t - I_{t-1})$. Assume first, as Roll did, that $I_t$ is i.i.d. with $\mathbb{P}(I_t = 1) = \tfrac12$, independent of $\varepsilon$. Then $\text{Var}(I_t) = 1$ and all cross-covariances vanish, so

$$
\text{Cov}(\Delta p_t, \Delta p_{t+1}) = c^2\,\text{Cov}(I_t - I_{t-1},\, I_{t+1} - I_t) = -c^2\,\text{Var}(I_t) = -\frac{S^2}{4}.
$$

Solving for the spread gives Roll's estimator:

$$
\widehat{S}^{\text{Roll}} = 2\sqrt{-\widehat{\text{Cov}}(\Delta p_t, \Delta p_{t+1})}.
$$

Bao, Pan & Wang (2011), "The Illiquidity of Corporate Bonds" (*Journal of Finance* 66(3)), use the same covariance directly as an illiquidity measure, $\gamma^{\text{BPW}} = -\text{Cov}(\Delta p_t,\Delta p_{t+1})$ computed on TRACE prices. They find bond illiquidity far larger than quoted spreads suggest, and priced in the cross-section. (Their $\gamma$ is not our risk aversion $\gamma$, hence the superscript.)

Now break the assumption the way credit breaks it. Large customer orders are *split*: a \$25mm sell goes out as five \$5mm RFQs over an afternoon. Model the trade signs as a symmetric two-state Markov chain with lag-one autocorrelation $\rho \in [0,1)$, so that $\text{Cov}(I_t, I_{t+j}) = \rho^{|j|}$. Expanding term by term,

$$
\text{Cov}(I_t - I_{t-1},\, I_{t+1} - I_t) = \rho - 1 - \rho^2 + \rho = -(1-\rho)^2,
$$

so $\text{Cov}(\Delta p_t,\Delta p_{t+1}) = -c^2(1-\rho)^2$ and

$$
\widehat{S}^{\text{Roll}} \;\to\; S\,(1-\rho).
$$

Order splitting makes Roll *underestimate* the spread by the factor $(1-\rho)$. Add informed flow that moves the mid in the direction of the trade over several prints, so that the $\varepsilon_t$ are positively autocorrelated, and the covariance can turn positive. The square root then has no real solution. That is not a numerical accident. It is the estimator telling you that the bounce has been overwhelmed by momentum, which is information in its own right (§18.3). Dynkin's team makes the same point from the other side when it uses return autocorrelation as an illiquidity proxy: investors split trades, which produces positive autocorrelation, and stale prices do the same (Dynkin p.771).

> **[SOURCE EXTRACTION]** *Ben_Dor_Quantitative_Credit_Portfolio_Management p.120:* "for most bonds the time between a broker-dealer buy and sell transaction for a given CUSIP can be very long, so it is difficult to calculate an accurate bid-ask spread using TRACE."
>
> **Annotation.** Our analysis: this is the practical objection to Roll in credit, and it bites harder than it looks. Roll's algebra assumes the mid barely moves between consecutive prints, so that $\sigma_\varepsilon^2$ is small next to $c^2$. When a dealer's round trip spans three days, the mid diffuses between prints and the bounce is buried. The covariance estimate is unbiased in theory and useless in practice, because its standard error scales with $\text{Var}(\Delta p)$, which is now dominated by $\sigma_\varepsilon^2$. Ben Dor's team responded by building Liquidity Cost Scores from trader *indications* rather than prints. The 2026 desk has a third option the 2010 authors lacked: dense electronic RFQ logs, its own and the platforms', where both sides of the market are observed within seconds. Use Roll on TRACE as a cross-check and a stress indicator, not as your spread.

> **[SOURCE EXTRACTION]** *Dynkin_Systematic_Investing_in_Credit p.702:* LCS "measures the cost of an immediate round-trip transaction of a typical institutional size and is expressed as a percentage of a bond price"
>
> **Annotation.** Our analysis: notice the three qualifiers, *immediate*, *round-trip*, and *typical institutional size*. Roll measures none of them exactly: it measures the average bounce across whatever sizes printed, with no immediacy constraint. For spread-quoted bonds, LCS is the bid–offer spread times spread duration. Ben Dor p.123 then multiplies the indications of non-benchmark bonds by an adjustment factor between 1.50 and 1.83, which is the industry admitting in writing that dealer indications are tighter than dealer markets. The modern desk uses LCS-type composites as the prior and its own RFQ fills as the likelihood.

> **Trend Watch: the great spread compression, and its stress reversals (2004–2026).** *What changed:* TRACE dissemination was phased in from 2002 to 2005. Edwards, Harris & Piwowar (2007, *Journal of Finance* 62(3)) and Goldstein, Hotchkiss & Sirri (2007, *Review of Financial Studies* 20(2)) both find that transparency lowered customer trading costs (magnitudes vary by sample and bond type; see the papers). *How big, then:* Chen, Lesmond & Wei (2007) estimate bid–ask spreads of about 25 bp for AAA bonds and 180 bp for CCC; Man's 2022 authors note that spreads are "markedly tighter in the current market" (Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.20). *The stress reversal:* the same Man page charts a 20-day average HY bid–ask (Bloomberg data, 1 July 2017 to 2 February 2021) that gaps out in February–March 2020 and then normalizes. Kargar et al. (2021, *Review of Financial Studies*) estimate that at the March 2020 peak, customers' willingness to pay for immediacy rose by roughly 200 bp per dollar traded, and flow shifted from risky-principal to slower agency trades. *2026:* MarketAxess data reported by The DESK (2026-10-01) show the median EUR IG bid–ask falling from 0.0879 to 0.0673 (−23.5%) over the 34 weeks to 2026-08-23. In the March 2026 stress, however, EUR IG bid–ask hit 64% above its January average, and recovery took 4 weeks (EUR IG), 6 (US HY), 8 (US IG), 13 (EUR HY), and 14+ (EM). *What it means for the desk:* the median spread is a fair-weather number. A cost model calibrated on a calm window, by Roll or anything else, underprices exactly the trades you most need to price. Make the spread estimator regime-conditional, and carry the stress multiplier as a parameter.

> **Ways This Blows Up.** (1) *Taking the absolute value.* When the sample covariance is positive, someone always writes `2*sqrt(abs(cov))`. That reports a spread when the data are reporting momentum. Return NaN and log the sign. (2) *Mixing sizes.* Odd lots pay more than blocks (Edwards, Harris & Piwowar 2007), and "5MM+" capped prints are a different market from \$50k retail prints. Estimate by size bucket. (3) *Interdealer double counting.* Both dealers report an interdealer trade. Leave both legs in and you manufacture a bounce of exactly zero width between two identical prices, which biases the covariance toward zero (§18.8). (4) *Stale prints.* Prints days apart measure diffusion, not bounce. Cap the gap between consecutive prints or weight by it.

### Specification for AI Implementation (Roll estimator)

**The Spec You Hand the Robot.** *What ROBO built from the vague version ("estimate the bid–ask spread from TRACE"):* it averaged (ask print − bid print) over all prints on the same day, on a bond that traded twice a week, and reported a spread of zero for every day with one print. The precise spec: input a time-ordered vector of cleaned prices (points per 100 par) for one bond and one size bucket. Output `(spread, autocov)` in points. Require at least `min_obs` price changes. Return `NaN` when the autocovariance is non-negative, and never take an absolute value. Sanity checks: recover a known spread on simulated Roll data, recover $S(1-\rho)$ under order splitting, and return `NaN` under momentum.

```python
import numpy as np
import pandas as pd
from scipy import stats, integrate, signal

RNG = np.random.default_rng(18)

def roll_spread(prices, min_obs=20):
    """Roll (1984) effective spread from consecutive trade prices (points per 100 par).
    Returns (spread_points, autocov). spread is NaN when autocov >= 0 (Roll undefined)."""
    p = np.asarray(prices, dtype=float)
    p = p[np.isfinite(p)]
    if p.size < min_obs + 2:
        return np.nan, np.nan
    dp = np.diff(p)
    c = np.cov(dp[1:], dp[:-1], ddof=1)[0, 1]
    if c >= 0.0:
        return np.nan, c          # momentum or splitting dominates: never take abs()
    return 2.0 * np.sqrt(-c), c

def simulate_roll(n, spread, sigma_mid, rho=0.0, phi_mid=0.0, rng=RNG):
    """p_t = m_t + (spread/2) I_t. I_t: symmetric +/-1 Markov chain with lag-1 autocorr rho.
    Mid increments: AR(1) with coefficient phi_mid (phi_mid > 0 mimics informed drift)."""
    stay = 0.5 * (1.0 + rho)
    flips = rng.random(n) >= stay
    flips[0] = False
    I = rng.choice([-1.0, 1.0]) * np.where(np.cumsum(flips) % 2 == 0, 1.0, -1.0)
    eps = rng.normal(0.0, sigma_mid, n)
    dm = signal.lfilter([1.0], [1.0, -phi_mid], eps)
    m = 90.0 + np.cumsum(dm)
    return m + 0.5 * spread * I

# Sanity 1: Roll recovers the spread when signs are i.i.d.
s_hat, _ = roll_spread(simulate_roll(200_000, spread=0.50, sigma_mid=0.05))
assert abs(s_hat - 0.50) < 0.02, s_hat
# Sanity 2: order splitting shrinks the estimate to S(1 - rho)
s_split, _ = roll_spread(simulate_roll(200_000, spread=0.50, sigma_mid=0.05, rho=0.6))
assert abs(s_split - 0.50 * 0.4) < 0.02, s_split
# Sanity 3: informed drift turns the covariance positive -> NaN, not a fake spread
s_mom, c_mom = roll_spread(simulate_roll(50_000, spread=0.10, sigma_mid=0.10, rho=0.6, phi_mid=0.4))
assert np.isnan(s_mom) and c_mom > 0, (s_mom, c_mom)
gamma_bpw = lambda prices: -roll_spread(prices)[1]   # Bao-Pan-Wang illiquidity, points^2
```

The third check is worth working by hand. With $S = 0.10$ and $\rho = 0.6$, the bounce contributes $-c^2(1-\rho)^2 = -0.0025 \times 0.16 = -0.0004$ to the autocovariance. The mid increments have stationary variance $0.01/(1-0.16) \approx 0.0119$ and lag-one autocovariance $0.4 \times 0.0119 \approx 0.0048$. Momentum wins by a factor of twelve, and a well-behaved estimator says so by refusing to answer.
