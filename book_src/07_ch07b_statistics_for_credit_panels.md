# Chapter 7-B: The Statistician's Toolbox for Credit Panels: Regression, Logistic Models, Survival Analysis, Shrinkage, PCA, Bootstrap and Monte Carlo


## 7-B.0 Cold Open: A t-Statistic of Six

Theo had never been this proud of a regression. He had turned the 13-week cash flow model, the one on the USB stick, into a number: weeks until projected liquidity breaches the minimum-liquidity covenant, capped at 13. He had handed ROBO the high-yield panel and one sentence: *regress next-month IDO return on runway and compute the standard errors.* ROBO had done exactly that. Coefficient positive. 38,412 bond-months. t-statistic 6.1.

"Six," Theo said. "In banking, six sigma was something a consultant sold us. Here it's a p-value with eight zeros in it."

Kaz looked at the screen the way a cardiologist looks at a smartwatch reading. "Which standard errors?"

"The ones ROBO gave me."

ROBO had computed the textbook ones, which assume that every row is an independent draw from the universe, to fourteen decimal places. They were accurate in the fourteenth decimal and wrong in the first.

"How many issuers?" Kaz asked.

"Two hundred and six."

"Is runway a bond number or a company number?"

"Company. Liquidity doesn't care which CUSIP you hold."

"So every bond of one issuer carries the same runway in the same month, and the same runway next month, and their returns move together. Halvorsen alone is eleven lines in this panel."

Ines put her coffee down on the one part of the desk that was not a keyboard. "So you showed me one hand eleven times and asked me to count it as eleven hands. Then you showed me the same hand again every month for three years. What's the pot, Theo, and how many times have you really seen this card?"

Kaz reran it with standard errors clustered by issuer. The t-statistic fell to 2.4. Clustered by issuer and by month, it fell to 2.1. Theo stared at it for a while.

"It's still above two," he said.

"It is," Kaz said. "Barely, and now honestly. That's a better number than six."

From two desks over Mags said, without turning around: "Back in my day we didn't have standard errors. We had the PM's standard error, which was zero, and the PM's error, which was standard."

So here is the question this chapter answers: **how do you estimate anything from a credit panel whose rows are not independent, whose clocks are censored, whose covariance matrix has more entries than you have months, and whose tails are the whole point, and how do you attach an error bar you would defend to Ines?**

By the end of this chapter you will be able to: (i) derive OLS and its sandwich variance, and choose between heteroskedasticity-robust, issuer-clustered, two-way clustered and Fama–MacBeth standard errors for a bond panel; (ii) correct for overlapping returns with Newey–West and say how many lags you need and why the textbook choice under-corrects; (iii) fit a logistic model by maximum likelihood, read it as Bayes' rule in log-odds, and calibrate it; (iv) do survival analysis in the right order: censoring, the survival, distribution and hazard functions, Kaplan–Meier with Greenwood bands, Nelson–Aalen, and the Cox proportional-hazards model; (v) estimate a covariance matrix you can invert: EWMA, Ledoit–Wolf shrinkage, a factor model, and PCA on a residual panel, with a test for which principal components are noise; (vi) bootstrap dependent data with block and stationary bootstraps; (vii) say what a tree ensemble adds to a logit and what it costs; and (viii) run Monte Carlo as a method: standard errors, the sample size behind every tolerance in this book's tests, variance reduction, discretisation bias, and the Brownian-bridge correction for first passage.

This chapter closes Part II because everything after it leans on it. Chapters 8–12, 14 and 15 regress, classify, survive, shrink, resample or simulate, and each of them now imports one module, `creditstats.py` (§7-B.10), instead of rebuilding a sandwich estimator in its own appendix.

**One measure convention for the whole chapter.** Everything estimated from data here is a physical-measure ($\mathbb{P}$) object: realized returns, realized defaults, realized covariances. Risk-neutral quantities appear only as regressors or features. The one exception is Monte Carlo (§7-B.8), which runs under whichever measure the payoff demands and says which in its first line (Law 4).

