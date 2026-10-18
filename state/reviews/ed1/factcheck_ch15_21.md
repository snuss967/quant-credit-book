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
| Transactions above $1bn were "approximately one-fourth" of filings in FY2024 | CORRECTED (wording: "filings" should be "reported transactions") | Quote is verbatim: "Approximately one-fourth of these transactions were valued over $1 billion"; Figure 2 of the FY2025 report gives 25.6%. The report says "transactions", not "filings" (filings received were 4,022 in FY2024 and 3,851 in FY2025, a different count) | FY2024 report URL above |
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
| Second-request rate oscillated between 1.6% and 3.0% "of adjusted filings" | CORRECTED (wording: "adjusted transactions") | Range is right (FY2022 low 1.55%, FY2016/2019/2020/2024 about 3.0%), but the base is "adjusted transactions" (e.g. 1,944 in FY2025), not filings | FY2025 report, Figure 3 and Appendix A |
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
| Convenience class (Class 7) reached about 120% cumulative, measured from 11 Nov 2022 | CONFIRMED | Trust release of the 31 Mar 2026 distribution: Class 7 "cumulative 120%", measured against 11 Nov 2022 claim values | https://lifestyle.kbew98country.com/story/122645/ftx-recovery-trust-to-distribute-approximately-22-billion-to-creditors-in-fourth-distribution-on-march-31-2026/ |
| Convenience class interest term of 9% a year | UNVERIFIABLE | The 9% rate was not seen in a primary document in this pass; the 120% total is consistent with it | n/a |
| Larger-class distributions began 30 May 2025 with more than $5bn, then about $1.6bn in Sept 2025 | UNVERIFIABLE (not rechecked) | Consistent with the Trust numbering 31 Mar 2026 as the "fourth distribution", but the May and September dates and amounts were not fetched | n/a |
| About $2.2bn on 31 Mar 2026, taking 5A to about 96% and 5B to about 100% | CONFIRMED, now STALE | 31 Mar 2026 distribution (about $2.2bn): 5A +18% to 96%, 5B +5% to 100%. A fifth distribution of about $900mm, announced in the Trust's 17 Jul 2026 release for 31 Jul 2026, takes 5A and 5B to 105% each (5A +9%, 5B +5%) and general unsecured and digital-asset-loan classes to 103%; cumulative distributions approach $11bn. Source is press coverage of the release; payment itself not confirmed | https://startupfortune.com/ftx-will-pay-creditors-up-to-120-percent-of-their-claims-next-month/ |
| Lehman era: monthly claims trading about $2.2-3.6bn (2011 Reuters, SecondMarket data) | UNVERIFIABLE | Not checked; the box already marks it approximate. Keep the hedge | n/a |
| A buyer went "from about 15 cents to more than 100 cents ... roughly seven times the money" | UNVERIFIABLE (arithmetic depends on the 15 cents) | 105/15 = 7x, but from 12 cents it is about 9x. Hedge: "roughly seven to nine times" | derived |


## Chapter 17: Private credit and public-private convergence

**Box 17.1, from niche to a Z.1 line item**

| claim | verdict | evidence / correct figure | source |
|---|---|---|---|
| Private-credit vehicle AUM about $350bn in 2012 to more than $2.6tn (Brinkman et al., FEDS Note, Oct 16, 2026) | CONFIRMED | "approximately $350 billion in 2012 to over $2.6 trillion as of 2025:Q4". Authors: Brinkman, Dobridge, Dore, Glossner, Holmquist, Nguyen, Perozek, Stefanescu; published October 16, 2026 | https://www.federalreserve.gov/econres/notes/feds-notes/introducing-private-credit-into-the-financial-accounts-of-the-united-states-20261016.html |
| Z.1 private-credit loans $1,042.6B (2023), $1,253.6B (2024), $1,493.5B (2025), about 20% a year | CONFIRMED | Table 6 "Total liabilities" row; growth 20.2% (2024) and 19.1% (2025). The row includes $35.1B of loans to rest-of-world borrowers, so "US private-credit loans" is slightly loose; the note itself says "$1.5 trillion in private credit loans extended to U.S. businesses" | same |
| Private credit 6% of nonfinancial business debt vs 3% for syndicated loans | CONFIRMED | Table 8, 2025:Q4: private credit $1.31T of $23.29T (about 6%); syndicated loans $0.77T (about 3%). Note the 6% uses $1.31T, not the $1.49T above | same |
| Z.1 codes FL893167205 (total), FL453067203 (BDCs), FL443067205 (private debt funds), FL673067205 (middle-market CLOs) | CONFIRMED | FL893167205 = total liabilities of the instrument; FL453067203 = held by BDCs; FL443067205 = held by private debt funds; FL673067205 = held by ABS issuers, "which covers U.S. middle-market CLOs" | same |
| Semi-liquid fund net assets about $15B (2018) to $388B (2025) (George and Shin, FEDS Note, Oct 14, 2026) | CONFIRMED | "from $15 billion in 2018 to $388 billion in 2025"; scope is interval funds, tender-offer funds and non-traded perpetual BDCs, a lower-bound estimate. Authors Logan George and Chaehee Shin; dated October 14, 2026 | https://www.federalreserve.gov/econres/notes/feds-notes/the-rise-of-semiliquid-funds-for-retail-investors-20261014.html |
| BDC loans held by private-credit BDCs rose from 1,395 (2010) to 20,182 (2022) (Ellias and de Fontenay, 134 Yale L.J., Jan 2025) | UNVERIFIABLE | Not fetched. Hedge: "from roughly 1,400 to roughly 20,000 loans" until checked against the article | n/a |
| Global AUM passed $2.2T in March 2025, forecast $4.5T for 2030 (BlackRock, Private Credit Primer, Jan 2026) | UNVERIFIABLE | PDF not fetched in this pass. Note that the Fed figure above ($2.6tn at 2025:Q4) and the BlackRock figure ($2.2T at March 2025) are different definitions; the box should not set them side by side without saying so | https://www.blackrock.com/gls-download/literature/market-commentary/private-credit-primer-january-2026.pdf |

**Box 17.2, the bank and private credit partnership wave**

