# Ch08 App Z fix log

## Note 1 (Z.08.1): §8.2 "two-factor derivation" claims H ≈ 0.03 at 500 bp and "slightly below zero" at 620 bp
- Recomputation (python3): ℓ = -0.56 × 0.022 / 0.00064 = -19.25. H(500 bp) = 1 - 19.25 × 0.05 = 0.0375 (0.04); with the rounded ℓ = -19 it is 0.05. Neither is 0.03. H(620 bp) = 1 - 19.25 × 0.062 = -0.1935 (-0.19), which is 231.7 × -0.1935 ≈ -45 contracts, i.e. a long future, not "slightly" below zero.
- Ruling: fixed (note right).
- Chapter edit (book_src/08_ch08_isolating_ido_and_empirical_duration.md, §8.2):
  - OLD: "so a B bond at 500 bp has $H \approx 0.03$, and Theo's bond at 620 bp comes out slightly below zero."
  - NEW: "so a B bond at 500 bp has $H \approx 0.04$ (from the unrounded $\ell = -19.25$), and Theo's bond at 620 bp comes out at $H \approx -0.19$, which is a long position in the future."
- App Z: the solution already quoted -0.19 and ℓ = -19.25, so no text change; the NOTE paragraph was deleted.

<!-- STATUS: COMPLETE -->
