# Figure check: Chapter 2-B (ed2 U4, Edition 2 checker)

Checked against tools/figures/style.py (house style), tools/figures/ch02b.py (the drawing script) and the five embeds in book_src/02_ch02b_transaction_cost_analysis_for_credit.md. All five PNGs exist, are numbered 2-B.1 to 2-B.5 in order of appearance, and the script re-runs cleanly (all under 170 KB). Every number the chapter gives was recomputed from the chapter's own formulas.

Verdicts and fixes are appended per figure below as each is checked.

## Figure 2-B.1, ch02b_benchmark_ladder

Correctness: PASS. Costs recomputed from eta(p-b)/b x 1e4 for the 98.42 buy: +4.07 (arrival 98.38), +2.03 (RFQ-time mid 98.40), -1.02 (composite offer 98.43), -3.05 (cover 98.45), -5.08 (next print 98.47), shown as +4.1, +2.0, -1.0, -3.0, -5.1 as in the Math, Gently box. Cover is on the worse side of the winning buy price, as an order statistic must be. TRACE print at 9:07 + 22 min = 9:29. Shortfall table recomputed in dollars: executed 9,765 + 6,975 + 72,540 = 89,280; Wednesday net 89,280 - 60,750 + 24,300 = 52,830 and the unfilled lines net to -36,450; Friday net 89,280 + 44,550 + 68,850 = 202,680 = 11.26 bp of $180mm; unfilled 113,400 = 55.95% of it. Bars, diamonds and call-outs match the table.

Honesty: PASS with a caption fix. The image draws two levels the caption did not list (composite offer, next print) and a cost column, and the top panel's numbers live in the Math, Gently box of 2B.1.1, seventy lines above the figure, with nothing pointing back to it. The clock times and the one-hour / one-day mids are assumptions and were only stated on the image.

Legibility and style: PASS after fixes. One y-axis (the cost table shares the price axis and hides its own ticks); blue / orange roles as in the script header; no slot 3 to 5 colours; text in ink. Fixed: stamp tick labels were 7.2 pt and ROUTED / QUOTED nearly touched, so the ordinal spacing was widened and the labels raised to 7.8 pt; the axis-note raised to 7.8 pt; the Friday net call-out sat hard against the diamond and was moved out a few units.

Embedding: PASS. Syntax correct, file exists, placed after the shortfall table it illustrates (bottom panel). Caption now points the top panel to the 2B.1.1 box.