**Notation, and five collisions resolved.** A regression is written $y = Xb + u$, with coefficients $b$ and error $u$, because $\beta_{i,k}$ is reserved for factor loadings and $\epsilon_{i,t}$ for idiosyncratic returns. When the regression *is* a factor regression, $b$ is $\beta$ and we say so. The logistic function is written $\operatorname{expit}(z) = 1/(1+e^{-z})$, because $\sigma$ is volatility and $\Lambda$ is order-arrival intensity. The cumulative default probability is $\text{PD}(t) = 1 - S(t)$, which statisticians call $F(t)$ and we cannot, because $F$ is face value. The cumulative hazard is $H(t)$, again because $\Lambda$ is taken. The EWMA decay is $\varphi$ (RiskMetrics' famous 0.94 is $\varphi = 0.94$ here; §10.2 writes it $\delta$ and §12.5 writes it $\lambda$, a collision Appendix A §A.3 records), the shrinkage intensity is $\delta^{\text{LW}}$ (plain $\delta$ is a quote distance), and eigenvalues are $\omega_k$. "Bootstrap" in this chapter means resampling data, never stripping a hazard curve from CDS quotes (§6.8).

> **Prerequisites.** The effective-sample-size problem and the forty-seven-hat rule (§7.1, §7.6); the survival function $S(t) = \exp(-\int_0^t \lambda_s\,ds)$ as a $\mathbb{Q}$ object (§6.6); purged, issuer-grouped cross-validation (§7.7). DTS appears below only as a scaling; §8.4 builds it. Everything else is built here from the definition up.


## 7-B.1 Regression on a Panel: OLS, the Sandwich, and Why Your Rows Are Not Independent

### Desk framing: every regression is a claim about a conditional mean

Every regression in this book says one thing: when $x$ is higher by one unit, the average of $y$ is higher by $b$. Empirical duration (§8.2) says a bond's return moves $b$ per basis point of Treasury yield. A trend regression (§10.4) says next quarter's return moves $b$ per unit of signal. Theo's regression says next month's IDO return moves $b$ per week of runway. The coefficient is usually the easy part. The hard part, and the part that decides whether a desk allocates risk, is the error bar, and the error bar depends entirely on what you assume about how the rows are related.

### The estimator, from the first-order condition

Stack $n$ observations: $y \in \mathbb{R}^n$, a regressor matrix $X \in \mathbb{R}^{n \times K}$ of full column rank (a column of ones included), and the model

$$
y = Xb + u, \qquad \mathbb{E}[u \mid X] = 0 .
$$

OLS picks $\hat b$ to minimize the sum of squared residuals $\lVert y - Xb \rVert^2$. Setting the gradient to zero gives the normal equations:

$$
X^\top\big(y - X\hat b\big) = 0 \quad\Longrightarrow\quad \hat b = (X^\top X)^{-1} X^\top y .
$$

The normal equations are a geometric statement: the residual vector is orthogonal to every column of $X$, so $X\hat b$ is the projection of $y$ onto the space the regressors span. Substitute $y = Xb + u$:

$$
\hat b - b = (X^\top X)^{-1} X^\top u .
$$

Two facts follow. First, $\mathbb{E}[\hat b \mid X] = b$: OLS is unbiased whenever the error has conditional mean zero, whatever its variance and correlation. Second, the variance of the estimator is

$$
\operatorname{Var}(\hat b \mid X) = (X^\top X)^{-1}\, X^\top \Omega X\, (X^\top X)^{-1}, \qquad \Omega = \mathbb{E}[u u^\top \mid X] .
\tag{7B.1}
$$

This is the **sandwich**. The two outer factors are the bread; $X^\top \Omega X$ is the meat. Every standard error in finance is a choice of meat.

The classical formula sets $\Omega = \sigma^2 I$, so the sandwich collapses to $\sigma^2 (X^\top X)^{-1}$. That is the formula ROBO used, and it assumes the residuals are homoskedastic and uncorrelated. In a bond panel neither holds: a CCC bond's residual has ten times the variance of a BBB's, and eleven Halvorsen bonds in the same month share most of theirs. The classical formula is a sandwich made with a photograph of the meat.

### Heteroskedasticity-robust: White's meat

If the residuals are uncorrelated but have different variances, $\Omega$ is diagonal and we estimate each diagonal entry by the squared residual:

$$
\widehat{X^\top \Omega X} = \sum_{i=1}^n \hat u_i^2\, x_i x_i^\top .
$$

No single $\hat u_i^2$ is a good estimate of $\mathbb{E}[u_i^2]$, but the *sum* is a consistent estimate of the meat, because it averages over $n$ rows. That is the whole trick behind every robust standard error: you never estimate $\Omega$, only the $K \times K$ matrix $X^\top \Omega X$.

### Issuer clustering: the meat that knows about siblings

Now let residuals correlate arbitrarily *within* an issuer and not at all *across* issuers. Index issuers by $g = 1, \ldots, G$ and let $X_g$, $\hat u_g$ be issuer $g$'s rows, all its bonds in all months. Then $\Omega$ is block-diagonal and the meat is

$$
\widehat{X^\top \Omega X} = c \sum_{g=1}^G X_g^\top \hat u_g \hat u_g^\top X_g, \qquad c = \frac{G}{G-1}\cdot\frac{n-1}{n-K} .
\tag{7B.2}
$$

The block for issuer $g$ allows every pattern of correlation inside it: sibling bonds in the same month, the same bond across months, sibling bonds across months. The factor $c$ is a small-sample correction. The asymptotics run in $G$, not $n$: the clustered estimator is reliable with roughly fifty or more clusters, and a panel of 38,412 bond-months from 206 issuers has 206 observations as far as this formula is concerned. With fewer than about fifty clusters, use the wild cluster bootstrap (§7-B.6).

How much does clustering matter? Take the simplest case that still teaches: one regressor, $G$ issuers each contributing $m$ rows, regressor intra-issuer correlation $\rho_x$, residual intra-issuer correlation $\rho_u$, everything demeaned. The variance of the score $\sum_i x_i u_i$ is the sum of the $n$ diagonal terms, $n\sigma_x^2\sigma_u^2$, plus the $n(m-1)$ same-issuer cross terms, each $\rho_x\sigma_x^2\cdot\rho_u\sigma_u^2$. Divide by what the classical formula assumes:

$$
\frac{\operatorname{Var}_{\text{true}}(\hat b)}{\operatorname{Var}_{\text{classical}}(\hat b)} \approx 1 + (m-1)\,\rho_x\,\rho_u .
\tag{7B.3}
$$

This is the **Moulton factor**. Read it twice. For an issuer-level signal such as runway, a rating, equity momentum or the PRS, every bond of the issuer carries the same value, so $\rho_x = 1$ and the factor is $1 + (m-1)\rho_u$. That is the denominator of effective breadth, $N/(1 + (m-1)\rho)$, from Law 2. The Moulton factor and effective breadth are the same formula wearing different ties: one says your standard error is too small, the other says your bets are too few, and both say forty-seven CUSIPs of one issuer are one hat.

For Halvorsen's eleven bonds with sibling residual correlation 0.6, the factor is $1 + 10 \times 0.6 = 7$. A panel made entirely of Halvorsens would need its classical standard errors multiplied by $\sqrt{7} \approx 2.65$ *(illustrative)*. A bond-level signal with low sibling correlation, such as a bond's own bid–ask bounce, has $\rho_x$ near zero, and clustering barely moves it. This is why clustering hurts issuer-level signals most, and why Theo's runway lost most of its t-statistic.

### Two-way clustering: issuers and months

Issuer clustering ignores one correlation that every credit panel has: in a given month, all bonds share the market's shock, whatever the regressors failed to absorb. Clustering by month captures that; clustering by issuer captures persistence within a name. When both are present, use both (Cameron, Gelbach and Miller 2011; Thompson 2011):

$$
\hat V_{\text{2-way}} = \hat V_{\text{issuer}} + \hat V_{\text{month}} - \hat V_{\text{issuer}\times\text{month}} ,
$$

where the last term clusters on the intersection (a bond-issuer-month cell) and removes the double count. The difference of positive semidefinite matrices need not be positive semidefinite, so `creditstats.py` clips negative eigenvalues to zero and logs that it did. Petersen's (2009) rule of thumb survives intact: a firm effect calls for firm clustering, a time effect calls for time clustering or Fama–MacBeth, and a credit panel has both.

### Fixed effects and Fama–MacBeth: two ways to ask a cross-sectional question

An **issuer fixed effect** adds one intercept per issuer. Algebraically it is the within transformation, $\ddot y_{i,t} = y_{i,t} - \bar y_i$ and likewise for $X$: the coefficient is identified only from changes *within* an issuer over time, and everything constant about the company (its sponsor, its industry, its lawyers) is absorbed. It is the econometrician's version of controlling for the company being the company. A **month fixed effect** demeans each month's cross-section, which removes the market return; a month fixed effect is the econometrician's index hedge. With month effects, $b$ measures cross-sectional predictability, which is what a long–short book earns. Fixed effects change the question; they do not fix the standard errors. Cluster anyway.

**Fama–MacBeth** (1973) runs one cross-sectional regression per month, collects the slopes $\hat b_t$, and reports their time-series mean with standard error $\operatorname{sd}(\hat b_t)/\sqrt{T}$. The slope is a portfolio return: $\hat b_t = w_t^\top y_t$ with $w_t^\top$ the relevant row of $(X_t^\top X_t)^{-1}X_t^\top$, a zero-cost portfolio with unit exposure to the characteristic and zero exposure to the other regressors. A Fama–MacBeth slope is a long–short portfolio return in a lab coat. That makes its standard error automatically robust to any cross-sectional correlation within a month, and not at all robust to persistence in $\hat b_t$ across months, which is why §7-B.2 applies Newey–West to the slope series.

### Errors in variables: stale marks bend the line

Suppose the regressor is measured with noise, $\tilde x = x + \eta$, with $\eta$ independent of everything. Then

$$
\operatorname{plim}\hat b = b\,\frac{\sigma_x^2}{\sigma_x^2 + \sigma_\eta^2} ,
$$

so the slope is biased toward zero. This is attenuation, and it is why betas estimated on stale marks are too small: the mark is the truth plus a lag, the lag behaves like noise in a same-day regression, and the Dimson correction of §8.5 recovers the slope by summing lagged coefficients (Law 9).

The more dangerous case is *correlated* errors in variables. If the same price error enters both the signal and the next return, the bias is no longer toward zero; it manufactures a premium. A bond whose month-end price is recorded too low looks cheap on any price-based value signal, and its next-month return is spuriously high because the error reverses. Dickerson, Robotti and Rossetti (2026) give the cleanest example: two bonds with true price 100 and true return zero, recorded with errors of $+0.50\%$ and $-0.50\%$, produce a measured long–short return of 1.00% from nothing. The fix is to break the link between the price in the signal and the price in the return, with a gap of at least a day, which §7.2 and Chapter 9-B treat in full.

> **Ways This Blows Up.** (1) *Clustering on the CUSIP.* It looks rigorous and captures none of the sibling correlation; cluster on the ultimate parent, the same key §7.7 groups folds by. (2) *Clustering on ticker.* Two issuers under one sponsor can share a credit agreement's trapdoors; for LMT-sensitive signals, cluster on the sponsor family. (3) *Few clusters.* A regression across eleven sectors clustered by sector has eleven observations of the meat; use a wild cluster bootstrap and say so. (4) *A fixed effect that eats the signal.* Issuer fixed effects on a rating regression identify the coefficient only from rating changes, which are rare and lagged; the standard error explodes, correctly.

*Used in:* §8.2 (empirical duration), §8.5 (Dimson betas), §8.6 (minimum-variance hedges), §9.3.4 and §9.7 (factor residuals and combinations), §10.4 and §10.5.3 (trend–carry and lead–lag regressions), §11.2.2 (asymmetric-beta regression), §11.4.2 (issuer-clustered hazard logit), §17.2 (pooled desmoothing regressions), §28.2 (effective breadth); Chapter 9-B (correlated errors in variables).


## 7-B.2 Overlapping Returns, Autocorrelation and Newey–West

### Desk framing: the 12-month return you counted twelve times

Chapter 10's trend signal predicts a 12-month return, and the natural way to test it is to sample that 12-month return every month. Consecutive observations then share eleven of their twelve months. You have not collected 240 observations in twenty years; you have collected about twenty, each photographed twelve times from slightly different angles.

### How much overlap inflates a t-statistic

Let one-period returns $r_t$ be i.i.d. with variance $\sigma^2$, and define the $h$-period overlapping return $R_t = \sum_{j=0}^{h-1} r_{t-j}$. Two such returns $k < h$ periods apart share $h - k$ terms, so

$$
\operatorname{Cov}(R_t, R_{t-k}) = (h-k)\,\sigma^2, \qquad \operatorname{Corr}(R_t, R_{t-k}) = 1 - \frac{k}{h} .
$$

The variance of the sample mean of $T$ such observations is, for $T \gg h$,

$$
\operatorname{Var}\big(\bar R\big) \approx \frac{h\sigma^2}{T}\Big[1 + 2\sum_{k=1}^{h-1}\Big(1 - \frac{k}{h}\Big)\Big] = \frac{h\sigma^2}{T}\cdot h ,
$$

because the bracket sums to $1 + 2(h-1) - (h-1) = h$. The naive formula reports $h\sigma^2/T$. It is too small by a factor of $h$, so the naive t-statistic is too large by $\sqrt h$. For a 12-month return sampled monthly that is $\sqrt{12} \approx 3.5$: a naive t-statistic of 7 is an honest 2. The same arithmetic applies to any overlapping label, which is why §7.4's triple-barrier labels need §7.6's uniqueness weights.

### The Newey–West estimator

Regression residuals with serial correlation need a meat that includes cross-products at nonzero lags. Write the score $g_t = x_t u_t$ and its sample autocovariances $\hat\Gamma_j = \frac{1}{T}\sum_{t=j+1}^{T} \hat g_t \hat g_{t-j}^\top$. Newey and West (1987) estimate the long-run variance as

$$
\hat S^{\text{NW}} = \hat\Gamma_0 + \sum_{j=1}^{L}\Big(1 - \frac{j}{L+1}\Big)\big(\hat\Gamma_j + \hat\Gamma_j^\top\big),
\qquad
\widehat{\operatorname{Var}}(\hat b) = (X^\top X)^{-1}\big(T\,\hat S^{\text{NW}}\big)(X^\top X)^{-1} .
\tag{7B.4}
$$

The triangular (Bartlett) weights are not decoration. Summing autocovariances with equal weights up to lag $L$ (the Hansen–Hodrick choice) is exactly right for an MA($h-1$) but can produce a negative variance in a finite sample. Up to end effects, the Bartlett-weighted sum is the average outer product of score sums over windows of length $L+1$, divided by $L+1$: a scaled sample variance, and a variance of anything cannot be negative.

The price of that guarantee is under-correction. Suppose the truth is the overlap triangle above and you set $L = h - 1$, the textbook choice. The estimator recovers

$$
1 + 2\sum_{k=1}^{h-1}\Big(1 - \frac{k}{h}\Big)^2 \quad\text{instead of}\quad h .
$$

For $h = 12$ the sum is $\frac{1}{144}\sum_{j=1}^{11} j^2 = \frac{506}{144} \approx 3.51$, so Newey–West reports a multiplier of about 8.0 where the truth is 12: two-thirds of the variance, and a t-statistic still about 22% too large. With $L = 2h - 1 = 23$ the same calculation gives about 10.0, or 83%. The desk rule follows: for overlapping returns set $L$ to at least $1.5h$–$2h$, and report beside the Newey–West result the $h$ non-overlapping subsamples (start in January, start in February, and so on), whose dispersion is a useful honesty check on its own. For autocorrelation that is not mechanical (stale marks in daily illiquid-bond returns) the plug-in rule $L = \lfloor 4(T/100)^{2/9} \rfloor$ is a reasonable floor; take the larger of the two.

There is a limit no estimator removes. A 20-year backtest of an annual signal has about twenty independent observations, a sample size that would embarrass a focus group. Newey–West t-statistics over-reject when $h/T$ is large, and the cure is not a better kernel but a longer history, more independent instruments, or humility.

> **Trend Watch.** *The second error bar (2009–2026).* **(1) The baseline.** Petersen (2009, *Estimating Standard Errors in Finance Panel Data Sets*, Review of Financial Studies 22(1)) showed that a large share of published finance panel studies reported standard errors that ignored firm or time correlation, and that the bias could be large; issuer clustering became the default in bond-panel work over the following decade. **(2) Non-standard errors.** In June 2024 Menkveld and coauthors published *Nonstandard Errors* (Journal of Finance 79(3), 2339–2390): 164 research teams tested the same hypotheses on the same data, the dispersion of their estimates was sizable, and the teams underestimated it. **(3) Bonds.** In April 2026 Dickerson, Robotti and Rossetti applied the idea to 108 corporate-bond factors (*The Corporate Bond Factor Replication Crisis*, arXiv:2604.07880). Across 648 defensible data-filtering paths per factor, the average non-standard error of a factor premium was 0.35% per month against an average premium of 0.33%, a ratio to the ordinary standard error of 1.15; across 168 methodological constructions the ratio averaged 1.45. Of 432 factor–specification combinations, only 26 bond-CAPM alphas survived a Benjamini–Hochberg false-discovery control, and correlated measurement error inflated price-based premia by 15–90 bp per month. **What it means for the desk:** report two error bars. One is the sampling error this section computes. The other is the specification error: the spread of your estimate across the defensible choices you did not make. When the second exceeds the first, the clustered t-statistic is not the most important number on the page. The full audit is §7.2 and Chapter 9-B.

"So the error bar has an error bar," Kaz said.

"Everything does," Ines said. "The trick is knowing which one is bigger before you push the chips in."

*Used in:* §7.4 and §7.6 (overlapping labels and uniqueness), §7.8 (Sharpe-ratio inference), §10.2.3 and §10.4 (trend tests on overlapping returns), §10.6.1 (the straddle regression with Newey–West errors), §10.5.3 (lead–lag at the right horizon), §28.3 (signal half-lives); Chapter 9-B (non-standard errors in the factor zoo).


## 7-B.3 Logistic Regression and Calibration: One Object for Every Probability on the Desk

### Desk framing: a probability is a promise with a number on it

The book estimates a binary probability in at least seven places before this chapter or without it: the chance an RFQ sender is informed (§1.3.3, §3.2.2), the chance a quote fills (§2.5.1), a default within twelve months (§11.4), an LMT within a year (the PRS, §13.8), an RFQ win (§18.7), and the chance a line was included in a portfolio trade because the client knew something (§19.8). They are one object. Build it once.

### The model is Bayes' rule written in log-odds

Let $Y \in \{0, 1\}$ (default or not, informed or not) and let $x$ be what you observe. Bayes' rule, in odds form, says

$$
\ln\frac{\mathbb{P}(Y=1 \mid x)}{\mathbb{P}(Y=0 \mid x)} = \underbrace{\ln\frac{\pi}{1-\pi}}_{\text{prior log-odds}} + \underbrace{\ln\frac{f_1(x)}{f_0(x)}}_{\text{log-likelihood ratio}} ,
$$

where $\pi$ is the base rate and $f_1, f_0$ are the densities of $x$ among events and non-events. If those two densities are Gaussian with a common covariance (or, more generally, members of an exponential family that share a sufficient statistic), the log-likelihood ratio is linear in $x$. The posterior log-odds is then linear too:

$$
\operatorname{logit} p(x) = \ln\frac{p(x)}{1 - p(x)} = b_0 + b^\top x, \qquad p(x) = \operatorname{expit}(b_0 + b^\top x) = \frac{1}{1 + e^{-(b_0 + b^\top x)}} .
$$

Three readings fall out. The intercept carries the base rate, which is why changing the sample's default rate changes only the intercept (the shift in §11.4.2). Each slope is a log odds ratio: $e^{b_k}$ multiplies the odds per unit of $x_k$. And independent pieces of evidence *add* in log-odds, which is the whole content of the toxicity term in §1.3.3: every signal about the sender contributes its own log-likelihood ratio, and the logistic function turns the total back into a probability. A logit is a restructuring banker's evidence memo with the adjectives replaced by log-likelihood ratios.

### Maximum likelihood, and the one free lunch

With $p_i = \operatorname{expit}(x_i^\top b)$ (the intercept folded into $x$), the log-likelihood of independent Bernoulli outcomes is

$$
\ell(b) = \sum_{i=1}^n \big[\, y_i \ln p_i + (1 - y_i)\ln(1 - p_i) \,\big] .
$$

Because $\partial p_i / \partial z_i = p_i(1-p_i)$ for $z_i = x_i^\top b$, the gradient and Hessian are

$$
\nabla \ell(b) = \sum_i (y_i - p_i)\,x_i = X^\top (y - p), \qquad \nabla^2 \ell(b) = -X^\top W X, \quad W = \operatorname{diag}\big(p_i(1-p_i)\big) .
$$

The Hessian is negative definite, so $\ell$ is concave and has at most one maximum. Newton's method, $b \leftarrow b + (X^\top W X)^{-1} X^\top (y - p)$, is iteratively reweighted least squares and usually converges in five to eight steps. At the optimum the score equations read $X^\top(y - \hat p) = 0$; the first row, for the intercept, says $\sum_i \hat p_i = \sum_i y_i$. A fitted logit always reproduces the sample's event rate exactly. Calibration in the large, in sample, is free. It is the only free lunch in this chapter, and it is served only in sample.

The classical variance is the inverse information, $(X^\top \hat W X)^{-1}$. On an issuer-month panel it has the same disease as §7-B.1, and the same cure: keep $(X^\top \hat W X)^{-1}$ as bread and use the issuer-clustered meat $\sum_g X_g^\top \hat e_g \hat e_g^\top X_g$ with $\hat e = y - \hat p$. That is the modern form of Shumway's correction, which divided chi-squared statistics by the average number of firm-years per firm (§11.4.2).

> **Ways This Blows Up.** *Separation.* If some combination of features separates events from non-events perfectly (on a hundred LMTs, "loan below 80 and runway under nine months" nearly does, §13.8), the likelihood keeps rising as the coefficients run to infinity, and the optimizer reports whatever it had when it gave up. Fix with a ridge penalty, a weakly informative prior (the MAP logit of §13.8), or Firth's bias-reduced likelihood, and report that you did. *Rare events.* With a 2% base rate, the intercept is estimated from a few dozen events; the slopes are fine and the level is fragile, so recalibrate on the deployment base rate. *Clipping.* Probabilities of exactly 0 or 1 make the log-loss infinite; clip to $[10^{-6}, 1 - 10^{-6}]$ and log it.

### Calibration: is 4% really 4%?

A model can rank perfectly and be wrong in every level, or be perfectly calibrated and rank nothing (predict the base rate for everyone). Ranking is **power**, measured by the AUC and the CAP curve (§11.5). Levels are **calibration**, and the desk needs both: power picks which bonds to avoid, calibration sets how much spread is fair compensation.

Measure calibration with a **proper scoring rule**, one whose expected value is optimized by reporting the true probability. The log loss is proper: if $Y \sim \text{Bernoulli}(p)$ and you report $q$, the expected loss $-p\ln q - (1-p)\ln(1-q)$ has derivative $-p/q + (1-p)/(1-q)$, which is zero only at $q = p$. A proper scoring rule is the one poker table where bluffing loses by construction. The **Brier score** $\text{BS} = \frac{1}{n}\sum_i (p_i - y_i)^2$ is also proper, and on $K$ probability buckets it decomposes (Murphy 1973) as

$$
\text{BS} = \underbrace{\sum_k \frac{n_k}{n}\big(\bar p_k - \bar y_k\big)^2}_{\text{reliability (want small)}} \;-\; \underbrace{\sum_k \frac{n_k}{n}\big(\bar y_k - \bar y\big)^2}_{\text{resolution (want large)}} \;+\; \underbrace{\bar y(1 - \bar y)}_{\text{uncertainty}} ,
$$

up to a within-bucket term. Reliability is calibration, resolution is power, and uncertainty is the base rate's fault. A reliability diagram plots $\bar y_k$ against $\bar p_k$; a calibrated model sits on the diagonal.

When a model ranks well but is mis-leveled, repair it on a holdout without touching the ranking. **Platt scaling** fits a two-parameter logit, $\operatorname{logit} p^{\text{cal}} = a + c\,\operatorname{logit}\hat p$, which fixes a shifted base rate ($a$) and over- or under-confidence ($c$). **Isotonic regression** fits the best monotone step function by pooling adjacent violators and needs more data. Tree ensembles and naive-Bayes scores are typically overconfident at the extremes and should always be recalibrated before their outputs are called probabilities (Niculescu-Mizil and Caruana 2005; §7-B.7).

**A worked check.** A model assigns 4% twelve-month PDs to 150 B3 issuers; nine default, 6%. Is the model wrong? Under independence the standard error of the default rate is $\sqrt{0.04 \times 0.96/150} \approx 1.6\%$, so the miss is 1.25 standard errors: no evidence. And independence flatters the test. Defaults are correlated, the true standard error is larger, and §7-B.6 shows that with realistic correlation even a tenfold miss can be noise. A single cohort is close to a single observation.

**One collision, named.** The "logistic adoption curve" of §2.3.1 is a different object with the same shape: a deterministic function of time fitted by nonlinear least squares to market shares. It has no Bernoulli likelihood and no calibration; it shares only the S. Appendix A §A.3 records the collision.

*Used in:* §1.3.3 (toxicity in log-odds), §2.5.1 (fill probabilities), §3.2.2 ($\pi(x)$ from markouts), §11.4.2 and §11.5 (PD logit, power curves), §13.8 (the PRS as a MAP logit), §18.7 (RFQ win curves), §19.8 (basket adverse selection); §7-B.4 (the logit as a discrete-time hazard) and §7-B.7 (recalibrating boosted trees).


## 7-B.4 Survival Analysis in the Right Order: Censoring, $S$, PD and $\lambda$, Kaplan–Meier, Cox

### Desk framing: the clock that stops before the story ends

A bond leaves your sample for many reasons: it defaults, it matures, it is called, it is tendered, it is exchanged, its issuer is acquired, or your data ends. Only the first is the event you are studying, and the others are not neutral. Survival analysis is the discipline of using the issuers whose story you did not see finish without pretending you know how it ended. Censoring is the signal (Law 14), and the RSSG reader has been doing this informally for years: the 13-week model was a hazard curve all along (§5.1.5).

### Censoring and truncation, defined

For issuer $i$, let $\tau_i$ be the event time and $C_i$ the time it leaves observation for any other reason. We observe

$$
\tilde t_i = \min(\tau_i, C_i), \qquad e_i = \mathbf{1}\{\tau_i \le C_i\} ,
$$

the observed time and the event indicator ($e_i$, because $\delta$ is a quote distance). Every estimator below assumes **non-informative censoring**: conditional on the covariates, $C_i$ is independent of $\tau_i$. In credit this assumption fails in a predictable direction. Issuers call bonds when they can refinance cheaply, which means when their credit is good, so calls remove healthy names from the risk set and leave it enriched in weak ones. A Kaplan–Meier curve on bonds subject to calls therefore *overstates* default relative to a world without calls. Mergers can go either way (§15.5). Distressed exchanges must never be treated as censoring: they are default (§11.4.3).

**Left truncation** is the mirror problem. An issuer that enters the high-yield universe as a fallen angel at age seven was not at risk *in your sample* for its first seven years. Count it in risk sets only from its entry date. Counting it from issuance credits the panel with seven years of survival it could not have failed, which is immortal-time bias, the survivorship bias of survival analysis.

### Three functions that are one object

For a continuous event time $\tau$ define the survival function, the cumulative default probability, the density and the hazard:

$$
S(t) = \mathbb{P}(\tau > t), \qquad \text{PD}(t) = 1 - S(t), \qquad f(t) = -S'(t),
$$

$$
\lambda(t) = \lim_{\Delta t \downarrow 0} \frac{\mathbb{P}(t < \tau \le t + \Delta t \mid \tau > t)}{\Delta t} = \frac{f(t)}{S(t)} = -\frac{d}{dt}\ln S(t) .
$$

Integrate the last identity and you get $S(t) = \exp(-H(t))$ with cumulative hazard $H(t) = \int_0^t \lambda(s)\,ds$. This is the formula of §6.6, now as a $\mathbb{P}$ object estimated from realized defaults rather than a $\mathbb{Q}$ object implied by prices. The two hazards differ by the credit risk premium, and comparing them across that line without saying so is how Law 4 gets broken. On a monthly grid the hazard is a conditional probability, $h_m = \mathbb{P}(\tau \in (m-1, m] \mid \tau > m-1)$, and survival is a product: $S(m) = \prod_{j \le m}(1 - h_j)$.

### Kaplan–Meier, derived

Order the distinct event times $t_{(1)} < t_{(2)} < \cdots$. At each, let $n_j$ be the number at risk (observed and event-free just before $t_{(j)}$) and $d_j$ the number of events. Among those at risk, the events are binomial, and the maximum-likelihood estimate of the discrete hazard is $\hat h_j = d_j / n_j$. A censored issuer contributes to every risk set up to its censoring time and then leaves; it is never counted as a survivor beyond what was seen, and never as a default. Chaining the conditional survival probabilities gives the **Kaplan–Meier** (product-limit) estimator:

$$
\hat S(t) = \prod_{j:\, t_{(j)} \le t}\Big(1 - \frac{d_j}{n_j}\Big) .
\tag{7B.5}
$$

Its variance comes from the delta method. Each $\ln(1 - \hat h_j)$ has variance approximately $\hat h_j / \big(n_j(1 - \hat h_j)\big) = d_j / \big(n_j(n_j - d_j)\big)$, and the terms are asymptotically uncorrelated across event times, so

$$
\widehat{\operatorname{Var}}\big(\hat S(t)\big) \approx \hat S(t)^2 \sum_{j:\, t_{(j)} \le t} \frac{d_j}{n_j(n_j - d_j)} ,
\tag{7B.6}
$$

**Greenwood's formula**. Build the confidence band on $\ln(-\ln \hat S)$ and transform back, so that it stays inside $[0, 1]$. The **Nelson–Aalen** estimator sums the hazards instead of multiplying the survivals, $\hat H(t) = \sum_{t_{(j)} \le t} d_j / n_j$, and $\exp(-\hat H)$ sits slightly above $\hat S$, with the two nearly equal when $d_j/n_j$ is small.

**Worked example: the practice cohort.** Run the desk's six fictional issuers through a hypothetical 36-month window *(illustrative; these are not their canonical histories, except that Quillfeather's exchange matches Chapter 14)*. Calloway Industrial's notes are taken out by a make-whole call at month 9 (censored). Quillfeather Packaging completes a distressed exchange at month 14 (event). Larkspur Foam exchanges at month 22 (event). Halvorsen defaults at month 27 (event). Halyard Holdings is acquired at month 30 (censored). Brambleworth is still alive when the window closes at month 36 (censored).

