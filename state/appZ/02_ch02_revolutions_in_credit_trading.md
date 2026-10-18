## Chapter 2: The Revolutions in Credit Trading

Six exercises, one per revolution that touches a number. Write your answer down before you read ours; the gap is your markout.

**Z.02.1: Censoring**

**Answer:** At $\hat\alpha = 4/3$ the tape shows $0.37/0.67 = 55.2\%$ of true HY volume. To show 80%, the tail index would have to be $\alpha \approx 2.08$, so the hidden blocks would average only 1.93 times the cap (about \$1.9mm, not \$4mm).

**How:** Take one average trade. A capped print shows the cap $c = 1$ but is really worth the Pareto conditional mean $m = c\alpha/(\alpha-1)$, which is 4 at $\alpha = 4/3$. Uncapped prints show their true size, so

$$
S(\alpha) = \frac{p\,c + (1-p)\,\mu}{p\,c\,\alpha/(\alpha-1) + (1-p)\,\mu} = \frac{0.1 + 0.27}{0.4 + 0.27} = 0.552 .
$$

For the 80% case, solve $0.37/(0.1\,m + 0.27) = 0.8$, which gives $m = 1.925$, and then invert the moment with $\hat\alpha = m/(m-c) = 1.925/0.925 = 2.08$. Here is what the desk can see. One trade in ten carries 60% of the volume ($0.40/0.67$), and only a quarter of that 60% reaches the screen. Seeing four-fifths of the money would take a tail thin enough to have finite variance ($\alpha > 2$), which is the opposite of what Ben Dor's imputation implies for HY. The blind spot is structural, and it sits on the large HY tickets.

**The trap:** The most common slip is to stop at $m = 1.925$ and report "$\alpha \approx 1.9$". That number is the hidden-block mean measured in caps, not the tail index; you still have to apply $\alpha = m/(m-c)$. The runner-up answer is "90%", which counts tickets instead of dollars. Dropping the capped prints entirely gives 40%. That is Femi's dead-battery loader.

**If you got this wrong, read:** §2.2.2, especially "The Full Derivation: the tail index from one moment".

**Z.02.2: The ceiling**

**Answer:** $\hat r(K)$ is strictly decreasing in $K$. With US HY at 6% (2015) and 32% (2025):

| $K$ | $\hat r$ (per year) | odds double every | midpoint $\hat t_0$ | 2030 projection |
| :-- | :-- | :-- | :-- | :-- |
| 0.5 | 0.257 | 2.7 yrs | 2022.8 | 43.3% |
| 0.6 | 0.233 | 3.0 yrs | 2024.4 | 47.1% |
| 0.8 | 0.211 | 3.3 yrs | 2026.9 | 52.5% |
| 1.0 | 0.200 | 3.5 yrs | 2028.8 | 56.1% |

Spec line for ROBO: "`K` is a sourced input, never a fitted knob: two points fit every `K` exactly, so `K = 0.5` must cite outside evidence in `OBS.source`, because it raises $\hat r$ from 0.20 to 0.26, moves the HY midpoint back to 2022 and asserts that half of HY never leaves the phone."

**How:** Write the slope as two pieces:

$$
\hat r(K)\,(t_2 - t_1) = \ln\frac{e_2}{e_1} + \ln\frac{K - e_1}{K - e_2},
\qquad
\frac{d}{dK}\ln\frac{K - e_1}{K - e_2} = \frac{e_1 - e_2}{(K - e_1)(K - e_2)} < 0 .
$$

The derivative is negative because $e_1 < e_2 < K$ makes the numerator negative and both factors of the denominator positive. As $K \downarrow e_2$ the slope blows up, and as $K \to \infty$ it falls to $\ln(e_2/e_1)/(t_2 - t_1) = 0.167$, which is a plain constant growth rate. So ROBO's 103% is the logistic with the ceiling taken away. For the projection, $z_{2030} = z_{2025}(K) + 5\,\hat r(K)$ and $\hat e_{2030} = K/(1 + e^{-z_{2030}})$. Listing 2.1's `fit_adoption(..., K=0.5)` reproduces the table.

**The trap:** People expect a lower ceiling to mean slower adoption, so they call $K = 0.5$ "conservative". It lowers the level and *raises* the rate, and it puts HY past its inflection point already. The second trap is to choose $K$ by goodness of fit. With two points every $K$ fits perfectly, so the data cannot price this assumption, and somebody has to.

**If you got this wrong, read:** §2.3.1 and "The Full Derivation: fitting a ceiling from two points".

**Z.02.3: Order statistics**

