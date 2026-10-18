# Ch 21 figure check (Edition 2)

Checked against tools/figures/style.py (house style), tools/figures/ch21.py, the chapter text and Listing 21.1 (Appendix F). All five PNGs were viewed after the final run; each is 90-122 KB (under the 500 KB budget). Chapter numbers were recomputed from the script's functions: buffers 1.065 / 4.164 / 7.768 (T+1 / T+7 / T+20, phi = 0.4), loan prices 101.36 / 100.45 / 100.12 with spread durations 2.72 / 0.899 / 0.246, note spreads 160.9 bp, residual 38.1 bp, 4.2% on 9% equity, -12 bp and -1.3% after a 50 bp repricing.

## Figure 21.1, ch21_settlement_clock.png (settlement clock)
- Correctness: PASS. Bonds T+3 -> T+2 (2017) -> T+1 (28 May 2024), loan par convention T+10 (Moyer 2004) -> T+7, T+5 paperwork deadline, medians T+12 (Jan-Aug 2016) -> T+9 (Sep 2016), about T+20 decade average all match section 21.2.1-21.2.2. Dead zone (T to T+7) and delayed-compensation window (after T+7) are placed as the derivation states.
- Honesty: PASS. Caption cites Moyer p.322, Markets Media (2 Nov 2016) and flags the LSTA 20-day average as approximate.
- Legibility: FIXED. The dashed vertical line at T+7 ran through the "T+1", "T+3", "T+7 par" and "T+10 par" labels. Removed it (the tint boundary already marks T+7) and shortened the T+1 label to "T+1 (28 May 2024)".
- Embedding: PASS. Placed after the forced-repo paragraph that points to it.

## Figure 21.2, ch21_clo_arbitrage.png (CLO stack and excess-spread waterfall)
- Correctness: PASS. Stack sums to 100% (62/11/8/5/5/9). Waterfall: 319 - 161 - 45 - 75 = 38 bp; the 50 bp repricing gives -12 bp; bars, connectors and the zero line are consistent; 38/9% = 4.2% and -12/9% = -1.3%, a 5.6-point fall (50/9).
- Honesty: PASS. Caption says "Illustrative", separates the sourced inputs (319 bp WAS, 130 bp AAA) from assumptions.
- Legibility/style: PASS. Two panels, one y-axis each, sequential blue for seniority, orange for equity, red only for the negative bar (with its text label); no slot 3-5 colors; text in ink; nothing clipped.
- Embedding: PASS.

## Figure 21.3, ch21_ccc_cliff_and_cure.png (CCC cliff and cure trade)
- Correctness: PASS. Left: haircut is zero until 7.5% and then rises monotonically with slope 1 - p* falling from 0.50 to about 0.34 (matches the annotation's "35-50 cents"). Right: the scripted functions are identical to Listing 21.1; the dots reproduce the chapter's +0.78 mm (richest) and -0.03 mm (cheapest); three loans sit in the excess set (4.8 mm of excess, the third in part); every performing-side point lies on or above the (21.6) lower bound and the in-excess points lie in [-c(1-p)dn, 0].
- Honesty: PASS. Caption says "Illustrative" and states the ladder used for the left panel.
- Legibility/style: PASS. No collisions; dollar signs render correctly; blue/orange roles consistent with the other figures.
- Embedding: PASS. Placed after the cure-trade discussion; the dollar signs in the caption are escaped.

## Figure 21.4, ch21_loan_short_call.png (loan as a floater short a call)
- Correctness: PASS. Corner at par (s = m) for the h > 0 lines; widening side identical for all h at 2.72 points per 100 bp; tightening slopes 2.72 / 0.90 / 0.25; prices at m - s = 50 bp match eq. (21.7) and the chapter's three values; lines are monotone decreasing in s.
- Honesty: PASS. Caption says "Illustrative", names the equations and parameters.
- Legibility: FIXED. The "100.45" value label was crossed by the dashed no-call line, and the three value labels sat tight against the lines. Moved the three prices into the legend entries (with the dots kept on the 50 bp guide) so no text sits on a line.
- Embedding: PASS.

## Figure 21.5, ch21_buffer_queue.png (cash buffer vs settlement lag)
- Correctness: PASS. Curves are strictly increasing in the lag and ordered phi = 0.7 > 0.4 > 0 for every lag above 1 (all coincide at T+1, same daily volatility); the phi = 0 curve is mu*l + z*sigma*sqrt(l); the phi = 0.4 curve gives 1.07 / 4.16 / 7.77 at T+1 / T+7 / T+20.
- Honesty: FIXED (caption). The caption said "at the loan lag it exceeds the 4.5% median", but at the T+7 convention the phi = 0.4 buffer is 4.16%, below 4.5%. Changed to "at the observed lag of about T+20 every curve exceeds the 4.5% median" (5.54 / 7.77 / 11.04 at T+20). The 4.5% median is cited to the Fed FEDS Note (19 Aug 2026), as in the chapter; the rest is labelled Illustrative.
- Legibility: FIXED. The "4.16%" label sat on the phi = 0 curve; moved it between the phi = 0 and phi = 0.4 curves. The threshold label was narrowed to three lines. Curves are direct-labelled (one hue, three shades), one y-axis.
- Embedding: PASS.

## Embedding summary
Five ch21_*.png figures, syntax `![Figure 21.n: ...](assets/figures/ch21_*.png)`, all files exist, numbered 21.1 to 21.5 in order of appearance, each directly after the paragraph that cites it. tools/check_book.py reports OK for the chapter.

## Fixes made
1. tools/figures/ch21.py: removed the T+7 dashed line and shortened the T+1 label (Fig 21.1); moved the three worked prices into the legend (Fig 21.4); repositioned the 4.16% label and narrowed the threshold label (Fig 21.5). All five figures re-run and re-viewed.
2. book_src/21_...md: Figure 21.5 caption corrected (T+20 instead of "the loan lag").
<!-- STATUS: COMPLETE -->
