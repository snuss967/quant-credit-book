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

**The trap:** Stopping at the quadratic term. It gives $20.25$bp for March (not 19.5) and $\sqrt{2f \times 0.005} = 14.1\%$ for the half point, and it overstates the gap by 2.4bp at 14.5% (52.6 against 50.2). The close second is dropping the $f$: $y^2/2 = 0.005$ gives 10%, which is off by a factor of $\sqrt{2f}/\sqrt{2}$. Underneath both is the habit of reading a G − Z gap as a credit statement. On a flat curve there is nothing credit-related in it.

**If you got this wrong, read:** §4B.2, "Continuous compounding, and the first convention", then §4B.8, Beat 2, for the gaps in Table 4B.1.

