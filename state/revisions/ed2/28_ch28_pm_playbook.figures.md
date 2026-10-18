# Figures log: Chapter 28 (ed2 U4)

No brief existed (section 3); state/research/trend_figure_data_series.md has no chapter-28 entry but confirms the FRED ICE BofA series and their 3-year rolling window. Figures were chosen from the chapter's own equations, worked numbers and the CCC case study. The chapter had no existing figures.
Script: tools/figures/ch28.py (run from the repo root). Data cache: tools/figures/data/ch28_ice_oas_2026ytd.csv (FRED BAMLH0A0HYM2, BAMLH0A3HYC, BAMLC0A0CM, 2026 rows only; fetched 18 October 2026). Licensing note for the editor: FRED flags the ICE BofA series "for internal use only; reproduction prohibited without ICE's written permission"; only the 2026 rows already quoted in the section 28.4 Trend Watch are cached and drawn.
Planned (in order of appearance):

1. ch28_breadth_ceiling (28.2): N_eff against bond count with the 1/rho_a ceiling; IR against breadth. Illustrative.
2. ch28_ccc_decompression (28.4, Trend Watch): 2026 OAS of IG, HY, CCC and the CCC/HY ratio. Real data (FRED).
3. ch28_kelly_ruin (28.4, case study): growth rate against fraction for Kaz's B3 bond and the CCC bucket in January vs October, with ruin boundaries. Illustrative.
4. ch28_mark_to_bid_stop (28.6): mark-to-bid shock against the two thresholds, and lifetime stop-out probability against stop distance. Illustrative.
5. ch28_leverage_band (28.7): floor, ceiling and speed limit against average LCS; the band empties. Illustrative.

Done / embedded:

- **Figure 28.1 ch28_breadth_ceiling** (section 28.2, after the "speed of light" paragraph). Left: N_eff against bonds in the book for rho_a = 0.01 and 0.03 (five bonds per issuer, rho_w = 0.9) with the 1/rho_a ceilings of 100 and 33 and Theo's point (300 bonds, N_eff = 39.7). Right: information ratio against independent bets at hit rates 50.5% and 52%, marking 40 versus 300 bets (1.0 vs 2.7; 4.0 vs 11.0). Data: Illustrative, equations (28.3) and (28.5); asserts reproduce 39.7, 65, 100, 2.7, 1.0, 11, 4.0. Embedded.
- **Figure 28.2 ch28_ccc_decompression** (section 28.4, after the CCC Trend Watch box, before "How a systematic desk would have read it"). Left: 2026 OAS of CCC-and-lower, HY and IG with the 30 March peak marked. Right: CCC/HY OAS ratio, 3.1 to 4.0. Data: real, FRED BAMLH0A0HYM2, BAMLH0A3HYC, BAMLC0A0CM (ICE BofA), 2 Jan to 15 Oct 2026, cached 2026 rows only in tools/figures/data/ch28_ice_oas_2026ytd.csv; asserts reproduce every number in the Trend Watch box (2.83/3.46/3.23, 8.88/8.38/10.20/12.82/12.78, 0.79/0.84). Embedded.
- **Figure 28.3 ch28_kelly_ruin** (section 28.4, after the "How a systematic desk would have read it" paragraph). Left: Kaz's B3 bond, expected log growth against f with Kelly 0.93, half Kelly, the ruin boundary 1/L = 1.67 and Merton's 1.93 beyond it. Right: CCC bucket in January (c 8.4%, lambda 6%, L 0.55; f* 1.10, ruin 1.82) and October (c 12.8%, lambda 10%, L 0.70; f* 0.65, ruin 1.43). Data: Illustrative, equations (28.9)-(28.11); c from FRED BAMLH0A3HYC, lambda and L are the section's illustrative inputs. Embedded.
- **Figure 28.4 ch28_mark_to_bid_stop** (section 28.6, after the "Theo's desk ... 7.2% of NAV" paragraph). Left: mark-to-bid shock (28.21) for the multiplier menu 1.64/3/5.8/6 at G = 5, LCS 0.6% (0.96, 3.0, 7.2, 7.5% of NAV) against the 5% cut and 7.5% exit. Right: lifetime stop-out probability e^(-2 SR x / sigma) against stop distance for Sharpe 0.5/1/2 at 6% vol (29%, 8.2%, 0.7% at 7.5%), with the 0.3% effective stop after a 7.2% shock (90%). Log y axis. Data: Illustrative, equations (28.19)-(28.21). Embedded.
- **Figure 28.5 ch28_leverage_band** (section 28.7, after the "Theo's HY PM" paragraph). Floor (28.2) at hurdles 5% and 4%, ceiling (28.22)-(28.23) with mark-to-bid cost, and the speed limit, against average LCS; marks the no-liquidity band [3.16, 4.74], the empty band at LCS 0.8% (ceiling 2.14 < floor 3.16) and the reopened [2.5, 3.0] at LCS 0.4% with a 4% hurdle. Data: Illustrative, N_eff = 40, sigma_DTS 5%, SR 2, kappa z_p 4, DD_max 7.5%, m 5.8; asserts reproduce the chapter. Embedded.

Pointer sentences ("Figure 28.k shows ...") were added as one short paragraph before each figure; nothing else in the chapter was changed.
Not drawn (considered, limit of 5): break-even half-life h* by tier (28.3, text and table already carry it); lifetime hit-rate standard error against N_eff (28.2); days-to-liquidate and the FRTB ladder (28.5); two-signal combined IC against rho (28.8).
Flag for the editor: Exercise 1 asks for the largest LCS at which the band is non-empty; Figure 28.5 shows the crossing (about a third of a percent) without a number.
All five PNGs viewed and cleaned (label collisions, clipped text, curve overlaps fixed); each under 125 KB.

<!-- STATUS: COMPLETE -->
