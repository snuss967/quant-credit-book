# Figure check: Chapter 14 (ed2 U4)

Checked all five embedded PNGs (ch14_two_default_rates, ch14_competing_risks_cif, ch14_redefault_clock, ch14_two_humps, ch14_lme_timeline) against tools/figures/ch14.py, the chapter text, state/research/trend_lmt_default_recovery_cycle.md and the house style (tools/figures/style.py). Every PNG was viewed; edge margins were measured with PIL (all at least 5 px, no clipping). Embedding: five `![Figure 14.n: ...](assets/figures/...)` lines, numbered 14.1 to 14.5 in order of appearance, every file exists, each under 120 KB.

## Figure 14.1 ch14_two_default_rates: PASS after caption fix
- Correctness: bar values 5.8/2.1 and 4.7/1.6 match Moody's (7 Aug 2025; 18 May 2026 direct-lending proxy). Ratio labels 2.8x and 2.9x are computed (5.8/2.1 = 2.76, 4.7/1.6 = 2.94), consistent with "almost three". Share points 32, ~50, ~60, ~60, ~65 match the Trend Watch and the dossier.
- Honesty: Real data, cited. Gap found: the 4.7%/1.6% proxy comes from Moody's 18 May 2026 (Hamilton), which the caption did not cite. Fixed. Also added that the S&P shares are US defaults (the right panel mixes S&P US and Moody's rated universes).
- Legibility/style: no collisions; legend clear of the ratio labels; orange = distressed exchange and blue = ex-DE hold the chapter's role colors; one y-axis per panel; text in ink.
- Embedding: after the Moody's 5.8% vs 2.1% paragraph that introduces it. OK.

## Figure 14.2 ch14_competing_risks_cif: PASS (one text cross-reference added)
- Correctness: S = exp(-lambda t), F_H and F_D = (lambda_x/lambda)(1 - S), so S + F_H + F_D = 1 exactly. 1 - KM_D = 1 - exp(-lambda_D t) is above F_D for every t > 0 and the gap rises monotonically (derivative lambda_D[exp(-lambda_D t) - exp(-lambda t)] > 0). At 15 years: F_D = 0.376, 1 - KM = 0.435, matching the plot.
- Honesty: caption says Illustrative, states lambda_H = 2.2% and lambda_D = 3.8%, which the chapter derives in 14.2.1. Matches.
- Legibility: white-on-blue and ink-on-orange labels inside the stack are legible; "1 - KM" and F_D end labels are not clipped (8 px margin); no overlaps.
- Embedding: figure follows the Aalen-Johansen identity paragraph (left panel), but its right panel illustrates the KM-trap item that follows. Fix: added "as the right panel of Figure 14.2 shows" to that item in 14.2.2.

## Figure 14.3 ch14_redefault_clock: FAIL on first view, fixed, now PASS
- Correctness: eta = 2/(-ln 0.3)^(1/k) gives 1.53/1.66/1.71, equal to the chapter table. F(2) = 0.175 = 0.70 x 0.25 for all k (anchor point correct). Year-six increments recomputed as 0.68/0.56/0.39 pp, equal to the chapter table. Population hazard h = p f0/((1-p) + p S0) is right and tends to 0. ROBO: 1 - exp(-0.11 u) is 0.667 at u = 10, expected time 9.1 years, matching the Ways This Blows Up box.
- Honesty: caption said the exponential "keeps climbing toward two-thirds", but two-thirds is its value at year ten, not a limit (the limit is 100%), and the right panel was not described. Fixed: the caption now describes both panels and says the exponential reaches two-thirds by year ten.
- Legibility: the first render had the dashed ROBO curve cutting through the legend entries and through the "ROBO's exponential" label. Fixed: legend moved to upper left, ROBO label moved to the open area right of its curve; re-viewed, no collisions.
- Style: the three shapes used RED, GREEN and BLUE, which broke the script's own role map (RED = excluded lenders in Fig 14.4, BLUE = hard default) and the fixed-order rule. All three curves are the same hard-default clock, so they now use one hue (blue ramp, light to dark with k; k = 1.2 preferred is darkest and thickest). Direct end labels on the right panel remain.
- Embedding: after the table and the paragraph that says "Figure 14.3 plots the three clocks". OK.

## Figure 14.4 ch14_two_humps: PASS after small fixes
- Correctness: Beta(74,26) and Beta(25,75) weighted 0.526/0.474 (areas 0.526 and 0.474). Mixture mean 50.8, total s.d. 24.85 (between-group 24.47, which is the chapter's 24.5). Moment-matched single Beta is Beta(1.55, 1.50), the flat arch drawn.
- Honesty: Illustrative, with Beta concentrations stated as assumed. Two fixes: the label said "s.d. (25 points)" while the chapter says 24.5; the label now says 24.9 and the caption explains 24.9 = 24.5 from membership plus within-group noise. Caption "puts its mass at a recovery" changed to "peaks at", because the Beta spreads its mass and only its peak sits at 51.
- Legibility: "Excluded" label sat within a few pixels of the red hump; moved out. The "49 points apart" arrow ran 27 to 72 (45 points); it now spans the two means, 25 to 74.
- Embedding: after the 24.5-point paragraph. OK.

## Figure 14.5 ch14_lme_timeline: PASS after small fixes
- Correctness: spans recomputed from the plotted dates: Serta 22 Jun 2020 to 23 Jan 2023 = 31 months; Wesco/Incora Mar 2022 to 1 Jun 2023 = 15; Mitel Oct 2022 to 10 Mar 2025 = 29; Del Monte Aug 2024 to 1 Jul 2025 = 11. 24-month ticks fall before the filing for Serta and Mitel and after it for Wesco and Del Monte, so "two inside, two outside the window" is right. Seven rulings match the Docket Diary dates (20 Jun 2024, 31 Dec 2024 twice, 17 Jan 2025, Sep 2025, 8 Dec 2025, 7 Jul 2026) and sit at the correct x positions. Names are sorted by LME date.
- Honesty: dates trace to the 14.3 Trend Watch, the 14.6 Docket Diary and 14.8. The Del Monte exchange month is flagged "reported, not verified" in the chapter but was plotted without that hedge; the caption now says so ("August 2024 ... as reported and not verified against the docket").
- Legibility: ruling key text raised from 7.6 to 8 pt; longest key line clears the nearest marker by about 28 px. Legend (orange circle = LME close, blue square = filing, bar = 24 months) uses the chapter's roles; no overlaps.
- Embedding: after the New Year's Eve paragraph that introduces it. OK.

## Files changed
- tools/figures/ch14.py (Fig 14.3 colors, legend, ROBO label; Fig 14.4 label offsets, arrow, s.d. label; Fig 14.5 key font), re-run: all five PNGs rewritten (84 to 115 KB).
- book_src/14_ch14_default_and_recovery_cycle_lmt_era.md (captions of Figures 14.1, 14.3, 14.4, 14.5; one cross-reference sentence in 14.2.2).
- Not changed, noted: chapter line 50 quotes Moody's "almost one-third" for 2.1/5.8, which is 36%; it is a direct quote, so left as is.

<!-- STATUS: COMPLETE -->
