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
| 2017-01 to 2026-09 | FINRA publishes 117 free monthly TRACE volume workbooks (cdn.finra.org/trace/volume/monthly/TRACE_Public_Monthly_Report_YYYY-MM.xlsx, 6-7 KB each, available "on the third business day following the end of the month"); all 117 downloaded and parsed this session. Rows by product (CORP, CONV, AGCY, ABS, MBS, TBA...) with columns Trades / Par Value ($mm) / Average Daily for ATS, Interdealer, Customer, Total | FINRA TRACE Monthly Volume Files and About TRACE Monthly Volume Reports (fetched 2026-10-18); CDN files |
| rule text | FINRA monthly-report definitions: volume is uncapped par in $mm; includes 144A; "ATS" counts the sell side of a trade executed on an ATS; "Interdealer" the sell side between FINRA members outside an ATS; "Dealer-to-Customer" all trades reported by a member against a non-member (excluding ATS trades with non-members). Platforms where dealers report RFQ trades with clients therefore show up as Customer, not ATS | FINRA About TRACE Monthly Volume Reports (fetched 2026-10-18) |
| 2026-09 | CORP: 3,019,506 trades, par $1,264.1bn, average daily par $60.2bn, average daily trades 143,786; ATS 7.4% of par and 15.4% of trades; interdealer 12.2% of par | FINRA TRACE_Public_Monthly_Report_2026-09.xlsx (parsed 2026-10-18) |
| 2017-01 | CORP: 1,158,450 trades, par $711.9bn, average daily par $35.6bn, average daily trades 57,923; ATS 2.2% of par and 16.8% of trades | FINRA TRACE_Public_Monthly_Report_2017-01.xlsx (parsed 2026-10-18) |
| 2017 to 2025 (annual) | TRACE CORP ATS share of par (computed from monthly files): 2.4% (2017), 2.8%, 3.6%, 4.3% (2020), 6.6% (2021), 5.3% (2022), 6.3%, 7.3% (2024), 7.0% (2025); 2026 through September 6.6%. ATS share of trades stays at 14-18% throughout because ATS prints are small. Customer share of par drifts from 83.5% (2017Q1) to 74.2% (2025Q4) while interdealer share rises from 14.2% to 18.5%. Quarterly series computed in the table in section 5 | FINRA monthly workbooks, author computation 2026-10-18 |
| 2017 to 2026 (annual) | TRACE CORP average daily par: $30.4bn (2017), $38.0bn (2020), $48.5bn (2024), $55.1bn (2025), $61.6bn (2026 Jan-Sep); average daily trades 52.9k (2017), 64.2k (2020), 123.2k (2024), 131.6k (2025), 135.0k (2026 Jan-Sep). The trade count steps from 73.5k (2022Q1) to 89.0k (2022Q2) while par is flat, so trade counts are not comparable across that step (CHECK cause: reporting change, not activity) | FINRA monthly workbooks, author computation 2026-10-18 |
| 2025-03 / 2025-04 | Largest month in the 117: March 2025 average daily par $77.2bn (3.58mm trades); April 2025 (tariff shock) $62.1bn, ATS share of par fell to 5.8% from 7.4% in March. 2020-03: $48.2bn, ATS 2.8% | FINRA monthly workbooks, author computation 2026-10-18 |
| 2026-07-07 (file date) | MarketAxess publishes a free Excel workbook at investor.marketaxess.com/volume (MKTX-Monthly-Volume-Release-Website-File-06-2026-New-View.xlsx; seven tabs: monthly, quarterly and annual for MKTX and for market volumes, plus Disclosure) with 102 monthly columns, 2018-01 to 2026-06, giving volume by product (US HG, US HY, EM, Eurobonds, Rates), "Open Trading percentage of credit volume", and FINRA-reported US HG and HY TRACE capped volumes; it is the only free source that lines platform volume up against TRACE | investor.marketaxess.com/volume; workbook downloaded and parsed 2026-10-18 |
| 1Q18 to 2Q26 | MarketAxess Open Trading (all-to-all) percentage of credit volume, quarterly: 19% (1Q18), 29% (4Q18), 33% (1Q20), 37% (4Q20), 35% (1Q21), 38% (4Q22), 34% (2Q23), 34% (1Q24), 35% (4Q24), 36% (2Q25), 39% (4Q25), 38% (1Q26 and 2Q26). The series is recast retrospectively to exclude products where Open Trading is not offered (EM local, portfolio trading) | MarketAxess workbook, tab MKTX - Quarter, footnote 4 (parsed 2026-10-18) |
| 1Q18 to 2Q26 | Ratio of MarketAxess US HG ADV to FINRA-reported HG TRACE ADV (workbook rows, computed): 18.0% (1Q18), 22.8% (4Q20), 21.1% (4Q22), 19.3% (1Q24), 18.4% (4Q25), 17.1% (1Q26), 16.4% (2Q26); HY: 8.2% (1Q18), 17.1% (4Q20), 20.5% (4Q22), 12.9% (1Q24), 13.3% (4Q25), 12.1% (2Q26). These ratios run 0.4 to 1.1pp below the company-reported "estimated market share" (e.g. 2Q26 HG 17.5%; CHECK the definitional gap before plotting) | MarketAxess workbook, author computation 2026-10-18 |
| 2021-07-26 | FINRA corrected its monthly volume reports for ATS trades double-reported on TRACE; MarketAxess estimates the correction cut reported TRACE volume by 2.5% (HG) and 2.5% (HY) for the 18 months to June 2021 and that "estimated TRACE ATS reported corporate volume would have been approximately 35% lower" | MarketAxess workbook, Disclosure tab (parsed 2026-10-18) |
| 2026-03 | MarketAxess estimates duplicate affiliate back-to-back reports raised monthly TRACE volume by up to 9% for US HG and up to 3% for HY in March 2026 (its HG share would be up to 190bp higher, HY up to 50bp), and says FINRA's agenda (Feb 2026) expected an SEC rule filing in Q2 2026 to suppress them | MarketAxess workbook, Disclosure tab footnote 1 (parsed 2026-10-18) |
| 2025-01 | MarketAxess January 2025 release: Open Trading share of credit volume 34% (36% Dec 2024); PT ADV $0.9bn with 77% executed on X-Pro; "Portfolio trading represented approximately 9% of U.S. high-grade and U.S. high-yield TRACE in January 2025, down from 13% in December 2024"; MarketAxess PT share of TRACE PT volume 14.7% (16.7% Dec 2024); record Dealer RFQ ADV $1.5bn | MarketAxess volume release, 2025-02-05 (PDF fetched 2026-10-18) |
| 2025 FY | Morgan Stanley (via The DESK, 2026-02-19): capped US PT volume about $1.3tn in 2025 (+52%), PT 15% of corporate bond trading in 2025 against 11% in 2024, peak 17% in July 2025, 16% at end-2025; uncapped estimate about $1.8tn from $1.1tn; IG PT $1.1tn (+44%); HY PT +116%, record $56bn in Q4 2025, 18% of HY trading in December 2025 and 16% for the year | The DESK, "IG credit sees portfolio trading plateau while HY hits records" (2026-02-19) |
| 2026 Q2 | Tradeweb Q2 2026: 19.0% share of fully electronic US HG TRACE (+101bp YoY) and 25.7% total HG share (-29bp); 8.5% fully electronic HY (+32bp) and 11.1% total HY (+44bp); US HG fully electronic ADV $8,672mm (+18.8%), HY fully electronic $1,202mm (+8.1%), European credit ADV $3,163mm (+23.4%); credit derivatives ADV +19.6% on "hedge fund and systematic account activity" | Tradeweb 8-K Ex-99.1 filed 2026-07-30 (tw-2026xq2xex991.htm, fetched 2026-10-18) |
| 2023-05-15 | FINRA TRACE Fact Book 2025 (Feb 2026 PDF) timeline: portfolio-trade modifier effective 2023-05-15; Treasuries reportable from 2017-07-10; 144A dissemination from 2014-06-30. The Fact Book PDF is an index of online tables and does not carry a portfolio-trade share | FINRA TRACE Fact Book 2025 (PDF fetched 2026-10-18) |
| 4Q22 to 2Q26 | Tradeweb share of fully electronic US HG TRACE, as first reported each quarter: 14.4% (4Q22), 13.3% (1Q23), 14.9% (2Q23), 16.6% (3Q23), 17.2% (4Q23), 17.6% (1Q24), 18.8% (2Q24), 17.7% (3Q24), 18.3% (4Q24), 18.0% (1Q25), 17.9% (2Q25), 18.6% (3Q25), 18.3% (4Q25), 17.7% (1Q26), 19.0% (2Q26); full-year 2023 HG 15.5%. The HG share has been flat in an 18-19% band for nine quarters | Tradeweb quarterly 8-K Ex-99.1, filings dated 2023-02-02 through 2026-07-30 (fifteen exhibits fetched and parsed 2026-10-18) |
| 1Q22 to 2Q26 | Tradeweb share of fully electronic US HY TRACE: 7.1% (1Q22), 6.1% (1Q23), 6.2% (2Q23), 7.8% (3Q23), 6.7% (4Q23), 6.7% (1Q24), 7.6% (2Q24), 7.8% (3Q24), 7.9% (4Q24), 7.5% (1Q25), 8.2% (2Q25), 7.5% (3Q25), 8.1% (4Q25), 7.4% (1Q26), 8.5% (2Q26). Total (including electronically processed) share since 2025: HG 25.9 / 26.0 / 26.2 / 25.7 / 25.0 / 25.7% and HY 10.1 / 10.7 / 9.8 / 10.0 / 9.8 / 11.1% for 1Q25 to 2Q26 | Tradeweb quarterly 8-K Ex-99.1 (parsed 2026-10-18); 2Q25 restated by about 10bp in the 2Q26 release (CHECK) |
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
