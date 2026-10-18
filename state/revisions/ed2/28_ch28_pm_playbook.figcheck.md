# Figure check: Chapter 28 (ed2)

Checked against tools/figures/style.py (house style), the drawing code in tools/figures/ch28.py, the chapter text and equations, and each PNG viewed after the final run. All five figures are embedded in order (28.1 to 28.5), each preceded by a pointer sentence, each file exists, each under 125 KB. The script's asserts reproduce every number in the chapter (39.7, 65, 100, 2.7, 1.0, 11.0, 4.0; 0.926, 1.67, 1.93, 1.10, 0.65, 5.1%, 5.8%; 7.2, 7.5, 8.2%, 29%, 0.7%, 0.3%; 3.16, 4.74, 2.14, 3.9, 2.53, 2.95).

## Figure 28.1 ch28_breadth_ceiling (section 28.2): PASS after fixes
- Correctness: N_eff curve is equation (28.5) with m = 5, rho_w = 0.9; ceilings 1/rho_a = 100 and 33.3 are the N to infinity limits; Theo's point (300, 39.7) is on the curve. Right panel is the exact form of (28.3); the four labelled points (1.0, 2.7, 4.0, 11.0) agree with the text. Both curves are monotone increasing and concave as the theory demands.
- Honesty: caption says Illustrative and names the equations and parameters; matches the image.
- Legibility: left panel had no key linking the blue and orange curves to rho_a (identity was implied only by the pale dotted ceilings). Fixed: added a two-entry legend (upper left, clear of the 100 line, the curves and Theo's label). No other collisions.
- Embedding: after the "speed of light" paragraph; pointer sentence present.

## Figure 28.2 ch28_ccc_decompression (section 28.4 Trend Watch): PASS, no change
- Correctness: real series BAMLH0A0HYM2, BAMLH0A3HYC, BAMLC0A0CM, 209 rows of 2026 data. I re-fetched all three series from FRED on 18 October 2026 and compared every cached row: 0 mismatches, no newer observation than 15 October. Asserts confirm 2.83/8.88/0.79 (2 Jan), 3.46/10.20 (30 Mar), 3.23/12.78/0.84 (15 Oct), 12.82 (14 Oct), 8.38 (28 Jan). The 30 March event line sits on the HY peak. Ratio 3.1x to 4.0x correct.
- Honesty: caption cites the three FRED series, the date range and the fetch date, and its two claims match the plot. Note: the Trend Watch box says its figures were fetched 17 October; the figure's cache was written 18 October and is identical to FRED today, so both statements are true and no edit was needed.
- Legibility: direct labels on all three lines (aqua IG slot is direct-labelled); one y-axis per panel (two panels, not twinx); no collisions. Right-hand x-axis runs to early December only to hold the end labels.
- Standing flag (unchanged, for the editor): FRED marks the ICE BofA series "internal use only"; the figure draws only the 2026 rows already quoted in the box.
- Embedding: after the Trend Watch box, before "How a systematic desk would have read it".

## Figure 28.3 ch28_kelly_ruin (section 28.4): PASS after fixes
- Correctness: left panel is the one-period growth p ln(1+fc) + q ln(1-fL) with Kelly 0.926 at the maximum, half Kelly, a vertical asymptote at 1/L = 1.67 (curve stops just inside it), and Merton's 1.93 placed beyond ruin. Right panel is (28.10) with sigma = 0; maxima at 1.10 (growth 3.7%) and 0.65 (2.2%), ruin boundaries 1.82 and 1.43. Concave, single maximum, drops to minus infinity at 1/L, as required.
- Legibility: two collisions that the earlier pass missed (visible when enlarged): the "ruin 1.43" label touched the October curve, and the "(Oct)" end of the bottom note was crossed by it. Fixed: label moved to the right of the orange dashed line; note wrapped to two lines at lower left.
- Honesty: caption cited only (28.9) and (28.10) and did not explain the dashed lines or Merton's 1.93. Fixed: caption now says dashed lines are the ruin boundaries, that Merton's 1.93 lies beyond ruin, and cites (28.9)-(28.11) with sigma = 0 in the right panel. Illustrative label, inputs and the FRED source for c are stated.
- Embedding: after the "How a systematic desk would have read it" paragraph; pointer sentence present.

## Figure 28.4 ch28_mark_to_bid_stop (section 28.6): PASS after fixes
- Correctness: bars are (28.21) at LCS 0.6%, G = 5 for m = 1.64, 3, 5.8, 6 (0.96, 3.0, 7.2, 7.5% of NAV), matching the menu and sources in section 28.5; thresholds 5% and 7.5% match the rule. Right panel is exp(-2 SR x / sigma) at 6% vol: straight lines on the log axis, ordered by Sharpe, 29% / 8.2% / 0.7% at 7.5%, and 90% at the 0.3% effective stop.
- Legibility: the dashed line at 7.5% in the right panel was unlabelled, and the Sharpe-1 label read "8%" while the text says 8.2%. Fixed: line labelled "exit 7.5%", label changed to 8.2%. Slot 2 (aqua) is direct-labelled. No collisions.
- Honesty: caption now states that the four multipliers are each applied to the same book and that (28.19) is used as its lifetime limit. Illustrative label present.
- Embedding: after the "Theo's desk ... 7.2% of NAV" paragraph; pointer sentence present.

## Figure 28.5 ch28_leverage_band (section 28.7): PASS after fixes
- Correctness: floor 3.16 (hurdle 5%) and 2.53 (4%) are flat in LCS; ceiling (28.23) falls monotonically from 4.74 through 2.95 (0.4%) and 2.14 (0.8%), crossing the 5% floor at about 0.33% LCS; speed limit DD/c1 (3.9 at 0.8%) stays above the ceiling everywhere. The band is shaded only where ceiling >= floor.
- Legibility: gridlines were drawn over the shaded band (a pale stripe at G = 4). Fixed with set_axisbelow(True). Direct labels everywhere, ink text, one y-axis, no collisions.
- Honesty: the dashed speed-limit curve was not mentioned in the caption. Fixed. Parameters and equations stated; Illustrative.
- Embedding: after the "Theo's HY PM" paragraph; pointer sentence present.

## Style notes (no change made)
- Colors follow roles per figure (blue, orange, aqua in order), not one global series-to-color map: CCC is orange in 28.2, the January case is blue and October orange in 28.3. Acceptable under the per-figure fixed-order rule; flagged only so the editor knows it was seen.
- Panel titles "(a)/(b)" are used as in other chapters' scripts; there is no in-image figure title.

## Files changed
- tools/figures/ch28.py (legend in 28.1, label and note placement in 28.3, "8.2%" and exit label in 28.4, grid order in 28.5); all five PNGs regenerated.
- book_src/28_ch28_pm_playbook.md: captions of Figures 28.3, 28.4, 28.5 only.

<!-- STATUS: COMPLETE -->
