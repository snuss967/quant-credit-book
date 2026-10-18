# Figure check (Edition 2): Chapter 8-C, The Morning Explain

Script: tools/figures/ch08c.py (re-run end to end after the fixes; all five PNGs rewritten, largest 201 KB, white background, 150 dpi).
Style reference: docstring of tools/figures/style.py (one y-axis, fixed colour order, direct labels for slots 3-5, text in ink, no in-image title).

Embedding (all five): syntax `![Figure 8-C.k: ...](assets/figures/ch08c_*.png)` is correct, every file exists, labels run 8-C.1 to 8-C.5 in order of appearance, no leftover "Figure 8C.k" labels in book_src (the stale 8C.k labels exist only in the generated output/ master book, which is rebuilt).

## Figure 8-C.1, ch08c_explain_waterfall: PASS after fixes

- Correctness: the twelve named lines are exactly the 8C.6 table and are asserted to foot (named lines -280.0; plus the -110.0 pending mark correction = -390.0; plus U -9.0 = -399.0). Bars start where the previous one ended; the sum and official bars run from zero. The tolerance band is centred on the explained total (-390) and the official -399 lies inside it; the inset shows U = -9 inside +-10. Checked arithmetic by hand: 75.8 + 12.4 - 52 + 40 - 338 + 110 - 16.7 - 96.3 + 0.3 - 15 - 4 + 3.5 = -280.0.
- Honesty: caption says Illustrative and its numbers match the chapter. The caption was silent on the inset and on what the band is centred on; fixed.
- Legibility: no collisions; 7.5 pt in-plot notes raised to 8 pt; the band label was touching the zero line after the size change, so it was shortened ("tolerance +-$10k around the explained total"); "x" in the legend replaced by a true multiplication sign.
- Embedding: the figure sat at the very end of 8C.4, after the month-end and ledger paragraphs, two paragraphs away from the tolerance paragraph it illustrates ("Monday's corrected residual was -$9,000, inside..."). Moved to directly after that paragraph (still in 8C.4, still number 8-C.1). Caption now reads: stale-mark and unexplained last, band of +-$10,000 around the explained total of -$390,000, inset zooms on the unexplained, "Illustrative: the numbers are the Monday table of 8C.6".

## Figure 8-C.2, ch08c_signal_split: PASS after fixes

- Correctness: standalone 3.0 and 2.0 stack to 5.0; the dashed box spans 2.4 to 5.0 and is the -2.6 interaction; sequential momentum-first 3.0 / -0.6 (negative segment drawn below zero); value-first 2.0 / 0.4; equal split = Shapley 1.7 / 0.7. All four columns net to 2.4 and the script asserts the numbers against the text (interaction -2.6, Shapley 1.7 and 0.7).
- Honesty: caption matches the image and says Illustrative, the chapter's September numbers.
- Legibility: the "interaction -2.6" label sat inside the box, over the orange bar and touching the dashed edges, and the "Momentum 0.4" label was crossed by the 2.4 reference line. Moved the interaction label (bold, ink) beside the dashed box, narrowed the bars so "Momentum" no longer touches the next bar, and nudged the 0.4 label down clear of the 2.4 line. Only slots 1-2 are used, with dot-and-text direct labels.
- Embedding: after the Shapley paragraph, before the Paleologo extraction. OK.

## Figure 8-C.3, ch08c_two_mornings: PASS after fixes

- Correctness: left, U = -119 as found is -9 (bond residuals) plus -110 (stale signature), then -9 after correction, inside the band. Right: every price, date and dollar figure checks against 8C.6: TRACE 84.25 for $2mm on 21 Oct, dealer runs 84-85 and 83 3/4-85 on 30 Oct, composite 84.2-84.6 for nine days, carry 84.50, neighbour's -9 points on 29 Oct, evaluated 81.50 (-$240k) on Monday 2 Nov, challenge 11:00 on 2 Nov, revised 84.00 (-$40k) on 3 Nov. 30 Oct 2026 is a Friday, so the weekdays in the chapter fit the calendar.
- Honesty: caption matches; Illustrative.
- Fixes: (1) the left bar was labelled "As found 7:28", but 7:28 is when Theo had the cause; the explain showed -11.9 bp at the 7:15 official run. Relabelled 7:15. (2) "challenge filed 2 Nov, 11:00" ran across the 29 Oct dashed line; re-wrapped to three lines. (3) "revised 84.00 (3 Nov)" ran to the right edge of the image; re-wrapped to three lines, which also let the right panel use the full width. (4) The right-panel title then overran the edge; shortened to "Morning (b): the Corriveau true-up".
- Aqua (slot 3) marks (stale signature, TRACE diamond, dealer runs) are all direct-labelled. One y-axis per panel.
- Embedding: at the end of 8C.6 after the Corriveau dispute paragraphs; it carries both mornings, as the caption says. Kept.

