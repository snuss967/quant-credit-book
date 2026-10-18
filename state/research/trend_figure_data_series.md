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