| claim | verdict | evidence / correct figure | source |
|---|---|---|---|
| Sept 26, 2024: Citi and Apollo announce a $25bn program, "initially in North America", Mubadala strategic partner, Athene participating, "flexibility to significantly expand" | UNVERIFIABLE (not rechecked) | A targeted search returned nothing on the Citi-Apollo release; details match my recollection of the release but were not sourced in this pass | n/a |
| Feb 24, 2025: J.P. Morgan raises direct-lending balance-sheet commitment to $50bn plus "nearly $15 billion from multiple co-lenders"; "over $10 billion across more than 100 private credit transactions" since 2021 | CONFIRMED | JPM release of February 24, 2025 (announced at its 30th Global Leveraged Finance Conference) | https://www.jpmorgan.com/about-us/corporate-news/2025/jpmorgan-increases-direct-lending-commitment-to-50-billion |
| May 2025: committed bank lines to private-credit vehicles about $95bn (Fed) | UNVERIFIABLE | Not found in the May 8, 2026 FSR and the May 2025 FEDS note was not fetched. Check "committed" vs "drawn" before printing | https://www.federalreserve.gov/econres/notes/feds-notes/bank-lending-to-private-credit-size-characteristics-and-financial-stability-implications-20250523.html |
| May 8, 2026: bank commitments to nonbank financial institutions total $2.6tn, with PE, BDCs and private credit the largest category after a $261bn upward revision | CONFIRMED (date and scope nuance) | FSR: commitments "grew ... in the fourth quarter of 2025 to $2.6 trillion"; PE/BDCs/private credit "the largest portion"; commitments to that category "revised up by $261 billion in the fourth quarter of 2025". The $2.6tn is a 2025:Q4 level and the $261bn is a reclassification, not new lending | https://www.federalreserve.gov/publications/files/financial-stability-report-20260508.pdf |
| Aug 7, 2026: bank loans about 40% of BDC debt, double their share a decade earlier (Haque and Wang) | CONFIRMED | "Bank loans now make up about 40 percent of BDC debt on average, up from about 20 percent a decade ago" (the share peaked near 50% in 2022). Authors Sharjil Haque and Jessie Jiaxu Wang | https://www.federalreserve.gov/econres/notes/feds-notes/the-price-of-bank-funding-behind-private-credit-evidence-from-business-development-companies-20260807.html |

**Box 17.3, the listed discount and the redemption queue**

| claim | verdict | evidence / correct figure | source |
|---|---|---|---|
| Nov 5-19, 2025: OBDC/OBDC II NAV-for-NAV merger announced and terminated within fourteen days | UNVERIFIABLE (not rechecked) | A targeted search did not return the November 2025 releases. The dossier's CNBC link of 2025-11-19 headlines the call-off, which fits; announcement date not seen | https://www.cnbc.com/2025/11/19/blue-owl-calls-off-merger-of-its-two-private-credit-funds-after-announcement-rattles-stock-sources-say.html |
| Feb 18, 2026: OBDC II replaces tender offers with return-of-capital distributions | CONFIRMED | Blue Owl release: up to $2.35 per share (about 30% of NAV at Dec 31, 2025) on or before March 31, 2026, to replace future quarterly tender offers; Blue Owl disputed that it was "halting" liquidity | https://www.blueowlcapitalcorporation.com/_assets/_a3f02cd34898c21e626100ac4e4bbfee/blueowlcapitalcorporation/news/2026-02-18_Certain_Blue_Owl_BDCs_to_Sell_1_4_Billion_of_89.pdf |
| Feb 18, 2026: OBDC repurchases stock at 86% of book | UNVERIFIABLE | The 86% figure was not found in the release excerpts retrieved (the same-day release was about a $1.4bn loan sale by certain Blue Owl BDCs). The chapter body ties it to a Q4 NAV of $14.81, which would be a repurchase price near $12.7. Check against the OBDC Q4 earnings release before printing; hedge: "buybacks at a discount of roughly 14% to book" | same |
| Mar 26, 2026: about $13bn of Q1 requests, more than $4.6bn trapped (Bloomberg Law) | UNVERIFIABLE | Paywalled; not fetched | n/a |
| End March 2026: median listed BDC about 0.74x forward NAV, widest since 2020 (Reuters/LSEG) | UNVERIFIABLE | The box already flags it. Consistency flag: 0.74x is a 26% discount, while the Apr 16 Octus line says "nearly a 20% discount"; the two may be different statistics (median vs average, forward vs reported NAV) or a rebound. Say which | n/a |
| Apr 14, 2026: IMF estimates non-traded BDCs can meet 5% quarterly redemptions for 9-11 quarters (mild stress) and 5-7 (moderate) | UNVERIFIABLE | IMF GFSR chapter 1 not fetched. The Fed FSR gives a different measure (cash covers "at least three calendar quarters" of net redemptions at the 5% level) | https://www.imf.org/-/media/files/publications/gfsr/2026/april/english/ch1.pdf |
| Apr 16, 2026: listed BDCs at "nearly a 20% discount", some "approaching a 50% discount" (Octus) | UNVERIFIABLE | Paywalled; see the consistency flag above | n/a |
| May 8, 2026: first quarter on record in which accepted redemptions exceeded inflows (Fed FSR) | CONFIRMED (scope nuance) | FSR: for perpetual BDCs, "accepted redemption requests somewhat exceeded new inflows in the first quarter of 2026, the first time this has occurred since these vehicles were created". The record is for perpetual BDCs, not all private credit vehicles | https://www.federalreserve.gov/publications/files/financial-stability-report-20260508.pdf |
| June 23, 2026: $26bn fund at 16.8% requests, $79bn fund at 10% (InvestmentNews) | UNVERIFIABLE | Not fetched | n/a |

**Box 17.4, from "no price" to five price sources**

