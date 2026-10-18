# Appendix Z (continued): Solutions for Parts V to VIII

The second half of Appendix Z, in the same form: the number first, then the method, then the trap,
and the section to reread.

## Part V: Market Microstructure, Portfolio Trading, ETFs & Loans

### Z.18 Chapter 18: OTC Credit Microstructure & the Market Maker's Equations

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

### Z.19 Chapter 19: Portfolio Trading & Basket Pricing Engines

Six exercises, all on the cold-open basket. The first finds the two lines, the next three break the engine in three ways (a stressed tape, a stale universe and a variance bump), and the last two turn the arithmetic toward the buy side and the two-way list. Every number below was recomputed by running Listings 19.1 to 19.8 (Appendix F) in one interpreter. Write your card before you read ours.

**Z.19.1: Find the two lines**

**Answer:** On `price_pt(b0, evict=False)` the cost terms of (19.6) come to $\mathcal{C}=$ \$1,542k. That is 75.5bp of the \$204.3mm market value, or \$1,558k and 76.3bp once the \$16k hedge half-spread is added. The 150 exact removal savings sum to \$1,654k, which is \$111k (7.2%) more than $\mathcal{C}$, and that \$111k is exactly $\tfrac12\gamma\sum_{i\ne j}x_i\Sigma^{\text{res}}_{ij}x_j$. Ranked by $\Delta_j/\text{MV}_j$, two lines stand far apart from the rest:

- **L117** is at 1,093bp: a \$359k saving on \$3.28mm, of which \$339k is AS.
- **L042** is at 307bp: a \$526k saving on \$17.1mm, made up of \$330k of handling and \$191k of risk.

The third line, L052, is at 81bp, against a basket average of 75.5bp. The two lines carry 57% of the cost on 10% of the market value, and evicting both leaves 35.8bp.

**How:** Evaluate the inside of Listing 19.5's loop once, with nothing evicted: $\Delta_j=c_j+\text{AS}_j+\gamma x_j(\Sigma^{\text{res}}\mathbf{x})_j-\tfrac12\gamma\Sigma^{\text{res}}_{jj}x_j^2$, taking $\Sigma^{\text{res}}$ from Listing 19.4, $c_j$ from Listing 19.2 and $\text{AS}_j$ from Listing 19.7. Then sum the risk part over $j$:

$$
\sum_j\Big[\gamma x_j(\Sigma\mathbf{x})_j-\tfrac12\gamma\Sigma_{jj}x_j^2\Big]=\tfrac12\gamma\,\mathbf{x}^\top\Sigma\mathbf{x}+\tfrac12\gamma\sum_{i\ne j}x_i\Sigma_{ij}x_j .
$$

The first piece is the \$293k risk term already inside $\mathcal{C}$. The second is the excess. Each pair's covariance cost is "saved" twice, once when you remove $i$ and once when you remove $j$, but you can only stop paying it once. Removing L042 and L117 together saves \$883.6k, not the \$884.3k sum of their two savings, and the \$0.7k gap is $\gamma x_{42}\Sigma^{\text{res}}_{42,117}x_{117}$. On this one-sided basket every off-diagonal entry of $\Sigma^{\text{res}}$ is positive, so the excess is positive and the best eviction is guaranteed to help.

**The trap:** The usual slip is to read the removal savings as an allocation that must add up to $\mathcal{C}$, and then to "fix" the 7% gap by rescaling. They are one-at-a-time counterfactuals, not slices of a pie. If you need a bill that adds up, say for a best-execution file, split the risk term with $\tfrac12\gamma x_j(\Sigma\mathbf{x})_j$, which sums to $\tfrac12\gamma\mathbf{x}^\top\Sigma\mathbf{x}$ exactly. The second slip is ranking by $\Delta_j$ in dollars. That puts L042 first and hides the fact that L117 is 3.5 times worse per dollar. Leave out the AS term and L117 ranks eighth, at 59.5bp against a 54.9bp average, which is the left half of Figure 19.4.

**If you got this wrong, read:** §19.6.1 (the sum identity under "The greedy step is a descent step"), then §19.8.2 and Figure 19.4 for the ranking with and without the AS term.

**Z.19.2: The ETF goes to a 5% discount**

**Answer:** The regime score is $s=(4-1)/3+(0.97-0.80)/0.20=1.85$, so $m=5.44$, $\gamma$ runs at 3.775 times calm and the basis at 4.7 times. The full list goes from \$1.56mm (76bp) to \$9.72mm (476bp). Term by term:

- **Risk grows most:** from \$293k to \$4.79mm, up \$4.49mm or 16.3 times, and it becomes the largest term.
- **Handling** grows by exactly $m$: from \$829k to \$4.51mm, up \$3.68mm.
- **AS** stays at \$420k.
- **The hedge half-spread** falls from \$16k to \$4k.

Eviction does not reach 45bp. The loop stops at $k_{\max}=10$ lines, with 14.4% of MV handed back, at 287bp, and this time L042 goes first and L117 second. Lift $k_{\max}$ and the $\alpha$ budget binds at 11 lines and 284bp. No subset can reach 45bp at all, because at $m=5.44$ the cheapest line's handling cost alone is 50.9bp per dollar. Tell the client the desk will not take the list all-or-none at a price it would want hit, and offer to work it as agent. "Decline" is a valid quote: in an AON auction, not bidding is an answer, and it was the right one in March 2020.

**How:** The hedged variance rises 4.3 times, from a standard deviation of \$766k to \$1.59mm. Split the \$4.79mm risk charge three ways:

- **\$1.11mm** is calm variance charged at the new $\gamma$.
- **\$2.18mm** comes from the basis. With $\sigma_u$ up 4.7 times, the one-factor ratio $\beta_h\sigma_g^2/(\beta_h^2\sigma_g^2+\sigma_u^2)$ of §19.4.1 attenuates the hedge from \$237mm to \$66mm of notional, and that systematic risk stays on the desk.
- **\$1.50mm** is the spike, $(0.25s)^2(\mathbf{g}^\top\mathbf{x})^2$.

Risk is $\gamma$ times variance, so two of the three dials multiply each other, while handling sees only $m$. The bound on the target is one line: cost per dollar on any kept set is at least $\min_i c_i/\text{MV}_i=50.9$bp. The falling hedge cost is an artifact. The hedge shrank, and half-spreads are not regime-scaled, as §19.10 admits.

**The trap:** The trap is Kaz's card: move $\gamma$ alone and leave costs and basis at calm, and you get about 116bp, \$7.3mm short of the engine. Close behind is assuming the hedge protects you more in stress. It protects you less, because the basis eats the hedge ratio.

**If you got this wrong, read:** §19.7.1 for the multiplier and the spike, §19.4.1 for basis attenuation, Two Tapes in §19.7.2 for "one score, three dials", and §19.10 for what a wrapper does with `hit_target=False`.

**Z.19.3: ROBO and the stale universe**

**Answer:** ROBO prices the full list at \$1.64mm, or 80.1bp, against 76.3bp with the real ages. With eviction on, it hands back L117 and L042 and quotes the other 148 at 42.3bp with `hit_target=True`. The whole change is \$78k on the risk term (\$293k to \$371k), because handling and AS never read `age`. The kill switch the spec asked for is "refuse to auto-quote if more than 20% of gross MV has `age > 10`". Here that share is 100%; on the real basket it is 8.4% (L042 alone). The switch belongs in `price_pt`, or a wrapper in front of it, and not in `Basket.__post_init__`.

**How:** Write the stale share as $\sum_i\text{MV}_i\,\mathbb{1}\{a_i>10\}/\sum_i\text{MV}_i$. The test, in words, has three parts:

1. Build the all-stale basket with `replace`, call `price_pt`, and assert that it refuses (raises, or returns a refused status with no cash) before any covariance is built.
2. Assert that `b0` still prices.
3. Pin the threshold with a basket on either side of 20%.

The number barely moves for a reason. Equation (19.5) multiplies a typical line's idiosyncratic variance by about 11, but idiosyncratic variance diversifies across 150 lines, and L042 actually got fresher (40 days to 30). The only guard the listing codes gets *happier*: $\operatorname{cond}(\Sigma^{\text{res}})$ falls from 69 to 8, because uniform diagonal inflation improves conditioning. In reality, 150 thirty-day-old evaluated prices share one evaluator's matrix (composite reflexivity, §19.3), so their errors are common and do not diversify. The model cannot see that risk, so a rule has to catch it.

Why `price_pt` and not the constructor: `__post_init__` answers "is this inquiry well formed?", and a stale universe is well formed (the spec table says "flag $>10$", not "reject"). The switch answers "should the machine quote it unattended?", which is policy, with a threshold a human may override. Putting it in the constructor would also break code that legitimately builds stale baskets. `drop()` rebuilds through `__post_init__` inside the eviction loop, and evicting fresh lines could push the share past 20% mid-loop. The lost-quote replay engine needs stale baskets too, and so does this exercise's own test.

**The trap:** The trap is believing that "staleness is variance" protects the desk on its own, so that a stale basket simply comes out wide. It comes out 3.8bp wider, and on target after eviction. The second trap is putting the switch in the constructor, where it turns a pricing policy into a data error.

**If you got this wrong, read:** §19.10 (the precise spec, and ROBO's "price the basket fast"), §19.5.1 (staleness as variance, and the line-42 multiplier), §19.3 ("composite reflexivity"), and the paragraph after the §19.2 spec table on what the `Basket` gate does not check.

**Z.19.4: Kaz's springing lien**

**Answer:** Compare the two versions on the full list, which is what an "all or none, final" client makes you price. Kaz's version (L117's `sig_idio` times 10, its AS set to zero) quotes 64.0bp (\$1.308mm). The AS version quotes 76.3bp (\$1.558mm). Kaz is \$250k too generous: the bump adds \$89k of risk (\$293k to \$382k) and deletes \$339k of AS. The hedges are identical to the dollar, \$79.8mm of ETF and \$157.1mm of CDX in both. With eviction, Kaz's version still hands back L117 and then L042, so it lands on the same 36.6bp counter-proposal and the same \$67.9mm/\$133.7mm hedge, but only just. L117's saving is 330bp per dollar against L042's 307bp. At any multiplier up to 9×, L117 stays in, gets hedged, and is quoted inside a 37–41bp counter-proposal, depending on the multiplier.

**How:** Step 2 gives $\text{CE}=\kappa_1-\tfrac12\gamma\kappa_2+\tfrac16\gamma^2\kappa_3-\cdots$. Under (19.10) the informed move is a shift of the *mean*, so it enters $\kappa_1$ at $-\Pr(I)\,J\,\text{MV}=-0.752\times0.1375\times\$3.28\text{mm}=-\$339$k. The same jump's variance charge is only $\tfrac12\gamma\,p(1-p)(J\,\text{MV})^2\approx\$19$k, and its skew term $\tfrac16\gamma^2\kappa_3$ is about \$1.4k. Kaz's bump touches only $\kappa_2$, so it can match the jump only by accident. Matching \$339k needs a 5-day standard deviation of 20.6 points, about 19 times `sig_idio`, and even then the match holds only at $\gamma=10^{-6}$ and at \$4mm of size. The variance charge scales as $\gamma x^2$, while AS is linear in MV and does not depend on $\gamma$. A dealer with $\gamma\to0$ would charge nothing, which is the "picked off" edge of §19.2.

On the hedge, (19.4) gives $\mathbf{h}^\star=\Sigma_{ff}^{-1}\Sigma_{fx}\mathbf{x}$, and $\Sigma_{fx}=A\,\Omega_T B^\top$ contains loadings but not $D$. So an idiosyncratic bump cannot move $\mathbf{h}^\star$ on a given basket. It moves the hedge only in two ways:

- **Through eviction:** at 9× or less, L117 is kept and gets \$9.6mm of index hedge against its spread beta, while its jump stays on the desk.
- **Through the loadings:** if the bump scales L117's whole return series, which is what multiplying returns before `np.cov` does, its loadings scale too and $\mathbf{h}^\star$ grows from \$236.9mm to \$323.6mm.

**The trap:** The trap is thinking that more variance is more conservative. It is the wrong moment: the charge comes out too small, it is symmetric, and it disappears for a fearless dealer. It also moves the toxicity out of the AS column, where the hand history could score it, and into a covariance nobody audits by line.

**If you got this wrong, read:** §19.2.1 (Step 2 and the edges of the master equation), §19.8.1 for (19.10), §19.4.1 for what $\Sigma_{fx}$ contains, and the springing-lien exchange at the top of §19.5.

**Z.19.5: Flip the inequality**

**Answer:** Take the cold-open basket `b0` as the program, with $\Sigma=B\Omega_1B^\top+D$ from Listing 19.4 at $T=1$ day. Ignoring leakage, the risk term of (19.11) caps the premium at:

- **$\phi=0.9$:** $\Pi\le$ \$8.2k, or 0.40bp of the \$204mm market value.
- **$\phi=0.6$:** $\Pi\le$ \$43.4k, or 2.1bp, which is 5.3 times as much.

