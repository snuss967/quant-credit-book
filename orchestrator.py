# orchestrator.py
"""The infinite book factory: research, write, and ship the book in editions, forever.

Each iteration:
  1. Pick the target: expansion_queue[0]. If the queue is empty, the edition is done:
     a FABLE EDITION PLANNER reads the research and the book, grows the TOC, writes
     state/continuation_prompt.md and a fresh queue, bumps the edition, and the book rebuilds.
  2. FABLE ADVISOR pass: a `claude` call on the advisor model researches and dissects
     the target and writes state/advisor_briefs/<stem>__itNNNN.md.
  3. WRITER pass: a `claude` call researches further and expands the chapter.
  4. Guard rails: restore book_state.json if the agent corrupted it, recount words, log the
     iteration, optionally git commit/push. Running chapter code is OFF by default (it is the
     lowest priority); set RUN_CODE_CHECKS=1 to execute it and queue fixes at the END of the queue.
  5. If 6 hours have passed since the last build, run ./build_book.sh.

Usage:
  python3 orchestrator.py                # run forever (Ctrl-C finishes the current step and exits)
  python3 orchestrator.py --once         # one iteration, then exit
  python3 orchestrator.py --build-only   # just compile the book
  python3 orchestrator.py --plan-edition # close the current edition and plan the next one now

Environment:
  AGENT_CMD            agent CLI (default: claude)
  ADVISOR_MODEL        model for advisor/planner passes (default: claude-fable-5-1)
  WRITER_MODEL         model for the writer pass (default: the CLI's default)
  ITERATION_TIMEOUT_S  per-agent-call timeout in seconds (default: 5400)
  RUN_CODE_CHECKS=1    execute chapter Python after each iteration (low priority)
  AUTO_COMMIT=1        git commit after every iteration;  AUTO_PUSH=1 also pushes
"""
import argparse
import glob
import json
import os
import re
import shutil
import signal
import subprocess
import sys
import time
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)

BUILD_INTERVAL_SECONDS = 6 * 3600  # 6 hours
STATE_FILE = "./state/book_state.json"
STATE_BACKUP = STATE_FILE + ".bak"
LOG_FILE = "./state/iteration_log.jsonl"
BRIEF_DIR = "./state/advisor_briefs"
CONTINUATION = "./state/continuation_prompt.md"
TARGET_RE = re.compile(r"^\s*([\w.-]+\.md)\s*:\s*(.*)$", re.S)
MIN_WORD_GAIN = 500  # below this, the iteration counts as a failed attempt

AGENT_CMD = os.environ.get("AGENT_CMD", "claude")
ADVISOR_MODEL = os.environ.get("ADVISOR_MODEL", "claude-fable-5-1")
WRITER_MODEL = os.environ.get("WRITER_MODEL") or None
ITERATION_TIMEOUT_S = int(os.environ.get("ITERATION_TIMEOUT_S", "5400"))

INITIAL_STATE = {
    "edition": 1,
    "iteration": 0,
    "last_build_timestamp": 0,
    "completed_modules": [],
    "case_studies": [],
    "chapters": {},
    "attempts": {},
    "expansion_queue": [],
}

DURABILITY = """DURABILITY (non-negotiable; you can be killed at any moment by a usage limit):
- Create your output file in your first few tool calls and append each section as soon as it is drafted; never hold more than ~1,500 words or ~10 sourced facts only in context.
- If your output file already exists, read it first: if it ends with `<!-- STATUS: COMPLETE -->` and your task is new writing, report and stop; if it is partial, continue from the last finished section without rewriting.
- When EXPANDING a complete file, first delete its `<!-- STATUS: COMPLETE -->` line, then append, then restore the marker as the last line when done.
- Your final action is appending `<!-- STATUS: COMPLETE -->` as the last line of your output file."""

_stop = False


def _request_stop(signum, frame):
    global _stop
    _stop = True
    print(f"\n[{now()}] stop requested: finishing the current step, then exiting.")


def now():
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")


# ---------------------------------------------------------------- state ----

def load_state():
    with open(STATE_FILE, encoding="utf-8") as f:
        return json.load(f)


def save_state(state):
    tmp = STATE_FILE + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2)
    os.replace(tmp, STATE_FILE)


def reload_state_or_restore():
    try:
        return load_state()
    except (json.JSONDecodeError, OSError):
        print(f"[{now()}] book_state.json corrupted by the agent; restoring backup.")
        shutil.copyfile(STATE_BACKUP, STATE_FILE)
        return load_state()


