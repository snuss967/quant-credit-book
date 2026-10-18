# Verify Report, Edition 2: Chapter 17 (Private Credit and the Public-Private Convergence)

Verifier pass, 18 Oct 2026. Pre text: commit 9ac1c379 (`/tmp/pre_17_ch17_private_credit_public_private_convergence.md`). Post text: `book_src/17_ch17_private_credit_public_private_convergence.md`. The revision log carried `<!-- STATUS: COMPLETE -->`, so the check ran.

## 1. Nothing removed (python3 comparison)

Checked, pre vs post:

- Headings: 48 pre, 62 post. Two pre headings changed, both on purpose per the brief: "Same Loans, Three Prices" became "Same Loans, Four Prices", and "### Case Study: Two Bank Partnerships, Read as Term Sheets" became the `####` frame inside §17.5.1. Fourteen new `####` subsections (Full Derivation x5, Kaz's first Dimson run, the quarter Kaz unsmoothed one fund, Medallia ledger, Long Scene 1, Theo's dual track, Pluralsight, Two Bank Partnerships, Long Scene 2, Quant-Shop Life, mark-gap signal).
- Display math: 48 `$$` in both (24 blocks); every block is verbatim identical after whitespace normalization. No equation changed or lost.
- [SOURCE EXTRACTION] blocks: 7 and 7, all verbatim, with their Annotations. Nuveen epigraph present.
- Trend Watch boxes: 4 and 4, verbatim. The "check against the OBDC Q4 release" parenthetical in the §17.6 box is left (protected wording; the dossier shows the release does say "86% of price-to-book value", so it can be dropped at the next fact-check pass).
- Exercises 1 to 6: byte-identical. Spec for AI Implementation: identical except the Listing 17.1 explanation, which the separate code-explanation pass replaced (the pre text still held the `EXPLAIN` marker).
- Appendix F links: all five `#code-17-1` to `#code-17-5` anchors present; post has 14 mentions (explanations and the Finder table).
- Resource Graph items: 24 bullets verbatim in post; 36 pre URLs all present. The 33 added URLs and 39 added bullets come from the separate Resource Graph pass (resgraph.md), not the writer; not re-verified here.
- Tables (31 table lines incl. Banegas, OBDC four-quarter, trade menu), Desk Myth, Poker Table, four "Ways This Blows Up" boxes: all verbatim.
- Figures 17.1 to 17.5: five images added by the figures pass; all five PNGs exist.
- Facts scan: every number and dollar token in pre appears in post (only `$0.947`/`$0.950` formatting differs). Key phrases of the rewritten paragraphs (Couts et al., Octus 50 cents and 40 points, NAIC/FactSet, Y-14, Berrospide, PIK 58.3%, Erel, Merton, Serta/Incora, etc.) survive. No deletion found; nothing needed restoring.

## 2. Facts (difflib by section, 22.8k added words reviewed)

Sources used: the dossiers `trend_private_credit_marks_and_redemptions_2025_2026.md`, `perspectives_buyside_credit_managers.md`, `perspectives_dealers_and_systematic_shops.md`, `case_lmt_private_and_european_2024_2026.md`, plus 11 web calls (SEC EDGAR, IMF GFSR PDF, Credit Edge page, searches).

