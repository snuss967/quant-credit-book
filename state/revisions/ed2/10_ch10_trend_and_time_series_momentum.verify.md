# Verification report: 10_ch10_trend_and_time_series_momentum (Edition 2, U2)

Chapter: `book_src/10_ch10_trend_and_time_series_momentum.md`. Pre-revision text: commit 9ac1c37. Revision log was COMPLETE (24 of 24 items). Web calls used: 4 searches (two on the SG indicator) plus 3 FRED CSV downloads, 7 in all; limit 15.

## 1. Nothing removed

Compared pre and post with python3 (headings, `$$` display math, extractions, boxes, links, URLs).

| Item | Pre | Post | Result |
| :-- | :-- | :-- | :-- |
| Headings | 41 | 49 | All 41 kept; 8 new (Quant-Shop Life, two Full Derivation subsections, Testing for the smile, replay, 9 March card, Grading the cards, Liberation Day scene). |
| `$$` delimiters | 56 | 56 | Every pre display equation text is present unchanged in post (0 missing). The blended-weight and smile derivations moved under "The Full Derivation" headings; nothing deleted. |
| [SOURCE EXTRACTION] blocks | 14 | 14 | All 14 byte-identical (page numbers, annotations included). |
| Trend Watch boxes | 2 | 2 | Both byte-identical, including "about $39bn (Man AHL, mid-2026)" and "January 2019 at −16.0%". |
| Appendix F links `#code-10-1` to `#code-10-6` | 6 | 6 | All present. |
| Exercises 1-5 with Checks | 5 | 5 | Section byte-identical. |
| Spec You Hand the Robot and text Spec block | | | Byte-identical. |
| Resource Graph | | | Every pre entry and URL present; 6 entries added by the separate resgraph pass (logged in `10_...resgraph.md`); the channel-level Odd Lots stub was replaced by a specific episode, as that log says. |
| Desk Myth vs. Reality, Ways This Blows Up (two), What ROBO Built, Case Studies B and C | | | Present. |
| Figures 10.1-10.5 and captions | 0 in pre (added by the figures pass) | 5 | Present. |
| Math, Gently boxes | 0 | 10 | At the cap of ten; no two boxes adjacent without narration (checked all 35 blockquote blocks). |

Not a writer loss, noted for completeness: the six `<!-- EXPLAIN -->` stubs and their one-line "Code Companion" blockquotes in §10.10 no longer exist; the explanation pass (U1) replaced them with explanation prose that opens on the roll-week Tuesday (Listing 10.1) and the 10 April x-ray (Listing 10.6), per brief item 23. The six `#code-` links are kept as "*The full listing is [Listing 10.n in Appendix F](#code-10-n).*"

