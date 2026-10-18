# Chapter 28: What a Desk Head / Senior PM Must Know to Extract Maximum Alpha


## 28.0 Cold Open: The Keys to the Table

Thursday, 15 October 2026, 4:05 p.m. The ICE BofA US High Yield index has closed at an option-adjusted spread of 323 bp. Its CCC-and-lower subindex has closed at 1,278 bp, a day after its widest level in at least three years (FRED). The index looks bored. Its basement is on fire.

Ines drops a lanyard on Theo's keyboard. It says RISK, in a font chosen by Compliance.

"You're not an analyst anymore. You have four PMs, a \$2bn gross book, and a risk officer who marks to bid. What's the pot?"

Theo starts to say "two billion," hears how wrong it is on the way out, and stops. Ines nods. It is the first good thing he has done as a desk head.

Kaz rolls over with a laptop. "I ran Kelly on the book. Good news: it's very confident. It wants 93% of capital in one B3 name."

"Which name?"

"The one with the fattest spread."

Mags, from the corner, without looking up: "Back in my day the stop-loss was a phone call from the CFO. You could hear the drawdown in his breathing."

ROBO has posted to the desk channel. Asked last night to "maximize the book's Sharpe ratio," it has found the highest-Sharpe asset in the building: a 2027 IG bond whose matrix-priced mark has not moved in eleven weeks, because nobody has traded it. Realized volatility 0.4%, Sharpe 11. ROBO proposes moving the whole book into it. The arithmetic is fine. The volatility has not gone away. It is sitting in the mark, waiting for the first trade.

Theo puts his hand on the USB stick with the 13-week cash flow model on it, for emotional support, and asks the only question he trusts. "But what does the credit agreement say?"

"There isn't one," says Ines. "That's the job. You write it. How much risk, in which horizon, in which names, for how long, and with whom?"

By the end of this chapter you will be able to: set a leverage band for a credit book from its effective breadth, its DTS-scaled volatility and its liquidity cost; put each signal in the horizon and instrument tier where it survives its own transaction costs; size a default bet with Kelly when the bet has a jump, a recovery and a ruin boundary; compute liquidity-adjusted VaR and days-to-liquidate for a book of RFQ-traded bonds; run a drawdown rule you can defend, with the mark-to-bid shock budgeted inside the rule rather than discovered on top of it; and build a team whose breadth survives contact with its own hit rate.

## 28.1 Risk, Not Capital: The Desk Head's Accounting Identity

Theo's first instinct, inherited from four years of sources-and-uses tables, is to hand out dollars: \$500mm of gross to each of his four PMs, done by lunch. It is the wrong unit. A PM cannot spend dollars. A PM can only spend risk: volatility while the position is alive, drawdown when it goes wrong, and liquidity when it has to be sold. Dollars are what you get when you divide a risk budget by how risky the instrument is, and in credit that divisor changes by a factor of ten between a three-year A-rated bond and a CCC with a lender call on Monday.

> **[SOURCE EXTRACTION]** *Paleologo_Advanced_Portfolio_Management p.88:* "Return on GMV is performance relative to a capital budget. But the real scarce resource is not capital; it is risk."
>
> **Annotation.** Paleologo writes this for an equity long/short book, where it is already true. In credit it is truer, for two reasons. First, the dollar size of a position is a poor proxy for its risk, because a bond's volatility scales with its spread and its spread duration (DTS), so \$50mm of a 5-year BB and \$50mm of a 2-year CCC are different animals that happen to weigh the same. Second, credit has a third risk budget the equity book barely notices, which is liquidity: the cost and the time of getting out. A 2026 desk head allocates three numbers per PM (a volatility budget, a drawdown budget, and a liquidity budget expressed in days-to-liquidate and liquidation cost) and lets the dollars fall out. The rest of this chapter computes each of the three.

> **Desk Myth vs. Desk Reality.** *Myth:* "We allocate \$200mm to the HY PM." *Reality:* "We allocate the HY PM 6% annualized volatility on \$200mm of allocated capital, which is \$12mm of vol, a 7.5% drawdown limit, which is \$15mm, and no more than 20% of the book beyond 20 days to liquidate *(all illustrative)*. The \$200mm is the denominator the investor letter prints."

### The identity, and why credit needs three substitutions

A notational warning first. Paleologo writes $s$ for the Sharpe ratio and $L$ for leverage. In this book $s$ is a credit spread and $L = 1 - R$ is loss given default, and both letters are busy in this chapter. We write $\text{SR}$ for the book's Sharpe ratio and $G$ for gross leverage, $G = \text{GMV}/\text{NAV}$, and use these throughout.

Let the book have net asset value (allocated capital) $K$ and gross market value $\text{GMV} = G K$. Split the GMV into $N$ positions with GMV shares $w_i$, $\sum_i |w_i| = 1$. Let $\sigma_i$ be the annualized idiosyncratic volatility of position $i$, as a fraction of its market value. If the $N$ bets are independent and equal, $w_i = 1/N$ and $\sigma_i = \sigma$, the volatility of the book per dollar of GMV is

$$
\sigma_{\text{GMV}} = \sqrt{\sum_{i=1}^{N} w_i^2 \sigma_i^2} = \frac{\sigma}{\sqrt{N}}.
$$

The book earns its Sharpe ratio on that volatility, so its return on GMV is $\text{SR}\,\sigma/\sqrt{N}$, and its return on NAV is $G$ times that:

$$
r_{\text{NAV}} = G \cdot \text{SR} \cdot \frac{\sigma}{\sqrt{N}}. \tag{28.1}
$$

This is Paleologo's equation (10.1) in our letters. Rearranged, a desk that must earn at least $r_{\min}$ on NAV needs leverage of at least

$$
G \;\ge\; \frac{\sqrt{N}}{\sigma}\cdot\frac{r_{\min}}{\text{SR}}. \tag{28.2}
$$

Read (28.2) as a sentence: a well-diversified book of low-volatility bets needs a lot of leverage to pay anyone's salary. Diversification lowers the risk per dollar of GMV, and so it lowers the return per dollar of GMV, and the only way to earn the hurdle is to own more GMV. That is why the platforms run what they run (see the Trend Watch below), and why the ceiling on $G$ in §28.7 matters more than the floor.

Credit forces three substitutions into (28.1)–(28.2). Each gets a section.

1. **$\sigma \to \sigma_{\text{DTS}}$.** A bond's excess return over a short horizon is approximately $-D^{\text{spr}}_i\,\Delta s_i = -D^{\text{spr}}_i s_i\,(\Delta s_i/s_i)$. If relative spread changes $\Delta s_i/s_i$ have annualized volatility $\sigma_{\text{rel}}$, then

$$
\sigma_i \approx D^{\text{spr}}_i\, s_i\, \sigma_{\text{rel}} = \text{DTS}_i \cdot \sigma_{\text{rel}}.
$$

This is the empirical regularity of Ben Dor et al., below: the volatility of a bond scales with its DTS, not with its duration or its spread alone. A 5-year HY bond at 350 bp has $D^{\text{spr}} \approx 4.2$ years and $s = 0.035$, so $\text{DTS} \approx 0.147$; at $\sigma_{\text{rel}} = 0.35$ a year *(illustrative)*, $\sigma_i \approx 5.1\%$ of market value per year.

2. **$N \to N_{\text{eff}}$.** Three hundred bonds are not three hundred bets when they come from sixty issuers in eleven sectors (§28.2).

3. **The drawdown budget includes liquidity.** The ceiling on $G$ (§28.7) is set by how much the book can lose, and in credit a book can lose money with no change in any issuer's fundamentals, simply because the bid moves away from the mid (§28.5–§28.6).

> **[SOURCE EXTRACTION]** *Ben_Dor_Quantitative_Credit_Portfolio_Management p.50:* "a portfolio with a weighted spread of 200 bps and spread duration of two years is equally risky as a portfolio with a spread of 100 bps and spread duration of four years"
>
> **Annotation.** This is DTS doing in one sentence what a rating-bucket risk system needs a page of tables to approximate. Ben Dor and coauthors show that excess-return volatility rises roughly linearly in DTS, with a slope equal to the volatility of relative spread changes, which is why $\sigma_{\text{DTS}} = \text{DTS}\times\sigma_{\text{rel}}$ is the volatility we put into every sizing formula in this chapter. The modern departure is in the slope. $\sigma_{\text{rel}}$ is not a constant: it jumps in stress, and in 2026 it has been visibly higher for CCCs than for the rest of the index (§28.4). Estimate it by bucket and by regime, and carry the stress multiplier as a parameter ($\kappa$, §28.7). For a distressed issuer, the same authors note that managing DTS contributions becomes roughly equivalent to managing market weights (p.63): once the spread is large enough, the bond trades on price and recovery, and the DTS approximation hands the job over to the jump model of §28.4.

> **Trend Watch: The platform becomes the operating system, 2024–2026.** *What changed:* the multi-manager platform, with centrally set drawdown rules, pass-through costs and very large gross books, became the main buyer of idiosyncratic risk and the main employer of the people who produce it. *How big, with dates:* Cambridge Associates' review of 2024 audited statements (published 10 October 2025) found that "all reviewed multi-manager platforms" pass through additional expenses, ranging from 0.87% to 12.99% of assets with a median of 4.53%. For 2025, Millennium returned about 10.5%, Citadel's flagship about 10.2%, ExodusPoint about 18% and Schonfeld's flagship about 12.5%, against 16.5% for the S&P 500 (Hedgeweek relaying the FT, 5 January 2026). Point72 reportedly returned about 18% and had expanded to 190 pods per Bloomberg *(not independently verified)*, and HFR put industry capital at a record \$5.15trn, up \$642.8bn in 2025 (The Daily Upside, 23 February 2026). In March 2026, the Iran-war shock forced an unwind of crowded positions, and ExodusPoint, Balyasny, Citadel and Millennium gave up all or part of their January–February gains (Bloomberg, 2 April 2026). The Fed's May 2026 *Financial Stability Report* described hedge-fund leverage as "stable at record-high levels," concentrated in a small number of large funds. In September 2026 a Goldman Sachs prime-insights head was reported as saying that multi-strategy managers had attracted about \$500bn of additional assets over the past year, roughly 25% growth, while sector headcount rose only 10–11%, and as citing a JPMorgan estimate of 645% average multi-strategy leverage (Hedgeweek, 15 September 2026; industry estimates, not independently verified). The drawdown convention is commonly reported rather than disclosed: per the WSJ as relayed by eFinancialCareers (5 December 2025), Millennium PMs who lose 5% of allocated capital "typically" have it halved, and those who lose another 2.5% are "usually" let go; the firm declined to comment. *What it means for the desk:* about a quarter more capital chasing about a tenth more PMs means each PM's risk is rationed by rule, and the rule binds before the alpha does. A rule shared across firms also produces shared behaviour: when everyone's 5% line is hit in the same week, everyone sells the same bonds. The engineering in this chapter is about making the alpha and the rule compatible *before* the week arrives.

## 28.2 Effective Breadth When Issuers Cluster

Theo's book has 300 bonds. Kaz's breadth calculation therefore says 300. Ines looks at the issuer column and asks how many hands Theo is actually playing. The answer turns out to be about forty, and the gap between 300 and 40 is the difference between an information ratio of 2.7 and one of 1.0 at the same 50.5% hit rate.

### The Fundamental Law in hit-rate form

Start where Paleologo starts. Each day, each of $N$ independent, equal-sized bets earns $+1$ unit with probability $p$ (the hit rate) and $-1$ with probability $1-p$. One bet has mean $2p-1$ and variance $1-(2p-1)^2$. Equal-weighted across $N$ independent bets, the book's daily return has mean $2p-1$ and variance $[1-(2p-1)^2]/N$. Annualizing with 252 days,

