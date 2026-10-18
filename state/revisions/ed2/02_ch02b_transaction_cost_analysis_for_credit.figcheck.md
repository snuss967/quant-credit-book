# Figure check: Chapter 2-B (ed2 U4, Edition 2 checker)

Checked against tools/figures/style.py (house style), tools/figures/ch02b.py (the drawing script) and the five embeds in book_src/02_ch02b_transaction_cost_analysis_for_credit.md. All five PNGs exist, are numbered 2-B.1 to 2-B.5 in order of appearance, and the script re-runs cleanly (all under 170 KB). Every number the chapter gives was recomputed from the chapter's own formulas.

Verdicts and fixes are appended per figure below as each is checked.

## Figure 2-B.1, ch02b_benchmark_ladder

Correctness: PASS. Costs recomputed from eta(p-b)/b x 1e4 for the 98.42 buy: +4.07 (arrival 98.38), +2.03 (RFQ-time mid 98.40), -1.02 (composite offer 98.43), -3.05 (cover 98.45), -5.08 (next print 98.47), shown as +4.1, +2.0, -1.0, -3.0, -5.1 as in the Math, Gently box. Cover is on the worse side of the winning buy price, as an order statistic must be. TRACE print at 9:07 + 22 min = 9:29. Shortfall table recomputed in dollars: executed 9,765 + 6,975 + 72,540 = 89,280; Wednesday net 89,280 - 60,750 + 24,300 = 52,830 and the unfilled lines net to -36,450; Friday net 89,280 + 44,550 + 68,850 = 202,680 = 11.26 bp of $180mm; unfilled 113,400 = 55.95% of it. Bars, diamonds and call-outs match the table.

Honesty: PASS with a caption fix. The image draws two levels the caption did not list (composite offer, next print) and a cost column, and the top panel's numbers live in the Math, Gently box of 2B.1.1, seventy lines above the figure, with nothing pointing back to it. The clock times and the one-hour / one-day mids are assumptions and were only stated on the image.

Legibility and style: PASS after fixes. One y-axis (the cost table shares the price axis and hides its own ticks); blue / orange roles as in the script header; no slot 3 to 5 colours; text in ink. Fixed: stamp tick labels were 7.2 pt and ROUTED / QUOTED nearly touched, so the ordinal spacing was widened and the labels raised to 7.8 pt; the axis-note raised to 7.8 pt; the Friday net call-out sat hard against the diamond and was moved out a few units.

Embedding: PASS. Syntax correct, file exists, placed after the shortfall table it illustrates (bottom panel). Caption now points the top panel to the 2B.1.1 box.

## Figure 2-B.2, ch02b_dealer_scorecard_heatmap

Correctness: PASS. Cells the chapter fixes all hold: K's 11% response rate is the panel minimum; C's 41% hit rate is the maximum; C's every-quote markout of -0.2 is exactly the median of the eleven (sorted: -3.6, -1.6, -1.1, -0.7, -0.4, -0.2, 0.2, ...), "fell to the middle of the table"; F's -3.6 is the worst, matching "worst at the table once every quote was counted"; done-away shares sum to 100%. Colour direction is right in every column (higher response / hit / markout is better; longer cover and larger done-away share worse), z-scores per column, clipped at +/-2 s.d., diverging blue-grey-red, text switches to white on dark cells. The 9 April column shows exactly two of eleven answering, K and E, F silent, matching the paragraph after the figure and the F phone call.

Honesty: PASS. Caption says Illustrative and fictional composites; the winners-only -4.2 bp for C is in the call-out, the table cells carry the every-quote markout, and the footnote says so. Fixed: the footnote now says which direction is shaded worse for cover distance and done-away share (the chapter does not state it) and that every cell the chapter's text does not fix is assumed.

Legibility and style: PASS after fixes. No in-image title, one panel, no series colours standing for series, text in ink. Footnote raised from 7.4 to 7.8 pt and extended to three lines (axes extended so nothing is clipped); right margin widened so the F call-out is no longer flush with the edge.

Embedding: PASS. After the Dealer K / F paragraph it illustrates; number in order.

Open for the text editor (not changed, outside figure scope): the paragraph just above the figure says the two dealers still answering at 10:40 were K and "the other, Dealer F ... answered nothing that morning", which contradicts itself and the later paragraph. The figure follows the later paragraph (F silent) and shows Dealer E as the second dealer; "The other, Dealer F," should read "The other was Dealer E. Dealer F,".

## Figure 2-B.3, ch02b_cost_curves_by_regime

Correctness: PASS after fixes. Re-fitted s + k sqrt(q) on the table's means: calm uses all four buckets, April 2025 uses the first three; both curves rise monotonically in clip size, as the square-root law requires; the April 2025 fit ends near 47 bp and the calm fit near 19 bp at $30mm. The prior is 3 x 14 = 42, drawn with a hollow marker and an arrow from the greyed raw point (-3, n=4); the dashed 3x-calm curve passes through it (41.1 on the fit against 42 on the bucket mean, under one marker radius). Counts match the table (3,812 / 2,407 / 311 / 38 and 402 / 188 / 19 / 4). The y-axis is half-spread plus impact against arrival, as the table states. The chapter and the script disagreed on one thing, fixed below.

