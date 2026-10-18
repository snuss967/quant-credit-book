## Z.7-B Chapter 7-B: The Statistician's Toolbox for Credit Panels: Regression, Logistic Models, Survival Analysis, Shrinkage, PCA, Bootstrap and Monte Carlo

This chapter has six exercises, all in the end-of-chapter set, and none carries a [Read]/[Derive]/[Build] tag; each is a new-numbers variation on a scene the chapter has already walked through, so there is no [Build] exercise to extend Listing 7-B.1, though its `kaplan_meier`, `nw_lags` and `first_passage_mc` supply cross-checks for three of the answers below. Everything is a physical-measure, realized-data calculation (t-statistics and probabilities, so no units to trip on), except Exercise 5's driftless first-passage process, where drift cancels in the bridge anyway. I recomputed every number in Python. Five of the printed brief solutions are right; the sixth (Exercise 5) uses an approximation as if it were the converged value, and carries one NOTE for the editor.

**Z.7-B.1: More CUSIPs**

**Answer:** The clustered t is $4.0/\sqrt3 = 2.31$ before and $4\sqrt2/\sqrt{5.5} = 2.41$ after. No number of extra rows can take it past $2.53$. Doubling the rows bought you 0.10 of t; the unreachable limit of infinitely many rows would buy 0.22. The classical $5.66$ is fiction. (A regression of realized returns on an issuer-level signal, so physical measure; t-statistics are dimensionless.)

**How:** An issuer-level signal is the same on every sibling, so $\rho_x = 1$ and the Moulton factor of (7B.3) is $1 + (m-1)\rho_u$: 3 at $m = 5$, 5.5 at $m = 10$. The classical t grows with the square root of the row count (same coefficient, same residual variance), so it goes from 4.0 to $4\sqrt2 = 5.66$, and the clustered t divides that by the square root of the factor:

$$
t_{m=5} = \frac{4.0}{\sqrt{3}} = 2.309, \qquad t_{m=10} = \frac{4\sqrt2}{\sqrt{5.5}} = 2.412 .
$$

For the ceiling, write the true variance of the slope as $\tfrac{1}{G}\big(\rho_u + \tfrac{1-\rho_u}{m}\big)$, which is $0.6/G$ at $m = 5$, $0.55/G$ at $m = 10$ and $0.5/G$ as $m \to \infty$. The t scales as the inverse square root of that, so the ceiling is $2.309\sqrt{0.6/0.5} = 2.530$. Equivalently, an issuer's effective breadth $m/(1 + (m-1)\rho_u)$ is 1.67 bonds, then 1.82, and never more than $1/\rho_u = 2$. (A simulation of 300 issuers reproduces the variance ratios, 3.0 and 5.4 against 3.0 and 5.5.) The only way up is more issuers: doubling $G$ takes 2.31 to 3.27.

**The trap:** Reporting 5.66 because "twice the rows, $\sqrt2$ more t". The classical formula rewards every row as a new hand; the eleven-Halvorsen lesson is that siblings carrying the same signal are one hand in different clothes. The milder version of the same mistake is "2.31 to 2.41 means siblings help a bit, so keep adding them". They help on a curve that flattens at 2.53.

**If you got this wrong, read:** §7-B.1, "Issuer clustering: the meat that knows about siblings" (equation 7B.3 and Figure 7-B.1) and the Full Derivation of the Moulton factor; §28.2, "Effective Breadth When Issuers Cluster".

**Z.7-B.2: A rumor repeated six times**

**Answer:** The honest t is $3.0/\sqrt6 = 1.22$. Newey–West gives $1.49$ at $L = 5$ (variance multiplier $4.06$, 68% of the true 6) and $1.34$ at $L = 11$ (multiplier $5.03$, 84%). All three sit below 2. (Realized returns, physical measure; t-statistics are dimensionless.)

**How:** Fifteen years sampled monthly is $T = 180$ observations of a six-month return, which is only 30 non-overlapping half-years. With i.i.d. monthly returns, two overlapping returns $k$ months apart correlate at $1 - k/6$ for $k < 6$ and zero beyond. The long-run variance multiplier of the sample mean is $1 + 2\sum_{k=1}^{5}(1 - k/6) = 6 = h$, so the naive t is too big by $\sqrt6$. Newey–West weights lag $k$ by $1 - k/(L+1)$, so it recovers

