# Fact-check report: Ch 9-B, The Bond Data Problem and the Replication Crisis

Chapter: `book_src/09_ch09b_the_bond_data_problem_and_the_replication_crisis.md`. Brief: `state/advisor_briefs/09_ch09b_the_bond_data_problem_and_the_replication_crisis.md`. Checked 2026-10-18 against `state/research/papers_factor_replication_crisis_and_bond_data.md`, `rv_credit_pairs_literature_and_mechanics.md`, `case_manufactured_credit_events.md`, `trend_trend_following_tsmom_credit.md`, `life_quant_shop_daily_life.md`, the media dossiers, `state/cast_bible.md`, and 19 web fetches or searches (primary sources first: arXiv 2604.07880 full text, the 94-page OBAP PDF with the Internet Appendix, the FINRA Rule 6730 text, the FINRA timeframes and file-layout pages, the DNR discussion paper PDF, the Warwick post, PyPI JSON, the pipeline README, the OBAP site, NBER w35578, QuantPedia, three *Flirting with Models* pages, one SIFMA search).

## 1. Brief CHECK list

| CHECK item | Resolution |
| :-- | :-- |
| SSRN id 6088966 unverified | Chapter never cites it; it cites arXiv:2604.07880 (title, authors Dickerson, Robotti, Rossetti, 9 Apr 2026 confirmed on arXiv). Resolved. |
| 269 months vs T = 268 | Found that the paper itself mixes both: Table 1, Fig. 3 and the survivor tables use 2002-09 to 2024-12, T = 268; Tables 3 and 4 (look-ahead) use 2002-08 to 2024-12, T = 269; Fig. 6 uses 2003-03 to 2024-12, T = 262. The chapter had asserted "the difference is not an error: 269 prices produce 268 returns" and that "the return tables report 268". FIXED: now states which tables use which T, and labels the explanation as this book's reading, not the paper's. Related "268 months" mentions in 9B.6 and 9B.8 adjusted. |
| Dick-Nielsen 2009/2014/2019 texts not read | Chapter attributes the step-1 filters to DRR's description and says so in the spec margin; FINRA layout fields (T/X/C/R/Y, As-Of A/R, Prior Reference Number, capacity A/P, 20-business-day reversal, match keys) verified on the FINRA page. Resolved. |
| BBW retraction notice text not read | Chapter does not quote the notice; relies on the Warwick post, which I read: "two of the remaining three factors had a 'lead error', while the third factor had a 'lag error'", ex-post filtering of the left tail, "no incremental pricing ability over the CAPM", "more than 400 times ... Google Scholar". Chapter wording matches. The "first retraction" claim was overstated (see fixes). No claim about intent; Georgetown outcome not asserted. Notice record (JFE 150(3), 103721, Dec 2023) rests on the dossier's Crossref/IDEAS check. |
| DFPS momentum numbers not retrieved | Chapter states no DFPS momentum numbers. QuantPedia page re-read: 23% retain significant alphas, CAPM fails, outliers reviewed individually, defaults kept, no momentum discussion. Resolved. |
| Fig. 6 curve points | Verified in the arXiv text: ex-ante trimming of either tail leaves the alpha indistinguishable from zero; right-tail ex-post at 10% a month about 0.60%; left-tail ex-post crosses zero "only at thresholds around -40%"; Mar 2003 to Dec 2024. The figure caption already says only these anchors come from the paper and the curves between them are schematic. Resolved. |
| OBAP data licence unstated | Confirmed on the OBAP site (no licence stated); repo is MIT (README). Chapter says both. Resolved. |

## 2. Claims checked and found correct

