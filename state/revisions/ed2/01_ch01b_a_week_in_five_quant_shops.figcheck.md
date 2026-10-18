# Figure check: Chapter 1-B (ed2 U4)

Checked against tools/figures/style.py (house style), tools/figures/ch01b.py (the drawing code), the chapter text, and state/research/life_quant_shop_daily_life.md (Senate PSI figures). Every PNG was opened and viewed, before and after the fixes. The script was re-run (`python3 tools/figures/ch01b.py`) and all five PNGs are regenerated, each under 500 KB.

## Whole-set findings

- Correctness: every number was recomputed from the chapter's own formulas (DTS, CS01, returns, ranks, the 2x2 table) and all match the chapter. None of the five figures draws a payoff, a waterfall or a distribution, so there are no strike kinks, tranche sums or tail shapes to check. The only stacked bar (Figure 1-B.2, long Kestrel plus CDX) sums to the short leg, as the chapter says.
- Real-data claims: all trace to the Senate PSI report as logged in the research file: $161mm booked vs $593mm at mids over 12-16 March 2012 (p.5), $690mm peak collateral disputes (p.6), the Controller's $719mm to $1.2bn (p.98), and the 6 bp index tolerance (p.112 n.675). The rule names (FINRA 6730, 5310; 17 CFR 240.15c3-5) are as the chapter cites them. No real number is invented.
- Embedding: all five files exist; numbered 1-B.1 to 1-B.5 in order; same `![Figure N-B.k: ...](assets/figures/...)` form as 3-B and 8-C; each sits beside the paragraph or box it illustrates.
- Style: no aqua, yellow or magenta; no twinx; no in-image titles (the two panel headings in Figure 1-B.4 are panel labels and were kept); text is ink; direct labels throughout (the legends in 1-B.1 and 1-B.2 are backed by labels or values); BLUE, ORANGE and VIOLET keep the roles declared in the script docstring across the chapter.
- Text size: the denser figures used 7.5 pt text, below the house 8 pt floor for annotations. Raised to 8 pt in Figures 1-B.1 and 1-B.3 and re-viewed; no collisions resulted.

## Figure 1-B.1, ch01b_five_clocks: PASS after fixes