| claim | verdict | evidence / correct figure | source |
|---|---|---|---|
| Man (2022): daily vendor pricing on 6,500 loan facilities; private credit "problematic from a data availability perspective" (p.41) | CONFIRMED | Man p.41: "loans and other private credit instruments are obviously problematic from a data availability perspective ... Already both Refinitiv and IHS Markit are providing daily pricing on 6,500 loan facilities." The vendors, not Man, provide the pricing; the quote covers "loans and other private credit instruments" | source_pdfs/Man_Quantitative_Credit_Alpha_Early_Mover_2022.pdf |
| Feb 2025: PRIV launches with a manager's firm bid on its private sleeve (State Street) | UNVERIFIABLE (not rechecked) | State Street product page not fetched; the launch month matches my recollection | https://www.ssga.com/us/en/intermediary/etfs/spdr-ssga-ig-public-private-credit-etf-priv |
| Mar 2026: ICE passes 5,000 private-credit identifiers (Apollo release) | UNVERIFIABLE | Not fetched. An ICE statistic cited to an Apollo release should be traced to ICE | n/a |
| Apr 2026: CDX Financials begins trading, reportedly with BDCs among its names (S&P DJI; unverified) | UNVERIFIABLE | The box already flags it | n/a |
| July 1 and Oct 1, 2026: Apollo daily pricing reaches IG then all credit vehicles; asset-level from Oct 30 | UNVERIFIABLE | Apollo release (Oct 2026) not fetched | https://www.apollo.com/insights-news/pressreleases/2026/10/apollo-expands-daily-pricing-to-all-credit-assets-advancing-transparency-in-private-credit-3372805 |
| Oct 16, 2026: private credit enters the Fed's Z.1 with holder-level series | CONFIRMED | FEDS Note of October 16, 2026, "Introducing Private Credit into the Financial Accounts of the United States" | Brinkman URL above |


## Chapter 18: OTC microstructure and Avellaneda-Stoikov

**Box 18.1, the great spread compression and its stress reversals**

| claim | verdict | evidence / correct figure | source |
|---|---|---|---|
| TRACE dissemination phased in 2002 to 2005 | UNVERIFIABLE (not rechecked; standard history) | Not fetched in this pass. Low risk | n/a |
| Edwards, Harris & Piwowar (2007, JF 62(3)) and Goldstein, Hotchkiss & Sirri (2007, RFS 20(2)) "both find that transparency lowered customer trading costs" | CORRECTED (overstated for GHS) | Citations are right (JF 62(3): 1421-1451; RFS 20(2): 235-273). EHP: costs "drop when the TRACE system starts to publicly disseminate their prices". GHS: transparency has "either a neutral or a positive effect on liquidity", spreads decline "except for very large trades", and no effect for very infrequently traded bonds | https://ideas.repec.org/a/bla/jfinan/v62y2007i3p1421-1451.html ; https://ideas.repec.org/a/oup/rfinst/v20y2007i2p235-273..html |
| Chen, Lesmond & Wei (2007): bid-ask about 25 bp for AAA and 180 bp for CCC | CONFIRMED | As reported by Man p.20: "the bid-ask spread for AAA-rated corporate bonds was estimated at 25bps, while for CCC-rated bonds it was 180bps" (checked in Man, not in the original paper) | source_pdfs/Man_Quantitative_Credit_Alpha_Early_Mover_2022.pdf |
| Man (2022, p.20): spreads "markedly tighter in the current market" | CONFIRMED | "Both of these figures would be markedly tighter in the current market." | same |
| Man chart: 20-day average HY bid-ask, Bloomberg, 1 July 2017 to 2 February 2021, gaps out Feb-Mar 2020 then normalizes | CONFIRMED | "Source: Bloomberg. Date range: 1 July 2017 to 2 February 2021"; text: "gap out in times of crisis like February/March 2020, levels swiftly return to normal" | same |
| Kargar et al. (2021, RFS): willingness to pay for immediacy up roughly 200 bp per dollar traded at the March 2020 peak; flow shifted from risky-principal to agency trades | CONFIRMED | RFS 34(11): 5352-5401 (2021); willingness to pay "roughly 200 basis points per dollar traded" at the peak; risky-principal costs rose (about fivefold per the working-paper abstract) and customers shifted to slower agency trades | https://nber.org/papers/w27355 |
| MarketAxess data (The DESK, 2026-10-01): median EUR IG bid-ask fell from 0.0879 to 0.0673 (-23.5%) "over the 34 weeks to 2026-08-23" | CORRECTED | The article compares the 34 weeks to 23 Aug 2026 with the same weeks of 2025 (year over year), in price % of par: "Median bid-ask fell from 0.0879 to 0.0673 price % of par, a compression of 23.5%". It is not a decline within the 34-week window. Article by Nick Dunbar, 1 Oct 2026 | https://www.fi-desk.com/liquidity-improves-amid-1-trillion-surge-in-corporate-debt/ |
| March 2026 stress: EUR IG bid-ask 64% above its January average | CONFIRMED (caveat) | Article: European IG "repriced harder - 64% above its January average at the single-week peak" in "the four weeks from 1 March"; its wording is "repriced", not "bid-ask", though the surrounding measure is the spread | same |
| Recovery: 4 weeks (EUR IG), 6 (US HY), 8 (US IG), 13 (EUR HY) | CONFIRMED | "Euro investment grade regained its pre-stress spread in four weeks, US high yield in six ... US investment grade in eight and euro high yield in 13" | same |
| Recovery: "14+ (EM)" | CORRECTED | "Emerging markets took 14 and then widened again, and has been above its January level in 21 of the 22 weeks since the peak." Fourteen weeks is not a floor; EM recovered and then re-widened | same |

**Box 18.2, the vanishing, then negative, dealer inventory**

| claim | verdict | evidence / correct figure | source |
|---|---|---|---|
| Bessembinder, Spatt & Venkataraman (2020, JFQA 55(1)): non-bank dealers 12.5% of customer-dealer volume in 2014-16 vs 2.4% before the crisis | UNVERIFIABLE | Sourced to "our industry dossier"; the survey was not retrieved. Hedge: "non-bank dealers' share of customer-dealer volume rose several-fold after the crisis" | n/a |
| March 2020: Kargar et al. find risky-principal costs "increased dramatically", flow shifted to agency | CONFIRMED (substance) | See Kargar row above; the quoted phrase was not located verbatim, the finding is | https://nber.org/papers/w27355 |
| The DESK (2024-11-20): primary dealers net short US$3.8bn of IG bonds over five years; McPartland quote ("agency (or at most, riskless principal)") | UNVERIFIABLE | Not fetched (The DESK, possibly paywalled). A same-themed DESK piece exists: https://www.fi-desk.com/?p=19715 | n/a |
| Hedgeweek (2026-07-13), Crisil Coalition Greenwich analysis of Fed data: primary dealers net short US corporates, about $4bn on average in 2026, first time in at least 25 years, vs about $16bn net long in 2017 | CONFIRMED | Coverage: "net short ... for the first time in at least 25 years"; average net short about $4bn in 2026 vs long inventories of about $16bn in 2017. The date 2026-07-13 matches Bloomberg's "Banks' Record Bond Short" Credit Weekly of that day | https://www.hedgeweek.com/banks-turn-net-short-corporate-bonds-for-first-time-as-market-structure-shifts/ |
| About $13.7bn short over five years and $9.7bn long in shorter paper | CONFIRMED | "short roughly $13.7bn of bonds maturing in five years or more, offset by a $9.66bn long position in shorter-dated debt" (nets to about $4bn short). Caveat from the coverage: cash bonds only, offsetting derivative positions excluded; the "squeeze risk" argument should say so | same |

