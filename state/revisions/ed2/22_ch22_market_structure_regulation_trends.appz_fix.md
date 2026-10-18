# Ch22 App Z numbers-editor log

## Note 1 (Z.22.2, §22.2.3 Poker Table, "lower the cap")
- Note: Ines says "nobody at this table will ever vote to *lower* the cap", but under (22.7) with alpha fixed lowering the cap helps her \$15mm block; raising it hurts.
- Recomputation (python3): cap effect on half-spread = lambda(mC - Q)(1 - Delta/T_u)^+, lambda = 0.5, Q = 15, Delta = 15, T_u = 120, m = 2.5. C = 5: mC = 12.5, effect -1.094bp (subsidy). C = 3: mC = 7.5, effect -3.281bp (bigger subsidy). C = 10: mC = 25, effect +4.375bp (tax). The note's numbers are right. The Poker Table itself says the cap "hid two and a half million of our size" (0.5 x 2.5 = 1.25bp), and Beat 3 says the 2019 pilot (higher caps) needed a 48-hour delay as compensation, so block desks resist a higher cap, not a lower one.
- Ruling: fixed (note right; chapter wrong).
- Edit, book_src/22_ch22_market_structure_regulation_trends.md, Poker Table: "why nobody at this table will ever vote to lower the cap." -> "why nobody at this table will ever vote to raise the cap."
- App Z: solution text never quoted the word; it already says large-block desks "defend the \$5mm cap" and accept a higher one only with compensation. NOTE paragraph deleted from state/appZ/22_ch22_market_structure_regulation_trends.md.

<!-- STATUS: COMPLETE -->
