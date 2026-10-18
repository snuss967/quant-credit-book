# Edition 2 Continuation Prompt

*Fable edition planner, 18 Oct 2026. Self-contained: an orchestrator that has read only this file, `state/PROCESS.md` and `state/style_bible.md` can run Edition 2. Inputs consolidated here: `state/reviews/ed1/{engagement,foundations,writer_returns,factcheck_*}.md`, `state/research/trend_*.md`, the Exploratory-space notes in `state/advisor_briefs/*.md`, and `SYSTEM_PROMPT.md` §3.*

## 0. Where Edition 1 left the book

28 chapters (13–19k words each, 471k words in `book_src/`), preface, eight Part openers, Appendices A–B, and a 3.1k-word Appendix C. The voice holds across independently written chapters (cast, catchphrases, ROBO's vague version, the 13-week-model arc). The four truncated chapters the reviews flagged (19, 24, 27, 28) were finished after the reviews were cut; all 28 now have a Desk Debrief.

What Edition 1 does not have, in the order the reviews rank it:

1. **A verified fact base.** Of about 520 Trend Watch claims checked, about 350 CONFIRMED, 16 CORRECTED, 4 STALE, about 156 UNVERIFIABLE; chapters 18–21 are still unchecked. Writers left about 60 CHECK-flagged facts in the text. Every reference implementation was written to run and never executed.
2. **The floor under the foundations.** Bond arithmetic, option pricing beyond the Merton formula, OLS/logistic/survival/shrinkage/PCA/bootstrap/Monte Carlo as methods, the bankruptcy and lien process, and market plumbing (settlement, margin, financing, ISDA events) are used from Chapter 1 and built, when built at all, in Chapters 8–24. Zero `> **Prerequisites.**` boxes exist. Ch 23 has zero `§` cross-references.
3. **One home per story.** Serta is told in 15 files, March 2020 in 19, April 2025 in 12, with no canonical home. Halvorsen has three lines of business. The cooperation-agreement counter runs 1, 0, 2, 2, 45, 0, overflow.
4. **Figures.** One image in 471k words. Chapter 12 is the only chapter with figures.
5. **Length.** Every chapter runs over its 8–12k brief; 290 source extractions is about 100 too many; "IDO or it didn't happen" appears 46 times; exercise counts run 0–24.

## 1. Theme and thesis

**Theme: "One Author, One Floor, One Home."** Edition 2 is the edition that makes 28 chapters by different hands read as one book by one author on a good night: every number sourced, every concept built once in the earliest place it is needed, every war story told once and seen through many lenses, and the TOC grown exactly where the research is thickest.

**Thesis.** The desk the reader is joining has changed in three ways since the book's shelf was written, and Edition 2 builds the chapters those changes demand: (a) **default became a negotiation** (distressed exchanges are two-thirds of defaults; courts turned contract tokens into regime switches; re-default is the base case), so Part IV needs an Autopsy Room and a restructuring-process primer; (b) **price became contested** (private marks versus listed prices, composite pricing as a benchmark asset, listed credit futures as the beta layer, hit-ratio-targeted dealer quoting), so Parts III–V need the marking, futures and RFQ-engine chapters; and (c) **the research base is under audit** (the bond-factor replication crisis), so Part III needs the data chapter that says which signals survive. Underneath all three sit the four primers the foundations review asked for.

**The user's priorities, which this plan obeys in order:** research and writing first; fun and intuitive; heavy focus on trends; TOC and exploratory space grow with research; quality over raw length (tighten, verify, cross-reference before adding pages); don't waste usage; code checking last.

## 2. Work packages, in priority order

Models: **Sonnet** (default researcher/editor) for fact application, research sweeps and mechanical edits; **Opus** for new chapters, rewrites and scenes; **Fable** only for short judgment passes over prepared material (briefs from dossiers, mapping, reviews). Sizes are relative usage: S ≈ one lean agent-hour, M ≈ 3–5, L ≈ 10+.

### WP1. Apply fact-check corrections (Sonnet, S) — first, before any chapter is touched

Scope:
- Apply every CORRECTED and STALE row in `state/reviews/ed1/factcheck_ch01_07.md` (7 corrected, 2 stale, with find/replace pairs C1–C5, S1–S2), `factcheck_ch08_14.md` (4 corrected: CCC OAS date mismatch Box 12.2; SG Trend "only twice" Box 10.2; "25 trading days" Box 12.4; MacKay quote wording), `factcheck_ch15_21.md` (3 corrected: HSR "transactions" not "filings" twice, vacatur date attribution; 2 stale: UP/NS STB refiling, FTX fifth distribution), `factcheck_ch22_28.md` (2 corrected: one-minute-rule date labels in Table 22.1; SEC withdrawal 12 Jun 2025 not 17 Jun).
- Finish the pending fact-check of chapters 18–21 Trend Watch boxes (Sonnet, same format, ≤40 web calls) and apply its rows.
- Apply the writers' own technical corrections from `writer_returns.md`: Ch 16's rule that jump-to-default enters a market-spot warrant or call price through $r+\lambda$, not an $e^{-\lambda T}$ haircut (grep every chapter that applies the haircut to a market spot); 503(b)(9)/GUC is *long* pool uncertainty near par; Hertz warrant implied vol 23–25% at the \$13.80 basis; Ch 3 §3.1 the $\mathbb{Q}$ (line 41) vs $\mathbb{P}$ (line 104) inconsistency.
- Resolve the CHECK-flagged facts the writers listed (one Sonnet researcher per Part, primary sources only, ≤25 web calls each); where a fact cannot be confirmed, keep the hedge and add *(approx.; source: …)* per the style bible, never delete the hedge.
- Do not change prose beyond the corrected clause.

Acceptance: `state/reviews/ed2/factcheck_applied.md` lists every CORRECTED/STALE row with `file:line` of the applied diff; `grep -c CHECK book_src/*.md` falls by at least half; `python3 tools/check_book.py` passes; no chapter's word count changes by more than 1%.

### WP2. Foundation primers and prerequisite boxes (Opus for the primers; Sonnet for boxes and back-references; M+L)

Build each concept once, in the earliest place a reader needs it, in the book's voice; make every later use a one-line back-reference.

2a. **Four primer chapters** (Opus, L total; 8–11k words each, hard cap 12k; full anatomy; each ships a module the later chapters import):
- `04_ch04b_bond_math_for_the_desk.md` — price–yield, Macaulay/modified/spread duration, convexity (and the three meanings of the word), DV01/CS01, key-rate duration, clean/dirty and day counts, G/I/Z/OAS/DM/YTW/asset-swap/par-CDS from one curve, a minimal callable-bond lattice so OAS and make-whole are computed; `bondmath.py`. Case: the Ch 1 §1.4 fallen angel repriced in every spread measure.
- `06_ch06b_options_and_measures_for_credit.md` — replication and the BS PDE in book notation, Greeks as risk-report lines, implied vol and skew, Merton with jump-to-default so Carr–Wu (§23.3) is a corollary, and the full $\mathbb{P}\to\mathbb{Q}$ section for intensities (hazard multiplier, the premium ratio as a traded quantity, the "say which measure" rule); `credit_options.py`. Becomes the single home for "CCC is an equity option", "HY is a short put", the CoC put, portability as a digital, backstops and warrants, the loan call, the OC test as an option book.
- `07_ch07b_statistics_for_credit_panels.md` — OLS/panel with issuer clustering, overlapping returns, Newey–West; logistic regression and calibration; survival in the right order (censoring, S/F/h, Kaplan–Meier, Cox PH, pointer to competing risks §14.2); covariance (EWMA, Ledoit–Wolf, factor covariance, PCA on a residual panel); block/stationary bootstrap; Monte Carlo as a method (standard error, variance reduction, discretisation, Brownian-bridge first-passage correction); tree ensembles in one section; `creditstats.py`.
- `12_ch12b_the_restructuring_process_as_a_state_machine.md` — which document governs which right (indenture, credit agreement, intercreditor, security agreement); lien vs payment subordination; amendment thresholds and sacred rights; the out-of-court menu as transitions; Chapter 11 as a timed state machine (petition, stay, first days, DIP and roll-ups, 363, exclusivity, disclosure statement, classes, voting, §1129, cramdown, APR, effective date); fulcrum and plan value defined once; claims mechanics (503(b)(9), GUC, 3001(e)); `restructuring_state_machine.py`. The Part IV opener begins "read 12-B first."

2b. **Two reference appendices** (Sonnet drafts, Opus polish, M): `93_appD_market_plumbing_and_contract_mechanics.md` (settlement cycles and fails for bonds/loans/CDS/ETFs; clearing and IM/VM; repo, haircuts and the funding leg; ISDA credit events, the DC, the auction, CTD and deliverables, succession and orphaning: tables, not narrative) and `94_appE_laws_of_the_desk.md` (the 16 laws from `foundations.md` §5, each with statement, equation, and section index; every Desk Debrief tags its bullets with law numbers).

2c. **Prerequisite boxes and reading-order fixes** (Sonnet, M): add `> **Prerequisites.**` boxes at the 20 locations in `foundations.md` §3.3; add "(built in §x.y)" tags to Ch 1 §1.3–1.4; reduce §9.2 to a back-reference to §8.4 (DTS built once); §24.2 keeps conventions and back-references §6.8 (CDS pricing built once); §14.7 imports the filter from §12.4; §2.2 and §18.8 point at each other; §14.2 opens "competing risks extend 7-B"; §15.5 keeps only the regulatory-clock application; §16.2 and §11.6 forward-reference §21.4; Ch 23 gets `§` cross-references throughout; App A §A.3 gains the six collisions (bootstrap, Kelly, logistic, convexity, $t+1$/T+1, duration) and the "measure of every expectation" rule; the preface gains the Laws list and a prerequisite-box legend.

Acceptance: `state/foundations_map.md` lists every concept in `foundations.md` §2 with exactly one "built in" section; `grep -c "Prerequisites\.\*\*" book_src/*.md` ≥ 20 across ≥ 14 files; Ch 23 has ≥ 15 `§` references; the four primers import-test clean in a single interpreter (`python3 tools/check_book.py --run-code` on those four files only is permitted here, since the later chapters import them); no primer exceeds 12k words.

### WP3. Canonical case-study homes and de-duplication (Sonnet for the trims; Opus for the issuer bible and Docket Diaries; M)

- Adopt the canonical-home table in `engagement.md` §3 verbatim. For each case, the canonical section gets (or keeps) a dated, sourced Docket Diary in the Hertz §16.6 format; every other chapter keeps only its named lens plus "see §X.Y" and loses the retold timeline. Serta → §13.3.1 (Docket Diary moved from §14.8.1); J.Crew → §13.6; Hertz → §16.6; March 2020 → §20.5; April 2025 → §10.7 Coda; SVB → §6.4.4; Mitel → §14.8.2; Carvana → §6.10.1; First Brands/Tricolor → §12.9B; CS AT1/Altice → §18.6.3; Windstream → §25.5.2; ConvergeOne → §16.3; Spirit → §16.7; GM/Ford 2005 → Ch 23 A; Knight → §26.11. Incora, Boardriders, Envision, Robertshaw, Hovnanian get homes in 13-B and Ch 24 (WP4/WP5).
- **Fictional-issuer bible** appended to `state/style_bible.md` (Opus, S): Halvorsen (one sponsor, one capital structure, one set of document trapdoors, the Serta blocker it does or does not have), Brambleworth, Larkspur Foam; then make Halvorsen consistent in Ch 1, 2, 18, 24 so "The Halvorsen Files" runs RFQ → uptier → basis → post-reorg.
- **Running-gag repairs:** cooperation-agreement counter sequence (0 in Ch 1–2; 1 after Ch 3; 2 and 3 in Ch 13; "overflowed" from Ch 14; payoff in Ch 28: Theo signs one); "IDO or it didn't happen" capped at once per chapter, in the Debrief; "open market purchase" gets its Dec 31 2024 payoff in Ch 14 and is retired by the Ad Hoc Group in Ch 28; Kaz's legal misreadings added in Ch 15, 16, 21, 22.
- Cull source extractions from 290 to about 190: keep every extraction whose annotation disagrees with or extends the source; drop those that merely restate it.
- Add `## Cold Open: Title` labels to the 23 chapters that lack them.

Acceptance: each case's dated timeline (three or more dated lines) appears in exactly one file (grep on the case's key dates); every non-canonical mention carries a `§` cross-reference; `grep -c "IDO or it didn" book_src/*.md` ≤ 1 per file; the counter is monotone in reading order; `grep -c "SOURCE EXTRACTION" book_src/*.md | awk` total ≤ 200; Halvorsen has one coupon, one maturity and one business.

