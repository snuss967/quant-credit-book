# Figure check: Chapter 15 (Event-Driven M&A, Regulatory Spreads & Change-of-Control)

Checker: Edition 2 figure checker. Script: tools/figures/ch15.py (re-run end to end after the fixes, all five PNGs under 200 KB). House style read from tools/figures/style.py. All five PNGs viewed before and after the fixes.

## Figure 15.1, ch15_deal_clause_map.png (schematic): PASS after one fix
- Correctness: five clauses (1, 3, 4, 5, 6) hang on the "closes" branch, the special mandatory redemption (2) hangs on the abandoned and litigated-block branches, and the issuer's consent strip or defeasance points only at clause 1. This matches the table in Section 15.1.2 row by row (payoffs, forced flows, clause numbers).
- Honesty: caption says "Illustrative: schematic ... not data". Matches.
- Style: colors in fixed order (closes = BLUE, abandoned = ORANGE, block = AQUA), the AQUA mark is direct-labeled by its box, no title, no twin axis, text in ink.
- Fix: the smallest text was 6.8 to 7.0 pt. Raised to 7.4 to 7.6 pt (clause boxes, regulatory-clock box, issuer box, arrow note, footnote); re-viewed, no clipping or collisions. Footnote shortened so it does not crowd the "Litigated block" box.
- Embedding: syntax correct, file exists, number 15.1 first, placed after the paragraph on the issuer's counter-options.

## Figure 15.2, ch15_coupon_vintage_put.png: PASS after a caption fix
- Correctness: recomputed independently. Put intrinsic value max(101 - P_post, 0) is linear in the coupon, kinked at the break-even coupon c* (5.31% strategic, 8.33% LBO), flat at zero beyond it. Sponsor-LBO values at 1.85%, 5.00% and 6.875% are 24.05, 12.35 and 5.39, matching the chapter's grid (24.0, 12.3, 5.4); the figure labels read 24, 12, 5.
- Honesty: caption says "Illustrative: computed from the model of Section 15.2.2" with the parameters. Matches.
- Style: two series (BLUE, ORANGE), direct-labeled, one y-axis, no collisions.
- Fix: caption said "the 1.85% bond is worth about four times the 6.875% bond". The ratio is 4.5 (24.05 / 5.39) and it is the put, not the bond. Now reads "the put on the 1.85% bond is worth more than four times the put on the 6.875% bond".
- Embedding: correct; sits after the "aha number one" paragraph that cites it.
- OPEN ITEM for the chapter reviser (not changed here; the chapter prose is under revision by other agents): the strategic-buyer numbers in the Step 4 text and grid do not follow from the stated model (4.5 years, UST zero 4.4% + 60bp, y = 5.0%). Exact values: A = 3.98 (text says 4.08), c* = 5.3% (text says 5.2%), P_post = 87.2, 99.7, 107.2 (grid says 87.4, 100.3, 107.9). The LBO column, A = 3.71 and c* = 8.3% are right. The figure draws the exact model, so its strategic break-even sits at 5.3%.

## Figure 15.3, ch15_smr_gauge.png: PASS after a spacing fix
- Correctness: left panel is P0 = pi G_f + (1 - pi) P_close with G_f = 102.15 e^(-0.0115) = 100.98; three lines (103.0, 100.98, 99.0) meet at G_f when pi = 1, the slope changes sign either side of P_close = G_f, and the quoted 99.40 maps to 20% (99.396). Right panel is 0.10 / |P_close - G_f| capped at 100 pp; the worked example 0.10 / 1.98 = 5.05 pp; the shaded zone is |gap| < 0.10, where the error covers the whole probability range (chapter: "a few cents, report no information"). All agree with Section 15.4.2.
- Honesty: caption names the tranche, fail-leg value and the 0.10-point price error; "Illustrative". Matches.
- Style: lines BLUE, ORANGE and NEUTRAL, direct labels, two panels instead of two axes, text in ink or muted.
- Fix: moved the "Rates rose" label 5 pt lower (it sat within a few pixels of the blue line).
- Embedding: correct; after the worked-number paragraph.

## Figure 15.4, ch15_competing_risks_incidence.png: PASS (no change)
- Correctness: generator, covariates, coefficients, Weibull parameters and seed 11 are identical to synthetic_deal_cohort in Listing 15.4 (Appendix F, block 4); Aalen-Johansen, Nelson-Aalen and risk-table code match the listing; the sum identity F_c + F_a + F_b = 1 - S is asserted to 1e-12 on every run. Curves are monotone steps; the dashed 1 - exp(-Lambda_c) sits above the competing-risks closing curve, as theory requires. Run output at 1.47 years: closes 71.7, abandoned 14.4, block 9.2, all exits 95.2, shortcut 89.9; stopped where fewer than 20 deals remain at risk.
- Honesty: caption numbers (90%, 72%, 14%, 9%) match the run; "Illustrative", synthetic cohort, seed and stopping rule stated.
- Style: BLUE, ORANGE, AQUA in the chapter's fixed order; AQUA and the others are direct-labeled at the line ends; labels at the right do not collide; one y-axis.
- Embedding: correct; follows the cumulative-incidence identity it illustrates.

## Figure 15.5, ch15_wbd_timeline.png: PASS after a label and caption fix
- Correctness (real events): every date checked against the primary EDGAR filings fetched during this review. Jun 9 and Jun 16, 2025 (8-K of June 13, 2025: tender offers launched, requisite consents received); Dec 4, 2025 (Netflix merger agreement, 8-K filed Dec 5, 2025; the earlier "unverifiable" flag in the Edition 1 fact-check is now resolved); Jan 19, 2026 (amended and restated agreement, all cash, $27.75); Apr 23, 2026 (vote tallies match the brief); Jun 4, 2026 (term loans $13bn and EUR 1,717mm); Oct 6, 2026 (closing, $31.01666668). Jun 26, 2025 and Feb 27, 2026 come from the filings cited in the chapter and brief. Gap check: Jun 16, 2025 to Feb 27, 2026 is 8.4 months; to Oct 6, 2026 is 15.7 months ("sixteen").
- Fix 1: label "Sep 30, 2026: ticking fee starts" is imprecise. The 8-K defines the fee as $0.00277778 per calendar day elapsed after September 30, 2026 through the closing date (October 1 to 6 = six days). Label now reads "Sep 30, 2026: ticking fee accrues from the next day".
- Fix 2: caption now says the Netflix signing date is from the EDGAR 8-K filed December 5, 2025.
- Honesty: caption gives a source (WBD 8-Ks, EDGAR). Chapter prose says "early December 2025" for the Netflix signing; consistent with, and less precise than, the figure's verified Dec 4.
- Style: lanes BLUE, ORANGE, AQUA with a legend and a text label beside every dot; text in ink; no collisions or clipping; "8 months" arrow sits in the Feb 27 row.
- Embedding: correct; after the "Three suitors, one clock" paragraph.

## Embedding summary
All five use ![Figure 15.N: ...](assets/figures/ch15_*.png), all files exist, numbering 15.1 to 15.5 follows order of appearance (lines 56, 166, 344, 464, 540), and each image sits next to the paragraph that cites it. No other chapter references these figures.

## Files changed
- tools/figures/ch15.py (font sizes in Figure 15.1, label offset in 15.3, ticking-fee label in 15.5)
- assets/figures/ch15_deal_clause_map.png, ch15_smr_gauge.png, ch15_wbd_timeline.png (regenerated; the other two regenerated unchanged)
- book_src/15_ch15_event_driven_mna_and_coc.md (captions of Figures 15.2 and 15.5 only)

<!-- STATUS: COMPLETE -->
