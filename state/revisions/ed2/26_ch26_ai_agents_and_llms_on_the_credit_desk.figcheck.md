# Ch 26 figure check (Edition 2)

Checked: tools/figures/ch26.py, assets/figures/ch26_*.png (5 files), embeds in book_src/26_ch26_ai_agents_and_llms_on_the_credit_desk.md. House style read from tools/figures/style.py. Numbers recomputed from the script's own functions (seed 26) and from closed forms.

Overall: all five figures are correct, honestly captioned ("Illustrative", no observed data plotted), and legible. Two cosmetic layout fixes, one axis-tick fix, one marker-clipping fix, and one caption fix were made. All PNGs were re-rendered and re-viewed after the fixes (85 to 130 KB each, under the 500 KB budget).

## Figure 26.1 ch26_citation_contract (section 26.4)
Verdict: PASS after one caption fix.
- Correctness: the decision path V -> S -> A matches the section 26.4 table row for row (V=0 fabricated pointer; V=1,S=0 footnoted hallucination, FH = mean V(1-S); V=S=1,A=0 stale support; V=S=A=1 good claim). Footer "S = 1 implies V = 1; no citation is V = 0" matches the text. Status colors (serious, critical, warning, good) are used for state and paired with text labels.
- Honesty: caption said "three deterministic checks", but A is graded against a labelled answer and S can be an LLM support test (chapter edge case iii), so "deterministic" overclaimed. Caption now reads "graded by three checks in order". "Illustrative" and the cold-open source are given.
- Legibility: no collisions or clipping. Body text is 7.1 pt, below the house 8 pt annotation size; accepted because the box widths are already full and shortening the chapter's named terms would break the layout. Recorded as a residual risk, not a defect.
- Embedding: file exists, blank lines before and after, placed right after the table and the stale-support paragraph that end "Figure 26.1 draws the same sorting as a decision path."

## Figure 26.2 ch26_calibration_power (section 26.4)
Verdict: PASS after one label nudge.
- Correctness: reader model matches Listing 26.2 in Appendix F (p_true = logistic(N(1.4, 0.9^2)), confidence = 1-(1-p)(1-overconf), overconf = 0.6, shuffle = permutation, 20,000 questions). Recomputed: ECE 0.0061 (calibrated) and 0.1435 (overconfident); AURC 0.1225 for both calibrated and overconfident, with identical curves (np.allclose True, as a monotone relabelling must give); shuffled AURC 0.2374, flat at the unconditional error rate, and all three curves meet at full coverage (0.2356 vs 0.2374 for the shuffled one, within sampling noise). Overconfident reliability points lie right of and below the diagonal, as they should.
- Honesty: caption gives the model, the sample size and "Illustrative"; ECE 0.14 matches the image (0.144) and the AURC values are in the image.
- Legibility: slot 3 (aqua) is used only for the shuffled curve and is direct-labelled with a dot and note, as the style requires. One y-axis per panel. Fix: the "Overconfident reader" label ran to the right spine; moved left (x 0.60 -> 0.52).
- Embedding: after the "Power, via selective prediction" paragraph, which ends "Figure 26.2 shows both properties for three simulated readers."

## Figure 26.3 ch26_abstention_threshold (section 26.5)
Verdict: PASS after one label nudge.
- Correctness: left panel plots (1-p)*C_FP for C_FP = 20 and 5 against the abstain cost of 1; the crossings are at p* = 0.95 and 0.80 and both lines reach 0 at p = 1. Right panel: p* = 1 - 1/r rises monotonically; coverage = P(p_true > p*) falls monotonically (checked numerically over r in [1, 200]); 50.6% (rounds to 51%) at r = 5 and 4.3% (4%) at r = 20, confirmed by simulation (50.8%, 4.3%).
- Honesty: caption says "Illustrative", states the cost unit and the source of the coverage numbers; "about half" and "about 4%" match the image labels.
- Legibility: direct labels on both right-panel curves (orange is used with labels; no slot 3 to 5). Fix: the "p* = 0.95" label touched the right spine; moved to x = 0.952, y = 2.0. The colors differ in meaning between panels (left: cost 20 vs 5; right: threshold vs share), but each panel has its own legend or direct labels, so left as is.
- Embedding: follows the boundary-conditions paragraph that ends "Figure 26.3 plots the comparison."

## Figure 26.4 ch26_chain_reliability (section 26.6)
Verdict: PASS after one tick fix.
- Correctness: p^n at n = 10 gives 0.904, 0.599, 0.349 (labelled 0.90, 0.60, 0.35); pass@5 = 1-0.3^5 = 0.9976 (0.998) and pass^5 = 0.7^5 = 0.168; pass^k decreases and pass@k increases, as theory demands; they coincide at k = 1 (0.7).
- Honesty: closed forms, "Illustrative" in the caption; "17%" is 0.168 rounded.
- Legibility: three shades of one blue hue for an ordered parameter (p), direct end labels; no collisions. Fix: the k axis had ticks 1, 2, 4, 6, 8, 10, so the annotated k = 5 had no tick; ticks now run 1 to 10.
- Embedding: after the "Proof." paragraph that ends "Figure 26.4 plots both ideas."

## Figure 26.5 ch26_luck_hurdle (section 26.7)
Verdict: PASS after one clipping fix.
- Correctness: formula sigma*[(1-gamma)Phi^-1(1-1/N) + gamma*Phi^-1(1-1/(Ne))] with sigma = 0.5 gives 0.9504 at N = 20 and 1.7236 at N = 2,000 (chapter and caption: 0.95, 1.72). The simulated mean-of-max points (4,000 or 1,500 replications per N) sit on the curve (e.g. N = 2: 0.29 vs exact 0.282); the curve is increasing and concave in log N, as expected.
- Honesty: caption says what the line and dots are, with sigma_SR = 0.5 and "Illustrative"; the legend says the same.
- Legibility: one y-axis, two series in slots 1 and 2, annotations clear of the curve. Fix: the N = 10k simulated marker was half-clipped by the axes edge; set clip_on=False, re-rendered, and the marker is whole.
- Embedding: after the paragraph that ends "Figure 26.5 plots the hurdle against the number of trials."

## Embedding summary
Five embeds, all with correct `![Figure 26.k: ...](assets/figures/ch26_*.png)` syntax, all five files exist, numbered 26.1 to 26.5 in order of appearance (lines 193, 221, 245, 313, 363), each with a blank line before and after and a pointer sentence in the preceding paragraph. No ch26_*.png is embedded elsewhere and no embedded figure is missing.

## Changes made
1. tools/figures/ch26.py: Figure 2 overconfident-reader label moved left; Figure 3 "p* = 0.95" label moved off the spine; Figure 4 k-axis ticks 1 to 10; Figure 5 simulated markers clip_on=False. Script re-run, all five PNGs rewritten and re-viewed.
2. book_src/26_ch26_ai_agents_and_llms_on_the_credit_desk.md: Figure 26.1 caption, "three deterministic checks" -> "graded by three checks".

Residual (not fixed): Figure 26.1 body text is 7.1 pt (flowchart density); Figure 26.3 right-panel sampling note: coverage figures are computed from the logistic-normal difficulty distribution analytically, while the chapter's Listing 26.2 reports "about 5% of those wrong" from its own seed (this figure's seed gives 3.8%); the figure does not plot that number, so no change.
<!-- STATUS: COMPLETE -->
