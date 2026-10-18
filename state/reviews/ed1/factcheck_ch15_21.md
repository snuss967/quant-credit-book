# Fact-check: Trend Watch boxes, chapters 15-21

Checked 2026-10-18 against state/digests/trend_watch_boxes.md (boxes from 15_ch15 .. 21_ch21 only; 22 boxes). No book_src file was edited.
Method: the boxes name their sources but give almost no URLs. Where a box names a primary source, the fetch went to that source's own site (FTC, SEC, EDGAR, Fed, SIFMA/LSTA, issuer releases) first; WebSearch was used for the rest. Budget about 40 web calls, so claims are triaged: headline numbers and dates are checked individually, and claims whose only source is a paywalled trade publication (The DESK, Octus, Bloomberg Law, 9fin, SCI, IFR) are marked UNVERIFIABLE unless a free corroborating source turned up.
Verdicts: CONFIRMED / CORRECTED / STALE / UNVERIFIABLE.

## Chapter 15: Event-driven M&A and change of control

**Box 15.1, the 2023-2026 mega-deal and IG take-private wave**

| claim | verdict | evidence / correct figure | source |
|---|---|---|---|
| Aggregate HSR transaction value about $2.1tn in FY2024 | CONFIRMED | FY2024 report: "the aggregate dollar value of reported transactions was $2.1 trillion" | https://www.ftc.gov/system/files/ftc_gov/pdf/FY24-HSR-ANNUAL-REPORT-FOR-TRANSMITTAL-TO-CONGRESS.pdf |
| Aggregate HSR transaction value $2.5tn in FY2025 | CONFIRMED | FY2025 report: "the aggregate dollar value of reported transactions was $2.5 trillion" | https://www.ftc.gov/system/files/ftc_gov/pdf/fy_2025_hsr_annual_report_for_transmittal_to_congress.pdf |
| Aggregate HSR transaction value about $1.6tn in FY2023 | UNVERIFIABLE | The FY2023 report was not retrieved and the FY2024/FY2025 reports do not restate it. Hedge: "about $1.6 trillion (FY2023 report; not rechecked)" or drop the FY2023 dollar figure and keep the transaction count | n/a |
| Reported transactions 1,805 (FY2023), 2,031 (FY2024), 2,006 (FY2025) | CONFIRMED | Appendix A, "Transactions Reported" row: 1,805 / 2,031 / 2,006 | FY2025 report URL above |
| Transactions above $1bn were "approximately one-fourth" in FY2024 | CONFIRMED (wording fix) | Quote is verbatim: "Approximately one-fourth of these transactions were valued over $1 billion"; Figure 2 of the FY2025 report gives 25.6%. The report says "transactions", not "filings" (filings received were 4,022 in FY2024 and 3,851 in FY2025, a different count) | FY2024 report URL above |
| 31.8% above $1bn in FY2025 | CONFIRMED | "Approximately 31.8% of these transactions were valued over $1 billion" | FY2025 report URL above |
| EA take-private: agreed Sept 29, 2025; PIF, Silver Lake, Affinity Partners; $210 per share cash | CONFIRMED | Ex. 99.1 to EA 8-K: "$210 per share in cash", announced September 29, 2025 | https://www.sec.gov/Archives/edgar/data/712515/000114036125036415/ef20056167_ex99-1.htm |
| EA enterprise value about $55bn | CONFIRMED | "an enterprise value of approximately $55 billion" | same |
| EA quote "the largest all-cash sponsor take-private investment in history" | CONFIRMED | Verbatim in the release body (headline capitalizes it). Release said close expected in Q1 FY27 (Apr-Jun 2026); closing status as of Oct 2026 was not checked | same |
| Union Pacific agreed July 29, 2025 to buy Norfolk Southern at about $85bn EV | UNVERIFIABLE (not fetched) | Consistent with widely reported terms, but no UP or STB primary page was fetched in this pass; budget went to the points that changed. Low risk | n/a |
| UP filed a roughly 7,000-page STB application on Dec 19, 2025 | STALE | The Dec 19 filing is real, but the STB rejected it as incomplete on Jan 16, 2026 (missing market-share projections and the full merger agreement), without prejudice. UP/NS refiled; the STB announced receipt of the revised application on Apr 30, 2026 and on May 28, 2026 found it complete but asked for supplemental information and put the procedural schedule in abeyance. Secondary sources; STB decision pages not fetched | https://fintool.com/news/stb-rejects-up-ns-merger-application ; https://www.dtnpf.com/agriculture/web/ag/news/article/2026/05/11/ns-resubmit-merger-application-stb ; https://railmarket.com/news/business/57579-us-surface-transportation-board-accepts-union-pacific-norfolk-southern-merger-application |
| WBD signed with Netflix on Dec 4, 2025 | UNVERIFIABLE | The Paramount 10-Q refers only to "a prior merger agreement between Netflix and WBD" with no date. Hedge: "in early December 2025" | https://www.sec.gov/Archives/edgar/data/0002041610/000204161026000026/psky-20260331.htm |
| WBD signed with Paramount Skydance Feb 27, 2026 at $31.00 cash | CONFIRMED | 10-Q: "On February 27, 2026, Paramount and Warner Bros. Discovery, Inc. announced a definitive merger agreement"; "Paramount will pay $31.00 per WBD share" (announced, not necessarily signed that day) | same |
| Per-diem ticking fee | CONFIRMED | $0.00277778 per share per day the deal is not closed past Sept 30, 2026, capped at $0.25 per WBD share per 90-day period | same |
| WBD deal closing October 6, 2026 | CONFIRMED (secondary) | Multiple outlets report completion on Tuesday Oct 6, 2026, holders receiving "just over $31" per share (consistent with six days of ticking fee). The WBD closing 8-K was not fetched. The box phrase "closing October 6, 2026" reads as a plan; the deal has actually closed | https://www.lawcommentary.com/articles/paramount-closes-111-billion-warner-bros-discovery-deal-creating-skydance ; https://www.lbc.co.uk/article/94ae9e335a3a40fc88216e2107f213c5-5HjdjTG_2/ |
| "IG market had not had to price [a deep-in-the-money CoC put] at scale since the late 1980s" | UNVERIFIABLE | Editorial historical judgment, no source. Hedge: "for the first time at scale in a generation" | n/a |