**Answer:** $\mathbb{E}[\delta_{(1)}] = b/(n+1)$. No number of dealers anchored at $\phi = 0.6$ matches two independent ones, because $n_{\text{eff}} < 1/\phi = 5/3 < 2$ for every $n$. A twelfth anchored connection moves $n_{\text{eff}}$ from 1.571 to 1.579 and improves the expected best quote by $0.003\,\theta$, about 0.5%.

**How:** The best quote exceeds $x$ only if all $n$ quotes do, so $\Pr(\delta_{(1)} > x) = (1 - x/b)^n$ on $[0, b]$, and the tail integral gives

$$
\mathbb{E}[\delta_{(1)}] = \int_0^b \left(1 - \frac{x}{b}\right)^n dx = \frac{b}{n+1}.
$$

For the anchored model of §2.3.2, $\mathbb{E}[\delta_{(1)}]/\theta = \phi + (1-\phi)/n$. That is always above $\phi = 0.6$, and two independent dealers give $1/2$. Equivalently, solving $n/(1 + (n-1)\phi) = 2$ gives $n = 2(1-\phi)/(1-2\phi) = -4$, and there is no positive solution whenever $\phi > 1/2$. So what you buy with a new connection is a lower $\phi$, not a higher $n$. A twelfth line that quotes off the same composite is worth 0.5% of $\theta$. One with its own fair value that cut $\phi$ to 0.5 would be worth 14.5%. Pay for independence, and test for it with the winner measured against an independent mark, not with the cover gap.

**The trap:** The algebra returns $n = -4$, and a tired reader drops the sign and writes "four anchored dealers". A negative count means "impossible". On the uniform part, people carry over the exponential's $b/n$; the uniform has a hard edge at 0, and that edge costs the $+1$.

**If you got this wrong, read:** §2.3.2 and "The Full Derivation: best-of-$n$ with a common anchor".

**Z.02.4: Units**

**Answer:** $\mathrm{TC} = 50/2 + 3 + 2 = 30$ bp of price, one way. The 55 bp figure overstated cost by $55/30 = 1.83$ times, so it cut optimal turnover to $(30/55)^2 = 0.30$ of its correct value, a 70% cut. The right optimum is 3.36 times the wrong one, and optimal net alpha was understated by the factor $30/55 = 0.55$.

**How:** LCS is a round trip, while Man's three terms are one-way bp of price, so convert the LCS before adding anything: $\mathrm{LCS}/2 = 25$ bp. Then

$$
\frac{\mathrm{TO}^\star_{\text{wrong}}}{\mathrm{TO}^\star_{\text{right}}} = \left(\frac{c_{\text{right}}}{c_{\text{wrong}}}\right)^2 = \left(\frac{30}{55}\right)^2 = 0.298 .
$$

With the chapter's illustrative $k = 0.0048$, that is 0.19 turns a year against 0.64. Listing 2.3's `man_tc_bp` would have accepted the junior's inputs without complaint, since its guards check sign and order but not round trip against one way.

**The trap:** Halving the whole 55 to get 27.5 bp. Slippage and calibration were already one-way, so only the LCS gets halved. The second trap is reporting the turnover effect as 1.83 times; turnover goes as $1/c^2$, so square the ratio.

**If you got this wrong, read:** §2.9.1 ("Units first") for the halving, and §2.9.2 for the $1/c^2$.

**Z.02.5: The router and Mags**

**Answer:** With $\chi_A = 1.5$ bp, all-to-all goes first when $\pi_A > 1.5/5.8 = 0.259$, which is fill odds above 0.349. With $\chi_A = 6$ bp the bar becomes $\pi_A > 6/10.3 = 0.583$, fill odds above 1.395. At the BBB's 55% fill rate, all-to-all-first now costs 8.64 bp against 8.3 bp straight to dealers, so the router skips it.

Theo's note: "$\chi_A$ raised from 1.5 to 6 bp by desk judgment, not estimate: the name is about three weeks from a likely uptier, the anonymous pool is full of holders reading the same 8-K, and a failed inquiry tells them a holder wants out before the deal, so a miss moves the price about four times as far as on a calm BBB; replace with markouts of failed A2A inquiries in LMT-flagged names."

**How:** Going first is better if and only if $\pi_A(J_R - c_A) > (1 - \pi_A)\chi_A$. Solve for the probability rather than the odds:

$$
\pi_A^{\min} = \frac{\chi_A}{\chi_A + J_R - c_A}, \qquad \frac{1.5}{1.5 + 4.3} = 0.259, \qquad \frac{6}{6 + 4.3} = 0.583 .
$$

