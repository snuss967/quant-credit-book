# Figure check (Edition 2): Chapter 4-C, Other Seats at the Table

Checked: five embedded figures (ch04c_*.png), the script tools/figures/ch04c.py against the house style in tools/figures/style.py, the chapter's embeds and captions, and the §12B.9 cap table. Every PNG was opened before and after the fixes. Baseline check: re-running the script reproduced the five PNGs byte for byte, so the script is the source of the images. All PNGs are under 200 KB, no twinx, one y-axis per panel, seat colours in fixed order (dealer blue, systematic orange, pod aqua, CLO yellow, insurer magenta, direct lender green, opportunistic violet; the desk is ink), slots 3 to 5 direct-labelled, text in ink or muted ink.

Embedding (all five): syntax `![Figure 4-C.n: ...](assets/figures/ch04c_x.png)` with blank lines around; all five files exist; numbered 4-C.1 to 4-C.5 in document order; the in-text pointers ("Figure 4-C.2 draws the box", "Figure 4-C.3 shows why...", "Figure 4-C.5" in 4C.8) agree with the numbers. Placement is next to the illustrated paragraph in each case (cold-open closing paragraph; after the horizon Math, Gently box; after the OC paragraph; after the accounting box; after the day-30 walk of the table). No other chapter refers to a 4-C figure number, so the earlier renumbering is safe.

## Figure 4-C.1, ch04c_seven_clocks.png: PASS after fixes
- Correctness: the horizons, check cadences and triggers agree with the §4C.9 table (dealer days, daily; systematic months, each rebalance; pod months to a year, daily; CLO reinvestment period, monthly; direct lender three to five years, quarterly tender; opportunistic years, no cadence; insurer decades, year-end; desk days to weeks, daily, trigger a price). Log axis ticks right.
- Honesty: caption now says what bar and diamond mean, that the desk's row comes on top of the seven seats ("Seven clocks, and the desk's", fixing the earlier "seven clocks, eight rows" mismatch), that ordering is rough, and that bar ends are drawn from the table (Illustrative).
- Legibility: raised the small text (rule lines 7.4 to 7.8 pt, headers and the "no diamond" note to 8 pt); removed a no-op annotate call. Right-column text ends inside the margin; no collisions.

## Figure 4-C.2, ch04c_horizon_flips_sign.png: PASS after fixes
- Correctness: recomputed the model. Gain 0.036T, swing 1.5 sqrt(T): 0.7 and 6.7 at 20 days, 9 and 24 at 252. Stop-touch probabilities 0.42 (Dana) and 0.41 (pod) from the reflection principle with drift; expected drift collected 0.54 and 6.73 via E[min(tau, T)]; exit cost 1.26 and 1.22; net -0.72 and +5.51. These agree with the box (about 0.45 and about four in ten; drift at most 0.7; pod 6 to 7; cost about 1.3 and 1.2).
- Fix: the break-even note said "about 1,760 days" (exact 9/252) while Exercise 2 says 1,740 (0.036 rounded). Changed the figure to 1,740 so the book gives one number.
- Honesty: caption now also states the nets (about -0.7 and +5.5) that the right panel shows; source line is "Illustrative" with the model stated.
- Note, not changed: the reflection formula assumes continuous monitoring. A daily-close simulation gives stop-touch rates of about 0.35 and 0.375, so the book's 0.42 and 0.41 are the continuous-time upper figures. The chapter and the caption both name the reflection principle, and the sign flip survives (Dana's net is about -0.5 on daily closes against -0.7), so no change.
- Legibility: no collisions; direct labels on both coloured markers.

## Figure 4-C.3, ch04c_cheapest_cure.png: PASS, no change
- Correctness: cost = 2(1 - p/100) falls monotonically with the price sold; points 0.84 (58), 0.46 (77), 0.28 (86); do-nothing level 0.84; second pool 0.46, 0.68, 0.92, with the highest-priced loan cheapest in each pool. Matches the Math, Gently box and Kundu (2023) rule.
- Honesty: caption cites the box, Kundu (2023) and says the second pool's 66 and 54 are invented.
- Legibility: labels clear the line and each other; yellow is the CLO seat and is direct-labelled.

