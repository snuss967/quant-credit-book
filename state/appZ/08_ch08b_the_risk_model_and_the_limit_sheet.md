## Z.8-B Chapter 8-B: The Risk Model You Run Every Morning: Factors, Idiosyncratic Variance, Jump-to-Default, Stress and the Limit Sheet

Seven exercises, none tagged [Read], [Derive] or [Build], each with a two-line solution already printed under it. I did not copy those: I reran every number in Python (the mixture by exact integration and again through Listing 8-B.1 of Appendix F, §F.8-B, unchanged, with two million Monte Carlo paths; Kupiec, Christoffersen, the JTD arithmetic and the sizing by hand and through the same listing), then wrote the long version. Every printed number holds up. The four NOTEs below are about logic and cross-references, and the one that matters is Exercise 6, where the printed sentence can still be read in a way that lets ROBO pass. Exercises 2 to 4 extend Listing 8-B.1 and are worth doing at a keyboard; Exercise 6 is the odd one out, because it asks for a sentence, not a number. Units are \$mm and decimals unless stated, losses are positive, and every probability here is physical ($\mathbb{P}$): the jump layer uses the desk's own default hazard and recovery view, and a backtest compares realised losses with a forecast. No risk-neutral quantity appears in these exercises.

**Z.8-B.1: Quadrature, in DTS**

**Answer:** The two bonds' stand-alone monthly volatilities are \$35.2k and \$79.2k, and the pair's is **\$104.2k** a month, against \$114.4k if they moved in lockstep. The DTS-0.09 bond owns **\$76.3k of it, 73.2%**, though it is half the capital. All of this is realised (physical) monthly P&L volatility, in thousands of dollars on \$10mm per bond.

**How:** Section 8.4's slope says excess-return volatility is proportional to DTS, $\sigma_i = \kappa\,\text{DTS}_i N_i$ with $\kappa = 8.8\%$ a month. So $\sigma_A = 0.088 \times 0.04 \times 10{,}000 = 35.2$ and $\sigma_B = 0.088 \times 0.09 \times 10{,}000 = 79.2$ (\$k). Quadrature with $\rho = 0.6$ gives

$$
\sigma_p = \sqrt{35.2^2 + 79.2^2 + 2(0.6)(35.2)(79.2)} = \sqrt{1{,}239 + 6{,}273 + 3{,}345} = \$104.2\text{k}.
$$

Diversification is worth $114.4 - 104.2 = \$10.2$k, about 9%. Euler splits the \$104.2k exactly: position $i$ owns $\sigma_i(\sigma_i + \rho\sigma_j)/\sigma_p$, so $B$ owns $79.2\,(79.2 + 21.1)/104.2 = 76.3$ and $A$ owns $35.2\,(35.2 + 47.5)/104.2 = 27.9$, and $76.3 + 27.9 = 104.2$. Because both volatilities are proportional to DTS, $\kappa$ and the notional cancel from the shares: with $d = \text{DTS}$, $B$'s share is $d_B(d_B + \rho d_A)/(d_A^2 + d_B^2 + 2\rho d_A d_B) = 0.01026/0.01402 = 73.2\%$ for any equal-sized pair.

**The trap:** Reading the share off the wrong object. The variances give 83.5% ($6{,}273/7{,}512$), which is the answer at $\rho = 0$; adding volatilities (\$114.4k, share 69.2%) is the answer at $\rho = 1$. The truth sits between them, 73.2%, because the cross term $2\rho\sigma_A\sigma_B$ is real risk that belongs to somebody, and Euler hands each bond its own variance plus half of it. A smaller slip is the units: DTS 0.04 means 4 years of spread duration times a 1% spread, so $8.8\% \times 0.04 = 0.352\%$ of the position a month, not 35.2%.

**If you got this wrong, read:** §8B.1 (the two "Math, Gently" boxes: quadrature, then Euler) and §8.4 ("The derivation", where $\sigma \approx \kappa\,\text{DTS}$ comes from).

**Z.8-B.2: The square root of ten**

**Answer:** One-day 99% ES on the mixture is **\$3.79mm**, ten-day is **\$10.83mm**, and the $\sqrt{10}$ shortcut gives \$11.99mm, so it **overstates** the ten-day ES by \$1.16mm (the mixture is 0.90 of the shortcut). The VaRs tell the same story with a different size: 2.41 and 8.92 against a shortcut of 7.62. Physical measure, \$mm, losses positive, a day is a trading day.

