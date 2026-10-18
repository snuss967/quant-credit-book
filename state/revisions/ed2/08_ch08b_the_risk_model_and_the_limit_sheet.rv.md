# RV weave log: Chapter 8-B (Edition 2, user directive 13)

*RV weaver, 2026-10-18. Thread entry: `08_ch08b_the_risk_model_and_the_limit_sheet` = scene (Marcus's call), PB-01 and the book, tool = the limit sheet and stop arithmetic, T10 (owner Ch 8-B), home 8-D, figure = stop-out heat map.*

## Preconditions

- `state/rv_thread.md` ends with the completion marker; no prior `.rv.md` log; no `.log.md` for this chapter (not busy).
- Read: thread §(a)–(f) and this chapter's row; `state/rv_pair_book.md` (re-read twice, it changed on disk during the pass: Ch 2 and Ch 3-B writers updated PB-01); `state/cast_bible.md` (Dov, Wen, Marcus, Gordon, Owen; C9, C10, C16); `state/reviews/ed2/u2_lessons.md`; style bible §8; POD dossier §4.1–4.5 (no quotations taken from transcripts marked CHECK).
- Grepped the chapter: no prior mention of pods, pairs, stops, drawdown lines, Dov, Marcus or Vantress. §8B.9 (Theo's Table 8-B.4 and the Whale case) is where the beat belongs; Ch 1-B already points to "§8B.9 (the limit sheet, which is Dov's x-ray seen from the risk manager's chair)".

## What was written, and where

1. **Scene, §8B.9, new `### The Pod's Sheet: Marcus's Call (Pair Book PB-01)`**, inserted after Figure 8-B.5 and before the section's *Builds on* line; decision card promoted to `#### The card at 7:30`. 1,999 words including Table 8-B.5 and the Figure 8-B.6 caption (1,754 words of prose). Fiction label at the top, in italics.
   - **Dated spine.** Fri 30 Oct 2026 (the month's last business day; Gordon Pike's 9 Oct grant on PB-01 from §8D.7 expires). Real anchors: the press-reported two-line shape (eFinancialCareers citing the WSJ, 5 Dec 2025), pointed to §1B.2 rather than re-quoted (one telling); the 15 Oct 2026 CCC tier (§8B.4, FRED). Closes on the in-chapter building-products sector review that Theo's committee asks about on Mon 2 Nov (§8B.9), leg unnamed.
   - **Tool.** The chapter's own engine read as a pod's sheet: Table 8-B.5 (beta, rating bucket, cells, gross, forecast vol, two jump rows, drawdown). The Gaussian layer gives the vol row via Figure 8-B.6; the jump layer (§8B.5's $\text{JTD}_i = \sum_j N_j(P_j - R_j)$) gives the jump rows; the sub-80 equity regime (§8B.4) explains why the DTS hedge no longer offsets Kestrel's spread loading in-model.
   - **Isolation, explicit.** Legs: long Kestrel 6% 2030, short Halvorsen 7.25% 2029 borrowed via the prime broker (102% cash collateral, 300 bp, recallable), CDX HY trim. Hedge: market-value DTS plus the index trim, 0.525 by face kept through the resize. Removes: HY factor and the building-products cell (in-model, via the CDX trim once Halvorsen is in the equity regime). Idio: Kestrel residual ≈ \$0.11mm/day vs Halvorsen ≈ \$0.43mm/day after the resize, the view. Leaks: what the stop counts and the explain does not pay (book drawdown: idio +\$2.6mm, factors −\$13.1mm, friction −\$4.5mm), the common residual, CCC tier via the short, exchange gap −\$2.0mm per 10 points, the recall, and the short's recovery as an opinion (Marcus R 40 vs Theo's desk R 15). Costs: carry ≈ +\$0.05mm/yr after the resize (Kestrel \$2.25mm, owed \$1.43mm, fee \$0.46mm, financing net of rebate ≈ \$0.3mm), half-spreads ≈ \$145k to resize.
   - **T10 proved with numbers.** Stop → size: hard (second line) \$21mm/0.56 = \$37.5mm face; soft (first line) \$9mm/0.56 ≈ \$16mm. Stop → vol budget: Sharpe 1 at 6.3% touches 6% in ≈31% of years, 9% in ≈7%; at 8%, ≈53%; from −\$15mm with 42 trading days to year-end, ≈22% / ≈1.4% (simulated; fictional run). Pod sentence: *The hedge sets the ratio. The stop sets the size.*
   - **Cross-reference to the canonical home:** Chapter 8-D, §8D.5 (sizing a pair to the stop; the training-sheet arithmetic is pointed to, not retold), plus §8D.7 (Gordon's grant) and §8D.2 (the short-leg menu, the ~100 CDS names). Other pointers: §1B.2, §4C.3, §13.5, §8.8, §9.7.2, §2.9.4, Chapter 22, Chapter 14, Chapter 28, §28.6.
2. **Table 8-B.5** (the pod's limit sheet, illustrative) inside the scene.
3. **Figure 8-B.6** `assets/figures/ch08b_stopout_heatmap.png` (107 KB, viewed): stop-out probability heat map, Sharpe × vol, Dov's 6% and 9% lines, his 6.3% column outlined. Script `tools/figures/ch08b_rv.py` (seeded, 200,000 paths per Sharpe row, common random numbers; reproduces the POD §4.3 checks 71.9% and 42.6% as 71.6% and 42.9%). Kept apart from `tools/figures/ch08b.py`.
4. **Desk Debrief:** one bullet added (the stop is the sheet; it counts net P&L, not the explain; the hedge sets the ratio, the stop sets the size).
5. **Exercise 7** (the stop as a size, for a pair; different numbers from the scene; solved number-first with a Check line).
6. **§8B.9 *Builds on / Used in* line:** added §8D.5 and §28.6.

## Retired

Nothing. Ch 8-B had no earlier telling of the stop, the pod sheet or PB-01 to retire. One telling per fact was kept by pointing rather than retelling: the 5 Dec 2025 quotation stays in §1B.2; the \$25.9mm / \$8.6mm training sheet and the reflection-principle Math, Gently stay in §8D.5; the borrow-fee and recall story stays in Chapter 22 and §2.9.4; the DTS-drift arithmetic stays in §1B.2 and Chapter 11. No topic, equation, Source Extraction, Trend Watch, exercise, figure, Appendix F link or URL was removed. No code blocks added. Chapter still ends with its completion marker.

## State files updated

- `state/rv_pair_book.md`: PB-01 row (stressed column gains 8-B; status gains 8-B; ratio cell notes 0.525 kept after the 30 Oct resize to \$37.5mm / \$19.7mm; what-leaked cell gains the Ch 8-B line); book-level rows Book beta (+0.03, 29 Oct), Largest JTD (**reconciled**, below), Stop distance (30 Oct values); a Ch 8-B note appended above the ledger's completion marker.
- `state/cast_bible.md`: new block "Ch 8-B additions (RV weave, 2026-10-18)" before Contradictions (story times, Dov's second line \$36mm as new canon, Marcus's and Wen's lines, Gordon receives the soft-breach note).

## Reconciliation recorded (the ledger asked Ch 8-B to make it)

The \$5mm "single-issuer jump line" (Ch 4-C, Ch 13, the thread's mandate) and Kestrel's ≈\$34mm JTD are both kept: Table 8-B.5 writes the jump in two forms. Inside one capital structure (PB-02, PB-06, PB-08) the pair's net JTD at model recovery is capped at \$5mm. Across issuers (PB-01, PB-19) each leg's JTD by itself is tested against the drawdown lines: soft through the first (\$24mm), hard through the second (\$36mm). This also fits Ch 8-D, which sized JTD against the stop distance.

## Flags for the orchestrator

1. The thread's table names the home as "8-D §D.6"; in the written Chapter 8-D the sizing section is §8D.5 (§8D.6 is the ledger). The beat points to §8D.5.
2. Dov's second line (\$36mm, 9%) is new canon; Ch 28 (PB-01's close, Dov's year) should use it or say otherwise.
3. The 30 Oct building-products sector review moves PB-01's rating-bucket row "without a trade"; which leg (if either) was downgraded is left unnamed for Ch 11/12-B/28 to settle against Halvorsen's B3 (Ch 11) and Exercise 5's hypothetical CCC downgrade.
4. Marcus's model carries Halvorsen at R 40 while Theo's desk uses 15 (§8B.5); the scene leaves it as "the part Marcus left for next month", a hook for Ch 8-C or Ch 28.

<!-- STATUS: COMPLETE -->