def ensure_workspace():
    for d in ("./state", "./book_src", BRIEF_DIR, "./state/research"):
        os.makedirs(d, exist_ok=True)
    if not os.path.exists(STATE_FILE):
        save_state(INITIAL_STATE)
    if not glob.glob("./state/pdf_pages/*/page_0001.txt"):
        print(f"[{now()}] page index missing: running index_pdfs.py")
        subprocess.run([sys.executable, "index_pdfs.py"], check=False)


def word_counts():
    counts = {}
    for path in sorted(glob.glob("./book_src/*.md")):
        with open(path, encoding="utf-8") as f:
            counts[os.path.basename(path)] = len(f.read().split())
    return counts


# ---------------------------------------------------------------- build ----

def rebuild_book(state):
    print(f"\n[{now()}] >>> REBUILDING MASTER BOOK (Edition {state.get('edition', 1)})...")
    subprocess.run(["./build_book.sh"], check=False)
    state["last_build_timestamp"] = time.time()
    save_state(state)


def maybe_rebuild_book():
    state = load_state()
    if time.time() - state.get("last_build_timestamp", 0) >= BUILD_INTERVAL_SECONDS:
        print(f"[{now()}] 6-hour timer triggered.")
        rebuild_book(state)


# ---------------------------------------------------------------- agents ---

def run_agent(prompt, model=None, label="agent"):
    cmd = [AGENT_CMD, "--dangerously-skip-permissions"]
    if model:
        cmd += ["--model", model]
    cmd += ["-p", prompt]
    print(f"[{now()}] {label}: {' '.join(cmd[:4])} ...")
    try:
        return subprocess.run(cmd, check=False, timeout=ITERATION_TIMEOUT_S).returncode
    except subprocess.TimeoutExpired:
        print(f"[{now()}] {label} timed out after {ITERATION_TIMEOUT_S}s")
        return -1
    except FileNotFoundError:
        sys.exit(f"Agent CLI '{AGENT_CMD}' not found. Install Claude Code or set AGENT_CMD.")


def edition_planner_prompt(edition):
    return f"""You are the FABLE EDITION PLANNER for the book in this repository. Edition {edition} is complete; plan Edition {edition + 1}.

Read ./SYSTEM_PROMPT.md (TOC + growth rule), ./state/book_state.json, ./state/continuation_prompt.md (if present), ./state/exploratory_space.md and everything in ./state/research/, and skim ./book_src/ (word counts, section headings, Trend Watch boxes).

Then research what has changed in credit markets and quant credit since the last edition: run web searches for fresh trend data, rulings, papers, and market-structure news. Save new findings to ./state/research/ with dated, sourced facts.

Strategize and dissect, then write:
1. ./state/continuation_prompt.md: a self-contained prompt for Edition {edition + 1}. Cover its theme, the TOC changes, per-chapter expansion targets, new chapters to write, open research questions, unverified facts to chase, and new trend threads.
2. Grow the TOC in ./SYSTEM_PROMPT.md section 3 using the growth rule (new chapters as NN_chNNb_slug.md), and update ./state/exploratory_space.md.
3. Replace `expansion_queue` in ./state/book_state.json with 20–40 targets in the form "FILE.md: description", ordered by leverage, with new chapters and trend threads first. Set "edition" to {edition + 1}. Leave `iteration`, `last_build_timestamp`, `chapters`, and `attempts` alone.
4. Append the Edition {edition + 1} plan to ./CHANGELOG.md.
Research and planning are your job; do not run code examples.

{DURABILITY}"""


