# Figures log: Chapter 15 (Event-Driven M&A, Regulatory Spreads & Change-of-Control)

Task U4 (Edition 2). Script: tools/figures/ch15.py. Output: assets/figures/ch15_<slug>.png.
No state/revisions/ed2/15_ch15...brief.md exists, so figures were chosen from the chapter's headings and key sections.
Plan (5 figures, in order of appearance): deal-outcome clause map (15.1.2), coupon-vintage put intrinsic value (15.2.2), SMR gauge (15.4.2), competing-risks cumulative incidence (15.5.2), WBD timeline (15.8).

## Embedded figures (all five viewed as PNG, clean; each under 500 KB)

- **Figure 15.1, ch15_deal_clause_map.png** (Section 15.1.2, after the paragraph on the issuer's counter-options). Flow graph of the deal-outcome tree: signing, regulatory clock, three outcomes (close, abandon, litigated block) with hazards h_c, h_a, h_b, the six clauses of the table hung on the branches that fire them, forced flow in italics, and the issuer's consent strip or defeasance knocking out clause 1. Data: none; schematic, captioned "Illustrative".
- **Figure 15.2, ch15_coupon_vintage_put.png** (Section 15.2.2, after the "aha number one" paragraph). Put intrinsic value (101 minus post-close price, floored at 0) against coupon for a strategic buyer (60bp) and a sponsor LBO (350bp), with the 1.85%, 5.00% and 6.875% vintages and the break-even coupon c*. Data: computed from the chapter's stated model (4.5 years left, flat Treasury zero 4.4%, strike 101); captioned "Illustrative".
- **Figure 15.3, ch15_smr_gauge.png** (Section 15.4.2, after the worked-number paragraph). Left: SMR price against break probability for P_close = 99.0, 100.98, 103.0, marking the quoted 99.40 and 20% break probability. Right: error in the implied probability from a 0.10-point price error against |P_close - G_f|, showing the switched-off region. Data: worked example of 15.4.2 (4.60% tranche, T_f = 0.25, G_f = 100.98); captioned "Illustrative".
- **Figure 15.4, ch15_competing_risks_incidence.png** (Section 15.5.2, after the cumulative-incidence identity). Aalen-Johansen cumulative incidence of close, abandon and block, total exits (1 - S), and the dashed cause-specific shortcut 1 - exp(-Lambda_c), which overstates closing (about 90% against 72% at 1.5 years). Data: the seeded 600-deal synthetic cohort of Listing 15.4 (same generator, seed 11), estimators written from scratch; the sum identity is asserted to 1e-12; curves stop where fewer than 20 deals remain at risk. Captioned "Illustrative".
- **Figure 15.5, ch15_wbd_timeline.png** (Section 15.8, after the "Three suitors, one clock" paragraph). Event timeline for Warner Bros. Discovery, June 2025 to October 2026, by lane (legacy bonds, deal, loans and financing), with the 8-month gap between the covenant strip (Jun 16, 2025) and the winning bid (Feb 27, 2026). Data: dates from the chapter's own WBD 8-K citations (EDGAR); the Dec 4, 2025 Netflix date from the advisor brief (state/advisor_briefs/15_ch15_event_driven_mna_and_coc.md, EDGAR 8-K link). Captioned "Source: WBD 8-Ks".

## Notes for the chapter reviser (chapter text not changed)

- Section 15.2.2, Step 4, strategic-buyer column: the stated model (4.5 years, UST zero 4.4% plus 60bp, y = 5.0%) gives A = 3.98 (not 4.08), c* = 5.3% (not 5.2%), and P_post of 87.2, 99.8 and 107.2 (table shows 87.4, 100.3 and 107.9). The LBO column and A = 3.71, c* = 8.3% check out. Figure 15.2 is computed exactly from the model and labels no strategic-buyer numbers, so it does not conflict, but the table's strategic column should be recomputed.
- Not used for figures but available: the HSR table in Section 15.5.1 (second-request share and early terminations, FY2016 to FY2025) would suit a two-panel regime-shift chart if a sixth figure is wanted.

<!-- STATUS: COMPLETE -->
