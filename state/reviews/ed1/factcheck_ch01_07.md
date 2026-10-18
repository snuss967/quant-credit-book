# Fact-check: Trend Watch boxes, chapters 1-7

Checked 2026-10-18 against state/digests/trend_watch_boxes.md (boxes from 01_ch01 .. 07_ch07 only). No book_src file was edited.
Method: none of the boxes in chapters 1-7 cites a URL, so there was no cited URL to fetch first. Local primary PDFs in source_pdfs/ were checked where a box cites them (no web call); everything else via WebSearch/WebFetch (budget about 40 calls).
Verdicts: CONFIRMED / CORRECTED / STALE / UNVERIFIABLE.


Source key (short names used in the tables). All fetched or run on 2026-10-18.
- GW24 = Coalition Greenwich, "U.S. corporate bond trading in 2024 by the numbers", Jan 2025: https://coalitiongreenwich.crisil.com/content/dam/coalition-greenwich/MarketViews/2025/US-corporate-bond-trading-2024-numbers-25-C4001.pdf
- GW25 = Greenwich 2025 data spotlight: https://www.greenwich.com/market-structure-technology/us-corporate-bond-trading-2025-numbers
- FactBook = FINRA TRACE Fact Book 2017 (the timeline is unchanged in later editions): https://www.finra.org/sites/default/files/2017-trace-fact-book.pdf
- SEC-101121 = SEC Rel. 34-101121 (20 Sep 2024): https://www.sec.gov/files/rules/sro/finra/2024/34-101121.pdf
- FRED = FRED series BAMLH0A0HYM2 / BAMLH0A1HYBB / BAMLH0A2HYB / BAMLH0A3HYC, pulled as CSV and recomputed: https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLH0A0HYM2,BAMLH0A1HYBB,BAMLH0A2HYB,BAMLH0A3HYC
- EDGAR-FTS = SEC EDGAR full-text search API, https://efts.sec.gov/LATEST/search-index (q="liability management transaction", forms=8-K), re-run per calendar year
- Local PDFs (source_pdfs/, page text in state/pdf_pages/) are cited by file and page.
Method note: a verdict of CONFIRMED on a figure the book attributes to a news article (The DESK, IFR, Insurance Business and so on) means the cited publisher or the underlying data owner says it; the "source" column gives the URL actually opened or the search that surfaced it. WebSearch results are summaries, so those rows are marked "(search summary)".

## Chapter 1 (4 boxes)

