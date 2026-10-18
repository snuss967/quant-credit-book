# App Z note fixes, Edition 2: Chapter 9

Numbers-editor pass on `state/appZ/09_ch09_factor_investing_in_credit.md` against `book_src/09_ch09_factor_investing_in_credit.md`, run 2026-10-18. One NOTE (for the editor) found, one handled.

## Z.09.5 (Exercise 5, "Extend the lab")

- **Note:** the exercise asks which signal the Blume-Stambaugh mechanism "inflates" more; on the chapter's own iid-error noise model, noise moves bond momentum down (-46bp a month, -5.4% a year against +0.05% clean) and ESI by +0.7bp a month, so "inflate" presupposes the wrong sign for the bond-price signal.
- **Recomputation (own run, `python3 -I`, scratchpad `ext.py`):** rebuilt Listings 9.1-9.7 verbatim from Appendix F (all hard checks pass; Blume-Stambaugh bias 0.985bp vs 1.000bp; lag-one reversal t = 26.8, skip-month t = 0.8). Extended with a planted ESI link (+0.01 w to the issuer log-spread residual, ESI observed at the start of the month, z-scored within rating, short high ESI) and six-month trailing-sum bond momentum computed from the same price series it is graded on, using lab noise of 0.4% IG and 1.2% HY, DTS-neutral deciles through the Listing 9.2 engine. Bond momentum: clean -0.07%/yr (t = -0.3), noisy -5.41%/yr (t = -16.0), a gap of about -45bp a month; skipping a month on noisy prices: -0.34%/yr (t = -1.3), so the damage is the shared price. ESI: clean 4.48%/yr (t = 11.3), noisy 4.54%/yr (t = 11.3), a gap of about +0.5bp a month. Analytic check agrees: with $\tilde r_{t+1} \approx r_{t+1} + u_{t+1} - u_t$ and a six-month sum carrying $+u_t$, the covariance of a buy-winners sort is $-\sigma_u^2$ (§9.9, Mechanism 2), the mirror image of the reversal sort. My numbers differ from the solution's only in the planted-link draw; the signs and sizes (about -46bp against under 1bp) match. Chapter text elsewhere is consistent: §9.9 Mechanism 1 (level bias $+\sigma_u^2$, size premium at §9.6.2) and Mechanism 2 are correctly stated; only the exercise stem presupposes an upward move.
- **Ruling:** fixed (note right). The exercise's wording, not any number, was misleading.
- **Edit, `book_src/09_ch09_factor_investing_in_credit.md`, Exercise 5:**
  - old: "Which one does the Blume–Stambaugh mechanism inflate more, and why does your answer depend on"
  - new: "Which one does the Blume–Stambaugh mechanism distort more, and why does your answer depend on"
- **Solution:** its Answer, How and Trap already carry the downward sign and the quoted trap "Bond momentum is inflated..." is still a trap, so no solution text changed; the NOTE paragraph was deleted from `state/appZ/09_ch09_factor_investing_in_credit.md`.

## Summary

1 note handled: 1 fixed, 0 ruled wrong, 0 softened. No figure script or listing output affected.

<!-- STATUS: COMPLETE -->
