# Ch 24 figure check (Edition 2)

Checked: five embedded figures (ch24_*.png) against tools/figures/ch24.py, tools/figures/style.py (house style), Listings 24.1-24.7 of Appendix F, and the chapter text. Math re-derived numerically from the chapter's own listings (loaded through the script's namespace). All five PNGs were viewed before and after the fixes (and zoomed where text was tight).

## Figure 24.1 (ch24_z_basis_vintage) -- PASS after fixes
- Correctness: PECS basis is 0 (to 1e-9) at every coupon; Z basis falls monotonically with price (+22 bp at 80, +10.2 at 88, -5.3 at 99, -18.8 at 111, -26.8 at 119), matching the +10/-5/-19 bp quoted in the log. JTD ratio (P-R)/(1-R) is linear, 0.80 at 88. Pass.
- Honesty: caption says "Illustrative: Listing 24.2" with parameters. One inaccurate claim: it said the Z basis crosses zero near 95 "because the CDS leg is ACT/360". Recomputed: the zero crossing is at price 95.1; the ACT/360 par spread is 297.4 bp, and a par semiannual bond has Z = 303.5 bp, so the -6 bp at par has two sources. Caption fixed to state the 297 bp vs 303 bp numbers.
- Legibility/style: no collisions. The 7.5 pt muted point labels ("4% coupon, 88") were raised to 8 pt ink-2. One y-axis per panel, BLUE = Z basis, ORANGE = PECS, direct labels present.
- Embedding: after the "vintage pattern" paragraph with a pointer sentence; file exists; numbering ok.

## Figure 24.2 (ch24_haircut_roe_mtm) -- PASS after fixes
- Correctness: ROE = (-b - phi(1-h))/h reproduces 4.4% (h 15%) and 2.4% (h 30%), decreasing and convex in h; MTM = d*D/h gives -45% at 150 bp widening for h = 15% and -22.5% for h = 30% (half), -90% / -45% at 300 bp. Caption numbers match.
- Honesty: "Illustrative: Listing 24.3", repo spread 40 bp, duration 4.5 stated.
- Legibility/style, fixed: (1) the "4.4%" and "2.4%" labels collided with the b = -150 curve, and the "repo spread 40 bp" note was crossed by the h = 15% dashed line; labels moved below-left / above-left of their points and the note moved to the empty right-middle. (2) Colour roles were inconsistent between panels (both worked points orange in (a), but h = 15% is BLUE in (b)); the h = 15% point is now BLUE and h = 30% ORANGE in both panels. (3) Hyphens replaced by true minus signs in "b = -150 bp" and the arrow note, matching the caption and tick labels.
- Embedding: after the "Mark-to-market" paragraph with pointer sentence ("Figure 24.2 plots both."); ok.

## Figure 24.3 (ch24_ctd_deliverable_prices) -- PASS after one fix
- Correctness: regime 1 prices 30.225 / 30.375 / 30.6 (3% / 5% / 8%), flat in maturity, swap pays 69.4 (8% 1.5y) or 69.6 (5% 22y); regime 2 (y = 11%, semiannual) prices fall monotonically with maturity for all three discount coupons, 95.95 for 8% 1.5y and 50.63 for 5% 22y (asserted in Listing 24.4), swap pays 4 or 49.4. The 30-year maximum maturity matches the chapter's SNAC list.
- Honesty: "Illustrative: Listing 24.4", event yield and recovery assumptions stated.
- Legibility/style, fixed: in panel (a) the two orange dots had no identity; added "8% due 1.5y" and "5% due 22y" labels. Coupon shades are sequential blue with direct labels in (b); the three flat lines in (a) overlap by design (0.4 points apart) and the annotation says so.
- Embedding: after the "Hovnanian blueprint" paragraph with pointer sentence; ok (the 30-year limit is explained in the paragraph just after the figure, a harmless forward reference).

## Figure 24.4 (ch24_auction_final_price) -- PASS after fixes
- Correctness: IMM 26.875 and the 1-point cap band; final price is non-increasing as net selling grows, non-decreasing as net buying grows; bids exhausted below -91 (price 0), offers exhausted above +51 (price 100), both matching the sums of the listing's limit orders (91 and 51 $mm). The 27.875 tab just left of zero is the listing's 28.0 crossed bid being capped at IMM + 1, i.e. the cap working in the base book. Right panel: rogue 30.0 bid for $10mm gives 30.0 uncapped and 27.875 capped for net selling of 0 to 10; the 28.0 step on the dotted line between -12 and -10 is correct.
- Honesty: "Illustrative: the eight-dealer book of Listing 24.5 ... with the rogue bid added" accurate. Caption tightened: the 30.0 vs 27.875 contrast holds "for net selling of up to $10mm".
- Legibility/style, fixed: the "(price 100)" label was struck through by the 32-point step; moved to the top of the panel. The "shaded: IMM +/- 1-point Cap" note (7.5 pt muted) and the "bids run out" label raised to 8 pt ink-2. BLUE = base book, ORANGE = rogue bid, legend in (b).
- Embedding: after the "game rather than a price discovery mechanism" paragraph with pointer sentence; ok.

## Figure 24.5 (ch24_successor_cliffs) -- PASS after fixes
- Correctness: panel (a) cliffs at 25% (orig 100 -> 50, new 0 -> 50, with 25.0% untouched and 25.1% split) and at 75% (all to the new entity, "75% or more"), per Listing 24.7. Panel (b) regions re-derived by hand: unchanged (both <= 25%), original+A / original+B (one share > 25%, original keeps > 25%, i.e. x+y < 75), A only / B only (one share > 25%, original keeps <= 25%), orig+A+B (both > 25%, x+y < 75), A+B (both > 25%, x+y >= 75); 1, 2, 3 swaps colour-coded in one hue.
- Honesty: "Illustrative ... a desk screen and not a legal determination." Caption wording for the diagonal cliffs ("each 25% line") was imprecise, since the diagonals are where the original's retained share crosses 25%; reworded.
- Legibility/style, fixed: the "original entity" label ran across the y-axis and the 25% line (shortened to "original"); the "75% or more: sole Successor" note overhung the axes (now three lines, y-limit raised); the 6.5 pt "orig.+A+B" label raised to 7 pt, other region labels to 8 pt, and the figure made slightly taller (7 x 3.7 in) with a wider panel (b). No legend needed (slots 0-1 and a sequential ramp only).
- Embedding: after the "With m Successors" paragraph with pointer sentence ("Figure 24.5 draws the thresholds as a map."); ok.

## Whole-chapter checks
- Numbering 24.1 to 24.5 in order, each file exists under assets/figures (95-121 KB, under the 500 KB budget), each image on its own paragraph with blank lines before and after, none inside a list, box or display math.
- No twinx, no slot 3-5 colours, no in-image titles; every caption begins with the claim and ends with "Illustrative: ..." plus its listing. No real-data claim appears in any figure.
- `python3 tools/figures/ch24.py` re-run clean; `tools/check_book.py --file` reports OK for the chapter (16,217 words).

## Edits made
- tools/figures/ch24.py: label positions and sizes (24.1, 24.2, 24.3, 24.4, 24.5), colour roles in 24.2(a), minus signs, figure size for 24.5; all five PNGs regenerated.
- book_src/24_ch24_bond_cds_basis_and_deliverables.md: three caption sentences (Figures 24.1, 24.4, 24.5), no other text touched.

<!-- STATUS: COMPLETE -->
