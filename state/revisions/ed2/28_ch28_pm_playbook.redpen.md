# Red-pen log (Edition 2): book_src/28_ch28_pm_playbook.md

Items: C9, D7. Sources read: synthesis rows C9 and D7; desk-head review (problem 11, dashboard table, `DESK` Sharpe, action 5); transition-coach review (gap 10, red-pen 7).

## C9: §28.9 dashboard

- Table: added a P&L row (day, MTD, YTD vs budget; unexplained $U$; hedge and basis lines; points to §8C.4 and §8C.2), a Risk vs limits row (limit-sheet lines vs soft/hard thresholds; Table 8-B.4, §8B.9; breach rule taken from that table's note), a Skill input row (SR with its standard error; band at the point estimate and one s.e. lower), and a Market maker row (inventory aging, residual markouts by tier, RFQ hit ratio and cover gap, residual risk after hedges, fails; §3.3.3, §18.7, Appendix D). All eight original rows kept unchanged. Intro clause "equation number" became "equation or section number".
- New prose after the table (three paragraphs, about 440 words): the P&L and limits panels as books of record beside the sizing equations; the market-maker panel and Ines's napkin rule (Ch 18); SR as an input with a standard error (about $1/\sqrt{Y}$, §7.8; 3 years of a 0.7 Sharpe gives about 0.6, marked illustrative), the demo run at 0.7, and the empty band as the honest result (a lower SR raises the floor and lowers the ceiling, so the band can only narrow).
- Spec: "SR" in the desk-parameter list became "SR with its standard error"; added the invariant "lowering SR raises the floor and lowers the ceiling" and a sentence saying which rows the engine computes and which are read from the explain, limit sheet and quoting log.
- Numbers added: 0.7 (the item's own), about 0.6 (= 1/sqrt(3)), floor "several times" the ceiling. Verified by running the Appendix F Chapter 28 listings in the scratchpad with `sharpe` = 0.7: floor 8.05, ceiling 1.43, band empty, all existing assertions pass. (At the listing's current 2.0 the demo band is also empty: floor 2.82, ceiling 1.83.)
- No web fetches used.
- FOLLOW-UP, outside this file: `95_appF_code_companion.md` Listing 28.8 still has `DESK = {..., "sharpe": 2.0, ...}` and no s.e. key; set `"sharpe": 0.7` (and add a Sharpe s.e. key) so the code matches the chapter. §8B.9/§8B.8/§12C.9 point to §28.9 for a "model-health panel" and a "restructuring position" row; those are not part of C9 and were not added.

## D7: §28.8

- Softened the division of labour: "Analysts own $L$, $L_{\max}$, the document features (PRS, Chapter 13) and the covariates of $\lambda^{\mathbb{P}}$, which is how Theo's 13-week runway becomes an input to it (§5.1.5); PhDs own the estimator of $\lambda^{\mathbb{P}}$, $\sigma_{\text{DTS}}$ and the covariance". Rest of the sentence unchanged.
- Added one paragraph (about 190 words) in the Case Study, after the ROBO-contract sentence: the analyst-side corollary of the standard-error argument (hit-rate s.e. on $n$ calls is $\sqrt{p(1-p)/n}$, about 8 points on forty calls, a 56% record under one s.e. from a coin; both marked illustrative and computed from that formula); judged on calibration, $\rho$ to the price factors (28.24) and hit rate with its s.e.; log every view in the Edge Ledger. No new sources.

## Checks

`python3 tools/check_book.py --file book_src/28_ch28_pm_playbook.md`: OK. Last line of the chapter (`<!-- STATUS: COMPLETE -->`) preserved. No currency symbols added; math in Pandoc form.

<!-- STATUS: COMPLETE -->
