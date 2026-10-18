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


## Chapter 16: Post-reorg equities and claims

**Box 16.1, the post-reorg premium (1999 to 2010)**

| claim | verdict | evidence / correct figure | source |
|---|---|---|---|
| Eberhart, Altman & Aggarwal (1999), J. Finance 54(5): 131 emerging firms | CONFIRMED | Journal of Finance 54(5), 1855-1868; 131 firms emerging from Chapter 11; authors read the result as market expectational error rather than mismeasured risk | https://ideas.repec.org/p/fth/nystfi/96-22.html |
| 200-trading-day CARs of 22.8% to 29.6% (medians 16.8% to 22.2%) depending on benchmark | UNVERIFIABLE | Abstract and secondary pages say only "positive excess returns over 200 days"; the quoted ranges are in the full text, which was not accessible. Hedge: "double-digit positive excess returns over the first 200 trading days, on every benchmark the authors tried" | same |
| Moyer (p.374): 2001 and 2002 vintage back-end equities beat the S&P 500 in 2003, citing Imperial Capital and Bloomberg; a study of 117 post-reorg equities, 1986-2003, also found outperformance | CONFIRMED | Checked in the local PDF. Moyer p.357 of the printed book (PDF page 374): "During 2003, back-end equities ... significantly outperformed the S&P 500", "regardless of whether the stock emerged in 2001 ... or in 2002", and "117 significant postreorganization equities that emerged between 1986 and 2003". Figure 13-1 source: Imperial Capital and Bloomberg. Note the page number is the PDF page, not the printed page | source_pdfs/Moyer_Distressed_Debt_Analysis.pdf |
| Jiang, Wang & Yang sample: US public filers with at least $50mm assets filing 1981-2016 and emerging public | CONFIRMED | Blog: "all US public firms with $50 million in assets that filed for Chapter 11 from 1981 to 2016 and emerged as public companies". The box heading "1981-2019" is not in the blog; 2019 is presumably the end of the return window (not verified) | https://sites.duke.edu/thefinregblog/2021/09/17/has-post-reorg-equity-outperformed-in-the-last-three-decades/ |
| Mean 200-day abnormal returns 40% to 50%; median abnormal return zero | CONFIRMED | "abnormal returns between 40% and 50%"; "the median abnormal return is zero" | same |
| Equal-weighted monthly-rebalanced portfolio from 1992 (about 20 stocks) beat benchmarks by 7.2% a year | CONFIRMED | Starts January 1992 "when there were 20 actively traded post-reorg stocks"; "outperforms the risk-adjusted benchmark portfolio by 7.2% annually" | same |
| ...concentrated in OTC names | UNVERIFIABLE | Not in the blog text retrieved; may be in the paper | same |
| Five-factor alpha 0.8% to 1.2% a month in 2000-2010, zero after 2010; exchange-listed stocks negative alpha in the latest decade | CONFIRMED | "0.8-1.2% per month between 2000 and 2010"; alpha falls to zero after; exchange-traded "negative alpha in the most recent decade" | same |
| Institutional ownership about 40% (1990s) to about 80% (2000s) | CONFIRMED | "increased from 40% in the 1990s to 80% in the 2000s" | same |
| Paper title "The Disappearing Outperformance of Post-reorg Equity" and author names | UNVERIFIABLE | The blog post is titled "Has Post-reorg Equity Outperformed in the Last Three Decades?"; author names and working-paper title were not retrievable in this pass. Cite the blog by its own title | same |

**Box 16.2, CLO documents and equity**

| claim | verdict | evidence / correct figure | source |
|---|---|---|---|
| O'Melveny (2020), Seward & Kissel notes; S&P video 10 Mar 2021; S&P "Par Wars" 23 Sep 2022; S&P Credit FAQ 26 Jul 2023; Weil note June 2024 | UNVERIFIABLE | Citations with dates only, no numeric claims; none was fetched in this pass (call budget went to the numeric boxes). Low risk, but confirm each date against the publisher page before the next printing | n/a |
| Industry tallies: sharp rise in share of new European CLOs with loss-mitigation language, 2020-2021 | UNVERIFIABLE | The box already flags this as approximate and unsourced; leave the hedge in place | n/a |

