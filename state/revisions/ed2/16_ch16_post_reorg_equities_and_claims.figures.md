# Figures log: Chapter 16 (ed2 U4)

Plan (no brief file existed; figures chosen from the chapter text; no figure dossier existed, so data are either sourced numbers quoted in the chapter or an Illustrative stated model):
1. ch16_overhang_delivery_lag (16.2.2): discount path, instant release vs staggered delivery. Illustrative.
2. ch16_backstop_put_and_fee (16.3.2): right and backstop payoffs, fair fee vs discount. Illustrative.
3. ch16_claim_recovery_pool_risk (16.5.3): E[R] vs V/m, near-par cost vs deep-OTM gift. Illustrative.
4. ch16_hertz_timeline (16.6): Hertz 2020-2026 events and sourced price points.
5. ch16_post_reorg_return_distribution (16.8.1): single name vs 20-name book. Illustrative.

## Embedded figures (all five drawn by tools/figures/ch16.py, each PNG viewed and cleaned)

- **Figure 16.1, ch16_overhang_delivery_lag.png** (§16.2.2, after the peak-timing paragraph): liquidity discount path for instant release (theta = 3.4, half-life 2.4 months) vs staggered delivery (alpha = 5), trough -6.6% at 2.9 months, 200-day marker. Data: Illustrative, the chapter's two-compartment model with the Poker Table parameters (kappa Q0/M = 15%); matches the chapter's -4.4%, -6.6%, -1.2% markouts.
- **Figure 16.2, ch16_backstop_put_and_fee.png** (§16.3.2, after the fee table): left, rights (call) and backstop (short put) payoffs per plan share, K = 0.75, dilution 0.36; right, fair fee vs discount for T = 0.25 and 0.50 with 6% (Seth 2025) and 10% (Hertz 8-K/A, 14 May 2021) reference lines. Data: Illustrative Black-Scholes, sigma 70%, zero rate, dilution factor 0.64; reproduces the table (8.9/12.5, 3.0/6.3, 0.3/1.6).
- **Figure 16.3, ch16_claim_recovery_pool_risk.png** (§16.5.3, after "Jensen cuts both ways"): E[R] vs V/m for s = 0.30 and 0.60 against min(1, V/m); marks 0.917 at par and 0.328 at V/m = 0.30. Data: Illustrative closed form of §16.5.3.
- **Figure 16.4, ch16_hertz_timeline.png** (§16.6, before the Docket Diary): Hertz 2020-2026 event timeline plus the three sourced price points ($10.00 rights, $29.00 re-IPO, about $3 in Jun 2026) against the $13.80 warrant strike. Data: sourced facts in the chapter (Hertz 8-K/A 14 May 2021, 8-K 7 Jul 2021, press release 8 Nov 2021, Third Circuit opinion 10 Sep 2024, 2026 press reports); no price path implied.
- **Figure 16.5, ch16_post_reorg_return_distribution.png** (§16.8.1, after the mean/median paragraph): histogram of 200-day single-name return (mean +33%, median -5%, 5% jump to -100%) beside a 20-name equal-weighted book (median +29%, 12% of books lose money). Data: Illustrative, 400,000 draws per panel from the §16.8.1 mixture, seed 16.

Chapter edits: five embeds plus one pointer sentence each, nothing else changed.
<!-- STATUS: COMPLETE -->
