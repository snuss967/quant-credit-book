# Figures log: Chapter 14 (ed2 U4)

No brief existed (section 3) and state/research/trend_figure_data_series.md does not exist, so figures were chosen from the chapter's headings.
Data: state/research/trend_lmt_default_recovery_cycle.md (sourced evidence table) and numbers stated in the chapter text; models are labelled Illustrative.
Script: tools/figures/ch14.py. Planned (in order of appearance):

1. ch14_two_default_rates (14.1): headline vs ex-DE default rates; DE share of defaults. Real data.
2. ch14_competing_risks_cif (14.2.2): S + F_H + F_D = 1 and the Kaplan-Meier overstatement. Illustrative.
3. ch14_redefault_clock (14.3.2): mixture-cure clock, three Weibull shapes vs ROBO's exponential. Illustrative.
4. ch14_two_humps (14.4.1): Serta recovery as a two-hump mixture vs a single moment-matched Beta. Illustrative.
5. ch14_lme_timeline (14.6): LME-to-filing spans for four names and the court rulings. Real dates.

Done / embedded:

- **Figure 14.1 ch14_two_default_rates** (section 14.1, after the Moody's 5.8% vs 2.1% paragraph). Left: headline vs ex-DE default rate (Moody's spec-grade bonds + loans TTM Jun 2025: 5.8% vs 2.1%; direct-lending proxy 2025: 4.7% vs 1.6%). Right: DE share of defaults (S&P 2010-23 32%, S&P 3 yrs to mid-2024 ~50%, Moody's 2024 ~60%, H1 2025 ~60%, 2025 ~65%). Data: real, from the chapter text and state/research/trend_lmt_default_recovery_cycle.md (Moody's AMR 7 Aug 2025, 6 Mar 2025, 28 Apr 2026; S&P 15 Aug 2024 via FTI 9 Oct 2026). Embedded.
- **Figure 14.2 ch14_competing_risks_cif** (section 14.2.2, after the Aalen-Johansen identity paragraph). Stacked S + F_H + F_D = 1; F_D vs 1 - KM_D (hard defaults censored) with the widening gap. Illustrative: constant hazards lambda_H = 0.022, lambda_D = 0.038 from section 14.2.1, closed form, no cures. Embedded.
- **Figure 14.3 ch14_redefault_clock** (section 14.3.2, after the k-shape paragraph). Mixture-cure Weibull, p = 0.25, k = 0.7/1.0/1.2 with eta solved from the 70%-within-two-years fact (eta = 1.53/1.66/1.71): cumulative hard-default probability vs ROBO's exponential (0.11/yr), and the population hazard on a log axis. Illustrative: model of section 14.3.2 calibrated to Moody's facts (Hamilton, 18 May 2026). Embedded.
- **Figure 14.4 ch14_two_humps** (section 14.4.1, after the 24.5-point standard deviation paragraph). Serta recovery mixture: pi = 0.526, Beta(74, 26) participants vs Beta(25, 75) excluded, against a single moment-matched Beta (mean 51, s.d. 24.9). Illustrative: 52.6%, 74 and 25 from the Serta remand facts (Mayer Brown, July 2026); Beta concentrations assumed. Embedded.
- **Figure 14.5 ch14_lme_timeline** (section 14.6, after the two-rulings-same-New-Year's-Eve paragraph). LME-to-filing spans (Serta 31 months, Wesco/Incora 15, Mitel 29, Del Monte 11) with a 24-month tick, plus seven numbered court rulings 2024-2026. Data: real dates from the chapter's Trend Watch, Docket Diary and case studies (S.D. Tex./D.N.J. dockets, law-firm memos); month-level where only a month is given; Del Monte exchange date as reported. Embedded.

Not drawn (considered): co-op break probability Pi(c) from section 14.5.1 (stays text-only; limit of 5 figures).
All five PNGs viewed and cleaned (collisions, clipped labels, legend overlaps fixed); each under 120 KB.

<!-- STATUS: COMPLETE -->
