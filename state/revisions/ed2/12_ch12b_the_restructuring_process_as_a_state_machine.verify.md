# Verification Report, Edition 2: Chapter 12-B (The Restructuring Process as a State Machine)

Verifier pass, 2026-10-18. Chapter: `book_src/12_ch12b_the_restructuring_process_as_a_state_machine.md`. Revision log was complete (`<!-- STATUS: COMPLETE -->`); no earlier verify report existed.

**Baseline note.** The commit named in the task (9ac1c37) predates several Edition 2 steps: it has no 12B.10 (Case Study, Spec), 12B.11, Exercises or Resource Graph, and its clock table has the old "Real-property leases" label. The true pre-revision text is d5c4bc0 (548 lines, 12,969 words; the brief's 12,955 is cea2d0d, which differs only in the cold-open date line). I ran check 1 against both. Current chapter: 24,357 words, 1.88 times the 12,955 baseline (inside the 1.6 to 1.9 budget, near the top).

## Check 1. Nothing removed (python3, both baselines)

| Item | 9ac1c37 | d5c4bc0 | Now |
|---|---|---|---|
| Headings (pre list, all present) | 21 | 26 | 35 (9 new: four Full Derivations, ICA-as-guards, Saks scene, Purdue jump, Momentive scene, Quant-shop life) |
| Display-math `$$` delimiters / blocks | 40 / 20 | 40 / 20 | 40 / 20; every pre block present after whitespace normalization |
| Equation `\tag` numbers | none lost | none lost | none new |
| `[SOURCE EXTRACTION]` blocks (Moyer pp. 403, 107, 98, 108) | 4 | 4 | 4, lines and all four Annotation paragraphs identical word for word |
| Trend Watch boxes | 1 | 1 | 1 identical |
| Appendix F links (`#code-12b-1`) | 0 | 1 | 2 (original plus the Finder); anchor exists at App F line 12608 |
| Exercises (4) and solutions | n/a | 4 | 4 identical |
| Resource Graph (4 bullets, every URL) | n/a | 4 | 4 identical, no URL missing |
| Figures 12-B.1 to 12-B.5 and captions | 5 | 5 | 5, none missing |
| Tables (rights, ICA, transitions, clock, claims ladder, capital structure, plan-value) | 7 | 7 | 7 identical (the only difference from 9ac1c37 is the pre-writer relabel "Nonresidential real-property leases") |
| Used-in lines | shortened, none deleted | | confirmed present at each section end |

Must-not-change numbers and objects confirmed present: 4.2 points, 60.8%, 68.0%, 53%, 1.5%, the 1,100/1,300/1,600 rows, \$120mm, day 71, 3.4%, 1.6 points, the five intensities, 0.927, 56.6, the 1.2-point caveat, 8.57%, 7.3 and 0.84 points per \$100mm, Mags's calendar line, ROBO's 40, Kaz's springing lien and stalking horse, Poker Table, Dead Co. (pp. 160 to 161), $V = K_j$, Listing 12-B.1 link. All ten Finder-table function names exist in Listing 12-B.1.

Sentence-level diff (difflib by paragraph) showed ~148 pre sentences not verbatim in the post; every one is in a retired list, a paragraph rewritten as narrative, or a derivation moved to a "The Full Derivation" subsection (turnover, roll-up, plan-value transfer, resolvent and burn). Nothing substantive is missing. Nothing needed restoring.

## Check 2. Facts (new real-world claims; dossiers first, then web, 12 of 15 web calls used)

Verified against the dossier and/or primary source:
- **Saks Global** (`case_lmt_autopsies_us_2020_2026.md` §8): Dec 2024 \$2.2bn 11% notes via Jefferies; Aug 2025 exchange, about 98%, \$51mm stub (hedged "by one case summary"); ABL availability \$200mm, \$375mm (1 Dec), \$500mm (16 Dec); petition 13 Jan 2026, S.D. Tex. 26-90103, Judge Perez, about \$3.4bn; DIP \$1.75bn with \$1bn new money, final order 20 Feb (also Willkie and MoFo, web); ad hoc group 72% and 50%; RSA 2 Apr, \$500mm exit financing; confirmation 5 Jun; \$3.4bn to \$1.2bn; HBC, Amazon, Authentic, G-III equity cancelled; \$20mm trust for about \$1.5bn; emergence 26 Jun as Exemplar Luxury Group, Pentwater and Bracebridge on the board. Matches Chapter 11's own Saks scene; the "six weeks ago" in the 27 Nov scene is exactly six weeks after Ch 11's 16 Oct replay.
- Web: interest of more than \$100mm due 30 Dec 2025 unpaid (Bloomberg Law); S&P cut to SD on Wednesday 7 Jan 2026 (Retail Dive, published 8 Jan); an earlier SD in Aug 2025 exists, so "again" is right.
- **Purdue**: 27 Jun 2024, 5-4, Gorsuch for the Court, Kavanaugh dissent; holding quoted verbatim; \$11bn and 75% of assets; \$4.325bn first offer (web, and dossier row from the slip opinion). Revised plan: bench ruling 14 Nov 2025, formal approval 18 Nov 2025 (AP); AP "up to \$7bn over 15 years", Bloomberg \$7.4bn estimate; chapter hedges ("by press reports").
- **Container Store** (676 B.R. 356, Rosenthal J.; appeal 10 Apr 2026, No. 26-20166): dossier only (`case_courts_as_regime_variables.md` lines 66, 181), not re-fetched.
- **Momentive**: April 2014 petition, accept-for-cash versus replacement notes "with a present value equal to the Allowed amount", 2d Cir. decided 20 Oct 2017, make-whole denied on acceleration (all from the Second Circuit opinion, read in full via pdftotext); remand rates L+4.50% with 1% floor (0.50% OID, 0.375% flex) and 7.9% against plan rates 3.88% and 4.69% (Weil, 24 Apr 2019); Third Circuit EFH (Nov 2016) contrary on make-whole, commentators called it a conflict.
- **Motors Liquidation**: 2d Cir. 21 Jan 2015, mistaken UCC-3, \$1.5bn term loan, held authorized and effective.
- **Rule 3001(e)(1) and (e)(2)**: quoted wording ("except for a claim based on a publicly traded note, bond, or debenture"; 21 days) matches the current rule on Cornell LII. Moyer "confi" (p. 79), ethical walls and 8-K (p. 80), third race (p. 81) match the page files (PDF page numbering, same convention as the chapter's p. 403, 107, 98, 108).
- **Jefferies**: initial purchaser of the Saks notes (dossier); Revlon BrandCo agent was Jefferies Finance LLC (credit agreement 7 May 2020, web).
- **Oaktree**: "opportunistic, value-oriented and risk-controlled" (oaktreecapital.com/about, per `perspectives_buyside_credit_managers.md` §3); Marks material is labeled paraphrase.
- **Pair box (PB-02)**: Vantress and Owen match `state/cast_bible.md` line 110 and `rv_thread.md` row 113; labeled fictional; Owen has no lines. All dollar arithmetic recomputed: 1.8mm, 1.75mm, about -50k, 285k, 420k, 160k, 72k, 220k, 335k.
- **Math Gently arithmetic** recomputed for all ten boxes (0.259 and 0.20 blocking stakes, 85.45, 62.5%, 60.5, 83%, pi_2 = 1/3 and pi_3 = 2/3, 90%, 0.982, 0.988, 57.5, annuity factors 4.712 and 5.683, 88.2, 90.8, c* = 4.8%): all correct.
- **Invented dialogue for real people**: none. Real-person text is limited to the Court's holding sentence (verbatim), Oaktree's self-description (verbatim) and Moyer's quoted words. Fictional composites carry labels: Mags's war story, Saks replay, Purdue scene, Momentive replay, Quant-shop life (Tallowmere, Hollis), The Pair, and the generic CLO, Oaktree and dealer seats.

## Check 3. Hygiene (python3)

No code fences; 40 `$$` delimiters, all on their own lines, even; no paragraph with an odd inline `$`; no unescaped currency; no `---` line; no emoji; no "CHECK" in book text; the last nonblank line of the chapter is `<!-- STATUS: COMPLETE -->`.

## Fixes made (small Edits in the chapter)

1. Saks Beat 1: "Each step in the minimum availability was \$500mm" was wrong (steps were 200, 375, 500); now "By 16 December the minimum had climbed to \$500mm".
2. Saks Beat 4: "A year and a half earlier the stub and the second-out notes had been the same bond" was wrong (the exchange was five months before); now "Five months earlier, before the August exchange".
3. Saks Beat 2: "the trackers do not say where" for the \$750mm became "the public summaries do not agree on where" (Bondoro cites about \$752mm of rolled-up FILO and NPC loans, MoFo a larger package); added "press accounts differ on the tranche split and the pricing" after the DIP terms, matching Chapter 11.
4. Saks Beat 3: Theo's Chapter 7 line ("landlords at the front of the line") replaced with the inventory paying the asset-based lenders, administrative claims next, juniors behind both.
5. Momentive Beat 2: the rate sentence now states the Treasury base (2.1%) plus 2.0 and 2.75 point adjustments, 4.1% and 4.85% at confirmation per the Second Circuit, then Weil's 3.88% and 4.69% as issued.
6. Momentive Beat 4: Kaz's invented 5.5% was said to be "roughly where the remand landed"; the remand was LIBOR plus 4.50% with a 1% floor (about 7% at April 2019 LIBOR), so 5.5% is the floor. Text and Kaz's line corrected ("My principle was right and my rate was low").
7. Dealer seat: "Jefferies ... facility agent for Revlon's BrandCo" became "its leveraged-finance affiliate, Jefferies Finance, was the administrative agent".
8. The Pair, short cost: \$38k a year did not follow from "a fee of 15%"; now states a cash rate near 4% and a rebate of about -11% (0.342mm times 11% = \$38k).
9. Logged the new findings as items 8 to 11 in `state/research/open_items_ch12b_ed2.md`.

## What remains doubtful

- Saks DIP: composition of the \$750mm, the SOFR+11% PIK pricing and the tranche split are not settled by public summaries; the chapter asserts no roll-up ratio and keeps two branches.
- Saks plan: which class the \$51mm stub sat in, whether it shared in the \$20mm trust, the (a)(10) accepting class (Theo's "reading that fits" is hedged), the \$51mm figure (AI-assisted case summary), and the notes' actual grace period are all unconfirmed.
- Purdue: \$7bn versus about \$6.5bn versus \$7.4bn depends on the source; "18 November 2025" is the formal approval date, the bench ruling was 14 Nov.
- Container Store citation and appeal number rest on the dossier alone.
- Momentive: exact petition day, whether the remand differential was actually paid, and the claim that the first-lien noteholders' class-level versus holder-level election worked as described are unchecked. Third Circuit EFH is stated as "practitioners noted" a conflict; the debtors argued the cases were consistent.
- Length: 1.88 times baseline, near the cap. Brief item 10 asked for a bathtub box; the writer made it a prose gloss to hold the ten-box cap (ten Math, Gently boxes counted, none adjacent), a deliberate and acceptable deviation.

<!-- STATUS: COMPLETE -->
