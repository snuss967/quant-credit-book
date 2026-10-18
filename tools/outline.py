#!/usr/bin/env python3
"""Compact digests of many Markdown files: cheap global context for agents.

    python3 tools/outline.py book_src/*.md                      # every heading of the book
    python3 tools/outline.py state/advisor_briefs/[0-9]*.md \\
        --full "thesis|outline|case stud" --max-words 900        # those sections in full, other headings only
    python3 tools/outline.py book_src/*.md --out state/digests/book_outline.md

A section (a `##` heading and everything under it) is printed in full when its heading matches
the --full regex (case-insensitive), truncated to --max-words. Every other heading is listed
so the reader still sees the file's shape.
"""
import argparse
import glob
import os
import re

HEADING = re.compile(r"^(#{1,4})\s+(.*)")


def digest(path, full_rx, max_words, intro=0):
    lines = open(path, encoding="utf-8").read().splitlines()
    out, in_code, keep, kept_words = [f"\n==== {os.path.basename(path)} ({sum(len(l.split()) for l in lines):,} words)"], False, False, 0
    keep, kept_words = (True, max_words - intro) if intro else (False, 0)  # keep the opening (cold open) up to `intro` words
    for line in lines:
        if line.lstrip().startswith("```"):
            in_code = not in_code
            if keep and kept_words < max_words:
                out.append(line)
            continue
        m = HEADING.match(line) if not in_code else None
        if m:
            level = len(m.group(1))
            if level <= 2:
                keep = bool(full_rx and full_rx.search(m.group(2)))
                kept_words = 0
            out.append(line)
            continue
        if keep and kept_words < max_words and line.strip():
            out.append(line)
            kept_words += len(line.split())
            if kept_words >= max_words:
                out.append("  [...truncated]")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="+")
    ap.add_argument("--full", help="regex of ##-level headings to include in full")
    ap.add_argument("--max-words", type=int, default=600)
    ap.add_argument("--out")
    ap.add_argument("--intro", type=int, default=0, help="also keep the first N words before the first ## heading")
    args = ap.parse_args()
    full_rx = re.compile(args.full, re.I) if args.full else None
    files = sorted({p for pat in args.paths for p in glob.glob(pat)})
    text = "\n".join(digest(p, full_rx, args.max_words, args.intro) for p in files)
    if args.out:
        os.makedirs(os.path.dirname(args.out), exist_ok=True)
        open(args.out, "w", encoding="utf-8").write(text + "\n")
        print(f"wrote {args.out}: {len(files)} files, {len(text.split()):,} words")
    else:
        print(text)


if __name__ == "__main__":
    main()
