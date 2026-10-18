# Fact-check: Trend Watch boxes, chapters 22-28

Checked 2026-10-18 against state/digests/trend_watch_boxes.md (boxes from 22_ch22 .. 27_ch27). The digest stops at chapter 27, so the three chapter 28 boxes were read directly from book_src/28_ch28_pm_playbook.md. Nine further boxes that exist in book_src but not in the digest (chapters 22, 23, 24, 27) are listed in a separate Supplement and only partly checked. No book_src file was edited.
Method: cited URLs and primary documents were fetched first (WebFetch), then WebSearch for the rest. Local primary PDFs (source_pdfs/, state/pdf_pages/) were checked with no web call where a box cites them. Web calls used: 52 (budget was about 40; nine of the extra calls were exact re-runs of the EDGAR full-text counts and three went on chapter 28, which the digest omits).
Verdicts: CONFIRMED (the source says it) / CORRECTED (source says something different) / STALE (superseded) / UNVERIFIABLE (no accessible source; "not checked" = no source opened in this pass, "not found" = searched and not located).
Tables are one per box, grouped under chapter headings. Final status marker is the last line of this file.

## Chapter 22: Market structure, regulation, trends (3 boxes)

Source note: FINRA notices 22-12, 25-17 and 26-16 and the ISDA study were fetched at the primary URL. Where a verdict rests only on trade press, the evidence column says so.

### Box 22-A: dealer corporate-bond inventories, 2007-2026

| claim | verdict | evidence / correct figure | source |
| :--- | :--- | :--- | :--- |
| Dealer corporate holdings peaked at roughly $235bn in 2007 (FR 2004) | CONFIRMED (approx.) | IFR, citing NY Fed primary-dealer data: peak US$235bn in 2007. Other estimates of the same series differ ("more than $230bn" per Goldman via Better Markets; "over $250bn" per the FRED blog), so "roughly" is right. None of the retrieved sources names the form "FR 2004"; they call it the Fed primary dealer survey of corporate securities due in more than one year. The category included private-label MBS before 2013, which supports the box's own upper-bound caveat. | https://www.ifre.com/story/1700121/dealer-inventory-slump-threatens-market-stability ; https://fredblog.stlouisfed.org/2015/10/illiquidity-in-the-bond-market/ |
| ...cut by about three-quarters by 2012 | CONFIRMED (approx.) | IFR: low of $40bn in mid-2012 (a fall of about 83% from $235bn); Better Markets/Goldman: "fell more than 75%". "About three-quarters" is the conservative end; "by 75-80%" would be safer. Not worth an edit. | https://www.ifre.com/story/1700121/dealer-inventory-slump-threatens-market-stability |
| Average long inventories were about $16bn in 2017 | CONFIRMED | Bloomberg report carried by Hedgeweek: dealers "carried a peak $16 billion of average inventory over 2017" (Crisil Coalition Greenwich analysis of Fed figures). | https://www.hedgeweek.com/banks-turn-net-short-corporate-bonds-for-first-time-as-market-structure-shifts/ |
| Primary dealers averaged a net short of about $4bn in US corporates "so far in 2026", "the first time in at least 25 years" (Crisil Coalition Greenwich, FR 2004) | CONFIRMED (trade press) | Same Hedgeweek/Bloomberg piece: average net short around $4bn so far in 2026; first net short in at least 25 years. Decomposition: net short about $13.7bn in bonds maturing in 5+ years offset by a $9.66bn long in shorter-dated debt (13.7 - 9.66 = 4.04, consistent). Figures run to end-June 2026 and cover cash bonds only (no CDS offsets). The retrieved coverage does not name "FR 2004" (it says "Federal Reserve figures"); Coalition Greenwich's own note is "Why dealers are net short corporate bonds" (Data Spotlight, 15 Jun 2026). Suggest adding "through end-June 2026" to "so far in 2026". | https://www.hedgeweek.com/banks-turn-net-short-corporate-bonds-for-first-time-as-market-structure-shifts/ ; https://www.greenwich.com/printpdf/158770 |
| In late 2024 Coalition Greenwich described dealers as short about $3.8bn of IG corporates longer than five years, and the market as "agency (or at most, riskless principal)" | UNVERIFIABLE | Two searches found no Greenwich text with the $3.8bn figure or the quoted phrase. Hedged wording: "In late 2024 Coalition Greenwich was already describing dealers as net short in longer-dated IG corporates, and the market as largely agency or riskless-principal trading *(figure not independently verified)*." Or drop the $3.8bn and the quote and rely on the 2026 data above. | n/a (searched greenwich.com) |

### Box 22-B: TRACE and adjacent reporting regimes (Table 22.1)

| claim | verdict | evidence / correct figure | source |
| :--- | :--- | :--- | :--- |
| 2002-07: TRACE dissemination begins, phased by size and rating | CONFIRMED | TRACE launched 1 Jul 2002; Phase I covered the largest, higher-credit issues. | https://www.finra.org/sites/default/files/2014-TRACE-Fact-Book.pdf |
| 2006-01-09: immediate dissemination of all public TRACE-eligible corporates | CONFIRMED | Fact books: all transactions in public TRACE-eligible securities disseminated immediately on receipt from 9 Jan 2006. | https://www.finra.org/sites/default/files/2017-trace-fact-book.pdf |
| 2017-07-10: Treasuries reportable (regulatory use only) | CONFIRMED | Regulatory Notice 16-39: members report Treasury trades to TRACE beginning 10 Jul 2017; "at this time, FINRA will not disseminate" them. | https://www.finra.org/rules-guidance/notices/16-39 |
| 2022-02-14: SBSR public dissemination of security-based swaps incl. single-name CDS (approx.; trade press) | CONFIRMED (secondary only) | Clarus: public dissemination under SEC Regulation SBSR went live 14 Feb 2022, first time single-name CDS prints are public. No SEC or DTCC release retrieved, so keep the "approx." tag. | https://www.clarusft.com/2022/02/23/ |
| 2022-09-01: covered depository institutions report Treasury trades | CONFIRMED | FINRA: from 1 Sep 2022, Covered Depository Institutions report Treasuries, agency debt and agency MBS to TRACE (Fed FR 2956 collection, announced in the Federal Register 28 Oct 2021). | https://www.finra.org/filing-reporting/trace/federal-reserve-depository-institution-reporting |
| 2023-05-15: portfolio-trade modifier mandatory | CONFIRMED (date) | Regulatory Notice 22-12 (24 May 2022): "will take effect on May 15, 2023"; SEC approval 4 Mar 2022. The parenthetical definition (">=10 issues, single basket price") was not on the retrieved page and was not separately checked. | https://www.finra.org/rules-guidance/notices/22-12 |
| 2024-03-25: end-of-day dissemination of individual on-the-run nominal Treasury trades (approx.; Rule 6750) | CONFIRMED | Regulatory Notice 24-06: end-of-day data product takes effect 25 Mar 2024 (historic data product 1 Apr 2024); on-the-run nominal coupons only; trade sizes capped. The "approx." tag can go. | https://www.finra.org/rules-guidance/notices/24-06 |
| 2024-05-28: T+1 settlement for corporates | CONFIRMED | SEC T+1 compliance date 28 May 2024; FINRA RN 24-04 conforming amendments operative the same day. (Secondary summaries: Davis Polk, Kelley Drye; SEC rule text not fetched.) | https://www.davispolk.com/insights/client-update/sec-adopts-t-1-settlement-effective-may-2024 |
| 2025-12-04: one-minute reporting abandoned (approved, never effective) | CORRECTED (date label) | The one-minute rule was SEC-approved 20 Sep 2024 (SR-FINRA-2024-004, Rel. 101121) and never took effect. It was rescinded by SR-FINRA-2025-008, approved 16 Sep 2025 (Rel. 103986). 2025-12-04 is the date of FINRA Regulatory Notice 25-17, which announced it ("not moving forward"), not the date of the legal change. Column is headed "Effective". | https://www.finra.org/sites/default/files/2025-12/Regulatory-Notice-25-17.pdf (endnotes 2, 9) |
| 2026-06-08: optional aggregate allocation reports (Rule 6730.08) for dual BD/IA firms | CONFIRMED | RN 25-17: "The amendments will become effective on June 8, 2026"; reporting under new Supplementary Material .08 is optional. | https://www.finra.org/rules-guidance/notices/25-17 |
| 2026-08-31: affiliate indicator extended to member affiliates, voluntary | CONFIRMED | RN 26-16 (26 Aug 2026): "Members may begin reporting ... on a voluntary basis beginning on August 31, 2026"; SEC order 24 Jul 2026 (Rel. 105991, 91 FR 47909). | https://www.finra.org/rules-guidance/notices/26-16 |
| 2027-08-02: affiliate indicator mandatory | CONFIRMED | RN 26-16: "The effective date ... by which compliance is mandatory is August 2, 2027." | https://www.finra.org/rules-guidance/notices/26-16 |
| One June 2026 industry estimate put duplicate affiliate prints at up to 8% of HG TRACE volume (approx.) | CONFIRMED (attribution tweak) | MarketAxess's own monthly volume releases (Apr, May, Jun 2026): "The Company estimates that duplicate trade reports inflated U.S. high-grade TRACE volumes by up to 8% in June 2026". It is one firm's estimate, not an industry estimate. Suggest "a June 2026 MarketAxess estimate". | https://s201.q4cdn.com/767283836/files/doc_news/2026/07/07/MKTX-Volume-Release-June-2026-Final.pdf |
| "at least four definitional breaks" in raw TRACE volume, 2020-2027 | CONFIRMED (derived) | Table itself lists 2022-09-01, 2023-05-15, 2024-05-28 (settlement fields), 2026-06-08, 2026-08-31 and 2027-08-02 within 2020-2027. | (table) |

