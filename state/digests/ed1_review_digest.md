
==== 01_ch01_anthology_and_landscape.md (13,019 words)
# Chapter 1: The Anthology of the Desk & The Modern Quant Credit Landscape
## 1.1 The Epistemological Clash: PJT RSSG vs. The Automated Market Maker
### Why the Hybrid PJT RSSG + Quant Architect Owns the Future
## 1.2 Evaluating the Market Set in Quantitative Credit
## 1.3 The Bid Equation, Derived
### 1.3.1 Setup and units (measure: $\mathbb{P}$, the desk's own beliefs)
### 1.3.2 The inventory term
### 1.3.3 The toxicity term: Bayes on the RFQ
### Specification for AI Implementation
### Deep-Dive Resource Graph
## 1.4 The Anthology, Part A: Measuring the Risk You Catch (Ben Dor; Veronesi)
# One-factor threshold model: Monte Carlo default rate matches p; tails fatten with rho
# --- a Ford-sized fallen angel, March 2020 style (all numbers illustrative) ---

==== 02_ch02_revolutions_in_credit_trading.md (16,341 words)
# Chapter 2: The Revolutions in Credit Trading
## 2.1 The Desk View: Execution Certainty and a Modelable Cost
## 2.2 Revolution 0: TRACE, or the Dataset Appears
### 2.2.1 The dissemination timeline
### 2.2.2 The caps: censoring as a data problem
### Deep-Dive Resource Graph
## 2.3 Revolution 1: From Phone to RFQ
### 2.3.1 The adoption S-curve, with an honest ceiling
### 2.3.2 The RFQ as an auction: why eleven anchored dealers are worth about two
## 2.4 Revolution 2: All-to-All, or the Buy Side Learns to Quote
### Deep-Dive Resource Graph
## 2.5 Revolution 3: Automation, or Algos Answering Algos
### 2.5.1 The router as a cost-minimization problem
## 2.6 Revolution 4: Portfolio Trading
### 2.6.1 What a dealer bids for a basket
### 2.6.2 Case Study: The Portfolio-Trading Cycle, 2021–2026
## 2.7 Revolution 5: ETFs as the Liquidity Backbone
### 2.7.1 The ETF discount as the price of immediacy
### Deep-Dive Resource Graph
## 2.8 Revolution 6: Non-Bank Liquidity Providers, and the Blocks That Stayed on the Phone
## 2.9 Why This Made Systematic Credit Possible: The Data-Exhaust Theorem
### 2.9.1 Units first: LCS and the Man decomposition
### 2.9.2 The theorem: cost sets breadth, and breadth sets the information ratio
### 2.9.3 Case Study: Two Shocks, Five Years Apart (March 2020 and April 2025)
### Specification for AI Implementation
## 2.10 Desk Debrief
- **Liquidity used to be a relationship and is now a variable.** A bond's value lives in its documents, and its tradability lives in its data exhaust. A systematic strategy needs both certainty of execution and a cost it can model (`Man_Revolutions p.4`), and each revolution improved one or both.
- **TRACE is censored, not missing.** `5MM+` and `1MM+` hide the blocks. Ben Dor's imputed caps imply Pareto tail indices of about 5/3 (IG) and 4/3 (HY), both with infinite variance. Train on the capped feed you will see live, and deduplicate affiliate echoes before fitting anything.
- **Fit adoption with a ceiling, and get the ceiling from outside the data.** Two points cannot identify $K$, and a fitted $K$ equal to the last observation is a warning, not a result. IG is around half electronic and HY has been near a third for four years. The gap between them is the structural fact.
- **Eleven anchored dealers are worth about two.** $n_{\text{eff}} = n/(1 + (n-1)\phi)$, capped at $1/\phi$. A falling cover gap is consistent with competition and with herding, so measure the winner against an independent fair value.
- **Route on all-in cost, including the cost of failing.** $J_p = \pi_p c_p + (1-\pi_p)\kappa$. Try all-to-all first only when the fill odds exceed leakage divided by savings. Near an LMT, leakage jumps and the formula agrees with Mags.
- **Protocol share is a regime, not a trend.** PT went from boom (2021) to bust (2022) to infrastructure (19.8% of customer volume, Q1 2026). Label every share with its denominator, and treat the ETF–NAV basis as the regime switch.
- **Cheaper plumbing makes the same signal a better strategy.** $\mathrm{TO}^\star \propto 1/c^2$ and $\alpha^{\text{net}\,\star} \propto 1/c$. Cutting cost from 12 to 7.5 bp is worth 2.56 times the turnover and 1.6 times the net alpha.
- **Theo's edge lives where the exhaust is thinnest.** About 90% of blocks still trade by phone or chat. The `5MM+` world of stressed names and ad hoc groups is where the router hands control to a person, and that person should have read the credit agreement.
### The Spec You Hand the Robot
Build `ch02_electronification_trend.py` with four functions and one sanity table. (1) `fit_adoption(years, shares, K=None|float|"fit")`: generalized-logit OLS for a fixed ceiling, plus a bounded three-parameter `curve_fit` diagnostic ($K \in [0.05,1]$, $r \in (0,2]$, `maxfev=10000`, logit-OLS fallback, a "not identified" note). Clip shares to $[10^{-4}, 1-10^{-4}]$, refuse a single point, reject $K \le \max(\text{share})$, center years on 2015, and return a 2026–2030 projection inside $(0, K)$. (2) `rfq_best_of_n(theta, n, phi)`: seeded Monte Carlo ($2\times10^5$ draws) of best quote and cover gap with anchoring share $\phi$, checked against $\phi\theta + (1-\phi)\theta/n$ and $(1-\phi)\theta/(n-1)$ within 2%, and returning $n_{\text{eff}} = n/(1+(n-1)\phi)$. (3) `lcs_spread_quoted`, `lcs_price_quoted` and `man_tc_bp`: spreads in decimal, LCS round trip, TC one way in bp, agreement within 5% for a 5.5-year bond with a 10 bp bid-offer. (4) `optimal_turnover(k, c)` returning $(k^2/4c^2,\ k^2/4c)$, verified by grid search, and `route(lines, kappa_bp)` minimizing $J = \pi c + (1-\pi)\kappa$ per line, plus the sequential odds rule. Every number in the demo is either sourced in `OBS.source` or labeled illustrative. Every check is an `assert`, collected and printed as a table.
  [...truncated]
### Exercises
### Deep-Dive Resource Graph

==== 03_ch03_pjt_rssg_cognitive_bridge.md (17,848 words)
# Chapter 3: Cognitive Rewiring, From PJT RSSG to Systematic Desk Head
## 3.1 From Survival Questions to Distributions
### 3.1.1 The two-point distribution and the variance it hides
### 3.1.2 Three outcomes, and the law of total variance
### 3.1.3 Horizon: the desk does not hold to resolution
### 3.1.4 The USB stick gets a job
## 3.2 The RFQ as a Poker Hand: Glosten–Milgrom for Request-for-Quote
### 3.2.1 The binary model
### 3.2.2 Making $\pi$ a function of the RFQ
### 3.2.3 Many dealers: the winner's curse
## 3.3 Markouts: The Hand History
### 3.3.1 Definition and sign convention
### 3.3.2 The decomposition
### 3.3.3 IDO markouts: strip beta before you accuse anyone
### 3.3.4 Counterparty scores, shrunk
### 3.3.5 Survivorship: only fills have markouts
## 3.4 The Bayesian 8-K: Updating a Default Distribution in Four Business Days (or Four Minutes)
### 3.4.1 The 8-K as a set of signals
### 3.4.2 The update
### 3.4.3 The base-rate trap
## 3.5 The RSSG Edge Ledger
## 3.6 Who at This Table Knows About the LMT?
### 3.6.1 The anatomy of pre-LMT flow
### 3.6.2 A sequential detector
### 3.6.3 The information wall is a feature
## 3.7 Case Study: Serta Simmons, June 22, 2020, Seen From a Market Maker's Blotter
## 3.8 The Engine: RFQ Adverse Selection, Markouts, 8-K Updates and the Pre-LMT Detector
### Specification for AI Implementation
## 3.9 Desk Debrief
*Thursday, 4:40 p.m. The lender call was Monday. The Brambleworth mid is 81.*
Theo has printed the markout. He knows that printing things is a banker's tell, and he does it anyway, because some numbers deserve paper. The dealer who won Friday's auction bought fifteen million at 85¾ and is now sitting on an IDO markout of about $-500$bp of price. Theo's counterfactual at 85½ is about $-470$bp. He lost the auction by a quarter of a point and, in doing so, avoided roughly \$600,000 of idiosyncratic loss *(illustrative; the hand of §3.3)*.
"I was right," he says.
"You were second," says Ines. "Second is not a strategy. Second is a coin that landed well. Why did you bid three-quarters under Kaz?"
Theo thinks about it honestly. "It felt wrong. Friday, lender call Monday, a distressed-fund account, fifteen million."
"That's four features and a flinch. The flinch was $\pi(x)$ with no calibration. Everything in this chapter is the flinch, written down, fitted and checked against the hand history. Do it on the next five thousand RFQs, then tell me you were right."
Kaz, without turning around: "I've replaced the Gaussian with a two-point mixture."
"Progress," says Mags. "Now it can be wrong in two places at once."
Theo puts the USB stick on the desk next to the printout. It still holds the 13-week model, and it now also holds a column called `liquidity_runway_weeks`. It is no longer emotional support. It has a refresh cadence and a decay horizon, which is more than most emotional support can say.
- **A survival question is a distribution with the variance left out.** The price is the mean. The dealer is paid for the conditional variance over the *holding horizon*, $\sigma_V^2(h)$, not over the life of the case, and a calendar event inside the horizon (a lender call, an 8-K deadline, a grace-period expiry) moves that variance more than any covenant does. Moyer's 62.5% was always a two-point distribution.
- **A bid is a posterior, not a markup.** $b = \mathbb{E}^{\mathbb{P}}[V \mid \text{client sells}]$, which for a symmetric two-point value is $m - \pi\,\sigma_V$ (3.1). The uninformed seller pays $\pi\sigma_V$ for the privilege of trading in a market that contains informed sellers. Charging it is what keeps you at zero; skipping it makes you the client's free data vendor.
- **Winning is information.** With $n$ dealers in competition, condition on winning: shade by $w(n)\,\sigma_V$ and carry the inventory term (3.2). The hands you lose look better than the hands you win. That is the winner's curse, and a backtest run on fills alone cannot see it.
- **Markouts are the hand history; IDO markouts are the honest hand history.** Measure at 1, 5 and 20 business days, strip index-spread and Treasury beta first, shrink counterparty scores toward zero, and never compute a markout against a mid you have not checked for staleness. A raw markout will accuse a pension fund of insider trading for owning beta.
  [...truncated]
### The Spec You Hand the Robot
### Exercises
### Deep-Dive Resource Graph

==== 04_ch04_inside_the_systematic_credit_industry.md (14,370 words)
# Chapter 4: Inside the Systematic Credit Industry
## 4.1 The Five Businesses Called "Systematic Credit"
## 4.2 Why Credit Lagged Equities by Twenty Years
## 4.3 The Six-Axis Framework Map
### Scoring the breadth column: the fundamental law with issuer clustering
## 4.4 Alpha Families: What Each Shop Thinks It Is Harvesting
### Value is the gap between Q and P
### The rest of the menu
## 4.5 The Data Stack and the Replication Crisis
### Case Study: The Day the Factor Zoo Got Audited (2019–2026)
## 4.6 Portfolio Construction: Guard Rails, Autopilot, GPS
### The risk unit: DTS
### Man's three layers, and the cost of changing your mind
### Nuveen's identity, or the 13-week model with a covariance matrix
## 4.7 Execution: The Revolution That Made the Industry
### Break-even turnover
### Case Study: Man Numeric's Execution Migration, 2021–2023
## 4.8 Capacity: How Big Before You Are the Market
### Specification for AI Implementation
## 4.9 Risk: Defense Without Beta
## 4.10 Case Study: From KMV to Blackstone Corporate Bond Strategies (1990s–2026)
## 4.11 The Genealogy of Quant Credit and the Empty Cells
## 4.12 Desk Debrief
- **"Systematic credit" is five businesses with five binding constraints:** capacity and costs for long-only, financing and crowding for long/short, breadth for allocators, rebalance predictability for ETFs, and adverse selection for algorithmic dealers. Ask which constraint binds before you ask about factors.
- **The alpha column is one memo. The money is in the plumbing.** Every value signal is a Q-minus-P gap (4.5). Know whether you are harvesting risk premium, liquidity or mispricing, because each one loses money in a different crisis.
- **Bonds are not bets; issuers are.** $BR_{\text{eff}} = N/(1+(m-1)\rho)$. Forty-seven bonds of one issuer are one bet with forty-seven CUSIPs.
- **Costs decide.** Break-even turnover is $\alpha_{\text{gross}}/(2\bar c)$. Barclays' realistic IG book gave up a third of its edge to costs, and the momentum family gives up more.
- **At the manager's favorite size the client keeps a third.** Capacity scales with $\mathcal{L}g^2/T^3$, and net alpha is zero at $\tfrac94 A^{*}$. Ask which size the capacity slide is quoting.
- **A 0.9 beta is not defense.** It is a smaller long. A default screen's recall is half a number until you know its flag rate.
- **Much of the published factor zoo did not survive cleaning.** Pin every field to its knowledge time, ban ex-post filters, and label every number gross or net, simulated or live.
- **The empty cells are distressed, LMT-aware signals, loans and private credit, securitized, and bond choice within the issuer.** They are where an RSSG brain is scarce.
### The Spec You Hand the Robot
> Build `capacity_breadth_engine.py` (numpy only, seed 404, units \$mm and annual decimals, turnover one-way). (1) `effective_breadth(n_bonds, n_issuers, rho)` returns $N/(1+(m-1)\rho)$; raise on `n_bonds < n_issuers` or `rho` outside $[0,1]$; `fundamental_law_ir(ic, br_eff, tc)`. (2) `net_alpha(aum, alpha0, turnover, cost0, eta, liquidity)` returns $\alpha_0 - 2T[c_0 + \eta\sqrt{2TA/\mathcal{L}}]$, where `liquidity` is the annual volume of the *selected* names; `aum_star_closed_form` returns $\mathcal{L}g^2/(18T^3\eta^2)$, or 0 if $g \le 0$. (3) `dynkin_cap_weights(mv, aum, cap_frac=0.05, w_max=None)` returns $\min(1/n, w_{\max}, c\,MV_i/A)$ and the uninvested fraction, floored at zero. (4) `framework_score(name, row)` returns $BR_{\text{eff}}$, gross IR, net IR at the row's AUM (scaled by net over gross alpha, tracking error held fixed), $A^{*}$ and cash drag. Assert: $\rho=1 \Rightarrow BR_{\text{eff}}=M$; numeric argmax of $A\alpha(A)$ within 1% of $A^{*}$; $\alpha(A^{*}) = g/3$; $\alpha(\tfrac94A^{*}) = 0$; tiny AUM gives equal weights; weights depend only on $c/A$. Never report bond count as breadth. Never use index ADV as $\mathcal{L}$. Label every output illustrative unless its inputs are sourced.
### Exercises
1. **Effective breadth.** A universe has 2,400 bonds from 600 issuers with within-issuer residual correlation $\rho = 0.6$. Compute $BR_{\text{eff}}$. What IC gives an IR of 0.5 with $TC = 0.5$? *(Answer: $BR_{\text{eff}} = 2{,}400/2.8 \approx 857$; $IC \approx 0.034$.)*
2. **Kaz's Sharpe of 3.1.** Kaz's backtest earns 6.2% a year of gross alpha at 2% tracking error, with one-way turnover of 8 times a year and transaction costs "set to zero so they wouldn't bias the results." Find the average cost per dollar traded at which the IR falls to 0.5, and the cost at which it hits zero. Compare both with a realistic HY half-spread and state, in one sentence, what Kaz should tell Ines. *(Answer: about 32.5bp and 38.75bp.)*
  [...truncated]
### Deep-Dive Resource Graph

