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

## 18.3 Who Knows More Than You: Glosten–Milgrom Recalled, Kyle Derived

Roll measured the spread and assumed nobody knew anything. The next two models put knowledge back in. Glosten–Milgrom asks *whether* the person on the other side knows more than you. Kyle asks *how much* their size tells you. In an RFQ market you get to see both the side and the size before you quote, which is a gift Kyle's market maker never received, and also a trap, because the client knows you are looking.

### 18.3.1 Glosten–Milgrom in one line

Chapter 3 derived the RFQ version. Let the bond's value be $V = m \pm \sigma_V$ with equal probability, and let a fraction $\pi$ of RFQs come from clients who know which. A zero-profit dealer sets each quote to the conditional expectation of value given the side of the trade:

$$
p^{b} = \mathbb{E}^{\mathbb{P}}[V \mid \text{client sells}] = m - \pi\sigma_V, \qquad p^{a} = m + \pi\sigma_V .
$$

The suspicion spread is $2\pi\sigma_V$. It is the price of not knowing which hand you are facing, and it exists even for a dealer with zero inventory and zero risk aversion. Remember that fact for §18.5, where dealer inventory goes to zero and the spread does not.

### 18.3.2 Kyle (1985), derived

Kyle's market maker does not see individual orders. It sees only the total order flow. One informed trader knows the liquidation value $v \sim \mathcal{N}(p_0, \Sigma_0)$, with $\sigma_v = \sqrt{\Sigma_0}$. Noise traders submit $u \sim \mathcal{N}(0,\sigma_u^2)$, independent of $v$. The insider submits $x$, the market maker sees $y = x + u$ and sets a price $p$ equal to $\mathbb{E}[v \mid y]$, and the insider maximizes expected profit $\mathbb{E}[(v - p)\,x \mid v]$.

*Notation.* The book reserves $\lambda$ for default intensity. Kyle's price-impact slope is therefore $\lambda^{K}$.

Guess linear strategies: $x = \beta(v - p_0)$ and $p = p_0 + \lambda^{K} y$.

*Insider's problem.* Given $v$, the insider chooses $x$ to maximize $\mathbb{E}[x(v - p_0 - \lambda^{K}(x + u))] = x(v - p_0) - \lambda^{K}x^2$. The first-order condition gives

$$
x = \frac{v - p_0}{2\lambda^{K}} \quad\Longrightarrow\quad \beta = \frac{1}{2\lambda^{K}} .
$$

*Market maker's problem.* Projection of $v$ on $y$ gives

$$
\lambda^{K} = \frac{\text{Cov}(v, y)}{\text{Var}(y)} = \frac{\beta\Sigma_0}{\beta^2\Sigma_0 + \sigma_u^2}.
$$

*Fixed point.* Substitute $\beta = 1/(2\lambda^{K})$:

$$
\lambda^{K}\left(\frac{\Sigma_0}{4(\lambda^{K})^2} + \sigma_u^2\right) = \frac{\Sigma_0}{2\lambda^{K}}
\;\Longrightarrow\; \lambda^{K}\sigma_u^2 = \frac{\Sigma_0}{4\lambda^{K}}
\;\Longrightarrow\; \lambda^{K} = \frac{\sigma_v}{2\sigma_u}, \qquad \beta = \frac{\sigma_u}{\sigma_v}.
$$

Market depth is $1/\lambda^{K}$: the flow needed to move the price one point. The posterior variance is $\text{Var}(v \mid y) = \Sigma_0/2$, so the trade reveals exactly half of the insider's information. The insider earns $\mathbb{E}[x(v-p)] = \tfrac12\sigma_v\sigma_u$, which the noise traders pay, while the market maker breaks even. The insider scales trading to the amount of camouflage: double the noise and the insider trades twice as much, at the same impact per unit of private information. That is why informed credit flow loves month-end and index rebalance days.

### 18.3.3 Translating Kyle to the RFQ

Three changes turn Kyle into a desk tool.

1. **Flow is observed per client, not in aggregate.** On a disclosed RFQ the dealer sees the client's name, side, and size. The noise-versus-informed split that Kyle hides in $u$ is now a *classification problem by client tier*. Glosten–Milgrom's $\pi$ becomes $\pi_c$, estimated from that client's hand history.
2. **The value $v$ is a future IDO-adjusted mid.** Define the $h$-day markout of trade $i$ as the change in the bond's mid from the trade time to $h$ days later, after stripping the rates move and the bond's factor-model prediction (Chapter 9). A markout that is factor beta is not information about the issuer. IDO or it didn't happen.
3. **Estimate $\lambda^{K}$ by regression.** Regress markouts on signed size normalized by average daily volume:

