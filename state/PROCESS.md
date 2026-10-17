# The Production Line

How the book gets made, edition after edition. Every stage has one owner, one set of artifacts, and a gate. The goal is maximum research and writing per token, with no duplicated work.

## Stages (one edition)

| # | Stage | Owner (model) | Artifacts | Gate to start |
| :--- | :--- | :--- | :--- | :--- |
| 0 | **Plan** | Fable edition planner | `state/continuation_prompt.md`, TOC in `SYSTEM_PROMPT.md` §3, `book_state.json` queue | Previous edition shipped |
| 1 | **Research** | Researchers (default model), closed by a **Fable mapper** per batch | `state/research/{trend,case,shelf,papers,media}_*.md`, `state/research/map_*.md`, `exploratory_space_*.md` | Topic not already in the ledger |
| 2 | **Advise** | **Fable advisor** per chapter | `state/advisor_briefs/<stem>.md` (or `__edN.md`) | Chapter is in the TOC |
| 3 | **Write** | Writer per chapter | `book_src/<stem>.md` | Its brief exists |
| 4a | **Pre-flight review** | **Fable engagement advisor** + **Fable foundations explainer** (on brief digests) | `state/reviews/edN/preflight_{engagement,foundations}.md` | All briefs for the edition exist |
| 4b | **Full review** | Per Part: **Fable engagement advisor** + **Fable foundations explainer** (on chapter text) | `state/reviews/edN/part_<X>_{engagement,foundations}.md` | All chapters in that Part exist |
| 5 | **Ship** | Orchestrator (me) | `output/*`, `CHANGELOG.md`, git commit + push | Every TOC chapter exists and the build passes |
| 6 | **Synthesize** | Fable edition planner | Next edition's Stage 0 artifacts | Reviews and research maps are done |
| 7 | **Cleanup** (lowest priority) | Any idle slot | Code-example fixes via `tools/check_book.py --run-code` | Nothing else is queued |

## Resource Rules

1. **One owner per topic.** Before launching research, check `state/run_ledger.md` and `ls state/research/`. Never research a topic twice in one edition. Deepen an existing dossier instead.
2. **Digests before documents.** Reviewers and planners read `tools/outline.py` digests (`state/digests/`) first and open full files only where needed.
3. **Fable for judgment, default model for volume.** Fable handles strategy, dissection, mapping, engagement, foundations, and planning. The default model handles research sweeps and long-form writing.
4. **Research and writing first; checking last.** Do not run or debug code examples while research or writing remains (Stage 7 only).
5. **Concurrency.** Each workflow runs 2 agents at once on this machine, so parallelism comes from running several workflows side by side. Target about 30–36 live agents. Never launch a workflow whose outputs overlap a running one.
6. **Canonical homes.** Each case study and each foundation concept has exactly one canonical chapter, set in `state/reviews/edN/preflight_*.md`. Every other chapter cross-references it instead of retelling it.
7. **Commit early, commit often.** Snapshot agent output to git at every turn boundary. Ship each edition as a single tagged commit message ("Ship Edition N").
