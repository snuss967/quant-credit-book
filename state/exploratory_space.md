# The Exploratory Space (living map; Edition 2 baseline)

*Maintained by the Fable planner and mappers. Consolidates `state/reviews/ed1/*`, `state/research/trend_*.md`, and the Exploratory-space notes in `state/advisor_briefs/*.md` (18 Oct 2026). Each Fable mapper pass that closes a research batch updates §2 and §3 and dates the change. The framework map in Ch 4 (§4.3, §4.11 "the empty cells") is the in-book version of this file.*

## 1. The axes

The book's space is the product of seven axes. A chapter is a region; a case study is a point; a trend is a drift along one axis; an "empty cell" is a region no chapter owns.

| # | Axis | Poles (2026) | Where the drift is |
| :-- | :-- | :-- | :-- |
| A1 | **Instrument and venue** | Cash bond · loan · CDS single-name · index CDS · ETF · listed credit future · private loan · claim | Risk transfer migrating from cash to baskets (ETF ↔ PT ↔ futures); private loans acquiring public plumbing (ICE IDs, daily prices, PRIV) |
| A2 | **Measure** | $\mathbb{P}$ (default scores, PRS, agency rates) ↔ $\mathbb{Q}$ (spreads, CDS hazards, option skews) | Every "value" signal in the industry is the $\mathbb{Q}-\mathbb{P}$ wedge; the wedge is now measured with three default definitions (headline, ex-DE, private "shadow") |
| A3 | **Horizon and speed** | Fifteen-second RFQ · daily markout · monthly factor · quarterly mark · multi-year docket | Fast models won 2020 and 2025; composite reflexivity makes daily marks a moving average of the truth |
| A4 | **Information source** | Price (TRACE, composites) · document (credit agreement, indenture) · docket (PACER, Rule 2019) · mark (BDC SOI) · chat/news (LLM features) | Document and docket features moving from Part IV lore to Part III regressors (PRS as a cross-sectional factor); composites becoming the benchmark asset |
| A5 | **Forced-flow rule set** | CLO tests and CCC buckets · ETF creation/redemption · rating stops and fallen angels · insurer RBC/SVO · redemption queues and gates · drawdown stops | New generators: NAIC CLO C-1 factors (YE2026), SVO discretion (Aug 2026), semi-liquid 5% gates (first net-outflow quarter Q1 2026), captive CLO equity and CLO ETFs as the reset bid |
| A6 | **Legal regime** | Contract vintage (blockers by year) · forum (S.D.N.Y., S.D. Tex., Fifth Circuit, NY Appellate Division, UK Part 26A, WHOA, sauvegarde) · doctrine ("open market purchase", integrated vs step-by-step, Purdue releases) | Courts as dated regime switches; the 2026 "consensual turn" (equity handovers replacing coercive uptiers) as a candidate structural break |
| A7 | **Automation level** | Voice · processed · auto-executed (no-touch) · agentic (LLM specifier + ROBO) | 60–88% no-touch on eligible RFQ items; measurement of "electronic" itself contested; agentic research creating a multiple-testing explosion |

## 2. The frontier: what is built, what Edition 2 builds, what is open

Status codes: **E1** built in Edition 1; **E2** planned (file named in `SYSTEM_PROMPT.md` §3 Edition 2 additions or in `continuation_prompt.md` WP5); **OPEN** research exists but no chapter owns it; **GAP** no research yet.

### 2.1 Foundations layer (the floor)
- Distributions, structural and intensity models, ML hygiene: **E1** (Ch 5–7).
- Bond arithmetic and spread measures, callable model: **E2** (4-B).
- Options, Greeks, JTD, $\mathbb{P}\to\mathbb{Q}$ for intensities: **E2** (6-B).
- Regression, logistic, survival in order, covariance, bootstrap, Monte Carlo method: **E2** (7-B).
- Restructuring process, liens, intercreditor, Chapter 11 state machine: **E2** (12-B).
- Plumbing: settlement, margin, financing, ISDA events: **E2** (App D).
- Default correlation / copulas as a built object (tranches, breadth, LVaR): **OPEN** (seeded in 7-B and Ch 28; a 28-B candidate for Edition 3: "Correlated Jumps: Copulas, Tail Dependence and the Platform Stop").
- Stochastic recovery ($R^{\mathbb{Q}}$ term structure, recovery locks, digital CDS): **OPEN** (Ch 5-B candidate).

