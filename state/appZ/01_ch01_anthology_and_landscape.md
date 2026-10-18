## Z.01 Chapter 1: The Anthology of the Desk & The Modern Quant Credit Landscape

Six exercises. Every number below was recomputed from the chapter's own inputs; where an input had to be assumed, the solution says so and labels it illustrative.

**Z.01.1: The ask, and where the two-sided quote is centred (Derivation)**

**Answer:** The ask for a client buying $\Delta q$ is

$$
A^{\text{res}} = m' + \tfrac12\gamma\sigma^2_{\text{IDO}}h\,(\Delta q - 2q).
$$

With $m' = m$ the midpoint is $\tfrac12(A^{\text{res}} + B^{\text{res}}) = m - \gamma\sigma^2_{\text{IDO}}h\,q = r^{\text{res}}$, and the width is $A^{\text{res}} - B^{\text{res}} = \gamma\sigma^2_{\text{IDO}}h\,\Delta q$, plus $2c$ if both sides pay the cost. On the cold open's inputs ($q = +5$, $\Delta q = 15$, $\gamma\sigma^2_{\text{IDO}}h = 0.0254$ points per \$mm, $\pi = 0$, $c = 0$), the quote is 91.65 bid and 92.03 offered, 0.38 wide, centred on 91.84, which is 0.127 below the 91.97 mid. If the buy-side RFQ has toxicity $\pi'$ (an informed buyer knows of an up-jump $J$), then $m' = S_t + \pi'J$ and the midpoint becomes $r^{\text{res}} + \tfrac12(\pi' - \pi)J$. Equal toxicity on both sides widens the quote by $2\pi J$ and leaves its centre where it was; unequal toxicity skews the centre toward the more dangerous side. Theo's Halvorsen seller ($\pi = 0.6$, $J = 13$) against an uninformed buy side pulls the centre 3.9 points below $r^{\text{res}}$, to 87.94.

**How:** Run §1.3.2's indifference argument with the trade reversed. Selling $\Delta q$ leaves the desk holding $q - \Delta q$ and $A\,\Delta q$ in cash, so

$$
(q-\Delta q)\,m' + A\,\Delta q - \tfrac12\gamma\sigma^2_{\text{IDO}}h\,(q-\Delta q)^2 = q\,m' - \tfrac12\gamma\sigma^2_{\text{IDO}}h\,q^2 .
$$

Cancel $q\,m'$, use $(q-\Delta q)^2 - q^2 = \Delta q\,(\Delta q - 2q)$, and divide by $\Delta q > 0$. Now average with (1.1). The block terms $\pm\tfrac12\gamma\sigma^2_{\text{IDO}}h\,\Delta q$ cancel, the two inventory terms $-\gamma\sigma^2_{\text{IDO}}h\,q$ are the same on both sides and survive, and a symmetric cost $c$ cancels too. For the toxic case, substitute $m = S_t - \pi J$ and $m' = S_t + \pi' J$ before averaging.

**The trap:** Writing the ask as the mirror image of the bid, $m + \tfrac12\gamma\sigma^2_{\text{IDO}}h\,(2q + \Delta q)$. That centres the quote on $m$ and throws away the inventory skew. A long desk is a keen seller: inventory pushes the ask *down* by exactly as much as it pushes the bid down, and that common shift is the Avellaneda–Stoikov reservation price. The quieter trap is assuming the buy side's $m'$ equals the sell side's $m$. It does only when the two RFQs are equally informative, and the chapter's whole point is that they rarely are.

**If you got this wrong, read:** §1.3.2 (the inventory term), then §1.3.3 for why $m$ is conditioned on the RFQ. Chapter 18 rebuilds the two-sided quote as Avellaneda–Stoikov.

**Z.01.2: Bayes, with a poker face**