| Month | Issuer | Event? | At risk $n_j$ | $d_j$ | $\hat S$ after |
| :--- | :--- | :---: | :---: | :---: | :---: |
| 9 | Calloway | censored (call) | 6 | 0 | 1.000 |
| 14 | Quillfeather | default (DE) | 5 | 1 | 0.800 |
| 22 | Larkspur Foam | default (DE) | 4 | 1 | 0.600 |
| 27 | Halvorsen | default | 3 | 1 | 0.400 |
| 30 | Halyard | censored (acquired) | 2 | 0 | 0.400 |
| 36 | Brambleworth | censored (end) | 1 | 0 | 0.400 |

So $\widehat{\text{PD}}(36) = 60\%$. Greenwood gives $\widehat{\operatorname{Var}} = 0.16 \times \big(\tfrac{1}{20} + \tfrac{1}{12} + \tfrac{1}{6}\big) = 0.16 \times 0.30 = 0.048$, a standard error of 22 points. Nelson–Aalen gives $\hat H = 0.2 + 0.25 + 0.333 = 0.783$ and $\exp(-0.783) = 0.457$. The two naive answers bracket the truth and are both wrong: counting censored issuers as survivors gives three defaults in six, 50%; dropping them gives three in four, 75%. Kaplan–Meier gives each censored issuer exactly the credit it earned.

