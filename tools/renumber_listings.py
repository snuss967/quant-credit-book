#!/usr/bin/env python3
"""Renumber the code listings of Appendix F in chapter order and keep every reference consistent.

Why: listings are numbered when they are first moved out of a chapter (tools/move_code_to_companion.py), so a
later pass that adds a listing in the middle of a chapter leaves the numbers out of order (Ch 1 read 1.1, 1.2,
1.4, 1.3), and the "continued" sections the mover appends sit at the end of the appendix.

What it does (dry run unless --apply):

  1. For each chapter file in book_src/, reads the order in which the chapter links to its own listings
     (the first `](#code-<chapter>-<k>)` link of each listing, outside code fences). That order defines the
     numbering: the first listing linked is N.1, the next N.2, and so on. A chapter's listings that it never
     links are numbered after the linked ones (in their old order) and reported.
  2. Rebuilds Appendix F: each chapter's listings are gathered into its main section ("## F.N: ... {#code-N}",
     any "(continued)" section is folded in and removed) in the new order, and every heading and anchor
     (`### Listing N.k: title {#code-N-k}`) is rewritten.
  3. Rewrites every reference to a renumbered listing, in one pass so a swap (1.3 <-> 1.4) cannot be applied
     twice: links and ids (`(#code-1-4)`, `{#code-1-4}`, always written in the canonical lower-case form, which
     also repairs mixed-case anchors such as #code-4D-1) and prose mentions (`Listing 1.4`, `Listings 11.3 and
     11.4`, `Listings 15.1-15.2`). Scanned: book_src/*.md, state/appZ/**/*.md (App Z is assembled from there by
     tools/assemble_appZ.py) and tools/figures/*.py (comments). Other roots can be given with --roots.
  4. Checks the result: every link resolves, no duplicate anchors, every listing is linked from its own
     chapter, and the numbers follow the chapter order.

Titles: `--titles` lists weak headings (auto-generated first lines such as "Eq", "Block 5", a truncated
"... (Sec", a bare formula, a file name) with the chapter heading each listing sits under, to help write a real
one. `--retitle titles.json` sets titles from a {"code-N-k": "Title"} map (keys are the anchors AFTER renumbering).

    python3 tools/renumber_listings.py                      # dry run: the plan and the checks
    python3 tools/renumber_listings.py --apply              # write the changes
    python3 tools/renumber_listings.py --check              # read-only consistency check, exit 1 on problems
    python3 tools/renumber_listings.py --titles             # weak titles with context
    python3 tools/renumber_listings.py --apply --retitle titles.json
    python3 tools/renumber_listings.py --root /tmp/copy_of_book   # rehearse on a copy

Idempotent: on a consistent book it changes nothing.
"""
import argparse
import glob
import json
import os
import re
import sys
import time

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SRC = os.path.join(ROOT, "book_src")
APPF = os.path.join(SRC, "95_appF_code_companion.md")
MARK = "<!-- STATUS: COMPLETE -->"
DEFAULT_ROOTS = ["book_src", "state/appZ", "tools/figures"]

SEC_RE = re.compile(r"^## F\.(?P<lab>[\w-]+?)(?P<cont> \(continued\))?: (?P<title>.*?)(?: \{#(?P<anchor>[\w-]+)\})?\s*$")
LST_RE = re.compile(r"^### Listing (?P<lab>[\w-]+)\.(?P<k>\d+): ?(?P<title>.*?)(?: \{#(?P<anchor>[\w-]+)\})?\s*$")
REF = r"(?:\d+(?:-[A-Z])?|[A-F])\.\d+"
SEP = r"(?:\s*,\s*and\s+|\s+and\s+|\s*(?:,|–|—|-|&)\s*|\s+(?:to|through)\s+)"
MENTION_RE = re.compile(rf"(?P<kw>\b[Ll]istings?\s+)(?P<refs>{REF}(?:{SEP}{REF})*)")
REF_RE = re.compile(rf"(?P<lab>\d+(?:-[A-Z])?|[A-F])\.(?P<k>\d+)")
ANCHOR_RE = re.compile(r"(?P<pre>\(#|\{#)code-(?P<key>[A-Za-z0-9]+)-(?P<k>\d+)(?P<post>\)|\})")
LINK_RE = re.compile(r"\]\(#(code-[A-Za-z0-9]+-\d+)\)")


