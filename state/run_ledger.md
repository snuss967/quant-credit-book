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
| ed2-reader-lens-reviews | review + WP4 | Fable ×3 → Fable synthesis → Opus ×2 lanes | Reviews as an RSSG partner, a desk head, and a transition coach → master gap list, TOC growth, briefs for the top 4 new files → write them | running |

## Pause (2026-10-18 01:30 UTC, NEAR_CAP at ~92%)

All workflows were stopped to protect the user's 97% cap. On disk at the pause:
- COMPLETE: 06_ch06b, App D, App E, the three reader-lens reviews, and 5 research dossiers.
- PARTIAL: 04_ch04b, 07_ch07b, 12_ch12b, and 4 dossiers.
- MISSING: the synthesis and 6 dossiers.

The resume checklist is in state/continuation_prompt.md, and a resume is scheduled for 04:17 UTC (user-set: 2h40m after 01:37 UTC).

## Edition 2 restart (2026-10-18 04:32 UTC, new window 04:30–09:30)

Prep (04:19–04:30, local only): code sweep (0 new listings), `<!-- EXPLAINED -->` marker added to the code mover, PDF untracked (rule 9 in PROCESS.md), and the meter now carries its scale across windows until the user gives a new reading. Scripts live in `tools/workflows/`. Pre-revision text for every chapter = commit `9ac1c37` (verifiers diff against it).

| Run | Task ID | Package | Models | Owns | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| reader-lens (resumed wf_aa7ed3ed-60e) | wrt9kw1ej | WP4 | Fable synthesis → Opus ×4 | synthesis.md, TOC growth, briefs and drafts for the top 4 new files (excluding 01_ch01b and 04_ch04c) | running |
| primers-finish | wz1dbyljo | WP2 | Opus | finish 04_ch04b, 12_ch12b, 07_ch07b (append-only) | running |
| research-A | wc8sol35m | research | Sonnet, no map | case_lmt_private_and_european, case_courts_as_regime_variables, trend_re_default_and_recovery_dataset, trend_private_credit_marks_and_redemptions, trend_listed_credit_futures | running |
| research-B | wpjuofa0m | research | Sonnet, no map | trend_part_v_market_structure_2026, case_carvana_svb_wolfspeed, case_manufactured_credit_events, trend_insurance_capital_forced_flow, trend_figure_data_series | running |
| u3-media | wgydgxc54 | U3 | Sonnet | media_episodes_posts_parts_I_II / III_IV / V_VIII (specific episodes and posts per chapter) | running |
| u3-perspectives-life | w28pii0xt | U3 + new chapters | Sonnet → Fable brief → Opus | life_quant_shop_daily_life, perspectives_buyside_credit_managers, perspectives_dealers_and_systematic_shops → 04_ch04c, 01_ch01b | running |
| u2-A | wmllmn46e | U1+U2 | Sonnet → Fable → Opus → Sonnet verify | Ch 1, 3, 2, 4 | running |
| u2-B | wt3057wkb | U1+U2 | Sonnet → Fable → Opus → Sonnet verify | Ch 5, 6, 7 | running |
| u1-lane-1 | w3worjqi3 | U1 | Sonnet | Ch 13–17, 8–12, 6-B, App B | running |
| u1-lane-2 | w14cc841q | U1 | Sonnet | Ch 18–28, App D, App E | running |
| pace-guard | bi16e9flv | — | — | `--target 97 --cap-only` (alarms at 91%) | running |

Next in line, as slots free: U2 on Part IV (Ch 13–17), U3b (Resource Graph upgrade from the media dossiers, Sonnet), U4 figures (Sonnet + matplotlib), U1 sweep on the three primers once they finish, then U2 on the remaining Parts.

### Widened at 04:44 UTC (user: "put more agents on it")

| Run | Task ID | Stages | Owns | Status |
| :--- | :--- | :--- | :--- | :--- |
| part-IV-a | wgzz9zxzv | figures → figcheck → brief → revise → verify | Ch 13, 14 | running |
| part-IV-b | w0wcd6yna | figures → figcheck → brief → revise → verify | Ch 16, 15 | running |
| figs-V-a | w4lyhs2cz | figures → figcheck | Ch 18, 19 | running |
| figs-V-b | w8lexa6xs | figures → figcheck | Ch 20, 22 | running |
| pace-guard v2 | b22xrgxiz | `--target 96 --cap-only --check-every 60` (alarm at 90%) | — | running (replaces bi16e9flv) |
| autosnap | bdca3onxd | commit + push every 10 min for 2 h | — | running |

Scheduled restart: 09:33 UTC (trigger trig_016k2PhmaKrabSxxMUUnipys; user-set, 4h50m after 04:43, just after the 09:30 reset). At the 90% alarm, stop every workflow, list them here under "Stopped at cap" with their run IDs, and resume them at the restart.

### 05:00 UTC: U1 complete everywhere except the three primers being finished (07_ch07b has 2 stubs, 12_ch12 has 0 after lane 1). Figures done: Ch 18, 19, 20, 22 (checked); Ch 13–16 (in their Part IV pipelines).

| Run | Task ID | Stages | Owns | Status |
| :--- | :--- | :--- | :--- | :--- |
| u1-lane-1 | w3worjqi3 | U1 | Ch 8–17, 6-B, App B | done |
| u1-lane-2 | w14cc841q | U1 | Ch 18–28, App D, E | done |
| figs-V-a | w4lyhs2cz | figures → figcheck | Ch 18, 19 | done |
| figs-V-b | w8lexa6xs | figures → figcheck | Ch 20, 22 | done |
| figs-VI-a | w24ff95yk | figures → figcheck | Ch 21, 23 | running |
| figs-VI-b | wums0yjya | figures → figcheck | Ch 24, 25 | running |
| figs-VII | w3c662d09 | figures → figcheck | Ch 26, 27 | running |

Still to queue: figures for Ch 8–12, 17, 28, 1-B, 4-C, primers, Ch 1–7 (after their revisions); U2 for Ch 17, Part III, Parts V–VIII.
| primers-finish | wz1dbyljo | WP2 | 04_ch04b, 12_ch12b, 07_ch07b finished (COMPLETE); new listings swept to App F | done |
| primers-pipeline | (see below) | u1 → figures → figcheck | 07_ch07b, 04_ch04b, 12_ch12b | running |
