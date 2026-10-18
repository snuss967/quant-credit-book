# Cleanup log: basis-and-pairs (2026-10-18)

Group items: date-clash-24, PB-03-financing, SVB-8K-ch8, ch19-74bp. No earlier log existed (no COMPLETE marker), so all four items were worked. Web calls used: 2 of 6 (one curl to sec.gov, refused with 403; one WebFetch of the 8 March 2023 SVB 8-K, succeeded).

Files touched: `book_src/24_ch24_bond_cds_basis_and_deliverables.md` (items 1, 2), `book_src/08_ch08_isolating_ido_and_empirical_duration.md` (item 3), `book_src/19_ch19_portfolio_trading_pricing_engines.md` (item 4), `state/rv_pair_book.md` (item 2, PB-03 row only). `state/cast_bible.md` was read only.

---

## [date-clash-24] — status: fixed

**Found.** Four scenes sit on Fri 23 Oct 2026, the end of Theo's fifth week:
- Ch 19 cold open: live 150-line RFQ at 2:58 p.m. (Ines bids with fifty seconds left, about 3:01), and its H1-2022 Long Scene is "played on Friday 23 October 2026 after the close", with the master equation "still on the whiteboard from the afternoon".
- Ch 21 Long Scene B: "Replay, run on Friday 23 October 2026"; its cards are "turned over on Monday 26 October", and Scene B opens "Last week the forced seller was a CLO" (Scene A is Fri 16 Oct). Ch 21 is therefore pinned to Fri 23.
- Ch 2-B cold open: the Friday 4:10 p.m. markout meeting, 23 Oct.
- Ch 24 Long Scene A: a full Ines-led replay at 3:05 p.m. on Fri 23 Oct, seven minutes after the Ch 19 RFQ closes and before the Ch 2-B 4:10 meeting, plus the two other "after the close" replays that day.

Cast bible story clock: Day One Tue 22 Sep; Ch 19 cold open Fri 23 Oct 2:58 p.m. is canon (C10; the Ch 19 block), and Ch 21's A/B pairing fixes its Friday. Ch 24 is the chapter out of line. Ch 24's own thread does not depend on Friday: the cold open is Tue 20 Oct 7:41 a.m.; the "by Friday" at line 198 is a generic deadline remark about the research desk's panel; Ch 24's other replays are already off-Friday (Sears Tue 27 Oct, Scene B Thu 29 Oct "Not every replay waits for a Friday"); Ch 1 §1.8.2 says "Most Friday afternoons", and Ch 6-B and Ch 10 already run Ines replays on weekdays. Ines's other known commitments: Wed 21 Oct 4:15 p.m. (Ch 6-B SVB folder), Thu 22 Oct 4:40 p.m. (Ch 3 debrief) and a Thu 22 Oct late-afternoon Theo/Mags memo scene (Ch 21, Ines not in it), Mon 26 Oct 4:15 p.m. (Ch 27 model review, Kaz). Thu 22 Oct 3:05 p.m. leaves the most slack on both sides, and it keeps chapter order (cold open Tue 20, Scene A Thu 22, Sears Tue 27, panel Wed 28, Scene B Thu 29).

**Fix (Ch 24 §24.4, Long Scene A).** Moved to Thursday 22 October, same 3:05 p.m.; the "Friday replay" ritual wording dropped because the replay is no longer on a Friday. The March 2020 Fridays inside the replay (20 March, 4:40 p.m.) are untouched.
1. Fiction label: `and this Friday replay are invented (illustrative).` → `and this replay are invented (illustrative).`
2. `*Friday 23 October 2026, 3:05 p.m.* Ines's Friday replays have one rule:` → `*Thursday 22 October 2026, 3:05 p.m.* Ines's replays have one rule:`
3. `This Friday she put a single page on the projector` → `This Thursday she put a single page on the projector`

**Follow-ups for other owners (not edited).**
- `state/cast_bible.md` line 142 (Ch 24 additions): "Scene A replay (March 2020 haircut call) Fri 23 Oct 2026 3:05 p.m." should read "Thu 22 Oct 2026 3:05 p.m."
- Ch 19's H1-2022 replay ("played on Friday 23 October 2026 after the close") and Ch 21 Scene B ("run on Friday 23 October 2026", no time given) still share that Friday evening with each other and with the Ch 2-B 4:10 p.m. meeting; that is a tight spot but not a clash I could fix without moving a pinned scene (Ch 21's A/B pairing and Ch 19's "still on the whiteboard from the afternoon" both fix their day), so I left it. Ch 21's own Tue 27 Oct replay (Trinseo, "run on Tuesday 27 October") also shares the day with Ch 24's Sears replay (9:45 a.m. to 2:00 p.m.); times differ only if Ch 21's is an afternoon scene.