def label_for(name):
    """Chapter label from a book_src file name: 04_ch04b_x.md -> '4-B'; 93_appD_x.md -> 'D'."""
    m = re.match(r"(\d\d)_ch(\d\d)([a-z]?)_", name)
    if m:
        return str(int(m.group(2))) + ("-" + m.group(3).upper() if m.group(3) else "")
    m = re.match(r"9\d_app([A-Z])_", name)
    return m.group(1) if m else None


def key_of(lab):
    return lab.lower().replace("-", "")


def anchor_of(lab, k):
    return f"code-{key_of(lab)}-{k}"


def split_fenced(text):
    """Yield (line, in_code) for each line; a fence line itself counts as code."""
    in_code = False
    for ln in text.split("\n"):
        if in_code:
            yield ln, True
            if ln.strip() == "```":
                in_code = False
        elif ln.lstrip().startswith("```"):
            in_code = True
            yield ln, True
        else:
            yield ln, False


# ---------------------------------------------------------------------------------------------- Appendix F model
class Block:
    def __init__(self, lab, k, title, anchor, header, body):
        self.lab, self.k, self.title, self.anchor, self.header, self.body = lab, k, title, anchor, header, body
        self.new_k = k
        self.moved = False
        self.orig = (k, title, anchor)


class Section:
    def __init__(self, lab, cont, header, title, anchor):
        self.lab, self.cont, self.header, self.title, self.anchor = lab, cont, header, title, anchor
        self.intro, self.blocks = [], []


def parse_appf(text):
    """Split Appendix F into (preamble lines, sections, trailer lines); serialize() is the exact inverse."""
    lines = text.split("\n")
    trailer = []
    marks = [i for i, ln in enumerate(lines) if ln.strip() == MARK]
    if marks:
        trailer, lines = lines[marks[-1]:], lines[:marks[-1]]
    pre, sections = [], []
    sec = blk = None
    in_fence = False
    for ln in lines:
        if in_fence:
            (blk.body if blk else sec.intro if sec else pre).append(ln)
            if ln.strip() == "```":
                in_fence = False
            continue
        if ln.lstrip().startswith("```"):
            in_fence = True
            (blk.body if blk else sec.intro if sec else pre).append(ln)
            continue
        m = SEC_RE.match(ln)
        if m:
            sec = Section(m["lab"], bool(m["cont"]), ln, m["title"], m["anchor"])
            sections.append(sec)
            blk = None
            continue
        m = LST_RE.match(ln)
        if m and sec is not None:
            blk = Block(m["lab"], int(m["k"]), m["title"], m["anchor"], ln, [])
            sec.blocks.append(blk)
            continue
        (blk.body if blk else sec.intro if sec else pre).append(ln)
    return pre, sections, trailer


def serialize(pre, sections, trailer):
    out = list(pre)
    for s in sections:
        out.append(s.header)
        out.extend(s.intro)
        for b in s.blocks:
            out.append(b.header)
            out.extend(b.body)
    return "\n".join(out + list(trailer))


def trailing_blanks(body):
    n = 0
    for ln in reversed(body):
        if ln.strip():
            break
        n += 1
    return n


def normalise_tail(body, blanks=2):
    body = list(body)
    while body and not body[-1].strip():
        body.pop()
    return body + [""] * blanks


# ---------------------------------------------------------------------------------------------- the plan
def chapter_link_order(path, lab):
    """Anchors (canonical) of this chapter's own listings, in order of first link outside code fences."""
    text = open(path, encoding="utf-8").read()
    want, seen, order = key_of(lab) + "-", set(), []
    for ln, in_code in split_fenced(text):
        if in_code:
            continue
        for m in LINK_RE.finditer(ln):
            a = m.group(1).lower()
            if a[5:].rsplit("-", 1)[0] + "-" == want and a not in seen:
                seen.add(a)
                order.append(a)
    return order


