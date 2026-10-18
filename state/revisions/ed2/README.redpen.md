# Red-pen log (Edition 2): README.md

## D10 (transition-coach #5, red-pen 12; desk-head gap 5 / synthesis A2 for the `book_src/lib/` part): fixed

All changes in `README.md`. Only the README parts of D10 were done; `tools/check_book.py`, App F and `00_02_how_to_use_this_book.md` belong to other items.

- **New subsection "Run the book's code"** (end of "Run it", after the `--dangerously-skip-permissions` paragraph). Three short paragraphs:
  1. Python environment: "Python 3.9 or newer" plus `pip install -r requirements.txt`; says chapter code imports only NumPy, SciPy, pandas and the standard library, and `pymupdf` is only for `index_pdfs.py`.
  2. Blocks accumulate per chapter: `check_book.py` joins a chapter's python blocks in order into one script in a fresh temp directory, so a lone pasted listing raises `NameError`; gives the one-chapter command (`--file book_src/<chapter>.md --run-code`); nothing carries across chapters.
  3. `book_src/lib/`: the reusable engines (`bondmath.py`, `creditstats.py`, `risk_model.py`) are meant to live there; states honestly that the `sys.path` change in `check_book.py` is an Edition 2 item that has not landed, and gives the working stopgap (absolute `PYTHONPATH`, or paste the defining listing).
- **Layout tree:** `book_src/` comment extended with "; lib/ holds the shared modules (Edition 2)". Directory does not exist yet, hence the Edition 2 tag.
- **House rules, "Code that runs" bullet:** one sentence appended pointing to `book_src/lib/` and the new subsection. Existing sentences (one interpreter, `# sketch`) unchanged.
- **Unchanged:** line 5's "Code examples have not been executed yet" hedge, all other bullets, the file's last line (the README has no STATUS comment line).

Verification (no web fetch needed for facts in the text; 4 PyPI metadata fetches used for the version floor): `requires_python` for numpy 1.26.0 (`>=3.9,<3.13`), scipy 1.11.0 (`>=3.9,<3.13`), pandas 2.1.0 (`>=3.9`), networkx 3.2 (`>=3.9`) confirms the 3.9 floor; the listings use builtin generics (`tuple[float, float]`, PEP 585, 3.9+) and every `X | None` annotation I traced sits in an App F block with `from __future__ import annotations`. Import census of non-`# sketch` python blocks in `book_src/` found only numpy, scipy, pandas and stdlib, plus two sibling-module imports (`lmt_engine`, `restructuring_state_machine`, both App F lines ~13712). `check_book.py` behaviour (joined script, `cwd` temp dir, `env={**os.environ, ...}`) read from the source and tested: a scratch chapter importing a module fails without `PYTHONPATH` and passes with the absolute path. No new unverified numbers; no topic removed.

Flag for the owner of A2: `requirements.txt` carries statsmodels, scikit-learn and networkx that no chapter block imports, and matplotlib (used by `tools/figures/`) is absent; left as is, outside D10.
<!-- STATUS: COMPLETE -->
