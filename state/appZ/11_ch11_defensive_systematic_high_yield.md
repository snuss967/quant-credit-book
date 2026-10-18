## Z.11 Chapter 11: Defensive Systematic High Yield

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

**How:** Look for the words in the sentence that leave a degree of freedom. "Minimize realized defaults" sets no breadth requirement, so concentration games the objective (portfolio 1). "Beating the index" has no risk unit, so leverage, or any extra beta, games it (portfolio 2). "Defaults" has no definition, so the label games it (portfolio 3). Each constraint closes one of those gaps. The issuer cap and DTS band set the risk unit at the benchmark's, as in §11.7. The long-only and DTS-max guard is the no-leverage rule of §11.8. The label is fixed by the spec rather than chosen by the optimizer. Then "beat the index" should be stated as an excess-return objective on DTS-matched risk, reported with $U$, $D$, $\beta^{+}$, $\beta^{-}$ on benchmark regimes. That is Desk Debrief's spec almost word for word.

**The trap:** Writing a constraint that sounds right and does not bind. A minimum number of *bonds* is the usual one: a capital structure with 47 lines satisfies it with one issuer. Another is a market-value-neutral or tracking-error limit with no DTS term, which lets the dimmer switch back in at a beta of 0.85. The third is a default definition left in a vendor's hands: Marisol's Tuesday in §11.4 shows a vendor moving every exchange's date overnight.

**If you got this wrong, read:** the §11.2 Specification (ROBO's T-bill portfolio), §11.4.3 (the desk label), §11.7.2 and the §11.7 Specification (IDO, the issuer cap and the refusal to lever), and The Spec You Hand the Robot after the Desk Debrief.

