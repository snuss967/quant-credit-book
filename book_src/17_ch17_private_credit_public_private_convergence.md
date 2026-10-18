# Chapter 17: Private Credit & the Public–Private Convergence

> *"Middle market direct lending (Private Credit): Proxy Index using S&P UBS Leveraged Loan B Index."* (Nuveen_Multi_Asset_Credit_Quant_Framework p.9)
>
> And, two pages earlier in the same framework's sector table, in the volatility column for middle-market direct lending: "N/A". (Nuveen_Multi_Asset_Credit_Quant_Framework p.2)

## Cold Open: Volatility N/A

Tuesday, June 23, 2026, 4:40 p.m. The RFQ is for \$25mm of a listed business development company's senior unsecured notes due 2029. It lands two hours after a headline that a \$26 billion non-traded private credit fund has received redemption requests for 16.8% of its shares this quarter, against a 5% cap. *(The fund and its numbers are real: InvestmentNews, June 23, 2026. The RFQ and the listed BDC are ours.)*

Kaz has already pulled the BDC's NAV history. "I don't see the problem. NAV per share has moved less than one percent all quarter. I tried to pull the volatility of the loan book and the vendor field says N/A."

"N/A isn't zero," Ines says. "N/A means nobody looked. What's the pot, what are the odds, and who at this table knows more than we do? Somebody wants out of the bond of a vehicle that owns the same kind of loans as the fund that just got a run. They want out at 4:40 today, not at 9:30 tomorrow. That's the hand."

"In my day," Mags says without looking up, "we called a bond with no price a bond. You found out what it was worth when you tried to sell it. Then you found out who else was trying."

Theo is reading the BDC's last 10-Q, which is what he does when people start talking about poker. "What does the revolver say about borrowing-base eligibility for PIK loans? If the bank haircuts anything that's been amended into PIK, and a fifth of the book is software that's been amended into PIK, then the borrowing base shrinks exactly when the fund needs it. And these notes sit behind that line."

"Are you saying the NAV is wrong?" Kaz asks.

"I'm saying the NAV is a mark," Theo says. "It's marked quarterly, by the manager, who earns fees on it. The bond price is a price. Underneath, it's the same loans."

Ines nods at the screen. "Then the question isn't what the bond is worth. It's what the loans are worth, and which of the things we *can* trade already knows."

The question this chapter answers: **what are the true value and risk of a portfolio whose only published price is set by its owner, and which public instruments let us trade our answer?**

By the end of this chapter you will be able to: write a private mark as a moving-average filter of an unobserved return and derive what that filter does to volatility, correlation, beta and Sharpe ratio; estimate the smoothing kernel from a few dozen quarterly marks without fooling yourself; turn a listed BDC's price-to-NAV ratio into an implied markdown on its loans, and its non-accrual disclosures into an implied carrying value for bad loans; forecast the direction of private-to-public refinancing flow from a public regime variable; price a semi-liquid fund's redemption queue as a run with a pro-rata cap; and assemble the book of public instruments that expresses all of it.

## 17.1 One Borrower Pool, Two Pricing Regimes

### 17.1.1 Desk framing: the same credit, measured twice

Start with the definitional trap, because every number in this chapter has to survive it. "Private credit" ranges from about \$1.3 trillion to more than \$3 trillion depending on whether you mean loans or assets under management, the US or the world, and whether you include dry powder. On October 16, 2026 the Federal Reserve settled the US loan number by putting private credit into the Financial Accounts (Z.1): \$1,493.5 billion of private-credit loans at the end of 2025, held by private debt funds (\$532B), BDCs (\$456B), the rest of the world (\$376B), interval and tender-offer funds (\$76B) and middle-market CLOs (\$54B) (Brinkman et al., FEDS Note, October 16, 2026). When someone tells you the size of private credit, ask which of those numbers they mean. It is the "but what does the credit agreement say?" of market sizing.

Now the fact that organizes the chapter. Private credit and public leveraged finance are not two asset classes. They are **one borrower pool with two pricing regimes**. A Fed study of the two markets finds that 41% of large middle-market borrowers have used both, that switching from leveraged loans to private credit peaked near half of leveraged-loan borrowers in early 2023, and that the borrowers in each market look like this:

| 2025 issuance (medians unless stated) | Private credit | Leveraged loans |
| :--- | ---: | ---: |
| Borrower revenue | \$223M | \$902M |
| Debt / EBITDA | 5.0x | 3.2x |
| Interest coverage | 2.2x | 3.7x |
| Spread | S+500 | S+400 |
| Rated BB or better | 0% | 28% |
| CCC or below | 15% | 9% |
| Software share of issuance | 21% | 16% |

*Source: Banegas et al., "Private Credit and Leveraged Loan Markets: Similarities, Differences, and Substitution," FEDS Note, August 11, 2026.*

The private borrower is smaller, more levered and more software-heavy. It pays about 100bp more for the privilege. None of that makes it a different kind of credit; it is the bottom-left of the same scatter plot. The same sponsor, the same software company and the same five turns of leverage can sit in a CLO as a daily-priced syndicated loan or in a BDC as a quarterly-marked unitranche. **What differs is not the credit. It is the measurement.**

A public loan is *priced*: daily, noisily, by people who lose money when they are wrong, with an error that is roughly mean zero. A private loan is *marked*: quarterly, from a model, smoothed, by the party that owns it and earns a fee on the number. Everything in this chapter is the mathematics of that difference. If you want one sentence for your monitor, it is this: *private credit is public credit with the price removed, and our job is to put the price back and get paid by whoever still believes it was never there.*

Theo will find the structure familiar, because he has seen it on the other side of the table. A BDC is, in the Boston Fed's phrase, "a CLO in which banks hold the top tranche" (Fillat, Landoni, Levin and Wang, Boston Fed Current Policy Perspectives 25-8, May 21, 2025): a bank revolver on top, unsecured notes in the middle, listed or non-listed equity at the bottom, and a manager who both picks the collateral and marks it. A perpetual BDC facing 16.8% redemption requests against a 5% cap is a liquidity-constrained borrower. The right tool for it is the one on Theo's USB stick: a thirteen-week cash flow model in which the "maturity wall" is the redemption queue and the "revolver availability" is the undrawn bank line plus whatever syndicated loans the fund holds for liquidity. And "selective default" (PIK amendments, amend-and-extends, covenant holidays) is the bilateral market's liability management transaction: the same redefinition of default Theo watched in Serta and Incora, done quietly, with one lender and no docket.

### 17.1.2 What "private" actually buys: access and patience

There is an honest case for private credit, and it is worth stating before we spend thirty pages being rude about marks. The post-crisis evidence says borrowers went to nonbanks for *access*, not price. In 2010–2015 about one-third of middle-market loans came directly from nonbanks, those loans priced about 190bp above comparable bank loans after controls, and the probability of borrowing from a nonbank rose sharply when EBITDA turned negative (Chernenko, Erel and Prilmeier, NBER w26458; RFS 2022). Private lenders write cash-flow loans that banks will not, with real maintenance covenants (Block, Jang, Kaplan and Schulze, NBER w30868). The lender is paid for underwriting what the syndicated market won't take, and for holding what nobody can sell.

> **[SOURCE EXTRACTION]** *Ben_Dor_Quantitative_Credit_Portfolio_Management p.166:* "Long-term investors, with reduced mark-to-market constraints, can choose to provide liquidity to the market and buy the bond, comfortable with the low default risk."
>
> **Annotation.** This is the respectable theory of the illiquidity premium: patient capital that does not have to mark to market earns a premium for absorbing assets that forced sellers must dump. Ben Dor and coauthors are writing about public bonds after downgrades, but the logic is the original pitch for private credit, and it has two conditions. The investor must have *reduced mark-to-market constraints*, and the default risk must be *low*. The 2020s growth of semi-liquid retail vehicles quietly removed the first condition: a fund that promises quarterly liquidity at NAV has re-imported the mark-to-market constraint while keeping the mark smoothed. The 2025–26 cycle tested the second, through software borrowers exposed to AI disruption. The modern desk departs from the shelf here. It treats the illiquidity premium as real but *conditional* on the holder's liability structure, and it prices the premium separately for a drawdown fund (patient), an insurer (patient but rating-constrained) and a perpetual BDC (patient until the redemption queue says otherwise).

The dishonest version of the case is the one the Nuveen table hints at. If the volatility cell says "N/A," an optimizer that needs a number will use whatever is smoothest, and the smoothest series in the world is one nobody updates. Cliffwater's direct lending index (CDLI), which aggregates BDC portfolio marks, returned 9.3% in 2025, 10.4% of it from interest income, with a 20-year average of 9.5% and one negative year (Cliffwater release, March 31, 2026). Those are real returns to real loans. The question §17.2 answers is how much real *risk* sits behind them, and why the reported series cannot tell you.

> **Trend Watch.** *From niche to a Z.1 line item, 2010–2026.* Private-credit vehicle AUM grew from about \$350 billion in 2012 to more than \$2.6 trillion (Brinkman et al., FEDS Note, October 16, 2026). The number of loans held by private-credit BDCs rose from 1,395 in 2010 to 20,182 in 2022 (Ellias and de Fontenay, *The Credit Markets Go Dark*, 134 Yale L.J., January 2025). On the Fed's new Z.1 basis, US private-credit loans were \$1,042.6B (2023), \$1,253.6B (2024) and \$1,493.5B (2025), growth of about 20% a year, and private credit is now 6% of nonfinancial business debt against 3% for syndicated loans (Brinkman et al.). The retail channel grew fastest: semi-liquid fund net assets rose from about \$15B in 2018 to \$388B in 2025 (George and Shin, FEDS Note, October 14, 2026). Globally, AUM passed \$2.2T in March 2025 with a \$4.5T forecast for 2030 (BlackRock *Private Credit Primer*, January 2026). **What it means for the desk:** private credit now has official holder-level series (Z.1 codes FL893167205 for the total, FL453067203 for BDCs, FL443067205 for private debt funds, FL673067205 for middle-market CLOs; see Appendix B), which makes it a flow-of-funds variable like any other. The forced-seller graph in Chapter 1 needs five new nodes, and the largest of them, BDCs, files a schedule of every loan it owns every quarter.

### Deep-Dive Resource Graph

- **Practitioner Writing:** Banegas et al., "Private Credit and Leveraged Loan Markets: Similarities, Differences, and Substitution," FEDS Note (Aug 11, 2026), https://www.federalreserve.gov/econres/notes/feds-notes/private-credit-and-leveraged-loan-markets-similarities-differences-and-substitution-20260811.html ; Brinkman et al., "Introducing Private Credit into the Financial Accounts of the United States," FEDS Note (Oct 16, 2026), https://www.federalreserve.gov/econres/notes/feds-notes/introducing-private-credit-into-the-financial-accounts-of-the-united-states-20261016.html
- **Academic Papers:** Chernenko, Erel and Prilmeier, "Why Do Firms Borrow Directly from Nonbanks?" (NBER w26458), https://www.nber.org/papers/w26458 ; Ellias and de Fontenay, "The Credit Markets Go Dark," 134 Yale L.J. (2025), https://www.yalelawjournal.org/article/the-credit-markets-go-dark
- **Data & Code:** Federal Reserve Z.1 Financial Accounts, https://www.federalreserve.gov/releases/z1/

## 17.2 The Mark as a Filter: Smoothing, Stale Prices and the Illusion of Low Volatility

### 17.2.1 Desk framing: you are fitting someone else's model

Before any algebra, the shelf has already diagnosed the disease, in a chapter written about vendor-priced public bonds.

> **[SOURCE EXTRACTION]** *Bohn_Stein_Active_Credit_Portfolio_Management p.334:* "Essentially, unwary modelers may inadvertently end up fitting someone else's model. ... Many supposedly profitable trading strategies end up being the result of an inadvertent fitting of a matrix model as reflected in matrix prices reported by a data vendor."
>
> **Annotation.** Bohn and Stein were warning about evaluated prices for bonds that rarely trade: the vendor fills the gap with a model, and a researcher who backtests on those prices is backtesting the vendor's model. A BDC net asset value is the same object with higher stakes. Under ASC 820 most private loans are Level 3 assets, valued by the manager's valuation committee with a third-party firm reviewing a sample. A backtest on CDLI, or on any series built from BDC marks, is therefore a backtest on fifty valuation committees. On a 2026 desk this cuts in both directions. It means any "low volatility, low correlation" result is suspect until it survives the corrections below. It also means the valuation model itself is an object we can estimate, and once estimated it is a predictable process, which is the root of every trade in §17.9.

The shelf even tells you what the disease looks like on a chart.

> **[SOURCE EXTRACTION]** *Bohn_Stein_Active_Credit_Portfolio_Management p.335:* "a time series plot that shows stair-stepped trends in price ... will likely reflect matrix pricing as new levels for the price are bled into the reported price, creating auto-correlation in the data."
>
> **Annotation.** Plot a BDC's NAV per share next to the leveraged loan index over 2022 and you will see exactly this: flat treads and small risers, with the risers arriving a quarter or two after the index moved. "Bled into the reported price" is the economic content of the smoothing kernel we are about to write down. The desk's first diagnostic chart for any private vehicle is that overlay, and its first statistic is the autocorrelation of the reported returns. The modern twist is that the stair-step now has a public counterpart. Listed BDC shares, BDC bonds and a small number of daily-priced private vehicles move *between* the steps, so the kernel can be estimated against observed prices instead of guessed.

Kaz looks at the overlay and says the natural thing. "So the NAV is just a lagged index. Let's regress it on the index with a few lags and call the sum of coefficients the true beta." Then, after a pause that everyone on the desk recognizes: "And let's just assume Gaussian." This time he is mostly right, and §17.2.2 says why. The part he will regret comes in §17.2.4.

### 17.2.2 Derivation: the Getmansky–Lo–Makarov smoothing model

**Notation.** In this chapter $t$ counts **quarters**, not years; we convert explicitly when comparing with monthly public data. We write returns as $x$ rather than $r$, because this book reserves $r$ for the short rate and $R$ for recovery. All expectations are under the physical measure $\mathbb{P}$: there is no liquid hedge for a single private loan, so nothing here is priced under $\mathbb{Q}$.

**Assumptions.** Let $x_t$ be the true, unobservable quarterly excess return on the loan portfolio, covariance-stationary with mean $\mu$ and variance $\sigma^2$, and serially uncorrelated. Let $F_t$ be the excess return on a public factor (the leveraged loan index, say), also serially uncorrelated, with $x_t=\beta F_t+\epsilon_t$, where $\epsilon_t$ is idiosyncratic and independent of $F$ at all leads and lags. The reported (marked) return is a finite moving average of true returns:

$$
x^{o}_t=\sum_{k=0}^{K}\theta_k\,x_{t-k},\qquad \theta_k\in[0,1],\qquad \sum_{k=0}^{K}\theta_k=1 .
$$

