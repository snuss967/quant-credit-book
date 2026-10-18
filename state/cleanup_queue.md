# Stage 7 Cleanup Queue

Code and consistency fixes found along the way. Lowest priority: run only when no research or writing is queued.

- Listing 25.1 (Appendix F, `#code-25-1`): the last assertion fails. The cycle regex requires whitespace after "means", so "Pro Forma Basis" ("means, with…") is skipped. Fix the regex to allow `means[,\s]`, re-run, then update the prose in Ch 25 if it quotes the cycle size. (Found by U1, 2026-10-18.)
- Ch 19 §19.8.2: the hand estimates "roughly 74bp ... about 35bp" differ from Figure 19.5's 76/37bp. The text already flags them as hand estimates; optionally align. (Found by figure check, 2026-10-18.)
