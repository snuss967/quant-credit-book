## Chapter 18: OTC Credit Microstructure & the Market Maker's Equations

Six exercises: one on greed, one on fear with lawyers in it, one on the tape, one on the sealed envelope, one on ROBO, and one on how busy a bond has to be before Avellaneda–Stoikov tells the truth. Every number below was recomputed from the chapter's formulas and Listings 18.1 to 18.7 (Appendix F). Write your card before you read ours.

**Z.18.1: Why a fearless dealer still has a spread (Warm-up)**

**Answer:** The per-side markup has the expansion

$$
\frac1\gamma\ln\!\Big(1+\frac\gamma k\Big) = \frac1k - \frac{\gamma}{2k^2} + \frac{\gamma^2}{3k^3} - \cdots \;\longrightarrow\; \frac1k ,
$$

and $\delta^{*} = 1/k$ maximizes $\delta A e^{-k\delta}$. With Kaz's $k = 3$ and $\gamma = 0.005$, the markup is 0.33306 points against the limit of 0.33333, so his fear changes his greed by 0.0003 points, under a four-hundredth of an eighth. The fearless dealer quotes 1/3 of a point each side, a spread of $2/k = 0.667$ points, and keeps $A/e$ of the business: 184 of the 500 RFQs a year in the §18.4 box.

**How:** Put $x = \gamma/k$ into $\ln(1+x) = x - x^2/2 + x^3/3 - \cdots$ and divide by $\gamma$, or use L'Hôpital on the $0/0$. For the second part, the expected markup earned per unit time is $\delta\,\Lambda(\delta)$, and

$$
\frac{d}{d\delta}\big(\delta A e^{-k\delta}\big) = A e^{-k\delta}(1 - k\delta) = 0 \;\Longrightarrow\; \delta^{*} = \frac1k ,
$$

with second derivative $-kAe^{-1} < 0$ there, so it is a maximum. The same answer drops out of the general first-order condition (18.2): as $\gamma \to 0$, $y^{*} \to -\Lambda/\Lambda' = 1/k$. Here is what to tell Kaz. Fills fall off with elasticity $k\delta$, so the dealer backs away from the mid until one more tick of margin costs exactly as many fills as it earns, which is unit elasticity. That is the textbook monopoly markup, with a marginal cost of zero because a risk-neutral dealer values the bond at the mid. Fear prices the inventory. Greed prices the client's lack of an alternative, and only competition, a larger $k$, takes it away. Notice too that $A$ has dropped out: how often you are asked does not set the markup.

**The trap:** "Risk-neutral means quoting at the mid." That is the answer for infinitely elastic demand ($k \to \infty$), not for $k = 3$. The mechanical version of the same mistake is to set $\gamma = 0$ in the formula, get $\ln(1)/0$, and call the markup undefined or zero. That is why Listing 18.3's `as_greed` switches to $1/k$ below $\gamma = 10^{-12}$. A smaller slip is to report $1/k$ as the whole spread: it is the markup per side, and the spread is $2/k$.

**If you got this wrong, read:** §18.4.2 (*Limit 1*), §18.4.3 Step 3 for (18.2) and (18.3), and the Math, Gently box "Why $\ln(1+x)$ is almost $x$".

**Z.18.2: Recovery is what you get, eventually (Stretch)**

**Answer:** With i.i.d. jump sizes $J = s - 100R$ and $R \sim \text{Beta}(a,b)$, the certainty equivalent becomes

$$
\theta(q) = q(s + \mu\tau) - \tfrac12\gamma q^2\sigma^2\tau - \frac{\lambda^{\mathbb{P}}\tau}{\gamma}\big(M_J(\gamma q) - 1\big),
\qquad
r^{b} = s + \mu\tau - (1+2q)\frac{\gamma\sigma^2\tau}{2} - \frac{\lambda^{\mathbb{P}}\tau}{\gamma}\big[M_J(\gamma(q+1)) - M_J(\gamma q)\big],
$$

