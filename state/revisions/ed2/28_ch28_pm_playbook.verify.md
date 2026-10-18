# Verification report: Ch 28 PM Playbook (Ed2 U2)

Verifier pass on `book_src/28_ch28_pm_playbook.md` after the writer's revision (log is STATUS: COMPLETE). Baselines: the commit named in the task (9ac1c37, 692 lines, no figures, predates Ed1 fixes) and e1af4b8 (790 lines, 5 figures), the text the writer actually started from. Both give the same result on every count below.

## 1. Nothing removed: PASS (no restoration needed)

| Item | Pre | Post |
| :-- | --: | --: |
| Headings | 42 | 53 (none missing; new: 10 `####` sub-sections including the Quant-Shop Life vignette, 1 `###` Dov Adler review) |
| `$$` lines (display math) | 78 | 78 (39 blocks; 3 differ only by trailing period -> comma) |
| Numbered equations (28.1)-(28.25) | 25 | 25 |
| `[SOURCE EXTRACTION]` blocks | 19 | 19 (quote lines identical; one annotation edit, below) |
| Trend Watch boxes | 3 | 3 (text byte-identical) |
| Desk Myth boxes / Ways This Blows Up | 2 / 1 | 2 / 1 |
| Spec blocks | 7 | 7 |
| Exercises 1-5 | | identical |
| Appendix F links (`#code-28-1`...`-8`) | 8 | 18 (all 8 listings still linked) |
| Figures 28.1-28.5 with captions | 5 (e1af4b8) | 5 |
| Debrief bullets, dashboard table rows, ROBO spec | 8 | 8 / all rows kept |
| §28.11 and Resource Graph | | byte-identical |
| Markdown links | | none lost |

A token-level pass (every number and capitalised name in the pre text) found only four numbers missing (0.033, 0.070, 0.147, 12.8 in the old CCC and DTS worked examples, now carried by the box, the scene and Figure 28.3) and no names missing except cosmetic ones. Derivations were moved, not deleted: hit-rate law, discrete Kelly with sensitivities, Kelly with a jump, FRTB clocks, stop with drift, and the band each sit under "The Full Derivation".

One protected-text edit, deliberate and logged by the writer: the Ben Dor p.112 (second) annotation ends "That was the edge the gate removed." in place of "That is the next case." (the extraction now sits inside the Third Avenue case). Accepted.

## 2. Facts

Method: difflib at sentence level against e1af4b8 (75 new sentences carrying dates, firms, rulings or amounts), then every checkable claim traced to a dossier or a primary source. Web calls used: 9 of 15 (NY Fed post, SEC order via pdftotext, a press search on the unwind length, a Kundu search, the ESRB paper, Kargar abstract, JPMorgan and BlackRock Q1 2020 transcripts, and an ESRB search).

Verified as stated:
- SEC Rel. IC-31943: $7.81 to $7.08 institutional NAV in November; $317mm November net redemptions; cash "over $200 million" by early December; $1.1bn YTD outflows, "more than 145%" of remaining NAV at 9 Dec; board plan of liquidation 9 Dec; sales suspended 10 Dec; order dated 16 Dec.
- NY Fed Liberty Street (Adrian, Fleming, Vogt, Wojtowicz, 19 Feb 2016, "Did Third Avenue's Liquidation Reduce Corporate Bond Market Liquidity?"): announcement 9 Dec, news public late 10 Dec, 11 Dec as reaction day, quintile sort, HY fell most / IG rose, all three quoted conclusions verbatim.
- Kundu, ESRB WP 141 (March 2023): both quotes verbatim (7.5% CCC limit and lowest-market-value marking; "median CLO operates within 4%").
- Kargar et al.: willingness to pay for immediacy up "about 200 bps" per dollar, subsiding after Fed announcements.
- JPMorgan Q1 2020 call (14 Apr 2020): "$820 million" bridge-book markdown (Piepszak), fixed income up 34%, Dimon Q&A fragment. BlackRock Q1 2020 call (16 Apr 2020, Ramji): LQD "traded almost 90,000 times", top five holdings "an average of 37 times". NY Fed Terms of Assignment 27 Mar 2020 (FMA, segregation, "neutral footing") and BofA ($450mm markdowns, FICC +13%, 15 Apr) from the dealers dossier 5B.4 and 5B.7.
- Mercer (May 2023) fee stack, the "approximately 20%" gross-for-10%-net sentence and "20-30% at times" turnover; the 1.17x own-P&L premium and 36-PM simulation (POD 3.3); 43% / 12% stop-out rates (POD 4.3, 40,000 paths); Ironshield quote and the EUR 400m / EUR 20m example (POD 5.3).
- Rule 22e-4 definitions and October 2016 adoption; Fifth Circuit Serta ruling; all weekday-date pairs (15 Oct 2026 Thu, 13 Oct Tue, 30 Nov 2015 Mon, 16/20/23/27 Mar 2020 Mon/Fri/Mon/Fri).
- Cross-chapter: Ch 1-B ($400mm allocation, $16mm below HWM, $24mm halving line), Ch 22 (61% on loan 6 Oct, 50 -> 300 bp), Ch 8 (0.28 mean residual correlation, 30 November 0.15 sentence), Ch 4 (vendor split issuer into three), Ch 16 (60/40 coin), Ch 20 (March 2020 replay), cast bible C2/C8, six years at PJT.
- Arithmetic re-done for every box and scene (Math, Gently boxes 1-10, Kelly 0.926 / 1.10 / 0.65 / 0.22 / 0.11, 250 trading days and $68mm Third Avenue cost, 1.5% and 3.2% mark losses, 74% stop-out odds, fixed point 4.74 -> 1.86 -> 3.61 -> 2.95, band 2.14 and 3.9x speed limit, 0.056/0.071/0.079, Sharpe cap 2.37 / 91% / 2.0, fee waterfall rows, $2.5mm payout, $4.8mm borrow-fee spike).

