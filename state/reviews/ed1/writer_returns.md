# Edition 1 Writer Returns (consolidated for the Edition 2 planner)

Each Edition 1 writer handed back follow-up targets (cleanup, verification, trims) and new-TOC ideas. Source: workflow journals.

## Chapter 1
**New TOC ideas:**
- Trend Watch #4 or an exercise follow-up: the Serta/Mitel/Wesco split on 'open market purchase' as a binary document feature for the toxicity model (bridge from Ch 1 to Ch 3 and Ch 13)
**Next targets (verification, cleanup, trims):**
- Optional cleanup: §1.6 has no section-level Deep-Dive Resource Graph, which the brief asks for at the end of §1.3, §1.6 and §1.8; its sources are already listed in the chapter-end graph
- Optional trim: the chapter is about 13k words against the 8k-12k target; §1.4 (1,238 words) and §1.6 (1,373 words) are the easiest places to cut
- Cleanup pass: run the two Specification for AI Implementation code blocks (§1.3 reservation_bid, §1.8 ForcedSellerGraph) to confirm the asserts pass

## Chapter 2
**New TOC ideas:**
- §2.x 'What Electronic Means': fully electronic vs processed vs auto-executed vs duplicate prints, with a denominator table (Greenwich 48% vs MarketAxess ~60% vs Barclays >50%).
- §2.y '2026: Consolidation Year': ICE-MarketAxess deal (July 29, 2026), Tradeweb's lead, Trumid's growth, monthly MarketAxess data going dark.
- Ch 19-B: Protocol Selection, Smart Routing and Auto-Execution, extending the §2.5.1 odds-threshold router (J = pi*c + (1-pi)*kappa, leakage chi) to multi-protocol sequencing with stress-conditioned parameters.
- Ch 18 section: effective dealer count n_eff = n/(1+(n-1)phi) estimated from own RFQ logs; separate competition from composite herding using winner-vs-independent-fair-value rather than cover gap.
- Ch 22-B: The Reporting-Time Wars (SR-FINRA-2024-004 to RN 25-17) and print latency as a fast/slow mixture by bond type.
- Ch 10 bridge: data-exhaust theorem with crowding costs, c(TO)=c0+c1*TO, linking index-mark clustering to momentum capacity.
**Next targets (verification, cleanup, trims):**
- Run the four Python blocks in Chapter 2's Specification for AI Implementation (ch02_electronification_trend.py) in the cleanup pass. They were written to run but not executed under this run's no-code rule. The riskiest assert is check (b), curve_fit vs logit-OLS within 1e-6.
- Chapter is over its 8,000-12,000 target: 16,337 words by wc, about 14,850 excluding code. Candidates to trim in an edit pass: §2.5 automation statistics paragraph, §2.7 ETF background, §2.8 non-bank list.
- Verify CHECK items still in the text: Greenwich 2021-22 e-share chart readings; Man p.4 Fig. 4 PT protocol share 2021-22; Citadel Securities self-reported 14.2% IG block share; the HRT Bloomberg title (Dec 1, 2025).
- Verify podcast episodes (Bloomberg Odd Lots on portfolio trading, bond ETFs in March 2020, electronification) for Chapter 2 Resource Graphs; none are currently listed.
- Paleologo p.118 quote from the brief source map was NOT found in state/pdf_pages and was not used; re-locate it if Chapter 19 needs it.

## Chapter 3
**New TOC ideas:**
- Universe-level false-alarm control for pre-LMT CUSUM detectors: multiple testing across hundreds of tranches, compliance capacity as a constraint on the threshold (Ch 13/21 section)
- Cover-price counterfactuals: identifying the winner's-curse shading w(n) from platform cover reports, and why it is identified in one direction only (Ch 18 section)
- Counterparty 'axe honesty' score: shrunk rate at which shown axes are followed by opposite-direction trades, as an Edge Ledger feature (Ch 19/22 section)
**Next targets (verification, cleanup, trims):**
- Ch 18: RFQ response engine with Barzykin-Ciceri hit-ratio multiplier (Ch 3 spec defers to it)
- Edition 2 event study of loan prices/flow in the 60 days before announced uptiers (Ch 3 case study flags it as open)

## Chapter 4
**New TOC ideas:**
- Ch 4-B: The Genealogy of Quant Credit - a sourced talent-and-IP tree (KMV->DCI->Blackstone, BlueCove->Ares, Apollo->Man Numeric, AQR/BGI->Acadian, Robeco->Cubist) with dated public roles only
- Capacity disclosure and the fee stack: the one-third rule, the 9/4 A* zero-alpha size, and the T^-3 turnover scaling as an audit tool for manager capacity slides
- Bond choice within the issuer as a separate model: negative selection / cheapest-to-deliver-into-your-own-optimizer, built on a capital-structure model
- Point-in-time data engineering: knowledge-time joins, ex-post filter bias (truncated-mean derivation), and rerunning the factor zoo on the Open Source Bond Asset Pricing panel
- Default-screen economics: recall vs flag rate and the carry forgone on excluded non-defaulters (BlackRock 77% recall claim)
- Insurance balance sheets as the capacity sink: Solvency II/NAIC-aware optimizers as the commercial product of systematic credit
**Next targets (verification, cleanup, trims):**
- Verify BCBS 'over $40bn' as-of date and the Ares-BlueCove completion date (both marked CHECK)
- Verify Greenwich protocol-mix figure column order in Man_Revolutions_in_Credit_Trading_2023 p.4
- Cleanup pass: execute the four capacity_breadth_engine.py blocks and confirm all asserts pass
- Optional trim: chapter is ~14.4k words by wc (about 1.5k of that is code and URLs), above the 12k target

