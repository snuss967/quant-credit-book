# Appendix B: The Data & API Atlas

It is 11:40 p.m. Theo Marsh has fourteen browser tabs open and a spreadsheet called `data_sources_FINAL_v3.xlsx`.

"TRACE has every corporate bond trade," he says. "EDGAR has every credit agreement. FRED has the high-yield spread back to the nineties. So I can rebuild the credit market from public data and go home."

Ines Okafor doesn't look up. "Which of those rows did you check this week? A trade over \$5 million shows up on the tape as `5MM+`. The credit agreement is filed with its schedules left out and the pricing grid redacted. And since April, the FRED series you love keeps only three years of history. Every dataset is a hand history with some cards face down. Your job is to know which ones."

Mags Dunleavy, coat on: "Back in my day the data source was a guy named Lenny. Lenny had survivorship bias too. He only remembered the trades that worked."

ROBO, asked to "get all the bond data," has queued 4.1 million requests to `data.sec.gov` with no User-Agent header. It is about to find out what a 403 is.

This appendix is the reference to keep open next to every other chapter. By the end of it you will be able to: (i) say, for each major credit data source, what it is, who pays for it, and which fields carry signal; (ii) list how each one misleads you: stale prices, survivorship, look-ahead, caps, licensing; (iii) quantify how stale prices distort variance and beta, and correct for it; and (iv) give ROBO a strict, testable schema for a tidy bond panel. Every URL below was checked on 2026-10-17. Where we could not check a source, it has no link.

## B.0 How to Read an Atlas Entry (and Four Ways Data Lies)

Each entry gives **what it is**, **access & cost**, **key fields**, **gotchas**, and **used in**. Four failure modes come up in almost every entry, so we state them formally once. ROBO cannot enforce a vibe.

**Sin 1: Stale prices.** Let $r_t$ be the true log return, i.i.d. with variance $\sigma^2$. Suppose the observed price only partially adjusts each day: $p^{o}_t = (1-\theta)\,p_t + \theta\,p^{o}_{t-1}$, where $\theta\in[0,1)$ measures staleness. Then

$$r^{o}_t = (1-\theta)\sum_{k=0}^{\infty} \theta^{k} r_{t-k}, \qquad \operatorname{Var}(r^{o}_t) = (1-\theta)^2 \sigma^2 \sum_{k=0}^{\infty}\theta^{2k} = \frac{1-\theta}{1+\theta}\,\sigma^2 .$$

The lag-$h$ autocovariance is $\gamma_h = \theta^{h}\operatorname{Var}(r^o_t)$, so $\rho_1=\theta$. The long-run variance is untouched:

$$\sum_{h=-\infty}^{\infty}\gamma_h = \frac{1-\theta}{1+\theta}\sigma^2\Big(1 + \tfrac{2\theta}{1-\theta}\Big) = \sigma^2 .$$

Staleness does not remove risk. It spreads today's risk over the following days. With $\theta=0.6$, a bond shows 25% of its true daily variance (half the volatility) and 60% first-order autocorrelation. Betas take the same hit. If $r_t=\beta f_t+\epsilon_t$ and the factor is observed fresh, then $\operatorname{Cov}(r^o_t,f_{t-k})=(1-\theta)\theta^k\beta\sigma_f^2$. A contemporaneous regression recovers only $(1-\theta)\beta$. The Dimson (1979) sum of lagged betas recovers $\beta$, because $\sum_k(1-\theta)\theta^k=1$. This is part of why high-yield bonds look rate-insensitive in daily data (Chapter 8). A stale price is a calm price, and calm is the most expensive thing to be wrong about.

> **[SOURCE EXTRACTION]** *Ben_Dor_Quantitative_Credit_Portfolio_Management p.208:* "we attempt to directly identify and exclude observations that possibly reflect stale prices. Specifically, all bonds comprising the Corporate and High Yield indexes with a sequence of five or more unchanged quotes in any month are excluded from the eligible population of bonds for that month."
>
> **Annotation.** The Barclays team used two fixes. Sampling biweekly instead of daily lowers the effective $\theta$, and a run-length filter removes bonds whose quotes don't move. The run-length rule still works as a first screen on *evaluated* prices, because those repeat when nothing new arrives. A price carried forward from TRACE trades doesn't look like "unchanged quotes," though. It is a single trade price copied onto later rows, so our schema carries an explicit `days_stale` counter instead (§B.16). The derivation shows what the filter buys you: dropping the bonds with high $\theta$ pushes measured variance and beta back toward the truth. The price is a tilt toward liquid names, which is a factor exposure of its own (Chapter 9).

**Sin 2: Look-ahead.** A feature $X_{i,t}$ is admissible only if $X_{i,t}\in\mathcal{F}_t$. In code, that means you join on `knowledge_ts` (when you could have known it), never `effective_ts` (the date the value refers to). Some examples. A TRACE print executed at 4:58 p.m. and reported at 5:12 p.m. is known at 5:12. A downgrade effective Tuesday and published Thursday is known Thursday. An XBRL fact is known when the filing is accepted. Restated values must not overwrite originals in a backtest.

**Sin 3: Survivorship.** The universe at date $t$ is every bond that existed and was eligible at $t$, including bonds that later defaulted, were called, tendered, or matured. Today's index constituents, today's ETF holdings, and any "active securities" table are survivor-biased. In credit, the bonds that drop out are the defaulted ones, and they *are* the left tail.

**Sin 4: Licensing.** Ratings, CUSIPs, index levels, and composites come with contracts that limit storage, redistribution, and derived products. If you can't legally keep the data behind a backtest, you can't audit the backtest. That is a model risk.

> **[SOURCE EXTRACTION]** *Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.20:* "It is necessary to combine information from a number of different data sources in order to build up a picture of the price landscape in the credit markets. These include data from market runs, electronic platforms, TRACE data and dealer information."
>
> **Annotation.** No single source gives you the price. This appendix sorts the sources into three kinds: *public and lagged* (TRACE), *proprietary and fresh* (platform RFQs, dealer runs), and *model outputs* (composites, evaluated prices). If a model treats all three as interchangeable "prices," the noise in one leaks into labels built from another.

## B.1 FINRA TRACE: The Tape

**What it is.** FINRA's reporting and dissemination system for OTC fixed-income trades. It launched July 1, 2002, with a 75-minute deadline that fell to 15 minutes by July 1, 2005. All public corporate trades have been disseminated on receipt since January 9, 2006. Agency and primary-market trades were added in 2010, ABS/MBS in 2011, 144A dissemination in 2014, and Treasury reporting in 2017. *(Source: FINRA, TRACE Fact Book 2025, <https://www.finra.org/sites/default/files/2026-02/TRACE_FactBook_2025.pdf>.)*

**Access & cost.** TRACE comes in four layers, from freshest to most complete:

