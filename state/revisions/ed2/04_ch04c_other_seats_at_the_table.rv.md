# RV weave log: Ch 4-C, Other Seats at the Table (Edition 2, user directive 13)

*RV weaver, 2026-10-18. Thread row: `04_ch04c_other_seats_at_the_table` = existing box, number it PB-02; tool = seven ledgers; "add the ledger number and the horizon line"; Day 3, 10:00; home Ch 12-C; figure = existing Fig 4-C.2 (no new figure). Truth illustrated: T6 (near default, match on market value and hedge a default only within one issuer's capital structure; owners Ch 12-B / 12-C), with T5 (the real short leg) and T9 (costs) in the box's cost line.*

## Preconditions

- `state/rv_thread.md` present, ends COMPLETE. No prior `.rv.md`. No `04_ch04c...log.md` (no reviser mid-flight). Chapter not modified in `git status` before this pass.

## What was written, and where

1. **§4C.3, the existing `> **The Pair.**` box rewritten in place as Pair Book entry PB-02 (595 words, four paragraphs).** Fiction label at the top (Owen's pod at Vantress, fictional composites; Halvorsen fictional; positions, prices, fees, P&L illustrative). Thesis; **Horizon** line (to the plan vote, inside the pod's one-year clock of §4C.1's Math, Gently, or the drop-down's close); Legs (long \$10mm 7.25% secured at 79; short \$3.8mm 6% 2031s at 55 borrowed from an asset manager's lending desk via the platform's prime broker on an overnight loan; Halvorsen CDS named and rejected as the short because it pays on the cheapest deliverable, pointer to Ch 24's basis); hedge construction (recovery-weighted market value, $h = 0.19/0.50 = 0.38$ face per face, 0.26 by MV). Removes: the default question and, incidentally, rates (\$1,300/bp leftover). Idio: $R_{\text{sec}}$ (P&L-in-default formula kept; \$100k/pt secured vs \$38k/pt unsecured; +\$0.5mm at 65, −\$4.5mm at Theo's 15, now placed just inside the platform's \$5mm single-issuer jump line). **Leaks, stress-tested with this chapter's tool:** "run §4C.9's table down each leg instead of down the bond." Day 12's −\$196k (long 79 → 74, −\$500k; 2031s 55 → 47, +\$304k) is decomposed: scaling the 2031s' 8 points by distance from par to recovery (95 vs 40) implies 3.4 points on the long, so ≈ \$163k is the CLOs' month-end selling of the pari TLB arriving on one leg only (flagged by the day-8 `forced_pressure` reading, §4C.4), and ≈ \$33k is the ruler (sized for the day of default). Second seat: the short's lender recalls for its vote when unsecured holders organize (§4C.8). Costs (R11 mechanics): coupon \$725k, financing \$7.9mm at 5.5% ≈ \$435k, short coupon owed \$228k, rebate on 102% collateral of \$2.09mm at 4.00% cash − 2.00% fee ≈ \$43k (fee set inside Asquith et al.'s 173–245 bp around bankruptcies, 2004–07); net ≈ \$105k/yr, ≈ \$20k if the fee resets to 6%; two legs of one-point half-spread ≈ \$140k each way. The old box's claim that the fee is "roughly offset by the interest earned on the short-sale cash" is replaced by the explicit rebate line (cash 4.00% matches §8D.2's illustrative rate).
2. **Cross-reference to the canonical home:** "§12C.2 turns Owen's 60 into the probability that plan value lands between the class's strikes; that is where this idio is priced."
3. **§4C.3 seat label:** now names "his platform, Vantress Capital Management" as invented (the cast bible makes 4-C Owen's introduction; Vantress was unnamed in the chapter).

## Retired (one telling per fact)

- **§4C.3 ¶ "So Owen took the third hand…":** the jump-to-default arithmetic (recoveries 60 / 5, \$1.9mm, 0.50 per \$1, \$3.8mm) now lives only in the box; the paragraph keeps the trade, the Ch 3-B pointer ("built from two bonds of one issuer instead of a bond and its CDS") and points to the box as PB-02.
- **§4C.3 ¶ "By day 12…":** "down five points on the long, \$500,000, while the short had made back only part of it" → "the pair was losing money on a day when nothing in Owen's documents had changed"; the leg numbers are told once, in the box.
- **§4C.3 ¶ "He did not have to…":** "A \$500,000 loss on a pod…" → "A loss of a couple of hundred thousand dollars on a pod…" (consistent with the pair's −\$196k rather than the long leg alone).
- **Desk Debrief bullet** on pairs: "leaks spread beta, borrow and carry" → "leaks the ruler, the borrow, the carry and the other seats' calendars; run the seat table down each leg, because forced selling arrives one leg at a time."
- Nothing protected removed: no equation, Source Extraction, Trend Watch, exercise (Exercise 4's −\$200,000 and recall answer still match), figure, Appendix F link or URL touched. Old box's "IDO or it didn't happen" sentence dropped (Law 1 is stated in Ch 1-B and App E).

## Ledger and cast

- `state/rv_pair_book.md` PB-02: status planned → **open (Ch 4-C)**; legs with the named lender and CDS rejection; ratio 0.38 by face / 0.26 by MV; idio share ≈ 0% on day 12 (all leak); what leaked = ≈ \$163k holder-base flow on the long + ≈ \$33k ruler, recall-for-vote risk, carry and half-spreads, day-30 \$114k coupon saving (told in §4C.8); still to come: attachment points move (12-B, 12-C).
- `state/cast_bible.md` Owen entry: Vantress named in 4-C; PB-02 numbered with sizes, horizon and day-12 loss.

## Checks and open items

- `tools/check_book.py --file`: 14,551 words (was 14,476); its four "missing anatomy" warnings (math, ai_spec, source_extraction, case_study) pre-date this pass. Pandoc renders the box's three inline math spans. No code blocks added; currency escaped; chapter's last line remains `<!-- STATUS: COMPLETE -->`.
- The \$5mm single-issuer jump line and the one-year horizon are the thread's illustrative mandate and §4C.1's clock respectively; the thread mandate's "one to nine months per pair" is looser than §4C.1's one-year pod clock; 8-B / 8-D should state which governs Owen's pod.
- The issuer-canon CHECK comment at the top of the chapter (7.25s secured here per §12B.9, unsecured in Ch 1) is untouched; PB-02 follows §12B.9.
<!-- STATUS: COMPLETE -->
