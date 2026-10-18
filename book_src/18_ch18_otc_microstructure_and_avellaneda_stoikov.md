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
> **Annotation.** Our analysis: the Man authors are right about the *protocol* and, by 2026, wrong about the *responder*. The disclosed RFQ is still a sealed-bid auction among a handful of dealers. What changed between 2022 and 2026 is who answers it. Trumid reported 88% of eligible RFQ line items executed with no human touch in September 2025, and Tradeweb says AiEX now handles a large and rising share of its institutional trades (sources in Trend Watch, §18.7). The runs are still "not firm and actionable", which is why §18.2 has to recover spreads from prints rather than quotes. The same page also complains about "if filled" trades. That complaint is the reason the modern engine treats fill probability as a modeled variable rather than as noise: in §18.7 the win curve $P(x)$ is a first-class input to the quote, not an afterthought in the backtest.

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

> **Trend Watch: the great spread compression, and its stress reversals (2004–2026).** *What changed:* TRACE dissemination was phased in from 2002 to 2005. Edwards, Harris & Piwowar (2007, *Journal of Finance* 62(3)) and Goldstein, Hotchkiss & Sirri (2007, *Review of Financial Studies* 20(2)) find that transparency helped liquidity, though not uniformly: the first reports lower trading costs once TRACE disseminates prices, and the second a neutral-to-positive effect, with spreads narrowing except for very large trades and very infrequently traded bonds (magnitudes vary by sample and bond type; see the papers). *How big, then:* Chen, Lesmond & Wei (2007) estimate bid–ask spreads of about 25 bp for AAA bonds and 180 bp for CCC; Man's 2022 authors note that spreads are "markedly tighter in the current market" (Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.20). *The stress reversal:* the same Man page charts a 20-day average HY bid–ask (Bloomberg data, 1 July 2017 to 2 February 2021) that gaps out in February–March 2020 and then normalizes. Kargar et al. (2021, *Review of Financial Studies*) estimate that at the March 2020 peak, customers' willingness to pay for immediacy rose by roughly 200 bp per dollar traded, and flow shifted from risky-principal to slower agency trades. *2026:* MarketAxess data reported by The DESK (2026-10-01) show the median EUR IG bid–ask down from 0.0879 to 0.0673 price % of par (−23.5%), comparing the 34 weeks to 2026-08-23 with the same weeks of 2025. In the March 2026 stress, however, EUR IG bid–ask hit 64% above its January average, and recovery took 4 weeks (EUR IG), 6 (US HY), 8 (US IG), 13 (EUR HY), and 14 (EM, which then widened again and has been above its January level in 21 of the 22 weeks since the peak). *What it means for the desk:* the median spread is a fair-weather number. A cost model calibrated on a calm window, by Roll or anything else, underprices exactly the trades you most need to price. Make the spread estimator regime-conditional, and carry the stress multiplier as a parameter.

> **Ways This Blows Up.** (1) *Taking the absolute value.* When the sample covariance is positive, someone always writes `2*sqrt(abs(cov))`. That reports a spread when the data are reporting momentum. Return NaN and log the sign. (2) *Mixing sizes.* Odd lots pay more than blocks (Edwards, Harris & Piwowar 2007), and "5MM+" capped prints are a different market from \$50k retail prints. Estimate by size bucket. (3) *Interdealer double counting.* Both dealers report an interdealer trade. Leave both legs in and you manufacture a bounce of exactly zero width between two identical prices, which biases the covariance toward zero (§18.8). (4) *Stale prints.* Prints days apart measure diffusion, not bounce. Cap the gap between consecutive prints or weight by it.

### Specification for AI Implementation (Roll estimator)

**The Spec You Hand the Robot.** *What ROBO built from the vague version ("estimate the bid–ask spread from TRACE"):* it averaged (ask print − bid print) over all prints on the same day, on a bond that traded twice a week, and reported a spread of zero for every day with one print. The precise spec: input a time-ordered vector of cleaned prices (points per 100 par) for one bond and one size bucket. Output `(spread, autocov)` in points. Require at least `min_obs` price changes. Return `NaN` when the autocovariance is non-negative, and never take an absolute value. Sanity checks: recover a known spread on simulated Roll data, recover $S(1-\rho)$ under order splitting, and return `NaN` under momentum.

Somewhere in the book is a B3 bond that prints twice a week, and nobody will tell you what it costs to get out of it. The derivation says the answer is hiding in the way consecutive prices bounce, but a derivation is not a nightly job. A desk that holds a few thousand bonds needs a spread estimate for each one, in each size bucket, before the morning risk meeting, and it needs the estimate to say "I don't know" in the same way every time, not only when the analyst on call happens to notice. That is the case for putting Roll's trick into a function and surrounding the function with tests that can fail.

Listing 18.1 has two working parts. `roll_spread` takes a time-ordered vector of prices in points per 100 par, discards anything that is not finite, and declines to answer unless at least `min_obs + 2` prices survive, which leaves `min_obs` pairs of consecutive price changes. It differences the prices, takes the sample covariance between each change and the one before it, and returns the pair `(spread, autocov)`. When the covariance is negative, the spread is twice the square root of its magnitude, which is the estimator derived above. When the covariance is zero or positive, the spread is `NaN` and the covariance comes back anyway, so the caller can log the sign. The function never takes an absolute value, because a positive covariance is the data reporting momentum, and a spread built from it would be fiction with a confident decimal point.

