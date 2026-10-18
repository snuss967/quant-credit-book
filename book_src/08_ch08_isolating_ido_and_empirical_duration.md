# Chapter 8: Stripping Beta to Isolate Pure IDO


## 8.0 Cold Open: Thirty-Seven Cents

At 2:58 p.m. on the Friday before a lender call, Theo's screen showed two numbers that refused to agree. He was long \$40mm of a B3 first-lien secured bond at +620. The 10-year had sold off 18 bp since lunch. The bond was down thirty-seven cents.

"Analytical duration 4.1," Kaz said, without looking up. "You're long \$16,400 of DV01. ROBO is sizing the hedge now. Two hundred thirty-two TY contracts, short."

"The bond only lost thirty-seven cents," Theo said. "Your duration says it should have lost seventy."

"Then it outperformed. That's alpha." Kaz kept typing. "Congratulations."

Ines rolled her chair over, holding a coffee she had clearly been nursing since the open. "What's the pot? If rates are selling off because the data says growth is fine, this bond tightens. Short two hundred thirty-two futures against it and your Treasury hedge isn't a hedge. It's a second position, with worse liquidity than the first one had at 9 a.m."

"So I hedge less?"

"So you find out how much this bond actually cares about rates before you sell something to protect yourself from them."

From across the aisle, without turning around, Mags said: "In 1994 we hedged B paper by buying the long bond. Flight to quality, they told us. Lost on both. By phone."

Theo opened his old 13-week cash flow model, the one on the USB stick, the way other people touch a lucky coin. "This thing has a duration of thirteen weeks and an empirical duration of zero. Nothing in it has ever moved with Treasuries."

Kaz lit up. "So it's a CCC bond."

Nobody laughed, mostly because it was correct.

Theo wrote the question on a sticky note and put it on his monitor: *Of the thirty-seven cents this bond moved today, how much was the bond?*

By the end of this chapter you will be able to decompose a corporate bond's return into carry, rates, spread beta, convexity, and residual, with every sign correct; estimate spread-dependent empirical durations by rating and recognize when the estimate is about to betray you; de-stale a beta estimated on bonds that trade twice a week; build, diagnose, and regularize a hedge matrix across CDX HY, Treasury futures, HYG/JNK, and equity puts; and define IDO precisely enough that a coding agent computes the same number you would.

## 8.1 The Subtraction: Return Decomposition With the Right Signs

Every restructuring banker has built a sources-and-uses table, and every one of them knows the rule: if the columns do not foot, somebody is about to be embarrassed in front of a client. A bond's daily return is a sources-and-uses table for performance. The uses side is one number, the realized total return. The sources side is a list of things you did not choose (Treasury carry, the curve, the rate move, the market's spread move, convexity) and one thing you did: the idiosyncratic residual you were paid to find. The desk calls that residual IDO, and the desk motto, "IDO or it didn't happen," is a statement about accounting before it is a statement about skill. Until the sources foot, you do not know whether you made money or the Federal Reserve made it for you.

The P&L explain that the risk system emails out every evening is this table. Nobody reads it, which is why this section exists.

### Deriving the decomposition

Write the bond's price as a function of its yield and time, $P(y,t)$, and split the yield into a Treasury part and a spread part, $y = y^{\text{TSY}} + s$. For a callable bond read $y$ as the option-adjusted yield and $s$ as the OAS. Over a short interval $\Delta t$ in which the issuer does not default, a second-order Taylor expansion gives

$$
\frac{\Delta P}{P} \approx \frac{1}{P}\frac{\partial P}{\partial t}\,\Delta t + \frac{1}{P}\frac{\partial P}{\partial y}\,\Delta y + \frac{1}{2}\,\frac{1}{P}\frac{\partial^2 P}{\partial y^2}\,(\Delta y)^2 .
$$

Define modified duration $D^{\text{mod}} = -\frac{1}{P}\frac{\partial P}{\partial y}$ and convexity $C = \frac{1}{P}\frac{\partial^2 P}{\partial y^2}$. Add the coupon accrual to the price change to get total return. At an unchanged yield, price pull plus coupon accrual earns the yield, so the time terms collapse to yield carry $y\,\Delta t$ plus a roll-down term when the curve is sloped. Now split $\Delta y = \Delta y^{\text{TSY}} + \Delta s$ and allow the spread sensitivity to differ from the rate sensitivity. For a fixed-rate bullet they are equal; for a floater, a callable, or a bond trading to a call date they are not. The result is

$$
R^{\text{tot}} \approx \underbrace{y\,\Delta t}_{\text{carry}} + \underbrace{\text{roll}}_{\text{curve}} \;-\; D^{\text{mod}}\,\Delta y^{\text{TSY}} \;-\; D^{\text{spr}}\,\Delta s \;+\; \tfrac{1}{2}\,C\,(\Delta y)^2 \;+\; \epsilon .
$$

Every symbol carries units. $R^{\text{tot}}$ is a decimal return. $y$ and $s$ are decimal annual rates. $\Delta t$ is in years under the bond's day count (30/360 for US corporates). $D^{\text{mod}}$ and $D^{\text{spr}}$ are in years. $\Delta y^{\text{TSY}}$ and $\Delta s$ are decimal changes, so an 18 bp sell-off is $0.0018$, not $18$. The residual $\epsilon$ collects the Taylor remainder, pricing noise, and anything specific to the issuer.

The index convention isolates the credit part by subtracting a portfolio of par Treasuries whose key-rate durations match the bond's. To the same order, that portfolio returns $y^{\text{TSY}}\Delta t + \text{roll} - D^{\text{mod}}\Delta y^{\text{TSY}} + \tfrac12 C^{\text{TSY}}(\Delta y^{\text{TSY}})^2$. Subtracting it leaves the excess return:

$$
R^{\text{xs}} \equiv R^{\text{tot}} - \sum_k w_k R^{\text{TSY}}_k \approx s\,\Delta t \;-\; D^{\text{spr}}\,\Delta s \;+\; (\text{convexity cross-terms}) \;+\; \epsilon .
$$

The carry is now OAS carry, $s\,\Delta t$, not yield carry. The rate term is gone by construction, and that is exactly what the index excess return is designed to do. Finally, rewrite the spread term in relative-change form, because (as §8.4 shows) relative spread changes are the quantity that is stable across credits:

$$
-D^{\text{spr}}\,\Delta s \;=\; -\,\underbrace{D^{\text{spr}}\,s}_{\text{DTS}}\,\cdot\,\frac{\Delta s}{s} .
$$

That is the whole chapter in one line. The accounting identity hands you $\Delta s$, the bond's own spread change. It does not tell you how much of $\Delta s$ was the market. Stage two of the subtraction is the factor model

$$
R^{\text{xs}}_{i,t} = \sum_{k} \beta_{i,k}\,F_{k,t} + \epsilon_{i,t},
$$

with factor returns $F_{k,t}$, loadings $\beta_{i,k}$, and residual $\epsilon_{i,t}$. IDO is what survives *both* stages. The decomposition residual is a bookkeeping error term; the factor residual is the asset.

*Assumptions and measure.* The expansion assumes small moves, no default inside $\Delta t$, and option-adjusted durations for callables. The decomposition is accounting and needs no probability measure. Two things built on it do. The *expected* excess return is a $\mathbb{P}$ object, because it is what you forecast. The OAS is a $\mathbb{Q}$-consistent spread, because it is what discounts the bond's cash flows to its price. OAS includes compensation for expected default loss, so "the bond yields +620 over Treasuries" is not "the bond is expected to beat Treasuries by 620 bp a year." The gap is the expected loss, and Chapter 5 priced it.

### The thirty-seven cents, itemized

Apply the decomposition to Theo's bond *(illustrative inputs)*: price \$95, $D^{\text{mod}} = 4.1$, $D^{\text{spr}} = 4.0$, yield 11.1%, one day of 30/360 carry. The 10-year sold off $\Delta y^{\text{TSY}} = +0.0018$, and the bond's OAS tightened 9 bp, $\Delta s = -0.0009$.

| Source | Formula | Return | Cents on \$95 |
| :--- | :--- | ---: | ---: |
| Carry | $y\,\Delta t = 0.111/360$ | +0.031% | +3 |
| Rates | $-D^{\text{mod}}\Delta y^{\text{TSY}} = -4.1 \times 0.0018$ | −0.738% | −70 |
| Spread | $-D^{\text{spr}}\Delta s = -4.0 \times (-0.0009)$ | +0.360% | +34 |
| Convexity | $\tfrac12 C (\Delta y)^2$, $C \approx 20$ | +0.000% | 0 |
| Residual | plug | −0.043% | −4 |
| **Total** | | **−0.390%** | **−37** |

Kaz's "alpha" was the 34 cents of spread tightening. The question for the next three sections is whether those 9 bp of tightening belonged to the bond or to the rate move. If high-yield spreads systematically tighten when yields rise for growth reasons, the 34 cents is beta wearing a disguise, and a hedge of 232 futures would have converted a modestly hedged position into a short rates bet with a spread rider.

> **[SOURCE EXTRACTION]** *Ben_Dor p.298:* "Barclays Capital reports excess returns that equal the difference in total return between a bond and a portfolio of hypothetical par Treasury bonds matching the bond's key rate duration exposures."
>
> **Annotation.** This sentence is the industry's definition of the first subtraction, and it carries two hidden choices. First, the hedge is *key-rate* matched, not single-duration matched, so a 30-year bond's excess return is not polluted by 2s10s steepening. Second, the hedge portfolio is *hypothetical*: par Treasuries at each key rate, rebalanced costlessly. A desk that hedges with actual futures earns the index's excess return minus the futures-cash basis, roll costs, and the cheapest-to-deliver switch (§8.6). On a 2026 desk the definition matters for a second reason: the excess-return series you download from an index provider is already a hedged P&L under a hedge you did not choose. Any empirical duration you estimate on *excess* returns is a duration *relative to that hedge*. Estimate $D^{\text{emp}}$ on total returns, then subtract.

> **[SOURCE EXTRACTION]** *Man_2022 p.14:* "ICE BofAML excess returns taken as total returns less key rate duration matched sovereign return."
>
> **Annotation.** Two index families, one convention. That is convenient and slightly dangerous, because it lets people forget that "excess return" is a model output. Asvanunt and Richardson (2017), *The Credit Risk Premium*, make the point that the measured credit premium is biased if the term component is mis-hedged; the definition you choose leaks into every Sharpe ratio built on it. For a systematic desk the operational rule is to store total returns, Treasury key-rate returns, and the hedge weights separately, and to compute excess returns in your own code. Then, when the index provider restates history, your backtest does not silently change its mind.

> **Ways This Blows Up.** (1) *The sign.* $-D\,\Delta y$ has a minus sign. ROBO, given the formula without it, will report that a rate sell-off made the book money, and the P&L explain will foot perfectly because the residual absorbs twice the error. (2) *Units.* $D \cdot \Delta y$ needs $\Delta y$ in decimal. Feed it 18 instead of 0.0018 and a 4-year bond loses 7,200% on a quiet afternoon. Assert $|\Delta y| < 0.05$ per day as a data-error trap. (3) *Yield carry versus OAS carry.* Yield carry belongs to total return and OAS carry to excess return. Mixing them double-counts the Treasury leg, roughly 5% a year in 2026, and hands you a mysterious, very stable "alpha." (4) *Callable HY.* Much of a high-yield index is callable, and a bond priced to a call date has a spread duration set by the call, not the maturity. Some of what looks like OAS carry is the short call decaying. When the bond crosses the call price, duration-to-worst jumps. Any rolling regression that treats that jump as a rate response will invent a structural break.

## 8.2 Empirical vs. Analytical Duration: One Formula, Three Regimes

Analytical duration answers a question nobody asked: what happens to the bond's price if Treasury yields move *and nothing else does*. On a desk, nothing else moving is the one scenario that never occurs. Empirical duration answers the question Ines asked: when yields move, what tends to happen to this bond, given that its spread tends to move too?

The RSSG reader already knows the limit case. A name in restructuring trades on dollar price, and every bond at the same seniority converges to the same recovery regardless of maturity. Its sensitivity to the 10-year is roughly zero. Empirical duration is the continuum between that limit and par.

### The two-factor derivation

Start from the excess-return identity of §8.1, put the Treasury leg back, and keep only first-order terms. Let $x_i \equiv \Delta s_i / s_i$ be bond $i$'s relative spread change. Then

$$
R_i \approx -D_i\,\Delta y - D_i\,s_i\,x_i ,
$$

where $\Delta y$ is the Treasury yield change and, for a bullet bond, $D_i = D^{\text{mod}}_i = D^{\text{spr}}_i$. Decompose the relative spread change into the part linearly predictable from the yield change and a part orthogonal to it:

$$
x_i = \rho_{y,s}\,\frac{\sigma_s}{\sigma_y}\,\Delta y + u_i, \qquad \mathrm{Cov}^{\mathbb{P}}(u_i,\Delta y) = 0 .
$$

Here $\rho_{y,s}$ is the correlation between yield changes and relative spread changes, $\sigma_s$ the volatility of relative spread changes, and $\sigma_y$ the volatility of yield changes, all measured over the same horizon. The coefficient $\rho_{y,s}\sigma_s/\sigma_y$ is the population OLS slope of $x$ on $\Delta y$. Substituting and taking the conditional expectation under $\mathbb{P}$:

$$
\mathbb{E}^{\mathbb{P}}[R_i \mid \Delta y] = -D_i\,\Delta y\left(1 + s_i\,\rho_{y,s}\,\frac{\sigma_s}{\sigma_y}\right).
$$

Empirical duration is the negative of the slope of this expectation in $\Delta y$:

$$
D^{\text{emp}}_i = D_i\left(1 + s_i\,\rho_{y,s}\,\frac{\sigma_s}{\sigma_y}\right), \qquad H_i \equiv \frac{D^{\text{emp}}_i}{D_i} = 1 + s_i\,\rho_{y,s}\,\frac{\sigma_s}{\sigma_y} .
$$

$H_i$ is the *hedge ratio*: the fraction of analytical duration you should actually hedge to minimize the variance of a Treasury-hedged position. (We write $H$ rather than $h$ because $h$ is reserved for the hedge-weight vector in §8.6.) Three properties follow by inspection. Because $s_i$, $\sigma_s$, and $\sigma_y$ are non-negative, the sign of $\rho_{y,s}$ alone decides whether $H$ is below or above one. The deviation from one scales with the spread level, so the same correlation that shaves 5% off an IG bond's duration can erase a B bond's. And nothing stops $H$ from going negative.

Define the *linkage factor* $\ell \equiv \rho_{y,s}\sigma_s/\sigma_y$, so $H = 1 + \ell s$. Ben Dor's 1998–2009 sample has $\sigma_y = 6.4$ bp a day and relative spread volatilities of 1.6% to 2.5% a day. For B-rated bonds, $\rho = -0.56$ and $\sigma_s \approx 2.2\%$ give $\ell \approx -0.56 \times 0.022/0.00064 \approx -19$ per unit of decimal spread. That is a loss of 0.19 of hedge ratio for every 100 bp of spread, so a B bond at 500 bp has $H \approx 0.03$, and Theo's bond at 620 bp comes out slightly below zero. Under the 1998–2009 parameters, every one of Kaz's 232 contracts was a second position. Under the 2026 parameters in the Trend Watch below, most of them were a hedge. That is the problem.

*The estimable form.* Theory gives the shape; data must give the numbers. With a panel of bond returns, regress