- Table 1 (all seven factors, premia, alphas, t-statistics, three columns), Table 4 (mom3_1, mom6_1, mom12_1, ivol_bbw, var_95, es_90), LIB shares (above 80%, 45-55%, 20-50%), corr 0.99 (0.93-0.98 within-firm), `$1 -> $12` vs `$1.1-$1.4` reversal wealth, Theorem B.1 form 2*kappa*rho*sigma_delta, LAB spikes in 2008-09, 2011-12, March 2020, convex in VIX, 2-3x larger in NIG (Internet Appendix).
- Survivor table (IA.X and IA.XI): dcs6_wf 2.46/2.66 (t 6.77/4.98, IR 1.59), val_ipr_wf 2.30/2.22, val_ipr_dts_wf 2.23/2.47, sysmom12_1_wf 2.20 (3.04), idimom12_1_wf 1.55 (2.94, IR 0.87), VW val_ipr 3.71 (2.12), industry momentum 3.44-4.46 (t 2.11-2.44), age the only single-sort survivor, val_hz in NIG 0.37 (t 1.91) the closest in IG/NIG separately; 432/65/26/25; NSE 0.35 vs 0.33, alphas 0.27 vs 0.15, 1.15 and 1.45, 648 and 168 paths, 12 of 36, 94%, 21% and 15%.
- Kappa values 1.09, 1.40, 1.75 recomputed from the normal tail; tiny numbers (0.53%, 0.33%, 1.00%) and Exercise 2 recomputed; Math Gently 98/99/100 arithmetic; DTS sizing and carry arithmetic in the Pair box ($22.0mm, $23.9mm face, $5.3mm, $12.4mm, $10.2mm, -$0.62mm, $155k); Newey-West floor(T^0.25) = 4 for T = 268 or 269.
- Pipeline facts (README_stage0 order and thresholds, v4.2.1 "Last Updated September 2026", MIT, about 5 hours, about 5 GB, WRDS TRACE/FISD/ratings), PyBondLab 0.3.0 (24 Sep 2026, MIT, Python 3.11+, required columns date, ID, ret, VW, RATING_NUM, SingleSort/WithinFirmSort/DataUncertaintyAnalysis/AssayAnomaly), OBAP 11 Dec 2025 "Stage 1 ... public beta".
- FINRA Rule 6730(a) quotation is verbatim ("as soon as practicable, but no later than within 15 minutes of the Time of Execution"); the "pattern or practice of late reporting ... Rule 2010" language is in 6730(f); caps $5MM IG and $1MM non-IG on the FINRA timeframes page.
- DNR (Hitotsubashi DP 771, 23 July 2025, Dickerson, Nozawa, Robotti): 341 factors, 58 significant, average alpha 0.28%, 0.09%/0.05% after costs, 2 and 1 significant, delay costs 0.11/0.22/0.11/0.06, ML 0.82% to 0.33%. 2022: 70% of 29,543 bonds on 10 or fewer days, 109 (0.4%) daily (dossier).
- Windstream: Judge Furman's ruling 15 Feb 2019, Chapter 11 on 25 Feb 2019 (ten days) per `case_manufactured_credit_events.md`. Asquith et al.: about 30 bp until about 70% on loan; 173 bp before and 245 bp after bankruptcy; Nashikkar-Pedersen on risky, low-rated, small, old bonds (dossier). NBER w35578 (Aug 2026; Ghaderi, Plante, Roussanov, Seo; 128 years; over 100,000 bonds; "sizable and statistically significant credit risk premium") confirmed on nber.org.
- Calendar: Mon 9 Nov 2026 and Tue 10 Nov 2026 weekdays correct; 29 Sep 2026 falls in September's last five NYSE business days (24-30 Sep); Veterans Day Wed 11 Nov 2026 (SIFMA lists it; secondary sources say bond-market close); Theo's eighth week matches Day One Tue 22 Sep 2026 in the cast bible; Brambleworth hand Fri 16 Oct matches "fourth week".
- Cross-references verified to exist: Ch 2 §2.2.2; Ch 4 rerun week (Sharpe 3.1 to 0.9) and Figure 4.3; Ch 7 §7.2 (BH box, one-day placebo), §7.8, §7.9; Ch 7-B (Ford-GM half-life card, residual-panel PCA); Ch 8 §8.2, §8.4; Ch 8-D §8D.3, §8D.5; Ch 9 §9.3, §9.8-§9.10, §9.9 (`obap_repro`, Hana); Ch 10 §10.1, §10.5, §10.5.4; Ch 12-B and 12-C (ruler flips near default); Ch 13; Ch 18 §18.8; Ch 22 §22.2, §22.2.2; Ch 24 §24.7; Ch 27 §27.2; App B §B.16; App E Laws 9 and 12 (and tags L1, L9-L12, L14); App F Listing 9-B.1 anchor `#code-9b-1`.

## 3. Fixes made to the chapter (all small Edits)

