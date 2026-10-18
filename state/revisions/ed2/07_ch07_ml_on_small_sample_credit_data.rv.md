# RV weave log: Chapter 7 (ML on Small-Sample Credit Data)

*RV weaver, Edition 2, user directive 13, 2026-10-18. Thread entry: `state/rv_thread.md` §(e) row `07_ch07_ml_on_small_sample_credit_data`: scene in §7.4–7.5, "the Pair Book panel", tool = triple barrier in DTS space + meta-labeling; H: label on the residual differential; I: what the model is allowed to predict; L: a missing factor becomes a feature with a great backtest (T3); event: Kaz's 3,000 backtests (canon); homes Ch 7-B, Ch 8 §8.8; RV figure: residual-differential path with the three barriers.*

## Preconditions
- `state/rv_thread.md` present and marked complete; no prior `.rv.md` log; `07_ch07_ml_on_small_sample_credit_data.log.md` ends with the complete marker (not busy).

## What already existed
- A ~300-word bold-run-in scene "The Pair Book panel" in §7.4 (lessons pass): 400 pairs, Sharpe 2.4 → 1.6, rating-bucket feature, Marcus's line, Wen's 0.35, Dov's rule. No legs, no hedge arithmetic, no costs, no short leg, no meta-labeling, no figure.

## What I wrote, and where
1. **§7.4, Act 1 (replaces the old scene; one telling).** `**The Pair Book panel.**` bold run-in, right after "Strip the carry", ~1,200 words of prose plus Figure 7.1. Fiction label once at the top. Worked pair **PB-19** (nine days old on Wed 2 Sep 2026):
   - Legs: long \$40mm MV Ford Motor Credit senior unsecured (95, Z 180, SD 4.5); short \$60mm MV GM Financial senior unsecured (98, Z 120, SD 4.5), borrowed via Vantress's prime broker from one asset manager's agent lender at 25 bp, 102% cash collateral, recallable on demand, coupons owed (all consistent with Ch 8-D).
   - The chapter's tool: one new unnumbered display equation, $r_{\text{pair}} \approx -\text{DTS}_L(\Delta\log s_L - \Delta\log s_S)$ under market-value DTS matching, so a pair is one corridor on the log spread ratio. Ratio 1.50 (DTS 0.081 vs 0.054); spread carry zero (\$720k each way, §8.4); differential relative vol $9\%\sqrt{0.4}\approx5.7\%$/month; 13-week half-width 0.80% of the long ≈ \$320k.
   - Costs: borrow \$150k + financing \$160k + half-spreads \$120k = \$430k/yr (Ch 8-D's numbers) ≈ \$108k a corridor; a +1 label ≈ \$320k idio ≈ \$210k P&L before leaks (capture → Ch 8-C).
   - Wen's edits: label paid for carry and beta; struck 31 candidates with no lender and no CDS; a recall is a side door (`touch = "exit"` at the buy-in price, §7.4's censoring rule).
   - Three labels: equal-dollar 2.4 → research's residual (DTS-scaled market + carry) 1.6 with the rating-bucket feature → Marcus's whole sheet (bucket + sector) 0.9; PB-19 top decile → mid-list; ≈0.4 of research's idio was the bucket (echoes PB-19's Sept idio share 0.58, §8D.6).
   - Leak (T3): Marcus's "factor with a great backtest"; Wen's 0.35 with the Collin-Dufresne, Goldstein and Martin (2001) quotes kept verbatim from the old scene; surviving feature = short leg's equity short interest within its rating bucket (Dynkin et al., *Systematic Investing in Credit*, ch. 21, verified on PDF p.794), priced by the lender ("The lender reads that column too").
   - Reader's card (alpha or factor, and which number), graded: the deflation bar for ~200 configurations on 72 months is ≈1.1 by §7.8's formula (computed: 0.326/month, 1.13 annualized); the 1.6 clears it because the factor is real, the 0.9 does not yet; pointer to Kaz's 3,000 (§7.8).
   - Dov's ticket in the ledger's columns (Hedge / Idio / Leaked) and the canon rule; pointers to §7-B.5 and §8.8 (0.28 at end-September).
2. **§7.5, Act 2.** `**The Pair Book panel, second week: the PM as the primary model.**`, ~470 words, placed after the "Three meta-labeling leaks" box and before "#### Quant-Shop Life: Model Review Tuesday" (a fourth leak the list lacks). Dov as primary (118 closed pairs, illustrative); meta-label on the pair corridor; research's residual: 68% vs 52% → sizes 0.30 vs 0.03 (computed with §7.5's map); Marcus's residual: 55% vs 53% → 0.08 vs 0.05; overall 54% → 0.06. Marcus: the sizing model levers the line he caps at a tenth of gross. Dov's second ticket line. Forward pointer: 6 Oct x-ray, bucket 0.11, eight of twelve pairs long the lower-rated name (Ch 8-D cold open).
3. **Figure 7.1** `assets/figures/ch07_pair_corridor.png` from new script `tools/figures/ch07_rv.py` (seeded simulation; research's residual touches the ceiling in week 8, label +1; whole-sheet residual ends in the dead zone, label 0; gray = the bucket factor, ≈0.39 of the move at the touch). Caption carries the fiction label. It is the chapter's first figure; if U4 adds figures earlier in the chapter, renumber.
4. **Finder table (§7.13):** triple-barrier row and meta-labeling row each gain a clause pointing to the scene.
5. **Shelf line:** Dynkin pages now "(pp. 611, 651, 794)".

## Retired
- The old §7.4 Pair Book panel text (≈300 words), rewritten into Act 1. Nothing else removed: no topic, equation, Source Extraction, Trend Watch, exercise, figure, Appendix F link or URL (URL list and protected-item counts diffed equal before/after). No code blocks added. Chapter last line unchanged. `tools/check_book.py --file` OK; pandoc MathML render of the scene clean. Chapter 33,447 → 35,046 words.

## State updated
- `state/rv_pair_book.md`: PB-19 row's "Stressed in" gains Ch 7 §7.4–7.5 (screened 2 Sep 2026); the Ch 7 chapter note is replaced by a full entry (legs, ratio 1.50 by MV DTS, costs, three labels, idio share ≈0.6, what leaked, Act 2 numbers).
- `state/cast_bible.md`: Ch 7 entry for Dov, Wen and Marcus extended (dates, Wen's 31 strikes and line, 118 closed pairs, Marcus's line, Dov's second ticket line).

## Open items
- None in book text. Ratings of the two captives are deliberately not stated (the text says only "the lower-rated of the two captives", as Ch 8-D does).

<!-- STATUS: COMPLETE -->