Fixed in the chapter:
1. **CLO box (Kundu), wrong mechanism.** The text said selling the cheap loans "would raise the lowest price and with it the haircut", which gets the sign backwards. Rewritten to the paper's logic: excess is carried at the lowest price, so selling a loan releases the gap between its price and that lowest price, widest for the highest-priced loan (confirmed against ESRB WP 141 section 2.1, "g(gamma - beta)A/L").
2. **Third Avenue "unwind will take roughly a year" attributed to the SEC order.** The order does not say it (press reports at the time said "as long as a year"; the wind-down ran longer). Reworded to "the press will report that the unwind may take as long as a year" and the scene label now credits press reports for that one figure.
3. **"$7.81 at the start of November and $7.08 at the end"** softened to "fell from $7.81 to $7.08 in November" (the order says only "in November 2015").
4. **Dimon quote.** Shortened to the fragment the transcript check confirmed ("you're going to have quarters where things get bad"); the longer lead-in is from a machine transcript and could not be confirmed.
5. **Dealer box inference about a real dealer's bid** generalised to "a dealer's flow-desk bid ... its commitment book" (still flagged as a guess).
6. **Arithmetic slip in the pod review.** Kaz said "sixty cents" went to lenders, financiers and market makers; costs are 12.5/31 = 40 cents and the leak is 6/31 = 19 cents. Now: sixty never reached the pod, forty to the street, nineteen leaked.
7. **Pair count.** Card said "fourteen pairs" (14 / (1 + 13 x 0.28)); Ch 1-B, Ch 8 and Ch 10 all give twelve. Recomputed: 12 / (1 + 11 x 0.28) = 2.9, 4.5 at 0.15, ceiling up by sqrt(4.5/2.9) = 1.25 (same "quarter more room").
8. **Attribution of the review-line ladder to Ch 1-B.** Ch 1-B prints only the $24mm halving line; the 3.5% / $14mm review call comes from the rv_thread mandate. Now "Chapter 1-B prints its halving line".

Real people, invented dialogue: none. Real speakers (Dimon, Piepszak, Ramji, Kundu, Paleologo, the Mercer and Ironshield passages, NY Fed authors) are quoted only from transcripts or papers; Barse is pointed to, not quoted. Fictional composites are labelled: cold open, Vantress vignette (Marcus, Gordon Pike), CCC case (Rafe's book), Third Avenue (Mags's recollection, cards), March 2020 and the 2026 coda (Bram), Dov Adler's review (Dov, Wen, Marcus, Vantress).

## 3. Hygiene: PASS

- Only fenced block is the ```text ROBO spec (lines 989-1008).
- 78 `$$` lines, all on their own line, balanced; no paragraph with an odd count of unescaped `$`; 0 unescaped currency (`\$` used 92 times).
- No `---` rule line anywhere; no stray `<!-- -->` except the final STATUS comment; last non-empty line of the chapter is `<!-- STATUS: COMPLETE -->`.
- Kaz pronouns clean (they/their; "his shoulder" is Theo's).

## Remaining doubtful

- Dimon, Piepszak, Ramji and BofA quotes rest on Motley Fool machine transcripts (JPM and BlackRock re-fetched; BofA from the dossier only). Check against audio or the companies' own transcripts before print.
- Ironshield (Fixed + Floating, 4 Aug 2026) quote and the Mercer figures come from the POD dossier; the Mercer PDF itself was not re-opened.
- Illustrative Pair-box lines are not mutually calibrated: $3.0mm of borrow fees at 64 bp implies about $470mm of shorts, i.e. gross near 2.3x capital, while the card uses gross at 4x. Not contradictory in print; a careful reader could notice.
- §28.11 still carries "Bermin and Holm (2026) ... (CHECK)" (U3 owns it); the body sentence no longer gives publication details.
- The old "roughly 32 points" recovery sensitivity (one-sided 15-point move) is unchanged from Ed1 and correct only for the upside move; the downward move is about 40 points.
- The pre-revision commit named in the task (9ac1c37) is older than the text the writer revised (e1af4b8); reviewers diffing against it will see the figures, Ed1 fact-check edits and the Code Companion rewrite as "new".
<!-- STATUS: COMPLETE -->