### 2.2 Trends (structural)
- Electronification, PT, all-to-all, ETF liquidity: **E1** (Ch 2, 19, 20); "what electronic means" and the 2026 consolidation year: **E2** (Ch 2 expansions).
- Listed credit futures and index microstructure: **E2** (10-B); the basket triangle: **E2** (Ch 20 section).
- Non-bank liquidity provider economics and the capital-free quote: **OPEN** (sections in Ch 2/18/22; Ed 3 candidate 22-C).
- Composite pricing as a contested asset (CP+, Ai-Price, ICE rationale): **OPEN** (seed in Ch 19 staleness-as-variance; Ed 3 candidate 19-B "Who Owns the Mid").
- Reporting-time wars and print latency as a mixture: **OPEN** (22-B candidate).
- Index-time liquidity and closing auctions: **OPEN** (19-B candidate).
- European and EM electronification, the EU consolidated tape: **GAP**.
- Odd lots and retail flow in TRACE: **GAP**.
- LMT cycle, DE as modal default, re-default base case, recovery bimodality: **E1** (Ch 13–14); the Autopsy Room and courts table: **E2** (13-B); the re-default clock dataset: **E2** (Ch 14 §14.3 expansion); cooperation agreements as cartels and the antitrust frontier: **OPEN** (14-B candidate; needs Optimum/Selecta dockets).
- Documentation arms race as a time series (blocker adoption by vintage): **OPEN** (App C thread; Ch 9 docs-vintage factor).
- The 2026 consensual turn (equity handovers): **OPEN**, track quarterly in App C; Hamilton-filter use case.
- Private credit convergence, marks vs prices, semi-liquid redemption dynamics: **E1** (Ch 17, 12); marking the unmarked and PC-LMEs: **E2** (17-B).
- Insurance capital, private letter ratings, NAIC as forced-flow calendar: **E2** (Ch 22 section); the offshore reinsurance loop as a demand engine: **OPEN** (1-B "Holder Map" candidate).
- Loans and CLOs: captive equity, resets, CLO ETFs as the reset bid, Octaura, Versana digital voting, *Kirschner*: **E1** (Ch 21) with App C rows **E2**; the CLO as a rule-bound buyer and cure-trade alpha: **OPEN** (21-B candidate).
- Regulation as a price (TRACE, T+1, clearing, dealer rule vacatur, Basel endgame): **E1/E2** (Ch 22 + sections).
- Systematic credit industry: bought not built, <2% share, hybrids win, AI not the moat: **E1** (Ch 4); genealogy tree and AUM cycle: **OPEN** (4-B was reassigned to bond math; genealogy is an Ed 3 section).
- Factor replication crisis and the bond data pipeline: **E2** (9-B).
- AI agents, provenance and the data room: **E1** (Ch 26); 26-B data-room/prompt-injection: **OPEN**; covenant-extraction benchmark (25-B): **OPEN**.
- Operational resilience and vendor concentration (ICE–MarketAxess, outages): **OPEN** (Ch 27 section or Part VIII).

### 2.3 Trends (strategy: trend and momentum)
- TSMOM in CDX/iTraxx, cross-asset lead–lag, trend+carry, CTA speed: **E1** (Ch 10).
- Momentum under the replication audit (which constructions survive BH-FDR; within-firm idiosyncratic 12-1): **E2** (9-B, with a Ch 10 cross-reference).
- Speed as a regime variable; multi-speed ensembles with cost curves: **OPEN** (Ch 10 section).
- Trend convexity via payer swaptions: **OPEN** (Ch 10/23).
- Rating momentum and DD momentum as trend in default intensity: **OPEN** (Ch 6/10/11 sections).
- Single-name trend with LMT-aware jump sizing (PRS → $\lambda_J$): **OPEN** (bridge Ch 10 ↔ 13).
- Event momentum through silent regulatory milestones (Ch 15 → Ch 10): **GAP**.

