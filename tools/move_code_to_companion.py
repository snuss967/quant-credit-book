#!/usr/bin/env python3
"""Move every code listing out of the chapters into Appendix F (the Code Companion).

Each fenced code block (python, cpp, rust, sql, bash, json, ...) in a chapter or appendix is
moved, in order, to book_src/95_appF_code_companion.md as "Listing N.k". In the chapter it is
replaced by a short linked stub. Later editions expand the stub into a plain-language explanation
of what the code does and why. `text` fences stay in place: they are diagrams and box layouts.
Idempotent: files whose code has already moved hold no movable fences.
"""
import glob, os, re, sys

MOVE = {"python", "py", "cpp", "c++", "c", "rust", "sql", "bash", "sh", "json", "yaml", "javascript", "js"}
FENCE = re.compile(r"^```\s*([\w+-]*)\s*$")
MARK = "<!-- STATUS: COMPLETE -->"
OUT = "book_src/95_appF_code_companion.md"


def label_for(files):
    m = re.match(r"(\d\d)_ch(\d\d)([a-z]?)_", files)
    if m:
        return str(int(m.group(2))) + (m.group(3).upper() and "-" + m.group(3).upper())
    m = re.match(r"9\d_app([A-Z])_", files)
    return m.group(1) if m else None


def describe(code):
    doc = re.search(r'"""(.*?)"""', code, re.S)
    if doc:
        first = " ".join(doc.group(1).split())
        return first.split(". ")[0].rstrip(".")[:180]
    for line in code.splitlines():
        s = line.strip()
        if s.startswith(("#", "//")) and len(s.lstrip("#/ ").strip()) > 8 and not s.lower().startswith(("# sketch", "#!/")):
            return s.lstrip("#/ ").strip()[:180]
    names = re.findall(r"^(?:def|class|fn|struct)\s+(\w+)", code, re.M)
    return ("Defines " + ", ".join(names[:4])) if names else "Reference implementation"


def title_of(path):
    for line in open(path, encoding="utf-8"):
        if line.startswith("# "):
            return line[2:].strip()
    return os.path.basename(path)


def main():
    apply = "--apply" in sys.argv
    files = sorted(p for p in glob.glob("book_src/*.md") if label_for(os.path.basename(p)) and not p.endswith("95_appF_code_companion.md"))
    existing = open(OUT, encoding="utf-8").read() if os.path.exists(OUT) else ""
    companion, moved_total = [], 0
    for path in files:
        lab = label_for(os.path.basename(path))
        lines = open(path, encoding="utf-8").read().split("\n")
        prior = [int(x) for x in re.findall(rf"### Listing {re.escape(lab)}\.(\d+):", existing)]
        out, i, k, listings = [], 0, max(prior, default=0), []
        while i < len(lines):
            m = FENCE.match(lines[i].strip()) if lines[i].lstrip().startswith("```") else None
            if m and m.group(1).lower() in MOVE:
                lang = m.group(1).lower()
                j = i + 1
                while j < len(lines) and lines[j].strip() != "```":
                    j += 1
                code = "\n".join(lines[i + 1:j])
                k += 1
                anchor = f"code-{lab.lower().replace('-', '')}-{k}"
                desc = describe(code)
                listings.append((k, anchor, lang, code, desc))
                out.append(f"<!-- EXPLAIN: Listing {lab}.{k} -->\n> **Code Companion: Listing {lab}.{k}.** {desc}. The full {lang} listing is in [Appendix F, Listing {lab}.{k}](#{anchor}).")
                i = j + 1
                continue
            out.append(lines[i])
            i += 1
        if listings:
            moved_total += len(listings)
            cont = f"## F.{lab}:" in existing
            companion.append(f"\n## F.{lab}{' (continued)' if cont else ''}: {title_of(path)}{'' if cont else ' {#code-' + lab.lower().replace('-', '') + '}'}\n")
            companion.append(f"Listings from `{os.path.basename(path)}`, in the order they appear in the chapter. Blocks within a chapter are written to run cumulatively in one interpreter.\n")
            for k, anchor, lang, code, desc in listings:
                companion.append(f"\n### Listing {lab}.{k}: {desc} {{#{anchor}}}\n\n```{lang}\n{code}\n```\n")
            if apply:
                open(path, "w", encoding="utf-8").write("\n".join(out))
        print(f"{os.path.basename(path):<62} listings moved: {len(listings)}")
    if apply and companion and existing:
        body = existing.replace(MARK, "").rstrip() + "\n" + "\n".join(companion) + "\n\n" + MARK + "\n"
        open(OUT, "w", encoding="utf-8").write(body)
    elif apply and companion:
        head = ("# Appendix F: The Code Companion\n\n"
                "Every reference implementation in the book lives here, chapter by chapter. The chapters explain what each listing does, why it is built that way, and when to use it; this appendix holds the code itself so the story is never interrupted by a wall of syntax. "
                "Listings within a chapter build on each other: run them in order in one interpreter (`python3 tools/check_book.py --file book_src/95_appF_code_companion.md --run-code` runs them all).\n")
        open(OUT, "w", encoding="utf-8").write(head + "\n".join(companion) + "\n\n" + MARK + "\n")
    print(f"TOTAL listings: {moved_total} ({'applied' if apply else 'dry run'})")


if __name__ == "__main__":
    main()
