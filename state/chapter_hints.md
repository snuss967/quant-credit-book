# Chapter Hints: Seed Dissection Notes for Advisors and Writers

These are starting points, not ceilings. Advisors should research past them. "CHECK" means verify before stating as fact.

## Ch 1 — Anthology & Landscape
Keep the seed's §1.1–1.2 and expand from §1.3. Build the anthology from the shelf's load-bearing beams: DTS and spread-vol proportionality (Ben Dor), EDF and distance-to-default (Bohn & Stein), factor credit (Dynkin; Man 2022), intensity models (Schmid), threshold models (Bolder), distressed process (Moyer), 363 sales (Houlihan Lokey), and portfolio process (Paleologo). Quote each briefly and annotate it deeply. Map the ecosystem as a forced-seller flow graph: CLO CCC buckets and OC tests, ratings-constrained insurers, ETF redemptions, mutual-fund outflows, and which archetype harvests each flow. The fair-value-minus-skew-minus-toxicity bid equation in §1.1 deserves a proper derivation.

## Ch 2 — The Revolutions in Credit Trading (trend)
Man Institute 2023 is the spine. The timeline runs from TRACE 2002 through MarketAxess Open Trading, Tradeweb, Trumid, all-to-all, auto-execution of small RFQs, portfolio trading (from ~2018–19), ETF growth and ETF-as-price-discovery, non-bank liquidity providers, and electronic share of IG and HY volume by year (CHECK figures, Coalition/Greenwich/MarketAxess data). Close on why electronification creates the data exhaust that makes systematic credit possible.

## Ch 3 — Cognitive Rewiring (RSSG → desk)
Cover Glosten–Milgrom adapted to RFQs: a posterior on an informed counterparty given RFQ features (size, timing vs. 8-K and earnings, counterparty type, number of dealers queried, past markouts). Markouts are the empirical toxicity test. Show a Bayesian PD update from an 8-K. Build the "RSSG Edge Ledger": each skill (basket reading, ad hoc group dynamics, 13-week cash flow, DIP sizing) mapped to a codable feature, a data source, and a decay horizon. Show how pre-LMT flow patterns look.

## Ch 4 — Inside the Systematic Credit Industry (frameworks)
Compare the five shelf papers (Man 2022 and 2023, Nuveen, Blackstone BCBS, BlackRock HY) along these axes: alpha families, data stack, portfolio construction, execution, capacity, and risk. Add AQR, Robeco, Invesco, PIMCO, Insight, and others from research (CHECK AUM and launch dates). The comparative map defines the book's exploratory space. Include industry growth and AUM trends.

## Ch 5 — Probability Distributions
Bond return as a mixture (survival with spread move, or default jumping to recovery) with closed-form moments. Capped upside (call price, negative convexity) vs. a floor at recovery. Of Merton jump-diffusion, VG, and NIG, separate what's useful on a desk from what's decoration. Recovery as a Beta distribution: method of moments by seniority, a Beta-regression mean conditioned on collateral coverage, zero- and one-inflated mass, and Altman's downturn PD–LGD correlation. "40% recovery" is a CDS convention, not a fact. Tails via the Hill estimator and EVT. Keep price, spread, and return distributions apart, and keep $\mathbb{P}$ and $\mathbb{Q}$ recovery apart.

## Ch 6 — Merton & Intensity Models
Itô's lemma intuition (the ½σ² "volatility tax"), GBM, then Merton 1974: equity = call; debt = riskless bond − put. Spread: $s(T) = -\frac{1}{T}\ln\left(N(d_2) + \frac{V_0 e^{rT}}{F}N(-d_1)\right)$ (verify signs). Short-end spreads go to zero. KMV solves for $(V,\sigma_V)$ from $(E,\sigma_E)$. Black–Cox first passage via the reflection principle, with covenant barriers. Cox processes, with the RMV, RFV, and RT recovery conventions; RMV gives the discount rate $r + \lambda L$. CIR intensity in affine closed form. The credit triangle $s \approx \lambda(1-R)$. Piecewise-constant hazard bootstrap from CDS. Traps: mixing ℙ and ℚ, unannualized σ_E, equity vol used as asset vol, and Monte Carlo barrier discretization bias (Brownian-bridge correction).

## Ch 7 — ML on Small-Sample Credit Data
Why credit is the worst ML dataset: stale TRACE marks, survivorship (calls, LMT exchanges), many bonds per issuer ("47 bonds from one issuer are one data point wearing 47 hats"), regime changes, and ratings and fundamentals lags. Fractional differentiation (FFD weights $w_k=-w_{k-1}\frac{d-k+1}{k}$), triple-barrier labels in spread space scaled by DTS vol, meta-labeling, purged K-fold with embargo plus issuer-grouped purging, uniqueness weights, clustered feature importance, and the deflated Sharpe ratio and PBO. Cover the 2019–2026 frontier on ML for bond returns (e.g., Bianchi–Büchner–Tamoni; Kelly–Palhares–Pruitt; Dickerson–Mueller–Robotti replication; CHECK).