**Box 16.3, rights offerings and the courts**

| claim | verdict | evidence / correct figure | source |
|---|---|---|---|
| Seth, CLS Blue Sky Blog, 11 Mar 2025: rights offerings financed about 35% of large Ch. 11 cases (asset-weighted), about 87% by 2019, about $46bn raised | CONFIRMED | "used in 35 percent of Chapter 11 bankruptcies (asset-size weighted)"; "inject roughly $46 billion"; "87 percent of bankruptcies in 2019 by asset size". Author: Gunjan Seth, USC Marshall | https://clsbluesky.law.columbia.edu/2025/03/11/do-rights-offerings-reduce-bargaining-complexity-in-chapter-11/ |
| Backstoppers charge about 6%, buy about 43% of the equity, appoint about 40% of the board; participants earn about 50% in three months | CONFIRMED | "6 percent of the amount raised"; "43 percent of the reorganized firm's equity"; "40 percent of the board members"; "50 percent average returns ... within three months" | same |
| IV estimates: recoveries up about 40%, cases shorter by about seven months | CONFIRMED | "increase total creditor recoveries by roughly 40 percent"; "decrease bankruptcy duration by about seven months". The post gives no baseline for the 40%, and reports a separate 40% reduction in absolute-priority deviations, so do not conflate them | same |
| NBER abstract (Feb 2024) gives 47% on a different basis | CONFIRMED | NBER draft abstract: rights offerings financed 47% of bankruptcies in the past decade | https://conference.nber.org/conf_papers/f194056/f194056.pdf |
| Buccola, Marcovich Gross & McBrady, ABLJ 100(1) (2026): 49 plans, Jan 2016 to June 2024 | CONFIRMED | "plans, confirmed between January 2016 and June 2024 ... The full sample consists of 49 plans" | https://www.ablj.org/wp-content/uploads/2026/04/3-Buccola-Backstop-Party.pdf |
| Average discount to plan value 25%, about 50% effective | CONFIRMED | 25.3% discount to plan-assumed value; "approximately a 50% discount to value" on arm's-length valuations | same |
| All-in backstop compensation 20.1% (25.1% with market-priced values); IPO and seasoned underwriting 3-7% | CONFIRMED | 20.1% full sample; 25.1% on the 19-case market subsample; underwriters "from 3% to 7% of capital raised" | same |
| Per dollar of identical claim: about 21 vs 8 cents (plan values), about 35 vs 19 cents (market values) | CONFIRMED | "21 cents per dollar of eligible claim held, compared to 8 cents"; "35 cents ... 19 cents" | same |
| Fifth Circuit Serta decision, 31 Dec 2024, equal-treatment rule of 1123(a)(4) | CONFIRMED | Opinion filed December 31, 2024 (revised 2/14/2025). The 1123(a)(4) holding is about the plan's indemnity for the Participating Lenders: "its inclusion in the Plan violated the Code's requirement of equal treatment". The same opinion held the uptier was not an "open market purchase" | https://www.ca5.uscourts.gov/opinions/pub/23/23-20181-CV0.pdf |
| ConvergeOne, 25 Sep 2025, S.D. Tex. reversed confirmation of exclusive backstop of a $245mm rights offering with a 10% fee and no market test | CONFIRMED | Law-firm alerts: district court (Judge Hanen) reversed that portion of the confirmation order; $245mm rights offering; fee of additional equity equal to 10% of the amount raised; exclusive to the majority first-lien lenders (about 81% of the class); held a violation of 1123(a)(4) absent a market test; drew on Serta | https://www.clearygottlieb.com/news-and-insights/publication-listing/us-district-court-finds-that-exclusive-backstop-agreement-violates-equal-treatment-in-convergeone |
| Debtors noticed an appeal on 22 Oct 2025; no Fifth Circuit ruling in October 2026 | UNVERIFIABLE | Neither the notice date nor the appeal's status could be confirmed; a targeted search found no Fifth Circuit ruling either. Hedge: "an appeal was reported pending; check the docket before relying on this" | n/a |
| LATAM's $5.4bn backstop for a subset of unsecured creditors approved after court-ordered mediation, on business-judgment grounds | UNVERIFIABLE | Not checked in this pass (call budget). Verify the $5.4bn figure, the mediation and the standard in the bankruptcy court's decision before printing | n/a |

