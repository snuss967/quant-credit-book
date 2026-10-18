# Verification Report, Edition 2: Chapter 6 (Merton and intensity models)

Chapter: `book_src/06_ch06_merton_and_intensity_models.md`. Pre-revision text: commit 9ac1c37 (14,249 words by wc; revised 36,675 words). Revision log was marked COMPLETE before this pass started.

## Check 1. Nothing removed (python3 comparison, pre vs post)

| Item | Pre | Post | Result |
| :--- | :--- | :--- | :--- |
| Headings (`#`) | 53 | 67 | All kept; one intentional retitle, "6.1.2 The derivation" to "6.1.2 The Full Derivation: Itô's lemma"; 14 new headings (Full Derivation subsections, Scene A, Scene B, When-to-reach) |
| Display-math blocks (`$$` count) | 80 | 80 | Equal; none lost when derivations moved under "The Full Derivation" |
| [SOURCE EXTRACTION] / Annotation pairs | 14 / 14 | 14 / 14 | Equal |
| Trend Watch boxes | 6 | 8 | Kept; two were converted from (1)(2)(3) lists to prose with every number and citation retained (checked token by token) |
| Docket Diary, Poker Table, Desk Myth, Spec You Hand | 1, 2, 2, 2 | 2, 2, 2, 2 | Equal or more |
| Ways This Blows Up | 7 | 9 | Equal or more |
| Appendix F links (`#code-6-1` to `#code-6-7`) | 7 | 7 | None missing |
| Resource Graph items | 5 sections x 4 bullets | same | Only change is the intended ISDA July 2026 addition |
| Exercises | 6 | 6 plus 2 warm-ups | All six kept, each now has a "Check:" number; Check numbers re-derived by hand (115% / 53% book recovery, 70% reinstatement probability, \$691 vs \$600 and break-even near 69, 13.8% vs 12%) |
| `<!-- EXPLAIN: Listing 6.x -->` stubs | 7 | 0 | Not a writer deletion. Git history shows the stubs disappeared in the U1 code-explanation commits (present in ad55d97, absent from b07d5db onward); the brief says U1 owns them. In their place are the Code Companion walkthroughs and the seven `*The full listing is [Listing 6.x in Appendix F](#code-6-x)*` links. No action taken. |

Sentence-level diff: of the pre-revision sentences not found verbatim in the post text, all are explained by the retitle, the list-to-narrative conversions (cold open "By the end of this chapter" list, three Trend Watch boxes, 6.5.3 bold-lead paragraphs, 6.10.3 signals), the cold-open time change from 1:07 a.m. to 11:52 p.m. on Thursday 9 March 2023, the U1 EXPLAIN replacement, and the Exercise "Check:" additions. Nothing needed restoring.

## Check 2. Facts

Sources used: the named dossiers (`case_carvana_svb_wolfspeed_capital_structure.md`, `perspectives_buyside_credit_managers.md`, `life_quant_shop_daily_life.md`, `case_lmt_autopsies_us_2020_2026.md`, `case_courts_as_regime_variables.md`, `media_episodes_posts_parts_III_IV.md`), plus primary documents fetched directly: the Federal Reserve Board's 28 April 2023 SVB review (PDF, text-searched), SVBFG 8-Ks of 10 and 13 March 2023, Carvana's 22 March, 19 April, 3 May, 17 May, 2 June and 19 July 2023 press releases, the Debtwire article of 26 April 2023 and Bloomberg's 2 July 2024 piece (via Accounting Today). Two WebFetch calls plus direct SEC and Fed fetches; no web search needed.

