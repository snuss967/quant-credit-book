# Chapter 8: Stripping Beta to Isolate Pure IDO


## 8.0 Cold Open: Thirty-Seven Cents

*The bond, the afternoon and its headline are illustrative; the desk and everyone on it are fictional.*

At 2:58 p.m. on the Friday before a lender call, Theo's screen showed two numbers that refused to agree. He was long \$40mm of a B3 first-lien secured bond at +620. The 10-year had sold off 18 bp since lunch. The bond was down thirty-seven cents.

"Analytical duration 4.1," Kaz said, without looking up. "You're long \$16,400 of DV01. ROBO is sizing the hedge now. Two hundred thirty-two TY contracts, short."

"The bond only lost thirty-seven cents," Theo said. "Your duration says it should have lost seventy."

"Then it outperformed. That's alpha." Kaz kept typing. "Congratulations."

Ines rolled her chair over, holding a coffee she had clearly been nursing since the open. "What's the pot? If rates are selling off because the data says growth is fine, this bond tightens. Short two hundred thirty-two futures against it and your Treasury hedge isn't a hedge. It's a second position, with worse liquidity than the first one had at 9 a.m."

"So I hedge less?"

"So you find out how much this bond actually cares about rates before you sell something to protect yourself from them."

From across the aisle, without turning around, Mags said: "In '94 the desk I joined two years later hedged its B paper by buying the long bond. Flight to quality, they were told. Lost on both. By phone. They were still paying for it when I got there."

Theo opened his old 13-week cash flow model, the one on the USB stick, the way other people touch a lucky coin. "This thing has a duration of thirteen weeks and an empirical duration of zero. Nothing in it has ever moved with Treasuries."

Kaz lit up. "So it's a CCC bond."

Nobody laughed, mostly because it was correct.

It was Theo's fourth Friday on the desk, and he had learned one thing about the place for certain: when two numbers disagree, somebody has a reconciliation, and nobody has read it. At PJT the reconciliation was the sources-and-uses tab, and the person who had not read it was usually the client. Here it was a button in the risk system labeled EXPLAIN, which nobody pressed because the same report arrived by email every evening at 6:40 whether anyone wanted it or not.

He pressed it. Ninety seconds later the email arrived, laid out by someone who had once been shown a spreadsheet and had taken against it:

*HY-FL1 B3 \$40mm. P&L today: −\$148,000 (−37¢). Explained: −\$132,000 (−33¢). Unexplained: −\$16,000 (−4¢).*

The word "Unexplained" was blue and underlined. Theo clicked it. The drill-down page took eleven seconds to load and contained one line, "Residual = Total − Σ(Explained)," and, at the bottom, a view counter that some optimistic engineer had installed when the system went live. It read 1. The 1 was him.

"Four cents," he said. "Who owns four cents?"

"Nobody," Kaz said. "It's the plug. Plugs are orphans by construction."

"At PJT the plug had an owner. Usually me, at two in the morning, before the client call."

"Here it has an owner too," Ines said. She had not rolled her chair back. "You. But four cents is the small problem. The thirty-three cents of 'explained' is the big one, because it was explained with Kaz's duration, and Kaz's duration assumes something about this afternoon that none of us knows." She turned her coffee cup a quarter turn on the desk, the way other people tap a table before a bet. "Serious question, before anybody sells anything. Why did rates sell off since lunch?"

Nobody answered. Kaz looked at the rates screen as if it might volunteer. Mags, across the aisle, said "Hm," which from Mags was a paragraph.

Theo opened the news pane and scrolled from noon. Between 12:00 and 2:58 there was exactly one headline that a bond market could have traded on. At 12:47 a Federal Reserve governor, speaking at a lunch, had said the committee could afford to be patient on further cuts because the economy was "proving resilient."

"There," Kaz said. "Resilient. Growth. The bond tightened nine basis points because growth is good for credit. Rates sold off because growth is bad for bonds. It's one story."

"Or," Ines said, "patient because inflation isn't done. That's a different story, and in that one your bond doesn't tighten on the news. It widens with the ten-year, a month from now, when everyone has read the transcript."

"Or," Mags said, still facing her own screens, "somebody large had to sell ten-years at one o'clock, and the headline is the excuse the tape found afterwards. Happens every week. Nobody writes a book about it."

Theo wrote the three on his notepad as if they were bidders in a process: *growth, inflation, somebody had to sell.* Under growth he wrote "bond tightens: hedge less." Under inflation, "bond widens with rates: hedge more, or hedge the spread." Under the forced seller, "bond doesn't care: hedge the duration, nothing else."

"So the hedge ratio depends on which one it was," he said.

"The hedge ratio *is* which one it was," Ines said. "Kaz's two hundred thirty-two contracts assume the bond moves like a Treasury whatever the reason. A smaller number assumes it was growth. A bigger one assumes inflation. Every number on that screen is somebody's guess about why the ten-year moved, written down as if it were arithmetic."

"The bond tightened," Kaz said. "That's evidence."

"That's the bond. It might have tightened for its own reasons on a day the ten-year sold off for its. You don't get to use the answer to grade the question." She stood up. "Find out what this bond has done on days like this, and on days that only looked like this. Then tell me what you'd short."

Theo looked at the three words on the notepad, then at the four cents nobody owned, then at the thirty-four cents Kaz had already called alpha. He wrote the question on a sticky note and put it on his monitor: *Of the thirty-seven cents this bond moved today, how much was the bond?*

By the end of this chapter you will be able to split a bond's move into the parts you did not choose and the one part you did, to hedge each part with the instrument that actually owns it, and to say what is left precisely enough that a coding agent computes the same number you would.

## 8.1 The Subtraction: Return Decomposition With the Right Signs

Every restructuring banker has built a sources-and-uses table, and every one of them knows the rule: if the columns do not foot, somebody is about to be embarrassed in front of a client. A bond's daily return is a sources-and-uses table for performance. The uses side is one number, the realized total return. The sources side is a list of things you did not choose (Treasury carry, the curve, the rate move, the market's spread move, convexity) and one thing you did: the idiosyncratic residual you were paid to find. The desk calls that residual IDO, and the desk motto, "IDO or it didn't happen," is a statement about accounting before it is a statement about skill. Until the sources foot, you do not know whether you made money or the Federal Reserve made it for you.

### Deriving the decomposition

Kaz's seventy cents came from one number, the 4.1 on the risk screen, and the number has a picture behind it that is worth having before any algebra.

> **Math, Gently.** *A curve, its tangent, and the bend.* Draw the bond's price against its yield and you get a hillside seen from the side: yield runs left to right, price runs up and down, and the ground slopes downhill because a higher yield means a lower price. Stand on the hill at today's yield. Duration is the steepness of the ground under your feet, the slope of the straight line (the *tangent*) that just touches the hill where you stand, quoted per dollar of price. Take a small step to the right and the tangent tells you roughly how far you drop. Convexity is how quickly that steepness changes as you walk. A bond's hillside is bowl-shaped, so the straight line always overstates the fall when yields rise and understates the gain when they drop, and the correction is half the bend times the *square* of the step. Theo's bond has a slope of 4.1 and the afternoon's step was 18 bp: $4.1 \times 0.0018 = 0.74\%$, about seventy cents on a \$95 price. The bend is about 20, so the correction is $\tfrac12 \times 20 \times (0.0018)^2 \approx 0.003\%$, a third of a cent, which is why the table below shows 0. Squares of small numbers are tiny. That is why a straight-line hedge works on a quiet afternoon, and why it stops working on a loud one. The formal version, a second-order Taylor expansion with the yield split into its Treasury and spread parts, is next.

In words, then: a bond's day is carry, minus its duration times the Treasury move, minus its spread duration times the spread move, plus the bend, plus whatever is left. Take away a matched Treasury portfolio and what remains of the credit part is DTS times the *relative* spread change. Take away what the whole market did through a factor model, and only what survives both subtractions has earned the name IDO.

#### The Full Derivation: from Taylor to the excess return

Write the bond's price as a function of its yield and time, $P(y,t)$, and split the yield into a Treasury part and a spread part, $y = y^{\text{TSY}} + s$. For a callable bond read $y$ as the option-adjusted yield and $s$ as the OAS. Over a short interval $\Delta t$ in which the issuer does not default, a second-order Taylor expansion gives

$$
\frac{\Delta P}{P} \approx \frac{1}{P}\frac{\partial P}{\partial t}\,\Delta t + \frac{1}{P}\frac{\partial P}{\partial y}\,\Delta y + \frac{1}{2}\,\frac{1}{P}\frac{\partial^2 P}{\partial y^2}\,(\Delta y)^2 .
$$

Define modified duration $D^{\text{mod}} = -\frac{1}{P}\frac{\partial P}{\partial y}$ and convexity $C = \frac{1}{P}\frac{\partial^2 P}{\partial y^2}$. Add the coupon accrual to the price change to get total return. At an unchanged yield, price pull plus coupon accrual earns the yield, so the time terms collapse to yield carry $y\,\Delta t$ (two parts with two different owners, split in the table below) plus a roll-down term when the curve is sloped. Now split $\Delta y = \Delta y^{\text{TSY}} + \Delta s$ and allow the spread sensitivity to differ from the rate sensitivity. For a fixed-rate bullet they are equal; for a floater, a callable, or a bond trading to a call date they are not. The result is

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

*Assumptions and measure.* The expansion assumes small moves, no default inside $\Delta t$, and option-adjusted durations for callables. The decomposition is accounting and needs no probability measure. Two things built on it do. The *expected* excess return is a $\mathbb{P}$ object, because it is what you forecast. The OAS is a $\mathbb{Q}$-consistent spread, because it is what discounts the bond's cash flows to its price. (The one-sentence version: a $\mathbb{Q}$ spread is the number that makes the discounted cash flows equal today's price, and a $\mathbb{P}$ return is the number you forecast and are later paid, or not paid, on. Chapter 5 and Chapter 6-B own risk-neutral pricing; nothing here needs more than the distinction.) OAS includes compensation for expected default loss, so "the bond yields +620 over Treasuries" is not "the bond is expected to beat Treasuries by 620 bp a year." The gap is the expected loss, and Chapter 5 priced it.

### The thirty-seven cents, itemized

Apply the decomposition to Theo's bond *(illustrative inputs)*: price \$95, $D^{\text{mod}} = 4.1$, $D^{\text{spr}} = 4.0$, yield 11.1%, a coupon of 10% (about what the price, yield and duration imply), one day of 30/360 carry. The 10-year sold off $\Delta y^{\text{TSY}} = +0.0018$, and the bond's OAS tightened 9 bp, $\Delta s = -0.0009$.

| Source | Formula | Return | Cents on \$95 |
| :--- | :--- | ---: | ---: |
| Carry | $y\,\Delta t = 0.111/360$ | +0.031% | +3 |
| *of which coupon accrual (custodian)* | $\dfrac{c\,\Delta t}{0.95} = \dfrac{0.10/360}{0.95}$ | +0.029% | +2.8 |
| *of which pull-to-par (model)* | $y\,\Delta t - \dfrac{c\,\Delta t}{0.95}$ | +0.002% | +0.2 |
| Rates | $-D^{\text{mod}}\Delta y^{\text{TSY}} = -4.1 \times 0.0018$ | −0.738% | −70 |
| Spread | $-D^{\text{spr}}\Delta s = -4.0 \times (-0.0009)$ | +0.360% | +34 |
| Convexity | $\tfrac12 C (\Delta y)^2$, $C \approx 20$ | +0.000% | 0 |
| Residual | plug | −0.043% | −4 |
| **Total** | | **−0.390%** | **−37** |

The two italic lines split the carry row and add back to it. They are not extra sources, and the total foots on the headline rows alone. They are separate because they have different owners. The coupon accrual is a fact: the custodian's records of accrued interest confirm it to the cent, and if the books disagree, someone has misbooked a coupon. Pull-to-par is a forecast: the model's projection of where a discount bond's price drifts if the yield stays where it is, and it is wrong the moment the yield moves. On this bond the forecast is 0.2 of a cent, so folding the two into one carry line costs nothing today. On a bond trading far below par it would not be small, and a missing coupon would hide inside it. Product control keeps the lines apart for that reason. Chapter 8-C does the same split for a whole book every morning, in the meeting where the four cents behind the EXPLAIN button stop being an orphan and become a line somebody is paid to own.

Kaz's "alpha" was the 34 cents of spread tightening. Whether those 9 bp belonged to the bond or to the rate move is Ines's question from the cold open, and §8.8 answers it to the cent.

> **[SOURCE EXTRACTION]** *Ben_Dor p.298:* "Barclays Capital reports excess returns that equal the difference in total return between a bond and a portfolio of hypothetical par Treasury bonds matching the bond's key rate duration exposures."
>
> **Annotation.** This sentence is the industry's definition of the first subtraction, and it carries two hidden choices. First, the hedge is *key-rate* matched, not single-duration matched, so a 30-year bond's excess return is not polluted by 2s10s steepening. Second, the hedge portfolio is *hypothetical*: par Treasuries at each key rate, rebalanced costlessly. A desk that hedges with actual futures earns the index's excess return minus the futures-cash basis, roll costs, and the cheapest-to-deliver switch (§8.6). On a 2026 desk the definition matters for a second reason: the excess-return series you download from an index provider is already a hedged P&L under a hedge you did not choose. Any empirical duration you estimate on *excess* returns is a duration *relative to that hedge*. Estimate $D^{\text{emp}}$ on total returns, then subtract.

> **[SOURCE EXTRACTION]** *Man_2022 p.14:* "ICE BofAML excess returns taken as total returns less key rate duration matched sovereign return."
>
> **Annotation.** Two index families, one convention. That is convenient and slightly dangerous, because it lets people forget that "excess return" is a model output. Asvanunt and Richardson (2017), *The Credit Risk Premium*, make the point that the measured credit premium is biased if the term component is mis-hedged; the definition you choose leaks into every Sharpe ratio built on it. For a systematic desk the operational rule is to store total returns, Treasury key-rate returns, and the hedge weights separately, and to compute excess returns in your own code. Then, when the index provider restates history, your backtest does not silently change its mind.

Kaz keeps the next list taped inside a desk drawer, one item for each morning it has cost somebody.

> **Ways This Blows Up.** (1) *The sign.* $-D\,\Delta y$ has a minus sign. ROBO, given the formula without it, will report that a rate sell-off made the book money, and the P&L explain will foot perfectly because the residual absorbs twice the error. (2) *Units.* $D \cdot \Delta y$ needs $\Delta y$ in decimal. Feed it 18 instead of 0.0018 and a 4-year bond loses 7,200% on a quiet afternoon. Assert $|\Delta y| < 0.05$ per day as a data-error trap. (3) *Yield carry versus OAS carry.* Yield carry belongs to total return and OAS carry to excess return. Mixing them double-counts the Treasury leg, roughly 5% a year in 2026, and hands you a mysterious, very stable "alpha." (4) *Callable HY.* Much of a high-yield index is callable, and a bond priced to a call date has a spread duration set by the call, not the maturity. Some of what looks like OAS carry is the short call decaying. When the bond crosses the call price, duration-to-worst jumps. Any rolling regression that treats that jump as a rate response will invent a structural break.

## 8.2 Empirical vs. Analytical Duration: One Formula, Three Regimes

Analytical duration answers a question nobody asked: what happens to the bond's price if Treasury yields move *and nothing else does*. On a desk, nothing else moving is the one scenario that never occurs. Empirical duration answers the question Ines asked: when yields move, what tends to happen to this bond, given that its spread tends to move too?

The RSSG reader already knows the limit case. A name in restructuring trades on dollar price, and every bond at the same seniority converges to the same recovery regardless of maturity. Its sensitivity to the 10-year is roughly zero. Empirical duration is the continuum between that limit and par.

Ines's instruction at the end of the cold open, find out what this bond has done on days like this, is a request for a cloud of dots and the line through it. Before the algebra, here is what that line is.

> **Math, Gently.** *Why a regression slope equals $\rho\,\sigma_s/\sigma_y$, and what the miss is.* Chapter 1 (§1.4) drew the cloud: one dot per day, and the tilt of the line through it is the bond's empirical answer to a rate move. Here the dot's distance to the right is that day's change in the 10-year yield, and its height is the same day's *relative* change in a B bond's spread (a move from 500 bp to 510 bp is +2%). **Part one, the slope.** The tilt factors into two pieces you can see. How tightly the dots hug a line is the correlation, $\rho$, between −1 and +1. How tall the cloud is relative to how wide is the ratio of the two volatilities, $\sigma_s/\sigma_y$. Multiply them and you have the slope. In the margin, with round numbers: $\rho = -0.5$, $\sigma_s = 2\%$ a day, $\sigma_y = 5$ bp a day, so each 1 bp of yield rise comes with $-0.5 \times 2\% / 5 = -0.2\%$ of relative spread change. A 10 bp sell-off predicts a spread 2% tighter, 10 bp off a 500 bp bond. **Part two, the miss.** No real day sits on the line. On a day the yield rose 10 bp and the spread fell 3%, the line predicted −2%, so the day *missed* by −1%. That vertical miss is the "part orthogonal" that the derivation calls $u_i$. The line is drawn so that the misses have no correlation at all with the yield change; if they had any, you could tilt the line and miss less. So everything in the bond's spread that the 10-year can explain sits on the line, and everything it cannot sits in the miss. Next, the slope becomes a hedge ratio.

### The two-factor derivation

Put the rate leg and the spread leg of §8.1 together, let the spread lean on the yield by the slope in the box, and the fraction of analytical duration worth hedging comes out in one line: $H_i = 1 + s_i\,\rho_{y,s}\,\sigma_s/\sigma_y$. Everything that matters in this chapter is visible in it. The correlation alone decides whether $H$ sits above or below one, because the spread and both volatilities are never negative. The spread level multiplies whatever the correlation says, so the same correlation that shaves 5% off an IG bond's duration can erase a B bond's. And nothing stops the answer from going negative.

