# Ch 20 figures log (Edition 2, U4)

Script: tools/figures/ch20.py (run from the repo root: `python3 tools/figures/ch20.py`). Data cache: tools/figures/data/ch20_BAA10Y.csv (FRED BAA10Y, daily, 2020-02-03 to 2020-06-30; fetched 2026-10-18). ICE BofA OAS series (BAMLC0A0CM, BAMLH0A0HYM2) were tried and rejected: FRED now serves only the last three years of them, so March 2020 is missing.

Plan (5 figures): ch20_wrapper_flows (s20.1), ch20_arbitrage_band (s20.3.1), ch20_ap_price_impact (s20.3.2), ch20_march2020_tape (s20.5.1), ch20_sleeve_runway (s20.6.1).

## Embedded figures

1. **Figure 20.1, ch20_wrapper_flows.png** (s20.1, after the cash-redemption paragraph). Flow graph: bond market, AP, fund and exchange, with creation arrows (blue) and redemption arrows (orange) showing what moves in each trade. Data: none; schematic of the Rule 6c-11 flows described in the section (caption: Illustrative).
2. **Figure 20.2, ch20_arbitrage_band.png** (s20.3.1, after the "Put in numbers" paragraph). The static no-arbitrage band (20.4) for the chapter's worked HY fund (-21 to +66 bp) and IG fund (-6 to +20 bp), with the issuer-reported premiums of HYG (+2 bp), JNK (+15 bp) and LQD (+4 bp) and the cold-open HYG discount (-93 bp). Data: band edges are the worked example in the text (Illustrative); premiums from the iShares HYG/LQD pages (2026-10-16) and SSGA JNK page (2026-10-15), as in the s20.1 table.
3. **Figure 20.3, ch20_ap_price_impact.png** (s20.3.2, after corollary (a)). Left: discount from AP price impact against net selling, calm vs stress (slopes 1 and 288 bp per $1bn). Right: the 2 x 36 x 4 = 288 multiplier built up as a product. Data: Illustrative, from the model of (20.5) with the multipliers stated in the text; the calm slope of 1 bp per $1bn is an assumption set so the text's "1 bp becomes 2.9%" example holds.
4. **Figure 20.4, ch20_march2020_tape.png** (s20.5.1, after the "HY premium on March 19" paragraph). Top: daily Baa-minus-10yr-Treasury spread, 2020-02-10 to 2020-05-22, with the SMCCF dates (Mar 23, Apr 9, May 12). Bottom: closing ETF premium/discount to NAV as cited in the chapter (UCITS USD IG ETF -7.5% and US floating-rate ETF -8.0% on Mar 12; LQD -5.08% and HYG +0.85% on Mar 19). Data: FRED BAA10Y (cached in tools/figures/data/ch20_BAA10Y.csv); discounts from BlackRock ViewPoint (July 2020) and MSCI (Bohak & Janosik, 2020-04-08) as in the s20.5.1 table; SMCCF dates from the Federal Reserve / NY Fed. HY OAS (BAMLH0A0HYM2) is not on FRED for 2020 any more (3-year history limit), so no HY spread line.
5. **Figure 20.5, ch20_sleeve_runway.png** (s20.6.1, after the "Plug in March 2020's pace" paragraph). Liquidity sleeve path under (20.8) for 3%, 5% and 10% sleeves, with a steady outflow of 2.1% of the fund per week (needs > 5.0%) and a concentrated 4.2% per week (needs > 10.1%), settlement lag 2.4 weeks; exhaustion points marked. Data: Illustrative, from the recursion (20.8); lag from Markit Q2-2016 (17 days, via Morningstar, as cited in s20.6) and the 9.2% March 2020 HY-fund outflow from the SEC staff report as cited in the text.

Checks: all five PNGs opened and inspected, under 110 KB each; tools/check_book.py reports OK for the chapter; chapter edits are limited to the five figure lines plus one pointer sentence before each.

<!-- STATUS: COMPLETE -->