Verified and left as written:
- Fed review: 12 Buy / 11 Hold / 1 Sell on 1 March; ratings stable since 2015 and Moody's last change in 2007 (pp.26-27); over \$40bn out on 9 March and over \$100bn more expected; Wachovia \$10bn over 8 days and WaMu \$19bn over 16 days; Table 1 peer figures (55 vs 25, 78 vs 42, 94 vs 41, deposits 89% of liabilities); HTM duration 6.2 years; \$21bn AFS sale, \$1.8bn after-tax loss, \$2.25bn raise, Moody's and S&P review; Silvergate wind-down (p.24).
- SVBFG 8-Ks: "The Company is no longer the parent company of the Bank" (10 March); "approximately \$3 billion of funded debt ... recourse only to the Company and is not guaranteed by the Company's subsidiaries" (13 March). Parent-only balance sheet figures sum correctly (assets ex-bank about \$4.2bn, liabilities about \$3.7bn, coverage a little over half without the cash).
- Debtwire 26 April 2023: 3.5% 2025s at 69 and 1.8% 2031s at 57 (MarketAxess), the Washington Mutual precedent (holdco exited in 2012 repaying bondholders at par with interest), PIMCO/Centerbridge/Davidson Kempner group and PJT as adviser (per WSJ).
- Bloomberg 2 July 2024: IRS claim cut from about \$649mm to \$43mm; 1.8% notes up as much as 2.625 to 63.625.
- Carvana: 22 March exchange (up to \$1.0bn of 9%/12% second-lien notes due 2028, \$500mm minimum, acceptance priority 1 = 2025s, total consideration \$632.50 to \$808.75, ADESA designated unrestricted, "at a premium to current trading prices"); 19 April extension with higher 2025s consideration; 3 May and 17 May extensions; 2 June (Friday) termination; 19 July release (83% of 2025 and 2027 maturities, over \$430mm a year of cash interest for two years, over \$1.2bn of debt, over 90% / about \$5.2bn, Moelis and Kirkland vs PJT and White & Case, Zito quote word for word, Q2 results the same day).
- Dossier-sourced and consistent: Apollo (Rowan "principal's mindset", Zelter 80% IG), Ares (Jim Miller, "walk away from transactions based on documentation terms", 4 Feb 2026), Hertz sponsors and offering breakdown (\$5.9bn; \$2.781bn / \$1.5bn / \$1.635bn), Oaktree memo titles and both Marks quotes, Octus Download EP 22 (23 Dec 2025, Judge Kaplan), Paleologo on Odd Lots (paraphrase, ex-Citadel and Millennium risk), SR 11-7 p.3 and pp.15-16, JPMorgan spreadsheet quote (Senate report p.185), Serta recoveries (0.6-2.4% vs 100% and about 75%), Serta remand (7 July 2026, \$261.13mm as of 22 June 2020), Bohn and Stein p.159 (page text on disk), Carvana per-series recoveries and the \$878mm gain.
- Arithmetic re-done: 3.1% volatility tax, 121/99/99/81 tree, \$600/\$110/6.0x/8x barrier at 70%, ATM call 12% vs 13.8%, hedge-pair P&L (+\$4.0mm bonds, -\$10.2mm short), reinstatement probability, bridge probability 38%, Newton steps.
- Real people: no invented dialogue. Zito and Marks are quoted from the primary documents; Paleologo, Rowan, Zelter, Miller are paraphrased with attribution. All dialogue belongs to the fictional cast (Theo, Kaz, Ines, Mags), and both long scenes carry "The dialogue is invented and belongs to the fictional cast"; both shop-life vignettes are labeled "fictional composite".

