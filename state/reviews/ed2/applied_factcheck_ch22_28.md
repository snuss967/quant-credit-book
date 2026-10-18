# Applied fact-check changes, Chapters 22-28 (Edition 2, WP1)

Source: `state/reviews/ed1/factcheck_ch22_28.md`. Started 2026-10-18. Edit tool only; each entry gives file, verdict class, before, after.

(Entries are appended below as edits are applied.)

Counts: 2 CORRECTED applied (report pairs 1 and 2); 0 STALE (report found none); 10 hedge edits for UNVERIFIABLE rows in range; 1 mirror edit in ch18 required by the report's note (outside the range, see section C). Total 13 net edits on 7 files (ch22 3, ch23 1, ch25 2, ch26 2, ch27 1, ch28 3, ch18 1). 15 Edit calls were made; one (ch27 "floated in 2022") was applied and then reverted after a web check, see D. Web calls: 1 (of 5 allowed). Every "find" string matched exactly once; no re-location was needed. The final `<!-- STATUS: COMPLETE -->` line is intact as the last line of all seven chapter files. Word counts after edits: ch22 15995 to 16002, ch23 15321 to 15332, ch25 14403 to 14411, ch26 14725 to 14733, ch27 16014 to 16016, ch28 17602 to 17619, ch18 13832 to 13834 (all under 0.2%).

## A. CORRECTED (2)

### A1. `book_src/22_ch22_market_structure_regulation_trends.md` line 310 (Table 22.1, one-minute-rule date label; report pair 1)
- Before: `| 2025-12-04 | One-minute reporting abandoned (approved, never effective) | Nothing. Use it as a placebo |`
- After: `| 2025-09-16 | One-minute reporting rescinded (SEC approved the rescission on 2025-09-16; FINRA announced it on 2025-12-04; the 2024 approval never took effect) | Nothing. Use it as a placebo |`
- Note: the row stays in date order (between 2024-05-28 and 2026-06-08). Other mentions of 2025-12-04 in ch22 (lines 235 and 838) refer to the date of FINRA Regulatory Notice 25-17, which is correct, and were left alone.

### A2. `book_src/26_ch26_ai_agents_and_llms_on_the_credit_desk.md` line 92 (Box 26-A timeline, SEC withdrawal date; report pair 2)
- Before: **Jun 17, 2025:** the SEC withdraws the proposal, with others from 2022–23 (Federal Register 2025-11110), saying
- After: **Jun 12, 2025:** the SEC withdraws the proposal, with others from 2022–23 (Release 33-11377; Federal Register 2025-11110), saying
- Note: the reference entry at line 862 cites the Federal Register document 2025-11110 at a URL dated 2025/06/17 (the publication date), which is consistent and was not changed.

## B. UNVERIFIABLE rows hedged (10)

### B1. `book_src/22_ch22_market_structure_regulation_trends.md` line 137 (Box 22-A, late-2024 Coalition Greenwich figure and quote; report refinement 8)
- Before: In late 2024 Coalition Greenwich already described dealers as short about \$3.8bn of IG corporates longer than five years, and the market as "agency (or at most, riskless principal)."
- After: In late 2024 Coalition Greenwich was already describing dealers as net short in longer-dated IG corporates *(late-2024 figure not independently verified)*.

### B2. `book_src/22_ch22_market_structure_regulation_trends.md` line 570 (Box 22-C, adoption date; hedge "adopted December 2023")
- Before: *Path:* adopted 2023-12-13 (cash 2025-12-31, repo 2026-06-30)
- After: *Path:* adopted December 2023 (cash 2025-12-31, repo 2026-06-30)
- Note: applied in the Trend Watch box only. The body text at line 498 still gives 2023-12-13 with the SEC press release 2023-247 cited in the references; the report rated the risk low, so a later pass may restore the day in the box.

