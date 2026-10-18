# Verification Report, Edition 2: Chapter 13

Chapter: `book_src/13_ch13_codifying_lmt_game_theory.md` (536 lines before, about 1,020 now). Pre text: commit 9ac1c379. Revision log was marked COMPLETE. Web calls used: 5 of 15 (Mayer Brown STG alert, an STG filing search, a Wesco/Pattonair search, a Saks plan search, a Selecta search; the dossiers carried the rest).

## 1. Nothing removed: PASS

Compared pre and post with a python script (headings, display math, extraction blocks, boxes, exercises, links, URLs) and a sentence-level difflib pass.

| Item | Pre | Post |
| :--- | ---: | ---: |
| Headings | 18 | 22 (the 4 additions are the "The Full Derivation" subsections) |
| Headings missing | | 0 |
| Display-math blocks (`$$` pairs) | 26 | 28 (all 26 originals present; 2 differ only in a closing comma turned into a period) |
| [SOURCE EXTRACTION] blocks | 8 | 8, byte-identical |
| Trend Watch boxes | 2 | 2 |
| Docket Diary boxes | 2 | 2 (dates corrected per brief item 21, nothing removed) |
| Poker Table, Ways This Blows Up (x2), Desk Myth | present | present |
| Exercises 1-5 | 5 | 5 |
| Appendix F links (#code-13-1/2/3) | 3 | 3 |
| URLs | all | all present, plus new ones |
| Figures 13.1-13.5 | 5 files | 5 files, all on disk |
| Resource Graph | | the two unverified podcast lines were replaced by the verified items as briefed; Wachtell, 9fin, HLS, Petition, Octus, Levine, all academic and data items kept |

Sentence-level check: 51 pre sentences were not found verbatim. Each one was traced:
- Moved into the new Full Derivation subsections or reworded into narrative (Eisenberg-Noe map, double-dip fixed point, Nash FOC, Shapley definition, MAP objective, FOC, shrinkage form, Serta parameter quotes, Trinseo make-whole fight, "never calibrate PRS to prices; regress price residuals on EPL").
- Three Code Companion stubs (`<!-- EXPLAIN: Listing 13.x -->`) were expanded by the writer into plain-language explanations of each listing, each ending with the Appendix F link. This is what tools/move_code_to_companion.py says later editions should do. No link was lost. Flagged below only because the stub wording no longer exists.
- Nothing was found deleted.

## 2. Facts: PASS after fixes

New factual claims were extracted by reading every added paragraph against the pre text, then checked against the named dossiers (`case_lmt_autopsies_us_2020_2026.md`, `case_courts_as_regime_variables.md`, `perspectives_buyside_credit_managers.md`, `case_lmt_private_and_european_2024_2026.md`, `media_episodes_posts_parts_III_IV.md`, `life_quant_shop_daily_life.md`) and the web where a dossier flagged CHECK.

Verified without change (dossier match, numbers recomputed where arithmetic):
- Cold open: CLO 7.5% CCC limit and lowest-price rule (Kundu); Serta 74 and 25; Lumen about 99 after about 30 months.
- Boardriders: $450mm, $110mm new money, $321mm roll-up, $431mm, about $85mm non-consenters, 40-50% discount, ICG and York, Justice Masley Oct 17, 2022, Authentic, dismissal Sep 2023.
- Serta: $1.95bn/$450mm, five Prevailing Lenders, $200mm/$1.2bn/$875mm, 52.6%, 74 and 39 (26% and 61% discounts), 25 court value, Jan 23, 2023 filing (31 months), Dec 31, 2024 holding and quotes, rehearing denied Feb 18, 2025, cert denied Nov 10, 2025, remand July 7, 2026 numbers ($261.13mm, $734mm, $348mm, $484.88mm, $223.75mm, $403mm, 70c), Skadden low-single-digit cents, Law360 "roughly $400 million". The unblend table recomputed: 934/1,950 = 47.9, 1,075/1,887 = 57.0, difference 3 to 12 points. The sign of the blending bias was corrected by the writer (blend understates the first-lien pre-deal slice); verified.
- Math Gently boxes recomputed: 0.6% below zero, 2,984/1,341/2,162, Phi(-1.95) = 0.026, 2.3 points, 13.5 points at median 1,200, Shapley pivots 10/10/2/2 by enumeration (and the 12/12 split by pivot position), Nash 45 then 40, bid ceiling 40, fixed-point column 50/60/65/67.5/68.75 to 70, 33 steps, 2,300 steps at slope 0.99, hazard 0.105, logistic/Poisson pairs, Beta 9.02% and 22%.
- Pluralsight/ARCC marks (89.0, 48.0, 96.8, 7.8-point gap), Blue Owl and Ares group about Aug 22, 2024.
- Robertshaw (May 9 and Dec 11, 2023; $228.3mm; $117.6mm; Feb 15, 2024; Judge Lopez June 20, 2024).
- Lumen (all TSA dates, thresholds, $250mm cap, participation 94.4/98.5/99.5, CreditSights prices, 49% primed, Sep 17, 2024 prices and tender percentages, AT&T Feb 2, 2026, May 20, 2026 at about 99.4); Guggenheim and Wachtell for Lumen (Houlihan was CHECK in the brief and the writer correctly left it out).
- Optimum (Nov 25, 2025; six defendants; No. 1:25-cv-09785; Judge Vargas; Feb 2026 motions; phase one order Aug 4, 2026; $4.12bn due April 2027) and Selecta (Oct 28, 2025; No. 1:25-cv-08956; web search confirmed Deltroit v. Selecta Group B.V.).
- Incora (all dollar figures, 59%, 67.9% and 57.4% arithmetic, "high degree of certainty", 96.5%, 98.4% plus $420mm, July 10, 2024 oral ruling, Dec 27, 2024, Jan 17, 2025, Jan 31, 2025, Dec 8, 2025, PIMCO and Silver Point quote from the district court opinion, BlackRock and JPMorgan).
- Trinseo (all dollar figures; whiteboard arithmetic recomputed: 2.19x, 5.0 cents, 69 cents, 14x, 31x, 6.0, 8.8, 24; $427.5mm DIP June 17; July 30 denial of judgment on the pleadings; Aug 19 hearing; no ruling by mid-October).
- Saks Dec 23, 2024 to Jan 13, 2026 and the exchange consideration grid. Scoreboard months and the 13.5-month median recomputed for both ends of Envision's range.
- Mitel (Mar 10 / Apr 17 / June 20, 2025; $1.15bn less debt), STG Jan 12, 2026.

Fixed in the chapter (small edits):
1. **Wesco/Pattonair (Incora scene).** Text said Wesco "had raised over $2bn for its 2020 acquisition of Pattonair". Web search: Platinum acquired Wesco Aircraft (closed Jan 9, 2020) and combined it with Pattonair; the notes financed that. Reworded to "to finance Platinum's acquisition of Wesco and its combination with Pattonair".
2. **STG date conflict.** §13.6 pre-text said "(N.Y. Sup. Ct., 2025)" while the new capped-forward passage said "early January 2026". Mayer Brown's STG alert gives the decision date as Jan 3, 2026 (a Saturday, as the dossier flagged; the law-firm alert prints it), and the filing was Jan 12, 2026 (web: D.N.J., lead case 26-10258). Citation changed to "Jan 3, 2026"; nine days holds.
3. **Saks plan outcome hedged.** The $1.2bn remainder and $20mm trust are single-source in the dossier; a search confirmed the June 5, 2026 confirmation and the pre-confirmation $20mm trust but other summaries say debt fell "nearly 75%". Text now says roughly two-thirds to three-quarters, one account near $1.2bn, trust as reported before confirmation.
4. **Required-Lender denominator (Family 2).** "most documents written after about 2017" (affiliate caps) and "most syndicated credit agreements" (all-or-substantially-all collateral release) were unsupported generalisations. Changed to "many". Only 66⅔% is named as a number, as the brief asked.
5. **Pluralsight rate.** "$1.175bn term loan at SOFR + 800" read as an April 2021 term; the dossier gives SOFR + 800 as the rate by Dec 2023. Reworded "paying SOFR + 800 by 2023".
6. **Larkspur arithmetic in §13.2.1.** "two months and two points from that corner" was wrong: at 78 the price condition (below 80) is already met; only the runway condition (11 vs 9 months) is not. Now "already through the price line at 78 and two months short of the runway line".
7. **PRS check.** "a sponsor's 13D landed" replaced by "a new Rule 2019 statement landed" (a sponsor-owned name has no 13D).
8. **Fictional chorus labelled.** In the J.Crew and Wesco Docket Diaries, "The Ad Hoc Group, represented by counsel" is the book's recurring fictional chorus (pre-existing) but sat inside real-case boxes. Both now read "The Ad Hoc Group (this book's fictional chorus)". The Larkspur ad hoc group in the cold open and §13.5 is already identified as fictional.