Here $\theta_0$ is the share of today's true return that shows up in today's mark, $\theta_1$ the share that shows up next quarter, and so on. The unit-sum constraint says the marks *eventually* catch up: nothing is hidden forever, only delayed. (When the constraint fails, with $\sum_k\theta_k<1$, the marks never catch up, because the collateral was never there. That is the fraud case, and §17.8 returns to it.)

**Mean.** By linearity, $\mathbb{E}[x^o_t]=\sum_k\theta_k\,\mathbb{E}[x_{t-k}]=\mu\sum_k\theta_k=\mu$. Smoothing does not change the average return. This is why the CDLI's 9.3% can be a perfectly good estimate of the mean while being useless for risk.

**Variance.** Because the $x_{t-k}$ are uncorrelated,

$$
\operatorname{Var}(x^o_t)=\sum_{k=0}^{K}\theta_k^2\,\sigma^2 .
$$

Since $\theta_k\in[0,1]$ and $\sum_k\theta_k=1$, we have $\sum_k\theta_k^2\le\big(\max_k\theta_k\big)\sum_k\theta_k\le1$, with equality only when one $\theta_k$ equals one. Reported volatility is deflated by the factor $\sqrt{\sum_k\theta_k^2}$, and the deflation is largest when the weights are spread evenly: with $K+1$ equal weights it is $1/\sqrt{K+1}$.

**Autocorrelation.** For lag $j\ge1$,

$$
\operatorname{Cov}(x^o_t,x^o_{t-j})=\sum_{k}\sum_{l}\theta_k\theta_l\operatorname{Cov}(x_{t-k},x_{t-j-l}) .
$$

The covariance inside the sum is $\sigma^2$ when $k=j+l$ and zero otherwise, so only the terms $k=l+j$ survive:

$$
\operatorname{Cov}(x^o_t,x^o_{t-j})=\sigma^2\sum_{l=0}^{K-j}\theta_l\,\theta_{l+j},
\qquad
\rho^{o}_j=\frac{\sum_{l=0}^{K-j}\theta_l\,\theta_{l+j}}{\sum_{k=0}^{K}\theta_k^2}\;\ge 0 .
$$

Every autocorrelation of the reported series is non-negative, and it is zero beyond lag $K$. Positive autocorrelation in a NAV series is therefore *mechanical*: it would appear even if the true returns were pure noise. Call it what it is. NAV "momentum" in a smoothed series is a property of the measurement, not of information, and a strategy that trades it inside the private wrapper is trading the valuation calendar.

**Sharpe ratio.** With $\text{SR}=\mu/\sigma$ the true Sharpe ratio,

$$
\text{SR}^{o}=\frac{\mu}{\sigma\sqrt{\sum_k\theta_k^2}}=\frac{\text{SR}}{\sqrt{\sum_k\theta_k^2}}\;\ge\;\text{SR}.
$$

**Beta and correlation to public credit.** Because $F$ is serially uncorrelated and independent of $\epsilon$, $\operatorname{Cov}(x_{t-k},F_t)=\beta\operatorname{Var}(F)$ when $k=0$ and zero otherwise. So

$$
\beta^{o}_{0}\equiv\frac{\operatorname{Cov}(x^o_t,F_t)}{\operatorname{Var}(F_t)}=\theta_0\,\beta,
\qquad
\operatorname{Corr}(x^o_t,F_t)=\frac{\theta_0}{\sqrt{\sum_k\theta_k^2}}\,\operatorname{Corr}(x_t,F_t).
$$

The contemporaneous beta to public credit is attenuated by exactly $\theta_0$. The rest of the beta has not disappeared; it is parked at lags $1,\dots,K$, where $\operatorname{Cov}(x^o_t,F_{t-k})=\theta_k\beta\operatorname{Var}(F)$. Correlation is attenuated by the smaller factor $\theta_0/\sqrt{\sum_k\theta_k^2}$, because the denominator's volatility was deflated too.

**Worked check.** Take $\theta=(0.5,0.3,0.2)$. Then $\sum_k\theta_k^2=0.25+0.09+0.04=0.38$, so reported volatility is $\sqrt{0.38}=0.616$ of true volatility and the reported Sharpe ratio is inflated by $1/0.616=1.62$. The autocorrelations are $\rho^o_1=(0.5\cdot0.3+0.3\cdot0.2)/0.38=0.21/0.38=0.553$ and $\rho^o_2=(0.5\cdot0.2)/0.38=0.263$. The contemporaneous beta is half the true beta, and the contemporaneous correlation is $0.5/0.616=0.81$ of the true one.

Those are not exotic numbers. A two-quarter lag in the marks, which any valuation committee can produce without anyone doing anything wrong, turns an asset with the risk of a single-B loan portfolio into one that reports 62% of the volatility, half the beta and 1.6 times the Sharpe ratio. That is how a vendor field ends up saying "N/A": the honest answer would have been "about 1.6 times what you see, and correlated with things you already own, a quarter later."

> **Desk Myth vs. Desk Reality.** *Myth:* Private credit has low volatility and low correlation with public credit, so it diversifies a high-yield book. *Reality:* It has low *measured* volatility because $\sum_k\theta_k^2<1$, and low *contemporaneous* correlation because $\theta_0<1$. Sum the lagged betas and the correlation comes back. Cliff Asness has made the uncomfortable version of the point: "What if investors will actually pay a higher price and accept a lower expected return for very illiquid assets?" and "Attractive smoothness of returns may not come for free" (Asness, "The Illiquidity Discount?", AQR, December 19, 2019). If investors value not seeing the volatility, the smoothing is a product feature, and somebody is paying for it. The desk's job is to find out who, and to be on the other side when the feature is withdrawn.

### 17.2.3 Recovering the beta: Dimson sums and the public-leads-private test

Kaz's instinct is the Dimson (1979) and Scholes–Williams (1977) correction for nonsynchronous trading, invented for thinly traded stocks and exactly right here. Regress reported returns on the current and $K$ lagged factor returns:

$$
x^o_t=\alpha+\sum_{k=0}^{K}b_k\,F_{t-k}+u_t,\qquad \hat\beta^{\text{agg}}=\sum_{k=0}^{K}\hat b_k .
$$

Under the model, $x^o_t=\sum_k\theta_k(\beta F_{t-k}+\epsilon_{t-k})$, so the population coefficients are $b_k=\theta_k\beta$, the residual $u_t=\sum_k\theta_k\epsilon_{t-k}$ is uncorrelated with every regressor, and

$$
\sum_{k=0}^{K}b_k=\beta\sum_{k=0}^{K}\theta_k=\beta,\qquad \hat\theta_k=\frac{\hat b_k}{\sum_l\hat b_l}.
$$

One regression gives you both the true beta and an estimate of the kernel. It is also the **public-leads-private test**: $b_1,b_2>0$ with respectable $t$-statistics *is* the lead–lag, and its tradable restatement is the one-quarter-ahead forecast

$$
\mathbb{E}_t\big[x^o_{t+1}\big]=\alpha+\sum_{k=1}^{K}b_k\,F_{t+1-k},
$$

which is known at $t$ because it uses only $F_t,F_{t-1},\dots$. The next NAV print is partly *already in the public data*. A desk that knows the index fell 3% this quarter and that $b_1\approx0.3$ knows the next mark will carry about $0.9\%$ of that fall, before the valuation committee meets. The residual $u_t$ is serially correlated (it is an MA($K$) in $\epsilon$), so use HAC standard errors with at least $K$ lags, or the $t$-statistics will flatter you too.

