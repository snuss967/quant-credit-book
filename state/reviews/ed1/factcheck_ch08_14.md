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