def build_plan(sections):
    """mapping {(lab, old_k): new_k}; plus notes for the report."""
    by_lab = {}
    for s in sections:
        for b in s.blocks:
            by_lab.setdefault(b.lab, []).append(b)
    notes, mapping = [], {}
    files = {label_for(os.path.basename(p)): p for p in sorted(glob.glob(os.path.join(SRC, "*.md")))
             if label_for(os.path.basename(p)) and not p.endswith("95_appF_code_companion.md")}
    for lab, blocks in by_lab.items():
        olds = {}
        for b in blocks:
            if b.k in olds:
                notes.append(f"ERROR duplicate Listing {lab}.{b.k} in Appendix F")
            olds[b.k] = b
        if lab not in files:
            notes.append(f"WARNING Listing {lab}.x has no chapter file; numbers kept")
            for b in blocks:
                mapping[(lab, b.k)] = b.k
            continue
        order = chapter_link_order(files[lab], lab)
        linked = []
        for a in order:
            k = int(a.rsplit("-", 1)[1])
            if k in olds:
                linked.append(k)
            else:
                notes.append(f"ERROR {os.path.basename(files[lab])} links #{a}, which has no listing in Appendix F")
        rest = sorted(k for k in olds if k not in linked)
        for k in rest:
            notes.append(f"WARNING Listing {lab}.{k} is not linked from {os.path.basename(files[lab])}; numbered after the linked ones")
        for new_k, k in enumerate(linked + rest, 1):
            mapping[(lab, k)] = new_k
    return mapping, notes


# ---------------------------------------------------------------------------------------------- rewriting
class Counter:
    def __init__(self):
        self.anchors = self.mentions = self.case = 0
        self.warnings = []


def rewrite(text, mapping, labels, cnt):
    """Rewrite anchors and prose mentions in one pass each. `labels` maps key_of(lab) -> lab."""

    def anchor_sub(m):
        lab = labels.get(m["key"].lower())
        if lab is None:
            return m.group(0)
        k = int(m["k"])
        if (lab, k) not in mapping:
            return m.group(0)
        new = f"{m['pre']}{anchor_of(lab, mapping[(lab, k)])}{m['post']}"
        if new != m.group(0):
            if mapping[(lab, k)] == k:
                cnt.case += 1
            else:
                cnt.anchors += 1
        return new

    def ref_sub(m):
        lab, k = m["lab"], int(m["k"])
        if (lab, k) in mapping and mapping[(lab, k)] != k:
            return f"{lab}.{mapping[(lab, k)]}"
        return m.group(0)

    def mention_sub(m):
        refs = m["refs"]
        new = REF_RE.sub(ref_sub, refs)
        if new != refs:
            cnt.mentions += 1
            if re.search(r"(?:–|—|-|\bto\b|\bthrough\b)\s*(?:\d|[A-F]\.)", refs[refs.find(".") + 1:]):
                cnt.warnings.append(f"range mentions a renumbered listing: '{m.group(0)}' -> '{m['kw']}{new}'; check it reads as a range")
        return m["kw"] + new

    text = ANCHOR_RE.sub(anchor_sub, text)
    return MENTION_RE.sub(mention_sub, text)


def atomic_update(path, fn, apply):
    """Apply fn(text) -> new text; if the file changed under us while we computed, recompute. Returns changed?"""
    for _ in range(5):
        before = open(path, encoding="utf-8").read()
        mtime = os.path.getmtime(path)
        after = fn(before)
        if after == before:
            return False
        if not apply:
            return True
        if os.path.getmtime(path) == mtime:
            tmp = path + ".renum.tmp"
            with open(tmp, "w", encoding="utf-8") as f:
                f.write(after)
            os.replace(tmp, path)
            return True
        time.sleep(0.5)
    raise RuntimeError(f"{path} kept changing while rewriting; try again")


