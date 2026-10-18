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

## Stopped at cap (2026-10-18 05:18 UTC, meter ~92%)

The pace guard fired NEAR_CAP at 05:17. All 10 running workflows were stopped (wrt9kw1ej, wc8sol35m, wpjuofa0m, wgydgxc54, w28pii0xt, wmllmn46e, wt3057wkb, wgzz9zxzv, w0wcd6yna, w9ho5nhr0). The autosnap loop keeps running (git only). Exact resume arguments are in `state/resume_runs.json`.

State on disk at the stop:
- **U2 narrative revision.** COMPLETE (log ticked): Ch 1 (10.7k→27.7k words), Ch 5 (15.2k→33.9k), Ch 6 (14.2k→36.7k). Nearly done: Ch 3 (26/27). In progress: Ch 7 (4/24), Ch 13 (13/23), Ch 14 (17/23), Ch 15 (15/26), Ch 16 (18/23). Brief only: Ch 2, Ch 4 (0/22). No verify pass has run yet on any of them.
- **Figures (U4), checked.** Ch 13–16, 18–27 and primers 4-B and 12-B (85 PNGs). 7-B figures are made but not checked.
- **Reader-lens.** synthesis.md COMPLETE. New file 03_ch03b_your_first_year_on_the_desk COMPLETE (11.7k). 12_ch12c_plan_valuation_dip_and_exit_as_derivatives PARTIAL (15.2k). Briefs exist for 08_ch08b (risk model and limit sheet) and 08_ch08c (morning P&L explain), but those files are not written yet.
- **Research.** COMPLETE: lmt_private_and_european, courts_as_regime_variables, re_default_and_recovery_dataset, part_v_market_structure_2026, carvana_svb_wolfspeed. PARTIAL: private_credit_marks, listed_credit_futures, manufactured_credit_events, insurance_capital_forced_flow. MISSING: figure_data_series.
- **U3.** COMPLETE: media parts I–II and III–IV, life_quant_shop_daily_life, perspectives_buyside. PARTIAL: media parts V–VIII, perspectives_dealers_and_systematic_shops. The briefs and chapters for 04_ch04c and 01_ch01b have not started.

**Resume at 09:33:** resume each run in `state/resume_runs.json` (Workflow with scriptPath + resumeFromRunId + args). Then add a Fable quality read of revised Ch 1 (check for duplication, pacing, and bloat, since chapters grew 2–2.5×) BEFORE U2 scales to the rest of the book.

## Resumed 05:38 UTC: user reading 53% (meter said 92.8%, so it was overestimating 1.75×)

The meter is recalibrated to 53% at 05:35. The user's rule: "estimate 110% as the drop dead stopping" (on the old meter scale). 110% old ≈ **62.8% actual**, so the pace guard (b2xbmwx7r) runs `--target 68.8 --cap-only --check-every 60` and alarms at 62.8%. If the user meant 97% actual, raise the target to 103.
The user completed the cut-off note: **"It seems like there is a lot of prescriptiveness and not narrative."** It is recorded as directive 12. `tools/prescriptiveness.py` now measures bullets, modal and imperative density, and dialogue per 1,000 words. Writer prompts (VOICE) now carry the verdict, and the brief and revise prompts read `state/reviews/ed2/u2_lessons.md` once it exists.
All 10 stopped runs were resumed (new task IDs in `state/resume_runs.json`), plus **u2-quality-read** (w0dq9p9lo, a Fable read of the revised Ch 1/5/6, producing a review, `u2_lessons.md`, and a fix list).

## 05:46 UTC: user reading 59%. New rule: "run for another 50% on your scale ... don't stop until you hit 110% by your count, counting from 59% now"