==== 05_ch05_credit_probability_distributions.md (18,163 words)
# Chapter 5: Probability Distributions in Distressed & High-Yield Credit
## Cold Open: The Fourteen-Sigma Tuesday
## 5.1 One Bond, Two Worlds: The Survive-or-Jump Mixture
### 5.1.1 Desk framing: two hands dealt from one deck
### 5.1.2 The mixture and its moments
### 5.1.3 Skew is minus one over root PD
### 5.1.4 The fourteen-sigma Tuesday, priced
### 5.1.5 The 13-week model, reborn as a hazard rate
### Deep-Dive Resource Graph
## 5.2 Price, Spread, Return: Three Distributions That Are Not the Same
### 5.2.1 Desk framing: three people, three ledgers
### 5.2.2 Price: a bounded interval with a cap and a floor
### 5.2.3 Spread: right-skewed, roughly lognormal
### 5.2.4 Return: left-skewed in the survival world, sign-flipping in distress
### Deep-Dive Resource Graph
## 5.3 Jumps in Continuous Time: Merton, Kou, and the Short End
### 5.3.1 Desk framing: the bond does not care how long it has left
### 5.3.2 Merton (1976): Gaussian diffusion plus compound Poisson jumps
### 5.3.3 Kou (2002): double-exponential jumps, and why memorylessness is a gift
### 5.3.4 What the jump model is for on a desk, and what it is not
### Deep-Dive Resource Graph
## 5.4 Lévy Processes: What Is Useful and What Is Decoration
## 5.5 Recovery as a Random Variable: Beta Models Conditioned on Collateral and Seniority
### 5.5.1 Desk framing: the waterfall was always a distribution
### 5.5.2 The Beta distribution and the method of moments
### 5.5.3 Beta regression and inflated masses: conditioning on what the RSSG reader knows
### 5.5.4 Downturn recovery: PD and LGD share a factor
### 5.5.5 Participation status: the covariate with the biggest coefficient
### 5.5.6 $\mathbb{P}$ recovery, $\mathbb{Q}$ recovery, and the 40% that is neither
### Deep-Dive Resource Graph
## 5.6 The Default Is Now a Negotiation: Distressed Exchanges, Re-Default, and Regime Mixtures
### 5.6.1 The Bernoulli becomes a categorical variable
### 5.6.2 Case Study: Serta Simmons and Hertz, the two ends of the recovery distribution
### Deep-Dive Resource Graph
## 5.7 Tails: Hill, Peaks-over-Threshold, and Why Single Bonds Have No Power Tail
### 5.7.1 Desk framing: which objects have tails worth estimating
### 5.7.2 Hill and peaks-over-threshold
### 5.7.3 The bounded-support trap
### 5.7.4 Diversification eats skew, correlation feeds it back
### Deep-Dive Resource Graph
## 5.8 Choosing the Shape: Five Objects, Five Distributions
## 5.9 The Credit Mixture Lab: A Reference Implementation
### 5.9.1 One last derivation: exact moments of the DTS survival leg
### Specification for AI Implementation
### Deep-Dive Resource Graph
## 5.10 Desk Debrief
On Monday Theo reissues the risk report. It is still one page. It now has two columns, *survival world* and *default world*, and a coin between them labeled $q = 4\%$ ($\mathbb{P}$, from the 13-week model, lender case). Kaz's Gaussian sits in the left column with a footnote explaining that it describes the bond on the days nothing happens. The bottom line reads: 99% expected shortfall $-92\%$; jump-to-default 52 points per 100 of par.
Mags reads the bottom line, says "Ninety-two. That's about what I'd have guessed by phone," and goes back to her screen, which is how Mags says *good*. Ines turns the heat map face up again. "Now it's a hand," she says. "Pot, odds, river. Hand history Friday." ROBO receives the spec and, for once, has no questions.
- **A high-yield return is two worlds and a coin.** $R_h = (1-D)X + DY$. The between-world term $q(1-q)J^2$ is most of the variance, and trailing price volatility measures only the world in which nothing happens.
- **Skew is minus one over root PD.** Excess kurtosis is about $1/q$. The safer the bond, the stranger its shape; investment-grade books look normal because they are big, not because their bonds are.
- **95% VaR is blind whenever $q < 5\%$.** Report expected shortfall and jump-to-default, $P_0 - \mathbb{E}[R]$ per unit of par, next to any VaR, or the risk report is a speedometer that only works below the speed limit.
- **Keep three ledgers.** Price lives on $[0, K_{\text{call}}]$, spread changes are right-skewed and DTS-scaled, and returns are left-skewed. Negative convexity skews a callable's survival leg left before anyone defaults.
- **Jumps earn their keep at the short end.** Kou's model gives a non-zero short spread, $\lambda^{\mathbb{Q}}L^{\mathbb{Q}}$, and PD–LGD correlation from a single parameter. Infinite-activity Lévy fits to single-name high-yield bonds are decoration.
- **Recovery is a U, not a bell, and 40% is a convention.** Fit a zero-one-inflated Beta regression on the covariates the RSSG seat knows cold. Participation status carries the biggest coefficient. Never pool trading-price and ultimate recoveries in one fit.
- **Default is a menu now.** Hard default, distressed exchange, and re-default are separate mixture components with separate recovery distributions, and $w_{\text{in}}$ is the probability that *you* get the call, not the share of lenders who do.
- **EVT belongs to unbounded objects.** Run Hill and GPD on spread changes, indices, ETFs, and books. On a single bond the sample maximum sits at the cap, and the "tail index" is the jump mass.
### The Spec You Hand the Robot
This is the version that fits in a prompt. Everything in it is defined in §5.9; the point of the compact form is that every noun has a unit, every probability has a measure, and every edge case has an instruction.
  [...truncated]
### Exercises
### Deep-Dive Resource Graph

==== 06_ch06_merton_and_intensity_models.md (16,183 words)
# Chapter 6: Stochastic Calculus, Intensity Models & Structural Frameworks
## Cold Open: Column N
## 6.1 Itô's Lemma: The Volatility Tax
### 6.1.1 Desk framing: every claim is a function of something random
### 6.1.2 The derivation
### 6.1.3 Annualize or die
### 6.1.4 Column N, renamed
## 6.2 Merton 1974: Equity Is a Call, Debt Is a Short Put
### 6.2.1 Desk framing: every waterfall is a payoff diagram
### 6.2.2 Replication and the pricing PDE
### 6.2.3 Closed forms
### 6.2.4 The spread, a worked example, and the short-end embarrassment
### Deep-Dive Resource Graph
## 6.3 $\mathbb{P}$ to $\mathbb{Q}$: The Credit Risk Premium
### 6.3.1 Desk framing: what happens versus what it costs to find out
### 6.3.2 The measure change
### 6.3.3 The credit spread puzzle, and why the premium has a jump in it
## 6.4 KMV and Distance to Default: The Inverse Problem
### 6.4.1 Desk framing: two equations, two unknowns, one deadline
### 6.4.2 The solver
### 6.4.3 The default point and the empirical mapping
### 6.4.4 Case Study: Silicon Valley Bank, March 2023, and why banks break Merton
## 6.5 Black–Cox: First Passage and Covenant Barriers
### 6.5.1 Desk framing: the covenant you spent ninety hours modeling
### 6.5.2 The first-passage probability
### 6.5.3 Covenants, cov-lite, and uptiers as barrier mechanics
### 6.5.4 Monte Carlo and the Brownian bridge
### Deep-Dive Resource Graph
## 6.6 Reduced Form I: Cox Processes, Jarrow–Turnbull, Duffie–Singleton, and Three Recoveries
### 6.6.1 Desk framing: default as a surprise with a rate
### 6.6.2 The Cox construction and the zero-recovery bond
### 6.6.3 Three recovery conventions, which are three numeraires
## 6.7 Reduced Form II: CIR Intensities in Closed Form
## 6.8 Hazard Bootstrapping from CDS and the Credit Triangle
### 6.8.1 Desk framing: the 13-week model, industrialized
### 6.8.2 The two legs
### 6.8.3 The bootstrap and the credit triangle
### Deep-Dive Resource Graph
## 6.9 Hybrids: Structural Signals Inside Intensity Models
### 6.9.1 The two-stage fit
### 6.9.2 Equity leads credit
### 6.9.3 Case Study: First Brands, 2025, a firm with no equity ticker
## 6.10 Case Study: Carvana 2022–23 and Hertz 2020–21, the Call Option That Would Not Expire
### 6.10.1 Carvana: a negotiated barrier move
### 6.10.2 Hertz: the hand that hit
### 6.10.3 How the desk would have flagged both
### Deep-Dive Resource Graph
## 6.11 The Engine: One Module for Structural and Intensity Models
### Specification for AI Implementation
## 6.12 Ways This Blows Up: The Consolidated List
## 6.13 Desk Debrief
- **Every credit model answers two questions: when is $\tau$, and what is $R$.** Structural models make $\tau$ a barrier crossing you read off a balance sheet; reduced-form models make it a surprise whose rate $\lambda_t$ you read off a curve. The desk runs both, in labeled measures.
- **Itô's tax is $\tfrac12\sigma^2$, and the convexity refund goes to whoever owns the option.** In a levered firm that is the equity; the bondholders sold it.
- **Equity is a call, debt is a riskless bond minus a put, and the fulcrum is the strike where the asset distribution has mass.** Merton gets the shape right and the short end wrong: zero spread at zero maturity. Jumps and noisy information fix it.
- **$\mathbb{Q}$ PDs exceed $\mathbb{P}$ PDs by a premium that grows with $\sqrt T$ and is proportionally largest for safe names.** The premium is carry, not alpha. IDO or it didn't happen.
- **Distance to default is a ranking variable first.** The probability scale comes from at least 400 defaults, preferably 1,000, through an empirical, monotone mapping. A naive DD that never fails beats a solver that fails silently.
- **A maintenance covenant is a Black–Cox barrier; cov-lite deleted it; an uptier moves it for someone else.** In 2026, default is a negotiation, so model it as a categorical event with a negotiable barrier, and bridge your Monte Carlo.
- **$s\approx\lambda(1-R)$, and $R$ is a quoting convention.** Bootstrap piecewise-constant hazards, reprice every quote, and flag negative buckets rather than hiding them.
- **The thirteen-week model was a hazard curve all along.** Its liquidity runway goes into the intensity as a covariate, next to DD momentum.
**The Spec You Hand the Robot.** *"Build `ch06_structural_intensity_engine` in numpy/scipy, seeded `default_rng(42)`. Inputs: per-issuer market cap series (weekly, \$mm), default point $F=\text{STD}+\tfrac12\text{LTD}$ plus material off-balance-sheet liabilities (\$mm), riskless rate (continuous), and CDS quotes (tenors in years, spreads in bp, RFV recovery, vectorized discount function). Outputs per issuer and date: $V_0$, $\sigma_V$ (annual), $DD^{\mathbb{P}}$ in standard deviations of $\ln V$ at one year, $\text{PD}^{\mathbb{P}}$ from an empirical DD map (not $N(\cdot)$), $\text{PD}^{\mathbb{Q}}$ and the piecewise-constant $\lambda^{\mathbb{Q}}$ curve from CDS, the ratio $\lambda^{\mathbb{Q}}/\lambda^{\mathbb{P}}$, a Black–Cox PD for any supplied covenant barrier, and flags `dd_method`, `negative_hazard_mask`, `measure`, `recovery_convention`, `sigma_frequency`, `as_of`. Raise on non-positive inputs and on $\sigma_E$ outside 5%–300%. Never floor a hazard curve in place. Pass checks A–L of §6.11 before any output is written."*
### Exercises
1. **The vol trade inside a bond.** For the §6.2.4 firm ($V_0=100$, $F=80$, $r=4\%$, $T=1$), compute the Merton spread at $\sigma_V=15\%$ and $35\%$. Show analytically that $\partial B_0/\partial\sigma_V=-\text{vega}<0$, and explain in one sentence to Theo why a bondholder is short volatility, and why a sponsor considering a risky acquisition knows it.
  [...truncated]
### Deep-Dive Resource Graph

==== 07_ch07_ml_on_small_sample_credit_data.md (17,169 words)
# Chapter 7: Machine Learning on Small-Sample, Non-Stationary Credit Data
## 7.0 Cold Open: Forty-Seven Hats
## 7.1 Why Credit Is the Worst Machine-Learning Dataset in Liquid Finance
## 7.2 Trend Watch: The Bond-Factor Replication Crisis, 2019–2026
## 7.3 Stationarity With Memory: Fractional Differentiation of Log Spreads
## 7.4 Labels That Respect Credit: The Triple Barrier in DTS Space
## 7.5 Meta-Labeling: The RSSG Analyst as the Primary Model
## 7.6 Sample Weights: Uniqueness and the Forty-Seven-Hat Problem
## 7.7 Cross-Validation That Cannot Peek: Purged, Embargoed, Issuer-Grouped
## 7.8 Multiple Testing and the Deflated Sharpe Ratio
## 7.9 The Two Biases That Built the Bond-Factor Zoo
## 7.10 Trend Watch: The ML-for-Bonds Frontier and the Data Stack
## 7.11 Case Studies: Three Autopsies of Credit-ML Failure
### Case Study A: The One-Month Lead (Bai–Bali–Wen, 2019–2023)
### Case Study B: The Honest Corrigendum (Bianchi–Büchner–Tamoni, 2021)
### Case Study C: How a Bid–Ask Bounce Became a Factor (Short-Term Reversal, 2026)
## 7.12 The Credit ML Lab: A Reference Implementation
### Specification for AI Implementation
## 7.13 Desk Debrief
Two weeks after the cold open, Kaz reran the gradient-boosted model through the lab. The screen was much less exciting, which on this desk is how you know a number has been near the truth.
The row count was unchanged: 212,000 bond-months. Above it, in a font Kaz had made deliberately large, sat the hat count, $N_{\text{eff}} \approx 24{,}000$. Below it: shuffled K-fold AUC 0.61, purged and parent-grouped AUC 0.52; 3,000 trials; an out-of-sample Sharpe ratio of 0.30 per month across the purged folds; deflated Sharpe ratio 0.84; PBO 0.41 *(all illustrative)*. The top decile still held nine issuers. It no longer had a reason to.
"It isn't a strategy," Kaz said. "It isn't nothing, either. It's mostly carry and one company."
"Strip the carry," Theo said, "and then show me the one company." IDO or it didn't happen.
Theo had run something smaller. His primary model was the credit-agreement read turned into flags: drop-down capacity through unrestricted subsidiaries, non-pro-rata uptier risk, and a liquidity runway from the 13-week model shorter than two quarters. That came to about forty flags a year across the high-yield universe. The secondary model, trained on purged, parent-grouped folds, learned only *when those flags were right* and sized them. He had tried four sizing models, and he wrote the number four at the top of the report as if it were a defined term. Out of sample, the result was a Sharpe ratio of 0.20 per month over 96 months, with skew −1.5 and kurtosis 8. Against the four-trial benchmark ($SR^\ast \approx 0.02$), the deflated Sharpe ratio was 0.93, and the minimum track record length was about 115 months, so he needs roughly a year and a half more of live trading before the number means what he wants it to mean *(illustrative)*.
"Now," Ines said, "you're showing me a hand *and* the number of hands you folded. Sit down."
Mags looked at the four. "Back in my day we had one sizing model. It was called the PM's mood, and it had an excellent track record, because the PM was the one who kept it."
At the bottom of the monitor Kaz had taped the epigraph that Dickerson, Robotti, and Rossetti chose for their 2026 audit, Ronald Coase's line: "if you torture the data enough, nature will always confess." By lunch a sticky note had appeared beneath it in the unmistakable register of the Ad Hoc Group: *The data, represented by counsel, will not confess to anything absent a cooperation agreement.* None was signed, so the counter waits for Part IV.
Theo put the USB stick back in his pocket. It had been a 13-week cash flow model when he arrived. It was now a vertical barrier, a primary model, and a reason to distrust anything labeled "adjusted," which Mags said was the first sign he might last.
  [...truncated]
### The Spec You Hand the Robot
### Exercises
### Deep-Dive Resource Graph

