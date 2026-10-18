# Figure check: Chapter 1-B (ed2 U4)

Checked against tools/figures/style.py (house style), tools/figures/ch01b.py (the drawing code), the chapter text, and state/research/life_quant_shop_daily_life.md (Senate PSI figures). Every PNG was opened and viewed.

Findings that apply to the whole set (first pass, before fixes):
- Correctness: every number was recomputed from the chapter's own formulas (DTS, CS01, returns, ranks, the 2x2 table) and all match the chapter. No shape, tail or monotonicity problems (none of the figures draws a payoff, waterfall or distribution).
- Real-data claims: all trace to the Senate PSI report (pp.5, 6, 98, and p.112 n.675) as logged in the research file, including the "12-16 March 2012" window for the $161mm / $593mm shadow-sheet figures.
- Embedding: all five files exist, are numbered 1-B.1 to 1-B.5 in order, use the same `![Figure N-B.k: ...](assets/figures/...)` form as the other B/C chapters, and sit beside the paragraph they illustrate.
- Style: no figure uses aqua, yellow or magenta; no twinx; no in-image titles (the two panel headings in Figure 1-B.4 are panel labels, kept).

## Figure 1-B.1, ch01b_five_clocks

(per-figure verdict follows below, appended as the checks finish)

