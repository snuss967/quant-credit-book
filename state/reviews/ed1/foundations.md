# Edition 1 Foundations Review — dependency map, gaps, primers

<!-- STATUS: IN PROGRESS -->

**Scope and method.** Edition 1 as it stands in `book_src/` (27 chapter files complete or near-complete, Ch 28 at 4,113 words, App A and B present, App C absent). Evidence is the Edition 1 review digest, the TOC in `SYSTEM_PROMPT.md` §3, the heading tree of App A, and `grep -c` counts of 55 concept patterns across every chapter file, with eight short section peeks to confirm whether a concept is *built* (defined, derived, coded) or merely *used*. Counts below are mentions per chapter from `grep -ciE`, so they are an index of reliance, not of quality.

**Headline.** The book has three real foundation layers (Ch 5–7: distributions, stochastic credit models, ML hygiene) and they are good. What it does not have is the layer *underneath* them: bond arithmetic, option pricing beyond the Merton formula, the bankruptcy and lien process, basic statistics (OLS, logistic, survival, shrinkage, PCA, bootstrap, Monte Carlo as a method), and contract plumbing (ISDA events, settlement, margin, financing). Those are used from Chapter 1 onward and taught, when they are taught at all, in Chapters 8, 12, 14, 15, 18, 21, 22 and 24, so the first third of the book leans on the last two thirds. Four chapters that were supposed to close foundational loops are unfinished: Ch 19 (ends at §19.4), Ch 24 (ends at §24.2, so CTD, auction and orphan-CDS mechanics do not exist), Ch 27 (ends at §27.2), Ch 28 (ends at §28.2, so Kelly-with-JTD and LVaR do not exist). Only three chapters (10, 13, 28) contain the word "prerequisite."

## 1. Dependency map

Format: **concept** → where it is first properly built → where it is used before, or without, being built. "Before" means an earlier chapter in reading order.

### 1.1 Mathematics and stochastic calculus

- **Itô's lemma** → built §6.1 ("the volatility tax"), 10 mentions. → Used in Ch 5 §5.3 (jump-diffusion SDEs for Merton/Kou, one explicit mention, implicit throughout 5.3–5.4) before it is built. Used later in Ch 23 §23.1–23.2 (CreditGrades) with no back-reference (Ch 23 has zero `§` cross-references in the whole file).
- **Change of measure, P vs Q (Girsanov)** → built §6.3.2 (two mentions of Girsanov, a correct one-paragraph statement, no Radon–Nikodym derivative, no discussion of what the measure change does to a jump intensity). → Used in Ch 1 §1.3.1 ("everything in this section is a physical-measure object", 4 mentions), Ch 3 (7 mentions, and §3.1 is internally inconsistent: line 41 prices the two-point bond under $\mathbb{Q}(V=V^+)=p$, line 104 then says "work under the desk's physical measure"), Ch 4 (7), Ch 5 (13). It is the single most-used idea in the book that is built late: 25 of 28 chapter files invoke risk-neutral or $\mathbb{Q}$, and Ch 13 ("PRS is P; the price is Q") and Ch 15 ("the SMR is a Q break gauge") make it a load-bearing distinction. The jump-intensity version of Girsanov (the P-to-Q hazard ratio, the "credit risk premium" as a multiplier on $\lambda$) is asserted in 6.3 and 14.9 ("never compare a CDS hazard with an agency default rate") but never derived.
- **Hazard rate / intensity** → built §6.6–6.8 (Cox processes, CIR, bootstrapping; 39 mentions). → Used before in Ch 3 (7: "the thirteen-week model was a hazard curve all along", the Bayesian 8-K) and Ch 5 (7). Heavy users after: Ch 14 (42), Ch 23 (20), Ch 17 (16), Ch 24 (15), Ch 11 (13), Ch 15 (11), Ch 21 (11). Ch 11 §11.4 ("hazard models, labels, and gradient boosting") uses the Cox proportional-hazards regression form, which is never built anywhere.
- **Poisson / compound Poisson / jump processes** → built §5.3 (Merton, Kou). → Used in Ch 1 §1.4 (anthology, 2 mentions) before; fine as anthology, but Ch 1 has no forward pointer.
- **Markov chains, HMM, regime switching** → built twice: §12.4 (two-state HMM) and §14.7 (Markov-switching joint law of $(\tau,R)$). → Used before in Ch 5 §5.6 (regime mixtures), Ch 9, Ch 10 (regime-conditional trend). Neither build references the other.
- **Brownian bridge** → never built. One mention in Ch 6 (line 374, first-passage discretisation bias in Black–Cox Monte Carlo). The reader is told the bias exists and not how to correct it.
- **Monte Carlo as a method** (seeding, standard error of an estimate, variance reduction, path discretisation) → never built. Used in Ch 1 §1.4 (one-factor threshold model), Ch 2 §2.3.2 (best-of-$n$ RFQ simulation), Ch 5 (8), Ch 6 (9), Ch 13–16, Ch 23. Every reference implementation runs a seeded simulation and asserts a tolerance; no section says where the tolerance comes from.
- **Copula / default correlation** → never built. 16 mentions, all in Ch 5 (a Bolder source-extraction annotation on Gaussian copulas, §5.7 area). Ch 1 §1.4 runs a one-factor threshold (Vasicek) Monte Carlo in the anthology. Then the concept disappears: Ch 12 (cross-sector covariance), Ch 19 (basket residual covariance), Ch 21 (CLO tranche loss, OC tests under correlated defaults) and Ch 28 (effective breadth when issuers cluster) all depend on a default-correlation model and none names one (Ch 21: zero copula mentions).

