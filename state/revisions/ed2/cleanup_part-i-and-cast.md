# Cleanup log: part-i-and-cast (2026-10-18)

Group items: ch1-odd-lots, ch3-svb-coda, ch3-remand, ch4-figs, cast-bible, columbus-day. No earlier log existed (no COMPLETE marker), so all six were worked. Web calls used: 6 of 6 (Accounting Today/Bloomberg article twice, Mayer Brown note, one WebSearch, CRA Finance page, signalsandthreads.com page). No call to the Serta opinion itself was possible (not in the dossiers; ECF 742 is not on the open pages found).

Files touched:
- `book_src/03_ch03_pjt_rssg_cognitive_bridge.md` (items 2, 3)
- `book_src/04_ch04_inside_the_systematic_credit_industry.md` (items 4, 5; plus one stray-currency escape, see item 4)
- `tools/figures/ch04.py` and three new PNGs `assets/figures/ch04_pod_fee_waterfall.png`, `ch04_etrading_timeline.png`, `ch04_genealogy.png` (item 4)
- `book_src/09_ch09b_the_bond_data_problem_and_the_replication_crisis.md` (one cross-reference, forced by item 4's renumbering: "Figure 4.3" -> "Figure 4.4")
- `book_src/01_ch01b_a_week_in_five_quant_shops.md` (item 5, Ep 29 citation)
- `book_src/92_appC_trend_tracker.md` (item 5, TRACE \$70.2bn hedge)
- `book_src/21_ch21_leveraged_loans_and_clo_microstructure.md` (item 6)
- `state/cast_bible.md` (items 5, 6; I was the only editor)
- Not touched: Ch 1 (item 1 already fixed), Ch 8-C (item 6, no day count crosses the holiday), Ch 4-D (its citations were already right; its fulcrum scene and dates are ruled on in the bible, not edited).

---

## [ch1-odd-lots] status: already-fixed

**Found.** `grep -n -i "odd lots" book_src/01_ch01_anthology_and_landscape.md` returns six lines, every one a specific episode with title, guest, date and URL, matching `media_episodes_posts_parts_I_II.md` / `media_podcasts_credit_quant.md` row for row:
- L302 "Episode 2: Under the Hood of the \$8 Trln Corporate Bond Market" (Chris White, 16 Nov 2015, omny .../episode-2-under-the-hood-of-the-8-trln-corporate-b)
- L303 "Here's Why It's So Hard to Fix the Corporate Bond Market" (Larry Harris, 18 Nov 2021, podscripts URL)
- L304 "Why the True Price of a Bond Can Still Be Hard To Know" (Kowara and Jacobson, 5 Apr 2021)
- L696 "A Longstanding Fear About The Corporate Debt Market May Finally Be Coming True" (Chris White, 23 Mar 2020)
- L697 "What David Barse Learned From Watching A Credit Fund Blow Up" (1 Oct 2018)
- L863 "Inside the Blood Sport of Creditor-on-Creditor Violence" (Sujeet Indap, 25 Nov 2024)

No "episode numbers omitted" note remains (`grep -i "episode numbers\|omitted"` is empty). Introduced by commit a01ff13 (Ch 1 complete). No edit.

---

## [ch3-svb-coda] status: fixed

**Source.** Jonathan Randles, Bloomberg News, 2 Jul 2024 10:27 a.m. EDT, "SVB bonds rise after \$600M cut to tax bill", read via Accounting Today (the dossier's [BBG-Randles]). Two fetches agree. The article says the 1.8% notes due 2026 "rose as much as 2.625 cents on the dollar to 63.625 cents, according to Trace" (the book's "2.625 points to 63.625 cents" matches), the IRS cut one claim from about \$649 million to \$43 million (matches), and the holding company is finalizing a plan that "would see it repay bondholders and other creditors owed \$3.5 billion at least 40% of that sum"; creditors had until 3 July to vote and Judge Glenn would consider approval later that month. So the figure is (a) one Bloomberg article, not "press reports", (b) "at least 40%", a stated minimum under the plan, not an expected recovery and not "roughly 40% or better", and (c) attributed by Bloomberg to the plan itself, not to a company filing or a Bloomberg estimate.

**Change (Ch 3 §3.4 coda, line 422).**
- Old: `and press reports put the expected recovery under the plan then out for a vote, for bondholders and other creditors owed \$3.5bn, at roughly 40% or better.`
- New: `and the same Bloomberg report said the plan then out for a vote would repay bondholders and other creditors owed \$3.5bn at least 40% of that sum.`

Hedge kept in the right place (it is Bloomberg's statement of what the plan would do, so the book no longer calls it an expected recovery). The dossier line 82/184 does not carry the 40% figure; not edited (outside the item).

---

## [ch3-remand] status: softened

**Found.** The text at §3.7 "After the announcement" (line 711) no longer carries the \$62mm-\$94mm range (the lessons pass cut it), so the remaining check was the arithmetic against the chapter's own inputs and whether the range can be restored.
- Chapter inputs: up to \$186mm face traded 22 Jun 2020 to 31 Dec 2021; defense says 29%-43% of observed volume; excluded holdings about \$895mm.
- Recomputed (python3): 29% x \$186mm = \$53.9mm; 43% x \$186mm = \$80.0mm; that is 6.0% to 8.9% of \$895mm, so "at most about a tenth" holds. The advisor briefs (state/advisor_briefs/03, 14, "VERIFIED from the opinion text") give the expert's but-for sales as \$62mm-\$94mm = "29-43% of observed volume". \$62mm is 33.3% and \$94mm is 50.5% of \$186mm; \$62mm / 29% = \$213.8mm and \$94mm / 43% = \$218.6mm. So the two pairs fit a common base near \$215mm-\$220mm, not \$186mm: the percentages are of a different (larger) volume base than the "up to \$186mm" the same brief quotes. The base cannot be tied from anything in the repo or on the pages reachable inside the call budget, so the dollar range is NOT restored.
- New source facts found: Mayer Brown (July 2026) reports the court's own finding rejecting failure to mitigate: "only approximately \$162 million in aggregate face amount traded over 18 months against the Plaintiffs' \$700+ million position" (also in `trend_re_default_and_recovery_dataset.md` row 2026-07-07); CRA Finance's page quotes the court on a position of "over \$700 million face amount" that the "actual market could not have absorbed". So \$186mm is the expert's "up to" count and \$162mm is the court's. Both fit the chapter's conclusion: 43% of \$162mm is \$70mm, 7.8% of \$895mm and 10% of \$700mm.

**Change.**
- Old: `Up to \$186mm face of first-lien term loans traded between June 2020 and December 31, 2021, and defense experts argued the excluded lenders could have sold 29% to 43% of the observed volume, against holdings of about \$895mm. In other words, even a holder who wanted out could have sold at most about a tenth of the position over eighteen months.`
- New: `Up to \$186mm face of first-lien term loans traded between June 2020 and December 31, 2021, by the defense expert's count (the court's own, as Mayer Brown summarizes it, was about \$162mm), and the defense argued the excluded lenders could have sold 29% to 43% of the observed volume, against holdings of about \$895mm. Even 43% of \$186mm is only about \$80mm *(our arithmetic)*, so a holder who wanted out could have sold at most about a tenth of the position over eighteen months.`

The "tenth" is now shown arithmetic, and it is robust to the unknown base: at a \$215mm-\$220mm base, 43% is about \$93mm, 10.4% of \$895mm. **Open for the owner:** the court's mitigation base is the plaintiffs' "\$700+ million" position, not the \$895mm excluded class; the book keeps \$895mm (the class), which is what §3.7's later arithmetic uses. Ch 14 line 940 still prints "\$62mm to \$94mm" from the same brief, unreconciled, and does not mention the \$162mm; not in this group's files.

**Event-study promise.** `grep -n -i "event stud\|future work\|first-lien flow"` finds no promise left in Ch 3. The only related sentence is line 699, "Whether the actual flow in May and June 2020 looked like it is an empirical question this book does not answer; the point is that the detector is designed to ask it." That is a plain disclaimer, not a cross-reference; nothing points to a missing section. Left as is.

---

## [ch4-figs] status: fixed

**Found.** Not `![..]` embeds: three `<!-- FIGURE: ... -->` placeholder comments (lines 121, 705, 913), which is why `tools/check_figures.py` did not list them (its 14 missing files are Ch 9-B, 13-B, 17-B and 18-B figures, none of them Ch 4). The earlier figures log said any later figure must be numbered in order of appearance and the others renumbered.

**Drawn (appended to `tools/figures/ch04.py`; docstring updated; run via the three new functions only, so the five existing PNGs were not regenerated).**
1. `ch04_pod_fee_waterfall.png` (85 KB). Stacked bars at gross 5, 10, 15, 20, 25%: net to the investor (blue, on the baseline), fixed charges 4 (1 + 3), PM incentive 20% x (gross - 3), fund incentive 20% x (gross - 4 - PM). Asserted in the script against the dossier table (rv_pod_platforms_and_risk.md 3.2) and the chapter: net 0.48, 3.68, 6.88, 10.08, 13.28; 6% gross nets 1.12; every stack sums to its gross. Direct labels (aqua and yellow are low-contrast slots), net printed under each bar, one annotation on Mercer's "10% net needs about 20% gross". Illustrative.
2. `ch04_etrading_timeline.png` (111 KB). Left: Greenwich e-share of US IG and HY volume, annual values plotted mid-year so "H1 2022" is a half-year band: 2021 34/25 and 2024 48/33 solid (the Trend Watch), 2022 41/31 and 2023 45/33 hollow (read off Greenwich's chart; the dossier flags them CHECK), the 2019-20 ranges IG 25-38% and HY 15-30% as shaded bands (approximate, from Man 2023 Fig. 1), the H1 2022 portfolio-trading cost spike as a labeled band with NO number (Man gives no public series; the chapter's 20bp-to-60bp is the fictional desk's). Right: Man Numeric electronic share of order flow, IG 60% and HY 30% to "over 90% of all credit order flow" (May 2023); the start is undated in the source and the axis says so. I did not extend the series to 2025: the only 2025 Greenwich readings in the dossier are mixed months (IG 52% in June, HY 30% in February), not a clean annual point.
3. `ch04_genealogy.png` (133 KB). Flow graph, five lineages from §4.10-§4.11: KMV (early 1990s) -> Moody's (bought, 2002) and -> DCI (Kealhofer and McQuown found it, 2004) -> Blackstone Corporate Bond Strategies (agrees to buy, 30 Nov 2020); Apollo quant research -> Man Numeric credit (co-head hired, 2018); AQR / BGI alumnus -> Acadian systematic credit (announced Jul 2022); Robeco factor-paper author -> Cubist Systematic Strategies (Point72); BlueCove (founded 2018) -> Ares Systematic Credit (agreed Oct 2025, closed Feb 2026). Blue = people move or found a firm, orange = a firm is bought. Every edge label is taken from the chapter's own text and citations.

All three PNGs opened and checked. Fixes from the first look: the e-trading figure's "2019-20" label ran into the y tick labels and was clipped (now three lines, headroom added), and the 2019-20 bands gained "IG, 25-38%" / "HY, 15-30%" labels. Fee waterfall and genealogy needed no changes.

**Embedded in `04_ch04_inside_the_systematic_credit_industry.md`, and the figures renumbered in order of appearance (4.1 fee waterfall, 4.2 effective breadth, 4.3 truncation, 4.4 factor zoo, 4.5 e-trading, 4.6 capacity, 4.7 genealogy, 4.8 empty cells).**
- Fee waterfall: placeholder comment deleted; the embed moved up to directly after the paragraph that does the Mercer arithmetic (it had sat six paragraphs later, after the pod discussion), and that paragraph gained "Figure 4.1 draws the waterfall at five gross returns."
- E-trading: placeholder replaced in place; the FINRA/TRACE paragraph before it gained "Figure 4.5 sets the market's electronic share beside Man Numeric's own migration."
- Genealogy: placeholder replaced in place; the family-tree paragraph gained "Figure 4.7 draws the tree."
- Renumbered pointer sentence and caption for the five existing figures: "Figure 4.1" -> 4.2 (effective breadth), 4.2 -> 4.3 (truncation), 4.3 -> 4.4 (factor zoo), 4.4 -> 4.6 (capacity), 4.5 -> 4.8 (empty cells).
- Cross-reference in another chapter: Ch 9-B line 228 "Chapter 4 put the audit's scoreboard on the screen (Figure 4.3)" -> "(Figure 4.4)". It is the only outside reference (`grep "Figure 4\."` over book_src; Ch 15's "Figure 4.3" is a Bohn-Stein source extraction, unrelated). One-token exact-string edit on a file another agent was editing; re-verified after the edit.
- Captions follow the house style (claim first; "Illustrative:" for the waterfall; "Source:" with the Trend Watch, Man 2023 pp.2-5, and the sources of §4.10-§4.11 for the other two). The e-trading caption states what is approximate (2019-20 ranges, 2022-23 points read off a chart) and that Man gives no start date and no 2022 cost series.
- `python3 tools/check_figures.py` still lists 14 missing files, none Ch 4; all eight Ch 4 figures resolve; `tools/check_book.py --file` on Ch 4 passes with no warnings.

**Incidental.** The lint's one warning on Ch 4 was a pre-existing unescaped pair in the Resource Graph (line 1014, "A \$40B systematic book that ... a \$100 billion business"), which pandoc could read as inline math. Escaped both dollar signs.

---

## [cast-bible] status: fixed

All seven sub-items are ruled in `state/cast_bible.md` (new "Cleanup rulings" block under the story clock; a "Ch 4-D additions" section; a ruling appended to C7; a fulcrum pointer in the Kaz ledger; a "Source flags" section). Chapter text changed only where a fact was wrong.

1. **Theo's start date.** Chapters checked: 00_02 ("Tuesday 22 September", eighty-six days from Sun 28 Jun: 28 Jun + 86 = 22 Sep, python3), Ch 4-D label ("Tuesday 22 September 2026"), Ch 3-B (A/B exchange Tue 22 Sep; Mon 21 Sep is the index roll, before Theo), Ch 10 (OAS count from 22 Sep), Ch 27 (Tue 29 Sep = week two). No chapter says Mon 21 Sep. The "Mon 21 Sep" is only in `state/advisor_briefs/04_ch04d_getting_the_seat.md` (line 7, "by the C10 clock: Fri 9 Oct is week three; CHECK against the preface"); week counts come out the same under either start. **Ruling: Day One is Tue 22 Sep 2026; Mon 21 Sep is the CDX roll day.** No chapter edit.
2. **Kaz's fulcrum misread (C7).** Ch 4-D §4D.9 (flashback, Thu 25 Jun 2026): Kaz asks "Is a *fulcrum* the thing you hang the hedge from?", Theo concedes it is half right (PB-06's long-the-fulcrum pair), Kaz writes it down; §4D.10: "Kaz had asked about the fulcrum and meant it." **Ruling (logged under C7, text unchanged): not a breach.** It is a probe that is partly correct, not the rationed comic misread (which stays Ch 1's "zero duration" by reading order); it precedes Ch 1 in story time so nothing can call back to it; and it adds no new wrong reading. Constraint recorded: do not reuse "hang the hedge from" as a gag.
3. **Vantress interview, Owen's email, Theo's ROBO.** Logged in the new "Ch 4-D additions" section: the Tue 23 Jun 2026 Vantress interview (third pod's composite PM; the unnamed risk manager and the "long that it did not mean to be" question; the Kelly question f* = 0.926 and the A/B pair at \$8.6mm / \$5.7mm), Owen's one-line email ("Knows documents. Has never been stopped out, because he has never had a P&L."), ROBO as Theo's own paid agent "since the spring" (Sat 27 Jun and Sun 28 Jun offers, both declined), plus Ines's and Kaz's interview slots and the distressed-fund pitch and decline so the bible has the full week.
4. **Ch 1-B "Ep 29" link.** Found that the queue's wording is not quite the fix. Ch 1 (line 280), Ch 3 (line 330), Ch 4-D (lines 60, 252, 463) and the dossier (`life_quant_shop_daily_life.md` 4.1, "Ep 29, Eric Mannes (2 Sep 2026)") all attribute the vendor-"whoops", save-the-arrival-time, negative-crude and `uscommoditiesrisk.xlsm` quotes to **Ep 29, 2 Sep 2026**, and Ch 4-D links that episode as "Wrestling the World into Rows". Only Ch 1-B linked those quotes to "Swapping the Engine Out of a Moving Race Car". The publisher's page for that URL says **Episode 15, guest Ella Ehrlich, 12 September 2022**, and a page-summarizing fetch found none of the three quoted phrases in its transcript. So the wrong parts were Ch 1-B's title and URL, not the number. Change (Ch 1-B lines 35 and 304): `Ep 29, "Swapping the engine out of a moving race car," 2 Sep 2026` -> `Ep 29, "Wrestling the World into Rows," 2 Sep 2026`; resource line `Ep 29, "Swapping the Engine Out of a Moving Race Car" (2 Sep 2026) ... https://signalsandthreads.com/swapping-the-engine-out-of-a-moving-race-car/` -> `Ep 29, "Wrestling the World into Rows" (2 Sep 2026) ... https://signalsandthreads.com/wrestling-the-world-into-rows/`. **Caveat:** the identification Ep 29 = "Wrestling the World into Rows" rests on the dossier and Ch 4-D; I used my last web call on the old URL, so the new page itself was not fetched. Confirm once before print (the dossier's "Ep 15 (Gord, the trading-data normaliser)" is also inconsistent with the page, so its episode numbering is not fully reliable).
5. **TRACE \$70.2bn.** Used in Ch 4 §4.7 Trend Watch, Ch 4-D §4D.7 (already worded "The DESK put ... at \$70.2bn") and App C. Source is The DESK, 9 Apr 2026 (trend_part_v_market_structure_2026.md row March 2026); no FINRA primary was reachable (the dossier's own FINRA reading is April 2025 at \$62bn; Tradeweb's Sep 2026 HG+HY under the affiliate indicator is about \$61bn, a different definition). Hedged: Ch 4 `Combined US IG+HY TRACE ADV is \$70.2bn (+14.7% year on year);` -> `The DESK reports combined US IG+HY TRACE ADV of \$70.2bn (+14.7% year on year; a trade-press figure we have not tied to FINRA's own monthly file);` and App C row 2026-03 `TRACE ADV \$70.2bn` -> `TRACE ADV \$70.2bn (The DESK's figure; not tied to FINRA's file)`. Ch 4-D left alone (already attributed in the sentence).
6. **Offer date vs 4-D (00_02).** Read both. 00_02 does not date the offer to Sunday 28 June: its flashback is Sun 28 Jun (eighty-six days out) and its plan page says "Ines's offer arrived at the end of the interview week of Chapter 4-D, the calendar started on Sunday 28 June". 4-D's debrief has him accept Ines and resign from PJT that same Sunday ("in that order"). The two agree if the offer email came at the end of the interview week (by Fri 26 Jun) and Sunday 28 Jun is the acceptance, the resignation and the start of the plan. **Ruling recorded in the bible; no chapter edit.** The distressed fund was declined Mon 29 Jun (4-D). No chapter gives an earlier date for the offer than "the end of the interview week", and none should.

---

## [columbus-day] status: fixed

**Found.** Mon 12 Oct 2026 is Columbus Day / Indigenous Peoples' Day: Federal Reserve holiday, SIFMA full-close recommendation, ICE Clear Credit clearing holiday (as recorded in `08_ch08c...rv.md` item 1 and the bible's Ch 8-C flag; not re-fetched, web budget). Day counts that cross it:
- **Ch 21.** Cold open is Wed 14 Oct 2026 live; the trade was Fri 11 Sep. Weekdays after 11 Sep through 14 Oct = 23 (python3), but with 12 Oct excluded it is **22**. The Debrief's "day twenty-seven" has no calendar date in the text; with the holiday, the same settlement date as under the old count (Tue 20 Oct, four business days after the cold open) is day 26 (day 27 would be Wed 21 Oct).
- **Ch 8-C.** Checked every day-count: "third business day of October" (Mon 5 Oct), "two business days after month-end" (Mon 2 and Tue 3 Nov), the Corriveau print "nine days earlier" (21 to 30 Oct, calendar), the roll-week cold open (Mon 21 Sep) and the three-days-on-a-Monday accrual. None crosses 12 Oct. Its only reference to Monday 12 Oct is the risk model's "Monday's run", which a holiday does not prevent. No edit.

**Change (Ch 21, three places; smallest fix, no story beat moved).**
- Cold open, line 5: `"Twenty-three business days," she said.` -> `"Twenty-two business days," she said.`
- Seat box, line 156: `Mags's twenty-three-day ticket` -> `Mags's twenty-two-day ticket`
- Debrief, line 972: `settled on day twenty-seven,` -> `settled on day twenty-six,`

**Recorded in the bible** under the story clock (the holiday is not a business day for any count; what was applied), in the C-list pointer on the Ch 8-C flag, and listed as still open.

**Not done (outside the item's "day counts"; each touches a story beat, so for the owner).** The lines that treat Mon 12 Oct as a trading day: Ch 1 ("78 as Monday's open"), Ch 1-B (FCM roll booked Monday, "Monday night" variation margin), Ch 8-B ("Monday's 78"; equity regime "since 12 Oct"), Ch 27 ("the FCM's record said Monday"), and Ch 6-B's live cold open at 7:12 a.m. on Mon 12 Oct. The rv's proposed fix is to move the open and the booking to Tue 13 Oct or to say the bond market was shut; I changed none of them.

<!-- STATUS: COMPLETE -->
