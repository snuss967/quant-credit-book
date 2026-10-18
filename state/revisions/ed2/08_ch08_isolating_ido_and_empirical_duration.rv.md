# RV weave log: Chapter 8 (Edition 2, user directive 13)

*RV weaver, 2026-10-18. Thread entry: `08_ch08_isolating_ido_and_empirical_duration` = Long Scene (new §8.8 subsection) + PB-03 opened in §8.4; pair PB-03 and the whole book; tool = the IDO ledger; H = everything the factor model names, I = whatever is left, L = the book's residuals correlate about 0.3 (T1 proved); events 25 Mar 2020 (Ford to BB+) and the Fed facilities of 23 Mar / 9 Apr 2020; home 8-D; figure = residual correlation heat map.*

**Outcome: strengthened.** Both assigned beats already existed (the PB-03 `> **The Pair.**` box in §8.4 and the Long Scene "Twelve Residuals" in §8.8, both written earlier on 18 Oct 2026), so no second beat was written. Each was checked against the thread entry and strengthened in place.

## Preconditions

- `state/rv_thread.md` ends with the completion marker; no prior `.rv.md` log for this chapter; `08_ch08_isolating_ido_and_empirical_duration.log.md` ends with the completion marker (not busy).
- Read: thread §(a)–(f) and this chapter's row; `state/rv_pair_book.md` (PB-03 row, book-level lines, Ch 7, Ch 10, Ch 19, Ch 8-D, Ch 8-B notes); `state/cast_bible.md` (Dov, Wen, Marcus, C16, Ch 8 / 8-D / 8-B / 19 blocks); `state/reviews/ed2/u2_lessons.md`; style bible §8; PAIRS dossier R9, R11, §5.1, §5.2, §5.5; POD dossier §3.4, §4.5.
- Cross-checked for continuity: Ch 1 §1.8.2 and Figure 1.5 (23 Mar SMCCF, ETF discounts 3.1–5.0% on 12 Mar 2020, 9 Apr extension); Ch 7-B PB-03 box; Ch 9 §9.7.2 (same Tuesday, value loading 0.7 → 0.2); Ch 10 Coda; Ch 19 §19.9.1 (the five pairs closed Fri 30 Oct); Ch 24 §24.7 (PB-03 closed); Ch 8-D §8D.1 (PB-19 opened 24 Aug 2026) and §8D.6 (ledger reads 0.28 for September).

## What was strengthened, and where

1. **§8.4, PB-03 box** (now about 600 words).
   - *Real short leg:* GM Financial bonds borrowed through the prime broker from an agent lender against 102% cash collateral marked daily, every coupon owed back (PAIRS R11 mechanics); GM Financial protection named as the menu's other short, pointing to Ch 24 (basis).
   - *Isolation / leak:* the open rating-bucket factor now has its dated policy edge: the Fed's 23 March 2020 corporate facilities were investment-grade only, the short leg's issuer sat inside that line and the long sat outside it from 25 March, so the next word on the line would move the pair without consulting Ford's credit (Ch 24 and Ch 7-B already record the 9 April extension).
   - *Costs:* financing added (cash rate + 40 bp on about \$22mm MV ≈ \$0.09mm a year, the cash rate near zero after 15 March; the short's collateral earns the cash rate less the fee already counted); running lines ≈ \$0.15mm over the six-month horizon; exit half-spreads now "if the market is still this wide" (Ch 24 prices the exit at \$0.2mm in September).
   - *Cross-reference to the canonical home:* "Chapter 8-D (§8D.1) reopens the same two captives live in August 2026 as PB-19."
2. **§8.8, Long Scene "Twelve Residuals"** (now 1,704 words of prose plus Figure 8.6).
   - Fiction label widened (loadings, costs; the March 2020 ETF discounts named as public).
   - *The book's two legs made visible:* Wen's ranking by loading: five unnumbered pairs carry more than half the component; PB-19 (the live Ford Credit / GM Financial pair) seventh; PB-01 (long the tighter name since April 2025) least, same sign.
   - *Isolation explicit at book level (T1):* a new paragraph written "the way the ledger writes a single pair": H = everything the vendor model names (market spread, sectors, rating buckets, key-rate curve); I = about two-thirds of each pair's residual variance after the first PC; L = the other third, one factor long in every pair, which is most of the book's idio variance because independent pieces diversify and a shared piece does not.
   - *Marcus's three answers priced, with a real short leg:* hedge = a DTS-matched package short HYG (borrowed shares, deep lending pool) against sold CDX HY protection, short cash bonds / long the contract, carrying close to nothing (§8.4), running cost ≈ 30 bp a year (share fee, futures for the ETF's rate duration), correlation ≈ 0.4 to the component so a minimum-variance hedge on an impure proxy (§8.6) removes ≈ a sixth, and it leaks the ETF's premium/discount to NAV (3–5% below on 12 Mar 2020, Ch 1 Figure 1.5). Shrink = close the five heaviest (two legs of half-spread on ten lines, five borrows returned, expected residual given up), leaving the seven at ≈ 0.14. Admit = report the line and be paid as a factor (Ch 28).
   - *Decision and continuity:* Dov declines the package ("That isn't a hedge. That's a thirteenth pair.") and writes the five names under his 30 Nov sentence; Ch 19 §19.9.1 closes them on the last Friday of October.
   - *Cross-reference to the canonical home:* "Chapter 8-D (§8D.6) finds it a week later, still there, on the bottom line of the ledger where the life of every pair in the book is kept."