**Box 15.2, portability in US public filings**

| claim | verdict | evidence / correct figure | source |
|---|---|---|---|
| EDGAR full-text hits for "Specified Change of Control Event": 1 (2018), 4 (2019), 8 (2020), 11 (2021), 2 (2022), 3 (2023), 5 (2024), 5 (2025), 10 (2026 to mid-Oct) | CONFIRMED (with a missing qualifier) | Reproduced exactly on 2026-10-18, but only after excluding foreign-private-issuer and other forms (20-F, 6-K, F-1, F-4, DRS, T-3, DEFA14A) and keeping 8-K, 8-K/A, 10-K, 10-Q, 424B and S-4. The unfiltered phrase search returns 94 documents / 85 unique filings for 2018-01-01 to 2026-10-17 (by year, unique filings: 9, 6, 12, 15, 7, 5, 11, 10, 10). The box should say which forms are counted | EDGAR full-text search API, query "Specified Change of Control Event", 2018-01-01 to 2026-10-17 |
| 424B2/424B5 using "Change of Control Triggering Event" run 230-400 a year | CONFIRMED (one-year spot check) | 2024: 278 documents | EDGAR full-text search, forms 424B2/424B5, 2024 |
| 424B2/424B5 using "Change of Control Repurchase Event" run 90-230 a year | CONFIRMED (one-year spot check) | 2024: 203 documents. Other years not rerun | same |

**Box 15.3, regulatory regime as a shift in baseline hazard**

| claim | verdict | evidence / correct figure | source |
|---|---|---|---|
| HSR early terminations granted: 1,102 (FY2016), 1,220 (FY2017), 417 (FY2021), 5 (FY2022), 0 (FY2023), 265 (FY2025) | CONFIRMED | Appendix A "Granted" row; FY2024 was 3 (not cited in the box) | FY2025 report URL above |
| Second-request rate oscillated between 1.6% and 3.0% "of adjusted filings" | CONFIRMED (wording fix) | Range is right (FY2022 low 1.55%, FY2016/2019/2020/2024 about 3.0%), but the base is "adjusted transactions" (e.g. 1,944 in FY2025), not filings | FY2025 report, Figure 3 and Appendix A |
| New HSR form took effect February 10, 2025 | CONFIRMED | FTC: "The new Form will be effective on Feb. 10, 2025." | https://www.ftc.gov/enforcement/premerger-notification-program |
| District court vacated it, "FTC notice dated February 12, 2026" | CORRECTED (date attribution) | The vacatur was on February 12, 2026; the FTC notice is dated 02/13/2026 | same |
| Fifth Circuit administrative stay on Feb 19, 2026 | CONFIRMED | "On February 19, 2026, the U.S. Court of Appeals for the Fifth Circuit granted an administrative stay" | same |
| Fifth Circuit denied stay pending appeal on Mar 19, 2026 | CONFIRMED | "On March 19, 2026, the U.S. Court of Appeals denied the Commission's motion for a stay pending appeal" | same |
| Agencies now accept filings on either form | CONFIRMED | Mar 19-20, 2026 notices: old form accepted, new form still accepted if filers choose. The page shows nothing later | same |

<!-- STATUS: PARTIAL (ch15 done; ch16-21 pending) -->
