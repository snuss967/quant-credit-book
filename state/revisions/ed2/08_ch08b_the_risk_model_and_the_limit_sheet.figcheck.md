# Figure check (Edition 2): Chapter 8-B, The Risk Model You Run Every Morning

Chapter: book_src/08_ch08b_the_risk_model_and_the_limit_sheet.md. Script: tools/figures/ch08b.py. Figures log was COMPLETE. The script was re-run from scratch (no randomness, no downloads) and all five PNGs were regenerated, viewed, and re-viewed after fixes. All five are under 175 KB.

Numbers recomputed independently of the script (scipy) and compared with the chapter:
- Kupiec LR_POF 5.497 (chapter 5.50), P(X >= 7) 1.37% (1.4%), binomial pmf 8.1/20.5/25.7/21.5/13.4/6.7/2.7/1.0% for 0..7.
- Christoffersen from n00 238, n01 4, n10 4, n11 3: pi01 1.65%, pi11 42.9%, ratio 25.9 (about 26), LR_ind 13.488 (13.49). The drawn calendar (exceptions on days 71, 152, 235-237, 243-244) reproduces exactly those four transition counts.
- Table 8-B.2: one-day VaR 2.39, ES 5.31; sqrt(10) times = 7.55 and 16.79; ten-day on the mixture 18.59 (table 18.60) and 21.70. Exercise 2 book: one-day ES 3.79, ten-day 10.83, shortcut 11.99. So the ES ratios plotted at ten days (1.29 and 0.90) and the VaR ratio (2.46) are right.
- Halvorsen: JTD 12 x (0.78 - 0.15) = 7.56; one-day default probability 0.0992%; ten-day 0.987%; mixture VaR 0.284, ES 1.042; folded sigma 0.266, folded VaR 0.620 (all as in the text).
- Stress library recomputed by hand for March 2020, 2022 and the hedge-basis case: matches the script output; bars sum to the printed totals.

## Figure 8-B.1, ch08b_factor_tree.png (8B.2): PASS, no changes
- Correctness: five factor branches plus residual and jump leaves match the equation under the figure; net DV01 (-6, +9, +13, -2) equals bond minus futures DV01 in the script; DTS cells sum as the script's E_RATING; thresholds match Table 8-B.4; Halvorsen 7.56 and Brambleworth 2.20 are the chapter's.
- Honesty: caption says "Illustrative book". Exposures not stated in the chapter (cells, bank holdco 4.15, liquidity 0.35, and so on) are the script's own and are labelled illustrative.
- Legibility: no collisions or clipping; text in ink; chips are status colours with text (HARD, SOFT).
- Embedding: directly after the paragraph naming the five branches; numbered 1. No in-text pointer sentence, which is acceptable.

## Figure 8-B.2, ch08b_mixture_traps.png (8B.6): FIXED
- Correctness: the exceedance curve has a 0.099% plateau, and the plateau ends at about 9.4 (12 x 0.78, recovery zero), so the right tail is bounded as it should be. The folded Gaussian has no plateau. Both reach the stated VaR and ES. The VaR ratio steps up near day 7, where the ten-day default probability crosses 1% (1 - exp(-0.0015 h) = 1% at h = 6.7). ES peaks there and then declines, as the mixture arithmetic requires.
- Problems fixed: (a) the dashed folded-Gaussian curve ran through the "mean loss $7.56mm" note, and the note's right edge touched the plateau's drop; the note now sits above the plateau, with its dot at x = 3.2. (b) The black curve had no direct label; the VaR/ES note now begins "mixture:".
- Caption fixed: it said "the mixture's ES and VaR" for the right panel, but VaR is drawn only for the Table 8-B.2 book. It now says ES (both books) and VaR (Table 8-B.2 book) as multiples of the shortcut, with the 1.29 and 0.90 ten-day ratios.
- Honesty: "Illustrative: computed from the 8B.5 Halvorsen inputs and the parameters of Table 8-B.2 and Exercise 2." Correct.
- Style: orange = jump layer, violet = the shortcut, ink = the mixture; one y-axis per panel; no slots 3-5 used. The "10 days" tag and the "0.90x" label sit close together but do not touch.
- Embedding: after the paragraph that points to it; the left panel illustrates the earlier Halvorsen paragraph, but the pointer covers both panels.

