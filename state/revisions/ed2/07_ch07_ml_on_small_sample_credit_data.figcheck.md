# Figure check: Chapter 7 (ed2, figure checker)

Scope: the six ch07_*.png embedded in book_src/07_ch07_ml_on_small_sample_credit_data.md (ch07b_* belong to Chapter 7B and were not checked). Scripts: tools/figures/ch07.py (Figures 7.1, 7.3 to 7.6) and tools/figures/ch07_rv.py (Figure 7.2). House style read from the docstring of tools/figures/style.py. Every PNG was viewed before and after fixes; the regions at risk (corridor right edge, purged-folds right panel) were also viewed upscaled.

Embedding (all six): syntax `![Figure 7.n: ...](assets/figures/ch07_*.png)` correct; all files exist; numbered 7.1 to 7.6 in order of appearance (lines 272, 359, 503, 573, 607, 691); each sits directly after the paragraph that says "Figure 7.n shows/plots/draws" with a blank line either side; no other chapter cites a Figure 7.n. PNGs are 1050 px wide, 82 to 138 KB.

## Figure 7.1, ch07_ffd_weights (section 7.3): PASS, no change
- Correctness: recomputed independently. Recursion w_k = -w_{k-1}(d-k+1)/k gives w_1 = -d; |w_k| < 1e-4 first at lag 282 for d = 0.4 (497 for d = 0.2, 140 for d = 0.6, matching the plot); partial sum equals (-1)^K C(d-1,K) = 0.0703 at K = 282 (the "7%"); d = 0.5 keeps 27.3% after 4 lags and 4.0% after 200 (the Math, Gently box). d = 1 dot at (1, 1) and a flat zero on the right panel are right.
- Honesty: caption says Illustrative, exact recursion of 7.3; matches the image (left, right, hollow dot, lag 282, 7%).
- Style: log-log axes labeled with units; slot 3 (aqua) used and direct-labeled; one y-axis per panel; text ink.

## Figure 7.2, ch07_pair_corridor (section 7.4): PASS after one label fix
- Correctness: barrier 0.081 x 0.057 x sqrt(3) = 0.80% of the long, $320k on $40mm; dead zone +/-0.25%; the sheet path stays inside the corridor and ends at +0.11 (label 0); research path touches on day 36 (the eighth week) at 0.83 (label +1); the dashed difference is exactly research minus sheet and is 0.32 of 0.83 at the touch (about four-tenths, as the caption says). Re-running reproduced the same seed and path.
- Fix: the wall sits at day 63 = 12.6 weeks on the weeks axis but was labeled "wall, 13 weeks", so it looked mislabeled. Label now reads "wall: 63 trading days (13 weeks)" (ch07_rv.py, re-run, re-viewed). Caption already says Illustrative and fictional; unchanged.
- Legibility: leader lines cross the curves but no text collides.

## Figure 7.3, ch07_hat_count (section 7.6): PASS, no change
- Correctness: 212,000 / 3 = 70,667 ("about 70,700"); / 3 = 23,556 ("about 24,000"); 23,556 / 79 = 298 ("about 300"). Bars start at 1 on a labeled log axis with the values printed, so the funnel reads honestly. Ties to 7.6 (79 windows, one-ninth ratio) and to the Debrief's 24,000.
- Honesty: caption says Illustrative, states the two divisions and the 79.
- Style: orange = the naive row count, blue = the corrected counts (chapter roles); no slots 3 to 5; labels clear. Open flag 1 below.