Note what the forecast does *not* say. It does not say you can buy the NAV low and sell it high, because inside a non-traded fund you transact at the smoothed NAV in both directions, subject to a cap. It says that any *public* instrument whose price is tied to that NAV (a listed BDC's equity, its bonds, a fund-of-BDCs ETF) will be repriced by a number you can forecast. §17.9 builds the book on that.

### 17.2.4 Unsmoothing, and why you should do less of it than you want to

The other direction is to invert the filter and recover $x_t$ from $x^o_t$. The workhorse is Geltner's (1991, 1993) appraisal-smoothing model from real estate, which is the GLM model with geometric weights, $\theta_k=(1-\theta)\theta^k$ for $k=0,1,2,\dots$ and $0\le\theta<1$. Those weights sum to one, and the model collapses to a recursion:

$$
x^o_t=(1-\theta)\,x_t+\theta\,x^o_{t-1}
\quad\Longrightarrow\quad
\hat x_t=\frac{x^o_t-\theta\,x^o_{t-1}}{1-\theta}.
$$

For the geometric kernel, $\sum_k\theta_k^2=(1-\theta)^2\sum_k\theta^{2k}=(1-\theta)/(1+\theta)$ and $\rho^o_j=\theta^j$, so $\theta$ is just the first-order autocorrelation of reported returns. The variance of the unsmoothed series follows from $\operatorname{Var}(a-\theta b)=\operatorname{Var}(a)+\theta^2\operatorname{Var}(b)-2\theta\operatorname{Cov}(a,b)$:

$$
\operatorname{Var}(\hat x_t)=\frac{(1+\theta^2)\operatorname{Var}(x^o_t)-2\theta\operatorname{Cov}(x^o_t,x^o_{t-1})}{(1-\theta)^2}.
$$

Now the regret. Real marks contain measurement noise $\eta_t$ (rounding, one-off valuation calls, the quarter a third-party valuer was replaced), so we observe $x^o_t+\eta_t$. The inversion is linear, so the noise passes through as

$$
\hat x_t-x_t=\frac{\eta_t-\theta\,\eta_{t-1}}{1-\theta},\qquad
\operatorname{Var}(\hat x_t-x_t)=\frac{1+\theta^2}{(1-\theta)^2}\,\sigma_\eta^2 .
$$

At $\theta=0.6$ the noise variance is amplified $8.5\times$; at $\theta=0.7$, $16.6\times$; at $\theta=0.9$, $181\times$. Unsmoothing a heavily smoothed series does not reveal the truth. It reveals the noise, enlarged. This is the place Kaz's Gaussian assumption bites: valuation noise is not Gaussian, it is lumpy (a single large write-down on a concentrated position), and the inversion turns a lump into a spike followed by an echo of the opposite sign.

Three more error-prone spots, each of which has embarrassed someone.

1. **Small samples.** Twenty to forty quarterly observations are all most vehicles have. With $n=30$ and $\rho_1=0.5$, the standard error of $\hat\rho_1$ is about $\sqrt{(1-\rho_1^2)/n}=0.16$, so a 90% interval for $\theta$ runs from roughly 0.24 to 0.76. Report intervals, not points.
2. **Common smoothing.** Couts, Gonçalves and Rossi ("Unsmoothing Returns of Illiquid Funds," *Review of Financial Studies* 37(7), 2024) show that funds holding similar assets share a *common* source of spurious autocorrelation, so unsmoothing fund by fund leaves correlated lag in the residuals and understates systematic risk. Estimate $\theta$ on a cross-holder panel, which for BDCs is natural: many hold the same facilities.
3. **Frequency.** A quarterly $\rho_1$ is not comparable with a monthly one. If you are benchmarking against the shelf's monthly autocorrelation buckets for public bonds, aggregate first.

> **[SOURCE EXTRACTION]** *Dynkin_Systematic_Investing_in_Credit p.623:* "if corporate bond prices are only updated infrequently and are subject to 'stale' pricing, their returns are likely to be positively correlated as new information slowly gets priced in."
>
> **Annotation.** Dynkin and coauthors use the trailing autocorrelation of excess returns as a *liquidity measure* for public corporate bonds, sorting bonds into low, middle and high autocorrelation buckets. Taken to its limit, a private loan is the most illiquid bucket with the volume column deleted: its reported returns are positively autocorrelated by construction, because the only "trades" are valuation-committee decisions. The departure for a 2026 desk is the direction of inference. For public bonds the autocorrelation *measures* illiquidity; for a private vehicle, the autocorrelation *is* the smoothing kernel, and once estimated it becomes an input to forecasting the next mark rather than a property to diversify away.

### Specification for AI Implementation

**The Spec You Hand the Robot (vague version).** "ROBO, estimate the volatility of private credit." ROBO computes the standard deviation of quarterly CDLI returns, annualizes it to 2.1% *(illustrative)*, compares it with the Treasury index, and files private credit as safer than Treasuries. It implemented exactly what was asked. The precise version follows.

**Engine.** `mark_gap`, the Mark-Gap Monitor. Pure functions, numpy and pandas only, built in four cumulative blocks across this chapter (smoothing in §17.2, marks in §17.3, flows in §17.4, runs in §17.6). Every block ends with seeded sanity checks.

**Data schemas** (pandas DataFrames; one row per key; money in USD; shares and rates as decimals, never percent strings; dates are quarter-end `datetime64`):

| table | key | columns (dtype) | source |
| :--- | :--- | :--- | :--- |
| `bdc_quarterly` | (`bdc_id`, `qdate`) | `nav_ps` float; `price` float or NaN (non-traded); `net_debt_to_equity` float; `w_na_cost`, `w_na_fv` float; `fv_total`, `cost_total` float; `pik_income`, `total_income` float; `first_lien_pct` float; `n_companies` int; `restated` bool | 10-Q/10-K, earnings releases |
| `soi` | (`bdc_id`, `qdate`, `facility_id`) | `borrower` str; `ice_id` str or None; `lien` in {1, 2, "unsecured", "equity"}; `spread_bp` float; `pik_flag` bool; `par`, `cost`, `fv` float; `maturity` date; `industry` str | schedules of investments (Chapter 25 parser) |
| `redemptions` | (`fund_id`, `qdate`) | `request_pct` float; `cap_pct` float (default 0.05); `fill_pct` float; `nav_total` float; `mode` in {"tender", "roc_distribution", "gated"} | 8-K, SC TO-I, N-23c-3 |
| `public_index` | `qdate` | `ll_excess_ret` float (quarterly; state it); `hy_excess_ret` float; `cdx_fin_spread_bp` float | vendor; Appendix B |

**Edge cases the robot must handle.** Non-calendar fiscal quarters (align to the nearest calendar quarter end and flag it). Restated NAVs (keep both vintages; never overwrite). `price` NaN for non-traded vehicles (P/NAV is undefined; never fill it with 1.0). `w_na_cost == 0` (return NaN, not infinity). The same facility held by several BDCs (join on `ice_id` when present, otherwise on fuzzy borrower name plus maturity plus spread). Percentages reported as strings such as "2.8%". The unit-sum constraint on $\theta$ (clip to $[0,1]$, renormalize, and report whether the clip bound).

**Numerical guards.** Require at least $10(K+1)$ observations for a Dimson regression with $K$ lags. Solve least squares by SVD (`lstsq`), not normal equations, because lagged factor returns are nearly collinear in calm regimes. Refuse to unsmooth with $\theta\ge0.9$ (noise amplification above $100\times$).

```python
# ---- Chapter 17 reference engine (mark_gap), block 1: the mark as a filter ----
import numpy as np
import pandas as pd


def simulate_smoothed(n, theta, beta=1.0, sigma_f=0.04, sigma_e=0.02, seed=17):
    """True quarterly excess return x_t = beta*F_t + e_t; reported x_obs_t = sum_k theta_k x_{t-k}.
    Returns (F, x_true, x_obs). The first K entries of x_obs are NaN (kernel not yet full)."""
    theta = np.asarray(theta, dtype=float)
    if theta.ndim != 1 or theta.size == 0 or np.any(theta < 0) or theta.sum() <= 0:
        raise ValueError("theta must be a non-empty vector of non-negative weights")
    theta = theta / theta.sum()                      # unit sum: marks eventually catch up
    K = theta.size - 1
    rng = np.random.default_rng(seed)
    F = rng.normal(0.0, sigma_f, n)
    x_true = beta * F + rng.normal(0.0, sigma_e, n)
    x_obs = np.full(n, np.nan)
    for t in range(K, n):
        x_obs[t] = float(np.dot(theta, x_true[t - K:t + 1][::-1]))   # theta_0 multiplies today
    return F, x_true, x_obs


def glm_moments(theta):
    """Closed-form GLM identities for a unit-sum kernel."""
    th = np.asarray(theta, dtype=float)
    th = th / th.sum()
    ss = float(np.dot(th, th))
    K = th.size - 1
    rho = np.array([np.dot(th[:-j], th[j:]) / ss for j in range(1, K + 1)])
    return {"var_ratio": ss, "rho": rho, "sharpe_inflation": 1.0 / np.sqrt(ss), "beta0_ratio": float(th[0])}


def autocorr(x, j):
    """Lag-j sample autocorrelation, ignoring NaNs at the start of the series."""
    x = np.asarray(x, dtype=float)
    x = x[~np.isnan(x)]
    x = x - x.mean()
    return float(np.dot(x[j:], x[:-j]) / np.dot(x, x))


def dimson_beta(x_obs, F, K):
    """Regress reported returns on current and K lagged factor returns. Returns (b_0..b_K, sum b_k)."""
    x_obs = np.asarray(x_obs, dtype=float)
    F = np.asarray(F, dtype=float)
    T = x_obs.size
    if T - K < 10 * (K + 1):
        raise ValueError("too few observations for K lags")
    rows, y = [], []
    for t in range(K, T):
        if np.isnan(x_obs[t]):
            continue
        rows.append([1.0] + [F[t - k] for k in range(K + 1)])
        y.append(x_obs[t])
    X, y = np.asarray(rows), np.asarray(y)
    coef, *_ = np.linalg.lstsq(X, y, rcond=None)
    return coef[1:], float(coef[1:].sum())


def kernel_from_dimson(b):
    """theta_hat_k = b_k / sum(b), clipped to [0, 1] and renormalised. Returns (theta_hat, clip_bound)."""
    b = np.asarray(b, dtype=float)
    s = b.sum()
    if abs(s) < 1e-12:
        raise ValueError("aggregate beta is ~0: the kernel is not identified")
    th = b / s
    clipped = bool(np.any(th < 0.0) or np.any(th > 1.0))
    th = np.clip(th, 0.0, 1.0)
    return th / th.sum(), clipped


def unsmooth_ar1(x_obs, theta):
    """Geltner inversion x_hat_t = (x_obs_t - theta x_obs_{t-1}) / (1 - theta)."""
    if not 0.0 <= theta < 0.9:
        raise ValueError("theta outside [0, 0.9): noise amplification too large")
    x = np.asarray(x_obs, dtype=float)
    out = np.full_like(x, np.nan)
    out[1:] = (x[1:] - theta * x[:-1]) / (1.0 - theta)
    return out


# --- sanity checks, block 1 ---
theta = (0.5, 0.3, 0.2)
mom = glm_moments(theta)
assert abs(mom["var_ratio"] - 0.38) < 1e-12
assert np.allclose(mom["rho"], [0.21 / 0.38, 0.10 / 0.38])
assert abs(mom["sharpe_inflation"] - 1.0 / np.sqrt(0.38)) < 1e-12

F, x_true, x_obs = simulate_smoothed(20_000, theta)
var_ratio = np.nanvar(x_obs) / np.var(x_true)
assert abs(var_ratio - 0.38) < 0.02, var_ratio                      # variance deflation
assert abs(autocorr(x_obs, 1) - mom["rho"][0]) < 0.03                 # mechanical momentum, lag 1
assert abs(autocorr(x_obs, 2) - mom["rho"][1]) < 0.03                 # lag 2
b0, agg0 = dimson_beta(x_obs, F, 0)
bK, aggK = dimson_beta(x_obs, F, 2)
assert abs(agg0 - 0.5) < 0.05, agg0                                   # contemporaneous beta = theta_0 * beta
assert abs(aggK - 1.0) < 0.05, aggK                                   # Dimson sum recovers beta
theta_hat, clip_bound = kernel_from_dimson(bK)
assert np.allclose(theta_hat, theta, atol=0.05) and not clip_bound

# Geltner: exact inversion of AR(1) smoothing, then noise amplification (1 + th^2) / (1 - th)^2
th1 = 0.6
x_ar = np.empty_like(x_true)
x_ar[0] = (1.0 - th1) * x_true[0]
for t in range(1, x_true.size):
    x_ar[t] = (1.0 - th1) * x_true[t] + th1 * x_ar[t - 1]
assert np.allclose(unsmooth_ar1(x_ar, th1)[1:], x_true[1:])
eta = np.random.default_rng(171).normal(0.0, 0.001, x_ar.size)
amp = np.var(unsmooth_ar1(x_ar + eta, th1)[1:] - x_true[1:]) / 0.001 ** 2
amp_theory = (1.0 + th1 ** 2) / (1.0 - th1) ** 2                     # = 8.5
assert abs(amp / amp_theory - 1.0) < 0.05, amp
print("block 1 ok: var ratio %.3f, rho1 %.3f, Dimson sum %.3f, noise amp %.1f"
      % (var_ratio, autocorr(x_obs, 1), aggK, amp))
```

**Why each check is there.** The variance ratio and the two autocorrelations are the closed-form identities; if the simulation disagrees, the kernel's time index is reversed (the most common bug: `theta[0]` multiplying the oldest return). The two Dimson runs show attenuation ($\theta_0\beta$) and recovery ($\sum_k b_k\to\beta$) in one picture. The Geltner pair shows that the inversion is exact on clean data and that it amplifies noise by the predicted factor on dirty data.

**Second-stage spec (text only).** `estimate_theta_panel(nav_returns_by_fund, F, K)` fits a shared MA($K$) kernel across funds by pooled OLS of $x^o_{i,t}$ on $F_{t-k}$ with fund fixed effects, following the Couts–Gonçalves–Rossi logic. It returns $\hat\theta_k=\hat b_k/\sum_l\hat b_l$ with a block bootstrap over quarters (block length 4), and it refuses to report a point estimate when the 90% interval for $\theta_0$ is wider than 0.4. ROBO will otherwise report $\hat\theta_0=0.47$ to three decimals from 22 observations, and someone will put it in a pitch book.

> **Ways This Blows Up.** (1) *The calm-regime collinearity trap.* In a quiet stretch, $F_t$, $F_{t-1}$ and $F_{t-2}$ are tiny and nearly collinear, the individual $\hat b_k$ swing wildly, and only their sum is stable; never trade a single lag coefficient. (2) *Breaks in the kernel.* Valuation policy changes when a new third-party valuer is hired or an auditor pushes back, and $\theta$ shifts with it. A kernel fitted on 2015–2021 will understate the speed of marks after an episode like 2026, when listed prices forced faster recognition. (3) *Asymmetric smoothing.* Managers mark gains and losses at different speeds (write-downs tend to arrive in lumps, recoveries gradually). A symmetric MA kernel then misreads a single large write-down as low $\theta$. Fit up-quarters and down-quarters separately before believing either.

### Deep-Dive Resource Graph

- **Academic Papers:** Getmansky, Lo and Makarov, "An Econometric Model of Serial Correlation and Illiquidity in Hedge Fund Returns" (NBER w9571, 2003; *Journal of Financial Economics*, 2004), https://www.nber.org/papers/w9571 ; Couts, Gonçalves and Rossi, "Unsmoothing Returns of Illiquid Funds," *Review of Financial Studies* 37(7), 2024; Dimson, "Risk Measurement When Shares Are Subject to Infrequent Trading," *Journal of Financial Economics* (1979); Scholes and Williams, "Estimating Betas from Nonsynchronous Data," *Journal of Financial Economics* (1977); Geltner, "Smoothing in Appraisal-Based Returns," *Journal of Real Estate Finance and Economics* (1991).
- **Practitioner Writing:** Asness, "The Illiquidity Discount?" AQR Perspectives (Dec 19, 2019), https://www.aqr.com/Insights/Perspectives/The-Illiquidity-Discount
- **Data & Code:** SEC EDGAR full-text search and APIs for BDC 10-Q schedules of investments, https://www.sec.gov/edgar

## 17.3 Marking the Unmarked: BDC P/NAV, Implied Markdowns and the Non-Accrual Gap

### 17.3.1 Desk framing: a listed CLO with the manager holding the pen

The BDC is the one place where a private loan book has a public price attached. Read it as Theo would read a capital structure. At the top sits a secured revolver from banks; bank loans are about 40% of BDC debt, up from about 20% a decade earlier, and the ten largest banks provide 82% of BDC commitments (Haque and Wang, FEDS Note, August 7, 2026). Below that sit unsecured notes, typically investment-grade rated and issued in \$300–\$400mm clips. At the bottom sits equity, listed for a public BDC and redeemable at NAV, subject to a cap, for a non-traded one. Since the 2018 change that let BDCs run 2:1 debt to equity, sector leverage has risen from about 0.4x to above 1x (Avalos, Doerr and Pinter, BIS Quarterly Review, March 2025).

Two features make it different from the CLOs of Chapter 21. First, the manager both selects and *marks* the collateral, and the NAV is the sum of those marks. Second, the equity pays a management fee on gross assets and an incentive fee on income. That fee stream is a claim senior to the shareholder in every state of the world, so even a perfectly marked BDC should trade below NAV unless the manager adds value. The listed equity is therefore a price on three things at once: the loans, the fees, and the market's opinion of the marks. The trick is to separate them.

Kaz, reading the latest 10-Q, wants to know whether a "tender offer" is an offer made gently. In a sense it is: it is the non-traded BDC's quarterly offer to buy back up to 5% of its shares at NAV, made politely, and suspended without much ceremony when something more important comes up, such as a merger.

### 17.3.2 Derivation: from a listed price to an implied asset markdown

**Notation.** In this section $P$ is the BDC's share price (not a bond price), NAV is book equity per share at reported marks, $A$ is total assets at reported fair value and $E$ is total NAV. We write leverage as $\ell=(A-E)/E$, net debt over NAV as the companies report it, rather than $L$, which this book reserves for loss given default. Then $A=E(1+\ell)$.

**Assumptions.** (i) The market values the loan book at $A(1-m)$, where $m\ge0$ is the implied markdown as a fraction of reported asset value. (ii) The equity also bears a structural fee drag with present value $\phi E$ (base and incentive fees capitalized at the equity's required return, net of any value the manager adds). (iii) The debt is money-good. Then market equity is assets at market, minus debt, minus fees:

$$
P\cdot\text{shares}=A(1-m)-(A-E)-\phi E=E-mA-\phi E .
$$

Divide by $E$ and substitute $A=E(1+\ell)$:

$$
\frac{P}{\text{NAV}}=(1-\phi)-m(1+\ell)
\qquad\Longrightarrow\qquad
m=\frac{(1-\phi)-P/\text{NAV}}{1+\ell}.
$$

The factor $1/(1+\ell)$ is the leverage translation: at $\ell=1.1$, each point of equity discount maps to only $0.48$ points of asset markdown. A 20% equity discount is not a claim that the loans are worth 80. It is a claim that they are worth about 90.

**Numbers.** Blue Owl Capital Corporation (OBDC) bought back about \$148mm of its own stock in the fourth quarter of 2025 at "86% of price-to-book value," with net debt to equity of 1.19x (company release, February 18, 2026). With an illustrative fee drag $\phi=0.05$, $m=(0.95-0.86)/2.19=4.1\%$ of assets. Octus reported on April 16, 2026 that BDCs traded "at nearly a 20% discount to net asset value, with certain large names approaching a 50% discount." At $P/\text{NAV}=0.80$ and an illustrative $\ell=1.1$, $m=(0.95-0.80)/2.1=7.1\%$; at $0.50$, $m=(0.95-0.50)/2.1=21.4\%$. The second number is the market saying that a book the manager carries at 98–100 is worth about 78. A widely reported tally put the median listed BDC at about 0.74 times *forward* NAV at the end of March 2026 (Reuters/LSEG; not independently verified for this edition), which maps to $m\approx10\%$.

**Boundary conditions.** If $P/\text{NAV}>1-\phi$, the formula returns $m<0$. Floor it at zero and attribute the premium to franchise value: net investment income in excess of the dividend, a lower-cost internal management structure, or a growing fee base. Main Street Capital, an internally managed BDC, has historically traded well above NAV, and nobody believes its loans are worth more than par. If the debt is *not* money-good, relax assumption (iii): equity becomes a call option on $A(1-m)$ struck at the debt, worth more than its intrinsic value, so a given price is consistent with a *larger* $m$. The money-good formula is then a lower bound on the markdown. That Merton-on-a-CLO extension, and the $\mathbb{Q}$-measure link to BDC CDS spreads, belongs to Chapter 23. Do not mix a $\mathbb{Q}$ spread with this $\mathbb{P}$ markdown without saying so.

### 17.3.3 Derivation: the non-accrual gap and the implied carrying value of bad loans

BDCs report non-accrual loans as a share of the portfolio at **cost** and at **fair value**. That pair of numbers hides a mark. Let $w^{C}_{\text{NA}}$ and $w^{FV}_{\text{NA}}$ be the two shares, and $C$ and $FV$ the whole portfolio's cost and fair value. The non-accrual bucket's cost is $w^C_{\text{NA}}C$ and its fair value is $w^{FV}_{\text{NA}}FV$, so its carrying value as a fraction of cost is

$$
\hat R^{\text{mark}}_{\text{NA}}=\frac{w^{FV}_{\text{NA}}\cdot FV}{w^{C}_{\text{NA}}\cdot C}=\frac{w^{FV}_{\text{NA}}}{w^{C}_{\text{NA}}}\cdot\frac{FV}{C}.
$$

The superscript is a warning: this is a *mark*, not a realized recovery. Compare it with Chapter 14's realized-recovery distributions, not with the manager's talking points. Alongside it, track the **gap series** $g_t=w^C_{\text{NA},t}-w^{FV}_{\text{NA},t}$, the share of cost sitting in loans that are no longer paying and have been written down. A rising $g_t$ with a falling $w^{FV}_{\text{NA},t}$ is the signature of new non-accruals arriving already heavily marked down: the headline (fair-value) number improves while the hole gets deeper.

OBDC's own releases give a clean four-quarter series *(company releases; FV/C of 0.98 is approximate and applied uniformly, so the implied marks are illustrative)*:

| Quarter end | NAV/share | Non-accrual at cost | at FV | Gap $g_t$ | $\hat R^{\text{mark}}_{\text{NA}}$ | Net D/E |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| Sep 30, 2025 | \$14.89 | 2.7% | 1.3% | 1.4pp | 0.47 | 1.22x |
| Dec 31, 2025 | \$14.81 | 2.3% | 1.1% | 1.2pp | 0.47 | 1.19x |
| Mar 31, 2026 | \$14.41 | 2.0% | 1.0% | 1.0pp | 0.49 | 1.13x |
| Jun 30, 2026 | \$14.26 | 2.8% | 0.8% | 2.0pp | 0.28 | 1.11x |

In the second quarter of 2026 the fair-value non-accrual rate fell to its lowest level in the series while the cost rate jumped, and the implied carrying value of the bad bucket fell from about 49 cents to about 28. On the same day the industry was quoting 70-cent recoveries, Octus estimated private-credit restructuring recoveries at "approximately 50 cents on the dollar," "well below the 70% previously cited by many managers" (Octus, April 16, 2026). The mark was moving toward the evidence; it just moved at the speed of the kernel.

Octus also put a number on the cross-holder problem. Adjusting for loans held by several BDCs raised sector non-accruals from 1.45% to 2.18% of cost, and it found "pricing gaps of nearly 40 points as measured by fair value divided by par" in widely held stressed loans. Two managers, one loan, forty points apart. One of them is wrong, and the listed price of each BDC is a vote on which.

> **[SOURCE EXTRACTION]** *Ben_Dor_Quantitative_Credit_Portfolio_Management p.208:* "all bonds comprising the Corporate and High Yield indexes with a sequence of five or more unchanged quotes in any month are excluded from the eligible population of bonds for that month."
>
> **Annotation.** For public index research, a run of unchanged quotes means the price is stale and the observation is discarded. On a schedule of investments the same rule becomes a *signal*: a facility marked at the same fair value over par for five consecutive quarters, while its public comparables and its co-holders' marks moved, is a mark that has not been looked at. Those are the candidates for mark convergence, and they cluster in vehicles whose other marks are also slow. The desk departs from Ben Dor in what it does with the flag. It does not drop the observation; it adds it to the vehicle's stale-mark share, a per-BDC feature in the §17.9 relative-value model.

### Case Study: OBDC and OBDC II, November 2025 to August 2026: Same Loans, Three Prices

This is the natural experiment of the cycle, and every number below is from Blue Owl's own releases unless marked.

**The setup (November 5, 2025).** Blue Owl proposed to merge OBDC II, a non-traded BDC, into OBDC, its listed sibling. The portfolios overlapped by about 98%. The exchange was NAV for NAV if OBDC traded at or below NAV, which meant OBDC II holders, who could tender at NAV, would receive listed shares worth less than NAV at market. OBDC II suspended its tender offers pending the close. Same loans, same manager, same marks: the only thing the merger changed was the wrapper, and the wrapper was worth a discount.

**The unwind (November 19, 2025).** Fourteen days later the merger was terminated: "we are no longer pursuing the merger at this point given current market conditions." OBDC II would reinstate tenders in the first quarter of 2026, subject to board approval; the release noted that "every quarterly tender since inception has been fully satisfied." It did not mention the share price or the exchange ratio, which were the whole story.

**Three prices in one quarter (February 18, 2026).** OBDC reported fourth-quarter NAV of \$14.81 and buybacks at 86% of book. That is the first price: the listed market, at 0.86 of the marks. The marks themselves are the second price, at roughly 1.00 of book by definition. The third price was a transaction. The same day, three Blue Owl BDCs agreed to sell \$1.4 billion of partial interests in loans to 128 companies (97% senior secured, average position about \$5mm, internet software and services the largest industry at 13%) to four North American pension and insurance investors. "The investments will be sold at fair value, which is equivalent to 99.7% of par value as of February 12, 2026." OBDC II's \$600mm share, about 34% of its commitments including unfunded ones, funded a return-of-capital distribution of up to \$2.35 per share, about 30% of NAV and "about six times" a planned 5% tender. Its board said it would use quarterly return-of-capital distributions instead of tender offers from then on. *(Cooperation agreements signed in this chapter: 0. Return-of-capital distributions substituted for tender offers: 1.)*

**Reading it with the engine.** §17.3.2 turns 0.86 into an implied markdown of about 4% of assets. §17.3.3 turns the June 2026 non-accrual pair into a 28-cent carrying value on the bad bucket. And the \$1.4 billion print says that *good* loans clear at par, which is exactly what adverse selection in a partial-interest sale predicts. A seller who needs liquidity sells the slices a pension fund will buy, the buyer chooses what it is willing to own, and the clearing price on the chosen slices says nothing about the ones left behind. Ines would call it showing your best two cards to prove your hand is strong.

**How a systematic desk would have traded it.** Into the merger announcement: short OBDC against a diversified basket of listed BDCs, on the view that a NAV-for-NAV exchange with OBDC below NAV transferred value away from OBDC II holders, who would resist it, and that resistance would come out of the listed price; cover on termination. Through the first quarter of 2026: long OBDC unsecured notes against short OBDC equity, because deleveraging from 1.22x to 1.11x and asset sales at par are good for bondholders and neutral at best for equity. Throughout: watch the redemption queues of Blue Owl's other non-traded vehicles as the leading indicator of further sales (§17.6). Ines replays the hand through markouts: the trade that paid was the one that read the merger terms as a statement about the marks.

```python
# ---- block 2: from listed prices and disclosures to implied marks ----
def implied_markdown(p_nav, lev, fee_drag=0.0):
    """m = ((1 - phi) - P/NAV) / (1 + ell), floored at 0. NaN for a non-traded vehicle."""
    if p_nav is None or np.isnan(p_nav):
        return np.nan
    if lev < 0 or not 0.0 <= fee_drag < 1.0:
        raise ValueError("leverage must be >= 0 and fee_drag in [0, 1)")
    return max(((1.0 - fee_drag) - p_nav) / (1.0 + lev), 0.0)


def implied_nonaccrual_mark(w_fv, w_cost, fv_over_cost=1.0):
    """Carrying value of the non-accrual bucket as a fraction of its cost (a mark, not a recovery)."""
    if w_cost <= 0:
        return np.nan
    return (w_fv / w_cost) * fv_over_cost


def cross_holder_dispersion(soi):
    """Per facility held by >= 2 vehicles: number of holders, mean, std and range of fv/par."""
    df = soi.assign(px=soi["fv"] / soi["par"])
    g = df.groupby("facility_id")["px"]
    out = pd.DataFrame({"n_holders": g.size(), "px_mean": g.mean(),
                        "px_std": g.std(ddof=0), "px_range": g.max() - g.min()})
    return out[out["n_holders"] >= 2]


def stale_mark_flag(px_by_quarter, n_unchanged=5, tol=1e-4):
    """True where a facility's mark has been unchanged (within tol) for n_unchanged consecutive quarters."""
    px = np.asarray(px_by_quarter, dtype=float)
    run, flags = 1, []
    for t in range(px.size):
        run = run + 1 if (t > 0 and abs(px[t] - px[t - 1]) <= tol) else 1
        flags.append(run >= n_unchanged)
    return np.array(flags)


obdc = pd.DataFrame({
    "qdate": pd.to_datetime(["2025-09-30", "2025-12-31", "2026-03-31", "2026-06-30"]),
    "nav_ps": [14.89, 14.81, 14.41, 14.26],
    "w_na_cost": [0.027, 0.023, 0.020, 0.028],
    "w_na_fv": [0.013, 0.011, 0.010, 0.008],
    "net_de": [1.22, 1.19, 1.13, 1.11],
}).set_index("qdate")
obdc["gap_pp"] = 100.0 * (obdc["w_na_cost"] - obdc["w_na_fv"])
obdc["na_mark"] = [implied_nonaccrual_mark(f, c, 0.98) for f, c in zip(obdc["w_na_fv"], obdc["w_na_cost"])]

# --- sanity checks, block 2 ---
assert abs(implied_markdown(0.86, 1.19, 0.05) - 0.0411) < 1e-3      # OBDC Q4 2025 buyback print
assert abs(implied_markdown(0.50, 1.10, 0.05) - 0.2143) < 1e-3      # a name near a 50% discount
assert implied_markdown(1.02, 1.0, 0.05) == 0.0                      # premium name: floor, not negative
assert np.isnan(implied_markdown(np.nan, 0.9))                       # non-traded: undefined, never 1.0
assert np.isnan(implied_nonaccrual_mark(0.0, 0.0))
assert abs(obdc["na_mark"].iloc[-1] - 0.28) < 0.005                  # ~28c on the bad bucket, Jun 2026
assert abs(obdc["gap_pp"].iloc[1] - 1.2) < 1e-9 and abs(obdc["gap_pp"].iloc[-1] - 2.0) < 1e-9

soi_toy = pd.DataFrame({                                             # illustrative holdings
    "facility_id": ["A", "A", "A", "B", "B", "C"],
    "bdc_id": ["X", "Y", "Z", "X", "Y", "Z"],
    "par": [10.0, 25.0, 5.0, 8.0, 12.0, 3.0],
    "fv": [9.8, 14.5, 4.6, 7.92, 11.88, 2.9],
})
disp = cross_holder_dispersion(soi_toy)
assert list(disp.index) == ["A", "B"]                                # C has a single holder
assert abs(disp.loc["A", "px_range"] - 0.40) < 1e-9                  # a 40-point same-loan gap
assert disp.loc["B", "px_range"] < 1e-9
assert stale_mark_flag([0.97, 0.97, 0.97, 0.97, 0.97, 0.95]).tolist() == [False] * 4 + [True, False]
print(obdc[["gap_pp", "na_mark"]].round(3))
```

> **Ways This Blows Up.** (1) *Gross versus net leverage.* Use net debt to NAV as reported, and say so; gross leverage overstates $\ell$ and understates $m$. (2) *Forward versus trailing NAV.* Price-to-forward-NAV and price-to-last-reported-NAV differ by a quarter of markdowns, which in 2026 was most of the signal. (3) *Buybacks.* Repurchases below NAV are accretive: they mechanically raise NAV per share, so $P/\text{NAV}$ can fall while NAV rises. OBDC's buyback was, technically, an open market purchase, the most expensive three words in finance, deployed here to make money for the holders who stayed. Adjust NAV per share for the accretion before computing $m$. (4) *Off-balance-sheet claims.* Unfunded commitments are not in $A$ but are a call on liquidity; joint ventures and preferred equity sit between debt and equity and break the two-layer algebra. (5) *Fee drag is not a constant.* The incentive fee falls away when income approaches the hurdle, so $\phi$ shrinks exactly in stress; holding it fixed overstates $m$ in bad quarters.

### Deep-Dive Resource Graph

- **Practitioner Writing:** Octus, "BDCs Trading at 50% Discount to NAV but Nonaccruals Ticking Downward" (Apr 16, 2026), https://octus.com/resources/blog/bdcs-trading-at-50-discount-to-nav-but-nonaccruals-ticking-downward/ ; Blue Owl Capital Corporation press releases (merger termination, Nov 19, 2025; \$1.4B asset sale and Q4 2025 results, Feb 18, 2026), https://www.blueowlcapitalcorporation.com/investors/news-events/press-releases
- **Academic Papers:** Haque and Wang, "The Price of Bank Funding behind Private Credit: Evidence from Business Development Companies," FEDS Note (Aug 7, 2026), https://www.federalreserve.gov/econres/notes/feds-notes/the-price-of-bank-funding-behind-private-credit-evidence-from-business-development-companies-20260807.html ; Fillat, Landoni, Levin and Wang, Boston Fed CPP 25-8 (May 21, 2025), https://www.bostonfed.org/publications/current-policy-perspectives/2025/could-the-growth-of-private-credit-pose-a-risk-to-financial-system-stability.aspx
- **Data & Code:** SEC EDGAR (10-Q/10-K schedules of investments; 8-K earnings exhibits), https://www.sec.gov/edgar

## 17.4 Two-Way Takeouts: PC↔BSL Migration as a Regime-Conditional Flow

### 17.4.1 Desk framing: the border moves, and a public variable moves it

If the two markets share one borrower pool, the interesting question is which way borrowers are crossing the border this quarter, and why. The Fed's 2026 substitution study gives the cleanest answer available. It dates a "tight leveraged-loan" regime from the syndicated market's excess loan premium, the part of loan spreads not explained by fundamentals, and finds it ran from May 2022 to September 2024. Inside that window, switching from leveraged loans to private credit peaked at about half of leveraged-loan borrowers in early 2023 (Banegas et al., August 11, 2026). Lenders call a syndicated borrower refinanced into a unitranche a "steal," and KBRA's count of steals has risen steadily since 2019. When syndicated spreads compressed in 2024, the flow reversed: takeouts in both directions were "considerably balanced" through the first nine months of 2025 (BlackRock *Private Credit Primer*, January 2026, citing LCD and KBRA).

This is RSSG home ground. Theo has run dual-track processes, a syndicated deal and a private club working in parallel with the sponsor choosing at the end, and he knows the choice turns on certainty of execution as much as spread. The quant upgrade is to stop treating each choice as a story and start treating the population of choices as a flow with a forecastable rate. That flow matters to a public desk for a concrete reason: **a private-to-syndicated takeout is new supply of syndicated loans**, and syndicated loan supply is the denominator of every CLO-demand and repricing model in Chapter 21.

### 17.4.2 Derivation: competing exits with a regime covariate

**Setup.** Each private loan $i$ outstanding at time $t$ can leave the private book in one of four ways: refinanced into the syndicated market ($B$), refinanced by another private lender ($P$), amended and extended ($X$), or defaulted. To respect the book's notation, we write the three non-default exit hazards as $\kappa^{(j)}_i(t)$ for $j\in\{B,P,X\}$ and keep $\lambda_i(t)$ for default. Hazards are annualized, so here $t$ is in years and a quarter is $\Delta t=1/4$. Cause-specific proportional hazards with a public regime covariate $\zeta_t$ (the excess loan premium, standardized, or its sign relative to its median) and the private-minus-syndicated spread differential $\Delta s_t$ (in percentage points) give

$$
\kappa^{(j)}_i(t)=\kappa^{(j)}_0\exp\!\big(\psi_j\,\zeta_t+\chi_j\,\Delta s_t+\boldsymbol{\omega}_j^{\top}\mathbf{v}_i\big),\qquad j\in\{B,P,X\},
$$

with the same form for $\lambda_i(t)$, where $\mathbf{v}_i$ holds borrower covariates (log size, software flag, credit estimate, sponsor, years to maturity). The signs the theory predicts are $\psi_B<0$ (a tight syndicated market slows takeouts into it), $\chi_B>0$ (a wider private premium pulls borrowers toward the syndicated market) and a positive size loading for $B$ (only larger borrowers can clear a syndicated book).

**Exit probabilities over a quarter.** Hold hazards constant over $[t,t+\Delta t]$ and let $\mathcal{K}_i=\kappa^{(B)}_i+\kappa^{(P)}_i+\kappa^{(X)}_i+\lambda_i$ be the total exit hazard. The loan survives to time $u$ with probability $e^{-\mathcal{K}_iu}$, and conditional on surviving to $u$ it exits via $B$ in $[u,u+du)$ with probability $\kappa^{(B)}_i\,du$. Integrating,

$$
\mathbb{P}\big(\text{exit via }B\text{ in }\Delta t\big)=\int_0^{\Delta t}\kappa^{(B)}_i\,e^{-\mathcal{K}_iu}\,du=\frac{\kappa^{(B)}_i}{\mathcal{K}_i}\Big(1-e^{-\mathcal{K}_i\Delta t}\Big).
$$

The expected syndicated supply from private takeouts over the next quarter is then

$$
Q^{P\to B}_{t+\Delta t}=\sum_{i\in\text{PC}}\text{Face}_i\cdot\frac{\kappa^{(B)}_i}{\mathcal{K}_i}\Big(1-e^{-\mathcal{K}_i\Delta t}\Big).
$$

**Why the competition term matters.** The naive estimate $\text{Face}_i\,(1-e^{-\kappa^{(B)}_i\Delta t})$ ignores the other exits. Since $g(y)=(1-e^{-y})/y$ is decreasing in $y>0$ and $\mathcal{K}_i\ge\kappa^{(B)}_i$,

$$
\frac{\kappa^{(B)}_i}{\mathcal{K}_i}\Big(1-e^{-\mathcal{K}_i\Delta t}\Big)=\kappa^{(B)}_i\Delta t\;g(\mathcal{K}_i\Delta t)\;\le\;\kappa^{(B)}_i\Delta t\;g(\kappa^{(B)}_i\Delta t)=1-e^{-\kappa^{(B)}_i\Delta t}.
$$

The naive number always overstates supply, and it overstates most in exactly the stressed regime where amend-and-extend and default hazards are high. A loan that gets amended into PIK this quarter cannot also be refinanced into a CLO.

**Assumptions and error-prone spots.** Hazards are proportional within a regime, and the exit cause is observed with a lag (announcements, not closings). Estimate each cause-specific hazard by partial likelihood, treating the other exits as censoring. Four things go wrong in practice. First, the regime variable is itself estimated and revised, so use the vintage available at $t$. Second, dual-track processes mean the cause is only known ex post; a process that starts as a syndication and ends as a unitranche is a $P$ exit that looked like a $B$ exit for six weeks. Third, the Fed's tight regime is *one* episode, so $\psi_j$ is a two-regime estimate with wide intervals. Fourth, the data are messier than the math: an exit appears on a BDC's schedule of investments as a facility that has vanished, and matching it to a new syndicated loan requires the borrower-name join of §17.2's schema.

### Case Study: Finastra 2023, the Steal, and the 2024 Reversal

On September 14, 2023, Kirkland & Ellis announced that it had advised Finastra, "a Vista Equity Partners portfolio company," on "a \$4.82 billion senior secured unitranche term loan facility" and "a \$500 million senior secured multicurrency revolving credit facility," used for "the refinancing of its existing credit facilities," with "more than twenty lenders and borrowers in multiple jurisdictions" (Kirkland release, September 14, 2023). The facilities being refinanced had been raised in the US and European syndicated loan markets. That is a steal of textbook size, and it was widely reported at the time as the largest private credit loan to date (KBRA DLD via press reports; not independently verified for this edition, nor were the lender names).

Put it on the regime clock. September 2023 sits in the middle of the Fed's tight window, when the excess loan premium was high and the syndicated market was charging for uncertainty as much as for credit. A software borrower with a large, aging capital structure could get certainty and size from a club of private lenders at a spread the syndicated market could not reliably match. The model's $\psi_B<0$ and $\psi_P>0$ are the formal version of that sentence.

Then the regime flipped. When syndicated spreads compressed through 2024, borrowers ran dual tracks and refinanced in both directions, and by 2024–9M2025 the takeouts were roughly balanced. A desk that carried the excess loan premium as a live input would have forecast both waves: the 2023 drain of syndicated supply into private credit, which supported CLO loan prices by shrinking the pool, and the 2024 return flow, which added supply just as CLO issuance was strong. **How to trade it:** the takeout forecast is a supply forecast. Ahead of a predicted private-to-syndicated wave, lean against repricing-sensitive loan prices and CLO equity, whose arbitrage depends on scarce collateral, and toward CLO senior tranches, which benefit from more issuance at tight liability spreads. Chapter 21 owns the CLO side; this section owns the supply number.

```python
# ---- block 3: PC <-> BSL migration as competing risks ----
EXITS = ("to_bsl", "to_pc", "amend_extend", "default")


def cause_specific_hazards(base, psi, chi, omega, zeta, ds, V):
    """Annualised hazards kappa_ij = base_j * exp(psi_j*zeta + chi_j*ds + V_i @ omega_j).
    base, psi, chi: (J,); omega: (p, J); V: (n, p); zeta and ds are scalars. Returns (n, J)."""
    base, psi, chi = (np.asarray(a, dtype=float) for a in (base, psi, chi))
    V = np.atleast_2d(np.asarray(V, dtype=float))
    omega = np.asarray(omega, dtype=float)
    if np.any(base < 0):
        raise ValueError("baseline hazards must be non-negative")
    lin = zeta * psi + ds * chi + V @ omega
    return base * np.exp(np.clip(lin, -30.0, 30.0))          # clip guards exp overflow


def exit_probabilities(kappa, dt=0.25):
    """Constant competing hazards over dt years: P(exit via j) = kappa_j / K * (1 - exp(-K dt)).
    Returns (n, J + 1): exit probabilities by cause, then P(still outstanding)."""
    kappa = np.atleast_2d(np.asarray(kappa, dtype=float))
    if np.any(kappa < 0):
        raise ValueError("hazards must be non-negative")
    tot = kappa.sum(axis=1, keepdims=True)
    p_any = 1.0 - np.exp(-tot * dt)
    with np.errstate(invalid="ignore", divide="ignore"):
        share = np.where(tot > 0, kappa / tot, 0.0)
    return np.hstack([share * p_any, 1.0 - p_any])


def bsl_supply(face, kappa, dt=0.25, naive=False):
    """Expected face refinanced from private credit into the BSL market over the next dt years."""
    face = np.asarray(face, dtype=float)
    kappa = np.atleast_2d(np.asarray(kappa, dtype=float))
    if naive:                                                  # ignores competing exits: overstates
        return float(face @ (1.0 - np.exp(-kappa[:, 0] * dt)))
    return float(face @ exit_probabilities(kappa, dt)[:, 0])


# --- sanity checks, block 3 (all parameters illustrative) ---
rng3 = np.random.default_rng(2023)
n_loans = 400
V = np.column_stack([rng3.normal(0.0, 0.5, n_loans),                  # log size vs median borrower
                     (rng3.random(n_loans) < 0.21).astype(float)])     # software flag
face = 150.0 * np.exp(V[:, 0])                                         # $mm
base = np.array([0.12, 0.08, 0.06, 0.02])
psi = np.array([-0.8, 0.3, 0.4, 0.2])          # tight-LL regime (zeta = +1) slows takeouts into BSL
chi = np.array([0.5, -0.2, 0.0, 0.0])          # wider PC-minus-BSL spread (pp) pulls loans into BSL
omega = np.array([[0.6, -0.2, 0.0, 0.0],       # size: bigger borrowers can reach the BSL market
                  [-0.3, 0.1, 0.3, 0.4]])      # software: harder to syndicate, more A&E, more default
kap_loose = cause_specific_hazards(base, psi, chi, omega, zeta=-1.0, ds=1.0, V=V)
kap_tight = cause_specific_hazards(base, psi, chi, omega, zeta=+1.0, ds=1.0, V=V)
probs = exit_probabilities(kap_loose)
assert probs.shape == (n_loans, 5) and np.allclose(probs.sum(axis=1), 1.0)
assert abs(exit_probabilities([[0.2, 0.0, 0.0, 0.0]])[0, 0] - (1.0 - np.exp(-0.05))) < 1e-12
assert np.allclose(exit_probabilities([[0.0, 0.0, 0.0, 0.0]]), [[0.0, 0.0, 0.0, 0.0, 1.0]])
s_loose, s_tight = bsl_supply(face, kap_loose), bsl_supply(face, kap_tight)
assert s_tight < s_loose                                               # the regime turns the tap
assert bsl_supply(face, kap_loose, naive=True) >= s_loose              # ignoring competition overstates
print("expected PC->BSL supply next quarter ($mm, illustrative): loose %.0f, tight %.0f" % (s_loose, s_tight))
```

### Deep-Dive Resource Graph

- **Practitioner Writing:** Kirkland & Ellis press release on the Finastra \$5.3 billion refinancing (Sep 14, 2023), https://www.kirkland.com/news/press-release/2023/09/kirkland-advises-finastra-group-on-53-billion-refinancing ; BlackRock, *Private Credit Primer* (Jan 2026), https://www.blackrock.com/gls-download/literature/market-commentary/private-credit-primer-january-2026.pdf
- **Academic Papers:** Banegas et al., FEDS Note (Aug 11, 2026), as in §17.1; for the estimation machinery, any graduate survival-analysis text on cause-specific hazards and the Fine–Gray subdistribution alternative (Fine and Gray, *Journal of the American Statistical Association*, 1999).
- **Data & Code:** PitchBook LCD and KBRA DLD (subscription) for steals and takeouts; BDC schedules of investments on EDGAR for exits.

## 17.5 Banks Moved Up the Stack, Insurers Moved Down the Funnel

### 17.5.1 Desk framing: nobody left; everybody changed seats

The story told in 2021 was that private credit was eating the banks' lunch. The flow graph says the banks moved to a different seat at the same table. Committed bank lines to private-credit vehicles were about \$95 billion at the end of 2024, \$56 billion drawn, up 145% in five years, with about 60% at five global systemically important banks (Berrospide, Cai, Lewis-Hayre and Zikes, FEDS Note, May 23, 2025). Of bank exposure to BDCs reported in the Fed's Y-14 data, 97% is first-lien senior secured, and every public BDC borrowed from at least one Y-14 bank over 2013–2023 (Boston Fed CPP 25-8). The bank is the AAA tranche of a CLO-shaped stack, paid a fee to originate and a spread to sit on top.

That seat is not free of risk, but the risk is mostly the BDC's. In the 2022 tightening, banks charged BDCs about 1.1 percentage points more than matched borrowers with the same bank, quarter and internal rating, and BDC line utilization rose 14.2 points more (Haque and Wang, August 7, 2026). The line gets more expensive exactly when the BDC draws on it. For the banks themselves, a \$36 billion drawdown shock costs only about 2bp of aggregate CET1 (Berrospide et al.). Read those two facts together and the bank revolver is a liquidity put the BDC bought, struck where the bank chooses, repriced when exercised.

> **Trend Watch.** *The bank–private credit partnership wave, 2023–2026.* September 26, 2024: Citi and Apollo announce a \$25 billion private credit and direct lending program, "initially in North America," with Mubadala as a strategic partner and Athene participating, and "the flexibility to significantly expand the size of the program beyond the initial \$25 billion" (Citi press release). February 24, 2025: J.P. Morgan raises its direct-lending balance-sheet commitment to \$50 billion plus "nearly \$15 billion from multiple co-lenders," having deployed "over \$10 billion across more than 100 private credit transactions" since 2021 (J.P. Morgan release). May 2025: committed bank lines to private-credit vehicles reach about \$95 billion (Fed). May 8, 2026: bank commitments to nonbank financial institutions total \$2.6 trillion, with private equity, BDCs and private credit the largest category after a \$261 billion upward revision (Fed *Financial Stability Report*). August 7, 2026: bank loans are about 40% of BDC debt, double their share a decade earlier (Haque and Wang). **What it means for the desk:** a "partnership" is an origination-and-distribution agreement plus a senior tranche, not a retreat. Model it as an edge in the forced-seller graph that runs both ways: banks feed loans into private vehicles at origination and pull liquidity back out through line pricing and borrowing-base haircuts in stress.

### Case Study: Two Bank Partnerships, Read as Term Sheets

Theo reads the two announcements the way he would read a commitment letter, looking for what is *not* said. The Citi release specifies a size, a geography and the participants, and it promises "to significantly enhance access for corporate and sponsor clients to the private lending capital pool." It says nothing about who holds which risk. The J.P. Morgan release says that "additional details around the co-lending arrangements have not been disclosed." Its most informative line is Jamie Dimon's: "We proudly bank 80,000 companies globally through our Commercial and Investment Bank." That is the origination funnel. The bank's edge in private credit is not its balance sheet; it is that it already sees the borrowers' cash management, revolvers and M&A plans, and can route each one to whichever pocket (syndicated, balance sheet, partner fund) pays best. For the competing-risks model of §17.4 this is a covariate: a borrower whose relationship bank runs a direct-lending program has a higher $\kappa^{(P)}$ and a bank-aligned choice of exit.

### 17.5.2 Insurers: the capital funnel and the ratings passport

Insurers sit lower in the funnel and buy the middle of the stack. Packaging middle-market loans into a CLO or BDC structure can cut the risk-based capital charge on the same underlying loans by about ten times; insurers with affiliated CLO or BDC managers control \$4.1 trillion, 72% of industry general-account assets; and affiliated BDCs hold more than \$100 billion, about 40% of BDC assets (Carlino, Foley-Fisher, Heinrich and Verani, FEDS Note, March 21, 2025). The passport that makes the capital arithmetic work is the private letter rating, which feeds an NAIC designation through the filing-exemption process.

That passport is now being inspected. In 2024 the NAIC "authorized regulators to challenge or override NAIC Designations assigned through the filing exemption process" (NAIC private credit resource page). By August 13, 2026 its working group reported that the "ability to implement discretion over NAIC Designations assigned through the Filing Exemption Process is operational," with an amendment on the treatment of CLOs exposed for comment through September 14, 2026 (NAIC IDAWG summary). FactSet's analysis of statutory filings found that "at year-end 2025, 19.7% of all filings were unresolved," that "private investments reached 38.7% of corporate bond holdings in 2024," and that new reporting Item 2025-19, effective December 31, 2026, "will require insurers to quantify every private placement on their books" supported only by private ratings (Johnson, FactSet Insight, May 29, 2026).

Mags has seen this movie. "Back in my day the rating agencies were paid by the issuer and everybody pretended that was fine. Now the rating is private, the issuer pays, and nobody even has to pretend. The regulator showing up to check is the first new idea in thirty years." Grudging respect: it is a good idea. **For a public desk it is a calendar.** If designation challenges or the CLO amendment push capital charges up, insurers will rotate out of privately rated paper and middle-market CLO mezzanine and into public BBB and BB credit. That is a forced flow with dates attached, which is the only kind of flow a systematic desk should pre-position for.

### Deep-Dive Resource Graph

- **Practitioner Writing:** Citi, "Citi and Apollo Announce \$25 Billion Private Credit, Direct Lending Program" (Sep 26, 2024), https://www.citigroup.com/global/news/press-release/2024/citi-and-apollo-announce-25-billion-private-credit-direct-lending-program ; J.P. Morgan, "JPMorgan Increases Direct Lending Commitment to \$50 Billion" (Feb 24, 2025), https://www.jpmorgan.com/about-us/corporate-news/2025/jpmorgan-increases-direct-lending-commitment-to-50-billion ; Johnson, "Almost One-Fifth of Insurer-Held Private Securities Are Not Rated, but Disclosure Is Changing," FactSet Insight (May 29, 2026), https://insight.factset.com/almost-one-fifth-of-insurer-held-private-securities-are-not-rated-but-disclosure-is-changing
- **Academic Papers:** Berrospide, Cai, Lewis-Hayre and Zikes, FEDS Note (May 23, 2025), https://www.federalreserve.gov/econres/notes/feds-notes/bank-lending-to-private-credit-size-characteristics-and-financial-stability-implications-20250523.html ; Carlino, Foley-Fisher, Heinrich and Verani, FEDS Note (Mar 21, 2025), https://www.federalreserve.gov/econres/notes/feds-notes/life-insurers-role-in-the-intermediation-chain-of-public-and-private-credit-to-risky-firms-20250321.html
- **Data & Code:** NAIC private credit resource center, https://content.naic.org/resource-center/private-credit-insurance-regulation

## 17.6 Semi-Liquid Vehicles and the Redemption Game

### 17.6.1 Desk framing: the failure mode moved from defaults to redemptions

Retail money became the marginal private-credit dollar. Semi-liquid vehicles (perpetual non-traded BDCs and interval funds) held about \$425 billion gross and \$241 billion net by the Fed's May 2026 count, about one-fifth of private credit's net AUM, and in the first quarter of 2026 accepted redemptions exceeded inflows for the first time (Fed *Financial Stability Report*, May 8, 2026). Non-traded BDCs hold about 0.2% of assets in short-term liquid instruments, with debt to equity of 0.90 (George and Shin, October 14, 2026). Their liquidity is not cash. It is bank lines, loan repayments and a sleeve of syndicated loans held to be sold.

That changes what can go wrong. A drawdown fund with ten-year locked capital fails, if it fails, through defaults. A semi-liquid fund that promises quarterly repurchases at NAV can fail through *redemptions* while its loans perform, because the NAV it pays out is smoothed and everyone knows it. The IMF put the mechanism precisely: slow-moving valuations create a first-mover advantage, and discretionary gating "may erode investor confidence across the broader industry" (IMF *Global Financial Stability Report*, April 2026, ch. 1).

Theo recognizes the problem instantly, which is a strange feeling for a man three weeks into a quant desk. A fund facing a redemption queue is a borrower facing a maturity wall, and his thirteen-week cash flow model, still on the USB stick, needs only three row renames: "revolver availability" becomes undrawn lines, "asset sales" becomes the syndicated sleeve, and "maturities" becomes the redemption cap. The model that refuses to die has found its next body: a liquidity runway measured in quarters.

### 17.6.2 Derivation: a run with a pro-rata cap

**Notation.** NAV per share is $N$ (smoothed); the true value per share is $N(1-m)$, with $m$ the markdown of §17.3. The quarterly cap is $c$ (typically 5% of shares). The request fraction is $a_t$, which we deliberately do not call $q$, a letter this book reserves for dealer inventory. The fill fraction is $f_t=\min(1,c/a_t)$, and the share of the fund actually redeemed is $p_t=f_ta_t=\min(a_t,c)$.

**The transfer.** With $S$ shares outstanding, redeemers receive $N$ per share on $p_tS$ shares and the stayers own what is left. Post-redemption true value per remaining share is

$$
N^{\text{true}}_{\text{stay}}=\frac{N(1-m)S-N\,p_tS}{S(1-p_t)}=N\cdot\frac{(1-m)-p_t}{1-p_t}.
$$

Compare it with the no-run value $N(1-m)$:

$$
N^{\text{true}}_{\text{stay}}<N(1-m)
\iff (1-m)-p_t<(1-m)(1-p_t)
\iff p_t\,m>0 .
$$

So stayers lose whenever anyone redeems and $m>0$. The total transfer is exactly $p_tSNm$, the redeemed shares times the overpayment per share, and it lands on the $(1-p_t)S$ shares that stayed.

**The game.** An investor who requests gets $N$ on a fraction $f_t$ of her shares and $N^{\text{true}}_{\text{stay}}$ on the rest; one who does not gets $N^{\text{true}}_{\text{stay}}$ on everything. Since $N>N(1-m)>N^{\text{true}}_{\text{stay}}$ when $m>0$, requesting pays $f_t\big(N-N^{\text{true}}_{\text{stay}}\big)>0$ more, for any $f_t>0$. **Requesting is a dominant strategy as soon as $m>0$ is believed**, net of whatever small early-repurchase fee or tax friction applies. The cap does not remove the first-mover advantage; it rations it. If everyone requests, $a_t=1$, $f_t=c$, and the fund pays out $c$ per quarter: a 5% cap turns a run into a twenty-quarter queue.

Why, then, do request fractions sit at 6% or 17% rather than 100%? Because $m$ is not common knowledge. Most holders came through an advisor, few read the 10-Q, and many do not know a listed sibling exists. The request fraction $a_t$ is therefore a *belief* variable: the share of holders who are both attentive and persuaded that $m>0$. It jumps when a public signal coordinates beliefs, which is why a listed sibling printing 0.86 of book, or a merger at NAV-for-NAV, moves the non-traded fund's queue.

**Queue dynamics.** Unfilled tender requests usually lapse and must be resubmitted, and in practice most are, which behaves like a rolling backlog $\mathcal{B}_t$. With new requests arriving as a fraction $a^{\text{new}}_t$ of non-queued shares, demand is $\mathcal{B}_t+a^{\text{new}}_t(S_t-\mathcal{B}_t)$, payouts are $\min(\text{demand},cS_t)$, the backlog carries the rest, and $S_{t+1}=S_t-\text{payout}$. Fill rates fall quarter after quarter even if new requests are steady, and that falling fill is itself a public signal that feeds the next quarter's $a^{\text{new}}$.

**Liquidity runway.** In quarters, for a vehicle with NAV normalized to one,

$$
\mathcal{T}=\frac{\text{Cash}+\text{Undrawn lines}+\text{Sleeve}\times(1-h)}{c\cdot\text{NAV}+\text{Unfunded draws}+\text{Debt maturities}-\text{Repayments}},
$$

where $h$ is the haircut on the syndicated sleeve under stress and every flow in the denominator is per quarter. If the denominator is zero or negative, the runway is unbounded. The IMF's calibration target is 9–11 quarters of 5% redemptions under mild stress and 5–7 under a moderate shock. The repayment term links this section to §17.4: repayments *are* the private book's exit hazards, $\kappa^{(B)}+\kappa^{(P)}$, and those fall in a tight-loan regime, exactly when redemptions rise. Two error-prone spots deserve emphasis. First, $h$ is reflexive: when several funds sell their sleeves at once, the sale *is* the spillover into public loan prices, and the haircut rises because of the selling it is meant to measure. Second, the fund can change $c$. OBDC II's move from tenders to return-of-capital distributions changed the payout rule, and with it the game.

> **Poker Table.** Ines draws the redemption queue as a hand. "Twenty players, one pot, and the dealer will only pay five percent of the pot per round, pro rata among whoever stands up. Everyone can see a card face down in the middle; it's the true NAV. Nobody can turn it over, but there's a mirror across the room, the listed sibling's price, and it says the card is worse than the dealer claims. The first players to believe the mirror stand up first and get paid at the dealer's number. Everyone else is subsidizing them. You don't win this hand by being right about the card. You win by being early about the mirror." Then she replays it through markouts: in the first quarter of 2026, the investors who requested in January were filled at a NAV that later quarters marked down.

### Case Study: The Redemption Quarters of 2026

**Q1 2026.** Investors sought about \$13 billion from "over a dozen funds," and with quarterly caps around 5% of net assets "more than \$4.6 billion of investor capital" was trapped behind withdrawal limits (Bloomberg Law, March 26, 2026). Barings capped a private credit fund at 5% after requests reported at 11.3% of shares, and Moody's reportedly moved its outlook on a large Blue Owl non-traded BDC to negative (press reports, early April 2026; not independently verified for this edition). The Fed's May report recorded that accepted redemptions exceeded inflows for the first time and that several funds received requests "much larger than 5 percent of NAV."

**Q2 2026.** Apollo Debt Solutions, a \$26 billion fund, saw requests reach "16.8%, equivalent to \$2.4 billion" and capped them at 5% of shares, "the standard limit for such vehicles"; Blue Owl's two non-traded BDCs received April exit requests of "roughly 20% and 40%"; Blackstone's \$79 billion BCRED received repurchase requests "amounting to 10% of shares outstanding" for the quarter to June 30; and Morgan Stanley's North Haven Private Income Fund had limited repurchases to 5% in March (InvestmentNews, June 23, 2026).

**The model mapping.** At $a=0.168$ and $c=0.05$ the fill is $0.05/0.168\approx30\%$. With an illustrative markdown of $m=5\%$, each quarter's redemptions transfer $p\,m=0.25\%$ of NAV from stayers to redeemers, and the stayers' true value per share falls from $0.950$ to $0.947$ of NAV. That is small per quarter and corrosive over five, which is why the funds' choices matter more than the arithmetic. They can sell the sleeve, which pushes public loan prices down; draw the bank line, which in 2022 cost an extra 1.1 points; or change the rules, as OBDC II did when it replaced tenders with return-of-capital distributions funded by the \$1.4 billion sale.

**The desk signal.** The request percentage per fund is a public, dated, numeric series: it appears in 8-Ks, tender-offer filings (Schedule TO) and fund letters within days of each quarter's deadline. It leads listed-BDC equity and BDC bond spreads, because it is the most direct measure of how many holders believe $m>0$. Build the `redemptions` table before anything else in this chapter; it is the cheapest data with the highest signal-to-noise.

> **Trend Watch.** *The listed discount and the redemption queue, November 2025 to September 2026.* November 5–19, 2025: the OBDC/OBDC II NAV-for-NAV merger is announced and terminated within fourteen days (Blue Owl releases). February 18, 2026: OBDC repurchases stock at 86% of book; OBDC II replaces tender offers with return-of-capital distributions (Blue Owl releases). March 26, 2026: about \$13 billion of first-quarter requests, more than \$4.6 billion trapped (Bloomberg Law). End of March 2026: the median listed BDC is reported at about 0.74 times forward NAV, the widest since 2020 (Reuters/LSEG; not independently verified). April 14, 2026: the IMF estimates non-traded BDCs can meet 5% quarterly redemptions for 9–11 quarters under mild stress and 5–7 under a moderate shock. April 16, 2026: listed BDCs at "nearly a 20% discount," some large names "approaching a 50% discount" (Octus). May 8, 2026: first quarter on record in which accepted redemptions exceeded inflows (Fed FSR). June 23, 2026: a \$26 billion fund at 16.8% requests and a \$79 billion fund at 10% (InvestmentNews). **What it means for the desk:** the dispersion of listed discounts, not their mean, is the tradable signal (§17.9), and the redemption series is its leading indicator.

```python
# ---- block 4: the redemption game and the liquidity runway ----
def redemption_fill(a, cap=0.05):
    """Pro-rata fill fraction f = min(1, cap / a)."""
    return 1.0 if a <= 0 else min(1.0, cap / a)


def stayer_value(nav, m, a, cap=0.05):
    """True value per remaining share after pro-rata redemptions paid at smoothed NAV."""
    paid = redemption_fill(a, cap) * a
    return nav * ((1.0 - m) - paid) / (1.0 - paid)


def queue_path(new_requests, cap=0.05):
    """New requests arrive as fractions of non-queued shares; unfilled requests stay queued.
    Shares start at 1. Returns one row per quarter."""
    S, backlog, rows = 1.0, 0.0, []
    for a_new in new_requests:
        if not 0.0 <= a_new <= 1.0:
            raise ValueError("request fractions must lie in [0, 1]")
        new = a_new * (S - backlog)
        demand = backlog + new
        paid = min(demand, cap * S)
        rows.append({"shares": S, "new": new, "demand": demand, "paid": paid,
                     "fill": paid / demand if demand > 0 else 1.0, "backlog_end": demand - paid})
        backlog = demand - paid
        S -= paid
    return pd.DataFrame(rows)


def runway_quarters(cash, undrawn, sleeve, haircut, nav, cap, unfunded, maturities, repayments=0.0):
    """Quarters of capped redemptions the vehicle can fund; all flows per quarter, as fractions of NAV."""
    if not 0.0 <= haircut <= 1.0:
        raise ValueError("haircut must lie in [0, 1]")
    outflow = cap * nav + unfunded + maturities - repayments
    return np.inf if outflow <= 0 else (cash + undrawn + sleeve * (1.0 - haircut)) / outflow


# --- sanity checks, block 4 ---
assert abs(redemption_fill(0.168) - 0.05 / 0.168) < 1e-12                 # ~30% fill at 16.8% requests
sv = stayer_value(1.0, 0.05, 0.168)
assert sv < 0.95 and abs(sv - 0.9474) < 1e-3                              # stayers lose vs N(1 - m)
assert abs(stayer_value(1.0, 0.0, 0.3) - 1.0) < 1e-12                     # honest marks: no transfer
paid = redemption_fill(0.168) * 0.168
assert abs((1.0 - paid) * (0.95 - sv) - paid * 0.05) < 1e-12              # stayers' loss = p * m
assert redemption_fill(0.168) * (1.0 - sv) > 0                            # requesting strictly dominates
path = queue_path([0.168, 0.10, 0.10, 0.10])
assert (path["paid"] <= 0.05 * path["shares"] + 1e-12).all()
assert abs(path["new"].sum() - path["paid"].sum() - path["backlog_end"].iloc[-1]) < 1e-12
assert path["fill"].is_monotonic_decreasing                               # fills fall with steady requests
T0 = runway_quarters(0.002, 0.10, 0.10, 0.10, 1.0, 0.05, 0.02, 0.0)
T1 = runway_quarters(0.002, 0.10, 0.10, 0.10, 1.0, 0.05, 0.02, 0.0, repayments=0.03)
assert abs(T0 - 2.743) < 0.01 and abs(T1 - 4.8) < 0.01                    # repayments buy two quarters
assert runway_quarters(0.0, 0.1, 0.0, 0.0, 1.0, 0.05, 0.0, 0.0, repayments=0.06) == np.inf
print(path.round(4))
print("runway (quarters): no repayments %.2f, with 3%%/qtr repayments %.2f" % (T0, T1))
```

The runway check is a non-traded BDC with 0.2% cash, an undrawn line of 10% of NAV and a 10% syndicated sleeve haircut by 10%, paying 5% redemptions and 2% of NAV a quarter in unfunded draws *(illustrative)*. With no repayments it lasts under three quarters; with repayments of 3% of NAV a quarter it lasts 4.8, just under the IMF's moderate-shock range. Everything turns on the repayment rate, and the repayment rate is the hazard model of §17.4.

> **Ways This Blows Up.** (1) *Treating the sleeve as cash.* The haircut is a function of how many other funds are selling the same loans that week. (2) *Assuming the rules are fixed.* Boards can suspend tenders, switch to return-of-capital distributions, or (in some structures) raise the cap; each changes the game mid-hand. (3) *Ignoring the bank.* A borrowing-base haircut on PIK or non-accrual loans shrinks the undrawn line exactly when the queue lengthens, which is the question Theo asked in the cold open. (4) *Reading low requests as health.* A falling $a_t$ after a gate may mean investors gave up, not that they were reassured; check whether the backlog was resubmitted.

### Deep-Dive Resource Graph

- **Practitioner Writing:** InvestmentNews, "Apollo Throttles Withdrawals from \$26B Private Credit Fund after Exit Requests Rise to 17%" (Jun 23, 2026), https://www.investmentnews.com/alternatives/apollo-throttles-withdrawals-from-26b-private-credit-fund-after-exit-requests-rise-to-17/267119 ; Bloomberg Law, "Private Credit Funds Trap \$5 Billion as Investors Rush for Exit" (Mar 26, 2026; paywalled), https://news.bloomberglaw.com/banking-law/private-credit-funds-trap-5-billion-as-investors-rush-for-exit
- **Academic Papers:** George and Shin, "The Rise of Semiliquid Funds for Retail Investors," FEDS Note (Oct 14, 2026), https://www.federalreserve.gov/econres/notes/feds-notes/the-rise-of-semiliquid-funds-for-retail-investors-20261014.html ; Diamond and Dybvig, "Bank Runs, Deposit Insurance, and Liquidity," *Journal of Political Economy* (1983), the original first-mover game.
- **Data & Code:** Federal Reserve *Financial Stability Report* (May 2026), https://www.federalreserve.gov/publications/files/financial-stability-report-20260508.pdf ; IMF *Global Financial Stability Report* (April 2026), ch. 1, https://www.imf.org/-/media/files/publications/gfsr/2026/april/english/ch1.pdf ; SEC EDGAR Schedule TO and 8-K filings for request percentages.

## 17.7 The Plumbing That Turns Marks into Prices

### 17.7.1 Desk framing: a 2022 prediction, scored in 2026

> **[SOURCE EXTRACTION]** *Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.41:* "While loans and other private credit instruments are obviously problematic from a data availability perspective at present, we believe that the momentum of quant activity in other areas of the fixed income markets will drive innovation and transparency in these historically opaque areas. Already both Refinitiv and IHS Markit are providing daily pricing on 6,500 loan facilities."
>
> **Annotation.** Four years later the prediction scores well on infrastructure and poorly on causation. Private credit did acquire identifiers, daily estimated values, a secondary desk, a CDS index with private-credit names in it and an official statistics line, all between 2025 and 2026. But the driver was not quant activity spilling over from public bonds. It was the wealth channel: managers competing for retail and 401(k) money needed something that looked like a daily price, and stressed redemption queues made the absence of one expensive. The desk's departure from Man's framing is practical. The new data are not prices in the sense of Chapter 19's TRACE prints; most of them are *marks published more often*. The smoothing kernel of §17.2 still applies, with shorter lags.

Mags has her own version. "Back in my day, distressed was the private market. You called three desks, got a 32–34 market on five million, and the bid evaporated if you said the word 'size.'" Moyer's description of the old distressed market is still the best one: "Liquidity, of course, is a matter of degree" (Moyer_Distressed_Debt_Analysis p.313). Then the grudging respect: "A firm bid that a manager is contractually obliged to honor every day? We'd have killed for that. Check who's on the other side of it."

### 17.7.2 Five price sources, and what each one actually measures

1. **Listed BDC equity and bonds.** True market prices, set by people who can lose money, on a wrapper that includes fees and leverage. §17.3 inverts them.
2. **Daily estimated values from managers.** Apollo extended daily pricing from its investment-grade products (July 1, 2026) to direct lending, asset-backed finance, multi-credit and opportunistic vehicles on October 1, 2026, with asset-level pricing from October 30, 2026. The release is careful to call it an internal estimated fair value, "not a market-clearing price" (Apollo release, October 1, 2026). A daily mark is still a mark. It stair-steps on smaller stairs.
3. **Identifiers and a secondary market.** ICE's private credit service had issued more than 5,000 ICE IDs by March 2026, and Apollo reported more than \$30 billion of secondary trading since 2024 (same release). Identifiers matter more than they sound: they are the join key that turns fifty BDC schedules of investments into one panel, which is what the cross-holder dispersion of §17.3 needs.
4. **A contractual bid.** The SPDR SSGA IG Public & Private Credit ETF (PRIV) launched in February 2025 with a 10–35% private-credit policy. At October 15, 2026 it held \$802.8 million in 363 positions, about 22.1% sourced from Apollo, and Apollo must post daily firm, executable bids on those assets and buy them back at those bids within stress-redemption limits (State Street fund page). The smoothing problem becomes a counterparty problem: the ETF's private sleeve is worth what Apollo's bid is worth, up to the facility's limits.
5. **Credit derivatives.** S&P Dow Jones Indices announced a CDX Financials index in early 2026, reported to contain 25 North American financial names including BDCs and private-credit managers, with trading from April 2026 (S&P DJI announcement, February 25, 2026; constituents and weights not verified for this edition). It is the first $\mathbb{Q}$-measure instrument with private credit inside it, and §17.9 explains why it is a worse hedge than it looks.

> **Trend Watch.** *From "no price" to five price sources, 2022–2026.* 2022: Man notes daily vendor pricing on 6,500 syndicated loan facilities and calls private credit "problematic from a data availability perspective" (Man p.41). February 2025: PRIV launches with a manager's firm bid on its private sleeve (State Street). March 2026: ICE passes 5,000 private-credit identifiers (Apollo release). April 2026: CDX Financials begins trading, reportedly with BDCs among its names (S&P DJI; details unverified). July 1 and October 1, 2026: Apollo daily pricing reaches investment-grade and then all credit vehicles; asset-level from October 30 (Apollo). October 16, 2026: private credit enters the Fed's Z.1 with holder-level series (Brinkman et al.). **What it means for the desk:** for the first time there are enough *public* observations of *private* marks to estimate the kernel, the gap and the lead–lag on live data rather than on CDLI back-fills. Wire each source into Appendix B's data atlas with its own measurement label: price, mark, bid or spread.

## 17.8 Systematic Approaches to Private Credit

### 17.8.1 Desk framing: four marks a year and a lot of footnotes

What can "systematic" mean for an asset that reports four times a year? Not high-frequency anything. It means a **look-through security master** built from BDC schedules of investments (every facility, every quarter, with cost, fair value, spread, lien and PIK flags) plus a set of slow, fundamental features computed on it. The corpus is research-grade: Davydiuk, Marchuk and Rosen used BDC schedule-of-investment data to show that BDC capital substitutes for bank credit after regulatory and lender-specific supply shocks ("Direct Lenders in the U.S. Middle Market," *Journal of Financial Economics* 162, 2024). Chapter 25's parser builds the table; this section says what to compute on it.

> **[SOURCE EXTRACTION]** *Bohn_Stein_Active_Credit_Portfolio_Management p.235 (fn. 11):* "it would be unusual in the private credit risk setting to have more than 10 year-end financial statements and quarterly financial statements."
>
> **Annotation.** Bohn and Stein are describing borrower-level data for private-firm default models, and the warning transfers directly to vehicle-level work: forty quarterly NAVs is a long history for a BDC, and many semi-liquid funds have fewer than twenty. Every estimate in this chapter (the kernel, the lead–lag, the hazard loadings) is a small-sample estimate, so the 2026 desk departs from single-vehicle modeling altogether. It pools across vehicles that hold the same loans, as Couts, Gonçalves and Rossi recommend; it uses purged, embargoed cross-validation with quarterly blocks (Chapter 7); and it reports intervals. The breadth of a private-credit strategy comes from the cross-section of vehicles and facilities, not from the time series of any one of them.

### 17.8.2 The features worth computing

- **Sector and AI exposure.** About one-fifth of direct-lending loans are to software companies, and software can exceed half of NAV in some levered vehicles (IMF GFSR, April 2026). Public markets repriced first: syndicated loan spreads widened "reflecting a high concentration of leveraged loan borrowers in the software industry" before private-credit new-loan spreads "ticked up" (Fed FSR, May 2026). A per-vehicle software loading is a sector factor in Chapter 9's framework.
- **Diversification.** BDCs with more than 200 borrowers averaged a 9.5% return on equity in 2025, against 6.1% for those with fewer than 100 (Cliffwater data via BlackRock *Private Credit Primer*, January 2026). Scale is a factor, not a footnote.
- **Hidden default.** PIK interest was 7.3% of CDLI income in 2025 (Cliffwater, March 31, 2026). Of investments paying PIK at the end of 2025, 58.3% carried "bad PIK," meaning PIK amended in after closing rather than agreed at origination (Lincoln International data via BlackRock's *Credit Currents* chartbook, 1H2026). Kaz asks whether that means there is a good PIK. There is: a PIK toggle priced into the original deal is a contract term. A PIK amended in after closing is a borrower who could not pay cash and a lender who preferred not to call it a default. Theo's "but what does the amendment say?" is, here, the entire feature.
- **Mark quality.** Stale-mark share (§17.3), cross-holder dispersion (§17.3) and the gap series $g_t$.
- **Net-of-fee reality.** Private debt funds' net-of-fee abnormal returns are statistically insignificant; gross alpha is positive, and so is alpha against a debt-only benchmark, which reflects embedded equity risk (Erel, Flanagan and Weisbach, NBER w32278, 2024). IDO or it didn't happen: strip leveraged-loan beta, rates and the equity-like tail before calling anything alpha.
- **Collateral uniqueness.** The unit-sum constraint of §17.2 fails when the collateral was never there. First Brands (Chapter 11, September 2025), Tricolor and the UK lender Market Financial Solutions were all accompanied by allegations that receivables or loans had been pledged to more than one lender (press and court reports; amounts not verified for this edition). No smoothing kernel catches that. A UCC lien-overlap check and a flag for receivables bought off-platform do.

### 17.8.3 Derivation: what the public data already knows about the next marks

The chapter's main engine combines §17.2 and §17.3. Under the smoothing model, the true value change through quarter $t$ is $\beta\sum_{s\le t}F_s$ (ignoring the idiosyncratic part, which has mean zero), and the marks through $t$ have recognized $\beta\sum_{s\le t}F_s\sum_{k=0}^{t-s}\theta_k$ of it. The difference is the **pending mark**:

$$
\Pi_t=\beta\sum_{s\le t}F_s\Big(1-\sum_{k=0}^{t-s}\theta_k\Big)=\beta\sum_{j=0}^{K-1}\bar\Theta_{j+1}\,F_{t-j},
\qquad \bar\Theta_{j}\equiv\sum_{k=j}^{K}\theta_k ,
$$

using $j=t-s$ and the unit-sum constraint, so that $1-\sum_{k=0}^{j}\theta_k=\bar\Theta_{j+1}$. $\Pi_t$ is the sum of all future reported returns already implied by public factor returns, known at $t$. With $\theta=(0.5,0.3,0.2)$, $\Pi_t=\beta(0.5F_t+0.2F_{t-1})$. If the loan index fell 4% this quarter and was flat last quarter, a unit-beta book still has 2% of markdowns to come.

The **mark-gap signal** compares that mechanical catch-up with what the listed price implies:

$$
G_{i,t}=m_{i,t}-\max\!\big(0,-\Pi_{i,t}\big).
$$

When $G_{i,t}>0$, the price discounts more than the public data says the marks will fall: either the market knows something about this book beyond its beta (high software share, bad PIK, stale marks), or it is overreacting. The cross-sectional regression of $G$ on the §17.8.2 features separates the two, and the residual is the relative-value signal. When $G_{i,t}<0$, the price has not caught up with marks that are coming, which is the cleanest short in the book.

```python
# ---- block 5: what the public data already knows about the next marks ----
def pending_mark(theta, beta, F_recent):
    """Expected sum of all future reported returns already implied by public factor returns.
    F_recent = [F_t, F_{t-1}, ..., F_{t-K+1}] (newest first). Returns beta * sum_j Theta_{j+1} F_{t-j}."""
    th = np.asarray(theta, dtype=float)
    th = th / th.sum()
    K = th.size - 1
    tail = np.array([th[j + 1:].sum() for j in range(K)])           # Theta_{j+1} = sum_{k > j} theta_k
    F_recent = np.asarray(F_recent, dtype=float)
    if F_recent.size != K:
        raise ValueError("need exactly K recent factor returns, newest first")
    return float(beta * np.dot(tail, F_recent))


def mark_gap_signal(p_nav, lev, fee_drag, theta, beta, F_recent):
    """G = price-implied markdown minus the markdown the public data says is still coming."""
    m_hat = implied_markdown(p_nav, lev, fee_drag)
    return m_hat - max(-pending_mark(theta, beta, F_recent), 0.0)


# --- sanity checks, block 5 ---
th = np.array([0.5, 0.3, 0.2])
assert abs(pending_mark(th, 1.0, [-0.04, 0.0]) + 0.02) < 1e-12          # 2% of markdowns still to come
shock = np.zeros(8)
shock[3] = -0.04                                                         # one bad quarter at t = 3
reported = np.array([sum(th[k] * shock[t - k] for k in range(3) if t - k >= 0) for t in range(8)])
assert abs(reported[4:].sum() - pending_mark(th, 1.0, [shock[3], shock[2]])) < 1e-12
G = mark_gap_signal(0.86, 1.19, 0.05, th, 1.0, [-0.04, 0.0])
assert abs(G - (0.0411 - 0.02)) < 1e-3                                   # price discounts ~2% beyond catch-up
print("pending mark %.4f, mark-gap signal %.4f" % (pending_mark(th, 1.0, [-0.04, 0.0]), G))
print("mark_gap: all sanity checks passed")
```

### Deep-Dive Resource Graph

- **Academic Papers:** Davydiuk, Marchuk and Rosen, "Direct Lenders in the U.S. Middle Market," *Journal of Financial Economics* 162 (2024), DOI 10.1016/j.jfineco.2024.103946; Erel, Flanagan and Weisbach, "Risk-Adjusting the Returns to Private Debt Funds" (NBER w32278), https://www.nber.org/papers/w32278
- **Practitioner Writing:** BlackRock, *Credit Currents* private credit chartbook (1H2026), https://www.blackrock.com/gls-download/literature/market-commentary/1h2026-credit-currents-chartbook-stamped.pdf
- **Data & Code:** Apollo daily pricing release (Oct 1, 2026), https://www.apollo.com/insights-news/pressreleases/2026/10/apollo-expands-daily-pricing-to-all-credit-assets-advancing-transparency-in-private-credit-3372805 ; State Street PRIV fund page, https://www.ssga.com/us/en/intermediary/etfs/spdr-ssga-ig-public-private-credit-etf-priv

## 17.9 What a Public-Markets Quant Desk Can Arbitrage

You cannot buy the loans. You can trade every public instrument whose price is a function of private marks. The menu, with the signal from this chapter that drives each one:

| Trade | Instruments | Signal | Hedge | Main failure mode |
| :--- | :--- | :--- | :--- | :--- |
| BDC equity relative value | Long scaled, diversified, low-software, low-bad-PIK BDCs; short sub-scale ones | Residual of $G_{i,t}$ on features; stale-mark share; cross-holder dispersion | Leveraged-loan TRS, loan ETF or HY CDX for beta; equity index for the equity tail | Borrow cost and buyback squeezes on the short side |
| BDC capital structure | Unsecured notes vs equity (revolver senior to both) | Deleveraging, asset sales near par, bank line pricing and utilization | Ratio from a Merton-on-a-CLO map (Chapter 23) | Thin bond trading; a single buyer can take a whole new issue |
| Index vs basket | CDX Financials vs a BDC-only basket | BDC spread dispersion vs index | Ratio-weighted index protection | Few private-credit names in the index: small, unstable hedge ratio |
| Wrapper premium/discount | PRIV and future hybrid ETFs | Premium/discount vs firm-bid facility headroom | Public IG sleeve | Facility limits bind in stress; counterparty concentration |
| Event-driven | Mergers at NAV, tender-to-RoC conversions, listings, portfolio sales | Exchange-ratio math, request percentages | Sector basket | Adverse selection in sales "at fair value" |
| Gate-driven selling | Syndicated loans held in semi-liquid sleeves | Quarter-end queues, runway $\mathcal{T}$ | Loan index | Crowded, small, and quickly arbitraged |
| Takeout supply | CLO tranches, repricing-sensitive loans | $Q^{P\to B}$ from §17.4 | CLO AAA vs equity | Misread regime; dual-track noise |
| Insurer rotation | Public BBB/BB vs MM-CLO mezzanine | NAIC calendar, designation challenges | Duration-matched IG index | Regulatory delay; the rotation is pre-announced |

Two of these deserve a warning label.

> **Ways This Blows Up.** (1) *The index hedge that isn't.* CDX Financials is a broad financials index with only a handful of private-credit names, so its beta to a BDC basket is small and moves with bank and insurer news that has nothing to do with marks. Hedging a BDC bond book with it is hedging a cough with an umbrella. (2) *The sale at fair value.* Every portfolio sale at or near par is evidence about the loans that were sold, not the loans that were kept. Treat a "sale at 99.7% of par" as an upper bound on the remaining book's marks, never as a confirmation of them. (3) *Equity beta in disguise.* Listed BDC equity carries equity-market beta that rises in selloffs; a BDC relative-value book that is not hedged against the equity index will look like private-credit alpha until the first equity drawdown. (4) *Crowding the obvious.* By mid-2026 every desk had the redemption series. The edge moved to its *second derivative*, the change in fill rates and backlog, and to vehicles whose sibling relationships are less obvious than Blue Owl's.

### Deep-Dive Resource Graph

- **Practitioner Writing:** Matt Levine, *Money Stuff* (Bloomberg Opinion), columns on private credit marks, BDC discounts and semi-liquid funds, 2025–2026 (search the archive; specific columns not verified for this edition).
- **Academic Papers:** Avalos, Doerr and Pinter, "The Global Drivers of Private Credit," *BIS Quarterly Review* (Mar 2025), https://www.bis.org/publications/qr-202503/global-drivers-private-credit
- **Data & Code:** FINRA TRACE for BDC unsecured bond prints, https://www.finra.org ; SEC EDGAR for 8-K and Schedule TO filings, https://www.sec.gov/edgar

## 17.10 Desk Debrief

Ines replays the cold-open hand. The desk bid the \$25mm of notes two points back of the screen and hedged half the risk with a short in the BDC's own equity, on the view that the seller knew about the redemption queue at a sibling-type vehicle and the equity would reprice before the bonds. The markouts said they were right about the direction and wrong about the ratio: the equity fell more than the bonds, as the capital-structure algebra predicts when the debt is money-good. The hand history goes in the file. *(The trade is illustrative.)*

- **Private credit is public credit with the price removed.** Same borrowers, same sponsors, two pricing regimes. The difference is measurement, not credit.
- **A mark is a moving average of the truth.** Reported volatility is deflated by $\sqrt{\sum_k\theta_k^2}$, contemporaneous beta by $\theta_0$, and the Sharpe ratio is inflated by $1/\sqrt{\sum_k\theta_k^2}$. NAV momentum is a property of the valuation calendar.
- **Sum the lags.** The Dimson aggregated beta recovers the true beta, and the lagged coefficients forecast the next mark from public data you already have.
- **Unsmooth gently.** Inverting a kernel with $\theta=0.7$ amplifies measurement noise more than sixteen times. Pool across co-holders and report intervals.
- **One discount point is half an asset point.** $m=\big((1-\phi)-P/\text{NAV}\big)/(1+\ell)$: at 1.1x leverage, a 20% equity discount says the loans are worth about 90, not 80.
- **The non-accrual pair hides a mark.** $\hat R^{\text{mark}}_{\text{NA}}=(w^{FV}/w^{C})(FV/C)$; a rising cost-minus-fair-value gap with a falling headline rate is the hole getting deeper.
- **A 5% cap rations a run; it does not stop one.** Requesting dominates once $m>0$ is believed, the transfer is $p\cdot m$ per quarter, and the request percentage is the best public belief series in the asset class.
- **Trade the wrappers.** BDC equity, BDC bonds, ETFs with firm bids, CDX Financials, the loans semi-liquid funds sell and the supply private takeouts create. IDO or it didn't happen.

### The Spec You Hand the Robot

**Vague version.** "ROBO, minimize the mark gap." ROBO writes to the valuation committee recommending that all loans be marked to the listed BDC's implied price, which minimizes the gap to zero and the manager's fee base by 10%. It did exactly what was asked.

**Precise version: the Mark-Gap Monitor.**

- **Inputs.** `bdc_quarterly`, `soi`, `redemptions` and `public_index` with the §17.2 schemas; quarterly frequency; decimals, not percent strings; net (not gross) debt to NAV; NAV vintage stored alongside each restatement.
- **Step 1, kernel.** For each cluster of co-holding vehicles, fit $\hat\theta$ by pooled Dimson regression with $K\le3$, requiring $10(K+1)$ observations; bootstrap quarters in blocks of four; refuse a point estimate if the 90% interval for $\theta_0$ is wider than 0.4.
- **Step 2, pending mark.** $\Pi_{i,t}=\hat\beta_i\sum_{j=0}^{K-1}\bar\Theta_{j+1}F_{t-j}$ using the vehicle's sector-matched public index.
- **Step 3, implied markdown.** $m_{i,t}=\max\big(0,((1-\phi_i)-P/\text{NAV})/(1+\ell_i)\big)$ on buyback-adjusted forward NAV; NaN for non-traded vehicles, never 1.0.
- **Step 4, gap and features.** $G_{i,t}=m_{i,t}-\max(0,-\Pi_{i,t})$; regress cross-sectionally on software share, bad-PIK share, stale-mark share, cross-holder dispersion, non-accrual gap $g_t$, borrower count and the sibling redemption request percentage; output the residual.
- **Step 5, runway.** For every semi-liquid vehicle, $\mathcal{T}$ with repayments taken from the §17.4 hazard model under the current regime; flag $\mathcal{T}<5$ quarters.
- **Outputs.** One row per (`bdc_id`, `qdate`): $\hat\theta$ with interval, $\Pi$, $m$, $G$, residual signal, $\mathcal{T}$ and every flag that fired. Units in column names.
- **Tests.** All five blocks' sanity checks in this chapter, plus a restatement test (a restated NAV must not change any earlier row's signal) and a non-traded test (no P/NAV, no $m$, no signal, but a runway).

### Exercises

1. **The year-long lag.** A manager's marks recognize a true return evenly over four quarters, $\theta_k=1/4$ for $k=0,\dots,3$. Show that the reported Sharpe ratio is twice the true one and that $\rho^o_1=3/4$. ROBO reports the vehicle's annualized volatility as 2.1%. What is the true figure, and what correlation with the loan index should you expect contemporaneously and after summing three lags?
2. **Marking the discount.** A listed BDC trades at 0.62 of NAV with net leverage 1.25x and an estimated fee drag of 4%. Compute $m$. Then argue, without computing, whether the true markdown is higher or lower once you admit that the BDC's unsecured notes are not money-good, and say which chapter's model you would use to find out.
3. **The bad bucket.** A BDC reports non-accruals of 3.1% at cost and 1.0% at fair value, with portfolio fair value at 97% of cost. What is the implied carrying value of its non-accrual loans? Compare it with the roughly 50-cent restructuring recoveries Octus reported in April 2026, and state which number you would put in a Chapter 14 recovery model, and why neither is a recovery.
4. **Kaz's fix.** Kaz proposes eliminating redemption queues by raising the cap to 100%. With requests at 40% of shares and a true markdown of 8%, compute the stayers' true value per share under a 5% cap and under Kaz's 100% cap. Then explain why the 100% cap does not end the game but changes it into a classic bank run, and what Diamond and Dybvig would have told him.
5. **Takeout season.** Using block 3, find the regime value $\zeta$ at which expected private-to-syndicated supply halves relative to $\zeta=0$. Then show that the naive supply estimate overstates the competing-risks one by more in the tight regime, and explain why that matters for a CLO-demand forecast.
6. **The thirteen-week model, reborn.** Take any perpetual BDC's latest 10-Q and fill in Theo's runway: cash, undrawn lines (net of any borrowing-base exclusion for PIK or non-accrual loans), the syndicated sleeve, unfunded commitments, debt maturities and trailing repayments. How many quarters of 5% redemptions can it fund? Now cut repayments by half, as in the 2022–2024 tight regime, and recompute. Write down what the credit agreement says about the borrowing base before you trust either number.

### Deep-Dive Resource Graph (Chapter 17)

- **Podcasts:** Bloomberg *Odd Lots* (Joe Weisenthal and Tracy Alloway), episodes on private credit, BDCs and the bank–private credit relationship; *Capital Allocators* (Ted Seides), conversations with private credit allocators; *Flirting with Models* (Corey Hoffstein), episodes on systematic fixed income. Specific episodes were not verified for this edition; search each archive for "private credit."
- **Practitioner Writing:** Asness, "The Illiquidity Discount?" (AQR, 2019), https://www.aqr.com/Insights/Perspectives/The-Illiquidity-Discount ; Octus on BDC discounts and non-accruals (Apr 16, 2026), https://octus.com/resources/blog/bdcs-trading-at-50-discount-to-nav-but-nonaccruals-ticking-downward/ ; Blue Owl Capital Corporation press releases, https://www.blueowlcapitalcorporation.com/investors/news-events/press-releases ; IMF blog, "Fast-Growing \$2 Trillion Private Credit Market Warrants Closer Watch" (Apr 8, 2024), https://www.imf.org/en/Blogs/Articles/2024/04/08/fast-growing-USD2-trillion-private-credit-market-warrants-closer-watch ; Man Group, *Quantitative Credit Alpha: Early Mover* (2022, shelf); Nuveen, *Multi-Asset Credit Quant Framework* (shelf).
- **Academic Papers:** Getmansky, Lo and Makarov (NBER w9571), https://www.nber.org/papers/w9571 ; Couts, Gonçalves and Rossi, *Review of Financial Studies* 37(7), 2024; Cai and Haque, "Private Credit: Characteristics and Risks," FEDS Note (Feb 23, 2024), https://www.federalreserve.gov/econres/notes/feds-notes/private-credit-characteristics-and-risks-20240223.html ; Block, Jang, Kaplan and Schulze (NBER w30868), https://www.nber.org/papers/w30868 ; Erel, Flanagan and Weisbach (NBER w32278), https://www.nber.org/papers/w32278 ; Ellias and de Fontenay, 134 Yale L.J. (2025), https://www.yalelawjournal.org/article/the-credit-markets-go-dark ; Davydiuk, Marchuk and Rosen, *JFE* 162 (2024).
- **Data & Code:** Federal Reserve Z.1 (private credit series FL893167205, FL453067203, FL443067205, FL673067205), https://www.federalreserve.gov/releases/z1/ ; Fed FEDS Notes index, https://www.federalreserve.gov/econres/notes/feds-notes/default.htm ; Fed *Financial Stability Report*, https://www.federalreserve.gov/publications/financial-stability-report.htm ; SEC EDGAR (schedules of investments, 8-K, Schedule TO, N-PORT), https://www.sec.gov/edgar ; NAIC private credit resource center, https://content.naic.org/resource-center/private-credit-insurance-regulation ; Cliffwater Direct Lending Index and KBRA DLD (subscription; no link).

<!-- STATUS: COMPLETE -->