### B3. `book_src/23_ch23_cross_asset_convexity_and_vol_surface.md` line 141 (Trend Watch, Blackstone attribution; report refinement 7)
- Before: Blackstone describes a default-probability model that uses "real-time equity market signals" (Blackstone_Systematic_Credit p.1)
- After: a summary of Blackstone's platform (an unsigned file, not a Blackstone publication) describes a default-probability model that uses "real-time equity market signals" (Blackstone_Systematic_Credit p.1)

### B4. `book_src/25_ch25_nlp_pacer_and_covenant_scraping.md` line 127 (Box 25-A, SPAC explanation untested; report hedge "probably reflects the SPAC wave")
- Before: The 2021 all-forms spike comes from the SPAC wave (S-4 and S-1 registrations), not from loans.
- After: The 2021 all-forms spike probably reflects the SPAC wave (S-4 and S-1 registrations), not loans.

### B5. `book_src/25_ch25_nlp_pacer_and_covenant_scraping.md` line 370 (Box 25-C, CourtListener count not reproducible; report's first suggested hedge)
- Before: returned a count of 1,868, with the newest hits dated September 2026.
- After: returned a count in the high hundreds to low thousands (1,868 on that day), with the newest hits dated September 2026.

### B6. `book_src/26_ch26_ai_agents_and_llms_on_the_credit_desk.md` line 101 (Box 26-A, Evident AI Index not found; report hedge, with "fifth" dropped)
- Before: **Oct 2026:** the fifth Evident AI Index ranks 50 banks, with JPMorganChase first.
- After: **Oct 2026:** Evident AI's October 2026 index again put JPMorganChase first *(50 banks ranked; edition number not independently verified)*.

### B7. `book_src/27_ch27_system_architecture_and_asics.md` line 96 (Box 27-A, Tradeweb AiEX share not found; report hedge)
- Before: Tradeweb's AiEX handled more than 40% of its institutional trades in 2025, against 30% in 2021 (Tradeweb 10-K, FY2025).
- After: Tradeweb says AiEX now handles a large and rising share of its institutional trades *(share not independently verified; Tradeweb 10-K, FY2025)*.

### B8. `book_src/28_ch28_pm_playbook.md` line 82 (Box 28-A, Point72 return and pod count not found; report hedge "reportedly")
- Before: Point72 returned 18% and had expanded to 190 pods per Bloomberg, and HFR
- After: Point72 reportedly returned about 18% and had expanded to 190 pods per Bloomberg *(not independently verified)*, and HFR

### B9. `book_src/28_ch28_pm_playbook.md` line 82 (Box 28-A, Goldman prime-insights and JPMorgan figures not found)
- Before: In September 2026 a Goldman Sachs prime-insights head said multi-strategy managers had attracted about \$500bn of additional assets over the past year, roughly 25% growth, while sector headcount rose only 10–11%, and cited a JPMorgan estimate of 645% average multi-strategy leverage (Hedgeweek, 15 September 2026).
- After: In September 2026 a Goldman Sachs prime-insights head was reported as saying that multi-strategy managers had attracted about \$500bn of additional assets over the past year, roughly 25% growth, while sector headcount rose only 10–11%, and as citing a JPMorgan estimate of 645% average multi-strategy leverage (Hedgeweek, 15 September 2026; industry estimates, not independently verified).
- Note: the report's suggested wording ("industry estimates put multi-strategy asset growth well ahead of headcount growth") would drop the figures, but the same box's "What it means" sentence ("about a quarter more capital chasing about a tenth more PMs") rests on them. An attribution hedge keeps the box coherent without touching that sentence.

### B10. `book_src/28_ch28_pm_playbook.md` line 314 (Box 28-B, sponsored-content label; Supplement row for Box 27-D, "keep the Cboe-sponsored label in both places")
- Before: overtook IBHY's for the first time (The DESK, 16 October 2026)
- After: overtook IBHY's for the first time (The DESK, 16 October 2026, Cboe-sponsored content)
- Note: ch27 line 690 already carries the label.

## C. Mirror edit outside the assigned range (1)

