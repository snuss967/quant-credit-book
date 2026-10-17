# index_pdfs.py
"""Split every source book into one text file per page so agents can cite by page.

Usage:
    python3 index_pdfs.py            # index new/changed books only
    python3 index_pdfs.py --force    # re-index everything

Handles .pdf and .epub (PyMuPDF opens both). Writes:
    state/pdf_pages/<book_id>/page_0001.txt ...   (gitignored: derived, large)
    state/pdf_index.json                          (TOC + page counts + low-text warnings)
"""
import json
import os
import sys

import pymupdf  # pip install pymupdf

PDF_DIR = "./source_pdfs"
OUT_DIR = "./state/pdf_pages"
INDEX_FILE = "./state/pdf_index.json"
EXTENSIONS = (".pdf", ".epub")
LOW_TEXT_CHARS = 200  # pages below this are probably scans/figures; flag them


def index_book(path, book_id):
    doc = pymupdf.open(path)
    book_page_dir = os.path.join(OUT_DIR, book_id)
    os.makedirs(book_page_dir, exist_ok=True)
    low_text_pages = []
    for page_num in range(len(doc)):
        text = doc[page_num].get_text("text")
        if len(text.strip()) < LOW_TEXT_CHARS:
            low_text_pages.append(page_num + 1)
        with open(os.path.join(book_page_dir, f"page_{page_num + 1:04d}.txt"), "w", encoding="utf-8") as f:
            f.write(text)
    return {
        "file": os.path.basename(path),
        "mtime": os.path.getmtime(path),
        "total_pages": len(doc),
        "low_text_page_count": len(low_text_pages),
        "toc": doc.get_toc(),
    }


def main():
    force = "--force" in sys.argv
    pymupdf.TOOLS.mupdf_display_errors(False)  # Wiley epub CSS spams harmless parser errors
    os.makedirs(OUT_DIR, exist_ok=True)
    manifest = {}
    if os.path.exists(INDEX_FILE) and not force:
        with open(INDEX_FILE, encoding="utf-8") as f:
            manifest = json.load(f)

    for fname in sorted(os.listdir(PDF_DIR)):
        if not fname.lower().endswith(EXTENSIONS):
            continue
        path = os.path.join(PDF_DIR, fname)
        book_id = os.path.splitext(fname)[0]
        prior = manifest.get(book_id)
        already_done = (
            prior
            and prior.get("mtime") == os.path.getmtime(path)
            and os.path.isdir(os.path.join(OUT_DIR, book_id))
        )
        if already_done:
            print(f"  skip  {book_id} ({prior['total_pages']} pages, unchanged)")
            continue
        manifest[book_id] = index_book(path, book_id)
        m = manifest[book_id]
        print(f"  index {book_id}: {m['total_pages']} pages ({m['low_text_page_count']} low-text)")

    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)
    print(f"Indexed {len(manifest)} books into {OUT_DIR}/ for rapid page-cited extraction.")


if __name__ == "__main__":
    main()
