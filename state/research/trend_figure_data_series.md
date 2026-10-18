# TREND DOSSIER: Reproducible series for the figure build and App C (FRED IDs, ICE composition, protocol shares, ETF premia)

Researcher run: 2026-10-18. Queue entry: state/research_queue_ed2.json -> trend_figure_data_series. Feeds: 92_appC_trend_tracker, 91_appB_data_and_api_atlas, 08_ch08, 12_ch12.

## 1. Headline trends

Six movements matter for the figure build and for Appendix C. Each is stated with the number that a caption can carry; section 2 holds the sourcing.

1. **The free window is closing from behind.** Since April 2026 every ICE BofA series on FRED holds only the latest three years (2023-10-17 to 2026-10-15 today, 794 rows). It rolls daily, so the 2022 rates shock is already gone, the April 2025 tariff peak (HY OAS 4.61% on 7 April 2025) leaves in April 2028, and FRED's own note calls the data "internal use only". Any figure that needs more must be frozen from a local archive now, and its right to be printed is an open licensing question (CHECK with counsel).
2. **The long axis moved to public-sector data.** The Federal Reserve Board's Gilchrist-Zakrajsek file runs monthly from 1973-01 to 2026-09, Moody's Baa-less-10-year spread runs from 1986 on FRED, the Fed's May 2026 Financial Stability Report publishes loan-spread and private-credit tables, and FINRA posts 117 free monthly TRACE volume workbooks (2017-01 to 2026-09). ICE supplies the fine, short series; the Fed and FINRA supply the long, coarse ones.
3. **The index under the spread changed composition.** BB was 53.55% of ICE HY market value on 17 April 2025 against a 44.53% average since 1996. A regression on FRED total returns puts it near 60% in October 2026 and CCC near 8%. At December 2024 weights, the 15 October 2026 HY OAS would be about 377bp rather than 323bp: roughly 54bp of the headline tightness is mix.
4. **TRACE cannot see protocols, so "protocol share" is assembled from three vantage points.** TRACE has capacity, an ATS flag (2.4% of corporate par in 2017, 7.3% in 2024) and, since 15 May 2023, a portfolio-trade modifier. RFQ, all-to-all and streaming shares come from platform filings: MarketAxess Open Trading 19% (1Q18) to 38% (2Q26) of its own credit volume, Tradeweb fully electronic HG TRACE share inside a 17.7-19.0% band for nine quarters, and portfolio trading 11% to 15% of corporate volume (Morgan Stanley, 2024 to 2025).
5. **An ETF premium is mostly a clock error.** Over 448 days the HYG premium averaged +0.135% and LQD +0.038%; the extremes fall on 8-9 April 2025 (HYG -0.66% then +1.49%) and on days the bond market was shut while NYSE was open. The free issuer history begins 2025-01-02 and will shed its 2025 rows in early 2027.
6. **The measurement keeps breaking.** FINRA corrected ATS double-reporting in July 2021, duplicate affiliate reports inflated March 2026 HG TRACE volume by up to 9%, and on 30 July 2026 MarketAxess stopped its monthly volume releases when ICE agreed to acquire it. The last free platform-versus-TRACE workbook ends in June 2026.

## 2. Evidence table

