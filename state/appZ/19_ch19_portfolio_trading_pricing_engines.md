## Chapter 19: Portfolio Trading & Basket Pricing Engines

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

<!-- STATUS: COMPLETE -->
