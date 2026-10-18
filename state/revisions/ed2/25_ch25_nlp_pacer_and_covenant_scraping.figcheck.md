# Figure check: Chapter 25 (ed2 U4, checker pass)

Chapter: book_src/25_ch25_nlp_pacer_and_covenant_scraping.md. Script: tools/figures/ch25.py. All five PNGs were re-rendered after the fixes below, re-viewed, and are 114 to 138 KB (budget 500 KB). Embeds: all five use `![Figure 25.n: ...](assets/figures/ch25_*.png)`, files exist, numbered 25.1 to 25.5 in file order (lines 113, 227, 292, 326, 424), each directly after the paragraph that cites it.

## Figure 25.1, ch25_definition_graph.png: PASS (one polish)
- Correctness: I ran Listing 25.1's matcher (App. F) on its own synthetic Section 1.01 with the `means[,\s]` regex fix and compared its edge set to `DEFINITION_EDGES` in the script: identical. Script asserts both SCCs (Consolidated EBITDA / Run-Rate Cost Savings / Pro Forma Basis; Restricted / Unrestricted Subsidiary / Material IP), beta(Consolidated EBITDA) = 3 and beta(Excluded Taxes) = 0. Arrows run from the term to the terms it uses, as in the legend.
- Honesty: caption says Illustrative and names the Listing 25.1 matcher. Caveat: the printed listing still has `means\s+` (cleanup_queue, U1), so until that regex is fixed the listing as printed does not return the Pro Forma Basis edges the figure shows. Figure and prose ("two loops") agree; the listing is the part to fix.
- Legibility: no collisions. Fix: node text raised from 7.2 to 7.8 pt (boxes still fit).

## Figure 25.2, ch25_addback_capacity.png: PASS after fixes
- Correctness: left, before = c, after = c/(1-c), 25% -> 33.3%, gap c^2/(1-c), shaded. Right, K(E) = max(0, 4.5E - 900) + max(75, 0.35E): flat 75 to E = 200, kink at 200, slope 4.5 to 214.3 then 4.85; points (200, 75) and (266.7, 393.3) asserted in the script and match the chapter table.
- Honesty fix: caption said "those extra dollars of EBITDA lift capacity from $75mm to $393.3mm", which attributes to the "after" reading what the whole $66.7mm of add-backs does (the "before" reading would give E = 250, K = 312.5). Caption now says "the resulting $66.7mm of add-backs lift ...". Also removed "E0" from the caption (the figure now uses the chapter's calligraphic notation).
- Style fixes: left-panel labels and y-axis used plain "E0" while the right panel and the chapter use calligraphic E (E_t is equity value); now script-wide ℰ₀. Right panel: curve ran off the top at E = 281; xlim 160-290 and ylim 0-600 so the curve ends inside the frame and the note no longer sits on a gridline.

## Figure 25.3, ch25_jcrew_mincut.png: PASS after fixes
- Correctness: the Edmonds-Karp routine in the script (as in Listing 25.3) asserts Phi = 0 with cut {trapdoor} and Phi = 250 with cut {150, 100 baskets}; the drawn cut lines cross exactly those arcs. Fix: in the bottom panel the trapdoor stroke (4.4) was thinner than the two baskets together (5.4); now 5.4 so thickness conserves flow.
- Honesty fix: caption said both numbers were "disclosed in J.Crew's filings". Per §25.4.2 the $150mm/$100mm baskets come from King & Spalding and the $250mm value from Torys (May 2019). Caption now attributes each to its source and points to §25.4.2.
- Legibility: no collisions, no clipping.

## Figure 25.4, ch25_token_vs_capacity.png: PASS after fixes
- Correctness: 1 - cos = k^2/||x||^2 verified by hand (x_i = k swapped to an unused token: x.x' = ||x||^2 - k^2, ||x'||^2 = ||x||^2); ||x||^2 = d(lambda^2 + lambda) = 2.4e6 gives 4.2e-7 at k = 1 and k = 155 at 1%. Right: max(0, m*266.667 - 900) gives $300mm at 4.50x, $500mm at 5.25x, +$200mm (asserted). Caption numbers match the chapter (4 x 10^-7, 155, $200mm).
- Legibility fixes: the "155 occurrences all amended" label was crossed by the orange line (moved above-left of the point; "1% move in cosine" moved under its dashed line); "4.50x: $300mm" touched the 5.25x dashed vertical (both point labels now two lines); the note on the right panel sat on the 700 gridline (ylim 770).

## Figure 25.5, ch25_docket_state_machine.png: PASS after fixes
- Correctness/honesty: dates and titles match the Docket Diary and the advisor brief (state/advisor_briefs/25_..., docket id 73709078): Docs. 154 (2026-08-10), 320 (2026-09-10), 369 (2026-09-20); 31 and 10 days check (August has 31 days). Caption cites the case number and the three documents.
- Fixes: legend said "Gray: states it had not reached", but Quiet precedes the first entry and is not shown; now "Gray: states before or after it". The estimator note used a Greek beta as a subscript stand-in for b (q-hat sub a-beta); it now uses mathtext, q-hat_ab = N_ab / T_a, as in the chapter. Text raised to 7.4-7.6 pt (card text was 6.9 pt) and the two muted notes now use INK_2; Doc. 320 card text rewrapped to fit.

## Edits made
- tools/figures/ch25.py (styles, labels, limits, widths as above); all five PNGs re-rendered.
- book_src/25_ch25_...md: two caption edits (Figure 25.2, Figure 25.3). Nothing else touched.

## Left for others
- Listing 25.1 regex in Appendix F (`means\s+` should be `means[,\s]`), already in state/cleanup_queue.md.
<!-- STATUS: COMPLETE -->
