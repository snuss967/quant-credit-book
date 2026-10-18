# Ch 10 figure check (Edition 2)

Chapter: book_src/10_ch10_trend_and_time_series_momentum.md. Script: tools/figures/ch10.py (re-run from the repo root, all five PNGs regenerated, 102-143 KB). Checked against the house style in tools/figures/style.py. Caches in tools/figures/data/ re-read to confirm every number quoted in the captions.

Numbers confirmed from the caches: 534 days with a full 12-month window, spread rule short 150 days, return rule short 13 (2 Oct 2024 to 15 Oct 2026); DTS notional 0.74 on 7 Apr 2025, EWMA 0.61 on 4 Apr (0.6108) and 0.70 on 30 Jun; 84 bucket-quarters, through-origin vol = 0.227 x OAS, log-log slope 0.86, R^2 0.62; BAA10Y peaks 6.16 (4 Dec 2008), 4.31 (23 Mar 2020), 2.42 (1 Jul 2022), 2.02 (7 Apr 2025). All match the captions and panel labels.

## Figure 10.1, ch10_carry_hurdle (s10.1.2): PASS after fixes
- Correctness: hurdle = s_bar x 100 / D: 4.5% / 4 = 112.5 bp and 1.0% / 7 = 14.3 bp, both dots on their lines. Right panel: return rule short iff 12-month change > 252-day mean OAS / 4, which is the chapter's M < 0 condition. Counts 150 and 13 reproduce.
- Honesty: caption cites BAMLH0A0HYM2 with the dates, says D = 4 is assumed, and marks the left panel Illustrative.
- Legibility: the "both rules short" shading was a sliver above the hurdle line that could not be seen (13 days). Fixed: each day is now shaded from zero up to the curve, light where only the spread rule is short, darker where both are, drawn above the grid. The dark block at March-April 2025 is now visible and matches the legend swatch.
- Embedding: syntax, file and pointer sentence correct, placed after the carry-hurdle paragraph.
- Style note (left as is): violet/green for HY/IG are chapter role colours, kept distinct from the blue (spread) / orange (return) roles of the right panel.

## Figure 10.2, ch10_dts_vol_scaling (s10.3.1): PASS after fixes, one open text conflict (below)
- Correctness: quarterly vol of daily OAS changes x sqrt(252) against mean OAS, 7 buckets x 12 quarters; the line is drawn through the origin (slope 1 in log-log) with beta from the cache. Right panel notional = 1 / forecast, normalised to 2 Apr 2025; the DTS notional is s(2 Apr)/s(t), so beta cancels and 342/461 = 0.74 is reproduced. EWMA centre of mass 60 (delta = 60/61) is right. Dates of the gap days correct (2, 3, 4, 7 April).
- Honesty: the cloud is sub-proportional (slope 0.86, R^2 0.62), so "roughly proportional" was right but the numbers were not given. Fix: added "R^2 0.62; log-log slope 0.86, a little under proportional" to the caption. Source and series IDs cited; derived statistics only (ICE licence, see below).
- Legibility: the "2 Apr: OAS 3.42%" label ran across the left spine into the tick-label area. Fixed: now uses mark_event, to the right of the line in the empty top band. Removed the x grid on the log panel (house style is y-grid only); "x" in the legend replaced by the multiplication sign.
- Embedding: fine. The figure sits after the three-consequence list that it illustrates; the pointer sentence is at the end of the last item.

## Figure 10.3, ch10_trend_smile (s10.6.1): PASS after fixes
- Correctness: E[r_TF | r] = r [2 Phi(rho r / (sigma sqrt(1 - rho^2))) - 1] is the chapter's formula (and I re-derived it: M | r is normal with mean rho r, sd sqrt(1 - rho^2) in standardised units). Even, U-shaped, flat at rho = 0, tends to |r|, small-move parabola coefficient sqrt(2/pi) rho / sqrt(1 - rho^2) correct. The script asserts the closed form against a 2-million-draw simulation. Right-panel points sit exactly on the +|r| and -|r| branches.
- Honesty: caption says Illustrative, model named, seed fixed.
- Legibility: the top-left note nearly touched both straddle lines; rewritten as three short lines. In the right panel "closed form, rho = 0.25" sat on the blue curve; moved below it, and the "bin means" note moved clear of the curve.
- Embedding: after the paragraph with the parabola and the Fung-Hsieh / Hamill reading, pointer sentence present.