### 2.4 Microstructure and execution
- A–S/GLFT with JTD, TRACE decoding, BWIC leakage: **E1** (Ch 18); hit-ratio-targeted quoting, cover price, client tiers, effective dealer count: **E2** (18-B).
- Protocol selection and smart routing under stress parameters: **OPEN** (19-B candidate from Ch 2's odds-threshold router).
- Block reservation pricing for $n$ lots and basket adverse selection: **E1** partial (Ch 19); revealed-preference $\gamma$ from won/lost PT quotes: **OPEN**.
- Dealer quote competition as a signal (Hendershott et al. 2026 runs data): **OPEN** (18-B section if the data arrive).
- Time-to-trade as a liquidity feature; axe-honesty scores: **OPEN** (Edge Ledger features).

### 2.5 Special situations
- PRS, uptier/drop-down game theory, double-dip waterfalls: **E1** (Ch 13); litigation map as a Markov model and the courts table: **E2** (13-B).
- Litigation claims as a recovery tranche (Serta \$261mm + 9%): **OPEN** (Ch 16 section).
- Deals away and the six-month par call as the sponsor's unwind option: **OPEN** (Ch 13 section).
- Defeasance and consent strips as a game tree (EA, WBD): **OPEN** (Ch 15 section).
- Convertible fundamental-change puts and make-whole tables (U.S. Steel): **OPEN** (15-B candidate).
- CDS succession and orphaning after LMEs (New Fortress, DISH DBS, Discovery Global): **OPEN** (Ch 24 section).
- Equity handovers and pricing the lender-owned company: **OPEN** (Ch 16 bridge).
- EM sovereign restructurings as the RSSG sector: **GAP**.

### 2.6 Portfolio management
- Horizon allocation, Kelly with JTD, LVaR, drawdown control, the team: **E1** (Ch 28).
- Liquidity speed limit $G < 2\,DD_{\max}/((m-1)\,LCS)$ with $m$ calibrated by rating and protocol: **OPEN**.
- Fund-as-borrower: the 13-week runway monitor for funds, BDCs and interval funds: **OPEN** (Ch 28 section; the 13-week model's next rebirth).
- Correlated drawdown rules as a common jump in forced selling (March 2020, March 2026): **OPEN**.
- Team production function from the Edge Ledger ($\rho$, $N_c$): **OPEN**.

## 3. Open empirical questions (the book's own research program)

Each is phrased so a Sonnet researcher or an Edition 3 writer could answer it with named data; none is answered in Edition 1.

1. **Pre-LMT flow:** in the 60 days before an announced uptier, do loan prices and TRACE flow show the CUSUM signature Ch 3 §3.6 predicts, and does the rate hedge ratio collapse first (the Alltel logic of Ch 8)? Data: LCD/TRACE around the 13-B cases.
2. **Is PRS spanned?** Regress Ch 13's Priming Risk Score on value and quality inside DTS cells (Ch 9 §9.3.4 hook). If it is not spanned, document risk is a factor.
3. **Is the 2026 consensual turn durable?** Quarterly share of coercive uptiers vs equity handovers; a Hamilton filter on the series; the courts-and-blockers explanation vs the cyclical one.
4. **Which momentum survives?** Rerun Ch 10's constructions on the OSBAP panel with the DRR 2026 filters; report net of the cost curve.
5. **BWIC leakage:** pre-auction drift and survivorship in CLO BWIC covers; no paper exists.
6. **Revealed dealer risk aversion:** invert PT hit rates for $\gamma$ and $\pi$; reconcile with the 30× gap to capital-based $\gamma$.
7. **Mark-to-price lead–lag:** do public LL software spreads lead private marks by one quarter, and does the redemption-request percentage lead both?
8. **The stress multiplier $m$:** bid-ask widening by rating and protocol in March 2020, April 2025, March 2026; does PT widen less than RFQ?
9. **Re-default hazard shape:** fit Weibull/mixture-cure to the hand-built LME→outcome dataset; does the >70%-within-two-years mass hold outside Moody's sample?
10. **Does the court matter in price?** Event-study excluded-lender loan prices around the Dec 31 2024 rulings, the Serta remand damages, and the Incora partial unwind.
11. **Cooperation-agreement headlines as a tradable signal:** price reaction to co-op formation announcements by coverage share.
12. **Composite reflexivity:** how much of daily OAS "mean reversion" is evaluated-pricing error with $\kappa\sigma^2\cdot$age growth, by pricing source?
13. **LLM-feature leakage:** does purging to the feature generator's knowledge cutoff erase the reported gains of text features for default prediction?

## 4. How this file grows

- A mapper pass closing a research batch moves items from **GAP** to **OPEN** (research exists) and from **OPEN** to **E2/E3** (a file is named), and adds or retires questions in §3 with a date.
- The planner, at each edition's Stage 6, promotes the highest-value **OPEN** regions to the next edition's TOC and records the promotion in `SYSTEM_PROMPT.md` §3.
- Chapter 4 §4.11 ("the empty cells") is regenerated from §2 of this file each edition.

<!-- STATUS: COMPLETE -->
