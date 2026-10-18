# Verification Report, Edition 2: Chapter 2 (The Revolutions in Credit Trading)

Chapter: `book_src/02_ch02_revolutions_in_credit_trading.md`. Pre-revision text: commit 9ac1c37, saved at `/tmp/pre_02_ch02_revolutions_in_credit_trading.md`. Revision log: complete (STATUS marker present). Chapter grew from 15,002 to about 32,100 words (headings 29 to 38).

## Check 1. Nothing removed

Method: a python script compared headings, `$$` display-math blocks, `[SOURCE EXTRACTION]` blocks, Trend Watch boxes, Ways This Blows Up boxes, exercises, Appendix F `#code-` links, URLs, table rows, inline-math expressions and Resource Graph sections; a second script compared every pre-revision sentence with the post text.

Results:
- Headings: all 29 pre headings are present verbatim. Nine new headings: seven `#### The Full Derivation: ...` subsections (tail index; fitting a ceiling; best-of-n with a common anchor; the sequential router; what a basket's risk charge nets; the arbitrage band with stale marks; optimal turnover under linear cost), plus the two new scenes `#### The Week the ETF Was the Only Price` and `#### The Same Shock on New Pipes`.
- Display math: 26 blocks pre, 26 post, every pre block present verbatim after whitespace normalisation (the derivations were moved, not edited). All 201 distinct pre inline-math expressions survive (post has 255).
- `[SOURCE EXTRACTION]` blocks: 17 and 17, each identical to its pre text. Trend Watch boxes: 5 and 5, and all 42 table rows are identical. Ways This Blows Up: 4 and 4. Poker Table, Desk Myth, Moyer period piece: 1, 1, 2 each side. URLs: 41 and 41, none missing. `#code-2-1` to `#code-2-4`: 4 and 4.
- Exercises 1 to 6, "The Spec You Hand the Robot" and all four Resource Graphs (three mid-chapter, one final): byte-identical to the pre text (diffed line by line).
- The four `<!-- EXPLAIN: Listing 2.k -->` stubs and their auto "Code Companion" blurbs are gone. They were replaced by the U1 code-explanation prose, each ending in `*The full listing is [Listing 2.k in Appendix F](#code-2-k).*`. The brief assigns the stubs to U1, so nothing was restored. I scanned the U1 prose for real-world claims and found none beyond numbers the chapter already derives.
- Sentence-level diff: of 749 pre sentences, 61 are not verbatim in the post. All 61 are accounted for: the cold-open skills paragraph (now spread through Ines's speech, one skill per sentence, all seven present), the three "What it means for the desk" points (all present), the router bullets (rewritten as Ines walking one line, all three symbols and the BBB numbers present, and the numbers repeated in the Full Derivation), the four non-bank bullets (Jane Street, Citadel 14.2% with its self-reported CHECK, Hudson River title-only flag, the Greenwich 10% and 13% and the BCG 26% all present), the eight Desk Debrief bullets (all eight takeaways present, bold, in the cast's mouths), the four EXPLAIN stubs, and the $K=0.80$ ceiling-sensitivity paragraph (moved into the fitting-a-ceiling derivation with 0.150, 61%, 0.211 and 53% intact).
- Nothing needed restoring.

## Check 2. Facts

Sources: the dossiers the brief names (`life_quant_shop_daily_life.md`, `trend_part_v_market_structure_2026.md`, `trend_electronification_pt_etf_liquidity.md`, `media_episodes_posts_parts_I_II.md`, `perspectives_buyside_credit_managers.md`), `state/cast_bible.md`, Chapter 1 §1.8.3, and 14 web calls to primary sources: The DESK (15 Oct 2026 FILS Europe article; Jane Street issuance article), MarketAxess AxessPoint (14 Jul 2025, fetched twice), Tradeweb's September 2026 monthly report (PDF decoded locally with pdftotext), FINRA Rule 6730, The Microstructure Exchange season page, Man's *Extra Credit* transcript page, Greenwich (search and one page fetch), Apollo (search), Tradeweb blog (search), and the New York Fed SMCCF pages (search; the direct page returned not-found).

New factual claims, verified and left as written:
- Rule 6730(a): "as soon as practicable, but no later than within 15 minutes of the Time of Execution" (FINRA page, verbatim).
- Abdi, Rossi and Wu, "Overnight Corporate Bond Trading," The Microstructure Exchange, Tuesday 15 Sept 2026; trades executed after 6:30 p.m. and before 8:00 a.m. are not publicly disseminated through TRACE until the next morning (abstract).
- Shop Life: Tradeweb's September 2026 report (file dated 5 Oct, published Tuesday 6 Oct); FINRA's rule change effective 31 Aug 2026, voluntary reporting for September 2026, mandatory from 2 Aug 2027; "lowered reported U.S. High Grade TRACE volumes"; no restatement; HY impact "minimal"; break unsized. MarketAxess duplicates up to 8% in June 2026 and the PT modifier from 15 May 2023 (dossiers). Weekdays checked (7 Oct 2026 is a Wednesday, 6 Oct a Tuesday).
- MarketAxess AxessPoint (14 Jul 2025): prices per RFQ 13.2 to 6.6 on April 9, 11.3 within a week; HG bid-ask up to 231% wider; 44.62 bp at the COVID peak; algos "consistently around 80%" of liquidity; and, in 2020, the algo share of prices fell from 60% to 50% (now used in the March 2020 scene).
- The DESK, 15 Oct 2026 (Nick Dunbar): Vanguard's Stephanie Creswell (unnamed in the chapter): "a lot of algos and PT execution got turned off" in the Russia/Ukraine period, "stayed there" in April 2025; Swiss Life Asset Managers' trader: "you see clearly a concentration to the usual banks" under stress.
- Greenwich: $89.7bn on 8 April 2025 with 12% PT (Trumid basis); $92bn on 30 April (19 May 2025 spotlight); 78% of institutions using PT, +5 points (via The DESK, 15 May 2026).
- Jane Street, 1 Sept 2026: $14.6bn senior secured notes, S&P BB; proceeds retire about $11.1bn of borrowings, remainder for general purposes including "additional trading capital" (The DESK).
- FINRA Fact Book Table C12: 17.27 (2023) to 24.51 (2025) firms a day, +42%; top-5 share of $25mm+ par 54.5% to 47.7% (dossier; the chapter labels this INFERENCE, CHECK, correctly).
- Man's *Extra Credit* transcript (machine-generated, recorded March 2024): every quoted phrase is verbatim. Speakers per the transcript page: Kamenski said "was the year of portfolio trading," "harder for those desks to recycle risk," "transaction costs generally went up substantially" and "circumstances where the best course of action is to trade voice"; Lam said "might not be the optimal way," "slice it" and "the best venue and the best protocol."
- Zito quote ("very bespoke, long-duration capital that's not traditional to the CUSIP market"): matches the buy-side perspectives dossier; Apollo's page confirms the Bloomberg Invest recording on 4 March 2026 and republication on 15 May 2026. Web search could not find the phrase itself, so this one rests on the dossier.
- Egbunike episode description matches the media dossier (ETF Central Podcast Ep. 19, 10 Jan 2024); the chapter describes the AP's choice generically and puts no words in anyone's mouth.
- SMCCF: announced 23 March, expanded 9 April, ETF sales from 7 June 2021, bond sales from 12 July, all holdings sold or matured by 31 August 2021 (NY Fed pages via search; New York Fed staff report). The 12 May and 16 June first-purchase dates are from the pre-revision text and were not independently re-confirmed.
- LQD 5.0% (12 Mar 2020), 0.19% (13 Mar), VCIT 3.2%, SPIB 3.1%: match Chapter 1 §1.8.3. Todorov (200 bp against 0.7 bp), Haddad, Moreira and Muir, Kargar et al. (about 200 bp): unchanged from the pre text.
- Arithmetic re-done and correct: S-curve (3.7 times, r = 0.131, doubling 5.3 years), random-walk charge (1.5e-5, about 0.8 bp), crowd variance 0.1045, $n_{\text{eff}} = 2$, 12.5 and 4 Pareto means, 2.56 and 1.6 at 12 to 7.5 bp (4.0 to 10.24 turns, 48 to 76.8 bp), router 6.6 bp and the 1.22 against 0.35 threshold, cover-gap factor 2.2 from 13.2 to 6.6 (leaving about 1.3), the Kaz and Ines winner-distance predictions (about +40% and about -20%), and the weather Poisson (1 day in 20).

Fixed (12 small edits in the chapter):
1. FILS quote was wrong. The Ways This Blows Up box said buy-side traders at FILS Europe said ELPs "help mainly in normal markets." The primary article has Swiss Life's Edouard Faure saying "They help more in quiet markets or normal market conditions." Quote and attribution corrected; the writer's CHECK comment removed. (The `trend_electronification` dossier carries the same wrong wording; flag for the dossier owner.)
2. Rule 6730 edges of the day were wrong. The chapter, following the dossier, said trades before 8:00 a.m. are reported after the next open. The rule says a trade executed before the system opens is reported the same day after the 8:00 a.m. open; trades in the last 15 minutes before the 6:30 p.m. close, or after it, roll to the next business day as "as/of." Rewritten.
3. Tradeweb footnote misquoted: "[we] have not restated" is actually "TRACE and Tradeweb have not restated prior periods and therefore these amounts may not be comparable." Corrected.
4. "Averaged 9.11 bp across April" overstated MarketAxess, which gives the average during the turbulence and no averaging window. Reworded, and the AxessPoint citation made explicit.
5. Removed "a Tradeweb blog post is reported to have put HY portfolio trading at a record 20% on April 10 (search snippet only; CHECK)." Two searches could not find it, and Greenwich/Tradeweb data put HY PT at about 16% on 30 April. Replaced with the Greenwich 19 May 2025 figure the brief wanted: PT at 22.4% of IG volume on 30 April (Tradeweb data). The writer's stale CHECK comment removed.
6. March 2020 scene: added the verified 60% to 50% fall in the algorithmic share of MarketAxess prices in 2020 (AxessPoint), and removed the stale "omitted" comment.
7. Jane Street: Moody's did not rate the notes (it had affirmed the firm's Ba1 issuer rating in July); proceeds mostly retire about $11.1bn of borrowings. The old wording read as if Moody's rated the issue and as if "additional trading capital" were the main use.
8. Mags's July 2002 line: "about 520 bonds" is the end-2002 figure in the Trend Watch table. Now "by the end of that year."
9. Man $116.5bn figure was attributed to "Man's 2022 paper" in the scene and to the 2021 primer in §2.4. The scene now points to "the Man research behind §2.4's figure."
10. Lam and Kamenski quotations are now attributed to the speaker the transcript names (Kamenski on 2021, 2022 and voice; Lam on slicing), and "speech-recognition" changed to "machine-generated" transcript.
11. Continuity with `state/cast_bible.md` (C5): Mags was at a dealer bank until January 2021, not a distressed fund, in March 2020. The scene now says a dealer's distressed desk, and "the dealers had remembered how to bid" became "the street." In §2.1 "Her distressed fund" became "Her distressed book."
12. Added two italic notes (end of the March 2020 scene, before the April 2025 public-record recap) saying the dialogue is invented and belongs to the fictional desk, that the desk log's numbers are illustrative, and that real people appear only through quoted published phrases. Real people: none has invented dialogue. Kamenski, Lam, a Vanguard trader and a Swiss Life trader are quoted verbatim from cited sources; Zito is quoted from the cited text; Egbunike, Abdi, Rossi, Wu and the academics are cited, not quoted. Fictional composites are labeled: the Shop Life box ("A fictional composite; the dates and rule changes are real"), the generic bank and dealer seats ("no bank is named"), and Halvorsen ("fictional").

