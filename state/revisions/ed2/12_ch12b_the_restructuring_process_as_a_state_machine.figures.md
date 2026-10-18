# Figures log: Chapter 12-B (ed2 U4)

Plan (no brief file existed; figures chosen from the chapter text; the chapter had no figures; no dossier data series apply, so statutory periods quoted in the chapter's own clock table are the only "real" data and every other figure is an Illustrative stated model or the chapter's own illustrative Halvorsen numbers):
1. ch12b_out_of_court_machine (12B.4): the out-of-court menu as a state machine with guards and clocks.
2. ch12b_chapter11_clocks (12B.5): the clock table laid on one day axis from the petition.
3. ch12b_waterfall_call_spreads (12B.6): classes as call spreads; fulcrum; expected delta = pi_j / C_j.
4. ch12b_plan_value_transfer (12B.6): senior and junior recovery against the plan value.
5. ch12b_halvorsen_waterfall (12B.9): where the 1,300 of plan value goes (silos to claims).

## Embedded figures

(All five drawn by tools/figures/ch12b.py; each PNG viewed and cleaned: label collisions, overflowing box text and a mathtext dollar-sign bug fixed.)

- **Figure 12-B.1, ch12b_out_of_court_machine.png** (§12B.4, after the "Two edges carry most of the desk's risk" paragraph): flow graph of the out-of-court menu drawn with matplotlib patches: Performing, Stressed, Grace, Event of default, Forbearance, Post-LMT, RSA signed, Petition, hand-off to Chapter 11; guards (missed interest, 30-day grace invariant, s >= theta_eff, tender >= 90%, 2/3 amount and 1/2 number RSA vote) and clocks on the arrows; Post-LMT -> Stressed re-default edge highlighted. Data: none; structure is the §12B.4 transition table (typical document terms, SEC Rule 14e-1, 11 U.S.C. §1126(b)).
- **Figure 12-B.2, ch12b_chapter11_clocks.png** (§12B.5, after the effective-date paragraph, before the clock table): the clock table on one day axis from the petition (13 clocks: stay, Rule 6003 window, schedules, final DIP hearing, §341 meeting, challenge period, two exclusivity clocks with extension to the 18- and 20-month caps, lease clock, governmental bar date, §546(a) avoidance period, preference and 503(b)(9) look-backs). Data: statutory and rule periods quoted in the chapter's clock table (11 U.S.C. and Fed. R. Bankr. P.); challenge period is a typical DIP-order term, drawn from the petition.
- **Figure 12-B.3, ch12b_waterfall_call_spreads.png** (§12B.6, after the fulcrum-delta paragraph): left, stacked dollars paid to each of four classes against distributable value V (each band is a call spread; old equity is the last call; V = 450 marked); right, expected delta pi/C in recovery points per +100mm of V (Class 2 12.8, Class 3 13.5, Class 4 2.6, Class 1 0.0). Data: Illustrative, strict absolute priority, claims 100/300/400/200, V lognormal with median 450 and sigma 0.40.
- **Figure 12-B.4, ch12b_plan_value_transfer.png** (§12B.6, after the "high plan value is the senior class selling equity" paragraph): senior R1 = V/Vplan and junior R2 = (Vplan - C1)V/(C2 Vplan) against the plan value from 800 to 1,400; at Vplan = V = 1,000 the senior is whole and the junior has 33%; both converge to 71% at 1,400. Data: Illustrative, the chapter's two-class all-equity formulas with C1 = 800, C2 = 600, V = 1,000.
- **Figure 12-B.5, ch12b_halvorsen_waterfall.png** (§12B.9, after the "plan delivers an exit ABL" paragraph): Sankey of the Halvorsen 1,300 plan value from ABL collateral 250, term-loan collateral 960 and unencumbered value 90 to ABL 150, first lien 760 (60.8% of 1,250), DIP 300, administrative and priority 75, unsecured pool 15 (1.5% of 1,020). Data: the chapter's own illustrative Halvorsen numbers (fictional company, 12B.9 waterfall steps 1-5); no external data.

Chapter edits: five embeds plus one pointer sentence each, nothing else changed. No real time-series data used: the chapter's quantitative content is statutory periods, fictional Halvorsen numbers and stated models.
<!-- STATUS: COMPLETE -->