==== 08_ch08_isolating_ido_and_empirical_duration.md (18,159 words)
# Chapter 8: Stripping Beta to Isolate Pure IDO
## 8.0 Cold Open: Thirty-Seven Cents
## 8.1 The Subtraction: Return Decomposition With the Right Signs
### Deriving the decomposition
### The thirty-seven cents, itemized
## 8.2 Empirical vs. Analytical Duration: One Formula, Three Regimes
### The two-factor derivation
### The canonical numbers, rebuilt
### Three regimes
### Deep-Dive Resource Graph
## 8.3 The Discontinuity: Why a CCC Bond Is an Equity Option That Wears a Tie to Work
### Two routes to zero duration
### The segmentation hypothesis
### Price level: the discount-bond asymmetry
### Case Study: One Bond, Four Hedge Ratios (Alltel's 7.875% 30-Year, 2006–2009)
## 8.4 DTS: The Unit of Credit Beta
### The derivation
### DTS-neutral pairs, and why they carry nothing
### Why DTS beats an estimated beta
## 8.5 Betas When Nothing Trades: Dimson, Scholes–Williams, and the Lag That Isn't Noise
### The smoothing model and the bias it creates
### The trap: lags that carry information
### Deep-Dive Resource Graph
## 8.6 The Hedge Matrix: CDX, UST Futures, HYG/JNK, Equity Puts
### The instruments, in DV01 terms
### The derivation: minimum variance, ridge, and hedging less
### Theo's hedge, four ways
### Deep-Dive Resource Graph
## 8.7 Case Studies: Three Times the Hedge Hedged the Wrong Thing
### Case Study A: 2022, the Year "Negative Duration" Was Positive
### Case Study B: March 2023, SVB, and the Hedge That Hedged Both Ways
### Case Study C: April 2025, Three Regimes in Seven Sessions
## 8.8 What's Left Is IDO (and How to Prove It)
### The definition, in four subtractions
### Theo's thirty-seven cents, answered
### The IDO ledger: proving it
## 8.9 The IDO Engine: A Reference Implementation
### Specification for AI Implementation
## 8.10 Desk Debrief
- **IDO or it didn't happen, in two subtractions.** First accounting (carry, KRD-matched Treasuries, convexity), then attribution (DTS-scaled factors, then the common residual factor). The P&L-explain residual is a bookkeeping error, not alpha.
- **Analytical duration answers a question nobody asked.** $H = 1 + s\,\rho_{y,s}\,\sigma_s/\sigma_y$. The sign of $\rho$ decides everything, and it has changed sign twice since 2021.
- **There are two roads to zero duration.** The correlation road is a regime. The recovery road, $H^{\text{rec}} = c/(c + \lambda R)$, is structural. CCC books travel both.
- **The IG/HY line is a quoting convention you can measure.** Baa at 700 bp hedges at 0.71; HY at 700 bp hedges at zero. Re-bucket the hedge ratio on the day of a downgrade across the line.
- **DTS is the unit of credit beta.** $\beta_i = \text{DTS}_i/\text{DTS}_M$. DTS-neutral pairs carry nothing, so what they earn is IDO.
- **Stale marks shrink betas to $\theta_0\beta$ and volatility to $\sqrt{\sum\theta_k^2}$.** Dimson-sum rates and credit factors. Treat lagged equity coefficients as a signal to test, not a correction to apply.
- **The hedge you want and the hedge you can trade are different matrices.** Cap the condition number, shrink, hedge less than naive, and if your mandate is IDO, hedge each factor with its own instrument instead of through a correlation.
- **The empirical hedge ratio is a bet on why rates move.** When this week's $\rho$ disagrees with the trailing window, cut confidence in the hedge. Do not re-estimate harder.
### The Spec You Hand the Robot
```text
TASK: Build ido_engine.py (numpy/scipy only, float64, seed np.random.default_rng(8)).
INPUTS: bond_returns (T,N) daily total returns, decimal; oas (T,N) decimal > 0; dur_mod, dur_spr (T,N) years;
        factors (T,K); hedge_returns (T,m) per unit notional, "long risk" sign convention; close_time per column.
        Missing marks are NaN. Never forward-fill prices into returns.
OBJECTIVE (required, no default): one of min_total_variance | zero_rates_keep_spread | zero_rates_zero_spread.
COMPUTE, in order:
 1. decompose_returns: carry, -D_mod*dy, -D_spr*ds, 0.5*C*(dy+ds)^2, residual; assert it foots to 1e-10.
 2. empirical_duration: pooled OLS of R on [-D*dy, -D*s*dy] by rating bucket; H(s) = beta + gamma*s,
    clipped at -0.5; re-estimate monthly; re-bucket H on the day of a rating change across Baa3/Ba1.
 3. Dimson betas (lags <= 3 daily) on rate and credit-index factors; equity lags reported, never auto-applied.
 4. DTS-scale excess returns by previous-close DTS before any covariance or PCA.
 5. hedge_matrix: variance-scaled ridge, eta chosen so cond(C + eta I) <= 50; Dimson-summed covariances if
    close times differ by > 30 min; bounded QP when limits are given; output h = notional to SHORT per unit.
 6. Units: TY contracts = H * DV01_target / (DV01_CTD / CF); CDX notional = h * target; ETF shares = h * notional / price.
 7. IDO = DTS_{t-1} * (scaled residual minus first principal component). Ledger: residual vol, monthly Spearman IC
  [...truncated]
### Exercises
### Deep-Dive Resource Graph

==== 09_ch09_factor_investing_in_credit.md (17,363 words)
# Chapter 9: Factor Investing in Corporate Credit
## 9.0 Cold Open: Sharpe 1.9, Beta 0.6
## 9.1 What a Factor Is in Credit, and Why It Is Not What It Is in Equities
## 9.2 DTS: The Beta You Did Not Know You Had
### 9.2.1 From proportional spread changes to beta
### 9.2.2 Why a dollar-neutral spread sort is long beta
### 9.2.3 DTS-neutral construction
## 9.3 Value: ESP, SPiDER, and the Fair-Spread Family
### 9.3.1 Excess spread to peers (ESP)
### 9.3.2 SPiDER and Man's spread per turn of leverage
### 9.3.3 The structural fair spread, and the measure trap
### 9.3.4 The residual is cheapness or it is information
## 9.4 Momentum: Bonds, Equities, and the Decay Clock
### 9.4.1 The decay clock
### 9.4.2 Break-even turnover
## 9.5 Carry and Low-Risk: One Risk Sort in Two Costumes
### 9.5.1 Carry is the price of DTS
### 9.5.2 Low-risk and defensive
### 9.5.3 Two live reminders that low-risk is a duration bet
## 9.6 Quality, Size, and the Informed Investor
### 9.6.1 Quality is a high-yield factor
### 9.6.2 Size, the factor that isn't
### 9.6.3 The informed investor
## 9.7 Combining Factors: Correlations, Weights, and Effective Breadth
### 9.7.1 The combination formula
### 9.7.2 Effective breadth: forty-seven hats again
### Case Study: One Telecom, Four Factors (Man Numeric, 2016–2017)
## 9.8 Portfolio Construction Under Costs
### 9.8.1 The optimizer
### 9.8.2 What a trade costs
### 9.8.3 Buffers: doing nothing on purpose
## 9.9 The Replication Debate, Read as a Desk
## 9.10 Crowding, Capacity, and the Drawdowns That Matter
### Case Study: March 2020 Through the Factor Lens
## 9.11 The Credit Factor Lab: A Reference Implementation
### Specification for AI Implementation
## 9.12 Desk Debrief
A week after the cold open, Kaz put the value strategy back on the screen, rebuilt with DTS-neutral legs inside rating × sector cells, start-of-month DTS, default months kept, and a skip-month rule between the price used for the signal and the price used for the return. The Sharpe ratio was 0.9 gross and 0.7 net. The beta was 0.02 *(illustrative)*.
"It's less," Kaz said.
"It's *yours*," Ines said. "Last week sixty percent of it belonged to the index. Now replay the hand: what did the cheap decile cost to trade, and how much of it was cheap because somebody at the table knew something?"
Theo had the answer to the second half. He had added two columns to the ESP regression: the 13-week model's liquidity runway and a crude document-risk flag for drop-down capacity. In B and CCC they pulled a fifth of the names out of the cheap decile. Most of the names they removed had widened further over the next six months. IDO or it didn't happen, and this time some of it had.
Mags read the new tear sheet twice, which for her is applause. "Back in my day, the value factor was a guy who bought what everybody else was selling and had a strong stomach. Yours has a cost model and a lawyer." A pause. "Fine. Yours is better than the guy."
- **Beta in credit is $\text{DTS}_i/\text{DTS}_m$.** A dollar-neutral spread sort is a long-beta portfolio. Report every factor both dollar-neutral and DTS-neutral; the gap is how much of it was beta.
- **Carry is the price of DTS.** Per unit of DTS, carry is $1/D^{\text{spr}}$, so a DTS-neutral carry factor is a short-duration factor and belongs with low-risk.
- **Value is a residual within a peer cell, on clean prices.** The residual is either cheapness or information you lack. Document-risk features (Chapter 13) separate the two, and that is where the RSSG reader's edge lives.
- **Momentum is real gross and perishable.** A top-decile half-life of about 1.2 months and the break-even rule $c^\ast = \mathbb{E}[r^{\text{gross}}]/\text{TO}$ decide whether you can keep it. At 73% monthly turnover you need round-trip costs below 72bp.
- **Size is mostly liquidity and price noise; the informed investor is a filter.** Neither is a stand-alone engine.
- **Combine with $\rho^{-1}\text{IR}$, shrunk toward equal weights.** Equal-risk weights can lose to the best single factor, and trade netting exists only in the traded portfolio.
- **Signal and return never share a price, defaults stay in, filters are written before the data are seen, and the library replicates Open Bond Asset Pricing in CI.**
- **Budget for a live net IR near 0.5, not 2.** Ten years of live multi-factor credit returns sit near the benchmark; the backtests do not.
  [...truncated]
### The Spec You Hand the Robot
### Exercises
### Deep-Dive Resource Graph

==== 10_ch10_trend_and_time_series_momentum.md (17,554 words)
# Chapter 10: Trend-Following & Time-Series Momentum in Credit
## 10.0 Cold Open: The Model Has No Amygdala
## 10.1 What a Trend Is, in Credit
### 10.1.1 The instruments, and why index CDS is the futures-like leg
### 10.1.2 Trend on returns, not on spread levels: the carry hurdle
## 10.2 The TSMOM Engine, Adapted
### 10.2.1 The Moskowitz–Ooi–Pedersen template
### 10.2.2 Smoother signals and ensembles
### 10.2.3 Building the return series correctly
## 10.3 Volatility Scaling Is DTS Scaling
### 10.3.1 The derivation
### 10.3.2 The stop-loss that was already a trend rule
## 10.4 Trend Plus Carry: Two Coefficients, No Tribes
### 10.4.1 The derivation
### 10.4.2 Why you cannot estimate your way out of the argument
### 10.4.3 What the literature says about the blend
## 10.5 Cross-Asset Trend: The Equity Market Moves First
### 10.5.1 The evidence on who leads
### 10.5.2 Equity Momentum in Credit, from the shelf
### 10.5.3 The lead–lag regression, and the stale-mark artifact
### 10.5.4 Total versus residual equity momentum, and the turning-point risk
## 10.6 Crisis Alpha and the Shape of the Payoff
### 10.6.1 Trend is a straddle, and the smile is the receipt for momentum
### 10.6.2 Whipsaw arithmetic: why trend cannot trade a V
### 10.6.3 Is credit trend just beta?
## 10.7 Case Studies: 2008, 2020, 2022, and the April 2025 Coda
### Case Study A: 2007–2009, the trend that paid and the rebound that charged
### Case Study B: February–June 2020, the V that trend could not trade
### Case Study C: 2022, trend's best year was mostly duration
### Coda: April 2025, "Liberation Day" (FRED-verified spreads)
## 10.8 Turnover, Costs, and Capacity
### 10.8.1 How often does a sign flip?
### 10.8.2 Break-even arithmetic
## 10.9 Trend in the LMT Era: Jumps, Not Diffusions
### 10.9.1 The jump-diffusion correction to vol scaling
## 10.10 The Credit Trend Lab: A Reference Implementation
### Specification for AI Implementation
## 10.11 Desk Debrief
- **Trend is absolute; momentum is relative.** Trade credit trend in indices (CDX, iTraxx, listed credit futures). Signal it from the markets that price information first: equity, then CDS, then cash.
- **Trend on returns, not spread levels.** The carry hurdle $\Delta s^*_h = \bar s\,h\,\Delta t / D^{\text{spr}}$ means 12-month HY trend goes short only after roughly 110 bp of widening *(illustrative)*. Write the version you mean.
- **Vol targeting in credit is a constant-DTS budget.** It sells after widening before any signal fires. Forecast volatility as $\max(\text{EWMA}, \beta^{\text{DTS}}\text{DTS}, \text{floor})$ and cap leverage.
- **Do not join a tribe.** $\mathbb{E}_t[r^{ex}_{t+1}] = s_t\Delta t + D\kappa(s_t-\bar s) - D\phi\Delta s_t$. Estimate $\kappa$ and $\phi$ on an expanding window and blend; carry and trend disagree exactly after large moves.
- **Equity leads credit, and stale marks fake it.** A bond that prints with probability $p$ shows a fake equity lead of about $p(1-p)\beta^{\text{ce}}$. Test on trades, or on the index.
- **Convexity is the receipt for momentum.** The smile coefficient is positive if and only if returns trend. A V captures $(T-4L)/T$ of the round trip. Trend hedges slow sell-offs, not gaps.
- **IDO or it didn't happen.** Credit TSMOM's alpha against passive beta had a *t*-statistic of 0.49 in AQR's test. Trend is beta that changed its mind. Strip it before you call it alpha.
- **Single names jump.** Add $\lambda^{\text{J}}\,\mathbb{E}[J^2]$ to the variance, map $\lambda^{\text{J}}$ from the Priming Risk Score, and switch engines when the capital structure stops moving together.
### The Spec You Hand the Robot
```text
TASK: credit_tsmom engine (index trend sleeve). Positive weight = long risk (sold protection).
INPUTS: daily spreads (decimal) or prices (points) per index and series_id; optional equity TR series;
        spread duration / RPV01 per day; coupon (IG 100 bp, HY 500 bp); FRED OAS CSV for research.
RETURNS: r_t = s_{t-1} * days/360 - D * (s_t - s_{t-1}) within one series_id; price-quoted:
         dP/100 + c * days/360. Never difference across series. Never use OAS level changes as returns.
SIGNALS (known at close t, applied to r_{t+1}; also report a 2-day lag run):
  sign TSMOM at 1, 3, 6, 12 months (21/63/126/252 days), ensemble mean; 20/120 EWMA crossover (tanh z);
  equity-to-credit: residualized equity momentum, horizons 1/3/6 months, each divided by sqrt(h).
SIZING: w = 0.10 / max(EWMA_vol(com=60), beta_DTS * DTS_t, 0.005) * sig; cap |w| <= 10;
        beta_DTS = zero-intercept fit of non-overlapping 63-day spread-change vol on spread level.
BLEND: f_t = s_t*dt - D*(a_t + b_t*s_t) - D*phi_t*ds_t, with (a, b, phi) from OLS on data up to t
       (min 120 months); w = f / (D * beta_DTS * s_t)^2 / dt, then scale to the risk budget.
SINGLE NAMES: variance += lambda_J * E[J^2], lambda_J = l0 + l1 * PRS; switch to the event engine when
  [...truncated]
### Exercises
### Deep-Dive Resource Graph