---

## [PB-03-financing] — status: fixed

**Found.** Ch 24 §24.7 box (line 639) summed half-spreads \$0.45mm + \$0.2mm and "the borrow and slightly negative carry for six months, about \$0.1mm" to "some \$0.75mm", so net \$0.5mm and capture "about two-thirds". Ch 8 §8.4 (the open box) prices a financing line, the long financed at the cash rate plus 40 bp on about \$22mm of market value, about \$0.09mm a year, with its running lines (carry, borrow, financing) about \$0.15mm over the six months. Recomputed in python3 (throwaway script in the session scratchpad):
- Financing over six months: 22 x 0.0040 / 2 = \$0.044mm, about \$0.05mm (Ch 8's \$0.09mm a year / 2 = \$0.045mm).
- Running lines: carry \$0.045mm + borrow \$0.065mm + financing \$0.045mm = \$0.155mm, matching Ch 8's \$0.15mm; Ch 24's existing "about \$0.1mm" covers carry + borrow (\$0.11mm).
- All-in: 0.45 + 0.2 + 0.1 + 0.05 = \$0.80mm (0.795 unrounded). Net = 1.25 - 0.80 = \$0.45mm. Capture = net / idio = 0.45 / 0.75 = 0.60 (0.607 unrounded; 0.60 using Ch 8's \$0.15mm).
- Old figures for the record: 0.75 all-in, 0.50 net, 0.667.
Not already fixed: the old text was still in place.

**Fix (Ch 24 §24.7, The Pair. box, "What it cost").**
Old: `...\$0.2mm out in a calmer September market, and the borrow and slightly negative carry for six months, about \$0.1mm: some \$0.75mm in all, against \$1.25mm gross, so the pair netted about \$0.5mm and its capture ratio, net over idio, was about two-thirds.`
New: `...\$0.2mm out in a calmer September market, the borrow and slightly negative carry for six months, about \$0.1mm, and the financing of the long at the cash rate plus 40 bp, about \$0.05mm (the line Chapter 8 §8.4 prices): some \$0.8mm in all, against \$1.25mm gross, so the pair netted about \$0.45mm and its capture ratio, net over idio, was about 0.6.`
The Wen short-pricing sentence that follows is unchanged.

**State.** `state/rv_pair_book.md` PB-03 row (three spots): capture cell `≈0.67 (net \$0.5mm / idio \$0.75mm)` → `≈0.60 (net \$0.45mm / idio \$0.75mm, financing included; was ≈0.67 before the 2026-10-18 cleanup)`; last cell `costs ~\$0.75mm all-in.` → `costs ~\$0.8mm all-in (half-spreads \$0.45mm in + \$0.2mm out, borrow and carry ~\$0.1mm, financing ~\$0.05mm).`; the Ch 8 weave note `is not in Ch 24's \$0.75mm all-in; with it ≈\$0.8mm, net ≈\$0.45mm, capture ≈0.6 (open item for Ch 24 §24.7)` → `was not in Ch 24's earlier \$0.75mm all-in; Ch 24 §24.7 now carries it (cleanup 2026-10-18): all-in ≈\$0.8mm, net ≈\$0.45mm, capture ≈0.6 (resolved)`. The idio-share cell (0.60 = 0.75 / 1.25) is unchanged and correct.

**Follow-ups for other owners (not edited; outside my named files).**
- `book_src/08_ch08d_the_pair_book_long_one_credit_short_another.md` line 220 (ledger table, PB-03 row) still prints capture `≈0.67`; it should become `≈0.60`. The Ch 8-D Figure 8-D.8 generator `tools/figures/ch08d*.py` hard-codes PB-03 kappa 0.67 (lines ~416, 464: assert `abs(kappa - 0.67) < 0.005`) and the PB-03 friction bar; both need the same update and a re-render. Ch 8 §8.4 itself needed no change.
- `state/cast_bible.md` line 148: "capture ≈ 0.67" should read "capture ≈ 0.6 (net \$0.45mm / idio \$0.75mm, financing included)".
- `state/open_items_ed2.md` line 49 (the §8.4 vs §24.7 row, status "open") can be closed.

---

## [SVB-8K-ch8] — status: fixed

**Found.** Ch 8 Case Study B (line 812) told the evening-of-8-March 8-K as carrying the \$23.97bn book value and \$21.45bn proceeds, the same misattribution fixed in Ch 4-B (4-B verify, item 1: those figures first appear in a later filing). Ch 4-B's corrected wording (line 270): the company "had sold substantially all of its available-for-sale book, at an after-tax loss of about \$1.8bn, and that it would raise \$2.25bn of capital. (A filing the following week put the sale at \$23.97bn of book value for \$21.45bn of proceeds...)".

Checked against the source: the 8 March 2023 8-K (SEC accession 0001193125-23-064680, fetched via WebFetch) says the sale of "substantially all of its AFS portfolio" "was completed today" and "will result in an after-tax loss of approximately \$1.8 billion in the first quarter"; it gives no book value or proceeds. Capital raise in the filing: a proposed \$1.25bn common offering, a separate \$500mm of Series F mandatory convertible preferred depositary shares, and a \$500mm General Atlantic common private placement contingent on the common offering. The filing does not itself state a \$2.25bn total (1.25 + 0.5 + 0.5 = 2.25 is a sum); the \$2.25bn is kept as in Ch 4-B and the dossier.

**Fix (Ch 8, Case Study B, "The tape that evening...").**
Old: `After the close, SVB Financial Group had filed an 8-K. Its bank had sold available-for-sale securities with a book value of \$23.97bn for proceeds of \$21.45bn, and the company was raising \$2.25bn of capital.`
New: `After the close, SVB Financial Group had filed an 8-K. It had sold substantially all of its available-for-sale securities, at an after-tax loss of about \$1.8bn, and was raising \$2.25bn of capital. (A filing the following week put the sale at \$23.97bn of book value for \$21.45bn of proceeds.)`
Nothing else in Ch 8 uses these figures; the fiction label's "the 8-K figures" and Ines's "You've read the 8-K" stay true. I wrote "the following week" rather than a date because the sources disagree (the Ch 4-B verify says 13 March; Ch 3 line 418 and Ch 6 line 466 say 14 March).

**Follow-up (not edited).** Ch 3 line 418 and Ch 6 line 466 already attribute \$23.97bn / \$21.45bn to a later 8-K (14 March), which is correct; the 13 vs 14 March discrepancy between those chapters and the Ch 4-B verify note should be settled by whoever owns the SVB dossier (the dossier lists 8-Ks of 13 (two) and 14 March).

---

## [ch19-74bp] — status: fixed

**Found.** Ch 19 §19.8.2 (line 683): "roughly 74bp all in, falling to about 35bp once both are evicted. (These are hand estimates on the synthetic basket. Your run will differ in the second digit.)" The code and Figure 19.5 give 76bp (full list, calm: \$1.56mm = \$829k handling + \$420k adverse selection + \$293k risk + \$16k hedge) and 37bp (lines 117 and 42 out, \$0.67mm); line 852 and the Figure 19.5 caption already say 76 / 37. Opened `assets/figures/ch19_cost_stack_by_scenario.png`: the bars read 76bp and 37bp, with the 45bp target line. So the figure and the text of line 852 agree; only the hand estimates differ, by 2bp each, because they are rounded arithmetic.

**Fix.** Kept the hand estimates (they are labelled as such and the §19.8.2 arithmetic is by hand) and replaced the vague parenthetical with one that says why they differ and gives the run's numbers.
Old: `(These are hand estimates on the synthetic basket. Your run will differ in the second digit.)`
New: `(These are hand estimates on the synthetic basket; the full run in Listing 19.8, plotted in Figure 19.5, gives 76bp and 37bp, so your run will differ in the second digit.)`
Listing 19.8 is `price_pt`, the listing Figure 19.5's caption names.

**Observation (not edited, not in the item).** Line 709 says cost per dollar falls "from about 76bp to 59bp to 36bp" using the Listing 19.5 loop with the adverse-selection vector, while line 852 and Figure 19.5 say 37bp for the same counter-proposal under Listing 19.8's `price_pt`. A 1bp difference between two listings; worth a glance by the Ch 19 owner. Lines 687 and 703 use "35bp" for the counter-proposal's concession (a bid, not a cost), which is a different quantity and is correct as written.

---

Item statuses: date-clash-24 fixed; PB-03-financing fixed; SVB-8K-ch8 fixed; ch19-74bp fixed.

## Review

Reviewer pass (2026-10-18). All four fixes are on disk (committed in the autosnap c6b9046 or earlier, so `git diff` shows nothing; read from the files and `git log -p`). Three confirmed as written, one confirmed with stragglers fixed.

**[date-clash-24] confirmed; stragglers fixed.**
- (a) Ch 24 lines 306-308 now read "this replay", "Thursday 22 October 2026, 3:05 p.m.", "Ines's replays", "This Thursday". 22 Oct 2026 is a Thursday (python3). No other "Friday" in Ch 24 refers to Scene A (lines 198, 326, 332, 420, 591 are generic or March 2020; line 696 "Not every replay waits for a Friday" is still true). (b) Italics, math and escapes untouched. (c) Straggler: `state/cast_bible.md` line 148 still said "Scene A replay ... Fri 23 Oct 2026 3:05 p.m."; changed to "Thu 22 Oct 2026". No other book_src or state file dates Scene A.
- Residual, not changed: Ch 3's debrief (Thu 22 Oct, 4:40 p.m., same four people: Ines, Theo, Kaz, Mags) follows Scene A by 95 minutes, and Scene A closes with "before anyone went home". Tight but workable; the Ch 21 Thursday memo scene ("late afternoon", Theo and Mags only) also sits on that Thursday. Ch 19 H1-2022 and Ch 21 Scene B still share Fri 23 Oct evening (both pinned), as the fixer said.

**[PB-03-financing] confirmed; stragglers fixed.**
- (a) Recomputed in python3: financing 22 x 0.0040 / 2 = $0.044mm; running lines 0.045 + 0.065 + 0.044 = $0.155mm (Ch 8's $0.15mm); all-in 0.45 + 0.2 + 0.1 + 0.05 = $0.80mm; net 1.25 - 0.80 = $0.45mm; capture 0.45 / 0.75 = 0.60 (0.595 unrounded). Ch 24 line 639 text is correct, escapes intact, cross-reference to Ch 8 §8.4 valid; `state/rv_pair_book.md` PB-03 row matches.
- (c) Stragglers fixed, one edit each: `book_src/08_ch08d_...pair_book...md` line 220 ledger capture `≈0.67` to `≈0.60`; `state/cast_bible.md` line 154 `capture ≈ 0.67` to `≈ 0.6, net $0.45mm / idio $0.75mm with financing`; `state/open_items_ed2.md` line 49 status `open` to `resolved`. Figure 8-D.8: `tools/figures/ch08d.py` PB-03 friction bar -100 to -150 (net 750 - 150 - 150 = 450, kappa 0.60), docstring and assert updated to 0.60, and `assets/figures/ch08d_pair_book_ledger.png` re-rendered (the script is deterministic: an unmodified run reproduced the old PNG byte for byte; the new PNG shows 0.60 for PB-03 and is otherwise unchanged). No other "0.67", "two-thirds" or "$0.75mm" tied to PB-03 survives in book_src, state or App Z.

**[SVB-8K-ch8] confirmed.**
- (a) Ch 8 line 812 now says "sold substantially all of its available-for-sale securities, at an after-tax loss of about $1.8bn, and was raising $2.25bn of capital. (A filing the following week put the sale at $23.97bn of book value for $21.45bn of proceeds.)", the same as Ch 4-B line 270; both 13 and 14 March are "the following week" of Wed 8 March, so the wording holds either way. (b) Dollar escapes intact; "the 8-K figures" in the fiction label and Ines's "You've read the 8-K" still true; the narrator's hindsight aside fits the scene's own "everyone already knows the ending". (c) $23.97bn / $21.45bn appear only in Ch 3 line 418 (14 March 8-K, Item 2.01), Ch 4-B, Ch 6 line 466 (later 8-K) and Ch 8, all attributed to a later filing. Ch 6 line 466 says the 8 March 8-K gave "about $21 billion" sold; Ch 8 does not use that figure, so no change, but the dossier owner may want to check it against the 8 March exhibit when settling 13 vs 14 March.

**[ch19-74bp] confirmed.**
- (a) Executed Listings 19.1-19.8 from App F (same method as `tools/figures/ch19.py`): full list, calm, $1,558k = $829k handling + $420k adverse selection + $293k risk + $16k hedge on $204.3mm = 76.3bp; lines 117 and 42 out $672k on $183.9mm = 36.6bp, i.e. 37bp. The new parenthetical in line 683 is correct and Listing 19.8 is `price_pt`. (b) Nothing else in the paragraph changed. (c) No other "74bp" or hand-estimate "35bp" survives (lines 687 and 703 use 35bp for the concession bid, a different quantity; App Z has no Ch 19 74/35).
- The fixer's side note on line 709 (36bp vs 37bp) is not an error: the Listing 19.5 loop (`evict_greedy`) excludes the hedge half-spread and returns 75.5, 58.9, 35.8bp, which round to the printed "76bp to 59bp to 36bp"; `price_pt` adds about 0.8bp of hedge cost to reach 76.3 and 36.6. No edit needed.

Reviewer edits: `state/cast_bible.md` (lines 148, 154), `book_src/08_ch08d_the_pair_book_long_one_credit_short_another.md` (line 220), `state/open_items_ed2.md` (line 49), `tools/figures/ch08d.py`, `assets/figures/ch08d_pair_book_ledger.png`.

<!-- STATUS: COMPLETE -->
