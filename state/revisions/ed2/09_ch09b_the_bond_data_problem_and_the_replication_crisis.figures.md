# Figures log: Chapter 9-B (ed2 U4)

Plan. No ed2 brief file existed for U4. The advisor brief (state/advisor_briefs/09_ch09b_the_bond_data_problem_and_the_replication_crisis.md, section 5) names four figures, and the chapter already embeds captions for all four, but none of the four PNGs had ever been drawn and tools/figures/ch09b.py did not exist (the fact-check log also notes the four files missing). The same situation as Ch 8-D. So this pass (a) draws the four promised PNGs, (b) adds one new figure the chapter lacked (the Stage 0 flow graph), and (c) renumbers every caption in order of appearance as 9-B.k (the chapter's four captions said "9B.k", unlike every other chapter's "N-B.k").
Script: tools/figures/ch09b.py (python3 tools/figures/ch09b.py; no network needed; data for Figure 9-B.4 in tools/figures/data/ch09b_drr_fig6_mom6_alpha.csv).
Order of appearance:
1. ch09b_stage0_pipeline (9B.2, NEW): flow graph of the Stage 0 order, with the Brambleworth Monday example threaded through it.
2. ch09b_two_prices (9B.3, EXISTING embed): one bond's prints over a month-end, the two windows, the three prices, the gap wedge.
3. ch09b_lib_waterfall (9B.4, EXISTING embed): Table 1 premia three ways for seven price-based factors.
4. ch09b_mom6_trimming (9B.5, EXISTING embed): six-month momentum alpha against trimming threshold, four ways.
5. ch09b_two_leg_bounce (9B.7, EXISTING embed): a two-leg pair's daily P&L from raw prints vs bounce-filtered prices.
Skipped on purpose: the brief's optional ch09b_survivors (432-cell grid, 26 lit): Chapter 4 already carries the audit scoreboard as Figure 4.4 and 9B.6 points back to it; a delay-cost bar chart for 9B.9 (Dickerson-Nozawa-Robotti, real numbers) would be a good sixth figure but the chapter would then exceed five.