## Figure 4-C.4, ch04c_one_path_seven_ledgers.png: PASS after fixes
- Correctness: prints 92, 78, 81, 74, 72, 76, 70 on days 1, 2, 4, 12, 16, 23, 30; desk -1.68 on 12mm at day 2; dealer 15 in at 91.25, out on day 3 at 79, realized -1.84 (12.25 points on 15mm = 1.8375), 40 block day 16 sold at 72; systematic exit of 8 at 77 on day 2; pod -0.5 on day 12; CLO -0.84 on day 9, -0.28 after the day-11 sale; insurer flat 99; direct lender 92 then 81 (half of the 22-point move, as in the box).
- Fixes: (a) the desk panel is now titled "if held", because the desk's 5-point stop would have fired on day 2 and the chapter never says Theo kept the position; (b) the pod panel is drawn as a line with markers like the desk's, instead of a step, so the two daily marks look alike; (c) the "market" label in the two bottom panels sat on the end of the grey line, so it moved to the empty space under the line; (d) the desk annotation moved down for clearance.
- Honesty: caption now lists the print days, flags "if held", the dashed day-9 downgrade line, and that the direct lender's day-30 quarter-end is an assumption (also stated in the panel); "seven P&Ls" became "seven different ledgers" since two panels show holdings.
- Legibility: shared x axis, titles carry units, no collisions after the fixes.

## Figure 4-C.5, ch04c_coalition_map.png: PASS after fixes
- Correctness: cap table matches §12B.9 (150, 900, 500, 600, 250, 150, 60; bar widths proportional; first-lien class = TLB plus 7.25s as in the §4C.7 box). Holdings match the chapter: systematic out at 77, CLO a Caa1 loan, dealer flat, pod long 10 and short 3.8, opportunistic fund 40, insurer through the CLO tranche, direct lender 15 in the liquid sleeve. Flows 8, 10, 40, 40 on days 2, 3, 16, 16 match the text.
- Fix (dated event): the declined arrow said "declined on day 16". In 4C.6 the committee declines at the Tuesday meeting on day 14; day 16 is when it becomes visible to the sponsor's bankers. The label now reads "declined at the day-14 committee", and the caption says so.
- Fix (legibility): text of 6.6 to 6.9 pt in the flow ladder, dot labels, legend and class bands raised to 7.4 to 7.6 pt; the flow ladder shifted down 0.6 so the "8" no longer crowds the CLO header dot. No collisions after the change.
- Honesty: caption gains the dot/ring key, the $200mm asked, and an explicit "Illustrative" source line.

## Flags (outside the figure edit; not changed)
1. Calendar: 4C.6 says "the Tuesday investment committee on day 14", but with day 1 a Friday and day 3 a Tuesday, day 14 is a Wednesday (a Tuesday is day 13), and the holiday would push it later. Left for the chapter author; the figure uses "day 14" only.
2. The advisor brief has the dealer winning at 90.75 and the chapter 91.25; the figures follow the chapter.
3. Figure 4-C.1 is placed in the cold open with no pointer sentence; it is fine where it is, and a one-line pointer could be added.
4. output/Quant_Credit_Master_Book.md holds the old Figure 4-C.1 caption until the next build.

## Files changed
tools/figures/ch04c.py (labels, fonts, desk/pod panels, dated label); assets/figures/ch04c_seven_clocks.png, ch04c_horizon_flips_sign.png, ch04c_one_path_seven_ledgers.png, ch04c_coalition_map.png (regenerated; ch04c_cheapest_cure.png regenerated identically); book_src/04_ch04c_other_seats_at_the_table.md (captions of Figures 4-C.1, 4-C.2, 4-C.4 and 4-C.5 only).
<!-- STATUS: COMPLETE -->