### WP4. New chapters (Fable brief from dossier, S each; Opus chapter, L total)

Per `SYSTEM_PROMPT.md` §3 growth rule; the full list with scopes is in §3's "Edition 2 additions." Order of writing (research-readiness first):

1. `09_ch09b_the_bond_data_problem_and_the_replication_crisis.md` (TREND) — needs `papers/factor_replication_crisis_and_bond_data`.
2. `13_ch13b_the_autopsy_room_lmt_docket_diaries.md` — needs `case/lmt_autopsies_us_2020_2026`, `case/lmt_private_and_european_2024_2026`, `case/courts_as_regime_variables`.
3. `17_ch17b_marking_the_unmarked_private_credit_lmes.md` (TREND) — needs `trend/private_credit_marks_and_redemptions_2025_2026`.
4. `18_ch18b_the_rfq_response_engine.md` — needs `papers/rfq_quoting_frontier_2025_2026`, `trend/part_v_market_structure_2026`.
5. `10_ch10b_credit_index_futures_and_index_microstructure.md` (TREND) — needs `trend/listed_credit_futures_and_index_microstructure`.
6. The four primers of WP2a and the two appendices of WP2b (they are new files too; listed there because they gate the back-references).
7. `00_01_tape_to_your_monitor.md` (front matter; Sonnet harvest, Fable 20-minute selection pass): the forty best Debrief bullets grouped by Part, plus the issuer bible's one-page summary.

