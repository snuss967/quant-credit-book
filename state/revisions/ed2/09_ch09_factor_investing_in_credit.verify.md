# Verification Report, Edition 2 (U2): Chapter 9, Factor Investing in Corporate Credit

Verifier pass on `book_src/09_ch09_factor_investing_in_credit.md` (30,784 words; revision log STATUS: COMPLETE confirmed before starting).

Baselines used. The pre-revision text named in the task, `git show 9ac1c379:...`, is 15,061 words and predates the five figures. The brief's baseline (19,091 words, Figures 9.1-9.5 in place) is commit `796815d`. Check 1 was run against both; Check 2 (new claims) was run against `796815d`, so figure captions are not counted as writer additions.

## 1. Nothing removed (python3 comparison)

| Item | Pre | Post | Result |
| --- | --- | --- | --- |
| Headings (lines starting `#`) | 40 | 47 | none missing or renamed; 7 new (4 x `The Full Derivation` in 9.2.1, 9.3.3, 9.7.1 and 9.9; `Long Scene: 2022...`; `Long Scene: March 2020...`; `Filters, survivors, and the build that went red`) |
| Display-math blocks (`$$` count) | 56 | 62 | all 28 pre blocks present; 3 pre blocks that carried tags (9.1, 9.2, 9.5) are now a one-line tagged statement plus the untagged full chain under `The Full Derivation`; tags 9.1-9.6 each appear exactly once |
| `[SOURCE EXTRACTION]` blocks | 15 | 15 | all 15 lines verbatim, page cites intact (Paleologo p.27, p.71; Ben Dor p.34, p.118; Dynkin p.524, 553, 610, 633, 679, 711, 741; Man p.25, 26, 27, 28) |
| Trend Watch boxes | 3 | 3 | all three byte-identical (cost curve, tight-spread regime, market share); moved to section ends as briefed |
| Desk Myth / Poker Table / Ways This Blows Up / Spec You Hand boxes | 2/1/2/1 | 2/1/2/1 | all byte-identical |
| Exercises | 6 | 6 | tail from `### Exercises` through the Resource Graph is identical |
| Deep-Dive Resource Graph items | 30 | 30 | identical |
| Appendix F links (`#code-9-1` to `#code-9-7`) | 7 | 7 | all present, anchors exist in App F |
| Figures 9.1-9.5 | 5 | 5 | present, files exist in `assets/figures/` |
| Telecom case, Listing explanations, Debrief bullets and scene | | | untouched apart from briefed bridge sentences |

Paragraph-level pass (every pre line not found verbatim in post, 49 lines, each inspected). All are intended rewrites or carried facts: the six learning-objective bullets (retired per brief; every objective is in the new one-paragraph preview); Facts one/two/three (all figures and the Dynkin p.633 cite kept); the six optimizer constraints (all six are rows of the owner table, Ben Dor's 1% versus 0.33% quote kept, with eight more rows added); the five replication rules (now the whiteboard); old Sec 9.5.3 and the three March 2020 case-study paragraphs (every fact and cite is in Scene B or Scene A: Agg -13%, HY -11%, the 2025-26 Robeco attribution, spreads tripling to nearly 400bp and HY past 1,000bp, Man p.12 and p.20, Dynkin p.739-741, p.711, p.703, Man p.30 PGGM/IPE survey; the "First... Second... Third" paragraph's three points are the grading); the "Three notes" lab paragraph (all three notes kept); the Sal spreadsheet line (kept and expanded). Nothing needed restoring.

## 2. Facts

Every new claim about real events, firms, people, dates, amounts or rulings was listed from the post-minus-pre line diff and checked against the PDF page texts in `state/pdf_pages/`, the dossiers the brief names, or the web (9 web calls of 15; primary sources first).

