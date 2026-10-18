# Ch14 App Z editor-note fixes (numbers editor)

Three NOTE (for the editor) paragraphs in state/appZ/14_ch14_default_and_recovery_cycle_lmt_era.md, handled in order. All three deleted from the solutions file.

## Note 1 (Z.14.2): Mitel's 29 months "inside the high-hazard window" vs Serta's 31 months "a late failure"

- Note: on the pooled clock Mitel (29 months) is no more inside the hump than Serta (31 months), which §14.8.1 calls late.
- Recomputed (python3, p = 0.25, k = 1.2, eta = 1.7134 from F(2)/p = 0.70): share of eventual defaulters already failed by 29 months = 77.9%; population hazard at 29 months = 0.0514 a year, against a peak of 0.1149 at 0.47 years (less than half). Serta at 31 months: 80.5% and 0.0463. Same clock, so the two labels contradict. With a name-specific eta_i = 3.28, 29 months is the median susceptible failure time (the runway story of §14.3.2), so Mitel fits only on its own clock.
- Ruling: note right. FIXED (chapter).
- Chapter §14.8.2, last sentence of the Mitel replay:
  - old: "failing inside the high-hazard window that the $k > 1$ calibration predicts, and the desk's model now keeps legality and survival in different columns on purpose."
  - new: "failing inside the window its own runway set, though late on the pooled clock, and the desk's model now keeps legality and survival in different columns on purpose."
- Solution: no quoted old value; NOTE deleted.

## Note 2 (Z.14.3 / Exercise 3): who is inside when the co-op breaks

- Note: the exercise's 36-point answer assumes members inside, outsiders primed, but the §14.5.1 arithmetic (d* = 3 defectors = 21% of the class) needs 29.1 of the outsiders' 30 points, so outsiders are mostly inside the deal.
- Recomputed: P(Bin(10, phi) >= 3) = 0.0702 at phi = 0.10 and 0.7384 at phi = 0.35. With D defectors at 7 points each the sponsor needs (50.1 - 7D)/30 of the outsiders (97% at D = 3, 74% at D = 4, 50% at D = 5, 0 from D = 8). Averaged over D >= 3 with binomial weights, an outsider is inside with q = 0.9215 at phi = 0.10 and q = 0.6994 at phi = 0.35 (the note's 0.92 and 0.70). Seat ceiling = Pi x (1 - q) x 0.49 = 0.0027 (0.3 points) at phi = 0.10 and 0.1088 (about 11 points, \$1.1mm on \$10mm) at phi = 0.35.
- Ruling: note right on the defect; its suggested fix is not. FIXED (chapter), with a different sentence. The note's "a deal, if done, is done with co-op members and primes everyone outside the co-op" contradicts d* = 3: if outsiders are primed they are not among the 50.1%, and the deal would need 8 of 10 members, not 3. So the exercise instead states how the sponsor fills the majority, which is consistent with the §14.5.1 threshold.
- Chapter Exercises, item 3, end of question:
  - old: "...what is the most you would pay to join the co-op, in points? *Where this came up:*"
  - new: "...what is the most you would pay to join the co-op, in points? Assume the sponsor takes every defector and fills the rest of its 50.1% from holders outside the co-op at random, and that a member can always defect. *Where this came up:*"
- Solution Z.14.3 edited to agree:
  - Answer: "Read the co-op as the room: if a deal is done, members are inside at 74 and holders outside it are primed to 25. Then joining is worth at most Pi x (mu_in - mu_out) = 0.738 x 49 ~ 36 points, about \$3.6mm on your \$10mm. Before the sponsor started paying (phi = 0.10), the same seat was worth 3.4 points (\$0.34mm)." -> the outsiders-are-the-votes argument, q = 0.92 / 0.70, "at most Pi x (1 - q) x (mu_in - mu_out) = 0.738 x 0.30 x 49 ~ 11 points, about \$1.1mm", and "0.070 x 0.08 x 49 ~ 0.3 points (\$0.03mm)" at phi = 0.10; ceilings hold only for a member that sells its vote.
  - How: seat formula "0.738 x (1 - 0) x 0.49 = 0.362 of par" -> "0.738 x (1 - 0.70) x 0.49 = 0.109 of par", with the D-by-D outsider requirement and pi_outsider = q, pi_member = 1.
  - Trap: "Paying the full 49 points ... 3.4 points" -> leads with the 36-point slip (co-op as the room) and the 29.1-of-30 reason, keeps the 49-point and phi = 0.10 slips (now 0.3 points).

## Note 3 (Z.14.6 / Exercise 6): "on about 45 annual points the switch date is uncertain by years"

- Note: in the exercise's own setup the date is sharp at 90 defaults a year; years appear only at private-credit size, with overdispersed counts, or a drifting share.
- Recomputed with Listing 14.4 (fit_ms2, filtered P(LME) > 0.9, switch in year 30, shares 0.30 -> 0.63):
  - 90 defaults, clean binomial, 200 histories: first crossing year 30 in 199, year 31 in 1; none before the switch. Confirms the note.
  - 12 defaults, 200 histories: first crossing at/after the switch in year 30 (16%), 31 (43.5%), 32 (21.5%), 33 (13.5%), 34-37 (5.5%); median lag 1 year, mean 1.5, 90th percentile 3; 11 of 200 crossed 0.9 before year 30. Confirms median lag one, 90th percentile three.
  - 90 defaults, share overdispersed (beta-binomial, sd 0.07 around each regime mean), 40 histories: 11 of 40 passed 0.9 before the switch (the note reports 19 of 40 on its draws; same direction, different RNG).
  - 90 defaults, share drifting linearly 0.30 -> 0.63 over years 25-35, 40 histories: first crossing years 28-33 (10th to 90th percentile about 29 to 32). Confirms the note.
- Ruling: note right. FIXED (chapter). The clause "uncertain by years" held only at small counts, extra-binomial noise or a drifting share.
- Chapter §14.7.2, Ines's filter paragraph:
  - old: "and on about 45 annual points the switch date is uncertain by years, worse when each year holds fewer defaults (Exercise 6 shrinks the counts to private-credit size)."
  - new: "and on about 45 annual points the switch date is sharp only if the counts are clean binomial draws around a share that jumps; with private-credit-sized counts (Exercise 6 shrinks them to that size), extra-binomial noise or a share that drifts, it is uncertain by years."
- Solution Z.14.6 already reports 199 of 200 and the private-credit lag; no change beyond deleting the NOTE.

Summary: 3 notes handled, 3 fixed (chapter edits: §14.8.2 Mitel clause, Exercise 3 assumption sentence, §14.7.2 switch-date clause), 0 ruled wrong, 0 softened. Throwaway scripts in /tmp/ed only. No figure script involved.

<!-- STATUS: COMPLETE -->
