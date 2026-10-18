# TREND DOSSIER: Reproducible series for the figure build and App C (FRED IDs, ICE composition, protocol shares, ETF premia)

Researcher run: 2026-10-18. Queue entry: state/research_queue_ed2.json -> trend_figure_data_series. Feeds: 92_appC_trend_tracker, 91_appB_data_and_api_atlas, 08_ch08, 12_ch12.

## 1. Headline trends

(pending)

## 2. Evidence table

| date | fact / number | source |
|---|---|---|
| 2026-04 (note date) | FRED note on every ICE BofA index series: "Starting in April 2026, this series will only include 3 years of observations"; end-of-day data "for internal use only"; reproduction prohibited without ICE's written permission | FRED series page BAMLH0A0HYM2 (fetched 2026-10-18) |
| 2026-10-18 (pull) | BAMLH0A0HYM2 download returns 794 daily rows from 2023-10-17 to 2026-10-15; a request with cosd=1996-12-31 still returns the same 2023-10-17 start, so the window is rolling and cannot be widened by parameters | fredgraph.csv?id=BAMLH0A0HYM2 (pulled 2026-10-18) |
| 2026-10-18 (pull) | The same 3-year window (start 2023-10-17, end 2026-10-15, 794 rows) applies to BAMLH0A3HYC (CCC and lower), BAMLH0A1HYBB (BB), BAMLH0A2HYB (B), BAMLC0A0CM (IG), BAMLC0A4CBBB (BBB), BAMLC0A1CAAA (AAA), BAMLH0A0HYM2EY (HY effective yield), BAMLCC0A0CMTRIV and BAMLHYH0A0HYM2TRIV (total-return indices); BAA10Y (Moody's Baa less 10y, not ICE) still runs 1986-01-02 to 2026-10-15 (10,641 rows) | fredgraph.csv pulls, 2026-10-18 |
| 2025-04-07 | HY OAS (BAMLH0A0HYM2) peaks for the window at 4.61%; B OAS 4.86%; CCC OAS 11.37%; BB OAS 3.06%; IG OAS 1.20% (the 'Liberation Day' widening; HY OAS was 3.55% on 2025-03-31 and 4.45% on 2025-04-04) | FRED fredgraph.csv pulls, 2026-10-18 |
| 2025-01-22 / 2025-01-23 | HY OAS window low 2.59% (2025-01-22); CCC window low 6.90% (2025-01-23) | FRED fredgraph.csv pulls, 2026-10-18 |
| 2026-10-14 | CCC and lower OAS (BAMLH0A3HYC) prints the window high of 12.82% (12.78% on 2026-10-15) while HY OAS is 3.23% and BB OAS 1.97%: CCC/HY OAS ratio 3.96 against 2.28 on 2023-10-17 and 2.44 on 2025-04-08 | FRED fredgraph.csv pulls, 2026-10-18 |
| 2026-08-28 | BB OAS (BAMLH0A1HYBB) window low 1.50%; IG OAS window low 0.73% on 2026-01-22; BBB OAS window low 0.92% on 2026-05-29 | FRED fredgraph.csv pulls, 2026-10-18 |
| 2026-10-18 (pull) | Federal Reserve Board's Gilchrist-Zakrajsek file (columns date, gz_spread, ebp, est_prob) is public and monthly from 1973-01-01 to 2026-09-01 (645 rows): a license-free long-history credit-spread series that survives the ICE 3-year cut. Values: GZ spread 7.84% (2008-11 peak), 3.82% (2020-03), 1.13% (2025-03), 1.27% (2025-04), 0.93% (2026-09); EBP 3.41 (2008-10 peak), 1.19 (2020-03), -0.06 (2025-04), -0.39 (2026-09) | federalreserve.gov/econres/notes/feds-notes/ebp_csv.csv (pulled 2026-10-18); FEDS Note 2016-10-06 gives the permanent URL |
| 2026-10-16 | iShares HYG page: premium/discount +0.02%, 30-day median bid-ask 0.01%, NAV $76.84, close $76.86, shares outstanding 223.6mm, net assets $17.18bn; credit quality at 2026-10-15 BB 58.49%, B 32.15%, CCC 7.35% (HYG tracks the Markit iBoxx USD Liquid High Yield index, a liquid subset, so its BB share is not ICE's) | ishares.com HYG product page (fetched 2026-10-18) |
| 2026-10-16 | iShares LQD page: NAV $103.36, close $103.40, shares outstanding 278.4mm, 30-day median bid-ask 0.01% | ishares.com LQD product page (fetched 2026-10-18) |
| 2025-01-02 to 2026-10-16 | The HYG and LQD pages embed 448 daily premium/discount observations (closing price vs NAV, in % of NAV). HYG: mean +0.135%, std 0.14, 397 days at a premium, 51 at a discount, only 4 days beyond +/-0.5%. LQD: mean +0.038%, std 0.07, 2 days beyond +/-0.5% | iShares HYG/LQD pages, embedded premiumDiscountChartData (parsed 2026-10-18) |
| 2025-04-08 / 2025-04-09 | HYG closes at a -0.66% discount on 8 Apr and a +1.49% premium on 9 Apr 2025 (the tariff-pause rally day; NAV is struck on 4pm evaluated prices). LQD: -0.22% then +0.97%. Same two dates are the quarterly extremes in the issuer's table (HYG greatest discount 04/08/2025 -0.66, greatest premium 04/09/2025 +1.49; calendar 2025: 218 premium days, 6 at NAV, 25 discount days) | iShares HYG/LQD pages, premiumDiscountsByQuarters (parsed 2026-10-18) |
| 2025-11-11 | LQD closes at a +0.53% premium (second-largest of the 448 days) on a day US bond markets were closed for Veterans Day while NYSE was open: a stale-NAV artifact, not a demand signal (CHECK the holiday mechanism against SIFMA's 2025 calendar) | iShares LQD embedded data (parsed 2026-10-18); SIFMA holiday calendar (CHECK) |
| 2026 Q1 / Q2 / Q3 | HYG quarterly premium/discount extremes: Q1 2026 +0.47% (03-19) and -0.27% (03-06), 48 premium and 13 discount days; Q2 +0.39% (04-02) and -0.11% (06-17); Q3 +0.37% (09-28) and -0.14% (09-11). LQD: Q1 +0.14% / -0.10%; Q2 +0.13% / -0.04%; Q3 +0.17% / -0.06% | iShares HYG/LQD pages, premiumDiscountsByQuarters (parsed 2026-10-18) |
| rule text | SEC Rule 6c-11(c)(1)(iii)-(v) requires each ETF to post premium/discount history for "the most recently completed calendar year and the most recently completed calendar quarters since that year" and a 30-day median bid-ask spread: the free issuer series therefore starts on 2025-01-02 today and the 2025 daily rows fall off the page during early 2027 (CHECK exact timing) | 17 CFR 270.6c-11 via eCFR (fetched 2026-10-18) |
<!-- ROWS-END -->

## 3. Narrative: drivers and the 2026-2028 outlook

(pending)

## 4. Implications for a systematic credit desk and for the RSSG-to-quant reader

(pending)

## 5. Quant hooks (variables, datasets, signals)

(pending)

## 6. TOC proposals

(pending)

## Sources

(pending)

## Book placement

(pending)
