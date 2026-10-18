# Figure check: Chapter 4 (ed2)

Chapter: book_src/04_ch04_inside_the_systematic_credit_industry.md. Script: tools/figures/ch04.py. Figures log was COMPLETE. House style read from the docstring of tools/figures/style.py. All five embedded PNGs were re-derived, viewed (full size, and zoomed where a collision was suspected), and checked against the chapter text and the dossier. Script re-run after every fix; all five files are under 130 KB.

Embedded figures: 4.1 effective_breadth, 4.2 truncation_bias, 4.3 factor_zoo_survivors, 4.4 capacity_hot_tub, 4.5 empty_cells_map. Numbering is in order of appearance (lines 269, 417, 507, 752, 937), every file exists, every image follows the paragraph that points to it, and the in-text pointers say 4.1, 4.2, 4.3, 4.4 and 4.5 in the right places.

## Figure 4.1 ch04_effective_breadth: PASS after one fix

1. Correctness. The curves are 1/(1+(m-1)rho), the share form of equation (4.1); all are monotone down, equal 1 at rho = 0, and end at 1/m at rho = 1 (the 47-bond issuer ends at 1/47). The ringed worked-example point is 1,800/(1+1.25 x 0.7) = 960 (asserted in the script); IC 0.03, TC 0.5 gives IR 0.636 (0.64) and 0.465 (0.46), as the label says.
2. Honesty. The caption says "Illustrative: equation (4.1)" and names the five m values; the picture shows exactly those five curves. No real-data claim.
3. Legibility. One y-axis; one-hue blue ramp for the four m values (magnitude), gray dashed for the 47-bond case; end labels direct; text in ink. Defect found: the boundary note ("rho = 0: every bond is a bet; rho = 1: one bet per issuer") sat about 3 px under the m = 8 curve. Fix: moved to the empty upper right as two lines, clear of every curve and of the call-out leader.
4. Embedding. Correct syntax, follows the worked example and the sentence "Figure 4.1 draws equation (4.1) for four universes and for ROBO's 47-bond issuer."

## Figure 4.2 ch04_truncation_bias: PASS after fixes

1. Correctness. Left: standard normal, lower 1% shaded, cut at z = -2.326 (label "u < -2.33"). Right: normal shift phi(z_q)/(1-q) = 0.0269 at 1% (0.027, 11bp at 4% volatility); Student t with 4 df uses the exact partial expectation f(c)(nu+c^2)/(nu-1), scaled by sqrt(nu/(nu-2)); the mixture uses root-finding for the cut and the exact partial mean, scaled by its own standard deviation. Independently checked by Monte Carlo (4 million draws): 0.0268, 0.0375, 0.0620 against the plotted 0.0269, 0.0373, 0.0620. All three curves are monotone in q, and mixture > t > normal at every one of the 80 grid points between 0.1% and 5%, so the caption's "larger at every cut" is true. The tail sizes match the caption's stated models (98% N(+0.5, 2) and 2% N(-12, 6)).
2. Honesty. "Illustrative", the closed form is named, both alternative models are stated, units are "standard deviations of its own distribution". Matches the picture.
3. Legibility. Direct labels on all three curves (aqua is slot 3 and is direct-labelled); fixed color order blue, orange, aqua; no twin axes. Defects found: (a) the left label "worst 1% of months deleted" ran into the bell outline ("deleted" crossed the curve); (b) the inset's title was wider than the inset and spilled past the axes; (c) the inset's baseline touched the bell outline; (d) "before" hung outside the inset and the 0.3 gridline appeared to strike through the labels. Fixes: four short lines in a white-backed label left of the curve; two-line inset title; inset moved right, narrowed and re-scaled so its labels, title and ticks sit inside it with a visible gap to the bell; "what is left" label moved off the 0.1 gridline.
4. Embedding. Follows the "manufactures the premium" paragraph, before the Full Derivation that the caption cites ("derived below").

## Figure 4.3 ch04_factor_zoo_survivors: PASS, no change

1. Correctness. 108 x 2 x 2 = 432; 65 (15.0%) pass t > 1.96; 26 (6.0%) survive BH-FDR; panel counts EW within-firm 16, VW within-firm 9, EW single-sort 1 (bond age), VW single-sort 0; 25 of 26 within-firm. All asserted in the script and matching state/research/papers_factor_replication_crisis_and_bond_data.md section 3.4 (IA.3: "VW single 0, VW within-firm 9, EW single 1, EW within-firm 16 = 26"). Bars are drawn from zero with true lengths.
2. Honesty. Caption cites Dickerson, Robotti and Rossetti (2026), arXiv:2604.07880, Internet Appendix IA.3, CAPM-B alpha, BH at 5% within each of the four panels, before trading costs; all of that is in the dossier. The picture shows exactly the stated counts.
3. Legibility. One axis per panel, two panels; gray ramp for funnel stages, blue for within-firm and orange for single-sort (same roles as the rest of the chapter); the "25 of the 26" bracket does not collide; no slot 3-5 colors. No clipping.
4. Embedding. After the Friday scoreboard paragraph that gives these numbers and ends "Figure 4.3 draws that scoreboard."