1. "Alessandro Robotti" corrected to **Cesare Robotti** (name on the Warwick post and on all three Dickerson-Robotti papers).
2. Warwick post: "the first retraction of its kind at the journal" replaced by the post's own words ("This is the first time this has happened"), with "400 citations on Google Scholar"; the post does not say "first retraction of its kind".
3. **rho in Theorem B.1 was wrongly described as a correlation.** The paper (Eq. A.26 text) says rho is the noise share of the observed signal, a ratio of standard deviations, "not a correlation coefficient". Fixed in the Math, Gently box and the formula paragraph; kappa now described as the paper's tail mean (Eq. A.25).
4. T = 268 / 269 paragraph rewritten (see section 1); "268 months" in 9B.6 and 9B.8 adjusted.
5. Brambleworth was "8% notes due 2030" in 9B.1 and "8% 2030s" in 9B.7, contradicting Ch 3 and Ch 3-B (the 85½ bid was on the **9.25% senior secured notes, B3**). Both changed to 9.25%; the pair arithmetic does not depend on the coupon.
6. DNR delay costs are "for large trades"; added, plus the 0.01-0.02% slow-factor figures. "Nine ML models keep about a third of a 0.82% alpha" corrected: they fall to about 0.33% (about 40%).
7. Obenshain "quote": the phrase is in the episode description, not a verified Obenshain quotation; re-attributed and lower-cased. Rosenberg "characteristic specificity" appears on neither show-notes page I could read; quote marks removed and replaced by a paraphrase of the page's Key Point.
8. Trend Watch: "November 2025: OBAP launches its open panels" was wrong; the site's 6 Nov 2025 item says "New website/data/code under development. Expected release EoY 2025." Rewritten.
9. DFPS "different data" removed (QuantPedia says only that they built their own cleaned database).
10. "The version a long-only desk could actually hold" (VW single-sort val_ipr, also in the 9B.9 table) was wrong: it is still a decile long-short with a short leg. Replaced by "leans on large bonds".
11. "The one large study of the bond loan market" (Asquith et al.) softened to "the standard large-sample study ... one custodian lender, 2004 to 2007".
12. Within-firm sort definition corrected: the OBAP documentation splits each firm's bonds at the within-firm median signal (long above, short below), aggregated across firms; the chapter had said top-ranked bond versus bottom-ranked bond. For two-bond issuers they coincide; text now says so.
13. "a stop it can size to (Chapter 8-B)" pointed at the wrong chapter; now Chapter 8-D, §8D.5 (Sizing to the Stop).
14. "the survivor Theo had decided in Chapter 4 to trust": Ch 4 leaves the decision open; now "had wanted to build around".
15. PB-03 box: the sentence that the real Ford Credit and GM Financial legs "had printed" low/high lots on one day is an invented illustration about real instruments; now marked "an invented day, not a real print ... in the composite rebuild".
16. Composite labels: Dov Adler and Marcus Oyelaran added to the chapter-opening list of invented persons and to the 9B.7 label line (hard rule: named composites are labelled).
17. Exercise 4: 58% unhedged corrected to 57% (1 - 101.5/238).
18. Pair Book: `state/rv_pair_book.md` row PB-03, "Stressed in" cell changed from "Ch 7-B, 9, 24" to "Ch 7-B, 9, 9-B (§9B.7 data lesson ...), 24"; status stays closed (Ch 24 §24.7). The Brambleworth within-issuer pair in 9B.7 is explicitly unledgered, so no other row is touched.

## 4. Hygiene

Only one code fence, a `text` block (the robot spec); `$` and `$$` delimiters balanced (checked per paragraph after stripping `\$`); currency escaped as `\$` outside math; no `---` lines; last line `<!-- STATUS: COMPLETE -->`.

## 5. Remaining doubtful (not fixable from sources I could reach)

- Figure files `assets/figures/ch09b_two_prices.png`, `ch09b_lib_waterfall.png`, `ch09b_mom6_trimming.png` and `ch09b_two_leg_bounce.png` do not exist yet on disk (figure task still running); the chapter references them. Figure 9B.3 is a four-line schematic of what Fig. 6 shows as bar panels with confidence intervals; the caption says so.
- Dick-Nielsen (2009, 2014, 2019) filter rules still not read; step 1 is attributed to DRR's description.
- JNPS (59 bp / 192 bp, "TRACE plus dealer quotes"), HvZ, IPR, KPP, Menkveld (164 teams), JKP (13 themes, 93 countries), Duarte et al., Ivashchenko-Kosowski, Collin-Dufresne et al. rest on dossier abstracts or Crossref records, not full text.
- "The quarterly WRDS refresh of the TRACE files" (9B.0) is a desk setting I did not verify against WRDS documentation; fictional framing covers it.
- SIFMA's own page snippet was garbled in the search result; Veterans Day full close for 2026 rests on SIFMA's listing plus secondary sources.
- The audit is under revise-and-resubmit and not reproduced end to end by a second team (per the OBAP site and the dossier); numbers may change.
- The chapter says Marcus and Ines are "in contact, Chapter 28": Ch 28 has Ines reading Marcus's review card, which supports it loosely.
- Story-clock conflicts with other chapters (9B runs 9-18 Nov 2026; Ch 19 and Ch 27 run late October) were not examined; the cast bible's Ch 27 dates end 6 Nov.

<!-- STATUS: COMPLETE -->
