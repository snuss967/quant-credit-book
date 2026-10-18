"""Assemble Appendix Z from the per-chapter solution files in state/appZ/.

Order follows book_src/ (the TOC order). Part headings come from the book's part files, and an
optional Part gate (state/appZ/gates/<part file stem>.md) follows each Part's chapters. Editor
NOTEs (lines that contain "NOTE (for the editor)") are kept out of the book and listed in
state/appZ/_editor_notes.md for the cleanup pass.

    python3 tools/assemble_appZ.py            # writes book_src/99_appZ_solutions_hints_and_self_assessment.md
"""
import os
import re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SRC = os.path.join(ROOT, "book_src")
ZDIR = os.path.join(ROOT, "state", "appZ")
OUT = os.path.join(SRC, "99_appZ_solutions_hints_and_self_assessment.md")
OUT_B = os.path.join(SRC, "99_appZb_solutions_parts_v_to_viii.md")
SPLIT_AT = "18_00_part_V"   # the spec splits App Z when it passes 15k words; Parts V-VIII go to App Zb
INTRO_B = """# Appendix Z (continued): Solutions for Parts V to VIII

The second half of Appendix Z, in the same form: the number first, then the method, then the trap,
and the section to reread.
"""
MARK = "<!-- STATUS: COMPLETE -->"

INTRO = """# Appendix Z: Solutions, Hints and the Gates

Every exercise in the book has its worked answer here. Each solution gives the number first, then
the method, then the trap most readers fall into, and ends with the section to reread if you missed
it. A solution states its measure (physical or risk-neutral) and its units whenever either could be
in doubt. Code appears only where the exercise asks you to build something, and then only as far as
the answer needs; the full listings live in Appendix F.

The appendix is arranged in book order, Part by Part. Where a Part has a gate, it comes after that
Part's chapters: a short self-assessment you can take before moving on, with the answers and the
sections to reread.
"""


def strip_status(text):
    return "\n".join(l for l in text.splitlines() if l.strip() != MARK).strip() + "\n"


def split_notes(text):
    keep, notes = [], []
    for para in re.split(r"\n\s*\n", text):
        (notes if "NOTE (for the editor)" in para else keep).append(para)
    return "\n\n".join(keep).strip() + "\n", notes


def main():
    stems = sorted(f[:-3] for f in os.listdir(SRC) if f.endswith(".md"))
    parts, out, all_notes, missing = [], [INTRO], [], []
    out_b = None
    current_part = None
    for stem in stems:
        if stem[:2] in ("95", "96", "97", "98", "99"):
            continue
        if stem[:2] in ("90", "91", "92", "93", "94") and current_part != "appendices":
            if not os.path.exists(os.path.join(ZDIR, stem + ".md")):
                continue
            out.append(gate(current_part))
            out.append("## The Appendices\n")
            current_part = "appendices"
        if "_00_part_" in stem:
            if current_part:
                out.append(gate(current_part))
            if stem == SPLIT_AT:
                out_b, out = out, [INTRO_B]
            with open(os.path.join(SRC, stem + ".md")) as fh:
                title = next((l for l in fh if l.startswith("# ")), "# " + stem)[2:].strip()
            out.append(f"## {title}\n")
            current_part = stem
            parts.append(stem)
            continue
        zpath = os.path.join(ZDIR, stem + ".md")
        if not os.path.exists(zpath):
            if current_part or stem.startswith("00_02"):
                missing.append(stem)
            continue
        with open(zpath) as fh:
            body, notes = split_notes(strip_status(fh.read()))
        # chapter sections are "## Z.NN ..." in the source; demote one level under the Part heading
        body = normalize(body)
        out.append(body)
        all_notes += [f"### {stem}\n\n{n}\n" for n in notes]
    if current_part:
        out.append(gate(current_part))
    first, second = (out_b, out) if out_b is not None else (out, None)
    for path, chunks in ((OUT, first), (OUT_B, second)):
        if chunks is None:
            continue
        with open(path, "w") as fh:
            fh.write("\n\n".join(c.strip() for c in chunks if c.strip()) + "\n")
        print(f"wrote {os.path.relpath(path, ROOT)}: {sum(len(c.split()) for c in chunks)} words")
    out = first + (second or [])
    with open(os.path.join(ZDIR, "_editor_notes.md"), "w") as fh:
        fh.write("# App Z editor notes (chapter-text discrepancies found while solving)\n\n" + "\n".join(all_notes))
    print(f"{len(all_notes)} editor notes -> state/appZ/_editor_notes.md")
    if missing:
        print("no solutions yet for: " + ", ".join(missing))


def normalize(body):
    """One heading scheme: '### Z.NN Chapter N: Title' for the chapter, a bold line for each exercise."""
    lines = body.splitlines()
    for i, l in enumerate(lines):
        m = re.match(r"^## (Z\.\S+ )?(Chapter|Primer|Appendix)\b(.*)$", l)
        if m and i < 3:
            tag = m.group(1)
            if not tag:
                n = re.match(r"\s*([0-9]+)(-[A-Z])?", m.group(3))
                tag = f"Z.{int(n.group(1)):02d}{n.group(2) or ''} " if n else ""
            lines[i] = f"### {tag}{m.group(2)}{m.group(3)}"
            continue
        m = re.match(r"^#{3,5} (Z\.\S+.*)$", l)
        if m:
            lines[i] = f"**{m.group(1).strip()}**"
            continue
        lines[i] = re.sub(r"^(#{2,4}) ", lambda h: "#" + h.group(1) + " ", l)
    return "\n".join(lines).strip() + "\n"


def gate(part_stem):
    p = os.path.join(ZDIR, "gates", part_stem + ".md")
    if not os.path.exists(p):
        return ""
    with open(p) as fh:
        return strip_status(fh.read())


if __name__ == "__main__":
    main()
