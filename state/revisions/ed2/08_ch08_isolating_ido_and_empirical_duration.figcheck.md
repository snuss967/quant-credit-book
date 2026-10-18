# Figure check: Chapter 8 (ed2 U4, figure checker)

Chapter: book_src/08_ch08_isolating_ido_and_empirical_duration.md. Script: tools/figures/ch08.py. Figures log: COMPLETE. Style read from the docstring of tools/figures/style.py. All five PNGs viewed before and after the fixes; all are under 135 KB, 150 dpi, white background, no in-image title, one y-axis, text in ink.

Chapter-wide color roles (checked, accepted): Baa/IG blue (SERIES[0]), Ba/HY orange (1), B green (5), Caa/CCC violet (6); truth blue and screen/stale orange in Figures 8.2 and 8.3. Slots 2 to 4 (aqua, yellow, magenta) are never used, so the low-contrast rule does not bite, and every multi-series figure still direct-labels its lines. A role keeps its color across the chapter, which is what "fixed order" is for.

## Figure 8.1, ch08_hedge_ratio_by_rating (Section 8.2): PASS after one wording fix
- Correctness: lines are H = beta + gamma*s from Table 8.1 (Baa 0.85/-0.02, Ba 0.41/-0.05, B 0.15/-0.03, Caa 0.07/-0.02 per 100 bp). Recomputed: at 700 bp Baa 0.71 (Ben Dor p.207 quote), Ba +0.06, B -0.06, Caa -0.07. Implied end spreads 900, 1,340, 1,900 and 2,950 bp reproduce the table's H at max sample OAS (0.67, -0.26, -0.42, -0.52). All slopes negative, so every line falls monotonically; Baa stays far above the HY lines at the 700 bp overlap.
- Honesty: caption cites Ben_Dor p.192 Table 7.1 (Table 8.1), says the end spread is implied by rounded coefficients and why Aaa-Aa and A are omitted. Real data, sourced.
- Legibility: direct labels at line ends, 700 bp event line, B and Caa dots at 700 bp sized so both show; no collisions or clipping.
- Embedding: after the "Read the table like a credit agreement" paragraph, which points to the figure. File exists.
- Fixes: caption and in-image note said Ba, B and Caa sit "at or below zero" / "zero or negative", but Ba is +0.06. Now "near or below zero" / "near zero or negative" (script re-run, PNG re-viewed).

## Figure 8.2, ch08_recovery_route (Section 8.3): PASS after one caption addition
- Correctness: P = (c + lambda R)/(r + lambda); screen duration 1/yield = P/c, true 1/(r + lambda), ratio c/(c + lambda R). Recomputed at lambda = 21%, c = 9%, R = 40%, r = 4%: 7.73 and 4.00 years, H^rec = 0.517. Both durations equal 25 years at lambda = 0 and fall monotonically; H^rec falls from 1 toward 0 and falls faster for higher R (20/40/60% curves ordered correctly). H^rec is independent of r, as the in-panel note says.
- Honesty: caption says "Illustrative", states c, R, r and that r enters only the left panel. The chapter does not state r; the caption now carries it.
- Legibility: direct labels (screen / true, R = 20/40/60%), single-hue sequential ramp for R, "fiction" gap labelled, event line and 0.52 call-out clear.
- Embedding: after the H^rec = 0.52 paragraph, which says "Figure 8.2 shows both halves". 
- Fix: caption now names the three R curves and says 0.52 is the 40% curve.

## Figure 8.3, ch08_stale_marks_beta (Section 8.5): PASS after three fixes
- Correctness: the script executes Listings 8.1-8.4 of Appendix F in one namespace (seed 8, 2,500 days), so numbers are the chapter's own: OLS 0.494 (= first weight 0.5), Scholes-Williams 0.810, Dimson 1.005 (sum of the three lag slopes, asserted equal to beta_dim). The stale line lags and smooths the true line, as the weights (0.5, 0.3, 0.2) imply.
- Fix 1 (honesty): the Scholes-Williams bar was labelled 0.812, the sum of the two drawn pieces, but the estimator is 0.8097 because a -0.002 lead term is not drawn. The label now shows the estimator (0.810); the script asserts drawn stack and estimator agree to within 0.005.
- Fix 2 (style): the "true" line was a dark gray; it is now the chapter's truth blue (as in Figure 8.2), with stale marks in the screen orange.
- Fix 3 (caption): a reader sees OLS same-day 0.49 beside SW same-day 0.52. Caption now explains the 1/(1 + 2 rho_f) rescaling and the undrawn lead term.
- Legibility: direct labels on the left panel; stacked bars labelled inside, lag legend on top; no collisions.
- Embedding: after the Scholes-Williams paragraph ("Figure 8.3 shows the staleness and the three estimators"). Caption is Illustrative and names the listings and seed.