### Box 22-C: Treasury clearing volumes and the compliance path

| claim | verdict | evidence / correct figure | source |
| :--- | :--- | :--- | :--- |
| Adopted 2023-12-13 | UNVERIFIABLE (low risk) | Not retrieved in this pass: DTCC and trade-press pages confirm the extension but not the adoption day. The extension orders confirm the original dates below, consistent with a Dec 2023 adoption. Hedged wording: "adopted December 2023". | n/a |
| Original dates: cash 2025-12-31, repo 2026-06-30 | CONFIRMED | Arnold & Porter advisory lists original dates 31 Dec 2025 (cash) and 30 Jun 2026 (repo). | https://arnoldporter.com/en/perspectives/advisories/2025/03/us-treasury-clearing-sec-extends-compliance-dates |
| Extended 2025-02-25 to cash 2026-12-31, repo 2027-06-30 | CONFIRMED | SEC order of 25 Feb 2025 moved dates by 12 months; DTCC: "December 31, 2026, for cash transactions and June 30, 2027, for repo transactions". | https://www.dtcc.com/insights/2025/navigating-the-new-timeline-sec-extension-for-us-treasury-clearing-compliance |
| ...margin separation enforced from 2025-09-30 | CONFIRMED (loose label) | Same SEC action: temporary exemption from Rule 17ad-22(e)(6)(i) so covered clearing agencies need not enforce segregation of indirect-participant margin until 30 Sep 2025 (original 31 Mar 2025). It is a clearing-agency rule date, not a repo-margin date. | https://www.thetradenews.com/sec-extends-us-treasury-clearing-compliance-deadline-in-bid-to-help-firms-implement-necessary-risk-management-changes/ |
| CME approved December 2025 | CONFIRMED | SEC approved CME Securities Clearing's clearing-agency registration on 1 Dec 2025 (Federal Register 4 Dec 2025). | https://worktraining.com/knowledge/sec-grants-registration-to-cme-securities-clearing-as-new-clearing-agency-for-us-treasury-securities |
| ICE approved in early 2026 | CONFIRMED | ICE Clear Credit Treasury clearing "receives SEC approval and is now operationally live" (Business Wire, 3 Feb 2026); repo clearing planned for Q4. | https://www.businesswire.com/news/home/20260203400787/en/ICE-Clear-Credits-Treasury-Clearing-Service-Receives-SEC-Approval-and-is-Now-Operationally-Live |
| No further delay found as of October 2026 | UNVERIFIABLE | Searches returned nothing dated after Feb 2026 on the 31 Dec 2026 cash date. Keep the box's own "(check before relying on it)". With the cash date about 10 weeks out, recheck at proof stage. | n/a |
| FICC GSD cleared a peak $11.8trn on 2025-06-30 (prior peak $11.4trn on 2025-04-09) | CONFIRMED | DTCC release (2 Jul 2025): peak $11.8trn on 30 Jun; previous high $11.4trn on 9 Apr. No later one-day peak turned up in a 2026 search. Watch item: a late-July 2026 DTCC survey says FICC now clears "more than $12 trillion in average daily transactions" across cash and repo (different measure, via The Asian Banker); reconcile before calling $11.8trn the current ceiling. | https://www.dtcc.com/news/2025/july/02/ficc-successfully-processes |
| Sponsored Service record $2.48trn the same day | CONFIRMED | DTCC: "over USD$2.48 Trillion" in Sponsored activity, prior record $2.11trn on 30 Apr. | https://www.dtcc.com/news/2025/july/02/ficc-successfully-processes |
| MMF FICC-cleared reverse repo up $132bn (11%) to $1.3trn in June 2026 (approx.; OFR via trade press) | CONFIRMED (trade press only) | Risk.net: FICC-cleared MMF reverse repos hit a record in June, up $132bn (11%) to $1.3trn, largest monthly rise of 2026, OFR data. OFR's own June 2026 dataset not retrieved; keep "approx.". | https://www.risk.net/risk-quantum/7963919/ficc-cleared-mmf-reverse-repos-hit-record-high-in-june |

## Chapter 23: Cross-asset convexity and the vol surface (1 box)

| claim | verdict | evidence / correct figure | source |
| :--- | :--- | :--- | :--- |
| In 2002 CreditGrades was a dealer-consortium product sold as a screen | CONFIRMED (consortium, date); "sold as a screen" unchecked | CreditGrades Technical Document dated May 2002, published by four institutions: Deutsche Bank, Goldman Sachs, JPMorgan and RiskMetrics Group, with model outputs provided online at creditgrades.com. RiskMetrics is not a dealer, so "dealer-consortium" is slightly loose ("three dealers and RiskMetrics"). The retrieved text says outputs were published online; it does not say they were sold. Hedged wording: "a 2002 consortium product of three dealers and RiskMetrics Group, with outputs published online". | https://www.msci.com/research-and-insights/paper/creditgrades-technical-document ; https://www.risk.net/node/1505455 |
| Cremers, Driessen, Maenhout and Weinbaum (2008, *J. Banking & Finance*) found option-implied volatility beats historical volatility in explaining both the cross-section and time series of spreads, level mattering most and the skew "to a lesser extent" | CONFIRMED | JBF 32(12), 2706-2715, "Individual stock-option prices and credit spreads". Abstract: implied volatilities of individual options improve on historical volatilities across firms and over time; "both the level of individual implied volatilities and (to a lesser extent) the implied-volatility skew matter". The retrieved pages did not print the JBF author line (it is the same four-author group as BIS WP 191); do not confuse with the RFS 2008 jump-premium paper (Cremers, Driessen, Maenhout). | https://research.tilburguniversity.edu/en/publications/individual-stock-option-prices-and-credit-spreads/ |
| Zhang, Zhou and Zhu (2009, *Rev. Financial Studies*): high-frequency equity volatility alone explains 48% of CDS-level variation, jump risk alone 19%, and 73% with ratings, macro and balance-sheet controls | CONFIRMED (published version) | RFS 2009 abstract (catalogue listing): volatility risk alone 48%, jump risk alone 19%, 73% with controls. Earlier working-paper versions (FEDS 2005-63, BIS WP 181) report 50%, 19%, 77%, so cite the RFS numbers, as the box does. | https://www.federalreserve.gov/econres/feds/explaining-credit-default-swap-spreads-with-the-equity-volatility-and-jump-risks-of-individual-firms.htm (WP); RFS DOI 10.1093/rfs/hhp004 |
| Blackstone describes a default-probability model using "real-time equity market signals" (Blackstone_Systematic_Credit p.1) | UNVERIFIABLE (as a Blackstone statement) | The phrase is on p.1 of the local file ("...capital structure, cash flows, leverage, and real-time equity market signals to calculate daily, dynamic default probabilities"). But the file is a Google Docs export with no byline, no citations and the voice of a generated summary ("Here is a nuanced breakdown of the architecture..."), not a Blackstone publication. Attribution to Blackstone is not established. Hedged wording below. | /home/user/quant-credit-book/source_pdfs/Blackstone_Systematic_Credit.pdf (p.1) |
| BlackRock's PD model uses "market data of equity and bond instruments" (BlackRock_Systematic_High_Yield_Credit p.6) | CONFIRMED | p.6: "The probability of default model uses accounting, market data of equity and bond instruments, bond ratings, and other economic variables to estimate the probability of default for the issuer over a forward looking 12-month period." Genuine BlackRock marketing paper ("A systematic approach to high yield credit", code BSYSH1225U). | /home/user/quant-credit-book/source_pdfs/BlackRock_Systematic_High_Yield_Credit.pdf (p.6) |