with $r^a$ the same using $M_J(\gamma q) - M_J(\gamma(q-1))$. For a flat or long dealer, recovery uncertainty *lowers* the bid below the bid with recovery fixed at its mean. For a short dealer it *raises* it. Take the cold-open numbers ($s = 91.25$, $\gamma = 0.005$, $q = 3$, $\lambda^{\mathbb{P}}\tau = 0.025$ over one week) and a mean recovery of 40, so $\bar J = 51.25$. The jump term in $r^b$ is then 3.15 points with $R$ fixed, 3.19 with $R \sim \text{Beta}(40, 60)$ (Listing 18.4's test case, standard deviation 4.9 points), and 3.78 with $R \sim \text{Beta}(2, 3)$ (standard deviation 20 points). The lawyers cost 0.04 points of bid in the first case and 0.63 in the second. A dealer short 3 lots bids 0.05 points *higher* under $\text{Beta}(2,3)$.

**How:** Let the gaps $J_1, J_2, \dots$ be i.i.d., independent of $N$ and $W$, so $S_T = s + \mu\tau + \sigma W_\tau - \sum_{i \le N_\tau} J_i$. Conditional on $N_\tau = n$, $\mathbb{E}\big[e^{\gamma q\sum J_i}\big] = M_J(\gamma q)^n$, and averaging over the Poisson count gives

$$
\mathbb{E}\big[e^{-\gamma q S_T}\big] = \exp\!\Big(-\gamma q(s + \mu\tau) + \tfrac12\gamma^2q^2\sigma^2\tau + \lambda^{\mathbb{P}}\tau\big(M_J(\gamma q) - 1\big)\Big).
$$

So $M_J(\gamma q)$ replaces $e^{\gamma qJ}$ in $\theta$, and $r^b = \theta(q+1) - \theta(q)$ follows. The fixed-$J$ factorization $e^{\gamma qJ}(e^{\gamma J} - 1)$ does not survive the expectation, because the new lot and the old lots share one recovery. To sign the effect, write the bid's jump term as $\mathbb{E}[g(J)]$ with $g(J) = e^{\gamma(q+1)J} - e^{\gamma qJ}$. Then $g''(J) = \gamma^2 e^{\gamma qJ}\big[(q+1)^2e^{\gamma J} - q^2\big] > 0$ for $q \ge 0$, so Jensen gives $\mathbb{E}[g(J)] \ge g(\mathbb{E}[J])$ and the bid falls. At $q = -1$, $g$ is concave and the inequality flips. For small $\gamma$, the jump term is $\lambda^{\mathbb{P}}\tau\big(\mathbb{E}[J] + \gamma(q + \tfrac12)\mathbb{E}[J^2]\big)$, so uncertainty moves the bid by $-\lambda^{\mathbb{P}}\tau\,\gamma(q+\tfrac12)\operatorname{Var}(J)$, and the jump variance in the fear term becomes $\lambda^{\mathbb{P}}\mathbb{E}[J^2]$. Here, though, $\gamma(q+1)J \approx 1$, so the expansion gets the sign right and the size wrong (0.175 points against the exact 0.63). Integrate the MGF numerically, as `jump_mgf_beta` in Listing 18.4 does.

**The trap:** Factoring the bid term as $M_J(\gamma q)\big(M_J(\gamma) - 1\big)$, as if every lot drew its own recovery. That gives 3.36 points instead of 3.78 and misses two-thirds of the effect. The second trap is "uncertainty always lowers the bid." Jensen on $M_J(\gamma q) \ge e^{\gamma q\mathbb{E}[J]}$ lowers the certainty equivalent $\theta(q)$ for every $q \ne 0$, longs and shorts alike. But a bid is the *difference* $\theta(q+1) - \theta(q)$. For a short dealer, buying shrinks the uncertain exposure, so uncertainty makes the dealer keener to buy.

NOTE (for the editor): the "Random jump sizes" paragraph of §18.6.1 says to "Replace $e^{\gamma qJ}$ with the moment generating function $M_J(\gamma q)$." That is exact inside $\theta(q)$. In (18.7) as printed, though, $e^{\gamma qJ}$ multiplies $(e^{\gamma J} - 1)$ in $r^b$, and $\sinh(\gamma J)$ in $r^{\text{res}}$, and a literal swap there gives $M_J(\gamma q)(M_J(\gamma) - 1) = 3.36$ points, or 3.29 if $e^{\gamma\bar J}$ is kept in the second factor, against the correct $M_J(\gamma(q+1)) - M_J(\gamma q)$ of 3.78 (inputs above, $\text{Beta}(2,3)$ recovery). Suggest adding "in $\theta(q)$", or writing the bid's jump term in the difference form.

**If you got this wrong, read:** §18.6.1 (*The Full Derivation* and "Random jump sizes"), the Math, Gently boxes "The exponential of a wobble, and Jensen's inequality" (§18.4.3, Step 1) and "The jump's exponential" (§18.6), and Chapter 5, §5.5.2 for the Beta recovery.