# ---------------------------------------------------------------------------------------------- checks
def check(sections, files_too=True):
    problems = []
    anchors, seen_nums = {}, {}
    for s in sections:
        for b in s.blocks:
            a = b.anchor or ""
            if a != anchor_of(b.lab, b.k):
                problems.append(f"Listing {b.lab}.{b.k}: anchor '{a}' should be '{anchor_of(b.lab, b.k)}'")
            if a in anchors:
                problems.append(f"duplicate anchor {a}")
            anchors[a] = b
            if (b.lab, b.k) in seen_nums:
                problems.append(f"duplicate Listing {b.lab}.{b.k}")
            seen_nums[(b.lab, b.k)] = b
    if not files_too:
        return problems
    files = {label_for(os.path.basename(p)): p for p in sorted(glob.glob(os.path.join(SRC, "*.md")))}
    sec_anchors = {"code-" + key_of(s.lab) for s in sections}
    for p in sorted(glob.glob(os.path.join(SRC, "*.md"))):
        text = open(p, encoding="utf-8").read()
        for m in re.finditer(r"\]\(#(code-[A-Za-z0-9]+(?:-\d+)?)\)", text):
            a = m.group(1)
            if a not in anchors and a not in sec_anchors:
                problems.append(f"{os.path.basename(p)}: link #{a} does not resolve")
        # link text must agree with the anchor
        for m in re.finditer(r"\[([^\]]*\bListing ([\w-]+)\.(\d+)[^\]]*)\]\(#(code-[A-Za-z0-9]+-\d+)\)", text):
            if m.group(4) != anchor_of(m.group(2), int(m.group(3))):
                problems.append(f"{os.path.basename(p)}: link text 'Listing {m.group(2)}.{m.group(3)}' points at #{m.group(4)}")
    for lab, p in files.items():
        if lab is None or p == APPF:
            continue
        own = [b for b in seen_nums.values() if b.lab == lab]
        if not own:
            continue
        order = [int(a.rsplit("-", 1)[1]) for a in chapter_link_order(p, lab)]
        if order != sorted(order):
            problems.append(f"{os.path.basename(p)}: listings are linked in the order {order}, not 1..n")
        missing = sorted(b.k for b in own if b.k not in order)
        if missing:
            problems.append(f"{os.path.basename(p)}: Listing {lab}.{missing} never linked from the chapter")
        ks = sorted(b.k for b in own)
        if ks != list(range(1, len(ks) + 1)):
            problems.append(f"Listing {lab}: numbers {ks} are not 1..{len(ks)}")
    return problems


# ---------------------------------------------------------------------------------------------- titles
WEAK_PATTERNS = [
    (re.compile(r"^(eq|equation)s?\b", re.I), "auto title 'Eq'"),
    (re.compile(r"^-{2,}"), "ruler line"),
    (re.compile(r"^block\s*\d+(?:\s+of\s+\d+)?\s*:?\s*(?:\W*\w+){0,2}\W*$", re.I), "just a block number"),
    (re.compile(r"\((sec|eq|sect)$|\b(of|in) (sec|eq|section)$|\bi\.e$|\bw\.p$|[^.]\b(Sec|eqs?|U\.S\.C)$", re.I), "truncated at an abbreviation"),
    (re.compile(r"[=*]|_\{|\*\*|\^\{"), "bare formula"),
    (re.compile(r"^(defines|reference implementation)", re.I), "auto 'Defines ...'"),
]


def weak_reason(title):
    t = title.strip()
    if t.count("(") != t.count(")"):
        return "unbalanced parenthesis (truncated)"
    for rx, why in WEAK_PATTERNS:
        if rx.search(t):
            return why
    if len(re.sub(r"\S+\.py\b:?", "", t).split()) < 3:
        return "fewer than three words (or only a file name)"
    return None