## Chapter 24: Bond-CDS basis and deliverables (1 box)

Every figure below was checked against the primary document: ISDA Research Note, "CDS Market Dynamics: Five Years of Activity and a Record 2025", July 2026 (ISDA web post dated 29 Jul 2026), text extracted from the PDF.

| claim | verdict | evidence / correct figure | source |
| :--- | :--- | :--- | :--- |
| ISDA July 2026 study, 29 Jul 2026, title as given | CONFIRMED | Research Note dated July 2026; web post at isda.org/2026/07/29/. | https://www.isda.org/2026/07/29/cds-market-dynamics-five-years-of-activity-and-a-record-2025/ |
| Record global CDS traded notional $41.8tn in 2025, above the 2022 peak of $38.7tn | CONFIRMED | "record $41.8 trillion in 2025, surpassing the previous peak of $38.7 trillion in 2022". | https://www.isda.org/a/Pa0iE/CDS-Market-Dynamics-Five-Years-of-Activity-and-a-Record-2025.pdf (p.1-2) |
| Index CDS was 93.3% of it; share near 90% every year | CONFIRMED | "93.3% of the market in 2025 and around 90% every year" (index $39.0tn, record; prior peak $36.4tn in 2022). | same, p.2 |
| Single-name notional peaked at $3.3tn in 2023, eased to $2.8tn in 2025 | CONFIRMED | "peaked at $3.3 trillion in 2023 ... before easing to $2.8 trillion in 2025". | same, p.2 and p.11 |
| 2023 was "the year of the regional-bank and Credit Suisse stress" | CONFIRMED | Q1 2023 coincided with the failures of Silicon Valley Bank and Signature Bank and the UBS acquisition of Credit Suisse. | same, p.6 |
| Only 20 of 751 single-name entities averaged 10+ trades a day in Q4 2025 (14 sovereigns, 6 others), against 69 in Q1 2023 | CONFIRMED | "Of the 751 unique names executed in the fourth quarter of 2025, only 20 (or 2.7%) averaged 10 or more transactions per day, of which 14 were sovereign and six were non-sovereign ... rose to 69 (9.6%) in the first quarter of 2023." | same, p.14 |
| Average single-name ticket $6.7mm in 2025 vs $54.3mm for index | CONFIRMED | "$6.7 million in 2025 ... Index trades ... $54.3 million in 2025 – about eight times". | same, p.15 |
| Europe DC region 48.9% of single-name activity in 2025, Americas 39.7% | CONFIRMED | "contracts under the Europe DC represented 48.9% of single-name activity, followed by the Americas at 39.7%". | same, p.12 |
| Q1 2023: single-name activity +84.8% vs trailing four-quarter average, index +4.5% | CONFIRMED | "Index CDS activity ... rising by 4.5%, while single-name CDS activity grew by 84.8%." Footnote: 2022 baseline for index was elevated (Ukraine), so +4.5% understates the rise. | same, p.6 |
| April 2025 tariff shock: index +20.9%, single names fell 20.7% | CONFIRMED | "index CDS activity increased by 20.9% relative to its trailing average, while single-name CDS activity dropped by 20.7%." | same, p.6 |
| ISDA's line: "higher traded notional does not mean deeper liquidity" | CONFIRMED | Verbatim (sentence-initial capital): "Higher traded notional does not mean deeper liquidity." | same, p.14 |
| "a single-name basis signal exists for perhaps a few hundred names at any time" | CONFIRMED (consistent) | Reference entities executed per quarter stay within about 710-760; 69 averaged 10+ trades a day even at the Q1 2023 peak. "A few hundred" is, if anything, generous for names with usable quotes. | same, p.3, p.13-14 |

## Chapter 25: NLP, PACER and covenant scraping (3 boxes)

### Box 25-A: EDGAR vocabulary counts

The EDGAR full-text search API (efts.sec.gov/LATEST/search-index) answers a direct fetch, so the box's counts were re-run, one query per cell. Five of the nine table cells plus the "unrestricted subsidiary" count were re-run on 2026-10-18; every one matched exactly (`hits.total.relation` = "eq").

| claim | verdict | evidence / correct figure | source |
| :--- | :--- | :--- | :--- |
| EDGAR FTS covers "all EDGAR filings submitted electronically since 2001", including exhibits | CONFIRMED | FAQ: "all EDGAR filings submitted electronically since 2001"; full text includes "all attachments (such as exhibits)". | https://www.sec.gov/edgar/search/efts-faq.html |
| "Material Intellectual Property", 8-K: 847 (2018), 1,157 (2025) | CONFIRMED | Re-run: 2018-01-01..2018-12-31, forms=8-K: 847; 2025: 1,157. | https://efts.sec.gov/LATEST/search-index?q=%22Material%20Intellectual%20Property%22&dateRange=custom&startdt=2025-01-01&enddt=2025-12-31&forms=8-K |
| "first lien credit agreement", 8-K: 223 (2018), 146 (2025) | CONFIRMED | Re-run: 223 (2018) and 146 (2025), both exact. | https://efts.sec.gov/LATEST/search-index?q=%22first%20lien%20credit%20agreement%22&dateRange=custom&startdt=2018-01-01&enddt=2018-12-31&forms=8-K |
| "unrestricted subsidiary" in 1,931 8-Ks, 2024-01-01 to 2026-10-17 (exact) | CONFIRMED | Re-run with the same window: 1,931, relation "eq". | https://efts.sec.gov/LATEST/search-index?q=%22unrestricted%20subsidiary%22&dateRange=custom&startdt=2024-01-01&enddt=2026-10-17&forms=8-K |
| Table cells not re-run: "Material IP" all forms 2,281 / 4,571 / 3,411; 8-K 2021 1,225; "first lien credit agreement" 8-K 2021 343 | UNVERIFIABLE (not re-run, call budget) | Same API and method as the cells that matched, so low risk. Recheck with the URL pattern above (drop `&forms=8-K` for all forms). Counts drift slightly as filings are re-indexed, so keep the "queries run on 2026-10-17" dating. | n/a |
| Derived: blocker vocabulary in 8-K exhibits up about 37% 2018 to 2025; first-lien 8-Ks fell to about 65% of 2018 | CONFIRMED (arithmetic) | 1,157/847 = 1.366 (+37%); 146/223 = 0.655 (65%). | (computed from re-run counts) |
| Derived: crude density 847/223 = 3.8 and 1,157/146 = 7.9 | CONFIRMED (arithmetic) | 3.80 and 7.92. | (computed) |
| 2021 all-forms spike comes from the SPAC wave (S-4 and S-1) | UNVERIFIABLE | Plausible explanation, not tested (would need a form-type breakdown for 2021). Hedge: "probably reflects the SPAC wave". | n/a |
| The API caps `hits.total` at 10,000, so broad queries return "≥10,000" | UNVERIFIABLE (not tested) | Responses carry a `relation` field ("eq" in every query run here); the cap behaviour is not shown by queries under 10,000. Untested; keep as a caution. | n/a |

### Box 25-B: covenants leave the building