$$
R_{i,t} = \beta\,(-D_{i,t}\,\Delta y_t) + \gamma\,(-D_{i,t}\,s_{i,t}\,\Delta y_t) + \epsilon_{i,t},
\qquad H(s) = \beta + \gamma\,s ,
$$

with $\gamma < 0$ expected. The first regressor is the analytical rate exposure; the second is that exposure scaled by spread. If the two-factor model were exact, $\beta = 1$ and $\gamma = \ell$. In data, $\beta < 1$ for HY even at low spreads, which is the puzzle of §8.3.

*Assumptions and failure modes.* (i) Horizon: daily, weekly, and monthly $\rho$ differ, and daily HY marks are stale (§8.5); Dynkin p.436 runs the pooled regression on monthly, carry-adjusted returns for exactly this reason. (ii) Extrapolation: $H(s)$ is linear in $s$ inside the sample and nowhere else. Ben Dor p.196 tests 2005–2009 spreads that lay outside the fitting range. (iii) The min-variance hedge also hedges your spread view (see the Poker Table below). (iv) In distress, price is pinned to recovery and $D \to 0$ whatever $\rho$ is: a second route to zero duration that this formula does not contain. (v) Price level matters: discount bonds respond asymmetrically (§8.3). On measures: $\rho$ and the $\sigma$'s are $\mathbb{P}$ sample moments, while $D_i$ is the derivative of a $\mathbb{Q}$-consistent price. The gap between $D$ and $D^{\text{emp}}$ is comovement, not mispricing. Nobody is wrong; the bond is just never alone.

### The canonical numbers, rebuilt

Table 8.1 restates Ben Dor's estimates (daily data, August 1998 to November 2009) in our notation.

| Rating | $\rho(\Delta y, \Delta s/s)$ | $H$ as $s \to 0$ ($\beta$) | Slope per 100 bp ($\gamma$) | $R^2$ | $H$ at max sample OAS | Model $H$ at average spread |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aaa–Aa | −0.14 | 0.94 | −0.05 | 0.79 | n/r | 0.95 |
| A | −0.17 | 0.92 | −0.05 | 0.75 | n/r | 0.93 |
| Baa | −0.23 | 0.85 | −0.02 | 0.74 | 0.67 | 0.88 |
| Ba | −0.50 | 0.41 | −0.05 | 0.06 | −0.26 | 0.24 |
| B | −0.56 | 0.15 | −0.03 | 0.01 | −0.42 | −0.04 |
| Caa | −0.40 | 0.07 | −0.02 | 0.01 | −0.52 | −0.23 |

*Table 8.1. Empirical rate hedge ratios by rating. Source: Ben_Dor p.192, Table 7.1 (panels A and B). The last column applies $H = 1 + s\rho\sigma_s/\sigma_y$ at each rating's average spread. "n/r": not reported.*

Read the table like a credit agreement: the interesting clauses are the ones that do not say what you expected. The two-factor model predicts the *ordering* well: IG near one, HY near or below zero. The regression intercepts tell a stranger story. Even as spreads go to zero, Ba bonds hedge at 0.41 and Caa at 0.07. A Ba bond at a tight spread is not a distressed instrument, so the recovery route cannot explain why it ignores Treasuries. And the $R^2$ for high yield is 0.01 to 0.06. The rate component of an HY bond's return is not merely small; it is barely there.

> **[SOURCE EXTRACTION]** *Ben_Dor p.191:* "If this correlation is negative, the empirical duration would be lower than the analytical one and may even end up being negative."
>
> **Annotation.** The sentence is conditional, and the condition is the whole game. In Ben Dor's 1998–2009 sample the correlation was reliably negative, because rates mostly moved on growth news and Fed easing, and spreads moved against them. The book treats the sign as a fact about the sample. A 2026 desk must treat it as a state variable. In 2022 the condition failed: rates rose on inflation and spreads widened with them, so $\rho > 0$ and $H > 1$. The formula held. The parameter moved. Any production system that hard-codes $H$ from a pre-2020 table is a 2022 loss waiting for a calendar.

> **[SOURCE EXTRACTION]** *Dynkin p.437:* "When rates fall, bond prices increase. Due to this negative correlation, however, spreads tend to widen, and thus the bond prices do not increase by as much as would have been expected based on analytical duration alone."
>
> **Annotation.** The plain-English version, and the one to read aloud to a PM who asks why the hedged book lost money on a rally. Note the asymmetry the sentence implies for convex payoffs. On a rally, a long credit position under-earns its duration *and* a full Treasury short loses its full duration, so the hedged book bleeds from both sides. The pooled monthly IG regression in the same chapter (Dynkin p.438–439, January 1992 to April 2014, 737,506 bond-months) finds a base hedge ratio of 0.97 that falls by 0.13 per 1% of spread. That is gentler than daily estimates, which is partly the stale-price effect of §8.5 washing out at monthly horizons.

### Three regimes

The formula $H = 1 + s\,\ell$ has one sign switch, so there are three regimes worth naming:

1. **Flight-to-quality or growth-driven rates, $\rho < 0$.** Yields fall when spreads widen. $H < 1$ for everything and $H \le 0$ for single-B and below. This is the 1998–2009 world and the March 2023 week (§8.7).
2. **Decoupled, $\rho \approx 0$.** Rates and spreads move on unrelated news. $H \approx 1$ even for high yield, and analytical duration is the right hedge by accident. FRED data put 2026 year-to-date here (Trend Watch below).
3. **Inflation-driven rates, $\rho > 0$.** Yields rise when spreads widen, because the same inflation news hurts both. $H > 1$: high yield has *more* rate sensitivity than its analytical duration. This was 2022.

> **Poker Table.** Ines draws it on a napkin. "Two hands. In the first, you're long a Ba bond because you think spreads tighten when the economy is strong, which is also when rates rise. You hedge at the empirical ratio, $H = 0.4$. Rates rise 50 bp, spreads tighten 30 bp, exactly what the correlation predicted, and the hedge and the bond net to zero. You were right, and you got paid nothing. The minimum-variance hedge saw your view in the correlation and hedged it away, because a view is variance. In the second hand you hedge the full analytical duration. Rates rise, the futures pay, spreads tighten, the bond pays. Now you got paid for the view, and you also carried the risk of the view. Pick the hedge that matches the bet you meant to make. If you have a view that spreads tighten when rates rise, the empirical hedge pays you nothing for being right."

> **[SOURCE EXTRACTION]** *Ben_Dor p.219:* "An empirical hedge, reduced to reflect this known correlation, would exactly offset both of these market effects. Is this what the investor intended?"
>
> **Annotation.** This is the most important question in the chapter, asked as a rhetorical aside. A hedge ratio is a choice of objective, not a fact. Minimum total variance gives you $H$. "Zero rate exposure, keep the spread beta" gives you $H = 1$ plus a separate decision about spread. "Zero exposure to both" gives you a different instrument set altogether. ROBO cannot choose among these. The spec must name the objective, and §8.9 makes that a required field.

> **Trend Watch: The Correlation That Changed Sides, 2018–2026.** *What changed.* For two decades the stock–bond correlation was negative or near zero (rolling three-year correlations, November 2000 to 2020, per Morningstar's diversification research as reported in secondary summaries; approx.). It turned positive in 2021 and was roughly 0.58 for full-year 2022 (approx.; secondary summaries of Morningstar's data, which differ on 2023). The rate–spread correlation $\rho_{y,s}$ is a cousin of that number: when inflation drives rates, it drives both. *How big.* In 2022 the 10-year rose from 1.52% to 3.88% and the 2-year from 0.73% to 4.41% (FRED, DGS10/DGS2, year-end closes). The Bloomberg US Corporate High Yield index returned about −11.2% and the IG Corporate index about −15.8% (approx.; secondary data summaries). Apollo's Torsten Slok noted on December 3, 2022 that the HY total-return index was "down 10% so far in 2022" and attributed it mainly to duration. High yield, the asset class with "negative empirical duration," lost money on rates. *What happened next.* Our computation on FRED daily data (ICE BofA OAS by rating against DGS10; relative OAS changes; $H = 1 + \bar s\rho\sigma_s/\sigma_y$; computed 2026-10-17, index level, correlation route only):
>
> | Window | $\rho$: HY / BB / B / CCC / IG | Implied $H$: HY / BB / B / CCC / IG |
> | :--- | :--- | :--- |
> | 2024 (249 days) | −0.34 / −0.39 / −0.29 / −0.22 / −0.38 | 0.65 / 0.64 / 0.66 / 0.61 / 0.92 |
> | 2025 (248 days) | −0.35 / −0.38 / −0.31 / −0.31 / −0.32 | 0.42 / 0.47 / 0.42 / 0.14 / 0.90 |
> | 2026 YTD to Oct 15 (197 days) | −0.03 / −0.10 / +0.02 / +0.09 / −0.08 | 0.97 / 0.90 / 1.03 / 1.19 / 0.98 |
>
> In 2024–2025 high yield behaved like the textbook: 0.4 to 0.65 of analytical duration, and the rolling 60-day CCC hedge ratio touched −0.78 in the window ending May 23, 2025. In 2026 so far, daily rate and spread moves have been nearly uncorrelated, and HY's empirical duration is roughly its analytical duration. IG never left the band [0.79, 1.04] on a rolling 60-day basis. *What it means for the desk.* The hedge ratio is a time series, and its sign has changed twice in five years. Re-estimate monthly, monitor a rolling $\rho$ daily, and treat a zero crossing as a regime alarm (§8.7). One more data-infrastructure fact: FRED's ICE BofA OAS pages state that starting in April 2026 the series include only three years of observations, so the free history now begins in October 2023. A desk that wants Ben Dor's 1998 start date must build its own spread history from TRACE (Appendix B).

### Deep-Dive Resource Graph

**Podcasts.** *Bloomberg Odd Lots*, episodes on the 2022 bond sell-off and on stock–bond correlation (show and topic only). *Resolve Riffs*, discussions of stock–bond correlation regimes (title only).

**Practitioner Writing.** Prentis and Ripka (Wellington, July 31, 2022), "Empirical duration of risk assets": https://www.wellington.com/en-us/institutional/insights/empirical-duration-risk-assets . Slok (Apollo Academy, December 3, 2022), "High Yield Total Returns in 2022 Mainly Driven by Moves in Duration": https://apolloacademy.com/?p=11885 . Mesirow, "Wrong-way bonds" (2021; title only).

**Academic Papers.** Ambastha, Ben Dor, Dynkin, Hyman and Konstantinovsky (2010), "Empirical Duration of Corporate Bonds and Credit Market Segmentation," *Journal of Fixed Income* 20(1). Ilmanen, McGuire and Warga (1994), "The Value of Duration as a Risk Measure for Corporate Debt," *Journal of Fixed Income*: https://www.aqr.com/Insights/Research/Journal-Article/The-Value-Of-Duration-as-a-Risk-Measure-for-Corporate-Debt . Asvanunt and Richardson (2017), "The Credit Risk Premium," *Journal of Fixed Income*: https://www.aqr.com/Insights/Research/Journal-Article/The-Credit-Risk-Premium . Molenaar, Senechal, Swinkels and Wang (2023), *Empirical evidence on the stock–bond correlation* (title only).

**Data & Code.** FRED ICE BofA OAS series BAMLH0A0HYM2, BAMLH0A1HYBB, BAMLH0A2HYB, BAMLH0A3HYC, BAMLC0A0CM and Treasury yields DGS2/DGS10: https://fred.stlouisfed.org/series/BAMLH0A3HYC (note the three-year window). The `empirical_duration` function in §8.9.

## 8.3 The Discontinuity: Why a CCC Bond Is an Equity Option That Wears a Tie to Work

If the hedge ratio depended only on the spread level, then a Baa bond at 700 bp and a Ba bond at 700 bp would hedge identically. In December 2008 they did not. The Baa bond was a downgraded, frightened, wide investment-grade credit that still behaved like a bond. The Ba bond at the same spread behaved like a stock. Something other than credit risk lives at the IG/HY line, and it is worth a section, because it is the most RSSG-friendly fact in quantitative credit: a market's *quoting convention* is a measurable risk factor.

### Two routes to zero duration

There are two separate reasons a corporate bond can stop caring about Treasuries, and a desk that conflates them will mis-hedge both.

**The correlation route** is §8.2: $H = 1 + \ell s$ falls to zero when the expected spread response to a rate move cancels the rate move. The bond's cash flows still discount at Treasury-plus-spread. The market simply moves the spread against the Treasury.

**The recovery route** needs no correlation at all. Take the cleanest possible case under $\mathbb{Q}$: a perpetual bond paying a continuous coupon $c$ per unit of par, a constant short rate $r$, a constant default intensity $\lambda$, and recovery of face $R$ paid at default (the RFV convention). Survival to $t$ has probability $e^{-\lambda t}$, so

$$
P = \int_0^\infty e^{-(r+\lambda)t}\,\big(c + \lambda R\big)\,dt = \frac{c + \lambda R}{r + \lambda} .
$$

The numerator is the bond's flow of value: coupons while it survives, plus the expected recovery arriving at rate $\lambda$. Differentiating with $\lambda$ held fixed gives the bond's true rate sensitivity:

$$
D^{\text{haz}} \equiv -\frac{1}{P}\frac{\partial P}{\partial r} = \frac{1}{r + \lambda} .
$$

The analytical duration on your risk screen is computed from the bond's yield, as if every cash flow were a promised coupon. For a perpetuity priced at $P$, the yield is $y = c/P$ and the yield duration is $D^{\text{yld}} = 1/y$. The ratio is

$$
H^{\text{rec}} \equiv \frac{D^{\text{haz}}}{D^{\text{yld}}} = \frac{y}{r+\lambda} = \frac{c}{c + \lambda R} .
$$

The recovery-route hedge ratio is the share of the bond's value flow that still looks like a bond. As $\lambda \to 0$ it goes to one. As $\lambda \to \infty$ it goes to zero, and the price goes to $R$ whatever $r$ is. That is the restructuring desk's "trades on dollar price" written as a limit. With *illustrative* CCC inputs, $c = 9\%$, $R = 40\%$, and $\lambda = 21\%$ (roughly a 1,280 bp spread over a 60% loss given default), $H^{\text{rec}} = 0.09/(0.09 + 0.084) \approx 0.52$. Half the analytical duration of that bond is fiction before anyone has computed a correlation. To first order the two routes multiply, so $H \approx H^{\text{rec}}\,(1 + \ell s)$, and a CCC book can lose all of its rate sensitivity by either road.

Kaz, reading over Theo's shoulder, frowned at the derivation. "So the fulcrum security is the one where the hedge ratio pivots through zero?"

"The fulcrum," said Mags, "is the class that gets the equity after the lawyers are done. Which is why its hedge ratio is zero." She paused. "You're accidentally right. That's the worst way to be right."

> **[SOURCE EXTRACTION]** *Ben_Dor p.194:* "With hedge ratios near or below zero across most spread levels, high-yield securities more closely resemble equities than bonds."
>
> **Annotation.** Hence the chapter title: a CCC bond is an equity option that wears a tie to work. The same page names the recovery route explicitly. Near default, the market tends to quote all bonds of an issuer at the same seniority "marked at the same dollar price, regardless of maturity," and a price that does not depend on maturity cannot depend on the discount rate. Two departures for 2026. First, "resemble equities" is now an instruction rather than an analogy. The natural hedge for a CCC position is a credit-equity instrument (CDX HY, single-name or index puts; §8.6), not a futures contract. Second, the 2024–2026 FRED data in §8.2 show HY hedge ratios between 0.4 and 1.0 at the index level. "Near or below zero" described a sample in which $\rho$ was strongly negative. The equity-like *recovery* behavior of CCCs is structural. The equity-like *correlation* behavior of the whole HY market is a regime.