**How:** Write the loss as a Gaussian plus a jump, $L = G + 8\cdot\mathbf{1}\{\text{default}\}$. The Gaussian layer scales with $\sqrt{h}$, so $\sigma_h = \sqrt{h}\,\$1\text{mm}$. The default probability scales with $h$: $p_h = 1 - (1 - 0.002)^h$, which is 0.200% at one day and 1.982% at ten. Find the quantile $q$ from $(1-p_h)\,\Phi(q/\sigma_h) + p_h\,\Phi((q-8)/\sigma_h) = 0.99$, then average the tail state by state:

$$
\text{ES}_{99\%} = \frac{1}{0.01}\Big[(1-p_h)\,m_0 + p_h\,m_8\Big], \qquad m_\mu = \mu\,\Phi\!\Big(\frac{\mu - q}{\sigma_h}\Big) + \sigma_h\,\varphi\!\Big(\frac{q-\mu}{\sigma_h}\Big).
$$

At one day $q = 2.41$: the default days (0.2% of days, all above $q$) supply 1.60 of the ES and the Gaussian days (the other 0.8%) supply 2.19, total 3.79. At ten days $q = 8.92$, and now defaults fill 0.76% of the 1% tail and Gaussian days only 0.24%: $8.52 + 2.32 = 10.83$. The shortcut is $\sqrt{10} \times 3.79 = 11.99$. The sign of the error flips with the jump's size because two things happen at once: the jump's share of the ES grows 5.3 times (1.60 to 8.52, faster than $\sqrt{10}$), but the Gaussian share is crowded out of the tail (2.19 to 2.32, not 3.16 times). At 0.2% a day the break-even JTD is about \$12mm: below it the shortcut overstates (\$8mm gives 0.90 of the shortcut), above it understates (\$20mm gives 1.15). To run it, take the §8B.6 self-check in Listing 8-B.1 and set `jump = {"J": [(8.0, 0.0, (1.0, 1.0))]}` with a daily default probability of 0.002; two million paths give 3.77 and 10.83 with standard errors of 0.015 and 0.012.

**The trap:** Taking the $\sqrt{10}$ shortcut, \$11.99mm, and calling it conservative. Here it is, by 11%. On Table 8-B.2's \$20mm jump the same shortcut is 23% short, and the committee cannot tell the two books apart from the one-day number. A second slip is folding the jump into a bigger Gaussian variance and scaling that: it describes no day the desk will ever have (§8B.5).

**If you got this wrong, read:** §8B.6 (the "Math, Gently" boxes on VaR, ES and mixtures, and on the random walk, plus Table 8-B.2), then §5.1 ("One Bond, Two Worlds: The Survive-or-Jump Mixture").

**Z.8-B.3: Kupiec**

**Answer:** $\text{LR}_{\text{POF}} = 5.50$ (p-value 0.019). It **rejects the model at 5%** (critical value 3.84) and **does not reject at 1%** (6.63). The null is the physical frequency $p = 0.01$ of loss days beyond the published 99% VaR.

**How:** If the model is right, the exception count is binomial with $n = 250$, $p = 0.01$: mean 2.5, standard deviation 1.57, and $\mathbb{P}(X \ge 7) = 1.4\%$. The likelihood ratio compares the model's $p = 0.01$ with the best-fitting rate $x/n = 7/250 = 0.028$:

$$
\ln L_0 = 243\ln 0.99 + 7\ln 0.01 = -34.678, \qquad \ln L_1 = 243\ln 0.972 + 7\ln 0.028 = -31.930,
$$

$$
\text{LR}_{\text{POF}} = -2\,(-34.678 + 31.930) = 5.497 \sim \chi^2_1 .
$$

Compare with 3.84 for a 5% test and 6.63 for a 1% test. `kupiec_pof(7, 250, 0.01)` in Listing 8-B.1 returns (5.497, 0.019). To see how thin the margin is, move the count: six exceptions give 3.56 (survives at 5%), eight give 7.73 (rejects even at 1%). The test is also two-sided: zero exceptions in 250 days gives $-2 \times 250 \ln 0.99 = 5.03$, which also rejects at 5%, because a model that never fails is overcharging for risk.