3. **Figure 8.6** `assets/figures/ch08_residual_heatmap.png` (70 KB, viewed): the thread's residual correlation heat map, before and after step three, five heaviest outlined, PB-19 and PB-01 labeled. Script `tools/figures/ch08_rv.py` (one-factor simulation, 60 days, seed searched from a fixed base until the sample matches the text: mean 0.276, PC1 share 0.355, five carry 62% of squared loadings, seven left at 0.144, mean −0.09 after removal). Kept apart from `tools/figures/ch08.py`. No other figure renumbered (Figures 8.1–8.5 all precede it).
4. **Desk Debrief:** one bullet ("A book's idio is not the sum of its pairs' idio").
5. **Exercise 7** ("The crate, at book scale": sixteen pairs at 0.2, a package at 0.5; different numbers from the scene; Check line \$400k / \$800k; 80%; a quarter, ≈ \$716k).

## Retired

No paragraph retired: the box and scene were already the single tellings of PB-03 and the common residual, and the additions extend them rather than repeat another section (the ETF discount is pointed to Ch 1 Figure 1.5, not retold; the ρ² hedge arithmetic points to §8.6; pay to Ch 28; the close of the five to Ch 19). Two in-box phrasings were tightened ("recallable" kept once, in What leaks). No topic, equation, Source Extraction, Trend Watch, exercise, figure, Appendix F link or URL was removed. No code blocks added. The chapter still ends with its completion marker.

## State files updated

- `state/rv_pair_book.md`: PB-03 row (opened-in cell and what-leaked cell, incl. the financing reconciliation); book-level "Residual correlation" row (ranking, hedge test, shrink, figure); a Ch 8 note appended above the ledger's completion marker.
- `state/cast_bible.md`: new block "Ch 8 additions (RV weave, 2026-10-18)" before Contradictions (Wen's pricing, Dov's line and the five names, PB-03 box adds no cast facts).
- `state/open_items_ed2.md`: three rows under the Ch 8 table.

## Flags for the orchestrator

1. **Ch 24 §24.7 reconciliation (open).** Ch 8's PB-03 box now carries financing (≈ \$0.09mm a year, ≈ \$0.045mm over six months). Ch 24's close totals "some \$0.75mm" without it; with it, all-in ≈ \$0.8mm, net ≈ \$0.45mm, capture ≈ 0.6 rather than "about two-thirds". Ch 24 should add the clause or say financing is charged at book level.
2. **Facts outside the dossiers:** GM Financial's investment-grade ratings in March 2020 and the 15 Mar 2020 FOMC cut to 0–0.25% are well-known but not dossier-sourced (logged).
3. **Figure numbering:** Figure 8.6 is new; if the figures pass inserts `ch08_condition_number_ridge.png` in §8.6, it must renumber this one to 8.7.
4. App Z has no solution entry for the new Exercise 7; its Check line is inline.

<!-- STATUS: COMPLETE -->