## Ch 8 — Isolating IDO & Empirical Duration
Return decomposition with the correct sign ($-D\,\Delta y$), OAS carry vs. yield carry, and key-rate-hedged excess returns. Why $D^{\text{emp}} < D^{\text{mod}}$ in HY and turns negative for CCC: spread–rate correlation (derive with $\rho$ and the vol ratio). Dimson and Scholes–Williams lag-sum betas for stale prices. DTS. The hedge matrix as constrained least squares across CDX HY/IG, UST futures (CTD DV01), HYG/JNK, and equity puts; ill-conditioning calls for ridge. Include the 2022 rates sell-off.

## Ch 9 — Factor Investing in Credit
Exact factor construction (Dynkin, Ben Dor, Man 2022, Houweling–van Zundert 2017, Israel–Palhares–Richardson 2018). Neutralize within rating × sector × maturity. DTS-neutral vs. market-value-neutral portfolios. Liquidity cost scores eat the alpha. Long-only constraints. The "informed investor" factor. Factor drawdowns in 2020 and 2022. Combining factors. The replication debate (CHECK). Use the IR numbers reported in Man 2022 (cite pages).

## Ch 10 — Trend & Time-Series Momentum in Credit (trend focus)
TSMOM on CDX/iTraxx and credit excess returns (Moskowitz–Ooi–Pedersen 2012 framework). Cross-asset trend: equity → credit lead–lag. Trend vs. cross-sectional momentum. Trend plus carry. Volatility scaling. Crisis alpha in 2008, 2020, and 2022 (CHECK). CTAs and managed futures in credit indices. Cover signal construction, turnover, and costs, and what trend does in the LMT era (jumps).

## Ch 11 — Defensive Systematic HY (BlackRock framework)
Default avoidance (distance-to-default, Altman Z, ML default models), downside capture, the CCC problem, quality and low-risk tilts, upside/downside capture math, capacity, and how systematic HY performed in 2022–2025 drawdowns (CHECK).

## Ch 12 — Multi-Asset Credit Allocation (Nuveen framework)
Cross-sector valuation (spread per unit of default loss and per unit of vol), regime models (HMM), risk parity vs. mean-variance across HY, loans, EMD, preferreds, securitized, and private credit, liquidity tiers, and allocation rules. Cite Nuveen's pages.

## Ch 13 — Codifying LMTs
Taxonomy: uptiers (Serta 2020, Boardriders, TriMark, Mitel, Incora/Wesco) and drop-downs (J.Crew, PetSmart/Chewy, Envision, Atos), plus double-dips (At Home) and pari-plus. The legal landscape: Fifth Circuit Serta (Dec 31, 2024), Mitel (NY App Div, 2024), Incora (Judge Isgur, 2024), and cooperation agreements and blockers (all CHECK). The Priming Risk Score as a hazard or logistic model on document features with Bayesian priors. Game theory: an n-player threshold game with a 2×2 payoff matrix and equilibria, and the sponsor auctioning between lender groups. A multi-obligor waterfall engine that conserves value.