### The segmentation hypothesis

Now the puzzle. The recovery route explains a CCC bond trading at 45. It does not explain a Ba bond at a tight spread hedging at 0.41 (Table 8.1). Ben Dor runs three tests that rule out the obvious explanations. Excluding bonds priced below 80 does not remove the gap, so distress is not the cause. Comparing Baa bonds during the 2008–2009 crisis with Ba bonds at *overlapping* spread levels shows Baa still behaving like a bond. Liquidity controls do not close it either.

> **[SOURCE EXTRACTION]** *Ben_Dor p.207:* "Baa bonds maintained a hedge ratio of 0.71, even at spreads of 700 bps, whereas high-yield bonds exhibited zero or even negative hedge ratios for the same level of spreads."
>
> **Annotation.** This is the overlap test, and it is the cleanest evidence in the chapter that the IG/HY line is a market convention, not a credit fact. Same spread, same macro shock, opposite behavior. The explanation offered (p.203) is sociological: investment-grade bonds are quoted as a spread to a parent Treasury and run against excess-return benchmarks, so an IG trader's screen literally moves when the 10-year moves. High-yield bonds are quoted in price and run on total return, so an HY trader's screen moves when the bid moves. For a systematic desk this has a concrete consequence. A bond downgraded from Baa3 to Ba1 changes its rate hedge ratio *at the moment it changes investor base*, before anything about its cash flows changes. The fallen-angel trade of Chapter 9 inherits a rate-hedge jump you should model, not discover.

Ben Dor also documents a nonlinearity (p.200). When Ba spreads topped 600 bp in 2002, empirical duration fell to about −2. As spreads blew past 1,000 bp in early 2009, the linear model predicted something far more negative, and it never came: durations bottomed not far below zero. The physics is the recovery route. As $\lambda$ rises, $H^{\text{rec}} \to 0$ squeezes the whole product toward zero from both sides. A deeply negative empirical duration requires a bond that is still rate-sensitive *and* strongly anti-correlated, and very distressed bonds are neither. The production consequence: clip extrapolated $H(s)$ at a floor such as $-0.5$ *(illustrative)* rather than trusting a linear fit at spreads the sample never saw.

> **Desk Myth vs. Desk Reality.** *Myth:* "High yield has negative duration." *Reality:* High yield had negative empirical duration when the Fed was the only thing moving rates. In 2022, inflation moved rates, and high yield had a duration of "yes."

### Price level: the discount-bond asymmetry

One more state variable. Dynkin's Tables 10.2–10.3 split bonds by price. Discount bonds show an empirical hedge ratio of 1.00 when yields fall and 0.72 when they rise; premium bonds show 0.80 and 0.86. Discount bonds respond fully to good rate news and only partially to bad rate news.

> **[SOURCE EXTRACTION]** *Dynkin p.439–440:* "discount bonds should follow a highly desirable behavior in which they react more strongly to favorable yield changes and less strongly to unfavorable ones—a positive convexity effect."
>
> **Annotation.** Why this is a 2026 problem: the 2020–2021 issuance vintage priced low coupons at par, and after the 2022 rate shock much of it trades at a discount. A discount bond has more call-free runway (no rational issuer calls a 3.75% coupon in a 5% world), so its duration does not shorten when rates fall. That is part of the positive convexity. A premium callable does the opposite, because its duration collapses toward the call date in a rally. An HY book whose discount share has risen therefore has a hedge ratio that depends on the *direction* of the next move. The regression of §8.2 should carry a price-bucket interaction, or be run separately for rising- and falling-yield days, before its $H$ goes into a hedge.

### Case Study: One Bond, Four Hedge Ratios (Alltel's 7.875% 30-Year, 2006–2009)

Ben Dor (p.211) follows a single security through a capital-structure round trip: the Alltel 7.875% bond with thirty years to maturity at issue. (The book prints the CUSIP; we describe the bond and do not reprint identifiers.) The path, using Ben Dor's dates and estimated hedge ratios:

1. **2006, rated A2, spread about +200 bp.** Rolling empirical hedge ratio about 0.75: a long-dated IG bond behaving like a long-dated IG bond.
2. **May 23, 2007, downgraded to Ba2 at about +450 bp**, as the company headed into a leveraged buyout by TPG and GS Capital Partners. Hedge ratio falls to about 0.4. Nothing about the coupon or maturity changed. The holder base and the quoting convention did.
3. **November 21, 2007, downgraded to Caa1** as the buyout closed and the bond sat in a heavily levered structure. Hedge ratio falls into negative territory, as low as −0.6.
4. **January 8, 2009, Verizon's acquisition closes and the bond is re-rated A2.** The hedge ratio climbs from about 0.25 back to about 0.95.

> **[SOURCE EXTRACTION]** *Ben_Dor p.211:* "When the bond was further downgraded to Caa1 on November 21, 2007, the hedge ratio dropped even further to negative territory (as a low as −0.6)."
>
> **Annotation.** One security, one indenture, four hedge ratios, from 0.95 to −0.6. A desk that estimated this bond's empirical duration over 2006–2009 as one number would have been wrong in every sub-period. The systematic lesson is that $H$ is a function of rating *bucket*, spread, and price, re-evaluated whenever any of them changes, with the rating transition treated as a jump. The RSSG lesson is better. The 2007 downgrades were the market repricing a change in the capital structure, the LBO debt landing on top of the existing bonds, and the hedge ratio moved *with the capital structure, not with the cash flows*. Chapter 13 asks whether the same signature appears before a priming transaction. If a bond's rate beta collapses before the uptier is announced, that is a free early-warning feature for the Priming Risk Score.

How a systematic desk would have traded it: carry a rating-bucket $H$ table re-estimated monthly; on a downgrade across the IG/HY line, switch the bond's $H$ to the new bucket's value *on the day* rather than waiting for a trailing window to notice; and size the Treasury hedge for the whole HY book from bucket-level $H$, never bond-level, because bond-level $R^2$ is 0.01.

> **Trend Watch: CCC Decompression, 2024–2026.** *What changed.* The CCC tier has come apart from the rest of high yield. On FRED's ICE BofA series the CCC-and-lower to BB OAS ratio was 4.0× at the end of 2024 (746 bp / 186 bp), 5.2× at the end of 2025 (885 / 169), and 6.5× on October 15, 2026 (1,278 / 197). The CCC OAS reached 12.82% on October 14, 2026 (HY 3.25%, IG 0.84% that day); on October 15 the CCC OAS was 12.78%, the broad HY OAS 3.23% and IG 0.84% (computed 2026-10-17). The beta of CCC relative spread changes on HY relative spread changes fell from 0.54 (2024) and 0.55 (2025) to 0.45 (2026 year to date). *What it means for the desk.* CCCs are loading less on the market spread factor and more on something issuer-specific. In this chapter's vocabulary, more of their return is idiosyncratic, which for a pure-IDO book is opportunity and for a DTS-scaled risk model is a warning: DTS assumes relative spread changes are common across credits, and in the CCC tier that assumption is weakening. We do not attribute causes here; Chapter 11 takes up the CCC problem and Chapter 14 the recoveries behind it.

## 8.4 DTS: The Unit of Credit Beta

The restructuring banker's instinct is that leverage is not one number. Six turns of debt at a software company and six turns at a regional grocer are different risks, and the spread already tells you how different. DTS is the same instinct applied to spread risk. Two bonds with identical spread duration are not equally risky if one trades at 80 bp and the other at 800 bp, because spreads do not move in basis points. They move in percent.

### The derivation

Ben Dor's central empirical regularity is that the volatility of spread changes is proportional to the spread level:

$$
\sigma(\Delta s_i) \approx \kappa\, s_i ,
$$

where $\kappa$ is a relative spread volatility (for example, per month) that is roughly common across bonds within a market. Combine it with the first-order excess return of §8.1, $R^{\text{xs}}_i \approx -D^{\text{spr}}_i\,\Delta s_i$:

$$
\sigma\big(R^{\text{xs}}_i\big) \approx D^{\text{spr}}_i\,\sigma(\Delta s_i) \approx \kappa\, D^{\text{spr}}_i\, s_i = \kappa\,\text{DTS}_i .
$$

Excess-return volatility is linear in DTS with slope $\kappa$. Ben Dor estimates the slope at 8.8% per month for investment grade, with an $R^2$ of 98% (p.51). The arithmetic for a bond with $D^{\text{spr}} = 6$ and $s = 1.5\%$: $\text{DTS} = 6 \times 0.015 = 0.09$, so monthly excess-return volatility is about $0.088 \times 0.09 = 0.79\%$. At very low spreads the line has a small structural floor (p.57), which is why DTS slightly understates the risk of the tightest bonds.

Now the beta. Suppose relative spread changes share a common market component, $\Delta s_i/s_i = x_{M} + u_i$, with $u_i$ idiosyncratic. Then

$$
R^{\text{xs}}_i \approx -\text{DTS}_i\,x_M - \text{DTS}_i\,u_i, \qquad R^{\text{xs}}_M \approx -\text{DTS}_M\,x_M ,
$$

so bond $i$'s beta to the market's excess return is

$$
\beta_{i,M} = \frac{\mathrm{Cov}(R^{\text{xs}}_i, R^{\text{xs}}_M)}{\mathrm{Var}(R^{\text{xs}}_M)} = \frac{\text{DTS}_i}{\text{DTS}_M} .
$$

That is the reason for this section's title. In the DTS world, credit beta is not estimated; it is *computed* from two numbers on your risk screen. Merton's model supports the near-linearity: for firms away from default, the spread's sensitivity to asset value scales roughly with the spread itself (Ben_Dor p.104–105).

> **[SOURCE EXTRACTION]** *Ben_Dor p.50:* "a portfolio with a weighted spread of 200 bps and spread duration of two years is equally risky as a portfolio with a spread of 100 bps and spread duration of four years."
>
> **Annotation.** The sentence that ended the reign of spread duration as the risk unit. For an RSSG reader the translation is that a two-year secured term loan at +400 and a four-year unsecured note at +200 carry the same spread risk, which is precisely the comparison a lender group makes when it trades a maturity extension for a rate increase. The 2026 caveat is the CCC Trend Watch above. DTS's equivalence rests on *common relative* spread moves, and the tier where relative moves are least common is where most of the IDO lives. Use DTS as the default risk unit, and let the residual covariance (§8.8) catch what it misses.

### DTS-neutral pairs, and why they carry nothing

A long–short pair hedged to zero DTS is the workhorse relative-value trade. With long bond $L$ and short bond $S$, set the short notional per unit long to

$$
h_S = \frac{\text{DTS}_L}{\text{DTS}_S} = \frac{D^{\text{spr}}_L\,s_L}{D^{\text{spr}}_S\,s_S} .
$$

If the two bonds have similar spread durations, $h_S \approx s_L/s_S$, and the pair's OAS carry is $s_L\,\Delta t - h_S\,s_S\,\Delta t \approx 0$. Ben Dor makes the point directly: matching DTS with similar spread durations "means the trades will also be zero-carry trades" (p.228). Read that as a feature, not a footnote. A DTS-neutral pair has stripped market spread beta *and* the carry that market beta pays you for holding. What it earns, it earns from convergence between the two names. That is IDO by construction, which is why the DTS-neutral pair is the unit test for any relative-value signal (Chapter 9).

### Why DTS beats an estimated beta

The obvious objection: why compute beta from DTS when you can estimate it by regression? Because the regression is unstable, not because it is biased.

> **[SOURCE EXTRACTION]** *Ben_Dor p.274:* "the average standard deviation of the beta-based hedge ratios (1.4) is more than double that of the DTS-based hedge ratios (0.6)."
>
> **Annotation.** On average, the estimated beta and the DTS ratio agree. Month to month, the estimated beta wanders more than twice as far. A hedge ratio that wanders forces rebalancing, and rebalancing in corporate bonds costs real bid–ask (Chapter 18). The general principle, which reappears in every shrinkage estimator in this book: when a structural model gives you an unbiased, low-variance answer, an unrestricted regression has to beat it out of sample, not in sample. For the 2026 desk the practical blend is to start from $\text{DTS}_i/\text{DTS}_M$ and shrink a rolling regression beta toward it, with the shrinkage weight set by out-of-sample hedge error. The DTS ratio is the prior. The data have to earn the deviation.

> **[SOURCE EXTRACTION]** *Man_2022 p.15:* "We therefore adjust our statistical factor risk model (SFRM) with Duration Times Spread (DTS) in order to take into account the various issues referenced above."
>
> **Annotation.** This is how DTS travels into a modern risk stack. Divide each bond's excess return by its DTS, estimate the covariance or principal components on the scaled returns, and multiply back. Without the scaling, a statistical factor model spends its first principal component discovering that high-spread bonds are volatile, which you already knew. With it, the components describe *how* bonds co-move rather than *how much*. Man's motivation (p.13) is that bond betas are "less concentrated around the mean than for equities," so a model that assumes equity-like beta dispersion mis-sizes everything. ROBO's version of the instruction is short. *DTS-scale before any covariance estimate; never estimate a covariance on raw excess returns of bonds whose spreads differ by more than a factor of two.*

> **Ways This Blows Up.** (1) *Wrong duration.* DTS uses spread duration. For a floating-rate loan, rate duration is near zero but spread duration is roughly the time to maturity or the expected refinancing date. Use $D^{\text{mod}}$ and your loan book shows no credit risk. (2) *Negative or tiny OAS.* Some very short or very high-quality bonds print negative OAS, which makes DTS negative and relative spread changes explode. Guard with `assert oas > 0` before computing $\Delta s/s$, and fall back to absolute changes with a warning. (3) *A regime-dependent slope.* $\kappa$ is not a constant of nature. It rises sharply in crises, and the proportionality itself bends in the CCC tier (Trend Watch above). DTS makes betas comparable across bonds at a point in time. It does not make volatility forecastable across regimes.

## 8.5 Betas When Nothing Trades: Dimson, Scholes–Williams, and the Lag That Isn't Noise

Every regression in this chapter so far has assumed that a bond's return on day $t$ is the bond's return on day $t$. It usually is not. In September 2009, about half the bonds in the Corporate and High Yield indices traded fewer than 15 times in the month, and 25–30% did not trade at all. Monthly turnover was about 5% of amount outstanding for IG and 4% for HY (Ben_Dor p.203). The daily "return" of a bond that did not trade is the change in an evaluated price, which is a pricing service's opinion of where it would have traded. That opinion is anchored to yesterday's opinion. A stale bond price is like a lender call: the information arrived days ago, and it is only now being acknowledged.

The signature is visible in volatility. Across Ben Dor's liquidity quintiles, daily price-return volatility differs by roughly 40% between the extremes: 122 versus 72 bp a day for Caa, 86 versus 54 for B, 67 versus 39 for Ba (Ben_Dor p.206, Table 7.4). Some of that gap is genuine risk, but much of it is smoothing. Stale prices are smoother prices, and smoother prices produce smaller betas.

### The smoothing model and the bias it creates

Following Getmansky, Lo and Makarov (2004), who note that "reported returns will tend to be smoother than true economic returns," model the observed return as a moving average of true returns:

$$
r^{o}_t = \sum_{k=0}^{q} \theta_k\, r_{t-k}, \qquad \theta_k \ge 0, \qquad \sum_{k=0}^{q}\theta_k = 1 .
$$

