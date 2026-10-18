# Verification report, Edition 2: Chapter 25 (NLP for Credit Agreements, Indentures & PACER Dockets)

Chapter: `book_src/25_ch25_nlp_pacer_and_covenant_scraping.md` (about 30.2k words after the writer; pre-revision text from `9ac1c37`). Revision log was marked COMPLETE. Verifier made 9 small Edits (listed under "Fixed"). Web calls used: 15 of 15.

## Check 1. Nothing removed

Method: python3 comparison of pre and post text (headings, `$$` blocks, Source Extractions, Trend Watches, boxes, exercises, listing links, Resource Graph lines, then a sentence-level sweep of every pre section).

| Item | Pre | Post | Result |
| :--- | ---: | ---: | :--- |
| Headings (exact) | 38 | 46 | All 38 present; 8 new (6 "The Full Derivation" subsections: nilpotence, contraction, flow-cut, swapped token, intensity MLE, IC exchange rate; 2 "Long Scene"). |
| Display-math blocks | 20 | 24 | Every pre block present; two differ only by trailing punctuation (comma to period) because the proofs moved. 4 new blocks (adjacency matrices, K slope, xfer shares, etc.). |
| `[SOURCE EXTRACTION]` blocks | 11 | 11 | 10 verbatim; Dynkin p.621 quote verbatim, annotation intentionally rewritten to point back to Ines's house rule (brief item 20). |
| Trend Watch boxes | 3 | 4 | All 3 verbatim; 1 new (public side's information set), placed before the existing docket-access Trend Watch. |
| Ways This Blows Up, Desk Myth, Hughes Docket Diary | 2, 1, 1 | 2, 1, 1 | All verbatim. |
| Exercises 1-6 with answers | 6 | 6 | Section byte-identical. |
| The Spec You Hand the Robot (```text block) | 1 | 1 | Byte-identical. |
| Desk Debrief bullets | 8 | 8 | All identical; Finder table added above them (10 rows). |
| Appendix F links `#code-25-1`..`25-9` | 9 | 9 (19 mentions) | All nine present; the nine `<!-- EXPLAIN -->` stubs are replaced by filled explanations (U1 work), each ending with the Appendix F link. |
| Resource Graph | 30 items | 35 items | All papers, URLs and datasets unchanged. Three generic podcast/newsletter lines were upgraded by the earlier resgraph step (`...resgraph.md`); not a writer deletion. |
| Moyer cites (pp.86, 166, 167, 168, 174, 220, 285, 286, 287, 329), Man p.32, Paleologo p.156 | present | present | OK. |

Sentence-level sweep: every pre sentence not found verbatim was traced to its new home (Windstream Facts into the cold open and §25.5.2; J.Crew Facts into the Long Scene; "Four things a desk takes from this" into the Serta grading; plumbing bullets into the "week the feed was built"; spec consequences into two sentences). Nothing lost. Moved derivations are all under "The Full Derivation" headings, none deleted.

## Check 2. Facts (new claims about real events, firms, people, dates, amounts)

Sources: the brief's dossiers (`case_manufactured_credit_events.md`, `case_courts_as_regime_variables.md`, `case_lmt_autopsies_us_2020_2026.md`, `perspectives_buyside_credit_managers.md`, `trend_re_default_and_recovery_dataset.md`, `case_carvana_svb_wolfspeed_capital_structure.md`), cross-chapter text (Ch 3, 5, 13, 14, 24), and 15 web calls.

Verified (dossier or primary/secondary source):
- Windstream cold open: spin 24 Apr 2015, notice of default 21 Sep 2017, two DC votes 15 to 0 (4 Oct, 21 Dec 2017), acceleration 7 Dec 2017, about \$465mm Original Notes with roughly 64% Aurelius, \$553.7mm Additional Notes dated 6 Nov 2017, Furman ruling Friday 15 Feb 2019 (Doc. 245, 55 pp.), Chapter 11 on 25 Feb 2019 (ten days), appeals moot 2021-06-23, five quarterly swap maturities in the gap, backdating refused, contracts alive on 25 Feb 2019 paid. Web: ruling for Aurelius, \$310.5mm plus interest from 23 Jul 2018, acceleration valid, Aurelius sought a declaration that the exchange notes were not permissible "additional notes" (all match). Day-of-week arithmetic checked (15 Feb 2019 Friday; 12 Oct 2017 Thursday; 30 Oct 2026 Friday).
- J.Crew Long Scene: 12 Oct 2016 designation; 5 Dec 2016 IP transfer into J.Crew Domestic Brand, LLC; 1 Feb 2017 press release and suit against Wilmington Savings Fund Society, with the "fully complied" language (web: press release text); 10-Q for the quarter ended 29 Apr 2017 **filed 12 Jun 2017** (EDGAR index) and its terms (up to \$190mm preferred, up to 15% of common, up to \$250mm IP-secured notes, \$150mm term-loan repurchase, \$30mm add-on; web); exchange closed 13 Jul 2017 (matches Ch 13); Chapter 11 on 4 May 2020, E.D. Va. No. 20-32181 (web: In re Chinos Holdings); Carvana ADESA designation (dossier, Ch 5). \$150mm and \$100mm baskets and \$250mm IP value are Torys and King & Spalding as in the pre text.
- Serta Long Scene: petition 23 Jan 2023 No. 23-90020; uptier closed 22 Jun 2020; lender names and \$200mm / \$1.2bn / about \$875mm terms (Fifth Circuit opinion as in dossier; \$734mm reconciliation points to Ch 5 §5.6.2, which exists); Docs 69, 75, 273, 289, 311, 389, 1116 and the adversary 4:23-ap-09001 and the 22 May 2023 North Star order (all from the pre text's table and paragraph); emergence 29 Jun 2023; March 2023 ruling and June plan with indemnity (Ch 14: 28 Mar 2023 partial summary judgment, plan confirmed 14 Jun 2023); Fifth Circuit holding quote 31 Dec 2024 (dossier verbatim); 23 months after Doc. 75 checked.
- Other: Sound Point order 26 Aug 2024, \$1.8mm (web, SEC settlement coverage); Wolfspeed 8-K of 23 Jun 2025, exhibit 99.2 (matches Ch 3 §3.6.3); 11 U.S.C. §1102(a)(1) and (b)(1) wording (red-pen log verified on Cornell LII); Kundu CCC quote (dossier verbatim); Buccola-Nini 600+ agreements, 40% (Ch 13 Trend Watch); PB-08 terms (Level 3 3.875% first-lien 2029s at 73, \$15mm long / \$10mm short, 150 bp, cut-off 10 Nov 2023) match `state/rv_pair_book.md` and Ch 13 §13.5.
- Arithmetic re-done: adjacency powers; fixed-point sequence 80, 70, 67.5, 66.9, 66.7; hockey stick (214.3 kink, 4.85 slope at 250 to 251); builder \$65mm versus \$10mm; pipes 40/60/30; cosine 13/14 and 4.4e-7; 21/60 = 35% and 21/70 = 30%; exponential 1 - e^(-31/40) = 54%; Youden box (45 of 50, about 47.5 false flags, J = 0.85, 0.639, 0.49); PB-08 screen 0.693 and 2.1x breadth; four workers x (2+8) = 40; 8 days from Doc. 1116 to emergence.

Fixed (9 Edits in the chapter, grouped into 7 items):
1. **Ares Capital seat box (§25.3.2): removed the direct quote and the speaker attribution.** The dossier and Ch 17 attribute "We will walk away from transactions based on documentation terms" to Jim Miller. The MarketBeat transcript of the 4 Feb 2026 call (fetched twice) shows the analyst question from RBC's Kenneth Lee on loosening terms and an answer by CEO Kort Schnabel containing "a heightened focus on documentation terms" and, as rendered, "We won't walk away from transactions based on documentation terms." Speaker and wording conflict, so the box now says "Ares Capital's management" and quotes only the phrase both sources share.
2. Serta beat one: "134 weeks" corrected to **135 weeks** (945 days from 22 Jun 2020 to 23 Jan 2023).
3. Serta beat two: the RECAP "not available" status was a fact about when the chapter's query ran, not about 24 Jan 2023; reworded to "when this chapter's query ran".
4. Windstream cards: "because the supplemental indenture called them that" (unverified detail about a real instrument) changed to "the issuer's own paperwork".
5. J.Crew beat two: "public 1 February 2017" and "the company's own public statement" changed to the company's press release of 1 Feb 2017; "furnished on an 8-K the next day" changed to "furnished on an 8-K" (next-day date unverified).
6. J.Crew: "By 1 February the J.Crew route was public" changed to "the transfer was public" (the third-provision structure was explained later by law firms).
7. J.Crew, Ines and Mags lines (two Edits): statements that real lenders left the page "unread" and "never read" it were an unsupported claim about real parties; reworded to what is supportable (the lenders' own later word "secret" suggests few had noticed; "a page that was there all along"; "agreement those lenders signed" changed to "lent under").

No real person has invented dialogue or quotes after these edits: Judge Furman, Aurelius, and the lenders appear only in narrated facts; all dialogue is by the fictional cast (Ines, Theo, Mags, Kaz, Paloma, Rhea). Every scene carries its italic fiction label (cold open, Halyard pivot, §25.2.4 composite, J.Crew, Windstream cards, §25.6.1, §25.6.2 vignette, Serta, PB-08 box). Dealer seat box keeps the firm unnamed and attributes the characterization to the dossier.

## Check 3. Hygiene

- Code fences: exactly one, the ```text Spec block (lines 903 to 923). No other code blocks.
- Math: 48 `$$` markers (even); no line with an odd number of unescaped inline `$` outside the ```text block (the `$mm` there is literal inside the fence).
- Currency in prose escaped as `\$` throughout (regex sweep for `$` followed by an amount and mm/bn/million found none unescaped).
- No line of `---` anywhere in the chapter; table separator rows only.
- No `CHECK`, `TODO` or "as summarized in search results" markers in text.
- Last line is `<!-- STATUS: COMPLETE -->`.

## What remains doubtful

- **Ares quote, other places.** `state/research/perspectives_buyside_credit_managers.md` lines 48 and 52 and **Chapter 17, line 101** still carry "We will walk away from transactions based on documentation terms" attributed to Jim Miller. The transcript I could read disagrees on both the speaker and the wording ("won't"). Someone should read the full Q&A of the 4 Feb 2026 call and fix Ch 17 and the dossier. Out of scope here, not edited.
- **Marathon Asset Management (30 Sep 2024, \$1.5mm)** in the new Trend Watch is carried from Ch 3 §3.6.3; the web search confirmed Sound Point but returned nothing on Marathon. **Skadden recoveries** (participants 100% and about 75%, non-participants 0.6 to 2.4%) are carried from the dossier; a web search could not find the Skadden piece.
- **Chapter 13 versus Chapter 25 on J.Crew.** Ch 13's Docket Diary says "Dec 5, 2016: J.Crew discloses...". Ch 25 now says the transfer was on 5 Dec 2016 and the company's press release was 1 Feb 2017. The press release itself gives the 5 Dec date; whether anything public appeared between those dates (the Q3 10-Q, filed in November 2016, cannot have carried it) was not established. Ch 13's wording may be loose.
- **7 Sep 2017 amended complaint ("secret trapdoor", Locke Lord)** is the pre-revision claim. The Locke Lord page now redirects to a dead Troutman URL, and a search found only the Eaton Vance and Highland suit in New York Supreme Court, Commercial Division, not the amended-complaint date. Left as is, with its attribution.
- **Windstream details from the dossier** (6 Nov 2017 issue date of the \$553.7mm, \$465mm and 64%, the "trustee went to court on 12 October" framing from the case caption) rest on the DC record and the CourtListener caption; the web search did not confirm the 6 Nov date or who filed first.
- **CourtListener API tiers** are stated "as fetched 2026-10-17" with the 7 May 2026 membership hedge; not re-fetched. The Ch 11 case number for J.Crew was Wikipedia-sourced in the dossier and is now confirmed by the web.
- Cross-chapter section pointers checked and exist: §1.3.3, §3.4.3, §3.6.3, §3.7, §5.6.2, §6.1.4, §13.2.1, §13.3.1, §13.5, §13.6, §14.8.1, §24.8.3. The five new figures named in the brief (timeline, blocking threshold, bucket, Youden, hockey stick) are U4 work and are not in the chapter yet.

<!-- STATUS: COMPLETE -->