$$
1 + 2\sum_{k=1}^{5}\Big(1 - \frac{k}{L+1}\Big)\Big(1 - \frac{k}{6}\Big) =
\begin{cases} 1 + 2\cdot\tfrac{55}{36} = 4.056, & L = 5,\\[2pt] 1 + 2\cdot\tfrac{145}{72} = 5.028, & L = 11,\end{cases}
$$

and $t = 3.0/\sqrt{\text{multiplier}}$ gives 1.49 and 1.34. At $L = 11 = 2h - 1$ the Bartlett weights on the five lags that matter run from 0.92 down to 0.58, against 0.83 down to 0.17 at $L = 5$, so less of the triangle is shaved off; that is why the desk's `nw_lags(180, overlap=6)` returns 11, where the plug-in rule alone would say 4. Two finite-sample footnotes: the exact multiplier for a mean over 180 months is 5.94, so the honest t is 1.23, and in 3,000 simulated 180-month samples the NW multipliers average 3.9 and 4.7, so both NW t-statistics are if anything slightly generous. Put the six non-overlapping subsamples beside them, as §7-B.2 advises.

**The trap:** Reporting 1.49, the textbook $L = h - 1$ answer, as "the corrected t". It is still $\sqrt{6/4.06} = 1.22$, or 22%, too large, and it is the one most likely to survive a code review because it came from a recognized estimator. The cruder version is dividing by $h$ rather than $\sqrt h$ (3.0 becomes 0.5).

**If you got this wrong, read:** §7-B.2, "How much overlap inflates a t-statistic", "The Newey–West estimator" and the Full Derivation "the overlap triangle and the Bartlett shortfall"; the Long Scene "One March, Counted Once" in §7-B.1, for what happens when the horizon is a big slice of the sample.

**Z.7-B.3: The fallen angel's missing years**