Verified clean:
- Medallia ledger: every mark, range, par ($1.97B), 77.8 to 49.2, SOFR+6.00%, 4% PIK removal, ADS 86.8 twice, "four to ten points" (computed 4.2 to 9.6), dispersion 5 to 14 (5.3 to 13.9). PIMCO/Karoui figures (writer's web check plus dossier, including "skewed upward").
- OBDC/OBDC II: 5 Nov proposal, 98% overlap, adviser allocating same investments since inception; termination release dated 19 Nov 2025 with the quoted sentence (confirmed on the exhibit); $14.81 NAV, $148mm at 86%, 1.22x (Sep) to 1.19x (Dec); $1.4B sale; OBDC II $600mm, 33.8% of commitments; revolver $225mm to $75mm (confirmed on OBDC II 8-K); Cox/Saba $3.80 for up to 8M shares, NAV $8.27 to $5.57, RoC to ~35%, "all tendered shares taken" (dossier).
- 99.7 vs 99.8: resolved. The press release says 99.7% of par as of 12 Feb 2026 on the whole $1.4B (confirmed by search); OBDC II's 8-K quotes 99.8% on its own $600mm excluding unfunded. Chapter's 99.7 is right for the $1.4B.
- Software week and BIS figures (dossier ACI-SW and BIS; trade-press part already hedged).
- Pluralsight: loan terms, 89.0 / 96.8 / 7.8 points; 83.4 to 97.0 and 13.6; 48.0 / 47.0; Vista equity values; IP drop-down; ~22 Aug takeover terms; $54.7mm vs $106.5mm; $60mm loss; Goodwin quote; 1.7% to 0.8% (all dossier case file section 1).
- Jim Miller, Arougheti (31 Jul), Rowan, Athene $292B (buy-side and dealer dossiers); Handler "we believe we were defrauded" (confirmed by search; Reuters reports the same words from the investor-day filing); Dimon 14 Oct 2025 / $170mm Tricolor.
- Default ladder (Proskauer 2.51%/716 loans, KBRA 3.5%, Moody's 4.0/5.8%, Fitch 6.3%/47%, PIMCO ~19%), BCRED $4.5B / half / $2.3B, OTIC, tracker funds, North Haven two-thirds, OCIC "vast majority", BCRED 10.0% to 9.1%, ADS 29.8% fill: dossier.
- HarbourVest / Greg Ciesielski: quotes confirmed on the Credit Edge episode page (see fix below).
- Date arithmetic: all weekdays given in the text (5 Nov, 19 Nov, 18 Feb, 6 Mar, 3 Jun 2024, 23 Jun, 6 Nov) are correct.
- All worked numbers in Math, Gently boxes A to I recomputed and correct (0.38 / 0.62, 0.24/0.52 = 0.46, 8.5x, 7.1%, 0.49 and 0.28, 7.2% / 4.8% / 4.9%, 0.947, 20.1 demand and 24% fill, -1.9%).

### Fixed in the chapter (small Edits)

1. **PRIV/SEC letters, misattribution (§17.7.2).** The chapter said SEC staff "noted that Apollo's bids came three times a day, each open for fifteen minutes, at Apollo's discretion, and that bid and adviser value could 'diverge significantly'". I read both EDGAR letters. Staff (27 Feb 2025) wrote only: effective "without resolution of staff comments"; the as-filed Apollo agreement was redacted so far that material terms were not public; and reliance "solely on bids from Apollo" was not "sufficient". The three-bids / 15-minute / discretion / "diverge significantly" language is the fund's counsel's reply of 28 Feb (footnote 3), and "no further comments" is a staff email the same day. Rewritten with correct attribution.
2. **IMF GFSR April 2026 quote misread (Long Scene 2, Beat 3).** The chapter (following the dossier) applied "despite apparent balance sheet capacity" to payouts above 5%. Footnote 27 of the PDF reads: managers "either accommodated redemptions above the 5 percent limit or gated them despite apparent balance sheet capacity", which "highlight the discretionary nature of these programs". Quote now given in full and correctly. (Dossier §3.3 carries the same slip; worth correcting there.)
3. **Greg Ciesielski quote (Saba seat box).** "Described 2026 as a buyer's market" overstated; now quotes what he said ("it's certainly a buyer's market at the moment, which is what you generally see in dislocation"; "through the first quarter we're run-rating above $50 billion this year").
4. **Unsmoothing scene arithmetic.** Kaz's point estimate 0.71 sat beside an interval computed at rho1 = 0.5, with no explanation. Added that the interval is the worked case at a middling 0.5, and that at 0.71 the band is about 0.49 to 0.93. Brief's arithmetic kept.
5. **Pluralsight replay hygiene.** "KBRA's count" now says the tally is KBRA's but the schedules behind it were public by the cut-off; "June 10-Qs" changed to "10-Qs for the June quarter" (they were filed in August, which is the "two months" the text means).
6. **Pair box PB-16.** "OBDC trades about 14% below NAV" is now marked as the pod's illustrative screen figure (no source found for OBDC's actual discount on 6 Nov 2025); "HYG holds almost no middle-market software" softened to a statement about HYG holding public high-yield bonds.
7. **Listing 17.2 opening.** "The second week of February 2026 ... a dozen BDCs inside five days" hedged to "Mid-February 2026 ... inside a few days of one another" (OBDC itself reported on the 18th).
8. **Cold open.** "Two other sponsors' funds" corrected to "Other sponsors' funds" (the InvestmentNews piece names three).
9. **Labels.** Added the fictional-composite italic line before the §17.8.3 Monday-ranking exchange (it was the one unlabeled invented scene).

Real-person dialogue check: no invented speech. Real people appear only through sourced quotes (Miller, Arougheti 31 Jul, Rowan, Handler, Karoui, Ciesielski, the Money Stuff episode description) or flagged paraphrase (Arougheti 10 Jun, Dimon's cockroach line given in indirect speech). Mags quoting Karoui is a verified quote. Weinstein is not quoted beyond the episode description. Every invented scene (cold open, Dimson run, unsmoothing, Medallia ledger, Long Scenes 1 and 2, Theo's dual track, Pluralsight replay, term-sheet reading, atlas walk, Tomasz vignette, Ines's feature review, pending-mark exchange, PB-16) carries a fiction/illustration label.

## 3. Hygiene

- No code fences anywhere (so no non-`text` blocks).
- `$$` count 48 (even); no line with an odd number of inline `$` once display blocks and `\$` are removed; no unescaped currency found (133 `\$` escapes; scan of math spans for prose found none).
- No line of `---` anywhere.
- No `EXPLAIN`, `CHECK` or `TODO` markers; no em dashes.
- Last line is `<!-- STATUS: COMPLETE -->` (preserved through all edits).

## Remaining doubts (hedged in text or logged in `open_items_ch17_ed2.md`)

- Arougheti 10 Jun 2026 remark (about 11% of requests from under 5% of investors): TIKR secondary only; chapter says "reported ... a secondary account ... we paraphrase it". The dossier does not say it was Ares's own non-traded BDC; the chapter infers it. Not verified.
- BCRED Q1 7.9% / upsized to 7% / ~$400mm feeder: AltsWire secondary; hedged "by press reports".
- Trade-press software-week moves (Blue Owl 13%, peers 8 to 10%): single source, hedged; unclear if "Blue Owl" is the manager or a vehicle.
- OBDC 0.71, FSK 0.56, median 0.76 of book: aggregator (stockanalysis.com) snapshot of 16 Oct 2026; hedged "on an aggregator's quote".
- Moody's 4.0%/5.8% (PDF carries a DRAFT header) and Fitch 6.3% (via Benzinga): hedged "a Moody's analysis" / "reported".
- Cox/Saba "more than 30% below NAV": the 31.8% uses the 31 Mar NAV ($5.57), after the first return of capital, while the bid is dated 6 Mar; wording "about two-thirds" is safe, the "NAV basis" is not confirmed from the SC TO filing.
- "Every quarterly tender since inception has been fully satisfied" is in quotation marks but the exhibit's wording appears to be "every quarterly tender has been fully satisfied" (since inception in 2017); pre-existing text, not changed. Same for the OBDC II "reinstate tenders" paraphrase.
- Pluralsight: "no bonds and no CDS" is an inference (private loan only), not in the dossier. Ares/Oaktree equity to zero in Feb 2026 is press/snippet only ("by press accounts"). Vista fund-document equity values are a Reuters report (publication date vs the 3 Jun cut-off unchecked; text says "reported later").
- Merger termination date: release dated 19 Nov 2025 (confirmed on the exhibit); the dossier's "18 Nov / thirteen days" is the outlier. Chapter is right.
- Medallia sponsor not named in text (Thoma Bravo, 2021, would be consistent but is not in the dossier).
- Resource Graph additions (39 bullets) were made by a different pass; their feed-checked descriptions were not re-verified here.

<!-- STATUS: COMPLETE -->
