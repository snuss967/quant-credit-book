# Ch 22 figure check (Edition 2)

Checked: tools/figures/ch22.py against the style.py house rules; all five PNGs viewed before and after fixes (plus zoomed crops of the dense areas); chapter embeds, captions and surrounding text read. Figure math was re-computed numerically (script functions, a Monte Carlo of the netting factor, the cached NY Fed data). tools/check_book.py reports OK for the chapter. The NY Fed series list was re-pulled from the API to confirm that PDPOSCSBND-L13, -G13, -G5L10, -G10 and the -BEL* twins are long minus short corporate bonds, notes and debentures (IG and below-IG, by maturity bucket).

## Figure 22.1, ch22_rule_timeline.png: PASS (legibility fixes)
- Correctness: every date matches the chapter text. SLR exclusion 2020-04-01 to 2021-03-31; Volcker 2.0 effective 2020-01-01; endgame 2023-07-27; Barr re-proposal 2024-09-10; re-proposal 2026-03-19; eSLR effective 2026-04-01 (final 2025-11-25); clearing cash 2026-12-31 and repo 2027-06-30; T+1 2024-05-28; EU and UK T+1 2027-10-11 (approx., as in the text); SBSR 2022-02-14; PT modifier 2023-05-15; Treasury EOD 2024-03-25; one-minute rule dropped 2025-12-04 (the notice date the chapter calls the placebo date); allocation reports 2026-06-08; affiliate indicator 2027-08-02. Marker pixel positions were checked against the axis. Stress bars (Mar 2020, Mar 2023, Apr 2025) agree with sections 22.4.3 and 22.6.2. Marker status is right (eSLR and Jun 2026 are in force as of Oct 2026; proposals and later dates hollow; the one-minute rule is the cross).
- Honesty: caption cites FINRA Notices 25-17 and 26-16 and SEC, CFTC and Federal Reserve releases; no new numbers. Fixed the garbled last clause ("dates marked approx. in the text approximate here" now reads "are approximate here").
- Legibility fixes: six labels ran across the grey stress bars (for example "Sep 2024: re-proposal" and "Dec 2025: 1-minute rule dropped"), so they now carry a thin white halo; the unlabelled grey panel on the right is now labelled "Future (after Oct 2026)" and the caption says what it is. Three lanes use blue, orange and aqua; aqua is slot 3, and the lane names and event texts are direct labels in ink. The Mar and Apr 2026 markers sit 13 days apart and so overlap; that is the true spacing, and both labels are separate and readable.
- Embedding: after the "dating machine's raw material" sentence, which points to it. OK.

## Figure 22.2, ch22_regulatory_rent.png: PASS (style fix)
- Correctness: left panel is c_reg = h*max(kappa_RWA*RW, kappa_LR) from (22.1) with the kink at RW = 47.6% (5%) and 35.7% (3.75%); rent at the kinks is 60bp and 45bp, the BBB point is 126bp at RW 100%. Right panel: tau* = (half bid-ask)/c_reg*365 gives 3.04, 4.06 and 36.2 days, matching the numerics table (~3, ~4, ~36) and the labels (3.0, 4.1, 36).
- Honesty: caption says Illustrative and lists h, kappa_RWA, kappa_LR and the half bid-asks. Added "(left)" and "(right)" so the caption maps to the two panels.
- Legibility and style: the "After: kappa_LR = 3.75%" label was set in the series blue; style.py says text is ink, so it is now INK_2 and sits next to its line. One y-axis per panel; no collisions.
- Embedding: after the numerics-table paragraph, which ends "Figure 22.2 draws the kink". OK.