## Figure 10.4, ch10_whipsaw_capture (s10.6.2): PASS after fixes
- Correctness: capture = (T - 4L)/T for T >= 2L (chapter), 2L/T - 2 for L < T <= 2L, 0 for T <= L. I re-derived the middle piece (four legs for T/2 < L <= T give 4L/T - 4 of d, i.e. 2L/T - 2 of 2d); the script checks all three pieces against brute-force integration and asserts the 70% and -20% values. Break-even dots at T = 4L (2, 6, 24); curves start at -100% for L = 0.5, T = 1 and touch -100% at T = 2L.
- Honesty: the caption said "only a two-week lag breaks even" at T = 2, but the figure shows the 12-month signal at 0% there too (it never flips), and the lead claim "loses on the round trip" fails for T <= L. Fixed the caption: adds "unless the V is so short that the signal never flips", panel tags (left)/(right), "the 12-month signal never turns and earns nothing, and even a two-week lag only breaks even", and the T <= L piece.
- Legibility/style: blue/orange meant long/short in the ribbons but 3-month/12-month in the lines, dots and right panel. Fixed: long stretches are neutral gray, the short stretch is a tint of the signal's own colour. The end dots touched the text labels; dots moved inside the ribbons.
- Style note (left as is): the 2-week lag line is violet, which is HY in 10.1 and 10.2; the figures never share a legend, so no confusion.
- Embedding: after the whipsaw-arithmetic paragraph, pointer sentence present.

## Figure 10.5, ch10_episodes_baa_spread (s10.7): PASS after fixes
- Correctness: peaks and dates verified in the cache (above); windows A 2007-07 to 2009-12, B 15 Feb to 30 Jun 2020, D 15 Feb to 30 Jun 2025 match the case studies; C was shaded only to 31 Oct although the case study and the SG Trend figure are calendar 2022. Fixed: window now 1 Jan to 31 Dec 2022.
- Honesty: caption cites FRED BAA10Y, says it is a long-history proxy and why; the SG Trend numbers match the chapter (+20.9%, +6.24%, +27.4%, -4.9%) and the cites named in the caption (Cambridge Associates, Hedgeweek, SG Prime Services) are the ones in s10.7.
- Legibility: the 12-month scale bar at 1.3 almost touched the line in panel D (BAA10Y dips to 1.4 in autumn 2024). Fixed: bars moved to 0.95 and 0.62, y limit lowered to 0.35. The window swatch in the legend now has the same tint as the panels.
- Embedding: after the intro paragraph that precedes Case Study A, pointer sentence present.

## Embedding, all figures
Five embeds, syntax `![Figure 10.n: ...](assets/figures/ch10_*.png)` as in other chapters, files exist, numbered 10.1 to 10.5 in order of appearance (lines 80, 191, 364, 387, 403). `python3 tools/check_book.py --file book_src/10_ch10_trend_and_time_series_momentum.md` reports OK.

## Edits made
- tools/figures/ch10.py: fills and zorder in 10.1; label and grid in 10.2; text placement in 10.3; ribbon colours and labels in 10.4; scale-bar position, ylim, window for C and swatch in 10.5. All five PNGs regenerated and re-viewed (full view plus zoomed crops).
- Chapter captions only: Figure 10.2 (R^2 and slope added) and Figure 10.4 (rewritten as above). No other chapter text touched.

## Open items (not fixed, for the reviser or the owner)
1. TEXT CONFLICTS WITH FIGURE 10.2 (prose, left untouched because it is outside figure scope and the file is being revised elsewhere). The real April 2025 data show the 60-day EWMA cutting the constant-risk notional harder and sooner than the DTS forecast (0.61 against 0.77 by 4 April; 0.70 against 1.16 at end June). Three passages say the opposite: the Annotation after the Paleologo source extraction in s10.3.1 ("A DTS-based forecast reacts at once, while an EWMA forecast needs weeks of realized moves to catch up", line 195), the Ways This Blows Up box in s10.3.2 ("A 60-day EWMA had about three new observations", line 207) and the code-explanation paragraph near line 568 ("needs weeks to catch up"). The caption states what the data show. Suggested repair: keep the conclusion (use the max of EWMA, DTS and a floor) but say that after a gap a short EWMA is quick to cut and slow to rebuild, while DTS cuts less and re-risks sooner.
2. ICE licence. Every ICE BofA series on FRED carries "reproduction prohibited without ICE's written permission". The figures plot derived statistics only and the caches hold no raw OAS history; the owner should still decide whether citing the series IDs is enough for publication.
3. Cosmetic, left as is: the smallest text is 7.6 pt in the four-panel Figure 10.5 (each panel is about 1.6 in wide, so larger text overflows).

<!-- STATUS: COMPLETE -->