The second part, `simulate_roll`, is the test bench. It builds prices as a random-walk mid plus half a spread times a trade sign. The signs come from a two-state Markov chain whose persistence `rho` stands for order splitting (`rho = 0` is Roll's original i.i.d. world), and the mid increments pass through an AR(1) filter with coefficient `phi_mid`, so a positive value plays the informed trader who keeps pushing the mid in the direction of the flow. Three assertions pin the estimator to the algebra. With i.i.d. signs, it recovers a 0.50-point spread to within 0.02. With `rho` of 0.6, it returns about 0.20, which is $S(1-\rho)$. With strong drift, it returns `NaN` and a positive covariance. The last line defines the Bao–Pan–Wang illiquidity measure as minus the autocovariance, in points squared.

Use it on TRACE prints for one bond in one size bucket, as a cross-check and a stress indicator rather than as the spread you quote from. The edge case that bites is that the function sees prices and nothing else. It has no timestamps, so a print from Monday and a print from Thursday are treated as neighbours, and dropping a non-finite price silently glues the series across the hole. The mid has diffused in the meantime, the bounce is buried under $\sigma_\varepsilon^2$, and the function returns a number that is mostly noise. The caller must bucket by size and cap the gap before the vector arrives. Remember too that a sample covariance is noisy: a single `NaN` is not proof of informed flow, and a run of them across many bonds on the same day says more than any one.

*The full listing is [Listing 18.1 in Appendix F](#code-18-1).*

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

A desk never gets to see how much the other side knows. It sees a signed size, a price, and, if it waits, where the bond went afterward. Kyle's model is the bridge between those observables and the thing you care about, and the bridge only holds if the regression used to cross it has been tested in a world where you know the answer. So the desk builds that world first: an insider, a crowd of noise, a market maker, and a planted $\lambda^{K}$. Then it asks whether its own estimator can find the number it just hid.

Listing 18.2 does this with two small functions and one simulation. `kyle_equilibrium` returns the closed form from §18.3.2, $\lambda^{K} = \tfrac12\sigma_v/\sigma_u$ in points per unit of flow and $\beta = \sigma_u/\sigma_v$ in flow per point, and it raises an error on non-positive volatilities instead of returning a number that looks like depth. `estimate_kyle_lambda` is the tool the desk would actually reuse: ordinary least squares of a markout, in points, on signed flow, with an intercept, returning the slope and its t-statistic.

The simulation sets the value volatility at 2 points and the noise volatility at USD 5mm, so the planted $\lambda^{K}$ is 0.2 points per USD mm. For 100,000 draws it generates a true value around a starting price of 90, an insider who trades $\beta$ times the surprise, noise traders who add their flow, and a market maker who prices at the starting price plus $\lambda^{K}$ times total flow. Four assertions follow. Regressing the move from the pre-trade mid on total flow recovers $\lambda^{K}$ within 3 percent, which is the information content of flow. Regressing the move from the trade price on the same flow gives no significant slope, which is the no-drift test for an efficient dealer. The insider's average profit lands on $\tfrac12\sigma_v\sigma_u$. And the variance of value left over after the trade is half the prior variance, the "half the information is revealed" result.

Use the estimator on markouts at a stated horizon, one bond tier at a time, with the benchmark written into the column name. The edge case that bites is that the t-statistic is the textbook one. Real markouts are fat-tailed, heteroskedastic, and clustered by issuer and day, so the listing's number overstates significance, sometimes by a lot. It is a check on the simulation, not a licence to trade on a slope. Swap in clustered robust errors before any estimate moves a quote. The benchmark matters just as much: measure from the pre-trade mid and you recover information, measure from the trade price and a good dealer recovers zero, and a column that mixes the two means neither.

*The full listing is [Listing 18.2 in Appendix F](#code-18-2).*

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

Kaz's quote took a page of arithmetic, and it was a quote for one bond, one inventory, one afternoon. A desk streaming prices on a few hundred bonds needs that arithmetic redone every time a fill changes $q$ or the volatility forecast ticks, with nobody around to notice that the 200 should have been a 7. The formulas are short, which is the dangerous part: short formulas get typed into spreadsheets, and spreadsheets do not have units. So the quoting core lives in a function with a narrow contract and a few tests, which makes the arithmetic boring and turns every bad input into somebody's explicit decision.

Listing 18.3 is that function. `as_greed` computes the per-side markup $\tfrac{1}{\gamma}\ln(1+\gamma/k)$ using `log1p` for accuracy, raises an error if $k$ is not positive, and falls back to the limit $1/k$ when $\gamma$ is below $10^{-12}$, so a risk-neutral setting does not divide by zero. `as_quotes` then takes the composite mid, inventory in lots, price volatility, risk aversion, the win-curve decay $k$, and the horizon $\tau$ in years. It computes the fear term $\gamma\sigma^2\tau$, shifts the center to $r^{\text{res}} = s - q\cdot\text{fear}$, and sets the bid and ask half the fear plus one greed away from that center. It returns the reservation price, both quotes, and the spread split into fear and greed, where `greed` is the two-sided total. The helper `to_eighth` rounds to the grid.

The tests reproduce Kaz's bid of 90.8947, which rounds to 90.875. They confirm that the spread is fear plus greed, that greed is over 90 percent of it, that greed approaches $1/k$ as $\gamma \to 0$, and that the center collapses to the mid when $\tau = 0$. A brute-force check then maximizes the general first-order objective numerically for the exponential intensity and finds that the optimum sits at the reservation offset plus `as_greed`, whatever the value of $A$. The last assertion feeds in 200 as volatility and confirms the bid drops below 78.

Use it for the marginal lot in a liquid-enough bond, with $\tau$ set to the holding period. Do not use it where $A$ matters (§18.5) or for blocks (§18.7). The edge case that bites is the last assertion: it records the unit mistake but does not prevent it. The function checks only that $\sigma$, $\gamma$, and $\tau$ are non-negative, so a volatility in basis points is a perfectly legal input. It also does not clip to the composite or round to the tick, so a large inventory can return a bid above the market. Both guards belong in the caller.

*The full listing is [Listing 18.3 in Appendix F](#code-18-3).*

## 18.5 GLFT: Inventory Bounds, Linear ODEs, and the Stationary Dealer

Every desk has a risk limit, and AS does not know it exists. Guéant, Lehalle & Fernandez-Tapia (2013), "Dealing with the inventory risk: a solution to the market making problem" (*Mathematics and Financial Economics*; arXiv 1105.3115), solve the exact problem with $|q| \le Q$. The surprise is that the nonlinear HJB collapses into *linear* ODEs.

**Derivation.** Guess $u(t,x,s,q) = -\exp(-\gamma(x+qs))\,v_q(t)^{-\gamma/k}$, which is the §18.4 ansatz with $\theta = qs + \tfrac1k\ln v_q(t)$. Then $\theta_s = q$, $\theta_{ss} = 0$, $\theta_t = \dot v_q/(k v_q)$, and the reservation prices are $r^b = s + \tfrac1k\ln(v_{q+1}/v_q)$ and $r^a = s - \tfrac1k\ln(v_{q-1}/v_q)$. Equation (18.3) gives the quotes:

$$
\delta^{b}_q(t) = \frac1k\ln\frac{v_q(t)}{v_{q+1}(t)} + \frac1\gamma\ln\!\Big(1+\frac\gamma k\Big), \qquad
\delta^{a}_q(t) = \frac1k\ln\frac{v_q(t)}{v_{q-1}(t)} + \frac1\gamma\ln\!\Big(1+\frac\gamma k\Big).
$$

At the optimum, $e^{-\gamma y^*} = k/(k+\gamma)$, so each supremum equals $A e^{-k\delta^*}/(k+\gamma)$. Substituting $e^{-k\delta^{b*}} = (v_{q+1}/v_q)(1+\gamma/k)^{-k/\gamma}$, the bid supremum becomes $\tfrac{\eta}{k}\,v_{q+1}/v_q$, with $\eta = A(1+\gamma/k)^{-(1+k/\gamma)}$. The reduced HJB, multiplied by $k v_q$, is

$$
\dot v_q(t) = \alpha q^2\, v_q(t) - \eta\big(v_{q-1}(t) + v_{q+1}(t)\big), \qquad \alpha = \tfrac12 k\gamma\sigma^2, \qquad v_q(T) = 1, \tag{18.5}
$$

for $q \in \{-Q,\dots,Q\}$. At $q = Q$ there is no bid, so the $v_{Q+1}$ term is dropped, and symmetrically at $-Q$. In matrix form, $\dot{\mathbf v} = M\mathbf v$ with $M$ symmetric tridiagonal ($\alpha q^2$ on the diagonal, $-\eta$ off it), so $\mathbf v(t) = e^{-M(T-t)}\mathbf 1$. Inventory risk has become a linear algebra problem.

**The stationary dealer.** A bond desk has no close: $T$ is an artifact, and the right object is the limit $T - t \to \infty$. There $\mathbf v \propto \mathbf f_0$, the ground state of $M$ (positive, by Perron–Frobenius), and the quotes stop depending on time. For a closed form, treat $q$ as continuous: $f_{q+1} + f_{q-1} \approx 2f + f''$, so $-\eta f'' + \alpha q^2 f = (\kappa + 2\eta) f$ for an eigenvalue $\kappa$ of $M$. That is the quantum harmonic oscillator, with ground state $f_0 \propto \exp(-\tfrac12\sqrt{\alpha/\eta}\,q^2)$ and eigenvalue spacing $2\sqrt{\alpha\eta}$. Then $\ln(f_q/f_{q+1}) = \tfrac12\sqrt{\alpha/\eta}\,(2q+1)$, which gives

$$
\delta^{b}_\infty(q) \approx \frac1\gamma\ln\!\Big(1+\frac\gamma k\Big) + \frac{2q+1}{2}\,\omega, \quad
\delta^{a}_\infty(q) \approx \frac1\gamma\ln\!\Big(1+\frac\gamma k\Big) - \frac{2q-1}{2}\,\omega, \quad
\omega = \sqrt{\frac{\sigma^2\gamma}{2kA}\Big(1+\frac\gamma k\Big)^{1+\frac k\gamma}}. \tag{18.6}
$$

The skew per lot is $\omega$, and **$A$ is back**. Set the AS skew $\gamma\sigma^2\tau$ equal to $\omega$ and solve for the horizon:

$$
\tau_{\text{eff}} = \frac{\omega}{\gamma\sigma^2} = \frac{1}{\sqrt{2k\gamma\sigma^2\eta}} = \frac{1}{2\sqrt{\alpha\eta}},
$$

the inverse spectral gap of $M$. The effective horizon is how long the street takes to forget your position, and it shrinks like $A^{-1/2}$: a bond asked about four times as often needs half the skew. With $\sigma = 8/\sqrt{252}$ points per $\sqrt{\text{day}}$, $\gamma = 0.005$, $k = 3$, and $A = 2$ fills per day per side at zero distance *(illustrative)*, we get $\eta \approx 0.735$, $\omega \approx 0.017$ points per lot, and $\tau_{\text{eff}} \approx 13$ trading days. That is longer than the one-week guess Kaz plugged into AS. On a Friday afternoon $A$ drops to zero for 60 hours, $\tau_{\text{eff}}$ blows up, and the stationary dealer widens on its own. Credit Suisse's AT1 holders learned why one weekend in 2023 (§18.6).

Guéant (2017), "Optimal market making" (*Applied Mathematical Finance*; arXiv 1605.01862), extends the result to general intensity functions and many assets, and applies it to two credit indices. Guéant & Manziuk (2019, arXiv 1910.13205) note that for a large bond universe "classical finite difference methods … cannot be used" and switch to model-based deep actor–critic methods. Chapter 19 inherits that curse of dimensionality.

> **Trend Watch: the vanishing, then negative, dealer inventory (2007–2026).** *What changed:* post-crisis capital rules pushed bank dealers from warehousing risk toward matching it. Bessembinder, Spatt & Venkataraman (2020, *JFQA* 55(1)) report that non-bank dealers' share of customer–dealer volume rose several-fold after the crisis (as summarized in our industry dossier). *Stress test:* in March 2020, Kargar et al. (2021) find risky-principal costs "increased dramatically" and flow shifted to agency trades. *How big, now:* The DESK (2024-11-20) reported primary dealers net short US\$3.8bn of IG bonds over five years, and quoted Crisil Coalition Greenwich's Kevin McPartland: "Our research continues to point to a corporate bond market that is agency (or at most, riskless principal)." Hedgeweek (2026-07-13), on Crisil Coalition Greenwich analysis of Fed data, reported primary dealers net short US corporates on average in 2026, about \$4bn, for the first time in at least 25 years, against an average net long of about \$16bn in 2017: roughly \$13.7bn short over five years and \$9.7bn long in shorter paper. *What it means:* the market's average fear term, $q\gamma\sigma^2\tau$ summed over dealers, is near zero and in the long end negative, so a typical dealer is *eager to buy* long paper. The spreads that remain are suspicion, greed, and franchise. Agency trading is the $\tau_{\text{eff}} \to 0$ limit of GLFT, where only the constant $\tfrac2\gamma\ln(1+\gamma/k)$ survives. A net-short street also creates squeeze risk if spreads tighten, because pensions and insurers rarely sell long paper. That point was raised in the Hedgeweek piece, and the inventory model prices it as a short-side $\omega$ that nobody budgeted for.

## 18.6 Jump-to-Default Inside the HJB

Kaz's model has one source of risk, $\sigma\,dW_t$. A B2 bond has two. The second is the Tuesday a company announces it would prefer you take 70 cents. Add a Poisson jump to the mid:

$$
dS_t = \mu\,dt + \sigma\,dW_t - J\,dN_t, \qquad N_t \text{ Poisson with } \mathbb{P}\text{-intensity } \lambda^{\mathbb{P}},
$$

where $J > 0$ is the gap in points (default to recovery, or an LMT repricing), and $\mu$ is a drift we come back to. The jump does not change the *structure* of AS. It changes the variance and adds a drift.

### 18.6.1 Exact reservation prices

Freeze inventory and use the Poisson moment generating function $\mathbb{E}[e^{cN_\tau}] = \exp(\lambda\tau(e^c - 1))$:

$$
\mathbb{E}\big[e^{-\gamma q S_T}\big] = \exp\!\Big(-\gamma q (s + \mu\tau) + \tfrac12\gamma^2 q^2\sigma^2\tau + \lambda^{\mathbb{P}}\tau\big(e^{\gamma q J} - 1\big)\Big).
$$

So the certainty-equivalent function becomes

$$
\theta(q) = q(s + \mu\tau) - \tfrac12\gamma q^2\sigma^2\tau - \frac{\lambda^{\mathbb{P}}\tau}{\gamma}\big(e^{\gamma q J} - 1\big),
$$

and, as in §18.4, $r^b = \theta(q+1) - \theta(q)$:

$$
r^{b} = s + \mu\tau - (1+2q)\frac{\gamma\sigma^2\tau}{2} - \frac{\lambda^{\mathbb{P}}\tau}{\gamma}\,e^{\gamma q J}\big(e^{\gamma J} - 1\big),
\qquad
r^{\text{res}} = s + \mu\tau - q\gamma\sigma^2\tau - \frac{\lambda^{\mathbb{P}}\tau}{\gamma}\,e^{\gamma qJ}\sinh(\gamma J). \tag{18.7}
$$

The factor $e^{\gamma qJ}$ makes the reservation price *asymmetric* in inventory. Comparing $q$ with $-q$, the long dealer's discount exceeds the short dealer's premium by $\tfrac{2\lambda^{\mathbb{P}}\tau}{\gamma}\sinh(\gamma J)\cosh(\gamma qJ)$. A long dealer fears the next bond more than a short dealer wants it.

**Small $\gamma$.** Expanding $\tfrac1\gamma e^{\gamma qJ}(e^{\gamma J}-1) = J + \gamma J^2(q + \tfrac12) + O(\gamma^2)$:

$$
r^{\text{res}} \approx s + \mu\tau - \lambda^{\mathbb{P}}J\tau - q\gamma\big(\sigma^2 + \lambda^{\mathbb{P}}J^2\big)\tau .
$$

Expected loss moves the center. Jump *variance* $\lambda^{\mathbb{P}}J^2$ adds to $\sigma^2$ in the inventory penalty, even for a dealer whose view is neutral. This is the $q\lambda J$ term promised in the Part V opener, multiplied by the $\gamma J$ that converts a loss into a fear.

**The measure question.** If the composite $s$ is already the $\mathbb{Q}$-fair mid, then $s$ is a $\mathbb{Q}$-martingale and its compensator drift is $\mu = \lambda^{\mathbb{Q}}J$. The expected-loss term becomes

$$
\mu\tau - \lambda^{\mathbb{P}}J\tau = -\big(\lambda^{\mathbb{P}} - \lambda^{\mathbb{Q}}\big)J\tau .
$$

This is the dollar value of a private read of the credit documents. If you plug CDS-implied intensities in as $\lambda^{\mathbb{P}}$, you charge the jump twice, once in the composite and once in your skew, and you never win an RFQ in a name the market is already worried about. The variance term, by contrast, needs $\lambda^{\mathbb{P}}$, because risk is borne under the physical measure.

**Random jump sizes.** For default, $J = s - 100R$ with recovery $R \sim \text{Beta}(a,b)$ (Chapter 5). Replace $e^{\gamma qJ}$ with the moment generating function $M_J(\gamma q) = \mathbb{E}[e^{\gamma q J}]$, computed by quadrature. By Jensen's inequality $M_J(\gamma q) \ge e^{\gamma q\,\mathbb{E}[J]}$, so recovery *uncertainty* costs inventory on top of expected recovery. Mags: "Price is what you pay. Recovery is what you get, eventually, after the lawyers." The MGF is how the lawyers enter the HJB.

**Inside GLFT.** The jump adds $\lambda^{\mathbb{P}}[u(s-J) - u] = \lambda^{\mathbb{P}}u(e^{\gamma qJ} - 1)$ to the HJB, and the drift adds $\mu\,\partial_s u$. Repeating §18.5 gives

$$
\dot v_q = \Big[\alpha q^2 - k\mu q + \frac{k\lambda^{\mathbb{P}}}{\gamma}\big(e^{\gamma qJ} - 1\big)\Big]v_q - \eta\big(v_{q-1} + v_{q+1}\big). \tag{18.8}
$$

The system is still linear and still symmetric. The potential is tilted toward short inventory, and its curvature at $q=0$ is $\alpha + \tfrac12 k\gamma\lambda^{\mathbb{P}}J^2$. With our numbers, jump variance contributes about eight times the diffusive curvature.

### 18.6.2 Where $\lambda^{\mathbb{P}}$ comes from: the RSSG bridge

Here Theo's old job pays rent. A dealer's $\lambda^{\mathbb{P}}$ should not be a constant. It is a *Poisson process with an appointment book*: a baseline from the default model of Chapter 6, plus bumps on scheduled dates (earnings calls, lender calls, coupon dates, maturity walls) scaled by the Priming Risk Score of Chapter 13. The 13-week cash flow model, still on its USB stick, is reborn once more as the liquidity-runway input to that score. When the PRS of a name spikes before its lender call, $\lambda^{\mathbb{P}} - \lambda^{\mathbb{Q}}$ is positive *before the market reprices*, and the bid moves for reasons the auto-quoter never saw. That is what Theo did in the cold open, in his head, in eleven seconds.

### 18.6.3 Case Study: Altice France (March 2024) and Credit Suisse AT1s (March 2023)

**Altice France, March 2024.** On its fourth-quarter 2023 results call, Altice France raised its leverage target and signaled that creditors would need to accept discounted transactions to bring leverage from roughly 6.2× toward 4×. In the session of 20 March 2024, its €1.3bn first-lien notes due 2027 reportedly fell about 21 points to around 48, their largest drop since issuance in 2020. Some of the group's bonds later traded below 30, and at least \$2bn of Altice-linked debt changed hands the following week *(approx.; as reported by BNN Bloomberg, 20 and 26 March 2024, with CreditSights and Octus commentary; CHECK against transaction data)*. Creditor groups began organizing with advisers within days.

*Autopsy.* This was a jump of about $J = 21$ points on a *first-lien* bond, with no default. A dealer long \$5mm at 69 lost about \$1.05mm overnight *(illustrative)*. Kaz's Gaussian, at 8 points a year, puts a one-day 21-point move at about 42 standard deviations, an event that happens under the normal distribution roughly never and in credit most springs. "Let's just assume Gaussian," Kaz said afterwards, as an epitaph.

*What the formula would have charged.* Into the call, take $\lambda^{\mathbb{P}}\tau = 0.10$ (a desk read of a one-in-ten chance that the call signals an LMT), $\lambda^{\mathbb{Q}}\tau = 0.03$, $J = 21$, $q = 5$, $\gamma = 0.005$, and a one-day $\tau$. Equation (18.7) moves the reservation price about 2.9 points below the composite: 1.47 points of credit view, $(0.10 - 0.03)\times 21$, and 1.46 points of jump-risk premium. That is still a long way from 21, and it should be. The engine's job was not to predict the call. It was to bid low enough to be paid for the chance, and to shrink $q$ into a scheduled event. A systematic desk would have flagged the name on three features: the calendar bump, a PRS input from the leverage-target language (Chapter 13's NLP), and Roll's estimator turning positive in the preceding days as informed sellers split orders (§18.2).

**Credit Suisse AT1s, March 2023.** On Sunday, 19 March 2023, UBS agreed to take over Credit Suisse, and FINMA ordered roughly CHF 16bn of Credit Suisse's AT1 bonds written down to zero, while shareholders received UBS shares *(approx.; widely reported)*. Litigation followed. For a market maker this is the cleanest $J = $ *everything* case: the jump took the whole price, it happened on a weekend when $A = 0$, and it inverted the textbook waterfall. Theo's first question would have been the right one: "But what does the prospectus say?" The write-down terms permitted it. Kaz's question was "Is a viability event a biology term?" In (18.7), $J$ equal to the full price makes $e^{\gamma qJ}$ enormous for any long inventory. The lesson for the GLFT dealer is (18.6): with $A \to 0$ over a weekend, the skew per lot goes to infinity. Inventory carried into a weekend is pure jump exposure, and a bond's JTD term must be priced on the *contract's* loss distribution, not the waterfall you assume.

> **Ways This Blows Up.** (1) *Double counting the measure:* $\lambda^{\mathbb{Q}}$ from CDS used as $\lambda^{\mathbb{P}}$ in the drift charges the market's fear twice. (2) *Overflow:* $e^{\gamma qJ}$ with $q = 50$ lots, $\gamma = 0.05$, and $J = 60$ is $e^{150}$. Compute in logs, cap $|q|$ at $Q$, and treat any reservation price below recovery as a hard "no bid, call a human." (3) *A constant $\lambda$:* jumps cluster on calendar dates. A flat intensity under-charges on the call date and over-charges the other 250 days, so you lose the business you should win and win the business you should lose. (4) *Gaussian recovery:* recovery is bounded on $[0,1]$ and bimodal for first liens in LMTs (Chapter 13). Use Beta, or a mixture, and integrate the MGF numerically.

### Specification for AI Implementation

This is the chapter's core inventory engine: GLFT with jump-to-default, plus exact block reservation prices.

**The Spec You Hand the Robot.** *Vague:* "add default risk to the market maker." *What ROBO built:* it multiplied σ by 1.5. *Precise:* (a) `jtd_reservation(s, q, n, sigma, gamma, tau, lam_P, J, lam_Q)` returns the frozen-inventory reservation bid and ask for a block of `n` lots, from $\theta(q)$ in §18.6.1; $\mu = \lambda^{\mathbb{Q}}J$ when `s` is a $\mathbb{Q}$-fair composite. (b) `glft_quotes` and `glft_stationary` solve (18.8) by symmetric eigendecomposition, rescaled by the smallest eigenvalue to prevent overflow, and return bid and ask distances (points from mid) per inventory level, with NaN where $v$ is numerically untrustworthy or the inventory bound forbids a side. (c) Units must be consistent: per trading day throughout the GLFT block. (d) Sanity checks: short-horizon GLFT equals AS; long-horizon GLFT equals the ground state; the ground state matches (18.6) near $q = 0$; quotes are symmetric without jumps; jumps make the dealer less eager to buy and more eager to sell; the small-$\gamma$ expansion holds; inventory asymmetry holds; and Beta-recovery quadrature matches Monte Carlo and obeys Jensen.

Altice France showed what the diffusive model leaves out, and Credit Suisse showed what it leaves out when the answer is everything. Putting the jump into the quote is not hard on paper: one extra term in the reservation price, one extra term on the diagonal of a matrix. The trouble is that the desk needs two products from the same ingredients. A client has just asked for a bid on eight lots, and the platform timer is running. The streaming engine, meanwhile, needs a table of quotes for every inventory level from short twenty to long twenty, refreshed whenever volatility or the jump view moves. Both are linear algebra on the same parameters, and both fail quietly when the units disagree. So they share a listing.

Listing 18.4 has two halves. The first is the block pricer. `jtd_reservation` evaluates $\theta(q)$ from §18.6.1, with drift, diffusion penalty, and the jump term computed by `expm1`, falling back to the linear limit when $\gamma$ is negligible. It returns the average price per lot for buying `n` more lots, $[\theta(q+n)-\theta(q)]/n$, and for selling `n`, $[\theta(q)-\theta(q-n)]/n$. That prices the block against current inventory, not the marginal lot. `jump_mgf_beta` handles uncertain recovery by integrating $e^{uJ}$ against a Beta density, with $J = s - 100R$.

The second half is the streaming engine. `glft_matrix` builds the tridiagonal matrix of (18.8) on a grid from $-Q$ to $Q$. The diagonal carries the diffusive curvature, the drift tilt, and, if an intensity is supplied, the jump potential. The off-diagonals are $-\eta$. `glft_quotes` computes $e^{-M\tau}\mathbf 1$ by symmetric eigendecomposition, subtracting the smallest eigenvalue first so nothing overflows. `glft_stationary` takes the lowest eigenvector instead, the $\tau \to \infty$ limit. Both feed `_quotes_from_logv`, which turns log ratios of neighbouring inventories into bid and ask distances, adds the `as_greed` markup from Listing 18.3, and leaves `NaN` where the limit forbids a side or `_safe_log` finds $v$ below $10^{-12}$ of its maximum.

The tests mirror the spec. Short horizons reproduce AS, long ones match the ground state, the effective horizon comes out near 13 trading days, quotes are symmetric without jumps, and jumps push the bid away and the ask in. The 8-lot bid of 90.5716 used in §18.7 is pinned, along with the small-$\gamma$ expansion, the long-versus-short asymmetry, and quadrature against Monte Carlo, with Jensen's inequality checked.

Use the pricer for a block at one instant and the matrix for streaming quotes under a hard limit. Neither scales to thousands of bonds. The edge case that bites is `lam_Q`. Its default of zero does not mean "no credit view." It means no compensator drift, so with a $\mathbb{Q}$-fair composite you must pass $\lambda^{\mathbb{Q}}$ or the function charges the market's own expected loss a second time. Intensities must also be rates in the same time unit as $\tau$: the block test passes a horizon probability divided by the horizon, not the probability itself.

*The full listing is [Listing 18.4 in Appendix F](#code-18-4).*

## 18.7 RFQ Hit Rates and the Price of Staying at the Table

An RFQ is not a limit order book. You do not sit at a price and wait. You answer one auction and either win or lose. Replace $\Lambda(\delta)$ with a **win curve**. Let $x = s - p^b$ be the bid's distance below the composite:

$$
P(x) = \frac{1}{1 + \exp\!\big(-(\beta_0 - \beta_1 x + \boldsymbol\beta_z^{\top}\mathbf z)\big)},
$$

where $\mathbf z$ holds the number of dealers in competition, size, client tier, protocol, and time of day. Fit it by maximum likelihood on the desk's own RFQ log, including the losses and their covers.

**The markup.** Equation (18.2) applies directly, because $P'/P = -\beta_1(1-P)$. For a block of $n$ lots, the utility gain from a win scales by $n$, so

$$
\text{greed}(x) = \frac{1}{\gamma n}\ln\!\Big(1 + \frac{\gamma n}{\beta_1(1-P(x))}\Big) \;\xrightarrow{\;\gamma\to0\;}\; \frac{1}{\beta_1(1-P(x))}.
$$

When winning is unlikely ($P \to 0$) this is the exponential case with $k = \beta_1$. When you are the favorite, the markup rises, because you have pricing power.

**Suspicion, conditional on winning.** Let $a_c$ be the expected *residual* markout from client tier $c$, conditional on winning. Conditioning on winning matters: you win when you are the most optimistic of $n$ dealers, which is exactly when the client's information is most likely against you (§18.9 does the arithmetic). Strip factor beta, carry, and index and ETF effects first, and count only the residual as toxicity. That is "IDO or it didn't happen," applied to markouts.

**Franchise.** Clients route flow to dealers who answer and sometimes win, so desks run a hit-ratio target $h^*$. Maximize expected profit subject to $\mathbb{E}[P] \ge h^*$, with multiplier $\nu \ge 0$. The Lagrangian adds $\nu P(x)$ to each RFQ's objective, and the first-order condition becomes

$$
x^* = d - \nu + \text{greed}(x^*), \qquad d = (s - r^b) + a_c .
$$

The hit-ratio constraint is a *subsidy*: you quote as if your reservation price were $\nu$ points better. Barzykin & Ciceri (2026), "Bond Market Making with a Hit-Ratio Target" (arXiv 2604.20406), formalize this on a size ladder. "Dualizing the hit ratio target term" keeps the HJB separable, and the linearized quotes decompose into "riskless spread, inventory-risk correction, and hit-ratio correction." Niang (2026), "Quality-Adjusted Hit-Ratio Targeting in Corporate Bond Market Making" (arXiv 2605.30643), shows in synthetic simulations that *raw* hit-ratio targeting subsidizes toxic flow, and replaces it with a hit ratio adjusted for residual quality. The quotes then gain a credit-alpha skew and a residual-toxicity charge.

**The market maker's equation.** Putting §18.4–§18.7 together, the bid on a client-sell RFQ of $n$ lots is

$$
p^{b} = s
- \underbrace{(\lambda^{\mathbb{P}}-\lambda^{\mathbb{Q}})J\tau}_{\text{credit view}}
- \underbrace{\big[(s - r^b_n) - (\lambda^{\mathbb{P}}-\lambda^{\mathbb{Q}})J\tau\big]}_{\text{fear (diffusive + jump)}}
- \underbrace{a_c}_{\text{suspicion}}
- \underbrace{\tfrac{1}{\gamma n}\ln\!\big(1 + \tfrac{\gamma n}{\beta_1(1-P)}\big)}_{\text{greed}}
+ \underbrace{\nu}_{\text{franchise}}, \tag{18.9}
$$

with $r^b_n = [\theta(q+n) - \theta(q)]/n$ from §18.6. The result is then rounded to the tick, because the guild insists.

**The cold open, solved.** Take $s = 91.25$, $q = 3$, $n = 8$, $\sigma = 8$, $\gamma = 0.005$, $\tau = 5/252$, $J = 20$, $\lambda^{\mathbb{P}}\tau = 0.025$ (Theo's read of the noon call), $\lambda^{\mathbb{Q}}\tau = 0.02$, $a_c = 0.15$, $\nu = 0.05$, $\beta_0 = 0$, $\beta_1 = 4$ *(all illustrative)*.

| Term | Points | Comment |
| :--- | ---: | :--- |
| Credit view | 0.10 | $(0.025-0.02)\times 20$ |
| Fear | 0.58 | 0.04 diffusive (block of 8, not 1) + 0.53 jump premium |
| Suspicion | 0.15 | residual markout, this client, pre-call |
| Greed | 0.25 | win probability ≈ 1.6% |
| Franchise | −0.05 | hit-ratio subsidy |
| **Bid** | **90.22 → 90.25** | Ines's number |

Kaz's 90.875 priced 0.355 points of the 1.03 points. Ines priced all of it, rounded to the eighth.

> **Poker Table: Ines's hand history.** The bond printed 86 twenty minutes later. *Kaz's 90.875* would have beaten the 90.50 cover and bought \$8mm at a markout of −4.875 points: **−\$390,000**. *The 90.50 cover* won and paid −\$360,000. *Ines's 90.25* lost and paid nothing. "Losing that hand was the best trade of the day," she says. "The equation said we'd win one time in sixty. The table said someone else wanted to pay for the lesson. Let them."

> **Trend Watch: the auto-quoting arms race (2021–2026).** *What changed:* the RFQ win curve is now fitted by machines on both sides. *How big:* Tradeweb's AiEX handled more than 40% of its institutional trades in 2025, against 30% in 2021 (Tradeweb 10-K, FY2025). MarketAxess dealer algorithmic responses rose from 32.5m (2023) to 40.9m (2024), and the number of clients using automated solutions went 204, 245, 261 over 2023–25 (MarketAxess 10-Ks). Coalition Greenwich (June 2024) put about 30% of dealer volume at no human touch, 57% at top-tier dealers and 70% at non-bank LPs, on about 30,000 inquiries a day (as summarized in our Chapter 3 brief). Trumid executed 88% of eligible RFQ line items fully no-touch in September 2025 (The DESK, 2025-10-08). A Q3-2024 Barclays survey found 60% of credit participants using auto-execution, up from 40% (The DESK, 2025-01-16). In October 2026, Vanguard reported about 70% of traded volume automated but nothing sent without a trader, while buy-side traders said ELPs "help mainly in normal markets" (The DESK, October 2026). Citadel Securities proposed LP reliability metrics (non-quote rates, market share, execution cost savings, hit rates, risk executed) and self-reported a 14.2% share of IG block risk transfer (The DESK, 2026-10-08; self-reported). *What it means:* competition raises $\beta_1$, so greed falls. In stress, auto-quoters switch to wider parameters or switch off, $\beta_1$ collapses, and greed returns, along with the 64% spread spike of March 2026 (§18.2). Hit rate, the metric Citadel wants published, is exactly the variable Niang warns you not to target raw.

### Specification for AI Implementation (win curve, hit-ratio dual, quote assembly)

The table above is one RFQ, solved by hand over a page. The desk gets thousands a day, each with its own size, client, and distance to the composite, and each needs an answer inside the platform's timer. Three pieces have to be automated, and they lean on each other. The win curve must be fitted from the desk's own log. The quote must be solved against that fitted curve, not the textbook exponential. And the hit-ratio target that sales keeps asking about must be enforced without handing free money to the clients who know the most.

Listing 18.5 builds this in four steps. `win_prob` is the logistic curve of §18.7 in the distance `x`, composite minus bid in points. `fit_win_curve` estimates its two coefficients by maximum likelihood on the RFQ log, writing the negative log likelihood with `logaddexp` for numerical stability and handing it to BFGS. `markup` is equation (18.2) for this curve and a block of $n$ lots, with the $\gamma \to 0$ limit built in. Because the markup depends on the win probability, which depends on the distance, `optimal_distance` solves the fixed point $x = d - \nu + \text{markup}(x)$ by bisection, over arrays of RFQs at once. The markup falls as $x$ rises, so the root is unique.

`rfq_bid` then assembles (18.9). It takes the block reservation bid from Listing 18.4, computes the credit view as $(\lambda^{\mathbb{P}}-\lambda^{\mathbb{Q}})J\tau$, calls the rest of the gap between mid and reservation price fear, adds the suspicion charge to the distance, solves for $x$, and returns the five terms, the bid, the tick-rounded bid, and the probability of winning.

The tests make three claims. A fit on 20,000 simulated RFQs recovers the planted coefficients, 0.3 and 4.0. The cold open comes out at 90.219, rounds to 90.25, wins under 3 percent of the time, and its five terms sum exactly to mid minus bid. The last block is Niang's argument in miniature. In a 4,000-RFQ book with 30 percent toxic flow, one multiplier is tuned so that the raw hit ratio is exactly 25 percent. Then the subsidy is removed on the toxic flow only. Clean flow is priced identically, expected margin over the reservation price rises, and the toxic share of wins falls, though the overall hit ratio lands below 25 percent. That shortfall is the price of not paying for information.

Use it per RFQ, with a curve fitted on the right segment: dealer count, size, client tier. The edge case that bites is the log itself. `fit_win_curve` assumes both outcomes appear. A log built from fills alone has `won` equal to one everywhere, the likelihood has no maximum, and BFGS marches the intercept off toward infinity without complaint. Perfect separation by distance does the same. Nothing in the listing checks that the fitted slope is positive, so the caller must.

*The full listing is [Listing 18.5 in Appendix F](#code-18-5).*

## 18.8 Decoding TRACE

TRACE is not a tape. It is a censored, lagged, double-counted ledger with a rulebook, and the rulebook is data. What a decoder must know (FINRA rules and notices, as of October 2026):

- **What prints.** Rule 6750 disseminates TRACE-eligible transactions, 144A included, "immediately upon receipt," with listed exclusions such as affiliate-principal-indicator trades and list or fixed-offering-price transactions.
- **Caps.** Sizes over \$5mm (IG) and \$1mm (HY) display as "5MM+" and "1MM+". Uncapped sizes reach the Historic Corporate Bond Data Set "six months after the calendar quarter in which the transactions are reported" (Regulatory Notice 25-17).
- **Clock.** The 15-minute outer limit survives. FINRA is "not moving forward" with one-minute reporting (RN 25-17).
- **Flags.** The portfolio-trade modifier has been mandatory since 15 May 2023 (RN 22-12). Optional aggregate allocation reports started on 8 June 2026 (RN 25-17). The expanded affiliate indicator is voluntary from 31 August 2026 and mandatory from 2 August 2027 (RN 26-16), because duplicate affiliate prints inflated US HG volume by up to 8% in June 2026 (MarketAxess Q2-2026 release).
- **Academic TRACE** masks dealer identities but keeps them consistent, which is what lets researchers study dealer inventories at all.

> **[SOURCE EXTRACTION]** *Ben_Dor_Quantitative_Credit_Portfolio_Management p.364, n.8:* "TRACE truncates the sizes of large transactions at \$1 million and \$5 million for high-yield and investment-grade bonds, respectively"
>
> **Annotation.** Our analysis: the footnote goes on to impute the average true size of capped prints by matching aggregate volume, about \$4mm for HY and \$12.5mm for IG, and to drop trades under \$100k to focus on institutions. Two lessons follow for 2026. First, the cap is a feature, not just a nuisance: a "1MM+" print in a HY bond is a block indicator, and blocks are where Kyle's $\lambda^{K}$ lives. Second, any real-time imbalance computed on capped sizes understates block flow. Carry a capped-share feature, and rebuild the uncapped history quarterly once FINRA's six-month lag expires. The caps in the footnote are the same caps in force in 2026.

**Pipeline.** Apply cancels and corrections by message sequence. Keep one leg of each interdealer trade. Flag capped sizes, portfolio-trade and ATS prints. Emit per-bond features: customer imbalance, capped share, PT share, ATS share, and minutes since the last print. Reading informed flow then becomes concrete. In the Altice week (§18.6), the features to watch were a one-sided customer imbalance, a jump in capped share, and Roll turning positive.

> **Ways This Blows Up.** Corrections applied before the trades they correct; agency and riskless-principal pairs counted as two trades; affiliate duplicates counted as volume (up to 8% in June 2026); the Dick-Nielsen cleaning steps (Dick-Nielsen 2009, "Liquidity Biases in TRACE"; Dick-Nielsen 2014, "How to Clean Enhanced TRACE Data") applied to a 2026 file without the new flags; and "processed" platform volume mistaken for executed risk.

### Specification for AI Implementation (TRACE decoder)

Schema (one row per report): `msg_seq` int, `orig_msg_seq` int (−1 if none), `status` in {T, X, C}, `bond_id` str (internal id, never an invented CUSIP), `rating_class` in {IG, HY}, `minute` int, `price` float (points), `reported_qty` float (USD mm, capped), `side` in {B, S} (reporting dealer's view), `contra` in {C, D}, `ats` bool, `pt` bool.

Every shop that uses TRACE has a version of the same week: someone builds a flow feature, the volume does not tie to the vendor, and four days later the cause turns out to be a correction applied to the wrong trade, or two dealers' reports of one trade counted as two. The rulebook above is easy to read and tedious to obey, and the cost of getting it wrong is silent, because a feature built on dirty prints still looks like a number. The way to stop relitigating it is to write the decoder once, feed it a file where the right answer is known, and make it prove it can recover that answer before it touches the real feed.

Listing 18.6 does both jobs, and the test file comes first. `make_synthetic_trace` draws 400 trades across eight placeholder bonds, four IG and four HY, with lognormal sizes, a 70/30 customer-to-dealer mix, and small shares of ATS and portfolio-trade prints. It expands each trade into the reports a dealer would file: one for a customer trade, two for an interdealer trade. Sizes are capped at \$5mm for IG and \$1mm for HY. It then corrupts the file in the two ways the pipeline names. Twenty reports are duplicated by mistake, and each duplicate is followed by a cancel pointing at it. Twenty originals are mispriced by a point and followed by a correction carrying the right price.

`clean_trace` is the pipeline in four lines. It collects every message sequence number that a cancel or correction refers to, drops the cancel records and everything they referenced, and keeps the corrections as the replacements. It then keeps only the sell-side leg of interdealer trades, flags prints at the cap, and sorts by bond, minute, and sequence. `trace_features` turns the clean file into one row per bond: customer imbalance from the dealer's side flag, the capped, portfolio-trade, and ATS shares, the print count, and minutes since the last print against a 390-minute session.

The tests ask that one row survive per true trade, that prices equal the true prices, that no size exceeds its cap, and that imbalance stays between minus one and one.

Use it as the skeleton of a daily decoder, not as the decoder. The edge case that bites is that it passes only the messes it was taught. Dropping the buy-side leg assumes the sell-side leg is also in the file. Where it is missing, the trade vanishes from volume entirely. The synthetic file has no riskless-principal pairs or affiliate duplicates either, so the equality of row counts proves the logic, not the feed. Imbalance is also computed on capped sizes, so it is blind to blocks, which is why `capped_share` travels beside it.

*The full listing is [Listing 18.6 in Appendix F](#code-18-6).*

## 18.9 BWICs: First-Price Auctions With a Leaky List

A bid-wanted-in-competition is the RFQ turned inside out. The seller circulates a list, dealers and investors submit sealed bids by a deadline, the best bid wins, and the market later learns the "cover" (second-best bid) or "DNT" (did not trade). Saunders, Srinivasan & Walter (1998), in a field study of the US inter-dealer corporate bond market (NYU Stern FIN-98-089), found that trading "closely resembles a first-price sealed-bid auction," and measured competition as the gap between the best and second-best bid. Mags has a shorter version: "A BWIC is a lender call where everyone talks at once and nobody says anything."

**The winner's curse, derived.** Bidder $i$ sees a signal $x_i = V + \varepsilon_i$ with $\varepsilon_i \sim \mathcal N(0,\sigma_\varepsilon^2)$ i.i.d. and a diffuse prior on $V$. Conditional on $x_i = x$, $V \sim \mathcal N(x,\sigma_\varepsilon^2)$. Conditional also on $x_i$ being the highest of $n$ signals, the posterior density of $\varepsilon_i = x - V$ is proportional to $\phi(\varepsilon/\sigma_\varepsilon)\,\Phi(\varepsilon/\sigma_\varepsilon)^{n-1}$, which is the density of $\sigma_\varepsilon$ times the maximum of $n$ standard normals. So

$$
\mathbb{E}[V \mid x_i = x,\ i \text{ wins}] = x - \sigma_\varepsilon\, e_n, \qquad e_n = \int_{-\infty}^{\infty} z\, n\,\phi(z)\Phi(z)^{n-1}\,dz,
$$

with $e_3 \approx 0.85$, $e_5 \approx 1.16$, and $e_8 \approx 1.42$. With $\sigma_\varepsilon = 1$ point, an eight-bidder list requires about 1.4 points of shading *before* strategic shading (Milgrom & Weber 1982, "A Theory of Auctions and Competitive Bidding"). The correction grows with $n$, which is why quotes get more conservative as more dealers are asked (§18.3).

**Leakage.** Once the list circulates, anyone who sees it is an order anticipator. If they pre-sell a fraction $\phi$ of the expected flow $Q\,p_{\text{trade}}$, Kyle's impact gives a pre-auction drift of $\Delta P = -\lambda^{K}\phi\,p_{\text{trade}}\,Q$, which the seller pays on the whole list. A \$300mm list with $p_{\text{trade}} = 0.9$, $\phi = 0.3$, and $\lambda^{K} = 0.5$ points per \$100mm drifts about 0.4 points and costs about \$1.2mm *(illustrative)*. A DNT reveals that the reserve was above the best bid, which is a reserve-price signal. BWIC prints are survivors: in stress the bonds that fail reserves are the weak ones, so marks built from BWIC covers are biased upward precisely when it matters.

### 18.9.1 Case Study: The LDI BWIC Week, October 2022

> **Trend Watch: BWIC supply, 2021–2026.** *2021:* total BWIC volume averaged \$5.2bn a quarter; *Q2-2022:* \$6.8bn, with CLOs 55% of volume (TwentyFour AM, 2022-07-11). *Late September 2022:* the UK mini-Budget triggered the gilt and LDI crisis, and the Bank of England began temporary long-gilt purchases on 28 September. *The following week:* more than €1.5bn of CLOs were listed via BWICs, with perhaps another €1bn traded away from the broader market; one Tuesday alone saw about €400m listed, predominantly AA. "Sales over the past week-and-a-half could exceed the previous three months combined." Almost all AAA and AA paper traded, while many BB and B bonds "didn't meet reserves." AA cash prices were "in the 80s," and LDI funds "had no choice but to sell" (TwentyFour AM, 2022-10-05). *2025–2026:* 9fin (2025-12-02) reported an insurer listing more than \$1bn of triple-A US CLOs in a single BWIC, and SCI (2026-02-16) headlined a \$56bn twelve-month US BSL CLO BWIC total led by triple-A supply *(headline-level; period CHECK)*. *What it means:* the BWIC is now a primary liquidity venue for structured credit, and its leak rate is a cost line.

*Autopsy.* LDI holders were Harris's purest utilitarian sellers: forced, uninformed about collateral, and on a margin clock. That should mean low suspicion, so $a_c \approx 0$. The winner's curse was mild for AAA (small $\sigma_\varepsilon$) and severe for BB (large $\sigma_\varepsilon$, few bidders, failed reserves). Leakage was enormous, because every list told the street that more lists were coming. A systematic desk would have read the ETF and gilt stress as an exogenous-seller regime and set $\nu > 0$ for that client tier: win the forced flow, at prices where the "cost of trading [was] rising every few hours." Survivorship bias would then have flattered the BB marks drawn from those prints.

### Specification for AI Implementation (BWIC shading and leakage)

The shading constant $e_n$ and the leakage bill are the two numbers a BWIC desk wants on screen before it bids, and neither deserves trust until it has been checked against something other than itself. Listing 18.7 integrates the expected maximum of $n$ standard normals numerically and tests it against the closed form $3/(2\sqrt{\pi})$ for three bidders and a Monte Carlo draw for eight, then computes the pre-auction drift and the seller's cost, reproducing the \$300mm example above to the decimal (0.405 points, \$1.215mm).

*The full listing is [Listing 18.7 in Appendix F](#code-18-7).*

## 18.10 Desk Debrief

- **A quote is five numbers, not one:** credit view, fear, suspicion, greed, and franchise. Equation (18.9) on one line. If you can't name all five, you priced one.
- **In bonds, diffusive fear is pennies.** The AS spread is mostly greed, $\tfrac2\gamma\ln(1+\gamma/k) \to 2/k$. The real fear is the jump term $\lambda^{\mathbb{P}}J^2$ and the factor $e^{\gamma qJ}$.
- **Charge the jump once.** Use $(\lambda^{\mathbb{P}} - \lambda^{\mathbb{Q}})J\tau$ against a $\mathbb{Q}$-fair composite, and $\lambda^{\mathbb{P}}$ for the variance. A CDS-implied $\lambda$ in the drift charges the market's fear twice.
- **There is no 4 p.m. in credit.** Use the stationary GLFT dealer. Its effective horizon is the inverse spectral gap, it shrinks like $A^{-1/2}$, and it goes to infinity on Friday night.
- **Roll returning NaN is information.** A positive autocovariance means split orders or informed drift. Never take an absolute value.
- **Hit ratios are a subsidy, and raw ones subsidize the wrong people.** Target quality-adjusted hit ratios on residual markouts. IDO or it didn't happen.
- **TRACE's censoring is the signal.** "5MM+" and "1MM+" are block flags; the six-month uncapped release is your quarterly recalibration.
- **A BWIC is a first-price auction with a leak.** Shade by $\sigma_\varepsilon e_n$, price the leak with $\lambda^{K}$, and distrust survivor marks.

**The Spec You Hand the Robot.** *Vague:* "Build an RFQ auto-quoter." *What ROBO built:* it maximized the hit ratio, bid par for everything, and owned the bond market by Thursday. *Precise:* Build `rfq_engine.quote(rfq, state) -> Quote`. **Inputs:** `rfq` = {bond_id, side, size_lots, n_dealers, client_tier, protocol, timer_s}; `state` = {composite_mid (points, $\mathbb{Q}$-fair), inventory_lots, sigma_pts_per_sqrt_yr (20-day $\mathbb{P}$ forecast), gamma_per_pt_lot, holding_tau_yr, lam_P_per_yr (baseline + event calendar × PRS), lam_Q_per_yr (CDS/composite-implied), jump_pts or recovery Beta(a, b), a_tox_pts[client_tier] (residual markout conditional on win), win-curve coefficients, nu_pts[client_tier] (quality-adjusted hit-ratio dual), tick}. **Computation:** block reservation price from $\theta(q)$ (§18.6) in logs; the markup from (18.2) with the logistic curve; the five terms of (18.9); round to tick. **Guards:** no quote if the reservation price is below recovery or $|q + n| > Q$; clip to composite ± band; widen or stop when the stress regime is on (ETF discount z-score, bid–ask percentile); stop a session when realized markouts breach 3σ of their forecast. **Logs (the hand history):** every term, $P(\text{win})$, the cover when lost, and 1/5/20-day IDO markouts. **Tests:** the asserts in this chapter, plus one that raw hit-ratio targeting fails on a synthetic toxic tier.

**Exercises**

1. Show that $\tfrac1\gamma\ln(1+\gamma/k) \to 1/k$ as $\gamma \to 0$, and that $1/k$ maximizes $\delta Ae^{-k\delta}$. Explain to Kaz why a risk-neutral dealer still has a spread.
2. Re-derive (18.7) with $J = s - 100R$, $R \sim \text{Beta}(a,b)$. Show that the MGF $M_J(\gamma q)$ replaces $e^{\gamma qJ}$, and use Jensen to sign the effect of recovery uncertainty on the bid.
3. On a TRACE extract with "5MM+" caps, estimate the Roll spread by size bucket ($<$\$100k, \$100k–\$1mm, \$1–5mm, capped). Which buckets return NaN, and why does order splitting make the capped bucket's estimate *too small*?
4. Compute the winner's-curse shading for a 3-dealer versus an 8-dealer BWIC with $\sigma_\varepsilon = 0.75$ points. Then argue whether the *equilibrium* bid rises or falls with $n$.
5. ROBO has been told to "maximize the hit ratio." Describe its inventory one week later, its markouts, and the email from risk. Then write the one-line constraint that fixes it.
6. Using `glft_stationary`, find the $A$ at which a dealer's stationary skew per lot equals the AS skew with a one-week horizon. Interpret the answer as "how often must this bond be asked about for AS to be right?"

### Deep-Dive Resource Graph

**Podcasts**
- *Bloomberg Odd Lots* (Joe Weisenthal and Tracy Alloway): search the archive for its episodes on corporate-bond market structure, portfolio trading, and credit ETFs.
- *Flirting with Models* (Corey Hoffstein): systematic-investing practitioners on execution and transaction costs.

**Practitioner Writing**
- The DESK: "Dealers struggle to unpick impact of runs sent to rivals" (2023-12-07); "Measuring implicit costs and market impact in credit trading" (2024-10-23); "IG credit dealers go short before Fed cuts" (2024-11-20); Citadel Securities LP-metrics coverage (2026-10-08); Vanguard automation (https://www.fi-desk.com/fils-europe-vanguard-automates-70-of-trades-others-urge-caution/).
- Hedgeweek, "Banks turn net short corporate bonds for first time as market structure shifts" (2026-07-13).
- TwentyFour AM, "Liquidity is expensive, but it's there" (2022-07-11) and "Where are CLOs trading after the Truss Tantrum?" (2022-10-05).
- Matt Levine, *Money Stuff* (Bloomberg Opinion), on bond market structure and the Credit Suisse AT1 write-down.
- Barclays (Dynkin et al.) and Ben Dor et al. on Liquidity Cost Scores (shelf: Dynkin p.702, Ben_Dor p.120–123).

**Academic Papers**
- Roll (1984), *JF* 39(4) (https://doi.org/10.1111/j.1540-6261.1984.tb03897.x); Glosten & Milgrom (1985), *JFE* 14(1) (https://doi.org/10.1016/0304-405X(85)90044-3); Kyle (1985), *Econometrica* 53(6) (https://doi.org/10.2307/1913210); Ho & Stoll (1981), *JFE* 9(1) (https://doi.org/10.1016/0304-405X(81)90020-9).
- Avellaneda & Stoikov (2008), *Quantitative Finance* 8(3) (https://doi.org/10.1080/14697680701381228); Guéant, Lehalle & Fernandez-Tapia (2013) (https://arxiv.org/abs/1105.3115); Guéant (2017) (https://arxiv.org/abs/1605.01862); Guéant & Manziuk (2019) (https://arxiv.org/abs/1910.13205); Cartea, Jaimungal & Penalva (2015), *Algorithmic and High-Frequency Trading* (Cambridge UP).
- Fermanian, Guéant & Pu (2017) (https://arxiv.org/abs/1511.07773); Barzykin & Ciceri (2026) (https://arxiv.org/abs/2604.20406); Niang (2026) (https://arxiv.org/abs/2605.30643); Guo, Lehalle & Xu (2021) (https://arxiv.org/abs/1903.09140).
- Bao, Pan & Wang (2011), *JF* 66(3) (https://doi.org/10.1111/j.1540-6261.2011.01655.x); Edwards, Harris & Piwowar (2007) (https://doi.org/10.1111/j.1540-6261.2007.01240.x); Goldstein, Hotchkiss & Sirri (2007) (https://doi.org/10.1093/rfs/hhl020); Hendershott & Madhavan (2015) (https://doi.org/10.1111/jofi.12164); Kargar et al. (2021), NBER WP 27355; Choi, Huh & Shin (2024) (https://doi.org/10.1287/mnsc.2022.4646); O'Hara & Zhou (2021), "The electronic evolution of corporate bond dealers" (https://doi.org/10.1016/j.jfineco.2021.01.001); Bessembinder, Spatt & Venkataraman (2020) (https://doi.org/10.1017/S0022109019000231); Saunders, Srinivasan & Walter (1998), NYU Stern FIN-98-089; Milgrom & Weber (1982), "A Theory of Auctions and Competitive Bidding"; Harris (2003), *Trading and Exchanges* (Oxford UP).

**Data & Code**
- FINRA TRACE hub (https://www.finra.org/filing-reporting/trace): End-of-Day file, Academic Corporate Bond TRACE, Historic TRACE, Fact Book; Regulatory Notices 22-12, 25-17, 26-16; Rule 6750.
- NY Fed Primary Dealer Statistics (weekly dealer positions; Trend Watch §18.5).
- SEC EDGAR (https://www.sec.gov/edgar) for MarketAxess and Tradeweb 10-K automation statistics.
- Dick-Nielsen (2009, 2014), TRACE cleaning procedures (title only; SSRN).

<!-- STATUS: COMPLETE -->
