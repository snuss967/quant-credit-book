# Run Ledger

Every workflow, what it owns, and where its output lands. Check this before launching anything, so no topic is researched twice. Restarts come from `python3 tools/status.py`, never from memory.

## Incidents

| When (UTC) | What | Impact | Prevention |
| :--- | :--- | :--- | :--- |
| 2026-10-17 ~23:25 | About 36 concurrent agents exhausted the session usage limit (reset 23:30) | All in-flight agents died. Lost: the research held in agent context (≈49 dossiers), every chapter writer, and 9 advisors. Survived: everything already on disk (13 briefs, 4 trend dossiers, front matter). | Durability rules (PROCESS.md): incremental writes, completion markers, resume-not-restart, status-driven relaunch, pacing at ~20 agents, a limit-handling playbook |

## Pacing event (2026-10-17 23:48 UTC)

Usage reached 30% of the window in about 15 minutes, about 75% of it from Fable research loops. All 12 workflows were stopped (no data lost: every brief and partial chapter was on disk). Replaced by a paced pool of 4 lean Opus writers with a background pace guard. Briefs for Ch 13 and 15–28 are PARTIAL but substantive (6–11k words, all sections drafted; Ch 20 is thinner at 4k) and are used as-is.

| Run | Owns | Status |
| :--- | :--- | :--- |
| writers-paced-A/B | First paced pool | stopped 00:02 (finished Ch 1, 3, 7) |
| throughput (8 writers) | First throughput pool | stopped 00:11 and replaced by 16 lanes (partials on disk) |
| wide-W1 | Ch 5, 9, 19, 28 | running |
| wide-W2 | Ch 13, 10, 20 | running |
| wide-W3 | Ch 15, 11, 21 | running |
| wide-W4 | Ch 26, 12, 22 | running |
| wide-W5 | Ch 4, 14, 23 | running |
| wide-W6 | Ch 2, 16, 24 | running |
| wide-W7 | Ch 6, 17, 25 | running |
| wide-W8 | Ch 8, 18, 27 | running |
| pace-guard | Cap-only guard; alarms at 84% | running |

## Edition 1: superseded runs (restarted 2026-10-17 23:40 UTC, stopped 23:48 for pacing)

| Run | Stage | Owns | Status |
| :--- | :--- | :--- | :--- |
| resilient-ch-1 | 2–3 | Ch 1 (resume seed), 2, 16 | stopped 23:48 (outputs on disk) |
| resilient-ch-2 | 2–3 | Ch 3, 4, 17 | stopped 23:48 (outputs on disk) |
| resilient-ch-3 | 2–3 | Ch 5, 6, 18 | stopped 23:48 (outputs on disk) |
| resilient-ch-4 | 2–3 | Ch 7, 8, 19 | stopped 23:48 (outputs on disk) |
| resilient-ch-5 | 2–3 | Ch 9, 10, 20, 21 | stopped 23:48 (outputs on disk) |
| resilient-ch-6 | 2–3 | Ch 11, 12, 22, 23 | stopped 23:48 (outputs on disk) |
| resilient-ch-7 | 2–3 | Ch 14, 24, 25 | stopped 23:48 (outputs on disk) |
| resilient-ch-8 | 2–3 | Ch 27, 28 | stopped 23:48 (outputs on disk) |
| legacy g6 | 2–3 | Ch 13 (advisor survived the outage; its writer follows) | stopped 23:48 (writer partial on disk) |
| legacy g1 | 2–3 | Ch 15 (advisor survived; writer follows) | stopped 23:48 (writer partial on disk) |
| legacy g5 | 2–3 | Ch 26 (advisor survived; writer follows) | stopped 23:48 (writer partial on disk) |
| research-trends-AB | 1 | TSMOM in credit; loans/CLOs; market-structure regulation; dealers/CDS/index; academic frontier; AI/LLMs; then the Fable map `exploratory_space_trends_AB.md` | stopped 23:48 (outputs on disk) |

## Edition 1: completed

| Run | Output |
| :--- | :--- |
| front-matter | Preface, 8 part openers, App A (notation, 6.7k words), App B (data atlas, 8.0k words) |
| advisors (pre-outage) | Briefs for Ch 1–12 and 14 |
| trend dossiers (pre-outage) | `trend_electronification_pt_etf_liquidity`, `trend_systematic_credit_industry`, `trend_lmt_default_recovery_cycle`, `trend_private_credit_convergence` |

## Queued (launch as chapter slots free up; tier b)

| Run | Owns |
| :--- | :--- |
| research-trend-C | EM/sovereign; securitized; ESG/climate; retail/wealth channel; tokenization/venues/Europe |
| research-cases-lmt | Serta; J.Crew; Incora/Wesco; Mitel; double-dip/pari-plus; 2024–26 LMT wave |
| research-cases-markets | March 2020 ETFs; SVB 2023; Hertz; Hovnanian/Windstream; Carvana 2023; GM/Ford 2005 |
| research-cases-systemic | CS AT1 2023; UK LDI 2022; energy 2015–16; Lehman CDS auction; China property; First Brands/Tricolor 2025 |
| research-shelf-1 / -2 | Digests of all 9 textbooks plus the 5 framework papers |
| research-papers | Bond factor zoo; trend/momentum; microstructure; default/recovery; LMT empirics; LLM/legal NLP |
| research-media | Podcasts; newsletters; courses/reading path; career map |
| preflight-review | Engagement and foundations review of all 28 brief digests (starts when all 28 briefs are COMPLETE) |
| part-reviews | Engagement and foundations review per Part on chapter text (after chapters) |
| appendix-C | Trend Tracker from all trend research |
| ed2-planner | Continuation prompt, TOC v2, and the next queue |

## Edition 1: finishing (00:40 UTC, usage 59%)

19 of 28 chapters are COMPLETE. Ch 19–25 are in progress and Ch 27–28 are starting in the wide lanes.

| Run | Owns | Status |
| :--- | :--- | :--- |
| ed1-reviews-and-trend-tracker | Fable engagement review, Fable foundations review (effort high, digest-driven), Appendix C | running |
| Sonnet research (targeted) | Only the case studies and gaps the reviews request | queued until the reviews land |
| trend-watch-factcheck (×2) | Sonnet checks of all 74 Trend Watch boxes, Ch 1–28, report-only | running |
| pace-guard | Cap-only, target 97 (alarms at 91) | running |

## Edition 2 (started 2026-10-18 ~01:05 UTC, theme "One Author, One Floor, One Home")

Edition 1 shipped at commit 8dffb93 (474k words, 1,212 pages). The Edition 2 plan is in state/continuation_prompt.md.

| Run | Package | Model | Owns | Status |
| :--- | :--- | :--- | :--- | :--- |
| ed2-wp1-apply-factchecks | WP1 | Sonnet ×4 | Apply 26 corrections and hedges across Ch 1–28; log in state/reviews/ed2/ | running |
| ed2-research-A | research | Sonnet | factor replication; US LMT autopsies; private/EU LMEs; courts as regimes; re-default dataset; private-credit marks; credit futures | running |
| ed2-research-B | research | Sonnet | foundations shelf pages; RFQ quoting frontier; Part V market structure 2026; cap-structure pain trades; manufactured credit events; insurance forced flow; figure data series | running |
| ed2-wp2-primers-1 | WP2 | Opus | 04_ch04b bond math; 12_ch12b restructuring state machine | running |
| ed2-wp2-primers-2 | WP2 | Opus | 06_ch06b options and measures; 07_ch07b statistics | running |
| ed2-wp2-appendices | WP2 | Opus | 94_appE Laws of the Desk; 93_appD plumbing | running |
