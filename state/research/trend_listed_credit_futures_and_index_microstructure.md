# TREND DOSSIER: Listed credit futures (CME, Cboe iBoxx IBHY/IBIG, ICE, Eurex) and CDX/iTraxx index microstructure, 2021-2026

*Researcher dossier for the book "Systematic & Quantitative Credit". Written 2026-10-18. Feeds: ch10b (credit index futures and index microstructure), ch08 (isolating IDO and empirical duration), ch20 (credit ETF creation/redemption arb), appC (trend tracker).*

## 1. Headline trends

*(to be written after evidence table)*

## 2. Evidence table

| date | fact / number | source |
|---|---|---|
| 2018-09-10 / 2018-10-08 | Listing dates of Cboe iBoxx iShares $ High Yield (IBHY) and $ Investment Grade (IBIG) Corporate Bond Index Futures on CFE. Cash-settled, $1,000 multiplier, tick 0.01 index points = $10.00/contract; up to 4 serial months plus 4 March-quarterly months; final settlement on the first business day of the contract month at the Markit/IHS iBoxx index close; cash delivered next business day. | Cboe, Summary Product Specifications Chart (cdn.cboe.com iboxx-ishares-contract-specs.pdf) |
| 2023 (spec rev.) | CFE rules for IBHY/IBIG: block minimum **50 contracts** (one leg), block/ECRP price increment 0.005 index points; ECRP related-position leg must be an ETF or a total return swap; position limit 100,000 contracts net (futures plus delta-adjusted options); reportable level 200 contracts; no market orders and no TAS; no-bust range 2% of market price. | Cboe contract-spec PDF (same) |
| 2023-08-08 | Cboe fact sheet (v1.0): indexes are the iBoxx iShares $ HY / IG corporate bond indices (built off the HYG and LQD holdings); options on futures IBYO (HY) and IBGO (IG) exist, physically delivered into the underlying future; the sheet pitches lower initial margin and "potentially better 60/40 tax treatment", UCITS eligibility, and no borrow needed to short. **CHECK**: the headline says "1 IBHY contract = +2500 high yield bonds, 1 IBIG = +1100 IG bonds" while its own comparison table gives constituents HY ~1,100 and IG ~2,500, so one of the two is transposed. | Cboe fact sheet (Cboe2023-iBoxx-Factsheet.pdf) |
| 2025-07-01 / 2026 page | Cboe Credit Suite page lists IBHY, IBIG, IEMD (EM debt futures), IBYO and IBGO (options on futures); says the HY and IG indexes are built by intersecting a benchmark with the actual holdings of HYG and LQD so the futures track the ETF portfolios; cites Bloomberg 20-day average volume data as of 2025-07-01; copyright 2026. | cboe.com/credit-suite |
| 2026-05-28 | CME Group (sponsored piece, speaker Ted Carey, CME): institutions adopting CME credit futures alongside ETFs, CDS and TRS; the page discloses no volumes, OI, launch date or spec. **CHECK** for any number before use. | The DESK, fi-desk.com/cme-credit-futures-surge/ |
| 2026-10-16 | Cboe (sponsored): block trades in Cboe credit index futures topped $1bn in a month for the second month running in Aug 2026. IBHY blocks about $1bn notional vs $2bn electronic (blocks nearly 1/3 of active volume); IBIG blocks $557m vs $888m electronic (just under 40%); IBIG blocks overtook IBHY for the first time; monthly block counts rose from low single digits in early 2024 to double digits through most of 2026, some months mid-teens. Exchange-reported, sponsored. | The DESK, fi-desk.com/cboe-block-trading-has-arrived-in-credit-index-futures-2/ |
| 2023-07-10 | Options on IBHY and IBIG futures (IBYO, IBGO) listed on CFE: American-style, physically settled into the same-month future (which then cash-settles), strike interval 0.25 index points, tick 0.01 = $10, block minimum 50 contracts, ECRP not allowed for the options. | Cboe, Summary Product Specifications Chart for options (IBHY-IBIG_OOF_Contract_Specification.pdf) |
| 2023-08-06 | CFE extended IBHY/IBIG futures trading to nearly 24 hours per weekday (Sunday-evening start; 5:00pm CT prior day to 4:00pm CT), turning the listed beta hedge into a global-hours instrument alongside CDX/iTraxx and ETFs in other time zones. | Cboe FAQ, 10-10-23 (cdn.cboe.com/resources/futures/10-10-23-Cboe2023-iBoxxFutures-FAQ.pdf) |
| 2023 (FAQ) | Cboe says the IBHY index construction is "inter-related with" HYG and the IBIG index with LQD, and that IBHY/IBIG futures are "highly correlated" with HYG/LQD; no correlation or tracking-error statistic is published in the FAQ or page. Spread-order pricing doc is dated 2018-10-29. | Cboe FAQ (same); cboe.com product page |
| 2026 (page) | Cboe IEMD (iBoxx USD Liquid Emerging Market Sovereigns & Sub-Sovereigns Index, IBXXEMLQ): index requires USD denomination, >= $1bn outstanding, >= 1 year to maturity at rebalance; page gives no launch date or volume. | cboe.com/tradable-products/corporate-credit/cboe-iboxx-emerging-market-bond-index-futures |
| 2018-11-08 / 2018-11-09 | First non-zero daily volume in the CFE daily volume/OI file: IBHY 162 contracts (OI 211) on 2018-11-08; IBIG 2 contracts on 2018-11-09 (listing dates Sep/Oct 2018, so the first two months printed nothing). | Cboe CFE daily volume and OI CSV (cdn.cboe.com/data/us/futures/market_statistics/historical_data/cfevoloi.csv), computed this session |
| 2018-2022 annual (contracts) | IBHY volume 3,656 (2018), 19,819 (2019), 136,330 (2020), 273,155 (2021), 276,893 (2022); IBIG 18, 861, 16,696, 151,587, 140,416. Year-end OI small: IBHY 27 / 215 / 1,161 / 839 / 860; IBIG 0 / 0 / 70 / 139 / 773. | Cboe CFE CSV (same), computed this session |
| 2023 annual | Volume collapsed to 72,429 (IBHY) and 69,076 (IBIG), about 26% and 49% of 2022 (monthly IBHY ADV ~5-6k contracts vs ~22-26k in 2022). Year-end OI 661 / 619. **CHECK**: the files do not say why 2020-22 volume was 3-4x the 2023 run-rate (candidates: market-maker incentive programme, index re-spec in May 2023, one large user); do not attribute without a source. | Cboe CFE CSV (same), computed this session |
| 2024 annual | IBHY 77,547 and IBIG 74,568 contracts; IEMD (first print 2024-07-01, 503 contracts) 33,081 in six months; IBYO/IBGO options 168 and 79 contracts in total (first options print 2023-11-10 for HY, 2024-04-15 for IG). Year-end OI: IBHY 2,556, IBIG 2,097, IEMD 681. | Cboe CFE CSV (same), computed this session |
| 2025 annual | IBHY 141,817 (+83% y/y) and IBIG 135,634 (+82%); IEMD 93,292 (about 2.8x its 2024 half-year). Options on the futures essentially dead (7 and 5 contracts). Year-end OI IBHY 8,672 (record in the file: 10,202 on 2025-11-24), IBIG 4,490, IEMD 489. | Cboe CFE CSV (same), computed this session |
| 2026 YTD to 2026-10-15 | IBHY 168,798 and IBIG 144,179 contracts already exceed all of 2025; vs the same window of 2025 (99,747 / 98,508) that is +69% and +46%. IEMD 103,790 (vs 73,268, +42%). OI on 2026-10-15: IBHY 6,162, IBIG 4,629, IEMD 1,627; IBIG OI peak 15,660 on 2026-08-26. Options volume zero in 2026. | Cboe CFE CSV (same), computed this session |
| monthly 2026 | Peak months: May 2026 IBHY 31,824 and IBIG 24,060 contracts; Aug 2026 IBHY 29,308 and IBIG 20,233; Feb 2026 24,760 / 24,927. Troughs 6.9k-11k contracts in non-roll months (Jun, Jul, Sep). Volume is lumpy and clusters in the last week of the month before expiry (top days: 2026-08-24, 2026-05-26/27, 2025-11-24/25, 2026-02-23/24), i.e. roll-driven. | Cboe CFE CSV (same), computed this session |
| derived 2026-10 | Implied average notional per contract, using Cboe's Aug 2026 notionals (IBHY blocks $1bn + electronic $2bn = $3bn; IBIG $557m + $888m = $1.445bn) divided by CSV contract volume (29,308; 20,233): about $102k per IBHY and about $71k per IBIG contract. **CHECK**: derived, assumes the CSV and the article count the same trades; would put IBHY OI at ~$0.8bn (7,424 contracts) and IBIG OI at ~$0.36bn at end Aug 2026. | Derived from Cboe CSV and The DESK/Cboe article above |
| 2025-04-07 to 04-10 | Tariff-shock week: IBHY volume only 1,079 / 830 / 1,137 / 852 contracts and IBIG 855 / 1,316 / 381 / 568 per day (about 0.1-0.15bn notional per day) (at the ~$71-102k per-contract notional derived below). The listed layer was a rounding error in the stress hedge relative to the cash/ETF/CDX markets (compare ISDA CDX volumes in the CDX rows). | Cboe CFE CSV, computed this session |
<!-- ROWS-END -->

## 3. Narrative: drivers and the 2026-2028 outlook

*(pending)*

## 4. Implications for a systematic credit desk and for the RSSG-to-quant reader

*(pending)*

## 5. Quant hooks (variables, datasets, signals)

*(pending)*

## 6. TOC proposals

*(pending)*

## Sources

*(pending)*

## Book placement

*(pending)*
