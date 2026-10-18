# Figures log: Chapter 4-D (ed2 U4)

Plan. No state/revisions/ed2 brief exists for 4-D; the chapter's advisor brief (state/advisor_briefs/04_ch04d_getting_the_seat.md, section 4) scripted three figures, and the chapter already EMBEDS all three
(Figures 4-D.1 to 4-D.3) but their PNGs were never drawn (assets/figures/ch04d_*.png did not exist, tools/figures/ch04d.py did not exist). So this run (a) draws the three embedded figures, so the existing
links resolve, and (b) adds three new figures from the Math, Gently boxes and the scenes. The brief's "alternative" for figure 3 (three rulers across four states) is NOT drawn: Chapter 8-D already has it
(Figure 8-D.3, "Three rulers, four market states"). Because one new figure lands between the old ones, the old captions are renumbered (old 4-D.2 -> 4-D.3, old 4-D.3 -> 4-D.4) and the one in-text reference to
"Figure 4-D.2" in the §4D.3 Poker Table box is updated to 4-D.3.
Final order: 4-D.1 interview_funnel (§4D.1, existing embed); 4-D.2 one_price_three_worlds (§4D.2, new); 4-D.3 live_counterparty_update (§4D.3, existing embed); 4-D.4 kelly_trapdoor (§4D.5, existing embed);
4-D.5 two_clocks_join (§4D.8, new); 4-D.6 sharpe_vs_cost (§4D.9, new).
Data: Theo, the five rooms, Kaz and every question are fictional composites, so every figure is Illustrative and drawn from numbers the chapter states or from its stated model (Bayes with one seller in five informed;
Kelly f* = (1-q)/L - q/c; a 16x-turnover cost model). No real series is used: the sourced dossiers (trend_figure_data_series.md etc.) hold no series for these scenes, and the chapter's real-world facts (TRACE volumes,
FINRA block-print counts, hiring announcements) are point quotations, not series. Every number in the figure script is asserted against the chapter's text (25% and 94, sd 26 and 20, the six posteriors, 0.926 and 0.280,
12.9% and 4.3%, IR 3.1 / 1.1 / 0.5, 32.5 and 38.75 bp).

## Embedded figures

All six are drawn by tools/figures/ch04d.py (run: python3 tools/figures/ch04d.py). Each PNG was opened and cleaned (see per-figure notes). All are under 260 KB.

