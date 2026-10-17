#!/usr/bin/env python3
"""Find which source-book pages talk about a topic, without reading whole books.

Examples:
    python3 tools/pdf_search.py "duration times spread"
    python3 tools/pdf_search.py "first passage" --book Schmid --top 15
    python3 tools/pdf_search.py "recovery" "beta distribution" --all   # pages containing ALL terms
    python3 tools/pdf_search.py --toc Ben_Dor                          # print a book's table of contents
    python3 tools/pdf_search.py --page Bolder_Credit_Risk_Modelling 112

Prints `book_id p.N  score  snippet`. Page numbers are PDF page indices (1-based),
which is what the [SOURCE EXTRACTION] citations use.
"""
import argparse
import glob
import json
import os
import re

PAGES_DIR = os.path.join(os.path.dirname(__file__), "..", "state", "pdf_pages")
INDEX_FILE = os.path.join(os.path.dirname(__file__), "..", "state", "pdf_index.json")


def iter_pages(book_filter):
    for book_dir in sorted(glob.glob(os.path.join(PAGES_DIR, "*"))):
        book_id = os.path.basename(book_dir)
        if book_filter and book_filter.lower() not in book_id.lower():
            continue
        for page_file in sorted(glob.glob(os.path.join(book_dir, "page_*.txt"))):
            page_num = int(re.search(r"page_(\d+)", page_file).group(1))
            with open(page_file, encoding="utf-8") as f:
                yield book_id, page_num, f.read()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("terms", nargs="*")
    ap.add_argument("--book", help="substring filter on book id")
    ap.add_argument("--top", type=int, default=10)
    ap.add_argument("--all", action="store_true", help="require every term on the page")
    ap.add_argument("--toc", metavar="BOOK", help="print table of contents for a book")
    ap.add_argument("--page", nargs=2, metavar=("BOOK", "N"), help="print one page")
    args = ap.parse_args()

    if args.toc:
        with open(INDEX_FILE, encoding="utf-8") as f:
            index = json.load(f)
        for book_id, meta in index.items():
            if args.toc.lower() in book_id.lower():
                print(f"== {book_id} ({meta['total_pages']} pages)")
                for level, title, page in meta["toc"]:
                    print(f"{'  ' * (level - 1)}{title}  [p.{page}]")
        return

    if args.page:
        book, n = args.page
        for book_dir in glob.glob(os.path.join(PAGES_DIR, f"*{book}*")):
            path = os.path.join(book_dir, f"page_{int(n):04d}.txt")
            if os.path.exists(path):
                print(f"== {os.path.basename(book_dir)} p.{n}")
                print(open(path, encoding="utf-8").read())
        return

    if not args.terms:
        ap.error("give search terms, --toc BOOK, or --page BOOK N")

    patterns = [re.compile(re.escape(t), re.IGNORECASE) for t in args.terms]
    hits = []
    for book_id, page_num, text in iter_pages(args.book):
        counts = [len(p.findall(text)) for p in patterns]
        if args.all and not all(counts):
            continue
        score = sum(counts)
        if score:
            m = patterns[counts.index(max(counts))].search(text)
            start = max(0, m.start() - 90)
            snippet = " ".join(text[start : m.end() + 90].split())
            hits.append((score, book_id, page_num, snippet))

    for score, book_id, page_num, snippet in sorted(hits, reverse=True)[: args.top]:
        print(f"{book_id} p.{page_num}  [{score}]  …{snippet}…")


if __name__ == "__main__":
    main()
