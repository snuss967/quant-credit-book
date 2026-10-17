# Run Ledger

Every workflow, what it owns, and where its output lands. Check this before launching anything, so no topic is researched twice.

## Edition 1

| Run | Stage | Owns | Outputs | Status |
| :--- | :--- | :--- | :--- | :--- |
| ch-group-1 | 2–3 | Ch 1, 8, 15, 22 | briefs + chapters | running |
| ch-group-2 | 2–3 | Ch 2, 9, 16, 23 | briefs + chapters | running |
| ch-group-3 | 2–3 | Ch 3, 10, 17, 24 | briefs + chapters | running |
| ch-group-4 | 2–3 | Ch 4, 11, 18, 25 | briefs + chapters | running |
| ch-group-5 | 2–3 | Ch 5, 12, 19, 26 | briefs + chapters | running |
| ch-group-6 | 2–3 | Ch 6, 13, 20, 27 | briefs + chapters | running |
| ch-group-7 | 2–3 | Ch 7, 14, 21, 28 | briefs + chapters | running |
| front-matter | 3 | Preface, 8 part openers, App A (notation), App B (data atlas) | `book_src/00_00_*`, `*_00_part_*`, `90_appA_*`, `91_appB_*` | running |
| trend-A | 1 | electronification/PT/ETF liquidity; systematic credit industry; trend/TSMOM; academic frontier; AI/LLMs | `state/research/trend_*.md`, `exploratory_space_A.md` | running |
| trend-B | 1 | LMT/default/recovery cycle; private credit; loans/CLOs; market-structure regulation; dealers/CDS/index | `state/research/trend_*.md`, `exploratory_space_B.md` | running |
| cases-lmt | 1 | Serta; J.Crew; Incora/Wesco; Mitel; double-dip/pari-plus; 2024–26 LMT wave | `state/research/case_*.md`, `map_case_lmt.md` | running |
| cases-markets | 1 | March 2020 ETFs; SVB 2023; Hertz; Hovnanian/Windstream; Carvana 2023; GM/Ford 2005 | `case_*.md`, `map_case_markets.md` | running |
| cases-systemic | 1 | CS AT1 2023; UK LDI 2022; energy 2015–16; Lehman CDS auction; China property; First Brands/Tricolor 2025 | `case_*.md`, `map_case_systemic.md` | running |
| shelf-1 | 1 | Ben Dor; Dynkin; Bohn & Stein; Paleologo; Moyer | `shelf_*.md`, `map_shelf_texts1.md` | running |
| shelf-2 | 1 | Schmid; Bolder; Veronesi; Houlihan Lokey; the five framework papers | `shelf_*.md`, `map_shelf_texts2.md` | running |
| papers | 1 | bond factor zoo; trend/momentum; microstructure; default/recovery; LMT empirics; LLM/legal NLP | `papers_*.md`, `map_papers_lit.md` | running |
| trend-C | 1 | EM/sovereign; securitized; ESG/climate; retail/wealth channel; tokenization/venues/Europe | `trend_*.md`, `map_trend_C.md` | running |
| media | 1 | podcasts; newsletters/blogs; courses/reading path; career map | `media_*.md`, `map_media_eco.md` | running |
| preflight-review | 4a | Engagement + foundations on all 28 brief digests | `state/reviews/ed1/preflight_*.md` | queued (starts when all 28 briefs exist) |
| part-reviews | 4b | Engagement + foundations per Part on chapter text | `state/reviews/ed1/part_*` | queued (after chapters) |
| appendix-C | 3 | Trend Tracker from all trend research | `book_src/92_appC_trend_tracker.md` | queued (after trend-A/B/C) |
| ed2-planner | 6 | Continuation prompt + TOC v2 + queue | `state/continuation_prompt.md` | queued (after reviews) |
