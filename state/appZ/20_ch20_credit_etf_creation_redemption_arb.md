## Chapter 20: Credit ETF Creation/Redemption Arbitrage (HYG, JNK, LQD, BKLN)

Six exercises: one on the census, one on Kaz's regression, one on the AP count, one on basket cardinality, one on the Fed's clause and one on the loan sleeve. We checked every number in python3, and the toy runs reuse Listing 20.1 (Appendix F) with its seed. Write your answer down before you read ours.

**Z.20.1: The premium-day census**

**Answer:** $(f^R + k^R)/(2\bar c + f^C + k^C) = 44/206 = 0.214$. Under a uniform premium the redemption door sits about a fifth as far below zero as the creation door sits above it. If the creation door is at the chapter's illustrative $+66$ bp, the redemption door is at about $-14$ bp. In a year of net inflows the uniform assumption is wrong, and it biases the ratio **down**: 0.214 is a floor, and the true lower door is further from zero than the census suggests.

**How:** With pro rata baskets, (20.4) runs from $\pi^{\text{lo}} = -a$ to $\pi^{\text{hi}} = b$, where $a = f^R + k^R$ and $b = 2\bar c + f^C + k^C$. If the premium is uniform on that interval, the share of discount days is the share of the room below zero:

$$
\frac{44}{250} = \frac{a}{a + b} \quad\Longrightarrow\quad \frac{a}{b} = \frac{44}{250 - 44} = \frac{44}{206} = 0.214 .
$$

Now the lean. In steady inflows the APs create at the margin, so the premium spends its time pressed against the upper door, and the density rises toward $\pi^{\text{hi}}$. For any true pair of doors that lean puts *fewer* closes below zero than a uniform would, so inverting the uniform reads the scarce discount days as a lower door close to zero. Here is how big the effect is: if the density rises linearly from the lower door to the upper one, then $P(\pi < 0) = \big(a/(a+b)\big)^2$, and the same 44/250 gives $a/(a+b) = 0.420$ and $a/b = 0.72$, more than three times the uniform answer. A rising market pushes the same way, because a NAV that lags a rally adds a positive staleness term $s_t$ to every close.

**The trap:** Answering $44/250 = 0.176$. That is $a/(a+b)$, the lower door's share of the whole room, but the exercise asks for the lower door over the upper door, $a/b$. The second trap is to think the lean makes 0.214 too high. Inflows pile the premium against the creation door, so the census *under*-counts discount days and makes the redemption door look closer than it is.

**If you got this wrong, read:** §20.3.1, "Reading the band: a census and two doors" (and the Math, Gently box on the room with two doors).

**Z.20.2: Kaz's regression**

**Answer:** Kaz's reading is only one of three that fit $\hat\eta = 0.08$. Taken at face value it is internally consistent: at $\eta = 0.08$ a gap has a half-life of 8.3 trading days, and 43% of it is still open after ten. But the attenuation formula allows two other stories. (1) **A noisy ETF:** the NAV is moderately fast, but flow noise dominates the premium. For example, $\eta = 0.4$ with a staleness share of $0.2$, which needs $\sigma_\ell = 1.5\,\sigma_r$. (2) **A fresh NAV:** the evaluator is quick, so there is almost no staleness to find, and even mild flow noise swamps it. For example, $\eta = 0.9$ with $\sigma_\ell = 0.32\,\sigma_r$, which gives a staleness share of $0.089$. The second regression puts the NAV return on lagged ETF returns, one lag at a time. The ratio of successive slopes is $1 - \eta$, and flow noise does not affect it. On ten years of simulated daily data it reads 0.92, 0.60 and 0.10 in the three cases (5th–95th percentiles 0.88–0.95, 0.53–0.67 and 0.06–0.13), so the three stories separate cleanly.

