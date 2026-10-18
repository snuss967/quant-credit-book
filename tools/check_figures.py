#!/usr/bin/env python3
"""Warn about figure embeds whose PNG does not exist (a writer referenced a figure no one has drawn yet)."""
import glob, os, re, sys

missing = []
for f in sorted(glob.glob("book_src/*.md")):
    for m in re.finditer(r"!\[[^\]]*\]\((assets/figures/[^)\s]+)\)", open(f, encoding="utf-8").read()):
        if not os.path.exists(m.group(1)):
            missing.append((os.path.basename(f), m.group(1)))
for f, p in missing:
    print(f"check_figures: {f} embeds {p}, which does not exist", file=sys.stderr)
print(f"check_figures: {len(missing)} missing figure file(s)")
