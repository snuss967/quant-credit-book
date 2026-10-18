# Ch 26 figures log (Edition 2, task U4)

Script: tools/figures/ch26.py (run `python3 tools/figures/ch26.py`; writes assets/figures/ch26_*.png).
Note: no brief (section 3) and no state/research/trend_figure_data_series.md existed for this chapter. No observed data is plotted: every quantity in the chapter is a closed form or the section 26.12 simulated reader, so all captions say "Illustrative". Figures were chosen from the chapter's own headings and equations. The reader model (difficulty = logistic of N(1.4, 0.9^2); stated confidence = 1-(1-p)(1-overconf); shuffled confidence for the no-power reader) was re-created from Listing 26.2 in Appendix F.

## Embedded

1. **ch26_citation_contract** (Figure 26.1, section 26.4, after the "stale support" paragraph that follows the four-cell table). Flow graph drawn with matplotlib patches: a claim (text, d, pi, [a,b), p-hat) passes V (pointer resolves), S (span supports), A (assertion correct); each "no" exits to a named, status-coloured cell (Fabricated pointer, Footnoted hallucination, Stale support) with its credit-desk example and who catches it; "yes" all the way is a Good claim. Data: none (the chapter's own definitions and table; section 6.08(b)(xiv) from the cold open).
2. **ch26_calibration_power** (Figure 26.2, section 26.4 "Calibration and selective prediction", after the risk-coverage paragraph). Left: reliability diagram of a calibrated reader (ECE 0.006) and an overconfident one (ECE 0.144). Right: risk-coverage curves, where the calibrated and overconfident readers coincide (AURC 0.123) and the shuffled-confidence reader is flat at the unconditional error rate (AURC 0.237). Illustrative: 20,000 simulated questions from the section 26.12 reader model, seed 26.
3. **ch26_abstention_threshold** (Figure 26.3, section 26.5, after the p* boundary-conditions paragraph). Left: expected cost per claim of answering, (1-p)*C_FP for C_FP = 20 and 5, vs abstaining (cost 1), crossing at p* = 0.95 and 0.80. Right: p* = 1 - C_abs/C_FP and the share of claims a calibrated reader may answer vs the cost ratio (51% at 5 to 1, 4% at 20 to 1). Illustrative: closed forms of section 26.5; coverage from the difficulty distribution of the section 26.12 reader.
4. **ch26_chain_reliability** (Figure 26.4, section 26.6, after the pass^k "Proof." paragraph). Left: success probability of an n-step chain at p = 0.99, 0.95, 0.90 (0.90, 0.60, 0.35 at n = 10). Right: pass@k vs pass^k for p = 0.7 (0.998 vs 0.168 at k = 5). Illustrative: closed forms of section 26.6.
5. **ch26_luck_hurdle** (Figure 26.5, section 26.7, after the paragraph on the 20-variant human vs 2,000-trial agent hurdles). Expected maximum Sharpe ratio of N zero-alpha trials vs N (log axis), formula of section 26.7 with sigma_SR = 0.5 (0.95 at N = 20, 1.72 at N = 2,000) against a simulated mean of the best of N normal draws. Illustrative.

## Considered, not drawn (cap of five)
Charlotin database breakdown by party and by nature of error (2,199 decisions; chapter-quoted counts, would be real data but the figure adds little beyond the Trend Watch box); retries buy coverage with accuracy (precision 0.961 to 0.943 as coverage rises 0.83 to 1); Trend Watch timeline 2022-2026; lost-in-the-middle U-curve (only the toy harness version exists, no sourced numbers); Knight Capital timeline.

## Chapter edits
Five insertions only (one per figure, each with a blank line before and after); each appends one short pointer sentence to the preceding paragraph ("Figure 26.k ...").
<!-- STATUS: COMPLETE -->
