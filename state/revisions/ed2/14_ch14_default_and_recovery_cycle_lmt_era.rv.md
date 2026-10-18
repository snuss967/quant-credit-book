# RV weave log: Ch 14 (Edition 2, user directive 13)

*RV weaver, 2026-10-18. Thread entry: `state/rv_thread.md` §(e) row `14_ch14_default_and_recovery_cycle_lmt_era` (scene; PB-05 closed; competing risks and the re-default clock; H direction / I exchange path / L short leg gaps up, re-default hazard on the post-LME long; T8 home).*

## Preconditions
- `state/rv_thread.md` present and ends `<!-- STATUS: COMPLETE -->`.
- No prior `.rv.md` log; `14_ch14_...log.md` ends `<!-- STATUS: COMPLETE -->` (not busy).

## Read
- `state/rv_thread.md` (spine, homes, Ch 14 row, PB-05 row, rules 1-10); `state/rv_pair_book.md` (PB-05 as opened by the Ch 5 weaver: 5.875% 2028s in the mid-50s, short stock at 0.30 of bond MV, cut at the close Fri 2 Jun 2023, delta resized monthly); `state/cast_bible.md`; `state/reviews/ed2/u2_lessons.md`; `state/style_bible.md` §8.
- Dossiers: `rv_credit_pairs_literature_and_mechanics.md` §5.1-5.6, R11, R15; `case_carvana_svb_wolfspeed_capital_structure.md` §1 (stock closes, stack marks, exchange ratios, h*, S3 count); `trend_re_default_and_recovery_dataset.md` (grep only).
- Chapter: §14.2 (CIFs, $\lambda_H$, $\lambda_D$), §14.3 (mixture-cure clock, 0.175, re-default ledger), §14.4, §14.9, §14.10. Carvana tellings in Ch 5 §5.6.1-5.6.2 and Ch 6 §6.10.1 (so Ch 14 points to them instead of retelling); Ch 24 (SNAC has no Restructuring credit event); Ch 13 §13.5 pod-scene framing; Ch 8-D brief (§8D.2 short-leg menu, §8D.4 jumps, §8D.8 points to §14 for T8).

## What I wrote, and where
1. **Scene** `#### The Pair Book: Carvana, and the short leg that gapped up` plus `#### Decision point: the parole long, 29 September 2023`, inserted at the end of §14.9 (after Ines's "IDO or it didn't happen" paragraph, before §14.10). About 1,800 words of prose plus two tables (about 2,000 words with tables). Fiction label once at the top; replay label (Ch 5 cut-off 2 Jun 2023, folder runs to the Sep 2023 quarter-end).
   - Chapter tool: Owen's competing-risks card, each leg's one-year P&L behind each door ($F_H$ 0.25, $F_D$ 0.60, $S$ 0.15, summing to one per §14.2.1), $\mathbb{E}[\Pi] = F_H\Pi_H + F_D\Pi_D + S\,\Pi_S \approx +\$0.28$mm; then the re-default clock (§14.3.2's 0.175, $1-p = 0.75$) decides the post-exchange long.
   - Legs: long \$10mm face Carvana 5.875% 2028s at 55; short 128,000 shares (0.30 of \$5.5mm MV at the \$12.92 May close), structural-model equity delta; June resize to 0.25 of MV at the company's June mark (about 71,000 shares at \$25.92); July/August resizes frozen by Marcus's 19 Jul risk call (pod practice).
   - H / I / L stated in order: removed direction behind door H (filing leaves the pair +\$0.12mm); idio = the exchange path (2028s got 66.6 vs 89.3 for the 2030s; long 55 → about 51.7 at the 77.7 stack mark, −\$0.33mm); leak = the short leg as the security the exchange restrikes (−\$1.14mm on 19 Jul 2023 alone; −\$2.80mm in four months against −\$0.39mm budgeted; leak −\$2.41mm, about 7× the idio).
   - Costs: stock borrow assumed 15% a year (no tape; labeled) −\$0.14mm less \$0.05mm rebate; no dividend; financing the long at 7% −\$0.12mm; half-spreads −\$0.10mm; coupon carry +\$0.15mm. Net −\$3.29mm; no capture ratio (idio negative).
   - T8 generalised through Dov's PB-01 (borrowed Halvorsen bond short loses the 1-B \$3.9mm behind a premium door D; at $\lambda_D \approx 0.038$, $F_D(1) \approx 3.7\%$, about \$0.14mm a year the DTS ratio never sees) and Carvana as anyone's short leg (2030s from the 2022 year-end mark, mid-40s to about 69). Wen's new column: recalls before a consent record date. SNAC CDS pays on door H only (Ch 24).
   - Decision card graded: keep long + stock short lost again (\$52.94 end-2023, \$203.36 end-2024); keep long naked paid (cure) but carried an unseen parole hazard (2023 cohort 46% re-defaulted by Apr 2025); close kept the mandate. PB-05 closed; post-exchange long declined (no short isolates the parole).
2. **Cross-reference to the canonical home:** "that arithmetic, and the menu of short legs with what each costs, are Chapter 8-D's (§8D.4 and §8D.2)". Ch 14 is itself the home for T8.
3. **Desk Debrief:** one Finder row ("A pair across competing risks", §14.9, Listing 14.2) and one bullet ("In an exchange, the short leg gets the premium").
4. **Ledger:** `state/rv_pair_book.md` PB-05 row updated in place (Ch 14 sizes appended to Legs and Hedge method; Closed in Ch 14 §14.9; status closed; idio share, explain line, what leaked appended to Ch 5's text).
5. **Cast bible:** Ch 14 facts appended to the Owen, Wen, Marcus and Dov entries (rule 8).

## Retired
- None. Ch 14 had no earlier Carvana, pair or short-leg paragraph; §14.9's "long likely-inside, short likely-outside" sentence is a different pair and stays. Ch 5 and Ch 6 Carvana facts (dates, 96.4%, allocation table, TSA terms, S3 count, stock path, stub) are pointed to by §, not retold.

## Protected items
- No topic, equation, Source Extraction, Trend Watch, exercise, figure, Appendix F link or URL removed. No code block added. Chapter last line still `<!-- STATUS: COMPLETE -->`.

## Open items
- **Continuity with Ch 6 (stresses PB-05):** Ch 14 fixes Owen's sizes (128,000 shares at \$12.92; ~71,000 after the June resize; resizes frozen from 19 Jul). If the Ch 6 beat sizes the 19 Jul stress differently, align Ch 6 to the ledger or adjust Ch 14's two numbers (19 Jul loss, short total).
- **Proxies:** the long is marked with Carvana's stack fair-value ratio (77.7 at the Sep 2023 quarter-end, 74.0 at June), not a series price; the \$12.92 entry is the May close (no 2 Jun close in the dossier); the 15% stock-borrow fee is assumed. All labeled illustrative in text.
- **RV figure not made:** the thread's optional "short-leg price path through an exchange" (CVNA closes 12.92 / 25.92 / 39.80 / 55.80 / 41.98 against the 2028s' exchange value) is left for the U4 figures pass (`tools/figures/ch14.py`).
- Ch 8-D section numbers §8D.2 and §8D.4 are taken from its advisor brief; check when that chapter is written.

<!-- STATUS: COMPLETE -->
