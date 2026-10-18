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
7. **Web search is shared and rate-limited.** Search before you fetch only when you don't know the primary source. Prefer WebFetch on known primary URLs (regulators, courts, exchanges, papers). Never repeat a search whose answer already sits in `state/research/`. If search is throttled, fall back to fetching primary sources directly.
8. **Commit early, commit often.** Snapshot agent output to git at every turn boundary. Ship each edition as a single tagged commit message ("Ship Edition N").

## Durability & Restart Rules

*Added after the 2026-10-17 outage. Around 36 concurrent agents exhausted the session usage limit near 23:25 UTC, and every in-flight agent died. Files on disk survived. Research and drafts held only in agent context were lost: about 49 research dossiers, every chapter writer, and 9 advisors.*

1. **Write early, write often.** Every agent creates its output file within its first few tool calls, as a skeleton with headings, then appends each section as soon as it is drafted. Never hold more than about 1,500 words of prose or about 10 sourced facts only in context. Researchers append facts to the dossier's evidence table as they find them.
2. **Completion marker.** An agent's final action is appending `<!-- STATUS: COMPLETE -->` as the file's last line. A file without the marker is PARTIAL by definition.
3. **Resume, never restart.** An agent whose output file already exists reads it first. If it is COMPLETE, the agent returns immediately. If it is PARTIAL, the agent continues from the last finished section and does not rewrite what exists.
4. **Status-driven relaunch.** Restarts are built from `python3 tools/status.py --json`: COMPLETE items are skipped, PARTIAL items resumed, MISSING items started. Never relaunch from memory.
5. **Usage pacing.** Cap live agents at about 20 (about 10 workflows). Priority order: (a) the current edition's chapters, (b) research feeding the next edition, (c) reviews, (d) cleanup. Launch a lower tier only when the higher tiers are already running.
6. **Limit handling.** When agents fail with a session or usage limit, stop launching. Record the reset time in the ledger, schedule a resume (`send_later`) for reset + 2 minutes, and resume from `tools/status.py`.
7. **Retry once.** Workflow scripts retry a failed agent once. Persistent failures are returned in the result and recorded in the ledger.
8. **Snapshots.** A background auto-commit runs every 10 minutes, plus a commit at every turn boundary, so partial files reach the remote within 10 minutes.
9. **Let unsaved work finish.** Do not kill a running agent that holds unsaved research unless it is duplicating other work. A stopped agent's context is lost.

## Usage Economics & Pacing Playbook (measured 2026-10-17)

*Measured with `tools/usage_meter.py`, calibrated to the user's reading of 30% at 23:46 UTC in a 5-hour window.*

- **Long Fable research loops are the expensive thing.** Twelve Fable advisors at xhigh effort, doing web research, burned about 1.0% of the window per minute, with about 1M cache-write tokens per agent every 10 minutes. Opus writers cost a fraction of that per agent.
- **So Fable does judgment, not legwork.** Use Fable for short, high-judgment passes over prepared material: dissection from a dossier, mapping, engagement and foundations reviews, and edition planning. Give it digests and dossiers rather than open-ended web research.
- **Bulk research goes to Sonnet researchers.** Fact-gathering dossiers are written to disk with sources; a short Fable pass then turns the dossier into a brief.
- **Writers stay on Opus but work lean.** They read only the style bible, their brief, and the needed SYSTEM_PROMPT sections. They write in 3–5 large passes, make at most about 6 web calls, and run no builds or code (the orchestrator builds centrally).
- **Pace to the window.** Sustainable rate = (target − used) / minutes left. `tools/pace_guard.py` runs in the background and wakes the orchestrator only on TOO_FAST, SLACK, or NEAR_CAP. Start at about 4 Opus writers and adjust on its signals.
- **Cap: 97% of the window (user, 2026-10-18).** Run the guard with `--target 97`, which alarms at 91%.
- **Throughput mode (the user's preference, 2026-10-18).** Finishing early and idling until the reset is fine. Run wide (about 8 lean Opus writers), with `pace_guard.py --cap-only`, which alarms only near the cap (target − 6%). At the alarm, stop new launches; in-flight work is crash-safe and resumes after the reset.
- **Verify every stop.** After stopping workflows, check `usage_meter.py`'s per-model breakdown 5 minutes later. A stopped model's burn must fall to about zero. (On 2026-10-18 a forgotten media-research workflow kept a Fable mapper running at xhigh effort for 15 minutes after the "stop everything".)
- **The user's reading is the ground truth.** The meter's token weights are only approximate (they underestimated real usage about 2.5x). Recalibrate at every reading (`--calibrate PCT AT_ISO`) and use the meter for relative burn and projections only.
- **Before every launch, check the meter.** `python3 tools/usage_meter.py`. When the user reports a reading, recalibrate with `--calibrate PCT AT_ISO`.