## Figure 7.4, ch07_purged_folds (section 7.7): PASS after three legibility fixes
- Correctness: matches the chapter's scheme. Test cell = one group x one block; same row and column set aside; purge strips on both sides of the test column, embargo only after it. Right panel recomputed from the rules in the text (purge t0 <= T1 and t1 >= T0, embargo t0 in (T1, T1 + eta]): 6 set aside, 4 purged (2 each side), 12 embargoed over 56 weeks (280 days / 5), 10 training. The grid's embargo strip (0.30 block) is close to scale, the purge strip (0.10 vs 0.0625) is wider, so "drawn wider than to scale" holds.
- Fixes (ch07.py): (1) the white box behind the embargo label cut a notch out of the shaded test-block band; the band and the T0/T1/T1+eta guide lines now stop at the embargo arrow and the label sits below, no box; (2) set-aside bars (fill #e6e5e1) were nearly invisible on the pink band, now outlined in the neutral gray, in the left grid and the legend too; (3) none other.
- Honesty: Illustrative schematic, said in the caption.

## Figure 7.5, ch07_dsr_noise_max (section 7.8): PASS after one clipping fix and one caption fix
- Correctness: SR* = sqrt(V)[(1-g)Phi^-1(1-1/N) + g Phi^-1(1-1/(Ne))], V = 1/T, T = 240. Values 0.193 a month (0.67 annualized) at N = 400 and 0.230 (0.795, shown 0.80) at N = 3,000 match the Full Derivation; Kaz's 0.30 x sqrt(12) = 1.04. Curve is increasing and concave in log N; simulated means of the maximum agree with the formula to within 0.01 at every N tested (the N = 2 dot is 0.119 vs 0.116).
- Fixes: the N = 2 simulation dot was half cut off by the left spine (x-limit now 1.5, Kaz's marker and label moved to 1.7). Caption: the 0.30 a month and the "400 effectively distinct trials" first appear in section 7.13 (Debrief and Exercise 4), after this figure, so the caption now says "(the clustering of Exercise 4)" and "(1.04 annualized, the rerun reported in §7.13)". The 0.30 vs 0.23 gap is consistent with the Debrief's DSR 0.84 (recomputed: about 0.83).
- Honesty: Illustrative, formula and simulation both named.

## Figure 7.6, ch07_reversal_gap (section 7.9): PASS after substantive fixes (the only real-data figure)
- Traced to the paper itself (arXiv:2604.07880, text extracted from the PDF), not just the dossier. Table 1 Panel A, str row, value-weighted: premium -0.99 (t -4.46), signal gap -0.09 (t -0.51), return gap -0.17 (t -0.98). Fig. 3 text: $1 grows to $12 by end of 2024 unadjusted, to $1.1 (adjusted signal) and $1.4 (adjusted return); the series is sign-corrected.
- Errors found and fixed: (1) the figures log said the paper reports no t for the return-gap column; it does (-0.98), now printed on the bar; (2) the sample for Table 1 and Fig. 3 is 2002-09 to 2024-12 (T = 268), not August 2002 (that is the full 269-month panel), so the axis label and caption now say September 2002; (3) the $1.10 and $1.40 are two specific values (signal gap, return gap), not a range, and the right panel was one floating bar; it is now three bars, same colors and order as the left panel; (4) the caption attributed the dollars to Table 1; it now cites Table 1 for premia and Fig. 3 for dollars.
- Chapter prose (line 689, "between $1.10 and $1.40, depending on the adjustment") remains true and was left alone; the dossier (papers_factor_replication_crisis_and_bond_data.md section 3.2) lacks the return-gap t and the sample start, worth patching there.
- Style: orange textbook, blue corrected; start-$1 line labeled; no slots 3 to 5; text ink.

## Flags for the orchestrator (outside the figure remit, not changed)
1. Carried from the figures log: the chapter never states the 3 bonds x 3 monthly dates derivation of 212,000 / 9 = 24,000 (Figure 7.3's caption does).
2. Carried: Theo's "four-trial benchmark, SR* about 0.02" (T = 96) does not follow from the formula with V = 1/T (about 0.107 a month, recomputed).
3. New: Kaz's cold-open in-sample Sharpe of 2.9 (about 0.84 a month if annualized) does not match the 0.23 a month "winner" deflated in 7.8's Full Derivation; Exercise 4(d) treats 2.9 as the in-sample number. Figure 7.5 avoids the conflict by drawing only the noise bar and the 0.30 rerun.
<!-- STATUS: COMPLETE -->