"A make-whole call," Kaz said. "Is that when the company phones to apologize?"

"It's when the company pays you enough to stop complaining," Mags said. "Which, in my experience, is the same thing."

Kaz's question was better than it sounded, because the make-whole is the informative-censoring problem in miniature: Calloway left because its credit was good enough to refinance, so the five issuers left behind are worse than the six who started.

**Where this goes next.** If the event has types (hard default versus distressed exchange), Kaplan–Meier on one type with the others censored estimates the wrong thing: $1 - \hat S_{\text{DE}}$ overstates the probability of a DE, because it treats issuers who hard-defaulted as if they could still have exchanged later. Competing risks extend this section, and §14.2 builds the cause-specific hazards and the Aalen–Johansen cumulative incidence that fix it (Law 13). §15.5 applies the same machinery to regulatory clocks, and §14.3 adds a cured fraction for re-default after an exchange.

### Cox proportional hazards: covariates without a baseline

Kaplan–Meier describes a cohort. To ask *which* issuers fail faster, Cox (1972) models the hazard of issuer $i$ as

$$
\lambda_i(t) = \lambda_0(t)\, \exp\!\big(b^\top z_i(t)\big),
$$

with $\lambda_0$ an arbitrary baseline and $z_i(t)$ covariates, possibly time-varying. Covariates scale the hazard proportionally, so $e^{b_k}$ is a hazard ratio. The magic is in how $b$ is estimated without ever specifying $\lambda_0$. At event time $t_{(j)}$, condition on the fact that exactly one issuer in the risk set $R_j$ failed. The probability that it was issuer $i$ is

$$
\frac{\lambda_0(t_{(j)})\, e^{b^\top z_i}}{\sum_{k \in R_j} \lambda_0(t_{(j)})\, e^{b^\top z_k}} = \frac{e^{b^\top z_i}}{\sum_{k \in R_j} e^{b^\top z_k}} ,
$$

and the baseline cancels. Cox's trick is a relative-value trade: the baseline is the market beta of time, common to everyone at risk, and it drops out of the ratio. Multiplying over event times gives the **partial likelihood**, with log

$$
\ell_p(b) = \sum_{j} \Big[\, b^\top z_{(j)} - \ln \sum_{k \in R_j} e^{b^\top z_k} \,\Big],
\qquad
\nabla \ell_p(b) = \sum_j \big[\, z_{(j)} - \bar z_j(b) \,\big],
\tag{7B.7}
$$

where $\bar z_j(b)$ is the risk-weighted average covariate of the risk set. The score has a desk reading: the fit is right when, on average, the issuer that defaulted looked no worse than the risk-weighted issuer standing next to it. $\ell_p$ is concave, Newton's method converges quickly, and tied event times are handled by Breslow's approximation (all $d_j$ events share the same denominator). Once $\hat b$ is in hand, Breslow's estimator recovers the baseline, $\hat H_0(t) = \sum_{t_{(j)} \le t} d_j / \sum_{k \in R_j} e^{\hat b^\top z_k}$, and $\hat S(t \mid z) = \exp\big(-\hat H_0(t)\, e^{\hat b^\top z}\big)$.

**Cox and the logit are the same model on a grid.** Put the panel in counting-process form: one row per issuer-month, with covariates fixed within the month. If the continuous-time Cox model holds, the monthly hazard is

