#!/usr/bin/env bash
# build_book.sh — stitch book_src/*.md (lexicographic order) into output/:
#   Quant_Credit_Master_Book.md    the monolith (with a Pandoc YAML header)
#   Quant_Credit_Master_Book.html  standalone HTML, clickable TOC, MathJax
#   Quant_Credit_Master_Book.pdf   via headless Chromium + MathML (skipped if no browser; BUILD_PDF=0 to skip)
set -euo pipefail
cd "$(dirname "$0")"
export LC_ALL=C  # deterministic glob order: 00_00 < 01_00 < 01_ch01 < 02_ch02 ...

TIMESTAMP=$(date -u +"%Y-%m-%d %H:%M UTC")
OUT_DIR="./output"
mkdir -p "$OUT_DIR"

MASTER_MD="$OUT_DIR/Quant_Credit_Master_Book.md"
MASTER_HTML="$OUT_DIR/Quant_Credit_Master_Book.html"
MASTER_PDF="$OUT_DIR/Quant_Credit_Master_Book.pdf"
BODY_MD="$(mktemp)"
OUT_BODY_MD="$(mktemp)"
# The print HTML sits at the repo root so figure paths (assets/figures/...) resolve for Chromium.
PRINT_HTML="$(pwd)/.print_book.html"
trap 'rm -f "$BODY_MD" "$OUT_BODY_MD" "$PRINT_HTML"' EXIT

EDITION=$(python3 -c "import json; print(json.load(open('state/book_state.json')).get('edition', 1))" 2>/dev/null || echo 1)
TITLE="Systematic & Quantitative Credit: From PJT RSSG to the Automated Desk"
SUBTITLE="Mathematical Foundations, Microstructure, LMT Game Theory, and Alpha Isolation (Edition $EDITION, Build: $TIMESTAMP)"

shopt -s nullglob
CHAPTERS=(./book_src/*.md)
if [ ${#CHAPTERS[@]} -eq 0 ]; then
    echo "build_book.sh: no chapters in ./book_src/" >&2
    exit 1
fi

# Body = every chapter, separated by a rule. The rule is followed by a blank line so
# Pandoc never mistakes it for the start of a YAML block.
for f in "${CHAPTERS[@]}"; do
    printf '\n' >> "$BODY_MD"
    cat "$f" >> "$BODY_MD"
    printf '\n\n---\n\n' >> "$BODY_MD"
done

# Files in output/ see figures one directory up.
sed 's#](assets/figures/#](../assets/figures/#g' "$BODY_MD" > "$OUT_BODY_MD"

{
    echo "---"
    echo "title: '${TITLE}'"
    echo "subtitle: '${SUBTITLE}'"
    echo "toc: true"
    echo "toc-depth: 3"
    echo "---"
    echo ""
    cat "$OUT_BODY_MD"
} > "$MASTER_MD"

# YAML blocks are disabled when reading the body so a stray '---' inside a chapter
# can never abort the build; metadata is passed on the command line instead.
PANDOC_COMMON=(-f markdown-yaml_metadata_block+lists_without_preceding_blankline -s --toc --toc-depth=3 --section-divs
    -H ./assets/book_head.html
    --metadata title="$TITLE" --metadata subtitle="$SUBTITLE"
    --metadata pagetitle="Quantitative Credit Master Book")

if command -v pandoc &> /dev/null; then
    pandoc "$OUT_BODY_MD" "${PANDOC_COMMON[@]}" --mathjax -t html5 -o "$MASTER_HTML"

    if [ "${BUILD_PDF:-1}" = "1" ]; then
        CHROME="${CHROME_BIN:-}"
        if [ -z "$CHROME" ]; then
            for c in chromium chromium-browser google-chrome /opt/pw-browsers/chromium-*/chrome-linux/chrome; do
                if command -v "$c" &> /dev/null; then CHROME="$c"; break; fi
            done
        fi
        if [ -n "$CHROME" ]; then
            # MathML renders natively in Chromium, so the PDF needs no network for MathJax.
            pandoc "$BODY_MD" "${PANDOC_COMMON[@]}" --mathml -t html5 -o "$PRINT_HTML"
            "$CHROME" --headless --no-sandbox --disable-gpu --no-pdf-header-footer \
                --print-to-pdf="$MASTER_PDF" "file://$PRINT_HTML" > /dev/null 2>&1 \
                || echo "build_book.sh: PDF step failed (HTML and MD are fine)" >&2
        else
            echo "build_book.sh: no Chromium found; skipping PDF" >&2
        fi
    fi
else
    echo "build_book.sh: pandoc not found; built Markdown only" >&2
fi

WORD_COUNT=$(cat "${CHAPTERS[@]}" | wc -w | tr -d ' ')
echo "[$TIMESTAMP] Edition $EDITION compiled successfully: ${#CHAPTERS[@]} files, $WORD_COUNT words."