**Answer:** With left truncation, $\hat S(36) = 0.8 \times 0.8 \times 0.75 = 0.48$, so $\widehat{\text{PD}}(36) = 52\%$ with Greenwood variance $0.0422$ and a standard error of about 21 points (20.6). Counted from month 0 the entrant joins the first risk set, $\hat S = \tfrac56 \times \tfrac45 \times \tfrac34 = 0.50$, and the PD reads 50%. (A physical-measure, cumulative probability over the cohort's 36-month window.)

**How:** Rebuild the risk sets at the three events from the practice cohort. At month 14 five issuers are being watched (Quillfeather, Larkspur, Halvorsen, Halyard, Brambleworth; Calloway left at 9) and the fallen angel is not yet among them, because it enters at 18. At 22 the entrant is in: four old names plus one, so 5. At 27 it is 4 (Halvorsen, Halyard, Brambleworth and the entrant; Halyard is not acquired until 30). Each event has $d_j = 1$:

$$
\hat S(36) = \Big(1 - \tfrac15\Big)\Big(1 - \tfrac15\Big)\Big(1 - \tfrac14\Big) = 0.48, \qquad
\widehat{\operatorname{Var}} = 0.48^2\Big(\tfrac{1}{5\cdot 4} + \tfrac{1}{5\cdot 4} + \tfrac{1}{4\cdot 3}\Big) = 0.2304 \times 0.1833 = 0.0422 .
$$

Counting from month 0 changes exactly one factor, month 14, where the denominator is 6 instead of 5. That is immortal-time bias: the entrant sits in the denominator for 18 months in which it was not a member of this cohort and could not have failed in it. The error is only two points here because just one event precedes the entry date; it grows with the number of earlier events and late entrants, and a bigger panel does not shrink it (the standard error falls, the bias stays). Listing 7-B.1's `kaplan_meier(times, events, entry=...)` reproduces 0.48 and 0.0422, and 0.50 and 0.0417 without the entry argument.

**The trap:** Adding the entrant as a seventh issuer present from the start, which is the 0.50 above. The second wrong answer is to call it a survivor and count defaults over names: $3/7 = 43\%$. The third is to drop it because "it has no history", which returns 0.40 and 60% and throws away the 18 months it was legitimately at risk.

**If you got this wrong, read:** §7-B.4, "Censoring and truncation, defined" (left truncation and immortal-time bias) and "Kaplan–Meier, derived" with the practice cohort and its table; the Full Derivation of Greenwood's formula in the same section.

**Z.7-B.4: One factor per coffee**

**Answer:** One factor. With $q = N/T = 250/60 = 4.17$ the Marchenko–Pastur edge is $(1 + \sqrt q)^2 = 9.25$, or 10.17 with the 10% margin the desk uses. Only 14.1 clears it. The 8.7 is below the edge and the 6.2 is deep in the noise. At least 191 eigenvalues are exactly zero. (Residual correlations from a physical-measure panel; eigenvalues are in units of the average variance, so dimensionless.)

**How:** The edge is for the eigenvalues of a correlation matrix of unit-variance noise, with the ratio of series to observations, not the reverse:

$$
\sqrt q = 2.041, \qquad (1 + \sqrt q)^2 = 3.041^2 = 9.249, \qquad 1.10 \times 9.249 = 10.17 .
$$

The rank of a demeaned $60 \times 250$ panel is at most $T - 1 = 59$, so $250 - 59 = 191$ eigenvalues are zero by arithmetic, and the 59 nonzero ones carry the whole trace of 250. To see what the 8.7 is worth I simulated 200 pure-noise panels of this exact shape. The top noise eigenvalue averaged 8.9 (maximum 9.7), and 80% of the panels produced a top eigenvalue above 8.7. So the 8.7 is what the biggest eigenvalue of nothing looks like; it may be a real sector factor, and this panel cannot say. Keep it as a candidate and ask whether its eigenvector is stable across windows and concentrated in an economically sensible group. The edge is a floor for skepticism, not a theorem: fat tails and stale marks push the noise edge up, never down, so they can only weaken the case for the 8.7.

**The trap:** Three of them. The first is flipping the ratio, $q = T/N = 0.24$, which gives an edge of 2.22 and "three factors, one per coffee". The second is the Kaiser rule, "keep eigenvalues above 1": in these pure-noise panels all 59 nonzero eigenvalues are above 1. The third is reading the 191 zeros as a software bug. They are the 191 directions in which the sample has no variance, and an optimizer will treat each as a free lunch.

**If you got this wrong, read:** §7-B.5, "PCA on a residual panel, and which components are real" (and its Math, Gently box on why noise has an edge) and the desk framing "more parameters than data"; §8.8, "What's Left Is IDO (and How to Prove It)".

**Z.7-B.5: A tolerance with a pedigree**

**Answer:** You need $n \ge 113{,}400$ paths (113,344 before rounding up). ROBO's 200,000 monthly-grid paths without the bridge average about 17.6%, not 23.0%, so the test misses by about 5.4 points. That is roughly 64 standard errors (the standard error at 200,000 paths is 0.085 points) and about eleven times the 0.5-point tolerance. (A probability for a driftless log asset 0.30 above its barrier, $\sigma_V = 0.25$, one year; with zero drift the choice of measure does not enter, and the bridge result holds for any constant drift anyway.)

**How:** The tolerance rule is $n \ge (z\,\sigma_g/\varepsilon)^2$ with the book's $z = 4$. For a probability, $\sigma_g = \sqrt{p(1-p)}$, so

$$
n \ge \Big(\frac{4\sqrt{0.23 \times 0.77}}{0.005}\Big)^2 = \Big(\frac{4 \times 0.4208}{0.005}\Big)^2 = 336.7^2 = 113{,}344 .
$$

For the second half, that formula presumes an unbiased estimator, and a monthly grid is not one: it sees 12 dates and misses every crossing in between. The exact 12-date probability, from integrating the Gaussian random-walk kernel on a fine grid, is 0.1758 against the continuous 0.2301, and a naive 200,000-path simulation gave $0.1748 \pm 0.0008$. The bias is $0.2301 - 0.1758 = 5.43$ points and the standard error is $\sqrt{0.176 \times 0.824/200{,}000} = 0.085$ points, so the test misses by about 64 standard errors; more paths only draw a tighter circle around the wrong number. The bridge removes the bias: the coin-flip version on 12 steps gave 0.2301, and 4 million survival-weight paths gave 0.2302, against an exact 0.2301. Those weights also have a smaller per-path standard deviation (0.400 against 0.421), so roughly 102,000 paths would meet the same tolerance.

NOTE (for the editor): The printed solution says the monthly grid "converges to about 17.1%", a 5.9-point bias, "about 70 standard errors", with a standard error of 0.084 points. The 17.1% is the Broadie–Glasserman–Kou shifted-barrier approximation of §7-B.8, $2\Phi(-1.37)$, which that section labels approximate. The actual 12-date discrete-monitoring probability is 17.58% (numerical integration of the kernel), and the listing's naive simulation lands there too. That agrees with the Figure 7-B.5 caption ("understates the exact 23.0% by 5.4 points at monthly dates") and with Listing 7-B.2's "the naive grid gives 0.176", and it disagrees with the solution's 5.9. At 17.6% the bias is 5.4 points, the standard error is 0.085 points and the miss is about 64 standard errors. Either quote 17.6% and 5.4 points, or say that 17.1% and 5.9 points are the approximation.

**The trap:** Two of them. The first is $z = 1.96$, which gives 27,200 paths and a 5% false-alarm rate per assertion, instead of the book's 4 standard errors. The second, and the expensive one, is to see that 200,000 exceeds 113,000 and conclude that the test passes. The path count sets the noise, not the bias; a tolerance can only vouch for a simulation that is unbiased, and "widen the tolerance until green" would here need 5.5 points.

**If you got this wrong, read:** §7-B.8, "Where every tolerance in this book comes from", "Discretisation, and the bias that first passage adds" and "The Brownian-bridge correction"; §6.5.4, "Monte Carlo and the Brownian bridge".

**Z.7-B.6: The base-rate oracle**

**Answer:** The Brier score is $0.0196 = 0 - 0 + 0.0196$: reliability 0, resolution 0, uncertainty $0.02 \times 0.98 = 0.0196$. The AUC is 0.5. The model is perfectly calibrated and has no skill at all: its Brier skill score against the base rate is exactly zero. (Realized default frequencies in a cohort, so physical measure; probabilities, no units.)

**How:** Every issuer receives the same forecast, so there is a single probability bucket with $\bar p = 0.02$ and $\bar y = 0.02$. Reliability is $(\bar p - \bar y)^2 = 0$. Resolution, $(\bar y_k - \bar y)^2$ for the one bucket, is 0. What is left is uncertainty, $\bar y(1 - \bar y) = 0.0196$, and since the forecast is constant there is no within-bucket term. A direct check agrees:

$$
\text{BS} = 0.02\,(1 - 0.02)^2 + 0.98\,(0.02)^2 = 0.019208 + 0.000392 = 0.0196 .
$$

Every score is tied, so every default/non-default pair counts as one half and the AUC is 0.5. This is exactly the model an intercept-only logit builds, because the first-order condition $\sum_i \hat p_i = \sum_i y_i$ forces the fitted probability to the sample default rate. It is the benchmark every real model must beat. For scale: a model that sorts issuers into honest 1% and 3% halves has Brier $0.0195$, an improvement of only $0.0001$, and that is a decent model at a 2% base rate. The yardstick is therefore the skill score $1 - \text{BS}/0.0196$, never the raw Brier.

**The trap:** Reading 0.0196 as an excellent score because it is tiny next to the 0.25 of a coin flip. At a 2% base rate the uncertainty term alone is 0.0196, so almost any forecaster has a small Brier score. The related error is to take "reliability = 0" as evidence of a good model; calibration without resolution is the weatherman who reads out London's average rainfall.

**If you got this wrong, read:** §7-B.3, "Calibration: is 4% really 4%?" (the weatherman Math, Gently box and the Murphy decomposition) and "Maximum likelihood, and the one free lunch"; §11.5, "Validation: Power Curves", for the AUC.

<!-- STATUS: COMPLETE -->
