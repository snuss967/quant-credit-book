# Verification Report, Edition 2: Chapter 8

Chapter: `book_src/08_ch08_isolating_ido_and_empirical_duration.md`. Pre-revision text: commit 9ac1c37 (diffed from `/tmp/pre_08_ch08_isolating_ido_and_empirical_duration.md`). Revision log was marked COMPLETE before this pass began. Web and network calls used: 10 of 15 (two FRED CSV pulls, five searches, three page fetches).

## 1. Nothing removed

Method: a python3 comparison of headings, display math, Source Extractions, boxes, exercises, Appendix F links and URLs, plus a line-by-line and sentence-by-sentence coverage test of the pre text against the post text.

| Item | Pre | Post | Result |
| :--- | ---: | ---: | :--- |
| Headings (42 pre) | 42 | 53 | none missing; 11 added (six Full Derivation, two Long Scenes in 8.7, "The common whisper, at book scale", "Twelve Residuals", "Quant-Shop Life") |
| Display-math delimiters (`$$`) | 68 | 68 | all 34 pre blocks present, verbatim and in the same order |
| `[SOURCE EXTRACTION]` blocks | 20 | 20 | every quotation and page number intact; one annotation (Ben Dor p.191) changed only by the brief's pointer to the 2022 scene |
| Trend Watch boxes | 8 (text matches) | 8 | all three present, wording unchanged |
| Poker Table, Desk Myth, Ways This Blows Up | 2, 1, 5 | 2, 1, 5 | intact |
| Exercises | 6 | 6 | identical text |
| Appendix F links (`#code-`) | 7 | 13 | all seven listing links kept; six more in the Finder table |
| Resource Graph sections | 4 | 4 | no URL from the pre text is missing; seven briefed resources added (Pflueger, Jersey, Younger, Robeco, SimCorp, Morningstar, Karoui) plus others from the dossier |
| Spec ("The Spec You Hand the Robot") | 1 | 1 | byte-identical |
| Numeric tokens in the pre text absent from post | | | none |

Restored: the pre text carried three show-level placeholder resources ("Odd Lots on the 2022 bond sell-off", "Flirting with Models on smoothed returns", "Resolve Riffs on stock-bond correlation"). The writer replaced the first two with named episodes. "Resolve Riffs" and the 2022 sell-off topic had no replacement, so one line was restored at the end of the final Podcasts list: "Show and topic only, no episode verified: ReSolve Riffs ...; Odd Lots on the 2022 bond sell-off."

Notes, no action needed:
- The "Code Companion" stubs and EXPLAIN comments in the pre text are now prose paragraphs before each "The full listing is Listing 8.x in Appendix F" link. The links are all kept.
- The Finder table has eight rows, as briefed. The Debrief bullets are unchanged. Figures 8.1-8.5 are present with captions (they were added by the figures pass, not by the writer).
- Headings for Alltel and Case Study C stayed at `###` (resolved in `open_items_ed2.md`).

## 2. Facts

New factual claims were extracted by sentence diff against the pre text, then checked against the dossiers named in the brief (`perspectives_buyside_credit_managers.md`, `perspectives_dealers_and_systematic_shops.md`, `case_carvana_svb_wolfspeed_capital_structure.md`, `rv_pod_platforms_and_risk.md`, `media_episodes_posts_parts_III_IV.md`, `life_quant_shop_daily_life.md`, `rv_pair_book.md`) and, where marked, against primary or independent sources.