## Chapter 5
**New TOC ideas:**
- Ch 5-B: Stochastic Recovery: recovery locks, digital CDS, and the term structure of R under Q (Berd convexity premium, Pan-Singleton identification)
- Section in Ch 14: The default as a categorical variable (hard default vs distressed exchange) with a calibrated re-default hazard and regime-switching Beta recoveries
- Section in Ch 23: Calibrating VG/NIG jumps to CDX option skews and HY ETF daily returns, where infinite-activity Levy models earn their keep
- Section in Ch 6 or Ch 28: Finite-level exceedance vs limiting tail dependence; why a Gaussian copula's 99.9% chi-hat is not zero and how desks mis-verify tail independence
- Exercise-driven appendix: kurtosis constraints as an accidental mandate to own distressed paper (exkurt approx 1/q), with ES/JTD replacements
**Next targets (verification, cleanup, trims):**
- Cleanup pass: execute the five credit_mixture_lab.py blocks in §5.9 (not run this session, per budget) and confirm the seeded asserts, especially the Beta-regression 4-SE recovery test, the GPD VaR/ES tolerances on t(3), and the t-copula chi-hat at 0.999
- Length trim: the chapter is 18.2k words against the 8-12k target. The previous passes (§5.1-5.7) were already 11.5k, and the §5.9 code is word-dense. Consider moving §5.9 blocks 4-5 to a companion appendix
- §5.4 has no Deep-Dive Resource Graph of its own; add one in a later edition
- Confirm the First Brands Group 2025 facts (brief §7.3, all CHECK) before any later edition uses it as a left-tail case study

## Chapter 6
**New TOC ideas:**
- Ch 6-B: Incomplete Information and the Structural-Reduced-Form Ladder (Duffie-Lando, Giesecke, CreditGrades; choosing the model by horizon and data quality)
- Banks Are Not Merton Firms: Nagel-Purnanandam concave assets, state-dependent sigma_V, deposit-run jumps (SVB, First Republic, Credit Suisse 2023)
- The Barrier Is Negotiable: multi-tranche first passage with priority ladders, uptier as strike shift, re-default hazard after an LME (for Ch 13/14)
- Structural Models Without Equity: peer-equity sigma_V transfer, intensities fitted to loan marks, opacity as a hazard covariate (First Brands; for Ch 17)
- Affine Jump-Diffusion Intensities and the Jump Risk Premium (Duffie-Pan-Singleton; Bai-Goldstein-Yang; JTD for Ch 18)
- Hazard Curve Trading: inverted curves, negative-hazard arbitrage, standard-coupon upfront mechanics, ISDA curve migration (bridge to Ch 24)
- DD Momentum and lambda_Q/lambda_P as trend and value signals (for Ch 10)
- Appendix: verified table of ISDA CDS Standard Model conventions (coupons, recovery by seniority/region, IMM dates, day counts, curve sources)
**Next targets (verification, cleanup, trims):**
- Verify S&P Global Ratings Feb 20, 2025 distressed-exchange share (~two-thirds of Q4 2024 defaults) against the primary report and remove the hedge
- Verify S&P Global Market Intelligence Market Signal PD figures for SVB (Sept 2022 1.1%->2.5%, 6% peak Dec 6, 2022) against the primary blog
- Cleanup pass: execute the six cumulative Python blocks in section 6.11 (checks A-L) and fix anything that fails; code was written carefully but not run, per budget instruction
- Optional trim: chapter is about 16.2k words by wc -w (heavily inflated by LaTeX and roughly 2.8k words of code); prose could be tightened toward the 10k target in an editing pass
- Confirm Carvana new secured notes' PIK terms and the Serta bankruptcy-court 2023 ruling date against primary filings