1. **Real-time feeds.** The Bond Trade Dissemination Service (BTDS) is the real-time corporate feed. Agency, securitized-product, and 144A trades have their own feeds. You license it from FINRA or, more often, through a market-data vendor, and it is priced like professional market data. We could not retrieve the current BTDS spec or fee schedule this session, so check both before you build a feed handler.
2. **Free views.** FINRA's site shows disseminated trades for individual bonds. The API Developer Center (<https://developer.finra.org/>) has a Query API and a dataset catalog. This is the public tape: sizes are capped and dealers are not identified.
3. **Enhanced Historical Data (EHD).** EHD includes "information previously not disseminated to the public, such as buy/sell indicators and counterparty (dealer or customer) information," and quantity "as reported and not subject to dissemination caps." FINRA "makes historical data available 6 months (18 months for Securitized Products) after the transaction date and publishes the information quarterly" (FINRA EHD product sheet, <https://www.finra.org/sites/default/files/TRACE_Enhanced_Historical_Data.pdf>). Coverage: corporate and 144A from July 1, 2002, agency from April 2010, structured products from May 2011. You need a Historical Data Agreement and pay fees. CUSIP and non-CUSIP versions are offered, the latter "for customers without a CUSIP license" (<https://www.finra.org/filing-reporting/trace/historic-academic-data>). Materials from 2016–2017 quote an 18-month corporate lag. The current page says 6.
4. **Academic Corporate Bond TRACE Data.** Available only to higher-education institutions, "on a 36-month delayed basis," with "masked identifying information regarding the dealer reporting each transaction." It includes 144A and non-disseminated trades. At launch the fee was \$500 per year plus a \$500 one-time set-up fee (FINRA Regulatory Notice 16-43, <https://www.finra.org/sites/default/files/notice_doc_file_ref/Regulatory-Notice-16-43.pdf>). Masked dealer IDs make dealer-network and inventory research possible, but nothing like them exists in production. Keep it on the research side of the wall.

Most researchers get TRACE Standard, Enhanced, and 144A tables through **WRDS**.

**Key fields.** CUSIP and FINRA symbol; execution date and time; *report* date and time; price; yield; quantity (capped publicly, true in EHD); buy/sell side; reporting- and contra-party type (dealer or customer); principal or agency capacity; commission flag; trade status and message sequence numbers; as-of and special-condition flags; ATS identifier; and the portfolio-trade modifier (from May 15, 2023).

**Dissemination caps.** On the public tape, investment-grade and unrated trades above \$5 million print as `5MM+`, and high-yield trades above \$1 million print as `1MM+`. True sizes appear only in historical products.

> **[SOURCE EXTRACTION]** *Ben_Dor_Quantitative_Credit_Portfolio_Management p.162:* "TRACE ... disseminates trade-by-trade corporate bond execution information within 15 minutes to all market participants. At this time, TRACE data are censored at \$5 million for investment grade and \$1 million for high-yield securities."
>
> **Annotation.** "Censored" is the statistically correct word. A capped print is right-censored, so volume sums and VWAPs built from the public tape are skewed toward small trades, and small trades tend to print on the wrong side of the spread. A 2026 desk does three things about it. It flags every capped print. It imputes true size from a tail fitted to EHD, for example a Pareto tail conditional on exceeding the cap. And it never trains on public-tape volumes while scoring on EHD volumes. One more trap: the cap depends on the rating *at trade time*. A fallen angel's cap drops from \$5mm to \$1mm on the day the downgrade becomes known, and §B.16 tests for exactly this.

**Reporting timing: the one-minute saga.** The 15-minute outer limit has applied to corporates since 2005. On September 20, 2024, the SEC approved SR-FINRA-2024-004, which cut the limit to one minute for fully electronic trades. Manual trades got a phase-in (15 minutes, then 10, then 5), and firms with fewer than 4,000 reported trades a year were exempt. "FINRA has not implemented the changes approved in File No. SR-FINRA-2024-004." Members pointed to allocations, portfolio trades, and voice or chat workflows. On September 16, 2025, the SEC approved SR-FINRA-2025-008, which *keeps* the 15-minute limit. The same filing lets dual broker-dealer/investment-adviser firms report the allocations of an aggregate order as a single report that includes the number of accounts (Release No. 34-103986, <https://public-inspection.federalregister.gov/2025-18147.pdf>). The record shows 82.9% of eligible trades executed between 8:00 a.m. and 6:15 p.m. were already reported within one minute in 2022. The rule mainly targeted the slow 17%, which is mostly blocks and voice trades, and those are the trades that carry information. Rule 6730 also sets 60 minutes for Treasuries, post-issuance CMOs, and specified pools; same day for CDOs and CMBS executed by 5:00 p.m.; and T+1 for List/Fixed Offering Price and Takedown trades (<https://www.finra.org/rules-guidance/rulebooks/finra-rules/6730>).

**What is *not* disseminated.** Under Rule 6750 (<https://www.finra.org/rules-guidance/rulebooks/finra-rules/6750>): affiliate trades; certain M&A transfers; List/Fixed Offering Price and Takedown trades; CMBS, CDOs, and CMOs that don't qualify for periodic dissemination; foreign sovereigns; and Treasuries other than on-the-run nominal coupons. Those on-the-run coupons have been disseminated end-of-day since March 25, 2024, with size caps, no participant IDs, and free next-day access for non-professional use (Regulatory Notice 24-06). CLO tranches fall under the CDO exclusion. They are *reported* to TRACE but not disseminated by transaction, so no public CLO tape exists.

**Gotchas.**
- *The tape is messages, not trades.* Cancellations, corrections, and reversals must be matched to the original by message sequence number. The rules differ before and after FINRA's February 2012 re-platform (Dick-Nielsen 2009, 2014).
- *Double counting.* An inter-dealer trade is reported by both sides, and agency trades can print twice.
- *Fat fingers.* Decimal shifts (1012.5 for 101.25) and one-print spikes that bounce back need explicit screens.
- *Two clocks.* Execution time and report time differ. A late report on a block is information in itself.
- *Settlement.* US corporates settle T+1 since May 28, 2024. Accrue interest to settlement date.

**Used in.** Chapters 2, 3, 7, 8, 9, 18, 19, 20, 22.

> **Trend Watch. The tape that almost got faster (2018–2026).** FINRA added transparency at the edges. Covered depository institutions began reporting Treasury, agency, and MBS trades on September 1, 2022. The portfolio-trade modifier and 60-minute Treasury reporting arrived May 15, 2023, and USD foreign sovereigns became reportable on November 6, 2023 (TRACE Fact Book 2025). End-of-day transaction data for on-the-run Treasuries began March 25, 2024. The historical corporate lag shrank from 18 months to 6. The core corporate tape, though, went in a circle. One-minute reporting was approved September 20, 2024, never implemented, and replaced on September 16, 2025, by a 15-minute limit plus aggregate allocation reporting. The MSRB rolled back the same day (SR-MSRB-2025-01). The 2018 SEC advisory-committee proposal to raise caps (up to \$10mm IG) has not changed the public tape. **Desk implication:** the 15-minute window and the caps are the information asymmetry your market-making model prices (Chapter 18). Treat both as fixed until a rule changes them. Keep the PT flag as a feature, because PT prints are priced as part of a basket, not bond by bond (Chapter 19).

## B.2 SEC EDGAR: The Legal Prose Warehouse

**What it is.** The SEC's filing system, holding 10-K and 10-Q financials (with XBRL), 8-K event disclosures, and the debt contracts filed as exhibits.

**Access & cost.** Free. The `data.sec.gov` APIs "do not require any authentication or API keys to access" (<https://www.sec.gov/edgar/sec-api-documentation>). `CIK##########` below is the zero-padded 10-digit CIK.
- Submissions: `https://data.sec.gov/submissions/CIK##########.json` ("typical processing delay of less than a second").
- Company facts: `https://data.sec.gov/api/xbrl/companyfacts/CIK##########.json`. Company concept: `.../api/xbrl/companyconcept/CIK##########/us-gaap/<Tag>.json`.
- Frames: `https://data.sec.gov/api/xbrl/frames/us-gaap/AccountsPayableCurrent/USD/CY2019Q1I.json`. Periods are written `CY2019` (annual), `CY2019Q1` (quarterly), and `CY2019Q1I` (instantaneous).
- Bulk files `companyfacts.zip` and `submissions.zip` are rebuilt nightly (around 3:00 a.m. ET). Use them for any large pull.

XBRL endpoints usually lag under a minute. There is no CORS support, so run your code server-side. Fair-access rules (<https://www.sec.gov/os/accessing-edgar-data>): "Current max request rate: 10 requests/second," and every request must carry a declared User-Agent of the form `Sample Company Name AdminContact@<sample company domain>.com`.

**Full-text search** (<https://www.sec.gov/edgar/search/efts-faq.html>) covers all electronic filings "since 2001," including "all attachments (such as exhibits)." It supports exact phrases, `OR`, `NOT`, `NEAR(n)` (default 10 words), and trailing wildcards. The JSON endpoint behind it on `efts.sec.gov` is undocumented, so assume it can change. This is the tool for a J.Crew-blocker screen: every exhibit since 2018 with *unrestricted subsidiary* within five words of *intellectual property* (Chapter 13).

**Credit-document exhibits** (Regulation S-K Item 601, <https://www.law.cornell.edu/cfr/text/17/229.601>): **EX-4** (indentures, supplemental indentures); **EX-10** ("every contract not made in the ordinary course of business that is material," which includes credit agreements, amendments, intercreditors, and joinders, usually attached to an 8-K under Item 1.01 or 2.03, or to a 10-Q); **EX-21** (subsidiaries, your starting point for the restricted/unrestricted map).

**Gotchas.**
- *The 10% hole.* Long-term debt that "does not exceed 10 percent of the total assets of the registrant and its subsidiaries on a consolidated basis" need not be filed (Item 601(b)(4)(iii)(A)).
- *Redactions.* Schedules may be omitted if they are listed (Item 601(a)(5)). Terms that are "both not material and is the type that the registrant treats as private or confidential" may be redacted (Item 601(b)(10)(iv)). Pricing grids often show up as `[***]`, so give your parser a redaction token.
- *Private issuers.* Issuers whose debt is 144A-for-life file nothing. Their documents sit in lender data rooms, on the private side.
- *XBRL look-ahead.* Frames returns, for each entity, the fact "that is last filed," so restatements overwrite originals. Rebuild point-in-time values from `companyfacts` using each fact's accession number and `filed` date, or better, the acceptance timestamp from submissions. Debt details often sit in custom extension tags that frames won't return.

**Used in.** Chapters 11, 13, 15, 25, 26.

## B.3 CourtListener, RECAP, PACER, and the Claims Agents

**What it is.** PACER is the judiciary's pay-per-page docket system. Free Law Project's CourtListener hosts the **RECAP Archive**, which mirrors PACER documents that users of the RECAP browser extension have already paid for. Claims agents run free case websites with dockets and claims registers.

**Access & cost.**
- **PACER** (<https://pacer.uscourts.gov/pacer-pricing-how-fees-work>): \$0.10 per page, capped at \$3 per document. The cap does not cover search results or reports that aren't case-specific. Audio is \$2.40 a file and opinions are free. Fees are waived in any quarter where you spend \$30 or less. Every docket refresh is billed again, so pull mega-case dockets incrementally with date filters.
- **CourtListener REST API v4** (docs now on the Free Law Project wiki, <https://wiki.free.law/c/courtlistener/help/api/rest/v4/overview>). Base URL `https://www.courtlistener.com/api/rest/v4/`. Authenticate with the header `Authorization: Token <token>`; the docs warn that "a common mistake is to forget the word 'Token'." Current defaults: "authenticated users may make up to 5 requests per minute, 50 requests per hour, and 125 requests per day," on a rolling window, with higher limits available through membership or commercial agreements. Use webhooks for docket alerts rather than polling.
- **RECAP Fetch** (<https://wiki.free.law/c/courtlistener/help/api/rest/v4/recap>): `POST /api/rest/v4/recap-fetch/` with `request_type` 1 (docket), 2 (PDF), or 3 (attachment page). It "uses your PACER credentials to purchase and download PACER content," runs asynchronously, and allows 30 requests a minute. The upload endpoint is "not available to the public."
- **Python.** `juriscraper` (<https://github.com/freelawproject/juriscraper>, BSD-2, Python 3.11+) parses court sites and "a variety of pages and reports within the PACER system."
- **Claims agents.** Stretto (<https://cases.stretto.com/>), Epiq (<https://dm.epiq11.com/>), and Verita Global (<https://www.veritaglobal.com/>), whose CaseView links point to the legacy KCC domain. Kroll Restructuring Administration (formerly Prime Clerk) and Omni Agent Solutions are the other majors; we could not open their sites this session. Agent sites are free, usually update faster than RECAP, and post claims registers in structured form.

**Key fields.** Dockets: court, case number, `pacer_case_id`, filing date, judge, parties, attorneys. Entries: number, date, description, and documents with `pacer_doc_id`. Claims: claim number, creditor, debtor entity, amount, priority (secured, 503(b)(9), priority, GUC), date filed. Rule 2019 statements become a time series of who is in the ad hoc group (Chapter 25).

> **Docket Diary.** A document is in RECAP only if someone with the extension bought it, so coverage favors mega-cases and misses the small-cap Chapter 11 your model needs. *The Ad Hoc Group, represented by counsel, notes that its Rule 2019 statement was amended four times and RECAP holds two of the versions.*

**Gotchas.** Docket text is free-form, so the same motion can carry a dozen different descriptions. Claim amounts are as *asserted*, not as allowed, and duplicate claims filed against several debtor entities inflate the totals. For look-ahead purposes, the right timestamp is when the entry appeared on the docket, not the date printed inside the PDF.

**Used in.** Chapters 13, 14, 16, 25.

## B.4 MSRB EMMA

**What it is.** EMMA (<https://emma.msrb.org/>) is the MSRB's free site for municipal trade data, official statements, continuing disclosures, statistics, and yield curves. Real-time and historical feeds are sold as MSRB subscriptions. Rule G-14 requires reporting to RTRS "as soon as practicable but no later than 15 minutes after the Time of Trade" (<https://www.msrb.org/Rules-and-Interpretations/MSRB-Rules/General/Rule-G-14>). One-minute amendments were approved September 20, 2024, and rescinded September 16, 2025.

**Gotchas.** Munis mask large trade sizes under their own conventions, so check RTRS dissemination rules before reusing TRACE cleaning code. Most issues almost never trade, which makes staleness worse than in HY corporates. A late continuing-disclosure filing is itself a credit signal.

**Used in.** Chapters 12, 22.

## B.5 CME Treasury Futures, MDP 3.0, and BrokerTec

**What it is.** CME lists the Treasury futures used for rate hedging (2-, 5-, and 10-year, Ultra 10-year, Bond, and Ultra Bond). It also owns **BrokerTec**, the inter-dealer central limit order book for cash Treasuries and repo, acquired with NEX Group in 2018. The real-time protocol is **MDP 3.0**: UDP multicast, Simple Binary Encoding (SBE), incremental and snapshot-recovery channels, and market-by-price and market-by-order books. History is sold through CME DataMine. CME's site returned HTTP 503 to automated requests this session, so we give no deep links.

**Access & cost.** Exchange licensing is per device or per enterprise, and an algorithm consuming the feed triggers non-display fees. DataMine is priced per dataset. Many shops buy normalized data rather than decode raw SBE.

**Key fields.** Contract and expiry, book levels and sizes, trades with the aggressor side, sequence numbers, exchange timestamps, settlement prices, and open interest. Add the deliverable basket and conversion factors, which you need for cheapest-to-deliver (CTD) and futures DV01 (Chapters 8, 24).

**Gotchas.** When you see a sequence gap, recover from the snapshot channel; never interpolate across it. Futures DV01 jumps when the CTD changes. Rolls move liquidity between contracts, and back-adjusted series give correct returns but wrong levels. BrokerTec shows only the inter-dealer market. Client flow, which is where the information is, trades on dealer-to-client RFQ platforms.

**Used in.** Chapters 8, 22, 24, 27.

## B.6 OPRA, Cboe, and Options Data

**What it is.** **OPRA** (<https://www.opraplan.com/>) is the securities information processor for US listed options. It disseminates consolidated "last sale and quotation information," volume, open interest, and end-of-day summaries from BOX, Cboe, MEMX, MIAX, Nasdaq, and NYSE options venues. Its 2026 notices add IEX Options and MX2 Options, extend trading hours effective September 21, 2026, and upgrade hardware. **Cboe DataShop** (<https://datashop.cboe.com/>) sells Option EOD Summary (with a 3:45 p.m. ET snapshot), interval Option Quotes, and Option Trades, with optional implied volatility and Greeks and an academic discount. OptionMetrics IvyDB, usually through WRDS, is the academic standard for volatility surfaces.

**Access & cost.** OPRA charges vendor and subscriber fees under its fee schedule. For credit work, a daily or 3:45 p.m. surface snapshot per issuer is enough for Merton/CreditGrades inputs, put-vs-CDS comparisons, and skew-implied jump-to-default (Chapter 23).

**Gotchas.** The options "close" is a quote snapshot, and it isn't synchronized with the equity close, which produces false put-call parity violations. Early exercise and dividends bias naive Black–Scholes implied vols in the deep out-of-the-money puts that carry the default signal. Corporate actions change contract terms.

**Used in.** Chapters 8, 23, 27.

## B.7 Index Data: ICE BofA, Bloomberg, iBoxx/CDX/iTraxx, and FRED

**What it is.**
- **ICE BofA** (<https://www.ice.com/fixed-income-data-services/index-solutions>): "over 6,000" fixed-income indices, including US High Yield (H0A0) and US Corporate (C0A0). ICE says its index history on Snowflake Marketplace spans "50 years."
- **Bloomberg** (the former Lehman/Barclays family): Aggregate, Corporate, High Yield, and the Very Liquid versions. JNK tracks the Bloomberg High Yield Very Liquid Index.
- **iBoxx, CDX, iTraxx** belong to S&P Global since its 2022 merger with IHS Markit. HYG tracks the iBoxx USD Liquid High Yield Index. CDX and iTraxx roll to a new series every six months.
- **FRED** republishes ICE BofA OAS: **BAMLH0A0HYM2** (HY, <https://fred.stlouisfed.org/series/BAMLH0A0HYM2>) and **BAMLC0A0CM** (IG, <https://fred.stlouisfed.org/series/BAMLC0A0CM>). On 2026-10-15 they were 3.23% and 0.84%, i.e., 323 bp and 84 bp (FRED, accessed 2026-10-17). The FRED API (<https://fred.stlouisfed.org/docs/api/fred/>) includes `fred/series/vintagedates` for real-time vintages.

**Access & cost.** Constituent-level data (weights, prices, OAS, duration, ratings by bond) is licensed and expensive. Index-level series are cheaper.

**Gotchas.**
- *Month-end rebalancing.* A bond downgraded mid-month stays in the IG index until the month-end rebalance, and fallen-angel selling clusters on those dates (Chapter 9).
- *Index prices are evaluated, bid-side prices* (§B.8). Index OAS is smoothed, so §B.0 applies.
- *Excess-return definitions differ.* Some families use duration-matched Treasuries, others swaps. Don't mix them in one regression.
- *CDX rolls.* An on-the-run series jumps in level on the roll date, so splice explicitly.
- *FRED is shrinking.* The series notes now say "Starting in April 2026, this series will only include 3 years of observations. For more data, go to the source." They also say "Copyright, 2023, ICE Data Indices. Reproduction of this data in any form is prohibited," and the data is "provided for your internal use only."

**Used in.** Chapters 2, 8, 9, 10, 11, 12, 20.

> **Trend Watch. Free data giveth, and free data taketh away (2018–2026).** In 2018 one line of `pandas-datareader` pulled decades of daily HY OAS from FRED. Since April 2026, FRED keeps three years and sends you "to the source," while ICE sells 50 years of history on Snowflake. CourtListener's default authenticated allowance is now 125 requests a day. Academic open data went the other way. The Open Source Bond Asset Pricing project released TRACE-based panels and factor libraries, with its Stage 1 daily panel in public beta on 2025-12-11, and FINRA's EHD corporate lag fell to 6 months. **Desk implication:** cache everything free in a versioned, point-in-time local store, because free data disappears. License what production depends on. Reconcile the open panels against vendor data so you notice when either one drifts.

## B.8 Composite and Evaluated Pricing: Model Outputs Dressed as Prices

**What it is.**
- **MarketAxess CP+** (<https://www.marketaxess.com/price/cp-plus>) covers IG, HY, EM, loans, munis, sovereigns, and rates. It is built from "proprietary MarketAxess trading activity, TRACE, TraX, and other market signals," including inquiries that never traded. MarketAxess says it prices "80% more bonds than public sources alone," and delivers via FIX API, OMS feeds, and an Excel add-in.
- **Tradeweb Ai-Price** is a machine-learning price for bonds that haven't traded recently, with confidence measures. **Bloomberg BVAL** is an evaluated price with a BVAL Score that grades how much market evidence supports it. **ICE evaluated pricing**, including continuous evaluated pricing, is the incumbent for fund NAVs. Others include S&P Global and LSEG evaluated pricing and BondCliQ quotes. We could not open the Tradeweb, Bloomberg, or ICE pricing pages this session, so read their methodology documents before you depend on them.

**Access & cost.** Enterprise licenses, with limits on redistribution and on how long you may store the data.

**Key fields.** Bid, mid, and ask; timestamp; confidence or score; methodology tier (based on trades vs. based on comparable bonds).

**Gotchas.**
- *Circularity.* Composites are built partly from TRACE. If you train on composite labels with TRACE features, part of what you predict is your own input. Validate on *subsequent* trades (markouts).
- *Staleness.* A bond with no new information follows its comparables, so its $\theta$ sits well above zero. Use the score field to set observation weights.
- *Bid-side NAVs.* Credit ETF NAVs are struck from bid-side evaluated prices. In March 2020, part of the "discount" of HYG and LQD to NAV was the NAV being stale (Chapter 20).
- *Licensing.* Composite contracts often forbid long histories or index-building. Read them before you build a 20-year backtest.

**Used in.** Chapters 7, 18, 19, 20.

> **Trend Watch. Pricing became a product (2018–2026).** Trading venues turned their order-flow data into pricing products (CP+, Ai-Price), and evaluated-pricing vendors sped up their updates. A portfolio trade, flagged in TRACE since May 15, 2023, is priced against composite mids, and the dealer's markup is measured against them (Chapter 19). **Desk implication:** your pricing engine competes with the composites. Log both prices on every RFQ, and show the edge as better markouts on the same trades.

## B.9 Ratings-Agency Default Studies

**What it is.** S&P Global Ratings publishes an annual global corporate default and rating-transition study. Moody's publishes an annual study of corporate default and recovery rates since 1920. Fitch publishes default studies and loan and HY default indices. SEC Rule 17g-7(b) requires rating agencies to publish their rating-action histories in XBRL, with a lag, which gives you free (if awkward) point-in-time ratings.

**Access & cost.** Summaries are often free after registration. Full data and production rating feeds are licensed. The trace-data-pipeline public download leaves out some columns "because agency ratings are licensed."

**Gotchas.** Results depend on how a study handles withdrawn ratings. Distressed exchanges count as defaults (S&P "SD"; Moody's distressed exchanges). In the LMT era that changes the recovery distribution and leads to re-defaults (Chapter 14). Default rates are physical-measure, through-the-cycle numbers. Using them as $\mathbb{Q}$ hazards without a risk premium understates spreads, which is the credit spread puzzle (Chapter 6). Join ratings on publication time, not effective date.

**Used in.** Chapters 5, 6, 11, 14.

## B.10 Academic Bond Panels: OBAP, WRDS Bond Returns, Mergent FISD

**Open Source Bond Asset Pricing** (<https://openbondassetpricing.com/>), run by Alexander Dickerson and coauthors, publishes "108 Bond Factors," 341 factors from *Factor Investing with Delays*, a bond-level ML panel with 341 predictors (2002-07 to 2022-12), duration-matched Treasury returns, and replication packages. Its **trace-data-pipeline** (<https://github.com/Alexander-M-Dickerson/trace-data-pipeline>, MIT license) works in stages. Stage 0 turns Enhanced, Standard, and 144A TRACE into daily panels using Dick-Nielsen (2009, 2014) and van Binsbergen–Nozawa–Schwert (2025) filters, a decimal-shift corrector (10×, 0.1×, 100×, 0.01×), a bounce-back filter, agency de-duplication, and an ultra-distressed flag. Stage 1 adds QuantLib analytics, ratings, and FISD terms. Stage 2 builds 108 monthly signals. Stages 0–1 need WRDS. §B.16 is a teaching-scale version of Stages 0–1.

**WRDS Bond Returns** (<https://wrds-www.wharton.upenn.edu/pages/grid-items/wrds-bond-returns/>) is a monthly panel of prices, returns, coupons, and yields built from TRACE Standard and Enhanced, starting July 2002, with a bond-to-equity link table built through CRSP. Its month-end price rule, meaning which late-month trade counts as the month-end price, moves measured reversal and factor premia. That sensitivity is the subject of Dickerson et al., *The Corporate Bond Factor Replication Crisis*.

**Mergent FISD** (via WRDS) is the academic security master. It holds offering terms, coupon type, maturity, seniority, 144A and convertible flags, call, put, and sink schedules, covenant indicators, and histories of amount outstanding and ratings. **Gotchas:** coverage of small and private issues is patchy. Amount-outstanding updates lag tenders and exchanges, and in an LMT the change in amount outstanding *is* the event. CUSIPs are licensed.

**Used in.** Chapters 7, 9, 10, 11.

## B.11 Leveraged Loans and CLOs

**What it is.** There is no public loan tape. In *Kirschner v. JPMorgan Chase* (2d Cir. 2023), the court held that the syndicated term-loan notes at issue were not securities. The sources you have: the **LSTA** (<https://www.lsta.org/>), which publishes market analysis such as its *BSL Market Monthly* (built on the Morningstar LSTA Leveraged Loan Index), settlement standards, and documentation; PitchBook LCD for new issues and defaults; and dealer-quote mark services such as LSEG's. CLO data comes from Intex (waterfalls), monthly trustee reports (collateral, OC/IC tests, CCC buckets), rating-agency surveillance, and Creditflux's CLO-i. TRACE collects CLO tranche trades but does not disseminate them (§B.1).

**Gotchas.** Loan "prices" are averages of dealer quotes, not trades. Settlement takes days to weeks. Repricings and amend-and-extends change a loan's terms without changing its identifier. Trustee reports arrive monthly and late, so the forced-seller signal from a CCC bucket (Chapter 21) is about a month stale.

**Used in.** Chapters 12, 16, 17, 21.

## B.12 ETF Holdings Files

**What it is.** Under SEC Rule 6c-11 (2019), most US ETFs post full holdings every day. iShares pages include "Download latest fund holdings CSV data." HYG (<https://www.ishares.com/us/products/239565/ishares-iboxx-high-yield-corporate-bond-etf>) launched April 4, 2007. SPDR pages offer a daily `.xlsx`. JNK (<https://www.ssga.com/us/en/intermediary/etfs/spdr-bloomberg-high-yield-bond-etf-jnk>) launched November 28, 2007. The files are free to download, and each sponsor's terms govern redistribution.

**Key fields.** As-of date, name, identifiers (ISIN, sometimes CUSIP), par, market value, weight, price, and sector, plus coupon, maturity, duration, and yield for bond funds. Layouts differ by sponsor, so write one parser per sponsor and test each against a stored sample file.

**Gotchas.** The holdings file is not the creation basket, because custom baskets are allowed (Chapter 20). Each file overwrites the last one. If you don't archive daily, you have no history and every backtest is survivor-biased. Cash, futures, and CDS overlays need special handling. File prices are the sponsor's evaluated prices, not trades.

**Used in.** Chapters 2, 19, 20.

## B.13 CDS Public Data (Brief)

Index CDS (CFTC swap repositories) and, since early 2022, single-name CDS (SEC Regulation SBSR; *date approximate*) have public tapes, with capped sizes and painful entity mapping. Use them for activity and basis signals (Chapter 24) and buy levels from a vendor.

## B.14 Open-Source Tooling

| Tool | What it does | Verified notes (2026-10-17) |
| :--- | :--- | :--- |
| `edgartools` (<https://github.com/dgunning/edgartools>) | EDGAR filings, XBRL statements, full-text search | MIT; Python 3.11+; call `set_identity("name@example.com")` first; stays within 10 req/s |
| OpenBB Open Data Platform (<https://github.com/OpenBB-finance/OpenBB>) | One data layer for public and licensed providers (Python, REST, MCP) | `pip install openbb`; Apache-2.0; Python 3.10–3.14; `openbb-api` serves on port 6900 |
| `pandas-datareader` (<https://pandas-datareader.readthedocs.io/en/latest/>) | Remote readers, including FRED | 0.11.2 dev build in the docs (July 2026); FRED now returns 3 years for ICE series |
| `juriscraper` | Court and PACER parsing | BSD-2; Python 3.11+ |
| trace-data-pipeline / PyBondLab | TRACE cleaning, analytics, factors | MIT; Stages 0–1 need WRDS |
| `wrds`, `QuantLib`, `fredapi` | WRDS SQL; bond math; FRED client | Not re-verified this session |

> **Ways This Blows Up.** When a provider changes its terms (FRED's window, CourtListener's limits, EDGAR's User-Agent rule), the wrappers break *quietly*. A call that returns three years of OAS where it used to return thirty raises no exception. It just deletes 2008 from your regime model. Assert row counts and date ranges on every pull, and fail the job if history shrinks.

## B.15 Case Study: A Fallen Angel Through Every Lens

Here is what a fallen angel looks like as data, using the synthetic bond `SYN-IG-B` from the code below (all numbers *illustrative*). The rating agency's downgrade from BBB- to BB+ takes effect on June 10 and is published on June 12. On EDGAR, an 8-K Item 2.03 filing earlier in the year attached an amendment as EX-10.1 with its pricing grid redacted. On the TRACE tape, large prints switch from `5MM+` to `1MM+` on June 12, not June 10. A model that joins on effective date "knows" about the cap change two days early. Index data keeps the bond in the IG index until the June month-end rebalance, which is when forced selling clusters. The ETF holdings file shows the IG fund's position disappearing at the rebalance, and the HY fund's holdings file shows the bond showing up the next day. Composites mark it down gradually, because they move with the comparables at a $\theta$ well above zero. Daily returns built from composites understate the move's volatility, and a Dimson-summed beta to HYG recovers it.

The desk's job is to line these five clocks up by `knowledge_ts`. That alignment is a feature in its own right. The gap between the downgrade's knowledge time and the index rebalance is the forced-selling window that Chapters 9 and 20 trade.

## B.16 Specification for AI Implementation: The Tidy Bond Panel

**The Spec You Hand the Robot.** *What ROBO built from the vague version ("make me a daily bond price table"):* it took the last trade of each day and forward-filled across holidays and weekends. It dropped the defaulted bond because its yield failed to solve. It joined ratings on effective date. Every one of those choices ships a bias into production. Here is the precise version.

| Table | Key | Required columns (units) | Rules |
| :--- | :--- | :--- | :--- |
| `secmaster` | `bond_id` | coupon (decimal), maturity, offering_amt (\$ par), security_level, rule_144a, freq, day_count | One row per bond; IDs are synthetic in tests, CUSIPs in production (licensed) |
| `ratings` | (`bond_id`, `knowledge_ts`) | effective_ts, knowledge_ts, rating, rating_num (1 = AAA … 22 = D) | As-of join on `knowledge_ts` only |
| `msgs` | `msg_seq` | trc_st ∈ {T, X, C}, orig_msg_seq, exec_ts, report_ts, price (% of par), qty_true (\$ par), side ∈ {B, S, D} | Simplified status codes; map FINRA's real codes per vintage (pre/post 2012) |
| `trades` | `msg_seq` | + rating at trade, cap, qty_dissem, qty_capped, flags | No cancelled or corrected originals; screens for decimal shifts and bounce-backs |
| `daily` | (`bond_id`, `date`) | px_clean, px_vwap_dissem, n_trades, par_volume, days_stale, is_stale, status, accrued, ytm, dur_mod, spread (decimal), dts (yr·bp) | Full business-day grid until maturity; defaulted bonds kept, flagged `trades_flat` |
| `monthly` | (`bond_id`, `month_end`) | px_eom, accrued, cpn_paid, ret_total | Month-end price only if `days_stale` ≤ 5; else NaN, never filled |

Edge cases the code must handle: settlement on T+1 business day; 30/360 accrual to settlement; flat trading (zero accrued, no yield) after default; caps keyed to point-in-time rating; Brent bracket of $[-5\%, 500\%]$ for distressed yields. Sanity checks: price–yield round trip to $10^{-8}$; analytic vs. finite-difference duration to $10^{-6}$; a par bond priced on a coupon date equals 100; and a Monte Carlo check of the §B.0 result $\operatorname{Var}(r^o)/\sigma^2=(1-\theta)/(1+\theta)$, $\rho_1=\theta$. The spread is a curve-interpolated G-spread against an *illustrative* Nelson–Siegel curve, not OAS. Requires pandas ≥ 2.2.

```python
# Tidy bond panel from a synthetic TRACE-like tape. Bond ids are synthetic labels, NOT CUSIPs.
import numpy as np
import pandas as pd
from scipy.optimize import brentq

RNG = np.random.default_rng(20261017)
IG_CAP, HY_CAP = 5_000_000, 1_000_000          # dissemination caps (par $)
RATING_SCALE = {"AAA": 1, "AA+": 2, "AA": 3, "AA-": 4, "A+": 5, "A": 6, "A-": 7,
                "BBB+": 8, "BBB": 9, "BBB-": 10, "BB+": 11, "BB": 12, "BB-": 13,
                "B+": 14, "B": 15, "B-": 16, "CCC+": 17, "CCC": 18, "CCC-": 19,
                "CC": 20, "C": 21, "D": 22}
IG_MAX_NUM = RATING_SCALE["BBB-"]

# ---------------------------------------------------------------- 1. security master
secmaster = pd.DataFrame({
    "bond_id":        ["SYN-IG-A", "SYN-IG-B", "SYN-HY-C", "SYN-HY-D"],
    "issuer_id":      ["ISS1", "ISS2", "ISS3", "ISS4"],
    "coupon":         [0.0450, 0.0525, 0.07875, 0.0950],
    "maturity":       pd.to_datetime(["2033-06-15", "2031-03-01", "2030-09-15", "2029-12-01"]),
    "offering_date":  pd.to_datetime(["2023-06-15", "2021-03-01", "2022-09-15", "2021-12-01"]),
    "offering_amt":   [1_500_000_000, 750_000_000, 600_000_000, 400_000_000],
    "security_level": ["SEN", "SEN", "SEN", "SUB"],
    "rule_144a":      [False, False, True, False],
    "freq":           [2, 2, 2, 2],
    "day_count":      ["30/360"] * 4,
})

# ------------------------------------------------- 2. point-in-time ratings history
# join on knowledge_ts (publication), never effective_ts
ratings = pd.DataFrame({
    "bond_id":      ["SYN-IG-A", "SYN-IG-B", "SYN-IG-B", "SYN-HY-C", "SYN-HY-D", "SYN-HY-D"],
    "effective_ts": pd.to_datetime(["2023-06-01", "2021-02-20", "2026-06-10", "2022-09-01",
                                    "2021-11-20", "2026-08-14"]),
    "knowledge_ts": pd.to_datetime(["2023-06-01", "2021-02-20", "2026-06-12", "2022-09-01",
                                    "2021-11-20", "2026-08-17"]),
    "rating":       ["A-", "BBB-", "BB+", "B", "CCC", "D"],
})
ratings["rating_num"] = ratings["rating"].map(RATING_SCALE).astype("int64")
DEFAULT_DATE = {"SYN-HY-D": pd.Timestamp("2026-08-14")}

# ------------------------------------------------------------- 3. bond math (30/360)
def d30360(d1, d2):
    """US 30/360 (bond basis) day count between two Timestamps."""
    D1 = min(d1.day, 30)
    D2 = d2.day
    if D2 == 31 and D1 >= 30:
        D2 = 30
    return 360 * (d2.year - d1.year) + 30 * (d2.month - d1.month) + (D2 - D1)

def coupon_dates(maturity, freq=2, start=None):
    months = 12 // freq
    out, d, k = [], maturity, 0
    while start is None or d > start - pd.DateOffset(months=months):
        out.append(d)
        k += 1
        d = maturity - pd.DateOffset(months=months * k)
        if start is None and k > 400:
            break
    return sorted(out)

def schedule(settle, maturity, freq=2):
    """(previous coupon date, list of future coupon dates) relative to settle."""
    dates = coupon_dates(maturity, freq, start=settle)
    future = [d for d in dates if d > settle]
    past = [d for d in dates if d <= settle]
    prev = past[-1] if past else future[0] - pd.DateOffset(months=12 // freq)
    return prev, future

def accrued(settle, maturity, coupon, freq=2):
    prev, _ = schedule(settle, maturity, freq)
    return 100.0 * coupon / freq * d30360(prev, settle) / (360.0 / freq)

def dirty_from_yield(y, settle, maturity, coupon, freq=2):
    prev, fut = schedule(settle, maturity, freq)
    w = d30360(settle, fut[0]) / (360.0 / freq)          # fraction of period to next coupon
    k = np.arange(len(fut))
    cf = np.full(len(fut), 100.0 * coupon / freq)
    cf[-1] += 100.0
    return float(np.sum(cf / (1.0 + y / freq) ** (w + k)))

def clean_from_yield(y, settle, maturity, coupon, freq=2):
    return dirty_from_yield(y, settle, maturity, coupon, freq) - accrued(settle, maturity, coupon, freq)

def yield_from_clean(p_clean, settle, maturity, coupon, freq=2):
    f = lambda y: clean_from_yield(y, settle, maturity, coupon, freq) - p_clean
    return brentq(f, -0.05, 5.0, xtol=1e-12)              # bracket: -5% to 500%

def mod_duration(y, settle, maturity, coupon, freq=2):
    prev, fut = schedule(settle, maturity, freq)
    w = d30360(settle, fut[0]) / (360.0 / freq)
    n = w + np.arange(len(fut))
    cf = np.full(len(fut), 100.0 * coupon / freq)
    cf[-1] += 100.0
    pv = cf / (1.0 + y / freq) ** n
    macaulay_years = np.sum((n / freq) * pv) / np.sum(pv)
    return float(macaulay_years / (1.0 + y / freq))

def tsy_curve(T, b0=0.042, b1=-0.005, b2=0.010, tau=2.0):
    """Synthetic Nelson-Siegel par curve (illustrative), bond-equivalent decimal."""
    T = np.maximum(np.asarray(T, dtype=float), 1e-6)
    x = T / tau
    return b0 + b1 * (1 - np.exp(-x)) / x + b2 * ((1 - np.exp(-x)) / x - np.exp(-x))

# ----------------------------------------------- 4. simulate "true" paths and a tape
bdays = pd.bdate_range("2026-03-02", "2026-09-30")
y0 = {"SYN-IG-A": 0.0480, "SYN-IG-B": 0.0590, "SYN-HY-C": 0.0760, "SYN-HY-D": 0.1350}
vol = {"SYN-IG-A": 0.0006, "SYN-IG-B": 0.0010, "SYN-HY-C": 0.0020, "SYN-HY-D": 0.0060}
lam = {"SYN-IG-A": 6.0, "SYN-IG-B": 4.0, "SYN-HY-C": 2.0, "SYN-HY-D": 1.5}
half_spread = {"SYN-IG-A": 0.10, "SYN-IG-B": 0.20, "SYN-HY-C": 0.40, "SYN-HY-D": 1.00}

rows, seq = [], 0
for _, b in secmaster.iterrows():
    y = y0[b.bond_id]
    for d in bdays:
        y += vol[b.bond_id] * RNG.standard_normal()
        if b.bond_id == "SYN-IG-B" and d >= pd.Timestamp("2026-06-10"):
            y += 0.0004                                   # fallen-angel drift
        settle = d + pd.offsets.BDay(1)                   # US corporates settle T+1
        defaulted = b.bond_id in DEFAULT_DATE and d >= DEFAULT_DATE[b.bond_id]
        if defaulted:
            true_px = 31.0 + 2.0 * RNG.standard_normal()  # trades flat near recovery
        else:
            true_px = clean_from_yield(max(y, 0.0), settle, b.maturity, b.coupon)
        for _ in range(RNG.poisson(lam[b.bond_id] * (2.0 if defaulted else 1.0))):
            side = RNG.choice(["B", "S", "D"], p=[0.4, 0.4, 0.2])   # cust buy/sell, dealer
            sgn = {"B": 1.0, "S": -1.0, "D": 0.0}[side]
            px = round(true_px + sgn * half_spread[b.bond_id] + 0.05 * RNG.standard_normal(), 3)
            median_qty = 1_000_000 if b.bond_id.startswith("SYN-IG") else 500_000
            qty = float(np.clip(np.round(RNG.lognormal(np.log(median_qty), 1.0), -3), 1_000, 25_000_000))
            exec_ts = d + pd.Timedelta(hours=9, minutes=30) + pd.Timedelta(seconds=int(RNG.integers(0, 6.5 * 3600)))
            seq += 1
            rows.append(dict(msg_seq=seq, orig_msg_seq=np.nan, trc_st="T", bond_id=b.bond_id,
                             exec_ts=exec_ts, report_ts=exec_ts + pd.Timedelta(seconds=int(RNG.integers(1, 900))),
                             price=px, qty_true=qty, side=side))
msgs = pd.DataFrame(rows)

# inject tape pathologies: cancels, corrections, a decimal shift, a bounce-back print
t_idx = msgs.index[msgs.trc_st == "T"]
cancel_targets = RNG.choice(t_idx, size=6, replace=False)
fix_targets = RNG.choice(np.setdiff1d(t_idx, cancel_targets), size=6, replace=False)
extra = []
for i in cancel_targets:
    r = msgs.loc[i].to_dict(); seq += 1
    r.update(msg_seq=seq, orig_msg_seq=msgs.at[i, "msg_seq"], trc_st="X")
    extra.append(r)
for i in fix_targets:
    r = msgs.loc[i].to_dict(); seq += 1
    r.update(msg_seq=seq, orig_msg_seq=msgs.at[i, "msg_seq"], trc_st="C", price=round(r["price"] + 0.25, 3))
    extra.append(r)
msgs = pd.concat([msgs, pd.DataFrame(extra)], ignore_index=True)
ig_a = msgs.index[(msgs.bond_id == "SYN-IG-A") & (msgs.trc_st == "T")]
msgs.loc[ig_a[100], "price"] *= 10.0                      # decimal-shift typo
msgs.loc[ig_a[200], "price"] += 7.0                       # bounce-back spike
msgs["orig_msg_seq"] = msgs["orig_msg_seq"].astype("Int64")

# ------------------------------- 5. point-in-time rating join (no look-ahead allowed)
def pit_rating(df, ts_col):
    left = df.sort_values(ts_col)
    right = ratings.sort_values("knowledge_ts")[["bond_id", "knowledge_ts", "rating", "rating_num"]]
    out = pd.merge_asof(left, right, left_on=ts_col, right_on="knowledge_ts", by="bond_id",
                        direction="backward", allow_exact_matches=True)
    assert (out["knowledge_ts"] <= out[ts_col]).all(), "look-ahead in rating join"
    return out

# --------------------------------------------- 6. clean the tape (Dick-Nielsen-lite)
def clean_tape(m):
    m = m.copy()
    cancelled = set(m.loc[m.trc_st == "X", "orig_msg_seq"].dropna().astype(int))
    corrected = set(m.loc[m.trc_st == "C", "orig_msg_seq"].dropna().astype(int))
    keep = (m.trc_st.isin(["T", "C"])) & ~m.msg_seq.isin(cancelled | corrected)
    t = m.loc[keep].copy()
    t = t.sort_values(["bond_id", "exec_ts"]).reset_index(drop=True)
    # decimal-shift and bounce-back screens against a rolling median of neighbours
    med = t.groupby("bond_id")["price"].transform(lambda s: s.rolling(11, center=True, min_periods=3).median())
    ratio = t["price"] / med
    t["flag_decimal"] = (ratio > 5) | (ratio < 0.2)
    prev_ = t.groupby("bond_id")["price"].shift(1)
    next_ = t.groupby("bond_id")["price"].shift(-1)
    jump_out = (t["price"] - prev_).abs()
    jump_back = (next_ - t["price"]).abs()
    t["flag_bounce"] = (jump_out > 3.0) & (jump_back > 3.0) & ((next_ - prev_).abs() < 1.0) & ~t["flag_decimal"]
    t = t.loc[~(t.flag_decimal | t.flag_bounce)].copy()
    # point-in-time rating -> dissemination cap the public tape would have shown
    t = pit_rating(t, "exec_ts")
    t["cap"] = np.where(t["rating_num"] <= IG_MAX_NUM, IG_CAP, HY_CAP)
    t["qty_dissem"] = np.minimum(t["qty_true"], t["cap"])
    t["qty_capped"] = t["qty_true"] > t["cap"]
    t["date"] = t["exec_ts"].dt.normalize()
    return t

trades = clean_tape(msgs)

# ------------------------------------------------ 7. bond-day panel on a full grid
def vwap(g, qty_col):
    return float(np.sum(g["price"] * g[qty_col]) / np.sum(g[qty_col]))

agg = (trades.groupby(["bond_id", "date"])
       .apply(lambda g: pd.Series({
           "px_vwap_true": vwap(g, "qty_true"),
           "px_vwap_dissem": vwap(g, "qty_dissem"),
           "px_last": g.sort_values("exec_ts")["price"].iloc[-1],
           "n_trades": len(g),
           "par_volume": g["qty_true"].sum(),
           "n_capped": int(g["qty_capped"].sum()),
           "cust_buy_par": g.loc[g.side == "B", "qty_true"].sum(),
           "cust_sell_par": g.loc[g.side == "S", "qty_true"].sum(),
       }), include_groups=False)
       .reset_index())

grid = pd.MultiIndex.from_product([secmaster.bond_id, bdays], names=["bond_id", "date"]).to_frame(index=False)
daily = grid.merge(agg, on=["bond_id", "date"], how="left").merge(secmaster, on="bond_id", how="left")
daily = daily.loc[daily["date"] < daily["maturity"]].copy()      # never drop defaulted bonds
daily = daily.sort_values(["bond_id", "date"]).reset_index(drop=True)
daily["traded"] = daily["n_trades"].fillna(0).astype("int64") > 0
daily["n_trades"] = daily["n_trades"].fillna(0).astype("int64")
daily["par_volume"] = daily["par_volume"].fillna(0.0)
daily["last_trade_date"] = daily["date"].where(daily["traded"])
daily["last_trade_date"] = daily.groupby("bond_id")["last_trade_date"].ffill()
daily["px_clean"] = daily.groupby("bond_id")["px_vwap_true"].ffill()          # carried price
daily["days_stale"] = [np.busday_count(l.date(), d.date()) if pd.notna(l) else np.nan
                       for l, d in zip(daily["last_trade_date"], daily["date"])]
daily["days_stale"] = daily["days_stale"].astype("float64")
daily["is_stale"] = daily["days_stale"] > 0
daily["status"] = np.where([b in DEFAULT_DATE and d >= DEFAULT_DATE[b] for b, d in zip(daily.bond_id, daily.date)],
                           "defaulted", "performing")
daily["trades_flat"] = daily["status"].eq("defaulted")
daily = pit_rating(daily, "date").sort_values(["bond_id", "date"]).reset_index(drop=True)

def analytics(r):
    if pd.isna(r.px_clean):
        return pd.Series({"accrued": np.nan, "ytm": np.nan, "dur_mod": np.nan, "tsy_yld": np.nan,
                          "spread": np.nan, "dts": np.nan})
    settle = r.date + pd.offsets.BDay(1)
    ai = 0.0 if r.trades_flat else accrued(settle, r.maturity, r.coupon)
    if r.trades_flat:                                   # yields are meaningless once flat
        return pd.Series({"accrued": ai, "ytm": np.nan, "dur_mod": np.nan, "tsy_yld": np.nan,
                          "spread": np.nan, "dts": np.nan})
    y = yield_from_clean(r.px_clean, settle, r.maturity, r.coupon)
    dmod = mod_duration(y, settle, r.maturity, r.coupon)
    T = (r.maturity - settle).days / 365.25
    ty = float(tsy_curve(T))
    s = y - ty
    return pd.Series({"accrued": ai, "ytm": y, "dur_mod": dmod, "tsy_yld": ty, "spread": s,
                      "dts": dmod * s * 1e4})          # DTS in years x bp
daily = pd.concat([daily, daily.apply(analytics, axis=1)], axis=1)

# ------------------------------------------- 8. monthly returns (stale-aware rule)
def monthly_returns(dp, max_stale_days=5):
    d = dp.copy()
    d["month_end"] = d["date"] + pd.offsets.BMonthEnd(0)
    me = d.loc[d["date"] == d["month_end"]].copy()
    ok = me["days_stale"] <= max_stale_days
    me["px_eom"] = np.where(ok, me["px_clean"], np.nan)
    me = me.sort_values(["bond_id", "month_end"])
    me["px_prev"] = me.groupby("bond_id")["px_eom"].shift(1)
    me["ai_prev"] = me.groupby("bond_id")["accrued"].shift(1)
    # coupon paid in (prev, this]: detected by an accrued-interest reset (approximation)
    me["cpn_paid"] = np.where((me["accrued"] < me["ai_prev"]) & ~me["trades_flat"],
                              100.0 * me["coupon"] / me["freq"], 0.0)
    me["ret_total"] = (me["px_eom"] + me["accrued"] + me["cpn_paid"]) / (me["px_prev"] + me["ai_prev"]) - 1.0
    return me[["bond_id", "month_end", "px_eom", "accrued", "cpn_paid", "ret_total",
               "days_stale", "rating", "status", "spread", "dur_mod", "dts"]].reset_index(drop=True)

monthly = monthly_returns(daily)

# --------------------------------------------------------- 9. schema + sanity checks
DAILY_SCHEMA = {"bond_id": "str", "date": "datetime", "px_clean": "float",
                "px_vwap_dissem": "float", "n_trades": "int", "par_volume": "float",
                "days_stale": "float", "is_stale": "bool", "rating": "str",
                "rating_num": "int", "status": "str", "accrued": "float",
                "ytm": "float", "dur_mod": "float", "spread": "float", "dts": "float"}
KIND_CHECK = {"str": pd.api.types.is_string_dtype, "datetime": pd.api.types.is_datetime64_any_dtype,
              "float": pd.api.types.is_float_dtype, "int": pd.api.types.is_integer_dtype,
              "bool": pd.api.types.is_bool_dtype}
for col, kind in DAILY_SCHEMA.items():
    assert col in daily.columns, f"missing column {col}"
    assert KIND_CHECK[kind](daily[col]), f"{col}: dtype {daily[col].dtype} is not {kind}"
assert not daily.duplicated(["bond_id", "date"]).any(), "panel key not unique"
assert (daily["date"] < daily["maturity"]).all()
assert "SYN-HY-D" in set(monthly.loc[monthly.status == "defaulted", "bond_id"]), "survivorship: defaulted bond dropped"
# no cancelled or corrected originals survive
dead = set(msgs.loc[msgs.trc_st.isin(["X", "C"]), "orig_msg_seq"].dropna().astype(int))
assert not trades["msg_seq"].isin(dead).any()
assert not trades["price"].gt(200).any(), "decimal-shift print survived"
# price-yield round trip and duration vs finite difference
s0, m0, c0 = pd.Timestamp("2026-04-15"), pd.Timestamp("2031-03-01"), 0.0525
y_rt = yield_from_clean(97.25, s0, m0, c0)
assert abs(clean_from_yield(y_rt, s0, m0, c0) - 97.25) < 1e-8
h = 1e-6
fd = -(dirty_from_yield(y_rt + h, s0, m0, c0) - dirty_from_yield(y_rt - h, s0, m0, c0)) / (2 * h) / dirty_from_yield(y_rt, s0, m0, c0)
assert abs(fd - mod_duration(y_rt, s0, m0, c0)) < 1e-6
# par bond on a coupon date prices at par
assert abs(clean_from_yield(0.0525, pd.Timestamp("2026-03-01"), m0, c0) - 100.0) < 1e-9
# fallen angel: the cap switches from $5mm to $1mm once the downgrade is KNOWN
fa = trades.loc[trades.bond_id == "SYN-IG-B"]
assert (fa.loc[fa.exec_ts < "2026-06-12", "cap"] == IG_CAP).all()
assert (fa.loc[fa.exec_ts >= "2026-06-13", "cap"] == HY_CAP).all()
# stale-price theorem check: EWMA smoothing shrinks variance by (1-theta)/(1+theta)
theta, n = 0.6, 400_000
r = RNG.standard_normal(n)
ro = np.empty(n); ro[0] = (1 - theta) * r[0]
for i in range(1, n):
    ro[i] = theta * ro[i - 1] + (1 - theta) * r[i]
var_ratio = ro[1000:].var() / r[1000:].var()
rho1 = np.corrcoef(ro[1001:], ro[1000:-1])[0, 1]
assert abs(var_ratio - (1 - theta) / (1 + theta)) < 0.01 and abs(rho1 - theta) < 0.01

print(f"messages={len(msgs)}, clean trades={len(trades)}, capped prints={int(trades.qty_capped.sum())}")
print(f"daily panel rows={len(daily)}, stale share={daily.is_stale.mean():.1%}")
print(f"var ratio={var_ratio:.4f} (theory {(1-theta)/(1+theta):.4f}), rho1={rho1:.4f}")
print(monthly.to_string(index=False, float_format=lambda v: f"{v:.4f}"))
```

## B.17 Desk Debrief

- **Every price has a clock.** Store `exec_ts`, `report_ts`, and `knowledge_ts` separately, and join only on knowledge.
- **Staleness hides risk; it doesn't remove it.** Observed variance shrinks by $(1-\theta)/(1+\theta)$, and summing lagged betas brings the full beta back.
- **The public TRACE tape is censored** at \$5mm IG and \$1mm HY. The cap follows the bond's point-in-time rating.
- **The 15-minute window survived.** One-minute reporting was approved in 2024 and abandoned in 2025, for both TRACE and the MSRB.
- **EDGAR misses the 10% hole, the redactions, and every 144A-for-life issuer.** Your covenant model has a coverage map whether you draw it or not.
- **Free data shrinks.** FRED's ICE series now keep 3 years and CourtListener allows 125 requests a day by default. Cache, version, and assert row counts.
- **Composites are model outputs.** Validate against later trades, never against themselves.
- **IDO or it didn't happen**, and IDO on stale prices didn't happen either.

**The Spec You Hand the Robot (summary).** "Build `daily` on a full business-day grid per bond until maturity. Never drop defaulted bonds; flag them `trades_flat`. Clean messages by matching X and C records to originals by `orig_msg_seq`. Join ratings by `merge_asof` on `knowledge_ts` and assert there is no look-ahead. Compute caps from point-in-time ratings. Carry prices forward only with an explicit `days_stale`, and leave a month-end return as NaN when `days_stale` > 5. Enforce dtypes by kind, keep keys unique, and pass the price–yield, duration, par, and staleness checks, or fail the build."

**Exercises.**
1. Estimate $\theta$ for each bond in `daily` from $\rho_1$ of returns on days with trades. Compare it with the variance-ratio estimate. Which one is more robust when trading days are irregular?
2. Fit a Pareto tail to `qty_true` above \$1mm for HY prints. Impute sizes for `1MM+` prints and measure the bias you remove from a capped VWAP.
3. Using the EDGAR full-text syntax, write a query for 8-K exhibits that pair "unrestricted subsidiary" with "intellectual property," and list three ways it gives false positives.
4. Kaz insists the frames API is fine for backtests "because restatements are rare." Design a test that measures how often a `companyfacts` value for a debt tag changes between its first and last `filed` date.

### Deep-Dive Resource Graph

**Podcasts.** Bloomberg's *Odd Lots* (market-structure, TRACE, and portfolio-trading episodes); *Flirting with Models* (Corey Hoffstein) on systematic data hygiene.

**Practitioner Writing.** Matt Levine, *Money Stuff* (on bond-market transparency and the "price" of untraded bonds); MarketAxess TraX and CP+ research; Free Law Project's CourtListener documentation (<https://wiki.free.law/c/courtlistener/help/api/rest/v4/overview>).

**Academic Papers.** Dick-Nielsen (2009), *Liquidity Biases in TRACE*; Dick-Nielsen (2014), *How to Clean Enhanced TRACE Data*; Dimson (1979), *Risk Measurement When Shares Are Subject to Infrequent Trading*; Getmansky, Lo & Makarov (2004), *An Econometric Model of Serial Correlation and Illiquidity in Hedge Fund Returns*; Edwards, Harris & Piwowar (2007), *Corporate Bond Market Transaction Costs and Transparency*; Bessembinder, Kahle, Maxwell & Xu (2009), *Measuring Abnormal Bond Performance*; Bai, Bali & Wen (2019), *Common Risk Factors in the Cross-Section of Corporate Bond Returns*; Dickerson, Mueller & Robotti (2023), *Priced Risk in Corporate Bonds*; Dickerson, Robotti & Rossetti, *The Corporate Bond Factor Replication Crisis* (working paper).

**Data & Code.** FINRA TRACE historic data (<https://www.finra.org/filing-reporting/trace/historic-academic-data>); SEC EDGAR APIs (<https://www.sec.gov/edgar/sec-api-documentation>); RECAP Fetch (<https://wiki.free.law/c/courtlistener/help/api/rest/v4/recap>); FRED HY OAS (<https://fred.stlouisfed.org/series/BAMLH0A0HYM2>); OBAP pipeline (<https://github.com/Alexander-M-Dickerson/trace-data-pipeline>); edgartools (<https://github.com/dgunning/edgartools>); OpenBB (<https://github.com/OpenBB-finance/OpenBB>). All other verified links appear inline above.
