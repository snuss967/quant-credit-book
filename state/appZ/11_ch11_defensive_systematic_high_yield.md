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