## Figure 4.4 ch04_capacity_hot_tub: PASS, no change

1. Correctness. Net alpha g - 2 T eta sqrt(2TA/L) and dollar alpha A x net match the chapter's alpha(A) and Pi(A); the peak is at A* = L g^2/(18 T^3 eta^2) and equals A* g/3; the zero is at 9/4 A*. Recomputed: HY book g = 120bp, A* = 1.852bn, peak 7.4mm, zero at 4.17bn; momentum g = 275bp, A* = 134.4mm, peak 1.24mm, zero at 302mm; client keeps 40bp and 92bp. The arrow runs from the peak to the straight line g x A (two thirds of the edge lost to impact) and the hill is concave with a single top. Script asserts 1.852, 4.167 and 134.4.
2. Honesty. "Illustrative", equation (4.2), the shared inputs and each book's alpha0 and T are in the caption. "More than twice the edge" (g 2.29x, alpha0 2.67x) and "over four times the turnover" (4.17x) are true; $134mm and $1.85bn match.
3. Legibility. Two panels with different dollar scales instead of two y-axes; blue for the HY long/short book and orange for momentum (the chapter's roles); annotations are ink with white backing and do not touch the dashed line or the hill. The two panel titles are panel labels, not an in-image title.
4. Embedding. After the worked example, which ends "Figure 4.4 draws both tubs."

## Figure 4.5 ch04_empty_cells_map: PASS after fixes

1. Correctness. All 48 cells re-read against the section 4.3 table: Man 2022 F F F F S S; Man 2023 S F S F S S; Blackstone F F F S S S; BlackRock F F S X X F; Nuveen F F F X S F; Robeco F S F X X S; Acadian F F S X X X; Barclays all F. Eight silent cells, four in execution and three in capacity (seven of the eight), matching the caption, and asserted in the script.
2. Honesty. Caption names the source (the 4.3 table) and says the shading is the book's own reading of each cell, then gives the silent-cell count that the picture shows. The dashed row (LMT exposure, distressed, bond choice within an issuer) is stated as "no entry at all", which matches 4.11's "No framework paper on the map has a feature for it."
3. Legibility. Light-gray "silent" cells used two sizes of italic text, the smaller at 6.9 pt ("not modeled", "not disclosed"), below the style's readable minimum. Fix: both wrapped to two lines at 7.8 pt, same size as "silent". One-hue blue magnitude (dark = specific, pale = stated); legend swatches clear of labels; no clipping.
4. Embedding. Placement is right (after the four numbered blanks), but the pointer sentence said the figure "puts Theo's whole sheet on one page", which overclaimed: three of the four numbered blanks (loans and private credit, sovereign and securitized, event-driven) are not on the figure. Fix: the sentence now says the figure shows the six columns with the unfilled cells shaded and, in the dashed row, LMT exposure, distressed debt and bond choice within an issuer.

## Fixes made (summary)

- tools/figures/ch04.py: Fig 4.1 note moved; Fig 4.2 label, inset geometry, inset title and "what is left" label; Fig 4.5 silent-cell labels. All five figures regenerated; assets/figures/ch04_*.png updated.
- book_src/04_ch04_inside_the_systematic_credit_industry.md: one sentence (the Figure 4.5 pointer in 4.11). Nothing else touched.

## Left alone, for the chapter author

- Three `<!-- FIGURE: ... -->` placeholders remain by design and are not embedded: ch04_pod_fee_waterfall (4.1, line 121), ch04_etrading_timeline (4.7, line 705), ch04_genealogy (4.11, line 913). If any is drawn, number by order of appearance and renumber the later ones (pod fee waterfall would be 4.1; e-trading would fall between the current 4.3 and 4.4; genealogy between 4.4 and 4.5). The 2021-22 Greenwich values for the e-trading figure are flagged CHECK in the dossier and must be sourced first.
- Text, not figure: the worked example says the IR difference "is about 28%" (0.64 to 0.46 rounded gives 28.1%; unrounded it is 27.0%), so "about 27%" would be exact.
- Text, not figure: section 4.3 says "Only Man 2023 and Barclays treat [execution and capacity] as first-class", while the map shades Man 2022's execution cell dark (a specific cost model, p.21) and Man 2023's capacity cell pale. The sentence and the map agree only if "first-class" means both columns; consider "only Barclays treats both as first-class".

<!-- STATUS: COMPLETE -->
