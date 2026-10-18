# Chapter 7: Machine Learning on Small-Sample, Non-Stationary Credit Data


## 7.0 Cold Open: Forty-Seven Hats

Kaz had the screen angled toward Theo the way a cat presents a dead bird: proudly, and slightly too close.

"Gradient-boosted trees," Kaz said. "Two hundred and twelve thousand bond-months, eighty-one features, high-yield excess returns, 2004 to 2024. In-sample Sharpe of 2.9 on the top-minus-bottom decile."

Theo had been on the desk three weeks. He had learned that quants say "in-sample" the way bankers say "pro forma": a sincere description of a world that does not exist. He pointed at the top decile.

"How many issuers are in there?"

Kaz scrolled. Scrolled again. "Nine."

"And how many bonds?"

"Fifty-eight. Well. One of the issuers has eleven."

"So the model's best idea is one company in eleven maturities."

"It's a very good company," Kaz said. "Its bonds all go up together."

"That's what makes it one company."

Ines drifted over with a coffee she drank black, at a temperature that suggested she had once lost a bet about it. She looked at the Sharpe ratio for exactly as long as it deserved.

"What's the pot," she said, "and how many hands did you fold before you showed me this one?"

Kaz did the arithmetic out loud, which was brave. "Four model families. Six label horizons. Three winsorization rules. Forty-odd feature sets. Call it three thousand?"

"So you're showing me the best of three thousand hands. Of course it's a good hand. The question is whether it's a good hand *for a guy who looked at three thousand of them*."

From two desks over, without looking up, Mags said: "Back in my day we overfit by hand. We called it conviction. It had a beautiful track record, because nobody wrote down the trades that didn't work."

Theo took the USB stick out of his pocket (the 13-week cash flow model, carried for emotional support) and set it on the desk like a chess piece. "In restructuring, nobody ever asked me whether a bond would go up. They asked whether the thesis was right, how sure I was, and how much to put on. Can the model answer *that*?"

Kaz looked at the stick, then at the screen, then at the nine issuers, and said nothing, which on this desk counted as a concession.

So here is the question this chapter answers: **how do you learn anything from about 800 issuers, 20 years, three regimes, and prices that are sometimes a rumor, and how do you know when you have learned nothing at all?**

By the end of this chapter you will be able to: (i) explain, with numbers, why corporate-bond panels have an effective sample size an order of magnitude below their row count; (ii) make log-spread features stationary without erasing their memory, using fractional differentiation; (iii) build triple-barrier labels scaled in Duration Times Spread, with censoring for calls, tenders, and exchanges; (iv) turn a credit-agreement read into a primary model and let a meta-labeling model size it; (v) weight samples by uniqueness across both time and sibling bonds; (vi) write a purged, embargoed, issuer-grouped cross-validator that cannot peek; (vii) deflate a Sharpe ratio for the number of things you tried; and (viii) recognize the two biases that built, and then demolished, the corporate-bond factor zoo between 2019 and 2026.

One measure convention for the whole chapter. Every expectation and probability below is under the physical measure $\mathbb{P}$, because we forecast realized excess returns and realized labels. Risk-neutral objects (OAS, a CDS-implied hazard $\lambda_t$, a Merton distance-to-default) appear only as *features*. Features may be $\mathbb{Q}$ quantities; labels and losses are always $\mathbb{P}$.

## 7.1 Why Credit Is the Worst Machine-Learning Dataset in Liquid Finance

Start with the desk framing, because it is brutal and short. An equity stat-arb researcher has about 3,000 liquid US names, each with one share class, a closing auction that produces a real price every day, and decades of clean history. A credit researcher has a panel with five structural defects, and each one breaks a textbook machine-learning assumption in a specific, predictable direction. The rest of the chapter is a repair manual, one defect at a time.

**Defect 1: the price is sometimes a rumor.** Most corporate bonds do not trade on most days. A 2026 study from SMU's Cox School (Venkataraman, Jacobsen, and Xu, *Illiquidity Meets Intelligence: AI-Driven Price Discovery in Corporate Bonds*, under review; sample 2017–2023) reports that 60% of corporate bonds did not trade in institutional size on a given day, and 27% did not trade for an entire week. What fills the gap is a mark: an evaluated price, a matrix price, a dealer run, or an AI composite such as MarketAxess CP+. Marks are smooth, and smoothness is a lie with a statistical signature. It lowers measured volatility, induces positive autocorrelation in returns, and makes a backtest's Sharpe ratio look better than anything you could have traded.

> **[SOURCE EXTRACTION]** *Ben_Dor_Quantitative_Credit_Portfolio_Management p.204:* "the magnitude of decline between the top and bottom quintiles (despite the generally higher duration of bonds in the bottom quintile) increases as credit quality deteriorates, consistent with a potentially larger degree of stale pricing for lower credit qualities."
>
> **Annotation.** Ben Dor and coauthors sorted bonds into TRACE-volume quintiles within each rating and found that the least-traded bonds show *lower* daily price-return volatility even though they carry *more* duration. Risk did not fall; information arrival did. The page's second finding (return correlation between volume quintiles falls as the quintiles move apart) says the illiquid bonds are reporting the same news *later*. Two consequences for machine learning follow, and both run in the dangerous direction. First, staleness is worse exactly where the alpha is supposed to live: down the quality spectrum, in single-B and CCC names. Second, any feature built from lagged returns of illiquid bonds will "predict" their future returns, because the future return is just the mark catching up to news that the liquid market priced last week. Your model will discover this, will call it momentum, and will be unable to trade it, because the only counterparty willing to sell at the stale mark is the pricing service, and the pricing service does not take orders. The modern desk keeps the lesson and changes the tooling. The 2026 desk measures staleness directly (days since last institutional-size print, a composite-versus-last-trade gap) and feeds it to the model as a feature *and* as a sample filter, so that the model is told which observations are prices and which are rumors.

**Defect 2: the issuer is the observation.** A bond panel counts rows by CUSIP. Default, restructuring, LMT risk, and most of the idiosyncratic spread variance live at the issuer, or more precisely at the ultimate parent.

> **[SOURCE EXTRACTION]** *Dynkin_Systematic_Investing_in_Credit p.651:* "As of 31 May 2018, US Corporate IG and HY indices included 629 and 784 issuers (column 1 of each panel) or 573 and 576 public issuers (column 2 of each panel) domiciled in the United States."
>
> **Annotation.** Here is the number that should appear on the first slide of every credit ML pitch. Whatever your bond-month count says, the US high-yield cross-section was 784 issuers on that date, and only 576 of them had public equity, which matters because public equity is where most of the timely information in credit comes from (Chapter 9 on equity-to-credit signals). Forty-seven bonds from one issuer are one data point wearing forty-seven hats. Count rows and you will believe you have 200,000 observations. Count issuers and you have a few hundred per cross-section, with monthly cross-sections that are heavily autocorrelated because issuers change slowly. Section 7.6 makes this quantitative with an effective sample size $N_{\text{eff}}$, and §7.7 makes it structural by forcing every bond of an ultimate parent into the same cross-validation fold. The RSSG reader should feel at home: the organizational chart in a first-day credit agreement review (HoldCo, OpCo, restricted and unrestricted subsidiaries, guarantors) is exactly the grouping key the model needs, and a pure quant who groups by ticker will leak information between a parent and the unrestricted subsidiary its best assets were just dropped into.

**Defect 3: the sample curates itself.** Bonds leave the panel through calls, tenders, maturities, defaults, and distressed exchanges, and each exit is informative. A tender is usually at a premium to market; a distressed exchange is usually a loss dressed as a choice. "Open market purchase," still the most expensive three words in finance, also turns out to be one of the most expensive data-cleaning problems: a bond that disappears through an exchange labeled voluntary is survivorship bias wearing a trench coat. Section 7.4 handles exits as censoring.

**Defect 4: the features arrive late.** Ratings lag spreads. Fundamentals arrive with a 10-Q filing lag of up to 40 or 45 days after quarter-end (and longer for 10-Ks and for private filers). A feature that is "Q2 leverage" is not knowable on June 30. Dickerson, Nozawa, and Robotti built a whole paper around this (*Factor Investing with Delays*, 2024): signals must be stamped with the date they became *available*, not the date they *describe*. This is the label-timestamp problem in miniature, and §7.11 shows how a one-month version of it got a top-journal paper retracted.

**Defect 5: the world changes regime, and the panel is short.** Twenty years of TRACE contains roughly three credit regimes (2008, March 2020, the 2022 rates shock) plus the April 2025 tariff spike. Even the calm periods hide dispersion. On FRED's ICE BofA series, the US high-yield OAS hit 2.59% on 2025-01-22, spiked to 4.61% on 2025-04-07, and sat at 3.23% on 2026-10-15; the CCC-and-lower OAS on that same 2026-10-15 date was 12.78%, wider than its 11.37% at the April 2025 panic (FRED series BAMLH0A0HYM2 and BAMLH0A3HYC, fetched 2026-10-17). The index was calm while the bottom tier screamed. A regime label computed at the index level is one hat on nineteen hundred heads.

**And underneath all five: sampling faster does not buy you a better mean.** This is the defect that sells the most bad backtests, so derive it.

> **[SOURCE EXTRACTION]** *Paleologo_Advanced_Portfolio_Management p.49:* "But the relative size of the error doesn't depend on n!"
>
> **Annotation.** Paleologo's point, rebuilt in our notation: suppose an annual excess return has mean $\alpha$ and volatility $\sigma$. Split the year into $n$ periods (months, days). Each period's return has mean $\alpha/n$ and volatility $\sigma/\sqrt n$. The sample mean of $n$ period returns estimates $\alpha/n$ with standard error $(\sigma/\sqrt n)/\sqrt n = \sigma/n$. The relative error is $(\sigma/n)/(\alpha/n) = \sigma/\alpha$, which does not depend on $n$. Daily data estimates *volatility* beautifully and estimates the *mean* no better than one annual observation per year. Over $T$ years the $t$-statistic of the mean is $(\alpha/\sigma)\sqrt T$. A credit signal with an honest information ratio of 0.5 and a 20-year history has $t \approx 0.5\sqrt{20} \approx 2.2$, which, as §7.8 will show, is not enough once you have tried more than a handful of signals. The only way to get more independent evidence about a mean is more *calendar time* or more *independent cross-sectional bets*, and Defect 2 just told you the cross-section is smaller than it looks. This is why credit ML is a small-sample problem even when the dataset is measured in gigabytes.

> **Desk Myth vs. Desk Reality.** *Myth:* "We have 212,000 bond-month observations, so a gradient-boosted model with 81 features is comfortably identified." *Reality:* you have about 800 issuers, roughly 20 independent years for anything that depends on the market regime, overlapping labels that duplicate each other, and marks that are partly the pricing service's opinion. The model is identified the way a 300-page credit agreement is "clear": only to the person who wrote it.

## 7.2 Trend Watch: The Bond-Factor Replication Crisis, 2019–2026

Before building anything, look at what happened to the people who built it first. Between 2019 and 2026 the academic corporate-bond literature ran the most expensive cross-validation experiment in its history, and most of the published factors failed it.

> **Trend Watch.** *The corporate-bond factor zoo, built and audited.*
>
> - **2019.** Bai, Bali, and Wen publish "Common risk factors in the cross-section of corporate bond returns," *Journal of Financial Economics* 131(3): 619–642: a four-factor model (bond market, downside risk, credit risk, liquidity) that becomes a standard benchmark.
> - **2023 (January, first draft).** Dick-Nielsen, Feldhütter, Pedersen, and Stolborg circulate "Corporate Bond Factors: Replication Failures and a New Framework" (AQR working-paper page dated 5 October 2023; Best Paper, 2024 Utah Winter Finance Conference). Built on a clean database with outliers reviewed one by one and returns around defaults kept in, it reports that "only 23% of the factors considered significant in the literature have significant alphas" (as quoted by Quantpedia, 14 May 2024). Reproducing each paper with that paper's own data choices, only one factor premium stays significant; with the other papers' choices, none do.
> - **2023.** Dickerson, Mueller, and Robotti, "Priced risk in corporate bonds," *JFE* 150(2), 103707: previously proposed bond factors add essentially nothing beyond the bond market factor. While replicating, they find data errors in the 2019 factors, and the 2019 paper is retracted (retraction notice, *JFE* 150(3)). Warwick Business School's account (10 September 2024) says two factors had a one-month "lead error," a third a "lag error," and some extreme losses had been removed; it calls the retraction a first for the journal ("This is the first time this has happened"). Mueller and Robotti receive the Fama-DFA Prize.
> - **2023, the counterweight.** Jensen, Kelly, and Pedersen, "Is There a Replication Crisis in Finance?" (*Journal of Finance* 78(5), 2023), argue with a Bayesian hierarchical model that most *equity* factors do replicate. Keep this in view: the crisis is not "all factors are fake," it is "bond factors were measured badly."
> - **2026 (9 April).** Dickerson, Robotti, and Rossetti post "The Corporate Bond Factor Replication Crisis" (arXiv:2604.07880): 108 signals in nine thematic clusters, August 2002–December 2024 (269 months, 52,656 unique bonds). Of 432 specifications (108 signals × 2 weightings × 2 sorts), 26 (6.0%) survive a Benjamini–Hochberg false-discovery correction. Short-term reversal falls from −0.99% per month ($t=-4.46$) to −0.09% ($t=-0.51$) once the signal and the return stop sharing the same noisy price. The abstract's verdict: "the majority of previously documented factors do not produce statistically significant bond CAPM alphas after correction." The authors release the cleaned data and code as Open Bond Asset Pricing.
>
> *What it means for the desk.* The binding constraint in credit ML from 2019 to 2026 was never model capacity. It was label timestamps, price noise shared between signal and return, and return filters that peek. Every one of those is a cross-validation failure in disguise, and every one is fixable with the machinery in §7.3–§7.9. A desk that adopts the 2026 protocol starts where the literature finished; a desk that downloads a 2019 factor file starts with someone else's lead error.

