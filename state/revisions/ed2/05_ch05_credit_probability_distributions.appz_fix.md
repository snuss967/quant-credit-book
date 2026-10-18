# App Z Fix Log (Edition 2): Chapter 5, `book_src/05_ch05_credit_probability_distributions.md`

Notes source: `state/appZ/05_ch05_credit_probability_distributions.md` (one NOTE for the editor, Z.05.2).

## Note 1 · Exercise 2 (The convexity tax): "right-skewed survival leg" holds only under §5.9.1's Gaussian Δs

- **Note:** The exercise says to show a non-call bond's survival leg is right-skewed, but that sign comes from the Gaussian Δs of §5.9.1; §5.2.4 says lognormal spreads give a survival-world skew of about -1.1, which positive convexity offsets only "a little."
- **Recomputation** (`/tmp/ed2/ch05_skew.py`, exact lognormal raw moments $E[L^n]=e^{n(n-1)\kappa^2/2}$ plus a 4,000,000-draw simulation; $s=0.055$, $\kappa=0.35$, $D^{\text{spr}}=3.5$): Gaussian Δs gives skew $-0.1319$ / $0$ / $+0.1319$ at $C^{\text{spr}} = -8 / 0 / +8$, $\sigma_X = 6.74\%$, tax $14.8$ bp (the exercise's check values stand). Lognormal Δs $= s(e^{-\kappa^2/2+\kappa Z}-1)$ gives exact skew $-1.3435$ / $-1.1300$ / $-0.9254$ (simulation $-1.346$ / $-1.132$ / $-0.926$), so the leg stays left-skewed; the spread's own skew is $+1.1300$, matching §5.2.3. Zero-skew convexity under lognormal is about $+54$. Mixture check (q=4%, Beta 40/27.5, P0=0.92, x0=7%): skew $-4.16$ / $-4.14$ (Gaussian, C = -8 / +8) and $-4.12$ / $-4.22$ (lognormal), so "mixture still left-skewed, about $-4.1$" holds either way.
- **Ruling: fixed** (note right). §5.2.4 and the exercise disagreed; §5.2.4 is correct, and the exercise is correct only under §5.9.1's Gaussian assumption. §5.2.4 and §5.9.1 left unchanged.
- **Chapter edit** (Exercises, item 2):
  - old: `Then flip the sign of $C^{\text{spr}}$, show that the survival leg of a non-call bond is right-skewed, and explain why the mixture is still left-skewed overall.`
  - new: `Then flip the sign of $C^{\text{spr}}$, show that under §5.9.1's Gaussian spread change the survival leg of a non-call bond is right-skewed, and explain why the mixture is still left-skewed overall. (With §5.2.3's lognormal spreads the leg itself stays left-skewed.)`
- **Solution edits** (`state/appZ/05_ch05_...md`, Z.05.2):
  - Answer: `the volatility does not change. The skew becomes $+0.13$` → `under §5.9.1's Gaussian spread change, the volatility does not change. The skew becomes $+0.13$`; added `With §5.2.3's lognormal spreads instead, the same leg stays left-skewed, at $-0.93$.`
  - How: after `so the skew becomes $+0.132$.` added the lognormal paragraph (skew $-1.13$ from the first-order term, $-0.93$ at $+8$, $-1.35$ at $-8$, convexity of about $+54$ to cancel).
  - Trap: added `The positive sign comes from the Gaussian $\Delta s$; with lognormal spreads the leg stays left-skewed. Either way ...` and `under the Gaussian` before "its skew is two orders of magnitude too small".
  - Read-list: added `For the lognormal case, read the first paragraph of §5.2.4.`
  - NOTE paragraph deleted.
- **Not touched:** `state/appZ/_editor_notes.md` (consolidated copy of this note) and the assembled `book_src/99_appZ_solutions_hints_and_self_assessment.md` (no NOTE in it, but its Z.05.2 text predates these edits; reassemble App Z to pick them up).

## Summary

1 note handled: 1 fixed, 0 ruled wrong, 0 softened.

<!-- STATUS: COMPLETE -->