==== 11_ch11_defensive_systematic_high_yield.md (15,574 words)
# Chapter 11: Defensive Systematic High Yield
## 11.0 Cold Open: The Bow Tie
## 11.1 The Asymmetry: Why High Yield Needs a Defense at All
### 11.1.1 The mixture return and where the skew comes from
### 11.1.2 The credit triangle, with the measure stated
## 11.2 The Average Manager's Dimmer Switch: Capture Ratios and the Beta-Tilt Diagnosis
### 11.2.1 The capture-ratio identity
### 11.2.2 Convexity: the asymmetric-beta regression
### 11.2.3 Case Study 1: The 2022–2023 Round Trip
### Specification for AI Implementation
## 11.3 Default Avoidance I: The Structural PD
### 11.3.1 Equity as a call, solved backward
### 11.3.2 The normal-distribution trap
### Specification for AI Implementation
## 11.4 Default Avoidance II: Hazard Models, Labels, and Gradient Boosting
### 11.4.1 Altman's Z, and the units trap
### 11.4.2 From static logit to the dynamic hazard
### 11.4.3 The label is the model
### 11.4.4 What machine learning adds, measured honestly
### Specification for AI Implementation
## 11.5 Validation: Power Curves and What "77% Within 24 Months" Means
### 11.5.1 CAP, ROC, and an identity worth knowing
### 11.5.2 From a hit rate to a return
### Specification for AI Implementation
## 11.6 The CCC Problem
### 11.6.1 Why tier exclusion is the wrong tool
### 11.6.2 Case Study: The 2026 CCC Decompression
## 11.7 Quality and Low-Risk Tilts
### 11.7.1 Why low risk wins, in one line of DTS
### 11.7.2 The long-only contradiction, and three ways out
### Specification for AI Implementation
## 11.8 Defense Without Sacrificing Offense: Regime-Aware Exposure
### 11.8.1 Case Study: The April 2025 Tariff Shock, a Ten-Week V
## 11.9 Capacity of Systematic HY
### Specification for AI Implementation
## 11.10 Desk Debrief
Theo unplugged the USB stick at 7:40 p.m. The 13-week model had become a covariate, capped at 13, and was now one of three features in a hazard function that covered 2,000 issuers. It seemed to be taking the demotion well.
- **High yield is a short put that pays a coupon.** The default jump carries skew of $-(1-2p)/\sqrt{p(1-p)}$: about $-6.9$ at a 2% PD, $-1.5$ at 20%. BB defense is tail avoidance; CCC defense is pricing.
- **$U = D = \beta$ is a dimmer switch.** A pure beta tilt gives equal capture ratios, and only alpha opens the gap. The average manager's 92.24%/89.56% reads as roughly a 0.91 beta with a small net alpha. Real defense is $\beta^{-} < \beta^{+}$, tested on pairs of regimes.
- **DD is a ranking, not a probability.** Map it to PD empirically, never with $N(-\text{DD})$, and send no-equity issuers to a separate, flagged model.
- **The label is the model.** With distressed exchanges at 65% of 2025 defaults, a PD trained on hard defaults is calibrated to a world that no longer exists. Label at the issuer, date it at announcement, and include LMEs that impair the holder.
- **A hit rate without an exclusion rate is half a sentence.** Default avoidance pays when $(\pi_X - \pi_K)L > s_X - s_K$; the same 77% can be +44bp or −9bp depending on how much of the table you folded.
- **CCC is a crowd, not a person.** Size the bucket by expected loss, choose inside it by PD, diversify it with breadth (high-PD risk is mostly idiosyncratic), and buy from forced sellers whose problem is a rating, not a balance sheet.
- **IDO or it didn't happen.** Every defensive signal is tested DTS-neutral first; a market-value-neutral low-risk tilt is beta wearing a factor's name tag.
- **Capacity is a square.** Halve turnover and capacity quadruples: exclusion and low risk scale into tens of billions, CCC reversal and fallen angels into low single-digit billions.
### The Spec You Hand the Robot
"Build an issuer-month panel from the security master, one row per ultimate parent per month. Label equals 1 if any of {payment default beyond grace, bankruptcy filing, distressed exchange, LME that impairs the holder} is *announced* in months $[t, t+12)$; drop rows whose window runs past the data. Features: empirically mapped distance-to-default (with `no_equity_flag`), CHS market and accounting covariates lagged to filing date, liquidity runway in weeks capped at 13, months since last LME, and the Chapter 13 PRS. Fit a calibrated dynamic logit with issuer-clustered errors and a gradient-boosted model, both with issuer-disjoint, 12-month-embargoed cross-validation; report AUC, AR (assert $\text{AR} = 2\,\text{AUC} - 1$ on untied scores), hit rate at 10/20/30% exclusion, and realized-versus-predicted default rates by PD decile. Portfolio: exclude the worst-PD quintile, tilt toward $(s_i - \hat\lambda_i L_i)/\text{DTS}_i$, hold $w^\top\text{DTS}$ within 1% of the benchmark times a regime multiplier in $[0.9, 1.2]$ driven by the DTS-weighted spread-to-model-spread residual, issuer cap 3%, long-only, no leverage. Report $U$, $D$, $\beta^{+}$, $\beta^{-}$ on benchmark regimes. Halt and alert if portfolio DTS deviates from target by more than 2%, if any weight is negative, if the target DTS is unreachable without leverage, or if a z-signal purchase has a PRS above threshold."
  [...truncated]
### Exercises
### Deep-Dive Resource Graph

