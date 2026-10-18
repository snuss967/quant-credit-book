# Figure check (Edition 2): Chapter 3-B, Your First Year on the Desk

Chapter: book_src/03_ch03b_your_first_year_on_the_desk.md. Script: tools/figures/ch03b.py. Figures log: state/revisions/ed2/03_ch03b_your_first_year_on_the_desk.figures.md (STATUS: COMPLETE at start).
House style read from the docstring of tools/figures/style.py. All eight PNGs were opened with the Read tool, before and after fixes; the full script was re-run at the end (all eight files under 260 KB, white background, 150 dpi).

Checks that apply to every figure
- No in-image titles; one y-axis per panel (no twinx anywhere in the script); text in INK, INK_2 or MUTED; grid on y only where used.
- Colours: the script holds a fixed role mapping across the chapter (BLUE = the desk's own object, ORANGE = somebody else's or wrong clock, VIOLET = clock with a contract attached, RED = default or critical event, grey = context) and documents it in its header. Aqua, yellow and magenta are never used, so the direct-label rule for slots 3-5 does not bite. Violet and red are slots 7 and 8 rather than 3 and 4; accepted as a deliberate, documented, chapter-consistent choice (slots 3-5 fail 3:1 contrast). Every series is also identified by a direct label or a note.
- Embedding: all eight embeds use `![Figure 3-B.k: ...](assets/figures/ch03b_*.png)`, every file exists, numbering 3-B.1 to 3-B.8 is in order of appearance, there are no stale "3B.k" labels in the chapter body (the old labels survive only in the generated output/Quant_Credit_Master_Book.md, which the next build replaces).
- Real-data traces re-verified: FRED DGS10 re-downloaded for 15 Oct 2021 to 15 Oct 2026 gives 1,248 daily changes and sigma 6.24 bp (caption: 6.2 bp), identical to the cached CSV (formatting differences only). 2026 FOMC dates re-read from federalreserve.gov/monetarypolicy/fomccalendars.htm: 27-28 Jan, 17-18 Mar, 28-29 Apr, 16-17 Jun, 28-29 Jul, 15-16 Sep, 27-28 Oct, 8-9 Dec, all matching the script's mid-dates. Every Saks date and number (23 Dec 2024, $2.2bn 11% notes, 47.5 on 16 May 2025 = day 144, $121mm end-June coupon, exchange offer 21 Jul to 8 Aug, $126mm December interest, ABL steps 1 and 16 Dec, S&P SD 7 Jan, petition 13 Jan, RSA 2 Apr, plan 5 Jun, emergence 26 Jun) matches state/research/case_lmt_autopsies_us_2020_2026.md section 8. Halvorsen dates (consent 5 Nov, coupon missed Fri 13 Nov, grace end Sun 13 Dec, day 28 = Fri 11 Dec 2026) match the chapter's own listing text and exercise 3.

## Per-figure verdicts

### Figure 3-B.1, ch03b_snap_phantom: PASS after caption and label fix
- Correctness: 4 bp x $22,000 = $88,000 (the marked drop is -2.7 to -6.7 bp, 4.0 bp); square-root curve $51.8k at 60 minutes (caption $52,000), straight line $20.3k (caption $20,000); both curves monotone and anchored at zero.
- Honesty: caption says Illustrative and cites FRED for the 6.2 bp scale. One inconsistency fixed: the chapter's box hedges a $50mm five-year bond, but the axis and caption said "10-year yield". Axis now reads "Treasury yield since yesterday's snap (bp)" and the caption says the simulated walk stands in for the Treasury yield behind the box's five-year bond, with the 6.2 bp scale taken from the 10-year (the only series checked).
- Legibility: no collisions or clipping.
- Embedding: after the paragraph that states the $52,000 result. OK.

### Figure 3-B.2, ch03b_day_timeline: PASS after font fix
- Correctness: times match the chapter text (6:45, 7:15, 7:30, 8:30, three intraday loops, 3:00 snap, marks from 4:00, futures about 3:00, equities 4:00, evaluated prices mid-to-late afternoon, CDX later). Venue clocks are flagged "(approximate)", as in the chapter.
- Honesty: Illustrative, times from the chapter. OK.
- Legibility: the dashed snap line passes behind the loop boxes (checked in a zoomed crop), no overlaps. Two labels were below the 8 pt house minimum ("(approximate)" 7.2, "marks, disputes, EOD risk" 7.6); both raised to 8.0 and still fit.
- Embedding: closes the 3B.1 time-slot tour. OK.

### Figure 3-B.3, ch03b_year_clocks: PASS after caption, font and halo fixes
- Correctness: ring geometry verified (weekend = last two of seven sectors; month-end = days 28-31; quarter-ends at day 90, 181, 273, 365; 20 Mar and 20 Sep rolls at the right angles; eight FOMC ticks at the verified dates; 6:45-8:30 and 4-6 p.m. wedges; 3:00 snap at 225 degrees).
- Honesty: the caption called the rings "day, week, month, quarter and half-year" but the figure's fourth ring is the year, which carries the quarter-ends and rolls. Caption rewritten to match, and the FOMC claim now cites federalreserve.gov ("Illustrative, except the 2026 FOMC dates").
- Legibility: ring letters and day-of-month digits were 7.0-7.2 pt, and the violet hands struck through "F", "A" and a week letter. Letters are now 8.0 pt, drawn above the hands with a halo in the ring's face colour, so every letter reads cleanly. No label collisions.
- Embedding: after the month-and-quarter paragraphs it summarises. OK.