### C1. `book_src/18_ch18_otc_microstructure_and_avellaneda_stoikov.md` line 50 (Annotation block; report's Box 27-A note says any Tradeweb change "must be mirrored" here)
- Before: and Tradeweb's AiEX handled more than 40% of its institutional trades in 2025 (sources in Trend Watch, §18.7)
- After: and Tradeweb says AiEX now handles a large and rising share of its institutional trades (sources in Trend Watch, §18.7)
- Follow-up for the ch18-21 Trend Watch pass: the Trend Watch box at ch18 line 691 (§18.7) still states "Tradeweb's AiEX handled more than 40% of its institutional trades in 2025, against 30% in 2021 (Tradeweb 10-K, FY2025)". It is a ch18 box outside this range and was not edited; hedge it the same way (or verify the FY2025 10-K) so ch18 and ch27 agree. The Trumid 88% claim is also repeated in ch18 lines 50 and 691 and in ch27, and was not changed because the report gave no hedged wording.

## D. Applied, then reverted after a web check (net no change)

### D1. `book_src/27_ch27_system_architecture_and_asics.md` line 141 (Box 27-B, "floated in 2022"; report refinement 5)
- The report (UNVERIFIABLE, not found) suggested dropping "floated in 2022" unless a 2022 FINRA notice is located. The edit "was floated in 2022 and approved in 2024" to "was approved in 2024" was applied, then ch22 line 288 and the reference at line 841 were seen to cite FINRA Regulatory Notice 22-17 for the 2022 proposal. One web call (https://www.finra.org/rules-guidance/notices/22-17) confirmed it: published 2 August 2022, "FINRA Requests Comment on a Proposal to Shorten the Trade Reporting Timeframe ... From 15 Minutes to One Minute". The original wording is correct and was restored. Net change: none.

## E. Report items not applied, with reason

- Refinement 3 (ch22, "one June 2026 industry estimate" to "a June 2026 MarketAxess estimate"), refinement 4 (ch27, "MarketAxess estimated that duplicate affiliate trade reports ..."), refinement 6 (ch28, "to a January low of 2.64%"): the report's verdict for each is CONFIRMED with an attribution or wording nuance, not CORRECTED, STALE or UNVERIFIABLE, so they are outside the assigned classes. All three are accurate improvements and are ready to apply by find/replace from the report if the orchestrator wants them.
- CreditGrades hedge (ch23, "dealer-consortium product sold as a screen"): the row verdict is CONFIRMED (the unchecked part is "sold as a screen"); not in the assigned classes.
- Box 22-A "through end-June 2026" suggestion: CONFIRMED row; not applied.
- Box 23-C (Supplement), "add the outlet name" to the 2026 convertible-issuance figure: the report does not name the outlet, so it cannot be applied without inventing a source.
- Box 23-D (Supplement): the box already says "iCapital's ... Market Pulse dates the trigger to ...", so the hedge the report asks for is present.
- UNVERIFIABLE rows with no suggested wording (nothing to apply, left as written): Trumid 88%, Vanguard 70%, Coalition Greenwich survey and FILS Europe quote (ch27); HFR $5.15trn, Iran-war unwind, Fed FSR quote, Millennium drawdown rule, Clarus CDX, Cboe block trades, March 2026 TRACE/PT volumes, Moody's recovery figure (ch28); the ch26 timeline rows marked "not checked" (ChatGPT, BloombergGPT, Lopez-Lira, AI-washing, FINRA 24-09, FSB, BoE/FCA remainder, MCP, Stanford, Claude for Financial Services, FINRA 2026 report, Vals provenance, Acadian, Mata, Park); ch25 EDGAR cells not re-run, API cap, full-year 2025 cov-lite; ch22 no-further-delay line (it already says "check before relying on it"); and the unchecked Supplement boxes (22-D capital-rule dates, 22-E ICE release, 23-B, 24-C, 27-C).
- Watch items the report lists for before print (not edits): Treasury-clearing cash date 2026-12-31, Vals v1.1 versus v2, adding an H1 2026 sentence to ch24, FICC "more than $12 trillion" reconciliation, the ch24-C DC meetings dated 19 Oct 2026.

<!-- STATUS: COMPLETE -->
