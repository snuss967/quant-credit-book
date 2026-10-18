
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
### The Spec You Hand the Robot
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
### The Spec You Hand the Robot
### Exercises
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
### The Spec You Hand the Robot
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
### Exercises
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
### The Spec You Hand the Robot
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
### The Spec You Hand the Robot
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
### The Spec You Hand the Robot
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
### The Spec You Hand the Robot
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
### The Spec You Hand the Robot
### Exercises
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
### Exercises
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
### The Spec You Hand the Robot
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
### The Spec You Hand the Robot
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
### The Spec You Hand the Robot
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
### The Spec You Hand the Robot
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
### The Spec You Hand the Robot
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
### Exercises
## 28.11 Sources and Links
### Deep-Dive Resource Graph
