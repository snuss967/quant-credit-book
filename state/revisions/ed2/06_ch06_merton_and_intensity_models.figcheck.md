# Figure check: Chapter 6 (ed2)

Chapter: book_src/06_ch06_merton_and_intensity_models.md. Script: tools/figures/ch06.py. Log: state/revisions/ed2/06_ch06_merton_and_intensity_models.figures.md (STATUS: COMPLETE, so the check ran).

Method: read the house style (tools/figures/style.py docstring); read the drawing code for each of the five embedded ch06_*.png; re-ran the script (all its assertions pass and the five PNGs reproduce byte for byte); viewed every PNG; read the chapter text around each embed; checked real-data claims against primary sources (FRED download of BAMLH0A3HYC; SEC EDGAR XBRL company facts for SVBFG FY2022; the repo's case dossier and the cached CVNA vendor file).

Embedding: five embeds, numbered 6.1 to 6.5 in order of appearance (lines 93, 187, 273, 492, 916 before edits), syntax `![Figure 6.n: ...](assets/figures/ch06_*.png)` matching ch05, all five files exist (tools/check_figures.py reports nothing for ch06), each figure follows the paragraph that points to it. check_book.py lints the chapter OK.

## Figure 6.1, ch06_volatility_tax: PASS (one cosmetic fix)
- Correctness: tree ends 121, 99, 99, 81 with probabilities 25/50/25; mean 100, median 99 (asserted). Lognormal: median 100*exp(0.08 - 0.03125) = 105.0, mean 108.33, P(V < 100) = 42.3% (asserted). Right tail is long, density zero below 0, mean line right of median line, as theory demands.
- Honesty: caption says "Illustrative" and names the §6.1.1 tree and the §6.1.2 parameters; numbers match the image.
- Legibility: no collisions; one y-axis per panel; fills are one hue; text in ink.
- Fix: the one informative note ("the 121 branch pulls the mean up") was MUTED grey at 8 pt; changed to INK_2.

## Figure 6.2, ch06_merton_payoff_fulcrum: PASS (one cosmetic fix, stale hook removed)
- Correctness: left, debt = min(V, 80) with its kink at 80, equity = max(V - 80, 0) with its kink at 80, the V = 70 shortfall of 10 marked; density is the 6.2.4 lognormal with 13.8% below F (asserted). Right, the four class payoffs have kinks at 400, 700 and 950 and sum to V (asserted); seniority runs dark to light blue, equity orange. Density: lognormal, median 530, vol 22%: mass between 400 and 700 is 79.7% (asserted), 5th to 95th percentiles are 530*exp(+-1.645*0.22) = about 369 to 761, matching the caption's "about $370mm to $760mm".
- Honesty: "Illustrative", with the density parameters stated in the caption (they are the author's, not data).
- Legibility: no collisions or clipping; text inside fills is white on dark blue or ink on light blue.
- Fixes: "firm value V" and "F = 80" labels MUTED to INK_2. Embedding: deleted the stale `<!-- FIGURE HOOK: ch06_merton_payoff_fulcrum.png ... -->` comment (the figure it asked for is now embedded eight paragraphs later, where its right panel has the numbers it needs).

## Figure 6.3, ch06_merton_spread_short_end: PASS (one cosmetic fix)
- Correctness: closed form of §6.2.3 (B = V - E, s = -ln(B / (F e^{-rT})) / T) checked against the worked example (216 bp at one year, 70 bp at three months, under 1 bp at 2.5 weeks, near 30 bp at 15% vol; all asserted). Spread tends to 0 at the short end, is humped at medium maturity and falls at 10 years, as the theory gives for this leverage.
- Honesty: independently re-pulled FRED BAMLH0A3HYC for 17 Oct 2023 to 15 Oct 2026: 786 observations, minimum 6.90% on 2025-01-23, maximum 12.82% on 2026-10-14, last value 12.78%. Caption's source line matches exactly. Curves are labelled Illustrative. The band is a different (more levered) universe than the 80/100 model firm; the chapter text frames it only as "the market's short end is never zero", so I left it. Licence note in the figures log (only the two end values are drawn) stands.
- Legibility: curves are one hue (SEQ_BLUE) and direct-labelled at the right; three leader-line annotations are clear of the curves; one y-axis.
- Fix: the parameter note "Merton firm: V0 = 100, F = 80, r = 4%" MUTED to INK_2.

## Figure 6.4, ch06_svb_holdco_waterfall: PASS after fixes
- Correctness: parent assets 19.679, less bank stake 15.456 = ex-bank 4.223, less cash at bank 2.258 = 1.965; liabilities 3.370 + 0.305 = 3.675; coverage 1.149 and 0.535 (asserted). Waterfall steps are drawn from unrounded values and connect.
- Honesty: checked against SEC EDGAR XBRL for the FY2022 10-K (filed 2023-02-24): held-to-maturity amortized cost $91.327bn, fair value $76.169bn, loss $15.158bn (so $15.2bn is right, though the rounded inputs $91.3bn and $76.2bn subtract to $15.1bn); stockholders' equity $16.004bn. Parent-only figures and the 8 March 2023 events agree with the dossier (sections 2.1 to 2.3) and the chapter's Beat 4 text.
- Problems and fixes: (1) left y-axis said "$ billions, 31 Dec 2022" although the third bar is the 8 March 2023 sale loss; changed to "$ billions" and moved the date into the caption ("all at 31 December 2022"). (2) Caption now says the $15.2bn is a loss on the unrounded figures, so a reader who subtracts the rounded inputs is not surprised. (3) Hatching was unexplained; the caption now says hatched bars are losses that are unbooked or assumed. (4) Rounded labels do not add (4.2 less 2.3 shown as 2.0); the caption now says so.
- Legibility: viewed after the changes; no clipping, "parent liabilities 3.7" sits outside the axes without being cut; x tick labels at 7.8 pt are small but legible.

## Figure 6.5, ch06_carvana_pair: PASS (no change)
- Correctness: cached vendor series (860 daily rows, 2021-08-02 to 2024-12-31): maximum $370.10 on 2021-08-10, minimum $3.72 on 2022-12-27 (-99.0%), 19 Jul 2023 close $55.80 (+40.2% on the day), last close $203.36; all reproduce the dossier. Right panel: notes +0.9, +2.9, +3.3, +4.0, short stock -1.1, -4.5, -7.9, -10.2, net -0.2, -1.5, -4.6, -6.2, from the dossier's stack marks (44.8, 53.8, 74.0, 77.7, 84.7) and closes (4.74, 9.79, 25.92, 41.98, 52.94); December legs equal the chapter's "$4 million" and "$10.2 million" (asserted). Exchange-event dates (22 Mar offer launched, 2 Jun offer terminated, 19 Jul TSA announced, 1 Sep settlement) match dossier section 1.1 and the chapter's beats.
- Honesty: caption cites Yahoo Finance (restated to as-traded, 5-for-1 reversed), the 8-Ks and 10-Qs, and says the note leg is a fair-value-ratio proxy and the sizing is Illustrative, before coupons, financing and borrow. "Fell 99%", "more than tenfold" (3.72 to 52.94 is 14x; 4.74 to 52.94 is 11.2x) and "lost money at every quarter-end" are all true to the data.
- Legibility: log axis with dollar ticks; event digits staggered, none touching; key at lower right clear of the price line; legend clear of bars; orange equity, blue notes, grey net; one y-axis per panel.

## Flags (not changed)
1. Chapter body, Beat 1 of 6.4 (line about 454): "\$91.3 billion ... \$76.2 billion. That is a \$15.2 billion unrealized loss" has the same rounding trap; a clause such as "on the unrounded figures" would fix it. Outside the figure remit.
2. tools/figures/data/ch06_CVNA.csv is vendor data (Yahoo Finance); the log already flags the licensing question.
3. `CCC_LAST_BP` in ch06.py is defined and unused; harmless.
4. output/Quant_Credit_Master_Book.md still holds the old FIGURE HOOK comment until the next build.

## Files touched
- tools/figures/ch06.py (four text colours MUTED to INK_2; one y-label)
- assets/figures/ch06_volatility_tax.png, ch06_merton_payoff_fulcrum.png, ch06_merton_spread_short_end.png, ch06_svb_holdco_waterfall.png (regenerated and re-viewed; ch06_carvana_pair.png unchanged)
- book_src/06_ch06_merton_and_intensity_models.md (stale FIGURE HOOK comment deleted; Figure 6.4 caption extended)

<!-- STATUS: COMPLETE -->
