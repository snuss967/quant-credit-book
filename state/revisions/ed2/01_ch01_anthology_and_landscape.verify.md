# Verification Report, Edition 2: Chapter 1

Verifier pass on `book_src/01_ch01_anthology_and_landscape.md` (805 lines) against the pre-revision text (`9ac1c37`) and `state/revisions/ed2/01_ch01_anthology_and_landscape.brief.md`. Revision log carried `<!-- STATUS: COMPLETE -->`; no prior verify file existed. Web budget used: 3 of 15 calls (BIS, WealthManagement.com, S&P search); everything else was checked against the named dossiers.

## 1. Nothing removed (python3 comparison, pre vs post)

| Item | Pre | Post | Result |
| :-- | --: | --: | :-- |
| Headings (`#` lines) | 25 | 26 | All 25 kept; the only addition is the restored `## 1.5` |
| Display-math `$$` lines | 22 | 28 | Nothing lost; new blocks are eq. (1.4), (1.5) and the one-factor p(Y) |
| `[SOURCE EXTRACTION]` blocks | 13 | 18 | All 13 verbatim; 5 from restored §1.5 |
| Trend Watch boxes | 4 | 4 | All verbatim (fact-checked hedged wording intact) |
| Exercises | 6 | 6 | Verbatim |
| Appendix F links (`#code-`) | 3 | 4 | 1.1, 1.2, 1.3 kept; 1.4 added for §1.5 (target exists in Appendix F) |
| Resource Graph items | 3 graphs | 3 graphs | All bullets verbatim; all 28 URLs present, none new |
| Poker Table / Desk Myth / Docket Diary / both Spec boxes / both "What ROBO built" | 1/1/1/2/2 | 2/1/1/2/2 | Kept (second Poker Table is the new §1.1 one) |

