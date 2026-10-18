# Verification Report, Edition 2: Chapter 7-B

Verifier pass on `book_src/07_ch07b_statistics_for_credit_panels.md` (955 lines, 26.1k words by `wc -w`) against the pre-revision text (`9ac1c37`, saved to `/tmp/pre_07_ch07b_statistics_for_credit_panels.md`) and `state/revisions/ed2/07_ch07b_statistics_for_credit_panels.brief.md`. The revision log carried `<!-- STATUS: COMPLETE -->` and no prior verify file existed. One caveat on the baseline: `9ac1c37` predates the U1 primer pass and the figures pass, so it has no figures, no Resource Graph and `EXPLAIN` stubs. I therefore ran every comparison twice, against `9ac1c37` and against `cea2d0d`, the version the brief describes (13,604 words, five figures). Web budget used: 7 of 15 calls (Venn episode page, SR 11-7 PDF, arXiv abstract page, two searches, Fed press release, podscripts transcript); everything else was checked against the dossiers and sibling chapters.

## 1. Nothing removed (python3 comparison, pre vs post)

| Item | Pre (`cea2d0d`) | Post | Result |
| :-- | --: | --: | :-- |
| Headings (`#` lines) | 51 | 63 | 49 kept verbatim; 2 renamed ("Ledoit-Wolf, derived in five lines" became "Ledoit-Wolf: noise over noise plus misspecification" with the derivation under the new Full Derivation heading; "The Brownian-bridge correction, derived" became "The Brownian-bridge correction" plus its Full Derivation); 14 added by the brief |
| Display-math blocks (`$$` lines) | 76 | 76 | All 38 blocks present; only differences are the attenuation plim (now written with its Cov/Var step) and the closing punctuation of (7B.6) |
| Numbered equations 7B.1-7B.9 | 9 | 9 | All present, same numbers |
| `[SOURCE EXTRACTION]` blocks and annotations | 2 | 2 | Verbatim (Bohn-Stein p.443; Bolder p.508) |
| Trend Watch | 1 box | 1 box | Verbatim; moved to the end of 7-B.2 as the brief directs. The other two "Trend Watch" strings are in-text pointers |
| Exercises 1-6 with solutions | 6 | 6 | Verbatim except one pronoun in Exercise 1 ("he" to "they") |
| Appendix F links (`#code-7b-1`, `#code-7b-2`) | 2 | 2 (+9 in the Finder table) | Kept, each listing has its link line |
| Resource Graph | 12 URLs | 12 URLs | The whole section is byte-identical to the base (`diff` empty) |
| "*Used in:*" lines | 11 | 11 | Verbatim |
| Figures 7-B.1 to 7-B.5 and captions | 5 | 5 | Present, unchanged |
| Practice-cohort table, §7-B.9 treatment table, CLO "other 4%" box, Spec You Hand the Robot, Mags's mood line | | | All present |

