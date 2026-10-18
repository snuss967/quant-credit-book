# Ch 7 App Z editor-note fixes (numbers editor)

Four NOTE (for the editor) paragraphs found in state/appZ/07_ch07_ml_on_small_sample_credit_data.md. All four deleted from the solutions file after ruling. Chapter edits are in book_src/07_ch07_ml_on_small_sample_credit_data.md.

## 1. Exercise 1 (a): "about 19" vs the "N_eff approx 20" the exercise asks the reader to show
- Note: the check's 11 x 1,197 / 693 gives every label the interior uniqueness; the exact sum is 19.98.
- Recomputation (python3, /tmp/n1.py; 11 bonds, T = 1,260, h = 63, 1,197 labels, issuer concurrency, exact sum of average uniqueness): N_eff = 19.984; 11 x 1,197 / 693 = 19.0; with 1,198 labels it is 20.000. Right: the interior approximation undershoots because edge labels share windows with fewer neighbours.
- Ruling: note right (fixed).
- Chapter (Exercises, item 1 check): "gives about 19. (b) They remain one group." -> "gives about 19 from the interior approximation, and 19.98, essentially 20, once the less crowded labels near the two ends of the sample are counted. (b) They remain one group."
- Solution (Z.07.1 Answer (a)): "Summed over all $11 \times 1{,}197 = 13{,}167$ labels, that gives $N_{\text{eff}} = 19.98 \approx T/h = 20$," -> "Summed over all $11 \times 1{,}197 = 13{,}167$ labels, the interior value alone gives $13{,}167/693 = 19.0$. The exact sum, which gives the less crowded labels near the two ends of the sample their higher uniqueness, is $N_{\text{eff}} = 19.98 \approx T/h = 20$," (the old wording credited the interior value with the exact sum). NOTE deleted.

