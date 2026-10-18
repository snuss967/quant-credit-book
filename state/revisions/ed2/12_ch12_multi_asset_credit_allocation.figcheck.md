# Figure check: Chapter 12 (ed2 U4, Edition 2 checker)

Script: tools/figures/ch12.py. Style reference: tools/figures/style.py docstring. All five PNGs were re-generated (the script's asserts pass), opened and viewed; two were also viewed enlarged.

## Checks run beyond reading the code

- Live FRED cross-check: all 3,444 cached ICE BofA values used by Figures 12.4 and 12.5 (OAS series and the total-return values for the dates used) were compared with a fresh download of the same eight FRED series. Zero mismatches (April 7, 2025 HY OAS 4.61; January 22 2.59; March 31 3.55; April 30 3.94; October 15, 2026 CCC 12.78, BB 1.97, HY 3.23).
- Figure 12.3 optimizer: the covariance is positive definite (minimum eigenvalue 1.1e-4). For all 400 draws, both the unconstrained and the tiered solution were compared with SLSQP restarts from other starting points: maximum utility gap 4.4e-13 and 2.8e-13, no infeasible tiered solution (15% illiquid cap, 35% liquid floor, 32-day budget, Nuveen bounds all hold). The inputs in the script are identical to Listings 12.1 and 12.3 and gamma = 8 as in Listing 12.5.
- Embedding: five `![Figure 12.N: ...](assets/figures/ch12_*.png)` lines, numbered 12.1 to 12.5 in order of appearance, each file exists (1050 x 480 or 1050 x 540, 150 dpi, 47 to 94 KB), blank line before and after each, each one preceded by a pointer sentence in the paragraph it illustrates (12.1 "Figure 12.1 draws the first point", 12.2, 12.3, 12.4, 12.5).

## Figure 12.1, ch12_same_bet_ownership.png (§12.1)

Verdict: pass, no change. Correctness: the five nodes are exactly the chapter's five (HY bond, term loan, CLO tranche that owns the term loan, direct loan, BDC that owns the direct loan), the post-default values 39%, 52%, 33% and the 5% of NAV a quarter gate match the §12.1 table and the Cai and Haque citation. Honesty: caption cites FEDS Notes for the three values and says the structure is Illustrative. Style: no title, text in ink, blue for claims and orange for wrappers as roles, no collisions or clipping, smallest text 7.6 pt. Embedding: fine.

## Figure 12.2, ch12_return_identity_waterfall.png (§12.2)

Verdict: pass, one label fix. Correctness: 6.97 - 2.55 - 0.37 - 0.49 = 3.56, the bar bottoms and connectors are exact (asserted), the dashed line at 3.68% is the mean of return minus Sharpe times volatility over Nuveen's six Figure 6 rows (3.652 to 3.704, mean 3.683, asserted). Honesty: the caption states that the 2.55/0.49 assignment and the cash rate are inferences of §12.2.
Fix made: the in-image label read "Implied cash rate (Nuveen Fig. 6)", which could be read as Nuveen's own number. It now reads "Cash rate implied by Nuveen Fig. 6: about 3.68%".

## Figure 12.3, ch12_constraints_decide.png (§12.6)

Verdict: pass, one caption fix. Correctness: see the optimizer check above; the reported moves (30.1 and 3.5 points of NAV, from the median weights) match the caption, and the shaded allowed range equals the bounds. Honesty: caption says Illustrative, 400 draws, risk aversion 8, 25 bp. Style: two panels, one x-axis each, blue then orange in order, no slots 3 to 5, legend in the right panel explains the marks used in both.
Fix made: the caption did not say what the circles are; it now ends "and circles the median".

## Figure 12.4, ch12_april_2025_daily_vs_month_end.png (§12.9 Case Study A)

Verdict: pass after a colour and caption fix. Correctness: peak 461 bp is on April 7 (asserted), January 22 is 259 bp, month-end prints 355 (March 31) and 394 (April 30, 23 days after the peak), drawdowns BB 2.83%, HY 3.83%, B 4.21%, CCC 7.80% (asserted, and all troughs fall on April 7). Honesty: all five FRED IDs are cited with the pull date.
Fixes made: (1) colour roles. The left panel drew the HY index in blue and the month-end sample in orange, while the right panel of the same figure (and Figure 12.5) uses blue for BB, orange for B and grey for the HY index. The left panel now draws the daily HY line in the HY grey and the month-end sample in ink, so blue and orange keep one meaning. (2) Caption: "the highest month-end print" was ambiguous over a three-year window (it is the highest of the half-year shown), now "of the half-year"; "from each index's peak to its April 7 trough" now says "from each index's high since February 1 to its April 7 low", which is what the script computes (peak dates are February 27, February 28 and March 24).

## Figure 12.5, ch12_ccc_bb_split.png (§12.9 Case Study C)

Verdict: pass after one legibility fix. Correctness: end values CCC 1,278, B 326, HY 323, BB 197 bp on October 15, 2026; year-to-date total returns from December 31, 2025: BB +0.33, HY +0.15, B +1.20, CCC -5.21 (all asserted); the April 7, 2025 event line is the HY OAS peak from Figure 12.4. Honesty: eight FRED IDs cited, pull date given, return window stated. Style: slot 3 (CCC, aqua) is direct-labelled in the left panel and by category name in the right; one y-axis per panel; the label inside the CCC bar is ink.
Fix made: B and HY end 3 bp apart and the grey HY dot hid the orange B dot. A larger orange dot now sits under the grey one, so both colours show at the line end.

## Notes for the editor (unchanged from the figures log, still open)

- ICE licensing: FRED marks ICE BofA series as internal use only. Figures 12.4 and 12.5 plot them and tools/figures/data/ch12_ice_fred.csv caches the plotted slice. Decide before publication: keep with citation, ask ICE, or drop the cache and the two figures.
- FRED serves only about three years of ICE history, so a --refresh after 2027 will lose the October 2023 start of Figure 12.5; the cache keeps the figures reproducible.
- The five embeds were already in the committed chapter; this pass changed two captions (12.3, 12.4) and tools/figures/ch12.py, and regenerated the PNGs.
<!-- STATUS: COMPLETE -->
