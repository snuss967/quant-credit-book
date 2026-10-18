# Ch15 App Z editor-note fixes (numbers editor)

Three NOTE (for the editor) paragraphs found in state/appZ/15_ch15_event_driven_mna_and_coc.md; all three handled in order and deleted from the solutions file.

## Note 1 (Z.15.1): "eighteen to nineteen points at signing" after Listing 15.1
- Note: the sentence after the Listing 15.1 description says the 1.85% bond's put is eighteen to nineteen points at signing; the listing prints 15.55 and check (1) gives 17.82.
- Recomputation (exec of Listing 15.1 from Appendix F): check-(3) LBO value 15.554 +/- 0.016, M = 1.0523, independent 14.781, with defeasance 0.00; check-(1) constant-350bp inputs (0.85, 0.9, 350bp) give 17.8185. Neither is 18 to 19.
- Ruling: fixed (note right).
- Old -> new (book_src/15_ch15_event_driven_mna_and_coc.md, sec 15.2, after Listing 15.1 pointer):
  "comes out at eighteen to nineteen points at signing, most of the gap"
  -> "comes out at about fifteen and a half points at signing (about eighteen at a constant 350bp), most of the gap"
- Solution: Z.15.1 already quotes 17.8 / 41.3 (constant 350bp) and 15.6 / 35.4 (check 3; recomputed 15.554 and 35.363), so no text change; NOTE deleted.

## Note 2 (Z.15.1): mean-preserving lognormal example "with sigma = 0.5"
- Note: the four-checks paragraph gives sigma = 0.5, median e^-0.125 = 88% of the mean, but check (3) uses sigma = 0.35.
- Recomputation: listing uses 0.035*exp(0.35 Z - 0.5*0.35^2); median/mean = e^-0.06125 = 0.9406; simulated median 329.2bp vs mean 350.07bp (seed 7, 200k draws). The 0.5 / 88% figures (e^-0.125 = 0.8825) belong to no check in the listing (sigma 0.5 would give a put of 14.33, M 1.10).
- Ruling: fixed (note right); changed the example to the listing's sigma rather than adding a clause.
- Old -> new (same paragraph, "The four checks do real work"):
  "so that with $\sigma = 0.5$ the median draw is $e^{-0.125} \approx 88\%$ of a 350bp mean;"
  -> "so that with $\sigma = 0.35$ the median draw is $e^{-0.061} \approx 94\%$ of a 350bp mean;"
- Solution: no text quoted sigma = 0.5; NOTE deleted.

## Note 3 (Z.15.2): "If rates have fallen, P_close > G_f" in "The sign flips with rates", sec 15.4.2
- Note: for the section's three-year 4.60% tranche issued at par, P_close (100.00) < G_f (100.99) until a rally of about 38bp, so "if rates have fallen" is true only for a large enough fall; the ruler box already says "far enough".
- Recomputation: 4.60% bond-equivalent = 4.548% continuous; par price 100.000; G_f = 102.15*exp(-0.04548*0.25) = 100.995 (100.982 at y_f = 4.60% continuous). Parallel shift of both legs: crossover at -38.3bp (BE yield 4.209%, both legs 101.09). A 10/20/30bp rally leaves P_close - G_f at -0.74/-0.48/-0.22; 40bp gives +0.05. (If only the close leg rallies and the fail leg stays put, the crossover is about 35bp; the solution's 38bp is the parallel move.) Ruler at issue is -0.995 (P_close below G_f).
- Ruling: fixed (note right). Used 38bp (matches the solution's computed figure) instead of the note's rounder 40bp.
- Old -> new (sec 15.4.2, "The sign flips with rates"):
  "If rates have fallen, $P^{\text{close}} > G_f$ and the holder is short a digital:"
  -> "If rates have fallen far enough (a parallel rally of about 38bp on a three-year tranche issued at par), $P^{\text{close}} > G_f$ and the holder is short a digital:"
- Solution: Z.15.2 already says about 38bp; NOTE deleted. No figure script prints any of these numbers (tools/figures/ch15.py Figure 15.3 uses the 100.98 worked example only), so no figure rerun.

<!-- STATUS: COMPLETE -->