### 1.2 Bond math

- **Modified duration, DV01/CS01** → built §8.2 (line 52, $D^{\text{mod}} = -\frac1P \partial P/\partial y$) and App A §A.5. → Used in Ch 1 (5), Ch 2 (3), Ch 3 (2), Ch 4 (4), Ch 5 (2), Ch 7 (3) before. Ch 5 §5.2 line 53 writes the return as $-D^{\text{spr}}\Delta s + \tfrac12 C^{\text{spr}}(\Delta s)^2 + \dots$ with $D^{\text{spr}}$ and $C^{\text{spr}}$ introduced as "the spread duration" and "the spread convexity", unbuilt. Macaulay duration, the price–yield function, key-rate duration (glossary only), and the empirical "duration regimes" of §8.2 all presuppose a price–yield derivation that is nowhere in the book.
- **Convexity** → never derived. Used in Ch 5 (9), Ch 6 (3), Ch 8 (15), Ch 10 (10, "convexity is the receipt for momentum"), Ch 11 (5), Ch 21 (5), Ch 23 (11). The word carries three different meanings (price–yield curvature, option gamma, payoff shape of a trend strategy) and the book never separates them.
- **DTS** → built twice, §8.4 and §9.2 (58 and 107 mentions). → Used in Ch 1 (20), Ch 4 (11), Ch 5 (19), Ch 7 (21, triple barrier "in DTS space") before any definition. App A has a glossary line only.
- **OAS, Z-spread, G-spread, discount margin, yield-to-worst** → App A §A.5 lists them in a table; no chapter builds any of them. OAS is used in Ch 8 (34), Ch 9 (18), Ch 10 (16), Ch 12 (11), Ch 19 (11), Ch 1 (8), Ch 11 (8). There is no callable-bond model anywhere (no short-rate tree, no call schedule arithmetic), so "option-adjusted" is a label the reader must take on faith. Make-whole (11 mentions across Ch 5, 13, 15, 16) and yield-to-worst (one mention, Ch 4) have the same status.
- **Clean/dirty price, accrued interest, day counts** → App A §A.4–A.5 only. Used in Ch 15 (7, CoC put at 101 plus accrued), Ch 8, Ch 24.
- **The loan as an instrument** (floating coupon, discount margin, call at par, repricing) → built §21.1. → Used in Ch 12 (loans as a MAC sleeve), Ch 13–14 (every LMT is a loan transaction), Ch 17 (private credit is a loan book), Ch 20 §20.6 (BKLN). Ten chapters earlier than its build.

### 1.3 Options and the two surfaces

- **Black–Scholes formula** → stated, not derived, at §6.2 line 146 (Merton equity as call) and restated at §23.1 line 38. The BS PDE, replication, and why $N(d_2)$ is a risk-neutral probability are asserted. Ch 6 has one "Black–Scholes" mention, Ch 23 three.
- **Greeks (delta, gamma, vega, theta), implied vol, skew** → §23.5 "gives the feeling a Greek letter", i.e. it maps CS01 onto Greeks, assuming the reader already runs an options book. Nothing before it builds a Greek. Yet option language is structural in Ch 8 §8.3 (CCC bond "is an equity option"), Ch 11 ("high yield is a short put that pays a coupon"), Ch 15 §15.2–15.3 (CoC put, portability as a short digital), Ch 16 §16.3–16.4 (backstop as a short put, warrants with dilution), Ch 21 §21.1 and §21.4 ("a floater that is short a call", "the tests as an option book"). Six chapters price options before the options section arrives in Ch 23, and Ch 23 does not build them either.
- **Jump-to-default inside option prices** (Carr–Wu corridor, skew as JTD) → built §23.3–23.4; HJB with JTD built §18.6. → Used in Ch 5 §5.1 (mixture), Ch 8 §8.3, Ch 10 §10.9, Ch 16 §16.8.2 (Kelly with a jump) before.
- **Avellaneda–Stoikov / HJB** → built §18.4–18.6 (HJB appears only in Ch 18, 9 mentions). → Ch 1 §1.3 derives "the bid equation" with an inventory term and cites A–S (2 mentions); Ch 3 §3.2 cites it once. Acceptable as forward use; both need a one-line pointer.
- **Kelly / growth-optimal sizing** → built briefly at §16.8.2 (first-order condition with a jump, half-Kelly), the full treatment is TOC'd as §28.4 and does not exist. → Used in Ch 1 (1), Ch 4 (1), Ch 9 (1) before; Ch 7's 6 "Kelly" hits are the author Bryan Kelly, which the grep conflates and a reader may too.

