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

**If you got this wrong, read:** §18.6.1 (*The Full Derivation* and "Random jump sizes"), the Math, Gently boxes "The exponential of a wobble, and Jensen's inequality" (§18.4.3, Step 1) and "The jump's exponential" (§18.6), and Chapter 5, §5.5.2 for the Beta recovery.

**Z.18.3: Roll, one size at a time (Core, data)**

**Answer:** Your extract will give its own numbers, but the pattern is reliable. The two small buckets return spreads: odd lots the widest, because retail pays the most, and \$100k–\$1mm narrower. They have many prints close together, and their trade signs are nearly independent. The \$1–5mm bucket returns a number on liquid names and sometimes NaN on thin ones. The capped "5MM+" bucket is the usual NaN. Even when it does return a number, splitting shrinks the bounce, so in a large sample the estimate converges to $S(1-\rho)$: 40% of the true spread at $\rho = 0.6$. On a high-yield bond the \$1–5mm bucket is empty by construction, because every size above \$1mm prints as "1MM+". A synthetic quarter run through Listing 18.1 (2,000 paths each; illustrative inputs) shows all of this:

| Bucket | True $S$ | $\rho$ | Prints | $S(1-\rho)$ | Median estimate | NaN share |
| :-- | --: | --: | --: | --: | --: | --: |
| $<$\$100k | 0.60 | 0.0 | 2,000 | 0.600 | 0.600 | 0% |
| \$100k–\$1mm | 0.30 | 0.1 | 600 | 0.270 | 0.270 | 0% |
| \$1–5mm | 0.15 | 0.3 | 150 | 0.105 | 0.113 | 11% |
| Capped | 0.10 | 0.6 | 60 | 0.040 | 0.156 | 45% |

The mid moves 0.05, 0.08, 0.15 and 0.25 points between consecutive prints in the four buckets, because big prints are days apart. With 400,000 capped prints and a quiet mid, the estimate settles at 0.040.

**How:** With trade signs following a Markov chain of persistence $\rho$, so that $\text{Cov}(I_t, I_{t+j}) = \rho^{|j|}$, expand the bounce term by term:

$$
\text{Cov}(I_t - I_{t-1},\, I_{t+1} - I_t) = \rho - 1 - \rho^2 + \rho = -(1-\rho)^2
\quad\Longrightarrow\quad
\widehat S^{\text{Roll}} \to S(1-\rho).
$$

Splitting a \$25mm sell into five \$5mm prints puts same-side prints next to each other. The price only bounces when the side changes, which now happens with probability $(1-\rho)/2$ instead of $\tfrac12$. The NaNs come in three kinds, and the second number `roll_spread` returns tells them apart. If the autocovariance is also NaN, there were fewer than `min_obs + 2` prints: no data. If it is positive in a bucket whose prints are days apart, the mid's diffusion has buried the bounce, and the sign is a coin toss. If it is positive and persistent across sessions, a split order with informed drift is behind it, which is information (the Altice replay). Two fixes are worth knowing. Enhanced TRACE carries the reporting side, so you can estimate $\hat\rho$ from the signs and divide by $1 - \hat\rho$, or regress $\Delta p_t$ on $\Delta I_t$, which needs no assumption about the sign process. And drop one leg of each interdealer trade *before* bucketing (`clean_trace`, Listing 18.6), or the duplicate prints add zero-width bounces.

**The trap:** Reading the small capped estimate as "blocks are cheap." Blocks do cost less per bond (Edwards, Harris & Piwowar 2007), but Roll understates even that by the factor $1-\rho$. The opposite trap is trusting any number from a 60-print bucket. A surviving estimate there is noise that happened to be negative, which is why its median, 0.156, sits *above* the true 0.10. "Too small" is a large-sample statement. In a thin bucket the bigger problem is that the estimate is mostly noise. And never rescue a NaN with `abs()`.

**If you got this wrong, read:** §18.2.1 (the splitting derivation and Ways This Blows Up items 2 to 4), the Ben Dor annotation on stale prints in §18.2, and §18.8 on the "5MM+" and "1MM+" caps.

**Z.18.4: Three envelopes or eight (Core)**

**Answer:** The winner's-curse shading is $\sigma_\varepsilon e_n$: $0.75 \times 0.846 = 0.635$ points with 3 dealers and $0.75 \times 1.424 = 1.068$ points with 8, so the eight-dealer list needs 0.43 points more. The equilibrium has two halves. Given *your own read*, the equilibrium bid falls a little as $n$ goes from 3 to 8: you shade 1.13 points below your read with 3 dealers and 1.26 with 8. But the *winning* bid, which is what the seller receives, rises: it sits 0.50 points below true value with 3 dealers and 0.20 with 8. The winner's curse lowers every bid. Competition raises the price.