$$
\text{IR} = \frac{(2p-1)\sqrt{252\,N}}{\sqrt{1-(2p-1)^2}} \;\approx\; (2p-1)\sqrt{252\,N}, \tag{28.3}
$$

where the approximation drops a term that is within 0.1% of one for any hit rate a human will achieve ($p = 0.52$ gives $\sqrt{1-0.04^2} = 0.9992$). The right-hand side is Grinold's law with $\text{IC} = 2p-1$ and breadth $\text{BR} = 252N$.

> **[SOURCE EXTRACTION]** *Paleologo_Advanced_Portfolio_Management p.148:* "(Inf. Ratio) = [2 × (hitting probability) − 1] × √(252 × (effective number of stocks))"
>
> **Annotation.** The phrase that does the work is "effective number." In an equity book of 150 single names, the effective number is close to the Herfindahl count of positions. In credit it is not, because the unit of independent information is the issuer, not the bond, and issuers in the same sector default in the same recession. A hit rate of 52% across 300 bonds would give an IR of $0.04\sqrt{252 \times 300} = 11$, a number that should make any risk officer reach for the phone. Across 40 effective bets it gives $0.04\sqrt{252\times 40} = 4.0$, and across 6 effective bets (a book that is really six views on six sectors) it gives 1.6. The second and third numbers are the ones a credit desk has seen.

### Two definitions of effective breadth

Paleologo's practical measure is the Herfindahl of GMV weights.

> **[SOURCE EXTRACTION]** *Paleologo_Advanced_Portfolio_Management p.150 (Procedure 8.1):* "H = sum[%GMV²(stock i)] … (effective number of stocks) = 1/H"
>
> **Annotation.** $1/H$ answers "how many equal positions would have the same concentration as mine?" It ignores correlation, which is harmless when residual correlations are near zero, as they are after a good equity factor model. In credit, residual correlation is not near zero inside an issuer (five bonds of one capital structure move together because they share one default time $\tau$) and it is not zero across issuers in the same sector and rating bucket. Use $1/H$ on issuer-netted weights as the floor of your breadth reporting, and the covariance-aware measure below as the number that goes into (28.2) and (28.3).

