## Chapter 21: Leveraged Loans, CLOs & Loan-Market Microstructure

Six exercises. Two are on the CLO's rulebook, one on the borrower's call, two on the plumbing under the marks, and one on the seat at the restructuring table that Theo used to fill. Write your card before you read ours.

**Z.21.1: The cure, by hand**

**Answer:** The deal holds \$36mm of CCC against a \$30mm limit, so the excess is \$6mm. All of it sits at 55, so $p^\ast = 0.55$. Selling \$4mm of the CCC at 90 and reinvesting at par gives $\Delta\text{ACPA} \ge +\$1.387$mm. Here the bound is exact, because every loan in the excess set is priced at $p^\ast$. Selling \$4mm of the CCC at 55 gives a $\Delta\text{ACPA}$ between $-\$0.135$mm (the theorem's floor) and zero. Because no CCC trades below 55, the exact figure is $-\$0.061$mm. Both trades leave \$32mm of CCC, about 8.0% of the pool, so the bucket is still over its limit either way. The difference is the numerator: the first trade adds \$1.39mm to it and the second takes \$61k off.

**How:** Loan $i$ at 90 sits above the excess set, so case 1 of (21.6) applies:

$$
\Delta\text{ACPA} \;\ge\; 4\big[(0.90 - 0.55) - 0.075 \times 0.45 \times 0.10\big] = 4 \times 0.3466 = 1.387 .
$$

The excess shrinks by $\Delta n[1 - \bar c(1-p_i)] = 3.97$, which leaves \$2.03mm, so the theorem's "excess stays positive" condition holds. To check by recompute: non-defaulted par becomes 399.6, the limit 29.97 and the excess 2.03. The haircut falls from 2.70 to 0.91, and subtracting the 0.40 of par burn gives +1.387. Selling the 55 is case 2. The par burn, $0.45 \times 4 = 1.80$, equals the haircut removed. The only residue is that the limit shrinks by $\bar c \times 1.80 = 0.135$, which pulls that much par of the next-cheapest CCC back into the excess at a haircut rate of at most $0.45$. That gives $-0.135 \times 0.45 = -0.061$.

Here is how you'd put it to the ex-RSSG colleague. "The test had already marked those 55s to market. Selling them turns a haircut into a realized loss of exactly the same size: \$1.8mm of par walks out the door, and \$1.8mm of haircut leaves with it. The numerator doesn't move, except that the pool got smaller, so the 7.5% limit got smaller too and dragged a sliver of another cheap loan back into the excess. You paid 45 points in cash for a charge the test had already taken. Selling the 90 lifts par out of the excess, which frees the 55s from their haircut, and it costs only ten points of par burn."

**The trap:** The common answer is that the cheap loans are "the problem", so selling them must help. The other common slip is to count only the par burn, $-\$1.8$mm for the cheap sale and $-\$0.4$mm for the rich one, and forget the haircut relief. A smaller slip is to forget that the limit shrinks with the par burn. That gives exactly zero for the cheap sale and $4 \times 0.35 = 1.40$ for the rich one.

**If you got this wrong, read:** §21.4.2 (the cure-trade theorem and its two-case proof), then §21.4.1 for the excess set and $p^\ast$. Listing 21.1's `sell_and_rebuy_par` runs the same recompute on the synthetic deal (+\$0.78mm for the richest CCC, $-\$0.03$mm for the cheapest).

**Z.21.2: The 85.01 trade**

**Answer:** Per \$100 of cash, a performing B3 bought at price $p$ adds $100(1/p - 1)$ to ACPA if $p$ is at or above the 85 threshold, and nothing if it is below. Above 85 that falls as $p$ rises, so the maximum sits at the threshold: +\$17.63 per \$100 at 85.01, against +\$11.11 at 90, zero at par, and zero at 84.99 or 80. ROBO therefore buys the cheapest B3s priced just above 85. Of the three tests, the **CCC bucket** is the one that exists to stop this. WARF cannot see the trade, because every candidate is B3 and carries the same rating factor (3,490). WAS reads the contractual margin, not the price, so a cheap loan with an ordinary margin passes it. The CCC bucket is the only one of the three that marks par back to market. A B3 at 85 is priced like next quarter's Caa1. When it is downgraded into a full bucket, each dollar costs $(1 - p^\ast)$, charged to the deal's cheapest CCCs.

**How:** In (21.5) principal cash counts at 1, and a loan that is neither discount nor CCC counts at full par. Spending cash $C$ at price $p \ge 85$ therefore gives

$$
\Delta\text{ACPA} = \frac{C}{p} - C = C\Big(\frac{1}{p} - 1\Big).
$$

Below 85 the loan falls into $\mathcal{O}$ and is carried at $p^0 = p$. Its par of $C/p$ then counts as $C$, so $\Delta\text{ACPA} = 0$. The objective is zero below 85, jumps there, and slopes down above it, so an optimizer told only to maximize the junior cushion puts every dollar at the jump. Mags described this trade in the cold open: \$6.98mm of sale proceeds buys \$8.2mm of par at 85, which adds about \$1.2mm to the numerator. The CCC bucket stops it only after the fact. Once the 85s do what their price says and migrate, the bucket overflows and the cliff of §21.4.1 takes back the par ROBO built, and the charge lands on loans ROBO never touched. The practical fix is to put the bucket into ROBO's objective. Maximize the cushion under a stress that moves loans priced below about 90 into Caa1, or cap exposure to near-threshold prices.

**The trap:** The usual wrong answer is "buy at 80, the cheapest." Below the threshold the loan is a discount obligation carried at what you paid, so it builds no par at all. The runner-up is "WARF stops it." WARF is rating-based, and in a B3 universe it is identical whatever ROBO buys.

**If you got this wrong, read:** §21.4.1 (the discount set $\mathcal{O}$ as a barrier digital, and the cliff), the cold open (Mags's arithmetic on the seller), and item (3) of "Ways This Blows Up" in §21.4.3 on rating mapping.

**Z.21.3: The ceiling**

**Answer:** For $m > s$, the premium over par in (21.7) is at most $100(m-s)/(y+h)$, which goes to 0 as $h \to \infty$, so the price goes to 100. It gets there slowly, at a rate of $1/h$: with 50 bp of excess margin the price is 100.45 at $h = 1$, 100.12 at $h = 4$ and 100.05 at $h = 10$. In the soft-call version, with a window of remaining length $\tau$,

$$
P^{\text{sc}} = 100\big[1 + (m-s)\,a(T; y+h)\big] + h\,a(\tau; y+h),
$$

and this tends to **101** as $h \to \infty$. Take $h = 2$, six months left on the soft call, $T = 3$ and $y = 6.65\%$. The borrower prefers to wait if $m - s$ is below about **131 bp** (126 bp undiscounted). Above that it pays the point and reprices now. The same threshold is 89 bp at $h = 1$ and 177 bp at $h = 4$. Typical repricing cuts are 40–55 bp, so real borrowers wait, which is why repricings bunch at soft-call expiry.

**How:** For the proof, $a(T; r) = (1 - e^{-rT})/r$ lies between 0 and $1/r$, so $0 < 100(m-s)\,a(T; y+h) \le 100(m-s)/(y+h) \to 0$. For the soft call, a repricing inside the window pays the lender 101, one point over par. That extra point arrives at the hazard's first ring $U$ if $U < \tau$. Its value is $\mathbb{E}[e^{-yU}\mathbf{1}\{U<\tau\}] = \int_0^\tau h e^{-(y+h)u}\,du = h\,a(\tau;y+h)$, which goes to 1 while the margin term goes to 0. For the borrower's choice, remember that the lender's price is the borrower's cost. Repricing whenever the clock rings costs $P^{\text{sc}}$. Waiting switches the clock off until $\tau$ and then lets it ring at rate $h$, which costs $100[1 + (m-s)(a(\tau;y) + e^{-y\tau}a(T-\tau;y+h))]$. Setting the two equal gives

$$
(m-s)^\ast = \frac{h\,a(\tau;y+h)}{100\,G}, \qquad G = a(\tau;y) - a(\tau;y+h) + \big(e^{-y\tau} - e^{-(y+h)\tau}\big)\,a(T-\tau;y+h),
$$

with $G = 0.474$ and $h\,a = 0.623$, so $(m-s)^\ast = 1.31\%$. The intuition comes from memorylessness. Waiting delays the expected repricing date by exactly $\tau$, which costs about $100(m-s)\tau$ points. Paying costs the point only if the clock would have rung inside the window, which happens with probability $1 - e^{-h\tau} = 63\%$. So $(m-s)^\ast \approx (1 - e^{-h\tau})/(100\,\tau) = 126$ bp.

**The trap:** The common answer treats exercise as instant: "wait if half a year of excess margin is worth less than a point," which gives 200 bp (203 discounted). That is the $h \to \infty$ limit, and at $h = 12$ the threshold is already 203 bp. A borrower with $h = 2$ might not have repriced inside the window anyway, so the point is only a 63% cost to it. The other slip is to say the soft-call price also tends to 100. Inside the window the cap is 101, and Listing 21.3's `loan_price` does not apply it for you.

**If you got this wrong, read:** §21.5.1 (equation 21.7 and "The ceiling"), the soft-call clause in §21.1, and the Math, Gently box on hazards in §21.5.1 for memorylessness.

**Z.21.4: Queue stress**

**Answer:** The stationary daily sd is $\sigma_f = 0.5\%/\sqrt{1-0.49} = 0.700\%$ of NAV. The bracket in (21.9) is 97.8, against 20 for i.i.d. flows, so the 20-day sd is 6.92% of NAV. At $z = 2.326$ and zero drift the **99% buffer is 16.1% of NAV**, or 17.1% if you carry the chapter's 5 bp a day of mean outflow. That is 3.6 times the 4.5% median liquidity ratio. It is also about four April 2025 weeks back to back: bank-loan funds lost 2.7–4.2% of assets over 2–9 April, and four weeks at 4.2% comes to 16.8%. A fund holding the median 4.5% therefore needs a committed line of about **11.6% of NAV** (12.6% with drift) to cover one bad window. If the line has to cover the worst 20-day window of a year, size it nearer 20%: in simulation, the 99th percentile of the annual maximum window is about 24.5%.

**How:** The weighted autocovariance sum has a closed form:

$$
\sum_{k=1}^{\ell-1}(\ell-k)\phi^k = \frac{\phi\,[\ell(1-\phi) - (1-\phi^\ell)]}{(1-\phi)^2} = \frac{0.7 \times 5.0008}{0.09} = 38.9 ,
$$

so the bracket is $20 + 2 \times 38.9 = 97.8$ and the variance is $4.90 \times 10^{-5} \times 97.8 = 4.79 \times 10^{-3}$. The two scaling limits bracket the answer. With i.i.d. flows the sd would be $0.5\% \times \sqrt{20} = 2.24\%$. With perfectly persistent flows it would be $20\,\sigma_f = 14.0\%$. At $\phi = 0.7$ it is 6.9%. To check against April, the same parameters give a 5-day sd of 2.75%, which makes the 4.2% week a 1.5-sd week. These are stress parameters, harsher than April, which is what a buffer should be sized on. The line is $b^\ast - 4.5\%$. Listing 21.4's `buffer_needed(0, 0.005, 0.7, 20)` reproduces 16.1%, and `simulate_flows` with `rolling_window_sums` gives the running maximum.

**The trap:** The common slip is to read $\sigma = 0.5\%$ as the stationary sd of daily flows. That drops the $1/(1-\phi^2)$ and gives 11.5%, about 30% too small. The bigger error is $\sqrt{\ell}$ scaling, $2.326 \times 0.5\% \times \sqrt{20} = 5.2\%$, which looks like "the median buffer plus a bit" and misses by a factor of three. The worst version is ROBO's: the largest one-day outflow.

**If you got this wrong, read:** §21.6.1 (equation 21.9, the scaling argument and the Fed's April 2025 numbers), then "Ways This Blows Up" after the ETF band and the Quant-Shop Life vignette on which cash number the buffer is built from.

**Z.21.5: Smoothing tax**

**Answer:** Equation (21.10) gives $\operatorname{Var}(\tilde r) = \sigma^2(1-\phi)/(1+\phi)$ and a lag-one autocorrelation of $\phi$. The filter leaves the mean unchanged, so the Sharpe ratio of the marks is inflated by $\sqrt{(1+\phi)/(1-\phi)}$: 1.363 at $\phi = 0.3$ and 1.73 at 0.5. On the generous reading, about **90 bp a month survives** ($122 \times 0.734 = 89.5$), which is 73% of the premium, and the smoothing tax is about 33 bp. The assumptions are these. $\phi = 0.3$ is the persistence of the strategy's monthly marked returns. True returns are serially uncorrelated. The 122 bp was earned at the volatility the marks reported, and you hold that risk budget fixed. The mean itself carries no smoothing artifact. The figure is before costs. Because of that last assumption, treat the 90 bp as an upper bound.

**How:** Iterate the recursion to get $\tilde r_t = (1-\phi)\sum_{k\ge0}\phi^k r_{t-k}$. Then

$$
\operatorname{Var}(\tilde r) = (1-\phi)^2\sigma^2\sum_{k\ge0}\phi^{2k} = \frac{(1-\phi)^2\sigma^2}{1-\phi^2} = \sigma^2\,\frac{1-\phi}{1+\phi},
$$

and since $r_t$ is independent of $\tilde r_{t-1}$, $\operatorname{Cov}(\tilde r_t, \tilde r_{t-1}) = \phi\operatorname{Var}(\tilde r)$, so the autocorrelation is $\phi$. The weights sum to $(1-\phi)\sum\phi^k = 1$, so $\mathbb{E}\tilde r = \mathbb{E}r$ and

$$
\frac{\text{SR}_{\text{marked}}}{\text{SR}_{\text{true}}} = \frac{\sigma}{\tilde\sigma} = \sqrt{\frac{1+\phi}{1-\phi}} .
$$

To run the strategy at the true risk the backtest *thought* it was taking, scale positions by $\sqrt{0.7/1.3} = 0.734$. The mean scales with them, which gives 89.5 bp. Why is that an upper bound? A lag-one autocorrelation of $\phi$ is itself momentum, so part of the mean can be the smoother too. Kaz's backtest shows it. At $\hat\phi = 0.45$, pure deflation turns a Sharpe of 2.4 into 1.48, but desmoothing took it to 1.1, and the extra drop was spurious autocorrelation sitting in the mean. So desmooth with the Geltner inversion and recompute; don't just divide.

**The trap:** The common answer is "smoothing doesn't change the mean, so all 122 bp survive." That holds for a buy-and-hold mean. It fails for a risk-adjusted premium, and it fails for a strategy that trades on autocorrelation. The arithmetic slip is to drop the square root: $122 \times 0.7/1.3 = 66$ bp.

**If you got this wrong, read:** §21.7.1 (equation 21.10 and the Math, Gently box), Listing 21.5 (`geltner_desmooth`, `dimson_beta`), and the capacity paragraph and desmoothed-backtest scene in §21.7 for what is left after costs.

