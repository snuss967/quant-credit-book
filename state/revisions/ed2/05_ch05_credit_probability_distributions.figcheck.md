# Figure check: Chapter 5 (ed2), Figure Checker Edition 2

Checked: six embedded figures (ch05_skew_vs_pd, ch05_two_worlds_mixture, ch05_pair_two_spikes, ch05_recovery_beta_shapes, ch05_serta_recovery_fork, ch05_carvana_stack). Five are drawn by tools/figures/ch05.py; ch05_pair_two_spikes is drawn by tools/figures/ch05_rv.py (checked too, since it is embedded). Both scripts re-run clean, every in-script assert passes, every PNG was viewed (and zoomed where text was tight), all are under 125 KB.

Method: read the house-style docstring; read each drawing function; recomputed the numbers by hand where the caption leans on them; compared every caption and label to the chapter text, to the dossiers (state/research/case_carvana_svb_wolfspeed_capital_structure.md, state/research/case_courts_as_regime_variables.md) and to Schmid p.103 (source_pdfs, 40.07 / 27.50 confirmed).

Embedding (all six): syntax `![Figure 5.n: ...](assets/figures/ch05_x.png)` correct, files exist, numbered 5.1 to 5.6 in document order, each with a blank line either side and a pointer sentence or the paragraph it illustrates immediately before it (5.1 at line 185, 5.2 at 231, 5.3 at 265, 5.4 at 604, 5.5 at 761, 5.6 at 773).

## Figure 5.1, ch05_skew_vs_pd: PASS after one fix
- Correctness: skeleton -(1-2q)/sqrt(q(1-q)) is right; zero at q = 1/2, positive above it, -1/sqrt(q) dashed as the slogan; the labelled points (A -45, BB -11, B3 -4.7, CCC -2.3, Carvana +1.3 at q = 0.77) match the chapter and the script asserts them.
- Honesty: caption says Illustrative, names the formula, and flags 0.77 as a risk-neutral, premia-included number; matches the §5.2.4 text.
- Legibility: the dashed q = 1/2 line ran through the legend text ("q(1-q))").
- Fix: legend moved left of the q = 1/2 line (bbox_to_anchor 0.865). Re-viewed: clean.

## Figure 5.2, ch05_two_worlds_mixture: PASS after one fix
- Correctness: mixture CDF = 0.96 N(7%, 4.1%) + 0.04 Beta-default leg R/0.92 - 1; the script reproduces the table's whole mixture column (1 in 29, VaR -2.2%, -83%, ES -92%, mean 4.5%, vol 14.4%, skew -5.1, kurtosis 28, 70%). The 15-point loss region starts at -15/92 = -16.3%, which is where the shading starts. Default plateau about 1 in 1,000 per 2-point bin, as captioned.
- Defect: the bins stopped at +20%, so the survival hump (and the Gaussian) ended abruptly at about 1 in 400 while the axis ran to +28%, hiding the right tail.
- Fix: bins now run to +30%; both curves taper off the bottom of the chart. Caption needed no change.
- Honesty: Illustrative, inputs stated, Schmid p.103 moments verified. "Rarer than 1 in 29,000" is true (see flag 1).

## Figure 5.3, ch05_pair_two_spikes: PASS after a typographic fix
- Correctness: -60 x (0.96 - 0.40) = -33.6 and 39 x (0.90 - 0.40) = +19.5; default odds 3.5%/0.6 = 5.8% and 6%/0.6 = 10%; both-default spike at -14.1 (0.6%) and both-survive 85% check; wobble s.d. $2.18mm and $2.15mm and thesis drift +$1.19mm recompute. Seeded run prints P(< -24) = 3.8% for the Beta panel, matching "about 4%" in the caption (5.3% in the fixed panel, which the caption does not claim). Output is byte-identical on re-run.
- Honesty: Illustrative and fictional composite, stated.
- Legibility: no collisions. Labels "-$24mm" and "-$33.6mm" used a hyphen; changed to a true minus to match the caption and tick labels (tools/figures/ch05_rv.py, two strings). Re-viewed.

## Figure 5.4, ch05_recovery_beta_shapes: PASS after a script fix and a caption fix
- Correctness: method-of-moments pairs (0.87, 1.30), (0.93, 0.40), (1.68, 2.33) asserted; the third is rescaled correctly to [0, 1.2] (mode about 0.41, density about 1.30). Blue is bounded at par (b > 1) and unbounded at 0; orange is unbounded at both ends.
- Defect (image): the orange curve passed through the "par" of the label "density -> inf at par".
- Fix: label moved to the left of the spike (anchored at 0.955).
- Defect (caption): "same spread" (27.5 vs 30 points) and "the first two curves run off the chart at the ends of the shelf" (the first is unbounded only at zero).
- Fix (chapter, one Edit): "a similar spread"; "the first curve is unbounded at zero while the second is unbounded at both ends of the shelf".
- Honesty: Schmid p.103 verified; the 50.21/26.46 family-recovery moments trace to Moody's LGD methodology (Aug 2006), marked VERIFIED in the advisor brief; the 70/30 book is labelled Illustrative. Colors: BLUE, ORANGE, AQUA in order, all three direct-labelled.

