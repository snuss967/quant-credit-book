# Stage 7 Cleanup Queue

Code and consistency fixes found along the way. Lowest priority: run only when no research or writing is queued.

- Listing 25.1 (Appendix F, `#code-25-1`): the last assertion fails. The cycle regex requires whitespace after "means", so "Pro Forma Basis" ("means, with…") is skipped. Fix the regex to allow `means[,\s]`, re-run, then update the prose in Ch 25 if it quotes the cycle size. (Found by U1, 2026-10-18.)
- Ch 19 §19.8.2: the hand estimates "roughly 74bp ... about 35bp" differ from Figure 19.5's 76/37bp. The text already flags them as hand estimates; optionally align. (Found by figure check, 2026-10-18.)
- Ch 15 §15.x after Listings 15.1–15.2: the prose cites 18–19 points, "mid-80s" survival and a 1.2× EBITDA threshold, but the code prints 15.55 points and 81% survival. Reconcile the prose with the listing output (or the listing parameters with the prose). (Found by U1, 2026-10-18.)
- Listing 11.5 demo runs for several minutes; consider a smaller default grid so check_book.py stays fast. (Found by U1, 2026-10-18.)
- Listing numbers can run out of chapter order when a reviser adds a listing later (Ch 1: 1.1, 1.2, 1.4, 1.3), and auto descriptions can be weak ("Listing 1.4: Eq"). Add a renumber pass to tools/move_code_to_companion.py (renumber by chapter order, rewrite anchors and links in both files) and give listings real titles. (2026-10-18.)
- Ch 7-B §7-B.8 and exercise 5 quote 17.1% for the monthly grid (continuity-correction approximation), while the simulation, the acceptance test and Figure 7-B.5 give 17.6–17.7%. Reconcile them, or say why they differ. (Figure check, 2026-10-18.)
- Ch 7-B §7-B.6: the Bohn–Stein claim "about half of the time ... 20 bps vs 200 bps" does not follow from the stated one-factor parameters. Re-derive or re-parameterize. (Figure check, 2026-10-18.)
- Ch 4-B Table 4B.1 shows 679 where the listing gives 678.5 (rounding; optional). (Figure check, 2026-10-18.)
- Ch 22 Resource Graph: the Uyeda speech figures must be checked against the SEC page before print (sec.gov returned 403 to scripted fetch). (resgraph, 2026-10-18)
- Ch 13 §13.6: the ΔR cases omit the V/F branch for V<T (figure check). Fix in the lessons pass. (2026-10-18)
- Listing 28.8 (App F) still sets `"sharpe": 2.0`, while revised §28.9 uses 0.7 with a standard error. Set it to 0.7, re-run, and reconcile every §28.9 number quoted from the listing's output. (Red pen, 2026-10-18.)
- The Part I opener now points to §A.10 (the RSSG-to-quant dictionary), which does not exist yet. Write App A §A.10, synthesis item "App A §A.10 dictionary". (Red pen, 2026-10-18.)
- §26.8 cites "OCC Bulletin 2011-12" from the synthesis; occ.gov pages returned 404. Verify before print. (Red pen, 2026-10-18.)
