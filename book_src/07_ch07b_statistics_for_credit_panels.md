# Chapter 7-B: The Statistician's Toolbox for Credit Panels: Regression, Logistic Models, Survival Analysis, Shrinkage, PCA, Bootstrap and Monte Carlo


## 7-B.0 Cold Open: A t-Statistic of Six

*Thursday 8 October 2026, 4:10 p.m., Theo Marsh's third week. The desk, its panel, Halvorsen and every number the desk produces are fictional; the two papers on Ines's desk are real.*

Theo had never been this proud of a regression. He had turned the 13-week cash flow model, the one on the USB stick, into a number: weeks until projected liquidity breaches the minimum-liquidity covenant, capped at 13. He had handed ROBO the high-yield panel and one sentence: *regress next-month IDO return on runway and compute the standard errors.* ROBO had done exactly that. Coefficient positive. 38,412 bond-months. t-statistic 6.1.

It had taken two evenings. The first went on teaching ROBO what a minimum-liquidity covenant was, which turned out to mean teaching it where in a credit agreement the definition of Liquidity lived and which of the four add-backs the lenders had actually agreed to. The second went on the panel itself: two hundred and six high-yield issuers, every bond each of them had outstanding, every month for three years, each row stamped with that issuer's runway at the start of the month and the bond's IDO return over the next. At PJT a model like this had been a spreadsheet with one company in it and a partner standing behind your chair. Here it was a panel with two hundred companies in it and nobody behind the chair at all, which was the part of the new job Theo had not yet decided how to feel about. He turned his screen toward the aisle.

Kaz rolled a chair over. Ines came the long way round from the coffee machine, a cup in one hand and two stapled printouts in the other, both striped with the green highlighter she used, as far as Theo could tell, only for things she meant to bring up later. He could read the top title upside down: *The Corporate Bond Factor Replication Crisis*, by Dickerson, Robotti and Rossetti, posted to arXiv on 9 April 2026. Theo had skimmed its abstract on his first weekend and put it in the folder of things he would understand in a month. The paper took the published corporate-bond return signals, sorted them into nine families, and rebuilt each of them hundreds of times, every rebuild a choice a careful researcher could defend: which month-end price to believe, which bonds to trim as bad prints, which part of the market to sort within. One of Ines's green stripes ran across a sentence about noise in month-end prices manufacturing premia out of nothing. Under it lay an older paper from the *Journal of Finance*, *Nonstandard Errors*, by Albert Menkveld and a very long list of coauthors, in which a large number of research teams had been handed one dataset and one set of hypotheses and had come back with answers spread far wider than any of them had predicted. In the margin of the top printout, in the handwriting that had once filled tournament scorecards, Ines had written: *Same data. Same question. Which team are you?*

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

What bothered him was not the size of the fall. It was that he should have seen it coming, and from his own side of the business. At PJT, eleven CUSIPs of one issuer had never been eleven of anything. They were one company, one waterfall, one set of advisers across the table and one plan of reorganization at the end, and an associate who modeled them as eleven separate recoveries would have been sent back to his desk with the spreadsheet and a look. Theo had known that for years. He had simply never been asked to know it about a t-statistic.

"It's still above two," he said.

"It is," Kaz said. "Barely, and now honestly. That's a better number than six."

From two desks over Mags said, without turning around: "Back in my day we didn't have standard errors. We had the PM's standard error, which was zero, and the PM's error, which was standard."

Ines picked her coffee back up and set the two printouts on Theo's keyboard, where he could not avoid them. "These are yours now. The top one rebuilds every bond factor anyone has published, hundreds of ways each, and asks how much of the premium survives the choices. The bottom one asks a room full of research teams the same question and counts how far apart their answers land. Your clustered two-point-one is one team's answer. Before you show it to anybody who allocates risk, I want to know two things: how many independent hands are underneath it, and how far it moves when somebody else makes the choices you made." She was already walking away. "At the next replay I'm dealing the spring of 2020. Bring a card."

Theo turned the top printout over. On the back, where he had expected nothing, Ines had drawn a column of tally marks, eleven of them, and then circled all eleven together and written *1* beside the circle. He looked at it for longer than he had looked at the t-statistic. Then he peeled a Post-it off the pad, wrote *How many hands?* on it, and stuck it to the bottom of his monitor, beside the USB stick, where it stayed for the rest of the month. Kaz, who had watched the whole exchange without comment, wheeled back to their own desk and opened a file called `cluster_everything.py`, which by Friday would have a different name.

So here is the question this chapter answers: **how do you estimate anything from a credit panel whose rows are not independent, whose clocks are censored, whose covariance matrix has more entries than you have months, and whose tails are the whole point, and how do you attach an error bar you would defend to Ines?**

The chapter follows what Theo did with that card over the rest of October, and each scene asks Ines's question of a different tool. A Friday replay of the spring of 2020, when six hundred bonds shared one spring and one fallen angel looked like thousands of data points, sets up regression, clustering and overlapping returns (§7-B.1–7-B.2); a Monday whiteboard of eight real liability-management deals, two of whose clocks had not stopped, sets up logistic models and survival analysis (§7-B.3–7-B.4); and the covariance matrix, the bootstrap, tree ensembles and Monte Carlo turn out to be the same count of evidence in four more costumes (§7-B.5–7-B.8), before Theo re-audits his own runway card row by row (§7-B.9). The Finder table at the top of the Desk Debrief (§7-B.11) maps each tool to its equation, its intuition box, the scene where it earned its place and its code listing.

This chapter closes Part II because everything after it leans on it. Chapters 8–12, 14 and 15 regress, classify, survive, shrink, resample or simulate, and each of them now imports one module, `creditstats.py` (§7-B.10), instead of rebuilding a sandwich estimator in its own appendix.

> **Prerequisites.** The effective-sample-size problem and the forty-seven-hat rule (§7.1, §7.6); the survival function $S(t) = \exp(-\int_0^t \lambda_s\,ds)$ as a $\mathbb{Q}$ object (§6.6); purged, issuer-grouped cross-validation (§7.7). DTS appears below only as a scaling; §8.4 builds it. Everything else is built here from the definition up.

#### Notation for this chapter

**One measure convention for the whole chapter.** Everything estimated from data here is a physical-measure ($\mathbb{P}$) object: realized returns, realized defaults, realized covariances. Risk-neutral quantities appear only as regressors or features. The one exception is Monte Carlo (§7-B.8), which runs under whichever measure the payoff demands and says which in its first line (Law 4).

