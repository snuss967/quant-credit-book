# Figure check: 00_02 How to Use This Book (ed2)

Checked against tools/figures/style.py (house style), the script tools/figures/00_02_.py, and the chapter text. The script was re-run before any edit and reproduced all five PNGs byte-for-byte (seeded), then re-run after the fixes below. Every PNG was opened and viewed before and after the fixes. All five files are under 260 KB and no figure embed in this chapter points at a missing file (tools/check_figures.py reports missing files only for other chapters: 09b, 13b, 17b, 18b).

## Figure 00_02_.1, 00_02__dependency_map (section 0.2): verdict PASS after fixes

- Correctness. Every blue edge matches the primer table of section 0.2 (4-B to 5, 8, 8-D, 8-B, 8-C, 24, 19; 7-B to 8, 9-12, Part IV; 6-B to 6, 23, 12-C, Part IV; 12-B to 12-C and Part IV, drawn heavy). The three violet edges match the "second generation" paragraph (8 to 8-D, 8-B to 8-D, 8-B to 8-C, 3B.4 clocks to 3-B). The orange route numbered 1 to 9 is exactly 1-B, 4-B, 5, 8, 8-D, 8-B, 8-C, 24, 28, as in sections 0.2, 0.4 and 0.9. Part tags (II, III, VI, VIII, V, IV, I) match the book's Part table.
- Honesty. The caption cites the table and the section 0.9 path and says no market data. One overclaim: the legend said "a module imports another chapter's module", but two of the violet edges start at a section (the section 8.4 rulers, the section 3B.4 clocks), not at a module. Legend and caption reworded.
- Legibility. No collisions. Smallest text raised from 6.6 pt to 7.0 pt; a dead invisible label (alpha 0) removed from the script.
- Embedding. Placed right after the primer table, before the paragraph that discusses the second generation. That paragraph still said "The figure the map will become draws these as arrows", stale now that the figure exists.
- Fixes made. Legend text now "a module builds on other work in the book (second generation)". Caption: "three second-generation modules (violet) build on work from elsewhere in the book". Chapter sentence now reads "The figure above draws these as arrows, dashed and in violet, because that is what they are."

## Figure 00_02_.2, 00_02__volatility_tax (section 0.3): verdict PASS after fixes

- Correctness. Simulated log price is (mu - sigma^2/2) + sigma Z with mu 5%, sigma 40%, so the exact mean is exp(0.05) = 1.051 and the median exp(-0.03) = 0.970 (simulation 1.050 and 0.969). Share below 1.00 is 0.531 (exact Phi(0.075) = 0.530), matching "53%". Right tail is the long lognormal tail on the right, as theory demands; histogram peak near 0.83 matches the lognormal mode. Ten-year lines are exp(0.5) = 1.65 and exp(-0.3) = 0.74, matching the labels and caption.
- Honesty. Caption says "Illustrative", names the seed, the path counts, and which lines are exact. Matches the chapter's box (1.051 and 0.970).
- Legibility. Three defects fixed. (1) The "median 0.97" label ran across the left spine; labels are now two-line and clear of the axis. (2) The log panel clipped the extreme paths (the 40 paths span 0.04 to 27 while the axis was 0.1 to 25), which hid exactly the tail that drags the average up; limits widened to 0.035 to 45 and the script now asserts nothing is clipped. (3) The note "53% of paths end below 1.00" overlapped bars and never said what the darker bars were; it now reads "(darker bars)" and sits clear of the histogram. One y-axis per panel, blue for average and orange for median in both panels, labels are ink.
- Embedding. Sits right after the "volatility tax, at all three tiers" box, before "Tier 3 is building". Syntax correct, file exists, number 2 in order. Caption unchanged.

## Figure 00_02_.3, 00_02__seat_paths (section 0.4): verdict PASS after fixes

- Correctness. Station sequences checked line by line against the seat table. Seat 1 (1-B, Part I, 2-B, 4-B, 3-B, 8, 8-B, 8-C, Part V, then back to 7-B), seat 4 (1-B, 4-B, 6-B, 7-B, 8, 8-B, 8-C, 22, Part VI, 27), seat 3 (1-B, Part I, 4-B, 4-C, 5, 6, 6-B, 7-B, 12-B, 12-C, 8-D, Part IV, spur 25) and seat 2 (1-B, Part I, 4-C, 5, 6, 6-B, 7, 7-B, Part III, Part VIII, 12-B, Part IV). Interchange rails: 4-B on seats 1, 4, 3 (not 2); 6-B on 4, 3, 2 (not 1); 12-B on 3 and 2; 7-B and 1-B on all four, so "7-B is on all four" is true. Hours 180-220, 160-200, 210-250, 230-280 match. Colors follow seat number in fixed order (blue, orange, aqua, yellow); slots 3-5 are direct-labelled by name block and numbered badge.
- Honesty. Source cited (the seat table); caption says stations and hours are as listed there and that left to right is reading order, not page order. The figure repeats that note.
- Legibility. The "4-D Getting the seat" heading touched the right edge of its box; box widened. Module names raised from 6.4 pt to 7.0 pt, and the 6.9 pt labels to 7.0 pt. No other collisions.
- Embedding. After the seat table, before the "Several of the stations" paragraph. Correct, number 3.
- Fixes made. Box width and feeder start, font sizes. Caption unchanged.