Read on the old overestimating scale (1.75×), +51 points there is about +29 actual, so the **stop is at about 88% actual**, below the 97% cap. The meter is recalibrated to 59% at 05:45. Pace guard b9kryba6o runs `--target 94.1 --cap-only --check-every 60` (alarm at 88.1%). The primers pipeline is done (4-B, 7-B, 12-B: U1, figures, checks).
The chapter pipeline gained a `resgraph` stage (U3b: specific episodes and posts from the media dossiers replace channel-level references).

| Run | Task ID | Stages | Owns |
| :--- | :--- | :--- | :--- |
| part-III-a | wr7mis8ev | figures → figcheck → resgraph → brief → revise → verify | Ch 8, 9 |
| part-III-b | wklksowgz | same | Ch 10, 11 |
| part-III-c | wu9xnpg9n | same | Ch 12, 17 |
| figs-misc | wyz2ysvwc | figures → figcheck | Ch 28, 6-B, 3-B |
| u3-media | wmgs3kr4j | — | All three media dossiers COMPLETE: 283 verified episodes, posts, and talks (Parts I–II 80, III–IV 88, V–VIII ~115 URLs) | done |
| resgraph-V-a | wg1sjulmh | resgraph | Ch 18–23 | running |
| resgraph-V-b | wl6vl10zt | resgraph | Ch 24–27, App D, App E, primers 4-B, 7-B, 12-B | running |

### 05:52 UTC: quality read done (w0dq9p9lo)
Verdict: the process works where it produced scenes and fails where it stacked new text on old (Ch 1 is "a palimpsest"). Modal density rose because the prescription moved into templated "When to reach for it" and "Reading Listing" paragraphs. There are 18 Math, Gently boxes in Ch 1, three of them adjacent. Ch 6 leaks "CHECK" and "search summary" text in 5 places. Ch 1's Serta "no co-op" sentence contradicts the dossier. Output: `state/reviews/ed2/u2_lessons.md` (16 rules: growth 1.6–1.9×, one telling per fact, template ban, box budget ≤1 per 1,200 words and ≤10 per chapter, a Finder table in each Debrief, cast bible, fiction labels) and `u2_fixes_ch01_05_06.md`.
| fixes-and-cast | wwluacbli | Sonnet cast bible → Opus fixer for Ch 6 (Ch 1 and 5 follow once their verify is COMPLETE) | running |
Follow-up queued: a lessons pass on Ch 3, 7, 13–16, which were revised before the lessons existed.
| resgraph-V-b | wl6vl10zt | resgraph | Ch 24–27, App D, E, 4-B, 7-B, 12-B upgraded to specific episodes/posts | done |
| part-VII-u2 | waulio30e | brief → revise → verify | Ch 24, 25 | running |

## Stopped at the user's ~88% rule (2026-10-18 06:11 UTC; meter 88.6%, calibrated at 59% at 05:45)

All 11 runs were stopped. `state/resume_runs.json` lists each one with its scriptPath, runId, and args.
State on disk:
- **U2 revision logs COMPLETE:** Ch 1, 2, 3, 5, 6, 7, 13, 14, 15, 16. Verify COMPLETE: Ch 5, 6, 13, 14, 15, 16. Verify pending: Ch 1, 2, 3, 7. Ch 4's revision is PARTIAL.
- **Quality fixes:** Ch 6 fix log PARTIAL. Ch 1 and Ch 5 fixes not started (they wait for verify).
- **Part III, in revision (PARTIAL logs):** Ch 8, 9, 11, 12, plus Ch 24 and 25. Ch 10 has figures and Resource Graph done, brief pending. Ch 17 has its brief done, revision pending.
- **Figures:** done for Ch 8–12, 13–16, 17–28, primers 4-B, 6-B, 7-B, 12-B. 03_ch03b figures PARTIAL. Ch 1–7 have none yet (they wait for their revisions).
- **Resource Graphs upgraded:** Ch 8–12, 17–27, App D, E, 4-B, 7-B, 12-B.
- **New files:** 12_ch12c COMPLETE (15.2k), 08_ch08b COMPLETE (14.7k), 08_ch08c PARTIAL (14.9k), 01_ch01b PARTIAL (3.2k), 04_ch04c PARTIAL (5.5k). Briefs for 01_ch01b and 04_ch04c are COMPLETE. The cast bible is COMPLETE.
- **Research:** all COMPLETE except trend_figure_data_series (PARTIAL).