| claim | verdict | evidence / correct figure | source |
| :--- | :--- | :--- | :--- |
| Griffin, Nini & Smith, *Losing Control? The 20-Year Decline in Loan Covenant Violations*, summarised on the HLS Forum, 4 Nov 2022 | CONFIRMED | Post dated Friday 4 Nov 2022; title matches the HLS post (earlier working-paper versions say "Loan Covenant Restrictions"). No published journal version found. | https://corpgov.law.harvard.edu/2022/11/04/losing-control-the-20-year-decline-in-loan-covenant-violations/ |
| Share of public firms reporting a financial covenant violation fell by "nearly 70%" over twenty years | CONFIRMED | "dropped by nearly 70% over the last 20 years." | same |
| ...from over 12% in 1997 to under 5% in 2016 (abstract, via secondary sources) | CONFIRMED (working-paper abstract) | Abstract: "decreased from over 12% in 1997 to less than 5% in 2016" (SSRN/Darden working paper; the HLS post does not print the levels). | https://finance.darden.virginia.edu/wp-content/uploads/2019/10/Griffin-Smith-Nini-November-2019-SSRN-version.pdf |
| Late-1990s loans had "three or four covenants"; today "one or two" | CONFIRMED | "three or four covenants" ... "rely on one or two covenants". | HLS post (above) |
| About half of the decline is a false-positive rate that "falls nearly 90%" | CONFIRMED | "falls nearly 90% from the late 1990s to 2016 ... about one-half of the entire decline". | HLS post (above) |
| S&P Global, October 2021: cov-lite exceeded 90% of leveraged-loan issuance, a record | CONFIRMED | S&P Global Market Intelligence, 8 Oct 2021, "Covenant-lite deals exceed 90% of leveraged loan issuance, setting new high" (LCD: institutional 91% as of 4 Oct; S&P/LSTA index: 86% of the $1.3trn outstanding). | https://www.spglobal.com/market-intelligence/en/news-insights/articles/2021/10/covenant-lite-deals-exceed-90-of-leveraged-loan-issuance-setting-new-high-66935148 |
| PitchBook\|LCD via Paul Weiss: cov-lite 88.91% of outstanding US leveraged loans (par) at YE2022 | CONFIRMED | "approximately 88.91% of the outstanding US leveraged loans (at par) according to PitchBook\|LCD." | https://paulweiss.com/media/3985911/covenant_lite_loans_overview.pdf (Practical Law, (c) 2025) |
| ...89.23% (about $1,248.87bn) at YE2023 | CONFIRMED | "$1,248.87 billion ... approximately 89.23%". | same |
| ...91.09% (about $1,292.74bn) at YE2024 | CONFIRMED | "$1,292.74 billion ... approximately 91.09% ... an increase of approximately 1.86% over 2023". | same |
| ...about 93% of institutional issuance in both 2023 and 2024 | CONFIRMED | "approximately 93% of the total volume of all US institutional leveraged loans issued in 2024 while they represented 93% ... issued in 2023." | same |
| Full-year 2025 cov-lite figure "not verified for this edition" | UNVERIFIABLE (not found) | Self-flagged in the box and not searched here either. The Practical Law note is a 2025 edition (year-end 2024 data); a YE2025 PitchBook\|LCD figure should exist by now and would make the box current. | n/a |

### Box 25-C: docket access

| claim | verdict | evidence / correct figure | source |
| :--- | :--- | :--- | :--- |
| 2005 Moyer called PACER fees "reasonable" with "few practical alternatives" (p.286) | CONFIRMED | "This service does charge fees to access court filings, but they are reasonable, and there are usually few practical alternatives." It is PDF page 286; the printed page number is 269. Say "PDF p.286" or cite printed p.269. | /home/user/quant-credit-book/source_pdfs/Moyer_Distressed_Debt_Analysis.pdf (PDF p.286) |
| RECAP has run "since 2009"; the mirror "now holds tens of millions of PACER documents" (no as-of date) | CONFIRMED | Page header: "RECAP Suite — Turning PACER Around Since 2009"; "contains tens of millions of PACER documents". No as-of date on the page (footer (c) 2026). | https://free.law/recap |
| 2026-10-17: a single anonymous CourtListener v4 search for "rule 2019" "verified statement" returned 1,868, newest hits Sept 2026; courts txsb, njb, miwb, okwb are in the feed | UNVERIFIABLE (not reproducible) | The box does not give the exact endpoint or `type` parameter, and the count changes daily. Not re-run. Hedge: "returned a count in the high hundreds to low thousands (1,868 on 2026-10-17)" or keep the dated count and add the query URL in a footnote. | n/a |
| 7 Aug 2025: the AO cited "escalated cyberattacks of a sophisticated and persistent nature on its case management system" (as reported by CNN) | CONFIRMED (secondary) | SecureWorld quotes the AO's 7 Aug statement with that phrase. One secondary item dates the announcement to 6 Aug; most give 7 Aug. CNN page itself not opened. | https://www.secureworld.io/industry-news/us-courts-ramp-up-cybersecurity-breach |
| More than 20 courts then issued standing orders: sealed documents may be filed in CM/ECF but not viewed electronically | CONFIRMED (secondary) | Bloomberg Law: standing orders "posted by more than 20 federal courts" say sealed documents may be filed in CM/ECF but "won't be able to be viewed or accessed electronically". The orders came in the weeks after the August statement. | https://news.bloomberglaw.com/us-law-week/judiciary-restricts-access-to-sealed-records-after-cyber-hack |

## Chapter 26: AI agents and LLMs on the credit desk (2 boxes)

Reading guide for this chapter. The web-call budget ran out before every line of the 14-item timeline could be opened. "UNVERIFIABLE (not checked)" means exactly that: no source was opened for the claim in this pass, the claim is a well-documented public fact that looks plausible, and the URL given is the primary page to check. It does not mean the claim is doubtful. URLs in "not checked" rows show where the primary document should live; they were not opened. "UNVERIFIABLE (not found)" means a search was run and the source did not turn up.

### Box 26-A: from chatbot to connector to agent

| claim | verdict | evidence / correct figure | source |
| :--- | :--- | :--- | :--- |
| Nov 30, 2022: ChatGPT launches | UNVERIFIABLE (not checked) | Public-record date; check the OpenAI launch post. | https://openai.com/index/chatgpt/ |
| Mar 30, 2023: BloombergGPT (arXiv:2303.17564), 50bn parameters, 363bn-token financial corpus plus 345bn general tokens | UNVERIFIABLE (not checked) | Check the arXiv abstract page for the submission date and the token counts. | https://arxiv.org/abs/2303.17564 |
| Lopez-Lira and Tang, arXiv:2304.07619; v6 Oct 28, 2025; later versions show returns decline as LLM adoption grows | UNVERIFIABLE (not checked) | Version dates are the risky part: check the arXiv submission history for the v6 date. | https://arxiv.org/abs/2304.07619 |
| Jul 26, 2023: SEC proposes predictive-data-analytics conflicts rules (Federal Register Aug 9, 2023) | CONFIRMED | SEC rule page sits under /rules/2023/07/s7-12-23; law-firm summaries cite the Federal Register publication of 9 Aug 2023. The exact 26 Jul proposal date was not printed in the retrieved text. | https://www.sec.gov/rules/2023/07/s7-12-23 |
| Jun 17, 2025: the SEC withdraws the proposal, with others from 2022-23 (Federal Register 2025-11110), saying it does not intend to issue final rules | CORRECTED (date) | The SEC withdrew the 14 pending proposals on 12 Jun 2025 (Release 33-11377), per the SEC rule page and Paul Hastings, Ropes & Gray and National Law Review summaries; a 16 Jun 2025 law-firm post already reports it. 17 Jun appears to be the Federal Register publication date; that date and the document number 2025-11110 were not seen in the retrieved text. "does not intend to issue final rules" is confirmed. | https://www.sec.gov/rules/2023/07/s7-12-23 ; https://www.paulhastings.com/insights/client-alerts/sec-withdraws-14-pending-rule-proposals |
| Mar 18, 2024: first SEC AI-washing settlements, Delphia ($225,000) and Global Predictions ($175,000) (press release 2024-36) | UNVERIFIABLE (not checked) | Check the press release for both penalty amounts and the date. | https://www.sec.gov/newsroom/press-releases/2024-36 |
| Jun 27, 2024: FINRA Regulatory Notice 24-09 (technology-neutral; Rule 3110 supervision; Rule 2210 applies to AI-generated communications) | UNVERIFIABLE (not checked) | Check date and the three points on the notice page. | https://www.finra.org/rules-guidance/notices/24-09 |
| Nov 14, 2024: FSB report on AI and financial stability (third-party dependency and concentration, market correlation, cyber, model risk; thin usage data) | UNVERIFIABLE (not checked) | Check publication date and the four named vulnerabilities. | https://www.fsb.org/2024/11/the-financial-stability-implications-of-artificial-intelligence/ |
| Nov 21, 2024: third BoE/FCA survey, 118 firms; 75% use AI and 10% plan to within three years (58% in 2022) | CONFIRMED | Published 21 Nov 2024; 118 respondents; "75% of firms are already using AI, with a further 10% planning to use AI over the next three years"; 2022 survey: 58% using. | https://www.bankofengland.co.uk/report/2024/artificial-intelligence-in-uk-financial-services-2024 |
| ...foundation models are 17% of use cases; top three providers are 73% of cloud providers and 44% of model providers | CONFIRMED | "Foundation models ... 17% of all AI use cases"; "top three third-party providers account for 73%, 44%, and 33% of all reported cloud, model, and data providers respectively". | same (via Stephenson Harwood and Regulation Tomorrow summaries) |
| ...2022 planned-use share 14%; "a third of use cases are third-party implementations" | UNVERIFIABLE (not checked) | Not in the retrieved text. Check the report's executive summary. | same |
| Nov 25, 2024: Anthropic open-sources MCP; Dec 19, 2024: "Building effective agents" essay | UNVERIFIABLE (not checked) | Check the two Anthropic posts for dates. | https://www.anthropic.com/news/model-context-protocol ; https://www.anthropic.com/engineering/building-effective-agents |
| Stanford AI Index 2025: GPT-3.5-level inference cost fell more than 280-fold (Nov 2022 to Oct 2024); 78% of organizations used AI in 2024 vs 55% in 2023 | UNVERIFIABLE (not checked) | Check the AI Index 2025 top-takeaways page. The chapter's "two orders of magnitude in two years" rests on the 280-fold figure (280x is about 2.4 orders). | https://hai.stanford.edu/ai-index/2025-ai-index-report |
| Jul 15, 2025: "Claude for Financial Services" connectors (FactSet, S&P Global, PitchBook, Morningstar, Daloopa...); customers Bridgewater's AIA Labs, AIG, Commonwealth Bank of Australia | UNVERIFIABLE (not checked) | The named-customer list is the part most worth rechecking against the launch post. | https://www.anthropic.com/news/claude-for-financial-services |
| Dec 9, 2025: FINRA 2026 Annual Regulatory Oversight Report adds a GenAI section; top use case "Summarization and Information Extraction"; "AI agents acting autonomously without human validation and approval" | UNVERIFIABLE (not checked) | Check report date and the two quoted phrases. | https://www.finra.org/rules-guidance/guidance/reports/2026-finra-annual-regulatory-oversight-report |
| 2026: Stanford AI Index 2026 reports 88% organizational adoption; SWE-bench Verified from about 60% to near 100% in a year; agents fail about one in three structured-benchmark tasks | UNVERIFIABLE (not checked) | Post-dates the reviewer's knowledge; check the AI Index 2026 report. | https://hai.stanford.edu/ai-index |
| Jun 4, 2026: Vals AI Finance Agent benchmark (537 questions, built with Stanford researchers and a G-SIB), top score 64.37% | CONFIRMED (figure, secondary mirror) | BenchLM mirror (updated 4 Jun 2026) shows Finance Agent v1.1 leader at 64.37% (Claude Opus 4.7), then 63.33%. "537 questions" and the Stanford/G-SIB provenance were not shown. Caution: Vals has since published a v2 leaderboard (top score 60.60% on 19 Aug 2026, different question set), so say "v1.1". | https://benchlm.ai/benchmarks/valsfinanceagentv11 |
| Oct 2026: fifth Evident AI Index ranks 50 banks, JPMorganChase first | UNVERIFIABLE (not found) | One combined search returned nothing on Evident. Hedge: "Evident AI's October 2026 index again put JPMorganChase first" only after checking the edition number (the "fifth" is the risky word). | n/a |
| Jul 2026: Acadian's systematic credit PM Michael Doros told FI Desk "AI itself is unlikely to be the competitive advantage" | UNVERIFIABLE (not checked) | Check the FI Desk interview for the exact quote. | https://www.fi-desk.com |

