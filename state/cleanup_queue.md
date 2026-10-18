# Stage 7 Cleanup Queue

Code and consistency fixes found along the way. Lowest priority: run only when no research or writing is queued.

- Listing 25.1 (Appendix F, `#code-25-1`): the last assertion fails. The cycle regex requires whitespace after "means", so "Pro Forma Basis" ("means, with…") is skipped. Fix the regex to allow `means[,\s]`, re-run, then update the prose in Ch 25 if it quotes the cycle size. (Found by U1, 2026-10-18.)
  - DONE 2026-10-18: Listing 25.1 regex now means[,\s]; all asserts pass; Ch 25 loop prose reconciled
- Ch 19 §19.8.2: the hand estimates "roughly 74bp ... about 35bp" differ from Figure 19.5's 76/37bp. The text already flags them as hand estimates; optionally align. (Found by figure check, 2026-10-18.)
- Ch 15 §15.x after Listings 15.1–15.2: the prose cites 18–19 points, "mid-80s" survival and a 1.2× EBITDA threshold, but the code prints 15.55 points and 81% survival. Reconcile the prose with the listing output (or the listing parameters with the prose). (Found by U1, 2026-10-18.)
- Listing 11.5 demo runs for several minutes; consider a smaller default grid so check_book.py stays fast. (Found by U1, 2026-10-18.)
- Listing numbers can run out of chapter order when a reviser adds a listing later (Ch 1: 1.1, 1.2, 1.4, 1.3), and auto descriptions can be weak ("Listing 1.4: Eq"). Add a renumber pass to tools/move_code_to_companion.py (renumber by chapter order, rewrite anchors and links in both files) and give listings real titles. (2026-10-18.)
- Ch 7-B §7-B.8 and exercise 5 quote 17.1% for the monthly grid (continuity-correction approximation), while the simulation, the acceptance test and Figure 7-B.5 give 17.6–17.7%. Reconcile them, or say why they differ. (Figure check, 2026-10-18.)
- Ch 7-B §7-B.6: the Bohn–Stein claim "about half of the time ... 20 bps vs 200 bps" does not follow from the stated one-factor parameters. Re-derive or re-parameterize. (Figure check, 2026-10-18.)
- Ch 4-B Table 4B.1 shows 679 where the listing gives 678.5 (rounding; optional). (Figure check, 2026-10-18.)
- Ch 22 Resource Graph: the Uyeda speech figures must be checked against the SEC page before print (sec.gov returned 403 to scripted fetch). (resgraph, 2026-10-18)
- Ch 13 §13.6: the ΔR cases omit the V/F branch for V<T (figure check). Fix in the lessons pass. (2026-10-18)
  - DONE 2026-10-18: added V/F branch (V<=T) and (V-T)+ to ΔR cases
- Listing 28.8 (App F) still sets `"sharpe": 2.0`, while revised §28.9 uses 0.7 with a standard error. Set it to 0.7, re-run, and reconcile every §28.9 number quoted from the listing's output. (Red pen, 2026-10-18.)
- The Part I opener now points to §A.10 (the RSSG-to-quant dictionary), which does not exist yet. Write App A §A.10, synthesis item "App A §A.10 dictionary". (Red pen, 2026-10-18.)
- §26.8 cites "OCC Bulletin 2011-12" from the synthesis; occ.gov pages returned 404. Verify before print. (Red pen, 2026-10-18.)
- App F Listing 1.2 contains stray §1.5 prose (verify, Ch 1). Move the prose back to the chapter or delete it from the listing block. (2026-10-18)
  - DONE 2026-10-18: already clean, no edit; fences balanced; Listing 1.3 heading intact
- The citation 'SSRN 6088966' (Dickerson–Robotti–Rossetti 2026) could not be confirmed. The verified id is arXiv:2604.07880. Replace it wherever the book cites SSRN 6088966 (grep book_src). (TSMOM dossier, 2026-10-18)
  - DONE 2026-10-18: dossier line 32 now cites arXiv:2604.07880; book_src already clean
- Ch 4-C §4C.6: 'Tuesday … day 14' is a Wednesday by the chapter's own calendar (figure check). Fix the weekday. (2026-10-18)
  - DONE 2026-10-18: Tuesday changed to Wednesday; day 14 is Wednesday (Friday day 1)
- Ch 3 §3.4 SVB coda: the Bloomberg (2 Jul 2024) "40% or better" recovery for creditors owed \$3.5bn is now hedged as "press reports put"; confirm the exact wording against the original Bloomberg article before print. (Lessons pass, 2026-10-18.)
- Ch 3 §3.7 "After the announcement": the remand's mitigation figures (29%–43% of observed volume vs \$62mm–\$94mm) did not reconcile with the \$186mm volume (29–43% of \$186mm is \$54mm–\$80mm); the dollar range was cut from the text. Check the Serta remand opinion (July 2026) for the base the experts used, and restore the dollar range if it can be tied. (Lessons pass, 2026-10-18.)
- Ch 3 §3.7: an event study of Serta first-lien flow in May–June 2020 (does net buying by LME-prone accounts show the pre-uptier signature?) was promised as future work in book text; the promise was cut. Open research item if wanted. (Lessons pass, 2026-10-18.)
- Ch 1 Resource Graphs (§1.8 and §1.10): the *Odd Lots* entries are still channel-level (no episode titles, dates or URLs); the lessons pass removed the "episode numbers omitted" process notes from the text. U3: replace with verified episodes (Ch 1-B already cites "How the Hottest Hedge Funds on Wall Street Really Manage Risk", 25 Jul 2024) or cut. (Lessons pass, 2026-10-18.)
- Ch 16 §16.2 (line ~176) says "Chapter 1's box in §1.8.1 has the same curve for price pressure"; the Ch 1 lessons pass turned that half-life box into a two-sentence gloss (same curve, same section), and Ch 9 §9.4 now holds the half-life box. Reword to "Chapter 1's §1.8.1 (and the box in §9.4)". (Lessons pass, 2026-10-18.)
- An Ares quote that the sources disagree on (speaker and wording) was removed from Ch 25 by verify, but Ch 17 and perspectives_buyside_credit_managers.md still carry it. Re-verify the quote or remove it from Ch 17. (verify Ch 25, 2026-10-18)
- Date clash: 23 October in Ch 24 versus Ch 19 and Ch 21 (verify Ch 24). Reconcile. (2026-10-18)
- **Data licensing (owner decision before publication).** Some figures plot FRED series that redistribute ICE BofA index data (e.g., BAMLH0A0HYM2 and the rating-tier OAS series) and Moody's yields (BAA10Y). Both carry reproduction restrictions on FRED. Affected scripts are listed by `grep -l "BAML\|ICE BofA\|BAA10Y\|Moody" tools/figures/*.py`. Before any public release, either get permission, switch to unrestricted series (e.g., FRED-computed Treasury data, TRACE aggregates, or the book's own simulated series, captioned Illustrative), or keep the figures for private use only. (Figure checks Ch 10, 11, 2026-10-18)
