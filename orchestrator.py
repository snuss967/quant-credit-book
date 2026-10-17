# orchestrator.py
"""The infinite book factory: expand the book forever, recompile it every 6 hours.

Each iteration:
  1. Pick the target: expansion_queue[0], or (queue empty) the thinnest chapter.
  2. FABLE ADVISOR pass: a `claude` call on the advisor model strategizes and dissects
     the target and writes state/advisor_briefs/<stem>__itNNNN.md.
  3. WRITER pass: a `claude` call expands the chapter from SYSTEM_PROMPT.md, the style
     bible, and the advisor brief(s); it calls a Fable referee for the hardest math.
  4. Guard rails: restore book_state.json if the agent corrupted it, lint the chapter and
     execute its Python, recount words, log the iteration, queue a fix if code broke,
     optionally git commit/push.
  5. If 6 hours have passed since the last build, run ./build_book.sh.

Usage:
  python3 orchestrator.py                # run forever (Ctrl-C finishes the current step and exits)
  python3 orchestrator.py --once         # one iteration, then exit
  python3 orchestrator.py --build-only   # just compile the book

Environment:
  AGENT_CMD            agent CLI (default: claude)
  ADVISOR_MODEL        model for the advisor pass (default: claude-fable-5-1)
  WRITER_MODEL         model for the writer pass (default: the CLI's default)
  ITERATION_TIMEOUT_S  per-agent-call timeout in seconds (default: 5400)
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
TARGET_RE = re.compile(r"^\s*([\w.-]+\.md)\s*:\s*(.*)$", re.S)
MIN_WORD_GAIN = 500  # below this, the iteration counts as a failed attempt

AGENT_CMD = os.environ.get("AGENT_CMD", "claude")
ADVISOR_MODEL = os.environ.get("ADVISOR_MODEL", "claude-fable-5-1")
WRITER_MODEL = os.environ.get("WRITER_MODEL") or None
ITERATION_TIMEOUT_S = int(os.environ.get("ITERATION_TIMEOUT_S", "5400"))

INITIAL_STATE = {
    "iteration": 0,
    "last_build_timestamp": 0,
    "completed_modules": [],
    "case_studies": [],
    "chapters": {},
    "attempts": {},
    "expansion_queue": [
        "01_ch01_anthology_and_landscape.md: Compile opening anthology with cited excerpts from the shelf + map the modern quant credit ecosystem",
        "02_ch02_pjt_rssg_cognitive_bridge.md: Convert PJT RSSG restructuring expertise (LMTs, covenants, DIP mechanics) into state-space representations and adverse selection filters",
        "03_ch03_credit_probability_distributions.md: Derive jump-diffusion, skewed recovery Beta distributions, and tail-risk math for AI coding specifiers",
        "04_ch04_merton_and_intensity_models.md: Full stochastic calculus derivations of Merton, Black-Cox covenant barrier models, and Duffie-Singleton hazard rates with Python simulation engines",
        "06_ch06_isolating_ido_and_empirical_duration.md: Empirical Duration across BB/B/CCC, cross-asset beta stripping, and isolating pure IDO alpha",
        "08_ch08_codifying_lmt_game_theory.md: Serta, J.Crew, Incora, and Carvana case studies with quantitative Priming Risk Scores and prisoner's dilemma matrices",
        "11_ch11_otc_microstructure_and_avellaneda_stoikov.md: Adapt Avellaneda-Stoikov to OTC corporate bond quoting, TRACE parsing, and RFQ adverse selection",
        "12_ch12_portfolio_trading_pricing_engines.md: Portfolio Trading (PT) pricing engines",
        "13_ch13_credit_etf_creation_redemption_arb.md: HYG/JNK/LQD/BKLN creation-redemption arbitrage loops",
        "16_ch16_nlp_pacer_and_covenant_scraping.md: Legal AST parsing of indentures, SEC EDGAR 8-Ks, and PACER Rule 2019 filings",
        "17_ch17_system_architecture_and_asics.md: FPGA/ASIC tick-to-trade pipelines for cross-asset credit quoting and production system construction",
    ],
}

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


def ensure_workspace():
    os.makedirs("./state", exist_ok=True)
    os.makedirs("./book_src", exist_ok=True)
    os.makedirs(BRIEF_DIR, exist_ok=True)
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
    print(f"\n[{now()}] >>> REBUILDING MASTER BOOK...")
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


def pick_target(state):
    if state["expansion_queue"]:
        return state["expansion_queue"][0]
    counts = {k: v for k, v in word_counts().items() if re.match(r"^\d\d_ch\d\d", k)}
    thinnest = min(counts, key=counts.get) if counts else "99_appZ_new_material.md"
    return (
        f"{thinnest}: This is currently the thinnest chapter. Add a brand-new 4,000-word sub-chapter with a new "
        "historical distressed/quant case study, cited source extractions from ./state/pdf_pages/, production Python "
        "specs, and a rich resource graph of podcasts, blogs, and SSRN papers. Then add 3 new deep-dive topics to "
        "expansion_queue."
    )


def advisor_prompt(task, target_file, stem, brief_path):
    chapter_brief = os.path.join(BRIEF_DIR, f"{stem}.md")
    return f"""You are a FABLE ADVISOR on the editorial board of the book in this repository.