def stub_context(path, anchor):
    """Heading chain above the first link to `anchor` in a chapter."""
    heads = []
    text = open(path, encoding="utf-8").read()
    for ln, in_code in split_fenced(text):
        if in_code:
            continue
        m = re.match(r"^(#{2,4}) (.*)", ln)
        if m:
            depth = len(m.group(1))
            heads = [h for h in heads if h[0] < depth] + [(depth, m.group(2).strip())]
        if f"(#{anchor})" in ln.lower():
            return [h[1] for h in heads]
    return []


def apply_retitle(sections, titles):
    done = []
    index = {b.anchor: b for s in sections for b in s.blocks}
    for a, t in titles.items():
        if a not in index:
            raise SystemExit(f"--retitle: no listing with anchor {a} (keys are anchors after renumbering)")
        t = re.sub(r"\s+", " ", t).strip().rstrip(".")
        if re.search(r"[{}]", t):
            raise SystemExit(f"--retitle: braces in title for {a}")
        if index[a].title != t:
            done.append((a, index[a].title, t))
            index[a].title = t
    return done


# ---------------------------------------------------------------------------------------------- main
def main():
    global ROOT, SRC, APPF
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--apply", action="store_true", help="write the changes (default: dry run)")
    ap.add_argument("--check", action="store_true", help="read-only consistency check; exit 1 on problems")
    ap.add_argument("--titles", action="store_true", help="list weak listing titles with chapter context")
    ap.add_argument("--retitle", metavar="JSON", help="{anchor: title} map applied after renumbering")
    ap.add_argument("--roots", nargs="*", default=DEFAULT_ROOTS, help="directories scanned for references")
    ap.add_argument("--root", default=ROOT, help="book root (default: the repository this script lives in); for tests on a copy")
    args = ap.parse_args()
    ROOT = os.path.abspath(args.root)
    SRC = os.path.join(ROOT, "book_src")
    APPF = os.path.join(SRC, "95_appF_code_companion.md")

    text = open(APPF, encoding="utf-8").read()
    pre, sections, trailer = parse_appf(text)
    assert serialize(pre, sections, trailer) == text, "Appendix F does not round-trip through the parser; refusing to touch it"
    labels = {key_of(b.lab): b.lab for s in sections for b in s.blocks}

    if args.check:
        problems = check(sections)
        for p in problems:
            print("PROBLEM", p)
        print(f"{sum(len(s.blocks) for s in sections)} listings, {len(problems)} problems")
        sys.exit(1 if problems else 0)

    if args.titles:
        files = {label_for(os.path.basename(p)): p for p in sorted(glob.glob(os.path.join(SRC, "*.md")))}
        n = 0
        for s in sections:
            for b in s.blocks:
                why = weak_reason(b.title)
                if why:
                    n += 1
                    ctx = stub_context(files[b.lab], b.anchor) if b.lab in files else []
                    print(f"{b.anchor:<14} [{why}] {b.title[:90]!r}\n{'':14} under: {' > '.join(ctx[-3:])}")
        print(f"{n} weak titles of {sum(len(s.blocks) for s in sections)}")
        return

    mapping, notes = build_plan(sections)
    changed = {k: v for k, v in mapping.items() if k[1] != v}
    cnt = Counter()

    # ---- rebuild Appendix F
    moved, removed_sections = [], []
    new_sections = []
    main_of = {}
    for s in sections:
        if s.lab not in main_of and not s.cont:
            main_of[s.lab] = s
    for s in sections:
        main_of.setdefault(s.lab, s)
    for s in sections:
        if main_of[s.lab] is not s:
            removed_sections.append(s)
            continue
        new_sections.append(s)
    for lab, main in main_of.items():
        allb = [b for s in sections if s.lab == lab for b in s.blocks]
        for b in allb:
            b.new_k = mapping[(lab, b.k)]
        allb.sort(key=lambda b: b.new_k)
        for b in allb:
            home = next(s for s in sections if b in s.blocks)
            if home is not main:
                b.moved = True
                moved.append(b)
            b.body = rewrite("\n".join(b.body), mapping, labels, cnt).split("\n")
            if b.moved:
                b.body = normalise_tail(b.body)
        main.blocks = allb
        if main.cont:
            main.cont = False
            main.header = re.sub(r" \(continued\)", "", main.header)
            if not main.anchor:
                main.anchor = "code-" + key_of(lab)
                main.header += f" {{#{main.anchor}}}"
        main.intro = rewrite("\n".join(main.intro), mapping, labels, cnt).split("\n")
    for s in new_sections:
        for b in s.blocks:
            b.k, b.anchor = b.new_k, anchor_of(b.lab, b.new_k)
    retitled = apply_retitle(new_sections, json.load(open(args.retitle, encoding="utf-8"))) if args.retitle else []
    for s in new_sections:
        for b in s.blocks:
            if (b.k, b.title, b.anchor) != b.orig:
                b.header = f"### Listing {b.lab}.{b.k}: {b.title} {{#{b.anchor}}}"
    for s in new_sections:                      # two blank lines close every section, as the mover writes them
        if s.blocks:
            if trailing_blanks(s.blocks[-1].body) < 2:
                s.blocks[-1].body = normalise_tail(s.blocks[-1].body)
    pre_new = rewrite("\n".join(pre), mapping, labels, cnt).split("\n")
    new_appf = serialize(pre_new, new_sections, trailer)

    # ---- report
    print(f"Appendix F: {sum(len(s.blocks) for s in new_sections)} listings in {len(new_sections)} sections")
    for (lab, old), new in sorted(changed.items()):
        print(f"  renumber Listing {lab}.{old} -> {lab}.{new}   (#{anchor_of(lab, old)} -> #{anchor_of(lab, new)})")
    for b in moved:
        print(f"  move Listing {b.lab}.{b.orig[0]} (now {b.lab}.{b.k}) into the main section F.{b.lab}")
    for s in removed_sections:
        print(f"  drop section {s.header.strip()[:80]}")
    for a, old, new in retitled:
        print(f"  retitle #{a}: {old!r} -> {new!r}")
    for n in notes:
        print("  " + n)
    if args.apply and any(n.startswith("ERROR") for n in notes):
        raise SystemExit("refusing to --apply while the plan has ERRORs (see above)")

    # ---- every other file
    touched = []

    def others():
        for root in args.roots:
            base = root if os.path.isabs(root) else os.path.join(ROOT, root)
            for dp, _, fns in os.walk(base):
                for fn in sorted(fns):
                    if fn.endswith((".md", ".py")) and os.path.join(dp, fn) != APPF:
                        yield os.path.join(dp, fn)

    for p in others():
        c0 = (cnt.anchors, cnt.mentions, cnt.case)
        if atomic_update(p, lambda t: rewrite(t, mapping, labels, cnt), args.apply):
            touched.append((os.path.relpath(p, ROOT), cnt.anchors - c0[0], cnt.mentions - c0[1], cnt.case - c0[2]))
        # Counters double-count on a retry; they are only a report.
    for rel, a, m, c in touched:
        print(f"  {'rewrote' if args.apply else 'would rewrite'} {rel}: {a} anchors, {m} mentions, {c} case fixes")
    for w in cnt.warnings:
        print("  WARNING", w)

    if args.apply:
        def write_appf(t):
            if t != text:
                raise RuntimeError("Appendix F changed while the plan was computed; run again")
            return new_appf
        atomic_update(APPF, write_appf, True)
    print("applied" if args.apply else "dry run (use --apply to write)")

    # ---- verify the outcome (on the written files when applying, on the plan otherwise)
    if args.apply:
        _, sections2, _ = parse_appf(open(APPF, encoding="utf-8").read())
        problems = check(sections2)
    else:
        problems = check(new_sections, files_too=False)
        problems += [f"(current state, would be fixed by the rewrite) {p}" for p in check(sections) if "does not resolve" in p or "points at" in p]
    for p in problems:
        print("PROBLEM", p)
    print(f"{len(problems)} problems after the pass")
    sys.exit(1 if problems and args.apply else 0)


if __name__ == "__main__":
    main()
