# Edition 1 Fact-Check: Trend Watch boxes, Chapters 8-14

Checked 2026-10-18 against `state/digests/trend_watch_boxes.md` (boxes from 08_ch08 .. 14_ch14). No `book_src` file was edited.
Verdicts: CONFIRMED (source says it), CORRECTED (source differs; replacement given), STALE (true at its date, superseded), UNVERIFIABLE (no accessible source; hedge).
Method note: claims quoting the repo's own source shelf (Dynkin, Man, BlackRock, Blackstone, Nuveen PDFs in `source_pdfs/`) are checked against the PDF text; FRED series are checked from FRED's own CSV download; everything else against the cited publisher page or a search.

## Chapter 8 (08_ch08_isolating_ido_and_empirical_duration.md): three boxes

FRED series were recomputed from FRED's own CSV download (file created 2026-10-17, data through 2026-10-15). Window conventions and the book's own definitions of rho and H were reproduced exactly for 2025 and 2026 and for 2024 once the first change of the year is dropped (249 changes).

### Box 8.1: The Correlation That Changed Sides, 2018-2026

| claim | verdict | evidence / correct figure | source |
| :--- | :--- | :--- | :--- |
| Stock-bond correlation negative or near zero (rolling 3-yr) Nov 2000 to 2020 | CONFIRMED (secondary) | Morningstar-based summaries: correlation "predominantly negative" since 2000 and near zero 2000-2020. Morningstar's own page returned 403, so read via secondary summary. | https://www.portfolio-institutional.co.uk/news-and-analysis/the-equity-bond-dilemma/ ; https://indexes.morningstar.com/insights/perspective/bltd4f3cf0897f7dc07/why-portfolio-diversification-is-about-more-than-just-correlations |
| Turned positive in 2021 | CONFIRMED (secondary) | Same summaries: "edged into positive territory in 2021". | same |
| "roughly 0.58 for full-year 2022 and 2023" | UNVERIFIABLE | Sources disagree: Portfolio Institutional repeats 0.58 for 2022 and 2023; SmartAsset attributes 0.58 to 2022 alone, with 0.15 for the trailing three years. Primary Morningstar text not accessible. Hedge: "roughly 0.58 for full-year 2022 (secondary summaries of Morningstar's data; later-year figures differ by source)". | https://smartasset.com/investing/morningstar-inflation-history ; https://www.portfolio-institutional.co.uk/news-and-analysis/the-equity-bond-dilemma/ |
| 10-yr rose 1.52% to 3.88% in 2022 | CONFIRMED | DGS10: 1.52 (2021-12-31), 3.88 (2022-12-30). | FRED DGS10 https://fred.stlouisfed.org/series/DGS10 |
| 2-yr rose 0.73% to 4.41% in 2022 | CONFIRMED | DGS2: 0.73 (2021-12-31), 4.41 (2022-12-30). | FRED DGS2 https://fred.stlouisfed.org/series/DGS2 |
| Bloomberg US Corp HY returned about -11.2% in 2022 | CONFIRMED | -11.19%. Bloomberg's own page not reached; YCharts shows Bloomberg index data. BlackRock p.3 also says HY "down over 11%". | https://ycharts.com/indices/^BBUSCOHYTR |
| Bloomberg IG Corporate index about -15.8% in 2022 | CONFIRMED | -15.76%. | https://ycharts.com/indices/^BBUSCOTR |
| Slok, 3 Dec 2022: HY total-return index "down 10% so far in 2022", mainly duration | CONFIRMED | Apollo Academy post dated December 3, 2022 by Torsten Slok, title "High Yield Total Returns in 2022 Mainly Driven by Moves in Duration"; body: "The US corporate high yield total return index is down 10% so far in 2022". The duration attribution is in the headline, not the body. | https://apolloacademy.com/?p=11885 |
| Table: rho HY/BB/B/CCC/IG and implied H for 2024, 2025, 2026 YTD (249/248/197 days) | CONFIRMED | Recomputed from FRED CSV (DGS10 daily change vs relative OAS change; H = 1 + mean(s)*rho*sd(rel ds)/sd(dy)). 2024: rho -0.34/-0.39/-0.29/-0.22/-0.38, H 0.65/0.64/0.66/0.61/0.92. 2025: -0.35/-0.38/-0.31/-0.31/-0.32, H 0.42/0.47/0.42/0.14/0.90. 2026: -0.03/-0.10/+0.02/+0.09/-0.08, H 0.97/0.90/1.03/1.19/0.98. All 15 rho values and 15 H values match to two decimals. | FRED BAMLH0A0HYM2, BAMLH0A1HYBB, BAMLH0A2HYB, BAMLH0A3HYC, BAMLC0A0CM, DGS10 |
| "0.4 to 0.65 of analytical duration" (2024-25 HY); 2026 H roughly 1 | CONFIRMED | HY-and-tier H 2024-25 ranges 0.14 (CCC 2025) to 0.67; HY, BB, B span 0.42-0.66; 2026 HY 0.97. Note the CCC 2025 value (0.14) is outside "0.4 to 0.65" but the sentence is about HY. | FRED, as above |
| Rolling 60-day CCC hedge ratio touched -0.78 in the window ending 23 May 2025 | CONFIRMED | Rolling 60-change H for CCC: -0.78 on 2025-05-23 (global minimum of the series). | FRED BAMLH0A3HYC, DGS10 |
| IG rolling 60-day H never left [0.79, 1.04] | CONFIRMED | Min 0.79 (2024-10-11), max 1.04 (2026-06-03). | FRED BAMLC0A0CM, DGS10 |
| FRED: from April 2026 ICE BofA OAS series include only three years, so free history begins October 2023 | CONFIRMED | FRED note: "Starting in April 2026, this series will only include 3 years of observations. For more data, go to the source." First observation in the download is 2023-10-17. | https://fred.stlouisfed.org/series/BAMLH0A3HYC |

### Box 8.2: CCC Decompression, 2024-2026

| claim | verdict | evidence / correct figure | source |
| :--- | :--- | :--- | :--- |
| CCC-to-BB OAS ratio 4.0x end-2024 (746/186); 5.2x end-2025 (885/169); 6.5x on 15 Oct 2026 (1,278/197) | CONFIRMED | 7.46/1.86 = 4.01; 8.85/1.69 = 5.24; 12.78/1.97 = 6.49. | FRED BAMLH0A3HYC, BAMLH0A1HYBB |
| CCC OAS reached 12.82% on 14 Oct 2026, "while the broad HY OAS was 3.23% and IG 0.84%" | CORRECTED (minor, date mismatch) | 12.82% on Oct 14 is right and is the highest in the three-year window. HY OAS 3.23% and IG 0.84% are the Oct 15 values; on Oct 14 HY was 3.25% (IG 0.84%). Find/replace below. | FRED BAMLH0A3HYC, BAMLH0A0HYM2, BAMLC0A0CM |
| Beta of CCC relative spread changes on HY relative spread changes: 0.54 (2024), 0.55 (2025), 0.45 (2026 YTD) | CONFIRMED | OLS slope: 0.541, 0.555 (0.554 within-window), 0.452. | FRED BAMLH0A3HYC, BAMLH0A0HYM2 |

### Box 8.3: Listed Credit Beta and the Duration-Hedged Index Family

| claim | verdict | evidence / correct figure | source |
| :--- | :--- | :--- | :--- |
| 23 Apr 2024 CME announcement: credit futures to launch 17 June 2024, pending regulatory review, on Bloomberg US Corporate (IG) and Bloomberg US HY Very Liquid indices, plus a duration-hedged index future | CONFIRMED | Three contracts: IG, HY Very Liquid, and IG Duration Hedged; scheduled to begin trading Monday 17 June 2024, pending regulatory review; ~$100,000 contract size; intercommodity spread with Treasury futures and margin offsets against rate and equity-index futures. The duration-hedged contract is on the IG index (the box does not say which index). | https://www.cmegroup.com/media-room/press-releases/2024/4/23/cme_group_u_s_creditfuturestobegintradingonjune17.html ; https://www.fi-desk.com/cme-group-to-begin-trading-credit-futures-in-june/ |
| HYGH launched 27 May 2014 | CONFIRMED | Inception 2014-05-27. | https://stockanalysis.com/etf/hygh/ |
| HYGH net assets about $652mm (15-16 Oct 2026) | CONFIRMED (approx.) | $653.82M, page checked 17 Oct 2026 (aggregator; iShares page not reached). | https://stockanalysis.com/etf/hygh/ |
| HYGH effective duration -0.01 years | UNVERIFIABLE | ishares.com page not accessible (404 on the product URL guess; search found no figure). Hedge: "an effective duration near zero". | n/a |
| HYGH roughly 4% of HYG's size | UNVERIFIABLE | HYG AUM not fetched; implies HYG near $16bn. Hedge: "a small fraction of HYG's size". | n/a |
| HYG effective duration about 3.2 years vs 4.2-4.8 in Ben Dor 2007-2009 | UNVERIFIABLE | HYG figure not accessible; a State Street note puts the Bloomberg US HY index option-adjusted duration at about 3.1 years in March 2024 (down from over 4.25 in 2022). Ben Dor's range is a shelf source and was not rechecked. | https://www.financialinvestigator.nl/en/nieuws-detailpagina/2024/03/21/State-Street-SPDR-ETFs-The-defensive-qualities-of-high-yield |

