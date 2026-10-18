# Ch 20 figure check (Edition 2)

Checked: tools/figures/ch20.py against style.py; all five PNGs viewed before and after fixes; chapter embeds, captions and source text read. tools/check_book.py reports OK for the chapter.

## Figure 20.1, ch20_wrapper_flows.png: PASS (minor legibility fix)
- Correctness: arrow directions match section 20.1. Creation (blue): AP buys bonds at the offer, sends bonds plus cash balancing amount to the fund, receives new shares, sells them on the exchange. Redemption (orange): AP buys cheap shares, delivers a creation unit to the fund, receives the redemption basket, sells bonds at the bid.
- Honesty: caption says Illustrative (schematic of Rule 6c-11 flows).
- Legibility: no collisions. Fix: lane and box sub-labels raised from 7.5-7.8 pt to 8-8.2 pt.
- Embedding: after the cash-redemption paragraph, which points to it. OK.

## Figure 20.2, ch20_arbitrage_band.png: PASS (label fix)
- Correctness: band edges recomputed from (20.4) and the worked example. HY: 30-45-1-5 = -21, 30+30+1+5 = 66. IG: 8-10-1-3 = -6, 8+8+1+3 = 20. Shading is right (left of the lower edge redemption pays, right of the upper edge creation pays). Premiums +2, +15, +4 bp match the section 20.1 table (0.02%, 0.15%, 0.04%). Cold open: (77.10-77.82)/77.82 = -92.5 bp, labelled -93 as in the scene.
- Honesty: caption cites iShares and SSGA pages with dates and marks the band edges and cold-open discount as illustrative.
- Legibility: fix. The row labels mixed a Unicode combining-overline "c" with a mathtext c^R, so the symbols rendered in different fonts. Both are now mathtext ($\bar{c}$ = 30 bp, $c^R$ = 45 bp).
- Embedding: after the "Put in numbers" paragraph, which points to it. OK.

## Figure 20.3, ch20_ap_price_impact.png: PASS (no changes)
- Correctness: left panel is the linear price impact of (20.5), psi*F, with slopes 1 and 288 bp per $1bn. The multiplier is 2 x (12/2)^2 x (8/2) = 2 x 36 x 4 = 288. Right panel cumulative bars 1, 2, 72, 288 are the running product. 288 bp = 2.88%, consistent with the text's "about 2.9%".
- Honesty: caption states the calm slope of 1 bp per $1bn is set by assumption, and says Illustrative.
- Legibility: direct labels in ink, one y-axis per panel, no collisions. The 1x bar is nearly invisible by scale, which is accurate.
- Embedding: directly after corollary (a) and the sentence "Figure 20.3 shows the multiplication". OK.

## Figure 20.4, ch20_march2020_tape.png: PASS (label fix)
- Correctness: spread is real FRED BAA10Y (cache tools/figures/data/ch20_BAA10Y.csv). Checked the series maximum, 4.31 on 2020-03-23, which matches the annotation. Event dates are right: Mar 23 SMCCF announced, Apr 9 extension to HY ETFs, May 12 ETF buying starts. Premiums and discounts match the section 20.5.1 table and the advisor brief (Mar 12: UCITS USD IG -7.5%, US floating-rate -8.0%; Mar 19: LQD -5.08%, HYG +0.85%), signed correctly.
- Honesty: caption cites FRED BAA10Y, BlackRock ViewPoint (July 2020), MSCI (Bohak & Janosik, 2020-04-08), the Federal Reserve and the NY Fed. No unsourced numbers.
- Legibility: fix. The "May 12 ETF buying starts" label ran to the figure edge (about 5 px of margin); it is now right-aligned to the event line. Two panels, one y-axis each. Violet is used only for the spread, blue and red are the diverging premium and discount colors.
- Embedding: after the March 19 HY-premium paragraph, which points to it. OK.

## Figure 20.5, ch20_sleeve_runway.png: PASS after honesty fix
- Correctness: path is phi(t) = phi0 - R*min(t, Lw) from (20.8), with Lw = 2.4 weeks. Requirements 2.1 x 2.4 = 5.04 (shown 5.0) and 4.2 x 2.4 = 10.08 (shown 10.1). Endpoints: left 3% -> -2.04, 5% -> -0.04 (just short), 10% -> 4.96; right 3% -> -7.08, 5% -> -5.08, 10% -> -0.08. Exhaustion markers at phi0/R (1.43, 2.38 left; 0.71, 1.19, 2.38 right). Kinks at the settlement lag are right.
- Honesty: the right panel was titled "Concentrated outflow", and the chapter sentence said "concentrate the same outflow into two weeks". But the plotted path holds 4.2% a week indefinitely. If outflows really stopped after about 2.2 weeks, the requirement would be 9.2%, not 10.1% or "doubled". Fixes: panel title is now "Double the pace, 4.2% of fund a week"; the chapter sentence now reads "Double the pace to 4.2% a week, as if the same outflow were concentrated into half the time and kept up through the whole settlement lag"; the caption now says "each outflow rate held constant from week 0". Caption still says Illustrative with the Markit/Morningstar and SEC sources.
- Legibility: duplicate set_xlim removed; note text raised from 7.6 to 8 pt; sleeves use one hue in sequential order with direct labels; the critical status color is paired with the text label "sleeve exhausted".
- Embedding: after the "Plug in March 2020's pace" paragraph, which points to it. OK.

## Cross-checks
- Numbering 20.1 to 20.5 is in order of appearance (chapter lines 55, 228, 278, 385, 448); all five files exist (54-108 KB each, under the 500 KB budget); syntax is `![Figure 20.N: ...](assets/figures/ch20_*.png)`.
- Style: no in-image titles, no twinx, text in ink, slots 3-5 unused.

## Files changed
- tools/figures/ch20.py (font sizes, mathtext labels, May 12 label alignment, Fig 5 panel title, duplicate xlim)
- assets/figures/ch20_*.png (all five regenerated)
- book_src/20_ch20_credit_etf_creation_redemption_arb.md (one sentence in section 20.6.1, caption of Figure 20.5)

<!-- STATUS: COMPLETE -->
