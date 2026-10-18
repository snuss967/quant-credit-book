# Figures log: Chapter 4-B (ed2 U4)

Plan (no brief file existed; figures chosen from the chapter text; no figure dossier existed for this chapter). Every bond number comes from Listing 4-B.1 (bondmath.py, Appendix F), which tools/figures/ch04b.py executes unchanged, so the figures reproduce Table 4B.1. The Treasury yields behind the table (1.52%, 0.76%, 0.66%) were checked against the FRED DGS10 CSV download (fredgraph.csv?id=DGS10) on 2026-10-18: all three match. The bond's yields are the chapter's illustrative ones, so every caption says "Illustrative".
1. ch04b_duration_balance_point (4B.3): PV weights of the 20 cash flows and the Macaulay balance point on 20 Feb vs 23 Mar.
2. ch04b_price_yield_taylor (4B.4): price-yield curve, tangent and two-term expansion; approximation error against yield change.
3. ch04b_dv01_vs_dts (4B.5): DV01 (-40%) vs DTS (x3.8) on three dates.
4. ch04b_five_rulers (4B.8): G, Z=OAS, two asset swaps and PECS on three dates, and the widening multiple per ruler.
5. ch04b_pnl_explain_waterfall (4B.8): the 20 Feb to 23 Mar P&L explain (rates, spread, convexity, residual).
Skipped on purpose: negative convexity of the callable (4B.7) already has the text schematic "Figure 4B.1 (schematic)".

## Embedded figures

All five drawn by tools/figures/ch04b.py (which executes Listing 4-B.1 from Appendix F unchanged); each PNG was viewed and cleaned (label collisions in 4-B.2, grid over bars, legend placement in 4-B.4 fixed). One embed plus one short pointer sentence per figure; nothing else in the chapter changed.

- **Figure 4-B.1, ch04b_duration_balance_point.png** (4B.3, after the paragraph giving D_Mac 8.25 / 7.74): left and right panels show each cash flow's share of present value at 3.50% and 9.00%, with the Macaulay balance point marked. Final payment is 67% of value at 3.50% and 60% at 9.00%. Data: Illustrative, Listing 4-B.1 on the stylized 4.50% ten-year note.
- **Figure 4-B.2, ch04b_price_yield_taylor.png** (4B.4, after "How big is the second term?"): left, true price-yield curve with the duration tangent and the duration-plus-convexity parabola built at 3.50%; right, approximation error against yield change (-10.6 for duration alone and +2.1 with convexity at +550bp). Data: Illustrative, Listing 4-B.1 (risk_at_yield, price); reproduces the chapter's 60.1 / 72.9 / 70.73.
- **Figure 4-B.3, ch04b_dv01_vs_dts.png** (4B.5, after the DV01-versus-DTS paragraph): DV01 per 10mm face ($8,785, $5,236, $7,258) and DTS (1,605, 6,100, 3,802) on 20 Feb, 23 Mar, 30 Jun. Data: Illustrative, Table 4B.1 recomputed by Listing 4-B.1; Treasury yields real (FRED DGS10, verified).
- **Figure 4-B.4, ch04b_five_rulers.png** (4B.8, after the paragraph "Every ruler agrees..."): dumbbell of five spread rulers (ASW market value, PECS, G, Z = OAS, ASW par-par) across the three dates, and the 23 Mar / 20 Feb multiple per ruler (3.3x to 5.1x). Data: Illustrative, Table 4B.1 recomputed by Listing 4-B.1.
- **Figure 4-B.5, ch04b_pnl_explain_waterfall.png** (4B.8, after "Then the P&L ..."): waterfall from 108.38 to 70.73: Treasury rally +6.7, spread widening -55.0, convexity +12.8, residual -2.1. Data: Illustrative, `explain` of Listing 4-B.1 with the real DGS10 moves (FRED DGS10).

## Flags for the orchestrator (not fixed: outside the figure edit's remit)
1. The chapter already has a text-art block labelled "Figure 4B.1 (schematic)" in 4B.7 (negative convexity). The new embedded figures are numbered 4-B.1 to 4-B.5 and the first of them appears earlier in the chapter, so the label "Figure 4B.1" now appears twice. Rename the schematic (e.g., "Sketch 4B.1") or replace it with a computed figure from the Brambleworth lattice.
2. Listing 4-B.1 returns an ASW par-par spread of 678.497bp on 23 March, which rounds to 678; the chapter's cold open and Table 4B.1 print 679 (and the chapter's "280 basis points" is 959 minus 679; the unrounded gap is 280.8). The figures avoid printing that entry; the chapter table or the assertion tolerance may need a one-line fix.
<!-- STATUS: COMPLETE -->
