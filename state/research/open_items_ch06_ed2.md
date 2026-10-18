# Open Fact Items: Chapter 6 (Edition 2, U2 fixer pass, 18 Oct 2026)

*Items whose "CHECK", "secondary, CHECK" or "search summary" flags were removed from book text in `book_src/06_ch06_merton_and_intensity_models.md`. Each was hedged in the text or attributed to a named source. None was re-fetched in this pass except where marked. Sources and dossier tags refer to `state/research/case_carvana_svb_wolfspeed_capital_structure.md` (§2 SVB, §1 Carvana).*

## SVB (§6.4.4, Scene A)

| # | Book text now | Was | Status / what would close it |
| :-- | :-- | :-- | :-- |
| 1 | SIVB 52-week IV floor 39; 30-day IV 167 on 10 Mar, range top 280, attributed to "a vendor's pre-market options report" (Market Rebellion, 10 Mar 2023) and "(same report)" | "(Market Rebellion ...; secondary, CHECK)" ×2 | Dossier [MR] gives the URL; not re-fetched. Close by fetching https://marketrebellion.com/news/pre-market-iv-report-march-10-2023 or OPRA data. |
| 2 | "By Friday afternoon, press reports put dealer offers for that paper somewhere in the high 30s to low 40s." | "(Bloomberg, 13 March 2023, as summarized in search results; secondary, CHECK)" | Dossier: 37-42 at 10 Mar close (Bloomberg/TRACE summary, CHECK). Close with TRACE prints for SIVB holdco CUSIPs, 10 Mar 2023. |
| 3 | "press reports that day put them anywhere from about 40 to the high 40s" (13 Mar) | "reportedly about 47 to 50 cents (Bloomberg ... via search summary; CHECK)" | Dossier: 47-50 (Bloomberg, CHECK) or about 40 (Reuters, CHECK); widened to cover both. Close with TRACE, 13 Mar 2023. |
| 4 | "press reports had distressed buyers paying around 30 cents for some of the paper"; Centerbridge, Davidson Kempner, PIMCO named as creditor-group holders via Debtwire (26 Apr 2023) citing WSJ | Named firms "had bought ... at around 30 cents" (WSJ via Axios; secondary, CHECK) | The named-firm membership and PJT role rest on Debtwire (verified in the U2 verify pass); the "around 30" price is now detached from the named firms. Close the price with the WSJ/Axios articles of 17-18 Mar 2023. |
| 5 | Uninsured-deposit denominator note: Fed 94% of deposits vs 87.5% (US-office uninsured \$151.5bn / total deposits \$173.1bn, computed from the FY2022 10-K); "the Fed's 94% is built from regulatory reports on a different basis" | "86-89% ... appears to mix a different denominator or reporting date (CHECK)" | The \$151.5bn figure is from the dossier (line 209 recommendation), not re-read from the 10-K this pass. Close by reading the 10-K deposit note and the Fed review Table 1 footnote. |
| 6 | "which had about \$209 billion of total assets at year-end (FDIC press release, 10 March 2023)" moved into Beat 4 from the deleted recap | Recap "(approx.; secondary sources)" | **Verified this pass** by WebFetch of https://www.fdic.gov/news/press-releases/2023/pr23016.html ("approximately \$209.0 billion in total assets"; deposits about \$175.4bn). |

## Carvana (§6.10.1, Scene B)

| # | Book text now | Was | Status / what would close it |
| :-- | :-- | :-- | :-- |
| 7 | Scene label: "Equity closes are a vendor's daily bars, restated to as-traded prices and not checked against exchange records, so treat the cents as approximate" | "(CHECK decimals against exchange data)" | Close against exchange closes for 10 Aug 2021, 27/30 Dec 2022, 31 Mar, 31 May, 19 Jul, 29 Dec 2023, 31 Dec 2024. |
| 8 | \$370.10, \$3.72, \$9.79, \$12.92, \$55.80, \$4.74, \$52.94, \$203.36 each labelled "(vendor data)" | "(vendor data; CHECK)" ×5 | As item 7. |
| 9 | Advisers (Moelis and Kirkland for Carvana; PJT and White & Case for the group) cited to the 19 Jul 2023 8-K Ex. 99.1 | "(...; CHECK role language)" | The U2 verify pass fetched the 19 Jul release and confirmed the names and sides; flag removed. Exact role wording ("financial advisor", "legal counsel") not re-quoted. |

## Not changed in this pass (noted for the next one)

- Cast bible !C1: Ch 6's cold open is dated Thu 9 Mar 2023 and is not yet labelled as a replay; Ch 6 §6.8.1 still says "Theo, who was in college in 2009" and "fifteen years" (cast bible canon: "in middle school in 2009", "eighteen"). Outside this fix list.
- S&P Market Signal PD figures (§6.4.4 "What the structural model saw") remain hedged as "as reported by the vendor in a blog post; figures not independently verified".

- Template paragraphs not on the fix list (lesson 4): §6.5.2 "When to reach for a barrier, and when it breaks" and §6.6.3 "When to reach for intensities, and when they break" ("They break in two ways... The first... The second... The first check a seasoned practitioner makes"); the §6.11 listing explanations open six paragraphs with "Use it for / Use the..." and "The edge case that bites" (lesson 12). Recast as scenes in a later pass; the Finder table now carries the rules.
- §6.10.1 Carvana still has a recap after Beat 5 ("Here are the facts again, compressed" + **The facts.**), the same pattern P1 removed from SVB; §6.9.3 First Brands answers its decision point in the same paragraph that poses it (lesson 9).
- Cast bible !C7: §6.5.1 has Kaz "reading a revolver term sheet for the first time" and misreading "springing lien" as seasonal; canon makes that a Ch 3 first, so Ch 6 should be a callback Kaz pre-empts.

<!-- STATUS: COMPLETE -->