Honesty: FAIL as drawn, fixed. The dashed curve was labelled "March 2020 envelope (3x calm spread, half the responses)" in the image and the caption. Neither number is March 2020's. In the chapter's cited source (MarketAxess, AxessPoint, 14 July 2025, quoted in Chapter 2) the widening of up to 231% and the fall in prices per RFQ from 13.2 to 6.6 are April 2025; March 2020 gets only a peak level of 44.62 bp. 2B.5's own text calls it the April 2025 envelope. The image label and the caption now say April 2025, and the caption cites the source, notes that 3x is the book's rounding of 231%, and says what is ours (fits, mid-sizes). Second fix: the script commented that the April 2025 fit uses "the three buckets above the minimum count", but the stress $5-10mm bucket has n=19, below the floor of 30 that 2B.10 states ("a stated prior below 30"). It stays on the plot because the chapter table reports 26 for it as a mean, but its label now reads "n=19 (<30)" and the caption flags it.

Legibility and style: PASS. Only series slots 1 and 2 (blue, orange), direct end labels, one y-axis, bucket bands recessive, no collision between the arrow and the n=19 label (8 px), text in ink or muted ink.

Embedding: PASS. After the cost-curve table it illustrates; numbered in order.

Open for the text editor (not changed): 2B.5 says "a bucket below a minimum count reports a prior" and "the two lowest buckets are estimates", yet its table reports a mean (26) for a stress bucket of 19 and calls neither that bucket an estimate nor a prior. Either the table should show a prior there or the floor should be lower than 30. The bucket mid-sizes (0.5, 2.2, 7.1, 15 $mm) are assumed; the 15 for the open-ended top bucket is a plain assumption, stated on the x-axis.

## Figure 2-B.4, ch02b_two_leg_shortfall

Correctness: PASS. April opening: Kestrel 120 (0.20 point on $60mm), Halvorsen 140 (0.36 point on $39mm = 140.4), legging net of the bridge 21, bridge half-spreads 16; running total 297; the execution report's 260 = 120 + 140; gap 37. The 2:40 trim: bond leg 14.0 (0.35 point on $4mm), CDX leg 1.94 (half of 1/32 point on $12.4mm), legging 4.43 (17,700 DTS x 0.25%), total 20.36 shown as 20.4, report 14.0, gap 6.4. Bars are drawn from a running base, connectors sit at the running level, the total is computed from the bars and not typed in, so tranches sum to the total by construction. The 13 October date is a Tuesday, as 2:40 trim of "Tuesday 13 October 2026".

Honesty: PASS. Caption matches the image and says all numbers illustrative, with the fictional composites named. Blue marks what the execution report shows and orange what it does not, as the legend says.

Legibility and style: PASS after fixes. Two panels because the two waterfalls differ in scale (no twin axes). Tick labels were 7.1 pt and are now 7.7 pt, with room to spare. The displayed parts of the trim (14.0 + 1.9 + 4.4) add to 20.3 against a total shown as 20.4, so a muted note on that panel gives the unrounded sum (14.00 + 1.94 + 4.43 = 20.36).

Embedding: PASS. After the PB-01 box, which covers the trim and follows the April paragraph; numbered in order.

## Figure 2-B.5, ch02b_roundtrip_conviction

Correctness: PASS. Cost multiple = 2 x 297 / (1,200 x w / 52): 4.29 at six weeks, 0.66 at 39 weeks, break-even 25.7 weeks (26); with the report's 2 x 260 the break-even is 22.5 (23). Curves fall monotonically in hold, the 1x line is where the thesis just pays for the trades, and a round trip is 49.5% of a year's thesis, matching "half a year of thesis". Quarter = 13 weeks, nine months = 39 weeks.

Honesty: PASS. Caption gives 4.3x, 0.66x, "a few weeks too short" (26 against 23) and "borrow is not included", and says Illustrative: the chapter's numbers; the closing-equals-opening assumption and the $1.2mm thesis are stated in the image note.

Legibility and style: PASS. One log y-axis with multiplier ticks, only ink and neutral grey (the full measured total in ink, the report's own number dashed grey), direct end labels, no text-on-line collision, note clear of both curves.

Embedding: PASS. Placed after the "Wen's arithmetic" paragraph, which points to it by number; numbered after 2-B.4.

## Summary of edits

- tools/figures/ch02b.py: Figure 2-B.1 stamp spacing and tick font; Figure 2-B.2 footnote text, size, axis limits; Figure 2-B.3 envelope relabelled to April 2025, n=19 flag, corrected fit comment; Figure 2-B.4 tick font and rounding note. All five PNGs regenerated and re-viewed; all under 190 KB.
- book_src/02_ch02b_transaction_cost_analysis_for_credit.md: captions of Figures 2-B.1 and 2-B.3 only (what the image draws, where its numbers come from, the source, the assumptions). No embed line, figure number or placement changed; no prose changed.

<!-- STATUS: COMPLETE -->