**Box 16.4, claims trading and FTX**

| claim | verdict | evidence / correct figure | source |
|---|---|---|---|
| FTX claims about 15% of face at start of 2023 and about 35% by Sept 2023 (Claims Market pricing, cited by Decrypt, 22 Sep 2023) | UNVERIFIABLE (conflict on the starting level) | The Decrypt piece was not found. Reprints of the Bloomberg story (21 Sep 2023) say Claims Market quotes for some lower-ranked FTX claims rose to about 35 cents "up from 12 cents at the start of the year". Hedge: "from roughly 12-15 cents to about 35 cents" and cite Bloomberg, 21 Sep 2023 | https://www.bloomberg.com/news/articles/2023-09-21/silver-point-diameter-buying-cheap-ftx-claims-in-lehman-redux |
| More than $250mm of claims bought by Silver Point, Diameter and Attestor; a $23mm claim bought by Hudson Bay | CONFIRMED | Bloomberg 21 Sep 2023: "bought more than $250 million worth of FTX debts since the beginning of the year"; Hudson Bay "buy a $23 million claim ... and sell about half of it to Diameter" | same, via https://www.bnnbloomberg.ca/silver-point-diameter-scoop-up-cheap-ftx-bankruptcy-claims-in-lehman-redux-1.1974701 |
| Possibly more than $100mm of unreported trades because of transfer-paperwork lags | UNVERIFIABLE | Decrypt-only statement | n/a |
| Convenience class (Class 7): 100% plus 9% annual interest from 11 Nov 2022, about 120% cumulative | CONFIRMED (120%); UNVERIFIABLE (9% term) | Trust release of the 31 Mar 2026 distribution: Class 7 "cumulative 120%", measured against 11 Nov 2022 claim values. The 9% rate was not seen in a primary document | https://lifestyle.kbew98country.com/story/122645/ftx-recovery-trust-to-distribute-approximately-22-billion-to-creditors-in-fourth-distribution-on-march-31-2026/ |
| Larger-class distributions began 30 May 2025 with more than $5bn, then about $1.6bn in Sept 2025 | UNVERIFIABLE (not rechecked) | Consistent with the Trust numbering 31 Mar 2026 as the "fourth distribution", but the May and September dates and amounts were not fetched | n/a |
| About $2.2bn on 31 Mar 2026, taking 5A to about 96% and 5B to about 100% | CONFIRMED, now STALE | 31 Mar 2026 distribution (about $2.2bn): 5A +18% to 96%, 5B +5% to 100%. A fifth distribution of about $900mm, announced in the Trust's 17 Jul 2026 release for 31 Jul 2026, takes 5A and 5B to 105% each (5A +9%, 5B +5%) and general unsecured and digital-asset-loan classes to 103%; cumulative distributions approach $11bn. Source is press coverage of the release; payment itself not confirmed | https://startupfortune.com/ftx-will-pay-creditors-up-to-120-percent-of-their-claims-next-month/ |
| Lehman era: monthly claims trading about $2.2-3.6bn (2011 Reuters, SecondMarket data) | UNVERIFIABLE | Not checked; the box already marks it approximate. Keep the hedge | n/a |
| A buyer went "from about 15 cents to more than 100 cents ... roughly seven times the money" | UNVERIFIABLE (arithmetic depends on the 15 cents) | 105/15 = 7x, but from 12 cents it is about 9x. Hedge: "roughly seven to nine times" | derived |

<!-- STATUS: PARTIAL (ch15-16 done; ch17-21 pending) -->
