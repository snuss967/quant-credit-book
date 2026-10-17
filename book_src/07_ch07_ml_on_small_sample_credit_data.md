# Chapter 7: Machine Learning on Small-Sample, Non-Stationary Credit Data

<!-- WRITER PLAN (sections appended in order as drafted; resume after the last complete "## 7.x" section):
7.0 Cold open; 7.1 Worst ML dataset; 7.2 Trend Watch replication crisis; 7.3 Fractional differentiation;
7.4 Triple barrier in DTS space; 7.5 Meta-labeling; 7.6 Uniqueness weights; 7.7 Purged/embargoed/grouped CV;
7.8 Deflated Sharpe & PBO; 7.9 LIB & LAB; 7.10 Trend Watch ML frontier; 7.11 Case studies;
7.12 Specification for AI Implementation (cumulative python); 7.13 Desk Debrief, Spec You Hand the Robot, Exercises;
Deep-Dive Resource Graph. -->

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
> - **2023.** Dickerson, Mueller, and Robotti, "Priced risk in corporate bonds," *JFE* 150(2), 103707: previously proposed bond factors add essentially nothing beyond the bond market factor. While replicating, they find data errors in the 2019 factors, and the 2019 paper is retracted (retraction notice, *JFE* 150(3)). Warwick Business School's account (9 September 2024) says two factors had a one-month "lead error," a third a "lag error," and some extreme losses had been removed; it calls the retraction "the only time" the journal has ever done so. Mueller and Robotti receive the Fama-DFA Prize.
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