**Box 18.3, the auto-quoting arms race**

| claim | verdict | evidence / correct figure | source |
|---|---|---|---|
| Tradeweb AiEX more than 40% of institutional trades in 2025 vs 30% in 2021 (Tradeweb 10-K FY2025) | UNVERIFIABLE | 10-K not fetched in this pass | https://www.sec.gov/Archives/edgar/data/1758730/000175873026000015/tw-20251231.htm |
| MarketAxess dealer algorithmic responses 32.5m (2023) to 40.9m (2024); clients using automated solutions 204, 245, 261 (2023-25) | UNVERIFIABLE | MarketAxess 10-Ks not fetched | https://www.sec.gov/Archives/edgar/data/1278021/000119312526067009/mktx-20251231.htm |
| Coalition Greenwich (June 2024): about 30% of dealer volume at no human touch, 57% at top-tier dealers, 70% at non-bank LPs, about 30,000 inquiries a day | UNVERIFIABLE | Sourced to the Chapter 3 brief; report not retrieved | n/a |
| Trumid executed 88% of eligible RFQ line items no-touch in Sept 2025 (The DESK, 2025-10-08) | UNVERIFIABLE | Not fetched | n/a |
| Q3-2024 Barclays survey: 60% of credit participants using auto-execution, up from 40% (The DESK, 2025-01-16) | UNVERIFIABLE | Not fetched | https://www.fi-desk.com/fixed-income-automation-surge-60-of-credit-traders-now-use-robots/ |
| Oct 2026: Vanguard about 70% of volume automated, nothing sent without a trader; ELPs "help mainly in normal markets" (The DESK) | UNVERIFIABLE | Not fetched | https://www.fi-desk.com/fils-europe-vanguard-automates-70-of-trades-others-urge-caution/ |
| Citadel Securities self-reported 14.2% share of IG block risk transfer (The DESK, 2026-10-08) | UNVERIFIABLE | Self-reported, as the box says | https://www.fi-desk.com/citadel-securities-reveals-glimpse-of-credit-platform-broker-rankings/ |

**Box 18.4, BWIC supply**

| claim | verdict | evidence / correct figure | source |
|---|---|---|---|
| 2021 BWIC volume averaged $5.2bn a quarter; Q2-2022 $6.8bn with CLOs 55% (TwentyFour AM, 2022-07-11) | UNVERIFIABLE | Not fetched | n/a |
| UK mini-Budget triggered the gilt/LDI crisis in late Sept 2022; BoE began temporary long-gilt purchases on 28 September | UNVERIFIABLE (not rechecked; well-documented) | Public record, not refetched in this pass. Low risk | n/a |
| More than EUR1.5bn of CLOs listed via BWICs the following week, about EUR400m on one Tuesday, AA cash prices "in the 80s" (TwentyFour AM, 2022-10-05) | UNVERIFIABLE | Not fetched | n/a |
| 9fin (2025-12-02): insurer listed more than $1bn of triple-A US CLOs in one BWIC; SCI (2026-02-16): $56bn twelve-month US BSL CLO BWIC total | UNVERIFIABLE | Headline-level, flagged "period CHECK" in the box | n/a |

## Chapter 19: Portfolio trading and pricing engines

**Box 19.1, the basket protocol**

| claim | verdict | evidence / correct figure | source |
|---|---|---|---|
| About 1% of IG volume in 2018 and 7% in 2021 (Meli & Todorova, Dec 2023 version) | UNVERIFIABLE | Paper not fetched | n/a |
| PT a record 5.4% of US corporate transactions in Jan 2021 vs 2.2% a year earlier (Tradeweb data via IFR) | UNVERIFIABLE | Not fetched | n/a |
| Barclays PT desk from "virtually zero" in 2018 to more than 2,000 inquiries and $175bn in 2021; PT about 8% of US credit volume by mid-2022 (The DESK, 2022-06-01) | UNVERIFIABLE | Not fetched | https://www.fi-desk.com/portfolio-trading-gaining-ground-fast-says-barclays/ |
| 2024: PT about 10% of IG and 8% of HY volume; electronic PT averaged $3.3bn a day, up 76% (Coalition Greenwich, Jan 2025) | CONFIRMED | "Portfolio trading accounted for an average of 10% of IG volume and 8% of HY volume in 2024"; e-PT ADNV "was $3.3 billion, which is 76% (or $1.4 billion) higher than 2023" (e-PT is about 85% of total PT volume) | https://coalitiongreenwich.crisil.com/content/dam/coalition-greenwich/MarketViews/2025/US-corporate-bond-trading-2024-numbers-25-C4001.pdf |
| March 2025: about 25% of institutionally sized US IG risk trades via PT, up from just over 20% in January (Bloomberg Market Dialogues, 2025-07-07) | UNVERIFIABLE | Not fetched | n/a |
| PT 12% of the $89.7bn traded on 2025-04-08 (Coalition Greenwich citing Trumid); 18% of $84.7bn on 2025-09-30 | UNVERIFIABLE | Not fetched; the box already notes the two "record" claims use different volume definitions | https://www.greenwich.com/market-structure-technology/us-corporate-bond-trading-2025-numbers |
| MarketAxess about 13% of electronic PT in 2024 vs Tradeweb's more than two-thirds (Coalition Greenwich) | CONFIRMED | "Tradeweb ... over two-thirds of executed volume in 2024 ... Trumid and MarketAxess each executed 13% of notional PT e-volume, and Bloomberg the remaining 7%". Trumid's equal 13% is worth a mention | same |
| MarketAxess estimated 20.9% share of US credit PT in Jan 2026 and 22.0% in May 2026 (monthly volume releases) | UNVERIFIABLE | Monthly releases not fetched | https://investor.marketaxess.com/news/news-details/2026/MarketAxess-Announces-Trading-Volume-Statistics-for-June-and-Second-Quarter-2026/default.aspx |
| SCOOS (June 2025): nearly two-thirds of dealers active in PT; four-fifths of those increased PT provision after Jan 2023; about four-fifths expect to do more | UNVERIFIABLE | Not fetched | n/a |

