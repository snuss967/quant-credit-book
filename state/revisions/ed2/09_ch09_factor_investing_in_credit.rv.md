# Ch 9 RV weave log (Edition 2, user directive 13)

*RV weaver, 2026-10-18. Thread entry: `09_ch09_factor_investing_in_credit` | scene (callback to Sharpe 1.9) | the book | factor neutralisation | H: DTS, by pair. I: supposed to be twelve views. L: every pair long the cheaper name, a value factor with extra steps; neutralise or admit | Man Numeric telecom case (§9.7) | home Ch 8 §8.8 | figure: book loadings on five factors before and after neutralisation.*

## Pre-checks

- `state/rv_thread.md` complete; no prior `.rv.md`; `.log.md` ends COMPLETE (not busy).
- The chapter already carried the beat (§9.7.2, Marcus's second x-ray, ~720 words, from the lessons pass). Per instructions: **strengthened in place**, not duplicated.

## What was written, and where

- **§9.7.2, new `####` heading "The Pair Book: One View, Twelve Times"** (replaces the five old beat paragraphs; one telling). Scene body ~1,870 words, Tue 29 – Wed 30 Sep 2026, fiction label once at top in italics. Kept from the old text: the 0.7 → 0.2 loading, Marcus's "value factor with extra steps" line, the April 2025 precedent paragraph (Ch 10), "Dov did both" resolution (four admitted, eight cut), the closing "not in the market for its own factors sold back to it".
- **Added (isolation, short leg, costs):**
  - Cross-reference to the canonical home at the opening: Chapter 8 (§8.8, "Twelve Residuals"); every short named as a bond borrowed through Vantress's prime broker, cash collateral, recallable.
  - Loading defined (standardized slope; value ≈ half the variance, other four ≈ a sixth, idio ≈ a third).
  - Callback to the cold open's Sharpe 1.9 / beta 0.6 (§9.0) and to Ch 8's orange line, which also read 1.9.
  - Wen's borrow-sheet finding: the eight value pairs were short the richest bond in each cell at ≈30 bp; "the cheapest short to hold is the value short" (mirror of §8D.2's fee slope: 33 bp average, 173 bp before a filing).
  - Isolation arithmetic with the chapter's own breadth formula: $12/(1+11\times0.28)\approx2.9$ → with value named, ρ ≈ 0.17, ≈ 4.2; resizing changes factor exposure, never residual correlation; the remaining 0.17 is illiquidity (§9.6.2).
  - A decision card (hedge, shrink, admit; Ch 8's three doors), graded.
  - Hedge priced: no CDX for value; factor basket long richest / short cheapest quintile, ≈140 lines, ≈\$450mm a side for 0.5 of loading on a ≈\$25mm/yr book (Ch 1-B's \$1.6mm days); short leg = cheap-quintile bonds borrowed at ≈120 bp (between Asquith et al.'s 52 bp post-downgrade and 173 bp pre-filing) or a dealer TRS whose spread is the fee; borrow ≈\$5.4mm/yr + rebalancing ≈\$5mm/yr (5% of each side a month, 0.941% HY LCS) ≈ \$10mm/yr vs ≈\$6mm/yr premium at the §9.12 live IR of 0.5; a long-only factor-tilted fund is mostly beta.
  - Shrink priced: §9.8.1's optimizer with one more constraint row (value loading ≤ 0.2, owned by risk); ≈\$1.6mm half-spreads on quarter-end Wed 30 Sep; DTS-neutral pairs carry ≈0 (§9.2.3), holding cost = long financing net of the short's rebate + fee; book fee 45 → 55 bp after the cut (higher after GM Financial's 25 → 70 bp reset on Tue 6 Oct, Ch 8-D cold open).
  - Admit: four pairs, *value, admitted*, booked on their own explain line (Ch 8-C, Ch 28). PB-01's thesis read as the value score's leverage denominator; PB-19's "toll" sent to the rating-bucket line and Ch 8-D §8D.3 (the 7 Oct ruler review).
  - Outcome: book risk −38%, idio −11%, idio share 34% → 70% (Figure 9.5). Leak column: the value premium on the eight; the unnamed common part at 0.17 > Dov's 0.15 (Ch 19 §19.9.1 closes five on Fri 30 Oct); the habit (new ledger column: short leg's value score beside its fee; Dov's dated sentence, value ≤ 0.25 through 31 Mar 2027).
  - One-line bridge into the Man Numeric telecom case (four witnesses on one issuer vs one witness in twelve cases).
- **Figure 9.5 (new)** `assets/figures/ch09_pair_book_value_loading.png`, script `tools/figures/ch09_rv.py` (hand-set illustrative numbers; prints its checks: loading 0.70 → 0.21, idio share 34% → 70%, vol 0.62×, idio vol 0.89×). Fiction label in caption. Viewed after render: no collisions.
- **Renumbered** the noisy-price figure 9.5 → **9.6** (caption and both text references in §9.9). `state/revisions/ed2/09_ch09_factor_investing_in_credit.figures.md` / `.figcheck.md` still say 9.5 for `ch09_noisy_price_premium`; harmless, noted here for U4.
- **Desk Debrief Finder** row "Combining factors": judgment cell now "Marcus's second x-ray of the Pair Book, hedge, shrink or admit (§9.7.2)".
- **Exercise 7 (new)** "The second x-ray": breadth at ρ 0.25 / 0.15, idio share at loading 0.6, a \$300mm-a-side value hedge at 100 bp borrow and 5%/0.4% turnover vs a \$4mm premium. Different numbers from the scene. No solution inline (matches Ch 9's format); for App Z.

## Nothing removed

No topic, equation, Source Extraction, Trend Watch, exercise, figure, Appendix F link or URL removed. No code blocks added. Pandoc math inline only; currency escaped. Chapter's last line still `<!-- STATUS: COMPLETE -->`. Chapter 30,082 → 31,797 words.

## Ledger and cast

- `state/rv_pair_book.md`: PB-19 "Stressed in" gains Ch 9 §9.7.2 (value admitted, full size); book-level row "Book loading on DTS-neutral value" updated (before/after variance split, ρ 0.17, breadth 2.9 → 4.2, Fig 9.5); new chapter note "Ch 9 (RV weave …)" with pair (the book), legs, hedge method, idio share, three doors priced, what leaked, reconciliation with Ch 8-B and Ch 8-D. PB-03's Ch 9 stress (thread §d, fallen-angel factor) not written: PB-03 is the closed 2020 replay; PB-19 is the live Ford/GM line here.
- `state/cast_bible.md`: entry for the scene (Marcus 7:20 a.m. Wed 30 Sep; Wen's borrow-sheet line and new ledger column; Dov's "two languages" line and dated sentence).

## Consistency notes

- PB-01 and PB-19 are two of the four admitted pairs, so neither is resized on 30 Sep (PB-01 stays \$60mm / \$35mm into October per Ch 1-B, 2, 8-B; PB-19 stays \$40mm / \$60mm until 8 Oct per Ch 8-D). The eight cut are unnumbered (Ch 8-D: twelve live pairs on 6 Oct; Ch 19: five closed on 30 Oct).
- Mild open tension, not introduced here: Ch 8-B §8B.9 says the CCC tier dragged "the four pairs Dov had kept long the cheaper name", but PB-01 is short the CCC-side Halvorsen per Ch 11; read as "some of the four".

<!-- STATUS: COMPLETE -->