**How:** The formula from §20.2.2 is $\hat\eta \to \eta\,V_s/(V_s + V_\ell)$, where $V_s = \sigma_r^2(1-\eta)^2/\big(\eta(2-\eta)\big)$. A small slope needs either a small $\eta$ or a small staleness share, and the share can be small for two reasons: $V_\ell$ is large, or $V_s$ is small because $\eta$ is large. So the slope is hump-shaped in $\eta$. With $V_\ell/\sigma_r^2 = 0.10$ it peaks at about 0.40 near $\eta = 0.57$ and returns 0.08 at both $\eta \approx 0.08$ and $\eta \approx 0.90$. For the second regression, recall that partial adjustment makes the NAV return a geometric distributed lag of true returns, $\Delta\ln\tilde M_t = \eta\sum_{i \ge 0}(1-\eta)^i r_{t-i}$. The ETF return is $\Delta\ln P_{t-j} = r_{t-j} + \ell_{t-j} - \ell_{t-j-1}$. Regress the first on the second separately for each $j = 0, \dots, 10$:

$$
b_j = \frac{\operatorname{Cov}(\Delta\ln\text{NAV}_t,\ \Delta\ln P_{t-j})}{\operatorname{Var}(\Delta\ln P)} = \frac{\eta(1-\eta)^j\,\sigma_r^2}{\operatorname{Var}(\Delta\ln P)}, \qquad \frac{b_{j+1}}{b_j} = 1 - \eta .
$$

Flow noise is independent of true returns, so it never enters the covariance. It only inflates the common denominator, and the ratio cancels it. Here are the three fingerprints. A slow NAV gives a long, flat tail: about 0.08 at every lag, and still 0.035 at lag 10. A noisy ETF gives small slopes that die within a week, with an extra hump at lag 1 if you run the lags jointly. A fresh NAV puts nearly everything on lag 0. (Instrumenting $p_{t-1}$ with $\Delta\ln P_{t-2}$ recovers $\eta$ too, but in the fresh-NAV case the instrument is weak, because its first stage is $(1-\eta)^2\sigma_r^2$.)

**The trap:** Treating the slope as $\eta$ and stopping there. The wobbling ruler always flattens the slope and never steepens it, so $\hat\eta$ is a lower bound on how fast the NAV catches up, not an estimate of it. The subtler trap is to think the only alternative is "noisy ETF". A very *fresh* NAV also gives a small slope, because there is little staleness for the premium to carry.

NOTE (for the editor): The display just above (20.3) reads $\Delta \ln \text{NAV}_t = \Delta \ln \tilde M_t - \Delta \ln(1 - \bar c_t)$. Since $\text{NAV}_t = \tilde M_t(1 - \bar c_t)$, the sign should be $+\Delta\ln(1-\bar c_t)$. With the printed sign, widening spreads would *raise* NAV returns. The last paragraph of §20.2.2 calls "$-\Delta \ln(1 - \bar c_t)$" a "negative drag", which is true only of $+\Delta\ln(1-\bar c_t)$. The economics is right and the sign is wrong in both places. (20.3) itself is unaffected, because it assumes a constant $\bar c$.

**If you got this wrong, read:** §20.2.2 (the Math, Gently box "A ruler with a wobbling zero" and the attenuation formula), then §20.2.1 for (20.2), and Block 2 of Listing 20.1 (`nav_catchup`).

**Z.20.3: The departing AP**

**Answer:** $\psi$ rises by $1/(1 - 0.4) - 1 = 66.7\%$, a factor of $5/3$. The AP-count paragraph's arithmetic ($J$ identical APs, $\bar\gamma = \gamma/J$) would put the loss of one AP in twenty at $20/19 - 1 = 5.3\%$, and its own 28-to-24 example gives 17%. The real departure costs more than twelve times the head-count estimate. If one of the small APs left instead, $\psi$ would rise by only 3.3%. For the regulator: *The cost of keeping an ETF near its NAV depends on how much balance sheet the APs will commit, not on how many of them have signed agreements, so one AP in twenty can raise the discount that the same selling produces by two-thirds if it carries 40% of the capacity, and by 3% if it carries 3%.*