## Chapter 20: Credit ETF creation, redemption and arbitrage

**Box 20.1, the wrapper eats the bond market**

| claim | verdict | evidence / correct figure | source |
|---|---|---|---|
| SEC adopted Rule 6c-11 on 2019-09-26; ETFs "come directly to market without the cost and delay of obtaining an exemptive order" | CONFIRMED | SEC press release 2019-190, dateline Sept. 26, 2019; Fact Sheet quote verbatim | https://www.sec.gov/news/press-release/2019-190 |
| At adoption about 2,000 ETFs with more than $3.3tn; more than 300 exemptive orders since 1992 | CONFIRMED | "approximately 2,000 ETFs with over $3.3 trillion in total net assets"; "Since 1992, the Commission has issued more than 300 exemptive orders" | same |
| Rule effective 2019-12-23 (Release 33-10695) | UNVERIFIABLE (low risk) | The press release gives no calendar date ("effective 60 days after publication in the Federal Register"); the release page was not fetched | same |
| Bond ETF assets passed $1.2tn in early 2021 (Shim & Todorov, BIS WP 975, 2021) | UNVERIFIABLE | Not fetched. Check that the BIS paper number and authors match; the dossier links BIS Quarterly Review r_qt2103d | https://www.bis.org/publ/qtrpdf/r_qt2103d.htm |
| US bond ETFs held $1.8tn at end-2024, 17% of all ETF assets; net issuance $295bn (2024) vs $201bn (2023) (ICI 2025 Fact Book, pp. 59-63) | CONFIRMED | "Bond ETFs ... accounted for $1.8 trillion (17 percent) of ETF net assets"; "net share issuance increasing from $201 billion in 2023 to $295 billion in 2024". The page range "pp. 59-63" was not checked | https://www.ici.org/system/files/2025-05/2025-factbook.pdf |
| State Street data via Advisor Perspectives: bond ETF assets above $2.5tn and record $64bn monthly inflow in May 2026 | UNVERIFIABLE | Already marked CHECK in the box; not fetched | n/a |
| Oct 2026: LQD $28.78bn, HYG $17.18bn, HYG well below its 2020 size | UNVERIFIABLE | Fund-level AUM not fetched; already marked CHECK in the box | n/a |

**Box 20.2, the basket triangle: ETF, portfolio trade, cash**

| claim | verdict | evidence / correct figure | source |
|---|---|---|---|
| Man calls 2021 "the year of portfolio trading", attributing it partly to bond ETF growth (Man 2023 p.2); PT costs rising in H1 2022 as custom baskets were lost (p.3) | CONFIRMED | p.2: "2021 then became ... the year of portfolio trading", attributed to "the growth of bond ETF trading and the advances made by algorithmic market-making desks"; p.3: PT transaction costs "increased through the first half of the year ... the loss of customised baskets for the ETF creation/redemption process is likely to have been another aggravating factor" | source_pdfs/Man_Revolutions_in_Credit_Trading_2023.pdf |
| Credit ETF ADNV $7.7bn in 2024, down 7%; cash-bond volume +21%; ETF-to-cash ratio 23.2% (2022) to 16.6% (2024) | CONFIRMED | "trading volume in the largest credit ETFs decline 7% year over year, while bond volume grew 21% ... ETF-to-cash ratio down to 16.6% from a high of 23.2% in 2022"; chart: $8,221m (2023) to $7,679m (2024). The base is 12 named ETFs, not all credit ETFs | Coalition Greenwich URL above |
| Feb 2024: credit ETFs 17% of bond notional volume, lowest since Q2 2021 (The DESK citing Coalition Greenwich, 2024-03-19) | UNVERIFIABLE | Not fetched | n/a |
| TRACE portfolio-trade modifier mandatory from 2023-05-15 (FINRA Regulatory Notice 22-12) | UNVERIFIABLE | Notice not fetched in this pass; confirm the effective date on the FINRA page | https://www.finra.org/rules-guidance/notices/22-12 |
| About $99bn of fixed income ETFs traded on 2025-04-07, roughly 60% in iShares funds (The DESK, 2025-06-10) | UNVERIFIABLE | Not fetched | n/a |

## Chapter 21: Leveraged loans and CLO microstructure

**Box 21.1, from bank asset to CLO asset**

| claim | verdict | evidence / correct figure | source |
|---|---|---|---|
| End-2018 US CLOs outstanding $617bn, "approximately half of U.S. leveraged loans outstanding" (FEDS Note, "Who Owns U.S. CLO Securities?", 2019) | UNVERIFIABLE | Note not fetched | https://www.federalreserve.gov/econres/notes/feds-notes/who-owns-us-clo-securities-20190719.htm |
| 2025:Q4 institutional leveraged loans $1,549bn, 12.6% average annual growth since 2000, fastest in the Fed's table (FSR, 8 May 2026, Table 1.1) | CONFIRMED | Table 1.1: leveraged loans 1,549 outstanding; 9.2% growth 2024:Q4-2025:Q4; 12.6% average annual growth (2000 to 2025:Q4); highest of the eight rows (public equities 9.9, Treasuries 8.1, IG bonds 7.8) | https://www.federalreserve.gov/publications/files/financial-stability-report-20260508.pdf |
| CLOs hold about two-thirds of outstandings and buy "nearly three-quarters" of new issue (Deutsche Bank Flow, 7 Oct 2025) | UNVERIFIABLE | Not fetched; already marked approximate | https://flow.db.com/Topics/trust-and-securities-services/update-on-clos-outlook-for-2026 |
| Bank-loan mutual funds shrank 21% to $71bn over 2019-2025; median liquidity ratio from about 10% (2021) to about 4.5% (FEDS Note, 19 Aug 2026) | CONFIRMED | "declined by $19 billion (21 percent) to $71 billion" (2019Q4 to 2025Q4); ratio "almost ten percent of net assets in 2021" and "about four-and-a-half percent since 2024". Authors Anadu, Baker, Cai, George, Larsson | https://www.federalreserve.gov/econres/notes/feds-notes/liquidity-transformation-risks-in-u-s-bank-loan-and-high-yield-mutual-funds-a-2026-update-20260819.html |
| USD LIBOR panels ended 30 June 2023; ARRC CSAs 11.448/26.161/42.826 bp (1m/3m/6m) | UNVERIFIABLE (not rechecked; standard public record) | Not fetched in this pass. Low risk | n/a |
| 2025: gross loan issuance about $400bn, only about $106bn net new vs $294bn repayments (Eagle Point Income Co, Form N-CSR FY2025) | UNVERIFIABLE | N-CSR not fetched (the numbers are internally consistent: 400 - 294 = 106). A fund shareholder report is an indirect source for market-wide issuance; consider citing LSTA or PitchBook LCD instead | https://www.sec.gov/Archives/edgar/data/1754836/000199937126004310/eic_ncsr-123125.htm |

