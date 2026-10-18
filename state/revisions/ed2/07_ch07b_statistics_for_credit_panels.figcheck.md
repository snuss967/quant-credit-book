# Figure check: Chapter 7-B (ed2)

Checked against tools/figures/style.py. Every figure was re-derived from the script and viewed as a PNG (before and after fixes). All five are Illustrative (model-generated); no real-data claims, so no source gaps. Embeds: syntax `![Figure 7-B.N: ...](assets/figures/ch07b_*.png)`, all five files exist (1050 px wide, 85-112 KB), numbered 7-B.1 to 7-B.5 in document order, each directly after the paragraph that names it ("Figure 7-B.N plots/shows/draws...").

## Figure 7-B.1, ch07b_moulton_breadth: PASS (no change)
- Correct: sqrt(1+(m-1)rho) and m/(1+(m-1)rho) match eq. 7B.3 with rho_x = 1; Halvorsen (m = 11, rho = 0.6) gives x2.65 and 1.57 bonds; dashed ceilings at 1/rho; curves monotone and saturating.
- Honest: caption matches both panels and says Illustrative.
- Style: sequential blue for magnitude, direct labels, one y-axis per panel, ink text. No collisions.

## Figure 7-B.2, ch07b_newey_west_shortfall: FIXED
- Correct: weights x overlap triangle reproduce 8.03 at L = 11 and 10.01 at L = 23 against truth 12 (t overstated by 22%); curve rises monotonically toward 12.
- Fixes: left y-label said "Weight on the lag-k autocovariance" but the colored curves are each lag's contribution to the multiplier, so it now reads "Lag-k contribution to the multiplier"; panel title "What Newey-West counts of the overlap" was ungrammatical, now "How much overlap Newey-West counts"; the "true overlap correlation" note sat on the 1.0 gridline, so it was raised above it (ylim 1.16, ticks kept to 1.0). Caption rewritten in left-then-right order so the right panel (L = 11 and 23 against the truth) is described.

## Figure 7-B.3, ch07b_km_practice_cohort: FIXED
- Correct: S = 0.8, 0.6, 0.4 at months 14, 22, 27; Greenwood sum 0.30 (Var 0.048); log-log band 0.05 to 0.75; Nelson-Aalen 0.457; censoring ticks at months 9 and 30 sit on the curve at the right heights.
- Honesty fix: the 0.25 reference line is labelled "censored dropped" but the chapter's 3-in-4 comes from dropping only the two early leavers (Calloway, Halyard), since Brambleworth is alive at the window end. Line label now "early leavers dropped: 0.25"; caption now "0.25 (the two issuers that left early dropped)". Orange line label shortened to "counted as survivors: 0.50" so it no longer touches the step at month 27.
- Style fixes: the Nelson-Aalen diamond was violet (an off-order series slot used once); it is now INK_2, still direct-marked and in the legend. Censored legend entry now "left early, or window closed" so it fits Brambleworth. Event red and censored blue are paired with filled/hollow shape, so color is not the only cue.

## Figure 7-B.4, ch07b_mp_edge: FIXED
- Correct: edges (1 +/- sqrt q)^2 = 2.44 (q = 0.32) and 7.98 (q = 3.33); MP curve integrates to T (N/q) and matches the bar heights; noise bulk stays below the edge (largest bulk 2.28 daily, 7.28 monthly).
- Fix 1 (correctness): the script took eigenvalues of X'X/T on unit-variance data, not of a correlation matrix, although the axis and caption say "correlation matrix". eigvals_corr now demeans and standardizes the columns and drops the zero eigenvalues when T < N. Values moved slightly (daily 17.9 and 2.8; monthly market factor 19.5, was 20.0); conclusions and caption unchanged.
- Fix 2 (honesty): eigenvalues above the edge were drawn as stems 17 units tall on an axis labelled "Number of eigenvalues", which read as a count of 17. Each is now a dot at count 1 (one eigenvalue), and the note says "dots: one eigenvalue above the edge"; caption adds the same.

## Figure 7-B.5, ch07b_first_passage_bridge: PASS (no change)
- Correct: exact 2*Phi(-1.2) = 23.0%; grid-only 11.6% (annual), 17.7% (monthly), 21.6% (daily), rising with the square root of the step; bridge 22.9% to 23.1% on every grid (Monte Carlo noise about 0.1 point).
- Honest: "5.4 points at monthly" and "about a quarter" (5.4 / 23.0 = 23%) match the plot; caption says Illustrative with paths and model. One y-axis, direct end labels (bridge, grid only), exact line labelled; no collisions.

## Flags for the orchestrator (not fixed: prose outside the figure remit)
1. 7-B.4 worked example says "dropping them gives three in four, 75%". Dropping all three censored issuers would leave three of three; the 3-in-4 holds only if Brambleworth (censored by the window close, not an early exit) stays in. Suggest "dropping the two that left early gives three in four". The figure and caption now say this.
2. Still open from the figures log: 7-B.8 and exercise 5 quote 17.1% for the monthly grid (continuity-correction approximation) while the simulation, the acceptance test and Figure 7-B.5 give 17.6-17.7%.
3. Still open: the Bohn-Stein "about half of the time ... 20 bps vs 200 bps" claim in 7-B.6 does not follow from the stated one-factor parameters.
4. figures.md quotes the old Figure 7-B.4 numbers (17.9 / 20.0); current build prints 17.85 and 2.77 (daily) and 19.53 (monthly).
5. style.py sets axes.titleweight to "semibold", which DejaVu Sans lacks (build warning; titles render bold). Not touched because the file is shared by every chapter.
<!-- STATUS: COMPLETE -->