## Ch 14 — Default & Recovery Cycle in the LMT Era (trend)
Distressed exchanges as a share of defaults (Moody's/S&P/Fitch data, CHECK), re-default rates after LMTs, recovery compression, cooperation-agreement proliferation, and 2024–2026 rulings. Model these as regime shifts in the PD and LGD distributions, linked to Ch 5 and Ch 13.

## Ch 15 — M&A & CoC
The 101 CoC put as an option conditional on deal × trigger: $\Pr(\text{deal})\Pr(\text{trigger}\mid\text{deal})\max(101-P_{\text{post}},0)$. Portability as a short option. Special mandatory redemptions. HSR and Second Request timelines as survival analysis (Kaplan–Meier, Cox PH). Target vs. acquirer spread compression. Cases: Broadcom–VMware, Kroger–Albertsons (blocked; SMR), Microsoft–Activision (CHECK).

## Ch 16 — Post-Reorg & Claims
Forced CLO selling and orphan-equity dynamics, with post-emergence return literature (CHECK). Rights offerings as an option plus backstop premium. Claims: 503(b)(9) vs. GUC, and pool-size uncertainty. Hertz 2020–21 (CHECK). Warrants as deep OTM calls.

## Ch 17 — Private Credit & Convergence (trend)
Market size and growth (CHECK), BDC marks vs. public comparables, private-to-public refinancings, private credit ratings, bank–private credit partnerships, secondaries, systematic approaches, and what a public quant desk can arbitrage.

## Ch 18 — Microstructure & Avellaneda–Stoikov
The AS 2008 derivation in full: HJB, exponential-utility ansatz, reservation price $r^{\text{res}} = s - q\gamma\sigma^2(T-t)$, spread $\gamma\sigma^2(T-t)+\frac{2}{\gamma}\ln(1+\gamma/k)$. GLFT 2013 with inventory bounds. Arrival intensity is $\Lambda(\delta)=Ae^{-k\delta}$, never $\lambda$. RFQ win probability is logistic in the distance to composite (CP+, Ai-Price, BVAL; CHECK names). Jump-to-default-adjusted reservation price: in the small-γ limit, the expected-loss term is $q\lambda J$. Roll, Glosten–Milgrom, and Kyle. TRACE rules (dissemination caps, D2D/D2C, ATS flags; CHECK). BWIC first-price common-value bid shading.

## Ch 19 — Portfolio Trading
PT price = Σ fair value − Σ liquidation cost − ½γ·(residual variance over the liquidation horizon). Include Almgren–Chriss unwind, covariance for stale bonds (factor model, Ledoit–Wolf), the eviction problem, stress liquidity commonality, the "mystery box" adverse selection, and engineering for 90 seconds. Include PT growth stats (CHECK).

## Ch 20 — Credit ETF Arb
AP mechanics, Rule 6c-11 custom baskets (2019, CHECK), bid-side NAV, arbitrage band edges from creation and redemption costs, March 2020 LQD/HYG discounts and the Fed SMCCF (CHECK dates and numbers), BKLN settlement mismatch, and ETF lead–lag as price discovery.

## Ch 21 — Loans & CLOs (trend)
Loan settlement (T+7 and beyond, CHECK), CLO tests (CCC bucket 7.5%, OC/IC), repricing waves, loan e-trading, CLO and loan ETFs (JAAA, BKLN, SRLN; CHECK AUM), and the CLO-driven demand curve.

## Ch 22 — Market-Structure Regulation (trend)
TRACE reporting-time changes (CHECK FINRA's 1-minute rule status), T+1 (May 28, 2024), Treasury clearing mandate dates (CHECK), Basel III endgame status, SEC dealer rule (vacated? CHECK), CDS security-based-swap reporting, and each one's effect on desk economics.

## Ch 23 — Cross-Asset Convexity & Vol
$\sigma_E E = \sigma_V V N(d_1)$, CreditGrades (2002), Carr–Wu 2011 puts vs. CDS, skew as jump-to-default, Natenberg-style Greeks expressed in spread terms, convertible arbitrage, cap-structure arbitrage in May 2005 (GM/Ford; Yu 2006), SVB 2023, and Hertz.

## Ch 24 — CDS Basis
CDS pricing (premium and protection legs, RPV01, 100/500 standard coupons plus upfront since 2009), basis definitions (Z-spread, PECS, ASW), negative basis funding, the CTD option, the two-stage auction, orphaned CDS, Hovnanian 2018, Windstream 2019, ISDA NTCE 2019, and DC rulings on LMTs (CHECK).

## Ch 25 — NLP for Credit Docs
The credit agreement as a definition graph (defined terms as nodes; cycles in Consolidated EBITDA). Pipeline: EDGAR (User-Agent and rate limits; EX-10 exhibits) → segmenter → definition extractor → basket normalizer for "greater of \$X and Y% of EBITDA" → LLM extraction with schema validation and citations → capacity calculator → PRS features. Also CourtListener v4 and RECAP, Rule 2019 parsing, claims registers, DIP roll-ups, and signal decay. Use synthetic agreement text only.

## Ch 26 — AI Agents & LLMs (trend)
LLM pricing and research products (CHECK vendors), agentic research workflows, evaluation and hallucination controls, document QA with citations, and the AI-specifier operating manual: specs, tests, deterministic replay, and why ROBO needs units and edge cases. Cover adoption trends from 2023 to 2026.

## Ch 27 — Systems & FPGAs
Honest latency economics: bond RFQs move in seconds, while hedges and quote-pulling move in microseconds. Cover the security master (LMT exchanges create new CUSIPs), pricing and risk engines, FIX, kill switches (Knight Capital 2012, CHECK), FPGA trigger tables ($\Delta P = -D\,\Delta y$ per bond with a threshold comparator), kernel bypass, and latency budgets as queueing.

## Ch 28 — PM Playbook
Paleologo is the spine. Allocation across horizons, $IR = IC\sqrt{BR}$ with effective breadth under issuer clustering, Kelly for a default bet with recovery and fractional Kelly under estimation error, days-to-liquidate and blocking positions, pod drawdown rules (CHECK; mark as commonly reported), LVaR, mark-to-bid, team design, and the PM dashboard.
