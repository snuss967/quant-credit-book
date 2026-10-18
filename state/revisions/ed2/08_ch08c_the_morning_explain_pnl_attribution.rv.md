# RV weave log: Chapter 8-C (Edition 2, user directive 13)

*RV weaver, 2026-10-18. Thread entry: `08_ch08c_the_morning_explain_pnl_attribution` = worked morning, PB-01, tool = the explain, T9 (owner Ch 8-C, home), H: market line with start-of-day betas, I / L / friction / capture ratio (PAIRS §5.6), the FCM roll mismatch (canon), figure = pair explain waterfall.*

## Preconditions

- `state/rv_thread.md` ends with the completion marker. No earlier `.rv.md` log existed, and there was no `.log.md` for this chapter, so nobody else was working on it.
- Read: thread §(a) to §(f) and this chapter's row; `state/rv_pair_book.md` (re-read after it changed on disk; PB-01 row, book-level lines, chapter notes); `state/cast_bible.md` (Dov, Wen, Marcus, Gordon, Bea; C9, C10, C16; the Ch 3-B and Ch 8-B blocks); `state/reviews/ed2/u2_lessons.md`; style bible §8; PAIRS dossier §5.1 to §5.6 (R7, R11). Also read the canon this beat touches: §1B.2 (PB-01, the 7:15 x-ray, the 2:40 trim, the \$140k OMS/FCM roll break), §3B.4 (PB-01's clocks, Marcus's "Right ruler. Wrong day."), §8D.6 (ledger, κ definition, PB-19's September, Exercise 5 already uses the PAIRS §5.6 numbers), §22 (fee 50 → 300 bp), §27.4.2 (the roll as a bitemporal bug) and §28.8 (the year-end packet folds the coupon differential into idio).
- Grepped the chapter. Before this pass it had no pair, pod or Pair Book content, apart from the §8C.5 View From Another Seat (*The multi-strategy platform*). The hedge-leg mechanics (§8C.2), financing and day-one (§8C.3) and the two worked mornings (§8C.6) are the tools the beat reuses.

## Design decision

The PAIRS §5.6 numbers (+\$40.5k idio, −\$12.96k, −\$14.2k, capture 0.33) already appear in Ch 8-D, scaled for PB-19's September and verbatim in Exercise 5. Repeating them here would have told the same fact twice. So the beat builds PB-01's own explain from canon positions, and it lands on the thread's capture ratio of 0.33. It uses the chapter's own lines: accrual (custodian) apart from pull-to-par (model), factor spread, issuer-curve idio, the fee, financing net of the rebate, and day-one against the composite. The FCM break is handled as an explain question: it is a book-level named line, not a pair cost. This avoids restating the break's mechanics.

## What was written, and where

