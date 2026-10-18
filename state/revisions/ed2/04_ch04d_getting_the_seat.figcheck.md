# Figure check: Chapter 4-D (ed2 U4, Edition 2)

Checked: book_src/04_ch04d_getting_the_seat.md, tools/figures/ch04d.py, the six assets/figures/ch04d_*.png (all re-drawn by the script, all viewed with the Read tool, all under 260 KB). House style read from the docstring of tools/figures/style.py. The figures log was COMPLETE.

Overall: 5 of 6 figures were mathematically right as drawn; 1 (Figure 4-D.4) had a real correctness error in the stop lines. Four legibility or style defects fixed. Two placement or pointer fixes in the chapter.

## Figure 4-D.1, ch04d_interview_funnel.png (the funnel by business): PASS (one tiny tweak)
- Correctness: not a data figure. The five cells the caption names are the five darkest ("most") cells, and they match the caption (market maker puzzles, pod pitch, systematic coding, bank puzzles, distressed pitch). The Portfolio row matches the two project tables of §4D.11 exactly (1,4,5 / 8,12 or a pair from 2 or 11 / 1,6,9 / 1,5,8 / 2,3,10,11). Section pointers (§3.7, §4D.5 ... §4D.11, §5.1.5, §28.2, Ch 8-D) match scenes in the chapter.
- Honesty: caption says "illustrative composite; no firm's process". Cells for stages the chapter does not narrate are shaded light or "rarely" (already flagged in the figures log).
- Legibility and style: single hue sequential shading, all text in ink, no collisions or clipping. Smallest text was 6.8 pt; raised the italic section pointers to 7.0 pt (matches the body text and the smallest size used elsewhere in the book).
- Embedding: syntax and file fine. The text never mentioned it; added one pointer sentence to the paragraph above it ("Figure 4-D.1 is that column filled in, one cell per room and stage"), which ties it to the "What they will actually test" column.

## Figure 4-D.2, ch04d_one_price_three_worlds.png (one price, two measures, three doors): PASS after one fix
- Correctness: left, Q 25%/75% gives mean 85 and P 10%/90% gives mean 94 (asserted); the triangles sit at 85 and 94. Right, three doors 10/30/60% on 40/70/100 give mean 85 (asserted), sd 20.1 against 26.0 for two doors, 40% not paid in full. All match §4D.2 and the caption.
- Honesty: caption says "illustrative: the numbers of §4D.2"; "assumed" physical 10% is stated as assumed.
- Legibility and style: AQUA (slot 3, below 3:1 on white) was used for the three-door bars with a legend and percentage labels but no direct name. FIX: added the direct label "three doors" above the bar at 70, which exists only in that bond. Everything else clean (legend rows above the bars, no collisions).
- Embedding: after the paragraph that says "Figure 4-D.2 draws both". Fine.

## Figure 4-D.3, ch04d_live_counterparty_update.png (live-counterparty update): PASS after one fix
- Correctness: recomputed from the model. Informed path 0.60, 0.69, 0.77, 0.84, 0.88, 0.92 and noise path 0.60, 0.50, 0.60, 0.69, 0.60, 0.50 match the caption (asserted). Quotes: 64/76 at the prior (spread 12), bid 58.5 after two sales (matches §4D.3's 58.5), informed spread falls monotonically to 3.7 with mid 70 to 45.1, noise band stays within 54 to 76. All match the text of §4D.3 and the Poker Table box ("climbs from 50% to 92%", "falls from 70 to about 45", spread "narrows").
- Honesty: caption states the setup and "(illustrative)".
- Legibility and style: the dashed 50% reference line ran through the noise-path end label. FIX: the line now stops at trade 6. One y-axis per panel (two panels), orange for informed and blue for noise, no slot 3 to 5 colors.
- Embedding: after the Poker Table box that cites it. Fine.

## Figure 4-D.4, ch04d_kelly_trapdoor.png (Kelly with a trapdoor): FAIL as found, FIXED
- Correctness (the main finding): Kelly f* = (1-q)/L - q/c is right (0.926 at q=3.1%, L=0.6; 0.280 at L=1; ruin line 1/L; curves fall monotonically in L and in q, as theory demands). BUT the pod stop (7.5% of capital) and the single-default line (2.5%) were drawn as flat lines against an L axis. A loss limit of $15mm (or $5mm) on a position that loses a fraction L on default allows a position of limit/L, so both ceilings fall as L rises; they equal the chapter's $25.9mm (12.9%) and $8.6mm (4.3%) only at L = 0.58 (the 98-dollar bond that recovers 40). A flat line understated how the document (uptier, L toward 1) also tightens the stop. FIX: both ceilings are now drawn as 7.5%/L and 2.5%/L, with a dot at L = 0.58 where they reproduce 12.9% ($25.9mm) and 4.3% ($8.6mm) (asserted against the chapter's numbers).
- Honesty: the note said a curve "ends where the formula turns negative", but the curves were cut at 3% of capital (the log axis cannot show zero). FIX: curves are cut at 5% of capital and the in-figure note says so ("a little further right f* is negative: no bet"); the 6% curve reaches zero at L = 0.705 and the 4.5% curve at L = 0.955. Caption updated to match (see below). Caption says "(illustrative)".
- Legibility and style: the end labels of the 4.5% and 6% curves were sitting on the bottom axis line (fixed by the new floor and a lower y limit; added a 2.5% tick, "400%" style tick labels kept); the 4.5% curve ran through the "same bond after an uptier" text (fixed: that label moved to the free space right of the ring, three lines, with a short leader). SEQ_BLUE used for one hue by q_D, light = low, direct end labels on every curve, one log y-axis, grid y only, text in ink. x axis extended to 1.36 to make room for the stop labels.
- Embedding: it sat after the "View From Another Seat" box at the end of §4D.5, four paragraphs from the stop paragraph it illustrates and with no pointer. FIX: moved to directly after the paragraph on the stop (before "So where does Kelly fit?"), with a pointer sentence at the end of that paragraph ("Figure 4-D.4 puts Kelly, the ruin line and the stops on one page."). Caption rewritten: the two loss limits are "ceilings that fall as 1/L", the 7.5% stop (\$15mm on \$200mm) allows \$25.9mm, 12.9% of the book, at L = 0.58 (the dot), the 2.5% line (\$5mm) allows 4.3% there, and each slice is cut at 5% of capital short of where the formula turns negative.