**How:** For $e_n$, use the integral of §18.9 (Listing 18.7's `expected_max_std_normal`). The case $n = 3$ has the closed form $3/(2\sqrt\pi) = 0.8463$. For the equilibrium, use the symmetric first-price bid with affiliated signals (Milgrom & Weber 1982), $b(x) = v(x,x) - \int L(\alpha \mid x)\,dv(\alpha,\alpha)$. Here $v(x,x)$ conditions on *tying* with the best rival, not on beating everyone. With the chapter's diffuse prior and normal errors, everything is translation-invariant, so

$$
b_n(x) = x - \sigma_\varepsilon\big(a_n + 1/h_n\big), \qquad
a_n = \frac{\int z\,\phi(z)^2\Phi(z)^{n-2}dz}{\int \phi(z)^2\Phi(z)^{n-2}dz}, \qquad
h_n = n(n-1)\!\int\!\phi(z)^2\Phi(z)^{n-2}dz .
$$

At $n = 3$, $a_3 = 0.33$ and $1/h_3 = 1.18$. At $n = 8$ they are $0.98$ and $0.70$. The pivotal winner's curse ($a_n$) grows with $n$ and the competitive margin ($1/h_n$) shrinks. From 3 to 8 bidders the first effect wins, by 0.13 points at $\sigma_\varepsilon = 0.75$, so the bid on a given read falls. The seller's price is the top of $n$ reads, $V + \sigma_\varepsilon e_n$, minus that shade. In the chapter's framing, "$e_n$ first, then strategic shading", the strategic part is $\sigma_\varepsilon(a_n + 1/h_n - e_n)$. That is 0.50 points at $n = 3$ and 0.20 at $n = 8$, and it is exactly the winner's expected profit and the seller's expected shortfall. (A quadrature best-response check confirms that no bidder gains by deviating from $b_n$, and a 400,000-draw Monte Carlo reproduces both shortfalls.)

**The trap:** Answering with one effect. "More dealers, more competition, higher bids" is true of the clearing price and false of your bid on a given read. "More dealers, bigger curse, lower bids" is true of your bid and false of the seller's proceeds, which rise. The quieter trap is quoting $x - \sigma_\varepsilon e_n$ as the equilibrium bid. That bid only breaks even. Everyone in equilibrium shades further, by 0.50 points with three dealers.

**If you got this wrong, read:** §18.9 (the Math, Gently box "The winner is the most wrong" and *The Full Derivation*), the Poker Table in §18.3.3 on Fermanian, Guéant & Pu, and Listing 18.7.

**Z.18.5: ROBO maximizes the hit ratio (Warm-up)**

**Answer:** One week later ROBO's hit ratio is close to 100%. To get there it bids through the composite ("par for everything", in the Debrief's spec box) and offers through it on the other side. Its inventory is therefore the street's net customer flow: long every bond a client wanted out of, heaviest in the names where selling was one-sided. Those are the falling names, the ones whose sellers had read something or had a margin call, and ROBO now holds many times its limit $Q$ in them. Its markouts are negative on every fill on the trade date, because it paid through the composite. On the Halvorsen ticket, a par bid for \$8mm loses 8.75 points, or \$700,000, at the composite, and \$1.12mm at the 86 print. Its 1-, 5- and 20-day residual markouts are worst in the tiers that know something. At a 5% hit ratio other dealers absorbed most of that flow; now ROBO owns all of it. The e-mail from risk reads: *inventory limit breached in [N] names; every fill marked below cost on day zero; 20-day markouts worst in the event-driven tier; auto-quoter suspended pending review.* The fix makes hit ratio a constraint, not the objective, and a quality-adjusted one at that:

$$
\max_{x}\ \sum_i P(x_i)\,(x_i - d_i)\quad\text{s.t.}\quad \frac{\sum_i w_{c(i)}P(x_i)}{\sum_i w_{c(i)}} \ge h^{*},\qquad |q + n_i| \le Q ,
$$

where $w_c$ is the weight tier $c$ gets for the quality of its residual markouts, and zero for a toxic tier.

**How:** The win curve $P(x)$ falls as $x$ rises, so "maximize $P$" has no interior optimum. It runs to $x \to -\infty$, the boundary, and nothing in the objective stops it. Put the hit ratio in as a constraint and the Lagrangian gives the chapter's first-order condition, $x^{*} = d - \nu_c + \text{greed}(x^{*})$: the target becomes a subsidy $\nu_c \ge 0$ per tier, it is zero whenever the target is already met, and it is zero on the toxic tier by construction. Listing 18.5's 4,000-RFQ synthetic book prices the whole menu. The profit-maximizing desk ($\nu = 0$) wins 5.4% of RFQs and earns $+0.015$ points per RFQ after expected markouts. A raw 25% target ($\nu = 0.54$) earns $-0.047$. ROBO's 99% ($\nu = 6.7$ points) earns $-1.71$ points per RFQ, about \$68mm on 4,000 one-lot RFQs, and toxic flow rises from 10% of its wins to 29%, which is simply its share of all the flow.