## Figure 8-C.4, ch08c_whale_shadow: PASS after fixes (real data, sourced)

- Correctness: 161 reported, 593 at mids, 593 - 161 = 432 unexplained, hatched on the right segment of the second bar. Timeline is ordinal and says so.
- Honesty, checked each event against the chapter's quotations from the Senate PSI report (15 March 2013): over $51bn (p.185); marks at or near the midpoint (p.5); $161mm / $593mm (p.5); $319mm and $512mm gap (p.5); over $157bn (p.185); $6mm re-issued after 90 minutes (p.5); mark as the Investment Bank, $690mm peak disputes (p.6); $660mm restatement, 13 July (p.98). Fixes: (1) the "Later" event put quotation marks round "more favorable prices within the daily range", but the chapter's quote is "...within the daily price range"; quote corrected and the unsupported "in Q1" dropped (the chapter says only "Later"), subject changed from "Marker" to "The book" as in the chapter. (2) The May event cited pp.5-6 where the chapter cites p.6; corrected to p.6. (3) The legend said aqua = "price set by an independent service", yet the left-hand "at mids" bar is also aqua and mids are not an independent service's prices; legend now reads "The desk's own marks" / "A price the desk did not choose (mids; from May, an independent service)". Caption: added "(hatched)" for the unexplained segment. Source line with page numbers was already present and is right.
- Legibility: nothing clipped; dollar signs are escaped; 7.5 pt footnote raised to 8 pt.
- Embedding: after "The outside explain" paragraph, before the dialogue. OK.

## Figure 8-C.5, ch08c_unexplained_by_day: PASS after fixes

- Correctness: the twelve breaches reproduce the ledger table (month-end true-ups 4 = 410; roll-week stale marks 3 = 260; booking 2 = 120; corporate actions 2 = 95; timing 1 = 18; total 903), asserted in the script; 7 breaches fall on the six marked days (three month-ends, one of which carries two true-ups, plus Mon-Wed of roll week), 5 elsewhere; the quiet bars are all below 10 and sum to 290. Mon 21 Sep is day 56 and 30 Sep day 63 on the abstract 63-day axis, which the axis label states. Dates fit the 2026 calendar (20 Sep 2026 is a Sunday, so the roll is effective Monday 21st).
- Honesty: the caption said only "Illustrative" although every bar is generated; now says the breaches are set to the ledger's cause totals ($903,000), the quiet days are simulated to sum to $290,000, and the axis is three 21-day months.
- Fixes: (1) the legend sat inside the plot with the Jul month-end dashed line running through its text; moved below the axes. (2) "Sep month-end" was cut by the roll-week edge line; month-end labels now sit above the plot (Sep on two lines to clear the roll-week band). (3) The roll-week band was the same pale blue as the tolerance band; now grey so pale blue means tolerance only. Text raised from 7.5 to 8 pt.
- Embedding: after the Edge Ledger paragraph that follows the table and the binomial box. OK.

## Flags for the prose (not changed: outside the figure-check scope)

- The 8C.9 ledger table says "51 days" inside tolerance and the text repeats "The 51 quiet days ... $290,000", but 63 days minus 12 breaches is 51 only if each breach has its own day. The chapter also says seven breaches fall on six days (two true-ups share a day), which leaves 11 breach days and 52 quiet days. Figure 8-C.5 follows the "seven on six days" statement and shows 52 quiet bars; it prints no count of quiet days, so it does not contradict the table on its face. The author should change "51" to "52" in the table and in the text after it (or drop the double day).
- The docstring's colour roles were loose: Figures 2 and 5 use blue and orange as plain categorical slots. The docstring now says so, and each figure names its colours in a legend or direct labels.

Verdicts: 8-C.1 PASS (fixed, moved); 8-C.2 PASS (fixed); 8-C.3 PASS (fixed); 8-C.4 PASS (fixed); 8-C.5 PASS (fixed).

<!-- STATUS: COMPLETE -->