**The trap:** Announcing a verdict without a level. "The model fails" is true at 5% and "the model passes" is true at 1%, and both are correct readings of the same 5.50. Pick the level before you look (the desk's backtest procedure of §8B.8 is a written finding, not a mood), and say which one you used. A second slip is to compare 5.50 with 2.5 and call it "twice the expected count": the statistic is a likelihood ratio, and its scale is the $\chi^2_1$ table, not a multiple of the expectation.

**If you got this wrong, read:** §8B.8 ("The Backtest", the "Math, Gently" box on counting exceptions and the Kupiec paragraph under it). The chapter also points to §7-B.2 for the likelihood-ratio idea, but see the first NOTE below.

NOTE (for the editor): The "Math, Gently" box in §8B.8 says of the likelihood ratio and the $\chi^2$ distribution "The full version is §7-B.2", and the "Builds on" line lists §7-B.2. Section 7-B.2 is "Overlapping Returns, Autocorrelation and Newey–West": it has no likelihood-ratio test, no binomial counting and no $\chi^2$ test, and a search of all of Chapter 7-B finds no $\chi^2$ anywhere (the nearest material is the maximum-likelihood logit of §7-B.3 and the survival likelihood of §7-B.4). Kupiec and Christoffersen are named nowhere in the book outside Chapter 8-B and its Appendix F listing. Either a short box on likelihood-ratio tests belongs in Chapter 7-B, or the pointer should go.

NOTE (for the editor): §8B.8 says Basel's yellow zone (five to nine exceptions in 250 days) is "the same verdict in another dialect". It matches only at seven. By my computation Kupiec's LR is 1.96 at five exceptions (p = 0.16) and 3.56 at six (p = 0.059), so it does not reject at 5% where Basel already says yellow; it first rejects at 5% at seven (5.50) and at 1% at eight (7.73, p = 0.005), nine gives 10.23 (p = 0.001), where Basel is still yellow. The Basel zones come from cumulative binomial probability (89.2% at four, 95.9% at five, 99.975% at nine, 99.995% at ten), a one-sided rule with its own cut-offs. "A neighbouring verdict" would be accurate; the exercise's check line ("the yellow zone of Basel's traffic light") leans on the same equivalence.

**Z.8-B.4: Christoffersen**

**Answer:** On timing alone the model is **not** rejected: $n_{00} = 235$, $n_{01} = n_{10} = 7$, $n_{11} = 0$, so $\hat\pi_{01} = 7/242 = 2.9\%$, $\hat\pi_{11} = 0$, and $\text{LR}_{\text{ind}} = 0.41$ (p = 0.52). Conditional coverage is $5.50 + 0.41 = 5.90$ (p = 0.052), just under the $\chi^2_2$ 5% value of 5.99, so the omnibus test survives at 5% by a hair. The count test, Kupiec's 5.50, still rejects at 5%. Physical measure; a 250-day window with seven interior, non-adjacent exceptions.

**How:** Each isolated exception creates exactly one quiet-to-exception step and one exception-to-quiet step and no exception-to-exception step. Over the 249 transitions of a 250-day window that gives $n_{01} = n_{10} = 7$, $n_{11} = 0$, $n_{00} = 249 - 14 = 235$. The pooled rate is $\hat\pi = 7/249 = 2.81\%$, and the two conditional rates are $\hat\pi_{01} = 7/242 = 2.89\%$ and $\hat\pi_{11} = 0/7 = 0$ (the term $0\ln 0$ is zero). Then

$$
\text{LR}_{\text{ind}} = -2\ln\frac{(1-\hat\pi)^{242}\,\hat\pi^{7}}{(1-\hat\pi_{01})^{235}\,\hat\pi_{01}^{7}\cdot 1^{7}\cdot 1} = 0.405 \sim \chi^2_1 .
$$

It is tiny because an exception after a quiet day (2.89%) is about as likely as an exception on an average day (2.81%): nothing is bunching. Compare the chapter's clustered seven, with $n_{11} = 3$ and $\hat\pi_{11} = 43\%$: 13.49. Same count, different timing, and the 13.1 points of difference are the whole information in the clustering. For the joint test, $\text{LR}_{\text{cc}} = 5.497 + 0.405 = 5.902$ against 5.99 at 5% (9.21 at 1%). `christoffersen_ind` in Listing 8-B.1 returns (0.405, 0.525, (235, 7, 7, 0)) for seven spread-out days. The counts do not depend on which interior days you choose; an exception on the first or last day shifts one of them by one.

**The trap:** Reading "independence passes" as "the model passes". The count is the problem here, and the clustering test cannot see it. The mirror-image slip is to read 5.90 under 5.99 as an endorsement: the same seven exceptions fail Kupiec at p = 0.019, and the joint test only slips under 5% because it spends a second degree of freedom on a statistic that adds 0.4 (its p-value is 0.052, worse than Kupiec's alone). The three statistics answer three questions, how often, how bunched, and both, and you read them together.

**If you got this wrong, read:** §8B.8 ("The Backtest", the paragraphs on Christoffersen, the transition counts and Figure 8-B.4).

**Z.8-B.5: The Halvorsen book**

**Answer:** The **issuer JTD, top-ten row** binds, not DTS or ES. Halvorsen's JTD is **\$9.12mm**; after the CCC downgrade its limits are 4.0 soft and 5.5 hard, so the book is over the hard line by \$3.62mm and over the soft line by \$5.12mm. To get inside the hard line by the close, shed **\$3.62mm of JTD**, for example about **\$5.75mm face** of the 7.25% notes at 0.63 of JTD per dollar of face (JTD then \$5.50mm, on the line; a little more gives margin). To clear the soft line as well, sell about \$8.1mm face. Recoveries are the desk's own means under $\mathbb{P}$, units \$mm.

**How:** JTD is a sum over the issuer's instruments, $\text{JTD}_i = \sum_j N_j (P_j - R_j)$, with price and recovery as fractions of par:

$$
\text{JTD}_{\text{Halv}} = 12\,(0.78 - 0.15) + 6\,(0.31 - 0.05) = 7.56 + 1.56 = \$9.12\text{mm}.
$$

Both notes default on the same afternoon and both are long, so they add into one number against one line (Listing 8-B.1's `jtd_overlay` and `mean_jtd` return 9.12). The line is set by issuer rating, and the downgrade moves the issuer from the B row (7.0 soft, 9.0 hard) to the CCC row (4.0, 5.5). Nothing traded, and the exposure did not change; the limit fell by 39%. Per dollar of face the 7.25% notes carry 0.63 of JTD and the junior note only 0.26, so the junior note cannot do the job alone: selling all \$6mm removes 1.56. Selling $x$ of the senior notes gives $9.12 - 0.63x = 5.5$, so $x = 3.62/0.63 = 5.75$, leaving \$6.25mm face and $6.25 \times 0.63 + 1.56 = 5.50$. For the soft line, $5.12/0.63 = 8.13$. A hard breach means reduce by the close or a written override with an expiry date; the soft one is a written explanation by noon (Table 8-B.4).

**The trap:** Stopping at the B row. At 9.12 against a hard 9.0 the book looks \$0.12mm over, a rounding trim, and the downgrade looks like a footnote. The downgrade is the event: the same exposure now sits against a line \$3.5mm lower. Close behind are measures that are not JTD: market value (\$11.22mm), face times one minus a flat 40% recovery (\$10.8mm), or the 40-to-15 recovery change forgotten, which gives $12(0.78 - 0.40) + 6(0.31 - 0.05) = \$6.12$mm and makes the breach look like \$0.6mm instead of \$3.6mm.

**If you got this wrong, read:** §8B.5 ("The Jump Layer", the $\text{JTD}_i$ formula and the Brambleworth netting), §8B.9 ("The sheet", Table 8-B.4), and the cold open for why the recovery view belongs to whoever reads the 8-K.

NOTE (for the editor): The exercise sends the reader to §12B.9 for "the issuer whose bankruptcy" follows, but the two chapters disagree about the paper. Section 12B.9's table has the 7.25% notes due 2029 as \$500mm of *senior secured* notes, pari passu with the term loan, priced at 61 on 23 November and recovering 60.8% under the plan; the unsecured bonds are the 6% 2031s (price 9, plan recovery 1.5%) and the 3% 2045s, and there is no junior note at 31. Chapter 8-B treats the same 7.25% 2029s as a senior unsecured bond (the "40 every senior unsecured bond gets", cut to 15). If the exercise's recovery for the notes were §12B.9's 60.8%, their JTD would be $12(0.78 - 0.608) = \$2.06$mm and nothing would need clearing. The October 15% is the desk's pre-petition view, so the numbers can both stand, but the exercise should say the junior note is a stand-in rather than a §12B.9 claim, and the name differs too: Halvorsen Building Products in the cold open, Halvorsen Packaging in §8B.9 and Chapter 12-B.