| claim | verdict | evidence / correct figure | source |
| :-- | :-- | :-- | :-- |
| Box 1.1. Greenwich 2021 e-trading: IG 37%, HY 27% (via IFR) | CORRECTED | Greenwich's own Jan 2025 series charts 2021 as IG 34%, HY 25% (total 30%). No accessible source shows 37%/27%. Ch2 and Ch3 already use 34%/25%. See pair C1 | GW24 p.3 chart |
| Box 1.1. 2024: IG 48%, HY 33% | CONFIRMED | "48% of IG bond volume traded electronically (HY e-trading was flat)", HY 33% | GW24 p.3 |
| Box 1.1. 2024 ADNV $46bn, up 21% | CONFIRMED | "$46.2B, up 21% from 2023" | GW24 p.1-2 |
| Box 1.1. Turnover 0.33% of outstanding (2021) to 0.44% (2024) | CONFIRMED | "In 2021, the equivalent of 0.33% of bonds outstanding traded each day; in 2024, turnover grew to 0.44%" | GW24 p.2 |
| Box 1.1. 2025 ADNV passed $50bn for the first time | CONFIRMED | "averaged over $50 billion per day in 2025 for the first time ever", up 11% on 2024 | GW25 |
| Box 1.1. 2025 IG e-trading just under 50%, HY 32% | CONFIRMED | Greenwich 2025 coverage: IG "hovering just below 50%", HY "32%" (search summary of Fi-Desk's report) | https://www.fi-desk.com/?p=27374 |
| Box 1.1. Disclosed RFQ fell to 38.6% of electronic volume in 2025 | UNVERIFIABLE | Only a monthly figure was found ("just over 40%" in May 2025). Hedge: "disclosed RFQ slipped to roughly 40% of electronic volume in 2025 (Coalition Greenwich)" | search: Greenwich June 2025 spotlight |
| Box 1.1. Record day $84.7bn on 30 Sep 2025, 18% portfolio trades | CONFIRMED | "A new single day record was also set on September 30 when $84.7 billion traded ... 18% of that via portfolio trades" | GW25 |
| Box 1.1. PT 11% of volume in 2024, 15% in 2025, peak 17% in July 2025 (Morgan Stanley via The DESK 19 Feb 2026) | CONFIRMED | "PT penetration peaked at 17% in July ... full-year share to 15%, up from 11% in 2024" (search summary; DESK date not checked) | https://www.fi-desk.com/ig-credit-sees-portfolio-trading-plateau-while-hy-hits-records/ |
| Box 1.1. Barclays: a portfolio trade every six minutes in H1 2025 vs every 41 minutes in 2020 | UNVERIFIABLE | IFR is paywalled; search surfaced only Barclays' "22% of dealer-to-client IG volume in H1". Hedge: "Barclays counts a portfolio trade every few minutes in 2025, against roughly one every 40 minutes in 2020 (IFR, 2025)" | search: IFR Barclays PT |
| Box 1.1. Jan 2026 record: ADNV up 22% y/y to $61bn (Greenwich 17 Feb 2026) | UNVERIFIABLE | Not found. Hedge: "January 2026 set another record, ADNV up more than 20% year on year (Coalition Greenwich)" | none accessible |
| Box 1.1. Tradeweb reported a single PT with more than 4,000 line items | UNVERIFIABLE | Not found. Hedge: "a single portfolio trade with several thousand line items" | none accessible |
| Box 1.2. Dickerson, Mueller, Robotti (2023, JFE): earlier bond factors add little beyond the market factor | CONFIRMED | Consistent with the replication literature and the 2026 paper's framing (search summary of AFR, WBS, Advisor Perspectives coverage) | https://wbs.ac.uk/news/flaw-data-corporate-bond-investors |
| Box 1.2. Bai-Bali-Wen 2019 JFE paper retracted in 2023 after a data-timing error found in replication | CONFIRMED | Retraction notice cites "temporal misalignment"; two factors had a lead error, one a lag error (search summary) | https://wbs.ac.uk/news/flaw-data-corporate-bond-investors |
| Box 1.2. 9 Apr 2026 Dickerson, Robotti, Rossetti, arXiv:2604.07880, 108 signals | CONFIRMED | "Submitted 9 April 2026"; "factor zoo of 108 signals across nine thematic clusters" | https://arxiv.org/abs/2604.07880 |
| Box 1.2. Most factors lose significance in bond-CAPM alphas after correcting price measurement error and asymmetric ex-post return filtering | CONFIRMED | Abstract: both sources named; "the majority of previously documented factors do not produce statistically significant bond CAPM alphas after correction" | https://arxiv.org/pdf/2604.07880 |
| Box 1.2. "Open Source Bond Asset Pricing" publishes error-corrected data | CONFIRMED | The paper calls it "Open Bond Asset Pricing" (openbondassetpricing.com). Ch7 uses the paper's name; the book also uses "Open Source Bond Asset Pricing" in Ch4, Ch10, Ch11, App B. Pick one name; not a factual error | https://arxiv.org/pdf/2604.07880 |
| Box 1.3. CDOs/CLOs held about 3% of low-rated loans and bonds in 1993, over 20% by early 2000s | CONFIRMED | "since 1993 the percentage ... held by CDOs has increased from approximately 3% to over 20%"; Fig. 2-18 runs 1993-2003 | Moyer p.55 (source_pdfs/Moyer_Distressed_Debt_Analysis.pdf) |
| Box 1.3. US CLOs about $1tn, about 65% of a $1.5tn institutional leveraged loan market (Maples/Nuveen, 13 Apr 2026) | CONFIRMED | "US institutional leveraged loan market is approximately US$1.5 trillion ... CLO market outstanding approximately US$1 trillion ... roughly 65%" (search summary; date not checked) | https://maples.com/knowledge/bringing-you-closer-an-insightful-clo-qa |
| Box 1.3. CLO ETFs $2.25bn (2023) to more than $20bn (end-2024) (Deutsche Bank) | UNVERIFIABLE | Not found. Hedge: "CLO ETF assets grew roughly ten-fold between 2023 and end-2024 (Deutsche Bank Flow)" | none accessible |
| Box 1.3. US fixed income ETF assets about $2tn in June 2025 (Daily Upside) | UNVERIFIABLE | Not found. Hedge: "about $2tn (mid-2025)" with the source retained | none accessible |
| Box 1.3. Life-insurer private placements 14% (2016) to 22% (2024) of corporate bond holdings (Chicago Fed, May 2026) | CONFIRMED | Chicago Fed Insights (Meisenzahl, Polacek, Overpeck) reports 14% in 2016 and 22% in 2024 (search summary) | https://www.chicagofed.org/publications/chicago-fed-insights/2026/assessing-life-insurers-interconnectedness |
| Box 1.3. Privately placed bonds 48.4% of life-industry bonds at YE2025 vs 37.4% five years earlier | CONFIRMED | Insurance Business, citing S&P Global MI's 2026 US Insurance Investments report, gives these numbers "under the NAIC's broad bond classification". S&P MI's narrower measure in May 2026 is 23.4% (2025) vs 18.3% (2021). Add the definition so it is not read against the 22% above | https://www.insurancebusinessmag.com/us/news/life-insurance/private-credit-now-dominates-life-insurer-bonds-as-naic-rewrites-the-rulebook-585542.aspx |
| Box 1.3. Dealers set a record net short in corporate bonds in early 2026 (Greenwich 17 Feb 2026) | UNVERIFIABLE | Not found. Hedge: "dealer net positions swung sharply short in early 2026" | none accessible |
| Box 1.3. About $30bn entered fallen-angel indices in 2026 through mid-year, most since 2020 (Insight/BNY Aug 2026) | UNVERIFIABLE | Not found; VanEck notes only full-year forecasts ($60bn Goldman, $88bn JPM for 2026/27). Hedge: "tens of billions of fallen-angel supply so far in 2026 (Insight Investment)" | https://www.vaneck.com/us/en/blogs/income-investing/fallen-angels-reclaim-the-ytd-lead-as-2026-new-entrants-deliver/ |
| Box 1.4. Distressed exchanges more than 60% of 2024 default volume (through mid-Dec), highest share since at least 2000 | CONFIRMED | "more than 60% ... the highest percentage seen since at least 2000", article dated 18 Dec 2024 | https://www.marquetteassociates.com/damsel-in-distress/ |
| Box 1.4. 2024 HY default rate 1.4% with DEs vs 0.3% without | CONFIRMED | Exact | https://www.marquetteassociates.com/damsel-in-distress/ |
| Box 1.4. 2024 loan default rate 4.0% with DEs vs 1.5% without | CONFIRMED | Exact | https://www.marquetteassociates.com/damsel-in-distress/ |
| Box 1.4. Moody's (18 May 2026): distressed restructurings about 65% of 2025 corporate defaults | CONFIRMED | "in 2025, roughly 65% of all corporate defaults were distressed restructurings" | https://www.moodys.com/web/en/us/insights/credit-risk/private-credit/lend-extend-and-then.html |
| Box 1.4. "its 1,173-event history of soft credit events since 1979" | CORRECTED | Moody's: "1,173 unique borrowers that experienced a soft credit event", 1979-2026. Borrowers, not events. Ch3 and Ch5 already say borrowers. See pair C2 | same Moody's URL |
| Box 1.4. About one in four soft events ended in hard default; more than 70% of eventual hard defaults within two years | CONFIRMED | "about one in four soft credit events ultimately ends in hard default"; ">70% of eventual hard defaults following a distressed restructuring occur within the first two years" (qualifier missing in Ch1; added in pair C2) | same Moody's URL |

## Chapter 2 (3 boxes)

| claim | verdict | evidence / correct figure | source |
| :-- | :-- | :-- | :-- |
| Box 2.1. Sept 1998: SEC asks NASD for corporate-debt transparency | CONFIRMED | "In September 1998, the SEC requested the NASD to provide more transparency" | Bohn_Stein p.91 fn.6 (local PDF) |
| Box 2.1. 1 Jul 2002: TRACE launches, 75-minute reporting; Phase I about 520 securities by end-2002 | CONFIRMED | "approximately 520 securities by the end of 2002"; 75 minutes on 1 Jul 2002 | FactBook p.3-4 |
| Box 2.1. 3 Mar and 14 Apr 2003: Phases IIa and IIb, about 4,650 bonds | CONFIRMED | Timeline gives both dates; "approximately 4,650 bonds". Text says Phase IIb adds 120 Baa/BBB plus 50 HY (the FINRA timeline table says "BB", a typo in the table) | FactBook p.3-4 |
| Box 2.1. 1 Oct 2003: clock cut to 45 minutes | CONFIRMED | Exact | FactBook p.3-4 |
| Box 2.1. 1 Oct 2004: Phase IIIa; clock cut to 30 minutes | CONFIRMED | Exact | FactBook p.4 |
| Box 2.1. 7 Feb 2005: Phase IIIb; about 99% of transactions and 95% of par disseminated immediately | CONFIRMED | "approximately 99 percent of all public transactions and 95 percent of par value" | FactBook p.3 |
| Box 2.1. 1 Jul 2005: clock cut to 15 minutes | CONFIRMED | Exact | FactBook p.3-4 |
| Box 2.1. 9 Jan 2006: immediate dissemination of all public TRACE-eligible corporates | CONFIRMED | "Since January 9, 2006, all transactions in public TRACE-eligible securities have been disseminated immediately" | FactBook p.3 |
| Box 2.1. 30 Jun 2014: Rule 144A corporate trades disseminated | CONFIRMED | "Effective June 30, 2014, TRACE began disseminating transactions executed pursuant to SEC Rule 144A" | FactBook p.3 |
| Box 2.1. 15 May 2023: portfolio-trade modifier required (RN 22-12) | CONFIRMED | "Members must append qualifying transaction reports with the portfolio trade modifier beginning on May 15, 2023"; notice published 24 May 2022 | https://www.finra.org/rules-guidance/notices/22-12 |
| Box 2.1. 11 Jan 2024: FINRA files SR-FINRA-2024-004 (one-minute rule) | CONFIRMED | "On January 11, 2024, FINRA filed" | SEC-101121 p.2 |
| Box 2.1. 20 Sep 2024: SEC approves the one-minute rule (Rel. 34-101121) | CONFIRMED | Order dated September 20, 2024 | SEC-101121 |
| Box 2.1. 5 Feb 2025: FINRA says it will not set an effective date (Mayer Brown, 10 Feb 2025) | UNVERIFIABLE | Not found. RN 25-17 fn.9 says SR-FINRA-2025-008 rescinded the timeframe cuts. Hedge: "in early 2025 FINRA signalled it would not set an effective date" and cite RN 25-17 | none accessible |
| Box 2.1. 4 Dec 2025: FINRA "is not moving forward"; 15-minute standard stays (RN 25-17) | CONFIRMED | Published 4 Dec 2025: "FINRA is not moving forward with its proposal to reduce the 15-minute TRACE reporting outer limit to one minute" | https://www.finra.org/rules-guidance/notices/25-17 |
| Box 2.1. 8 Jun 2026: optional aggregate allocation reporting begins | CONFIRMED | "The amendments will become effective on June 8, 2026 ... optional for firms" | https://www.finra.org/rules-guidance/notices/25-17 |
| Box 2.1. 31 Aug 2026 voluntary, 2 Aug 2027 mandatory (RN 26-16) | CONFIRMED | Published 26 Aug 2026; both dates exact | https://www.finra.org/rules-guidance/notices/26-16 |
| Box 2.1. In 2022, 82.9% of trades between 8:00 a.m. and 6:15 p.m. ET reported within one minute; 90.6% within three | CONFIRMED | "in 2022, 82.9 percent of the trades ... executed after 8:00 a.m. and before 6:15 p.m. ET were reported within one minute"; 90.6% within three minutes | SEC-101121 p.3, p.18 |
| Box 2.1. Rule would speed up to 16.4% of annual volume, 6.1 million trades, $20 trillion par | CONFIRMED | "up to 16.4% of current annual trading volume, or up to 6.1 million trades and 20 trillion dollars in par value" | SEC-101121 |
| Box 2.2. 2015: IG 20%, HY 6% (Greenwich, McPartland, 10 Jun 2025) | UNVERIFIABLE | Not found. Hedge: "about a fifth of IG and a few percent of HY in 2015" | none accessible |
| Box 2.2. 2021: IG about 34%, HY about 25% (chart reading, CHECK) | CONFIRMED | Chart in GW24: IG 34%, HY 25%, total 30%. Remove the CHECK flag | GW24 p.3 |
| Box 2.2. 2022: IG about 41%, HY about 31% (chart reading, CHECK) | CONFIRMED | Chart: IG 41%, HY 31%, total 38%. Remove the CHECK flag | GW24 p.3 |
| Box 2.2. 2023: IG 45%, HY 33% | CONFIRMED | Chart: IG 45%, HY 33%, total 41% | GW24 p.3 |
| Box 2.2. Feb 2024: IG 45%, HY 29% (The DESK, 19 Mar 2024) | UNVERIFIABLE | Monthly values not found. Keep with the DESK attribution or drop | none accessible |
| Box 2.2. 2024: IG 48%, HY 33%, overall 44%, ADNV $46.2bn, 125,723 trades/day, average ticket $381k | CONFIRMED | All exact ("$381K", "125,723", "$46.2B", "44%") | GW24 p.1-3 |
| Box 2.2. Feb 2025: HY 30% (Greenwich Data Spotlight 17 Mar 2025) | UNVERIFIABLE | Not found | none accessible |
| Box 2.2. Jun 2025: IG 52% (Greenwich Data Spotlight 14 Jul 2025) | UNVERIFIABLE | Not found. Full-year 2025 IG is "just under 50%" (see Ch1), so a 52% month is plausible but unconfirmed | none accessible |
| Box 2.2. MarketAxess 10-K estimates: IG about 45% / 50% / 60%, HY about 30% (2023/2024/2025) | UNVERIFIABLE | 10-Ks not opened (budget). Hedge: "MarketAxess's own estimates run above Greenwich's, by its definition" | MarketAxess FY2025 10-K (not opened) |
| Box 2.2. Disclosed RFQ 48.3% (2021), 42.3% (2022), 47.2% (2023), 44.0% (2024) | CONFIRMED | Exact in the protocol-mix chart | GW24 p.4 |
| Box 2.2. Man: from about 30% HY and 60% IG electronic to over 90% as of 1 May 2023 | CONFIRMED | "moved from roughly 30% of our order flow in high yield and 60% in investment grade ... to over 90%"; footnote "Man Numeric; as of 1 May 2023" | Man_Revolutions_2023 p.3-4 (local PDF) |
| Box 2.2. Barclays, Sept 2025: "more than 50%" electronic; MarketAxess about 60% | UNVERIFIABLE | Not found. Keep as attributed or hedge to "around or above half on broader definitions" | none accessible |
| Box 2.3. 2021 to 2022 PT share of US e-volume about 7% to about 10% (Man Fig. 4, chart reading, CHECK) | CONFIRMED | Man Fig. 4: PT 7% (2021), 10% (2022). Column order resolved: the disclosed-RFQ pair 48%/42% matches Greenwich's 48.3% (2021)/42.3% (2022), so the first number is 2021. Greenwich's restated series reads PT 6.4% to 9.7%. Remove CHECK | Man_Revolutions_2023 p.4; GW24 p.4 |
| Box 2.3. 2023: PT about 7-8% of TRACE (Husveth via The DESK 29 Jan 2025) | UNVERIFIABLE | Not found | none accessible |
| Box 2.3. 2023: PT about 5% of customer volume (Bondwave, 20 May 2026) | UNVERIFIABLE | Bondwave report not found | search: Bondwave "A Market Transformed" |
| Box 2.3. 2024: PT 10% of IG, 8% of HY; near 13% of IG in December | CONFIRMED | "10% of IG volume and 8% of HY volume ... peaking at nearly 13% for IG in December" | GW24 p.4 |
| Box 2.3. 2024 electronic PT ADNV $3.3bn (+76%); about 85% of all PT; Tradeweb more than two-thirds | CONFIRMED | "$3.3 billion, which is 76% higher"; "about 85% of total PT volume"; Tradeweb "over two-thirds" | GW24 p.4-5 |
| Box 2.3. Dec 2024: PT 11.4% of TRACE (The DESK 29 Jan 2025) | UNVERIFIABLE | Not found | none accessible |
| Box 2.3. 8 Apr 2025: PT 12% of an $89.7bn record day (Greenwich citing Trumid, 14 Apr 2025) | UNVERIFIABLE | Not found, and it conflicts with the next row: Greenwich says 30 Sep 2025 ($84.7bn) was "a new single day record". Either the two figures use different bases or one is wrong. Hedge: label the April figure "peak-volatility day, Trumid basis" or drop "record" | GW25 |
| Box 2.3. 30 Sep 2025: PT 18% of an $84.7bn record day | CONFIRMED | Exact | GW25 |
| Box 2.3. Q1 2026: PT 19.8% of customer volume (Bondwave) | UNVERIFIABLE | Bondwave report not found. Also used in the Ch2 Desk Debrief | search: Bondwave |
| Box 2.3. Q1 2026: 15.5% of corporate volume prints at the index mark (5% in 2016, 9.3% in 2021) | UNVERIFIABLE | Bondwave report not found | search: Bondwave |
| Box 2.3. Q2 2026: MarketAxess PT ADV +33% to $1.97bn | CONFIRMED | Release headline: "33% Increase in Portfolio Trading ADV to Record $2.0 Billion". The $1.97bn decimal was not seen; consistent with rounding | https://investor.marketaxess.com/news/news-details/2026/MarketAxess-Reports-Second-Quarter-2026-Financial-Results/default.aspx |
| Box 2.3. Q2 2026: MarketAxess share of US credit PT 20.6% | UNVERIFIABLE | No share in the Q2 release as fetched (FY2025 release: 19% for the year, 21% in 4Q25). Hedge: "about 20%" | MarketAxess Q2 and FY2025 releases |
| Box 2.3. Nearly half of PT volume prints at or after index time; Bondwave PT execution-quality percentile 57.3 (May 2023) to 50.3 (Feb 2026) | UNVERIFIABLE | Bondwave report not found | search: Bondwave |

## Chapter 3 (3 boxes)

| claim | verdict | evidence / correct figure | source |
| :-- | :-- | :-- | :-- |
| Box 3.1. 2016: about 19% of US IG trading electronically facilitated (Greenwich, cited in Bessembinder, Spatt, Venkataraman 2020) | UNVERIFIABLE | Paper not opened. Hedge: "roughly a fifth of US IG trading in 2015-16" | none accessible |
| Box 3.1. Greenwich IG e-share 34%, 41%, 45%, 48% for 2021-2024 ("approx." for 2021-22) | CONFIRMED | Chart values IG 34/41/45/48. Drop "approx." | GW24 p.3 |
| Box 3.1. IG 52% in June 2025 | UNVERIFIABLE | See Ch2 row; monthly value not found | none accessible |
| Box 3.1. "high yield was stuck near 30-33% throughout" | CORRECTED | HY was 25% (2021), 31% (2022), 33% (2023), 33% (2024), 32% (2025). "Throughout" fails for 2021. See pair C3 | GW24 p.3 chart; Fi-Desk 2025 summary |
| Box 3.1. June 2024: nearly 30% of dealer trading volume executed without human intervention | CONFIRMED | Coalition Greenwich release, 11 Jun 2024 (search summary) | https://coalitiongreenwich.crisil.com/en/homepage/press-release/Free/2024/bond-dealers-increasingly-automate-trading.html |
| Box 3.1. Top-tier desks field about 30,000 inquiries per day | CONFIRMED | "roughly 30,000 inquiries per day on average" | same Greenwich release |
| Box 3.1. Top-tier dealers execute 57% with no human; non-bank liquidity providers 70% | CONFIRMED | "top-tier firms ... executing 57% ... without human intervention and non-bank liquidity providers 70%" | same Greenwich release |
| Box 3.1. MarketAxess automation suite handled over 36% of clients' global RFQ tickets in 2025 YTD (22 Sep 2025) | UNVERIFIABLE | Not found | none accessible |
| Box 3.1. 261 client firms used automated/algorithmic tools in 2025 (204 in 2023) | UNVERIFIABLE | MarketAxess 10-Ks not opened | MarketAxess 10-K (not opened) |
| Box 3.1. Dealer algorithmic responses 32.5 million (2023) to 40.9 million (2024) | UNVERIFIABLE | MarketAxess 10-Ks not opened | MarketAxess 10-K (not opened) |
| Box 3.1. Trumid: 88% of eligible RFQ line items executed fully no-touch in Sept 2025 (The DESK) | UNVERIFIABLE | Not found | none accessible |
| Box 3.2. 8-K counts for "liability management transaction": 4, 9, 23, 15, 14, 55, 54, 37 (2019-2026 to 16 Oct) | CONFIRMED | Re-run on 2026-10-18 with the exact phrase, form 8-K, same date windows: totals 4, 9, 23, 15, 14, 55, 54, 37 | EDGAR-FTS |
| Box 3.2. Distinct filers 4, 6, 16, 12, 8, 24, 27, 24 | CONFIRMED | Distinct first-listed filer names per year reproduce exactly (distinct CIK counts across co-registrants run slightly higher: 17 in 2021, 26 in 2024, 29 in 2025, 27 in 2026; state the counting rule) | EDGAR-FTS |
| Box 3.2. Wachtell: high-water mark of 38 LMEs in 2024, 24 in 2025; memo 3 Feb 2026 | CONFIRMED | "24, compared to a high-water mark of 38 in 2024"; dated February 3, 2026 | https://www.wlrk.com/FirmMemos/WLRK/WLRK.29921.26.pdf |
| Box 3.3. Moody's: DEs 64% of defaults in H1 2025, "about the same pace" as 2024, "the highest annual share on record" | CONFIRMED | Verbatim in the report | https://www.moodys.com/web/en/us/insights/resources/us-report-july-2025.pdf |
| Box 3.3. June 2025 default rate 5.8% falls to 2.1% when the 51 distressed restructurings are removed | CONFIRMED | "came in at 5.8% in June. Removing the 51 distressed restructurings ... 2.1%". Population is all high-yield (bond plus loan) issuers; report is by Moody's Analytics Asset Management Research | same Moody's PDF |
| Box 3.3. Report cited as "US Credit Review & Outlook," July 2025 | CORRECTED | Cover date is 7 August 2025 (the file name says july). See pair C5 | same Moody's PDF |
| Box 3.3. Moody's later put distressed restructurings at about 65% of 2025 defaults | CONFIRMED | Moody's 18 May 2026: "roughly 65%" | https://www.moodys.com/web/en/us/insights/credit-risk/private-credit/lend-extend-and-then.html |
| Box 3.3. ... dated "April 28, 2026" | UNVERIFIABLE | No 28 April piece found; the 65% appears in the 18 May 2026 report (cited in Ch1 and Ch5). Safe fix: cite 18 May 2026 (optional pair H1) | none accessible |
| Box 3.3. Wachtell: LMEs from 38 (2024) to 24 (2025), still about two-thirds of default activity by issuer count | CONFIRMED | "LMEs still accounted for two-thirds of default activity by issuer count in 2025" | Wachtell PDF above |
| Box 3.3. Moody's sample of 1,173 borrowers, one in four to hard default, more than 70% within two years (18 May 2026) | CONFIRMED | Exact; qualifier "following a distressed restructuring" is in the Ch3 text | Moody's 18 May 2026 URL above |

## Chapter 4 (2 boxes)

| claim | verdict | evidence / correct figure | source |
| :-- | :-- | :-- | :-- |
| Box 4.1. Man Numeric formally launches credit business Oct 2018 under two co-heads (Hedgeweek, 10 Oct 2018) | UNVERIFIABLE | Hedgeweek not found. Hedge: "Man Numeric launched its credit business in autumn 2018" | none accessible |
| Box 4.1. BlackRock IGEB and HYDB launched July 2017 | UNVERIFIABLE | Not re-fetched; the project dossier (state/research/trend_systematic_credit_industry.md) dates it 11 Jul 2017 | dossier only |
| Box 4.1. 2020: $116.5bn on MarketAxess Open Trading via quant funds in first three quarters, +150% | CONFIRMED | "$116.5 billion traded on MarketAxess's Open Trading platform via quant funds during the first three quarters of 2020, a 150% increase" | Man_Quantitative_Credit_Alpha_2022 p.8 (local PDF) |
| Box 4.1. Blackstone agrees to buy DCI, "about $7.5bn", 30 Nov 2020 | CORRECTED | The announcement is 30 Nov 2020, but $7.5bn is DCI's assets under management; deal terms were not disclosed. The Ch4 body (line 611) says it correctly. See pair C4 | https://www.blackstone.com/news/press/blackstone-announces-agreement-to-acquire-dci-a-pioneer-in-technology-driven-quantitative-credit-investing/ |
| Box 4.1. 2021: eVestment about $52bn actively managed quant credit, more than double five years earlier | UNVERIFIABLE | IFR not found. Hedge: "on the order of $50bn" | none accessible |
| Box 4.1. 2021: BlueCove, quant credit about 0.4% of a $66trn fixed-income universe vs about 15% for quant equity | UNVERIFIABLE | Not found; the box already flags the date CHECK | none accessible |
| Box 4.1. 2023: "Systematic credit funds doubled in size in 2023" (Bloomberg 20 May 2024, via BBH 2 Mar 2026) | UNVERIFIABLE | Not found. Keep as a quoted attribution | none accessible |
| Box 4.1. 2024: Barclays QPS sizes quant-screened IG and HY funds at $90-140bn (via Impax, 19 Sep 2025) | UNVERIFIABLE | Not found | none accessible |
| Box 4.1. Invesco study: 88% of managers use systematic methods in fixed income, up from 73% in 2023 | UNVERIFIABLE | Not found | none accessible |
| Box 4.1. Man Numeric co-head: "still in a very low single digits of market share" (podcast, Mar 2024) | UNVERIFIABLE | Podcast not checked | none accessible |
| Box 4.1. 2025: systematic about 20% of global equities, under 2% of investable fixed income (Bloomberg 2 Feb 2026 via BBH) | UNVERIFIABLE | Not found | none accessible |
| Box 4.1. Man systematic long-only credit $3.1bn and discretionary $37.5bn at Sept 2026 | CONFIRMED | Man trading statement, 16 Oct 2026: long-only credit $40.6bn = discretionary $37.5bn + systematic $3.1bn | https://www.investegate.co.uk/announcement/rns/man-group--emg/trading-statement-for-quarter-ended-30-sept-2026/9825923 |
| Box 4.1. Same series in March 2025: systematic $2.0bn, discretionary $19.8bn | UNVERIFIABLE | The Q3 2026 statement starts at Sep 2025 (systematic $2.8bn, discretionary $27.7bn); the Mar 2025 column sits in the Q1 2026 statement, not re-fetched. Note the jump in discretionary from $19.8bn to $27.7bn in six months deserves a check against the Q1 2026 table | Man Q1 2026 RNS (not re-fetched) |
| Box 4.2. 2021: US IG 37%, HY 27% (Greenwich via IFR, date CHECK) | CORRECTED | Greenwich Jan 2025 series: 34% and 25%. See pair C1 | GW24 p.3 |
| Box 4.2. Man: "2021 was the year of portfolio trading; 2022 was the year of electronic trading" | CONFIRMED | Verbatim | Man_Revolutions_2023 p.5 |
| Box 4.2. 2021 to 2022: disclosed RFQ 48% to 42%, PT 7% to 10%, streaming 7% to 9% (column order CHECK) | CONFIRMED | Man Fig. 4 values match. First number = 2021 (Greenwich restated: RFQ 48.3% to 42.3%, PT 6.4% to 9.7%, streaming 8.2% to 8.5%). Remove CHECK | Man_Revolutions_2023 p.4; GW24 p.4 |
| Box 4.2. May 2023: Man routes over 90% of credit order flow electronically | CONFIRMED | "over 90% of our order flow", as of 1 May 2023 | Man_Revolutions_2023 p.3-4 |
| Box 4.2. 2024: IG 48%, HY 33%, ADNV $46.2bn (+21%) | CONFIRMED | Exact | GW24 |
| Box 4.2. 2024: non-bank liquidity providers about 10% of US credit market-making revenue | CONFIRMED | "roughly 10% of total credit market-making revenue in 2024" | GW24 p.5 |
| Box 4.2. 2024: Tradeweb more than two-thirds of electronic PT | CONFIRMED | "over two-thirds of executed volume in 2024" | GW24 p.5 |
| Box 4.2. 2025: US corporate bond trading over $50bn a day for the first time (Greenwich 27 Jan 2026) | CONFIRMED | See Ch1 row | GW25 |
| Box 4.2. MarketAxess FY2025: record PT ADV $1.4bn (+48%), 19% share of US credit PT | CONFIRMED | "48% increase in total portfolio trading ADV to record $1.4 billion"; "Record U.S. credit portfolio trading market share of 19%" | https://investor.marketaxess.com/news/news-details/2026/MarketAxess-Reports-Fourth-Quarter-and-Full-Year-2025-Financial-Results/default.aspx |
| Box 4.2. Sept 2025: MarketAxess, Tradeweb, Trumid each about $8.5-8.8bn e-credit ADV, about 15% of TRACE each (The DESK 8 Oct 2025) | CONFIRMED | MarketAxess $8.82bn (15.3%), Tradeweb $8.57bn (14.8%), Trumid $8.5bn (14.7%) | https://www.fi-desk.com/trumids-us-electronic-credit-volume-in-sight-of-marketaxess-and-tradewebs/ |
| Box 4.2. Mar 2026: combined IG+HY TRACE ADV $70.2bn (+14.7%) | UNVERIFIABLE | The DESK 9 Apr 2026 not found | none accessible |
| Box 4.2. Mar 2026: MarketAxess PT ADV record $2.3bn | UNVERIFIABLE | Q2 2026 release gives a record $2.0bn for the quarter; no March figure seen | MarketAxess Q2 2026 release |
| Box 4.2. Mar 2026: Trumid record $10.3bn ADV | UNVERIFIABLE | Not found | none accessible |
| Box 4.2. Jul 2026: ICE to acquire MarketAxess at $167 a share cash, about $6.0bn equity, close in H1 2027 | CONFIRMED | "$167 per share in cash ... equity value of approximately $6.0 billion and total enterprise value of approximately $5.7 billion ... expected to close in the first half of 2027"; 33% premium to the 29 Jul 2026 close | https://www.sec.gov/Archives/edgar/data/1278021/000119312526324933/d159148dex991.htm |
| Box 4.2. Oct 2026: Vanguard automated low/no-touch about 70% of desk volume, up from about 40% (The DESK 14 Oct 2026) | CONFIRMED | Article of 14 Oct 2026: "Historically for us, those last two methods would represent maybe 40% ... Now that number is more like 70%". The two methods are low-touch and no-touch; the 40% has no stated date | https://www.fi-desk.com/fils-europe-vanguard-automates-70-of-trades-others-urge-caution/ |

## Chapter 5 (3 boxes)

| claim | verdict | evidence / correct figure | source |
| :-- | :-- | :-- | :-- |
| Box 5.1. 15 Oct 2026 OAS: HY index 323 bp, BB 197, single-B 326, CCC 1,278 | CONFIRMED | FRED rows for 2026-10-15: 3.23, 1.97, 3.26, 12.78. Last observation in the file is 15 Oct | FRED |
| Box 5.1. CCC/HY ratio low 2.24 on 20 Oct 2023 | CONFIRMED | 9.69/4.25 on 2023-10-17 is higher; minimum over the window is 2.237 on 2023-10-20 | FRED |
| Box 5.1. CCC/HY ratio high 4.06 on 11 Sep 2026 | CONFIRMED | 10.76/2.65 = 4.060 | FRED |
| Box 5.1. Quarter-end ratios 2.66 (Dec 2023), 2.55 (Dec 2024), 3.15 (Dec 2025), 3.53 (Jun 2026), 3.78 (Sep 2026) | CONFIRMED | Computed 2.661, 2.555, 3.149, 3.527, 3.779. (2.555 rounds to 2.55 or 2.56; the book's 2.55 is fine) | FRED |
| Box 5.1. BB OAS touched 150 bp on 28 Aug 2026 | CONFIRMED | 1.50 on 2026-08-28 (also 1.50 on 2026-09-11). Window minimum | FRED |
| Box 5.1. CCC OAS hit 1,282 bp on 14 Oct 2026 | CONFIRMED | 12.82 on 2026-10-14, the window maximum | FRED |
| Box 5.1. Index peak 461 bp on 7 Apr 2025 (tariff shock) | CONFIRMED | 4.61 on 2025-04-07, the window maximum | FRED |
| Box 5.1. FRED serves three years of history, from 17 Oct 2023 | CONFIRMED | First row is 2023-10-17 | FRED |
| Box 5.1. Credit-triangle arithmetic: CCC 0.1278/0.6 about 21%; BB about 3% | CONFIRMED | 0.1278/0.6 = 21.3%; 0.0197/0.6 = 3.3% | arithmetic from FRED |
| Box 5.1. Moody's Analytics, US Credit Review & Outlook, "July 2025" | CORRECTED | Cover date is 7 August 2025. See pair C5 | Moody's PDF (see Ch3) |
| Box 5.2. Moody's via BMA (5 Sep 2024): trading-price recoveries 1983-2023 of 65% (first-lien bank loans), 55% (first-lien bonds), 38% (senior unsecured bonds) | UNVERIFIABLE | BMA document not found. Moody's long-run figures are widely quoted but were not re-checked. Hedge: add "approximately" | none accessible |
| Box 5.2. Ultimate recoveries 1987-2023: 87% revolvers, 71% term loans, 62% senior secured bonds, 47% senior unsecured | UNVERIFIABLE | Same | none accessible |
| Box 5.2. S&P: first-lien and priority debt more than 75% of typical structures | UNVERIFIABLE | Not found | none accessible |
| Box 5.2. Fitch 2023 Annual Manual (30 Mar 2023): first-lien loan 30-day post-default price averaged 59.5% (median 62.8%), 2007-2022 | UNVERIFIABLE | Not found | none accessible |
| Box 5.2. S&P CreditWeek (20 Feb 2025): first-lien recovery ratings in the mid-to-low 60% range vs long-term 75-80% (via search summary) | UNVERIFIABLE | The box itself says "via search summary". Hedge: keep the qualifier | none accessible |
| Box 5.2. Moody's via Bloomberg Law (23 Apr 2025): first-lien distressed-exchange recoveries 71% at end-2024, up from 55% in 2023 | UNVERIFIABLE | Bloomberg Law is paywalled; not opened | https://news.bloomberglaw.com/bankruptcy-law/distress-exchange-leads-to-re-default-half-the-time-moodys |
| Box 5.2. Moody's 22 Sep 2026 (via American Banker 28 Sep 2026): first-lien loan recoveries projected "declining to 55%" | UNVERIFIABLE | Not found in search. A 2023 figure of 55% and a 2026 projection of 55% in the same paragraph deserves a re-read of the source | none accessible |
| Box 5.3. Fitch: DDEs 45% (volume) and 50% (count) of 2022 defaults | UNVERIFIABLE | Fitch manual not found | none accessible |
| Box 5.3. S&P (via FTI, 9 Oct 2026): DDEs about half of rated US corporate defaults for three years vs 32% for 2010-2023 | UNVERIFIABLE | FTI article not opened (budget) | https://www.fticonsulting.com/insights/articles/state-of-restructuring-market |
| Box 5.3. Moody's Analytics: DEs 64% of H1 2025 defaults, quote, 5.8% vs 2.1% after removing 51 | CONFIRMED | Verbatim in the 7 Aug 2025 report | Moody's PDF (see Ch3) |
| Box 5.3. Moody's 18 May 2026: about 65% of 2025 defaults; 1,173 soft-event borrowers 1979-2026; one in four; more than 70% within two years | CONFIRMED | Exact | Moody's 18 May 2026 URL (see Ch1) |
| Box 5.3. Moody's 22 Sep 2026 (via American Banker): DEs/LMEs "roughly 70% of defaults since early 2022"; default rate 5.3% in Aug 2026 | UNVERIFIABLE | Not found. If true, the 5.3% conflicts with the Ch6 box glide path (see Ch6) | none accessible |

## Chapter 6 (3 boxes)

| claim | verdict | evidence / correct figure | source |
| :-- | :-- | :-- | :-- |
| Box 6.1. Blackstone BCBS: "the largest pure-play quantitative credit operation in the world, with over $40 billion in assets under management" | CONFIRMED | Verbatim; shelf document is undated, as the box says | Blackstone_Systematic_Credit p.1 (local PDF) |
| Box 6.1. DCI acquired late 2020, co-founded by the creators of the KMV model | CONFIRMED | Same document: "late-2020 acquisition of DCI, a quantitative credit pioneer co-founded by the creators of the KMV model". Announcement date 30 Nov 2020 confirmed by Blackstone's press release | Blackstone doc p.1; Blackstone press release URL (Ch4) |
| Box 6.1. BlackRock PD signal identified 77% of defaulted ICE BofA HY bonds within 24 months of default since 2010, data as of 31 Mar 2024 | CONFIRMED | Verbatim; footnote "BlackRock, ICE BofA ML as of March 31, 2024, using data since January 2010" | BlackRock_Systematic_High_Yield_Credit p.6 (local PDF) |
| Box 6.1. Dynkin et al.: Merton hedge ratios about 5% lower than empirical in both IG and HY, Jan 1993 - Dec 2019 | CONFIRMED | "the analytical hedge ratios were lower by about 5% in both IG and HY"; sample Jan 1993-Dec 2019 | Dynkin p.87, p.115 (local) |
| Box 6.1. "Goyal, Bali, Huang, Jiang, and Wen (2020 working paper), Predicting Corporate Bond Returns: Merton Meets Machine Learning" | UNVERIFIABLE | Not looked up. Working recollection (unchecked): the paper is Bali, Goyal, Huang, Jiang and Wen, SFI Research Paper 20-110, so the author order may be wrong. Check on SSRN before the next edition | none accessible |
| Box 6.2. S&P (Feb 2025): DEs about two-thirds of US spec-grade defaults in Q4 2024; DE default rate about 3.2% vs about 2% other types | UNVERIFIABLE | The box already says "not independently verified". Search found S&P's Aug 2024 note (DEs two-thirds of July 2024 global defaults) and a Feb 2025 Europe note (DE rate 2.9%), but not these US figures. Keep the hedge | https://www.spglobal.com/ratings/en/research/articles/240815-default-transition-and-recovery-distressed-exchanges-reached-their-highest-level-since-2009-13217386 |
| Box 6.2. Oaktree Q4 2024 via Quinn Emanuel (Jan 2026): LMEs "over 50%" of corporate defaults | UNVERIFIABLE | Not found | none accessible |
| Box 6.2. 31 Dec 2024: Fifth Circuit holds Serta's 2020 uptier not an "open market purchase" | CONFIRMED | Fifth Circuit reversed; uptier outside the exception. The opinion was later revised (14 Feb 2025, per the Fifth Circuit file name in the dossier), so cite both dates if citing the revised text | https://www.mayerbrown.com/en/insights/publications/2025/05/serta-and-mitel-the-latest-major-court-decisions-on-uptier-transactions |
| Box 6.2. Reporter cite 125 F.4th 555 | UNVERIFIABLE | Cite not seen in any source opened. Check on Westlaw or the court's PDF before print | https://www.ca5.uscourts.gov/opinions/pub/23/23-20181-CV0.pdf (not opened) |
| Box 6.2. Same day, NY App. Div. First Dept upheld the Mitel uptier (Ocean Trails CLO VII v. MLN Topco) | CONFIRMED | "First Department upheld Mitel's 2022 uptier", 31 Dec 2024 | Mayer Brown, above |
| Box 6.2. Moody's: global spec-grade default rate 4.3% in May 2026 (4.1% Dec 2025, avg 4.2%); US 5.0%; forecasts 3.1% global / 3.5% US by Dec 2026 (First Trust, 22 Jun 2026) | UNVERIFIABLE | Not found. Cross-chapter conflict: Ch5 reports a US default rate of 5.3% in Aug 2026, which would put the forecast glide path (5.0% falling to 3.5%) behind. If the Ch5 number is confirmed, treat this forecast as superseded | none accessible |
| Box 6.2. UBS AM projected a 4.8% USD HY default rate for 2025, 3.1% excluding two large names (17 Jan 2025) | UNVERIFIABLE | Not found | none accessible |
| Box 6.3. ISDA May 2023: single-name traded notional $405bn to $1.1tn per quarter over 2018-Q1 2023, trough Q4 2020, five-year peak $1.1tn in Q1 2023 on bank failures | CONFIRMED | "ranged between $405 billion and $1.1 trillion per quarter, hitting a trough in the fourth quarter of 2020 ... peak"; bank failures named as a driver | https://www.isda.org/a/0jLgE/Single-name-CDS-Market-Update.pdf |
| Box 6.3. Reference entities trading per quarter 854 (Q1 2018) to 719 (Q1 2023) | CONFIRMED | Exact for those dates | same ISDA PDF |
| Box 6.3. "Breadth shrank" (the trend claim) | STALE | ISDA July 2026: breadth "remained broadly stable ... approximately 710 to 760 names" each quarter 2021-2025, 751 in Q4 2025. See pair S1 | https://www.isda.org/a/Pa0iE/CDS-Market-Dynamics-Five-Years-of-Activity-and-a-Record-2025.pdf |
| Box 6.3. 1,169 entities traded at least once in five years; about 600 less than once a quarter; 496 traded every quarter, over 80% of activity | CONFIRMED | Exact | ISDA May 2023 PDF |
| Box 6.3. Q1 2023: 51.2% of single-name and 87.4% of index notional centrally cleared | STALE | Those shares apply to notional "required to be reported under" US SEC (single-name) and CFTC (index) rules. ISDA July 2026 gives 2025: 63.1% single-name, 78.1% index. See pair S2 | ISDA May 2023 PDF; ISDA July 2026 note |
| Box 6.3. BIS: CDS notional $8.5tn at end-Dec 2023, down from $9.9tn six months earlier; 65% cleared (16 May 2024) | CONFIRMED | "fell 14% in the second half of 2023, from $9.9 trillion to $8.5 trillion"; cleared share 70% to 65%. Newer BIS releases exist (Nov 2024, May 2025, Nov 2025, May 2026); I could not retrieve the later ones (bis.org/publ/otc_hy2605.htm returned 404), so treat the series as due for an update | https://www.bis.org/publ/otc_hy2405.htm |
| Box 6.3. BIS: credit derivatives $9.2tn at end-June 2024, down 9% y/y (21 Nov 2024) | CONFIRMED | "credit derivatives declined by 9% yoy to $9.2 trillion"; release dated 21 Nov 2024. Same update caveat as above | https://www.bis.org/publ/otc_hy2411.htm |
| Box 6.3. ISDA CDS Standard Model rate curves moved to a new S&P Global site; old site shut after 15 Aug 2026 (cdsmodel.com) | UNVERIFIABLE | cdsmodel.com not opened. The shutdown date is already past (today is 2026-10-18); put the sentence in the past tense once confirmed | none accessible |

## Chapter 7 (2 boxes)

| claim | verdict | evidence / correct figure | source |
| :-- | :-- | :-- | :-- |
| Box 7.1. Bai, Bali, Wen (2019), JFE 131(3): 619-642, four-factor model | UNVERIFIABLE | Paper and its retraction are real (search); volume and pages not re-checked. Check on Crossref | search: JFE retraction coverage |
| Box 7.1. Dick-Nielsen, Feldhutter, Pedersen, Stolborg: AQR page 5 Oct 2023, Best Paper at 2024 Utah Winter Finance Conference, "only 23% of the factors ... have significant alphas" (Quantpedia 14 May 2024) | UNVERIFIABLE | Not searched (budget) | none accessible |
| Box 7.1. Dickerson, Mueller, Robotti, "Priced risk in corporate bonds", JFE 150(2), 103707; factors add essentially nothing beyond the market factor | CONFIRMED | Paper and finding confirmed by coverage (WBS, AFR); volume and article number not re-checked | https://wbs.ac.uk/news/flaw-data-corporate-bond-investors |
| Box 7.1. Data errors in the 2019 factors; 2019 paper retracted (JFE 150(3)) | CONFIRMED | Retraction confirmed; two factors lead error, one lag error, extreme returns truncated (search summary). The issue number was not re-checked | https://wbs.ac.uk/news/flaw-data-corporate-bond-investors |
| Box 7.1. Warwick Business School account dated 9 Sep 2024; calls it "the only time" the journal has retracted a paper | UNVERIFIABLE | The WBS page exists and describes the lead/lag errors, but the date and the "only time" wording were not seen. Hedge: drop the date and the quote, or re-open the page | https://wbs.ac.uk/news/flaw-data-corporate-bond-investors |
| Box 7.1. Mueller and Robotti receive the Fama-DFA Prize | CONFIRMED | WBS news item "Research on bond market wins Fama-DFA prize" with Robotti and Mueller (search result title) | https://www.wbs.ac.uk/news/research-bond-market-wins-fama-dfa-prize/ |
| Box 7.1. Jensen, Kelly, Pedersen, "Is There a Replication Crisis in Finance?", JF 78(5), 2023 | UNVERIFIABLE | Not looked up; recollection agrees but unchecked | none accessible |
| Box 7.1. arXiv:2604.07880 (9 Apr 2026): 108 signals, nine clusters, Aug 2002 - Dec 2024 (269 months), 52,656 unique bonds | CONFIRMED | "August 2002 to December 2024 (269 months), with 52,656" | https://arxiv.org/pdf/2604.07880 |
| Box 7.1. 432 specifications (108 x 2 x 2); 26 (6.0%) survive Benjamini-Hochberg | CONFIRMED | "Across 432 factor-specification combinations ... only 26 (6.0%)" | https://arxiv.org/pdf/2604.07880 |
| Box 7.1. Short-term reversal falls from -0.99% (t=-4.46) to -0.09% (t=-0.51) | CONFIRMED | Exact, plus "bias comprising over 90% of the documented effect" | https://arxiv.org/pdf/2604.07880 |
| Box 7.1. Abstract quote "the majority of previously documented factors do not produce statistically significant bond CAPM alphas after correction"; data and code released as Open Bond Asset Pricing | CONFIRMED | Verbatim | https://arxiv.org/pdf/2604.07880 |
| Box 7.2. MarketAxess CP+ launched May 2017 after about 18 months; more than 350,000 bonds; refreshes every 15 seconds | UNVERIFIABLE | Not searched (company claims, per the box) | none accessible |
| Box 7.2. SMU Cox study (March 2026) on CP+ | UNVERIFIABLE | Not searched | none accessible |
| Box 7.2. Bianchi, Buchner, Tamoni, RFS 34(2), 2021 | UNVERIFIABLE | Not looked up | none accessible |
| Box 7.2. Kelly, Palhares, Pruitt, JF 78(4), 2023; Robeco 23 Jun 2023 | UNVERIFIABLE | Not looked up | none accessible |
| Box 7.2. Feng, He, Wang, Wu, JBF 171: out-of-sample R-squared 4.48% | UNVERIFIABLE | Not looked up | none accessible |
| Box 7.2. BondBERT arXiv:2511.01869 (Oct 2025), about 30,000 UK bond-news articles | UNVERIFIABLE | Not looked up | https://arxiv.org/abs/2511.01869 (not opened) |
| Box 7.2. Bell, Kakhbod, Lettau, Nazemi, "Glass Box Machine Learning and Corporate Bond Returns", NBER WP 33320; JFE 181, 2026 | CONFIRMED | NBER page: issued Dec 2024, revised Jul 2025; JFE vol. 181 (2026), DOI 10.1016/j.jfineco.2026.104294 | https://www.nber.org/papers/w33320 |
| Box 7.2. 81 predictors, 1,207 firms, Jul 2002 - Aug 2020, nine-year test window, 10-1 portfolio 0.67% per month, alpha 0.55% (t=4.22) | UNVERIFIABLE | Not on the NBER abstract page; needs the full paper | https://www.nber.org/papers/w33320 |
| Box 7.2. SIFMA: US corporate-bond ADV $66.7bn through Sept 2026, up 13.4% y/y | UNVERIFIABLE | SIFMA statistics not opened | none accessible |
| Box 7.2. Man 2022: less than $150bn of US bonds traded electronically by quant investors in the prior year | CONFIRMED | "last year in the US less than $150 billion bonds were transacted electronically by quantitative investors" (attributed there to one data provider) | Man_Quantitative_Credit_Alpha_2022 p.3 (local PDF) |

## Summary

Claims checked: 186 (every figure or date in the 20 Trend Watch boxes of chapters 1-7, grouped where a sentence carries one source).

| verdict | count |
| :-- | --: |
| CONFIRMED | 105 |
| CORRECTED | 7 |
| STALE | 2 |
| UNVERIFIABLE | 72 |

By chapter (CONFIRMED / CORRECTED / STALE / UNVERIFIABLE): Ch1 21/2/0/8; Ch2 28/0/0/15; Ch3 12/2/0/7; Ch4 13/2/0/13; Ch5 11/1/0/10; Ch6 11/0/2/7; Ch7 9/0/0/12.

Effort. 42 WebFetch/WebSearch/curl calls (8 of them were PDFs that returned binary and were read locally with pdftotext) plus 8 EDGAR full-text API requests, which were one check run once per year. That is a little over the "about 40" budget. None of the boxes cites a URL, so no cited-URL pass was possible; local primary PDFs in source_pdfs/ were used wherever a box cites them. UNVERIFIABLE rows are mostly paywalled trade press (The DESK, IFR, Bloomberg Law, American Banker), the Bondwave report, and academic citation details that were not looked up. They are not a finding that the claim is wrong.

What the checks found:
- The only real errors are small: a 2021 e-share vintage mismatch (37%/27% vs Greenwich's own 34%/25%), "1,173 events" (borrowers), "HY stuck near 30-33% throughout" (25% in 2021), DCI's $7.5bn (assets, not price), and the Moody's report date (7 Aug 2025, not July).
- Two STALE items in the Ch6 CDS box (ISDA, July 2026 note supersedes the 2023 breadth trend and clearing shares).
- The numerically heaviest boxes hold up exactly: FRED spreads and ratios (Ch5), EDGAR 8-K counts and filer counts (Ch3), the TRACE timeline and the SEC order statistics (Ch2), the arXiv paper statistics (Ch1, Ch7), Man's trading statement (Ch4), ISDA 2023 counts (Ch6).
- The CHECK flags in Ch2 and Ch4 are resolved: 2021/2022 e-shares are 34/25 and 41/31 (Greenwich chart), and Man Fig. 4 column order is 2021 first.

Cross-box conflicts for the editor to resolve (not find/replace-able without a source):
1. Ch2 PT table: "8 Apr 2025, $89.7bn record day" vs Ch1/Ch2 "30 Sep 2025, $84.7bn single-day record" (Greenwich says Sept 30 was the record). One basis or one number is wrong.
2. Ch5 box 3 (Moody's, 5.3% in Aug 2026) vs Ch6 box 2 (US 5.0% in May 2026, forecast to fall to 3.5% by Dec 2026). If the 5.3% is right, the Ch6 forecast has been overtaken. Neither figure was verified.
3. Ch1 box 3: 22% (Chicago Fed, private placements as a share of corporate bonds, 2024) beside 48.4% (S&P MI via Insurance Business, NAIC broad definition, YE2025). Different denominators; say so.
4. Ch4 box 1: Man discretionary long-only credit $19.8bn (Mar 2025) to $27.7bn (Sep 2025) is a $8bn jump in six months. Check the Q1 2026 statement.
5. Ch6 box 3 BIS series is due for update: BIS has published end-2024, mid-2025 and end-2025 data since the cited release; bis.org/publ/otc_hy2605.htm returned 404, so the newer figures were not retrieved.
6. "Open Source Bond Asset Pricing" (Ch1, Ch4, Ch10, Ch11, App B) vs "Open Bond Asset Pricing" (the paper, Ch7). Pick one.

### Find/replace pairs for the editor (CORRECTED and STALE). Strings were verified to occur in book_src; `\$` is the book's own dollar escape.

C1a. File 01_ch01_anthology_and_landscape.md (Box 1.1; the line is long, match the string only)
- find: `Coalition Greenwich put IG e-trading at 37% and HY at 27% in 2021 (via IFR); at 48% and 33% in 2024`
- replace: `Coalition Greenwich put IG e-trading at 34% and HY at 25% in 2021 (its restated series) and at 48% and 33% in 2024`

C1b. File 04_ch04_inside_the_systematic_credit_industry.md (Box 4.2)
- find: `US IG e-trading reaches 37% and HY 27% of volume (Coalition Greenwich, via IFR, c. early 2022; date CHECK)`
- replace: `US IG e-trading reaches 34% and HY 25% of volume (Coalition Greenwich, *U.S. corporate bond trading in 2024 by the numbers*, January 2025)`

C2. File 01_ch01_anthology_and_landscape.md (Box 1.4)
- find: `in its 1,173-event history of soft credit events since 1979, about one in four ended in a hard default, with more than 70% of eventual hard defaults arriving within two years`
- replace: `in its sample of 1,173 borrowers with soft credit events since 1979, about one in four ended in a hard default, with more than 70% of eventual hard defaults after a distressed restructuring arriving within two years`

C3. File 03_ch03_pjt_rssg_cognitive_bridge.md (Box 3.1)
- find: `high yield was stuck near 30–33% throughout`
- replace: `high yield rose from 25% in 2021 to 31–33% in 2022–2024 and then stalled near a third`

C4. File 04_ch04_inside_the_systematic_credit_industry.md (Box 4.1)
- find: `Blackstone agrees to buy DCI, about \$7.5bn, on 30 November 2020`
- replace: `Blackstone agrees to buy DCI, a quant credit manager with about \$7.5bn of assets (terms undisclosed), on 30 November 2020`

C5 (Moody's report date; the cover says 7 August 2025). Five places:
- 03_ch03_pjt_rssg_cognitive_bridge.md: find `("US Credit Review & Outlook," July 2025)` replace `("US Credit Review & Outlook," 7 August 2025)`
- 03_ch03_pjt_rssg_cognitive_bridge.md: find `*US Credit Review & Outlook* (July 2025)` replace `*US Credit Review & Outlook* (7 August 2025)`
- 05_ch05_credit_probability_distributions.md: find `*US Credit Review & Outlook*, July 2025)` (occurs twice; replace all) replace `*US Credit Review & Outlook*, 7 August 2025)`
- 05_ch05_credit_probability_distributions.md: find `*US Credit Review & Outlook* (July 2025)` replace `*US Credit Review & Outlook* (7 August 2025)`
- Outside chapters 1-7 (not checked here): grep book_src for other `US Credit Review` citations; the Ch3 and Ch5 counts above were 2 and 3.

S1 (STALE). File 06_ch06_merton_and_intensity_models.md (Box 6.3). Source: ISDA, "CDS Market Dynamics: Five Years of Activity and a Record 2025", July 2026, https://www.isda.org/a/Pa0iE/CDS-Market-Dynamics-Five-Years-of-Activity-and-a-Record-2025.pdf
- find: `Breadth shrank: the number of reference entities trading in a quarter fell from 854 in Q1 2018 to 719 in Q1 2023`
- replace: `Breadth shrank: the number of reference entities trading in a quarter fell from 854 in Q1 2018 to 719 in Q1 2023, and has since held in a narrow range of about 710 to 760 names (751 in Q4 2025; ISDA, July 2026)`

S2 (STALE). Same file and source.
- find: `In Q1 2023, 51.2% of single-name notional and 87.4% of index notional was centrally cleared`
- replace: `In Q1 2023, 51.2% of single-name notional and 87.4% of index notional reported in the US was centrally cleared; by 2025 the shares were 63.1% and 78.1% (ISDA, July 2026)`

Optional hedge H1 (UNVERIFIABLE date, number confirmed elsewhere). File 03_ch03_pjt_rssg_cognitive_bridge.md
- find: `Moody's later put distressed restructurings at approximately 65% of all 2025 defaults (April 28, 2026)`
- replace: `Moody's later put distressed restructurings at roughly 65% of all 2025 defaults ("Lend, extend, and then...," May 18, 2026)`

Hedged wording for the highest-visibility UNVERIFIABLE items is in the table rows (Ch1 disclosed RFQ 38.6%, Barclays six-minute PT, Jan 2026 $61bn; Ch2 Apr 2025 $89.7bn, Bondwave figures, MarketAxess 20.6%; Ch5 recovery series; Ch6 First Trust, UBS, Quinn Emanuel; Ch7 citation details). Apply only if the source cannot be recovered before print.

Relayed instruction noted: the pacing cap is 97% of the window, not 90%. state/PROCESS.md already says so (line 53); nothing in this review depends on it and no book_src or state file other than this one was edited.

<!-- STATUS: COMPLETE -->
