# Ch19 figures log (Edition 2, task U4)

Script: tools/figures/ch19.py (executes Listings 19.1-19.8 from book_src/95_appF_code_companion.md, so every number is the chapter's own synthetic cold-open basket; all figures are "Illustrative"). Run: python3 tools/figures/ch19.py
No brief file existed; figures chosen from the chapter's headings. No existing figures in the chapter at start.
Color roles: terms of eq. 19.2 (handling BLUE, risk GREEN, AS VIOLET, hedge YELLOW); L042 ORANGE, L117 VIOLET; stress RED.

## Embedded figures

1. **Figure 19.1, ch19_handling_cost_fat_tail** (section 19.3, after the "last assert is the fat tail" paragraph). Left: size multiplier max(1, x/4mm)^eta of eq. 19.3 for eta 0.5, 0.75, 1 with line 42 marked at 3.1x. Right: the ten most expensive lines by handling cost; L042 is about 8% of notional and 40% of handling cost. Data: Illustrative, Listings 19.1-19.2 synthetic basket.
2. **Figure 19.2, ch19_hedge_bowl_and_basis** (section 19.4, after the one-factor "With no basis" paragraph). Left: 5-day P&L std of the cold-open basket vs hedge size (x the calm optimum): $1.37mm unhedged, $0.52mm at optimum; with 3x basis the optimum is 0.5x and the floor $1.03mm. Right: one-factor attenuation, hedge ratio kept = 1/(1+rho^2) vs basis noise over hedge factor risk. Data: Illustrative, Listing 19.3 and the section 19.4.1 formula.
3. **Figure 19.3, ch19_stress_commonality** (section 19.7, after the `stress_cov` paragraph). Left: regime map, one score s to m, gamma and basis multipliers (5.8x, 4.0x, 5.0x at the cap). Right: risk per dollar vs number of lines (random subsets of the 148 ordinary lines): idiosyncratic falls ~45bp to ~8bp, the rank-one liquidity spike at s = 1 stays ~20bp. Data: Illustrative, Listings 19.4 and 19.6.
4. **Figure 19.4, ch19_eviction_ranking_flip** (section 19.8.2, after the "two lines paying for the whole trade" paragraph). Top-8 lines by exact removal saving per dollar of MV, without and with the AS term: L042 leads (305bp) without AS, L117 is rank 8 (59bp, near the 55bp basket average); with AS L117 jumps to rank 1 (about 1,090bp). Data: Illustrative, eq. 19.7, Listings 19.5 and 19.7.
5. **Figure 19.5, ch19_cost_stack_by_scenario** (section 19.10, after the `price_pt` paragraph). Stacked four-term cost in bp of kept gross MV for full list calm (76bp), counter-proposal calm (37bp), full list stress s = 1 (257bp), counter-proposal stress with 10 evictions (148bp, target missed). Data: Illustrative, price_pt of Listing 19.8.

Checks: all five PNGs viewed and cleaned (label collisions, clipped axis labels and text fixed); each under 110 KB; python3 -I tools/figures/ch19.py regenerates all five; tools/check_book.py reports the chapter OK (the odd $$ warning is pre-existing, 45 delimiters before and after).

<!-- STATUS: COMPLETE -->