Call the slope the *linkage factor*, $\ell \equiv \rho_{y,s}\sigma_s/\sigma_y$, so $H = 1 + \ell s$. Ben Dor's 1998–2009 sample has $\sigma_y = 6.4$ bp a day and relative spread volatilities of 1.6% to 2.5% a day. For B-rated bonds, $\rho = -0.56$ and $\sigma_s \approx 2.2\%$ give $\ell \approx -0.56 \times 0.022/0.00064 \approx -19$ per unit of decimal spread. That is a loss of 0.19 of hedge ratio for every 100 bp of spread, so a B bond at 500 bp has $H \approx 0.03$, and Theo's bond at 620 bp comes out slightly below zero. Under the 1998–2009 parameters, every one of Kaz's 232 contracts was a second position. Under the 2026 parameters in the Trend Watch below, most of them were a hedge. That is the problem.

#### The Full Derivation: the two-factor hedge ratio

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

$H_i$ is the *hedge ratio*: the fraction of analytical duration that minimizes the variance of a Treasury-hedged position. (We write $H$ rather than $h$ because $h$ is reserved for the hedge-weight vector in §8.6.) The three properties stated above the derivation follow by inspection.

*The estimable form.* Theory gives the shape; the numbers come from data. With a panel of bond returns, regress

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

Read the table like a credit agreement: the interesting clauses are the ones that do not say what you expected. The two-factor model predicts the *ordering* well: IG near one, HY near or below zero. The regression intercepts tell a stranger story. Even as spreads go to zero, Ba bonds hedge at 0.41 and Caa at 0.07. A Ba bond at a tight spread is not a distressed instrument, so the recovery route cannot explain why it ignores Treasuries. And the $R^2$ for high yield is 0.01 to 0.06. The rate component of an HY bond's return is not merely small; it is barely there. Figure 8.1 draws the table as lines in spread, which makes the 700 bp comparison visible.

![Figure 8.1: Empirical hedge ratio against spread, by rating. The Baa line stays high (0.71 at 700 bp, the figure Ben Dor quotes) while Ba, B and Caa sit near or below zero at the same spread (+0.06, −0.06, −0.07), so the investment-grade/high-yield line is a break in behavior, not in spread. Source: Ben_Dor p.192, Table 7.1 (Table 8.1 here), H = β + γs; each line stops at the table's H at the maximum sample OAS, with the spread implied by the rounded coefficients; Aaa–Aa and A are omitted because no maximum is reported.](assets/figures/ch08_hedge_ratio_by_rating.png)

> **[SOURCE EXTRACTION]** *Ben_Dor p.191:* "If this correlation is negative, the empirical duration would be lower than the analytical one and may even end up being negative."
>
> **Annotation.** The sentence is conditional, and the condition is the whole game. In Ben Dor's 1998–2009 sample the correlation was reliably negative, because rates mostly moved on growth news and Fed easing, and spreads moved against them. The book treats the sign as a fact about the sample. A 2026 desk must treat it as a state variable. In 2022 the condition failed, $\rho > 0$ and $H > 1$ (§8.7). The formula held. The parameter moved. Any production system that hard-codes $H$ from a pre-2020 table is a 2022 loss waiting for a calendar.

> **[SOURCE EXTRACTION]** *Dynkin p.437:* "When rates fall, bond prices increase. Due to this negative correlation, however, spreads tend to widen, and thus the bond prices do not increase by as much as would have been expected based on analytical duration alone."
>
> **Annotation.** The plain-English version, and the one to read aloud to a PM who asks why the hedged book lost money on a rally. Note the asymmetry the sentence implies for convex payoffs. On a rally, a long credit position under-earns its duration *and* a full Treasury short loses its full duration, so the hedged book bleeds from both sides. The pooled monthly IG regression in the same chapter (Dynkin p.438–439, January 1992 to April 2014, 737,506 bond-months) finds a base hedge ratio of 0.97 that falls by 0.13 per 1% of spread. That is gentler than daily estimates, which is partly the stale-price effect of §8.5 washing out at monthly horizons.

### Three regimes

The formula $H = 1 + s\,\ell$ has one sign switch, so there are three regimes worth naming. Ines names them the way she would name the tables in a card room. "Three tables," she told Theo, tapping the formula on his screen with the cap of a pen. "Flight, nobody, inflation. Find out which one you're sitting at before you buy chips."

The flight table is where Ben Dor's sample sat for eleven years, August 1998 to November 2009, and where the market went back for one week in March 2023 (§8.7). Rates are moved by growth news and by a Fed that eases into trouble, so when spreads widen, yields fall: $\rho < 0$. Then $H < 1$ for everything, and $H \le 0$ for single-B and below. A Treasury short on a high-yield bond at this table is not a hedge but a second bet, and it loses on the days the bond loses.

The nobody table is 2026 so far. Rates and spreads move on unrelated news, $\rho \approx 0$, and $H \approx 1$ even for high yield. Analytical duration is the right hedge by accident, and the desk that uses it looks wise for reasons it did not earn. The FRED computation in the Trend Watch at the end of this section puts 2026 year-to-date here.

The inflation table is 2022. The same news pushes yields up and spreads wider, so $\rho > 0$ and $H > 1$: high yield carries *more* rate sensitivity than its analytical duration, the opposite of what Table 8.1 recommends. The replay in §8.7 sits Theo down at this table with Table 8.1 in his hand.

> **Poker Table.** Ines draws it on a napkin. "Two hands. In the first, you're long a Ba bond because you think spreads tighten when the economy is strong, which is also when rates rise. You hedge at the empirical ratio, $H = 0.4$. Rates rise 50 bp, spreads tighten 30 bp, exactly what the correlation predicted, and the hedge and the bond net to zero. You were right, and you got paid nothing. The minimum-variance hedge saw your view in the correlation and hedged it away, because a view is variance. In the second hand you hedge the full analytical duration. Rates rise, the futures pay, spreads tighten, the bond pays. Now you got paid for the view, and you also carried the risk of the view. Pick the hedge that matches the bet you meant to make. If you have a view that spreads tighten when rates rise, the empirical hedge pays you nothing for being right."

Theo had spent six years watching clients sign documents that did something other than what they meant, and he recognized the shape of Ines's napkin. Ben Dor asks the same question in one line, almost in passing.

> **[SOURCE EXTRACTION]** *Ben_Dor p.219:* "An empirical hedge, reduced to reflect this known correlation, would exactly offset both of these market effects. Is this what the investor intended?"
>
> **Annotation.** This is the most important question in the chapter, asked as a rhetorical aside. A hedge ratio is a choice of objective, not a fact. Minimum total variance gives you $H$. "Zero rate exposure, keep the spread beta" gives you $H = 1$ plus a separate decision about spread. "Zero exposure to both" gives you a different instrument set altogether. ROBO cannot choose among these. The spec must name the objective, and §8.9 makes that a required field.

Every argument in this section assumes the reader wants to get rid of rate risk. There is a seat in credit that does not, and it holds a great deal of the market.

> **View From Another Seat.** *The insurer, who wants the duration.* An annuity writer reads this section backwards. Its liabilities are long, fixed-rate promises to policyholders, so it does not ask how much Treasury duration to strip out of a bond; it *wants* the duration, matched against those liabilities, and the question it asks of a bond is whether the spread over Treasuries beats the capital charge the bond attracts under risk-based capital rules and its ratings. The seat is large. Athene, Apollo's retirement-services business, reported net invested assets of \$292B at year-end 2025 and a blended net spread, excluding notable items, of 120 bp in the fourth quarter (Jim Zelter, Apollo's president, on the 9 February 2026 earnings call). For a balance sheet built that way, $H > 1$ in 2022 was not the disaster it was for a hedged trading book. The bonds fell in market value, but an insurer holding them to maturity against long fixed-rate liabilities records most of that fall as an accounting event rather than a realized loss, and the same rise in yields let it put new premiums to work at higher rates. How any particular insurer hedges is its own business, and nothing here infers Apollo's policy. What this seat worries about is what the chapter's hedges cannot see: a default that turns a spread into a loss, and a capital charge that jumps when a bond is downgraded across a line, Alltel-style (§8.3).

Mags put it more briefly, to nobody in particular. "Every basis point of duration this desk sells ends up on somebody's balance sheet. The biggest balance sheets in credit buy it on purpose."

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

**Podcasts.**

- **"Why Treasuries Are 'Risky' Again"** (*Odd Lots*, with Carolin Pflueger of the University of Chicago, October 5, 2026). Bonds turning "more stock-like", and the Fed's credibility as the thing that makes them "bond-like" again: the sign of the stock–bond correlation is the regime switch of this section. https://omny.fm/shows/odd-lots/why-treasuries-became-risky-again
- **"What We Learned About Treasuries on the Night of April 8"** (*Odd Lots*, with Ira Jersey of Bloomberg Intelligence, April 28, 2025). Who sold, and why the safe-haven hedge failed in an acute way after "Liberation Day": the market-side story behind Case Study C (§8.7). https://omny.fm/shows/odd-lots/what-we-learned-about-treasuries-on-the-night-of-april-8

**Practitioner Writing.** Prentis and Ripka (Wellington, July 31, 2022), "Empirical duration of risk assets": https://www.wellington.com/en-us/institutional/insights/empirical-duration-risk-assets . Slok (Apollo Academy, December 3, 2022), "High Yield Total Returns in 2022 Mainly Driven by Moves in Duration": https://apolloacademy.com/?p=11885 . Mesirow, "Wrong-way bonds" (2021; title only).

- **"AQR Quant Sketches a Factor-Investing Future for Corporate Bonds"** (Yakob Peterseil, Bloomberg via WealthManagement.com, May 15, 2019). Reports AQR's Roni Israelov sketching a top-down way to replicate corporate-credit exposure with derivatives on government bonds and stocks: the return-decomposition idea behind the book's beta-stripping (§8.1). https://www.wealthmanagement.com/fixed-income/aqr-quant-sketches-a-factor-investing-future-for-corporate-bonds
- **"Debunking the high credit beta myth"** (Christoph Schon, SimCorp, 2024; page undated, year from the URL). Argues that high spread is high volatility but not necessarily high beta to the index, since low-rated names often show weak correlation with the market: the warning to carry from the empirical-duration table into the CCC discussion of §8.3. https://www.simcorp.com/resources/insights/industry-articles/2024/Debunking-the-high-credit-beta-myth

**Academic Papers.** Ambastha, Ben Dor, Dynkin, Hyman and Konstantinovsky (2010), "Empirical Duration of Corporate Bonds and Credit Market Segmentation," *Journal of Fixed Income* 20(1). Ilmanen, McGuire and Warga (1994), "The Value of Duration as a Risk Measure for Corporate Debt," *Journal of Fixed Income*: https://www.aqr.com/Insights/Research/Journal-Article/The-Value-Of-Duration-as-a-Risk-Measure-for-Corporate-Debt . Asvanunt and Richardson (2017), "The Credit Risk Premium," *Journal of Fixed Income*: https://www.aqr.com/Insights/Research/Journal-Article/The-Credit-Risk-Premium . Molenaar, Senechal, Swinkels and Wang (2023), *Empirical evidence on the stock–bond correlation* (title only).

**Data & Code.** FRED ICE BofA OAS series BAMLH0A0HYM2, BAMLH0A1HYBB, BAMLH0A2HYB, BAMLH0A3HYC, BAMLC0A0CM and Treasury yields DGS2/DGS10: https://fred.stlouisfed.org/series/BAMLH0A3HYC (note the three-year window). The `empirical_duration` function in §8.9.

## 8.3 The Discontinuity: Why a CCC Bond Is an Equity Option That Wears a Tie to Work

If the hedge ratio depended only on the spread level, then a Baa bond at 700 bp and a Ba bond at 700 bp would hedge identically. In December 2008 they did not. The Baa bond was a downgraded, frightened, wide investment-grade credit that still behaved like a bond. The Ba bond at the same spread behaved like a stock. Something other than credit risk lives at the IG/HY line, and it is worth a section, because it is the most RSSG-friendly fact in quantitative credit: a market's *quoting convention* is a measurable risk factor.

### Two routes to zero duration

There are two separate reasons a corporate bond can stop caring about Treasuries, and a desk that conflates them will mis-hedge both.

**The correlation route** is §8.2: $H = 1 + \ell s$ falls to zero when the expected spread response to a rate move cancels the rate move. The bond's cash flows still discount at Treasury-plus-spread. The market simply moves the spread against the Treasury.

**The recovery route** needs no correlation at all. It needs only a clock.

> **Math, Gently.** *The memoryless clock: exponential waiting times and the hazard rate.* Picture a smoke detector with a fault. In every small slice of time $dt$ it beeps with the same small probability, $\lambda\,dt$, and it never "gets closer" to beeping: a detector that has been quiet for three years is exactly as likely to go off this afternoon as a new one. That is a *memoryless* clock, and $\lambda$, the hazard rate, is its beep rate per year. The wait until the first beep follows an *exponential* distribution. With $\lambda = 21\%$ a year, the chance of a quiet year is $e^{-0.21} \approx 0.81$, so roughly one chance in five that the clock rings this year, and the average wait is $1/\lambda \approx 4.8$ years. The shape is not the bell curve of Chapter 5: a waiting time cannot be negative, most of its mass sits early, and a long tail runs off to the right, so a few issuers survive for decades on the same clock that takes others in months. Nor is it the Poisson distribution, though the two are siblings: Poisson *counts* the rings in a fixed window, and the exponential *times* the gap between them. Chapter 6 (§6.1.4) built this clock to price default. Here it does a quieter job. A coupon that might never arrive is worth less, and the part of the price that hangs on the clock does not care about the discount rate, so every point of hazard takes a little duration off the bond. The next few paragraphs say how much.

Price a perpetual bond on that clock and three facts come out, each derived in full below. The bond is worth $P = (c + \lambda R)/(r + \lambda)$: coupons while it survives, plus the expected recovery arriving at rate $\lambda$, discounted at the risk-free rate plus the hazard. Its true sensitivity to Treasuries is $1/(r + \lambda)$, while the risk screen, which reads every cash flow as a promised coupon, reports $1/y$. And the share of the screen's duration that is real, $H^{\text{rec}} = c/(c + \lambda R)$, is the share of the bond's value flow that still looks like a bond. With *illustrative* CCC inputs, $c = 9\%$, $R = 40\%$, and $\lambda = 21\%$ (roughly a 1,280 bp spread over a 60% loss given default), $H^{\text{rec}} = 0.09/(0.09 + 0.084) \approx 0.52$. Half the analytical duration of that bond is fiction before anyone has computed a correlation. To first order the two routes multiply, so $H \approx H^{\text{rec}}\,(1 + \ell s)$, and a CCC book can lose all of its rate sensitivity by either road. Figure 8.2 shows both halves of that claim: the screen's duration and the true one separate as default intensity rises.

