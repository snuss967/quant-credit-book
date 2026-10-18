# Ch 23 figure check (Edition 2)

Script: tools/figures/ch23.py. Chapter: book_src/23_ch23_cross_asset_convexity_and_vol_surface.md. All five figures are Illustrative (closed forms of the chapter); no real-data series is claimed. I re-computed the quoted numbers from the script's own pricing functions: Merton table (46/73/117% equity vol, 0.8/80/626bp), CreditGrades time-zero mass (24.96% at $5, 1.3e-4 at $30), JTD implied vols (36/41/52/72/102%), floors (2.4/4.7/9.2%), 24-cent put, bank path (43, 41.58, 1.42, 31.42, 77.75, -46.33) and Merton PD 0.36%. All match the captions and the text. Monotonicity checked numerically: sigma_E and the Merton spread both rise as V falls; every CreditGrades survival curve is non-increasing in t.

## Figure 23.1 (ch23_waterfall_call_spreads): PASS after fixes
- Correctness: stack of call spreads kinks at 40, 55, 70 and its top edge is the 45-degree line; equity is the open call at F = 70. Lognormal risk-neutral density (drift r - sigma^2/2) is right; interval probabilities 4/28/37/31% sum to 100%; V0 = 62 lies in the unsecured interval.
- Fixed (legibility): the dashed V0 line ran through the "37%" label and "28%"/"37%" nearly touched. The line now stops under the header strip, the strip names each claim ("1st lien", "2nd lien", "Unsecured", "Equity") so the aqua band is direct-labelled in the right panel too, and the explanatory note moved from MUTED 7.5 pt to INK_2 8 pt. Left-panel labels renamed "1st lien"/"2nd lien" to match.
- Fixed (caption): "Each claim's payoff is a call spread" was loose, since equity is a plain call. Now "Each debt claim pays a call spread on firm value and equity pays the call struck at total debt".
- Embedding: placed after the paragraph that ends "Figure 23.1 draws the stack."; file exists.

## Figure 23.2 (ch23_leverage_skew): PASS, no changes
- Correct (see numbers above), two panels so one y-axis each, log axis labelled, direct labels on the marked points, text in ink. Caption matches. Placed after Consequence 2, which ends "Figure 23.2 plots both consequences."

## Figure 23.3 (ch23_creditgrades_ghost): PASS after fixes
- Correctness: survival formula matches the CreditGrades (23.3) barrier form, with the time-zero mass included in the protection leg. Curves are upward-sloping ($30), flat ($15) and inverted ($5), as the caption says.
- Fixed (honesty): the in-image note and the caption said "25% of the default probability is booked at t = 0". That is wrong: the model books a 25% default probability at t = 0 (about two thirds of the five-year total). Image note and caption reworded.
- Fixed (legibility): the "$15" and "$30" end labels on the spread panel touched (now offset 4 pt apart), and the longer left-panel note would have crossed the $15 curve (now shortened and placed between the $15 and $5 curves).
- Embedding: after the sentence "Figure 23.3 shows the survival curve and the spread curves it produces."

## Figure 23.4 (ch23_jtd_skew_floor): PASS after fixes
- Correctness: JTD put (23.8) gives a flat P(K)/K floor at e^{-rT}(1 - e^{-lambda T}); the pure diffusion goes to zero; implied-vol wing climbs toward 102% at K/S0 = 0.2; the 30% no-jump line is shown.
- Fixed (clipping): the lambda = 10% curve (15.4% at K/S0 = 1) left the top of the right panel; ylim raised from 14 to 16.5.
- Fixed (embedding): the figure had no pointer in the text. Added to the lead-in of the three readings: "Three readings follow, and Figure 23.4 draws the first two." The figure sits right after the list. Caption unchanged and accurate.

## Figure 23.5 (ch23_bank_run_runway): PASS after fix
- Correctness: waterfall replays bank_run_dd (kappa 0.42, rho 2.0, 10% haircut, $30bn/day). Default on day 2 is asserted in the script. Run rates 25.2% and 63.0% match the caption; Merton PD 0.36% shown as 0.4%.
- Fixed (sums): bars were labelled in whole bn (31, -78, -46 and 43, -42, 1.4), so the visible arithmetic did not add up (31 - 78 is not -46). Labels now carry exact two-decimal values where non-integer (13 + 30 = 43; 43 - 41.58 = 1.42; 1.42 + 30 = 31.42; 31.42 - 77.75 = -46.33). Caption and text round to $1.4bn, $42bn, $31bn, $78bn, which is consistent.
- Style note, left as is: blue and orange here mean "securities sold" and "deposits leaving" (explicit legend), not first and second lien as in Fig. 23.1; red is a STATUS color paired with the text label "Shortfall: default".
- Embedding: after the worked example, which ends "Figure 23.5 lays out the two days."

## Open items for the chapter editor (body text, not touched by this check)
1. Section 23.4, reading 1: "Black-Scholes at 30% vol prices it at about 10^{-11} dollars". The computed Black-Scholes price of the $5-strike put on $100 at 30% vol, 1 year, r = 3% is 2.0e-24 dollars (Figure 23.4 right panel shows it going to zero). Suggest "about $10^{-24}$ dollars" or "a rounding error".
2. Section 23.2, "Ways This Blows Up", time-zero ghost: "makes the curve too flat". For S0 = $5 the model curve is strongly inverted (about 8,300bp at 3 months, 4,300bp at 6 months, 690bp at 5 years), as Figure 23.3 shows. Suggest "inflates short-tenor spreads and inverts the curve".

## Summary of edits
- tools/figures/ch23.py: Fig 1 strip/labels, Fig 3 note and label offsets, Fig 4 ylim, Fig 5 label precision; all five PNGs regenerated and re-viewed (all under 105 KB).
- Chapter: captions of Figures 23.1 and 23.3 reworded; one pointer clause added before the three readings in 23.4.
<!-- STATUS: COMPLETE -->
