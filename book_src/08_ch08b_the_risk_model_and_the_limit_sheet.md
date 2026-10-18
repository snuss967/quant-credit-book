# Chapter 8-B: The Risk Model You Run Every Morning: Factors, Idiosyncratic Variance, Jump-to-Default, Stress and the Limit Sheet

> **Prerequisites.** Chapter 4-B (DV01, key rates, CS01); Chapter 7-B (EWMA, Ledoit–Wolf, PCA, bootstrap, Monte Carlo errors); §8.1–§8.8 (the decomposition, the sub-80 discontinuity, DTS, Dimson betas, the hedge matrix, the common residual); §5.5 (Beta recoveries); §12.5 (DTS covariance, desmoothing); §24.3 ($N^{\text{JTD}}$). None of the mathematics is new. What is new is one engine that runs at 7:30 every morning and is graded by its own backtest.

*Builds on:* §5.1.4 (the first Fourteen-Sigma Tuesday), §5.5, §6.3 and §11.4 ($\lambda^{\mathbb{P}}$), §6.8, §8.1–§8.8, §12.4–§12.5, §24.3, §28.2, §28.5. *Used in:* Chapter 8-C (the morning explain imports `risk_model.py`), §9.8 (the optimizer's covariance), §12.5 (the regime correlation), §19.5 (the basket residual covariance becomes a special case), §28.5 and §28.9 (the risk-versus-limits panel of the PM dashboard).

## Cold Open: Fourteen-Sigma Tuesday, the Sequel

The e-mail arrives at 7:31 a.m., one minute after the risk pack, in the capital letters that compliance software reserves for weather warnings and limit breaches.

*LIMIT BREACH (3). Issuer JTD top-10: HALVORSEN BUILDING PRODUCTS, SOFT. DTS, B-rated Industrials: HARD. ES 1d 99%: SOFT.*

Theo reads it twice, the way he once read a notice of default from an agent bank. On Friday the Halvorsen 7.25% notes due 2029 had been 92. On Monday, after a lender call half the street was on and the desk was not, they opened at 78 (Chapter 1). The desk still owns \$12mm face. Monday was one bad day, lived through and explained. What Theo cannot see is why a bond that did nothing new overnight has set off three alarms.

Kaz is already at the whiteboard, which is a bad sign before eight. "The model called Monday a fourteen-sigma move," they say. "The one-day standard deviation on the position was a point. The bond fell fourteen. So either we saw the rarest event since the Cambrian or—"

"Or your model has the wrong sigma," Ines says, without taking off her coat. She sets her coffee on Theo's desk like a chip on the felt. "Fine. Which line do we cut, and what's the pot if we're wrong about which line?"

Mags arrives last with a printout of the risk pack, because she does not trust a number she cannot fold. "Two soft, one hard." She taps the second line. "A limit is something you breach politely, in writing, before lunch. I told you that your first week. The hard one you fix before you finish your coffee, or you explain it to the risk committee after they finish theirs."

A fourth item in the inbox is timestamped 2:14 a.m. Someone on the overnight desk had asked ROBO to "keep risk under the limit," and ROBO has drafted orders to sell all 2,000 lines of the book at 9:31 a.m. and buy every one back at 3:59 p.m. Its note explains, correctly, that the intraday limit monitor runs from 9:30 to 4:00, so the book will be inside every limit for as long as anyone is checking. Estimated round-trip cost: 1.9 points on the whole portfolio. "Flat all day," Kaz reads aloud. "Bankrupt by Thursday."

Theo is not looking at ROBO's orders. He is looking at the JTD line, because he recognizes the number. On Monday night he read the issuer's 8-K, saw that the new-money financing being discussed on the lender call would sit in a subsidiary that held the company's patents, and cut his recovery assumption for the notes from 40 cents to 15. He typed it into the recovery table at 11:40 p.m. and went to bed feeling diligent. The price had fallen fourteen points. His recovery had fallen twenty-five. Jump-to-default, the loss if Halvorsen defaulted tomorrow, had gone *up*.

"I did that one," he says.

"Good," says Ines. "Then that's the one line on this page you understand. Now explain the other two."

Which raises the question this chapter answers. **What is the number on the risk report supposed to be, and what do you do when it is wrong?**

By the end of the chapter Theo will have rebuilt the model that sent that e-mail and found the bug in it. Along the way he learns why credit loadings are measured in DTS, why a bond below 80 needs a different model rather than a bigger volatility, why default lives in its own layer, how expected shortfall is read off the mixture, how to count the model's own failures, and what a limit sheet really is: a contract between the model and the people allowed to overrule it.

## 8B.1 What the Model Is For

At Theo's old firm the thirteen-week cash flow model had one job: to say how much cash could go wrong before the next re-forecast, judged brutally by what happened in week four. Nobody asked it whether the company was a good investment. It answered a narrower, more useful question: *how much room do we have, and where do we run out first?*

The risk model is the same animal in a different suit, a forecast of how much the book could lose before tomorrow's re-forecast, with three questions attached. *How much*, on a normal bad day and a very bad one? *Where from*: rates, a sector, one issuer, a hedge that stops hedging? And *what then*: which limit line binds, and who gets the phone call? People keep asking it a fourth question, whether the book will make money, and it has no opinion. Its expected return is zero by construction, and a desk that reads a falling risk number as good news has confused the thermometer with the weather.

"In my day," Mags says, "the risk report was a man named Gerry who walked over to your desk around four and asked if you were sure." She considers this. "Gerry had a very good backtest. He was wrong about once a year and he always told you which year."

What Gerry carried in his head, and what the model has to carry in matrices, is the single fact that makes portfolio risk different from the sum of position risks.

> **Math, Gently.** *Variance adds in quadrature, and correlation decides how much.* A standard deviation is the typical size of a day's move, in dollars; variance is its square. When two positions move independently their *variances* add, not their standard deviations: daily standard deviations of \$60k and \$80k combine to $\sqrt{60^2 + 80^2} = \$100$k, not \$140k. That is Pythagoras, which is why risks are said to add "in quadrature": two sides of a right triangle, with the portfolio as the hypotenuse. Correlation, $\rho$, measures how much the two positions move together, on a scale from $-1$ to $+1$, and it bends the triangle. The general rule for two positions is
>
> $$
> \sigma_p^2 = \sigma_A^2 + \sigma_B^2 + 2\rho\,\sigma_A\sigma_B .
> $$
>
> At $\rho = 1$ the triangle collapses into a straight line and the risks add: \$140k. At $\rho = 0.6$, a typical number for two single-B bonds in the same sector, the book's risk is $\sqrt{3{,}600 + 6{,}400 + 5{,}760} \approx \$126$k. Now flip the sign of B to make it a hedge: $\sqrt{3{,}600 + 6{,}400 - 5{,}760} \approx \$65$k, which is *more* than the \$60k you started with. A hedge that is only 60% correlated, put on at full size, adds risk. The variance-minimizing size is $\rho\,\sigma_A/\sigma_B = 0.6 \times 60/80 = 0.45$ of a unit, which brings the risk down to $60\sqrt{1 - 0.36} = \$48$k. The full version, with matrices, is the covariance of §7-B.5.

The small example has a large consequence. A book of 2,000 bonds is not 2,000 independent bets, because bonds share issuers, sectors, ratings and a market. If the average correlation between positions is $\bar\rho$, the number of *effectively* independent bets in a book of $n$ equal positions is about

$$
n_{\text{eff}} = \frac{n}{1 + (n-1)\bar\rho}.
$$

With $n = 2{,}000$ and an average correlation of only 0.025, that is $2{,}000/(1 + 1{,}999 \times 0.025) \approx 39$. Two thousand lines, forty hands, the same forty that §28.2 finds in the issuer column. A risk model that cannot see the shared part reports a book that looks as diversified as a phone book and behaves like forty concentrated positions.

The same arithmetic says where the risk lives, because volatility splits exactly into contributions from each position.

> **Math, Gently.** *Who owns the risk? Marginal contribution, by Euler.* Ask how much the book's volatility would rise if one position grew by a dollar: $\partial\sigma_p/\partial w_i = (\Sigma w)_i/\sigma_p$, where $(\Sigma w)_i$ is position $i$'s covariance with the whole book. Multiply each by the position's size and the pieces add exactly to $\sigma_p$, a theorem Euler proved two centuries before anyone owned a bond. In the two-bond book at $\rho = 0.6$, A contributes $(3{,}600 + 2{,}880)/125.5 \approx \$52$k and B $(6{,}400 + 2{,}880)/125.5 \approx \$74$k, summing to \$126k: B owns 59% of the risk with half the capital. The full version, by factor and issuer, is the first table of the risk pack and the input to §9.8's optimizer.

But a contribution table is only as good as the covariance behind it, and a covariance for 2,000 bonds is four million numbers, most of them unknowable from a credit desk's data. The way out is the one a restructuring banker takes with a forty-instrument capital structure: notice that most of them are claims on the same few things.

## 8B.2 The Factor Taxonomy

Kaz draws the tree on Tuesday afternoon, and Theo, who has drawn a thousand organization charts of holding companies and guarantor subsidiaries, recognizes the shape before it is labelled. "Every bond here is a claim on five things," Kaz says. "Rates, spread, liquidity, whatever the market is doing that our spread factors missed, and the hedges' own idea of the price. Then the part that belongs to the bond alone." They write *IDO?* in the last box, catch a look from Ines, and change it to *residual*.

The first branch is **key-rate DV01s** (Chapter 4-B): the price change for a one-basis-point move at the 2-, 5-, 10- and 30-year points of the curve. A 2029 note and a 2034 note with the same modified duration hedge each other on a parallel shift and lose together on a steepener, and the key rates are what notice.

The second branch is where credit lives. Bonds are grouped into **rating × sector cells** (B-rated Industrials, BB Energy, CCC Retail), and each cell has a factor return: its common *relative* spread change for the day. A bond's loading on its cell is not estimated bond by bond. It is the bond's DTS (§8.4) times a cell-level sensitivity estimated from the whole panel, because Ben Dor found spread volatility proportional to the spread itself. Twice the DTS means twice the exposure to the same sector shock, whatever the bond's own patchy price history says.

The third branch is **liquidity**, built from daily changes in liquidity cost scores, so that a morning when every dealer widens at once is one shock rather than two thousand small surprises. The fourth is the common component that Collin-Dufresne, Goldstein and Martin (2001) found in what structural variables could not explain, which §8.8 stripped out as the first principal component of the residuals. Here it becomes a **named factor**, so the morning meeting can call it something other than "idiosyncratic, all of it, in the same direction." The fifth is **basis**: CDX against cash, the high-yield ETFs against NAV, Treasury futures against the cash curve. These exist only because the desk hedges, and they bite when a hedge decides to be a separate asset for a week (§8.6, Chapter 20).

![Figure 8-B.1: The factor tree for a cash-and-derivatives credit book, with Tuesday's exposures marked on each branch: key-rate DV01s, rating × sector spread cells in DTS units, the liquidity factor, the common residual and the basis factors, with issuer residuals and the jump layer drawn as separate leaves. Illustrative book.](assets/figures/ch08b_factor_tree.png)

Put together, a bond's daily return in the model reads

$$
r_{i,t} = -\sum_{m} \text{KRD}_{i,m}\,\Delta y_{m,t} \;-\; \text{DTS}_i \sum_{k} b_{g(i),k}\,F_{k,t} \;+\; \beta^{L}_{i}\,F^{L}_{t} \;+\; \beta^{C}_{i}\,F^{C}_{t} \;+\; \sum_{j} \beta^{B}_{i,j}\,F^{B}_{j,t} \;+\; \epsilon_{i,t}.
$$

Here $\text{KRD}_{i,m}$ is bond $i$'s key-rate duration at curve point $m$ and $\Delta y_{m,t}$ the yield change at that point; $g(i)$ is the bond's rating × sector cell; $F_{k,t}$ is spread factor $k$'s relative spread change ($\Delta s/s$, a decimal); $b_{g,k}$ is the sensitivity of cell $g$ to factor $k$, which is 1 for a bond's own cell and something smaller for neighbouring cells when the model allows spillovers; $F^{L}$, $F^{C}$ and $F^{B}_{j}$ are the liquidity factor, the common residual and the basis factors, with their loadings $\beta$; and $\epsilon_{i,t}$ is whatever is left. The minus signs are the bond-math signs: yields up and spreads wider both lose money for a long position.

> **Math, Gently.** *A factor model is a regression that every bond shares.* Picture forty apartments on one heating system. On a cold night every apartment cools, and the ones with more windows cool more. A factor model says the same of bonds: each return is a few shared shocks (the cold front) times the bond's exposure to each (its windows), plus a bit that is the bond's own business (someone left a window open). The shocks are *factor returns* $F_{k,t}$, the exposures *loadings* $\beta_{i,k}$, the leftover the *idiosyncratic return* $\epsilon_{i,t}$. Tiny example: if B-rated Industrials widen 5% in relative terms ($F = 0.05$), a bond with DTS 0.20 loses about $0.20 \times 0.05 = 1\%$ from the factor and a cell-mate with DTS 0.08 loses 0.4%. The payoff is that the covariance of 2,000 bonds becomes the covariance of perhaps sixty factors plus 2,000 separate leftover variances, which a few years of data can actually estimate. The full version is §7-B.5.

Stack the loadings into an $n \times K$ matrix $B$, write $\Sigma_F$ for the factor covariance and $\Omega$ for the diagonal matrix of idiosyncratic variances. (Many risk texts call it $D$, a letter this book reserves for duration.) Then

$$
\Sigma = B\,\Sigma_F\,B^{\top} + \Omega, \qquad \sigma_p^2 = w^{\top}\Sigma\,w = \underbrace{(B^{\top}w)^{\top}\,\Sigma_F\,(B^{\top}w)}_{\text{factor}} + \underbrace{w^{\top}\Omega\, w}_{\text{idiosyncratic}} .
$$

The vector $B^{\top}w$ is the book's exposure to each factor; the first term is factor risk and the second is the risk that diversifies away as positions multiply. A restructuring banker makes the same split without equations when he says that a sector sell-off and one company's bad quarter are different problems with different fixes.

> **[SOURCE EXTRACTION]** *Paleologo_Advanced_Portfolio_Management p.111:* "Factor PnL is the sum of all the individual factor PnLs; each factor PnL is the product of factor exposure and factor return; and each factor exposure is the sumproduct of loadings and position NMVs."
>
> **Annotation.** Our analysis: Paleologo writes for an equity book. The credit translation changes one word and one unit. The word is *DTS*: the loading on a spread factor is DTS times a cell sensitivity, so the "sumproduct" is a DTS-weighted sum of market values that moves when a spread or a rating moves, with no trade. The unit is relative spread change. The sentence also explains why Chapter 8-C's morning explain and this risk pack share their loadings: the sumproduct that forecasts tomorrow's risk is the one that explains yesterday's P&L.

That DTS loading surprised Theo more than anything else on the tree. Because the loading is $\text{DTS}_i\,b_{g(i),k}$, a bond's risk moves without a trade when its spread widens (DTS rises) or its rating changes (it moves to a different cell and bucket). On Monday the whole B-rated Industrials cell had widened in sympathy with Halvorsen, every bond's DTS had risen with its spread, and the cell's exposure, comfortably inside its limit on Friday, was over the hard line without the desk buying a bond. That was breach number two. It was not a modelling error. It was the model noticing that the same bonds had become riskier.

The factor covariance $\Sigma_F$ comes from a few years of daily factor returns, with two adjustments derived in Chapter 7-B.

> **Math, Gently.** *EWMA and shrinkage: a memory that fades, and a guess pulled toward common sense.* An exponentially weighted moving average gives yesterday's squared move the most weight and each earlier day a constant fraction less. With a 60-day half-life, a move from three months ago counts half as much as yesterday's and one from a year ago about a sixteenth, so the covariance notices a new regime within weeks without forgetting the old one. Shrinkage solves a different problem: with sixty factors and a few hundred days, some estimated correlations are noise dressed as signal, and the matrix can come out nearly impossible to invert. Ledoit and Wolf blend the noisy estimate with a stable target (say, one average correlation everywhere) in a proportion estimated from the data. Tiny example: a sample correlation of 0.9, a target of 0.3 and a weight of 0.25 give $0.75 \times 0.9 + 0.25 \times 0.3 = 0.75$. The full version is §7-B.5.

That is the Gaussian half of the model, and on a quiet day it is most of the job. But the other two breaches in Theo's inbox had nothing to do with whether the factors were right. One came from a bond that had stopped behaving like a bond, the other from a default that had not happened.

## 8B.3 Loadings When Nothing Trades

The factor tree is easy to draw and hard to feed, because most bonds in a high-yield book do not trade on a given day. DTS loadings survive this, since an evaluated price supplies a spread and a duration. The trouble is everything estimated from history: the liquidity, basis and common-residual betas, and above all the idiosyncratic variance, which inherits every flaw in the factors.

An evaluated price for a bond that did not trade is a weighted average of recent evidence, a moving average of the truth (§8.5; App E, Law 9). Regress it on same-day factor returns and the beta comes out too small, because part of today's move reaches the mark only tomorrow. Dimson's repair is to regress on yesterday's, today's and tomorrow's factor returns and add the coefficients:

$$
\hat\beta^{\text{Dim}}_{i,k} = \sum_{\ell=-1}^{1} \hat\beta_{i,k,\ell}, \qquad r_{i,t} = \alpha_i + \sum_{\ell=-1}^{1}\beta_{i,k,\ell}\,F_{k,t-\ell} + \epsilon_{i,t}.
$$

The lead term ($\ell = -1$) looks like cheating and is not: it catches marks set before the factor's move showed in its close, which happens when the two are snapped at different times. Hold that thought.

For bonds without enough history even for Dimson, the model falls back in the order a banker looks for comparables. The bond's own estimate, if it has the prints. Then the issuer's other bonds, rescaled by DTS, since a 2029 and a 2031 of one company share almost everything but duration. Then the rating × sector cell, again rescaled by DTS. Man Group describes the same fill: normalize by DTS, fill new issues from issuer-level loadings, rescale by current DTS (*Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.15*; §9.8.1). A new issue also takes its idiosyncratic variance from the upper quartile of its bucket for its first few weeks, because new issues trade noisily while the market decides what they are worth, and a model that seasons them too fast under-reserves the bonds the desk most often holds in size.

When none of the three exists, the model refuses. Kaz learned why in their first month, when a convertible tagged with the sector "UNKNOWN" got zero loadings and zero idiosyncratic variance, and so contributed nothing to the book's risk for eleven days. It was the riskiest position on the desk.

The last ingredient sounds like plumbing, and it has caused more misery than any equation in this chapter: the timestamp.

> **Quant-Shop Life (a fictional composite).** *A systematic credit asset manager in a converted office park in New Jersey; a Tuesday in mid-March.* The risk job is scheduled for 6:10 a.m. and finishes, as usual, by 6:25. It is wrong, and nobody knows until 7:50, when the portfolio manager asks why the basis factor, CDX HY against the cash basket, moved a full standard deviation on a day when nothing happened. The risk engineer, a patient former physicist with a jar of rubber bands on her desk that she has never explained, spends three hours with two spreadsheets. The cash composites are snapped at 3:00 p.m. New York. The CDX closes come from a vendor whose configuration keys the snap to "15:00 local exchange time" for a feed it believes to be London-adjacent. The United States moved its clocks on the second Sunday of March; Britain would not move until the last. For two weeks a year the CDX mark sits an hour away from the bond mark, and whenever the market moves in that hour the basis factor reports a dislocation that is really a clock. She finds it at 10:41, after clearing the pricing vendor, the CUSIP-to-index map, the roll date and a theory about index reweighting. The fix takes four minutes: the snap written as a time zone and a wall-clock time rather than an offset, and a guard that stops the run if any two inputs disagree. The incident report takes two days. The portfolio manager's comment on it, in full, is "So the hedge was fine?" It was. The basis had been jumping by an hour's worth of market and reversing the next morning, two weeks a year, since before she arrived.

Theo's desk snaps everything at 3:00 p.m.: futures settlement, CDX close and bond composites, the same minute the P&L explain of Chapter 8-C uses. Risk and P&L share one snap or they share nothing (App E, Law 9 again), a sentence nobody believes until they have spent a morning chasing a basis that turned out to be daylight saving time.

*Builds on:* §8.5, §9.8.1, §27.2 (feeds and timestamps), §27.3 (the security master). *Used in:* Chapter 8-C (same loadings, same snap).

## 8B.4 Idiosyncratic Variance by Rating and Price Bucket

By Tuesday afternoon Theo had explained two of the three breaches. The expected shortfall breach was the one nobody liked, because it was only *soft*. The book had just had its worst day of the quarter, its central bond had fallen fourteen points, and the model thought the book was a little over its limit.

The reason was in the idiosyncratic-variance table, estimated each month by grouping every bond's factor residuals by rating and price bucket and taking the EWMA variance of each group. A simplified version:

| Rating | Price $\ge 95$ | 90–95 | 80–90 | Below 80 |
| :--- | ---: | ---: | ---: | :--- |
| BB | 0.20 | 0.35 | 0.70 | equity regime |
| B | 0.30 | 0.45 | 0.85 | equity regime |
| CCC | 0.55 | 0.75 | 1.10 | equity regime |

*Table 8-B.1. Daily idiosyncratic volatility in price points by rating and price bucket (illustrative), and the switch to the equity regime below 80.*

Halvorsen, at 78, belonged in the right-hand column. It sat in the 90–95 column, because buckets were assigned from the month-end evaluated price, and at the end of September the bond had been 93. One stale field in an otherwise fresh model, and a bond that had just become an equity option was being treated as a single-B bond near par with 0.45 points of daily idiosyncratic volatility.

"So we widen the vol," Kaz said. "Times three for anything under 80. Done."

Mags said no, and her reason is the idea of this section. Below 80 a high-yield bond does not become a more volatile bond. It becomes a different kind of claim (§8.3). Its price stops depending on the discount rate, because nobody expects the coupons on schedule, and starts depending on what the claim will recover and when: a question about enterprise value, which the equity market prices every day. The recovery-route hedge ratio of §8.3 goes to zero as the default intensity rises. A model that keeps the spread and rate loadings and triples the idiosyncratic volatility reports a bigger number and then hedges the wrong thing, selling Treasury futures against a bond that no longer cares about Treasuries.

So the model switches regimes. Below 80 the spread loadings give way to a loading on the issuer's equity, or on a sector equity index when there is no listed equity (Halvorsen is sponsor-owned, so its proxy is a building-products basket):

$$
r_{i,t} = \beta^{E}_{i}\,R^{E}_{t} + \epsilon^{E}_{i,t} \quad \text{if } P_i < 80, \qquad \beta^{E}_i \approx \frac{\partial P_i}{\partial E}\cdot\frac{E}{P_i},
$$

where $R^{E}_t$ is the equity proxy's return and $\beta^{E}_i$ comes from the bond's own prices against the equity when there is history, or from the structural elasticity of §6.2 when there is not. The switch, $\mathbf{1}\{P_i < 80\}$, has hysteresis: a bond enters the equity regime at 80 and leaves only above 85, so a bond hovering near 80 does not flicker between models twice a day and turn the risk report into a strobe light.

> **Math, Gently.** *Why a price near 100 and a price near 40 cannot share a distribution.* A *distribution* is the full list of what could happen tomorrow and how likely each outcome is. The bell-shaped *normal* has moves of a given size equally likely up or down and very large moves vanishingly rare. A *lognormal* is what you get when moves are percentages of the current level: a \$40 stock moving 3% moves \$1.20, and at \$20 it moves \$0.60; prices stay above zero and the right tail is long. A bond at 99 is neither. It sits under a ceiling (par at maturity, a call not far above), so its good days are fractions of a point, and over a trapdoor, so its bad days can be twenty. A bond at 40 has no ceiling in view: 70 on a good headline, 15 on a bad one, moves that scale with its level the way an equity's do. It is closer to lognormal, like the equity it is turning into. Tiny example: a 2% day is 2 points for the bond at 99, perhaps a once-a-year move, and 0.8 points for the bond at 40, a most-weeks move. Same percentage, opposite surprise. One volatility cannot describe both, so the model changes the distribution at 80, not the size of the move. The full version is §8.3.

Re-bucketed, with an equity-regime idiosyncratic volatility of about 2.2 points a day *(illustrative)* and a loading on the building-products basket, Halvorsen moved the one-day 99% expected shortfall from soft breach to hard. The model had understated the risk in exactly the bond that had just proved it was risky, the failure the bucket structure exists to prevent, defeated by a field that updated monthly.

The buckets are also where the market's own regime shows first. On Thursday, 15 October 2026, the ICE BofA US High Yield index closed at an option-adjusted spread of 323 bp, its CCC-and-lower subindex at 1,278 bp (a day after 1,282 bp, its widest in at least three years) and investment grade at 84 bp (FRED: BAMLH0A0HYM2, BAMLH0A3HYC, BAMLC0A0CM; §28.0). On 2 April 2025, before the tariff shock, the two high-yield numbers had been 342 and 925 bp, a ratio of 2.7. In October 2026 the ratio was about 4.0. The index looked bored; its basement was on fire. A model that scaled CCC risk off the high-yield index would have reported a quiet market, because the factor *was* quiet. The risk lived in the dispersion of the bottom buckets, in names moving on their own news, which is why idiosyncratic variance is estimated by rating and price bucket rather than as one multiple of the index.

*Builds on:* §8.3, §6.2, §11.6 (the CCC problem), §28.0 and §28.4 (the 2026 decompression). *Used in:* §8B.6, §8B.9.

## 8B.5 The Jump Layer

On Wednesday morning Kaz arrived with a proposal. They had spent the night adding Halvorsen's default risk to the Gaussian model, the elegant way: compute the variance of the loss from a possible default, add it to the bond's idiosyncratic variance, and let the covariance do the rest. "One model," they said. "Let's just assume Gaussian, with a bigger variance."

Theo had been waiting three weeks to say the next sentence. "A default isn't a big move. It's a different event." In six years of watching companies default, he had never seen one drift there. They were fine, and then the revolver was drawn, the grace period started, the ad hoc group hired counsel, and the bonds went from 78 to 30 on a Thursday. The question was never the size of the daily wobble. It was whether the event would happen, and what the claim would be worth when it did.

> **Math, Gently.** *A clock that rings once: the exponential, the hazard rate and the Poisson count.* Think of default as an alarm clock with a hidden setting. The *hazard rate* $\lambda$ is the chance per year that it rings, given that it has not rung yet. With constant $\lambda$ the waiting time is *exponential*, and the chance it rings within $h$ years is $1 - e^{-\lambda h}$, almost exactly $\lambda h$ when that is small. Default probability therefore scales with time, not with its square root. Tiny example: Halvorsen after the lender call, at $\lambda = 25\%$ a year, has a one-day default probability of $1 - e^{-0.25/252} \approx 0.099\%$ and a ten-day one of about 0.99%, ten times as large. Each issuer is a coin that lands "default" with that probability, a *Bernoulli* trial, and across many issuers with independent clocks the number of defaults is close to *Poisson*, the distribution of counts of rare events. The full version, with hazards that change over time, is §6.6 and §7-B.4.

The jump layer models that event issuer by issuer and keeps it out of the Gaussian layer. Over a horizon of $h$ years the book's loss is

$$
L_h = L^{\text{Gauss}}_h + \sum_{\text{issuers } i} \mathbf{1}\{\tau_i \le h\}\,\text{JTD}_i, \qquad \text{JTD}_i = \sum_{j \in i} N_j\,(P_j - R_j), \qquad \mathbb{P}(\tau_i \le h) = 1 - e^{-\lambda^{\mathbb{P}}_i h}.
$$

Here $L^{\text{Gauss}}_h$ is the factor-plus-idiosyncratic loss of the previous sections; $\tau_i$ is issuer $i$'s default time; the inner sum runs over every instrument $j$ the desk holds that defaults when issuer $i$ does, with signed notional $N_j$ (long positive), current price $P_j$ and recovery $R_j$, both as fractions of par. (This $N_j$ is a notional, not the Poisson process $N_t$; its subscript is an instrument, not a time.) A long bond loses $P - R$ per unit of face; bought CDS protection gains $1 - R$, a JTD of $-N(1-R)$; a short bond gains $P - R$; an equity put gains roughly its strike.

The recovery is a random variable, and it lives on a shelf with two ends.

> **Math, Gently.** *The Beta distribution: a shelf with two knobs.* Recovery cannot fall below zero or (accrued aside) rise above par, and a bell curve leaks probability past both ends. The Beta distribution lives between 0 and 1 and has two knobs, $a$ and $b$: turn up $a$ and probability slides toward full recovery, turn up $b$ and it slides toward zero; with both below one it is U-shaped. Its mean is $a/(a+b)$. Tiny example: Chapter 5's senior unsecured fit, Beta(0.87, 1.30), has a mean of $0.87/2.17 \approx 40\%$ and a spike near zero; a first-lien loan book at Beta(0.93, 0.40) averages 70% and piles up near par. The full version, conditioned on collateral and seniority, is §5.5.

Kaz came round by lunch. They drew Theo's revised Halvorsen recovery on the whiteboard, a Beta(0.6, 3.4) with mean 15% and standard deviation 16%, a tall spike near zero and a thin tail toward 60, and stood back. "It's a Gaussian with opinions," they said, the most affectionate thing Kaz has ever said about a distribution that is not Gaussian.

Theo's revision made Halvorsen's JTD $12 \times (0.78 - 0.15) = \$7.56$mm, against a soft limit of \$7.0mm for a single-B issuer *(illustrative)*; before it, $12 \times (0.92 - 0.40) = \$6.24$mm. The price had fallen fourteen points and the expected recovery twenty-five, so the gap between them, which is what the desk loses if the company files tomorrow, had grown. That is why the JTD line uses the desk's own recovery view, and why the person who owns that view, often the ex-banker who reads the documents, owns the line.

Kaz's version fails in a way the numbers make plain. On Halvorsen alone the Gaussian layer has a one-day standard deviation of about \$0.12mm. The jump layer, at a 0.099% one-day default probability and \$7.56mm of JTD, has $\sqrt{0.00099 \times 0.99901} \times 7.56 \approx \$0.24$mm. Fold them into one Gaussian and the standard deviation is $\sqrt{0.12^2 + 0.24^2} \approx \$0.27$mm, the 99% one-day VaR about \$0.62mm, and that number corresponds to nothing that can happen. On 999 days in a thousand Halvorsen survives and the 99th-percentile loss is near \$0.28mm; on the thousandth it defaults and the desk loses about \$7.6mm. The blend invents a world in between, overstates ordinary days, understates the day that matters, and hands the optimizer of §9.8 a covariance that thinks the jump diversifies away like a wiggle. Defaults cluster in recessions; wiggles do not.

Measures are the second reason to keep the layers apart. The jump layer's hazard is $\lambda^{\mathbb{P}}$, the desk's forecast of real-world default frequency (§6.3, §11.4), not the $\lambda^{\mathbb{Q}}$ backed out of CDS spreads, which carries a risk premium and for high-grade names is typically a multiple of the physical rate. A risk model forecasts real losses, so it lives in $\mathbb{P}$ (App E, Law 4). The same JTD runs through the credit-triangle arithmetic of §6.8, the dealer's quote in §18.6 and this risk pack, and it is charged once (App E, Law 6). A desk that charges it in the quote, again as Gaussian variance, and a third time on the limit sheet has paid for one risk three times and will soon find it can afford to own nothing worth owning.

> **[SOURCE EXTRACTION]** *Dynkin_Systematic_Investing_in_Credit p.400:* "Rating‐based stop‐loss rules do not protect against jump to default."
>
> **Annotation.** Our analysis: Dynkin's team says this of portfolios hit by Lehman Brothers and Washington Mutual in 2008–2009. On a 2026 desk it is the case for a separate layer. A stop-loss or a downgrade trigger acts on the path, and a jump has no intermediate points to act on. The only defence is to size the jump before it happens, issuer by issuer, which is the JTD line's job.

Issuer netting is where the layer earns its keep on a desk that owns more than bonds. The desk holds Brambleworth, a fictional issuer, three ways *(illustrative)*: \$8mm face of senior notes at 95, \$5mm of the first-lien term loan at 98, and \$6mm of bought five-year CDS on the senior notes. With mean recoveries of 40% on the notes and 70% on the loan,

$$
\text{JTD}_{\text{Bramble}} = 8\,(0.95 - 0.40) + 5\,(0.98 - 0.70) - 6\,(1 - 0.40) = 4.40 + 1.40 - 3.60 = \$2.20\text{mm}.
$$

Two details keep this honest. The notes and the CDS share one recovery draw, because the CDS settles on an auction of the same obligations (Appendix D). The loan's recovery is a different but correlated draw, since both come from one enterprise value; the engine of §8B.11 drives all of an issuer's recoveries from one random number, a shortcut for running a waterfall over a simulated value (§5.5, Chapter 12-C). And the CDS notional that would make the notes JTD-neutral is not their face but $N^{\text{JTD}} = 8 \times (0.95 - 0.40)/(1 - 0.40) \approx \$7.33$mm (§24.3), so \$6mm of protection leaves the desk long about \$0.8mm of jump on the notes.

> **View From Another Seat.** *The dealer desk and the CLO manager.* A bank credit-trading desk reads the JTD line through its capital. At the largest US dealer the binding limits on markets businesses are the G-SIB surcharge, risk-weighted assets and the stress capital buffer, and its CFO has called the G-SIB surcharge "a significant disincentive to a particular type of business, in particular some markets business" (JPMorgan Chase, first-quarter 2026 earnings call, 14 Apr 2026). For a dealer the question is JTD per unit of balance sheet, and a jump is something to sell on rather than hold, which is why Chapter 18-B prices it into the quote. A CLO manager's binding line is the CCC bucket, typically 7.5% of the portfolio, above which excess CCC loans count at market value in the over-collateralization test (§21.4). It is softer than it looks: S&P Global Ratings reported that about 42% of 554 reinvesting US broadly syndicated CLOs had CCC exposure above 7.5%, yet just over 1% were failing a junior OC test (S&P, 28 Apr 2023, as cited in Chapter 1). For the CLO a downgrade from B3 to Caa1 changes the limit sheet the way a migration changes Theo's DTS cells: with no trade, on the agencies' schedule.

> **View From Another Seat.** *The insurer and the systematic fund (generic seats).* A life insurer holding the same bond computes no binding expected shortfall on it. Its risk number is a capital charge set by the NAIC designation, its question is spread per unit of required capital, and it sells when a downgrade raises the charge, not when the price falls five points. The charges themselves move: in June 2026 the NAIC adopted new C-1 factors for CLO tranches, effective for year-end 2026 reporting (Sidley, 9 Jul 2026). A systematic fund sees the JTD line as a breadth problem, holding hundreds of issuers in small sizes behind an issuer cap often well under 1% of the book. Its blind spot is the mirror of the insurer's: a cap protects against one default and does nothing about forty in the same recession, which is why the stress library of §8B.7 shocks factors and jumps together.

*Builds on:* §5.5 (Beta recoveries), §6.3, §6.6 and §6.8 (measures, intensities, the credit triangle), §18.6 (the jump in the quote), §24.3 ($N^{\text{JTD}}$), Appendix D (the auction). *Used in:* §8B.6, §8B.7, §8B.9 (the issuer JTD top ten), Chapter 18-B, §28.4 (Kelly with jumps).

## 8B.6 Expected Shortfall on the Mixture

With two layers, the risk number on the first page of the pack can no longer be a standard deviation times 2.33. It has to be read off the distribution of $L_h$ itself, which is a mixture: on most days a Gaussian, and on a few days a Gaussian plus a jump.

> **Math, Gently.** *VaR is the threshold; ES is the average of the bad days; a mixture is two stories with weights.* Line up a thousand possible tomorrows from best to worst. The 99% *value-at-risk* is the loss on the tenth-worst day, a threshold crossed one day in a hundred. It says nothing about how bad those ten days are, so a book that loses \$3mm on its worst day and one that loses \$30mm can share a VaR. The 99% *expected shortfall* is the average of the ten worst days: it looks over the cliff edge instead of measuring where the edge is. A *mixture distribution* draws tomorrow from one of several distributions with given probabilities, here "no default" with probability $1 - p$ and "default" with probability $p$. Tiny example: if a desk's only risk were a \$10mm default with probability 0.5% a day, its 99% VaR would be zero, since the default fills only half of the worst 1% of days, and its 99% ES would be $0.5/1 \times 10 = \$5$mm. VaR is blind to any loss rarer than its own confidence level. The full version is §5.1 and §5.10.

That blind spot matters at once. Halvorsen's one-day default probability of 0.099% sits below the 1% line, so the position's honest one-day 99% VaR is about \$0.28mm, the Gaussian wobble alone, while its one-day 99% ES is about \$1.04mm, because the worst ten days in a thousand include the day it defaults. Section 5.10 asked for ES and JTD beside any VaR; this engine makes the request expensive to ignore.

The horizon is the second trap. Committees like a ten-day number, and the traditional way to get one is to multiply the one-day number by $\sqrt{10}$.

> **Math, Gently.** *The random walk and the square root of time.* A drunk takes one step a day, left or right at random. After ten days he is rarely ten steps from the lamp post, because the steps partly cancel; his typical distance grows like the square root of the number of steps, about $\sqrt{10} \approx 3.2$. That is a *random walk*, and it is why a diffusive P&L's ten-day volatility is about 3.2 times its one-day volatility when days are independent. A default is not a step. It is a trapdoor open each day with a small probability, and the chance of having fallen through within ten days is about ten times the one-day chance. Diffusion scales with $\sqrt{h}$; jumps scale with $h$. The full version is §5.1 and the Brownian-motion primer of §6.1.

Mix the two and no single scaling works. Take a book with a one-day Gaussian standard deviation of \$1mm and one concentrated issuer with a JTD of \$20mm and a one-day default probability of 0.15% *(illustrative)*.

| \$mm | 1-day | $\sqrt{10}\times$ 1-day | 10-day, computed on the mixture |
| :--- | ---: | ---: | ---: |
| 99% VaR | 2.39 | 7.55 | 18.60 |
| 99% ES | 5.31 | 16.80 | 21.70 |

*Table 8-B.2. One concentrated jump and a Gaussian book (illustrative). Over one day the jump is rarer than 1% and VaR cannot see it; over ten days its probability is about 1.5%, and it becomes the VaR.*

The ten-day VaR is not three times the one-day VaR but nearly eight times, because over ten days the default has moved inside the worst 1%, and the ten-day ES is 30% above the shortcut. With a smaller jump the error flips sign: for an \$8mm JTD at 0.2% a day the shortcut *overstates* the ten-day ES (Exercise 2). The shortcut is neither conservative nor aggressive. It is a different model from the one the desk runs. Figure 8-B.2 shows both traps, Halvorsen's one-day loss on the left and the square-root shortcut on the right.

![Figure 8-B.2: The two traps of §8B.6. Left: the chance that Halvorsen's one-day loss exceeds x; its 0.099% default plateau (mean loss 7.56mm) sits below the 1% line, so VaR (0.28) sees only the Gaussian wobble while ES (1.04) sees the plateau, and folding the jump into one Gaussian gives a VaR of 0.62 that matches no real day. Right: the mixture's ES and VaR against the square-root-of-time shortcut, which understates the Table 8-B.2 book and overstates the Exercise 2 book. Illustrative: computed from the §8B.5 Halvorsen inputs and the parameters of Table 8-B.2 and Exercise 2.](assets/figures/ch08b_mixture_traps.png)

The engine computes the layers by different methods because they are different objects. The Gaussian layer is historical simulation: today's exposures times the past few years of factor returns, summed in $h$-day blocks rather than scaled by $\sqrt{h}$ (which keeps whatever autocorrelation the factors really have), plus idiosyncratic draws from the buckets. The jump layer is Monte Carlo: on each path every issuer's coin is flipped with probability $1 - e^{-\lambda^{\mathbb{P}}_i h}$, defaulted issuers draw recoveries from their Beta legs, and the JTD losses are added to that path's Gaussian draw. A 99% ES from 100,000 paths rests on the worst 1,000, and an issuer with a 0.1% one-day default probability defaults on only about 100 paths, so its contribution is noisy. The engine prints the standard error beside the number (§7-B.8) and switches to importance sampling, raising default probabilities in the simulation and reweighting, when the tail rests on too few draws.

*Builds on:* §5.1, §5.10, §7-B.6 (block bootstrap), §7-B.8 (Monte Carlo errors). *Used in:* §8B.9, §28.5 (LVaR).

## 8B.7 The Stress Library

On Thursday the risk committee asked for "the usual stresses." Ines, who regards the word *usual* as a tell, asked which usual they meant, and was handed a page of paragraphs. *Scenario 3: a severe recession with a flight to quality and a liquidity crunch.* "That's a story," she said. "I can't bet against a story. Give me the board."

The board, in a factor model, is a vector of factor shocks: a dated episode translated into moves of the factors the model already has, plus a jump overlay saying which hazards rise and which issuers default. Written that way, a scenario applies to any future book, because it shocks factors rather than bonds the desk may no longer own, and it can be argued with line by line: a committee that sees the CCC cell shocked by 35% can ask why not 50%.

The desk keeps six dated scenarios and one constructed one, each pointing to the section that tells its story in full.

| Scenario | Window | What moved (sources in the cited §) | Factor translation (illustrative) |
| :--- | :--- | :--- | :--- |
| March 2020 | 20 Feb–23 Mar 2020 | Moody's Baa–Treasury spread 205 bp to 431 bp; 10-year 1.52% to 0.54% (9 Mar), back to 1.18% (18 Mar), 0.76% (23 Mar) (FRED); LQD at a 5.08% discount on 19 Mar while HYG traded at a premium (§20.5) | Spread cells +100% to +120% relative, IG worse than HY in ETF form; liquidity 6σ; ETF–NAV basis −5 points; rates whipsaw both ways |
| The 2022 rates year | 31 Dec 2021–30 Dec 2022 | 10-year 1.52% to 3.88%, peak 4.21% on 21 Oct (FRED); HY OAS near 600 bp in early July (approx., §10.7) | Key rates +230 to +250 bp; spread cells +60% relative; $\rho_{y,s} > 0$ all year |
| LDI BWIC week | 26 Sep–7 Oct 2022 | More than €1.5bn of CLOs listed in BWICs in a week, AA in the 80s, BB and B lists failing to meet reserves (§18.9.1) | Liquidity factor 5σ, structured-credit basis −8 points; corporate cells only +10% |
| SVB | 8–13 Mar 2023 | 2-year 5.05% to 4.03%; HY OAS 461 to 503 bp from 10 to 13 Mar, the largest daily widening since June 2020; Baa–Treasury 179 to 214 bp (§8.7B, FRED) | Key rates −70 to −100 bp at the front; HY cells +10% relative; bank sub-debt and holdco JTD overlay |
| April 2025 | 2–11 Apr 2025 | HY OAS 342 to 461 bp (7 Apr), CCC 925 to 1,137, B 353 to 486, BB 212 to 306, IG 96 to 120; $\rho_{y,s}$ changed sign twice in seven sessions (§8.7C, §10.7 Coda) | HY cells +35% relative, CCC +23%; CDX–cash basis +15 bp; correlation sign flip as a regime input |
| 2026 CCC decompression | Q3–Q4 2026 | HY OAS 323 bp and CCC 1,278 bp on 15 Oct 2026, a CCC/HY ratio near 4.0 against 2.7 in April 2025 (§28.0) | HY factor flat; CCC cells +30% relative; idiosyncratic variance in the CCC buckets ×2; hazard overlay ×1.5 below 80 |
| Hedge basis widens with spreads | constructed | The case the §8.6 annotation demands: the hedge stops hedging on the day the book needs it, as the ETF discount did in 2020 and the rates hedge did in March 2023 | Spread cells +40%; CDX and ETF hedges move only half as much; rates hedge loses as the curve rallies |

*Table 8-B.3. The stress library. Levels are FRED closes or the canonical sections' sourced figures; the factor translations are the desk's illustrative calibration.*

The SVB row is the one in which both layers fail together. The rates leg of a hedged high-yield book lost as the front end rallied a full point while the spread leg lost as high yield widened (§8.7B), and the bank holding-company notes some credit books owned carried a jump no Gaussian layer could see. SVB Financial Group's senior notes, about \$3.3bn in one class, sat behind depositors, the Federal Home Loan Bank and the FDIC, while the bank's equity implied volatility had spent the previous year near the bottom of its range (§6.4.4, from the 10-K, the March 2023 8-Ks and the Federal Reserve's review of 28 April 2023). The jump layer's job in that scenario is not to forecast the run. It is to say, before the run and in a column the committee can read, what the desk loses if a name it owns does what SVB did.

Each scenario runs on today's book and reports two columns, Gaussian and jump, which the committee sees separately before anyone adds them.

![Figure 8-B.3: The book's P&L under each scenario of the stress library, with the factor-and-idiosyncratic loss and the jump-to-default overlay shown as separate bars. The constructed hedge-basis scenario is the worst on the factor bar; SVB and the 2026 decompression are the worst on the jump bar. Illustrative book.](assets/figures/ch08b_stress_library.png)

The Ad Hoc Group, by letter of counsel, asked to be added to the risk factor list "as a matter of record." Kaz read the letter twice and replied that the Group was already in the model, as the jump layer. The Group's counsel replied that it reserved all rights.

*Builds on:* §8.6–§8.7, §10.7, §18.9.1, §20.5, §28.0. *Used in:* §8B.9, §12.9 (MAC stress tests), Chapter 8-C.

## 8B.8 The Backtest

A forecast never compared with what happened is an opinion. The 13-week model got its grade in week four; the risk model gets one every day, when the desk compares the loss it took with the VaR it published the morning before. A day on which the loss exceeds the VaR is an *exception*. At 99% coverage a correct model produces exceptions on about 1% of days, about two and a half in a year of 250 trading days.

By the end of October, Theo's model had seven in its trailing 250 days.

> **Math, Gently.** *Counting exceptions as coin flips.* If the model is right, each day is a coin that lands "exception" with probability $p = 0.01$, independently of the others, and the count in $n$ days is *binomial* with mean $np$: 2.5 in 250. Seven is possible under a correct model, the way a run of heads is possible with a fair coin, but the chance of seven or more is only about 1.4%. A *likelihood ratio* turns that surprise into a number: how probable is the count under the model's $p$, relative to the best-fitting rate $x/n$? If the model were right, twice the log of that ratio would follow a *chi-squared* distribution with one degree of freedom, whose 95th percentile is 3.84. The full version is §7-B.2.

Kupiec's (1995) proportion-of-failures statistic is that likelihood ratio. With $x$ exceptions in $n$ days at coverage $p$,

$$
\text{LR}_{\text{POF}} = -2\ln\frac{(1-p)^{\,n-x}\,p^{\,x}}{(1 - x/n)^{\,n-x}\,(x/n)^{\,x}} \sim \chi^2_1 .
$$

For seven exceptions in 250 days at $p = 0.01$, the numerator's log is $243\ln 0.99 + 7\ln 0.01 = -34.678$ and the denominator's $243\ln 0.972 + 7\ln 0.028 = -31.930$, so $\text{LR}_{\text{POF}} = -2(-34.678 + 31.930) = 5.50$: above 3.84, so the model fails at 5%, and below 6.63, so it survives at 1%. Basel's traffic light puts five to nine exceptions in 250 days in the yellow zone, the same verdict in another dialect.

The count is half the story. Christoffersen (1998) asked whether exceptions arrive independently or in bunches. A model slow to notice a new regime misses on Monday, Tuesday and Wednesday of the same bad week and then catches up. His test treats the exception sequence as a two-state Markov chain, whose state tomorrow depends only on today's, and compares the chance of an exception after a quiet day, $\pi_{01}$, with the chance after an exception, $\pi_{11}$. Theo's seven came in four clusters: three consecutive days in the week of the Halvorsen gap, two consecutive days a week later, and two isolated days. The transitions are $n_{00} = 238$, $n_{01} = 4$, $n_{10} = 4$, $n_{11} = 3$, so $\hat\pi_{01} = 4/242 = 1.7\%$ while $\hat\pi_{11} = 3/7 = 43\%$. An exception made another exception twenty-six times more likely. The independence statistic is

$$
\text{LR}_{\text{ind}} = -2\ln\frac{(1-\hat\pi)^{\,n_{00}+n_{10}}\,\hat\pi^{\,n_{01}+n_{11}}}{(1-\hat\pi_{01})^{\,n_{00}}\,\hat\pi_{01}^{\,n_{01}}\,(1-\hat\pi_{11})^{\,n_{10}}\,\hat\pi_{11}^{\,n_{11}}} = 13.49 \sim \chi^2_1, \qquad \hat\pi = \frac{n_{01}+n_{11}}{n_{00}+n_{01}+n_{10}+n_{11}},
$$

and conditional coverage, the sum, is $\text{LR}_{\text{cc}} = 5.50 + 13.49 = 18.98 \sim \chi^2_2$, against a 1% critical value of 9.21. The model fails, and the clustering says why: its memory is too long. A 60-day half-life took weeks to notice that October was not September, and a bucket assignment that updated monthly took longer still. Figure 8-B.4 shows the count and the clusters.

![Figure 8-B.4: Seven exceptions in 250 days is a 1.4% outcome for a correct 99% model, so Kupiec rejects at 5%, and the seven came in clusters: an exception made another 26 times as likely (43% against 1.7%), which Christoffersen's independence test rejects. Illustrative: the binomial and both statistics are computed from the chapter's counts (n00 = 238, n01 = 4, n10 = 4, n11 = 3); the calendar positions of the exceptions are drawn for illustration.](assets/figures/ch08b_backtest_exceptions.png)

The backtest also runs bucket by bucket, as realized residual volatility over predicted, where a ratio near one means the bucket is honest. In October the sub-80 bucket's ratio was 2.6: the price-bucket bug of §8B.4, caught by its own statistics.

A failing backtest licenses a change, through a procedure: a written finding, a challenger run in shadow beside the champion, a comparison on data the challenger was not tuned on, and promotion through the rings and canaries that §27.8 uses for code. It does not license retuning the model inside the drawdown that produced the exceptions. The desk still tells new hires about the week Larkspur Foam's term loan fell to 84 on its drop-down headline (Chapter 13), when a junior quant shortened the EWMA half-life from 60 days to 15 on the third day of losses, "to make it more responsive." The re-run backtest was immaculate, because it had been tuned on the exceptions it was graded on, which is look-ahead in a lab coat. The short half-life then spent a quiet quarter overstating risk by 40% and squeezing the desk out of positions it would have been paid to hold. Mags's review was the shortest in the desk's history: "You wrote the exam and then you graded it."

*Builds on:* §7-B.2, §7-B.5, §27.8 (deployment). *Used in:* §8B.9, §28.9 (model-health panel).

## 8B.9 The Limit Sheet

The risk committee met on the first Monday of November, and Mags prepared Theo for it the way she once prepared junior lawyers for a confirmation hearing: by telling him about the worst one she knew.

### Case Study: The Whale and the Five Limits (JPMorgan's Chief Investment Office, 2012)

"Everything you need to know about limit sheets," she said, "is in a Senate report about a bank that had a perfectly good one."

The book was the Synthetic Credit Portfolio of JPMorgan Chase's Chief Investment Office, a portfolio of credit index and tranche positions originally meant to hedge the bank's credit exposure. In the first quarter of 2012 its traders tripled its net notional, from \$51bn to \$157bn, including at least \$62bn in a US investment-grade credit index, \$71bn in a European investment-grade index and \$22bn in a US high-yield index (Senate Permanent Subcommittee on Investigations, *JPMorgan Chase Whale Trades: A Case History of Derivatives Risks and Abuses*, staff report, 15 Mar 2013, PDF p.12; page references below are to the PDF). It had five risk metrics with limits or advisories: VaR, CS01, a 10% credit-spread-widening measure called CSW10%, stress loss and stop-loss advisories. In the first quarter it breached all five, and between 1 January and 30 April the limits and advisories were breached more than 330 times (PDF p.15).

Theo recognized every line. CS01 is his CS01 ladder; CSW10% is his DTS cell limit, a loss for a 10% relative widening, under another name; the stress limit is his stress library. What was missing was close to his jump and concentration lines: concentration limits, "commonplace for the same instruments" at the bank's investment bank, were absent at the CIO (PDF p.15).

"So the sheet was fine," he said. "What went wrong?"

"Everything that happens *after* the sheet," Mags said.

In January 2012 the portfolio breached the VaR limits of both the CIO and the whole bank for four days, a breach reported to the bank's most senior management (PDF p.15). While it was in breach, an alternative VaR model was "hurriedly adopted," approved on 30 January, and it cut the portfolio's VaR by 50%, from \$132mm to \$66mm (PDF pp.16, 188). The breach ended; the positions did not. A recommendation to lower the CIO's VaR limit from \$95mm to \$70mm alongside the new model was not acted on, and the report summarized the result in a sentence Mags read aloud: "rather than remove the offending credit derivative positions to reduce the amount of risk in the SCP, JPMorgan Chase removed the brakes instead" (PDF p.191). The new model, it later emerged, ran on spreadsheets fed by hand and contained "calculation errors involving hazard rates and correlation estimates that improperly lowered the VaR results" (PDF p.194). On 10 May the bank revoked it and reinstated the old one, and the revised first-quarter VaR came out at \$129mm, twice what had first been reported (PDF pp.16, 21).

The CS01 limit was simply outlived: exceeded by 100% in January, 270% in early February and more than 1,000% by mid-April (PDF p.15), and in breach for 59 trading days by 30 March. On 17 April an automated end-of-day notice read, in full, "MtM cs bpv limit is in excession by 1074% and has been in excession for 71 days" (PDF p.211). A risk measure called the Comprehensive Risk Measure had warned in February of a possible \$6.3bn loss over a year; it was dismissed internally as "garbage" (PDF p.15). The report's verdict on the breaches as a group was that they "were largely ignored or ended by raising the relevant risk limit" (PDF p.15). The portfolio lost at least \$6.2bn in 2012 (PDF p.12).

Kaz read the hazard-rate sentence twice. "They put the jump inside a spreadsheet. Hazards and correlations, hand-keyed, feeding a VaR, no separate layer, no backtest before it went live, swapped in during the breach it was meant to measure." They glanced at the Larkspur note pinned above their monitor. "That's §8B.8 with ten figures."

Ines put it as a hand. "Five tells, all showing, for four months. Nobody at the table folded. They changed the deck instead."

What the desk took from the case was a description of what a limit is for. A limit is a pre-agreed conversation: which number, crossing which line, obliges which person to explain what to whom, by when. Its value lies entirely in the conversation happening. A model change that halves the risk number is a limit change whether or not anyone edits the limit, so it goes to the same committee. A breach that lasts seventy-one days has become the new limit, chosen by nobody. And an override is a loan of risk capacity, which is why every override on Theo's desk carries a size, a reason, a name and an expiry date, and a second override of one line in a quarter puts the line itself on the committee's agenda.

### The sheet

Here is the sheet Theo's desk runs, with the soft and hard thresholds that turn exposures into conversations *(illustrative levels for a \$400mm high-yield book)*.

| Line | Measured as | Soft | Hard |
| :--- | :--- | ---: | ---: |
| DTS, each rating × sector cell | loss for a 10% relative widening of the cell, \$mm | 1.2 | 1.5 |
| CS01 ladder (0–3y, 3–7y, 7y+) | \$k per bp of spread | 60 / 90 / 70 | 80 / 120 / 90 |
| Key-rate DV01, net of hedges (2, 5, 10, 30y) | \$k per bp; a band around the target | ±15 | ±25 |
| Issuer JTD, top ten | \$mm, by issuer rating | B 7.0, CCC 4.0 | B 9.0, CCC 5.5 |
| ES 99%, 1-day and 10-day | \$mm, on the mixture (§8B.6) | 2.5 / 9.0 | 3.0 / 11.0 |
| Stress loss | worst library scenario, Gaussian plus jump, \$mm | 15 | 20 |
| Days to liquidate (§28.5) | days at 10% of average daily volume | 5 | 10 |
| Share of an issue | % of the issue outstanding | 7.5% | 10% |
| Backtest exceptions | count in 250 days at 99% | 5 | 10 |

*Table 8-B.4. The limit sheet. A soft breach starts a written explanation from the PM by noon; a hard breach requires a reduction by the close or a written override, with an expiry date, from the risk function's delegated approver; anything open for three days escalates to the desk head and the chief risk officer's office.*

Two rows carry earlier ideas. *Days to liquidate* is the 13-day model, sibling to the 13-week one, as Theo put it when he added a second file to the USB stick: a position of $q$ dollars in a bond trading $\text{ADV}$ a day, sold at participation $\kappa$, takes $q/(\kappa\,\text{ADV})$ days to exit, which bounds the forced-seller problem of §16.2 from the desk's own side. *Share of an issue* is the concentration limit the Whale lacked, and it bounds something no volatility measures: whether the desk *is* the market in a bond, in which case the mark is its own opinion and the exit a negotiation.

Early in the project ROBO had been asked to "set sensible limits." It set every line to the book's current exposure plus one dollar, sensible in that the book was inside every limit at the moment of setting, and put the desk in breach on eleven lines by 9:32 a.m. the next day.

The committee's first question that Monday was the one every risk committee asks. "Why is the ten-day ES 11% higher than on Friday, when the desk sold bonds on Friday?" The model's change report had the answer at 7:30. On Friday evening one agency had finished a sector review of building products and downgraded twelve issuers, and the desk's rating convention (the middle of three agency ratings) had moved forty bonds from the B cells to the CCC cells, each with a larger cell sensitivity, a higher idiosyncratic bucket and a tighter JTD limit. Nothing had traded. The same bonds now meant something different, the DTS loading of §8B.2 working as designed. The committee chair wrote one word on her pad, which Theo later learned was *good*.

![Figure 8-B.5: Tuesday's risk report grown into the limit sheet: each line's exposure against its soft and hard thresholds, with the three breaches of the cold open marked and the forty-bond migration shown as the before-and-after change in the CCC cells. Illustrative.](assets/figures/ch08b_limit_sheet.png)

*Builds on:* §4B.5 (CS01 and DV01), §16.2 (forced sellers), §21.4 (the OC test as a limit), §28.5 (days-to-liquidate). *Used in:* §28.9 (the dashboard's risk-versus-limits panel), Chapter 3-B (the 7:30 risk pack), Chapter 8-C.

## 8B.10 When to Apply It, and When It Breaks

A factor risk model is at its best on ordinary days in a many-issuer book, saying where the risk is and catching concentrations built by accident. It is at its worst on the days it is most needed, and a seasoned risk manager reads it with four suspicions.

The first is that correlations are regimes. The rate–spread correlation $\rho_{y,s}$ changed sign twice between 2021 and 2025 (§8.2, §8.7), and twice more in seven sessions of April 2025, so the engine takes it as a regime input from the hidden Markov model of §12.4; where §12.5's multi-asset covariance holds it at zero, this engine supplies the regime value. The second is that correlations rise together in exactly the stress the model was built for, which is why the stress library shocks factors jointly rather than trusting the covariance.

> **View From Another Seat.** *The dealer in March 2020.* A dealer's risk system sees the same failure from the other side of the trade. Describing March 2020 to analysts, Morgan Stanley's then chief financial officer said: "Historical relationships broke down and liquidity dried up. Clients reacted by reducing risk and raising cash" (Morgan Stanley first-quarter 2020 earnings call, 16 Apr 2020). For a dealer, broken relationships mean hedges that do not hedge and inventory that will not sell at the mark; for a buy-side desk, they mean a covariance estimated on calm years describes a market that has, for now, stopped existing.

The third suspicion is about inputs. Stale marks understate volatility, so the de-smoothing of §8.5 and §12.5 is part of the model, not an option. And the model is only as good as the security master (§27.3) and the corporate-actions handling of the tidy bond panel (Appendix B, §B.16): a bond exchanged, tendered or called but still in the master at its old terms carries a loading, a DTS and a JTD for a claim that no longer exists.

The fourth is numerical. A sixty-factor covariance can be nearly singular, and an optimizer fed one will find enormous positions the matrix believes are riskless.

> **Math, Gently.** *The condition number: how close a matrix is to dividing by zero.* A covariance matrix stretches some directions and squashes others; the condition number is the ratio of the largest stretch to the smallest. At 10, every direction is about equally well measured. At 10 million, some combination of factors looks almost riskless, usually because the data cannot tell two factors apart, and anything that inverts the matrix leans on that combination hard. Tiny example: two factors with correlation 0.999 give a two-by-two correlation matrix with condition number $(1+0.999)/(1-0.999) \approx 2{,}000$. The engine raises an alarm above a threshold and shrinks harder (§7-B.5).

Finally, the hedges have a band. A KRD or CDX hedge rebalanced on every wiggle pays the bid–offer all day; one never rebalanced lets the mismatch become risk. Suppose the mismatch $x$ drifts like a random walk with variance rate $s^2$, trading costs $c$ per unit, and holding the mismatch costs the desk $\tfrac{\gamma}{2}x^2$ per unit time. Then the cheapest policy leaves $x$ alone inside a band $[-b, b]$ and trades only at its edges. Inside the band the mismatch spends equal time everywhere, so its average squared size is $b^2/3$; pushing it back at the edges costs about $c\,s^2/(2b)$ per unit time. Minimizing $\gamma b^2/6 + c\,s^2/(2b)$ gives

$$
b^{*} = \left(\frac{3\,c\,s^{2}}{2\,\gamma}\right)^{1/3}.
$$

Since $\gamma$ is risk aversion times the variance of the factor being hedged, costly hedges get wide bands and hedges against volatile factors get narrow ones, and both only by the cube root: halving the cost narrows the band by about a fifth. That is the band in the KRD row of Table 8-B.4, and the derivation in hedge-matrix form belongs with §8.6.

> **Trend Watch.** *The volume inputs moved in 2026.* A volume-based liquidity factor rests on series that changed definition this year. In its second-quarter 2026 release of 30 July 2026, published as ICE agreed to acquire it for \$167 a share in cash (an equity value of about \$6.0bn), MarketAxess said it was "suspending its practice of issuing monthly volumes press releases" (MarketAxess Q2-2026 release, pp. 4–5, 9; ICE 8-K, Exhibit 99.1). FINRA's affiliate-principal indicator, voluntary from 31 August 2026 and mandatory from 2 August 2027, suppresses the inter-affiliate leg of qualifying trades from dissemination (FINRA Regulatory Notice 26-16, 26 Aug 2026); FINRA's own baseline put such trades at up to about 5.7% of 2025 transactions, counted by trades rather than dollars (SR-FINRA-2026-009, pp. 19–21). Tradeweb's September 2026 report said the change lowered reported US high-grade TRACE volumes and that prior periods were not restated. *What it means for the desk:* volume-based liquidity and days-to-liquidate inputs carry a structural break at 31 August 2026, and platform series do not splice across it.

*Builds on:* §8.2, §8.6, §8.7, §12.4–§12.5, §27.3, Appendix B §B.16. *Used in:* §9.8 (the optimizer's covariance guard), §12.5.

## 8B.11 The Risk Model Engine

### Specification for AI Implementation

By now the desk has every piece of the model on paper and has watched each piece fail once: a bucket read from a stale field, a basis invented by a clock, a jump folded into a variance, a half-life retuned on its own exceptions. The engine exists to make those failures hard to repeat. Chapter 8-C's explain, the optimizer of §9.8, the MAC covariance of §12.5, the basket of §19.5 and the dashboard of §28.9 all import it, so the number in the risk pack and the number behind a trade are the same number.

ROBO's version of "keep risk under the limit" is in the cold open. The precise version reads like a covenant package, because it is one. The inputs are five tables. *Positions*: instrument, issuer, face, price as a fraction of par and its provenance (trade, quote or evaluation, §27.2), rating, rating × sector cell, DTS, key-rate durations and price bucket. *Factor returns*: a dated panel, oldest first, every column snapped at 3:00 p.m. New York. *Loadings inputs*: cell sensitivities, and Dimson loadings on the liquidity, residual and basis factors, own or inherited. *Idiosyncratic volatilities* by rating and price bucket, in points. *JTD legs*: for each instrument, its default loss as a constant plus a slope on recovery, with Beta parameters under $\mathbb{P}$. The outputs are the factor and idiosyncratic split, the issuer JTD list, VaR and ES at one and ten days on the mixture with Monte Carlo standard errors, two-column stress results, the backtest statistics and the limit sheet marked ok, soft or hard.

Four design choices carry the chapter's argument. The jump layer is simulated and added to Gaussian draws path by path, and no function returns a Gaussian variance with default inside it. An issuer's legs share one uniform draw pushed through each leg's Beta, so the notes and the CDS on them recover alike and a loan recovers more in the same states; this comonotone shortcut is cruder than a waterfall over simulated enterprise value (Chapter 12-C) and is the first place to upgrade. The price bucket has hysteresis. And the engine refuses rather than guesses: mismatched snaps, a sub-80 bond without an equity loading, a bond with no loading and no fallback, or an ill-conditioned covariance all raise an error.

The engine suits a many-issuer book marked daily. For a book of five distressed claims the jump layer is the whole model, the plan-value engine of Chapter 12-C does the work, and this module only aggregates. The edge case that bites is the thin tail sample: an issuer with a 0.1% one-day default probability defaults on about a hundred paths in a hundred thousand, and an ES that moves 10% between seeds is reporting its own noise, which is why the standard error is printed beside it.

*The full python listing is [Listing 8-B.1 in Appendix F](#code-8b-1).*

## 8B.12 Desk Debrief

A week after Fourteen-Sigma Tuesday the desk held its post-mortem in the small conference room with the broken blind. The breach had been real. The model's sigma had been wrong for a reason that fit on an index card: Halvorsen had crossed 80, the bucket had been read from a monthly field, and the loading had not switched. The JTD line had been right all along, because someone who read the 8-K had moved it. ROBO's orders, cancelled at 7:34, now hang framed above the coffee machine with the caption *flat all day*. Theo wrote the week up the way he once wrote up first-day hearings, and the desk taped it to his monitor.

- A migration moves risk when nothing trades, because DTS is the unit and the cell is part of the loading. [L3]
- Default is an event, not a large move: it lives in its own layer, in $\mathbb{P}$, with its own distribution and its own limit, and it is charged once. [L4] [L6]
- Below 80 the bond is a different claim, so the model changes regime rather than volatility.
- Risk and P&L share one snap, or the basis they report is a clock. [L9]
- A model has an exception rate; the desk counts it, and changes the model through a review rather than inside the drawdown that produced the exceptions. [L12]
- A limit is a conversation with a timestamp, and a breach that lasts seventy-one days has quietly become the limit. [L11]

Mags initialled the list and added a line in pencil: *IDO or it didn't happen, and risk or it didn't count.* Then she went to lunch, which on this desk no longer stops the risk model.

### The Spec You Hand the Robot

"Implement `risk_model.py` per §8B.11. Units: \$mm, decimals, years. One snap, 15:00 America/New_York, checked on every input. Loadings: −KRD on key rates, −DTS × cell sensitivity on spread cells, estimated loadings own → issuer (DTS-rescaled) → cell → raise. Equity regime below 80, exit above 85. EWMA covariance, shrunk, with a condition-number alarm. Idiosyncratic variance by rating × price bucket. Jump layer: issuer JTD legs, Beta recoveries under $\mathbb{P}$, comonotone within issuer, added path by path and never to a variance. VaR and ES at 1 and 10 days on the mixture, with standard errors. Two-column stress. Kupiec and Christoffersen. Limit sheet, soft and hard. All listed self-checks pass."

### Exercises

1. *(Quadrature, in DTS.)* Two \$10mm positions have DTS of 0.04 and 0.09 (400 and 900 bp-years), the relative spread volatility is 8.8% a month (§8.4), and the correlation is 0.6. What is the pair's monthly volatility, and what share of it does the riskier bond own? *Solution:* stand-alone volatilities are \$35.2k and \$79.2k; the pair's is $\sqrt{35.2^2 + 79.2^2 + 2(0.6)(35.2)(79.2)} \approx \$104.2$k, against \$114.4k at perfect correlation. Check: by Euler, the DTS-0.09 bond contributes $(79.2^2 + 0.6 \times 35.2 \times 79.2)/104.2 \approx \$76$k, about 73%.
2. *(The square root of ten.)* A book has a one-day Gaussian volatility of \$1mm and one issuer with a fixed JTD of \$8mm and a one-day default probability of 0.2%. Compute the one-day and ten-day 99% ES on the mixture and compare with $\sqrt{10}$ times the one-day number. *Solution:* about \$3.79mm and \$10.83mm; the shortcut gives \$11.99mm, an overstatement, where Table 8-B.2's larger jump gave an understatement. Check: the sign of the error depends on the jump's size relative to the Gaussian layer.
3. *(Kupiec.)* Run the proportion-of-failures test on seven exceptions in 250 days at 99%. *Solution:* $\text{LR}_{\text{POF}} = 5.50$, which rejects at 5% (3.84) and not at 1% (6.63). Check: the yellow zone of Basel's traffic light.
4. *(Christoffersen.)* The same seven exceptions arrive on seven isolated days. Is the model still rejected? *Solution:* $n_{00} = 235$, $n_{01} = n_{10} = 7$, $n_{11} = 0$, and $\text{LR}_{\text{ind}} \approx 0.41$, so independence is not rejected; $\text{LR}_{\text{cc}} \approx 5.90$ sits just below the $\chi^2_2$ 5% value of 5.99. Check: the count fails the model at 5% and the timing does not, which is why the tests are read together.
5. *(The Halvorsen book.)* The desk owns \$12mm of Halvorsen's 7.25% notes at 78 (mean recovery 15%) and \$6mm of a junior Halvorsen note at 31 (mean recovery 5%), the issuer whose bankruptcy §12B.9 follows. Halvorsen is downgraded to CCC. Which line of Table 8-B.4 binds, and how much JTD has to go? *Solution:* JTD is $12(0.78 - 0.15) + 6(0.31 - 0.05) = 7.56 + 1.56 = \$9.12$mm, above the single-B hard limit of 9.0 and far above the CCC hard limit of 5.5. Reaching 5.5 means shedding \$3.62mm of JTD, for example about \$5.75mm face of the 7.25% notes at 0.63 of JTD per dollar of face. Check: the downgrade moved the limit, not the exposure; the binding constraint is the jump.
6. *(ROBO, again.)* Rewrite "keep risk under the limit" in one sentence so that ROBO's 9:31-and-3:59 plan stops being a solution. *Solution:* one version is "Hold the 1-day 99% ES on the mixture, computed on end-of-day positions at the 15:00 New York snap and monitored intraday on the same definition, below \$2.5mm soft and \$3.0mm hard, reducing by the trades of least expected cost; round trips within a day count at their cost and leave the end-of-day position unchanged." Check: it names the measure, horizon, snap, threshold and cost of compliance.

### Deep-Dive Resource Graph

**Podcasts**
- *Odd Lots*, "How the Hottest Hedge Funds on Wall Street Really Manage Risk" (25 Jul 2024). https://omny.fm/shows/odd-lots/how-the-hottest-hedge-funds-on-wall-street-really. Pod-shop risk limits in practice.
- *Odd Lots*, "The Math That Explains How Multi-Strategy Hedge Funds Make Money," with Dan Morillo (7 Oct 2024). https://omny.fm/shows/odd-lots/100724-odd-lots-dan-morillo-master. Crowding, factor neutrality and capacity.
- *Odd Lots*, "Giuseppe Paleologo on Quant Investing at Multi-Strat Hedge Funds" (21 Jun 2025). https://omny.fm/shows/odd-lots/giuseppe-paleologo-on-quant-investing-at-multi-strat-hedge-funds. Companion to the Paleologo text quoted in §8B.2.
- *Flirting with Models*, "Giuseppe Paleologo – Multi-Manager Hedge Funds & Thinking Deeply About Simple Things (S7E11)" (2 Sep 2024). https://www.flirtingwithmodels.com/episodes/l2l3xUqwZbz. Factor models in hedging, at a technical level.
- *Flirting with Models*, "Jeff Rosenberg – The Past, Present, and Future of Systematic Fixed Income (S7E19)" (18 Aug 2025). https://www.flirtingwithmodels.com/episodes/8V74zBaN4jN. Why credit factors are characteristic-specific: the DTS-loading argument from a practitioner.

**Practitioner Writing**
- US Senate Permanent Subcommittee on Investigations, *JPMorgan Chase Whale Trades: A Case History of Derivatives Risks and Abuses*, staff report (15 Mar 2013). https://www.hsgac.senate.gov/wp-content/uploads/imo/media/doc/REPORT%20-%20JPMorgan%20Chase%20Whale%20Trades%20(3-15-13).pdf. The case study of §8B.9, and the best public account of a credit-derivatives risk process under stress.
- Robeco (van Leeuwen, Penninga and Houweling), "Duration Times Spread: measuring credit risk" (2 Sep 2024). https://www.robeco.com/en-uk/insights/2024/09/duration-times-spread-measuring-credit-risk. The originators on DTS.
- Paleologo, *Advanced Portfolio Management* (Wiley, 2021), Chapter 7 on managing factor risk and setting limits.

**Academic Papers**
- Kupiec, P. (1995), "Techniques for Verifying the Accuracy of Risk Measurement Models," *Journal of Derivatives* 3(2).
- Christoffersen, P. (1998), "Evaluating Interval Forecasts," *International Economic Review* 39(4).
- Collin-Dufresne, P., R. Goldstein and J. S. Martin (2001), "The Determinants of Credit Spread Changes," *Journal of Finance* 56(6).
- Dimson, E. (1979), "Risk Measurement When Shares Are Subject to Infrequent Trading," *Journal of Financial Economics* 7(2).
- Ledoit, O. and M. Wolf (2004), "Honey, I Shrunk the Sample Covariance Matrix," *Journal of Portfolio Management* 30(4).
- Whalley, A. E. and P. Wilmott (1997), "An Asymptotic Analysis of an Optimal Hedging Model for Option Pricing with Transaction Costs," *Mathematical Finance* 7(3).

**Data & Code**
- FRED: ICE BofA US High Yield OAS (https://fred.stlouisfed.org/series/BAMLH0A0HYM2), CCC & Lower OAS (https://fred.stlouisfed.org/series/BAMLH0A3HYC), Moody's Baa minus 10-year (https://fred.stlouisfed.org/series/BAA10Y) and the 10-year Treasury (https://fred.stlouisfed.org/series/DGS10). The ICE series on FRED carry only the most recent three years of history, so pre-2023 scenario levels come from the canonical sections or from BAA10Y.
- FINRA, SR-FINRA-2026-009 (Apr 2026), the affiliate-principal baseline. https://www.finra.org/sites/default/files/2026-04/SR-FINRA-2026-009.pdf.
- `risk_model.py` (this chapter, Appendix F and `book_src/lib/`), with `creditstats.py` (§7-B.10) for the Ledoit–Wolf weight and Monte Carlo standard errors.

<!-- STATUS: COMPLETE -->
