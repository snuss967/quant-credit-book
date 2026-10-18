# Figures log: Chapter 9 (ed2 U4)

No brief existed (section 3). state/research/trend_figure_data_series.md carries only ICE/FRED series whose redistribution ICE restricts, so no ICE series is used. Figures were chosen from the chapter's headings; data are the sourced numbers quoted in the chapter (Dynkin, Man, Israel-Palhares-Richardson) or models stated in the captions (labelled Illustrative).
Script: tools/figures/ch09.py. Planned (in order of appearance):

1. ch09_kaz_book_dts_neutral (9.2.3): Kaz's book dollar-neutral vs DTS-neutral. Illustrative.
2. ch09_momentum_decay_clock (9.4.1): top-decile survival and monthly outperformance. Sourced (Dynkin p.610-611).
3. ch09_breakeven_cost (9.4.2): break-even round-trip cost vs turnover. Sourced (Dynkin p.633, p.703).
4. ch09_equal_risk_vs_best_single (9.7.1): equal-risk blend vs average correlation. Sourced IRs (IPR 2018, Man 2022) plus equation (9.5).
5. ch09_noisy_price_premium (9.9): Blume-Stambaugh bias and the lag-one reversal "alpha". Illustrative simulation.

Done / embedded:

- **Figure 9.1 ch09_kaz_book_dts_neutral** (section 9.2.3, after the carry paragraph). Left: leg DTS per 100mm long for the long leg (12.0), the dollar-neutral short (7.2) and the DTS-neutral short (166.7mm, 12.0), with the 4.8 gap that gives beta 4.8/8 = 0.6. Right: 84 simulated months of book return against the index excess return: dollar-neutral slope 0.6 with +0.8%/yr carry, DTS-neutral slope 0 and zero carry. Data: Illustrative; the chapter's worked example (DTS 12.0, 7.2, market 8.0; spreads 2.0% and 1.2%), seeded simulation, no signal. Embedded.
- **Figure 9.2 ch09_momentum_decay_clock** (section 9.4.1, after the half-life paragraph). Left: top-decile survival 0.17^(t/3) (stay probability 0.55 a month, half-life 1.2 months) with the sourced 17%-at-three-months point. Right: outperformance per month 35, 22, 19bp, then the 19bp remainder of the 95bp six-month total spread over months 4-6 (76 of 95bp = 80% in the first quarter). Data: Dynkin et al. p.610-611 as quoted in the chapter; survival curve is the implied Markov chain. Embedded.
- **Figure 9.3 ch09_breakeven_cost** (section 9.4.2, after the break-even paragraph). Break-even round-trip cost c* = (gross/12)/TO against monthly one-way turnover for the 6.34% EMC portfolio (point at 73%, 0.72%) and the 2.5% worked example (point at 35%, 0.6%), with Barclays LCS levels (IG 2008 2.8%, HY July 2019 0.94%, IG 2018-19 0.6%) as horizontal lines. Data: Dynkin et al. p.633 and p.703 as quoted in the chapter; equation (9.3). Embedded.
- **Figure 9.4 ch09_equal_risk_vs_best_single** (section 9.7.1, after the "run the formula backward" paragraph). Equal-risk blend IR against average pairwise correlation for the four-factor sets of Israel-Palhares-Richardson (0.35, 1.11, 0.85, 1.75) and Man (2.15, 1.69, 1.55, 0.79), with the best single factor, the published blends (2.19 and 2.35, implied correlations -0.05 and 0.24) and the break-even correlations (0.12 and 0.36). Data: IRs quoted in the chapter (IPR 2018; Man 2022 p.28); curves from equation (9.5). Embedded.
- **Figure 9.5 ch09_noisy_price_premium** (section 9.9, after the Mechanism 2 paragraph). Left: Monte Carlo bias in the mean computed return against pricing error sigma_u, on the sigma_u^2 curve (3% gives 9bp a month). Right: decile long-short return of a reversal sort at lags 1 to 4 on noisy marks (1,000 bonds, about 240 months, sigma_u = 1%, true returns i.i.d.): 1.07% a month at lag one, about zero at lags two to four. Data: Illustrative; seeded simulation of the section's model. Embedded.

Not drawn (considered): the buffer hysteresis of 9.8.3, and a Gilchrist-Zakrajsek credit-spread series for the tight-spread Trend Watch of 9.10 (the five-figure limit; ICE/FRED series are not used because ICE restricts reproduction).
All five PNGs viewed and cleaned (collisions, clipped labels and legend overlaps fixed); each under 110 KB.

<!-- STATUS: COMPLETE -->
