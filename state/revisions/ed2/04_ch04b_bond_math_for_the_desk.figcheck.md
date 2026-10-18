# Figure check: Chapter 4-B (ed2 U4)

Checked against tools/figures/style.py (house style), the script tools/figures/ch04b.py, Listing 4-B.1 (executed unchanged by the script), and each PNG viewed after re-running the script. All five figures are illustrative, built on the stylized 4.50% ten-year note; the real inputs are the FRED DGS10 yields (1.52%, 0.76%, 0.66%), already verified in the figures log. I recomputed every number a caption prints.

## Verdicts

**Figure 4-B.1, ch04b_duration_balance_point.png: PASS, no change.**
- Correctness: bars are each flow's share of PV (sum 100%); the marker is the PV-weighted mean time, which equals the listing's D_Mac (8.2478 at 3.50%, 7.7356 at 9.00%). Final payment is 66.7% and 59.9% of value, matching "two-thirds" and "60%".
- Honesty: caption says Illustrative and names Table 4B.1 and Listing 4-B.1.
- Style: shared y axis across two panels; 20 Feb blue, 23 Mar orange (date roles fixed for the chapter); labels in ink; no collisions or clipping.
- Embedding: follows the paragraph that gives 8.25 / 7.74; numbered first.

**Figure 4-B.2, ch04b_price_yield_taylor.png: FIXED.**
- Correctness: the tangent lies below the convex price curve everywhere (error negative on both sides of 3.50%), the parabola overshoots beyond about +400bp. The right-panel marker values were read from the nearest grid point (548.9bp), so the plot said -10.6 and the caption said 10.6; exact at +550bp the error is -10.67, and the chapter's own rounded arithmetic (48.3 predicted loss minus 37.6 actual loss) gives 10.7. Convexity overshoot is +2.12 (2.1, unchanged).
- Fix 1: the script now computes the +550bp errors exactly (p_lin - p_act, p_quad - p_act); the panel labels now read -10.7 and +2.1.
- Fix 2: the dashed +550bp event line ran through the direct labels "duration only" and "duration + convexity"; both labels now have a white halo.
- Fix 3 (caption): "10.6 points too low" changed to "10.7 points too low".
- Honesty, style, embedding: Illustrative caption; colors INK_2 / VIOLET / RED fixed for the three curves; one y axis per panel; placed after "How big is the second term?".

**Figure 4-B.3, ch04b_dv01_vs_dts.png: PASS (one robustness edit).**
- Correctness: DV01 8,785 / 5,236 / 7,258 (-40%, -17%); DTS 1,605 / 6,100 / 3,802 (x3.8, x2.4); caption's "fell 40%" and "rose 3.8 times" match. Bars start at zero.
- Edit: the panel title "3.8x riskier" was typed; it is now computed from the DTS values.
- Honesty: Illustrative, with the units (per $10mm face; DTS = D_mod x G-spread in bp) and the table/listing named; G-spread rests on the real DGS10 yields cited in Table 4B.1.
- Style: two panels (two scales), date colors blue / orange / green, values labeled on bars, no collisions.
- Embedding: directly after the DV01-versus-DTS paragraph.

**Figure 4-B.4, ch04b_five_rulers.png: FIXED (colour).**
- Correctness: 23 Mar levels G 824.0, Z 804.5, ASW par 678.5, ASW mv 959.2, PECS 945.3; spread of the rulers 280.5-280.8bp ("about 280bp", computed by the script); multiples 3.27 (par-par), 5.08 (PECS), 5.01, 4.16, 4.11 match the caption's 3.3 and 5.1. Z = OAS holds (asserted in the listing).
- Fix: the right-panel bars used SEQ_BLUE step 7, which is exactly the 20 Feb series blue (#2a78d6) and read as a 20 Feb quantity. Changed to the dark sequential step 11 so blue keeps one meaning in the chapter.
- Honesty: Illustrative, flat Treasury curve, FRED DGS10 cited for the real yields.
- Style: legend with three dated dots, no tiny or overlapping text, label "23 Mar spread / 20 Feb spread" fits (6 px margin).
- Embedding: after "Every ruler agrees ..." which says "Figure 4-B.4 shows the five rulers".

**Figure 4-B.5, ch04b_pnl_explain_waterfall.png: PASS (robustness edit).**
- Correctness: tranches sum exactly to the total: +6.68 - 54.99 + 12.79 - 2.12 = -37.64 = 70.73 - 108.38 (the script asserts it). Gains use the blue end and losses the red end of the diverging ramp; totals are neutral. Axis labels -76bp, +626bp, +550bp match the data.
- Edit: the bar labels (-76 bp, +626 bp, +550 bp) and the note "D = 8.11, C = 78.0" were typed; they are now computed from the data.
- Caption: components 6.7, 55.0, 12.8, 2.1 are each rounded, so they sum to 37.6 versus the printed 37.65 total, consistent with the chapter's own text.
- Honesty, style: Illustrative, real DGS10 moves noted; y axis from zero; all text ink or muted.
- Embedding: after "Then the P&L ...", which introduces it.

## Fixes made
1. tools/figures/ch04b.py: exact +550bp error markers and labels (Figure 4-B.2); white halo on the two direct labels; typed labels now computed (4-B.3 title, 4-B.5 axis labels and note); ratio bars in 4-B.4 recoloured. All five PNGs regenerated and re-viewed (48-106 KB each, under the 500 KB limit).
2. book_src/04_ch04b_bond_math_for_the_desk.md, Figure 4-B.2 caption: 10.6 -> 10.7.
3. book_src/04_ch04b_bond_math_for_the_desk.md, section 4B.7: the text-art block "Figure 4B.1 (schematic)" collided with the numbered Figure 4-B.1 (and sat out of order, between 4-B.3 and 4-B.4). Relabelled "Sketch 4B.1 (schematic, not a numbered figure)". Nothing else in the book referenced it.

## Judgement calls (left as is)
- Date series use SERIES slots 1, 2 and 6 (blue, orange, green) and skip aqua, which is below 3:1 on white. This is documented in the script docstring and keeps the dates legible without direct labels. Slots 3-5 are not used anywhere in the chapter.
- Chapter numbering "Figure 4-B.n" matches ch07b and ch12b; ch03b uses "3B.n". That is a book-wide convention question, not specific to this chapter.

## Flag for the orchestrator (not fixed: chapter table, not a figure)
Table 4B.1 prints the 23 Mar par-par asset swap as 679, but Listing 4-B.1 gives 678.497 (rounds to 678). The cold open's "280 basis points" (959 - 679) is 280.75 unrounded. The figures print neither number ("about 280bp" holds either way), so Figure 4-B.4 is unaffected; the table entry, or the listing's assertion tolerance (`abs(... - 678.5) < 1`), needs a one-line fix.
<!-- STATUS: COMPLETE -->
