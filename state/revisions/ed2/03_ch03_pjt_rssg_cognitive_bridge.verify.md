# Verification Report, Edition 2: Chapter 3 (PJT RSSG Cognitive Bridge)

Chapter: `book_src/03_ch03_pjt_rssg_cognitive_bridge.md`. Pre-revision text: commit `9ac1c37`. Revision log was COMPLETE. Web calls used: 15 of 15 (13 WebFetch of SEC, Debtwire, Bloomberg-via-Accounting Today, American Banker, Financier Worldwide and Wolfspeed pages, one EDGAR filing list, one WebSearch). The rest was checked against the dossiers the brief names and by re-running the Appendix F listings.

## 1. Nothing removed: PASS

Script comparison of pre and post (headings, `$$` blocks, boxes, exercises, links, Resource Graph items, then every pre sentence):

| Item | Pre | Post |
| :--- | :--- | :--- |
| Headings | 32 | 41 (all 32 kept; 9 new Full Derivation, Units, vignette, when-works, SVB scene headings) |
| Display-math blocks | 29 | 30 (all 29 present verbatim; one added: the symmetric GM bid) |
| SOURCE EXTRACTION boxes | 9 | 9 |
| Trend Watch boxes | 3 | 3 |
| Poker Table, Ways This Blows Up, Docket Diary | 2, 1, 1 | 2, 1, 1 |
| Exercises with answer checks | 6 | 6 |
| Appendix F links (`#code-3-1` to `#code-3-6`) | 6 | 6 |
| Resource Graph items (4 bullets) | 4 | 4 (Podcasts bullet extended; nothing replaced) |
| URLs | all kept | 4 added (9fin x2, Signals and Threads x2) |