**New stage `lessons`** (Opus): applies u2_lessons.md to chapters revised before the lessons existed (audit → fix → metrics). Queue it for Ch 2, 3, 7, 13, 14, 15, 16 once each one's verify is COMPLETE. Ch 1, 5, 6 get the Fable fix list (fixes-and-cast script) instead.

**Restart plan (09:33):**
1. Resume every run in resume_runs.json.
2. Launch chapter_pipeline `lessons` for [13, 14], [15, 16], and [2, 3, 7] (gated on verify).
3. Relaunch fixes-and-cast with stems [06, 01, 05].
4. U2 (figures already done) for Ch 18–23, 26–28 and primers 4-B, 6-B, 7-B, 12-B: stages brief → revise → verify.
5. Figures and Resource Graphs for Ch 1–7 and for the new files once their revisions settle.
6. Build, send the PDF, commit.

## 06:45 UTC: user directive 13, the relative-value thread (pod long-one/short-another to isolate idio, woven through every chapter)

Measured coverage: idio isolation is concentrated in Ch 1, 7, 8, 8-B, 8-C, 19 and 28; the explicit pod pair trade is thin almost everywhere. Plan: `state/rv_thread_plan.md`. Prompts updated: every writer's VOICE, every brief's required list, and the lessons audit now carry the RV beat. New stage `rv` (Opus RV weaver) is for chapters already revised. New workflow `tools/workflows/rv_thread.js`: Sonnet research ×2 (pods and risk; pairs literature and mechanics) → Fable RV architect (`state/rv_thread.md`, `state/rv_pair_book.md`, optional new chapter 08_ch08d) → Opus writer. **Launch FIRST at 09:33**, before resuming the revisers, so the revisions pick up the thread.

## Restart 09:34 UTC (window 09:30–14:30)

Launched: **rv-thread** (wnoycfspo), reader-lens (w0vm8d6o1), research-B (wjge66z49), u3-perspectives-life (wt0odrxzq), figs-misc (woka093x1), fixes-and-cast with Ch 6/1/5 (wjaxjrny2), verify for Ch 1, 3, 2, 7 (w3oiwl78i), and lessons→rv for Ch 13–14 (wh7jk9av4) and Ch 15–16 (wmcxw8m61); the rv stage waits for the thread. **Held until state/rv_thread.md is COMPLETE:** u2-A, u2-B, part-III-a/b/c, part-VII-u2. Pace guard b5dam393p (`--target 94`, alarm 88% actual). Autosnap bihya4qw7.
| reader-lens | w0vm8d6o1 | — | DONE: all 4 top new files COMPLETE (3-B 10.6k, 12-C 13.8k, 8-B 13k, 8-C 13.5k). Synthesis-endorsed files still to write: 00_02 (how to use), 4-D (getting the seat), 2-B (TCA), App Z (solutions). Queue them after the RV thread (4-D and 2-B carry RV beats; App Z goes last, once the exercises settle) | done |
| redpen | wpslncppo | Sonnet | Synthesis §5 red-pen items on idle files: App A (A5), Ch 28 (C9, D7), Ch 27 (C10), Ch 26 (C11, D9), Ch 25 (B10), Ch 12 (C11), Ch 8 (C11), Ch 4 (D11 §4.1), preface and Part I (D6), README (D10). Remaining items (B7, B13 Ch 13; B8, B12 Ch 14; B9 Ch 16; B11, C12 Ch 5; D8 Ch 3; D11 Ch 1) fold into those chapters' later passes | running |
| newfiles-figs | we6vugnpe | figures → figcheck → resgraph | 12-C, 8-B, 8-C | running |
