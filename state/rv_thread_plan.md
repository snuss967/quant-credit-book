# The Relative-Value Thread: Plan (user directive 13, 2026-10-18)

> "I want to make sure we are deeply exploring the relative value side of quantitative credit as well. Particularly the pod shop long a credit short a credit so that we can isolate the idio as the alpha. That weaves through every chapter. So be intentional about how you work it in."

## Where the book stands (measured 06:42 UTC)

Idiosyncratic isolation is concentrated in Ch 1, 7, 8, 8-B, 8-C, 19 and 28 (20–100 mentions each). The explicit pod trade (long one credit, short another, hedged so the residual is the view) is thin almost everywhere: "pair" or "long-short" appears 0–5 times in most chapters, and "relative value" appears 0–4 times. The Ch 8 TOC entry ("Stripping Beta to Isolate Pure IDO") is the natural mechanical home, but nothing ties the trade across chapters.

## Design (to be refined by a Fable RV architect, then executed)

1. **The spine: one trade, many lenses.** The pod RV trade is a question every chapter can ask of its own tool: *what does this let me be long, what does it let me be short, and what is left over once the hedge has eaten the beta?* Each chapter answers it once, with intention, in its own vocabulary.
2. **The Pair Book.** A labeled fictional composite: a credit RV pod on a multi-manager platform (cast: a PM, an analyst, and the platform's risk manager, checked against `state/cast_bible.md`). It runs a book of named pairs on real public issuers, with fictional positions and fictional P&L, labeled. Each chapter opens, adjusts, stress-tests, or closes one pair, using that chapter's tool. A running ledger (pairs, hedge ratios, idio share of P&L, what leaked) is kept in `state/rv_pair_book.md` and summarized in a new appendix. Every pair names its thesis, both legs, its hedge construction, the risk it intends to keep, the risks it must remove, and the way it can blow up.
3. **Canonical homes.**
   - Ch 8 (Stripping Beta to Isolate Pure IDO) owns the mechanics: spread-duration, DTS and empirical-beta hedge ratios; residualization against a factor model; the idio-share-of-P&L metric.
   - Ch 8-B owns the pod risk regime: factor-exposure limits, gross and net, drawdown stops, the center book.
   - Ch 8-C owns the pair P&L explain (carry, roll, convergence, factor residue, funding and borrow).
   - Ch 24 owns the bond-versus-CDS basis as the short leg.
   - Ch 28 owns pod economics and capacity.
   - A possible new chapter, **"The Pair Book: Long One Credit, Short Another"** (placement Part III, e.g. `08_ch08d_the_pair_book`): the craft and business of credit RV at a pod. The architect decides whether it earns a chapter or lives inside Ch 8.
4. **Per-chapter RV beats (draft, for the architect to sharpen).**
   - **Part I: the landscape.**
     - Ch 1: the pod as counterparty and competitor of the market maker.
     - Ch 2: electronification made both legs tradeable at scale (PT, ETF baskets, CDX).
     - Ch 3: the RSSG instinct as intra-capital-structure RV (long the fulcrum, short the junior; long secured, short unsecured).
     - Ch 1-B and Ch 4: life in the pod seat.
     - Ch 4-C: the pod's view of the shared bond.
   - **Part II: the math and statistics.**
     - Ch 4-B: hedge ratios from spread duration and DTS; curve pairs.
     - Ch 5: a pair's P&L is the difference of two jump processes, so tails are asymmetric (short one default, long another), and default correlation matters.
     - Ch 6: capital-structure arbitrage (equity or equity vol against CDS; CreditGrades).
     - Ch 6-B: P versus Q in a pair.
     - Ch 7: predicting the residual, not the spread.
     - Ch 7-B: cointegration and half-life of spread differentials; clustered residual regressions.
   - **Part III: the systematic toolkit.**
     - Ch 8: canonical home for the mechanics.
     - Ch 9: factor-neutral long/short, where the idio is what remains after factors.
     - Ch 10: residual momentum against TSMOM.
     - Ch 11: quality long/short within a ratings bucket.
     - Ch 12: cross-asset RV (CDX against HY ETF against loans).
   - **Part IV: restructuring and events.**
     - Ch 12-B and Ch 12-C: cap-structure pairs through Chapter 11 and plan valuation.
     - Ch 13: long the likely participant, short the likely excluded (and co-op dynamics).
     - Ch 14: sector pairs through a default wave; recovery RV.
     - Ch 15: long CoC-protected against short unprotected; acquirer against target.
     - Ch 16: claims against bonds; post-reorg equity pairs.
     - Ch 17: public proxy shorts against private marks.
   - **Part V: market structure and execution.**
     - Ch 18: legging risk and the two-leg execution cost.
     - Ch 19: pairs inside portfolio trades.
     - Ch 20: ETF against basket.
     - Ch 21: loan against bond of the same issuer.
     - Ch 22: borrow, repo and capital rules that make shorting credit hard.
   - **Parts VI–VIII: cross-asset, legal data, systems and the PM.**
     - Ch 23: equity vol against CDS.
     - Ch 24: the basis as the short leg.
     - Ch 25: weak-docs short against strong-docs long, from covenant NLP.
     - Ch 26: LLM pair screening.
     - Ch 27: pair infrastructure and legging.
     - Ch 28: pod economics and capacity.
   - **Appendices.**
     - App A: RV notation.
     - App B: data for pairs, including borrow and CDS.
     - App E: RV laws.
5. **Truths the thread must teach (not just assert):**
   - Shorting cash corporate bonds is expensive and sometimes impossible, so CDS, ETFs and CDX are often the real short leg, each with its own basis.
   - A hedge ratio is a model. Spread duration, DTS and empirical beta disagree most exactly when it matters.
   - "Idio" is defined relative to a factor model, and a wrong model turns factor bets into fake alpha.
   - Pairs carry asymmetric jump-to-default; carry, funding and borrow costs decide many pairs.
   - Pods pay for idio and penalize beta; stop-outs shape behavior.
   - Crowding: the same pairs across pods unwind together.
6. **Research (Sonnet, public sources only).**
   - Multi-manager platform structure and risk regimes as publicly described.
   - Credit RV, capital-structure arbitrage and pairs literature: Duarte, Longstaff and Yu (2007) on fixed-income arbitrage; Yu (2006) on capital-structure arbitrage; Ben Dor et al. (2007) on DTS; Asquith, Au, Covert and Pathak (2013) on bond borrowing.
   - Shorting bonds and borrow costs; CDS as the short; residual and idiosyncratic credit returns; crowding and pod unwinds (e.g. 2023–2025 multi-manager episodes as reported).
   - Specific podcast episodes and posts on credit RV.
7. **Execution (pipeline).**
   - Every brief, revise, lessons and new-chapter prompt reads `state/rv_thread.md` and must deliver the chapter's beat as a scene or a `> **The Pair.**` box, making the isolation logic explicit: what the hedge removes, what idio remains, and what leaks.
   - Chapters already revised get an `rv` stage after their lessons pass.
   - Figures: one RV figure per chapter where it teaches (pair spread differential, hedge-ratio decomposition, pair P&L attribution).
