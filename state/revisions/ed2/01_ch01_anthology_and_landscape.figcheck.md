# Figure check: Chapter 1 (ed2 U4)

Checked against tools/figures/style.py (house style), tools/figures/ch01.py (the drawing code), the chapter text, Listing 1.3 in Appendix F, and Chapter 1-B (pod PB-01). Every PNG was opened and viewed before and after the fixes (the two densest regions were also cropped and enlarged). Baseline: re-running `python3 tools/figures/ch01.py` before any edit reproduced all five PNGs byte for byte, so the script is the source of the images. All five are under 205 KB.

## Whole-set findings

- Correctness: every number was recomputed from the chapter's formulas and inputs (eq. 1.2, the Full Derivation, eqs. 1.6 and 1.7, Listing 1.3). All match. The script asserts the key values (0.317, 91.40, 83.60, 19%, 3.6, 12.9, 6.5, 6.4, 4.31).
- Real data: the only real series is FRED BAA10Y. The cached CSV (tools/figures/data/ch01_BAA10Y.csv) was compared with a fresh fetch of fredgraph.csv for 2 Mar to 3 Apr and 1 May to 31 Dec 2020 (the stretches drawn and quoted): 0 differences in 200 daily values, including 2.44 on 2 Mar, 4.31 on 23 Mar and 2.18 on 31 Dec. Dated events agree with the chapter's own sourced text (§1.8.2 Acts 1-3, §1.8.3).
- Embedding: all five files exist; the form `![Figure 1.k: ...](assets/figures/ch01_*.png)` is the one build_book.sh rewrites to ../assets/figures/; numbered 1.1 to 1.5 in order of appearance; dollars escaped as \$ in captions; each sits beside the paragraph it illustrates (details below). No stray FIGURE placeholder comments remain in the chapter.
- Style: no title in any image; no twinx; one y-axis per panel; no aqua, yellow or magenta; BLUE, ORANGE and VIOLET keep the roles declared in the script docstring across the chapter (BLUE fair value / Gaussian / absorbers / the Fed, ORANGE forced seller / inventory / dealer residual, VIOLET toxicity / jump bag / permanent part). VIOLET is slot 7, with slots 3-6 skipped; accepted as the deliberate, documented, chapter-consistent choice (same as Chapters 1-B, 3-B, 4-B, 6-B, 8). Every series is direct-labelled.
- Text: all annotation text is 8.0 pt or larger. Several 8 pt notes were in MUTED (#8a8984, about 3.5:1 on white), including the "Illustrative" tag inside Figure 1.4 and the parameter note in Figure 1.3; all are now INK_2 (same fix as the Chapter 9 and 8-B checks). A local `note_ink()` replaces the house `note()` for the two parameter notes.

## Figure 1.1, ch01_bid_decomposition: PASS after caption fix

- Correctness: S - inventory - c = 91.97 - 0.31746 - 0.25 = 91.4025 (printed 91.40); less pi x J = 7.8 gives 83.6025 (printed 83.60). The three steps sum to the total drop of 8.37; the toxicity step is 13.8 times the other two combined, so "more than ten times" holds. The 78 line is Monday's open as in the cold open. The bars are floating and connected; the y-axis starts at 76 and the axis label says so.
- Honesty: caption says Illustrative and lists the inputs. Fixed: it said "the third term is most of the bid", but the image shows a concession from the mid, and 7.8 is 8.5% of the bid. It now reads "the third term is 93% of the 8.4-point concession from the mid" (7.8 / 8.37 = 93%).
- Legibility: no collisions (the "ten times" note and the right-hand note had already been separated); grey notes raised from MUTED to INK_2.
- Embedding: in the slot right after "Kaz typed. The toxicity term is 0.6 x 13 = 7.8 ...", before the paragraph that begins "Drawn as a waterfall". OK.

## Figure 1.2, ch01_gauss_vs_jump: PASS after fixes

- Correctness: left, the Gaussian loss is N(1, 7): P(loss >= 50) = sf(7) = 1.28e-12, one in 780 billion (caption: about one in 800 billion). The jump bag is a plateau at 0.02 out to 50 and then a drop to zero (dashed vertical), so the tail has the right shape and the right end point; both bags have mean loss 1 and sd 7 (sqrt(0.02 x 0.98) x 50 = 7.0). Right, the ratio 2(e^x - 1 - x)/x^2 is exactly the Full Derivation's last term over its quadratic cousin; it starts at 1, increases monotonically, is 1.234 at 0.6 (quadratic 19% short) and 3.575 at 3 (a factor of 3.6).
- Legibility fix: the "at 0.6 ..." annotation sat on the curve (the purple line ran through "Gaussian" and "short"). Moved below the curve with its leader line, set on three lines, clear of the "quadratic = 1" tag. Added "(exact is 1.23x as large)", because the y-axis shows exact divided by Gaussian (1.23) while the text says 19% short; the two are the same fact seen from either side.
- Honesty: caption matches the image, says Illustrative, and cites the Math, Gently example and the Full Derivation, which follows the figure. The 19% and 3.6 agree with the Full Derivation's closing sentence.
- Embedding: directly after "Figure 1.2 shows what he was looking at.", before the Ways This Blows Up box. OK.

## Figure 1.3, ch01_price_pressure_decay: PASS

- Correctness: dent = kappa x I/ADV = 0.4 x 12.8 = 5.12; half-life ln 2 / (1/20) = 13.9 days (marker at 13.86 on -2.56, caption "14 days"); recovered by day 60 = 5.12 x (1 - e^-3) = 4.87; permanent part 0.25 x 13 = 3.25 as a dashed floor; day-0 informed level 3.25 + 5.12 = 8.37. Both curves are monotone and tend to 0 and to -3.25 respectively. Matches eq. (1.7) and the Listing 1.3 demo (I = 6.4, ADV = 0.5).
- Honesty: caption says Illustrative, gives kappa, I/ADV, theta and the permanent pi x J from eq. (1.2); the informed curve keeping the same 5.12 temporary dent is stated as "plus a permanent pi J".
- Legibility: no collisions; the dot-and-text direct labels sit in free space; parameter note raised to INK_2.
- Embedding: after the half-life paragraph, which names "Figure 1.3". OK.

## Figure 1.4, ch01_forced_seller_flow_graph: PASS

- Correctness: the script recomputes Listing 1.3: sells 5.0 + 4.0 + 3.0 + 0.9 = 12.9; capacity 3.0 + 1.5 + 2.0 = 6.5; residual 6.4 (asserted). Ribbons are each seller's sale split pro rata over the four buyers (the listing's edges), all on one scale (2.9 units per \$bn), so node heights equal the sums of their ribbons and ribbon widths are to scale. The conservation law holds on both sides. Percentages (100% of 5.0, 50% of 8.0, 25% of 12.0, 10% of 9.0) match the listing's rules. The pod box matches the chapter's The Pair box and Chapter 1-B: long \$60mm Kestrel bought from dealers, short \$39mm Halvorsen borrowed from an asset manager, recall as a trigger with f = 1 and a window of one settlement cycle. The Fed node is dashed and labelled hypothetical, "from day 10, \$5bn (Exercise 4)", as in Exercise 4.
- Honesty: caption is Illustrative, cites Listing 1.3 (eq. 1.6), calls the Fed node Exercise 4's counterfactual and the pod the Chapter 1-B composite. It does not reveal the April answer beyond what Theo and Kaz already say aloud in the scene.
- Legibility: no clipped text (the longest label ends inside the image edge); the "Illustrative" tag and "downgrade to HY" raised from MUTED to INK_2.
- Embedding: in the Decision point slot, after "Figure 1.4 is the graph to write it against." and before "What happened, and the answer". OK.

