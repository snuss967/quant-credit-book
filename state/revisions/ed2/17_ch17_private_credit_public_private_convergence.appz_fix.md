# Ch17 App Z fix log

## Note 1: Z.17.5 "Takeout season", "overstates most / by more in the tight regime"
- Note: Exercise 5 ("overstates ... by more in the tight regime") and §17.4.2 ("overstates most in exactly the stressed regime") hold only in proportional terms for block 3; in dollars the overstatement falls from the loose to the tight regime.
- Recomputation (Listing 17.3 block 3 re-run in python3, seed 2023, 400 loans, ds=1): competing supply / naive supply / gap / gap as % of competing: zeta=-1: 8090.7 / 8196.1 / \$105.4mm / 1.30%; zeta=0: 3756.6 / 3825.3 / \$68.7mm / 1.83%; zeta=+1: 1705.1 / 1748.8 / \$43.8mm / 2.57%; zeta=+2: 764.4 / 792.0 / \$27.6mm / 3.61%. The fractional overstatement rises with the regime (it is g(kappa_B dt)/g(K dt) per loan), but the dollar gap shrinks because tight-regime supply is about a fifth of loose-regime supply.
- Ruling: fixed (note right). The §17.4.2 general inequality is correct; only the comparative "most / more" was ambiguous between fraction and dollars.
- Edits:
  - book_src/17_ch17_private_credit_public_private_convergence.md, §17.4.2: "and it overstates most in exactly the stressed regime where" -> "and by a larger fraction in exactly the stressed regime where"
  - book_src/17_ch17_private_credit_public_private_convergence.md, Exercise 5: "overstates the competing-risks one by more in the tight regime" -> "overstates the competing-risks one by a larger fraction in the tight regime"
  - state/appZ/17_ch17_private_credit_public_private_convergence.md, Z.17.5 trap: "\"By more\" only makes sense as a fraction of supply." -> "The claim is about the fraction of supply, not the dollar gap." (answer text already quoted the right percentages and the shrinking dollar gap; unchanged)
  - NOTE paragraph deleted from the Z.17.5 solution.
- No figure script or Appendix F listing text affected (tools/figures/ch17.py has no overstatement number; Listing 17.3 code and checks unchanged).
- Not touched (outside this chapter's scope): the assembled copies book_src/99_appZ_solutions_hints_and_self_assessment.md (Z.17.5 trap sentence, old wording) and state/appZ/_editor_notes.md (aggregated copy of the NOTE) will need to pick up the change on the next App Z assembly.

<!-- STATUS: COMPLETE -->
