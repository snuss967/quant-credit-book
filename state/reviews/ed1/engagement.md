# Edition 1 Engagement Review

*Fable Engagement Advisor, 18 Oct 2026. Inputs: `state/style_bible.md`, `state/digests/ed1_review_digest.md`, the TOC in `SYSTEM_PROMPT.md`, corpus-wide `grep` counts over `book_src/`, and eight sampled sections (Ch 5 cold open; Ch 1 §1.1; Ch 13 opening and §13.1; Ch 18 §18.4; Ch 16 §16.6; Ch 19 tail; Ch 24 opening and §24.1; Ch 28 opening). No whole chapters were read and no web research was done. Word counts below are live `wc -w` figures, which differ from the digest for Ch 19–24 and 28 because those files grew after the digest was cut.*

**Headline.** The voice is real and it holds across 400k words written by independent writers: the cast is consistent (Theo 349 mentions in 36 files, Kaz 270, ROBO 248, Ines 196, Mags 137), the catchphrases land, and the best cold opens (Ch 5, 13, 24, 28) are as good as the style bible's calibration sample. The book is *fun where it is finished*. The engagement problems are structural, not tonal: (1) seven chapters are unfinished or stop before their Desk Debrief (19, 20, 21, 22, 23, 24, 27, 28: no Debrief in 19–24; 24, 27, 28 are 4k-word stubs), so Part V and Part VI, the parts a market maker would read first, currently end mid-sentence; (2) the book has essentially **no figures** (the only "figure" hits are prose mentions; zero images, zero mermaid/SVG blocks in 400k words), which is the single cheapest engagement fix available; (3) the same war stories are told in several chapters at different lengths (Serta in 15 files, March 2020 in 19, April 2025 in 12) with no canonical home and no cross-references, so a cover-to-cover reader meets the Serta timeline five times; (4) two running gags have broken continuity (the cooperation-agreement counter, and the fictional issuer "Halvorsen" who has three different lines of business). Fix those four and the book reads like one author on a good night.

---

## 1. What's Working: Keep and Amplify