Sentence-level diff (834 pre sentences, 105 not found verbatim in post): all 105 reviewed. They are the retired passages the brief names (the "By the end of this chapter" paragraph, the stop-loss list paragraph, "Two consequences follow", "Three consequences follow" lead-ins, the §10.2.3 stitching paragraph, the italic case lead-ins, the "Lesson:" sentence, the Coda's old paragraphs, the Code Companion stubs, the Resource Graph stub), plus facts that were re-told elsewhere: Dynkin 788/899 and 950/991 (now at the 4 December 2008 cut, pp.215-216), basis "back toward zero" (p.390), SG +20.9% and MSCI ACWI −42.2%, Man AHL "no hard-wired long credit bias", AlphaSimplex −11.3%, 600 to 1,800 bp, the April 2025 FRED path, 119 bp in three sessions, 20.9%/20.7% ISDA, SG −4.9% April, the arccos 0.131 and 1.6 flips, the 25-50% roll share, the Barclays QPS numbers (6.34%, 1.56, 15.9%, pp.608-609, 5 to 8 bp), Kendall-Stambaugh and the confidence region. Every one of those facts was found in the post text. Nothing restored.

## 2. Facts

New factual claims about real events, firms, people, dates and amounts, and how each was checked (FRED values were recomputed from downloaded CSVs of BAMLH0A0HYM2, BAMLC0A0CM and BAA10Y).

Verified, no change:
- BAA10Y peaked at 6.16% on 4 December 2008, and is the maximum of 1 Jul 2007 to 30 Jun 2009 (FRED CSV).
- HY OAS: 2.62% (18 Feb 2025), 3.42% (2 Apr), 4.01% (3 Apr), 4.61% (7 Apr, April high), 4.37% (9 Apr), 3.09-3.10% (13-14 May, "near 3.1"), 2.96% (30 Jun); IG OAS April high 1.21% on 9 Apr, two sessions after HY's high; 3.93% on Monday 5 Aug 2024 (2024 maximum); 3.46% on 30 Mar 2026 (2026 maximum); 2.68% (22 Sep 2026) and 3.23% (15 Oct 2026). All match FRED. 3.42/4.01 = 0.85; 2.68/3.23 = 0.83; 2.68 + (3.23 − 2.68)/2 = 2.955.
- Dossier `trend_trend_following_tsmom_credit`: "first sustained credit trend since 2022" above the 3.46% March high (as a conditional); Man AHL Evolution via The Hedge Fund Journal; Robeco 17 Aug 2012 "with about 50%"; Haesen-Houweling-van Zundert.
- Man 2022 p.31 quote and the Bektić (2016) footnote: matched on page text (`state/pdf_pages/Man_Quantitative_Credit_Alpha_Early_Mover_2022/page_0031.txt`): "the only spill-over to achieve meaningful statistical significance is equity Momentum, which generates a higher alpha than corporate bond Momentum itself", and "more swiftly in equities than in bonds".
- Insurer box: NAIC bond factors 2.C 2.168%, 3.A 3.151%, 3.C 6.017% (dossier `trend_insurance_capital_forced_flow`, row 2026-06-23); "nearly half" is 3.151/2.168 = +45%. CLO box: 7.5% CCC limit, excess carried at the lowest CCC price, 85c average versus 58c cheapest, sell the higher-priced CCCs (dossier `trend_loans_clos`, Kundu ESRB WP 141, March 2023).
- S&P 500: record close 1,565.15 (9 Oct 2007) to 676.53 (9 Mar 2009) is −56.8%, so "fallen by more than half" is right and 9 March 2009 was the low (web search, ETF Trends snapshots).
- BNP Paribas suspended three ABS funds on 9 August 2007; 10 August 2007 was the next day (web search; closes the open item in `state/open_items_ed2.md`).
- Calendar checks: 20 September 2019 was a Friday; 22 September 2026 a Tuesday; 12 October 2026 Theo's third Monday; 15 October 2026 a Thursday; 9 March 2009 a Monday; 4 December 2008 a Thursday; the 7 sessions 1-9 April 2025 are seven trading days; the 9 April 2025 tariff pause and the 2 April 2025 Rose Garden announcement are as dated.
- Kendall (1954) bias (1+3ρ)/T, ρ = 0.97, T = 300 gives 0.013; SE sqrt((1−ρ²)/T) = 0.014 (arithmetic; the brief's κ-based 0.004 was a plugging error and the writer correctly used ρ).
- All worked arithmetic recomputed: δ^60 = 0.37, δ^180 = 0.05, half-life 42 days; 342/461 = 0.74; Φ(0.258) = 0.60 and 2Φ − 1 = 0.20 at ρ = 0.25; 0.56 at a 3σ move; 0.075 and 0.027 stale-clock leads; (2 − 4 × 0.75)/2 = −50%; arccos(11/12)/π = 0.131; jump box (0.0147 variance, 12% jump vol, 4.1% diffusion vol at β = 0.23 and DTS 0.18, jump about 90% of variance, 3.1x oversizing, 1.2% at N = 100); fee 300 bp on $39mm face at 78 = $0.91mm.
- Pair Book numbers against `state/rv_pair_book.md` and Ch 1-B: 72,600 versus 71,600 DTS, Halvorsen 90 to 78, 600 to 1,400 bp, spread duration 3.4 to 2.3, fee 50 to 300 bp, mirror-image construction (long the tighter credit), the −0.6 flashback row.

Fixed in the chapter:
1. Corrupted LaTeX in the §10.2.1 EWMA box: `\approx` had lost its backslash to a bell control character (`\x07pprox`), so the 0.37 would not have rendered. Restored.
2. Pair box: "the x-ray's orange line in September 2026" is wrong; Ch 1-B and the ledger put the 40%-of-a-leg orange line on Tuesday 13 October 2026. Corrected.
3. Cold open: Mags said 3.42 on 2 April was "after the Rose Garden"; the 3.42 was the close before the evening announcement. Now "the day of the Rose Garden".
4. Cold open napkin: 112 bp hurdle uses a 4.5% running spread while the same scene quotes a 3.23% OAS. Added one sentence calling 4.5% the book's working number, saying today's true hurdle is smaller, and "on the napkin". The 55/112 ratio and the sticky note stay.
5. Insurer box: "CLO factors adopted in June 2026" overstated the status (working group on 23 June; Executive Committee 8 July per the dossier). Now "as restated in the June 2026 working-group papers that set the new CLO factors".
6. Dealer box: "a 20/120 crossover is SG's own published indicator" could not be verified (two searches; the SG Trend Indicator's construction was not found, and SG's own research in the dossier says the index "behaves more like a much slower model"). Replaced with "moving-average crossovers at a handful of standard speeds".
7. Grading the cards: "the equity-to-credit signal flipped weeks before credit's own" was stated as history; now framed as the desk's replay, tied to the Paleologo annotation that already says it.
8. Stambaugh parenthetical overgeneralized ("any coefficient whose regressor is persistent"); now "a related bias in regressions on persistent predictors".
9. Debrief: Ines read Theo's card "from under her own coffee cup", but the cold open leaves the card on Theo's desk. Now "from his desk".

Invented dialogue and labels: no real person speaks. Real-source quotations (Man p.31, Robeco "with about 50%", Ben Dor "back toward zero as the crisis abated", Dynkin, Paleologo, The Hedge Fund Journal "no hard-wired long credit bias") are verbatim from the shelf text or the dossier. Charlie McElligott appears only as a Resource Graph episode title. Fictional composites are labeled once per scene: cold open, the remembered RSSG client meeting, Quant-Shop Life (Lucía Ferrer, QR-3307; in `state/cast_bible.md`), the 12 October model review, Kaz's EMC pitch, the stale-clock run, the 2007-09 replay, the Liberation Day replay and Vantress flashback, the Pair box (PB-01, "every number is illustrative"), and the Debrief. Mags's 2007 and 2009 lines match the cast bible row for Ch 10 (no position in 2007; "Sal" canon; the par-recovery-at-40 line is the chapter's own).

## 3. Hygiene

- Code fences: only the Spec's ```text block (lines 870-893); no other code blocks.
- Math delimiters: 56 `$$` (even), no odd inline `$` on any line after removing display blocks, braces balanced in every display and inline expression, no control characters left.
- Currency: no unescaped `$` before digits; all dollar amounts use `\$`.
- No `---` lines in the chapter.
- Last line is `<!-- STATUS: COMPLETE -->`.

## Remains doubtful

- The SG 20/120 attribution still stands in protected Exercise 5 ("If SG's 20/120-day crossover...") and in Ines's dealer-hand line; not verifiable from the dossier or web, left because protected or fictional dialogue. Worth a fact-check by the owner of the Exercises.
- "SG Trend Index lost 4.9% in April" is cited to SG Prime Services (protected Trend Watch and the Coda); the dossier's figure (−4.89%, −9.33% YTD) comes from the Top Traders Unplugged compilation and the SG Prime check is still open (`open_items_ed2.md`).
- The 4.5% working spread against a 3.23% live OAS: the cold open now says so, but Figure 10.1's caption describes its 112.5 bp bar as "trailing 252-day mean OAS / D = 4", which for the real 2024-26 mean (about 3%) would be nearer 75 bp; that is the figures pass's to reconcile.
- The jump box uses β^DTS ≈ 0.23 (from the Figure 10.2 data) where the brief and the planned figure `ch10_jump_vs_diffusion_var.png` assume 0.4; the figure must follow the text (logged open).
- The cold-open and replay descriptions of what the fast and slow sleeves "would have done" in 2007 and 2025 are the desk's fictional run, not backtests; they are labeled but not reproduced in the Lab.
- The truncated Omny URL for the McElligott Odd Lots episode ("...on-the-sharp-str") is copied from the dossier as the host gave it; not re-fetched.
- Scratchpad note: another verifier run shares the scratchpad directory and overwrote one of my helper scripts mid-run; chapter edits were unaffected (git diff against HEAD shows only the 8 lines above).

<!-- STATUS: COMPLETE -->