## Figure 1.5, ch01_march2020_timeline: PASS

- Correctness (real data): checked against a live FRED fetch (above). Event verticals land on the right days (pixel positions of 12, 13, 23, 25, 31 Mar and 9 Apr agree with the 9 Mar / 23 Mar / 6 Apr / 20 Apr ticks, which are Mondays). Peak 4.31 on 23 Mar, the day the SMCCF was announced; 25 Mar S&P cut of Ford to BB+; 31 Mar month-end rebalance with about \$36bn leaving the IG index; 9 Apr expansion to issuers IG on 22 Mar; ETF buying from 12 May, bonds from June (drawn at month level), all ending 31 Dec. Each is what §1.8.2 and §1.8.3 say. The scale change at 1 May is visible and named in the caption.
- Honesty: the caption lists a source for every real claim (FRED BAA10Y; WealthManagement.com, 16 Mar 2020; Bloomberg; T. Rowe Price, Nov 2020; Federal Reserve; New York Fed, 11 May 2020), and the in-image note says the line is a market-wide gauge, not a Ford series.
- Legibility: lane labels and event labels sit on grey backing so the dashed verticals do not strike through text; nothing clipped; note raised to INK_2. The 12 and 13 Mar dots are 11 px apart but distinct.
- Embedding: after the post-mortem paragraph that names "Figure 1.5", in the 1.8.3 case study. OK.

## Not changed, noted for the text editor

- Body text after Figure 1.1: "The third term is most of the bid." (§1.3.3, the paragraph after the figure) says the same loose thing the caption used to say: the toxicity term is most of the concession from the mid, not most of the bid. The caption is now precise; the sentence was left alone as outside this task.
- Act 2 describes the SMCCF as a node "with a capacity so large that the line width broke the plotting library's default scale", while Exercise 4 and Figure 1.4 draw a \$5bn Fed from day 10. They are different Feds (the figures log already says so); Figure 1.4 draws only the exercise's.

## Files changed

- /home/user/quant-credit-book/tools/figures/ch01.py (note_ink helper; MUTED text to INK_2; Figure 1.2 annotation moved off the curve and given the 1.23x ratio)
- /home/user/quant-credit-book/assets/figures/ch01_bid_decomposition.png, ch01_gauss_vs_jump.png, ch01_price_pressure_decay.png, ch01_forced_seller_flow_graph.png, ch01_march2020_timeline.png (regenerated and re-viewed)
- /home/user/quant-credit-book/book_src/01_ch01_anthology_and_landscape.md (Figure 1.1 caption, one clause)
<!-- STATUS: COMPLETE -->