1. **Scene, §8C.6, new `### Morning (c): the pair, at Vantress`.** It sits after Figure 8-C.3 and before the section's *Builds on* line. The section is retitled `## 8C.6 Three Worked Mornings`. Length is 1,918 words including the table and the Figure 8-C.4 caption, about 1,550 words of prose. The fiction label is at the top, in italics.
   - **Spine.** Wed 14 Oct 2026, 7:15 a.m. at Vantress (the morning after Ch 1-B's Tuesday). Wen folds the platform's Tuesday explain into idio, leak, friction and net. The platform's default pair report priced the market line on the 4:00 positions and spread book-level CDX lines across pairs by DTS gap. The decision card is posed before the answer. Marcus walks over at 7:40 and Dov comes in at 7:55. The new pod sentence goes on the wall.
   - **Legs and short leg.** Long \$60mm Kestrel 6% 2030. Short \$39mm Halvorsen 7.25% 2029, in bonds borrowed from an asset manager's agent lender through the prime broker, against 102% cash collateral, recallable on demand, at a 300 bp fee. From 2:40 the pair also holds about \$13mm of CDX HY protection sold (illustrative). That index position is now PB-01's third leg, with its own coupon, factor and series-roll lines.
   - **Hedge construction.** Market-value DTS, 0.65 by face, set in April. Start-of-day DTS is 70,200 against 98,000, the 7:15 x-ray. The trim was to \$35mm plus the CDX sale.
   - **What the hedge removes.** The shared rally (+\$140,400 on the long against −\$196,000 on the short) and the building-products factor.
   - **Idio.** +\$132,900: Kestrel 3 bp tighter on its own (+\$62,900) and Halvorsen lagging the rally by 10 bp (+\$70,000).
   - **What leaks.** −\$61,600 in total. The ruler, priced on the start-of-day ratio, is −\$55,600. The rates residue is −\$6,000: about \$12,000 of DV01 net long, because the legs were matched on spread risk and the price fall shortened the short. The CDX slice will carry its own roll leak from now on.
   - **Friction.** −\$26,860 in total: accrual +\$10,000, coupon owed −\$7,850, pull-to-par +\$1,170 and −\$5,970, fee −\$2,540, financing net of the rebate −\$1,670, day-one on the cover (78.75 against a 78.35 composite) −\$16,000, and CDX half-spread −\$4,000.
   - **Net and capture.** Net is +\$44,440 and the capture ratio is **0.33**. The same day priced on the 4:00 ratio gives idio +\$77,300, leak −\$6,000 and capture 0.57, with the same net. That is "the 2:40 trade paid for hedging ten o'clock."
   - **Further points.** The carry convention is stated in the report header. This pod puts carry in friction, while §28.8 folds the coupon differential into idio. Standing cost without the two trades is \$6,860 a day, about \$2.5mm a year. The borrow sheet shows about \$3,000 per business day; the gap is the short's pull-to-par, about 5.5 points a year at an unchanged yield, which is the premium for the default the short holds (§5.1.4). The thesis was sized at about \$1.2mm a year. Marcus: "Right ruler. Right day." (a callback to §3B.4).
   - **T9 stated once.** Judged on idio, paid on the net. The pay mechanics point to Ch 28.
   - **Cross-reference to the canonical home:** §8D.6 (the Pair Book ledger row and κ). The scene also points to §1B.2, §3B.4, §5.1.4, §8B.9, §8D.3, §8C.2, §8C.3, §8C.5, Chapter 10-B, Chapter 27, Chapter 28 and §28.8.
2. **Table** (the PB-01 pair explain for Tuesday, labeled illustrative) inside the scene.
3. **Figure 8-C.4** `assets/figures/ch08c_pair_explain_waterfall.png` (58 KB, viewed). It has two waterfall panels, idio → leak → friction → net: one on the start-of-day ratio (κ 0.33) and one on the 4:00 ratio (κ 0.57). The script is `tools/figures/ch08c_rv.py` and its printed checks match the scene's numbers. It is kept apart from `tools/figures/ch08c.py`. **Renumbered:** the Whale figure is now 8-C.5 and the unexplained-by-day figure is now 8-C.6. Only the captions changed, and nothing in the prose cited those numbers.
4. **Learning objectives** (cold open's "By the end of this chapter"). Added one clause: regroup a pair into idio, leak and friction with the hedge priced as it stood at the open, and read its capture ratio.
5. **Desk Debrief.** Added one bullet: a pair is judged on idio and paid on the net; price the hedge as it stood at the open; carry, fee, financing and half-spreads decide most pairs; the capture ratio goes on the ledger row (§8C.6, §8D.6).
6. **Exercise 8C.7** (the morning's ratio). It uses different numbers from the scene and is solved number-first with a *Check*. It shows a negative capture ratio, and a meaningless one of 3.4 when the 4:00 ratio sends the idio line negative. The rule: when idio is negative, the ledger leaves κ blank.
7. **§8C.6 *Builds on / Used in* line.** Added §1B.2 to Builds on. Added §8D.6, Chapter 27 and §28.8 to Used in.

## Retired

- **§8C.5 View From Another Seat (*The multi-strategy platform*).** Its generic sentence, "Portfolio managers are typically paid a share of their own P&L, with factor exposure hedged or charged centrally, so the platform's explain strips factors first and pays on what is left", is cut to one clause ("its explain strips factors first and judges each pod on what is left") plus a pointer to Morning (c), which now tells it with numbers. The rest of the box (cross-terms between pods, the single-desk analogue, the *Odd Lots* citation) is kept.
- **Nothing else retired.** No topic, equation, Source Extraction, Trend Watch, exercise, figure, Appendix F link or URL was removed. No code blocks were added. The chapter still ends with its completion marker. It has grown from 14,038 to about 16,260 words.

## State files updated

- `state/rv_pair_book.md`, PB-01 row:
  - Stressed column: "8-C" replaced by a full entry.
  - Status gains 8-C.
  - Idio share gains the Tue 13 Oct line.
  - Capture gains "0.33 (Tue 13 Oct, one day; 0.57 on the 4:00 ratio)".
  - What-leaked gains the Ch 8-C line.
- `state/rv_pair_book.md`, other changes:
  - The book-level Capture ratio row records the pair-level convention 8-C fixes: start-of-day ratio; the leak and friction groups; carry placement stated in the header; κ blank when idio is negative.
  - A Ch 8-C note is appended above the ledger's completion marker.
- `state/cast_bible.md`: new block "Ch 8-C additions (RV weave, 2026-10-18)" before Contradictions. It records story times, lines for Wen, Marcus and Dov, the platform's default pair report as a new fictional fact, and a continuity flag on the real calendar (below).

## Flags for the orchestrator

1. **Real calendar against canon. Mon 12 Oct 2026 was Columbus Day.** SIFMA recommended a full close for US dollar fixed income (press release, 29 Sep 2026, sifma.org). ICE Clear Credit's 2026 holiday schedule lists 2026-OCT-12 as a clearing holiday for the New York group (CDX, North American single names). Several chapters treat that Monday as a trading day:
   - Ch 1: "78 as Monday's open".
   - Ch 1-B: the FCM booked the roll Monday, with "Monday night" variation margin and series that "moved differently on Monday".
   - Ch 8-B: "Monday's 78"; equity regime "since 12 Oct".
   - Ch 27: "the FCM's record said Monday".

   Ch 8-C's scene asserts nothing about Monday's market. It mentions only "Monday's run" of the risk model, which can happen on a holiday. Proposed fix for those chapters: move the Halvorsen open and the FCM's booking to Tue 13 Oct (the FCM books the Friday roll on its next clearing day), or say the platform ran its batch on a day the bond market was shut.
2. **New quantified point for later chapters.** At 78, the short's pull-to-par makes PB-01's explain-basis standing cost about \$6,860 a day (about \$2.5mm a year). Ch 1-B, Ch 2, Ch 22 and Ch 8-B quote coupon-basis carry only (about −\$3,000 per business day, then +\$0.05–0.08mm a year after the cover and the resize). Those figures stay correct as borrow-sheet numbers. Ch 28 (PB-01's close) should state which convention its carry line uses.
3. **Carry convention.** 8-C prints coupons and pull in friction and names the convention in the report header. Ch 28 §28.8 folds the coupon differential into idio. The scene presents both as defensible as long as the header says which one is used. Ch 8-D §8D.6's friction definition (fee, financing, transaction cost) is silent on carry. A one-clause addition there ("and carry, where it is not zero") would align it.
4. The thread table names no home for 8-C beyond itself. The beat's cross-reference is to §8D.6, where κ is defined and recorded.

<!-- STATUS: COMPLETE -->