Paragraph-level diff: 119 of 136 pre paragraphs are verbatim in the post text. The 17 that are not were checked one by one and are accounted for:
- Rewritten as the brief directs: promise paragraph (all five outcomes survive in narrative form), the PJT and SIG walk-through (now Theo's two Mondays), the two assertion paragraphs, the §1.2 intro and table firm column (made generic; every row and every "Forced to Do What" cell kept), the feature list (all six features survive in the Ines/Theo dialogue), the Code Companion stubs (replaced by "Reading Listing" explanations with the Appendix F links).
- Split or moved with nothing cut: "Ways This Blows Up" (CARA formula and the 19% / 3.6x comparison now sit in **The Full Derivation** inside the box), the cold-open numbers (91.97, +5, 15, 8, 5/252, 0.02, 0.25, 0.317, 91.40, pi = 0.6, J = 13, 7.8, 83.60, 78 all present), the Ford paragraph (every fact and citation moved into Acts 2 to 4), "Walk the graph" and the LQD paragraph (kept).
- Credit-triangle, Bolder and Bohn-Stein derivations: kept, with the triangle and p(Y) moved into "The Full Derivation" blocks.
No restoration was needed.

## 2. Facts (new claims about real events, firms, people, dates, amounts)

Checked against dossiers, with web checks where noted. Verified:
- Barclays QPS \$90-140bn; hit rates 58% / 66% / 52% (Impax, 19 Sep 2025): `trend_systematic_credit_industry.md`, and Ch 4 line 105 and Ch 28 line 646 carry the same figures, including the 52%.
- Deutsche Bank Flow, 7 Oct 2025, "nearly three-quarters of all leveraged loans issued": dossier, verbatim.
- Kundu, ESRB WP 141 (Mar 2023), pp. 7-8 (lowest-price CCC haircut); 85c average CCC versus 58c cheapest-in-CLO: dossier rows 48-49.
- S&P, 554 reinvesting US BSL CLOs, 42% above 7.5% CCC, just over 1% failing junior OC, CLO Insights 29 Sep 2023: **web-confirmed** (S&P report of 29 Sep 2023 gives these exact figures; the writer's September date is right and the brief's April date was the earlier scenario paper).
- Jane Street *Signals and Threads* Ep 20 (7 Oct 2024) and Ep 29 (2 Sep 2026) quotes, incl. `uscommoditiesrisk.xlsm` and "along with the time we received it": `life_quant_shop_daily_life.md` lines 63-64, verbatim.
- FINRA Rule 6730 (15 minutes, contra-party and capacity fields, "as/of"): same dossier, section 2.3.
- Rowan quote (9 Feb 2026), Marks quote (*Cockroaches in the Coal Mine*, 6 Nov 2025), Apollo 0-50% LTV wording, Hertz 8-K Ex. 99.1 (\$5.9bn, \$19bn): `perspectives_buyside_credit_managers.md`, verbatim.
- LQD 5.0% / VCIT 3.2% / SPIB 3.1% discounts at the 12 March 2020 close, LQD 0.19% on 13 March: **web-confirmed** at WealthManagement.com (also shows VCIT 0.48% and SPIB 1.5% on 13 March; the chapter does not use those).
- Todorov, BIS Quarterly Review, March 2021 (creation baskets about 20%, redemption 35%, holdings' bid-ask 17x the ETF's, tracking error above 200 bp for some funds in March-April 2020, 0.7 bp): **web-confirmed**.
- Serta: remand 7 Jul 2026, \$261.13mm plus 9% from 22 Jun 2020; \$223.75mm retained value on \$895mm (25 cents); Chapter 11 on 23 Jan 2023 (about 31 months after the uptier); Houston ruling in 2023 (28 Mar 2023, dossier flags CHECK); Fifth Circuit 31 Dec 2024 with "occurs on the secondary market for syndicated loans"; rehearing denied 18 Feb 2025; cert denied 10 Nov 2025; Skadden recoveries 0.6-2.4% versus 100% and about 75%: all in `case_courts_as_regime_variables.md`, `case_lmt_autopsies_us_2020_2026.md`, `trend_re_default_and_recovery_dataset.md`.
- Ford, SMCCF (23 Mar), BB+ (25 Mar), \$36bn, \$90bn / \$48bn / \$197bn, 12 May ETF purchases: unchanged from the pre text, which was already fact-checked.
- Day-of-week claims (12 Mar Thursday, 13 Mar Friday, 23 Mar Monday, 25 Mar Wednesday, 30 Mar Monday, rebalance 31 Mar) checked.
- Every worked number in the Math, Gently boxes and the Ford demo was recomputed: 82.4 for the coin, CE = 0, 0.025 / 0.0127 / 0.19, Bayes 0.031 x 12 x 1.5 -> 0.36, sd 7 for the 2% x 50 jump, 99 for +10% then -10%, 4.5% volatility drag, N(-4), e^-0.02, 120 bp, 12 bp versus 100 bp, 9.7% conditional PD, 12.8 days of volume -> 5.12, 4.87 recovered by day 60, stress dent 10.32 ("more than doubled"). The brief's 83.6 for the coin was an arithmetic slip; the chapter's 82.4 is right.
- Real people: the only named real people are Rowan and Marks (verbatim, sourced quotes) and Hoffstein, Lam, Kamenski, Levine as resource links. No real person has invented dialogue. Fictional composites are labelled: Halvorsen ("fictional"), the cast ("fictional, like everything the cast does"), Quant-Shop Life ("fictional composite"), Ford Long Scene 1, Serta Long Scene 2 ("the dealer, both accounts, every RFQ... are invented, and no real lender is depicted").

## What I fixed (small Edits in the chapter)

1. §1.2 CLO seat: "marginal buyer of the whole loan market" -> "of new leveraged loans" (the 75% figure is of issuance).
2. Act 1, BIS sentence: "sector average of 0.7 bp" -> "historical average of 0.7 bp" (the BIS wording).
3. Act 2: "crossover funds that had already spent their dry powder, and dealers whose balance sheets were full" -> stated as the model's assumptions (no source supports it as fact).
4. Act 1: Kaz's "the most liquid IG product in the world" -> "one of the most liquid".
5. §1.7 opportunistic seat: "this is who buys it" hedged to "the kind of buyer that can take it", and the Hertz example labelled as a plan sponsor, not a buyer from forced sellers (the dossier says Apollo bought equity of a solvent estate and was not a creditor).
6. Serta scene, second account: made explicit that it was a fund "pitched the Serta deal and passed", so the fiction implies no real participant traded while restricted (matches Mags's own caveat).
7. Serta closing note: removed "Serta's lender base was fragmented and CLO-heavy, with no co-op among the lenders who were left behind" (unverified); replaced with the sourced fact that the left-behind lenders went to court afterwards as plaintiffs. The cooperation-agreement counter stays at 0.

## 3. Hygiene

No code fences of any kind; display `$$` balanced (28 lines, 14 blocks); no odd inline `$` in any paragraph; no stray unescaped currency `$` (every currency amount is `\$`); no `---` line adjacent to text (all nine are surrounded by blank lines); no em dashes; no leftover `EXPLAIN` stubs; last line is `<!-- STATUS: COMPLETE -->`. Four `\$` inside math spans (`\$15\text{ million}`, `1/(\$\text{mm}\cdot\text{pt})` x3) are valid and pre-existing.

## What remains doubtful

- **Appendix F, Listing 1.2** still carries the stray §1.5 prose (a second `## 1.5 ...` heading with the Source Extractions) and a duplicate of the §1.5 code, as the revision log warns. Outside this chapter, so not touched; it should be trimmed.
- The "Ad Hoc Group, the book's Greek chorus" lines (pre-existing Docket Diary quip and the new 2 p.m. parenthetical) put invented words in the mouth of a group name that is also a real Serta term. They are labelled as the book's chorus; left as is, but a stricter reviewer may want "fictional" added.
- Serta items rest on the dossiers (Mayer Brown July 2026 summary, not fetched here): the \$261.13mm, 25-cent valuation and 18 Feb / 10 Nov 2025 dates. The Houston ruling date is hedged to "2023" (dossier CHECK on 28 Mar 2023).
- Docket Diary says \$734mm of second-out; Ch 5 says about \$875mm. They reconcile (first-lien participants' share versus all second-out issued) but Ch 1 does not say so; the Diary is protected, so I did not add a clause.
- The Bayes box reuses Exercise 2's exact inputs (as the brief required), which spoils the exercise; the later quality read suggests different numbers. Left for the fixer pass, along with the structural issues it lists (repeated tellings, box clustering, templated "When to reach for it" passages, 26,700 words against 9,900).
- Kundu and Deutsche Bank Flow were checked against the dossier only (the S&P and BIS items were web-confirmed).
- Serta NY suit date was never verified and is correctly omitted.

<!-- STATUS: COMPLETE -->