$$
\text{MO}_{i,h} = a_h + \lambda^{K}_{h}\,\frac{y_i}{\text{ADV}_i} + \mathbf{b}_h^{\top}\mathbf{z}_i + e_{i,h},
$$

where $y_i > 0$ is a customer buy and $\mathbf{z}_i$ holds controls (rating, age, ETF flow, time of day). Use $h \in \{1, 5, 20\}$ days. The regression on the move from the *pre-trade* mid recovers the information content $\lambda^{K}$. Run the same regression on the move from the *trade price* and an efficient dealer should see a slope of zero. A positive post-trade slope means the street under-reacted to the flow, and the bond *drifts* after informed trades. A negative slope means the street over-reacted, or charged for inventory, and the price *bounces back*.

This is momentum and reversal at the microstructure scale, and it is the same fork Chapter 10 meets at monthly horizons. Post-RFQ drift is momentum conditional on informed flow. Roll's bounce is reversal conditional on uninformed flow. The desk's job is to tell them apart in three seconds.

Guo, Lehalle & Xu (2021), *Transaction Cost Analytics for Corporate Bonds* (arXiv 1903.09140), estimate exactly this kind of curve on Enhanced TRACE. The transient impact jumps at the trade and then decays toward a permanent level. In the language of this chapter, the jump is the dealer's suspicion and inventory charge, the decay is Harris's resiliency, and the permanent level is Kyle's information. Their headline finding is an *asymmetry* between customer-buy and customer-sell impact, which a symmetric $\lambda^{K}$ cannot capture. Estimate $\lambda^{K}_{\text{buy}}$ and $\lambda^{K}_{\text{sell}}$ separately.

> **Poker Table.** Ines draws it on a napkin. "The number of dealers in comp is the number of players. The size is the bet. The client's name is the tell. And the cover, the second-best price you only learn after you lose, is the hand you didn't get to see." Winning an RFQ against four other dealers means you were the most optimistic of five people looking at the same cards. "If you win every hand at a five-handed table," she says, "you aren't good. You are the one paying for everyone's information." Hendershott & Madhavan (2015, *Journal of Finance* 70(1)) find that electronic auctions are used mainly for smaller, more liquid, less information-sensitive trades, while larger tickets go to voice, where fewer players see the cards. Fermanian, Guéant & Pu (2017, arXiv 1511.07773) model one European dealer's multi-dealer-to-client RFQ data and find that dealers quote more conservatively as the number of requested dealers rises. That is the winner's curse, priced in at the table (§18.9 does the arithmetic).

### Specification for AI Implementation (Kyle estimator)

Input: arrays of markouts (points, IDO-adjusted, horizon $h$ stated in the column name) and signed flow (customer buy positive; USD mm or ADV-normalized; state which). Output: slope and $t$-statistic. In production, use heteroskedasticity-robust errors clustered by issuer and day. The simulation below checks the closed form, the absence of post-trade drift under efficient pricing, and the insider's profit $\tfrac12\sigma_v\sigma_u$.

```python
def kyle_equilibrium(sigma_v, sigma_u):
    """One-period Kyle (1985). Returns (lambda_K, beta).
    lambda_K is in points per unit of flow; beta in flow units per point."""
    if sigma_v <= 0 or sigma_u <= 0:
        raise ValueError("volatilities must be positive")
    return 0.5 * sigma_v / sigma_u, sigma_u / sigma_v

def estimate_kyle_lambda(markout, signed_flow):
    """OLS slope of markout (points) on signed flow, with intercept. Returns (slope, t_stat)."""
    yv = np.asarray(markout, float)
    xv = np.asarray(signed_flow, float)
    X = np.column_stack([np.ones_like(xv), xv])
    coef, *_ = np.linalg.lstsq(X, yv, rcond=None)
    resid = yv - X @ coef
    s2 = resid @ resid / (len(yv) - 2)
    se = np.sqrt(s2 * np.linalg.inv(X.T @ X)[1, 1])
    return coef[1], coef[1] / se

sig_v, sig_u, n_k, p0 = 2.0, 5.0, 100_000, 90.0     # value std (points), noise std (USD mm)
lam_K, beta_K = kyle_equilibrium(sig_v, sig_u)       # 0.2 points per USD mm
v_k = p0 + RNG.normal(0.0, sig_v, n_k)
u_k = RNG.normal(0.0, sig_u, n_k)
x_k = beta_K * (v_k - p0)
y_k = x_k + u_k
p_k = p0 + lam_K * y_k
slope_total, _ = estimate_kyle_lambda(v_k - p0, y_k)
slope_post, t_post = estimate_kyle_lambda(v_k - p_k, y_k)
assert abs(slope_total / lam_K - 1.0) < 0.03          # information content = lambda_K
assert abs(t_post) < 4.0                              # efficient pricing: no post-trade drift
assert abs(np.mean(x_k * (v_k - p_k)) / (0.5 * sig_v * sig_u) - 1.0) < 0.03
assert abs(np.var(v_k - p_k) / (0.5 * sig_v**2) - 1.0) < 0.03   # half the information revealed
```