Check: at the threshold, $J_{A \to R} = \pi c_A + (1-\pi)(\chi_A + J_R) = 8.3 = J_R$. Holding $c_A$ and $J_R$ fixed is generous, too. Near an uptier both rise and $\pi_A$ falls, which is why Listing 2.4's `try_a2a_first` stress case, with $\pi_A = 0.25$, says no by a wide margin.

**The trap:** Reading the odds threshold as a probability. That gives "$\pi_A > 0.35$" in the calm case, and in the stressed case "the threshold is 1.40, a probability can't exceed 1, so all-to-all never goes first." Convert with $\pi = o/(1+o)$.

**If you got this wrong, read:** §2.5.1, "The Full Derivation: the sequential router".

**Z.02.6: Data-exhaust theorem**

**Answer:** $\mathrm{TO}^\star$ solves $k/(2\sqrt{\mathrm{TO}^\star}) = c_0 + 2c_1\,\mathrm{TO}^\star$, and at the optimum $\alpha^{\text{net}\,\star} = c_0\,\mathrm{TO}^\star + 3c_1\,\mathrm{TO}^{\star 2}$. The elasticities with respect to $c_0$ are $2c_0/(c_0 + 6c_1\mathrm{TO}^\star) < 2$ for turnover and $c_0/(c_0 + 3c_1\mathrm{TO}^\star) < 1$ for net alpha. Illustration, with $k = 0.0048$ and $c_1 = 1$ bp per turn: cutting $c_0$ from 12 to 7.5 bp moves $\mathrm{TO}^\star$ from 2.16 to 3.08 turns (1.43 times, not 2.56) and net alpha from 40.0 to 51.7 bp (1.29 times, not 1.6). As $c_0 \to 0$, turnover stalls at $(k/4c_1)^{2/3} = 5.2$ turns.

**How:** Net alpha is

$$
\alpha^{\text{net}}(\mathrm{TO}) = k\sqrt{\mathrm{TO}} - c_0\,\mathrm{TO} - c_1\,\mathrm{TO}^2,
$$

which is concave, since its second derivative $-k/(4\mathrm{TO}^{3/2}) - 2c_1$ is negative. The first-order condition is a cubic in $\sqrt{\mathrm{TO}}$ with one positive root. You don't need Cardano: differentiate the condition implicitly, $d\mathrm{TO}^\star/dc_0 = -1/\big(k/(4\mathrm{TO}^{3/2}) + 2c_1\big)$, and use the condition itself to replace $k/(4\mathrm{TO}^{3/2})$ with $(c_0 + 2c_1\mathrm{TO})/(2\mathrm{TO})$. Simplifying gives the elasticity $2c_0/(c_0 + 6c_1\mathrm{TO}^\star)$, which equals 2 only when $c_1 = 0$. For alpha, the envelope theorem gives $d\alpha^\star/dc_0 = -\mathrm{TO}^\star$. Substituting $k\sqrt{\mathrm{TO}^\star} = 2c_0\mathrm{TO}^\star + 4c_1\mathrm{TO}^{\star 2}$ gives $\alpha^\star$ and its elasticity.

The 4 p.m. link is that $c_1$ is the crowding slope. The index mark took 15.5% of all corporate volume in Q1 2026, against 5% in 2016, and nearly half of PT volume prints at or after it (§2.6.2). A book that turns over more pushes more through the window where everyone else rebalances, against dealer balance sheet that is finite at 4 p.m., so its per-unit cost rises with its own turnover. Note that the elasticity *falls* as $c_0$ falls: the cheaper tickets get, the more crowding sets capacity. The 2.56 of §2.9.2 is therefore a ceiling, not a forecast. Estimate $c_1$ as a time-of-day term in the cost model. A backtest that fills at the mark has set $c_1 = 0$ at the most crowded print of the day.

**The trap:** Setting marginal benefit equal to *average* cost, $k/(2\sqrt{\mathrm{TO}}) = c_0 + c_1\mathrm{TO}$, which drops the factor 2. That overshoots turnover (4.20 turns against 3.08 at $c_0 = 7.5$ bp) and gives up 2.4 bp of alpha. It is the right condition only when the crowding comes from other people's turnover and yours is too small to move it. Plugging $c(\mathrm{TO}^\star)$ into $k^2/4c^2$ makes the same mistake.

**If you got this wrong, read:** §2.9.2, "The Full Derivation: optimal turnover under linear cost", then the index-mark rows of the Trend Watch in §2.6.2.

<!-- STATUS: COMPLETE -->
