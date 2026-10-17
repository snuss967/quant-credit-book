#!/usr/bin/env python3
"""Lint book chapters for the mandatory anatomy and run their Python.

    python3 tools/check_book.py                      # lint every chapter in book_src/
    python3 tools/check_book.py --file book_src/04_ch04_merton_and_intensity_models.md --run-code
    python3 tools/check_book.py --run-code --json    # machine-readable (used by orchestrator.py)

Code convention: all ```python blocks in a chapter are executed *cumulatively, in order*
in one fresh interpreter (like a notebook), so later blocks may use earlier definitions.
A block whose first line is `# sketch` is skipped (interface sketches, pseudo-code).
"""
import argparse
import glob
import json
import os
import re
import subprocess
import sys
import tempfile

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
CHAPTER_RE = re.compile(r"^\d\d_ch\d\d")

ANATOMY = {
    "math": re.compile(r"\$\$"),
    "ai_spec": re.compile(r"^#{2,4} .*Specification for AI Implementation", re.M),
    "source_extraction": re.compile(r"\[SOURCE EXTRACTION\]"),
    "case_study": re.compile(r"^#{2,4} .*Case Study", re.M | re.I),
    "resource_graph": re.compile(r"^#{2,4} .*Deep-Dive Resource Graph", re.M),
}
FENCE_RE = re.compile(r"^```(\w[\w+-]*)?\s*$")


def python_blocks(text):
    blocks, lang, buf = [], None, None
    for line in text.splitlines():
        m = FENCE_RE.match(line.strip()) if line.lstrip().startswith("```") else None
        if buf is None and m:
            lang, buf = (m.group(1) or "").lower(), []
        elif buf is not None and line.strip() == "```":
            if lang == "python" and not (buf and buf[0].strip().lower().startswith("# sketch")):
                blocks.append("\n".join(buf))
            lang, buf = None, None
        elif buf is not None:
            buf.append(line)
    return blocks


def strip_code(text):
    out, in_code = [], False
    for line in text.splitlines():
        if line.lstrip().startswith("```"):
            in_code = not in_code
            continue
        if not in_code:
            out.append(line)
    return "\n".join(out)


def lint(path, run_code, timeout):
    text = open(path, encoding="utf-8").read()
    prose = strip_code(text)
    name = os.path.basename(path)
    report = {"file": name, "words": len(text.split()), "missing": [], "warnings": [], "code": None}

    if CHAPTER_RE.match(name):
        report["missing"] = [k for k, rx in ANATOMY.items() if not rx.search(text)]

    lines = prose.splitlines()
    for i, line in enumerate(lines[:-1]):
        if line.strip() == "---" and lines[i + 1].strip():
            report["warnings"].append(f"line ~{i + 1}: '---' followed by text (YAML/setext trap); add a blank line")
    if prose.count("$$") % 2:
        report["warnings"].append("odd number of $$ display-math delimiters")
    for m in re.finditer(r"(?<![\\$])\$\d[\d,.]*\s*(million|billion|bn|mm|k)\b", prose, re.I):
        report["warnings"].append(f"unescaped currency '{m.group(0)}' (write \\$ outside math)")
        break
    if re.search(r"\]\(\s*\)", prose):
        report["warnings"].append("empty link target ()")

    if run_code:
        blocks = python_blocks(text)
        if blocks:
            with tempfile.TemporaryDirectory() as tmp:
                script = os.path.join(tmp, "chapter_code.py")
                with open(script, "w", encoding="utf-8") as f:
                    f.write("\n\n".join(f"# ---- block {i + 1} ----\n{b}" for i, b in enumerate(blocks)))
                try:
                    proc = subprocess.run(
                        [sys.executable, script], cwd=tmp, capture_output=True, text=True, timeout=timeout,
                        env={**os.environ, "MPLBACKEND": "Agg"},
                    )
                    ok = proc.returncode == 0
                    tail = (proc.stderr if not ok else proc.stdout)[-1500:]
                except subprocess.TimeoutExpired:
                    ok, tail = False, f"timeout after {timeout}s"
            report["code"] = {"blocks": len(blocks), "ok": ok, "tail": tail}
        else:
            report["code"] = {"blocks": 0, "ok": True, "tail": ""}
    return report


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--file", action="append", help="chapter file(s); default all of book_src/")
    ap.add_argument("--run-code", action="store_true")
    ap.add_argument("--timeout", type=int, default=600)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    files = args.file or sorted(glob.glob(os.path.join(ROOT, "book_src", "*.md")))
    reports = [lint(f, args.run_code, args.timeout) for f in files]

    if args.json:
        print(json.dumps(reports, indent=2))
    else:
        for r in reports:
            code = ""
            if r["code"] is not None:
                code = f"  code: {r['code']['blocks']} blocks {'OK' if r['code']['ok'] else 'FAILED'}"
            flag = "OK " if not r["missing"] and not (r["code"] and not r["code"]["ok"]) else "!! "
            print(f"{flag}{r['file']:<58} {r['words']:>7} words{code}")
            for m in r["missing"]:
                print(f"     missing anatomy: {m}")
            for w in r["warnings"]:
                print(f"     warning: {w}")
            if r["code"] and not r["code"]["ok"]:
                print("     " + r["code"]["tail"].replace("\n", "\n     "))
        total = sum(r["words"] for r in reports)
        print(f"\n{len(reports)} files, {total:,} words")
    failed = any(r["code"] and not r["code"]["ok"] for r in reports)
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