def advisor_prompt(task, target_file, stem, brief_path, edition):
    chapter_brief = os.path.join(BRIEF_DIR, f"{stem}.md")
    return f"""You are a FABLE ADVISOR on the editorial board of the book in this repository (Edition {edition}).
TARGET: {task}

Read ./SYSTEM_PROMPT.md, ./state/continuation_prompt.md, ./state/style_bible.md, ./book_src/{target_file} (if it exists), {chapter_brief} (the chapter's founding brief, if it exists), and any relevant files in ./state/research/.

Your priority is RESEARCH: web searches for the latest dated, sourced trend data, papers, rulings, and deal facts, plus shelf pages via `python3 tools/pdf_search.py`. Then strategize and dissect. Do NOT write book prose and do NOT run code. Write {brief_path} containing:
1. The one-sentence thesis and the "aha" reframing for an ex-PJT-RSSG reader.
2. An outline for 3,000–5,000 NEW words that does not duplicate what the chapter already covers, with at least one Trend Watch box.
3. Derivation skeletons with final LaTeX formulas, assumptions, measure (P vs Q), and error-prone spots.
4. A code spec and the sanity check that would prove the code right.
5. 3–8 source pages (book_id p.N), each with the exact short quotation to use.
6. A research dossier of dated, sourced facts, each with a URL or citation. Mark unconfirmed ones CHECK. Never invent CUSIPs, URLs, or episode numbers.
7. 5–10 jokes, analogies, or running-gag beats that each teach a correct idea, in the style bible's voice and cast.
8. Resource-graph candidates flagged VERIFIED-URL or TITLE-ONLY.
9. Two follow-up expansion targets ("FILE.md: description") and any new TOC chapters the research justifies.
Modify no other files except new research notes in ./state/research/.

{DURABILITY}"""


def writer_prompt(iteration, edition, task, target_file, briefs):
    brief_list = ", ".join(briefs) if briefs else "(none found)"
    return f"""EDITION {edition}, ITERATION #{iteration}
CURRENT TARGET: {task}

INSTRUCTIONS FOR THIS TURN (research and writing first; do not spend turns running or debugging code examples):
1. Read ./SYSTEM_PROMPT.md, ./state/continuation_prompt.md, ./state/style_bible.md, ./state/book_state.json, and the Fable advisor brief(s): {brief_list}.
2. Research: do web searches wherever the brief is thin, especially for fresh, dated trend data. Use `python3 tools/pdf_search.py` to find shelf pages and quote them briefly in `> **[SOURCE EXTRACTION]**` blocks with book_id p.N citations, annotated in depth.
3. Write at least 3,000–5,000 words of new, dense, rigorous, and entertaining content into ./book_src/{target_file}: LaTeX derivations, Trend Watch boxes, a `### Specification for AI Implementation` block with carefully written Python, a deep case study, and a `### Deep-Dive Resource Graph`. Expand; never delete valid content. If the chapter would exceed 15,000 words, continue in a new file that sorts right after it (e.g. NN_chNNb_...md).
4. If your research shows the TOC is missing a chapter or section, add it to SYSTEM_PROMPT.md section 3 (growth rule) and queue it.
5. Run `BUILD_PDF=0 ./build_book.sh`; it must succeed.
6. Update ./state/book_state.json: remove the completed task from the front of `expansion_queue`, append it to `completed_modules`, record new case studies under `case_studies`, and append 2 new granular sub-topics ("FILE.md: description") to the end of `expansion_queue`. Leave `edition`, `iteration`, `last_build_timestamp`, `chapters`, and `attempts` alone; the orchestrator owns them.

{DURABILITY}"""


# ------------------------------------------------------------- iteration ---

def lint_file(target_file):
    path = os.path.join("book_src", target_file)
    if not os.path.exists(path):
        return None
    proc = subprocess.run(
        [sys.executable, "tools/check_book.py", "--file", path, "--run-code", "--json"],
        capture_output=True, text=True, check=False,
    )
    try:
        return json.loads(proc.stdout)[0]
    except (json.JSONDecodeError, IndexError):
        return {"file": target_file, "code": {"ok": False, "tail": proc.stderr[-800:]}}


def git_commit(message):
    if os.environ.get("AUTO_COMMIT") != "1":
        return
    subprocess.run(["git", "add", "-A", "book_src", "state", "output", "SYSTEM_PROMPT.md", "CHANGELOG.md"], check=False)
    subprocess.run(["git", "commit", "-q", "-m", message], check=False)
    if os.environ.get("AUTO_PUSH") == "1":
        branch = subprocess.run(["git", "branch", "--show-current"], capture_output=True, text=True).stdout.strip()
        for delay in (0, 2, 4, 8, 16):
            time.sleep(delay)
            if subprocess.run(["git", "push", "-u", "origin", branch], check=False).returncode == 0:
                break