### Figure 3-B.4, ch03b_event_windows: PASS after caption fix
- Correctness: windows recomputed by hand with SIFMA business days (consent 22 Oct to 5 Nov, coupon 29 Oct to 13 Nov with Veterans Day skipped, grace 13 Nov to 13 Dec, RSA 27 Nov to 11 Dec). Intensity levels check: 4 x e^0.4 = 6.0; consent plus coupon 10.9; coupon alone 7.3; one-day spike on 13 Nov 24.2 (coupon plus grace); grace alone 13.3; grace plus RSA 29.6. Multipliers 1.5, 1.8, 3.3, 2.2 are right. Step function, red line at day 28.
- Honesty: assumed coefficients (0.4, 0.6, 0.8) are stated as assumed; Illustrative. Fixed: the caption wrote lambda(t) and plain-text x_k(t), e^beta while the axis and the chapter's formula use lambda^P; the caption now uses the chapter's math form, `$\lambda^{\mathbb{P}}(t) = \lambda_0 \exp(\beta^{\top} x(t))$`.
- Legibility: all labels clear of the line (the grace-alone collision was already fixed in the previous pass).
- Embedding: directly after the lambda^P paragraph. OK.

### Figure 3-B.5, ch03b_saks_calendar: PASS after caption fix
- Correctness: every date placed on the right day (see traces above); the zoom box spans 24 Nov 2025 to 20 Jan 2026 and contains the two ABL steps and the petition; December interest drawn as the whole month because the dossier has no date, and the label says "date: see indenture".
- Honesty: source given, 47.5 flagged as a Debtwire indication not a TRACE print. Fixed: the caption said the zoom ends 19 January, the axis (and the dashed box) end 20 January; caption now says 20 January.
- Legibility: no collisions or clipping.
- Embedding: after the second-year paragraph. OK.

### Figure 3-B.6, ch03b_wall_interval: PASS, no changes
- Correctness: S(t) = e^(-t/20) falls monotonically; S(20) = 36.8% (caption "about 37%"); S(30) = 22.3% (caption 22%); area under the curve to day 30 = 15.54 days (caption 15.5); the vertical drop at day 30 shows the outside-date cliff. Top strip matches the scene (10:14 day 0, deal day 19, 8-K 7:05 and lift 7:40 on day 20, outside date day 30).
- Honesty: Illustrative, points to the box. Legibility: clean. Embedding: after the cleansing paragraph. OK.

### Figure 3-B.7, ch03b_jtd_hedge: PASS, no changes
- Correctness: N = F(P-R)/(1-R): $8.0mm at 88 and $5.0mm at 70 for R = 40; R = 30 and 50 lines are right (5.7 and 4.0 at 70); extra bet 2.0 and 5.0; face-hedged default P&L = F(1-P) = $1.2mm at 88 and $3.0mm at 70 whatever R; lines monotone and drawn only for P at or above R.
- Honesty: Illustrative, formula stated. Legibility: callouts clear of the thin lines. Embedding: right after the JTD box. OK.

### Figure 3-B.8, ch03b_hit_rate_se: PASS after script, caption and placement fixes
- Correctness: SE(40) = 7.9 points, band 39.3% to 70.7% (caption 39% to 71%), 2 SE = 5 points at n = 4p(1-p)/0.05^2 = 396 (caption "near 400"), SE(400) = 2.5; band narrows and SE falls monotonically.
- Honesty: the caption gave no source or Illustrative label; it now ends "Illustrative: computed from SE = sqrt(p(1-p)/n) with p = 0.55, the box's example."
- Legibility: the left panel's band curves left the frame at 10 views (y limits 25-85 against a band of 23.6-86.4); y limits widened to 20-90 so both curves are fully visible. Right panel labels do not collide.
- Embedding: the figure sat one paragraph after the SE box; moved to sit directly under the box, before "So a first-year analyst cannot be measured on outcomes."

## Files changed
- tools/figures/ch03b.py (axis label, four font sizes, halo on ring letters, y limits), re-run: all eight PNGs regenerated in assets/figures/.
- book_src/03_ch03b_your_first_year_on_the_desk.md (captions of 3-B.1, 3-B.3, 3-B.4, 3-B.5, 3-B.8; Figure 3-B.8 moved under its box). No caption text outside those five was touched.

## Left as is, for the record
- Violet and red as categorical colours (slots 7 and 8) with slots 3-6 skipped: deliberate and documented in the script header.
- Figure 3-B.2 sits after the 4:00-6:00 p.m. paragraph, after Figure 3-B.1 although it summarises the whole day; moving it would renumber both figures, and the order of appearance is correct as is.

<!-- STATUS: COMPLETE -->