Verified, no change:
- FRED yields: DGS10 1.52% (31 Dec 2021), 4.25% (24 Oct 2022 high), 3.88% (30 Dec 2022), 3.98% and 3.55% (8 and 13 Mar 2023), 4.20 / 4.01 / 4.15 / 4.48% (2, 4, 7, 11 Apr 2025), from the cached FRED pull. DGS2 0.73%, 4.41%, 5.05% (8 Mar 2023), 4.03% (13 Mar 2023), from a fresh FRED pull. The "down 102 bp" arithmetic holds.
- Bloomberg 2022 returns: Corporate -15.76% and High Yield -11.19% (YCharts); Treasury Index -12.5%, worst year on record (Fortune carrying Bloomberg, 31 Dec 2022). The Treasury figure was the one new number.
- HY OAS 310 bp at end-2021 and a 599 bp peak in early July 2022 (Janus Henderson note, Aug 2022). Kept as "approx."
- SVB: 8 Mar 8-K ($23.97bn book, $21.45bn proceeds, $2.25bn raise), 9 Mar stock -60.4% to \$106.04 and more than \$40bn of deposits out, 10 Mar closure and FDIC receivership, 12 Mar joint statement, 17 Mar holdco Chapter 11, 25 Apr 2023 holdco notes at 69 (3.5% 2025) and 57 (1.8% 2031), the \$2bn deposit frozen (dossier §2.1 and §2.3, tagged to the 8-K, the Fed's Barr review and Debtwire/MarketAxess). The dossier also confirms the two notes are one class under one indenture (20 Sep 2010), so "same indenture" stands. The "wiped out" phrasing (flagged CHECK in the dossier) is not quoted, as briefed.
- Athene \$292B net invested assets at year-end 2025 and 120 bp blended net spread ex-notables in Q4, Jim Zelter (President), 9 Feb 2026 call (buy-side dossier §8). No hedging policy is attributed to Apollo.
- Jane Street: "trading more than \$900 billion with clients globally in 2025", "pricing more than 25,000 bonds" and "one of the world's leading ETF liquidity providers" all confirmed on janestreet.com/what-we-do/client-offering/ today. The basket logic is framed as the seat's logic, not a quoted statement.
- PB-03: S&P cut Ford to BB+ on 25 Mar 2020 and Ford's roughly \$35.8bn of debt was due to leave the Bloomberg investment-grade index at month-end (Bloomberg/BNN, 25 Mar 2020; consistent with Ch 1 §1.8.2). Pair arithmetic rechecked: h_S = 1.65, \$36.4mm market value, about \$39mm face, DV01 residue \$5.4k, coupon difference -\$0.09mm, borrow \$0.13mm.
- Pod x-ray seat: 2.8 times DTS, 64% unhedged, about \$32mm of outright beta, all correct. Paleologo (20 May 2024) and Falk-Wallace (25 Jul 2024) are paraphrased from the dossier; no quotation marks around anything they said.
- Twelve Residuals: 66 pairs, 0.58 versus 0.29 volatility, first PC about a third, pod Sharpe arithmetic (2.17 and 2.37) all recompute. Sharpe-cap formula is Morillo's per the pod dossier §3.4.
- Odd Lots (Pflueger, Jersey, Younger, Paleologo, Falk-Wallace, Morillo, Kowara/Jacobson, White, Weinstein, Kumar), Trillions, Credit Edge (Karoui), Flirting with Models (Smith), Robeco, SimCorp, AQR/Peterseil, Robotti: titles, guests, dates and URLs match the media dossiers. Pflueger's page was fetched and confirms guest, affiliation and the "more stock-like" and "bond-like" phrases (the page shows no date; 5 Oct 2026 comes from the RSS feed record in the dossier).
- April 2025 hedge-ratio arithmetic (about -4, +2, 0) and the SVB week grading (+0.4%, -2.4%, -2.7%, -0.4%) recompute from the stated yields and spreads.
- Cross-references exist: Ch 10 §10.7 Case Study C (2022), Ch 7-B §7-B.5 (covariance and PCA), Ch 6 §6.1.4 (exponential clock), SR 11-7's three validation elements (conceptual soundness, ongoing monitoring, outcomes analysis).
- Invented people and dialogue: none for real persons. The Fed "governor" at the lunch is unnamed and the day is labeled illustrative. All dialogue belongs to the fictional cast; Dov, Wen, Marcus, Vantress, Elif Arslan and the "systematic credit asset manager" carry fiction labels; the insurer, pod and market-maker seats name no firm in anyone's mouth. Mags's 2022 "fund winding down" line matches cast canon C5.

Fixed in the chapter:
1. **Verizon close date.** Ben Dor p.211 says January 8, 2009. Verizon's own release and 8-K are dated January 9, 2009. The Alltel scene now reads "On 8 January 2009, by Ben Dor's dating (Verizon's own closing release is dated the next day), ..." The Source Extraction and its annotation are untouched.
2. **2022 Treasury move.** "roughly 250 to 370 bp" became "240 to 370" (10-year +236 bp, 2-year +368 bp), and the rate-leg cost "10 to 14 points, \$20mm to \$28mm" became "10 to 15 points, \$20mm to \$30mm" (duration 4 times 2.4 to 3.7 points).
3. **Morillo attribution.** The 2.17 / 2.37 figures could be read as his. They now say the formula is Morillo's and the Sharpe ratio, correlation and pod count are this book's illustration.
4. **Jane Street.** "alongside one of the larger ETF liquidity businesses" (the book's characterization) became the firm's own words, "describes itself as one of the world's leading ETF liquidity providers."
5. **Alltel investor-base claim.** Mags's statement that the May 2007 sellers quoted in spread and the buyers in points is the segmentation story, not Ben Dor's data for this bond. Now "In May '07, I'd bet, ...".
6. **Regime alarm in the 2022 scene.** "fired in the first quarter" now carries "(illustrative; the date depends on the window)", matching the earlier hedge in the same scene and the pre text.
7. **Resource Graph.** Restored placeholder line (section 1).

## 3. Hygiene

- Code fences: one, the ```text spec block (lines 1147-1167). No other fences.
- Math: 68 `$$` delimiters (34 blocks, all alone on their lines); no line has an odd number of inline `$`; currency is escaped as `\$` throughout.
- No line of `---` anywhere. No "CHECK", "TODO" or "FIXME" in the text. Two em dashes, both inside a Source Extraction quote and a table cell inherited from the source.
- Last line is `<!-- STATUS: COMPLETE -->`, with a trailing newline.

## What remains doubtful

- **Trend Watch 2024 rows (protected text, untouched).** The figures pass could not reproduce the 2024 CCC and HY rows of the §8.2 Trend Watch on a fresh FRED pull (CCC ρ -0.17 / H 0.68 and HY -0.31 / 0.67, against the printed -0.22 / 0.61 and -0.34 / 0.65). The 2025 and 2026 rows reproduce. Needs a re-pull and a decision by the owner of the Trend Watch pass.
- **2022 spread path.** Only the end-2021 level (310 bp) and the early-July peak (599 bp) were confirmed, from a secondary note. The free FRED history starts in October 2023, so the year-end "high 400s", the "up about ten points / gave back more than half" CDX arithmetic and the Q1 sign change of the rolling correlation are marked approximate or illustrative and remain unverified.
- **Alltel.** The dates, ratings and hedge ratios are Ben Dor's and unverified beyond him, except the Verizon date noted above. The LBO close and sponsors stay out of the text (open item in `open_items_ed2.md`, which could also record the 8 versus 9 January point).
- **SVB holdco notes.** The "recovery route made real" reading of the 69 / 57 quotes is the chapter's interpretation; the dossier calls the 12-point gap a reinstatement bet on one claim class, and the 1.8% 2031 coupon alone explains part of a price gap. The text says only that "whatever the twelve points were a bet on, it was not the yield curve", which is safe, but Ch 24 or Ch 14 may want the nuance.
- **Insurer accounting sentence** ("records most of that fall as an accounting event rather than a realized loss") is a general characterization (amortized cost / AOCI), not tied to a named standard.
- **Continuity, not fact.** Cast bible line 113 has Theo hearing the April 2025 sleeve cards in a Ch 10 replay on Fri 16 Oct 2026, 7:20 a.m. (the cold-open day), while Ch 8 gives him the April 2025 card only after the SVB replay, days later, and says he had not traded it. Ch 8's own bible entry leaves exact days open; the Ch 10 pass should reconcile.
- **Brief errors the writer correctly did not follow.** The brief's ridge example (η = 0.05 giving a condition number near 20) is wrong (it gives about 34); the chapter's η = 0.1 giving about 19 is right. The brief had the B-bucket move in the vignette reversed (0.73 to 1.03); the chapter's 1.0 to 0.7 matches a window losing 2022.

<!-- STATUS: COMPLETE -->
