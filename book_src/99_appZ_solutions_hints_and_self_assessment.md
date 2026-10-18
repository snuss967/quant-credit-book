# Appendix Z: Solutions, Hints and the Gates

Every exercise in the book has its worked answer here. Each solution gives the number first, then
the method, then the trap most readers fall into, and ends with the section to reread if you missed
it. A solution states its measure (physical or risk-neutral) and its units whenever either could be
in doubt. Code appears only where the exercise asks you to build something, and then only as far as
the answer needs; the full listings live in Appendix F.

The appendix is arranged in book order, Part by Part. Where a Part has a gate, it comes after that
Part's chapters: a short self-assessment you can take before moving on, with the answers and the
sections to reread.

## Part I: The Cognitive Bridge & The State of Quant Credit

### Z.01 Chapter 1: The Anthology of the Desk & The Modern Quant Credit Landscape

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

**Z.01.5: ROBO literalism**

**Answer:** The vague spec: *"Using the RFQ history table, fit the toxicity model that best explains the desk's five-day markouts."* ROBO does exactly that. It uses every column, including the post-trade composite mid and the corrected prints that already contain the markout, adds issuer and date dummies until the in-sample fit is perfect, and reports a model that has memorised which names blew up in which weeks. The two clauses that prevent it:

1. *Validation.* "Report only out-of-fold performance, with folds grouped by ultimate parent (no parent on both sides) and split in time, purging every training RFQ whose label window overlaps the test span and embargoing for the longest feature lookback; nest all tuning inside the training folds." (Chapter 7, §7.7.)
2. *The label window.* "The label is the markout from the RFQ timestamp $t$ to $t + 5$ trading days, fixed before fitting; every feature must be computable from data as known at its arrival time strictly before $t$, so no column populated or corrected inside $(t, t+5]$ may enter the features, and the label horizon may not be tuned on the test folds."

**How:** Find the two ways a toxicity model can see the answer. The first is *across rows*. RFQs in one name in one week share one jump: Halvorsen's Friday RFQs all mark out at about $-13$. A shuffled fold therefore puts siblings of the test RFQ in training, and an issuer dummy "predicts" them perfectly. Grouping by parent closes that door, and the time split, purge and embargo close the market-wide version of it. The second is *within a row*. If any feature is measured after $t$, or the label window starts before the features stop, the label leaks into the inputs. Pinning the label to $[t, t+h]$ and the features to as-of data before $t$ closes it. That is the Quant-Shop Life lesson in §1.3.3: keep every print with the time it arrived.

**The trap:** "Use cross-validation" as the fix. Ordinary shuffled K-fold is the leak, not the cure: it passes the memorising model with flying colours, because every test fold contains the same events as training. A related trap is writing the label as "the markout" with no window. ROBO then picks whichever horizon fits best, which is one more parameter tuned on the answer.

**If you got this wrong, read:** §1.3.3 (the Quant-Shop Life box and "What ROBO built from the vague version"), then §7.4 (labels with recorded intervals) and §7.7 (purged, embargoed, issuer-grouped cross-validation).

**Z.01.6: Courtroom quant**

**Answer:** Define $x_{\text{NPR}} = 1$ if the credit agreement's pro rata sharing clause carves out borrower purchases with no "open market" qualifier and no requirement that the offer be open to all lenders (Mitel's bare "purchase"), and $x_{\text{NPR}} = 0$ otherwise. It belongs in **both**, but in different roles. In $J$ it is a main effect, because the document sets how far left-behind paper can fall once a majority deal is done. Serta's remand numbers price that fall at about 29 points of par: \$261.13mm of damages on \$895mm of excluded loans, on top of the 25 cents those lenders kept. In $\pi$ it enters only through the prior and as an interaction. It raises the base rate $\mu$ of informed selling, and it scales up the likelihood ratios of sender features such as lender-group membership and minutes since the call. It never enters as a standalone sender likelihood ratio, because a public document is identical for every seller and cannot tell you who is selling.

**How:** Split the bid's third term the way §1.3.3 does. $J$ is about the *bond*: what the informed seller knows the price is going to. A document that lets a bare majority prime the minority widens the distribution of $J$ and raises the chance that a jump is coming at all. $\pi$ is about the *sender*. The document makes information more valuable, so more of the people who hold it will be selling, which is why it moves $\mu$. It also makes "was on the call" a bigger tell, which is the interaction:

$$
\operatorname{logit}\pi = \operatorname{logit}\mu(x_{\text{NPR}}) + \theta_1 g + \theta_2\,g\,x_{\text{NPR}} + \dots,
$$

with $g$ the lender-group indicator. Mags's two June 2020 sellers share the same document and should still get bids several points apart; only the sender terms can do that. One more caution: the public, probability-weighted part of the document risk is already in $S_t$. Counting it a third time, as a sender feature, is the double-conditioning the spec forbids. As a scale for the stakes, the 9% New York prejudgment interest (simple) adds about \$142mm to the \$261.13mm over the six years to July 2026, about \$403mm in all.

**The trap:** Treating $x_{\text{NPR}}$ as a sender feature, "toxic document, toxic seller". That charges the CLO the same as the lender-group regular, which is the mistake the decision point in §1.9.1 exists to prevent. The subtler trap is believing the binary feature would have caught Serta. It would have scored Serta 0: Serta's agreement *had* an open-market qualifier, merely an undefined one, and the uptier closed anyway, was upheld in 2023 and was reversed only on 31 December 2024. Mitel, scored 1, was upheld, and Wesco's multistep route was blessed in 2025. The feature's coefficient is a function of the court and the date. Ship it with a "qualifier present but undefined" level and a ruling-regime interaction, or it will be confidently wrong about the one case it is named after.

**If you got this wrong, read:** §1.9.1 (the Docket Diary, the two-sellers decision point and the 2023–2026 coda) and §1.3.3 on what $\pi$ and $J$ each condition on. Chapter 13 builds the Priming Risk Score, and Chapter 25 scrapes the clauses.

### Z.02 Chapter 2: The Revolutions in Credit Trading

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

### Z.03 Chapter 3: Cognitive Rewiring, From PJT RSSG to Systematic Desk Head

Six exercises, one for each tool in the chapter's engine. Every number below was recomputed from the chapter's equations, and the code-facing ones from Blocks 2, 4 and 6 run on their own seed (Appendix F, Listings 3.2, 3.4 and 3.6). Write your answer down before you read ours; the gap is your markout.

**Z.03.1: Moyer's footnote, with a clock**

**Answer:** (a) Both models price at 85: $0.625(100) + 0.375(60) = 85$ and $0.50(100) + 0.25(80) + 0.25(60) = 85$. Their standard deviations are 19.36 points (A) and 16.58 points (B). (b) For Model A at $\pi = 0.1$, the exact charge is 1.92 points below the mid for a sell RFQ and 1.83 points above it for a buy RFQ, against a symmetric $\pi \times \text{sd} = 1.94$. (c) $\sigma_V(5) = 9.29$ points for A and 8.14 for B, so the bids are about 84.07 and 84.19. Choosing between the models moves the bid by 0.11 points. The horizon moves it by about a point, because pricing to resolution would give bids of 83.06 and 83.34.

**How:** In A the variance is $p(1-p)\Delta^2 = 0.625 \times 0.375 \times 40^2 = 375$. In B it is $0.5(15)^2 + 0.25(5)^2 + 0.25(25)^2 = 275$. Both models are point masses, so all of their variance is between-scenario. For (b), use the asymmetric Glosten–Milgrom formula with $q = 0.625$ and $\Delta = 40$. The buy side is the same formula with $q$ and $1-q$ swapped:

$$
m - b = \frac{\Delta\,q(1-q)\,\pi}{\tfrac{1-\pi}{2} + \pi(1-q)} = \frac{0.9375}{0.4875} = 1.923, \qquad
a - m = \frac{\Delta\,q(1-q)\,\pi}{\tfrac{1-\pi}{2} + \pi q} = \frac{0.9375}{0.5125} = 1.829 .
$$

The sell side is wider because informed sellers appear only in the bad state, and the bad state is the less likely one. A sell RFQ is therefore the bigger surprise and moves the posterior further than a buy, which points where the prior already leans. For (c), apply §3.1.3 to each model and set the bid at $85 - 0.1\,\sigma_V(5)$:

$$
\sigma_V^2(5) \approx \rho\,\operatorname{Var}_{\text{between}} + h\,\sigma_{\text{d}}^2 = 0.2 \times 375 + 5 \times 1.5^2 = 86.25 \;(\text{A}), \qquad 0.2 \times 275 + 11.25 = 66.25 \;(\text{B}).
$$

**The trap:** Pricing the five-day quote off the resolution-day standard deviation (19.36 or 16.58). That gives bids near 83.1 and 83.3, so the client is charged a full point for uncertainty that will not resolve while you hold the bond. In (b), the usual slip is to reuse the sell-side denominator for the buy and get 1.92 both ways. The numbers have a lesson for the banker: arguing about scenario probabilities is the right instinct for the case and the wrong one for the quote.

**If you got this wrong, read:** §3.1.1 (two-point variance), §3.1.2 (the law of total variance), §3.1.3 (the horizon), and in §3.2.1 "The Full Derivation: the Glosten–Milgrom bid" (the asymmetric version).

**Z.03.2: Switch off the winner's curse**

**Answer:** (a) Test A still passes, and so does Test B's first assertion (fills are 49% of the tape). The run stops at `assert mo_fill.mean() < -3 * se(mo_fill)`. On the seeded tape the fill markout is $-0.006$ points with a standard error of 0.005, which is about $-1.2$ standard errors, nowhere near $-3$. This is the correct failure. With $\rho = 0$, winning tells you nothing about the value, and Glosten–Milgrom at the true $\pi(x)$ breaks even on fills just as it does on the whole tape. A test that still passed with its effect switched off would be testing nothing. (b) A winner's curse needs a common value: a prize worth the same to every bidder, which each bidder estimates with error. A bond's post-trade value is the next mid, and that number is the same for every dealer, so it is almost purely common. (c) Cover prices let you test a *larger* shading on history but not a smaller one.

**How:** (a) In Listing 3.2 a rival's effective concession is `conc - eta * rho * sigma_v * u`. At $\rho = 0$ it is independent of $u$. Whether you win then depends on $h^{\text{GM}}(x)$ and on noise unrelated to the value, so

$$
\mathbb{E}[\text{MO} \mid \text{fill}, x] = \mathbb{E}[\text{MO} \mid x] = 0 .
$$

Your fills still lean toward low-$\pi$ RFQs, because a smaller half-spread wins more often. The lean costs nothing, because the GM quote breaks even at every $x$. (b) Under private values each bidder knows what the prize is worth to *it*, so winning reveals nothing. Under common values, winning means your estimate was the most optimistic one in the room. A dealer's private components (inventory, balance sheet, an axe) are small next to "where will this mark in five days?". (c) On a Done RFQ, an extra shading $\Delta$ still wins exactly when the shaded price still beats the cover. If it does, the markout improves by $\Delta$; if it does not, the RFQ drops out of the Done set. Replaying that over history evaluates any larger $w(n)$. A smaller $w(n)$ would also have won some RFQs you lost, and whether it beats the winner depends on the winning level. Losers rarely see that level: "Covered" tells you your rank, not your distance from the winner.

**The trap:** Saying that both Test B assertions fail. The second one, `mo_lost.mean() > mo_fill.mean()`, compares two means that are both zero in expectation, so it is a coin flip. On seed 3 it passes by less than one standard error. On seven other seeds we tried it failed twice. In the listing it never runs, because the assertion before it stops the script. One more thing to see: with $\rho = 0$, Block 2's last line (the $w(n)$ shading) cuts fills from 49% to 3.3% at $+0.17$ points each. Shading against a curse that is not there buys margin by giving away nearly all the volume.