**The cold opens that end on a question.** Ch 5 "The Fourteen-Sigma Tuesday" is the template: 350 words, every cast member gets one line that is also their thesis, ROBO's literalism is a punchline *and* a lesson (minimizing kurtosis by buying bills), and it ends on the chapter's question in bold. Ch 13 (Larkspur Foam, the Serta-blocker-is-a-mattress-protector exchange, the Ad Hoc Group speaking offstage "we neither confirm nor deny that we exist; we hold 51.3%") and Ch 24 (the sticky-note basis trade, "is a deliverable obligation the one with free shipping?", Ines's "which one of them is lying") are equally strong. Ch 28's "Keys to the Table" opens on a real dated FRED print (15 Oct 2026, HY 323 bp, CCC 1,278 bp: "the index looks bored; its basement is on fire") and that is the right move: a real number anchors the fiction. **Amplify:** label every scene `## Cold Open: Title` (only 15 of 28 files use the heading; Ch 1, 2, 3, 4, 13, 14, 18 have scenes but no label, and Ch 19–24 have neither), and make the Ch 5 pattern (one line per cast member, ROBO's vague-spec disaster, bold question) the hard template.

**Desk Debriefs written as scenes, not lists.** The best debriefs replay the cold open a week later with the numbers fixed (Ch 3: "You were second. Second is not a strategy"; Ch 7: Kaz's AUC falling from 0.61 to 0.52 under purged CV, "it's mostly carry and one company"; Ch 9: "Yours has a cost model and a lawyer. Fine. Yours is better than the guy"; Ch 17: the hand replayed through markouts, "right about the direction and wrong about the ratio"). These are the emotional payoff of the chapter formula and they are where the running gags earn their keep. Chapters whose debriefs are bullet-only (1, 2, 4, 6, 8, 10, 13, 14, 15, 16, 18) should get a 150-word scene before the bullets.

**Bullets sharp enough to tape to a monitor.** The debriefs already contain the best lines in the book, and they should be harvested for a front-matter "Tape to Your Monitor" page: "Eleven anchored dealers are worth about two"; "Forty-seven bonds of one issuer are one bet with forty-seven CUSIPs"; "Skew is minus one over root PD"; "A bid is a posterior, not a markup"; "A quote is five numbers, not one"; "There is no 4 p.m. in credit"; "Roll returning NaN is information"; "A distressed exchange is parole, not immunity"; "Recovery is two humps"; "A citation that cannot be checked is a hallucination with a footnote"; "The most expensive three words have a cousin: defease certain obligations"; "Private credit is public credit with the price removed."

**ROBO's vague version.** The "what ROBO built from the vague spec" device appears in 28 files (56 hits) and is the book's most reliable joke-that-teaches: "minimize the mark gap" ends with ROBO writing to the valuation committee to cut the fee base 10%; "build an RFQ auto-quoter" ends with ROBO bidding par for everything and "owning the bond market by Thursday"; "maximize Sharpe" finds a matrix-priced bond with Sharpe 11. Keep it mandatory, one per Spec box.

**The 13-week model arc.** 81 hits across 29 files with a genuine character arc: emotional support (Ch 1), gets a job (§3.1.4), reborn as a hazard rate (§5.1.5), industrialized (§6.8.1), a vertical barrier and primary model (Ch 7), a covariate capped at 13 "taking the demotion well" (Ch 11), the builder basket (§25.3.5), and the PM dashboard (Ch 28, promised in the Part VIII opener but not yet written). This is the book's spine; the payoff must be written.

**Source extractions with annotations.** 290 extractions in 29 files, and the annotations are consistently better than the quotes ("this is the founding argument of the basis, and the rest of the chapter is a list of the ways it fails"). Keep.

**The Hertz Docket Diary (§16.6).** The best single case-study block in the book: dated, sourced, every leg mapped to an instrument in the chapter, the Ad Hoc Group's closing remark ("in 2021 it was unimpaired, which is how it lost its vote and found its lawsuit"), and a 2026 coda that brings PJT back into the room. This is the canonical-home format every recurring case should adopt.

**Devices with good coverage:** Ways This Blows Up (64 in 26 files), Trend Watch (48 in 16), Desk Myth vs Reality (27 in 24), Poker Table (29 in 21), "back in my day" (35 in 26), "hand history" (54 in 27). Docket Diary is under-used (12 in 11 files) given that Part IV is the book's selling point.

## 2. Where It Drags: By Chapter, With Fixes

**Ch 1 (13.0k).** The cold open (Halvorsen RFQ, 00:14 countdown, bonds open Monday at 78) is excellent. §1.1 then collapses into pitch-deck prose: "Walk onto the restructuring floor at PJT Partners in Midtown... now walk onto the market-making floor at Susquehanna in Bala Cynwyd," followed by a three-term bid equation before the reader has met Bayes, and "pure quantitative researchers trained in equity stat-arb fail in distressed credit." It names real firms in a speculative register the style bible forbids, and it tells the reader the thesis instead of showing it. **Fix:** cut §1.1 to 300 words that point at the three-term table (which is good) and move the "epistemological clash" into the Preface. Replace the "Hybrid Owns the Future" subsection with one Poker Table box. The anthology sections (1.4 onward) need a figure: the forced-seller flow graph the chapter promises is currently prose plus a Monte Carlo; draw it.

**Ch 2 (16.3k).** Six "Revolutions" in a row is a listicle. The Data-Exhaust Theorem (§2.9) is the payoff and arrives 14k words in. **Fix:** move the theorem's one-line result ($\alpha^{\text{net}\star}\propto 1/c$) into the opening and treat the six revolutions as the evidence; compress Revolutions 2 and 3 (all-to-all and automation) into one section; add one figure: protocol share 2018–2026 with the ETF–NAV basis overlaid as the regime switch.

**Ch 3 (17.8k).** Strong throughout; the Brambleworth hand (85¾, lender call Monday) is the best worked example in Part I. **Drag:** §3.4 (the Bayesian 8-K) and §3.5 (the Edge Ledger) are two essays where one would do. **Fix:** fold the Edge Ledger into a one-page table and give the saved space to a hand-history replay figure (price path with the 1/5/20-day markout markers).

**Ch 4 (14.4k).** The six-axis framework map and the genealogy are reference material and read like it. **Fix:** turn §4.3 into a single annotated table and §4.11 into a one-page diagram ("the empty cells"), and let the two case studies (the factor zoo audit; Man Numeric's execution migration) carry the chapter. Only two Trend Watch boxes in a TREND chapter: add one on AUM 2018–2026.

**Ch 5–7 (18.2k, 16.2k, 17.2k).** These are the book's best-paced technical chapters; the only fix is length. Ch 5 §5.4 (Lévy processes: "what is useful and what is decoration") can be cut to the one-paragraph verdict. Ch 6 §6.7 (CIR closed form) belongs in an appendix. Ch 7 is fine; add a figure of the purged/embargoed fold layout, which is the one idea readers never get from prose.

**Ch 8 (18.2k, 17 exercises).** Over-stuffed: three case studies plus Alltel plus a four-way hedge. **Fix:** move Case Study A (2022 "negative duration") to Ch 10 §10.7C, which already covers 2022, and cut exercises to eight. Add the chapter's missing figure: empirical hedge ratio against spread with the Baa3/Ba1 discontinuity.

**Ch 9–10 (17.5k, 17.6k).** Each is good; together they tell the March 2020 and April 2025 stories twice. **Fix:** per §3 below, Ch 10 keeps April 2025 (FRED-verified), Ch 9 keeps March 2020 through the factor lens, and each cross-references the other in one sentence.

**Ch 11 (15.7k).** Five Specification blocks in one chapter is four too many for a reader; fine for ROBO. **Fix:** keep the spec headings but collapse the first four into a shared schema and one engine; the chapter's two case studies (2022–23 round trip, 2026 CCC decompression) deserve the room.

**Ch 12 (15.7k).** The only chapter with figures (7). Model for the others. The HMM section (§12.4) can lose 1k words.

**Ch 13 (15.2k).** Best cold open in Part IV, then a 300-word taxonomy table that duplicates the Part IV opener. **Drag:** §13.9 "Autopsies" is where the reader wants Boardriders, Envision, Incora, Robertshaw and Altice as dated Docket Diaries and instead gets prose. The TOC promises Boardriders and Envision, and they appear *only* in the Part IV opener (one hit each). **Fix:** give §13.9 five short Docket Diaries, 150 words each; add a figure of the uptier waterfall before and after (the $\Delta_j(V)$ transfer function as a payoff diagram).

**Ch 14 (14.5k).** Rigorous and dry: competing risks, mixture-cure Weibull, Hamilton filter, in sequence, with the three "clocks" case studies held until §14.8. **Fix:** open §14.2 with the Mitel/Serta "same day, opposite rulings" story (now in §14.8.2), because it is the reason the regime variable exists. Add a figure: the two-hump recovery distribution by coalition membership.

**Ch 15 (14.0k).** Good scene (Friday the Thirteenth, Aisle Four), good cases (EA defeasance, WBD covenant strip). The three Specification blocks interrupt the derivations. **Fix:** move the specs to the end of the chapter as one engine.

**Ch 16 (18.6k).** Excellent, and too long. §16.2.3 (fitting the execution rate to aggregates) is a methods appendix. **Fix:** cut 2k words there; nothing else.

**Ch 17 (16.9k).** The strongest TREND chapter; OBDC/OBDC II "same loans, three prices" and the redemption-queue model are gripping. **Drag:** §17.5 (banks and insurers "changed seats") is a survey. **Fix:** compress to one table and one Trend Watch.

**Ch 18 (13.8k).** The AS derivation (§18.4, sampled) is correct, complete and, for 75 lines, joke-free. The bible permits that inside load-bearing steps, but the reader needs one exhale per step. **Fix:** after (18.1) add Ines's line about skew being the dealer's tell; after the FOC add the "a risk-neutral dealer still has a spread" observation now buried in Exercise 1. Add the five-term quote decomposition as a stacked-bar figure.

**Ch 19 (6.7k, no Debrief, no exercises).** Stops after the covariance engine and a resource graph. The master equation (§19.2) is set up well; eviction, stress liquidity commonality and basket adverse selection are missing entirely. **Fix:** finish it (see §6).

**Ch 20 (11.0k, no Debrief).** Has the March 2020 case study (§20.5) that should be the book's canonical one, and three Poker Table boxes, then ends. **Fix:** finish; add the arbitrage-band figure (price vs NAV with creation/redemption thresholds, March 2020 path overlaid).

**Ch 21 (13.1k, no Debrief).** Content is complete through five case studies; it lacks the close. Cheapest finish in the book.

**Ch 22 (13.6k, no Debrief).** Same. The One-Minute Rule and T+1 case studies are good; the Basel III endgame and CDS clearing sections promised in the TOC are absent.

**Ch 23 (11.8k, no Debrief).** Ends after Case Study A (GM/Ford May 2005). The SVB case promised in the TOC is a cross-reference at best. **Fix:** finish with SVB and the Carvana 2023 cap-arb squeeze (see §4).

**Ch 24 (3.8k).** A stub with the best cold open in Part VI. Hovnanian and Windstream, the CTD option, the auction simulation, orphaned CDS: all promised, none written.

**Ch 25 (10.3k).** Good and complete; the definition graph as a typed program is the most original idea in Part VII. Needs its figure most of any chapter: draw the J.Crew entity graph with the min-cut highlighted.

**Ch 26 (14.8k, 24 exercises).** Complete and funny (nine ROBO-vague-version hits). Cut exercises to ten.

**Ch 27 (4.1k) and Ch 28 (4.1k).** Stubs with writer-plan comments still in the file. Ch 28 is the payoff chapter for the 13-week-model arc and the Ines pit-boss frame; the book currently ends without its ending.

**Cross-cutting drag:** (a) 290 source extractions is about 100 too many; keep the ones whose annotation disagrees with the source. (b) "IDO or it didn't happen" appears 46 times; cap at once per chapter, in the Debrief, or it becomes wallpaper. (c) Exercise counts range from 0 to 24; standardize at 4–6.

## 3. The Case-Study Canonical-Home Map

Rule: one chapter owns the dated timeline (a Docket Diary or Trend Watch with sources); every other chapter gets one sentence plus "see §X.Y" and may add *only* its own lens. The lens is the point: Serta seen from a blotter, from a formula, from a clock and from a docket is a feature, as long as the facts are told once.

| Case | Files now | Canonical home | Other chapters: keep only this lens, cross-reference the rest |
| :--- | :--- | :--- | :--- |
| **Serta Simmons 2016–2026** | 15 (106 hits) | **Ch 13 §13.3.1** (the uptier in the formula) with the dated Docket Diary moved here from Ch 14 §14.8.1 | Ch 3 §3.7: the June 22, 2020 blotter only. Ch 5 §5.6.2: the two ends of the recovery distribution (with Hertz). Ch 14 §14.8.1: the re-default clock and the Fifth Circuit ruling as a regime jump. Ch 25 §25.7.3: the Rule 2019 panel. Ch 1, 6, 7, 16, 17, 26, 27: one-line mentions only. |
| **J.Crew 2016–17** | 10 (36) | **Ch 13 §13.6** (drop-down arithmetic) | Ch 25 §25.4.2 keeps the entity graph and min-cut (the document lens). Ch 1, 3, 7, 26: mention only. |
| **Hertz 2020–26** | 5 (62) | **Ch 16 §16.6** (already the model Docket Diary) | Ch 6 §6.10.2: the structural-model lens only. Ch 5 §5.6.2: recovery-distribution lens. Ch 13 Part opener: mention. |
| **March 2020** | 19 (72) | **Ch 20 §20.5** "When the ETF Was the Only Price in Town" owns the dated timeline (HYG/LQD discounts, SMCCF) | Ch 2 §2.9.3: the two-shock comparison. Ch 9 §9.10: factor lens. Ch 10 §10.7B: the V trend could not trade. Ch 21: CLO OC tests. Ch 22 §22.4.3: Treasury dash for cash. Ch 28: drawdown rule. Ch 1, 4, 7, 8, 11, 12, 18, 19, 27: one sentence each. |
| **April 2025 (tariff shock)** | 12 (58) | **Ch 10 §10.7 Coda** (FRED-verified spreads, day by day) | Ch 2 §2.9.3: microstructure comparison with 2020. Ch 8 §8.7C: three hedge regimes. Ch 11 §11.8.1: the ten-week V. Ch 12 §12.9A: regime filter lag. Ch 21: JAAA and the repricing round trip. Ch 5, 7, 9, 14, 22, 24: cross-reference. |
| **SVB March 2023** | 5 (16) | **Ch 6 §6.4.4** (why banks break Merton) | Ch 8 §8.7B: hedge that hedged both ways. Ch 23: write the vol-surface lens, then cross-reference. |
| **Mitel 2022–25** | 7 (30) | **Ch 14 §14.8.2** ("win the case, lose the credit"; Dec 31 2024 same-day rulings with Serta) | Ch 13: the uptier mechanics in one paragraph. Ch 1, 3, 5, 6: mention. |
| **Incora/Wesco 2022–24** | 7 (30) | **None exists.** Create a Docket Diary in Ch 13 §13.9 (Judge Isgur's partial unwind is the "court as random variable" exhibit) | Ch 1, 5, 14, 17: cross-reference. |
| **Boardriders, Envision** | 1 each (Part IV opener only) | Promised in the TOC; absent. Add to Ch 13 §13.9 (Boardriders: uptier plus the first-lien litigation; Envision: AmSurg drop-down then Chapter 11) | |
| **Carvana 2022–23** | 2 (10) | **Ch 6 §6.10.1** (negotiated barrier) | Ch 23: add the cap-arb squeeze lens (§4). |
| **First Brands / Tricolor 2025** | 3 / 2 | **Ch 12 §12.9B** (the first BDC redemption cycle) | Ch 6 §6.9.3: the no-equity-ticker lens. Ch 17: cross-reference. |
| **Credit Suisse AT1 / Altice France** | 5 / 3 | **Ch 18 §18.6.3** (jump inside the HJB) | Altice also belongs in Ch 13 as the 2024 European drop-down; one paragraph and a cross-reference to Ch 18. Ch 12, 21, 22, 24: mention. |
| **Windstream / Aurelius** | 4 (11) | **Ch 25 §25.5.2** (one defined term) | Ch 24: write the manufactured-credit-event lens, cross-reference the document story. |
| **Hovnanian 2018** | 2 (2) | **Ch 24** (to be written) | Part VI opener: mention. |
| **ConvergeOne 2024** | 4 (12) | **Ch 16 §16.3** (exclusive backstop reversal) | Ch 5, 13, 14: cross-reference. |
| **Spirit Airlines** | 2 | **Ch 16 §16.7** (the five-month zero; add the Aug 2025 Chapter 22) | Ch 15: cross-reference. |
| **Trinseo, Del Monte, Robertshaw** | 1–2 each | Trinseo Ch 13 §13.7.1; Del Monte Ch 14 §14.8.3; Robertshaw needs a home in Ch 13 §13.9 | |
| **EA 2025–26, WBD 2025–26** | 1 / 3 | **Ch 15** §15.2 and §15.8 | Ch 13, 14: cross-reference WBD. |
| **OBDC / OBDC II, Finastra** | 1 each | **Ch 17** §17.3 and §17.4 | |
| **GM/Ford May 2005** | 9 files for "GM" | **Ch 23 Case Study A** | Ch 3, 4, 8, 9, 12, 26, 28: these are mostly generic "GM" hits; confirm and cross-reference. |
| **LDI BWIC week Oct 2022** | 2 | **Ch 18 §18.9.1** | Ch 4: mention. |
| **Knight Capital 2012** | 2 | **Ch 26 §26.11** | Ch 27 should cross-reference it from the kill-switch section. |
| **Alltel 2006–09** | 1 | Ch 8 §8.3 | |

**Fictional-issuer continuity (same rule applies).** Halvorsen is "Building Products 7.25% 2029" in Ch 1, "Freight" in Ch 2 or 18, and "Packaging 6% 2031" in Ch 24; Brambleworth lives only in Ch 3; Larkspur Foam only in Ch 13. **Fix:** a one-page fictional-issuer bible in the style bible (name, sponsor, capital structure, documents' trapdoors, the Serta blocker it does or does not have), so the same three companies recur across the book and every worked number is traceable. "The Halvorsen Files" can then become a running case the reader follows from RFQ (Ch 1) to uptier (Ch 13) to basis (Ch 24) to post-reorg (Ch 16).

## 4. Content to Bring In, Ranked

Ranked by (reader grip) × (desk usefulness) × (fit with an existing engine). Every item marked *verify* needs the Sonnet research requests in §7 before a date or number goes in the text; nothing here was checked against the web in this review.

1. **Pluralsight 2024: the first big private-credit LME.** *Why:* the drop-down of IP into a new entity to pressure direct lenders (Vista as sponsor; the lenders took the keys), executed with no public bonds, no TRACE and no CDS. It is the book's missing bridge between Part IV and Ch 17. *Where:* Ch 17 §17.4 (as the private-side mirror of J.Crew) and a one-paragraph cross-reference in Ch 13 §13.6. *Desk learns:* document risk does not need a public price to transfer value; the PRS features are the same, the markout is a quarterly mark. *Verify:* dates, the entity structure, the lender group's recovery.
2. **Lumen 2024: the largest LME, run through a cooperation agreement that won.** *Why:* it is the counterexample to Serta: a co-op above the blocking threshold turning an auction into a bargain, exactly §13.5's claim, with real numbers. *Where:* Ch 13 §13.5 and Ch 14 §14.5 (the repeated game). *Desk learns:* the co-op's coverage share is the state variable, and the market's reaction to a co-op headline is tradable. *Verify:* size, co-op share, the TSA terms.
3. **Saks Global, Dec 2024 to 2026: a bond that went from new issue to LME to court in eighteen months.** *Why:* the fastest clock in the book's era (a \$2.2bn new issue, an uptier/FILO fight with excluded holders within months, then Chapter 11), and it happened to bonds, not loans, so TRACE shows the whole markout path. *Where:* Ch 14 §14.8 as the fourth clock; Ch 3 §3.6 for the pre-LMT flow detector on real prints. *Desk learns:* "new issue" is not a safe label; Theo's runway variable would have flagged it at pricing. *Verify:* filing date, the bond issuance terms, the exchange structure.
4. **Serta at the Fifth Circuit and Mitel in New York, Dec 31 2024: the same day, opposite rulings.** Already in Ch 14 §14.8; promote it to the *opening scene* of Ch 14 and give it its own Docket Diary. *Why:* it is the single best illustration of "the court is a random variable with a clause, a forum, a doctrine and a vintage," and it is funny: two courts, one afternoon, two words ("open market"). *Verify:* already sourced; confirm the rehearing history and 2025–26 follow-on rulings.
5. **Incora/Wesco: the uptier a court partly unwound (2024).** *Why:* the only major uptier that was actually clawed back; it is the "P(court unwinds)" node in the PRS tree with a real number attached. *Where:* Ch 13 §13.9 Docket Diary; Ch 14 §14.6. *Desk learns:* excluded lenders' claims have option value through the court, so the digital put has a second strike. *Verify:* the opinion's holdings and the final settlement.
6. **Revlon 2020: the \$900mm Citi wire, and the brand drop-down.** *Why:* two stories in one name. The drop-down (Revlon's 2019–20 move of brand IP to support new debt, the 2016 Barclays "BrandCo" structure) is a Ch 13 case; the Citi mistaken wire to the term lenders (district court: finders keepers; Second Circuit 2022: reversed) is the funniest operational-risk story in credit and belongs in Ch 27's kill-switch section next to Knight Capital. *Desk learns:* operations are a position. *Verify:* amounts, dates, the Second Circuit holding.
7. **The Carvana 2023 cap-arb squeeze.** *Why:* Ch 6 tells Carvana as a negotiated barrier move; Ch 23 needs the pain trade: short equity, long bonds, then a 1,000% equity rally after the exchange. The reader of Ch 23 should see cap-structure arbitrage lose on the leg it was sure about. *Where:* Ch 23 (new Case Study B). *Desk learns:* a barrier that can be moved by negotiation breaks every structural hedge ratio. *Verify:* the exchange terms (Aug–Sep 2023), equity path, and bond prices.
8. **Purdue (Supreme Court, June 2024) and the end of non-consensual third-party releases.** *Why:* it changed the value of a plan sponsor's "deal certainty" everywhere, and it is a clean regime-switch timestamp for Ch 14 §14.6 and Ch 16 (plan value as a negotiated number). *Desk learns:* confirmation risk entered every plan's $\mathbb{Q}$. *Verify:* holding and 2025–26 plan-structuring workarounds.
9. **Thames Water 2025: the UK restructuring plan as a co-op fight with a regulator in the room.** *Why:* the book is US-centric; Thames gives Part IV a non-US forum with a different doctrine (cross-class cram-down under Part 26A), a Class A versus Class B creditor fight, and public utility politics. *Where:* Ch 14 §14.6 (the court as regime variable, UK column) and Ch 22 (regulation as a price). *Verify:* plan terms, Court of Appeal decision, final outcome.
10. **Codere 2013 and Sears 2019: manufactured credit events and deliverables.** *Why:* Ch 24 is a stub and needs its stories. Codere (the GSO-engineered late coupon that The Daily Show covered) is the origin of the manufactured-default genre; Hovnanian 2018 is its peak; the Sears auction fight (Cyrus vs. other holders over what was deliverable) is the CTD option made flesh. *Desk learns:* the swap pays what the Definitions say, not what the economics say. *Verify:* dates, DC decisions, auction results.
11. **Wolfspeed 2025: convertible holders versus a prepackaged plan.** *Why:* an RSSG-era fight in a name with liquid equity, options and converts, so every Part VI instrument prices the same event, which is the Ch 23 "one distribution, many strikes" thesis on live data. *Where:* Ch 23 and Ch 15 (SMR/CoC mechanics in a prepack). *Verify:* filing date, plan terms, convert treatment.
12. **Spirit Airlines, Chapter 22 (Aug 2025).** Already half in Ch 16 §16.7; the second filing within a year of emergence is the re-default clock of Ch 14 §14.3 on a public equity. *Desk learns:* the mixture-cure model's "cured" fraction is smaller than plans assume. *Verify:* dates and the first plan's equity recovery.
13. **Zayo 2025 and Altice France 2024–25: the European and the fiber LMEs where lenders organized first.** *Why:* two large co-op-first cases, one US, one European, with opposite sponsor tactics (Zayo's lenders largely won; Altice's sponsor demanded a haircut from the first day). *Where:* Ch 13 §13.5, Ch 14 §14.5. *Verify:* co-op shares, final terms.
14. **The 2025 private-credit scare: Tricolor, First Brands, and "cockroaches."** Already seeded in Ch 12 §12.9B and Ch 17; add the fund-level consequences (BDC non-accruals, the redemption-request series, the public comments by bank CEOs) as a Trend Watch in Ch 17 §17.6. *Desk learns:* the request percentage is the best public belief series in the asset class, and it moved first.
15. **Market-structure stories for Part V:** (a) Citadel Securities and Jane Street entering IG and ETF-basket market making 2023–26, with the dealer-share data; (b) the April 2025 Treasury basis unwind and what it did to credit RFQ response rates; (c) the SEC dealer-definition rule vacated (Nov 2024) and the Treasury clearing mandate's deadline slips, as Ch 22's "a rule is a price" exhibits. *Verify:* all numbers.

**Stories to use as one-paragraph jokes, not case studies:** the Robinhood Hertz traders (already in §16.6), the AMC APE saga (Ch 16: equity as a security factory), the Citi "fat finger" flash crash of May 2022 (Ch 27), and the LLM that cited a non-existent section of a credit agreement (Ch 26 §26.10 already has the right frame).

## 5. New Recurring Formats

**Trade of the Chapter (new box, mandatory in Parts III–VI).** One card per chapter: thesis in one sentence; instruments and sizes; what kills it (two bullets); the hand history (1/5/20-day IDO markouts, illustrative or sourced); and "what ROBO would have done with the vague version." Ch 17's debrief already does this informally (the \$25mm BDC notes against a BDC equity short); Ch 24's cold-open basis trade and Ch 3's Brambleworth hand are ready-made. Format:

```text
> **Trade of the Chapter.** *Thesis:* ... *Legs:* ... *Size:* ... *Kills it:* ... *Hand history:* +12 / −38 / −71 bp IDO *(illustrative)*. *Ines's note:* ...
```

**Hand-History Replay (standardize Ines's gag).** The bible says every adverse-selection lesson ends with the hand replayed through markouts; the corpus has 54 "hand history" hits but only Ch 3, 7, 9 and 17 actually replay one. Make it a box with a fixed three-row table (t+1, t+5, t+20; raw, beta-stripped, IDO) and use it in every case study in Parts I, III and V.

**Fourteen-Sigma Tuesday (a recurring risk-report gag).** Theo's one-page risk report from Ch 5 should reappear at each Part boundary, one column richer each time (survival/default worlds in Ch 5, DTS in Ch 8, regime in Ch 12, PRS in Ch 13, LVaR in Ch 28). It gives the 13-week model a sibling arc and gives the reader a figure that grows.

**Price This RFQ in Fifteen Seconds (timed exercise opening every Part V chapter).** Give the RFQ (size, side, protocol, dealers in comp, time of day, calendar), a composite and an inventory, and ask for a bid before reading. Reveal the chapter's engine's bid in the Debrief. Ch 1's cold open is already this; make it a format.

**Spot the Trapdoor (Part IV and Ch 25 exercise type).** Quote 80 words of a real or Larkspur clause and ask which word is the leak ("purchase" vs "open market purchase"; "and" vs "or" in a sacred-rights carve-out; "Consolidated EBITDA" add-back caps). Score against the entity-graph engine. Kaz is the foil who gets it wrong first.

**Desk Myth vs. Reality as a true/false quiz page.** The 27 existing Myth boxes are a quiz already; collect ten per Part into a Part-opener quiz with answers at the Part's end.

**Docket Diary everywhere a date matters.** Only 12 in 11 files; Parts IV and VI should have one per case study. The Hertz block is the format.

**Figures: the book needs about forty, and it has none.** Minimum list, one per chapter, all drawable as inline SVG or matplotlib in the chapter's own code block so they reproduce: Ch 1 forced-seller flow graph; Ch 2 protocol share 2018–26 with the ETF–NAV basis regime; Ch 3 the Brambleworth price path with markout markers; Ch 5 the three ledgers (price, spread, return densities side by side) and the survive-or-jump mixture; Ch 6 Merton payoff diagram with the fulcrum strike; Ch 7 purged/embargoed/issuer-grouped folds; Ch 8 empirical hedge ratio vs spread with the Baa3/Ba1 cliff; Ch 9 dollar-neutral vs DTS-neutral factor returns; Ch 10 the trend straddle payoff and the V-whipsaw; Ch 11 the capture-ratio dimmer; Ch 13 the uptier transfer function $\Delta_j(V)$ before/after; Ch 14 the two-hump recovery and the re-default hazard shape; Ch 15 the CoC put moneyness by coupon vintage; Ch 16 the forced-seller overhang curve and the Hertz circuit as a timeline; Ch 17 the smoothing kernel and the P/NAV to implied-markdown map; Ch 18 the five-term quote as a stacked bar; Ch 19 the four-term basket price; Ch 20 the arbitrage band with the March 2020 path; Ch 21 the OC-test option book; Ch 23 the capital structure as a vol surface; Ch 24 the basis decomposition and the CTD auction; Ch 25 the J.Crew entity graph with the min-cut; Ch 26 the risk–coverage curve; Ch 27 the four timestamps of a fill; Ch 28 the PM dashboard (the 13-week model's final form, as a picture).

**Interactive companions (Edition 2, as artifacts or notebooks):** a Priming Risk Score worksheet (sliders for the five clause families and runway); an uptier sandbox on the Ch 13 waterfall engine (move the lien split, watch $K_1$ move); an RFQ quoting game against a synthetic toxic tier (the Ch 18 engine as a game: the reader quotes, the hand history scores them); and a "fit the ceiling" toy from Ch 2.

**Running gags: repairs and payoffs.**
- *Cooperation-agreement counter is out of order.* Ch 3 says 1, Ch 5 says 0, Ch 13 says 2 (twice), Ch 14 says "one in Chapter 3, plus forty-five in 2024 alone," Ch 17 says "this chapter: 0," Ch 21 says the counter overflowed. Fix the sequence (0 in Ch 1–2, 1 after Ch 3, 2 and 3 in Ch 13, "overflowed" from Ch 14 onward) and give it a payoff in Ch 28: Theo signs one.
- *Kaz vs. legal vocabulary* is under-used: about eight hits in 36 files, and the bible asks for one per appearance. The best ones (mattress protector, free shipping, "does sacred rights require a priest") should be matched in Ch 15 (make-whole: "is that a spa?"), Ch 16 (503(b)(9): "a tax form?"), Ch 21 (OC test: "optical character?"), Ch 22 (T+1: "a vitamin?").
- *"IDO or it didn't happen"* is over-used (46 hits); reserve it for Debriefs and the moment a case study's alpha is stripped.
- *"Open market purchase"* (48 hits, 18 files) works; give it the Dec 31 2024 payoff in Ch 14 and let the Ad Hoc Group retire the phrase in Ch 28.
- *The 13-week model* needs Ch 28 written; the Part VIII opener promises the dashboard and Mags's line ("the first adjusted number she has ever trusted, and then asks who adjusted it"), which is the best closing joke in the book and currently exists only in a Part opener.
- *Mags's "back in my day"* is well paced (35 hits); add the one war story the book keeps gesturing at and never tells: pricing bonds by phone in the 2008 basis blow-up (Ch 24's cold open sets it up).