Verified against primary or page text:
- Dynkin p.703: IG LCS 0.608% and HY 0.941% at 31 Jul 2019; 0.4% (2007), 2.8% (2008), 0.6% (2018-19). Dynkin p.545: ESP outperformance "is larger when there is a high dispersion in ESP".
- Man 2022: p.8 ($116.5bn on Open Trading by quant funds, first three quarters of 2020, +150%), p.11 (daily prime-broker borrow feeds), p.12 (IG spread chart), p.19 (both quotes verbatim: dealer runs "not firm and actionable"; "if filled" indictment), p.20, p.30.
- Man 2023 (Lam and Kamenski, June 2023): p.3 quotes verbatim (portfolio-trading costs up in H1 2022, dealers committing less balance sheet, loss of customised ETF baskets; 30%/60% to over 90% electronic, as of 1 May 2023); p.5 "vast majority of our trades" are RFQs.
- BlackRock Systematic HY p.3-4: S&P -18%+, HY -11%+, Agg -13%+ in 2022 and "fastest rate hiking campaign in decades"; 2023 HY +13%+, Agg +5%+; eVestment +0.47% (2022) and -0.68% (2023).
- Federal Reserve press release, 9 Apr 2020 (federalreserve.gov): "These three programs will now support up to $850 billion in credit". The three are PMCCF, SMCCF and TALF. **Fixed:** the draft said "the programs were expanded to support up to $850 billion", which read as if the two corporate facilities alone were meant. Now says the Fed expanded the corporate facilities and that they, with TALF, support up to $850bn.
- SEC press release 2025-15 (sec.gov), 16 Jan 2025, Two Sigma: "in or before March 2019" vulnerabilities identified; "waited until August 2023"; "unauthorized changes to more than a dozen models"; $90 million civil penalties; $165 million repaid. All as the vignette states them. No invented words for any Two Sigma person.
- Ares/BlueCove (web search of Business Wire, fi-desk, Alternative Credit Investor): minority stake 2023 ($1.8bn AUM then); agreement announced 29-30 Oct 2025; $5.5bn at 30 Sep 2025; about 60 professionals; Ares Systematic Credit under Alex Khein; completion announced early February 2026. **Fixed:** the draft gave "Business Wire, 2 February 2026"; the wire's dateline appears as 3 Feb while the URL id reads 20260202, and the page could not be fetched (403), so the day is removed ("early February 2026").
- Dossier-verified (`perspectives_dealers_and_systematic_shops.md`, `life_quant_shop_daily_life.md`, `trend_systematic_credit_industry.md`, `papers_factor_replication_crisis_and_bond_data.md`): AQR Palhares and Richardson (FAJ 76(2), 2020, pp. 82-102, both quotes; sample counts correctly omitted) and J. Fixed Income Winter 2019 quote; AQR white paper simulated through CDS and CDS indices; Robeco van der Linden and Houweling 7 Sep 2026 (three quotes verbatim, 1,600 and 2,600 issuers, more than 20 analysts, quant fixed income since 1995); Robeco fund launched 15 Jun 2015 (pre text); Ramji 12 Mar 2020 (LQD almost 90,000 trades, five largest holdings 37 times), paraphrased without quote marks; Bank of England ETFs more than 5% below NAV; NY Fed Terms of Assignment 27 Mar 2020; Kargar, Lester, Lindsay, Liu, Weill, Zuniga NBER 27355 quotes; D. E. Shaw "$400 million in CAS and STACR", "redemption requests and margin calls", 2001 versus 2008 (also in Ch 4-C); Blackstone/DCI 2020 (FY2025 10-K); Dimon letter 4 Apr 2023 pp. 22-23; Open Bond Asset Pricing pipeline (five stages, stages 0-1 on WRDS, ratings omitted from public Stage 1, about 5 hours and 5 GB, v4.2.1, Sept 2026, paper under review); Dickerson, Robotti, Rossetti (432 = 108 x 2 x 2; 119 and 65 at t > 1.96; 26 FDR survivors, 25 within-firm; IA.3).
- Knowledge-checked: Fed first hike 16 Mar 2022 (first since 2018); 19 Mar 2020 Thursday, 23 Mar Monday, 12 Mar Thursday, 30 Dec 2022 Friday, 2 Mar 2020 Monday; 2022 front-end Treasury yields up more than two points; 2023 yields ended near the start; math in all Math, Gently boxes (N(-1.93) = 2.7%, 0.8^3, ln 2/ln(1/0.8) = 3.1, 2.2/sqrt3 = 1.27, ln(300/220) = 0.31, 4%/12/0.40 = 0.83%).
- Cross-references checked against `book_src/`: Ch 1 sec 1.8.2 (Ford and March 2020), Ch 1 coffee-cooling and regression-slope boxes, Ch 4 fundamental law with issuer clustering, Ch 5 lognormal and Ito box, Ch 6 sec 6.1-6.3, Ch 7 hats and FDR box, Ch 8-B quadrature box, Ch 8 sec 8.8, Ch 12 sec 12.7 shadow-price box, Ch 13 drop-down material, Ch 20 sec 20.5 ("only price in town", same 19 Mar 2020 date), Ch 22 borrow-fee scene, Ch 4-C D. E. Shaw story. All exist.

