# Systematic & Quantitative Credit: From PJT RSSG to the Automated Desk

A book that writes itself: an autonomous agent loop grows a rigorous, and deliberately entertaining, treatise on quantitative credit, market microstructure, and special situations. Fable advisors dissect each topic before a writer agent expands it, and the whole thing recompiles every six hours.

**Edition 1 shipped (2026-10-18):** 28 chapters, preface, 8 part openers, and 3 appendices. About 474k words, a 1,212-page PDF. Facts in the Trend Watch boxes were fact-checked (≈95% of verifiable claims confirmed; corrections queued for Edition 2). Code examples have not been executed yet. See `CHANGELOG.md` and `state/continuation_prompt.md` for Edition 2.

**Read the book:** [`output/Quant_Credit_Master_Book.html`](output/Quant_Credit_Master_Book.html) (MathJax, clickable TOC), [`output/Quant_Credit_Master_Book.pdf`](output/Quant_Credit_Master_Book.pdf), or the Markdown monolith [`output/Quant_Credit_Master_Book.md`](output/Quant_Credit_Master_Book.md). Each chapter also stands alone in [`book_src/`](book_src/).

## Layout

```
quant-credit-book/
├── SYSTEM_PROMPT.md           # master instruction for every agent (mission, TOC, chapter anatomy, integrity rules)
├── orchestrator.py            # infinite loop: Fable advisor → writer → guard rails → 6-hour rebuild
├── build_book.sh              # Pandoc compiler → output/*.md, *.html, *.pdf
├── index_pdfs.py              # splits source_pdfs/ into per-page text for citation
├── tools/
│   ├── pdf_search.py          # find pages by keyword, print a TOC or a page
│   ├── check_book.py          # lint chapter anatomy and execute every chapter's Python
│   ├── status.py              # COMPLETE / PARTIAL / MISSING for every brief, chapter, and dossier (drives restarts)
│   ├── outline.py             # compact digests so reviewers read outlines, not 400k words
│   ├── usage_meter.py         # estimate usage-window burn from transcripts (calibrate to real readings)
│   └── pace_guard.py          # background guard: wakes the orchestrator when burn is too fast or near the cap
├── source_pdfs/               # the shelf (PDF + EPUB)
├── state/
│   ├── book_state.json        # queue, completed modules, case studies, word counts
│   ├── style_bible.md         # voice, cast, running gags, notation table (by the Fable Showrunner)
│   ├── PROCESS.md             # the production line, durability rules, usage economics
│   ├── run_ledger.md          # every workflow run, what it owns, incidents
│   ├── reviews/ed1/           # Fable engagement and foundations reviews, Sonnet fact-checks, writer returns
│   ├── research/              # trend dossiers (dated, sourced)
│   ├── advisor_briefs/        # Fable dissection briefs, one per chapter plus one per loop iteration
│   ├── pdf_index.json         # per-book TOC and page counts
│   ├── iteration_log.jsonl    # one line per loop iteration
│   └── pdf_pages/             # derived page text (gitignored; rebuilt by index_pdfs.py)
├── book_src/                  # modular chapters, compiled in lexicographic order
├── assets/book_head.html      # reading styles for the HTML/PDF build
└── output/                    # compiled book
```

## Run it

```bash
pip install -r requirements.txt          # plus pandoc; Chromium is optional (enables the PDF)
python3 index_pdfs.py                    # once, and again whenever you add books
chmod +x build_book.sh && ./build_book.sh
python3 orchestrator.py                  # forever; Ctrl-C finishes the current step and exits
python3 orchestrator.py --once           # a single iteration
```

The orchestrator calls the `claude` CLI twice per iteration:

1. **Fable advisor pass** (`ADVISOR_MODEL`, default `claude-fable-5-1`): strategizes and dissects the target. It produces the thesis, an outline of new material, verified derivation skeletons, a code spec, source pages, case-study facts marked VERIFIED or CHECK, and the jokes that teach. The brief goes to `state/advisor_briefs/<chapter>__itNNNN.md`.
2. **Writer pass** (`WRITER_MODEL`, CLI default): expands the chapter from the system prompt, style bible, and briefs, then asks a Fable referee to check its hardest math.

After both passes it restores `book_state.json` if the agent corrupted it, executes the chapter's Python with `tools/check_book.py --run-code`, and puts a FIX task at the head of the queue if anything broke. A target that stalls twice rotates to the back of the queue. Every iteration is logged, and the book rebuilds whenever six hours have passed. Set `AUTO_COMMIT=1` to commit each iteration, and add `AUTO_PUSH=1` to push as well.

The orchestrator runs the CLI with `--dangerously-skip-permissions`, so run it in a sandbox or container you are comfortable handing to an unattended agent.

## House rules (summarized from SYSTEM_PROMPT.md)

- **Six-part anatomy** in every chapter: desk framing, rigorous derivation, `### Specification for AI Implementation`, `> [SOURCE EXTRACTION]`, a case study, and a `### Deep-Dive Resource Graph`. `check_book.py` flags whichever are missing.
- **Code that runs.** All of a chapter's ```` ```python ```` blocks run in order in one interpreter, so later blocks can use earlier definitions. Start a block with `# sketch` to exempt pseudo-code.
- **Quote briefly, cite exactly.** Source extractions are short quotations with `book_id p.N` citations followed by our own analysis. Derivations are rebuilt, not transcribed.
- **No fabrication.** CUSIPs, URLs, SSRN ids, and episode numbers appear only when verified. Historical numbers are either sourced or labeled illustrative.