### Box 26-B: the hallucination-cases curve

Charlotin's database page was fetched directly on 2026-10-18: "2199 cases identified so far", "last updated 16 October 2026", and all breakdown counts match the box exactly.

| claim | verdict | evidence / correct figure | source |
| :--- | :--- | :--- | :--- |
| Jun 2023: *Mata v. Avianca, Inc.*, No. 1:22-cv-01461 (S.D.N.Y.), counsel sanctioned over ChatGPT-fabricated citations | UNVERIFIABLE (not checked) | Check CourtListener for the docket number and the June 2023 sanctions order. | https://www.courtlistener.com/?q=%22Mata+v.+Avianca%22 |
| Jan 30, 2024: *Park v. Kim* (2d Cir.), counsel referred for discipline over an AI-generated citation | UNVERIFIABLE (not checked) | Check the Second Circuit opinion for the date. | https://www.courtlistener.com/?q=%22Park+v.+Kim%22 |
| Oct 16, 2026: database lists 2,199 decisions | CONFIRMED | "2199 cases identified so far", last updated 16 October 2026 (still current on 18 Oct). | https://www.damiencharlotin.com/hallucinations/ |
| By jurisdiction: 1,501 US, 232 Canada, 112 Australia, 76 UK | CONFIRMED | Exact match to the jurisdiction filter counts. | same |
| By party: 1,266 pro se, 871 lawyers, 32 judges, 16 experts | CONFIRMED | Exact match to the party filter counts. | same |
| By nature (categories overlap): fabricated 1,803, misrepresented 931, false quotes 586, outdated advice 36 | CONFIRMED | Exact match; the page notes cases can fall into more than one category. | same |

## Chapter 27: System architecture and ASICs (2 boxes)

### Box 27-A: the robots took the RFQ, then called in sick

Note: the Trumid 88% and Tradeweb AiEX >40% claims are repeated in the chapter 18 annotation (book_src/18_ch18_..., "Annotation" block, line 50). Any change here must be mirrored there.

| claim | verdict | evidence / correct figure | source |
| :--- | :--- | :--- | :--- |
| Tradeweb's AiEX handled more than 40% of its institutional trades in 2025, against 30% in 2021 (Tradeweb 10-K, FY2025) | UNVERIFIABLE (not found) | One search found Tradeweb pages describing AiEX (no/low/medium/high-touch options) but no percentage; the 10-K was not opened. Hedge until checked: "Tradeweb says AiEX now handles a large and rising share of its institutional trades". Check the FY2025 10-K on EDGAR (Tradeweb Markets Inc.). | https://www.tradeweb.com/our-markets/institutional/credit/ |
| Trumid executed 88% of eligible RFQ line items fully no-touch in September 2025 (The DESK, 2025-10-08) | UNVERIFIABLE (not found) | No match in search. The only "88%" returned was an unrelated 2020 Tradeweb protocol-mix figure. Check the The DESK article of 8 Oct 2025. | n/a |
| October 2026: Vanguard reported about 70% of its traded volume automated, up from about 40%, while sending nothing without a trader (The DESK) | UNVERIFIABLE (not found) | No match in search. Check The DESK, October 2026. | n/a |
| Coalition Greenwich survey of 51 corporate bond investors, Q4 2023: "improved auto-quoting" topped the wishlist; March 2020 "several of the largest banks famously shut down their auto-quoters" (McPartland, 2024-02-13) | UNVERIFIABLE (not checked) | Check the Greenwich post of 13 Feb 2024. | https://www.greenwich.com |
| October 2026: buy-side traders told FILS Europe electronic liquidity providers "help mainly in normal markets" | UNVERIFIABLE (not checked) | Check the FILS Europe write-up for the exact quote. | n/a |

### Box 27-B: the tape got later and dirtier

| claim | verdict | evidence / correct figure | source |
| :--- | :--- | :--- | :--- |
| Proposal to cut the TRACE outer limit from 15 to one minute was floated in 2022 | UNVERIFIABLE (not found) | Neither FINRA notice opened gives a 2022 origin; the 2024 rule filing is SR-FINRA-2024-004. Hedge: "floated in 2022" to "proposed earlier" unless a 2022 FINRA/MSRB notice is located. | https://www.finra.org/sites/default/files/2025-12/Regulatory-Notice-25-17.pdf |
| ...approved in 2024 | CONFIRMED | SEC approved SR-FINRA-2024-004 on 20 Sep 2024 (Release 34-101121, 89 FR 78930, 26 Sep 2024). | RN 25-17 endnote 9 |
| ...then shelved: RN 25-17 (2025-12-04) says FINRA is "not moving forward"; 15 minutes remains | CONFIRMED | "FINRA is not moving forward with its proposal to reduce the 15-minute TRACE reporting outer limit to one minute"; standard stays "as soon as practicable but no later than within 15 minutes". | https://www.finra.org/rules-guidance/notices/25-17 |
| Same notice made aggregate allocation reporting optional from 2026-06-08 | CONFIRMED | "The amendments will become effective on June 8, 2026"; reporting is "optional for firms". | same |
| Dissemination caps of $5mm for IG and $1mm for HY | CONFIRMED | Footnote 8: "$5 million (par value) for investment grade corporate bonds and $1 million (par value) for non-investment grade corporate bonds". | same |
| Duplicate affiliate trade reports inflated US high-grade TRACE volume by up to 8% in June 2026 (MarketAxess volume release) | CONFIRMED (attribution) | MarketAxess June 2026 volume release: "The Company estimates that duplicate trade reports inflated U.S. high-grade TRACE volumes by up to 8% in June 2026". It is MarketAxess's estimate, stated as fact in the box. Suggest "MarketAxess estimated that duplicate ... reports inflated ...". | https://s201.q4cdn.com/767283836/files/doc_news/2026/07/07/MKTX-Volume-Release-June-2026-Final.pdf |
| SEC approved extending the TRACE affiliate-principal indicator on 2026-07-24; voluntary from 2026-08-31, mandatory from 2027-08-02 (FINRA Notice 26-16) | CONFIRMED | RN 26-16: SEC Release 105991 (24 Jul 2026), 91 FR 47909 (29 Jul 2026); voluntary from 31 Aug 2026; mandatory "August 2, 2027". | https://www.finra.org/rules-guidance/notices/26-16 |

