# Verification Report, Edition 2: Chapter 16 (Post-Reorganization Equities, Rights Offerings & Bankruptcy Claims)

Chapter: `book_src/16_ch16_post_reorg_equities_and_claims.md`. Pre-revision text: commit 9ac1c37 (16,187 words by wc; now 35,812 words, 994 lines). The revision log was marked COMPLETE before this pass started.

Baseline caveat: 9ac1c37 predates two upstream passes that also changed this file, so a raw diff shows changes the writer did not make. (a) The five figures (Figure 16.1 to 16.5) were inserted by the figures pass. (b) The five `<!-- EXPLAIN: Listing 16.x -->` plus "Code Companion" stubs were replaced by listing-explanation prose and `*The full listing is [Listing 16.x in Appendix F](#code-16-x)*` links (the U1 stage). Neither is a writer deletion, and no action was taken.

## Check 1. Nothing removed (python3 comparison, pre vs post)

| Item | Pre | Post | Result |
| :--- | :--- | :--- | :--- |
| Headings (`#`) | 43 | 52 | All 43 kept verbatim; 9 new (five "The Full Derivation" subsections, four "When ... applies, and when it breaks" subsections) |
| Display-math blocks (`$$` pairs) | 37 | 38 | Every pre block found verbatim in post (whitespace-normalised); one extra block added |
| [SOURCE EXTRACTION] / Annotation | 9 / 9 | 9 / 9 | Equal; every extraction line identical |
| Trend Watch boxes | 4 | 4 | Equal (one hedge sentence updated, see Check 2) |
| Docket Diary box | 1 | 1 | Byte-identical after whitespace normalisation |
| Poker Table, Desk Myth vs. Desk Reality, Ways This Blows Up | 1, 1, 1 | 1, 1, 1 | Equal |
| Spec You Hand the Robot | 5 | 5 | Equal |
| Appendix F links (`#code-16-1` to `#code-16-5`) | 5 | 5 | None missing |
| Exercises | 6 | 6 | All six identical |
| Resource Graph bullets (Podcasts, Practitioner, Academic, Data) | 32 | 32 | All pre URLs present (0 missing); additions only |
| Long quoted strings (40+ characters) in pre | all | all but one | The one missing is the sentence "a 30-year warrant is mostly a bet on not needing Chapter 11 again before 2051", recast in the new warrant coda as Mags's "weather forecast for 2051" with the same point |
| Figures | 0 | 5 | Image files exist in `assets/figures/` |

Sentence-level diff (every pre sentence not found verbatim in post, 52 lines inspected): all are explained by (i) the cold-open learning-objectives list becoming a narrative paragraph, (ii) the §16.5.2 statute bullets and the §16.6 six-item list becoming scenes (every citation, number and caveat retained), (iii) the Debrief bullets becoming Theo's read-aloud (content kept, two sentences sharpened as briefed), (iv) the U1 EXPLAIN replacement, (v) three small rewordings (the "\$769mm was not a gift" pair, "Theo does not say I told you so", the §16.4.3 coda). Nothing needed restoring.

## Check 2. Facts

Sources used: the dossiers the brief names (`case_carvana_svb_wolfspeed_capital_structure.md`, `case_courts_as_regime_variables.md`, `case_lmt_autopsies_us_2020_2026.md`, `perspectives_buyside_credit_managers.md`, `media_episodes_posts_parts_III_IV.md`, `life_quant_shop_daily_life.md`, `trend_lmt_default_recovery_cycle.md`), plus 13 web calls (searches and fetches; Reuters via Yahoo, the ABLJ page, Simpson Thacher, the HLS Roundtable post, and search summaries for Wolfspeed, Spirit and Hertz). Arithmetic re-done in python3.