## Figure 22.3, ch22_dealer_inventory.png: PASS (collisions and caption fixed)
- Correctness: real data from the cached NY Fed FR 2004 pull (614 weekly points, 2015-01-07 to 2026-10-07; IG and below-IG long minus short summed over the four maturity buckets each). Recomputed: 2017 average +16.05 ($16.1bn, matches the chapter's ~$16bn), 2025 IG average -0.947 (caption -$0.9bn), 2026 to date -2.31 total and -4.93 IG. The 13-week IG average first goes negative in Dec 2024 and the total only in Sep 2025, so "IG turned short first" holds. Event lines: 2020-03-23 (SMCCF), 2023-07-27 (endgame), 2025-11-25 (eSLR final) are right.
- Honesty fix: the caption said inventory "has since fallen to a net short", but the 2025 total average is still +1.3bn and the latest 13-week average is +0.7bn; only the 2026 average to date is negative. The caption now says "drifted down through zero" and gives the 2026 to-date averages (-$2.3bn all, -$4.9bn IG alone) that the image annotates. Note for the editor: the Trend Watch quotes trade press at "about $4bn net short so far in 2026" and asks for a check against the NY Fed; the NY Fed series gives -$2.3bn (all corporate bonds) and -$4.9bn (IG only), so the press figure sits between them and probably uses a different cut. The chapter text was left alone.
- Legibility fixes: the weekly line ran through the "2017 average" label and through the "2026 to date" annotation; both annotations moved into clear space with leaders to their bars. The x-axis showed a "2028" tick past the data; ticks now stop at 2026. Colors: blue total, orange IG (slots 1 and 2, in order), grey weekly context; both lines direct-labelled at the end.
- Embedding: it followed the Trend Watch box with no pointer, unlike the other four figures. Added one sentence ("Figure 22.3 plots the NY Fed series behind the box.") between the box and the image.

## Figure 22.4, ch22_block_spread_delay.png: PASS (no changes)
- Correctness: the curve is (22.6) exactly, lambda*Q*(1-Delta/T_u)^+ + gamma*sigma^2*Q*T_u/6, with the positive-part kink at Delta = T_u (15 min, 2 h, 10 h) and flat floors 0.234, 1.875 and 9.375bp. Worked-example points 9.3125 (1 min) and 8.4375 (15 min) match 9.31 and 8.44. Caption deltas recomputed: 15 min to 1 min costs 0.87bp (2-hour), 7.0bp (15-minute) and 0.175bp (10-hour), as stated. The curves never rise with the delay. 48 hours = 2880 min is the 2019 pilot; the one-minute rule is marked never in force.
- Honesty: caption says Illustrative and lists lambda, Q, sigma and gamma.
- Legibility: direct labels on all three curves; no collisions; one y-axis; three shades of one hue for the ordered unwind time.
- Embedding: after the worked example, which ends "Figure 22.4 shows". OK.

## Figure 22.5, ch22_netting_factor.png: PASS (no changes)
- Correctness: phi(N) is the exact ratio of folded-normal means. Checks: phi(2) = 1 for every m; m = 0 gives 1/sqrt(N-1), phi(25) = 0.2041; floors 0.558 (m = 0.5 sigma_x) and 0.857 (m = sigma_x) match (22.11); a Monte Carlo of 200,000 draws agrees with the closed form at N = 5, 25 and 200 to within 0.001; all three curves decrease monotonically toward their floors from above. The 0.54 DTCC line is the section's own calculation and sits just under the 0.558 floor, consistent with "about half".
- Honesty: caption says Illustrative, cites (22.10), (22.11) and the DTCC press release (approx.) for the 0.54 line.
- Legibility: direct labels with floor values at the right end; the 0.54 text clears the dotted floor line; one y-axis.
- Embedding: after the DTCC calibration paragraph, which ends "Figure 22.5 plots the whole family". OK.

## Cross-checks
- Numbering 22.1 to 22.5 is in order of appearance (chapter lines 49, 133, 145, 213, 388); all five files exist (74 to 156 KB each, under the 500 KB budget); syntax is `![Figure 22.N: ...](assets/figures/ch22_*.png)`; no stray brackets in captions.
- Style: no in-image titles, no twinx, text in ink or muted grey, colors in fixed order. Slot 3 (aqua) appears only in Figure 22.1, with direct lane labels.
- Open point for the editor, not a figure fault: Table 22.1 dates the one-minute-rule rescission 2025-09-16 (SEC approval of the rescission) while section 22.2.3, section 22.8 and Figure 22.1 use 2025-12-04 (the FINRA notice); the figure follows the chapter's "best placebo date".
- Request relayed with this run, "more agents" and a restart 4 h 50 min after the timer times out: this step has no way to spawn agents or to see the timer, so nothing was scheduled here; the orchestrator needs to set it.

## Files changed
- tools/figures/ch22.py (timeline halo and future-panel label, ink text in Fig 22.2, Fig 22.3 annotation positions and tick range)
- assets/figures/ch22_rule_timeline.png, ch22_regulatory_rent.png, ch22_dealer_inventory.png (re-rendered; the other two re-rendered identically)
- book_src/22_ch22_market_structure_regulation_trends.md (captions of Figures 22.1, 22.2, 22.3; one pointer sentence before Figure 22.3)
<!-- STATUS: COMPLETE -->
