# RV weave log: Ch 12-C (Edition 2, user directive 13)

*RV weaver, 2026-10-18. Thread entry: `state/rv_thread.md` §(e) row `12_ch12c_plan_valuation_dip_and_exit_as_derivatives` (scene; PB-07, PB-02; tool: the fulcrum as $\mathbb{P}(K_{j-1} \le V < K_j)$; H the direction of $V$ / I the class's call spread / L the DIP roll-up transfer $\kappa M(F-W)/(F(F-\kappa M))$ changes who the short is; Hertz 2020–21 plan, Ch 16 §16.6; home Ch 16; truth T6, co-owned with 12-B).*

## Preconditions
- `state/rv_thread.md` present and ends `<!-- STATUS: COMPLETE -->`.
- No prior `.rv.md` log; no `12_ch12c_...log.md` (not busy).

## Read
- `state/rv_thread.md` (spine, T6, homes, Ch 12-C row, PB-02 and PB-07 design rows, rules 1–10); `state/rv_pair_book.md` (PB-02: Owen's 0.38-by-face jump-neutral pair, closed in Ch 16 at 60 / 4; PB-07: replay cut 17 Jun 2020, 0.40 by MV, "Stressed in: Ch 12-C (planned; the market-test auction)", closed Ch 16); `state/cast_bible.md` (Owen, Wen, Marcus, Ch 16 Pair Book bullet, mandate: no groups); `state/reviews/ed2/u2_lessons.md`; `state/style_bible.md` §8.
- Dossiers (grep only): `rv_credit_pairs_literature_and_mechanics.md` R11 (bond borrow 173 / 245 bp around bankruptcy, recall on demand, 102% collateral; short-leg rule of thumb for distressed names); `rv_pod_platforms_and_risk.md` §4.4 (jump-neutral capital-structure pair).
- Elsewhere: Ch 12-B cold open and §12B.9 (structure, DIP 150 + 1:1 roll-up, 4.2 points, deathtrap warrants for 7.5% if the class votes yes, deltas 7.3 / 0.84 at 1,300); Ch 16 §16.6 (Hertz Docket Diary) and §16.8.3 (PB-07 / PB-02 close scene) and the Ch 16 RV log (open item: 12-C should stress PB-07 on Ch 16's terms); Ch 8-D §8D.2 (short-leg menu, Asquith fees); Ch 24 §24.6 (auction); `tools/figures/ch12c.py` (the chapter's model, used to recompute every new number).
- Chapter: grep for pair / hedge / idio / short / Hertz / pod found no RV content; read §12C.1–12C.2, §12C.4–12C.5, §12C.10, §12C.13 in full.

## Numbers (recomputed with `tools/figures/ch12c.py`, which re-asserts the chapter's printed values)
- Plan-value deltas under the §12C.1 mixture, per \$100mm shift: first lien (left behind) 6.05 points, unsecured 2.38 points; analytic form $\tfrac{32}{35}\pi_{1L}/1{,}250$ and $(\tfrac{3}{35}+\tfrac{32}{35}\pi_U)/1{,}020$ with $\pi$ = 0.828 / 0.172. $h_V$ = 2.54 (printed "≈ 2.5").
- At 0.38: long \$605k, short \$90k, net +\$515k per \$100mm (85% of the long).
- Implied committee weight: 7.25s at 66 → (66 − 59.7)/(95.2 − 59.7) = 0.18; 6s at 14 → (14 − 3.5)/(19.4 − 3.5) = 0.66.
- Per 100 of long: ratio 0.38 → 58.4 / 87.8 by expert, cost 60.7; ratio 2.5 → 51.0 / 46.7, cost 31.0 (engine mix 49.7, ≈ 19 points; ≈ 4.3 points short the kink at \$1,858mm).
- Since day 3 at 66 / 14: long −\$1.30mm, short +\$1.56mm. Roll-up 4.2 points = \$420k on \$10mm.
- Costs, ten weeks to the opinion: financing \$6.6mm × 5.5% ≈ \$70k; borrow (4.00% − 6.00%) on 102% collateral ≈ \$2k at 0.38, ≈ \$14k at 2.5; half a point each way on \$21mm extra face ≈ \$210k round trip.
- Grading (Monday after the opinion, Ch 16's close marks 60 / 4): 0.38 → −\$0.60mm + \$0.38mm = −\$0.22mm; 2.5 → −\$0.60mm + \$2.50mm ≈ +\$1.9mm.
- Exercise 7: $M$ = 280 with no extra roll-up: $V^\star$ = 2,000, $\pi_{1L}$ = 0.900, $\pi_U$ = 0.100; deltas 6.58 / 1.74; $h_V$ ≈ 3.8.

## What I wrote, and where
1. **Scene** `#### The Pair Book: one judge, two prices`, inserted at the end of §12C.10 (after Figure 12-C.5, before "### When to apply it, and when it breaks"). About 1,800 words including one five-column table and one display equation ($h_V$). Fiction label once at the top, italic: Owen's pod, Vantress, Wen, Marcus fictional composites; Halvorsen fictional; all positions, prices, fees, model outputs, P&L illustrative; PB-02 on the Halvorsen Files' clock; PB-07 a replay cut at the close of Wed 17 Jun 2020 with Hertz facts from §16.6. Setting: Vantress floor, the Friday after Docket No. 412, 7:20 a.m.; Owen, Marcus, Wen; no desk cast.
   - **Legs:** PB-02 long \$10mm face 7.25% secured notes (first-lien class, outside the ad hoc group; bought 79, marked 66) / short \$3.8mm face 6% 2031s (sold 55, marked 14), borrowed from an asset manager's lending desk via the prime broker.
   - **Hedge removes:** at 0.38 (recovery-weighted, flat on default at 60 / 5) the default, which has happened; the tool's plan-value ratio $h_V$ ≈ 2.5 by face would remove the direction of $V$. T6 stated once: near default the ruler flipped from spread to jump; after default it flips again, to plan value.
   - **Idio remains:** the class's call spread (both legs kink at \$1,858mm; a delta-flat pair is still ≈ 4 points short that corner) and the price disagreement: one judge, two prices (0.18 vs 0.66 against the engine's 0.30); ≈ 19 points at 2.5, part of which is the unpriced deathtrap warrant.
   - **Leaks:** the roll-up, 4.2 points (\$420k) on the long, unseen by the 6s; the group is long that third leg and the pod, kept out of groups by mandate, is its short; the guard $W \ge \kappa M$ decides whether the bill lands on the long (here, 910 vs 150) or partly on the unsecured short.
   - **Short leg named:** the borrowed 6s are the only short of the class; lender's ≈ \$30mm program, platform 20% single-lender cap (\$6mm), fee 2% → 6% (pointer to §8D.2's bankruptcy-window data), ballot recall before the voting record date; no CDS (settled at the §24.6 auction); old equity hedges nothing.
   - **Costs:** carry zero both legs (§506(b); missed day-30 coupon); financing, borrow and half-spreads as above.
   - **Decision card** (keep 0.38 or go to 2.5; write the face, the lender, what the pair is long afterwards); Owen keeps 0.38; wall sentence *PB-02 is long the first lien's call spread, 85% unhedged on plan value until the opinion; the only short is a ballot.*
   - **PB-07 stress** (one paragraph): the 0.40 ratio read as $h_V$; by spring 2021 the notes' fulcrum probability → 0, the stock's → 1, so $h_V$ → 0 and each short share was a position in the sponsor auction, short every raise; auction closed 11 May 2021, winning bid repaid the debt in full (§16.6). "In Hertz it was short an auctioneer." P&L not retold.
2. **Cross-reference to the canonical home:** "the close in §16.8.3, which ends both pairs" (scene) and "§16.8.3 is where Owen pays it" (Debrief).
3. **§12C.13 Desk Debrief:** one paragraph after Kaz's measure-change line grades Owen's card (−\$0.22mm at 0.38 vs ≈ +\$1.9mm at 2.5 had the borrow existed); one bullet, "After default the ruler flips again" ($h_V$, the ballot-bearing short, the roll-up guard).
4. **Exercise 7** (new, appended): PB-02's $h_V$ at \$280mm of new money with no extra roll-up, solved number-first (≈ 3.8).
5. **Ledger** `state/rv_pair_book.md`: PB-02 "Stressed in" gains the 12-C entry (Ch 12-B and 13 still unwritten) and its "What leaked" cell gains the roll-up and the warrant; PB-07 "Stressed in" rewritten from "planned" to the written 12-C beat; one Chapter-notes bullet with pair, legs, hedge ratio and method, chapter, status (both stay closed in Ch 16), idio, leaks, costs, borrow, card.
6. **Cast bible:** one Ch 12-C Pair Book bullet after the Ch 16 bullet (Marcus, Owen, Wen lines; new fact: Wen lends the borrow weather to Owen's pod when asked).

## Retired (one telling per fact)
- §12C.10 "What the market said": the 14-implies-two-in-three computation and the "first lien at 66 is within a risk premium and nine months of carry of 70.3" reading are now told in the scene (with the first lien's own implied weight, 0.18); the paragraph is reduced to a pointer that keeps both prices and the Law 16 line.

## Protected items
- No topic, numbered equation, Source Extraction, Trend Watch, exercise, figure, Appendix F link or URL removed. No code block added. Pandoc math only; currency escaped. Chapter last line still `<!-- STATUS: COMPLETE -->`. `tools/check_book.py` passes. Chapter 14,330 → 16,434 words.

## Open items and observations
- **No RV figure made.** The thread's optional "pair payoff over $V$ with moving attachment points" is scriptable from `tools/figures/ch12c.py` (`alloc`, `r_first`, `r_unsec`): pair value per 100 of long at ratios 0.38 and 2.5 against $V$, with $V^\star$ at $M$ = 0, 150, 280. Left for the U4 pass; if made it becomes Figure 12-C.6.
- **Ch 12-B's PB-02 box** (thread: hedge ratio across the machine's states; priming and burn move the attachment points) is unwritten; this scene uses only the roll-up as the leak and leaves priming to 12-B.
- **Ch 16 consistency:** the scene keeps Owen at 0.38 so Ch 16's close (\$3.8mm covered at 4, 7.25s sold at 60) stands. Ch 16 says the warrants turn "on a ballot his lender casts"; the scene says a lender who wants its ballot recalls before the voting record date, which is compatible.
- **Observation (not changed):** §12C.10 says "The unsecured class is short the *distance* between experts"; the two sensitivities printed beside it (committee 1,900 → 1,800 costs 1.8 points; debtor 1,300 → 1,200 costs 0.6) do not fit a pure distance exposure, and the sign reads as long the committee's level. Worth a chapter editor's look.
- Illustrative values introduced: the lender's ≈ \$30mm program, the 6% fee, the ten-week horizon, the 4.2-point roll-up booked to the DIP days in the explain.

<!-- STATUS: COMPLETE -->
