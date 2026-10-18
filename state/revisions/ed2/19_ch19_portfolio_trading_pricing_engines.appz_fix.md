# Ch 19 App Z editor-note fixes (numbers editor)

Three NOTE (for the editor) paragraphs found in state/appZ/19_ch19_portfolio_trading_pricing_engines.md. All three deleted from the solutions file after ruling. All numbers recomputed by running Appendix F Listings 19.1-19.8 cumulatively in one interpreter (copy under /tmp/ed19, not in the repo).

## 1. Z.19.2: "exhausts its alpha budget" at s=2 (and the 2022 annotation)
- Note: with Listing 19.5's defaults it is k_max that binds, not alpha.
- Recomputation: gross MV 204.294mm. price_pt at s=2 (etf_disc_z=-10, bidask_pct=1): 10 evictions, 14.36% of MV, 315.7bp, hit_target False; with k_max=50: 11 evictions, 15.00% of MV, 312.9bp. s=1: 10 evictions, 14.36%, 148.3bp (already the chapter's "ten evictions leaving 148bp"); k_max=50: 11 lines, 15.0%, 147.2bp. Exercise-2 regime (z=-4, 97th pct, s=1.85): 10 evictions, 14.36%, 286.9bp; k_max=50: 11 lines, 15.0%, 284.4bp. Matches the note.
- Ruling: note right (fixed). Same wrong mechanism restated in two more places in the chapter (the 2022 annotation and the Grading paragraph), fixed alongside; the annotation and the grading are generic claims about HY baskets, so they now name either limit.
- Chapter (§19.7.2, Two Tapes, tape one): "the eviction loop exhausts its $\alpha$ budget, 15% of the market value handed back, long before" -> "the eviction loop stops at its $k_{\max}$ cap of ten lines, 14% of the market value handed back, long before".
- Chapter (§19.6.2, Annotation): "would have seen its eviction loop hit the $\alpha$ budget before reaching $\kappa^\star$ on HY baskets" -> "would have seen its eviction loop hit its $\alpha$ budget or its $k_{\max}$ cap before reaching $\kappa^\star$ on HY baskets".
- Chapter (§19.7.2, The grading): "its eviction loop exhaust the $\alpha$ budget on every high-yield basket" -> "its eviction loop run into its $\alpha$ budget or its $k_{\max}$ cap on every high-yield basket".
- Solution (Z.19.2): already said k_max=10, 14.4% and "lift k_max and the alpha budget binds at 11 lines and 284bp"; no text edit, NOTE deleted.

## 2. Z.19.4 / Exercise 4: variance version "distorts h*" / "over-hedges it"
- Note: in Listing 19.3's factor model h* = Sff^-1 Sfx x does not depend on sig_idio, so the hedge is unchanged; an over-hedge appears only if the bump also scales L117's loadings.
- Recomputation: min_var_hedge on the full basket with L117 sig_idio x1, 3, 5, 9, 10 = \$79.798mm ETF / \$157.102mm CDX every time (total \$236.9mm). Scaling L117's row of Sxf (its loadings) by 10: \$108.989mm ETF / \$214.572mm CDX (total \$323.6mm, +\$86.7mm). Kaz version through the eviction loop (AS zero, sig x m): m<=9 evicts only L042, hedge on survivors \$71.16mm/\$140.10mm, i.e. L117 kept and hedged (+\$9.6mm of index hedge vs \$67.92mm/\$133.71mm); m>=10 evicts L117 then L042 and the hedge equals the AS version's. Kaz's L117 ratio is 330bp against L042's 305-307bp, so only just. Matches the note.
- Ruling: note right (fixed). Hedge changes only through eviction, or through the loadings if the whole return series is scaled.
- Chapter (§19.5, Ways This Blows Up (3)): "and over-hedges it (the hedge solve now thinks line 117 is noisy, not toxic)" -> "and mis-ranks it for eviction (the loop now thinks line 117 is noisy, not toxic)".
- Chapter (Exercises, item 4): "why the variance version both under-charges the jump and distorts $\mathbf{h}^\star$." -> "why the variance version both under-charges the jump and distorts the eviction ranking and, if applied to the whole return series, $\mathbf{h}^\star$."
- Solution (Z.19.4): already said the hedges are identical and listed the two ways they move; no text edit, NOTE deleted.

## 3. Z.19.5 / Exercise 5: "a 150-line IG program" with Sigma from 19.5, no retry cost
- Note: 19.5 builds Sigma only for the HY cold-open basket; the exercise gives no c^retry; the solution used b0 at T=1.
- Recomputation (b0, T=1, Sxx with staleness, gamma_B=5e-7): diagonal part \$72.62k, pair part \$89.57k. phi=0.9: 0.1*72.62+0.01*89.57 = \$8.16k = 0.40bp of \$204.3mm; phi=0.6: 0.4*72.62+0.16*89.57 = \$43.38k = 2.12bp. Monte Carlo (20,000 draws) \$8.21k and \$43.66k. L042 is 96% of the diagonal. Retry at 5bp per dollar adds 0.1*5bp = 0.5bp and 0.4*5bp = 2.0bp (\$10.2k, \$40.9k). Sres at T=1 gives \$7.2k and \$30.1k. All as in the solution. No IG basket exists anywhere in the chapter or listings, so the IG wording could not be reproduced.
- Ruling: note right (fixed).
- Chapter (Exercises, item 5): "For a 150-line IG program with RFQ fill probabilities $\phi_i=0.9$, $\gamma_B=5\times10^{-7}$ per dollar, and $\Sigma$ from §19.5 over a one-day re-trade horizon, compute the maximum" -> "Take the cold-open basket `b0` as the program, with RFQ fill probabilities $\phi_i=0.9$, $\gamma_B=5\times10^{-7}$ per dollar, a retry cost of 5bp per dollar and $\Sigma$ from §19.5 over a one-day re-trade horizon, and compute the maximum".
- Solution (Z.19.5, Answer): "Take the chapter's 150-line program, with" -> "Take the cold-open basket `b0` as the program, with"; "at an assumed 5bp of extra cost per retried dollar" -> "at the exercise's 5bp of extra cost per retried dollar". NOTE deleted. Numbers unchanged.

<!-- STATUS: COMPLETE -->