$$
h_{i,m} = 1 - \exp\!\big(-e^{\alpha_m + b^\top z_{i,m}}\big), \qquad \alpha_m = \ln\!\int_{m-1}^{m}\lambda_0(s)\,ds ,
$$

which is a complementary log-log link: $\ln\!\big(-\ln(1 - h_{i,m})\big) = \alpha_m + b^\top z_{i,m}$. When $h$ is small, $-\ln(1-h) \approx h \approx h/(1-h)$, so the cloglog and the logit coincide. Shumway's firm-month logit (§11.4.2) is a discrete-time Cox model with a smooth baseline, and the same $b$ appears in both. One object, two chapters.

**The USB stick, again.** Theo's runway becomes a Cox covariate: $z_i(t) = \mathbf{1}\{\text{runway}_i(t) < 13 \text{ weeks}\}$. A fitted $b = 1.1$ *(illustrative)* means a hazard ratio of $e^{1.1} \approx 3.0$: an issuer inside a quarter of its liquidity floor defaults three times as fast as one outside it, whatever the baseline year looks like. Thirteen weeks of cash flows, reborn as a hazard ratio.

**Check the proportionality.** Plot $\ln(-\ln \hat S)$ by covariate group against $\ln t$; proportional hazards means parallel curves. In credit, proportionality fails across regimes: a covariate that predicted bankruptcy before 2020 predicts distressed exchanges after it, with a different ratio (§14.1). Stratify the baseline by regime, or interact covariates with an era dummy, rather than averaging two worlds into one hazard ratio.

*Used in:* §5.1.5 (the 13-week model as a hazard), §6.6 and §6.8 (the $\mathbb{Q}$ survival curve these estimates are compared against), §11.4.2 (the discrete-time hazard logit), §13.8 ($\lambda^{\text{LMT}}$), §14.2 (competing risks extend this section), §14.3 (re-default and the cured fraction), §15.5 (regulatory clocks), §17.1 (private-credit default clocks).


## 7-B.5 Covariance You Can Invert: EWMA, Shrinkage, Factor Models and PCA on a Residual Panel

### Desk framing: more parameters than data

A covariance matrix for 400 bonds has $400 \times 401/2 = 80{,}200$ distinct entries. Ten years of monthly returns supply $120 \times 400 = 48{,}000$ numbers. You are estimating more parameters than you have observations, which in banking is called a projection and in statistics is called a mistake. Worse, the sample covariance $\hat\Sigma$ has rank at most $T - 1 = 119$, so it is singular, and an optimizer that inverts it will find portfolios with an estimated variance of zero and pile into them. Every tool in this section is a way of adding structure the data cannot supply.

### EWMA: memory with a half-life

The exponentially weighted estimator updates as

$$
\hat\Sigma_t = \varphi\,\hat\Sigma_{t-1} + (1 - \varphi)\, x_t x_t^\top, \qquad 0 < \varphi < 1 ,
$$

placing weight $(1-\varphi)\varphi^j$ on the observation $j$ periods back. The half-life is $\ln 2 / \ln(1/\varphi)$, and the effective sample size of a weighted average, $(\sum w_j)^2 / \sum w_j^2$, works out to $(1 + \varphi)/(1 - \varphi)$. At RiskMetrics' daily $\varphi = 0.94$ the half-life is 11.2 days and the effective sample is about 32 days. EWMA tracks volatility regimes (§10.3) and makes the dimensionality problem *worse*, because it shrinks the effective $T$. The standard compromise is a fast EWMA for variances and a slow, structured estimator for correlations.

### Shrinkage, the general idea

Shrinkage trades a little bias for a lot of variance. For means it is old: estimate a counterparty's markout with $n_i$ fills as a weighted average of its own mean and the population's, with weight $w_i = \tau^2/(\tau^2 + \sigma^2/n_i)$ on its own data (the normal–normal posterior; §3.3.4 uses exactly this). James and Stein (1961) proved the uncomfortable general version: for three or more means, shrinking all of them toward a common point beats estimating each separately, in total squared error, *whatever the true means are*. Factor weights "shrunk toward equal" (§9.7) are the same move applied to a portfolio.

### Ledoit–Wolf, derived in five lines

Shrink the sample matrix toward a structured target $\Sigma^{\text{tgt}}$: $\Sigma(\delta) = \delta\,\Sigma^{\text{tgt}} + (1-\delta)\,\hat\Sigma$. Choose $\delta$ to minimize the expected squared Frobenius error $\mathbb{E}\lVert \Sigma(\delta) - \Sigma \rVert_F^2$. Write $\Sigma(\delta) - \Sigma = (\hat\Sigma - \Sigma) - \delta(\hat\Sigma - \Sigma^{\text{tgt}})$; the loss is quadratic in $\delta$ and its minimizer is

$$
\delta^{*} = \frac{\mathbb{E}\big\langle \hat\Sigma - \Sigma,\; \hat\Sigma - \Sigma^{\text{tgt}} \big\rangle}{\mathbb{E}\lVert \hat\Sigma - \Sigma^{\text{tgt}} \rVert_F^2} .
$$

If the target is fixed and $\hat\Sigma$ is unbiased, the cross terms vanish and

$$
\delta^{\text{LW}} = \frac{\sum_{i,j}\operatorname{Var}(\hat\Sigma_{ij})}{\sum_{i,j}\operatorname{Var}(\hat\Sigma_{ij}) + \lVert \Sigma - \Sigma^{\text{tgt}} \rVert_F^2} = \frac{\text{noise}}{\text{noise} + \text{misspecification}} ,
\tag{7B.8}
$$

clipped to $[0, 1]$. Shrink hard when the sample is noisy; shrink little when the target is wrong. The noise is estimable from the data, $\widehat{\operatorname{Var}}(\hat\Sigma_{ij}) = T^{-2}\sum_t (x_{it}x_{jt} - \hat\Sigma_{ij})^2$, and the misspecification is $\lVert \hat\Sigma - \Sigma^{\text{tgt}} \rVert_F^2$ minus the noise. Ledoit and Wolf give the targets (scaled identity, 2004; constant correlation, 2004; single index, 2003) and the extra term needed when the target is itself estimated; §12.5 and §19.5 run the one-factor version.

### Factor covariance: structure you can believe

A factor model imposes the structure directly:

$$
\Sigma = B\,\Sigma_F\,B^\top + D ,
$$

with $B$ the $N \times K$ loadings, $\Sigma_F$ the factor covariance and $D$ a diagonal of idiosyncratic variances. For $N = 400$ and $K = 5$ that is $2{,}000 + 15 + 400 = 2{,}415$ parameters instead of 80,200. The matrix is positive definite whenever $D > 0$, and Woodbury's identity inverts it in $O(NK^2)$:

$$
\Sigma^{-1} = D^{-1} - D^{-1}B\big(\Sigma_F^{-1} + B^\top D^{-1} B\big)^{-1} B^\top D^{-1} .
$$

Credit has a gift here: the loading on the market spread factor is known before you estimate anything. It is DTS (§8.4), so dividing each bond's excess return by its DTS puts every bond on one scale, and the factor model in DTS units has loadings you did not have to estimate (Law 3).

### PCA on a residual panel, and which components are real

After stripping the known factors you are left with a $T \times N$ panel $\tilde\epsilon$ of DTS-scaled residuals (§8.8). Its first principal component is the unit vector that captures the most variance:

$$
\max_{v}\; v^\top \hat\Sigma_{\tilde\epsilon}\, v \quad \text{s.t.} \quad v^\top v = 1
\quad\Longrightarrow\quad
\hat\Sigma_{\tilde\epsilon}\, v = \omega\, v ,
$$

from the Lagrangian $v^\top\hat\Sigma v - \omega(v^\top v - 1)$. The variance captured is the eigenvalue $\omega_1$; the $k$-th component is the $k$-th eigenvector, orthogonal to the rest. The component's time series is $g_t = \tilde\epsilon_t v_1$, and removing it leaves $\tilde\epsilon - g\,v_1^\top$.

The question PCA does not answer by itself is whether $\omega_1$ is signal. Random matrix theory supplies the null. If the panel were pure noise with unit variance and aspect ratio $q = N/T$, the nonzero eigenvalues of its sample correlation matrix would fill, as $N, T \to \infty$, the Marchenko–Pastur interval

$$
\big[(1 - \sqrt q)^2,\; (1 + \sqrt q)^2\big] .
$$

For 400 bonds and 120 months, $q = 3.33$ and the upper edge is $(1 + 1.826)^2 \approx 8.0$: pure noise produces eigenvalues eight times the average. On five years of daily data, $q = 400/1{,}260 \approx 0.32$ and the edge falls to about 2.4. A principal component is noise until proven larger than Marchenko–Pastur. Clipping the eigenvalues below the edge to their average (Laloux et al. 1999) is one more shrinkage estimator.

"So we just assume Gaussian," Kaz said, and then, a beat later, regretted it. The Marchenko–Pastur edge assumes thin-tailed, serially independent noise; fat tails and stale marks widen the noise band. Treat the edge as a floor for skepticism, not a theorem about your data. Two more traps: the sign of an eigenvector is arbitrary, so align each window's loadings with the previous window's before you chart them; and when two eigenvalues are close, their eigenvectors rotate freely between windows, so the "second factor" may be a different factor every month.

*Used in:* §3.3.4 (shrunk counterparty scores), §8.4 (DTS scaling), §8.6 (ridge hedges), §8.8 (removing the common residual factor), §9.7 (weights shrunk toward equal), §10.3 (EWMA volatility), §12.5 (EWMA, shrinkage and desmoothing), §19.5 (residual covariance for 150 stale bonds), §28.2 (breadth from the residual correlation).


## 7-B.6 The Statistical Bootstrap: Block, Stationary and Cluster

### The plug-in principle