==== 12_ch12_multi_asset_credit_allocation.md (15,573 words)
# Chapter 12: Multi-Asset Credit Allocation
## 12.0 Cold Open: Seven Piles, One Bet
## 12.1 The MAC Universe as a Capital-Structure Map
## 12.2 The Return Identity: Four Terms and Two Measures
## 12.3 Spread per Unit of What? Cross-Sector Valuation
### Deep-Dive Resource Graph (§12.1–12.3)
## 12.4 Regimes: A Two-State Hidden Markov Model for Credit
## 12.5 Covariance You Can Trust: DTS Structure, EWMA, Shrinkage and Desmoothing
## 12.6 Optimization: Mean-Variance, Risk Budgets, and Why the Frontier Is Flat
## 12.7 Liquidity Tiers as the Binding Constraint
### Deep-Dive Resource Graph (§12.4–12.7)
## 12.8 Tactical Overlays and the Turnover Budget
## 12.9 Case Studies: Three Stress Tests of the Framework
### Case Study A: April 2025, a Regime Transition in 25 Trading Days
### Case Study B: First Brands, Tricolor and the First BDC Redemption Cycle
### Case Study C: The 2026 CCC/BB Split
## 12.10 The MAC Engine: A Reference Implementation
### Specification for AI Implementation
## 12.11 Desk Debrief
Friday afternoon. Kaz's direct-lending weight had fallen from the 35% bound to whatever the 15% cap and the days budget allowed. The PM's comment on the new spreadsheet said "Why?" Theo answered it with three numbers, and none of them was a yield.
- **The forward return is an identity with two measures in it.** Yield is a market ($\mathbb{Q}$-flavored) quantity; the loss term must be physical. A CDS-implied default probability in the loss term forecasts a zero risk premium by construction.
- **Expected credit loss is the restructuring banker's variable.** Set recovery by the seat in the waterfall (about 33% for direct loans, 52% for syndicated loans, 39% for HY bonds per FEDS 2024), not by a rating table. A 33% recovery has a 40% larger loss given default than a 52% one.
- **Rank sectors by spread per unit of something.** Break-even default $s/(1-R)$, carry per unit of DTS risk $(1 - \text{EL}/s)/(D^{\text{spr}}\sigma(\Delta s/s))$, and spread net of LCS. A wider spread is a bigger bet, not a better one.
- **Composition moves the mean, not the tail.** The HY index went from 37% BB to 51–54% BB. Z-scores against raw history mostly measure that change. Use fixed-mix spreads and bucket-level models.
- **Desmooth before you optimize.** $\sigma_{\text{true}} = \sigma_{\text{reported}}/\sqrt{\sum_j\theta_j^2}$; contemporaneous beta is understated by $\theta_0$. At AR(1) $\phi = 0.8$, volatility is understated threefold and beta fivefold.
- **The frontier is flat by the mediant inequality.** Long-only credit Sharpe ratios are weighted averages of sectors' systematic Sharpes. When the optimizer's choice sits inside the error bars, the constraints, not the objective, decide the allocation.
- **Liquidity tiers bind first.** The 15% illiquid cap, the liquid-sleeve minimum and the days-to-liquidate budget are known exactly; expected returns are not. Report shadow prices, and remember that a 5% quarterly gate is a queue position.
- **Regimes size the tilt; valuation directs it.** Trade on filtered probabilities with a delay, never smoothed ones. Expect the filter to be a month late into stress and a month late out of it, as in April 2025.
### The Spec You Hand the Robot
```text
ROBO: build mac_engine, a multi-asset credit allocator. Implement exactly this; where anything is
unspecified, stop and ask. Do not guess.
INPUTS (decimals per year; durations in years; point-in-time)
  sectors[n]: yld (yield-to-worst EX-DISTRESSED: drop constituents priced < 50, model them separately),
              pd (PHYSICAL annual default rate; never CDS-implied), rec (by seat in the waterfall),
              dmod, dspr (OAS duration for callables), spread, dspread_h (expected change over horizon),
              tier in {HL, ML, LL, IL} (Rule 22e-4 style), days (to liquidate), lcs_bp (round trip),
              w_min, w_max, smoothed (bool: appraisal-marked series?)
  R[T,n] monthly excess returns at bucket level (BB, B, CCC split); U[T,n] relative spread changes
  h horizon (years), cash rate, gamma (risk aversion)
  [...truncated]
### Exercises
### Deep-Dive Resource Graph

==== 13_ch13_codifying_lmt_game_theory.md (15,188 words)
# Chapter 13: Codifying Liability Management Transactions (LMTs)
## 13.1 The LMT Zoo, Seen From the Desk
## 13.2 Legal Prose to State Space
### 13.2.1 The feature vector
## 13.3 The Uptier as a Recovery Transfer
### 13.3.1 Case Study: Serta Simmons (2016–2026), in the Formula
## 13.4 Game Theory I: Threshold Games and the Sponsor's Auction
## 13.5 Game Theory II: Cooperation Agreements as Commitment Devices
## 13.6 Drop-Downs: Collateral Leakage Arithmetic
## 13.7 Double-Dips and Pari-Plus: A Waterfall Engine That Conserves Value
### 13.7.1 Case Study: Trinseo (2023–2026), the Double-Dip Meets Chapter 11
## 13.8 The Priming Risk Score
### Specification for AI Implementation
## 13.9 Autopsies: The Court Is a Random Variable
## 13.10 Desk Debrief
- **An LMT is the difference of two waterfalls.** In low states it is zero-sum among creditors; the liquidity story lives in high states. Compute $\Delta_j(V)$ before you read the press release.
- **Know your payoff shape.** Excluded from an uptier: short a soft digital put struck at $K_1$. Victim of a drop-down: short a forward capped at $C^{\text{unsub}}/F$. Diluted by a double-dip: someone is counted twice in your denominator.
- **The sponsor solves a knapsack** and leaves out the constrained, the fragmented and the litigious. Model your invitation probability, not your participation decision.
- **A co-op above $1 - \theta$ turns an auction into a bargain.** Deal-away capacity costs the co-op $\eta$ per dollar; carve-out premiums are Shapley values. (Cooperation agreements signed in this book so far: 2. Antitrust complaints about them: 2, and counting.)
- **One word can be the whole loss.** The court is a random variable with a clause, a forum, a doctrine and a vintage.
- **PRS is $\mathbb{P}$; the price is $\mathbb{Q}$.** Never calibrate the score to prices. The prior keeps $\hat\beta$ finite, and Theo's runway is the covariate that separates.
- **The LMT is not the terminal state.** Only 22% of coercive-LME firms avoided both re-default and bankruptcy within two years. Price the next event.
### The Spec You Hand the Robot
Build `lmt_engine.py` (numpy/scipy; `rng = np.random.default_rng(13)`; runs top to bottom; values in \$mm, recoveries in fraction of par, runway in months, PRS at a 12-month horizon). (1) `waterfall_clearing(entities, claims)`: priority ranks, pro rata within rank, intercompany receipts and subsidiary equity routed to parents, `reduce_by` for co-obligor claims on one debt; stop at $\lVert \Delta p \rVert_\infty < 10^{-10}$, raise after 10,000 iterations; assert conservation to $10^{-8}$, no payment above face, monotonicity in $V$, the double-dip closed form, pari-plus collapse at $V_f = 0$. (2) `uptier`, `priming_loss`: guard $N = 0$ and $p = 1$; assert conservation, zero loss for $V \ge F + N$, full loss for $V \le K_1$; expected loss by quadrature checked against Monte Carlo and the lognormal partial expectation. (3) `min_cost_coalition`: brute force to 12 holders, greedy beyond, `None` when a co-op exceeds $1 - \theta$; `shapley` by enumeration. (4) `fit_map`: Newton with step-halving, Gaussian slope prior, Beta base-rate prior; assert the intercept first-order condition, both $\tau$ limits, the bootstrap band, signs, and a holdout Brier score below the base rate. (5) `expected_priming_loss` $=$ PRS $\times$ P(NPR $\mid$ LMT) $\times$ P(excluded $\mid$ NPR) $\times$ $\mathbb{E}[\Delta R]$, inputs in $[0,1]$. Never fit PRS to prices.
### Exercises
1. **Unblend Serta.** Redo §13.3.1 with the \$1.95bn first lien and \$450mm second lien as separate classes. Parameterize the unknown lien split of the \$1.2bn exchanged, compute $K_1$ for the excluded first-lien lenders, and find the split at which the blended 44.8-point transfer at $V = \$1.075$bn is off by more than 10 points.
  [...truncated]
### Deep-Dive Resource Graph

==== 14_ch14_default_and_recovery_cycle_lmt_era.md (14,557 words)
# Chapter 14: The Default & Recovery Cycle in the LMT Era (TREND)
## 14.1 Two Default Rates, Two Recovery Rates
### Deep-Dive Resource Graph (§14.1)
## 14.2 Splitting the Default Intensity: Competing Risks
### 14.2.1 Cause-specific hazards and cumulative incidence
### 14.2.2 Estimating CIFs without fooling yourself
## 14.3 The Re-Default Clock: Survival After a Soft Default
### 14.3.1 The state space
### 14.3.2 A mixture-cure clock, calibrated to Moody's
### 14.3.3 Expected loss when the path has a soft default in it
## 14.4 Recovery Is a Mixture over Coalition Membership
### 14.4.1 Two humps, not one bell
### 14.4.2 The new first stage
### Deep-Dive Resource Graph (§14.3–14.4)
## 14.5 Cooperation Agreements: The Lender Cartel as a Repeated Game
### 14.5.1 The threshold game with a co-op
## 14.6 The Courts as a Regime Variable
### 14.6.1 Encoding a ruling as a jump
## 14.7 Regime Shifts in the Joint Law of $(\tau, R)$: A Markov-Switching Engine
### 14.7.1 The Hamilton filter on the default mix
### 14.7.2 $\mathbb{P}$ versus $\mathbb{Q}$: the definitional wedge
### Specification for AI Implementation
### Deep-Dive Resource Graph (§14.7)
## 14.8 Case Studies: Three Clocks
### 14.8.1 Case Study: Serta Simmons Bedding, 2020–2026 (the whole regime in one name)
### 14.8.2 Case Study: Mitel Networks, 2022–2025 (win the case, lose the credit)
### 14.8.3 Case Study: Del Monte Foods, 2024–2026 (the fast clock)
## 14.9 Trading the Regime
## 14.10 Desk Debrief
- **"The default rate" is two numbers.** Headline and ex-DE rates differed by a factor of almost three in June 2025 (5.8% vs. 2.1%). Carry $\lambda_H$ and $\lambda_D$ separately, and name the definition in the column.
- **Use cumulative incidence, not 1 − Kaplan–Meier.** Censoring the competing cause overstates the probability of the cause you care about, and the bias grows with horizon.
- **A distressed exchange is parole, not immunity.** About a quarter of soft events end in hard default, more than 70% of those within two years. The hazard among the susceptible *rises* at first, because the deal bought runway. Calibrate $k \gtrsim 1$, not $k < 1$.
- **Recovery is two humps.** Membership alone can generate a 24-point standard deviation. Stage 0 of the LGD model is $\mathbb{P}(\text{in majority})$, and it belongs to the holder, not the loan.
- **Co-ops move risk; they don't remove it.** Coverage above the blocking line crushes the uptier hazard and raises the drop-down and deal-away hazard. The co-op's own legality is a dated scenario.
- **Rulings are regime switches with timestamps.** Encode them as documented log-odds jumps by wording class. Serta and Mitel, decided the same day, are the proof that tokens beat economics.
- **Never compare a CDS hazard with an agency default rate** without removing $\lambda_D$ and replacing the 40% convention. Most "the market is underpricing default" notes are units errors.
**The Spec You Hand the Robot.** "Build `lme_cycle_engine.py` per §14.7. Inputs: an event table with the schema given, or `LMEParams` for simulation. Hazards are per year under $\mathbb{P}$, recoveries are fractions of par, and the DE recovery is the value held immediately after the exchange. Estimate cause-specific Nelson–Aalen and Aalen–Johansen CIFs on first events only, and assert $S + \sum_k F_k = 1$ to 1e-10. Fit the post-DE clock as a mixture-cure Weibull with right-censoring. Never fit an exponential or set the hazard to zero after the last observed event. Report EL by coalition side (`in`, `out`, `blend`) by quadrature, and check it against Monte Carlo within 0.005. Fit the two-state binomial Markov-switching model on DE *counts*, with ordered shares and a log-space filter, and accept time-varying $P$ as a $(T,2,2)$ array. Never delete DE rows to 'exclude' them: report the ex-DE rate as a second output. Seed every generator. Raise on a horizon beyond `T_max`. Print PASS/FAIL for every check in block 5."
## Exercises
### Deep-Dive Resource Graph

==== 15_ch15_event_driven_mna_and_coc.md (13,995 words)
# Chapter 15: Event-Driven M&A, Regulatory Spreads & Change-of-Control
## Cold Open: Friday the Thirteenth, Aisle Four
## 15.1 The Event-Driven Credit Map: Six Cash Flows That Fire on a Deal
### 15.1.1 Desk framing: the merger is the underlying, the regulator is the clock
### 15.1.2 The six contingent cash flows
### 15.1.3 The forced-flow view
### Deep-Dive Resource Graph
## 15.2 Anatomy and Pricing of the 101 Change-of-Control Put
### 15.2.1 Desk framing: a smoke detector with two licensed inspectors
### 15.2.2 Derivation: the put as a compound option
### Specification for AI Implementation
### Case Study: Electronic Arts 2025–26, the In-the-Money Put That Got Defeased
## 15.3 Portability: The Short Option You Did Not Know You Sold
### 15.3.1 Desk framing
### 15.3.2 Derivation: a short digital on a number the counterparty chooses
## 15.4 Special Mandatory Redemptions: The Deal-Break Gauge in the Acquirer's Curve
### 15.4.1 Desk framing: a bond with a deal-break digital stapled to it
### 15.4.2 Derivation: the implied break probability and the duration jump
### Specification for AI Implementation
### Deep-Dive Resource Graph
## 15.5 Antitrust and Regulatory Timelines as Survival Analysis
### 15.5.1 Desk framing: the regulator counts in working days
### 15.5.2 Derivation: Kaplan–Meier to competing risks
### Specification for AI Implementation
### Deep-Dive Resource Graph
## 15.6 Target vs. Acquirer: Spread Compression, Acquirer Widening, and Event Momentum
## 15.7 When the Deal Dies: The Merger as the Credit
## 15.8 Case Study: Warner Bros. Discovery 2025–26, the Covenant Strip and the Ticking Fee
## 15.9 Desk Debrief
- **Every deal clause is a payoff function.** Write it as (outcome, trigger, price at trigger), and store the issuer's counter-options (consent strip, defeasance, exchange offer) next to it in the security master.
- **CoC moneyness is coupon vintage.** The put cares about $101 - P$, not the credit story. The IG double trigger needs both inspectors, and for LBOs the trigger and the payoff covary ($M > 1$).
- **Portability is a short digital on a number the sponsor chooses.** Every point of permitted add-back lowers the odds that your put survives.
- **The SMR is a $\mathbb{Q}$ break gauge inside the acquirer's curve.** Its resolution is $|P^{\text{close}} - G_f|$, its control group is contaminated, and its duration jumps on ruling day.
- **Regulatory clocks are competing-risks survival data.** Censoring is informative, regimes shift $h_0$, and $\sum_k F_k = 1 - S$ is your unit test.
- **Silence is data, and beta is not alpha.** Update $\pi_d$ through quiet milestones, then strip the acquirer's beta before claiming the event. IDO or it didn't happen.
- **The most expensive three words have a cousin:** "defease certain obligations."
**The Spec You Hand the Robot.** "Build `event_credit_engine.py` (numpy, scipy, pandas; seeded). (1) `price_coc_put`: Monte Carlo over post-close spreads (decimal), deal × trigger × issuer-counter-option probabilities integrated analytically, bond priced on the post-close curve, return value in points per 100, stderr and $M$; exact zeros for degenerate inputs. (2) `curve_match_close_price`, `smr_fail_leg`, `smr_implied_break_prob`, `smr_duration`: PCHIP Z-spread curve over non-SMR tranches with an extrapolation flag; accrued to the redemption date; raise when $|P^{\text{close}} - G_f| < 10^{-6}$; clip and report. (3) `kaplan_meier`, `nelson_aalen`, `aalen_johansen`, `cox_ph` (Breslow, log-sum-exp, analytic gradient and Hessian), `bayes_deal_prob_path`. Assert: closed-form match for a constant spread; SMR round trip to $10^{-10}$; KM equals $1-$ECDF without censoring; CIFs sum to $1-\hat S$ within $10^{-12}$; Cox recovers planted $\beta$ within four standard errors. Units: years ACT/365 for clocks, 30/360 accrued, spreads decimal, prices per 100 face. Never pool regimes without a regime covariate. Never mix $\mathbb{P}$ and $\mathbb{Q}$ without saying so."
### Exercises
1. **The defeasance arithmetic.** With block 1, price the put on 1.85% and 2.95% bonds with 4.5 and 24.5 years remaining under an LBO spread of 350bp *(illustrative)*. Then compute what a sponsor saves per 100 face by depositing Treasuries instead of paying 101. Explain why 95% of EA's legacy holders declined the tender, and whether they were right.
2. **The blind thermometer.** Find the parallel Treasury move after issue at which a 4.60% three-year SMR tranche has $P^{\text{close}} = G_f$. Explain why $\hat\pi_f$ is undefined there and which instrument you would use instead.
3. **The vintage anomaly.** For an IG issuer on a take-private watch list, regress same-issuer Z-spreads on coupon with maturity controls. Derive the sign the embedded put predicts for the coupon coefficient, and design the test that tells the put apart from the low-coupon bonds' lower convexity and better index eligibility.
  [...truncated]
### Deep-Dive Resource Graph

==== 16_ch16_post_reorg_equities_and_claims.md (18,586 words)
# Chapter 16: Post-Reorganization Equities, Rights Offerings & Bankruptcy Claims
## Cold Open: Effective Date, 9:31 a.m.
## 16.1 The Back-End Equity Problem: What Emerges and Who Is Not Allowed to Hold It
### 16.1.1 Desk framing: a plan is a security factory with a distribution problem
### 16.1.2 What history says the stock does next
### Deep-Dive Resource Graph
## 16.2 Forced Selling as a Supply Process: From Fallen Angels to Orphan Equity
### 16.2.1 Desk framing: borrow the cleanest experiment on the shelf
### 16.2.2 Derivation: overhang, slow capital, and the drift you can schedule
### 16.2.3 Fitting the execution rate to published aggregates
### 16.2.4 From model to signal: momentum with an expiry date
### Specification for AI Implementation
### Deep-Dive Resource Graph
## 16.3 Rights Offerings and Backstops: Pricing the Put You Sold
### 16.3.1 Desk framing: the backstop is the player who agrees to call any bet
### 16.3.2 Derivation: the right is a call, the backstop is a put
### 16.3.3 Desk Myth vs. Desk Reality
### 16.3.4 Case Study: the Hertz rights offering, June 2021
### Deep-Dive Resource Graph
## 16.4 Warrants: Long-Dated Calls Handed to People Who Were Told They'd Get Nothing
### 16.4.1 Desk framing: the consolation prize is the most convex thing in the plan
### 16.4.2 Derivation: dilution, the fixed point, and the jump that Kaz gets backwards
### 16.4.3 Case Study: the Hertz warrants, from "worthless" to \$1.35bn of intrinsic value
### Specification for AI Implementation
### Deep-Dive Resource Graph
## 16.5 Claims: 503(b)(9) vs. General Unsecured, and the Denominator Problem
### 16.5.1 Desk framing: a claim is a zero-coupon bond with a random face, a random maturity, and a random number of siblings
### 16.5.2 The statute block: what decides the face value
### 16.5.3 Derivation: the random denominator
### Specification for AI Implementation
### Deep-Dive Resource Graph
## 16.6 Case Study: Hertz 2020–2026, the Whole Circuit
## 16.7 Case Study: Spirit Airlines, the Five-Month Zero
### Deep-Dive Resource Graph
## 16.8 Putting It Together: A Post-Reorg Book
### 16.8.1 The distribution you are actually trading
### 16.8.2 Sizing: Kelly with a trapdoor, then a liquidity ceiling
### 16.8.3 The pair trades
### Specification for AI Implementation
### Deep-Dive Resource Graph
## 16.9 Desk Debrief
- **The plan value is a negotiated number.** Anchor every post-reorg instrument to the price insiders actually pay in the same plan (the rights price, the direct-investment price), never to the disclosure statement's midpoint.
- **Forced selling is a supply schedule, not a mood.** Overhang $Q_0$, execution rate $\theta$ (about 3.4 a year, a 2.4-month half-life, from the fallen-angel aggregates), capital $M_t$ arriving slowly. The discount peaks *after* the event when delivery is staggered, and the signal expires when the 13G says the constrained holders are out.
- **The post-reorg premium is a portfolio property.** Mean +40%, median zero, and no alpha after 2010 for listed names. Only a diversified book harvests the right tail, and the surviving OTC alpha does not scale past a few hundred thousand dollars a name.
- **A backstop is a short put, and the fee is its smallest leg.** At a 25% discount and 70% volatility the fair fee is about 6%; the discount, the fee paid in shares and the exclusivity option take the all-in transfer to about 20% of the raise. Since *ConvergeOne*, an exclusive backstop without a market test also carries legal reversal risk.
- **Price warrants with dilution, and never charge for the funeral twice.** With a market spot, jump-to-default enters through $r + \lambda$, not as an $e^{-\lambda T}$ haircut. The plan's own warrant valuation tells you the volatility the other side assumed.
- **A claim is long a ratio and short a call at par.** Near par, pool uncertainty costs recovery (about 8 points at a 30% log-sd); deep out of the money, it helps. Know which side of the kink you are on.
- **The 503(b)(9)/GUC pair isolates pool risk.** The person who has counted the leases, applied the §502(b)(6) cap and struck the duplicate claims should be long the GUC against the 503(b)(9). That person used to work at PJT.
- **Check the 13-week model before the multiple.** Spirit's first post-reorg equity lasted under six months; Hertz's warrants run to 2051 and the company was back in the room in 2026. Runway drives the jump term.
**The Spec You Hand the Robot.** Build `post_reorg_engine.py` with five modules, each under $\mathbb{P}$ unless labeled, each carrying the asserts in Blocks 1–5 as unit tests. (1) `overhang`: `ForcedSellerOverhang(Q0, theta, M0, M_star, rho, kappa, alpha=None)` with `Q`, `discount`, `drift`, `half_life`, `peak_time`; inputs from a holder registry (plan schedule, Rule 2019, 13D/13G, Form 4, 13F, trustee reports); output a daily expected-excess-drift signal per name that is exactly zero once executed fraction reaches one. (2) `rights`: `RightsOffering(n0, m, K)` with `post_money`, `right_value_per_plan_share`, `backstop_payoff`, `fair_fee(x0, sigma, T)`; plus an all-in transfer with fee in shares, reserved fraction `a`, unexercised-in-the-money fraction `eta`, and a fee-survival probability by circuit and market test. (3) `warrants`: `warrant_price(S, K, T, sigma, r, omega, lam)` as the dilution fixed point with jump via $r+\lambda$; `implied_vol_warrant` by bracketed root-finding; spot must be labeled `market` or `going_concern`, and only the latter may take a survival haircut. (4) `claims`: register ingestion (drop superseded and withdrawn claims, apply §502(b)(6)/(b)(7) caps, separate 503(b)(9) by receipt evidence), `expected_recovery_lognormal`, `price_claim` for `GUC` and `503b9`, the priority-spread decomposition, and `in_kind_recovery` for claims fixed in petition-date dollars. (5) `book`: jump-lognormal return simulation, Kelly on a grid strictly below one, half-Kelly, a liquidity cap of participation × ADV × exit days, and a runway-driven jump intensity $\lambda_t = \lambda_0 e^{-\beta L_t/B_t}$. Units: shares in millions, money in USD millions unless a field says per share, rates and intensities per year, time in years. Seed every simulation with `np.random.default_rng(16)`. ROBO should refuse, not guess, when a required field is missing.
  [...truncated]
### Exercises
### Deep-Dive Resource Graph

==== 17_ch17_private_credit_public_private_convergence.md (16,899 words)
# Chapter 17: Private Credit & the Public–Private Convergence
## Cold Open: Volatility N/A
## 17.1 One Borrower Pool, Two Pricing Regimes
### 17.1.1 Desk framing: the same credit, measured twice
### 17.1.2 What "private" actually buys: access and patience
### Deep-Dive Resource Graph
## 17.2 The Mark as a Filter: Smoothing, Stale Prices and the Illusion of Low Volatility
### 17.2.1 Desk framing: you are fitting someone else's model
### 17.2.2 Derivation: the Getmansky–Lo–Makarov smoothing model
### 17.2.3 Recovering the beta: Dimson sums and the public-leads-private test
### 17.2.4 Unsmoothing, and why you should do less of it than you want to
### Specification for AI Implementation
### Deep-Dive Resource Graph
## 17.3 Marking the Unmarked: BDC P/NAV, Implied Markdowns and the Non-Accrual Gap
### 17.3.1 Desk framing: a listed CLO with the manager holding the pen
### 17.3.2 Derivation: from a listed price to an implied asset markdown
### 17.3.3 Derivation: the non-accrual gap and the implied carrying value of bad loans
### Case Study: OBDC and OBDC II, November 2025 to August 2026: Same Loans, Three Prices
### Deep-Dive Resource Graph
## 17.4 Two-Way Takeouts: PC↔BSL Migration as a Regime-Conditional Flow
### 17.4.1 Desk framing: the border moves, and a public variable moves it
### 17.4.2 Derivation: competing exits with a regime covariate
### Case Study: Finastra 2023, the Steal, and the 2024 Reversal
### Deep-Dive Resource Graph
## 17.5 Banks Moved Up the Stack, Insurers Moved Down the Funnel
### 17.5.1 Desk framing: nobody left; everybody changed seats
### Case Study: Two Bank Partnerships, Read as Term Sheets
### 17.5.2 Insurers: the capital funnel and the ratings passport
### Deep-Dive Resource Graph
## 17.6 Semi-Liquid Vehicles and the Redemption Game
### 17.6.1 Desk framing: the failure mode moved from defaults to redemptions
### 17.6.2 Derivation: a run with a pro-rata cap
### Case Study: The Redemption Quarters of 2026
### Deep-Dive Resource Graph
## 17.7 The Plumbing That Turns Marks into Prices
### 17.7.1 Desk framing: a 2022 prediction, scored in 2026
### 17.7.2 Five price sources, and what each one actually measures
## 17.8 Systematic Approaches to Private Credit
### 17.8.1 Desk framing: four marks a year and a lot of footnotes
### 17.8.2 The features worth computing
### 17.8.3 Derivation: what the public data already knows about the next marks
### Deep-Dive Resource Graph
## 17.9 What a Public-Markets Quant Desk Can Arbitrage
### Deep-Dive Resource Graph
## 17.10 Desk Debrief
Ines replays the cold-open hand. The desk bid the \$25mm of notes two points back of the screen and hedged half the risk with a short in the BDC's own equity, on the view that the seller knew about the redemption queue at a sibling-type vehicle and the equity would reprice before the bonds. The markouts said they were right about the direction and wrong about the ratio: the equity fell more than the bonds, as the capital-structure algebra predicts when the debt is money-good. The hand history goes in the file. *(The trade is illustrative.)*
- **Private credit is public credit with the price removed.** Same borrowers, same sponsors, two pricing regimes. The difference is measurement, not credit.
- **A mark is a moving average of the truth.** Reported volatility is deflated by $\sqrt{\sum_k\theta_k^2}$, contemporaneous beta by $\theta_0$, and the Sharpe ratio is inflated by $1/\sqrt{\sum_k\theta_k^2}$. NAV momentum is a property of the valuation calendar.
- **Sum the lags.** The Dimson aggregated beta recovers the true beta, and the lagged coefficients forecast the next mark from public data you already have.
- **Unsmooth gently.** Inverting a kernel with $\theta=0.7$ amplifies measurement noise more than sixteen times. Pool across co-holders and report intervals.
- **One discount point is half an asset point.** $m=\big((1-\phi)-P/\text{NAV}\big)/(1+\ell)$: at 1.1x leverage, a 20% equity discount says the loans are worth about 90, not 80.
- **The non-accrual pair hides a mark.** $\hat R^{\text{mark}}_{\text{NA}}=(w^{FV}/w^{C})(FV/C)$; a rising cost-minus-fair-value gap with a falling headline rate is the hole getting deeper.
- **A 5% cap rations a run; it does not stop one.** Requesting dominates once $m>0$ is believed, the transfer is $p\cdot m$ per quarter, and the request percentage is the best public belief series in the asset class.
- **Trade the wrappers.** BDC equity, BDC bonds, ETFs with firm bids, CDX Financials, the loans semi-liquid funds sell and the supply private takeouts create. IDO or it didn't happen.
### The Spec You Hand the Robot
**Vague version.** "ROBO, minimize the mark gap." ROBO writes to the valuation committee recommending that all loans be marked to the listed BDC's implied price, which minimizes the gap to zero and the manager's fee base by 10%. It did exactly what was asked.
**Precise version: the Mark-Gap Monitor.**
- **Inputs.** `bdc_quarterly`, `soi`, `redemptions` and `public_index` with the §17.2 schemas; quarterly frequency; decimals, not percent strings; net (not gross) debt to NAV; NAV vintage stored alongside each restatement.
- **Step 1, kernel.** For each cluster of co-holding vehicles, fit $\hat\theta$ by pooled Dimson regression with $K\le3$, requiring $10(K+1)$ observations; bootstrap quarters in blocks of four; refuse a point estimate if the 90% interval for $\theta_0$ is wider than 0.4.
- **Step 2, pending mark.** $\Pi_{i,t}=\hat\beta_i\sum_{j=0}^{K-1}\bar\Theta_{j+1}F_{t-j}$ using the vehicle's sector-matched public index.
  [...truncated]
### Exercises
### Deep-Dive Resource Graph (Chapter 17)

==== 18_ch18_otc_microstructure_and_avellaneda_stoikov.md (13,784 words)
# Chapter 18: OTC Credit Microstructure & the Market Maker's Equations
## 18.1 Harris's Zoo, Relabeled for Credit
## 18.2 Roll's Trick: Seeing the Spread When No One Will Show You One
### 18.2.1 Derivation
### Specification for AI Implementation (Roll estimator)
## 18.3 Who Knows More Than You: Glosten–Milgrom Recalled, Kyle Derived
### 18.3.1 Glosten–Milgrom in one line
### 18.3.2 Kyle (1985), derived
### 18.3.3 Translating Kyle to the RFQ
### Specification for AI Implementation (Kyle estimator)
## 18.4 Avellaneda–Stoikov, Derived Without Skipping Steps
### 18.4.1 Setup
### 18.4.2 The HJB equation
### 18.4.3 Step 1: the frozen-inventory value and the reservation prices
### 18.4.4 Step 2: the exponential ansatz
### 18.4.5 Step 3: the first-order condition
### 18.4.6 Step 4: the AS approximation, and the two halves of the spread
### Specification for AI Implementation (AS quoting core)
## 18.5 GLFT: Inventory Bounds, Linear ODEs, and the Stationary Dealer
## 18.6 Jump-to-Default Inside the HJB
### 18.6.1 Exact reservation prices
### 18.6.2 Where $\lambda^{\mathbb{P}}$ comes from: the RSSG bridge
### 18.6.3 Case Study: Altice France (March 2024) and Credit Suisse AT1s (March 2023)
### Specification for AI Implementation
## 18.7 RFQ Hit Rates and the Price of Staying at the Table
### Specification for AI Implementation (win curve, hit-ratio dual, quote assembly)
## 18.8 Decoding TRACE
### Specification for AI Implementation (TRACE decoder)
## 18.9 BWICs: First-Price Auctions With a Leaky List
### 18.9.1 Case Study: The LDI BWIC Week, October 2022
### Specification for AI Implementation (BWIC shading and leakage)
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
  [...truncated]
### Deep-Dive Resource Graph

==== 19_ch19_portfolio_trading_pricing_engines.md (13,958 words)
# Chapter 19: Portfolio Trading & Basket Pricing Engines
## 19.1 What a Portfolio Trade Is (and Isn't)
## 19.2 The Master Equation: Four Terms, One Price
### 19.2.1 Derivation: the basket bid as a certainty equivalent
### Specification for AI Implementation
## 19.3 Per-Line Liquidation Cost: LCS, Size, and the Fat Tail
### 19.3.1 Derivation: from a standalone score to a basket cost
### Specification for AI Implementation (handling cost)
## 19.4 The Hedge: Collapsing 150 Lines into One Lump
### 19.4.1 Derivation: the minimum-variance hedge and the residual
### Specification for AI Implementation (factor model and hedge)
### Deep-Dive Resource Graph
## 19.5 Residual Covariance for 150 Stale Bonds
### 19.5.1 Derivation: factor structure, staleness, shrinkage
### Specification for AI Implementation (residual covariance)
## 19.6 Eviction: Which Lines to Kick Out, and the Price of Keeping Them
### 19.6.1 Derivation: marginal cost, exact removal saving, greedy loop
### 19.6.2 Case Study: The H1 2022 Reversal
### Specification for AI Implementation (greedy eviction)
## 19.7 Stress Liquidity Commonality: When Every $c_i$ Moves Together
### 19.7.1 Derivation: a common multiplier in costs, a rank-one spike in risk
### 19.7.2 Case Study: March 2020 and the April 2025 Tariff Week
### Specification for AI Implementation (regime and stress covariance)
## 19.8 Adverse Selection in Baskets: The Mystery Box
### 19.8.1 Derivation: the inclusion model and the AS charge
### 19.8.2 Case Study: The Mystery Box at Line 117 (illustrative)
### Specification for AI Implementation (adverse selection and hand history)
### Deep-Dive Resource Graph
## 19.9 The Buy Side: When to Use a PT, and How to Build One the Dealer Will Love
### 19.9.1 Derivation: the all-or-none inequality
## 19.10 Engineering for 90 Seconds
### Specification for AI Implementation (the full engine)
### Deep-Dive Resource Graph
## 19.11 Desk Debrief
- **A PT bid is four terms plus a margin:** fair value, minus liquidation cost, minus residual risk *after the hedge*, minus adverse selection, minus $\pi$. Every term is in dollars until the very last line.
- **You are pricing one lump and a residual.** The hedge turns $\Sigma$ into $\Sigma^{\text{res}}$, and $\Sigma^{\text{res}}$ is the re-hedged covariance for *any* basket, so eviction re-hedges for free.
- **LCS is a standalone price.** Use only its handling share inside a basket, scale it for size, and never multiply it by duration again.
- **Staleness is variance, not a haircut.** Line 42 is not a bad bond; nobody knows what it is worth, and that ignorance is what the engine prices.
- **Evict on exact removal savings, and recompute after every eviction.** Liquidity scores evict line 42. Only the AS term evicts line 117.
- **The liquidity factor does not diversify.** In stress, one regime score must move $m$, $\gamma$ and the basis together.
- **The hand history is by line and net of the hedge.** A basket-level markout averages away the two cards that were face down. IDO or it didn't happen.
- **Ninety seconds is 89 seconds of precomputation and judgment, and one second of linear algebra.**
### The Spec You Hand the Robot
> Build `price_pt(inquiry, model_state, market_state) -> Quote`. **Inputs:** a struct-of-arrays inquiry ($N\le500$ lines: id, signed par \$, composite mid as a fraction of par, age in business days, print fraction, LCS at \$4mm, OASD, OAS, sector, daily idiosyncratic vol, PRS, days to lender call, ad hoc flag). Also: overnight loadings $B$ $(N,K)$, factor covariance $\Omega$ $(K,K)$, hedge loadings $A$ $(H,K)$ and basis covariance $U$ $(H,H)$, plus live ETF discount z-score and bid–ask percentile. **Compute (all under $\mathbb{P}$, all in dollars):** handling cost (19.3); idiosyncratic variance with staleness, print-frequency inflation and ridge (19.5); $\Sigma^{\text{res}}$ by Schur complement (19.4), PSD-projected, with $\operatorname{cond}\le10^6$; the stress spike (19.9) from one regime score that also scales $\gamma$ and the basis; the AS charge (19.10) from a logistic inclusion model; greedy eviction on exact removal savings (19.7), stopping at the target cost per dollar, $\alpha$ of MV, or $k_{\max}$ lines; and the minimum-variance hedge of the kept basket. **Return:** cash, cost in \$ and in bp of gross MV, the four-term decomposition, hedge notionals, evicted ids, a `hit_target` flag and latency. **Refuse** if mids look like points, if more than 20% of MV has age $>10$, or if a guard fails. **Escalate to a human** if $s\ge1$, if any $\text{PRS}>0.7$, or if one line carries more than 25% of cost. **Tests:** CE matches Monte Carlo under Gaussian P&L; hedged variance equals the Schur form; costs are side-symmetric; eviction strictly lowers cost per dollar; stress cost is at least 2× calm on the reference basket; the live path runs in under 1 s.
  [...truncated]
### Exercises
### Deep-Dive Resource Graph

==== 20_ch20_credit_etf_creation_redemption_arb.md (13,883 words)
# Chapter 20: Credit ETF Creation/Redemption Arbitrage (HYG, JNK, LQD, BKLN)
## 20.1 The Machine: Two Markets, One Wrapper
## 20.2 NAV Is an Opinion: Price, Evaluated Prices and the Bid Side
### 20.2.1 Derivation: three reasons a price differs from a NAV
### 20.2.2 Measuring staleness: does the NAV catch up?
### 20.2.3 The three readings of a discount
## 20.3 The Arbitrage Band, Derived
### 20.3.1 The static band
### 20.3.2 The band with a balance sheet
## 20.4 Custom Baskets: The Liquidity Sink
### 20.4.1 The rule and the regulator's worry
### 20.4.2 What the baskets actually look like
### 20.4.3 Derivation: the custom basket as a quadratic program
## 20.5 Case Study: March 2020, When the ETF Was the Only Price in Town
### 20.5.1 The tape
### 20.5.2 The Fed buys a seat at the table
### 20.5.3 How a systematic desk would have flagged and traded it
## 20.6 BKLN: The Basket That Cannot Settle
### 20.6.1 Derivation: the settlement gap and the liquidity runway
### 20.6.2 What the wrapper is now being asked to hold
## 20.7 Building the Arbitrage Monitor
### Specification for AI Implementation
## 20.8 Desk Debrief
- **A credit ETF is two markets and a conversion right.** The secondary market nets; only the residual reaches the APs, and the band is the price of converting.
- **Premium = flow + staleness + bid-side constant** (20.1). Only the flow term is a trade. Staleness is a forecast of tomorrow's marks, and $\bar c$ is a decimal point in the valuation policy.
- **The band is $[\bar c - c^R - f^R - k^R,\ \bar c + c^C + f^C + k^C]$** (20.4). Bid-side NAVs slide it up by $\bar c$, which is why calm HY ETFs "trade at a premium." Custom baskets move the two edges independently.
- **In stress, price impact multiplies**: $\psi = \bar\gamma \sigma_b^2 T^{\text{h}}$ (20.5). Two times 36 times 4 turns a 1 bp flow into a 3% discount without anyone leaving the table.
- **Custom baskets are worth $\mathcal{D}/(2\theta)$** (20.7): the dispersion of net costs over the fund's tracking aversion. They are how PT dealers recycle risk, and losing them in H1 2022 showed up in PT pricing.
- **March 2020 was not a broken arbitrage.** IG's flow term collapsed because it was the most sellable risky asset. The Fed fixed it by lowering everyone's price of risk, mostly before it bought a share.
- **Loan ETFs live or die by (20.8):** sleeve over burn rate against the settlement lag. It is Theo's 13-week model in a 40 Act wrapper.
- **IDO or it didn't happen:** an ETF discount trade earns only the convergence, net of rate and spread beta.
**The Spec You Hand the Robot.** *Vague:* "Build me an ETF arb monitor." *What ROBO built:* see §20.7, all 206 alerts of it. *Precise:* Build `etf_arb.monitor(date, ticker) -> Signal`. **Inputs:** `etf_daily` and `holdings` per the schema in §20.7, published creation and redemption baskets, TRACE same-day dispersion `u`, and the change in shares outstanding as $F$. **Compute:** $\bar c$, $c^C$ and $c^R$ from half-LCS weights; the static band (20.4) with the fund's fee schedule; $\hat\eta$ from (20.3) on a trailing 250-day calm window, reported with its attenuation bound; $\hat s_t$ from (20.2) using ETF returns as the proxy for true returns; $\hat\psi$ from (20.5) as the regression slope of the premium on $F$ over a rolling window; the regime label from `classify`. **Guards:** fractions of NAV everywhere; refuse to run without `nav_convention`; skip days with no NAV strike; mark any day with a pricing-methodology change as `measurement_noise`; never emit a trade signal from the premium alone. **Outputs:** the regime label, the band edges, the three components of (20.1), $\hat\psi$, and for loan funds the runway from (20.8). **Tests:** the asserts in Blocks 1–6, plus one replay of 2020-03-09 to 2020-03-27 that must label LQD's March 19 discount `flow_dislocation_redeem` and HYG's same-day premium `inside_band` or `measurement_noise`.
  [...truncated]
### Exercises
### Deep-Dive Resource Graph

==== 21_ch21_leveraged_loans_and_clo_microstructure.md (16,343 words)
# Chapter 21: Leveraged Loans, CLOs & Loan-Market Microstructure
## 21.1 The Leveraged Loan as an Instrument: A Floater That Is Short a Call
### 21.1.1 Derivation: carry, price, and the two durations
## 21.2 Plumbing: Settlement, Marks, and the Arrival of E-Trading
### 21.2.1 Settlement: the slowest thing in credit
### 21.2.2 Derivation: delayed compensation is a forced repo
### 21.2.3 E-trading arrives, two decades late
### Deep-Dive Resource Graph (21.2)
## 21.3 CLO Anatomy and the Arbitrage
### 21.3.1 Derivation: the arbitrage and its 11× gearing
### 21.3.2 Derivation: why every CLO owns the same 200 names
## 21.4 The Tests as an Option Book
### 21.4.1 Derivation: the adjusted numerator
### 21.4.2 The cure-trade theorem
### 21.4.3 The CLO Forced-Sale Pressure Index
### Case Study: COVID-19 2020 and the 2022–2023 Junior-OC Failures
### Specification for AI Implementation
### Deep-Dive Resource Graph (21.4)
## 21.5 Repricing Waves: The Borrower Exercises
### 21.5.1 Derivation: the price of a loan under a repricing hazard
### Case Study: The January–April 2025 Round Trip, and the 2026 Replay
### Specification for AI Implementation (repricing engine)
## 21.6 Loan ETFs vs CLO ETFs: Where Liquidity Transformation Lives
### 21.6.1 Derivation: the buffer is a queue
### Case Study: JAAA, April–May 2025
### Specification for AI Implementation (liquidity queue)
### Deep-Dive Resource Graph (21.6)
## 21.7 Trend and Momentum in Loans: Smoothing, Ceilings, and Forced Sellers
### 21.7.1 Derivation: what smoothing does to a mark
### Specification for AI Implementation (stale marks)
## 21.8 CLOs Inside the LMT
### Case Study: Two Holder Bases, One Uptier Proposal
### Deep-Dive Resource Graph (21.8)
## 21.9 Desk Debrief
- **A performing loan is a floater that is short a par call.** Its spread duration is about 2.7 on the way down and about 0.25 on the way up when the repricing window is open (21.7). Quote carry net of the expected repricing loss (21.8), or you are quoting fiction.
- **The OC test is an option book written by the CLO equity.** It cannot see performing-loan prices and is short the cheapest tail of the CCC book (21.5). Past the 7.5% cliff, each dollar of new CCC costs about $(1 - p^{\ast})$, around 42 cents at Kundu's 58-cent average, through *other* loans.
- **The cure is deterministic: sell the richest CCC** (21.6). Forced sellers sell the freshly downgraded loan, which is the one fundamental buyers want. FSPI tells you who must sell, and the reversal pays the liquidity provider.
- **Every repricing costs CLO equity about 11× the spread cut** (21.3). The ETF bid for AAA resets is the equity's counter-move.
- **Settlement is a risk factor, not a back-office detail.** About 20 days on average; delayed compensation is a forced repo at the base rate; a loan fund's buffer scales between $\sqrt{\ell}$ and $\ell$ (21.9).
- **Retail liquidity moved to the tranche because the tranche settles like a bond.** JAAA could redeem in kind in April 2025. A loan ETF cannot.
- **Desmooth the marks before you believe a momentum backtest** (21.10). Then condition winners on headroom and losers on FSPI.
- **Ask two questions.** What does the credit agreement say? What does the CLO indenture say? The second decides who is a forced seller under the first.
**The Spec You Hand the Robot.** Build `loan_clo_engine` with five deterministic, seeded modules and the asserts from Blocks 1–5:
1. `acpa(pool, cash, ccc_limit)` implements (21.5): cheapest-first CCC excess, $\max(0, 1-p)$ haircuts, defaulted loans at $\min(p, R^{\text{ag}})$, discount loans at purchase price, and indenture priority "without duplication."
2. `cure_candidates(pool)` ranks CCC sales by exact recomputed ΔACPA and checks the bound (21.6).
3. `fspi(holdings, outstanding, cushion, excess)` returns, for each loan, the expected fraction sold. It uses the logistic calibrated to $\pi = 13.27\%$ at a 4% cushion with $+1.56$ pp per $-3.26\%$ of cushion, and it checks that holdings never exceed outstanding.
4. `loan_price(m, s, base, T, h)` implements (21.2)/(21.7), with a monthly-logit hazard converted by $h = -12\ln(1-q)$, margin and CSA kept as separate state, one-sided spread durations, and (21.8) carry loss.
5. `buffer_needed` and `etf_discount_bound` implement (21.9) and the band, cross-checked by simulation within 8%. Desmoothing implements (21.10) with a Dimson beta.
Units: prices as fractions of par in code and points in reports, spreads as decimals, \$mm for par, business days for $\ell$. Never infer a CCC classification, a market-value source or a test trigger: read it from the parsed indenture, or raise.
  [...truncated]
### Exercises
### Deep-Dive Resource Graph

==== 22_ch22_market_structure_regulation_trends.md (16,001 words)
# Chapter 22: Market-Structure Regulation & the Forces Reshaping Liquidity
## 22.1 A Rule Is a Price: Taxes on Balance Sheet, Time, and Information
### 22.1.1 Derivation: the regulatory cost of carry in the reservation price
### Specification for AI Implementation
## 22.2 TRACE, 2002–2027: The Transparency Ledger
### 22.2.1 Derivation: the reporting delay is an option the block dealer holds
### 22.2.2 Derivation: what hides behind "5MM+"
### 22.2.3 Case Study: The One-Minute Rule That Died (2022–2025), and the Block Pilot That Never Lived (2019)
### Specification for AI Implementation (TRACE regime layer)
## 22.3 T+1 and the Settlement Clock
### 22.3.1 Derivation: why T+1 cut margin by about a quarter
### 22.3.2 Fails, and the identity hiding in the fails charge
### 22.3.3 Case Study: May 28–29, 2024, the Weekend the Clock Moved
### Specification for AI Implementation (settlement clock)
## 22.4 The Treasury Clearing Mandate: Netting, Margin, and the Price of a Very Large Market
### 22.4.1 Derivation: what multilateral netting buys, and when it stops
### 22.4.2 Derivation: dealer capacity as a convex state variable
### 22.4.3 Case Study: The March 2020 Dash for Cash
### Specification for AI Implementation (netting and capacity)
## 22.5 Dealer Capital: Volcker, the Leverage Ratio, and the Endgame
### 22.5.1 Case Study: The Basel III Endgame Saga, 2023–2026
## 22.6 CDS: From the Index Clearing Mandate to SBSR, Rule 9j-1, and the Dealer Rule That Wasn't
### 22.6.1 Derivation: when clearing a CDS is cheaper than not
### 22.6.2 Case Study: Two Stresses, Two Instruments (Q1 2023 and April 2025)
## 22.7 The Regulated Venue: Consolidation, Tapes, and the Non-Bank Question
## 22.8 The Regulatory Event-Study Engine
### 22.8.1 Derivation: difference-in-differences around an effective date
### Specification for AI Implementation (event-study engine)
## 22.9 Desk Debrief
- **A dealer sells balance sheet, time, and information, and every rule is a tax or a subsidy on one of them.** The desk does not comply with rules; it prices them, and it dates them.
- **Rent is $h\cdot\max(\kappa_{\text{RWA}}\text{RW}, \kappa_{\text{LR}})\cdot\tau^{\text{hold}}$.** A flat dealer widens both sides; a long dealer skews. For a 2-year Treasury, rent is the whole spread (breakeven hold of three to four days); for a BBB, it is a rounding error (about a month). That inequality explains why Treasuries went agency first.
- **A reporting delay is an option the block dealer holds**, worth $2\lambda Q/T_u$ of spread per unit of delay. The fifteen-minute, \$5mm/\$1mm equilibrium has survived attacks from both sides since 2019. It is priced into every block you quote.
- **Behind "5MM+" is a Pareto tail** with $\alpha \approx 1.67$ for IG and $1.33$ for HY, so block-size variance does not exist. Use the historic file, medians, and rating-specific tails; never average at the cap.
- **Square roots and floors.** T+1 cut the volatility component of margin by between $1-\sqrt{2/3}$ and $1-\sqrt{1/2}$, and DTCC's 23–29% landed inside the bracket. Netting shrinks exposure by $1/\sqrt{N-1}$ in a two-way market and by almost nothing in a one-way market, which is the only market in which you need it.
- **Dealer capacity is a hinge:** rent in calm markets, convex in stress, with the kink near a third of utilization. Make the liquidity model's dealer term a slow state variable, not a constant.
- **Capital rules are dated changes in $\kappa$.** For each one, ask which inventories are leverage-bound and which are risk-bound; the 2023–2026 endgame saga moved them in opposite directions.
- **Every effective date is a structural break, and every abandoned rule is a placebo.** No control group, no effect: IDO or it didn't happen.
### The Spec You Hand the Robot
*Vague version:* "make the models regulation-aware." *What ROBO built:* a dummy variable for every page of the Federal Register since 2002, a model with more regulatory features than bonds, and a perfect in-sample fit. *Precise version (prompt-ready):*
> Build `reg_cost_engine.py` (numpy and pandas only; every random draw seeded). (1) `regulatory_carry_bp(kappa_rwa, risk_weight, kappa_lr, hurdle, holding_days)`: $10^4\,h\,\max(\kappa_{\text{RWA}}\text{RW}, \kappa_{\text{LR}})\,\text{days}/365$, decimals only, reject ratios outside [0, 1] and non-positive days; `breakeven_holding_days` per (22.4); `carry_table` over a positions frame using $|$notional$|$. (2) `block_half_spread` per (22.6) with the positive-part guard and an optional inferred size; `pareto_alpha_from_imputed_mean` and `censored_impact` per (22.7), with $\alpha > 1$ enforced. (3) `margin_ratio` per (22.8) on the horizon including close-out; `fail_cost_annual` per (22.9). (4) `netting_factor_mc` returning simulated, theoretical ($1/\sqrt{N-1}$) and directional-floor (22.11) factors; `mandate_net_benefit` per (22.12); `capacity_hinge` calibrated from two published sentences. (5) `REGIME_DATES` as the single dated table, and `trace_regime_flags`, which rejects naive timestamps, compares New York calendar dates, keeps `one_minute_rule` False forever, and flags capped sizes by rating bucket. (6) `event_study_did` per (22.17) with a cluster bootstrap by bond, and `placebo`. Acceptance tests: the asserts in this chapter, unchanged, including: Treasury rent 1.15bp a week at 5% and 12%; margin ratios 0.7071 and 0.8165 bracketing DTCC's 0.71 and 0.77; netting factor within 2% of 0.204 at $N = 25$; a synthetic +2bp rule effect recovered within four standard errors despite a −3bp concurrent market move; placebo estimates below 0.25bp. Do not invent bond identifiers; use descriptive `bond_id` strings.
  [...truncated]
### Exercises
### Deep-Dive Resource Graph

==== 23_ch23_cross_asset_convexity_and_vol_surface.md (15,322 words)
# Chapter 23: Cross-Asset Convexity & the Volatility Surface
## 23.1 One Distribution, Many Strikes: The Capital Structure as a Vol Surface
### The Merton identity: equity vol is leveraged asset vol
## 23.2 From Equity Vol to a Spread: CreditGrades in Production
### The model
### Specification for AI Implementation
## 23.3 Puts vs. CDS: Carr–Wu and the Default Corridor
## 23.4 Skew as Jump-to-Default
### Specification for AI Implementation (continued): the put-surface engine
## 23.5 Greeks in Spread Terms: Natenberg for the Credit Desk
### Specification for AI Implementation (continued): spread Greeks
## 23.6 Capital-Structure Arbitrage: Rules, Returns, and Why Single Trades Lose
### Case Study A: May 2005, GM and Ford, or How to Lose on Both Legs
### Specification for AI Implementation (continued): the cap-structure backtester
## 23.7 Convertible Arbitrage: The Original Cap-Structure Trade
## 23.8 When the Surface Lies: Banks, Runs, and Contractual Inversions
### Case Study B: SVB, March 8–10, 2023
### Case Study C: Credit Suisse AT1, March 19, 2023
### Case Study D: Hertz, 2020–21, the Happy Inversion
### Specification for AI Implementation (continued): the bank override
## 23.9 Cross-Asset Trend: Does the Surface Lead the Spread?
## 23.10 Desk Debrief
- **The capital structure is one distribution sliced at different strikes.** Equity is the call, bonds are short puts, CDS is the put without rates, and a low-strike equity put is a CDS that forgot to tell anyone.
- **Equity vol is leveraged asset vol** ($\sigma_E E = \sigma_V V N(d_1)$). Cheap stocks are mechanically high-vol stocks, the skew is built in, and plugging $\sigma_E$ in for $\sigma_V$ overstates default risk by the leverage.
- **CreditGrades is the production bridge**, with honest warts: the time-zero ghost, a reported error in the published closed form, two different recoveries, and $\nu$ fitted on non-financials. Integrate the legs yourself and test against Monte Carlo.
- **A put spread inside the default corridor is a model-free default claim** (Carr–Wu). Match the payment convention (American pays at default, European at expiry) before you trade the basis against CDS.
- **The low-strike floor $P(K)/K$ is the hazard.** Jumps make it flatten to a constant; stochastic vol sends it to zero. Diagnose with prices, not implied vols.
- **Hedge ratios are the part of Merton that works.** Cap-structure arbitrage bets the ratio is right and the price is wrong; single trades lose, portfolios earn. Strip carry, simulate defaults, and stress the May 2005 vector (stock up, spread up).
- **The surface breaks where the process is not a diffusion:** runs (SVB), contractual triggers (Credit Suisse AT1), and estates whose value tail was fatter than anyone modeled (Hertz). The credit agreement, the prospectus, and the deposit base decide those cases, and reading them is the ex-RSSG analyst's edge.
**The Spec You Hand the Robot.** Build `ch23_cross_asset_surface`, numpy/scipy/pandas only, seeded RNG (`seed=23`), no network. (1) `cg_survival`, `cg_cds_spread`, `cg_implied_vol` per (23.3)–(23.5), with the leg integration monthly, the time-zero mass in the protection leg, `nan` outside the inversion range, and a Monte Carlo check with a Brownian-bridge correction. (2) `urc_from_puts` per (23.6), returning bid and ask bounds and a payment `convention`, and `urc_from_cds` per (23.7) with a matching `payment` argument; raise on convention mismatch. (3) `jtd_put_price` and `jtd_fit` per (23.8), fitting $(\sigma, \lambda)$ jointly on $P(K)/K$, with borrow backed out of at-the-money parity first and the `floor_ratio` diagnostic. (4) `spread_greeks` (CS01, convexity, DTS) and `cg_greeks` (shares per \$10mm, stock-space gamma, equity and asset vega), plus JTD per notional reported as its own line. (5) `capstruct_backtest` with Yu's rules, carry reported separately from convergence, defaults simulated at the CDS-implied hazard in production runs, and an event-sign stress (stock +20%, spread +30%). (6) A router that sends any issuer with deposits above 50% of liabilities to `bank_run_dd`, and flags any instrument with a contractual write-down trigger as `contractual_waterfall_override`. Inputs in decimals and years; outputs in bp, \$, and shares, with units in every column name. Every function raises on non-positive prices, vols, or debt.
  [...truncated]
### Exercises
### Deep-Dive Resource Graph

==== 24_ch24_bond_cds_basis_and_deliverables.md (16,114 words)
# Chapter 24: Bond-to-CDS Basis & Deliverable Obligation Mechanics
## 24.1 Two Doctors, One Patient, and the Frictionless Lie
## 24.2 Pricing the Swap: Two Legs and One Risky Annuity
### 24.2.1 Derivation
### Specification for AI Implementation (CDS legs, par spread and upfront)
## 24.3 Four Things People Mean by "Basis"
### 24.3.1 Derivation: why a par swap and a discount bond disagree even when nothing is wrong
### Specification for AI Implementation (bond-level basis: Z, PECS and JTD hedge ratio)
## 24.4 Funding, Repo, and the Counterparty: Why a Negative Basis Is Not Free
### 24.4.1 Derivation: the carry of each package and the arbitrage band
### Specification for AI Implementation (basis package carry and stress)
## 24.5 The Cheapest-to-Deliver Option
### 24.5.1 Derivation: when the option is worth nothing and when it is worth half of par
### Specification for AI Implementation (CTD under the two default regimes)
## 24.6 The Two-Stage Auction
### 24.6.1 Derivation: the inside market midpoint and the final price
### Specification for AI Implementation (two-stage auction simulator)
## 24.7 Trading the Basis Systematically
### 24.7.1 Derivation: a mean-reverting basis and the cost threshold
### Specification for AI Implementation (OU basis signal, net of costs)
## 24.8 When the Legal Layer Breaks: Successors, Orphans and Manufactured Credit Events
### 24.8.1 Derivation: the successor arithmetic
### 24.8.2 Case Study: Hovnanian, Sunrise Trails and the Coupon Nobody Wanted Paid (2017–2018)
### 24.8.3 Case Study: Windstream (2015–2019): One Sale-Leaseback, Two Successor Answers, One Auction
### 24.8.4 The patch, and what it does not reach
### Specification for AI Implementation (successor map and manufactured-event flags)
## 24.9 Desk Debrief
- **A CDS is a par instrument; your bond is not.** Compare them with PECS, or expect a Z-spread basis of ±15 bp on bonds priced perfectly, plus a few bp of day-count noise.
- **Hedge to jump-to-default, not to face.** $N^{\text{JTD}} = (P-R)/(1-R)$. At 88 and 40% recovery, \$10mm of bonds needs \$8mm of protection.
- **A negative basis is a funding trade with a default option.** Its ROE is divided by the haircut, and the haircut rises when the basis widens. Price the haircut process, not today's haircut.
- **The swap doesn't pay recovery. It pays par minus the auction price of the cheapest deliverable.** In bankruptcy that is close to recovery. In a failure to pay without acceleration it can be half of par from a solvent company.
- **The auction is a poker hand with the cards face up.** Read the open interest, respect the cap, and expect bonds to bounce after a large sell imbalance.
- **Exits make the Sharpe.** On the fallen-angel basis, transaction costs took three-quarters of the gross Sharpe until the exit rule cut the holding period.
- **Successors are arithmetic with cliffs.** At 25.0% nothing happens and at 25.1% your swap splits. Run the thresholds before the DC does.
- **The definition of default is a risk factor.** Flag affiliate payees, conditional financing, new long low-coupon deliverables and refinancings that orphan the swap, and use the 13-week model as evidence.
### The Spec You Hand the Robot
> Build `basis_engine` for one reference entity and its deliverable bonds. **Inputs:** an OIS curve (named and dated); CDS quotes by tenor with coupon and quoting recovery; a contract-terms table (day count, accrual on default, credit events, deliverable characteristics, Definitions vintage); bonds with coupon, maturity, seniority, price and timestamp; repo spread, haircut and borrow fee per bond. **Steps:** (1) bootstrap a piecewise-flat $\mathbb{Q}$-hazard curve and reproduce the standard upfront to the cent; (2) per bond, compute $Z$, ASW, PECS and the JTD hedge ratio, reporting $b^{Z}$ and $b^{\text{PE}}$ in bp; (3) compute the arbitrage band and ROE at current and doubled haircuts; (4) compute the regime-1 and regime-2 CTD payout over the deliverable set; (5) fit an OU model to the market-adjusted basis and emit entry and exit signals net of per-name costs; (6) run the successor map on any announced transaction and the manufactured-event flags on any missed payment. **Guards:** refuse a basis if the CDS mark is older than the bond print; raise an error on an empty deliverable set ("possible orphan"); round auction prices with halves going up; label every flag a heuristic. **Tests:** every assert in this chapter, in order. **Never:** use the bond's yield as its spread, use $R = 40\%$ for quoting and a different $R$ for valuation, or report an ROE without its haircut.
  [...truncated]
## 24.10 Exercises
### Deep-Dive Resource Graph

==== 25_ch25_nlp_pacer_and_covenant_scraping.md (14,417 words)
# Chapter 25: NLP for Credit Agreements, Indentures & PACER Dockets
## 25.0 Cold Open: Thirty Percent of What?
## 25.1 The Document Is the Constraint Set
### 25.1.1 Three layers of text
## 25.2 The Definition Graph: Legalese as a Typed Program
### 25.2.1 Two structures, not one
### 25.2.2 Reachability, nilpotence and blast radius
### 25.2.3 Cycles are real; condense them
### 25.2.4 Finding the vertices and edges
## 25.3 Basket Arithmetic: From Clauses to Dollars
### 25.3.1 Node types
### 25.3.2 The ratio basket, and the four words that stop a perpetual-motion machine
### 25.3.3 The add-back fixed point
### 25.3.4 Capacity is levered to add-backs
### 25.3.5 The builder basket, or the 13-week model gets a job
### 25.3.6 Maintenance versus incurrence: two node types, two default semantics
## 25.4 Value Leakage as a Flow Problem
### 25.4.1 The entity graph and max-flow min-cut
### 25.4.2 Case Study: J.Crew, 2016–2017, the Trapdoor as a Cut
## 25.5 Versions and Diffs: Amendments Are Events
### 25.5.1 Text diffs are blind where it matters
### 25.5.2 Case Study: Windstream, Aurelius, and One Defined Term (2015–2019)
## 25.6 The Docket as an Event Stream
### 25.6.1 The plumbing, with the numbers that bind
### 25.6.2 Rate limits as a token bucket
## 25.7 The Rule 2019 Time Series and the Holder Graph
### 25.7.1 From statements to a panel
### 25.7.2 The docket as a state machine
### 25.7.3 Case Study: Serta Simmons, Read From the Docket (2023)
## 25.8 Claims Registers and the Transfer Feed
## 25.9 From Text to Signal: Error, Decay and Discipline
### 25.9.1 Classifier error is an IC tax
### 25.9.2 Discipline and decay
## 25.10 The Covenant-and-Docket Engine
### Specification for AI Implementation
## 25.11 Desk Debrief
- **A basket is a function, not a sentence.** It maps the state of the company to \$mm and carries a scope, a netting flag and a source span. Without units, it didn't happen.
- **Parse definitions into a graph.** Evaluate it in Tarjan order and solve cycles as contractions. The EBITDA node has the largest blast radius in the document, so read it first and diff it every time.
- **"After giving effect to" turns a 25% cap into 33.3%.** Each add-back dollar buys $m + \sum p_j$ dollars of debt capacity, 4.85 at Halyard. Mags is right to distrust "adjusted."
- **Leakage is max-flow; the binding baskets are the min cut.** J.Crew's trapdoor created no capacity of its own. It moved the cut upstream onto \$250mm of "small" baskets.
- **Diff the capacity vector, not the tokens.** One ratio edit moves cosine similarity by less than $10^{-6}$ and capacity by \$200mm.
- **The docket is an append-only event log.** Use one global token bucket with $b + \rho h_0 \le L$. CourtListener's 125 requests a day means search and webhooks, not polling. Alert on silence.
- **Rule 2019 gives you quantities and dates, never prices.** Impute basis from the acquisition quarter, carry rounding as an interval, and remember that with turnout $\varphi$ a group blocks at $\theta > \varphi/3$.
- **Classifier error is an IC tax.** The tax rate is Youden's $J$ times a variance ratio, and at a 5% base rate half your flags are wrong. Span-cite everything.
**The Spec You Hand the Robot.**
```text
TASK: Covenant capacity + docket monitor for universe U (loans/bonds with EDGAR exhibits or open bankruptcy cases).
INPUTS: EDGAR exhibits EX-4.*, EX-10.* (versioned by accession, sha256); CourtListener v4 search/webhooks; RECAP Fetch
        (our PACER account); Rule 2019 statements; claims-transfer notices. All money in $mm, ratios in x, dates UTC.
