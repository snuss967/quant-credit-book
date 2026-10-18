#!/usr/bin/env python3
"""Measure how prescriptive vs narrative a chapter reads (user verdict on Edition 1: "a lot of
prescriptiveness and not narrative"). Rough, but comparable across chapters and revisions.

    python3 tools/prescriptiveness.py book_src/01_ch01_*.md            # current text
    python3 tools/prescriptiveness.py --pre 9ac1c37 book_src/01_ch01_*.md   # also the text at a commit

Metrics per 1,000 words of prose (code fences, math blocks, and tables excluded):
  bullets%   share of prose words that sit in bullet or numbered-list lines
  modal      should/must/never/always/need to/have to/make sure/do not/don't
  imper      sentences that open with a bare imperative verb (Use, Compute, Check, ...)
  rule       "rule", "law", "lesson", "takeaway", "the point is", "remember"
  dialog     quoted speech marks (scene density)
  boxes      Math, Gently / View From Another Seat boxes (absolute counts)
"""
import argparse, re, subprocess, sys

IMPER = r"(Use|Compute|Check|Run|Treat|Build|Keep|Avoid|Prefer|Start|Never|Always|Do|Don't|Remember|Note|Make|Read|Write|Ask|Stop|Think|Assume|Set|Add|Put|Take|Measure|Estimate|Watch|Know|Trust|Hedge|Price|Sell|Buy|Cut)"
MODAL = re.compile(r"\b(should|must|never|always|need to|needs to|have to|has to|make sure|do not|don't|cannot afford)\b", re.I)
RULE = re.compile(r"\b(rule|rules|law|laws|lesson|lessons|takeaway|takeaways|the point is|remember)\b", re.I)
SENT_IMPER = re.compile(r"(?:^|[.!?]\s+|^\s*[-*]\s+|^\s*\d+\.\s+)" + IMPER + r"\b")
DIALOG = re.compile(r"[\"“][^\"”]{3,200}[\"”]")


def prose(text):
    out, in_code, in_math = [], False, False
    for line in text.split("\n"):
        s = line.strip()
        if s.startswith("```"):
            in_code = not in_code
            continue
        if s == "$$":
            in_math = not in_math
            continue
        if in_code or in_math or s.startswith("|") or s.startswith("<!--") or (s.startswith("$$") and s.endswith("$$")):
            continue
        out.append(line)
    return out


def metrics(text):
    lines = prose(text)
    words = sum(len(l.split()) for l in lines) or 1
    bullet_words = sum(len(l.split()) for l in lines if re.match(r"^\s*(?:[-*+]|\d+\.)\s+", l))
    body = "\n".join(lines)
    k = 1000.0 / words
    return {
        "words": words,
        "bullets%": round(100.0 * bullet_words / words, 1),
        "modal": round(len(MODAL.findall(body)) * k, 1),
        "imper": round(sum(len(SENT_IMPER.findall(l)) for l in lines) * k, 1),
        "rule": round(len(RULE.findall(body)) * k, 1),
        "dialog": round(len(DIALOG.findall(body)) * k, 1),
        "mathgently": body.count("Math, Gently"),
        "seat": body.count("View From Another Seat"),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="+")
    ap.add_argument("--pre", help="git commit to compare against")
    a = ap.parse_args()
    cols = ["words", "bullets%", "modal", "imper", "rule", "dialog", "mathgently", "seat"]
    print(f"{'file':<58} {'ver':<4} " + " ".join(f"{c:>10}" for c in cols))
    for f in a.files:
        rows = []
        if a.pre:
            try:
                old = subprocess.run(["git", "show", f"{a.pre}:{f}"], capture_output=True, text=True, check=True).stdout
                rows.append(("pre", metrics(old)))
            except subprocess.CalledProcessError:
                pass
        rows.append(("now", metrics(open(f, encoding="utf-8").read())))
        for tag, m in rows:
            print(f"{f.split('/')[-1][:58]:<58} {tag:<4} " + " ".join(f"{m[c]:>10}" for c in cols))


if __name__ == "__main__":
    sys.exit(main())