## Check 3. Hygiene

- Code fences: none (0 occurrences of three backticks), so there are no non-`text` blocks.
- Math: 52 `$$` markers, all alone on their lines, even, no block longer than 5 lines; no non-display line has an odd number of inline `$`.
- Currency: no unescaped `$digit` outside math spans; all dollar amounts use `\$`.
- No line of `---` anywhere (table separators use `:--` only).
- HTML comments balanced (4 open, 4 close). The file ends with a single `<!-- STATUS: COMPLETE -->` and a newline.

## What remains doubtful

- Halvorsen continuity. The chapter still says "Halvorsen Freight 7.125% senior notes due 2030, B2" and Kaz says "B2." `state/cast_bible.md` C9 sets canon at Halvorsen Packaging Holdings, 7.25% senior unsecured 2029, B3/B-. The CHECK comment at line 21 stays for the cast fixer (the ledger shows Chapter 2 is not yet in the fix queue). No numbers elsewhere depend on B2.
- Theo's PJT start. Canon C3 gives 2020 to Sept 2026, but Theo now has a March 2020 memory at PJT (thirteen-week cash models). A CHECK comment was added after that paragraph; the fixer must set a start before March 2020 or rewrite his corner.
- The Zito quotation rests on the dossier (the Apollo page confirms the event and dates, but I could not retrieve its text).
- Three Greenwich items (12% PT on 8 April, 22.4% IG PT on 30 April, 78% PT use) were checked against search results and the dossier, not against the paywalled reports. The 12 May and 16 June SMCCF first-purchase dates are inherited from the pre text.
- Pre-existing and unchanged: the §2.3.1 fit uses 48% for 2025, while the Trend Watch table lists 48% for full-year 2024 (June 2025 shows 52%); the chapter's own text calls it "48% to 48%, 2024 to 2025." Worth a one-line reconciliation at the next pass.
- Pre-existing and unchanged: the Jane Street article's own 2026 total ($5.4bn) does not reconcile with the issue size, as the dossier notes; the chapter does not use that total.
- Shop Life dashboard claim that September looks "soft against June's" is fictional and unsourced; Tradeweb reports September TRACE HG ADV at $47.0bn, up from August's $42.7bn. It is labeled a composite, so left.
- Word-level: Mags's "a rumor with four decimal places" about NAV is rhetorical (NAVs are normally published to two or four decimals depending on the fund); left as characterization.

<!-- STATUS: COMPLETE -->
