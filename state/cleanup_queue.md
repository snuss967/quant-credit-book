# Stage 7 Cleanup Queue

Code and consistency fixes found along the way. Lowest priority: run only when no research or writing is queued.

- Listing 25.1 (Appendix F, `#code-25-1`): the last assertion fails. The cycle regex requires whitespace after "means", so "Pro Forma Basis" ("means, with…") is skipped. Fix the regex to allow `means[,\s]`, re-run, then update the prose in Ch 25 if it quotes the cycle size. (Found by U1, 2026-10-18.)
- Ch 19 §19.8.2: the hand estimates "roughly 74bp ... about 35bp" differ from Figure 19.5's 76/37bp. The text already flags them as hand estimates; optionally align. (Found by figure check, 2026-10-18.)
- Ch 15 §15.x after Listings 15.1–15.2: the prose cites 18–19 points, "mid-80s" survival and a 1.2× EBITDA threshold, but the code prints 15.55 points and 81% survival. Reconcile the prose with the listing output (or the listing parameters with the prose). (Found by U1, 2026-10-18.)
- Listing 11.5 demo runs for several minutes; consider a smaller default grid so check_book.py stays fast. (Found by U1, 2026-10-18.)