**Notation, and five collisions resolved.** A regression is written $y = Xb + u$, with coefficients $b$ and error $u$, because $\beta_{i,k}$ is reserved for factor loadings and $\epsilon_{i,t}$ for idiosyncratic returns. When the regression *is* a factor regression, $b$ is $\beta$ and we say so. The logistic function is written $\operatorname{expit}(z) = 1/(1+e^{-z})$, because $\sigma$ is volatility and $\Lambda$ is order-arrival intensity. The cumulative default probability is $\text{PD}(t) = 1 - S(t)$, which statisticians call $F(t)$ and we cannot, because $F$ is face value. The cumulative hazard is $H(t)$, again because $\Lambda$ is taken. The EWMA decay is $\varphi$ (RiskMetrics' famous 0.94 is $\varphi = 0.94$ here; §10.2 writes it $\delta$ and §12.5 writes it $\lambda$, a collision Appendix A §A.3 records), the shrinkage intensity is $\delta^{\text{LW}}$ (plain $\delta$ is a quote distance), and eigenvalues are $\omega_k$. "Bootstrap" in this chapter means resampling data, never stripping a hazard curve from CDS quotes (§6.8).


## 7-B.1 Regression on a Panel: OLS, the Sandwich, and Why Your Rows Are Not Independent

### Desk framing: every regression is a claim about a conditional mean

A regression is a claim about a conditional mean: when $x$ is one unit higher, the average of $y$ is $b$ higher (the Friday replay at the end of this section collects the desk's examples, from empirical duration in §8.2 to the trend book in §10.4). Theo's cold open printed one slope and three t-statistics: 6.1, 2.4 and 2.1. Same coefficient, same 38,412 rows. Everything that changed between them was one assumption about which rows are related to which, and that assumption is worth having a picture of before it gets its algebra.

> **Math, Gently.** *The error bar, and the two ways a panel's rows are related.* **Part 1: the wobble.** A regression slope is the single straight line drawn through a cloud of points (Chapter 1's box in §1.4 builds it). Its **standard error** is how much that slope would wobble if you could re-deal the panel and draw the line again (Chapter 7's box in §7.1 does the $\sqrt n$ arithmetic for a plain average). The re-deal is the whole idea, and the only question is what you are allowed to re-deal. If every row were its own hand of cards you could re-deal rows. A bond panel is one hand photographed many times: the four bonds of one issuer are four pictures of one company's month, and re-dealing the pictures without re-dealing the company manufactures certainty. Tiny number: an issuer with four bonds whose residuals correlate 0.5 with one another, and a signal, like runway, that is the same for all four. Each extra sibling adds half a bond's worth of shared noise, so the printed variance is too small by a factor of $1 + (4-1)(0.5) = 2.5$, and the honest standard error is $\sqrt{2.5} \approx 1.58$ times the printed one. A printed t of 3.2 is an honest 2.0. **Part 2: two directions at once.** A credit panel's rows are related in two ways. Siblings share an issuer, and every bond in the same month shares that month's market shock. Clustering by issuer lets the noise inside each company be as correlated as it likes; clustering by month does the same inside each month. Doing both is the arithmetic of counting wedding guests who came with the bride's family or with the groom's: add the two lists, then subtract the cousins who are on both, or they get counted twice. Tiny number: if the issuer-clustered variance is 4, the month-clustered variance is 3 and the variance clustered on single issuer-month cells is 1, the two-way variance is $4 + 3 - 1 = 6$. The full version, with the sandwich it all hangs on, is next.

### The estimator, from the first-order condition

Stack $n$ observations: $y \in \mathbb{R}^n$, a regressor matrix $X \in \mathbb{R}^{n \times K}$ of full column rank (a column of ones included), and the model

$$
y = Xb + u, \qquad \mathbb{E}[u \mid X] = 0 .
$$

OLS picks the $\hat b$ that minimizes the sum of squared residuals, which is $\hat b = (X^\top X)^{-1} X^\top y$. It is unbiased whenever the error has conditional mean zero, whatever the error's variance and correlation, so the coefficient survives every complaint in this section. What does not survive is its variance, which is

$$
\operatorname{Var}(\hat b \mid X) = (X^\top X)^{-1}\, X^\top \Omega X\, (X^\top X)^{-1}, \qquad \Omega = \mathbb{E}[u u^\top \mid X] .
\tag{7B.1}
$$

This is the **sandwich**. The two outer factors are the bread; $X^\top \Omega X$ is the meat. Every standard error in finance is a choice of meat. (The normal equations behind it, and the geometry that makes OLS a projection, are in the Full Derivation below, after errors in variables.)

The classical formula sets $\Omega = \sigma^2 I$, so the sandwich collapses to $\sigma^2 (X^\top X)^{-1}$. That is the formula ROBO used, and it assumes the residuals are homoskedastic and uncorrelated. In a bond panel neither holds: a CCC bond's residual has ten times the variance of a BBB's, and eleven Halvorsen bonds in the same month share most of theirs. The classical formula is a sandwich made with a photograph of the meat.

### Heteroskedasticity-robust: White's meat

If the residuals are uncorrelated but have different variances, $\Omega$ is diagonal and we estimate each diagonal entry by the squared residual:

$$
\widehat{X^\top \Omega X} = \sum_{i=1}^n \hat u_i^2\, x_i x_i^\top .
$$

No single $\hat u_i^2$ is a good estimate of $\mathbb{E}[u_i^2]$, but the *sum* is a consistent estimate of the meat, because it averages over $n$ rows. That is the whole trick behind every robust standard error: you never estimate $\Omega$, only the $K \times K$ matrix $X^\top \Omega X$.

### Issuer clustering: the meat that knows about siblings

Now let residuals correlate arbitrarily *within* an issuer and not at all *across* issuers. Index issuers by $g = 1, \ldots, G$ and let $X_g$, $\hat u_g$ be issuer $g$'s rows, all its bonds in all months. The meat becomes one block per issuer:

$$
\widehat{X^\top \Omega X} = c \sum_{g=1}^G X_g^\top \hat u_g \hat u_g^\top X_g, \qquad c = \frac{G}{G-1}\cdot\frac{n-1}{n-K} .
\tag{7B.2}
$$

The block for issuer $g$ allows every pattern of correlation inside it: sibling bonds in the same month, the same bond across months, sibling bonds across months. The factor $c$ is a small-sample correction. The asymptotics run in $G$, not $n$: the clustered estimator is reliable with roughly fifty or more clusters, and a panel of 38,412 bond-months from 206 issuers has 206 observations as far as this formula is concerned. With fewer than about fifty clusters, use the wild cluster bootstrap (§7-B.6).

How much does clustering matter? In the simplest case that still teaches (one regressor, $G$ issuers each contributing $m$ rows, regressor intra-issuer correlation $\rho_x$, residual intra-issuer correlation $\rho_u$), the classical variance is too small by the **Moulton factor**:

$$
\frac{\operatorname{Var}_{\text{true}}(\hat b)}{\operatorname{Var}_{\text{classical}}(\hat b)} \approx 1 + (m-1)\,\rho_x\,\rho_u .
\tag{7B.3}
$$

For an issuer-level signal such as runway, a rating, equity momentum or the PRS, every bond of the issuer carries the same value, so $\rho_x = 1$ and the factor is $1 + (m-1)\rho_u$, which is the denominator of effective breadth, $N/(1 + (m-1)\rho)$, from Law 2. It is one formula wearing two ties: one tie says your standard error is too small, the other says your bets are too few, and both say forty-seven CUSIPs of one issuer are one hat. For Halvorsen's eleven bonds with sibling residual correlation 0.6, the factor is $1 + 10 \times 0.6 = 7$, and a panel made entirely of Halvorsens would need its classical standard errors multiplied by $\sqrt{7} \approx 2.65$ *(illustrative)*. A bond-level signal with low sibling correlation, such as a bond's own bid–ask bounce, has $\rho_x$ near zero, and clustering barely moves it. That asymmetry is why Theo's runway, a company number, lost most of its t-statistic. Figure 7-B.1 plots the multiplier and the breadth it implies.

![Figure 7-B.1: Left, how far an issuer-level signal's standard error inflates over the classical formula as bonds per issuer m grows (the Moulton factor with the signal shared across the issuer). Right, the same formula as effective breadth: Halvorsen's eleven bonds at sibling correlation 0.6 carry 1.57 bonds' worth of independent information, and no number of extra rows lifts an issuer past 1/ρ. Illustrative: computed from equation 7B.3, not market data.](assets/figures/ch07b_moulton_breadth.png)

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

Suppose the regressor is measured with noise, $\tilde x = x + \eta$, with $\eta$ independent of everything. Then the slope is biased toward zero by the share of the regressor's variance that is signal, $\sigma_x^2/(\sigma_x^2 + \sigma_\eta^2)$ (derived below). This is attenuation, and it is why betas estimated on stale marks are too small: the mark is the truth plus a lag, the lag behaves like noise in a same-day regression, and the Dimson correction of §8.5 recovers the slope by summing lagged coefficients (Law 9).

The more dangerous case is *correlated* errors in variables. If the same price error enters both the signal and the next return, the bias is no longer toward zero; it manufactures a premium. A bond whose month-end price is recorded too low looks cheap on any price-based value signal, and its next-month return is spuriously high because the error reverses. Dickerson, Robotti and Rossetti (2026) build a premium out of nothing this way with two bonds and half a percent of recording noise; Chapter 9-B works their example. The fix is to break the link between the price in the signal and the price in the return, with a gap of at least a day, which §7.2 and Chapter 9-B treat in full.

#### The Full Derivation: the sandwich, the cluster meat and the Moulton factor

*The sandwich (7B.1).* OLS minimizes $\lVert y - Xb \rVert^2$. Setting the gradient to zero gives the normal equations:

$$
X^\top\big(y - X\hat b\big) = 0 \quad\Longrightarrow\quad \hat b = (X^\top X)^{-1} X^\top y .
$$

The normal equations are a geometric statement: the residual vector is orthogonal to every column of $X$, so $X\hat b$ is the projection of $y$ onto the space the regressors span. Substitute $y = Xb + u$:

$$
\hat b - b = (X^\top X)^{-1} X^\top u .
$$

Taking expectations conditional on $X$ gives $\mathbb{E}[\hat b \mid X] = b$: OLS is unbiased whenever the error has conditional mean zero, whatever its variance and correlation. Taking the outer product of $\hat b - b$ with itself and conditioning on $X$ gives $(X^\top X)^{-1} X^\top \mathbb{E}[uu^\top \mid X] X (X^\top X)^{-1}$, which is (7B.1).

*The cluster meat (7B.2).* White's estimator above replaces each diagonal entry of $\Omega$ by a squared residual; no single $\hat u_i^2$ estimates $\mathbb{E}[u_i^2]$ well, but the $K \times K$ sum $\sum_i \hat u_i^2 x_i x_i^\top$ is consistent because it averages over $n$ rows. If residuals correlate within issuer $g$ and not across issuers, $\Omega$ is block-diagonal with one block per issuer, and $X^\top \Omega X = \sum_g X_g^\top \Omega_g X_g$. Replace each unknown block $\Omega_g$ by the outer product of that issuer's residual vector, $\hat u_g \hat u_g^\top$, and the same averaging argument, now over $G$ issuers instead of $n$ rows, makes the sum consistent as $G$ grows. The constant $c$ in (7B.2) corrects the small-sample downward bias of the plug-in residuals.

*The Moulton factor (7B.3).* Take one demeaned regressor, $G$ issuers each contributing $m$ rows, regressor intra-issuer correlation $\rho_x$ and residual intra-issuer correlation $\rho_u$. The variance of the score $\sum_i x_i u_i$ is the sum of the $n$ diagonal terms, $n\sigma_x^2\sigma_u^2$, plus the $n(m-1)$ same-issuer cross terms, each $\rho_x\sigma_x^2\cdot\rho_u\sigma_u^2$. The total is $n\sigma_x^2\sigma_u^2\,[1 + (m-1)\rho_x\rho_u]$. The classical formula assumes only the diagonal, and since the bread is the same in both, the ratio of the true variance of $\hat b$ to the classical one is the bracket, which is (7B.3).

*Attenuation.* With $\tilde x = x + \eta$ and $\eta$ independent of $x$ and $u$,

$$
\operatorname{plim}\hat b = \frac{\operatorname{Cov}(\tilde x, y)}{\operatorname{Var}(\tilde x)} = \frac{b\,\sigma_x^2}{\sigma_x^2 + \sigma_\eta^2} = b\,\frac{\sigma_x^2}{\sigma_x^2 + \sigma_\eta^2} ,
$$

so the slope is shrunk toward zero by the signal share of the regressor's variance, and no amount of extra data removes it.

#### Long Scene: One March, Counted Once

*A Friday-afternoon replay in October 2026, run as a review rather than blind: the data runs to 30 June 2020 and everyone may look at all of it. The desk, its 2020 panel and every regression, spread level and statistic attributed to it are fictional (the desk's fictional run, illustrative). Dov Adler's pod at Vantress and its Pair Book are fictional composites (Chapter 1-B; Chapter 8 §8.4). The dated market events are real and sourced in Chapter 1 §1.8.2.*

Most Friday afternoons Ines runs a replay, and most replays are blind: the calendar goes back to a date and nobody may mention what happened next. This one was not. "You've all played this hand," she said, uncapping a marker. "We traded it on a Saturday, off Mags's run sheets. Today we don't trade it. We count it."

She wrote five dates down the left edge of the whiteboard, one per line, the way she writes a hand history. Thursday 12 March 2020, when LQD closed five percent below its own net asset value. Monday 23 March, when the Fed announced its secondary-market corporate facility. Wednesday 25 March, when S&P cut Ford to BB+ (as reported by Bloomberg), with roughly \$36bn of Ford debt due out of the investment-grade index at the 31 March rebalance (T. Rowe Price, Nov 2020). Thursday 9 April, when the Fed extended its facilities to issuers that had been investment grade as of 22 March, which covered Ford. And Tuesday 12 May, the first day the Fed bought corporate-bond ETFs. The Saturday replay had traded those dates as a hand, one day at a time (§1.8.2). Today's rule, Ines said, was different: every number that went on the board needed an error bar, and every error bar needed to say what it had counted.

Kaz had come prepared, which with Kaz meant a panel. Six hundred and forty bonds from two hundred issuers, everything in the desk's universe that had started 2020 investment grade, every trading day from 1 April to 30 June: 63 days, 40,320 bond-days. The left-hand side was each bond's daily IDO return, what was left after carry, rates and DTS-scaled market beta had been stripped out, because on this desk a return with beta still in it was not allowed in the room. The right-hand side was a single dummy, equal to one for every Ford Motor Credit bond after the rebalance and zero for everything else. Thirty-six Ford CUSIPs in all.

"Every regression on this desk says the same thing," Ines said while it loaded. "When $x$ is one unit higher, the average $y$ is $b$ higher. Empirical duration says it per basis point of Treasury yield. The trend book says it per unit of signal. Theo's says it per week of runway. Kaz's says it per fallen angel. The $b$ is the easy part. The error bar decides whether anybody gets paid. Kaz, the $b$."

"Four point one basis points a day of idio," Kaz said, "for a bond that has just been thrown out of its index. Classical t of fourteen point two." They paused, in the manner of someone who had rehearsed the pause. "Annualized that's about ten points of alpha. Fallen angels are the best trade in credit and I have a fourteen to prove it."

Theo looked at the Post-it on the bottom of his monitor.

"That's one company," he said. "And one spring."

He was surprised by how quickly it came out. A week earlier he would have asked for the confidence interval and written it down. "Thirty-six CUSIPs of Ford are one Ford. If Ford's bonds had a good April they had it together, because the reason they had it was Ford's. And all six hundred and forty bonds had the same April, because the reason for that was the Fed."

Kaz clustered by issuer, and the t fell from 14.2 to 2.6. Clustered by trading day, so that every bond on a given day shared that day's shock, it fell to 2.5. Two-way, issuer and day with the doubly counted cells subtracted, it came out at 1.8.

"Below two," Kaz said, "which is a respectable place to be, for a t-statistic or a credit rating."

"And the 1.8 is generous," Ines said. "Issuer clustering learns how much a block can wobble by looking at all the blocks. The question you're asking is about one block. A formula that has one treated cluster to learn from can't tell you how far that cluster would move on a re-deal, so I don't believe the 1.8 in either direction." She wrote *wild cluster bootstrap* on the board and underlined it twice, which on Ines's board means *later, and not optional* (§7-B.6 is the later). "How many independent fallen angels are in this regression?"

"One," Theo said.

From the far end of the desk Mags said, without looking up: "Back in my day we called that a position, not a sample."

Kaz was not finished, and was not wrong to keep going. "Fine. Daily idio is noise. The effect is the reversal. Sixty trading days after the rebalance the forced selling is over and the discount comes back." They built the label in front of everyone: the Ford block's sixty-day forward IDO return over the panel's, measured from each of the 63 days of the quarter, so every observation looked sixty days ahead. Newey–West with fifty-nine lags, the textbook $h - 1$. A t of 3.3.

"Your consecutive labels share fifty-nine of their sixty days," Theo said.

"That's what the lags are for."

"The lags get you about two-thirds of the way," Ines said, "even when the sample is long, because of how the Bartlett weights taper." (§7-B.2 does the arithmetic.) "Your sample isn't long. You have 63 start dates and every label is sixty days, so the whole thing spans 123 trading days. That is two non-overlapping sixty-day returns, Kaz, and both of them are Ford."

"Then I need more data."

"You need more fallen angels," Mags said. "By my count the tape since TRACE started has four waves of them in it: 2005, 2008 and 2009, the energy names in 2015 and 2016, and this one. That's your sample size for the reversal. Four. One of them is the one you're looking at." Chapter 9 meets the same flows as a forced-seller factor (§9.6.1), and the factor inherits the short count.

Ines wrote it underneath the dates, because it was the sentence she wanted people to leave with. "Twenty years of an annual signal is about twenty observations, a sample that would embarrass a focus group. When the horizon is a big slice of the sample, Newey–West over-rejects whatever kernel you hand it. The cure isn't a better kernel. It's a longer history, more independent instruments, or humility."

"I'll start with humility," Kaz said. "It's the only one I can get by Monday."

Ines turned the whiteboard round. On the back she had already drawn the hand she had come to deal.

It was a pair. Long Ford Motor Credit senior unsecured, short GM Financial senior unsecured, sized so that the two legs carried the same market-value DTS, the leftover index beta trimmed in CDX IG. It was, leg for leg, the third row of the Pair Book that Dov Adler's pod keeps at Vantress, a replay Dov had built of exactly this spring (§8.4), and Ines knew it because her desk quotes the pod most weeks and had quoted its GM protection earlier that month (Chapter 8-D). Dov had written the thesis as he writes all of them, one sentence with a date: Ford Credit's notes give back the discount that index-forced selling put on them, measured against an auto lender that stayed investment grade, by 30 September 2020. GM had stayed investment grade. Ford had not. The two captive lenders fund the same car buyers through the same dealers, so the hedge removes the common auto factor along with the market, and what it leaves is the part of Ford's spread that was a mandate's price rather than a credit's.

"Dov's ledger row has a blank where the half-life goes," Ines said, "so Kaz has fitted one."

Kaz had fitted it the way they had fitted the dummy: on everything. Ford Credit had thirty-six bonds in the panel and GM Financial twenty-two, so Kaz had built every Ford-minus-GM spread differential across the 792 CUSIP pairs, stacked them, and run one pooled AR(1) on the daily differential from 1 April to 30 June. The autoregressive coefficient was 0.93 a day, which is a half-life of $\ln 2/(-\ln 0.93) \approx 9.6$ trading days, and the t-statistic on the pull toward the mean was minus forty-two.

"Which," Kaz said, "is the answer to everything."

#### Decision point: the Ford–GM card

It is a Friday afternoon in October 2026. Dov's pod has the same two names on again, live, as Chapter 8-D's PB-19, with a thesis that ends *half of it is gone by 31 March 2027*. Kaz's 2020 estimate is on the board. Ines handed out the cards. *Write three things: the half-life you estimate for the differential, the t-statistic you would defend for it, and your size, as a fraction of the replay's \$25mm long.* Before you read on, write yours.

Kaz wrote: *9.6 days. t = −42. Full size, and add.*

Theo wrote: *One pair, so one series: 63 days. t about −1.5. Half-life: don't know. Half size.*

Mags wrote: *As long as a forced sale lasts. No t. Whatever I can carry to the far end of my not knowing.*

Ines turned the cards over and graded them the way she grades everything, against what was actually on the table.

**The answer.** The 792 CUSIP pairs are one pair photographed 792 times. Every Ford bond shared Ford's news and every GM Financial bond shared GM's, so stacking them multiplies the rows and adds no information, and the t of −42 is roughly the honest t multiplied by $\sqrt{792} \approx 28$. Cluster by issuer pair and there is exactly one cluster, which no clustering formula can use; the honest unit is the single differential series, 63 daily points. On 63 points the AR(1) coefficient of 0.93 has a standard error of about $\sqrt{(1 - 0.93^2)/63} \approx 0.046$, so the t on the pull toward the mean is about $-0.07/0.046 \approx -1.5$, and even that is read against the wrong bar: a test of whether a series mean-reverts at all is a Dickey–Fuller test (Chapter 7's box in §7.3), whose 5% critical value with a constant is about $-2.9$, not $-1.96$. A 95% interval for the coefficient runs from about 0.84 to 1.02, which is a half-life of four days at one end and never at the other. Two more things push the 9.6 days the wrong way. The fastest "reversion" in the sample happened on one day, 9 April, when the Fed's eligibility decision lifted every recent fallen angel at once; that is the rating-bucket factor moving, not Ford's discount closing, and with that day dummied out the coefficient rises to about 0.96, a half-life of 17 days. And on a short sample an estimated autoregressive coefficient is biased toward zero by roughly $(1 + 3\rho_1)/T$, with $\rho_1$ the lag-one autocorrelation (not the EWMA decay $\varphi$), about 0.06 here (Kendall worked this out in 1954), so a fitted 0.96 is consistent with anything up to a random walk. The half-life the data can defend is "longer than this sample can see". The t it can defend is below any bar worth the name. And the size is the one you would hold if the half-life were the long end of the interval, because for as long as the differential behaves like a random walk the pair's P&L does too, and then the stop sets the size (Chapter 8-B), not the t.

**What happened.** In the replay the pod took about five of its six points of convergence by September and closed the pair on Ford's bond–CDS basis (Chapter 24 §24.7), a pace that, fitted after the fact, is a half-life of roughly two months on the whole move *(illustrative)*. The platform's x-ray put about \$0.5mm of the \$1.25mm gross on the fallen-angel factor rather than on Ford, which is the 9 April day showing up as money. Kaz's 9.6 days was too fast by a factor of five and was mostly the Fed. Theo's card got the t and the interval right and the size roughly right. Mags's card had no numbers on it and was the closest to the truth, which Ines said was not a compliment to the card.

"And Dov's live sentence," Ines said, tapping *31 March 2027*, "implies a half-life of about seven months. That's not Kaz's ten days and it shouldn't be. In 2026 there's no forced seller and no central bank, only a rating-bucket toll. A half-life is a property of a regime, and you've measured one regime once."

Mags had come over to look at the board. "The last time somebody told me Ford and GM were two observations," she said, "was May 2005. S&P cut them both on the same Thursday." She did not tell the rest; Chapter 6 §6.9.2 deals that hand and Chapter 23 §23.6 grades it, including what the two names weighed in each index. "Two names, one cluster. Write that on the card too."

> **The Pair.** *Pair Book PB-03 as this chapter's statistics see it (Dov Adler's pod at Vantress, fictional composites; legs, sizes and costs are Chapter 8 §8.4's, a 2020 replay, all illustrative).*
>
> **Pair.** Long \$25mm face of Ford Motor Credit senior unsecured, short about \$39mm face of GM Financial senior unsecured.
>
> **Hedge.** Market-value DTS at 1.65; the GM leg in borrowed bonds through the prime broker; beta residue in CDX IG; the DV01 residue in Treasury futures.
>
> **Removed.** Index spread beta and the common auto-lender factor, since both captives fund the same car buyers.
>
> **Remains.** Ford's forced-seller discount and its refinancing story: one pair, one regime, a half-life somewhere between four days and never, and a t of about −1.5 on 63 days.
>
> **Leaks.** The rating-bucket factor, left open on purpose (Ford high yield, GM investment grade), so 9 April's facility news arrived as a factor jump that an AR(1) reads as reversion; and the GM borrow, recallable on a day's notice.
>
> **Costs.** A borrow fee of 35 bp, about \$0.13mm a year, plus the CDX carry on the residue; near-zero coupon carry; about \$0.45mm of half-spreads each way. The toll is getting in and out, not waiting.

The first of those mistakes had been Theo's, on the evening of the cold open. After Ines walked away he tried to reproduce Kaz's issuer-clustered 2.4 on his own, to be sure he understood it, and the first identifier he reached for was the CUSIP, because at PJT the CUSIP was what you traded and what the claims register listed. The t-statistic came back at 5.8, and for about four minutes he believed he had defended his six. Kaz, passing behind him with a coat on, read the screen. "That is a rigorous way of doing nothing," they said. A CUSIP cluster lets each bond's own months correlate with one another, which is real and small. It says nothing about eleven Halvorsen bonds sharing one company, which was the whole problem: with runway identical on every sibling, the sibling correlation was where the t had been hiding. The mistake cost four minutes and a second Post-it, *parent, not CUSIP*, which by the desk's standards was cheap. "Cluster on whatever makes the rows move together," Kaz said from the door. "For a company number, that's the company." The box keeps the other three ways the same mistake comes back.

> **Ways This Blows Up.** (1) *Clustering on the CUSIP* (Theo's evening, above): cluster on the ultimate parent, the same key §7.7 groups folds by. (2) *Clustering on ticker.* Two issuers under one sponsor can share a credit agreement's trapdoors; for LMT-sensitive signals, cluster on the sponsor family. (3) *Few clusters.* A regression across eleven sectors clustered by sector has eleven observations of the meat; use a wild cluster bootstrap and say so. (4) *A fixed effect that eats the signal.* Issuer fixed effects on a rating regression identify the coefficient only from rating changes, which are rare and lagged; the standard error explodes, correctly.

*Used in:* §8.2 (empirical duration), §8.5 (Dimson betas), §8.6 (minimum-variance hedges), §9.3.4 and §9.7 (factor residuals and combinations), §10.4 and §10.5.3 (trend–carry and lead–lag regressions), §11.2.2 (asymmetric-beta regression), §11.4.2 (issuer-clustered hazard logit), §17.2 (pooled desmoothing regressions), §28.2 (effective breadth); Chapter 9-B (correlated errors in variables).


## 7-B.2 Overlapping Returns, Autocorrelation and Newey–West

### Desk framing: the 12-month return you counted twelve times

Chapter 10's trend signal predicts a 12-month return, and the natural way to test it is to sample that 12-month return every month. Consecutive observations then share eleven of their twelve months. You have not collected 240 observations in twenty years; you have collected about twenty, each photographed twelve times from slightly different angles. Kaz's sixty-day reversal labels in the Friday replay were the same problem at a daily frequency, and with a sample barely longer than the label.

> **Math, Gently.** *Overlap: one rumor, twelve messengers.* Suppose a rumor reaches you from twelve people. If each of them heard it on their own, twelve is strong evidence. If all twelve heard it from the same man at the same bar, you have heard it once, twelve times. An overlapping return is the second kind of rumor. A three-month return measured at the end of every month shares two of its three months with the one before it, so each month's news turns up in three consecutive observations; count them as independent and every piece of news has been counted three times. The variance of your average is then about three times what the naive formula reports, and the t-statistic is too large by $\sqrt 3$. Tiny number: a naive t of 3.5 on three-month returns sampled monthly is an honest $3.5/\sqrt 3 \approx 2.0$. The general rule, that an $h$-period return sampled every period is too confident by $\sqrt h$, comes from counting how many messengers share each piece of news, and the full version is next.

### How much overlap inflates a t-statistic

Let one-period returns be i.i.d. and let $R_t$ be the $h$-period return ending at $t$, sampled every period. Two such returns $k < h$ periods apart share $h - k$ of their periods, so their correlation is $1 - k/h$, a triangle that falls from one to zero over $h$ lags. Summing the triangle shows that the variance of the sample mean is $h$ times what the naive formula reports (derived below), so the naive t-statistic is too large by $\sqrt h$. For a 12-month return sampled monthly that is $\sqrt{12} \approx 3.5$: a naive t-statistic of 7 is an honest 2. The same arithmetic applies to any overlapping label, which is why §7.4's triple-barrier labels need §7.6's uniqueness weights.

### The Newey–West estimator

Regression residuals with serial correlation need a meat that includes cross-products at nonzero lags. Write the score $g_t = x_t u_t$ and its sample autocovariances $\hat\Gamma_j = \frac{1}{T}\sum_{t=j+1}^{T} \hat g_t \hat g_{t-j}^\top$. Newey and West (1987) estimate the long-run variance as

$$
\hat S^{\text{NW}} = \hat\Gamma_0 + \sum_{j=1}^{L}\Big(1 - \frac{j}{L+1}\Big)\big(\hat\Gamma_j + \hat\Gamma_j^\top\big),
\qquad
\widehat{\operatorname{Var}}(\hat b) = (X^\top X)^{-1}\big(T\,\hat S^{\text{NW}}\big)(X^\top X)^{-1} .
\tag{7B.4}
$$

The triangular (Bartlett) weights are not decoration. Summing autocovariances with equal weights up to lag $L$ (the Hansen–Hodrick choice) is exactly right for an MA($h-1$) but can produce a negative variance in a finite sample. Up to end effects, the Bartlett-weighted sum is the average outer product of score sums over windows of length $L+1$, divided by $L+1$: a scaled sample variance, and a variance of anything cannot be negative.

The price of that guarantee is under-correction, and it is larger than most people expect. With the textbook choice $L = h - 1$ and a 12-month return sampled monthly, Newey–West reports a variance multiplier of about 8.0 where the truth is 12: two-thirds of the variance, and a t-statistic still about 22% too large. With $L = 2h - 1 = 23$ it recovers about 10.0, or 83% (the arithmetic is in the Full Derivation below). That is why the desk sets $L$ to at least $1.5h$–$2h$ for overlapping returns, and reports beside the Newey–West result the $h$ non-overlapping subsamples (start in January, start in February, and so on), whose dispersion is a useful honesty check on its own. For autocorrelation that is not mechanical (stale marks in daily illiquid-bond returns) the plug-in rule $L = \lfloor 4(T/100)^{2/9} \rfloor$ is a reasonable floor, and the larger of the two lag choices wins. Figure 7-B.2 shows where the missing variance goes.

![Figure 7-B.2: A 12-month return sampled monthly. Left, the Bartlett weights times the overlap triangle show where the variance goes missing. Right, with the textbook L = 11 lags Newey–West recovers a variance multiplier of 8.0 against a truth of 12, so the t-statistic stays about 22% too large; L = 23 recovers 10.0. Illustrative: exact calculation from equation 7B.4 for i.i.d. one-month returns, h = 12.](assets/figures/ch07b_newey_west_shortfall.png)

No lag choice rescues a horizon that is a large slice of the sample; that limit, and the three cures for it, belong to the Friday replay above, where Kaz's sixty-day labels on sixty-three days turned out to be two observations of one company.

#### The Full Derivation: the overlap triangle and the Bartlett shortfall

*The triangle.* Let one-period returns $r_t$ be i.i.d. with variance $\sigma^2$, and define the $h$-period overlapping return $R_t = \sum_{j=0}^{h-1} r_{t-j}$. Two such returns $k < h$ periods apart share $h - k$ terms, so

$$
\operatorname{Cov}(R_t, R_{t-k}) = (h-k)\,\sigma^2, \qquad \operatorname{Corr}(R_t, R_{t-k}) = 1 - \frac{k}{h} .
$$

*The factor of $h$.* The variance of the sample mean of $T$ such observations is, for $T \gg h$,

$$
\operatorname{Var}\big(\bar R\big) \approx \frac{h\sigma^2}{T}\Big[1 + 2\sum_{k=1}^{h-1}\Big(1 - \frac{k}{h}\Big)\Big] = \frac{h\sigma^2}{T}\cdot h ,
$$

because the bracket sums to $1 + 2(h-1) - (h-1) = h$. The naive formula reports $h\sigma^2/T$. It is too small by a factor of $h$, so the naive t-statistic is too large by $\sqrt h$.

*The Bartlett shortfall.* Suppose the truth is the overlap triangle and you set $L = h - 1$. Newey–West weights the lag-$k$ autocorrelation $1 - k/h$ by $1 - k/h$ again, so the estimator recovers

$$
1 + 2\sum_{k=1}^{h-1}\Big(1 - \frac{k}{h}\Big)^2 \quad\text{instead of}\quad h .
$$

For $h = 12$ the sum is $\frac{1}{144}\sum_{j=1}^{11} j^2 = \frac{506}{144} \approx 3.51$, so the multiplier is $1 + 2 \times 3.51 \approx 8.0$ against a truth of 12, and $\sqrt{12/8.0} \approx 1.22$ is the 22% by which the t-statistic stays too large. With $L = 23$ the weights become $1 - k/24$ on the same triangle, and the multiplier is about 10.0. For large $h$ with $L = h - 1$ the recovered share tends to two-thirds, which is why Kaz's $L = 59$ on sixty-day labels fell short by the same third.

Kaz borrowed Theo's copy of the Dickerson, Robotti and Rossetti printout that evening, found the table where every factor's premium was rebuilt hundreds of ways and its spread across the rebuilds set beside its ordinary standard error, and read it slowly. The Trend Watch below has the numbers.

"So the error bar has an error bar," Kaz said.

"Everything does," Ines said. "The trick is knowing which one is bigger before you push the chips in."

> **Trend Watch.** *The second error bar (2009–2026).* **(1) The baseline.** Petersen (2009, *Estimating Standard Errors in Finance Panel Data Sets*, Review of Financial Studies 22(1)) showed that a large share of published finance panel studies reported standard errors that ignored firm or time correlation, and that the bias could be large; issuer clustering became the default in bond-panel work over the following decade. **(2) Non-standard errors.** In June 2024 Menkveld and coauthors published *Nonstandard Errors* (Journal of Finance 79(3), 2339–2390): 164 research teams tested the same hypotheses on the same data, the dispersion of their estimates was sizable, and the teams underestimated it. **(3) Bonds.** In April 2026 Dickerson, Robotti and Rossetti applied the idea to 108 corporate-bond factors (*The Corporate Bond Factor Replication Crisis*, arXiv:2604.07880). Across 648 defensible data-filtering paths per factor, the average non-standard error of a factor premium was 0.35% per month against an average premium of 0.33%, a ratio to the ordinary standard error of 1.15; across 168 methodological constructions the ratio averaged 1.45. Of 432 factor–specification combinations, only 26 bond-CAPM alphas survived a Benjamini–Hochberg false-discovery control, and correlated measurement error inflated price-based premia by 15–90 bp per month. **What it means for the desk:** report two error bars. One is the sampling error this section computes. The other is the specification error: the spread of your estimate across the defensible choices you did not make. When the second exceeds the first, the clustered t-statistic is not the most important number on the page. The full audit is §7.2 and Chapter 9-B.

*Used in:* §7.4 and §7.6 (overlapping labels and uniqueness), §7.8 (Sharpe-ratio inference), §10.2.3 and §10.4 (trend tests on overlapping returns), §10.6.1 (the straddle regression with Newey–West errors), §10.5.3 (lead–lag at the right horizon), §28.3 (signal half-lives); Chapter 9-B (non-standard errors in the factor zoo).


## 7-B.3 Logistic Regression and Calibration: One Object for Every Probability on the Desk

### Desk framing: a probability is a promise with a number on it

One morning that week Theo noticed the same S-shaped curve on three screens inside ten minutes. Ines's toxicity monitor was turning an RFQ's features into the chance that the sender knew something (§1.3.3, §3.2.2). The RFQ engine was turning a quote into the chance of winning it (§18.7), a cousin of the chance a resting quote fills (§2.5.1). And Kaz's twelve-month default model (§11.4) was turning an issuer's numbers into a PD, with relatives that score an LMT within a year (the PRS, §13.8) and the chance a line sat in a portfolio trade because the client knew something (§19.8). Seven probabilities across the book, one curve. They are one object, and this section builds it once.

> **Math, Gently.** *Evidence adds in log-odds.* Chapter 1's box in §1.3.3 did Bayes' rule in odds: multiply the prior odds by how much likelier the evidence is if the story is true than if it is false. Take logarithms and the multiplication becomes addition, which is the whole reason to bother. Picture a kitchen scale rather than a dial. The base rate is the weight already sitting in the pan, and every clue adds or removes its own weight, independently of the others, so the reading does not care in what order the clues arrived. Tiny number: a 2% base rate is odds of $0.02/0.98 \approx 0.0204$, which is log-odds of about $-3.9$. Two independent clues with likelihood ratios 3 and 2 add $\ln 3 + \ln 2 \approx 1.1 + 0.7 = 1.8$, so the log-odds become about $-2.1$; equivalently, the odds are multiplied by 6, to $0.122$, and the probability is $0.122/1.122 \approx 10.9\%$. The logistic function is only the gauge that turns the scale's reading back into a probability. Why each clue's weight comes out as a straight line in the features is next.

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

It is concave, so it has at most one maximum, and Newton's method finds it in five to eight steps (the gradient, the Hessian and the iteration are derived below). At the maximum, the first-order condition for the intercept says $\sum_i \hat p_i = \sum_i y_i$. A fitted logit always reproduces the sample's event rate exactly. Calibration in the large, in sample, is free. It is the only free lunch in this chapter, and it is served only in sample.

The classical variance is the inverse information, $(X^\top \hat W X)^{-1}$ with $\hat W = \operatorname{diag}\big(\hat p_i(1-\hat p_i)\big)$. On an issuer-month panel it has the same disease as §7-B.1, and the same cure: keep $(X^\top \hat W X)^{-1}$ as bread and use the issuer-clustered meat $\sum_g X_g^\top \hat e_g \hat e_g^\top X_g$ with $\hat e = y - \hat p$. That is the modern form of Shumway's correction, which divided chi-squared statistics by the average number of firm-years per firm (§11.4.2).

#### The Full Derivation: the logistic likelihood

Because $\partial p_i / \partial z_i = p_i(1-p_i)$ for $z_i = x_i^\top b$, the gradient and Hessian of $\ell$ are

$$
\nabla \ell(b) = \sum_i (y_i - p_i)\,x_i = X^\top (y - p), \qquad \nabla^2 \ell(b) = -X^\top W X, \quad W = \operatorname{diag}\big(p_i(1-p_i)\big) .
$$

The Hessian is negative definite, so $\ell$ is concave and has at most one maximum. Newton's method, $b \leftarrow b + (X^\top W X)^{-1} X^\top (y - p)$, is iteratively reweighted least squares and usually converges in five to eight steps. At the optimum the score equations read $X^\top(y - \hat p) = 0$; the first row, for the intercept, says $\sum_i \hat p_i = \sum_i y_i$, which is the free lunch above. The inverse of the negative Hessian at the optimum, $(X^\top \hat W X)^{-1}$, is the classical variance.

> **Ways This Blows Up.** *Separation.* If some combination of features separates events from non-events perfectly (on a hundred LMTs, "loan below 80 and runway under nine months" nearly does, §13.8), the likelihood keeps rising as the coefficients run to infinity, and the optimizer reports whatever it had when it gave up. Fix with a ridge penalty, a weakly informative prior (the MAP logit of §13.8), or Firth's bias-reduced likelihood, and report that you did. *Rare events.* With a 2% base rate, the intercept is estimated from a few dozen events; the slopes are fine and the level is fragile, so recalibrate on the deployment base rate. *Clipping.* Probabilities of exactly 0 or 1 make the log-loss infinite; clip to $[10^{-6}, 1 - 10^{-6}]$ and log it.

### Calibration: is 4% really 4%?

A model can rank perfectly and be wrong in every level, or be perfectly calibrated and rank nothing (predict the base rate for everyone). Ranking is **power**, measured by the AUC and the CAP curve (§11.5). Levels are **calibration**, and the desk needs both: power picks which bonds to avoid, calibration sets how much spread is fair compensation.

> **Math, Gently.** *Ranking versus level, or the honest weatherman who tells you nothing.* Picture two weather forecasters in a city where it rains on 30% of days. The first says "30% chance of rain" every morning of every year. He is perfectly **calibrated**, because on the days he says 30% it rains 30% of the time, and he is perfectly useless, because he never tells you which days to carry an umbrella. The second says 60% on half the mornings and 0% on the rest; on her 60% days it rains six times in ten, and on her 0% days never. She is calibrated too, and she also **ranks**: she separates the wet days from the dry ones. A **Brier score** grades both jobs at once: it is the average of (forecast minus outcome) squared, with the outcome 1 for rain and 0 for none, and lower is better. Tiny number: the first forecaster scores $0.3 \times (1 - 0.3)^2 + 0.7 \times 0.3^2 = 0.3 \times 0.7 = 0.21$ every year. The second scores $\tfrac12\big[0.6 \times 0.4^2 + 0.4 \times 0.6^2\big] + \tfrac12 \times 0 = 0.12$, and the whole 0.09 between them is ranking. A default model has the same two jobs, picking which bonds to avoid and saying how often they will default, and the decomposition that pulls the two apart is next.

Calibration is measured with a **proper scoring rule**, one whose expected value is optimized by reporting the true probability. The log loss is proper: if $Y \sim \text{Bernoulli}(p)$ and you report $q$, the expected loss $-p\ln q - (1-p)\ln(1-q)$ has derivative $-p/q + (1-p)/(1-q)$, which is zero only at $q = p$. A proper scoring rule is the one poker table where bluffing loses by construction. The **Brier score** $\text{BS} = \frac{1}{n}\sum_i (p_i - y_i)^2$ is also proper, and on $K$ probability buckets it decomposes (Murphy 1973) as

$$
\text{BS} = \underbrace{\sum_k \frac{n_k}{n}\big(\bar p_k - \bar y_k\big)^2}_{\text{reliability (want small)}} \;-\; \underbrace{\sum_k \frac{n_k}{n}\big(\bar y_k - \bar y\big)^2}_{\text{resolution (want large)}} \;+\; \underbrace{\bar y(1 - \bar y)}_{\text{uncertainty}} ,
$$

up to a within-bucket term. Reliability is calibration, resolution is power, and uncertainty is the base rate's fault. A reliability diagram plots $\bar y_k$ against $\bar p_k$; a calibrated model sits on the diagonal.

A model that ranks well but is mis-leveled can be repaired on a holdout without touching the ranking. **Platt scaling** fits a two-parameter logit, $\operatorname{logit} p^{\text{cal}} = a + c\,\operatorname{logit}\hat p$, which fixes a shifted base rate ($a$) and over- or under-confidence ($c$). **Isotonic regression** fits the best monotone step function by pooling adjacent violators and needs more data. Tree ensembles and naive-Bayes scores are typically overconfident at the extremes, so their outputs are recalibrated before anyone calls them probabilities (Niculescu-Mizil and Caruana 2005; §7-B.7).

**A worked check.** A model assigns 4% twelve-month PDs to 150 B3 issuers; nine default, 6%. Is the model wrong? Under independence the standard error of the default rate is $\sqrt{0.04 \times 0.96/150} \approx 1.6\%$, so the miss is 1.25 standard errors: no evidence. And independence flatters the test. Defaults are correlated, the true standard error is larger, and §7-B.6 shows that with realistic correlation even a tenfold miss can be noise. A single cohort is close to a single observation.

Ines read the worked check over Kaz's shoulder and then told them the dealer's version of it, because before this desk she had run one.

> **View From Another Seat.** *The dealer desk's win curve (a generic seat; no firm is named).* An electronic credit-trading desk at a dealer fits the same object as Kaz's PD model: a logit that turns a quote's distance from the composite, the size, the number of dealers in competition and the client's tier into the probability of winning the RFQ (§18.7). From that seat the logit has a problem a default model does not. The dealer's own quoting moves the base rate it is estimating. Tighten the quotes for a week to win back share and the win rate rises at every distance, so a curve fitted on last month's quotes is mis-leveled by Monday, while its slopes, the shape of the S, usually hold for longer. The dealer also sees outcomes only for the RFQs it chose to answer, so the sample is cut by its own decisions. So the desk recalibrates the intercept on a short, recent window, often weekly, and refits the slopes far less often. It is Platt scaling as a routine, and it is the free lunch of calibration in the large, paid for every week, because the sample it was free in keeps moving.

**One collision, named.** The "logistic adoption curve" of §2.3.1 is a different object with the same shape: a deterministic function of time fitted by nonlinear least squares to market shares. It has no Bernoulli likelihood and no calibration; it shares only the S. Appendix A §A.3 records the collision.

*Used in:* §1.3.3 (toxicity in log-odds), §2.5.1 (fill probabilities), §3.2.2 ($\pi(x)$ from markouts), §11.4.2 and §11.5 (PD logit, power curves), §13.8 (the PRS as a MAP logit), §18.7 (RFQ win curves), §19.8 (basket adverse selection); §7-B.4 (the logit as a discrete-time hazard) and §7-B.7 (recalibrating boosted trees).


## 7-B.4 Survival Analysis in the Right Order: Censoring, $S$, PD and $\lambda$, Kaplan–Meier, Cox

### Desk framing: the clock that stops before the story ends

On Monday 12 October Mags put eight real liability-management deals on a whiteboard and stopped the clock before two of them had finished; the Long Scene below is that morning. Survival analysis is the discipline of using the issuers whose story you did not see finish without pretending you know how it ended. Censoring is the signal (Law 14), and the RSSG reader has been doing this informally for years: the 13-week model was a hazard curve all along (§5.1.5).

> **Math, Gently.** *A clock that stops early, and a coin flipped $n$ times.* **Part 1: the clock.** A bond can leave your sample in many ways: it defaults, matures, is called, tendered or exchanged, its issuer is taken over, or your data simply ends. Only the first is the event you are timing, and the others are not neutral. For every other exit the clock stops before the story ends, and the honest record is "still alive when I stopped watching". That is **censoring**. Tiny number: ten issuers start a study. In month 1 one defaults and, at the month's end, two others are called away by refinancings. The month-1 hazard, the chance of defaulting given you were there at the start of the month, is $1/10$. Seven issuers remain. In month 2 one of the seven defaults, a hazard of $1/7 \approx 0.143$. The chance of surviving both months is $0.9 \times 0.857 \approx 0.771$. The two that were called count fully in month 1, where they were at risk and did not default, and then leave the arithmetic: they are neither survivors past month 1 nor defaults. Counting them as survivors would flatter the curve, and dropping them from the start would throw away a month in which they did survive. (The continuous clock, $S = e^{-\int\lambda}$, is Chapter 5's and Chapter 6's, §5.1.5 and §6.6; this box needs only the monthly version.) **Part 2: the coin.** Each month's defaults are a coin flipped once for every issuer at risk, $d$ heads in $n$ flips, with the hazard $h$ as the coin's bias. The count has mean $nh$ and variance $nh(1-h)$, so the estimated hazard $d/n$ has standard error $\sqrt{h(1-h)/n}$. Tiny number: one default among seven at risk is a hazard of 14% with a standard error of $\sqrt{0.143 \times 0.857/7} \approx 0.13$, thirteen points. Small risk sets make big error bars, and chaining those coin flips month by month is the whole of Kaplan–Meier, whose full version follows the Long Scene.

### Censoring and truncation, defined

For issuer $i$, let $\tau_i$ be the event time and $C_i$ the time it leaves observation for any other reason. We observe

$$
\tilde t_i = \min(\tau_i, C_i), \qquad e_i = \mathbf{1}\{\tau_i \le C_i\} ,
$$

the observed time and the event indicator ($e_i$, because $\delta$ is a quote distance). Every estimator below assumes **non-informative censoring**: conditional on the covariates, $C_i$ is independent of $\tau_i$. In credit this assumption fails in a predictable direction. Issuers call bonds when they can refinance cheaply, which means when their credit is good, so calls remove healthy names from the risk set and leave it enriched in weak ones. A Kaplan–Meier curve on bonds subject to calls therefore *overstates* default relative to a world without calls. Mergers can go either way (§15.5). A distressed exchange is not censoring at all: it is a default (§11.4.3).

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

#### Long Scene: The Chapter 22 Cohort

*Story-now: Monday 12 October 2026, 5:40 p.m., Mags's whiteboard. The eight deals, their dates and their outcomes are real and come from company filings, court records and press reports; the months are computed from the dates shown. The desk's codings, fitted hazards and every number it produces are illustrative, and the three post-LMT bonds on the decision card are fictional.*

The desk had spent the day on Halvorsen, which had opened at 78 (Chapter 1), and by twenty to six the only person still standing was Mags, in front of the whiteboard by the window with a marker in each hand. At the top she had written CHAPTER 22, and underneath, smaller, *(the bankruptcy kind)*.

"Back in my day," she said, when Theo and Kaz drifted over, "a Chapter 22 was a company that filed for Chapter 11 twice. Now it's a company that did a liability-management deal and then filed once, which is the same thing with better lawyers. The agencies count the exchange as a default. The filing is the second one."

Theo had asked for this. The week before, he had asked the question every restructuring banker hears from a client about to sign an uptier and never gets to answer with data: *how often does the deal actually work?* Mags had said she would show him, and she had brought eight deals, every one of them public, and every one of them a company Theo knew from the other side of the table as a case study, a pitch book page or a war story told at a closing dinner.

| Company | Clock starts (first liability-management step) | How the story stood at 12 Oct 2026 | Months | On the curve |
| :--- | :--- | :--- | :---: | :--- |
| Revlon | BrandCo drop-down and roll-up, 7 May 2020 | Chapter 11, 15 Jun 2022 | 25 | filed |
| Boardriders | Uptier through an "open market purchase", Aug 2020 | Sold to Authentic; excluded lenders repaid at par, Sep 2023 | 37 | censored |
| Envision | Drop-down Apr 2022; uptier closed Aug 2022 | Chapter 11, 15 May 2023 | 9 (13 from April) | filed |
| Incora | One-day notes transaction, 28 Mar 2022 | Chapter 11, 1 Jun 2023 | 14 | filed |
| Robertshaw | Super-priority exchange, 9 May 2023 | Chapter 11, 15 Feb 2024 | 9 | filed |
| Lumen | Transaction support agreement signed 31 Oct 2023, closed 22 Mar 2024 | No filing | 31 | censored |
| Trinseo | Double dip, 8 Sep 2023 (exchange 17 Jan 2025) | Chapter 11, 26 May 2026 | 33 (16 from 2025) | filed |
| Saks Global | Non-pro-rata exchange, 8 Aug 2025 (notes issued 23 Dec 2024) | Chapter 11, 13 Jan 2026 | 5 (13 from issue) | filed |

Theo did what anyone does with a table like that. He counted. "Six of eight filed. Seventy-five percent."

"Six of eight *have filed*," Mags said. "Boardriders and Lumen aren't survivors. They're unfinished." She tapped the Boardriders row. "That one stopped being watchable when Authentic bought it and the people the uptier left behind were paid at par. That's an ending, but it's not the ending you're timing. And Lumen is still here. Thirty-one months since the deal closed, no filing, and you don't know it won't. If you call it a survivor you've told me how its story ends. If you drop it you've thrown away thirty-one months in which it didn't file, which is information you paid for."

Before anyone touched a number, she made them argue about the clocks, because, she said, that was where she had seen most of these studies go wrong. Envision's liability management came in two steps: a drop-down in April 2022 and an uptier that closed in August. Start the clock in April and Envision lasted thirteen months; start it when the excluded lenders were actually excluded and it lasted nine. Mags took August. Trinseo's first step was the September 2023 double dip and its second the January 2025 exchange; the first step started the clock, so thirty-three. Then she circled Theo's Saks row, which he had copied as thirteen from a deal list. "December 2024 is when the notes were born, not when they were restructured. The exchange was August 2025." Theo crossed out the thirteen and wrote five. Nobody said anything about it, which on this desk is how a correction is accepted.

Kaz took the marker. Kaplan–Meier, they said, does only one thing: at each month in which somebody filed, it asks what fraction of the companies still being watched filed that month, and it multiplies the survivals together. They wrote the filing months in order, five, nine, nine, fourteen, twenty-five, thirty-three, with Lumen leaving the watch at thirty-one and Boardriders at thirty-seven, and walked down the list. At month 5 eight companies were at risk and Saks filed: $7/8 = 0.875$. At month 9 seven were at risk and two filed, Envision and Robertshaw: $0.875 \times 5/7 = 0.625$. At month 14, five at risk, Incora: $0.625 \times 4/5 = 0.50$. At month 25, four at risk, Revlon: $0.50 \times 3/4 = 0.375$. At month 31 Lumen walked out of the risk set without filing, which changed nothing on the curve and everything afterwards. At month 33 only two were left, Trinseo and Boardriders, and Trinseo filed: $0.375 \times 1/2 \approx 0.19$.

"So the chance of filing within three years is eighty-one percent," Kaz said, "not seventy-five."

Theo frowned. "Doing it properly made the number worse?"

"Doing it properly made the number honest," Mags said. "Lumen got thirty-one months of credit for not filing and then left. When Trinseo went at thirty-three, there were only two companies in the room, so one filing was half the room. Your seventy-five percent counted Lumen as if it would never file. Kaplan–Meier counts it as exactly what it is: a company that hadn't filed yet when you stopped looking."

Kaz added Greenwood's band, because Ines would ask. At twelve months the curve says 37.5% filed, with a standard error of about seventeen points; at thirty-six months, 81% with about sixteen. "Eight companies," Kaz said. "The error bar is the size of the estimate's personality."

Then Kaz asked the question that, in the cast's long tradition, was wrong in a useful way. "Lumen signed a cooperation agreement. Is that a form of censoring? The lenders agreeing to be quiet?"

"It's the lenders agreeing to be loud together, in one room, so nobody else can get in," Mags said. "At Lumen the support agreement *was* the deal: signed in October 2023 and closed in March 2024, it starts the clock, at the closing, by the rule we just used for Envision, and it is not an exit from it. Censoring is when you stop being able to watch. Lumen you can watch every day; it just hasn't filed." She pointed back at Boardriders. "That one is the dangerous kind. It left because somebody bought it, and somebody bought it because it was worth buying. Companies that leave a risk set by being sold or refinanced are the healthy ones, so the companies left behind are sicker than the ones that started. That's informative censoring, and Kaplan–Meier assumes it away." Here it happened not to bite, because Boardriders left at month 37, after every filing on the board; the practice cohort below shows a case where it does.

"So censoring isn't noise," Kaz said.

"Censoring is the signal," Mags said, and wrote it at the bottom of the board, where Law 14 already was in Ines's handwriting from some earlier week.

Ines had come over during the Greenwood band, carrying the desk's re-default ledger (the one Chapter 14 builds, §14.3), and she put the eight against it. Moody's found that about 46% of 2023's distressed exchanges had already re-defaulted by April 2025, most of them in under a year (Bloomberg Law, 23 April 2025). Roe and Rotaru hand-collected 89 coercive non-pro-rata liability-management deals and found that only 22% had avoided bankruptcy or re-default two years later (Harvard Law School Bankruptcy Roundtable, 24 February 2026). And Moody's study of 1,173 borrowers with a soft credit event between 1979 and 2026 found that more than 70% of the eventual hard defaults came within 24 months (18 May 2026). The three numbers look as if they disagree and do not; they count different events in different cohorts, and §14.3 reconciles them. "Your eight are one draw from that," Ines said. "And not eight independent draws. They share a vintage, a rate cycle and a short list of law firms. It's the same disease as Theo's runway panel: count the hands, not the pictures of the hands." The 38 liability-management deals of 2024 were inside Moody's two-year window as they spoke, which is why the desk cared on a Monday evening at all.

Kaz wanted a covariate. Mags let them have one, under protest about the coding. Five of the eight deals had been non-pro-rata in the plain sense that some holders were left behind and stayed behind: Envision, Incora, Robertshaw, Trinseo and Saks. Revlon's excluded lenders had litigated and settled inside the plan, Boardriders' had been paid at par, and Lumen's term-loan deals had been open to all its term lenders, although its note deals had not been; Kaz coded those three as zero. "Revlon is a judgment call," Mags said, "and so is Lumen. Write down that they're judgment calls."

The fit was a Cox model, which Kaz explained the way they explain everything, by what cancels. At each filing month, look only at the companies still standing and ask which of them filed. Whatever the year was doing to all of them, the rate shock of 2022 and 2023, the closed high-yield market, the baseline hazard, multiplies every company's chance equally and divides out of the comparison, so the model never has to say what the baseline was. What is left is whether the company that filed tended to be the flagged one. On the desk's eight the coefficient came out at about 1.78, a hazard ratio of about six, with a standard error of 1.13: an interval running from about two-thirds to about fifty-four, and a t-statistic of 1.6 *(illustrative; the desk's coding of real dates)*.

"Six," Theo said, with the particular tone the desk now used for that number.

"Six with an interval from two-thirds to fifty-four," Ines said. "On eight companies that's not an estimate. It's a direction."

Mags had one more thing, and it was the one Theo wrote down. "And the six is this decade's six. Before 2020 the thing that predicted bankruptcy was leverage and a maturity wall. After 2020 the same covariates predict exchanges, and at a different ratio, because the company has a door it didn't used to have. Don't average two worlds into one hazard ratio. Split the baseline by era, or give the covariate an era interaction, and see if the six survives." Kaz drew the check she was asking for, the log of minus the log of each group's survival curve against the log of time, which should run in parallel if one ratio fits all months and visibly does not if it does not.

Three clock questions were left, and Mags answered them in the order the desk would get them wrong. If you insist on starting Saks's clock when its notes were issued in December 2024, then Saks did not join a cohort of post-deal companies until the exchange in August 2025; it enters the risk sets at month 8, not month 0, or you have credited it with eight months it could not have failed as a member of this cohort. On this board the delayed entry changes nothing, because the first filing after it comes at month 9, and that is luck, not design. A distressed exchange is never censoring: Trinseo's January 2025 exchange was itself a default event, and if the event you are timing is "any default" rather than "Chapter 11", Trinseo's clock stops at 16, not 33 (Law 14). And Lumen's later tenders near par, like Boardriders' par takeout, are exits of a different kind. Kaplan–Meier run on one kind of ending, with the others treated as censored, makes $1 - \hat S$ overstate that ending, because it pretends a company already taken out could still have filed later. Chapter 14 builds the cause-specific hazards and the Aalen–Johansen cumulative incidence that fix it (§14.2, Law 13), adds a cured fraction for re-default after an exchange (§14.3), and §15.5 puts the same machinery on regulatory clocks.

#### Decision point: three bonds after the deal

It is Monday 12 October 2026. The desk holds small positions in three post-LMT bonds. Corvane Health Partners did a non-pro-rata uptier that closed in March 2026, seven months ago. Ostrander Specialty Chemicals did a drop-down with a double dip in January 2026, nine months ago, and its excluded lenders have sued. Tallis Marine Holdings did a pro-rata exchange open to every holder in November 2025, eleven months ago, with a sponsor equity check alongside. Mags capped the marker. *Write three things: which one you would short, the twelve-month re-default hazard you assign it, and the one fact that would change your mind.* Before you read on, write yours.

Kaz wrote: *Corvane and Ostrander both. Cox hazard ratio 6 on a baseline of about 15% a year: 12-month hazard about 60%. Fact: a refinancing.*

Theo wrote: *Corvane. About 45%. Fact: its credit agreement.* Then he went and read it, because that is what Theo does, and came back twenty minutes later with a page flagged. Corvane's uptier had been done through the open-market-purchase exception, and the exception was still in the document, unamended, the same three words the lenders Boardriders left behind had spent three years litigating. "They can do it again," he said. "Another uptier is another distressed exchange, and that's a default. The model has no column for it."

Mags wrote: *Corvane, small. A coin flip. Fact: who owns the new money.*

Ines graded the cards against the two numbers on the board, because she did not have the future and would not pretend to. The cohort's Kaplan–Meier step at twelve months is 37.5%, plus or minus seventeen points, and the public one-year rate sits near a coin flip: Moody's 46% for the 2023 vintage, most of it inside a year, and Roe and Rotaru's finding that fewer than half of coercive non-pro-rata deals got through their first year clean. Both clocks start at the deal, not at today, which Mags pointed out nobody's card had adjusted for: Corvane had already used seven of its twelve months. Kaz's 60% had multiplied a point estimate whose interval ran to fifty-four by a baseline Kaz had invented, and had shorted two names on the strength of a t of 1.6; Ines marked it down for confidence, not direction. Mags's coin flip sat on the public rate and asked the right next question, since whoever funded the new money decides whether there is a second step. Theo's 45% sat between the cohort and the public numbers, and his fact was the best on the board, because it was the one covariate no model on the desk had: a document that still allowed the deal to be done twice. "Cox can see what you coded," Ines said. "It can't see what you didn't read." She pinned Theo's card next to the open-market-purchase clause and wrote the desk's oldest joke under it: *the most expensive three words in finance*.

### Kaplan–Meier, derived

Order the distinct event times $t_{(1)} < t_{(2)} < \cdots$. At each, let $n_j$ be the number at risk (observed and event-free just before $t_{(j)}$) and $d_j$ the number of events. Among those at risk, the events are binomial, the coin flipped $n_j$ times of the box above, and the maximum-likelihood estimate of the discrete hazard is $\hat h_j = d_j / n_j$. A censored issuer contributes to every risk set up to its censoring time and then leaves; it is never counted as a survivor beyond what was seen, and never as a default. Chaining the conditional survival probabilities gives the **Kaplan–Meier** (product-limit) estimator, the arithmetic Kaz did on Mags's whiteboard:

$$
\hat S(t) = \prod_{j:\, t_{(j)} \le t}\Big(1 - \frac{d_j}{n_j}\Big) .
\tag{7B.5}
$$

Its variance is **Greenwood's formula** (the delta-method argument is in the Full Derivation at the end of this section):

$$
\widehat{\operatorname{Var}}\big(\hat S(t)\big) \approx \hat S(t)^2 \sum_{j:\, t_{(j)} \le t} \frac{d_j}{n_j(n_j - d_j)} .
\tag{7B.6}
$$

The confidence band is built on $\ln(-\ln \hat S)$ and transformed back, so that it stays inside $[0, 1]$. The **Nelson–Aalen** estimator sums the hazards instead of multiplying the survivals, $\hat H(t) = \sum_{t_{(j)} \le t} d_j / n_j$, and $\exp(-\hat H)$ sits slightly above $\hat S$, with the two nearly equal when $d_j/n_j$ is small.

**The practice cohort, in the margin.** The desk's six fictional issuers, run through a hypothetical 36-month window *(illustrative; these are not their canonical histories, except that Quillfeather's exchange matches Chapter 14)*: a make-whole call takes out Calloway Industrial at month 9, Quillfeather Packaging and Larkspur Foam complete distressed exchanges at months 14 and 22, Halvorsen defaults at 27, Halyard Holdings is acquired at 30, and Brambleworth is alive when the window closes.

| Month | Issuer | Event? | At risk $n_j$ | $d_j$ | $\hat S$ after |
| :--- | :--- | :---: | :---: | :---: | :---: |
| 9 | Calloway | censored (call) | 6 | 0 | 1.000 |
| 14 | Quillfeather | default (DE) | 5 | 1 | 0.800 |
| 22 | Larkspur Foam | default (DE) | 4 | 1 | 0.600 |
| 27 | Halvorsen | default | 3 | 1 | 0.400 |
| 30 | Halyard | censored (acquired) | 2 | 0 | 0.400 |
| 36 | Brambleworth | censored (end) | 1 | 0 | 0.400 |

So $\widehat{\text{PD}}(36) = 60\%$. Greenwood gives $\widehat{\operatorname{Var}} = 0.16 \times \big(\tfrac{1}{20} + \tfrac{1}{12} + \tfrac{1}{6}\big) = 0.16 \times 0.30 = 0.048$, a standard error of 22 points. Nelson–Aalen gives $\hat H = 0.2 + 0.25 + 0.333 = 0.783$ and $\exp(-0.783) = 0.457$. Counting the censored issuers as survivors would have said 50%, dropping the two that left early 75%; Kaplan–Meier gives each censored issuer exactly the credit it earned. Figure 7-B.3 draws the cohort and the curve.

![Figure 7-B.3: The six-issuer practice cohort (left) and its Kaplan–Meier survival curve (right). S falls to 0.40 at 36 months, between the naive 0.50 (censored issuers counted as survivors) and 0.25 (the two issuers that left early dropped), and the 95% Greenwood log-log band runs from 0.05 to 0.75. Illustrative: the hypothetical cohort of this section, computed from equations 7B.5 and 7B.6.](assets/figures/ch07b_km_practice_cohort.png)

"A make-whole call," Kaz said. "Is that when the company phones to apologize?"

"It's when the company pays you enough to stop complaining," Mags said. "Which, in my experience, is the same thing."

Kaz's question was better than it sounded, because the make-whole is the informative-censoring problem in miniature: Calloway left because its credit was good enough to refinance, so the five issuers left behind are worse than the six who started.

> **Math, Gently.** *Why the baseline cancels: a race in the wind.* Two runners on one track, in one wind. The wind slows them both by the same proportion, whatever it is doing that day, so if all you ask is *who crosses the line first*, the wind drops out and only their relative speed matters. Cox's model treats default the same way. Every issuer still standing faces the year's baseline hazard, the wind, and a flag such as "inside a quarter of its liquidity floor" multiplies its own hazard by $e^{b}$. Tiny number: two issuers at risk, one flagged, with $b = 0.7$, so the flagged one's hazard is $e^{0.7} \approx 2.0$ times the other's. If this month's baseline is 1%, the hazards are 2% and 1%; if it is 10%, they are 20% and 10%. Either way, given that one of the two is the next to fall, the chance it is the flagged one is $2/(2+1) = 2/3$. The baseline, whatever the year is doing, has divided out, and stringing those "who fell next" probabilities together over every default is the partial likelihood, next.

### Cox proportional hazards: covariates without a baseline

Kaplan–Meier describes a cohort. To ask *which* issuers fail faster, Cox (1972) models the hazard of issuer $i$ as

$$
\lambda_i(t) = \lambda_0(t)\, \exp\!\big(b^\top z_i(t)\big),
$$

with $\lambda_0$ an arbitrary baseline and $z_i(t)$ covariates, possibly time-varying. Covariates scale the hazard proportionally, so $e^{b_k}$ is a hazard ratio. At each event time, conditioning on the fact that one issuer in the risk set $R_j$ failed and asking which one, the baseline cancels, exactly as the wind did in the box. Cox's trick is a relative-value trade: the baseline is the market beta of time, common to everyone at risk, and it drops out of the ratio. Multiplying the "which one" probabilities over event times gives the **partial likelihood**, with log and score

$$
\ell_p(b) = \sum_{j} \Big[\, b^\top z_{(j)} - \ln \sum_{k \in R_j} e^{b^\top z_k} \,\Big],
\qquad
\nabla \ell_p(b) = \sum_j \big[\, z_{(j)} - \bar z_j(b) \,\big],
\tag{7B.7}
$$

where $\bar z_j(b)$ is the risk-weighted average covariate of the risk set. The score has a desk reading: the fit is right when, on average, the issuer that defaulted looked no worse than the risk-weighted issuer standing next to it. That is the fit Kaz ran on the eight LMTs, and its interval from two-thirds to fifty-four is what a partial likelihood says when it has six events to work with.

**Cox and the logit are the same model on a grid.** Put the panel in counting-process form, one row per issuer-month, and the Cox model's monthly hazard has a complementary log-log link, which for small hazards coincides with the logit (derived below). Shumway's firm-month logit (§11.4.2) is a discrete-time Cox model with a smooth baseline, and the same $b$ appears in both. One object, two chapters.

**The USB stick, again.** Theo's runway becomes a Cox covariate: $z_i(t) = \mathbf{1}\{\text{runway}_i(t) < 13 \text{ weeks}\}$. A fitted $b = 1.1$ *(illustrative)* means a hazard ratio of $e^{1.1} \approx 3.0$: an issuer inside a quarter of its liquidity floor defaults three times as fast as one outside it, whatever the baseline year looks like. Thirteen weeks of cash flows, reborn as a hazard ratio.

The check Mags asked for on the whiteboard is a picture: plot $\ln(-\ln \hat S)$ by covariate group against $\ln t$, and proportional hazards means parallel curves; where they are not parallel, stratify the baseline by regime or interact the covariate with an era dummy (§14.1).

#### The Full Derivation: Greenwood, the partial likelihood and the cloglog link

*Greenwood (7B.6).* Write $\ln \hat S(t) = \sum_{j} \ln(1 - \hat h_j)$. By the delta method each $\ln(1 - \hat h_j)$ has variance approximately $\hat h_j / \big(n_j(1 - \hat h_j)\big) = d_j / \big(n_j(n_j - d_j)\big)$, the binomial variance $\hat h_j(1-\hat h_j)/n_j$ divided by $(1 - \hat h_j)^2$. The terms are asymptotically uncorrelated across event times, so the variance of $\ln \hat S$ is their sum, and one more application of the delta method, $\operatorname{Var}(\hat S) \approx \hat S^2 \operatorname{Var}(\ln \hat S)$, gives (7B.6).

*The partial likelihood (7B.7).* At event time $t_{(j)}$, condition on the fact that exactly one issuer in the risk set $R_j$ failed. The probability that it was issuer $i$ is

$$
\frac{\lambda_0(t_{(j)})\, e^{b^\top z_i}}{\sum_{k \in R_j} \lambda_0(t_{(j)})\, e^{b^\top z_k}} = \frac{e^{b^\top z_i}}{\sum_{k \in R_j} e^{b^\top z_k}} ,
$$

and the baseline cancels. Taking logs and summing over event times gives $\ell_p$ in (7B.7); differentiating gives the score, with $\bar z_j(b) = \sum_{k \in R_j} z_k e^{b^\top z_k} / \sum_{k \in R_j} e^{b^\top z_k}$. $\ell_p$ is concave, Newton's method converges quickly, and tied event times are handled by Breslow's approximation (all $d_j$ events share the same denominator). Once $\hat b$ is in hand, Breslow's estimator recovers the baseline, $\hat H_0(t) = \sum_{t_{(j)} \le t} d_j / \sum_{k \in R_j} e^{\hat b^\top z_k}$, and $\hat S(t \mid z) = \exp\big(-\hat H_0(t)\, e^{\hat b^\top z}\big)$.

*The cloglog link.* In counting-process form, with covariates fixed within each month, the continuous-time Cox model implies the monthly hazard

$$
h_{i,m} = 1 - \exp\!\big(-e^{\alpha_m + b^\top z_{i,m}}\big), \qquad \alpha_m = \ln\!\int_{m-1}^{m}\lambda_0(s)\,ds ,
$$

which is a complementary log-log link: $\ln\!\big(-\ln(1 - h_{i,m})\big) = \alpha_m + b^\top z_{i,m}$. When $h$ is small, $-\ln(1-h) \approx h \approx h/(1-h)$, so the cloglog and the logit coincide, with the month effects $\alpha_m$ playing the role of the logit's time-varying intercept.

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

> **Math, Gently.** *Shrinkage, or the early-season batting average.* Three weeks into a baseball season some hitter is batting .450. Nobody believes it, and nobody should: twenty at-bats are mostly luck, and the honest forecast for the rest of his season sits much closer to the league average than to .450. **Shrinkage** is that instinct with a dial on it. Blend the player's own number with the average, and set the weight on his own number by how far it can be trusted: $w = \tau^2/(\tau^2 + \sigma^2/n)$, where $\tau^2$ is how much true talent varies across players, $\sigma^2$ how noisy a single at-bat is, and $n$ the number of at-bats. Tiny number: with $\tau^2 = 1$, $\sigma^2 = 4$ and $n = 4$, $w = 1/(1 + 4/4) = 0.5$, half his own record and half the league's. Quadruple the at-bats and $w$ rises to 0.8. Two lessons come out of the formula and survive every generalization of it: shrink hard when your own estimate is noisy, and shrink little when the thing you are shrinking toward is wrong for this player. A covariance matrix is eighty thousand batting averages at once, and the general idea is next.

Shrinkage trades a little bias for a lot of variance. For means it is old: estimate a counterparty's markout with $n_i$ fills as a weighted average of its own mean and the population's, with weight $w_i = \tau^2/(\tau^2 + \sigma^2/n_i)$ on its own data (the normal–normal posterior; §3.3.4 uses exactly this). James and Stein (1961) proved the uncomfortable general version: for three or more means, shrinking all of them toward a common point beats estimating each separately, in total squared error, *whatever the true means are*. Factor weights "shrunk toward equal" (§9.7) are the same move applied to a portfolio.

### Ledoit–Wolf: noise over noise plus misspecification

Shrink the sample matrix toward a structured target $\Sigma^{\text{tgt}}$, $\Sigma(\delta) = \delta\,\Sigma^{\text{tgt}} + (1-\delta)\,\hat\Sigma$, and choose $\delta$ to minimize the expected squared (Frobenius) distance between the blend and the truth. The answer, derived at the end of this section, is the batting-average weight for a whole matrix:

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

After stripping the known factors you are left with a $T \times N$ panel $\tilde\epsilon$ of DTS-scaled residuals (§8.8). The question is whether anything common is still in it, which is the question the RV thread keeps asking: a pair's "idio" is idio only relative to the factors you removed, and a residual panel with a common component in it is a book of pairs that are secretly one trade (Chapter 8 §8.8 runs that test on the Pair Book).

> **Math, Gently.** *What an eigenvalue is, and why noise has an edge.* **Part 1: a stretched ball.** Plot two bonds' daily returns against each other and the cloud is not round. It is an ellipse, stretched along the direction in which the two tend to move together. A covariance or correlation matrix is the recipe for that stretch: its **eigenvectors** are the ellipse's axes and its **eigenvalues** are how long each axis is, which is the variance of a portfolio pointing along it. Tiny number: two bonds with unit variance and correlation 0.6. One axis points along "both together", $(1, 1)/\sqrt2$, with eigenvalue $1 + 0.6 = 1.6$; the other points along "one against the other", $(1, -1)/\sqrt2$, with eigenvalue $1 - 0.6 = 0.4$. The long axis is the market. The short one is the pair, long one bond and short the other, which is why a pair's variance is so much smaller than either leg's, and why an axis whose length is estimated at zero is a portfolio an optimizer believes is riskless: the 400-bond matrix of the desk framing is a ball squashed flat along 281 such axes. **Part 2: noise has an edge.** Pure noise also makes a stretched ball, because a finite sample always finds some direction that happened to move more than the others. Marchenko and Pastur worked out how far noise alone can stretch it: for $N$ unrelated series observed $T$ times, with $q = N/T$, the longest noise axis is about $(1 + \sqrt q)^2$ times the average. Tiny number: 100 bonds and 400 days give $q = 0.25$ and an edge of $(1 + 0.5)^2 = 2.25$, so a top eigenvalue of 2.0 on that panel is nothing at all. The full version is next.

The first principal component of the residual panel is the unit vector $v_1$ along the longest axis of its covariance, $\hat\Sigma_{\tilde\epsilon}\, v_1 = \omega_1 v_1$; the variance it captures is the eigenvalue $\omega_1$, and the $k$-th component is the $k$-th eigenvector, orthogonal to the rest (the Lagrangian is in the Full Derivation below). The component's time series is $g_t = \tilde\epsilon_t v_1$, and removing it leaves $\tilde\epsilon - g\,v_1^\top$.

The question PCA does not answer by itself is whether $\omega_1$ is signal. Random matrix theory supplies the null. If the panel were pure noise with unit variance and aspect ratio $q = N/T$, the nonzero eigenvalues of its sample correlation matrix would fill, as $N, T \to \infty$, the Marchenko–Pastur interval

$$
\big[(1 - \sqrt q)^2,\; (1 + \sqrt q)^2\big] .
$$

For 400 bonds and 120 months, $q = 3.33$ and the upper edge is $(1 + 1.826)^2 \approx 8.0$: pure noise produces eigenvalues eight times the average. On five years of daily data, $q = 400/1{,}260 \approx 0.32$ and the edge falls to about 2.4. A principal component is noise until proven larger than Marchenko–Pastur. Clipping the eigenvalues below the edge to their average (Laloux et al. 1999) is one more shrinkage estimator. Figure 7-B.4 shows the edge moving with the sampling frequency.

![Figure 7-B.4: Eigenvalues of a 400-bond correlation matrix built from noise plus a market factor and a weak sector factor. With five years of daily data (q = 0.32) noise stays below 2.4 and both factors stand out. With ten years of monthly data (q = 3.33) noise reaches 8.0, only the market factor clears it, and the sector factor is lost in the bulk. Illustrative: simulated with a fixed seed; the line is the Marchenko–Pastur density, and each dot is a single eigenvalue above the edge.](assets/figures/ch07b_mp_edge.png)

"So we just assume Gaussian," Kaz said, and then, a beat later, regretted it. The Marchenko–Pastur edge assumes thin-tailed, serially independent noise; fat tails and stale marks widen the noise band. The edge is a floor for skepticism, not a theorem about your data. Two more traps: the sign of an eigenvector is arbitrary, so align each window's loadings with the previous window's before you chart them; and when two eigenvalues are close, their eigenvectors rotate freely between windows, so the "second factor" may be a different factor every month.

A systematic manager that sells factor analytics to other investors draws the same line in a different place, and Ines, who had listened to the episode on a flight, thought the contrast was the point.

> **View From Another Seat.** *The systematic manager's factor lens (Venn by Two Sigma, from a public podcast).* On *Flirting with Models* (S7E20, 2 September 2025), Chris Carrano of Venn by Two Sigma discussed the thinking behind Venn's factor lens: eighteen factors, orthogonalized so that each one's exposure means something on its own; a fit that, per the episode's description, blends Lasso with ordinary least squares to keep the regression from chasing noise; and a stated preference for factors a client can interpret over a larger, more complex set (paraphrased from the episode notes and Venn's own published account of the lens). From that seat the lens has to describe whatever portfolios clients bring to it, so a small, stable set of factors is the product and Lasso, itself a shrinkage estimator, is what keeps eighteen from overfitting. The desk's credit model makes the opposite trade: five factors, one asset class, and a market loading it never estimates because DTS supplies it (Law 3). Both seats are obeying the same edge. A residual panel at daily frequency, where $q$ is near 0.3 and the noise edge sits near 2.4, can afford to look for more structure than a monthly panel, where the edge is 8.0 and only the market clears it, provided the daily marks are prices and not stale copies of yesterday's, which in credit is a large proviso.

#### The Full Derivation: Ledoit–Wolf and the first principal component

*Ledoit–Wolf (7B.8).* Write $\Sigma(\delta) - \Sigma = (\hat\Sigma - \Sigma) - \delta(\hat\Sigma - \Sigma^{\text{tgt}})$. The expected squared Frobenius error $\mathbb{E}\lVert \Sigma(\delta) - \Sigma \rVert_F^2$ is quadratic in $\delta$, and its minimizer is

$$
\delta^{*} = \frac{\mathbb{E}\big\langle \hat\Sigma - \Sigma,\; \hat\Sigma - \Sigma^{\text{tgt}} \big\rangle}{\mathbb{E}\lVert \hat\Sigma - \Sigma^{\text{tgt}} \rVert_F^2} .
$$

If the target is fixed and $\hat\Sigma$ is unbiased, the cross terms vanish: the numerator becomes $\mathbb{E}\lVert \hat\Sigma - \Sigma \rVert_F^2 = \sum_{i,j}\operatorname{Var}(\hat\Sigma_{ij})$ and the denominator that plus $\lVert \Sigma - \Sigma^{\text{tgt}} \rVert_F^2$, which is (7B.8).

*The first principal component.* Maximize the captured variance $v^\top \hat\Sigma_{\tilde\epsilon}\, v$ subject to $v^\top v = 1$. The Lagrangian $v^\top\hat\Sigma v - \omega(v^\top v - 1)$ has first-order condition

$$
\max_{v}\; v^\top \hat\Sigma_{\tilde\epsilon}\, v \quad \text{s.t.} \quad v^\top v = 1
\quad\Longrightarrow\quad
\hat\Sigma_{\tilde\epsilon}\, v = \omega\, v ,
$$

so the optimum is an eigenvector and the variance captured, $v^\top \hat\Sigma v = \omega$, is its eigenvalue; the largest eigenvalue wins. Repeating the problem orthogonal to $v_1$ gives the second component, and so on.

*Used in:* §3.3.4 (shrunk counterparty scores), §8.4 (DTS scaling), §8.6 (ridge hedges), §8.8 (removing the common residual factor), §9.7 (weights shrunk toward equal), §10.3 (EWMA volatility), §12.5 (EWMA, shrinkage and desmoothing), §19.5 (residual covariance for 150 stale bonds), §28.2 (breadth from the residual correlation).


## 7-B.6 The Statistical Bootstrap: Block, Stationary and Cluster

### The plug-in principle

> **Math, Gently.** *Ask the sample about itself.* Chapter 7's box in §7.6 said what a bootstrap does; this one says why it is allowed to. You cannot re-run history to see how much your average would wobble, so you do the next best thing: treat the sample you have as if it were the whole world, and draw new samples from it. Write each observation on a slip, put the slips in a hat, draw one, write it down, put it back, and repeat until you have as many draws as you had slips. Tiny number: five markouts, in basis points, of $-2, -1, 0, 1$ and $7$, with a plug-in mean of 1. One resample draws $-2, -1, 0, 0, 1$ and never sees the 7: its mean is $-0.4$. Another draws the 7 twice, $7, 7, 1, 0, -1$: mean 2.8. Do it a thousand times and the spread of those means is your error bar. Notice what drives the spread: about a third of all resamples, $(4/5)^5 \approx 0.33$, miss the 7 entirely, so the error bar is mostly a statement about one big markout. And notice what the hat cannot do. It holds only the slips you put in it, so the bootstrap never draws a markout worse than your worst. The plug-in principle in full, and the ways credit data break it, is next.

You want the sampling distribution of a statistic $\hat\theta$ (a Sharpe ratio, an AUC, a default rate) and you have one sample. Efron's (1979) idea is to treat the empirical distribution as if it were the population: draw $n$ observations with replacement, recompute $\hat\theta^{*}$, repeat $B$ times, and use the spread of $\hat\theta^{*} - \hat\theta$ as a stand-in for the spread of $\hat\theta - \theta$. Percentile intervals are the simplest. Studentized (bootstrap-$t$) intervals, which resample a pivot $(\hat\theta^{*} - \hat\theta)/\widehat{\text{se}}^{*}$, are more accurate, and the extra computation is cheap next to a wrong answer.

### Why the i.i.d. bootstrap lies on credit data

Resampling single observations destroys dependence, and credit data are made of dependence. For an AR(1) series with autocorrelation $\rho$, the variance of the sample mean is approximately $\frac{\sigma^2}{T}\cdot\frac{1+\rho}{1-\rho}$; the i.i.d. bootstrap reports $\sigma^2/T$. Stale marks with $\rho = 0.3$ hide a factor of 1.86 in variance. Across issuers it is worse, because correlated defaults make one cohort close to one observation.

> **[SOURCE EXTRACTION]** *Bohn_Stein_Active_Credit_Portfolio_Management p.443:* "Thus, about half of the time, even with infinite data, we would mistake the default probability for 20 bps when it was actually 200 bps."
>
> **Annotation.** Bohn and Stein's setting is a portfolio with uniform asset correlation 0.25 and a true PD of 2%, tested against a believed PD of 20 bps, and "mistake" means the test fails to reject. At correlation 0.25 and a PD of 20 bps, the realized default rate of an infinitely large portfolio stays below about 88 bps in 95% of draws (the source prints 87 bps), so any realized rate under that bound leaves the 20 bps hypothesis standing. Because defaults share a factor, the realized default rate of even an infinitely large portfolio is one draw from the distribution of the systematic factor, and that draw is often benign: the median draw for a 2% PD is 0.89%, and the realized rate falls below the 88 bps bound about half of the time (49.8% in Vasicek's limiting distribution). It is the test that is fooled, not the realized rate: a 2% portfolio shows 20 bps or less only about 19% of the time. At 90% confidence the bound drops to 49 bps and the test still passes 20 bps 36% of the time, the source's "more than a third." Their next page describes the Hanson–Schuermann bootstrap, which resamples *firms*, and warns that multiyear bounds are hard "due to the dependence induced in the sample from year 1 to year 2" (p.444). The 2026 desk takes both warnings literally. Resample *years* (whole cross-sections), in blocks long enough to keep a cycle's persistence, never firms one at a time. And accept the limit no resampling scheme removes: twenty years of data hold two or three credit cycles, and the bootstrap never shows you a crisis you did not have. It only reshuffles the ones you did.

### Block and stationary bootstraps

The **moving block bootstrap** (Künsch 1989) resamples blocks of $\ell$ consecutive observations and concatenates them, so dependence within a block survives. The circular version wraps the series end to start so every observation is equally likely to be drawn. The **stationary bootstrap** (Politis and Romano 1994) draws block lengths from a geometric distribution with mean $1/p$: at each step, with probability $p$ start a new block at a random date, otherwise take the next date (circularly). The resampled series is itself stationary, which fixed-length blocks are not. In theory the block length grows like $T^{1/3}$, and the Politis–White (2004) rule picks it automatically; for overlapping returns, any block shorter than the overlap $h$ cuts through the very dependence the blocks exist to keep.

### Panels: resample the unit that is independent

Kaz spent a Tuesday that month finding out what that heading costs, in compute and in pride. The panel was Theo's runway regression from the cold open, the one §7-B.9 re-audits row by row. The first run resampled bond-months one row at a time. It took four minutes and returned an interval so tight it implied a t of 5.9 *(illustrative, as are the next three numbers)*: the classical answer in a bootstrap's clothes, because drawing rows one at a time destroys exactly the dependence the cold open was about. The second run resampled dates with the cross-section intact, blocks of months with every bond in a drawn month carried along, so each month's shared market shock stayed in one piece. It took forty minutes, most of them in a queue behind the risk team's overnight batch, and the interval widened to a t of 3.8. The third resampled issuers with replacement, each with all its bonds and all its months, the cluster (pairs) bootstrap that is the resampling twin of (7B.2), and came back at 2.5, within rounding of the issuer-clustered 2.4. Three intervals, one coefficient; the only thing that changed was what Kaz agreed to count as a hand. Then Kaz kept the promise Ines had underlined on the replay whiteboard and ran the wild cluster bootstrap on the Ford dummy: keep $X$ fixed, multiply each issuer's whole residual vector by an independent random sign, rebuild $y^{*} = X\hat b_0 + u^{*}$ under the null, refit, and repeat (Cameron, Gelbach and Miller 2008). It is the tool for a regression with a dozen clusters, a cross-section of sectors, say. With one treated cluster it returned a p-value of about one half, which is the method's polite way of agreeing with Theo. Comparing two strategies' Sharpe ratios is the same logic with a time series: a studentized circular block bootstrap of the difference (Ledoit and Wolf 2008), deflated for the number of trials, which §7.8 runs (Law 12).

*Used in:* §7.6 (the sequential bootstrap for bagging over overlapping labels), §7.8 (Sharpe-ratio inference), §11.5 (confidence bands on AUC and hit rates), §14.2 (cohort uncertainty in cumulative incidence), §28.2 and §28.6 (breadth and drawdown confidence); collision with curve bootstrapping (§6.8) recorded in Appendix A §A.3.


## 7-B.7 Tree Ensembles in One Section

**A tree** partitions feature space by recursive binary splits. At each node it picks the feature $j$ and threshold $c$ that most reduce impurity (squared error for a return, Gini $\sum_k p_k(1 - p_k)$ or entropy for a default flag) and predicts the leaf average. Trees find thresholds and interactions a logit cannot ("distance to default below 1.5 *and* runway under 13 weeks"), and they are invariant to monotone transformations of features, so a leverage ratio needs no winsorizing. A single deep tree is also a high-variance estimator that memorizes its training set.

**Bagging** averages $B$ trees grown on bootstrap samples. If each tree's prediction has variance $\sigma^2$ and any two have correlation $\rho$, the average has variance

$$
\operatorname{Var}\Big(\frac{1}{B}\sum_{b=1}^{B} f_b\Big) = \frac{1}{B^2}\big[B\sigma^2 + B(B-1)\rho\sigma^2\big] = \rho\,\sigma^2 + \frac{1 - \rho}{B}\,\sigma^2 ,
$$

which falls to $\rho\sigma^2$, not zero, as $B \to \infty$. This is Law 2 again, inside the model: forty-seven correlated trees are about one tree. Random forests (Breiman 2001) lower $\rho$ by letting each split consider only a random subset of features.

**Boosting** (Friedman 2001) builds the model in stages, $F_m(x) = F_{m-1}(x) + \nu\, h_m(x)$, where each small tree $h_m$ is fitted to the negative gradient of the loss at $F_{m-1}$ and $\nu \in [0.01, 0.1]$ is a learning rate. With log loss and $F$ in log-odds, the negative gradient is $y_i - p_i$, exactly the score contribution of §7-B.3. Boosting on log loss is a logistic regression that grows its own features. XGBoost (Chen and Guestrin 2016) adds second-order steps and regularization.

**What credit adds to the recipe.** The first boosted default model the desk built learned Halvorsen. Kaz had cross-validated it with ordinary random folds, the out-of-fold AUC came back at 0.93 *(illustrative)*, and the feature-importance chart had coupon and maturity at the top, which made no economic sense until Theo looked at it. "A 7.25% coupon maturing in 2029 isn't a feature," he said. "It's a name." Halvorsen's siblings sat on both sides of every fold, so the trees had learned to recognize the issuer from its coupon-and-maturity pair and to remember how its story ended, which is the economics of nothing. Refit with purged, embargoed, parent-grouped folds (§7.7), the AUC fell to 0.78. Then Theo found a leaf in which the predicted PD fell as leverage rose, a quirk of six issuers that had levered up for acquisitions in a good year. "The credit agreement doesn't let leverage be good for you," he said, and Kaz added monotone constraints where the economics is not in doubt: PD non-decreasing in leverage, non-increasing in distance to default and in runway. The last fix was the one §7-B.3 predicts. Boosted log-odds are overconfident in the tails, so the outputs were recalibrated on a holdout before anyone called them probabilities.

Two more habits come from the same model's later life. Trees do not extrapolate: a tree has never heard of anything worse than the worst thing it has seen, so an issuer at 12× leverage scores like the most-levered leaf in training. And the feature ranking that survived was permutation importance computed on held-out purged folds, not in-sample impurity, which favors continuous, high-cardinality features, and coupons and maturities are exactly that. Measured honestly, the gain is real where the signal is nonlinear: on walk-forward bankruptcy prediction, trees lift AUC well above a linear logit using distance to default alone (§11.4.4). Where events are few, as with roughly a hundred LMTs, a logit with a prior still wins (§13.8).

*Used in:* §7.0 and §7.5 (the secondary model in meta-labeling), §7.6 (the sequential bootstrap), §7.7 (grouped CV), §11.4.4 (the bankruptcy horse race), §14.1 (PD models trained on the wrong labels), §26.7 (an agent's trials are your trials).


## 7-B.8 Monte Carlo as a Method: Standard Errors, Variance Reduction and the Brownian Bridge

### The estimator and its error

To compute $\theta = \mathbb{E}[g(X)]$, under a stated measure, draw $X_1, \ldots, X_n$ and average: $\hat\theta_n = \frac{1}{n}\sum_i g(X_i)$. The central limit theorem gives $\sqrt n(\hat\theta_n - \theta) \to \mathcal{N}(0, \sigma_g^2)$, so the standard error is $\hat s_g/\sqrt n$ in any dimension. That is Monte Carlo's virtue and its tax: halving the error costs four times the paths.

> **Math, Gently.** *The square-root tax, and the mirror.* **Part 1: the tax.** A Monte Carlo estimate is an average of simulated outcomes, so its wobble is the outcome's wobble divided by $\sqrt n$, and accuracy is bought at a square-root price. Tiny number: a probability near 0.23 estimated from 10,000 paths has a standard error of $\sqrt{0.23 \times 0.77/10{,}000} \approx 0.0042$, about 0.42 percentage points. Halving that to 0.21 points takes not twice the paths but four times, 40,000; a tenth of it takes a hundred times. The tax is the same in one dimension or a thousand, which is Monte Carlo's virtue, and it never goes away, which is its cost. **Part 2: the mirror.** The second building block is about paths that cross a line between the moments you look at them. Picture a coin-flip walk, one step up or down per flip, and a line three steps above the start. Take any path that touches the line and ends at +1. Reflect everything it does after its first touch in the line, and you get a twin that ends at +5. The pairing is one-for-one, so paths that touch the line and end below it are exactly as common as paths that end the same distance above it. That is the **reflection principle** (Chapter 6's box in §6.5.2 uses it over a whole horizon; the random walk itself is Chapter 5's and Chapter 6's, §5.2.3 and §6.1.1). Applied to one time step whose two ends you know, it says how likely the path was to dip to a barrier in between. Tiny number: a step that starts 0.3 above the barrier and ends 0.1 above it, with variance 0.0625 over the step, touched the barrier in between with probability $\exp(-2 \times 0.3 \times 0.1/0.0625) = e^{-0.96} \approx 0.38$. The full version is (7B.9), at the end of this section.

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

#### Quant-Shop Life: Thursday Model Review

*A fictional composite: a systematic credit asset manager, its people, its engine, its tickets and its numbers are invented, and no real firm is described. The public order cited at the end is real.*

The model risk committee of a systematic credit manager meets on Thursdays at ten, in a room with a screen that takes four minutes to find the laptop. The fourth item on the agenda, after a vendor contract renewal and the quarterly inventory attestation, was a question from the committee's chair about the overnight tail report. The probability that the firm's high-yield sleeve lost more than its risk budget over a year had printed 23.1% on Tuesday and 23.4% on Wednesday *(illustrative)*. Nothing in the portfolio had changed overnight. Why had the number?

Jonah Feld, eighteen months out of a master's program and the engine's owner since spring, said he would come back before lunch, and spent the next two hours finding out. The difference itself took ten minutes: the engine ran 10,000 paths, so a probability near 23% carried a standard error of about 0.42 points, and 0.3 points was less than one of them. The number had moved by noise. The question was why the noise was visible at all, because until March the job had used a fixed seed and printed the same number every night the inputs did not change. The commit log answered it. In March a refactor had changed the nightly seed from a constant to the run date, so that consecutive nights would not reuse draws. The engine's regression test compared a simulated probability on 200,000 paths with its closed form, using a tolerance of 0.001 that someone had set years earlier after watching it pass on the fixed seed. That is about one standard error, and with a fresh seed every night it fails about one night in three. The same commit widened it to a flat 0.02, with the message *widen tol until green*. The test had been green ever since, and it would now pass a number wrong by two points; the four-standard-error rule of the subsection above would have set it near 0.004. Then Jonah found the second stream. The recovery draws came from a generator seeded as `seed + 1`, which had been harmless with a constant seed and was not with a date: Tuesday's recovery stream was Wednesday's default stream, number for number. In the backlog there was a ticket, opened eighteen months earlier by a contractor who had since left, titled *derive streams with SeedSequence.spawn, not seed arithmetic*. It had been triaged low and had aged ever since.

At 11:55 Jonah told the committee that the move was noise, that the noise was now visible because of an unlogged change, and that the change had come with a weakened test and a stream collision. The chair asked for two things: the Monte Carlo standard error printed next to every simulated number in the report, and the March commit written up as a model change under the firm's change-control policy, which follows the supervisory guidance that "all changes are logged and can be audited" (Federal Reserve and OCC, SR 11-7, 2011, p.12). The fix was eleven lines. Validating it took three weeks. The public record has a larger version of the same aging ticket: in its January 2025 order against Two Sigma, the SEC said employees had identified model vulnerabilities in or before March 2019 that the firm did not act on until August 2023 (Chapter 1-B tells it). Ticket age is a risk number. The next subsection is what Jonah's eleven lines did.

### Seeds, streams and common random numbers

Jonah's eleven lines seeded one `numpy.random.Generator` per experiment and derived its independent streams with `SeedSequence.spawn`, instead of by adding 1 to a seed, which is the whole of the fix and the convention every listing in this book follows. The same discipline buys something more when two numbers are compared, two strategies, two parameter values, or a bumped and an unbumped price: **common random numbers**, the same draws for both. Since $\operatorname{Var}(\hat\theta_A - \hat\theta_B) = \operatorname{Var}\hat\theta_A + \operatorname{Var}\hat\theta_B - 2\operatorname{Cov}(\hat\theta_A, \hat\theta_B)$, positively correlated estimates make the difference far more precise than either level. A finite-difference Greek without common random numbers is mostly noise.

### Variance reduction: three tools that earn their keep

Kaz found out which of the three earns most on a Black–Cox bond, the barrier model of §6.5, by pricing it on one seed with and without help. Plain simulation on 10,000 paths gave the price with a standard error of about nine cents per 100 of face *(illustrative, as are the reductions below)*. The cheapest trick, **antithetic variates**, pairs each normal draw $Z$ with $-Z$. The pair average has variance $\frac{\sigma_g^2}{2}(1 + \rho)$ with $\rho = \operatorname{Corr}(g(Z), g(-Z))$, which is negative for any monotone $g$, so monotone payoffs (most bond and loss payoffs) get cheaper; here the error fell by about a third. A **control variate** did far better, because the model next door has an answer in closed form: the Merton bond, the same firm with default checked only at maturity, simulated on the same paths. If $Y$ has known mean $\mu_Y$, use $\hat\theta_c = \hat\theta - c(\bar Y - \mu_Y)$; the optimal $c^{*} = \operatorname{Cov}(g, Y)/\operatorname{Var}(Y)$ cuts the variance by the factor $1 - \rho_{gY}^2$. The two bonds' simulated payoffs were correlated about 0.95, so the variance fell to $1 - 0.95^2 \approx 0.10$ of what it was and the standard error to about a third, as if Kaz had run ten times the paths for free. (A portfolio loss simulation uses its analytic expected loss the same way.) The third tool is for tails. **Importance sampling** draws from $q$ instead of $p$ and reweights by the likelihood ratio: $\hat\theta = \frac{1}{n}\sum_i g(X_i)\,p(X_i)/q(X_i)$. In a one-factor threshold model, shift the systematic factor to $Z \sim \mathcal{N}(\mu, 1)$ with $\mu < 0$ so that bad states are sampled often, and weight each path by $p(z)/q(z) = \exp(-\mu z + \mu^2/2)$. This is the technique behind Bolder's 3,000-path estimator above, and the one to reach for when the number on the page is a 99.9% quantile.

### Discretisation, and the bias that first passage adds

Simulate log-normal quantities exactly in logs, with the drift carrying Itô's $-\tfrac12\sigma^2$ correction (Chapter 6's volatility tax, §6.1.1), so that the grid introduces no error at the grid points. Between the grid points is another matter. A path-dependent payoff that depends on whether a barrier was ever touched (Black–Cox default, a covenant trip, a drawdown stop) misses every crossing that happens between grid points and comes back, and this bias shrinks only like $\sqrt{\Delta t}$. Broadie, Glasserman and Kou (1997) show that a discretely monitored barrier behaves like a continuous one shifted away by a factor $e^{0.5826\,\sigma\sqrt{\Delta t}}$. For a driftless log asset 0.30 above its barrier with $\sigma_V = 0.25$, the one-year continuous hitting probability is $2\Phi(-1.2) \approx 23.0\%$; monitoring monthly behaves like a barrier at distance $0.30 + 0.5826 \times 0.25 \times \sqrt{1/12} \approx 0.342$, or $2\Phi(-1.37) \approx 17.1\%$ *(approx., via the continuity correction)*. That shift is a first-order approximation, and here it runs half a point low: the exact probability for twelve monthly dates, by numerical integration and confirmed by simulation, is 17.6%. Use 17.6% as the monthly-grid number; it is the one Figure 7-B.5 (below) and the acceptance test of §7-B.10 report, both by simulation. The monthly grid misses 5.4 points of the exact 23.0%, about a quarter of the defaults.

### The Brownian-bridge correction

The exact fix needs one fact about Brownian motion, the mirror of the box at the top of this section. Over one step of length $\Delta t$, a log asset with volatility $\sigma_V$ that starts at $x_i$ and ends at $x_{i+1}$, both above a log barrier $b$, touched the barrier in between with probability

$$
p_i = \mathbb{P}\Big(\min_{[t_i, t_{i+1}]} X \le b \;\Big|\; x_i, x_{i+1}\Big) = \exp\!\Big(-\frac{2\,(x_i - b)\,(x_{i+1} - b)}{\sigma_V^2\,\Delta t}\Big) ,
\tag{7B.9}
$$

the formula §6.5.4 uses, and it holds for any constant drift (both facts are derived below). The corrected algorithm simulates exact log endpoints on a coarse grid, records a hit if an endpoint is at or below $b$, and otherwise records a hit with probability $p_i$ (Beaglehole, Dybvig and Zhou 1997; Glasserman 2004). Better still, do not flip the coin: carry the path's survival probability $\prod_i (1 - p_i)$ as its weight. The mean is the same and the variance is lower, because you integrated the coin out analytically. Figure 7-B.5 sets the grid, the bridge and the exact answer side by side.

![Figure 7-B.5: Probability that a driftless log asset 0.30 above its barrier, with volatility 0.25, touches it within one year. Checking only on a grid understates the exact 23.0% by 5.4 points at monthly dates and closes the gap only like the square root of the step, while the Brownian-bridge crossing probability (7B.9) recovers 23.0% on any grid, even a single annual step. Illustrative: Monte Carlo, 2,000,000 paths per point, from the model of §7-B.8.](assets/figures/ch07b_first_passage_bridge.png)

#### The Full Derivation: the Brownian-bridge crossing probability

For a standard Brownian motion $W$ started at 0 and a level $a > 0$, the reflection principle says that a path that touches $a$ and ends at $y \le a$ is matched one-for-one by its reflection after the touch, which ends at $2a - y$. Hence the joint density of "touched $a$" and "$W_t \in dy$" is $\phi_t(2a - y)$, where $\phi_t$ is the $\mathcal{N}(0, t)$ density, and dividing by the density of $W_t$ at $y$ gives

$$
\mathbb{P}\Big(\max_{s \le t} W_s \ge a \;\Big|\; W_t = y\Big) = \frac{\phi_t(2a - y)}{\phi_t(y)} = \exp\!\Big(-\frac{(2a-y)^2 - y^2}{2t}\Big) = \exp\!\Big(-\frac{2a(a - y)}{t}\Big).
$$

Now take the log asset $X$ over one step of length $\Delta t$ with volatility $\sigma_V$, starting at $x_i$ and ending at $x_{i+1}$, both above a log barrier $b$. Reflect so that "down to $b$" becomes "up to $a$": the distance to the barrier is $a = x_i - b$, the displacement toward it is $y = x_i - x_{i+1}$, so $a - y = x_{i+1} - b$, and the variance is $\sigma_V^2\Delta t$. Substituting gives (7B.9). It holds for any constant drift, because the Girsanov density that adds a drift depends on the path only through its endpoint, so conditioning on the endpoint cancels it.

*Used in:* §1.5 (the one-factor threshold simulation), §2.3.2 (best-of-$n$ RFQ simulation), §5.9 (the mixture lab), §6.5.4 and §6.11 (Black–Cox with the bridge), §14.7 (the regime-switching engine), §15.2 (the change-of-control put), §16.3 and §16.5 (backstop and claims checks), §23.2 (the CreditGrades check), §28.4 and §28.6 (Kelly with JTD, drawdown barriers); every seeded `assert` in the book.


## 7-B.9 Case Study: Theo's Runway, Re-Audited

Ines's card from the cold open had two questions on it, how many independent hands were under the 2.1 and how far it moved when somebody else made the choices, and Theo answered it the slow way. He re-ran the runway regression himself, one row of the table a day, in the gaps of a week that had other plans for him. All numbers are *illustrative*; the sequence is the lesson.

| Treatment | Unit of independence | t-statistic |
| :--- | :--- | :---: |
| Classical OLS (what ROBO did) | bond-month | 6.1 |
| White (HC1) | bond-month, unequal variances | 5.6 |
| Clustered by ultimate parent | issuer (206) | 2.4 |
| Two-way: parent and month | issuer and month | 2.1 |
| Fama–MacBeth, Newey–West on slopes ($L = 4$) | month (36) | 2.2 |
| Wild cluster bootstrap, p-value | issuer | 0.04 |

Monday was the first two rows, which took twenty minutes and taught him one thing. White's estimator, the meat that lets every row have its own variance, moved the t from 6.1 to 5.6. The CCC bonds really were noisier than the BBs, but noise of different sizes had never been the problem. The problem was eleven bonds telling one story, and a diagonal meat cannot see that by construction.

Tuesday was the third row, and it took all day, none of it on statistics. Clustering by ultimate parent needs a parent for every bond, and the desk's security master had three Halvorsen entities (the holding company, an operating subsidiary and a finance vehicle that existed to issue one bond in 2021), two issuers that had merged in 2024 and were still listed separately, and a CUSIP whose issuer field read *TBD*. Theo fixed the mappings by hand, with the credit agreements open in another window, which was the first time in three weeks that his old job had been the fastest way to do his new one. The t came back at 2.4, as Kaz's had. The Post-it that said *parent, not CUSIP* stayed where it was.

Wednesday was two-way clustering, 2.1, and one line in the log he nearly reported as a bug: `creditstats.py` had clipped a negative eigenvalue of the two-way covariance to zero, as §7-B.1 says it will, because the difference of two positive semidefinite matrices need not be one. Thursday was Fama–MacBeth, 36 monthly cross-sectional slopes with Newey–West at four lags: 2.2. Theo liked that row best, because it was the one he could explain to a credit committee: each month's slope is the return on a portfolio long short-runway issuers and short long-runway ones, and 36 months is 36 observations, however many bonds are inside each. Friday morning he ran the wild cluster bootstrap by issuer, which put the p-value at 0.04. Five methods, five ways of deciding what a hand is, and every honest one of them landed between 2 and 2.5.

Then Kaz came over with the second error bar, and the argument that followed took most of Friday's lunch. Kaz had built 24 defensible specifications, every combination of runway capped at 13 or 26 weeks, a one- or two-month knowledge lag on lender reporting, IDO or plain excess returns, and ex-ante trimming at three thresholds, and the coefficient ranged from 0.4 to 1.9 bp per week of runway, against a clustered standard error of 0.5.

"Pick one," Kaz said. "Thirteen-week cap, two-month lag, IDO, trim at one percent. That's the clean one. That's *the* result."

"Why is it the clean one?"

"Because it's the one I'd have built first."

"That's the problem," Theo said. "It's the one you'd have built first. The printout Ines left on my keyboard is about exactly that." The paper on his desk had done the same exercise to every published bond factor, and its point, which the Trend Watch in §7-B.2 puts in numbers, was that the spread of an estimate across the choices a careful researcher could defend is often as large as its standard error. Theo's was: the non-standard error, the spread across the 24, was about the size of the clustered standard error, which by that measure is normal for credit and still uncomfortable. Kaz conceded by writing both numbers on the summary, the second in a slightly smaller font. The Cox fit of §7-B.4 told the same story on a different clock, a hazard ratio near 3 for issuers inside thirteen weeks.

"So it's real," Theo said, "but it's one real thing, not six."

"It's a hand worth playing at a quarter of the size you wanted," Ines said. "Which is usually what a real edge looks like."

Ines's quarter has a cousin on the platforms, where the size of a bet is set by somebody whose job is to distrust the t-statistic.

> **View From Another Seat.** *The pod's risk desk (a generic seat; the arithmetic is illustrative).* On a multi-manager platform Theo's table would not be research; it would be an allocation. Platforms keep their books market- and factor-neutral and put the leverage on what is left. Rich Falk-Wallace, formerly of Citadel, put it in one line on *Odd Lots* (25 July 2024): "what you're levering is just that residual term." Giuseppe Paleologo, who has worked in risk at Citadel and Millennium, described the machinery around it on *Odd Lots* (20 May 2024): a purchased factor model that reads every book each day, and a stop-loss that works as crude insurance against a PM whose payoff looks like an option on his own P&L (paraphrased). From that seat the clustered t is the number that sets the size, because the size is a multiple of how sure the platform is that the residual is real. Size a t of 2.1 as if it were 6 and the book runs close to three times the volatility its evidence supports, and Chapter 8-D's stop arithmetic says what follows: a PM with a Sharpe ratio of 1 at 6% volatility touches a 5% stop in about 43% of years, and at 4% volatility in about 13% (§8D.5). The fastest way to the stop is not a bad signal. It is a real one, sized by the wrong error bar.

*Used in:* §11.4.2 (runway as a hazard covariate), §13.8 (runway inside the PRS), §28.9 (the dashboard's runway column).


## 7-B.10 The Credit Statistics Module: A Reference Implementation

Every tool in this chapter is one function in `creditstats.py`, and the week's scenes are its test cases: the runway panel of the cold open and §7-B.9, Kaz's clustered Ford dummy and the Ford–GM half-life of the replay, the eight deals on Mags's whiteboard, the three bootstraps of §7-B.6, and Jonah's seeds. The specification below is the week's receipt.

### Specification for AI Implementation

**What ROBO built from the vague version.** Theo's first spec said: "Estimate default probabilities for the practice cohort. Use clean data." ROBO dropped every issuer without an observed outcome, as instructed, and reported a 75% three-year PD for six issuers that §7-B.4 shows have a 60% product-limit PD with a 22-point standard error. "Clean" had meant "censored," and nobody had said so. The precise spec below names the unit of independence, the censoring rule and the error bar for every estimator.

**The Spec You Hand the Robot.** Build `creditstats.py` (NumPy and SciPy only; no `statsmodels`, `lifelines` or `sklearn`, so every estimator is auditable against this chapter's equations). Every random function takes an explicit `numpy.random.Generator`; experiments spawn independent streams with `SeedSequence.spawn`.

**The functions.** `ols` and `vcov` (classical, hc1, cluster on the ultimate parent, two-way, Newey–West; equations 7B.1, 7B.2, 7B.4) with `nw_lags`; `logit_fit` (IRLS, optional ridge on slopes, issuer-clustered sandwich) and `platt_calibrate`; `kaplan_meier` (Greenwood, Nelson–Aalen, entry times for left truncation; 7B.5–7B.6) and `cox_ph` (Breslow ties and baseline; 7B.7); `ledoit_wolf` (7B.8), `mp_edge` and `residual_pca`; `stationary_bootstrap_indices` and `block_bootstrap` (stationary, moving-block, i.i.d.); `mc_estimate`, `control_variate`, `bridge_hit_prob` (7B.9), `first_passage_mc` and `first_passage_exact`. Shapes: `y (n,)`, `X (n, K)` with the constant in column 0, returns panels `(T, N)`; times in months or years as the caller states; $\sigma_V$ annualized decimal.

**Edge cases ROBO must handle, not guess.** Cluster on the ultimate parent, never the CUSIP; flag fewer than 50 clusters in `info`. Two-way covariances that are not positive semidefinite are eigenvalue-clipped and the clipping is logged. `nw` requires one time-ordered row per period. A logit that has not converged in 50 Newton steps raises an error that names separation, rather than returning the last iterate. Probabilities are clipped to $[10^{-6}, 1 - 10^{-6}]$ before any logarithm. Kaplan–Meier counts an issuer censored at an event time as at risk at that time, and an issuer with an entry time only after entry (left truncation). Distressed exchanges are events, never censoring, and the caller passes them as such. PCA loadings are sign-normalized so they sum to a positive number, and the count of "real" components uses the Marchenko–Pastur edge with a 10% margin for finite samples. Every Monte Carlo result returns its standard error and its 4-s.e. tolerance.

The first block is the module, saved as `creditstats.py`; the second is its acceptance test. Both are seeded; neither touches the network or the disk.

By Friday Theo had nine estimators, each with a paragraph on how it lies and a footnote on why you use it anyway. A list of estimators is not a tool. The trouble with a standard error is that a wrong one looks exactly like a right one: the runway signal printed a t-statistic of 6.1 or 2.4 depending on a single argument, and nothing in the output blushed. A desk that will run these estimators thousands of times across Chapters 8 through 15 cannot have every researcher re-derive the sandwich from memory and hope the degrees-of-freedom correction survived the trip. So the estimators live in one module, written once against this chapter's equations, small enough for Kaz to audit in an afternoon and strict enough that ROBO cannot quietly improve it.

The listing is `creditstats.py`, seven parts in the chapter's order, importing only `numpy` and `scipy`. For regression, `ols` returns coefficients and residuals, and `vcov` turns them into a covariance by wrapping a "bread", the inverse of $X'X$, around a "meat" built from scores, each row of $X$ scaled by its residual. The `kind` argument picks the meat: the pooled residual variance for `classical`, row-by-row outer products for `hc1`, scores summed within each group first for `cluster` (so eleven sibling bonds count as one draw), parent plus month minus their intersection for `twoway`, and Bartlett-weighted lagged cross-products for `nw`, with `nw_lags` choosing the window. The returned `info` carries the cluster count and a flag under 50. The logit is Newton's method from the sample log-odds, with a ridge that spares the constant, and `platt_calibrate` fits a two-parameter logit on a holdout and hands back a function. `kaplan_meier` and `cox_ph` walk the distinct event times and count who is still at risk at each; the first returns the product-limit curve with Greenwood variance and the Nelson–Aalen hazard, the second a Breslow-ties coefficient, its covariance and a baseline hazard. The rest serves panels and simulation: `ledoit_wolf` shrinks toward a scaled identity and returns the weight, `residual_pca` counts eigenvalues above 1.10 times the Marchenko–Pastur edge, `block_bootstrap` resamples whole dates so the cross-section travels together, and `mc_estimate`, `control_variate`, `bridge_hit_prob` and `first_passage_mc` report every simulated number with its standard error, with `first_passage_exact` as the closed-form referee.

Kaz treats the module as two things at once: the reference every faster implementation on the desk is checked against, and the daily driver at the scale of this book's panels. It is not a cure for few clusters. Under 50, `vcov` raises the flag and does nothing more, and the wild cluster bootstrap Kaz ran in §7-B.6 lives outside the module. The survival loops are plain Python over event times, fine for thousands of issuers and slow for millions. The trap is in `nw`, which lags rows, not dates. `nw_meat` slides down the score matrix and assumes each row is the next period. Hand it a bond-by-month panel stacked bond after bond and it will cheerfully correlate one bond's last month with the next bond's first, then return a confident, wrong standard error without a murmur. Theo's Thursday row in §7-B.9 collapsed the panel to one time-ordered Fama–MacBeth slope per month before calling it, which is the habit the function assumes.

*The full listing is [Listing 7-B.1 in Appendix F](#code-7b-1).*

A statistics module has a peculiar failure mode: it runs. A sandwich with the wrong small-sample factor, a Kaplan–Meier curve that drops a censored issuer from the risk set one period early, a bridge probability with the wrong sign in the exponent: each hands back a plausible number, and plausible numbers go into position sizes. The only defense is to make the code answer questions whose answers we already know, and to write the tolerance down before running it. Mags, who distrusts anything labeled "adjusted," would approve of the principle. A function earns its place by reproducing a result you could have worked out on the back of a docket.

The acceptance test draws six independent streams from one `SeedSequence(707)`, so that editing one experiment cannot move another, then runs one check per section of the chapter. The structural checks use bands derived from theory. A panel of 200 issuers with 11 bonds each and sibling correlation 0.6 is expected to show a clustered-to-classical standard error ratio near $\sqrt{1+(m-1)\rho}$, about 2.65; the run gives 2.66. Twelve-period overlapping sums of white noise return Newey–West multipliers near 8.0 at $L = 11$ and 10 at $L = 23$, against a truth of 12, so the test asserts the shortfall instead of hiding it. The six-issuer practice cohort returns survival of 0.8, 0.6 and 0.4 and a Greenwood variance of 0.048, which is the 60% PD and its 22-point error bar. The statistical checks use four standard errors: the logit recovers its three coefficients, and its fitted probabilities sum to the observed defaults; the Cox fit recovers a log hazard ratio of 1.1 under independent censoring; a million-draw tail probability lands on the normal. Shrinkage stays invertible with more bonds than months, and one planted factor clears the Marchenko–Pastur edge while pure noise does not. The block bootstrap sees the AR(1) dependence the i.i.d. bootstrap misses. The last block sets a monthly grid against the exact first-passage probability, 0.230: the naive grid gives 0.176, the bridge gives 0.230, and a drifted case on four steps confirms that drift cancels.

The desk runs it after every edit to the module and every upgrade of NumPy or SciPy. It proves only that the code reproduces cases generated by its own assumptions; it cannot tell you the world is stationary. Its weak point is the one Jonah found in §7-B.8, in a different shop: a shared stream. `r_mc` feeds the bootstrap, Monte Carlo and bridge checks in sequence, so the results are deterministic only for this exact order of draws. Insert one assertion above them and every later draw changes; a four-standard-error band then fails by luck about once in sixteen thousand tries per assertion, and the temptation, the one with a March commit message, is to widen the tolerance. The fix is the one Jonah's eleven lines made: give the new experiment its own stream.

*The full listing is [Listing 7-B.2 in Appendix F](#code-7b-2).*

*Used in:* imported by Chapters 8–12, 14 and 15 (`from creditstats import vcov, logit_fit, kaplan_meier, ledoit_wolf, first_passage_mc`); its asserts are the tolerance convention for every reference implementation in the book.


## 7-B.11 Desk Debrief

Before the sheet, the map: each tool in the chapter, where its equation lives, the box that pictures it, the scene in which somebody needed it, and the code.

| Concept | Equation | Intuition (box) | Judgment (scene) | Code |
| :--- | :--- | :--- | :--- | :--- |
| Sandwich, cluster meat and the Moulton factor | (7B.1)–(7B.3), §7-B.1 | The re-deal and the wedding guests (§7-B.1) | Cold open, 6.1 → 2.4 → 2.1; Theo's CUSIP evening; Kaz's Ford dummy, 14.2 → 1.8 (§7-B.1) | [Listing 7-B.1](#code-7b-1) |
| Overlapping returns and Newey–West | (7B.4), §7-B.2 | One rumor, twelve messengers (§7-B.2) | Kaz's sixty-day labels: two observations of one company (One March, Counted Once) | [Listing 7-B.1](#code-7b-1) |
| A pair's half-life | AR(1), $\ln 2/(-\ln\rho_1)$ (One March, Counted Once) | What an ADF test asks (Ch 7 §7.3) | The Ford–GM card: 9.6 days, or four days to never (PB-03) | none |
| Logit and calibration | $\operatorname{logit} p = b_0 + b^\top x$; Brier decomposition, §7-B.3 | Evidence on a kitchen scale; two weathermen (§7-B.3) | The dealer's weekly recalibration (§7-B.3); the boosted model that learned Halvorsen (§7-B.7) | [Listing 7-B.1](#code-7b-1) |
| Kaplan–Meier and Greenwood | (7B.5)–(7B.6), §7-B.4 | A clock that stops early, and the coin (§7-B.4) | The Chapter 22 Cohort: six of eight is 81% at three years | [Listing 7-B.1](#code-7b-1) |
| Cox proportional hazards | (7B.7), §7-B.4 | A race in the wind (§7-B.4) | A hazard ratio of six, from two-thirds to fifty-four; Theo's open-market clause (§7-B.4) | [Listing 7-B.1](#code-7b-1) |
| Shrinkage and Ledoit–Wolf | (7B.8), §7-B.5 | The early-season batting average (§7-B.5) | Venn's eighteen factors against the desk's five (§7-B.5) | [Listing 7-B.1](#code-7b-1) |
| PCA and the Marchenko–Pastur edge | $(1 + \sqrt q)^2$, §7-B.5 | A stretched ball; noise has an edge (§7-B.5) | "So we just assume Gaussian" (§7-B.5) | [Listing 7-B.1](#code-7b-1) |
| Bootstrap by the independent unit | Plug-in principle, §7-B.6 | Slips in a hat (§7-B.6) | Kaz's three intervals and a wild-cluster p of one half (§7-B.6) | [Listing 7-B.1](#code-7b-1) |
| Monte Carlo error and the Brownian bridge | $\hat s_g/\sqrt n$; (7B.9), §7-B.8 | The square-root tax and the mirror (§7-B.8) | Thursday model review: the seed, the tolerance, the ticket (§7-B.8) | [Listing 7-B.2](#code-7b-2) |

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
4. *(One factor per coffee.)* A residual panel of 250 bonds over 60 months has top correlation eigenvalues 14.1, 8.7 and 6.2, and Kaz announces three factors, one for each coffee they drank this morning. How many clear Marchenko–Pastur with a 10% margin, and how many eigenvalues are zero? *Solution.* $q \approx 4.17$, the edge is $(1 + 2.04)^2 \approx 9.25$, or 10.2 with the margin: one factor. The 8.7 may be real, but this panel cannot tell, so check its stability across windows. Rank is at most 59, so at least 191 eigenvalues are zero, and an optimizer handed the raw matrix will find 191 riskless portfolios that are not.
5. *(A tolerance with a pedigree.)* The one-year first-passage probability of §7-B.8 is 23.0%. How many paths give a 4-s.e. tolerance of 0.5 points? ROBO runs 200,000 on a monthly grid without the bridge; by how much does the test fail? *Solution.* $n \ge (4\sqrt{0.23 \times 0.77}/0.005)^2 \approx 113{,}000$. The grid converges to 17.6% (the continuity correction of §7-B.8 says 17.1%, but it is only an approximation), with a standard error of about 0.085 points at 200,000 paths, so the 5.4-point bias is about 64 standard errors. More paths drew a tighter circle around the wrong number.
6. *(The base-rate oracle.)* Kaz's model gives every issuer 2% in a cohort that defaults at 2%. Decompose its Brier score. *Solution.* Reliability and resolution are both zero, so the score is the uncertainty, $0.02 \times 0.98 = 0.0196$, and the AUC is 0.5: perfectly calibrated, no ranking at all, like a forecaster who reads out London's average rainfall every morning. An intercept-only logit builds this model for free (§7-B.3), so that is what it is worth.

### Deep-Dive Resource Graph

- **Podcasts:** *Odd Lots*, "Why the True Price of a Bond Can Still Be Hard To Know" (5 Apr 2021), https://omny.fm/shows/odd-lots/why-the-true-price-of-a-bond-can-still-be-hard-to (pricing error, §7-B.1). *Flirting with Models*, "Ralph Smith – Scientific Investing in Fixed Income (S5E7)" (11 Jul 2022), https://www.flirtingwithmodels.com/episodes/kAEkSoYuRwd (which bonds a backtest may assume it held). *Cloud 9fin*, "LME Doomscrolling — Data-driven reality check" (7 Apr 2026), https://share.transistor.fm/s/1f62123b (life after coercive LMEs, §7-B.4).
- **More Episodes and Lectures (Edition 2):**
  - **"How to Forecast the Future"** (*Odd Lots*, Philip Tetlock, 2019-08-26). How to judge whether predictions are good ones and how to become a better forecaster: the non-technical door to forecast scoring before the Brier decomposition of §7-B.3 and Exercise 6. https://omny.fm/shows/odd-lots/how-to-forecast-the-future
  - **"The Zombie Apocalypse with Dr. Edward Altman"** (*Cloud 9fin*, 2024-09-11). The Z-score as a classic default-probability model, used here to define zombie firms by low scores: the historical benchmark to hold the logistic model and calibration plots of §7-B.3 against. https://share.transistor.fm/s/5db565ae
  - **"Petter Kolm - 23/08/21"** (*Risk.net Quantcast*, NYU Courant, 2021-08-25). Transaction-cost analysis that ignores partial fills "might be off by 20% to 30%": a selection-bias example for why the cohort you can see is not the cohort that existed, the censoring and survivorship point of §7-B.4. https://soundcloud.com/user-393208363/petter-kolm-230821
  - **"Chris Carrano: Factor Models, Institutional Insights, and Portfolio Diagnostics (S7E20)"** (*Flirting with Models*, Venn by Two Sigma, 2025-09-02). Why Venn uses 18 orthogonalized factors, blends Lasso and OLS to reduce overfitting, and prefers interpretability over complexity: a practitioner's case for the shrinkage and structured-covariance logic of §7-B.5 (the feed title reads "Designing Practical Factor Models"). https://www.flirtingwithmodels.com/episodes/HB4VTNpvBp2
  - **"The Illusion of Backtests and Drivers of Price ft. Richard Brennan"** (*Top Traders Unplugged*, SI310, host Niels Kaastrup-Larsen, 2024-08-24). Why a backtest cannot predict future performance and how to set more realistic expectations of future risk and return: the motivation for the block and stationary bootstraps of §7-B.6. https://www.toptradersunplugged.com/podcast/the-illusion-of-backtests-and-drivers-of-price-ft-richard-brennan/
  - **"Lecture 8: Time Series Analysis I"** (MIT OpenCourseWare 18.S096, Dr. Peter Kempthorne, Fall 2013). First of three lectures on stochastic processes via regression and stationarity models: a free video primer on the autocorrelation that makes overlapping returns misleading in §7-B.2. https://ocw.mit.edu/courses/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/resources/lecture-8-time-series-analysis-i/
- **Practitioner Writing:** Petersen, "Programming Advice - Finance Panel Data Sets," with a test data set for checking `vcov`, https://www.kellogg.northwestern.edu/faculty/petersen/htm/papers/se/se_programming.htm ; J.P. Morgan/Reuters, *RiskMetrics Technical Document* (1996).
- **Academic Papers:** Petersen (2009), RFS; Cameron, Gelbach and Miller (2011), *Robust Inference with Multiway Clustering*; Newey and West (1987), Econometrica; Shumway (2001), *Forecasting Bankruptcy More Accurately*; Kaplan and Meier (1958); Cox (1972); Ledoit and Wolf (2004), JMVA; Politis and Romano (1994), *The Stationary Bootstrap*; Beaglehole, Dybvig and Zhou (1997), *Going to Extremes*, FAJ.
- **Data & Code:** `creditstats.py` (§7-B.10, Appendix F); `arch` time-series bootstraps, https://arch.readthedocs.io/en/latest/bootstrap/timeseries-bootstraps.html ; Open Bond Asset Pricing, https://openbondassetpricing.com

*Used in:* every chapter that reports an error bar; the Debrief feeds App E (Laws 2–5, 7, 9, 11–15).

<!-- STATUS: COMPLETE -->