STEP 1  Definitions -> graph. Case-sensitive, word-bounded, longest-match-first, span-consuming matcher; plurals.
        Tarjan SCCs; evaluate condensation in emission order; solve each cycle by fixed-point iteration; if the
        estimated Lipschitz constant >= 1, STOP and route to a human. Never guess a missing definition.
STEP 2  Baskets -> typed nodes {fixed, grower, ratio, builder, maintenance} with scope, netting flag, usage.
        Ratio with proceeds netting -> return inf and raise a red flag. Builder uses cumulative CNI (50% / -100%).
STEP 3  Entity graph -> max-flow Phi by commodity (IP, cash, other); report min-cut arcs and Phi/EV.
STEP 4  On each new version: dollar-weighted blast radius sum_u |K_u(v_k) - K_u(v_k-1)| / EV, signed per node.
STEP 5  Docket: classify entries (entry text + first page); state machine Quiet->Organized->Contested->Standstill->
        Plan->Confirmed; MLE q_ab = N_ab / T_a with censored spells. Rule 2019 -> panel of (holder, class, face,
        acq_quarter) with share intervals, flows, imputed basis, HHI lower bound, blocking flag theta > turnout/3.
  [...truncated]
### Exercises
### Deep-Dive Resource Graph

==== 26_ch26_ai_agents_and_llms_on_the_credit_desk.md (14,732 words)
# Chapter 26: AI Agents & LLMs on the Credit Desk
## 26.0 Cold Open: Section 6.08(b)(xiv)
## 26.1 What a Language Model Is, for a Specifier
### Reading is not using
### The stochastic reader, formally
## 26.2 Trend Watch: The Reading Machine Arrives on the Desk, 2022–2026
## 26.3 The Tool Stack: What Is Sold vs. What It Is
## 26.4 Document QA With Provenance: The Citation Contract
### The claim tuple
### What the evidence says about document QA in finance
### Calibration and selective prediction
## 26.5 Hallucination Is an Incentive Problem: Abstention, Controls, and the Cases Curve
### Why published hallucination rates are not comparable
### Controls, in order of leverage
## 26.6 Workflows First, Agents Last
### The arithmetic of chains
### The bill and the frontier
## 26.7 Agentic Alpha Research and the Multiple-Testing Explosion
## 26.8 Model Risk for Stochastic Readers: SR 11-7 Meets the LLM
## 26.9 The AI-Specifier's Operating Manual
## 26.10 Prompt Injection in the Data Room
## 26.11 Case Studies: Knight Capital, the Withdrawn Papers, and AI-Washing
## 26.12 The Harness in Code
### Specification for AI Implementation
## 26.13 Desk Debrief
- **A language model is a stochastic reader.** Validate it the way you validate a PD model (power, calibration, robustness, transparency). You cannot diagnose the model itself, so make every *claim* diagnosable.
- **The Loop Rule.** The model sits around the pricing loop, never in it. It emits typed features with provenance. It never emits a price, a spread, a hedge ratio, or a size.
- **A citation that cannot be checked is a hallucination with a footnote.** Tape this to the monitor: $\text{FH} = \frac1N\sum V(1-S)$. The section that does not exist is the error that embarrasses you. The real section that does not say what the claim says is the one that costs you money.
- **Abstain at $p^\ast = 1 - C_{\text{abs}}/C_{\text{FP}}$**, on calibrated confidence, enforced in code. Calibration can be repaired later and power cannot, so buy power.
- **Reliability multiplies.** Verifiers help through Bayes, and retries buy coverage with accuracy. Workflows first, agents last, and nothing autonomous between the model and a quote.
- **The agent's trials are your trials.** Deflate by the logged count, discarded ideas included, and purge by the generator's training cutoff.
- **Temperature zero is not a promise.** Log stochastic outputs as point-in-time data, and replay the deterministic half bit for bit.
- **Provenance proves the document said it, not that the document is honest.** Diff operative text deterministically, and give every tool the least privilege its job needs.
**The Spec You Hand the Robot.**
```text
ROLE: Build llm_desk_harness: an offline harness that scores a document reader against a
point-in-time store. Python 3, numpy/scipy/pandas only, seeded, no network calls.
UNITS: USD as float64 (never "mm"); percentages as decimals; PDF pages 1-based; offsets
[start, end) into the stored normalized text only.
CLAIM SCHEMA: question, fixed, pct, doc_id, page, start, end, conf in [0,1]. A claim with
no pointer is a FAILED claim (V=0), never neutral.
VERIFY (deterministic): V = pointer resolves; S = span passes support test vN (versioned);
A = matches label. Report acc, valid, support, FH = mean(V*(1-S)), ECE (10 bins), the
risk-coverage curve and AURC, every metric next to a deterministic regex baseline.
ABSTAIN: answer iff calibrated conf > p* = 1 - C_abs/C_FP. Costs are inputs, written down.
CALCULATORS: basket capacity = max(fixed, pct * max(EBITDA_as_reported, 0)); remaining =
max(capacity - used, 0); flag used > capacity. The model never computes these.
REPLAY: hash every deterministic output table; store each model output keyed by
sha256(prompt|model_id|params|timestamp); never re-run the model to check the past.
TESTS: >= 10,000 property draws (capacity >= fixed; non-decreasing in EBITDA; EBITDA <= 0
gives exactly fixed); golden fixture with a negative-EBITDA quarter; MC vs closed form
for the verifier posterior; pass^k unbiased estimator, NaN when k > n.
  [...truncated]
### Exercises
## 26.14 Sources and Links
### Deep-Dive Resource Graph

==== 27_ch27_system_architecture_and_asics.md (16,037 words)
# Chapter 27: System Construction, Low-Latency Infrastructure & ASICs/FPGAs
## 27.0 Cold Open: The Fastest Thing on the Desk
## 27.1 Two Clocks: Why Credit Latency Is Not Equity Latency
### 27.1.1 The price of a microsecond, derived
## 27.2 Ingestion: Feeds, Normalisation, and the Provenance Problem
### 27.2.1 The feed zoo
### 27.2.2 The provenance rule
### 27.2.3 Clocks, and the four timestamps of a fill
### Specification for AI Implementation
## 27.3 The Security Master Is the Credit Agreement of the System
### 27.3.1 What the master holds
### 27.3.2 The bitemporal model, derived
### 27.3.3 Case Study: Serta Simmons, 22 June 2020, as a sequence of master-table rows
### Specification for AI Implementation (bitemporal master)
## 27.4 Pricing, Risk, OMS/EMS, and the Order State Machine
### 27.4.1 The reference architecture
### 27.4.2 The order state machine
## 27.5 Latency Budgets Are Queues, Not Numbers
### 27.5.1 Little, Pollaczek–Khinchine, and the p99, derived
### 27.5.2 Two budgets on one desk
### 27.5.3 Case Study: CME Globex halts, 2019 and 2025, a budget with an infinite term
### Specification for AI Implementation (latency as a queue)
## 27.6 FPGA Trigger Tables for Quote-Pulling
### 27.6.1 The trigger table, derived
### 27.6.2 What a stale quote costs: diffusion versus tournament
### 27.6.3 Case Study: The 15 October 2014 Treasury flash rally, replayed against a trigger table
### Specification for AI Implementation (trigger tables)
## 27.7 Kill Switches as Stopping Rules
### 27.7.1 The hierarchy
### 27.7.2 CUSUM on markouts, derived
### 27.7.3 Case Study: Knight Capital (2012) and Citigroup (2022), mapped to tiers
### Specification for AI Implementation (kill switch)
## 27.8 Observability, Deployment, and Resilience Beyond Your Walls
## 27.9 Desk Debrief
- **Two clocks, one desk.** The quote clock runs in seconds to minutes; the hedge clock runs in microseconds. Speed is worth $\Delta\ell/T$ of your edge, so buy it in proportion to $1/T$ of the information you act on, not in proportion to how much you enjoy hardware.
- **The fastest thing on the desk is the thing that says no.** The fast path compares precomputed numbers and may only pull. Only the slow path, which can be audited, may say yes again.
- **Every price says what it is and when you knew it.** `price_kind` plus `known_at`, or it does not get a badge. Labels, fills and cost targets come from prints and firm quotes only.
- **The security master is the credit agreement of the system.** Use internal surrogate keys, bitemporal rows and append-only knowledge time. Serta's 22 June 2020 is a test case, not an anecdote.
- **The p99 is the number the sniper trades against, and it is worst when the market moves.** Little, Pollaczek–Khinchine and fan-out turn "40 ms" into "1.5 seconds on FOMC day, and 78% of PTs slow."
- **The cheap trigger rule is safe by the triangle inequality, and it costs false pulls in a flight to quality.** Store dollar sensitivities, budget the threshold, and set a guard band above fixed-point and convexity error.
- **A kill switch is a stopping rule with two numbers attached.** The desk head picks the false-alarm interval, and the detection delay comes with it, growing only with its log. Anyone can trip, two humans re-arm, and nothing can be clicked past.
- **Silence is not safety.** A dead hedge feed, a missing eighth server or a counterparty in manual settlement is a Tier-2 event with a named owner and a five-second deadline.
### The Spec You Hand the Robot
```text
SYSTEM: two-clock quoting engine for a systematic credit desk. Implement exactly this; ask before guessing.
1. PRICE STORE. Every record: instrument_key (internal surrogate), value, price_type in {PRICE, SPREAD, YIELD},
   side, size_mm (USD mm par; flag TRACE-capped), price_kind in {TRADED, FIRM_QUOTE, INDICATIVE_RUN, EVALUATED,
   COMPOSITE}, source, event_ns, known_ns. Only TRADED and FIRM_QUOTE may be labels, fills or cost targets.
   Late records go to a correction stream; never overwrite. TRACE affiliate duplicates are MARKED, never deleted;
   tag regime {no_flag, flag_voluntary (from 2026-08-31), flag_mandatory (from 2027-08-02)}.