**Box 21.2, settlement and e-trading**

| claim | verdict | evidence / correct figure | source |
|---|---|---|---|
| T+10 par / T+30 distressed with delays to 120 days (Moyer p.322, 2004) | CONFIRMED (citation-year nit) | Moyer printed p.305 (PDF p.322): "10 days (T+10)" for par loans; "30 days, but delays (sometimes of up to 120 days) are fairly common" for distressed. The copyright page reads "Copyright 2005"; the "2004" appears only in the Library of Congress call number. The book uses "2004" in several chapters | source_pdfs/Moyer_Distressed_Debt_Analysis.pdf |
| Median T+12 falling to T+9 after the Sept 2016 delayed-comp protocol (Markets Media, Nov 2016); ten-year average near 20 days to Jan 2025 (LSTA slides; CHECK) | UNVERIFIABLE | Not fetched; the second is already marked CHECK | n/a |
| Bonds T+3 to T+2 (2017) to T+1 (May 2024) | UNVERIFIABLE (not rechecked; standard public record) | Low risk | n/a |
| Secondary loan trading $824bn in 2022 (then a record), $821.4bn in 2024, record $971bn in 2025 | CONFIRMED | LSTA: 2025 annual volume $971bn, "18% higher than 2022's previous record of $824 billion and 2024's $821 billion"; 2024 "$821.4 billion" | https://www.lsta.org/content/secondary-trading-settlement-study-first-quarter-2026/ |
| Trailing-twelve-month volume passed $1tn in Q1 2026 | CONFIRMED | LSTA 1Q26 study: record quarter of $288bn, and twelve-month volume "surpassed $1 trillion for the first time" | same |
| Q2 2026 fell 18% "as volatility subsided" (LSTA) | UNVERIFIABLE (possible mix-up) | No Q2 2026 LSTA data was found. The only 18% decline located is 3Q25, down 18% to $233B (yet up 11% year over year). Check the 2Q26 LSTA release before printing | https://www.lsta.org/tag/secondary-trading-executive-summary/ |
| Octaura share 0% (Apr 2023), 1% (Apr 2024), 6.4% (Jul 2025), about 7.5-7.7% (H1 2026), vendor-reported | UNVERIFIABLE | Vendor-reported, not fetched | https://news.octaura.com/on-the-blotter-2025-in-review |

**Box 21.3, the repricing machine**

| claim | verdict | evidence / correct figure | source |
|---|---|---|---|
| 2024 repricing volume $756.8bn; US institutional volume including repricings and extensions "almost $1.4 trillion" (William Blair citing PitchBook LCD); about 62% of loans above par at year-end (Guggenheim) | UNVERIFIABLE | Not fetched | n/a |
| Jan 2025 a record $215bn month, repricings 52% of YTD volume (Matrix CMG citing LCD); cycle averaged $52.5bn a month and touched 632 borrowers, 57% of index borrowers (LCD, May 2026) | UNVERIFIABLE | Not fetched | n/a |
| Q2 2025 repricing fell to a multiyear low of $28.5bn after the tariff shock; above-par share of trading 8% in April, 37% in June (LSTA) | UNVERIFIABLE | Not fetched | n/a |
| FY2025 repricing $503.6bn (second to 2024), refinancing $191.8bn; B- new-issue spreads 354 bp in Q4 "the lowest level since the Global Financial Crisis" (William Blair); 58% of loans above par at year-end (Loomis Sayles) | UNVERIFIABLE | Not fetched; Loomis's Q4-2025 letter is free (https://loomissayles.com/wp-content/uploads/2026/01/Loomis-on-Loans-Q4-2025-Final.pdf) | n/a |
| 2026: $108bn of repricings in January; Feb-April only $11.8bn; BB- loans at or above par 13% (end-March), 59% (end-April), 76% (11 May) (PitchBook LCD via Yahoo Finance, 15 May 2026) | UNVERIFIABLE | Not fetched | https://finance.yahoo.com/markets/options/articles/market-enters-post-saas-pocalypse-103621347.html |

**Box 21.4, the retail wrapper moved up the stack**

| claim | verdict | evidence / correct figure | source |
|---|---|---|---|
| Bank-loan mutual funds fell 21% to $71bn, with $23bn of net outflows over 2019-2025 (FEDS Note, Aug 2026) | CONFIRMED | $71bn and 21% confirmed. The $23bn of net outflows (27% of assets) comes from Morningstar Direct data in the note's footnote 6, not from its N-PORT analysis | FEDS Aug 19, 2026 URL above |
| SRLN $5.38bn (Oct 2026); BKLN about $6.8bn (mid-2026, approx.) | UNVERIFIABLE | Fund AUM not fetched | https://www.ssga.com/us/en/intermediary/etfs/state-street-blackstone-senior-loan-etf-srln |
| US CLO ETFs from about $38bn (Sep 2025, Deutsche Bank Flow) to above $50bn (Jul 2026, BofA via Octus); JAAA passed $30bn (13 Aug 2026) | UNVERIFIABLE | Not fetched | https://www.janushenderson.com/en-us/advisor/press-releases/janus-hendersons-aaa-clo-etf-jaaa-the-worlds-largest-clo-etf-surpasses-30-billion-in-assets-under-management/ |
| First European CLO ETF listed in September 2024 | UNVERIFIABLE | Not fetched | n/a |