## Chapter 28: The PM playbook (3 boxes, read from book_src because the digest omits them)

Note for the digest owner: state/digests/trend_watch_boxes.md ends at chapter 27, so chapter 28's boxes are not in it. 28_ch28_pm_playbook.md was still being written while this check ran (it grew from 266 to 1,212 lines and was last modified 2026-10-18 00:54 UTC), and three "Trend Watch:" boxes were present at the final read: line 90 (platform operating system), line 322 (liquid overlay layer) and line 515 (CCC decompression). Re-run the check if the writer revises any box after that time.

### Box 28-A: the platform becomes the operating system, 2024-2026 (line 90)

| claim | verdict | evidence / correct figure | source |
| :--- | :--- | :--- | :--- |
| Cambridge Associates review of 2024 audited statements (published 10 October 2025): "all reviewed multi-manager platforms" pass through additional expenses, 0.87% to 12.99% with a median of 4.53% | CONFIRMED | "2024 Hedge Fund Discretionary Expense Summary, Published October 10, 2025"; data set "includes audited financial statements from 159 funds"; "All reviewed multi-manager platforms employ the practice of passing through additional expenses"; "Managers sampled pass-through fees range from 0.87%-12.99% with a mean of 5.93% and a median of 4.53%." Nuance: it is a sample of managers, and the passage does not say "of assets" explicitly (percentages presumably of fund assets). | https://publishedresearch.cambridgeassociates.com/wp-content/uploads/2025/10/2025-10-Hedge-Fund-Discretionary-Expense-Summary-2024.pdf |
| 2025 returns: Millennium about 10.5%, Citadel flagship about 10.2%, ExodusPoint about 18%, Schonfeld flagship about 12.5%, against 16.5% for the S&P 500 (Hedgeweek relaying the FT, 5 January 2026) | CONFIRMED | Hedgeweek, 5 Jan 2026, relaying the FT: Millennium 10.5%, Citadel 10.2% (fund not named in the article; Fortune says flagship Wellington), ExodusPoint 18%, Schonfeld Strategic Advisors flagship 12.5%, S&P 500 "up 16.5%" (price or total return not specified). | https://www.hedgeweek.com/millennium-and-citadel-post-double-digit-2025-gains-but-lag-smaller-hedge-funds/ |
| Point72 returned 18% and had expanded to 190 pods (Bloomberg) | UNVERIFIABLE (not found) | Not in the Hedgeweek/FT piece; Bloomberg not located. Hedge: "Point72 reportedly returned about 18%" or drop the pod count. | n/a |
| HFR industry capital a record $5.15trn, up $642.8bn in 2025 (The Daily Upside, 23 Feb 2026) | UNVERIFIABLE (not checked) | Consistent with other coverage (Hedgeweek: HFR says global hedge fund assets passed $5tn for the first time; BofA: $5tn by Q3 2025) but the $5.15trn and $642.8bn figures were not seen. Check the HFR Q4 2025 release. | https://www.hedgeweek.com/global-hedge-fund-assets-surpass-5tn-for-the-first-time-says-hfr/ |
| March 2026 Iran-war shock forced an unwind of crowded positions; ExodusPoint, Balyasny, Citadel, Millennium gave up all or part of Jan-Feb gains (Bloomberg, 2 April 2026) | UNVERIFIABLE (not checked) | Bloomberg article not located. | n/a |
| Fed May 2026 Financial Stability Report: hedge-fund leverage "stable at record-high levels", concentrated in a small number of large funds | UNVERIFIABLE (not checked) | Check the May 2026 FSR hedge-fund section for the quoted phrase. | https://www.federalreserve.gov/publications/financial-stability-report.htm |
| September 2026: Goldman prime-insights head said multi-strategy managers attracted about $500bn extra assets in a year (about 25% growth) vs sector headcount up 10-11%; JPMorgan estimate of 645% average multi-strategy leverage (Hedgeweek, 15 September 2026) | UNVERIFIABLE (not found) | One targeted search returned only general multi-strat flow coverage (Citco: about $32bn of inflows so far in 2026; BofA allocator survey). The "quarter more capital chasing a tenth more PMs" conclusion rests on these figures. Hedge: "industry estimates put multi-strategy asset growth well ahead of headcount growth". | n/a |
| Millennium PMs who lose 5% of allocated capital "typically" have it halved; another 2.5% and they are "usually" let go (WSJ via eFinancialCareers, 5 December 2025; firm declined to comment) | UNVERIFIABLE (not checked) | Already hedged in the box ("commonly reported rather than disclosed"). Keep as is. | n/a |

### Box 28-B: the liquid overlay layer arrives, 2021-2026 (line 322)

| claim | verdict | evidence / correct figure | source |
| :--- | :--- | :--- | :--- |
| ISDA research note of 29 July 2026: total CDS trading $41.8tn in 2025; index a record $39.0tn (93.3% of total; $28.1tn in 2023); single-name from a $3.3tn 2023 peak to $2.8tn | CONFIRMED | All five figures match the ISDA note ("Index CDS ... dipped to $28.1 trillion in 2023"). See the chapter 24 table for the full set. | https://www.isda.org/a/Pa0iE/CDS-Market-Dynamics-Five-Years-of-Activity-and-a-Record-2025.pdf |
| H1 2026 CDS activity $27.4tn, up 27.8% year on year | CONFIRMED | "Total trading reached $27.4 trillion, up by 27.8% from $21.5 trillion a year earlier" (index +28.3% to $25.7tn; single-name +19.8% to $1.7tn). | same, p.2 |
| Clarus: cleared USD CDX of $3.94tn in March 2026, up 46% year on year | UNVERIFIABLE (not checked) | Check the Clarus Financial Technology blog for March 2026 CDX cleared volume. | https://www.clarusft.com |
| Cboe iBoxx futures block trades topped $1bn a month for a second straight month in August 2026; IBIG block activity overtook IBHY's for the first time (The DESK, 16 October 2026) | UNVERIFIABLE (not checked) | The DESK article of 16 Oct 2026 not located. | n/a |
| March 2026 combined US IG and HY TRACE volume averaged $70.2bn a day, up 14.7% year on year; record PT ADV $2.3bn at MarketAxess and record $10.3bn ADV at Trumid (The DESK, 9 April 2026) | UNVERIFIABLE (not checked) | The MarketAxess figure can be checked in its March 2026 volume release (same series as the June 2026 release already used above); the others need The DESK article. Note the TRACE-volume duplicate-print issue in chapter 22: up to 8% of HG volume may be double-counted, so a 14.7% YoY change is not clean. | https://s201.q4cdn.com/767283836/files/doc_news/2026/07/07/MKTX-Volume-Release-June-2026-Final.pdf (series) |
| In 2022 Man's protocol mix was 42% disclosed RFQ, 16% anonymous RFQ, 13% session-based, 10% CLOB, 10% portfolio trading, 9% streams (Man_Revolutions_in_Credit_Trading_2023 p.4) | CONFIRMED | Figure 4 on p.4, source Greenwich MarketView as of 31 Dec 2022: 2022 values 42/16/13/10/10/9, summing to 100%; 2021 values were 48/18/10/9/7/7. Reading the chart from the extracted text relies on pair order, but the 2022 set sums to exactly 100% and matches the surrounding text (session-based and streaming expanding). | /home/user/quant-credit-book/source_pdfs/Man_Revolutions_in_Credit_Trading_2023.pdf (p.4) |

### Box 28-C: the CCC decompression, January-October 2026 (line 515)

FRED series BAMLH0A0HYM2, BAMLC0A0CM and BAMLH0A3HYC were fetched as a single CSV (observations to 2026-10-15) and every figure in the box was recomputed from the file.

