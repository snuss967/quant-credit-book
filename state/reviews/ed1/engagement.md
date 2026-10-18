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