def plan_next_edition():
    state = load_state()
    edition = state.get("edition", 1)
    shutil.copyfile(STATE_FILE, STATE_BACKUP)
    print(f"\n[{now()}] Edition {edition} complete: convening the Fable edition planner.")
    rebuild_book(state)  # ship the finished edition before planning the next
    git_commit(f"Ship Edition {edition} of the book")
    run_agent(edition_planner_prompt(edition), model=ADVISOR_MODEL, label="fable-planner")
    state = reload_state_or_restore()
    if state.get("edition", edition) == edition:  # planner forgot; keep the loop moving anyway
        state["edition"] = edition + 1
    if not state["expansion_queue"]:
        counts = {k: v for k, v in word_counts().items() if re.match(r"^\d\d_ch\d\d", k)}
        state["expansion_queue"] = [
            f"{f}: Edition {state['edition']} research-driven expansion: fresh trend data, a new case study, deeper derivations"
            for f in sorted(counts, key=counts.get)
        ]
    save_state(state)
    git_commit(f"Plan Edition {state['edition']}")


def run_agent_iteration():
    state = load_state()
    if not state["expansion_queue"]:
        plan_next_edition()
        state = load_state()
    edition = state.get("edition", 1)
    iteration = state["iteration"] + 1
    task = state["expansion_queue"][0]
    m = TARGET_RE.match(task)
    target_file = m.group(1) if m else "99_appZ_new_material.md"
    stem = target_file[:-3]
    words_before = word_counts().get(target_file, 0)
    shutil.copyfile(STATE_FILE, STATE_BACKUP)
    print(f"\n[{now()}] Edition {edition}, iteration #{iteration}: {task[:160]}")

    # Pass 1: the Fable advisor researches and dissects the target.
    brief_path = os.path.join(BRIEF_DIR, f"{stem}__it{iteration:04d}.md")
    run_agent(advisor_prompt(task, target_file, stem, brief_path, edition), model=ADVISOR_MODEL, label="fable-advisor")
    briefs = [p for p in (os.path.join(BRIEF_DIR, f"{stem}.md"), brief_path) if os.path.exists(p)]

    # Pass 2: the writer researches further and expands the book.
    rc = run_agent(writer_prompt(iteration, edition, task, target_file, briefs), model=WRITER_MODEL, label="writer")

    state = reload_state_or_restore()
    counts = word_counts()
    gained = counts.get(target_file, 0) - words_before
    state["iteration"] = iteration
    state["chapters"] = counts
    attempts = state.setdefault("attempts", {})
    if gained < MIN_WORD_GAIN and state["expansion_queue"] and state["expansion_queue"][0] == task:
        attempts[task] = attempts.get(task, 0) + 1
        if attempts[task] >= 2:  # stuck: rotate it to the back so the loop keeps moving
            state["expansion_queue"].append(state["expansion_queue"].pop(0))
            attempts.pop(task)

    code_ok = None
    if os.environ.get("RUN_CODE_CHECKS") == "1":  # lowest priority: fixes go to the END of the queue
        lint = lint_file(target_file)
        code_ok = bool(lint and lint.get("code", {}).get("ok", True))
        fix = f"{target_file}: FIX the chapter's Python so `tools/check_book.py --run-code` passes"
        if lint and not code_ok and not any(t.startswith(fix) for t in state["expansion_queue"]):
            state["expansion_queue"].append(f"{fix}. Last error: {lint['code']['tail'][-400:]}")
    save_state(state)

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps({
            "edition": edition, "iteration": iteration, "time": now(), "task": task, "writer_rc": rc,
            "words_gained": gained, "total_words": sum(counts.values()), "code_ok": code_ok,
        }) + "\n")
    print(f"[{now()}] Iteration #{iteration} done: +{gained} words in {target_file}; "
          f"book total {sum(counts.values()):,} words.")
    git_commit(f"Edition {edition}, iteration #{iteration}: {task[:120]}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--once", action="store_true", help="run a single iteration")
    ap.add_argument("--build-only", action="store_true", help="compile the book and exit")
    ap.add_argument("--plan-edition", action="store_true", help="close this edition and plan the next")
    args = ap.parse_args()

    signal.signal(signal.SIGINT, _request_stop)
    signal.signal(signal.SIGTERM, _request_stop)
    ensure_workspace()

    if args.build_only:
        rebuild_book(load_state())
        return
    if args.plan_edition:
        plan_next_edition()
        return
    maybe_rebuild_book()  # first run builds immediately (timestamp 0); restarts respect the 6-hour clock
    while not _stop:
        run_agent_iteration()
        maybe_rebuild_book()
        if args.once:
            break
        time.sleep(5)


if __name__ == "__main__":
    main()