**Answer:** $\pi \approx 0.36$ (posterior odds $0.557$). At $J = 13$, toxicity takes $\pi J \approx 4.65$ points off the bid. With the cold open's inventory and cost terms, the bid would be about 86.75, between Kaz's 91.40 and Theo's 83.60. Rather know the counterparty: knowing who is selling resolves $\pi$ to 0 or 1, while knowing $J$ only fine-tunes a charge you can already set correctly on average.

**How:** Work in odds, as in the §1.3.3 box. The prior odds are $0.03/0.97 = 0.0309$. Independent pieces of evidence multiply, so the combined likelihood ratio is $12 \times 1.5 = 18$, the posterior odds are $0.0309 \times 18 = 0.557$, and

$$
\pi = \frac{0.557}{1 + 0.557} = 0.358, \qquad \pi J = 0.358 \times 13 = 4.65 \text{ points}.
$$

In logit form this is $\operatorname{logit}\pi = \operatorname{logit}(0.03) + \ln 12 + \ln 1.5$, a two-feature logistic regression. Compare Theo's "call it $\pi = 0.6$": at a 3% prior that needs a likelihood ratio of about 48, so his gut priced the features about 2.7 times stronger than these estimates. On the poker question: the charge $\pi J$ is linear in $J$, so an unbiased estimate of $J$ already sets the expected charge correctly, and a 50% error in $J$ moves it by only $\pm 2.3$ points. Not knowing the type mis-prices *every* trade: an uninformed seller is overcharged by 4.65 points, and an informed one is undercharged by $13 - 4.65 = 8.35$. The type is also the thing you can learn, from Rule 2019 statements and from markouts bucketed by sender.

**The trap:** Multiplying the *probability* by the likelihood ratio: $0.03 \times 18 = 0.54$, so a charge of 7.02 points. Close behind it is forgetting to turn the odds back into a probability ($0.557 \times 13 = 7.24$ points). Both overcharge by about 2.5 points, enough to lose every uninformed seller in the name to a competitor. Bayes multiplies odds, and the answer has to go back through $\pi = \text{odds}/(1+\text{odds})$. Adding the ratios ($12 + 1.5$) is the third version of the mistake and gives 0.29.

**If you got this wrong, read:** §1.3.3, the Math, Gently box on Bayes in odds and the Poker Table box after the cold-open numbers. Chapter 3 builds the toxicity model.

**Z.01.3: DTS for a BBB, and for a CCC quoted at 68**

**Answer:** For the BBB, DTS works. If the bond is a par 10-year at 140 bp over a 4.2% Treasury *(illustrative)*, its spread duration is about 7.6, its DTS about 1,060 bp-years, and at $\sigma_{\text{rel}} = 8\%$ a month (1.3) gives about 85 bp of excess-return volatility, roughly 0.85% of price a month. For the CCC, DTS is meaningless. At 68 the bond is price-quoted, its "spread" depends on coupons nobody expects to be paid, and its price is anchored to recovery rather than to discounting. The single measure to use is risk **in percent of market value**, with two branches like LCS. A spread-quoted bond uses $\text{DTS}\cdot\sigma_{\text{rel}}$, converted from bp to percent of price. A price-quoted bond uses price-return volatility measured in price space and scaled by the distance to recovery, $(P - 100R)/P$, with jump-to-default $P - 100R$ as its hard limit. Both branches come out in the same units, so the two equal-weight positions can be added.

**How:** The BBB passes both tests in §1.4. Its spread is a real price of risk, and a spread move maps linearly into price: $r^{\text{xs}} \approx -D^{\text{spr}}\Delta s$ with $\Delta s = s\,\varepsilon$. Force the same calculation onto the CCC and it falls apart in three ways (8% coupon, 3.9% Treasury, all illustrative):

- **The spread depends on the promised coupons.** At 68 the "spread" is about 1,950 bp and the DTS about 4,650. Assume a 6% or a 10% coupon instead and the spread at the *same* price is 1,700 or 2,210 bp.
- **Maturity stops mattering, but DTS does not notice.** A 7-year bond of the same issuer at 68 has a "DTS" of about 5,590, yet in default both bonds receive the same recovery, because pari passu claims accelerate together.
- **The linear map breaks.** If the spread doubles, linear DTS says the price falls 31.6 points, and a full repricing says 24.1. With $R = 40\%$ the bond cannot lose more than the 28 points it stands above recovery.