Hedged or softened:
- AQR box: "regressed ... returns on the market and on a set of systematic credit factors" became "measured ... exposures to the credit market and to a set of systematic credit factors" (the method beyond the abstract is unverified).
- Insurer box: "holds most of its bonds to maturity" became "tends to hold its bonds to maturity"; "does not mark its book to the screen" became "does not need to mark...". The generic-seat framing is kept.

People and dialogue. No real person has invented dialogue or invented quotes. Real quotations (Dimon, Palhares and Richardson, van der Linden and Houweling, Lam and Kamenski, Kargar et al., D. E. Shaw, Ares, BlackRock) are verbatim from published documents and cited. Ramji, the Man March 2024 recording and Two Sigma staff are paraphrased or reported from the SEC order, with no quote marks on machine-transcript material. Mags's joke naming Dickerson, Mueller and Robotti is pre-existing and puts no words in their mouths. Fictional composites are labeled: Scene A, Scene B, the CI vignette ("A fictional week at a systematic asset manager"), the 8:10 sale ("a composite; the bond, the sizes and the fills are invented"), the paper rebalance, Theo's runway run, and the Dov Adler/Vantress Pair Book scene. The sponsor-owned company in Theo's pitch-book anecdote is generic. Kaz pronouns (they/them) are consistent throughout.

## 3. Hygiene

- Code blocks: exactly one fence pair, the pre-existing ```text spec block in "The Spec You Hand the Robot" (a text prompt, not code). No other fences.
- Math: 62 `$$` (even), no display block left open, no line with an odd number of unescaped inline `$`, no inline span containing prose; currency written `\$` throughout (no bare `$20mm`-style leaks).
- No `---` lines anywhere in the chapter; no CHECK/TODO markers; no two boxed elements in a row (36 blockquote boxes, none adjacent); 8 Math, Gently boxes (cap 10).
- Last line is `<!-- STATUS: COMPLETE -->` and it appears once.

## Fixed in the chapter (4 small edits, 3 lines)

1. Fed 9 Apr 2020 $850bn attribution (CCFs plus TALF).
2. Ares completion citation: day removed.
3. AQR method description softened.
4. Insurer seat: two absolutes softened.

## What remains doubtful

- Dimon "fair-weather friends" quote and pp. 22-23: verbatim in the dossier from a fetched letter; my web search did not surface the letter text and the annual-report PDF exceeded the fetch limit. Treat as dossier-verified only.
- Robeco 30 Sep 2026 attribution wording and "as the long end rallied" are pre-existing text cited to the fund page; I did not re-fetch the page. The Scene B claim that 2025-26 saw a long-end rally is the brief's framing, not independently checked.
- Bank of England ETF discount ("by the middle of the month") rests on the dossier's secondary source (Investment Executive); the 12 March LQD figures rest on a machine transcript of the Q1 2020 call, paraphrased.
- Scene B cut date is Fri 30 Dec 2022, not 30 Jun 2022 as the brief said. The log's reason (full-year sourced numbers; Ch 11 sec 11.2.3 already owns a 30 Jun 2022 replay with this cast) holds up, and the cast bible was updated. The orchestrator should note the deviation.
- Story-time: the brief says Theo's week three; the cast bible's Ch 27 line puts Tue 29 Sep in Theo's second week. The chapter itself says only "the last Tuesday of September" and is internally consistent.
- The Hana/CI-job dates (Mon-Fri week, v4.2.1 pin) are fictional-week framing around verified public facts and are labeled so.
- Five additional figures in brief section 3 (march2020_factor_lens, lowrisk_total_vs_excess_2022, measure_trap, fdr_survivors, buffer_hysteresis) are not drawn; deferred to U4. The 2022 figure should show the sleeve as long-only, DTS-matched, with a duration gap, cut at year-end.

<!-- STATUS: COMPLETE -->