## Figure 8.4, ch08_rolling_hedge_ratio (Section 8.7, Case Study C): PASS (data independently reproduced), one body-text rounding fix
- Correctness: H = 1 + sbar*rho*sigma_s/sigma_y on rolling 60-day windows of daily relative OAS changes and DGS10 changes, common dates only. I recomputed H from the cached FRED CSVs with an independent loop; it matches the stored series at 2025-04-30 (CCC -0.0379, HY 0.214, IG 0.895), 2025-05-23 (CCC -0.7836), 2025-05-30 (CCC -0.6684) and 2026-06-04 (CCC 1.8539). Series range: 688 windows, 2024-01-12 to 2026-10-15; CCC min -0.78 on 2025-05-23, max 1.85 on 2026-06-04; IG min 0.786, max 1.038 (caption says 0.79 to 1.04, correct). Event line sits at 2 April 2025 (tariff announcement), CCC minimum annotated at the right date. H < 0 zone is labelled "minimum-variance hedge is long futures", which is the right sign.
- Honesty: caption cites the four FRED IDs, the compute date, the formula and the three-year ICE history limit. Real data, derived series only is stored (ICE redistribution terms).
- Legibility: three colored lines, end-of-line direct labels in the right margin, dashed H = 1 line noted, no collisions with the event label or the shaded negative zone.
- Embedding: after the "indictment of trailing windows" paragraph, which points to the figure.
- Fix: the body text said the CCC estimate "reached -0.66 by the window ending May 30"; the data give -0.668, which rounds to -0.67. Text changed to -0.67 (the figures log had judged -0.66 fine).
- Not fixed, for the orchestrator (outside figure scope; already in the figures log): the 2024 CCC and HY rows of the 8.2 Trend Watch (-0.22 / 0.61 and -0.34 / 0.65) do not reproduce on a fresh pull (-0.17 / 0.68 and -0.31 / 0.67). The figures log also says "794 daily rows"; the common-date count is 748 (747 changes, 688 rolling windows).

## Figure 8.5, ch08_thirty_seven_cents (Section 8.8): PASS after one caption fix
- Correctness: waterfall +3, -70, +28, +6, -4 steps from 0 to -37 and the total bar equals the running sum. Recomputed from the table: -4.1 x 0.0018 x 95 = -70 cents, 0.248 x 0.012 x 95 = +28, 0.248 x 0.0025 x 95 = +6. Connectors sit at 3, -67, -39, -33, -37. The bracket spans exactly the beta and IDO bars (28 + 6 = 34, Kaz's "alpha").
- Honesty: "Illustrative", with the bond's price, duration, OAS and the day's moves stated.
- Legibility: value labels clear of bars, bracket label does not touch the rates bar, diverging-ramp ends for gain and loss, tinted blues separate beta from IDO.
- Embedding: after "Theo's thirty-seven cents, answered" and its table, which points to the figure.
- Fix: caption said "itemized with the four subtractions", but carry and the residual are not among the four subtractions. Now "itemized as in the table above".

## Embedding check (all five)
Syntax `![Figure 8.n: ...](assets/figures/ch08_*.png)` matches the other chapters (build_book.sh rewrites the prefix). Numbers run 8.1 to 8.5 in order of appearance; each file exists; each figure follows the paragraph that introduces it; no other "Figure 8.x" text in the book points elsewhere.

## Files changed
- tools/figures/ch08.py (Fig 8.1 note wording; Fig 8.3 colors, estimator totals, assertion). PNGs regenerated: ch08_hedge_ratio_by_rating.png, ch08_stale_marks_beta.png (the other three are byte-identical on re-run).
- book_src/08_ch08_isolating_ido_and_empirical_duration.md: captions of Figures 8.1, 8.2, 8.3, 8.5 and one number (-0.66 to -0.67) in the Case Study C paragraph.
<!-- STATUS: COMPLETE -->
