# Red-pen log (Edition 2): 08_ch08_isolating_ido_and_empirical_duration.md

## C11 (desk-head red-pen), §8.1 accrual line only: fixed

All changes in `book_src/08_ch08_isolating_ido_and_empirical_duration.md`, §8.1. The §12.5 and §26.8 parts of C11 belong to other files and were not touched. Source of the item: synthesis row C11 and desk-head review ("§8.1 carry line": $y\,\Delta t$ mixes coupon accrual, certain and reconciled to the custodian, with pull-to-par, a model output; the one-bond table hides the distinction).

- **Derivation paragraph (clause extended):** after "yield carry $y\,\Delta t$" added "(two parts with two different owners, split in the table below)". The collapse of accrual plus price pull into the yield is unchanged and still correct.
- **"The thirty-seven cents, itemized", inputs line:** added "a coupon of 10% (about what the price, yield and duration imply)". This is an illustrative input, needed because accrual cannot be separated from pull-to-par without a coupon. It is not a sourced fact. Check run: a 10% semiannual coupon at an 11.1% yield prices at 95.6 with modified duration 4.10 at 5.5 years (95.3 and 4.37 at 6 years), so it reproduces the stated \$95 and 4.1 to rounding. Flagged here as the one added number.
- **Table:** the Carry row (+0.031%, +3 cents) is kept and two italic memo rows added beneath it: coupon accrual (custodian), $(c\,\Delta t)/0.95 = (0.10/360)/0.95$, +0.029%, +2.8 cents; pull-to-par (model), $y\,\Delta t - (c\,\Delta t)/0.95$, +0.002%, +0.2 cents. They sum to the carry row (2.8 + 0.2 = 3). Rates, spread, convexity, residual and the total (−0.390%, −37 cents) are unchanged, and the total foots on the headline rows alone. The headline structure stays at six rows (carry, rates, spread, convexity, residual, total), so Chapter 8-C's line "The one-bond table has six rows" still holds.
- **New paragraph after the table (about 125 words):** accrual is a fact the custodian confirms; pull-to-par is a model forecast that is wrong once the yield moves; on this bond the forecast is 0.2 of a cent so merging them costs nothing today, on a bond trading far below par it would, and a missing coupon would hide in it; product control keeps them apart, as the Chapter 8-C production explain does. No other new numbers.

Web fetches used: 0 (no external fact was involved). Check: `tools/check_book.py --file` reports OK. No topic removed; the closing status line of the chapter is preserved.
<!-- STATUS: COMPLETE -->