## Figure 8-B.3, ch08b_stress_library.png (8B.7): FIXED (label and caption)
- Correctness: scenario order and shocks follow Table 8-B.3. The hedge-basis case is the worst on the factor bar (14.4) and in total; SVB (4.5) and the 2026 CCC decompression (3.7) are the worst on the jump bar. Both claims in the caption hold. Bars are losses, positive, and sum to the totals shown.
- Fixed: the label "LDI BWIC week (Oct 2022)" is now "(Sep-Oct 2022)", since the table window is 26 Sep-7 Oct 2022.
- Caption fixed: "P&L" is now "loss", to match the axis ("Loss on Tuesday's book").
- Honesty: "Illustrative book". Legibility: no collisions; direct value labels; legend is above the plot. Embedding: after "each scenario runs on today's book and reports two columns".

## Figure 8-B.4, ch08b_backtest_exceptions.png (8B.8): FIXED (minor)
- Correctness: the binomial is Binomial(250, 0.01) with the grey/red split at 7; 7 or more is 1.4%; LR 5.50 > 3.84; pi01 = 4/242 = 1.7%, pi11 = 3/7 = 43%; LR_ind 13.49 > 6.63. All verified above. The calendar strip reproduces the chapter's clusters (three in a row, two in a row, two isolated).
- Fixed: the leader line from "the model claims 1%" ran into the "1.7%" label; the leader now sits at x = -0.24.
- Honesty: caption says the calendar positions are drawn for illustration. Correct. Timing is consistent with Figure 8-B.5: the "3" exceptions on Tuesday's report are the two isolated days plus the Monday gap day, which is the first of the three in a row.
- Embedding: after the sentence "Figure 8-B.4 shows the count and the clusters."

## Figure 8-B.5, ch08b_limit_sheet.png (8B.9): FIXED
- Correctness: every value, soft and hard threshold matches Table 8-B.4 (the CS01 3-7y bucket 90/120, key-rate 15/25, JTD B 7.0/9.0, ES 1-day 2.5/3.0, 10-day 9/11, and so on). Status colours are right: DTS 1.62 over 1.5 is hard; Halvorsen 7.56 over 7.0 and ES 2.7 over 2.5 are soft; the stress line is the worst total of Figure 8-B.3 (14.4, under the soft 15). Migration: 1.08 - 0.60 = 0.22 -> 0.70 less 0.22 = 0.48 in both cells, so what left B Industrials arrived in CCC Industrials.
- Problems fixed: (a) the note "moved, nothing traded," ran past the right edge of the image and lost its comma; it is now four lines inside the axes with a white backing so the gridlines do not strike through it. (b) The Monday bars were violet, but violet is reserved in this chapter for the shortcut or folded-in alternative; Monday is now Gaussian-layer blue (Friday stays neutral grey).
- Caption fixed: it said "the change in the CCC cells", but the figure shows B Industrials and CCC Industrials; it also did not say which lines were drawn or which Monday. It now says ten lines of Table 8-B.4 (one bucket of each ladder), names the three cold-open breaches, and labels the right panel as the committee Monday's forty-bond migration.
- Honesty: "Illustrative". Embedding: after the committee's "why is the ten-day ES 11% higher" paragraph.

## Embedding summary
Five embeds, numbered 8-B.1 to 8-B.5 in order of appearance, relative paths `assets/figures/ch08b_*.png`, all files present. Only 8-B.2 and 8-B.4 have an in-text pointer.

## Edits made
- tools/figures/ch08b.py: mixture label and plateau note; LDI scenario label; backtest leader; limit-sheet note, Monday colour; docstring now states that violet is used for nothing else.
- Chapter: captions of Figures 8-B.2, 8-B.3 and 8-B.5 only. No body text changed.

## Remaining notes for the orchestrator (not fixed, outside figure remit)
1. The stress limit (soft 15) works only because the illustrative book is index-hedged (net spread exposure about 0.4 against gross 5.2 per 10% widening); if the chapter ever states gross exposure, restate the stress line (already flagged in the figures log).
2. The "bank holdco 4.15" in the factor tree appears nowhere in the chapter text; it exists to carry the SVB overlay of Table 8-B.3.
3. The cold open and 8B.4 differ on the ES line (soft, then hard after re-bucketing); Figure 8-B.5 shows the soft morning number, as its caption says.
<!-- STATUS: COMPLETE -->