Paragraph-level diff: 197 of 261 base paragraphs are verbatim in the post text. The 64 that are not were each inspected and are accounted for by a brief item: the (i)-(viii) "By the end of this chapter" list (narrative plus Finder table, every tool still in the chapter); the seven-place probability inventory (all six named places survive in the narrative); "Where this goes next" (its Aalen-Johansen, cured-fraction and §15.5 pointers moved into Scene 2's last paragraph); "Check the proportionality" (Mags's regime sentence, plot kept); the panel-bootstrap bullets (Kaz's three intervals, wild cluster, Sharpe pointer); "What credit adds" (the boosted-model story, extrapolation and permutation-importance habits kept); variance-reduction bullets (antithetic, control variate, importance sampling with its weight all kept); the derivation paragraphs moved into the five Full Derivation subsections (sandwich, Moulton score variance, attenuation, Bartlett shortfall, logistic IRLS, Greenwood, partial likelihood, Breslow, cloglog, Ledoit-Wolf, PCA Lagrangian, bridge density, Girsanov remark all present). Against `9ac1c37` the only extra losses are the two U1 `EXPLAIN` stubs, which U1 had already replaced before this revision. No restoration was needed.

## 2. Facts (new claims about real events, firms, people, dates, amounts)

I split the post text into sentences, removed those already in the base, and read the 620 new sentences that name a real entity, date or amount. Verified:

- Dickerson, Robotti and Rossetti, arXiv:2604.07880, posted 9 Apr 2026, 108 signals in nine clusters: **web-confirmed** (arXiv abstract page) and dossier B1. Menkveld et al., *Nonstandard Errors*, JF: unchanged Trend Watch wording.
- 12 Mar 2020 (Thursday) LQD 5% below NAV; 23 Mar (Monday) SMCCF; 25 Mar (Wednesday) S&P cut Ford to BB+, about \$36bn (T. Rowe Price, Nov 2020); 31 Mar rebalance: unchanged from Ch 1 §1.8.2 and Ch 8 §8.4 (already fact-checked). 9 Apr 2020 (Thursday) Fed expansion of the corporate facilities: **web-confirmed** (Fed press release of 9 Apr 2020); the "IG as of 22 March" eligibility rule is Ch 1 §1.8.2's. 12 May 2020 (Tuesday) first ETF purchases: Ch 1 and the electronification dossier. All weekdays recomputed.
- PB-03 legs, sizes, DTS ratio 1.65, 35 bp borrow (about \$0.13mm), \$0.45mm half-spreads, \$0.5mm of \$1.25mm on the fallen-angel factor, the thesis sentence and its 30 Sep 2020 date, closure in Ch 24 §24.7, PB-19's "half gone by 31 March 2027": all match `state/rv_pair_book.md` and Ch 8 §8.4.
- The eight-deal table (Revlon 7 May 2020 to 15 Jun 2022; Boardriders Aug 2020 to Sep 2023; Envision Apr/Aug 2022 to 15 May 2023; Incora 28 Mar 2022 to 1 Jun 2023; Robertshaw 9 May 2023 to 15 Feb 2024; Lumen 31 Oct 2023 / 22 Mar 2024, no filing; Trinseo 8 Sep 2023, 17 Jan 2025, 26 May 2026; Saks 23 Dec 2024, 8 Aug 2025, 13 Jan 2026): all in `case_lmt_autopsies_us_2020_2026.md` section 0. Every month count was recomputed from the dates (25, 37, 9/13, 14, 9, 31, 33/16, 5/13).
- Moody's 46% of 2023 distressed exchanges re-defaulted (Bloomberg Law, 23 Apr 2025); Roe and Rotaru, 89 coercive non-pro-rata LMEs, 22% clean at two years and fewer than half at one year (HLS Roundtable, 24 Feb 2026); Moody's 1,173 soft-event borrowers, more than 70% of hard defaults within two years (18 May 2026); 38 LMTs in 2024: `trend_lmt_default_recovery_cycle.md` rows 14-15, 45, 57, 60, 115, and Ch 14 §14.3 carries the same figures and dates.
- Mags's May 2005 line: S&P cut GM and Ford on Thursday 5 May 2005 (weekday checked; PB-04 dossier). Nothing quantitative is added.
- SEC order against Two Sigma, 16 Jan 2025 ("in or before March 2019", acted on "until August 2023"): `life_quant_shop_daily_life.md` 6.2 and `perspectives_dealers_and_systematic_shops.md` 3.5; Ch 1-B tells it. SR 11-7 p.12 "all changes are logged and can be audited": dossier 2.1 and the Ch 7 verifier's earlier check (the Fed PDF is image-only, so I could not re-extract it).
- Falk-Wallace, *Odd Lots* 25 Jul 2024, "what you're levering is just that residual term": **text confirmed** in the podscripts transcript (machine transcript, speaker inferred). Paleologo, 20 May 2024: paraphrase only, per dossier 5.1.
- Kendall (1954) bias $-(1+3\rho)/T$ and the Dickey-Fuller 5% value of about -2.9: textbook, recomputed.
- Pod-stop arithmetic (Sharpe 1, 6% vol, 5% stop): 43% confirmed in Ch 8-D §8D.5 and the pod dossier.
- Every worked number in the ten Math, Gently boxes, both Long Scenes, the vignette and the exercises was recomputed: Moulton 2.5 and 1.58, wedding-guest 6, rumor 3.5/sqrt3, log-odds 0.122 and 10.9%, Brier 0.21 and 0.12, ten-issuer 0.771, race 2/3, batting w=0.5 and 0.8, eigenvalues 1.6 and 0.4, MP edge 2.25, 281 null axes, hat-of-slips mean -0.4, 2.8 and 0.33, MC se 0.42 points and 40,000 paths, reflection e^-0.96 = 0.38, KM 0.875/0.625/0.50/0.375/0.19, Greenwood 17 and 16 points, 60-day AR(1) se 0.046 and half-lives 9.6, 4 and 17 days, 792 = 36 x 22 and sqrt(792) = 28, 63 trading days in Apr-Jun 2020, Brier, the 4-s.e. tolerance and the one-in-three failure rate of the old tolerance, Broadie-Glasserman-Kou 17.1% versus 23.0%, control variate 1-0.95^2.

### Problems found and fixed (small Edits in the chapter)

1. **Arithmetic impossibility in Scene 1, Beat 2.** Issuer t 2.6, day t 4.0 and a two-way t of 1.8 cannot coexist: two-way variance equals issuer plus day minus the cell, with the cell term non-negative, so the two-way t cannot fall below about 2.18. Changed the day-clustered t from 4.0 to 2.5 (two-way 1.8 now follows). Logged the change in `state/cast_bible.md`. The figures pass should use 14.2, 2.6, 2.5, 1.8.
2. **Cross-reference that overstated Ch 9.** "Chapter 9 counts them as a factor (§9.6.1)" is not what §9.6.1 does (it treats ratings-driven forced selling, no wave count). Reworded to "meets the same flows as a forced-seller factor (§9.6.1), and the factor inherits the short count".
3. **Unsourced history stated as fact.** Mags's "four waves of fallen angels since TRACE" is now "by my count".
4. **Lumen clock contradiction.** Mags said the support agreement "is the first step on the clock" while the table and KM clock start at the 22 Mar 2024 closing (31 months). Reworded to start the clock at the closing "by the rule we just used for Envision".
5. **Lumen coding was one-sided.** The dossier says Lumen's term-loan deals were open to all but the note deals were "not offered to all holders". The coding sentence now says so and calls Lumen a second judgment call.
6. **Cox interval did not follow from the quoted inputs.** exp(1.8 +/- 1.96 x 1.1) gives 0.70 to 52, not the 0.65 to 54 used in three places. Gave the unrounded inputs (coefficient 1.78, standard error 1.13), which reproduce 0.65 to 54, hazard ratio about 6 and t 1.6.
7. **Venn seat over-reached.** The public episode page and Venn's own "Parsimony and a Less-Is-More" article confirm 18 orthogonal factors, interpretability and a two-step regression, but not Lasso/OLS (that detail is the dossier's feed description). Rewrote to "per the episode's description", dropped "explains a little more" and the unsupported "any portfolio a client uploads, across asset classes".
8. **Falk-Wallace credential.** "A former Citadel portfolio manager" became "formerly of Citadel" (what the sources support).
9. **12% versus 13%.** The pod seat quoted "about 12%" at 4% vol and cited §8D.5, which says 13%; changed to 13%.
10. **Hygiene.** Em dash in the Finder table placeholder cell replaced by "none"; trailing blank line after the STATUS marker removed.