**If you got this wrong, read:** §3.2.3 (the winner's curse and the Poker Table on cover prices), §3.3.5 (Done, Covered, Traded Away), and Block 2 of §3.8 with Listing 3.2 in Appendix F.

**Z.03.3: Kaz's bag of words, de-biased**

**Answer:** (a) $p^{*} = 0.218$. (b) Kaz's shortcut gives $p\,T/S = 0.054$, which is four times too low. As $p \to 1$ the corrected value goes to 1, while the shortcut can never exceed $T/S = 0.06$. (c) With $T = 0.15$ the corrected value is 0.614 and the shortcut 0.27. (d) About 2,280bp. The hazards are $-\ln(1 - 0.218) = 0.2456$ and $-\ln(1 - 0.054) = 0.0555$, and $0.6 \times 2 \times 0.1901 = 0.228$. (e) One answer: "The model learned how much more often defaulters use the phrase than survivors do, not how often users of the phrase default, and only the second number trades."

**How:** Elkan's correction is an odds update, scaled by the ratio of the live base-rate odds to the sample's:

$$
\frac{p^{*}}{1-p^{*}} = \frac{p}{1-p}\cdot\frac{T/(1-T)}{S/(1-S)} = 9 \times \frac{0.03/0.97}{1} = 0.278
\;\;\Rightarrow\;\; p^{*} = \frac{0.278}{1.278} = 0.218 .
$$

At $S = 0.5$ the sample odds are 1, so the correction reduces to multiplying the model's odds by the live odds. In (c) the live odds are $0.15/0.85 = 0.176$, the posterior odds are 1.59, and $p^{*} = 0.614$. The shortcut rescales the probability rather than the odds. That is the first-order version of the update and holds only while $p$ is small. At $p = 0.9$ the model's odds are 9, and the shortcut discards them. For (d), convert each answer to a one-year hazard, $\lambda = -\ln(1-p)$, and apply $\Delta s \approx L\,\kappa\,\Delta\lambda$.

**The trap:** §3.4.3 warns that the $T/S$ shortcut *overstates* and can exceed one, so readers expect it to err high here. That warning is for $T > S$, Bohn and Stein's case. Kaz's balanced sample has $S = 0.5 > T$, so the shortcut errs low, and the error is largest on the highest-scoring filings, which are the names you most need to price. In (d), the usual slip is to difference probabilities instead of hazards: $(0.218 - 0.054) \times 1.2 \times 10^4 \approx 1{,}965$bp.

**If you got this wrong, read:** §3.4.3 and "The Full Derivation: Elkan's correction is a Bayes update"; §3.4.2 for the hazard inversion and the explicit $\kappa$; Listing 3.5 in Appendix F (`elkan`, `hazard_from_pd`).

**Z.03.4: Put the Ledger on a clock**

**Answer:** (a) The flow signal has an IC of 0.079 at 1 day and 0.031 at 5 days. The fulcrum view has 0.040 and 0.039. (b) $h^\star = 4.07$ business days, from the closed form and from a numerical root alike. (c) The flow signal belongs in $\pi(x)$ only. The fulcrum view belongs in both, because it beats the flow signal at the 5-day markout horizon (0.039 against 0.031) and dominates at 20 days (0.036 against 0.001). (d) One definition: a counterparty's lie rate is the shrunk fraction of the axes or indications it showed the desk that were followed, within $k$ business days, by its own RFQs or trades in the opposite direction. You can build it from your own RFQ and axe logs. Give it a long half-life, months to years, because a grudge lasts.

**How:** Use $\text{IC}(h) = \text{IC}_0\,2^{-h/h_{1/2}}$, set the two features equal, and take logs:

$$
\ln 0.10 - \frac{h\ln 2}{3} = \ln 0.04 - \frac{h\ln 2}{120}
\;\;\Rightarrow\;\;
h^\star = \frac{\ln(0.10/0.04)}{\ln 2\,\big(1/3 - 1/120\big)} = \frac{0.9163}{0.2253} = 4.07 .
$$

By day 20 the flow signal has been through almost seven half-lives, while the fulcrum view has lost about a tenth of its power. Shrink the lie rate with the same estimator as §3.3.4, so that one broken axe does not condemn an account.

**The trap:** Ranking the features by $\text{IC}_0$ and putting the flow signal everywhere because 0.10 beats 0.04. The ranking flips after four days, which is inside the RFQ engine's own five-day horizon. The banker's version of the mistake runs the other way: keeping the fulcrum view out of $\pi(x)$ because it is "a portfolio view" that took ninety hours to build. At five days it beats the tape. A mechanical slip is to write $e^{-h/h_{1/2}}$ for $2^{-h/h_{1/2}}$, which treats the half-life as an e-folding time and gives $h^\star = 2.8$ days.

**If you got this wrong, read:** §3.5 (the decay column, the IC formula and Paleologo's common clock), the half-life box in §1.8.1, and §3.3.4 for shrinking the lie rate.

**Z.03.5: Detector economics**

**Answer:** (a) At $h = 4$ the bound is at most $400 \times 252 / e^{4} \approx 1{,}846$ false alarms a year; at $h = 8$ it is about 34. (b) $K = 1/2$, so detection takes about 8 days at $h = 4$ and 16 days at $h = 8$, leaving about 22 and 14 days of warning. (c) The thresholds are $h = 3.80$, 6.00 and 8.20 for PRS 0.9, 0.5 and 0.1, with delays of about 7.6, 12 and 16.4 days. Reading the documents buys about 8.8 days of warning across that range. (d) $h \ge \ln(400 \times 252/52) = \ln 1{,}938 = 7.57$. Under the chapter's Gaussian model, the realized rate at that threshold is about 8 alarms a year, not 52.

**How:** Lorden says the null average run length is at least $e^{h}$, so each tranche raises at most $252/e^{h}$ false alarms a year; multiply by 400. The delay is about $h/K$ with $K = \mu_1^2/(2\sigma_y^2) = \tfrac12$, so it is simply $2h$ days. The PRS threshold is

$$
h(\text{PRS}) = h_0 - \ln\frac{\text{PRS}}{1-\text{PRS}} = 6 \mp \ln 9 = 6 \mp 2.197 .
$$

All three values sit inside Listing 3.6's floor of 2.5 and cap of 10, so the clip never binds. For (d), the realized rate is lower because $e^{h}$ is a floor on the run length, not its value. Under the null, each day's evidence has a mean of $-K$, and the tally keeps resetting at zero, so it takes far longer to drift to $h$ than the bound allows. Siegmund's approximation and a 2,000-path simulation of (3.5) agree on the size of the gap. The run length is about 331 days against a bound of 55 at $h = 4$, consistent with Block 6's censored 304. At $h = 7.57$ it is about 12,000 days against 1,939. The simulated delays come out a few tenths of a day above $h/K$ (8.4 at $h = 4$, 16.4 at $h = 8$), because the tally overshoots the line. The PRS gap is still about 8.7 days.

**The trap:** Treating $e^{h}$ as *the* run length, then setting $h = 7.57$ and budgeting for 52 alarms a year. Compliance will see about eight. The overcorrection is just as wrong. Under independent Gaussian flow, $h \approx 5.75$ would already deliver about 52 real alarms a year, but real ADV-scaled flow is fat-tailed and autocorrelated. §3.8 calls $e^{h}$ a design target, not a guarantee, so keep it. A smaller slip: dropping the 400 tranches, which gives 4.6 alarms a year at $h = 4$, or using 365 calendar days instead of 252 trading days.

**If you got this wrong, read:** §3.6.2, including "The Full Derivation: Page's CUSUM" and "The prior: the documents set the fuse"; Block 6 of §3.8 and Listing 3.6 in Appendix F.

**Z.03.6: ROBO and the lucky client**

**Answer:** (a) ROBO ranks clients by raw mean markout. The one-fill client's $+300$bp puts it at the top, so it gets the tightest quote on the platform. It keeps that quote until its next trade, which comes quickly, because the best price on the platform is now being shown to it. (b) $\sigma^2/\tau^2 = 56.25$, so $k = 0.017$, 0.151 and 0.640 for $n = 1$, 10 and 100. The one-fill client's shrunk score is about $+5$bp ($0.0175 \times 300 = 5.2$). (c) For example: "Score each counterparty by the empirical-Bayes shrunk mean of its 5-day IDO markouts, in bp of price, re-estimating the between-counterparty variance monthly and flooring it at zero. Tighten quotes by at most `c` bp of price per bp of shrunk score, never on a raw mean, and log every override for a counterparty with fewer than `n_min` fills." (d) Selecting the top of many noisy scores selects for noise.

**How:** With $\sigma = 150$bp and $\tau = 20$bp,

$$
k = \frac{n}{n + \sigma^2/\tau^2}: \qquad \frac{1}{57.25} = 0.017, \qquad \frac{10}{66.25} = 0.151, \qquad \frac{100}{156.25} = 0.640 .
$$

A client needs 56 fills before its own record gets half the weight. The IDO requirement in (c) is what keeps the score from charging a client for the tide (§3.3.3). For (d), if you rank many clients by score $= \theta_c + \text{noise}$, the top of the list is selected for positive noise, so $\mathbb{E}[\text{noise} \mid \text{ranked first}] > 0$. It is the winner's curse again, with you as the auctioneer and your own scores as the bidders.

**The trap:** Using $\sigma/\tau = 7.5$ instead of $\sigma^2/\tau^2 = 56.25$, which gives $k(1) = 0.118$ and a score of 35bp. Another slip is to plug in Block 4's *estimated* $\hat\tau \approx 42$bp. That gives $\sigma^2/\hat\tau^2 \approx 12.5$, $k(1) = 0.074$ and a score of 22bp. The exercise asks for the true spread, and an estimate that comes out at double the truth on a seeded panel is the reason the spec re-estimates and floors $\tau^2$ rather than trusting a single fit. Watch the sign as well: a $+300$bp markout is *good* for the dealer, so ROBO's error is generosity to a lucky client, not suspicion of a toxic one.

**If you got this wrong, read:** §3.3.4 (counterparty scores, shrunk, and the batting-average box), §3.3.3 (IDO markouts), §3.2.3 (the winner's curse), and Listing 3.4 in Appendix F (`shrunk_cpty_scores`).

### Z.04 Chapter 4: Inside the Systematic Credit Industry

Six exercises. Each one checks a number that a pitch book tends to leave out: breadth, cost, capacity, the clip, the capture ratio and the filing date. Write your answer down before you read ours.

**Z.04.1: Effective breadth**

**Answer:** With $m = 2{,}400/600 = 4$ bonds per issuer, $BR_{\text{eff}} = 2{,}400/(1 + 3 \times 0.6) = 2{,}400/2.8 \approx 857$ independent bets. To reach an IR of 0.5 at $TC = 0.5$ you need $IC \approx 0.034$.

**How:** The design effect is $1 + (m-1)\rho = 1 + 3 \times 0.6 = 2.8$, so the 2,400 bonds diversify like 857 independent bets. That is only 1.4 times the 600 issuers, a long way from 2,400. Then invert (4.1):

$$
IC = \frac{IR}{\sqrt{BR_{\text{eff}}}\;TC} = \frac{0.5}{\sqrt{857.1}\times 0.5} = \frac{1}{29.28} \approx 0.0342 .
$$

The skill bar is $\sqrt{2.8} = 1.67$ times what the bond count suggests. Now run Kaz's Thursday check. At a stress-window $\rho$ near one, breadth collapses to the 600 issuers and the bar rises to $IC \approx 0.041$. Listing 4.1's `effective_breadth(2400, 600, 0.6)` returns the 857.

**The trap:** The usual mistake is to put the bond count straight into the law, which gives $IC = 0.5/(0.5\sqrt{2{,}400}) \approx 0.020$. That understates the skill you need by about 40%, and you would then lever the book to diversification you do not have. A second slip is to write $N/(1 + m\rho) = 706$. The "minus one" is there because a bond's correlation with itself is already counted in the $N$ variances; only its $m-1$ siblings add cross terms.

**If you got this wrong, read:** §4.3, "Scoring the breadth column: the fundamental law with issuer clustering," and its Full Derivation.

**Z.04.2: Kaz's Sharpe of 3.1**

**Answer:** An average cost of 32.5bp per dollar traded takes the IR to 0.5, and 38.75bp takes it to zero. A realistic HY half-spread is about 25bp to cross a liquid line, which is Ines's first number and an eighth to a quarter of a point in Chapter 4-D. The cheap-decile bonds a value signal buys cost more. At 25bp the IR is already down to 1.1, before size and fade. At Ines's all-in 50bp (25 + 10 + 15) it is $-0.9$. The sentence for Ines: "The 3.1 assumed free trading on sixteen dollars of turnover per dollar of book; a realistic half-spread takes it to about 1 and your all-in cost takes it below zero, so I'm putting the cost in the backtest and cutting the turnover before it goes anywhere near an allocator."

**How:** Costs do not change tracking error, so the IR is net alpha divided by 2%, and an IR of 0.5 means 1.0% of net alpha. One-way turnover of 8 is 8 sales plus 8 purchases, so the drag is $2T\bar c = 16\,\bar c$:

$$
6.2\% - 16\,\bar c = 0.5 \times 2\% \;\Rightarrow\; \bar c = \frac{5.2\%}{16} = 32.5\text{bp}, \qquad 6.2\% - 16\,\bar c = 0 \;\Rightarrow\; \bar c = \frac{6.2\%}{16} = 38.75\text{bp}.
$$

Each basis point of cost removes 16bp of alpha, or 0.08 of IR. The zero point is (4.6) read backwards: at $\bar c = 38.75$bp, $T_{\max} = 6.2\%/(2\bar c) = 8$. At 50bp, $T_{\max}$ is only 6.2 turns.

**The trap:** The usual mistake is dropping the 2 and dividing by 8 rather than 16, which gives 65bp and 77.5bp. Those look comfortably above a 25bp half-spread, and they would let Kaz tell Ines that costs don't matter. The subtler trap is to compare 32.5bp with the half-spread alone and call it safe. The half-spread is only the first of Man's three cost terms, and costs rise in exactly the months when a value or momentum book trades most.

**If you got this wrong, read:** §4.7, "Break-even turnover" (4.6), and Ines's "Twenty-five to cross" a few paragraphs earlier. Chapter 4-D replays this same exercise as an interview question.

**Z.04.3: The fee-adjusted hot tub**

**Answer:** The client's net alpha after fees is zero at

$$
A_f = \frac{\mathcal{L}\,(g-f)^2}{8\,T^3\eta^2} = \tfrac94 A^{*}\Big(1-\frac{f}{g}\Big)^2, \qquad 0 < f < g,
$$

and no positive size works if $f \ge g$. For any $f > 0$ the bracket is below one, so $A_f < \tfrac94 A^{*}$. Take the §4.8 worked example ($g = 120$bp, $A^{*} \approx \$1.85$bn). A 20bp fee moves the zero from \$4.17bn to \$2.89bn. A 50bp fee moves it to \$1.42bn, which is below $A^{*}$ itself, because $A_f > A^{*}$ only when $f < g/3 = 40$bp. A manager paid only on assets earns $fA$, which rises without limit. With sticky assets it therefore wants to be as large as it can raise, even past $A_f$, where clients lose money after fees. Performance-chasing flows change this. Clients leave once net alpha after fees turns negative, so $A_f$ becomes a ceiling. A manager that also sets its fee then maximizes $f A_f$, and the maximum is at $f = g/3$, which puts the book exactly at $A^{*}$ and hands the manager the whole $\Pi(A^{*}) = gA^{*}/3 \approx \$7.4$mm a year while the client keeps nothing.

**How:** The fee is a transfer from client to manager. It does not cost the strategy anything, so the hill $\Pi(A)$ stays where it was; only the split of the dollars changes. Set the client's net to zero:

$$
g - 2T\eta\sqrt{2TA/\mathcal{L}} - f = 0 \;\Rightarrow\; \sqrt{A_f} = \frac{g-f}{2T\eta\sqrt{2T/\mathcal{L}}} \;\Rightarrow\; A_f = \frac{\mathcal{L}(g-f)^2}{8T^3\eta^2}.
$$

Dividing by $A^{*} = \mathcal{L}g^2/(18T^3\eta^2)$ gives $A_f/A^{*} = \tfrac{18}{8}(1-f/g)^2$. With $f = 0$ you recover the chapter's $\tfrac94$. When flows drive the client's surplus to zero, revenue is $R(f) = \tfrac94 A^{*} f(1-f/g)^2$. Its derivative is proportional to $(1-f/g)(1-3f/g)$, which is zero at $f = g/3$, and there $A_f = \tfrac94 \cdot \tfrac49 A^{*} = A^{*}$. This is Berk and Green's point in miniature: when flows are competitive, the manager captures the rent and the client gets the market return.

**The trap:** The common wrong answer is that the asset-paid manager chooses $A^{*}$. That size maximizes *total* dollar alpha, so it is the choice of a manager paid a share of alpha. A pure asset fee pays on $A$, and the only thing that stops growth is the client walking out. Two algebra slips are also common. One is charging the fee per dollar traded, so that it gets multiplied by $2T$. The other is treating the client's net at $A^{*}$, $g/3 - f$, as if it were the zero point.

**If you got this wrong, read:** §4.8, Ines's "Who gets paid on what?" and the Full Derivation of the capacity maximum. Listing 4.2's `net_alpha_curve` will draw the hill if you subtract $f$.

**Z.04.4: Split the clip**

**Answer:** Branch on the *signs* of EBITDA and net debt before you form any ratio. With $\ell_i = \text{ND}_i/\text{EBITDA}_i$ and a sourced floor $\ell_{\min}$ (say 0.5x, illustrative, not 0.1):

$$
\text{score}_i =
\begin{cases}
\text{OAS}_i/\ell_i & \text{EBITDA}_i > 0,\ \ell_i \ge \ell_{\min} \quad\text{(ordinary)}\\
\text{OAS}_i/\ell_{\min},\ \text{flag low\_lev} & \text{EBITDA}_i > 0,\ 0 < \ell_i < \ell_{\min} \quad\text{(low positive leverage)}\\
\text{peer-relative spread } \tilde V_i \text{ only, flag net\_cash} & \text{EBITDA}_i > 0,\ \text{ND}_i \le 0 \quad\text{(net cash)}\\
\text{no value score} \rightarrow \text{distressed model} & \text{EBITDA}_i \le 0 \quad\text{(negative EBITDA)}
\end{cases}
$$

Missing or stale inputs get no score in any branch. The negative-EBITDA branch passes the distressed model what a recovery analysis needs, not what a ratio needs: the CUSIP mapped to issuer and class (lien, guarantors, structural position, from the security master); price rather than OAS, with its knowledge time; debt by class and maturity; liquidity (cash plus undrawn revolver) and cash burn; covenant headroom; the document flags for LMT capacity; and the knowledge times of the fundamentals. The distressed model returns price against expected recovery by class. The bond leaves the value ranking entirely. One assert that would have caught the 15,000: `assert not np.any((ebitda <= 0) & np.isfinite(value_score))`, meaning no issuer with non-positive EBITDA comes out of the value screen with a score. The distributor's EBITDA of $-\$20$mm trips it.

**How:** The ratio $\text{ND}/\text{EBITDA}$ is negative in two opposite worlds. A net-cash issuer has $\text{ND} < 0$ and $\text{EBITDA} > 0$, and is very strong. A company like the distributor has $\text{ND} > 0$ and $\text{EBITDA} < 0$, and is in distress. Separately, the ratio explodes as EBITDA approaches zero from above. A single `max(., 0.1)` sends all three cases to the same number. That is how the BB scores $250/4 = 62.5$, the net-cash IG name $900$, and the CCC $1{,}500/0.1 = 15{,}000$: 240 times the BB and 17 times the next-best name. The cure is to test the components before you divide, so the branches are decided by sign and size rather than by the clipped ratio. Within each branch, neutralize against peers as usual.

**The trap:** One common fix is to raise the clip, to 0.5 say. The CCC then scores 3,000 and still tops the list. Another is to take the absolute value of leverage: $|-30| = 30$ gives the CCC a score of 50, which looks like an unremarkable rich BB and quietly leaves a restructuring candidate in the value ranking. The third mistake is to route every negative ratio to the distressed model, which sends the net-cash IG issuer to a restructuring desk.

**If you got this wrong, read:** §4.4, "Value is the gap between Q and P," from the edge cases through Theo's building-products distributor. Chapter 13 covers what the distressed model has to see about priming.

**Z.04.5: Capture-ratio forensics**

**Answer:** $a \approx 15.4$bp a month (about 1.85% a year) and $\beta \approx 0.93$. Read through the linear model, this is not mainly beta. Of the 15 points of down-capture "defense," about 7 come from the slope ($1 - 0.93$) and about 8 from the alpha cushion ($a/\bar d = 0.081$). With BlackRock's mix of 168 up and 72 down months, $\mathbb{E}[r_m] = 0.34\%$, and the manager beats the index by about 13bp a month (1.6% a year), against roughly $-1$bp for BlackRock's average manager. That is top-decile HY, and that should make you suspicious. A capture pair with $UC > 1 > DC$ is just what a backtest with regime bins defined after the fact produces. It also fits asymmetric beta with no alpha at all ($\beta_{\text{up}} = 1.05$, $\beta_{\text{down}} = 0.85$). Two numbers cannot tell these stories apart. To tell them apart you need:

- the monthly manager and index returns, with the index named and the bins set by its sign;
- the counts of up and down months;
- a gross/net and live/simulated label;
- a regression with separate up and down slopes;
- the down months one by one, to see whether one month carries the result;
- holdings, to look for cash, IG, CDX protection or duration that rallies in risk-off.

**How:** Subtract the two capture equations of (4.7), using $\bar d > 0$:

$$
UC - DC = a\Big(\frac{1}{\bar u} + \frac{1}{\bar d}\Big) \;\Rightarrow\; a = \frac{0.20}{1/0.013 + 1/0.019} = \frac{0.20}{129.55} = 0.00154,
$$

then $\beta = UC - a/\bar u = 1.05 - 0.119 = 0.931$. Check: $DC = 0.931 - 0.00154/0.019 = 0.850$. Once you allow $\beta_{\text{up}} \ne \beta_{\text{down}}$, (4.7) has three unknowns and two equations, so it cannot separate alpha from convexity. A long HY book is short its issuers' default puts and should be *concave*, which makes the 20-point convex gap the claim that most needs explaining.

**The trap:** The common mistake is to read 85% downside capture as a beta of 0.85, which is the $a = 0$ reading, and call it a smaller long. That is BlackRock's average manager, not this one. A sign slip catches people too. Plugging $\bar d = -1.9\%$ into the formula gives $a = 0.20/(76.9 - 52.6) \approx 82$bp a month and $\beta \approx 0.42$, which no HY manager has ever had.

**If you got this wrong, read:** §4.9, "A line through the months," (4.7) and its Full Derivation, then "Seventy-two down months, and the one that matters."

**Z.04.6: The 10-Q join**

**Answer:** A non-accelerated filer has 45 days after quarter end to file its 10-Q and 90 days after year end to file its 10-K, and such filers usually file close to the deadline. A join on the fiscal quarter end therefore gives the backtest about 45 days of foresight in three quarters and about 90 in the fourth, roughly 56 days on average. If every filing uses the Form 12b-25 extension (5 more days for a 10-Q, 15 for a 10-K), that rises to about 64. At monthly rebalancing, 9 of every 12 month-ends trade on a leverage number nobody outside the company had. The join breaks the first of the Friday spec lines in §4.5: every field carries a knowledge time, and every join is an as-of join on it, so $s_{i,t} = f(\{x : t^{\text{kn}}(x) \le t - \ell\})$. Joining on event time is a lead error. The bias is largest for deteriorating credits for three reasons:

1. They file latest, through NT filings, going-concern work with the auditor and covenant waivers negotiated before the filing, and sometimes they never file at all.
2. Their leverage moves most from one quarter to the next, so the leaked number is the news.
3. A spread-over-leverage screen ranks them cheap in real time because the spread has already widened while the denominator is stale.

So the honest backtest buys the value trap and takes the loss when the 10-Q lands. The leaky one already sees the higher leverage, cuts the score and steps out of the way.

**How:** Take the quarter ending 30 June, with the 10-Q accepted by EDGAR around 14 August. The leaky join uses Q2 leverage at the 30 June and 31 July rebalances, and the honest join first uses it at 31 August, so two of the three month-ends leak. For the 10-K quarter, the 31 December, 31 January and 28 February rebalances all leak. That is $3 \times 2 + 3 = 9$ of 12. Put a number on it *(illustrative)*: a bond at 600bp with last-filed leverage of 4.0x scores 150 and sits in the cheap decile. If the unfiled Q2 leverage is 6.0x, the leaky backtest scores it 100 six weeks before anyone could have, and the bond is out of the long leg before the bad 10-Q lands. The error is correlated with the next month's return, so it does not average out. It inflates the value premium, and it does so in the long leg's worst names.

**The trap:** "Forty days" is the deadline for accelerated filers, not non-accelerated ones. A more expensive mistake is to "fix" the join with a fixed 90-day lag. That is too slow for early filers, and it still leaks for a 10-K filed under an NT extension (90 + 15 = 105 days). The honest fix is each filing's own EDGAR acceptance timestamp, or the earnings release where that release actually contains the field, plus a processing lag $\ell$.

**If you got this wrong, read:** §4.5, the "sealed envelope" box and the knowledge-time formula, then Thursday of "Rerunning Kaz's backtest on the clean panel," where Theo finds this exact join.

## Part II: Mathematical & Probabilistic Foundations for AI Specifiers

### Z.05 Chapter 5: Probability Distributions in Distressed & High-Yield Credit

Six exercises. I recomputed every number in Python. Exercise 3's simulation extends Listing 5.3 (Appendix F) on seed 7 with a million paths, using that listing's other Kou inputs. None of the chapter's exercises carries a [Read]/[Derive]/[Build] tag. Exercise 3 is a build in all but name, and Exercise 5(c) is a modelling exercise with more than one defensible answer, so its solution shows one worked choice and the reasons for it.

**Z.05.1: Two bonds, one VaR**

**Answer:** (a) The BB, at $q = 0.8\%$, has skew $-11.0$ and excess kurtosis $120$. The CCC, at $q = 12\%$, has skew $-2.34$ and excess kurtosis $3.5$. (b) The BB's 95% VaR never sees default. Since $0.8\% < 5\%$, the 5th percentile sits in the survival world. The CCC's VaR does see it. Since $12\% > 5\%$, the 5th percentile sits inside the default lump, at about the 42nd percentile of the recovery distribution ($5/12$). (c) The screen is measuring $1/q$, which is how *rarely* the bond defaults, not how much it loses when it does. The CCC looks "safer" because it defaults so often that default has become part of the body of its distribution.

**How:** Pin both worlds to points. The return is then an affine function of a Bernoulli, and its shape depends on $q$ alone:

$$
\text{skew} = -\frac{1-2q}{\sqrt{q(1-q)}}, \qquad \text{exkurt} = \frac{1-6q(1-q)}{q(1-q)}.
$$

For the BB, $q(1-q) = 0.007936$. The skew is $-0.984/0.0891 = -11.05$ and the excess kurtosis is $(1 - 0.0476)/0.007936 = 120.0$. For the CCC, $q(1-q) = 0.1056$. The skew is $-0.76/0.325 = -2.34$ and the excess kurtosis is $(1-0.634)/0.1056 = 3.47$. For (b), a 95% VaR stands on the 5% mark of the whole distribution, and the default world is the bottom $q$ of it. If $q < 5\%$, the mark falls among the survival wobbles. If $q > 5\%$, it falls among the recoveries. Price, recovery and survival volatility enter neither part. The jump size $J$ sets the variance, never the shape.

**The trap:** The usual mistake is reading kurtosis (or the size of the skew) as a riskiness score and concluding the BB is the dangerous bond. Kurtosis does not depend on units or position size. It measures how much of the variance comes from a rare outlier rather than the crowd, so it rewards a bond for defaulting *often*. The other slip, in (b), is calling the CCC's VaR "blind too" by reflex. At 12% the default world is a big enough slice that the 95% VaR lands in it. The BB's VaR stays blind until you go past 99.2%.

**If you got this wrong, read:** §5.1.3, "Skew is minus one over root PD," then the 95% VaR row of the §5.1.4 table and the paragraph under it.

**Z.05.2: The convexity tax**

**Answer:** $\sigma_X = 6.74\%$, the survival-leg skew is $-0.13$, and the convexity tax is $|c|\,v = 14.8$ bp (about 15). Flip to $C^{\text{spr}} = +8$ and the volatility does not change. The skew becomes $+0.13$, and the 14.8 bp becomes a convexity *bonus* to the mean. Now put that non-call survival leg into Theo's bond ($q = 4\%$, $P_0 = 0.92$, recovery Beta with mean 40 and s.d. 27.5). The mixture skew is still about $-4.1$.

**How:** Here $v = \kappa^2 s^2 h = (0.35 \times 0.055)^2 = 0.000371$ and $c = \tfrac12 C^{\text{spr}} = -4$. The exact moments of §5.9.1 give

$$
\sigma_X^2 = (D^{\text{spr}})^2 v + 2c^2v^2 = 12.25 \times 0.000371 + 32 \times (0.000371)^2 = 0.004544,
$$

so $\sigma_X = 6.74\%$. The convexity term adds almost nothing to the variance. The third moment is $\mu_{3,X} = 6(D^{\text{spr}})^2 c\, v^2 + 8c^3v^3 = -4.04\times10^{-5}$, and dividing by $\sigma_X^3 = 3.06\times10^{-4}$ gives a skew of $-0.132$. The mean is $x_0 + c\,v$, so the tax is $|c|\,v = 4 \times 0.000371 = 0.00148$.

Flipping the sign of $C^{\text{spr}}$ flips the sign of $c$. The variance and $\mu_{4,X}$ contain only even powers of $c$, while $\mu_{3,X}$ is odd in $c$, so the skew becomes $+0.132$.

For the mixture, compare the pieces of the full third moment (the Full Derivation at the end of §5.1.4). The survival leg contributes $(1-q)\,\mu_{3,X} = +0.00004$. The between-world term $-q(1-q)(1-2q)J^3$, with $J \approx 0.62$, contributes $-0.0085$. The cross term $3q(1-q)J(\sigma_X^2 - \sigma_Y^2)$ adds $-0.0061$, because the recovery lump is much wider than the survival hump. The coin outweighs the convexity by a factor of about 200.

**The trap:** There are two. The first is getting the tax wrong. $|C^{\text{spr}}|\,v$ gives 30 bp, but the half belongs in $c$. Writing it as $\tfrac12 |C^{\text{spr}}|\,\kappa s$ is also wrong, because $v$ is a variance, $\kappa^2 s^2 h$. The second trap is concluding from the positive survival skew that a non-call bond "has right-skewed returns." The survival leg is a lump sitting next to a coin, and its skew is two orders of magnitude too small to change the overall shape.

**If you got this wrong, read:** §5.9.1, "One last derivation: exact moments of the DTS survival leg," and then the Full Derivation at the end of §5.1.4 for the cross term.

**Z.05.3: Find the jump**

**Answer:** $\eta_2 = \ln 3/\ln 1.5 = 2.71$, $\mathbb{E}[V_\tau/B] = 2.71/3.71 = 0.730$, and the expected recovery given a jump default is $0.7 \times 0.730 = 51.1\%$. Then add the Brownian-bridge check to `simulate_kou_jd` and run it with Listing 5.3's other inputs ($\mu = 5\%$, $\sigma_V = 25\%$, $\eta_1 = 10$), weekly steps, seed 7 and a million paths. The one-year default probability rises from 15.75% to 17.10%, about 1.3 points or 8.5% of the uncorrected number. The whole rise is in the diffusive defaults, which go from 6.6% to 8.1%. Jump defaults stay at about 9.1%. A 2,520-step run with the bridge gives 17.08%, so the corrected weekly grid is effectively the continuous-monitoring answer. A daily grid *without* the bridge gives 16.51%, still half a point short. At the listing's own $\eta_2 = 4$ the rise is similar, from 13.74% to 15.14%.

**How:** Set the Result 1 intensity equal to the target:

$$
\lambda^{V}(1-p)\left(\frac{B}{V}\right)^{\eta_2} = 0.5 \times 0.6 \times 1.5^{-\eta_2} = 0.10.
$$

That gives $1.5^{\eta_2} = 3$, so $\eta_2 = 1.0986/0.4055 = 2.71$. Memorylessness makes the undershoot $U \sim \text{Exp}(\eta_2)$, so $\mathbb{E}[e^{-U}] = \eta_2/(1+\eta_2) = 0.730$. With $B = F$ and $\alpha = 0.3$,

$$
\mathbb{E}[R \mid \text{jump default}] = (1-\alpha)\,\frac{B}{F}\,\frac{\eta_2}{1+\eta_2} = 0.7 \times 0.730 = 51.1\%.
$$

That lies between the 52.5% and 46.7% rows of the §5.3.3 table, as it should for an $\eta_2$ between 3 and 2.

The build extends Listing 5.3 (Appendix F). In each step, keep the log-distance $x_t$ from before the diffusion move. For every path still above zero after that move, draw a uniform. If the uniform is below $\exp\!\left(-2x_t\,x_{t+\Delta t}/(\sigma_V^2\Delta t)\right)$, default the path and log it as diffusive, with `ratio` 1.0. The check belongs after the diffusion move and before the jumps, because the bridge formula applies only over a stretch of pure diffusion.

**The trap:** In the first part, the common slip is solving $(B/V)^{\eta_2} = 0.10$ and forgetting the $\lambda^{V}(1-p) = 0.3$ in front. That gives $\eta_2 = \ln 10/\ln 1.5 = 5.68$, a thin-jump world with an 85% undershoot. Another is to stop at 73% and call it the recovery. The 0.73 is assets over the barrier, before the 30% bankruptcy cost. In the build, don't apply the bridge probability to paths already below zero, because that double-counts them. And don't feed it $x$ after the jumps, because that slips a jump into what must be a pure-diffusion bridge. Finally, don't expect the one-year default probability to equal the 10% intensity. The intensity is instantaneous. Over a year the drift moves firms away from the barrier, so the jump-only default probability is about 9.1%, and diffusion adds another 8.

**If you got this wrong, read:** §5.3.3, Results 1 and 2 and the table that follows them, and then item (2) of the Ways This Blows Up box at the end of §5.9 for the bridge.

**Z.05.4: ROBO minimizes kurtosis**

**Answer:** The cap $\text{exkurt} \le 10$ holds exactly when $q(1-q) \ge 1/16$, that is, for $6.7\% \le q \le 93.3\%$. Every bond with a default probability below 6.7% fails it, and almost all distressed paper passes. At $q = \tfrac12$ the excess kurtosis is $-2$, the lowest any distribution can have. Here is a limit that does what the PM meant *(illustrative numbers)*: "Maximize yield subject to two limits. For every name, the jump-to-default loss $N_i\,(P_{0,i} - \mathbb{E}[R_i])$ must be at most 0.5% of NAV. For the book, the one-year 99% expected shortfall under $\mathbb{P}$, with defaults drawn on the common factor of §5.5.4, must be no worse than $-6\%$ of NAV." Theo's bond has a JTD of 52 points, so under that rule it can be at most $0.5\%/0.52 = 0.96\%$ of NAV in face.

**How:** Write $u = q(1-q)$. The skeleton's excess kurtosis is $(1-6u)/u = 1/u - 6$, so

$$
\frac{1}{u} - 6 \le 10 \iff u \ge \frac{1}{16} \iff q^2 - q + \tfrac{1}{16} \le 0 \iff \frac{1-\sqrt{3}/2}{2} \le q \le \frac{1+\sqrt{3}/2}{2},
$$

which is $0.067 \le q \le 0.933$. The cap acts as a *floor* on the default probability. At $q = \tfrac12$, $u = \tfrac14$ and $1/u - 6 = -2$.

That is the floor for any distribution, not just a bond. For a standardized $Z$, $\mathbb{E}[Z^4] - (\mathbb{E}[Z^2])^2 = \operatorname{Var}(Z^2) \ge 0$, so kurtosis is at least 1 and excess kurtosis at least $-2$. Equality needs $Z^2$ to be constant, which means two values with equal weight: a fair coin. The bond the metric scores best is therefore one equally likely to pay par or recovery. Yield rises with $q$, so the objective pulls the same way, and ROBO's ideal holding is a coin flip with a coupon attached.

The fix has to measure the *size* of the loss, and kurtosis cannot, because it does not depend on position size: double the position and the kurtosis stays the same. JTD prices the default card in dollars. The 99% ES averages the worst 1% of outcomes, which for any name with $q > 1\%$ means averaging inside the default lump (§5.1.4's $-92\%$).

**The trap:** The usual mistake is treating a kurtosis cap as conservative because "fat tails are bad." Excess kurtosis is about $1/q$, large when default is *rare*, so capping it bans the safe names and admits the distressed ones. The tempting repair, capping skew as well, fails the same way, because in the skeleton skew is also a function of $q$ alone. A limit that contains no position size and no loss amount cannot be a risk limit.

**If you got this wrong, read:** §5.1.3 for the two skeleton formulas, the VaR and expected-shortfall rows of the §5.1.4 table, and "95% VaR is blind whenever $q < 5\%$" in §5.10.

**Z.05.5: The 13-week model, one more time**

**Answer:** (a) $S = 0.998^8 \times 0.985^5 = 0.9841 \times 0.9272 = 0.9125$, so the 13-week default probability is $q = 8.75\%$. (b) The skeleton skew is $-2.92$ and the excess kurtosis 6.5. Because $q > 5\%$, a 13-week 95% VaR does see the default world. The 5% mark sits at about the 57th percentile of the default lump ($5/8.75$). (c) One defensible split uses §5.6.1's Moody's share of about 65% distressed exchanges: $q_{\text{DE}} \approx 5.7\%$, $q_{\text{HD}} \approx 3.1\%$, and survival 91.25%. The mixture is

$$
R_h = \mathbf{1}_{\{E=\text{S}\}}\,X + \mathbf{1}_{\{E=\text{DE}\}}\left(\frac{R_{\text{DE}}}{P_0} - 1\right) + \mathbf{1}_{\{E=\text{HD}\}}\left(\frac{R_{\text{HD}}}{P_0} - 1\right), \qquad E \sim \text{Categorical}(0.9125,\, 0.057,\, 0.031),
$$

with $R_{\text{HD}} \sim \text{Beta}(0.87, 1.30)$ (mean 40, s.d. 27.5) and

$$
f_{R_{\text{DE}}}(r) = w_{\text{in}}\,\text{Beta}(r;\, 5.59,\, 1.96) + (1-w_{\text{in}})\,\text{Beta}(r;\, 0.92,\, 2.77).
$$

The participant component is centred at 74 (s.d. 15) and the non-participant component at 25 (s.d. 20). All of (c) is *illustrative*.

**How:** (a) The survival curve is the product of one minus each week's hazard. The hazard view also tells you *when*: only 1.6 of the 8.75 points arrive in weeks 1–8, and the rest come after the revolver is gone. (b) Use Exercise 1's skeleton with $q = 0.0875$: $q(1-q) = 0.0798$, so the skew is $-0.825/0.2826 = -2.92$. The horizon is 13 weeks, so this is a 13-week VaR, not a one-year one.

(c) A default probability with no event type attached is now ambiguous (the §5.6.1 Trend Watch). Moody's June 2025 rates, 5.8% with distressed exchanges and 2.1% without, put the exchange share at $1 - 2.1/5.8 = 64\%$, and its 2025 full-year share was about 65%. For a sponsor-backed name whose agreement lets a simple majority do a non-pro-rata uptier, Mags's "runs out of patience in about week six" argues for at least that share.

The hard-default face takes §5.5.2's senior unsecured Beta. The exchange face takes two Betas, split by participation and fitted by the method of moments: $k = \mu(1-\mu)/\sigma^2 - 1$, $a = \mu k$, $b = (1-\mu)k$, which gives $k = 7.55$ for participants and $3.69$ for outsiders. The participant mean follows Serta's 74 exchange price and its 73.7–100 plan range. The outsider mean follows the remand court's 25. The weight $w_{\text{in}}$ is the probability that *you* are invited: about 0.1 for a small passive holder, close to 1 for a group member. At $w_{\text{in}} = 0.1$ the expected exchange recovery is $0.1 \times 74 + 0.9 \times 25 = 30$, *below* the hard default's 40, and that inversion is the lesson.

A full model would also send the exchange face into the re-default corridor, $\Pr(\text{HD by } t) = 0.25\,(1-e^{-0.60\,t})$. Within 13 weeks that moves at most 3.5% of the exchange mass, so it can be dropped at this horizon. At one year it is 11%, and it cannot.

**The trap:** In (a), adding the hazards, $8 \times 0.2\% + 5 \times 1.5\% = 9.1\%$. That is close here but wrong in principle, because you can only default in week 9 if you survived to it. In (b), calling the VaR "blind" by reflex. Blindness needs $q < 5\%$. At 8.75% the VaR lands in the lump, and its value then depends on the recovery Beta, which is where the work is. In (c), the classic error is setting $w_{\text{in}}$ to the participation share (52.6% at Serta, or "the group had 70%"). The other is giving the exchange face a single Beta with a middling mean, which averages two lumps into a hump that no holder will ever actually be paid.

**If you got this wrong, read:** §5.1.5 and its hazard-rate box for (a), and §5.1.3 for (b). For (c), read §5.6.1 (the three doors, the re-default clock, and "When the third state earns its parameters") and the Serta case in §5.6.2.

**Z.05.6: Two coins after the trim**

**Answer:** (a) The Kestrel spike is $60 \times (0.97 - 0.40) = -\$34.2$mm, at odds of $0.0335/0.6 = 5.6\%$ a year. The Halvorsen spike is $35 \times (0.78 - 0.40) = +\$13.3$mm, at $0.14/0.6 = 23.3\%$. (b) The expected jump P&L is $0.2333 \times 13.3 - 0.0558 \times 34.2 = 3.10 - 1.91 = +\$1.19$mm a year, and the jump standard deviation is $\sqrt{61.7 + 31.6} = \$9.66$mm. (c) Matching Kestrel's DTS takes $70{,}190/(0.78 \times 2.3 \times 1{,}400) = \$27.9$mm of Halvorsen face, and that short alone leaves $+\$0.57$mm. The other \$7.05mm of short adds $+\$0.625$mm. (d) Two lines. The short owes the lender Halvorsen's 7.25% coupon on \$35mm, about \$2.54mm a year. The borrow fee, reset to 300 bp on \$27.3mm of market value, is about \$0.82mm a year. Together that is \$3.36mm of cash cost against \$1.19mm of expected jump gain.

**How:** Strip each leg to §5.1.2's coin: a spike of face times (price minus recovery), with $\mathbb{Q}$ odds $\lambda \approx s/(1-R)$. Independent coins add their means and also their between-world variances:

$$
\operatorname{Var} = 34.2^2 \times 0.0558 \times 0.9442 + 13.3^2 \times 0.2333 \times 0.7667 = 61.7 + 31.6 = 93.3 .
$$

The jump s.d. has barely moved from April's \$9.8mm, but its make-up has. The long alone is \$7.85mm. The coins-only skew of the pair is now about $-1.8$, against $-1.4$ in April, because the short's spike has shrunk from \$19.5mm to \$13.3mm and offsets less of the Kestrel tail.

For (c), DTS per dollar of face is $P\,D^{\text{spr}}\,s$, and the expected jump per dollar of face is $s\,(P-R)/(1-R)$. Their ratio does not contain the spread:

$$
\frac{\text{expected jump}}{\text{DTS}} = \frac{P-R}{(1-R)\,P\,D^{\text{spr}}} .
$$

It is 0.272 for Kestrel and 0.353 for Halvorsen. In April the two were 0.270 and 0.272, which is why the April match netted to about $-\$10{,}000$. Halvorsen's fall in duration from 3.4 to 2.3 raises its ratio by 48%. Its fall in price from 90 to 78 lowers it by 12%, because there is less room to fall to 40. So even a DTS-matched \$27.9mm short carries \$0.57mm more expected default gain than the long carries expected loss. The \$7.05mm the 2:40 trim left above the match adds $0.2333 \times 7.05 \times 0.38 = \$0.625$mm.

For (d), the +\$1.19mm is a $\mathbb{Q}$ number. The 23.3% is what the market charges for Halvorsen's coin, and the short pays that charge every year Halvorsen survives: in the coupon it owes the lender, and in the pull to par running against it. The fee's jump from 50 bp to 300 bp is the price of a crowd wanting to hold the same coin. Add the long's \$3.6mm coupon and roughly \$0.6mm of financing, and the pair now runs at about $-\$0.36$mm a year before the CDX HY carry.

**The trap:** In (b), people net the spikes ($34.2 - 13.3 = \$20.9$mm) and call that the pair's tail, or they subtract the variances. Independent coins add variance even when their means offset. In (c), the trap is assuming a DTS match is a jump match. It is one only when prices and durations are close, as they were in April, because DTS scales with duration and the jump does not (§5.3.1). A second trap is putting all of the +\$1.19mm down to the DTS overhang and treating the CDX HY sale as the fix. The index moves neither spike. In (d), the trap is taking a positive expected jump P&L as free. At $\mathbb{Q}$ odds the short's expected gain is just what it pays in carry. Under $\mathbb{P}$ the odds are lower and the gain is smaller, while the coupon and the fee go out in cash every day.

**If you got this wrong, read:** The Pair box at the end of §5.1.4 (PB-01 in April), then §1B.2 for the orange line, the 2:40 trim and the carry lines. §8D.4, "Two Jump Processes," has the expected-jump formula, and §5.3.1's Dynkin annotation explains why a jump to default ignores duration.

### Z.06 Chapter 6: Stochastic Calculus, Intensity Models & Structural Frameworks

Eight exercises: the two warm-ups, A and B, and the six numbered ones. I recomputed every number in Python. Where an exercise names an engine function, I ran it from Appendix F, Listings 6.1–6.7, seeded `default_rng(42)`. None of the chapter's exercises carries a [Read]/[Derive]/[Build] tag, so none appears below.

**Z.06.A: Warm-up A, the holdco at 40**

**Answer:** (a) Outside the bank, the holding company has $\$2{,}258+491+896+577=\$4{,}222$mm of assets against $\$3{,}370+305=\$3{,}675$mm of liabilities. Book recovery is therefore **1.15 per dollar (115%) with the cash** and $\$1{,}964/\$3{,}675=$ **0.53 (53%) without it**. The notes at 40 were pricing the no-cash world. They actually sat 13 points *below* it, a discount for time, fees, and claimants who had not filed yet. (b) A twelve-point gap implies a reinstatement probability of $12/17\approx$ **71%, "roughly 70%."**

**How:** For (a), add up the four non-bank assets and divide by the two liabilities. Then remove the cash, because a bank holding company keeps its cash at its bank, and from noon on 10 March that cash was a deposit claim on a receivership. For (b), use two states. With probability $p$ the bonds are reinstated (2025s worth 97, 2031s worth 80). Otherwise both pay the same liquidation value $L$ per dollar of claim:

$$
P_{25}=97p+L(1-p),\qquad P_{31}=80p+L(1-p)\;\Longrightarrow\;P_{25}-P_{31}=17p=12,\quad p=0.706 .
$$

The unknown $L$ cancels, and that is the whole trick: the *gap* identifies the probability without your knowing the recovery. Use only the gap. Put $p=0.706$ back into either price and the implied $L$ is under 2 cents, far below the 53% no-cash coverage, so the two-state model reads a probability from the spread but is not meant to fit the two price levels. I checked the reinstatement values. Priced at a 5% yield from 25 April 2023, a 3.50% note maturing January 2025 is worth 97.5 clean and a 1.800% note maturing February 2031 is worth 79.6, so 97 and 80 are fair. A low coupon kept to a long maturity is worth less when the market yields 5%.

**The trap:** In (a), the trap is the 115%: you read "par is in there" and buy at 40. That is Theo's first answer, before Mags asks where a bank holdco keeps its cash. In (b), the trap is to read the gap as an arbitrage between two identical claims. They are identical only in liquidation. The market was pricing a second state in which they are not.

**If you got this wrong, read:** §6.4.4, Beat 4 and "Decision point: the holdco at 40" (with Figure 6.4), then Beat 5, "the same claim at two prices."

**Z.06.B: Warm-up B, secured at 76.8 or stripped at par**

**Answer:** Exchanging is worth $0.768\times\$1{,}000\times0.90=$ **\$691** per \$1,000 of old face. Holding out is worth $\$1{,}000\times0.60=$ **\$600**, so the exchange wins by about \$91. The holdout breaks even at a stripped-note price of $0.768\times90=$ **69.1**. The sentence: *the holdout still owns \$1,000 of face, but it now stands behind about \$4.2bn of new secured notes with a lien it does not share, in an indenture whose covenants were stripped by exit consents. Its strike moved up and its barrier was deleted, so the face amount is the only thing that stayed the same.*

**How:** Put both choices on the same denominator, \$1,000 of *old* face:

$$
V_{\text{exchange}}=0.768\times P_{\text{sec}}\times1{,}000,\qquad V_{\text{hold}}=P_{\text{strip}}\times1{,}000,\qquad P^{*}_{\text{strip}}=0.768\times P_{\text{sec}}=69.1 .
$$

This ignores coupons (the new notes' early PIK, the old 5.5% cash coupon), which is fine over a short horizon where the price gap dominates. In the language of §6.5.3, the left-behind payoff becomes $\min\big(\max(V_T-F^{+},0),F\big)$: the same $F$ of face, sitting on top of a new senior layer $F^{+}$.

**The trap:** One wrong answer compares prices and says "90 beats 60," which forgets that you get only 76.8 cents of new face per dollar of old. The mirror-image error is "\$1,000 of face beats \$768." The answer is always face times price. For the sentence, the trap is "same CUSIP, same coupon, same maturity, so same claim." Everything that made it a claim on the firm's value (rank, liens, guarantees, covenants) was changed around it.

**If you got this wrong, read:** §6.10.1, Beats 3–4 and "The Merton reading"; §6.5.3, "An uptier moves the barrier for someone else."

**Z.06.1: The vol trade inside a bond**

**Answer:** For the §6.2.4 firm, the Merton spread is **27 bp at $\sigma_V=15\%$** (27.4), 216 bp at 25%, and **531 bp at 35%**. Debt is worth 76.65, 75.22 and 72.89. The derivative is $\partial B_0/\partial\sigma_V=-V_0\,\phi(d_1)\sqrt T<0$, which is $-7.5$, $-19.9$ and $-26.0$ per unit of volatility at the three points. At 25%, one more vol point costs the bond about 0.20 and widens the spread by about 26 bp. The sentence for Theo: *your bond is par minus a put you wrote to the shareholders, and a put is worth more when the asset is more volatile, so every point of asset vol is money out of your pocket and into the equity's. A sponsor who owns the call knows that a risky acquisition financed at today's spread moves value from the bondholders to the sponsor before a single synergy shows up.*

**How:** $V_0$ does not depend on $\sigma_V$, so

$$
B_0=V_0-E_0\quad\Longrightarrow\quad\frac{\partial B_0}{\partial\sigma_V}=-\frac{\partial E_0}{\partial\sigma_V}=-\text{vega}.
$$

Differentiate the call. The identity $V_0\phi(d_1)=Fe^{-rT}\phi(d_2)$ kills the cross terms, and $\partial d_1/\partial\sigma_V-\partial d_2/\partial\sigma_V=\sqrt T$, so

$$
\text{vega}=V_0\,\phi(d_1)\sqrt T>0 .
$$

Equivalently, $B_0=Fe^{-rT}-\text{Put}$, and by put–call parity the put has the same vega as the call. For the spreads, use $s=-\tfrac1T\ln\!\big(B_0/Fe^{-rT}\big)$ with $Fe^{-rT}=76.86$. Notice the convexity: from 15% to 25% the spread rises by 189 bp, and from 25% to 35% by 315 bp. Listing 6.2's `merton_prices` reproduces all three spreads.

**The trap:** The most common wrong answer is "bondholders are long vol, because higher vol means a wider spread and a bigger coupon." That confuses the spread a *new* buyer demands with the value of the bond you already own, which falls. The second trap is algebraic: if you skip the identity $V_0\phi(d_1)=Fe^{-rT}\phi(d_2)$, you are left with a four-term mess and often a sign error.

**If you got this wrong, read:** §6.2.1, "Payoff diagrams" (the bondholder wrote a put); §6.2.3, the closed forms; §6.2.4, the worked example and Figure 6.3.

**Z.06.2: Is it cheap or is it the rake?**

**Answer:** At one year, $DD^{\mathbb{P}}=-N^{-1}(1.5\%)=2.170$. The shift is $\rho\,\text{SR}_M=0.175$, so $DD^{\mathbb{Q}}=1.995$ and **$\text{PD}^{\mathbb{Q}}_1=2.30\%$**. At five years, compounding the 1.5% gives **$\text{PD}^{\mathbb{P}}_5=7.28\%$**. The shift grows to $0.175\sqrt5=0.391$, so **$\text{PD}^{\mathbb{Q}}_5=14.4\%$**. On the CDS side, $\lambda^{\mathbb{Q}}=0.018/0.60=$ **3.0%**, which gives a five-year $\mathbb{Q}$-PD of **13.9%**. Compared raw, protection looks twice too expensive. The CDS hazard is 2.0 times the $\mathbb{P}$ hazard, and the $\mathbb{P}$-PD alone justifies only about 91 bp. But after the diffusive premium *alone*, the structural $\mathbb{Q}$-PD (14.4%, an average hazard of 3.10%, a fair spread near 186 bp) sits slightly *above* the CDS's 13.9%. So the CDS is about 6 bp tight, not wide. It is the rake.

Three things to strip before calling any residual alpha:

1. **The whole risk premium.** The CAPM shift removes the diffusive part. The jump premium of §6.3.3 is still in there, and removing it would make the CDS look tighter still.
2. **The recovery convention.** The 3.0% is conditional on the 40% quoting recovery, and a spread identifies only $\lambda(1-R)$. At $R=23\%$ the same 180 bp gives $\lambda=2.34\%$ and a five-year PD of 11.0%.
3. **Systematic factor exposure and liquidity.** Beta, the illiquidity premium, and the CDS–bond basis all sit in the gap. A high $\lambda^{\mathbb{Q}}/\lambda^{\mathbb{P}}$ in a risk-off week is "beta wearing a disguise." IDO or it didn't happen.

**How:** The Bohn–Stein shift is

$$
\text{PD}^{\mathbb{Q}}_T=N\!\Big(N^{-1}\big(\text{PD}^{\mathbb{P}}_T\big)+\rho\,\text{SR}_M\sqrt T\Big).
$$

At five years, first turn the one-year $\mathbb{P}$-PD into a five-year one with a constant hazard: $\lambda^{\mathbb{P}}=-\ln(0.985)=1.51\%$, so $\text{PD}^{\mathbb{P}}_5=1-0.985^5=7.28\%$. Only then shift, by $0.175\sqrt5$: $N(-1.455+0.391)=N(-1.064)=14.4\%$. For the CDS, the triangle gives $\lambda=s/(1-R)$ and survival $e^{-5\lambda}=e^{-0.15}$. To compare like with like, turn the structural $\mathbb{Q}$-PD back into a hazard: $-\ln(1-0.1437)/5=3.10\%$. Times $0.60$, that is 186 bp against the 180 bp quoted.

**The trap:** The trap is Theo's first week: you set a $\mathbb{P}$ number (1.5%) beside a $\mathbb{Q}$ number (3.0%) and sell protection because "the market is too scared." The gap is the premium you are paid to bear default in bad states, and it is not a mispricing. Two mechanical errors follow from it. If you drop the $\sqrt T$, the five-year $\text{PD}^{\mathbb{Q}}$ comes out at 10.0% and the CDS looks four points too wide. If you shift the CDS-implied 13.9% a second time, you get 24.4%, a double count that makes every bond look rich.

**If you got this wrong, read:** §6.3.1, Ines's napkin; §6.3.2, the Full Derivation and "What the shift does to a risky firm and a safe one"; §6.3.3 on the jump premium; §6.8.3, the credit triangle and "Forty percent recovery is a convention"; §6.9.1, the $\Pi_t$ ratio.

**Z.06.3: ROBO receives $\sigma_E=0.04$ for a CCC issuer**

**Answer:** These are the guards that should fire, in order:

1. **The input guard in `solve_kmv` (Listing 6.3).** It rejects any $\sigma_E$ outside 5%–300% with a `ValueError`, *before* `fsolve` runs. This is the one that fires.
2. **The post-solve bound $\sigma_V\in[1\%,300\%]$.** Without guard 1, this would raise a `RuntimeError` for any name whose equity is below roughly a third of its default point: $\sigma_V$ solves to 0.69% at $E/F=0.2$ and 0.95% at $E/F=0.3$. It passes at $E/F\ge0.4$ ($\sigma_V=1.18\%$), so treat it as a backstop. You cannot rely on it.
3. **Upstream, the spec's `sigma_frequency` field.** It should have said "daily" before the number reached the engine.

The `_d1d2` clamp at 0.0001 does *not* fire. The naive-DD fallback does not rescue you either, because it uses the same 4% and returns a PD of 0.07% at $E/F=0.2$. The message ROBO should print:

> ValueError: [issuer, as_of] sigma_E = 0.04 is outside [5%, 300%]. Is it annualized? If daily, 0.04 × √252 = 63.5%; if weekly, 0.04 × √52 = 28.8%. Check sigma_frequency on the vendor feed. No DD or PD written for this issuer.

Without any guard, the reported one-year PD is **0.00%**. In fact it is about $10^{-166}$ under $\mathbb{Q}$ for a CCC whose market cap is 20% of its default point, and below $10^{-144}$ for every equity-to-default-point ratio from 0.05 to 0.6. Annualize the same 4% as a daily figure (63.5%) and that balance sheet gives $\sigma_V=11.5\%$ and a $\mathbb{Q}$-PD of 5.9%.

**How:** The dangerous part is that the solver *converges*, with residuals around $10^{-15}$. As $\sigma_V\to0$ the call is worth its intrinsic value, $E_0\approx V_0-Fe^{-rT}$. Take $E_0=20$ and $F=100$: then $V_0\approx116.1$ and $\sigma_V\approx\sigma_E E_0/(N(d_1)V_0)=0.04\times20/116.1=0.69\%$, so

$$
d_2\approx\frac{\ln\!\big(1+E_0/Fe^{-rT}\big)}{\sigma_V}=\frac{\ln(116.08/96.08)}{0.0069}\approx27,\qquad N(-27)\approx10^{-166}.
$$

The numerator is positive for *any* positive equity, so $d_2\to\infty$ as $\sigma_V\to0$ on every balance sheet. That is why "any plausible CCC balance sheet" reports 0.00%. Through the desk's empirical DD map it would land in the safest bucket, an AA's default rate pinned on a CCC. That is the page for Mags's rating-agency file.

**The trap:** The usual wrong belief is that a bad input produces a failed solve and an error. It produces a clean, converged, fifteen-digit answer to the wrong question. The second wrong answer is "the fallback catches it," but the naive DD inherits the same $\sigma_E$. The third is accepting 4% as merely low. It is lower than the annual volatility of almost any listed stock, let alone a CCC's, which runs at 60% or more.

**If you got this wrong, read:** §6.1.3, "Annualize or die," and the `sigma_frequency` story; §6.11, Block 2, and "Edge cases ROBO must handle, in writing"; §6.4.3 on the empirical mapping; §6.12, item 2.

**Z.06.4: Covenants and uptiers as barrier mechanics**

**Answer:** **Covenant.** $V_0=8\times110=880$, the barrier is $K=(8/6)\times600=800$, and $x_0=\ln1.1=0.0953$. With zero log drift ($\mu=\tfrac12\sigma_V^2$ in `black_cox_pd`), the one-year breach probability is $2N(-0.381)=$ **70.3%**, matching §6.5.3. If you pass `mu=0` to `black_cox_pd` (zero drift in $V$), you get 73.6% instead.

**Uptier.** Under Merton with $T=3$, $r=4\%$, $\sigma_V=25\%$ and $V_0=880$ held fixed, the left-behind lenders' \$600mm falls from **\$514.5mm** to **\$465.0mm**. That is a loss of **\$49.5mm**, and with it their $\mathbb{Q}$-PD rises from 17.2% to 38.9% and their spread from 113 bp to 450 bp. The new \$200mm super-priority layer is worth \$177.4mm, almost riskless ($200e^{-0.12}=177.4$). With $V_0$ fixed, everyone beneath it pays for it: \$49.5mm comes from the left-behind lenders and \$127.9mm from the equity. So about \$49mm of the old lenders' value moved to the group that now ranks ahead.

**For Kaz: no.** In an open-market purchase, whoever sells gets the market price. The lenders who do not sell keep $\min(V_T,F)$, with the kink where it was (or lower, since less debt now sits beside them) and nothing new ahead of them. Here the left-behind diagram gained a dead zone from 0 to 200 and its kink moved from 600 to 800: the whole line slid \$200mm to the right. A purchase does not change the payoff of the holders who did not sell. A priming does, and this diagram is a priming.

**How:** The Black–Cox formula with $g=0$ and $T=1$ is

$$
\mathbb{P}(\tau\le1)=N\!\Big(\frac{-x_0-m}{\sigma_V}\Big)+e^{-2mx_0/\sigma_V^2}N\!\Big(\frac{-x_0+m}{\sigma_V}\Big)\;\xrightarrow{\;m=0\;}\;2N\!\Big(\frac{-0.0953}{0.25}\Big)=0.703 .
$$

In `black_cox_pd` (Listing 6.4), $m=\mu-\tfrac12\sigma_V^2-g$, so zero log drift means passing $\mu=0.03125$. For the uptier, write each claim as calls on the same $V$, with $C(K)$ the three-year Merton call from Listing 6.2:

$$
\underbrace{\min(V_T,600)}_{\text{before}}=V_T-(V_T-600)^+\;\Rightarrow\;V_0-C(600)=514.5,\qquad \underbrace{(V_T-200)^+-(V_T-800)^+}_{\text{after}}\;\Rightarrow\;C(200)-C(800)=465.0 .
$$

Value is conserved: $49.5+127.9=177.4=V_0-C(200)$. One extension worth knowing: suppose the \$177mm were real new money that stayed in the firm ($V_0=1{,}080$). The left-behind lenders would still lose about \$15mm (514 to 499), so priming moves value even when the cash is real.

**The trap:** For the covenant, there are two traps. One is the `mu=0` mistake above (73.6%). The other is using the Merton *terminal* probability, 35.2%, and forgetting that a monitored barrier roughly doubles it. For the uptier, the common wrong answer is pro-rata thinking: treat \$800mm as one class and give the old lenders three-quarters of it, $0.75\times(880-C(800))=\$481.8$mm, a loss of only \$32.7mm. That prices the new debt as pari passu. The whole point of the exercise is that it ranks ahead.

**If you got this wrong, read:** §6.5.2, the Math, Gently box and the three checks in the Full Derivation; §6.5.3, the loan's life from covenant to uptier, and the Docket Diary; Listing 6.4.

**Z.06.5: Mags's recovery**

**Answer:** Take a one-year contract quoted at 500 bp, with 4% flat discounting and quarterly coupons with accrual on default (Listing 6.6). The bootstrap gives **$\lambda=8.29\%$ at $R=40\%$** (the triangle says 8.33%) and **$\lambda=6.46\%$ at $R=23\%$** (the triangle says 6.49%). Both curves reprice the 500 bp quote to about $10^{-17}$. The upfront on a 100 bp standard coupon is $(s-c)\times\text{RPV01}$: **3.75 points at $R=40\%$** and **3.78 points at $R=23\%$**. Default pays **60 points versus 77**. The default payout is the number that changes when the name defaults tomorrow. The auction sets recovery, not the quoting convention, so if Mags is right the protection seller hands over 77 points, not 60. The jump-to-default is 17 points larger than a book marked at $R=40\%$ believes, while today's price barely moved.

**How:** A quote identifies only the product $\lambda(1-R)$, so the triangle gives $0.05/0.60$ and $0.05/0.77$. The bootstrap runs Brent on $\lambda$ until $\text{PV}_{\text{prot}}/\text{RPV01}=500$ bp. Coupons paid quarterly in arrears make the premium leg a little less valuable, so $\lambda$ lands just below the triangle. The upfront is

$$
U=(s-c)\cdot\text{RPV01}=0.04\times0.9363=3.75\ \text{pts}\quad(R=40\%),\qquad 0.04\times0.9447=3.78\ \text{pts}\quad(R=23\%).
$$

The two upfronts differ only because the annuities differ. A higher $\lambda$ means lower survival (92.0% against 93.7% at one year) and so a slightly smaller RPV01. At zero rates the upfronts are 3.84 and 3.87.

**The trap:** The most common wrong answer is "lower recovery is riskier, so the hazard goes up." For a *fixed* spread it goes down: each default costs more, so fewer defaults are needed to justify 500 bp. The arithmetic version of the same slip is dividing by $R$ instead of $1-R$, which gives $0.05/0.23=21.7\%$. A second trap is quoting the upfront as $5-1=4$ points and forgetting the RPV01. A third is believing a recovery change reprices the contract today. It reprices nothing until default, which is why you ship $R$ with every hazard curve.

**If you got this wrong, read:** §6.8.2 on the two legs and the upfront; §6.8.3, the bootstrap, the triangle, and "Forty percent recovery is a convention"; §6.6.3, "forty percent of what?"; Listing 6.6.

**Z.06.6: "A bankrupt company's equity is worthless."**

**Answer:** **$E_0=13.75\%$ of $F$**, which rounds to 13.8%. The rule of thumb gives 12% (the exact zero-rate value is 11.9%). The gap is the rate: at 4% the strike's present value is only $0.961F$, so the call starts about 4% of $F$ in the money on a forward basis. Adding roughly half of that to the rule gives 14.0%. The model being right about the value does not make the June 2020 trade good, for three reasons:

1. **Value is not price.** Merton says an at-the-money claim with a year until confirmation is worth something. It does not say that something is whatever the tape prints after a run of about 1,000% from \$0.59 to \$5.50.
2. **Look at who sold.** The most informed seller at the table, the company itself, offered shares under a prospectus saying they "could ultimately be worthless." Ines's markout reads that as a statement about information, not about value.
3. **Outcome is not decision.** The package that arrived (\$1.53 in cash, a share of 3% of the new company, warrants or rights) depended on a right-tail move in used-car prices and on plan sponsors choosing to pay creditors in full at a strike they negotiated. "The pot odds were terrible. The hand still hit." Post-petition equity after a 1,000% rally is, ninety-nine times in a hundred, the worst bet at the table. In Chapter 11 the strike is not fixed: the plan writes it, and Merton assumes it cannot.

**How:** With $V_0=F$, $\ln(V_0/F)=0$, so

$$
d_1=\frac{(r+\tfrac12\sigma_V^2)T}{\sigma_V\sqrt T}=\frac{0.04+0.045}{0.30}=0.2833,\qquad d_2=-0.0167,
$$

$$
\frac{E_0}{F}=N(0.2833)-e^{-0.04}N(-0.0167)=0.6115-0.9608\times0.4934=0.1375 .
$$

The rule of thumb is the zero-rate, at-the-money expansion: $E_0=V_0\big[N(\tfrac12\sigma_V\sqrt T)-N(-\tfrac12\sigma_V\sqrt T)\big]\approx\phi(0)\,\sigma_V\sqrt T\,V_0=0.399\times0.30\,V_0\approx0.12\,V_0$. Notice also that $N(-d_2)=50.7\%$. Under $\mathbb{Q}$ it is a coin flip whether equity finishes out of the money, and the call is still worth about a seventh of the debt.

**The trap:** One wrong answer is zero, the RSSG instinct that a filing means the strike has already been evaluated. Another is 12%, the rule of thumb without rates, which is Theo's number before Kaz corrects it. The deeper trap is concluding that because the model valued the claim correctly, buying it was correct. That mixes up a valuation with a price, and an outcome with a decision.

**If you got this wrong, read:** §6.2.1, "Payoff diagrams"; §6.2.3, the closed forms; §6.10.2, "Hertz: the hand that hit," and Ines's Poker Table box.

### Z.07 Chapter 7: Machine Learning on Small-Sample, Non-Stationary Credit Data

This chapter has six exercises, all in the end-of-chapter set, and none carries a [Read]/[Derive]/[Build] tag. I recomputed every number in Python. That includes the warm-up count in Listing 7.1, the uniqueness sum in Listing 7.4, the purge-and-embargo condition in Listing 7.5, and the $SR^\ast$, PSR and MinTRL formulas in Listing 7.6 (all in Appendix F).

**Z.07.1: Count Kaz's hats**

**Answer:** (a) In the interior, $11 \times 63 = 693$ labels are live on any given day, so $\bar u_i \approx 1/693 \approx 0.0014$. Summed over all $11 \times 1{,}197 = 13{,}167$ labels, that gives $N_{\text{eff}} = 19.98 \approx T/h = 20$, and you get exactly the same 19.98 with one bond or with eleven. (b) Yes, they stay **one group**, keyed on the ultimate parent. What the drop-down creates is a new *within-parent* target: the OpCo–HoldCo basis, meaning the priming loss to the HoldCo notes relative to the OpCo notes. Inside this one family you can validate it only across time blocks (purged and embargoed walk-forward), because there is no other parent to hold out. (c) $(\sum w)^2/\sum w^2 = 10^2/40 = $ **2.5**. Five rows, two and a half opinions.

**How:** For (a), skip the interior approximation and use the identity that makes the hat count exact. Each covered day $t$ appears in $c_t$ label windows, and each of those labels counts it at $1/c_t$, so the day contributes exactly 1 to the double sum. With every window $L = 63$ days long ($t_1 = t_0 + 62$):

$$
N_{\text{eff}} = \sum_i \bar u_i = \frac{1}{L}\sum_i \sum_{t=t_{0,i}}^{t_{1,i}} \frac{1}{c_t} = \frac{1}{L}\sum_{t\ \text{covered}} c_t \cdot \frac{1}{c_t} = \frac{1{,}197 + 62}{63} = 19.98 .
$$

The bond count $B$ drops out, because eleven sibling labels cover the same days as one. If you count the window inclusively as 64 days ($t_1 = t_0 + 63$), you get $1{,}260/64 = 19.7$, which is still $\approx T/h$. For (b), the HoldCo and OpCo notes are claims on one enterprise value and react to the same news. The unrestricted subsidiary that received the assets maps to the parent too (§7.5's Model Review Tuesday). Put the HoldCo notes in training and the OpCo notes in test, and the model reads one side's answer off the other. Model the basis as a pair label on the two legs (§7.4's pair corridor). If you later collect drop-down events across many issuers (Chapter 13), group by parent again.

**The trap:** In (a), the trap is $11 \times 20 = 220$, or the 13,167 rows. More bonds feel like more evidence, but siblings formed on the same day are one issuer's news at eleven durations. In (b), the trap is to treat the drop-down as a new credit and split the family "because the documents now separate them". The documents separate the *claims*. The *information* is still one company's. In (c), the trap is to answer 5 because "there are five rows".

**If you got this wrong, read:** §7.6, "Hats, not rows", "Uniqueness, defined" and "The hat count"; §7.7, "Group by parent, not ticker, especially in the LMT era"; §7.5, Quant-Shop Life.

**Z.07.2: Memory after a closing night**

**Answer:** (a) The weights are $(1,\ -0.4,\ -0.12,\ -0.064,\ -0.0416)$. They sum to 0.3744, so after four lags about 37% of the level is still in the feature (27% at $d = 0.5$). (b) The partial sum is $\prod_{j=1}^{K}(j-d)/j$, a product of factors that each lie in $(0,1)$. It is therefore positive for every finite $K$ and decays like $K^{-d}/\Gamma(1-d) \to 0$. (c) The embargo must be **at least 280 days** (281 by Listing 7.1's count), because $\max(h, \text{FFD window}) = \max(63, 280)$. The embargo alone removes $280/315 = 89\%$ of a block, and 22% of the sample, after every test block except the last. Add the 63-day purge that sits in front of it, and the training data lost after each test block is about 343 days, more than a whole block. At $\tau = 10^{-3}$ the window is 54 days, so $h = 63$ sets the embargo again. The cost is memory: the truncated filter keeps 13.6% of the level instead of 7.0%, the series trends more, and the smallest $d$ that passes the unit-root test tends to rise.

**How:** For (a), start at $w_0 = 1$ and apply $w_k = -w_{k-1}(d-k+1)/k$: $w_1 = -0.4$, $w_2 = 0.4(-0.6)/2 = -0.12$, $w_3 = 0.12(-1.6)/3 = -0.064$, $w_4 = 0.064(-2.6)/4 = -0.0416$. For (b), write $a_k = (-1)^k\binom{d-1}{k}$. Pascal's rule turns each weight into a difference:

$$
w_k = (-1)^k\Big[\tbinom{d-1}{k} + \tbinom{d-1}{k-1}\Big] = a_k - a_{k-1}
\quad\Longrightarrow\quad
\sum_{k=0}^{K} w_k = a_K = \prod_{j=1}^{K}\frac{j-d}{j} = \prod_{j=1}^{K}\Big(1 - \frac{d}{j}\Big).
$$

For $d \in (0,1)$ every factor lies strictly between 0 and 1, so the product is positive. Its logarithm is at most $-d\sum_{j \le K} 1/j$, which goes to $-\infty$ like $-d\ln K$, so the product goes to zero. The Gamma-function form gives the rate, $K^{-d}/\Gamma(1-d)$: at $K = 280$ that is 0.0705 against an exact 0.0705. For (c), apply the Spec's rule, embargo $\ge \max(h, \text{longest feature lookback, FFD window included})$. The warm-up solves $k^{-1.4}/3.72 = 10^{-4}$, which gives $K \approx 281$. In Listing 7.5 a training label is removed when $t_{0,j} \le T_1 + \eta$ and $t_{1,j} \ge T_0$, where $T_1$ is the last test label's *end*. That inequality removes $h + \eta$ formation days after the block. On the time axis alone, the average training share per fold falls from about 66% with the 21-day embargo to about 50% with 281 days, before parent grouping takes its fifth.

**The trap:** In (a), the trap is alternating signs ($+0.12$ for $w_2$), carried over from the binomial theorem. For $0 < d < 1$, every weight after $w_0$ is negative. In (c), the trap is keeping block 5's `embargo=21` because the label horizon is "only" 63 days. The embargo covers the longest *lookback*, not just the label. The other trap is to confuse the two costs. The 280 NaN warm-up rows are paid once per series, at the start. The embargo is paid again after every test fold.

**If you got this wrong, read:** §7.3, "Math, Gently: the dial", "The warm-up cost, computed" and "The Full Derivation: the fractional weights"; §7.7, "The embargo" and Ways This Blows Up item (2); §7.12, the paragraph after block 5 on the `embargo=21` trap.

**Z.07.3: Size Theo's hand**

**Answer:** (a) **Without the meta-model**, Theo makes **+0.10% per trade**, or **+4.0% a year** over 40 trades. **With it**, he makes 15.3 trades at **+1.30% per trade**, for **+19.9% ≈ +20% a year**, from fewer than half the trades. (b) At $p = 0.75$, $z = 0.577$ and the size is **0.44**. At $p = 0.55$, $z = 0.100$ and the size is **0.08**. A 55% read is a tenth of a standard deviation away from a coin flip, so it earns a chip, not a stack. (c) Use **purged, embargoed folds grouped by ultimate parent**, with the unrestricted subsidiaries mapped to their parents. Shuffled K-fold trains on the answer to the test flag.

**How:** For (a), the expected value per trade is precision times the win plus one minus precision times the loss: $0.35(4) - 0.65(2) = 0.10$. The meta-model keeps $0.6 \times 14 = 8.4$ of the 14 winners. At 55% precision that implies $8.4/0.55 = 15.27$ trades, of which 6.87 are losers. It has cut 74% of the losers and 40% of the winners. The year is $8.4(4) - 6.87(2) = 19.85\%$. For (b):

$$
z = \frac{p - \tfrac12}{\sqrt{p(1-p)}},\qquad m = 2\Phi(z) - 1:\qquad
p = 0.75 \Rightarrow \tfrac{0.25}{0.433} = 0.577,\ m = 0.436;\qquad
p = 0.55 \Rightarrow \tfrac{0.05}{0.497} = 0.100,\ m = 0.080 .
$$

Near $p = \tfrac12$ the map is roughly $m \approx 1.6\,(p - \tfrac12)$, so a five-point edge buys about eight points of size, not 55. In Ines's terms, the size is your confidence that you have an edge, not your opinion about the bond. For (c), flags on one parent cluster in time around one corporate event, and the drop-down entity is the same family as the parent. A shuffled split or a ticker split therefore puts the event's neighbours in training. Generate the primary's flags out of sample before you build meta-labels; that is leak (1) in §7.5's list.

**The trap:** In (a), the trap is to keep 40 trades for the meta-model and report $40 \times 1.30 = 52\%$. A filter wins by trading *less*. In (b), the trap is "55% sure, so 55% of a full position", which bets the opinion and not the confidence. In (c), the trap is ticker grouping: the unrestricted subsidiary's flags land in training while the parent's land in test.

**If you got this wrong, read:** §7.5, "The math", the Poker Table box and Ways This Blows Up; §7.7, "The purge, formally" and "Group by parent, not ticker"; §7.5, Quant-Shop Life.

**Z.07.4: Deflate the honest number**

**Answer:** (a) $SR^\ast = 0.230$ a month (0.80 annualized), and the DSR is $\Phi(0.98) = $ **0.84**. (b) With 400 effective trials, $SR^\ast = 0.193$ a month (0.67 annualized) and the DSR is $\Phi(1.49) = $ **0.93**: better, and still short of 95%. (c) The MinTRL is $T^\ast \approx$ **292 months, about 24.4 years**. TRACE dissemination has run about 291 months (July 2002 to October 2026), and Kaz has 240, so Kaz is roughly four years short. (d) The DSR corrects for selection *across* trials. An in-sample Sharpe also contains overfitting *within* the trial. Deflate only return series that are already out of sample.

**How:** Here $V = 1/240$, so $\sqrt V = 0.0645$. For $N = 3{,}000$ the quantiles are $\Phi^{-1}(1 - 1/3000) = 3.403$ and $\Phi^{-1}(1 - 1/(3000e)) = 3.667$. The bracket is $0.423(3.403) + 0.577(3.667) = 3.555$, so $SR^\ast = 0.2295$. The shape term is $1 - (-0.5)(0.30) + \tfrac{5-1}{4}(0.30)^2 = 1.24$, with square root 1.114. Then

$$
\widehat{\text{DSR}} = \Phi\!\left[\frac{(0.30 - 0.2295)\sqrt{239}}{1.114}\right] = \Phi(0.979) = 0.836 .
$$

Against zero, the same number gives $\Phi(4.17) = 0.99998$, which is the naive report. For $N = 400$ the quantiles are 2.807 and 3.115, the bracket is 2.985, and $SR^\ast = 0.1927$, so $z = 0.1073 \times 15.46/1.114 = 1.49$. A Monte Carlo of the maximum of 400 and 3,000 standard normals, scaled by $\sqrt V$, gives 0.192 and 0.229, so the formula is accurate here. For (c):

$$
T^\ast = 1 + 1.24\left(\frac{1.645}{0.30 - 0.1927}\right)^2 = 1 + 1.24 \times 235.0 = 292 .
$$

For (d), the 2.9 is annualized, or 0.84 a month. Fed into the formula, it returns a DSR of $\Phi(6.5) \approx 1.0000$. The formula happily certifies trees that memorized 47 hats. That is a haircut applied to pro forma EBITDA that already includes the synergies.

**The trap:** The commonest error in (c) is to compute the MinTRL against $SR_0 = 0$: $1 + 1.24(1.645/0.30)^2 = 38$ months, "three years and done". The benchmark that matters is the noise bar, not zero. In (a) and (b), the traps are mixing units (an annualized 0.80 bar against a monthly 0.30 Sharpe) and plugging in excess kurtosis (2) where the formula wants raw kurtosis (5). In (b), expect less than you might from clustering. Cutting $N$ by a factor of 7.5 lowers the bar by only 16%, because $SR^\ast$ grows like $\sqrt{2\ln N}$.

**If you got this wrong, read:** §7.8, "The Full Derivation: PSR, DSR, MinTRL and PBO", the Paleologo annotation on clustering trials, and Figure 7.5; §7.12, block 6 (the paragraph on handing `deflated_sharpe` only the survivors).

**Z.07.5: The composite is not a clean gap**

**Answer:** (a) $\operatorname{Cov}(\tilde r_t, \tilde r^{\text{gap}}_{t+1}) = \operatorname{Cov}(r_t, r_{t^+ \to t+1}) - \rho\,\sigma_\delta\sigma_{\delta'}$. At $\rho = 0$ the bias is zero. At $\rho = 1$ with equal variances it is $-\sigma_\delta^2$, the full Roll bias of §7.9. On Theo's whiteboard, with equal noise, the fake long–short return is $\rho \times 1.00\%$ a month, so a composite with $\rho = 0.5$ still pays half a point a month out of noise. (b) In fire sales the composite converges slowly and inherits the stale print, so **$\rho$ rises exactly when dispersion is widest and the reversal strategy trades hardest**. Enter at the first executable institutional-size print, or at a dealer level you could actually have hit, and report the premium both ways.

**How:** Write both observed returns in terms of the noise:

$$
\tilde r_t = r_t + \delta_t - \delta_{t-1},
\qquad
\tilde r^{\text{gap}}_{t+1} = r_{t^+ \to t+1} + \delta_{t+1} - \delta'_{t^+}.
$$

Expand the covariance term by term. The true returns are independent of the noise, $\delta_{t+1}$ is a fresh draw, and the composite anchors on the *last* print, not the one before it, so $\operatorname{Cov}(\delta_{t-1}, \delta'_{t^+}) = 0$. The only surviving noise term is $\operatorname{Cov}(\delta_t, -\delta'_{t^+}) = -\rho\,\sigma_\delta\sigma_{\delta'}$. For the whiteboard number, write $\delta' = \rho(\sigma_{\delta'}/\sigma_\delta)\,\delta_t + \text{fresh noise}$. Bond A, marked 0.5% low, then has an expected gap return of $+\rho(\sigma_{\delta'}/\sigma_\delta) \times 0.5\%$, and B mirrors it. A two-million-draw Monte Carlo with $\sigma_\delta = 0.5\%$ and $\sigma_{\delta'} = 0.4\%$ matches $-\rho\,\sigma_\delta\sigma_{\delta'}$ at $\rho = 0, 0.5, 0.9, 1$.

**The trap:** The trap is to believe that any price with a later timestamp is a clean gap. A gap works only when it gives a *different draw* of the noise. A composite anchored on the last print is the same draw, partly re-served. Sign slips are the second trap: $+\rho\sigma\sigma'$ would say that anchoring *hides* reversal, when in fact it manufactures it.

**If you got this wrong, read:** §7.9, Math, Gently on covariance (the mis-zeroed scale), "Latent implementation bias" and "The fix is a gap"; §7.1, "Defect 1: the price is sometimes a rumor" (the SMU Cox study and AI composites); §7.11, Case Study C; §7.10, the Trend Watch entry on Composite+.

**Z.07.6: ROBO and the future**

**Answer:** One version, in 115 words:

> Every feature value carries `available_at`: the moment the desk could first have read it (filing time, release vintage, trade-report time), never the period it describes. Join features to a label formed at $t_0$ by as-of join only: the latest value with `available_at <= t0`. Never forward-fill across a release date and never use revised vintages. Purge training label $j$ if $[t_{0,j}, t_{1,j}]$ intersects $[T_0, T_1 + \eta]$, using the recorded $t_1$. The embargo $\eta$ is at least $\max(h, \text{longest feature lookback, FFD window included})$. Fit every preprocessing parameter ($d^\star$, winsorization cutoffs, scalers) inside the training fold. CI fails the build unless pure-noise features give `auc_shuffled > auc_purged + 0.03` and `|auc_purged - 0.5| < 0.06`.

**How:** Theo's draft names an intention. ROBO needs a mechanism, and the future does not live in a column, so deleting one cannot remove it. It lives in *timestamps*, and each of the five required pieces closes one door the chapter showed being opened. The `available_at` field and the as-of join close the door that Long Scene 1's misdated factor file and Case B's FRED vintages and period-end forward-fill came through. The purge closes the one Kaz's shuffled 1.8 came through, overlapping label windows. The embargo closes the door of trailing-window features formed just after the test span. The FFD window can stretch that lookback to 280 days (Z.07.2). The canary test is behavioural: it fails on what the pipeline *does* with noise, whatever the code looks like. The bonus line, fitting $d^\star$ and the winsorization cutoffs inside the fold, catches the quieter leak of §7.3's Ways box and of Kaz's full-sample winsorization in §7.9.

**The trap:** The commonest wrong answer is a better-worded intention, such as "use only data available at the time", with no field, no join and no test. ROBO will comply with it as literally as it complied with the first draft. The second is to key the join on the date a value *describes* (quarter-end, reference month), which is exactly Case B's leverage figure sitting in the panel forty-odd days before its 10-Q existed. The third is an embargo equal to the label horizon, which forgets the feature lookback.

**If you got this wrong, read:** §7.2, Long Scene 1 and "The one-day placebo"; §7.11, Case Study B; §7.7, "The purge, formally" and "The embargo"; §7.12, block 5; §7.13, "The Spec You Hand the Robot".

## Part III: Isolating Idiosyncratic Alpha (IDO), Factors & Trend

### Z.08 Chapter 8: Stripping Beta to Isolate Pure IDO

Seven exercises. Every number below was recomputed in Python. Exercise 1(b) uses FRED daily data (BAMLH0A2HYB against DGS10, pulled 2026-10-18), and Exercises 3–5 use the Appendix F listings on seed 8 unless stated otherwise.

**Z.08.1: Theo's thirty-seven cents, three ways**

**Answer:** The full analytical hedge is $\text{DV01} = \$40\text{mm} \times 4.1 \times 0.0001 = \$16{,}400$. One TY contract carries $\$63/0.89 = \$70.8$, so $H = 1$ is 231.7 contracts.

- **(a) Ben Dor B, 1998–2009.** $\ell = -19.25$ and $H = -0.19$. That is a *long* of about 45 TY. In practice it means zero futures, because almost no desk buys Treasuries against a B bond.
- **(b) 2026 YTD B.** The Trend Watch's $H = 1.03$ is measured at the B index's own average spread, about 305 bp, and gives 239 contracts short (Table 8.2). Re-evaluated at Theo's 620 bp, with $\rho = +0.022$, $\sigma_s = 1.92\%$ and $\sigma_y = 4.45$ bp, so $\ell \approx +0.94$, it gives $H \approx 1.06$, about 245 contracts short.
- **(c) A 2022-style regime.** $\ell = +10.3$ and $H = 1.64$, about 380 contracts short.

What each hedge assumes about why rates move:

- (a) Rates move on growth scares and Fed easing, so yields fall exactly when spreads widen.
- (b) Rates move on news this bond does not care about.
- (c) Rates move on inflation, which pushes yields up and spreads wider on the same day.

**How:** Everything goes in decimals.

$$
H = 1 + s\,\ell, \qquad \ell = \rho\,\frac{\sigma_s}{\sigma_y} = -0.56 \times \frac{0.022}{0.00064} = -19.25, \qquad H_a = 1 + 0.062 \times (-19.25) = -0.19 .
$$

Contracts are $N = H \cdot \text{DV01}_{\text{target}}/(\text{DV01}_{\text{CTD}}/\text{CF}) = 231.7\,H$. For (b), the Trend Watch gives you $\rho$ and $H$ at the index's average spread but not $\ell$. Back $\ell$ out as $(H-1)/\bar s = 0.029/0.0305 \approx 0.94$, then re-evaluate at $s = 0.062$. Because $H$ is linear in $s$, the regime's tilt away from 1 doubles when the spread doubles. For (c), $\ell = 0.3 \times 0.022/0.00064 = 10.31$.

**The trap:** The most common mistake is to read Table 8.1's B row ($-0.04$) or the Trend Watch's 1.03 as if it were Theo's bond. Both are evaluated at the index's average spread, and the caption under Table 8.2 says so. A second trap is mixing routes. Ben Dor's regression gives $\beta + \gamma s = 0.15 - 0.03 \times 6.2 = -0.04$ at 620 bp, while the two-factor formula the exercise asks for gives $-0.19$. A third is units: typing $\sigma_y = 6.4$ instead of $0.00064$ gives $\ell \approx -0.002$ and $H \approx 1$, which puts you at the "nobody" table by unit error.

**If you got this wrong, read:** §8.2, "The two-factor derivation" and "Three regimes", then the Trend Watch table; §8.6, the Veronesi extraction on futures sizing, and Table 8.2.

**Z.08.2: Kaz's fulcrum**

**Answer:** $\lambda = c/R = 0.07/0.35 = 20\%$ a year. Check: $H^{\text{rec}} = 0.07/(0.07 + 0.20 \times 0.35) = 0.07/0.14 = 0.5$. The sentence for Kaz: *the fulcrum's value is the recovery itself, a share of the reorganized company that the plan values off enterprise value and not off any Treasury curve, so for that class $\lambda$ is effectively infinite, $c/(c + \lambda R)$ goes to zero, and a ratio of one-half belongs to a bond that still collects about half its value as coupons.*

**How:** Set the ratio to one half and solve:

$$
\frac{c}{c + \lambda R} = \frac12 \;\Longrightarrow\; c + \lambda R = 2c \;\Longrightarrow\; \lambda = \frac{c}{R} .
$$

Notice that $r$ drops out. $H^{\text{rec}}$ depends only on how the bond's value flow splits between coupons and expected recovery. At $\lambda = 20\%$ (with $r = 4\%$, say) the bond is a stressed credit, not a fulcrum: $P = 0.14/0.24 = 58.3$, $y = 12\%$, a screen duration of 8.3 years against a true 4.2. Push the clock harder and the ratio falls: 0.17 at $\lambda = 100\%$ and 0.04 at $500\%$. In the limit $P \to R$ whatever $r$ is, which is "trades on dollar price."

**The trap:** One mistake is inverting to $\lambda = R/c = 500\%$. The subtler one is believing Kaz's earlier line that the ratio "goes through zero" at the fulcrum. Since $c/(c + \lambda R) > 0$ for every finite $\lambda$, the recovery route only *approaches* zero. A negative hedge ratio needs the correlation route. Calling $H = 0.5$ "half bond, half equity, so it must be the fulcrum" mixes up the bond whose value is split with the class whose whole value *is* the recovery.

**If you got this wrong, read:** §8.3, "Two routes to zero duration" and "The Full Derivation: the recovery route" (Figure 8.2).

**Z.08.3: When Scholes–Williams is enough**

**Answer:** With $\theta = (\theta_0, 1-\theta_0)$ and a serially uncorrelated factor, the three slopes converge to $b_{-1} \to 0$, $b_0 \to \theta_0\beta$ and $b_{+1} \to (1-\theta_0)\beta$, while $\rho_f \to 0$. So $\hat\beta_{\text{SW}} \to \beta$ exactly. Under $\theta = (0.5, 0.3, 0.2)$, $\hat\beta_{\text{SW}} \to 0.8\beta$: a bias of $-0.2\beta$ ($-20\%$), which is the third envelope that Scholes–Williams never opens. The code prints SW/true $= 0.810$. The extra 0.01 is sampling noise. The raw slopes are $-0.002$, $0.494$ and $0.279$, which sum to $0.771$, and dividing by $1 + 2\hat\rho_f = 0.952$ gives $0.810$. Here $\hat\rho_f = -0.024$ is sample noise, since the true value is 0. Figure 8.3's "0.52 rather than 0.49" is the same division.

**How:** Write $r^o_t = \theta_0 r_t + \theta_1 r_{t-1}$ with $r_t = \alpha + \beta f_t + \epsilon_t$. Then $\mathrm{Cov}(r^o_t, f_{t-k}) = \theta_k\beta\sigma_f^2$ for $k = 0, 1$. For the lead $k = -1$ the covariance is zero, because $f_{t+1}$ is independent of everything dated $t$ or earlier. Each univariate slope is that covariance over $\sigma_f^2$, so

$$
\hat\beta_{\text{SW}} \xrightarrow{p} \frac{0 + \theta_0\beta + (1-\theta_0)\beta}{1 + 2\cdot 0} = \beta .
$$

With a second lag the numerator becomes $(\theta_0 + \theta_1)\beta = (1 - \theta_2)\beta = 0.8\beta$. In general Scholes–Williams recovers one lag's worth of news, and Dimson with $L \ge q$ recovers all of it (1.005 in the printout).

**The trap:** Blaming the denominator. With $\rho_f = 0$ it is 1, and the whole bias is the lag the estimator never looks at. The lead term is there for a *stale factor*, so it cannot mop up a stale bond's second day. The opposite mistake is to read 0.81 as the theoretical value. The population answer is 0.80, and the printout sits 0.01 away because of a sample autocorrelation that should have been zero.

**If you got this wrong, read:** §8.5, "The Full Derivation: Scholes–Williams and Dimson under a smoothing model", and Figure 8.3.

**Z.08.4: The regime-switching robot**

**Answer:** These figures are for the listing's bond at 6% and $D = 4$.

- **Population hedge ratios.** $H = 0.20$ in the first half ($\rho = -0.4$) and $1.60$ in the second ($\rho = +0.3$). The pooled $\rho \approx -0.05$ puts the full-sample $H$ near 0.90.
- **On the listing's seed.** The regression gives 0.95 for the full sample, 0.21 for the first half and 1.64 for the second.
- **How badly the full-sample number hedges.** Hedged at 0.95, the first half's variance is 15.5% above that half's best hedge. That is worse than no Treasury hedge at all, which costs only 1.3%. The second half's variance is 14.6% above its best.
- **Rolling 60-day $H$.** On seed 8 it first touches 1 on day 30 after the switch, dips back, and stays above 1 from day 43. Across 500 seeds the median first crossing is day 35 (interquartile range 27–42, 5th–95th percentile 16–51), close to the back-of-envelope figure of 34.

**How:** In the setup block of Listing 8.3 (Appendix F), make `RHO` a vector, $-0.4$ for $t < 1250$ and $+0.3$ after. Then build $x_t = \ell_t\,\Delta y_t + \sigma_s\sqrt{1-\rho_t^2}\,z_t$ and refit `empirical_duration` on each half and on the whole sample. The hedged return is $R + H D\,\Delta y$. Its excess variance over a half's best hedge is $(D\sigma_y)^2(H - H_{\text{half}})^2$. With $D\sigma_y = 0.0024$ and a gap of about 0.7, that comes to $3\times10^{-6}$ against a spread-driven base near $2\times10^{-5}$, which is the 15%. For the window, use equal volatilities and let $k$ days of the new regime sit inside 60:

$$
\rho_{\text{roll}}(k) \approx \frac{(60-k)(-0.4) + k\,(0.3)}{60} = 0 \;\Longrightarrow\; k = \frac{24}{0.7} \approx 34 \text{ trading days.}
$$

The link to Case Study C: April 2025 flipped the sign twice in seven sessions. A 60-day window needs about seven weeks to cross 1, so it could not see a regime that lasted three days. It moved only after the event (the CCC rolling $H$ hit $-0.78$ on May 23). That is why the desk's answer was to lower its confidence in $H$, by raising $\eta$, widening the no-trade band and leaning on CDX, rather than to re-estimate harder.

**The trap:** Thinking "0.95 is close to 1, so the full-sample number is a fair compromise." It is close to 1 only because a flight table and an inflation table cancel into something that looks like the nobody table. It hedges each half worse than that half's own number, and the first half worse than not hedging. The second trap is treating the first noisy touch of 1 as detection. On seed 8, the estimate prints 1.05 on day 30, falls back to 0.88 by day 36, and only commits on day 43.

**If you got this wrong, read:** §8.2, "Three regimes"; §8.7, Case Study C and Figure 8.4; §8.9, the notes on Listing 8.3 and the closing "Ways This Blows Up".

**Z.08.5: The duration-hedged future as a sixth column**

**Answer:** We built the product as an HY index return (HYG's loadings, its own 5 bp/day tracking noise, no ETF basis) plus a short TY overlay at a fixed $H = 1$ *(illustrative methodology)*. What is left is $-0.11\,x + \text{noise}$, a near-twin of CDX (correlation 0.96). On the listing's seed:

- **Condition number and penalty.** Raw $\text{cond}(C)$ goes from $9.2\times10^{6}$ to $1.2\times10^{7}$. It barely moves because the HYG–JNK twin already sets the smallest eigenvalue. The penalty $\eta$ needed to cap it at 50 rises from 0.059 to 0.074.
- **CDX weight.** Under ridge it falls from 1.10 to 0.67 while the new column takes 0.72. Under OLS it falls from 1.50 to 0.98, and the drift in the OLS weights between the two halves of the sample rises from 12.3 to 32.9.
- **Out-of-sample hedged variance.** It goes from 0.364 to 0.358 of unhedged, which is no real gain.
- **With JNK removed the effect is clean.** $\text{cond}(C)$ goes from 25 to 82, $\eta$ from 0 to 0.025, and the CDX weight from 1.50 to 0.82.
- **If the product is literally $\text{HYG} - (3.2/6.5)\,\text{TY}$.** $C$ is singular ($\text{cond} \approx 10^{16}$), and OLS posts $-4.7$ in the product against $+3.6$ in HYG.

**How:** Append the column to `R_H` in Listing 8.6 (Appendix F), drawing its noise from a separate generator so the listing's own draws do not change, then rerun `hedge_matrix`. Everything the product holds lies close to the span of the existing columns $\{\text{CDX}, \text{TY}, \text{HYG}\}$. Ridge therefore splits one job, the spread hedge, between two near-substitutes, and the CDX weight stops meaning "the spread-beta hedge." Note also that a fixed $H = 1$ overlay makes the product rate-neutral only on paper. In this flight-table simulation ($\rho = -0.4$), its spread leg moves with yields, so its empirical duration is $-1.5$ years.

A fixed-$H$ product is worse than building the hedge yourself in four cases:

- **Your objective is `min_total_variance` and $\rho$ is far from zero.** Here the book's minimum-variance $H$ is 0.2. The product imposes 1, so you buy TY back to undo it and pay two bases for nothing. Product plus TY leaves 0.382 of variance out of sample, against 0.361 for CDX plus TY.
- **Its index is not your book.** An index at about 300 bp of very liquid names is not Theo's 620 bp B3.
- **It is small and its overlay runs on its own clock.** HYGH has about \$652mm against \$17.2bn for HYG, and the overlay rebalances on the methodology's schedule, not yours.
- **The regime moves and the methodology does not.**

The product is *not* worse when your objective is `zero_rates_zero_spread`, your book looks like its index, and your mandate rules out futures. In that case it is Theo's two-instrument hedge, sold pre-assembled.

**The trap:** Assuming that more instruments make a better hedge. The sixth column adds collinearity, not information. The CDX weight falls because ridge shares one job between twins, not because CDX became a worse hedge. The other trap is reading "duration-hedged" as "rate-neutral." $H = 1$ is a bet that $\rho = 0$, which is the nobody table.

**If you got this wrong, read:** §8.6, "Math, Gently" (the condition number), "The Full Derivation: minimum variance, ridge, and hedging less", and the Trend Watch "Listed Credit Beta and the Duration-Hedged Index Family"; §8.8 on the two-instrument hedge.

**Z.08.6: ROBO and the flat line**

**Answer:** The sentence: *"For an IDO book the OBJECTIVE is `zero_rates_zero_spread`: size every hedge from a named exposure (TY from DV01 at $H = 1$, CDX HY from $\text{DTS}_{\text{book}}/\text{DTS}_{\text{CDX}}$), never from a regression of the book's own P&L on the hedge instruments, because whatever that regression leaves behind is the thing we are paid for."* The test: plant a known IDO stream in a synthetic book and assert that the hedge leaves it intact.

**How:** First notice that \$38mm of HYG against \$40mm of the cold-open bond matches no named exposure. A rates-neutral HYG hedge is $40 \times 4.1/3.20 = \$51.3$mm. A DTS-neutral one is $40 \times 0.248/(3.20 \times 0.0284) = \$109$mm. A size that matches neither is a statistical fit, and a fit to the book's own P&L removes whatever moved with HYG in the sample, the view included (Ines's napkin, §8.2).

The test, written in prose:

1. Simulate 2,500 days of a book whose return is $-4.1\,\Delta y - 0.248\,x$ plus a planted IDO of 30 bp a day.
2. Fit the engine on the first 2,000 days and score it on the last 500.
3. Assert that each hedge notional is within 5% of its exposure-implied size.
4. Assert that, out of sample, the hedged P&L correlates above 0.9 with the planted IDO.
5. Assert that hedged variance is at least 0.9 times the planted IDO variance. A hedged book quieter than its own idio has hedged away the alpha.

We ran it: the exposure-sized two-instrument hedge scores a correlation of 0.96 and a variance ratio of 1.07, so it passes. A flat line fails the variance-floor assertion by construction. Running Listing 8.7's planted-IC ledger on the *hedged* P&L is the same test in IC units.

**The trap:** Writing a better version of the bad objective, such as "minimize variance, but cap the hedge at 1×." The fix is to *name* the objective, which is why §8.10's spec makes OBJECTIVE a required field with no default. The matching test-writing trap is asserting that hedged variance went *down*. That is the test ROBO's flat line passes with honours.

**If you got this wrong, read:** §8.9, "Specification for AI Implementation" (what ROBO built); §8.10, "The Spec You Hand the Robot" (OBJECTIVE and TESTS); §8.2, the Poker Table and the Ben Dor p.219 extraction; §8.8, "The IDO ledger: proving it".

**Z.08.7: The crate, at book scale**

**Answer:**

- **(a)** \$400k if the residuals are independent; \$800k at a correlation of 0.2.
- **(b)** 80%.
- **(c)** A minimum-variance hedge removes $0.5^2 = 25\%$ of the component, leaving the book's idio volatility at about \$716k.

**The two legs:**

- Short HYG, with the shares borrowed.
- Sell CDX HY protection sized to the same DTS, so market beta cancels.

Add TY futures to take out HYG's rate duration. The package is short cash bonds and long the contract: short the price of *holding paper*, which is what the pairs are long.

**What leaks:**

- The ETF's premium or discount to NAV (3–5% below NAV for the big credit ETFs on 12 March 2020).
- The CDX–cash basis and the 20 March / 20 September roll.
- The borrow, both its fee and the risk of recall.
- Three quarters of the component, which the package never touches.

**How:** In units of \$100k, so that the variance units are $(\$100\text{k})^2$:

$$
\sigma^2_{\text{book}} = N\sigma^2\,[1 + (N-1)\rho] = 16\,[1 + 15 \times 0.2] = 64, \qquad \text{common share} = \frac{N\rho}{1 + (N-1)\rho} = \frac{3.2}{4} = 0.8 .
$$

With $\rho = 0$ the variance is 16, giving \$400k, and 64 gives \$800k. In the one-factor reading the book's common component has variance $N^2\rho\sigma^2 = 51.2$ out of 64. A proxy that correlates $\rho_h = 0.5$ with the component removes $\rho_h^2$ of the component's variance, $0.25 \times 51.2 = 12.8$. That leaves $64 - 12.8 = 51.2$, and $\sqrt{51.2} = 7.155$, so \$716k. A 200,000-draw simulation returns \$800k, 0.80, \$716k and 24.9%.

**The trap:**

- **(a)** Adding the vols to get \$1.6mm. That assumes a correlation of 1, not 0.2.
- **(b)** Answering 20%, or answering 75% by counting only the off-diagonal covariance, $48/64$. The common factor lives on the diagonal too: $0.2 \times 16 = 3.2$ of the 16.
- **(c)** Either "a correlation of 0.5 removes half," or taking 25% off the *whole* book, $\sqrt{48} \to \$693$k. The hedge only acts on the common part.

**If you got this wrong, read:** §8.8, "The common whisper, at book scale" (Twelve Residuals: the same arithmetic at 12 pairs and 0.28); §8.6, "Why you hedge less than the naive amount".

### Z.09 Chapter 9: Factor Investing in Corporate Credit

Seven exercises. Every number below was recomputed in Python; the lab exercise was run on the Appendix F listings with the extension described in its solution.

**Z.09.1: Kaz's hedge, two ways**

**Answer:** (a) Dollar-neutral beta $= (12 - 7.2)/8 = 0.6$. DTS-neutral short notional $= 100 \times 12/7.2 = \$166.7$mm per \$100mm long. (b) Net carry $= 3.0\% \times \$100\text{mm} - 0.9\% \times \$166.7\text{mm} = \$3.0\text{mm} - \$1.5\text{mm} = +\$1.5$mm a year, or 150bp on the long notional. You have built a short-duration (low-risk) factor, not a value or carry factor.

**How:** Beta is a ratio of DTS numbers, (9.1), so the dollar-neutral book's beta is the DTS gap over market DTS. Matching DTS means scaling the short leg by $12/7.2 = 1.667$. For carry, use (9.4): per unit of DTS, carry is $1/D^{\text{spr}}$. Both legs carry the same DTS, 12, so

$$
\text{net carry} = \text{DTS}^{\ast}\left(\frac{1}{D^{\text{spr}}_L} - \frac{1}{D^{\text{spr}}_S}\right) = 12\left(\frac14 - \frac18\right) = 1.5\%.
$$

The spreads cancel, and only the durations survive. In §9.2.3 the carry was zero because the legs had the same duration. Here the long leg is a 4-year bond and the short leg is an 8-year bond, so the 1.5% is what the market pays you for being short the long end of the credit curve. The book has no beta to the index, but it is a duration bet: it gains when long-dated spreads widen more than short-dated ones and loses when they tighten more.

**The trap:** One common wrong answer is 2.1% ($3.0\% - 0.9\%$), which is the carry of equal dollars and forgets the short leg's 1.667 scaling. The other is 0%, copied from §9.2.3 without noticing that the durations now differ. A third mistake is calling the 1.5% "value" or "carry alpha". By (9.4) it is the duration premium, and the box after (9.4) says to rename it before compliance does.

**If you got this wrong, read:** §9.2.2–§9.2.3 for the beta and the scaling, and §9.5.1 for (9.4) and why carry turns into a duration factor.

**Z.09.2: Can you afford it?**

**Answer:** Break-even round-trip cost $c^\ast = (3.0\%/12)/0.40 = 0.625\%$. **Investment grade: it survives, barely.** The cost is $0.40 \times 0.608\% \times 12 = 2.92\%$ a year, which leaves +0.08% (8bp) net. **High yield: it fails.** The cost is $0.40 \times 0.941\% \times 12 = 4.52\%$ a year, which leaves −1.52% net. The high-yield turnover cap is $\text{TO}^\ast = (3.0\%/12)/0.941\% = 26.6\%$ a month. At that cap the cost equals the full 3.0% gross, so a buffer has to cut turnover by a third **without giving up any gross return** just to break even. More generally, the buffer can give up at most 11.3bp of annual gross return for each point of monthly turnover it removes.

**How:** Use (9.3), $\mathbb{E}[r^{\text{net}}] = \mathbb{E}[r^{\text{gross}}] - \text{TO}\cdot c$, with $\text{TO}$ the one-way monthly turnover and $c$ the round-trip cost. A liquidity cost score is a round-trip cost (§9.8.2), so it goes straight into $c$. Put everything in monthly units: gross is $3.0\%/12 = 0.25\%$ a month. The IG bill is $0.40 \times 0.608\% = 0.243\%$, so IG clears by 0.007% a month. The HY bill is 0.376%, so HY falls short by 0.126%. Invert (9.3) for the cap: $\text{TO}^\ast = 0.25\%/0.941\% = 26.6\%$. A buffer that trades turnover for gross return keeps the strategy alive only while

$$
G(\text{TO}) \;>\; 12 \times 0.941\% \times \text{TO} = 11.3\% \times \text{TO}.
$$

Barclays' buffers cost roughly a seventh of the gross IR (1.52 to 1.31, §9.8.3). Take 3.0% down by a seventh to about 2.6%, and the turnover has to fall to about 23% a month, not 26.6%.

**The trap:** One mistake is treating the LCS as a one-way cost and charging $2 \times \text{TO} \times \text{LCS}$. That gives an IG cost of 5.8% a year and the wrong verdict, "neither". The other is comparing the 3.0% annual gross with the 0.24% monthly bill and declaring victory in both markets. Also, do not read the IG result as comfortable. Eight basis points a year is well inside the error in any cost model, and it disappears in any month when costs rise above their average (§9.8.3, Trend Watch).

**If you got this wrong, read:** §9.4.2 for (9.3) and the taxi-meter box, §9.8.2 for what an LCS measures, and §9.8.3 for buffers.

**Z.09.3: The measure trap**

**Answer:** $\text{PD}^{\mathbb{Q}}_3 = 3.54\%$, so the fair spread **with** the $\mathbb{P}\to\mathbb{Q}$ step is **72bp** (71.6). **Without** it, the fair spread is **20bp** (20.1). At 65bp the bond is **not cheap**: it is about 7bp rich. A desk that skipped the step sees it as **45bp cheap**, and every other bond looks cheap to that desk too.

**How:** Turn the physical PD into a distance, shift it by $\theta\sqrt{T}$, and turn it back, following (9.2):

$$
N^{-1}(0.01) = -2.326, \qquad \theta\sqrt{T} = 0.3\sqrt3 = 0.520, \qquad \text{PD}^{\mathbb{Q}}_3 = N(-1.807) = 3.54\%.
$$

Then apply the recovery-of-Treasury fair spread from the derivation in §9.3.3:

$$
s^{\text{fair}} = -\tfrac13 \ln(1 - 0.0354 \times 0.6) = 71.6\text{bp}, \qquad s^{\text{fair}}_{\mathbb{P}} = -\tfrac13 \ln(1 - 0.01 \times 0.6) = 20.1\text{bp}.
$$

The market spread is a $\mathbb{Q}$ price, so it has to be compared with the $\mathbb{Q}$ fair spread: $65 - 72 = -7$bp. The 52bp gap between the two fair spreads is the credit risk premium. The desk that skipped the step counts it as alpha.

**The trap:** "65 is more than 20, buy." That is the measure trap itself. It shows every bond cheap by roughly the risk premium, so the desk ends up buying the index (§9.3.3). The quieter mistakes are using $\theta T$ instead of $\theta\sqrt{T}$, which gives a shift of 0.9, $\text{PD}^{\mathbb{Q}} = 7.7\%$ and a fair spread of 157bp, and forgetting to multiply by the 0.6 loss.

**If you got this wrong, read:** §9.3.3, both the gloss before (9.2), which works the same steps at 1% and four years, and the full derivation. Then read Chapter 6, §6.3, for why $\mathbb{Q}$ shades the odds toward default.

**Z.09.4: ROBO literalism**

**Answer:** Here are three literal builds that satisfy the sentence and lose money.

1. *"Cheap" read as "wide".* ROBO buys the widest-spread decile and shorts the tightest, dollar-neutral. That is the cold-open book: a beta of 0.6 and carry on borrowed beta (§9.2.2). The long leg is also where the next defaults sit, and in the lab 19% of ESP's cheapest decile carries the hidden priming risk, against 5% of the universe (Listing 9.3 output). The book loses in the first selloff.
2. *The Treasury build.* ROBO reads "cheap" as a low dollar price, "avoid momentum crashes" as "hold nothing whose spread can gap", and "keep costs low" as "trade the asset with the lowest LCS" (Treasuries, 0.028%, §9.8.3 Trend Watch). It fills the book with deep-discount, low-coupon long Treasuries. All three clauses are satisfied, and the result is a long-duration rates book inside a credit mandate. In a 2022-style year (the Aggregate fell over 13%, §9.5.3) it loses double digits. The quieter version parks residual weight in bills and runs an unhedged duration gap nobody wrote down.
3. *The crash rule that is itself the crash.* ROBO "avoids momentum crashes" with a stop-loss that liquidates the sleeve after a drawdown and buys back after the rebound. It "keeps costs low" by pricing every trade at last year's average LCS. That is two round trips at stressed prices in exactly the month when immediacy is most expensive (March 2020, §9.10), plus the missed recovery.

**How:** Each failure comes from a word without a unit, a time stamp or a boundary. Here is the rewrite (§9.2.3 and §9.12 hold the full versions):

1. *Universe:* index corporates at the start of month $t$. Bonds above 1,000bp OAS leave DTS scaling and are sized on price and recovery. Residual weight sits in Treasuries matched to the benchmark's key-rate durations, never bills, and returns are excess returns over duration-matched Treasuries.
2. *Cheap:* the ESP residual of log OAS (OAS, never Z-spread) on rating × sector × maturity intercepts and three ratios lagged at least 3 months. Cells under 30 bonds pool with the adjacent rating, residuals are winsorized at 1/99, and negative EBITDA is set to 15× before the 0.1× floor. The signal uses a start-of-month composite mid, and returns use executable levels or a one-month skip.
3. *Momentum and crashes:* EMC over 1, 3 and 6 months, with no stop-loss. Crash protection is structural: DTS-neutral legs at 12 (years × %) per leg in each rating × sector cell, from start-of-month DTS, re-neutralized whenever a leg's DTS drifts more than 10% from target.
4. *Costs:* one-way cost $c_i = \text{LCS}_i/2$ from today's LCS, scaled up for non-standard tickets. One-way turnover $\tfrac12\sum_i|\Delta w_i| \le 10\%$ a month, entry at the 90th percentile and exit below the 80th, with no ticket below the desk minimum.
5. *Acceptance:* report gross, cost, net, turnover and beta, with $|\beta| < 0.10$. Anything unspecified: stop and ask.

**The trap:** The usual failure is a rewrite that only adds adjectives ("truly cheap", "low-cost execution"). A spec is fixed only when every noun has a unit (years × %, decimal OAS, fraction of value), every number has a time stamp (start of month, lagged a quarter), and every rule has an edge case (thin cells, distressed names, defaults). Being "more careful" is not a fix.

**If you got this wrong, read:** the Spec You Hand the Robot box in §9.2.3 (ROBO's two-year Treasuries), the 2022 replay in §9.5.3 (the bills), the March 2020 replay in §9.10, and the full spec in §9.12.

**Z.09.5: Extend the lab**

**Answer:** The signal built from bond prices is the one the noise moves, by roughly sixty times as much as the equity-data signal. With the independent errors of Listing 9.7, though, the noise moves it **down**, not up. In my run (lab noise of 0.4% for IG and 1.2% for HY, DTS-neutral deciles) bond momentum went from +0.05% a year ($t = 0.2$) on clean prices to −5.4% a year ($t = -17.6$) on noisy ones, a gap of −46bp a month. The equity-short-interest signal went from 2.71% to 2.80% a year, a gap of +0.7bp a month, with $t$ unchanged at 6.3. The pure Blume–Stambaugh level term ($\sigma_u^2$, at most 1.4bp a month here) is the only bias ESI carries. It is tiny, and it nets to near zero across legs for both signals.

**How:** This builds on Listing 9.7, with signals in the style of Listing 9.3 and the Listing 9.2 engine. I planted the ESI link in `simulate` by adding $+0.01\,w_{j,t-1}$ to the issuer residual, with $w$ drawn from its own seed. I observed ESI at the start of month $t$ as $0.02 + 0.01\,\text{rating} + 0.01\,w_{j,t} + \text{noise}$ and traded it z-scored within rating, short the high-SI names. Bond momentum is the sum of the last six months' returns, computed from the same price series (clean or noisy) on which it is graded. On noisy prices the six-month sum telescopes:

$$
\textstyle\sum_{k=0}^{5}\tilde r_{t-k} \;\approx\; \sum_{k=0}^{5} r_{t-k} \;+\; u_t - u_{t-6}, \qquad \tilde r_{t+1} \;\approx\; r_{t+1} + u_{t+1} - u_t ,
$$

so the latest mark error enters the signal with a plus sign and the next return with a minus sign. By §9.9's Mechanism 2 that contributes $-\sigma_u^2$ to the covariance: the "winners" are partly bonds marked too high, and they give the error back. Skip a month and the shared price disappears (gap +0.3bp a month). ESI comes from the equity market, so its errors are independent of the bond marks. Noise in the returns then adds variance but no covariance with the signal, and the only bias left is the $\sigma_u^2$ level term weighted by how differently noisy the two legs are.

**The trap:** "Bond momentum is inflated, because noise makes everything look better." Under independent errors the shared price makes momentum look *worse*, the mirror image of how it manufactures short-term reversal. A second trap is calling ESI immune. Its returns are still measured on bond marks, and when I made the marks stale instead of noisy (not updated with probability 0.2 in IG and 0.5 in HY), ESI's gross fell from 2.71% to 1.78% a year. Stale marks book the planted widening after the position has rotated out. Bond momentum fell further still, to −6.6% a year.

**If you got this wrong, read:** §9.9, Mechanisms 1 and 2 and the Full Derivation, then §9.11 on Listing 9.7, including its paragraph on why stale marks are not cleared by a one-month skip.

**Z.09.6: First-day declaration**

**Answer:** A declaration the Ad Hoc Group of Replicators cannot pick apart has three sections, and each claim in it carries a number or a test.

1. *Cause of distress.* (i) Timing. Two of the four published factor series led returns by a month and a third lagged, and an after-the-fact filter capped losses. The paper was retracted in December 2023 (§9.9; Chapter 7). (ii) Noisy month-end marks. Each mark adds $\sigma_u^2$ to average returns, which is 9bp a month (about 1.1% a year) at $\sigma_u = 3\%$, by (9.6). Signals and returns that share a price also manufacture reversal and "value" from the mark error alone. (iii) Filters that peek and defaults that vanish, which remove exactly the left tail that value and carry portfolios hold. (iv) False discovery. Only 23% of significant literature factors keep a significant alpha in a clean framework (Dick-Nielsen, Feldhütter, Pedersen and Stolborg), and 25 of the 26 survivors of the 2026 audit are within-firm sorts.
2. *DIP financing (the clean data).* Open Bond Asset Pricing's cleaned TRACE panels, its corrected Bai–Bali–Wen factors and its duration-matched Treasury returns, pinned to a release (v4.2.1). Point-in-time fundamentals stamped with `available_at` and lagged at least a quarter. Composite mids for signals, and executable levels (or a skip month) for returns.
3. *Plan of reorganization (the five rules).* Signal and return never share a price. No ex-post filters: cleaning rules are written before any return is seen, and outliers are reviewed by a person. Defaults stay in: recovery minus last price in the default month, and the bond leaves the panel the next month, never retroactively. Double-sort on DTS or rating. Replicate in CI: the four corrected factors are rebuilt nightly to four decimals, and every candidate passes the placebo (in the lab, a lag-one reversal must show $t > 5$ and its skip-month twin a $t$ near zero).

**How:** Write it the way a first-day declaration is written. Each cause names a mechanism and its size. The financing names a source, a version and a timing convention. Each plan provision is paired with the cause it cures: rule 1 cures (ii), rule 2 cures (i) and (iii), rule 3 cures (iii), rule 4 cures the cold open's beta, and rule 5 makes the whole plan auditable. One page is enough if every sentence carries a number or a test.

**The trap:** "Data quality issues were identified and have been remediated" is the answer the Group objects to, and it will win. A vague cause cannot be matched to a cure. The second trap is declaring the whole estate worthless. The survivors (equity-derived signals, value on clean prices with DTS control, and low-risk) are the reorganized company, and the plan should name them.

**If you got this wrong, read:** §9.9, Mechanisms 1–3 and the red build with Kaz's whiteboard, then Chapter 7, §7.11, for the retraction itself.

**Z.09.7: The second x-ray**

**Answer:** (a) Without value, $\text{BR}_{\text{eff}} = 12/(1 + 11 \times 0.25) = 3.2$. With value, $12/(1 + 11 \times 0.15) = 4.5$. (b) Idio share $= 1 - 0.6^2 - 0.20 = 0.44$. (c) Borrow costs $\$300\text{mm} \times 1.00\% = \$3.0$mm a year. Rebalancing costs $2 \times \$300\text{mm} \times 5\% \times 0.8\% \times 12 = \$2.9$mm a year. That is **\$5.9mm a year** to give away a \$4mm premium, so the hedge loses. **Shrink** the pairs where value is incidental, and **admit** the ones whose thesis is cheapness. For the hedge to win, the cheap quintile's borrow fee would have to fall below about **37bp**, roughly what the rich, liquid shorts cost (§9.7.2), or someone would have to list an instrument that is mostly value.

**How:** Treating the twelve pairs as one issuer-like cluster, §9.7.2's formula has $N = \bar n = 12$, and naming value buys about 1.3 extra hats. For (b), a loading on unit-volatility series is a correlation, so its variance share is the square: $0.6^2 = 0.36$. Then $1 - 0.36 - 0.20 = 0.44$. For (c), use the chapter's turnover convention. One-way turnover of 5% means selling 5% and buying 5% of each side, so each side pays $5\% \times$ the round trip ($2 \times 0.4\% = 0.8\%$) a month, as in (9.3) and in Wen's own pricing in the scene. The break-even fee comes from

$$
300 \times f + 2.88 = 4.0 \quad\Longrightarrow\quad f = 0.37\%.
$$

Even at a zero fee, the rebalancing alone eats 72% of the premium.

**The trap:** In (b), using the loading without squaring it gives $1 - 0.6 - 0.2 = 0.2$. In (a), dividing by $1 + \bar\rho$ or keeping twelve hats. In (c), charging the 0.4% once on the 5% gives \$1.44mm of rebalancing, \$4.44mm all-in and a break-even fee of 85bp. The verdict survives that reading, but it understates the bill by half. The bigger mistake is reading "hedge" as free because value turns over slowly. The bill is the borrow, because the short leg is the cheapest quintile, the wide, thin end of every cell that nobody lends cheaply.

**If you got this wrong, read:** §9.7.2, "The Pair Book: One View, Twelve Times" (Wen's pricing of the hedge, and the shrink and admit doors), then Chapter 8-D, §8D.2, for why the fee climbs toward the bonds you most want to short.

### Z.10 Chapter 10: Trend-Following & Time-Series Momentum in Credit

Five exercises. Every number below was recomputed in Python. Exercise 5 also runs Listings 10.1–10.6 (Appendix F) on ICE BofA US HY OAS from FRED (`BAMLH0A0HYM2`, the copy pulled for Chapter 8), so the stylized V can be checked against the real tape. Write your card before you read ours.

**Z.10.1: The Crossover hurdle**

**Answer:** $\Delta s^*_6 = 0.03 \times 0.5 / 4.2 = 0.00357$, so about **36 bp** (35.7 bp; 36.2 bp if you accrue a true ACT/360 half-year of 182.5 days). Over six months, iTraxx Crossover has to widen by more than about 36 bp before a 6-month return signal goes short. A smaller widening gives you a chart trending wider and a ledger trending up, and the signal reads the ledger.

**How:** One period's excess return is carry minus duration times the spread change, $r^{ex} \approx s\,\Delta t - D^{\text{spr}}\,\Delta s$. Sum it over the window and ask when the total turns negative:

$$
\Delta s^*_h = \frac{\bar s\,h\,\Delta t}{D^{\text{spr}}} = \frac{0.03 \times 0.5}{4.2} = 35.7\text{ bp}.
$$

For the PM, put a number on it. A 20 bp widening over six months costs $4.2 \times 20 = 84$ bp of mark-to-market and pays $300 \times 0.5 = 150$ bp of carry, so the six-month excess return is $+66$ bp. "Spreads are trending wider" describes the chart. "The signal is long" describes the P&L, and the P&L is still up. The two agree only once the widening passes 36 bp. Strictly, $\bar s$ is the average spread over the window. If 300 bp is where the spread started, the widening lifts the average and the hurdle to about 38 bp. If 300 bp is where it ended, the hurdle is about 34 bp. The 36 bp sits in the middle of that range.

**The trap:** Using the Crossover's 500 bp fixed coupon as the carry gives 60 bp. The carry of index CDS is the par spread, not the coupon, because the upfront amortizes the difference (§10.2.3, Step 2). The second slip is forgetting the half-year and quoting the 12-month hurdle, 71 bp. The third is answering "zero" because you thought in spread changes. That is a different strategy: in Figure 10.1, the spread-change rule is short on 150 days where the return rule is short on 13.

**If you got this wrong, read:** §10.1.2 (the landlord box and the hurdle derivation), then §10.2.3 for why the par spread is the carry.

**Z.10.2: Sheppard's turnover**

**Answer:** $\rho_3 = 2/3$. A flip happens with probability $\arccos(2/3)/\pi = 0.268$, so annual turnover is $2 \times 12 \times 0.268 = 6.43$ units, and at 1.1 bp per unit the bill is **7.1 bp a year per unit of notional**. Costs stay under a tenth of expected return when

$$
\text{SR} \;>\; \frac{10\,c^{\text{tr}}\,\text{TO}}{\sigma_{\text{unit}}} \;=\; \frac{0.71\%}{\sigma_{\text{unit}}},
$$

where $\sigma_{\text{unit}}$ is the annualized volatility of one unit of notional. The 10% target cancels out. At $|w| = 1$, which needs an instrument that already runs at 10% volatility, the bar is **SR > 0.07**. At the 3.9% volatility AQR reports for the quietest CDS indices (§10.6.3), $|w| = 2.6$, the bill is 18 bp, and the bar is **SR > 0.18**. For CDX IG in a calm year, $\sigma_{\text{unit}} \approx 0.23 \times 4.5 \times 1\% \approx 1.0\%$. Then $|w| \approx 10$, which is the leverage cap, the bill is about 68 bp, and the bar is **SR > 0.7**.

**How:** Consecutive 3-month sums share two of their three monthly returns, so $\operatorname{Cov} = 2\sigma^2$, $\operatorname{Var} = 3\sigma^2$, and $\rho_3 = 2/3$. Sheppard's formula gives $\mathbb{P}(\text{flip}) = \arccos(2/3)/\pi = 0.2677$ (a two-million-draw simulation gives 0.2678). Each flip trades two units, and there are 12 decisions a year, so $\text{TO} = 6.43$. The large-$h$ approximation gives 6.24, but $h = 3$ is not large. A sleeve at 10% volatility holds $|w| = 0.10/\sigma_{\text{unit}}$ of notional. Its cost is $7.07\text{ bp} \times |w|$, and its expected return is $\text{SR} \times 10\% = \text{SR} \times |w|\,\sigma_{\text{unit}}$. Require cost $< 0.1 \times$ expected return, and $|w|$ cancels. Two effects push every bar above higher. Volatility scaling trades between flips, because the weight moves whenever $\hat\sigma$ moves. And 1.1 bp is a calm-market cost, while trend's trades cluster in the weeks when bid–offer has gapped (§10.8.1, the annotation).

**The trap:** The tempting move is to compare 7 bp with $\text{SR} \times 10\%$ directly and conclude that any SR above 0.07 will do. That treats the 10%-volatility sleeve as if it held one unit of notional. In CDX IG it holds several units, and every one of them pays the 7 bp. The other slip is counting flips (3.2 a year) instead of units traded (6.4): a flip from $+1$ to $-1$ trades two.

**If you got this wrong, read:** §10.8.1 for Sheppard's formula and the turnover expression, §10.8.2 for the 1.1 bp and the break-even arithmetic, and §10.3.1 for why notional per unit of risk depends on spread times duration.

**Z.10.3: Kaz's runway momentum**

**Answer:** Runway momentum earns a place only if three things hold. (i) The change in the median constituent's runway carries news about CDX HY constituents' default and LMT risk that equity prices have not already absorbed. (ii) That news arrives slowly enough to be a trend at a monthly horizon, rather than a persistent level. (iii) The signal can be built point-in-time from public filings. The test is a monthly regression of next-month CDX HY excess return on the runway signal, with equity momentum, credit's own trend and carry as controls. What decides it is an expanding-window, out-of-sample forecast race against the same model without runway. **The idea dies if the out-of-sample $R^2$ relative to the equity-only model is $\le 0$, or if the Clark–West test fails to reject at 5%.** It also dies if the result disappears when the filing lag is enforced, or if it survives only in 2008 and 2020. Power check: with about 150 out-of-sample months (2014–2026), passing at $t \approx 2$ needs an incremental monthly $R^2$ near 2.6%, a timing Sharpe of about 0.57. So write the kill rule down *before* the run.

**How:** Equity is the first market to price issuer-level news (§10.5.1). The inputs to a runway (cash, revolver availability, burn) arrive in 10-Qs, and the stock reads those filings on the day they are published. So "beyond equity momentum" needs a channel equity misses. The credible candidate is jumps: a runway extension through a priming deal can lift the stock while the excluded debt gaps down (§10.9). Ines has already pointed out that a runway is a memory horizon and not a trend horizon (§10.2.1), so the signal has to be the *change* in runway. With $\widetilde{\Delta R}^{(h)}_t$ the $h$-month change in the median runway, standardized and residualized on equity momentum using only data up to $t$:

$$
r^{\text{HY}}_{t+1} = a + b_R\,\widetilde{\Delta R}^{(h)}_t + b_E\,\text{EMC}_t + b_M\,\operatorname{sign}\!\big(M^{\text{HY},(12)}_t\big) + b_s\,s_t + u_{t+1},
$$

Use non-overlapping months, roll-safe returns (§10.2.3) and HAC errors. Because nobody tries only one runway definition, ask for $t > 3$ on $b_R > 0$. Then run the race. From month 120 on an expanding window, as in Listing 10.5, fit the restricted model ($b_R = 0$) and the full model, forecast $r_{t+1}$, and compare squared errors. Point-in-time means four things: each runway is dated on its filing date, which can be up to 45 days after quarter-end; index membership is taken as of each date, defaulters included; the specification is pre-registered; and no client model enters. That is why the USB stick stays home: Theo's 13-week models are non-public client work, they cannot be reproduced, and none of them existed on the dates the backtest needs.

**The trap:** The usual mistake is to regress CDX HY on runway momentum *alone*, find a $t$ of 2.5, and declare a signal. Any measure of deteriorating liquidity will correlate with equity momentum and with credit's own trend, so the regression has rediscovered both. The second mistake is dating runways at quarter-end instead of filing date, which hands the backtest six weeks of look-ahead, the "tomorrow's newspaper" bug of §10.2.1. The third is to build the median on today's index members: the names whose runway ran out defaulted and left the series, and survivorship deletes exactly the observations the signal exists for. Finally, the median may be the wrong statistic, because index losses come from the tail of the runway distribution. If you switch to the 10th percentile after seeing the results, that is a second hypothesis, and it has to be counted.

**If you got this wrong, read:** §10.5.1 and §10.5.4 for why equity leads and why the residual is the version worth owning, §10.4.2 for estimating on an expanding window and reporting a range, §10.2.1 for the memory-versus-trend distinction, and §10.9 for the jump channel that is the idea's only real hope.

**Z.10.4: The every-other-week bond**

**Answer:** $f(p) = p(1-p)$ has $f'(p) = 1 - 2p = 0$ at $p = \tfrac12$ and $f''(p) = -2 < 0$, so the fake lead peaks there at $\beta^{\text{ce}}/4$. For a bond that prints once every five weeks, $p = 0.2$ and the lead is **$0.2 \times 0.8 \times \beta^{\text{ce}} = 0.16\,\beta^{\text{ce}}$**, which is 0.048 at the box's $\beta^{\text{ce}} = 0.3$. **Filter:** run the regression only on bond-weeks with a print at both $t$ and $t+1$. Then $m_t = P_t$, the stale gap is zero, and the fake lead goes with it. In simulation it fell from 0.048 to 0.001. A version that wastes less data uses trade-to-trade returns: regress each bond's return from one print to the next on the equity return in the week of the earlier print. That keeps every print of every bond, and its lead in simulation is 0.000. Or measure the lead on CDX, where $p \approx 1$.

**How:** The stale gap $G_t = P_t - m_t$ holds this week's equity-driven move whenever the bond did not print, which happens with probability $1-p$. Next week's print collects the gap with probability $p$. So $\operatorname{Cov}(\Delta m_{t+1}, r^{\text{eq}}_t) = p(1-p)\,\beta^{\text{ce}}\operatorname{Var}(r^{\text{eq}})$. Conditioning on $U_t = 1$ sets $G_t = 0$, which leaves $\Delta m_{t+1} = \Delta P_{t+1}$. That is independent of $r^{\text{eq}}_t$ when there is no true lead, and it keeps any lead that is real. The cost is sample size, not universe. A bond with $p = 0.2$ keeps $p^2 = 4\%$ of its weeks under the both-ends filter and $p = 20\%$ under the trade-to-trade version, but no bond is dropped. Report the lead by print-frequency bucket alongside it, as Theo did: an artifact rises as $p$ falls toward $\tfrac12$, and a real lead does not care.

**The trap:** The tempting move is to filter on *bonds* by keeping only the names that print at least weekly. That throws away most of the HY universe, which is exactly the exercise's warning. It also biases the sample toward large, liquid issuers, so any lead you then find is a lead for a different universe. The other slip is to read $p = 0.2$ as "less stale, so less artifact" because it sits further from $\tfrac12$. In fact 0.16 is still about two-thirds of the maximum, 0.25. Infrequent printing does not save you until $p$ is near zero, and by then the bond has no returns to regress.

**If you got this wrong, read:** §10.5.3 (the wall-clock box and the four-line derivation), then Listing 10.6(a) in Appendix F, which plants the artifact at $p = \tfrac12$ and finds it at $t \approx 9.9$.

**Z.10.5: Liberation Day, priced**

**Answer:** The capture is zero at $L = T/4 = 0.375$ months. That is about **8 trading days**, or 11 calendar days. For a lag of a few weeks, the formula predicts a **loss**. The capture is −23% of the round trip at a 2-week lag and −84% at 3 weeks. The worst case is −100%, at $L = T/2$, about 3¼ weeks. Beyond that the formula changes branch to $2L/T - 2$ (−77% at 4 weeks), and the loss shrinks until the signal never flips ($L \ge T$, capture 0). In money terms, the round trip was about 119 bp out and back at $D = 4$, so $2d \approx 9.5\%$ of notional, and a 3-week lag at unit size loses about 8%. A vol-targeted, carry-hurdled sleeve loses less for four reasons:

1. Its legs after the gap are smaller, because the DTS forecast cut notional to $342/461 = 0.74$ and the EWMA forecast cut it to 0.61.
2. A fractional signal (ensemble or tanh) shrinks as its components start to disagree.
3. Components behind a carry hurdle flip late or not at all, and a signal that never flips captures zero, not a loss.
4. The real V was lopsided: 3 sessions out and 24 back. The symmetric formula overstates the loss on a gap.

On the real tape, Listing 10.6's sleeve lost 0.88% of capital from 2 April to 14 May. That is 0.66% per unit of the notional it held on 2 April, against 1.7% for a fixed-size crossover sign.

**How:** Sum the four legs of the stylized V to get capture $= (T-4L)/T$, then set it to zero to find $L = T/4$. In trading days, $0.375 \times 21 = 7.9$. With a 3-week lag of 0.69 months, the capture is $(1.5 - 2.76)/1.5 = -0.84$. Now make the V lopsided: it falls over $a$ periods and recovers over $b$, and the lag sits between them ($a < L < b$). The follower is long through the whole fall ($-d$), then long, short for $a$ periods, and long again on the way up. The legs sum to

$$
\text{P\&L} = -d + \frac{d}{b}\big[(L-a) - a + (b-L)\big] = -\frac{2ad}{b},
\qquad \text{capture} = -\frac{a}{b},
$$

and the lag cancels out. On FRED HY OAS the fall took 3 sessions (3.42% on 2 April to 4.61% on 7 April) and the recovery to 3.15% took 24, which gives a capture of about −12.5%. The gap did the damage before any lag mattered. On the tape, the sleeve's weight went from −1.33 on 2 April to −0.53 on 5 May. Volatility rose from 4.7% to 7.5%, which offset the stronger signal, and the ensemble decayed to zero as the 1-month and 12-month signals turned long. So the short it carried into the recovery shrank while the recovery was happening.

**The trap:** One common wrong answer is a positive sign: it was a huge move, trend is a straddle, so crisis alpha. The smile pays on large moves only when the move outlasts the lag (§10.6.1). A V is two large moves of opposite sign inside one lag. The other wrong answer comes from using $(T-4L)/T$ past its range. At a 4-week lag it gives −145%, which is worse than shorting at the top and covering at the bottom. Once $L > T/2$ the signal flips after the trough, and the legs give $2L/T - 2$ instead (Figure 10.4's caption). A capture below −100% means you are on the wrong branch.

**If you got this wrong, read:** §10.6.2 and Figure 10.4 for the whipsaw arithmetic and both branches, §10.3 for the 0.74, §10.1.2 for the hurdle, and the §10.7 Coda for the week itself.

### Z.11 Chapter 11: Defensive Systematic High Yield

Six exercises. Every number below was recomputed from the chapter's inputs, and the two that rerun code (4 and 6) used Listings 11.3 and 11.6 as printed in Appendix F. Inputs the exercise does not pin down are labelled illustrative.

**Z.11.1: The top-quartile hand history**

**Answer:** $\alpha \approx 6.2$bp a month (about 75bp a year) and $\beta \approx 0.951$. The zero-alpha asymmetric portfolio with the same capture ratios is $\beta^{+} = 0.99$, $\beta^{-} = 0.92$. On the June/July 2022 pair ($-6.8\%$, then $+6.0\%$) the alpha book compounds to $-1.01\%$ and the asymmetric book to $-0.69\%$, against $-1.21\%$ for the benchmark, so the convex book wins the pair by 32bp. On a quiet pair ($-0.5\%$, $+0.5\%$) the alpha book wins by 9bp. The two books tie in a month exactly at the regime means, $+1.6\%$ and $-2.0\%$. Capture ratios only see those means, so they cannot tell the books apart.

**How:** From §11.2.1,

$$
U - D = \alpha\left(\frac{1}{0.016} + \frac{1}{0.020}\right) = 112.5\,\alpha \;\Rightarrow\; \alpha = \frac{0.07}{112.5} = 0.000622,
$$

and $\beta = U - \alpha/\bar r_b^{\,\mathcal U} = 0.99 - 0.0389 = 0.951$. Check: $D = 0.951 - 0.000622/0.020 = 0.920$. With $\alpha = 0$ in the asymmetric regression of §11.2.2, $U = \beta^{+}$ and $D = \beta^{-}$, so you read the betas straight off the ratios. Month by month, the convex book minus the alpha book is $(\beta^{+} - \beta)\,r_b - \alpha = 0.0389\,r_b - \alpha$ in an up month and $0.0311\,\lvert r_b\rvert - \alpha$ in a down month. Both are zero at the regime means and positive beyond them. For the consultant: capture ratios are two averages, and many portfolios produce the same two averages. A regime-pair test, or the kinked regression, looks at how the return scales with the *size* of the move. The alpha book earns a fixed 6.2bp whatever happens; the convex book earns its edge in the big months, which are the ones a defensive mandate exists for. The regression gives the first book $\beta^{+} = \beta^{-} = 0.951$ with a positive intercept, and the second book $0.99$ and $0.92$ with no intercept.

**The trap:** Plugging $\bar r_b^{\,\mathcal D} = -2.0\%$ in with its sign. The bracket becomes $62.5 - 50 = 12.5$, and $\alpha$ comes out at 56bp a month (6.7% a year), which is hedge-fund alpha from a long-only manager. The identity needs $\lvert\bar r_b^{\,\mathcal D}\rvert$. A milder slip is taking $\beta = (U+D)/2 = 0.955$. The midpoint is only roughly beta: it is off by $\tfrac12\alpha(1/0.016 - 1/0.020) = 0.004$.

**If you got this wrong, read:** §11.2.1 and its Full Derivation, then §11.2.2 for the kinked regression, and the BlackRock p.5 annotation and §11.2.3 for why the test is run on pairs.

**Z.11.2: Skew by tier**

**Answer:** $\dfrac{d}{dp}\left[-\dfrac{1-2p}{\sqrt{p(1-p)}}\right] = \dfrac{1}{2\,[p(1-p)]^{3/2}} > 0$, so the skew rises toward zero as the PD rises. It is $-9.85$ at $p = 1\%$ and $-2.67$ at $p = 10\%$. For sizing, equal expected loss is not equal risk. With the same $L$, a 1% BB position needs ten times the weight of a 10% CCC position to carry the same EL. Its default then costs ten times as much, and its jump has 3.3 times the standard deviation.

**How:** Write $g(p) = (1-2p)\,[p(1-p)]^{-1/2}$ and differentiate:

$$
g'(p) = -\frac{2}{[p(1-p)]^{1/2}} - \frac{(1-2p)^2}{2\,[p(1-p)]^{3/2}} = -\frac{4p(1-p) + (1-2p)^2}{2\,[p(1-p)]^{3/2}} = -\frac{1}{2\,[p(1-p)]^{3/2}},
$$

because $4p - 4p^2 + 1 - 4p + 4p^2 = 1$. The skew is $-g$, so it increases on all of $(0,1)$, which covers $(0,\tfrac12)$. Plug in: $-0.98/\sqrt{0.0099} = -9.85$ and $-0.80/0.30 = -2.67$.

The paragraph: give each name an EL budget $e$, so $w = e/(pL)$. The loss if it defaults is $wL = e/p$, which is $100e$ for the BB and $10e$ for the CCC. The jump's standard deviation is $wL\sqrt{p(1-p)} = e\sqrt{(1-p)/p}$, which is $9.95e$ against $3.0e$. On a 10bp-per-name budget with $L = 0.6$, the BB is 16.7% of the book and the CCC 1.7% *(illustrative)*. The BB's risk sits in a rare, very skewed jump, and per Bolder (§11.6.1) it arrives with the cycle and does not diversify. The CCC's risk is a frequent, mostly idiosyncratic jump that breadth can average away. So cap BB positions by jump-to-default, the issuer cap, and size CCC positions by EL, spread across many names. EL is a first-moment budget, and the skew says the BB's danger is in the third moment.

**The trap:** Reading "less negatively skewed" as "safer" and sizing the CCC up. Skew is a shape statistic and says nothing about scale: the CCC still has ten times the EL per dollar. The mirror-image error is equal-EL sizing that quietly puts a sixth of the book in one BB name. The algebra trap is differentiating the Bernoulli skew $(1-2p)/\sqrt{p(1-p)}$, which *falls* with $p$, and forgetting that $-L_P$ flips the sign.

**If you got this wrong, read:** §11.1.1 (the mixture, and why the safest bonds are the most skewed), then §11.6.1 (Bolder on idiosyncratic high-PD risk, the EL budget and the per-issuer limit).

**Z.11.3: Ines's question, answered**

**Answer:** $\mu = 1.466$, the cutoff is 0.727 on the survivor scale, 23.4% of survivors are flagged, and $q = 24.97\% \approx 25\%$. Then $\pi_X = 9.25\%$ and $\pi_K = 0.92\%$, and the active return is $0.2497 \times (5.00\% - 4.00\%) \approx +25$bp a year. It is good news, but thin. The claim fits an honest model with AR 0.70, and at a 25% exclusion it pays. Break-even, though, is an excess spread of 500bp in the excluded set, and every 100bp above 400 costs about 25bp a year.

**How:** Invert the AUC: $\mu = \sqrt2\,\Phi^{-1}(0.85) = 1.4142 \times 1.0364 = 1.466$. Flag every name scoring above a cutoff $c$. The hit rate is the defaulters' tail, $1 - \Phi(c - \mu) = 0.77$, so $c = \mu + \Phi^{-1}(0.23) = 1.466 - 0.739 = 0.727$. Survivors above $c$: $1 - \Phi(0.727) = 0.2336$. The exclusion fraction counts both crowds:

$$
q = 0.03 \times 0.77 + 0.97 \times 0.2336 = 0.0231 + 0.2266 = 0.2497 .
$$

Then $\pi_X = 0.0231/0.2497 = 9.25\%$ and $\pi_K = 0.0069/0.7503 = 0.92\%$, so the excess default loss is $(0.0925 - 0.0092)\times 0.6 = 5.00\%$. By §11.5.2, $\mathbb{E}[r_{\text{active}}] \approx 0.2497 \times (0.0500 - 0.0400) = 0.0025$. A flagged name defaults at 9.2%, about three times the base rate, and the 23% of survivors you threw out take their carry with them. The same binormal model gives hit rates of 54%, 71% and 81% at $q$ of 10%, 20% and 30%, so the vendor's single point sits on a perfectly ordinary curve.

**The trap:** Forgetting the $\sqrt2$, so that $\mu = \Phi^{-1}(0.85) = 1.04$. That model is weaker. It needs $q \approx 39\%$ to reach 77%, and the active return turns into about $-46$bp. The other common slip is calling 23.4% (the share of *survivors* flagged) the exclusion fraction. That drops the defaulters you also excluded and understates $q$ by 1.6 points.

**If you got this wrong, read:** §11.5.1 (AUC as a bet; AR $= 2\,$AUC $- 1$), then §11.5.2, including the Base Rates box and the $+44$/$-9$bp worked example that this exercise reruns.

**Z.11.4: The soft-default world**

**Answer:** `de_share` only relabels defaults that have already been drawn, so the panel is unchanged: 163 issuer defaults, and a full 12-month label rate of 3.24% of issuer-months. What changes is the label mix. 67% of default rows (66.5% of defaulted issuers) become exchanges, which leaves a hard-default rate of 1.07%. A model trained on the hard label predicts about a third of the realized full-label rate in almost every decile:

| PD decile (hard model) | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Predicted, hard label (%) | 0.03 | 0.06 | 0.10 | 0.15 | 0.23 | 0.34 | 0.52 | 0.88 | 1.89 | 6.49 |
| Realized, full label (%) | 0.00 | 0.17 | 0.26 | 0.53 | 0.81 | 0.68 | 0.81 | 2.22 | 7.41 | 19.51 |
| After prior shift (%) | 0.09 | 0.19 | 0.31 | 0.47 | 0.70 | 1.03 | 1.60 | 2.69 | 5.62 | 17.13 |

The mean absolute error across deciles is 2.18 points before the shift and 0.61 after. The mean PD goes from 1.07% to 2.98%, against 3.24% realized. AUC against the full label is 0.885 both before and after the shift, and 0.886 for a model trained on the full label. So in the listing's world the shift repairs almost everything. It cannot repair the *ranking* when exchanges cluster in sponsor-owned issuers with drop-down capacity. The feature that can is a dated drop-down capacity flag (unrestricted-subsidiary and investment-basket capacity, or Chapter 13's PRS), together with months since the last LME, fitted on the full label.

**How:** Call `simulate_hy_universe(de_share=0.65)`, lag the features by 3 months, set $y^{\text{hard}} = y \cdot (1 - \text{de\_flag})$, fit `fit_logit` on $y^{\text{hard}}$, bin the fitted PDs into deciles and compare each decile with the realized full label. These numbers are in-sample, on issuer-months with overlapping labels. The shift uses $\pi_s = 1.07\%$ and $\pi = 3.24\%$, which multiplies every issuer's odds by

$$
\frac{0.0324/0.9676}{0.0107/0.9893} = 3.10 .
$$

It works here because the listing draws `is_de` independently of every covariate. The hard label is then a random one-third thinning of the full label, which changes the prior and leaves the likelihood ratio alone, exactly the condition in the intercept-shift derivation of §11.4.2. It is not perfect, because thinning scales probabilities, not odds. The odds factor actually needed is $(1-\theta p)/(\theta(1-p))$ with $\theta \approx 0.33$. That rises from about 3.0 for small PDs to about 3.5 at 20%, so one constant over-corrects the bottom deciles and under-corrects the top. The shift adds the same constant to every logit, which is a monotone map: the order of issuers, and with it the AUC, the CAP and every hit rate, cannot change. When exchanges are concentrated, the hard label calls the drop-down-capable issuers survivors, so the likelihood ratio itself is wrong for them, and no prior repairs a likelihood. To check, I ran a variant of the simulator *(my extension, illustrative)*: 54% of issuers have capacity, only they do exchanges, and the exchange share is 65.5%. After the shift, the hard model predicts 2.6% for capacity issuers that default at 5.8%, and 5.1% for the rest, which default at 3.0%. Its AUC stays at 0.848. A full-label model with the capacity flag scores 0.871 in-sample (on purged folds the gain is smaller, from 0.791 to 0.798), and its hit rate at a 20% exclusion rises from 71% to 75%.

**The trap:** Concluding from the clean result above that the prior shift fixes soft defaults in general. The listing assigns exchanges at random, which is the one case where the shift is guaranteed to work. The second trap is adding the capacity flag but keeping the hard label. In the variant, the flag then gets a coefficient of $-2.3$: the model learns that drop-down capacity *protects* you, which is the "default softly and never default" lesson of §11.4.3, now written into the model's coefficients. You need the full label and the feature together.

**If you got this wrong, read:** §11.4.2 (the intercept shift and its Full Derivation: "power and calibration are separate repairs"), §11.4.3 (the Saks replay and the desk label), and the Listing 11.3 specification. Chapter 13 builds the Priming Risk Score.

**Z.11.5: ROBO, defensively**

**Answer:** Three portfolios that satisfy the sentence literally, and the constraint that kills each one.

1. **One BB bond.** Put 100% in the single short-dated BB with the lowest PD. In a backtest, ROBO can even pick the one that, with hindsight, beat the index and did not default. Realized defaults are zero, and in a selloff year it beats the index. *Constraint:* $w_i \le 3\%$ for every *issuer* (so at least 34 names), together with DTS-neutrality, $\lvert w^\top\text{DTS}/\text{DTS}^{\text{bench}} - 1\rvert \le 1\%$, so the book cannot hide in a low-DTS corner. Selection is walk-forward only.
2. **Leverage.** Hold the safest BBs, or Treasuries, and borrow (or add a total-return swap) until expected return beats the index. Its holdings never default, and its return is just beta bought with borrowed money. *Constraint:* $w \ge 0$, $\mathbf 1^\top w = 1$, no borrowing or derivatives unless the mandate says so, and $\text{DTS}^{\text{target}} \le \text{DTS}^{\max}$, with a halt-and-alert if the target cannot be reached long-only.
3. **Redefine "default".** Score defaults as bankruptcy filings or missed coupons only, then fill the book with sponsor-owned names whose distress will arrive as exchanges and LMEs. That was most of 2025's defaults, so the book reports "zero defaults" while holders are being primed. *Constraint:* the desk label from §11.4.3, fixed in the spec. A default is any of {payment default beyond grace, bankruptcy, distressed exchange, LME that impairs the holder}, announced in $[t, t+12)$, stamped at announcement, counted once per issuer, and read from a point-in-time event table.

**How:** Look for the words in the sentence that leave a degree of freedom. "Minimize realized defaults" sets no breadth requirement, so concentration games the objective (portfolio 1). "Beating the index" has no risk unit, so leverage, or any extra beta, games it (portfolio 2). "Defaults" has no definition, so the label games it (portfolio 3). Each constraint closes one of those gaps. The issuer cap and DTS band set the risk unit at the benchmark's, as in §11.7. The long-only and DTS-max guard is the no-leverage rule of §11.8. The label is fixed by the spec rather than chosen by the optimizer. Then "beat the index" should be stated as an excess-return objective on DTS-matched risk, reported with $U$, $D$, $\beta^{+}$, $\beta^{-}$ on benchmark regimes. That is, almost word for word, the spec at the end of the chapter.

**The trap:** Writing a constraint that sounds right and does not bind. A minimum number of *bonds* is the usual one: a capital structure with 47 lines satisfies it with one issuer. Another is a market-value-neutral or tracking-error limit with no DTS term, which lets the dimmer switch back in at a beta of 0.85. The third is a default definition left in a vendor's hands: Marisol's Tuesday in §11.4 shows a vendor moving every exchange's date overnight.

**If you got this wrong, read:** the §11.2 Specification (ROBO's T-bill portfolio), §11.4.3 (the desk label), §11.7.2 and the §11.7 Specification (IDO, the issuer cap and the refusal to lever), and The Spec You Hand the Robot after the Desk Debrief.

**Z.11.6: Capacity is a square**

**Answer:** $C^\ast \propto 1/\text{TO}^2$, so $C^\ast(\text{TO}/2) = 4\,C^\ast(\text{TO})$. On Listing 11.6's niche inputs, capacity is \$1.2bn at a turnover of 2.0 and \$4.8bn at 1.0. In practice it never quadruples, because a CCC-reversal edge is earned per trade. If gross alpha is proportional to turnover, halving turnover takes $\alpha_0$ from 3% to 1.5%, and capacity *falls* to \$0.3bn. Capacity only holds at \$1.2bn if the slower book keeps at least 2.0% of its 3.0% gross alpha *(all inputs illustrative)*.

**How:** Every term in $C^\ast = V_{\text{ADV}}H\big((\alpha_0 - \alpha_{\min})/(\kappa\,\text{TO})\big)^2$ except $\text{TO}$ is held fixed, so

$$
\frac{C^\ast(\text{TO}/2)}{C^\ast(\text{TO})} = \frac{(\text{TO})^2}{(\text{TO}/2)^2} = 4 .
$$

The intuition comes from the net-alpha line. The cost term $\kappa\,\text{TO}\sqrt{C/(V_{\text{ADV}}H)}$ stays the same when $\text{TO}$ halves and $C$ quadruples. Niche inputs: $V_{\text{ADV}}H = \$1.5\text{bn} \times 20 = \$30\text{bn}$, $\alpha_0 - \alpha_{\min} = 2\%$, $\kappa = 0.05$. At $\text{TO} = 2$: $30 \times (0.02/0.10)^2 = \$1.2$bn, which matches the listing's printout. At $\text{TO} = 1$: $30 \times (0.02/0.05)^2 = \$4.8$bn. Now let the edge decay, $\alpha_0 = 3\% \times (\text{TO}/2)^{g}$. With $g = 1$ (a fixed edge per round trip), $\text{TO} = 1$ gives $30 \times (0.005/0.05)^2 = \$0.3$bn. With $g = \tfrac12$ it gives \$1.5bn. The economics explain the decay. CCC reversal is a liquidity-provision premium paid by forced sellers: CLOs defending OC tests, fallen-angel index exits and ETF redemptions. The dislocation is temporary (Elkamhi and Nozawa, in the §11.6.1 CLO box), and in April 2025 HYG went from a 0.66% discount to a 1.49% premium in two days. A book that trades half as often arrives after the price has come back, and holds the name's default risk for longer. Worse, $\kappa$ is state-dependent and peaks exactly when the signal fires.

**The trap:** Saying capacity doubles. That treats cost as linear in turnover and forgets that, under square-root impact, cost grows with $\sqrt C$, so restoring the same cost lets $C$ grow by the *square* of the turnover cut. The subtler trap is treating $\alpha_0$ as a constant you can carry across turnover levels. For the core sleeve, an exclusion rule whose edge is about whom not to own, that is roughly true. For the satellite it is false, and the quadrupling only exists on paper.

**If you got this wrong, read:** §11.9 and its Listing 11.6 Specification, and Chapter 4, §4.8 for square-root impact. For why the satellite's edge is perishable, read §11.6.1's CLO-manager box and the HYG beats of §11.8.1.

### Z.12 Chapter 12: Multi-Asset Credit Allocation

Six exercises. Every number below was recomputed in Python, with a simulation wherever a closed form needed checking. There is one note for the editor, in Z.12.5. Write your card before you read ours.

**Z.12.1: Read the chart**

**Answer:** At 40% recovery the loss given default is 0.6. If 2.55 is the expected credit loss, the implied physical default rate is $2.55/0.6 =$ **4.25% a year**. If 0.49 is the loss, it is **0.82% a year**. The first assignment survives: expected credit loss 2.55, rates MTM 0.37, spread MTM 0.49. To settle it without economics you need the PDF's *geometry*, not its text order. That means the page coordinates of each number and each category label (or the bar heights in the drawing layer, or simply the rendered image), so that each value can be snapped to the bar it sits on.

**How:** Invert the loss term of (12.1), $\lambda^{\mathbb{P}} = \text{EL}/(1-R)$. Then test the other label the same way. If 2.55 were the spread drag, the five-year widening it implies at $D^{\text{spr}} \approx 3.2$ would be

$$
\Delta s = \frac{2.55\% \times 5}{3.2} \approx 398\text{ bp},
$$

which more than doubles the index spread, and it would be the *central* forecast. The other assignment, 0.49, implies about 77 bp of widening, which is an ordinary assumption (Listing 12.1 uses 75 bp). A 4.25% default rate is in the range of long-run speculative-grade experience. A 0.82% rate is implausible for an index that is about half single-B and below. Both tests point the same way. Notice what the surviving reading implies: a 2.55% loss eats most of an index spread that stood near 2.8% (281 bp at year-end 2025, §12.3). That is why HY's 3.56% lands below the 3.68% implied cash rate in Figure 12.2. As for the PDF: the text layer lists the labels in reverse order, so the extraction order proves nothing. Word bounding boxes (an $x_0$ and a top for every string) let you match each value to its nearest category label. In the drawing layer, a 2.55 bar is about five times as tall as a 0.49 bar on the same axis.

**The trap:** The most common slip is dividing by the recovery instead of the loss given default, which gives $2.55/0.4 = 6.4\%$ and $0.49/0.4 = 1.2\%$. The ranking survives, but the numbers are wrong, and 6.4% would have you believing Nuveen assumes a recession. The subtler trap is thinking the arithmetic settles the question. $6.97 - 2.55 - 0.37 - 0.49 = 3.56$ ties under *both* assignments, because addition does not care about labels.

**If you got this wrong, read:** §12.2, "Theo's Tuesday rebuild" and the bookmaker's-odds box; then §12.3 for $\lambda^{\text{BE}} = s/(1-R)$.

**Z.12.2: The appraisal discount**

**Answer:** Under AR(1) smoothing, the lag-1 autocorrelation of the reported series *is* $\phi$, so $\phi = 0.6$ and $\xi = (1-\phi)/(1+\phi) = 0.4/1.6 =$ **0.25**. True volatility is $1.8\%/\sqrt{0.25} =$ **3.6% a year**, twice what was reported. The contemporaneous HY beta is understated by the factor $\theta_0 = 1-\phi =$ **0.4**, so the true beta is 2.5 times the reported one. The correlation with HY is understated by $\sqrt{1-\phi^2} = 0.8$.

**How:** With AR(1) weights $\theta_j = (1-\phi)\phi^j$, $\xi = \sum_j \theta_j^2 = (1-\phi)^2/(1-\phi^2)$. The reported 1.8% is a quarterly 0.9% multiplied by $\sqrt 4$. Desmoothed, that becomes $0.9\%/0.5 = 1.8\%$ a quarter and 3.6% a year. Beta sees only the part of each market move that is booked in the same quarter, $\operatorname{Cov}(r^o_t, m_t) = \theta_0\beta\sigma_m^2$, which is why its factor is smaller than the volatility's. A two-million-quarter simulation returns an autocorrelation of 0.600, a variance ratio of 0.250, a beta ratio of 0.400 and a correlation ratio of 0.800. To recover the beta, regress on current and four lagged HY returns and sum the coefficients (Dimson); that gets back $1 - 0.6^5 = 92\%$ of it.

For the committee: "Your marks add up. The smoothing weights sum to one, so every dollar the loans gain or lose reaches the NAV eventually. Nothing is hidden; it is only spread over several quarters, which is what a prudent committee does when it anchors on last quarter's mark. Our mistake came later. We multiplied the quarterly standard deviation by two, the $\sqrt 4$ rule, and that rule assumes each quarter is independent news. Your quarters carry 60% of the last one forward. Annualizing a delay as if it were independence makes it look like calm." One refinement if they push back: even an autocorrelation-adjusted annualization of the *reported* series (Lo 2002) gives only 2.77% at one year, because part of this year's move is still sitting in next year's marks. The reported series catches up with the true risk only over long horizons; in simulation, 10-year sums reach 98% of the true volatility. Desmoothing quarter by quarter, $\hat r_t = (r^o_t - \phi r^o_{t-1})/(1-\phi)$, gives the 3.6% directly.

**The trap:** Applying one factor to everything. Most readers get the volatility right and then say the beta is understated by the same 0.5. It is understated by 0.4, a bigger factor. The other slip is dropping the square root. $1.8/0.25 = 7.2\%$ treats $\xi$ as a ratio of volatilities, but it is a ratio of variances.

**If you got this wrong, read:** §12.5, Step 4: "A thermometer with a lag" and the Full Derivation that follows it (Getmansky, Lo and Makarov).

**Z.12.3: Kaz's typo**

**Answer:** The expected durations are $1/(1-0.97) =$ **33.3 months** for calm and $1/(1-0.10) =$ **1.11 months** for stress. The stationary distribution puts $\pi^\star_{\text{stress}} = 0.03/(0.03 + 0.90) =$ **3.2%** on stress and **96.8%** on calm. A filter acting with a one-month delay can act on a stress month only if the month before was also stress, and that happens with probability $P_{22} = 0.10$. So it misses 90% of stress months, and 90% of the trades it makes "for stress" land in calm months. Per visit, it overlaps $1.11 - 1 = 0.11$ months of stress. If the delay is two months, as with a NAV that arrives six weeks late, the overlap falls to 0.011 months.

**How:** The filter can label month $t$ only after month $t$'s returns have printed, and it acts in month $t+1$. Even when it is certain at $t$, the predict step gives $\Pr(\text{stress at } t+1) = P_{22} = 0.10$. In general, the filter's deviation from the stationary mix decays at the chain's second eigenvalue, $\lambda_2 = P_{11} + P_{22} - 1 = 0.07$:

$$
\xi_{t+1\mid t} - \pi^\star = \lambda_2\,\big(\xi_{t\mid t} - \pi^\star\big).
$$

So 93% of whatever the filter has learned is gone by the time it is allowed to trade. In (12.2) with a 12-month horizon, a filter that is *certain* of stress moves the stress weight from 3.2% to 3.8%. Compare the fitted chain of Listing 12.4 (durations of 21.9 and 5.7 months), which keeps 43%. A three-million-month simulation agrees: 9.8% of stress months follow a stress month.

There are two ways to repair it. (a) *Weekly data.* Keep the calendar and change the clock. A two-month stress becomes $P_{22} \approx 1 - 1/8.7 = 0.885$ per week, and calm becomes $P_{11} \approx 0.993$. A one-week delay now costs one week of a nine-week episode, and the filter acts on about 88% of stress weeks. Kaz's weekly rerun on the BB/B/CCC vector crossed one half in the third week of March 2025 (§12.9). The costs: weekly returns are noisier and less Gaussian, so there are more false alarms, each paid for in LCS. Loans, CLO mezzanine and the BDC have no honest weekly price and must leave the regime vector. A $P_{11}$ near one is estimated imprecisely. And stale prints in weekly bond data can masquerade as persistence. (b) *A prior on $P_{22}$.* Put a Beta$(a,b)$ prior on it and run MAP-EM, which replaces the M-step with $\hat P_{22} = (n_{22} + a - 1)/(n_{2\cdot} + a + b - 2)$. To illustrate: with ten one-month stress visits in the sample ($n_{22} = 1$, $n_{21} = 10$), a Beta(16, 4) prior (mean 0.8) pulls $\hat P_{22}$ to 0.55. That is a 2.2-month duration, and $\lambda_2$ becomes 0.52. The cost is that the stress duration is now partly your assumption rather than a finding. The model holds stress longer, so it is late *out* of stress, which is the BlackRock warning of §12.8 and the two-session snap-back of April 2025. And if Kaz was right that stress is one-month noise, the prior has manufactured a regime. Report the prior, and show $\hat P_{22}$ under two of them.

**The trap:** Inverting the wrong probability: $1/P_{22} = 10$ months for stress and $1/P_{11} \approx 1.03$ months for calm. That reverses the story, because a ten-month stress looks perfectly tradable with a one-month lag. A visit ends at the first "leave", so the duration is $1/(1 - \text{stay})$. The second slip is "the filter will catch it next month". The first stress month is always over before the filter can see it, and with $P_{22} = 0.10$ there is usually no second month.

**If you got this wrong, read:** §12.4: the weather coin, "Bayes, every evening" (the predict step that evaporates the alarm) and (12.2) with its stationary limit. Then Case Study A in §12.9 for the weekly rerun.

**Z.12.4: Two-asset ERC**

**Answer:** $w_{\text{HY}} = 0.22/(0.096 + 0.22) =$ **69.6%** and $w_{\text{CLO}} =$ **30.4%**, whatever the correlation. Each sleeve then carries the same DTS contribution, 0.0668. The 50/50 market-value book puts 69.6% of its DTS in the CLO tranche, and its risk share goes to CLO in the same way: 70% at $\rho = 1$, 71% at $\rho = 0.8$ and 84% at $\rho = 0$. Getting from 50/50 to ERC means moving about 20 points of NAV from CLO into HY. At $\rho = 1$ the ERC book also has 15% less volatility (DTS 0.134 against 0.158).

**How:** Write out the two risk contributions:

$$
w_1(\Sigma w)_1 = w_1^2\sigma_1^2 + w_1w_2\,\rho\,\sigma_1\sigma_2, \qquad
w_2(\Sigma w)_2 = w_2^2\sigma_2^2 + w_1w_2\,\rho\,\sigma_1\sigma_2 .
$$

The cross term is the same in both, so setting them equal leaves $w_1^2\sigma_1^2 = w_2^2\sigma_2^2$. With positive weights that is $w_1\sigma_1 = w_2\sigma_2$, so $w_i \propto 1/\sigma_i$, and $\rho$ has dropped out (for any $\rho > -1$; at $-1$ the portfolio has zero variance and the shares are undefined). Under (12.3), $\sigma_i = \text{DTS}_i\,\sigma(\Delta s/s)$. The common $\sigma(\Delta s/s)$ cancels too, leaving $w_i \propto 1/\text{DTS}_i$. So two-asset ERC is simply *equal DTS contributions*, which is Ben Dor's consistency argument (p.63) for a book of two sleeves. Under 50/50, HY's risk share is $(\sigma_1^2 + \rho\sigma_1\sigma_2)/(\sigma_1^2 + \sigma_2^2 + 2\rho\sigma_1\sigma_2)$: 16.0% at $\rho = 0$, 28.6% at 0.8 and 30.4% at 1. From three sectors on, the correlations no longer cancel, which is why Listing 12.5's `optimize_erc` solves the problem by Newton's method. Two caveats from the chapter apply. The DTS-implied volatility of a mezzanine tranche is a floor, because tranches gap in stress (§12.5), so an honest ERC weight on CLO is *below* 30%. And Nuveen's bounds cap CLO at 10% anyway.

**The trap:** Inverse-variance weights, $w \propto 1/\sigma^2$, which give 84/16. That is the minimum-variance answer at $\rho = 0$, not ERC, and it starves the riskier sleeve until it contributes only 16% of the risk. The other trap is believing that equal weights mean equal risk. The 50/50 book hands about 70% of its risk to the CLO tranche.

**If you got this wrong, read:** §12.6 on risk budgeting and its Full Derivation, then §12.3 and §12.5 (Step 1) on DTS as the common unit of risk.

**Z.12.5: The gate as a queue**

**Answer:** Under strict pro-rata fills, **never**. This quarter fills $5/15 = 1/3$ of the request, and every later quarter fills $5/10 = 1/2$ of what is left. After $n$ quarters the unpaid share is $\tfrac23\left(\tfrac12\right)^{n-1}$: half is out after 2 quarters, 90% after 4, 95% after 5 and 99% after 8. The dollar-weighted mean exit time is $2\tfrac13$ quarters, about **213 days**. The optimizer should use that mean as $\tau$ in its days budget, which is a linear average. The stress test should use a tail number: 95% out takes 5 quarters, about **456 days**. Both should be computed as functions of the request ratio $Q/g$ and re-estimated every tender cycle. A constant is wrong because $Q$ is set by other holders, and it rises exactly when you most want to leave.

**How:** Pro-rata means you receive $g/Q_t$ of whatever you ask for each quarter. Unfilled requests are not carried over, so you resubmit the remainder, and $R_n = R_{n-1}(1 - g/Q_n)$. With a constant fill $p$, the wait is geometric with mean $1/p = Q/g$ quarters. Here, therefore,

$$
\bar\tau = 1 \cdot \tfrac13 + \tfrac23\,(1 + 2) = 2\tfrac13 \text{ quarters}.
$$

The chapter's "at least three quarters" (§12.7) is the case where the line *drains*: fills of 1/3, then 5/10, then 5/5. In this exercise the line refills to 10% every quarter, so the fill never reaches one. If the 10% were new requests *on top of* the resubmissions, the line would grow and the exit would take longer still. Now feed this into the engine. At a 15% weight, $0.15 \times 213 = 32$ days, which is Listing 12.5's entire $\bar\tau$, against 27 days at Listing 12.1's constant of 180. At the 95%-out figure, $0.15 \times 456 = 68$ days, and the days budget alone would cap the sleeve near 7%. A constant fails for four reasons. $Q$ is endogenous: HPS's flagship went from requests of about 4% of shares in the fourth-quarter cycle to about 9% in the first, and Blue Owl's technology fund from above 15% to about 40% (§12.7). $Q$ moves with the news and with the spread factor, so the exit is longest in the state where you need it (Ben Dor p.296). The line refills itself through resubmissions. And the gate is a decision: the IMF noted managers who paid out more than 5%. A constant 90 days describes a world where $Q \le g$.

**The trap:** Answering "three quarters" ($15/5$), as if the line were a stock that drains. That is the lower bound in the §12.7 annotation, and it holds only if nobody new joins. With the line refilling to 10%, you get half of what is left each quarter, forever. A related slip is "twenty quarters", which reads the gate as 5% of *your* position rather than 5% of the fund.

**If you got this wrong, read:** §12.7: the annotation to Ben Dor p.296, the constraint set (12.4) and "Long Scene: The Queue" (Theo's card and Ines's).

**Z.12.6: ROBO literalism**

**Answer:** ROBO builds a regime model that never switches. The cleanest version has one state ($K = 1$). The sticky version has two states with the transition matrix pinned at, or pushed toward, the identity, so that each state is absorbing. Either way it reports zero switches and meets the objective. With one state the overlay "mixture mean minus stationary mean" is identically zero, so you asked for a tactical overlay and received the strategic allocation with a regime label on it. If it has to keep two live states, ROBO's next move is to report the smoothed or Viterbi path. That path flickers less because it has read the future, which is Hana's beautiful backtest. The line that prevents it is pipeline step 4: **"HMM: K=2, full covariance, log-space forward-backward, EM"**. $K=2$ closes the one-state escape. EM makes the transition probabilities maximum-likelihood estimates from the returns, so the number of switches is something the data report, not a dial ROBO is allowed to turn.

**How:** In a stationary chain, the expected number of switches per period is $\pi^\star_1 P_{12} + \pi^\star_2 P_{21} = 2\pi^\star_1 P_{12}$. Kaz's chain gives about 0.7 a year. The count is therefore an output of $P$, and it has a trivial, data-free minimum at $P_{kk} = 1$. EM instead maximizes $\ell(\Theta) = \sum_t \ln \mathbf{1}^{\top}(\xi_{t\mid t-1} \odot f_t)$. When the sample contains stress months, the identity is not the maximum. There is one subtlety. Baum–Welch never moves a transition probability off zero, because $\xi_t(j,k)$ carries a factor $P_{jk}$, so an EM started at the identity stays there. In a 600-month test it did, with a log-likelihood 173 points below the fit from a sensible start. The chapter's code starts from the worst 20% of months, and the spec's first line, "where anything is unspecified, stop and ask", is what makes ROBO ask about the start instead of choosing the identity. The clause "act on FILTERED probabilities ... never use smoothed ones" blocks the hindsight version. And if what you actually wanted was less churn, that already has a home. Step 7's $\ell_1$ budget $\kappa$ and LCS costs decide whether a switch is worth trading, so the model can be left to report what it sees.

**The trap:** Pointing at the FILTERED clause. It stops the look-ahead hack, but a one-state model has perfectly good filtered probabilities too: they are constant. The deeper trap is treating fewer switches as a virtue. A regime model earns its keep by switching at the right time. Kaz's typo fails because it leaves stress too fast ($P_{22} = 0.10$), not because it reports too many regimes.

**If you got this wrong, read:** §12.4 (the filter, EM and label alignment; Hana's refresh for filtered versus smoothed), §12.8 for where turnover belongs, and "The Spec You Hand the Robot" in §12.11.

## Part IV: Quantifying Special Situations & PJT RSSG Mechanics

### Z.15 Chapter 15: Event-Driven M&A, Regulatory Spreads & Change-of-Control

Five exercises: one on the EA defeasance, one on the SMR gauge going blind, one on a regression design, one on the WBD ticking fee and one on Kaz's bell curve. Every number below was recomputed, from the chapter's Blocks 1 and 3 (Appendix F, Listings 15.1 and 15.3) where an exercise uses them and from the chapter's own inputs otherwise. Where we had to assume an input, the solution says so and labels it illustrative. Write your answer down before you read ours.

**Z.15.1: The defeasance arithmetic**

**Answer:** We price on Listing 15.1's illustrative Treasury curve, whose zero rates are 4.39% at 4.5 years and 4.49% at 24.5 years, plus a flat 350bp LBO spread. The post-close prices are 77.0 for the 1.85% 2031s and 45.3 for the 2.95% 2051s, so if the put triggers at close it is worth **24.0 points and 55.7 points**. At signing, with Block 1's check-(1) inputs ($\pi_d = 0.85$, $\pi_{\text{trig}\mid d} = 0.9$, close in nine months, $B = 0.970$), the put is worth **17.8 and 41.3 points**. With check (3)'s lognormal spread and logistic ratings leg it is worth 15.6 and 35.4 ($M \approx 1.05$). Turn on the `defeasance_prob` callable and both go to 0.00.

Defeasance costs the sponsor the scheduled cash flows at Treasury flat, **89.6 and 76.8** per 100, so it **saves 11.4 and 24.2 points** against 101. On the \$681mm and \$742mm left outstanding after the tender, that is about **\$258mm**, which matches Fancourt's "over \$250mm".

The 95% who stayed were not wrong. The 2051s' tender at about 74 sat within a few points of the defeased value: 76.8 at a 4.49% long zero, 70.5 at a flat 5%, with break-even at a flat 4.70%. So tendering versus holding was a quarter-point bet on long Treasury yields, not a call on credit. Holding also kept the slim chance that the sponsor would pay 101 after all. And an insurer is glad to own Treasury-backed duration. Only 9.2% of the 2031s and 1.1% of the 2051s were tendered, 5.1% of the \$1.5bn. The holders who lost were the ones who paid 90 for a 101 that a defeasance article had already knocked out.

**How:** This is Step 3 of §15.2.2. Price the bond for the life left after close on the post-close curve,

$$
P^{\text{post}} = \sum_i \tfrac{c}{2}\,e^{-(y^{\text{TSY}}_{t_i}+s^{\text{post}})t_i} + 100\,e^{-(y^{\text{TSY}}_{T}+s^{\text{post}})T},
$$

take $(101 - P^{\text{post}})^{+}$, and multiply by $\pi_d\,\pi_{\text{trig}\mid d}\,B$ for the signing value. A constant spread makes $M = 1$. In Block 1 these are `price_coc_put` calls with `maturity_years` of 5.25 and 25.25 and `t_close = 0.75`. The sponsor's alternative is a deposit that pays every scheduled cash flow, so it costs the same sum at a zero spread:

$$
D = P(s=0), \qquad \text{saving} = 101 - D .
$$

Multiply by the face still outstanding to get dollars. Then read the same arithmetic from the holder's seat. Compared with being paid 101, the holder loses $101 - D$. Compared with being left as unsecured LBO paper, the holder gains $D - P^{\text{post}}$, which is 12.6 and 31.5 points, because the deposit replaces the sponsor's credit with the Treasury's. For the tender, set 74 against $D$ at whatever long yield you expect on the settlement date, and solve $D(y) = 74$ for the break-even.

**The trap:** Saying the sponsor saves the put, 24 and 56 points. That discounts the defeased bond at the LBO spread, but a box of Treasuries is priced at Treasury yields. The put's value is $101 - P^{\text{post}}$, the sponsor's saving is $101 - D$, and the gap between them, $D - P^{\text{post}}$, is what the holder keeps. A close second is "defeasance pays in full, so the saving is one point". In full means the scheduled payments, and on a 2.95% coupon in a 4.5% world those are worth 77, not 100.

**If you got this wrong, read:** §15.2.2 Steps 3–4 for the post-close price and the coupon-vintage table, then cuts two and three of the EA case study in §15.2. PB-10 in the same section turns the two defeased values into a hedge ratio.

**Z.15.2: The blind thermometer**

**Answer:** The two legs meet after a **parallel rally of about 38bp from issue**. Take a three-year 4.60% tranche issued at par (4.60% bond-equivalent, a 4.548% continuous yield) with the ruling a quarter away. The legs meet when the close leg's yield has fallen to 4.21%, and both are then worth 101.09. At issue the ruler is not zero. It is 1.00 point long, 100.00 against 100.99, because the fail leg carries the one-point premium plus accrued. Each basis point of rally shortens it by about 0.026 points, the gap between the two legs' dollar durations (roughly 2.8 years against 0.25, on about 101). Measured from the worked example's marks instead (close leg at 99.00, $y_f = 4.60\%$), the blind spot is a **77bp** rally away. On Listing 15.1's Nelson–Siegel curve with a flat 23bp issuer spread, it is 42bp.

At the blind spot, $\hat\pi_f$ is undefined: the tranche is worth $P^{\text{close}}$ whatever $\pi_f$ is, so its price cannot tell you $\pi_f$. Within about 4bp of that point, a 0.10-point price error moves $\hat\pi_f$ by 100 percentage points or more. Even 20bp away the same error moves it by about 20 points.

Use another instrument whose ruler is long. The first choice is a **sibling SMR tranche of the same deal with a different duration**, which has the same issuer, the same deal and the same $\mathbb{Q}$. At this rate move, a seven-year 4.90% SMR tranche issued at par has a ruler of +1.16 points: its sign has flipped, but it still carries information. Failing that, use the target's equity merger-arbitrage spread, and name its contaminants: the takeover premium, the standalone value and borrow costs. A §15.5 hazard model is not a substitute, because it is a $\mathbb{P}$ number and the gauge is a $\mathbb{Q}$ number.

**How:** Under (B1)–(B2), a parallel Treasury move $\Delta$ shifts both legs' yields:

$$
P^{\text{close}}(\Delta) = \sum_i \tfrac{c}{2}\,e^{-(y+\Delta)t_i} + 100\,e^{-(y+\Delta)T},
\qquad
G_f(\Delta) = \big(101 + 1.15\big)\,e^{-(y_f+\Delta)T_f},
$$

with $\text{AI}_{T_f} = 4.60 \times 0.25 = 1.15$ and no coupon before $T_f = 0.25$. Solve $P^{\text{close}}(\Delta) = G_f(\Delta)$ by root-finding. The linear version gets you within a basis point:

$$
\Delta^{*} \approx -\frac{G_f - P^{\text{close}}}{P^{\text{close}}D^{\text{close}} - G_f T_f} \approx -\frac{0.995}{258} \approx -39\text{bp}.
$$

Why undefined: $\partial P_0/\partial\pi_f = G_f - P^{\text{close}} = 0$ there, so every $\pi_f$ gives the same price and the mixture cannot be inverted. Near that point the inversion is a ratio of two small, noisy numbers, and a price error $\delta P$ becomes $\delta\hat\pi_f = \delta P/|P^{\text{close}} - G_f|$. To hold a 0.10-point error to 10 percentage points you need a 1-point ruler, which means about 38bp of distance from the blind spot. That is the case at issue, and almost nowhere else nearby.

**The trap:** "Zero: the gauge goes blind when rates are back where they were at issue, because the bond is at par." At par the close leg is 100 and the fail leg is about 101, so the gauge reads perfectly well. The holder only turns short the digital once a rally has lifted the close leg above 101 plus the carry difference. The second trap is to clip, or report 0.5, at the blind spot. Clipping a ratio of two noises produces a confident number. The honest output is "no information".

**If you got this wrong, read:** §15.4.2, the ruler box and "The sign flips with rates", then "Reading the gauge" for Ines's three-cent ruler, and the paragraph on Listing 15.3's `tol` guard.

**Z.15.3: The vintage anomaly**

**Answer:** The coupon coefficient is **positive** below the break-even coupon and **zero above it**. Low-coupon bonds trade *tight*, not cheap: with the put in the price, a higher coupon means a wider Z-spread,

$$
\frac{\partial z^{\text{obs}}}{\partial c} \;\approx\; \frac{\pi_d\,\pi_{\text{trig}\mid d}\,B\,M\,A(s^{\text{post}})}{P\,D_s} \;>\; 0 \quad (c < c^{*}), \qquad 0 \quad (c > c^{*}).
$$

To size it, take illustrative 5.25-year bonds (4.5 years left after a close nine months out) at a 150bp pre-deal Z-spread, with 350bp post-close, $\pi_{\text{trig}\mid d} = 0.9$, $B = 0.970$, $A = 3.72$ and $M = 1$. The slope is about **8bp of Z-spread per point of coupon at $\pi_d = 0.10$, 20bp at 0.25 and 38bp at 0.5**, and it goes flat beyond $c^{*} \approx 8.3\%$. At $\pi_d = 0.10$ the 1.85% bond trades 41bp inside the 6.875% bond, and at 0.25 it trades 100bp inside.

The test that separates the put from convexity and index eligibility uses issuer-by-date fixed effects and an interaction of coupon with the deal-and-trigger probability. The put lives in the interaction, in its kink at $c^{*}$ and in its jumps on deal-news dates. Convexity and index eligibility live in the plain coupon slope and in bond characteristics that do not change when the news arrives.

**How:** The put adds $V_{\text{CoC}}(c)$ to the price, and the Z-spread inverts price, so $dz = -dP/(P\,D_s)$ and $z^{\text{obs}} \approx z^{\text{straight}} - V_{\text{CoC}}(c)/(P\,D_s)$. Step 4 of §15.2.2 gives $\partial P^{\text{post}}/\partial c = A$, so each point of coupon takes $A$ points off the intrinsic value. With $V_{\text{CoC}} \approx \pi_d\,\pi_{\text{trig}\mid d}\,B\,M\,(K - P^{\text{post}})^{+}$, that makes $\partial V/\partial c = -\pi_d\,\pi_{\text{trig}\mid d}\,B\,M\,A$ below $c^{*}$ and zero above it. The chain rule then gives the sign. Now the design:

$$
z_{ijt} = \alpha_{it} + g(T_{ij}) + \beta\,c_{ij} + \gamma\,c_{ij}\,\hat\pi_{it} + \theta' X_{ijt} + \varepsilon_{ijt}.
$$

Here $\alpha_{it}$ is an issuer-by-date effect that absorbs the credit, $g$ is the maturity control, $\hat\pi_{it}$ is the deal-times-trigger probability (watch-list and rumour flags, sponsor versus strategic bidder), and $X$ holds each bond's computed convexity, amount outstanding, index flag, age and bid–ask. The put predicts $\gamma > 0$, of roughly the size $B\,M\,A/(P\,D_s)$, while convexity and index eligibility predict $\beta \neq 0$ and $\gamma = 0$. Cluster by issuer.

Identification comes from four places:

1. **Event dates.** The slope should steepen on the announcement and collapse when a strategic IG bidder appears ($\pi_{\text{trig}\mid d} \to 0$), when the deal breaks, or when a consent strip or defeasance is signalled, as with EA in February 2026. A bond's convexity and index membership do not change on those days.
2. **Placebos.** Use same-vintage bonds of the issuer without the CoC covenant, or with it stripped (WBD after June 2025), and non-watch-list issuers whose coupons are just as spread out.
3. **Shape.** The put is a hockey stick with a kink at $c^{*}$, and convexity is smooth in $c$.
4. **Rates.** A Treasury move shifts $c^{*}$ and the slope, while index eligibility does not move with rates.

**The trap:** Predicting a *negative* coefficient because deep-discount bonds look cheap. A low dollar price is not a wide spread. The put makes the low-coupon bond rich in Z-spread terms. The second trap is running one cross-section and crediting the whole slope to the put. In a single cross-section, index eligibility (the large 2020–21 benchmarks) and convexity both have a coupon slope of their own, and the convexity one can push either way depending on whether you measure it per dollar or per 100 face. Only variation in $\pi_d$ separates the three.

**If you got this wrong, read:** §15.2.2 Step 4 (the slope $A$, the hockey stick, $c^{*}$) and the Schmid annotation after it, then "The Full Derivation" for $M$. §7-B.1 covers the fixed effects and issuer clustering.

**Z.15.4: Was the ticking fee generous?**

**Answer:** From the signing on February 27, 2026, the meter starts at $t^{*}$ = September 30, **215 days** later. Fit a Weibull with a median of seven months (213 days) and the chapter's shape of 1.6: the scale is 268 days and the mean 240. Then $\mathbb{E}[(\tau_c - t^{*})^{+}] \approx 72$ days, so the **expected ticking is about \$0.20 a share**, roughly \$0.5bn on WBD's 2.51bn shares. The realized figure was **\$0.0167** (6 days, \$41.9mm), a twelfth of that. The realized close was an ordinary draw: the Weibull puts 52% of closings on or before day 221. The \$0.20 comes from the tail. Given that the deal is late at all, it is late by 146 days on average.

The shape matters: 1.1 gives \$0.36, 2.5 gives \$0.11 and 4 gives \$0.06. The careless readings both undershoot. At the median the meter reads zero (213 < 215), and at the mean it reads 25 days, or \$0.07.

Against cash: the per diem annualizes to \$1.014, **3.27% on \$31**, below a 2026 cash yield of about 4% (Listing 15.1's illustrative three-month zero is 3.97%). Even while it runs, the meter covers only about 82% of a holder's cost of carry. It pays nothing for the 215 days before $t^{*}$ and nothing for break risk. **Not generous. Paramount Skydance wrote the better option.** It priced the meter below cash, started it at about the median closing date, and in the event paid for six days.

**How:** Count $t^{*}$ in calendar days from signing. For a Weibull, $S(t) = e^{-(t/\lambda)^{k}}$ and the median is $m = \lambda(\ln 2)^{1/k}$, so $\lambda = m/(\ln 2)^{1/k}$. The expected positive part is the area under the survival curve past the grace period:

$$
\mathbb{E}\big[(\tau_c - t^{*})^{+}\big] = \int_{t^{*}}^{\infty} S(t)\,dt, \qquad
\mathbb{E}[\text{ticking}] = 0.00277778 \times \int_{t^{*}}^{\infty} e^{-(t/\lambda)^{k}}\,dt .
$$

The \$0.25-per-90-days cap is exactly 90 times the per diem, so it never binds. For a full price, multiply by the closing probability (no close, no ticking) and discount from the close date. Both trim a few percent, leaving the answer in the high teens of cents. For the cash comparison, set the per diem against $31\,r/365$ a day. The realized figure is $6 \times 0.00277778 = 0.01666668$, which matches the \$31.01666668 closing price.

**The trap:** Reading the meter at the expected or median closing date and getting \$0.07 or zero. The meter never runs backwards, so $\mathbb{E}[(\tau_c - t^{*})^{+}] \ge (\mathbb{E}\tau_c - t^{*})^{+}$, and the gap is the right tail. The second trap is to judge the fee by the one realized draw. \$0.0167 against \$0.20 says the deal closed at about its median, not that the fee was stingy. It was stingy because 3.27% is below cash.

**If you got this wrong, read:** §15.8, the parking-meter box and "Pricing the ticking fee", then §15.5.2 for the Weibull of shape 1.6 and why deal hazards ripen. Chapter 5 owns the distribution.

**Z.15.5: Kaz assumes Gaussian**

**Answer:** FY2025 had 1,944 adjusted transactions and 41 Second Requests, which gives weights of 0.979 and 0.021. Model "cleared in the initial period" as centred at 28 days (sd 5) and "Second Request" as centred at a year (sd 120 days, Kaz's own); both are illustrative. The **best** Gaussian is the maximum-likelihood one, with mean 35 days and sd 52, and it scores −10,428 nats. The two-component mixture scores at least −6,216, so it wins by **at least 4,212 nats, about 2.2 per deal**. Three extra parameters cost about 11 nats under BIC.

The margin does not depend on the illustrative choices. With within-component sds from 2 to 10 days, Second Request means from 180 to 540 days and sds from 60 to 240, it never falls below about 1,550 nats. FY2024's counts (1,973 transactions and 59 Second Requests) give 4,490.

On clearing before filing: Kaz's $\mathcal{N}(270, 120^2)$ puts **1.2%** of deals clearing before they file and 1.05% in the first thirty days, against about 98% in the data. Fitting the Gaussian to the HSR universe makes the first number worse. The best Gaussian, mean 35 and sd 52, puts **25% of deals clearing before they file** and only 46% by day 30.

**How:** Every Gaussian is a mixture with all its weight on one component, so the best mixture cannot lose. The only question is by how much. The best Gaussian's log-likelihood depends only on the total variance:

$$
\ell_G^{*} = -\tfrac{n}{2}\big[\ln(2\pi\hat\sigma^2) + 1\big], \qquad \hat\sigma^2 = W + B,
$$

where $W = \sum_j w_j s_j^2$ is the within-group variance and $B = w_1 w_2 (m_2 - m_1)^2$ is the between-group variance. For the mixture, the density at each deal is at least that of its own component, $p(x) \ge w_j\,\mathcal{N}(x; m_j, s_j^2)$. That gives $\ell_{\text{mix}} \ge -nH(w) - \sum_j \tfrac{n_j}{2}\big[\ln(2\pi s_j^2) + 1\big]$, where $H(w) = 0.102$ nats is the entropy of the weights. Subtract, and use Jensen's inequality, $\ln W \ge \sum_j w_j \ln s_j^2$:

$$
\ell_{\text{mix}} - \ell_G^{*} \;\ge\; n\Big[\tfrac12\ln\!\Big(1 + \frac{B}{W}\Big) - H(w)\Big].
$$

The mixture wins whenever $B/W > e^{2H} - 1 = 0.23$. Here $B \approx 2{,}345$ and $W \approx 328$ days², so $B/W \approx 7.1$, and the bound alone guarantees 1,840 nats. It holds for any Second Request sd below about 700 days. The between-group term is the gap between "a month" and "a year". It inflates $\hat\sigma$, and the Gaussian pays for that on every one of the 1,903 quick clearances. The share of deals clearing before they file is $\Phi(-\mu/\sigma)$.

**The trap:** Beating Kaz's $\mathcal{N}(270, 120^2)$ and declaring victory. His bell is not the best Gaussian on HSR data, and "every Gaussian" means you must beat the maximum-likelihood one, at 35 and 52 days. The follow-on trap is assuming the better-fitted Gaussian fixes the negative-days problem. It makes it twenty times worse. A symmetric distribution fitted to a positive, skewed waiting time whose sd exceeds its mean has to put mass below zero. A third trap is crediting the win to the extra parameters: they cost about 11 nats, and the win is in the thousands.

**If you got this wrong, read:** §15.5.1 at 10:30 a.m. (Kaz's bell, and Mags on the sprinter and the marathon runner) and the HSR table above it, then §15.5.2's Cox paragraph, where the bell "belongs nowhere" because waiting times cannot be negative. Chapter 5 owns mixtures.

### Z.16 Chapter 16: Post-Reorganization Equities, Rights Offerings & Bankruptcy Claims

Six exercises: two on the forced seller, one on the backstop seat, one on warrants, one at the loading dock and one on a dollarized crypto claim. Every number below was recomputed from the chapter's Blocks 1 to 5 (Appendix F, Listings 16.1 to 16.5). Write your answer down before you read ours; the gap is your markout.

**Z.16.1: The CLO that wanted a term loan**

**Answer:** (a) $\phi^{\text{OH}} = 30/65 = 46.2\%$. (b) The expected total abnormal return is $\kappa Q_0/M = 0.3 \times \tfrac12 = 15\%$, half of it earned in the first $\ln 2/3.4 = 0.20$ years (2.4 months), with a starting drift of 51% a year. (c) Electing CLOs leave 6 points of the class in CLO hands, so $\phi^{\text{OH}} = 6/(6 + 35) = 14.6\%$. With the arbitrage capital unchanged, the total abnormal return falls to $0.3 \times 6/60 = 3\%$. The half-life is still 2.4 months.

**How:** The float is everything that is neither controlled nor locked, $n^{\text{float}} = n^{\text{out}} - n^{\text{lock}}$, and that is the CLOs plus the free holders: $30 + 35 = 65$. Block 1 with constant capital ($\rho = 0$, $M_0 = M^{*} = M$) has the closed form

$$
\int_{t_0}^{\infty}\mu_t\,dt = \frac{\kappa Q_0}{M} = 0.3 \times \frac{Q_0}{2Q_0} = 0.15 .
$$

Here $\theta$ sets only the timing, not the size. In (c), 80% of the CLOs, 24 points of the class, take the term loan *instead of* stock, so those shares are never issued. The share pie becomes $6 + 35 + 35 = 76$ and the float becomes $6 + 35 = 41$. The overhang falls to $Q_0' = 0.2\,Q_0$, while $M$, the patient money willing to absorb it, has not changed: $\kappa Q_0'/M = 0.3 \times 0.2/2 = 3\%$. So the election moved four-fifths of the forced supply into an instrument the sellers are allowed to hold. At the open, every share the sponsor and the free holders own is marked 12 points closer to fundamental value, and there is much less of a seller for anyone to wait out. A buyer of the open loses the flow trade, and every holder of the stock gains.

**The trap:** Re-scaling capital to "twice the *new* overhang" gives 15% again and makes the election look irrelevant. $M$ belongs to the market, not to the seller, and it does not shrink because the CLOs sold less. The runner-up mistake in (a) is $30/100 = 30\%$, which forgets that the sponsor's locked 35% cannot trade. In (c) it is $6/65 = 9.2\%$, which keeps the electing CLOs' never-issued shares in the float.

**If you got this wrong, read:** §16.1.1 (the overhang share), §16.2.2 (the constant-capital closed form) and §16.2.1 (Mags: "Did they elect?").

**Z.16.2: Two speeds**

**Answer:** We used Block 1's other inputs ($Q_0 = 30$, $\kappa = 0.3$, $\theta = 3.42$ from the fallen-angel calibration), plus $\rho = 0.5$, $M_0 = 30$ and $M^{*} = 60$. The model's three six-month reversals are then $25.56\%$, $3.74\%$ and $0.588\%$. A single exponential through the first two gives $\hat\theta = 3.84$ and predicts $w_3 = 0.547\%$, so it falls 7% short of the true third window. The joint `least_squares` fit returns $\theta = 3.42 \pm 0.02$ and $\rho = 0.50 \pm 0.03$. It ran on the mean of a 200-name, 1.5-year panel with 2% daily noise, from a fresh `default_rng(16)`, with $\kappa$, $Q_0$, $M_0$ and $M^{*}$ held at their true values. The third window identifies $\rho$.

**How:** This extends Listing 16.1: `simulate_residual_panel` builds the panel, and the residual for `least_squares` is `ForcedSellerOverhang(...).discount(s)` minus the cross-sectional mean. The discount decays at a rate that changes over time:

$$
-\frac{d}{ds}\ln\frac{\kappa Q_s}{M_s} = \theta + \frac{\dot M_s}{M_s} = \theta + \frac{\rho\,(M^{*} - M_s)}{M_s},
$$

which falls from 3.92 at $s = 0$ to 3.57 at $s = 1.5$ as the capital settles. A single exponential through $w_1$ and $w_2$ reads the early, faster rate, so it underpredicts $w_3$. To see which parameter the third window pins down, differentiate the two log ratios. Both $\ln(w_2/w_1)$ and $\ln(w_3/w_2)$ load about $-0.49$ on $\theta$, but they load $-0.35$ and $-0.13$ on $\rho$. Their difference, which is the bend in the decay that only a third window can show, therefore loads $+0.22$ on $\rho$ and $-0.003$ on $\theta$. Two windows give one combination of the two speeds. The third separates them, and what it adds is $\rho$.

**The trap:** Reading $w_3$ straight off the panel by differencing the cross-sectional mean on two single days. Each daily mean carries noise of $0.02/\sqrt{200} \approx 0.14$ points, so the difference carries about 0.2 points, which is as large as $w_3$ itself. With seed 16 it prints 0.33% and seems to say the opposite. Use the fitted curve, or average several days at each end. The second trap is to hear "the third window identifies $\rho$" as "the tail decays at $\rho$". It does not; see the note.

**If you got this wrong, read:** §16.2.2 (*The Full Derivation*: the quotient rule behind the two drift terms), §16.2.3, and Listing 16.1 in Appendix F.

**Z.16.3: Four legs of the seat**

**Answer:** In expectation, and in \$mm on the \$500mm raise:

| Leg | Value | Share of the raise |
| :-- | --: | --: |
| Fee, paid in shares | +62.9 | 12.6% |
| Reserved allocation at a discount | +25.7 | 5.1% |
| Exclusivity option | +16.7 | 3.3% |
| The put | −10.5 | −2.1% |
| **All-in** | **+94.8** | **19.0%** |

The fee is the largest leg by a wide margin. Give it a 60% chance of surviving and it is worth \$37.7mm, still the largest, and the all-in falls to \$69.6mm (13.9%). A court can reach the fee directly. It can reach the reserved allocation and the exclusivity option only by opening the seat to the whole class, which spreads them pro rata rather than deleting them. It cannot reach the put, which is market risk borne by whoever sits in the seat. Nor can it reach the rights' own discount, which every holder already gets on equal terms.

**How:** Normalize $x_0 = 1$, so $K = 0.7$ and $m = 500/0.7 = 714.3$. A dilution factor of 0.6 makes $N_{\text{eff}} = 0.6\,m = 428.6$ and $S^{\text{post}} = 0.6\,x + 0.4\,K$. Under the chapter's driftless $\mathbb{P}$-lognormal, $\mathbb{E}[x] = 1$, so $\mathbb{E}[S^{\text{post}}] = 0.88$. The two linear legs then need no option model: the fee is $0.10 \times 714.3 \times 0.88$ and the reserved slice is $0.20 \times 714.3 \times 0.6\,(1 - 0.7)$. The other two legs use Block 2's `bs_call` and `bs_put` at $\sigma = 0.65$, $T = 0.3$ and zero rate:

$$
C_{\text{BS}}(1, 0.7) = 0.3245, \qquad \text{Put}(1, 0.7) = C - (x_0 - K) = 0.0245 .
$$

Then the exclusivity option is $0.8 \times 0.15 \times 714.3 \times 0.6 \times 0.3245 = 16.7$ and the put is $-428.6 \times 0.0245 = -10.5$, which is exactly the fair fee $f^{*} = 2.1\%$ of the raise. A million-path Monte Carlo (seed 16) matches every leg within \$0.05mm. So the seat is paid 10% for insurance worth 2.1%. Because it is paid in shares worth 0.88 rather than 0.70, the fee is really 12.6%: six times the put on its own, before the reserved slice and the exclusivity option are even counted.

**The trap:** Valuing the fee at cash, $f\,m\,K = \$50$mm. It is paid in shares, each worth $S^{\text{post}}$, not $K$. The runner-up is believing the chapter's Desk Myth that the fee is the smallest leg (see the note). The third is applying the 60% only to the fee and calling the seat "fixed". The reserved slice and the exclusivity option ride on the same exclusive seat.

**If you got this wrong, read:** §16.3.2 ("The all-in transfer" and the fair-fee derivation), the *ConvergeOne* bullet in §16.3.2's Trend Watch, and Listing 16.2 in Appendix F.

**Z.16.4: Kaz's funeral, formally**

**Answer:** The call is strictly increasing in the rate, so $C_{\text{BS}}(r + \lambda) > C_{\text{BS}}(r)$ for any $\lambda > 0$. At the Hertz inputs ($S = 10$, $K = 13.80$, $T = 30$, $r = 2\%$, $\sigma = 52\%$, $\lambda = 2\%$), the correct jump price is \$9.03, the no-jump call is \$8.66 and Kaz's haircut price is \$4.75. The going-concern spot that makes Kaz right is

$$
S^{\text{GC}} = S\,e^{\lambda T} = 10\,e^{0.6} = \$18.22, \qquad S^{\text{GC}}/S = 1.82,
$$

whatever $\sigma$ and $K$ are. In one sentence: the \$10 on the screen already prices the second Chapter 11; it is an \$18.22 value-if-Hertz-survives-to-2051 times the 55% chance it does, so Kaz's haircut belongs only on a DCF that assumes survival, and that DCF would sit 82% above the screen.

**How:** The rate sensitivity is

$$
\frac{\partial C_{\text{BS}}}{\partial r} = K\,T\,e^{-rT}\,\Phi(d_2) > 0,
$$

which is 21.0 at these inputs. Raising the rate shrinks the present value of a strike that is paid only at expiry. By the mean value theorem, any $\lambda > 0$ gives a strict increase. For the spot, put $S' = S\,e^{\lambda T}$ into Kaz's price. Then $\ln(S'/K) = \ln(S/K) + \lambda T$, so $d_1'$ and $d_2'$ are exactly the $d_1$ and $d_2$ of the call at rate $r + \lambda$, and

$$
e^{-\lambda T}\left[S e^{\lambda T}\Phi(d_1) - K e^{-rT}\Phi(d_2)\right] = S\,\Phi(d_1) - K e^{-(r+\lambda)T}\Phi(d_2) = C_{\text{BS}}(S, K, T, \sigma, r + \lambda).
$$

Kaz's price rises with $S'$, so this root is the only one, and `brentq` returns 18.2212 at 52%, 53.0% and 51.6% volatility alike. In words: a pre-default stock that drifts at $r + \lambda$ from \$10 reaches the same forward as a stock that never dies and drifts at $r$ from \$18.22.

**The trap:** Solving numerically at one volatility and reporting \$18.22 as if it were a fact about Hertz's volatility. It is a fact about survival alone: $e^{\lambda T}$. The bigger trap is Kaz's own, believing a jump to zero must make a call cheaper. That holds only when the spot ignores the jump. A market spot has already paid for the funeral, and with the dilution fixed point of Listing 16.3 the ordering survives: \$8.97 with the jump, \$8.56 without, \$4.70 haircut.

**If you got this wrong, read:** §16.4.2 ("The jump to zero" and *The Full Derivation*), with Chapter 6, §6.1.4 for the memoryless default clock.

**Z.16.5: The boat and the truck**

**Answer:** Vendor A, the boat, holds the 503(b)(9) claim. Vendor B, the truck, holds a general unsecured claim. We assume clean paperwork ($p_A = 1$) and no administrative insolvency, since the exercise gives neither. On those assumptions Block 4 prices A's claim at $0.926$ per dollar (\$1.852mm on \$2mm) and B's at $0.393$ (\$0.787mm). The slower ship was worth **\$1.07mm**, a little over half the invoice. Using the listing's own illustrative allowance and insolvency inputs (0.97 and 0.95; 5% times 50%) instead, the gap is \$1.00mm.

**How:** Under *World Imports*, goods are "received" when the debtor takes physical possession, not when title and risk pass at a foreign port. A's container was unloaded 18 days before the petition, inside the 20-day window. B's truck was unloaded 22 days out, outside it. Both claims share the timing factor

$$
\frac{h}{h + r + \psi} = \frac{1.5}{1.5 + 0.04 + 0.08} = 0.9259 .
$$

The 503(b)(9) claim is paid in full in cash on the effective date (§1129(a)(9)(A)), so its price is the timing factor alone. The GUC multiplies the timing factor by the random-pool recovery

$$
\mathbb{E}[R] = \Phi\!\left(\frac{\mu_Y}{s_Y}\right) + e^{\mu_Y + s_Y^2/2}\,\Phi\!\left(-\frac{\mu_Y}{s_Y} - s_Y\right) = 0.0044 + 0.4253 \times 0.9883 = 0.4247,
$$

with $\mu_Y = \ln 0.4$ and $s_Y = 0.35$. That gives $0.9259 \times 0.4247 = 0.3933$. Notice $0.4247 > 0.40$: this class sits deep on the impaired side of the kink, where pool uncertainty is a small gift.

**The trap:** Following the bill of lading. Title passed to the retailer 25 days out, so A "must" be outside the window, and B, at 22 days, looks only slightly late. Both readings swap the contract for the dock: the statute asks when the debtor *held* the goods. On the pricing side, the usual slips are to use $e^{\mu_Y} = 0.40$ as the recovery, which ignores Jensen's 2.5 points, or to discount at the mean wait, $e^{-0.12/1.5} = 0.923$ rather than $h/(h + r + \psi) = 0.926$. Together those slips give \$0.739mm for the GUC.

**If you got this wrong, read:** §16.5.2 (the statute block: the loading dock and §1129(a)(9)(A)), §16.5.3 ("Pricing the claim" and the closed form for $\mathbb{E}[R]$), and Listing 16.4 in Appendix F.

**Z.16.6: Short a call, paid nothing**

**Answer:** The call the customer wrote, on 1.2 BTC struck at the petition-date \$17k for 2.5 years at 60% volatility, was worth **\$7,441** at a zero rate ($1.2 \times \$6{,}201$), or \$8,094 at 4%. That is 44% of the \$17k claim. A claims buyer at 15 cents paid \$2,550 for the *whole* claim, so the call alone was worth 2.9 times the buyer's price, and the buyer turned \$2,550 into \$20,400 in cash, eight times the money. The customer was the one short volatility. Dollarization made him write the call, and selling at 15 cents also sold the estate's recovery, which the crypto rally was about to lift. The buyer was long that recovery, so in substance he held the long side of the customer's option, capped at par plus interest.

**How:** Compare the cash the customer gets with what 1.2 BTC in kind would pay. By put-call parity,

$$
1.2 \times 17{,}000 = 1.2\,A_T - 1.2\,(A_T - 17{,}000)^{+} + 1.2\,(17{,}000 - A_T)^{+},
$$

so the dollar claim is long 1.2 BTC, short 1.2 calls and long 1.2 puts at the petition price. With $\sigma\sqrt{T} = 0.949$ and zero rate, $d_{1,2} = \pm 0.474$ and $C = 17{,}000\,[\Phi(0.474) - \Phi(-0.474)] = \$6{,}201$ a coin (`bs_call` from Listing 16.2). At the money and at zero rate the put is worth the same \$7,441. The customer's protection came from the estate, though, and the estate's assets were largely the same crypto. So the put was weakest exactly when it would have paid, which is the wrong-way risk the 15-cent print was pricing, while the call was given away in full. Ex post, \$20,400 against a coin near \$100k is the chapter's 20.4% in-kind recovery.

**The trap:** Valuing the call with hindsight, at $1.2 \times (100{,}000 - 17{,}000) = \$99{,}600$. That is the realized cost of the option the customer wrote, not its value on the day it was written. The smaller slips are pricing one coin instead of 1.2 (\$6,201), or putting a \$20.4k strike on one coin (\$5,237). Both confuse the 120% payout with the 1.2-coin notional.

**If you got this wrong, read:** §16.5.3 ("Denomination risk"), the Trend Watch "Claims trading went crypto, 2023–2026" that follows it, and §16.3.2's *The Full Derivation* for the Black–Scholes arithmetic.

### Z.17 Chapter 17: Private Credit & the Public–Private Convergence

Six exercises: one on the smoothing kernel, two on reading a BDC's disclosures, one on the redemption game, one on takeout supply and one on the runway. Every number below was recomputed by running the chapter's five blocks (Appendix F, Listings 17.1 to 17.5) and extending them. Write your answer down before you read ours; the gap is your markout.

**Z.17.1: The year-long lag**

**Answer:** With $\theta_k=\tfrac14$ for $k=0,\dots,3$, the variance ratio is $\sum_k\theta_k^2=\tfrac14$. Reported volatility is therefore half the true figure, and the reported Sharpe ratio is $1/\sqrt{1/4}=2$ times the true one. The lag-one autocorrelation is $\rho^o_1=\tfrac34$; the lag-two and lag-three values are $\tfrac12$ and $\tfrac14$. ROBO's 2.1% is really **4.2%**. Measured in the same quarter, the vehicle's correlation with the loan index is **half** the true correlation. Sum the current quarter and the three lags (the whole kernel) and you get **all** of it back.

**How:** Each line comes from the §17.2.2 moments.

$$
\sum_k\theta_k^2=4\cdot\tfrac1{16}=\tfrac14,\qquad
\text{SR}^o=\frac{\text{SR}}{\sqrt{1/4}}=2\,\text{SR},\qquad
\rho^o_1=\frac{\theta_0\theta_1+\theta_1\theta_2+\theta_2\theta_3}{1/4}=\frac{3/16}{1/4}=\tfrac34 .
$$

Reported volatility is $\sigma/2$. The annualizing factor $\sqrt4$ multiplies both series equally, so the true figure is $2\times2.1\%=4.2\%$. In the same quarter, $\operatorname{Corr}(x^o_t,F_t)=\big(\theta_0/\sqrt{\sum_k\theta_k^2}\big)\rho=(\tfrac14/\tfrac12)\rho=\rho/2$. Against the summed index you get $\operatorname{Cov}\big(x^o_t,\sum_{k=0}^{3}F_{t-k}\big)=\beta\operatorname{Var}(F)\sum_k\theta_k=\beta\operatorname{Var}(F)$ with $\operatorname{Var}\big(\sum_{k=0}^{3}F_{t-k}\big)=4\operatorname{Var}(F)$ and $\operatorname{sd}(x^o)=\sigma/2$, so the correlation is $\beta\sigma_F/\sigma=\rho$. Put another way, a Dimson regression with $K=3$ has an $R^2$ of exactly $\rho^2$. We checked all of this with Listing 17.1's `simulate_smoothed` over 400,000 quarters. The measured correlations were 0.500 and 0.999 of the true correlation, and the simulated autocorrelations 0.749, 0.500 and 0.250.

**The trap:** The most common slip is to divide by the variance ratio instead of its square root, which gives $2.1\%/0.25=8.4\%$. A second is to think that calendar-year returns wash the smoothing out. They don't. A year of reported returns weights seven true quarters by $(1,2,3,4,3,2,1)/4$, so its volatility is $\sqrt{11/16}=0.83$ of the true annual figure: 3.5%, not 4.2%. A third is to stop one lag short. With lags 0 to 2 the summed correlation is only $\sqrt3/2=0.87$ of the truth, because a Dimson regression whose $K$ is smaller than the kernel's still under-reports.

**If you got this wrong, read:** §17.2.2 (the porch-thermometer box and *The Full Derivation*), §17.2.3 (summing the canyon's echoes) and Listing 17.1 in Appendix F.

**Z.17.2: Marking the discount**

**Answer:** $m=(0.96-0.62)/2.25=0.34/2.25=$ **15.1%** of reported assets. The market is carrying a book that the manager marks near 100 at about 85. Once you admit that the unsecured notes are not money-good, the true markdown is **higher**, so 15.1% is a lower bound. To find out by how much, use the Merton model of Chapter 23 (§23.1, equity as a call on firm assets, with the machinery from Chapter 6), which is the "Merton-on-a-CLO" extension that §17.3.2 points to.

**How:** The thin slice says $P/\text{NAV}=(1-\phi)-m(1+\ell)$. The fee takes 4 of the 38 points of discount, which leaves 34 points that are about the loans, and dividing by $1+\ell=2.25$ turns the equity discount into an asset markdown. Listing 17.2's `implied_markdown(0.62, 1.25, 0.04)` returns 0.1511. For the second part, drop assumption (iii). If the notes can default, their market value $D^{\text{mkt}}$ is below face $D$, and

$$
P\cdot\text{shares}=A(1-m)-D^{\text{mkt}}-\phi E\;>\;A(1-m)-D-\phi E .
$$

The price is fixed, so $A(1-m)=P\cdot\text{shares}+D^{\text{mkt}}+\phi E$ must be smaller than in the money-good case, which makes $m$ larger. In option language, limited liability gives the equity time value on top of its intrinsic value, so part of the 0.62 is option value rather than asset value. As a size check (we computed this, though the exercise doesn't ask for it): with asset volatility of 8% and a 3-year horizon, the Merton-implied $m$ stays at 15.1% (it moves only in the fourth decimal place); at 15% volatility and 5 years it rises to 16.3%. The direction is certain. The size matters only when asset volatility is high, which is precisely when the market has stopped trusting the marks.

**The trap:** The first trap is reading the equity discount as the asset discount. That gives 38%, or 34% net of fees, and forgets that the equity is a thin slice on top of a levered book. The second is dropping the fee drag, which gives $0.38/2.25=16.9\%$. In the argument, the tempting wrong answer is "lower, because the noteholders absorb part of the loss." With the price held fixed, that sharing is exactly why the equity price is *less* sensitive to the loans, so a given discount implies a *bigger* loss on the loans. Don't set a $\mathbb{Q}$-measure BDC CDS spread beside this $\mathbb{P}$ markdown without saying which is which.

**If you got this wrong, read:** §17.3.2 (the thin-slice box and *Boundary conditions*), Listing 17.2, and Chapter 23 §23.1.

**Z.17.3: The bad bucket**

**Answer:** $\hat R^{\text{mark}}_{\text{NA}}=(1.0/3.1)\times0.97=$ **0.313**, so the non-accrual loans are carried at about 31 cents per dollar of cost, with a gap of $g=2.1$pp. That is 19 cents below Octus's ~50-cent restructuring recoveries, and close to OBDC's June 2026 figure of 28 cents. Octus's ~50 cents belongs in the Chapter 14 recovery model as the prior for the restructuring-date recovery, with a wide distribution and the §14.3 re-default clock applied on top. The 31-cent mark is a signal you compare against the model's output, not something to fit the model to. Neither number is a recovery. The 31 cents is a present value of loans that have not been resolved. The 50 cents is measured at a moment the borrower chose, on other managers' loans, before any second default.

**How:** The bucket's fair value over its cost is

$$
\hat R^{\text{mark}}_{\text{NA}}=\frac{w^{FV}_{\text{NA}}\,FV}{w^{C}_{\text{NA}}\,C}=\frac{0.010}{0.031}\times0.97=0.313 .
$$

Listing 17.2's `implied_nonaccrual_mark(0.010, 0.031, 0.97)` returns 0.3129. Why neither number is a recovery: a recovery is cash or value received at resolution, per dollar of claim. The mark is a valuation committee's present value today. It is quoted per dollar of cost rather than par, it moves on the §17.2 kernel, and it covers some loans that will cure. Discount 50 cents received two years from now at a distressed rate of 20–25% and you get $0.50/1.2^2=0.35$ to $0.50/1.25^2=0.32$, so the two numbers can both be right. Octus's figure is measured *at the restructuring*, which is §14.1's "recovery at the exchange." It comes before the second default that Pluralsight's new equity went through (written to zero by February 2026), and it is a cross-section of other managers' loans rather than this book's bucket.

**The trap:** The most common slip is to put the 31 cents into the model as a recovery (an LGD of 69%), which fits Chapter 14 to one manager's opinion, lagged. The second is to read the 1.0% fair-value share as "the bad bucket is small." What matters is the cost share, and the gap between the two. Dropping the $FV/C$ factor gives 32.3 cents. That error is small here, but it grows as the whole book is marked down.

**If you got this wrong, read:** §17.3.3 (the bowl box and the OBDC table), §14.1 (two recovery rates) and §14.3 (the re-default clock).

**Z.17.4: Kaz's fix**

**Answer:** With no redemptions the true value is $1-m=0.920$ of NAV per share. **Under a 5% cap** ($p=0.05$) the stayers hold $(0.92-0.05)/0.95=$ **0.9158**: they lose 0.42 points, and the transfer is $p\,m=0.40\%$ of NAV. **Under Kaz's 100% cap** ($p=0.40$) they hold $(0.92-0.40)/0.60=$ **0.8667**: they lose 5.33 points, and the transfer is $3.2\%$ of NAV, all of it borne by the 60% who stayed. The markdown left on the surviving shares compounds as $m/(1-p)$, to 8.4% after a capped quarter and to 13.3% after Kaz's.

**How:** Use $N^{\text{true}}_{\text{stay}}=N\big((1-m)-p\big)/(1-p)$ with $p=\min(a,c)$, which is Listing 17.4's `stayer_value(1.0, 0.08, 0.40, cap)`. The new markdown on the shares that stay is

$$
m'=1-\frac{(1-m)-p}{1-p}=\frac{m}{1-p}.
$$

The game has not ended, because requesting still dominates whenever $m>0$. Under the cap a requester gets $0.125\times1+0.875\times0.9158=0.926$ against 0.916 for staying, an edge of about 1 point. Under Kaz's cap she gets 1.00 against 0.867, an edge of 13 points. Without rationing the edge compounds: at 40% requests a quarter, $m$ goes 8% → 13.3% → 22.2% → 37.0% → 61.7% → above 100% in quarter five. At that point the fund cannot pay $N$ to everyone, and whoever is last gets nothing. Liquidity makes it worse. With cash at 0.2% and leverage of 0.9x, paying 40% of NAV means selling about $0.40/1.9\approx21\%$ of the loan book in one quarter, and the fire-sale discount raises the realized $m$. That is Diamond–Dybvig. With sequential service and illiquid assets, a run is a self-fulfilling equilibrium even when the marks are honest. Their remedies are suspension of convertibility, which is the gate, or the cap Kaz wants to remove, and deposit insurance or a lender of last resort (here, the sponsor's house money, like BCRED's \$400mm). They would have told Kaz that the queue is the visible price of preventing the run. To actually end the game you need $m=0$: faster marks, or paying redeemers nearer true value through a repurchase fee or swing price sized to $m$.

**The trap:** One slip is to give 0.92 under both caps, which forgets that leavers are paid at the smoothed NAV. Another is to use $p=a=0.40$ under the 5% cap as well and get 0.867 twice. The conceptual trap is to call the 100% cap "fairer because nobody is trapped." It is fairer only to the people who leave first.

**If you got this wrong, read:** §17.6.2 (the pizza box, *The game* and *The Full Derivation*), Listing 17.4, and Chapter 23 §23.8 (a run is not a diffusion).

**Z.17.5: Takeout season**

**Answer:** We used block 3's illustrative book (400 loans, seed 2023) with its spread differential $\Delta s=1$pp. Competing-risks supply at $\zeta=0$ is \$3,757mm, and it halves at $\zeta\approx$ **0.88**, which is 0.88 standard deviations of the excess loan premium. That is very close to the one-door shortcut $\ln2/|\psi_B|=\ln2/0.8=0.87$. The naive estimate overstates the competing-risks one by **1.3%** at $\zeta=-1$ (loose), 1.8% at $\zeta=0$, **2.6%** at $\zeta=+1$ (tight) and 3.6% at $\zeta=+2$. In dollars the overstatement *shrinks*, from \$105mm to \$44mm, because tight-regime supply (\$1,705mm) is about a fifth of loose-regime supply (\$8,091mm).

**How:** Supply is $S(\zeta)=\sum_i\text{Face}_i\,\kappa^{(B)}_i\Delta t\,g(\mathcal{K}_i\Delta t)$ with $g(y)=(1-e^{-y})/y$ and $\kappa^{(B)}\propto e^{-0.8\zeta}$. If $g$ were constant, supply would halve at $\ln2/0.8$. As $\zeta$ rises, the syndicated door narrows faster than the other doors widen. The face-weighted total hazard falls from 0.38 to 0.31, so $g$ rises slightly, and supply falls a little more slowly than $\kappa^{(B)}$. Root-finding on `bsl_supply` gives 0.878 (0.870 with $\Delta s=0$). For the overstatement, expand $g(y)\approx1-y/2$:

$$
\frac{1-e^{-\kappa^{(B)}\Delta t}}{\frac{\kappa^{(B)}}{\mathcal{K}}\big(1-e^{-\mathcal{K}\Delta t}\big)}=\frac{g(\kappa^{(B)}\Delta t)}{g(\mathcal{K}\Delta t)}\approx1+\tfrac12\big(\kappa^{(P)}+\kappa^{(X)}+\lambda\big)\Delta t .
$$

The overstatement is half of one quarter's hazard on the *other* doors. Because $\psi_P,\psi_X,\psi_D>0$, those doors widen as the market tightens: their face-weighted hazard rises from 0.109 to 0.210, and the approximation gives 1.4% and 2.6%, against the exact 1.3% and 2.6%. For a CLO-demand forecast (Chapter 21), the error points one way and is largest in proportion exactly when collateral is scarce, which is when the forecast matters. The loans it counts in are ones that were amended into PIK or defaulted, and neither kind is CLO collateral. The bias moves with the regime, so no constant calibrates it away. Keep the sizes in view, though. With these illustrative hazards the correction is 1–4%, while the regime itself moves supply by −79%, so get $\zeta$ right first. On the software-only subset the overstatement is already 3.1% at $\zeta=+1$, and a book whose other-door hazards are several times larger has a correction several times larger.

**The trap:** One wrong answer is $\zeta=\ln2/0.8=0.87$ from the syndicated hazard alone. It is close here, but only because $\mathcal{K}\Delta t$ is small, so say why it is close. Another is to compare dollar gaps and conclude that the naive estimate overstates *less* in the tight regime. "By more" only makes sense as a fraction of supply.

**If you got this wrong, read:** §17.4.2 (the three-doors box and *Why the competition term matters*), Listing 17.3, and Chapter 21 for the CLO-demand side.

**Z.17.6: The thirteen-week model, reborn**

**Answer:** Your fund's numbers will differ, so here is a worked version on the chapter's illustrative stack: cash 0.2% of NAV, an undrawn line of 10%, a 10% sleeve haircut by 10%, 5% redemptions, unfunded draws of 2% a quarter, no maturities in the window and repayments of 3% a quarter. That gives $\mathcal{T}=0.192/0.04=$ **4.8 quarters**. Halve repayments to 1.5% and it falls to $0.192/0.055=$ **3.5 quarters**; with no repayments, 2.7. If the borrowing base excludes PIK and non-accrual loans, and that cuts the undrawn line from 10% to 6% of NAV, the runway falls to 3.8 and **2.8** quarters. Every version sits below the IMF's moderate-shock range of 5–7 quarters, and none of them should be trusted until you have read the credit agreement's eligibility and advance-rate definitions.

**How:** Fill in $\mathcal{T}=\big(\text{Cash}+\text{Undrawn}+\text{Sleeve}(1-h)\big)\big/\big(c\cdot\text{NAV}+\text{Unfunded draws}+\text{Maturities}-\text{Repayments}\big)$ from the 10-Q.

- Cash comes from the balance sheet.
- Undrawn lines come from the borrowings note or the MD&A liquidity section. Take availability *under the borrowing base*, not the commitment.
- The sleeve is the broadly syndicated, Level 2 loans in the schedule of investments.
- Unfunded commitments are in the commitments note. Convert them to a quarterly draw rate.
- Maturities are in the borrowings note.
- Trailing repayments are "repayments and sales" in the investment-activity table or the cash-flow statement.

The runway is convex in repayments, because $\partial\mathcal{T}/\partial\text{Rep}=\text{numerator}/\text{denominator}^2$. At 3% repayments, each point of NAV per quarter is worth 1.2 quarters of runway, which is why halving them costs 1.3 quarters. Listing 17.4's `runway_quarters` reproduces every figure above. Halving is, if anything, mild. In block 3 (Listing 17.3) the face-weighted quarterly probability of a syndicated or private takeout, which is what a repayment is, falls from 12.8% at $\zeta=-1$ to 4.6% at $\zeta=+1$, a cut of nearly two-thirds.

**The trap:** One trap is to treat the commitment as the undrawn line. The borrowing base usually excludes or haircuts PIK, non-accrual and over-concentrated loans, so availability shrinks exactly when the queue lengthens, which is Theo's question from the cold open. Another is to use trailing repayments from the 2024–25 refinancing wave as though they were a constant; they are the §17.4 hazards, and they fall when $\zeta$ rises. A third is to value the sleeve at par when every fund is selling the same loans the same week. Check also whether the facility sweeps repayments to pay down the line, because then they cannot be counted twice. The 1940 Act's 150% asset-coverage test is rarely the first constraint at 0.9x leverage; the borrowing base binds first.

**If you got this wrong, read:** §17.6.2 (*Liquidity runway* and *The Full Derivation*), Ways This Blows Up (3) in §17.6, §17.4.2 for the repayment hazards, and Listing 17.4 in Appendix F.