The weights sum to one, so the information arrives eventually; it just arrives late. Let the true return follow a factor model, $r_t = \alpha + \beta f_t + \epsilon_t$, with $f_t$ serially uncorrelated with variance $\sigma_f^2$. The contemporaneous covariance picks up only the first weight:

$$
\mathrm{Cov}(r^{o}_t, f_t) = \theta_0\,\beta\,\sigma_f^2 \quad\Longrightarrow\quad \hat\beta_{\text{OLS}} \xrightarrow{p} \theta_0\,\beta < \beta .
$$

OLS on stale data is biased toward zero by exactly the fraction of information that arrives on time. The variance is biased too. If $r_t$ is itself serially uncorrelated,

$$
\mathrm{Var}(r^{o}_t) = \sigma_r^2 \sum_{k=0}^{q}\theta_k^2 < \sigma_r^2 ,
$$

because $\sum\theta_k^2 < (\sum\theta_k)^2 = 1$ whenever more than one weight is positive. With $\theta = (0.5, 0.3, 0.2)$ the observed volatility is $\sqrt{0.25 + 0.09 + 0.04} = 0.616$ of the true volatility. A risk model fed these marks thinks the book is 38% less volatile than it is. The hedge, sized on the stale beta, is half as large as it should be.

**The Dimson fix.** Regress the observed return on leads and lags of the factor, and sum the coefficients (Dimson, 1979):

$$
r^{o}_t = a + \sum_{k=-L}^{L} b_k\, f_{t-k} + e_t, \qquad \hat\beta_{\text{D}} = \sum_{k=-L}^{L}\hat b_k .
$$

Under the smoothing model with serially uncorrelated $f$, $\mathrm{Cov}(r^o_t, f_{t-k}) = \theta_k\beta\sigma_f^2$, so $\hat b_k \to \theta_k\beta$ for $0 \le k \le q$ and the sum recovers $\beta$ once $L \ge q$. Leads ($k < 0$) are there in case the *factor* is the stale one, which happens when you regress a bond on an index built from evaluated prices.

**Scholes–Williams.** With one lead and one lag, each from a separate univariate regression, and $\hat\rho_f$ the factor's first-order autocorrelation, Scholes and Williams (1977) give

$$
\hat\beta_{\text{SW}} = \frac{\hat b_{-1} + \hat b_{0} + \hat b_{+1}}{1 + 2\hat\rho_f} .
$$

The denominator corrects for the factor's own autocorrelation, which univariate regressions would otherwise double-count. It recovers only one lag of smoothing, so on a bond with two days of staleness it under-corrects.

**De-smoothing the series itself.** Dimson fixes a beta; sometimes you need the whole return series, for a volatility, a drawdown, or a covariance matrix. The Dimson coefficients estimate the smoothing weights, $\hat\theta_k = \hat b_k / \sum_j \hat b_j$. Invert the moving average recursively:

$$
\hat r_t = \frac{r^{o}_t - \sum_{k=1}^{q}\hat\theta_k\,\hat r_{t-k}}{\hat\theta_0} .
$$

The recursion is stable only if the moving-average polynomial $\theta_0 + \theta_1 z + \dots + \theta_q z^q$ has all its roots outside the unit circle. Check this before running it. A non-invertible $\hat\theta$ produces a de-smoothed series that explodes politely over a few hundred days.

**The monthly shortcut.** When only monthly data exist, Dynkin corrects annualized volatility for first-order autocorrelation alone. If returns have autocorrelation $\phi_1$ at lag one and none beyond, the variance of a 12-month sum is $12\sigma_m^2 + 2\cdot 11\cdot\phi_1\sigma_m^2$, because a year contains 11 adjacent pairs of months. Hence

$$
\sigma_{\text{ann}} = \sigma_m\sqrt{12 + 2\cdot 11\cdot \phi_1} .
$$

> **[SOURCE EXTRACTION]** *Dynkin p.129 (n.27):* "the annualized volatility is calculated as volatility in monthly returns multiplied by the squared-root of (12+2*11*AR1)"
>
> **Annotation.** A footnote doing a load-bearing job. For a monthly credit strategy with $\phi_1 = 0.3$, the correction factor is $\sqrt{18.6}/\sqrt{12} = 1.25$, so the naive Sharpe ratio is overstated by a quarter. Two departures for the desk. The formula keeps only the first autocorrelation, so a strategy holding stale CCC paper with two or three months of smoothing needs the full sum $12 + 2\sum_{k=1}^{11}(12-k)\phi_k$. And the same correction belongs on any *backtest* Sharpe ratio built from evaluated prices, which is most of them. Chapter 7's deflated Sharpe ratio assumes you have already done this.

> **[SOURCE EXTRACTION]** *Dynkin p.623:* "if corporate bond prices are only updated infrequently and are subject to "stale" pricing, their returns are likely to be positively correlated as new information slowly gets priced in."
>
> **Annotation.** Positive autocorrelation as a staleness detector is a cheap, model-free diagnostic, and it belongs in the data-quality layer, not the alpha layer. Compute it per bond and per price source. TRACE last-trade returns and vendor evaluated prices smooth differently, and mixing them in one series manufactures autocorrelation from the switch itself. The counterpoint is Bao, Pan and Wang (2011), who measure illiquidity from *negative* autocovariance of transaction price changes: bid–ask bounce. Transaction data bounce and evaluated data smooth, so the sign of the first autocorrelation tells you which disease you have before you prescribe a lag.

### The trap: lags that carry information

Here the econometrics meets the trading. Dimson assumes the lagged coefficients are pure smoothing, information that was always going to arrive. Some of it is genuine *information diffusion*: the equity market learns first and the bond market follows. Gebhardt, Hvidkjaer and Swaminathan (2005) document momentum spillover from stocks to bonds. Dynkin (p.606) reports that bonds of issuers in the bottom equity-momentum decile delivered −4.7% a year of excess return over 1993–2017, against about +4.0% for the top decile. A Dimson beta of a bond on its issuer's stock is therefore part stale-price correction and part trend signal. Sum the lags into the hedge and you hedge away a signal Chapter 10 would like to trade. The practical rule: estimate Dimson betas against *rates and credit-index* factors, where the lag is mostly staleness, and treat lagged *equity* coefficients as a candidate signal, to be validated out of sample before it is allowed to change a hedge.

A *computed illustration*, offered as a hypothesis rather than proof. On FRED daily ICE BofA index data from January 2024 to October 2026, the same-day correlation between relative OAS changes and 10-year yield changes is −0.27 for HY, −0.32 for BB, −0.23 for B, −0.19 for CCC, and −0.28 for IG. The correlation with the *previous* day's yield change is +0.098, +0.125, +0.091, +0.038, and −0.041 respectively (computed 2026-10-17). High yield partially reverses its same-day spread response the next day; investment grade does not.

> **[SOURCE EXTRACTION]** *Ben_Dor p.203:* "Investment-grade bonds are typically quoted as a spread to a Treasury security with similar maturity ("parent"), whereas high-yield bonds are quoted on price."
>
> **Annotation.** The convention predicts the pattern. If an HY bond's price is sticky and the Treasury sells off, the computed OAS (yield implied by an unchanged price, minus a higher Treasury yield) mechanically *tightens* the same day, then widens back as the price catches up. Part of high yield's negative daily rate–spread correlation is the OAS calculator doing arithmetic on a stale price. An IG bond quoted at a fixed spread to its parent moves its price with Treasuries automatically, so no reversal appears. Ben Dor's tests (p.207) show staleness cannot explain the whole IG/HY gap at the levels they study. Our point is narrower and operational: at *daily* frequency, a Dimson-summed $\rho$ for HY is materially closer to zero than the same-day $\rho$. With the numbers above, summing one lag cuts HY's same-day correlation from −0.27 to roughly −0.17, which moves the pooled 2024–2026 HY hedge ratio from about 0.72 toward 0.82 *(illustrative arithmetic: equal-variance lags, so coefficient ratios equal correlation ratios)*. Hedge at a weekly horizon or Dimson-sum the daily one. Do not hedge daily on a same-day estimate.

> **Ways This Blows Up.** (1) *Too many lags.* Each lag adds a coefficient's worth of estimation noise to the sum. Cap $L$ at 2–3 for daily data and 1 for monthly, or shrink the lag coefficients toward zero; the code refuses $L > 5$. (2) *Forward-filled prices.* A missing price forward-filled into a return series creates zeros followed by catch-up jumps, a smoothing model you invented. Compute returns only between actual marks, and record the gap length so the smoothing model can use it. (3) *Overlapping returns.* Weekly returns sampled daily overlap, so the regression errors are a moving average. Use Newey–West standard errors or non-overlapping samples, or the $t$-statistics on your hedge ratios are fiction.

### Deep-Dive Resource Graph

**Podcasts.** *Flirting with Models* (Corey Hoffstein), episodes on systematic credit and on smoothed returns in private and illiquid assets (show and topic only).

**Practitioner Writing.** Asness, Krail and Liew (2001), "Do Hedge Funds Hedge?", *Journal of Portfolio Management* 28(1): the canonical demonstration that summed lagged betas reveal market exposure hidden by stale marks (DOI 10.3905/jpm.2001.319819).

**Academic Papers.** Dimson (1979), "Risk measurement when shares are subject to infrequent trading," *Journal of Financial Economics* 7(2): https://ideas.repec.org/a/eee/jfinec/v7y1979i2p197-226.html . Scholes and Williams (1977), "Estimating betas from nonsynchronous data," *Journal of Financial Economics* 5(3): https://ideas.repec.org/a/eee/jfinec/v5y1977i3p309-327.html . Getmansky, Lo and Makarov (2004), "An econometric model of serial correlation and illiquidity in hedge fund returns," *Journal of Financial Economics* 74(3): https://ideas.repec.org/a/eee/jfinec/v74y2004i3p529-609.html . Bao, Pan and Wang (2011), "The Illiquidity of Corporate Bonds," *Journal of Finance* 66(3): https://ideas.repec.org/a/bla/jfinan/v66y2011i3p911-946.html . Gebhardt, Hvidkjaer and Swaminathan (2005), "Stock and bond market interaction: Does momentum spill over?", *Journal of Financial Economics* 75(3): https://ideas.repec.org/a/eee/jfinec/v75y2005i3p651-690.html .

