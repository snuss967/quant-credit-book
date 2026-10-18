# Red-pen log (Edition 2): 00_00_preface.md

## D6 (transition-coach #9, #15, red-pen 6, 10, 11): fixed

Sources read: synthesis row D6; coach gap 9, gap 15, red-pen 6, 10, 11 (the cited "red-pen 6, 10, 11" are the transition coach's, not the RSSG partner's, whose 6/10/11 concern Ch 13, 25 and 5); `state/reviews/ed1/foundations.md` line 175 (preface gets the Laws list and a prerequisite-box legend); `book_src/94_appE_laws_of_the_desk.md` §E.1 (tag form, four families, law names); `state/cast_bible.md`. No web fetch used (no external fact needed).

Changes in `book_src/00_00_preface.md`:

- **"Three ways through the book" became "Four seats through the book"** (coach gap 9, red-pen 6). Opening count fixed: "Eight parts, twenty-eight chapters, three appendices" now reads "Eight parts, twenty-eight numbered chapters, the lettered chapters beside them (4-B, 6-B, 7-B, 12-B and others), Appendices A through F, and growing" (App A-F verified in `book_src/`). Added a one-sentence gloss of the four primers (4-B, 6-B, 7-B, 12-B). Old Path 1 and Path 2 split into a short banker/quant entry paragraph plus four seats: market maker, systematic HY/IG PM, event and distressed quant, risk and strat. Banker route now Part I, 4-B, 5, 6, 6-B, 7-B, 12-B, then Part IV (the coach's order), with the reason (Ch 13-15 use survival analysis, Beta regression and option payoffs built in those chapters). The quant reads 12-B whatever else is skipped. Every old topic kept: Edge Ledger, the five Part IV themes, the Chapter 6 Merton aside (both hedges intact), Ch 13 + Ch 25 back to back, Avellaneda-Stoikov departures (JTD, RFQs, nine-day bonds), Ch 5 recovery and Ch 7 issuer-grouped CV traps, Parts III/V/VI/VII/VIII and Appendix A (now "come back for the Parts you skipped, keep Appendix A open"). Path 3 (AI-agent specifier) kept word for word as "a lens on any seat"; the trend path kept, "fourth" changed to "unofficial" because the seats now number four.
- **Laws-of-the-Desk legend** added after the Desk Debrief sentence in "How a chapter is built": the `[L6]` / `[L4, L7]` tag form, the pointer to Appendix E, and the sixteen law names in their four families (Ruler, Table, Tape, Clock) as printed in App E's headings. No equation or number added beyond law numbers.
- **Prerequisite-box legend** added in the same place: what the `> **Prerequisites.**` box names, that "read X first" means it, that the lettered primers are its usual targets, and a one-clause pointer to Math, Gently boxes for new mathematics.
- **Theo's origin paragraph** (coach gap 15, red-pen 11) added under his cast entry, one paragraph, no dates, no new numbers: no quant résumé; the final-round market-making question from Ines; his knowledge of which paragraph moves the price. Fiction label unchanged (the cast section already says they are fictional). Fact recorded in `state/cast_bible.md` (Theo, Backstory) per the bible's rule 1.

Change in `book_src/01_00_part_I.md` (coach red-pen 10):

- "Part I is the arrival kit: a phrasebook" now points the word at "(Appendix A, §A.10, the banker's word beside the desk's)". Ch 1 is no longer called "the phrasebook and the map" (that would double-book the word); it is now "the shelf and the map". The rest of the Part I opener untouched.

Notes for the integrator:
- App A §A.10 is synthesis item A6 and did not exist when this edit was made; the Part I pointer is live once A6 lands.
- Deliberately not linked from the preface: `00_01`, `00_02`, Ch 4-D and App Z (not yet built). When `00_02` lands, add a one-line pointer in "Four seats through the book".
- Net new words: preface +573, Part I opener +9 (under the 600-word item cap). `tools/check_book.py --file` passes for both files. Both files still end with `<!-- STATUS: COMPLETE -->`.
- No topic removed; no hedge changed; no new unverified number (the only counts used, "twenty-eight" and "Appendices A through F", are stated or verifiable from the file listing).
<!-- STATUS: COMPLETE -->