You want the sampling distribution of a statistic $\hat\theta$ (a Sharpe ratio, an AUC, a default rate) and you have one sample. Efron's (1979) idea is to treat the empirical distribution as if it were the population: draw $n$ observations with replacement, recompute $\hat\theta^{*}$, repeat $B$ times, and use the spread of $\hat\theta^{*} - \hat\theta$ as a stand-in for the spread of $\hat\theta - \theta$. Percentile intervals are the simplest. Studentized (bootstrap-$t$) intervals, which resample a pivot $(\hat\theta^{*} - \hat\theta)/\widehat{\text{se}}^{*}$, are more accurate, and the extra computation is cheap next to a wrong answer.

### Why the i.i.d. bootstrap lies on credit data

Resampling single observations destroys dependence, and credit data are made of dependence. For an AR(1) series with autocorrelation $\rho$, the variance of the sample mean is approximately $\frac{\sigma^2}{T}\cdot\frac{1+\rho}{1-\rho}$; the i.i.d. bootstrap reports $\sigma^2/T$. Stale marks with $\rho = 0.3$ hide a factor of 1.86 in variance. Across issuers it is worse, because correlated defaults make one cohort close to one observation.

> **[SOURCE EXTRACTION]** *Bohn_Stein_Active_Credit_Portfolio_Management p.443:* "Thus, about half of the time, even with infinite data, we would mistake the default probability for 20 bps when it was actually 200 bps."
>
> **Annotation.** Bohn and Stein's setting is a portfolio with uniform asset correlation 0.25 and a true PD of 2%. Because defaults share a factor, the realized default rate of even an infinitely large portfolio is one draw from the distribution of the systematic factor, and that draw is often benign. Their next page describes the Hanson–Schuermann bootstrap, which resamples *firms*, and warns that multiyear bounds are hard "due to the dependence induced in the sample from year 1 to year 2" (p.444). The 2026 desk takes both warnings literally. Resample *years* (whole cross-sections), in blocks long enough to keep a cycle's persistence, never firms one at a time. And accept the limit no resampling scheme removes: twenty years of data hold two or three credit cycles, and the bootstrap never shows you a crisis you did not have. It only reshuffles the ones you did.

### Block and stationary bootstraps

The **moving block bootstrap** (Künsch 1989) resamples blocks of $\ell$ consecutive observations and concatenates them, so dependence within a block survives. The circular version wraps the series end to start so every observation is equally likely to be drawn. The **stationary bootstrap** (Politis and Romano 1994) draws block lengths from a geometric distribution with mean $1/p$: at each step, with probability $p$ start a new block at a random date, otherwise take the next date (circularly). The resampled series is itself stationary, which fixed-length blocks are not. Block length should grow like $T^{1/3}$; the Politis–White (2004) rule picks it automatically, and for overlapping returns it must be at least the overlap $h$.

### Panels: resample the unit that is independent

- **Dates, with the cross-section intact.** To keep both serial and cross-sectional dependence, resample blocks of months and carry every bond in each month along. Resample months, not bonds.
- **Issuers, with their history intact.** For issuer-level dependence, the cluster (pairs) bootstrap resamples issuers with replacement, each with all its bonds and months. This is the bootstrap analogue of (7B.2).
- **Few clusters.** With a dozen sectors, use the wild cluster bootstrap: keep $X$ fixed, multiply each cluster's residual vector by an independent random sign, rebuild $y^{*} = X\hat b_0 + u^{*}$ under the null, and refit (Cameron, Gelbach and Miller 2008).
- **Sharpe ratios.** To compare two strategies' Sharpe ratios, use a studentized circular block bootstrap of the difference (Ledoit and Wolf 2008), then deflate for the number of trials (§7.8, Law 12).

*Used in:* §7.6 (the sequential bootstrap for bagging over overlapping labels), §7.8 (Sharpe-ratio inference), §11.5 (confidence bands on AUC and hit rates), §14.2 (cohort uncertainty in cumulative incidence), §28.2 and §28.6 (breadth and drawdown confidence); collision with curve bootstrapping (§6.8) recorded in Appendix A §A.3.


## 7-B.7 Tree Ensembles in One Section

**A tree** partitions feature space by recursive binary splits. At each node it picks the feature $j$ and threshold $c$ that most reduce impurity (squared error for a return, Gini $\sum_k p_k(1 - p_k)$ or entropy for a default flag) and predicts the leaf average. Trees find thresholds and interactions a logit cannot ("distance to default below 1.5 *and* runway under 13 weeks"), and they are invariant to monotone transformations of features, so a leverage ratio needs no winsorizing. A single deep tree is also a high-variance estimator that memorizes its training set.

**Bagging** averages $B$ trees grown on bootstrap samples. If each tree's prediction has variance $\sigma^2$ and any two have correlation $\rho$, the average has variance

$$
\operatorname{Var}\Big(\frac{1}{B}\sum_{b=1}^{B} f_b\Big) = \frac{1}{B^2}\big[B\sigma^2 + B(B-1)\rho\sigma^2\big] = \rho\,\sigma^2 + \frac{1 - \rho}{B}\,\sigma^2 ,
$$

which falls to $\rho\sigma^2$, not zero, as $B \to \infty$. This is Law 2 again, inside the model: forty-seven correlated trees are about one tree. Random forests (Breiman 2001) lower $\rho$ by letting each split consider only a random subset of features.

**Boosting** (Friedman 2001) builds the model in stages, $F_m(x) = F_{m-1}(x) + \nu\, h_m(x)$, where each small tree $h_m$ is fitted to the negative gradient of the loss at $F_{m-1}$ and $\nu \in [0.01, 0.1]$ is a learning rate. With log loss and $F$ in log-odds, the negative gradient is $y_i - p_i$, exactly the score contribution of §7-B.3. Boosting on log loss is a logistic regression that grows its own features. XGBoost (Chen and Guestrin 2016) adds second-order steps and regularization.

**What credit adds to the recipe.** (1) Cross-validate with purged, embargoed, parent-grouped folds (§7.7): trees can identify an issuer from a coupon-and-maturity pair and will happily learn the issuer instead of the economics. (2) Impose monotone constraints where the economics is not in doubt: PD non-decreasing in leverage, non-increasing in distance to default and in runway. (3) Recalibrate the output (§7-B.3); boosted log-odds are overconfident in the tails. (4) Remember that trees do not extrapolate. A tree has never heard of anything worse than the worst thing it has seen, so an issuer at 12× leverage scores like the most-levered leaf in training. (5) Rank features by permutation importance computed on held-out purged folds, not by in-sample impurity, which favors continuous, high-cardinality features. Measured honestly, the gain is real where the signal is nonlinear: on walk-forward bankruptcy prediction, trees lift AUC well above a linear logit using distance to default alone (§11.4.4). Where events are few, as with roughly a hundred LMTs, a logit with a prior still wins (§13.8).

