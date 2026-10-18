# Figures log: Chapter 11 (ed2 U4)

Plan (no brief file existed for this chapter, and the chapter had no figures; figures chosen from the chapter's headings and key derivations). The only figure dossier used is state/research/trend_figure_data_series.md (FRED series IDs and the ICE three-year-window note); every other number is either quoted in the chapter with its source or generated from a stated model and labelled Illustrative.

1. ch11_mixture_skew (11.1.1): the mixture return and the skew of its jump.
2. ch11_capture_plane (11.2.1): the capture-ratio plane, beta tilt versus alpha.
3. ch11_dd_pd_map (11.3.2): the normal-distribution trap, N(-DD) against an empirical DD-to-PD map.
4. ch11_exclusion_pays (11.5.2): one 77% hit rate, two exclusion fractions, opposite signs.
5. ch11_tier_oas (11.6.2): ICE BofA tier spreads and the CCC-to-index ratio.

Skipped on purpose: the capacity curve of 11.9 (closed form, already a two-line formula), the 2022 round-trip path of 11.2.3 and the April 2025 z-signal of 11.8.1 (the tariff shock is marked on Figure 11.5 instead).

## Embedded figures (all five drawn by tools/figures/ch11.py; each PNG viewed and cleaned until no label collisions, clipping or off-axis text remained)

- **Figure 11.1, ch11_mixture_skew.png** (section 11.1.1, after the "Read that table twice" paragraph): left, the one-year excess return of a bond as 97% N(3.3%, 4.0%) survive plus a 3% jump of -60% (mean +1.4%, std. dev. 11.5%, jump 88% of variance); right, skewness -(1-2p)/sqrt(p(1-p)) against p on a log axis with the chapter's points -6.9, -4.1, -1.5 at 2%, 5%, 20%. Data: Illustrative, the section 11.1.1 mixture; the 3.3% survive-case mean is the 326bp single-B OAS of 15 Oct 2026 (FRED BAMLH0A2HYB) and the 60% price loss is the chapter's L_P example.
- **Figure 11.2, ch11_capture_plane.png** (section 11.2.1, after the decomposition paragraph and table): upside against downside capture, the diagonal of pure beta tilts, the benchmark, and the two BlackRock managers with arrows from their same-beta alpha-zero points. Data: capture ratios 89.56/92.24 and 92.00/99.00 are BlackRock (2025) p.3 as quoted in the chapter; the alpha-beta split is the section 11.2.1 identity with the chapter's illustrative regime means (+1.6%, -2.0%), reproducing beta 0.91/0.95 and alpha 29bp/75bp of the chapter's table.
- **Figure 11.3, ch11_dd_pd_map.png** (section 11.3.2, after the Bohn-Stein source extraction box, before "Where the structural PD breaks"): Gaussian N(-DD) against the placeholder empirical map PD = exp(-0.718 - 0.9718 DD) capped at 35% from Listing 11.2, the DD = 4 gap (0.003% against 1.0%, about 300 times), the DD > 4 zone, and the sponsor-levered B issuer. Data: Illustrative; the issuer (E 2,000, sigma_E 55%, STD 600, LTD 3,000) is re-solved in the script with the listing's own nested Brent search and asserted to give DD 2.44 and PD 4.6% (Gaussian 0.74%), matching the chapter. DD > 4 majority claim: Bohn-Stein p.138 as quoted in the chapter.
- **Figure 11.4, ch11_exclusion_pays.png** (section 11.5.2, after the "Same hit rate, opposite sign" paragraph): the default loss avoided (pi_X - pi_K) L as a function of the exclusion fraction q at a fixed 77% hit rate, with the chapter's two excess-spread inputs as markers; +44bp at q = 20% and -9bp at q = 40%. Data: Illustrative, the section 11.5.2 credit-triangle arithmetic (3% default rate, L = 0.6, 420bp and 300bp excess spreads); the script reproduces 6.41%, 2.78%, +44bp and -9bp.
- **Figure 11.5, ch11_tier_oas.png** (section 11.6.2, after the paragraph giving the 15 Oct 2026 closes): left, daily OAS of BB, B, CCC & lower and the index with the 7 Apr 2025 tariff shock marked; right, the month-end ratio of CCC & lower OAS to index OAS with the chapter's points 2.61, 2.54, 3.15, 3.53, 3.96. Data: real, FRED BAMLH0A0HYM2, BAMLH0A1HYBB, BAMLH0A2HYB, BAMLH0A3HYC, pulled 18 Oct 2026 (794 rows, 8 blank holiday rows dropped, 17 Oct 2023 to 15 Oct 2026); the script asserts the 15 Oct closes (323, 197, 326, 1,278bp) and all six month-end ratios quoted in the chapter.

Chapter edits: five embeds, five one-sentence pointers ("Figure 11.k draws ..."; Figure 11.3's pointer is its own short paragraph because the figure follows a source-extraction box), nothing else changed. Figures are numbered 11.1 to 11.5 in order of appearance (the chapter had none before).

## Flags for the author

- Licensing: FRED marks every ICE BofA series "for internal use only; reproduction prohibited without ICE's written permission" (see the dossier). Figure 11.5 is a chart and a derived ratio, not a data file, and the raw CSVs are deliberately NOT stored in the repository (the script caches them in ~/.cache/quant-credit-book/ and re-downloads on demand). If the publisher wants no ICE-derived chart at all, drop Figure 11.5 and its pointer sentence; nothing else depends on it.
- Reproducibility: FRED serves only a rolling three-year window of the ICE series, so a re-run after October 2026 will start later than 17 Oct 2023; the script truncates at 15 Oct 2026 and its assertions will fail loudly if the window no longer reaches the quoted month-ends (Jan 2025 to Oct 2026).
- Figure 11.3 uses the Listing 11.2 placeholder map, which is calibrated so that DD = 4 gives 1%; it illustrates the shape of the trap, not a calibrated EDF.

<!-- STATUS: COMPLETE -->