LCS faced the same problem and solved it by quoting both branches as a percentage of price. Do the same for risk.

**The trap:** Backing a spread out of the price, computing a CCC "DTS" of about 4,600, and averaging it with the BBB's 1,060. The number you get is well formatted and means nothing, like row 3,112 in Theo's spreadsheet. Its size is set by an arbitrary coupon and maturity, and its linearity promises losses beyond the bond's distance to recovery. A milder version of the trap is Theo's: spread in percent rather than bp, which understates DTS a hundredfold.

**If you got this wrong, read:** §1.4, the derivation of (1.3), the annotation on Ben Dor p.112 (the two-branch LCS and "below 70"), and the paragraph on Theo's percent column. Part IV moves the risk into price-and-recovery space.

**Z.01.4: The Fed as a day-10 absorber (Flow graph)**

**Answer:** The drop does not change: it is still 5.12 points on day 0, because capacity that arrives on day 10 cannot cushion day 0. On day 10 the Fed's \$5bn takes the dealer residual from \$6.4bn to \$1.4bn, and the price jumps 2.43 points that day. The 60-day reversal rises only from 4.87 to 5.06 points, but it arrives much earlier: 4.44 points are back by day 10 instead of 2.01. The Fed's direct share of the reversal booked so far is 55% at day 10, 31% at day 20 and 4% at day 60. Who earned it? Mostly the central bank. Any P&L booked in the first three weeks was largely the Fed's own buying, and the slow decay that pays a patient desk the rest rests on a $\theta$ that assumes buyers keep arriving. In March 2020 the Fed is the reason they did. (Under the stress toggle the same run gives a 10.32-point drop, 7.9 left on dealers after day 10, and the same 2.43-point jump.)

**How:** Extend Listing 1.3 so that each absorber carries an arrival day, and give `run` a `day` argument that counts only the capacity that has arrived by then. On day 0 the total capacity is 6.5 against $Q^{\text{sell}} = 12.9$, so the residual is 6.4. From day 10 it is 11.5, every absorber fills completely, the Fed takes 5.0 and the residual is 1.4. Conservation holds on both runs. Make the stress toggle switch off the private absorbers only: a policy absorber is not state-dependent capacity. Then let the imbalance in (1.7) be a step function on the trigger's clock:

$$
p_t = p^* - \kappa\,\frac{I^+(t)}{\text{ADV}}\,e^{-\theta t}, \qquad I(t) = \begin{cases} 6.4, & t < 10 \\ 1.4, & t \ge 10 \end{cases}
$$

With $\kappa = 0.4$, ADV $= 0.5$ and $\theta = 1/20$: the dent is 5.12 on day 0 and $5.12e^{-0.5} = 3.11$ just before day 10, which falls to $1.12e^{-0.5} = 0.68$ on day 10 itself, and $1.12e^{-3} = 0.06$ remains on day 60. Restarting the decay clock on day 10 gives 5.03 instead of 5.06, and the conclusion is the same.

**The trap:** Putting the \$5bn into capacity on day 0. You then get a 1.12-point drop and a 1.06-point 60-day reversal, and conclude that the Fed *shrank* the trade. That run describes a different world, one where the absorber was there, or was credibly announced and priced, at the trigger. The dent never opens, and there is nothing for anyone to earn. The second trap is reading the in-model 96% share at day 60 as the desk's skill. The model hands the desk that share by assuming $\theta$; Ines's "IDO or it didn't happen" says strip the Fed and the beta first.

**If you got this wrong, read:** §1.8.1 (eqs. 1.6–1.7 and the half-life gloss), then Act 4 of §1.8.2 and "What happened, and the answer"; Listing 1.3 for the `run` you are extending.

