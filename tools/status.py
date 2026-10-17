#!/usr/bin/env python3
"""What is done, what is partial, what is missing: the source of truth for restarts.

Every agent ends its output file with a completion marker line:
    <!-- STATUS: COMPLETE -->
A file without the marker is PARTIAL: the agent died mid-write, and the next agent must
resume it rather than start over. A file that does not exist is MISSING.

    python3 tools/status.py                 # human-readable table
    python3 tools/status.py --json          # machine-readable (used to build workflow args)
    python3 tools/status.py --mark FILE...  # append the marker to files verified complete by hand
"""
import argparse
import glob
import json
import os
import re

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
MARKER = "<!-- STATUS: COMPLETE -->"
TOC_RE = re.compile(r"- \*\*Ch (\d+[A-Za-z]?) `(\w+)`: (.+?)\*\*")


def status(path):
    if not os.path.exists(path):
        return "MISSING", 0
    text = open(path, encoding="utf-8").read()
    words = len(text.split())
    return ("COMPLETE" if MARKER in text[-400:] else "PARTIAL"), words


def toc_chapters():
    text = open(os.path.join(ROOT, "SYSTEM_PROMPT.md"), encoding="utf-8").read()
    return [{"n": m.group(1), "stem": m.group(2), "title": m.group(3).rstrip(".")} for m in TOC_RE.finditer(text)]


def scan():
    chapters = []
    for ch in toc_chapters():
        b, bw = status(os.path.join(ROOT, "state/advisor_briefs", f"{ch['stem']}.md"))
        c, cw = status(os.path.join(ROOT, "book_src", f"{ch['stem']}.md"))
        chapters.append({**ch, "brief": b, "brief_words": bw, "chapter": c, "chapter_words": cw})
    research = []
    for p in sorted(glob.glob(os.path.join(ROOT, "state/research/*.md"))):
        s, w = status(p)
        research.append({"file": os.path.basename(p), "status": s, "words": w})
    other = []
    for p in sorted(glob.glob(os.path.join(ROOT, "book_src/*.md"))):
        name = os.path.basename(p)
        if not re.match(r"^\d\d_ch\d\d", name):
            s, w = status(p)
            other.append({"file": name, "status": s, "words": w})
    return {"chapters": chapters, "research": research, "front_and_back_matter": other}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--mark", nargs="+", metavar="FILE")
    args = ap.parse_args()
    if args.mark:
        for p in args.mark:
            text = open(p, encoding="utf-8").read()
            if MARKER not in text[-400:]:
                with open(p, "a", encoding="utf-8") as f:
                    f.write(("" if text.endswith("\n") else "\n") + "\n" + MARKER + "\n")
                print(f"marked {p}")
        return
    s = scan()
    if args.json:
        print(json.dumps(s, indent=1))
        return
    print(f"{'Ch':>4}  {'brief':<9} {'words':>6}   {'chapter':<9} {'words':>6}  stem")
    for c in s["chapters"]:
        print(f"{c['n']:>4}  {c['brief']:<9} {c['brief_words']:>6}   {c['chapter']:<9} {c['chapter_words']:>6}  {c['stem']}")
    for group in ("front_and_back_matter", "research"):
        print(f"\n{group}:")
        for r in s[group]:
            print(f"  {r['status']:<9} {r['words']:>6}  {r['file']}")
    done = sum(c["chapter"] == "COMPLETE" for c in s["chapters"])
    print(f"\nchapters complete: {done}/{len(s['chapters'])}; briefs complete: "
          f"{sum(c['brief'] == 'COMPLETE' for c in s['chapters'])}/{len(s['chapters'])}")


if __name__ == "__main__":
    main()
