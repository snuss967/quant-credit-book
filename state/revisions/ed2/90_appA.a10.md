# Progress log: 90_appA §A.10 "The Phrasebook: RSSG to Quant" (Ed2, synthesis A6 / coach gap 3)

Sources read: synthesis row A6 and D6; transition-coach gap 3 and §"Write the dictionary"; style bible §8; `state/rv_thread.md` (T1–T12, Pair Book, short-leg menu, capture ratio); Part I opener line 7 (points to §A.10); section headings of every chapter in `book_src/` to anchor each row to a § that exists.

Plan: 60–90 rows in seven themed tables (capital structure; valuation; process and documents; risk and P&L; execution; relative value; careers), each with a short warm lead-in paragraph, columns Banker says / Desk says / Formula or tool / Built in / What changes. Insert before the file's final `<!-- STATUS: COMPLETE -->`.

Section anchors checked against headings (not every ed2 file in the TOC exists yet: no 02-B, 4-D, 9-B, 10-B, 13-B, 17-B, 18-B, 00_01, 00_02; rows cite only existing sections).

- [x] 1. Intro paragraphs and how to read a row (cold-open vignette: "the fulcrum is the seconds", heard three ways; Kaz's first-class lever)
- [x] 2. Capital structure table (9 rows: fulcrum as most JTD per point of value, waterfall, recovery P vs Q, seniority as document variable, equity cushion, covenant headroom, OTM equity, CCC bond, DIP)
- [x] 3. Valuation table (12 rows: comps as factor model/ESP, trading levels as composite prior, marks, SPiDER, adjusted EBITDA, base/downside case, pricing-in as Q, runway, yield, plan value, horizon h)
- [x] 4. Process and documents table (15 rows: credit agreement graph, baskets, thresholds, holder vector, co-op, uptier, drop-down, blocker, amendment diff, clocks, cramdown strike, CoC put, court, the wall)
- [x] 5. Risk and P&L table (10 rows: size as DTS, four exposure lines, hedged-to-what, explain, IDO, Kelly, breadth, stop as size, PM option)
- [x] 6. Execution table (8 rows: short menu with costs, bid as reservation price, adverse selection, markout, liquidity, BWIC, PT, ETF band)
- [x] 7. Relative value table (11 rows: pitch as pair ticket, long fulcrum/short junior, rulers, market neutral, idio, capture ratio, cap-structure arb, basis, crowding as borrow fee, catalyst as exit, post-reorg supply)
- [x] 8. Careers table and close (8 rows: five businesses, model review, hit-rate SE, Edge Ledger decay, ROBO spec, deflated Sharpe, pay as a call, first ninety days; closing paragraph, no rule list)
- [x] 9. Checks: 71 rows; ~3,300 prose words (3,970 by raw `wc -w`, pipes included); every table row 6 pipes; currency escaped; inline math has no inner padding; `tools/check_book.py --file` OK; prescriptiveness bullets% 77.5 → 69.0. Inserted as lines 264–392, before the file's final status line.

Notes for later passes: "capture ratio" collides in name with §11.2's up/down capture (row says so). §8-C does not yet carry the capture ratio (the rv_thread plans it there); the row cites §8D.6 where it is defined. The Ch 18 reservation price uses $\tau$ for the horizon; the row writes $(T-t)$ to respect §A.3.
<!-- STATUS: COMPLETE -->
