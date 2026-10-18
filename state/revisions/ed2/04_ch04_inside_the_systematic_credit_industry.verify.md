# Verification report (Edition 2): Chapter 4, Inside the Systematic Credit Industry

Verifier pass, 2026-10-18. Chapter: `book_src/04_ch04_inside_the_systematic_credit_industry.md`. Pre-revision text: commit 9ac1c37 (591 lines, 13.7k words); revised text 1,071 lines, 37.0k words. Revision log was COMPLETE before this pass. Web calls used: 7 of 15.

## 1. Nothing removed (python3 compare of pre vs post)

| Item | Pre | Post | Result |
| :-- | :-- | :-- | :-- |
| Headings | 26 | 45 | None missing; 19 new (Full Derivation, When-it-breaks, case-scene and shop-life subsections) |
| `$$` delimiters (display blocks) | 42 (21) | 44 (22) | All 21 original blocks present; one differs only by trailing punctuation (period to comma, because a clause now follows); one new block (truncated-normal derivation, moved into a Full Derivation) |
| Equations (4.1) to (4.7) | 7 tags | 7 tags | All present |
| SOURCE EXTRACTION boxes | 13 mentions | 13 | Nine annotated extractions intact, plus the four repeated references |
| Trend Watch boxes | 2 | 3 mentions | Both boxes intact; §4.2 box augmented with the Man Group $14.7bn to $42.7bn line |
| Exercises | 6 | 6 | Identical text (diffed) |
| Resource Graph | 1 | 1 | Identical text (diffed) |
| Appendix F links `#code-4-1` to `#code-4-4` | 4 | 4 | All four present. The "Code Companion" blockquotes were already converted to prose walkthroughs with links in the earlier code-explanation pass (HEAD 6acb12e, before the revision), so this is not a revision loss |
| Desk Myth box, Specification for AI Implementation, Spec You Hand the Robot, Desk Debrief bullets | present | present | Intact |
| Worked numbers (960; 0.46/0.64; 230/180bp; 62.5/900/15,000; 0.027 and 11bp; 11.5%/1.4%; 6.97-2.55-0.37-0.49=3.56; 2.66/1.78/0.88/1.89/1.26; $1.85bn/40bp/$4.2bn/$134mm; 53%/98%; 2.1bp/0.91; 77%) | | | All present |
| Running gags (USB stick, IDO or it didn't happen, fulcrum/torque, Mags "back in my day", ROBO) | | | All present |

Sentence-level diff of pre against post found no deleted content beyond intended rewrites: learning-objective bullets became a paragraph (allowed by the brief), the three "places this goes wrong" and three numbered capacity readings became prose scenes, derivations moved under "The Full Derivation" headings. Table rows changed only where a CHECK marker was replaced by a hedge (see §2). Nothing needed restoring.

## 2. Facts: new claims checked

Sources: pdf_pages text of Man 2022 (p.17, 19, 31), Man 2023 (p.3 to 5), BlackRock p.3, Dynkin p.207 and p.711, Blackstone p.1 to 2, Bohn-Stein p.123; dossiers `trend_systematic_credit_industry`, `perspectives_buyside_credit_managers`, `perspectives_dealers_and_systematic_shops`, `rv_pod_platforms_and_risk`, `papers_factor_replication_crisis_and_bond_data`, `life_quant_shop_daily_life`, `trend_electronification_pt_etf_liquidity`; web (primary where possible).

Verified, no change:
- Man 2022 quotes at p.19 and p.31; Man 2023 quotes at p.3 and p.5 (all verbatim); BlackRock p.3 quotes; Dynkin p.207 quote; Blackstone p.1 to 2 quotes; Dynkin cost drift 1.15% (2007 to 2012) and 0.64% (2013 to 2019) on p.711.
- Ares/BlueCove: 29 to 30 Oct 2025 agreement, $1.8bn (2023) to $5.5bn (30 Sep 2025), about 60 staff, minority stake since 2023, "increased interest in systematic credit", Business Wire release "Ares Completes Acquisition of BlueCove to Launch Systematic Credit Strategy" (web search confirmed the exact title and early February 2026 date; the open-item row is resolved).
- Miller (4 Feb 2026) and Rowan (9 Feb 2026) quotes match the dossier transcript table word for word. No real person has invented dialogue: the only direct speech from real people is these sourced quotes, the Swiss Life and Vanguard panel quotes (unnamed traders, verbatim from the dossier), and Mercer's sentence.
- Mercer fee waterfall arithmetic recomputed: 20 gross gives PM 3.4, fixed 4, fund 2.52, client 10.08; 6 gross gives about 1.1; the figure series 0.48/3.68/6.88/10.08/13.28 recomputed and correct. Cambridge Associates pass-through 0.87% to 12.99%, mean 5.93% (dossier, primary). Dov Adler's pair ($60mm Kestrel 6s 2030, $39mm Halvorsen 7.25s 2029, $400mm allocation) matches Chapter 1-B.
- DRR 2026 facts (269 months Aug 2002 to Dec 2024, 52,656 bonds, 432 specifications, 65 at t > 1.96, 26 FDR survivors, 25 within-firm, bond age the lone single-sort survivor, non-standard error 0.35% vs 0.33%, LIB +/-0.50% gives 1.00%, signal gap 1 to 10 days, 35-point bounce filter, 5-day VWAP month price, 144A from June 2014, pipeline v4.2.1 Sept 2026, 5 hours and 5 GB): all match the dossier. Case-study composite (Kaz's panel, 20% fewer bonds, the 3.1 to 0.9) is labeled fictional.
- Fed FEDS Note, 21 March 2025 (Carlino, Foley-Fisher, Heinrich, Verani): title, authors, "$4.1 trillion, accounting for about 72 percent of the industry", "a record $212 billion" all confirmed on federalreserve.gov.
- Balyasny hire (Daniel Chen, ex-BlackRock, Hedgeweek 20 Aug 2026) and its quoted sentence confirmed verbatim.
- PT modifier (15 May 2023, FINRA RN 22-12, at least ten unique issues at a single basket price), Coalition Greenwich 10% non-bank share (Jan 2025), Vanguard 70% automated, recovery weeks 4/6/8/13 (The DESK, 1 Oct 2026), FILS Europe quotes (14 to 15 Oct 2026), Athene $292bn, Apollo "dislocation-driven", Moody's buying KMV in 2002, DCI 2004 founding and Blackstone's May 2021 rationale (carried from pre-text): consistent with dossiers and pdf pages.
- Labeled fictional composites: retailer creditors, packaging-company CUSIPs, distributor, Mags's 1998 and EDF stories, Ines's June 2022 hand history, Dov Adler, pitch book, Kaz's desk. All carry a "fictional" label at or near their start.

Wrong or unsupported, fixed in the chapter:
1. Millennium (Hedgeweek, 2 Jun 2025) hired two people that day (Brevan Howard credit-index trader, Laurion partner); the LMR former US head of credit was an earlier hire. Sentence corrected.
2. Todorov (BIS QR, Mar 2021): tracking error above 200bp was "for some funds in March to April 2020", and it is a gap to benchmark, not price to NAV. Sentence corrected.
3. Citadel Securities 14.2% share: source says IG credit block risk transfer; the added word "US" was unsupported. Removed.
4. "Since about 2020 the bank desks have had company": no support. Changed to "In recent years".
5. Dealer box said no public statement of Jefferies's view exists; the dealers dossier holds Jefferies heads-of-credit-trading statements. Reworded to "this box attributes no view to either" (open-items row updated).
6. Man guard rails/autopilot/GPS cited as p.15 to 18; it is p.17 only. Fixed.
7. Dynkin: the 5% ownership rule is stated on p.207 itself, not "the next page". Fixed.
8. Surviving momentum: the audit's survivors include both systematic (fitted) and residual 12-1 momentum (EW, within-firm), not residual only. Two sentences corrected.
9. Mags's remark said the original process "decided in advance not to learn about default"; that implies intent, which the brief forbids. Reworded to a neutral statement, and the replication finding is now stated as "among other things the after-the-fact filtering of extreme losses".
10. "Each pointed to insurance clients when explaining why" (Blackstone/DCI and Ares): the reported DCI rationale was capacity and data, not insurance. Narrowed to "both sell to insurance clients, which Ares said outright".
11. Theo's five reasons: "best supported" yield claim now cites BlackRock p.3 ("all in yields looked attractive in corporate credit"); "the first participants to step back" softened to "among the first".
12. Smaller edits: dropped unverifiable "fetched 18 October 2026" (Apollo page) and "checked 17 October 2026" (stockanalysis); IGEB/HYDB figures stay "as of the 16 October 2026 close" per dossier; Fed quote now says general account assets at the end of 2023; Ines's "spread beta costs a few basis points" widened to a range (ETFs cost tens of bp); "increasingly attached" changed to "often attached".

## 3. Hygiene

- Code fences: none (no ```text diagrams either).
- Display math: 42 `$$` lines, even, braces and \left/\right balanced in every block. Inline `$` parity even on every line; no inline-math span contains prose.
- Currency: every dollar amount is `\$`; no unescaped currency found.
- No `---` line anywhere. No CHECK markers remain in text (all hedged; logged in `state/open_items_ed2.md`).
- Last line of the chapter is `<!-- STATUS: COMPLETE -->`.

## Remaining doubts

- Blackstone "over $40 billion": undated in the source; chapter says so openly (open item).
- Cboe IBIG/IBHY block volume: from a sponsored The DESK article; Cboe primary data not opened (open item).
- Capacity "Silent (none found)" cells for BlackRock, Robeco, Acadian: negative claim, absence of evidence only.
- The pod scene ends by pointing to Chapter 28 for the pay, netting and capacity arithmetic "which proves what Ines has just asserted". Chapter 28 has no such section yet (rv_thread row T12 assigns it). Logged as an open item for the Chapter 28 reviser; if not delivered, soften the sentence.
- Man Group $14.7bn to $42.7bn and Citadel's 14.2%: taken from trade-press dossier rows (Alternative Credit Investor, The DESK), primary pages not opened. The Hedgeweek Millennium page also did not display the exact "Brevan Howard CDS and CMBS index" wording the dossier records; the chapter says "credit-index trader", matching the article.
- Ares-Miller framing ("a firm that already had the second seat bought the first") is interpretation, not a sourced claim.
- Apollo "fetched" dates and the IGEB/HYDB aggregator figures are secondary-source numbers.

<!-- STATUS: COMPLETE -->
