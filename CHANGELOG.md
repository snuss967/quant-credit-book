# Changelog

*Systematic & Quantitative Credit: From PJT RSSG to the Automated Desk.* One entry per edition. The planning entry for the next edition is filled in when that edition ships.

## Edition 1 (2026-10-18)

**Built.**
- 28 chapters in eight Parts (`book_src/01_ch01` … `28_ch28`), 13–19k words each, about 467k words of chapter text and 471k in `book_src/` with the preface, eight Part openers and Appendices A (notation and conventions), B (data and API atlas) and C (Trend Tracker, a 3.1k-word megatrend summary rather than the dated row table the TOC describes).
- One voice and one cast across independently written chapters: Theo, Ines, Kaz, Mags, ROBO and the Ad Hoc Group; the 13-week-model arc from emotional support (Ch 1) to the PM dashboard (Ch 28); about 74 Trend Watch boxes, 290 source extractions with annotations, 64 Ways This Blows Up, 29 Poker Tables, 12 Docket Diaries, and a Specification for AI Implementation with Python in every chapter.
- The production line in `state/PROCESS.md`: Sonnet research dossiers (`state/research/`), Fable advisor briefs per chapter (`state/advisor_briefs/`), Opus writers, Fable engagement and foundations reviews (`state/reviews/ed1/`), Sonnet fact-checks of every Trend Watch box, writer returns consolidated for the next planner, and a build to Markdown, HTML and PDF in `output/`.

**Known limitations (carried into the Edition 2 plan).**
- *Unverified facts.* About 520 Trend Watch claims were checked: about 350 confirmed, 16 corrected and 4 stale (corrections recorded in `state/reviews/ed1/factcheck_*.md` but not yet applied to the text), about 156 unverifiable from accessible sources; the boxes in chapters 18–21 are still unchecked. Writers left about 60 CHECK-flagged facts hedged in the text.
- *Unexecuted code.* Every reference implementation was written to run and never executed, by rule (research and writing first). Writers named the asserts most likely to need tuning.
- *Overlap and missing homes.* The same cases are retold in many chapters (Serta in 15 files, March 2020 in 19, April 2025 in 12) with no canonical home; Boardriders, Envision, Incora and Robertshaw are promised by the TOC and have no Docket Diary; the fictional issuer Halvorsen has three lines of business; the cooperation-agreement counter is out of sequence.
- *Foundations built late.* Bond arithmetic, option pricing beyond the Merton formula, regression and survival analysis as methods, the bankruptcy and lien process, and market plumbing are used from Chapter 1 and built, where built, in Chapters 8–24; there are no prerequisite boxes and Chapter 23 has no section cross-references.
- *Length and figures.* Every chapter exceeds its 8–12k brief; exercises run 0–24 per chapter; one image in the whole book.

## Edition 2 (planned)

Theme: **"One Author, One Floor, One Home."** Plan in `state/continuation_prompt.md`; new files listed in `SYSTEM_PROMPT.md` §3 "Edition 2 additions"; research in `state/research_queue_ed2.json`; the living map in `state/exploratory_space.md`.

Work packages, in order: (1) apply the fact-check corrections and finish chapters 18–21; (2) four foundation primers (4-B bond math, 6-B options and measures, 7-B statistics for credit panels, 12-B the restructuring process as a state machine), Appendices D (plumbing) and E (laws of the desk), and prerequisite boxes with reading-order fixes; (3) canonical case-study homes, the fictional-issuer bible and running-gag repairs; (4) five new chapters where the research is thickest (9-B the bond data problem and the replication crisis; 10-B credit index futures; 13-B the Autopsy Room; 17-B marking the unmarked; 18-B the RFQ response engine) and the "Tape to Your Monitor" front matter; (5) targeted expansions, led by one figure per chapter and a dated Appendix C; (6) tightening every Edition 1 chapter to at most 15k words; (7) code cleanup last.

Shipped: *(to be filled at ship time: new word counts, files added, fact-check and code ledgers, what was deferred to Edition 3).*