## 18.4 Avellaneda–Stoikov, Derived Without Skipping Steps

Kaz's auto-quoter was an Avellaneda–Stoikov engine. Avellaneda & Stoikov (2008), "High-frequency trading in a limit order book" (*Quantitative Finance* 8(3): 217–224), built on the dealer-inventory model of Ho & Stoll (1981). It is the most-cited model on the desk and the least-read. We read it now, one step at a time.

### 18.4.1 Setup

Work under $\mathbb{P}$, with time in years.

- **Mid.** $dS_t = \sigma\,dW_t$, arithmetic Brownian motion in price points. Here $\sigma$ is in points per $\sqrt{\text{yr}}$. (Jumps are added in §18.6.)
- **Quotes.** The dealer posts a bid $p^b_t = S_t - \delta^b_t$ and an ask $p^a_t = S_t + \delta^a_t$, with $\delta^b,\delta^a$ in points.
- **Fills.** Counting processes $N^b_t$ and $N^a_t$ jump by one lot when the bid or ask is hit, with intensities $\Lambda(\delta^b_t)$ and $\Lambda(\delta^a_t)$, where $\Lambda(\delta) = A e^{-k\delta}$. $A$ is the arrival rate at zero distance (RFQs per year per side), and $k$ (per point) is how fast business decays as you quote away.
- **Inventory and cash.** $q_t = N^b_t - N^a_t$ in lots, and $dX_t = p^a_t\,dN^a_t - p^b_t\,dN^b_t$.
- **Objective.** Exponential utility of terminal wealth, with risk aversion $\gamma$ per point-lot:

$$
u(t,x,s,q) = \sup_{\delta^b,\delta^a}\; \mathbb{E}^{\mathbb{P}}_t\!\left[-\exp\!\big(-\gamma(X_T + q_T S_T)\big)\right].
$$

### 18.4.2 The HJB equation

Dynamic programming gives the diffusion term from $S$ and one jump term per counting process. When the bid is hit, cash falls by $s - \delta^b$ and inventory rises by one; when the ask is lifted, cash rises by $s + \delta^a$ and inventory falls by one:

$$
\partial_t u + \tfrac12\sigma^2\partial_{ss}u
+ \sup_{\delta^b}\Lambda(\delta^b)\big[u(t,x - s + \delta^b, s, q+1) - u\big]
+ \sup_{\delta^a}\Lambda(\delta^a)\big[u(t,x + s + \delta^a, s, q-1) - u\big] = 0,
$$

with terminal condition $u(T,x,s,q) = -\exp(-\gamma(x + qs))$.

### 18.4.3 Step 1: the frozen-inventory value and the reservation prices

Suppose first that the dealer cannot trade. Using $\mathbb{E}[e^{aZ}] = e^{a^2/2}$ for standard normal $Z$, with $\tau = T - t$,

$$
v(t,x,s,q) = \mathbb{E}\big[-e^{-\gamma(x + qS_T)}\big] = -\exp\!\Big(-\gamma x - \gamma q s + \tfrac12\gamma^2 q^2\sigma^2\tau\Big).
$$

The **reservation bid** $r^b$ is the price at which the dealer is indifferent to buying one more lot: $v(t, x - r^b, s, q+1) = v(t,x,s,q)$. Equating exponents,

$$
\gamma r^b - \gamma s + \tfrac12\gamma^2\sigma^2\tau\big[(q+1)^2 - q^2\big] = 0
\;\Longrightarrow\;
r^b = s - (1+2q)\,\frac{\gamma\sigma^2\tau}{2}.
$$

