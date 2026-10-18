# Figures log: Chapter 1 (ed2 U4)

Plan (from section 3 of state/revisions/ed2/01_ch01_anthology_and_landscape.brief.md, and the three FIGURE placeholder comments the chapter already carried; no figure was embedded yet). Script: tools/figures/ch01.py. Five figures, ordered by appearance:

1. ch01_bid_decomposition (cold open, "The cold open, in numbers", placeholder slot): the bid as a waterfall.
2. ch01_gauss_vs_jump (end of 1.3.3, after Kaz stops defending the quadratic): the Gaussian bag against the jump bag, and the exact-to-quadratic jump charge.
3. ch01_price_pressure_decay (1.8.1, after the half-life paragraph): eq. (1.7), the dent that heals and the permanent part that does not.
4. ch01_forced_seller_flow_graph (1.8.2, Decision point, placeholder slot): the Listing 1.3 demo as a flow graph, with the Fed as a dashed hypothetical and the PB-01 pod edges.
5. ch01_march2020_timeline (1.8.3, after the post-mortem): March 2020 dated events against a real spread series.

Skipped on purpose: ch01_dd_gauss_vs_empirical (the only real point on the empirical map is Bohn-Stein's DD = 4 -> almost 1%; the rest of the curve would be invented) and ch01_serta_capital_stack (the Docket Diary and the box carry the numbers; five figures is the cap).

## Embedded figures

1. Figure 1.1, ch01_bid_decomposition (Cold open numbers, section 1.3.3, in the placeholder slot after "Kaz typed. The toxicity term is 0.6 x 13 = 7.8 points ..."; the placeholder comment was replaced by the figure): waterfall from the composite mid 91.97 through the inventory term (-0.317) and cost (-0.25) to Kaz's 91.40, then the toxicity step (-7.8 = 0.6 x 13) to Theo's 83.60, with Monday's open at 78 as a dashed line; the axis starts at 76 and says so. Data: Illustrative; recomputed in the script from eq. (1.2) and the chapter's inputs (asserts 0.317, 91.40 and 83.60).
2. Figure 1.2, ch01_gauss_vs_jump (section 1.3.3, after "Kaz put a fifty-point jump ... stopped defending the quadratic", with a one-sentence pointer appended to that paragraph, before the Ways This Blows Up box): left, the probability of losing at least x points over five days on a log axis for the Gaussian bag (mean loss 1, sd 7) against the jump bag (2% chance of losing 50; same mean and sd): 1 in 800 billion against 1 in 50 at a 50-point loss; right, the exact CARA jump charge divided by the quadratic charge, 2(e^x - 1 - x)/x^2 with x = gamma q ell, marked at 0.6 (the quadratic is 19% short) and 3 (a factor of 3.6). Data: Illustrative; the Math, Gently example and the Full Derivation formula, recomputed in the script (asserts 19% and 3.6).
