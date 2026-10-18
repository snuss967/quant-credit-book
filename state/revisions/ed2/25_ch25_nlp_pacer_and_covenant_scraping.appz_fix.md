# Ch 25 App Z editor-note fixes (numbers editor)

One NOTE (for the editor) paragraph found in state/appZ/25_ch25_nlp_pacer_and_covenant_scraping.md. Deleted from the solutions file after ruling.

## 1. Section 25.7.3: "only three of the seven rows move a term-loan recovery"
- Note: by the Rule 2019 table's own rows, four rows (Docs. 69, 75, 389, 1116, the two lender groups) move a term-loan recovery; three (273, 289, 311: utilities, equity group) do not.
- Recomputation (python3): table has 7 rows; lender-group rows = [69, 75, 389, 1116] = 4; non-lender rows = [273, 289, 311] = 3. The surrounding text agrees (beat three: Docs. 273, 289, 311 are the three irrelevant 2 a.m. pages; Doc. 69 + 389 + 1116 are the priority group's three snapshots; Doc. 75 is the excluded first-lien lenders' original). The App Z solution to Exercise 6 already says the spec pages for Docs. 69, 75, 389 and 1116 and digests 273, 289, 311.
- Ruling: note right (fixed).
- Chapter (Section 25.7.3, sentence below the `type=rd` table): "...and only three of the seven rows move a term-loan recovery." -> "...and only four of the seven rows move a term-loan recovery."
- Solution (Exercise 6): did not quote the old value; no text change. NOTE paragraph deleted.
- Not touched: state/appZ/_editor_notes.md (aggregate copy of notes, outside the assigned files).

<!-- STATUS: COMPLETE -->