The covariance-aware measure asks a sharper question: how many independent, equal-volatility bets would have the same ratio of *undiversified* to *diversified* risk as my book? Let $\Sigma$ be the idiosyncratic covariance matrix (the residual after the factor model of Chapter 8 strips rates, spread beta and the credit factors; IDO or it didn't happen), $\sigma_i = \sqrt{\Sigma_{ii}}$, and $w$ the vector of position weights. Define

$$
N_{\text{eff}} = \frac{\left(\sum_i |w_i|\,\sigma_i\right)^2}{w^{\top}\Sigma\, w}. \tag{28.4}
$$

The numerator is the variance the book would have if every position moved in lockstep; the denominator is the variance it actually has. Two checks. If all $N$ positions are independent with equal weight and volatility, the numerator is $N^2 w^2\sigma^2$ and the denominator $N w^2\sigma^2$, so $N_{\text{eff}} = N$. If they are perfectly correlated, numerator and denominator are equal and $N_{\text{eff}} = 1$.

Now add issuer structure. Suppose $N$ bonds come from $J$ issuers with $m = N/J$ bonds each, equal weights and volatilities, residual correlation $\rho_w$ between bonds of the same issuer and $\rho_a$ between bonds of different issuers. Each bond has $m-1$ same-issuer partners and $N-m$ other-issuer partners, so

$$
w^\top\Sigma w = w^2\sigma^2\big[N + N(m-1)\rho_w + N(N-m)\rho_a\big],
$$

and (28.4) becomes

$$
N_{\text{eff}} = \frac{N}{1 + (m-1)\rho_w + (N-m)\rho_a}. \tag{28.5}
$$

Theo's book: $N = 300$ bonds, $J = 60$ issuers of $m = 5$ bonds, $\rho_w = 0.9$ (bonds of one issuer share a default time), and a residual cross-issuer correlation of $\rho_a = 0.01$ *(illustrative)*. The denominator is $1 + 3.6 + 2.95 = 7.55$, and $N_{\text{eff}} \approx 39.7$. Two limits explain the number. With $\rho_a = 0$, $N_{\text{eff}} = 300/4.6 \approx 65$: the issuer count, slightly inflated because bonds of one issuer are not perfectly correlated. And as $N \to \infty$ with $m$ fixed, $N_{\text{eff}} \to 1/\rho_a = 100$: a residual correlation of one percent caps the breadth of any credit book at a hundred bets, however many CUSIPs it owns. Kaz calls this the "speed of light" of credit diversification. It is the reason a bigger book is not a better book after the first hundred issuers, and the reason the platform pays more for a new *signal* than for a new *name* (§28.8).

### How noisy is your hit rate?

The same binomial arithmetic tells you how long it takes to know whether a PM is any good. A year of daily hits on $N_{\text{eff}}$ independent bets is $252\,N_{\text{eff}}$ Bernoulli draws, so the standard error of the measured hit rate is

$$
\text{SE}(\hat p) = \sqrt{\frac{p(1-p)}{252\,N_{\text{eff}}}}. \tag{28.6}
$$

> **[SOURCE EXTRACTION]** *Paleologo_Advanced_Portfolio_Management p.150:* "The standard error associated to this yearly hitting rate is 0.33%. This is a very large value, comparable to the 'edge' of 0.5%."
>
> **Annotation.** Equation (28.6) reproduces the 0.33% with about 90 effective names and $p \approx 0.505$. For a credit PM with 40 effective bets, the standard error over a year is 0.50%, the same size as the edge itself: a year of P&L cannot tell a 50.5% PM from a coin. This is the quiet scandal under every drawdown rule in §28.6. The rule is a decision about skill made on a sample too small to measure skill, which is defensible only because its real job is survival, not inference. It is also the best argument for instrumenting hit rates *by signal and by analyst* (the Edge Ledger of Chapter 3), where the sample is larger and the attribution is sharper than one PM's annual P&L.

### Concentration is not rewarded in debt

The ex-RSSG instinct is to concentrate: you did the work, you read the intercreditor, you know the fulcrum. The shelf disagrees, politely and then not politely.

> **[SOURCE EXTRACTION]** *Bohn_Stein_Active_Credit_Portfolio_Management p.489:* "Unlike equities, however, debt has no upside potential to offset the potential for large losses … there are no practical circumstances under which an investor or counterparty can be rewarded for taking on concentrations of default risk."
>
> **Annotation.** The payoff of a bond is capped at par plus coupons and floored at recovery, so the right tail that rewards a concentrated equity bet does not exist. A concentrated credit bet earns the same spread as a diversified one and carries more default variance. The modern desk keeps the principle and adds an exception the authors would recognize: when the PM's information is genuinely about $L$ rather than about $\lambda$ (a recovery the market has mispriced because it has not read the documents), the bet is less a default bet than a recovery bet, and §28.4 sizes it with Kelly. Even then, the single-name cap comes from the ruin boundary, not from conviction.

> **[SOURCE EXTRACTION]** *Bolder_Credit_Risk_Modelling p.391:* "One half of the total risk can … be allocated to the 16 largest obligors"
>
> **Annotation.** Bolder's example is a 100-obligor one-factor portfolio, and the punchline generalizes: tail risk concentrates far faster than position count suggests. On the same pages Bolder argues for expected shortfall over VaR as the economic-capital measure, because ES contributions are stable with feasible simulation sizes while VaR contributions are not. On a desk this becomes a dashboard column (§28.9): ES contribution by issuer, ranked, with the top decile of names flagged when they carry more than half the tail.

How should conviction enter sizing, then? Paleologo's evidence is that the simple rule beats the clever one.

> **[SOURCE EXTRACTION]** *Paleologo_Advanced_Portfolio_Management p.100 (Insight 6.2):* "Using target positions that are proportional to the forecasted expected returns of a stock beats other common methods."
>
> **Annotation.** In credit, with covariance matrices built from sparse, stale, issuer-clustered data (Chapter 8), full mean-variance inverts noise and produces positions nobody can trade. Proportional sizing on factor-neutralized alphas (Paleologo's Procedure 6.3 regresses the alphas on the factor loadings and sizes the standardized residuals) is robust to all of that. Our credit amendment is to make the proportionality *per unit of DTS-scaled volatility*: target $w_i \propto \alpha_i/\sigma_{\text{DTS},i}^2$ per issuer, then cap each issuer at the Kelly ruin bound of §28.4, then net to issuer before computing $N_{\text{eff}}$.

### Specification for AI Implementation (Block 1): Effective Breadth and the Hit-Rate Law

What ROBO built from the vague version ("compute breadth"): `len(book)`. It returned 300, and it was correct about the length.

The precise version: compute $1/H$ on issuer-netted GMV weights, $N_{\text{eff}}$ from (28.4) on the idiosyncratic covariance, the closed form (28.5) for equal issuer blocks as a regression test, the IR from (28.3) in both exact and approximate form, and the hit-rate standard error (28.6). Check the hit-rate law by Monte Carlo. All blocks in this chapter run in order in one interpreter.

<!-- EXPLAIN: Listing 28.1 -->
> **Code Companion: Listing 28.1.** 1/H on absolute GMV weights. The full python listing is in [Appendix F, Listing 28.1](#code-28-1).

The edge cases ROBO must handle: a long/short pair in two bonds of the same issuer (a basis or curve trade) makes the denominator of (28.4) nearly zero and $N_{\text{eff}}$ explode, which is why the function refuses and the spec says to net to issuer first; a book with no gross exposure raises; and negative variance from a non-positive-definite estimated covariance is clipped on the diagonal but should be repaired upstream (shrinkage, Chapter 8), not here.

## 28.3 Allocation Across Signal Horizons

Theo's four PMs run four different clocks. Priya *(fictional, as are all PMs in this chapter)* runs index trend on CDX (Chapter 10) and turns her book over every few weeks. Dov runs value, carry and quality in liquid cash bonds (Chapter 9) and holds for quarters. Rafe runs ETF creation/redemption and portfolio-trade arbitrage (Chapters 19–20) and holds for days. Sunita, ex-RSSG like Theo, runs LMT candidates, post-reorg equities and docket-driven events (Chapters 13–16) and holds until a judge rules. Theo's question is how to split the risk among them. The answer depends less on who has the best backtest than on a property of each signal that nobody puts in the pitch deck: how fast it dies, compared with how much it costs to trade.

> **[SOURCE EXTRACTION]** *Dynkin_Systematic_Investing_in_Credit p.520:* "However, limited liquidity in credit markets makes high‐turnover strategies less practical and necessitates long investment horizons consistent with fundamentally driven styles such as"
>
> **Annotation.** Dynkin and coauthors are describing cash bonds, and in cash bonds the sentence is a law. The 2026 desk's departure is that "credit" is no longer one instrument. Since about 2021 the index CDS market, credit ETFs, listed credit futures and portfolio trading have built a liquid layer on top of the cash market where turnover is cheap (see the Trend Watch below). The horizon constraint has not gone away. It has become a property of the *tier*, not of the asset class. Fast signals are viable if they are expressed in the liquid layer; slow signals belong in cash; and the desk head's job is to stop anyone trading a fast signal in a slow instrument.

### The break-even half-life

Model a signal as a forecast of excess return whose strength decays exponentially. At inception it predicts an expected return *rate* of $\alpha_0$ per year, and the rate decays as $\alpha(t) = \alpha_0 e^{-\phi t}$, where $\phi$ is the decay rate and $h = \ln 2/\phi$ the half-life. A position opened on the signal and held while the forecast lasts earns, in expectation,

$$
\int_0^\infty \alpha_0 e^{-\phi t}\,dt = \frac{\alpha_0}{\phi}.
$$

Let $c^{\text{RT}}$ be the round-trip cost in the instrument used to express the signal, as a fraction of price. In credit that is the liquidity cost score of Ben Dor et al. (§28.5): $\text{LCS} = D^{\text{spr}} \times$ bid-ask spread in spread terms. A signal that refreshes continuously turns its positions over about once per signal life, $\phi$ times a year, so its annual gross alpha is $\phi \cdot \alpha_0/\phi = \alpha_0$, its annual cost is $\phi\, c^{\text{RT}}$, and its net alpha is

$$
\alpha^{\text{net}} = \alpha_0 - \frac{\ln 2}{h}\,c^{\text{RT}}. \tag{28.7}
$$

Setting $\alpha^{\text{net}} = 0$ gives the shortest half-life a signal can have and still pay for itself in a given tier:

$$
h^{\ast} = \frac{\ln 2 \cdot c^{\text{RT}}}{\alpha_0}. \tag{28.8}
$$

Take a signal with $\alpha_0 = 3\%$ a year. In the index layer, with a round-trip cost of 0.05% of price *(illustrative)*, $h^\ast = 0.693 \times 0.0005/0.03 = 0.0116$ years, about three trading days. In liquid cash bonds at 0.6% *(illustrative)*, $h^\ast = 0.139$ years, about seven weeks. In stressed bonds at 2.5% *(illustrative)*, $h^\ast = 0.58$ years, seven months. Equation (28.8) explains in one line why trend lives in CDX and LMT alpha lives in bonds you hold until the court rules. Trend's half-life is weeks: viable in tier 0 and a money-loser in cash. The LMT trade's half-life is months, and its $\alpha_0$ is large enough to pay a stressed bid-ask.

Two refinements, both from the literature. First, Gârleanu and Pedersen (2013, *Journal of Finance*, "Dynamic Trading with Predictable Returns and Transaction Costs") show for quadratic costs that the optimal policy is to "aim in front of the target" and trade partially toward it, and that predictors with slower decay get more weight in the aim portfolio. Credit costs are mostly linear (half the bid-ask on every trade) with a size-dependent impact on top (§28.5), and linear costs produce a no-trade band rather than partial trading: do not trade a bond whose target position has moved less than the band. That is exactly Dynkin's "turnover buffer" (Dynkin p.707), and its alternative is a hard turnover budget with explicit exposure constraints (p.715), which avoids the large rebalancing events a buffer can store up. Second, fills are probabilistic. The trade a backtest assumes is a trade an RFQ may not fill, and the unfilled order leaves an exposure nobody modelled.

> **[SOURCE EXTRACTION]** *Man_Revolutions_in_Credit_Trading_2023 p.4:* "Liquidity modelling is essential too: an optimised portfolio is not optimal if you can't trade it. Furthermore, unfilled orders may create unintended and potentially unmodelled risk exposures in the portfolio."
>
> **Annotation.** The horizon ladder below is the desk-level response. A fill probability below one is a hidden cost in (28.7): if a fraction $1-\pi$ of intended trades fail, the realized position lags the target, so a fast signal decays further before it is expressed. Man's companion point (same page) is that with more than 90% of its flow electronic, it could make "more frequent, smaller trades," which lowers $c^{\text{RT}}$ for small tickets and so lowers $h^\ast$. Electronification moves signals *down* the ladder: a signal that needed tier 0 in 2015 may be viable in liquid cash in 2026, if the tickets are small.

> **[SOURCE EXTRACTION]** *Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.19:* "We cannot overstate the importance of transaction cost and liquidity modelling for quant credit participants" … "Momentum tends to have the highest turnover of any factor approach while both Size and Quality see the least churn."
>
> **Annotation.** Momentum is the canonical victim of (28.8). At our illustrative cash cost of 0.6% round trip, a cash-bond momentum signal with a two-month half-life needs $\alpha_0$ above $0.693 \times 6 \times 0.006 = 2.5\%$ a year to break even. That is a high bar for a factor whose long-only premium is usually quoted in tens of basis points. The modern answer is not to drop momentum but to stop trading it standalone: use it as a tie-breaker inside trades the slow signals were going to make anyway, where its marginal cost is zero, or express it in the index layer.

### The horizon ladder

| Tier | Instruments | Round-trip cost *(illustrative)* | Regulatory anchor | Signals that live here | Chapters |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 0 | CDX/iTraxx, credit index futures, HY/IG ETFs | 0.02–0.10% of price | Exchange or SEF liquidity; days to liquidate below one | Index trend, ETF premium/discount, beta overlay, hedges | 10, 19, 20 |
| 1 | Liquid IG/HY cash bonds, PT-eligible | 0.3–1.0% | FRTB liquidity horizon 40 days (IG corporate), 60 days (HY corporate) | Value, carry, quality, defensive HY, slow momentum tilts | 8, 9, 11, 12 |
| 2 | Stressed, LMT candidates, post-reorg equity and claims | 2–5% or more | FRTB 120 days ("other" credit spread); SEC Rule 22e-4 "illiquid" bucket | Covenant, docket, priming-risk and recovery alpha | 13–16, 25 |

The FRTB horizons are from the Basel Framework, MAR33.12 (in force 1 January 2023). They are regulatory anchors for a bank's trading book, not a hedge fund's liquidation plan, but they encode a consensus that a corporate HY position takes half again as long to exit as an IG one, and a stressed one twice as long again.

The ladder prescribes the allocation in three steps. First, each signal goes to the cheapest tier that can express it, and is dropped (or demoted to a tie-breaker) if (28.7) is negative there. Second, each tier gets a liquidity budget (days-to-liquidate and stressed LCS, §28.5), and the volatility budget follows from it, not the other way around. Third, the overlay in tier 0 hedges the beta that the slow books accumulate, so the slow books can hold their IDO without being forced to trade it every time spread beta moves. IDO or it didn't happen: the overlay is how a cash book keeps its idiosyncratic alpha without paying a cash bid-ask to manage its systematic exposure.

> **Poker Table.** Ines explains the ladder to Theo with chips. "Dov's value book is a big pair you slow-play. You don't raise every street, because every raise pays the rake, and in cash bonds the rake is half a point. Priya's trend sleeve is your table image: small bets, frequent, in the index, where the rake is a few cents. The table sees you trading all day and never notices you haven't touched the big pair in four months." Theo asks what happens when the trend sleeve and the value book disagree. "Then you're hedged, and you've paid the index rake to be hedged instead of the cash rake. That's the whole edge." The hand history agrees: in the desk's markouts *(illustrative)*, the value book's one-month markouts on new positions are flat and its six-month markouts carry the alpha, while the trend sleeve's markouts are the other way round. A desk that judged both at one horizon would fire one of them for the other's sins.

> **Trend Watch: The liquid overlay layer arrives, 2021–2026.** *What changed:* the tier-0 instruments that let a credit desk trade fast signals and hedge slow books cheaply grew to record size. *How big, with dates:* ISDA's research note of 29 July 2026 puts total CDS trading at \$41.8tn in 2025, with index products a record \$39.0tn (93.3% of the total; \$28.1tn in 2023), while single-name activity fell from a \$3.3tn peak in 2023 to \$2.8tn; H1 2026 activity was \$27.4tn, up 27.8% year on year. Clarus reports cleared USD CDX of \$3.94tn in March 2026, up 46% year on year. In listed credit, Cboe iBoxx futures block trades topped \$1bn a month for a second straight month in August 2026, and IBIG block activity overtook IBHY's for the first time (The DESK, 16 October 2026, Cboe-sponsored content). In cash, March 2026 combined US IG and HY TRACE volume averaged \$70.2bn a day, up 14.7% year on year, with record portfolio-trading ADV of \$2.3bn at MarketAxess and a record \$10.3bn ADV at Trumid (The DESK, 9 April 2026). In 2022, Man's protocol mix was 42% disclosed RFQ, 16% anonymous RFQ, 13% session-based, 10% central limit order book, 10% portfolio trading and 9% streams (Man_Revolutions_in_Credit_Trading_2023 p.4). *What it means for the desk:* the cost of the overlay in (28.8) has fallen and its capacity has risen, so more of the desk's fast alpha can be moved into tier 0 and more of its beta management out of tier 1. It also means more of everyone's de-risking happens in the same few instruments on the same few days. The overlay is cheap until the day every pod uses it to cut gross at once.

### Specification for AI Implementation (Block 2): The Horizon Ladder

What ROBO built from the vague version ("put each signal where it makes the most money"): it ranked signals by gross backtest return and put all of them in the tier with the most bonds, tier 1, because that was where the most money had been made before costs.

The precise version: for each signal and each tier that can express it, compute the net alpha (28.7); assign the signal to the tier with the highest positive net alpha; flag signals with no positive tier as tie-breakers only. Report the break-even half-life (28.8) for each tier at a reference $\alpha_0$.

<!-- EXPLAIN: Listing 28.2 -->
> **Code Companion: Listing 28.2.** Eq. The full python listing is in [Appendix F, Listing 28.2](#code-28-2).

Edge cases: a signal with $\alpha_0 \le 0$ has an infinite break-even half-life and is never traded; a half-life of zero is an error, not a very fast signal; and costs must be *stressed* costs when the ladder is used for the liquidity budget (§28.5), because a tier-1 bond at a 5× bid-ask is a tier-2 bond for as long as the stress lasts.

## 28.4 Kelly With Jump-to-Default

Kaz's 93% deserves a proper autopsy, because nothing in it is an arithmetic error. Kaz took one B3 bond with carry $c = 4.5\%$ a year, a one-year default probability of $q = 3.1\%$ read from a rating-agency table for B3 issuers, and a loss given default of $L = 0.6$ (the agency's average 40% recovery), and applied the Kelly criterion for a binary bet. The formula did what it was told.

> **[SOURCE EXTRACTION]** *Paleologo_Advanced_Portfolio_Management p.91:* "If your goal were to maximize expected returns and your expected returns forecasts were accurate, the investment decision would be straightforward: the portfolio would hold a single stock, the one with highest expected returns. Those who follow this rule need to read this book the most, but probably don't have enough money to buy it"
>
> **Annotation.** The credit version is "hold the one CCC with the fattest spread," and it is worse than the equity version, because the fattest spread is usually fattest for a reason the spread does not tell you: a maturity wall, a sponsor shopping for an uptier, a recovery that depends on whether the "first lien" is first. Kelly is the disciplined alternative to maximizing expected return: it maximizes expected *log* wealth, which penalizes the possibility of ruin infinitely. In credit, ruin has a precise address. It is the default of a position large enough that $f L \ge 1$.

### Discrete Kelly for a bond

Over one period, a fraction $f$ of NAV in the bond earns $+c$ with survival probability $p$ and loses $L$ with default probability $q = 1-p$ (excess returns over financing; pull-to-par and rolldown ignored). Expected log growth is

$$
g(f) = p\,\ln(1 + f c) + q\,\ln(1 - f L).
$$

Setting $g'(f) = pc/(1+fc) - qL/(1-fL) = 0$ and cross-multiplying, $pc(1 - fL) = qL(1 + fc)$, so $pc - qL = fcL(p+q) = fcL$, and

$$
f^\ast = \frac{pc - qL}{cL} = \frac{p}{L} - \frac{q}{c}. \tag{28.9}
$$

Three facts follow. The bet has positive edge, $pc - qL > 0$, if and only if $q < c/(c+L)$. The growth function is defined only for $f < 1/L$, the **ruin boundary**: at $f = 1/L$ a default takes wealth to zero and $\ln 0 = -\infty$. And for Kaz's inputs, $f^\ast = 0.969/0.6 - 0.031/0.045 = 1.615 - 0.689 = 0.926$. There is the 93%.

Now the sensitivities, which are where the ex-RSSG analyst earns a seat. Differentiating (28.9),

$$
\frac{\partial f^\ast}{\partial L} = -\frac{p}{L^2}, \qquad \frac{\partial f^\ast}{\partial q} = -\left(\frac{1}{L} + \frac{1}{c}\right).
$$

At Kaz's inputs these are $-2.69$ and $-23.9$. The fraction is nine times more sensitive to $q$ per unit, but the units are not equally uncertain. A one-year default probability for a B3 name is known to perhaps $\pm 1.5$ points, which moves $f^\ast$ by about 36 points of NAV; a recovery is known to perhaps $\pm 15$ points, which moves it by about 32. First-lien distressed-exchange recoveries alone went from 55% in 2023 to 71% at end-2024 in Moody's data (Bloomberg Law, 23 April 2025; see the Trend Watch in §5.5). The two uncertainties are of the same size, and only one of them can be shrunk by reading the credit agreement. The PhD takes $L$ from a table. The analyst who has read the intercreditor agreement knows whether the first lien is first.

### Continuous time, and the jump

Let a position of fraction $f$ in a bond have excess return $dP/P = c\,dt + \sigma\,dW_t - L\,dN_t$, where $\sigma$ is the diffusive (spread) volatility, $N_t$ a Poisson process with intensity $\lambda$ (the default intensity, under $\mathbb{P}$; see below), and the bond is replaced after default so the bet is stationary. Wealth follows $dX_t/X_{t^-} = f(c\,dt + \sigma\,dW_t - L\,dN_t)$. Itô's formula for a jump-diffusion gives

$$
d\ln X_t = \left(fc - \tfrac12 f^2\sigma^2\right)dt + f\sigma\,dW_t + \ln(1 - fL)\,dN_t,
$$

so the long-run growth rate is

$$
g(f) = fc - \tfrac12 f^2 \sigma^2 + \lambda \ln(1 - fL). \tag{28.10}
$$

With $\sigma = 0$, $g'(f) = c - \lambda L/(1-fL) = 0$ gives

$$
f^\ast = \frac{1}{L} - \frac{\lambda}{c}, \tag{28.11}
$$

the continuous twin of (28.9). With $\sigma > 0$, $g'(f) = c - f\sigma^2 - \lambda L/(1 - fL) = 0$. Multiply by $(1 - fL)$:

$$
\sigma^2 L\, f^2 - (cL + \sigma^2)\, f + (c - \lambda L) = 0. \tag{28.12}
$$

The left side is positive at $f = 0$ (when the edge $c - \lambda L$ is positive) and equals $-\lambda L < 0$ at $f = 1/L$, so exactly one root lies inside the ruin boundary, and it is the smaller one. In rationalized form, which avoids cancellation when $\sigma$ is small,

$$
f^\ast = \frac{2(c - \lambda L)}{(cL + \sigma^2) + \sqrt{(cL - \sigma^2)^2 + 4\sigma^2\lambda L^2}}.
$$

(The discriminant has been rewritten as a sum of squares, so it is never negative.) At Kaz's inputs with $\lambda = 0.031$ and $\sigma = 5\%$, $f^\ast \approx 0.94$.

Compare the shortcut Kaz almost used, Merton's diffusion fraction with the jump replaced by a diffusion of the same mean and variance, $\lambda L$ and $\lambda L^2$:

$$
f^{\text{M}} = \frac{c - \lambda L}{\sigma^2 + \lambda L^2} = \frac{0.0264}{0.0025 + 0.0112} = 1.93.
$$

Merton's approximation says to hold 193% of NAV in a bond whose default costs $1.93 \times 0.6 = 116\%$ of NAV. The approximation is excellent for small jumps and disastrous near the ruin boundary, because a diffusion never jumps over it. Bermin and Holm (2026, *Kelly trading when asset prices have jumps*; publication details CHECK) make the general point that the continuous approximation can badly underestimate bankruptcy risk when leverage is high. In credit, every default is a large jump, so the approximation is never safe for single names. Use (28.10).

### Fractional Kelly is full Kelly for people with standard errors

Near its maximum, any growth function is approximately quadratic, $g(f) \approx \mu f - \tfrac12 v f^2$, with $f^\ast = \mu/v$ and $g^\ast = \mu^2/(2v)$. Betting a multiple $\theta$ of Kelly gives

$$
g(\theta f^\ast) = \frac{\mu^2}{v}\left(\theta - \frac{\theta^2}{2}\right) = g^\ast\,(2\theta - \theta^2).
$$

Half Kelly keeps 75% of the growth at half the volatility, and double Kelly keeps none of it. Now suppose the edge is estimated with relative error $\varepsilon$, mean zero and standard deviation $s_\varepsilon$, so that the desk bets $\theta(1+\varepsilon)f^\ast$. Expected growth is

$$
\mathbb{E}\big[g\big(\theta(1+\varepsilon)f^\ast\big)\big] = g^\ast\left(2\theta - \theta^2(1 + s_\varepsilon^2)\right),
$$

which is maximized at

$$
\theta^\ast = \frac{1}{1 + s_\varepsilon^2}. \tag{28.13}
$$

An edge known to within 100% of itself, which is generous for a single credit, gives $\theta^\ast = \tfrac12$. Half Kelly is not timidity. It is the full Kelly of a PM who is honest about the standard error of her edge, and the hit-rate arithmetic of §28.2 says that standard error is large.

### Which measure, and which loss

Kelly needs the physical default intensity $\lambda^{\mathbb{P}}$, never the risk-neutral $\lambda^{\mathbb{Q}}$ bootstrapped from CDS in Chapter 6. The reason is a one-line proof. Under $\mathbb{Q}$ the credit triangle holds, $c \approx \lambda^{\mathbb{Q}} L$, so the edge $c - \lambda^{\mathbb{Q}} L$ is zero and (28.11) gives $f^\ast = 0$: the risk-neutral measure is the measure in which nobody has an edge, by construction. The edge that Kelly sizes is $c - \lambda^{\mathbb{P}}L$, the credit risk premium plus whatever your information adds. That is why mixing sources is dangerous. Kaz's $c$ came from the market, his $q$ from a long-run agency cohort, and his $L$ from an agency average, and the 93% is the product of three numbers from three different worlds.

Recovery is not a constant either. Let $L = L_{\max} U$ with $U \sim \text{Beta}(a, b)$ (the recovery model of Chapter 5). The growth rate becomes

$$
g(f) = fc - \tfrac12 f^2\sigma^2 + \lambda\,\mathbb{E}\big[\ln(1 - fL)\big],
$$

defined for $f < 1/L_{\max}$. Two consequences. Because $x \mapsto x/(1 - fx)$ is convex, Jensen's inequality gives $\mathbb{E}[L/(1 - fL)] > \mathbb{E}[L]/(1 - f\,\mathbb{E}[L])$, so a random $L$ lowers $f^\ast$ below the constant-$L$ value at the same mean. And the **ruin boundary is set by the worst recovery, not the average one**. If the analyst's reading of the collateral package and the intercreditor shows a 25% recovery floor, $L_{\max} = 0.75$ and the boundary is $1.33\times$ NAV. If the documents permit a non-pro-rata uptier (Chapter 13), the worst case for a non-participating lender is close to zero recovery, $L_{\max} \to 1$, and the boundary falls to $1.0\times$, the unlevered position. The Priming Risk Score is, among other things, an estimate of where the ruin boundary is. Kelly in credit is the intercreditor agreement, priced in leverage.

### Many names, one recession

For independent jumps, (28.10) is additive across names and each $f_i^\ast$ is computed alone. Defaults are not independent. Add a common Poisson process with intensity $\lambda_c$ that defaults all $n$ names of a cluster together (a sector, a sponsor, a CLO's weakest bucket). For $n$ symmetric names each held at $f$,

$$
g(f) = n f c - \tfrac12 n f^2 \sigma^2 + n\lambda_i\ln(1 - fL) + \lambda_c\ln(1 - n f L),
$$

and the first-order condition (with $\sigma = 0$) is

$$
c = \frac{\lambda_i L}{1 - fL} + \frac{\lambda_c L}{1 - n f L}, \qquad 0 < f < \frac{1}{nL}. \tag{28.14}
$$

The right-hand side is larger than in the single-name problem at the same total intensity, so each $f$ is smaller, and the cluster as a whole obeys $\sum_j f_j L_j < 1$. A desk that computes forty single-name Kelly fractions and adds them up has computed a number with no meaning. The binding constraint is the cluster ruin bound.

> **Ways This Blows Up.** *Kelly on a $\mathbb{Q}$ hazard:* gives zero or a negative fraction, which fails safe, and so tempts someone to "fix" it by mixing a market spread with a historical default rate and an agency recovery, which is how you get 93%. *Kelly on a smoothed mark:* ROBO's favourite IG bond had a realized volatility of 0.4% because its matrix mark had not moved; fed into (28.12), it produces leverage limited only by the ruin boundary, and the volatility arrives with the first trade. Estimate $\sigma$ from traded prices or from a DTS model, never from the mark. *Kelly on correlated CCCs:* individually optimal fractions summed across a sector breach (28.14). *Kelly on yesterday's $L$:* the recovery distribution moved between 2023 and 2026 (§5.5); a static $L$ calibrated on pre-2015 defaults is an upper bound on recovery for sponsor-backed, loan-only borrowers.

### Case Study: The 2026 CCC Decompression

> **Trend Watch: The CCC decompression, January–October 2026.** *What changed:* the bottom of the high-yield market repriced while the index barely moved. *How big, with dates (ICE BofA option-adjusted spreads, FRED series BAMLH0A0HYM2, BAMLC0A0CM and BAMLH0A3HYC, fetched 17 October 2026):* US HY went from 2.83% on 2 January to a low of 2.64% on 22 January, peaked at 3.46% on 30 March during the Iran-war shock, and stood at 3.23% on 15 October. US IG went from 0.79% to 0.73%, 0.94% (16 March) and 0.84%. The CCC-and-lower subindex went from 8.88% to a low of 8.38% (28 January), 10.20% (30 March) and 12.78% on 15 October, after 12.82% on 14 October, its widest since at least October 2023. The CCC-to-HY spread ratio rose from about 3.1× in January to about 4.0× in October. Recovery expectations moved the same way: Moody's September 2026 *Corporate Defaults and Recoveries* report projected first-lien loan recoveries "declining to 55%" (via American Banker, 28 September 2026). *What it means for the desk:* a book sized on index-level risk saw a calm year. A book sized on name-level $\lambda$ and $L$ saw the two inputs of (28.11) moving against each other while the headline spread looked boring, which is the setting where Kelly earns its keep.

How a systematic desk would have read it. Take a representative CCC bond at the January low, with $c \approx 8.4\%$ (the subindex OAS), and illustrative physical inputs $\lambda^{\mathbb{P}} = 6\%$ a year and $L = 0.55$. Equation (28.11) gives $f^\ast = 1/0.55 - 0.06/0.084 = 1.82 - 0.71 = 1.10$: Kelly would lever it. By mid-October, with $c \approx 12.8\%$, suppose the hazard model of Chapter 14 (re-defaults in the 2024 LMT cohort) has $\lambda^{\mathbb{P}}$ at 10% and the recovery model has $L$ at 0.70 *(both illustrative)*. The edge has risen, from $0.084 - 0.033 = 5.1\%$ to $0.128 - 0.070 = 5.8\%$ a year, so a spread screen says buy. But (28.11) gives $f^\ast = 1.43 - 0.78 = 0.65$, a 40% *cut*. The spread said the bucket got cheaper. Kelly says it got cheaper and more dangerous, and the danger grew faster: the ruin boundary moved in from 1.82 to 1.43 as $L$ rose, and $\lambda/c$ rose from 0.71 to 0.78.

Three refinements turn this into a trade. First, apply (28.13): with a relative standard error on the edge of about 1, bet half of each fraction. Second, cap each name at the ruin boundary implied by its *documents*, $1/L_{\max}$, which for LMT-permissive credits is $1.0$ or less, not $1/\mathbb{E}[L]$. Third, impose (28.14) on each cluster: the CCC bucket of one sector, or the issuers of one sponsor, share a common jump. What survives is a book that leaned into CCC carry in January, cut it as $\lambda$ and $L$ rose through the summer, and concentrated what remained in names where the analyst's reading of the documents put a floor under recovery. That last step is not quant. It is the RSSG seat, sized.

### Specification for AI Implementation (Block 3): Kelly With Jumps

What ROBO built from the vague version ("size positions by Kelly"): it computed $\mu/\sigma^2$ per bond from three months of marks, found the matrix-priced IG bond, and requested 4,000% of NAV in it.

The precise version: implement (28.9), (28.10)–(28.12) with the rationalized root, Merton's approximation (for comparison only, never for sizing), the fractional multiplier (28.13), the random-loss growth rate with a Beta recovery and a ruin boundary at $1/L_{\max}$, and the cluster solver (28.14). Inputs are physical-measure intensities. Long-only: return zero when the edge is not positive.

<!-- EXPLAIN: Listing 28.3 -->
> **Code Companion: Listing 28.3.** Eq. The full python listing is in [Appendix F, Listing 28.3](#code-28-3).

Edge cases ROBO must handle: an edge of exactly zero returns zero, not a division by zero; `lam = 0` falls back to the diffusion fraction and is the only case where the ruin boundary does not apply; a Beta recovery with $a < 1$ or $b < 1$ has an unbounded density at an endpoint, which `quad` integrates but slowly, so the spec requires $a, b \ge 1$ for production fits; and every output fraction is a fraction of NAV *before* the cluster cap, the fractional multiplier and the leverage band of §28.7 are applied, in that order.

## 28.5 LVaR, Days-to-Liquidate and the 5× Problem

The risk officer marks to bid. Theo thinks this is a technicality until Ines explains what it does to his P&L on the day the bid moves. A long bond marked at the bid loses money when the bid-ask widens, whether or not anything has happened to the issuer. A short bond marked at the offer loses money too. On a gross book the bid-ask is a short volatility position, and it is short exactly the volatility that arrives with every stress.

> **[SOURCE EXTRACTION]** *Ben_Dor_Quantitative_Credit_Portfolio_Management p.112:* "We define LCS as the bond's OASD multiplied by this spread. Consequently, a bond's LCS can be interpreted as the cost, in percentage points, of immediately executing a roundtrip transaction." … "Over this time period, the LCS for the IG Index ranged from 0.59% to 3.40%."
>
> **Annotation.** The period is January 2007 to June 2009, and the move from 0.59% (January 2007) to 3.40% (November 2008) is a 5.8× widening of the round-trip cost of the US IG index. The same page notes that the index's LCS had already doubled between June and September 2007, more than a year before Lehman, and the next page that the HY-minus-IG gap went from about 40 bp to more than 400 bp. So "bid-ask widens 5×" is not a stress scenario somebody made up for a risk committee. It is the 2007–2008 base case for investment grade, and HY was worse. The modern departure is speed: in March 2020 IG costs roughly tripled in three weeks (below), and in March 2026 EUR IG spreads rose 64% above their January average in days. The multiplier is a parameter, and it has to sit inside the sizing before the stress, because afterwards it sits inside the P&L.

### From Bangia's LVaR to a credit LVaR

Bangia, Diebold, Schuermann and Stroughair (1998/99, *Modeling Liquidity Risk, With Implications for Traditional Market Risk Measurement and Management*) add the cost of liquidation to parametric VaR. For a position of value $P$ with daily log-return volatility $\sigma$,

$$
\text{VaR} = P\left[1 - e^{-2.33\,\sigma}\right], \qquad \text{COL} = \tfrac12 P\left(\bar S + a\,\tilde\sigma\right), \qquad \text{LVaR} = \text{VaR} + \text{COL}, \tag{28.15}
$$

where $S = (\text{Ask} - \text{Bid})/\text{Mid}$ is the relative spread, $\bar S$ and $\tilde\sigma$ are its mean and volatility, and the multiplier $a$ "ranges from 2.0 to 4.5 depending on the instrument" (they measured 2.5 for JPY and 3.5 for THB in 1997–98). The factor $\tfrac12$ is there because liquidating at the bid costs half the bid-ask. Two translations make it a credit formula.

First, for a spread-quoted bond the relative bid-ask in price terms *is* the LCS, so $\text{COL}_i = \tfrac12 |\text{MV}_i| \cdot \text{LCS}_i^{\text{stress}}$, and shorts pay at the offer just as longs pay at the bid. Second, the $\bar S + a\tilde\sigma$ form does not reach 5× in practice. To get from 0.59% to 3.40% you need $a\tilde\sigma = 2.81$ points; a calm-window $\tilde\sigma$ of 0.10–0.20 points *(illustrative)* would need $a$ between 14 and 28, four to ten times Bangia's FX range. Credit liquidity does not wiggle around a mean. It jumps between regimes. So the desk carries a multiplicative stress factor $m$ instead:

$$
\text{COL}_i^{\text{exo}} = \tfrac12\, m\, \overline{\text{LCS}}_i\, |\text{MV}_i|, \qquad m \in \{1.64,\ 3,\ 5.8,\ 6\},
$$

with the menu calibrated to EUR IG in March 2026 (+64%), IG costs in March 2020 (about 3×), the IG index in 2007–2008 (5.8×), and IG blocks in March 2020 (more than 6×), all sourced in this section.

Bangia's model covers only *exogenous* liquidity, the market-wide spread. The *endogenous* part is that your own size moves the price. Man's modelled HY transaction costs by ticket size, \$1mm to \$20mm, span roughly 0.5% to 4.0% of price over 2004–2021 (Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.22, read from a chart), so the cost of a ticket is a function of the ticket. We use the simplest form that respects that evidence:

$$
\text{COL}_i = \tfrac12\, m\, \overline{\text{LCS}}_i\, |\text{MV}_i| \left(1 + \eta \sqrt{\frac{|\text{MV}_i|}{\text{ADV}_i}}\right), \tag{28.16}
$$

with $\eta$ fitted to the desk's own markouts by ticket size *(functional form illustrative)*. Because (28.16) grows faster than linearly in position size, the liquidity cost of the whole book grows faster than linearly in leverage, and that is what turns the leverage ceiling of §28.7 into a fixed point.

### Days-to-liquidate, and the regulatory clocks

A position of $q_i$ dollars in a bond that trades $\text{ADV}_i$ a day, sold at a participation rate $\pi$, takes

$$
T_i = \frac{q_i}{\pi\,\text{ADV}_i} \tag{28.17}
$$

days to exit. Paleologo's example (p.126) is a position of two days' volume at 4% participation: 50 days. For a HY bond that trades \$5mm a day, a \$25mm position at 10% participation is also 50 days *(illustrative)*, which is to say most of a quarter. VaR over a liquidation horizon scales the one-day risk by roughly $\sqrt{T_i}$, and the Basel FRTB rules make that scaling explicit. With base horizon $T = 10$ days and liquidity horizons $LH_j \in \{10, 20, 40, 60, 120\}$, the liquidity-adjusted expected shortfall is

$$
\text{ES} = \sqrt{\text{ES}_T(P)^2 + \sum_{j \ge 2}\left(\text{ES}_T(P, j)\sqrt{\frac{LH_j - LH_{j-1}}{T}}\right)^2}, \tag{28.18}
$$

where $\text{ES}_T(P, j)$ is the 10-day ES from shocking only the risk factors with horizon at least $LH_j$ (Basel Framework MAR33.4; horizons in MAR33.12). A book whose risk is all HY corporate spread (60 days) has $\text{ES} = \text{ES}_T\sqrt{1 + 1 + 2 + 2} = \text{ES}_T\sqrt{6} = \text{ES}_T\sqrt{60/10}$, which is the square-root-of-time rule recovered as a sanity check. For a registered fund, the clock is SEC Rule 22e-4: "highly liquid" means convertible to cash within three business days, "illiquid" means not reasonably expected to be sold in seven calendar days without significantly changing the market value, and illiquid holdings are capped at 15% of net assets.

Which bonds do you sell first? Ben Dor's answer is counterintuitive.

> **[SOURCE EXTRACTION]** *Ben_Dor_Quantitative_Credit_Portfolio_Management p.112:* "a strategy of selling illiquid bonds at the beginning of a liquidity crisis may be more productive than selling liquid bonds first."
>
> **Annotation.** The logic is the cost of waiting. If the LCS of the illiquid bucket widens faster as the crisis deepens, every day you hold it raises its exit cost, so you sell it while the bid exists. In March 2020 most investors did the opposite and sold their most liquid bonds first (O'Hara and Zhou, 2021, *Anatomy of a Liquidity Crisis: Corporate Bonds in the COVID-19 Crisis*, *Journal of Financial Economics*), because that was where the bids were. For a fund with redeemable shares the choice has a second edge: selling liquid bonds first to meet early redemptions leaves the illiquid ones for the investors who stay, which rewards running. That is the next case.

### Case Study: Third Avenue Focused Credit Fund, December 2015

The facts are from the SEC's temporary order (Investment Company Act Release No. 31943, 16 December 2015). The Focused Credit Fund had "\$1.1 billion in estimated net outflows for the year to date through December 9, 2015, which was more than 145% of its remaining net asset value at that date," which puts the remaining NAV near \$0.75bn. Net redemptions in November alone were \$317mm, and the institutional NAV per share fell from \$7.81 to \$7.08 that month. By early December the fund had raised cash to "over \$200 million." On 9 December its board adopted a plan of liquidation, sales of shares were suspended from 10 December, and the SEC's order under §22(e)(3) permitted the suspension of redemptions. The SEC noted that institutional holders would otherwise have redeemed first, to the detriment of retail investors. The unwind took roughly a year.

Now run Theo's 13-week model on the *fund*. Cash of about \$200mm against a burn of about \$73mm a week (\$317mm over November's 4.3 weeks) is a runway of about 2.7 weeks. In the RSSG seat, a borrower with under one quarter of liquidity runway is a going-concern question and a first-day-of-engagement conversation. The fund was the borrower, its redemptions were the debt service, and its portfolio of distressed and stressed bonds was the collateral that could not be sold at the mark in seven calendar days. A systematic desk would have flagged it from public data: a fund-level runway under 13 weeks, a high share of tier-2 holdings, NAV falling while outflows accelerated, and a liquidation cost under (28.16) that was a large fraction of NAV. It would then have done two things. It would not have bought what the fund was certain to sell until the fund had sold it, and it would have been ready with capacity to provide liquidity after the gate, when the price of immediacy was highest and the information content of the selling was lowest (forced, not informed). Ines calls this "the only hand where you know the other player has to fold."

The 13-week model, it turns out, was never about the borrower. It was about the gap between when cash leaves and when assets can be sold, and every leveraged book has that gap.

### Specification for AI Implementation (Block 4): LVaR, Days-to-Liquidate and Runway

What ROBO built from the vague version ("compute liquidity risk"): the average bid-ask over the last year, times the book. It reported \$4mm. The stressed figure was \$23mm *(illustrative)*, and ROBO's comment field read "liquidity is fine on average."

<!-- EXPLAIN: Listing 28.4 -->
> **Code Companion: Listing 28.4.** Bangia eq. The full python listing is in [Appendix F, Listing 28.4](#code-28-4).

Edge cases: zero ADV (a bond that has not traded in the window) is floored at \$1 so the size term is enormous rather than infinite, which is the right sign; a negative weekly burn (net inflows) gives infinite runway; and `credit_col` deliberately takes absolute values, because a short pays the offer just as a long pays the bid.

## 28.6 Drawdown Control: The Two-Threshold Rule, the PM Option and Marking to Bid

The platforms' drawdown rule, as commonly reported, is two numbers: lose 5% of allocated capital and your capital is halved; lose another 2.5% and you are out (WSJ via eFinancialCareers, 5 December 2025; the firm did not comment). Theo's four PMs know the rule better than they know their own positions. The desk head's job is to understand what the rule is for, what it costs, and how a credit book can trip it without anything going wrong.

> **[SOURCE EXTRACTION]** *Paleologo_Advanced_Portfolio_Management p.164:* "Stop-loss rules are a partial hedge for the PM call option. … it is in the interest of the manager to run with the highest possible volatility, independently of her skill."
>
> **Annotation.** A PM paid a fraction $\varphi$ of positive annual P&L $\Pi$ holds a call. If $\Pi \sim N(\mu, \sigma^2)$, the payout is worth $\varphi\left[\mu\,\Phi(\mu/\sigma) + \sigma\,\phi(\mu/\sigma)\right]$, and its derivative with respect to $\sigma$ is $\varphi\,\phi(\mu/\sigma) > 0$ for every $\mu$, skilled or not. The stop-loss caps how much volatility the PM can harvest before the option is taken away. In credit there is a second, sneakier volatility: concentration in names with jump-to-default. A PM can sell default insurance, collect carry for three years, and look like a low-volatility genius until the jump. The stop-loss does not hedge that, because the jump arrives in one print. The Kelly cluster bound of §28.4 does.

### Setting the stop with drift

Model the PM's cumulative P&L as a fraction of allocated capital, $X_t = \mu t + \sigma W_t$ with $\mu = \text{SR}\cdot\sigma$. The probability of touching $-x$ before time $T$ is the classical first-passage result for Brownian motion with drift,

$$
\Pr\left(\min_{t \le T} X_t \le -x\right) = \Phi\!\left(\frac{-x - \mu T}{\sigma\sqrt{T}}\right) + e^{-2\mu x/\sigma^2}\,\Phi\!\left(\frac{-x + \mu T}{\sigma\sqrt{T}}\right), \tag{28.19}
$$

and as $T \to \infty$ the lifetime probability is $e^{-2\mu x/\sigma^2} = e^{-2\,\text{SR}\,x/\sigma}$. Inverting gives the stop that a desk head would set for a target lifetime stop-out probability $P$:

$$
x = \frac{\sigma\,\ln(1/P)}{2\,\text{SR}}. \tag{28.20}
$$

A PM running 6% volatility with a Sharpe of 1, held to a 10% lifetime stop-out probability, gets $x = 0.06 \times 2.303/2 = 6.9\%$, close to the reported 7.5%. At 7.5%, the lifetime probability is $e^{-2.5} = 8.2\%$, and the one-year probability from (28.19) is about 4.5%. A PM with a Sharpe of 0.5 at the same volatility and stop faces a lifetime probability of $e^{-1.25} = 29\%$. The rule is the same for both, and its price is not.

> **[SOURCE EXTRACTION]** *Paleologo_Advanced_Portfolio_Management p.167:* "a two-threshold one (cut capital in half when loss reaches (x/2)%, and liquidate at x% loss). To approximate heavy-tailed returns … returns distribution in the simulation is not Gaussian, but a Student with 6 degrees of freedom." … "The price of safety is higher for lower-Sharpe PMs than higher-Sharpe ones."
>
> **Annotation.** This is the platform rule, simulated. Because the cuts are decided on past P&L and returns are independent of the past, expected P&L under the rule is exactly $\mu$ times expected capital-time, so the price of safety is $\mu$ times the capital-time the rule takes away. Low-Sharpe PMs lose more capital-time, because they hit the first threshold more often. Paleologo's companion line (p.166) is the one to read aloud at the risk committee: "Stop-loss exists to ensure survival of a firm, not to improve the performance of a strategy. There is a price to pay." Block 5 reproduces the simulation and its ranking.

Two credit-specific notes on the rule. First, Grossman and Zhou (1993, *Optimal Investment Strategies for Controlling Drawdowns*) show that the smooth version of the rule keeps exposure proportional to the cushion above the drawdown floor, $\text{exposure}_t = k\,(X_t - (1-x)M_t)$ with $M_t$ the running maximum, which never breaches the floor in continuous time. The two-threshold rule is a two-step approximation of that policy, and it is the approximation the platforms can audit. Second, do not use ratings as stop-losses. Dynkin et al. find that rating-based stop-loss rules "lead to lower portfolio returns" at every threshold they test, with risk reductions much smaller than the returns given up, because downgraded bonds tend to outperform their new rating peers (Dynkin p.419). Use rating as an entry rule, not an exit rule.

### The stop-loss you don't know you have

Paleologo writes (p.163) that "there is the stop-loss that you have, and the one you don't know you have." In credit, the one you don't know you have is the mark. Let a book with gross leverage $G$ be marked to bid on longs and offer on shorts, with average round-trip cost $\overline{\text{LCS}}$. When the bid-ask widens by a factor $m$, the marks move by half the change, and the drawdown in NAV, with no change in any issuer, is

$$
\Delta^{\text{mark}} = \tfrac12\,(m - 1)\,\overline{\text{LCS}}\;G. \tag{28.21}
$$

Theo's desk: $\overline{\text{LCS}} = 0.6\%$, $G = 5$, and the 2007–2008 multiple $m = 5.8$ give $\Delta^{\text{mark}} = 0.5 \times 4.8 \times 0.006 \times 5 = 7.2\%$ of NAV. That is through the 5% cut and within 30 bp of the 7.5% exit, from marks alone. The effective stop is $x - \Delta^{\text{mark}}$. If it is not budgeted before the stress, the rule fires at the bottom, on the day the price of immediacy is highest, and forces the desk to sell to the people who budgeted for it.

> **[SOURCE EXTRACTION]** *BlackRock_Systematic_High_Yield_Credit p.5:* "these managers gave up more excess return in subsequent "Very Positive" regimes than was mitigated on the downside during "Very Negative""
>
> **Annotation.** BlackRock's sample covers the 2013 taper tantrum, 2018, 2020 and 2022, and its finding is that the defensive HY managers who de-risked on the way down lost more on the rebound than they saved. A forced de-risking caused by marks is the worst version of this, because it sells for a reason unrelated to the forecast. Blackstone's systematic credit description states the mirror image: "When credit spreads widen aggressively (often due to market panic rather than fundamental deterioration), the model algorithmically increases credit exposure" (Blackstone_Systematic_Credit p.1). That is possible only for a book whose drawdown budget survived the marks.

### Case Study: March 2020 and March 2026

*March 2020.* The Fed's own retrospective (Sharpe and Zhou, FEDS Notes, 7 October 2020) has IG transaction costs rising from about 30 bp in February to nearly 90 bp in mid-March, IG block-trade costs from 24 bp to over 150 bp by 23 March, and bond mutual fund outflows above \$250bn in March, about 5% of assets. Kargar et al. (NBER WP 27355; *Review of Financial Studies* 2021) estimate that customers' willingness to pay for immediacy rose by about 200 bp per dollar traded at the peak. On 23 March the Fed announced the Secondary Market Corporate Credit Facility. Treat the block-cost numbers as round-trip LCS *(an assumption)*, and (28.21) puts the mark-to-bid hit on a 5× IG book at $\tfrac12 \times (1.50\% - 0.24\%) \times 5 = 3.2\%$ of NAV, two-thirds of the way to the first threshold with no default anywhere. A desk whose rule ignored the marks was cut in the week the Fed announced it would buy. A desk that had budgeted (28.21) kept its gross, and was among the buyers.

*March 2026.* The Iran-war shock forced an unwind of crowded positions, and ExodusPoint, Balyasny, Citadel and Millennium all posted March declines, giving up all or part of their gains from the first two months (Bloomberg, 2 April 2026). HY OAS peaked at 3.46% on 30 March (FRED). EUR IG bid-ask rose to 64% above its January average, and normalizing took 4 weeks in EUR IG, 6 in US HY, 8 in US IG, 13 in EUR HY and more than 14 in EM (MarketAxess data via The DESK, 1 October 2026). The lesson is about correlation of rules, not of assets. When many pods at many firms share a 5% line and similar positions, their stops are one stop. A desk head should estimate, from positioning data and crowding measures (Chapter 9), how much of the book's exposure belongs to trades that other people will be forced out of at the same threshold, and treat that share as having a higher $m$.

### Specification for AI Implementation (Block 5): Stops, Hitting Probabilities and the Mark-to-Bid Shock

What ROBO built from the vague version ("minimize drawdown"): it held cash, as it always does, and reported a maximum drawdown of zero and a Sharpe ratio of "undefined, but excellent."

<!-- EXPLAIN: Listing 28.5 -->
> **Code Companion: Listing 28.5.** Eq. The full python listing is in [Appendix F, Listing 28.5](#code-28-5).

Edge cases: `prob_hit` requires $\sigma > 0$ and $T > 0$; a negative $\mu$ is allowed (a losing PM) and the formula still holds; `stop_for_lifetime_prob` is undefined for a non-positive Sharpe ratio, for which every stop is eventually hit; and the two-threshold simulation must measure loss on *initial* allocated capital, as Paleologo specifies, because measuring it on current capital after the cut silently moves the exit.

## 28.7 The Leverage Band and the κ Problem

Every term is now on the table, and they assemble into the one equation to tape to the monitor. The floor is (28.2). The ceiling comes from the drawdown limit. Let the book's annual NAV return be $G(\mu_{\text{GMV}} + \kappa\,\sigma_{\text{GMV}} Z)$, with $\sigma_{\text{GMV}} = \sigma_{\text{DTS}}/\sqrt{N_{\text{eff}}}$, $\mu_{\text{GMV}} = \text{SR}\,\sigma_{\text{GMV}}$, $Z$ a standardized shock with distribution $F$, and $\kappa \ge 1$ the factor by which realized volatility exceeds predicted volatility in a drawdown. Require $\Pr(\text{loss} > \text{DD}_{\max}) \le p_{\text{loss}}$ (we write $\text{DD}_{\max}$, not $D_{\max}$, because $D$ is duration). With $z_p = -F^{-1}(p_{\text{loss}})$, the condition is $G\sigma_{\text{GMV}}(\kappa z_p - \text{SR}) \le \text{DD}_{\max}$. In credit the drawdown budget must also absorb the liquidation and mark-to-bid cost $\text{COL}(G)$, as a fraction of NAV, which arrives in the same tail event. So

$$
\frac{\sqrt{N_{\text{eff}}}}{\sigma_{\text{DTS}}}\cdot\frac{r_{\min}}{\text{SR}} \;\le\; G \;\le\; \frac{\sqrt{N_{\text{eff}}}}{\sigma_{\text{DTS}}}\cdot\frac{\text{DD}_{\max} - \text{COL}(G)}{\kappa z_p - \text{SR}}. \tag{28.22}
$$

The ceiling is a fixed point, because $\text{COL}$ grows with $G$. With the linear mark-to-bid cost of (28.21), $\text{COL}(G) = c_1 G$ with $c_1 = \tfrac12(m-1)\overline{\text{LCS}}$, and writing $A = \sqrt{N_{\text{eff}}}/(\sigma_{\text{DTS}}(\kappa z_p - \text{SR}))$,

$$
G_{\max} = \frac{A\,\text{DD}_{\max}}{1 + A\,c_1} \;<\; \frac{\text{DD}_{\max}}{c_1} = \frac{2\,\text{DD}_{\max}}{(m-1)\,\overline{\text{LCS}}}. \tag{28.23}
$$

The right-hand bound is the **liquidity speed limit**: no amount of breadth, Sharpe or model confidence takes a credit book's leverage above it, because as $A \to \infty$ the ceiling converges to it. At $\text{DD}_{\max} = 7.5\%$, $m = 5.8$ and $\overline{\text{LCS}} = 0.8\%$, the speed limit is $0.15/0.0384 = 3.9\times$.

> **[SOURCE EXTRACTION]** *Paleologo_Advanced_Portfolio_Management p.175–176:* "we … assume that realized portfolio volatility is inflated by a positive factor κ … with values between 1 (if we really believe in models) and 3 (if we are skeptical)." … "In practice, we want to set −κF⁻¹(p_loss) between 4 and 6."
>
> **Annotation.** In credit, $\kappa$ has an observable cousin: the ratio of stressed to calm relative-spread volatility, $\sigma_{\text{rel}}$ in a stress window over $\sigma_{\text{rel}}$ in the calibration window. Estimate it by bucket, because the CCC ratio in 2026 is not the IG ratio. And note that credit has two stress multipliers, not one: $\kappa$ inflates the volatility, and $m$ inflates the bid-ask. They hit together, which is why (28.22) charges both in the same tail.

Theo's HY PM: $N_{\text{eff}} = 40$, $\sigma_{\text{DTS}} = 5\%$, $\text{SR} = 2$, $\kappa z_p = 4$, $\text{DD}_{\max} = 7.5\%$ and $r_{\min} = 5\%$ *(all illustrative)*. Without liquidity, the band is $[3.16,\ 4.74]$. Charge the 2008 mark-to-bid with $\overline{\text{LCS}} = 0.8\%$ and the ceiling falls to $4.74/(1 + 63.2 \times 0.0192) = 2.14$, below the floor. **The band is empty.** The liquidity term closed it. The desk head has four levers, and all of them are in this chapter: cut $\overline{\text{LCS}}$ (route beta management to the overlay, use smaller tickets and PT, §28.3), lower the PM's hurdle $r_{\min}$, buy a wider drawdown limit with a lower $p_{\text{loss}}$ elsewhere on the platform, or raise $\text{SR}$ by adding uncorrelated signals (§28.8). Halving the LCS and accepting a 4% hurdle reopens the band at about $[2.5,\ 3.0]$.

> **Desk Myth vs. Desk Reality.** *Myth:* "A higher-Sharpe PM needs less leverage." *Reality:* a higher Sharpe *requires* less (the floor falls) and *permits* more (the ceiling rises, because $\kappa z_p - \text{SR}$ shrinks). Paleologo makes the same point about the idiosyncratic share of variance, $p_{\text{idio}}$ (p.178): "When the percentage idio p_idio increases, it works its magic on both sides of the equation: the lower admissible leverage decreases and the highest admissible leverage increases." IDO or it didn't happen, in leverage form: idiosyncratic risk is the only risk that widens the band from both ends.

### Specification for AI Implementation (Block 6): The Leverage Band

What ROBO built from the vague version ("use as much leverage as is safe"): the ceiling without the floor, and without COL. It reported 4.74× and the word "safe."

<!-- EXPLAIN: Listing 28.6 -->
> **Code Companion: Listing 28.6.** Eq. The full python listing is in [Appendix F, Listing 28.6](#code-28-6).

Edge cases: $\kappa z_p \le \text{SR}$ means the PM's Sharpe exceeds the stress quantile and the formula has no ceiling, which is a sign the inputs are wrong, so the function raises; `col_fn` must be increasing in $G$ for the fixed point to be unique; and the floor uses the *forecast* Sharpe, so a floor computed from a backtest Sharpe is a floor computed from the wrong number (deflate it, Chapter 26).

## 28.8 Running Ex-RSSG Analysts Alongside PhDs

Sunita is explaining a fulcrum analysis to Kaz. Kaz, delighted, asks whether the fulcrum security is "the one at the pivot of the lever, where a small force moves a large load." Sunita says yes, actually: it is the class where value breaks, so a small change in enterprise value moves its recovery the most. Kaz has, for once, read a legal term correctly by reading it as physics. It is the right picture of the team: two vocabularies for one sensitivity.

The team is a production function. Two signals with information coefficients $\text{IC}_1$, $\text{IC}_2$ and correlation $\rho$, combined optimally (regress the forward return on both standardized signals), have a combined IC equal to the multiple correlation,

$$
\text{IC}_c^2 = \mathbf{ic}^{\top} C^{-1}\, \mathbf{ic} = \frac{\text{IC}_1^2 + \text{IC}_2^2 - 2\rho\,\text{IC}_1\text{IC}_2}{1 - \rho^2}. \tag{28.24}
$$

Two signals with IC 0.05 each combine to 0.056 if they correlate at 0.6 (another price factor), 0.071 if they are uncorrelated (a docket or covenant signal), and 0.079 at $\rho = -0.2$. The value of an ex-RSSG analyst to a quant book is mostly the $\rho$, not the IC: documents, dockets and process are information the price factors do not contain.

Breadth has a cost the formula hides. Suppose a PM's edge per bet dilutes as coverage grows, $e(N) = e_0 N_c/(N + N_c)$, with $N_c$ the coverage at which attention halves the edge. Then $\text{IR} \propto e(N)\sqrt{N} \propto \sqrt{N}/(N + N_c)$, whose derivative vanishes where $N + N_c = 2N$:

$$
N^\ast = N_c. \tag{28.25}
$$

Optimal coverage equals the dilution scale. Past it, each new name lowers the IR. A team helps only by adding coverage at the *new* member's own $N_c$, not by stretching the PM's.

> **[SOURCE EXTRACTION]** *Paleologo_Advanced_Portfolio_Management p.149:* "The power of diversification is great. It is not a skill: it is a skill multiplier." … "Beyond a certain threshold, coverage and breadth increase at the expense of accuracy."
>
> **Annotation.** Equation (28.25) is the second sentence, made precise. Its credit corollary is the hiring rule: an analyst is worth adding when her names are ones the book does not cover and her hit rate on them, measured with the standard error of (28.6), is at least the PM's. Paleologo also warns (p.131) that a platform run "as a fund of funds" pays "the opportunity cost of not adopting more advanced techniques": pods that never share signals cannot combine them through (28.24).

### Case Study: Aligned Signals, and the Hybrid Shop

Barclays' QPS and credit research teams, as reported by Impax (19 September 2025), measured the effect directly in US investment grade. The issuer-level hit rate was about 58% overall, about 66% when analyst and quant signals agreed, and about 52% when they conflicted. Concentrating on aligned decisions lifted excess return from 2.0% to 3.7% a year and the IR from 1.09 to 1.71, and doubling exposure to aligned signals gave 4.1% with an IR of 1.83. The industry has priced the same conclusion: in late October 2025, Ares agreed to buy BlueCove, a systematic fixed-income manager with about \$5.5bn of AUM and about 60 staff, and to rebrand it Ares Systematic Credit (Alternative Credit Investor, 30 October 2025; see Chapter 4). The design rule that follows is a division of labour. Analysts own $L$, $L_{\max}$ and the document features (PRS, Chapter 13); PhDs own $\lambda^{\mathbb{P}}$, $\sigma_{\text{DTS}}$ and the covariance; and every analyst view is logged in the Edge Ledger (Chapter 3) with timestamp, horizon and confidence, so that its IC, its $\rho$ and its hit rate are measured rather than remembered. The ROBO spec is the contract between the two cultures: if a view cannot be written as a field with units, it is not yet a view.

<!-- EXPLAIN: Listing 28.7 -->
> **Code Companion: Listing 28.7.** Eq. The full python listing is in [Appendix F, Listing 28.7](#code-28-7).

## 28.9 The PM Dashboard: The 13-Week Model, Reborn

Theo's USB stick finally earns its keep. The PM dashboard asks the question the 13-week model always asked (do we make it to the other side of the quarter?) about the desk instead of the borrower, and answers it with every formula in this chapter on one screen. Mags reads it top to bottom and asks who adjusted it. Theo points to the equation number next to each line.

| Panel | Metric | Formula | Alarm *(illustrative thresholds)* |
| :--- | :--- | :--- | :--- |
| Leverage | $G$ against floor, ceiling and speed limit | (28.2), (28.22), (28.23) | $G$ above the ceiling, or band empty |
| Breadth | $N_{\text{eff}}$, $1/H$ on issuers, ES share of top decile | (28.4), Procedure 8.1 | $N_{\text{eff}} < 25$ |
| Horizon | Net alpha by signal and tier | (28.7) | Any signal traded with negative net alpha |
| Sizing | Capped half-Kelly vs actual, by issuer and cluster | (28.11)–(28.14) | Actual above cap; cluster $\sum fL \ge 1$ |
| Liquidity | Stressed COL, days-to-liquidate, FRTB-style ES | (28.16)–(28.18) | More than 20% of gross beyond 20 days |
| Drawdown | Realized loss plus $\Delta^{\text{mark}}$ against $x/2$ and $x$ | (28.21) | Budget used above 80% of $x/2$ |
| Runway | Weeks of cash against margin and redemption burn | Block 4 | Under 13 weeks |
| Team | Hit rate and SE by signal and analyst | (28.6) | Hit rate within one SE of 50% after a year |

### Specification for AI Implementation: `pm_playbook_engine`

**Input schema (one row per bond; internal identifiers only, never a CUSIP the spec did not supply).**

| Column | Type | Units | Notes |
| :--- | :--- | :--- | :--- |
| `bond_id`, `issuer_id`, `sector` | str / int | — | Net to `issuer_id` before breadth and Kelly |
| `tier` | int | 0, 1, 2 | §28.3 ladder |
| `mv_usd` | float64 | USD | Signed; marked at bid (long) or offer (short) |
| `spr_dur`, `spread` | float64 | years, decimal | $D^{\text{spr}}$ and OAS ($s$) |
| `sigma_rel` | float64 | decimal / yr | Relative spread volatility |
| `lcs`, `adv_usd` | float64 | decimal, USD/day | Calm round-trip LCS; trailing ADV |
| `lam_p`, `lgd_mean`, `lgd_max` | float64 | 1/yr, decimal | $\lambda^{\mathbb{P}}$ (never $\mathbb{Q}$); $L$ and its document-implied worst case |

Desk parameters (NAV, $\text{DD}_{\max}$, $\kappa z_p$, SR, $r_{\min}$, $m$, the two stop levels, realized drawdown, cash, liquid sleeve, weekly burn, participation, $\rho_w$, $\rho_a$, the Kelly edge s.e.) are a dictionary with units in the key names. The engine is pure: no I/O, no clock, seeded.

<!-- EXPLAIN: Listing 28.8 -->
> **Code Companion: Listing 28.8.** --- Final block: pm_playbook_engine --------------------------------------------. The full python listing is in [Appendix F, Listing 28.8](#code-28-8).

The one non-obvious line is `sigma_book`. Equation (28.22) is written for $N_{\text{eff}}$ equal, independent bets of volatility $\sigma_{\text{DTS}}$, so the engine backs out the per-bet volatility that, with the measured $N_{\text{eff}}$, reproduces the book's actual volatility per dollar of GMV: $\sigma_{\text{DTS}} = \sigma_{\text{GMV}}\sqrt{N_{\text{eff}}}$. Because of how (28.4) is defined, this per-bet volatility is exactly the GMV-weighted average bond volatility $\sum_i |w_i|\sigma_i$, which makes a useful audit: the band built from $(N_{\text{eff}}, \sigma_{\text{DTS}})$ reproduces the book's measured risk per dollar of GMV by construction. Feeding in a median or unweighted bond volatility breaks that identity, and the band with it.

## 28.10 Desk Debrief

- **Allocate risk, not dollars.** Give each PM three budgets: volatility, drawdown, and liquidity (days-to-liquidate and stressed cost). The dollars fall out of the division.
- **Breadth is issuers, not CUSIPs.** Use $N_{\text{eff}}$ from (28.4). A residual correlation of 1% caps any credit book at about 100 bets, and a year of P&L on 40 bets measures the hit rate with a standard error the size of the edge.
- **Every signal pays its rake.** $h^\ast = \ln 2 \cdot c^{\text{RT}}/\alpha_0$: fast signals in the index layer, slow ones in cash, docket alpha in stressed bonds. The overlay manages beta so the cash books keep their IDO.
- **Kelly in credit is $f^\ast = 1/L - \lambda^{\mathbb{P}}/c$, inside a ruin boundary set by the documents.** The worst recovery sets $1/L_{\max}$, not the average one. Half Kelly is full Kelly with honest standard errors. Clusters obey $\sum f L < 1$. Never use $\mathbb{Q}$, never use a smoothed mark.
- **The 5× is the base case.** IG round-trip cost went from 0.59% to 3.40% in 2007–2008. Use $\text{COL} = \tfrac12 m\,\overline{\text{LCS}}\,|\text{MV}|$ with a size term, and treat a fund with under 13 weeks of runway as a going-concern question.
- **The stop you don't know you have is the mark.** $\Delta^{\text{mark}} = \tfrac12(m-1)\,\overline{\text{LCS}}\,G$ belongs inside $x$, and $x = \sigma\ln(1/P)/(2\,\text{SR})$ is how you set $x$.
- **Tape (28.22) to the monitor, and remember the speed limit** $G < 2\,\text{DD}_{\max}/((m-1)\,\overline{\text{LCS}})$, which no breadth can lift.
- **An analyst's value is her $\rho$, not her IC.** Optimal coverage is $N^\ast = N_c$. Log every view in the Edge Ledger, or it is a memory, not a signal.

**The Spec You Hand the Robot.**

```text
ROLE: Build pm_playbook_engine: a pure, seeded Python function (numpy/scipy/pandas only)
mapping (book DataFrame, desk dict) -> one dashboard Series. No I/O, no clock, no network.
UNITS: USD float64; spreads, LCS, vols, drawdowns as decimals; hazards per year under P;
days are trading days; leverage G = gross MV / NAV. Never invent identifiers.
BREADTH: net to issuer; N_eff = (sum|w|sigma)^2 / (w' S w) on the idiosyncratic covariance;
refuse near-zero variance. Report 1/H beside it.
SIZING: f* = smaller root of sigma^2 L f^2 - (cL + sigma^2) f + (c - lam L) = 0 (rationalized);
0 if c <= lam L; multiply by 1/(1 + se^2); cap at 1/L_max (documents) and the cluster
bound sum f L < 1. Merton's mu/sigma^2 is for comparison only.
LIQUIDITY: COL = 0.5 m LCS |MV| (1 + eta sqrt(|MV|/ADV)), longs and shorts; T = |q|/(pi ADV);
FRTB ES with horizons 10/20/40/60/120; runway = (cash + (1-h) liquid) / weekly burn.
DRAWDOWN: used = realized + 0.5 (m-1) LCS G; compare with x/2 and x on INITIAL capital.
BAND: floor sqrt(N)/sigma * r_min/SR; ceiling = fixed point of G = A (DD - COL(G)), A =
sqrt(N)/(sigma (kz - SR)); raise if kz <= SR; report the speed limit 2 DD/((m-1) LCS).
TESTS: every assert in Blocks 1-7 and the final block; MC vs closed form for the hitting
probability (Brownian bridge) and the hit-rate IR; the 50-day and sqrt(6) regression tests.
FORBIDDEN: Q-measure hazards in Kelly; volatility from marks that have not traded;
silently filling a missing ADV or L_max (raise instead).
```

### Exercises

1. **The empty band.** For Theo's HY PM of §28.7, find the largest average LCS at which the band is non-empty with $r_{\min} = 5\%$. Then find the smallest $N_{\text{eff}}$ at which it is non-empty with no liquidity charge at all, and explain why adding names does not help once the speed limit binds. *(Hint: hold the per-bet IR fixed, so that $\text{SR}$ rises with $\sqrt{N_{\text{eff}}}$, and see which side of (28.22) moves.)*
2. **Kaz's 93%, re-audited.** The same B3 bond's 5-year CDS trades at 450 bp. Bootstrap $\lambda^{\mathbb{Q}}$ with $L = 0.6$ and show that (28.11) returns zero. Then use $\lambda^{\mathbb{P}} = 1.5\%$ and compute $f^\ast$. Finally, Sunita reports that the credit agreement permits a non-pro-rata uptier: set $L_{\max} = 1$ with a Beta recovery of mean 0.6 and recompute. Which of the three numbers would you defend at the risk committee, and to whom does it belong?
3. **Your fund is the borrower.** A credit fund has \$150mm of cash, a \$400mm tier-1 sleeve that can be sold at a 3% haircut in stress, prime-broker margin calls of \$10mm a week, and redemptions of \$25mm a week. Compute the runway. Then double the margin haircuts (margin calls to \$20mm a week) and apply the 2008 multiple to the sleeve's cost. Is the fund a going concern by Theo's standard?
4. **Mags's adjusted number.** Mags asks which line of the dashboard is "adjusted." Name the three inputs to (28.22) that are estimates rather than observations, give each a standard error, and propagate them to a confidence interval on the ceiling. Is the band still a band?
5. **ROBO and the stop-loss.** Told "never hit the 7.5% stop," ROBO cuts gross to zero at a 3.75% loss and never restarts. Show, using the identity that expected P&L equals $\mu$ times expected capital-time, how much expected return this costs a Sharpe-1, 6%-vol PM relative to Paleologo's two-threshold rule. Then write the spec sentence that would have stopped it.

## 28.11 Sources and Links

### Deep-Dive Resource Graph

**Podcasts**
- AIMA podcast, Goldman Sachs prime insights on multi-strategy growth and hiring (September 2026), as reported by Hedgeweek (episode details not verified; title only).
- *Odd Lots* (Bloomberg) and *Flirting with Models* (Corey Hoffstein): episodes on multi-manager pod economics, risk budgeting and position sizing (title only).

**Practitioner Writing**
- Hedgeweek, "Multi-strats may need to accelerate PM hiring as assets surge" (15 September 2026): https://www.hedgeweek.com/multi-strats-may-need-to-accelerate-pm-hiring-as-assets-surge/
- Hedgeweek, Millennium and Citadel 2025 returns (5 January 2026): https://www.hedgeweek.com/millennium-and-citadel-post-double-digit-2025-gains-but-lag-smaller-hedge-funds/
- The Daily Upside on Point72's 2025 return and 190 pods (23 February 2026): https://www.thedailyupside.com/finance/hedge-funds/point72-tops-citadel-and-millennium-returns-as-multi-strategy-funds-expect-another-strong-year/
- eFinancialCareers on the commonly reported drawdown rule (5 December 2025): https://www.efinancialcareers.com/news/pratik-madhvani-glen-scheinberg
- Bloomberg, "Hedge Funds Walloped by a Month of Turmoil Sparked by War" (2 April 2026): https://news.bgov.com/new-york-brief/hedge-funds-walloped-by-a-month-of-turmoil-sparked-by-iran-war
- *Title only:* Cambridge Associates, *2024 Hedge Fund Discretionary Expense Summary* (October 2025); Impax on Barclays QPS aligned signals (19 September 2025); The DESK on MarketAxess bid-ask recovery (1 October 2026) and on Cboe iBoxx futures blocks (16 October 2026); ISDA, *CDS Market Dynamics: Five Years of Activity and a Record 2025* (29 July 2026).
- Shelf: Paleologo, *Advanced Portfolio Management* (chs. 6, 8, 9, 10); Ben Dor et al., *Quantitative Credit Portfolio Management* (DTS, LCS); Dynkin et al., *Systematic Investing in Credit* (horizons, turnover, rating stop-losses); Man Group (2022, 2023); BlackRock and Blackstone systematic credit papers; Bolder; Bohn and Stein.

**Academic Papers**
- Gârleanu and Pedersen (2013), *Dynamic Trading with Predictable Returns and Transaction Costs*, *Journal of Finance* 68(6): https://www.nber.org/papers/w15205
- Bangia, Diebold, Schuermann and Stroughair (1999), *Modeling Liquidity Risk, With Implications for Traditional Market Risk Measurement and Management*: https://ideas.repec.org/p/wop/pennin/99-06.html
- Kargar, Lester, Lindsay, Liu, Weill and Zúñiga (2021), *Corporate Bond Liquidity During the COVID-19 Crisis*: https://www.nber.org/papers/w27355
- Sharpe and Zhou (2020), *The Corporate Bond Market Crises and the Government Response*, FEDS Notes: https://www.federalreserve.gov/econres/notes/feds-notes/the-corporate-bond-market-crises-and-the-government-response-20201007.html
- Garivaltis (2019), *Game-Theoretic Optimal Portfolios for Jump Diffusions*, *Games* 10(1): https://arxiv.org/abs/1812.04603
- *Title only:* Bermin and Holm (2026), *Kelly trading when asset prices have jumps* (CHECK); O'Hara and Zhou (2021), *Anatomy of a Liquidity Crisis*; Grossman and Zhou (1993), *Optimal Investment Strategies for Controlling Drawdowns*; MacLean, Thorp and Ziemba (2010), *Good and Bad Properties of the Kelly Criterion*; Almgren and Chriss (2001), *Optimal Execution of Portfolio Transactions*; Clarke, de Silva and Thorley (2002), *Portfolio Constraints and the Fundamental Law of Active Management*; Buckle (2004), *How to Calculate Breadth*.

**Data & Code (regulatory sources included)**
- SEC Release IC-31943 (Third Avenue, 16 December 2015): https://www.sec.gov/files/rules/ic/2015/ic-31943.pdf
- SEC Rule 22e-4 small-entity compliance guide: https://www.sec.gov/files/secg-liquidity.htm
- Basel Framework MAR33 (FRTB liquidity horizons): https://www.bis.org/basel_framework/chapter/MAR/33.htm?inforce=20230101&published=20200605
- Federal Reserve, *Financial Stability Report* (May 2026): https://www.federalreserve.gov/publications/files/financial-stability-report-20260508.pdf
- FRED, ICE BofA OAS series: https://fred.stlouisfed.org/series/BAMLH0A0HYM2 ; https://fred.stlouisfed.org/series/BAMLC0A0CM ; https://fred.stlouisfed.org/series/BAMLH0A3HYC
- This chapter's reference implementation: Blocks 1–7 and `pm_playbook_engine` above, which run in order in one interpreter.

<!-- STATUS: COMPLETE -->