Fixed (11 small edits in the chapter):
1. 6.2.1 fulcrum argument: the first-lien banker's valuation was \$450mm, which would leave the first lien covered and make the second lien still the fulcrum; changed to \$350mm and the range to "350 to 750" so the argument is arithmetically right.
2. Scene A Beat 3: the "roughly 85 percent of the bank's deposit base" quote was attached to the Friday \$100bn alone; the Fed review applies it to the two days together. Reworded.
3. 6.4.2 JPMorgan vignette: "faulty results went undetected until April or May" had no support in the dossier; replaced with the supported quote that an error "likely had the effect of muting volatility by a factor of two" (pp.185-86, quoting the bank's task-force report).
4. Scene B Beat 1: "three-year and eight-year paper" replaced with "the shortest and the longest paper" (the 2030s were about 7.5 years out; the dossier says near and 2030).
5. Scene B Beat 1: removed the unsupported attribution of the best-short claim to S3 Partners; now credited only to Institutional Investor, 9 November 2022 (secondary).
6. Serta CLO seat: "CLO vehicles managed by LCM" was background knowledge, not in the sources; reworded to "LCM Lenders" with the caveat about LCM XXII Ltd.
7. 6.9.3: "over the last week of September 2025" widened to "over September 2025" (the refinancing pull and adviser hires came earlier than the filing week).
8. 6.10.3 first screen: "notes still priced like a near-term default story" conflicted with the company's own 74% end-of-June mark; reworded to "still priced a restructuring rather than a recovery to par".
9. Hertz: "not a creditor" about Apollo hedged to "as the offering documents describe the structure".
10. Scene A Beat 5: noteholder advisers' names would not be in "first-day pleadings"; changed to "early docket filings".
11. 6.8 Big Bang scene: Delphi bonds "went up after the bankruptcy" softened to "bid up around the settlement".

## Check 3. Hygiene

- No code fences anywhere in the chapter (no ```text diagrams either; none were there before).
- Display math: 80 `$$` markers, pairs balanced, no block over 25 lines. Inline `$`: no line has an odd count; no unescaped currency found (every `$digit` hit was a math span).
- No `---` line anywhere.
- The last line is `<!-- STATUS: COMPLETE -->` (one occurrence, file ends with a newline).
- Cross-references checked: Chapter 5 cold open (2 June 2023 Carvana scene, 19 April \$858.75 consideration), Chapter 5 §5.1.5, §5.5, §5.6, §5.7, Chapter 6-B §6-B.2 all exist.

## What remains doubtful

- Secondary or vendor items kept hedged in the text and not independently verified: SIVB implied volatility 39 floor and 167 print (Market Rebellion); holdco bond levels of 37-42 on 10 March and 47-50 on 13 March (Bloomberg/Reuters summaries); purchases "around 30" by Centerbridge, Davidson Kempner and PIMCO (WSJ via Axios); CVNA closes (\$3.72, \$9.79, \$12.92, \$55.80, \$203.36) and the 74% / 53.8% / 44.8% / 84.7% fair-value ratios, all vendor bars or computed from the 10-K and 10-Qs; S3 Partners' \$646mm and \$2.18bn; SIVB \$106.04 close (class-action notices).
- The late-August 2026 N.D. Cal. ruling on the \$1.71bn FDIC claim is reported only by American Banker and Reuters; the text says the opinion was not reviewed.
- Mags's 2008-09 recollection (fax confirmations, Delphi 2005, Big Bang spring 2009 with 100/500 bp coupons) comes from general knowledge, not from a dossier or fetch. The broad facts are standard, but the Delphi pricing detail is softened rather than checked.
- Pre-existing items the ed2 fact-check flagged and this revision did not touch: S&P Market Signal PD figures, 125 F.4th 555 and Ocean Trails v. MLN Topco, UBS 4.8%/3.1%, First Trust/Moody's 4.3% (May 2026), Quinn Emanuel "over 50%". They remain hedged as in the earlier text.
- Hertz 424B4 breakdown and the Apollo/Ares/Marks items rest on the perspectives dossier, which says it fetched them; not re-fetched here.
- Serta 0.6-2.4% recoveries rest on a Skadden summary in the case dossier; the Mayer Brown remand figures rest on a dossier entry, not a re-fetch.
- Length: the chapter is now 2.6 times its pre-revision length, which the log attributes to the brief's mandated scene sizes; whether that is too much is an editorial call, not a fact problem.
<!-- STATUS: COMPLETE -->