### 1.4 Bankruptcy and legal process

This is the largest gap, and it sits under the Part the book is named for.

- **Chapter 11 as a process** (petition, automatic stay, first-day motions, DIP, exclusivity, disclosure statement, classes, voting, §1129 confirmation, cramdown, absolute priority, 363 sale) → never built. App A §A.9 glossary defines 363 sale, APR, adequate protection, DIP, DIP roll-up, exclusivity, first-day motions, fulcrum, impaired class, cram-down in one line each. Chapter usage: "absolute priority" appears in Ch 4, 5, 6, 16 (one each) and Ch 25 (1); "plan of reorganization" in Ch 4, 9, 14, 16 (≤2 each); "cramdown" nowhere outside the glossary; "classes of claims" nowhere; "confirmation" only Ch 16 (1) and Ch 25 (3); "exclusivity" Ch 16 (6), Ch 25 (4). Ch 16 (post-reorg equity, rights offerings, 503(b)(9) vs GUC) and Ch 25 §25.6–25.8 (the docket as an event stream, Rule 2019, claims registers) presuppose the whole process. Ch 14's 17 "DIP" mentions (DIP roll-ups as an LMT-era recovery transfer) presuppose DIP priority and roll-up mechanics.
- **Liens, collateral packages, intercreditor agreements, payment vs lien subordination** → never built. "Intercreditor" appears in Ch 14 (1), Ch 25 (2), Ch 26 (1), Ch 28 (1), and *zero times in Ch 13*, the uptier chapter, whose entire mechanism (Serta: a majority amends the credit agreement to create a super-priority tranche; the minority's remedy lives in the sacred-rights and pro-rata-sharing clauses) is an intercreditor and amendment-threshold story. "First lien / second lien" appears in Ch 14 (9) and Ch 16 (7). §13.2 "Legal prose to state space" encodes clauses as a state space without first explaining which document (credit agreement vs indenture vs intercreditor) governs which right.
- **Fulcrum security, enterprise-value waterfall, plan value** → the recovery waterfall engine is built in §13.7 (double-dip/pari-plus) and plan value in §16.1. → "Fulcrum" is used in Ch 1 (1), Ch 3 (5), Ch 4 (3), Ch 8 (3) before; "waterfall" in Ch 3 (2), Ch 4 (4), Ch 5 (5), Ch 6 (4), Ch 12 (10) before. The reader of Ch 5 §5.5 (Beta recovery conditioned on seniority) is assumed to know what seniority does in a waterfall.
- **Distressed exchange, consent solicitation, exit consents, unanimous/sacred rights, open-market purchase** → partially built §13.1–13.5 and §14.1 (distressed exchange as a soft default). → Used in Ch 1 (4), Ch 3 (6), Ch 5 (4, §5.6), Ch 6 (4), Ch 7 (3), Ch 10 (2) before.
- **Claims trading mechanics** (transfer feed, 3001(e), trade claims vs bonds) → §16.5 and §25.8 cover claims as instruments; the mechanics of how a claim settles and is assigned are not built.

### 1.5 Market plumbing

- **TRACE fields, caps, dissemination** → built §2.2 (history and censoring) and §18.8 (decoding). Used throughout; the two builds do not point at each other.
- **ISDA credit events, auction, CTD, deliverable obligations, succession** → TOC'd for Ch 24 §24.3+, which does not exist (Ch 24 ends at §24.2). "ISDA / credit event / auction" is used in Ch 3 (10), Ch 6 (9), Ch 10 (10), Ch 13 (10), Ch 18 (12), Ch 24 (10), Ch 16 (6). Ch 13's manufactured-default discussion and Ch 14's "two default rates" both lean on an auction and a CTD mechanism the book never shows.
- **CDS pricing (RPV01, par spread, upfront, standard coupons)** → built twice: §6.8 (7 RPV01 mentions) and §24.2 (15). Upfront conventions are used in Ch 5 (1), Ch 6 (5), Ch 10 (3) before §24.2 formalises them. Ch 10 trades CDX with 9 RPV01 mentions and 42 "settlement/T+1" hits, most of which are time-index notation ($t+1$) colliding with the settlement vocabulary, a notation collision App A §A.3 should list.
- **Settlement (T+1, fails, DTCC), clearing, initial and variation margin** → built §22.3–22.4; "margin" as a plumbing term appears only in Ch 22 (2). Ch 24's own "Ways This Blows Up" says "initial margin on the CDS leg is funded, put it in", with nothing to put it in. Ch 21 §21.2 builds loan settlement (T+20 and delayed-comp).
- **Repo, financing, haircuts, the funding leg of the basis** → §24.1 names the "frictionless lie"; no section builds a financing cost, a haircut schedule, or a prime-brokerage margin model. (The grep pattern "repo" is polluted by "report"; the underlying point stands on §24.1's text.)
- **ETF creation/redemption, AP, custom baskets, iNAV** → built Ch 20. → Used in Ch 2 §2.7 (ETF discount as the price of immediacy), Ch 8 §8.6 (HYG/JNK in the hedge matrix), Ch 10 §10.5, Ch 12 §12.7 before.
- **CLO constraints (OC/IC tests, CCC buckets, reinvestment period)** → built §21.3–21.4. → Ch 11 §11.6 (the CCC problem) and Ch 16 §16.2 (forced CLO selling of orphan equity and CCC paper) discuss the forced-seller behaviour and neither names an OC test or a CCC bucket (zero hits in Ch 11, 12, 14, 16).

### 1.6 Statistics and machine learning

- **OLS / panel regression, standard errors, Newey–West, Dimson betas** → regression is used in Ch 8 (39), Ch 9 (26), Ch 5 (23), Ch 10 (18), Ch 11 (13), Ch 2 (12), Ch 26 (11). §8.5 builds Dimson/Scholes–Williams on top of an assumed OLS. No section states the OLS estimator, its variance under autocorrelated and overlapping returns, or what a panel with issuer fixed effects is.
- **Logistic regression** → built §11.4 (22 mentions, alongside gradient boosting). → Used in Ch 1 §1.3.3 (additive log-likelihood ratio ⇒ logistic $\pi(x)$, 6 mentions), Ch 2 (12: fill-probability model and the logistic adoption curve, two different objects sharing a name), Ch 3 (3), Ch 5 (7) before.
- **Gradient boosting / tree ensembles** → never built; appears in Ch 11 (2), Ch 14 (1), Ch 26 (1).
- **Survival analysis** (survival function, censoring, Kaplan–Meier, Cox PH, cumulative incidence) → built in two pieces in the wrong order: §14.2–14.3 builds *competing risks* (Aalen–Johansen, "use cumulative incidence, not $1-$KM") and its code names Kaplan–Meier (line 849) before §15.5 builds basic survival analysis and Kaplan–Meier for regulatory clocks. Ch 6 §6.6 has the survival function $S(t)=\exp(-\int\lambda)$ but not estimation from data. Ch 11 §11.4 "hazard models" for default prediction precede both.
- **Bayesian updating** → built §3.4 (the 8-K). → Used in Ch 1 §1.3.3 (13 mentions) before; acceptable in an anthology, needs a pointer. Later uses in Ch 18 (2), Ch 26 (3).
- **Shrinkage (James–Stein, Ledoit–Wolf), covariance estimation, EWMA** → built §12.5 (Ledoit–Wolf, 5 mentions; EWMA, 9). → Shrinkage is used in Ch 3 §3.3.4 (counterparty scores "shrunk"), Ch 9 §9.7 (weights "shrunk toward equal"), EWMA in Ch 10 §10.3 (20 mentions, one line of decay algebra at line 106) before.
- **PCA / common residual factor** → never built; used in Ch 8 §8.8 (strip leading principal components from the DTS-scaled residual panel, with code at line 1002), Ch 7 (1), Ch 22 (1).
- **Bootstrap (statistical), block/stationary bootstrap** → never built; one mention each in Ch 7 and Ch 17. (The 28 "bootstrap" hits in Ch 6 are curve bootstrapping, a collision App A should record.)
- **Sharpe ratio, information ratio, fundamental law of active management, effective breadth** → Sharpe inference built §7.8 (deflated Sharpe). The fundamental law ($IR = IC\sqrt{BR}\cdot TC$) is used in Ch 2 §2.9.2 (the data-exhaust theorem), Ch 4 §4.8 (9 mentions), Ch 9 §9.7, Ch 28 §28.2 and never derived. Effective breadth $N/(1+(m-1)\rho)$ is built in Ch 4 and rebuilt in Ch 28.
- **Cross-validation, overfitting, multiple testing** → built Ch 7 (§7.7–7.8). → Used in Ch 1 (2), Ch 3 (1), Ch 6 (3) before. Ch 26 §26.7 ("the agent's trials are your trials") correctly back-references the idea.

## 2. The gap list, ranked by dependent chapters

Ranking counts chapters that *use* the concept with no build available earlier in reading order (or no build at all).

1. **P vs Q and the credit risk premium, done properly** (25 chapters use; built late and thinly at §6.3). Math. Needs: the measure change as a hazard multiplier, the P/Q ratio as a traded quantity, what a "Q gauge" (Ch 15) and a "P score" (Ch 13) are, and a notation rule for which measure every expectation sits in.
2. **Bond arithmetic: price–yield, Macaulay/modified/spread duration, convexity, DV01/CS01, clean/dirty, spread measures (OAS, Z, G, DM, YTW), the callable** (21 chapters use duration or OAS; none builds the price–yield function). Bond math.
3. **The bankruptcy and restructuring process, liens and intercreditor agreements** (Ch 3, 5, 13, 14, 15, 16, 17, 25, 26, 28 lean on it; glossary only). Legal.
4. **Option pricing and Greeks beyond the Merton formula, with jump-to-default** (Ch 6, 8, 11, 15, 16, 21, 23, 28 price options; BS stated once, never derived; no Greek built). Options.
5. **Regression, logistic regression, and panel-data hygiene for bonds** (Ch 1, 2, 3, 5, 8, 9, 10, 11 regress before Ch 11 builds logistic and nothing builds OLS). Statistics.
6. **Survival analysis in the right order: censoring, S/F/h, KM, Cox PH, then competing risks** (Ch 6, 11, 14, 15, 17; built back-to-front across 14 and 15). Statistics.
7. **Default correlation: one-factor threshold model, copula vocabulary, what it does to tranches and breadth** (Ch 1, 5, 12, 19, 21, 28 depend; never built). Math/statistics.
8. **ISDA credit events, the auction, CTD and deliverables** (Ch 3, 6, 10, 13, 14, 16, 18, 24 use; TOC'd in Ch 24 and unwritten). Plumbing.
9. **Monte Carlo as a method and the Brownian bridge** (every reference implementation; Ch 1, 2, 5, 6, 13–16, 23). Math/statistics.
10. **Covariance estimation: EWMA, shrinkage, PCA, factor covariance** (Ch 3, 8, 9, 10, 19 before §12.5 builds part of it; PCA never). Statistics.
11. **Financing, haircuts, margin and the funding leg** (Ch 12, 17, 20, 21, 22, 24, 28; no build). Plumbing.
12. **The fundamental law and effective breadth, derived once** (Ch 2, 4, 9, 28; used in two theorems, never derived). Statistics/portfolio.
13. **Kelly and growth-optimal sizing with a jump** (Ch 1, 4, 9, 16, 28; §16.8.2 is the only build and §28.4 is unwritten). Math.
14. **CLO and loan vocabulary before Part III uses it** (Ch 11, 12, 16 use CCC buckets and forced CLO selling without naming the tests; built §21.4). Plumbing.
15. **Tree ensembles and the statistical bootstrap** (Ch 7, 11, 14, 17, 26; never built). ML.

## 3. Proposal: primer chapters and appendices vs prerequisite boxes

Principle: build a thing once, in the earliest place a reader needs it, in the book's voice (desk framing, derivation, spec block, source extraction, case, resource graph), and make every later use a one-line back-reference. Where the concept is small or already built late, add a **prerequisite box** (a fenced `> **Prerequisites.**` block at the top of the section listing the three symbols or facts the section assumes and the § where each is built). Where the concept is large and unbuilt, add a chapter or appendix per the growth rule (`NN_chNNb_slug.md`, "Chapter NN-B"; `9N_appX_slug.md`).

### 3.1 New chapters

- **`04_ch04b_bond_math_for_the_desk.md`, "Chapter 4-B: Bond Math for the Desk: Price, Yield, Duration, Convexity, Spread Measures and the Callable Bond."** Placement: last chapter of Part I, so every Part II formula has its units. Scope: derives the price–yield function, Macaulay/modified/spread duration, convexity, DV01/CS01 and key-rate duration, then every spread measure the book quotes (G, I, Z, OAS, discount margin, YTW, asset-swap, par CDS) from one discount curve, with a minimal callable-bond model (a call schedule plus a one-factor lattice) so OAS and make-whole are computed rather than named. The spec block ships `bondmath.py` (clean/dirty, day counts, yield solvers, duration/convexity, Z and OAS) that Chapters 5, 8, 9, 10, 12, 15, 19 import. Case: the March 2020 fallen angel from Ch 1 §1.4, repriced in every spread measure, to show which numbers moved and which were conventions.
- **`06_ch06b_options_and_measures_for_credit.md`, "Chapter 6-B: Options for Credit People: Replication, Black–Scholes, Greeks, Jump-to-Default and the Two Measures."** Placement: after Ch 6, before Ch 7. Scope: replication and the BS PDE in the book's own notation, the Greeks as risk-report lines, implied vol and skew, a Merton jump-to-default extension so the Carr–Wu corridor of §23.3 is a corollary, and a full P-to-Q section that extends §6.3.2 to intensities (the hazard multiplier, the risk-premium ratio, the notation rule for every expectation). It becomes the single home for "CCC is an equity option" (§8.3), "HY is a short put" (Ch 11), the CoC put (§15.2), portability as a digital (§15.3), backstops and warrants (§16.3–16.4), the loan call (§21.1) and the OC test as an option book (§21.4). Spec block: `credit_options.py` with BS, Greeks, Merton-JTD and an implied-vol solver.
- **`07_ch07b_statistics_for_credit_panels.md`, "Chapter 7-B: The Statistician's Toolbox for Credit Panels: Regression, Logistic Models, Survival Analysis, Shrinkage, PCA, Bootstrap and Monte Carlo."** Placement: after Ch 7, closing Part II. Scope: OLS and panel regression with issuer clustering, overlapping returns and Newey–West; logistic regression and calibration (so Ch 1, 2, 3, 11 share one object); survival analysis in the right order (censoring, S/F/h, Kaplan–Meier, Cox PH, then a pointer to competing risks in §14.2); covariance estimation (EWMA, Ledoit–Wolf, factor covariance, PCA for a residual panel); the statistical bootstrap (block and stationary) and Monte Carlo as a method (standard error, variance reduction, discretisation and the Brownian-bridge correction for first passage). Spec block: `creditstats.py`, imported by Ch 8, 9, 10, 11, 12, 14, 15.
- **`12_ch12b_the_restructuring_process_as_a_state_machine.md`, "Chapter 12-B: The Restructuring Process as a State Machine: Documents, Liens, Intercreditor Agreements, Out-of-Court and Chapter 11."** Placement: by the growth rule it files after Ch 12 and before `13_00_part_IV.md`, so it reads as the gateway into Part IV; the Part IV opener should begin with "read 12-B first." (Alternative if the Part boundary matters more than the growth rule: `93_appD_...` as a reference appendix; a chapter is recommended because the material needs the full anatomy, including a Serta-to-Incora case and a `restructuring_state_machine.py` spec.) Scope: which document governs which right (indenture vs credit agreement vs intercreditor vs security agreement), lien and payment subordination, amendment thresholds and sacred rights; the out-of-court menu (exchange, consent, uptier, drop-down) as transitions; Chapter 11 as a timed state machine (petition, stay, first days, DIP and roll-ups, 363, exclusivity, disclosure statement, classes and voting, §1129, cramdown, APR, effective date) with the fulcrum and plan value defined once; and claims mechanics (503(b)(9), GUC, 3001(e) transfers). Ch 13–16 and 25 then back-reference it instead of re-explaining.

### 3.2 New appendices

- **`93_appD_market_plumbing_and_contract_mechanics.md`, "Appendix D: Plumbing: Settlement, Clearing, Margin, Financing, and the ISDA Credit-Event Machine."** Scope: a reference, not a narrative: bond, loan, CDS and ETF settlement cycles and fails; clearing and initial/variation margin; repo, haircuts and the funding leg of every basis; ISDA credit events, the determinations committee, the auction, CTD and deliverable rules, succession and orphaning. It is the back-reference target for Ch 10, 12, 17, 20, 21, 22, 24, 28 until Ch 24 §24.3–24.6 are written, after which the appendix keeps the tables and Ch 24 keeps the derivations.
- **`94_appE_laws_of_the_desk.md`, "Appendix E: The Laws of the Desk."** Scope: the numbered list in §5 below, each law with its one-line statement, the equation it compresses, and the sections where it bites. Every chapter's Desk Debrief tags its lessons with law numbers, and the preface points here.
- **`92_appC_trend_tracker.md`** is in the TOC and absent from `book_src/`. Not a foundations item, but it is the only missing file the TOC promises.

### 3.3 Prerequisite boxes (no new file)

Add a `> **Prerequisites.**` box at the top of: Ch 1 §1.3 (P vs Q → 6-B; Bayes → §3.4; A–S → §18.4); Ch 3 §3.1 (fix the P/Q inconsistency, point to 6-B) and §3.3.4 (shrinkage → 7-B); Ch 5 §5.2 (duration/convexity → 4-B) and §5.3 (Itô → §6.1); Ch 5 §5.5 (seniority and the waterfall → 12-B); Ch 8 §8.8 (PCA → 7-B); Ch 9 §9.7 and Ch 10 §10.3 (EWMA, shrinkage → 7-B/§12.5); Ch 11 §11.4 (logistic, Cox PH, boosting → 7-B); Ch 11 §11.6 and Ch 16 §16.2 (OC tests and CCC buckets → §21.4); Ch 13 §13.2 (documents, liens, thresholds → 12-B); Ch 14 §14.3 (Kaplan–Meier → 7-B/§15.5); Ch 15 §15.2 (puts, digitals → 6-B); Ch 16 §16.3–16.4 and §16.8.2 (options, Kelly → 6-B, §28.4); Ch 21 §21.1 and §21.4 (options → 6-B); Ch 23 §23.1 and §23.5 (Itô, BS, Greeks → §6.1, 6-B); Ch 24 §24.1 (financing, margin → App D).

## 4. Reading-order fixes

1. **Survival analysis is built back-to-front.** §14.2–14.3 (competing risks, Aalen–Johansen, the "1 − KM" trap, with KM named in code) precede §15.5 (basic survival and Kaplan–Meier). Fix: move the S/F/h/KM/censoring build to 7-B; §14.2 opens with "competing risks extend §7-B.4"; §15.5 keeps only the regulatory-clock application and the Bohn–Stein extraction.
2. **DTS is built twice** (§8.4, §9.2). Keep §8.4 as the build ("the unit of credit beta"), turn §9.2 into a one-page back-reference plus the factor-specific point (beta $=\text{DTS}_i/\text{DTS}_m$).
3. **CDS pricing is built twice** (§6.8, §24.2). Keep §6.8 as the pricing build (RPV01, par spread, triangle, bootstrapping); §24.2 keeps conventions (standard coupons, upfront, ISDA model inputs) and the basis, and back-references §6.8. Then write §24.3–24.6 (CTD, auction, orphaned CDS, manufactured events), which Ch 3, 10, 13, 14, 18 already cite.
4. **Regime models are built twice** (§12.4 HMM, §14.7 Markov-switching). Cross-reference both ways; §14.7 should import the filter from §12.4's code.
5. **TRACE is built twice** (§2.2 censoring, §18.8 decoding). Add mutual pointers and move the field-level table to App B.
6. **Ch 1 is an anthology that uses everything.** Each extracted idea in §1.3–1.4 needs a "(built in §x.y)" tag: Bayes → §3.4, A–S → §18.4, threshold Monte Carlo → 7-B and §5.7, credit triangle → §6.8, DD calibration → §6.4, Kelly → §28.4.
7. **Forward references from Part I–II are thin where they matter.** Ch 1–5 forward-reference Ch 6 (12 times) but Ch 24 once, Ch 18 five times (all from Ch 3), Ch 21 and Ch 22 never. Ch 2 §2.7 → Ch 20; Ch 2 §2.3 → §18.7; Ch 5 §5.6 → Ch 14; Ch 5 §5.5 → 12-B.
8. **Ch 23 has zero `§` cross-references and six "Chapter" mentions** for a chapter that rests on §6.1–6.4, §5.3, §8.3 and §18.6. Ch 4 (5 chapter refs), Ch 20 (5), Ch 24 (3) and Ch 28 (5) are the other under-linked files.
9. **Ch 16 §16.2 and Ch 11 §11.6 should forward-reference §21.4** for the CLO tests that make the forced seller forced, and §21.4 should back-reference them as the two places the option book is exercised.
10. **Notation collisions to add to App A §A.3:** "bootstrap" (curve vs statistical), "Kelly" (criterion vs author), "logistic" (classifier vs adoption curve), "convexity" (price–yield vs gamma vs payoff shape), "$t+1$" vs "T+1", "duration" (analytical vs empirical vs spread).
11. **Finish the four truncated chapters before Edition 2 adds breadth:** Ch 19 (§19.5+, eviction, stress liquidity commonality, basket adverse selection), Ch 24 (§24.3+), Ch 27 (§27.3+), Ch 28 (§28.3–28.6: horizons, Kelly with JTD, LVaR, running the team). Three of those (Kelly, LVaR, auction mechanics) are foundations other chapters already cite.

## 5. The Laws of the Desk

Lessons that already recur across three or more Desk Debriefs, stated once so later chapters can cite a number instead of restating. Suggested wording and where each bites.

1. **IDO or it didn't happen.** Strip index spread, Treasury and DTS beta before you call anything alpha, a markout or a hedge. (Ch 3, 8, 10, 11, 19)
2. **Bonds are not bets; issuers are.** Effective breadth is $N/(1+(m-1)\rho)$, and forty-seven CUSIPs of one issuer are one hat. (Ch 4, 7, 9, 28)
3. **DTS is the unit of credit beta.** Vol targeting is a constant-DTS budget; carry is the price of DTS; beta is $\text{DTS}_i/\text{DTS}_m$. (Ch 8, 9, 10, 12)
4. **Say which measure you are in.** PRS is $\mathbb{P}$; the price is $\mathbb{Q}$; a CDS hazard is not an agency default rate; the gap between them is the premium you are paid or paying. (Ch 1, 6, 13, 14, 15)
5. **A bid is a posterior, not a markup, and winning is information.** Condition on the sender and on having won; a backtest on fills alone cannot see the winner's curse. (Ch 1, 3, 18, 19)
6. **Charge the jump once.** Diffusive fear is pennies in bonds; the jump-to-default is the whole premium, so price it in one place and do not re-add it in the spread, the skew and the sizing. (Ch 5, 16, 18, 23, 28)
7. **Default is a menu and recovery is a U.** There are two default rates and two recovery humps; 40% is a quoting convention; a distressed exchange is parole, not immunity. (Ch 5, 6, 13, 14, 24)
8. **Every clause is a payoff function, and one word can be the whole loss.** Read the document as a program before you model it as a distribution. (Ch 13, 15, 16, 25, 26)
9. **A mark is a moving average of the truth.** Stale marks shrink betas, fake lead–lag and flatter Sharpe; sum the lags and desmooth before you optimise. (Ch 8, 10, 12, 17, 20)
10. **Costs decide and capacity is a square.** Break-even turnover is $\alpha/2\bar c$; at the manager's favourite size the client keeps a third; liquidity tiers bind first. (Ch 2, 4, 9, 12, 28)
11. **Label every number.** Gross or net, simulated or live, $\mathbb{P}$ or $\mathbb{Q}$, numerator and denominator, knowledge time, and sourced or illustrative. (Ch 2, 4, 7, 14, 26)
12. **Count your trials.** The agent's trials are your trials; deflate every Sharpe by the number of things you tried, including the ones the machine tried for you. (Ch 7, 9, 26)
13. **The label is the model.** Triple-barrier in DTS space, cumulative incidence not 1 − KM, a hit rate without an exclusion rate is half a sentence. (Ch 7, 11, 14)
14. **Censoring is the signal.** TRACE caps, surviving bonds, filled RFQs and non-accruals are truncated samples; model the truncation before the data. (Ch 2, 3, 5, 17, 18)
15. **Forced selling is a supply schedule, not a mood.** Fallen angels, CLO tests, ETF redemptions and post-reorg holders sell on rules you can read in advance. (Ch 11, 16, 20, 21)
16. **The court is a random variable with timestamps.** Rulings are regime switches; the plan value is a negotiated number; model both as such. (Ch 13, 14, 16, 25)

## 6. Edition 2 targets

- `04_ch04b_bond_math_for_the_desk.md`: new, 8–10k words; price–yield, durations, convexity, DV01/CS01, spread measures, callable model, `bondmath.py`; Ch 5, 8, 9, 10, 12, 15, 19 switch to back-references.
- `06_ch06b_options_and_measures_for_credit.md`: new, 8–10k words; replication, BS, Greeks, Merton-JTD, Carr–Wu as corollary, intensity-space Girsanov and the P/Q premium; `credit_options.py`.
- `07_ch07b_statistics_for_credit_panels.md`: new, 8–10k words; OLS/panel, logistic, survival (S/F/h, KM, Cox), covariance (EWMA, Ledoit–Wolf, PCA), bootstrap, Monte Carlo method and Brownian bridge; `creditstats.py`.
- `12_ch12b_the_restructuring_process_as_a_state_machine.md`: new, 8–12k words; documents, liens, intercreditor, amendment thresholds, out-of-court menu, Chapter 11 timeline, APR, cramdown, fulcrum, claims mechanics; `restructuring_state_machine.py`.
- `93_appD_market_plumbing_and_contract_mechanics.md`: new, 4–6k words; settlement, clearing, margin, financing, ISDA events and auction, as reference tables.
- `94_appE_laws_of_the_desk.md`: new, 2k words; the 16 laws with equations and section index.
- `92_appC_trend_tracker.md`: create the TOC-promised file.
- `03_ch03_pjt_rssg_cognitive_bridge.md`: fix the $\mathbb{Q}$/$\mathbb{P}$ inconsistency in §3.1 (lines 41 vs 104); prerequisite boxes at §3.1, §3.3.4.
- `05_ch05_credit_probability_distributions.md`: prerequisite boxes at §5.2, §5.3, §5.5; forward references to Ch 14 and 12-B.
- `06_ch06_merton_and_intensity_models.md`: §6.3.2 extended or replaced by a pointer to 6-B; Brownian-bridge correction added to the Black–Cox Monte Carlo at line 374.
- `08_ch08_isolating_ido_and_empirical_duration.md`: §8.2 back-references 4-B; §8.8 back-references 7-B for PCA.
- `09_ch09_factor_investing_in_credit.md`: §9.2 reduced to a back-reference to §8.4.
- `11_ch11_defensive_systematic_high_yield.md`: §11.4 imports logistic/Cox/boosting from 7-B; §11.6 forward-references §21.4.
- `13_ch13_codifying_lmt_game_theory.md`: §13.2 opens with the document map from 12-B; add "intercreditor" to the uptier mechanism.
- `14_ch14_default_and_recovery_cycle_lmt_era.md`: §14.3 back-references KM in 7-B; §14.7 cross-references §12.4.
- `15_ch15_event_driven_mna_and_coc.md`: §15.5 reduced to application; §15.2–15.3 back-reference 6-B.
- `16_ch16_post_reorg_equities_and_claims.md`: §16.1 and §16.5 back-reference 12-B; §16.2 forward-references §21.4; §16.8.2 points to §28.4.
- `19_ch19_portfolio_trading_pricing_engines.md`: write §19.5–19.8 (eviction, stress commonality, basket adverse selection, engine).
- `23_ch23_cross_asset_convexity_and_vol_surface.md`: add `§` cross-references throughout; §23.5 back-references 6-B.
- `24_ch24_bond_cds_basis_and_deliverables.md`: write §24.3–24.6; §24.2 back-references §6.8 and App D.
- `27_ch27_system_architecture_and_asics.md`: write §27.3 onward.
- `28_ch28_pm_playbook.md`: write §28.3–28.6 (horizons, Kelly with JTD, LVaR, the team); §28.2 back-references §4.8.
- `90_appA_notation_and_conventions.md`: add the six collisions from §4.10 to §A.3; add a "measure of every expectation" rule.
- `00_00_preface.md`: add the Laws of the Desk list and a "prerequisite box" legend to "how to read this book."

## 7. Research requests

- Shelf pages for 12-B: Moyer on plan process, classes and cramdown; Bohn–Stein or Schmid on lien subordination; the Serta, Incora and Mitel rulings for the amendment-threshold and sacred-rights language (dates and citations already in Ch 13's resource graphs).
- Shelf pages for 4-B and 6-B: Tuckman-style price–yield and OAS derivations and Natenberg's Greeks, if they exist in `/source_pdfs/`; otherwise write from first principles with no citation needed.
- One source for the Brownian-bridge first-passage correction (Beaglehole–Dybvig–Zhou style) to cite in 7-B and §6.5.
- Grinold–Kahn pages for the fundamental law so Ch 2 §2.9.2, Ch 4 §4.8 and Ch 28 §28.2 cite one derivation.
- No web research needed for the prerequisite boxes or reading-order fixes.

<!-- STATUS: COMPLETE -->