Verified and left as written:
- Wolfspeed: exchange ratios 0.008352 and 0.013920 (1,306,896 and 2,178,190 shares over 156.48mm old shares); 24,533,760 of 25,840,656 shares to converts; plan value \$22.02; prepack in Houston; Reuters "surged 33% on Tuesday" (30 Sep 2025); a volatility halt on 29 Sep (two independent reports); \$17.41 at 31 Dec 2025, \$73.50 on 26 May 2026 (dossier); \$1.5bn conditional government loan commitment of 7 Oct 2026 and a close of \$31.02 on 8 Oct 2026 (one source, kept hedged in the text).
- Envision/AmSurg: emerged 3 Nov 2023, second lien took all the equity, \$300mm rights offering at a 30% discount, 73% projected recovery; Ascension agreed to buy AmSurg on 17 Jun 2025 for a reported \$3.9bn, about \$250mm above the top of the plan valuation (dossier citing Octus, Becker's; text keeps "approximate").
- Buccola, Marcovich Gross & McBrady (ABLJ page fetched): 49 bankruptcies since 2016; 18 of 19 deals with an arm's-length value estimate; factor of two; 25.3% average discount; 20.1% all-in; Buccola is at the University of Chicago Law School; the body text says the estimates come from market prices or acquisition consideration, which matches the chapter's gloss.
- ConvergeOne: 25 Sep 2025, Judge Hanen, S.D. Tex., §1123(a)(4), \$245mm rights offering, 10% backstop fee (Simpson Thacher), mootness denied Oct 2024 and appeal noticed 22 Oct 2025 (dossier).
- Hertz: sponsor quotes ("over \$5.9 billion of new equity capital", "nearly \$19 billion of creditors in full", 8-K Ex. 99.1); share table sums to 471,102,514; \$769mm / 89.05mm = \$8.64; \$1.16bn ex post seat value; June 2026 drop of 40.7% to \$3 from \$5.06 (IFR, via search summary); Bloomberg Law 16 Oct 2026 adviser hires (dossier); 10-K professional fees and bankruptcy costs of about \$175mm (2020) and \$257mm (2021).
- Spirit: emerged 12 Mar 2025; Q2 10-Q filed 11 Aug 2025 with "substantial doubt" going-concern language; shutdown announced 2 May 2026 with about \$500mm of federal support talks collapsing (Octus, Inquirer, AirlineGeeks). Accounts differ on why the package failed, and the chapter already hedges the DIP-lender attribution as a podcast account.
- Cross-references exist: Ch 1 §1.5 (Itô ½σ² box), Ch 6 §6.1.1, Ch 5 §5.1.1, §28.4 (Kelly with jump-to-default), §13.8 (Priming Risk Score), §14.3 (re-default clock), §12B.6 and Ch 12-C.
- Real people: no invented dialogue. All dialogue belongs to Theo, Kaz, Ines, Mags, Harlan and Dana, who are the fictional cast. Real people appear only as cited authors or through quoted public documents (the Third Circuit opinion, the Hertz 8-K). Labels are present on the cold-open company, Mags's banker ("fictional composite"), Dana's vignette ("fictional composite"), Harlan's deal, the two vendors and retailer, the Spirit desk, position and committee, and the second airline.
- Arithmetic re-done: Black-Scholes put 0.0734, 37% and 0.20 shortfall; fixed-point sequence 8.66, 8.58, 8.56 (slope 0.15); \$26.70 warrant at \$29 (computed 26.68); about \$2 at a \$3 spot (computed 1.99 to 2.01); price floor \$2.43; implied volatility low 50s (53.1% computed); Jensen examples 0.3125 and 0.917; hazard factors 0.926 and 0.862; Kelly 2.0%, 1.5% and -0.2% per flip; mixture median -5%; runway dial 0.71; N_eff 1.33; \$400k cap; 93% cleared after 200 days.

Fixed (8 small edits in the chapter):
1. §16.5.2: the stale sentence "the vendor who shipped on day 22 by boat and the vendor who delivered on day 19 by truck" (inherited from the pre text, now contradicting the scene's own dates and Exercise 5) was rewritten to the scene's facts (25 days out by sea, 22 days out by truck), still not solving Exercise 5.
2. §16.7: "The airline it owned lasted about fourteen months more" was wrong (emergence on 12 Mar 2025 to shutdown on 2 May 2026 is about fourteen months in all). It now says the airline kept flying about eight months after the second filing and about fourteen months after emergence.
3. §16.3.1: "a year earlier" became "in October 2024" (dossier date for the mootness ruling).
4. §16.3.1 and the §16.3.2 Trend Watch: the ConvergeOne appeal is no longer described as simply "open". A Simpson Thacher note of 5 Feb 2026 reports that the debtors and majority lenders stipulated to open the backstop to the minority lenders after noticing the appeal. The text states that and says no Fifth Circuit merits opinion was found. The Simpson Thacher note was added to the resource graph.
5. §16.3.4 Ines's line "In Hertz they weren't creditors at all" was narrowed to the sponsors' seat (buying equity in a solvent company); the sponsor-seat box now says "as the offering documents describe the structure" before the claim that Apollo was not a creditor (the same hedge the Chapter 6 verification used).
6. §16.6 admin-burn aside: replaced "an order of magnitude, not a tally" with the 10-K figures (about \$175mm for 2020 and \$257mm for 2021, approximate).
7. §16.6 and §16.4.3: the October 2026 "stock is about \$3" now says it is the last sourced print (the June drop), because no October quote was found.
8. Cold open: "vendors differ on the exact closing print" widened to opening and closing prints (the \$18.00 open is one vendor's chart; another source puts the close at \$20.89).

## Check 3. Hygiene

- No code fences anywhere (none were there before; no ```text diagrams either).
- Display math: 76 `$$` markers (38 blocks), balanced, all single-line. Inline `$`: no line has an odd count; no unescaped currency; no `\$` inside a math span.
- No `---` line anywhere.
- The last line of the chapter is `<!-- STATUS: COMPLETE -->` (one occurrence). Re-run after the edits: still clean.

## What remains doubtful

- Wolfspeed day-one prints: the \$18.00 open, the \$8.05 low in the brief and the close (\$22.10 on Yahoo bars, \$20.89 in one news summary) differ by vendor. The text avoids the low and says vendors differ. The brief's \$23.22 close on 16 Oct 2026 could not be sourced; the text uses the \$31.02 close of 8 Oct 2026 (single source: an AskTraders summary) and says so.
- Hertz's October 2026 share price was not found; only the June 2026 drop to \$3 is sourced (IFR, search summary). The Docket Diary's "exchangeable PIK notes" wording is pre-existing and unchanged, while the IFR summary says "convertible bond offering".
- ConvergeOne: the stipulation comes from one law-firm newsletter; the Fifth Circuit docket was not checked, and the Lowenstein PDF could not be read. The resource graph still lists Lowenstein/Mondaq and Bloomberg Law titles that say "Fifth Circuit" (kept as published, with the existing caveat); they may concern other Fifth Circuit decisions.
- Spirit: the second filing's \$8.1bn debts vs \$8.6bn assets and the \$795mm of converted debt are pre-existing press-report figures, not re-checked; the reason the federal package failed is reported differently by Octus, the podcast and the trade press.
- The make-whole table (*Energy Future*, *Momentive*, *Ultra*, *Hertz*) was checked against memory and the Third Circuit's own description, not re-read from the opinions; it carries the "read the opinions" caveat.
- AmSurg figures rest on the case dossier (Octus, Becker's, flagged CHECK there).
- The forward pointer to "Chapter 16-B" names a chapter that does not exist in `book_src/` yet (the brief allows the pointer).
- Length: the chapter is 2.2 times its pre-revision length, within the brief's scene sizes; whether that is too long is an editorial call, not a fact problem.
<!-- STATUS: COMPLETE -->