**Data & Code.** FINRA TRACE (canonical root https://www.finra.org/filing-reporting/trace) for transaction-based returns; `dimson_beta`, `scholes_williams_beta`, and `desmooth` in §8.9.

## 8.6 The Hedge Matrix: CDX, UST Futures, HYG/JNK, Equity Puts

At 2:58 p.m., Theo cannot short "the market spread factor." He can short what is on the screen, and each instrument there is a different, imperfect, separately priced claim on the factors he wants to remove. Ines's framing: "You don't get to hedge the risk. You get to trade the instruments. The difference is the basis, and the basis is a position."

### The instruments, in DV01 terms

**US Treasury futures (TY, UXY, and the rest).** The rates leg. A futures contract does not deliver one bond; it delivers whichever eligible note the short chooses, at an invoice price set by a conversion factor.

> **[SOURCE EXTRACTION]** *Veronesi p.237:* "The invoice price equals the futures settlement price times a conversion factor plus accrued interest. The conversion factor is the price of the delivered note (\$1 par value) to yield 6 percent."
>
> **Annotation.** The 6% notional coupon matters because, with yields far from 6%, the conversion factor mis-scales the deliverables and one of them becomes reliably cheapest. The futures then trade like that bond divided by its conversion factor. Hence the hedge sizing $N = \text{DV01}_{\text{target}} / (\text{DV01}_{\text{CTD}}/\text{CF})$, where $\text{DV01}_{\text{CTD}}$ is per contract face (\$100,000 for TY). For the cold-open bond, $\text{DV01}_{\text{target}} = \$40\text{mm} \times 4.1 \times 0.0001 = \$16{,}400$. With *illustrative* CTD inputs of \$63 DV01 per \$100,000 face and $\text{CF} = 0.89$, one contract carries about \$70.8 of DV01, so a full analytical hedge is 232 contracts. Two departures for a credit desk. Futures settle daily, so a precise hedge is "tailed" by the discount factor to delivery (Veronesi p.269), which matters for size and long horizons and hardly at all for a one-week hedge. And when the CTD switches, the futures' DV01 jumps, which is the futures' own convexity and a source of hedge slippage that has nothing to do with credit.

Kaz, reading the futures primer, looked up. "Cheapest-to-deliver. Is that a kind of drop-down?"

"Same idea, better suit," Mags said. "The short picks which bond to hand you, and he picks the one that hurts you most. In a drop-down, the sponsor picks which assets you get to keep. Both times it's an option against whoever is long and not paying attention."

**CDX HY.** The spread leg in its purest listed form. The index trades in price with a fixed 500 bp running coupon and rolls to a new series every March 20 and September 20. Sign conventions are where desks lose money. Buying protection is *short* credit. The quoted price *rises* when spreads tighten. For small moves $\Delta P \approx -\text{RPV01}\cdot\Delta s$, where RPV01 is the index's risky annuity, roughly its spread duration. The index is a near-perfect hedge for HY market spread beta and a terrible hedge for anything idiosyncratic, which is the point.

**HYG and JNK.** The cash-bond beta, wrapped in an exchange-traded fund. As of mid-October 2026, HYG had net assets of about \$17.2bn across 1,334 holdings, an effective duration of 3.20 years, an OAS of 284 bp, and 30-day average volume of about 64.6 million shares. JNK had about \$5.7bn of assets, 1,161 holdings, and an option-adjusted duration of 3.23 years (ishares.com and ssga.com product pages, October 15–16, 2026). The ETFs carry *both* rates and spread exposure, and in stress their price departs from NAV. That is a basis you are long or short whether you meant to be or not (Chapter 20). JNK tracks the same Bloomberg High Yield Very Liquid index family that underlies CME's HY credit future, which makes the pair a natural arbitrage leg.

**Equity puts.** The tail leg, and the one Kaz finds most natural, because Ben Dor already told him a CCC bond resembles equity (§8.3). Carr and Wu (2011) show that a spread between two co-terminal American puts struck inside a default corridor "replicates a pure credit contract." For a CCC book, single-name or index puts hedge the jump to default that CDX dilutes across a hundred names. For a BB book they are mostly an expensive way to buy noise.

**Non-synchronous closes.** These instruments do not stop moving at the same moment. Treasury futures settle in the early afternoon Chicago time (around 3 p.m. New York), evaluated bond prices are typically struck mid-to-late afternoon in New York, equities close at 4 p.m., and CDX end-of-day marks come later still *(approx.; check each venue's methodology)*. A daily covariance between a bond priced at 3:30 and an index marked at 5:00 is §8.5's staleness problem, built in by design. Estimate the hedge matrix on Dimson-summed covariances,

$$
\Sigma^{\text{D}}_{Hp} = \sum_{k=-1}^{1}\mathrm{Cov}(r_{H,t-k},\, r_{p,t}),
$$

or on weekly returns, and use daily data only to monitor.

### The derivation: minimum variance, ridge, and hedging less

Let $r_p$ be the target portfolio's return and $r_H \in \mathbb{R}^m$ the returns of $m$ hedge instruments, each per \$1 of notional. Choose hedge weights $h$, the notional of each instrument to *short* per \$1 of target, to minimize the variance of the hedged return $r_p - h^\top r_H$ under $\mathbb{P}$:

$$
\mathrm{Var}(r_p - h^\top r_H) = \sigma_p^2 - 2\,h^\top\Sigma_{Hp} + h^\top\Sigma_{HH}\,h .
$$

The first-order condition $-2\Sigma_{Hp} + 2\Sigma_{HH}h = 0$ gives

$$
h^\star = \Sigma_{HH}^{-1}\,\Sigma_{Hp}, \qquad \sigma^2_{\text{resid}} = \sigma_p^2 - \Sigma_{pH}\,\Sigma_{HH}^{-1}\,\Sigma_{Hp} .
$$

This is OLS of $r_p$ on $r_H$, and it has the problem of OLS on a screen full of substitutes. HYG, JNK, and CDX HY all load on the same spread factor, with daily correlations around 0.9 *(illustrative)*, so $\Sigma_{HH}$ is nearly singular. Its condition number, $\text{cond}(\Sigma) = \mu_{\max}/\mu_{\min}$ (the ratio of its largest to smallest eigenvalue), runs into the thousands. In that state, OLS answers a small change in the sample with a large, offsetting long–short in two near-identical ETFs. The in-sample residual barely improves. The gross notional, the trading costs, and the out-of-sample error get worse.

**Ridge.** Penalize the size of the hedge. We call the penalty $\eta$, because $\lambda$ is reserved for default intensity. With the penalty scaled by each instrument's variance, so it does not depend on units,

$$
h_\eta = \big(\Sigma_{HH} + \eta\,\mathrm{diag}(\Sigma_{HH})\big)^{-1}\Sigma_{Hp} .
$$

Equivalently, standardize the instruments to unit variance, so their covariance becomes the correlation matrix $C$, and add $\eta I$ to $C$. On that scale the condition number after regularization is $(\mu_{\max}+\eta)/(\mu_{\min}+\eta)$. To cap it at a target $c^{\max}$, solve for the smallest sufficient penalty:

$$
\eta = \max\!\left(0,\; \frac{\mu_{\max} - c^{\max}\,\mu_{\min}}{c^{\max} - 1}\right).
$$

Our default is $c^{\max} = 50$ *(illustrative; tune on out-of-sample hedge error)*. It is deterministic, cheap, and explains itself in a risk meeting.

**Constraints.** Real hedges have limits: position bounds $|h_j| \le h_j^{\max}$ from liquidity, a gross notional budget $\sum_j |h_j| \le G$, and sometimes a sign constraint (you may not be allowed to *buy* puts in a mandate). The constrained problem is a small quadratic program,

$$
\min_h\; h^\top(\Sigma_{HH} + \eta\,\mathrm{diag}\,\Sigma_{HH})\,h - 2\,h^\top\Sigma_{Hp} \quad \text{s.t.}\quad |h_j| \le h_j^{\max} ,
$$

which a bounded quasi-Newton solver handles in milliseconds.

**Why you hedge less than the naive amount.** Suppose the target loads $b$ on a factor $f$, $r_p = b\,f + e_p$, and the only available hedge is an impure factor proxy, $r_H = f + e_H$, with its own noise of variance $\omega^2$ independent of everything else. The naive hedge shorts $b$ units. The minimum-variance hedge shorts

$$
h^\star = \frac{\mathrm{Cov}(r_p, r_H)}{\mathrm{Var}(r_H)} = b\,\frac{\sigma_f^2}{\sigma_f^2 + \omega^2} < b .
$$

Every unit of hedge imports $\omega^2$ of the instrument's own noise, so past a point, more hedge adds more risk than it removes. The matrix version, with $\Omega_f$ the factor covariance and $\Omega_{\text{FMP}}$ the idiosyncratic covariance of the factor-mimicking hedge portfolios, is $h^\star = (\Omega_f + \Omega_{\text{FMP}})^{-1}\Omega_f\,b$: a shrinkage of the naive hedge $b$ that is strongest along directions where the hedge instruments are noisiest. Paleologo derives the full version, including trading costs.

> **[SOURCE EXTRACTION]** *Paleologo p.196:* "To a first approximation, we always hedge less than in the "naïve" hedge"
>
> **Annotation.** Paleologo is writing about equity factor hedging with factor-mimicking portfolios. Credit is the harder case. Every credit hedge instrument is a noisy proxy: CDX has a basis to cash, HYG has a basis to NAV, Treasury futures have a basis to the CTD, and puts carry volatility risk. So the attenuation in the scalar formula above is large, not a rounding refinement. The ridge solution is the same idea from the estimation side. Shrinking $h$ toward zero is right when the instruments are noisy, *and* right when the covariance estimate is noisy, and on a credit desk both are true at 2:58 on a Friday.

> **[SOURCE EXTRACTION]** *Paleologo p.195:* "It is important to minimize total risk, and not just factor risk. Factor-mimicking portfolios contain idiosyncratic risk, and this risk should not be ignored."
>
> **Annotation.** This is the line ROBO needs most. "Zero out the spread beta" is a factor-risk objective, and the cheapest way to achieve it with HYG adds the ETF's own basis risk to the book. The objective in the spec is total hedged variance, subject to whatever factor exposures you *choose* to keep. Paleologo p.40 adds that even the simplest hedge, shorting the market against a long book, is run daily on portfolios worth hundreds of billions of dollars. Simple is not the same as safe.

### Theo's hedge, four ways

Back to the cold open: \$40mm of a B3 bond, analytical DV01 \$16,400, 70.8 DV01 per TY contract. The futures leg alone, sized at different hedge ratios:

| Hedge-ratio source | $H$ | TY contracts short |
| :--- | ---: | ---: |
| Analytical (Kaz) | 1.00 | 232 |
| FRED pooled B, Oct 2023–Oct 2026 | 0.73 | 169 |
| FRED B, 2026 YTD | 1.03 | 239 |
| Ben Dor B, 1998–2009, at the average spread | −0.04 | 0 (or a tiny long) |

*Table 8.2. One bond, four defensible hedges (FRED rows computed 2026-10-17 at the B index level and its average spread, not at Theo's 620 bp; Ben Dor row from Table 8.1).*

Every row is defensible, which is the indictment. The hedge ratio is a bet on *why rates will move* over the hedge horizon. The matrix approach does not remove that bet. It makes the bet explicit, and it lets the CDX leg take the spread beta that the futures were implicitly being asked to absorb. The Ad Hoc Group, represented by counsel, confirms that its members' positions are fully hedged with respect to interest rates, and declines to say with what.

> **Trend Watch: Listed Credit Beta and the Duration-Hedged Index Family, 2014–2026.** *What changed.* In an April 23, 2024 announcement, CME Group said it would launch credit futures on June 17, 2024, pending regulatory review, on the Bloomberg US Corporate (IG) Index and the Bloomberg US High Yield Very Liquid Index, along with futures on a Bloomberg *duration-hedged* index. It also said users could manage duration risk through an intercommodity spread with Treasury futures, with margin offsets against interest-rate and equity-index futures (Markets Media, April 29, 2024; FI Desk). For the first time, a cleared, listed contract packaged "credit beta with the rates stripped out" as a product. The ETF version is older: the iShares Interest Rate Hedged High Yield Bond ETF (HYGH) launched May 27, 2014. On October 15–16, 2026 it showed an effective duration near zero and net assets of about \$652mm, a small fraction of HYG's size (ishares.com). *How big.* The market for pre-packaged rate-hedged HY is small relative to the unhedged product. Most investors decline to commit to a hedge ratio in advance, which is the rational response to Table 8.2. Meanwhile the thing being hedged has shrunk. HYG's effective duration of about 3.2 years compares with roughly 4.2–4.8 years for HY in Ben Dor's 2007–2009 sample (p.206), so the spread leg dominates the HY hedge matrix more than ever. *What it means for the desk.* A duration-hedged credit future is a fifth column in the hedge matrix with an $H$ chosen by the index methodology, not by you. Know that methodology before you use it, because its hedge ratio will be wrong in exactly the regimes this chapter catalogs. (Contract codes, sizes, and later contract launches should be checked against CME's own documentation.)

> **Ways This Blows Up.** (1) *The futures–cash basis in a crisis.* In Ben Dor's replication study (Table 14.5, p.386), the tracking error of replicating the US Treasury index with futures rose from 5.0 to 37.5 bp a month in 2008, and the worst monthly error from 12.1 to 87.3 bp. The rates hedge broke in the same month as the credit book. (2) *Roll dates.* CDX rolls on March 20 and September 20 and Treasury futures roll quarterly. An unadjusted continuous series shows jumps that a covariance estimator reads as volatility and a regression reads as beta. Splice rolls on a return basis, never a price basis. (3) *Signs.* Long CDX protection is short credit, and the CDX price rises when spreads tighten. ROBO will get exactly one of these two right unless the schema states both. (4) *ETF basis in stress.* In March 2020, HY ETFs traded at large discounts to NAV (Chapter 20), so a hedge sized on NAV beta was mis-sized in price terms exactly when it mattered.

> **[SOURCE EXTRACTION]** *Ben_Dor p.386:* "TEVs for U.S. Treasury Index and MBS Index replication increased to 37.5 bps and 18.5 bps, respectively. The largest monthly tracking errors increased as well, more than fivefold, to 87.3 bps and 54.3 bps"
>
> **Annotation.** The hedge instruments are not risk-free tools. They are positions with their own crisis behavior. A credit desk's stress test must shock the hedge basis together with spreads, not after them. In 2008 the futures leg lost its tie to cash in the same months that credit spreads exploded, so a "rates-neutral" book was neither. The modern version of the lesson is the condition-number alarm in §8.9: when $\text{cond}(\Sigma_{HH})$ rises, it is often because one instrument has decoupled from its siblings, which is the basis blowing out in real time.

### Deep-Dive Resource Graph

**Podcasts.** *Bloomberg Odd Lots*, episodes on credit ETFs and on the April 2025 Treasury sell-off (show and topic only).

**Practitioner Writing.** Markets Media (April 29, 2024), "CME US credit futures to begin trading on June 17": https://www.marketsmedia.com/cme-us-credit-futures-to-begin-trading-on-june-17 . FI Desk, "CME Group to begin trading credit futures in June": https://www.fi-desk.com/cme-group-to-begin-trading-credit-futures-in-june/ . CME Group, "Understanding Bloomberg credit futures" (2024) and "A practitioner's guide to credit futures" (2026) (title only). Rudin (2025), "Hedging Interest Rate Risk in High-Yield Bonds," in Fabozzi and de Jong (eds.), *Derivatives Applications in Asset Management*, Springer: https://ideas.repec.org/h/spr/sprchp/978-3-031-86354-7_24.html .

**Academic Papers.** Carr and Wu (2011), "A Simple Robust Link Between American Puts and Credit Protection," *Review of Financial Studies* 24(2): https://ideas.repec.org/a/oup/rfinst/v24y2011i2p473-505.html . Kapadia and Pu (2012), "Limited arbitrage between equity and credit markets," *Journal of Financial Economics* 105(3): https://ideas.repec.org/a/eee/jfinec/v105y2012i3p542-564.html .

**Data & Code.** iShares HYG: https://www.ishares.com/us/products/239565/ishares-iboxx-high-yield-corporate-bond-etf . iShares HYGH: https://www.ishares.com/us/products/264544/ishares-interest-rate-hedged-high-yield-bond-etf . SPDR JNK: https://www.ssga.com/us/en/intermediary/etfs/spdr-bloomberg-high-yield-bond-etf-jnk . CME Group (canonical root, Treasury futures specifications): https://www.cmegroup.com . `hedge_matrix`, `hedge_qp`, and `futures_contracts` in §8.9.

## 8.7 Case Studies: Three Times the Hedge Hedged the Wrong Thing

The three episodes below cover all three regimes of §8.2, in four years. Each is told the same way: the levels, the mechanism in terms of $\rho_{y,s}$ and $H$, and the signal a systematic desk would have had in hand.

### Case Study A: 2022, the Year "Negative Duration" Was Positive

*The levels.* The 10-year Treasury yield rose from 1.52% at the end of 2021 to 3.88% at the end of 2022, with a high of 4.25% on October 24. The 2-year rose from 0.73% to 4.41% (FRED). The Bloomberg US Corporate High Yield index returned about −11.2% for the year, the IG Corporate index about −15.8%, and the US Treasury index about −12.5% *(approx.; secondary data summaries)*. The ICE BofA HY OAS went from roughly 310 bp to a peak near 600 bp in early July and ended the year in the high 400s *(approx.; FRED no longer serves 2022 OAS history, see §8.2)*. Apollo's chief economist summarized it on December 3, 2022: the HY total-return index was "down 10% so far in 2022," and his note's title attributed the year's returns mainly to moves in duration.

*The mechanism.* Rates rose because of inflation, and inflation is bad for credit, so spreads widened as yields rose: $\rho_{y,s} > 0$, regime three, $H > 1$. High yield had *more* rate sensitivity than its analytical duration, not less. Consider a desk that had carried a Treasury hedge at $H \approx 0.3$ on the strength of a 1998–2009 table, or no hedge at all because "high yield has negative empirical duration." It ran an unhedged rates position into the worst bond year in decades. With intermediate Treasury yields up roughly 250–370 bp (the 10-year and 2-year moves above), a 4-year-duration book's rate leg alone cost on the order of 10–14 points before carry *(illustrative arithmetic)*. A hedge at 0.3 covered under a third of it.

"In 1994 we hedged B paper by buying the long bond," Mags said. "Lost on both. In 2022 the kids hedged B paper with nothing, because a PDF said empirical duration was negative. Lost on rates and spreads. Progress is losing the same money faster." She looked at Theo's rolling-correlation monitor for a long moment. "That's good, though. I'd have killed for that. I'd have killed for a *screen*."

*The systematic flag.* A rolling 60-day $\rho_{y,s}$ crossing zero from below is a regime alarm, and in 2022 it fired in the first quarter *(the exact date depends on the window; illustrative)*. The response is not "re-estimate $H$ more carefully," because a trailing window lags the regime by construction. The response is a rule: when the rolling $\rho$ is above zero, hedge at least the full analytical duration. Better, hedge rates with futures at $H = 1$ and hedge spread beta separately with CDX, so the hedge stops depending on the correlation at all (§8.8). Theo's lesson for the sticky note: *the empirical hedge ratio is a bet on why rates move.*

### Case Study B: March 2023, SVB, and the Hedge That Hedged Both Ways

*The levels.* The 2-year Treasury yield fell from 5.05% on March 8, 2023 to 4.03% on March 13, a 102 bp drop in three sessions. The 10-year fell from 3.98% to 3.55% (FRED). Credit went the other way. The ICE BofA HY OAS widened 42 bp in a single day, from 461 bp on Friday, March 10 to 503 bp on Monday, March 13, the largest daily widening since June 2020 (Reuters, via Kitco, March 14, 2023).

*The mechanism.* A flight to quality: $\rho_{y,s}$ sharply negative for a week, regime one, the world Ben Dor's sample was built on, arriving exactly one year after the regime that broke it. Take a B book with duration 4 *(illustrative)*, intermediate yields down about 70 bp, and spreads out about 60 bp over the window. The bond gains roughly $4 \times 0.70\% = 2.8\%$ on rates and loses $4 \times 0.60\% = 2.4\%$ on spread, for a net of about +0.4%. A full analytical futures short loses 2.8%, so the "hedged" book is down about 2.4%. Hedged at $H = 0.3$, the futures lose only 0.84%, and the book is down about 0.4%. The full hedge was not a hedge. It was a short-rates position with a credit position attached, entered the week a bank failure became the only macro variable that mattered.

*The systematic flag.* The week's realized $\rho$ was strongly negative while the trailing 60-day $\rho$ still carried 2022's positive memory, so the two estimates disagreed sharply. That disagreement is the signal. It says the *source* of rate moves has changed: from inflation, which hurts both legs, to flight to quality, which helps the rates leg and hurts the spread leg. Conditioning the hedge ratio on the source of the rate move is a classification problem, not a regression problem, and Chapter 10 (trend) and Chapter 12 (regimes) supply the classifiers.

### Case Study C: April 2025, Three Regimes in Seven Sessions

*The levels* (FRED, closing OAS and yields; CCMG for the monthly path):

| Date (2025) | 10-year | HY OAS | BB | B | CCC | IG | What the hedge did |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | :--- |
| Apr 2 | 4.20% | 342 | 212 | 353 | 925 | 96 | (baseline, before the tariff announcement) |
| Apr 4 | 4.01% | 445 | n/r | n/r | n/r | n/r | Rally plus widening: $\rho < 0$. The futures short loses into the widening; a full hedge forfeits the rally's cushion |
| Apr 7 | 4.15% | 461 | 306 | 486 | 1,137 | 120 | Sell-off plus widening: $\rho > 0$. Under-hedged book loses on both legs |
| Apr 11 | 4.48% | 426 | n/r | n/r | n/r | n/r | Sell-off plus tightening: $\rho < 0$ again |
| Apr 30 | 4.17% | 394 | n/r | n/r | n/r | n/r | Month: Treasuries +0.63%, HY −0.02% |

*Table 8.3. April 2025 (FRED ICE BofA OAS in bp and DGS10; "n/r" = not recorded in our extract; monthly index returns from CCMG's April 2025 recap).*

The month's summary statistics hide the week. For April as a whole, CCMG reports Bloomberg index returns of +0.63% for Treasuries, +0.06% for US Credit, −0.02% for High Yield, and −0.68% for the S&P 500. Victory Capital reports month-over-month widening of 13 bp in IG and 39 bp in HY. GW&K noted that the range in the 10-year yield that month was the widest since March 2023, "when Silicon Valley Bank folded." Inside that range, the sign of the rate–spread comovement flipped twice in seven sessions. A book hedged at a trailing-window $H$ was wrong on the first two days, right on the next one, and wrong again by the end of the week, in different directions.

Ines replayed it as a hand history. "April 2 to 4, you had the nuts. Rates rallied, spreads gapped, and your under-hedge paid because you weren't short futures into the rally. April 7, the board paired: Treasuries sold off *with* credit, and you were still betting day-one odds. By April 11 the board changed again. Your hedge ratio is your read on the table. Update it when the board changes, not when the month ends."

*The indictment of trailing windows.* The rolling 60-day CCC hedge ratio computed on FRED data was close to zero in the window ending April 30 and reached −0.66 by the window ending May 30 (and −0.78 for the window ending May 23). The *estimate* swung hard negative *after* the event, which is exactly when it was least useful. Rudin (2025), using the Bloomberg US Corporate High Yield index, makes the general point: hedging high yield with Treasury futures based on duration "often leads to increased portfolio volatility."

*The systematic flag.* When the realized one-week $\rho$ changes sign within the week, the right response is to cut confidence in the hedge ratio, not to re-estimate harder. Operationally, raise the ridge penalty $\eta$ (shrinking the hedge toward a robust prior), widen the band within which the hedge is left alone, and lean on the instrument that hedges the spread factor directly (CDX HY) rather than the instrument that hedges it through a correlation (futures at $H < 1$).

## 8.8 What's Left Is IDO (and How to Prove It)

After the Treasury leg, the empirical rate beta, and the DTS-scaled market spread factor, the residual still is not idiosyncratic. Collin-Dufresne, Goldstein and Martin (2001) regressed credit spread changes on the variables structural models say should matter (leverage, volatility, rates, the slope of the curve) and found "rather limited explanatory power." Worse for anyone hoping for a clean residual, the unexplained part was "mostly driven by a single common factor." There is a market-wide spread shock the theory variables do not see: liquidity, risk appetite, dealer balance sheets, flows. If you call that residual IDO, you will discover in the next drawdown that every one of your "idiosyncratic" positions shared it.

### The definition, in four subtractions

Let $\text{DTS}_{i,t-1}$ be bond $i$'s DTS at the previous close, known before the return occurs, so the definition cannot look ahead. The pure-IDO return is defined by four subtractions:

1. **Rates.** Excess return over KRD-matched Treasuries, $R^{\text{xs}}_{i,t} = R^{\text{tot}}_{i,t} - \sum_k w_{i,k}R^{\text{TSY}}_{k,t}$ (§8.1). This removes the full analytical rate exposure. The part of the spread move that is correlated with rates stays in $R^{\text{xs}}$, and the market spread factor in the next step removes it, whatever $\rho$ happens to be.
2. **Market, sector and rating spread factors, DTS-scaled.** Regress $R^{\text{xs}}_{i,t}/\text{DTS}_{i,t-1}$ on factor returns $F_{k,t}$ with Dimson-summed loadings for stale marks (§8.5):
$$
\frac{R^{\text{xs}}_{i,t}}{\text{DTS}_{i,t-1}} = \sum_{k} \beta^{\text{D}}_{i,k}\,F_{k,t} + \tilde\epsilon_{i,t} .
$$
3. **The common residual factor.** Take the panel of scaled residuals $\tilde\epsilon$ (time by bonds), extract its leading principal component $g_t$ with loadings $v_i$, and remove it: $\tilde\epsilon^{\perp}_{i,t} = \tilde\epsilon_{i,t} - v_i\,g_t$. This is the Collin-Dufresne–Goldstein–Martin factor, estimated rather than named.
4. **Scale back to returns.**
$$
\text{IDO}_{i,t} \equiv \text{DTS}_{i,t-1}\,\tilde\epsilon^{\perp}_{i,t} .
$$

What remains is small, noisy, and yours. That is not a disappointment. That is the definition.

### Theo's thirty-seven cents, answered

Run the cold-open bond through the four subtractions with *illustrative* market data for the day: the B-rated index's relative spread change was −1.2%, and the bond's own was $-9/620 = -1.45\%$. With $\text{DTS} = 4.0 \times 0.062 = 0.248$:

| Component | Calculation | Cents on \$95 |
| :--- | :--- | ---: |
| Carry | §8.1 | +3 |
| Rates (analytical) | $-4.1 \times 0.0018$ | −70 |
| Market spread beta | $-0.248 \times (-0.012)$ | +28 |
| Bond-specific spread (IDO) | $-0.248 \times (-0.0145 + 0.012)$ | +6 |
| Decomposition residual | plug (probably tomorrow's stale-price catch-up) | −4 |
| **Total** | | **−37** |

Of the thirty-seven cents, about six were the bond. Four were the pricing service, and they will probably reverse tomorrow (§8.5). The rest was the Treasury market and everyone else's opinion of the economy. Kaz's "alpha" of 34 cents was 28 cents of beta and 6 cents of alpha. Theo peeled the sticky note off his monitor and wrote "6" on it.

The table also shows the cleanest version of the hedge. The empirical-duration approach hedges the 28 cents of market spread beta *indirectly*: it shorts fewer futures because, on average, spreads tighten when yields rise. That works while $\rho$ holds and fails when it flips (§8.7). The two-instrument approach hedges each factor with its own instrument: futures at $H = 1$ for the 70 cents of rates, and CDX HY sized at $\text{DTS}_i/\text{DTS}_{\text{CDX}}$ for the 28 cents of spread beta. It does not depend on $\rho$ at all. It pays for that robustness with the CDX–cash basis and the index roll, and it hedges away spread beta you might have wanted to keep, which is Ines's poker hand from §8.2. Which hedge is right depends on what Theo is paid for. If his mandate is IDO, the answer is the two-instrument hedge, because a view on $\rho$ is not his job.

> **[SOURCE EXTRACTION]** *Ben_Dor p.220:* "the low explanatory power (R2 = 8%) suggests that there are other factors that influence the performance of the strategy."
>
> **Annotation.** Ben Dor tests a DTS-neutral "short empirical duration" strategy (long Ba, short Baa) and finds a significant loading on rates (0.39, $t = 3.86$) that explains only 8% of its return variance. That is a pattern to recognize. A strategy can have a real, statistically significant factor exposure that is economically small next to its residual. The IDO ledger reports both: the loading's $t$-statistic (is the exposure real?) and the factor's share of variance (does it matter?). A residual that is 92% of variance is either a great deal of alpha or a great deal of factor you have not named yet. The ledger's job is to tell those apart.

### The IDO ledger: proving it

A residual is a claim until a signal predicts it. The ledger keeps three numbers per strategy, per month:

- **Residual volatility**, $\sigma(\text{IDO})$ for the portfolio. This is the risk budget the strategy actually consumes after the hedges, and the number to compare with the risk model's forecast.
- **Information coefficient.** The cross-sectional Spearman rank correlation between the signal at $t-1$ and $\text{IDO}_{i,t}$, $\text{IC}_t$, averaged over months. Rank correlation, because credit residuals have fat tails and one defaulting CCC should not decide the month.
- **Its $t$-statistic**, $t = \overline{\text{IC}}\,\sqrt{T}/\mathrm{sd}(\text{IC}_t)$ over $T$ months. Chapter 7's warning applies: a $t$ of 2 after forty specification searches is not a $t$ of 2.

The fundamental law, $\text{IR} \approx \text{IC}\sqrt{\text{BR}}$ (Chapter 9), connects the ledger to the PM's question. If the IC is measured on raw excess returns, the IR it implies is partly a beta IR, and it disappears in the first regime change. If it is measured on IDO, it is the desk's. IDO or it didn't happen.

## 8.9 The IDO Engine: A Reference Implementation

### Specification for AI Implementation

**What ROBO built from the vague version.** Asked to "hedge the rates," ROBO sold analytical-duration TY futures against a B/CCC book and reported, accurately, that the hedged P&L was more volatile than the unhedged one, which is Rudin's (2025) finding reproduced by accident. Asked to "minimize hedged variance with HYG," ROBO sold \$38mm of HYG against \$40mm of bonds and delivered a pleasant, alpha-free flat line. Both outputs were correct implementations of bad specs. The spec below names the objective, the instruments, the units, and the failure modes.

**Module.** `ido_engine.py`, numpy and scipy only, `float64` throughout, seeded with `np.random.default_rng(8)`.

**Schemas.**

- `bond_returns: (T, N)` daily total returns, decimal. `oas: (T, N)` decimal, strictly positive where relative changes are used. `dur_mod, dur_spr: (T, N)` years. All aligned to one trading calendar.
- `factors: (T, K)` factor returns. `hedge_returns: (T, m)` per 1 unit of notional for each instrument, with the sign convention "long risk" (CDX quoted long risk, futures long, ETF long, puts long).
- Every column carries a `close_time` attribute. If two columns' close times differ by more than 30 minutes, the engine warns and uses Dimson-summed covariances (§8.6).
- Missing marks are `NaN`. Never forward-fill a price into a return: compute returns only between actual marks and record the gap length.
- Output `h: (m,)` is the notional of each instrument to **short** per 1 unit of target notional. Unit conversion is a separate, explicit step (`futures_contracts`, `etf_shares`).

**Hedge objective (required field, no default).** One of `"min_total_variance"`, `"zero_rates_keep_spread"`, or `"zero_rates_zero_spread"`. ROBO refuses to run without it.

**Guards.** $|\Delta y| < 0.05$ per day, else raise (unit error). `oas > 0` before relative changes. Refuse more than 5 Dimson lags. Raise on a non-invertible smoothing polynomial. Alarm when $\text{cond}(C) > 10^3$ on the instrument correlation matrix. Cap $\text{cond}(C + \eta I)$ at 50 by default. Check `abs(h).sum()` against a gross budget.

**Sanity checks (built in, printed PASS/FAIL).** The decomposition foots to $10^{-10}$. Regression $H$ matches the closed form. OLS beta on stale data is attenuated to $\theta_0$, Dimson recovers it, and the stale volatility ratio is $\sqrt{\sum\theta_k^2}$. DTS equivalence and zero carry hold. Ridge caps the condition number, hedges out of sample, and produces stable weights. The single-proxy hedge is less than naive. Futures sizing matches §8.6. The common residual factor is stripped, and the ledger recovers a planted IC.

The blocks below run in order in one interpreter.

```python
# ---------- 0. Setup: one seeded generator, one scoreboard ----------
import numpy as np
from scipy import optimize, stats

RNG = np.random.default_rng(8)
CHECKS = {}


def report(name, ok, detail=""):
    CHECKS[name] = bool(ok)
    print(f"{'PASS' if ok else 'FAIL'}  {name:<40s} {detail}")
```

```python
# ---------- 1. Return decomposition with the right signs (Section 8.1) ----------
def decompose_returns(total_ret, y, s, dy_tsy, ds, D_mod, D_spr, convexity, dt):
    """Split realized total returns into carry, rates, spread, convexity and residual.

    Shapes: every argument is a float scalar or an array of shape (T,).
    Units: y, s, dy_tsy, ds in DECIMAL (0.0018 = 18 bp); durations in years;
    convexity in years^2; dt in years under the bond's day count (30/360).
    carry_oas is reported for excess-return work but is NOT part of the total-return sum.
    """
    total_ret, y, s, dy_tsy, ds = (np.asarray(a, dtype=float) for a in (total_ret, y, s, dy_tsy, ds))
    if np.any(np.abs(dy_tsy) > 0.05) or np.any(np.abs(ds) > 0.05):
        raise ValueError("a daily move above 500 bp: inputs are probably in bp, not decimal")
    parts = {
        "carry_yield": y * dt,
        "rates_pnl": -D_mod * dy_tsy,            # the minus sign ROBO forgets
        "spread_pnl": -D_spr * ds,
        "convexity_pnl": 0.5 * convexity * (dy_tsy + ds) ** 2,
    }
    parts["residual"] = total_ret - sum(parts.values())
    parts["carry_oas"] = s * dt
    recon = sum(parts[k] for k in ("carry_yield", "rates_pnl", "spread_pnl", "convexity_pnl", "residual"))
    assert np.allclose(recon, total_ret, atol=1e-10, rtol=0.0), "decomposition does not foot"
    return parts


# The cold-open bond (illustrative inputs from Section 8.1)
cold = decompose_returns(total_ret=-0.0039, y=0.111, s=0.062, dy_tsy=0.0018, ds=-0.0009,
                         D_mod=4.1, D_spr=4.0, convexity=20.0, dt=1.0 / 360.0)
cents = {k: 95.0 * 100.0 * float(v) for k, v in cold.items()}      # cents on a 95-dollar price
report("8.1 decomposition foots",
       abs(cents["rates_pnl"] + 70.1) < 0.5 and abs(cents["residual"] + 4.1) < 0.5,
       f"rates {cents['rates_pnl']:.1f}c, spread {cents['spread_pnl']:.1f}c, resid {cents['residual']:.1f}c")
```

```python
# ---------- 2. Empirical duration: regression and closed form (Section 8.2) ----------
def empirical_duration(R, dy, D, s):
    """Pooled no-intercept OLS of R on [-D*dy, -D*s*dy]; H(s) = beta + gamma*s.

    R, dy, D, s: 1-D float arrays of equal length (stack bonds and days).
    Returns (beta, gamma, H) where H maps a spread grid (decimal) to hedge ratios.
    """
    R, dy, D, s = (np.asarray(a, dtype=float).ravel() for a in (R, dy, D, s))
    X = np.column_stack([-D * dy, -D * s * dy])
    (beta, gamma), *_ = np.linalg.lstsq(X, R, rcond=None)
    return float(beta), float(gamma), (lambda grid: beta + gamma * np.asarray(grid, dtype=float))


def h_closed_form(s, rel_ds, dy):
    """H = 1 + s * rho * sig_s / sig_y from sample moments (Ben Dor's two-factor result)."""
    c = np.cov(rel_ds, dy)
    rho = c[0, 1] / np.sqrt(c[0, 0] * c[1, 1])
    return 1.0 + np.asarray(s, dtype=float) * rho * np.sqrt(c[0, 0] / c[1, 1])


T = 2500
SIG_Y, SIG_S, RHO = 0.0006, 0.02, -0.4          # 6 bp/day yield vol; 2%/day relative-spread vol
D_BOND, S_BOND = 4.0, 0.06
LINK = RHO * SIG_S / SIG_Y                       # linkage factor: -13.3 per unit of decimal spread
dy = SIG_Y * RNG.standard_normal(T)
x = LINK * dy + SIG_S * np.sqrt(1.0 - RHO ** 2) * RNG.standard_normal(T)   # relative spread change
S_LEVELS = np.array([0.01, 0.03, 0.06, 0.09])
R_panel = np.stack([-D_BOND * dy - D_BOND * sl * x + 0.0005 * RNG.standard_normal(T) for sl in S_LEVELS])

beta_hat, gamma_hat, H_of = empirical_duration(
    R_panel.ravel(), np.tile(dy, len(S_LEVELS)), np.full(R_panel.size, D_BOND), np.repeat(S_LEVELS, T))
H_true = 1.0 + S_BOND * LINK                     # = 0.20
H_reg, H_cf = float(H_of(S_BOND)), float(h_closed_form(S_BOND, x, dy))
report("8.2 regression H matches closed form",
       abs(H_reg - H_cf) < 0.05 and abs(beta_hat - 1.0) < 0.05,
       f"H_reg {H_reg:.3f}, H_closed {H_cf:.3f}, beta {beta_hat:.3f}")
report("8.2 H near population value", abs(H_reg - H_true) < 0.15, f"H_true {H_true:.2f}")
```

```python
# ---------- 3. Stale-price betas: Dimson, Scholes-Williams, de-smoothing (Section 8.5) ----------
def lagged(f, k):
    """out[t] = f[t-k], NaN where undefined. k > 0 is a lag, k < 0 a lead."""
    f = np.asarray(f, dtype=float)
    out = np.full(f.shape, np.nan)
    if k >= 0:
        out[k:] = f[:len(f) - k]
    else:
        out[:k] = f[-k:]
    return out


def ols_slope(yv, xv):
    ok = ~(np.isnan(xv) | np.isnan(yv))
    xc, yc = xv[ok] - xv[ok].mean(), yv[ok] - yv[ok].mean()
    return float(xc @ yc / (xc @ xc))


def dimson_beta(r_obs, f, lags=2, leads=0):
    """Sum of slopes from ONE regression of r_obs[t] on f[t+leads], ..., f[t-lags] (Dimson 1979)."""
    if lags > 5 or leads > 5:
        raise ValueError("refusing more than 5 lags or leads: estimation noise dominates the sum")
    r_obs = np.asarray(r_obs, dtype=float)
    ks = list(range(-leads, lags + 1))
    X = np.column_stack([np.ones(len(f))] + [lagged(f, k) for k in ks])
    ok = ~np.isnan(X).any(axis=1) & ~np.isnan(r_obs)
    coef, *_ = np.linalg.lstsq(X[ok], r_obs[ok], rcond=None)
    b = dict(zip(ks, coef[1:]))
    return float(sum(b.values())), b


def scholes_williams_beta(r_obs, f):
    """(b_lead + b_0 + b_lag) / (1 + 2 rho_f), each slope from its own univariate regression."""
    b = [ols_slope(r_obs, lagged(f, k)) for k in (-1, 0, 1)]
    rho_f = np.corrcoef(f[1:], f[:-1])[0, 1]
    return float(sum(b) / (1.0 + 2.0 * rho_f))


def desmooth(r_obs, theta):
    """Invert r_obs[t] = sum_k theta[k] * r[t-k] recursively; theta must be invertible."""
    theta = np.asarray(theta, dtype=float)
    if np.any(np.abs(np.roots(theta[::-1])) <= 1.0):
        raise ValueError("MA polynomial not invertible: the de-smoothed series would explode")
    q = len(theta) - 1
    r_hat = np.array(r_obs, dtype=float)
    for t in range(q, len(r_hat)):
        r_hat[t] = (r_obs[t] - theta[1:] @ r_hat[t - q:t][::-1]) / theta[0]
    return r_hat


DTS_BOND = D_BOND * S_BOND                       # 0.24
THETA = np.array([0.5, 0.3, 0.2])                # 50% of news priced today, 30% tomorrow, 20% the day after
r_true = -D_BOND * dy - DTS_BOND * x + 0.0005 * RNG.standard_normal(T)
r_obs = np.convolve(r_true, THETA)[:T]           # r_obs[t] = sum_k THETA[k] * r_true[t-k]
burn = slice(10, None)
beta_true = ols_slope(r_true[burn], x[burn])
beta_ols = ols_slope(r_obs[burn], x[burn])
beta_dim, b_lags = dimson_beta(r_obs[burn], x[burn], lags=2)
beta_sw = scholes_williams_beta(r_obs[burn], x[burn])
vol_ratio = r_obs[burn].std() / r_true[burn].std()
report("8.5 OLS beta attenuated to theta_0", abs(beta_ols / beta_true - THETA[0]) < 0.05,
       f"OLS/true {beta_ols / beta_true:.3f}")
report("8.5 Dimson(2) recovers beta", abs(beta_dim / beta_true - 1.0) < 0.10,
       f"Dimson/true {beta_dim / beta_true:.3f}")
report("8.5 Scholes-Williams catches one lag", 0.70 < beta_sw / beta_true < 0.90,
       f"SW/true {beta_sw / beta_true:.3f}")
report("8.5 stale vol ratio", abs(vol_ratio - np.sqrt(np.sum(THETA ** 2))) < 0.03,
       f"{vol_ratio:.3f} vs {np.sqrt(np.sum(THETA ** 2)):.3f}")

theta_hat = np.array([b_lags[k] for k in range(3)]) / beta_dim
r_hat = desmooth(r_obs, theta_hat)
tail = slice(50, None)
vr = r_hat[tail].std() / r_true[tail].std()
report("8.5 de-smoothing restores vol",
       abs(vr - 1.0) < 0.10 and np.corrcoef(r_hat[tail], r_true[tail])[0, 1] > 0.9,
       f"vol ratio {vr:.3f}, theta_hat {np.round(theta_hat, 3)}")
```

```python
# ---------- 4. DTS: the unit of credit beta (Section 8.4) ----------
def dts(D_spr, oas):
    oas = np.asarray(oas, dtype=float)
    if np.any(oas <= 0.0):
        raise ValueError("non-positive OAS: use absolute spread changes for these bonds, with a warning")
    return np.asarray(D_spr, dtype=float) * oas


def dts_scale(xs_returns, dts_lag):
    """Excess return per unit of previous-close DTS (approximately minus the relative spread change)."""
    return np.asarray(xs_returns, dtype=float) / np.asarray(dts_lag, dtype=float)


def dts_pair_hedge(dts_long, dts_short):
    """Notional of the short bond per 1 unit of long notional that zeroes net DTS."""
    return float(dts_long / dts_short)


h_pair = dts_pair_hedge(dts(2.0, 0.02), dts(4.0, 0.01))        # 200 bp x 2y vs 100 bp x 4y
h_carry = dts_pair_hedge(dts(5.0, 0.03), dts(5.0, 0.015))      # equal durations, 300 vs 150 bp
report("8.4 DTS equivalence and zero carry",
       np.isclose(h_pair, 1.0) and np.isclose(0.03 - h_carry * 0.015, 0.0),
       f"pair hedge {h_pair:.2f}, carry-pair hedge {h_carry:.2f}")

# Beta to the market equals the DTS ratio when relative spread shocks are common.
x_m = SIG_S * RNG.standard_normal(T)
dts_cs = np.array([0.05, 0.12, 0.24, 0.40])
xs_cs = -dts_cs[:, None] * (x_m[None, :] + 0.005 * RNG.standard_normal((4, T)))
xs_mkt = xs_cs.mean(axis=0)
beta_cs = np.array([ols_slope(xs_cs[i], xs_mkt) for i in range(4)])
report("8.4 beta equals DTS ratio", np.allclose(beta_cs, dts_cs / dts_cs.mean(), rtol=0.10),
       f"betas {np.round(beta_cs, 2)} vs {np.round(dts_cs / dts_cs.mean(), 2)}")
```

```python
# ---------- 5. The hedge matrix: min-variance, ridge, bounds, units (Section 8.6) ----------
def cond_number(M):
    w = np.linalg.eigvalsh(M)
    return float(w.max() / max(w.min(), 1e-300))


def eta_for_condition(C, cond_max=50.0):
    """Smallest ridge penalty capping cond(C + eta I) at cond_max (C a correlation matrix)."""
    w = np.linalg.eigvalsh(C)
    return max(0.0, float((w.max() - cond_max * w.min()) / (cond_max - 1.0)))


def _moments(r_p, R_H):
    S = np.cov(np.column_stack([R_H, r_p]), rowvar=False)
    return S[:-1, :-1], S[:-1, -1]


def hedge_matrix(r_p, R_H, eta=None, cond_max=50.0):
    """Variance-scaled ridge hedge. r_p: (T,), R_H: (T, m), returns per 1 unit of notional.

    Returns h (notional of each instrument to SHORT per unit of target), in-sample residual
    variance, cond(C) before and after regularization, and the penalty eta used.
    """
    r_p, R_H = np.asarray(r_p, dtype=float), np.asarray(R_H, dtype=float)
    S_HH, S_Hp = _moments(r_p, R_H)
    sd = np.sqrt(np.diag(S_HH))
    C = S_HH / np.outer(sd, sd)
    if eta is None:
        eta = eta_for_condition(C, cond_max)
    h = np.linalg.solve(S_HH + eta * np.diag(np.diag(S_HH)), S_Hp)
    resid_var = float(np.var(r_p - R_H @ h, ddof=1))
    return h, resid_var, cond_number(C), cond_number(C + eta * np.eye(len(sd))), eta


def hedge_qp(r_p, R_H, bounds, eta=0.0):
    """Ridge hedge with per-instrument bounds [(lo, hi), ...], solved by L-BFGS-B."""
    S_HH, S_Hp = _moments(np.asarray(r_p, dtype=float), np.asarray(R_H, dtype=float))
    A = S_HH + eta * np.diag(np.diag(S_HH))
    k = 1.0 / np.mean(np.diag(A))                # rescale so the optimizer sees O(1) numbers
    res = optimize.minimize(lambda h: k * (h @ A @ h - 2.0 * h @ S_Hp), np.zeros(len(S_Hp)),
                            jac=lambda h: k * (2.0 * A @ h - 2.0 * S_Hp),
                            bounds=bounds, method="L-BFGS-B")
    return res.x


def futures_contracts(dv01_target, dv01_ctd_per_contract, conv_factor, hedge_ratio=1.0):
    """N = H * DV01_target / (DV01_CTD / CF)."""
    return hedge_ratio * dv01_target / (dv01_ctd_per_contract / conv_factor)


def etf_shares(h, target_notional, etf_price):
    return h * target_notional / etf_price


# Four instruments plus a near-copy (JNK ~ HYG), all built from the same rate and spread factors.
dyH = SIG_Y * RNG.standard_normal(T)
xH = LINK * dyH + SIG_S * np.sqrt(1.0 - RHO ** 2) * RNG.standard_normal(T)


def noise(sd):
    return sd * RNG.standard_normal(T)


cdx = -0.14 * xH + noise(0.0005)                 # CDX HY, long risk: ~RPV01 4 x spread 3.5%
ty = -6.5 * dyH + noise(0.0001)                  # TY future, per unit of face
hyg = -3.2 * dyH - 0.11 * xH + noise(0.0012)     # HYG: rates + spread beta + NAV basis
put = 0.30 * xH + noise(0.004)                   # equity put proxy: gains when spreads widen
jnk = hyg + noise(0.000002)                      # the collinearity trap
R_H = np.column_stack([cdx, ty, hyg, put, jnk])
r_book = -D_BOND * dyH - DTS_BOND * xH + noise(0.003)   # B book with 30 bp/day of IDO

tr, te = slice(0, 2000), slice(2000, None)
h_ols, _, cond_raw, _, _ = hedge_matrix(r_book[tr], R_H[tr], eta=0.0)
h_rdg, _, _, cond_rdg, eta = hedge_matrix(r_book[tr], R_H[tr])


def oos(h):
    return float(np.var(r_book[te] - R_H[te] @ h, ddof=1))


v_un, v_ols, v_rdg = float(np.var(r_book[te], ddof=1)), oos(h_ols), oos(h_rdg)
report("8.6 collinearity detected and capped", cond_raw > 1e3 and cond_rdg <= 50.0 * (1 + 1e-6),
       f"cond {cond_raw:.1e} -> {cond_rdg:.1f}, eta {eta:.3f}")
report("8.6 ridge hedges out of sample", v_rdg < 0.6 * v_un and v_rdg <= 1.15 * v_ols,
       f"vs unhedged {v_rdg / v_un:.2f}, vs OLS {v_rdg / v_ols:.3f}")

half_a, half_b = slice(0, 1000), slice(1000, 2000)


def drift(e):
    ha = hedge_matrix(r_book[half_a], R_H[half_a], eta=e)[0]
    hb = hedge_matrix(r_book[half_b], R_H[half_b], eta=e)[0]
    return float(np.linalg.norm(ha - hb))


report("8.6 ridge weights are stable", drift(eta) < drift(0.0),
       f"weight drift ridge {drift(eta):.2f} vs OLS {drift(0.0):.2f}")

# Paleologo's attenuation: one noisy proxy, so hedge less than the naive amount.
f_true = 0.01 * RNG.standard_normal(T)
proxy = f_true + 0.01 * RNG.standard_normal(T)   # omega^2 = sigma_f^2, so attenuation is one half
target = 0.8 * f_true + 0.005 * RNG.standard_normal(T)
h_star = hedge_matrix(target, proxy[:, None], eta=0.0)[0][0]
report("8.6 hedge less than naive",
       abs(h_star - 0.4) < 0.05 and np.var(target - h_star * proxy) < np.var(target - 0.8 * proxy),
       f"h* {h_star:.3f} vs naive 0.8")

bounds = [(0.0, 1.0), (-1.0, 1.0), (-0.5, 0.5), (-0.5, 0.0), (-0.5, 0.5)]   # liquidity and mandate limits
h_box = hedge_qp(r_book[tr], R_H[tr], bounds, eta=eta)
inside = all(lo - 1e-9 <= hb <= hi + 1e-9 for hb, (lo, hi) in zip(h_box, bounds))
report("8.6 bounded hedge respects limits", inside and oos(h_box) < 0.8 * v_un,
       f"h_box {np.round(h_box, 2)}")

dv01_bond = 40e6 * 4.1 * 1e-4                    # the cold-open bond: 16,400 per bp
n_full = futures_contracts(dv01_bond, 63.0, 0.89)
n_emp = futures_contracts(dv01_bond, 63.0, 0.89, hedge_ratio=0.73)
report("8.6 futures sizing matches Table 8.2", round(n_full) == 232 and round(n_emp) == 169,
       f"{n_full:.1f} and {n_emp:.1f} TY contracts")
```

```python
# ---------- 6. Common residual factor and the IDO ledger (Section 8.8) ----------
def strip_common_factor(eps_scaled, n_pc=1):
    """Remove the leading principal components from a (T, N) panel of DTS-scaled residuals."""
    X = np.asarray(eps_scaled, dtype=float)
    X = X - X.mean(axis=0)
    U, sv, Vt = np.linalg.svd(X, full_matrices=False)
    share = sv ** 2 / np.sum(sv ** 2)
    return X - (U[:, :n_pc] * sv[:n_pc]) @ Vt[:n_pc], share


def ido_ledger(ido, signal, min_names=10):
    """ido, signal: (T, N). signal[t] must be known before ido[t] is realized."""
    ics = []
    for t in range(ido.shape[0]):
        ok = ~(np.isnan(ido[t]) | np.isnan(signal[t]))
        if ok.sum() >= min_names:
            ics.append(stats.spearmanr(signal[t, ok], ido[t, ok])[0])
    ics = np.asarray(ics)
    return {"resid_vol": float(np.nanstd(ido)), "ic_mean": float(ics.mean()),
            "ic_t": float(ics.mean() * np.sqrt(len(ics)) / ics.std(ddof=1)), "months": len(ics)}


TM, NB = 60, 200
g = 0.02 * RNG.standard_normal(TM)                               # the CDGM common residual factor
eps_scaled = np.outer(g, RNG.uniform(0.5, 1.5, NB)) + 0.03 * RNG.standard_normal((TM, NB))
clean, share_before = strip_common_factor(eps_scaled)
_, share_after = strip_common_factor(clean)
ido = clean * RNG.uniform(0.05, 0.40, NB)[None, :]              # back to returns with each bond's DTS
signal = 0.15 * ido / ido.std() + RNG.standard_normal((TM, NB))  # a planted, modest edge
ledger = ido_ledger(ido, signal)
report("8.8 common residual factor stripped", share_before[0] > 0.2 and share_after[0] < 0.1,
       f"PC1 share {share_before[0]:.2f} -> {share_after[0]:.2f}")
report("8.8 IDO ledger finds the planted IC", ledger["ic_mean"] > 0.05 and ledger["ic_t"] > 3.0,
       f"IC {ledger['ic_mean']:.3f}, t {ledger['ic_t']:.1f} over {ledger['months']} months")

print(f"\n{sum(CHECKS.values())}/{len(CHECKS)} checks passed")
assert all(CHECKS.values()), [k for k, v in CHECKS.items() if not v]
```

> **Ways This Blows Up.** The simulation is kinder than the market in three ways. Its rate–spread correlation is constant, so the trailing-window problem of §8.7 never appears; rerun section 2 with $\rho$ switching sign halfway through and watch the regression $H$ average two regimes into a hedge ratio that fits neither. Its smoothing weights are the same for every bond, while real weights differ by price source and liquidity bucket. And its instruments have no roll dates, so the jumps in real CDX and futures series never reach the covariance matrix. Each is an exercise below.

## 8.10 Desk Debrief

- **IDO or it didn't happen, in two subtractions.** First accounting (carry, KRD-matched Treasuries, convexity), then attribution (DTS-scaled factors, then the common residual factor). The P&L-explain residual is a bookkeeping error, not alpha.
- **Analytical duration answers a question nobody asked.** $H = 1 + s\,\rho_{y,s}\,\sigma_s/\sigma_y$. The sign of $\rho$ decides everything, and it has changed sign twice since 2021.
- **There are two roads to zero duration.** The correlation road is a regime. The recovery road, $H^{\text{rec}} = c/(c + \lambda R)$, is structural. CCC books travel both.
- **The IG/HY line is a quoting convention you can measure.** Baa at 700 bp hedges at 0.71; HY at 700 bp hedges at zero. Re-bucket the hedge ratio on the day of a downgrade across the line.
- **DTS is the unit of credit beta.** $\beta_i = \text{DTS}_i/\text{DTS}_M$. DTS-neutral pairs carry nothing, so what they earn is IDO.
- **Stale marks shrink betas to $\theta_0\beta$ and volatility to $\sqrt{\sum\theta_k^2}$.** Dimson-sum rates and credit factors. Treat lagged equity coefficients as a signal to test, not a correction to apply.
- **The hedge you want and the hedge you can trade are different matrices.** Cap the condition number, shrink, hedge less than naive, and if your mandate is IDO, hedge each factor with its own instrument instead of through a correlation.
- **The empirical hedge ratio is a bet on why rates move.** When this week's $\rho$ disagrees with the trailing window, cut confidence in the hedge. Do not re-estimate harder.

### The Spec You Hand the Robot

```text
TASK: Build ido_engine.py (numpy/scipy only, float64, seed np.random.default_rng(8)).
INPUTS: bond_returns (T,N) daily total returns, decimal; oas (T,N) decimal > 0; dur_mod, dur_spr (T,N) years;
        factors (T,K); hedge_returns (T,m) per unit notional, "long risk" sign convention; close_time per column.
        Missing marks are NaN. Never forward-fill prices into returns.
OBJECTIVE (required, no default): one of min_total_variance | zero_rates_keep_spread | zero_rates_zero_spread.
COMPUTE, in order:
 1. decompose_returns: carry, -D_mod*dy, -D_spr*ds, 0.5*C*(dy+ds)^2, residual; assert it foots to 1e-10.
 2. empirical_duration: pooled OLS of R on [-D*dy, -D*s*dy] by rating bucket; H(s) = beta + gamma*s,
    clipped at -0.5; re-estimate monthly; re-bucket H on the day of a rating change across Baa3/Ba1.
 3. Dimson betas (lags <= 3 daily) on rate and credit-index factors; equity lags reported, never auto-applied.
 4. DTS-scale excess returns by previous-close DTS before any covariance or PCA.
 5. hedge_matrix: variance-scaled ridge, eta chosen so cond(C + eta I) <= 50; Dimson-summed covariances if
    close times differ by > 30 min; bounded QP when limits are given; output h = notional to SHORT per unit.
 6. Units: TY contracts = H * DV01_target / (DV01_CTD / CF); CDX notional = h * target; ETF shares = h * notional / price.
 7. IDO = DTS_{t-1} * (scaled residual minus first principal component). Ledger: residual vol, monthly Spearman IC
    of the signal at t-1 against IDO at t, and its t-stat.
GUARDS: |dy| < 0.05/day; oas > 0 before relative changes; refuse lags > 5; raise on a non-invertible smoothing
        polynomial; alarm if cond(C) > 1e3; alarm when the 60-day rolling rho(dy, ds/s) changes sign.
TESTS: every sanity check in Section 8.9 prints PASS. Do not "improve" the objective. Ask if anything is ambiguous.
```

### Exercises

1. **Theo's thirty-seven cents, three ways.** For the cold-open bond (price \$95, $D^{\text{mod}} = 4.1$, OAS 620 bp), compute $H$ and the TY hedge under (a) Ben Dor's B-rated 1998–2009 parameters ($\rho = -0.56$, $\sigma_s = 2.2\%$/day, $\sigma_y = 6.4$ bp/day), (b) the 2026 year-to-date B estimate from §8.2's Trend Watch, and (c) a 2022-style regime with $\rho = +0.3$ and the same volatilities. State in one sentence what each hedge assumes about *why* rates move.
2. **Kaz's fulcrum.** Kaz now claims the fulcrum security is the one where $H^{\text{rec}} = 0.5$. Using the perpetuity of §8.3 with $c = 7\%$ and $R = 35\%$, find the default intensity at which Kaz is accidentally right. (Answer: $\lambda = c/R = 20\%$.) Then explain to Kaz, in one sentence and without the word "priest," why the true fulcrum's hedge ratio is closer to zero.
3. **When Scholes–Williams is enough.** Show analytically that with one day of smoothing, $\theta = (\theta_0, 1 - \theta_0)$, and a serially uncorrelated factor, $\hat\beta_{\text{SW}}$ recovers $\beta$. Then compute its bias under the chapter's $\theta = (0.5, 0.3, 0.2)$ and confirm it against the code's printout.
4. **The regime-switching robot.** Modify section 2 of the code so that $\rho = -0.4$ for the first half of the sample and $+0.3$ for the second. Show that the full-sample $H$ hedges neither half well, then build a rolling 60-day $H$ and measure how many days it takes to cross 1 after the switch. Relate the answer to Case Study C.
5. **The duration-hedged future as a sixth column.** Add an instrument equal to the HY spread factor plus a futures overlay at a fixed $H = 1$ *(illustrative methodology)*. Show what happens to $\text{cond}(C)$ and to the CDX weight, and explain when a fixed-$H$ product is worse than building the hedge yourself.
6. **ROBO and the flat line.** Write the single sentence you would add to ROBO's spec to stop it from selling \$38mm of HYG against \$40mm of bonds. Then write the test that would have caught it.

### Deep-Dive Resource Graph

**Podcasts**

- *Bloomberg Odd Lots*: episodes on credit ETFs, the 2022 bond sell-off, and the April 2025 Treasury sell-off (show and topic only; episode numbers not verified).
- *Flirting with Models* (Corey Hoffstein): episodes on systematic credit and on smoothed returns in illiquid assets (show and topic only).
- *Resolve Riffs*: discussions of stock–bond correlation regimes (show and topic only).

**Practitioner Writing**

- Prentis and Ripka (Wellington, July 31, 2022), "Empirical duration of risk assets": https://www.wellington.com/en-us/institutional/insights/empirical-duration-risk-assets
- Slok (Apollo Academy, December 3, 2022), "High Yield Total Returns in 2022 Mainly Driven by Moves in Duration": https://apolloacademy.com/?p=11885
- Reuters via Kitco (March 14, 2023), report on US junk-bond spreads widening to a five-month high after SVB: https://www.kitco.com/news/off-the-wire/2023-03-14/us-junk-bond-spreads-balloon-widest-five-months
- CCMG, "Benchmark Review: Monthly Recap, April 2025": https://ccmg.com/benchmark-review-monthly-recap-april-2025/
- GW&K, "Taxable Monthly Update, April 2025": https://www.gwkinvest.com/wp-content/uploads/GWK-Taxable-Monthly-Update-April-2025.pdf
- Victory Capital, "Fixed Income Monthly Update, April 2025": https://advisor.vcm.com/assets/market-insights/VINC-Fixed-Income-Monthly-Update-COM-April-2025.pdf
- Markets Media (April 29, 2024), "CME US credit futures to begin trading on June 17": https://www.marketsmedia.com/cme-us-credit-futures-to-begin-trading-on-june-17
- FI Desk, "CME Group to begin trading credit futures in June": https://www.fi-desk.com/cme-group-to-begin-trading-credit-futures-in-june/
- Title only: Mesirow, "Wrong-way bonds" (2021); Robeco, "Duration Times Spread" explainer (2017); CME Group, "Understanding Bloomberg credit futures" (2024) and "A practitioner's guide to credit futures" (2026).

**Academic Papers**

- Ambastha, Ben Dor, Dynkin, Hyman and Konstantinovsky (2010), "Empirical Duration of Corporate Bonds and Credit Market Segmentation," *Journal of Fixed Income* 20(1), DOI 10.3905/jfi.2010.20.1.005.
- Ben Dor, Dynkin, Hyman, Houweling, van Leeuwen and Penninga (2007), "DTS (Duration Times Spread)," *Journal of Portfolio Management* 33(2), DOI 10.3905/jpm.2007.674796.
- Schaefer and Strebulaev (2008), "Structural models of credit risk are useful: Evidence from hedge ratios on corporate bonds," *Journal of Financial Economics* 90(1): https://ideas.repec.org/a/eee/jfinec/v90y2008i1p1-19.html (the academic twin of §8.2–8.3: Merton hedge ratios survive, but corporate rate sensitivity is "substantially lower than conventional duration measures would suggest").
- Collin-Dufresne, Goldstein and Martin (2001), "The Determinants of Credit Spread Changes," *Journal of Finance* 56(6): https://ideas.repec.org/a/bla/jfinan/v56y2001i6p2177-2207.html
- Rudin (2025), "Hedging Interest Rate Risk in High-Yield Bonds," in Fabozzi and de Jong (eds.), *Derivatives Applications in Asset Management*, Springer, DOI 10.1007/978-3-031-86354-7_24: https://ideas.repec.org/h/spr/sprchp/978-3-031-86354-7_24.html
- Dimson (1979): https://ideas.repec.org/a/eee/jfinec/v7y1979i2p197-226.html ; Scholes and Williams (1977): https://ideas.repec.org/a/eee/jfinec/v5y1977i3p309-327.html ; Getmansky, Lo and Makarov (2004): https://ideas.repec.org/a/eee/jfinec/v74y2004i3p529-609.html
- Bao, Pan and Wang (2011), "The Illiquidity of Corporate Bonds," *Journal of Finance* 66(3): https://ideas.repec.org/a/bla/jfinan/v66y2011i3p911-946.html
- Gebhardt, Hvidkjaer and Swaminathan (2005), "Stock and bond market interaction: Does momentum spill over?": https://ideas.repec.org/a/eee/jfinec/v75y2005i3p651-690.html
- Carr and Wu (2011), "A Simple Robust Link Between American Puts and Credit Protection": https://ideas.repec.org/a/oup/rfinst/v24y2011i2p473-505.html ; Kapadia and Pu (2012), "Limited arbitrage between equity and credit markets": https://ideas.repec.org/a/eee/jfinec/v105y2012i3p542-564.html
- Asvanunt and Richardson (2017), "The Credit Risk Premium": https://www.aqr.com/Insights/Research/Journal-Article/The-Credit-Risk-Premium ; Ilmanen, McGuire and Warga (1994), "The Value of Duration as a Risk Measure for Corporate Debt": https://www.aqr.com/Insights/Research/Journal-Article/The-Value-Of-Duration-as-a-Risk-Measure-for-Corporate-Debt
- Asness, Krail and Liew (2001), "Do Hedge Funds Hedge?", *Journal of Portfolio Management* 28(1), DOI 10.3905/jpm.2001.319819.
- Title only: Israel, Palhares and Richardson (2018), "Common Factors in Corporate Bond Returns," *Journal of Investment Management*; Molenaar, Senechal, Swinkels and Wang (2023), *Empirical evidence on the stock–bond correlation*.

**Data & Code**

- FRED, ICE BofA OAS by rating (BAMLH0A0HYM2, BAMLH0A1HYBB, BAMLH0A2HYB, BAMLH0A3HYC, BAMLC0A0CM) and Treasury yields (DGS2, DGS10): https://fred.stlouisfed.org/series/BAMLH0A3HYC . Since April 2026, only three years of history.
- FINRA TRACE (transaction-based returns and the staleness diagnostics of §8.5): https://www.finra.org/filing-reporting/trace
- iShares HYG: https://www.ishares.com/us/products/239565/ishares-iboxx-high-yield-corporate-bond-etf ; iShares HYGH: https://www.ishares.com/us/products/264544/ishares-interest-rate-hedged-high-yield-bond-etf ; SPDR JNK: https://www.ssga.com/us/en/intermediary/etfs/spdr-bloomberg-high-yield-bond-etf-jnk
- CME Group (Treasury and credit futures specifications, canonical root): https://www.cmegroup.com
- This book: `ido_engine.py` in §8.9; Appendix B for building a TRACE-based OAS history now that FRED's free window is three years.

<!-- STATUS: COMPLETE -->