- **Figure 4-D.1, ch04d_interview_funnel.png** (§4D.1, after the Sunday paragraph; EXISTING embed, PNG newly drawn): a 6-by-5 grid, stages (screen, puzzles, coding, pitch, portfolio, offer) top to bottom against five businesses (market maker,
  multi-strategy pod, systematic manager, bank desk, distressed fund); every cell names what the stage screens for and the section that trains it (the five cells the caption names are the darkest); shade = how heavily the business weighs the stage
  (rarely, lightly, fairly, most). Data: Illustrative composite (no firm's process); section pointers from §4D.1 to §4D.11 and the project weights from the closing table of §4D.11. Cleaned: header collisions (two-line names), cell text wrapped at 19 characters.
- **Figure 4-D.2, ch04d_one_price_three_worlds.png** (§4D.2, after the paragraph ending "being polite about it", before the Math, Gently box; NEW, with one pointer sentence): left, the bond that pays 100 or 40 at a price of 85 under Q (25% / 75%) and under an assumed P (10% / 90%),
  with triangles at the expected payoffs 85 and 94; right, the same price 85 as the mean of the three-door bond (40 / 70 / 100 at 10 / 30 / 60%), standard deviation 20 against 26 for the two-door bond. Data: Illustrative, the numbers of §4D.2 (asserted: means 85, 94, 85; sd 26.0 and 20.1).
  Cleaned: legend rows moved above the bars (axis extended to 1.3), triangle labels moved into the axis label, no label collisions.
- **Figure 4-D.3, ch04d_live_counterparty_update.png** (§4D.3, after the Poker Table box; EXISTING embed, old number 4-D.2, PNG newly drawn): left, the posterior that the bond is worth 40 after each of six trades, informed path (six sales: 0.60, 0.69, 0.77, 0.84, 0.88, 0.92) and noise path
  (sell, buy, sell, sell, buy, buy: 0.60, 0.50, 0.60, 0.69, 0.60, 0.50); right, the bid-ask band for the next trade on each path (spread 12 at the start, 3.7 after six informed sales; informed mid 70 -> 45.1; noise band 54 to 76). Data: Illustrative, the Bayes model of §4D.3 (asserted against the caption's two posterior lists).
  Cleaned: "prior" label and the sell/buy tags moved off the lines, noise-path label wrapped, band labels placed on the plot.
- **Figure 4-D.4, ch04d_kelly_trapdoor.png** (§4D.5, after the View From Another Seat box; EXISTING embed, old number 4-D.3, PNG newly drawn): the Kelly fraction as a surface over (q_D, L), drawn as five slices (q_D = 1%, 2%, 3.1%, 4.5%, 6%; SEQ_BLUE, light = low) on a log axis
  of position as a share of capital against L from 0.3 to 1.0, with the ruin line f = 1/L above them, the pod stop at 12.9% ($25.9mm on $200mm) and the single-default line at 4.3% ($8.6mm) as flat ceilings, Theo's dot at (0.6, 93%) and the same dot at L = 1 (Kelly 28%, ruin line 100%); curves
  end where the formula turns negative (no bet; 6% at L = 0.69, 4.5% at L = 0.93). Data: Illustrative, f* = (1-q)/L - q/c with c = 4.5% (asserted 0.926 and 0.280). Cleaned: end labels, the L = 1 ring moved off the q_D = 3.1% label, Theo's label moved into the empty lower left, note moved to the top right.
- **Figure 4-D.5, ch04d_two_clocks_join.png** (§4D.8, after the paragraph on the join; NEW, with one pointer sentence): top, five trades in one invented issuer (rated BB until a downgrade to B+ published 18 Mar 2025 and to CCC+ published 11 Sep 2025) and the rating each join attaches (as-of join, blue, against a merge on today's table, orange; the gray connector is the look-ahead,
  all of it for the three 2024 trades); bottom, a zoom on the 14 March 2025 trade, which falls between the downgrade's effective date (13 Mar) and its publication date (18 Mar): the join on the effective clock attaches B+, four days before anyone could know, and only the as-of join on the publication clock attaches BB.
  Data: Illustrative, an invented issuer and invented dates (the chapter says only that the merge carried today's rating and that 2024 trades knew 2025 downgrades). Cleaned: the two-clock effect was invisible in a single panel (five days on a two-year axis), so a zoom panel was added; label collisions and tick collisions fixed.
- **Figure 4-D.6, ch04d_sharpe_vs_cost.png** (§4D.9, after the paragraph on the costs set to zero; NEW, with one pointer sentence): the net information ratio (6.2% gross alpha less 16 dollars traded per dollar of book times the cost, over 2% tracking error) against the cost per dollar traded in bp: IR 3.1 at zero, 2.1 at 12.5 bp, 1.1 at 25 bp, 0.5 at 32.5 bp, zero at 38.75 bp; the shaded band is
  an eighth to a quarter point. Data: Illustrative, the numbers of §4D.9 (asserted 32.5, 38.75, 1.1). Cleaned: the band label moved to the bottom of the band, the end labels moved off the line.

Edits to the chapter (nothing else changed): renumbered the two old captions (4-D.2 to 4-D.3, 4-D.3 to 4-D.4) and the one reference to "Figure 4-D.2" in the §4D.3 Poker Table box (now 4-D.3); added a clause to the Kelly caption saying the surface is drawn as five slices (the figure is five slices on one panel, not a 3-D surface);
added the three new embeds, each with one pointer sentence at the end of the paragraph it illustrates and blank lines around.

## Flags for the orchestrator (not fixed: outside the figure edit's remit)
1. The chapter shipped with three embeds whose PNGs did not exist (and no ch04d.py). They resolve now. A grep of book_src found no other reference to "Figure 4-D.n" outside this chapter.
2. The brief's alternative figure (three rulers, four states) duplicates Figure 8-D.3, so it was not drawn. The table in §4D.6 is that figure's data (P&L numbers reproduce from DV01 arithmetic: for example +0.235 for the duration short when both widen 10%).
3. Figure 4-D.1 assigns the "puzzles" and "pitch" stages to businesses beyond the five cells the caption names (for example the pod's Kelly puzzle, the market maker's "break my backtest" pitch with Kaz) using the chapter's own scenes; cells for stages the chapter does not narrate (the pod's coding, the systematic manager's pitch, the bank desk's coding and offer, the distressed fund's puzzles and offer) are marked light or "rarely tested" and are illustrative.

<!-- STATUS: COMPLETE -->
