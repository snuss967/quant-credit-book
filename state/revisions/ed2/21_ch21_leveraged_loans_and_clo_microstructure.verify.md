# Verification Report, Chapter 21 (Edition 2, U2 revision)

*Verifier pass, 18 Oct 2026. Pre text: `git show 9ac1c379053d9d0254e9d524d9a40efdec4a2c71:book_src/21_ch21_leveraged_loans_and_clo_microstructure.md`. Post text: `book_src/21_ch21_leveraged_loans_and_clo_microstructure.md` (about 191k characters against 90k). Revision log was marked `<!-- STATUS: COMPLETE -->` before this pass started. Web calls used: 7 of 15.*

## 1. Nothing removed

Checked with python3 (normalized text comparison, pre against post):

| Item | Pre | Post | Result |
| :-- | :-- | :-- | :-- |
| Headings (lines starting with `#`) | 36 | 50 | All 36 present; 14 new (ten "The Full Derivation", Long Scenes A and B, two "The Pair", Quant-Shop Life) |
| Display-math blocks (`$$` pairs) | 26 blocks (52 `$$`) | 26 blocks (52 `$$`) | Every pre block present verbatim; equation tags (21.1)-(21.10) all present |
| `[SOURCE EXTRACTION]` blocks | 9 | 9 | All verbatim except the Schmid p.177 Annotation (the sanctioned CHECK hedge, "as S&P's April 2025 CLO index put it") |
| Trend Watch boxes | 4 | 4 | Present; settlement box differs only in the source tag "(LSTA slides; CHECK)" to "(LSTA slides; approx.)", as the brief ordered |
| Exercises | 6 | 6 | Verbatim |
| Appendix F links (`#code-21-1` to `-5`) | 5 | 5 (11 references) | None missing |
| Resource Graph URLs | 25 | 39 | None missing; 14 added by earlier passes |
| Desk Myth, Poker Table, both Ways This Blows Up, Serta Docket Diary, ZAIS6 arithmetic, Spec, JAAA Case Study | present | present | Verbatim |
| Figures 21.1-21.5 and captions | n/a | 5 | Present. The pre commit predates the figures pass, so they are not "removed" anywhere |

Differences that are not removals, noted for the record:
- The five `Code Companion` boxes of the pre text were replaced by explanatory prose plus `*The full listing is [Listing 21.n in Appendix F](#code-21-n).*` in the earlier U1 pass; every link survives.
- The pre closing Resource Graph bullet "Bloomberg *Odd Lots*... we do not cite an episode we have not verified" and the separate LSTA settlement-study bullet were replaced or merged by the earlier media and Resource-Graph upgrade pass (commit `cea2d0d`), not by this revision. The settlement-study URL is still in the (21.2) graph and the closing graph.
- Pre paragraphs that died into scenes (cold-open bullet list, the 21.1 bullets, "Why is it slow?", the March 2020 and 2025 window case-study paragraphs, the "hazard itself" feature list, the Weil bullets) have their facts in the new scenes; I checked each number against the scene (see section 2).

Nothing needed restoring.

## 2. Facts

New claims (sentences not in the pre text, found by difflib/regex by section) about real events, firms, people, dates and amounts, and how each was checked:

| Claim in the revision | Check | Result |
| :-- | :-- | :-- |
| Sep 2026 CLO activity \$41.1bn / 92 deals / \$13.8bn new issue / refis above resets first time since April (Trepp via CRE Daily, 14 Oct 2026) | Dossier `trend_loans_clos` row "Sep 2026" | Confirmed |
| Voya IM 12 Oct 2026 ratings decompression, BBs firm, CCCs weaker | Dossier row 2026-10-08/12 | Confirmed |
| 21.7% above par end-June 2026 (Eagle Point N-CSRS); 58% at year-end | Dossier | Confirmed |
| Octaura May 2025 cost to sell 23c to 9c, cost to buy 13c; Mar 2025 70% sellers; Apr 55% sellers, -1.85 points, VIX mid-40s; Jun 72% buyers | Dossier (Octaura "On the Blotter: 2025 in review") | Confirmed. The Edition 2 brief's crowd-side wording was already corrected by the writer |
| Octaura CFO 7.51% exit June 2026; CLO platform Sep 2025; Live Feedback Feb 2026 | Dossier | Confirmed |
| Versana "put amendment and consent voting on a live digital platform in October 2026" | Dossier says Versana *announced* a platform on 5 Oct 2026 (vendor site) | **Fixed**: now "announced in October 2026 a live digital platform for amendment and consent voting *(vendor-reported)*"; §21.8 Annotation reworded to "the agent-bank voting data its platform says it will carry" |
| LSTA delayed-comp protocol: Phase I 1 Sep, Phase II 1 Nov 2016; buyer signs by T+5, picks settlement T+7 or earlier; median T+12 to T+9; 23% to 37% within T+7 | Fetched Markets Media (2 Nov 2016) | Confirmed |
| Shop-life: signing on T+6, one day past T+5, leaves the seller owing nothing | Law-firm summaries of the 2016 rules (search): loss of delayed comp applies after the seller's failure notice and a missed T+5 | **Fixed**: added that the seller's closer had sent the failure notice that starts the clock |
| Bloomberg 30 Jan 2025: banks pitching repricings timed to soft-call expiry, offering to do deals for free | Search found the BNN Bloomberg syndication, headline "banks offer to do deals for free in hectic leveraged loan market" (only the excerpt seen) | **Fixed**: "timed to the day each loan's soft call expired" overstated; now "timed to each loan's soft-call expiry" |
| 2 Apr 2025 tariff announcement; 7 Apr 2025 a Monday; replay dates 16, 23, 26, 27, 30 Oct 2026 and 8 Oct 2026 weekdays | Calendar computed | Confirmed |
| Scene A: 29 Feb 2020 95.18, 23 Mar 2020 76.23, -12.4% (second to Oct 2008 -13.2%), distress ratio 57%, 82.9 by 31 Mar, "beyond 300 basis points" 19 Mar; 20 Mar 2020 a Friday, 23 Mar a Monday | Same figures stood in the pre text (earlier fact-check); dates by calendar | Confirmed as carried over |
| Scene A: junior OC cushion fell to 1.13%; CCC exposure peak 12.31% (S&P, 28 Apr 2023) | Search of the S&P article: "a low of 1.13% in 2020" for the average junior O/C cushion of *pre-pandemic* CLOs. The 12.31% could not be matched (S&P page returns 403; a 2022 S&P piece gives a pandemic peak of "12%") | **Fixed**: now "S&P put the average junior OC cushion of pre-pandemic CLOs at a low of 1.13% in 2020". 12.31% left as in the pre text and the protected Desk Myth (see doubtful) |
| Scene A numbers: \$87mm mark-to-market loss, numerator -\$0.6mm, cushion 3.4 to 3.3, 15 loans / \$30mm into CCC, excess \$4.8mm to \$34.8mm, numerator -\$12.7mm, junior OC 107.3% to about 104.5% | Re-ran the Appendix F Listing 21.1 engine on the scene's marks | Matches, except the writer's "about \$85mm" loss; the run gives \$86.8mm. **Fixed** to \$87mm |
| Box 4: "$11 \times 0.50 \approx 5.6$" | 1/0.09 = 11.1; 11 x 0.5 = 5.5 | **Fixed** to 11.1 |
| Box 5 (diversity): variance 529, DS 29.5, ceiling 33; Box 8 (hazard): 101.36 / 100.45 / 100.12, e^-0.5 = 61%, 37%, under 2%, 38 bp; Box 1: 2.69 and 1.35; Box 3: about \$97 a day, \$2,100, \$1,800; Box 10 | Recomputed | All correct |
| Scene B: 62% above par Dec 2024, \$215bn Jan, 83% Octaura, \$109.2bn April, \$119.3bn March 2020, 8%, 37%, 97.6 by 24 Jul | Carried over from pre text (already fact-checked) | Confirmed as carried over |
| Scene B: "index line, which had fallen through par" | Index average bid ended 2025 at 97.08 (dossier); it was never above par | **Fixed**: now "the share of the market bid above par, which had been shrinking since January and kept shrinking" |
| Case study: bank-loan funds lost several percent "in the second week of April" | Fed FEDS Note window is 2-9 April 2025 | **Fixed** to "between 2 and 9 April" |
| Box B: Loomis Sayles Q4 2025 quote ("we do believe the risk of liability management exercises will remain elevated as not all these maturities are refinanceable"); JAAA 62.1 / 9.0 / 28.9% by deal vintage (Octus 7 Jul 2026) | Dossier `perspectives_buyside_credit_managers` (quote verbatim; CLO-manager status unverified, and the chapter says "a large loan manager"); dossier `trend_loans_clos` for the Octus split | Confirmed |
| Box C: NAIC dates 23 Jun / 30 Jun / 8 Jul 2026, YE2026 effective, AAA about a quarter of a AAA bond, BB+ 15.1% vs 3.15% (4.8x), 11.77-point surcharge on BSL tranches 2.C or below and 4% thick or less, MM CLOs excluded, residual 45%, measured on latest trustee report | Dossier `trend_insurance_capital_forced_flow` rows of 2026-06-23 | Confirmed. Citation "Mayer Brown, 1 Jul 2026" was seen only as a search result per the dossier: **removed**; the caption now says "a law-firm note" |
| PB-17: Table 8.3 levels (10-year 4.20% on 2 Apr, 4.01% on 4 Apr, 4.15% on 7 Apr, 4.48% on 11 Apr; HY OAS 461 bp on 7 Apr; 2.96% on 30 Jun) | Chapter 8 Table 8.3 and Chapter 10 text | Confirmed (-19 bp, +33 bp). "Loan discount margin of about 520 bp" is not FRED data: **fixed** to "an assumed loan discount margin" |
| PB-17: sizing arithmetic (2.7 x 520 about 1,400 and 3.2 x 461 about 1,475 bp-years; \$47.5mm HYG; carry \$4.0mm less \$2.85mm; \$0.14mm at 30 bp) | Recomputed | Correct, labeled illustrative |
| PB-15 Trinseo: 8 Sep 2023 "a senior secured term loan facility of \$1,077 million" by two SPVs, \$948mm on-lent, no consent | Ch 13 §13.7.1 and dossier `case_lmt_autopsies_us_2020_2026` §7 | Confirmed |
| PB-15: 17 Jan 2025 about \$447mm of unsecured notes became second-lien, intercompany +\$494.5mm to about \$1.5bn, SPV votes counted | Dossier and Ch 13; web search of Trinseo's 15 Jan 2025 result release: \$446.5mm (99.88%) of the 5.125% senior notes due 2029 tendered for new 7.625% second-lien notes due 2029 | Confirmed; the "paper the old unsecured notes had become" is correct |
| PB-15: Ch 11 on 26 May 2026; recoveries OpCo 2028 TL 2-9%, 7.625% 2029 notes 0%, Super HoldCo 60-78%; RSA about 86%; CastleKnight group about 40% of the 2028 loans, sued | Dossier §7 and Ch 13 | Confirmed (an allegation is labeled as such) |
| PB-15: borrow cost 173 bp before and 245 bp after bankruptcy (Asquith, Au, Covert, Pathak 2013) | Dossier `rv_credit_pairs_literature_and_mechanics` R11 | Confirmed |
| PB-15 arithmetic: \$4mm each way at recoveries 70 and 10; loss about \$12mm on 2-9 recoveries | Recomputed | Correct |
| Kirschner v. J.P. Morgan Chase (2d Cir., 24 Aug 2023) | Carried over from pre; known date | Confirmed |