| date | fact / number | source |
|---|---|---|
| 2026-04 (note) | Every ICE BofA series on FRED carries: "Starting in April 2026, this series will only include 3 years of observations"; data "for internal use only"; reproduction needs ICE's written permission | FRED page BAMLH0A0HYM2 |
| 2026-10-18 | BAMLH0A0HYM2 pull returns 794 daily rows, 2023-10-17 to 2026-10-15; `cosd=1996-12-31` and `vintage_date` change nothing, so the window rolls and cannot be widened by parameter | fredgraph.csv, pulled 2026-10-18 |
| 2026-10-18 | The same window binds CCC (BAMLH0A3HYC), BB (BAMLH0A1HYBB), B (BAMLH0A2HYB), IG (BAMLC0A0CM), BBB (BAMLC0A4CBBB), HY yield (BAMLH0A0HYM2EY) and the total-return indices (BAMLHYH0A0HYM2TRIV, ...A1BBTRIV, ...A2BTRIV, ...A3CMTRIV, BAMLCC0A0CMTRIV). Not bound: BAA10Y (1986-01-02), DGS10 (1962), DGS2 (1976), VIXCLS (1990) | fredgraph.csv pulls |
| 2026-10-18 | Gotchas tested: a multi-series request applies `cosd` to the first series only; the guessed ID BAMLH0A0HYM2TRIV returns an HTML 404 that `pd.read_csv` would try to parse; the FRED API returns HTTP 400 without a key | FRED requests |
| 2025-04-07 | Window peak: HY OAS 4.61%, B 4.86%, CCC 11.37%, BB 3.06%, IG 1.20% (HY was 3.55% on 2025-03-31 and 4.45% on 04-04) | FRED pulls |
| 2025-01-22/23 | Window lows: HY 2.59% (01-22), CCC 6.90% (01-23); later lows BB 1.50% (2026-08-28), IG 0.73% (2026-01-22) | FRED pulls |
| 2026-10-14 | CCC OAS hits its window high 12.82% (12.78% on 10-15, when HY is 3.23% and BB 1.97%): the CCC/HY ratio on 10-15 is 3.96, against 2.28 on 2023-10-17 and 2.44 on 2025-04-08 | FRED pulls |
| 2026-09 | Fed Board file `ebp_csv.csv` (date, gz_spread, ebp, est_prob): 645 monthly rows, 1973-01 to 2026-09, license-free. GZ spread 7.84% (2008-11), 3.82% (2020-03), 1.27% (2025-04), 0.93% (2026-09); EBP 3.41 (2008-10), -0.39 (2026-09) | federalreserve.gov, pulled 2026-10-18 |
| 2026-05 | Fed Financial Stability Report accessible tables publish data for Fig 1.9 (EBP to 2026-03), Fig 1.10 (leveraged-loan discounted spreads, B and BB, monthly from 1997, weekly 2013-11-22 to 2026-04-17; PitchBook LCD) and Figs A, B (private credit). Figs 1.7-1.8 (ICE BBB and HY yields and OAS) have no data table | Fed FSR May 2026 |
| 2020-03-20 | Fig 1.10 weekly loan spreads, B / BB: 9.69% / 7.88% (series high), 4.44% / 2.85% (2025-04-04), 3.99% / 2.35% (2026-04-17); CHECK column mapping before use | Fed FSR Fig 1.10 |
| 2012-2025 | Private credit $217bn (2012), $1,262bn (2024), $1,449bn (2025); 12.7% to 33.8% of below-IG debt; semi-liquid funds $8.7bn (2020) to $237.7bn (2025), 20.4% of private credit | Fed FSR Figs A, B |
| 2020-03-23 | BAA10Y (full history): 2.05% (2020-02-20), 4.31% peak (2020-03-23), 6.16% (2008-12-04), 1.44% (2026-10-15). DGS10: 1.52, 0.76, 0.66% on 2020-02-20, 03-23, 06-30; 3.88% (2022-12-30); 5.10% (2026-10-15) | FRED pulls |
| 2025-04-08 | VIX closes 46.98 (04-07) and 52.33 (04-08), 16.46 on 2026-10-15; HY OAS peaked 04-07, one day before VIX | FRED VIXCLS |
| 2026 page | FINRA enhanced historical TRACE (corporates) lags 6 months, published quarterly, under a paid agreement; academic product (masked dealers) lags 36 months | FINRA historic data page |
| 2025-12-11 | Open Source Bond Asset Pricing: trace-data-pipeline Stage 1 in public beta; daily and monthly data via WRDS; ML panel 2002-07 to 2022-12, 341 predictors | openbondassetpricing.com |
| 2025-04-17 | BB share of ICE HY market value 53.55% against a 44.53% average for 1996-2024; face value $1.4tn, unchanged in ten years; OAS 1,087bp on 2020-03-23, 2,147bp in 2008-09 | Fridson, CFA Institute, 2025-06-02 |
| 2021-09 | BB share all-time high 54.30% (search snippet only; PitchBook returned 403) CHECK | PitchBook snippet |
| 2004; YE2024 | Nuveen: HY index 37% BB in 2004, 51% at YE2024; index not named in the extract CHECK (Nuveen uses Bloomberg HY on p.9) | shelf: Nuveen pp.4, 9 |
| 2024-04 to 2026-10 | Implied ICE HY weights BB/B/CCC from a 126-day constrained regression of HY on bucket total returns: 49.3/39.4/11.4 (Apr 2024), 53.4/34.0/12.6 (Dec 2024), 53.8/34.5/11.6 (Apr 2025, against Fridson's actual 53.55), 55.4/34.3/10.3 (Dec 2025), 60.1/31.8/8.1 (15 Oct 2026). Standard errors about 0.2pp; the OAS identity reproduces HY OAS within 1-7bp | author computation, FRED TR series |
| 2024-04 to 2026-10 | Implied ICE IG weights AAA/AA/A/BBB, same method: 1.1/8.5/43.0/47.4 (Apr 2024) to 0.8/9.2/45.9/44.1 (Oct 2026); AAA and AA noisy, A and BBB stable | author computation |
| 2026-10-15 | HYG (Markit iBoxx, not ICE) credit quality BB 58.49%, B 32.15%, CCC 7.35%; net assets $17.18bn; premium/discount +0.02%; 30-day median bid-ask 0.01% | iShares HYG page |
| 2025-01-02 to 2026-10-16 | The iShares pages embed 448 daily premium/discount rows. HYG: mean +0.135%, sd 0.14, 51 discount days, 4 beyond +/-0.5%. LQD: mean +0.038%, sd 0.07, 103 discount days, 2 beyond +/-0.5% | iShares HYG, LQD pages |
| 2025-04-08/09 | HYG closes -0.66% then +1.49% to NAV; LQD -0.22% then +0.97%; these are the 2025 extremes in the issuer table (HYG 218 premium, 6 at-NAV, 25 discount days in 2025) | iShares pages |
| 2025-10-13; 11-11; 2026-10-12 | On bond-market holidays with NYSE open the premium jumps: HYG +0.40/+0.44/+0.28, LQD +0.11/+0.53/+0.18 (means +0.37/+0.27 against +0.135/+0.038), a stale-NAV artifact. MarketAxess's SIFMA count has 18 US days in Nov 2025 against 19 NYSE days | iShares pages; MarketAxess workbook |
| 2026 Q1-Q3 | HYG quarterly premium/discount extremes +0.47/-0.27 (Q1), +0.39/-0.11 (Q2), +0.37/-0.14 (Q3); LQD +0.14/-0.10, +0.13/-0.04, +0.17/-0.06 | iShares premiumDiscountsByQuarters |
| rule text | Rule 6c-11(c)(1)(iii)-(v): premium/discount for "the most recently completed calendar year and the most recently completed calendar quarters since that year", plus a 30-day median bid-ask; the 2025 daily rows should leave the page in early 2027 (CHECK timing) | 17 CFR 270.6c-11, eCFR |
| 2017-01 to 2026-09 | FINRA posts 117 monthly TRACE workbooks (par in $mm, 144A included). ATS = sell side executed on an ATS; Interdealer = sell side between members off-ATS; Customer = member against non-member (ATS trades with non-members excluded). RFQ trades that dealers report against clients therefore land in Customer | FINRA About TRACE Monthly Volume Reports |
| 2017-01 and 2026-09 | CORP par/day $35.6bn to $60.2bn; trades/day 57.9k to 143.8k; ATS share of par 2.2% to 7.4%, of trades 16.8% to 15.4% (Sep 2026: $1,264bn par, 3.02mm trades) | FINRA workbooks, computed |
| 2017-2026 annual | ATS share of par 2.4% (2017), 4.3% (2020), 6.6% (2021), 5.3% (2022), 7.3% (2024), 7.0% (2025), 6.6% (2026 YTD); par/day $30.4bn (2017), $55.1bn (2025); customer share of par 83.5% (2017Q1) to 74.2% (2025Q4) | FINRA workbooks, computed |
| 2022 | Trades/day ramp 56.9k (Dec 2021) to 96.0k (Jun 2022) while par/day stays $37-39bn, so average size falls about $0.45mm to $0.40mm (CHECK cause); March 2025 is the peak month at $77.2bn par/day, April 2025 $62.1bn with ATS share down to 5.8% from 7.4% | FINRA workbooks, computed |
| 1Q18-2Q26 | MarketAxess workbook (102 months, 2018-01 to 2026-06): Open Trading share of credit volume 19% (1Q18), 29% (4Q18), 37% (4Q20), 38% (4Q22), 34% (1Q24), 36% (2Q25), 39% (4Q25), 38% (1Q26, 2Q26); recast to products where Open Trading is offered | MarketAxess investor site |
| 1Q18-2Q26 | MarketAxess ADV over FINRA HG TRACE ADV (workbook rows): 18.0% (1Q18), 22.8% (4Q20), 19.3% (1Q24), 16.4% (2Q26); HY 8.2%, 17.1%, 12.9%, 12.1%; 0.4-1.1pp below the company's reported shares (2Q26 HG 17.5%) CHECK | MarketAxess workbook, computed |
| 2021-07-26 | FINRA corrected monthly volumes for ATS trades double-reported; MarketAxess estimates a 2.5% cut in HG and HY TRACE totals (18 months to June 2021) and ATS corporate volume "approximately 35% lower" | MarketAxess workbook, Disclosure |
| 2026-03 | Duplicate affiliate back-to-back reports raised TRACE volume up to 9% (HG) and 3% (HY); FINRA rule filing expected Q2 2026 | MarketAxess workbook, Disclosure |
| 2026-07-30 | MarketAxess 8-K: ICE to acquire MarketAxess; monthly volume press releases suspended, guidance withdrawn; the last free workbook covers June 2026 | MarketAxess 8-K Ex-99.1 |
| 4Q22-2Q26 | Tradeweb fully electronic share of US HG TRACE: 14.4, 13.3 (1Q23), 14.9, 16.6, 17.2, 17.6 (1Q24), 18.8, 17.7, 18.3, 18.0 (1Q25), 17.9, 18.6, 18.3, 17.7 (1Q26), 19.0% (2Q26): inside 17.7-19.0% from 2Q24 | Tradeweb quarterly 8-Ks |
| 1Q22-2Q26 | Tradeweb fully electronic HY share: 7.1 (1Q22), 6.1 (1Q23), 6.2, 7.8, 6.7, 6.7 (1Q24), 7.6, 7.8, 7.9, 7.5 (1Q25), 8.2, 7.5, 8.1, 7.4 (1Q26), 8.5% (2Q26). Total HG share 25.9, 26.0, 26.2, 25.7, 25.0, 25.7% and HY 10.1, 10.7, 9.8, 10.0, 9.8, 11.1% (1Q25-2Q26) | Tradeweb quarterly 8-Ks |
| 2Q26 | Tradeweb: US HG fully electronic ADV $8,672mm (+18.8%), HY $1,202mm (+8.1%), European credit $3,163mm (+23.4%); credit derivatives +19.6% on "hedge fund and systematic account activity" | Tradeweb 8-K, 2026-07-30 |
| 4Q24-2Q26 | MarketAxess: PT about 11% of HG+HY TRACE in 4Q24 (13% Dec 2024, 9% Jan 2025; its share of TRACE PT 16.2%); PT ADV $1.3bn (1Q25), $1.5bn (2Q25), $1.4bn (FY2025, US PT share 19%, 21% in 4Q25), $1.9bn (1Q26), $2.0bn (2Q26) | MarketAxess 8-Ks and release |
| 2025 | Morgan Stanley: PT 15% of corporate trading in 2025 (11% in 2024), peak 17% in July, 16% at year-end; $1.3tn capped (+52%), about $1.8tn uncapped; HY PT 16% (18% in December), record $56bn in Q4 | The DESK, 2026-02-19 |
| 2025; 2025-01 | Greenwich: IG e-share just under 50%, HY 32%; ADNV $51bn; trade size $398k; 128,141 trades/day; disclosed RFQ 38.6%. January 2025: IG 47%, HY 33%, PT 18% of e-volume (13% a year earlier). Underlying series are sold (MarketView) | The DESK, 2026-01-30; Greenwich PDF |
| 2025-02 to 2025-12 | SG Trend monthly (TTU): -3.19, -1.67, -4.89, -2.22, +1.52, -0.04, +2.74, +5.73, +1.41, +1.37, +1.92%; FY +2.39%. Compounding reproduces the reported YTD to 0.02pp; January 2025 implied +0.14% (derived) | TTU monthly reports |
| 2026-02 to 2026-10 | SG Trend 2026: Feb +3.90, Apr +2.85, May +0.26, Jun -1.17, Jul -1.12, Aug +2.94%; YTD +11.07% (Aug), +16.14% (9 Oct), +14.97% (16 Oct); Jan and Mar pages 404; implied September about +4.3% (derived, CHECK); TTU Barometer 36 on 16 Oct | TTU reports and weekly reviews |
| 2022-03; 2023-03; 2024-05 | SG Trend stress anchors: +9.90%, -7.69% (YTD -7.27%), -2.18% (YTD +11.82%). The 2022-2024 monthly table is in the next three rows; SG's own site (bot wall) and BarclayHedge (paid redirect) give no free CSV | TTU reports; curl tests |
| 2022-01 to 2022-12 | SG Trend monthly as stated in TTU report prose: +3.32, +3.61, +9.90, +7.06, +0.82, +2.85, -4.28, +4.06, +5.78, -0.11, -5.96, -0.25%; reported YTD +29.2 (Jun), +23.79 (Jul), +36.1 (Sep), +27.3 (Dec). The twelve stated months compound to +28.9%, not +27.3%, and Jan-Jun compound to +30.6% against +29.3% implied by the July YTD; TTU's May page says YTD "9.7%" (typo: Jan-May compounds to +27.0%). Treat 2022 monthly values as CHECK | TTU "Trend Following Performance Report" pages Jan-Dec 2022, computed |
| 2023-01 to 2023-12 | SG Trend monthly as stated: -1.37, +1.85, -7.69, +2.89, +3.32, +1.85, -1.60, -0.95, +3.64, +0.12, -4.87, -0.32%; Dec YTD -4.16%. Months implied by the reported YTD path differ for May (+3.23), Jun (+1.94), Sep (+3.39) and Oct (-0.10, a sign change); all other months match to 0.01pp. Use the YTD-implied values; CHECK against SG | TTU reports Jan-Dec 2023, computed |
| 2024-01 to 2024-12 | SG Trend monthly as stated: +1.18, +6.45, +4.19, +1.85, -2.18, -2.68, -2.41, -4.51, +0.98, -4.30, +3.27, +1.40%; Dec YTD +2.42%. YTD-implied Jan +1.19, Jun -2.80, Nov +3.31, Dec +1.29; the rest match. Whole of 2024 reproduces to 0.2pp | TTU reports Jan-Dec 2024, computed |
| 2025-01 | TTU's January 2025 page quotes three intramonth SG Trend snapshots (+1.06%, +0.85%, -0.21% MTD) and no month-end figure; the March YTD (-4.67%) with Feb -3.19% and Mar -1.67% implies January +0.14% CHECK | TTU January 2025 report, computed |
| 2026-10-18 | URL probes with curl through the proxy: all FRED graph-CSV and series pages, Fed ebp_csv.csv, FSR PDF and accessibility-tables page, FINRA workbooks, Fact Book and About-TRACE pages, SEC exhibits (MarketAxess, Tradeweb), iShares HYG and LQD pages, eCFR, NY Fed pd API and TTU report pages return HTTP 200; investor.marketaxess.com/volume returns a Cloudflare "Just a moment" 403 to curl (workbook parsed from the copy fetched earlier in the run) | curl status checks, 2026-10-18 |
| 2015-01-07 to 2026-10-07 | NY Fed primary dealers, eight weekly series PDPOSCSBND-{L13,G13,G5L10,G10,BELL13,BELG13,BELG5L10,BELG10}: IG+HY net annual mean $16.1bn (2017), $8.0bn (2024), $1.3bn (2025), -$2.3bn (2026 YTD; IG -$4.9bn, HY +$2.6bn); low -$11.3bn (2026-02-25); latest -$1.5bn; 56 of 614 weeks negative. Appendix C's "about $4bn net short" matches IG alone CHECK | NY Fed API, computed |
| 2026-10-18 | Repo scan: 102 line-start Trend Watch boxes in `book_src` against 74 in the digest and in Appendix C; about 323 day-level dates (mean 3.2 per box), 10 boxes cite FRED, 23 carry "approx.", 6 CHECK. Appendix C already specifies `trend_tracker.csv`; no extractor script exists in `tools/` | book_src, state/digests |
| 2026-10-15 | Constant-mix check recomputed from a fresh pull: BB 1.97, B 3.26, CCC 12.78, HY 3.23. At the December 2024 weights (53.4/34.0/12.6) the HY OAS would be 377bp; at April 2024 weights 371bp; at October 2026 weights 326bp (actual 323bp, a 3bp identity error). CCC/HY ratio 3.96. Window max 4.61% (2025-04-07), min 2.59% (2025-01-22) reproduced | FRED fredgraph.csv pulls, 2026-10-18 |
| 2025-06-02 | Fridson's article gives 360bp on 2019-12-31 and 1,087bp on "March 23, 2023" in one sentence and March 23, 2020 as the maximum-OAS date later; the 2023 is an internal slip, and the figure caption must say 2020 CHECK. Also confirmed: 53.55% BB on 17 April 2025, 44.53% average 31 Dec 1996 to 31 Dec 2024, face $1.4tn "unchanged from 10 years earlier", +2,147bp peak in 2008-09 | CFA Institute Enterprising Investor (via rpc.cfainstitute.org redirect) |
| 2022-12 | MacKay Shields (New York Life Investments), as quoted in a search snippet: ICE BofA US HY Index 51% BB on a par-value basis at end-2022 against 43% at end-2011, CCC down to 11%; the page itself returned 404 on re-fetch, so par-weight, not market-value-weight, and unverified CHECK | WebSearch snippet, nylim.com page 404 |
| 2025-12-31 | Chapter 12's composition-adjustment inputs reproduce on FRED: HY 2.81%, BB 1.69, B 3.01, CCC 8.85, IG 0.79; 2025-04-30 HY 3.94% (the month-end that hides the 4.61% intraperiod peak). The chapter's illustrative 2025 mix (53/36/11) gives 295bp against 281bp actual; the regression-implied December 2025 mix (55.4/34.3/10.3) gives 288bp, closer. The FRED CSV header is `observation_date,<ID>` (not DATE) and 8 of the 794 HY OAS rows are blank holidays | FRED pulls; book_src/12_ch12 lines 59, 171 |
| 2013-04-03 to 2026-10-07 | NY Fed pd API returns `{"pd":{"timeseries":[{"asofdate","keyid","value"}]}}` with `value` as a string in $mm (first L13 value 3111 on 2013-04-03 = $3.1bn) | markets.newyorkfed.org API, fetched 2026-10-18 |
<!-- ROWS-END -->

## 3. Narrative: drivers and the 2026-2028 outlook

**How the free tier came to this.** Until spring 2026 the first move of any credit quant was a one-line pull of HY OAS from FRED, back to 1996. FRED's April 2026 note now ends with the sentence "for more data, go to the source", which is how a free tier stops subsidizing a paid one. Appendix B says ICE sells the history through a data platform; that was not checked this session. What survives in public is telling. The Board's GZ spread and excess bond premium, the Moody's Baa spread and the Treasury yields all persist with full history because a public body or a rating agency computes them, not an index vendor. The Fed's own Financial Stability Report prints the ICE yield and OAS charts "with permission" but ships data tables only for the series it computes (the premium) and for PitchBook's loan spreads. The pattern is simple: the more a series is a product, the shorter its free window.

**Why three vantage points disagree about protocols.** TRACE records what a dealer reports. When a client sends an RFQ to five dealers and one wins, the winner files a customer trade and the venue vanishes from the record; when two clients meet anonymously on an all-to-all venue, FINRA's monthly file counts the sell side under "ATS". So "ATS is 7% of par" is a floor under all-to-all, and it says nothing about RFQ. We could not establish from public documents which TRACE bucket matched-principal Open Trading prints land in (CHECK). The platforms fill the gap with shares of their own volume, which is a different denominator again: MarketAxess's Open Trading doubled from 19% to 38% of *its* credit volume while its share of TRACE fell from 22.8% (4Q20) to 16.4% (2Q26) by the workbook's own rows, and Tradeweb's fully electronic HG share of TRACE stayed inside 17.7-19.0% for nine quarters while the market electronified around it. Portfolio trading shows the problem in its purest form: 11% in 4Q24 by MarketAxess's estimate, 15% for 2025 by Morgan Stanley, and 18% of electronic volume in January 2025 by Greenwich, three numbers that are each right for their own denominator.

**Why the index spread stopped being one number.** Public high yield stood still at about $1.4tn of face value for ten years while institutional loans and private credit grew (private credit $217bn in 2012 to $1,449bn in 2025, a third of below-investment-grade debt, in the Fed's tables). The weakest borrowers left the bond index for those sleeves, the rest got upgraded or refinanced, and the BB share climbed. What remains is two markets in one ticker: BB at 197bp and CCC at 1,278bp on 15 October 2026, averaged by weights that moved by 11 points of BB in 30 months. A spread history that ignores this compares a 2007 portfolio with a 2026 one.

**Why an ETF premium is a clock.** The fund's NAV is struck at 4pm from evaluated bond prices; the ETF closes on an exchange that sometimes trades when the bond market does not. The HYG series has its fattest tails on exactly those mismatches: the tariff-pause rally of 9 April 2025 (+1.49% at close, after -0.66% the day before) and the bond-market holidays of 13 October and 11 November 2025. The signal is real but it is information about timing before it is information about demand.

**Where this goes, 2026 to 2028.** The calendar is more reliable than any view about spreads.
- *October 2026.* The September SG Trend print arrives around the 22nd (implied about +4.3%, YTD about +15.8%); Tradeweb reports third-quarter shares at the end of the month; whether MarketAxess still updates its workbook after the ICE agreement is the first observable.
- *January 2027.* Under Rule 6c-11 the issuer premium history should drop its 2025 rows and keep 2026; the SG Trend Index reconstitutes on 1 January. Anything built on the 448 rows must be archived before then.
- *First half of 2027.* The ICE-MarketAxess closing is expected then (earlier dossier, CHECK); FINRA's suppression of duplicate affiliate prints, planned for a 2026 filing, will de-inflate TRACE volumes by up to 9% in HG and so break every ratio of platform volume to TRACE volume.
- *April 2028.* The 7 April 2025 tariff peak leaves the free ICE window. After that, the free record of the book's best stress test is gone.

My read is that the equilibrium is a desk-owned archive plus a spread built from TRACE itself. FINRA's six-month enhanced file and the open bond-pricing pipeline are the only sources whose licences allow long histories, and an index-free OAS built from them will replace the pasted ICE chart as the standard. The result would be wrong if ICE reopened its history, if FINRA published protocol or portfolio-trade aggregates, or if the MarketAxess workbook outlived its parent's agreement; each of those is observable within eighteen months.

## 4. Implications for a systematic credit desk and for the RSSG-to-quant reader

**For a systematic credit desk.** The first consequence is that history becomes a balance-sheet asset. A desk that archived daily ICE closes in 2022 owns a regime sample (the rates shock, the March 2023 bank scare) that a desk starting in 2026 cannot buy back from FRED, and the archive's value rises each month as the free window rolls. The second is that a spread level is no longer comparable with itself across time. The 54bp gap between the 323bp headline and the constant-December-2024-mix 377bp is the size of a medium trade idea, and it was invisible to anyone who read only the headline OAS. A z-score on that series partly measures index housekeeping; the model should carry weights as a state variable and standardize composition-adjusted spreads, with the CCC-to-HY ratio (3.96 on 15 October 2026 against 2.28 on 17 October 2023) tracked as a separate regime feature. The third is that any liquidity feature built on volume must say whose volume. A model that divides platform ADV by TRACE ADV inherits the 2021 double-reporting correction, the 2026 duplicate prints and the end of MarketAxess's monthly releases, and it will show a share "decline" on the day FINRA fixes the denominator. The fourth is that an ETF premium feature should be conditioned on the calendar: on the three bond-holiday sessions in the sample the HYG premium averaged +0.37% against +0.135% overall, and a signal that fires on Veterans Day is trading the holiday schedule.

**For the reader coming from restructuring advisory.** The nearest habit is the data room. A restructuring banker knows that a number without an as-of date, a perimeter and a source is not evidence, and knows which exhibits the other side redacted. The same instincts apply here almost one for one: the three-year window is a redaction, the TRACE ATS flag is a perimeter, and "PT 15% versus 11% versus 18%" is three management cases on different bases. What the reader must add is the quantitative habit of keeping the redacted versions, because in this market the exhibit is deleted from the room a day at a time. The CCC story is also home ground. The tier at 12.8% is where the reader's old clients live, and the 8.1% weight explains why the headline looks so calm: the borrowers who would have mattered to a restructuring group are a shrinking slice of an index whose average has been improved by upgrades and by the exit of the weakest names to loans and private credit. The same observation turns the book's CCC decompression chapters into a data-engineering lesson as much as a market view.

## 5. Quant hooks (variables, datasets, signals)

**Variables, with identifiers and the licence risk that goes with each.** Names are the column names a `figure_series.csv` should carry; the Appendix B atlas row can be generated from the same table.

| variable | definition | identifier / URL pattern | free window | note |
|---|---|---|---|---|
| `hy_oas`, `bb_oas`, `b_oas`, `ccc_oas`, `ig_oas`, `bbb_oas` | ICE BofA option-adjusted spreads, % | FRED BAMLH0A0HYM2, BAMLH0A1HYBB, BAMLH0A2HYB, BAMLH0A3HYC, BAMLC0A0CM, BAMLC0A4CBBB | rolling 3 years (794 rows to 2026-10-15) | "internal use only"; archive daily |
| `hy_tr`, `bb_tr`, `b_tr`, `ccc_tr`, `ig_tr` | total-return index levels | BAMLHYH0A0HYM2TRIV, ...A1BBTRIV, ...A2BTRIV, ...A3CMTRIV, BAMLCC0A0CMTRIV | rolling 3 years | the guessed ID BAMLH0A0HYM2TRIV does not exist |
| `baa10y`, `dgs10`, `dgs2`, `vix` | Moody's Baa less 10y; Treasury CMT; VIX close | BAA10Y, DGS10, DGS2, VIXCLS | 1986, 1962, 1976, 1990 to date | no window; safe long axis |
| `gz_spread`, `ebp`, `est_prob` | Gilchrist-Zakrajsek spread, excess bond premium, implied recession probability | federalreserve.gov/econres/notes/feds-notes/ebp_csv.csv | 1973-01 to 2026-09, monthly | Board product, no licence issue |
| `w_bb`, `w_b`, `w_ccc` | implied ICE HY market-value weights | author regression on the four HY total-return series, 126-day window | 2024-04 onward (limited by the window) | standard error about 0.2pp; not an ICE-published weight |
| `prem_hyg`, `prem_lqd` | close less NAV, % of NAV | embedded `premiumDiscountChartData` on the iShares pages | 2025-01-02 to date, until the Rule 6c-11 roll in 2027 | archive monthly; flag bond-holiday sessions |
| `trace_ats_par_share`, `trace_corp_par_day` | ATS share of corporate par; average daily par, $bn | cdn.finra.org/trace/volume/monthly/TRACE_Public_Monthly_Report_YYYY-MM.xlsx | 2017-01 to 2026-09 | sell-side definition; RFQ trades land in "Customer" |
| `mkt_ot_share`, `mkt_hg_share_trace` | Open Trading % of MarketAxess credit volume; MarketAxess HG ADV over FINRA HG TRACE ADV | MarketAxess monthly workbook | 2018-01 to 2026-06, now frozen | restated retrospectively; denominator changes in 2021-07 and 2026-03 |
| `tw_fe_hg`, `tw_fe_hy`, `tw_total_hg` | Tradeweb share of US TRACE, fully electronic and total | quarterly 8-K Ex-99.1 | 4Q22 (HG), 1Q22 (HY) to 2Q26 | quarterly, restated by about 10bp |
| `pt_share` | portfolio trading as % of corporate volume | three vantage points (MarketAxess, Morgan Stanley, Greenwich) | sparse | always store the denominator as a text column |
| `sg_trend_m` | SG Trend Index monthly return, % | TTU monthly reports (secondary) | 2022-01 to 2026-08 | cross-check by YTD; 2022-23 carry CHECK |
| `pd_net_ig`, `pd_net_hy` | primary-dealer net corporate position, $mm | NY Fed API PDPOSCSBND-* | weekly from 2013 (IG) and 2015 (all eight) | state the perimeter in the caption |

**A script stub (not run; for the figure build).** It encodes the three gotchas found this session: one series per request, a header and row-count assertion so a silently shortened window raises, and a dated archive so history accrues locally.

```python
import csv, io, datetime as dt, pathlib, urllib.request

FRED = "https://fred.stlouisfed.org/graph/fredgraph.csv?id={sid}"   # one id per call; cosd applies to the first id only
MIN_ROWS = {"BAMLH0A0HYM2": 700, "BAA10Y": 10000}                 # fail loudly if the window shrinks or grows unexpectedly

def pull(sid, root="archive/fred"):
    raw = urllib.request.urlopen(FRED.format(sid=sid), timeout=40).read().decode()
    if not raw.startswith("observation_date," + sid):               # a wrong id returns HTML, not CSV
        raise ValueError(f"{sid}: not a FRED CSV: {raw[:60]!r}")
    rows = [r for r in csv.reader(io.StringIO(raw))][1:]
    rows = [(d, float(v)) for d, v in rows if v not in ("", ".")]    # holidays are blank
    if len(rows) < MIN_ROWS.get(sid, 100):
        raise ValueError(f"{sid}: only {len(rows)} rows; window changed?")
    out = pathlib.Path(root) / f"{sid}_{dt.date.today():%Y%m%d}.csv"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("date,value\n" + "\n".join(f"{d},{v}" for d, v in rows))
    return rows                                                      # first date is 2023-10-17 today and rolls daily

def implied_weights(r_hy, r_bb, r_b, r_ccc):
    """126-day constrained least squares: r_hy = w_bb*r_bb + w_b*r_b + w_ccc*r_ccc, w >= 0, sum(w) = 1."""
    ...  # scipy.optimize.minimize with SLSQP; report the standard error of each weight
```

**Tables that can be written as CSV today.** Each has a verified source in section 2: `sg_trend_monthly.csv` (date, return_pct, ytd_reported_pct, ytd_implied_return_pct, flag; 2022-01 to 2026-08); `trace_corp_monthly.csv` (month, par_mm, trades, ats_par, interdealer_par, customer_par; 117 rows); `mkt_platform_quarterly.csv` (quarter, ot_share, hg_adv, hy_adv, trace_hg_adv, trace_hy_adv, pt_adv); `tw_share_quarterly.csv` (quarter, fe_hg, fe_hy, total_hg, total_hy; 4Q22 to 2Q26); `etf_premium_daily.csv` (date, ticker, premium_pct; 448 x 2 rows, to be archived before 2027); `ice_weights_implied.csv` (date, w_bb, w_b, w_ccc, se); `trend_tracker.csv` for Appendix C, whose columns already exist in the specification, with a regex extractor over `book_src/*.md` for the 102 line-start Trend Watch boxes and their about 323 day-level dates (an `approx` column from the 23 "approx." flags and a `check` column from the 6 CHECK flags).

**Signals and features these series make possible.**
1. *Composition-adjusted spread.* `oas_adj(t) = sum_k w_k(ref) * s_k(t)` with the reference weights frozen at a named date, and `composition_effect = oas - oas_adj`. On 15 October 2026 the effect against December 2024 is -54bp (323 against 377). Standardize `oas_adj`, not `oas`.
2. *CCC-to-HY ratio.* 3.96 now, 2.28 on 17 October 2023, 2.44 on 8 April 2025. A rising ratio with a flat headline OAS is the index-composition signature of weak tails inside a tight average.
3. *Premium z-score with a calendar mask.* `z = (prem - mean) / sd`, estimated off sessions where NYSE was open and SIFMA was closed. The three holiday sessions in the sample have means of +0.37% (HYG) and +0.27% (LQD) against +0.135% and +0.038% overall.
4. *Platform share with a denominator flag.* Store `denominator in {FINRA_capped, FINRA_uncapped, company_estimate}` and a break dummy for 2021-07 (ATS double-report fix) and 2026-03 (affiliate duplicates).
5. *Long-axis anchor.* GZ and EBP for 1973 to date; the Baa-10y spread for 1986 to date. These supply regime labels (EBP 3.41 in October 2008 against -0.39 in September 2026) that the ICE window cannot.
6. *Lead-lag.* HY OAS peaked on 7 April 2025 and the VIX on 8 April; a one-day lead on a single episode is an anecdote, but the daily series are free to test on every episode of the window.
7. *Dealer inventory.* `pd_net_ig + pd_net_hy` at -$1.5bn in the latest week, with 56 of 614 weeks negative; the sign flips of 2026 are the cleanest free proxy for dealer balance-sheet retreat.
8. *Crowding.* TTU Trend Barometer 36 on 16 October 2026 beside SG Trend YTD +14.97%: a trend-following sleeve that is up 15% and cold at once is where the book's Chapter 10 should look first.

## 6. TOC proposals

(pending)

## Sources

(pending)

## Book placement

(pending)