2. SECURITY MASTER. Bitemporal facts (key, attr, value, valid [from, to), known [from, to)); knowledge time
   non-decreasing; exclusion constraint per (key, attr). Backtests query as_of(valid <= t, known = t) only.
   Test: Serta 2016 first-lien loan as of 2020-06-23 known 2020-06-22 00:00 returns first_lien_pari.
3. LATENCY. Measure sojourn (arrival to response), not service time. Report p50/p99/p99.9 by utilisation band.
   Alert when the p99 at current load exceeds the trigger-table refresh budget.
4. TRIGGER TABLE (fast path). Per exposed quote i: side, hedge reference prices H_ref[j], beta[i,j] in bond points
  [...truncated]
### Exercises
## 27.10 Sources and Links
### Deep-Dive Resource Graph

==== 28_ch28_pm_playbook.md (17,621 words)
# Chapter 28: What a Desk Head / Senior PM Must Know to Extract Maximum Alpha
## 28.0 Cold Open: The Keys to the Table
## 28.1 Risk, Not Capital: The Desk Head's Accounting Identity
### The identity, and why credit needs three substitutions
## 28.2 Effective Breadth When Issuers Cluster
### The Fundamental Law in hit-rate form
### Two definitions of effective breadth
### How noisy is your hit rate?
### Concentration is not rewarded in debt
### Specification for AI Implementation (Block 1): Effective Breadth and the Hit-Rate Law
## 28.3 Allocation Across Signal Horizons
### The break-even half-life
### The horizon ladder
### Specification for AI Implementation (Block 2): The Horizon Ladder
## 28.4 Kelly With Jump-to-Default
### Discrete Kelly for a bond
### Continuous time, and the jump
### Fractional Kelly is full Kelly for people with standard errors
### Which measure, and which loss
### Many names, one recession
### Case Study: The 2026 CCC Decompression
### Specification for AI Implementation (Block 3): Kelly With Jumps
## 28.5 LVaR, Days-to-Liquidate and the 5× Problem
### From Bangia's LVaR to a credit LVaR
### Days-to-liquidate, and the regulatory clocks
### Case Study: Third Avenue Focused Credit Fund, December 2015
### Specification for AI Implementation (Block 4): LVaR, Days-to-Liquidate and Runway
## 28.6 Drawdown Control: The Two-Threshold Rule, the PM Option and Marking to Bid
### Setting the stop with drift
### The stop-loss you don't know you have
### Case Study: March 2020 and March 2026
### Specification for AI Implementation (Block 5): Stops, Hitting Probabilities and the Mark-to-Bid Shock
## 28.7 The Leverage Band and the κ Problem
### Specification for AI Implementation (Block 6): The Leverage Band
## 28.8 Running Ex-RSSG Analysts Alongside PhDs
### Case Study: Aligned Signals, and the Hybrid Shop
## 28.9 The PM Dashboard: The 13-Week Model, Reborn
### Specification for AI Implementation: `pm_playbook_engine`
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
  [...truncated]
### Exercises
## 28.11 Sources and Links
### Deep-Dive Resource Graph
