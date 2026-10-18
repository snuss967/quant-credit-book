# Ch19 figure check (Edition 2)

Chapter: book_src/19_ch19_portfolio_trading_pricing_engines.md. Script: tools/figures/ch19.py. Figures log was COMPLETE.
Method: read the drawing code for each figure; recomputed every number quoted in the captions by loading the script's engine (Listings 19.1-19.8 executed from Appendix F); viewed every PNG; re-ran `python3 -I tools/figures/ch19.py` after fixes; `tools/check_book.py` reports the chapter OK.

## Figure 19.1 (ch19_handling_cost_fat_tail) - PASS, no change
- Correctness: size multiplier max(1, x/4)^eta is flat to $4mm with the kink exactly at the standard size and monotone above it; L042 at (18/4)^0.75 = 3.09x (2.1x to 4.5x across eta 0.5 to 1) matches the label. L042 handling cost $330k = 39.8% of the total on 8.4% of market value, matching "about 40% on 8%". Bars are the true top-10 by c0.
- Honesty: caption says Illustrative, cites eq. 19.3 and Listings 19.1-19.2. No real data.
- Style: one y-axis per panel, eta lines direct-labeled (sequential blue shades for an ordered parameter), L042 orange in both panels, text ink. No collisions (the leader line crosses the eta = 1 line once, harmless).
- Embedding: after the "last assert is the fat tail" paragraph, which also introduces it. Syntax and file OK.

## Figure 19.2 (ch19_hedge_bowl_and_basis) - PASS after fixes
- Correctness: left panel recomputed: unhedged $1.37mm, calm optimum $0.52mm at 1.0x (symmetric bowl, returns to $1.37mm at 2x), 3x basis gives optimum 0.507x and floor $1.03mm. Right panel: h*/h_DTS = 1/(1+rho^2) and surviving systematic variance = rho^2/(1+rho^2) follow from the section 19.4.1 formula with rho = sigma_u / (beta_h sigma_g); the two regions are exact complements. Section 19.4.1 exists as the caption says.
- Honesty: Illustrative, sources named. OK.
- Fixes made (script):
  1. The "unhedged: $1.37mm" note sat far from the grey square it describes; it now has a short leader to the marker.
  2. Right panel used BLUE, which is the handling colour everywhere else in the chapter. The hedge-ratio-kept region is now YELLOW (hedge role), boundary line in ink, surviving variance stays GREEN (risk role). Regions are direct-labeled.
  3. Log-axis ticks changed from 10^-1, 10^0, 10^1 to 0.1, 1, 10.
- Embedding: after the one-factor paragraph that points to it. OK.

## Figure 19.3 (ch19_stress_commonality) - PASS, no change
- Correctness: regime lines are straight in s; at s = 2 the multipliers are m 5.8, gamma 4.0, basis 5.0, and at s = 1 (ETF -2.5 sigma, 90th percentile spread) m 3.4, gamma 2.5, basis 3.0, matching caption and annotation. Right panel: idiosyncratic risk per dollar falls from 45.5bp (4 lines) to 7.8bp (148); the rank-one spike (0.25 s g'x / gross) stays near 20bp; the crossing near 16 to 32 lines supports "comes to dominate". The 148 ordinary lines are the basket minus L042 and L117.
- Honesty: Illustrative, cites Listings 19.4 and 19.6; no real-event dates drawn.
- Style: BLUE/YELLOW/GREEN direct-labeled with ink text (slot 4 yellow is labeled); RED for stress. The "risk aversion" label ends about 12px from the right panel's y-label: tight but clear.
- Embedding: after the `stress_cov` paragraph, which cites it. OK.

## Figure 19.4 (ch19_eviction_ranking_flip) - PASS, no change
- Correctness: ratios use the exact removal saving of eq. 19.7 and match the greedy loop's first step. Without AS: L042 305bp rank 1, L117 59bp rank 8, basket average 55bp. With AS: L117 1,093bp rank 1, L042 308bp rank 2, average 76bp. Both panels share one x-axis, so the flip is read at the same scale. Caption ("eighth, barely above the average", "about 1,090bp") matches.
- Honesty: Illustrative. Style: L042 orange, L117 violet (the AS colour) with a legend; bars are labeled by line id and rank. No collisions.
- Embedding: ends section 19.8.2's "two lines paying for the whole trade" paragraph, which introduces it. OK.

## Figure 19.5 (ch19_cost_stack_by_scenario) - PASS after fixes
- Correctness: terms recomputed per kept gross MV: full calm 76.3bp (handling 40.6, risk 14.4, AS 20.6, hedge 0.8), counter-proposal calm 36.6bp (L117, L042 out, target hit), full stress 257.4bp, counter-proposal stress 148.3bp with 10 evictions (14.4% of MV, under the 15% budget; target missed). The stacked terms sum to the labeled totals. The $ figures in the surrounding text (1.56mm, 829k, 420k, 293k, 16k) check out.
- Honesty: Illustrative, names price_pt of Listing 19.8.
- Fixes made (script and caption):
  1. Gridlines were drawn over the bars and read as segment boundaries; set_axisbelow(True).
  2. "45bp target" label was split around the dashed line; now one line above it at the right end.
  3. Total labels now sit directly above each bar on a white backing (the 37bp label no longer floats above the target line).
  4. The hedge term (yellow, slot 4) had no legend entry; added "Hedge half-spread (under 1bp)", and the legend now reads top-down in stack order. The in-figure note was dropped as redundant.
  5. Caption: added "(the hedge half-spread, under 1bp, is too thin to see)" since the figure shows three visible terms.
- Embedding: after the `price_pt` paragraph that says "Figure 19.5 stacks those terms". OK.

## Chapter-level checks
- Numbering 19.1 to 19.5 in order of appearance; all five files exist in assets/figures/ (each under 110 KB, 150 dpi); syntax `![Figure 19.n: ...](assets/figures/ch19_*.png)` matches other chapters; dollar signs escaped as in the chapter body.
- No real-world dates or real data in any figure, so no source citations are required beyond "Illustrative".
- Noted, not changed: section 19.8.2 quotes hand estimates "roughly 74bp ... about 35bp" and a "35bp concession", while Figures 19.4/19.5 and section 19.10 show the engine's 76bp and 37bp. The text carries its own caveat ("hand estimates ... differ in the second digit"), so left for the narrative pass; aligning them to 76/37 would remove a 2bp inconsistency a reader could notice.

<!-- STATUS: COMPLETE -->