No real person has invented dialogue. Real people appear only as sourced quotation (Falk-Wallace), paraphrase with the source named (Carrano, Paleologo), or citation (Menkveld, DRR, Roe and Rotaru, Kendall, Petersen and so on). Fictional composites are labelled where they appear: Scene 1 header (desk, panel, regressions, Dov's pod and Pair Book fictional), Scene 2 header (dates real; codings, hazards and the Corvane, Ostrander and Tallis cards fictional), the Quant-Shop Life vignette ("A fictional composite ... no real firm is described"; the Two Sigma order is cited separately as public record), the dealer seat ("a generic seat; no firm is named") and the pod seat ("a generic seat; the arithmetic is illustrative"). Mags's 2005 line is a fictional character recalling a public event; no real person speaks.

## 3. Hygiene

No code fences of any kind; 76 `$$` lines, balanced and unmixed with text; no paragraph with an odd inline `$`; 563 inline math spans checked for stray prose or currency inside them (none); no unescaped currency (every dollar amount is `\$`); no `---` line anywhere; one em dash left, inside a Resource Graph episode title that is verbatim and protected; one `STATUS` marker, and the last line is `<!-- STATUS: COMPLETE -->`.

## What remains doubtful

- **Lasso/OLS** in the Venn seat rests on the episode feed description in the dossier. Hedged in the text; re-listen or drop the clause if the fact-check pass wants it firm.
- **Falk-Wallace and Paleologo** come from machine transcripts (podscripts). The Falk-Wallace sentence was found verbatim; speaker attribution is by inference, and the Bloomberg audio page dates the episode 24 Jul where directories say 25 Jul. The Paleologo paraphrase was not re-checked against audio.
- **Fed 9 April 2020 eligibility** ("IG as of 22 March") is carried from Ch 1 §1.8.2; the press release I could read confirms the date and the expansion, not the 22 March detail.
- **SR 11-7 p.12** quote relied on the dossier and the Ch 7 verifier; the Fed PDF has no text layer.
- **Roe-Rotaru, Moody's 46% and the 1,173-borrower study** were checked against the dossier and Ch 14, not re-fetched.
- **Coding choices in Scene 2** (Envision's clock at the August close, Revlon and Lumen as zero) are judgment calls and are flagged as such in the scene; the dossier marks some Envision, Boardriders and Saks details CHECK, but the chapter uses only the dates.
- **"At PJT"** is the book's established former employer for Theo; the new sentences describe a hypothetical associate's habits, not a claim about the firm.
- **"Chapter 9-B"** (cross-reference in the Errors-in-variables paragraph and a "Used in" line) has no file in `book_src` yet; this is inherited from the base and the TOC plan.
- **For the figures pass:** follow the chapter, not the brief: event months 5, 9, 9, 14, 25, 33 with Boardriders 37 and Lumen 31 censored; Scene 1 t-statistics 14.2, 2.6, 2.5, 1.8; Cox 1.78 / 1.13; the 40,320 bond-days / 200 issuers / 63 days panel.

<!-- STATUS: COMPLETE -->