## Chapter 9 (09_ch09_factor_investing_in_credit.md): three boxes

Claims that quote the repo's source shelf were checked against the extracted PDF pages in `state/pdf_pages/` (page numbers as cited in the boxes).

### Box 9.1: Systematic credit's share of the market

| claim | verdict | evidence / correct figure | source |
| :--- | :--- | :--- | :--- |
| Systematic strategies manage roughly 20% of global equities but "less than 2% of the fixed-income universe" | CONFIRMED | Blackstone p.2: "systematic strategies manage roughly 20% of global equities, they account for less than 2% of ..." | source_pdfs/Blackstone_Systematic_Credit.pdf p.2 |
| Dynkin: scientific credit investing stands "where scientific equity investing stood at the turn of the century: in an uncrowded space and on the threshold of considerable secular growth" | CONFIRMED | Verbatim on p.45. | Dynkin epub p.45 |
| Stated reasons: more fixed-income data, price transparency, "established quantitative insights from the equity markets" (p.49-50) | CONFIRMED | p.49: "increased availability of fixed income data, improved price transparency, and the influence of established quantitative insights from the equity markets". | Dynkin epub p.49 |
| Barclays QPS (Mateer et al., 2024) via Impax, 19 Sep 2025: US$90bn to US$140bn in funds using quantitative screening in IG and HY | CONFIRMED | Impax: funds using quantitative screening "now hold between US$90bn and US$140bn in assets under management"; footnote 2 cites Mateer et al., 2024; page dated 19 September 2025. "Growing faster than fixed income overall" was not in the passage retrieved; keep only if the original report is checked. | https://impaxam.com/insights-and-news/blog/quant-meets-credit-enhancing-fundamental-analysis-through-systematic-screening/ |
| State Street converted two US high-quality corporate strategies to a fully systematic process effective 31 Dec 2023 (SSGA SAFI Q3 2025 commentary, 25 Nov 2025) | CONFIRMED (wording note) | Page: strategies moved to the SAFI process "effective December 31, 2023"; commentary dated November 25, 2025. The page does not itself say "fully systematic"; SAFI is State Street's systematic active fixed income process. Suggested wording: "moved to State Street's SAFI (systematic active fixed income) process effective 31 December 2023". | https://www.ssga.com/us/en/institutional/insights/fixed-income-q3-2025-safi-commentary |
| Robeco QI Global Multi-Factor Credits launched 15 June 2015 | CONFIRMED (wording note) | Share-class inception 15-06-2015; the fund page's performance table starts "since inception" 12-06-2015. | https://www.robeco.com/en-int/products/funds/isin-lu1235145304/robeco-qi-global-multi-factor-credits-fh-eur |
| Robeco fund EUR 1,039mm at 30 Sep 2026 | CONFIRMED | EUR 1,039.09 million as of 30-09-2026. | same |
| Realized transaction costs 0.20% a year (three-year average) | CONFIRMED | 0.20%, average annual over the last three years. | same |
| Man: prime brokers now provide daily borrow availability across the cash-bond universe | CONFIRMED | Man p.11: "Prime Broker security lending desks now provide daily feeds with firm borrow availability and fees across the entire investable cash bond universe." | source_pdfs/Man_Quantitative_Credit_Alpha_Early_Mover_2022.pdf p.11 |

### Box 9.2: The cost curve, 2007-2026

| claim | verdict | evidence / correct figure | source |
| :--- | :--- | :--- | :--- |
| Chen, Lesmond and Wei (2007): bid-ask about 25bp for AAA and 180bp for CCC; Man: "Both of these figures would be markedly tighter in the current market" | CONFIRMED (as relayed by Man) | Man p.20 gives 25bps (AAA) and 180bps (CCC) and the quoted sentence verbatim. The 2007 paper itself was not opened. | Man 2022 p.20 |
| Barclays LCS, IG index average: 0.4% (2007), 2.8% (2008), 0.6% in 2018-2019 | CONFIRMED | Dynkin p.703: "increased from 0.4% in 2007 to 2.8% in 2008 and then declined to 0.6% in 2018-2019". | Dynkin p.703 |
| July 2019 LCS: IG 0.608%, HY 0.941%, Treasuries 0.028% | CONFIRMED | Dynkin Table 18.3 (31 July 2019): USD Credit IG 0.608, USD Credit HY 0.941, USD Treasuries 0.028. | Dynkin p.703 |
| Cost drag on the liquid ESP+EMC strategy fell from about 1.15% a year (2007-2012) to about 0.64% a year (2013-2019) | CONFIRMED | p.711: relative return declines 1.15%/yr from 2007 to 2012; drag 0.64%/yr in 2013-2019. The strategy label "ESP+EMC" was not rechecked. | Dynkin p.711 |
| Man 20-day HY bid-ask spiked Feb-March 2020 and normalized within months (levels only in a chart) | CONFIRMED (shape only) | Chart title "High-Yield Bid-Ask Spreads (20-day average)" on Man p.20; box correctly gives no levels. | Man 2022 p.20 |
| Robeco realized transaction costs 0.20% a year, three-year average to 30 Sep 2026 | CONFIRMED | See Box 9.1. | Robeco fund page |
| "In a stress month it can jump fivefold overnight" | UNVERIFIABLE | The only cited series is Dynkin's IG LCS, 0.4% (2007) to 2.8% (2008), a seven-fold rise over about a year, not overnight. No cited source shows a fivefold overnight jump. Hedge: "in a stress episode it can rise several-fold within months (Barclays IG LCS: 0.4% in 2007, 2.8% in 2008)". | Dynkin p.703 |

### Box 9.3: The tight-spread regime and the first live track records, 2024-2026