## Figure 5.5, ch05_serta_recovery_fork: PASS after two script fixes and a caption fix
- Correctness: bars 73.7 to 100 and 0.6 to 2.4 match the plan range in the text; 73.7/2.4 = 30.7, so "a factor of thirty or more" holds. Timeline dates (22 Jun 2020, Jan 2023, 28 Mar 2023, 31 Dec 2024, 10 Nov 2025, 7 Jul 2026) and amounts ($200mm, about $875mm, $261.13mm plus 9% from 22 Jun 2020) match §5.6.2 and the dossier.
- Defect (honesty): the row "Court's value, 7 Jul 2026" implied a 2026 mark. The dossier gives the 25 cents as the court's valuation as of 22 Jun 2020 (the date the award is measured from); 7 Jul 2026 is the ruling date. Also the x label said "first-lien claim" while the 39 is a second-lien price.
- Fix: row relabelled "Court's value, as of 2020"; annotation now "excluded loans valued at 25 cents (ruling of 7 Jul 2026)"; axis label "Cents per dollar of claim".
- Defect (caption sourcing): the caption credited Proskauer for the 74/39 exchange prices; the chapter text and dossier give the Fifth Circuit opinion and the Paul Weiss memo (10 Jan 2025), with Proskauer for the $200mm/$875mm. It also said "other dates as in the Docket Diary", but 22 Jun 2020, Jan 2023 and 10 Nov 2025 are in §5.6.2 text, not the Diary.
- Fix (chapter, caption): description of the 25 cents now says "as of the 2020 exchange (ruling of 7 July 2026)"; sources re-attributed; "other dates as in §5.6.2 and the Docket Diary of §5.6.1".
- Legibility: no collisions after the fix; the 10 Nov 2025 label sits about 5 px from the 7 Jul 2026 stem but does not touch it.

## Figure 5.6, ch05_carvana_stack: PASS after four script fixes
- Correctness: marks 44.8, 53.8, 74.0, 77.7, 84.7 at the five quarter-ends, the 37 to 48 quote on 18 Nov 2022, and the per-series ratios 76.8, 66.6, 64.9, 89.3 plus the 2025s' 85 cash tender all match the dossier (sections 1.2 and 1.3) and the chapter. Events 22 Mar (offer), 2 Jun (terminated, $500mm minimum unmet), 17 Jul (TSA, over 90%), 1 Sep (settled) match the dossier timeline. Cash tender is drawn in gray and labelled, so it is not read as new secured par.
- Defects (image): (a) the leader line for "bond in the cold open's chair" struck through the "66.6" value label; (b) the 22 Mar stem ran through "53.8"; (c) gridlines ran through the "A year earlier" note; (d) the 2 Jun and 17 Jul labels spilled past the axes into the gutter; the y spine ran to 135 with ticks only to 100.
- Fixes: chair label moved inside its orange bar (ink on orange, rotated, no leader); value labels and the 99.5 note get a white backing placed under the line and markers (zorder 3.5, so the series line stays whole); event labels shortened to "2 Jun: exchange fails" and "17 Jul: deal signed" (the "over 90%" and the "(the decision)" tag are in the caption and chapter text); left spine now stops at 100.
- Honesty: caption cites the 10-K and 10-Qs, Bloomberg via American Banker, the 8-Ks and the Q3 10-Q, and says which numbers are computed; matches the chapter's own citations.

## Flags for the editor (not changed)
1. §5.1.4 table, Gaussian column: "1 in 29,000" for losing 15 points reproduces only with a zero-mean N(0, 4.1%); with the table's own mean of 7% the chance is about 1 in 160 million. Figure 5.2 says "rarer than 1 in 29,000" (true either way) and never prints the Gaussian's own number. The table row is the thing to fix, and it is outside the figures. (Already noted in the figures log.)
2. The plan recovery range 73.7 to 100 / 0.6 to 2.4 is cited to Norton Rose Fulbright (Q3 2023) in the chapter; the dossier backs the 0.6 to 2.4 against Skadden and gives "about 75%" for the low end of participants. Consistent with the chapter, but the NRF source itself was not re-opened here.
3. The "Jan 2023" dot sits at 15 January; the chapter says only "January 2023", so no day is claimed. If a date is wanted, the dossier does not give one.

## Files changed
- tools/figures/ch05.py (figures 5.1, 5.2, 5.4, 5.5, 5.6), tools/figures/ch05_rv.py (figure 5.3 minus signs)
- assets/figures/ch05_skew_vs_pd.png, ch05_two_worlds_mixture.png, ch05_recovery_beta_shapes.png, ch05_serta_recovery_fork.png, ch05_carvana_stack.png, ch05_pair_two_spikes.png (regenerated)
- book_src/05_ch05_credit_probability_distributions.md (Figure 5.4 and Figure 5.5 captions only)
<!-- STATUS: COMPLETE -->