Invented-quote review: no real person speaks invented words. All dialogue belongs to the fictional cast (Theo, Kaz, Mags, Ines) or to the fictional chorus. Real-person quotations are from opinions or filings (Judge Isgur "with a high degree of certainty" is in the dossier from Octus; the Fifth Circuit quotes are from the opinion). The quant-shop-life vignette (Priya) is labelled "a fictional composite" and its Moyer quotation matches pdf pages 79-81 (printed 62-64). Serta, Lumen and Incora scenes state that the cast reads the record and was not present.

## 3. Hygiene: PASS

- No fenced code blocks at all (zero ``` fences; no ```text diagrams exist in this chapter).
- Display math: 56 `$$` lines, all paired. Inline math: no paragraph has an odd number of `$` once `\$` is removed. No inline math span contains prose or an amount (no currency masquerading as math). Currency is escaped as `\$` throughout.
- No `---` lines in the chapter.
- Last line is `<!-- STATUS: COMPLETE -->`, preceded by a blank line.
- Cross-references checked to exist: §12B.3 (Thresholds), §6-B.1 and §6-B.6, §6.6, §7-B.3, §7-B.4, §5.5, Chapter 25.

## What remains doubtful

- **STG ruling date** (Jan 3, 2026, a Saturday) rests on one law-firm alert and the dossier; the filing date is solid.
- **Incora on appeal:** the Fifth Circuit docket number (26-20018, docketed Jan 13, 2026) and the "notice of appeal about Jan 6" are unchanged from the dossier; no Fifth Circuit ruling was found as of Oct 18, 2026 and the text says so.
- **Trinseo after July 30, 2026:** "no ruling found by mid-October" is the dossier's own CHECK.
- **Incora secondary figures** ($1.27bn of new first-lien notes, more than $1.7bn of new debt, 85-to-above-par run in the 2026s) are labelled secondary in the text and remain so.
- **Lumen:** no suit by excluded holders was found; the crossholder group's identity is not public (text says holders were not named in the 8-Ks).
- **Saks plan terms** beyond confirmation date and the roughly 75% debt reduction are single-source.
- **Mayer Brown Wesco alert:** the resource-graph title is reconstructed from the URL slug and is marked "title only"; the Jan 21, 2026 date comes from the trend dossier.
- **Code Companion stubs:** replaced by explanation paragraphs with the Appendix F link. If the build script keys on `<!-- EXPLAIN: Listing -->`, it will find none (the explanations are already written); no `<!-- EXPLAINED -->` marker was added.
- Whether the revised chapter still reads as narrative rather than prescription (the user's note about prescriptiveness) was not part of this verification pass; the added scenes are narrative, but the Specification for AI Implementation and the closing bullet card remain prescriptive by design.
<!-- STATUS: COMPLETE -->