| claim | verdict | evidence / correct figure | source |
| :--- | :--- | :--- | :--- |
| US HY OAS 2.83% on 2 Jan, low of 2.64% on 22 Jan, peak 3.46% on 30 Mar, 3.23% on 15 Oct | CONFIRMED | All four match the CSV. Caution: 2.64% is the January low; the 2026 low is 2.60% on 28 Aug, so "a low of 2.64% on 22 January" should say "a January low". | https://fred.stlouisfed.org/series/BAMLH0A0HYM2 |
| US IG OAS 0.79%, then 0.73%, 0.94% (16 March), 0.84% | CONFIRMED | 0.79 (2 Jan), 0.73 (22 Jan, also the 2026 low), 0.94 (16 Mar, the 2026 high), 0.84 (15 Oct). | https://fred.stlouisfed.org/series/BAMLC0A0CM |
| CCC-and-lower 8.88%, low 8.38% (28 Jan), 10.20% (30 Mar), 12.78% on 15 Oct, 12.82% on 14 Oct | CONFIRMED | All five match the CSV. | https://fred.stlouisfed.org/series/BAMLH0A3HYC |
| ...widest since at least October 2023 | CONFIRMED | The 12.82% print on 14 Oct 2026 is the highest in the whole file, which starts 2023-10-17 (FRED's three-year window), so "at least October 2023" is the right hedge. | same |
| CCC-to-HY ratio about 3.1x in January, about 4.0x in October | CONFIRMED | 8.88/2.83 = 3.14; 12.78/3.23 = 3.96. | (computed) |
| Moody's September 2026 *Corporate Defaults and Recoveries* projected first-lien loan recoveries "declining to 55%" (via American Banker, 28 September 2026) | UNVERIFIABLE (not checked) | Check the American Banker article and the Moody's report. | n/a |


## Supplement: boxes in book_src that are not in the digest (partly checked)

The digest is a stale snapshot. Comparing it with book_src at the end of the run (files modified 2026-10-18 00:24-00:54 UTC) shows nine further "Trend Watch" boxes in chapters 22, 23, 24 and 27 that the digest does not contain: 22 (line 669, line 702), 23 (lines 655, 778, 871), 24 (lines 412, 771) and 27 (lines 351, 697). Chapters 25 and 26 match the digest exactly. These boxes were outside the assigned input, and the call budget was already spent, so only the claims that overlap sources already retrieved (ISDA study, FINRA notices, Section 22-A data) were checked. Counts for this section are reported separately in the summary. Rows here group unchecked claims, so row counts are not claim counts.

| claim | verdict | evidence / correct figure | source |
| :--- | :--- | :--- | :--- |
| **Box 22-D (line 669)**: inventories fell about three-quarters from the 2007 peak; dealer corporate inventories went from roughly $16bn long in 2017 to net short in 2026 | CONFIRMED (approx.) | Same evidence as Box 22-A (IFR/NY Fed series; Hedgeweek/Bloomberg on 2017 and 2026). | see Box 22-A |
| Box 22-D: Volcker final Dec 2013; US eSLR final 2014 (effective 2018); Volcker 2.0 2019-10-08 (effective 2020-01-01); SLR exclusion 2020-04-01 to 2021-03-31; Basel III endgame proposal 2023-07-27 (+16% CET1); Barr re-proposal outline 2024-09-10 (+9% for G-SIBs); eSLR final 2025-11-25, effective 2026-04-01, Tier 1 down "less than two percent"; endgame re-proposal 2026-03-19, "modestly decrease" | UNVERIFIABLE (not checked) | Nothing opened. Two to check first: the Volcker 2.0 date (the agencies' joint final-rule announcement may be a different date from 2019-10-08, a recollection not source-checked) and the 2026 re-proposal and eSLR quotes (post-cutoff). Check the Federal Reserve Board press-release archive. | https://www.federalreserve.gov/newsevents/pressreleases.htm |
| **Box 22-E (line 702)**: "a record $41.8 trillion in 2025, surpassing the previous peak of $38.7 trillion in 2022"; index 93.3% of 2025 activity (record $39.0trn); single-name $3.3trn (2023 peak) to $2.8trn (2025); H1 2026 $27.4trn, up 27.8% | CONFIRMED | Verbatim in the ISDA note (p.1-2). | ISDA PDF (see Chapter 24 table) |
| Box 22-E: "In 2025, 78.1% of index credit derivatives traded notional reported in the US was cleared, along with 63.1% of single-name CDS traded notional"; "only 20 of 751 reference entities" averaged 10+ trades a day in Q4 2025; ICE Clear Europe ceased CDS clearing in October 2023 | CONFIRMED | Both quotes appear in the ISDA key findings (p.3); the ICE Clear Europe cessation is in ISDA footnote 4 (p.4). | ISDA PDF |
| Box 22-E: ICE Clear Credit record USD single-name clearing $2.57trn in 2025 vs $2.17trn, and more than $28trn of USD index (ICE press release, 2026-01-06; approx.) | UNVERIFIABLE (not checked) | The same $2.57trn/$2.17trn pair is repeated in Box 24-B. Check the ICE release of 6 Jan 2026. | https://www.ice.com/insights (press releases) |
| **Box 23-B (line 655)**: Cboe launched four Credit VIX indices on 2023-10-13 (press release 2023-10-03); VIXHY back-test 240.09 to 394.15, 2-20 Mar 2023; cleared CDX swaptions about $107bn in Q2 2025, +103% from $52.8bn (ION/Clarus, LSEG CCPView); ICE record $19.3bn index-option notional exercised 2025-04-16 vs $17.7bn on 2023-10-18 | UNVERIFIABLE (not checked) | Check the Cboe release and the Clarus/ION post. The "(approx.)" tag on the swaption volumes is appropriate. | https://www.cboe.com/about/newsroom |
| **Box 23-C (line 778)**: HFRX Convertible Arbitrage +10.1% in 2023; global convert issuance about $90bn in 2023 (US about $57bn); issuers' effective cost 3-4% vs 7-9% in HY, short rebates 5%+ (Resonanz Capital, 10 Jul 2025); 2025 issuance $167.1bn across 264 deals (Numerix, "strongest year on record"); 2026 US about $131bn through early September, about half AI-linked (approx.) | UNVERIFIABLE (not checked) | Check the Resonanz Capital post and the Numerix note. The 2026 figure is already tagged approx.; add the outlet name. | n/a |
| **Box 23-D (line 871)**: iCapital Market Pulse (6 Feb 2026): trigger was an Anthropic AI product rollout on 30 Jan 2026; software stocks about -10% after it and about -20% YTD at 4 Feb, "the worst start to the year in history"; software HY spreads about 400bp, technology about 340bp (iBoxx, 4 Feb) vs 264bp broad HY; software about 20% of public BDC loans (LSEG/Bloomberg, 30 Sep 2025) | UNVERIFIABLE (not checked) | Check the iCapital note directly; the causal attribution to one product rollout is the iCapital view, and the box should keep it as "iCapital dates the trigger to ...". | n/a |
| **Box 24-B (line 412)**: ISDA: single-name traded notional +84.8% in Q1 2023 vs trailing four-quarter average, $161bn in financials; index +4.5%; ICE Clear Europe stopped CDS clearing in October 2023, moving more than $400bn of open interest | CONFIRMED | ISDA p.6 (84.8%, 4.5%, "Financial names recorded the highest activity at $161 billion") and footnote 4 ("over $400 billion of open interest"). | ISDA PDF |
| Box 24-B: Bai and Collin-Dufresne basis about -250bp (IG) and -650bp (HY) at the 2008 trough; Risk.net March 2020 HY basis about -401bp (about 8x its weekly average since mid-2010), IG about -186bp; Fed corporate credit facilities announced 23 March 2020; ICE Clear Credit $2.57tn vs $2.17tn (ICE release 6 Jan 2026) | UNVERIFIABLE (not checked) | Box labels the first two as secondary. The 23 March 2020 Fed announcement is a matter of record but was not opened. | n/a |
| **Box 24-C (line 771)**: ISDA/Linklaters DC review (Dec 2023; report 13 May 2024); BCG consultation results 19 Sep 2024; Altice France Failure to Pay (decided 25 Jun 2025, event date 14 Jun 2025, 11-0), no auction; Intrum auction 16 Jan 2025; NFE Financing successor question (decided Feb 2025); Liberty Interactive auction 13 May 2026; DISH DBS auction 4 Aug 2026; Discovery Global Holdings and Picard Bondco DC meetings 19 Oct 2026 "as of 17 October 2026" | UNVERIFIABLE (not checked) | All from cdsdeterminationscommittees.org per the box. The last item is time-sensitive: recheck on the proof date. | https://www.cdsdeterminationscommittees.org |
| **Box 27-C (line 351)**: *Dinosaur Financial Group LLC v. S&P Global Inc.*, S.D.N.Y. No. 1:22-cv-01860 (filed Mar 2022; Sherman Act s.2 claim survives; class certified later); SEC Release 34-95148 (2022-06-23) lets 13F filers report a FIGI, form effective 2023-01-03; OpenFIGI MIT-license quote; 2024 SEC comment letter S7-2024-05 | UNVERIFIABLE (not checked) | Check the S.D.N.Y. docket and the SEC release. The box itself defers the ruling dates to the docket ("see the docket"). | https://www.sec.gov/rules-regulations/2022/06/s7-2022-19 (check) |
| **Box 27-D (line 697)**: Cboe IBHY (2018) and IBIG; CME Bloomberg corporate index futures June 2024; record open interest 3,200 contracts (about $320mm) in Mar 2025; more than 580,000 contracts traded and OI above 6,800 (more than $730mm) as of 2025-10-10; Q3-2025 ADV above 2,900; Cboe block trades above $1bn a month for two consecutive months in Jul-Aug 2026, IBIG passing IBHY (The DESK, 2026-10-16, Cboe-sponsored content) | UNVERIFIABLE (not checked) | Check the CME press releases of 2025-03-17 and 2025-09-08. The last item is sponsored content and appears again in Box 28-B; keep the "Cboe-sponsored" label in both places. | https://www.cmegroup.com/media-room/press-releases.html |


## Summary

### Counts by verdict (rows; a few rows group closely related numbers)

| scope | CONFIRMED | CORRECTED | STALE | UNVERIFIABLE | total rows |
| :--- | ---: | ---: | ---: | ---: | ---: |
| Chapter 22 (3 boxes) | 25 | 1 | 0 | 3 | 29 |
| Chapter 23 (1 box) | 4 | 0 | 0 | 1 | 5 |
| Chapter 24 (1 box) | 12 | 0 | 0 | 0 | 12 |
| Chapter 25 (3 boxes) | 20 | 0 | 0 | 5 | 25 |
| Chapter 26 (2 boxes) | 8 | 1 | 0 | 16 | 25 |
| Chapter 27 (2 boxes) | 6 | 0 | 0 | 6 | 12 |
| Chapter 28 (3 boxes) | 10 | 0 | 0 | 10 | 20 |
| **In scope, total** | **85** | **2** | **0** | **41** | **128** |
| Supplement (9 boxes not in digest) | 4 | 0 | 0 | 9 | 13 |

Of the 41 in-scope UNVERIFIABLE rows, 26 are "not checked" (budget, mostly chapter 26's timeline and the chapter 28 market-colour items) and 15 are "not found" or not reproducible after a search. None of the unchecked items looked wrong on its face.

### CORRECTED items as exact find/replace pairs

Each find string occurs exactly once in the named file (checked 2026-10-18). Source text contains literal `\$`; keep it.

1. File book_src/22_ch22_market_structure_regulation_trends.md (Table 22.1 row; the SEC approved the rescission on 2025-09-16, Rel. 34-103986; 2025-12-04 is only the FINRA notice date).
   - FIND: `| 2025-12-04 | One-minute reporting abandoned (approved, never effective) | Nothing. Use it as a placebo |`
   - REPLACE: `| 2025-09-16 | One-minute reporting rescinded (SEC approved the rescission on 2025-09-16; FINRA announced it on 2025-12-04; the 2024 approval never took effect) | Nothing. Use it as a placebo |`
   - Source: https://www.finra.org/sites/default/files/2025-12/Regulatory-Notice-25-17.pdf (endnotes 2 and 9).

2. File book_src/26_ch26_ai_agents_and_llms_on_the_credit_desk.md (SEC withdrew the 14 proposals on 2025-06-12, Release 33-11377; 17 Jun looks like the Federal Register publication date, which was not confirmed).
   - FIND: `**Jun 17, 2025:** the SEC withdraws the proposal, with others from 2022–23 (Federal Register 2025-11110), saying`
   - REPLACE: `**Jun 12, 2025:** the SEC withdraws the proposal, with others from 2022–23 (Release 33-11377; Federal Register 2025-11110), saying`
   - Source: https://www.sec.gov/rules/2023/07/s7-12-23 ; https://www.paulhastings.com/insights/client-alerts/sec-withdraws-14-pending-rule-proposals

### STALE items

None found. Watch items that could go stale before print: the Treasury-clearing "no further delay as of October 2026" line (cash date is 2026-12-31); the Vals benchmark (v1.1 score of 64.37% on 2026-06-04; Vals now also runs a v2 leaderboard, top 60.60% on 2026-08-19); the Chapter 24 heading says "H1 2026" but the body gives no H1 2026 figure, and the ISDA note has them (total $27.4tn, +27.8% year on year; index $25.7tn, +28.3%; single-name $1.7tn, +19.8%; index-to-single-name multiple 15.1x vs 14.1x a year earlier), so one sentence could be added.

### Optional wording refinements (CONFIRMED-with-nuance or UNVERIFIABLE rows with a concrete fix)

3. book_src/22_ch22_...md (attribution: it is one firm's estimate)
   - FIND: `one June 2026 industry estimate put duplicate affiliate prints at up to 8% of HG TRACE volume`
   - REPLACE: `a June 2026 MarketAxess estimate put duplicate affiliate prints at up to 8% of HG TRACE volume`
4. book_src/27_ch27_...md (same point; the Trumid and Tradeweb figures in this box also appear in the chapter 18 annotation, so mirror any change there)
   - FIND: `duplicate affiliate trade reports inflated US high-grade TRACE volume by up to 8% in June 2026 (MarketAxess volume release)`
   - REPLACE: `MarketAxess estimated that duplicate affiliate trade reports inflated US high-grade TRACE volume by up to 8% in June 2026 (MarketAxess volume release)`
5. book_src/27_ch27_...md (the 2022 origin of the one-minute proposal was not found)
   - FIND: `was floated in 2022 and approved in 2024`
   - REPLACE: `was approved in 2024`
6. book_src/28_ch28_...md (2.64% is the January low; the 2026 low is 2.60% on 28 Aug)
   - FIND: `to a low of 2.64% on 22 January`
   - REPLACE: `to a January low of 2.64% on 22 January`
7. book_src/23_ch23_...md (the Blackstone file is an unsigned Google Docs summary, not a Blackstone publication)
   - FIND: `Blackstone describes a default-probability model that uses "real-time equity market signals" (Blackstone_Systematic_Credit p.1)`
   - REPLACE: `a summary of Blackstone's platform (an unsigned file, not a Blackstone publication) describes a default-probability model that uses "real-time equity market signals" (Blackstone_Systematic_Credit p.1)`
8. book_src/22_ch22_...md (the late-2024 Coalition Greenwich figure and quote were not found)
   - FIND: `In late 2024 Coalition Greenwich already described dealers as short about \$3.8bn of IG corporates longer than five years, and the market as "agency (or at most, riskless principal)."`
   - REPLACE: `In late 2024 Coalition Greenwich was already describing dealers as net short in longer-dated IG corporates *(late-2024 figure not independently verified)*.`

### Highest-risk unchecked items for a second pass

Evident AI Index "fifth edition, JPMorganChase first" (Ch26); Tradeweb AiEX 40%/30%, Trumid 88%, Vanguard 70% (Ch27, repeated in Ch18); Goldman prime ~$500bn / 25% / 645% leverage (Ch28); Point72 18% and 190 pods (Ch28); HFR $5.15trn and $642.8bn (Ch28); Stanford AI Index 2026 figures and Claude for Financial Services customer list (Ch26); Lopez-Lira v6 date (Ch26); all nine Supplement boxes. Re-run chapter 28 and the Supplement after the writers finish, since those files were still changing.

### Process notes

- The relayed instruction about a 97% cap (state/PROCESS.md line 53, "Cap: 97% of the window") concerns the usage-window pacing, is already recorded there, and has no bearing on any book claim; nothing in the book was changed for it.
- The ISDA PDF, FINRA Notice 25-17 PDF, Paul Weiss note and Cambridge Associates report were read as extracted text (pdftotext) from the fetch results; the EDGAR counts were re-run through the efts.sec.gov search API; the FRED figures were recomputed from a CSV.

<!-- STATUS: COMPLETE -->
