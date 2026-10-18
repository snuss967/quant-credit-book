# Figure check: Chapter 6-B (ed2 U4, figure checker)

Chapter: book_src/06_ch06b_options_and_measures_for_credit.md. Script: tools/figures/ch06b.py. Figures log: COMPLETE. Style read from the docstring of tools/figures/style.py. All five PNGs viewed before and after the fixes (plus 3x crops of the tight spots); all are under 120 KB, 150 dpi (1050 x 480), white background, no in-image title, one y-axis, text in ink or muted ink. The script reruns in about 2.5 s and reproduced the committed PNGs byte for byte before my edits, so the images are a pure function of the script, which executes Listing 6-B.1 (Appendix F) unchanged.

Method for correctness: besides reading the drawing code, I recomputed every plotted headline number in a separate script that does not touch the listing (scipy only): gamma rent 9.19 / 2.52 / 1.22 cents a day (1 week / 3 months / 1 year), Merton bond delta 0.1195 and 0.3342 and gamma -0.00798 and -0.00910 at V = 100, unit recovery claim 0.04686, jump-put implied vol 101.1% and wing bound 78.53% at K/F0 = 0.2 (c = 1.6569), hazard 6.19%, xi 2.343, survival 94.0% and 86.5%, decomposition 371.3 / 498.7 / 280.0 = 1,150 bp, recovery-bet legs +5.91, -4.74, +1.18 (= 0.0619 x 19). All match the figures and captions.

Chapter-wide color roles (checked, accepted, and documented in the script header): physical P / 216 bp firm / diffusion only = BLUE (SERIES[0]); risk-neutral Q / CCC cousin / with jump = ORANGE (1); recovery premium = VIOLET (6); time to expiry = one-hue SEQ_BLUE ramp; P&L polarity = the ends of the diverging ramp. Slots 2 to 4 (aqua, yellow, magenta) are never used, so the low-contrast rule does not bite; a role keeps its color across the chapter, which is what "fixed order" is for (same convention as Chapters 4-B and 8).

## Figure 6-B.2, ch06b_gamma_rent (6-B.2.4): PASS after one label fix
- Correctness: left panel is (1/2) Gamma S^2 (0.40^2 - 0.30^2)/365 = S phi(d1) (sigma_r^2 - sigma_i^2) / (2 sigma_i sqrt(T) 365); peak at the strike, narrower and taller for short expiries (9.2 cents at one week against 1.2 at one year). Right panel: daily-hedged long call, 20,000 lognormal paths, 63 daily hedges, common random numbers; the mean rises monotonically with realized vol and is +0.02 at 30% (zero crossing at the implied vol), slope about 2.0 per 10 vol points, which equals the call's vega (19.8) x 0.10. The self-financing book starts at zero value (verified in the code).
- Honesty: caption says "Illustrative", states 30% implied, 4% rates, strike 100, 20,000 paths, three-month call, daily hedging. The 5th to 95th percentile band is labelled in the image.
- Legibility: the "1 year" dot and label sat on the crossing of the 1-year and 3-month curves (spot 122), so the label read as belonging to either curve. Moved to spot 67.5, where the 1-year curve stands alone; label clear of all curves in a 4x crop.
- Embedding: after the sentence "Figure 6-B.2 shows where the rent is earned...", directly under the gamma-rent equation. File exists.
- Script additions: asserts that mean P&L increases in realized vol and is within 0.15 of zero at 30%.

## Figure 6-B.3, ch06b_merton_bond_greeks (6-B.3.4): PASS
- Correctness: bond delta N(-d1) falls monotonically from 1 toward 0 for both firms; bond gamma -phi(d1)/(V sigma sqrt(T)) is negative at every V and deepest at V about 70 (below the face values 80 and 95). Dots at V = 100 read 0.12 / 0.33 and -0.0080 / -0.0091, matching the table in 6-B.3.4. Firm parameters (F = 80, vol 25%; F = 95, vol 40%, r = 4%, T = 1) match the worked example.
- Honesty: "Illustrative", names merton() of Listing 6-B.1 and the two firms.
- Legibility: legend in the empty upper right, value labels beside the dots (blue label above, orange below, matching the dot order), no clipping, gamma axis runs to -0.0245 so the minimum is visible.
- Embedding: after the "Three readings" paragraph, which ends "Figure 6-B.3 draws the bond delta and gamma rows of the table". 
- Script additions: asserts monotone delta in [0, 1] and negative gamma on the whole grid.
- Chapter fix (see below): the table's 0.120 for the 216 bp firm's bond delta is now 0.119.