![Figure 8.2: The recovery route to zero duration for the perpetuity of Section 8.3. Left: the duration on the risk screen (1/yield) and the bond's true sensitivity to Treasury yields (1/(r + λ)); at λ = 21% the screen says 7.7 years and the true figure is 4.0. Right: the ratio of the two, the recovery-route hedge ratio c/(c + λR), is 0.52 there and falls toward zero as default intensity rises, faster when recovery is higher (curves for R = 20%, 40% and 60%; the 0.52 is the 40% curve). Illustrative: the model of Section 8.3 with c = 9%, R = 40% and r = 4% (r matters only for the left panel).](assets/figures/ch08_recovery_route.png)

#### The Full Derivation: the recovery route

Take the cleanest possible case under $\mathbb{Q}$: a perpetual bond paying a continuous coupon $c$ per unit of par, a constant short rate $r$, a constant default intensity $\lambda$, and recovery of face $R$ paid at default (the RFV convention). Survival to $t$ has probability $e^{-\lambda t}$, so

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

As $\lambda \to 0$ the ratio goes to one. As $\lambda \to \infty$ it goes to zero, and the price goes to $R$ whatever $r$ is. That is the restructuring desk's "trades on dollar price" written as a limit.

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

*The desk's conversation is fictional. The bond's path, its dates, ratings, spreads and estimated hedge ratios are Ben Dor's (p.211).*

On the Monday after the thirty-seven cents, Theo found a photocopy on his keyboard: one page of Ben Dor, a chart with a single jagged line on it, and Ines's handwriting across the top. *One bond. Tell me what happened to it.*

The bond was Alltel's 7.875% issue with thirty years to maturity at issue. (Ben Dor prints the CUSIP; we describe the bond and do not reprint identifiers.) Theo read the chart the way he used to read a debt schedule in a first-day declaration, left to right, looking for the date somebody changed the deal. In 2006 the bond was rated A2 at a spread of about +200 bp, and its rolling empirical hedge ratio sat near 0.75: a long-dated investment-grade bond behaving like one. On 23 May 2007 it was downgraded to Ba2 at about +450 bp, as the company headed into a leveraged buyout, and the hedge ratio fell to about 0.4. On 21 November 2007, with the buyout closed and the bond sitting inside a heavily levered structure, it was cut to Caa1, and the hedge ratio fell into negative territory, as low as −0.6. On 8 January 2009, by Ben Dor's dating (Verizon's own closing release is dated the next day), Verizon's acquisition of the company closed, the bond was re-rated A2, and the hedge ratio climbed from about 0.25 back to about 0.95.

"Nothing happened to it," Theo said, when Ines came by. "That's the point, isn't it? The coupon was 7.875% the whole way through. The maturity never moved. The indenture is the same document in 2009 that it was in 2006. Somebody put a pile of new debt on top of it in 2007, and somebody else took the whole company out in 2009. The capital structure got rewritten twice around a bond that didn't change a word."

"And the bond's sensitivity to the ten-year went from 0.75 to minus 0.6 and back," Ines said. "Without a word."

Theo asked the only question he ever asks. "What did the indenture say about change of control? Whether this bond got taken out, or left behind, or put back at par, that's what decided how it traded in 2007."

"Ben Dor didn't print the indenture," Ines said. "He printed the beta."

"It doesn't matter for the hedge anyway." Mags had wandered over with her own copy of the page, which she had apparently owned for years. "Whatever the document said, the rate beta moved with the cap table, not the coupons. The coupons never did anything. What changed was who owned the paper and what they looked at when they priced it. In May '07, I'd bet, the people who quoted it as a spread to the long bond sold it to people who quoted it in points. Their screens don't move when the ten-year moves."

Kaz pulled the page toward them and ran a finger along the line. "A sixty-day rolling window would have caught the May downgrade by about the end of July."

"And from May to July," Ines said, "you'd have been hedging a Ba2 bond with an A2 hedge ratio. Short twice the futures you needed, on a bond that had stopped listening to them." She put the page back on Theo's desk. "This is why we keep a rating-bucket table and re-estimate it every month. The day a bond crosses the line, in either direction, it gets the new bucket's $H$ that morning. We don't wait for a trailing window to notice a downgrade the rating agency already announced. And the Treasury hedge for the whole high-yield book is sized off the buckets, never off one bond's own regression, because one bond's $R^2$ is 0.01. You can't hedge with a number that explains one percent of anything."

"A bucket average is a cruder estimate," Kaz said.

"A crude estimate of something that's there beats a precise estimate of noise." Ines was already walking away. "Ask Theo what he'd do on 21 November."

Theo looked at the chart. On 21 November 2007 the bucket rule would have moved the bond to the Caa table, where $H$ was near zero or below, and taken the futures off. It would not have told him to go long Treasuries against the bond because one rolling estimate touched −0.6, and he decided that was the right amount of humility for a rule. What the rule could not do, and what he wrote in the margin next to the May date, was see the buyout before the agency did. Ben Dor's own note on the page says where that thought leads.

> **[SOURCE EXTRACTION]** *Ben_Dor p.211:* "When the bond was further downgraded to Caa1 on November 21, 2007, the hedge ratio dropped even further to negative territory (as a low as −0.6)."
>
> **Annotation.** One security, one indenture, four hedge ratios, from 0.95 to −0.6: one number estimated over 2006–2009 would have been wrong in every sub-period, and the scene above has both readings, Ines's bucket and Mags's cap table. What the page adds is a test. Chapter 13 asks whether the same signature appears before a priming transaction. If a bond's rate beta collapses before the uptier is announced, as Alltel's did when the buyout's debt landed on top of it, that is a free early-warning feature for the Priming Risk Score.

Kaz, who had kept the photocopy, pinned it next to a printout of this month's FRED spreads and drew an arrow from the Caa1 step to the CCC line. "Alltel was one bond that stopped answering to the index for twenty months. The CCC tier has stopped answering to it as a group."

> **Trend Watch: CCC Decompression, 2024–2026.** *What changed.* The CCC tier has come apart from the rest of high yield. On FRED's ICE BofA series the CCC-and-lower to BB OAS ratio was 4.0× at the end of 2024 (746 bp / 186 bp), 5.2× at the end of 2025 (885 / 169), and 6.5× on October 15, 2026 (1,278 / 197). The CCC OAS reached 12.82% on October 14, 2026 (HY 3.25%, IG 0.84% that day); on October 15 the CCC OAS was 12.78%, the broad HY OAS 3.23% and IG 0.84% (computed 2026-10-17). The beta of CCC relative spread changes on HY relative spread changes fell from 0.54 (2024) and 0.55 (2025) to 0.45 (2026 year to date). *What it means for the desk.* CCCs are loading less on the market spread factor and more on something issuer-specific. In this chapter's vocabulary, more of their return is idiosyncratic, which for a pure-IDO book is opportunity and for a DTS-scaled risk model is a warning: DTS assumes relative spread changes are common across credits, and in the CCC tier that assumption is weakening. We do not attribute causes here; Chapter 11 takes up the CCC problem and Chapter 14 the recoveries behind it.

## 8.4 DTS: The Unit of Credit Beta

The restructuring banker's instinct is that leverage is not one number. Six turns of debt at a software company and six turns at a regional grocer are different risks, and the spread already tells you how different. DTS is the same instinct applied to spread risk. Two bonds with identical spread duration are not equally risky if one trades at 80 bp and the other at 800 bp, because spreads do not move in basis points. They move in percent.

> **Math, Gently.** *Spreads move in percent: proportional volatility, and what it has to do with the lognormal.* Put a 100 bp bond and an 800 bp bond side by side on the same bad day. The first widens 10 bp and the second 80. In basis points the second moved eight times as far; in percent, both moved 10%. Spreads have that habit, and stock prices have it too: the thing that behaves like a bell curve is the *percentage* change, not the level. Chapter 7 met the shape this produces, the lognormal, as a fact about distributions. Here it is a fact about risk. When percentage moves are the common currency, a spread can never be pushed below zero (a 10% tightening takes 10 bp off a 100 bp bond and 1 bp off a 10 bp bond), and the bond with the bigger spread always has the bigger move in basis points. So the natural measure of a bond's spread risk is its spread duration times its spread, DTS: how much the price moves for a 1% relative move in the spread. In the margin, a bond with spread duration 6 at a spread of 1.5% has $\text{DTS} = 6 \times 0.015 = 0.09$. Ben Dor's estimated slope for investment grade (p.51) is 8.8% a month, so the bond's monthly excess-return volatility is about $0.088 \times 0.09 = 0.79\%$. A beta is a regression slope too, the tilt of the cloud in §8.2, but here the cloud has been drawn in advance: if every bond's spread moves by roughly the same percentage on a market day, a bond's beta to the market is the ratio of two numbers already on the risk screen, $\text{DTS}_i/\text{DTS}_M$. The derivation follows.

### The derivation

The box makes two claims, both derived below: excess-return volatility is proportional to DTS, $\sigma(R^{\text{xs}}_i) \approx \kappa\,\text{DTS}_i$, and credit beta is a ratio of DTS, $\beta_{i,M} = \text{DTS}_i/\text{DTS}_M$.

#### The Full Derivation: proportional volatility and the DTS beta

Ben Dor's central empirical regularity is that the volatility of spread changes is proportional to the spread level:

$$
\sigma(\Delta s_i) \approx \kappa\, s_i ,
$$

where $\kappa$ is a relative spread volatility (for example, per month) that is roughly common across bonds within a market. Combine it with the first-order excess return of §8.1, $R^{\text{xs}}_i \approx -D^{\text{spr}}_i\,\Delta s_i$:

$$
\sigma\big(R^{\text{xs}}_i\big) \approx D^{\text{spr}}_i\,\sigma(\Delta s_i) \approx \kappa\, D^{\text{spr}}_i\, s_i = \kappa\,\text{DTS}_i .
$$

Excess-return volatility is linear in DTS with slope $\kappa$. Ben Dor estimates the slope at 8.8% per month for investment grade, with an $R^2$ of 98% (p.51); the box above ran it for a bond with $D^{\text{spr}} = 6$ and $s = 1.5\%$. At very low spreads the line has a small structural floor (p.57), which is why DTS slightly understates the risk of the tightest bonds.

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

That paragraph is a pod's daily bread, and the platform's risk team reads it differently from the PM who built the pair.

> **View From Another Seat.** *The multi-strategy pod's risk x-ray.* A credit PM on a multi-manager platform builds a long–short that screens flat on her own blotter: \$50mm long a single-B bond at 700 bp against \$50mm short a BB bond at 250 bp, similar spread durations, DV01 matched to the dollar *(illustrative)*. Flat in notional, flat in rates. Overnight the platform's central risk team runs every book through a bought factor model, and in the morning her line on the factor screen is orange. The long carries 2.8 times the short's DTS, so 64% of the long leg's spread beta is unhedged: the "pair" is about \$32mm of outright single-B beta with a short attached. One PM's leak is a rounding error. Hundreds of PMs each leaking a little in the same direction add up to a firm-level long in high yield that nobody chose and the platform did not mean to pay residual prices for. In the public accounts of how these platforms are run, that is why books are kept market- and factor-neutral, why the factor model serves as a daily x-ray of every book, and why the leverage goes on the residual rather than on the beta (Giuseppe Paleologo on *Odd Lots*, 20 May 2024; Rich Falk-Wallace on *Odd Lots*, 25 Jul 2024). From that seat a DTS ratio is not an analytics nicety. It is the difference between selling the platform a residual and selling it beta at a residual's price.

Dov Adler's pod, on a platform of that kind, builds its pairs the other way round, ruler first. The Pair Book's third entry is the textbook DTS pair, with one factor left open on purpose and written down as such.

> **The Pair.** *Pair Book entry PB-03, Dov Adler's pod at Vantress Capital Management (fictional composites). A replay, cut off at the close of Tuesday 31 March 2020. Positions, prices and P&L are illustrative; the issuers, the downgrade and its dates are real (Chapter 1, §1.8.2).* **Thesis.** Dov's sentence, with its date: *Ford Motor Credit's senior unsecured notes give back the discount that index-forced selling put on them, measured against an auto lender that stayed investment grade, by 30 September 2020.* S&P had cut Ford to BB+ on 25 March, and roughly \$36bn of Ford debt was due to leave the investment-grade index at the month-end rebalance. **Legs.** Long \$25mm face of a Ford Motor Credit note with about four years left, at 88, +850 bp, spread duration 3.5; short a GM Financial note of similar maturity at 93, +500 bp, spread duration 3.6, borrowed through the prime broker. Matching market-value DTS, $h_S = (3.5 \times 0.085)/(3.6 \times 0.050) \approx 1.65$, puts \$36.4mm of market value on the short, about \$39mm face; whatever beta survives the match is trimmed in CDX IG. **What the hedge removes.** Market spread beta, by construction, and most of the auto-lender sector factor, since both legs live off the same car buyers. **What idio remains.** The bet that Ford's 25 March price was a mandate's price, not a credit's. **What leaks.** The rating-bucket factor, deliberately: the long is now high yield and the short is not, so the pair is long the fallen-angel factor of Chapter 9, and its P&L will look like idio to anyone who forgets that. Rates, by accident of the ruler: a short 1.65 times the long's market value leaves the pair short about \$5,400 of DV01 ($\$13{,}100 - \$7{,}700$), which Dov hedges in futures rather than carry a rates view inside a credit pair. And the borrow, recallable on a day's notice. **What it costs.** The long's coupon (5.1% on \$25mm, \$1.28mm a year) against the short's coupon owed to the lender (3.5% on \$39mm, \$1.37mm) is −\$0.09mm a year, and the two pulls to par nearly cancel, so the pair carries close to nothing, as the paragraph above predicts. Borrow at 35 bp on \$36mm is about \$0.13mm a year. Two legs of half-spread in a March 2020 market, about a point on Ford and half a point on GM Financial, cost about \$0.45mm to get in and as much again to get out, against a thesis the pod sizes at six points of relative convergence, \$1.5mm *(all illustrative)*. In this market the friction is more than half the thesis. Chapter 7-B estimates the pair's half-life, Chapter 9 names the factor it was long, and Chapter 24 closes it on the basis.

### Why DTS beats an estimated beta

The obvious objection: why compute beta from DTS when you can estimate it by regression? Because the regression is unstable, not because it is biased.

> **[SOURCE EXTRACTION]** *Ben_Dor p.274:* "the average standard deviation of the beta-based hedge ratios (1.4) is more than double that of the DTS-based hedge ratios (0.6)."
>
> **Annotation.** On average, the estimated beta and the DTS ratio agree. Month to month, the estimated beta wanders more than twice as far. A hedge ratio that wanders forces rebalancing, and rebalancing in corporate bonds costs real bid–ask (Chapter 18). The general principle, which reappears in every shrinkage estimator in this book: when a structural model gives you an unbiased, low-variance answer, an unrestricted regression has to beat it out of sample, not in sample. For the 2026 desk the practical blend is to start from $\text{DTS}_i/\text{DTS}_M$ and shrink a rolling regression beta toward it, with the shrinkage weight set by out-of-sample hedge error. The DTS ratio is the prior. The data have to earn the deviation.

> **[SOURCE EXTRACTION]** *Man_2022 p.15:* "We therefore adjust our statistical factor risk model (SFRM) with Duration Times Spread (DTS) in order to take into account the various issues referenced above."
>
> **Annotation.** This is how DTS travels into a modern risk stack. Divide each bond's excess return by its DTS, estimate the covariance or principal components on the scaled returns, and multiply back. Without the scaling, a statistical factor model spends its first principal component discovering that high-spread bonds are volatile, which you already knew. With it, the components describe *how* bonds co-move rather than *how much*. Man's motivation (p.13) is that bond betas are "less concentrated around the mean than for equities," so a model that assumes equity-like beta dispersion mis-sizes everything. ROBO's version of the instruction is short. *DTS-scale before any covariance estimate; never estimate a covariance on raw excess returns of bonds whose spreads differ by more than a factor of two.*

DTS has its own ways of failing, and none of them announces itself.

> **Ways This Blows Up.** (1) *Wrong duration.* DTS uses spread duration. For a floating-rate loan, rate duration is near zero but spread duration is roughly the time to maturity or the expected refinancing date. Use $D^{\text{mod}}$ and your loan book shows no credit risk. (2) *Negative or tiny OAS.* Some very short or very high-quality bonds print negative OAS, which makes DTS negative and relative spread changes explode. Guard with `assert oas > 0` before computing $\Delta s/s$, and fall back to absolute changes with a warning. (3) *A regime-dependent slope.* $\kappa$ is not a constant of nature. It rises sharply in crises, and the proportionality itself bends in the CCC tier (Trend Watch above). DTS makes betas comparable across bonds at a point in time. It does not make volatility forecastable across regimes.

## 8.5 Betas When Nothing Trades: Dimson, Scholes–Williams, and the Lag That Isn't Noise

Every regression in this chapter so far has assumed that a bond's return on day $t$ is the bond's return on day $t$. It usually is not. In September 2009, about half the bonds in the Corporate and High Yield indices traded fewer than 15 times in the month, and 25–30% did not trade at all. Monthly turnover was about 5% of amount outstanding for IG and 4% for HY (Ben_Dor p.203). The daily "return" of a bond that did not trade is the change in an evaluated price, which is a pricing service's opinion of where it would have traded. That opinion is anchored to yesterday's opinion. A stale bond price is like a lender call: the information arrived days ago, and it is only now being acknowledged.

The signature is visible in volatility. Across Ben Dor's liquidity quintiles, daily price-return volatility differs by roughly 40% between the extremes: 122 versus 72 bp a day for Caa, 86 versus 54 for B, 67 versus 39 for Ba (Ben_Dor p.206, Table 7.4). Some of that gap is genuine risk, but much of it is smoothing. Stale prices are smoother prices, and smoother prices produce smaller betas.

> **Math, Gently.** *News in three envelopes: what a moving average does to a slope.* Suppose each day's true news about a bond arrives in three envelopes. Half of it is opened today, 30% tomorrow and the last 20% the day after, because the pricing service marks the bond partly off its own previous mark until a trade forces it to catch up. The shares add up to one, so all the news gets in eventually; it just gets in late. Run a same-day regression of the bond's marked return on the market's return and the regression only ever sees the first envelope: a bond whose true beta is 1.0 reads 0.5. Add yesterday's market return as a second regressor and its coefficient picks up the second envelope, 0.3, for a running total of 0.8. Add the day before and the last 0.2 arrives, for 1.0. Adding up the coefficients across the lags is Dimson's correction. The simulation behind Figure 8.3 lands on 0.49, 0.81 and 1.005, which is these three numbers plus the simulation's rounding (its middle figure is Scholes–Williams, a one-lag cousin). The same envelopes flatter the volatility, because a shock spread over three days partly averages itself away, so the hedge comes out too small and the risk report agrees with it. The algebra is next.

### The smoothing model and the bias it creates

Write the envelopes as a moving average and three results follow, each derived below: the same-day beta converges to the on-time share of the news, $\theta_0\beta$; the marked volatility shrinks by the factor $\sqrt{\sum\theta_k^2}$; and summing the coefficients on lagged factor returns recovers $\beta$ once the lags cover the smoothing, while Scholes–Williams recovers one lag's worth.

#### The Full Derivation: Scholes–Williams and Dimson under a smoothing model

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

The denominator corrects for the factor's own autocorrelation, which univariate regressions would otherwise double-count. It recovers only one lag of smoothing, so on a bond with two days of staleness it under-corrects. Figure 8.3 shows the staleness and the three estimators side by side.

![Figure 8.3: Stale marks shrink beta, and lagged regressors put it back. Left: cumulative return of a bond whose marks absorb each day's news over three days (weights 0.5, 0.3, 0.2) against its true return. Right: OLS recovers only the same-day weight (0.49), Scholes–Williams one more lag (0.81), and Dimson with two lags the full beta (1.005). Scholes–Williams divides by 1 + 2ρ_f, which is why its same-day piece is 0.52 rather than 0.49; its lead term (−0.002) is too small to draw. Illustrative: simulated from the smoothing model of Section 8.5 by Listings 8.1 to 8.4 (seed 8, 2,500 days).](assets/figures/ch08_stale_marks_beta.png)

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

Here the econometrics meets the trading. Dimson assumes the lagged coefficients are pure smoothing, information that was always going to arrive. Some of it is genuine *information diffusion*: the equity market learns first and the bond market follows. Gebhardt, Hvidkjaer and Swaminathan (2005) document momentum spillover from stocks to bonds. Dynkin (p.606) reports that bonds of issuers in the bottom equity-momentum decile delivered −4.7% a year of excess return over 1993–2017, against about +4.0% for the top decile. A Dimson beta of a bond on its issuer's stock is therefore part stale-price correction and part trend signal.

The desk found this out the way it finds out most things, by arguing over a printout. By Wednesday Kaz had the Dimson code running against every factor on the desk's list, the issuers' own stocks included. "Two lags on the equity, summed into the beta," they said. "The math doesn't care what the regressor is called."

Ines looked at the output for Theo's bond. The coefficient on the issuer's stock return from the day before was larger than the coefficient on the same day's. "That isn't the pricing service catching up. That's the stock telling the bond something a day early."

"It's a lag. Lags are smoothing."

"Some lags are smoothing. That one is the hand history." She tapped the number. "When the stock moves first and the bond follows, somebody at this table knew more than you, and they told the equity market first. Sum that into the hedge and you hedge away the one thing that would have paid you. You don't hedge it. You study it." She wrote *Ch 10* next to the coefficient, which is where the desk keeps the things that might be trend.

Kaz did not concede in words, but by Friday the whiteboard said *rates and index lags: staleness; equity lags: evidence, until an out-of-sample test says otherwise*, in Kaz's handwriting, which on this desk counts as the minutes.

A *computed illustration*, offered as a hypothesis rather than proof. On FRED daily ICE BofA index data from January 2024 to October 2026, the same-day correlation between relative OAS changes and 10-year yield changes is −0.27 for HY, −0.32 for BB, −0.23 for B, −0.19 for CCC, and −0.28 for IG. The correlation with the *previous* day's yield change is +0.098, +0.125, +0.091, +0.038, and −0.041 respectively (computed 2026-10-17). High yield partially reverses its same-day spread response the next day; investment grade does not.

> **[SOURCE EXTRACTION]** *Ben_Dor p.203:* "Investment-grade bonds are typically quoted as a spread to a Treasury security with similar maturity ("parent"), whereas high-yield bonds are quoted on price."
>
> **Annotation.** The convention predicts the pattern. If an HY bond's price is sticky and the Treasury sells off, the computed OAS (yield implied by an unchanged price, minus a higher Treasury yield) mechanically *tightens* the same day, then widens back as the price catches up. Part of high yield's negative daily rate–spread correlation is the OAS calculator doing arithmetic on a stale price. An IG bond quoted at a fixed spread to its parent moves its price with Treasuries automatically, so no reversal appears. Ben Dor's tests (p.207) show staleness cannot explain the whole IG/HY gap at the levels they study. Our point is narrower and operational: at *daily* frequency, a Dimson-summed $\rho$ for HY is materially closer to zero than the same-day $\rho$. With the numbers above, summing one lag cuts HY's same-day correlation from −0.27 to roughly −0.17, which moves the pooled 2024–2026 HY hedge ratio from about 0.72 toward 0.82 *(illustrative arithmetic: equal-variance lags, so coefficient ratios equal correlation ratios)*. Hedge at a weekly horizon or Dimson-sum the daily one. Do not hedge daily on a same-day estimate.

> **Ways This Blows Up.** (1) *Too many lags.* Each lag adds a coefficient's worth of estimation noise to the sum. Cap $L$ at 2–3 for daily data and 1 for monthly, or shrink the lag coefficients toward zero; the code refuses $L > 5$. (2) *Forward-filled prices.* A missing price forward-filled into a return series creates zeros followed by catch-up jumps, a smoothing model you invented. Compute returns only between actual marks, and record the gap length so the smoothing model can use it. (3) *Overlapping returns.* Weekly returns sampled daily overlap, so the regression errors are a moving average. Use Newey–West standard errors or non-overlapping samples, or the $t$-statistics on your hedge ratios are fiction.

### Deep-Dive Resource Graph

**Podcasts.**

- **"Why the True Price of a Bond Can Still Be Hard To Know"** (*Odd Lots*, with Maciej Kowara and Eric Jacobson of Morningstar, April 5, 2021). Evaluated prices differ by firm on illiquid bonds: the stale-price mechanism behind the non-synchronous betas in this section. https://omny.fm/shows/odd-lots/why-the-true-price-of-a-bond-can-still-be-hard-to
- **"Boaz Weinstein"** (*Money Stuff: The Podcast*, with Matt Levine and Katie Greifeld, March 19, 2026). Private-credit NAVs, BDC discounts and "volatility laundering": the smoothing problem of this section in a live market, where the desmoothing is left to you. https://omny.fm/shows/money-stuff-the-podcast/boaz-weinstein
- **"Investors Keeping Score on 'Bad PIK', Benefit Street Partners' Kumar Says"** (*The Credit Edge*, with Anant Kumar of Benefit Street Partners, August 6, 2026). PIK used to mask stress and a transparency push that is forcing dubious marks to be addressed faster: stale marks seen from the manager's side. https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/investors-keeping-score-on-bad-pik-and-stale-marks-benefit-street-partners-kumar-says
- **"Ralph Smith - Scientific Investing in Fixed Income (S5E7)"** (*Flirting with Models*, with Ralph Smith of BlueCove, July 11, 2022). Breadth and liquidity differ between credit and rates, and the assumption about a bond's availability materially moves a backtest: the practitioner's version of asking whether the price you regress on was one you could trade. https://www.flirtingwithmodels.com/episodes/kAEkSoYuRwd

**Practitioner Writing.** Asness, Krail and Liew (2001), "Do Hedge Funds Hedge?", *Journal of Portfolio Management* 28(1): the canonical demonstration that summed lagged betas reveal market exposure hidden by stale marks (DOI 10.3905/jpm.2001.319819).

- **"Common pitfalls in the evaluation of corporate bond strategies"** (Cesare Robotti, Warwick Business School; Finance Seminar, Aarhus University, April 11, 2024). The abstract's claim that large abnormal returns from many bond strategies mostly stem from microstructure noise in transaction prices: the same noisy-price problem this section corrects for in betas. https://econ.au.dk/research/finance/seminars/vis/artikel/finance-seminar-cesare-robotti-warwick

**Academic Papers.** Dimson (1979), "Risk measurement when shares are subject to infrequent trading," *Journal of Financial Economics* 7(2): https://ideas.repec.org/a/eee/jfinec/v7y1979i2p197-226.html . Scholes and Williams (1977), "Estimating betas from nonsynchronous data," *Journal of Financial Economics* 5(3): https://ideas.repec.org/a/eee/jfinec/v5y1977i3p309-327.html . Getmansky, Lo and Makarov (2004), "An econometric model of serial correlation and illiquidity in hedge fund returns," *Journal of Financial Economics* 74(3): https://ideas.repec.org/a/eee/jfinec/v74y2004i3p529-609.html . Bao, Pan and Wang (2011), "The Illiquidity of Corporate Bonds," *Journal of Finance* 66(3): https://ideas.repec.org/a/bla/jfinan/v66y2011i3p911-946.html . Gebhardt, Hvidkjaer and Swaminathan (2005), "Stock and bond market interaction: Does momentum spill over?", *Journal of Financial Economics* 75(3): https://ideas.repec.org/a/eee/jfinec/v75y2005i3p651-690.html .

**Data & Code.** FINRA TRACE (canonical root https://www.finra.org/filing-reporting/trace) for transaction-based returns; `dimson_beta`, `scholes_williams_beta`, and `desmooth` in §8.9.

## 8.6 The Hedge Matrix: CDX, UST Futures, HYG/JNK, Equity Puts

At 2:58 p.m., Theo cannot short "the market spread factor." He can short what is on the screen, and each instrument there is a different, imperfect, separately priced claim on the factors he wants to remove. Ines's framing: "You don't get to hedge the risk. You get to trade the instruments. The difference is the basis, and the basis is a position."

### The instruments, in DV01 terms

So Theo did what a banker does with a list of financing sources: he opened each one in its own window and asked what was wrong with it. Ines, who had rolled her chair back over, named the basis before he finished reading the ticker.

The first window was the Treasury futures strip, TY, UXY and the rest: the rates leg. "The contract doesn't deliver a bond," Ines said. "It delivers whichever eligible note the short decides to hand you, at an invoice price set by a conversion factor. You're hedging with a bond somebody else gets to choose."

> **[SOURCE EXTRACTION]** *Veronesi p.237:* "The invoice price equals the futures settlement price times a conversion factor plus accrued interest. The conversion factor is the price of the delivered note (\$1 par value) to yield 6 percent."
>
> **Annotation.** The 6% notional coupon matters because, with yields far from 6%, the conversion factor mis-scales the deliverables and one of them becomes reliably cheapest. The futures then trade like that bond divided by its conversion factor. Hence the hedge sizing $N = \text{DV01}_{\text{target}} / (\text{DV01}_{\text{CTD}}/\text{CF})$, where $\text{DV01}_{\text{CTD}}$ is per contract face (\$100,000 for TY). For the cold-open bond, $\text{DV01}_{\text{target}} = \$40\text{mm} \times 4.1 \times 0.0001 = \$16{,}400$. With *illustrative* CTD inputs of \$63 DV01 per \$100,000 face and $\text{CF} = 0.89$, one contract carries about \$70.8 of DV01, so a full analytical hedge is 232 contracts. Two departures for a credit desk. Futures settle daily, so a precise hedge is "tailed" by the discount factor to delivery (Veronesi p.269), which matters for size and long horizons and hardly at all for a one-week hedge. And when the CTD switches, the futures' DV01 jumps, which is the futures' own convexity and a source of hedge slippage that has nothing to do with credit.

Kaz, reading the futures primer, looked up. "Cheapest-to-deliver. Is that a kind of drop-down?"

"Same idea, better suit," Mags said. "The short picks which bond to hand you, and he picks the one that hurts you most. In a drop-down, the sponsor picks which assets you get to keep. Both times it's an option against whoever is long and not paying attention."

The second window was CDX HY, the spread leg in its purest listed form. It trades in price with a fixed 500 bp running coupon and rolls to a new series every March 20 and September 20. Ines made Theo say the sign conventions out loud, because they are where desks lose money: buying protection is *short* credit, and the quoted price *rises* when spreads tighten. For small moves $\Delta P \approx -\text{RPV01}\cdot\Delta s$, where RPV01 is the index's risky annuity, roughly its spread duration. "Its basis is everything that isn't the market," she said. "It's a near-perfect hedge for high-yield spread beta and a terrible hedge for anything idiosyncratic. Which is the point. If it hedged your idio, you wouldn't have any."

The third window held two tickers, HYG and JNK, the cash-bond beta wrapped in an exchange-traded fund. As of mid-October 2026, HYG had net assets of about \$17.2bn across 1,334 holdings, an effective duration of 3.20 years, an OAS of 284 bp, and 30-day average volume of about 64.6 million shares. JNK had about \$5.7bn of assets, 1,161 holdings, and an option-adjusted duration of 3.23 years (ishares.com and ssga.com product pages, October 15–16, 2026). "Two bases," Ines said. "They carry rates *and* spread, so you hedge both whether you meant to or not. And in stress the price walks away from NAV, which is a basis you are long or short without having been asked" (Chapter 20). JNK tracks the same Bloomberg High Yield Very Liquid index family that underlies CME's HY credit future, which makes the pair a natural arbitrage leg.

The last window was equity puts, the tail leg, and the one Kaz found most natural, because Ben Dor had already told them a CCC bond resembles equity (§8.3). Carr and Wu (2011) show that a spread between two co-terminal American puts struck inside a default corridor "replicates a pure credit contract." "For a CCC book," Ines said, "single-name or index puts hedge the jump to default that CDX spreads across a hundred names. For a BB book they're mostly an expensive way to buy noise." There was no window for single-name CDS, because Theo's issuer had no liquid contract. For an issuer that has one, single-name protection is the jump-to-default hedge, and Chapter 24 derives its ratio.

Then she made him look at the clocks. These instruments do not stop moving at the same moment. Treasury futures settle in the early afternoon Chicago time (around 3 p.m. New York), evaluated bond prices are typically struck mid-to-late afternoon in New York, equities close at 4 p.m., and CDX end-of-day marks come later still *(approx.; check each venue's methodology)*. A daily covariance between a bond priced at 3:30 and an index marked at 5:00 is §8.5's staleness problem, built in by design. Estimate the hedge matrix on Dimson-summed covariances,

$$
\Sigma^{\text{D}}_{Hp} = \sum_{k=-1}^{1}\mathrm{Cov}(r_{H,t-k},\, r_{p,t}),
$$

or on weekly returns, and use daily data only to monitor. That is the research answer. The production answer is duller and matters more. The desk snaps every mark to one timestamp: the 3 p.m. New York Treasury futures settlement, a 3 p.m. CDX snapshot, a 3 p.m. composite for the bonds and ETFs. The risk system and the P&L explain read the same snap. A hedge ratio estimated on one clock and marked on another manufactures a residual every evening, and Theo, looking at the four cents nobody owned, began to suspect where some of them came from.

> **View From Another Seat.** *The market maker's basket.* For a principal market maker, Theo's bond is not a position with a hedge attached; it is one leg of a basket. Jane Street, to take a firm that describes itself in public, says on its own pages that it traded "more than \$900 billion with clients globally in 2025" and prices "more than 25,000 bonds," and describes itself as one of the world's leading ETF liquidity providers (janestreet.com, fetched 18 October 2026). At that scale the logic of the seat, whatever any one firm's internal practice, runs like this. An RFQ in the bond is a question about the basket: can the risk be laid off in HYG, a CDX position or the issuer's equity cheaply, and is there a way out within days through an ETF creation or a portfolio trade? If so, the seat quotes tight and small. If its models see a jump coming (a lender call, a missed coupon, a filing) rather than a diffusion, the basket stops hedging and the quote widens or disappears. Non-synchronous closes are this seat's daily life, since its book is a set of legs marked on different clocks, and the snap above is how such desks live with it. The advice the seat would give Theo is the advice Ines just gave him: there is no hedge, only a basket with a basis, and the basis is the position you actually hold.

Theo now had four windows, four bases and one question: how much of each to sell.

### The derivation: minimum variance, ridge, and hedging less

The answer depends on how alike the instruments are, and HYG, JNK and CDX are very alike. That turns out to be a problem rather than a comfort.

> **Math, Gently.** *Two hedges that are almost the same hedge: the matrix inverse, the condition number, and the ridge.* Try to pin a point on a table with two rulers laid almost on top of each other. Along the direction they share, they fix the point beautifully. Across it, where they barely differ, a hair's slip in either ruler moves your answer a long way. A hedge built from HYG and JNK is that pair of rulers. Solving for the best hedge means *inverting* the instruments' covariance matrix, the matrix version of dividing by a number, and dividing by something close to zero produces something enormous. The *condition number* measures how close: the ratio of the matrix's largest stretch to its smallest (its largest and smallest eigenvalues), here the stretch along the shared direction against the stretch across it. Two instruments with unit variance and correlation 0.99 have eigenvalues $1 + 0.99 = 1.99$ and $1 - 0.99 = 0.01$, a condition number of 199, so a 1% error in the estimated covariance can become an error of up to about 199% in the hedge weights. Add a small *ridge*, $\eta = 0.1$, to each diagonal entry and the eigenvalues become 2.09 and 0.11, a condition number of about 19. The hedge stops lurching. The price is that every weight shrinks toward zero, which is a polite way of saying you hedge less, and the derivation below shows why hedging less is often right anyway.

In symbols, the variance-minimizing hedge is a regression of the book on its hedge instruments, $h^\star = \Sigma_{HH}^{-1}\Sigma_{Hp}$; the ridge adds $\eta$ to the diagonal before inverting; and when the only hedge is a noisy proxy, the best hedge is smaller than the naive one by the share of the proxy's variance that is signal.

#### The Full Derivation: minimum variance, ridge, and hedging less

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

Every row is defensible, which is the indictment. Theo read the four numbers out loud, and Mags, who had not appeared to be listening, said the sentence the rest of this chapter tries to get out from under: "The empirical hedge ratio is a bet on why rates move." Over the hedge horizon, she meant, and with somebody else's money. The matrix approach does not remove that bet. It makes the bet explicit, and it lets the CDX leg take the spread beta that the futures were implicitly being asked to absorb. The Ad Hoc Group, represented by counsel, confirms that its members' positions are fully hedged with respect to interest rates, and declines to say with what.

> **Ways This Blows Up.** (1) *The futures–cash basis in a crisis.* In Ben Dor's replication study (Table 14.5, p.386), replicating the US Treasury index with futures ran a tracking error of 5.0 bp a month, worst month 12.1 bp, before 2008; the extraction below says what 2008 did to both. The rates hedge broke in the same month as the credit book. (2) *Roll dates.* CDX rolls on March 20 and September 20 and Treasury futures roll quarterly. An unadjusted continuous series shows jumps that a covariance estimator reads as volatility and a regression reads as beta. Splice rolls on a return basis, never a price basis. (3) *Signs.* Long CDX protection is short credit, and the CDX price rises when spreads tighten. ROBO will get exactly one of these two right unless the schema states both. (4) *ETF basis in stress.* In March 2020, HY ETFs traded at large discounts to NAV (Chapter 20), so a hedge sized on NAV beta was mis-sized in price terms exactly when it mattered.

Ben Dor measured the first of those failures directly, in the year it mattered most.

> **[SOURCE EXTRACTION]** *Ben_Dor p.386:* "TEVs for U.S. Treasury Index and MBS Index replication increased to 37.5 bps and 18.5 bps, respectively. The largest monthly tracking errors increased as well, more than fivefold, to 87.3 bps and 54.3 bps"
>
> **Annotation.** The hedge instruments are not risk-free tools. They are positions with their own crisis behavior. A credit desk's stress test must shock the hedge basis together with spreads, not after them. In 2008 the futures leg lost its tie to cash in the same months that credit spreads exploded, so a "rates-neutral" book was neither. The modern version of the lesson is the condition-number alarm in §8.9: when $\text{cond}(\Sigma_{HH})$ rises, it is often because one instrument has decoupled from its siblings, which is the basis blowing out in real time.

The market has since started to sell, as a product, the subtraction this chapter performs by hand.

> **Trend Watch: Listed Credit Beta and the Duration-Hedged Index Family, 2014–2026.** *What changed.* In an April 23, 2024 announcement, CME Group said it would launch credit futures on June 17, 2024, pending regulatory review, on the Bloomberg US Corporate (IG) Index and the Bloomberg US High Yield Very Liquid Index, along with futures on a Bloomberg *duration-hedged* index. It also said users could manage duration risk through an intercommodity spread with Treasury futures, with margin offsets against interest-rate and equity-index futures (Markets Media, April 29, 2024; FI Desk). For the first time, a cleared, listed contract packaged "credit beta with the rates stripped out" as a product. The ETF version is older: the iShares Interest Rate Hedged High Yield Bond ETF (HYGH) launched May 27, 2014. On October 15–16, 2026 it showed an effective duration near zero and net assets of about \$652mm, a small fraction of HYG's size (ishares.com). *How big.* The market for pre-packaged rate-hedged HY is small relative to the unhedged product. Most investors decline to commit to a hedge ratio in advance, which is the rational response to Table 8.2. Meanwhile the thing being hedged has shrunk. HYG's effective duration of about 3.2 years compares with roughly 4.2–4.8 years for HY in Ben Dor's 2007–2009 sample (p.206), so the spread leg dominates the HY hedge matrix more than ever. *What it means for the desk.* A duration-hedged credit future is a fifth column in the hedge matrix with an $H$ chosen by the index methodology, not by you. Know that methodology before you use it, because its hedge ratio will be wrong in exactly the regimes this chapter catalogs. (Contract codes, sizes, and later contract launches should be checked against CME's own documentation.)

### Deep-Dive Resource Graph

**Podcasts.**

- **"Why Treasuries Are 'Risky' Again"** (*Odd Lots*, with Carolin Pflueger of the University of Chicago, October 5, 2026). The stock–bond correlation sign decides whether the Treasury-futures leg of the hedge matrix hedges or doubles the loss. https://omny.fm/shows/odd-lots/why-treasuries-became-risky-again
- **"What We Learned About Treasuries on the Night of April 8"** (*Odd Lots*, with Ira Jersey of Bloomberg Intelligence, April 28, 2025). Who sold, and why the safe-haven hedge failed in an acute way after "Liberation Day": the hedge-ratio instability of this section as it happened. https://omny.fm/shows/odd-lots/what-we-learned-about-treasuries-on-the-night-of-april-8
- **"How The Crisis Nearly Blew Up One Of The World's Safest Trades"** (*Odd Lots*, with Josh Younger of JPMorgan, March 26, 2020). The Treasury cash-futures arbitrage failing in March 2020: the rates-side twin of the credit-ETF dislocation, and a reminder that the futures leg has its own basis risk. https://omny.fm/shows/odd-lots/how-the-crisis-nearly-blew-up-one-of-the-world-s-s
- **"Goldman Tells Credit Investors to Buy Cheap Hedges"** (*The Credit Edge*, with Lotfi Karoui of Goldman Sachs, February 13, 2025). A dated sell-side statement that hedge cost was "the lowest it's been in probably a very long time", with a pointer to the left tail: the price side of the CDX and equity-put legs. https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/goldman-tells-credit-investors-to-buy-cheap-hedges
- **"What the Actual ETF Is Going on Right Now"** (*Trillions*, March 19, 2020). Live commentary on ETFs in the 2020 crash, days after the LQD discount: the audio companion for the HYG/JNK leg. https://omny.fm/shows/trillions/what-the-actual-etf-is-going-on-right-now
- **"A Longstanding Fear About The Corporate Debt Market May Finally Be Coming True"** (*Odd Lots*, with Chris White of Viable Markets, March 23, 2020). Recorded in the March 2020 meltdown: search for yield, issuance and plumbing as the setup for forced selling, the mood in which the ETF leg of a hedge is priced. https://omny.fm/shows/odd-lots/a-longstanding-fear-about-the-corporate-debt-marke

**Practitioner Writing.** Markets Media (April 29, 2024), "CME US credit futures to begin trading on June 17": https://www.marketsmedia.com/cme-us-credit-futures-to-begin-trading-on-june-17 . FI Desk, "CME Group to begin trading credit futures in June": https://www.fi-desk.com/cme-group-to-begin-trading-credit-futures-in-june/ . CME Group, "Understanding Bloomberg credit futures" (2024) and "A practitioner's guide to credit futures" (2026) (title only). Rudin (2025), "Hedging Interest Rate Risk in High-Yield Bonds," in Fabozzi and de Jong (eds.), *Derivatives Applications in Asset Management*, Springer: https://ideas.repec.org/h/spr/sprchp/978-3-031-86354-7_24.html .

**Academic Papers.** Carr and Wu (2011), "A Simple Robust Link Between American Puts and Credit Protection," *Review of Financial Studies* 24(2): https://ideas.repec.org/a/oup/rfinst/v24y2011i2p473-505.html . Kapadia and Pu (2012), "Limited arbitrage between equity and credit markets," *Journal of Financial Economics* 105(3): https://ideas.repec.org/a/eee/jfinec/v105y2012i3p542-564.html .

**Data & Code.** iShares HYG: https://www.ishares.com/us/products/239565/ishares-iboxx-high-yield-corporate-bond-etf . iShares HYGH: https://www.ishares.com/us/products/264544/ishares-interest-rate-hedged-high-yield-bond-etf . SPDR JNK: https://www.ssga.com/us/en/intermediary/etfs/spdr-bloomberg-high-yield-bond-etf-jnk . CME Group (canonical root, Treasury futures specifications): https://www.cmegroup.com . `hedge_matrix`, `hedge_qp`, and `futures_contracts` in §8.9.

## 8.7 Case Studies: Three Times the Hedge Hedged the Wrong Thing

The three episodes below cover all three regimes of §8.2, in four years. The first two are replays, Ines's Friday ritual of freezing a real episode at a date and making the desk trade it blind. The third is a card she handed out the week after, for a week the desk had lived through.

### Case Study A: 2022, the Year "Negative Duration" Was Positive

#### Long Scene: The Year a PDF Said Zero (2022, replayed)

*A replay, cut off at the close of Friday 31 December 2021. The desk, its book and all dialogue are invented; the dates, yields, index returns and the Apollo note are sourced, and the spread path is approximate.*

A few days after the thirty-seven cents, late on a quiet afternoon, Ines turned the big screen at the end of the desk to face the room, which is how everyone knew it was a replay. She had frozen the tape at the close of the last trading day of 2021. The 10-year Treasury yield read 1.52%. The 2-year read 0.73% (FRED). Nothing else on the screen moved, because nothing after that evening was allowed to exist yet.

"House rules," she said. "You know what everyone knew that night and nothing they learned after. You write a card. I run the tape. The tape grades the card."

Theo's packet was two pages. The first described a book *(illustrative)*: \$200mm of single-B bonds, duration 4, analytical DV01 of \$80,000 a basis point. At the chapter's illustrative \$70.8 of DV01 per TY contract (§8.6), a full analytical hedge was 1,130 contracts short. The second page was Table 8.1, Ben Dor's 1998–2009 hedge ratios by rating, with the B row circled in Ines's pen. The card asked for three things.

> *Your card, before the tape runs: write your $H$, your TY count, and one sentence on why rates will move in 2022.*

Kaz finished first, which surprised no one. "B bonds at the average spread, $H = -0.04$. Rounded, zero futures. Strictly, a long of about forty-five contracts, which I decline to buy on grounds of dignity." They wrote *0* on the card and, underneath, *rates move for the reasons they have always moved; the table is eleven years of data.*

Mags wrote for a long time and then crossed most of it out. What survived was *Full hedge. 1,130. And sell some spread: buy CDX HY protection on half the book. Because the Fed said the word.*

"Which word?" Kaz asked.

"Doesn't matter which. When a central bank starts choosing its words, it's about to start choosing numbers. I have watched that happen more than once, and the bonds never enjoyed it."

Ines did not write a card. The dealer never does. She walked behind the three of them, reading over shoulders, and stopped behind Theo. "What's the pot?" she said, to the room. "Two hundred million of B paper and a year of rates. What are the odds? Ask yourselves who's dealing. For eleven years of that table, the Fed dealt: rates fell when the economy got scared, and spreads widened when it got scared, so the two legs pulled against each other and Kaz's zero was the right hedge. This year, inflation is the dealer. If inflation deals, it hurts both hands at once."

Theo had been staring at his card for five minutes. He was thinking, as he usually did when the numbers ran out, about documents. A bond indenture says what the issuer owes and when. It does not say why the Treasury market moves, and it does not care. The bond had no opinion about inflation. Every hedge ratio on Table 8.1 was a statement about how the *market* had behaved when rates moved, which was a statement about why rates had moved, which was exactly the thing he did not know.

He wrote: *1,130 TY, full duration, because the bond doesn't know why rates move and I don't either, so I won't bet the hedge on it. Then hedge the spread separately, with something that is spread.*

Ines read it twice, which on this desk means something. "Not bad. What's the something?"

"Something that moves with the high-yield market and not with Treasuries."

"That's a description, not a ticker. You can't sell a description." She took his card and put it face down on the desk. "I'm not grading this one until you can tell me what the second instrument is. Run the tape."

The tape ran, as it always does, faster than the cards had imagined. Ines moved it in chunks and said the numbers she was allowed to say. In the first quarter the rolling 60-day correlation between yield changes and relative spread changes, the $\rho$ of §8.2, climbed from below zero to above it *(the date depends on the window; illustrative)*. Nobody on the desk in the replay had a screen that showed it; Kaz's model, re-estimated on a trailing window, would notice months later. By early July the ICE BofA high-yield OAS had gone from roughly 310 bp to near 600 *(approx.)*.

That number had taken Kaz most of Thursday to find. FRED's free ICE BofA history now starts in October 2023 (§8.2), so the replay's 2022 spreads came out of the desk's own archive, a folder of CSVs saved by someone who had left the firm, with a column named `oas_final_v2` that turned out to be in percent on some days and basis points on others. Kaz had fixed it with an assertion and a sigh. Nobody in a replay ever sees that part, and every replay depends on it.

Ines stopped the tape in early July. "One change allowed. It costs you a point of the book to make it."

Kaz looked at their model, which re-estimated $H$ every month on a trailing 60-day window. It had finally noticed. The window now held a spring of days in which yields and spreads had risen together, and the estimate for single-B had climbed through one. "My window has caught up," they said. "$H$ is above one now. I'd like to put the hedge on."

"You'd be hedging the half of the year that's already happened," Ines said. "The window just told you what inflation did in March, April and May. It knows nothing about the next six months. Does the reason rates are moving still hold?"

"The model doesn't have a field for reason."

"Then it's going to keep finding out three months late, every time the reason changes." She let Kaz make the change, and took the point. "Let's see whether it was worth one."

It was, as it happened, worth something: the second half of 2022 still had a rate shock in it. But Kaz had paid half a year of losses for the privilege of buying the hedge after the window agreed, and the window would be just as late in the other direction the next March. Mags and Theo kept their cards.

On 24 October the 10-year touched 4.25%. By the last trading day of 2022 it had settled at 3.88%, and the 2-year was at 4.41% (FRED). Over the year the Bloomberg US Corporate High Yield index returned about −11.2%, the investment-grade Corporate index about −15.8%, and the US Treasury index about −12.5% *(approx.; secondary data summaries)*. The high-yield OAS ended the year in the high 400s *(approx.)*.

"Inflation dealt," Ines said. "Both hands. Grade yourselves."

The arithmetic was not subtle. Intermediate Treasury yields had risen by roughly 240 to 370 bp, the range between the 10-year's move and the 2-year's. On a duration-4 book the rate leg alone cost on the order of 10 to 15 points before carry, \$20mm to \$30mm on \$200mm *(illustrative arithmetic)*. An unhedged book ate every point of it, and with the spread leg widening and the carry partly offsetting it, did roughly what the index did, a loss of about a ninth of its value. Kaz's card had been that book until July. The hedge put on after the window agreed covered only the part of the rate shock that came later, and the change had cost a point on top. "High yield has negative empirical duration," Kaz said quietly, reading their own card back. "It said so in the table."

"The table was right about its eleven years," Ines said. "It was wrong about the twelfth."

Mags's card won the replay, and Ines graded it down anyway. The 1,130 contracts paid back most of the rate leg; a 10-year contract does not perfectly hedge a book whose duration sits at four years in a year when the 2-year rose half again as much as the 10-year, so some of the curve leaked *(illustrative)*. The CDX leg was where the card bled. Buying high-yield protection on \$100mm costs its spread every day it is held, about 3% a year at January's level, and it pays only on the days spreads widen. Marked at the July peak, the protection was up about ten points on the year. Marked at December, it had given more than half of that back *(approx.; illustrative sizing on the secondary spread path)*. Net, Mags's book was down a little, and the best number on any card.

"Right answer," Ines said. "Now tell me why."

"Because the Fed was going to hike into inflation and inflation is bad for credit."

"Exactly. You bet on why rates would move, and you were right about why. That's a macro trade. A good one. It's not a hedge." Ines tapped the card. "In a year when the reason is different, the same card is a short-rates position with protection attached, and it loses on both. We'll play that year next."

The reader's card is graded the same way. If it put $H$ near zero because Table 8.1 said so, it lost what Kaz lost. If it said full hedge because the Fed was about to fight inflation, it won Mags's money for Mags's reason, and it was a bet on the source of the rate move that happened to come in. If it said, in some form, *I don't know why rates will move, so I won't let the hedge depend on it*, it is Theo's card, and it is owed a grade the moment it can name a ticker.

Theo, it turned out, could not name one that afternoon. He thought about it on the train. The answer was in the hedge matrix of §8.6, which he had read and not yet used, and he worked it out properly over the next few days (§8.8).

The coda was not a card. It was the Apollo note of 3 December 2022 that §8.2's Trend Watch quotes, and Ines put it on the screen without comment.

Mags read it from her chair. "In 2022 the kids hedged B paper with nothing, because a PDF said empirical duration was negative. Lost on rates and spreads. Progress is losing the same money faster." She looked at Theo's rolling-correlation monitor, the one Kaz had built that week, for a long moment. "That's good, though. I'd have killed for that. I'd have killed for a *screen*."

"It would have crossed zero in the first quarter," Ines said, "months before Kaz's window agreed with it. So that's the floor on this desk: while that line is above zero, nobody hedges less than the full duration. When Theo can name his second instrument, we stop needing the line at all."

Theo added a line under the question on his sticky note: *Rates with rates. Spread with spread. Name the second instrument.* Chapter 10 (§10.7, Case Study C) tells 2022 again from the trend sleeve's side, where the same duration losses were somebody else's best year.

### Case Study B: March 2023, SVB, and the Hedge That Hedged Both Ways

#### Long Scene: The Hedge That Hedged Both Ways (8–13 March 2023, replayed)

*A replay, cut off at the close of Wednesday 8 March 2023. The desk trades a generic single-B book, not SVB paper, and nobody on it is restricted; the desk, its book and all dialogue are invented. Dates, yields, spreads, the 8-K figures and the April note prices are sourced.*

"We'll play that year next," Ines had said, and she meant it literally. A few days later the big screen showed the close of Wednesday 8 March 2023, and the room went quiet in the way it does when everyone already knows the ending and is trying to pretend they don't.

The tape that evening was busy but not frightening. After the close, SVB Financial Group had filed an 8-K. Its bank had sold available-for-sale securities with a book value of \$23.97bn for proceeds of \$21.45bn, and the company was raising \$2.25bn of capital. The 2-year Treasury closed at 5.05% and the 10-year at 3.98% (FRED). If you had lived through 2022, those yields were the point: the Fed was still hiking into inflation, and the market had spent a year learning that rates and spreads rose together.

The book on Theo's packet was the same \$200mm of single-B bonds, duration 4 *(illustrative)*. This time it came pre-hedged. The desk in the replay had sized its Treasury futures on a trailing 60-day window, the way Kaz's model did, and the window was full of 2022's lesson: rates and spreads moving together, $\rho$ positive, and an estimated $H$ of 1.1 *(illustrative)*. The book was short about 1,240 TY contracts against \$80,000 of DV01, a little more than the full analytical hedge.

"It's 7 a.m. Thursday," Ines said. "You've read the 8-K. You haven't read anything else, because nothing else exists yet."

> *Your card, Thursday 7 a.m.: keep the hedge at 1.1, cut it to Ben Dor's number for single-B (about zero), or keep the futures at one and add CDX HY protection for the spread beta. Write the number and the reason.*

Kaz kept the hedge. "The model says 1.1. A window is a window. Three months ago everyone wanted me to trust the window, and the window was right."

Mags had a different view and, unusually, no war story to go with it. She had been at a fund that was winding down for most of 2022, and she had her own memories of that particular week's bank paper (Chapter 6), which she did not offer. What she offered was a year. "This is '98 again. Something breaks, everyone runs to Treasuries, Treasuries rally, and the rally is the fear. In a fear rally your futures short loses money on exactly the day your bonds do. Take the futures off." Her card said *0*.

Theo had spent the days since the 2022 replay doing what Ines told him: naming the second instrument. His card said *Futures at $H = 1$, about 1,130 contracts, for the rates. CDX HY protection, sized to the book's DTS over the index's DTS, for the spread beta. I don't know which way the week goes and I don't need to.* He showed it to Ines before she asked.

"You named it," she said. "Good. Now we find out what it costs to be agnostic."

Thursday, 9 March, ran first. SVB's stock fell 60.4% to \$106.04, and more than \$40bn of deposits left the bank in a day. Ines read the numbers slowly, the way a dealer turns cards. The 2-year was falling; the high-yield index was widening. Kaz watched the book's P&L line on the replay screen go red on the futures and redder on the bonds, and said nothing for a while.

"The futures short is losing because Treasuries are rallying," Theo said. "And the bonds are losing because spreads are widening. The hedge is losing on the same day as the thing it hedges."

"Both ways," Ines said. "That's what a hedge ratio above one does in a flight to quality. In 2022 the two legs moved together, so a big futures short protected you. This week they're moving apart, so the same short is a second position. Same contracts. Opposite job."

Kaz asked for the replay's P&L explain for Thursday, because a replay runs the same risk system as the live book, and the explain came back in the familiar committee-designed format. For Kaz's book it had two red lines, *Rates hedge* and *Spread*, and one black one, *Rates (bonds)*, which the futures had more than cancelled. For Mags's book it had one black line and one red one, and a total close to flat. For Theo's it had four lines, two red and two black, sized almost exactly against each other, and a total near zero.

"Yours is boring," Kaz said.

"Boring is the point," Ines said. "Read the four lines. The bonds made money on rates and the futures gave it back. The bonds lost money on spread and the protection gave it back. What's left is the bonds against the index, which is the only thing Theo claims to know anything about. His explain tells you what he is paid for. Yours tells you what the Treasury market did."

On Friday, 10 March, the California Department of Financial Protection and Innovation closed the bank and appointed the FDIC as receiver. The ICE BofA high-yield OAS closed at 461 bp. Over the weekend, on 12 March, the Treasury, the Federal Reserve and the FDIC issued a joint statement on the failure. Kaz used the weekend, as replays allow, to re-estimate the model on the new data. Two days of observations in a sixty-day window moved the estimate a little. It still said $H$ was above one.

"The model hasn't noticed," Kaz admitted on Monday morning, which in replay time was ten minutes later.

"The model can't notice," Ines said. "Look at it. Your sixty-day window says $\rho$ is positive, because it remembers January. This week's realized $\rho$ is sharply negative. This week's hand and the sixty-day hand disagree. When they disagree, you are not holding what you think you are holding. That disagreement is the most important number on the screen, and you don't have a field for it."

Monday, 13 March, closed the scene. The 2-year Treasury yield ended at 4.03%, down 102 bp in three sessions, and the 10-year at 3.55% (FRED). High yield went the other way: the ICE BofA HY OAS widened 42 bp in a single day, from 461 bp on Friday to 503 bp on Monday, the largest daily widening since June 2020 (Reuters, via Kitco, March 14, 2023). It was the flight table of §8.2, $\rho$ sharply negative, the world Ben Dor's sample was built on, arriving exactly one year after the regime that broke it.

Ines graded with the chapter's own arithmetic. Over the window, take intermediate yields down about 70 bp and the book's spreads out about 60 bp *(illustrative)*. The bonds gain roughly $4 \times 0.70\% = 2.8\%$ on rates and lose $4 \times 0.60\% = 2.4\%$ on spread, for a net of about +0.4% unhedged. Mags's zero hedge was that book: up about 0.4%, in the week a large American bank failed. A full analytical futures short loses 2.8%, so a book hedged at one is down about 2.4%; Kaz's 1.1 lost a little more, about 3.1% on the futures, down about 2.7% in all. A card cut to a compromise of $H = 0.3$ loses 0.84% on the futures and finishes down about 0.4%. Theo's card was flat to both markets, as his four-line explain had said on Thursday, less whatever the CDX–cash basis did that week, which the replay did not have.

"So Mags won again," Theo said.

"Mags won twice," Ines said. "In 2022 she said inflation and was right. This week she said fear and was right. That's not a hedge ratio. That's a read on why rates are moving, made fresh each time, by somebody who has seen enough tables to know which one she's sitting at. It's a real skill. It's also a different job from yours." She turned to Kaz. "Your card was the only one that lost on both legs. Not because the model was bad. Because a trailing window is always fighting the last war."

"And mine?" Theo asked.

"Yours made nothing. In the week a bank failed and spreads had their worst day in nearly three years, your hedge made nothing and lost nothing. That's the grade." She pushed his card back across the desk, face up this time. "Keep it. You'll need it when you answer your own sticky note."

The reader's card gets the same three grades. If it kept 1.1, it lost on both legs. If it cut to zero, it won by reading the week's source of rate moves correctly, which is a forecast. If it put the rates hedge at one and the spread hedge in CDX, it gave up the chance to be right in return for not needing to be.

There was a coda, because Ines always has one. She moved the tape forward six weeks, to 25 April 2023. SVB Financial Group, the holding company, had filed for Chapter 11 on 17 March. The FDIC had frozen the holdco's \$2bn deposit at the failed bank. Two of the holdco's senior notes, from the same indenture and the same class of claim, were quoted that day at 69 for the 3.5% notes due 2025 and 57 for the 1.8% notes due 2031 (Debtwire, citing MarketAxess). Two notes six years apart in maturity, twelve points apart in price, and neither one cared what the 2-year Treasury had done in March. This was the recovery route of §8.3 made real: a price pinned to a claim on an estate, where the discount rate had stopped mattering. Whatever the twelve points between them were a bet on, it was not the yield curve.

Theo wrote the dates of both replays on the back of his sticky note, one above the other: 2022, $\rho > 0$; March 2023, $\rho < 0$; twelve months apart. Then the sentence Ines had left him with. Conditioning a hedge ratio on the source of the rate move is a classification problem, not a regression problem, and Chapter 10 (trend) and Chapter 12 (regimes) supply the classifiers.

### Case Study C: April 2025, Three Regimes in Seven Sessions

*The card is a desk exercise and the dialogue is invented; yields, spreads and index returns are sourced, and the grading arithmetic is illustrative.*

The third card was not a replay in the usual sense. Everyone on the desk except Theo had traded April 2025 live. Theo had watched it from a conference room at his old job, between drafts, with the vague sense that something in the Treasury market had broken and that it was somebody else's problem. Ines handed him the card the morning after the SVB replay, with a pencil.

The setup was one week of screen. On Wednesday 2 April 2025, after the close, came the tariff announcement. By the close of Friday 4 April the 10-year yield had fallen from 4.20% to 4.01%, and the ICE BofA high-yield OAS had gapped from 342 bp to 445 (FRED). Yields down, spreads out: the flight table.

> *Your card, Friday 4 April 2025, at the close: the 10-year is 4.01% and the HY OAS is 445 bp. Choose the hedge ratio you will carry into Monday, and write one sentence on why rates will move next week.*

Theo looked at it for a long time. "Two days ago this was the flight table. Rates rallied and spreads blew out, so the right hedge was small, maybe zero. If it's still the flight table on Monday, I want a low $H$. If it isn't..."

"If it isn't?"

"Then I'm Kaz in March 2023." He wrote the same card he had written for SVB: futures at one, CDX for the spread beta, no sentence about why rates would move. Ines took it without comment, which he had learned was a grade of its own.

Here is what the screen did next (FRED, closing OAS and yields; CCMG for the monthly path):

| Date (2025) | 10-year | HY OAS | BB | B | CCC | IG | What the hedge did |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | :--- |
| Apr 2 | 4.20% | 342 | 212 | 353 | 925 | 96 | (baseline, before the tariff announcement) |
| Apr 4 | 4.01% | 445 | n/r | n/r | n/r | n/r | Rally plus widening: $\rho < 0$. The futures short loses into the widening; a full hedge forfeits the rally's cushion |
| Apr 7 | 4.15% | 461 | 306 | 486 | 1,137 | 120 | Sell-off plus widening: $\rho > 0$. Under-hedged book loses on both legs |
| Apr 11 | 4.48% | 426 | n/r | n/r | n/r | n/r | Sell-off plus tightening: $\rho < 0$ again |
| Apr 30 | 4.17% | 394 | n/r | n/r | n/r | n/r | Month: Treasuries +0.63%, HY −0.02% |

*Table 8.3. April 2025 (FRED ICE BofA OAS in bp and DGS10; "n/r" = not recorded in our extract; monthly index returns from CCMG's April 2025 recap).*

The month's summary statistics hide the week. For April as a whole, CCMG reports Bloomberg index returns of +0.63% for Treasuries, +0.06% for US Credit, −0.02% for High Yield, and −0.68% for the S&P 500. Victory Capital reports month-over-month widening of 13 bp in IG and 39 bp in HY. GW&K noted that the range in the 10-year yield that month was the widest since March 2023, "when Silicon Valley Bank folded." Inside that range, the sign of the rate–spread comovement flipped twice in seven sessions.

Grading the card makes the point in one line of arithmetic. Take a duration-4 book that moves with the index spread, and ask what hedge ratio would have left it flat over each stretch *(illustrative arithmetic on Table 8.3)*. From Wednesday to Friday, with yields down 19 bp and spreads out 103, the answer is about −4: the flat book needed to be *long* Treasury futures, because the rally was the fear. From Friday to Monday, with yields up 14 bp and spreads out 16, it is about +2: inflation's table, where the futures short has to cover more than the bond's own duration. From Monday to Friday 11 April, with yields up 33 bp and spreads in 35, it is about zero: the spread tightening paid for the rate sell-off by itself. A card that read Friday's flight table and carried a low $H$ into Monday lost on both legs on Monday. A card that carried a high one was right on Monday, and by the next Friday it was holding a profitable short-rates bet it had never meant to make. Theo's card, the same two-instrument hedge as the week before, had nothing to say about which table the market was at and did not need to; it was left holding the book against the index and a basis the exercise does not price.

Ines put the week as a hand history in two lines. "The board changed three times in seven sessions. Your hedge ratio is your read on the table, so you update it when the board changes, not when the month ends."

Then Ines showed him what the desk's own estimator had done with the week, which was the part she minded most. The rolling 60-day CCC hedge ratio computed on FRED data was close to zero in the window ending April 30 and reached −0.67 by the window ending May 30 (and −0.78 for the window ending May 23). The *estimate* swung hard negative *after* the event, which is exactly when it was least useful. Rudin (2025), using the Bloomberg US Corporate High Yield index, makes the general point: hedging high yield with Treasury futures based on duration "often leads to increased portfolio volatility." Figure 8.4 draws the whole three-year window of the rolling estimate.

![Figure 8.4: The rolling 60-day hedge ratio on FRED data, January 2024 to October 2026. The CCC estimate was near zero at the end of April 2025, fell to −0.78 on May 23, weeks after the tariff shock, and rose above 1.8 by June 2026; high yield follows it at smaller amplitude, and investment grade stays between 0.79 and 1.04. Source: FRED BAMLH0A3HYC, BAMLH0A0HYM2, BAMLC0A0CM and DGS10, computed 2026-10-18 as H = 1 + s̄ρσ_s/σ_y on daily relative OAS changes (the free ICE BofA history starts in October 2023).](assets/figures/ch08_rolling_hedge_ratio.png)

Kaz, who had traded that week live with a trailing window and remembered it, took the lesson in their own vocabulary. When the realized one-week $\rho$ changes sign inside the week, the estimate has not become less accurate so much as less meaningful, and the desk's response since then has been to lower its confidence in the hedge ratio rather than re-estimate it harder: raise the ridge penalty $\eta$ of §8.6, shrinking the hedge toward a robust prior; widen the band within which the hedge is left alone; and lean on the instrument that hedges the spread factor directly (CDX HY) rather than the one that hedges it through a correlation (futures at $H < 1$). "It is the same answer as Theo's card," Kaz said, "arrived at by a longer road."

## 8.8 What's Left Is IDO (and How to Prove It)

After the Treasury leg, the empirical rate beta, and the DTS-scaled market spread factor, the residual still is not idiosyncratic. Collin-Dufresne, Goldstein and Martin (2001) regressed credit spread changes on the variables structural models say should matter (leverage, volatility, rates, the slope of the curve) and found "rather limited explanatory power." Worse for anyone hoping for a clean residual, the unexplained part was "mostly driven by a single common factor." There is a market-wide spread shock the theory variables do not see: liquidity, risk appetite, dealer balance sheets, flows. If you call that residual IDO, you will discover in the next drawdown that every one of your "idiosyncratic" positions shared it.

### The definition, in four subtractions

Let $\text{DTS}_{i,t-1}$ be bond $i$'s DTS at the previous close, known before the return occurs, so the definition cannot look ahead. The pure-IDO return is defined by four subtractions, and Theo, who had now been told twice to name his second instrument, walked the cold-open bond through them with a pencil; the table after them is his worksheet.

1. **Rates.** Excess return over KRD-matched Treasuries, $R^{\text{xs}}_{i,t} = R^{\text{tot}}_{i,t} - \sum_k w_{i,k}R^{\text{TSY}}_{k,t}$ (§8.1). This removes the full analytical rate exposure. The part of the spread move that is correlated with rates stays in $R^{\text{xs}}$, and the market spread factor in the next step removes it, whatever $\rho$ happens to be.
2. **Market, sector and rating spread factors, DTS-scaled.** Regress $R^{\text{xs}}_{i,t}/\text{DTS}_{i,t-1}$ on factor returns $F_{k,t}$ with Dimson-summed loadings for stale marks (§8.5):
$$
\frac{R^{\text{xs}}_{i,t}}{\text{DTS}_{i,t-1}} = \sum_{k} \beta^{\text{D}}_{i,k}\,F_{k,t} + \tilde\epsilon_{i,t} .
$$

Step two leaves a residual for every bond, and Collin-Dufresne, Goldstein and Martin say those residuals are not yet independent of one another. The next step needs one more idea.

> **Math, Gently.** *The common whisper: what a first principal component is.* Take three bonds' residuals after every named factor has been removed, and draw them as three noisy lines over a month. If they were truly idiosyncratic, their wiggles would be unrelated. Often they are not. On some days all three dip together, as if the market had whispered something none of the named factors heard. The first principal component is the single line that, scaled up or down separately for each bond, explains as much of that shared movement as one line can. Its value on a given day, $g_t$, is how loud the whisper was; each bond's scaling, its loading $v_i$, is how closely that bond listens. Removing it is subtraction. In the margin: on a day when the three residuals are $(+2, +1, -3)$ and the whisper is $g = +1$ with loadings $(1, 0.5, -0.5)$, the whisper accounts for $(+1, +0.5, -0.5)$ and leaves $(+1, +0.5, -2.5)$. The third bond's move was mostly its own; half of the first bond's was not. Chapter 7-B (§7-B.5) owns the full treatment, including how to tell a real component from noise. Here it is a subtraction.

3. **The common residual factor.** Take the panel of scaled residuals $\tilde\epsilon$ (time by bonds), extract its leading principal component $g_t$ with loadings $v_i$, and remove it: $\tilde\epsilon^{\perp}_{i,t} = \tilde\epsilon_{i,t} - v_i\,g_t$. This is the Collin-Dufresne–Goldstein–Martin factor, estimated rather than named. On the cold-open day the desk's estimate of the whisper was close to zero *(illustrative)*, so this step took nothing off Theo's bond. On other days, and in other books, it takes a great deal, as the next subsection but one shows.
4. **Scale back to returns.**
$$
\text{IDO}_{i,t} \equiv \text{DTS}_{i,t-1}\,\tilde\epsilon^{\perp}_{i,t} .
$$

What remains is small, noisy, and yours. That is not a disappointment. That is the definition.

### Theo's thirty-seven cents, answered

Theo's worksheet used *illustrative* market data for the day, and the step-three whisper was close to zero: the B-rated index's relative spread change was −1.2%, and the bond's own was $-9/620 = -1.45\%$. With $\text{DTS} = 4.0 \times 0.062 = 0.248$:

| Component | Calculation | Cents on \$95 |
| :--- | :--- | ---: |
| Carry | §8.1 | +3 |
| Rates (analytical) | $-4.1 \times 0.0018$ | −70 |
| Market spread beta | $-0.248 \times (-0.012)$ | +28 |
| Bond-specific spread (IDO) | $-0.248 \times (-0.0145 + 0.012)$ | +6 |
| Decomposition residual | plug (probably tomorrow's stale-price catch-up) | −4 |
| **Total** | | **−37** |

Of the thirty-seven cents, about six were the bond. Four were the pricing service, and they will probably reverse tomorrow (§8.5). The rest was the Treasury market and everyone else's opinion of the economy. Kaz's "alpha" of 34 cents was 28 cents of beta and 6 cents of alpha. Theo peeled the sticky note off his monitor and wrote "6" on it. Figure 8.5 draws the table as a waterfall.

![Figure 8.5: The thirty-seven cents, itemized as in the table above: carry +3, analytical rates −70, market spread beta +28, bond-specific spread (IDO) +6 and a −4 decomposition residual sum to −37. Kaz's "alpha" of 34 cents is 28 cents of beta and 6 of IDO. Illustrative: the cold-open B3 bond (price 95, modified duration 4.1, OAS 620 bp) on the chapter's illustrative day (10-year +18 bp, B-index relative OAS change −1.2%, the bond's own −1.45%).](assets/figures/ch08_thirty_seven_cents.png)

The table also shows the cleanest version of the hedge. The empirical-duration approach hedges the 28 cents of market spread beta *indirectly*: it shorts fewer futures because, on average, spreads tighten when yields rise. That works while $\rho$ holds and fails when it flips (§8.7). The two-instrument approach hedges each factor with its own instrument: futures at $H = 1$ for the 70 cents of rates, and CDX HY sized at $\text{DTS}_i/\text{DTS}_{\text{CDX}}$ for the 28 cents of spread beta. It does not depend on $\rho$ at all. It pays for that robustness with the CDX–cash basis and the index roll, and it hedges away spread beta you might have wanted to keep, which is Ines's poker hand from §8.2. Which hedge is right depends on what Theo is paid for, and when he asked, Ines answered before he had finished the sentence. "Your mandate is IDO. So it's the two-instrument hedge. A view on $\rho$ is not your job. If it were, we'd pay you for it."

> **[SOURCE EXTRACTION]** *Ben_Dor p.220:* "the low explanatory power (R2 = 8%) suggests that there are other factors that influence the performance of the strategy."
>
> **Annotation.** Ben Dor tests a DTS-neutral "short empirical duration" strategy (long Ba, short Baa) and finds a significant loading on rates (0.39, $t = 3.86$) that explains only 8% of its return variance. That is a pattern to recognize. A strategy can have a real, statistically significant factor exposure that is economically small next to its residual. The IDO ledger reports both: the loading's $t$-statistic (is the exposure real?) and the factor's share of variance (does it matter?). A residual that is 92% of variance is either a great deal of alpha or a great deal of factor you have not named yet. The ledger's job is to tell those apart.

### The common whisper, at book scale

#### Long Scene: Twelve Residuals (Dov Adler's pod, the last week of September 2026)

*Dov Adler's pod and Vantress Capital Management are fictional composites. The pod's twelve pairs, their sizes, limits and P&L, and every line of dialogue are illustrative; the Sharpe-ratio arithmetic is public.*

The orange line appeared on a Tuesday, which Wen Zhao said was the worst day for it, because Monday's orange lines could be blamed on the weekend.

Dov Adler was running twelve pairs that week, each built the way PB-03 had been built in its replay (§8.4). Every morning the platform's factor model x-rayed each pair and reported what was left after everything it could name: the market spread factor, sectors, rating buckets, rates by key rate. What was left was supposed to be Dov's. On his monitor, above a dated thesis for every pair, was a sticky note in his own handwriting: *IDO or it didn't happen.*

The x-ray was clean. Net DTS sat inside ±5% of gross, the beta to CDX HY inside ±0.05, and no sector cell was over its cap. The orange line was about none of that. It was a ratio on the risk summary that nobody reads until it changes colour: realized idiosyncratic volatility over the last sixty days, divided by the risk model's forecast. It read 1.9.

Marcus Oyelaran called at 8:10. He never asks what the view is. "What are you long that you didn't mean to be?"

"Nothing," Dov said. "Every pair is flat to the model. Look at the factor screen."

"I am looking at it. The factor screen shows me what the model can name. It says your idio is twice as volatile as twelve independent residuals should be, and twelve independent anythings don't do that. Correlate your residuals with each other and call me back."

Wen did it, and it took most of the morning, because nothing on a desk is as simple as "correlate your residuals." The pairs had been opened on different dates, so the twelve series started in different places. Three of the short legs had gone a day without a mark in the week a lender recalled bonds, and the explain had filled those days with zeros, which is a smoothing model nobody chose (§8.5). She cut the panel to the sixty days on which all twelve pairs had real marks, scaled every residual by its pair's DTS so that a wide pair could not shout over a tight one, and computed the sixty-six pairwise correlations. Their average was 0.28.

"Nearly point three," she said. "Every pair against every other pair. It isn't one bad apple. It's the crate."

Dov did the next part in his head and did not enjoy it. If twelve equally sized residuals with volatility $\sigma$ are independent, the book's idio volatility is $\sigma/\sqrt{12}$, about $0.29\sigma$. With an average correlation of 0.28 it is $\sigma\sqrt{(1 + 11 \times 0.28)/12} = \sigma\sqrt{4.08/12}$, about $0.58\sigma$. The risk model had forecast the first number and the book had delivered roughly the second. The orange 1.9 was not noise. It was the book saying that a large part of what Dov called idiosyncratic was common to all twelve pairs.

Wen ran step three of the definition above on the panel: the first principal component of the twelve residuals. Every loading had the same sign, and the component explained about a third of the residual variance, which squared with the 0.28. Sorted by loading, the heaviest pairs were the ones whose long leg was the wider, less traded name and whose short leg was the tighter, more liquid one, which described most of the book. "It's the same whisper in every pair," Wen said. "Whatever the market does to the bonds dealers least want to hold, we're long it twelve times."

"It's not in the factor model."

"It's not in *the vendor's* factor model. It's in ours now." She saved the loadings. Chapter 9 will put a name on what she found; for the pod that morning it was enough that it had a number.

When Dov called back, Marcus did not ask for the trades to come off. He explained why the platform cared, which on a platform is the same request in a politer voice. A multi-manager firm buys residuals from dozens of pods and pays each pod on its own. If the residuals are independent, adding pods adds Sharpe under a square root. If they share even a little, the arithmetic caps it: the platform's Sharpe ratio is the pod Sharpe times $\sqrt{N/(1 + (N-1)\rho)}$, and it can never exceed the pod Sharpe divided by $\sqrt{\rho}$. At a pod Sharpe of 0.75 and a cross-pod correlation of 0.10, forty-five pods reach 2.17 against a ceiling of 2.37 (the formula is the one Dan Morillo set out on *Odd Lots*, 7 October 2024; the Sharpe ratio, correlation and pod count are this book's illustration, not his). "Your twelve residuals have a common part," Marcus said. "So does the next pod's. If it's the same common part, and in credit it usually is, every pod that's long the illiquid name raises $\rho$ for everybody. The platform can buy that factor for a few basis points in an index. It can't afford to buy it from you at a residual's price."

"So what do you want?"

"I want the ledger to say what it is. Hedge it if you can find an instrument that's mostly that factor. Shrink the pairs that load on it hardest if you can't. Or keep it, report it as its own line in the explain, and get paid for it like a factor. What I don't want is to meet it for the first time in a drawdown."

Dov wrote a sentence with a date in it, as he does: *By 30 November 2026, mean residual correlation across the book below 0.15, or the common component reported as its own line in the explain.* Then he opened the Pair Book's ledger and filled in a cell that had been blank since the book began. Residual correlation: 0.28, measured 29 September 2026. Chapter 8-D finds it a week later, still there, on the ledger's bottom line. A pod's PM, its risk manager and its platform agree on one thing when they agree on nothing else: idio is whatever the hedge leaves, so the hedge had better leave only the issuer.

### The IDO ledger: proving it

A residual is a claim until a signal predicts it. On Theo's desk the proof is a month-end meeting in the small room with the blind that does not close, at which a strategy may describe itself only in three numbers.

October's meeting was Kaz's. They had a relative-value signal that ranked single-B bonds once a month *(illustrative)*, and the first slide said it had an information coefficient of 0.06 with a $t$-statistic of 2.4 over three years. Mags, who attends these meetings because she is suspicious of anything called adjusted and had heard there would be adjustments, asked the only question she ever asks of a slide.

"On what?"

"Monthly excess returns."

"Then some of that is the market. Show me it on IDO."

Kaz had run it on IDO and had not led with it. On IDO the coefficient was 0.03 and the $t$-statistic 1.3.

The three numbers on the ledger are the ones Kaz's slide had buried. The first is the residual volatility of the strategy's portfolio, $\sigma(\text{IDO})$: the risk budget the strategy actually consumes after its hedges, and the number to set beside the risk model's forecast, since a residual more volatile than forecast has a common part in it (the scene above). The second is the information coefficient: the cross-sectional Spearman rank correlation between the signal at $t-1$ and $\text{IDO}_{i,t}$, $\text{IC}_t$, averaged over months. (Spearman's correlation is the ordinary correlation computed on ranks: sort the bonds by signal and by IDO, number them, and correlate the numbers.) Ranks are used because credit residuals have fat tails, and ranks keep one defaulting CCC from deciding the month. The third is its $t$-statistic over $T$ months, $t = \overline{\text{IC}}\,\sqrt{T}/\mathrm{sd}(\text{IC}_t)$, and Chapter 7's warning comes attached: a $t$ of 2 after forty specification searches is not a $t$ of 2. Mags asked how many specifications Kaz had tried before the one on the slide. Kaz said "several." Mags said that "several" is a number in the same way that "adjusted" is a number.

The fundamental law, $\text{IR} \approx \text{IC}\sqrt{\text{BR}}$ (Chapter 9), connects the ledger to the question the PM is actually asking. With a breadth of 200 independent bets a year *(illustrative)*, Kaz's excess-return IC of 0.06 implies an information ratio of about 0.85, and the IDO coefficient of 0.03 implies about 0.42. If the IC is measured on raw excess returns, the IR it implies is partly a beta IR, and it disappears in the first regime change. If it is measured on IDO, it is the desk's. "Half your IR was the market," Mags said, gathering her folders. "Bring me the other half next month, with more months under it." IDO or it didn't happen.

## 8.9 The IDO Engine: A Reference Implementation

### Quant-Shop Life: The Window That Shrank

*A fictional composite: a systematic credit asset manager running long-only, benchmark-relative portfolios with a monthly rebalance. The firm, its people, the job and its numbers are invented; FRED's change to its ICE BofA history is real and stated on the FRED series pages.*

Elif Arslan had been a junior quant at the firm for ten months, long enough to own one job outright and not long enough to have chosen it. The job was `hbucket_monthly`. On the first business day of every month it pulled the ICE BofA OAS series by rating from FRED, pulled Treasury yields, re-estimated the empirical hedge ratio for each rating bucket over a 60-month window, and wrote a six-row table to a shared drive. The Treasury-futures overlay, which kept every portfolio's duration inside a band around its benchmark, read the table at 10 a.m. Nobody read it before then, including, most months, Elif.

In May 2026 the job did not fail, and that was the problem. Its backfill step asked FRED for sixty months of history, got back thirty-six, and said nothing, because nothing in the code had ever asked how many rows came back. FRED's own series pages explained why: starting in April 2026 the ICE BofA series include only three years of observations. The job estimated over what it had. The single-B hedge ratio, which had sat near 1.0 for months because the 60-month window still held 2022, came out near 0.7 *(illustrative)*, and the overlay, which trusted the table the way the table trusted FRED, bought back about thirty percent of its futures short across the high-yield sleeves by lunchtime.

Elif found out on the following Monday, by accident, because the overlay's trade report was longer than usual and the operations analyst who reconciles it had asked, politely, whether something had happened.

The risk committee met on Tuesday. It asks one question of every number it is shown, and it asked it of this one: why is this different from last month? Elif had prepared two slides. The first said the hedge ratio had moved because the window had lost 2022, the inflation table of §8.2, so the estimate now came only from flight-table and nobody-table years. The second said that 2026 so far had in fact been a nobody table, so a lower number was not obviously wrong. The committee chair, who had sat through enough of these meetings to recognize the shape, summarized it more honestly than either slide. "So a parameter moved and a data vendor truncated a series on the same morning, and you can't yet tell us which did what."

"Not yet," Elif said.

"Then the overlay goes back to last month's table until you can."

It took her two weeks, most of them spent rebuilding a 2021–2023 OAS history from an archived file and checking it against the firm's TRACE-based series (Appendix B), and the answer was dull: about two-thirds of the move was the window and one-third was the year. The fix was duller. Two lines went into the job's specification. The first was an assertion that the estimation window holds the number of observations its name promises, so a 60-month window that receives 36 months stops and says so. The second was an alarm on the rolling 60-day correlation between yield changes and relative spread changes that fires when it changes sign, the same guard that ends the GUARDS line of the robot spec in §8.10. Model-risk guidance has a name for this kind of thing, ongoing monitoring, which SR 11-7 lists among the three parts of model validation. The committee had a shorter name for it, which was "finally." The next time the table moved, it moved with a reason attached, and the reason was in the email.

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

The EXPLAIN email in the cold open footed to the cent and still could not say who owned four cents, and every item on Kaz's drawer list in §8.1 fails the same way: quietly, with a total that foots. At PJT a closing ended with a checklist on which somebody initialled every condition precedent, because nobody accepted "it looked fine." So before any of the machinery, the first block builds the thing that will check it.

The block builds almost nothing, and everything after it leans on it. It imports `numpy` for the arrays and linear algebra, and from `scipy` the optimizer that the bounded hedge in Listing 8.6 will need and the statistics module that the information coefficient in Listing 8.7 will need. It creates one random-number generator, `RNG`, seeded with 8, from which every simulated series in the later blocks is drawn, so the run produces the same numbers every time. It creates `CHECKS`, an empty dictionary that serves as the scoreboard. And it defines `report(name, ok, detail)`, which stores `bool(ok)` under the check's name and prints one line: PASS or FAIL, the name padded to forty characters, and a detail string that shows the number behind the verdict. Eighteen calls to `report` are scattered through the later blocks. The last block prints the tally and asserts that every check passed, so a clean run ends with 18/18 and a broken one stops with the offender's name. A comparison against NaN is False, so a series that quietly turned to NaN lands as FAIL rather than as silence.

Use this pattern when the point of the code is to be re-run after every edit. Do not mistake it for a test suite: production code on a desk wants independent tests, each with its own seed and tolerance, run by a test runner. The edge case that bites is the shared generator. Because every block draws from the same `RNG`, the data a block sees depends on how many numbers the blocks above it consumed. Insert a simulation above Listing 8.3, or swap two blocks, and every later series changes. A tolerance that sat comfortably at the original draw may now sit on a knife edge, and the resulting FAIL will look like a modeling bug when it is a reshuffled deck. Anyone extending the engine should give the new block its own generator and leave the old blocks their cards.

*The full listing is [Listing 8.1 in Appendix F](#code-8-1).*

Theo built the thirty-seven-cent table by hand, with a calculator, a sticky note, and the particular adrenaline of being wrong in public. That works once. A book of nine hundred bonds produces nine hundred of those tables every night, and each is worth something only if the signs are right, including on the nine hundredth, which arrives from a vendor feed in basis points because someone upstream felt like it. The decomposition is therefore the first thing the engine automates: one function, one table, a hard stop on the unit mistake, and ROBO's favorite sign error labeled in a comment so that nobody reintroduces it.

`decompose_returns` takes the day's realized total return, the bond's yield and OAS, the Treasury yield change and the spread change, the two durations, convexity, and `dt`, the fraction of a year under 30/360. Everything is a decimal: 0.0018 is 18 bp. It accepts scalars or arrays of shape (T,), converts the return and rate arguments to floats, and raises if any daily Treasury or spread move exceeds 0.05, which is what a basis-point feed looks like to a function that expects decimals.

It then builds the sources of §8.1. Yield carry is `y * dt`. Rates is `-D_mod * dy_tsy`. Spread is `-D_spr * ds`, using the spread duration, which differs from the rate duration for floaters and callables. Convexity is half the convexity times the square of the total yield move. The residual is the realized total return minus those four. OAS carry, `s * dt`, is stored in the same dictionary but kept out of the sum, because it belongs to excess-return work and adding it to total return would count the Treasury leg twice. A final assertion re-adds the five pieces and requires them to match total return to 1e-10. Run on the cold-open inputs, in cents on a \$95 price, it returns rates of minus 70.1, spread of plus 34.2 and a residual of minus 4.1, which is the §8.1 table.

Use it every night as the first step of the P&L explain, before any factor regression touches the numbers. Do not expect it to say anything useful on the day a bond gaps twenty points; the expansion assumes small moves and no default, and the residual will simply tell you so. The edge case that bites is that the footing assertion cannot catch bad economics. The residual is a plug, so the pieces sum to the total by construction, and the assertion catches only shape mistakes and NaNs. The unit guard looks only at the two moves. Hand the function a yield of 11.1 instead of 0.111 and the carry balloons to about 290 cents, the residual swings to about minus 294, and everything still foots. The only alarm is the size of the residual, so monitor it per bond, per day.

*The full listing is [Listing 8.2 in Appendix F](#code-8-2).*

At 10 a.m. on the first business day of May, Elif's `hbucket_monthly` ran this estimate on thirty-six months it believed were sixty, and nobody noticed until the following Monday. A hedge ratio that has changed sign twice in five years is an estimate to be re-run on a schedule, with a second method standing by to say whether the first is lying, so it becomes the next block.

The block holds two functions and a test bench. `empirical_duration(R, dy, D, s)` flattens its four inputs, so bonds and days can be stacked into one long sample, and regresses return on two columns with no intercept: `-D * dy`, the analytical rate exposure, and `-D * s * dy`, the same exposure scaled by the bond's spread. The coefficients are the $\beta$ and $\gamma$ of §8.2. It returns them along with a small function that maps any grid of spreads to the hedge ratio $H(s) = \beta + \gamma s$. `h_closed_form(s, rel_ds, dy)` is the cross-check. It computes the sample correlation and volatilities of relative spread changes and yield changes and returns $1 + s\,\rho\,\sigma_s/\sigma_y$, the two-factor formula, with no regression at all.

The bench simulates 2,500 days with 6 bp of daily yield volatility, 2% of daily relative-spread volatility, and a correlation of minus 0.4. That makes the linkage factor about minus 13.3 per unit of decimal spread, so a four-year bond at 6% should hedge at 0.20. Four copies of the bond, at spreads of 1%, 3%, 6% and 9%, are stacked and fed to the regression. It returns 0.23, the closed form returns 0.23, the population value is 0.20, and $\beta$ lands near 1. Even with 2,500 clean days the estimate misses the truth by 0.03, which is a reasonable floor for what real data will do.

Use it on a rating bucket, daily or weekly, re-estimated monthly. Do not feed it stale daily high-yield marks without the §8.5 treatment, and do not pool across a window in which $\rho$ changed sign, because the regression will average two regimes into a hedge ratio that fits neither. The edge case that bites is spread dispersion. The two columns are proportional when every bond has the same spread, and then $\gamma$ is not identified. `lstsq` does not complain. It returns a minimum-norm split that is right at the one spread you sampled and flat everywhere else; a run of this listing with a single spread level gave 0.23 at a 1% spread where the truth was 0.87. With a narrow range of spreads the split is merely noisy. Either way, read $H(s)$ only inside the range of spreads the sample actually contained.

*The full listing is [Listing 8.3 in Appendix F](#code-8-3).*

By the Wednesday after the thirty-seven cents, Kaz had a Dimson regression running against every factor on the desk's list, and the printout started the argument of §8.5 about which lags were staleness. Mags priced by phone and by grudge, and the grudge was usually a day old. For the engine the point is plainer: every beta estimated on daily marks arrives shrunk by a fraction nobody printed on the file. The desk needs a detector, a correction for the beta, a correction for the whole series, and a bench where the truth is known, so it can see whether the corrections work before they are pointed at real bonds.

The block holds five small functions and a test bench. `lagged(f, k)` shifts a series so that `out[t] = f[t-k]`, with NaN where nothing is defined; a negative `k` is a lead. `ols_slope` is a univariate slope that drops NaN pairs. `dimson_beta(r_obs, f, lags=2, leads=0)` runs one multiple regression of the observed return on the factor at every lag and lead, with an intercept, drops any row containing a NaN, and returns the sum of the slopes together with the slopes by lag. It refuses more than five lags or leads. `scholes_williams_beta` runs three separate univariate regressions on the lead, the same day and the lag, adds the slopes, and divides by one plus twice the factor's first-order autocorrelation. `desmooth(r_obs, theta)` first checks that the smoothing polynomial's roots lie outside the unit circle, raising if they do not, and then recovers each true return from the observed one and the previous reconstructed values.

The bench takes the relative spread move `x` from Listing 8.3 and builds a bond with DTS of 0.24 (a four-year spread duration at 6%), then smooths its returns with weights of 0.5, 0.3 and 0.2. Plain OLS recovers 0.49 of the true beta, which is the first weight. Dimson with two lags recovers 1.005. Scholes–Williams recovers 0.81, because it can return only one lag's worth of the missing 0.5. The smoothed series has 0.61 of the true volatility, against a theoretical 0.616. The de-smoothing weights are not given to the function. They are the Dimson lag coefficients divided by their sum (0.50, 0.295, 0.205 here), and with them the volatility ratio returns to 1.00.

Use these on rates and credit-index factors, where the lags are staleness, and not on lagged equity coefficients, which may be signal (§8.5). The edge case that bites is the start of the recursion in `desmooth`. It begins as a copy of the observed series and starts correcting at observation q, so the first few days stay stale, and each corrected value feeds the next, so an error in the estimated weights compounds down the series. That is why the check scores from observation 50. The invertibility guard is not decoration: the product of the polynomial's roots has magnitude equal to the first weight over the last, so a bond whose last weight exceeds its first can never pass it.

*The full listing is [Listing 8.4 in Appendix F](#code-8-4).*

The pod PM's orange line in §8.4 came from a DTS ratio nobody had computed on her blotter: the long carried 2.8 times the short's DTS, and the "pair" was \$32mm of single-B beta with a short attached. Wen's first move in Twelve Residuals (§8.8) used the same unit, scaling every residual by its pair's DTS so a wide pair could not shout over a tight one. A desk turns that unit into three small tools. One computes DTS and refuses the inputs that break it. One puts excess returns into per-DTS units, so a bond at 80 bp and a bond at 800 bp can share a covariance matrix without the first principal component announcing that the 800 is more volatile. One sizes a pair so that net DTS is zero.

`dts(D_spr, oas)` multiplies spread duration by OAS in decimal, and raises a `ValueError` if any OAS is zero or negative. It does not fall back to absolute spread changes; the error message names that fallback and leaves the choice to the caller. `dts_scale(xs_returns, dts_lag)` divides excess returns by the previous close's DTS, which gives approximately minus the relative spread change, the quantity that is comparable across credits. `dts_pair_hedge(dts_long, dts_short)` returns the short notional per unit of long notional that nets DTS to zero, which is simply the ratio of the two.

The tests exercise the §8.4 claims. A two-year bond at 200 bp against a four-year bond at 100 bp has DTS of 0.04 on both sides, and the pair hedge is exactly 1.00. A pair with equal five-year durations at 300 bp and 150 bp needs a hedge of 2.00, and the net OAS carry, 0.03 minus 2 times 0.015, is zero: the pair has been stripped of the carry as well as the beta. The last check simulates four bonds with DTS of 0.05, 0.12, 0.24 and 0.40, all hit by one common relative spread shock of 2% a day plus a little idiosyncratic noise, and regresses each on the equal-weighted average of the four. The betas come out at 0.24, 0.59, 1.18 and 1.99, against DTS ratios of 0.25, 0.59, 1.19 and 1.98. Since the shocks are common and proportional by construction, this proves the algebra, not the market.

Use DTS as the default risk unit, and scale before any covariance or principal-components step. Be careful in the CCC tier, where relative moves are the least common (§8.4). The edge case that bites is the lag. `dts_scale` divides by whatever it is handed; the name `dts_lag` is a promise, not a shift. Pass it same-day DTS and the denominator contains part of the move being scaled: a bond that doubles its spread has its scaled return halved, so the largest moves are the ones the scaling distorts most.

*The full listing is [Listing 8.5 in Appendix F](#code-8-5).*

Theo's four windows in §8.6 ended on one question, how much of each to sell, and the screen offered five cousins: a Treasury future, a credit index, two high-yield ETFs that are nearly the same security, and an equity put. Solving that by feel produces the classic result, a long position in one ETF and a short position in its twin, each large enough to be embarrassing and the net just small enough to ignore. Solving it with a plain regression produces the same thing with better arithmetic. The engine needs a hedge that survives the twins, respects the limits a trading desk actually has, and comes out in units a trader can send to a broker.

`hedge_matrix(r_p, R_H)` takes the book's return series and a (T, m) matrix of instrument returns per \$1 of notional, in the "long risk" sign convention. It computes the sample covariance matrix of the instruments and their covariance with the book, converts the first to a correlation matrix, and, unless you supply a penalty, calls `eta_for_condition` to find the smallest ridge penalty that caps the condition number of that correlation matrix at 50. It then solves for the hedge with the penalty scaled by each instrument's own variance, so units drop out, and returns the weights, the residual variance, the condition number before and after, and the penalty. `hedge_qp` solves the same objective with per-instrument bounds by L-BFGS-B, starting from zero and rescaling the objective so the optimizer sees numbers near one. `futures_contracts` and `etf_shares` are the separate unit-conversion step: contracts are $N = H \cdot \text{DV01}_{\text{target}}/(\text{DV01}_{\text{CTD}}/\text{CF})$, and shares are weight times notional over price.

The bench builds CDX, a Treasury future, HYG, an equity put, and a JNK that is HYG plus almost no noise, all from the same rate and spread factors, plus a B-rated book with 30 bp a day of idiosyncratic risk. It fits on 2,000 days and tests on 500. The raw condition number is about 9 million; a penalty of 0.06 brings it to exactly 50. Out of sample, the ridge hedge leaves 36% of the unhedged variance, within 1.5% of the OLS hedge, and its weights differ by 0.04 between the two halves of the training sample where the OLS weights differ by 12. A one-proxy case lands at 0.40 against the naive 0.80, and the futures sizing reproduces Table 8.2: 232 and 169 contracts.

Use it when the menu has overlapping instruments. It minimizes total hedged variance, so it will also hedge away a spread view you meant to keep (§8.2); the objective has to be chosen first. The covariances are plain sample covariances, so synchronizing closes, or Dimson-summing them as §8.6 describes, is the caller's job. The edge case that bites is the sign. The weights are notional to short, so a negative weight is a long position. The put's bounds of (-0.5, 0.0) permit buying puts and forbid selling them. Write them the other way round and nothing complains: the optimizer pins the put at zero and shifts the work onto the other instruments.

*The full listing is [Listing 8.6 in Appendix F](#code-8-6).*

Wen's Tuesday morning in Twelve Residuals (§8.8) was this block done by hand, and Kaz's month-end slide was the question it ends on. The last block does both. It removes the common factor from a panel of scaled residuals and puts the remainder back into returns. Then it asks the question the whole chapter has been building toward: does any signal predict what is left?

`strip_common_factor(eps_scaled, n_pc=1)` takes a (T, N) panel of DTS-scaled residuals, subtracts each bond's time average, and takes the singular value decomposition. The squared singular values, as shares of their total, say how much of the panel's variance each component carries, and the function returns them. It subtracts the rank-`n_pc` reconstruction built from the leading components and returns the cleaned panel. `ido_ledger(ido, signal, min_names=10)` loops over the rows, keeps the bonds with both a residual and a signal, skips any row with fewer than `min_names` of them, and records the Spearman rank correlation as that row's IC. It returns the pooled standard deviation of every residual in the panel, the mean IC, its t-statistic (mean times root n over the sample standard deviation), and the number of periods. It pairs row t of the signal with row t of the residual, so the caller must have shifted the signal to be known beforehand.

The bench simulates 60 months of 200 bonds: a common factor with 2% volatility, loaded at 0.5 to 1.5 on every bond, plus 3% idiosyncratic noise. The first principal component carries 31% of the variance before stripping and 4% after. The cleaned panel is multiplied by each bond's DTS, drawn between 0.05 and 0.40, to return to returns, and a signal is planted that contains 0.15 standard deviations of the residual plus unit noise. The ledger finds a mean IC of 0.137 with a t of 14. That is what a planted edge looks like with 200 names a month and no specification search; Chapter 7's warning applies to anything found on real data. The closing lines print 18/18 and assert.

Run it after the factor regressions. Do not give `strip_common_factor` a panel with gaps: the decomposition raises on NaN, though the ledger tolerates them. The edge case that bites is that the component is estimated on the whole sample. The factor and its loadings use months after t to clean month t, so a backtest built from this function has looked ahead. The same step removes each bond's average residual, so a bond that is persistently rich or cheap loses that persistent part. A live ledger should re-estimate on an expanding window through t minus 1.

*The full listing is [Listing 8.7 in Appendix F](#code-8-7).*

> **Ways This Blows Up.** The simulation is kinder than the market in three ways. Its rate–spread correlation is constant, so the trailing-window problem of §8.7 never appears; rerun section 2 with $\rho$ switching sign halfway through and watch the regression $H$ average two regimes into a hedge ratio that fits neither. Its smoothing weights are the same for every bond, while real weights differ by price source and liquidity bucket. And its instruments have no roll dates, so the jumps in real CDX and futures series never reach the covariance matrix. Each is an exercise below.

## 8.10 Desk Debrief

Theo's sticky note now had a question on the front, a number under it, and two replays on the back. The table below is the rest of the chapter folded to the same size: where each idea is derived, where it was first pictured, where somebody had to use it under pressure, and where the code lives.

| Concept | Equation | Intuition (box) | Judgment (scene) | Code |
| :--- | :--- | :--- | :--- | :--- |
| Return decomposition | $R^{\text{xs}} \approx s\,\Delta t - \text{DTS}\cdot\Delta s/s$ (§8.1) | A curve, its tangent, and the bend (§8.1) | Cold open: the EXPLAIN button and the four cents | [Listing 8.2](#code-8-2) |
| Empirical duration | $H = 1 + s\,\rho\,\sigma_s/\sigma_y$ (§8.2) | What a regression slope is (§8.2) | The Year a PDF Said Zero (§8.7) | [Listing 8.3](#code-8-3) |
| Recovery route | $H^{\text{rec}} = c/(c + \lambda R)$ (§8.3) | The memoryless clock (§8.3) | Alltel's four hedge ratios (§8.3); the SVB holdco coda (§8.7) | — |
| DTS beta | $\beta_i = \text{DTS}_i/\text{DTS}_M$ (§8.4) | Spreads move in percent (§8.4) | The pod's risk x-ray and PB-03 (§8.4) | [Listing 8.5](#code-8-5) |
| Stale-mark betas | $\hat\beta_{\text{D}} = \sum_k \hat b_k$ (§8.5) | News in three envelopes (§8.5) | Kaz and Ines on the equity lag (§8.5) | [Listing 8.4](#code-8-4) |
| Hedge matrix | $h_\eta = (\Sigma_{HH} + \eta\,\mathrm{diag}\,\Sigma_{HH})^{-1}\Sigma_{Hp}$ (§8.6) | Two hedges that are almost the same hedge (§8.6) | The four windows; Theo's hedge, four ways (§8.6) | [Listing 8.6](#code-8-6) |
| Two-instrument hedge | Futures at $H = 1$; CDX at $\text{DTS}_i/\text{DTS}_{\text{CDX}}$ (§8.8) | (none) | The Hedge That Hedged Both Ways (§8.7); Ines on the mandate (§8.8) | Spec field `OBJECTIVE` (§8.10) |
| IDO and the ledger | $\text{IDO}_{i,t} = \text{DTS}_{i,t-1}\,\tilde\epsilon^{\perp}_{i,t}$; $t = \overline{\text{IC}}\sqrt{T}/\mathrm{sd}(\text{IC}_t)$ (§8.8) | The common whisper (§8.8) | Twelve Residuals; the month-end meeting (§8.8) | [Listing 8.7](#code-8-7) |

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

- **"Why Treasuries Are 'Risky' Again"** (*Odd Lots*, with Carolin Pflueger of the University of Chicago, October 5, 2026). Bonds "more stock-like" and the Fed's credibility as what makes them "bond-like" again: the stock–bond correlation sign decides whether the Treasury-futures leg of the hedge matrix hedges or doubles the loss (§8.2, §8.6). https://omny.fm/shows/odd-lots/why-treasuries-became-risky-again
- **"What We Learned About Treasuries on the Night of April 8"** (*Odd Lots*, with Ira Jersey of Bloomberg Intelligence, April 28, 2025). Who sold, and why the safe-haven hedge failed in an acute way after "Liberation Day": the live case for Case Study C (§8.7). https://omny.fm/shows/odd-lots/what-we-learned-about-treasuries-on-the-night-of-april-8
- **"How The Crisis Nearly Blew Up One Of The World's Safest Trades"** (*Odd Lots*, with Josh Younger of JPMorgan, March 26, 2020). The Treasury cash-futures arbitrage failing in March 2020: the rates-side twin of the credit-ETF dislocation, and the basis risk of the futures leg (§8.6, §8.7). https://omny.fm/shows/odd-lots/how-the-crisis-nearly-blew-up-one-of-the-world-s-s
- **"Goldman Tells Credit Investors to Buy Cheap Hedges"** (*The Credit Edge*, with Lotfi Karoui of Goldman Sachs, February 13, 2025). A dated sell-side statement that hedge cost was "the lowest it's been in probably a very long time": the price side of the CDX and equity-put legs (§8.6). https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/goldman-tells-credit-investors-to-buy-cheap-hedges
- **"What the Actual ETF Is Going on Right Now"** (*Trillions*, March 19, 2020). Live commentary on ETFs in the 2020 crash, days after the LQD discount: the audio companion for the HYG/JNK leg (§8.6, §8.7). https://omny.fm/shows/trillions/what-the-actual-etf-is-going-on-right-now
- **"Why the True Price of a Bond Can Still Be Hard To Know"** (*Odd Lots*, with Maciej Kowara and Eric Jacobson of Morningstar, on their report "Bond Pricing: Agreeing To Disagree," April 5, 2021). Evaluated prices differ by firm on illiquid bonds: the stale-price mechanism behind non-synchronous betas (§8.5). https://omny.fm/shows/odd-lots/why-the-true-price-of-a-bond-can-still-be-hard-to
- **"Boaz Weinstein"** (*Money Stuff: The Podcast*, with Matt Levine and Katie Greifeld, March 19, 2026). Private-credit NAVs, BDC discounts and "volatility laundering": the smoothing problem of §8.5 in a live market. https://omny.fm/shows/money-stuff-the-podcast/boaz-weinstein
- **"Ralph Smith - Scientific Investing in Fixed Income (S5E7)"** (*Flirting with Models*, with Ralph Smith of BlueCove, July 11, 2022). Breadth and liquidity differ between credit and rates, and the assumption about a bond's availability materially moves a backtest: the practitioner's version of asking whether the price behind a backtest or a hedge ratio was one you could trade (§8.5, §8.6). https://www.flirtingwithmodels.com/episodes/kAEkSoYuRwd
- **"How to Succeed at Multi-Strategy Hedge Funds"** (*Odd Lots*, with Giuseppe Paleologo, May 20, 2024). How a platform watches its PMs: market- and factor-neutral books and the factor model as a daily x-ray, the practice behind the pod seat in §8.4 (paraphrased in the text; the transcript is machine-made). https://omny.fm/shows/odd-lots/how-to-succeed-at-multi-strategy-hedge-funds
- **"How the Hottest Hedge Funds on Wall Street Really Manage Risk"** (*Odd Lots*, with Rich Falk-Wallace, July 25, 2024). Leverage applied to the residual rather than the beta: why a pod's hidden spread beta is the platform's problem (§8.4, §8.8). https://omny.fm/shows/odd-lots/how-the-hottest-hedge-funds-on-wall-street-really
- **"The Math That Explains How Multi-Strategy Hedge Funds Make Money"** (*Odd Lots*, with Dan Morillo, October 7, 2024). The correlation cap on a platform's Sharpe ratio, the arithmetic Marcus walks Dov through in the Twelve Residuals scene (§8.8). https://omny.fm/shows/odd-lots/100724-odd-lots-dan-morillo-master
- Show and topic only, no episode verified: *ReSolve Riffs* on stock–bond correlation regimes; *Odd Lots* on the 2022 bond sell-off.

**Practitioner Writing**

- **"Duration Times Spread: measuring credit risk"** (Erik van Leeuwen, Olaf Penninga and Patrick Houweling, Robeco, September 2, 2024). The originators' own account: developed in 2003 and now the industry standard for credit volatility; read it before the DTS derivation in §8.4. https://www.robeco.com/en-uk/insights/2024/09/duration-times-spread-measuring-credit-risk
- **"Debunking the high credit beta myth"** (Christoph Schon, SimCorp, 2024; page undated, year from the URL). Argues that high spread is high volatility but not necessarily high beta to the index, since low-rated names often show weak correlation with the market: the practical warning behind §8.3 and the hedge-ratio regressions in §8.8. https://www.simcorp.com/resources/insights/industry-articles/2024/Debunking-the-high-credit-beta-myth
- **"AQR Quant Sketches a Factor-Investing Future for Corporate Bonds"** (Yakob Peterseil, Bloomberg via WealthManagement.com, May 15, 2019). Reports AQR's Roni Israelov sketching a top-down way to replicate corporate-credit exposure with derivatives on government bonds and stocks: the return-decomposition idea behind beta-stripping, and a check on how much credit beta the Treasury and equity legs can carry (§8.1, §8.6). https://www.wealthmanagement.com/fixed-income/aqr-quant-sketches-a-factor-investing-future-for-corporate-bonds
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
