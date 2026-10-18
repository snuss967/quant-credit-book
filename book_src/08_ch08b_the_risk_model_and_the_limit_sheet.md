# Chapter 8-B: The Risk Model You Run Every Morning: Factors, Idiosyncratic Variance, Jump-to-Default, Stress and the Limit Sheet

> **Prerequisites.** Chapter 4-B for DV01, key-rate durations and CS01; Chapter 7-B for EWMA, Ledoit–Wolf shrinkage, PCA, the bootstrap and Monte Carlo standard errors; §8.1–§8.8 for the return decomposition, the sub-80 discontinuity (§8.3), DTS (§8.4), Dimson betas (§8.5), the hedge matrix (§8.6) and the common residual (§8.8); §5.5 for Beta recoveries by seniority; §12.5 for the DTS-structured covariance and desmoothing; §24.3 for $N^{\text{JTD}}$. Nothing here is new mathematics. What is new is that the pieces finally sit in one engine that runs at 7:30 every morning and is graded by its own backtest.

*Builds on:* §5.1.4 (the first Fourteen-Sigma Tuesday), §5.5, §6.8 and §11.4 ($\lambda^{\mathbb{P}}$), §8.1–§8.8, §12.4–§12.5, §24.3, §28.2, §28.5. *Used in:* Chapter 8-C (the morning explain imports `risk_model.py`), §9.8 (the optimizer's covariance), §12.5 (the regime correlation), §19.5 (the basket residual covariance becomes a special case), §28.5 and §28.9 (the risk-versus-limits panel of the PM dashboard).

## Cold Open: Fourteen-Sigma Tuesday, the Sequel

The e-mail arrives at 7:31 a.m., one minute after the risk pack, in the capital letters that compliance software reserves for weather warnings and limit breaches.

*LIMIT BREACH (3). Issuer JTD top-10: HALVORSEN BUILDING PRODUCTS, SOFT. DTS, B-rated Industrials: HARD. ES 1d 99%: SOFT.*

Theo reads it twice, the way he once read a notice of default from an agent bank. On Friday the Halvorsen 7.25% notes due 2029 had been 92. On Monday, after a lender call that half the street was on and the desk was not, they opened at 78 (Chapter 1). The desk still owned \$12mm face of them. That was one bad day, already lived through and already explained. What Theo cannot see is why a bond that did nothing new overnight has now set off three alarms.

Kaz is already at the whiteboard, which is a bad sign before eight. "The model called Monday a fourteen-sigma move," they say. "The one-day standard deviation on the position was a point. The bond fell fourteen. So either we saw the rarest event since the Cambrian or—"

"Or your model has the wrong sigma," Ines says, without taking off her coat. She sets her coffee on Theo's desk like a chip on the felt. "Fine. Which line do we cut, and what's the pot if we're wrong about which line?"

Mags arrives last, reading glasses on her head and a printout of the risk pack in her hand, because she does not trust a number she cannot fold. "Three breaches. Two soft, one hard." She taps the second line. "A limit is something you breach politely, in writing, before lunch. I told you that your first week. The hard one is the exception. That one you fix before you finish your coffee, or you explain it to the risk committee after theirs."

There is a fourth item in Theo's inbox, timestamped 2:14 a.m. Someone on the overnight desk had asked ROBO to "keep risk under the limit." ROBO had obliged. It has drafted orders to sell all 2,000 lines of the book at 9:31 a.m. and buy every one of them back at 3:59 p.m. Its note explains, correctly, that the intraday limit monitor runs from 9:30 to 4:00, so the book will be inside every limit for the entire period in which anyone is checking. Estimated round-trip cost: 1.9 points on the whole portfolio. "Flat all day," Kaz reads aloud. "Bankrupt by Thursday."

Theo is not looking at ROBO's orders. He is looking at the JTD line, because he recognizes the number. On Monday night he read the issuer's 8-K, saw that the new-money financing being discussed on the lender call would sit in a subsidiary that held the company's patents, and cut his recovery assumption for the notes from 40 cents to 15. He typed it into the recovery table at 11:40 p.m. and went to bed feeling diligent. The price had fallen fourteen points. His recovery had fallen twenty-five. Jump-to-default, the loss if Halvorsen defaulted tomorrow, had gone *up*.

"I did that one," he says.

"Good," says Ines. "Then that's the one line on this page you understand. Now explain the other two."

Which raises the question this chapter answers. **What is the number on the risk report supposed to be, and what do you do when it is wrong?**

By the end of the chapter Theo will have built the model that produced that e-mail, piece by piece, and found the bug in it. He will be able to say what a factor is in a credit book and why its loadings are measured in DTS. He will know why a bond that has fallen below 80 needs a different model rather than a bigger volatility, why default lives in its own layer with its own distribution, and how expected shortfall is computed on the mixture of the two. He will be able to write a stress scenario as a set of factor shocks rather than a story, count the model's own failures and tell whether they are bad luck, and read a limit sheet as what it really is: a contract between the model and the people who are allowed to overrule it.

## 8B.1 What the Model Is For

At Theo's old firm the thirteen-week cash flow model had one job. It said how much cash could go wrong before the next re-forecast, and it was judged, brutally, by what actually happened in week four. Nobody expected it to say whether the company was a good investment. It answered a narrower and more useful question: *how much room do we have, and where will we run out first?*

The risk model is the same animal wearing a different suit. It is a forecast of how much the book could lose before the next morning's re-forecast, with three questions attached. *How much* could we lose, on a normal bad day and on a very bad one? *Where* would it come from: rates, a sector, one issuer, a hedge that stops hedging? And *what would we do about it*: which line on the limit sheet is the binding one, and who gets the phone call? There is a fourth question that people keep trying to ask it, which is whether the book will make money. The risk model has no opinion. Its expected return is zero by construction, and the desk that reads a falling risk number as good news has confused the thermometer with the weather.

"In my day," Mags says, "the risk report was a man named Gerry who walked over to your desk around four and asked if you were sure." She considers this. "Gerry had a very good backtest. He was wrong about once a year and he always told you which year."

What Gerry carried in his head, and what the model has to carry in matrices, is the single fact that makes portfolio risk different from the sum of position risks.

> **Math, Gently.** *Variance adds in quadrature, and correlation decides how much.* A standard deviation is the typical size of a day's move, measured in dollars. Variance is its square. The useful fact is that when two positions move independently, their *variances* add, not their standard deviations: two independent positions with daily standard deviations of \$60k and \$80k combine to $\sqrt{60^2 + 80^2} = \$100$k, not \$140k. This is Pythagoras, which is why risk people say risks add "in quadrature": the two risks are the sides of a right triangle and the portfolio is the hypotenuse. Correlation, $\rho$, measures how much the two positions move together, on a scale from $-1$ to $+1$, and it bends the triangle. The general rule for two positions is
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

With $n = 2{,}000$ and an average correlation of only 0.025, that is $2{,}000/(1 + 1{,}999 \times 0.025) \approx 39$. Two thousand lines, forty hands. Section 28.2 arrives at the same forty from the issuer column, and Ines would say it more simply: you are playing forty hands, and most of what you think of as your other 1,960 are the same hands dealt again. A risk model that cannot see the shared part will report a book that looks as diversified as a phone book and behaves like forty concentrated positions.

The same arithmetic tells the desk where the risk lives. Portfolio volatility can be split exactly into contributions from each position, because volatility is what mathematicians call homogeneous of degree one: double every position and the volatility doubles.

> **Math, Gently.** *Who owns the risk? Marginal contribution, by Euler.* Ask how much the book's volatility would rise if one position grew by a dollar. That is the marginal contribution, $\partial\sigma_p/\partial w_i = (\Sigma w)_i/\sigma_p$, where $(\Sigma w)_i$ is position $i$'s covariance with the whole book. Multiply each marginal contribution by the position's size and the pieces add up exactly to $\sigma_p$, a theorem Euler proved two centuries before anyone owned a bond. In the two-bond book at $\rho = 0.6$, A contributes $(3{,}600 + 2{,}880)/125.5 \approx \$52$k and B contributes $(6{,}400 + 2{,}880)/125.5 \approx \$74$k, which sum to the \$126k total. B owns 59% of the risk with 50% of the capital, because it is the more volatile of two positions that move together. The full version, by factor and by issuer, is the first table of the risk pack and the input to §9.8's optimizer.

That first table, contributions by factor and by issuer, is what the risk committee reads first, and it is what made Theo's breach e-mail legible once he knew how to read it. But a contribution table is only as good as the covariance behind it, and a covariance for 2,000 bonds is four million numbers, most of them unknowable from the data a credit desk has. The way out is the same way out the restructuring banker uses when a capital structure has forty instruments: notice that most of them are claims on the same few things.

## 8B.2 The Factor Taxonomy

Kaz draws the tree on the whiteboard on Tuesday afternoon, after the breaches have been explained to everyone's partial satisfaction. It has five branches, and Theo, who has drawn a thousand organization charts of holding companies and their guarantor subsidiaries, recognizes the shape before Kaz labels it.

"Every bond on the desk is a claim on five things," Kaz says. "Rates, spread, liquidity, whatever the market as a whole is doing that our spread factors missed, and the hedges' own idea of the price. Then there's the part that belongs to the bond alone." They write *IDO?* next to the last box and then, after a look from Ines, cross out the question mark and write *residual*. "We find out later whether any of it is IDO."

The first branch is the one Theo already knows from Chapter 4-B. A bond's price moves when Treasury yields move, and a single duration number hides which part of the curve it is exposed to. The risk model carries **key-rate DV01s**: the price change for a one-basis-point move in the 2-, 5-, 10- and 30-year points of the curve, with the curve interpolated between them. A 2029 note and a 2034 note with the same modified duration can hedge each other on a parallel shift and lose money together on a steepener, and the key rates are what notice.

The second branch is where credit lives. The model groups bonds into **rating × sector cells** (B-rated Industrials, BB Energy, CCC Retail, and so on) and gives each cell a factor return: the cell's common *relative* spread change for the day. The loading of a bond on its cell's factor is not estimated bond by bond. It is the bond's DTS, duration times spread (§8.4), multiplied by a cell-level sensitivity estimated from the whole panel. The reason is Ben Dor's regularity that spread volatility is proportional to the spread itself, so a bond's excess-return volatility is proportional to DTS. A bond with twice the DTS of its neighbour has twice the exposure to the same sector shock, whatever its own short and patchy price history says.

The third branch is **liquidity**: a factor built from day-to-day changes in liquidity cost scores, so that a morning when every dealer widens its bid–offer at once shows up as one shock rather than as two thousand small idiosyncratic surprises. The fourth is the factor that §8.8 found hiding in the residuals. Collin-Dufresne, Goldstein and Martin showed in 2001 that most of what structural variables could not explain about spread changes was a single common component, and §8.8 removed it as the first principal component of the residual panel. Here it is promoted from a statistical cleanup step to a **named factor** with its own row in the covariance and its own line in the explain, so that when it moves, the morning meeting can call it something other than "idiosyncratic, all of it, in the same direction." The fifth branch is **basis**: CDX index versus its cash constituents, the high-yield ETFs versus their net asset value, Treasury futures versus the cash curve. These are the factors that only exist because the desk hedges, and they are the ones that bite when the hedge decides to be a separate asset for a week (§8.6, Chapter 20).

![Figure 8-B.1: The factor tree for a cash-and-derivatives credit book, with Tuesday's exposures marked on each branch: key-rate DV01s, rating × sector spread cells in DTS units, the liquidity factor, the common residual and the basis factors, with issuer residuals and the jump layer drawn as separate leaves. Illustrative book.](assets/figures/ch08b_factor_tree.png)

Put together, a bond's daily return in the model reads

$$
r_{i,t} = -\sum_{m} \text{KRD}_{i,m}\,\Delta y_{m,t} \;-\; \text{DTS}_i \sum_{k} b_{g(i),k}\,F_{k,t} \;+\; \beta^{L}_{i}\,F^{L}_{t} \;+\; \beta^{C}_{i}\,F^{C}_{t} \;+\; \sum_{j} \beta^{B}_{i,j}\,F^{B}_{j,t} \;+\; \epsilon_{i,t}.
$$

Here $\text{KRD}_{i,m}$ is bond $i$'s key-rate duration at curve point $m$ and $\Delta y_{m,t}$ the yield change at that point; $g(i)$ is the bond's rating × sector cell; $F_{k,t}$ is spread factor $k$'s relative spread change ($\Delta s/s$, a decimal); $b_{g,k}$ is the sensitivity of cell $g$ to factor $k$, which is 1 for a bond's own cell and something smaller for neighbouring cells when the model allows spillovers; $F^{L}$, $F^{C}$ and $F^{B}_{j}$ are the liquidity factor, the common residual and the basis factors, with their loadings $\beta$; and $\epsilon_{i,t}$ is whatever is left. The minus signs are the bond-math signs: yields up and spreads wider both lose money for a long position.

> **Math, Gently.** *A factor model is a regression that every bond shares.* Imagine forty bonds in the same building, each with its own apartment, all connected to one heating system. On a cold night every apartment cools; some cool more because they have more windows. A factor model says exactly this: each bond's return is a few shared shocks (the heating system, the cold front) multiplied by how exposed that bond is to each (its windows), plus a bit that is the bond's own business (someone left a window open). The shared shocks are the *factor returns* $F_{k,t}$; the exposures are the *loadings* $\beta_{i,k}$; the leftover is the *idiosyncratic return* $\epsilon_{i,t}$. Tiny example: if B-rated Industrials widen 5% in relative terms overnight ($F = 0.05$), a bond with DTS of 0.20 loses about $0.20 \times 0.05 = 1\%$ from the factor alone, and a bond with DTS 0.08 in the same cell loses 0.4%. The payoff for the modeller is that the covariance of 2,000 bonds is now the covariance of perhaps sixty factors, plus 2,000 separate leftover variances, which is a problem that a few years of data can actually answer. The full version is §7-B.5.

The covariance matrix follows directly. Stack the loadings into an $n \times K$ matrix $B$, write $\Sigma_F$ for the $K \times K$ covariance of the factor returns and $\Omega$ for the diagonal matrix of idiosyncratic variances. (The letter $D$, which many risk texts use here, is reserved for duration in this book, hence $\Omega$.) Then

$$
\Sigma = B\,\Sigma_F\,B^{\top} + \Omega, \qquad \sigma_p^2 = w^{\top}\Sigma\,w = \underbrace{(B^{\top}w)^{\top}\,\Sigma_F\,(B^{\top}w)}_{\text{factor}} + \underbrace{w^{\top}\Omega\, w}_{\text{idiosyncratic}} .
$$

The vector $B^{\top}w$ is the book's exposure to each factor, so the first term is the factor risk and the second the risk that diversifies away as positions multiply. The split is the first table of the risk pack, and it is the same split that the restructuring banker makes without equations when he says that a sector-wide sell-off and a bad quarter at one company are different problems with different fixes.

> **[SOURCE EXTRACTION]** *Paleologo_Advanced_Portfolio_Management p.111:* "Factor PnL is the sum of all the individual factor PnLs; each factor PnL is the product of factor exposure and factor return; and each factor exposure is the sumproduct of loadings and position NMVs."
>
> **Annotation.** Our analysis: Paleologo writes for an equity book, where loadings are estimated characteristics and positions are net market values. The credit translation changes one word and one unit. The word is *DTS*: in a credit book the natural loading on a spread factor is the bond's DTS times a cell sensitivity, so the "sumproduct" is a DTS-weighted sum of market values, and it moves when a bond's spread or rating moves even if no position changes. The unit is relative spread change rather than return. The sentence also explains why the morning explain of Chapter 8-C and this chapter's risk pack have to share their loadings: the same sumproduct that forecasts tomorrow's risk is the one that explains yesterday's P&L.

The DTS loading carries a consequence that surprised Theo more than anything else on the tree. Because the loading is $\text{DTS}_i\,b_{g(i),k}$, two things move a bond's risk without any trade. Its spread can widen, which raises DTS, and its rating can change, which moves it to a different cell $g$ with a different sensitivity and a different idiosyncratic bucket. On Tuesday morning both had happened to Halvorsen's neighbours. The whole B-rated Industrials cell had widened on Monday in sympathy, every bond's DTS had risen with its spread, and the cell's DTS exposure, which had been comfortably inside its limit on Friday, was now over the hard line without the desk having bought a bond. That was breach number two. It was not a modelling error. It was the model doing the one thing Theo had not expected a risk model to do, which was to notice that the same bonds had become riskier.

The factor covariance itself, $\Sigma_F$, is estimated from a few years of daily factor returns, with two adjustments that Chapter 7-B derives and this chapter simply uses.

> **Math, Gently.** *EWMA and shrinkage: a memory that fades, and a guess pulled toward common sense.* An exponentially weighted moving average gives yesterday's squared move the most weight, the day before slightly less, and so on, each day's weight shrinking by a constant factor. With a half-life of 60 trading days, a move from three months ago counts half as much as yesterday's; one from a year ago counts about a sixteenth as much. The covariance therefore reacts to a new regime within weeks without forgetting the old one entirely. Shrinkage handles a different problem: with sixty factors and a few hundred days of data, some estimated correlations are noise that happens to look like signal, and the matrix can come out nearly impossible to invert. Ledoit and Wolf's recipe blends the noisy estimate with a simple, stable target (for instance, the same average correlation everywhere) in a proportion chosen from the data itself. Tiny example: if the sample says two factors have correlation 0.9, the target says 0.3, and the estimated shrinkage weight is 0.25, the model uses $0.75 \times 0.9 + 0.25 \times 0.3 = 0.75$. The full version, including how the weight is estimated, is §7-B.5.

That is the Gaussian half of the risk model, and on a quiet Tuesday it is most of the job. But two of the three breaches in Theo's inbox had nothing to do with whether the factors were right. One came from a bond that had stopped behaving like a bond. The other came from a default that had not happened.
