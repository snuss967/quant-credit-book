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

The triangular (Bartlett) weights are not decoration. Summing autocovariances with equal weights up to lag $L$ (the Hansen–Hodrick choice) is exactly right for an MA($h-1$) but can produce a negative variance in a finite sample. The Bartlett-weighted sum equals the variance of averages over windows of length $L+1$, and a variance of anything cannot be negative.

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