Pre sentences not verbatim in post (48) were all intended conversions, each content-checked: the seven-bullet feature list (every citation kept: Easley and O'Hara, Pinter-Wang-Zou, Wei and Zhou, Di Maggio-Kermani-Song, PRS Chapter 13), the radiologist paragraph (replaced by the SVB scene, brief item 15), the "three columns" paragraph (decay horizon, refresh, who else has it all kept), the four-step LMT anatomy (all four steps and the 50%/two-thirds/sacred-rights thresholds kept as Saks events), the CUSUM lead-in (moved into the Full Derivation), the "Chapter 25" to "Chapter 26" fix, and the six Code Companion stubs plus `<!-- EXPLAIN -->` markers (replaced by explanations per directive 11/U1, with the Appendix F links kept). Nothing needed restoring.

## 2. Facts

I read all new text (about 20,000 new words, 927 new sentences). Numbers and arithmetic were recomputed (Moyer 375 and 19.4; mixture 525.7 and 93%; coin jar 0.85; IDO split 0.48 and 5.5; crossover 4.1 days; SVB drill 41/27/45, 1.88 points, bid 39; Serta 2.86 and 627mm/70c; CUSUM e^4 and delay 8; 69/57 puzzle p about 0.55, R about 36). All correct. Appendix F listings 3.1 to 3.6 were run: 54% fills, -1.29 and +1.53 points, 36% with shading, pi-hat 0.64, bid 81.07, MSE 3307 vs 410, 1,034bp, ARL 304, delay 8.7 days. All match the new explanations.

Verified against primary or dossier sources:
- Debtwire 26 Apr 2023 (fetched): 69 and 57 on 3.5% 2025s ($350mm) and 1.8% 2031s ($500mm), MarketAxess; same class; WaMu 2012 "repaid bondholders at par with interest"; Charter 2009 reinstatement; FDIC froze the $2bn deposit; "a bunch of hedge funds bought these bonds in the 30s" (a trader); PIMCO, Centerbridge, Davidson Kempner formed a group and retained PJT (via WSJ).
- SVB 8-Ks (EDGAR): 7 filings in March 2023; 14 Mar Item 2.01 ($23.97bn to $21.45bn, Goldman, signed by Kosturos as CRO); 13 Mar Item 8.01 (five named directors, Centerview, Sullivan & Cromwell, A&M, "approximately $3 billion of funded debt," "recourse only to the Company") and Item 5.02 (Kosturos); 17 Mar Items 1.03, 3.01, 5.02 (No. 23-10367 SDNY; Nasdaq suspension 28 Mar); 22 Mar Item 2.04 (seven tranches, 2010 indenture, 1.800% Oct 2026 $650mm).
- 7 Nov 2024 release ex 99.3: PJT Partners and Davis Polk advise the "Ad Hoc Group of Senior Noteholders."
- Bloomberg via Accounting Today, 2 Jul 2024: 1.8% 2026s up as much as 2.625 to 63.625 (Trace); IRS claim $649mm to $43mm.
- American Banker 9 Sep 2026: Judge Freeman, 12-day trial, ruling 28 Aug, $1.71bn.
- Wolfspeed 23 Jun 2025 8-K: RSA 22 Jun, more than 97% secured, more than 67% converts, Renesas a party, milestones (petition by 1 Jul, 75 days, four months), cleansing material as ex 99.2.
- Dossiers: HLLSV 23% vs 11%, Baldauf-Mollner, Tradeweb 0.1-0.3bp (vendor, not peer-reviewed); Mannes and Friedberg quotes, FINRA 6730, SR 11-7 override quote; Apollo ladder quote and LTV bands; Serta 2016 loans, s.2.18/9.02(b)/9.05(g), 52.6/47.4, 26%/61%, "Open Market Purchase and Cashless Exchange Agreement," party names; 9fin episode titles and dates.

### Fixed in the chapter (27 small edits)

1. **13 March filings.** Chapter said one 8-K carried the committee and the CRO. EDGAR shows two: Item 8.01 (committee) and Item 5.02 (Kosturos). Rewrote the scene paragraph and the 3.4.1 narrative. The stitched quote ("all alternatives for addressing...") is now limited to fragments the 8-K contains.
2. **3.4.1 item sequence.** Chapter said the first flaggable filing was 13 Mar and that Item 3.01 "arrived weeks after the cushion had gone." Actually the 10 Mar 8-K carried Item 1.03 (receivership), and Item 3.01 was filed 17 Mar together with Item 1.03. Rewritten ("a week after the cushion had gone").
3. **Drill timing.** The Item 5.02 filing was accepted at 4:59 p.m. on the Monday, not before 9:02 a.m.; the "illustrative" note now says so.
4. **Group formation timing.** "Formed a group ahead of the filing" (two places), "in the week of the drill" and "before the week was out" went beyond Debtwire. Now "formed a group and retained PJT," "within weeks," "reported to be organising."
5. **Fed review "six weeks later"** is seven (9 Mar to 28 Apr). "$100bn ... roughly 85% of the deposit base" was arithmetically wrong as phrased; now "together would have taken most of the $173bn."
6. **Parent-only balance sheet.** Removed the unverified $896mm and $491mm; replaced with the verified remainder (19,679 - 15,456 = about $4.2bn, of which $2,258mm cash). Removed a quotation attributed to the 10-K risk factors that could not be checked (now a paraphrase).
7. **Merton line** now states the inputs the dossier computed (asset value about $19bn, vol 33%, 4.5% rate).
8. **Bloomberg 1 Jul 2024.** The article is dated 2 Jul and its trade date is unclear; now "early July 2024." The "at least 40%" sentence is garbled in the copy fetched, so it is hedged. "Four years of lawyers" is now "years."
9. **Mags on WaMu:** "senior bondholders" is now "bondholders" (Debtwire says bondholders).
10. **Saks.** Removed "S&P moved it to selective default on 7 January 2026" (single blog source) and "about $126mm" (search found "more than $100 million" due 30 Dec). Removed "crammed down a class of old notes that voted against it" (dossier CHECK; Financier Worldwide does not say it) and the unconfirmed "5 June" date ("early June 2026"; debt $3.4bn to $1.2bn and equity wiped out are confirmed). The $51mm outside figure is now "reported."
11. **Wolfspeed.** The "substantial doubt about our ability" quote could not be tied to ex 99.2; replaced with the phrase the 8-K itself contains.
12. **Serta liquidity.** 29% to 43% of $186mm is $54mm to $80mm, not $62mm to $94mm. The two sets of numbers come from different bases in the opinion summary; reworded and flagged as not reconciled.
13. **Insurer seat.** HLLSV paraphrase tightened to the dossier ("take 23% of its trades when they are quoting the bond").
14. **Podcasts.** Mannes is described as "not talking about credit" (dossier says commodities, not "equities"); Friedberg's alert tool is now "a tool that engineers built"; Resource Graph "most honest public account" softened.
15. **Cross-reference.** The first appearance of the half-sigma-squared is Chapter 5 section 5.2.3 (lognormal, with its own Math, Gently box), not section 5.3.2. Fixed.
16. **Continuity.** "On your first Friday" (two places) conflicted with the cold open's three weeks; now "after Brambleworth" and "on the Brambleworth Friday." "In the four business days after its bank was seized" became "in the days around the seizure."

Real persons and dialogue: no invented words for any real person or firm. Quotes of Mannes and Friedberg are fragments from the transcripts in the dossier; Kosturos, the five directors, Barclays, PJT, Centerview and Apollo appear only as filing facts or quoted public text. Fictional composites are labeled (Tuesday vignette, spreadsheet-as-feature meeting, wall-crossing routine, SVB drill, Serta blotter, the 19 June 2020 RFQ).

## 3. Hygiene: PASS

No fenced code blocks anywhere; 60 `$$` markers (even); no unbalanced inline `$`; no unescaped currency; no `---` line; zero `<!-- EXPLAIN -->` stubs left; the last line of the chapter is `<!-- STATUS: COMPLETE -->` (once).

## What remains doubtful

- The 10 Mar 8-K sentence "The Company is no longer the parent company of the Bank" was taken from the brief and not re-fetched (the filing's items, 1.03 and 8.01, are confirmed).
- From dossier summaries, not re-opened: the 8 Mar raise split ($1.25bn / $500mm / $500mm) and $1.8bn after-tax loss; the Fed review's $40bn and more than $100bn outflow figures and the "told supervisors" attribution; the 10-K deposits, 94% uninsured and FHLB figures; the parent-only cash, bank investment and debt figures.
- Plan terms for senior noteholders (stock plus trust units) and the 2 Aug 2024 confirmation date come from the dossier's reading of the Nov 2024 8-K; the Randles piece said the hearing was "later that month" (July). The 7 Nov release exhibit does not itself state the consideration.
- Saks exchange terms, the 91.9% pre-commitment and 98% tender figures come from company releases through the dossier; the $51mm and the 47.5 price are Debtwire and blog sourced.
- Serta remand testimony (Barclays "lead market maker," $186mm, 29% to 43%) comes from the advisor brief's reading of the opinion and Mayer Brown; not reconciled.
- Kaz's gloss on the 12 Mar joint statement (debtholders "explicitly" unprotected) relies on the statement's well-known line about "certain unsecured debtholders," which was not fetched.
- Mags's "everybody said the holdco bonds were zero" is colloquial, not sourced.
- The 8.01 committee filing's acceptance time was not retrieved.
- Narrative timeline: the SVB drill weekend and the Brambleworth lender-call Monday coincide, while the Tuesday vignette is "third Tuesday after the hand" and the Serta scene is "fifth week." Consistent enough, but a continuity read is advisable.
- HLLSV, Baldauf-Mollner and the Tradeweb paper were checked against the dossier summaries, not the papers.

<!-- STATUS: COMPLETE -->
