## Z.4-B Chapter 4-B: Bond Math for the Desk: Price, Yield, Duration, Convexity, Spread Measures and the Callable Bond

Five exercises, none tagged [Read], [Derive] or [Build], each with a two-line solution already printed under it. I did not copy those: I reran everything in Python (Listing 4-B.1 from Appendix F, §F.4-B, unchanged, plus FRED par yields pulled on 18 October 2026) and then wrote the long version. The inline solutions hold up in substance; the three NOTEs below are about wording and one assert, not arithmetic. Exercises 2 to 4 are Build-style, since they extend Listing 4-B.1, and are worth doing at a keyboard. Exercise 2 is the unusual one: its printed solution gives only a direction ("its size must come from that day's data"), so the number here, 809.4bp, is new. Unless I say otherwise, prices are per 100 face, dirty (equal to clean on the stylized coupon dates), spreads are in basis points, and the Treasury curve is the reference. The lattice in Exercise 4 is risk-neutral ($\mathbb{Q}$); the P&L in Exercise 3 is realized, historical ($\mathbb{P}$) price P&L with carry ignored.

**Z.4-B.1: Rulers**

**Answer:** On a flat curve the whole G − Z gap is convention: 2.45bp on 20 February, 19.5bp on 23 March and 7.3bp on 30 June 2020 (G in the bond's semi-annual convention, Z continuous). Half a point of "spread" is pure compounding at a bond yield of about 14.5%.

**How:** With $y^{\text{cc}} = f\ln(1 + y/f)$, the compounding gap of any semi-annual yield is

$$
y - y^{\text{cc}} = \frac{y^2}{2f} - \frac{y^3}{3f^2} + \cdots
$$

On a flat curve the Treasury leg gets the same treatment at its own yield $y_T$: G subtracts $y_T$ itself, Z subtracts its continuous equivalent, so $G - Z = \text{gap}(y) - \text{gap}(y_T)$. For 23 March, $y = 9\%$: $20.25 - 0.61 = 19.64$bp for the bond, and $0.0076^2/4 = 0.14$bp for the Treasury, which leaves $19.50$. February: $3.06 - 0.04 = 3.03$ for the bond, less $0.58$ for the 1.52% Treasury, gives $2.45$. June: $7.56 - 0.14 = 7.42$, less $0.11$, gives $7.31$. Listing 4-B.1 gets $2.45$, $19.52$ and $7.32$; the table's $198 - 196$, $824 - 804$ and $484 - 477$ are the same numbers after rounding each spread before subtracting.

For the half point, set $\text{gap}(y) - \text{gap}(y_T) = 0.005$. The Treasury term is about 0.1bp, so solve $y^2/4 - y^3/12 = 0.005$ and get $y \approx 14.5\%$. The exact $y - 2\ln(1 + y/2)$ reaches 50bp at 14.48%, or 14.50% once the 0.76% Treasury term is subtracted. The gap grows with the square of the level: 34.6bp at 12%, 50.2bp at 14.5%, 93.8bp at 20%. That is why the rulers drift back together as the bond returns toward par (§4B.8, Beat 4).

**The trap:** Stopping at the quadratic term. It gives $20.25$bp for March (not 19.5) and $\sqrt{2f \times 0.005} = 14.1\%$ for the half point, and it overstates the gap by 2.4bp at 14.5% (52.6 against 50.2). The close second is dropping the $f$: $y^2/2 = 0.005$ gives 10%, which is short by a factor of $\sqrt{f}$. Underneath both is the habit of reading a G − Z gap as a credit statement. On a flat curve there is nothing credit-related in it.

**If you got this wrong, read:** §4B.2, "Continuous compounding, and the first convention", then §4B.8, Beat 2, for the gaps in Table 4B.1.

**Z.4-B.2: The real curve**

**Answer:** On the real 23 March 2020 Treasury par curve, $Z = 809.4$bp against 804.5bp on the flat 0.76% curve, so the shape term **raises** Z by 4.9bp. G is still 824bp (the ten-year par yield has not changed), so $Z - G$ moves from $-19.5$bp to $-14.6$bp. Continuous compounding, Treasury curve, the stylized note at its price of 70.73 (the 9.00% yield).

**How:** The par yields from FRED on 23 March 2020 are 0.17, 0.28, 0.38, 0.63, 0.76 and 1.33% for DGS1, DGS2, DGS5, DGS7, DGS10 and DGS30. Interpolate them linearly onto the half-year grid (flat before one year; the note only needs the first 20 nodes), bootstrap with `curve_from_par`, and call `z_spread(70.73, t, cf, disc)` on the note's twenty flows. The continuous zeros come out at 0.28% (2y), 0.38% (5y), 0.63% (7y) and 0.77% (10y). The curve climbs 13bp between the seventh and tenth years, and that climb is what moves Z.

The logic is the linearization of §4B.6: $y^{\text{cc}} - Z \approx \sum_k \omega_k z(t_k)$, a duration-weighted average zero. The note, with a Macaulay duration of 7.7 years, averages 0.709%. The par ten-year Treasury that G is measured against has a Macaulay duration of 9.6 years and averages 0.759%. The difference, $75.9 - 70.9 = 4.9$bp, is the shape term, and it is positive because the note's weight sits earlier on a rising curve. A flat curve at 0.76% over-discounts the early coupons, so the real curve needs a larger spread to reach the same price. In the bond's own semi-annual compounding the same calculation gives $Z = 828.9$bp, which is $G + 4.9$: the compounding gap disappears and only the shape is left. The same method gives $+1.1$bp for 20 February ($Z = 196.6$) and $+4.4$bp for 30 June ($Z = 481.0$). Adding DGS3, DGS20 and DGS6MO moves the March answer by 0.02bp, so the interpolation choice is not what you are measuring.

**The trap:** Answering "no change, 804" because "the ten-year yield is the same." That is the stylization of §4B.8, Beat 1, not a fact about the market: the cold-open table holds the whole curve at the ten-year par yield, and the real curve is below it for every maturity under ten years. The second wrong answer is the sign, "the shape lowers Z," from picturing a curve that sits above a flat one. This curve sits below it until year ten.

**If you got this wrong, read:** §4B.6, "The curve" for the bootstrap and "The eight" (the Z-spread paragraph) for the linearization; then §4B.8, Beat 1, for why the table uses a flat curve.

NOTE (for the editor): §4B.6 says that on an upward-sloping curve a high-coupon bond has "$Z > G$," and the Trend Watch in §4B.7 says the 2022–24 inversion "flipped the sign of $Z - G$ for high-coupon bonds." In the book's own continuous convention, the real 23 March 2020 curve (clearly upward-sloping) gives $Z - G = 809.4 - 824 = -14.6$bp, not a positive number, because the +4.9bp shape term is smaller than the $-19.5$bp compounding gap. The sentence is true of the shape term alone, or of Z quoted in the bond's own compounding (828.9 against 824). It is true of the full $Z - G$ only when the curve is steep enough: a 6.5% ten-year priced at $G = 400$bp has $Z - G = +5.4$bp on 31 March 2021 (2s10s +158bp) and $-15.9$bp on 3 July 2023 (2s10s −108bp). Consider "the shape term in $Z - G$ changes sign," or a clause naming the convention.

**Z.4-B.3: The hedge**

**Answer:** Unhedged, −\$3.76mm. With the analytic hedge (short \$9.50mm of ten-year Treasuries), −\$4.46mm. With Ben Dor's Ba ratio (long \$2.47mm of Treasuries), −\$3.58mm. This is realized price P&L, 20 February to 23 March 2020 ($\mathbb{P}$, history), on \$10mm of the note, with carry and roll ignored (they are tens of thousands of dollars).

**How:** The note goes from 108.376 to 70.732, a loss of 37.64 points, so $-\$3.764$mm on \$10mm. (The chapter's 37.65 subtracts the two rounded prices.) The analytic hedge ratio is $-\text{DV01}_{\text{bond}}/\text{DV01}_H = -878.5/924.5 = -0.950$, so short \$9.50mm of the par ten-year at 1.52%. When its yield falls to 0.76% that Treasury reprices to 107.305, up 7.305 points, and the short loses

$$
\$9.50\text{mm} \times 0.07305 = \$0.694\text{mm}, \qquad -3.764 - 0.694 = -\$4.459\text{mm}.
$$

Ben Dor's ratio is $-0.26$ times the analytic notional, so the position is $-0.26 \times (-\$9.50\text{mm}) = +\$2.47\text{mm}$, a long. A long Treasury gains on the rally, $0.26 \times 0.694 = +\$0.180$mm, and the total is $-3.764 + 0.180 = -\$3.584$mm. So the hedge that follows the duration column costs \$0.69mm against doing nothing, and the empirical one earns back \$0.18mm.

One caution on the $-0.26$. It is Ben Dor's Ba value at the sample's maximum OAS (Table 8.1), which his rounded coefficients put near 1,340bp. His own Ba line at the note's 824bp gives $0.41 - 0.05 \times 8.24 \approx 0.00$, which is no hedge at all and leaves the unhedged −\$3.76mm. The chapter's "a small long, or nothing" covers both, and the exercise's point survives either way: the analytic hedge was the worst of the three, because the fear that pushed Treasuries up pushed spreads out at the same time.

**The trap:** The sign. Treasuries rallied, so it is tempting to book the hedge as a gain and answer $-3.764 + 0.694 = -\$3.07$mm. A short Treasury position loses when yields fall. The other slip is reading $-0.26$ as "short 26% of the analytic notional," which gives $-\$3.94$mm; the negative sign means the position flips to a long.

**If you got this wrong, read:** §4B.5, "The hedge ratio," and §4B.8, Beat 3; then §8.2 (Table 8.1) for where $-0.26$ comes from and §8.7 for 2022, when the empirical hedge lost.

**Z.4-B.4: Kaz reads the redemption section**

**Answer:** On all three dates the T+50 make-whole callable and the plain bullet price identically at the note's Z-spread. The difference from `lattice_price` is 0.0, and the OAS equals Z: 195.5, 804.5 and 476.7bp, which sit 146, 754 and 427bp above $m_w = 50$bp. The call starts to bind the moment the spread drops **below $m_w = 50$bp**, and not at par. On the 23 March tree (Ho–Lee, $\sigma = 100$bp, flat 0.76% curve) the call is worth 0.10 points at 49bp, 0.52 at 45bp, 1.04 at 40bp, 2.6 at 25bp and 5.3 at 0bp. Risk-neutral ($\mathbb{Q}$) prices per 100, continuous spread.

**How:** Extend Listing 4-B.1 (App F, §F.4-B). Build `ho_lee(flat_curve(y_T), 10.0, 40, 0.01)` for each date's Treasury yield, place the flows with `on_grid`, and set `calls = {k: None for k in range(2, 40, 2)}`, a call at every coupon date with the strike supplied by `mw=0.005`. Then

$$
\texttt{lattice\_price(flows, dt, rates, Z, calls, mw=0.005)} - \texttt{lattice\_price(flows, dt, rates, Z)} = 0
$$

at each date's $Z$. Scanning $s$ downward from 100bp, the difference stays at 0.0 exactly until $s = 50$bp (0.0 at 50.0000001bp, $1 \times 10^{-5}$ at 49.9999bp) and then grows by about 0.1 point per basis point.

The reason is the proposition of §4B.7. At any node the continuation value is at most the bullet's value at spread $s$, and for $s \ge m_w$ that is at most the bullet's value at $m_w$, which is $W$, the make-whole amount itself. Below $m_w$ the inequality reverses: continuation exceeds $W$. And because $r + m_w$ is far below the 4.5% coupon, $W > 100$ (it is 130.3 at the root), so the strike is $W$, not par, and the issuer calls at the first date. The callable is then pinned near 130.3 however tight the spread gets (130.32 at 50bp, 130.65 at 0bp, while the bullet climbs to 135.9). That is also why `oas` returns an absurdly negative spread (−119bp at a market price of 131.4), or raises, for a market price above the cap. The 50bp threshold did not move when I changed $\sigma$ from 0 to 200bp or the flat curve from 0.76% to 4% or 8%. Only the size of the call below the threshold changes.

On the banker's question: the clause is worthless as an option and valuable as a claim. On the 23 March note the make-whole amount is about 130 per 100 against a market price of 70.7. No issuer calls it for rate reasons. But when something else triggers the redemption, a merger refinancing (§15.1, row 3), a covenant defeasance or a bankruptcy, the formula sets the amount owed. In Hertz the fight was over whether it was owed at all, with more than \$270mm at stake (§16.6). The proposition says nothing about who gets a payout when someone else pulls the trigger, so the RSSG habit of reading the definition and the triggers carries over intact.

**The trap:** "It binds once the bond trades above par," the logic of a call struck at 100. At $s = 100$bp this callable trades at 124.96, nearly 25 points over par, and the make-whole still does nothing. The strike moves with the curve, so the test is the issuer's spread against $m_w$, not the price against a fixed number.

**If you got this wrong, read:** §4B.7, "The make-whole" (the proposition) and "The four asserts"; then §15.1.2's table (row 3) and §16.6.

NOTE (for the editor): the last make-whole assert in Listing 4-B.1 (`lattice_price(flows_fa, dt_fa, rates_fa, z_mar, mw_calls, 0.005) - lattice_price(flows_fa, dt_fa, rates_fa, z_mar)`) runs after the `for d, (y_b, y_t) in dates.items()` loop, so `flows_fa`, `dt_fa` and `rates_fa` are the tree left over from the last iteration, 30 June (0.66% curve), while `z_mar` is the 23 March spread (804.5bp). I checked: the leftover tree equals the 0.66% tree, not the 0.76% one. The assert passes either way (the difference is 0.0), and the in-loop OAS assert already covers each date, but the line reads as if it tests 23 March. Moving it inside the loop, with `table[d]["Z"]`, would make it test all three dates, as the exercise asks.

**Z.4-B.5: ROBO's momentum signal**

**Answer:** Three ways the "spread column" can measure the ruler instead of the market over 2019–2025: (1) a reference-curve switch inside the sample (swap-based spreads moving from LIBOR to SOFR in 2023); (2) G-spread drifting with the shape of the Treasury curve through the 2022–24 inversion; (3) a spread-to-worst whose workout date, and therefore benchmark, changes when the price crosses a call price. The cure in each case is one spread, on one named curve, for the whole sample: Z, or OAS at a stated $\sigma$ and tree.

**How:** Each failure is a gap that would exist on a day when nothing happened to the credit.

1. *Curve switch.* The USD LIBOR panel ended on 30 June 2023, and the ARRC fallback spread for three-month LIBOR is 26.161bp (§21.1). An I-spread, asset-swap or discount-margin series that is spliced across the switch carries a level shift of that order, and a twelve-month momentum rule reads it as a market move for a year.
2. *G across the curve.* G subtracts the par Treasury at the bond's maturity and ignores the curve's shape. Hold the credit fixed (a 6.5% ten-year with $Z = 400$bp throughout) and G reads 394.5bp on 31 March 2021 (2s10s +158bp) and 409.5bp a year later (2s10s +4bp): 15bp of apparent widening with nothing happening to the credit. By 3 July 2023 (2s10s −108bp) it reads 416.6bp, 22bp up, made of curve shape and a higher yield level (compounding, Exercise 1). Small next to a 300bp high-yield move, but it is the same sign for every bond for two years, which makes it a bias and not noise.
3. *Workout date.* On Brambleworth (illustrative terms of §4B.7) the worst date moves from year 5 to year 4 at a price of 100, from year 4 to year 3 at 108.39 and from year 3 to year 2 at 108.82. The yield is continuous across each point (9.253% at 99.99, 9.247% at 100.01). The benchmark Treasury it is measured against is not. On the 3 July 2023 curve (par 2y 4.94%, 3y 4.56%, 4y 4.38% interpolated, 5y 4.19%) the spread-to-worst falls 19bp as the price crosses 100 and 38bp at 108.82, with no change in the market. OAS at a stated $\sigma$ has no workout date to switch (Law 11).

Also on the list, from the same chapter: vendor history that was restated after the fact (§4B.8, Beat 1), the one-day accrued shift at T+1 on 28 May 2024, and par versus market-value asset swaps, which differ by a factor of $100/P$.

**The trap:** ROBO's own argument, "the six columns are 0.97 to 0.99 correlated, so keep any one." That is a statement about levels. Table 4B.1 shows the same bond's spread multiplying by 3.3 on the par asset swap and 5.1 on PECS in one month, and the five rulers disagreeing by about 300bp on the change, which is the quantity a momentum signal uses. The other tempting answer is a list of generic backtest sins (stale prices, survivorship, look-ahead). They are real, but none is a convention in the column's own definition, which is what the question asks for.

**If you got this wrong, read:** §4B.8, Beat 2 ("six rulers, one length"); §4B.6 for G versus Z; and §4B.7 ("Yield-to-worst" and the Trend Watch on the reference curve).

NOTE (for the editor): the inline solution says "YTW jumping when the workout date changes." Yield-to-worst is a minimum of continuous functions of price, so it kinks but does not jump. On Brambleworth it is 9.253% at a price of 99.99 and 9.247% at 100.01, while the workout moves from year 5 to year 4. What jumps is the workout date and, with it, the benchmark Treasury and the duration, so a spread-to-worst (YTW minus the Treasury at the workout date) falls 19bp on the 3 July 2023 curve as the price crosses 100. Consider "spread-to-worst jumping when the workout date changes."

<!-- STATUS: COMPLETE -->