TARGET: {task}

Read ./SYSTEM_PROMPT.md, ./state/style_bible.md, ./book_src/{target_file} (if it exists), and {chapter_brief} (the chapter's founding brief, if it exists).

Do NOT write book prose. Strategize and dissect. Write {brief_path} containing:
1. The one-sentence thesis and the "aha" reframing for an ex-PJT-RSSG reader.
2. An outline for 3,000-5,000 NEW words that does not duplicate what the chapter already covers.
3. Derivation skeletons with final LaTeX formulas, assumptions, measure (P vs Q), and error-prone spots; verify closed forms numerically in a scratch directory and say which you verified.
4. Code spec: functions, data schema, numerical guards, and the sanity check that proves the code right.
5. 3-8 source pages (book_id p.N) located with `python3 tools/pdf_search.py`, one line each on why.
6. Case-study facts, each marked VERIFIED (with source) or CHECK. Never invent CUSIPs, URLs, or episode numbers.
7. 5-10 jokes, analogies, or running-gag beats that each teach a correct idea, in the style bible's voice and cast.
8. Resource-graph candidates flagged VERIFIED-URL or TITLE-ONLY.
9. Two follow-up expansion targets in the form "FILE.md: description".
Modify no other files."""


def writer_prompt(iteration, task, target_file, briefs):
    brief_list = ", ".join(briefs) if briefs else "(none found)"
    return f"""ITERATION #{iteration}
CURRENT TARGET: {task}

INSTRUCTIONS FOR THIS TURN:
1. Read ./SYSTEM_PROMPT.md, ./state/style_bible.md, ./state/book_state.json, and the Fable advisor brief(s): {brief_list}.
2. Locate relevant pages with `python3 tools/pdf_search.py` and quote them briefly in `> [SOURCE EXTRACTION]` blocks with book_id p.N citations, annotated in depth.
3. Write at least 3,000-5,000 words of new, dense, rigorous, and entertaining content into ./book_src/{target_file}: LaTeX derivations, a `### Specification for AI Implementation` block with runnable Python, a deep case study, and a `### Deep-Dive Resource Graph`. Expand; never delete valid content. If the chapter would exceed 15,000 words, continue in a new file that sorts right after it (e.g. NN_chNNb_...md).
4. For the hardest derivation you wrote, spawn a Fable referee (Agent tool, model "fable") to check the math and code; fix what it finds.
5. Run `python3 tools/check_book.py --file book_src/<each file you touched> --run-code` and `./build_book.sh`; both must pass.
6. Update ./state/book_state.json: remove the completed task from the front of `expansion_queue`, append it to `completed_modules`, record new case studies under `case_studies`, and append 2 new granular sub-topics ("FILE.md: description") to the end of `expansion_queue` so the book grows forever. Leave `iteration`, `last_build_timestamp`, `chapters`, and `attempts` alone; the orchestrator owns them."""


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


def git_commit(iteration, task):
    if os.environ.get("AUTO_COMMIT") != "1":
        return
    subprocess.run(["git", "add", "-A", "book_src", "state", "output"], check=False)
    msg = f"Book iteration #{iteration}: {task[:120]}"
    subprocess.run(["git", "commit", "-q", "-m", msg], check=False)
    if os.environ.get("AUTO_PUSH") == "1":
        branch = subprocess.run(["git", "branch", "--show-current"], capture_output=True, text=True).stdout.strip()
        for delay in (0, 2, 4, 8, 16):
            time.sleep(delay)
            if subprocess.run(["git", "push", "-u", "origin", branch], check=False).returncode == 0:
                break


def run_agent_iteration():
    state = load_state()
    iteration = state["iteration"] + 1
    task = pick_target(state)
    m = TARGET_RE.match(task)
    target_file = m.group(1) if m else "99_appZ_new_material.md"
    stem = target_file[:-3]
    words_before = word_counts().get(target_file, 0)
    shutil.copyfile(STATE_FILE, STATE_BACKUP)
    print(f"\n[{now()}] Iteration #{iteration}: {task[:160]}")

    # Pass 1: the Fable advisor dissects the target.
    brief_path = os.path.join(BRIEF_DIR, f"{stem}__it{iteration:04d}.md")
    run_agent(advisor_prompt(task, target_file, stem, brief_path), model=ADVISOR_MODEL, label="fable-advisor")
    briefs = [p for p in (os.path.join(BRIEF_DIR, f"{stem}.md"), brief_path) if os.path.exists(p)]

    # Pass 2: the writer expands the book.
    rc = run_agent(writer_prompt(iteration, task, target_file, briefs), model=WRITER_MODEL, label="writer")

    # Guard rails: the agent may have mangled the state file.
    try:
        state = load_state()
    except (json.JSONDecodeError, OSError):
        print(f"[{now()}] book_state.json corrupted by the agent; restoring backup.")
        shutil.copyfile(STATE_BACKUP, STATE_FILE)
        state = load_state()

    counts = word_counts()
    gained = counts.get(target_file, 0) - words_before
    lint = lint_file(target_file)
    code_ok = bool(lint and lint.get("code", {}).get("ok", True))

    state["iteration"] = iteration
    state["chapters"] = counts
    attempts = state.setdefault("attempts", {})
    is_fix = task.startswith(f"{target_file}: FIX")
    failed = gained < MIN_WORD_GAIN or (is_fix and not code_ok)
    if failed and state["expansion_queue"] and state["expansion_queue"][0] == task:
        attempts[task] = attempts.get(task, 0) + 1
        if attempts[task] >= 2:  # stuck: rotate it to the back so the loop keeps moving
            state["expansion_queue"].append(state["expansion_queue"].pop(0))
            attempts.pop(task)
    if lint and not code_ok:
        fix = f"{target_file}: FIX the chapter's Python so `tools/check_book.py --run-code` passes. Last error: {lint['code']['tail'][-400:]}"
        if not any(t.startswith(f"{target_file}: FIX") for t in state["expansion_queue"][:1]):
            state["expansion_queue"].insert(0, fix)
    save_state(state)

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps({
            "iteration": iteration, "time": now(), "task": task, "writer_rc": rc,
            "words_gained": gained, "total_words": sum(counts.values()),
            "code_ok": code_ok, "missing_anatomy": (lint or {}).get("missing"),
        }) + "\n")
    print(f"[{now()}] Iteration #{iteration} done: +{gained} words in {target_file}; code {'OK' if code_ok else 'FAILED'}; "
          f"book total {sum(counts.values()):,} words.")
    git_commit(iteration, task)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--once", action="store_true", help="run a single iteration")
    ap.add_argument("--build-only", action="store_true", help="compile the book and exit")
    args = ap.parse_args()

    signal.signal(signal.SIGINT, _request_stop)
    signal.signal(signal.SIGTERM, _request_stop)
    ensure_workspace()

    if args.build_only:
        rebuild_book(load_state())
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
