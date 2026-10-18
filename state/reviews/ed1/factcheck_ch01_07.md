# Fact-check: Trend Watch boxes, chapters 1-7

Checked 2026-10-18 against state/digests/trend_watch_boxes.md (boxes from 01_ch01 .. 07_ch07 only). No book_src file was edited.
Method: none of the boxes in chapters 1-7 cites a URL, so there was no cited URL to fetch first. Local primary PDFs in source_pdfs/ were checked where a box cites them (no web call); everything else via WebSearch/WebFetch (budget about 40 calls).
Verdicts: CONFIRMED / CORRECTED / STALE / UNVERIFIABLE.

STATUS: PARTIAL (in progress)

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