*Used in:* §7.0 and §7.5 (the secondary model in meta-labeling), §7.6 (the sequential bootstrap), §7.7 (grouped CV), §11.4.4 (the bankruptcy horse race), §14.1 (PD models trained on the wrong labels), §26.7 (an agent's trials are your trials).


## 7-B.8 Monte Carlo as a Method: Standard Errors, Variance Reduction and the Brownian Bridge

### The estimator and its error

To compute $\theta = \mathbb{E}[g(X)]$, under a stated measure, draw $X_1, \ldots, X_n$ and average: $\hat\theta_n = \frac{1}{n}\sum_i g(X_i)$. The central limit theorem gives $\sqrt n(\hat\theta_n - \theta) \to \mathcal{N}(0, \sigma_g^2)$, so the standard error is $\hat s_g/\sqrt n$ in any dimension. That is Monte Carlo's virtue and its tax: halving the error costs four times the paths.

### Where every tolerance in this book comes from

Every reference implementation in this book asserts that a simulated number matches a closed form within a tolerance. The tolerance is not a matter of taste. For an assertion $|\hat\theta_n - \theta| < \text{tol}$ to fail by chance with probability $\alpha$, set $\text{tol} = z_{\alpha/2}\,\hat s_g/\sqrt n$; to reach a target error $\varepsilon$, you need

$$
n \ge \Big(\frac{z_{\alpha/2}\,\sigma_g}{\varepsilon}\Big)^2 .
$$

The book's convention is four standard errors, a two-sided false-alarm rate of $6.3 \times 10^{-5}$ per assertion, with a fixed seed so that the test is deterministic. A tolerance tuned until the test passes is a p-hack with a seed.

Tails are expensive. For a probability $p$, $\sigma_g = \sqrt{p(1-p)}$ and the *relative* standard error is $\sqrt{(1-p)/(np)}$. A 0.1% tail event estimated from 100,000 paths carries a 10% relative error. Quantiles are worse: the standard error of the sample $\alpha$-quantile is $\sqrt{\alpha(1-\alpha)/n}\,/\,f(q_\alpha)$, and the density $f$ in the far tail is tiny.

> **[SOURCE EXTRACTION]** *Bolder_Credit_Risk_Modelling p.508:* "The standard error for this brute-force estimator is extremely small for lower levels of confidence, but increases significantly as we reach the extreme part of the tail of the default-loss distribution."
>
> **Annotation.** Bolder's report card for the one-factor Gaussian threshold model compares raw simulation at 10 million and 100,000 iterations with importance sampling at 3,000, and finds that the variance-reduced estimator's error grows much more slowly as the quantile moves into the tail. The desk lesson is a reporting rule: every simulated VaR, CVaR or tail probability ships with its Monte Carlo standard error, computed at the quantile that is reported, and a 99.9% number without one is unlabeled (Law 11). Where the modern desk departs from the book is scale: a portfolio of correlated credits with jump-to-default is now routinely simulated on a GPU, which shrinks the cost of brute force but not the $1/\sqrt n$ law. A GPU buys you paths; it does not repeal the square root.

### Seeds, streams and common random numbers

Seed one `numpy.random.Generator` per experiment and derive independent streams from it with `SeedSequence.spawn`, never by adding 1 to a seed. When you compare two strategies, two parameter values, or a bumped and an unbumped price, use **common random numbers**: the same draws for both. Since $\operatorname{Var}(\hat\theta_A - \hat\theta_B) = \operatorname{Var}\hat\theta_A + \operatorname{Var}\hat\theta_B - 2\operatorname{Cov}(\hat\theta_A, \hat\theta_B)$, positively correlated estimates make the difference far more precise than either level. A finite-difference Greek without common random numbers is mostly noise.

### Variance reduction: three tools that earn their keep

- **Antithetic variates.** Pair each normal draw $Z$ with $-Z$. The pair average has variance $\frac{\sigma_g^2}{2}(1 + \rho)$ with $\rho = \operatorname{Corr}(g(Z), g(-Z))$, which is negative for any monotone $g$, so monotone payoffs (most bond and loss payoffs) get cheaper.
- **Control variates.** If $Y$ has known mean $\mu_Y$, use $\hat\theta_c = \hat\theta - c(\bar Y - \mu_Y)$. The optimal $c^{*} = \operatorname{Cov}(g, Y)/\operatorname{Var}(Y)$ cuts the variance by the factor $1 - \rho_{gY}^2$. Price a Black–Cox bond with the Merton bond as control, or a portfolio loss with its analytic expected loss.
- **Importance sampling.** Draw from $q$ instead of $p$ and reweight by the likelihood ratio: $\hat\theta = \frac{1}{n}\sum_i g(X_i)\,p(X_i)/q(X_i)$. In a one-factor threshold model, shift the systematic factor to $Z \sim \mathcal{N}(\mu, 1)$ with $\mu < 0$ so bad states are sampled often, and weight each path by $p(z)/q(z) = \exp(-\mu z + \mu^2/2)$. This is the technique behind Bolder's 3,000-path estimator above.

### Discretisation, and the bias that first passage adds

Simulate log-normal quantities exactly in logs, so that the grid introduces no error at the grid points. Between the grid points is another matter. A path-dependent payoff that depends on whether a barrier was ever touched (Black–Cox default, a covenant trip, a drawdown stop) misses every crossing that happens between grid points and comes back, and this bias shrinks only like $\sqrt{\Delta t}$. Broadie, Glasserman and Kou (1997) show that a discretely monitored barrier behaves like a continuous one shifted away by a factor $e^{0.5826\,\sigma\sqrt{\Delta t}}$. For a driftless log asset 0.30 above its barrier with $\sigma_V = 0.25$, the one-year continuous hitting probability is $2\Phi(-1.2) \approx 23.0\%$; monitoring monthly behaves like a barrier at distance $0.30 + 0.5826 \times 0.25 \times \sqrt{1/12} \approx 0.342$, or $2\Phi(-1.37) \approx 17.1\%$ *(approx., via the continuity correction)*. The monthly grid misses about a quarter of the defaults.

### The Brownian-bridge correction, derived

The exact fix needs one fact about Brownian motion. For a standard Brownian motion $W$ started at 0 and a level $a > 0$, the reflection principle says that a path that touches $a$ and ends at $y \le a$ is matched one-for-one by its reflection after the touch, which ends at $2a - y$. Hence the joint density of "touched $a$" and "$W_t \in dy$" is $\phi_t(2a - y)$, where $\phi_t$ is the $\mathcal{N}(0, t)$ density, and dividing by the density of $W_t$ at $y$ gives

$$
\mathbb{P}\Big(\max_{s \le t} W_s \ge a \;\Big|\; W_t = y\Big) = \frac{\phi_t(2a - y)}{\phi_t(y)} = \exp\!\Big(-\frac{(2a-y)^2 - y^2}{2t}\Big) = \exp\!\Big(-\frac{2a(a - y)}{t}\Big).
$$

Now take the log asset $X$ over one step of length $\Delta t$ with volatility $\sigma_V$, starting at $x_i$ and ending at $x_{i+1}$, both above a log barrier $b$. Reflect so that "down to $b$" becomes "up to $a$": the distance to the barrier is $a = x_i - b$, the displacement toward it is $y = x_i - x_{i+1}$, so $a - y = x_{i+1} - b$, and the variance is $\sigma_V^2\Delta t$. Then

$$
p_i = \mathbb{P}\Big(\min_{[t_i, t_{i+1}]} X \le b \;\Big|\; x_i, x_{i+1}\Big) = \exp\!\Big(-\frac{2\,(x_i - b)\,(x_{i+1} - b)}{\sigma_V^2\,\Delta t}\Big) ,
\tag{7B.9}
$$

the formula §6.5.4 uses. It holds for any constant drift, because the Girsanov density that adds a drift depends on the path only through its endpoint, so conditioning on the endpoint cancels it. The corrected algorithm simulates exact log endpoints on a coarse grid, records a hit if an endpoint is at or below $b$, and otherwise records a hit with probability $p_i$ (Beaglehole, Dybvig and Zhou 1997; Glasserman 2004). Better still, do not flip the coin: carry the path's survival probability $\prod_i (1 - p_i)$ as its weight. The mean is the same and the variance is lower, because you integrated the coin out analytically.

*Used in:* §1.5 (the one-factor threshold simulation), §2.3.2 (best-of-$n$ RFQ simulation), §5.9 (the mixture lab), §6.5.4 and §6.11 (Black–Cox with the bridge), §14.7 (the regime-switching engine), §15.2 (the change-of-control put), §16.3 and §16.5 (backstop and claims checks), §23.2 (the CreditGrades check), §28.4 and §28.6 (Kelly with JTD, drawdown barriers); every seeded `assert` in the book.


## 7-B.9 Case Study: Theo's Runway, Re-Audited

A week after the cold open, Theo ran the runway signal through every tool in this chapter. All numbers are *illustrative*; the sequence is the lesson.

| Treatment | Unit of independence | t-statistic |
| :--- | :--- | :---: |
| Classical OLS (what ROBO did) | bond-month | 6.1 |
| White (HC1) | bond-month, unequal variances | 5.6 |
| Clustered by ultimate parent | issuer (206) | 2.4 |
| Two-way: parent and month | issuer and month | 2.1 |
| Fama–MacBeth, Newey–West on slopes ($L = 4$) | month (36) | 2.2 |
| Wild cluster bootstrap, p-value | issuer | 0.04 |

Then the second error bar. Across 24 defensible specifications (runway capped at 13 or 26 weeks, a one- or two-month knowledge lag on lender reporting, IDO or plain excess returns, ex-ante trimming at three thresholds), the coefficient ranged from 0.4 to 1.9 bp per week of runway, against a clustered standard error of 0.5. The non-standard error was about the size of the standard error, which by the Trend Watch's measure is normal for credit and still uncomfortable. The Cox fit of §7-B.4 told the same story on a different clock, a hazard ratio near 3 for issuers inside thirteen weeks.

"So it's real," Theo said, "but it's one real thing, not six."

"It's a hand worth playing at a quarter of the size you wanted," Ines said. "Which is usually what a real edge looks like."

*Used in:* §11.4.2 (runway as a hazard covariate), §13.8 (runway inside the PRS), §28.9 (the dashboard's runway column).


## 7-B.10 The Credit Statistics Module: A Reference Implementation

### Specification for AI Implementation

**What ROBO built from the vague version.** Theo's first spec said: "Estimate default probabilities for the practice cohort. Use clean data." ROBO dropped every issuer without an observed outcome, as instructed, and reported a 75% three-year PD for six issuers that §7-B.4 shows have a 60% product-limit PD with a 22-point standard error. "Clean" had meant "censored," and nobody had said so. The precise spec below names the unit of independence, the censoring rule and the error bar for every estimator.

**The Spec You Hand the Robot.** Build `creditstats.py` (NumPy and SciPy only; no `statsmodels`, `lifelines` or `sklearn`, so every estimator is auditable against this chapter's equations). Every random function takes an explicit `numpy.random.Generator`; experiments spawn independent streams with `SeedSequence.spawn`.

**The functions.** `ols` and `vcov` (classical, hc1, cluster on the ultimate parent, two-way, Newey–West; equations 7B.1, 7B.2, 7B.4) with `nw_lags`; `logit_fit` (IRLS, optional ridge on slopes, issuer-clustered sandwich) and `platt_calibrate`; `kaplan_meier` (Greenwood, Nelson–Aalen, entry times for left truncation; 7B.5–7B.6) and `cox_ph` (Breslow ties and baseline; 7B.7); `ledoit_wolf` (7B.8), `mp_edge` and `residual_pca`; `stationary_bootstrap_indices` and `block_bootstrap` (stationary, moving-block, i.i.d.); `mc_estimate`, `control_variate`, `bridge_hit_prob` (7B.9), `first_passage_mc` and `first_passage_exact`. Shapes: `y (n,)`, `X (n, K)` with the constant in column 0, returns panels `(T, N)`; times in months or years as the caller states; $\sigma_V$ annualized decimal.

**Edge cases ROBO must handle, not guess.** Cluster on the ultimate parent, never the CUSIP; flag fewer than 50 clusters in `info`. Two-way covariances that are not positive semidefinite are eigenvalue-clipped and the clipping is logged. `nw` requires one time-ordered row per period. A logit that has not converged in 50 Newton steps raises an error that names separation, rather than returning the last iterate. Probabilities are clipped to $[10^{-6}, 1 - 10^{-6}]$ before any logarithm. Kaplan–Meier counts an issuer censored at an event time as at risk at that time, and an issuer with an entry time only after entry (left truncation). Distressed exchanges are events, never censoring, and the caller passes them as such. PCA loadings are sign-normalized so they sum to a positive number, and the count of "real" components uses the Marchenko–Pastur edge with a 10% margin for finite samples. Every Monte Carlo result returns its standard error and its 4-s.e. tolerance.

The first block is the module, saved as `creditstats.py`; the second is its acceptance test. Both are seeded; neither touches the network or the disk.

<!-- EXPLAIN: Listing 7-B.1 -->
> **Code Companion: Listing 7-B.1.** Bartlett-weighted sum of score cross-products (not divided by T); rows time-ordered. The full python listing is in [Appendix F, Listing 7-B.1](#code-7b-1).

<!-- EXPLAIN: Listing 7-B.2 -->
> **Code Companion: Listing 7-B.2.** Acceptance tests for creditstats.py (seeded; every tolerance is derived, not tuned). The full python listing is in [Appendix F, Listing 7-B.2](#code-7b-2).

*Used in:* imported by Chapters 8–12, 14 and 15 (`from creditstats import vcov, logit_fit, kaplan_meier, ledoit_wolf, first_passage_mc`); its asserts are the tolerance convention for every reference implementation in the book.


## 7-B.11 Desk Debrief

On Friday Theo taped one sheet beside the monitor where the t-statistic of six had lived. Ines read it, crossed out every "always," and handed it back.

- **The coefficient is cheap; the error bar is the claim.** OLS is unbiased under almost any dependence, and its standard error is whatever you assumed about $\Omega$. On a bond panel that means clustering on the ultimate parent, adding the month when the market shock sits in the residual, and bootstrapping when clusters are few. (Laws 2, 11)
- **The Moulton factor and effective breadth are one formula.** $1 + (m-1)\rho_x\rho_u$ charges issuer-level signals in full; extra CUSIPs add rows, not information. (Law 2)
- **Overlap divides your sample by $h$.** Newey–West at $L = h - 1$ still misses about a third of the variance; $1.5h$ to $2h$ lags, shown beside the $h$ non-overlapping subsamples, is the honest pair. (Law 12)
- **Every probability on the desk is one logit.** Evidence adds in log-odds, the intercept carries the base rate, and calibration is free in sample and earned on a holdout. (Laws 5, 11)
- **Censoring is the signal.** Kaplan–Meier gives each censored issuer the credit it earned: calls censor the healthy, distressed exchanges are events, late entrants join on entry, and event types go to §14.2. (Laws 7, 13, 14)
- **Every covariance you invert is a shrinkage estimator, chosen or not.** Ledoit–Wolf weighs noise against misspecification, DTS supplies the market loading, and a principal component is noise until it clears Marchenko–Pastur. (Laws 3, 9)
- **Resample the unit that is independent.** Months travel with their cross-section, issuers with their history, and no bootstrap shows you a crisis you did not have. (Laws 2, 14)
- **A simulated number ships with its standard error, and a barrier with its bridge.** More paths make a biased grid more precise, never more right. (Laws 4, 11)

Mags read it over his shoulder. "Back in my day the error bar was the PM's mood," she said. "At least that was clustered properly. One mood a week, and every trade that week shared it."

> **View From Another Seat.** *The CLO manager's other 4%.* §7-B.3 asks whether a 4% PD comes true 4% of the time. A CLO manager needs that answer and one more, because the vehicle's tests never read the desk's model. They read agency ratings, mapped through a fixed table into a weighted-average rating factor, and a CCC bucket whose excess is carried at a haircut in the overcollateralization test (§21.4). A loan fairly priced at a 4% PD can still cost the CLO money if a downgrade pushes it over the bucket limit. So that seat calibrates twice, to realized defaults for the credit view and to the agencies for the tests, and treats the gap between them as a risk of its own. The systematic fund on the other side of the resulting sale reads the same gap as a supply schedule it can forecast (Law 15).

**The Spec You Hand the Robot.** "Implement `creditstats.py` per §7-B.10, NumPy and SciPy only: `vcov` (classical, HC1, parent-clustered, two-way with logged eigenvalue clipping, Newey–West); an IRLS `logit_fit` that raises on separation, and `platt_calibrate`; `kaplan_meier` with Greenwood, Nelson–Aalen and entry times; Breslow `cox_ph`; `ledoit_wolf`, `mp_edge` and sign-normalized `residual_pca`; bootstraps over months or issuers, never bonds; Monte Carlo helpers that return a standard error and a 4-s.e. tolerance; `first_passage_mc` with bridge weights. Every random function takes a `Generator`. Tests: the Moulton ratio; Newey–West multipliers near 8 and 10 out of 12; the practice cohort's $\hat S = 0.400$ with variance 0.048; one planted factor above the Marchenko–Pastur edge and none in pure noise; bridged first passage within four standard errors of the exact value."

### Exercises

1. *(More CUSIPs.)* An issuer-level signal has a classical t-statistic of 4.0 on 300 issuers with five bonds each and sibling residual correlation 0.5. Theo adds every issuer's loans, doubling $m$ to 10 at the same correlation. Find the clustered t before and after, and the most any number of extra rows could deliver. *Solution.* Before, the factor is $1 + 4(0.5) = 3$ and $t \approx 2.31$. After, the classical t is $4\sqrt2 \approx 5.66$, the factor 5.5, the clustered t about 2.41. The true variance is proportional to $(1 + (m-1)\rho_u)/m$, which falls from 0.6 to a floor of 0.5, so the ceiling is $2.31\sqrt{0.6/0.5} \approx 2.53$. The sample is 300 issuers, whatever ROBO counts.
2. *(A rumor repeated six times.)* A six-month-return signal sampled monthly for fifteen years shows a naive t of 3.0. Treating it as the sample-mean case of §7-B.2, find the honest t and the Newey–West t at $L = 5$ and $L = 11$. *Solution.* Honest: $3/\sqrt6 \approx 1.22$. At $L = 5$ the multiplier is $1 + 2\sum_{k=1}^{5}(1 - k/6)^2 = 1 + 110/36 \approx 4.06$, so $t \approx 1.49$. At $L = 11$ the weights $1 - k/12$ meet autocorrelations $1 - k/6$, giving $1 + 2(145/72) \approx 5.03$ and $t \approx 1.34$.
3. *(The fallen angel's missing years.)* Add to the practice cohort a fallen angel that enters at month 18 and is alive at 36. Compute $\widehat{\text{PD}}(36)$ with left truncation, then counting it from month 0, and give the Greenwood standard error of the first. *Solution.* The risk sets at the three events are 5, 5 and 4, so $\hat S = 0.8 \times 0.8 \times 0.75 = 0.48$ and $\widehat{\text{PD}} = 52\%$. From month 0 they are 6, 5 and 4, so $\hat S = 0.50$: the entrant is credited with surviving month 14, when it could not have failed in the sample. Greenwood gives $0.48^2(\tfrac1{20} + \tfrac1{20} + \tfrac1{12}) \approx 0.042$, about 21 points. In a panel of thousands the standard error shrinks; the bias does not.
4. *(One factor per coffee.)* A residual panel of 250 bonds over 60 months has top correlation eigenvalues 14.1, 8.7 and 6.2, and Kaz announces three factors, one for each coffee he drank this morning. How many clear Marchenko–Pastur with a 10% margin, and how many eigenvalues are zero? *Solution.* $q \approx 4.17$, the edge is $(1 + 2.04)^2 \approx 9.25$, or 10.2 with the margin: one factor. The 8.7 may be real, but this panel cannot tell, so check its stability across windows. Rank is at most 59, so at least 191 eigenvalues are zero, and an optimizer handed the raw matrix will find 191 riskless portfolios that are not.
5. *(A tolerance with a pedigree.)* The one-year first-passage probability of §7-B.8 is 23.0%. How many paths give a 4-s.e. tolerance of 0.5 points? ROBO runs 200,000 on a monthly grid without the bridge; by how much does the test fail? *Solution.* $n \ge (4\sqrt{0.23 \times 0.77}/0.005)^2 \approx 113{,}000$. The grid converges to about 17.1%, with a standard error of about 0.084 points at 200,000 paths, so the 5.9-point bias is about 70 standard errors. More paths drew a tighter circle around the wrong number.
6. *(The base-rate oracle.)* Kaz's model gives every issuer 2% in a cohort that defaults at 2%. Decompose its Brier score. *Solution.* Reliability and resolution are both zero, so the score is the uncertainty, $0.02 \times 0.98 = 0.0196$, and the AUC is 0.5: perfectly calibrated, no ranking at all, like a forecaster who reads out London's average rainfall every morning. An intercept-only logit builds this model for free (§7-B.3), so that is what it is worth.

### Deep-Dive Resource Graph

- **Podcasts:** *Odd Lots*, "Why the True Price of a Bond Can Still Be Hard To Know" (5 Apr 2021), https://omny.fm/shows/odd-lots/why-the-true-price-of-a-bond-can-still-be-hard-to (pricing error, §7-B.1). *Flirting with Models*, "Ralph Smith – Scientific Investing in Fixed Income (S5E7)" (11 Jul 2022), https://www.flirtingwithmodels.com/episodes/kAEkSoYuRwd (which bonds a backtest may assume it held). *Cloud 9fin*, "LME Doomscrolling — Data-driven reality check" (7 Apr 2026), https://share.transistor.fm/s/1f62123b (life after coercive LMEs, §7-B.4).
- **Practitioner Writing:** Petersen, "Programming Advice - Finance Panel Data Sets," with a test data set for checking `vcov`, https://www.kellogg.northwestern.edu/faculty/petersen/htm/papers/se/se_programming.htm ; J.P. Morgan/Reuters, *RiskMetrics Technical Document* (1996).
- **Academic Papers:** Petersen (2009), RFS; Cameron, Gelbach and Miller (2011), *Robust Inference with Multiway Clustering*; Newey and West (1987), Econometrica; Shumway (2001), *Forecasting Bankruptcy More Accurately*; Kaplan and Meier (1958); Cox (1972); Ledoit and Wolf (2004), JMVA; Politis and Romano (1994), *The Stationary Bootstrap*; Beaglehole, Dybvig and Zhou (1997), *Going to Extremes*, FAJ.
- **Data & Code:** `creditstats.py` (§7-B.10, Appendix F); `arch` time-series bootstraps, https://arch.readthedocs.io/en/latest/bootstrap/timeseries-bootstraps.html ; Open Bond Asset Pricing, https://openbondassetpricing.com

*Used in:* every chapter that reports an error bar; the Debrief feeds App E (Laws 2–5, 7, 9, 11–15).

<!-- STATUS: COMPLETE -->

