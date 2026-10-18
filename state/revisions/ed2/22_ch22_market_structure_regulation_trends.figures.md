# Ch 22 figures log (Edition 2, task U4)

Script: tools/figures/ch22.py (run `python3 tools/figures/ch22.py`; writes assets/figures/ch22_*.png).
Cached real data: tools/figures/data/ch22_nyfed_pd_corp_bond_net.csv (delete to re-download from the NY Fed API).
Note: no brief (section 3) and no state/research/trend_figure_data_series.md existed for this chapter; figures were chosen from the chapter's own headings, equations and case studies. trend_market_structure_regulation.md is an empty skeleton.

## Embedded

1. **ch22_rule_timeline** (Figure 22.1, section 22.1, after the "two machines" paragraph). Three-lane timeline 2018-2030 of dated rule changes on the three inputs a dealer sells (balance sheet, time, information); markers distinguish in force / proposed-adopted-scheduled / approved-never-in-force; grey bars mark the Mar 2020, Mar 2023 and Apr 2025 stresses. Data: dates quoted in sections 22.2-22.6 and Table 22.1 (FINRA Notices 25-17, 26-16; SEC/CFTC/Fed releases). Not new numbers.
2. **ch22_regulatory_rent** (Figure 22.2, section 22.1.1, after the numerics-table paragraph). Left: rent c_reg = h*max(kappa_RWA*RW, kappa_LR) vs equivalent risk weight, before and after 2026-04-01, with switching points 47.6% and 35.7% and the 126bp BBB point. Right: breakeven holding period (22.4) of 3.0, 4.1 and 36 days. Illustrative: h = 12%, kappa_RWA = 10.5%, kappa_LR = 5% then 3.75%, half bid-ask 0.5bp / 12.5bp (chapter numerics table).
3. **ch22_dealer_inventory** (Figure 22.3, section 22.1, after the Trend Watch on dealer corporate-bond inventories). REAL DATA: US primary dealers' net (long minus short) corporate-bond positions, IG and below-IG bonds, all maturities, weekly 2015-01-07 to 2026-10-07, with 13-week averages, IG only, the 2017 average (+$16.1bn, matches the chapter's ~$16bn), the 2026 year-to-date average (-$2.3bn total, -$4.9bn IG only) and event lines for Mar 2020 (SMCCF, SLR exclusion), the Jul 2023 endgame proposal and the Nov 2025 eSLR final. Source: NY Fed Primary Dealer Statistics (FR 2004), series PDPOSCSBND-L13, -G13, -G5L10, -G10, -BELL13, -BELG13, -BELG5L10, -BELG10 (https://markets.newyorkfed.org/api/pd/get/<series>.json).
4. **ch22_block_spread_delay** (Figure 22.4, section 22.2.1, after the worked example). Competitive block half-spread (22.6) vs reporting delay (log scale) for unwind times of 15 min, 2 h and 10 h, with the 1-minute-rule, today's 15-minute and 2019-pilot 48-hour delays marked and the worked-example points (9.31bp, 8.44bp). Illustrative: eq. (22.6) with lambda = 0.5bp per $mm, Q = $15mm, sigma = 2.5bp per sqrt(min), gamma = 0.001.
5. **ch22_netting_factor** (Figure 22.5, section 22.4.1, after the DTCC calibration paragraph). Exact netting factor phi(N) of (22.10)-(22.11) for N from 2 to 200 at common components m = 0, 0.5 sigma_x and sigma_x, with the floors 0.558 and 0.857, the 0.204-at-N=25 point and the DTCC Sponsored Service reading (about 0.54). Illustrative closed forms; the 0.54 marker is the chapter's calculation from DTCC's press release (approx.).

## Considered, not drawn (cap of five)
T+1 square-root margin bracket (22.8); Pareto tail behind 5MM+ (22.7); dealer-capacity hinge (22.13); March 2020 price path (FRED BAA10Y and DGS10 are available; the ICE BofA OAS series on FRED covers only the last three years); CDS index-to-single-name multiple (four published points only).

## Chapter edits
Five insertions only (one per figure, each with a blank line before and after); four of them append one short pointer sentence to the preceding paragraph (Figures 22.1, 22.2, 22.4, 22.5); Figure 22.3 follows the Trend Watch box with none.
<!-- STATUS: COMPLETE -->