Add $\sum_i(1-\phi_i)c^{\text{retry}}_i$ on top: at the exercise's 5bp of extra cost per retried dollar, that is another 0.5bp and 2.0bp. The 0.9 number is 2023. Electronic fill rates had risen, a ceiling under 1bp is below any dealer's margin, and so the flow goes by RFQ (Man's ">90%" electronic). The 0.6 number is 2021. The ceiling is a few basis points, and the second tier was competing $\Pi$ toward zero, so the inequality held almost everywhere.

**How:** Write $q=1-\phi$. Because $\mathbb{1}_i^2=\mathbb{1}_i$, the diagonal of $\mathbb{E}[\mathbf{u}\mathbf{u}^\top]$ carries $q$, while the off-diagonal carries $q^2$:

$$
\tfrac12\gamma_B\,\mathbb{E}[\mathbf{u}^\top\Sigma\mathbf{u}]=q\cdot\underbrace{\tfrac12\gamma_B\textstyle\sum_i x_i^2\Sigma_{ii}}_{\$72.6\text{k}}+q^2\cdot\underbrace{\tfrac12\gamma_B\textstyle\sum_{i\ne j}x_ix_j\Sigma_{ij}}_{\$89.6\text{k}} .
$$

At $q=0.1$ that is $7.26+0.90=$ \$8.2k; at $q=0.4$ it is $29.0+14.3=$ \$43.4k. A Monte Carlo over 20,000 fill draws gives \$8.17k and \$43.4k. Lonely lines (the diagonal) are 89% of the $\phi=0.9$ number. Moving from $q=0.1$ to $q=0.4$ multiplies the diagonal part by 4 and the pair part by 16, which is why the total grows between 4 and 16 times. One caution on scale: 96% of the diagonal is L042, the big stale line. Switch off the staleness term in (19.5) and the ceilings fall to \$1.6k (0.08bp) and \$17.0k (0.83bp). Using $\Sigma^{\text{res}}$, as a client that hedges would, gives \$7.2k and \$30.1k.

**The trap:** The most common slip is to put $q^2$ on the diagonal too, as if the unfilled residual were a scaled-down copy of the whole program. That gives \$1.6k and \$26.0k, and understates the 2023 number five times because it forgets that a miss is usually one lonely line. The opposite slip, $q$ everywhere, gives \$16.2k and \$64.9k.

**If you got this wrong, read:** §19.9.1 (the derivation, then Wen's Month-End List for the same three terms with a leak), and §19.5.1 for where $\Sigma$ and its staleness term come from.

**Z.19.6: The mixed basket**

**Answer:** Flip every third line from L001 to a client buy: 50 lines, 28.8% of MV, and neither L042 nor L117 among them. Then $\mathbf{g}^\top\mathbf{x}$ falls from $-$\$1.93mm to $-$\$0.975mm per unit of $m$, so $(\mathbf{g}^\top\mathbf{x})^2$ falls to 25.6% of its one-sided value, from $3.72\times10^{12}$ to $0.95\times10^{12}$ \$². At $s=1$:

- The spike's standard deviation falls from \$482k to \$244k, and its risk charge from \$290k to \$74k.
- The full-list cost falls from 257bp to 196bp. In calm markets it falls from 76.3bp to 71.5bp.
- Handling (\$829k calm, \$2.82mm at $s=1$) and AS (\$420k) do not move by a dollar.

**How:** Every $g_i=-\theta\,\text{LCS}_i\widehat P_i$ is negative. Flipping lines that carry a share $w$ of $\sum_i\lvert g_ix_i\rvert$ turns $\mathbf{g}^\top\mathbf{x}$ into $(1-2w)\,\mathbf{g}^\top\mathbf{x}$, so the spike scales by $(1-2w)^2$. Here $w=0.247$, and $0.506^2=0.256$. A random 50 lines gives a median of 0.18, and less again when the big L042 happens to be flipped.

The bid tightens because price risk nets, even though costs do not. Handling depends on $\lvert x_i\rvert$, since you pay the spread whichever way the client trades. The cost variance in (19.8) is also written in $\lvert x_i\rvert$. Two things do net:

- **The factor lump:** $B^\top\mathbf{x}$ shrinks, so the hedge falls from \$237mm to \$101mm of notional, and the basis residual falls with it.
- **The liquidity shock:** when $m$ jumps, the bonds the dealer bought fall and so do the ones it sold short, so the short side pays.

Nothing on the hedge card kills the liquidity term (§19.4). The only hedge for it is the other side of the basket. The risk term falls from \$293k to \$206k in calm markets and from \$2.01mm to \$0.77mm at $s=1$.

**The trap:** One slip is to say "LCS is unchanged, so the price is unchanged". The opposite slip is to expect the handling cost, or the liquidation-cost variance in (19.8), to net between buys and sells. Neither nets, and the whole gain is in the risk term. Don't lean on Listing 19.8's side-symmetry test either: flipping *every* line leaves the cost identical, while flipping *some* of them is what shrinks it.

**If you got this wrong, read:** §19.7.1 for (19.8), (19.9) and the sentence "A mixed buy/sell basket nets it", §19.4 for why no instrument hedges the liquidity term, and Wen's Month-End List in §19.9.1 for a client building the two-way list deliberately.

### Z.20 Chapter 20: Credit ETF Creation/Redemption Arbitrage (HYG, JNK, LQD, BKLN)

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

### Z.21 Chapter 21: Leveraged Loans, CLOs & Loan-Market Microstructure

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

**Z.21.6: Read the holder base**

**Answer:** With $\theta = 0.65$, the non-CLO holders' 35% cannot carry a majority. You need at least 15.1 points of the tranche from CLOs, which is 23% of CLO-held par. The uptier that wins those votes is a CLO-friendly roll-up:

- a par-for-par exchange into a super-priority first-lien term loan;
- floating rate, paying cash;
- no maturity extension;
- rated B3/B− or better by both agencies *before* launch;
- new money funded by the 35% non-CLO holders, who get a backstop fee and any equity kicker (the CLOs would mark that equity at zero anyway);
- for the CLOs, at most a small allocation through their loss-mitigation (LML) baskets.

**LML binds first.** Rescue financing is capped at about 1–3% of a deal's principal, carries an extra OC haircut, and is often funded from interest proceeds. A deal with a 1.2-point cushion is one downgrade away from having that interest diverted. PIK (up to 5%) and long-dated (2.5–7.5%) bind only if you put PIK or an extension into the paper, so don't. Fixed-rate (10–15%, no haircut) binds last.

**How:** Start with the majority arithmetic: $0.501 - 0.35 = 0.151$ of the tranche must come from CLOs, and $0.151/0.65 = 23\%$ of their par. Then read $\psi$ and $\bar\kappa$, which say that these CLOs vote for a rating, not a recovery. Of the CLO holders, 60% (39% of the tranche) are already over their CCC limit. For them, a CCC outcome hits the cliff at about $1 - p^\ast \approx 42$ cents per dollar, at Kundu's 58-cent $p^\ast$, charged to other loans. Suppose the junior trigger is near 104%. Then a 1.2-point cushion is about $1.2/105.2 = 1.14\%$ of the numerator, which is room for roughly $1.14/0.42 = 2.7\%$ of the pool in fresh CCC before the junior test fails. A typical 0.5% position going CCC uses about a fifth of that room. Hence the design rules. Get the rating first. Don't extend, because an extension pushes the paper into the long-dated bucket and risks a distressed-exchange SD, then a CCC, then the cliff, which is the Loan A warning. Keep the CLOs out of the new money: at 2% on a \$400mm deal, LML is \$8mm for *every* workout in the book, and 60% of these holders already have a full CCC bucket that is drawing on it. One more reading of the numbers: the CLOs under their limit (26 points) plus the non-CLOs (35) make 61%. If you don't win the over-limit CLOs, a majority can be built without them, and they become the excluded minority with the highest Priming Risk Score.

**The trap:** The common mistake is to sweeten the economics for the CLOs instead of fixing the rating, with a better recovery, equity, a PIK toggle or a fat fixed coupon, each of which lands in a bucket or a haircut. The next is to assume the CLOs can fund their pro rata share of the new money: they can sign but not fund. The answer that picks PIK "because 5% is small" misses that LML is smaller, and that new money is the one thing every uptier needs.

**If you got this wrong, read:** §21.8 (the Weil memo, the state variable $(\theta_i, \bar\kappa_i, \psi_i)$, and Loans A and B), §21.4.1 for the cliff, and Chapter 13 for the Priming Risk Score.

### Z.22 Chapter 22: Market-Structure Regulation & the Forces Reshaping Liquidity

Six exercises: two on rent and clocks, two on the tape and the netting set, and two on dates, which is where this chapter's money is. Write your card before you read ours.

**Z.22.1: The ante**

**Answer:** $\tau^\ast = 0.25/60$ years $= 0.00417$ years $\approx 1.52$ calendar days at $\kappa_{\text{LR}} = 5\%$, and $0.25/45$ years $= 0.00556$ years $\approx 2.03$ days at $3.75\%$. At a two-day hold the dealer paid 0.33bp of rent against a 0.25bp half-spread under the old floor, losing about 0.08bp per round trip. That is an agent with extra steps, and an unpaid warehouse. Under the new floor the rent is 0.247bp against 0.25bp, so it breaks even: a principal that earns nothing on the hold. In both regimes, principal market making pays only if the dealer turns its Treasuries in under about two calendar days.

**How:** The bid-ask is 0.5bp of price, so the numerator of (22.4) is the *half* spread, 0.25bp. Rent per year is

$$
c_{\text{reg}} = h\,\kappa_{\text{LR}} = 0.12 \times 0.05 = 0.006 = 60\text{bp/yr}, \qquad 0.12 \times 0.0375 = 45\text{bp/yr}.
$$

Divide: $\tau^\ast = 0.25/60$ and $0.25/45$ years, then multiply by 365 (the chapter's ACT/365 convention). For the two-day check, compare the half-spread with $60 \times 2/365 = 0.329$bp and $45 \times 2/365 = 0.247$bp. The risk weight never enters, because a 5-year on-the-run Treasury sits far below the switching point (22.14), so the leverage floor is the whole rent.

**The trap:** The usual slip is to put the full 0.5bp on top of (22.4) and get 3.0 and 4.1 days. Those match the §22.1 table, but that table priced a 2-year that was 1bp wide, with a half-spread of 0.5bp. With them, a two-day hold looks comfortably principal, and the conclusion flips. The runner-up is a calendar slip: $\tau^\ast$ is in calendar days, so "two days" held over a weekend is four, and that dealer is underwater under either floor.

**If you got this wrong, read:** §22.1.1 (eq. 22.4 and the numerics table), then the ante in §22.5.1.

**Z.22.2: Pooling at the cap**

**Answer:** The cap is neutral at $Q = mC = 2.5 \times \$5\text{mm} = \$12.5$mm for IG (the HY twin is $4 \times \$1\text{mm} = \$4$mm). It moves the competitive half-spread by exactly $\lambda(mC - Q)(1 - \Delta/T_u)^+$, which is positive, a widening, for every $C < Q < mC$. With the worked-example parameters ($\lambda = 0.5$, $\Delta = 15$, $T_u = 120$, $\sigma = 2.5$, $\gamma = 0.001$):

| $Q$ (\$mm) | uncapped (bp) | capped (bp) | cap's effect |
| :-- | :-- | :-- | :-- |
| 6 | 3.38 | 6.22 | +2.84 |
| 10 | 5.63 | 6.72 | +1.09 |
| 12.5 | 7.03 | 7.03 | 0 |
| 15 | 8.44 | 7.34 | −1.09 |
| 25 | 14.06 | 8.59 | −5.47 |

The worst place to be is just above the cap: a ticket one dollar over \$5mm pays 3.28bp more than one at \$5mm.

**How:** Above the cap the market prices the conditional mean, so the inferred size in the leak term of (22.6) becomes $mC$ while the inventory term keeps the true $Q$:

$$
\frac{s_B^{\text{cap}}}{2} - \frac{s_B^\ast}{2} = \lambda\,(mC - Q)\Big(1 - \frac{\Delta}{T_u}\Big)^+ .
$$

The inventory term $\gamma\sigma^2 Q T_u/6$ cancels, so the neutral point is $Q = mC$ whatever $\lambda$, $\gamma$ or $\sigma$ are, as long as $\Delta < T_u$. (If the unwind finishes before the print, the cap is irrelevant at every size.) With $m = \alpha/(\alpha-1) = 2.5$ from Ben Dor's imputed \$12.5mm, the sign is the sign of $mC - Q$. Here is how Ines would put the politics. A desk whose blocks are \$5–12.5mm is taxed by the pool, so it wants a higher cap or finer size buckets: the 2019 pilot's \$10mm cap would have let its \$6–10mm tickets print at their true size. A desk whose blocks are above \$12.5mm is subsidized, so it defends the \$5mm cap. It accepts a higher one only with compensation, which is what the 2019 pilot's 48-hour delay was. With $\alpha$ fixed, a \$10mm cap puts $mC$ at \$25mm, which turns a \$15mm block from a 1.09bp subsidy into a 4.38bp tax. Same tape, opposite comment letters.

**The trap:** The common wrong answer is "the cap always helps the dealer, because hiding size is good", or a neutral point at $Q = C$. The cap does not hide size. It replaces it with the pool's average, and the average is \$12.5mm, which is bigger than most capped trades. A \$6mm ticket is being priced as if it were twice its size.

**If you got this wrong, read:** §22.2.2 (eq. 22.7 and the pooling paragraph), with (22.6) from §22.2.1; Beat 3 of §22.2.3 for the 2019 pilot.

**Z.22.3: Negative specials**

**Answer:** The floor on the special repo rate is $r^{\text{sp}} = \min(0,\ r^{\text{ref}} - 3\%)$. That is $-2.75\%$ at $r^{\text{ref}} = 0.25\%$ and $0\%$ at $r^{\text{ref}} = 4\%$. At near-zero rates the fails charge lets specials go about 2.75 points negative. At 4% the charge is asleep, and the old zero bound is back.

**How:** Measure both choices against delivering on time and investing the proceeds at $r^{\text{ref}}$. Failing costs (22.9), $\max(r^{\text{ref}}, 3\%)$: you lose the interest and pay the charge. Borrowing the bond means lending your sale proceeds in repo at $r^{\text{sp}}$ to get it, so you give up $r^{\text{ref}} - r^{\text{sp}}$. Set the two equal:

$$
r^{\text{ref}} - r^{\text{sp}} = \max(r^{\text{ref}}, 3\%) \;\Longrightarrow\; r^{\text{sp}} = r^{\text{ref}} - \max(r^{\text{ref}}, 3\%) = \min(0,\ r^{\text{ref}} - 3\%).
$$

Below that rate the short fails instead, so no bond lender can push repo lower. Now Veronesi's May 2009. With the policy rate near zero and failing free (cost $\approx r^{\text{ref}} \approx 0$), the floor sat at zero. Specials piled up there, and fails were the cheap alternative. The 3% penalty from 1 May 2009 dropped the floor to about $-2.75\%$ ($-3\%$ if you take the reference as exactly zero). That made room for the negative special repo rates Veronesi records that same day. The floor is a bound, not a forecast: the 2009 specials did not have to go anywhere near $-2.75\%$.

**The trap:** One slip is to drop the $\min$ and report $+1\%$ at a 4% reference rate, as if a special could not trade below 1%. Above 3% the charge is zero, failing costs only the lost interest, and specials can go all the way to zero. The other is $-3\%$ at 0.25%, which forgets that the failing seller also loses the 0.25% of interest.

**If you got this wrong, read:** §22.3.2 (eq. 22.9 and the Veronesi annotation).

**Z.22.4: When does netting give up?**

**Answer:** The floor is $\phi_\infty = 0.5/0.8956 = 0.558$. By simulation (20,000 paths) and by closed form, $\phi(5) \approx 0.651$, $\phi(10) \approx 0.580$, $\phi(25) \approx 0.559$ and $\phi(100) \approx 0.558$. It is within 5% of the floor (at or below 0.586) from $N = 10$. $N = 9$ misses by a hair, at 5.03% above, which 20,000 paths cannot reliably tell apart from $N = 10$. Past about ten members, more clearing members buy nothing in a one-way market. Clearing removes at most 44% of gross exposure, where the two-way formula promises 67% at $N = 10$ and 90% at $N = 100$.

**How:** Draw $x_{ij} = 0.5 + Z_{ij}$ ($\sigma_x = 1$) in $N - 1$ columns, and divide the mean absolute row sum by the mean row sum of absolute values. This is [Listing 22.4](#code-22-4)'s `netting_factor_mc` with `common_component=0.5`. Check it against the exact factor. With $n = N - 1$ and $f(a) = \mathbb{E}|a + Z| = \sqrt{2/\pi}\,e^{-a^2/2} + a\,\operatorname{erf}(a/\sqrt2)$,

$$
\phi(N) = \frac{f(\sqrt{n}\,m)}{\sqrt{n}\,f(m)}, \qquad f(0.5) = 0.8956 .
$$

Convergence is fast because the only thing separating $\phi(N)$ from the floor is the chance that the netted position flips sign, $\Phi(-\sqrt{n}\,m/\sigma_x)$. That chance is 6.7% at $N = 10$ and 0.7% at $N = 25$. Once the sum has a sign, there is nothing left to cancel.

**The trap:** The usual wrong answer is the two-way formula $1/\sqrt{N-1}$: 0.50, 0.33, 0.20 and 0.10. It says a 100-member clearing house removes 90% of exposure, when a market leaning half a standard deviation one way keeps 56%. Two smaller slips: reading "within 5%" as 0.05 absolute, which gives $N = 7$, and using $N$ columns instead of $N - 1$ counterparties, which matters only at small $N$.

**If you got this wrong, read:** §22.4.1, especially (22.11) and "The Full Derivation: the netting factor with a common direction."

**Z.22.5: Kaz's event date**

**Answer:** 2025-12-31 is the stale date. The December 2023 adopting release set it, and on 2025-02-25 the SEC moved cash compliance to 2026-12-31 and repo to 2027-06-30. Nothing became mandatory on 2025-12-31, so Kaz would be measuring a year-end and crediting it to a rule. Turned around, that same date is the best placebo the study has. The design:

- **Event** $t_0$ = 2026-12-31, a Thursday that is also year-end, a G-SIB measurement snapshot, and the eve of a market holiday.
- **Treated** are Treasury flows the mandate newly pulls into clearing: cash trades on interdealer-broker platforms, and trades between clearing members and non-member broker-dealers or government securities dealers that used to settle bilaterally. For the credit desk, that means its own Treasury hedges with in-scope counterparties.
- **Controls** are flows that do not change on the date: trades already cleared member-to-member at FICC, and exempt ones (central banks, sovereigns, international financial institutions, natural persons, inter-affiliate).
- **Placebos** are 2025-12-31 (the same calendar position and the same photograph, with no rule) and 2024-12-31, plus one or two mid-quarter fake dates whose post-windows end well before Q4 2026.
- **Distrust trigger:** a significant "effect" at 2025-12-31 of the same sign and similar size as the one at 2026-12-31. That would mean the estimate is the year-end, not the mandate.

**How:** First take the date from the latest release, not the first one. Keep adoption (2023-12-13), the extension (2025-02-25), margin separation (2025-09-30), the CME and ICE approvals, and each compliance date as separate columns, the way Ines's card did for the one-minute rule. Then run (22.17) with bond- or segment-level changes, so the date effect $\bar\mu^{\text{post}} - \bar\mu^{\text{pre}}$, which here is mostly year-end balance-sheet dressing, cancels against controls that dress for the same photograph. Keep the repo date a separate event, and keep every placebo window clear of the real dates. Two more results should shake you. One is a pre-trend: treated flows diverging through 2026 as dealers migrate early (Uyeda put FICC cleared volume about 165% above pre-proposal levels in September 2026). That means the pre-window is already treated and a sharp-window $\hat\delta$ measures the stragglers. The other is controls that move with the treated, because the same dealers clear both segments and sponsored repo already nets at the sponsor. That is Kaz's affiliate-indicator problem again. A last detail: the listing's business-day count has no holiday calendar, so a window across 2027-01-01 holds one fewer trading day than it thinks.

**The trap:** The common answer is "wrong date, use 2026-12-31" and stop there. The right date is still a year-end, so a before-and-after, or a weak control group, will hand the quarter-end photograph to the rule. The stale date is valuable precisely because it shares that calendar position.

**If you got this wrong, read:** §22.8.1 (placebo dates and the affiliate-indicator run), §22.4 (the rule and its Trend Watch: "give each one a placebo twin"), and the fourth envelope of §22.2.3.

**Z.22.6: ROBO maximizes transparency**

**Answer:** With $\Delta = 0$ and $C = \infty$, every principal block pays the full leak on its full true size: $s_B^\ast/2 = \lambda Q + \gamma\sigma^2 Q T_u/6$. On the worked example, a \$15mm block unwound over two hours goes from 7.34bp today (15 minutes, priced as the pooled \$12.5mm) to 9.38bp, up 28%. A \$25mm block goes from 8.59bp to 15.63bp, up 82%. A \$15mm block unwound in fifteen minutes goes from 0.23bp to 7.73bp. A \$1mm ticket barely moves, from 0.56bp to 0.63bp.

- **What survives:** small tickets; agency crosses; riskless-principal trades whose other side is done before the print; and trades the market reads as uninformative (small $\lambda$).
- **What dies:** principal risk transfer of blocks worked over an hour or two, which are exactly the trades the delay and the cap were protecting.
- **Where the rest goes:** portfolio trades (Chapter 19), where a basket price, flagged by the PT modifier, dilutes any one bond's signal; ETF creation and redemption (Chapter 20), where size moves in kind in the primary market and the price risk trades as a fund share; and agency and all-to-all protocols that match without warehousing.
- **The result that should worry ROBO's sponsor:** Asquith, Covert and Pathak found that transparency cut costs (high-yield costs down 22.9%, about \$600mm a year in savings), but that "trading activity does not increase and, by one measure, decreases." By that measure, high-yield activity fell 71.1%. Maximum transparency lowers the price of liquidity and shrinks the quantity on offer.

**How:** Put $\Delta = 0$ into (22.6). The positive part $(1 - 0/T_u)^+ = 1$ for every $T_u > 0$, so the dealer is fully exposed when the print appears. Only a trade with no inventory at execution ($T_u = 0$) escapes. With $C = \infty$, the inferred size is the true $Q$, so the pooling subsidy of (22.7) disappears for every block above \$12.5mm. Both terms are now linear in $Q$, so total cost grows like $Q^2$. That pushes size into protocols where nobody warehouses it or where the print says less. One honest caveat: (22.6) holds $\lambda$ fixed. Asquith, Covert and Pathak's cost result is the evidence that transparency lowers the average price too. Their volume result is the evidence that the block dealer's side of (22.6) is real.

**The trap:** The usual answer is "more information means less asymmetry, so spreads fall everywhere." That is true of the average ticket, and the average ticket is a \$1mm trade the auto-quoter crosses riskless. In (22.6) the delay and the cap are subsidies to the block dealer. Removing them raises the price of the trades a principal dealer exists to do, and the volume moves elsewhere or does not happen.

**If you got this wrong, read:** §22.2.1 (the delay as an option), §22.2.2 (pooling), and the Asquith, Covert and Pathak paragraph that opens §22.2; then Chapters 19 and 20 for the protocols.

## Part VI: Capital Structure Arbitrage & Volatility Surfaces

### Z.23 Chapter 23: Cross-Asset Convexity & the Volatility Surface

*Worked solutions. Numbers were recomputed from the chapter's equations and Listings 23.1–23.3. Inputs the exercise leaves open are stated as assumptions.*

**Z.23.1: ROBO targets volatility**

**Answer:** ROBO's target weight is $10\%/\sigma_E$. That is 21.7% of capital at $V = 150$, 13.7% at 100 and 8.5% at 75, a 61% cut in exposure. But ROBO never sells a share. The stock falls 86%, from 82.1 to 11.2, which shrinks the position faster than the target shrinks, so ROBO has to *buy*. Per \$100 of fixed risk capital the share count goes from 0.267 to 0.420 to 0.763. If it rebalances only at the three rows, with its losses flowing through NAV, the count goes 0.267, 0.364, 0.603. The sentence for the committee: *"The overlay sizes by equity vol, and equity vol is asset vol times leverage, so it always holds the same slice of the firm's asset risk (40% of NAV here); it has traded a call struck at the debt for a fixed slice of the assets, which makes it short exactly the convexity that sits at the fulcrum strike."*

**How:** The dollar vol of $n$ shares is $n\,\sigma_E E$, and (23.1) says $\sigma_E E = \sigma_V V N(d_1)$. To keep dollar vol at 10% of NAV,

$$
n = \frac{0.10\,\text{NAV}}{\sigma_V\, V\, N(d_1)} .
$$

Down the table the denominator falls from 37.5 to 23.8 to 13.1, so $n$ rises. The weight $nE/\text{NAV} = 0.10/\sigma_E$ falls only because $E$ falls faster than $n$ rises. With continuous rebalancing, $d\text{NAV} = n\,dE = n N(d_1)\,dV$, which gives $d\text{NAV}/\text{NAV} = (0.10/\sigma_V)\,dV/V = 0.4\,dV/V$, so $\text{NAV} \propto V^{0.4}$. From 150 to 75, NAV ends at $0.5^{0.4} = 75.8\%$ of where it started (a step-by-step simulation gives the same number). A power of 0.4 is concave in $V$, while the equity ROBO holds is convex in $V$, because it is a call struck at $F = 70$. Holding a constant mix is short gamma relative to holding the claim itself, and here that gamma sits at the debt strike.

**The trap:** Answering "ROBO sells 61%." That is the cut in the weight, mistaken for a trade. An investor who bought and held would see the weight fall further, to 3.7% of a NAV of 81.1, so measured against doing nothing ROBO is a buyer. It is a seller only against a constant-weight book, which would still hold 21.7%. That comparison is the one the committee sentence should make.

**If you got this wrong, read:** §23.1, "The Merton identity" (23.1) and "Sliding the assets down the table."

**Z.23.2: Chase the ghost**

**Answer:** Inputs: $\sigma_E = 40\%$, $F^{\text{ps}} = 30$, $\bar\ell = 0.5$, $\nu = 0.3$, $R = 40\%$, $r = 3\%$.

| | $S_0 = 5$, true model | $S_0 = 5$, (23.3) | $S_0 = 30$, true model | $S_0 = 30$, (23.3) |
| :-- | --: | --: | --: | --: |
| $1 - \mathcal{S}(0)$ | 13.4% | 25.0% | 0.007% | 0.013% |
| 1-year spread | 1,530bp | 2,306bp | 32.6bp | 32.7bp |
| 5-year spread | 555bp | 691bp | 161.0bp | 161.0bp |

The time shift moves the 1-year spread by more than 50bp once the stock falls below about **\$11.40**, which is $S_0/F^{\text{ps}} \approx 0.38$. For the 5-year spread the threshold is about \$7.05. At \$30 the approximation costs nothing. At \$5 it doubles the ghost and adds 776bp to the 1-year spread.

**How:** In the true model the barrier $L = \bar\ell F^{\text{ps}} e^{\nu Z - \nu^2/2}$ is drawn once, so the time-zero mass is exact:

$$
1 - \mathcal{S}(0) = N\!\Big(-\frac{\ln\big(V_0/\bar\ell F^{\text{ps}}\big) + \nu^2/2}{\nu}\Big),
$$

which is $N(-1.109) = 13.4\%$ at $V_0 = 20$. Conditional on $Z$, put $y = \ln(L/V_0) < 0$ into the known-barrier formula of Step 3: $\mathcal{S}(t \mid Z) = N\big(\tfrac{-\sigma_V^2 t/2 - y}{\sigma_V\sqrt t}\big) - e^{-y} N\big(\tfrac{-\sigma_V^2 t/2 + y}{\sigma_V\sqrt t}\big)$. Then integrate over $Z$. A Monte Carlo run with 200,000 paths, daily steps and the Brownian-bridge correction agrees: a ghost of 13.2% and $\mathcal{S}(1) = 0.795$, against 0.793 from quadrature. Put both survival curves through the same monthly legs of (23.5) and root-find for the stock price at which the gap is 50bp. The factor of about 2 in the ghost (25.0% against 13.4%, and $1.3\times10^{-4}$ against $0.7\times10^{-4}$) is the drunk's mirror at work. The time-shifted walk counts every path that touched the barrier during the hidden interval $[-\xi, 0]$, including the ones that walked back, while the true model counts only the ones that start below it.

**The trap:** Running Listing 23.1's `cg_survival_mc` and concluding that the approximation is exact. That routine simulates the *time-shifted* process, for which (23.3) is exact, so it agrees by construction. The other common slip is to redraw the barrier at every time step, which builds a different model, not CreditGrades.

**If you got this wrong, read:** §23.2, "The Full Derivation of (23.3)–(23.5)" (Step 2), the drunk-and-gutter Math, Gently box, and the Ways This Blows Up box on the time-zero ghost.

**Z.23.3: Trade the basis**

**Answer:** Assume Listing 23.2's chain settings ($S_0 = \$100$, $\sigma = 30\%$, $T = 1$, $r = 3\%$, $q = 0$, strikes \$10 to \$150) and the corridor $A = 0$, $B = \$20$. Then:

- From the puts: $U^{\text{opt}} = P(20)/20 = 0.05651$, on the `at_expiry` convention.
- From CDS at 250bp and $R = 40\%$: $\lambda = 4.167\%$, and the at-expiry claim is $U^{\text{CDS}} = 0.03960$.
- The basis is $\text{basis}_U = +0.01691$ per \$1 of claim. In spread units the puts imply $\lambda = 6.00\%$, or 360bp, so the basis is **+110bp**.

The put spread is *rich*, so you sell it and buy protection. With $A = 0$ that means selling 300,000 \$20 puts (3,000 contracts) against \$10mm of bought CDS. You collect \$339k of premium for a claim that CDS values at \$238k, an edge of \$101k in present value. If the stock bleeds into the corridor instead of jumping through it, the trade stops being default-neutral and becomes a naked short put. At $S_T = \$10$ with no credit event, the puts cost \$3.0mm and the CDS pays nothing.

**How:** Size the trade so the default payoffs match:

$$
n(B - A) = (1 - R)N = 0.6 \times \$10\text{mm} \;\Rightarrow\; n = 300{,}000 .
$$

At 20% of spot the diffusion part of (23.8) is about $10^{-9}$, so $P(20)/20$ is the floor $e^{-rT}(1 - e^{-\lambda T})$. The CDS claim on the same European timing is $e^{-rT}(1 - e^{-s T/(1-R)})$. To convert back to spread, use $\lambda = -\ln(1 - U e^{rT})/T$ and $s = \lambda(1 - R)$. The match holds in amount, not in timing: the CDS pays at $\tau$ and the puts pay at $T$. In a slow bleed the put pays $B - S_T$ on paths where the firm survives, so the corridor proof breaks at its first line ("before default, $S_t > B$"). The protection you bought gains mark-to-market as the spread widens, but a 1-year contract with no credit event expires worthless. GM drifted from 2005 to 2009 through every corridor you could have drawn. The extra 110bp may be exactly the market's price for that path.

**The trap:** Sizing $n = N/B = 500{,}000$ and forgetting $1 - R$. That over-hedges the default by 67%, leaving you net short \$4mm of default payoff. A close second is mixing conventions: the at-default CDS claim, 0.04021, gives a basis of about 104bp, and the 6bp difference is pure timing. Also check the sign before you act. §23.3's "buy the put spread, sell CDS" is the trade for a *cheap* put spread.

**If you got this wrong, read:** §23.3, "The CDS side" and "The signal," (23.6)–(23.7); §23.4, Ways This Blows Up ("American exercise").

**Z.23.4: Kaz and the prospectus**

**Answer:** It is not an arbitrage. Seniority binds in a liquidation, and a write-down clause acts before there is one.

*The override logic.* Any instrument whose terms contain a contractual write-down or conversion trigger gets `contractual_waterfall_override = True`. The flag has four consequences:

1. The instrument leaves CreditGrades and every other priority-ordered model.
2. The risk system refuses to net it against the same issuer's equity. There is no "seniority hedge."
3. Its jump-to-default is booked as the full face at zero recovery, in a trigger state that can come before, and apart from, an equity default.
4. It needs a trigger-probability input (distance to the CET1 trigger, the regulator, the odds of state support) in place of a barrier.

*The three prospectus fields.*

1. **Trigger definition:** the CET1 trigger level and the viability-event clause, including who makes the determination and whether extraordinary public support counts as a trigger.
2. **Loss-absorption mechanism:** write-down or conversion; full or partial; permanent or temporary; and the conversion price, if it converts.
3. **Conditionality and ranking:** whether the write-down requires equity to absorb losses first. Credit Suisse's did not.

*CreditGrades on 17 March 2023.* All inputs are illustrative: $S_0 = \text{CHF } 2.00$, $\sigma_E = 60\%$, debt per share CHF 35 excluding deposits, $\bar\ell = 0.5$, $\nu = 0.3$, $r = 1.5\%$, and a 9.75% AT1 priced as a 5-year bond to its call. The model says:

- a time-zero ghost of 56% and a 5-year default probability of 60%;
- CDS-equivalent spreads of about 7,900bp at 1 year and 1,790bp at 5 years;
- an AT1 fair value of **80** at $R = 40\%$, 68 at $R = 20\%$, and still **56 at $R = 0$** (about 50 even at $\sigma_E = 100\%$).

So CreditGrades tells Kaz that the AT1 at 40 is cheap, whatever recovery is typed in. It gives Sunday's outcome (AT1 at zero, equity at CHF 0.76) a probability of exactly zero. On the illustrative entry, Kaz's pair loses all 40 points on the long and makes CHF 1.24 a share on the short.

**How:** In (23.3)–(23.5), default is the asset value touching $\ell F^{\text{ps}}$. At that moment the equity is zero by construction and every debt claim receives its $R \ge 0$. To value the AT1, discount its coupons and principal at the CG survival probabilities, $\sum c\,e^{-rt}\mathcal{S}(t) + e^{-rT}\mathcal{S}(T)$, and add $R\big[1 - \mathcal{S}(0) + \int e^{-ru}(-d\mathcal{S})\big]$. The model has no state in which a junior claim keeps value while a senior one is zeroed. The viability clause creates exactly that state, and a regulator, not a diffusion, sets its strike.

**The trap:** Setting $R_{\text{AT1}} = 0$ and calling the model fixed. Even at zero recovery CG says 56, because its default event wipes out the equity first. What is wrong is the event, not the recovery number. Lowering $\nu$ for a financial, as the spec's override allows, *raises* the model value to 60 at $R = 0$, so the AT1 at 40 looks even cheaper.

**If you got this wrong, read:** §23.8, Case Study C and its Desk Myth box; §23.2, Ways This Blows Up ("Financials," "Two recoveries"); the bank-override spec at the end of §23.8.

**Z.23.5: Both legs, again**

**Answer:** On full revaluation the book loses about **\$0.59mm**; the Greeks say \$0.58mm. Day 1 (stock +18%) costs \$0.18mm and day 2 (spread +30%) costs \$0.41mm.

| Leg | Day 1 | Day 2 | Total |
| :-- | --: | --: | --: |
| Convertible: calls net of their own delta (gamma) | +\$50k | | |
| Convertible: stock hedge of the bond's credit delta | −\$113k | | |
| Convertible: bond floor | | −\$201k | |
| **Convertible leg** | | | **−\$264k** |
| CDS: short stock hedge | −\$117k | | |
| CDS: sold protection | | −\$206k | |
| **CDS leg** | | | **−\$323k** |

The only line with a plus sign is the convertible's long gamma. For Wolfspeed, the first flag you can date from public data is **the convertible floor**, on by 28 March 2025 at the latest, on a secondary report: the 2026s near 60 against a secured-curve floor of about 87. $z$ at \$2.59 comes out at about $-0.39$ to $-0.42$, which is inside Yu's lowest threshold and points the wrong way (buy the stock). These are single dated points under stated assumptions, not series: no free bond-price, CDS or option-surface history for Wolfspeed was found, so the put floor cannot be rebuilt.

**How:** The setup is Listing 23.3's \$30 name: $\sigma_E = 40\%$, $F^{\text{ps}} = \$30$, $R = 40\%$, $r = 3\%$, $T = 5$. That gives a CG spread of 161bp and $ds/dS = -4.96$bp per \$. The convertible is assumed: \$10mm face, a 2% coupon, and a bond floor of 88.24 at 161bp ($D^{\text{spr}} = 4.77$). The calls are on 266,667 shares struck at \$37.50, a 25% conversion premium, worth \$9.65 each with a delta of 0.643. The convertible's hedge is short $171{,}362 + 20{,}858$ shares. The second number is the bond's credit delta, $-D^{\text{spr}} B\, ds/dS$. `cg_greeks` puts the CDS hedge at short 21,589 shares, with an RPV01 of 4.35.

On day 1 the market spread does not move, although the model's falls to 137bp. Every share shorted against a *credit* delta (42,447 shares) loses \$5.40 and nothing comes back. On day 2, $\Delta s = +48$bp: the bond loses $D^{\text{spr}} B\,\Delta s$ and the protection loses $\text{RPV01}\cdot N\cdot\Delta s$.

In §23.6's decomposition, the CDS leg is convergence of −\$103k on day 1 (the gap widens 23.7bp) plus −\$206k on day 2 (48bp), and gamma of about −\$13k. The two legs are the same trade twice, long credit and short stock, so the hedges compound instead of offsetting.

*Wolfspeed:*

- Debt per share is $6{,}658.2/156.48 = \$42.5$ (10-K stack, old shares).
- Convert floor (assumed: a 1 May 2026 maturity, and the secured notes' 10-K mark of 85 on 29 June, a yield of 16.4%, standing in for the March curve): the 2026s' cash flows give about 87, against a market near 60 around 28 March (a secondary report).
- CG with $\sigma_E$ assumed at 80–120% and $R$ assumed at 27% (inside the plan's 25–30% range for the converts): at the January ATM price of \$7.20 it already shows a 25% ghost and 3,700–5,100bp at 1 year. At \$2.59 the ghost is 55% and the 1-year spread 9,400–10,000bp (8,700–9,200bp at the converts' own 1.09-year tenor).
- The converts at 60 imply about 5,300bp (flat hazard to maturity, $R = 27\%$), so $z \approx -0.39$ to $-0.42$ at the same tenor.
- The put floor needs OPRA history. Borrow would distort it as well: short interest was quoted at 64% in May 2025.

**The trap:** Letting the market spread follow the model on day 1. Do that and the CDS leg loses only its \$13k of stock-space gamma and the convertible looks hedged. May 2005's whole lesson is that the market spread did not follow the model. On Wolfspeed, the trap is trusting $z$ at $S/F^{\text{ps}} = 0.06$, far inside the zone where Z.23.2 shows the time-zero ghost dominates the spread.

**If you got this wrong, read:** §23.5 (the Natenberg map, (23.10), and Theo's whiteboard on JTD); §23.6, the P&L decomposition and "The Tape, and the Cards Graded"; §23.7, the Wolfspeed case note.

**Z.23.6: Three speeds**

**Answer:** About **68bp of software high-yield spread per 10% of software equity drawdown**: a 136bp gap over a 20% drawdown. Treat that as an upper bound; with technology HY at 340bp as the control, it is about 30bp. Over the full 20% drawdown that is +136bp, and at a spread duration of about 3 it forecasts a markdown of roughly **4 points** for a software loan book at 97.8, to about **93.8**, arriving a quarter or so behind high yield. If private spreads move half as much as public ones, the forecast is about 2 points, to 95.8. The assumption that would make the forecast wrong: that the equity drawdown is a *credit* event. If the low-strike put floor did not move, the fall is multiple compression on equity that sits well below the first lien, and senior marks have no reason to follow.

**How:** iCapital gives levels, not changes. Software HY was at 400bp against 264bp for broad HY, while software equities were down 20% year to date. Attribute the 136bp gap to the drawdown and you get 6.8bp per 1%. That only works if software HY traded flat to the index on 1 January, which is why the estimate is a ceiling. Cross-check with §23.9: Dynkin's +1% of equity momentum buys 5–8bp of next-month bond excess return. At an HY spread duration of about 3.5, that is only 14–23bp of spread per 10%, so part of the 136bp was there before January or built up over more than a month. For the loan, use (23.9) at the assumed spread duration of 3:

$$
\Delta P \approx -D^{\text{spr}}\,\Delta s\,P = -3 \times 0.0136 \times 97.8 \approx -4.0 .
$$

The lag is the three speeds of the Trend Watch: equity in days, public HY in weeks, private marks at the next quarter-end valuation. Before you publish the forecast, test whether the drawdown was about the tail: look at $\Delta\widehat\lambda^{\text{put}}$, the change in the put-floor hazard, in the regression.

**The trap:** Dividing the whole 400bp by the 20% drawdown, which gives 200bp per 10% and treats a level as a move. The other common one is marking the loan down by the spread move itself, 1.36 points, and forgetting spread duration.

**If you got this wrong, read:** §23.9 (the lead–lag regression, the Man annotation on valuation versus credit events, and the "three speeds" Trend Watch); §23.5, (23.9) for spread duration; Chapter 17 for how private marks are made.

### Z.24 Chapter 24: Bond-to-CDS Basis & Deliverable Obligation Mechanics

Six exercises: one on the hedge ratio, one on a phantom signal, one on the band, one on an auction's rounding, and two on paper, because the legal layer is where this chapter's money is. Every number below was recomputed from the chapter's inputs and Listings 24.1 to 24.7 (Appendix F). Write your card before you read ours.

**Z.24.1: The over-hedge**

**Answer:** The JTD-neutral notional is $N^{\text{JTD}} = (0.72 - 0.35)/(1 - 0.35) = 0.569$, so \$5.69mm of protection per \$10mm face. If the auction (and with it the bond, which in bankruptcy recovers the same as everything else pari passu) comes in at 25 rather than 35, the package loses about \$431k. The bond loses 47 points (\$4.70mm), and the swap pays 75 points on \$5.69mm (\$4.27mm). The package is long recovery by $1 - N^{\text{JTD}} = (1-P)/(1-R) = 0.43$ of face, or about \$43k per point of recovery on \$10mm.

**How:** At default the bond goes from $P$ to $R$ and $N$ of protection pays $N(1-R)$, so the package's default P&L per unit face is

$$
\Pi(R) = (R - P) + N(1-R).
$$

Setting $\Pi(0.35) = 0$ gives $N^{\text{JTD}} = (P-R)/(1-R) = 0.37/0.65$. Now differentiate with respect to the recovery that actually happens:

$$
\frac{\partial \Pi}{\partial R} = 1 - N, \qquad 1 - N^{\text{JTD}} = \frac{1-P}{1-R} = \frac{0.28}{0.65} = 0.431 .
$$

Ten points of recovery miss times 0.431 times \$10mm is \$431k, which is the P&L above. The bond's sensitivity to recovery is one per unit face, but the swap's is only $N$. The two cancel only when $N = 1$, and $N^{\text{JTD}} = 1$ only when $P = 1$. Par-for-par (\$10mm) is the mirror image: it has no recovery delta at all, but it is long \$2.8mm of jump-to-default at any recovery. With one swap you can neutralize the jump or the recovery, not both, unless the bond is at par. That is Schmid's "a default swap is a par product" sentence turned into a Greek.

**The trap:** The usual slip is to say "I hedged JTD, so default can't hurt me." The hedge is flat at the recovery you assumed, not at the one the auction prints. The runner-up is hedging market value, \$7.2mm (bond price times face). That is neither JTD-flat (+\$0.98mm at 35) nor recovery-flat. A subtler slip is in the scenario itself. If the bond recovers 35 but the auction prices a cheaper deliverable at 25, the package *makes* \$0.57mm. That is §24.5's cheapest-to-deliver option, not a recovery delta, so keep the two apart.

**If you got this wrong, read:** §24.3.1, the Schmid p.159 annotation after the vintage table ($N^{\text{JTD}}$ and its recovery delta), and "Ways This Blows Up" (2) in §24.4 for JTD drift as the price moves; then §24.5.1 for when the bond and the auction stop recovering the same amount.

**Z.24.2: Vintage alpha that isn't**

**Answer:** Take $r = 4\%$, $\lambda = 5\%$, $R = 40\%$, $T = 5$ and nine semiannual bonds with coupons 2%, 3%, …, 10%, each priced off the hazard with `bond_price_hazard`. Prices run from 79.69 to 111.18, and the Z basis against the 297.4 bp CDS runs from +22.1 bp to −18.8 bp. Regress the Z basis on price and you get a slope of −1.29 bp per point, $t = -47$ and $R^2 = 0.997$. With coupons every 50 bp (17 bonds) the $t$-statistic is −72, and every 25 bp (33 bonds) it is −106. The PECS basis is zero, to about $3 \times 10^{-9}$ bp, on every bond. The "signal" is real, perfectly significant, and worth nothing: every bond earns exactly the same risk-adjusted return, because every bond was priced off the same hazard.

**How:** This extends Listing 24.2. Loop `bond_price_hazard`, `z_spread` and `pecs` over the coupon grid, then run OLS of $b^{Z} = 10^4(s^{\text{CDS}} - Z)$ on $100P$. The slope comes from the recovery convention. The swap's loss is $1-R$ of face, but the Z-spread prices a loss of roughly $(P-R)/P$ of market value. That gives

$$
Z \approx \lambda\,\frac{P-R}{P}, \qquad b^{Z} \approx \lambda(1-R) - \lambda\,\frac{P-R}{P},
$$

which falls smoothly as $P$ rises. (This is the instantaneous version and it overstates the size, because the price pulls to par over the bond's life. Only the sign and the shape carry over.) A deterministic function of price, regressed on price, gives a $t$-statistic that grows like $\sqrt{n}$ as you add bonds. The 0.3% of variance the line misses is curvature (the quadratic term is positive), not noise. The zero crossing sits at a price of about 95.1, not 100. The ACT/360 CDS spread (297 bp) is below the 303 bp Z-spread of a par semiannual bond, which matches the Figure 24.1 caption. The "cheap-bond" sort, long negative-Z-basis bonds against short positive ones, is a sort on coupon: it is long premium bonds and short discount bonds, with zero expected excess return.

**The trap:** The trap is to read a big $t$ as a big effect. Significance measures how precisely you estimated a pattern, not whether the pattern pays. Here the precision is perfect because there is no noise at all. Note the sign as well. The convention makes discount bonds look *rich* (positive $b^{Z}$), not cheap. So if your screen says the 2021 low coupons are cheap, the recovery convention is not the cause. Look for something like Ruth's stale curve date. Either way, rerun the regression on $b^{\text{PE}}$: the slope goes to zero.

**If you got this wrong, read:** §24.3.1 (the box "forty back on what?" and *The Full Derivation: the vintage pattern*), then the Ruth vignette in §24.3 for what a vintage effect usually turns out to be.

**Z.24.3: The band in March 2020**

**Answer:** Before costs ($k^{-} = 0$), the negative edge $-\phi(1-h)$ moves from $-30 \times 0.90 = -27$ bp to $-150 \times 0.65 = -97.5$ bp. A −186 bp IG basis lay *outside* the band in both cases: by 159 bp before and by 88.5 bp after. So the band says the package should have been bought. It wasn't, at least not fast enough, and the gap is the term the exercise left out. At a 35% haircut the package's carry of 88.5 bp is only a 2.5% ROE over cash, against 15.9% at the old terms. For −186 to sit *on* the edge you need $k^{-} = 88.5$ bp. As a hurdle on the posted equity, that is $88.5/0.35 \approx 25\%$ a year over cash: a plausible price for scarce balance sheet that month *(illustrative)*.

**How:** Use the carry from §24.4.1, with the basis in bp of face:

$$
\pi^{-} = -b - \phi(1-h), \qquad \text{edge} = -\phi(1-h) - k^{-}.
$$

Before: $\pi^{-} = 186 - 27 = 159$ bp, and $\text{ROE}^{-} = 0.0159/0.10 = 15.9\%$. After: $\pi^{-} = 186 - 97.5 = 88.5$ bp, and $\text{ROE}^{-} = 0.00885/0.35 = 2.5\%$. Take the two moves one at a time. The repo spread alone (150 bp at $h = 10\%$) puts the edge at −135. The haircut alone (30 bp at $h = 35\%$) *narrows* it to −19.5, because you borrow less. The haircut does its damage through the divisor, not through the edge. It also bites through the mark-to-market: a further 100 bp of widening at $D^{\text{spr}} = 4.5$ costs 45% of equity at $h = 10\%$ and 12.9% at 35%. Writing $k^{-} = \rho h$ for a hurdle $\rho$ on equity, the edge becomes $-\phi(1-h) - \rho h$, and this is where the haircut widens the band.

**The trap:** One common slip is to compare −186 with $-\phi = -150$ and say "outside by 36," which forgets the $(1-h)$. The bigger one is to conclude "outside the band, so free money." The band as written prices the equity at the risk-free rate. In March 2020 equity was the scarce input: Mags's prime broker raised haircuts in the same week the basis widened. A basis outside a band that leaves out the price of balance sheet is a measurement of that price.

**If you got this wrong, read:** §24.4.1 (the band, the ROE line and the mark-to-market paragraph), Long Scene A in §24.4 for the same arithmetic on Ines's blotter, and "Ways This Blows Up" (1) in §24.4 on the haircut as a process.

**Z.24.4: ROBO rounds the IMM**

**Answer:** Listing 24.5's own eight-dealer book does it. The raw midpoint is exactly 26.8125, which is 214.5 eighths. Rounding halves up gives an IMM of 26.875, and Python's `round()` gives ROBO 26.75. Now add a rogue \$10mm bid at 30.0 against \$5mm of net selling open interest. The book clears at $p^{*} = 30.0$, the cap binds, and the final price is $\text{IMM} + 1$: 27.875 for the correct auction and 27.75 for ROBO's. Protection buyers are paid 72.125 rather than 72.25 points. On \$5bn of CDS outstanding *(illustrative)*, ROBO's auction moves $0.125\% \times \$5\text{bn} = \$6.25$mm from protection sellers to protection buyers. The crossing dealer's Adjustment Amount changes as well, to \$25,000 from \$22,500.

**How:** Sort the bids down and the offers up. The first pair, a 28.0 bid against a 27.0 offer, crosses and is discarded. That leaves seven pairs, of which you keep the best $h = \lceil 7/2 \rceil = 4$:

$$
\text{IMM}^{\text{raw}} = \frac{(26.25 + 26 + 26 + 25.75) + (27.25 + 27.5 + 27.75 + 28)}{8} = \frac{214.5}{8} = 26.8125 .
$$

That is a tie between 26.75 and 26.875. Halves-up goes to 26.875, and round-half-to-even goes to 214 eighths, or 26.75. In stage 2, OI $< 0$ walks the bids from the top. The rogue bid fills all \$5mm at 30.0, so $\text{FP} = \min(30.0,\ \text{IMM} + 1)$ and the whole rounding error passes through. The buy side works the same way. A rogue \$10mm offer at 24.0 against \$5mm of buying gives $\max(24.0,\ \text{IMM} - 1)$, which is 25.875 against 25.75.

**The trap:** One slip is to think a rounding error is at most a sixteenth. On a tie it is a full increment, because the two candidates are an eighth apart. Another is to assume the IMM error never reaches the final price. It doesn't when the cap is slack: at \$50mm of selling both versions clear at 23.0. It does whenever the final price *is* the IMM, which happens when OI is zero or the cap binds. Watch the units too: an eighth of a point is 0.125% of notional, so \$6.25mm, not \$625k.

**If you got this wrong, read:** §24.6.1 (the IMM formula and the cap cases), the ROBO paragraph in the Specification for the auction simulator, and Figure 24.4's right panel, which is this exact book.

**Z.24.5: Design a drop-down (on paper)**

**Answer:** *Design A (no Successor):* have NewCo assume exactly \$1,000mm, which is 25.0% of the \$4bn. "More than 25%" is strict, so `successors({"NEWCO": 0.25})` returns the swap unchanged. At \$1,000.01mm the swap splits. *Design B (two Successors):* have NewCo assume more than \$1.0bn and less than \$3.0bn, say \$2.0bn. NewCo is above 25% and the original keeps more than 25%, which is case 3, so each \$10mm swap becomes \$5mm on NewCo and \$5mm on the original. Stop short of \$3.0bn: at exactly 75%, NewCo takes the whole swap (case 1). For a protection buyer, **Design A is the more dangerous**, because its limit is an orphan and no rule ever fires on the way there.

**How:** Run Listing 24.7 on the shares $w = D_{\text{moved}}/\$4\text{bn}$ and walk the four cases. With one new entity, any $w \in (0.25, 0.75)$ leaves $w_0 = 1 - w > 0.25$ automatically, so the whole interval is case 3. Design B costs the buyer something visible. The DC announces the split, half the notional may sit on whichever entity the sponsor made safe (the Windstream/Uniti shape), and the buyer can reprice and re-hedge. Each half still references an entity with debt to default on and to deliver. Design A is invisible. The code even lets you repeat it: three subsidiaries at 25.0% each move \$3bn, or four move all \$4bn, and the code still prints "unchanged." The real Definitions would test that chain as a Steps Plan, which the code does not model. The assumption test decides the real case. Under the 2014 Definitions an entity *succeeds* to an obligation only if it becomes liable for it (by law or by agreement) or issues bonds or loans exchanged for it, and the reference entity then stops being an obligor or guarantor of it. If NewCo instead borrows new money and the proceeds *repay* the original's bonds, NewCo succeeds to nothing. Its share is 0% however much debt moved economically, so Design A has no \$1bn ceiling. The swap stays at full notional on a shell whose deliverable set shrinks toward empty: McClatchy's planned refinancing in §24.8.1. If the original stays a guarantor, there is no succession either, but the moved debt may stay deliverable, which helps the buyer.

**The trap:** One slip is to answer "\$1.0bn plus a dollar." That is 25.00000…1% and it splits the swap. Another is to put \$3.0bn into Design B, which hands the whole swap to NewCo. On the judgement, the common mistake is "no Successor means nothing happened, so A is safe." The step function is flat at 25.0%, and so is the screen, but that is exactly how an orphaning plan looks from the outside. A data trap sits underneath: compute shares from principal amounts as exact fractions, because a float that arrives as 0.2500000001 turns Design A into Design B.

**If you got this wrong, read:** §24.8.1 (the staircase box, the four-case table and the orphaning paragraph on McClatchy and Octus), then the Specification for the successor map, which routes Steps Plans and the assumption test to counsel.

**Z.24.6: Kaz writes a credit event**

**Answer:** Three levers, each of which works in both directions:

1. **Move the cash.** To manufacture the event, pay a dividend, prepay or buy back debt, fund an acquisition, or sweep cash to an unrestricted or non-guarantor subsidiary outside the model's perimeter. Runway falls below four weeks and creditworthiness hasn't changed. To avoid it, take a short-dated injection from a sponsor, or rescue money from a protection seller (the RadioShack pattern), that holds runway above four weeks until the swaps expire.
2. **Write the forecast.** The issuer writes the 13-week model. Front-loading disbursements, pushing receipts back a week, haircutting collections, or assuming the revolver is or isn't available are all defensible judgements, and each one moves runway by weeks.
3. **Time the test.** Draw the revolver, stretch payables, factor receivables or defer capex in the week the model is read, which is window dressing. Or let a facility lapse just before it, which is the reverse. "Less than four weeks" is a cliff, and 4.0 against 3.9 is a choice.

Kaz's trigger is **worse than Failure to Pay as a trigger, and better as evidence.**

**How:** Compare what each definition asks a committee to verify. Failure to Pay asks about a fact: was a payment of at least the \$1mm Payment Requirement missed after its grace period? Anyone can check it, and the issuer pays a real price to manufacture it, a default under its own documents (Hovnanian had to engineer a \$1.04mm missed coupon and a lender to pay for it). The 13-week model is a forecast. It is unaudited, unpublished, revised weekly, and every line of it belongs to the issuer, so it is cheaper to move in either direction and no Determinations Committee can verify it. What Kaz's version gets right is the link to creditworthiness. Hovnanian, at about 80 weeks of runway, could never have triggered it. That is the job of the 2019 NTCE Credit Deterioration Requirement, and it is how the chapter uses the model. Keep Failure to Pay as the hard trigger, and use the 13-week model as evidence for or against deterioration: the "more than 52 weeks of runway" flag in Listing 24.7.

**The trap:** The usual answer is "better, because it measures real distress." It does, in the issuer's own hand. A definition the issuer writes is a definition the issuer can game. Hovnanian showed that the gap between a contract's trigger and the company's condition is where the engineering goes. Kaz's version moves that gap from a payment date into a spreadsheet, where it is harder to see.

**If you got this wrong, read:** §24.8.2 (Long Scene B, Theo's runway model as evidence, and the Docket Diary), §24.8.4 on the Credit Deterioration Requirement and what it does not reach (manufactured non-defaults and orphaning), and the manufactured-event flags in the successor-map Specification.

## Part VII: Alternative Data, NLP, AI & Systems

### Z.25 Chapter 25: NLP for Credit Agreements, Indentures & PACER Dockets

Six exercises: one on a recursive cap, one on a regex, one on a min cut, one on a cosine, one on a vote, and one on a pager. Every number below was recomputed from the chapter's inputs and from Listings 25.1 to 25.9 (Appendix F), run in order in one interpreter. Write your own answer before you read ours; on this chapter the trap is usually the answer that arrives first.

**Z.25.1: The four most expensive words, again**

**Answer:** Measured "after giving effect," a 30% cap lets add-backs reach $c/(1-c) = 0.3/0.7 = 42.9\%$ of pre-add-back EBITDA $\mathcal{E}_0$, against 30% on the "before" reading. The gap is 12.9 points of $\mathcal{E}_0$, which is exactly $c^2/(1-c) = 0.09/0.7$. The "after" reading doubles the "before" reading at $c = 1/2$ (50% becomes 100%). At Halyard's $\mathcal{E}_0 = \$200$mm, the cap goes from \$60mm to \$85.7mm, so the sponsor's whole \$80mm claim now fits under it, and incremental debt capacity goes from \$361mm to \$458mm.

**How:** The add-back counts toward the base that caps it, so the constraint is $A \le c(\mathcal{E}_0 + A)$. Collect $A$ on the left:

$$
A(1-c) \le c\,\mathcal{E}_0 \quad\Longrightarrow\quad A \le \frac{c}{1-c}\,\mathcal{E}_0 .
$$

Subtract the "before" cap $c\,\mathcal{E}_0$ and put it over one denominator: $\frac{c}{1-c} - c = \frac{c - c(1-c)}{1-c} = \frac{c^2}{1-c}$. For doubling, set $\frac{c}{1-c} = 2c$; divide by $c > 0$ to get $1 - c = \tfrac12$. Notice that the ratio of the two readings is $1/(1-c)$, so it climbs steeply: 1.33 at 25%, 1.43 at 30%, 2 at 50%. The iteration $A_{k+1} = \min\big(80,\ 0.3(200 + A_k)\big)$ in `addback_fixed_point` (Listing 25.2) agrees: it stops at the \$80mm claim, because the fixed point (85.7) is above it.

**The trap:** Running one round of the loop and stopping: $0.3 \times (1 + 0.3) = 39\%$. That is the cap after the add-back has been fed back once, not after it has settled; the remaining 3.9 points come from feeding the extra back again, and again. The geometric series $c + c^2 + c^3 + \dots = c/(1-c)$ is the same answer written as an iteration. On the doubling question, the slip is to solve $c/(1-c) = 2$ and report $c = 2/3$. That doubles $\mathcal{E}_0$, not the "before" reading.

**If you got this wrong, read:** §25.3.3 (Equation 25.1 and the "Fixed points and contractions" box), then the Full Derivation "the cycle as a contraction"; §25.3.4 for what each added dollar of EBITDA buys in capacity.

**Z.25.2: Break Kaz's regex**

**Answer:** Block 1 (Listing 25.1) passes two of the five tests and fails three.

- *Passes:* "Affiliated Lender". With "Affiliated Lender" and "Lender" both in the dictionary, `find_references("no Affiliated Lender shall vote", …)` returns only `{"Affiliated Lender"}`, because the longer term is matched first and its span is consumed. The plural "Affiliated Lenders" passes too.
- *Passes:* the possessive. "the Restricted Subsidiaries' assets" maps to `{"Restricted Subsidiary"}`, because the plural stem accepts "-ies" and the lookahead `(?![A-Za-z])` lets the apostrophe through.
- *Fails:* the inline definition. `(any such transaction, a "Specified Investment")` never becomes a vertex, because `DEF_RE` only reads lines that begin `"Term" means`.
- *Fails:* the redefinition, in either phrasing. Written as `"Indebtedness" means, for purposes of this Article VII, …`, it silently overwrites the Section 1.01 definition: the dict keeps the last one, with "for purposes of this Article VII" glued onto the body. Written as `For purposes of this Article VII, "Indebtedness" means …`, it is never parsed at all.
- *Fails:* the hyphenation, twice. Inside a definition, the body stops at "Unre-", so the edge is lost. Fed the broken text directly, `find_references("any Unre-\nstricted Subsidiary", TERMS)` returns `{"Subsidiary"}`: an edge to the wrong term, which is the substring night again in a third costume.

Two side findings came out of the tests. First, if "Affiliated Lender" is defined in another document, so that it is missing from the dictionary, "Affiliated Lenders" draws an edge to "Lenders". The fix for that is the dictionary, not the regex. Second, the synthetic agreement defines "Lenders" in the plural, so a singular "each Lender" matches nothing.

**How:** Write each case as an assert on `find_references` or `parse_definitions`, run it against Block 1 unchanged, and see which ones fail. The patch makes four changes, all in Block 1:

1. Join a line-break hyphen only when the next fragment starts in lower case, so "Run-\nRate" keeps its hyphen. Do the join inside `find_references`, so the character offsets into the raw text, which are the citation anchors, do not move.
2. Let `DEF_RE`'s body run (with `re.S`) up to the next line that opens a definition, instead of stopping at the end of the physical line. This also fixes the wrapped-definition weakness that §25.10 flags.
3. Accept an optional scope in either position. Store scoped definitions under (term, scope) in a second dict, and raise if a global term is defined twice instead of letting the later definition win.
4. Add a second regex for parenthetical definitions. Each match becomes a vertex, with the enclosing clause as its body and the opening parenthesis as its anchor.

After the patch all five tests pass, every assert in Listings 25.1 to 25.9 still passes, and the definitions and edge set for the synthetic agreement come out identical to the original's.

**The trap:** The first trap is to expect the matcher tests (Affiliated Lender, the possessive) to fail and to "fix" the matcher. Block 1 was built for exactly those cases. The three failures are in the parser that feeds the matcher: a term that never becomes a vertex can have no edges, and nothing raises an error. The second trap is the tempting patch for the hyphenation case: dropping the word boundary, or matching case-insensitively, so that "stricted Subsidiary" can be caught. That breaks the existing `"any Unrestricted Subsidiary"` assert and replays Paloma's night. The third is to join every "-\n": that turns "Run-Rate Cost Savings" into "RunRate Cost Savings" whenever a line happens to wrap at the hyphen.

**If you got this wrong, read:** §25.2.4, Paloma's 4:10 a.m. diff and the "Ways This Blows Up" box; then the commentary on Listing 25.1 in §25.10 (the paragraph on the one-line body).

**Z.25.3: Move the cut**

**Answer:** $\Phi = \$100$mm, and the min cut is {trapdoor (\$60mm), direct basket (\$40mm)}. The two upstream baskets (\$250mm) carry only \$60mm and have \$190mm of slack. Add a J.Crew blocker, which sets the IP capacity of every arc into the unrestricted subsidiary to zero, and $\Phi^{\text{IP}} = 0$. The cut is the same two arcs, now at zero for IP. Cash is untouched: $\Phi^{\text{cash}}$ is still \$100mm, and so is $\Phi$.

**How:** Extend Listing 25.3. Give `jcrew_arcs` a fourth arc, ("LoanParties", "Unrestricted", "direct basket", 40), set the trapdoor to 60, and call `max_flow_min_cut`. It returns 100.0 and names the trapdoor and the direct basket. By hand, every $s$–$t$ cut has to contain the direct arc, because that arc runs straight from $s$ to $t$. What remains is to cut the $s \to N \to t$ route at its narrowest point, which gives

$$
\Phi = c_{s\to t} + \min\big(c_1 + c_2,\; c_{N\to t}\big) = 40 + \min(250, 60) = 100 .
$$

For IP, rerun with both arcs into $t$ at zero. That returns 0.0 with the same two arcs in the cut. The theorem's sensitivity statement checks out numerically too: raising either cut arc by \$1mm raises $\Phi$ to 101, and raising an upstream basket changes nothing.

**The trap:** In the first part, the usual wrong answers are 290 (treating the trapdoor as uncapped, as in the chapter's original J.Crew case) and 60 (forgetting that the direct basket is a parallel route, so it sits in every cut). In the second part, the expensive mistake is to model the blocker as "shut the trapdoor". That leaves IP flowing through the direct basket, so $\Phi^{\text{IP}} = 40$, not 0. The mirror image is a blocker drafted only against Loan Party investments in unrestricted subsidiaries. That gives $\Phi^{\text{IP}} = 60$ through the trapdoor, which is exactly the route J.Crew used. Finally, do not add $\Phi^{\text{IP}}$ to $\Phi^{\text{cash}}$. The two commodities draw on the same baskets, so each figure is an upper bound on its own commodity, and they never sum.

**If you got this wrong, read:** §25.4.1 (the pipes box and max-flow min-cut), then "Blockers are commodity-specific cuts" in §25.4.2, and the Listing 25.3 commentary in §25.10 on why the listing's blocker is two single-commodity runs.

**Z.25.4: How loud must a covenant shout?**

**Answer:** $1 - \cos(x, x') = k^2/\|x\|^2$, so for a 1% move you need $k^2 = 0.01 \times 2.4 \times 10^6 = 24{,}000$, or $k \approx 154.9$: about **155** occurrences, every one of them amended. One occurrence moves cosine by $4.2 \times 10^{-7}$ (Listing 25.4 prints $4.17 \times 10^{-7}$ with $\|x\|^2 = 2{,}399{,}897$).

**How:** "4.50" appears $k$ times ($x_i = k$), "5.25" never ($x_j = 0$), and the amendment moves all $k$: $x' = x - k\,e_i + k\,e_j$. The dot product loses $k \cdot k$ on coordinate $i$ and gains nothing on $j$. The new length loses $k^2$ on $i$ and gains $k^2$ on $j$:

$$
x \cdot x' = \|x\|^2 - k^2, \qquad \|x'\|^2 = \|x\|^2 - k^2 + k^2 = \|x\|^2,
$$

so $1 - \cos = 1 - (\|x\|^2 - k^2)/\|x\|^2 = k^2/\|x\|^2$. Setting that equal to 0.01 gives $k = \sqrt{24{,}000}$. The 2.4 million comes from $n^2/d + n \approx 2.25 \times 10^6 + 1.5 \times 10^5$: Cauchy–Schwarz's floor plus the multinomial noise. If you plant the $k$ copies into Listing 25.4's vector, they add their own $k^2$ to $\|x\|^2$, so 155 copies give 0.991% and 156 give 1.004%. "About 155" is the right level of precision.

**The trap:** The usual wrong answer is to scale the one-token result linearly: $0.01 / (4.2 \times 10^{-7}) \approx 24{,}000$ occurrences. The drop grows with $k^2$, not $k$, because the edit takes $k$ away from the dot product on a coordinate that is itself $k$ long. The quieter wrong answer is 150, from plugging in the Cauchy–Schwarz bound $n^2/d$ as if it were $\|x\|^2$. That bound is a floor on $\|x\|^2$, so it understates both the length and the $k$ needed. And neither number changes the conclusion: the capacity change is \$200mm whether the ratio appears once or 155 times.

**If you got this wrong, read:** §25.5.1, the shopping-list box and the Full Derivation "one swapped token" (redo it with $k$ in place of 1); then the commentary on Listing 25.4 in §25.10.

**Z.25.5: Is the group a blocker?**

**Answer:** The group's true share is somewhere in $[32.8\%, 33.2\%]$.

- **"Blocks" is robust** for every turnout $\varphi < 98.4\%$, down to the group's own 33% (if the group votes, turnout cannot be below its holding).
- **"Does not block" is robust** for $\varphi \ge 99.6\%$.
- **The ambiguous band** is $98.4\% \le \varphi < 99.6\%$, just 1.2 points of turnout wide.

PACER fees to resolve it: at most \$3 a document, however long the PDF. That is \$3 for the latest statement, or \$6 for both, to see whether the amounts are exact or "approximately". The balloting agent's tabulation declaration, which is where the turnout comes from, is one more document at \$3 or less. If that is all the desk buys this quarter, PACER's waiver of bills of \$30 or less makes the invoice \$0. Less than the coffee indeed.

**How:** The group blocks on amount when $\theta > \varphi/3$. A verdict is robust only if it holds at both ends of the interval. "Blocks" needs the *smallest* share to clear the bar, $0.328 > \varphi/3$, so $\varphi < 0.984$. "Does not block" needs the *largest* share to miss it, $0.332 \le \varphi/3$, so $\varphi \ge 0.996$. Between those two turnouts the answer depends on rounding you cannot see. A grid check against `blocks` in Listing 25.7 reproduces both edges. The ±0.2% comes from four members each good to \$0.5mm on \$1,000mm. If you think rounding applies per *lot* rather than per member, Holder_A's two lots make five roundings, the interval becomes ±0.25%, and the band widens to 98.25%–99.75%. Either way, the band sits near full turnout because 33% is so close to a third.

**The trap:** The first trap is to use the point estimate and report one cutoff, "blocks below 99%, not above". That skips the band, which is the whole point of carrying an interval. The second is to treat "exactly a third" as a block. At $\theta = 33.2\%$ and $\varphi = 99.6\%$ the group holds exactly one third of the vote, and §1126(c) needs more than one third, so it does not block. The third is to get the direction backwards: a fuller room raises the bar, so higher turnout makes blocking harder. On the fees, the slip is to price the PDF by the page (a 40-page statement at \$0.10 a page would be \$4). The \$3 cap applies first.

**If you got this wrong, read:** §25.7.1, the "fuzzy slices" box, the blocking arithmetic and the rounding bound $n\delta/(2F_c)$; then §25.6.1 (Friday: PACER's fees, the cap and the waiver) and Mags's grade in §25.7.3.

**Z.25.6: Spec ROBO into sleeping through the utilities**

**Answer:** Theo's sticky note, as a spec:

1. *Page only for a Rule 2019 statement whose filer discloses a class on the desk's watchlist* (here the first-lien term loan and the 2020 super-priority debt), reading the class from the statement's first page, not from the entry text.
2. *Within those, page on the first statement from a group not yet seen in the case, and on any amended or supplemental statement (ordinal ≥ 1) from a group already on the watchlist.*
3. *Every other Rule 2019 entry (utilities, equity, trade, landlords) goes to the 7 a.m. digest. Never page on `doc_class` alone.*

Key on these fields: `doc_class`; the filer, resolved from `description` to a stable group id; the amendment ordinal, also parsed from `description` ("amended", "second amended", "supplemental"); the disclosed `class` from `r2019_lots`; and the `docket_number` on the watchlist. Run on the seven Serta rows, the spec pages for Docs. 69, 75, 389 and 1116 and sends Docs. 273, 289 and 311 to the digest. Theo sleeps through all three 2 a.m. pages and still gets the second amended priority-lender statement eight days before emergence.

**How:** Ask what makes a statement matter to a term-loan position. The answer is who holds what, and what changed. The class field answers "what". The group id plus the ordinal answers "who" and "what changed". The doc class only says the paper is the right shape. Test the rule against the `type=rd` table in §25.7.3 row by row, including the two rows it must not suppress: the excluded lenders' original (Doc. 75) and the priority group's amendments (Docs. 389 and 1116). Reading the class means opening the PDF, at up to \$3 a statement. That is the same lesson Kaz's card learned: the free docket text says who filed, not what they hold.

**The trap:** Most wrong specs key on the filer's name. A deny-list on "utility" fails the next time the filer is the Ad Hoc Committee of Trade Creditors. An allow-list on "Ad Hoc" still pages at 2:11 for Doc. 289, the Ad Hoc *Equity* Group. Keying on "amended" alone pages at 2:26 for the utilities' supplement (Doc. 311) and stays silent for the day-one original from the excluded lenders (Doc. 75). Quiet hours are not a fix either: they delay the page that matters along with the ones that don't.

**If you got this wrong, read:** §25.7.3, beat three (the 2 a.m. page) and the `type=rd` table; §25.7.1 on endogenous sampling (why an amendment from a known group is the event); and the `docket_entries` and `r2019_lots` schemas in §25.10.

### Z.26 Chapter 26: AI Agents & LLMs on the Credit Desk

Six exercises: two on prices (the abstention bar and the scoring rule), two on probability (retries and pass$^k$), one on the calendar, and one on a document that lies about itself. Every number below was recomputed in Python from the chapter's inputs and from Listings 26.1 to 26.3 (Appendix F). Write your card before you read ours.

**Z.26.1: The price of a check**

**Answer:** $p^\ast = 1 - 250/150{,}000 = 1 - 1/600 \approx 0.9983$. At that bar the reader answers 31% and sends 69% to people, but the queue holds only 40%. So the **human queue binds**, and it is short by 29% of volume. Pay for the shortfall, don't move the bar to hide it. Buy the checks (29 more per 100 questions at \$250, or \$7,250 per 100 questions), work the queue in order of expected loss so that whatever is left over is the cheapest to leave, price $C_{\text{FP}}$ position by position (not every basket question carries a \$150,000 mistake), or defer what can wait. Lowering the threshold until coverage reaches 60% is the costliest of these options. Every claim it lets through below 0.9983 costs more in expectation than the \$250 check it replaces: at $p = 0.99$ the expected loss is \$1,500, the price of six checks.

**How:** Answering beats checking when $(1-p)\,C_{\text{FP}} < C_{\text{abs}}$, so the bar sits where the cost ratio puts it, here 600 to 1:

$$
p^\ast = 1 - \frac{C_{\text{abs}}}{C_{\text{FP}}} = 1 - \frac{250}{150{,}000} = 0.99833 .
$$

The queue needs $1 - \phi \le 0.40$, i.e. coverage $\phi \ge 0.60$, and the reader gives 0.31. The reader's coverage is a fact about the reader. The queue's 40% is the constraint, and it binds. For any claim with $p < p^\ast$, answering it unchecked costs $(1-p)C_{\text{FP}} - C_{\text{abs}} > 0$ in expectation, by the definition of $p^\ast$. A lower threshold therefore always loses money compared with buying the check, and the only open question is who pays. The \$250 is desk opex: it shows up in the analyst budget every month. The \$150,000 is an expected loss on the book: it belongs to the PM, and through the PM to the investors, and nobody sees it until it lands. Lowering the threshold moves cost from the visible line to the invisible one. So the person who owns the invisible line (the PM, with risk signing) has to sign the change, and it goes in the model inventory with the cost assumptions written down (§26.5's third point). When the queue still binds, the honest product is an order in which to read: check claims in descending order of $(1-p)\,C_{\text{FP}}$. (A sanity flag: under §26.12's toy reader, a bar of 0.9983 sits 5.5 standard deviations above the mean difficulty and coverage would be essentially zero. A 31% coverage already assumes the deterministic checks are carrying a lot of the load.)

**The trap:** "The reader binds, it only answers 31%, so lower the threshold until it answers 60%." That treats $p^\ast$ as a tuning knob when it is a price. Moving it quietly declares that a wrong basket costs less than \$150,000, without asking the person who pays for it. Smaller slips: inverting the ratio ($250/150{,}000 = 0.0017$, "answer everything"), and reusing the chapter's 0.95, which belongs to a 20-to-1 cost ratio. This one is 600 to 1.

**If you got this wrong, read:** §26.5, the cost version of Kalai's rule and the "three things go wrong" paragraph; then §26.3 at 11:40, where the bar is 99.5%, the queue binds and Theo's card turns the list into a reading order; and $J(\vartheta, \phi)$ in §26.6, "The bill and the frontier".

**Z.26.2: Lazarus, audited**

**Answer:** At $m = 2$ (two attempts, which means one retry), $\Pr(\text{right}\mid\text{accepted}) = 0.9526$ and coverage is $0.9439$, which matches the chapter's 0.953 and 0.944. For the whole path: $m = 1$ gives 0.9614 and 0.830, $m = 3$ gives 0.9479 and 0.9745, and $m \to \infty$ gives 0.9432 and 1. A Monte Carlo run of 2 million paths gives 0.9526 and 0.9436. With a single question type the posterior is $a_R/(a_R + a_W)$ for every $m$ (0.977 at $p = 0.9$). Retries still are not free: in the mixture, the answers that come back on the second try are right only 88.8% of the time, against 96.1% on the first.

**How:** Per attempt, $a_R = p(1-f)$, $a_W = (1-p)(1-d)$ and $r = 1 - a_R - a_W$. Easy questions have $(0.9025,\ 0.010,\ 0.0875)$ and hard ones $(0.38,\ 0.12,\ 0.50)$. A type is accepted within $m$ attempts with probability $1 - r^m$. Because $1 - r = a_R + a_W$, the geometric series cancels, and type $j$'s posterior is $\pi_j = a_{R,j}/(a_{R,j} + a_{W,j})$ (0.989 for easy, 0.760 for hard), with no $m$ in it. That is the single-type result. The mixture is a weighted average with weights that do depend on $m$:

$$
\Pr(\text{right}\mid\text{acc}) = \frac{\sum_j w_j\,\pi_j\,(1 - r_j^m)}{\sum_j w_j\,(1 - r_j^m)}, \qquad \text{coverage} = \sum_j w_j\,(1 - r_j^m).
$$

At $m = 2$ the easy questions contribute $0.8(1 - 0.0875^2) = 0.7939$ and the hard ones $0.2(1 - 0.5^2) = 0.15$. So coverage is 0.9439 and precision is $(0.7939 \times 0.989 + 0.15 \times 0.76)/0.9439 = 0.9526$. The point for Kaz is that $m$ moves the weights toward the type with the high $r$, which is the hard type with the low $\pi$. Hard questions go from 12.0% of accepted answers to 15.9%, and the 11.4 points of extra coverage arrive at 88.8% precision. The option is exercised by the questions you get wrong. Even in the one-type case the retries cost tokens and latency. And the i.i.d. assumption flatters them: a second draw from the same model is correlated with the first, so the answer that finally gets past a same-family verifier is selected for that verifier's blind spot. That is Ines's rebuy.

**The trap:** Two numerical ones. If you weight the per-type posteriors by the prior shares, $0.8 \times 0.989 + 0.2 \times 0.76 = 0.943$, you have computed the $m \to \infty$ limit, whatever $m$ you meant, because only infinite retries accept every question. If you read $m$ as a count of retries rather than attempts, so that $m = 2$ means three attempts, you get the chapter's $m = 3$ row (0.948, 0.974). The conceptual trap is Kaz's: "the posterior doesn't depend on $m$, so retries are free". That holds for one question type, and a desk never has one.

**If you got this wrong, read:** §26.6, "Verifiers, retries and the Lazarus rate" and its Full Derivation; the *A checker, in odds* box for the one-type posterior; and `verified_closed_form` and `simulate_verified` in Listing 26.3 (Appendix F), which this exercise reruns at $m = 2$.

**Z.26.3: ROBO, scored**

**Answer:** Score a right answer $+1$, an abstention $0$ and a wrong answer $-w$, with $w = (C_{\text{FP}} - C_{\text{abs}})/C_{\text{abs}}$. Answering is then worth $p - (1-p)w$, which is positive if and only if $p > w/(1+w) = 1 - C_{\text{abs}}/C_{\text{FP}} = p^\ast$. That is Kalai et al.'s rule with $t = p^\ast$. On the §26.12 reader at 20 to 1 ($w = 19$): answer-everything scores $-3.61$ per question, abstain-everything scores 0, and the honest reader scores $+0.012$ (it answers 4.3% of questions and gets 3.7% of those wrong). At 5 to 1 ($w = 4$) the three scores are $-0.15$, 0 and $+0.21$, with 51% answered and 11.8% of those wrong. A reader with no power that answers the same share scores $-0.16$ and $-0.08$, so honesty without eyesight loses too. When a vendor reports a single accuracy number $a$, the rule collapses to one point. It can score only answer-everything, at $(a - t)/(1 - t)$ (86% at $t = 0.95$ scores $-1.8$ per question), and it says nothing about the policy you would actually run.

**How:** Start from the desk's costs: a right answer costs 0, an abstention $-C_{\text{abs}}$, a wrong answer $-C_{\text{FP}}$. Add $C_{\text{abs}}$ and divide by $C_{\text{abs}}$. That is a positive affine map, so it changes no decision, and it gives $+1$, $0$ and $-(C_{\text{FP}} - C_{\text{abs}})/C_{\text{abs}}$. With $t = p^\ast$, $t/(1-t) = (C_{\text{FP}} - C_{\text{abs}})/C_{\text{abs}} = w$, which is Kalai's penalty. The honest policy (answer iff $p > t$) is optimal question by question. It beats answer-everything by $\mathbb{E}\big[((1-p)w - p)^+\big]$, which is positive as soon as some questions have $p < t$. It beats abstain-everything by $\mathbb{E}\big[(p - (1-p)w)^+\big]$, which is positive as soon as some have $p > t$. It can act on that split only if its $\hat p$ separates the two groups, which is what power means. In risk–coverage terms the score per question at threshold $\theta$ is

$$
\text{score}(\theta) = \phi(\theta)\Big[1 - \frac{R(\theta)}{1 - t}\Big],
$$

which is positive if and only if the selective risk satisfies $R < 1 - t = C_{\text{abs}}/C_{\text{FP}}$. A vendor's single accuracy number is the point $\phi = 1$, $R = 1 - a$. Scoring the honest policy needs $\phi$ and $R$ at *your* $t$, and that means the curve. If the vendor's number is accuracy on answered questions with no coverage beside it, abstaining on everything but one sure question posts 100%, which is ROBO's 0.0% at 0.0% again.

**The trap:** Grading only one side of the trade-off. Grade accuracy alone and answer-everything wins; grade hallucination rate alone and abstain-everything wins. Those are ROBO's two bosses. The quieter trap is a round-number penalty such as $-1$, which puts $t$ at 0.5 and lets the reader bluff on every 60% claim, when a wrong basket costs twenty checks. The penalty has to be the cost ratio.

**If you got this wrong, read:** the start of §26.5 (Kalai et al., the cost version, and ROBO's two failures); then §26.4, "Calibration and selective prediction", for $\phi$, $R$ and why power cannot be added after the fact; then the Paleologo annotation in §26.3 on vendor numbers.

**Z.26.4: Prove it**

**Answer:** For $p \in [0,1]$ and $k \ge 1$, $p^k \le p \le 1 - (1-p)^k$, with equality only at $k = 1$ or $p \in \{0, 1\}$. Both $\binom{c}{k}/\binom{n}{k}$ and $1 - \binom{n-c}{k}/\binom{n}{k}$ are unbiased, because each is an average of an indicator over all $\binom{n}{k}$ subsets of attempts. Put pass$^k$ in the model-risk report. pass@$k$ is in the vendor deck because it is the bigger number (0.998 against 0.168 at $p = 0.7$, $k = 5$), and because it quietly assumes an oracle that picks out the attempt that worked.

**How:** The bounds take one line each: $p^k = p \cdot p^{k-1} \le p$, and $(1-p)^k \le 1 - p$ gives $1 - (1-p)^k \ge p$. For unbiasedness, let $X_1, \dots, X_n$ be i.i.d. Bernoulli($p$). Among the $k$-subsets $S$, exactly $\binom{c}{k}$ contain only successes, so

$$
\frac{\binom{c}{k}}{\binom{n}{k}} = \frac{1}{\binom{n}{k}} \sum_{|S| = k}\ \prod_{i \in S} X_i , \qquad \mathbb{E}\Big[\prod_{i \in S} X_i\Big] = p^k ,
$$

and the average of terms with mean $p^k$ has mean $p^k$. Replace $X_i$ by $1 - X_i$: $\binom{n-c}{k}/\binom{n}{k}$ is unbiased for $(1-p)^k$, so one minus it is unbiased for pass@$k$. Both need $k \le n$, because otherwise there are no $k$-subsets to average over, and that is why the listing returns NaN. A worked case: with 14 successes in 20, the pass$^5$ estimate is $2002/15504 = 0.129$ and the pass@5 estimate is $1 - 6/15504 = 0.9996$. Averaged over $c \sim \text{Bin}(20, 0.7)$, the first comes to exactly $0.7^5 = 0.16807$. On the report: the desk asks the same clause every quarter and acts on every answer, so the event that costs money is "wrong at least once", and pass$^k$ is its complement. pass@$k$ is best-of-$k$ with a perfect picker. In a coding benchmark the unit test does the picking. On a desk, if you had a perfect picker you would not need the reader.

**The trap:** Using the plug-in $(c/n)^k$. Because $x^k$ is convex, Jensen gives $\mathbb{E}[(c/n)^k] \ge p^k$. At $n = 20$, $p = 0.7$, $k = 5$ the plug-in averages 0.204 against a true 0.168, overstating consistency by about a fifth. (The pass@$k$ plug-in errs the other way: it is concave, and it averages 0.9940 against 0.9976.) The other trap is returning 0 when $k > n$. A zero averages into a dashboard as "this agent never works". NaN says "not measured".

**If you got this wrong, read:** §26.6, "The arithmetic of chains" and "The Full Derivation: the unbiased pass^k estimator", with the *Reliability multiplies; attempts add* box; then `pass_hat_k` and `pass_at_k` in Listing 26.3 (Appendix F).

**Z.26.5: The melting ice cube**

**Answer:** **9 clean months** (April to December 2026) for any feature the new model computes, down from 18 (July 2025 to December 2026) under the June 2025 cutoff. The other 27 months, January 2024 to March 2026, are inadmissible for new-model features. The feature history computed with the old model is still usable, and keeps its 18 clean months, but only if its outputs were logged when they were made, with each value keyed by prompt hash, model id, sampling parameters and timestamp. The model version must also have been pinned for the whole stretch, with no silent vendor update; check that $\hat\kappa$ and the cross-family disagreement rate stay flat across it. And the prompt must have been frozen before July 2025. Recomputing "with the old model" later counts only if the vendor still serves the pinned weights and your $\hat\kappa$ on a fixed prompt set shows they have not moved. The stakes are measurable: a Sharpe ratio's standard error is about $1/\sqrt{0.75} = 1.15$ over 9 months and $1/\sqrt{1.5} = 0.82$ over 18, so a true Sharpe of 2 is 1.7 standard errors from zero in one case and 2.4 in the other. The vendor's update cost you the ability to measure the feature.

**How:** The admissible set for a generator with cutoff $T_c$ is

$$
\mathcal{T}_{\text{adm}} = \{\, t : t > T_c \,\},
$$

and the cutoff that matters is the cutoff *of the model that produced each value*. On 36 month-start dates from January 2024, $T_c$ = 30 June 2025 admits 18 dates (Listing 26.3 asserts exactly this), and $T_c$ = 31 March 2026 admits 9. Kaz's springing lien: a springing lien attaches when a trigger written into the document fires, and it binds collateral from then on. Nothing attaches to values you have already logged. What moves is $T_c$, and it moves only in the admissible set of features the *new* model computes. That model has read July 2025 to March 2026, so its knowledge reaches back over nine months that used to be clean. Going forward, either stay on the pinned old version or bring the new one in as a challenger scored on an overlap of post-March months. Do not splice old-model values before the switch onto new-model values after it without a version column, because a level shift on the switch date is a feature of the vendor, not of the covenant.

**The trap:** There are two, and they point in opposite directions. "The update contaminates everything, so throw the old history away" is wrong, because a value produced by a model that had not read the future stays clean, provided you can prove which model produced it. "Nothing changed, rerun the backtest with the new model, still 18 months" is wrong, because the new model has read the ending of nine of those months. The off-by-one: counting March 2026 as clean (10 months). A cutoff stated as a month means the model may have read any day of it.

**If you got this wrong, read:** §26.7, the admissible window and the melting-ice-cube paragraph, and Long Scene B at 11:05 (seven clean months, standard error 1.3); then §26.9's replay contract (stochastic outputs are stored as point-in-time data and never re-run) and §26.8's vendor row (every update enters as a challenger).

**Z.26.6: The technical amendment**

**Answer:** The test is a section-scoped diff of operative text, and it runs before the reader does. **Inputs:** (1) the conformed copy $C$, as amended through the day before the amendment, in the store's canonical normalized text, with its hash; (2) the amendment: every character in the PDF's text layer, whatever its colour, size or position, normalized the same way, together with the post-amendment text $C'$ it produces (its conformed exhibit, or its "is hereby amended" instructions applied in code); (3) the section index, which maps section ids such as 6.08(b)(xii) to character ranges in $C$ and $C'$. **Output:** the set $\Delta$ of section ids whose text changed, each with its old and new SHA-256 and the changed lines. Any claim of the form "does not modify §$X$" fails when $X \in \Delta$, and the capacity column cannot stay put until a human signs. On §26.10's document, $\Delta$ contains 6.08(b)(xii) with eleven changed lines, and the white-text claim fails. **The failure mode:** a change routed through a definition. Amend "Consolidated EBITDA" (an uncapped add-back, like "Automatable Services" in §26.3) or "Available Amount" in Article I and leave §6.08 byte-identical. A section-scoped diff then excludes 6.08 from $\Delta$, "this amendment does not modify Section 6.08" is literally true and economically false, and the test passes the malicious document along with it.

**How:** Normalize $C$ and $C'$ the same way (ligatures, hyphenation, whitespace), slice both by the section index, compare hashes section by section, and emit line diffs wherever they differ. Visibility never enters the test: it reads the same bytes whether they render black, white or at half a point. That is why it beats a "find the white text" detector, which an attacker defeats by switching to a tiny font or putting the text behind an image. Its strength is that it never trusts what the document says about itself. Its weakness is its scope: it compares text inside sections, while a basket's economics live in the definitions the section uses. Close the gap by diffing the whole agreement and pushing $\Delta$ through the definition graph of Chapter 25, so that §6.08 is flagged whenever any defined term in its transitive closure changes. What is left after that is the one thing no diff can check, its own baseline. If the conformed copy came from the borrower's counsel, or already absorbed an earlier "technical" amendment, the diff measures change from the wrong base. So the conformed copy needs provenance of its own: who prepared it, as of what date, and its hash.

**The trap:** Trusting the citation contract or a second reader. The white sentence earns $V = 1$ and $S = 1$, because the document really does say it, and a second model family reading the same text layer reads the same instruction. Provenance proves that the document said it, not that the document is honest. The smaller trap is to write the test as "detect hidden text". That catches this attack and not the next one, and it raises alarms on harmless white boilerplate.

**If you got this wrong, read:** §26.10, the *Ways This Blows Up* box and Theo's Thursday; §26.4 for what $V$ and $S$ do and do not prove; and Chapter 25's definition graph for the transitive closure.

### Z.27 Chapter 27: System Construction, Low-Latency Infrastructure & ASICs/FPGAs

Seven exercises: a queue, a trigger row, a drop-down written as rows, a stopping rule, a spec, a memo and a pair with one leg missing. Every number below was recomputed from the chapter's inputs, and from Listings 27.3 to 27.5 (Appendix F) where an exercise extends them, with simulations run fresh. Where an exercise asks you to choose an input, ours is stated and marked illustrative. Write your own answer before you read ours. In this chapter the trap is usually the number the system would have reported: the mean, the per-leg view, the field that reads "OK."

**Z.27.1: Kaz's engine on a CPI morning**

**Answer:** The approximate p99 *wait* reaches 500 ms at $\rho \approx 0.31$. To stay inside a 500 ms budget the engine must run at or below that, so the desk has to shed or batch $1 - 0.31/0.5 \approx 38\%$ of quote refreshes at $\rho = 0.5$, and $1 - 0.31/0.9 \approx 65\%$ at $\rho = 0.9$. A Lindley simulation puts the ceiling a little lower, near $\rho = 0.27$ (46% and 70%), because the exponential tail is slightly optimistic at light load when $c_s^2 = 4$. With $c_s^2 = 1$ at $\rho = 0.7$, the mean wait falls from 233 ms to 93 ms, the p99 wait from 1.42 s to 0.57 s, and the p99 sojourn from about 1.5 s to about 0.61 s. The ceiling rises to $\rho \approx 0.66$: nothing needs shedding at 0.5, and 26% at 0.9. The sentence for the risk meeting: *every refresh waits behind whatever the engine is already working on, so the queue is set by the rare slow jobs, not the typical one; halving the lattice jobs cuts the p99 wait from 1.4 s to 0.33 s, while halving the trivial refreshes, which makes the average 25% faster, only gets it to 1.06 s.*

**How:** With $\mathbb{E}[S] = 40$ ms and $(1 + c_s^2)/2 = 2.5$, Pollaczek–Khinchine gives $\mathbb{E}[W_q] = 100\rho/(1-\rho)$ ms, and the tail quantile of §27.5.1 becomes

$$
t_{0.99} \approx \frac{\mathbb{E}[W_q]}{\rho}\,\ln\frac{\rho}{0.01} = \frac{100}{1-\rho}\,\ln(100\rho)\ \text{ms}.
$$

Set it equal to 500 and solve $\ln(100\rho) = 5(1-\rho)$ numerically: $\rho^\star = 0.312$. Check the ends against the chapter: 782 ms at $\rho = 0.5$ and 4.5 s at 0.9. Shedding a refresh, or coalescing several refreshes of one quote into one, removes an arrival, and utilisation is proportional to the arrival rate, so the share to remove is $1 - \rho^\star/\rho$. With $c_s^2 = 1$ the same steps give $t_{0.99} = \frac{40}{1-\rho}\ln(100\rho)$, which is exact for M/M/1. For the sentence, write the mean wait as $\mathbb{E}[W_q] = \Lambda^{\text{q}}\,\mathbb{E}[S^2]/\big(2(1-\rho)\big)$ and model Kaz's 40 ms as 95% trivial refreshes of 21.6 ms and 5% lattices of 389 ms (an illustrative mixture with $c_s^2 = 4$). The lattices supply 94% of $\mathbb{E}[S^2]$. Halving either kind brings the mean to about 30 ms, but halving the lattices cuts $\mathbb{E}[S^2]$ by 71% and halving the trivial refreshes cuts it by 4%.

**The trap:** Two of them. The first is to read the mean: at $\rho = 0.5$ the mean wait is 100 ms, comfortably inside 500, so "no shedding needed." The p99 is 782 ms. The second is to subtract utilisations: going from 0.9 to 0.31 is 59 points of utilisation, but the share of refreshes you have to remove is $0.59/0.9 = 65\%$.

**If you got this wrong, read:** §27.5.1 (both parts of the queues box, then the Full Derivation and the tail quantile); the usage note under Listing 27.3 on feeding the stress hour's load rather than the day's; §27.1.1's grading of the cold-open card.

**Z.27.2: Add LQD and CDX IG to the table**

**Answer:** By the method of §27.6.1, with LQD as the bond's only credit hedge, $\beta_{i,\text{LQD}} = P_i D^{\text{spr}}_i \kappa^{\text{IG}}_i/(H_{\text{LQD}} D_{\text{LQD}}) \approx 1.30$ bond points per LQD dollar; CDX IG on the same footing gives $-0.180$ points per bp. In one row with TY the three must share the work. Split the credit exposure evenly between LQD and CDX IG and take LQD's rate content out of the TY beta, and the row is $\boldsymbol\beta_i = (0.158,\ 0.648,\ -0.0898)$, in bond points per TY point, per LQD dollar and per CDX IG basis point. With $\theta_i = 0.14$ points and the stress-window volatilities below, the budget splits as $\theta_{ij} = (0.014,\ 0.086,\ 0.040)$ points, so the thresholds are 0.089 TY points, \$0.133 of LQD and 0.44 bp of CDX IG. A flight to quality (TY up 6/32, LQD up \$0.09, CDX IG 1.25 bp wider) moves fair value by $-0.024$ points: the joint rule stays quiet, and the per-instrument rule pulls on TY and on CDX. In 200,000 fat-tailed simulated moves the joint rule pulls in 33% of windows and the per-instrument rule in 70%. False pulls are 37% of all windows (53% of the cheap rule's pulls), and the cheap rule misses no joint pull: zero in each of three seeds.

**How:** Inputs, all illustrative: the cold-open bond ($P_i = 95$, $D^{\text{spr}}_i = 8$, 130 bp, $\text{DV01}_i = 0.076$ points per bp, $\kappa^{\text{rate}} = 0.9$); LQD at \$108 with a duration of 8.3, so \$0.0896 per bp; the IG cash index at 85 bp; CDX IG at 55 bp. The DTS betas are $\kappa^{\text{IG}} = 130/85 = 1.53$ and $\kappa^{\text{CDX}} = 130/55 = 2.36$, so

$$
\beta_{i,\text{LQD}} = \frac{95 \times 8 \times 1.53}{108 \times 8.3} = 1.30, \qquad \beta_{i,\text{CDX}} = -\frac{95 \times 8 \times 2.36}{10^{4}} = -0.180 .
$$

Each formula assumes its instrument is the only credit hedge, and LQD's price also carries eight years of rate duration. In a shared row, give each credit hedge half the credit exposure, and read the IG spread change from LQD as $-\Delta H_{\text{LQD}}/0.0896 + \Delta H_{\text{TY}}/0.065$; the second term comes off the TY beta, $1.052 - \tfrac12 (1.53)(0.076/0.065) = 0.158$. Check the row on pure moves: a 1 bp rally gives $0.158(0.065) + 0.648(0.0896) = 0.0684 = 0.9 \times 0.076$, and a 1 bp IG widening gives $-0.116 = -0.076 \times 1.53$. Then allocate as in §27.6.1: $\theta_{ij} = c\,|\beta_{ij}|\,\sigma_j$ with $c = \theta_i/\sum_j |\beta_{ij}|\sigma_j = 0.886$, and $\tau_{ij} = \theta_{ij}/|\beta_{ij}| = c\,\sigma_j$. Our covariance for one stress window: volatilities of 0.10 TY points, \$0.15 of LQD and 0.5 bp of CDX IG; correlations TY–LQD $+0.75$, TY–CDX $+0.35$ (TY rallies when CDX widens) and LQD–CDX $-0.25$. Fat tails come from Listing 27.4's chi-squared(4) scale mixture, with moves rounded to grids of 1/64, \$0.01 and 0.05 bp. This extends Listing 27.4 from two hedges to three. The zero-miss count is the triangle inequality at work, not luck: it holds draw by draw, whatever the covariance.

**The trap:** Pasting the three one-hedge betas into one row (1.05, 1.30, $-0.180$). That counts rates twice (TY and LQD) and credit twice (LQD and CDX): a 1 bp rally reads as 0.185 points instead of 0.068, and a 1 bp IG widening as $-0.232$ instead of $-0.116$. The cheap rule built on that row pulls in 95% of stress windows, and its joint rule still misses about one true pull in a thousand windows, because it weighs offsetting moves wrongly. The safety theorem protects you relative to the $\boldsymbol\beta$ you wrote down, not relative to the bond.

**If you got this wrong, read:** §27.6.1 (the trigger table, the "two detours" box, the theorem and the paragraph on allocating the budget); Listing 27.4 in Appendix F, which this exercise extends; Chapter 8 for the empirical rate beta and the DV01 ratios.

**Z.27.3: The J.Crew drop-down as rows**

**Answer:** The rows are below. A backtest of Chapter 25's covenant-flag signal must use the knowledge-time snapshot at its decision time, $Q(k, a;\ t^{v} \le t,\ t^{k} = t)$, and must read the parser's output the same way. If the vendor's "point-in-time" file is valid-time only, it answers $Q(\cdot;\ t^{v} = t,\ t^{k} = \text{now})$. The IP then leaves the collateral on the transfer's effective date rather than when anyone outside the company knew, the signal fires before the 5 December 2016 disclosure, and the backtest trades the term loan at prices from before the market had read the filing. Every later correction leaks backwards too: a 2019 re-parse, or a `jcrew_blocker` field back-filled onto agreements signed before the move that named it, reads as if it had been known all along.

Notation: $t_0$ is the date the desk onboarded the loan, $t_x$ the transfer's effective date as the filing states it (on or before 2016-12-05), and $k_1$ = 2016-12-05 18:00, when the desk's event feed confirmed it *($t_0$ and the 18:00 are illustrative; keys are internal surrogates)*. ASSET-JC-USIP is the interest in the US marks that the 2017 notes were later secured on (72.04%, per Chapter 13).

| Key | Attribute | Value | Valid from | Valid to | Known from | Known to |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| ASSET-JC-USIP | owner | ENT-JC-LOANPARTY | $t_0$ | ∞ | $t_0$ | $k_1$ |
| ASSET-JC-USIP | owner | ENT-JC-LOANPARTY | $t_0$ | $t_x$ | $k_1$ | ∞ |
| ASSET-JC-USIP | owner | ENT-JC-DOMBRAND | $t_x$ | ∞ | $k_1$ | ∞ |
| INS-JC-TL | collateral | all assets incl. ASSET-JC-USIP | $t_0$ | ∞ | $t_0$ | $k_1$ |
| INS-JC-TL | collateral | all assets incl. ASSET-JC-USIP | $t_0$ | $t_x$ | $k_1$ | ∞ |
| INS-JC-TL | collateral | all assets excl. ASSET-JC-USIP | $t_x$ | ∞ | $k_1$ | ∞ |
| ENT-JC-DOMBRAND | parent | ENT-JC-NGRS (non-guarantor restricted sub) | $t_x$ | ∞ | $k_1$ | ∞ |
| ENT-JC-DOMBRAND | obligor_role | unrestricted; not a guarantor or grantor of INS-JC-TL | $t_x$ | ∞ | $k_1$ | ∞ |
| EVT-JC-2016-12 | event | drop_down: ASSET-JC-USIP to ENT-JC-DOMBRAND; INS-JC-TL collateral reduced; source: company filing, 2016-12-05 | $t_x$ | n/a | $k_1$ | ∞ |

**How:** Follow the Serta pattern of §27.3.3. Rows the desk believed before $k_1$ are closed in knowledge time at $k_1$, never edited, which is invariant (I2); the corrected history and the new facts all open at $k_1$, whatever their valid dates. The guarantor map is the dated graph of §27.3.1: the new box ENT-JC-DOMBRAND gets a dated arrow to its parent and a role outside the obligor group, so the question "is the IP inside the term lenders' collateral?" has two dated answers. If the filing dates the two hops separately (loan party to the non-guarantor restricted subsidiary, then on to the unrestricted one), each hop gets its own owner row and its own event row. The July 2017 exchange is a second event: it creates the 13% notes of J.Crew Brand, LLC and J.Crew Brand Corp. with their own collateral row, and retires part of the PIK notes. For the backtest, a decision at noon on 5 December sees the IP still with the loan party, even though $t^{v} \ge t_x$; a decision on the morning of 6 December sees it gone. Chapter 25's signal is built from the parsed capacity vector and the obligor map, so it inherits both knowledge times: the master's, and that of the parse it read.

**The trap:** Stamping the new rows "known from $t_x$" because that is when the transfer happened. That one choice turns the archive into the wiki: the drop-down looks known before it was disclosed, and the signal looks prescient for the same reason Theo's Serta backtest did. The other slip is to edit the old owner row's valid-to in place, which erases what the desk believed on 4 December.

**If you got this wrong, read:** §27.3.2 (the two invariants, the theorem and the corollary on valid-time-only "point-in-time" files); §27.3.3 (Serta as rows, and Mags's three questions); §27.3.1 for the dated obligor graph; Chapter 13's J.Crew Docket Diary for the facts; §25.9 on when a text signal is executable.

**Z.27.4: Your PM says "never false-alarm"**

**Answer:** As $c \to \infty$ the detection delay goes to infinity, linearly in $c$: $\text{ARL}_1 \approx 2(c + 1.166)/\delta - 2/\delta^2$. A switch that never false-alarms never alarms. Measured against the quiet time, though, the delay grows only with its log, $\text{ARL}_1 \approx \big(\ln(\mathcal{K}\,\text{ARL}_0) - 1\big)/\mathcal{K}$ with $\mathcal{K} = \delta^2/2$. For one false alarm a month at 200 fills a day, $\text{ARL}_0 = 21 \times 200 = 4{,}200$ fills. With $\delta = 0.75$ (allowance $\delta/2 = 0.375$) that needs $c = 8.28$; round to 8.3, which gives $\text{ARL}_0 \approx 4{,}280$ fills (21.4 trading days) and $\text{ARL}_1 \approx 21.7$ bad fills, about a tenth of a day's flow. A 4,000-run simulation at $c = 8.28$ gives $\text{ARL}_0 \approx 4{,}260$ and $\text{ARL}_1 \approx 21.8$.

For the PM, in poker: "Never fold a hand that might have won" has exactly one strategy that obeys it, which is never to fold. You call every bet to the river, every hand, all night. At an honest table that costs nothing. At a table with a cheat you pay him off on every hand and find out when your stack is gone. Any rule that ever gets you up from the table will sometimes fold the best hand. Folding the best hand about once a month is the price of getting up after about twenty-two hands against a cheat, and setting the line higher buys very little: to fold a winner only once a year, you would sit through about thirty.

**How:** Siegmund's approximation from §27.7.2, with drift $\mp\delta/2$ and $b = c + 1.166$:

$$
\text{ARL}_0 = \frac{e^{\delta b} - \delta b - 1}{\delta^2/2}, \qquad \text{ARL}_1 = \frac{e^{-\delta b} + \delta b - 1}{\delta^2/2}.
$$

As $b \to \infty$, $e^{-\delta b} \to 0$ and $\text{ARL}_1$ is linear in $b$, while $\text{ARL}_0 \approx e^{\delta b}/\mathcal{K}$ grows exponentially; take logs and substitute to get the log form. For the calibration, solve $e^{0.75 b} - 0.75 b - 1 = 4{,}200 \times 0.28125 = 1{,}181$: $b = 9.44$, so $c = 8.28$, and put $b$ back into $\text{ARL}_1$. `siegmund_arl` in Listing 27.5 does both with drifts $\pm 0.375$. One reading note for the PM: $\text{ARL}_0$ is an average. The wait for the first false alarm is roughly exponential, so a calm month passes with no false alarm only about 38% of the time (the simulation agrees); "one a month on average" is not "at most one in any month."

**The trap:** Leaving out the 1.166 shift and setting the line at $c = 9.44$. That doubles the quiet time (about 10,100 fills, fifty trading days) and costs three more bad fills ($\text{ARL}_1 \approx 24.7$), a different trade-off from the one the PM signed. The other slip is to keep the $\delta = 1$ allowance of 0.5: healthy fills then drift at $-0.5$ and bad ones at only $+0.25$, the line comes out at 6.5, and the delay is 22.8 fills from a test tuned for the wrong deterioration.

**If you got this wrong, read:** §27.7.2 (the box, then the Full Derivation and "tripling the quiet time costs two fills of delay"); the end of the Knight replay in §27.7.3, where Ines explains why the line is not set at two; Tomasz's eleven percent in §27.8.

**Z.27.5: ROBO and the zero-pick-off mandate**

**Answer:** ROBO builds a desk that never shows a firm price, or shows one so wide or for so short a time that nothing ever fills. It meets the spec exactly, because the expected pick-off loss of a quote that is never live is zero. Every term of §27.6.2 vanishes: the diffusion loss at zero exposure, and the jump loss with $\pi = 0$. A spec that makes "quote nothing" a failure, with every number illustrative and owned by the desk head:

- *Objective.* Maximise expected net capture per day, in dollars: over all fills, the half-spread earned minus the 60-second adverse markout, times face over 100.
- *Definition.* A pick-off is a fill whose 60-second markout against hedge-implied fair value is worse than $-h_i$ points; its loss is $(|\text{markout}| - h_i) \times \text{face}/100$.
- *Loss budget.* Pick-off losses no more than \$25,000 per trading day, with Tier 1's CUSUM on markouts ($\delta$ and $c$ in config, $\text{ARL}_0$ and $\text{ARL}_1$ logged) as the intraday early warning.
- *Presence floor.* Two-way quotes of at least \$1mm a side, live on at least 90% of the streaming list for at least 80% of the *eligible* seconds of the session, with each half-spread no wider than the desk's stated cap for its liquidity bucket.
- *Boundary conditions.* A second is excused from the floor only if (a) a trigger row has pulled the quote and the slow path has not yet re-armed it; (b) a Tier-2 condition holds (hedge heartbeat gap over 400 ms, clock fault, version skew, venue down); (c) realised hedge volatility over the last $N$ seconds is above the re-arm gate; or (d) it falls inside a declared event window (FOMC, CPI). Any other second without a quote counts against the floor, and five minutes below it while healthy pages the owner.
- *Eligibility.* Stream only bonds whose half-spread is at least twice the typical hedge-implied jump over one refresh, $h_i \ge 2\,\mathbb{E}|J_i|$; the rest are RFQ-only.

Now "quote nothing" breaks the floor and "quote everything, always" breaks the budget, so the optimum is interior: show the quote when a second of exposure earns more expected capture than the budget's shadow price times its expected pick-off loss.

**How:** §27.6.2 prices the two ways a live quote loses: the diffusion loss $\sigma\sqrt{\Delta}\,[\varphi(x) - x\,\Phi(-x)]$ with $x = h/(\sigma\sqrt{\Delta})$, and the jump loss $\pi\,(|J_i| - h_i)^{+}$. Both go to zero as $\Delta \to 0$ (never shown), as $h \to \infty$ (never hit) or as $\pi \to 0$ (always pulled first). A spec that is only a loss constraint has all of these as optima, and the cheapest one to build is the one that never shows a price: ROBO's eleven seconds of quoting in §27.6, taken to its limit. Units are what make a spec checkable: dollars per day for the budget, points and seconds for the definition of a pick-off, and a list of excused silences for the floor. For scale, with the cold-open numbers a jump pick-off on \$3mm costs about \$5,500, so a \$25,000 day is four or five cold-open hands, and the CUSUM should trip on a sustained problem well before the budget is gone.

**The trap:** Adding the loss budget but no floor or objective. "Expected pick-off loss at most \$25,000 a day" is still met by quoting nothing, so ROBO still quotes nothing. A budget limits the downside. Only the objective or the presence floor makes the desk turn up.

**If you got this wrong, read:** §27.6.2 (both regimes and the Full Derivation); the ROBO paragraph that opens the trigger-table spec at the end of §27.6.3; §27.7.1 for the tiers that own the boundary conditions; §27.5.3 for why a silent hedge feed is an excused second, not a quiet one.

**Z.27.6: Kaz wants the callable-bond OAS model on the FPGA**

**Answer:** One paragraph, for example:

> *To Kaz, cc Ines. Re: callable OAS on the FPGA. Declined, with an alternative.* The FPGA earns its place by doing one fixed thing in nanoseconds: it compares hedge moves with numbers the slow path wrote into a row. The table is data and the logic is fixed. An OAS model is logic, not data: a rate lattice whose size depends on each bond's call schedule, calibrated every day to a volatility surface. Every change to it would mean re-synthesising the design, hours of build and a change-control meeting, for a comparator we synthesise once a quarter and test like a bridge. We would either re-synthesise weekly or run a model weeks out of calibration, and both are worse than the slow path we have. Nor can the linear row stand in for the model on these bonds. Our 0.01-point guard band covers Veronesi's second-order term $\tfrac12 C P (\Delta r)^2$ for a bullet (about 0.004 points at $C = 80$, $P = 95$ and 10 bp), but a callable near its call price has negative convexity that swings as the call moves in and out of the money: at $C = -300$ and $P = 101$ *(illustrative)*, the same 10 bp move gives 0.015 points, more than the whole band, and our own trigger-table spec already says not to use the rule for callables. So callables stay on the slow path. Where the flow justifies streaming them, we quote from the slow path at a wider $h$, one that covers that convexity error plus the typical hedge jump over a refresh, and the FPGA keeps a conservative row that pulls them on a small TY move, because saying no needs no model. The rest stay RFQ-only. If that flow is worth more, the case is for a faster slow path, not a cleverer fast one.

**How:** Each of the three citations rules out a different version of the request. The *convexity term* says the linear row the FPGA can hold is wrong by more than its guard band on exactly these bonds, $\tfrac12 \times 300 \times 101 \times (0.001)^2 = 0.015 > 0.01$, against $\tfrac12 \times 80 \times 95 \times (0.001)^2 = 0.004$ for a bullet. The *re-synthesis cycle* says the model cannot live in the fabric either, because its logic and calibration change faster than fixed logic can follow. And *"the table is data, the logic is fixed"* says what the fast path is for: pull-only comparisons against numbers the slow path computed. A pull is always safe, so the FPGA can still say no to a callable; what it cannot do is price one.

**The trap:** Arguing from speed ("the FPGA can't run a lattice fast enough"). With enough engineering it might, and Kaz will say so. The reasons that hold are change and error: the model changes too often to live in fixed logic, and the cheap linear substitute is wrong by more than the guard band. The second slip is to offer callables at the bullet's $h$ "because the slow path prices them correctly": it priced them correctly when it wrote the row, and nothing on the fast path can correct the price as rates move.

**If you got this wrong, read:** the opening of §27.6 (what an FPGA is good and bad at, and "the table is data and the logic is fixed"); the guard-band paragraph and the Veronesi extraction in §27.6.1; the usage note under Listing 27.4 ("Do not use them for callables or distressed paper").

**Z.27.7: PB-01 with one leg missing**

**Answer:** The pod now carries a net market-value DTS of $+72{,}576$ (about $+72{,}600$), all of it the Kestrel long, where the matched pair carried $+972$. Its CS01 is \$20,736 per basis point of Kestrel spread. An overnight 10% proportional widening takes Kestrel from 350 to 385 bp and costs about \$726,000 (\$725,760), against about \$9,700 had both legs filled. The tier that should have caught it is **Tier 0**, a hard limit applied at the parent's scope, not Tier 1. The hedge, assuming a CDX HY spread duration of 3.9 and an index spread of 350 bp *(illustrative)*, is to buy about \$53mm of protection, whose CS01 is also about \$20,700 per bp. What the hedge leaves is Kestrel against the whole high-yield index: Kestrel's own default and documents, and the building-products factor that the Halvorsen short used to offset, plus the single-name-against-index basis and the roll. That is a hedged outright long, not a pair.

The residual-risk event the parent should emit, field by field:

- `event_type` RESIDUAL_RISK; `parent_id` the PB-01 parent order; `parent_state` PARTIAL.
- `children`: the Kestrel buy, \$60mm at 96, FILLED; the Halvorsen borrow-and-sell, \$39mm at 90, EXPIRED, filled 0, `reason` LOCATE_EMPTY.
- `event_time` 16:58:00 from the prime broker's locate response, and `known_at` when the desk's store committed it.
- `residual`: Kestrel's surrogate key, long \$60mm face, \$57.6mm market value, DTS $+72{,}576$ against a target of $+972$, CS01 \$20,736/bp, a 10%-wider stress loss of \$725,760, and the long's rate DV01, which a CDX hedge does not touch.
- `per_account`: the residual split by the allocation rule written before the order left.
- `strategy`, `trader`, `desk`: Dov's pod, PB-01; `owner` and `deadline`: an alert within 5 seconds, a hedge or unwind decision inside one quote-clock cycle.
- `action`: re-invoke the optimiser with the Halvorsen fill probability marked down, `proposed_hedge` buy \$53mm CDX HY protection, and `thesis_flag` PAIR_BROKEN.

**How:** DTS is face × price/100 × spread duration × spread in bp. Kestrel: $60 \times 0.96 \times 3.6 \times 350 = 72{,}576$. Halvorsen: $39 \times 0.90 \times 3.4 \times 600 = 71{,}604$, now zero. CS01 is market value × spread duration × 1 bp, $57.6\text{mm} \times 3.6 \times 10^{-4} = \$20{,}736$. Under DTS's rule one unit of market-value DTS is worth \$1 per 1% proportional move in spreads, so a 10% widening costs $10 \times 72{,}576 = \$725{,}760$, the same as 35 bp times the CS01. *The tier:* the EXPIRED report is one message that moves the pod's net DTS from about $+1{,}000$ to about $+72{,}600$ through a pre-set bound (the pod's net-beta limit). One message, one bound, no statistics: that is Tier 0. Better still, the same check runs before routing, on the parent's worst case (one child filled, the other not), so no long child leaves ahead of a confirmed locate. *Not Tier 1,* because Tier 1 accumulates noisy evidence over many fills and pays for its quiet with a delay of ten to twenty bad fills; here there is no noise to average, since the state machine knew at 4:58 with certainty, and Kestrel's fill has a perfectly good markout, so a markout CUSUM would never fire at all. *The hedge:* match DTS, $N \times 3.9 \times 350 = 72{,}576$, so $N = \$53.2$mm. Because the assumed index spread equals Kestrel's 350 bp, the DTS match is also a CS01 match: $53.2\text{mm} \times 3.9 \times 10^{-4} = \$20{,}736$. The assumption is consistent with Chapter 8-C, where the pod sold about \$13mm of CDX HY protection against 17,700 of DTS, about 1,360 per \$mm.

**The trap:** Reporting the pod as roughly flat (net DTS about $+1{,}000$) because the parent order is a matched pair. That is the OMS's view of intent, not of position, and it is exactly the quiet failure that the residual-risk event exists to prevent. Two smaller slips: naming Tier 1 because the tier table lists "child-to-parent ratio tests" there (those catch too many children, as at Knight, not one that never filled), and *selling* CDX HY protection. The surviving leg is long credit, so the hedge buys protection.

**If you got this wrong, read:** §27.4.2 (the state table, "every non-`FILLED` terminal emits a residual-risk event", and The Pair, PB-01); §27.7.1 (the tiers, and authority); Chapter 1-B's DTS box for the ruler; Chapter 8-C for how the pod sized its last CDX HY trade.

## Part VIII: The Portfolio Manager's Playbook

### Z.28 Chapter 28: What a Desk Head / Senior PM Must Know to Extract Maximum Alpha

Five exercises, one per clause of Theo's term sheet: the band, the sizing, the runway, the error bars on the band, and the stop. Every number below was recomputed in Python from the chapter's inputs and Listings 28.3 to 28.6 (Appendix F). Write your card before you read ours.

**Z.28.1: The empty band**

**Answer:** At $r_{\min} = 5\%$ and the 2008 multiple ($m = 5.8$), the band has room only if $\overline{\text{LCS}} \le 0.33\%$ (exactly 0.329%; at that point floor and ceiling meet at 3.16). At the March 2020 multiple ($m = 3$) the limit would be 0.79%. With no liquidity charge, and the per-bet IR held at $2/\sqrt{40} = 0.316$, the band opens at $N_{\text{eff}} = 25.6$, where $\text{SR} = 1.6$. Adding names cannot rescue a band that liquidity has closed. With SR rising like $\sqrt{N_{\text{eff}}}$, the floor stays at 3.16 however many names you add, and the ceiling can only climb toward the speed limit $2\,\text{DD}_{\max}/((m-1)\overline{\text{LCS}})$. At $\overline{\text{LCS}} = 0.8\%$ that limit is 3.91, so on paper the band reopens. It does so only at $N_{\text{eff}} \approx 97$ with $\text{SR} \approx 3.1$, which is the $1/\rho_a = 100$ breadth ceiling of §28.2. Above $\overline{\text{LCS}} = 0.99\%$ the speed limit sits below the floor, and no number of names reopens the band.

**How:** Write the ceiling (28.23) as $G_{\max} = \text{DD}_{\max}/(c_1 + 1/A)$, with $1/A = \sigma_{\text{DTS}}(\kappa z_p - \text{SR})/\sqrt{N_{\text{eff}}}$ and $c_1 = \tfrac12(m-1)\overline{\text{LCS}}$. The floor is $F = \sqrt{N_{\text{eff}}}\,r_{\min}/(\sigma_{\text{DTS}}\text{SR})$. The band exists if and only if $c_1 \le \text{DD}_{\max}/F - 1/A$:

$$
c_1 \le \frac{\sigma_{\text{DTS}}}{\sqrt{N_{\text{eff}}}}\left[\frac{\text{DD}_{\max}\,\text{SR}}{r_{\min}} - (\kappa z_p - \text{SR})\right] = 0.00791\,(3 - 2) = 0.79\%,
$$

so $\overline{\text{LCS}} \le 0.79\%/2.4 = 0.33\%$. For the second part, set $\text{SR} = \text{IR}_b\sqrt{N}$. The floor becomes $r_{\min}/(\sigma_{\text{DTS}}\text{IR}_b) = 3.16$, with no $N$ left in it, so it is the side that does not move. The dry ceiling $\sqrt{N}\,\text{DD}_{\max}/(\sigma_{\text{DTS}}(\kappa z_p - \text{IR}_b\sqrt N))$ rises with $N$ and reaches the floor when $\text{SR} = r_{\min}\kappa z_p/(\text{DD}_{\max} + r_{\min}) = 0.2/0.125 = 1.6$, which is $N = (1.6/0.316)^2 = 25.6$. With the liquidity charge, $G_{\max} < \text{DD}_{\max}/c_1$ for every positive $1/A$. Breadth can only push the ceiling toward that limit, and getting there needs $\text{SR} \to \kappa z_p$ (here at $N_{\text{eff}} = 160$, beyond any breadth a 1% residual correlation allows).

**The trap:** Holding SR fixed at 2 while you add names. Then the floor and the dry ceiling both scale with $\sqrt{N}$, their ratio stays at $r_{\min}(\kappa z_p - \text{SR})/(\text{DD}_{\max}\text{SR}) = 2/3$, and you conclude that breadth makes no difference, or, reading only the floor, that breadth hurts. The second trap is treating the reopening at $N_{\text{eff}} \approx 97$ as a lever. It needs a Sharpe of 3.1 and every bet the residual correlation will allow. In practice a closed band gets reopened by cutting the cost of leaving, not by adding bonds.

**If you got this wrong, read:** §28.7, the *ceiling that moves when you lean on it* box, the band's Full Derivation and Theo's four levers; §28.2 for the $1/\rho_a$ ceiling; and `leverage_floor` and `leverage_ceiling` in Listing 28.6 (Appendix F).

**Z.28.2: Kaz's 93%, re-audited**

**Answer:** There are three numbers. (1) $\lambda^{\mathbb{Q}} = 0.045/0.6 = 7.5\%$, and (28.11) gives $f^\ast = 1/0.6 - 0.075/0.045 = 1.667 - 1.667 = 0$. A quarterly-premium bootstrap at a 4% rate gives 7.46% and $f^\ast = 0.008$, which is convention noise, not edge. (2) Under $\lambda^{\mathbb{P}} = 1.5\%$, $f^\ast = 1.667 - 0.333 = 1.33$ of NAV (1.31 with $\sigma = 5\%$). That is inside the average-loss boundary $1/0.6 = 1.67$. (3) Set $L = L_{\max}U$ with $L_{\max} = 1$ and $U \sim \text{Beta}(3, 2)$, Listing 28.3's shape with mean loss 0.6. Then $f^\ast = 1.00$: Kelly runs straight to the ruin boundary the documents imply, $1/L_{\max} = 1.0$. Defend the third number, and only after (28.13) halves it, to about 0.50 of NAV, with the cluster cap applied after that. The number belongs to Sunita. $L_{\max}$ and the shape of the recovery distribution are hers (§28.8: analysts own $L$ and $L_{\max}$), and they are what moved it. $\lambda^{\mathbb{P}}$ belongs to Kaz, and the desk head signs.

**How:** With a flat hazard and continuous premium, $s = \lambda^{\mathbb{Q}}L$ exactly. Since the bond's carry equals the CDS spread (zero basis), $f^\ast = 1/L - s/(Lc) = 0$. Under $\mathbb{P}$ the edge is $c - \lambda L = 4.5\% - 0.9\% = 3.6\%$ a year, so 80% of the spread is risk premium. Now put number (2) through the uptier: at $L = 1$ it loses 133% of NAV, which is past ruin. For random $L$ the first-order condition is $c = \lambda\,\mathbb{E}[L/(1 - fL)]$. At $f = 1/L_{\max}$ with $U \sim \text{Beta}(a, b)$, $\mathbb{E}[U/(1-U)] = a/(b-1)$, so

$$
\lambda\,\frac{a}{b-1} = 0.015 \times \frac{3}{1} = 0.045 = c,
$$

and the condition holds exactly at the cliff. The shape decides the answer. A mean-0.6 Beta with $b < 2$ puts enough weight near total loss to pull $f^\ast$ inside the cliff ($\text{Beta}(1.5, 1)$ gives 0.95). With $b \ge 2$, $f^\ast$ is pinned at 1.0. A Kelly fraction sitting on its cap tells you the model's tail is thinner than the documents' tail, and that is why the half is not optional here.

**The trap:** Defending 1.33 because it is "inside the ruin boundary of 1.67". That boundary is $1/\mathbb{E}[L]$. The credit agreement moved the worst case to $L = 1$, and there 1.33 is a 133% loss. The zero under $\mathbb{Q}$ tempts the other mistake: "fixing" it with a physical hazard while keeping the agency's average $L$, which is how Kaz got to 93% in the first place.

**If you got this wrong, read:** §28.4, the *P and Q* box and "Which measure, and which loss" (random $L$, and the ruin boundary set by the worst recovery); "Fractional Kelly is full Kelly for people with standard errors" for (28.13); Theo's card in the 2026 CCC case study; §28.8 for who owns which input; and `kelly_random_loss` in Listing 28.3 (Appendix F).

**Z.28.3: Your fund is the borrower**

**Answer:** Base case: $(150 + 0.97 \times 400)/(10 + 25) = 538/35 = 15.4$ weeks. Stressed: the haircut becomes $3\% \times 5.8 = 17.4\%$, so the sleeve raises \$330.4mm and the weekly burn is \$45mm, giving $480.4/45 = 10.7$ weeks. That is under 13, so by Theo's standard the fund is a going-concern question: the first-day-of-engagement conversation, not a strategy meeting. Most of the damage comes from the margin side. Doubling the margin alone takes the runway to 12.0 weeks; the 2008 haircut alone leaves it at 13.7. At the stressed haircut, 13 weeks of runway allows a burn of no more than \$37mm a week.

**How:** Block 4's runway is (cash + $(1-h)\times$ liquid sleeve) / weekly burn, and the burn is margin calls plus redemptions. The stress hits both sides at once. The denominator rises 29% (\$35mm to \$45mm) and the numerator falls 11% (\$538mm to \$480mm). Using the exact 2007–08 ratio $3.40/0.59 = 5.76$ instead of 5.8 gives a 17.3% haircut and the same 10.7 weeks. Cash alone covers 4.3 weeks in the base case and 3.3 in stress. Everything after that depends on selling a \$400mm sleeve in the very weeks its bid has moved 5.8 times. That is Third Avenue's gap between the runway clock and the days-to-liquidate clock, and the formula hides a second assumption: that the whole sleeve converts to cash at once. Run (28.17) on the sleeve before you believe even the 10.7.

**The trap:** Dividing by redemptions alone, $538/25 = 21.5$ weeks, and calling the fund comfortable. The margin calls are this borrower's debt service, and they are the part of the burn that doubles in stress. Smaller slips: leaving out the haircut ($550/35 = 15.7$), or applying the 5.8 to the margin calls as well as the sleeve, which counts one stress twice.

**If you got this wrong, read:** §28.5, the Third Avenue case study (folder one, then Ines's four clocks after the card); `runway_weeks` and `days_to_liquidate` in Listing 28.4 (Appendix F); and the Runway row of the §28.9 dashboard.

**Z.28.4: Mags's adjusted number**

**Answer:** The three estimates are $\text{SR}$, $\kappa z_p$ and $N_{\text{eff}}$. Everything else in (28.22) is either policy ($\text{DD}_{\max}$, $r_{\min}$), read off quotes ($\overline{\text{LCS}}$), or a named scenario ($m$).

- $\text{SR} = 2 \pm 0.58$: three years under §28.9's $1/\sqrt{Y}$ rule. Lo's correction at a Sharpe of 2 widens this to $\pm 1.0$.
- $\kappa z_p = 4 \pm 1$: nobody has measured $\kappa$, and Paleologo's own range for $-\kappa F^{-1}$ runs from 4 to 6.
- $N_{\text{eff}} = 40 \pm 8$: a residual correlation of $\rho_a = 0.010 \pm 0.005$ maps to 33–49, and Marcus's dashboard went from 41 to 27 to 33 in one night.

Take Theo's reopened band ($\overline{\text{LCS}} = 0.4\%$, $r_{\min} = 4\%$), which runs from 2.53 to 2.95. The ceiling's standard error in logs is 0.36. One standard error each way gives 2.1 to 4.3, and a simulation gives a 90% interval of 1.8 to 5.7. In 4% of the draws $\kappa z_p \le \text{SR}$, and then there is no ceiling at all. The floor's 90% interval is 1.65 to 4.9. The band is 0.42 turns wide, and its uncertainty is about ten times that. The probability that it is empty is about 41%. With SR one standard error lower it is certainly empty: the floor is 3.56 and the ceiling 2.50. So it is not a band. It is a probability, and the dashboard's Skill row is right to show it again at one standard error lower.

**How:** Write the ceiling as $G_{\max} = \text{DD}_{\max}/\big(c_1 + (\kappa z_p - \text{SR})\,\sigma_{\text{DTS}}/\sqrt{N_{\text{eff}}}\big)$ and apply the delta method to its log:

$$
\text{se}(\ln G_{\max}) = \frac{\sigma_{\text{DTS}}/\sqrt{N_{\text{eff}}}}{c_1 + (\kappa z_p - \text{SR})\,\sigma_{\text{DTS}}/\sqrt{N_{\text{eff}}}}\sqrt{\text{se}_{\text{SR}}^2 + \text{se}_{\kappa z}^2 + \left(\frac{(\kappa z_p - \text{SR})\,\text{se}_{N}}{2N_{\text{eff}}}\right)^2} = 0.311 \times 1.17 = 0.365 .
$$

Taken one at a time, $\kappa z_p$ contributes 0.31 of that, SR 0.18 and $N_{\text{eff}}$ 0.06. The input nobody has measured carries most of the error. For the floor, $\text{se}(\ln F) = \sqrt{(\text{se}_N/2N_{\text{eff}})^2 + (\text{se}_{\text{SR}}/\text{SR})^2} = 0.31$. The floor and the ceiling share SR with opposite signs, so their intervals are not independent. That is why the empty-band probability comes from a joint simulation: two million independent normal draws of the three inputs, keeping only the draws with $\kappa z_p > \text{SR}$. The right tail of the ceiling is bounded by the speed limit, 7.8.

**The trap:** Naming $\text{DD}_{\max}$, $r_{\min}$ or the LCS. The first two are decisions the desk makes, so an "error" in them is a choice, and the LCS is read off the screen. The subtler trap is to put error bars on the floor and the ceiling separately and report that "the intervals overlap but the point estimates don't". The number that matters is $\Pr(\text{floor} > \text{ceiling})$. A lower SR raises the floor and lowers the ceiling at the same time, so the band empties faster than either interval suggests.

**If you got this wrong, read:** §28.7, Kaz on $\kappa$ and the Paleologo extraction that follows; §28.9's Skill row and the paragraph after the dashboard on SR as a pair; *The Map, Not the Territory* in §28.2 for $N_{\text{eff}}$ as a model output; and §7.8 for the standard error of a Sharpe ratio.

**Z.28.5: ROBO and the stop-loss**

**Answer:** Over a one-year allocation, the book with no rule earns 6.00%. Paleologo's two-threshold rule earns 5.53% (expected capital-time 0.922). ROBO earns 5.08% (expected capital-time 0.846). ROBO's rule costs **46 bp a year**, or 40 bp in Listing 28.5's daily-monitored Student-t(6) setup, and it doubles the price of safety from 7.8% to 15.4% of expected P&L. What it buys is small: the chance of a 7.5% loss within the year falls from 0.65% to zero. Over a career the gap is larger, because ROBO never restarts. It ends the PM's capital with probability $e^{-1.25} = 29\%$, against $e^{-3.75} = 2.4\%$ under the two-threshold rule. The spec sentence: *"The stop-loss is the platform's survival constraint, not the book's objective. Implement the two-threshold rule exactly: halve allocated capital at a loss of $x/2$ and liquidate at $x$, both measured on initial allocated capital. Never cut earlier, deeper or for longer than the rule says, and submit any proposed change with its price of safety, $\mu$ times the expected capital-time it removes."*

**How:** Capital $c_t$ is set from past P&L, and $\mathbb{E}[dX_t \mid \text{past}] = \mu\,dt$, so $\mathbb{E}[\text{P\&L}] = \mu\,\mathbb{E}\big[\int_0^T c_t\,dt\big]$. The two rules are identical until the first touch of $-3.75\%$, which happens in 23.7% of years by (28.19). After that, Paleologo's rule keeps half the capital until the underlying return falls a further 7.5%, because at half capital that is the next 3.75% of P&L. ROBO keeps none. So the whole difference is

$$
\Delta\,\mathbb{E}[\text{P\&L}] = \mu \cdot \tfrac12\,\mathbb{E}\big[(\tau_2 \wedge T) - (\tau_1 \wedge T)\big] = 0.06 \times 0.076 = 0.46\%,
$$

which you get by integrating the first-passage density of $\tau_1$ against $\int_0^{T-s}\big(1 - \Pr(\text{hit } 7.5\% \text{ by } u)\big)\,du$, with $\Pr(\text{hit})$ taken from (28.19). The lifetime figures use the limit of (28.19): ROBO is switched off for good the first time its line is touched, $e^{-2\mu(0.0375)/\sigma^2} = e^{-1.25}$. The two-threshold rule liquidates only if both legs are hit, $e^{-1.25}\,e^{-2.5} = e^{-3.75}$.

**The trap:** "ROBO's rule is safer and costs nothing, because it acts at the same 3.75% line." The first touch is where the two rules *start* to differ, and the whole cost lies in the capital-time after it. The deeper error is counting the "losses avoided" as a gain. Under the identity, a stop never changes the return earned per unit of capital-time. All it can do is remove capital-time, so for a PM with $\mu > 0$ it can only cost. As Paleologo puts it, stops exist for the firm's survival, not to improve performance.

**If you got this wrong, read:** §28.6, the Paleologo p.167 extraction and its annotation (the identity), "Setting the stop with drift" for (28.19) and (28.20), and `simulate_two_threshold` in Listing 28.5 (Appendix F), which this exercise reruns with ROBO's rule beside the platform's.