## Chapter 7
**New TOC ideas:**
- Chapter 7-B: The Corporate Bond Data Pipeline, Tick to Panel (TRACE Enhanced/144A/FISD merge, Dick-Nielsen filters, decimal-shift and bounce-back correctors, month-begin returns as a desk standard)
- Section: Survival-analysis labels for bonds, with calls, tenders, exchanges and defaults as competing risks
- Section: LLM-derived features and training-cutoff leakage (purging must extend to the feature generator's knowledge cutoff)
- Section: Bayesian hierarchical shrinkage for the 108-signal bond zoo, reporting posterior alphas instead of t-stats
- Section: AI pricing composites as both the return denominator and the adverse-selection counterparty (correlated-noise gap bias, Exercise 7.5)
**Next targets (verification, cleanup, trims):**
- Cleanup pass: run the six cumulative python blocks in 7.12 once; the block-6 DSR assert (dsr < 0.95) is looser than the brief's DSR < 0.10 target, and the ROBO cold-open line says DSR 0.48
- Chapter is ~17.2k words, above the 8-12k target; an editor could trim sections 7.1-7.9 by ~20% without losing an anatomy element
- Verify PyBondLab PyPI page and a Bloomberg Odd Lots episode on credit market structure to add as links in the Resource Graph
- Check the Dick-Nielsen et al. '23% of factors' figure and Feng et al. Sharpe (gross vs net) flagged CHECK in the brief before quoting them in later chapters (Ch 9-10)

## Chapter 8
**New TOC ideas:**
- Ch 8-B: Credit index futures and the duration-hedged index family (CME June 2024 IG/HY/duration-hedged contracts, HYGH, methodology hedge ratios, effect on hedge-matrix conditioning and ETF arb)
- Section: CCC decompression as a regime, 2024-2026 (CCC/BB OAS ratio 4.0x to 6.5x; CCC beta on HY falling to 0.45; DTS assumption weakening in the CCC tier)
- Section: Classifying the source of rate moves (growth vs inflation vs flight-to-quality) to condition the empirical hedge ratio; HMM/logistic state model linked to Ch 10 and Ch 12
- Section: Stale-price artefacts in daily HY OAS (same-day over-tightening and next-day reversal in price-quoted markets) as a designed non-synchronous-close problem across futures, bond evaluations, equities and CDX marks
- App B addendum: building a TRACE-based OAS and excess-return history now that FRED's ICE BofA series are limited to three years (from April 2026)
- Ch 13/14 link: does a bond's rate hedge ratio collapse before a priming or uptier announcement (Alltel event-study logic as a PRS early-warning feature)
**Next targets (verification, cleanup, trims):**
- Cleanup pass: run the cumulative Python in section 8.9 (ido_engine) and fix any failing sanity checks; it was written to run but never executed
- Length check: wc counts the chapter at 18,222 words including code, tables and LaTeX, above the 7,000-10,000 target; an editor may want to trim the per-section resource graphs or the April 2025 table
- Verify the CHECK-flagged figures, which the text labels approx.: 2022 Bloomberg HY (-11.2%), IG (-15.8%) and Treasury (-12.5%) returns, the 2022 HY OAS path, and the Morningstar stock-bond correlation of about 0.58
- Verify the Treasury futures settlement time and CDX end-of-day mark timing used in the non-synchronous-close paragraph of section 8.6, which the text hedges as approx.

## Chapter 9
**New TOC ideas:**
- Ch 9-B: The Bond Data Problem: a TRACE cleaning pipeline, separate sources for signal and return prices, and an OBAP replication CI harness
- Section: carry per unit of DTS equals 1/D, so carry and low-risk are one factor in DTS space; test it on OBAP data
- Section: crowding measures for credit factors (holdings overlap, factor valuation spread inside DTS cells, short interest on the short leg), plus a written-in-advance autopsy template for a credit quant quake
- Section: the cost of leverage in DTS-neutral low-risk books, and BAB-style funding drawdowns in credit
- Section: document-risk as a cross-sectional factor, testing whether the Ch 13 PRS is spanned by value and quality
**Next targets (verification, cleanup, trims):**
- Cleanup pass: run the seven cumulative Python blocks in section 9.11 once and tune any PASS/WARN soft checks; the hard asserts were designed with wide margins but have not been executed
- Prose trim: wc total is about 17.4k including code and LaTeX, above the 7k-10k from-scratch target; sections 9.3 and 9.6 are the best candidates for tightening
- Verify the March 2020 IG and HY spread peak levels (currently marked approximate) against ICE BofA OAS series on FRED
- Chapter 10 cross-reference: time-series trend vs cross-sectional EMC is flagged in section 9.4
- Chapter 13 hook: Priming Risk Score as an ESP regressor is planted in sections 9.3.4, 9.11 (hidden-risk DGP), and the Desk Debrief

## Chapter 10
**New TOC ideas:**
- Ch 10-B: Credit index microstructure for systematic traders (roll-adjusted return series, roll windows carrying 25-50% of quarterly notional, series basis, dealer price discrimination per Collin-Dufresne-Junge-Trolle)
- Speed as a regime variable: multi-speed trend ensembles in CDX with explicit cost curves (fast trend uneconomic in cash, affordable in index)
- Trend convexity via payer swaptions: break-even vol vs trend lag (whipsaw capture (T-4L)/T)
- Stale-mark lead-lag artifact p(1-p)beta: a TRACE print-frequency audit of equity-to-bond lead-lag results
- Single-name trend with jump-aware sizing: lambda_J mapped from the Priming Risk Score; decoupling flag that switches names to the event engine
- Rating momentum as a trend in default intensity (Schmid non-Markov transitions; Lee-Naranjo-Sirmans slow-moving ratings)
- Listed credit futures (Cboe iBoxx IBHY/IBIG, CME) as the CTA route into credit beta: block-trade growth 2024-2026
**Next targets (verification, cleanup, trims):**
- Run the six python blocks in a cleanup pass (they were written once and never executed, as instructed); the asserts most likely to need tuning are block 3 (Sharpe gap of at least 0.3) and block 4 (realized vol within 25% of target)
- Verify HY OAS peaks for 2008, March 2020 and July 2022 against the full ICE history; these are marked approximate in 10.7
- Check the Top Traders Unplugged SG Trend figures for 2025 full year and 2026 YTD against SG Prime Services
- Optional length trim: wc counts about 17.6k words including about 4k of code and LaTeX tokens, above the 7k-10k target for a new chapter; tightening 10.6 to 10.8 would be the place to start

## Chapter 11
**New TOC ideas:**
- Ch 11-B: Default prediction in the LMT era: labeling soft defaults (DE, uptier, drop-down with guarantee release), the post-LME re-default hazard (Moody's 1,173-borrower study: >70% of hard re-defaults within two years), and PRS features as PD covariates
- Private-issuer PD coverage: bond-implied vs accounting-only PDs for sponsor-owned HY issuers with no listed equity, with model-regime flags as features; Trend Watch on private-credit defaults (Fitch 6% record, April 2026) spilling into public CCC
- The CCC tier as its own asset class: CLO 7.5% CCC-bucket and OC-test forced selling, CCC/HY OAS ratio as a regime indicator (2.6 in Jan 2025 to 4.0 in Oct 2026), PD-ranked selection inside CCC vs tier exclusion
- Convexity overlays instead of beta tilts: HYG/JNK puts and CDX HY payers to buy downside protection while holding beta at 1.0, cost vs forgone upside of a 0.9 beta (links Ch 20, Ch 23)
- Fallen angels and rising stars inside defensive HY: buying forced-sold low-PD fallen angels as defense plus offense, with capacity tables (Dynkin p.209)
- Default clustering and breadth: Vasicek/Basel asset correlation falling with PD (Bolder p.324) as the formal case for broad, small CCC positions; link to Ch 28 Kelly-with-JTD sizing
**Next targets (verification, cleanup, trims):**
- Cleanup pass: execute the six cumulative Python blocks in Ch 11 in order (Block 5 SLSQP feasibility under the 3% issuer cap and Block 3 OOS AUC > 0.75 are the asserts most worth confirming)
- Verify HY-specific ADV (about $14bn/day, labeled illustrative in 11.9) from SIFMA's downloadable corporate bond statistics
- Confirm exact 2022 and 2023 ICE BofA US HY calendar returns (the chapter uses BlackRock's 'down over 11%' / 'up over 13%')
- Confirm S&P figures (5.1% US spec-grade default rate, Dec 2024; about 68% distressed-exchange share of 2025 YTD defaults), currently labeled approximate
- Confirm which agency produced the 'distressed exchanges 94% of downgrades to D/SD' count reported by The DESK
- Optional trim: the chapter is about 15.7k words by wc (roughly 2.5k of that is code and LaTeX), above the 7k-10k target; 11.4 and 11.7 could each lose one source-extraction annotation if a later edition needs the space

## Chapter 12
**New TOC ideas:**
- Semi-liquid vehicles and the gate as a state variable: perpetual BDCs ($306bn gross), interval funds, the 5% NAV cap as a stochastic queue; Q1 2026 first net-outflow quarter (coordinate with Ch 17 and Ch 20)
- CLO tranche expected loss by waterfall simulation as a function of the CCC bucket and OC tests, replacing rating-table EL in MAC capital market assumptions (coordinate with Ch 21)
- EM sovereign restructurings as the RSSG sector: recovery-conditioned EL and ex-distressed index yields
- Preferreds and AT1: point-of-non-viability trigger as a jump-to-zero state; $25-par vs $1,000-par split
- Cross-sector style factors (carry, value as spread per expected loss, momentum, defensive) with the AQR R-squared result as the null
- Structural breaks in mean-reversion targets: composition-adjusted z-scores (HY 37% to 54% BB) linked to Ch 7 regime labels
**Next targets (verification, cleanup, trims):**
- Cleanup pass: execute the five cumulative python blocks in 12.10 (not run per budget instructions) and fix any assert or solver-tolerance failures
- Verify Nuveen Figure 3 label/value mapping against the chart image (text layer lists labels in reverse order; chapter states the economic reading and the ambiguity)
- Optional trim: chapter is ~15.7k words by wc (code and LaTeX included), above the 8-12k target

## Chapter 13
**New TOC ideas:**
- Ch 13-B: The LMT litigation map as a Markov model (announced, challenged, MTD denied, trial, reversed, settled, Ch 11), with forum- and doctrine-conditional q and the integration_gap feature
- Deals away and the six-month par call: price the sponsor's unwind option as the d_sp in Nash bargaining
- The double-dip in Chapter 11: a Trinseo 2026 full-cycle autopsy with the clearing engine, plus intercompany make-wholes and allowed-claim ranges
- Cooperation agreements as cartels: Shapley carve-outs, WBD-style anti-cartel covenants, and the Optimum/Selecta antitrust challenges
- Text-to-feature at scale: extract buyback_exception, sacred-rights scope and unsub capacity (as max-flow on the definitions graph) from EDGAR credit agreements by vintage
**Next targets (verification, cleanup, trims):**
- Cleanup pass: the chapter is 15,168 words by wc, over the 8,000-12,000 target. About 2,000 of those are Python and LaTeX tokens; if a trim is wanted, the cheapest cuts are the PetSmart paragraph in 13.6 and the 13.9 forum paragraph
- Execute and debug the three cumulative lmt_engine.py blocks in 13.8 (not run, per the budget rules). The asserts most likely to need tuning are the stochastic ones: bootstrap band, holdout Brier, and the 4-SE Monte Carlo checks
- Ch 14 should continue the cooperation-agreement counter from 2 (Ch 13 ends at 'Cooperation agreements signed in this book so far: 2. Antitrust complaints about them: 2')
- CHECK items still hedged in the text: the Incora trial and Crane reversal dates, Mitel deal amounts, the Lions Gate/Starz holding (Mar 17, 2026, not reviewed), and the ConvergeOne decision date

## Chapter 14
**New TOC ideas:**
- Ch 14-B: The Re-Default Clock - recurrent-event and mixture-cure hazards after LMTs, with a hand-built public LME-to-outcome dataset (2016-2026) calibrated to Moody's 1,173-borrower moments
- Ch 14-C: Co-Ops, Deals Away & the Antitrust Frontier - threshold/defection games, carve-out co-ops as mechanism design, Optimum v. Co-op Lenders and Sharon Steel
- Litigation claims as a recovery tranche: valuing excluded-lender claims after the Serta remand (award plus 9% NY interest as a dated contingent claim)
- Recovery-by-coalition dataset section: estimate (pi, mu_in, mu_out) by year and LME type for every LME since 2016
- Ch 24 section: DE is not a credit event - the North American No-R wedge between agency lambda_H+lambda_D and CDS-implied lambda_H
- Appendix D: LMT case docket and regime-switch calendar (ruling dates as time-varying transition inputs for the Hamilton filter)
**Next targets (verification, cleanup, trims):**
- Cleanup pass: execute the five lme_cycle_engine.py blocks in 14.7 in one interpreter and fix any failing asserts (code written to run but not executed, per budget rules)
- Verify the Fitch 2024-emergence first-lien recoveries (23% with prior LME vs 53% without; currently cited via PitchBook and hedged as indicative)
- Read the Del Monte first-day declaration and complaints (Bankr. D.N.J. 25-16984; adv. 26-01018; D.N.J. 3:26-cv-02379) before adding deal terms to Case Study 14.8.3
- Confirm the STG Logistics (N.Y. Sup. Ct.) ruling date and the Optimum antitrust complaint's filing date and docket number for the 14.6 Docket Diary
- Coordinate the cooperation-agreement counter with Ch 13 (Ch 14 sets it to 'one in Chapter 3, plus forty-five in 2024 alone' as an overflow joke)
- Optional trim: the chapter runs about 14.5k words including about 3.5k words of code, above the 7k-10k target; candidate cuts are the section-level resource graphs and the 14.8.1 timeline that overlaps Ch 13.3.1

## Chapter 15
**New TOC ideas:**
- Ch 15-B: Convertible fundamental-change puts and make-whole tables, with the 2025 U.S. Steel Share Exchange Event supplemental indenture as the worked example
- Defeasance and consent-strip counter-options as a game tree (EA 2026, WBD June 2025), possibly a Ch 13 subsection
- Non-HSR hazards (CFIUS/presidential, STB, state AGs, SAMR) as separate cause-specific baseline hazards
- IG LBO-risk factor: screen for low-coupon legacy notes plus weak defeasance protection and test for an event-risk premium in cross-sectional spreads (Ch 9 link)
- Event momentum in target bonds through silent regulatory milestones (Giglio-Shue in credit), Ch 10 link
- Ticking fees and reverse termination fees as contractual prices of time vs survival-implied carry
**Next targets (verification, cleanup, trims):**
- Cleanup pass: execute the chapter's four cumulative python blocks in one interpreter and fix any failures (block 4 Cox trust-exact convergence; block 3 PCHIP exactness assert)
- Verify CHECK items before Edition 2: whether each WBD series kept its CoC offer after the June 2025 strip; the EA indenture's covenant-defeasance article and the rating actions; HPE-Juniper closing date; the Tapestry PI date
- Trim pass: the chapter is about 14,000 words, above the 12,000 target; candidates are the 15.4 tranche table prose and the 15.5 HSR table
- Fix the Ben Dor citation span (pp.212-213) in the source map, and confirm Paleologo p.152 against the shelf

## Chapter 16
**New TOC ideas:**
- Over target: wc -w gives 18,566 words in total and about 16,000 outside the code blocks, against the 7,000-10,000 brief. A later edition can cut it by moving the five Python blocks into an appendix or companion repo.
- Ch 14/16 bridge: a runway-driven jump intensity, lambda_t = lambda_0*exp(-beta*L_t/B_t), fitted on Chapter 22 re-defaults (Spirit 2024-25). This is where Theo's 13-week model reappears as a hazard feature.
- Correction carried to other chapters: if the spot is a market price, jump-to-default enters a warrant or call price through r+lambda, not as an exp(-lambda*T) haircut. Any chapter that applies the haircut to a market spot should be fixed.
- Correction to brief 3.3: long 503(b)(9) / short GUC is LONG pool uncertainty near par, not short. Also, Jensen cuts both ways: variance raises expected recovery for deeply impaired classes, because 1/C is convex.
- Correction to brief 3.4: the Hertz warrant implied vol at the $13.80 basis is about 23-25%, not 26%. At the $10 spot it is in the low 50s.
- Possible Trend Watch for Edition 2: an exclusive-backstop legal-hazard index by circuit (Serta, ConvergeOne, LATAM), tracking any Fifth Circuit ruling on the ConvergeOne appeal. An October 2026 search found none.
**Next targets (verification, cleanup, trims):**
- Verify the dates and figures marked per-press-reports or CHECK before publication: Hertz June 2020 ATM sales (~$29mm), the June 2026 41% drop and its financing terms, the Oct 2026 Bloomberg Law adviser report, Spirit's filing, emergence and refiling dates and its $8.1bn/$8.6bn figures, and the FTX distribution amounts and class percentages.
- Run the five cumulative Python blocks in Chapter 16 in one interpreter during cleanup. They are written to run but have not been executed. The assert margins to watch are the 1-month markout (< -0.04, model gives -0.044) and the trough-to-1y markout (> 0.05, model gives 0.054).
- Confirm Dynkin p.158's reversal windows (+5.75%, +1.04%, +0.86%), which were taken from the brief and not re-checked on the shelf page.

## Chapter 17
**New TOC ideas:**
- Ch 17-B: Marking the Unmarked: BDC NAVs, listed discounts, the pending-mark/mark-gap signal and cross-holder mark dispersion
- Ch 17-C: Semi-Liquid Vehicles, Redemption Queues and Private-Credit Run Dynamics (TREND): belief-driven request fractions, backlog dynamics, reflexive sleeve haircuts
- Ch 22-B: Insurance Capital, Private Letter Ratings and the NAIC SVO as a forced-flow calendar
- Section in Ch 14: selective default in the bilateral market (bad PIK, A&E) as a hidden-default series
- Section in Ch 12: private credit in MAC optimizers: proxy bias (Nuveen LL B proxy), desmoothing and liquidity tiers
**Next targets (verification, cleanup, trims):**
- Cleanup pass: execute the five cumulative mark_gap Python blocks once (written to run on numpy/pandas; not executed per budget rules)
- Re-verify CHECK-flagged facts printed with hedges: Reuters/LSEG 0.74 median P/forward NAV, Barings 11.3% requests, Moody's OCIC outlook, CDX Financials constituents and private-credit weight, Finastra 'largest ever' and lender names
- Ch 21: consume Q^{P->B} takeout-supply output from block 3 in the CLO-demand/repricing models
- Ch 23: Merton-on-a-CLO extension of the BDC implied-markdown formula (risky BDC debt, Q-measure CDS link)
- Ch 25: SOI parser that feeds the soi table schema (ice_id join, PIK flags, stale-mark share)
- Appendix B: add Z.1 private credit series codes, Schedule TO/8-K redemption data, ICE IDs, Apollo daily prices, PRIV holdings

## Chapter 18
**New TOC ideas:**
- Block reservation pricing for RFQs of n lots: theta(q+n)-theta(q) with JTD convexity, size ladders, and why AS's one-lot quote under-prices blocks (bridge from Ch 18 to Ch 19 PT pricing)
- Event-calendar jump intensities: lambda^P as a Poisson process with an appointment book (earnings calls, lender calls, coupon dates) driven by the Priming Risk Score; a backtest of widening bids into scheduled events
- Street-inventory inference from composite-contributor skews and NY Fed primary-dealer positions as an RFQ-engine feature (net-short dealer regime and squeeze risk)
- BWIC leakage as an empirical research gap: estimating pre-auction drift and survivorship bias in CLO BWIC covers (Edition 2 target; no academic paper found)
**Next targets (verification, cleanup, trims):**
- Run the chapter's Python blocks in order during a cleanup pass (Roll, Kyle, AS, GLFT+JTD, win curve and hit ratio, TRACE decoder, BWIC); the asserts were checked by hand but never executed
- Check the CHECK-marked facts: the Altice France March 2024 price path (BNN Bloomberg), the SCI Feb 2026 $56bn BWIC headline period, and the Coalition Greenwich June 2024 no-touch shares
- Chapter is about 13.8k words by wc, of which about 3k is code; trim the prose if the build enforces the 10k cap

## Chapter 19
**New TOC ideas:**
- Revealed-preference calibration of dealer risk aversion gamma and margin pi from won/lost PT quotes (hit-rate inversion); capital-based gamma is ~30x too small to explain observed PT pricing
- Two-way (mixed buy/sell) baskets: netting of the rank-one liquidity spike (g'x)^2 as a quantitative reason dealers bid tighter for two-way PTs
- Exact Euler-vs-removal cost attribution for best-ex files: per-line Delta_j sums exceed total cost by the off-diagonal risk term; how to report per-line PT costs to compliance
- Staleness-as-variance: modelling evaluated-pricing error growth kappa*sigma^2*age for composite-anchored engines across ICE/BVAL/CP+/Ai-Price (composite reflexivity)
- MarketAxess vs Tradeweb PT platform-share war 2024-2026 (MKTX estimated US credit PT share 13% in 2024 to ~21-22% in 2026)
**Next targets (verification, cleanup, trims):**
- Ch 20 credit ETF creation/redemption: link custom-basket loss (Man p.3) and Koont et al. basket tilts to the PT residue outlet
- Ch 22: reconcile the two 2025 'record day' volume definitions ($89.7bn 2025-04-08 vs $84.7bn 2025-09-30) referenced in Ch 19 TW1
- Cleanup pass: execute the Ch 19 cumulative python blocks (eviction asserts ev==[41] and [116,41], stress >2x, latency <1s) and adjust if any illustrative calibration misses
- Optional trim of Ch 19 toward 10-12k words if the editor enforces length (19.3-19.5 prose is the longest)

## Chapter 20
**New TOC ideas:**
- Ch 20-B: The Basket Triangle - arbitrage bands linking ETF creation/redemption, portfolio trades and credit index futures (IBHY/IBIG), with custom-basket availability as a state variable
- ETF share classes of bond mutual funds (post-2025 DFA relief): in-kind redemption through the ETF class as the exit door for 1940 Act bond money
- Evaluated-price forecasting: using ETF premia and the NAV catch-up regression to predict next-day pricing-service marks for collateral, NAV and risk-limit users
- Private-credit and loan wrappers (PRIV, BKLN) under Rule 22e-4: settlement-lag liquidity runway models and contractual liquidity providers
**Next targets (verification, cleanup, trims):**
- Verify the bid-side NAV convention in the HYG/LQD/JNK prospectuses or SAIs (currently sourced to Vanguard/Morningstar/etf.com commentary)
- Confirm BKLN's AUM against Invesco, check whether it creates/redeems in cash, find its March 2020 discount, and confirm its current liquidity sleeve and credit line
- Confirm HYG's 2020 peak AUM, the exact Rule 6c-11 custom-basket exemptive-order cutoff, and the PRIV SEC letter date and response
- Confirm 2026 bond ETF AUM and flow figures against State Street's own releases (Advisor Perspectives/SSGA figures are search-listed)
- Cleanup pass: run the six cumulative Python blocks in section 20.7 (SLSQP convergence and the asserts in Blocks 2-4 are the riskiest); trim prose toward 10-11k words if the editor wants it

## Chapter 21
**New TOC ideas:**
- Ch 21-B 'The CLO as a Rule-Bound Buyer: CCC Haircuts, OC Tests & Forced-Flow Alpha': expand the cure-trade theorem (21.6), the FSPI calibration on trustee data, and a Kundu-style IV event study into a full chapter.
- Section in Ch 22 'Loans Are Not Securities': Kirschner (2d Cir. 2023), why loan settlement stays near T+20, NAIC YE2026 CLO C-1 factors with the thin-tranche surcharge, and quarterly N-PORT from 2027.
- Section in Ch 20 'From BKLN to JAAA: the CLO ETF stack': reset-heavy ETF holdings as a bid for CLO resets, plus the 2-8 week wrapper-to-loan-bid lead-lag hypothesis.
- Appendix C dated rows: Octaura share milestones (1% Apr 2024 to about 7.5% H1 2026), the Jan 2025 and Jan 2026 repricing bursts and the Feb-Apr 2026 freeze, JAAA passing \$30bn (13 Aug 2026), Versana digital voting (Oct 2026).
**Next targets (verification, cleanup, trims):**
- Chapter is over its 7,000-10,000 word target: about 16.3k words by wc, of which roughly 3k are the five Python blocks. A trim pass could cut 21.2.3 and 21.6 prose by 15-20% without losing anatomy elements.
- Execute the five Python blocks in order in one interpreter during cleanup. They are written to run but were not executed. Highest-risk asserts: the Block 1 cure-theorem bounds, the Block 4 MC-vs-analytic 8% tolerance, and the Block 5 desmoothing tolerances.
- Resolve the CHECK items before print: the LSTA '10-year average 20 days' settlement slide, the Beyhaghi-Ehsani sample period, the S&P 2023 and 2025 CLO vintage cushion figures, the Octus MM-CLO software >30% figure, whether the SEC withdrew S7-26-22 in 2025, and the volume/pages for Cordell-Roberts-Schwert.
- Confirm with the Ch 13/14 writers that the Serta Docket Diary facts match: June 2020 uptier, LCM XXII Ltd. v. Serta (S.D.N.Y.), January 2023 chapter 11 filing in S.D. Tex., and the Fifth Circuit's 31 Dec 2024 'open market purchase' holding.
- Ch 20 cross-reference: §21.6 calls the March 2020 loan-ETF discount partly a settlement event and derives the AP arbitrage band d* = f*l/360 + min(c/2, z*sigma*sqrt(l/252)). Ch 20 should match or cite it.

## Chapter 22
**New TOC ideas:**
- Ch 22-B: The customer's regulator: Solvency II, NAIC RBC/SVO, and CLO CCC buckets as forced-flow generators (Blackstone p.2, Nuveen p.5 hooks)
- Appendix C: dated regulatory regime table (TRACE, T+1, clearing, capital, SBSR) with placebo dates such as the 2025-12-04 one-minute-rule abandonment
- Box series 'Rules as Prices': one-line rent, delay-option, and netting-factor calculators reused across Part V
- Edition 2 section: non-bank liquidity providers after the dealer-rule vacatur, comparing their gamma/k with bank dealers' and the capital-free quote
**Next targets (verification, cleanup, trims):**
- Cleanup pass: run the six cumulative python blocks in one interpreter (reg carry, TRACE regime layer, settlement clock, netting/capacity, event-study DiD) and fix any assert drift; asserts were hand-computed, not executed
- Verify CHECK items before print: SEC approval date of SR-FINRA-2024-004 (autumn 2024); CME (Dec 2025) and ICE (early 2026) Treasury clearing approvals; primary dealers net short ~$4bn corporates in 2026 vs NY Fed FR 2004 data; SBSR public dissemination start 2022-02-14; dealer-rule vacatur 2024-11-21 and appeal dismissal; 2024-03-25 Treasury end-of-day TRACE dissemination; EU/UK T+1 2027-10-11; Ediphy CTP 2025-07-03; UK bond regime 2025-12-01
- Find the working URL for SEC press release 2025-43 (Treasury clearing extension); the guessed URL returned 404, so it is cited by title only
- Chapter length is ~16.0k by wc (about 14k words of prose outside code), over the 7-10k target but in line with other chapters (16-18k); trim 22.3 or 22.7 if the editor enforces the target
- Wire REGIME_DATES from 22.2 into Appendix C timeline and Chapters 19, 20, 24 feature pipelines as the single source of regulatory structural breaks

## Chapter 23
**New TOC ideas:**
- Bank liquidity-runway default models: deposit-run intensity, uninsured share, HTM losses vs CET1 as a standalone section (SVB/First Republic)
- Credit VIX and CDX swaption implied vol vs single-name equity implied vol: vol-vs-vol cross-asset relative value
- Contractual waterfall inversions: AT1/CoCo write-down triggers and point-of-non-viability as a regulator-set strike
- Convertible supply from AI capex as a driver of single-name equity vol surfaces
- Measuring CreditGrades time-shift approximation error vs the true random-barrier model
**Next targets (verification, cleanup, trims):**
- 24_ch24 (CDS curve bootstrapping / CTD, referenced by 23.3 for hazard curves and recovery mismatch)
- Cleanup pass: execute the five cumulative Python blocks in Ch 23 and confirm all asserts PASS (MC check at 4 SE, backtest Sharpe ordering across phi)
- Verify secondary-sourced figures marked approx. in Ch 23: SVB holdco note price path (TRACE), Hertz $239mm cash to old equity, Wolfspeed final plan terms, 2026 US convert issuance $131bn, single-name CDS ~6% of cleared index notional
- Confirm Kiesel & Veraart (Journal of Credit Risk) citation on the CreditGrades closed-form error

## Chapter 24
**New TOC ideas:**
- CDS auction event-trading chapter: forecasting open interest from positioning and deliverable supply, then trading the post-auction bond bounce (Chernov-Gorbenko-Makarov, Du-Zhu)
- Successor and orphaning engine for LMEs: how drop-downs, exchanges and par refinancings move CDS (New Fortress 2024-25, DISH DBS 2026, Discovery Global Holdings 2026), linked to Ch13 PRS
- Net-short debt activism and 'net short lender' provisions: Windstream to the 2026 loan-document market, written as an NLP feature for Ch25
- Determinations Committee governance and the 300/5 no-auction outcome (Altice France Holding 2025) as a liquidity risk for single-name hedges
- Funding-regime-aware basis model: repo haircut processes, SOFR OIS vs. repo spread, and the March 2020 Fed-facility natural experiment
**Next targets (verification, cleanup, trims):**
- Cleanup pass: run all seven cumulative Python blocks in one interpreter and confirm every assert (auction IMM 26.875, CTD prices 95.95/50.63, OU parameter recovery, PECS round trip)
- Verify the Windstream 18 Mar 2019 auction final price of 29.5 from a primary source (Creditix/DC results page); currently secondary via Creditflux
- Check the SNAC deliverable obligation characteristics list (Not Subordinated, Specified Currency, Not Contingent, Assignable Loan, Consent Required Loan, Transferable, Max Maturity 30y, Not Bearer) against the 2014 Definitions / Physical Settlement Matrix
- Upgrade secondary figures to primary: Risk.net March 2020 basis (-401 HY / -186 IG), Bai & Collin-Dufresne 2008 magnitudes, ICE Clear Credit 2025 \$2.57tn, NTCE Credit Deterioration Requirement wording from the ISDA supplement
- Optional trim: chapter is about 13,900 words of prose plus 2,170 words of code, above the 7,000-10,000 target; candidates are the Trend Watch boxes in 24.4 and 24.8 and the 24.7 literature paragraph

## Chapter 25
**New TOC ideas:**
- Covenant capacity as a multi-commodity flow LP with shared basket capacities (IP vs cash vs other assets), extending 25.4's single-commodity max-flow
- Docket state-machine hazard models across a panel of Chapter 11 cases (Organized -> Contested -> Standstill) as an event-driven return predictor, building on Huang, Lewellen & Wang
- Claims-agent portal adapters and the Rule 3001(e) transfer feed as a distressed trade-claim flow dataset
- EBITDA-definition permissiveness as a time series: replicate Badawi et al. with LLM span extraction on post-2018 agreements
- Price imputation for Rule 2019 holdings: cost-basis reconstruction from acquisition quarters plus TRACE/LSTA marks, and its link to plan-negotiation behavior
**Next targets (verification, cleanup, trims):**
- Verify Huang, Lewellen & Wang (SSRN 4854111) sample size, years and bp magnitudes from the paper's tables
- Fetch the Windstream Doc. 245 opinion text to replace the press-statement characterization of the holdings with short verbatim quotes
- Confirm the full-year 2025 PitchBook|LCD cov-lite share for the 25.3 Trend Watch
- Fix EDGAR FTS NEAR() operator encoding and rerun the blocker-proxy counts
- Cleanup pass: execute the eight cumulative Python blocks in 25.10 (written to run; not executed per budget). Optionally trim prose about 10% toward the 10k target

## Chapter 26
**New TOC ideas:**
- Ch 26-B: The Reading Machine's Data Room: prompt injection in PDFs, retrieval sanitization, point-in-time evidence libraries
- New §7.x: Agentic research and the multiple-testing explosion (DSR with machine-generated N, knowledge-cutoff purging of feature generators, pre-registered agent search spaces)
- New §11.x: Tabular foundation models for PD/LGD on low-default portfolios (Baesens et al. 2026)
- New §18.x: LLM agent-based models of RFQ microstructure and dealer-chat extraction (FinDialogLens, TraderTalk)
- New §25.x: A synthetic credit-agreement QA benchmark with set-operation and multi-hop basket questions (KG-MuLQA as yardstick)
- Appendix C Trend Tracker rows: Charlotin hallucination-cases curve, FINRA GenAI report sections, BoE/FCA adoption %, Vals Finance Agent top score, EU AI Act milestones
- Retries vs. verifier posterior under question heterogeneity: a Ways-This-Blows-Up box for Ch 27 (Lazarus-rate auditing)
**Next targets (verification, cleanup, trims):**
- Cleanup pass: run the three python blocks in §26.12 in one interpreter and fix any assert or pandas-version issue (not executed this pass, per budget)
- Optional trim: the chapter is ~14.8k words by wc (about 2.1k of that is code); a later editing pass could tighten §26.3 and §26.6 prose to move toward the 12k target
- CHECK items still title-only: SR 11-7 text (paraphrased only), Mata v. Avianca sanction date and amount, Man Group AlphaGPT, IOSCO 2025 AI report

## Chapter 27
**New TOC ideas:**
- Operational Resilience & Vendor Concentration for credit desks (ICE-MarketAxess composites/venues, ICBC FS manual settlement, CrowdStrike/SGX, Bloomberg 2015 outage) as a standalone chapter or Part VIII section
- Appendix: FIX-for-credit cookbook (SecurityIDSource/PriceType/benchmark fields, spread-vs-price parser bugs, venue rules-of-engagement differences)
- Volatility-gated re-arm policies after flash events, linked to Ch 28 drawdown control and kill-switch governance
**Next targets (verification, cleanup, trims):**
- Cleanup pass: execute ch27 Python blocks 1-5 in order and fix any failing asserts
- Cross-reference consistency with Ch 18 s18.7 (auto-quoting Trend Watch), Ch 19 (90-second PT budget), Ch 26 s26.11 (Knight), Ch 28 (kill switches)
- Verify Citi 2022 FCA final-notice figures against the notice itself
- Fill Dinosaur v. S&P Global ruling dates from CourtListener docket

## Chapter 28
**New TOC ideas:**
- Liquidity speed limit: G < 2*DD_max/((m-1)*LCS) as a platform-wide capacity constraint, with an empirical calibration of the stress multiplier m by rating bucket and protocol (RFQ vs PT vs all-to-all), 2007-2026
- Kelly ruin boundary set by documents (1/L_max): a joint PRS-recovery model that maps credit-agreement provisions (non-pro-rata uptier, drop-down baskets) into L_max and sizing caps
- Correlated drawdown rules: modeling the platform-wide 5%/7.5% stop as a common jump in forced selling, using March 2020 and March 2026 positioning and crowding data
- Fund-as-borrower: a 13-week runway monitor for credit funds, BDCs and interval funds (redemption queues, margin haircuts, 22e-4 buckets), with Third Avenue 2015 and the 2026 private-credit redemption queue as cases
- Team production function: measuring analyst-signal correlation (rho) and coverage dilution (N_c) from an Edge Ledger, extending the Barclays QPS aligned-signal evidence
**Next targets (verification, cleanup, trims):**
- Run the chapter's cumulative Python (Blocks 1-7 plus pm_playbook_engine) in a cleanup pass; the code was written once and not executed per budget instructions
- Verify Bermin & Holm (2026) publication details (marked CHECK in text and resource graph)
- Optionally pull primary sources for March 2026 pod returns if exact percentages are wanted (text uses only Bloomberg's directional lede)
- Trim pass if the editor wants the chapter nearer the 10-12k target: candidates are the Block 3 asserts and the 28.3 source-extraction annotations
- Add Impax/Barclays QPS, The DESK and ISDA URLs to the resource graph once verified (currently title only)

<!-- STATUS: COMPLETE -->