| claim | verdict | evidence / correct figure | source |
| :--- | :--- | :--- | :--- |
| US IG OAS about 77bp (4 July 2025) to about 72bp (Sept 2025), "the tightest since 1998" | CONFIRMED (index caveat) | SSGA: "near 77bps on July 4, 2025" and "roughly 72bps in September", "the tightest spreads since 1998". These are the Barclays/Bloomberg index levels. On FRED's ICE BofA index the same dates read 80bp (4 July) and a low of 74bp (19 Sept), so the 77/72 pair should be attributed to State Street's index, not to ICE BofA. | https://www.ssga.com/us/en/institutional/insights/fixed-income-q3-2025-safi-commentary ; FRED BAMLC0A0CM |
| Dynkin p.545: ESP outperformance "is larger when there is a high dispersion in ESP" | CONFIRMED | p.545: "the ESP strategy is larger when there is a high dispersion in ESP". | Dynkin p.545 |
| State Street Q3 2025: value +14bp (intermediate), +43bp (long); momentum roughly flat to +4bp | CONFIRMED | Value +14bps / +43bps; momentum flat (Intermediate) / +4bps (Long). | SSGA SAFI Q3 2025 commentary |
| Max relative drawdown since Jan 2024 of -5bp against a peer average of -44bp | CONFIRMED (scope note) | -5bps is SAFI Intermediate only; -44bps is the average maximum alpha drawdown across 73 managers. Add "(intermediate strategy)". | same |
| Roughly flat net through March-April 2025 drawdown while the average manager lagged by about 35bp | CONFIRMED (period note) | Credit managers underperformed benchmarks by 35bps on average; SAFI "roughly flat, net of fees" during the Q1 drawdown (the page's period label is Q1, the box says March-April). | same |
| Since-inception IRs of 2.89 and 2.63; sample under two years | CONFIRMED | 2.89 (Intermediate), 2.63 (Long); strategies systematic since 31 Dec 2023. | same |
| Robeco as of 30 Sep 2026: 1y -2.69% vs -2.77%; 3y 3.14% vs 3.45%; 5y -2.00% vs -1.64%; since inception 0.63% vs 0.87% | CONFIRMED | All eight figures match the fund page (annualized, net, vs Bloomberg Global Aggregate Corporates hedged). | Robeco fund page |
| Attribution: value slightly positive, low-risk/quality the largest detractor, momentum neutral, size slightly negative | CONFIRMED | Fund page (September 2026 commentary): value slightly positive; low-risk/quality largest detractor (underweight longer-dated bonds); size slightly negative; momentum neutral. | same |
| Backtests in the chapter run from an IR of 0.5 to 2.4 | OUT OF SCOPE | Internal to the chapter, not a Trend Watch fact. | n/a |

## Chapter 10 (10_ch10_trend_and_time_series_momentum.md): two boxes

The ISDA research note and the SG Prime Services CTA update were downloaded by the fetch tool as PDFs and read as text, so these checks are against the primary documents.

### Box 10.1: The index CDS market becomes the trend follower's venue, 2021-2026

| claim | verdict | evidence / correct figure | source |
| :--- | :--- | :--- | :--- |
| ISDA research note of 29 July 2026: total CDS trading $41.8tn in 2025, prior peak $38.7tn (2022), $31.4tn (2023) | CONFIRMED | "record $41.8 trillion in 2025, above the prior peak of $38.7 trillion in 2022. It declined to $31.4 trillion in 2023". Page dated July 29, 2026. | https://www.isda.org/2026/07/29/cds-market-dynamics-five-years-of-activity-and-a-record-2025/ ; https://www.isda.org/a/Pa0iE/CDS-Market-Dynamics-Five-Years-of-Activity-and-a-Record-2025.pdf |
| Index share 93.3%, record $39.0tn ($36.4tn 2022, $28.1tn 2023) | CONFIRMED | Verbatim in the note. | same |
| Single-name peaked at $3.3tn in 2023, fell to $2.8tn in 2025 | CONFIRMED | "peaked at $3.3 trillion in 2023 ... easing to $2.8 trillion in 2025". | same |
| CDX.NA.IG 43.4% of 2025 index activity, iTraxx Europe 32.4%, CDX.NA.HY 10.4%, iTraxx Crossover 7.7% | CONFIRMED | Verbatim. | same |
| CDX.NA.IG 500-900 trades a day, more than 900 in Q2 2025 | CONFIRMED | "typically trading between 500 and 900 times a day and exceeding 900 times in the second quarter of 2025". | same |
| Q1 2020 index activity 78.1% above trailing average | CONFIRMED | "increased by 78.1% relative to its trailing four-quarter average". | same |
| Q2 2025: index +20.9%, single-name -20.7% | CONFIRMED | Verbatim (tariff shock, April 2025). | same |
| H1 2026 activity $27.4tn, up 27.8% year on year | CONFIRMED | "$27.4 trillion, up by 27.8% from $21.5 trillion a year earlier". | same |
| More than 99% of the three benchmark indices cleared; SEF share 96.5-98.0% in H1 2025 | CONFIRMED (scope note) | SwapsInfo H1 2025: "Over 99% of traded notional in CDX HY, CDX IG and iTraxx Europe was cleared"; SEF share 97.6% (CDX HY), 98.0% (CDX IG), 96.5% (iTraxx Europe). Across all US-reported index credit derivatives, clearing was 79.1% and SEF share 76.8%, so "close to universal" holds for the three benchmarks only. | https://www.isda.org/a/4cpgE/SwapsInfo-First-Half-of-2025-and-the-Second-Quarter-of-2025.pdf |
| Clarus: cleared USD CDX $3.94tn in March 2026, up 46% year on year | CONFIRMED | "CDX were $3.94 trillion - up 46 percent YoY and up 35 percent HoH." Clarus article of 10 June 2026. | https://www.clarusft.com/us-firms-powered-march-2026-itraxx-swaps-volume-growth/ |
| Cboe iBoxx credit futures block trades topped $1bn a month for a second month in Aug 2026; IBIG block activity overtook IBHY for the first time (The DESK, 16 Oct 2026) | CONFIRMED (sponsored) | "topped $1 billion in a single month for the second consecutive time in August"; "In August 2026, IBIG futures block trade activity overtook IBHY futures block trade activity for the first time". The article is labelled sponsored content from Cboe. | https://www.fi-desk.com/cboe-block-trading-has-arrived-in-credit-index-futures-2/ |

### Box 10.2: CTAs, speed, and crowding, 2024-2026

| claim | verdict | evidence / correct figure | source |
| :--- | :--- | :--- | :--- |
| SG quote: CTAs "showcase a level of adaptability akin to the Kardashians" | CONFIRMED | Verbatim in SG's May 2025 CTA Industry Update. | https://content.sgmarkets.com/CTA_UPDATE_KEEPING_UP_WITH_THE_TRENDFOLLOWERS_2025 |
| SG Trend Index -4.9% in April 2025, -9.3% YTD | CONFIRMED | "loss of -4.9% in April, leaving it down -9.3% YTD". | same |
| 12-month return to 30 Apr 2025 of -18.6% | CONFIRMED | "To 30 April 2025, the rolling 12-month return for trend following is -18.6%." | https://www.man.com/insights/is-this-time-different |
| "a 12-month loss deeper than 15% had happened only twice before" | CORRECTED | Man: "only twice has the Societe Generale (SG) Trend index lost more than 15% over rolling 12-month windows", with "the previous worst return at -16.0%, occurring in January 2019"; the chart's red bar "includes current drawdown". So the two occurrences include the 2025 episode, which leaves one earlier one. Man does not spell out the count; this is the natural reading. | https://www.man.com/insights/is-this-time-different |
| AlphaSimplex: peak-to-trough -21.8% from 15 Apr 2024 to 14 May 2025 (Kaminski and Wen, June 2025) | CONFIRMED | Table 1, "Liberation day": start 4/15/2024, end 5/14/2025, magnitude -21.8%. | https://www.alphasimplex.com/assets/files/2025.06---market-cycles-and-managed-futures---kaminski-and-wen.pdf |
| Cambridge Associates: -20.4% May 2024 to May 2025, second-largest drawdown since 2000 | CONFIRMED | "declining 20.4% from May 2024 through May 2025"; "second largest drawdown since inception in 2000" (SG Trend Index; article dated 19 Aug 2025). | https://www.cambridgeassociates.com/insight/does-trend-followings-recent-struggle-signal-that-the-strategy-is-structurally-broken/ |
| Full-year 2025: SG Trend +2.39% vs S&P 500 TR +17.89% (Top Traders Unplugged, 23 Jan 2026) | CONFIRMED | TTU December 2025 report, byline 23 January 2026: SG Trend +2.39%, S&P 500 TR +17.89% (trailing 12 months through December). | https://www.toptradersunplugged.com/trend-following-performance-report-december-2025/ |
| 2026: +10.13% YTD by end-April | UNVERIFIABLE (not fetched) | TTU April 2026 report not fetched within the call budget. Cross-check: TTU's July report gives +7.90% YTD at end-July and the August report +11.07% at end-August, which are consistent with a path through +10.13%. Hedge: "about +10% year to date by end-April (Top Traders Unplugged)". | https://www.toptradersunplugged.com/trend-following-performance-report-april-2026/ |
| HY OAS peaked at only 3.46% on 30 March 2026 | CONFIRMED | FRED BAMLH0A0HYM2: 2026 maximum 3.46 on 2026-03-30. | FRED BAMLH0A0HYM2 |
| +11.07% YTD at end-August 2026 | CONFIRMED | "The year-to-date figure climbed to 11.07 percent from 7.90 percent" (report of 22 Sep 2026; August return +2.94%). | https://www.toptradersunplugged.com/trend-following-performance-report-august-2026/ |
| July 2026: SG Trend -1.12%; programs "largely positioned the same way" | CONFIRMED | "declined 1.12 percent in July"; breadth across 51 programs "offered little shelter because the programs were largely positioned the same way" (report of 21 Aug 2026). Note the quote sits in the compiler's TF Index section. | https://www.toptradersunplugged.com/trend-following-performance-report-july-2026/ |
| SG: 2024 pairwise correlation of index constituents 0.78 | CONFIRMED | "The average pairwise correlation between the constituents of the SG Trend Index in 2024 was 0.78, but the range of returns was nearly 15%". | SG CTA update (above) |
| Man: correlation was 0.87 before 2007 | CONFIRMED | Man Group deep dive: 0.87 average over 2000-2006, falling to 0.78 from 2007 onwards (data to Dec 2024). Note Man's 0.78 is a post-2007 average, a separate number from SG's 2024 value. | https://www.man.com/insights/deep-dive-trend-following |
| SG: since 2007 the index "behaves more like a much slower model"; faster models "delivered the best hypothetical returns" in 2020 | CONFIRMED | Verbatim in SG update. | SG CTA update |
| Man: adding alternative markets "such as power, synthetic credit indices and interest rate swaps" improved performance, more so for slower systems | CONFIRMED | Man: alternative markets "such as power, synthetic credit indices and interest rate swaps"; "additivity of alternative markets more apparent in slower trend systems". | https://www.man.com/insights/deep-dive-trend-following |
| SG cites industry AUM of about $340bn (BarclayHedge, Q4 2024) | CONFIRMED | "industry AUM estimated around $340b", footnote "Backstop BarclayHedge 2024 Q4 as of 13 May 2025". | SG CTA update |
| Man AHL $39.4bn of trend-following AUM across "900+ traditional and alternative markets" at 30 June 2026 | UNVERIFIABLE (not fetched) | man.com/trend-following not fetched within the call budget. Hedge: "about $39bn (Man AHL, mid-2026)". | https://www.man.com/trend-following |
| HY OAS in a tight band 2.59-4.61% over 2024-2026 | CONFIRMED | FRED: low 2.59% (2025-01-22), high 4.61% (2025-04-07) within 2024-2026. | FRED BAMLH0A0HYM2 |

## Chapter 11 (11_ch11_defensive_systematic_high_yield.md): three boxes

### Box 11.1: The Whipsaw Years, 2022-2026

| claim | verdict | evidence / correct figure | source |
| :--- | :--- | :--- | :--- |
| 2022 US HY "down over 11%"; 2023 "up over 13%" (BlackRock p.3, Bloomberg data as of 31 Mar 2024) | CONFIRMED | p.3: "U.S. high yield was down over 11%" (2022) and "up over 13%" (2023); footnote "Source: Bloomberg, as of March 31, 2024". | source_pdfs/BlackRock_Systematic_High_Yield_Credit.pdf p.3 |
| Average manager beat benchmark by 0.47% in 2022, lagged by 0.68% in 2023 | CONFIRMED | p.4: "outperformed their benchmark by 0.47%"; "underperformed their benchmark by -0.68%". | BlackRock p.4 |
| 2024: +0.35% vs benchmark in Q1, -0.37% over the rest of the year | CONFIRMED | p.5: "+0.35% in the first quarter of 2024, but underperformed by -0.37% for the remainder of 2024". | BlackRock p.5 |
| ICE BofA US HY total return +8.20% in 2024 and +8.50% in 2025 | CONFIRMED | Recomputed from BAMLHYH0A0HYM2TRIV: +8.20% and +8.50%. | FRED BAMLHYH0A0HYM2TRIV |
| Fell 3.83% from 28 Feb to 7 Apr 2025; regained prior peak on 12 May 2025 ("ten-week V") | CONFIRMED | -3.83% (2025-02-28 to 2025-04-07); first close at or above the 28 Feb level is 2025-05-12 (10.4 weeks after the peak). | FRED BAMLHYH0A0HYM2TRIV |
| 2026: fell 2.87% from 27 Aug to 1 Oct; +0.15% YTD on 15 Oct | CONFIRMED | -2.87% (2026-08-27 to 2026-10-01, the 2026 maximum drawdown); YTD +0.15% to 2026-10-15. | FRED BAMLHYH0A0HYM2TRIV |

### Box 11.2: The Soft-Default Regime, 2024-2026

| claim | verdict | evidence / correct figure | source |
| :--- | :--- | :--- | :--- |
| S&P: US trailing-12-month speculative-grade default rate 5.1% in Dec 2024 | UNVERIFIABLE | S&P pages were not retrieved (the box itself flags this). Hedge: "S&P put the US trailing-12-month speculative-grade default rate near 5% at the end of 2024". | n/a |
| S&P: distressed exchanges about 68% of 2025 defaults through April, highest YTD share since 2008 | UNVERIFIABLE | Not confirmed. A search summary of S&P's April 2025 default outlook reports distressed exchanges at 62% of defaults in Q1 2025. Hedge: "S&P put distressed exchanges at well over 60% of defaults in early 2025". | https://www.spglobal.com/ratings/en/research/articles/250416-default-transition-and-recovery-trade-tensions-could-reverse-decline-in-corporate-defaults-13473883 |
| Moody's: distressed exchanges 65% of all corporate defaults in 2025 | CONFIRMED | "in 2025, roughly 65% of all corporate defaults were distressed restructurings" (Moody's Analytics, 18 May 2026); "approximately 65% of all defaults in 2025" (28 Apr 2026). Note The DESK paraphrases the same number as "65% of private credit defaults", which is a misreading. | https://www.moodys.com/web/en/us/insights/credit-risk/private-credit/lend-extend-and-then.html ; https://www.moodys.com/web/en/us/insights/credit-risk/private-credit/us-corporate-default-risk-in-2026.html |
| Average forward one-year PD for US HY companies 3.2% in Q1 2026 (Moody's Analytics, 18 May 2026) | CONFIRMED | "As of Q1 2026, the average forward-looking one-year probability of default for U.S. high-yield companies has eased to 3.2%." Page dated May 18, 2026. | Moody's "Lend, extend, and then..." (above) |
| Fitch forecast 2026 default rates of 2.5-3.0% (US HY) and 4.5-5.0% (US leveraged loans) (Investment Executive, 3 Dec 2025) | CONFIRMED | "high yield issuers will be between 2.5% and 3%"; "leveraged loans will be in the range of 4.5% to 5% by the end of 2026". Article dated December 3, 2025. | https://www.investmentexecutive.com/news/u-s-leveraged-loan-defaults-to-ease-in-2026-fitch/ |
| Fitch US private credit default rate hit a record 6% in April 2026 (The DESK, 27 May 2026) | CONFIRMED | "Fitch Ratings reported in May 2026 that the US private credit default rate reached a record 6% in April". Article by Dan Barnes dated May 27, 2026. | https://www.fi-desk.com/defaults-creep-higher-in-leveraged-credit-markets/ |
| UBS: 2025 USD HY default expectation 4.8%, 3.1% excluding two large distressed capital structures (UBS AM, 17 Jan 2025) | CONFIRMED | "USD high yield defaults expected to be 4.8%"; "Excluding these special situations, the default forecast comes in at 3.1%". Dated 17 Jan 2025. | https://www.ubs.com/us/en/assetmanagement/insights/asset-class-perspectives/fixed-income/articles/2025-fixed-income-default-study.html |
| "any PD model trained on hard defaults alone is calibrated to a world in which two-thirds of today's defaults would have counted as survival" | CONFIRMED (consistent) | Consistent with Moody's 65% share. | Moody's, above |

### Box 11.3: Electronic HY and the Systematic Share, 2019-2026

| claim | verdict | evidence / correct figure | source |
| :--- | :--- | :--- | :--- |
| Man Numeric moved from roughly 30% of HY and 60% of IG order flow on electronic venues to over 90% of order flow by May 2023 | CONFIRMED | p.3: "from having roughly 30% of our order flow in high yield and 60% in investment grade going through electronic venues, to over 90% of our order flow going through electronic trading venues"; footnote "Source: Man Numeric; as of 1 May 2023". | source_pdfs/Man_Revolutions_in_Credit_Trading_2023.pdf p.3 |
| Total US corporate bond ADV $66.7bn through Sept 2026, +13.4% y/y | CONFIRMED | SIFMA: "Trading (through September) $66.7 billion ADV, +13.4% Y/Y". | https://www.sifma.org/resources/research/statistics/us-corporate-bonds-statistics/ |
| $12.1tn outstanding at 2Q26 (SIFMA page dated 14 Oct 2026) | CONFIRMED | "Outstanding (as of 2Q26) $12.1 trillion, +4.2% Y/Y"; page published October 14, 2026. | same |
| Blackstone systematic credit platform manages more than $40bn across IG, HY and EM | CONFIRMED | Blackstone p.1: "over $40 billion in assets under management ... liquid investment-grade, high-yield, and emerging market portfolios". | source_pdfs/Blackstone_Systematic_Credit.pdf p.1 |
| HYDB launched July 2017 | CONFIRMED | Inception July 11, 2017. | https://stockanalysis.com/etf/hydb/ |
| HYDB held $1.52bn at a 0.35% expense ratio (checked 17 Oct 2026) | CONFIRMED | AUM $1.52B, expense ratio 0.35%, last checked Oct 17, 2026 (aggregator). | same |
| HYDB "selected and weighted by default probability, default-adjusted spread, and volatility" | UNVERIFIABLE (not fetched) | Index methodology not retrieved. Hedge: "selected and weighted by a systematic default-risk model". | n/a |

## Chapter 12 (12_ch12_multi_asset_credit_allocation.md): four boxes

Federal Reserve Financial Stability Reports (May 2026 and November 2025) were downloaded as PDFs and searched as text.

### Box 12.1: The HY Index That Stopped Growing (2004-2026)

| claim | verdict | evidence / correct figure | source |
| :--- | :--- | :--- | :--- |
| Fridson: HY index face value about $1.4tn in April 2025, essentially unchanged over ten years | CONFIRMED | "On our April 17, 2025 observation date, the ICE BofA US High Yield Index's total face amount was $1.4 trillion, unchanged from 10 years earlier." | https://rpc.cfainstitute.org/blogs/enterprising-investor/2025/think-weve-seen-the-last-1000-bps-high-yield-spread-think-again |
| BB share 53.55% against a 1996-2024 average of 44.53% (CFA Institute Enterprising Investor, June 2025) | CONFIRMED | 53.55% on April 17, 2025; 44.53% average, 31 Dec 1996 to 31 Dec 2024. Post dated 2 June 2025. | same |
| Nuveen: 51% BB at year-end 2024 against 37% in 2004 | CONFIRMED | Nuveen p.4: "At year-end 2024, 51% of the index was rated BB, compared to 37% in 2004". | source_pdfs/Nuveen_Multi_Asset_Credit_Quant_Framework.pdf p.4 |
| Institutional leveraged loans $1,549bn at 2025Q4 (9.2% growth over the year) | CONFIRMED | Fed FSR May 2026 table: leveraged loans 1,549, growth 9.2%; "data extend through 2025:Q4"; note says the figure is institutional leveraged loans. | https://www.federalreserve.gov/publications/files/financial-stability-report-20260508.pdf |
| HY and unrated bonds $1,772bn | CONFIRMED | Same table: 1,772 (growth 4.7%). | same |
| Private credit about $1.4tn, "about one-third of total below-investment-grade debt, excluding bank loans" | CONFIRMED | Box 4.1: "about $1.4 trillion, or 10 percent, of the total debt of U.S. nonfinancial corporations, or about one-third of total below-investment-grade debt, excluding bank loans" (latest data, second half of 2025). | same |

### Box 12.2: The 2026 CCC Decompression

| claim | verdict | evidence / correct figure | source |
| :--- | :--- | :--- | :--- |
| CCC OAS 7.46% (YE 2024), 8.85% (YE 2025), 12.78% on 15 Oct 2026, a post-2023 high | CONFIRMED | FRED: 7.46, 8.85, 12.78; the window maximum is 12.82% on 14 Oct 2026, so 12.78% is the second-highest print, "post-2023 high" holds. | FRED BAMLH0A3HYC |
| BB OAS 1.86%, 1.69%, 1.97%; overall HY OAS 3.23% | CONFIRMED | 1.86 (2024-12-31), 1.69 (2025-12-31), 1.97 (2026-10-15); HY 3.23 (2026-10-15). | FRED BAMLH0A1HYBB, BAMLH0A0HYM2 |
| CCC/BB ratio 4.0, 5.2, 6.5; CCC-BB gap 560, 716, 1,081 bp | CONFIRMED | 4.01, 5.24, 6.49; gaps 560, 716, 1,081 bp. | FRED |
| YTD total returns to 15 Oct 2026: CCC -5.21%, BB +0.33%, HY +0.15% | CONFIRMED | -5.21%, +0.33%, +0.15%. | FRED BAMLHYH0A3CMTRIV, BAMLHYH0A1BBTRIV, BAMLHYH0A0HYM2TRIV |
| 10-year Treasury yield 5.10% | CONFIRMED | DGS10 = 5.10 on 2026-10-15. | FRED DGS10 |
| Effective fed funds from 3.62% (May 19) to 3.88% (Sept 17) | CONFIRMED | DFF 3.62 (2026-05-19), 3.88 (2026-09-17). | FRED DFF |
| Fed May 2026 FSR: software the largest sector in private-credit portfolios; secondary leveraged-loan spreads rose, "reflecting a high concentration of leveraged loan borrowers in the software industry" | CONFIRMED | Box 4.1: "The software sector had become the largest sector in private credit portfolios"; ch.1: spread "increased moderately, reflecting a high concentration of leveraged loan borrowers in the software industry". The report says "increased moderately". | Fed FSR May 2026 |

### Box 12.3: Private Credit's First Redemption Cycle

| claim | verdict | evidence / correct figure | source |
| :--- | :--- | :--- | :--- |
| Semi-liquid vehicles $425bn gross ($241bn net), about 20% of private-credit vehicle net assets | CONFIRMED | "semi-liquid funds account for $425 billion in gross assets and $241 billion in net assets, or about 20 percent of net assets under management in private credit vehicles". | Fed FSR May 2026, Box 4.1 |
| Perpetual-life BDCs $306bn gross ($161bn net); interval funds $119bn gross ($80bn net) | CONFIRMED | Verbatim; the parts sum to the totals (306+119, 161+80). | same |
| Redemption requests "accelerated further in the first quarter of 2026, when a number of funds received requests that were much larger than 5 percent of NAV"; most managers capped at 5% | CONFIRMED | Verbatim ("5 percent of NAV"; "Most managers chose to cap redemptions at 5 percent of NAV"). | same |
| "accepted redemption requests somewhat exceeded new inflows in the first quarter of 2026, the first time this has occurred since these vehicles were created" | CONFIRMED | Verbatim. | same |
| Nov 2025 report judged the First Brands and Tricolor bankruptcies to "so far appear to be isolated events" while noting "unexpected losses could arise from opaque off-balance-sheet funding arrangements" | CONFIRMED (naming note) | Quotes are verbatim, but the report does not name the firms: it says "two privately held firms, an auto parts supplier and a subprime auto lender". Naming them is the book's inference. Report dated November 2025 (file 20251107). | https://www.federalreserve.gov/publications/files/financial-stability-report-20251107.pdf |
| "a 1.9% volatility" for a BDC sleeve | OUT OF SCOPE | Model parameter internal to the chapter, not a sourced fact. | n/a |

### Box 12.4: April 2025 as a Transition Test

| claim | verdict | evidence / correct figure | source |
| :--- | :--- | :--- | :--- |
| "a regime transition in about 25 trading days" | CORRECTED (imprecise) | 26 trading days fits the HY total-return peak-to-trough (28 Feb to 7 Apr 2025). The OAS move quoted in the next sentence (22 Jan to 7 Apr) spans 52 trading days, and OAS first crossed 3.0% on 10 March. Replacement wording below. | FRED BAMLH0A0HYM2 |
| HY OAS from 259 bp (22 Jan) to 461 bp (7 Apr) | CONFIRMED | 2.59% and 4.61%. | FRED BAMLH0A0HYM2 |
| Peak-to-trough total returns: HY -3.83% (28 Feb to 7 Apr), CCC -7.80%, B -4.21%, BB -2.83%, IG -3.03% (3 Mar to 11 Apr), EM corporate -2.37%, EM HY corporate -3.79% | CONFIRMED | Series maximum drawdowns in H1 2025: HY -3.83%, CCC -7.80%, B -4.21%, BB -2.83%, IG -3.03% (3 Mar to 11 Apr), EM -2.37%, EM HY -3.79%. Each series has its own peak and trough dates; only HY and IG dates are given in the box. | FRED BAMLHYH0A0HYM2TRIV, ...3CMTRIV, ...2BTRIV, ...1BBTRIV, BAMLCC0A0CMTRIV, BAMLEMCBPITRIV, BAMLEMHBHYCRPITRIV |
| HY mutual funds and ETFs: -$10.9bn flows in April, +$18.5bn May to September | CONFIRMED | MacKay: "in April, retail investors pulled $10.9 billion from U.S. high yield mutual funds and ETFs, according to J.P. Morgan ... from May through September ... $18.5 billion". | https://www.nylim.com/mackay-shields/insights/specialty-fixed-income-outlooks-4q25/high-yield-4q-2025-outlook |
| End-Sept 2025 HY spread-to-worst 299 bp, "22 bps wider than the post-2008 tights earlier in 2025", after 12 straight quarterly gains, longest since 1997 | CORRECTED (quote wording) | Facts match: 299 bps; 12 consecutive quarters, longest since 1997. The source wording is "only 22 bps wider than the post-2008 tights reached earlier in 2025"; the box's quotation drops "reached". Replacement below. | MacKay Shields 4Q 2025 HY Outlook (above) |

## Chapter 13 (13_ch13_codifying_lmt_game_theory.md): two boxes

The Wachtell Lipton memo (3 Feb 2026) and the Fed reports were downloaded as PDFs and searched as text; the Harvard, Octus and 9fin pages were fetched as HTML and searched as text.

### Box 13.1: The strike moved, and so did the volume

| claim | verdict | evidence / correct figure | source |
| :--- | :--- | :--- | :--- |
| Buccola and Nini: 600+ leveraged loan agreements, 2016-2022 | CONFIRMED | "A comprehensive review of over 600 leveraged loan agreements from 2016 to 2022". | https://bankruptcyroundtable.law.harvard.edu/2025/04/08/the-loan-market-response-to-dropdown-and-uptier-transactions/ |
| "prior to 2020, only 40% of loans restricted uptiers, often inadvertently"; "by mid-2022, 85% of new loans explicitly blocked uptiers, with 70% requiring unanimous lender consent for subordination" (HLS Roundtable, 8 Apr 2025) | CONFIRMED | Verbatim; page dated April 8, 2025. The Journal of Legal Studies 53:489 (2024) citation is not on the page and was not checked. | same |
| Octus counted 11 non-pro-rata uptiers from March 2022 to July 2024 (Octus, 16 July 2024) | CONFIRMED | "Reorg analyzed 11 non-pro-rata uptier transactions dating back to March 2022"; article dated Jul 16, 2024. | https://octus.com/resources/articles/reorgs-analysis-of-11-non-pro-rata-uptiers/ |
| Wesco, Mitel and Robertshaw moved 100% of value away from non-ad-hoc creditors | CONFIRMED | "Wesco, Mitel and Robertshaw resulted in the most transferred value, with creditors not in the ad hoc group transferring 100% of their value". | same |
| Six most recent moved an average of 18% (Apex 38%, Valcour 12%, EyeCare 13%, GoTo 13%) | CONFIRMED | "The six most recent transactions move an average of 18% of value away from non-ad-hoc creditors ... Apex Tool ... 38% ... Valcour ... 12% ... EyeCare Partners and GoTo Group ... 13%". Only four of the six are named in the box. | same |
| LMEs hit a high-water mark of 38 in 2024 and fell to 24 in 2025 | CONFIRMED | "24, compared to a high-water mark of 38 in 2024". | Wachtell, Liability Management 2026: For Better or Worse, 3 Feb 2026, https://www.wlrk.com/FirmMemos/WLRK/WLRK.29921.26.pdf |
| About two-thirds of default activity by issuer count in 2025; exceeded both payment defaults and bankruptcies on a rolling 12-month basis in every month of 2025 | CONFIRMED | "LMEs still accounted for two-thirds of default activity by issuer count in 2025 and exceeded both payment defaults and bankruptcies on a rolling 12-month basis for each month of 2025". | same |
| H1 2026: 25 LMEs closed vs 24 in H1 2025; "the coercive uptier structures that defined 2025 have all but vanished", replaced by equity handovers and consensual amend-and-extends (9fin, 28 Aug 2026) | CONFIRMED (date not shown) | 9fin: "25 completed LMEs in the first half of 2026, marginally ahead of the 24 recorded in H1 2025 ... equity handovers and consensual amend-and-extends now dominate, while the coercive uptier structures that defined 2025 have all but vanished". The retrieved page text shows no publication date. | https://9fin.com/insights/h1-2026-lme-update |

### Box 13.2: From auctions to bargaining, 2024-2026

| claim | verdict | evidence / correct figure | source |
| :--- | :--- | :--- | :--- |
| Within a month of the Fifth Circuit's Serta ruling the market had "amend-extend-and-exchange", "deployed throughout 2025" | CONFIRMED | "Less than a month after Serta, a new technique hit the market"; "Transaction structures of this ilk were deployed throughout 2025". | Wachtell memo (above) |
| Deals away returned (Optimum/Altice USA, Altice International, Liberty Puerto Rico, KIK), often with six-month par calls | CONFIRMED | "deals away ... by Optimum Communications (f/k/a Altice USA), Altice International, Liberty Puerto Rico, and KIK"; "A number of recent deals away have included six-month par call rights". | same |
| 25 LMEs in H1 2026 vs 24 in H1 2025; "all but vanished" (9fin, 28 Aug 2026) | CONFIRMED (date not shown) | See Box 13.1. | https://9fin.com/insights/h1-2026-lme-update |
| Fed FSR of 7 Nov 2025: volume-weighted leveraged-loan default rate "stayed well below its historical median"; defaults including distressed exchanges "continued to be elevated relative to history" | CONFIRMED | Verbatim ("The volume-weighted default rate on leveraged loans stayed well below its historical median"; "continued to be elevated relative to history"). Report file dated 2025-11-07. | https://www.federalreserve.gov/publications/files/financial-stability-report-20251107.pdf |
| May 8, 2026 report repeated the point | CONFIRMED (wording note) | May 2026: "the volume-weighted default rate on leveraged loans stayed below its historical median, defaults including distressed exchanges ... remained relatively high". The wording is softer ("below", not "well below"; "relatively high", not "elevated relative to history"). | https://www.federalreserve.gov/publications/files/financial-stability-report-20260508.pdf |
| May 2026: in private credit "the elevated usage of payment-in-kind (PIK) provisions indicates some borrowers may face repayment difficulties" | CONFIRMED | Verbatim. | same |
| "$580 billion of loans and $625 billion of high-yield bonds mature between 2027 and 2029" (Wachtell) | CONFIRMED | Verbatim. | Wachtell memo |

## Chapter 14 (14_ch14_default_and_recovery_cycle_lmt_era.md): three boxes

### Box 14.1: The soft-default takeover, 2010-2026

| claim | verdict | evidence / correct figure | source |
| :--- | :--- | :--- | :--- |
| S&P: distressed exchanges about 32% of rated US corporate defaults 2010-2023, then roughly 50% for three consecutive years to mid-2024 (S&P, 15 Aug 2024, via FTI Consulting, 9 Oct 2026) | UNVERIFIABLE | Neither the S&P report nor the FTI piece was retrieved (the box itself says the S&P original could not be opened). Partial corroboration: a JPMorgan note reported in May 2024 put distressed exchanges at half of 2024 default volume to date. Hedge: "S&P counted distressed exchanges at roughly one-third of US defaults over 2010-2023 and about half in the years to mid-2024 (as cited by FTI Consulting)". | https://www.kitco.com/news/off-the-wire/2024-05-02/us-high-yield-spreads-still-tight-despite-pick-distress |
| 2024: distressed exchanges about 63% of Moody's-rated defaults, "the highest annual share on record, with data going back to the 1980s" (Moody's AMR, 6 Mar 2025) | UNVERIFIABLE | Moody's AMR of 6 March 2025 not retrieved. Moody's May 2026 note has a chart of annual distressed-exchange share but no extractable number. Hedge: "roughly three in five Moody's-rated defaults, a record share". | https://www.moodys.com/web/en/us/insights/credit-risk/private-credit/lend-extend-and-then.html |
| LMT counts hit a high-water mark of 38 (Wachtell, 3 Feb 2026) | CONFIRMED | See Box 13.1. | Wachtell memo |
| H1 2025: 64% of defaults, "about the same pace as all of 2024", concentrated in loan-only PE-backed structures (Moody's AMR, 7 Aug 2025) | UNVERIFIABLE | Moody's AMR of 7 August 2025 not retrieved. Hedge: "about 60% of defaults in the first half of 2025, similar to 2024 (Moody's)". | n/a |
| 2025: about 65% of all defaults were distressed restructurings (Moody's, 28 Apr 2026) | CONFIRMED | "Distressed restructurings accounted for approximately 65% of all defaults in 2025"; page dated April 28, 2026. | https://www.moodys.com/web/en/us/insights/credit-risk/private-credit/us-corporate-default-risk-in-2026.html |
| LME counts fell to 24; LMEs about two-thirds of default activity; exceeded payment defaults and bankruptcies every month (Wachtell, 3 Feb 2026) | CONFIRMED | See Box 13.1. | Wachtell memo |
| Moody's direct-lending proxy: default rate 1.6% excluding distressed exchanges, 4.7% including them | CONFIRMED | "a proxy default rate for private credit (direct lending) that ranges from 1.6% (without distressed exchanges) to 4.7% (including them)". | Moody's, 18 May 2026 (URL above) |
| Fed May 2026 FSR: defaults including distressed exchanges "remained relatively high" while volume-weighted loan default rates sat below their median | CONFIRMED | Verbatim in ch.2. | Fed FSR May 2026 |
| 9fin: 25 completed LMEs in H1 2026 vs 24 in H1 2025 (28 Aug 2026) | CONFIRMED (date not shown) | See Box 13.1. | https://9fin.com/insights/h1-2026-lme-update |

### Box 14.2: The re-default ledger, 2020-2026

| claim | verdict | evidence / correct figure | source |
| :--- | :--- | :--- | :--- |
| Of 1,173 soft-event borrowers since 1979, about one in four hard-defaulted and more than 70% of those did so within two years (Moody's, 18 May 2026) | CONFIRMED | "the 1,173 unique borrowers that experienced a soft credit event ... from 1979 to 2026"; "about one in four soft credit events ultimately ends in hard default"; "More than 70% of eventual hard defaults ... occur within the first two years". | https://www.moodys.com/web/en/us/insights/credit-risk/private-credit/lend-extend-and-then.html |
| About 46% of 2023 distressed exchanges had re-defaulted by April 2025, most in under a year, against a historical average of about 3.5 years (Moody's via Bloomberg Law, 23 Apr 2025) | CONFIRMED | "About 46% of the distressed exchanges that took place in 2023 have already re-defaulted"; "Most ... re-defaulted in less a year, compared with the historic average of 3.5 years". Article dated April 23, 2025. The paywalled text did not show whether repeat exchanges count as re-defaults. | https://news.bloomberglaw.com/bankruptcy-law/distress-exchange-leads-to-re-default-half-the-time-moodys |
| "That figure counts repeat exchanges as re-defaults" | UNVERIFIABLE | Definition not visible behind the paywall; Moody's May 2026 note counts "another distressed credit event" as a repeat event. Hedge: "reportedly counts repeat exchanges". | n/a |
| 89 coercive non-pro-rata LMEs: fewer than half avoided bankruptcy or re-default within one year, only 22% within two | CONFIRMED | "hand-collected dataset of 89 coercive, non-pro rata LMEs"; "Within one year of an LME, fewer than half avoided bankruptcy or re-default; within two years, only 22% avoided both." | Roe and Rotaru, HLS Bankruptcy Roundtable, https://bankruptcyroundtable.law.harvard.edu/2026/02/24/liability-managements-limited-runway-corporate-restructuring-today/ |
| Of firms with at least two years of history, 56% had filed; LME debtors spent two to three times longer in bankruptcy than prepackaged cases | CONFIRMED | "Among firms with at least two years of post-LME history, 56% had already filed for bankruptcy"; "two-to-three times longer in bankruptcy than non-LME prepacks or PE-backed debtors". | same |
| CLO view: after an LME 33% of issuers filed, 56% re-defaulted or were rated CCC+ or below, 10% repaid or reached B- or better (S&P BSL CLO research via Wellington, 1 Apr 2026) | UNVERIFIABLE | Wellington page not retrieved; the box already labels it secondary. Hedge: "S&P CLO research, as relayed by Wellington, finds that roughly a third of issuers filed after an LME". | n/a |
| Serta: uptier closed 22 June 2020, Chapter 11 on 23 Jan 2023, about 31 months | UNVERIFIABLE (consistent) | Search results confirm a Serta Simmons filing in S.D. Texas on a Monday; 23 Jan 2023 was a Monday. Docket not accessed. The interval 22 Jun 2020 to 23 Jan 2023 is 31 months. | https://coleschotz.com/wp-content/uploads/2023/01/Serta-Simmons-Petition.pdf |
| Mitel: uptier October 2022, Chapter 11 on 10 March 2025, about 29 months | UNVERIFIABLE | A Bloomberg item of 4 March 2025 said Mitel was preparing to file "as soon as next week"; a search summary hinted at April but its dates were inconsistent. Docket not accessed. Hedge: "Chapter 11 in March 2025". Arithmetic holds for March (29 months). | https://www.bloomberg.com/news/articles/2025-03-04/telecommunications-firm-mitel-prepares-to-file-for-chapter-11 |
| Wesco/Incora: notes transaction March 2022, Chapter 11 on 1 June 2023, about 15 months | UNVERIFIABLE (consistent) | Octus dates the earliest of its 11 uptiers to March 2022 and discusses the Wesco/Incora bankruptcy; the 1 June 2023 petition date was not retrieved. | https://octus.com/resources/articles/reorgs-analysis-of-11-non-pro-rata-uptiers/ |
| Robertshaw: 2023 LME, Chapter 11 on 15 Feb 2024 | UNVERIFIABLE (consistent) | Octus: Robertshaw's "December 2023 payoff of Invesco's first-out loans"; a search found a Robertshaw Chapter 11 in early 2024 (page dated 23 Feb 2024) but not the exact day. | Octus (above) |
| Del Monte Foods: 2024 financing (August 2024), Chapter 11 on 1 July 2025, about 11 months | UNVERIFIABLE | No source retrieved for either date. Hedge: "Chapter 11 in July 2025". | n/a |

### Box 14.3: Co-ops, from four a year to forty-five

| claim | verdict | evidence / correct figure | source |
| :--- | :--- | :--- | :--- |
| About 45 co-op agreements in the US in 2024, against about four a year over 2018-2023, cited in Optimum's antitrust complaint (9fin) | CONFIRMED | "Around 45 co-op agreements were entered into in the US in 2024, up from an average of just four a year between 2018-2023. This statistic was cited in the original complaint filed in the Optimum antitrust proceedings." | https://www.9fin.com/insights/cooperation-agreement-crash-course |
| Offensive, defensive and carve-out variants, carve-out fastest-growing; equity reacts negatively and firm value rises modestly (Seaton, HLS, 14 Apr 2026) | CONFIRMED | "The fastest-growing variant is the Carveout Co-Op"; "The equity market reacts negatively in the immediate aftermath, firm value tends to rise modestly". Page dated April 14, 2026. The retrieved passage lists offensive and carve-out variants; "defensive" is inferred from the three-use framing. | https://bankruptcyroundtable.law.harvard.edu/2026/04/14/the-value-and-legality-of-lender-cooperation-agreements/ |
| "Anti-cartel" provisions in Warner Bros. Discovery's 2025 bonds; borrower NDAs "met significant market resistance" | CONFIRMED | "Anti-cartel provisions pioneered in the Warner Bros. Discovery 2025 bond issuance"; "Attempts by borrowers to suppress Co-Op formation have met significant market resistance". | same |
| CSC Holdings has about $21.8bn of debt | CONFIRMED | 8-K: CSC Holdings is obligor on "approximately $21.8 billion of secured debt, guaranteed notes and senior notes" as of March 31, 2026. | https://www.sec.gov/Archives/edgar/data/0001702780/000121390026063161/ea0292871-8k_optimum.htm |
| A June 2024 co-op claims about 99% of it | UNVERIFIABLE (partly) | Crowell and Debtwire summaries of the complaint: the "Cooperative" holds about 99% of Optimum's outstanding debt (an allegation). The June 2024 formation date was not confirmed, and the 8-K does not mention a co-op. | https://www.crowell.com/en/insights/client-alerts/optimums-shot-across-the-bow-an-antitrust-challenge-to-cooperation-agreements |
| "On 1 June 2026 Optimum moved Optimum East and its 50.01% Lightpath stake into an unrestricted Unsub Topco and raised $300mm of preferred (Optimum 8-K, 1 June 2026)" | CORRECTED (date) | The 8-K is filed and signed June 1, 2026 with "Date of Report ... June 1, 2026 (May 29, 2026)". The $300mm Series A Preferred Units were sold on May 29, 2026, not June 1. The 8-K names Unsub Topco and "CSC Holdings' interest in Cablevision Lightpath LLC" but gives no percentage; the 50.01% comes from Octus. Find/replace below. | 8-K (above); https://octus.com/?p=42278 |
| Q2 2026 10-Q going-concern warning; $4.12bn maturing April 2027 and $2.225bn July 2027 | UNVERIFIABLE | 10-Q not retrieved. A search found no going-concern language in the 8-K. Hedge: "Optimum's filings flag substantial near-term maturities (details to be checked in the Q2 2026 10-Q)". | n/a |
| Optimum and CSC Holdings sued the co-op lenders under the Sherman Act in S.D.N.Y., alleging price-fixing and a group boycott | CONFIRMED (venue not checked) | Crowell: complaint alleges "a group boycott and a price-fixing scheme"; suit filed November 2025 against Apollo, Ares, GoldenTree, Loomis, Oaktree and PGIM as "the Cooperative". The S.D.N.Y. venue was not shown in the summaries. | https://www.crowell.com/en/insights/client-alerts/optimums-shot-across-the-bow-an-antitrust-challenge-to-cooperation-agreements |
| Complaint alleges the co-op lenders hold 88% of a "Leveraged-Finance Market" it defines itself (Cleary Gottlieb, 18 Dec 2025) | CONFIRMED | Optimum alleges the Cooperative controls "approximately 88% of the entire leveraged finance market"; reported by Crowell and Debtwire. The Cleary memo "Cooperation, Not a Cartel" is dated December 18, 2025 (full text not read). | Crowell (above); https://ionanalytics.com/insights/debtwire/optimum-communications-claims-its-creditors-control-leveraged-finance-market-in-antitrust-attack-on-cooperation-agreement-legal-analysis/ |
| Defenses include rule-of-reason analysis, market definition and Sharon Steel v. Chase Manhattan (2d Cir. 1982) | UNVERIFIABLE (not fetched) | Legal argument summary; the case itself is a standard 2d Cir. 1982 citation (691 F.2d 1039). No change recommended. | n/a |
| Similar challenges (Optimum, Selecta) "in their early days" in early 2026 (Wachtell, 3 Feb 2026) | CONFIRMED | "Antitrust challenges in connection with cooperation agreements (Optimum and Selecta) are in their early days". | Wachtell memo |
| Baker McKenzie, Jan 2026: "a growing backlash against cooperation agreements" in 2025; non-pro-rata deals at Victoria PLC, Ardagh, Selecta and Hunkemoller | UNVERIFIABLE (not fetched) | Baker McKenzie leveraged finance report not retrieved (no figures involved). | https://www.bakermckenzie.com/en/insight/publications/2026/01/-/media/files/insight/publications/2026/01/lev-fin-annual-report-2026.pdf |

## Summary

Rows checked: 168 table rows (a row can bundle several figures, each of which was checked). Two rows are marked OUT OF SCOPE (internal model parameters, not sourced facts) and are not counted below.

| verdict | count |
| :--- | ---: |
| CONFIRMED | 137 |
| CORRECTED | 5 |
| STALE | 0 |
| UNVERIFIABLE | 24 |

By chapter (CONFIRMED / CORRECTED / STALE / UNVERIFIABLE): Ch8 17/1/0/4; Ch9 23/0/0/1; Ch10 26/1/0/2; Ch11 18/0/0/3; Ch12 21/2/0/0; Ch13 15/0/0/0; Ch14 17/1/0/14.

Method and limits. About 60 external fetches were used (two FRED CSV downloads, about 25 publisher pages or PDFs, about 10 searches, the rest 403/404 failures), which is over the 40-call guide because the Fed, ISDA, SG, Wachtell and FRED sources each settled many figures at once. Every FRED-based figure (rho, H, OAS levels, total returns, drawdowns, yields) was recomputed from FRED's own CSV download, and the Chapter 8 table was reproduced to two decimals. Claims citing the repo's own shelf (Dynkin, Man, BlackRock, Blackstone, Nuveen) were checked against `state/pdf_pages/`. Not reached: S&P and Moody's Ratings annual default reports, Wellington, Baker McKenzie, the Optimum 10-Q, ishares.com, bankruptcy dockets. The Ch14 UNVERIFIABLE count is high mainly for those reasons (Moody's AMR shares, S&P shares, five case dates).

### Find/replace pairs for CORRECTED items (apply in book_src; each FIND string occurs exactly once in the named file)

1. File `book_src/08_ch08_isolating_ido_and_empirical_duration.md` (Box 8.2, mixed dates)

FIND:
```
The CCC OAS reached 12.82% on October 14, 2026, while the broad HY OAS was 3.23% and IG 0.84% (computed 2026-10-17).
```
REPLACE:
```
The CCC OAS reached 12.82% on October 14, 2026 (HY 3.25%, IG 0.84% that day); on October 15 the CCC OAS was 12.78%, the broad HY OAS 3.23% and IG 0.84% (computed 2026-10-17).
```

2. File `book_src/10_ch10_trend_and_time_series_momentum.md` (Box 10.2, Man's "only twice" includes the 2025 episode; source: https://www.man.com/insights/is-this-time-different)

FIND:
```
a 12-month loss deeper than 15% had happened only twice before (Man Group, *Trend Following and Drawdowns: Is This Time Different?*)
```
REPLACE:
```
the index had lost more than 15% over a rolling 12 months only twice in its history, this episode and January 2019 at −16.0% (Man Group, *Trend Following and Drawdowns: Is This Time Different?*)
```

3. File `book_src/12_ch12_multi_asset_credit_allocation.md` (Box 12.4, 26 trading days is the Feb 28 to Apr 7 drawdown, not the Jan 22 to Apr 7 OAS move)

FIND:
```
*What happened:* a regime transition in about 25 trading days. The HY OAS moved from 259 bp (January 22) to 461 bp (April 7);
```
REPLACE:
```
*What happened:* a regime transition in about 26 trading days of drawdown (February 28 to April 7). The HY OAS moved from 259 bp (January 22) to 461 bp (April 7);
```

4. File `book_src/12_ch12_multi_asset_credit_allocation.md` (Box 12.4, quotation wording; source: MacKay Shields 4Q 2025 HY Outlook)

FIND:
```
"22 bps wider than the post-2008 tights earlier in 2025," after 12 straight quarterly gains, the longest run since 1997
```
REPLACE:
```
"only 22 bps wider than the post-2008 tights reached earlier in 2025," after 12 straight quarterly gains, the longest run since 1997
```

5. File `book_src/14_ch14_default_and_recovery_cycle_lmt_era.md` (Box 14.3, the $300mm preferred was sold 29 May 2026; the 8-K was filed 1 June 2026; source: https://www.sec.gov/Archives/edgar/data/0001702780/000121390026063161/ea0292871-8k_optimum.htm)

FIND:
```
On 1 June 2026 Optimum moved Optimum East and its 50.01% Lightpath stake into an unrestricted "Unsub Topco" and raised \$300mm of preferred (Optimum 8-K, 1 June 2026).
```
REPLACE:
```
In an 8-K filed on 1 June 2026, Optimum disclosed that it had moved Optimum East and its 50.01% Lightpath stake into an unrestricted "Unsub Topco", which sold \$300mm of preferred on 29 May 2026.
```

### STALE items

None found. Watch-list, not verified and not counted: ISDA SwapsInfo for H1 2026 (Box 10.1 cites H1 2025 clearing and SEF shares), Man Group's Q3 2026 trading statement (Box 10.2 cites Man AHL AUM at 30 June 2026), Top Traders Unplugged's September 2026 report (due after today), and any Fitch mid-2026 default-forecast update (Box 11.2 cites December 2025).

### Optional hedged wording for the main UNVERIFIABLE items (apply only if the editor does not re-source them)

6. File `book_src/08_ch08_isolating_ido_and_empirical_duration.md`

FIND:
```
It turned positive in 2021 and was roughly 0.58 for full-year 2022 and 2023 (approx.; same source).
```
REPLACE:
```
It turned positive in 2021 and was roughly 0.58 for full-year 2022 (approx.; secondary summaries of Morningstar's data, which differ on 2023).
```

7. File `book_src/08_ch08_isolating_ido_and_empirical_duration.md`

FIND:
```
it showed an effective duration of −0.01 years and net assets of about \$652mm, roughly 4% of HYG's size (ishares.com)
```
REPLACE:
```
it showed an effective duration near zero and net assets of about \$652mm, a small fraction of HYG's size (ishares.com)
```

8. File `book_src/09_ch09_factor_investing_in_credit.md`

FIND:
```
in a stress month it can jump fivefold overnight
```
REPLACE:
```
in a stress episode it can rise several-fold within months (Barclays IG LCS: 0.4% in 2007, 2.8% in 2008)
```

9. File `book_src/14_ch14_default_and_recovery_cycle_lmt_era.md`

FIND:
```
Mitel: uptier October 2022, Chapter 11 on 10 March 2025, about 29 months
```
REPLACE:
```
Mitel: uptier October 2022, Chapter 11 in March 2025, about 29 months
```

10. File `book_src/14_ch14_default_and_recovery_cycle_lmt_era.md`

FIND:
```
Del Monte Foods: a 2024 financing (reported as August 2024; terms not verified here), Chapter 11 on 1 July 2025, about 11 months
```
REPLACE:
```
Del Monte Foods: a 2024 financing (reported as August 2024; terms not verified here), Chapter 11 in July 2025, about 11 months (docket date not verified)
```

11. File `book_src/10_ch10_trend_and_time_series_momentum.md`

FIND:
```
+10.13% year to date by end-April
```
REPLACE:
```
about +10% year to date by end-April
```


<!-- STATUS: COMPLETE -->