**How:** Risk tolerances add, so $1/\bar\gamma = \sum_j 1/\gamma_j$, and $\psi = \bar\gamma\,\sigma_b^2 T^{\text{h}}$ is inversely proportional to the street's total tolerance $\mathcal{T}$. The large AP holds $0.4\,\mathcal{T}$, and the other nineteen share $0.6\,\mathcal{T}$, so each holds $0.6/19 = 3.2\%$. When the large AP leaves,

$$
\frac{\psi'}{\psi} = \frac{\mathcal{T}}{0.6\,\mathcal{T}} = \frac{5}{3}, \qquad \text{versus} \qquad \frac{\mathcal{T}}{(1 - 0.6/19)\,\mathcal{T}} = 1.033 \text{ for a small one.}
$$

The count changes by the same one AP in both cases. Only the capacity differs. There is a twist the regulator should see. Measured by the inverse Herfindahl of tolerance shares, the street had about 5.6 *effective* APs before the departure and has 19 after, because the 19 survivors are identical. Concentration "improves" while capacity falls by 40%, so neither the head count nor a concentration index is the right statistic. The right one is total committed balance sheet, which the desk backs out as $\hat\psi$ from (20.5).

**The trap:** Saying $\psi$ rises 40%, as if the lost share passed straight through. $\psi$ scales with $1/\mathcal{T}$, so losing 40% of the capacity raises the price of the rest by $1/0.6 - 1 = 67\%$. The other trap is the head count itself, 5.3%, which is exactly the statistic the exercise asks you to retire.

**If you got this wrong, read:** §20.3.2, the Math, Gently box "A hill, and risk tolerances that add like resistors", and the paragraph after Figure 20.3 on going from 28 APs to 24. Block 3 of Listing 20.1 (`clearing_premium` takes a list of `gammas`, so you can test it directly).

**Z.20.4: Cardinality**

**Answer:** Adding $\chi$ per line gives the problem

$$
\min_{w,\,z}\; k^\top w + \frac{\theta}{2}(w - h)^\top \Sigma (w - h) + \chi\,\mathbf{1}^\top z \quad \text{s.t.} \quad \mathbf{1}^\top w = 1,\quad 0 \le w_i \le z_i,\quad z_i \in \{0, 1\}.
$$

The objective is a convex quadratic in $w$ plus a linear term in $z$, and the constraints are linear, but $z$ is binary. That makes it a mixed-integer QP. A good heuristic is greedy backward elimination. Solve (20.6) with $w \ge 0$, score every line by the exact rise in $J$ from forcing it out, drop the cheapest line while its score is below $\chi$, re-solve, and repeat. We tested it against exhaustive search on eleven random 12-bond instances at three values of $\chi$ each, and it found the optimum all 33 times. Coverage ends up in the 10–35% range because the value of keeping a line grows with the *square* of its weight, while $\chi$ is charged per line. In a 1,300-bond fund, the long tail of small lines fails the test, and the basket becomes the heavy index lines plus the lines with large tilts.

**How:** The cost $\chi\,\#\{i : w_i > 0\}$ is an $\ell_0$ penalty: it is discontinuous at zero and nonconvex, and the binaries $z_i$ (with $w_i \le z_i$ as the big-M link, since $w_i \le 1$) are the standard way to write it. Adding the constraint $w_i = 0$ to the equality-constrained QP on the current set $S$ raises the optimum by

$$
\Delta J_i = \frac{\theta\, w_i^{*2}}{2\, q_i}, \qquad q_i = (\Sigma_S^{-1})_{ii} - \frac{\big((\Sigma_S^{-1}\mathbf{1})_i\big)^2}{\mathbf{1}^\top \Sigma_S^{-1} \mathbf{1}},
$$

which matches a brute-force re-solve to $10^{-17}$. Drop $\arg\min_i \Delta J_i$ while it is below $\chi$, and drop any line the re-solve pushes negative. Two features of the score do the work. It is quadratic in $w_i^*$, so a line at the pro rata weight $\sim 1/N$ is worth $O(1/N^2)$ in tracking, while it costs a full $\chi$. And $1/q_i$ is the line's variance *conditional on the rest*, so a bond with close substitutes is cheap to drop and an idiosyncratic one is expensive. To see the scaling, we extended Listing 20.1's Block 4 to $N$ bonds, with lognormal index weights, 5% of lines axed and $\theta$ scaled with $N$. With $\chi = 0$ the $w \ge 0$ corners keep about 80% of lines at every $N$. At $\chi = 0.05$–$0.5$ bp per line, a 1,300-bond fund keeps 11–26% of its lines, which still carry 35–58% of the index weight and most of the axes. Redemptions add the fund's shadow value $\ell_i$ to the gaps, so they have more lines with big tilts than creations do, which is why redemption coverage runs above creation coverage (about 20% against 10% in Shim–Todorov).

**The trap:** Relaxing $\ell_0$ to $\ell_1$, as in a lasso. On the budget simplex, $\sum_i |w_i| = \mathbf{1}^\top w = 1$ for every feasible basket, so the $\ell_1$ penalty is a constant and selects nothing. The other trap is dropping lines by smallest *weight* rather than by $\Delta J_i$: a small, idiosyncratic line can cost more to drop than a larger one with close substitutes.

NOTE (for the editor): §20.4.3 says "the fractional baskets in the data are the corner solutions of this problem." Listing 20.1's own Block 4 prints `basket coverage 92%` at the $w \ge 0$ corners, and our scaled runs give about 80% at $\chi = 0$. The 10–35% in the data needs the per-line cost of this exercise as well. Suggest "partly the corner solutions of this problem, and partly a fixed cost per line (Exercise 4)."

**If you got this wrong, read:** §20.4.3 (the Math, Gently box "Pegs on springs inside a rubber band", (20.6)–(20.7) and the derivation's remark on $w \ge 0$), §20.4.2 for the coverage ratios, and Block 4 of Listing 20.1 (`basket_qp`), which this exercise extends.

**Z.20.5: The Fed's clause**

**Answer:** Above the upper door, creation is profitable: $\Pi^C = \pi - \pi^{\text{hi}} > 0$ per \$1 of NAV. So APs buy the creation basket, create shares and sell them to the Fed. The transfer to the APs per dollar the Fed spends is

$$
\frac{\pi - \pi^{\text{hi}}}{1 + \pi} \;\approx\; \pi - \pi^{\text{hi}} .
$$

On the chapter's illustrative IG band ($\pi^{\text{hi}} = 20$ bp), a purchase at a 1% premium hands the APs 79.2 bp per dollar. On a position the size of the SMCCF's \$2.47bn of LQD, that would be about \$19.6mm, if all of it had been bought that way (a hypothetical; it was not). The Fed's full overpayment against the bonds' mid value is about 91 bp per dollar. Of that, about 12 bp goes to people who did real work: dealers' half-spread $c^C$, the fund's fee $f^C$ and the AP's costs $k^C$. The remaining 79 bp is the APs' rent.

**How:** From the creation leg of §20.3.1, $\Pi^C_t = (1 + \pi) - \frac{1 + c^C}{1 - \bar c} - f^C - k^C \approx \pi - (\bar c + c^C + f^C + k^C) = \pi - \pi^{\text{hi}}$. This is positive whenever $\pi > \pi^{\text{hi}}$, and it carries no risk, because the buyer is standing there. With $\bar c = c^C = 8$ bp, $f^C = 1$ bp and $k^C = 3$ bp, the exact profit at $\pi = 1\%$ is 79.99 bp per \$1 of NAV. Each dollar of purchases buys $1/(1+\pi)$ dollars of NAV, so the rent is 79.2 bp per dollar. Measured against mid, the overpayment splits as

$$
\pi - \bar c = \underbrace{(\pi - \pi^{\text{hi}})}_{\text{AP rent}} + \underbrace{c^C + f^C + k^C}_{\text{paid for real services}} .
$$

The paragraph: *A bid-side NAV puts a calm IG ETF at a small premium, and a NAV that lags a rally adds a staleness premium on top, so a facility forbidden to buy "above NAV" could not have bought on most ordinary days (JNK closed at a premium on 206 of 250 days in 2025), even though neither the accounting constant $\bar c$ nor the staleness $s_t$ is a transfer to anyone. "Materially exceed" lets the Fed pay those two harmless terms and promises it will not pay above $\pi^{\text{hi}}$, the line beyond which every basis point is a riskless gift to whoever can create shares. The phrase turns "NAV" into "the band": the Fed could bid the discount closed, up to the creation door, and no further. Its mirror, "materially below" on the exit, kept it from selling into the redemption door that it had been brought in to shut.*

**The trap:** Calling the whole premium, $\pi$, the transfer. Part of it is the bid-side constant $\bar c$: the Fed receives bonds worth mid, not bid, so that part is not an overpayment at all. Another $c^C + f^C + k^C$ pays dealers, the fund and the AP's balance sheet for real services. Only $\pi - \pi^{\text{hi}}$ is rent to the APs.

**If you got this wrong, read:** §20.3.1 (the derivation of the creation edge in (20.4)) and §20.5.2, "The Fed buys a seat at the table".

**Z.20.6: The sleeve and the line**

**Answer:** $B$ must exceed **2% of NAV**, and the infimum is exactly 2%. The outflow is 9%, both weeks fall inside the three-week lag, and the sleeve covers 7%, so the gap is $9\% - 7\% = 2\%$. How the 9% splits between the two weeks does not matter (4.5/4.5, 6/3 and 3/6 all trough at $-2\%$). The undrawn fee is $0.5\% \times 2\% = 1$ bp of NAV a year, or \$100k a year per \$1bn of fund, which is cheap next to a 0.65% expense ratio. For Theo: *"Same company as any 13-week borrower with lumpy payables and slow receivables. Beginning cash 7, disbursements of 4.5 in each of the first two weeks, receipts of 4.5 arriving three weeks after each disbursement. Ending cash runs 2.5, −2.0, −2.0, 2.5, 7.0. It's solvent, because the receivables cover every dollar. It's illiquid for two weeks. Size the revolver to the trough plus your minimum-cash cushion, draw it in week 2 and repay it from the first receipt. Then stress the receipts: a longer lag lengthens the draw, and if the outflows keep coming, the trough deepens."*

**How:** This extends Listing 20.1's Block 5. Treat the line as cash that is in the sleeve from week 0, and run `sleeve_path(0.07 + B, [0.045, 0.045, 0, ...], lag_weeks=3)`. The recursion $\phi_{t+1} = \phi_t - R_t + R_{t-3}$ gives

$$
\phi = 0.07 + B,\ \ 0.025 + B,\ \ -0.02 + B,\ \ -0.02 + B,\ \ 0.025 + B,\ \ 0.07 + B, \dots
$$

so survival needs $B > 0.02$. In general, the line has to cover the largest cumulative outflow that falls inside any one lag window, minus the sleeve. When the whole outflow fits inside the lag ($L \ge 2$ weeks here), the depth of the trough is fixed at 2% and the lag sets only its length: one week at $L = 2$, two at $L = 3$, three at $L = 4$. At $L = 1$ the sleeve alone survives. That is Theo's warning from §20.6.1 in numbers. A longer lag lengthens the draw, and a longer lag combined with a longer burn deepens it.

**The trap:** Plugging the burst into (20.8) as if it were a steady rate: $\bar R L_w = 4.5\% \times 3 = 13.5\%$, so $B = 6.5\%$. (20.8) assumes the outflow continues for the whole lag, so for a burst that stops after two weeks it overstates the need by more than three times. A smaller trap is in the code. At $B = 2.00\%$ exactly, `sleeve_path` reports survival only by floating-point luck: its minimum prints as $1.4 \times 10^{-17}$ against a `phi <= 0` test. Mathematically the sleeve touches zero, so quote "just above 2%".

**If you got this wrong, read:** §20.6.1 ("The Full Derivation: the settlement gap" and "The runway in March 2020's weather", including Theo's remark that the lag lengthens in a bad week) and Block 5 of Listing 20.1 (`sleeve_path`).

<!-- STATUS: COMPLETE -->