## Figure 4-D.5, ch04d_two_clocks_join.png (two clocks on one join): PASS
- Correctness: as-of join on publication dates gives BB, BB, BB, BB, B+ for the five trades; the naive merge gives CCC+ for all (printed by the script and read off the figure). The 14 March 2025 trade lies between the effective date (13 Mar) and the publication date (18 Mar): the effective-date join gives B+, four days (18 minus 14) before it could be known; the as-of join gives BB. The zoom window (8 to 26 March) matches the grey band on the top panel; the step dates sit at the right x positions.
- Honesty: an invented issuer and invented dates, said so in the caption ("illustrative"). The chapter's own claim (2024 trades knew 2025 downgrades) is what the top panel shows.
- Legibility and style: blue = as-of join, orange = naive merge, ink text, direct labels in both panels, two panels rather than a second y axis, no collisions or clipping. Slots 3 to 5 not used.
- Embedding: after the paragraph that says "Figure 4-D.5 shows what each join attaches to the same five trades". Fine.

## Figure 4-D.6, ch04d_sharpe_vs_cost.png (Kaz's Sharpe against cost): PASS
- Correctness: IR(c) = (6.2 - 16c/100)/2 is a straight line falling with cost: 3.1 at 0, 2.1 at 12.5 bp, 1.1 at 25 bp, 0.5 at 32.5 bp, 0 at 38.75 bp, all matching §4D.9 and asserted in the script. The shaded band (12.5 to 25 bp, an eighth to a quarter point) cuts the IR by about a third (3.1 to 2.1) to about two-thirds (3.1 to 1.1), as the caption says.
- Honesty: "illustrative: the numbers of §4D.9". The band label says "half-spread", the chapter text says "half-spread ... an eighth or a quarter of a point on a liquid bond"; consistent.
- Legibility and style: single blue series, a few direct labels (no number on every point beyond the chapter's own five), ink text, one y-axis, no collisions. The line leaves the plot at the lower right edge, which is ordinary clipping of data, not text.
- Embedding: after the paragraph that says "Figure 4-D.6 draws the whole line". Fine.

## Numbering and embedding (whole chapter)
Figures 4-D.1 to 4-D.6 appear in order, all six PNGs exist, all embeds use the correct `![Figure 4-D.n: ...](assets/figures/ch04d_....png)` syntax, each now has a pointer sentence in the text, and no other chapter cites a 4-D figure number.

## Files changed by this check
- tools/figures/ch04d.py (funnel pointer font size; "three doors" direct label; 50% reference line shortened; Kelly stop lines as limit/L with dots at L = 0.58, curve floor 5%, axis limits, ticks, note, annotation placement)
- assets/figures/ch04d_interview_funnel.png, ch04d_one_price_three_worlds.png, ch04d_live_counterparty_update.png, ch04d_kelly_trapdoor.png (re-drawn)
- book_src/04_ch04d_getting_the_seat.md (Figure 4-D.4 caption and position, pointer sentences for Figures 4-D.1 and 4-D.4)

## Flags for the orchestrator (not fixed)
- The chapter's single Kelly example uses L = 0.6 (recovery 40) while the stop arithmetic uses L = 0.58 (a bond at 98 recovering 40); the figure shows both honestly (Theo's dot at 0.6, the stop dots at 0.58), but the text could use one value.
- Figure 4-D.1 cells for stages the chapter does not narrate remain illustrative (as the figures log already notes).

<!-- STATUS: COMPLETE -->
