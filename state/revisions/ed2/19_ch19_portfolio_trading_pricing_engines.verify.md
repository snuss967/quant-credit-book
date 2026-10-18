# Verification report (Edition 2): 19_ch19_portfolio_trading_pricing_engines

Chapter: `book_src/19_ch19_portfolio_trading_pricing_engines.md` (30,098 words after revision; `tools/check_book.py` reports OK). Pre-revision text: commit `9ac1c37`. Revision log was COMPLETE. Web calls used: 9 of 15.

## 1. Nothing removed: PASS, no restoration needed

Compared pre and post with python3.

- Headings: all 37 pre headings are present in post. 19 headings were added (eight `#### The Full Derivation`, seven aside subsections such as "Reading the master equation at its edges", two Long Scene headings, `#### The Hand History: Friday 30 October 2026`, `#### Wen's Month-End List: Friday 30 October 2026`). The Hand History date is Fri 30 Oct, not the brief's 16 Oct, per cast bible C10 and the Ch 19 canon entry.
- Display math: 22 blocks pre, 22 post, every block present with identical content (whitespace-normalised). Equations (19.1)-(19.11) all present, numbering unchanged.
- `[SOURCE EXTRACTION]` blocks: 11 and 11, same sources and page numbers (Man pp.2, 2, 3, 4; Ben Dor pp.112 twice, 118, 166; Paleologo pp.193, 186; Dynkin p.704; Bohn & Stein p.48), each with its Annotation.
- Trend Watch boxes: 4 and 4, all four word-for-word identical to pre.
- Desk Myth, Poker Table, three Ways This Blows Up boxes: all present, identical.
- Exercises 1-6: titles and order identical. The Spec You Hand the Robot and all eight section Specs present.
- Appendix F links: all eight `#code-19-1` to `#code-19-8` present (in prose after U1 replaced the stubs, plus the Finder table). The `<!-- EXPLAIN -->` stubs were replaced by real explanations, as directive U1 requires.
- Resource Graphs: 4 and 4; no pre bullet lost and no URL lost (27 pre URLs all present; 17 added by the U3b resgraph pass). Figures 19.1-19.5 embedded with captions.
- Pre-revision prose that was reworded rather than copied (55 non-verbatim lines) was checked line by line: the P-measure statement, boundary checks, units paragraph, hedge menu, SCOOS weights, Campbell/Minieri/7%/67%, Serta pointer and the hand-history numbers all survive (as scene text, boxes or derivation prose).

## 2. Facts: new claims checked

Dossiers: `perspectives_dealers_and_systematic_shops.md`, `trend_electronification_pt_etf_liquidity.md`, `life_quant_shop_daily_life.md`, `trend_systematic_credit_industry.md`, plus the Man PDFs in `state/pdf_pages`, `cast_bible.md`, `rv_pair_book.md`, and Chapters 1, 2, 20, 22 for cross-references.

Verified (dossier and/or primary source):