## Figure 6-B.4, ch06b_jtd_put_floor_and_wing (6-B.5.5): PASS after one label fix
- Correctness: (6B.1) put/K flattens at the unit recovery claim e^{-rT}(1 - e^{-lambda T}) = 0.0469 as K -> 0 (jump curve never below it, asserted; both curves increase in K, asserted); the diffusion-only put per strike falls toward zero (clipped by the log axis below 1e-4). Right panel: implied vols inverted from (6B.1) prices, 101.1% at K/F0 = 0.2 (the chapter's "about 100%"), always above the (6B.3) bound (asserted at every strike drawn), bound 78.5% at 0.2 and falling to 0 at K = F0, crossing the 40% diffusion line near K/F0 = 0.47 as it should.
- Honesty: "Illustrative"; caption gives spot, vol, r, lambda, T and the functions used.
- Legibility: the in-panel label "floor: the unit recovery claim" ran into the diffusion curve (the curve touched "claim"). Now two lines, clear of the curve in a 3x crop. Leader line and annotation on the right are clean.
- Embedding: after the paragraph that ends "Figure 6-B.4 draws both, the floor ratio on the left and the wing with its bound on the right". 

## Figure 6-B.5, ch06b_halvorsen_two_measures (6-B.8, Step 4): PASS after one style fix
- Correctness: S^P(t) = e^{-0.0619 t}, S^Q(t) = e^{-0.145 t} = (S^P)^xi with xi = 2.34; one-year points 94.0% and 86.5%; both curves decreasing, Q below P everywhere. Waterfall 371 + 499 + 280 = 1,150 bp with correct floating bases and connectors; total bar equals the running sum (now asserted against the 115 bp input spread).
- Honesty: "Illustrative", fictional Halvorsen, numbers from spread_decomposition() of Listing 6-B.1; matches the 6-B.8 Step 4 table to the basis point.
- Style fix: the two curve labels were ink text floating at the right edge with no colored mark beside them, so the reader had to infer which curve was which. Replaced by a legend in the empty lower-left corner (colored line handles, ink text, hazard values kept). No collision with the 94.0% / 86.5% call-outs or the xi note.
- Embedding: after the Step 4 table and the paragraph ending "Figure 6-B.5 shows the two survival curves behind steps 1 to 3 and the decomposition as bars".

## Figure 6-B.6, ch06b_halvorsen_recovery_bet (6-B.8, Step 5): PASS after one legibility fix
- Correctness: payoff at default is R - 78 for the notes alone and R - 78 + 57 = R - 21 with 57 points of puts: zero at 21, +19 at 40 (checked on the plot). Waterfall: notes lambda_Q(78-21) - lambda_P(78-40) = +5.91, puts -(lambda_Q - lambda_P) x 57 = -4.74, net +1.18 = lambda_P x 19 (asserted); floating bars and connectors are placed at 5.9 / 1.2 correctly. Gain and loss use the diverging ramp ends, net the dark sequential blue.
- Honesty: "Illustrative", fictional Halvorsen; the caption states that the left panel is before carry and the put premium, which is true to the drawing.
- Legibility: the three-line x labels "expected loss" and "expected payout" nearly touched. Tick label size reduced to 8 pt; gap is now clear. "+19" label and event labels sit between the dashed lines without collision.
- Embedding: after the paragraph ending "Figure 6-B.6 shows the payoff at default and the cancellation of the hazard premium"; follows the Step 5 formulas.

## Chapter-level checks
- Numbering: text-art block "Figure 6-B.1" (6-B.1.4) is followed by embedded figures 6-B.2 to 6-B.6 in order (lines 176, 274, 390, 559, 569); every figure is introduced by a sentence naming it; captions follow the house form (claim, then "Illustrative: ..." with parameters). No real-data claim in any figure, so no external source is required; no real-event dates appear.
- Syntax: five embeds of the form ![Figure 6-B.N: ...](assets/figures/ch06b_*.png); all five files exist; no stray ch06b PNGs.

## Fixes made
1. tools/figures/ch06b.py: 1-year label moved off the curve crossing (6-B.2); floor label wrapped to two lines (6-B.4); legend with colored handles replaces floating curve labels (6-B.5); tick labels 8 pt (6-B.6); extra assertions (monotone mean P&L and zero crossing at implied vol, monotone bond delta, negative bond gamma, jump put above its floor and monotone in K, waterfall sum equals the input spread). Script re-run, four PNGs regenerated and re-viewed.
2. book_src/06_ch06b_options_and_measures_for_credit.md line 265: table entry "Bond delta, 216 bp firm" 0.120 -> 0.119. N(-d1) with d1 = 1.1776 is 0.11948 (independently recomputed), which rounds to 0.119, so 0.120 could not be reproduced by the listing; the figure and caption (0.12) agree with both. No other mention of 0.120 in the chapter.

## Not fixed (for the orchestrator)
- The capital-structure ladder "Figure 6-B.1" is still a text-art block. A computed PNG (call-spread ladder, fulcrum marked) named ch06b_cap_structure_ladder would keep the number 6-B.1; optional.
- tools/check_book.py flags the chapter with "!!" (11,300 words); length, not a figure issue.
- Note on the shared scratchpad: it contains a stray struct.py from another agent's session that shadows the standard library when python is started from that directory; run python there only with -I.
<!-- STATUS: COMPLETE -->