The same argument for selling one lot gives $r^a = s + (1-2q)\,\gamma\sigma^2\tau/2$. Their average is the famous **reservation price**:

$$
r^{\text{res}} = s - q\,\gamma\sigma^2\tau. \tag{18.1}
$$

A long dealer ($q>0$) values the bond below the mid, and by an amount proportional to inventory, risk aversion, variance, and time left. This is the skew.

### 18.4.4 Step 2: the exponential ansatz

Try $u = -\exp(-\gamma(x + \theta(t,s,q)))$ with $\theta(T,s,q) = qs$. Then $\partial_t u = -\gamma u\,\theta_t$ and $\partial_{ss}u = u(\gamma^2\theta_s^2 - \gamma\theta_{ss})$. The jump terms factor as

$$
u(t, x - s + \delta^b, s, q+1) - u = u\left[e^{-\gamma(\delta^b - s + r^b)} - 1\right], \qquad r^b \equiv \theta(t,s,q+1) - \theta(t,s,q),
$$

and similarly on the ask, with $r^a \equiv \theta(t,s,q) - \theta(t,s,q-1)$. These $r^b, r^a$ are the indifference prices of the *true* value function, not of the frozen one. Because $u<0$, dividing the HJB by $-\gamma u > 0$ preserves the supremum and gives

$$
\theta_t + \tfrac12\sigma^2\theta_{ss} - \tfrac12\gamma\sigma^2\theta_s^2
+ \sup_{\delta^b}\frac{\Lambda(\delta^b)}{\gamma}\Big[1 - e^{-\gamma(\delta^b - (s - r^b))}\Big]
+ \sup_{\delta^a}\frac{\Lambda(\delta^a)}{\gamma}\Big[1 - e^{-\gamma(\delta^a - (r^a - s))}\Big] = 0 .
$$

Read the bracket on the bid: $\delta^b - (s - r^b) = r^b - p^b$ is the profit from buying at $p^b$, measured at the dealer's own reservation value, passed through the utility.

### 18.4.5 Step 3: the first-order condition

Write $y = \delta - \Delta$, with $\Delta = s - r^b$ on the bid. Maximize $f(\delta) = \Lambda(\delta)(1 - e^{-\gamma y})$. Setting $f'(\delta) = 0$:

$$
\Lambda'(\delta)\big(1 - e^{-\gamma y}\big) + \gamma\Lambda(\delta)e^{-\gamma y} = 0
\;\Longrightarrow\;
y^{*} = \frac{1}{\gamma}\ln\!\left(1 - \gamma\,\frac{\Lambda(\delta^*)}{\Lambda'(\delta^*)}\right). \tag{18.2}
$$

Equation (18.2) holds for *any* decreasing intensity, and §18.7 uses it with a logistic win curve. Since $f = 0$ at $y = 0$, $f \to 0$ as $\delta \to \infty$, and $f > 0$ in between, the unique critical point is a maximum. For the exponential intensity, $\Lambda'/\Lambda = -k$, so

$$
p^{b} = r^{b} - \frac{1}{\gamma}\ln\!\Big(1 + \frac{\gamma}{k}\Big), \qquad
p^{a} = r^{a} + \frac{1}{\gamma}\ln\!\Big(1 + \frac{\gamma}{k}\Big). \tag{18.3}
$$

The parameter $A$ has cancelled: how *often* you are asked does not enter the markup. Hold that thought.

### 18.4.6 Step 4: the AS approximation, and the two halves of the spread

The exact $r^b, r^a$ require solving for $\theta$ (GLFT do this in §18.5). Avellaneda and Stoikov approximate them by the frozen-inventory values of Step 1, which is accurate when $\gamma$ or the fill intensity is small. Substituting:

$$
p^{b} = s - \big(q + \tfrac12\big)\gamma\sigma^2\tau - \frac{1}{\gamma}\ln\!\Big(1+\frac{\gamma}{k}\Big),
\qquad
p^{a} = s - \big(q - \tfrac12\big)\gamma\sigma^2\tau + \frac{1}{\gamma}\ln\!\Big(1+\frac{\gamma}{k}\Big),
$$

$$
p^{a} - p^{b} = \underbrace{\gamma\sigma^2\tau}_{\text{fear}} + \underbrace{\frac{2}{\gamma}\ln\!\Big(1+\frac{\gamma}{k}\Big)}_{\text{greed}}. \tag{18.4}
$$

*Limit 1: $\gamma \to 0$.* A Taylor expansion gives $\tfrac{1}{\gamma}\ln(1+\gamma/k) = \tfrac1k - \tfrac{\gamma}{2k^2} + O(\gamma^2) \to \tfrac1k$. A risk-neutral dealer facing demand $Ae^{-k\delta}$ maximizes $\delta A e^{-k\delta}$, whose maximizer is $\delta^{*} = 1/k$. So the second half of the spread is the monopoly markup. It is pure market power, and $k$ is the price elasticity of your RFQ wins. A more competitive market (larger $k$) means a smaller markup, and a dealer with no risk aversion still charges it.

*Limit 2: $t \to T$.* The fear term and the skew both vanish. The AS dealer becomes fearless at the bell.

**Worked example (the cold open).** Take $\sigma = 8$ points$/\sqrt{\text{yr}}$, which is roughly what a B2 bond with spread duration near 4 and spread volatility near 200 bp a year implies *(illustrative)*. Take $\tau = 5/252$ years, a one-week expected holding period rather than the time to the close. Take $\gamma = 0.005$ per point-lot, with a lot of \$1mm, so the dealer's risk tolerance $1/\gamma$ is 200 point-lots, or \$2mm. Take $k = 3$ per point and $q = +3$. Then $\sigma^2\tau = 1.270$ point$^2$, so the fear per lot is $\gamma\sigma^2\tau = 0.0063$ points and the inventory part of the bid distance is $(q+\tfrac12)\gamma\sigma^2\tau = 0.022$ points. The greed per side is $200\ln(1.001667) = 0.333$ points. The bid is $91.25 - 0.022 - 0.333 = 90.895$, which rounds to 90.875 on the eighths grid. That is Kaz's quote.

Notice the proportions: Kaz's quote was 94% greed and 6% fear. In a bond, the diffusive inventory term is usually pennies. The AS dealer is a monopolist with a nervous tic. The real fear lives in jumps (§18.6) and in the client (§18.7), neither of which the formula was given.

> **Units box: what ROBO did with the volatility.** $\sigma$ is the price volatility of the mid in **points per $\sqrt{\text{yr}}$**; $\tau$ is in **years**; $\gamma$ is per **point × lot**; $k$ is per **point**; $q$ is in **lots** (state the lot size); $A$ is in **RFQs per year per side**. Convert spread volatility to price volatility with $\sigma_P \approx D^{\text{spr}}\,P\,\sigma_s$, where $\sigma_s$ is the decimal spread volatility; for $D^{\text{spr}} = 4$, $P = 91.25$ and $\sigma_s = 0.02$, that gives $\sigma_P \approx 7.3$ points. ROBO was told "use the bond's volatility" and fed 200, the spread vol in bp. The fear term rose by a factor of 625, and the bid came out at 77.03 on a bond at 91.25. ROBO was, technically, being prudent.

> **Ways This Blows Up.** (1) *Terminal time is a calendar artifact.* With $T$ set to 4 p.m., the skew collapses into the close, so the dealer gets brave at 3:55 p.m., the least liquid minutes of the HY day. Set $\tau$ to the expected holding period or use the stationary GLFT quotes (§18.5). (2) *The skew can cross the market.* The spread in (18.4) is positive, but the center $r^{\text{res}}$ moves by $q\gamma\sigma^2\tau$. A desk short 50 lots can produce a bid above the composite offer. Clip quotes to a band around the composite and route breaches to a human. (3) *$A$ does not enter.* AS quotes the same in a bond asked about once a month as in one asked about a hundred times a day. For illiquid bonds this is plainly wrong, and §18.5 fixes it. (4) *$\sigma$ must be a $\mathbb{P}$ forecast of mid price volatility* over the holding period, not CDS implied vol and not spread vol in bp. (5) *The exponential intensity is local.* A real RFQ win curve saturates at one when you bid through the composite. Use (18.2) with the fitted curve (§18.7). (6) *One lot is not a block.* AS prices the marginal lot. The client is selling eight (§18.7).

> **[SOURCE EXTRACTION]** *Ben_Dor_Quantitative_Credit_Portfolio_Management p.120:* "If a trader were temporarily long inventory of a particular bond, then the trader might quote the bond with a tighter spread (i.e., a higher offered spread) to entice a bid, and vice versa."
>
> **Annotation.** Our analysis: this is the AS skew observed in the wild, written down by people who wanted to remove it. A long trader moves the offer toward the bid to attract buyers, which in spread terms means raising the offered spread. That is (18.1) acting on one side of the market. To Ben Dor's team the skew is contamination in a liquidity measure, and they average a month of indications to wash it out. To a market maker it is the optimal policy, and it carries information: a dealer whose runs skew persistently toward selling a bond is telling you its inventory. The 2026 desk can turn the observation around and estimate street inventory from the skew of composite contributors, then use it as a feature (§18.8). One caveat about the quotation's world: these were indications, not firm quotes. A dealer can skew a run for free; a firm streaming quote has to pay for the skew when it is hit.

### Specification for AI Implementation (AS quoting core)

**The Spec You Hand the Robot.** *Vague version:* "quote bonds using Avellaneda–Stoikov." *What ROBO built:* $T$ = 4 p.m. New York, so its quotes widened at 9:30 a.m. and tightened all afternoon, and its σ came from the CDS ladder. *Precise version:* inputs are the composite mid $s$ (points), inventory $q$ (lots of \$1mm), price volatility $\sigma$ (points/$\sqrt{\text{yr}}$, 20-day $\mathbb{P}$ forecast), $\gamma$ (per point-lot), $k$ (per point, from the fitted win curve), and holding-period horizon $\tau$ (years, never the time to the close). Outputs are bid, ask, $r^{\text{res}}$, and the fear and greed split, all in points, plus prices rounded to the instrument's tick. Guards: reject negative inputs; use the $1/k$ limit when $\gamma < 10^{-12}$; never let unit conversion happen inside the function.

```python
from scipy.optimize import minimize_scalar

def as_greed(gamma, k):
    """Per-side markup (1/gamma) ln(1 + gamma/k), in points. Tends to 1/k as gamma -> 0."""
    if k <= 0:
        raise ValueError("k must be positive (per point)")
    if gamma < 1e-12:
        return 1.0 / k
    return np.log1p(gamma / k) / gamma

def as_quotes(s, q, sigma, gamma, k, tau):
    """Avellaneda-Stoikov (2008) approximate quotes. s points; q lots; sigma points/sqrt(yr);
    gamma per point-lot; k per point; tau years. Returns prices and the fear/greed split."""
    if sigma < 0 or gamma < 0 or tau < 0:
        raise ValueError("sigma, gamma, tau must be non-negative")
    fear = gamma * sigma**2 * tau                     # full-spread inventory term, points
    g = as_greed(gamma, k)
    r_res = s - q * fear                              # (18.1)
    return {"r_res": r_res, "bid": r_res - 0.5 * fear - g, "ask": r_res + 0.5 * fear + g,
            "spread": fear + 2.0 * g, "fear": fear, "greed": 2.0 * g}

to_eighth = lambda px: np.round(np.asarray(px, float) * 8.0) / 8.0

tau_hold = 5.0 / 252.0
qa = as_quotes(s=91.25, q=3, sigma=8.0, gamma=0.005, k=3.0, tau=tau_hold)
assert abs(qa["bid"] - 90.8947) < 1e-3 and to_eighth(qa["bid"]) == 90.875     # Kaz's quote
assert abs(qa["spread"] - (qa["fear"] + qa["greed"])) < 1e-12                  # (18.4)
assert qa["greed"] / qa["spread"] > 0.9                                         # mostly greed
assert abs(as_greed(1e-9, 3.0) - 1.0 / 3.0) < 1e-9                              # gamma -> 0
assert as_quotes(91.25, 3, 8.0, 0.005, 3.0, 0.0)["r_res"] == 91.25             # t -> T

# General FOC (18.2), checked by brute force for the exponential intensity
A_, k_, g_, Delta = 50.0, 3.0, 0.005, 0.0222
obj = lambda d: -A_ * np.exp(-k_ * d) * (-np.expm1(-g_ * (d - Delta))) / g_
d_star = minimize_scalar(obj, bounds=(Delta, Delta + 5.0), method="bounded",
                         options={"xatol": 1e-10}).x
assert abs(d_star - (Delta + as_greed(g_, k_))) < 1e-6

# ROBO's unit error: spread vol in bp (200) fed as price vol in points
assert as_quotes(91.25, 3, 200.0, 0.005, 3.0, tau_hold)["bid"] < 78.0
```