- FIMSAC 10 Feb 2020 TRACE portfolio-trade flag recommendation, 30 issuers, all-or-none (dossier row; SEC/WilmerHale/FINRA RN 20-24 via web search). The 2023 modifier at ten issues is the pre text.
- Goldman: about 8,000 PTs, 300+ clients, about \$60mm, about 100 CUSIPs in 2023 (Greenwich write-up, greenwich.com/node/148251, via web search; webinar 17 Jan 2024).
- SCOOS June 2025: read the Fed PDF itself. All of: high-grade frequent for all active dealers, high yield three-fifths; insurers and pensions three-fifths frequent; composition four-fifths, market conditions two-thirds, relationship and balance sheet about one-half; net one-fifth "decreased somewhat"; three-fifths hedge with credit ETFs. All match.
- Jane Street client-offering quote and Flow Traders AR 2025 quote, and the "reduced the capital deployed to fixed income in 2025" sentence: match dossier verbatim.
- Jefferies (Orlan, Jallot, The DESK 2023-10-26), Trumid's Pender (Jan 2024 and 10 Feb 2026), JPMorgan's Cajfinger and Grant (Making Sense, recorded 23 Apr 2025, published 9 May 2025; episode and speaker titles confirmed on the podcast listing): quotes and titles match the dossier. "He" for Pender matches the dossier.
- LQD about 90,000 trades and top five holdings averaging 37 (Ramji, BlackRock Q1 2020 call, 16 Apr 2020): dossier and Ch 20. LQD about 5% under NAV on Thu 12 Mar 2020: consistent with Ch 1 §1.8.2 and Ch 20 (5.0%).
- Quant funds \$116.5bn on MarketAxess Open Trading, Q1-Q3 2020, +150%: Man 2022 p.8 text confirmed.
- Man 2023 quotes in the §19.9 View From Another Seat (duly switched, slicing up trades, 30%/60% to over 90%, 1 May 2023, smaller more frequent trades, digestible in RFQ form, vast majority sent as RFQs): all confirmed against the extracted pages, including the paper's title and June 2023 date.
- Barclays lunch-hour 11.3% to 12.5% "since 2022" (The DESK 2025-09-17): dossier.
- Fed: 25bp on 16 Mar 2022 (to 1/4-1/2) and 4 May 2022 (to 3/4-1, balance sheet reduction from 1 June): Fed statements fetched.
- Ford: S&P to BB+ on 25 Mar 2020 (web search); Moody's had already cut Ford to Ba1 in Sept 2019, so "split-rated" on the 12 March tape is correct and was left alone.
- Fed facilities 23 Mar and 9 Apr 2020: match Ch 20's tape table. Tariff announcement Wed 2 Apr and pause Wed 9 Apr 2025: weekdays computed; dates are standard.
- All story dates and weekdays computed (23 Oct, 30 Oct, 17 May 2022, 12 Mar 2020, 7 Apr 2025, 13 Jan 2026). All correct.
- Cross-references checked against the book: Ch 1 §1.3.1/§1.3.3/§1.4/§1.8.2, Ch 2 §2.6.2/§2.7.1/§2.9.3, Ch 4 §4.6/§4.8, Ch 5 §5.1.1/§5.1.3/§5.5.3, Ch 6 §6.1.1/§6.2.2, Ch 7-B §7-B.5, Ch 8 §8.8, Ch 18 §18.6/§18.6.3, Ch 20 and Ch 22 (the "50-300bp" is Halvorsen's fictional fee path in Ch 22 and Ch 1-B). All exist and say what Ch 19 claims. PB-01 (Halvorsen 7.25% 2029 short leg) matches `rv_pair_book.md`.
- Arithmetic of every Math, Gently box, the Pair box (\$254k coupon, \$49k borrow fee, \$330k, \$355k, R-squared 0.16), the Wen cost tally (\$39k vs \$31k) and the hand-history charge (\$0.34mm, 16bp): recomputed, all correct.
- Real people: no invented dialogue. Orlan, Jallot, Pender, Grant, Cajfinger, Campbell and Minieri appear only through verbatim published quotes with sources. Ines, Mags, Kaz, Theo, Hana, Yusuf, Wen, Dov, Bea, Vantress, Halvorsen and Wexcombe are labeled fictional or illustrative in the italic opener or the scene labels, and all appear in the cast bible.

## What I fixed (small Edits)

1. Two Tapes: "US fixed-income ETFs traded about \$99bn that day, a record" had no support in the dossier (which says only "FI ETFs, \$99bn, 7 Apr, about 60% iShares"; web search could not find the figure). Removed "US" and "a record", and cited The DESK 2025-06-10 with a pointer to the §19.4 Trend Watch.
2. Two Tapes: "within months, listed credit futures" had no dated support. Replaced with "in small size, the listed credit-index futures that exchanges began offering in 2024" (dossier: CME and ICE launched in 2024).
3. H1 2022 scene: internal contradiction. The desk "left \$\pi\$ where it was", yet Ines later bid 25bp, "the margin she had raised to in April". Now "ten basis points over the 2021 margin she had been holding" (consistent with Theo's "15 is what we got paid in 2021").
4. H1 2022 scene: "portfolio trading's share ... more than doubled in a year" was placed in a Q4 2021 context but rests on January 2021 vs January 2020 (5.4% vs 2.2%). Now "in the year to January 2021".
5. The Pair box: "within a few basis points" (112bp vs 120bp is 8bp). Now "within about 8bp of market value".
6. Hygiene: unescaped currency in two Resource Graph entries (the MarketAxess March 2026 release, in Graphs 3 and 4): `$2.3 billion`, `$8,478 million`, `$6,608 million` now `\$`. Added a blank line after `#### The Full Derivation` in §19.6.1.

## 3. Hygiene: PASS

- No code fences at all (no ```text diagrams either). Chapter has no CHECK, TODO, template wording or "By the end of this chapter" list. "Write three things before 3:00" is the card text the brief prescribes.
- Display math: every `$$` fence pairs (22 blocks). Inline math is balanced. The one odd-looking sentence (the units paragraph ending `=\$$.`) is identical to the pre text and parses as inline math closing after an escaped dollar.
- Currency escaped as `\$` everywhere in prose after fix 6.
- No `---` lines in the chapter. Last line is `<!-- STATUS: COMPLETE -->`.
- `tools/check_book.py`: OK.

## 4. Remaining doubts

- The Jane Street page ("fetched 18 October 2026"), the Orlan/Jallot/Pender 2023-24 quotes and the Cajfinger/Grant quotes rest on the dossier's own fetches; I confirmed the podcast episode, speakers and titles and the Greenwich Goldman figures, but did not re-read the transcripts or The DESK article.
- The \$99bn fixed-income ETF day (7 Apr 2025) remains in the pre-existing hedge-stack Trend Watch (The DESK 2025-06-10) and could not be re-confirmed on the open web; left as sourced.
- "Chapter 18-B" (named in the Pair box) is a planned chapter in the RV thread, not yet a file in `book_src`; if the plan changes, the pointer needs updating.
- The hand-history text quotes hand estimates (74bp, 35bp) while Figures 19.4/19.5 and §19.10 show 76bp and 37bp; the text carries its own "differ in the second digit" caveat (noted earlier in figcheck, not changed).
- The brief said line 117 down "about 9 points"; the chapter (1 and 5 points at 1 and 5 days, 14 points at 20 days in Listing 19.7) follows the cast bible canon and the listing, so I left it.
- Dossier note on Orlan's earlier Barclays role comes from a search-result summary and is not used in the chapter.

<!-- STATUS: COMPLETE -->