## 2. Exercise 2 (c): embargo cost counted without the purge tail
- Note: the check counts the embargo alone (280 days, 89% of a 315-day block); under §7.7 / Listing 7.5 the embargo runs from the last test label's end, so the training data removed after a test block is about 63 + 280 = 343 days.
- Recomputation (python3, /tmp/n2.py; Listing 7.5 rule `(t0 <= T1 + embargo) & (t1 >= T0)` on 1,260 daily labels, four 315-day blocks, embargo 280): training labels removed after a test block = 342 (t1 = t0 + 62) or 343 (t1 = t0 + 63) = 1.09 blocks = 27% of the sample, so the next block is lost entirely (blocks 1 and 2 after tests 0 and 1; block 3 after test 2). Embargo alone: 280 = 88.9% of a block, 22.2% of the sample (check's numbers true but incomplete). Purge before the test block adds another 62-63 days on the front side.
- Ruling: note right (fixed, one clause).
- Chapter (Exercises, item 2 check): "removed after every test block. At $\tau = 10^{-3}$" -> "removed after every test block, and with the 63-day purge in front of it (§7.7 measures the embargo from the last test label's end), more than a whole block. At $\tau = 10^{-3}$"
- Solution (Z.07.2): already carried the 343-day / "more than a whole block" sentence; no text change. NOTE deleted.

## 3. Exercise 4 (c): MinTRL computed from a rounded gap
- Note: the check rounds 0.30 - SR* to 0.11 and gets 280 months, "roughly 23 years"; unrounded gives 292 months, about 24.4 years.
- Recomputation (python3, /tmp/n3.py; Listing 7.6 `expected_max_sr`, `min_trl`): SR*(N=400, V=1/240) = 0.19267; gap = 0.10733; shape term 1 + 0.15 + 0.09 = 1.24; T* = 1 + 1.24 x (1.645/0.10733)^2 = 292.2 months = 24.35 years. (With the rounded 0.11 the formula itself gives 278.3, not 280.) Against zero: 38.3 months (unchanged trap). TRACE: July 2002 to October 2026 = 291 months, so 292 is about its whole life; 292 - 240 = 52 months = 4.3 years beyond Kaz. (b)'s "0.11 ... Phi(1.5) approx 0.93" is rounding-level (exact z = 1.49, DSR 0.932) and left alone.
- Ruling: note right (fixed).
- Chapter (Exercises, item 4 check (c)): "(c) $T^\ast = 1 + 1.24 \times (1.645/0.11)^2 \approx 280$ months, roughly 23 years. That is about the entire life of TRACE (dissemination began in July 2002), and more than three years longer than Kaz's sample." -> "(c) With the unrounded $SR^\ast = 0.1927$ the gap is $0.30 - 0.1927 = 0.1073$, so $T^\ast = 1 + 1.24 \times (1.645/0.1073)^2 \approx 292$ months, roughly 24 years. That is about the entire life of TRACE (dissemination began in July 2002), and more than four years longer than Kaz's sample."
- Solution (Z.07.4 (c)): already 292 months, 24.4 years, four years short; no text change. NOTE deleted.

## 4. Exercise 4 (d) vs §7.8's worked example: which Sharpe was deflated?
- Note: (d) calls deflating an in-sample Sharpe a category error, but §7.8's example deflates "Kaz's winner" at SR-hat = 0.23 a month, which is neither the in-sample 2.9 (0.84 a month) nor an out-of-sample figure; the Exercise 4 intro also says §7.8 "deflated Kaz's in-sample winner".
- Recomputation (python3, /tmp/n3.py): 2.9 / sqrt(12) = 0.837 a month, not 0.23. SR* (N = 3,000) = 0.2295 a month = 0.795 annualized, so 0.23 is the noise bar itself and DSR = Phi(0) = 0.5 by construction (§7.8 example denominator sqrt(1 + 0.115 + 0.053) = 1.08, PSR(0) = Phi(3.29) = 0.9995, as printed). Kaz's actual out-of-sample 0.30 gives DSR 0.836 (Exercise 4a, §7.13). Feeding 0.84 a month would give Phi(6.5), the category error (d) warns about. So 0.23 is a stylized winner pinned at the bar, and the chapter never said so.
- Ruling: note right (fixed, one clause in §7.8, plus the matching words in the Exercise 4 intro, which otherwise would still say "in-sample winner").
- Chapter (§7.8, Full Derivation): "Run Kaz's winner through it: with $\widehat{SR} = 0.23$," -> "Run a stylized winner through it, one whose measured Sharpe sits exactly at the noise bar (not Kaz's in-sample 2.9, which is not fit to deflate; Exercise 4 returns to why): with $\widehat{SR} = 0.23$,"
- Chapter (Exercises, item 4 intro): "Section 7.8 deflated Kaz's in-sample winner. Now deflate" -> "Section 7.8 deflated a stylized winner whose Sharpe sat exactly at the noise bar. Now deflate"
- Solution (Z.07.4): did not quote either line; (d) already says the 2.9 is 0.84 a month and returns Phi(6.5). No text change. NOTE deleted.
- Left alone on purpose (outside the note): the "in words" paragraph of §7.8 ("Against a benchmark of zero, Kaz's winner looks overwhelming ... The answer is a coin flip") and the §7.13 table row "Kaz's 3,000 (§7.8: a coin flip)" speak of Kaz's winner generically at the noise bar; they now read consistently with the stylized-winner clause. Appendix F listing and tools/figures/ch07.py print none of the changed numbers (Listing 7.6 prints MinTRL(SR 0.3 vs 0.1) = 1 + 1.24 ... for its own demo, unchanged).

## Status
- 4 notes handled: 4 fixed, 0 ruled wrong, 0 softened. No figure script or Appendix F listing needed a change. book_src/99_appZ_solutions_hints_and_self_assessment.md is assembled from state/appZ and was not edited by hand; it needs the next reassembly to pick up the shortened Z.07.
<!-- STATUS: COMPLETE -->
