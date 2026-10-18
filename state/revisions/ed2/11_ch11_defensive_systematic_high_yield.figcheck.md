# Figure check: Chapter 11 (ed2)

Checked against tools/figures/style.py (house style), tools/figures/ch11.py (script), the five embedded ch11_*.png files (each viewed with Read, before and after fixes), and the chapter text around each embed. The script was re-run after the fixes; all of its built-in assertions passed (issuer DD 2.44 and PD 4.6%; 15 Oct 2026 closes 323/197/326/1,278bp; the six quoted month-end ratios).

## Figure 11.1, ch11_mixture_skew.png (section 11.1.1). Verdict: PASS, no change

- Correctness: mixture mean 1.36% and std. dev. 11.5% recomputed by hand from Var = (1-p)v + p(1-p)(m+L)^2 (jump share 88%); density peak 9.7% equals 0.97 x pdf(0) x 100; default spike height 3 in a 1-point bin equals 3%. Right panel: skew -(1-2p)/sqrt(p(1-p)) gives -6.9, -4.1, -1.5 at 2%, 5%, 20%, increasing monotonically to 0 at p = 50% (the right tail behavior the theory demands).
- Honesty: caption says "Illustrative", states all inputs (N(3.3%, 4.0%), p = 3%, L = 60%) and sources the 3.3% carry to the 326bp single-B OAS (FRED BAMLH0A2HYB, 15 Oct 2026, which matches the chapter's break-even table).
- Legibility and style: no collisions or clipping; one y-axis per panel; two colors in role order (blue survive, orange jump); text in ink; no in-image title; log x-axis labelled.
- Embedding: syntax and file OK, number 11.1 first, sits after the skew paragraph it illustrates, pointer sentence present.

## Figure 11.2, ch11_capture_plane.png (section 11.2.1). Verdict: PASS after a minor style fix

- Correctness: re-derived alpha and beta from U = beta + alpha/ubar, D = beta + alpha/dbar with ubar = +1.6%, dbar = -2.0% (factor 112.5): average manager alpha 28.6bp, beta 0.908; top quartile alpha 74.7bp, beta 0.951, matching the chapter table. Axes are D (x) and U (y); the diagonal is the pure beta tilt (U = D = beta); blue region U > D is alpha, gray region U < D is "gives up more upside than it saves", which is the right reading; arrows run from the same-beta alpha-zero point to the observed point; benchmark at (100, 100).
- Honesty: caption cites BlackRock (2025) p.3 (eVestment, 2005-2025, net of fees, all as in the chapter text) and labels the regime means illustrative.
- Legibility and style: no collisions; single color group (blue) plus ink; direct labels throughout; vertical grid is deliberately on for a two-axis plane.
- Fix made: three annotation texts were 8.2 pt; set to the house 8.5 pt (script, then re-run and re-viewed; no new collisions).
- Embedding: OK, 11.2, after the decomposition table and its pointer sentence.

## Figure 11.3, ch11_dd_pd_map.png (section 11.3.2). Verdict: PASS after a labelling fix

- Correctness: N(-4) = 3.17e-5 (0.003%); placeholder map exp(-0.718 - 0.9718 DD) gives 1.00% at DD = 4, ratio 316, "about 300x"; both curves decrease monotonically; the 35% cap is visible as a flat segment to DD ~ 0.34; the curves cross near DD ~ 0.7, where the Gaussian then runs above the capped map, as the formulas require. The sponsor-levered issuer is re-solved with the listing's nested Brent search (V ~ 4,016, sigma_V ~ 27.5%) and asserted at DD 2.44, empirical 4.6%, Gaussian 0.74%, matching the chapter's prose. Log y-axis from 0.001% to 100%.
- Honesty: the DD > 4 shaded zone is tied in-image and in the caption to Bohn-Stein p.138 ("the majority of publicly traded firms have DDs greater than 4", quoted in the chapter). The curve itself is a placeholder; the caption says "Illustrative: the placeholder map".
- Fix made: the in-image label read "Empirical map (Listing 11.2)", which could be taken as real calibrated data by a reader who skips the caption. It now reads "Placeholder empirical map (Listing 11.2)". Re-run, re-viewed, fits inside the axes.
- Legibility and style: no collisions or clipping; leader lines are used for the two annotations; one y-axis; direct labels on both curves.
- Embedding: OK, 11.3, after the Bohn-Stein extraction box and its short pointer paragraph.

## Figure 11.4, ch11_exclusion_pays.png (section 11.5.2). Verdict: PASS, no change

- Correctness: loss avoided (pi_X - pi_K)L with pi_X = h pi/q and pi_K = (1-h) pi/(1-q): 6.41% at q = 20%, 2.78% at q = 40%; active return q[(pi_X - pi_K)L - (s_X - s_K)] = +44bp and -9bp, matching chapter section 11.5.2 and the caption; curve is monotone decreasing in q. The top-left of the curve leaves the axes at 10% (q ~ 13%), which is intended.
- Honesty: caption says "Illustrative", names the 3% default rate, L = 0.6, and the two excess-spread inputs, and states that the curve holds the hit rate at 77% for every q.
- Legibility and style: one y-axis (percent per year); legend plus direct annotations; at q = 40% the circle and diamond nearly touch, but both are readable and the annotation arrow resolves them.
- Embedding: OK, 11.4, directly after the "Same hit rate, opposite sign" paragraph.

## Figure 11.5, ch11_tier_oas.png (section 11.6.2). Verdict: PASS after label and caption fixes

- Correctness and data: re-read the cached FRED CSVs (794 rows each, 8 blank holiday rows dropped, 17 Oct 2023 to 15 Oct 2026). 15 Oct closes are 323/197/326/1,278bp; the 14 Oct CCC close of 1,282bp is the three-year high the chapter cites; month-end ratios 2.61 (Jan 2025), 2.54 (Apr 2025), 3.15 (Dec 2025), 3.53 (Jun 2026), 3.96 (Aug 2026 and Oct 2026) all reproduce. The index OAS peaked on 7 Apr 2025 at 461bp, so the dashed event line is on the correct date, but it marks the spread peak of the tariff shock, not the 2 Apr announcement.
- Honesty: caption cites all four FRED series and the three-year window, and says the ratio is "our computation". Licensing caveat (ICE) is in the figures log; raw CSVs are not stored in the repo.
- Fixes made: (1) the B and index share a label whose aqua dot sat next to the text "index 323bp", so it was ambiguous which line was which. Now "B 326bp" (aqua dot) and "Index 323bp" (gray dot, a larger gray ring under the aqua dot, matching the thick gray index line) are separate labels. (2) The event label read "Tariff shock 7 Apr 2025"; now "Tariff-shock peak 7 Apr 2025". (3) The October 2026 point on the ratio panel is the 15 October close, not a month-end; the caption now says so.
- Legibility and style: two panels, never twinx; aqua (slot 3) is direct-labelled; colors BB blue, B aqua, CCC orange, index neutral; text in ink; no collisions after the fix.
- Embedding: OK, 11.5, after the paragraph giving the 15 Oct closes and the ratios.

## Cross-figure checks

- Numbering 11.1 to 11.5 in order of appearance; all five PNGs exist in assets/figures/, 91-117 KB each (limit 500 KB), 150 dpi, white background.
- Embed syntax `![Figure 11.k: ...](assets/figures/ch11_*.png)` matches the repo convention (build_book.sh rewrites the path for the output directory).
- Color roles (blue = the trusted object, orange = the adverse side or comparison) are consistent across the chapter and documented in the script docstring.

## Fixes made, in one list

1. tools/figures/ch11.py: Figure 11.2 text 8.2 pt to 8.5 pt.
2. tools/figures/ch11.py: Figure 11.3 map label says "Placeholder".
3. tools/figures/ch11.py: Figure 11.5 B and index labels split, with a gray ring for the index; event label "Tariff-shock peak".
4. book_src/11_ch11_defensive_systematic_high_yield.md: Figure 11.5 caption notes that October 2026 is the 15 October close.
5. All five PNGs regenerated and the changed three re-viewed.

## Notes for the author (no change made)

- The sentence before Figure 11.1 says "Read that table twice", but the skew values are given in a sentence, not a table.
- ICE licensing flag from the figures log stands: if the publisher wants no ICE-derived chart, drop Figure 11.5 and its pointer sentence.

<!-- STATUS: COMPLETE -->