Two observations about the trend before moving on. First, the speed: the canonical four-factor bond model went from publication to retraction in four years, and the field's largest factor zoo went from "hundreds of anomalies" to "26 of 432 survive" in seven. In equities the same audit took two decades. Credit compressed it because the errors were *data* errors, which are verifiable, rather than *multiplicity* errors, which are arguable. Second, the direction: the price-based signals (reversal, momentum, volatility) were hit hardest, which is exactly what Defect 1 predicts. Section 7.9 derives why.

## 7.3 Stationarity With Memory: Fractional Differentiation of Log Spreads

Kaz's model in the cold open used the *level* of log OAS as a feature. That is defensible on economics (wide spreads mean-revert; valuation is a level concept, see Chapter 9) and indefensible on statistics: a level that wanders across regimes means the model learns "2008 was wide" rather than "wide predicts tightening." The textbook fix is to difference, using $\Delta \log s_t$. That is stationary, and it is also amnesiac. It throws away exactly the level information that made the feature worth having. The desk wants a dial between "level, non-stationary, full memory" and "change, stationary, no memory." Fractional differentiation is that dial (Hosking 1981; López de Prado, *Advances in Financial Machine Learning*, 2018, ch. 5).

**Why log spreads and not spreads.** Before dialing anything, choose the right object.