Each new chapter's brief is a Fable short pass (≤ 30 minutes, no web) over the named dossier plus the engagement and foundations reviews, in the Edition 1 brief format.

Acceptance per chapter: 8–11k words (hard cap 12k); cold open ≤ 400 words labelled `## Cold Open:`; the six anatomy elements; ≥ 1 Trend Watch with dated, sourced figures; ≥ 1 figure script in `figures/`; a Prerequisites box; a Trade of the Chapter box (Parts III–VI); a Debrief written as a scene plus 5–8 bullets tagged with law numbers; 4–6 exercises; no retelling of a canonical case beyond one sentence and a `§`; ends with `<!-- STATUS: COMPLETE -->`; recorded in `SYSTEM_PROMPT.md` §3 and `book_state.json["toc"]`.

### WP5. Targeted expansions (Opus, M; Sonnet for App C rows and figure scripts)

Ranked; stop when the usage window says so.

1. **Figures, one per chapter** (the cheapest engagement fix): the list in `engagement.md` §5, written as `figures/chNN_<slug>.py` (matplotlib, reproducible from the chapter's own numbers or FRED series named in `trend/figure_data_series`) with a caption and `![…](figures/chNN_<slug>.png)` in the text. The orchestrator renders them centrally in one run; a script that fails is deferred to WP7, not debugged by the writer.
2. **Ch 14**: open §14.2 on the Dec 31 2024 same-day Serta/Mitel rulings (its own Docket Diary); §14.3 fits the re-default clock to the hand-built LME→outcome dataset (`trend/re_default_and_recovery_dataset`); add the two-hump recovery figure; Spirit's second filing as the re-default clock on a public equity.
3. **Ch 23**: Case Study B (SVB vol-surface lens, cross-referencing §6.4.4), Case Study C (Carvana 2023 cap-arb squeeze), Wolfspeed 2025 as "one distribution, many strikes"; `§` cross-references throughout (`case/carvana_svb_wolfspeed_capital_structure`).
4. **Ch 24**: verify coverage of Codere 2013, Hovnanian 2018, Sears 2019 and the Altice France 300/5 no-auction outcome; fill gaps as Docket Diaries; Windstream manufactured-event lens cross-referencing §25.5.2 (`case/manufactured_credit_events`).
5. **Ch 17 §17.6**: Trend Watch on the 2025–26 stress series (BDC non-accruals at cost vs fair value, redemption-request percentages, First Brands/Tricolor dates), cross-referencing 17-B.
6. **Ch 20**: "The Basket Triangle" section: arbitrage bands linking creation/redemption, portfolio trades and credit index futures, with custom-basket availability as the state variable; reconcile the AP band with §21.6's $d^*$.
7. **Ch 22**: the TOC-promised Basel III endgame and CDS clearing sections; "the customer's regulator" section (NAIC CLO C-1 factors YE2026, SVO discretion Aug 2026, PBBD, Solvency II) as forced-flow generators (`trend/insurance_capital_forced_flow`); wire `REGIME_DATES` into App C.
8. **Ch 27**: the Citi/Revlon \$900mm wire and the May 2022 Citi fat finger next to Knight Capital in the kill-switch section.
9. **Ch 2**: "What Electronic Means" denominator table and "2026: Consolidation Year" (ICE–MarketAxess, monthly data going dark) as one Trend Watch each; move the Data-Exhaust Theorem's one-line result into the opening.
10. **Ch 11**: "The CCC tier as its own asset class" section (CCC/HY OAS ratio regime, CLO bucket flows, PD-sorted selection within CCC), cross-referencing §21.4 and Ch 28's Box C.
11. **Ch 13 §13.9**: becomes a one-page pointer into 13-B; §13.2 opens with the document map from 12-B and names the intercreditor agreement.
12. **App C**: grow from the 3.1k-word megatrend summary into the dated, sourced row table (one line per Trend Watch box, now about 74), with the blocker-adoption, regulatory-regime, LMT-ruling and private-credit threads the briefs asked for.
13. **New recurring formats** (style bible first, then inserts): Trade of the Chapter (Parts III–VI), Hand-History Replay table (every case study in Parts I, III, V), Fourteen-Sigma Tuesday risk report at each Part boundary, Price This RFQ in Fifteen Seconds (Part V openers), Spot the Trapdoor exercises (Part IV, Ch 25).
14. **Debrief scenes** (150 words before the bullets) for the eleven bullet-only chapters: 1, 2, 4, 6, 8, 10, 13, 14, 15, 16, 18.

Acceptance: every chapter has ≥ 1 rendered figure; App C has ≥ 70 dated rows with sources; each expansion is net-neutral or negative on chapter length (pair every addition with a WP6 cut in the same file); Trend Watch boxes added carry dates and sources or are not added.

### WP6. Tightening passes (Sonnet for trims from the writers' own cut lists; Opus for the five restructures; M)

- Bring every Edition 1 chapter to ≤ 15k words total and ≤ 12k words of prose, using the writers' own candidates in `writer_returns.md` (e.g. Ch 1 §1.4/§1.6; Ch 2 §2.5/§2.7/§2.8; Ch 5 §5.4 to a verdict and §5.9 blocks 4–5 to an appendix; Ch 6 §6.7 CIR closed form to an appendix; Ch 8 Case A to §10.7C and exercises to eight; Ch 9 §9.3/§9.6; Ch 12 §12.4 −1k; Ch 16 §16.2.3 −2k; Ch 17 §17.5 to a table; Ch 21 §21.2.3/§21.6; Ch 26 exercises to ten).
- Five restructures (Opus): Ch 1 §1.1 to 300 words and the "epistemological clash" to the preface; Ch 2 revolutions 2+3 merged; Ch 4 §4.3 and §4.11 to a table and a diagram; Ch 11's five spec blocks to one shared engine; Ch 15's three spec blocks to one engine at the end.
- Standardize exercises at 4–6; Debrief bullets at 5–8; one ROBO vague version per spec box.
- Move the cut code (not deleted) to `book_src/9X_app*` companions or `figures/` so nothing executable is lost.

Acceptance: `wc -w` ≤ 15,000 for every `NN_chNN_*.md`; `tools/check_book.py` reports all six anatomy elements per chapter; exercise count 4–6 in every chapter; total book length does not grow by more than the new chapters' own words.

### WP7. Code cleanup, last (Sonnet, M)

Run `python3 tools/check_book.py --run-code` per file in one interpreter per chapter; fix failing asserts starting with the ones the writers named as riskiest (Ch 2 check (b); Ch 7 block-6 DSR; Ch 10 blocks 3–4; Ch 11 blocks 3 and 5; Ch 13 stochastic asserts; Ch 14, 16, 19, 20, 21, 24 named blocks); render any figure scripts deferred from WP5. Never change a result the prose quotes without updating the prose.

Acceptance: every chapter's Python runs clean; `state/reviews/ed2/code_ledger.md` lists each block's status.

## 3. Sequencing, concurrency and usage

- **Order:** WP1 → (WP2a primers ∥ research queue) → WP2c/WP3 (mechanical, Sonnet, can overlap with primers) → WP4 chapters as their dossiers complete → WP5 → WP6 → WP7. The reviews (Stage 4) run per Part once a Part's new chapters exist.
- **Research first, in parallel with WP1:** launch `state/research_queue_ed2.json` (13 items, Sonnet, ≤ 40 web calls each, primary sources, dated evidence tables, `<!-- STATUS: COMPLETE -->`). A Fable mapper closes each batch in a short pass and updates `state/exploratory_space.md`.
- **Fable budget:** this plan; 11 short briefs (new chapters and appendices); 2–3 mapper passes; the engagement and foundations reviews per Part at the end; the Edition 3 plan. No Fable web research.
- **Usage sizes:** WP1 S; WP2 L (four Opus primers) + M (Sonnet boxes); WP3 M; WP4 L (five Opus chapters + front matter); WP5 M–L (figures are many small Sonnet tasks); WP6 M; WP7 M. Run wide on Opus writers (about 8) with `pace_guard.py --cap-only --target 97`; stop launching at the alarm; everything is resume-safe by file.
- **Durability:** every agent creates its file within its first few calls and ends with `<!-- STATUS: COMPLETE -->`; relaunch from `tools/status.py --json`, never from memory.

## 4. Ship criteria for Edition 2

1. WP1–WP4 complete; WP5 items 1–7 complete; WP6 complete for every chapter that WP5 touched; WP7 at least for the four primers and the new chapters.
2. `SYSTEM_PROMPT.md` §3 and `book_state.json["toc"]` list every new file; `CHANGELOG.md` has the Edition 2 entry filled in; the build passes; one tagged commit "Ship Edition 2".
3. Edition 3 planning inputs exist: `state/reviews/ed2/*`, updated `state/exploratory_space.md`, writer returns consolidated.



## USER DIRECTIVES, TOP PRIORITY FOR EDITION 2 (2026-10-18)

Read `state/user_directives_ed2.md` and the "Edition 2 Voice Amendments" in `state/style_bible.md` before any work. They add to WP1–WP7 and remove nothing. Order of work after the restart:
1. **Finish the in-flight work.** Run the reader-lens synthesis plus its 4 new chapters (their writers must follow the voice amendments), finish primers 04_ch04b, 07_ch07b and 12_ch12b, and run the remaining research.
2. **U3, media and perspectives research (Sonnet):** specific podcast episodes and blog posts per chapter; public perspectives of Apollo, Ares, DE Shaw, Oaktree, Jefferies, BofA and others; public accounts of quant-shop life.
3. **U1, code explanations (Sonnet):** replace every `<!-- EXPLAIN -->` stub. Re-run `python3 tools/move_code_to_companion.py --apply` first, to sweep any code that new writers added.
4. **New chapters 01_ch01b and 04_ch04c (Opus,** each from a short Fable brief built on the U3 dossiers).
5. **U2, narrative revision, chapter by chapter (a short Fable brief, then Opus),** starting with Ch 1–7 (the book's on-ramp), then Part IV (the RSSG reader's home turf).
6. **U4, figures (Sonnet with Python scripts),** at least 3 per chapter.
7. Then WP3–WP7 as planned.

## Resume Checklist (paused 2026-10-18 01:30 UTC at ~92% usage; scheduled restart 04:17 UTC)

Run `python3 tools/status.py` first. Workflow scripts live in ~/.claude/projects/-home-user-quant-credit-book/6416563a-50d0-5129-a66c-5b16ba7386c8/workflows/scripts/.
1. **Synthesis and new chapters.** The three reader-lens reviews are COMPLETE in state/reviews/ed2/. Resume the reader-lens workflow so the cached reviews replay and the Fable synthesis runs live, followed by the 4 Opus writers: `Workflow({scriptPath: ".../ed2-reader-lens-reviews-wf_aa7ed3ed-60e.js", resumeFromRunId: "wf_aa7ed3ed-60e"})`.
2. **Finish the primers.** 04_ch04b, 07_ch07b and 12_ch12b are PARTIAL. Run `ed2-wp2-primers-wf_a9d1dfae-4df.js` with those three stems. Writers resume and append; they never rewrite.
3. **Research, on Sonnet with no Fable mapper.** Run `research-resilient-wf_bd451f4f-5fb.js` with `model: "sonnet"` and `no_map: true` for the PARTIAL or MISSING slugs in state/research_queue_ed2.json: case_lmt_private_and_european_2024_2026, case_courts_as_regime_variables, trend_re_default_and_recovery_dataset, trend_private_credit_marks_and_redemptions_2025_2026, trend_listed_credit_futures_and_index_microstructure, trend_part_v_market_structure_2026, case_carvana_svb_wolfspeed_capital_structure, case_manufactured_credit_events, trend_insurance_capital_forced_flow, trend_figure_data_series.
4. **Then WP3 onward**, in this file's package order: canonical homes, the WP4 new chapters from the synthesis, WP5 figures, WP6 tightening, and WP7 code last.
5. **Pacing.** Recalibrate the meter once the user gives a reading (`tools/usage_meter.py --window-start 2026-10-18T04:30:00+00:00 --calibrate PCT AT`). Run `pace_guard.py --target 97 --cap-only`. Fable handles judgment only; bulk research goes to Sonnet; Opus writers stay lean.

## Edition 2 addendum (reader-lens reviews, 2026-10-18)

Source: `state/reviews/ed2/synthesis.md` (the deduplicated, ranked master list in four layers, with actions and costs), built from `review_rssg_partner.md`, `review_desk_head.md` and `review_transition_coach.md`. The user directives still outrank it; nothing is removed. Appendix F is the Code Companion and stays; new appendices take letters G onward and App Z is reserved for solutions; the transition coach's "getting the seat" chapter is **4-D** (`04_ch04d`), since 4-C is the user's "other seats at the table". The eight endorsed files are in `SYSTEM_PROMPT.md` §3 ("Edition 2 additions", end of the subsection) and `book_state.json["expansion_queue"]`.

New work, in priority order:

1. **Write the TOP 4 now (Opus, from the briefs in `state/advisor_briefs/`; each writer follows the Voice Amendments):** `03_ch03b_your_first_year_on_the_desk`, `12_ch12c_plan_valuation_dip_and_exit_as_derivatives`, `08_ch08b_the_risk_model_and_the_limit_sheet`, `08_ch08c_the_morning_explain_pnl_attribution` (8-B before 8-C if not in parallel; 8-C imports `risk_model.py`). None waits on a PARTIAL dossier.
2. **Plumbing fix before any new module ships (Sonnet, S):** `book_src/lib/` on `sys.path` in `tools/check_book.py`; document in App F and `README.md`; a Model Inventory table at the head of App F.
3. **Scope additions to in-flight files (Opus, M):** 12-B intercreditor mechanics, Required-Lenders denominator, the fulcrum defined once, the Purdue node; 13-B's RSA/TSA diary, the Passport forum table, the Purdue jump, Incora dates reconciled.
4. **Section-level additions (Opus, M each; see synthesis §1):** §3.6.3 walls and the cleansing 8-K; §13.5.2 co-op economics and PRS covariates; §8.6 hedging as an operation; §9.8 constraints that bind; Ch 16 §16.9 the claims desk (+ App D rows); Ch 27 §27.9 from notebook to blotter; App A §A.10 dictionary and §A.11 Statute Block; §28.9 panels and the Sharpe input; Part gates; the make-whole circuit-split table (§15.1/§16.6).
5. **Red-pen fixes (Sonnet, one pass per file; synthesis §5):** App A §A.9 cram-up and APR; §13.3.1, §13.2, §13.9/§14.6 dates; §16.1.1, §16.6 leg 1; §25.8; §5.5.1; §12.5 rho; §26.8, §26.9; §28.8; §3.5 (rows, Ch 25→26 reference); §27.4, §27.8; §1.1 and §4.1 tables; preface and Part I opener; README.
6. **Learning-path files, after the primers are COMPLETE and U3 lands (Opus):** `00_02_how_to_use_this_book`, `04_ch04d_getting_the_seat` (with the twelve-project Portfolio), then `02_ch02b_transaction_cost_analysis_for_credit` after 18-B.
7. **App Z solutions (Sonnet drafts, Opus checks; staged):** primers and Part I first; the rest after WP6 stabilizes the exercise sets; retrofit exercise tags and "Check:" parentheticals in the same pass.
8. **Deferred to Edition 3 (record in `state/exploratory_space.md` §2 at the next mapper pass):** 27-B research-to-production, 16-B the claims desk, the Forum Atlas and Tax Line appendices, the Portfolio appendix, the Statute Block appendix; each has an interim home above.

Scope notes for the user-specified chapters (synthesis §4): 1-B is a five-shop ethnography with a different composite per shop and one View From Another Seat box per week on the Halvorsen bond; it shows the risk pack and the explain from the corridor and does not teach them. 4-C is one bond through seven seats and closes by noting that the seats become 12-B's classes and 12-C's DIP lender, backstop party and claims fund; its dealer seat hands off to 18-B and its systematic seat to 8-B.

<!-- STATUS: COMPLETE -->