## Figure 00_02_.4, 00_02__ninety_days (section 0.6): verdict PASS after fixes

- Correctness. Dates: day 0 is Sunday 28 June 2026 and day 86 is Tuesday 22 September 2026 (verified by calendar: 86 days later, and both weekdays correct). Strips: days 1-30, 31-60, 61-86 with 55-60, 55-60 and 45-55 hours, as in the table. Every chip's text and tier color matches the table (Tier 1: Ch 1, 2, 4, Ch 7 except 7.7, Ch 13 and 14; Tier 2: Ch 3, 4-B, 5, 6, 7-B, and sections 13.3, 13.8, 14.2; Tier 3: bondmath.py and the 6.11 engine; grey where the table states none). Gates on days 30 and 60 are stated in the table; days 87-90 hatched as "funded by sleep" is the chapter's own account.
- Honesty. One claim went beyond the source. The star and its label said "day 86: mock interview...", but the table only lists the mock interview or mock morning as the last item of the 61-86 stretch, and day 86 is also the first day on the desk, so a mock morning "on day 86" is not what the chapter says. The star now reads "ends the last stretch: mock interview, or a mock morning if you have the seat". The figure's own note (no day-by-day order inside a stretch) stays.
- Legibility. The text "Project 1: TRACE panel, Roll spread" ran to the edge of its chip; shortened to "Project 1: TRACE, Roll spread". Smallest text raised to 7.0 pt. Colors: blue, orange, aqua in fixed order for Tiers 1, 2, 3; aqua chips also carry the word "build"; key present.
- Embedding. After the 30/60/90 table. Correct, number 4.
- Fixes made. Chip text, star label, caption: "a mock interview or mock morning to close the last stretch" (was "on day 86").

## Figure 00_02_.5, 00_02__hand_history (section 0.6): verdict PASS after fixes

- Correctness. Left panel plots the checked rows of the chapter's hand_history listing: 50% said, 7 of 10 right (0.70); 70% said, 2 of 3 (0.667); 90% said, 9 of 12 (0.75); bars are sqrt(p(1-p)/n). The diagonal is perfect calibration. Right panel: band is 0.72 plus or minus 2 sqrt(p(1-p)/n): 0.54 to 0.90 at n = 25 and 0.63 to 0.81 at n = 100, both as in the chapter's box; the band clears 0.60 at n = (2 sqrt(p(1-p)) / (p - 0.60))^2 = 56.0, which the script computes rather than hard-codes. The band is clipped at 1.0 for very small n, which is right for a proportion. The band narrows monotonically with n, as it must.
- Honesty. Caption says "Illustrative", names the listing and the formula, and states the band rule. The chapter text agrees ("90% answers right about 75%, 50% answers about 70%"). The 70% bucket is labelled "too few to say", which is fair at n = 3.
- Legibility. Two defects fixed. The "right as often as he said" label was crossed by the diagonal; it is now below the line's start and reads "dashed: right as often as he said". The blue dotted line at 0.72 was unlabelled; it now carries "hit rate 0.72". One shared y-axis; blue only, the diagonal and the 0.60 line neutral and ink; text is ink.
- Embedding. Placed after the "confidence column" paragraph, which points to it ("Figure 00_02_.5 draws that table, and the band it sits in"). Correct, number 5.
- Fixes made. Label positions only; caption unchanged.

## Cross-cutting notes

- Numbering is in order of appearance, 00_02_.1 to .5 (lines 64, 106, 138, 227, 239 of the chapter). The label "00_02_" is the workflow's fallback tag for a front-matter file (the chapter's own sections are 0.1 to 0.11 and other chapters use "Figure 1.1"). I left it because the pipeline defines the label, and a rename touches five captions, one in-text reference, the script's finish() names and five file names. A text editor may prefer "Figure 0.1" to "0.5" and files 00_02__* renamed to match.
- Left as found, for the text editor: the log's observations (b) to (d) still stand: only two gates are drawn because the table states only two; the chapter says "150 and 185 hours" while the table's stretches add to 155-175; day 86 is both the last plan day and the first day on the desk.
- Files changed: tools/figures/00_02_.py, assets/figures/00_02__*.png (all five regenerated), book_src/00_02_how_to_use_this_book.md (three small edits: Figure 1 caption, the stale "will become" sentence, Figure 4 caption).

<!-- STATUS: COMPLETE -->