> **[SOURCE EXTRACTION]** *Ben_Dor_Quantitative_Credit_Portfolio_Management p.39:* "These results clearly indicate that absolute spread volatility is highly unstable and tends to rise with increasing spread. Computing volatilities based on relative spread change generates a more stable time series."
>
> **Annotation.** This is the empirical foundation of DTS (Chapter 8), and it doubles as a feature-engineering rule. If spread changes are roughly proportional to spread levels, then $\Delta s_t \approx s_{t-1}\,\Delta \log s_t$, and the stable object is the relative change $\Delta \log s_t$, with sector volatilities that Ben Dor and coauthors report clustered between about 5% and a bit over 10% per month on the same page. Feed a model raw spreads, and a 50bp move means one thing for a 100bp BBB and another for an 800bp B3. Feed it log spreads, and the scale is comparable across ratings and across regimes, which is what lets one model span 2008 and 2021 without learning a separate world for each. Where the modern desk departs: the proportionality breaks near default (a bond at 3,000bp quotes on price, not spread) and near zero (the structural floor Ben Dor's own regressions show as a positive intercept). Cap the log transform's domain, switch distressed names to price-based features, and say so in the spec.

**The derivation.** Let $B$ be the backshift operator, $B x_t = x_{t-1}$. Ordinary differencing is $(1-B)x_t = x_t - x_{t-1}$. For a real exponent $d \ge 0$, define $(1-B)^d$ by the binomial series:

$$
(1-B)^d \;=\; \sum_{k=0}^{\infty} \binom{d}{k}(-B)^k \;=\; \sum_{k=0}^{\infty} w_k B^k,
\qquad w_k = (-1)^k \binom{d}{k} = (-1)^k\,\frac{d(d-1)\cdots(d-k+1)}{k!}.
$$

Take the ratio of consecutive weights. The numerator gains the factor $(d-k+1)$, the denominator gains $k$, and the sign flips:

$$
\frac{w_k}{w_{k-1}} = -\,\frac{d-k+1}{k}
\quad\Longrightarrow\quad
w_0 = 1,\qquad w_k = -\,w_{k-1}\,\frac{d-k+1}{k}.
$$

So $w_1 = -d$, $w_2 = d(d-1)/2$, $w_3 = -d(d-1)(d-2)/6$. For $d = 1$ the recursion gives $w_2 = 0$ and every later weight vanishes, recovering $x_t - x_{t-1}$. For $0 < d < 1$, every weight after $w_0$ is negative (each step multiplies by $-(d-k+1)/k$, which is positive once $k > d+1$, so the sign set at $w_1 = -d$ persists) and the magnitudes decay *hyperbolically*. Writing the weights with Gamma functions, $w_k = \Gamma(k-d)/\big(\Gamma(-d)\,\Gamma(k+1)\big)$, and using $\Gamma(k-d)/\Gamma(k+1) \sim k^{-d-1}$:

$$
|w_k| \;\sim\; \frac{k^{-d-1}}{|\Gamma(-d)|}\qquad (k \to \infty).
$$

That slow decay is the "long memory": a shock from 200 days ago still carries weight, unlike an ARMA filter whose weights decay geometrically.

How much of the level survives? Use the partial-sum identity $\sum_{k=0}^{K} (-1)^k\binom{d}{k} = (-1)^K\binom{d-1}{K}$, whose magnitude behaves like $K^{-d}/\Gamma(1-d)$. As $K \to \infty$ the full filter's weights sum to $(1-1)^d = 0$, so an infinitely long fractional difference annihilates a constant level, just as ordinary differencing does. But the decay is slow, and a *truncated* filter keeps a sliver of the level proportional to $K^{-d}$. That sliver is the memory we wanted to keep. Small $d$ keeps more; $d=1$ keeps none.

**Fixed-width window (FFD).** The expanding-window version uses more weights for later observations, which makes the transformed series non-stationary by construction (its variance depends on $t$). Fix a weight tolerance $\tau$ and keep only $k \le K(\tau)$ with $|w_k| \ge \tau$:

$$
\tilde x_t = \sum_{k=0}^{K(\tau)} w_k\, x_{t-k}.
$$

Then choose the smallest $d$ that makes the series stationary:

$$
d^\star = \min\big\{ d \in \{0, 0.05, \ldots, 1\} : \text{ADF}\big(\tilde x^{(d)}\big)\ \text{rejects a unit root at } 5\% \big\},
$$

and report $\rho\big(\tilde x^{(d^\star)}, x\big)$, the correlation between the transformed and raw series, as "memory retained." In plain terms, $d^\star$ is the least amnesia that still makes the feature stationary. Fractional differentiation is how much you remember after a closing night: enough to be stationary in the morning, not so much that you remember the covenant you agreed to at 3 a.m.

**The warm-up cost, computed.** The window length is not a detail. With $d = 0.4$, $|\Gamma(-0.4)| = \Gamma(0.6)/0.4 \approx 1.489/0.4 \approx 3.72$, so $|w_k| \approx k^{-1.4}/3.72$. Setting this equal to $\tau = 10^{-4}$ gives $k^{1.4} \approx 2{,}690$, or $K \approx 280$ trading days, more than a year of warm-up before the first usable value. With $\tau = 10^{-3}$, $K \approx 54$ days. A bond issued 14 months ago has no FFD feature at $\tau = 10^{-4}$, and new issues are exactly where a lot of the relative-value action lives. The fix is to compute FFD on an *issuer-level* constant-maturity log spread (interpolated from the issuer's curve, Chapter 8) and map it to the new bond, rather than on the bond's own short history.

> **Ways This Blows Up.** *Three ways fractional differentiation lies to you in credit.* (1) **Jumps.** A jump-to-default or an LMT announcement is a level shift that no $d<1$ makes stationary. One Serta-style uptier in the sample will dominate the ADF statistic and push $d^\star$ toward 1. Estimate $d^\star$ on a jump-filtered series (or on IG and HY separately), apply it to the raw one, and handle jumps as events, not as noise. (2) **Stale marks.** A stale bond's spread series is a step function. That manufactures positive autocorrelation in changes and makes the level look more persistent, so you can get a "low $d^\star$" from an illiquid bond whose low $d^\star$ is a liquidity artifact. Dynkin p.771 makes the same point about return autocorrelation; here it contaminates the memory estimate. (3) **Look-ahead in $d^\star$ itself.** Choosing $d^\star$ on the full sample and then backtesting uses the future to pick a preprocessing parameter. Choose $d^\star$ inside each training fold, or fix it once on a burn-in period you never test on.

## 7.4 Labels That Respect Credit: The Triple Barrier in DTS Space

The default label in a first-draft notebook is $y = \operatorname{sign}(r_{t \to t+h})$: did the bond's excess return over the next $h$ days end up positive? It is the wrong label for credit in three ways. It ignores the *path*: a bond that fell 9 points in week 2, triggering every risk limit on the desk, and then recovered to $+0.1$ by week 13 is labeled a winner. It ignores *scale*: a 1% move is noise for a CCC and a career event for an A-rated utility. And it ignores *exits*: the bond that was tendered at 101 in week 5 has no week-13 return at all. The triple-barrier method fixes all three. Credit needs one more adjustment, which is to measure the barriers in DTS units.

**The scale, derived.** Over a short interval the excess return of bond $i$ is carry minus spread duration times the spread change (Chapter 8 has the full decomposition):

$$
r^{\text{xs}}_{i,t} \;\approx\; s_{i,t-1}\,\Delta t \;-\; D^{\text{spr}}_{i,t-1}\,\Delta s_{i,t}.
$$

If spread changes are proportional to spread levels (the Ben Dor result quoted in §7.3), write $\Delta s_{i,t} = s_{i,t-1}\,\Delta \log s_{i,t}$. Then the volatility term is

$$
D^{\text{spr}}_{i,t-1}\,\Delta s_{i,t} \;=\; \underbrace{D^{\text{spr}}_{i,t-1}\, s_{i,t-1}}_{\text{DTS}_{i,t-1}}\;\Delta \log s_{i,t}
\quad\Longrightarrow\quad
\sigma\big(r^{\text{xs}}_{i}\big) \;\approx\; \text{DTS}_{i}\,\sigma_{\text{rel}},
$$

where $\sigma_{\text{rel}} = \sigma(\Delta \log s)$ is the relative spread volatility per period. Units matter here: with $D^{\text{spr}}$ in years and $s$ in decimal, a five-year bond at 400bp has $\text{DTS} = 5 \times 0.04 = 0.20$; with $\sigma_{\text{rel}} = 10\%$ per month, its excess-return volatility is about $0.20 \times 0.10 = 2\%$ per month.

> **[SOURCE EXTRACTION]** *Ben_Dor_Quantitative_Credit_Portfolio_Management p.50:* "a portfolio with a weighted spread of 200 bps and spread duration of two years is equally risky as a portfolio with a spread of 100 bps and spread duration of four years."
>
> **Annotation.** Both portfolios have the same DTS (2 × 200 = 4 × 100 = 400 in the bp-years convention), so they get the same barrier. That is the entire argument for DTS-scaled labels, in one sentence. A barrier set at a fixed 2% would label the long-duration IG bond's ordinary month as an event and the HY bond's ordinary month as nothing. A DTS barrier puts both on a common risk clock. Ben Dor's group also estimates the slope of excess-return volatility on DTS directly: 8.8% per month for corporates, and 9.8% for the Aaa Agency debentures used as a cross-check on p.57 (with DTS measured in years × percent, so a DTS of 20 maps to roughly $0.088 \times 20 \approx 1.8\%$ per month). That slope *is* $\sigma_{\text{rel}}$, so the book's default prior for the barrier scale is "about 9–10% relative spread volatility per month" before any estimation, and an estimated $\hat\sigma_{\text{rel},t}$ that comes out at 3% or 30% should trigger a data check, not a celebration. The modern departure: estimate $\hat\sigma_{\text{rel},t}$ with an exponentially weighted window per rating bucket, because the 2022 and April 2025 episodes showed relative vol itself moves with the regime.

**The barriers.** For bond $i$ at formation date $t$, let $X_{i,t}(u) = \sum_{v=1}^{u} r^{\text{xs}}_{i,t+v}$ be cumulative excess return after $u$ days, and let $h$ be the horizon in the same units as $\hat\sigma_{\text{rel}}$. Define

$$
\bar b_{i,t} = +\,\bar m\;\text{DTS}_{i,t}\,\hat\sigma_{\text{rel},t}\sqrt{h},
\qquad
\underline b_{i,t} = -\,\underline m\;\text{DTS}_{i,t}\,\hat\sigma_{\text{rel},t}\sqrt{h},
$$

with a vertical barrier at $u = h$. The label is $y_{i,t} = +1$ if $\bar b$ is touched first, $-1$ if $\underline b$ is touched first, and $\operatorname{sign}\big(X_{i,t}(h)\big)$ at the vertical barrier (optionally $0$ inside a dead zone $|X| < \epsilon$). Record the touch time $t_{1,i}$. The *label interval* $[t_{0,i}, t_{1,i}]$ with $t_{0,i}=t$ is the object that §7.6 and §7.7 need: it defines which labels overlap and therefore which ones must be purged.

**Strip the carry, or the label learns the coupon.** Here is a number that surprises people. Take $h = 13$ weeks $= 3$ months, $\text{DTS} = 0.20$, $\sigma_{\text{rel}} = 10\%$ per month, $\bar m = \underline m = 1$. The barrier half-width is $0.20 \times 0.10 \times \sqrt 3 \approx 3.5\%$. A 500bp bond accrues carry of $0.05 \times 0.25 = 1.25\%$ over the same 13 weeks, about 36% of the barrier width *(illustrative)*. Raw excess-return labels in high yield are therefore tilted toward $+1$ by carry alone, and a model trained on them learns to buy the highest-spread bonds, which is the always-long-carry strategy with extra steps. Build the labels on carry-adjusted, market-beta-stripped residual returns (the IDO return of Chapter 8) instead. The desk motto applies to labels too: IDO or it didn't happen.

**The trapdoor.** In credit the lower barrier is not a wall you bump into; it is a trapdoor. A jump-to-default or a priming announcement moves the price from 92 to 55 between two marks, so the label is $-1$ and the realized return at touch is many barrier-widths below $\underline b$. Two consequences. First, keep the realized return at touch, $X_{i,t}(t_{1,i}-t)$, alongside the sign; §7.6 uses it for return-attribution weights, and the sizing layer in §7.5 needs to know that $-1$ labels in CCC carry fatter losses than $+1$ labels carry gains (Chapter 5's mixture distributions). Second, consider $\underline m < \bar m$ for the lowest ratings: a tighter stop on the side where the distribution has a jump component matches how a risk manager would actually run the position.

**The 13-week model, reborn.** How long should $h$ be? Theo's answer was immediate, and for once the data agrees with the emotional-support USB stick.

> **[SOURCE EXTRACTION]** *Dynkin_Systematic_Investing_in_Credit p.611:* "The number of issuers that remain above median drops by 31% in the first month after momentum signal formation. After six months, 52% of issuers drop out."
>
> **Annotation.** This is signal-decay evidence for equity-momentum-based bond portfolios, and it sets the vertical barrier. If a third of the signal's membership churns in month one and half by month six, a 12-month label mostly measures what happened *after* the information was spent, and adds overlap (every daily label shares 11 months with its neighbor) without adding evidence. The book's default is $h = 13$ weeks, which sits where Dynkin's evidence says most of the effect has arrived and also where Theo's 13-week cash flow model has always stopped forecasting. That running gag is now a hyperparameter. The departure: decay rates differ by signal family. Value signals in credit decay more slowly than momentum (Chapter 9), so a value label can justify a longer vertical barrier, and the purging in §7.7 must then widen with it.

**Censoring: when the bond leaves before the label finishes.** Bonds exit through calls, tenders, maturities, defaults, and exchanges. The practitioner literature has a standard way of handling exits in *portfolio* studies:

> **[SOURCE EXTRACTION]** *Ben_Dor_Quantitative_Credit_Portfolio_Management p.338:* "If an issuer left the sample before the end of the analysis window, because all its outstanding bonds matured, were called, or defaulted, we assumed that it continued to earn the same return as its peer group for all remaining months."
>
> **Annotation.** For the question Ben Dor's group was asking (how fallen angels perform relative to peers over a long window), peer-return imputation is sensible: it keeps the cohort intact and prevents the survivors-only bias that would flatter the distribution. For a *supervised label*, the same move is a leak. The exit itself carries information. A tender at a premium is a positive outcome the model should learn to anticipate, and a distressed exchange (an "open market purchase" in a trench coat) is a negative one. Replacing either with the peer-group return teaches the model that exits are average, which is exactly backward. The label rule for this book: close the label at the exit date and exit value (the tender price, the call price, or the market value of the exchange package), set `touch = "exit"`, record the exit type, and set `censored = True` when the exit occurs before the vertical barrier. The model sees what really happened, and the analyst can later decide whether to train on censored labels, drop them, or model exits as a competing risk (Chapter 14).

> **Ways This Blows Up.** *Touches on stale marks.* A barrier "touch" on an evaluated price that reverts the next day is not an event; it is the pricing service sneezing. Require a touch to be confirmed by an institutional-size print, or by two consecutive marks beyond the barrier, before closing the label. The 2026 replication literature added a bounce-back filter to TRACE cleaning for the same reason (Dickerson, Robotti, and Rossetti 2026): a price that jumps and immediately jumps back is usually an error. And never compute the feature and the first day of the label from the same month-end price; §7.9 shows that this single shortcut manufactured most of a published factor.

## 7.5 Meta-Labeling: The RSSG Analyst as the Primary Model

Here is the chapter's main idea for the reader who came from restructuring: **you already do meta-labeling for a living.** A restructuring banker never asks "will this bond go up?" The questions are "is the thesis right," "how confident am I," and "how much do we put on." López de Prado's meta-labeling splits the problem in exactly that way. A *primary model* decides the side. A *secondary model* is trained only to predict whether the primary is right, and its probability becomes the bet size.

The division of labor is the whole point. The pure quant cannot build a good primary model for special situations, because the primary model is legal prose converted into state space: drop-down capacity in the unrestricted-subsidiary basket, an open-market-purchase clause loose enough to drive a Serta uptier through, a 13-week liquidity runway that ends before the next coupon. That is the Priming Risk Score of Chapter 13, the structural distance-to-default of Chapter 6, and the cash runway Theo keeps on the USB stick. The banker, meanwhile, has never been made to estimate the *precision* of their own calls, let alone condition it on the spread regime, the sector, or how many dealers are already short the bond. Meta-labeling is where the two halves meet.

**The math.** The primary model produces a side $\hat y^{(1)}_{i,t} \in \{-1, +1\}$. Given the triple-barrier label $y_{i,t}$ from §7.4, define the meta-label

$$
y^{(2)}_{i,t} = \mathbf 1\big\{\hat y^{(1)}_{i,t}\, y_{i,t} > 0\big\},
$$

that is, 1 when the primary was right. The secondary model estimates $p_{i,t} = \mathbb{P}\big(y^{(2)}_{i,t} = 1 \mid \mathcal{F}_t\big)$ from features the primary does not use (spread regime, staleness, dealer positioning, issuer dispersion). Map the probability to a size with the test statistic for "is $p$ different from a coin flip":

$$
z_{i,t} = \frac{p_{i,t} - \tfrac12}{\sqrt{p_{i,t}(1-p_{i,t})}},
\qquad
m_{i,t} = 2\,\Phi(z_{i,t}) - 1 \in (-1, 1),
\qquad
\text{size}_{i,t} = \max(m_{i,t}, 0)\cdot \hat y^{(1)}_{i,t}.
$$

Here $\Phi$ is the standard normal CDF. The numbers are worth memorizing: $p = 0.5$ gives size 0; $p = 0.75$ gives $z = 0.25/0.433 = 0.58$ and $m \approx 0.44$; $p = 0.9$ gives $z = 0.4/0.3 = 1.33$ and $m \approx 0.82$. Truncating at zero means the secondary can only shrink or veto a primary call, never reverse it. That is deliberate: the secondary model knows *when* the analyst is reliable, not *what* the analyst knows.

> **Poker Table.** Ines, to Theo: "Your read on the covenant is your hand. The meta-model is the part of you that remembers how often that hand wins at *this* table, with *these* players, at *this* hour. You don't bet your opinion. You bet your confidence in your opinion. Most people at this table bet their opinion, which is why I like this table." Then, replaying the hand history: "Your drop-down calls were right 61% of the time overall. When the bond had already moved five points on no news, you were right 78% of the time, because someone else had read the same basket. When the bond hadn't moved, 52%. Same hand, different table. Size accordingly."

**Precision, recall, and the marketing sentence.** The primary should be tuned for *recall* (never miss a candidate trapdoor) and the secondary for *precision* (only bet when the call is likely right). The desk pays for the combination, summarized by $F_1 = 2PR/(P+R)$. A real-world sentence shows why reporting one side of this trade-off is uninformative.

> **[SOURCE EXTRACTION]** *BlackRock_Systematic_High_Yield_Credit p.6:* "Our proprietary probability of default signal that has underpinned all of our credit strategies for over 20 years has successfully identified 77% of the defaulted bonds in the ICE BofA High Yield Index within 24 months of its default since 2010."
>
> **Annotation.** Seventy-seven percent is a *recall*: of the bonds that defaulted, the share that had been flagged. It is a perfectly honest number, and on its own it tells you nothing about how useful the signal is, because a signal that flags every bond in the index has 100% recall. A marketing sentence is a confusion matrix with one cell filled in; ask for the other three. Here is an illustration with made-up round numbers *(illustrative, not BlackRock's)*: a 1,000-bond universe with a 6% 24-month default rate has 60 defaulters, so 77% recall catches about 46 of them. If the signal flags 200 bonds, precision is $46/200 = 23\%$, nearly four times the 6% base rate: a valuable underweight list. If it flags 400 bonds, precision is 11.5% and the lift is under 2×. Same recall, very different signal. The page also says the signal's logic is structural (default when asset value falls below liabilities), which makes it a natural *primary* model in our framework: high-recall, economically grounded, and in need of a secondary model to say when its flags deserve size.

> **Ways This Blows Up.** *Three meta-labeling leaks.* (1) **Training the secondary on in-sample primary calls.** If the primary model was fit on the same data, its calls are overfit and look right too often; the secondary learns to trust an illusion. Generate primary calls out of sample (walk-forward) *before* building meta-labels. (2) **Class imbalance from carry.** If the primary is "long high spread" and HY drifts up on carry, the primary is right about 70% of the time *(illustrative)* and "always bet" has 70% accuracy. Report $F_1$, the Brier score, and the IDO-stripped PnL, never raw accuracy. (3) **Feeding the primary's score as a feature without normalizing it.** A PRS distribution that drifts as documents get looser (2020–2026 saw exactly this, Chapter 13) is a non-stationary feature; rank-transform it within each date.

## 7.6 Sample Weights: Uniqueness and the Forty-Seven-Hat Problem

Return to the cold open. Kaz's 212,000 bond-months were not 212,000 pieces of evidence, for two separate reasons. *Time overlap:* if a label is formed every day with a 13-week vertical barrier, each label shares most of its window with the 60-odd labels on either side of it. *Sibling overlap:* if an issuer has eleven bonds, eleven labels formed on the same day mostly record the same issuer news at eleven durations. Both inflate the count; neither adds information. The fix is to weight each label by how much of its window it shares with no one else.

**Uniqueness, defined.** For label $i$ with interval $[t_{0,i}, t_{1,i}]$ on bond $b(i)$ of ultimate parent $g(i)$, define the *issuer concurrency* at date $t$ as the number of labels on any bond of the same parent that are live at $t$:

$$
c^{\text{iss}}_{g,t} \;=\; \sum_{j\,:\,g(j) = g} \mathbf 1\{t_{0,j} \le t \le t_{1,j}\}.
$$

The *average uniqueness* of label $i$ is the average, over its own window, of the share of the issuer's live labels it represents:

$$
\bar u_i \;=\; \frac{1}{t_{1,i} - t_{0,i} + 1}\sum_{t = t_{0,i}}^{t_{1,i}} \frac{1}{c^{\text{iss}}_{g(i),t}} \;\in\; (0, 1].
$$

Counting concurrency within the parent, rather than across the whole universe, is the credit-specific choice. López de Prado's original definition counts every concurrent label in a single series. In a cross-section, two labels from *different* issuers on the same day are not duplicates: they carry different idiosyncratic news, and their shared market component is handled by the cross-validation purge in §7.7. Two labels from the *same* parent on overlapping windows are duplicates in the sense that matters, because the default, the LMT, and most of the idiosyncratic spread variance are parent-level events. Counting within the parent therefore corrects for both time overlap (the same bond's neighboring labels) and sibling overlap (the other bonds) in one formula.

**The hat count.** The sum of uniquenesses, $N_{\text{eff}} = \sum_i \bar u_i$, is approximately the number of non-overlapping issuer-windows in the data. Check it on the simplest case: one issuer with $B$ bonds, daily labels for $T$ days, horizon $h$. Concurrency is about $Bh$ in the interior, so each label has $\bar u_i \approx 1/(Bh)$, and $N_{\text{eff}} \approx BT \cdot 1/(Bh) = T/h$, independent of $B$. Eleven bonds, one hat. Now scale up *(illustrative)*: 800 parents, about three bonds each, 20 years of daily labels ($T \approx 5{,}000$ trading days) with $h = 63$ days gives about 12 million label rows, roughly 576,000 bond-months, and

$$
N_{\text{eff}} \;\approx\; 800 \times \frac{5{,}000}{63} \;\approx\; 63{,}000.
$$

That is about one-ninth of the bond-month count and one two-hundredth of the label count. And it is still an *upper bound* on the independent evidence for any conclusion that depends on the market regime, because all 800 issuers live through the same 79 non-overlapping 13-week windows. A model that times high yield as a whole has about 79 observations, not 63,000. Print $N_{\text{eff}}$ next to every backtest result. If ROBO is told nothing else in this chapter, it should be told that.

**From uniqueness to weights.** Use $\bar u_i$ as a sample weight in the loss function, so that duplicated labels share one unit of influence. Two refinements are standard. *Return attribution* multiplies by the absolute residual return the label earned, attributed by concurrency, $\big|\sum_{t} r^{\text{xs}}_{i,t}/c^{\text{iss}}_{g(i),t}\big|$, so that windows in which something happened count more than windows in which nothing did. Use it with care in credit, where a few default jumps will dominate the weights. *Time decay* down-weights old labels linearly or exponentially, which is a crude but honest admission that the 2005 market is not the 2026 market. Normalize weights to sum to the number of labels so that regularization strengths keep their meaning, and when weights are unequal, report the Kish effective size $(\sum w_i)^2/\sum w_i^2$ as well.

**The sequential bootstrap, sketched.** Bagging over overlapping labels has the same disease: a bootstrap sample drawn uniformly is full of near-duplicates, so the bagged trees are more correlated than they look. The sequential bootstrap draws labels one at a time, each with probability proportional to its average uniqueness *given the labels already drawn*, so the sample spreads itself across distinct windows. In a credit panel, run it within parent groups (draw parents first, then labels within a parent), which is the block bootstrap the RSSG reader would have invented anyway: you would never test a recovery model by resampling the same company's eleven bonds as eleven independent bankruptcies.

## 7.7 Cross-Validation That Cannot Peek: Purged, Embargoed, Issuer-Grouped

Kaz's in-sample Sharpe of 2.9 had a cousin: a cross-validated Sharpe of 1.8 from shuffled K-fold, which Kaz considered the conservative number. It was not. Shuffled K-fold on overlapping labels puts the label formed on Tuesday into the test fold and the nearly identical labels formed on Monday and Wednesday into the training fold. The model then "predicts" Tuesday by remembering Monday. The leakage is mechanical, not subtle, and it is fatal in credit, where labels are long and issuers repeat.

The credit-risk modeling tradition knew a version of this decades before machine learning arrived on bond desks.

> **[SOURCE EXTRACTION]** *Bohn_Stein_Active_Credit_Portfolio_Management p.465:* "Finally, the most robust procedure is shown in the lower right quadrant and should be the preferred sampling method for credit risk models. In addition to being segmented in time, the data are also segmented across the population of obligors."
>
> **Annotation.** Bohn and Stein's validation figure is a two-by-two grid: split by time or not, split by obligor or not. Their preferred quadrant splits both ways at once, so no obligor in the test set was seen in training and no test date precedes the training window. That is purged, issuer-grouped cross-validation, described for default models before the term existed. What the modern desk adds is precision about *where* the split sits. Labels have duration, so a time split must remove training labels whose windows overlap the test window (the purge), plus a buffer after the test window (the embargo). Issuers have org charts, so the obligor split must group at the ultimate parent, not at the ticker. The quadrant was right; the boundaries need to be drawn in label time and in corporate-family space.

**The purge, formally.** Let the test fold be the set of labels $\mathcal T$, spanning label time $[T_0, T_1]$ with $T_0 = \min_{i \in \mathcal T} t_{0,i}$ and $T_1 = \max_{i \in \mathcal T} t_{1,i}$. A training label $j$ is purged if its interval overlaps the test span:

$$
t_{0,j} \le T_1 \quad\text{and}\quad t_{1,j} \ge T_0.
$$

**The embargo.** Even after purging, features computed from trailing windows leak forward: a 12-month momentum feature for a training label formed just after $T_1$ is built from prices *inside* the test window. So also drop training labels with $t_{0,j} \in (T_1, T_1 + \eta]$, where $\eta$ is at least the longest feature lookback that touches price data. The textbook default is $\eta \approx 1\%$ of the sample length. In credit, set $\eta$ to the maximum of that and the feature lookback, which usually makes it months, not days. Mags, on the embargo: "So the model isn't allowed to call the bond desk for a month after the test. Fine. Neither were we, after Enron."

**The group.** Assign every label to a fold by ultimate parent, so no parent appears on both sides. Grouping removes *issuer-specific* leakage: the model cannot learn in training that this particular company defaulted in 2021 and then "predict" its 2019 deterioration in the test. Grouping does *not* remove *time* leakage through the common factor, because other issuers' labels from the same weeks still carry the market move. Purging does not remove issuer leakage, because a parent's labels from other years still identify the parent. You need both. The resulting scheme is a two-way split: the test set is (parents in group $G_k$) during (time block $B_m$); the training set is (parents not in $G_k$) during (times outside $B_m$, purged and embargoed). With $K$ parent groups and $M$ time blocks, each test fold trains on roughly $(1 - 1/K)(1 - 1/M)$ of the data, less the purge. That is expensive. It is also the true price of an honest estimate, and it is cheaper than finding out in production.

**Group by parent, not ticker, especially in the LMT era.** The interesting bonds of 2016–2026 often live in entities created to receive assets: the unrestricted subsidiary that received J.Crew's intellectual property, the new-money super-priority tranche issued through a fresh financing SPV, the HoldCo and OpCo notes of the same family. A ticker-level grouping sends the drop-down entity to the training fold and the parent to the test fold, and the model learns the parent's fate from the child's price. The grouping key is the corporate-family tree from the security master (Chapter 27), and the RSSG reader is the person on the desk best qualified to audit it.

**Walk-forward is the special case you already trust.**

> **[SOURCE EXTRACTION]** *Bohn_Stein_Active_Credit_Portfolio_Management p.467:* "Fit the model using all the data available on or before the selected year. Once the model's form and parameters are established for the selected time period, generate the model outputs for all the firms available during the following year"
>
> **Annotation.** This is walk-forward testing, step two and step three of Bohn and Stein's recipe: fit through year $y$, predict year $y+1$, roll. It is a purged CV in which the folds are ordered and the embargo is implicit (nothing after the training window is ever used), and it emulates how the model will actually be run. Its weakness is that it produces *one* backtest path, so its performance estimate has the variance of a single history, and the early folds train on very little data. Combinatorial purged cross-validation (CPCV) generalizes it: split the time axis into $N$ blocks, choose every combination of $k$ blocks as the test set, purge and embargo around each, and stitch the test predictions into $\binom{N}{k}\,k/N$ distinct backtest paths. For $N = 6$ and $k = 2$ that is 15 splits and 5 paths, enough to see a *distribution* of Sharpe ratios rather than one lucky number. Run walk-forward as the production rehearsal and CPCV as the research diagnostic, and keep the parent grouping in both.

And then there is the footnote that every credit modeler should have taped to the monitor, right below the issuer count.

> **[SOURCE EXTRACTION]** *Bohn_Stein_Active_Credit_Portfolio_Management p.466:* "It can be argued that there is no truly honest out-of-sample test since most modelers use portions of the data to test early models as they converge on a functional form for the model."
>
> **Annotation.** Footnote 31 is the bridge from cross-validation to multiple testing. Purging and grouping protect a *single* model evaluation from leakage. They do nothing about the fact that the modeler evaluated forty versions, looked at the test results each time, and kept the best. Each glance at the test fold turns it, a little, into training data. That is the 2019–2026 bond-factor story in one sentence, and it is why the next section exists. The practical response is to log every evaluation (the trial count $N$ in §7.8 is a number you *record*, not one you estimate afterwards) and to lock away a final hold-out period that no one is allowed to look at until the research is frozen.

> **Ways This Blows Up.** *Four ways a purged CV still leaks.* (1) Purging on calendar months while labels are event-timed: a label that closed early at a barrier has a shorter interval, and one that closed late (a stale mark held it open) has a longer one. Purge on the recorded $t_{1,i}$, not on the nominal horizon. (2) Forgetting that fractional differentiation (§7.3) has a window of up to $K \approx 280$ days, which is a feature lookback and therefore sets the embargo. (3) Hyperparameter search *outside* the CV loop: choosing the tree depth on the full sample and then cross-validating the chosen depth. Nest the search inside each training fold. (4) Cross-sectional standardization (z-scoring features by date) is safe; *global* standardization with full-sample means and standard deviations is a small look-ahead that compounds with everything else.

## 7.8 Multiple Testing and the Deflated Sharpe Ratio

Purging makes one evaluation honest. It does not make the *best of many* evaluations honest. Kaz tried about 3,000 configurations, so the right question about the winner is Ines's: how good would the best of 3,000 hands look if every hand were dealt at random?

> **Poker Table.** "The deflated Sharpe ratio asks the only question that matters about a guy showing you his winning hands: how many did he fold first? And the embargo is the dealer burning a card. You don't get to see the card right after the one you bet on, because that card is correlated with yours."

**The expected maximum of noise.** Suppose $N$ strategies have true Sharpe zero and their estimated Sharpe ratios are roughly normal with variance $V = \operatorname{Var}[\widehat{SR}_n]$ across trials. Extreme-value theory gives the expected maximum (Bailey and López de Prado, *The Deflated Sharpe Ratio*, 2014; the bound is the "false strategy theorem" of their 2021 paper):

$$
SR^\ast \;=\; \mathbb{E}\Big[\max_n \widehat{SR}_n\Big] \;\approx\; \sqrt{V}\,\Big[(1-\gamma)\,\Phi^{-1}\!\Big(1 - \tfrac1N\Big) + \gamma\,\Phi^{-1}\!\Big(1 - \tfrac{1}{N e}\Big)\Big],
$$

where $\gamma \approx 0.5772$ is the Euler–Mascheroni constant and $e$ is Euler's number. Put in Kaz's numbers *(illustrative)*: $N = 3{,}000$ trials on $T = 240$ months gives $V \approx 1/T$ for monthly Sharpe ratios near zero, so $\sqrt V \approx 0.065$. The quantiles are $\Phi^{-1}(1 - 1/3000) \approx 3.40$ and $\Phi^{-1}(1 - 1/8155) \approx 3.67$, so

$$
SR^\ast \approx 0.065 \times (0.423 \times 3.40 + 0.577 \times 3.67) \approx 0.065 \times 3.56 \approx 0.23 \text{ per month} \approx 0.80 \text{ annualized}.
$$

The best of 3,000 *pure-noise* strategies over 20 years shows an annualized Sharpe of about 0.8. That is the bar *before* the model has done anything.

**The probabilistic and deflated Sharpe ratios.** With $T$ observations, sample Sharpe $\widehat{SR}$ (per period), sample skewness $\hat\gamma_3$, and sample kurtosis $\hat\gamma_4$ (not excess), the probability that the true Sharpe exceeds a benchmark $SR_0$ is

$$
\widehat{\text{PSR}}(SR_0) \;=\; \Phi\!\left[\frac{(\widehat{SR} - SR_0)\sqrt{T-1}}{\sqrt{1 - \hat\gamma_3\,\widehat{SR} + \frac{\hat\gamma_4 - 1}{4}\,\widehat{SR}^2}}\right].
$$

The denominator is the standard error of a Sharpe estimate under non-normal returns: negative skew ($\hat\gamma_3 < 0$) and fat tails ($\hat\gamma_4 > 3$) both widen it, and monthly high-yield excess returns have both. The *deflated* Sharpe ratio sets the benchmark to the noise maximum, $\widehat{\text{DSR}} = \widehat{\text{PSR}}(SR^\ast)$. Run Kaz's winner through it: with $\widehat{SR} = 0.23$, $T = 240$, $\hat\gamma_3 = -0.5$, $\hat\gamma_4 = 5$ *(illustrative)*, the denominator is $\sqrt{1 + 0.115 + 0.053} \approx 1.08$ and $\widehat{\text{PSR}}(0) = \Phi(0.23 \times 15.5 / 1.08) = \Phi(3.3) \approx 0.9995$. A naive report says 99.95% confident. The deflated ratio, with $SR_0 = SR^\ast = 0.23$, is $\Phi(0) = 0.5$: a coin flip. The best noise strategy is, by construction, about as good as the expected best noise strategy.

Two companion statistics belong in every report. The **minimum track record length** is the number of periods needed for $\widehat{\text{PSR}}(SR_0)$ to reach confidence $1-\alpha$:

$$
T^\ast = 1 + \Big[1 - \hat\gamma_3\,\widehat{SR} + \tfrac{\hat\gamma_4 - 1}{4}\,\widehat{SR}^2\Big]\left(\frac{z_{1-\alpha}}{\widehat{SR} - SR_0}\right)^2.
$$

The **probability of backtest overfitting** (PBO; Bailey, Borwein, López de Prado, and Zhu 2017) uses combinatorially symmetric cross-validation (CSCV). Split the $T \times N$ matrix of trial returns into $S$ time blocks. For each of the $\binom{S}{S/2}$ ways to choose half the blocks as "in-sample," find the in-sample best trial $n^\ast$, compute its relative rank $\bar\omega \in (0,1)$ among all trials out of sample, and take the logit $\ell = \log\big(\bar\omega/(1-\bar\omega)\big)$. PBO is the share of splits with $\ell \le 0$: how often the in-sample winner is below median out of sample. Noise gives PBO near 0.5. Skill gives PBO near 0.

**Thresholds from the literature.** Harvey, Liu, and Zhu (*Review of Financial Studies*, 2016) catalogued 316 equity factors and argued that a new factor should clear $t > 3.0$, not 2.0. Chordia, Goyal, and Saretto (*RFS*, 2020), using more than two million random strategies, put the bar near $t \approx 3.8$ for time-series tests and $3.4$ for cross-sectional ones. The 2026 bond audit used Benjamini–Hochberg false-discovery control and found that 6% of specifications survive (§7.2). Paleologo frames the same discipline for the PM seat:

> **[SOURCE EXTRACTION]** *Paleologo_Advanced_Portfolio_Management p.159:* "there are ways to assign a "Sharpe haircut" to a backtested strategy. This is a quantitative topic and you could work with a quantitative analyst to establish some selection principle"
>
> **Annotation.** The surrounding page draws the line that matters: a *confirmatory* test (you believe a specific dataset improves a specific estimate, so you add it and check) versus an *exploratory* search (you try many combinations and keep the best). Confirmatory tests deserve something close to their nominal $t$-statistic; exploratory searches deserve a haircut that grows with the number of trials, and the deflated Sharpe ratio is one explicit form of that haircut. For the ex-RSSG reader, this is the most transferable idea in the chapter: a covenant-driven primary model (§7.5) is confirmatory by nature, because the hypothesis ("loose open-market-purchase language predicts uptier losses") was written down before the data was touched, while a gradient-boosted search over 81 features is exploratory by nature. Report them differently. Where the modern desk goes further: the trial count $N$ must include *every* configuration evaluated, by anyone on the team, on the same data, and correlated trials should be collapsed by clustering the trial-return correlation matrix into an effective number of independent trials, so that 400 near-identical momentum variants count as a handful, not as 400.

> **Ways This Blows Up.** *Your Sharpe is inflated before you deflate it.* Smoothed marks lower measured volatility (§7.1), so a backtest on evaluated prices overstates $\widehat{SR}$, and positive autocorrelation from staleness means the usual $\sqrt{12}$ annualization overstates it again (the variance of a sum of positively autocorrelated returns exceeds the sum of variances). Unsmooth returns first, or compute Sharpe from executable prices only, and use an autocorrelation-adjusted annualization. Deflation corrects for *search*; it cannot correct for a numerator and denominator that were both measured on rumors.

## 7.9 The Two Biases That Built the Bond-Factor Zoo

Kaz's contribution to this section came on a Tuesday. Kaz had found the TRACE field `As Of Indicator`, seen that a value of `R` means "reversal," and spent the morning building a short-term-reversal factor out of trade cancellations. Theo had to explain that in FINRA's historic TRACE layout, a reversal is the cancellation of a trade reported more than 20 business days earlier, which is a data-cleaning event, and that a reversal *factor* is a different thing. Both, he added, would ruin your month. Then he realized the joke had a serious point, because the second kind of reversal had been built out of something almost as accidental as the first.

**Latent implementation bias: noise in both the signal and the return.** Let the observed log price be the true log price plus noise, $\tilde p_t = p_t + \delta_t$, where $\delta_t$ is i.i.d. with variance $\sigma_\delta^2$ (bid–ask bounce, a stale mark, a dealer-side mix). The observed returns are

$$
\tilde r_t = r_t + \delta_t - \delta_{t-1},
\qquad
\tilde r_{t+1} = r_{t+1} + \delta_{t+1} - \delta_t .
$$

The two returns share $\delta_t$ with opposite signs. With the true returns independent of the noise,

$$
\operatorname{Cov}(\tilde r_t, \tilde r_{t+1}) \;=\; \operatorname{Cov}(r_t, r_{t+1}) \;-\; \sigma_\delta^2 .
$$

Pure noise manufactures reversal. A portfolio that buys last month's losers and sells last month's winners is, in part, buying bonds whose month-end price was recorded too *low* ($\delta_t < 0$) and selling bonds recorded too *high*, then collecting $-\delta_t$ when the next price is drawn fresh. The premium is real in the data and unavailable in the market, because you cannot buy at the mis-recorded price. This is Roll's (1984) bid–ask model wearing a factor's clothes: Chapter 18 uses the same covariance to *estimate* the spread, as $2\sqrt{-\operatorname{Cov}}$. Dickerson, Robotti, and Rossetti (2026) call the general problem latent implementation bias, because the same noisy price sits in the sort and in the denominator of the next return.

**The fix is a gap.** Form the signal from the month-end price, but measure the return from the first feasible execution price the next month (the "month-begin" price), so the two prices are different draws of noise:

$$
\tilde r^{\text{gap}}_{t+1} = (p_{t+1} + \delta_{t+1}) - (p_{t^+} + \delta'_{t^+}),
\qquad
\operatorname{Cov}(\delta'_{t^+}, \delta_t) = 0
\;\Longrightarrow\;
\operatorname{Cov}(\tilde r_t, \tilde r^{\text{gap}}_{t+1}) = \operatorname{Cov}(r_t, r_{t^+ \to t+1}).
$$

The 2026 numbers show how much of the zoo the gap removes. Short-term reversal goes from −0.99% per month to −0.09%, so more than 90% of the documented effect was bias. Across the zoo, 43–67% of the 30 price-based factors show a significant gap between month-end and month-begin premia, against 10–18% of the 78 non-price-based factors. That asymmetry is the fingerprint of noise rather than economics: if the premia were real compensation for risk, the timing of the first trade would not matter much.

**Look-ahead bias in the return filter.** The second bias is quieter. Researchers winsorize or trim extreme returns to protect against data errors, which is reasonable. But if the thresholds are percentiles computed from the *full sample*, the filter uses future information. If the trimming is *asymmetric* (cutting the left tail harder than the right, or deleting returns around defaults), it deletes exactly the outcomes a long-short portfolio is most exposed to, and it chooses them with knowledge of which bonds were about to crash. Dickerson, Robotti, and Rossetti report that 6-month momentum's 0.30% per month premium comes entirely from asymmetric ex-post winsorization and is zero without it, and that 57–78% of the alpha of idiosyncratic-volatility and downside-risk factors comes from ex-post filtering. Their measure of "researcher degrees of freedom" is also worth knowing: across 648 filtering configurations, the interquartile range of factor premia averages 0.35% per month against an average premium of 0.33%. The choice of cleaning rule moves the answer by more than the answer.

The fix is ex-ante filtering: thresholds computed only from data available at the formation date, applied symmetrically, with returns around defaults *kept* (Dick-Nielsen and coauthors made the same choice). A model that never sees a default in training will be very confident about bonds that are about to default. That is not caution; it is a CLO manager's nightmare with a nice ROC curve.

## 7.10 Trend Watch: The ML-for-Bonds Frontier and the Data Stack

> **Trend Watch.** *Machine learning reaches corporate bonds, 2017–2026.*
>
> - **May 2017.** MarketAxess launches Composite+ (CP+), an ML-built pricing engine, after about 18 months of experimentation; by the company's later account it covers more than 350,000 bonds and refreshes as often as every 15 seconds (company claims, reported by FI Desk). The SMU Cox study cited in §7.1 (March 2026) finds CP+ more informative about future trade prices than the last trade, tracking efficient prices well in March 2020 but converging slowly during fire sales. AI composites are now both a *feature* (a better denominator than the last print, which shrinks latent implementation bias) and a *counterparty* (the price a market maker is adversely selected against; Chapter 18).
> - **2021.** Bianchi, Büchner, and Tamoni, "Bond Risk Premiums with Machine Learning," *RFS* 34(2), on Treasuries, followed by a corrigendum in the same volume (§7.11).
> - **2023.** Kelly, Palhares, and Pruitt, "Modeling Corporate Bond Returns," *Journal of Finance* 78(4): a conditional five-factor model (IPCA) with loadings driven by bond characteristics. Robeco (23 June 2023) describes regression-tree fair-value models for credit value investing, with the main benefit reported as lower active risk, especially in high yield.
> - **2025.** Feng, He, Wang, and Wu, "Predicting individual corporate bond returns," *Journal of Banking & Finance* 171, report an out-of-sample $R^2$ of 4.48%; their leading predictors include downside risk, short-term reversal, and skewness, three of the price-based signals the 2026 audit flags for latent implementation bias. BondBERT (arXiv:2511.01869, October 2025) fine-tunes a language model on about 30,000 UK bond-news articles, because good news for a company's equity is often bad news for its bonds.
> - **2026.** Bell, Kakhbod, Lettau, and Nazemi, "Glass Box Machine Learning and Corporate Bond Returns" (NBER WP 33320; *JFE* 181, 2026), use an explainable boosting machine with 81 predictors on 1,207 firms (July 2002–August 2020), with a deliberately long nine-year test window; the value-weighted 10−1 portfolio earns 0.67% per month with an alpha of 0.55% ($t = 4.22$). The most important interaction is financial-uncertainty shocks times spread, which is a structural-model prediction (Chapter 6) rediscovered by a model that can show its work.
> - **Market plumbing.** SIFMA reports US corporate-bond average daily volume of \$66.7 billion through September 2026, up 13.4% year on year (fetched 2026-10-17). Man Group's 2022 paper notes that, per one data provider, less than \$150 billion of US bonds had been traded electronically by quantitative investors in the prior year (Man 2022 p.3).
>
> *What it means for the desk.* The frontier moved from "can ML predict bond returns?" (2019–2021) to "can we trust the inputs?" (2023–2026) to "can the model explain itself?" (2026). The models that held up share three traits: long, untouched test windows; firm-level aggregation (one hat per issuer); and economic structure built in (Merton links, interpretable shape functions).

> **[SOURCE EXTRACTION]** *Blackstone_Systematic_Credit p.2:* "While systematic strategies manage roughly 20% of global equities, they account for less than 2% of the fixed-income universe."
>
> **Annotation.** The adoption gap is the commercial case for this chapter and also a warning. A tenfold gap means the field is early, and early fields reward the managers who get the data right: Blackstone's own paper credits electronic trading, better pricing data, and computing power for closing it. But the same gap means most of the published evidence was produced on short samples by people who had never traded the bonds, which is how a four-factor model got retracted. Man Group's 2022 forecast was that "the future of quant credit will be one of increasing data sophistication, of the increasing use of machine learning" (Man 2022 p.41); the 2023–2026 record says the order of those two clauses matters. Data sophistication comes first.

## 7.11 Case Studies: Three Autopsies of Credit-ML Failure

### Case Study A: The One-Month Lead (Bai–Bali–Wen, 2019–2023)

*What happened.* A four-factor model published in the *JFE* in 2019 became a benchmark. During replication, Dickerson, Mueller, and Robotti found that two factor return series were misdated by one month in one direction and a third by one month in the other, and that some extreme losses had been removed; the paper was retracted in 2023, a first for the journal according to Warwick Business School's 10 September 2024 account. Robotti's summary of the corrected factors: they provided "no investment advantage at all."

*How the desk would have caught it.* A purged walk-forward on the *published* factor series cannot catch a misalignment buried inside that series; the leak is upstream of the CV. What catches it is an *implementation audit*: rebuild one factor from raw TRACE with explicit availability timestamps, trade it from month-begin prices, and compare. A one-month lead shows up immediately as a premium that disappears when the return window moves one month later. *Lesson for Theo:* label timestamps are covenants. Read them the way you would read the definition of "Consolidated EBITDA."

### Case Study B: The Honest Corrigendum (Bianchi–Büchner–Tamoni, 2021)

*What happened.* The *RFS* published both the original paper and, in the same volume, a corrigendum with an added coauthor (Hoogteijling) that corrects the analysis for "using information not available when the forecasts were made." Out-of-sample $R^2$ fell; predictability remained significant.

*Why it matters.* This is the gold standard of error handling, and it shows that look-ahead is usually a *pipeline* property (data vintages, revised macro series, forward-filled values), not a modeling choice. Pair it with Bohn and Stein's footnote 31 in §7.7: most leaks are things the researcher did not know they knew. The desk control is a point-in-time feature store in which every value carries the timestamp at which it became available, and ROBO is forbidden to join on anything else.

### Case Study C: How a Bid–Ask Bounce Became a Factor (Short-Term Reversal, 2026)

*What happened.* Measured with month-end prices in both the signal and the return, corporate-bond short-term reversal earned −0.99% per month ($t = -4.46$), one of the strongest results in the zoo. With a month-begin return, it earned −0.09% ($t = -0.51$). The covariance identity in §7.9 explains the whole gap.

*How the desk would have traded it, and why it would have lost.* On an RFQ desk you cannot buy at last month's stale print; the first executable price already reflects the bounce. Ines replayed the hand history: "Every 'loser' we bought in this backtest was a bond whose last print was a small dealer selling to a large one at the bid. We would have paid the offer. The factor was the bid–ask spread, and we would have been on the wrong side of it." Chapter 9 picks up what survives (value and some equity-informed signals), and Chapter 10 rebuilds credit momentum on clean returns.

## 7.12 The Credit ML Lab: A Reference Implementation

### Specification for AI Implementation

**What ROBO built from the vague version.** Theo's first spec said: "Find a strategy with a Sharpe above 2." ROBO ran 12,000 feature combinations overnight and returned the best one: in-sample Sharpe 2.1, deflated Sharpe ratio 0.48. It had done exactly what was asked. The precise spec below asks for something else: every reported result must carry its trial count $N$, the cross-trial Sharpe variance $V$, the deflated Sharpe ratio, the probability of backtest overfitting, and the effective sample size $N_{\text{eff}}$, and the pipeline must refuse to print a Sharpe ratio without them.

**Data schemas (all arrays NumPy `float64` unless stated; day index $t = 0, \ldots, T-1$).**

| Object | Shape / type | Meaning and units |
| :--- | :--- | :--- |
| `xs` | `[T, NB]` | Daily excess return per bond from *marks* (decimal); `xs[0] = 0`; zero after exit |
| `spread`, `dts` | `[T, NB]` | Spread (decimal) and $\text{DTS} = D^{\text{spr}} \cdot s$ (years × decimal) |
| `issuer_of` | `[NB]` int | Ultimate-parent id (not ticker) |
| `exit_day` | `[NB]` int | Day of call, tender, maturity, or exchange; `T + 1` means never |
| `labels` | DataFrame | `bond, issuer, t0, t1` (int days, `t1` inclusive), `label` ∈ {−1, 0, 1}, `ret`, `touch` ∈ {upper, lower, vertical, exit}, `censored` (bool), `u` (uniqueness) |
| `X` | `[n_labels, F]` | Features using information available at `t0` only (point-in-time) |
| `R` | `[T_m, N]` | Returns of *every* trial evaluated, for DSR and PBO |

**Edge cases ROBO must handle, not guess.** Labels whose vertical barrier falls after the last date are not formed (never forward-fill). Single-bond parents have uniqueness from time overlap only. A fold with no positive labels is skipped and reported. Kurtosis with fewer than 30 observations is not estimated; the DSR is reported as unavailable. Bet-size probabilities are clipped to $[10^{-6}, 1 - 10^{-6}]$. FFD warm-up rows are NaN and are dropped, never zero-filled. The embargo is at least the longest feature lookback, including the FFD window.

The six blocks below run in order in one interpreter (NumPy, SciPy, pandas only), are seeded, and end each step with numerical sanity checks. The synthetic panel's parameters are illustrative.

```python
import numpy as np
import pandas as pd
from itertools import combinations
from scipy import special, stats

# ---------- 1. Fractional differentiation with a fixed-width window (Section 7.3) ----------
def ffd_weights(d, tau=1e-4, k_max=100_000):
    """w_0 = 1, w_k = -w_{k-1} (d - k + 1) / k, truncated once |w_k| < tau."""
    w = [1.0]
    for k in range(1, k_max):
        w_k = -w[-1] * (d - k + 1) / k
        if abs(w_k) < tau:
            break
        w.append(w_k)
    return np.array(w)

def frac_diff(x, d, tau=1e-4):
    """x_tilde_t = sum_k w_k x_{t-k}. The first K values are NaN (warm-up), never zero."""
    x = np.asarray(x, dtype=float)
    w = ffd_weights(d, tau)
    K = len(w) - 1
    out = np.full(len(x), np.nan)
    if len(x) > K:
        out[K:] = np.convolve(x, w, mode="valid")
    return out

DF_CRIT_5PCT = -2.86  # approximate Dickey-Fuller 5% critical value (constant, no trend)

def df_tstat(x):
    """t-stat of b in dx_t = a + b x_{t-1} + e_t (no augmentation lags)."""
    x = np.asarray(x, dtype=float)
    x = x[~np.isnan(x)]
    dx, xl = np.diff(x), x[:-1]
    X = np.column_stack([np.ones_like(xl), xl])
    beta, *_ = np.linalg.lstsq(X, dx, rcond=None)
    resid = dx - X @ beta
    s2 = resid @ resid / (len(dx) - 2)
    return beta[1] / np.sqrt(s2 * np.linalg.inv(X.T @ X)[1, 1])

def min_d(x, grid=np.round(np.arange(0.0, 1.0001, 0.05), 2), tau=1e-4):
    """Smallest d whose FFD series rejects a unit root -> (d_star, memory correlation)."""
    x = np.asarray(x, dtype=float)
    for d in grid:
        xd = frac_diff(x, d, tau)
        ok = ~np.isnan(xd)
        if ok.sum() > 100 and df_tstat(xd) < DF_CRIT_5PCT:
            return float(d), float(np.corrcoef(xd[ok], x[ok])[0, 1])
    return 1.0, float("nan")

w = ffd_weights(0.5)
k = np.arange(len(w))
assert np.allclose(w, (-1.0) ** k * special.binom(0.5, k), rtol=0, atol=1e-12)  # recursion = binomial
K = len(w) - 1
assert abs(w.sum() - (-1.0) ** K * special.binom(0.5 - 1, K)) < 1e-9             # partial-sum identity
assert 0 < w.sum() < 0.1                                   # the 'memory sliver' truncation keeps
assert 250 <= len(ffd_weights(0.4, 1e-4)) - 1 <= 320       # ~280-day warm-up at tau = 1e-4
assert 45 <= len(ffd_weights(0.4, 1e-3)) - 1 <= 65         # ~54-day warm-up at tau = 1e-3
rw = np.cumsum(np.random.default_rng(1).normal(0, 0.02, 2000))   # log-spread-like random walk
assert np.allclose(frac_diff(rw, 1.0)[1:], np.diff(rw))          # d = 1 is ordinary differencing
assert df_tstat(frac_diff(rw, 1.0)) < -10 < df_tstat(rw)         # change stationary, level not
print("FFD on a random walk: d* = %.2f, memory retained rho = %.2f" % min_d(rw))
```

```python
# ---------- 2. Synthetic credit panel with smoothed (stale) marks (Section 7.1) ----------
def simulate_panel(n_issuers=120, T=1260, seed=11):
    rng = np.random.default_rng(seed)
    n_bonds = 1 + rng.poisson(2.0, n_issuers)                       # bonds per ultimate parent
    issuer_of = np.repeat(np.arange(n_issuers), n_bonds)
    NB = issuer_of.size
    base = np.exp(rng.uniform(np.log(0.01), np.log(0.08), n_issuers))  # 100-800bp (illustrative)
    D = rng.uniform(2.0, 8.0, NB)                                   # spread duration, years
    theta = rng.uniform(0.2, 1.0, NB)                               # mark adjustment speed; 1 = live
    basis = rng.normal(0.0, 0.05, NB)
    f, a, e = np.zeros(T), np.zeros((T, n_issuers)), np.zeros((T, NB))
    for t in range(1, T):
        f[t] = 0.995 * f[t - 1] + rng.normal(0, 0.010)             # common log-spread factor
        jump = (rng.random(n_issuers) < 0.10 / 252) * 0.5           # LMT/downgrade-style jump
        a[t] = 0.99 * a[t - 1] + rng.normal(0, 0.012, n_issuers) + jump
        e[t] = 0.95 * e[t - 1] + rng.normal(0, 0.010, NB)           # bond-level basis noise
    L_true = np.log(base)[issuer_of] + basis + f[:, None] + a[:, issuer_of] + e
    L_mark = np.empty_like(L_true)
    L_mark[0] = L_true[0]
    for t in range(1, T):                                           # partial adjustment = smoothing
        L_mark[t] = L_mark[t - 1] + theta * (L_true[t] - L_mark[t - 1])
    s_true, s_mark = np.exp(L_true), np.exp(L_mark)

    def excess(s):                                                  # carry minus D * spread change
        xs = np.zeros_like(s)
        xs[1:] = s[:-1] / 252 - D * (s[1:] - s[:-1])
        return xs

    xs_true, xs = excess(s_true), excess(s_mark)
    exit_day = np.full(NB, T + 1)
    leaves = rng.random(NB) < 0.30
    exit_day[leaves] = rng.integers(T // 4, T, leaves.sum())
    tender = rng.random(NB) < 2 / 3                                 # otherwise a distressed exchange
    for b in np.flatnonzero(leaves):
        xs[exit_day[b], b] += 0.02 if tender[b] else -0.15          # illustrative exit returns
        xs[exit_day[b] + 1:, b] = 0.0
    return dict(xs=xs, xs_true=xs_true, spread=s_mark, dts=D * s_mark, issuer_of=issuer_of,
                exit_day=exit_day, theta=theta, T=T, NB=NB, n_issuers=n_issuers)

P = simulate_panel()
stay = np.flatnonzero(P["exit_day"] > P["T"])
b_slow = stay[np.argmin(P["theta"][stay])]
lag1 = lambda x: np.corrcoef(x[1:-1], x[2:])[0, 1]
assert P["xs"][1:, b_slow].std() < 0.8 * P["xs_true"][1:, b_slow].std()   # marks understate vol
assert lag1(P["xs"][:, b_slow]) > lag1(P["xs_true"][:, b_slow]) + 0.2     # and fake autocorrelation
```

```python
# ---------- 3. Triple-barrier labels in DTS space with exit censoring (Section 7.4) ----------
def triple_barrier(xs, dts, issuer_of, exit_day, h=63, step=10, m_up=1.0, m_dn=1.0, sigma_rel_m=0.09):
    T, NB = xs.shape
    C = np.cumsum(xs, axis=0)                          # cumulative excess return through day t
    scale = sigma_rel_m * np.sqrt(h / 21.0)            # monthly relative vol -> horizon (21 d/month)
    cols, frames = np.arange(NB), []
    for t0 in range(0, T - h, step):                   # vertical barrier always inside the sample
        alive = exit_day > t0
        path = C[t0 + 1:t0 + h + 1] - C[t0]            # (h, NB): X(u), u = 1..h
        width = scale * dts[t0]                        # barrier half-width, decimal return
        days = np.arange(t0 + 1, t0 + h + 1)[:, None]
        hits = {"upper": path >= m_up * width, "lower": path <= -m_dn * width,
                "exit": days >= exit_day[None, :]}
        first = {name: np.where(M.any(0), M.argmax(0), h) for name, M in hits.items()}
        k_ev = np.minimum(np.minimum(first["upper"], first["lower"]), first["exit"])
        k_end = np.where(k_ev >= h, h - 1, k_ev)
        touch = np.where(k_ev >= h, "vertical",
                         np.where(first["exit"] == k_ev, "exit",
                                  np.where(first["lower"] == k_ev, "lower", "upper")))
        ret = path[k_end, cols]
        label = np.where(touch == "upper", 1, np.where(touch == "lower", -1, np.sign(ret))).astype(int)
        frames.append(pd.DataFrame({"bond": cols, "issuer": issuer_of, "t0": t0, "t1": t0 + 1 + k_end,
                                    "label": label, "ret": ret, "touch": touch})[alive])
    out = pd.concat(frames, ignore_index=True)
    out["censored"] = out["touch"].eq("exit")
    return out

labels = triple_barrier(P["xs"], P["dts"], P["issuer_of"], P["exit_day"])
assert labels["label"].isin([-1, 0, 1]).all() and (labels["t1"] > labels["t0"]).all()
assert labels.loc[labels.touch == "upper", "ret"].min() > 0 > labels.loc[labels.touch == "lower", "ret"].max()
shares = labels["touch"].value_counts(normalize=True)
assert 0.05 < shares.get("vertical", 0.0) < 0.95 and shares.get("exit", 0.0) > 0
print("touch shares:", shares.round(3).to_dict())
```

```python
# ---------- 4. Parent-level average uniqueness and the hat count (Section 7.6) ----------
def issuer_uniqueness(labels, T):
    u = np.empty(len(labels))
    t0_all, t1_all = labels["t0"].values, labels["t1"].values
    for _, idx in labels.groupby("issuer").indices.items():
        t0, t1 = t0_all[idx], t1_all[idx]
        diff = np.zeros(T + 2)
        np.add.at(diff, t0, 1.0)
        np.add.at(diff, t1 + 1, -1.0)
        conc = np.cumsum(diff)[:T + 1]                 # live labels of this parent on each day
        inv = np.concatenate([[0.0], np.cumsum(1.0 / np.maximum(conc, 1.0))])
        u[idx] = (inv[t1 + 1] - inv[t0]) / (t1 - t0 + 1)
    return u

toy = pd.DataFrame({"issuer": [0, 0, 1], "t0": [0, 0, 0], "t1": [9, 9, 9]})
assert np.allclose(issuer_uniqueness(toy, 20), [0.5, 0.5, 1.0])   # siblings share a hat; others don't
labels["u"] = issuer_uniqueness(labels, P["T"])
n_eff = labels["u"].sum()
assert ((labels["u"] > 0) & (labels["u"] <= 1 + 1e-12)).all() and n_eff < 0.25 * len(labels)
print(f"label rows {len(labels):,}   N_eff {n_eff:,.0f}   ratio {n_eff / len(labels):.3f}")
```

```python
# ---------- 5. Purged, embargoed, parent-grouped CV vs shuffled K-fold (Section 7.7) ----------
def shuffled_kfold(n, k=5, seed=0):
    fold = np.random.default_rng(seed).permutation(n) % k
    for i in range(k):
        yield np.flatnonzero(fold != i), np.flatnonzero(fold == i)

def purged_group_kfold(t0, t1, groups, n_group_folds=5, n_time_blocks=4, embargo=21, seed=0):
    """Test = (parents in group fold g) x (time block m). Train = other parents whose label
    windows neither overlap the test span nor start within `embargo` days after it."""
    t0, t1, groups = np.asarray(t0), np.asarray(t1), np.asarray(groups)
    parents = np.unique(groups)
    gfold = pd.Series(np.random.default_rng(seed).permutation(parents.size) % n_group_folds, index=parents)
    gf = gfold.loc[groups].values
    edges = np.linspace(t0.min(), t0.max() + 1, n_time_blocks + 1)
    for g in range(n_group_folds):
        for m in range(n_time_blocks):
            test = (gf == g) & (t0 >= edges[m]) & (t0 < edges[m + 1])
            if not test.any():
                continue
            T0, T1 = t0[test].min(), t1[test].max()
            leaks = (t0 <= T1 + embargo) & (t1 >= T0)      # purge and embargo in one condition
            yield np.flatnonzero((gf != g) & ~leaks), np.flatnonzero(test)

def knn_scores(Xtr, ytr, Xte, k=10, batch=500):            # a flexible model that can memorize
    sq, out = (Xtr ** 2).sum(1), np.empty(len(Xte))
    for s in range(0, len(Xte), batch):
        xb = Xte[s:s + batch]
        d2 = (xb ** 2).sum(1)[:, None] + sq[None, :] - 2.0 * xb @ Xtr.T
        out[s:s + batch] = ytr[np.argpartition(d2, k, axis=1)[:, :k]].mean(1)
    return out

def auc(y, score):
    r = stats.rankdata(score)
    n1 = y.sum()
    n0 = len(y) - n1
    return (r[y == 1].sum() - n1 * (n1 + 1) / 2) / (n1 * n0)

def cv_auc(X, y, splits, k=10):
    score = np.full(len(y), np.nan)
    for tr, te in splits:
        if len(tr) > k and len(te) > 0:
            score[te] = knn_scores(X[tr], y[tr], X[te], k)
    ok = ~np.isnan(score)
    return auc(y[ok], score[ok])

rng = np.random.default_rng(23)
keep = rng.choice(P["n_issuers"], 25, replace=False)
L = labels[labels["issuer"].isin(keep)].reset_index(drop=True)
F = 4
z_parent = rng.normal(0.0, 1.0, (P["n_issuers"], F))                     # persistent parent traits
drift = np.cumsum(rng.normal(0.0, 0.02, (P["T"], P["NB"], F)), axis=0)   # slowly wandering noise
drift += rng.normal(0.0, 0.3, (1, P["NB"], F))
X = z_parent[L["issuer"].values] + drift[L["t0"].values, L["bond"].values]   # PURE NOISE features
y = (L["label"].values > 0).astype(int)
auc_naive = cv_auc(X, y, shuffled_kfold(len(y)))
auc_purged = cv_auc(X, y, purged_group_kfold(L["t0"], L["t1"], L["issuer"]))
print(f"pure-noise AUC: shuffled K-fold {auc_naive:.3f}   purged + grouped {auc_purged:.3f}")
assert auc_naive > auc_purged + 0.03          # overlapping labels leak through shuffled folds
assert abs(auc_purged - 0.5) < 0.06           # the honest splitter finds nothing, correctly
```

```python
# ---------- 6. Meta-label bet sizing, deflated Sharpe, MinTRL, PBO (Sections 7.5, 7.8) ----------
def bet_size(p, side):
    """Secondary-model probability -> size in [0, 1), times the primary model's side."""
    p = np.clip(p, 1e-6, 1 - 1e-6)
    z = (p - 0.5) / np.sqrt(p * (1 - p))
    return np.maximum(2 * stats.norm.cdf(z) - 1, 0.0) * side

assert abs(bet_size(0.75, 1) - 0.4364) < 1e-3 and abs(bet_size(0.9, -1) + 0.8176) < 1e-3
assert bet_size(0.4, 1) == 0.0                # the meta-model may veto, never reverse

EULER_GAMMA = 0.5772156649015329

def sharpe(R):
    return R.mean(0) / R.std(0, ddof=1)

def psr(sr, T, skew, kurt, sr0=0.0):
    return stats.norm.cdf((sr - sr0) * np.sqrt(T - 1) / np.sqrt(1 - skew * sr + (kurt - 1) / 4 * sr ** 2))

def expected_max_sr(n_trials, var_sr):
    g = EULER_GAMMA
    return np.sqrt(var_sr) * ((1 - g) * stats.norm.ppf(1 - 1 / n_trials)
                              + g * stats.norm.ppf(1 - 1 / (n_trials * np.e)))

def deflated_sharpe(R):
    """R: (T, N) returns of EVERY trial evaluated; reports the best trial, deflated."""
    T, N = R.shape
    srs = sharpe(R)
    b = int(np.argmax(srs))
    sk, ku = stats.skew(R[:, b]), stats.kurtosis(R[:, b], fisher=False)
    sr_star = expected_max_sr(N, srs.var(ddof=1))
    return dict(sr=srs[b], sr_star=sr_star, psr0=psr(srs[b], T, sk, ku), dsr=psr(srs[b], T, sk, ku, sr_star))

def min_trl(sr, sr0, skew, kurt, alpha=0.05):
    return 1 + (1 - skew * sr + (kurt - 1) / 4 * sr ** 2) * (stats.norm.ppf(1 - alpha) / (sr - sr0)) ** 2

def pbo_cscv(R, S=10):
    T, N = R.shape
    blocks = np.array_split(np.arange(T), S)
    logits = []
    for ins in combinations(range(S), S // 2):
        tr = np.concatenate([blocks[i] for i in ins])
        te = np.concatenate([blocks[i] for i in range(S) if i not in ins])
        n_star = np.argmax(sharpe(R[tr]))
        omega = stats.rankdata(sharpe(R[te]))[n_star] / (N + 1)
        logits.append(np.log(omega / (1 - omega)))
    return float(np.mean(np.array(logits) <= 0))

rng = np.random.default_rng(42)
T_m, N_tr = 120, 1000                                         # 10 years of months, 1,000 trials
maxes = [sharpe(rng.normal(0, 0.02, (T_m, N_tr))).max() for _ in range(40)]
assert abs(np.mean(maxes) / expected_max_sr(N_tr, 1 / T_m) - 1) < 0.10    # extreme-value formula holds
noise = rng.normal(0, 0.02, (T_m, N_tr))
rep = deflated_sharpe(noise)
assert rep["psr0"] > 0.95 and rep["dsr"] < 0.95               # 'significant' naively; a coin flip deflated
print({key: round(float(val), 3) for key, val in rep.items()})
pbo_noise = pbo_cscv(noise[:, :200])
skilled = np.column_stack([noise[:, :200], rng.normal(0.012, 0.02, T_m)])   # one real edge, SR 0.6/month
pbo_skill = pbo_cscv(skilled)
assert 0.10 < pbo_noise < 0.90 and pbo_skill < 0.25
print(f"PBO noise {pbo_noise:.2f}   PBO with one real strategy {pbo_skill:.2f}   "
      f"MinTRL(SR 0.3 vs 0.1, skew -0.5, kurt 5) {min_trl(0.3, 0.1, -0.5, 5):.0f} months")
```

What the blocks demonstrate, in desk language. Block 2 shows that smoothed marks cut measured volatility and manufacture autocorrelation, which is Defect 1 in code. Block 4 prints a hat count roughly an order of magnitude below the label count. Block 5 is the chapter's central experiment: with features that are *pure noise by construction*, shuffled K-fold reports an AUC well above 0.5 because each test label's nearest neighbors are its own overlapping siblings in time, while the purged, embargoed, parent-grouped splitter reports about 0.5, which is the truth. Block 6 shows the best of 1,000 noise strategies looking significant at a naive 95% and looking like a coin flip once deflated. Port the same functions to the real panel by replacing `simulate_panel` with the point-in-time TRACE and pricing-composite feed (Appendix B) and keeping every assert as a production test.

## 7.13 Desk Debrief

Two weeks after the cold open, Kaz reran the gradient-boosted model through the lab. The screen was much less exciting, which on this desk is how you know a number has been near the truth.

The row count was unchanged: 212,000 bond-months. Above it, in a font Kaz had made deliberately large, sat the hat count, $N_{\text{eff}} \approx 24{,}000$. Below it: shuffled K-fold AUC 0.61, purged and parent-grouped AUC 0.52; 3,000 trials; an out-of-sample Sharpe ratio of 0.30 per month across the purged folds; deflated Sharpe ratio 0.84; PBO 0.41 *(all illustrative)*. The top decile still held nine issuers. It no longer had a reason to.

"It isn't a strategy," Kaz said. "It isn't nothing, either. It's mostly carry and one company."

"Strip the carry," Theo said, "and then show me the one company." IDO or it didn't happen.

Theo had run something smaller. His primary model was the credit-agreement read turned into flags: drop-down capacity through unrestricted subsidiaries, non-pro-rata uptier risk, and a liquidity runway from the 13-week model shorter than two quarters. That came to about forty flags a year across the high-yield universe. The secondary model, trained on purged, parent-grouped folds, learned only *when those flags were right* and sized them. He had tried four sizing models, and he wrote the number four at the top of the report as if it were a defined term. Out of sample, the result was a Sharpe ratio of 0.20 per month over 96 months, with skew −1.5 and kurtosis 8. Against the four-trial benchmark ($SR^\ast \approx 0.02$), the deflated Sharpe ratio was 0.93, and the minimum track record length was about 115 months, so he needs roughly a year and a half more of live trading before the number means what he wants it to mean *(illustrative)*.

"Now," Ines said, "you're showing me a hand *and* the number of hands you folded. Sit down."

Mags looked at the four. "Back in my day we had one sizing model. It was called the PM's mood, and it had an excellent track record, because the PM was the one who kept it."

At the bottom of the monitor Kaz had taped the epigraph that Dickerson, Robotti, and Rossetti chose for their 2026 audit, Ronald Coase's line: "if you torture the data enough, nature will always confess." By lunch a sticky note had appeared beneath it in the unmistakable register of the Ad Hoc Group: *The data, represented by counsel, will not confess to anything absent a cooperation agreement.* None was signed, so the counter waits for Part IV.

Theo put the USB stick back in his pocket. It had been a 13-week cash flow model when he arrived. It was now a vertical barrier, a primary model, and a reason to distrust anything labeled "adjusted," which Mags said was the first sign he might last.

Tape these to the monitor.

- **Count hats, not rows.** The issuer is the observation: the ultimate parent, not the ticker. Print $N_{\text{eff}} = \sum_i \bar u_i$ next to every result. In Kaz's panel, 212,000 bond-months come to about 24,000 hats. A model that times the whole high-yield market has roughly one observation per non-overlapping 13-week window, which is about 79 in twenty years.
- **A mark is not a price.** Stale and smoothed marks lower measured volatility, manufacture autocorrelation, and inflate the Sharpe ratio *before* any deflation. Treat staleness as a feature and as a filter. It is worst in single-B and CCC bonds, exactly where the alpha is supposed to live.
- **Keep the memory, lose the trend.** Fractionally difference log spreads to the smallest $d$ that passes a unit-root test. Taking $d = 1$ throws away the level information that makes a spread a spread. Warm-up rows are NaN, never zero, and the FFD window counts toward the embargo.
- **Label the trade you would actually make.** Use triple barriers scaled by DTS, set on IDO returns (strip the carry, or the label learns the coupon), with a 13-week vertical barrier. Censor exits at the exit value rather than imputing them from peers. A distressed exchange is not an average outcome, however politely the press release calls it an "open market purchase."
- **The credit agreement picks the side; the model picks the size.** Meta-labeling is what RSSG already did by hand. The secondary model may veto a trade. It may never reverse one.
- **Cross-validate as if the bonds were watching.** Purge overlapping labels, embargo past the longest lookback, and group by ultimate parent. Shuffled K-fold finds signal in pure noise, and block 5 of §7.12 will demonstrate it on demand.
- **Report the folded hands.** Every Sharpe ratio travels with $N$, $V[\widehat{SR}_n]$, the DSR, the PBO, and the MinTRL, and a new factor should clear roughly $t > 3$. ROBO refuses to print a Sharpe ratio without them, and so should you.
- **Timestamps are covenants.** Measure returns from the first feasible price after formation (the gap), filter ex-ante and symmetrically, keep the defaults, and join only on availability time. Between a retraction, a corrigendum, and 26 surviving specifications out of 432, the 2019–2026 record says credit ML is a data-integrity discipline first and a modeling discipline second.

### The Spec You Hand the Robot

Paste the block below into ROBO's prompt. It compresses §7.3–7.12 into one engine. The six Python blocks in §7.12 are the executable reference, and their asserts are the acceptance tests.

```text
ROBO: build credit_ml_lab, a leakage-proof research harness for bond-level ML.
Implement exactly this. Where something is unspecified, stop and ask; do not guess.

INPUTS (point-in-time; every field carries available_at; join on nothing else)
  xs[T,NB]       daily excess return vs duration-matched Treasuries, decimal, from marks
  s[T,NB]        spread, decimal;  D_spr[T,NB] in years;  DTS = D_spr * s
  stale[T,NB]    trading days since the last institutional-size TRACE print
  parent[NB]     ULTIMATE-PARENT id (not ticker; unrestricted subs map to their parent)
  exit_day[NB]   call/tender/maturity/exchange/default day, T+1 if none; exit_type[NB]
  primary[T,NB]  side in {-1, 0, +1} from the analyst/covenant model (Chapter 13 flags)

PIPELINE
  1 FFD features on log s: d* = smallest d on 0.00:0.05:1.00 with DF t < -2.86
    (approximate 5%); tau = 1e-4, or 1e-3 if the warm-up exceeds the embargo budget.
    Warm-up rows are NaN and are dropped.
  2 Labels: triple barrier on IDO returns (carry and factor beta stripped, Chapter 8);
    half-width = m * 0.09 * sqrt(h/21) * DTS[t0], m = 1, h = 63 trading days.
    An exit before t0+h closes the label at the exit value: touch="exit", censored=True.
    Never form a label whose vertical barrier lies past the last date.
  3 Weights: parent-level average uniqueness u in (0,1]; N_eff = sum(u); Kish size;
    weights normalized to sum to n_labels.
  4 CV: purged, embargoed, parent-grouped K-fold x time blocks, plus annual walk-forward.
    embargo >= max(h, longest feature lookback including the FFD window).
    A fold with no positive labels is skipped and reported.
  5 Meta-label: secondary model -> p, clipped to [1e-6, 1-1e-6];
    size = max(2*Phi((p-0.5)/sqrt(p*(1-p))) - 1, 0) * primary.  Veto yes, reversal never.
  6 Evaluation returns start at the first feasible price AFTER signal formation (gap).
    Return filters are ex-ante and symmetric; returns around defaults are kept.

OUTPUT (one JSON record per experiment, appended to an immutable trial log)
  n_trials_raw, n_trials_clustered, var_sr, sr, psr0, dsr, min_trl, pbo (CSCV, S=10),
  n_labels, n_eff, kish, auc_shuffled, auc_purged, share_censored, share_stale_gt5d

REFUSE
  - to print any Sharpe ratio without n_trials, var_sr, dsr, pbo and n_eff beside it
  - to estimate kurtosis or the DSR from fewer than 30 returns (report "unavailable")
  - to delete a trial from the log, ever

ACCEPTANCE TESTS (keep in CI)
  - pure-noise features: auc_shuffled > auc_purged + 0.03 and |auc_purged - 0.5| < 0.06
  - 1,000 noise strategies x 120 months: mean max SR within 10% of the formula;
    the best has psr0 > 0.95 and dsr < 0.95
  - FFD weights equal (-1)^k binom(d, k) to 1e-12; d = 1 reproduces np.diff
  - two sibling bonds on identical windows get u = 0.5 each; a lone bond gets u = 1.0
```

The refusal to delete a trial is the line that matters most. A deflated Sharpe ratio is only as honest as the trial count fed into it, and the cheapest way to raise a DSR is to forget the 2,999 configurations that never made the slide. ROBO does not forget, which is the one respect in which it is a better researcher than any of us.

### Exercises

1. **Count Kaz's hats.** One issuer has 11 bonds. Each bond produces a daily triple-barrier label with $h = 63$ trading days over $T = 1{,}260$ days, and every label runs to its vertical barrier. (a) Show that an interior label has $\bar u_i \approx 1/(11 \times 63)$ and that the issuer contributes $N_{\text{eff}} \approx T/h \approx 20$, whatever the number of bonds. (b) Seven of the 11 bonds are guaranteed OpCo notes. Four are HoldCo notes that were primed last quarter by a drop-down into an unrestricted subsidiary. Do they remain one group for cross-validation? What new label does the drop-down create, and how would you validate a model of it? (c) Compute the Kish effective size of the weights $w = (1, 1, 1, 1, 6)$.
   *Check:* (a) Concurrency is about $11 \times 63 = 693$ in the interior, and roughly $11 \times 1{,}197$ labels divided by 693 gives about 19. (b) They remain one group. The ultimate parent is the information unit, and splitting it lets the model read the OpCo bonds' answers off the HoldCo bonds. The drop-down does create a legitimate *within-parent* target, the OpCo–HoldCo basis, but it can only be validated across time blocks, because there is no other parent to hold out. (c) $(\sum w)^2 / \sum w^2 = 100/40 = 2.5$: five rows, two and a half opinions.

2. **Memory after a closing night.** (a) Compute the first five FFD weights for $d = 0.4$ from $w_k = -w_{k-1}(d-k+1)/k$. (b) Prove that $\sum_{k=0}^{K} w_k = (-1)^K \binom{d-1}{K}$, that this partial sum is strictly positive for every finite $K$ when $d \in (0,1)$, and that it tends to zero as $K \to \infty$. (c) Block 5 of §7.12 uses a 21-day embargo because its features have no lookback. Suppose you add FFD features with $d = 0.4$ and $\tau = 10^{-4}$, whose warm-up is about 280 days (block 1). What embargo does the edge-case rule require, and how much of a 1,260-day sample split into four time blocks does it remove after each test block? What does raising $\tau$ to $10^{-3}$ buy, and what does it cost?
   *Check:* (a) $(1, -0.4, -0.12, -0.064, -0.0416)$. (b) Since $w_k = (-1)^k \binom{d}{k}$, Pascal's rule $\binom{d}{k} = \binom{d-1}{k} + \binom{d-1}{k-1}$ makes the alternating sum telescope to $(-1)^K \binom{d-1}{K} = \prod_{j=1}^{K} (j-d)/j$. Every factor is positive for $d \in (0,1)$, and the product behaves like $K^{-d}/\Gamma(1-d) \to 0$. (c) The embargo must be at least 280 days. That is close to 90% of a 315-day block, and more than a fifth of the sample, removed after every test block. At $\tau = 10^{-3}$ the window falls to about 54 days, and the horizon $h = 63$ sets the embargo again. The cost is a larger leftover weight sum, so the filtered series carries more of the trending level, and the smallest $d$ that passes the unit-root test usually rises. You pay for the extra training data in memory.

3. **Size Theo's hand.** Theo's primary model raises 40 flags a year with a precision of 35%. A winning flag earns +4% and a losing one −2% in IDO return, at unit size *(illustrative)*. The meta-model keeps 60% of the winners and lifts precision to 55%. (a) Compute the expected IDO return per trade, and per year summed over trades at unit size, with and without the meta-model. (b) Compute the bet size for $p = 0.75$ and for $p = 0.55$. In Ines's terms, explain why a 55% read earns a small position rather than a slightly-better-than-half one. (c) The meta-model's training set contains every flag Theo has ever raised, including flags on issuers that later did a drop-down. Which splitter must you use, and what goes wrong with the obvious one?
   *Check:* (a) Without it: $0.35 \times 4 - 0.65 \times 2 = +0.10\%$ per trade, or $+4\%$ a year. With it: 8.4 winners at 55% precision means about 15.3 trades, and $0.55 \times 4 - 0.45 \times 2 = +1.30\%$ per trade, or about $+20\%$ a year from fewer than half the trades. (b) For $p = 0.75$, $z = 0.25/\sqrt{0.1875} \approx 0.577$ and $2\Phi(z) - 1 \approx 0.44$. For $p = 0.55$, $z = 0.05/\sqrt{0.2475} \approx 0.10$, giving about 0.08. The sizing rule converts the edge into a test statistic and bets the confidence that the edge exists. A 55% read is barely distinguishable from a coin flip, so it gets a chip, not a stack: bet your confidence, not your opinion. (c) Use purged, parent-grouped folds. Flags on one parent cluster in time around the same corporate event, so a shuffled split trains on the answer to the test flag.

4. **Deflate the honest number.** Section 7.8 deflated Kaz's in-sample winner. Now deflate the number on his new report: a purged out-of-sample Sharpe ratio of 0.30 per month over $T = 240$ months, with skew $-0.5$ and kurtosis 5, selected from $N = 3{,}000$ trials with $V \approx 1/T$. (a) Show that the DSR is about 0.84. (b) Clustering the trial-return correlations finds about 400 effectively distinct trials. Holding $V$ fixed, recompute $SR^\ast$ and the DSR. (c) Compute the MinTRL at 95% confidence against the clustered $SR^\ast$, and compare it with the history TRACE has. (d) Explain why feeding the *in-sample* Sharpe ratio of 2.9 into the DSR is a category error.
   *Check:* (a) $SR^\ast \approx 0.23$, the denominator is $\sqrt{1 + 0.15 + 0.09} \approx 1.11$, and $\Phi(0.07 \times 15.46 / 1.11) = \Phi(0.98) \approx 0.84$. (b) $\Phi^{-1}(1 - 1/400) \approx 2.81$ and $\Phi^{-1}(1 - 1/(400e)) \approx 3.12$, so $SR^\ast \approx 0.065 \times (0.423 \times 2.81 + 0.577 \times 3.12) \approx 0.065 \times 2.99 \approx 0.19$, and the DSR is $\Phi(0.11 \times 15.46 / 1.11) = \Phi(1.5) \approx 0.93$. It is better, and still short of 95%. (c) $T^\ast = 1 + 1.24 \times (1.645/0.11)^2 \approx 280$ months, roughly 23 years. That is about the entire life of TRACE (dissemination began in July 2002), and more than three years longer than Kaz's sample. (d) The DSR corrects for selection *across* trials. An in-sample Sharpe ratio also contains overfitting *within* the trial (the trees memorized the 47 hats), so each trial's return series must already be out of sample before it is deflated. Deflating an in-sample number is like haircutting a pro forma EBITDA that already includes the synergies.

5. **The composite is not a clean gap.** In §7.9 the gap return used a month-begin price whose noise $\delta'_{t^+}$ was uncorrelated with the month-end noise $\delta_t$. Suppose instead that the month-begin price is an AI composite anchored partly on the last print, so that $\operatorname{Corr}(\delta'_{t^+}, \delta_t) = \rho > 0$, with standard deviations $\sigma_{\delta'}$ and $\sigma_\delta$. (a) Show that $\operatorname{Cov}(\tilde r_t, \tilde r^{\text{gap}}_{t+1}) = \operatorname{Cov}(r_t, r_{t^+ \to t+1}) - \rho\,\sigma_\delta \sigma_{\delta'}$. (b) The SMU Cox study found that the composite tracked efficient prices well in March 2020 but converged slowly during fire sales. What does that imply about $\rho$ in exactly the months when a reversal strategy is most active, and what would you use as the entry price instead?
   *Check:* (a) The only noise shared by the two returns is $+\delta_t$ in $\tilde r_t$ against $-\delta'_{t^+}$ in the gap return, so the bias is $-\operatorname{Cov}(\delta_t, \delta'_{t^+}) = -\rho\,\sigma_\delta\sigma_{\delta'}$. At $\rho = 0$ it vanishes. At $\rho = 1$ with equal variances it is the full Roll bias of §7.9 again. (b) Slow convergence means the composite inherits the stale print, so $\rho$ rises precisely when dispersion and measured reversal premia are largest. Use the first executable institutional-size trade (or a dealer level you could actually have hit) as the entry price, and report the premium under both definitions.

6. **ROBO and the future.** Theo's first draft of the leakage rule read: "Make sure the model doesn't use future data." ROBO complied by deleting the label column, which was the only future data in the table. Write the precise rule in at most 120 words. Name the timestamp field, the join rule, the purge condition, the embargo, and one test that fails the build if anyone breaks the rule.
   *Check:* A good answer names `available_at` and requires an as-of join (`available_at <= t0`) for every feature. It states the purge as "drop training label $j$ if $[t_{0,j}, t_{1,j}]$ intersects $[T_0, T_1 + \text{embargo}]$," with the embargo at least $\max(h, \text{longest lookback})$. It ships the pure-noise AUC test from block 5 as the guard. Bonus credit for forbidding forward-fill across a data-release date, which is one common way the kind of error behind the 2021 corrigendum gets into a pipeline.

### Deep-Dive Resource Graph

**Podcasts**

- *Flirting with Models* (Corey Hoffstein), Season 7, Episode 32: Ben Wellington, "Complex Feature Engineering at Two Sigma." Feature construction as a discipline, which is the step before §7.3–7.4.
- *Flirting with Models*, Season 7, Episode 33: Stacie Mintz, "Turning Qualitative Fundamentals into Quantitative Factors." The closest podcast treatment of the primary-model idea in §7.5: analyst judgment turned into a signal a model can size.
- *Bloomberg Odd Lots*. No episode on bond-level machine learning was verified for this edition. Search the archive for its credit market-structure episodes (companions to Part V) rather than relying on a citation here.

**Practitioner Writing**

- Robeco (Messow, Houweling, and 't Hoen), "The next frontier in value investing in credits: integrating machine learning" (23 June 2023): https://robeco.com/en-us/insights/2023/06/the-next-frontier-in-value-investing-in-credits-integrating-machine-learning
- Robeco, "How machine learning enhances value investing in credits" (April 2024): https://robeco.com/en-ch/insights/2024/04/how-machine-learning-enhances-value-investing-in-credits
- AQR, working-paper page for Dick-Nielsen, Feldhütter, Pedersen, and Stolborg, "Corporate Bond Factors: Replication Failures and a New Framework": https://www.aqr.com/Insights/Research/Working-Paper/Corporate-Bond-Factors-Replication-Failures-and-a-New-Framework ; Quantpedia's summary: https://quantpedia.com/corporate-bond-factors-replication-failures-and-a-new-framework/
- *Systematically Biased* (Substack), "Pockets of Replicability (Post #6)" (2 June 2026), a narrative of the Bai–Bali–Wen misalignment: https://systematicallybiased.substack.com/p/pockets-of-replicability-post-6
- Warwick Business School, news item on the Fama-DFA Prize awarded to Dickerson, Mueller, and Robotti (9 September 2024): https://www.wbs.ac.uk/news/research-bond-market-wins-fama-dfa-prize/
- SMU Cox, *Cox Today*, on Venkataraman, Jacobsen, and Xu's study of AI-driven bond pricing (7 March 2026): https://www.smu.edu/cox/coxtoday-magazine/2026-03-07-ai-driven-technique-bond-prices ; FI Desk on MarketAxess CP+: https://www.fi-desk.com/marketaxess-bringing-transparency-to-the-muni-marketplace-with-ai-powered-pricing/
- On the shelf: Ben Dor, Dynkin, Hyman, and Phelps, *Quantitative Credit Portfolio Management* (pp. 39, 50, 204, 338); Dynkin and coauthors, *Systematic Investing in Credit* (pp. 611, 651); Bohn and Stein, *Active Credit Portfolio Management in Practice* (pp. 465–467); Paleologo, *Advanced Portfolio Management* (pp. 49, 159); BlackRock, *Systematic High Yield Credit* (p. 6); Blackstone, *Systematic Credit* (p. 2); Man Group's 2022 and 2023 quant-credit papers (Man 2022 pp. 3, 41).

**Academic Papers**

*The overfitting canon.*

- López de Prado (2018), *Advances in Financial Machine Learning* (Wiley): chapters 3–5 (labeling, sample weights, fractional differentiation) and chapter 7 (purged cross-validation).
- Hosking (1981), "Fractional differencing," *Biometrika* 68(1): 165–176, DOI 10.1093/biomet/68.1.165.
- Bailey and López de Prado (2014), "The Deflated Sharpe Ratio," *Journal of Portfolio Management* 40(5): 94–107: https://papers.ssrn.com/abstract=2460551
- Bailey, Borwein, López de Prado, and Zhu (2017), "The Probability of Backtest Overfitting," *Journal of Computational Finance* 20(4), DOI 10.21314/jcf.2016.322: https://papers.ssrn.com/abstract=2326253
- Bailey and López de Prado (2021), "The False Strategy Theorem," *American Mathematical Monthly* 128(9): https://escholarship.org/content/qt95t7k79q/qt95t7k79q.pdf
- Harvey, Liu, and Zhu (2016), "... and the Cross-Section of Expected Returns," *Review of Financial Studies* 29(1): 5–68, DOI 10.1093/rfs/hhv059: https://www.nber.org/papers/w20592
- Chordia, Goyal, and Saretto (2020), "Anomalies and False Rejections," *Review of Financial Studies* 33(5): 2134–2179, DOI 10.1093/rfs/hhaa018.
- Jensen, Kelly, and Pedersen (2023), "Is There a Replication Crisis in Finance?" *Journal of Finance* 78(5): 2465–2518, DOI 10.1111/jofi.13249: https://www.nber.org/papers/w28432 (the optimistic counterweight, for equities).
- Title only: Harvey and Liu (2015), "Backtesting," *Journal of Portfolio Management* 42(1); López de Prado (2019), "A Data Science Solution to the Multiple-Testing Crisis in Financial Research," *Journal of Financial Data Science*; Joubert (2022), "Meta-Labeling: Theory and Framework," *Journal of Financial Data Science*; Roll (1984), "A Simple Implicit Measure of the Effective Bid-Ask Spread in an Efficient Market," *Journal of Finance*.

*The bond-factor audit.*

- Bai, Bali, and Wen (2019), "Common risk factors in the cross-section of corporate bond returns," *Journal of Financial Economics* 131(3): 619–642: https://ideas.repec.org/a/eee/jfinec/v131y2019i3p619-642.html ; retraction notice, *Journal of Financial Economics* 150(3), DOI 10.1016/j.jfineco.2023.103721.
- Dickerson, Mueller, and Robotti (2023), "Priced risk in corporate bonds," *Journal of Financial Economics* 150(2), 103707; arXiv posting: https://arxiv.org/abs/2604.05699
- Dick-Nielsen, Feldhütter, Pedersen, and Stolborg (2023, revised 2025), "Corporate Bond Factors: Replication Failures and a New Framework," SSRN 4586652.
- Dickerson, Robotti, and Rossetti (2026), "The Corporate Bond Factor Replication Crisis," arXiv:2604.07880: https://arxiv.org/abs/2604.07880
- Title only: Dick-Nielsen (2009), "Liquidity Biases in TRACE"; Dick-Nielsen (2014), "How to Clean Enhanced TRACE Data."

*Machine learning for bonds.*

- Bianchi, Büchner, and Tamoni (2021), "Bond Risk Premiums with Machine Learning," *Review of Financial Studies* 34(2): 1046–1089, DOI 10.1093/rfs/hhaa062, and the corrigendum with Hoogteijling, *Review of Financial Studies* 34: 1090–1103, DOI 10.1093/rfs/hhaa098.
- Gu, Kelly, and Xiu (2020), "Empirical Asset Pricing via Machine Learning," *Review of Financial Studies* 33(5).
- Bali, Goyal, Huang, Jiang, and Wen (2020), "Predicting Corporate Bond Returns: Merton Meets Machine Learning," Swiss Finance Institute Working Paper 20-110, SSRN 3686164.
- Kelly, Palhares, and Pruitt (2023), "Modeling Corporate Bond Returns," *Journal of Finance* 78(4): 1967–2008, DOI 10.1111/jofi.13233.
- Feng, He, Wang, and Wu (2025), "Predicting individual corporate bond returns," *Journal of Banking & Finance* 171, 107372.
- Bell, Kakhbod, Lettau, and Nazemi (2026), "Glass Box Machine Learning and Corporate Bond Returns," *Journal of Financial Economics* 181, DOI 10.1016/j.jfineco.2026.104294: https://www.nber.org/papers/w33320
- Jostova, Nikolova, Philipov, and Stahel (2013), "Momentum in Corporate Bond Returns," *Review of Financial Studies* 26(7).
- Barter, Gao, Christodoulaki, Chen, and Cartlidge (2025), the BondBERT paper, arXiv:2511.01869: https://arxiv.org/abs/2511.01869v2
- Title only: Kelly, Malamud, and Zhou (2024), "The Virtue of Complexity in Return Prediction," *Journal of Finance*, read with Nagel (2025), "Seemingly Virtuous Complexity," as the critique; van Binsbergen, Nozawa, and Schwert, "Duration-Based Valuation of Corporate Bonds," *Review of Financial Studies*.

**Data & Code**

- Open Bond Asset Pricing (Dickerson and coauthors): daily and monthly TRACE panels, the 108-signal zoo, and corrected Bai–Bali–Wen factors: https://openbondassetpricing.com/ . The companion Python package, PyBondLab, is distributed on PyPI (search by name; its page was not verified for this edition).
- Dickerson–Mueller–Robotti replication package, Mendeley Data, DOI 10.17632/n66rp59tr7.2: https://data.mendeley.com/datasets/n66rp59tr7
- FINRA, TRACE historic data file layout, including the `As Of Indicator` reversal flag that fooled Kaz in §7.9: https://www.finra.org/filing-reporting/trace/historic-data-file-layout-post-2612-files
- FRED, ICE BofA option-adjusted spreads for US high yield, US corporates, and CCC and lower: https://fred.stlouisfed.org/series/BAMLH0A0HYM2 , https://fred.stlouisfed.org/series/BAMLC0A0CM , https://fred.stlouisfed.org/series/BAMLH0A3HYC
- SIFMA, US corporate bond statistics (volume, issuance, amount outstanding): https://www.sifma.org/resources/research/statistics/us-corporate-bonds-statistics/
- Open Source Asset Pricing (Chen and Zimmermann): the equity-side model for a public, reproducible signal zoo (title only).
- This book: Appendix B for point-in-time TRACE and pricing-composite feeds, and the reference implementation in §7.12.

<!-- STATUS: COMPLETE -->
