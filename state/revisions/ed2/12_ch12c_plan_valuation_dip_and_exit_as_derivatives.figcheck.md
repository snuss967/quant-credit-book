# Figure check (Edition 2): Chapter 12-C

Checked: tools/figures/ch12c.py (house style read from tools/figures/style.py), the five embedded ch12c_*.png, and their captions and placement in book_src/12_ch12c_plan_valuation_dip_and_exit_as_derivatives.md. The figures log carried its completion marker.

Method: besides reading the drawing code and viewing every PNG, I recomputed the model independently of the plots (scratch check, not kept in the repo): the silo waterfall sums to V at every V on a 0 to 6,000 grid (max error 5e-13) and each class's payout is non-decreasing; payoff kinks fall at V = 150, 250, 468.8, 490.6, 891.7, 1,857.8 and 2,795 (the first lien's ramp is 490.6 to 1,857.8, the unsecured pool's last ramp ends at 2,795); the histogram masses sum to 1.0000 (first lien, including the 17.2% point mass) and 0.9992 (unsecured pool, mass below 0.5% recovery omitted); the 5th and 95th percentiles reproduce the chapter's table (46.2% / 100% and 1.9% / 35.2%); the fulcrum curves are monotone (first lien up, unsecured pool down) and old equity never exceeds 0.088%; the take-back exact price and first-order line cross at 200bp ($26.54mm) and differ by $1.0mm at 300bp (2.6%).

## Verdicts

**Figure 12-C.1, ch12c_call_spreads.png: PASS after fixes.**
- Correctness: bands are the true silo waterfall and stack exactly to V; kinks at the strikes (first lien 490.6 to 1,857.8, unsecured pool 891.7 to 2,795, old equity above 2,795); V* = 1,858 and 2,795 marked correctly; density is the right right-skewed lognormal mixture (mode near 1,290, shoulder near 1,900); shaded areas are 82.8% and 17.2%.
- Honesty: Illustrative, but the caption said the density was "overlaid" while the image draws it in a shared-x panel beneath the bands (twinx is banned by the house style). Caption rewritten to match, and it now names the model (mixture of §12C.1, waterfall of §12C.10).
- Legibility and style: no collisions; one y-axis per panel; BLUE first lien, ORANGE unsecured pool, greys for the rest; no slots 3 to 5. The "Old equity" label sat 5 px from the right edge; moved inside its wedge with margin.
- Embedding: it sat after the "Kaz's question" anecdote, two paragraphs away from the fulcrum-probability formulas it draws, with no pointer in the text. Moved to directly after the paragraph that closes the mixture formulas, and a pointer sentence added to that paragraph.

**Figure 12-C.2, ch12c_rollup_transfer.png: PASS after one label fix.**
- Correctness: left panel 65.0 to 100.0 for the rolled 150 (gain $52.5mm) and 65.0 to 60.8 for the 1,250 left behind (4.2 points x 1,250 = $52.5mm, conserved); right panel (W - x)/(F - x) falls monotonically and accelerates, 60.8 at 150 and 55.5 at 300 (-4.2 and -9.5 points), reaches 0 at kM = W = 910 where the chapter's guard refuses the formula.
- Honesty: caption matches; Illustrative with the formula and inputs named.
- Legibility: no collisions, leader lines clear of text. The in-plot label "shaded gap = transfer to the rolled holders" was imprecise (the vertical gap is points of recovery per 100 of face left behind, not dollars); relabelled "shaded gap = loss per 100 of face left behind".
- Embedding: after the roll-up paragraph that points to it; numbered 12-C.2.

**Figure 12-C.3, ch12c_recovery_distributions.png: PASS after fixes.**
- Correctness: first-lien hump near 60 (debtor's expert, 59.7 mean), flat committee tail from 70 to 100 and a 17.2% point mass at par; unsecured pool hump near 3 to 4 (debtor), a committee hump at 5 to 8 (V below V*, where only the unencumbered share pays) and a long tail to 100 that is essentially all committee (debtor share beyond 10% recovery: 0.008%); means 70.3 and 8.3 match the analytic values; log-axis bins are equal in log recovery so heights are comparable.
- Honesty: caption matches. Added "(dark: the debtor's; light: the committee's)" so the shading code is in the caption.
- Legibility and style: (1) the point mass at par was drawn on top of the last histogram bin [97.5, 100), so the foot of the spike was double-shaded and the mass was conflated with that bin; it is now a separate bar just right of the last bin. (2) The right panel had no key for dark versus light; added a compact "Expert adopted" key in clear space, away from bars and the mean line. Text stays 8 pt or larger, in ink.
- Embedding: after the "Look at the shape before the numbers" paragraph, which points to it.

**Figure 12-C.4, ch12c_fulcrum_prob_vs_dip.png: PASS (caption addition only).**
- Correctness: 74.8 / 25.1 at M = 0, 82.8 / 17.2 at 150, 90.0 / 10.0 at 280, as the caption says; monotone; old equity's probability stays under 0.1% (max 0.088%), as the in-plot note says.
- Honesty: caption now states the model ("the mixture of §12C.1 with the first-lien strike V*(M) of §12C.10") in place of a bare "Illustrative".
- Legibility: direct labels at the line ends, blue and orange in fixed order, one y-axis, no clipping (end label has 7 px margin).
- Embedding: after the paragraph that cites it; numbered 12-C.4.

**Figure 12-C.5, ch12c_takeback_transfer.png: PASS after fixes.**
- Correctness: exact = F x gap x a5(8% + gap) (the chapter's P/S = 1 - (y - c) a_n(y)), first order = F x a5(10%) x gap; both give $26.5mm at 200bp, $13.3mm per 100bp for the line, exact bends below it beyond 200bp, agree within 2.6% at 300bp. Matches the chapter's $26.5mm and 92.4 price.
- Honesty: caption now says the plan coupon is held at 8.0% so the market yield is 8.0% plus the gap (otherwise the x variable is ambiguous), and which line is which.
- Style: the dashed line was ORANGE and the exact line BLUE, but in this chapter blue and orange mean first lien and unsecured pool; the first-order line is the baseline approximation, so it is now grey (MUTED) per the chapter's convention ("grey is the baseline"), and the exact line stays blue (the note electors' first-lien transfer). End labels were 9 pt apart and touching; separated by 3 pt each way.
- Embedding: after the paragraph that cites it; numbered 12-C.5.

## Fixes made (summary)

- tools/figures/ch12c.py: label positions (12-C.1, 12-C.2, 12-C.5), point-mass bar and right-panel key (12-C.3), first-order line colour (12-C.5); re-run, all five PNGs regenerated and re-viewed (all under 140 KB, margins at least 5 px); check_model() assertions still pass.
- Chapter: Figure 12-C.1 moved up two paragraphs with a pointer sentence; captions of 12-C.1, 12-C.3, 12-C.4 and 12-C.5 edited as above. Numbering is in order of appearance (12-C.1 to 12-C.5), no old "12C.k" references remain, every file exists, the Debrief mention of Figure 12-C.1 still resolves.

## Open item for the chapter editor (prose, not changed here)

- §12C.10 "almost a third of its expected value comes from the committee's hump, where it is paid in full": by the figure's own numbers the committee's expert supplies 0.3 x 95.2 / 70.3 = 40.6% of the first lien's expected recovery (about two fifths), and the paid-in-full spike alone supplies 17.2 x 100 / 70.3 = 24.5% (about a quarter). Neither is "almost a third". Suggest "about two fifths of its expected value comes from the committee's hump, a quarter from the spike at par alone".
<!-- STATUS: COMPLETE -->
