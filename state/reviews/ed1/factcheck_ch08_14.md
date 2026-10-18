# Edition 1 Fact-Check: Trend Watch boxes, Chapters 8-14

<!-- STATUS: IN PROGRESS -->

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