Real people and dialogue: no real person speaks invented words. Quotes attributed to real parties (Loomis Sayles letter, TwentyFour, Weil memo phrases, Moyer, Schmid, Duffie, LSTA and Fed phrases) are verbatim from the dossiers or the pre text. All speaking characters (Ines, Mags, Theo, Kaz, Hana, Dov Adler of Vantress, Ilse Varga) are fictional, and the fiction is labeled at the head of each scene (cold open, 21.1, 21.2.1, Scene A, Scene B, shop-life, Pair boxes, §21.8 scene, Debrief). Desk numbers carry "(illustrative)". Character continuity checked against the cast bible: Theo ten weeks into PJT in March 2020 (joined Jan 2020), Mags at a bank in March 2020, Kaz they/them throughout, the Kroger replay about three weeks before 14 Oct.

## 3. Hygiene

- No code fences anywhere (no ```text diagrams either).
- `$$` count 52 (balanced); no odd inline `$`; braces balanced in every display and inline block; the one `cases` environment closes; no unescaped currency found.
- No `---` lines at all, so none directly before text.
- No CHECK, TODO or "via search" left in the reading text (the six hedges are logged in `state/research/open_items_ch21_ed2.md`).
- Last line is `<!-- STATUS: COMPLETE -->` (single occurrence, file ends with a newline).

## Fixed during this pass (all small edits in the chapter)

1. Box 4: 11 x 0.50 changed to 11.1 x 0.50 (5.6).
2. Scene A: market-value loss \$85mm to \$87mm; 1.13% cushion re-attributed to pre-pandemic CLOs.
3. Scene B: "index line fell through par" replaced by the above-par share; Bloomberg wording tightened; case-study date window "2 and 9 April".
4. Versana: "announced ... (vendor-reported)" in §21.2.3, and the §21.8 Annotation.
5. Shop-life: failure-notice condition added to the T+5 rule.
6. PB-17: loan discount margin marked as assumed.
7. Insurer box: removed the unverified Mayer Brown citation.

## What remains doubtful

1. **"Twenty-three business days" (cold open, §21.2 seat, the Debrief's "day twenty-seven").** 11 Sep to 14 Oct 2026 is 23 weekdays only if Monday 12 Oct 2026 (Columbus Day, a Federal Reserve holiday) counts as a business day. Under a New York banking-day definition it is 22. Left as the brief set it; the figure is a fiction device, but a pedant may count.
2. **S&P 12.31% CCC peak** (Scene A, Desk Myth, Poker Table). Could not be matched online (S&P page returned 403; one S&P piece gives about 12%). Carried over from the pre text.
3. **Bloomberg 30 Jan 2025** "banks offer to do deals for free": only the headline and excerpt were reachable, not the article body.
4. **Name collision.** `state/cast_bible.md` lists Ilse (she/her) as a data engineer at a fictional shop (Ch 27 vignette); Ch 21's shop-life makes "Ilse Varga" a risk analyst at a different fictional shop. Either rename one or have the cast bible record two people. Not changed.
5. **Octaura and Versana figures** are vendor-reported; the Versana item is an announcement, not evidence of adoption.
6. The six items in `open_items_ch21_ed2.md` (LSTA 20-day chart, Octus >30% software, "came to a halt in March" source, SEC withdrawal, Beyhaghi-Ehsani sample period, S&P April 2025 cushions) are still open; none was closable in this pass.
7. Scene dates 23, 26, 27 and 30 Oct 2026 lie after the date of this pass (18 Oct 2026); they are fiction, and no real-world fact is attributed to them.

<!-- STATUS: COMPLETE -->