**The trap:** "Fixing" ROBO with a raw hit-ratio target. That is Niang's warning. A flat $\nu$ raises the win rate fastest where other dealers shade hardest, in the toxic tiers. In the same synthetic book the raw 25% target lifts toxic flow from 10.4% of wins to 15.1%. The quality-adjusted version, with $\nu$ withheld from the toxic tier, cuts it to 2.6% and loses less per RFQ ($-0.036$ against $-0.047$), at the price of a 21.8% hit ratio instead of 25%. The other trap is calling ROBO's markouts bad luck. Winning every hand means you hold every hand anyone wanted to fold. That is the Poker Table's point.

**If you got this wrong, read:** §18.7 ("Franchise", the panel-review e-mail, and the Specification box for Listing 18.5), the Poker Table in §18.3.3, and the Desk Debrief's *The Spec You Hand the Robot* (§18.10) for the inventory guard.

**Z.18.6: How busy must a bond be for AS to be right? (Stretch, code)**

**Answer:** $A \approx 14.4$ RFQs per trading day per side at zero distance. That is 14.43 from `glft_stationary` with the listing's $Q = 20$, 14.38 once the wall is far enough away not to matter ($Q \ge 40$), and 14.28 from the closed form (18.6). It is 7.2 times the chapter's $A = 2$. At the dealer's actual quote, about a third of a point from the mid, that becomes $Ae^{-k\delta} \approx 5.3$ fills a day on *each* side, or roughly 2,700 trades a year. So a one-week AS horizon is right only for a bond that trades about ten times a day, which describes a benchmark issue, not an off-the-run B3. On the chapter's twice-a-day bond, AS skews too little by a factor of 2.7: 0.0063 points per lot against GLFT's 0.0171.

**How:** Work per trading day throughout: $\sigma^2 = 64/252$, $\gamma = 0.005$, $k = 3$. The one-week AS skew per lot is $\gamma\sigma^2\tau = 0.005 \times 0.254 \times 5 = 0.00635$ points. From `glft_stationary`, read the skew as the step in the bid distance near flat, $\delta^b(1) - \delta^b(0)$, which matches the slide of the quote centre per lot, $c(0) - c(1)$ with $c(q) = \tfrac12(\delta^a_q - \delta^b_q)$, to six decimals. It falls monotonically in $A$, so `brentq` on $A \in [1, 100]$ finds the root. Cross-check with the closed form by setting $\omega(A) = \gamma\sigma^2\tau$:

$$
A^{*} = \frac{(1+\gamma/k)^{1+k/\gamma}}{2k\gamma\sigma^2\tau^2} = \frac{2.7205}{0.1905} = 14.28,
\qquad\text{or}\qquad A^{*} = 2\Big(\frac{\tau_{\text{eff}}(2)}{5}\Big)^2 = 2\Big(\frac{13.36}{5}\Big)^2 = 14.3,
$$

because $\tau_{\text{eff}} \propto A^{-1/2}$. The 1% gap between the solver and the closed form comes from the discreteness of the inventory grid, since (18.6) treats $q$ as continuous. At $A = 2$ the listing's stationary skew is 0.01713, which is the "about 2.7 times" of Figure 18.2.

**The trap:** Mixing clocks. With $\sigma$ per $\sqrt{\text{yr}}$, $\tau$ in days and $A$ per day, the answer comes out 252 times too small. With $\tau$ in years and everything else per day, it comes out $252^2$ times too large. Pick one unit and convert outside the function, as the Spec demands. The conceptual slip is expecting a *busier* bond to need *more* skew. It needs less, since the skew scales like $A^{-1/2}$: the street forgets your position faster. Nor does "A cancelled" from §18.4 mean $A$ is irrelevant: it cancels from the greed, not from the fear. One more thing to watch: with a tight limit, say $Q = 10$, no $A$ works at all. The wall alone forces a skew of about $\pi^2/\big(4k(Q+1)^2\big) = 0.0068$ points per lot, and `glft_stationary` bottoms out at 0.0069, above the AS target.

**If you got this wrong, read:** §18.5 (the Math, Gently box "A marble in a bowl", (18.6), and *The Full Derivation*), the Units box in §18.4.4, and Listing 18.4 (`glft_stationary`, `glft_omega`).

<!-- STATUS: COMPLETE -->
