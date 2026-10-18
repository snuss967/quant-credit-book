# Figure check: Chapter 17 (ed2)

Checked: five embedded figures, tools/figures/ch17.py, the figures log, the dossier trend_private_credit_marks_and_redemptions_2025_2026.md, the chapter paragraphs around each embed. Every PNG was viewed before and after fixes. All are under 125 KB.

## Figure 17.1, ch17_z1_holders.png: PASS
- Correctness: values match the dossier's Table F4.4.s line. Component sums are 1,042.7 / 1,253.6 / 1,493.6 against published totals 1,042.6 / 1,253.6 / 1,493.5 (rounding of components; the legend uses the published totals). Growth multiples recomputed: 1.2x, 1.9x, 1.2x, 2.2x, 1.7x.
- Honesty: caption cites Brinkman et al. FEDS Note and Table F4.4.s and says the borrower-side split is estimated. Fix: "sell to retail investors" softened to "reach retail investors" (the BDC bucket includes private and listed BDCs).
- Style: one hue light to dark for years, direct label on the 2025 bar only, no title, no collisions.
- Embedding: after the market-sizing paragraph, with a pointer sentence; numbered 17.1.

## Figure 17.2, ch17_smoothing_staircase.png: PASS
- Correctness: smooth() is the GLM filter with theta = (0.5, 0.3, 0.2), sum 1. Right panel is cumsum(theta) x 4 = 2.0 / 3.2 / 4.0 with 2.0 and 0.8 still to come; monotone; capped at the 4.0 true loss. Left: the mark's trough is later and shallower (103.3 at quarter 13 against 99.3 at quarter 12) and it converges to the true path by quarter 15. Note (no fix): the mark ends slightly above the true line, because smoothing arithmetic returns lowers volatility drag; this is the model, not an error.
- Honesty: caption says Illustrative and states the model, seed and shocks.
- Style: legend order now follows colour order (Reported mark blue first, True value orange second; was reversed). One y-axis per panel; text in ink.
- Embedding: after the "not exotic numbers" paragraph, which points to it.

## Figure 17.3, ch17_implied_markdown.png: FIXED, PASS
- Correctness: m = (d - phi)/(1 + l) floored at 0, kink at d = 5%; slopes 1/(1+l) flatten as leverage rises; points recomputed: OBDC 4.11% (14%, 1.19x), Octus 7.14% (20%) and 21.43% (50%) at 1.1x. All match the chapter text.
- Legibility fix: the "1 for 1" label collided with the dashed 45-degree line (the line ran through "for" and "mean"). Moved the label right of where the line exits the top of the plot and raised ylim to 36.5. Re-viewed: clear.
- Honesty fix: caption now says the Octus points are plotted at an assumed 1.1x leverage (the chapter calls it illustrative).
- Style: leverage in one blue hue by magnitude, direct end labels, orange for market observations. Embedding: after the Numbers paragraph, before Boundary conditions.

## Figure 17.4, ch17_medallia_marks.png: FIXED, PASS
- Correctness: all 42 values match the dossier ledger. Ranges recomputed 12.0 / 5.3 / 13.9 / 6.2 / 10.8 / 11.1, shown as 12, 5, 14, 6, 11, 11. Dates are placed at true quarter-ends on a real time axis (March 2025 is not in the ledger).
- Honesty fixes: caption said the two June 2026 groups were "ten points apart"; group means are 49.6 and 40.3, so now "about nine points apart". "At every date" became "at every date shown". The awkward "from 87 to 99 in December 2024 to 39 to 50" now reads "from between 87 and 99 ... to between 39 and 50". The Monroe par caveat is kept and matches the dossier CHECK item.
- Legibility fix: the "range N" tick text was undefined in the image; added an x-axis label "Quarter end (range = highest minus lowest mark, in points)". End labels do not clip.
- Style: two series colours only (blue upper camp, orange lower camp), direct labels. Embedding: after the Octus cross-holder paragraph that introduces it.

## Figure 17.5, ch17_redemption_queue.png: FIXED, PASS
- Correctness: left-panel requests and Q2 fill rates match the dossier; fill = 5 / requests checks for all seven funds (13.1, 26.6, 29.8, 34.7, 37.6, 46.0, 50.0). Right panel reproduces the chapter's queue_path (companion Listing 17.4): paid is always 5.0% of current shares, fill 50 / 34 / 26 / 21 / 18 / 16 / 14 / 13%, demand grows monotonically. Requests are 1.8 to 8.1 times the cap, so the title "2 to 8 times" holds.
- Legibility fix: BCRED's Q2 and Q3 dots (both about 10%) coincided, so Q2 was invisible. Markers are now nested (Q1 largest, Q3 smallest, all at least 5.5 pt) and the legend matches.
- Honesty fix: caption now says BCRED's Q1 request is not shown (the dossier holds only a secondary 7.9% marked CHECK), that its Q2 and Q3 were both about 10%, and keeps Q3 preliminary and "approximately half" (its Q2 fill).
- Style: quarters in one blue hue, no slot 3 to 5 colours, text in ink. Embedding: after "The model mapping" in the case study, with a pointer sentence.

## Numbering and syntax
Five embeds in order 17.1 to 17.5 (lines 35, 151, 287, 314, 498); syntax and relative paths match other chapters; all five files exist; section references (§17.2.2, §17.3.2, §17.6.2) match the headings.

## Files changed
- /home/user/quant-credit-book/tools/figures/ch17.py (legend order, 1-for-1 label, ylim, x-label, nested markers)
- /home/user/quant-credit-book/assets/figures/ch17_*.png (all five regenerated)
- /home/user/quant-credit-book/book_src/17_ch17_private_credit_public_private_convergence.md (four caption edits only)
<!-- STATUS: COMPLETE -->
