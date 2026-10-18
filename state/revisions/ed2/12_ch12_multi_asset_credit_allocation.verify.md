# Verification Report, Edition 2 (U2): Chapter 12, Multi-Asset Credit Allocation

Chapter: `book_src/12_ch12_multi_asset_credit_allocation.md` (30,300 words after revision; 13,093 in the pre text at commit 9ac1c37). Revision log: COMPLETE. Pre text diffed from `git show 9ac1c379053d9d0254e9d524d9a40efdec4a2c71`. Note: the pre-to-post diff also contains the earlier figures, resource-graph (U3b) and red-pen C11 passes, which have their own logs; those are listed below as out of scope except where a spot check was cheap.

## Check 1. Nothing removed

Method: python3 comparison of headings, `$$` blocks, boxes, URLs and line-level text between pre and post (normalized whitespace).

| Item | Pre | Post | Result |
| :--- | :-: | :-: | :--- |
| Headings (lines starting `#`) | 22 | 38 | None missing; 16 new (Full Derivation subsections, scene and vignette headings) |
| Display-math blocks (`$$ ... $$`) | 23 | 24 | All 23 found verbatim in post; the 24th is the red-pen C11 total-return covariance with the cross term |
| `[SOURCE EXTRACTION]` blocks | 15 | 15 | All verbatim, annotations included |
| Trend Watch boxes | 4 | 4 | All four verbatim (positions moved to section ends as briefed; the "7" in a raw count includes cross-references) |
| Desk Myth box | 1 | 1 | Verbatim |
| Ways This Blows Up boxes | 3 | 3 | Verbatim |
| Exercises | 6 | 6 | Verbatim, none solved by a box |
| Appendix F links `#code-12-1` to `-5` | 5 | 5 (14 occurrences) | All present; the five "Code Companion" stubs became scene-opened explanations ending "The full listing is Listing 12.k in Appendix F" |
| Resource Graph sections | 3 | 3 | All present; every pre URL is still present (0 missing). Channel-level placeholders (Odd Lots, Flirting with Models, Capital Allocators, Credit Edge, "no episode verified") were replaced by specific episodes in the earlier U3b pass |
| Figures 12.1 to 12.5 with captions | 5 | 5 | Present |
| Equations (12.1) to (12.4) | 4 | 4 | Present, text unchanged |

Paragraph-level residue: 53 pre paragraphs are not verbatim in post. I checked every one: each is either (a) a derivation moved under "The Full Derivation" with light connective edits, (b) a list or case-study paragraph rewritten into scene or vignette form with its facts intact (First Brands/Tricolor facts, Cambridge/KBRA, JPMorgan charge, Dimon quote, the damage-control logic, the three April 2025 lessons, the four regime-model errors, Rule 22e-4 buckets and dates, CCC break-even 19.7%, 7.5% CLO haircut), or (c) the intended deletions (the "By the end of this chapter you will be able to" list, now two sentences plus the Finder table; the double-counted Case B paragraphs, now a stub pointing to the scene). A token-level check (numbers and capitalized names in pre but absent from post) found only the First Brands/Tricolor dollar prices written as "96", "11", "105", "12.50", "70s" without the escaped dollar sign, and "Bloomberg Odd Lots" placeholder text. Nothing restored; nothing needed restoring.

One wording item noticed and left alone: the protected heading "Seven Piles, One Bet" and Ines's "Seven piles" line (pre text) sit beside "five of the eleven tabs" in §12.1; that is pre-existing and not a fact error.

## Check 2. Facts

New factual claims were collected by reading the whole post chapter against the pre text (python3 sentence diff by section, then a full read), then checked against the dossiers the brief names (`trend_private_credit_marks_and_redemptions_2025_2026.md`, `perspectives_buyside_credit_managers.md`, `perspectives_dealers_and_systematic_shops.md`, `trend_figure_data_series.md`, `trend_electronification_pt_etf_liquidity.md`, `trend_part_v_market_structure_2026.md`), FRED, and the web (7 calls used of 15).

### Verified against primary or dossier