- Correctness: all 24 ticks and the Tuesday span were checked against the chapter's times (7:40, 8:00, 11:10, 11:25, 4:30; 5:55, 7:15, 9:30 to 11:00, 2:40, 5:10; 6:10, 8:00, 11:00, 1:30, 2:30; 7:40, 9:00, 12:15, 3:45, 4:20, 4:40; 6:45, 10:40, 10:52, 11:30, 5:45). All correct. Friday's restricted band starts at 10:52 and runs off the right edge with an arrow, as the caption says. Counts match the caption: 4 blue, 6 orange, 14 grey plus the grey span.
- Honesty fix: the legend said "set by a rule", but several blue ticks (11:25 rollback, Wednesday 8:00 amber line, Thursday 9:00 reminder) are story events that a rule makes someone document or schedule, not times a rule sets. Legend changed to "tied to a rule" and the caption to "a rule is behind only a few of the ticks (blue)". The caption's sourcing ("Illustrative" scene times; rule citations for blue; section sources for orange) was already right.
- Legibility fix: event labels 7.5 pt to 8 pt (also the Friday band label). Re-viewed: no overlaps (tightest gap is Monday's 7:40 and 11:10 labels, about 20 px).
- Embedding: after the Cold Open's closing paragraph, which introduces the five rooms. OK.

## Figure 1-B.2, ch01b_dts_drift: PASS after fixes

- Correctness: recomputed 72,576 / 110,160 / 71,604 / 70,189 / 97,952 / 87,906 (chapter: 72,600 / 110,200 / 71,600 / 70,200 / 98,000 / 87,900). The CDX piece (17.7k) is the gap, as the chapter says ("sized to the DTS gap and no larger"). Net-short labels: 38k (52%, "short half a leg" in the chapter) and 28k (40%, "about 40%"). CDX protection sold is long market, so it is correctly stacked on the long side.
- Style fix: the value labels were white 7.5 pt text inside the bars (white on orange is about 3.2:1, and the house rule is ink text). They now sit in ink above each bar; the stacked bar shows its total (87.9) and the CDX piece is in the legend entry ("CDX HY protection sold (+17.7)"). Net-short annotations moved up to clear them; y-limit 150 to 158.
- Caption matches (about 40% of a leg; price 90 to 78; spread 600 to 1,400 bp; spread duration 3.4 to 2.3) and says Illustrative with the DTS formula. The chapter text points to the figure by number.
- Embedding: right after the paragraph that introduces the drifting ruler. OK.
- Not changed: the y-axis unit is "thousands" of the chapter's unitless DTS figures, which is what the chapter itself prints.

## Figure 1-B.3, ch01b_trace_cascade: PASS after fixes

- Correctness: -9.0% (71/78-1), +9.2% (77.5/71-1), -1.3% (77/78-1), +0.6% (77.5/77-1), ranks 206 to 41 (165 places) all match the chapter's Math, Gently box. Column order matches the text: 71 reported Monday; the Tuesday-morning run sees it; cancel and as/of re-report Tuesday evening; the Wednesday-morning run sees the 77; the back-test is owed the version known Tuesday. The orange (wrong) and blue (corrected) roles match the chapter's other figures.
- Legibility fixes: box text and the "moves 165 places" note 7.5/7.6 pt to 8 pt; the Tuesday-evening tape box text was re-broken so it no longer touches the box edge. Re-viewed: nothing clipped, all labels direct.
- Accepted: the grey tape-to-archive arrow in the Tuesday-evening column crosses the model lane's horizontal arrow. Any vertical path between those two lanes in that column must; it is a line crossing, not a text collision, and the weights and colours keep it readable.
- Caption matches the image and is marked Illustrative with the Rule 6730 mechanics. Embedding: after the return-as-ratio box, before Arjun's follow-up question. OK.
- Observation for the text editor (not changed here, outside this task): the Math, Gently box and this figure both have the Tuesday-morning run seeing "Tuesday +9.2%" (Tuesday's price near 77.50) as well as Monday's -9.0%. A model run in the morning can only see Tuesday's return if Tuesday's trades have already printed; consider "Tuesday's first trades" or running the model after the open.

## Figure 1-B.4, ch01b_tolerance_senate: PASS after caption fix

- Correctness (left, illustrative): CS01 = 6,000,000 x 0.78 x 2.3 x 0.0001 = $1,076 (chapter: about $1,080), so 6 bp = $6.5k; the 79 mark is 1.25 points = $75,000, about 70 bp (69.7 before rounding; chapter: "about 70 bp"); index position 6 bp x $50,000 = $300k. All match.
- Correctness (right, real): $161mm booked vs $593mm at mids, 12-16 March 2012 (p.5); $690mm (p.6); $719mm to $1.2bn (p.98). Each matches the research file and the chapter, and the bars are scaled from zero.
- Honesty fix: the caption sourced only the right panel; the left panel's "6 bp" is itself a real figure (the report's index tolerance, p.112 n.675) applied here to the chapter's invented positions. Caption now says so: "Left: the 6 bp tolerance is the report's (p.112, n.675); applying it to the chapter's positions is Illustrative, with CS01 = ...".
- Legibility and style: no collisions, 8 to 8.5 pt text, one x-axis per panel, no y-axes, ink text; the panel headings state which panel is illustrative and which is real. No change needed. Embedding: after the paragraph on two prices for one position, which follows the tolerance box. OK.
- Observation for the text editor (already in the figures log, not changed here): §1B.4 says a mark is "a choice made inside the bid-ask spread", but the 79 mark is above the 78.50 offer, so it is outside the quoted spread; this figure shows it as 70 bp from mid and does not claim otherwise.

## Figure 1-B.5, ch01b_silence_odds: PASS after caption fix

- Correctness: 50/1,000 = 5.0%; 40/135 = 29.6%; ratio 5.9 (shown as "x 6", as the box says); odds 40:95 against 50:950 is exactly 8x (shown as "odds x 8"); the uniform "no comment" leaves 5.0% (x 1). All match the box's 2x2 table.
- Honesty fix: the image shows "odds x 8" but neither the box nor the caption mentioned odds. Caption now reads "(about 30%, against a 5% prior: the odds rise eightfold, from 50:950 to 40:95)". The remaining caption text already matched and is marked Illustrative with the table's counts.
- Legibility and style: single series in BLUE on a grey full-width track, ink labels, 8 to 8.5 pt, nothing clipped or colliding. No change needed. Embedding: right after the conditional-probability box, before Kaz's last email. OK.

## Not figures, noted

- The optional placeholder comment `<!-- FIGURE (optional): ch01b_alert_history.png ... -->` (after the 212-fires paragraph) was left in place on purpose, as the figures log says: only 212 fires and 2 actioned are given, and the rest of the split would be invented. No build tool in tools/ reads these comments.

## Files changed

- /home/user/quant-credit-book/tools/figures/ch01b.py (fonts to 8 pt, legend word, Figure 1-B.2 value labels, Figure 1-B.3 text break, docstring sentence)
- /home/user/quant-credit-book/assets/figures/ch01b_five_clocks.png, ch01b_dts_drift.png, ch01b_trace_cascade.png (and the other two re-saved unchanged)
- /home/user/quant-credit-book/book_src/01_ch01b_a_week_in_five_quant_shops.md (three caption edits: Figures 1-B.1, 1-B.4, 1-B.5)
<!-- STATUS: COMPLETE -->