## Summary

Claims checked: 155 (22 boxes, chapters 15-21). CONFIRMED 71, CORRECTED 6, STALE 2, UNVERIFIABLE 76.

| chapter | claims | CONFIRMED | CORRECTED | STALE | UNVERIFIABLE |
|---|---|---|---|---|---|
| Chapter 15 | 26 | 18 | 3 | 1 | 4 |
| Chapter 16 | 33 | 19 | 0 | 1 | 13 |
| Chapter 17 | 27 | 12 | 0 | 0 | 15 |
| Chapter 18 | 26 | 9 | 3 | 0 | 14 |
| Chapter 19 | 9 | 2 | 0 | 0 | 7 |
| Chapter 20 | 12 | 5 | 0 | 0 | 7 |
| Chapter 21 | 22 | 6 | 0 | 0 | 16 |
| total | 155 | 71 | 6 | 2 | 76 |

Reading the counts: the large UNVERIFIABLE share is mostly a sourcing fact, not a sign of error. The boxes lean on paywalled trade press (The DESK, Octus, Bloomberg Law, 9fin, SCI, IFR), vendor-reported shares (Octaura, MarketAxess monthly releases) and a few filings whose full text was not read inside the call budget. Claims that a free primary source could settle were checked against it: FTC/DOJ HSR reports, the FTC premerger page, the EA 8-K, the Paramount 10-Q, Fed FEDS Notes and the FSR, ICI, SEC, the Fifth Circuit opinion, ABLJ, CLS Blue Sky, Coalition Greenwich, one free The DESK page, LSTA summaries, and the local Man and Moyer PDFs. Where a CONFIRMED verdict carries a caveat, the caveat is in the evidence column.

### CORRECTED and STALE items: exact find/replace pairs

Each FIND string occurs exactly once in the named book_src file (checked 2026-10-18 by exact-string count; no file was edited).

**1. CORRECTED, 15_ch15_event_driven_mna_and_coc.md**

FIND: `"approximately one-fourth" of filings in FY2024 and 31.8% in FY2025`

REPLACE: `"approximately one-fourth" of reported transactions in FY2024 and 31.8% in FY2025`

Source: FY2025 HSR report: "Approximately 31.8% of these transactions"; FY2024: "Approximately one-fourth of these transactions". Filings (4,022; 3,851) are a different count.

**2. CORRECTED, 15_ch15_event_driven_mna_and_coc.md**

FIND: `oscillated between 1.6% and 3.0% of adjusted filings`

REPLACE: `oscillated between 1.6% and 3.0% of adjusted transactions`

Source: FY2025 HSR report, Figure 3 and Appendix A: base is "adjusted transactions".

**3. CORRECTED, 15_ch15_event_driven_mna_and_coc.md**

FIND: `a federal district court vacated it (FTC notice dated February 12, 2026)`

REPLACE: `a federal district court vacated it on February 12, 2026 (FTC notice dated February 13, 2026)`

Source: https://www.ftc.gov/enforcement/premerger-notification-program

**4. STALE, 15_ch15_event_driven_mna_and_coc.md**

FIND: `filing an application of roughly 7,000 pages with the Surface Transportation Board on December 19, 2025 (Union Pacific releases, EDGAR)`

REPLACE: `filing an application of roughly 7,000 pages with the Surface Transportation Board on December 19, 2025, which the Board rejected as incomplete on January 16, 2026; the railroads refiled on April 30, 2026, and on May 28, 2026 the Board found the revised application complete but asked for supplemental information (Surface Transportation Board decisions; Union Pacific releases, EDGAR)`

Source: Secondary sources (fintool, DTN, railmarket); check the STB decision pages before printing. https://fintool.com/news/stb-rejects-up-ns-merger-application

**5. STALE, 16_ch16_post_reorg_equities_and_claims.md**

FIND: `bringing the dotcom customer class (5A) to about 96% and the US customer class (5B) to about 100% cumulative *(per press reports; verify against FTX Recovery Trust notices)*`

REPLACE: `bringing the dotcom customer class (5A) to about 96% and the US customer class (5B) to about 100% cumulative; a fifth distribution of about \$900mm, announced for 31 Jul 2026, takes both classes to about 105% *(per press reports; verify against FTX Recovery Trust notices)*`

Source: https://startupfortune.com/ftx-will-pay-creditors-up-to-120-percent-of-their-claims-next-month/ (reports the Trust's 17 Jul 2026 release; payment itself not confirmed)

**6. CORRECTED, 18_ch18_otc_microstructure_and_avellaneda_stoikov.md**

FIND: `both find that transparency lowered customer trading costs (magnitudes vary by sample and bond type; see the papers)`

REPLACE: `find that transparency helped liquidity, though not uniformly: the first reports lower trading costs once TRACE disseminates prices, and the second a neutral-to-positive effect, with spreads narrowing except for very large trades and very infrequently traded bonds (magnitudes vary by sample and bond type; see the papers)`

Source: https://ideas.repec.org/a/bla/jfinan/v62y2007i3p1421-1451.html ; https://ideas.repec.org/a/oup/rfinst/v20y2007i2p235-273..html

**7. CORRECTED, 18_ch18_otc_microstructure_and_avellaneda_stoikov.md**

FIND: `show the median EUR IG bid–ask falling from 0.0879 to 0.0673 (−23.5%) over the 34 weeks to 2026-08-23`

REPLACE: `show the median EUR IG bid–ask down from 0.0879 to 0.0673 price % of par (−23.5%), comparing the 34 weeks to 2026-08-23 with the same weeks of 2025`

Source: https://www.fi-desk.com/liquidity-improves-amid-1-trillion-surge-in-corporate-debt/

**8. CORRECTED, 18_ch18_otc_microstructure_and_avellaneda_stoikov.md**

FIND: `and 14+ (EM)`

REPLACE: `and 14 (EM, which then widened again and has been above its January level in 21 of the 22 weeks since the peak)`