| Claim (location) | Status |
| :--- | :--- |
| CoCo write-down on Sunday 19 March 2023, Credit Suisse (§12.0) | Correct (FINMA AT1 write-down announced Sunday 19 March 2023) |
| Recoveries 52/39/33 (Cai and Haque, FEDS Notes, 23 Feb 2024) | Pre text, matches dossier |
| NAIC June 2026 CLO C-1 factors, effective RBC reporting at 31 Dec 2026; 45% residual charge kept; 11.77% pretax surcharge on below-IG BSL CLO tranches 4% thick or thinner (Sidley note, 9 Jul 2026) | Verified by fetch of the Sidley note (adopted 23 Jun 2026 call; BSL only; thickness 4% or less) |
| Carlino, Foley-Fisher, Heinrich, Verani, FEDS Notes, 21 Mar 2025: "a record $212 billion by the end of 2023"; B-rated portfolio capital cut by two-thirds via CLO stack | Verified by fetch (authors, date, both statements; the second quote's full wording is from the dossier's earlier fetch) |
| First Brands: 28 Sep 2025 filing, about $5bn sales, $12mm cash, over $9bn liabilities; TL 96 on 4 Sep, 11 on 14 Oct; $5.5bn loans | Dossier row (and pre text) |
| Tricolor Chapter 7; AAA tranches in the 70s; lower tranche 105 to 12.50 (MacKay Shields 4Q25) | Pre text / dossier |
| JPMorgan about $170mm Tricolor charge; Dimon "When you see one cockroach, there are probably more", 14 Oct 2025 call | Dossier (Fortune/CNN) |
| OBDC/OBDC II merger proposed 5 Nov 2025; about 98% overlap because the adviser allocated the same investments to both since OBDC II's inception; NAV-for-NAV exchange ratio; OBDC II filled every prior tender; terminated "due to current market conditions" | Dossier plus web: 8-K says termination effective 18 Nov 2025, press release and 8-K filed 19 Nov. **Fixed** the citation wording (see below) |
| Marks memo "Cockroaches in the Coal Mine", 6 Nov 2025; "The worst of loans are made in the best of times" | Dossier (buy-side perspectives, memo table) |
| Fed FSR Nov 2025 "isolated events"; May 2026 Box 4.1 figures and "first time" line | Already in the Trend Watch (protected, earlier fact-check); cited once in Beat 4, once in Trend Watch |
| Cambridge Associates / KBRA 1.5% vs 3.8% | Pre text |
| Early-Feb 2026 AI-tool software sell-off; Blue Owl down as much as 13%; Ares, KKR, Blackstone, TPG, Apollo vehicles down 8-10% | Dossier, trade press (Alternative Credit Investor, 4 Feb 2026); chapter says "trade press reported" (hedged) |
| BIS (Quarterly Review, March 2026): over $500bn to software borrowers, 19% of direct loans; software equities down almost 30% Oct to Feb, BDC shares about 10% | Dossier |
| 18 Feb 2026: $1.4bn loans sold at 99.8% of par to pension and insurance buyers, $600mm from OBDC II, fairness opinion; OBDC II ends tenders; revolver $225mm to $75mm; OBDC bought back $148mm of stock at 86% of book | Dossier (OBDC II 8-K, OBDC Q4) |
| HPS Corporate Lending Fund Q1 requests about 9% of shares, paid a little over half (9.2%, 54.0%); OCIC 21.9%; OTIC 40.4%; Q4-cycle HLEND 4.1% filled in full, OTIC 15.4% | Dossier ("computed"); chapter says "as we read them" and "our computations" |
| Cox Capital (Saba-affiliated) tender at $3.80 from 6 Mar 2026, 31.8% below $5.57 NAV (computed), all tendered shares taken; return of capital $2.50 + $0.42 = 35% of NAV | Dossier. **Fixed** the base of the 35% (it is of the $8.27 start-of-quarter NAV) |
| IMF GFSR 14 Apr 2026: 9-11 quarters mild, 5-7 moderate; payouts above 5% observed | Dossier |
| North Haven Q3 2026: nearly two thirds of requests were resubmissions; listed OBDC non-accruals 1.1% of fair value, 2.3% at cost | Dossier |
| Arougheti, Ares Q2 2026 call, 31 Jul 2026: "some of the wealth flows could be more pro-cyclical than people thought they were"; "the individual investor can sometimes look to divest when they should be investing" | Verified by fetch of the transcript (speaker, answer to Bank of America's analyst) |
| Ares non-traded BDC requests about 11% from fewer than 5% of investors (June 2026) | Secondary (TIKR); chapter says "Press accounts" (hedged as briefed) |
| D. E. Shaw, "Assessing U.S. Mortgage-Backed Credit Stress in 2020", originally November 2020: "in excess of $400 million in CAS and STACR bonds at a significant discount to par"; "put under stress by redemption requests and margin calls" | Verified by fetch of the D. E. Shaw page (both sentences, title, date) |
| ESRB Working Paper 141 (Kundu, March 2023): 7.5% CCC limit, lowest-price haircut, "median CLO operates within 4% of the most stringent covenant threshold"; Eagle Point Income Co. letter 18 Feb 2026: CCC 4.3%, junior OC cushions 3.9% | Dossier (verbatim) |
| Whalen on *The Credit Edge*: "the weakest borrower, and they cry uncle first" | Verified by fetch of the episode page. **Fixed** the title (see below). The page shows no date; 15 Oct 2026 is the dossier's feed date |
| FRED numbers: HY OAS 259 (22 Jan 2025), 355 (31 Mar), 445 (4 Apr), 461 (7 Apr), B 486, CCC 1,137, BB 306, IG 120, 394 (30 Apr), VIX 46.98 (7 Apr) and 52.33 (8 Apr); 15 Oct 2026: HY 323, BB 197, CCC 1,278; YTD returns CCC -5.21%, BB +0.33%, HY +0.15% | Pulled from FRED CSV; all match exactly |
| 7 Apr 2025: $99bn of fixed-income ETFs, about 60% in iShares (Coalition Greenwich via The DESK); 8 Apr: $89.7bn record, 12% portfolio trades; HYG -0.66% then +1.49% to NAV; MarketAxess RFQ prices 13.2 to 6.6 on 9 Apr, 11.3 within a week; 9 Apr 90-day tariff pause | Dossiers (electronification, Part V market structure, figure series) |
| Hana's headline OAS at December 2024 weights, 377 bp vs 323 (54 bp of mix) | Dossier (figure series); ratios 1,278/323 = 3.96 and 1,137/461 = 2.47 re-computed |
| Math checks in the new boxes (mixture variance 4.35, sigma 2.1%, tail 0.13% vs 1.7%, 13x, between-regime part 0.96; filter 8:9 = 47% then 25%; OU 1.98-year half-life and 89 bp; lambda 0.97 half-life 22.8 months, effective sample 66; thermometer 5.7%; mediant 0.33/0.37; turnover 6% and 4.5 bp; 3.2-duration drag 32 bp) | Re-computed; all correct (the brief's 0.91 was corrected by the writer to 0.96, which is right) |
| Code-output figures quoted in the §12.10 explanations (3.62%, 6.53%, xi 0.379, 6.30% vs 2.10%, delta 1.000, 21.9 and 5.7 months, 98.2% vs 99.0%, Sharpe 0.21 to 0.35, 3.02% claimed vs 4.56%) | Appendix F listings 12.1 to 12.5 were run; every number reproduces |

### Fixed in the chapter (small Edits)

1. §12.3, Thursday 15 Oct scene: "its widest since 2023" was not verifiable (FRED's ICE series now begin on 17 Oct 2023, and 14 Oct 2026 printed 12.82%). Replaced with "a hair under the previous day's 12.82%, the widest print in the three years of history FRED serves".
2. §12.9 Case C: "TCW's chief investment officer Bryan Whalen" changed to "chief investment officer of TCW's fixed-income group" (the episode page's own description).
3. §12.7, Beat 2: 8-K citation "5 and 18 November 2025" changed to "5 and 19 November 2025; the termination took effect on the 18th" (filing date vs effective date).
4. §12.7, Beat 3: Cox/OBDC II return of capital "about 35% of NAV" now says "about 35% of the \$8.27 net asset value per share the fund had started the quarter with", the dossier's base; the \$5.57 end-of-March NAV is after the distribution.
5. §12.7, Beat 1: Theo's "Receivables pledged twice" now "Receivables allegedly pledged twice" (allegations, not findings).
6. §12.3, Ratio 3 scene: the invented two-point CMBS BBB bid-offer now tagged *(illustrative)*.

### Real people, invented dialogue, fiction labels

- No real person speaks invented lines. Dimon, Marks, Arougheti and Whalen appear only through quotations from their published or recorded words, each cited; the Ares conference-call paraphrase is hedged as press accounts. Fed, IMF, BIS, NAIC, Kundu, Carlino et al. and D. E. Shaw appear only as cited sources.
- Fictional characters (Theo, Kaz, Mags, Ines, Hana, Dov Adler, Wen Zhao, Vantress) match `state/cast_bible.md` (Theo: six years at PJT RSSG, 2020 to Sept 2026, tariff week on generic runway updates; no named PJT mandate; Hana: August refresh vignette with DATA-3107 and DATA-2840; Day One 22 Sep 2026 so 12 Oct is week four).
- Labels present: italic fiction notes at the cold open, the vignette (explicitly "fictional composite"), the Queue replay, the Twenty-Five Days replay and Case C; PB-13 box labeled "fictional composite"; insurer, direct-lender, CLO-manager seats described as generic; invented desk numbers tagged *(illustrative)* or *(the desk's fictional run)*. No "CHECK" appears in book text.

### Remaining doubtful (not fixed; hedged or flagged for the author)

- Listed-BDC median price-to-book 0.76 on 16 Oct 2026: a "computed" median of ten externally managed BDCs from a single aggregator, marked CHECK in the dossier. The chapter hedges ("By one market-data aggregator's count ... about 0.76") and the scene is set on the same morning, so "traded that day" slightly overreaches the timing; consider "as of the prior close".
- Early-February 2026 BDC drawdowns (Blue Owl as much as 13%; peers 8-10%) rest on one trade-press piece (CHECK in dossier). Hedged as "trade press reported". Not re-verified on the web.
- Fed Nov 2025 FSR date, Moody's, IMF Oct 2026 and the Fed "ten largest BDCs, about 80% of sector assets" clause (pre text, not new) were not re-fetched; they come from dossiers and the earlier Trend Watch fact-check.
- Whalen episode date (15 Oct 2026) is a feed date, not shown on the episode page.
- The December 2024 index weights behind Hana's 377 bp are dossier regression estimates (FRED publishes no bucket weights); the chapter labels it "the desk's computation".
- Ares June conference figure (11% of requests from fewer than 5% of investors) is secondary and hedged.
- Resource Graph additions (16 specific items from the U3b pass) were not re-audited here; the resgraph log says titles, dates and URLs were checked against the media dossier, and "why" lines quote the sources' own claims.
- Story-clock note, not a fact error: the cast bible says October replays run on Friday afternoons, but the Queue replay is dated Wednesday 14 Oct 2026 and Case C Thursday 15 Oct; Twenty-Five Days is Friday 16 Oct. The brief did not fix the weekdays.

## Check 3. Hygiene

- Code blocks: exactly one fence pair (lines 966 to 996), tagged `text` (the Spec You Hand the Robot). No other fences.
- Math: 48 `$$` delimiters (even); every non-display line has an even number of unescaped `$`; no currency pair parses as math.
- Currency: all dollar amounts are `\$`-escaped (no unescaped `$` followed by an amount outside math).
- No line of `---` anywhere in the chapter.
- No adjacent boxed elements (38 blockquote blocks, none separated by fewer than two lines); ten Math, Gently boxes.
- Last line: `<!-- STATUS: COMPLETE -->` (file ends with a single newline; unchanged by the edits).
- `tools/check_book.py --file` passes: 30,300 words.
<!-- STATUS: COMPLETE -->