Source: https://www.fi-desk.com/liquidity-improves-amid-1-trillion-surge-in-corporate-debt/

### UNVERIFIABLE items worth a hedge: suggested find/replace pairs

These are not errors found; they are claims no accessible source supports, or where sources conflict. Apply only if the editor wants the hedge.

**H1. 15_ch15_event_driven_mna_and_coc.md**

FIND: `signed with Netflix on December 4, 2025 before signing with Paramount Skydance`

REPLACE: `signed with Netflix in early December 2025 before signing with Paramount Skydance`

Why: Netflix date not in any accessible source. The same date also appears in the chapter body ("WBD signed with Netflix on December 4, 2025, amended on January 19, 2026"); change both together.

**H2. 16_ch16_post_reorg_equities_and_claims.md**

FIND: `earned 200-trading-day cumulative abnormal returns of 22.8% to 29.6% (medians 16.8% to 22.2%) depending on the benchmark`

REPLACE: `earned large positive excess returns over the first 200 trading days on every benchmark the authors tried (check the exact range in the paper)`

Why: Abstract gives no figures; full text not accessible.

**H3. 16_ch16_post_reorg_equities_and_claims.md**

FIND: `FTX customer claims traded around 15% of face at the start of 2023 and about 35% by September 2023, according to Claims Market pricing cited by Decrypt (22 Sep 2023)`

REPLACE: `Some lower-ranked FTX claims traded at roughly 12 to 15% of face at the start of 2023 and about 35% by September 2023, according to Claims Market pricing (Bloomberg, 21 Sep 2023; Decrypt, 22 Sep 2023)`

Why: Bloomberg reprints say "up from 12 cents"; the Decrypt article was not found.

**H4. 16_ch16_post_reorg_equities_and_claims.md**

FIND: `roughly seven times the money`

REPLACE: `roughly seven to nine times the money`

Why: Follows from the 12 to 15 cent starting range.

**H5. 16_ch16_post_reorg_equities_and_claims.md**

FIND: `The debtors noticed an appeal on 22 Oct 2025; our October 2026 search found no Fifth Circuit ruling.`

REPLACE: `An appeal was reported; we could not confirm its status and found no Fifth Circuit ruling as of October 2026.`

Why: Notice date and appeal status not confirmable.

**H6. 17_ch17_private_credit_public_private_convergence.md**

FIND: `February 18, 2026: OBDC repurchases stock at 86% of book;`

REPLACE: `February 18, 2026: OBDC repurchases stock at a reported 86% of book (check against the OBDC Q4 release);`

Why: 86% not found in the sources reached.

**H7. 17_ch17_private_credit_public_private_convergence.md**

FIND: `May 8, 2026: first quarter on record in which accepted redemptions exceeded inflows (Fed FSR).`

REPLACE: `May 8, 2026: the Fed FSR reports that, for perpetual BDCs, accepted redemptions exceeded inflows in Q1 2026, the first time since those vehicles were created.`

Why: CONFIRMED but the "record" is specific to perpetual BDCs.

**H8. 21_ch21_leveraged_loans_and_clo_microstructure.md**

FIND: `then Q2 2026 fell 18% "as volatility subsided" (LSTA)`

REPLACE: `then Q2 2026 fell back as volatility subsided (LSTA; size of the decline to be checked)`

Why: Only an 18% decline in 3Q25 (to $233B) was found.

### Other notes for the editor (no change required unless desired)

- Ch15, EDGAR portability counts: the per-year counts (1, 4, 8, 11, 2, 3, 5, 5, 10) reproduce exactly, but only when the search is limited to domestic-issuer forms (8-K, 8-K/A, 10-K, 10-Q, 424B*, S-4). Unfiltered, the same phrase returns 85 unique filings for 2018 to 17 Oct 2026. Suggest adding "limited to US domestic-issuer forms" to the box.
- Ch15, WBD: the Paramount deal closed on Oct 6, 2026 (multiple outlets, "just over $31" per share), so "closing October 6, 2026" can read "which closed October 6, 2026". The EA deal was expected to close in Q1 FY27 (Apr-Jun 2026); its closing was not checked.
- Ch15, UP/NS: the $85bn enterprise value and the July 29, 2025 date were not re-sourced in this pass.
- Ch16, FTX: the fifth-distribution figures (105% for 5A and 5B, 103% for general unsecured, about $900mm, cumulative about $11bn against a $16bn estate) come from press coverage of the Trust's 17 Jul 2026 release; the payment itself was not confirmed.
- Ch17, scope: the Fed's "first time since these vehicles were created" is for perpetual BDCs. The 0.74x forward-NAV figure (end-March, 26% discount) and the "nearly a 20% discount" (Apr 16) should state their bases.
- Ch17, units: the Fed's $2.6tn of private-credit AUM (2025:Q4) and BlackRock's $2.2T (March 2025) are different definitions; the Z.1 "$1,493.5B" row includes $35.1B to rest-of-world borrowers.
- Ch18, Hedgeweek: the net-short position is cash bonds only and excludes offsetting derivatives; the squeeze-risk argument should say so.
- Ch21, Moyer: the copyright page reads 2005; "2004" is the Library of Congress call-number year. The book uses "2004" in ch14, ch16 and ch21, so change them together or leave as is.
- Ch21, Eagle Point N-CSR is an indirect source for market-wide loan issuance; LSTA or PitchBook LCD would be better.
- Not checked in this pass (call budget): LATAM $5.4bn backstop; Citi-Apollo $25bn release; the OBDC merger dates (Nov 5-19, 2025); the IMF GFSR redemption-coverage estimate; BlackRock primer; Tradeweb and MarketAxess 10-K figures; all The DESK, Octus, Bloomberg Law, 9fin and SCI items; Meli & Todorova; SCOOS; MarketAxess monthly PT shares; FINRA RN 22-12 effective date; fund-level AUM (LQD, HYG, SRLN, BKLN, JAAA); William Blair, Guggenheim, Loomis and PitchBook LCD loan statistics.
- Web calls: 42 (WebSearch, WebFetch and three EDGAR full-text API requests, including one 404). Local checks, no web call: Man 2022 pp.20 and 41, Man 2023 pp.2 and 3, Moyer pp.322 and 374, and PDFs saved by WebFetch read with pdftotext.

<!-- STATUS: COMPLETE -->
