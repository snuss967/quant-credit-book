# Chapter 23: Cross-Asset Convexity & the Volatility Surface

*A replay, and Ines's ritual: on Friday afternoons she takes a real episode, cuts the tape at a stated minute, and has the cast trade it blind, with what actually happened held face down until she turns it over. Today's tape stops at 6:40 a.m. on Thursday, March 9, 2023, and Ines plays the rest of the market from her own screen; whatever the desk shows, she decides whether to lift it. SVB Financial Group's filings, the Federal Reserve's post-mortem and the market marks are real and cited. The desk's quotes, Ines's bids, ROBO's column, every number marked (illustrative) and all dialogue are invented.*

6:40 a.m., Thursday, March 9, 2023. Theo Marsh, in his third week of replays, still reads bank filings for fun, which is how he knows things nobody has asked him yet. Last night SVB Financial Group announced that it had sold \$21 billion of available-for-sale securities, was booking a \$1.8 billion after-tax loss, and wanted to raise \$2.25 billion of capital (Federal Reserve, *Review of the Federal Reserve's Supervision and Regulation of Silicon Valley Bank*, April 28, 2023). The stock is indicated sharply lower.

The replay corner is the part of the floor with the good whiteboard and the bad chairs. Kaz has the SIVB listed put surface on the big screen, frozen at Wednesday's close, the last prices anyone paid before the announcement. It is a portrait of a dull bank. The stock closed at \$267.83, and its 30-day implied volatility has spent the past year near the bottom of its range; a vendor's pre-market report would later put the floor of that 52-week range at 39 (Market Rebellion, pre-market IV report, March 10, 2023). Kaz shows a ladder of one-month puts priced around that level, with an ordinary skew, and Ines starts lifting the low strikes one after another without haggling. Kaz moves the offers up. She lifts those too. Kaz backs the volatility out of the last fill, something north of 150 *(illustrative)*, and frowns at it.

"The one-month low-strike puts are bid at an implied vol that makes no sense," they say, "unless the stock is going to zero."

"It can go to zero by lunch," Theo says. "At year-end about 94 percent of the deposits were uninsured, and the held-to-maturity book had a weighted-average duration of 6.2 years. The equity is a call option on whether the depositors read the same footnote I did."

He has the 10-K open at the fair-value tables, and he reads it the way he used to read a borrower's liquidity schedule at two in the morning, hunting for the line the company hopes you will skip. "Unrealized losses on the securities, both books, about seventeen point seven billion. Common equity, twelve point four. Mark the bonds and the common is gone one and a half times over." The ratio is 143 percent, computed from the FY2022 10-K. Chapter 6 tells the same balance sheet with the held-to-maturity hole alone, \$15.2 billion, set against total equity including the preferred, \$16.0 billion. Both are right: one asks whether the common survives a mark, the other whether the whole equity layer does.

Ines does not look up from her markouts. "So what's the pot, what are the odds, and who at this table knows more than you? Somebody is lifting every put we show, and it isn't a pension fund rebalancing."

Nobody points out that the somebody is Ines. That is the ritual working: she lifts what the informed side of the 2023 tape lifted, and the desk has to read from the hand history who it is playing against.

"Merton says the distance to default is fine," Kaz offers. "Bank asset volatility is tiny."

"Bank asset volatility is tiny right up until the assets are on the other side of the street," says Mags, from the distressed corner, where the screens are older and the opinions are firmer. "Press reports had the holdco notes near ninety earlier this week. Price is what you pay. Recovery is what you get, eventually, after the FDIC."

ROBO's overnight batch, asked to "compute the equity-implied CDS spread for every bank in the book," has helpfully populated a column. SVB Financial Group: 12bp. Nobody has the heart to tell it.

Kaz, who does have the heart, opens the inputs, expecting a bug, and finds none in the arithmetic. The stock is Wednesday's close. The debt per share counts the holding company's own notes, about \$3.3 billion over 59 million shares, call it \$56 a share against a \$268 stock; the \$173 billion of deposits at the bank are not in the column at all (computed from the 10-K; the run is illustrative). Feed choices like those to the model Section 23.2 builds and 12bp is what comes out. ROBO did exactly what it was asked, about exactly the entity it was given. Kaz writes *which F?* on a sticky note and presses it onto the monitor bezel, where it will stay until Section 23.8.

Mags watches the fills stack up on the board and says what she thinks the trouble is, which is not a model. "When it's assets wobbling, the stock and the bonds are arguing about the same thing, and one of them is just slow. When it's a run, or a contract, or a regulator with a pen, they aren't arguing about the same thing at all. Then your arbitrage is a bet on who wrote the document."

Ines deals a blank index card to each of them, and one to the reader. The cards are the only fixed rule of the ritual. *Write three things: which instrument is lying, what you would trade against it in what size, and what would have to be true for you to be wrong.* Theo writes for a long time. Kaz writes a number, crosses it out, and writes a smaller one. Mags writes a single word, folds the card, and parks it under her coffee. The cards go face down in the middle of the desk. The tape runs forward in Section 23.8, and the cards are graded there against what happened on Thursday, on Friday, and in the week after.

The question this chapter answers is the one Ines is really asking: *when the equity-volatility surface and the credit curve disagree, which one is lying, and how do you size the bet that it's the other one?*

The answer comes in three movements. Sections 23.1 to 23.5 build the translation layer between the two markets (Merton, CreditGrades, the Carr–Wu put spread, the jump floor in the skew, and Greeks in spread units) and let you believe in it, because most days it deserves belief. Section 23.6 breaks it on General Motors in May 2005, when two shocks on consecutive days hit two different claims and a hedged pair lost on both legs. Section 23.8 breaks it three more ways, with Mags's distinction doing the work: a run is not a diffusion, a trigger can reorder a waterfall, and the right tail can belong to the creditors.

## 23.1 One Distribution, Many Strikes: The Capital Structure as a Vol Surface

In RSSG, Theo built waterfalls. A waterfall takes an enterprise value and hands it out by priority: the first-lien gets paid until it is whole, then the second-lien, then the unsecureds, then whatever is left falls to equity. He thought of it as a legal object. It is also a payoff diagram. If tranche $k$ attaches at claim level $a_k$ and detaches at $b_k$ (cumulative claims senior to it, and senior plus itself), then at resolution it receives

$$
\text{Payoff}_k(V_T) = (V_T - a_k)^+ - (V_T - b_k)^+ ,
$$

a call spread on firm value $V_T$ struck at its attachment and detachment points. Equity is the call struck at total debt $F$. The fulcrum security is the tranche whose strike interval contains the value: the at-the-money strike. When Kaz first heard the term they asked whether "the fulcrum" was the security with the most leverage, which is exactly right and is the annoying thing about Kaz. Figure 23.1 draws the stack.

![Figure 23.1: Each debt claim pays a call spread on firm value and equity pays the call struck at total debt (left), and the same strikes cut the risk-neutral distribution of firm value into the intervals that decide which claim is the fulcrum, here the unsecured notes because assets stand at 62 (right). Illustrative: lognormal firm value, asset volatility 25%, r = 3%, one year, strikes at 40, 55 and 70.](assets/figures/ch23_waterfall_call_spreads.png)

What RSSG never priced is the *distribution* of $V_T$. Theo ran three EV cases, called them low, mid, and high, and wrote a recovery under each. The systematic desk prices the whole distribution, and the market reveals that distribution one strike at a time: the stock is the high strike, the bonds are the middle strikes, CDS is the middle strike stripped of rates, and a deep out-of-the-money equity put is a bet on the low tail that happens to trade on an exchange. A CCC bond is an equity option that wears a tie to work; a 20-delta put is a CDS that forgot to wear one. Every slice is priced off the same risk-neutral law of $V_T$, so the volatility surface of one slice is a forecast of the spread of another. This chapter builds that translation layer.

> **Math, Gently.** *The bookmaker's odds, and why firm value is lognormal.* Picture a bookmaker who must quote odds on every horse in a race and cannot afford to be picked off. He does not need to know which horse will win. He needs odds at which no combination of bets lets a customer make money for certain, once the house has been paid the interest it could have earned sitting in cash. Those are *risk-neutral* odds, and they are a pricing device rather than a forecast: the odds on a long shot carry whatever extra people pay to be insured against it, which is why a market's $\mathbb{Q}$ default probabilities sit above the physical frequencies of Chapter 6. A tiny number: a claim pays 100 if the firm's assets end the year above 70 and nothing otherwise, the pricing odds put that outcome at 0.6, and the risk-free rate is 3%. The price is $0.6 \times 100 / 1.03 = 58.25$. Every price in this chapter has that shape, $P_0 = e^{-rT}\,\mathbb{E}^{\mathbb{Q}}[\text{payoff}]$: average the payoff under the pricing odds, then discount. The second fact is the shape of the odds. Firm value cannot go below zero, and percentage moves compound rather than add: a year at −30% followed by a year at +30% leaves you at $0.7 \times 1.3 = 0.91$, down 9%, not flat. So the model makes the *logarithm* of assets bell-shaped, which makes the assets themselves lognormal: floored at zero, with a long right tail and a median below the mean. Chapter 5 owns the distributions and Chapter 6 the two measures; here you need only these two facts.

### The Merton identity: equity vol is leveraged asset vol

Recall the setup from Chapter 6. Under $\mathbb{P}$ firm assets follow $dV_t = \mu V_t\,dt + \sigma_V V_t\,dW_t$; under $\mathbb{Q}$ the drift is $r$. Debt is a single zero-coupon claim of face $F$ due at $T$, so $E_T = (V_T - F)^+$ and

$$
E_0 = V_0 N(d_1) - F e^{-rT} N(d_2), \qquad d_{1,2} = \frac{\ln(V_0/F) + (r \pm \tfrac12\sigma_V^2)T}{\sigma_V\sqrt{T}} .
$$

Here $N(\cdot)$ is the standard normal CDF. The desk's question is narrower than the formula: when the assets shake by a given amount, how much does the stock shake? Answering it takes the one piece of stochastic calculus this chapter cannot do without.

> **Math, Gently.** *Why a wobble pays a curved claim: Itô's ½σ².* Equity is a curved function of assets, flat when the firm is deep under water (the call is worthless and stays worthless for small moves) and steep when it is comfortably solvent. Whenever a payoff curves upward, wobbling the input raises the average output, because the gain on the up-wobble beats the loss on the down-wobble. A tiny number: let $f(V) = V^2$, and let $V$, now 100, move to 90 or 110 with equal odds. The average of $f$ is $(8{,}100 + 12{,}100)/2 = 10{,}100$, not $f(100) = 10{,}000$. The extra 100 is one half times the squared wobble ($10^2 = 100$) times the curvature ($f'' = 2$): $\tfrac12 \times 100 \times 2 = 100$. Ordinary calculus throws that term away because, for a smooth path, a squared step is negligible next to the step. A random path's squared step is not negligible: over a short interval $dt$ it averages $\sigma_V^2 V^2\,dt$, so the bonus becomes $\tfrac12\sigma_V^2V^2\,\partial^2E/\partial V^2\,dt$ and lands in the drift of equity. For the identity below the bonus is a side character. It lives in the $dt$ term, while the identity lives in the shaking term, where only the slope $\partial E/\partial V$ appears. Kaz's version: curvature changes what you earn on average, slope changes how much you shake. The step-by-step derivation comes next.

Matching how much equity shakes to how much the assets shake gives the identity every cross-asset screen rests on:

$$
\sigma_E E = \sigma_V V N(d_1) \quad\Longleftrightarrow\quad \sigma_E = \sigma_V \cdot \underbrace{\frac{V\,N(d_1)}{E}}_{\Omega\ \ge\ 1} . \tag{23.1}
$$

The identity holds under either measure, because Girsanov changes drifts and leaves volatilities alone. The factor $\Omega$ is the elasticity of a call with respect to its underlying, which is at least 1, so equity vol is asset vol times a leverage multiplier. Bohn and Stein write the same identity as $\sigma_E E = \sigma_A A\,\partial E/\partial A$ and build the KMV-style iteration on it (Bohn_Stein_Active_Credit_Portfolio_Management p.169).

The model debt is $B_0 = V_0 - E_0 = F e^{-rT}N(d_2) + V_0 N(-d_1)$, so the model credit spread, continuously compounded, is

$$
s^{\text{M}}(T) = -\frac{1}{T}\ln\!\Big[N(d_2) + \frac{V_0}{F e^{-rT}}N(-d_1)\Big]. \tag{23.2}
$$

#### The Full Derivation of (23.1)

Equity is a smooth function $E(V,t)$, so Itô's lemma gives

$$
dE_t = \frac{\partial E}{\partial V}\,dV_t + \Big(\frac{\partial E}{\partial t} + \tfrac12 \sigma_V^2 V_t^2 \frac{\partial^2 E}{\partial V^2}\Big)dt .
$$

Only the first term carries a $dW_t$, and its coefficient is $\frac{\partial E}{\partial V}\sigma_V V_t$. Writing the equity dynamics as $dE_t = (\cdot)\,dt + \sigma_E E_t\,dW_t$ and matching diffusion coefficients, with the call delta $\partial E/\partial V = N(d_1)$, gives $\sigma_E E_t = \sigma_V V_t N(d_1)$, which is (23.1). The convexity bonus from the box, $\tfrac12 \sigma_V^2 V_t^2\,\partial^2 E/\partial V^2$, sits wholly inside the $dt$ coefficient and never enters the match.

#### Sliding the assets down the table

With the replay cards face down, Kaz takes the marker. "Forget banks for a minute. A boring firm. Asset vol twenty-five percent, and it stays twenty-five percent, I promise. Debt face seventy, one year, rates at three." They write three rows and fill them in out loud, the way a croupier calls the numbers *(illustrative)*:

| Assets $V$ | Equity $E$ | $N(d_1)$ | Equity vol $\sigma_E$ |
| :-- | :-- | :-- | :-- |
| 150 | 82.1 | 0.999 | 46% |
| 100 | 32.6 | 0.953 | 73% |
| 75 | 11.2 | 0.699 | 117% |

"Assets at 150. Equity is worth 82, the call is nearly all delta, so the stock is the assets with a lever of about 1.8 on it. Equity vol 46." The marker drops a row. "Assets at 100. Equity 32.6. Same business, same twenty-five percent, but the cushion is a third of the firm now. Equity vol 73." Another row. "Assets at 75, five above the debt. Equity 11.2, delta 0.7. Equity vol 117."

"What changed about the business?" Ines asks.

"Nothing. Asset vol never moved. Equity vol went from 46% to 117% because the equity cushion got thinner. Cheap stocks are mechanically high-vol stocks."

"Then walk a vol-targeting overlay down your rows." Ines does not wait for the answer; she has sat across from that overlay. At 150 it holds a full position, because 46 looks like an ordinary stock. At 100 it trims, because 73 looks like a risky one. At 75 it is selling hard into a stock whose only news is arithmetic, at the moment the stock is starting to behave like the credit. "It reads leverage as risk appetite," she says. How much it sells on the way down is Exercise 1's problem, and the risk committee will want the answer in one sentence.

Theo has been sketching the rows as a curve. "So if I plot equity vol against the stock price, it slopes down. The skew is in there already." Kaz nods: the elasticity of a call falls as the call moves into the money, so $\partial \sigma_E/\partial E < 0$ with $\sigma_V$ constant, and equity vol rises as the stock falls. That is a negative skew in the option surface before anyone has said "crash risk" or "jumps." Section 23.4 adds a jump to default, which steepens the low-strike wing far beyond what leverage alone produces. Figure 23.2 plots both effects.

![Figure 23.2: With asset volatility pinned at 25%, equity volatility climbs from 46% to 117% and the model one-year spread from under 1bp to 626bp as assets fall from 150 toward the debt face of 70, so the skew and the spread are both built into leverage alone. Illustrative: Merton model (23.1) and (23.2), debt face 70, r = 3%, one year.](assets/figures/ch23_leverage_skew.png)

"And backwards?" Theo asks. "The market hands me the stock and its vol, not the assets." That is the inverse problem, and it is the version the desk actually runs: observe $(E_0, \sigma_E)$, solve (23.1) and the call-price equation jointly for $(V_0, \sigma_V)$, and read the equity-implied spread off (23.2). Kaz lists the two classic ways to get it wrong and owns the first. Skip the inversion and plug $\sigma_E$ in as $\sigma_V$, and you overstate default probability by roughly a factor of leverage; Kaz did that once in graduate school, in a paper nobody read. The second classic error is ROBO's from the cold open, and the marker taps the sticky note that says *which F?* The spec in Section 23.2 holds the autopsy.

> **[SOURCE EXTRACTION]** *Dynkin_Systematic_Investing_in_Credit p.93:* "In the Merton model (1974), a corporate bond is a short put on the underlying asset plus a risk‐free asset, while the company's stock is a call option on the underlying asset. The short put on the underlying asset also can be decomposed into a stock (call) plus a short straddle (a call and put at‐the‐money (ATM)) position on the underlying asset."
>
> **Annotation.** This is the sentence to tape above the cross-asset screen. If a bond is a Treasury plus some stock plus a short straddle on firm assets, then a long-credit book is short volatility, and it should earn the variance risk premium that option sellers earn; Dynkin's team tests exactly that and finds the bond-over-equity-replication return loads on the equity VRP. Two desk consequences follow. First, "bonds beat risk-matched equity" is partly a short-vol carry, so it will lose in vol spikes, which is when your equity hedge also misbehaves. Second, a capital-structure trade that is long the bond and short the stock is *not* flat vol: you have hedged the delta and kept the short straddle. Where the 2026 desk departs from the 1974 picture is that we no longer pretend the straddle is on a single lognormal asset; we read it off the listed surface strike by strike.

> **Desk Myth vs. Desk Reality.** *Myth:* Equity and credit are different markets with different investors, so their prices can disagree indefinitely and that is nobody's problem. *Reality:* They are different strikes on the same distribution, so a disagreement is a trade. The catch, which we will spend Section 23.6 on, is that at daily and weekly horizons the two markets are only weakly integrated (Kapadia and Pu, 2012), so the trade converges on the portfolio's schedule, not yours.

## 23.2 From Equity Vol to a Spread: CreditGrades in Production

Merton is the right picture and the wrong production model. It needs a single debt maturity, it puts default only at $T$, and short-dated spreads in it go to zero for any firm not already insolvent, which is not what the CDS market says. In May 2002 RiskMetrics Group, working with Goldman Sachs, JPMorgan, and Deutsche Bank, published the *CreditGrades Technical Document* (Finger, Finkelstein, Lardy, Pan, Ta and Tierney, 2002): a first-passage barrier model whose inputs are the stock price, an equity volatility, debt per share, and three constants. You can calibrate it before the coffee is ready, and two decades later it is still the default equity-to-credit bridge on many desks.

The coffee line matters more than it sounds. The desk runs an equity-implied spread on about 900 names every night *(illustrative)*, and nobody reads 900 rows. People read the dozen rows that moved, and the morning question is never whether the model is elegant. It is whether the column is wrong in a way somebody can see before they trade on it: a stock that split and kept its old strikes, a debt-per-share figure that still counts a bond redeemed last month, a bank that slipped into a list built for industrials. A model with four auditable inputs and three published constants fails loudly when an input is wrong, and loud failures are the kind a data team catches. ROBO's 12bp for SVB Financial Group was a failure of the quiet kind. The spec at the end of this section takes it apart, and Section 23.4 spends a week with a data team catching the loud kind.

**Notation, renamed.** CreditGrades writes $S$ for the stock (we use $S_t$, as in the market-making chapters), $D$ for debt per share (we use $F^{\text{ps}}$, since $D$ is duration in this book), $\bar L$ for the mean global recovery (we use $\bar\ell$, since $L = 1-R$ is loss given default), and $\lambda$ for the dispersion of the barrier (we use $\nu$, since $\lambda$ is reserved for the hazard rate). Survival is written $\mathcal{S}(t) = \mathbb{Q}(\tau > t)$ in calligraphic type in this chapter, because the stock price $S_t$ is on every line.

### The model

Assets per share follow a driftless lognormal, $V_t = V_0 e^{\sigma_V W_t - \sigma_V^2 t/2}$ (the document argues on p.11 that zero drift relative to the barrier is the right compromise). Default is the first time assets touch the barrier $\ell F^{\text{ps}}$, where the global recovery fraction $\ell$ is itself uncertain:

$$
\ell = \bar\ell\, e^{\nu Z - \nu^2/2}, \qquad Z \sim N(0,1) \text{ independent of } W .
$$

The barrier uncertainty is the whole trick. A known barrier with continuous asset paths gives zero short-dated spreads; an uncertain barrier means you might already be closer to it than you think.

> **Math, Gently.** *The drunk, the lamppost and the gutter: first passage and the reflection principle.* A drunk leaves a lamppost at ten o'clock with no plan; every step is a coin flip, left or right. How likely is he to touch the gutter, a fixed distance to his left, before midnight? Counting where he ends up is not enough, because a man who touched the gutter at eleven may be back on the pavement by twelve. The trick is a mirror. Take any path that touched the gutter and reflect every step after the first touch, so that left becomes right. The mirrored path is just as likely, and it ends on the far side of the gutter. So every touched path that ends on the pavement has an equally likely twin that ends in the gutter, and every path that ends in the gutter must have touched it, which makes $\mathbb{P}(\text{touched by midnight}) = 2 \times \mathbb{P}(\text{ends in the gutter})$. A tiny number: a standard Brownian motion over one year with a floor at −1. The chance of *ending* below −1 is $N(-1) = 0.159$, so the chance of touching the floor at some point in the year is $2 \times 0.159 = 0.318$, twice the answer you get by looking only at the end. That doubling is why barrier models default so much more often than terminal-value models with the same inputs; a drift, such as the $-\tfrac12\sigma^2$ that rode along in Section 23.1, tilts the mirror, and the tilt is the factor $d$ in the second term of (23.3). The second part of the trick is CreditGrades's own. Nobody knows exactly where the gutter is, because the recovery that sets the barrier is uncertain. Not knowing where the gutter is turns out to be, to a very good approximation, the same as not knowing exactly where the drunk started, and that is the same as having started the clock earlier. So the model starts the walk before time zero. A few of those early walks have already reached the gutter by ten o'clock, which is why survival at time zero comes out below one. The three equations it produces come next, and the algebra after them.

Fold the floor's uncertainty into the starting point, apply the mirror, and survival to $t$ is the document's equation (2.11) in our notation, with $d = V_0 e^{\nu^2}/(\bar\ell F^{\text{ps}})$ measuring how far the assets sit above the expected barrier:

$$
\mathcal{S}(t) = N\!\Big(-\frac{\Sigma_t}{2} + \frac{\ln d}{\Sigma_t}\Big) - d\, N\!\Big(-\frac{\Sigma_t}{2} - \frac{\ln d}{\Sigma_t}\Big), \qquad \Sigma_t^2 = \sigma_V^2 t + \nu^2 . \tag{23.3}
$$

Boundary check: as $\nu \to 0$ it collapses to the standard first-passage survival of a driftless lognormal against a known barrier; as $t \to \infty$ it goes to zero; and at $t = 0$, $\Sigma_0 = \nu > 0$ and $\mathcal{S}(0) < 1$. That last fact is not a typo. The time shift puts probability mass on "already defaulted at inception," and the document itself flags the "counterintuitive result that there is a non-zero probability of default at t = 0."

Calibration ties the unobservable asset state to the two things a screen does show, the stock and its volatility:

$$
V_0 = S_0 + \bar\ell F^{\text{ps}}, \qquad \sigma_V = \sigma_E\,\frac{S_0}{S_0 + \bar\ell F^{\text{ps}}} \tag{23.4}
$$

Read (23.4) backwards and you have Section 23.1's leverage skew in one line: for fixed $\sigma_V$, $\sigma_E = \sigma_V (S_0 + \bar\ell F^{\text{ps}})/S_0$ rises as $S_0$ falls. The document says it plainly: "This dependence of equity volatility on the stock price is evident in a pronounced volatility skew in equity option markets, especially for high yield names" (Finger et al., 2002, p.11).

The par CDS spread then sets the premium leg, an annuity paid while the name is alive, equal to the protection leg, which pays the time-zero mass on day one and the rest as defaults arrive. With constant $r$ and instrument recovery $R$:

$$
s^{\text{CG}}(T) = \frac{(1-R)\Big[1 - \mathcal{S}(0) + \int_0^T e^{-ru}\,\big(-d\mathcal{S}(u)\big)\Big]}{\int_0^T e^{-ru}\,\mathcal{S}(u)\,du} . \tag{23.5}
$$

The document gives a closed form for (23.5) built on Rubinstein and Reiner's barrier integrals. We integrate (23.5) numerically on a monthly grid instead, for a reason the Ways This Blows Up box below gives. Figure 23.3 shows the survival curve and the spread curves it produces.

![Figure 23.3: CreditGrades books a 25% default probability for a \$5 stock at time zero, before any time has passed (left), and turns the upward-sloping spread curve of a \$30 stock into an inverted one for a \$5 stock (right). Illustrative: (23.3) and (23.5) at equity volatility 40%, debt per share \$30, mean barrier 0.5, barrier dispersion 0.3, recovery 40%, r = 3%.](assets/figures/ch23_creditgrades_ghost.png)

#### The Full Derivation of (23.3)–(23.5)

**Step 1 (rewrite the default event).** Default by $t$ means $V_0 e^{\sigma_V W_s - \sigma_V^2 s/2} \le \bar\ell F^{\text{ps}} e^{\nu Z - \nu^2/2}$ for some $s \le t$. Take logs and move everything random to the left:

$$
X_s := \sigma_V W_s - \nu Z - \tfrac12\sigma_V^2 s - \tfrac12 \nu^2 \;\le\; \ln\frac{\bar\ell F^{\text{ps}}}{V_0} - \nu^2 =: y .
$$

**Step 2 (the approximation).** $X_s$ is Gaussian with mean $-\tfrac12\sigma_V^2(s + \xi)$ and variance $\sigma_V^2(s + \xi)$, where $\xi = \nu^2/\sigma_V^2$. Those are exactly the moments of a Brownian motion with drift $a = -\tfrac12\sigma_V^2$ and volatility $b = \sigma_V$ that *started at time $-\xi$*. CreditGrades replaces $X$ by that process. In the document's words, the approximation "replaces the uncertainty in the default barrier with an uncertainty in the level of the asset value at time 0."

**Step 3 (reflection principle).** For $Y_u = a u + b W_u$ started at zero and a barrier $y < 0$,

$$
\mathbb{Q}\Big\{\min_{v \le u} Y_v > y\Big\} = N\!\Big(\frac{a u - y}{b\sqrt{u}}\Big) - e^{2 a y / b^2}\, N\!\Big(\frac{a u + y}{b\sqrt{u}}\Big).
$$

**Step 4 (substitute).** Set $u = t + \xi$, so $b\sqrt{u} = \sqrt{\sigma_V^2 t + \nu^2} =: \Sigma_t$ and $a u = -\Sigma_t^2/2$. Define $d = V_0 e^{\nu^2}/(\bar\ell F^{\text{ps}})$, so $y = -\ln d$ and $e^{2ay/b^2} = e^{-y} = d$. Substituting into Step 3 gives (23.3).

**Step 5 (calibration).** CreditGrades links the unobservable $(V_0, \sigma_V)$ to the stock through $\sigma_E = \sigma_V \frac{V}{S}\frac{\partial S}{\partial V}$, the same identity as (23.1). Far from default, $S \approx V - \bar\ell F^{\text{ps}}$ and $\partial S/\partial V \approx 1$; the document shows (pp.10–11) that the choice (23.4) satisfies both the near-default and far-from-default boundary conditions.

**Step 6 (the CDS spread).** Per unit notional, the premium leg is worth $s \int_0^T e^{-ru}\mathcal{S}(u)\,du$ and the protection leg $(1-R)\big[1 - \mathcal{S}(0) + \int_0^T e^{-ru}(-d\mathcal{S}(u))\big]$, the bracket's first term being the loss paid at once on the mass already in default at inception. Setting the two equal and solving for $s$ gives (23.5).

#### Parameters and empirics: which vol, which horizon, which debt

The document's defaults are $\bar\ell = 0.5$ and $\nu = 0.3$, the latter estimated from roughly 300 U.S. non-financial defaults over 1987–1997, with the note that "a lower λ is expected for the financial sector" (their $\lambda$ is our $\nu$). Debt per share includes financial debt, capital leases, under-funded pensions, and preferreds, and excludes payables and deferred taxes. On 6,194 CDS quotes for 122 U.S. firms through August 2001, the implied asset volatility was "quite stable," and "a simple measure of volatility based on the last 1000 days of equity returns produces good estimates of the volatility implied by the 5-year CDS quotes," with 88% within 10%. The document also tests at-the-money implied vol of the longest listed tenor. Kaz's instinct is to use one-month implied vol, and they defend it at the whiteboard. "It's the market's view. The thousand-day number is a history lesson."

"Which market's view of what?" Ines asks. "The one-month option is the market's view of the next month, and you're pricing a five-year claim. Ask the five-year question of the longest option that trades, or of a thousand days that at least contain a bad year."

Theo is still on the other input. "And which debt goes in debt per share? In March 2023 Carvana designated ADESA US Auction, LLC an unrestricted subsidiary under its unsecured indentures, which released its guarantees, before launching an exchange offer (Carvana 8-K, March 22, 2023). The consolidated debt per share didn't move a cent. What the unsecured notes could reach did. The barrier moved by board resolution, and the column never noticed."

Kaz reaches for a sticky note to write *which F?*, sees the one already on the bezel from the replay, and puts the pad down. "Debt per share comes from the balance sheet," they say slowly. "The barrier comes from the indenture."

> **Ways This Blows Up.** *The time-zero ghost.* For a healthy name the mass $1 - \mathcal{S}(0)$ is negligible (about $10^{-4}$ for $S_0 = 30$, $\sigma_E = 40\%$, $F^{\text{ps}} = 30$). For a stressed name with $S_0 = 5$ and the same debt, it is about 25%: the model says a quarter of the default probability happened before you finished reading the screen, which inflates short-tenor spreads and inverts the curve (Figure 23.3). *The published closed form.* A later paper in the *Journal of Credit Risk* by Kiesel and Veraart has been reported to identify an error in the document's closed-form spread; we have not verified the details, so the reference engine integrates (23.5) directly and checks (23.3) against Monte Carlo. *Financials.* $\nu = 0.3$ was fitted on non-financials, and debt per share for a bank is mostly deposits, at which point the model is pricing a run with a diffusion (Section 23.8). *Two recoveries.* $\bar\ell$ is the global recovery that sets the barrier; $R$ is the recovery on the CDS reference obligation. Setting them equal by habit is a silent error. *The inversion floor.* Implied asset vol from a CDS quote is well posed only if the quote sits above the spread the model produces at near-zero vol; below that floor there is no answer, and the solver should say so rather than return its bracket endpoint.

### Specification for AI Implementation

**The Spec You Hand the Robot (what ROBO built from the vague version).** Asked to "compute the equity-implied CDS spread," ROBO used one-month at-the-money implied vol as asset vol, treated deposits as equity, and reported SVB Financial Group at 12bp on March 8, 2023. Every one of those choices was permitted by the sentence it was given. The precise version follows.

**Schemas.**

- `EquityState`: `S0: float` (last trade, \$ per share), `sigma_E: float` (annualized decimal, tagged `"hist1000d"` or `"atm_impl_longest"`), `q: float` (dividend yield), `shares_out: float`.
- `DebtPerShare`: `F_ps: float` (\$ per share) with components `{financial_debt, capital_leases, pension_deficit, preferred}` and an `asof` date. Deposits are **not** a component; banks route to the Section 23.8 engine.
- `CGParams`: `ell_bar = 0.5`, `nu = 0.3` (flag any override; financials require an explicit override and a reason), `R: float` (reference-obligation recovery), `r: float` (continuous, decimal).
- `CDSQuote`: `tenor_years`, `par_spread_bp` or (`upfront_pct`, `coupon_bp`), `recovery`, `curve_date`.

**Guards.** Raise on `S0 <= 0`, `sigma_E <= 0`, or `F_ps <= 0` (no debt, no CDS). Clip $d_{1,2}$ to $\pm 40$ before `norm.cdf`; compute $d\,N(\cdot)$ in (23.3) through `norm.logcdf` so large $d$ does not overflow. Times in years (ACT/365), spreads decimal internally and bp only in printouts. Return `nan` from the implied-vol inverter outside the model's range. The code blocks in this chapter run in order in one interpreter.

Before the code, count what this section has asked of you: a Merton identity, a leverage skew, a translation from share price to asset state, a survival curve with a barrier, two legs of a swap integrated on a grid, an inverter, and a Monte Carlo cross-check. For one name, with a spreadsheet and a free afternoon, that is a tidy exercise. For every issuer on the screen before the open, it is a job for a machine, and the kind of job where a sign error on one line gives you a confident, wrong spread on every name at once. So the reference engine is a single listing that computes the chapter's numbers and then tests itself against the chapter's own claims before anyone looks at a screen.

The listing works in two layers. The first is Merton. `merton_equity` prices equity as a call on firm assets and returns the value with $d_1$ and $d_2$, clipped to plus or minus 40 so the normal CDF never sees an absurd argument. `merton_equity_vol` gives the leverage skew of (23.1), `merton_spread` the model spread of (23.2), and `merton_solve_V_sigma` runs the problem backwards: from a market cap and an equity volatility it solves for the unobservable asset value and asset volatility with `fsolve`, in log parameters so neither goes negative, and it raises if the solver fails to converge rather than return a half-solved pair.

The second layer is CreditGrades. `cg_asset_state` applies (23.4): asset value is the share price plus $\bar\ell$ times debt per share, and asset volatility is equity volatility scaled by $S_0/V_0$. `cg_survival` evaluates (23.3) in closed form, building the second term in logs. `cg_cds_spread` integrates both legs of (23.5) on a monthly grid and adds the time-zero mass $1-\mathcal{S}(0)$ to the protection leg; it accepts a scalar or an array of share prices, so a stock-price ladder is one call. `cg_implied_vol` inverts a market spread for equity volatility with `brentq` between 2% and 500%. `cg_survival_mc` is the independent witness: it simulates the time-shifted Brownian motion for which (23.3) is exact, with a Brownian-bridge correction for barrier touches between grid dates, and returns an estimate with its standard error.

Inputs are a price, a volatility, debt per share, a recovery and a rate; outputs are spreads and volatilities in decimals. Use it for a non-financial issuer with a liquid stock and a tenor of a year or more. Do not point it at a bank, where debt per share is mostly deposits (Section 23.8).

The edge case that bites is the inverter's floor. Barrier uncertainty $\nu$ keeps default probability positive even at near-zero volatility, so the model spread has a floor, and a quote below it has no solution. `cg_implied_vol` returns `(nan, nan)` in that case, and a caller that does not test for it will carry the `nan` quietly into a portfolio average. The checks at the bottom of the listing confirm the Merton round trip, a monotone survival curve, closed form within four standard errors of Monte Carlo, and an inverter that refuses a 0.01bp quote.

*The full listing is [Listing 23.1 in Appendix F](#code-23-1).*

The Monte Carlo check is deliberately honest about what it verifies: it simulates the time-shifted Brownian motion for which (23.3) is exact, so agreement tests the algebra and the code, not the approximation. If you simulate the "true" model instead, a lognormal against a barrier drawn once at time zero, you get a different time-zero mass, and the difference is the price of a closed form. Exercise 2 asks you to measure it.

> **Trend Watch.** *The equity-implied PD moved onto the systematic desk.* In 2002 CreditGrades was a dealer-consortium product sold as a screen. The academic evidence then hardened: Cremers, Driessen, Maenhout and Weinbaum (2008, *Journal of Banking & Finance*) found that option-implied volatility beats historical volatility in explaining both the cross-section and the time series of corporate spreads, with the level mattering most and the skew "to a lesser extent"; Zhang, Zhou and Zhu (2009, *Review of Financial Studies*) found that high-frequency equity volatility alone explains 48% of the variation in CDS levels, jump risk alone 19%, and 73% with ratings, macro and balance-sheet controls. By the 2020s, equity-market inputs were ordinary features in systematic credit engines: a summary of Blackstone's platform (an unsigned file, not a Blackstone publication) describes a default-probability model that uses "real-time equity market signals" (Blackstone_Systematic_Credit p.1), and BlackRock's PD model uses "market data of equity and bond instruments" (BlackRock_Systematic_High_Yield_Credit p.6). *What it means:* the equity-implied spread is no longer an edge by itself; it is a baseline feature, and the edge is knowing when it is wrong (Sections 23.6 and 23.8).

## 23.3 Puts vs. CDS: Carr–Wu and the Default Corridor

Ines has a line she uses on every new hire who arrives from a restructuring shop: "The put is the CDS that forgot to tell anyone." Theo gets it on a Tuesday, when he asks how the desk would get short a name he knows from his old life, a listed specialty retailer with a bond stack and no single-name CDS that anyone can find *(a fictional composite; all numbers illustrative)*. Ines answers with a hand history instead of a theory.

"Years ago, a client started buying put spreads from me on a name like yours. Seven-fifty strike long, two-fifty short, one-year expiry, stock at fourteen. A thousand contracts a day, every day, never haggling." She had thought it was somebody being clever about the skew, and she sold the spreads at what her vol surface said, forty-five cents. "Three weeks later the company skipped a coupon, and the stock opened at ninety cents. Every spread paid five dollars, the maximum. The markouts were the worst page I printed that year." What the client had been buying was not volatility. A \$7.50/\$2.50 put spread on a stock that will sit above \$7.50 until the filing and below \$2.50 after it pays exactly \$5 if the company defaults before expiry and nothing if it does not. At forty-five cents, that is a 9% discounted chance of default, about 575bp of the CDS that did not exist (at 40% recovery and a 3% rate).

Theo, who has watched stocks of filing companies open at pennies on more first-day mornings than he can count, sees it at once: the assumption that makes the spread a default claim is a statement about how companies file, and that is his old job. "So the stock never trades between the strikes."

"That's the bet," Ines says. "The put is the CDS that forgot to tell anyone."

She means it literally. For most of the names an ex-RSSG analyst knows best, the single-name CDS is either untraded or traded by four people who all know each other; by one 2025 count of cleared volumes, single names were on the order of 6% of index notional *(approx.)*. The listed put chain, meanwhile, is on OPRA, prints all day, and quotes strikes down to a few dollars. If you can turn a put spread into a default claim, you have a tradable single-name credit instrument for names where none exists.

Carr and Wu (2011, *Review of Financial Studies* 24(2), 473–505) showed that you can, under one assumption and no model.

**The claim to be priced.** The *unit recovery claim* pays \$1 at default if default happens before $T$:

$$
U(t,T) = \mathbb{E}^{\mathbb{Q}}_t\Big[e^{-r(\tau - t)}\,\mathbf{1}_{\{\tau \le T\}}\Big].
$$

**The assumption (the default corridor).** There are levels $0 \le A < B$ such that the stock stays above $B$ before default and below $A$ from default onward. The stock never trades inside $[A, B]$. That is the whole assumption; nothing is said about volatility, jumps above $B$, or dynamics after default.

> **Math, Gently.** *Two tickets and no model: dominance bounds.* Picture two lottery tickets. Whatever world turns up, ticket A pays at least what ticket B pays, and in some worlds more. Then A cannot sell for less than B: if it did, you would buy A, sell B, and pocket the difference today with nothing to lose later. That argument needs no probabilities, no volatility and no view, which is why it survives when every model on the desk is wrong. Squeeze the same argument from both sides, a ticket worth at least X and at most X in every world, and its price is pinned. A tiny number: under the corridor, a 10-strike put spread with its lower strike at zero pays exactly 10 if the firm defaults before expiry and nothing if it does not. It is ten tickets that each pay \$1 at default. If the spread trades at 0.48, each ticket is worth 0.048, and the market's discounted default probability is 4.8%. The proof below is this paragraph with a square at the end.

**The result.** For co-terminal American puts $P^{\text{Am}}(K)$ with expiry $T$,

$$
U(t,T) = \frac{P^{\text{Am}}(B) - P^{\text{Am}}(A)}{B - A}, \qquad \text{and with } A = 0:\quad U(t,T) = \frac{P^{\text{Am}}(B)}{B}. \tag{23.6}
$$

**Proof.** Hold one put struck at $B$ long and one struck at $A$ short. *Before default*, $S_t > B > A$, so both puts are out of the money; nobody exercises an out-of-the-money put early, and if there is no default by $T$ both expire worthless. *At default*, $S_\tau < A$ and both are in the money. Exercising both immediately pays $(B - S_\tau) - (A - S_\tau) = B - A$, so the spread is worth at least $B - A$ at $\tau$. No-arbitrage also caps an American put spread at the strike difference, so it is worth at most $B - A$. Pinned from both sides, the spread is worth exactly $B - A$ at $\tau$ and zero if $\tau > T$, which is $(B - A)$ unit recovery claims. $\square$

The proof never mentions a diffusion, a hazard, or a recovery rate. It needs only that the stock jumps through the corridor, which is how equity behaves when a firm files: SVB's stock fell about 60% on March 9, 2023 and was halted on March 10. It fails for slow bleeds. GM drifted from 2005 to 2009 through every corridor you could have drawn, which is a hint that the corridor is a statement about *how* a name defaults, and an ex-RSSG analyst usually has a view on that.

**The CDS side.** With a flat hazard $\lambda$ and recovery $R$, the credit triangle gives $s = \lambda(1 - R)$, and the same claim implied by CDS is

$$
U^{\text{CDS}}(T) = \int_0^T e^{-ru}\,\lambda e^{-\lambda u}\,du = \frac{\lambda}{r + \lambda}\Big(1 - e^{-(r+\lambda)T}\Big), \qquad \lambda = \frac{s}{1-R}. \tag{23.7}
$$

For a European put the payment comes at $T$ instead of at $\tau$, so the matching claim is $e^{-rT}(1 - e^{-\lambda T})$. With $\lambda = 5\%$, $r = 3\%$ and $T = 1$ the two are 0.0481 and 0.0473 *(illustrative)*; mixing them is a 7bp-of-URC error, which is the time value of getting your recovery at default rather than at expiry. For standard-coupon CDS, use the bootstrapped hazard curve from Chapter 24 rather than the triangle.

**The signal.** Define the basis in claim units, $\text{basis}_U = U^{\text{opt}} - U^{\text{CDS}}$, and convert it back into spread units by inverting (23.7). When the put spread is cheap to CDS, buy the put spread and sell CDS protection, sized so the default payoffs match: $n(B - A) = (1 - R)\times\text{CDS notional}$. The position is default-neutral by construction; what is left is a pre-default MTM spread between two markets with different investors, which is the trade.

Cruz López and Ibáñez (2021, *Quarterly Journal of Finance*) show a European version under endogenous default, with a corridor that forms at cash-outflow dates, and a moral that RSSG people will enjoy: "no equityholders' fresh money, no endogenous corridor." Whether the corridor exists depends on whether equity will fund the next coupon, which is a negotiation, not a parameter.

> **[SOURCE EXTRACTION]** *Schmid_Credit_Risk_Pricing_Models p.154:* "at least as expensive as the corresponding default swap premium"
>
> **Annotation.** Schmid's context is credit spread options: a spread option that can be exercised on default carries the default payoff inside it, so its price is bounded below by the matching default-swap premium. The same dominance logic is what drives Carr–Wu. Any instrument that pays at least the default leg in every default state cannot be cheaper than the default leg; the put spread pays *exactly* the default leg and nothing else, so it is priced at it. On a 2026 desk the bound is a screening rule: if a listed put spread with $B$ comfortably below the post-default trading level is offered *below* the CDS-implied claim, either the corridor is wrong (a slow-bleed name), the borrow is distorting the chain, or someone is selling you default protection too cheaply. Check those three in that order.

> **Poker Table.** *Who is lifting your puts?* Ines, on the hand history: "In single-name low-strike puts, the bid side is a crowd and the offer side is a person." Low-delta puts are where informed flow goes when it cannot get into the CDS, because the options are listed, small, and anonymous. Around earnings, a missed coupon, or a liability-management rumor, the markouts on puts you sold are the worst on the sheet. Replay the hand: you sold 20-delta puts at a vol that looked rich by your skew model; two days later the company announced a drop-down financing and the puts were worth five times what you sold them for. The skew was not rich. Your model did not know the credit agreement had a basket for it, and the buyer did. Chapter 13's Priming Risk Score belongs in your put-quoting engine, not just in your bond book.

## 23.4 Skew as Jump-to-Default

Section 23.1 produced a skew from leverage. Real high-yield surfaces have a low-strike wing far steeper than leverage alone can make, and the cleanest explanation is that the stock can jump to zero. Write the simplest model that says so: Merton's (1976) jump-diffusion with one possible jump, to zero, at a constant risk-neutral hazard $\lambda$.

> **Math, Gently.** *Counting rare events: the Poisson clock and the compensating drift.* The bell curve of Section 23.1 describes the *sizes* of ordinary moves: today the stock is up 1.2%, tomorrow down 0.7%. Some things are not sizes but *counts*. How many times this year will a meteor hit the car park? How many times will this company default (at most once, after which the count stops mattering)? The Poisson distribution is the law of counts of rare, independent events arriving at a steady rate, and its single parameter, the hazard $\lambda$, means "expected events per year." A hazard of 5% says to expect 0.05 defaults in a year, so the chance of none is $e^{-0.05} = 0.951$ and the chance of at least one is 4.9%. Now the drift. Under the pricing odds every asset must earn the risk-free rate on average, dead ones included. If roughly one stock in twenty goes to zero this year, the survivors have to make up the loss, so the living stock must drift about 5% a year faster than $r$. A tiny number, ignoring the wiggles: $r = 3\%$, $\lambda = 5\%$, start at 100. A survivor ends near $100 \times e^{0.08} = 108.3$; weighting by the survival chance gives $0.951 \times 108.3 = 103.0$, which is exactly $100 \times e^{0.03}$. The dead stocks sit in the average at zero, and the survivors' extra 5% pays for them. That extra drift is called the compensator, and it is the $+\lambda\,dt$ in the equation below. Chapter 5 owns the whole family of distributions; this is the only member this section adds.

Under $\mathbb{Q}$,

$$
\frac{dS_t}{S_{t^-}} = (r - q + \lambda)\,dt + \sigma\,dW_t - dN_t, \qquad N_t \sim \text{Poisson}(\lambda),
$$

where $q$ is the dividend yield and $\sigma$ is the pre-default diffusive volatility. The extra drift $\lambda$ compensates the jump, so that $e^{-(r-q)t}S_t$ is a $\mathbb{Q}$-martingale: alive stocks must grow faster to pay for the dead ones. This is the pre-default dynamics of Carr and Wu (2010) with constant hazard and no stochastic volatility. Price a put on that stock and you get (23.8), whose two-step derivation follows the story of what it means:

$$
P^{\text{JTD}}(K) = K e^{-rT}\Big[1 - e^{-\lambda T}N(d_2)\Big] - S_0 e^{-qT}N(-d_1) \;\xrightarrow{\;K \to 0\;}\; K e^{-rT}\big(1 - e^{-\lambda T}\big). \tag{23.8}
$$

#### Kaz prices the \$5 put twice

Kaz does not believe (23.8) the first time, which is the correct response to most formulas and the wrong one to this formula. They pick the most boring example they can think of: a \$100 stock, 30% volatility, one year, rates at 3%, no dividend, and a put struck at \$5, a ticket that pays only if the stock loses 95% of its value. First, Black–Scholes. The strike is ten standard deviations below the forward in log terms, and the price comes out at about $10^{-24}$ dollars, a number so small the desk's risk system displays it as zero and is right to. Then the same put under (23.8), with a hazard of 5%. The whiteboard says about 24 cents.

Kaz checks the arithmetic, then the code, then the arithmetic again, and finally does the limit by hand. As the strike falls toward zero, $d_2$ runs off to infinity and the diffusion term $N(-d_1)$ vanishes faster than $K$, so what is left is a floor linear in the strike: $P(K)/K \to e^{-rT}(1 - e^{-\lambda T}) \approx \lambda T e^{-rT}$. At $\lambda = 5\%$ that is 0.0473 per dollar of strike, and 0.0473 times \$5 is 24 cents. "The diffusion part is dead," Kaz says. "What's left is the jump. The put is worth the strike times the discounted chance the company dies before expiry."

"That's Section 23.3's claim," Theo says, and it is: the floor is exactly the European unit recovery claim of the corridor theorem with $A = 0$. The skew model and the corridor theorem agree, and the code checks it to four decimals. Ines, passing, puts the moral in one line, because she has sold too many of these: "Black–Scholes prices it at a rounding error. The market prices it at a hazard rate."

The second surprise follows from the first. Kaz feeds the (23.8) prices back into a Black–Scholes solver and asks what volatility each strike would need to fetch that price in a world without jumps. With $\sigma = 30\%$, $\lambda = 5\%$ and $T = 1$, the implied vol is roughly 36% at the money, 41% at 80% moneyness, 52% at 60%, 72% at 40%, and about 100% at 20% *(illustrative; the code prints the exact values)*. A pure diffusion cannot produce a positive floor in $P(K)/K$, so the implied vol that matches (23.8) has to go to infinity as $K \to 0$; the wing must blow up. That steep left wing is the signature of every HY name's surface, and Kaz has looked at hundreds of them without knowing that most of the steepness was a hazard rate in disguise.

Theo asks the question a restructuring banker asks of any number: over what period? The floor grows like $\lambda T$, so the low-strike wing at each expiry gives one point on the cumulative default curve. Fit the wing expiry by expiry and you have a hazard term structure read straight off the equity surface, ready to set beside the CDS curve, or to stand in for one on names that have no CDS. Figure 23.4 draws the blown-up wing and the floor.

![Figure 23.4: A jump to default lifts Black-Scholes implied volatility from 36% at the money to 102% at a strike of 20% of spot (left) and puts a floor under the put price per dollar of strike of about the one-year default probability, where a pure diffusion goes to zero (right). Illustrative: (23.8) with volatility 30%, one year, r = 3%, no dividend, and a hazard of 5% on the left and of 2.5%, 5% and 10% on the right.](assets/figures/ch23_jtd_skew_floor.png)

#### The Full Derivation of (23.8)

**Step 1 (condition on survival).** If $\tau > T$, $S_T = S_0 \exp\{(r - q + \lambda - \tfrac12\sigma^2)T + \sigma W_T\}$; if $\tau \le T$, $S_T = 0$. A call pays only on survival, so

$$
C = e^{-rT}e^{-\lambda T}\,\mathbb{E}\big[(S_T - K)^+ \mid \tau > T\big] = S_0 e^{-qT}N(d_1) - K e^{-(r+\lambda)T}N(d_2),
$$

$$
d_{1,2} = \frac{\ln(S_0/K) + (r - q + \lambda \pm \tfrac12\sigma^2)T}{\sigma\sqrt{T}} .
$$

This is Black–Scholes with the discount rate on the strike bumped by the hazard. Credit spreads, it turns out, were hiding in the risk-free rate the whole time.

**Step 2 (put–call parity).** Parity holds because the forward is unchanged, $P = C - S_0 e^{-qT} + K e^{-rT}$. Substituting Step 1's call gives the put in (23.8); as $K \to 0$, $d_2 \to \infty$ and $N(-d_1)$ vanishes faster than $K$, leaving the floor linear in the strike.

#### Jumps, stochastic volatility, and a hazard that moves

**Telling jumps from stochastic volatility.** Stochastic-vol skew and jump-to-default skew both steepen the wing, so do not diagnose from the implied-vol picture. Use the price ratio: under stochastic volatility $P(K)/K \to 0$ as $K \to 0$; under jump-to-default it flattens to a positive constant. The `floor_ratio` diagnostic in the spec is that test.

**Making the hazard depend on the stock.** A constant $\lambda$ is a first draft. Convertible-bond models use $\lambda(S) = \lambda_0 (S_0/S)^p$, so the hazard rises as the stock falls (Andersen and Buffum, 2003, for convertibles); Linetsky (2006) derives closed forms for a CEV diffusion with this kind of default. Carr and Wu (2010, *Journal of Financial Econometrics*) estimate a joint model with stochastic volatility and a Cox default arrival on eight firms rated from B to AAA, jointly fitting options and CDS. The $p > 0$ version is the one to use when the name is near the fulcrum, because the market's hazard is not constant when the equity cushion is the thing being negotiated.

> **Ways This Blows Up.** *One strike, one lambda.* Fitting $\lambda$ from a single low strike turns bid–ask noise into hazard noise; at 5–10 delta the spread can be half the premium. Fit across strikes and expiries with bid and ask as bounds, not mid as truth. *Borrow masquerading as default.* In hard-to-borrow names puts are the synthetic short, so low-strike puts are rich because borrow is expensive, not because default is likely. Back the borrow fee out of at-the-money parity first and put it in $q$. *American exercise.* Listed single-stock puts are American. At default the holder exercises at once, so the American floor is $K\,\frac{\lambda}{r+\lambda}(1 - e^{-(r+\lambda)T})$, not the European $K e^{-rT}(1 - e^{-\lambda T})$. The engine tags every chain with its convention and refuses to compare across them. *Dividends.* A name about to cut its dividend has a forward that is about to jump, and the low strikes know it before the board does.

#### Quant-Shop Life: four days of `floor_ratio`

*A fictional composite. The fund, its vendor, its PM, its names and every number are invented; the failure modes are the ordinary ones.*

Dana, the second-year data analyst whose week with a holder registry is told in Chapter 16, works at a systematic credit fund across town that has no market-making desk and no interest in Ines's replays. One spring her fund adds the jump-to-default diagnostic to its morning screen: for every issuer with listed puts, fit (23.8) across the chain and flag any name whose `floor_ratio` says the low-strike wing is pricing a hazard. On the Monday it goes live, it flags 41 names. The PM, who had expected three or four, asks Dana to "make it stop firing," a sentence with two possible meanings. She picks the honest one.

Monday goes on twelve names that turn out to share a venue. The options vendor had moved those chains to a new exchange feed the week before, and the new feed's exercise-style field defaulted to European. Twelve chains of American puts were being fitted against a European floor and compared with a CDS claim on the wrong timing, the at-default versus at-expiry gap of Section 23.3, and on names near the threshold that was enough. Dana does not fix the vendor's field. She files a ticket asking the vendor to fix it, adds a column of her own, `convention`, filled from the exchanges' contract specifications rather than the feed, and makes the comparison refuse to run when the two disagree.

Tuesday is reverse splits. Seven names had consolidated one-for-ten or one-for-twenty in the past year, and the archived strikes on the older expiries were still in pre-split dollars. A \$2 put on a stock now trading at \$30 looked like a ludicrously expensive lottery ticket. It was a \$40 strike.

Wednesday is borrow and the bottom of the chain. Eleven of the remaining names were hard to borrow, with fees from 15% to well over 100%, and their puts were rich because puts were the cheapest way to be short: the borrow masquerading as default from the box above, sitting in the forward where the dividend yield belongs. Backing the fee out of at-the-money parity moves ten of them off the list. Then the 5-delta strikes. The vendor's "mid" for a put bid at 0.05 and offered at 0.60 was 0.325, and the fitted hazard was the midpoint of nothing. Dana switches the fit to treat bid and ask as bounds, as the One strike, one lambda warning says, and nine more names go quiet.

Thursday is the dullest day of the four. Dana rebuilds the archive point in time, so that each morning's chain is the chain the fund could actually have seen that morning, with the convention and split factor it carried then, rather than the vendor's corrected history. A back-test on corrected data is a time machine, and nobody wants a time machine in their Sharpe ratio. It takes the whole day, and nobody thanks her.

Thursday evening the screen flags three names. All three have low-strike puts whose price per dollar of strike sits flat across the bottom four strikes, at levels between 6% and 11% a year, on chains with clean conventions and ordinary borrow. Two have no CDS at all. One of them files for Chapter 11 nine weeks later. The hazard had been on the screen all week under 38 names' worth of plumbing, and it became visible only when the plumbing was fixed. The spec that follows starts from Dana's ticket, which is why its first rule is a refusal to compare across conventions.

### Specification for AI Implementation (continued): the put-surface engine

**Schema.** `OptionChain` is a pandas DataFrame with columns `T` (years, ACT/365), `K` (\$), `cp` (`"P"` or `"C"`), `bid`, `ask` (\$ per share), and `american` (bool), plus optional `open_interest`. Pivoting by expiry gives bid and ask tensors of shape `(n_expiries, n_strikes)`, kept separate. Interpolate missing strikes linearly in *price*, never in vol, and never extrapolate outside the listed strikes. Every unit recovery claim carries a `convention` tag (`"at_default"` for American, `"at_expiry"` for European), and comparisons across conventions raise an error.

The corridor theorem is lovely and useless until it meets a real option chain. Real chains have ragged strikes, wide bids and offers at the bottom where the interesting information lives, American exercise on every listed single-stock put, and no one to tell you which convention a given row follows. The question the desk actually asks is blunt: the stock is down by half, the CDS says one thing, the puts struck at five percent of spot say another, who is right, and is the gap big enough to trade after costs? Answering that on every name, every morning, is a job for code, and the code needs a synthetic market inside it so that it can be tested against a world where the answer is known.

The listing starts with two pricers. `bs_put` is the textbook put, kept only as an independent reference; `jtd_put_price` is (23.8), the put on a stock that diffuses and may jump to zero at rate $\lambda$. The hazard enters as an extra drift term in $d_1$ and as a default-probability term in the payoff, written with `expm1` so that a small hazard does not lose its digits. `make_put_chain` uses it to manufacture a chain with a chosen half-spread, which is how the later checks get a market whose true $\sigma$ and $\lambda$ are known.

`urc_from_puts` is (23.6) in code. It selects the puts at one expiry, interpolates bid and ask linearly in price, and forms the claim from a put spread struck at $A$ and $B$. With $A = 0$ the claim is simply $P(B)/B$; otherwise the claim's bid is B's bid less A's ask, because you must sell one leg and buy the other, and the ask uses the opposite pair. It returns the bid, the ask and a convention tag: `at_default` if every put in the slice is American, `at_expiry` otherwise. `urc_from_cds` produces the same claim from a flat-hazard CDS under either timing, which is what the tag is for. `jtd_fit` fits $\sigma$ and $\lambda$ jointly to mid prices divided by strike, so the cheap low strikes are not drowned by the money, and returns `floor_ratio`: the lowest-strike price ratio over the floor the fitted hazard implies. A value near one says jump-to-default describes the wing; a value far from one says something else, stochastic volatility or borrow, does.

Inputs are a chain, spot, rate, dividend yield and a corridor; outputs are a bid-ask claim, a convention and a fitted hazard. Use it on liquid single names with listed puts deep into the wings and, ideally, a quoted CDS. Do not use it where the low strikes are dead or the borrow is special.

The edge case that bites is the corridor guard. `urc_from_puts` raises if $B$ exceeds the highest listed strike, or if $A > 0$ lies below the lowest. With $A = 0$, though, the low-side check is skipped, and a $B$ below the lowest listed strike would be priced by `np.interp` holding the first quote flat, a quiet extrapolation of exactly the kind the spec forbids. Choose $B$ at or above the lowest strike yourself.

*The full listing is [Listing 23.2 in Appendix F](#code-23-2).*

## 23.5 Greeks in Spread Terms: Natenberg for the Credit Desk

An options trader runs a book on four numbers: delta, gamma, vega, theta. A credit trader runs a book on CS01 and a feeling. This section gives the feeling a Greek letter.

> **Math, Gently.** *The slope under your feet, and how fast it changes: delta, gamma and Taylor.* Stand on a hillside where height is a price and the ground under you runs along the spread. Delta is the slope under your feet: one step east and you drop this much. Gamma is how fast the slope itself changes as you walk, the difference between a straight ramp and a bowl. For a small step the slope is all you need. For a big one the bowl matters, because the ground curves up to meet you, or away from you. Taylor's idea is to write the change as slope times step, plus one half of curvature times the step squared, and stop there. A tiny number: a bond with spread duration 4 and convexity 20, and spreads 100bp wider, a step of 0.01. The slope alone says the price falls $4 \times 0.01 = 4\%$. The bowl gives back $\tfrac12 \times 20 \times 0.01^2 = 0.1\%$, so the bond falls 3.9%. On a 10bp day the bowl's contribution is a hundred times smaller, which is why traders talk about delta every minute and about gamma only on days that move. Every Greek in this section is either a slope or a curvature measured in some coordinate, and the arguments on the desk are about which coordinate. Equation (23.9) is this box with the spread's name on it.

**Bonds.** Expand a bond's price in its spread, holding rates fixed:

$$
\frac{dP}{P} \approx -D^{\text{spr}}\,ds + \tfrac12 C^{\text{spr}}\,ds^2, \qquad \text{CS01} = D^{\text{spr}}\,P \times 10^{-4}. \tag{23.9}
$$

This is the duration–convexity identity with the yield replaced by the spread (Veronesi_Fixed_Income_Securities p.152 gives the rate version). Now write $ds = s\,(ds/s)$:

$$
\frac{dP}{P} \approx -\underbrace{D^{\text{spr}} s}_{\text{DTS}} \cdot \frac{ds}{s} .
$$

DTS is the exposure to *relative* spread changes, and relative spread volatility is roughly stable across spread levels, which is why DTS behaves like a vega-scaled delta. Ben Dor's team makes the point that spread volatility itself is unobservable and estimates it by maximum likelihood with $\sigma_t(s) = \alpha + \beta s_{t-1} + \gamma \hat{s}^2_{t-1}$ (Ben_Dor_Quantitative_Credit_Portfolio_Management p.70). Credit had no implied vol to read, so it built one out of a regression. Section 23.6 shows that it now has a listed one.

**CDS.** Bought protection with running coupon $c$, marked at market spread $s$, is worth per unit notional

$$
\text{MTM}^{\text{buy}}(s) = (s - c)\,\text{RPV01}(s), \qquad \text{RPV01}(s) \approx \frac{1 - e^{-(r+\lambda)T}}{r + \lambda}, \quad \lambda = \frac{s}{1-R}.
$$

Differentiating, the spread delta is $\text{RPV01} + (s - c)\,\text{RPV01}'$, which equals RPV01 at inception. The spread gamma at $s = c$ is $2\,\text{RPV01}'(c) < 0$, because a wider spread means a shorter expected premium stream. So bought protection is *short* spread convexity, and the bondholder, who is long credit, is long it.

Kaz once spent an afternoon arguing with Ines over whether long protection is long or short gamma. They were both right, in different coordinates. In *spread* space bought protection is short convexity; in *stock* space it behaves like a long put, because the model spread is a convex, decreasing function of the stock. Which gamma you report depends on which risk you hedge with: CDX if you hedge in spread, stock if you hedge in equity. A cross-asset book reports both and labels them.

**The Natenberg map.**

| Options Greek | Credit translation | What hedges it |
| :-- | :-- | :-- |
| Delta | CS01 (spread space) or shares per notional (stock space) | Index CDS; the stock |
| Gamma | Spread convexity; stock-space convexity of the model spread | Options on CDX; listed puts |
| Vega | Sensitivity to $\sigma_V$ through the model spread; CDX swaption vega | Swaptions; the equity surface |
| Theta | Carry plus roll-down | Nothing; it is why you are there |
| Jump | JTD: $(1-R)$ per unit notional, minus the hedge's jump | Put spreads (23.6); not the stock |

**Equity Greeks of a credit instrument.** Use the chain rule through firm value. In Merton, $\partial B/\partial V = N(-d_1)$ and $\partial E/\partial V = N(d_1)$, so $\partial B/\partial S = N(-d_1)/N(d_1)$ and the elasticity hedge ratio is

$$
h = \frac{\partial B / B}{\partial E / E} = \frac{N(-d_1)}{N(d_1)} \cdot \frac{E}{B}. \tag{23.10}
$$

For the illustrative firm of Section 23.1 ($V = 100$, $F = 70$), $h \approx 0.024$: a 1% stock move is a 2.4bp bond move. For a stressed firm $N(d_1)$ falls, $E/B$ falls, and the ratio of the two decides; the elasticity rises sharply as the name approaches the fulcrum, which is when bonds start trading like equity. In CreditGrades the corresponding "delta" is, in the document's words, the "number of shares of the equity required to offset small price moves" of a CDS position (Finger et al., 2002, p.14); its gamma rises as the stock falls, and its asset vega converts to equity vega through (23.4), $\partial/\partial\sigma_V = (V_0/S_0)\,\partial/\partial\sigma_E$.

**JTD: the Greek that is not a derivative.** Theo works this one on the whiteboard with Mags watching from the end of the desk, arms folded, which is how Mags watches anything she expects to go wrong. At default the stock falls to roughly nothing, so a protection buyer hedged with $\delta$ long shares collects $(1 - R)N$ on the CDS and loses about $\delta S_{\tau^-}$ on the stock. Theo sizes it for \$10mm notional on a \$30 stock: the CreditGrades delta is on the order of 20,000–25,000 shares, roughly \$0.7mm of stock *(illustrative)*. He circles the number. The book is delta-neutral.

"Now tell me what the stock does on the day the bonds pay forty," Mags says.

Theo writes it underneath. The protection pays \$6mm at 40% recovery. The stock, \$30 a week earlier, opens at pennies, and the \$0.7mm of shares goes with it. "Six million in, seven hundred thousand out."

"And if you'd *sold* the protection, which is what Kaz's screen will tell you to do half the time?"

"Six out, seven hundred in." Delta hedging a CDS with stock leaves almost all of the jump on the table, in whichever direction the trade happens to face. That is not a flaw in the hedge; it is the reason the stock is the wrong instrument for JTD.

Mags unfolds her arms, which from Mags is applause. "The stock hedges delta," she says. "Nothing you do with the stock itself hedges the jump." The desk has kept the sentence. The put spread of (23.6), which pays its strike difference on exactly the day the shares go to pennies, hedges the jump, and a complete capital-structure book holds both.

> **[SOURCE EXTRACTION]** *Dynkin_Systematic_Investing_in_Credit p.87:* "Research has shown that analytical equity hedge ratios based on the Merton model make reasonably accurate predictions of how corporate bond returns vary given the corresponding equity returns (Schaefer and Strebulaev 2008)"
>
> **Annotation.** This is the most useful sentence about structural models ever written, because it separates the part that works from the part that doesn't. Schaefer and Strebulaev (2008, *Journal of Financial Economics*) find that Merton predicts spread *levels* badly but bond-to-equity *sensitivities* well, and Dynkin's team reports analytical hedge ratios only about 5% below empirical ones in both IG and HY. Capital-structure arbitrage is therefore a bet that the hedge ratio is right and the price is wrong, which is a coherent bet. The page that follows supplies the caveat: for high-equity, low-debt growth names (Dynkin's example is a Netflix-type HY issuer), the Merton ratio comes out far too low because "it uses the leverage ratio as one of the few inputs" (Dynkin_Systematic_Investing_in_Credit p.88). The 2026 fix is an empirical overlay: shrink the model hedge ratio toward a rolling regression elasticity, with the shrinkage weight a function of how far leverage is from the training sample.

> **Ways This Blows Up.** *The sign flip.* A long-bond, short-stock book assumes bonds and stock move together. On a liability-management rumor, or a takeover bid, the stock rallies while the excluded creditors' bonds drop, and you lose on both legs; Section 23.6's May 2005 autopsy is the canonical case. *Gamma near the barrier.* As the stock approaches the default region the CreditGrades delta changes fastest, so daily rebalancing turns into rebalancing every hour, at the bid–ask of a stock that is gapping. *Wrong duration.* Using modified duration where spread duration is needed (floaters, callables, loans) mislabels rate risk as credit risk, and the hedge ratio inherits the mistake.

### Specification for AI Implementation (continued): spread Greeks

The last few pages gave you five Greeks in prose, and prose does not get a hedge ticket sent. The risk meeting asks a plainer question about the same name: if the spread moves one basis point, what happens to the bond, what happens to the protection, and how many shares do I buy against it? If three people answer on three spreadsheets with three bump sizes, the book's number never ties to the desk's number, and the morning is spent reconciling instead of trading. The cure is one differencing routine, applied to every instrument, so that the answers are comparable by construction.

The listing has three layers. The first is a pair of pricing primitives. `cds_rpv01` is the risky annuity of a flat-hazard CDS, with hazard equal to the spread over one minus recovery, and `cds_mtm_buyer` is the protection buyer's mark: spread minus coupon, times that annuity. `bond_price_flat` prices a semiannual bond discounted at the risk-free rate plus a flat spread. The second layer, `spread_greeks`, takes any function from a spread to a price, bumps the spread up and down by one basis point, and returns spread duration, convexity, CS01 and duration times spread; because it takes a function, a bond, a loan and a CDS all go through the same code. `merton_elasticity` is (23.10) in closed form, the percent move in the bond per percent move in the stock.

The third layer, `cg_greeks`, is the one a hedge ticket needs. It strikes a protection position at today's CreditGrades spread, so the mark starts at zero, then reprices it under bumps. Delta is the negative slope of the mark in the stock price (a central difference of 1% of the share price), reported as shares to buy against the protection; gamma is the second difference in stock space; equity vega is one volatility point, and asset vega rescales it through (23.4). The repricing values the annuity with the flat-hazard formula at the new model spread, not with the CreditGrades integral.

Use it for sizing a stock hedge and for risk reporting on non-financial names with a liquid stock. It does not hedge the jump (that is the put spread's job), and it is no use for instruments with optionality in the spread. The checks confirm that duration and convexity explain a 50bp move, that bought protection is short spread convexity, and that the hedge ratio rises as the stock falls from \$30 to \$15.

The edge case that bites is the coupon. Because the position is struck at the model spread, the term (spread minus coupon) vanishes at the start, and delta collapses to the annuity times the slope of the model spread. A real trade done at a standard coupon with an upfront, or at a spread away from the model's, carries a nonzero mark and therefore a different delta. Greek the position you hold, not the par trade.

*The full listing is [Listing 23.3 in Appendix F](#code-23-3).*

## 23.6 Capital-Structure Arbitrage: Rules, Returns, and Why Single Trades Lose

Theo's first question about any cap-structure trade is "but what does the indenture say about the fulcrum?", and it is the right first question for a reason the model cannot see: the trade assumes the stock and the CDS are claims on the same value under the same rules. The second question is the model's: how far apart are they, and how fast do they come back together?

**The rule (Yu, 2006, adapted).** Compute the CreditGrades spread $s^{\text{CG}}_t$ from (23.3)–(23.5) using 1000-day or longest-tenor implied equity vol, and define the relative mispricing

$$
z_t = \frac{s^{\text{mkt}}_t - s^{\text{CG}}_t}{s^{\text{CG}}_t}. \tag{23.11}
$$

If $z_t > \alpha$, the market spread is rich to the equity: sell protection and short $\delta_t$ shares. If $z_t < -\alpha$: buy protection and buy $\delta_t$ shares. Here $\delta_t$ is the CreditGrades delta from Section 23.5, rebalanced daily, and Yu tests $\alpha \in \{0.5, 1, 2\}$. Exit on convergence ($|z_t| < \epsilon$), at a 180-day limit, or at a stop. Ex post, decompose the P&L as

$$
\Delta\Pi = \underbrace{-\,\text{RPV01}\cdot\Delta(s^{\text{mkt}} - s^{\text{CG}})}_{\text{convergence}} \;+\; \underbrace{c\,\Delta t}_{\text{carry}} \;+\; \underbrace{\tfrac12\Gamma_S\,(\Delta S)^2}_{\text{gamma}} \;+\; \underbrace{\text{JTD}\cdot\Delta N}_{\text{jump}} \;-\; \text{costs},
$$

for a protection seller, with signs flipped for a buyer. Only the first term is the thesis. "IDO or it didn't happen" applies here with force: carry is compensation for the jump term, and a backtest that books the carry and simulates no defaults has discovered that selling insurance is profitable in years without fires.

**What the evidence says.** Yu (2006, *Financial Analysts Journal*) runs the rule on 135,759 daily CDS spreads for 261 North American obligors over 2001–2004. Individual trades can lose heavily, because at short horizons CDS and equity are weakly correlated; an equally weighted portfolio of trades earns Sharpe ratios comparable to other fixed-income arbitrage strategies, and the speculative-grade monthly index has a Sharpe ratio of 0.75, uncorrelated with equity and bond factors. Kapadia and Pu (2012, *Journal of Financial Economics*) explain why: short-horizon pricing discrepancies are common, a significant fraction are anomalous rather than mean-reverting, and the degree of integration varies with frictions such as liquidity in both markets and idiosyncratic risk. Duarte, Longstaff and Yu (2007, *Review of Financial Studies*), asking whether fixed-income arbitrage is "nickels in front of a steamroller," find that strategies requiring more "intellectual capital," capital-structure arbitrage among them, earn significant alphas after factors and fees, with positively skewed returns. The single trade is a coin flip with a thesis attached; the portfolio is the edge.

> **Poker Table.** Ines: "A convergence trade is short a straddle on time." You are paid if the gap closes before your patience, your capital, or your risk manager runs out, and you lose if it widens first, which in this market is the more common short-horizon outcome. Size so that a 2x widening is a bad day, not a career event. Then replay the hand: on the trades that lost, did the gap widen because the model was wrong (a hedge ratio problem), because the market was wrong for longer (a capital problem), or because the rules changed (a credit-agreement problem)? Only the first is fixable with math.

### Case Study A: May 2005, GM and Ford, or How to Lose on Both Legs

**The setup.** By spring 2005 General Motors and Ford were investment-grade issuers drifting toward high yield, and GM was one of the largest names in both the convertible market and the CDS index tranches. Hedge funds held two popular structures on it. Convertible arbitrage: long GM convertibles, short GM stock, a trade "motivated by discrepancies between the price at which convertible bonds issued by GM were trading and the price of a replicating portfolio (consisting of regular bonds plus equity call options)" (BIS *Quarterly Review*, June 2005, p.6). Correlation: sell protection on the equity tranche of the iTraxx Europe index and buy index protection as a hedge, which "would have earned a spread of 300 to 400 basis points" and is "commonly referred to as a long correlation position" (ibid.).

#### Long Scene: GM, 3–5 May 2005 (replay)

*A replay, cut at the close of Tuesday, May 3, 2005, and dealt on a Friday afternoon in October 2026. The pair is Pair Book entry PB-04, which Owen Achterberg's capital-structure pod at Vantress (Chapter 4-C, a fictional composite) opened at Chapter 6's replay and keeps in its ledger as a teaching trade; this is the second sitting of the same hand. GM's and Tracinda's filings, S&P's rating actions and the BIS account are real and cited, and no real person's words are invented. The CDS and model marks, the positions, sizes and P&L, and all dialogue are invented and illustrative.*

The *4 May* envelope from the first sitting lies on the table, still sealed, with Ines's coffee on top of it. She does not open it yet. The model on the screen has changed since that night, from Merton to CreditGrades, and she wants a second card from everyone before anybody sees Wednesday. Mags, who spent the first sitting against the wall under the rule for people with memories, pulls her chair in. "I was there for the tape," she says. "Nobody asked me this question in 2005." Ines lets her play and says her card will carry an asterisk.

*The screen.* Kaz has the $z$ column up before Ines has finished dealing. The rule is (23.11), and the inputs are the ones Section 23.2 argued about and settled: 1000-day equity volatility, debt per share from the last annual report, $\bar\ell = 0.5$, $\nu = 0.3$. On the replay deck's marks, GM's five-year CDS is at 650bp and the model says 380bp, so $z = (650 - 380)/380 = 0.71$ *(illustrative; the deck rounds its marks because the real tick history is not in the room)*. That clears the lowest of the three thresholds Yu tests, and the screen's instruction is the one written above: the market spread is rich to the equity, so sell protection and short the CreditGrades delta in stock.

"Ten million notional, full size," Kaz says. "With the stock at twenty-seven *(illustrative)* the delta is about forty thousand shares. Call it a million and change of short stock against ten million of sold protection." They have the evidence ready, because Kaz always has the evidence ready: Yu's 261 names, the Sharpe ratios, the intellectual-capital alphas, all of it summarized two pages back. "The portfolio works."

"The portfolio is 261 names," Ines says. "This is one. Which one is it?"

*The table argues.* Mags has been reading the deck's other pages, which is what she does instead of looking at $z$. "Who benefits if somebody bids for the stock?"

Kaz finds this a strange question. "The stock."

"And the bonds?"

"If the firm is worth more, then everyone..." Kaz stops, because Kaz has just heard it. A bid for the stock is not a statement that the assets are worth more. It is somebody paying for influence over the residual claim, and nothing in that payment reaches a creditor. A buyer who wants the equity to be worth more may even like the leverage.

Theo has gone to the creditors' pages of the deck and found what a restructuring banker always finds first, which is a calendar. "This is an investment-grade name about to stop being one. GM and Ford together are about three percent of the investment-grade bond market, and they could be up to fifteen percent of global high yield (BIS *Quarterly Review*, June 2005, p.6). The index providers use an average of three ratings, so when the agencies move, the exit isn't a surprise. It's a schedule. Every holder that tracks an investment-grade index becomes a seller on a date you can write down." He turns a page. "And the deck has a convertible desk down the hall that's long GM converts and short GM stock. Same name. Same stock."

Ines nods slowly. This is the part of the hand she wanted someone to find. "And a correlation book that has sold protection on the equity tranche of an index GM sits in. So our sold protection, their converts and their tranche are one trade wearing three hats. Whatever hits GM hits all three in the same afternoon, and every one of them will want to buy back the same stock at the same time."

"The model has a column for none of that," Kaz says, with the air of someone reporting a fact rather than conceding a point.

"No," says Ines, and deals the cards.

#### The GM Card: Which Legs, What Size, Which Path

*Write three things: which legs you put on, in what size, and the single two-day path that loses on both.*

Kaz writes quickly: sell \$10mm of five-year protection, short 40,000 shares, rebalance daily. For the losing path Kaz writes "default," looks at it, and adds a note that the premium is paid precisely to bear that, which is true and is not an answer to the question.

Mags writes the same two legs at half the size, then adds a third: one-month calls on the stock, about 20-delta, on 50,000 shares, as insurance on her short. She labels them *the Kerkorian put*, after the 1995 bid for Chrysler, which she missed by a year and has heard about ever since. "A cheap car company with a famous name gets a rich man sooner or later. I'd rather pay for the calls than find out which week." Her losing path: "Somebody likes the stock on Monday and the agencies don't like the bonds on Tuesday."

Theo writes *no trade* in the first two lines and leaves the size at zero. For the path he writes: "Day one, something good for the stock that does nothing for the bonds. Day two, the agencies." Underneath, smaller: "Don't know what day one is. Day two is on a calendar."

The reader has a card too, and should fill it in before turning the page.

#### The Tape, and the Cards Graded

Ines turns over the first day.

| Date (2005) | Event | Equity | Credit |
| :-- | :-- | :-- | :-- |
| May 3 | Last trading day before Tracinda's announcement (Schedule 14D-9) | | |
| May 4 | Kirk Kerkorian's Tracinda offers to buy up to 28mm GM shares (about 4.95%) at \$31.00 cash; it already holds 22mm (about 3.89%) | GM up about 18% | |
| May 5 | S&P downgrades GM two notches to BB and Ford one notch to BB+ | Falls back | Bond and CDS spreads gap wider |
| May 9 | Tender offer commences; expires June 7 | | |
| June 1 | Both names leave the CDX and iTraxx indices at the roll | | |

*Wednesday, May 4.* A cash tender for up to 28 million shares at \$31, from an investor who already holds 22 million. "Tender," says Kaz. "As in gentle?" "As in cash," says Mags, who is already doing the arithmetic on her calls. GM's stock closes up about 18%. On the deck, the CDS does not move: a bid for 5% of the equity says nothing about whether the bonds get paid. Kaz's short stock loses about \$194,000 on the day *(illustrative, as are all the P&L figures that follow)*. The model, seeing an 18% higher stock, lowers its spread from 380bp to about 340bp, so the gap that was supposed to close has widened by 40bp. Mags's calls, bought for \$0.35 and now well in the money, pay a little more than her half-size short loses, and she sells them at the close.

*Thursday, May 5.* S&P cuts GM two notches to BB and Ford one notch to BB+. The stock gives back some of Wednesday, and the credit does what Theo's calendar said it would: bond and CDS spreads gap wider, on the deck by 30%, from 650bp to 845bp. At an RPV01 held at 4.2 for the arithmetic, Kaz's sold protection loses \$819,000. The rebalanced short claws back about \$43,000. Nobody on Thursday was buying the stock for the bonds' sake, and nobody was buying the bonds for the stock's.

The BIS put the episode in one sentence that every capital-structure desk should frame. Investors in the convertible trade "lost money on both legs of the trade: on 4 May GM's stock price increased by 18% after an offer from turnaround specialist Kirk Kerkorian to buy a large stake in the company, and then on 5 May the company's bond and CDS spreads increased after S&P's downgrade" (BIS *Quarterly Review*, June 2005, p.6). The deck's convert desk lost on both legs, exactly so. The short stock lost on the bid; the long credit lost on the downgrade. The correlation book lost separately: "Investors expecting default correlations to remain stable or increase were surprised in May when they instead fell sharply," and "at times in early May the two moved in opposite directions," meaning the mezzanine tranche and the index (ibid.). The BIS judged the episode "similar in nature, albeit certainly not in magnitude" to 1998. Convertible-arbitrage funds lost about 8% in early 2005, in what one later retrospective called "the worst environment since 1994" (Resonanz Capital, July 10, 2025). Specific fund-loss rumors at the time were denied and are not repeated here.

Ines grades Kaz's card with the chapter's own decomposition, because a loss nobody can split into its pieces teaches nothing. Over the two days Kaz's book lost about \$967,000 on \$10mm of notional. The convergence term, $-\text{RPV01}\cdot\Delta(s^{\text{mkt}} - s^{\text{CG}})$, accounts for about \$937,000 of it: the gap widened by 40bp on Wednesday, when the model's spread fell and the market's did not, and by another 183bp on Thursday, when the market's spread jumped and the model's barely moved. Carry earned about \$3,600 over two days. The jump term is zero, because nobody defaulted; Kaz's losing path never arrived, and the book lost anyway. The gamma term cost about \$33,000. A protection seller hedged in stock is short convexity in stock space, Section 23.5's coordinates, so every big move in either direction costs a little.

Mags's book lost about \$380,000 on half the notional. Her calls are the only line in either book with a plus sign: a long call is long gamma, and on Wednesday the gamma term in her book was positive and almost exactly paid for her short. On Thursday nothing helped her, because nothing on the stock side hedges a creditor event. Ines marks her card "right about Wednesday, priced Thursday as a risk she was paid to take, and half the size, which is the only reason she can laugh about it." The asterisk stays on: a card from somebody who was there in 2005 counts for its reasoning, and the reasoning, insure a short stock against a bid, is the part worth keeping.

Theo made nothing and lost nothing. Ines turns his card over twice. "Right," she says, "for a reason the model has no column for." He did not know what Wednesday would be, and he said so. He knew that Thursday was a scheduled event in the creditors' world that the equity-implied spread had no way to see, and that the pair's two legs would not be standing on the same ground when it came.

Then Ines lifts her coffee and opens the envelope. Owen's first-sitting card, \$10mm sold and \$0.4mm of stock short by the Merton delta, would have lost on both days, exactly as Kaz's did. Theo's first card has Owen's sizes and a bad day that now reads like a forecast: "anything good for the shareholders and bad for the creditors, or a downgrade on a day when somebody wants the stock." He had the path at the first sitting and traded anyway. Tonight, with the index calendar in front of him, he did not, and Ines says the difference between the two cards is the whole chapter. Mags's only contribution that night, called from the wall without turning round, was "Write down who else is in it." Owen had written it down. Tonight Theo found who: the convert desk and the tranche book.

Why could the model not see it? Both legs were hedged against *the same* shock to firm value. May 4 and May 5 were two different shocks: a large shareholder bidding for equity, an equity-holder event that did nothing for creditors, and a ratings action with forced-selling consequences, a creditor event that did nothing for the bid. In Merton language, $\sigma_V$ did not change; the claim structure did, because a buyer of a control-sized equity stake and an index-eligibility cliff are not in the model. In RSSG language, Theo would have asked who benefits from Kerkorian's stake, and the answer, "not the bonds," is the hedge ratio flipping sign. The reader's card is graded by the same question. If your losing path had two different kinds of event on two different days, give yourself the marks Theo got; if it had one shock moving both legs, you were trading the model's world, which is the one that did not happen.

<!-- FIGURE (brief §3): ch23_gm_2005_two_leg_pnl.png — two-day P&L of PB-04 by leg and net; note for U4: the gamma bar is negative for Kaz's book (short stock-space convexity); the only positive bar is Mags's call. -->

Ines writes up the replay's ledger line for PB-04 herself, because closing a pair is the part of the ritual she trusts no one else with, and sends it to Owen. *Hedge:* the model delta, the Duarte–Longstaff–Yu rule, which removed the stock's ordinary daily wobble from the sold protection and nothing else. *Idio:* the gap between GM's CDS and its equity-implied spread, the one thing the trade meant to own. *Leaks:* an equity-holder event and a creditor event on consecutive days, each moving one leg and not the other, plus the correlation book's separate loss in the same week, which arrived through the same crowded exit. *What it costs to carry:* on paper the sold protection carries 650bp a year, which is the bait; the honest number is capital, and Duarte, Longstaff and Yu put it at \$66.25 of capital per \$100 of CDS notional, equal-weighted, to run the strategy at 10% volatility (2007, Table 5), many times what a swap-spread trade needs. *What it costs to short:* the borrow on the stock, the dividend the short owes while it is open, and, on days like Wednesday, the price of buying back stock alongside every other hedged desk in town. *The sequel:* on 70 obligors over 2005–2009, the same classical rule produced negative Sharpe ratios both before and during the crisis (Avino and Lazar, 2012). Status: closed in this chapter, at a loss, as a teaching entry.

Then Ines says the line the desk now works by. Every capital-structure book is shocked to the May 2005 vector, stock up 20% and spread up 30% at once, and the loss is capped. Any name within a notch of high yield carries a forced-selling column for its index exit. A name that is simultaneously the book's hedge, somebody's convertible hedge and an index constituent gets one limit, not three. And the morning a 13D, a tender offer or an activist stake appears, the name moves to a "hedge ratio unreliable" state and its $z$ is suspended until somebody has read the filing.

> **Math, Gently.** *A stretched rubber band: persistence, half-life, and why the Sharpe decays.* Think of the gap between the CDS and the equity-implied spread as a rubber band stretched away from zero. Each day it lets go of part of the stretch and takes a random new tug. The persistence $\phi$ is the fraction of the stretch it keeps: tomorrow's gap is $\phi$ times today's plus noise, which is all "AR(1)" means (one lag, one coefficient). A $\phi$ of 0.9 lets go of 10% a day; a $\phi$ of 0.99 lets go of 1%. The half-life, the number of days for half the stretch to disappear, is $\ln 0.5/\ln\phi$. A tiny number: at $\phi = 0.9$ the half-life is $\ln 0.5/\ln 0.9 \approx 6.6$ days, and at $\phi = 0.99$ it is about 69 days. A convergence trade earns the daily let-go and suffers the daily tug, and the ratio of the two, its Sharpe per unit of noise, scales like $\sqrt{(1-\phi)/(1+\phi)}$: about 0.23 at $\phi = 0.9$ and 0.071 at $\phi = 0.99$, less than a third as good from a change in the second decimal of one parameter. Read that way, the 180-day stop in Yu's rule is a bet on $\phi$: it says a gap whose half-life runs to several months is not a mispricing anyone can afford to wait for. GM in May 2005 was worse than a high $\phi$, because the band was not being tugged at random; it was pulled, two days running, by two different hands. Chapter 7-B owns autocorrelation; here it is enough to read $\phi$ as patience, priced.

<!-- FIGURE (brief §3): ch23_persistence_sharpe_decay.png — half-life ln 0.5/ln φ and Sharpe scale √((1−φ)/(1+φ)) against φ from 0.5 to 0.995, marking φ = 0.9 (6.6 days, 0.23) and φ = 0.99 (69 days, 0.071), with the 180-day stop drawn as a vertical line on the half-life axis. Pending U4. -->

Owen's pod keeps a second capital-structure pair in the ledger whose hedge failed for a different reason, and it earns one box here before Chapter 14 tells its ending.

> **The Pair.** *Pair Book entry PB-05, Owen Achterberg's capital-structure pod at Vantress (fictional composite; a replay; hedge ratios illustrative). Carvana's prices, filings and dates are real and cited, and the pair's losses are computed from them.* **Thesis.** Carvana's stock had closed at \$3.72 on 27 December 2022, about 99% below its 2021 peak, and the notes had ended that year in the 40s (the 10-K's fair-value mark for the whole stack was 44.8). By the spring the equity surface still said default, and on 2 June 2023 the company's first exchange offer died for want of its \$500mm minimum participation. Owen's pod bet that the notes were the better claim on the same firm. **Legs and hedge.** In a replay cut at that Friday's close, long \$10mm face of the 5.875% notes due 2028 at 55 and short Carvana common at the structural model's delta, 0.30 of the notes' market value, resized monthly (Chapter 14 has the sizes). **What the hedge removed.** Nothing that mattered. A delta assumes the stock and the notes are two strikes on one firm value, rising and falling together at a known ratio. **What idio remained.** The exchange. On 19 July 2023 Carvana announced a transaction support agreement with holders of over 90% of the notes, and the stock rose about 40% in a day to \$55.80; the exchange settled on 1 September 2023 with 96.4% of the notes tendered (Carvana 8-Ks; Q3 2023 10-Q). **What leaked.** The equity was a closing condition of the credit's recovery. The support agreement could terminate unless at least \$350mm of new equity was raised, and the controlling Garcia Parties bought \$126mm of stock at \$46.31 to help fund the deal: the rally the short was betting against was the money that paid the noteholders. Computed from the fair-value marks and closing prices since 30 December 2022, a pair hedged anywhere in the 20–50% band a delta would have used lost money in every quarter of 2023, and by December the equity leg had lost two to six times what the notes gained; the break-even short never exceeded about 19% of the notes' value. **What it cost to carry and to short.** The notes paid their coupons. The short paid the borrow on a stock with 47% of its float already sold short (S3 Partners, as reported in July 2023) and carried recall risk at exactly the wrong moment. The close is Chapter 14's.

<!-- FIGURE (brief §3): ch23_carvana_breakeven_hedge.png — the dossier's break-even short-stock ratio h* by quarter of 2023 (never above about 19% of the notes' value) against the 20–50% band a delta hedge would have used. Caption: "every delta-sized pair lost in every period." Source: case_carvana_svb_wolfspeed_capital_structure.md §1.3 (calc). Pending U4. -->

### Specification for AI Implementation (continued): the cap-structure backtester

**What ROBO built from the vague version.** Told to "backtest capital-structure arbitrage," ROBO sold protection on every name, booked the carry, simulated no defaults, and reported a Sharpe ratio of 4. It was correct about the simulation it was given. The spec below strips carry from the convergence P&L, reports it separately, and states the noise model.

**Inputs.** `panel`: long DataFrame with `issuer`, `day`, `S`, `sigma_E`, `F_ps`, `s_model` (decimal, from CreditGrades), `ds_dS` (decimal per \$), `s_mkt`. Parameters: `alpha` (entry threshold on $z$), `eps` (exit), `hold_max_days = 180`, `cost_bp_cds` (running-spread equivalent, converted to upfront with RPV01), `cost_bp_eq` (bp of traded stock notional). Unit CDS notional per trade. Output: daily portfolio P&L, per-trade P&L, Sharpe, hit rate, and carry reported separately.

Here is the trouble with testing a capital-structure rule on real data: when the rule loses money, you cannot tell whether the model was wrong, the mispricing was never there, or the costs ate it. Real panels also contain only a handful of defaults, so the one outcome that ruins a protection seller is almost absent from the sample. A desk that wants to understand its rule before it risks capital builds a market where the answer is known: the model is exactly right, the market is the model plus noise, and the only dial is how long the noise remembers itself. Then the backtest measures the rule, not the data.

The listing runs three functions in sequence. `simulate_cg_panel` builds the world: twenty issuers over 500 trading days, each with a random starting price between \$15 and \$60, equity volatility between 25% and 60%, and debt per share between \$10 and \$60. Stocks follow geometric Brownian motion with no defaults, and for every day the function computes the CreditGrades spread at that day's price, together with the stock-space slope of the spread by a central difference of plus or minus 1% of the price. `add_market_noise` turns the model spread into a market spread by multiplying it by $e^{u}$, where $u$ is an AR(1) with persistence $\phi$ and a stationary standard deviation of 0.30.

`capstruct_backtest` trades the rules of (23.11) on the signal $z$, the market spread over the model spread, minus one. When $|z|$ exceeds `alpha` and the name is flat, it sells protection if the market is wide and shorts stock against it, or buys protection and goes long stock if the market is tight. The hedge is the annuity times the slope, rescaled to the market spread and rebalanced daily. It exits when $|z|$ falls below `eps`, after 180 days, or on the last day. Daily P&L is the change in the CDS mark plus the stock hedge's gain, less costs on entry, exit and every rebalance. Carry is accumulated but kept out of P&L. Outputs are an annualized Sharpe ratio, trade count, hit rate, the carry total and a trade ledger.

Use it to learn what a rule can and cannot do under assumptions you control, and to compare persistence regimes. Do not quote its Sharpe as a forecast: the data have no defaults, no jumps, no borrow fees and no gaps.

The edge case that bites is the time stop. A mispricing with persistence near one often fails to close inside 180 days, so the trade is force-closed wherever $z$ happens to sit, paying exit costs and realizing whatever the position lost on the way.

*The full listing is [Listing 23.4 in Appendix F](#code-23-4).*

The Sharpe ratios this prints are large, and they are large because the only thing in the synthetic market is mean-reverting noise around a correct model. That is the point of the exercise and the reason not to put the number in a pitch book. The useful output is the *shape* the rubber-band box predicted: run it at $\phi = 0.9$ and again at $\phi = 0.99$ and the Sharpe ratio falls by roughly the factor of three that $\sqrt{(1-\phi)/(1+\phi)}$ promises. Kapadia and Pu's weak integration is a statement that real $\phi$ is high and varies by name.

> **Trend Watch.** *Credit got its own volatility surface.* Until recently a credit desk inferred spread volatility from regressions (Section 23.5); now it can read it off a listed index. On October 13, 2023, Cboe launched four Credit VIX indices, VIXIG (CDX North America IG), VIXHY (CDX North America HY), VIXIE (iTraxx Europe Main) and VIXXO (iTraxx Crossover), built from CDX and iTraxx swaption prices using the VIX methodology and co-developed with S&P Dow Jones Indices (Cboe press release, October 3, 2023). The pre-launch back-test shows VIXHY rising from 240.09 to 394.15 between March 2 and March 20, 2023, during the bank failures (hypothetical back-tested data, per Cboe). Volumes followed: cleared CDX swaptions were about \$107bn in Q2 2025, up 103% year on year from \$52.8bn (ION/Clarus analysis of LSEG CCPView data, one scope; approx.), and ICE cleared a record \$19.3bn of index-option notional exercised on April 16, 2025, against a prior record of \$17.7bn on October 18, 2023. *What it means:* the cross-asset trade no longer has to be level against level. The desk can trade implied against implied, equity-surface hazard against CDX swaption vol, and hedge credit vega with an instrument rather than a hope.

## 23.7 Convertible Arbitrage: The Original Cap-Structure Trade

Mags has a word for every strategy that got a Greek letter after she was already doing it. "Back in my day we called it buying the bond and shorting the stock. We sized the short by phone and by grudge. Now it has a gamma." Then, grudgingly: "The gamma is better than the grudge."

The grudge was a particular one *(her story; the issuer goes unnamed and the numbers are illustrative)*. In 1999 she ran a small hedged position in the convertible notes of a paging company whose name she will not say, because it no longer exists. The delta came off a laminated card of hedge ratios her desk head had worked out in 1997 and updated, in pencil, when he remembered. The short stock came from the firm's stock-loan desk, one phone call a morning, at whatever rate the voice on the phone named. One Tuesday a rumor went round that a bigger carrier would buy the company. The stock rose 30% before lunch; the convertible rose 6 points, because the credit was still a paging company's credit. At 11:40 the stock-loan desk called her, which it never did, to say the lender wanted its shares back by Thursday. The lender had heard the same rumor and wanted to sell into it. She bought in 40,000 shares near the high of the week, and a hedged convert became a long convert with no hedge and a hole in it. The rumor was false. The company filed eighteen months later. "So when somebody tells me convert arb is long gamma and short nothing, I tell them about that Thursday. The borrow is a leg. It just isn't on the term sheet." This book's other borrow story, Sal and the bonds, is Chapter 9's; this one was stock, and the recall came on the up day.

> **[SOURCE EXTRACTION]** *Moyer_Distressed_Debt_Analysis p.260:* "The classic example of a capital structure arbitrage is a hedged convertible bond trade. A convertible arbitraguer that arranges a capital structure arbitrage, which is called "putting on the trade," will purchase the convertible bond and then sell short an appropriate amount of stock."
>
> **Annotation.** Moyer is writing from the distressed seat, where the point of the hedge is to "lock in" the coupon with little net capital, because the short-sale proceeds fund much of the convertible. That framing is still correct about the economics and silent about the risk. The modern decomposition is that a hedged convertible is long credit (the bond floor), long equity volatility (the embedded call, which the delta hedge turns into gamma), and short borrow (the stock loan). "An appropriate amount of stock" is the delta, which depends on the hazard, which depends on the stock: the $\lambda(S)$ of Section 23.4. In 2005 the credit leg broke; in 2008 the borrow leg broke as well. A 2026 desk reports the three legs separately and stresses them jointly.

**The P&L of a delta-hedged convertible.** Let $\text{CB}(S, t)$ be the convertible's value with a stock-dependent hazard, $\Delta = \partial\text{CB}/\partial S$ and $\Gamma = \partial^2\text{CB}/\partial S^2$. Over $dt$, long one bond and short $\Delta$ shares earns, before default,

$$
d\Pi \approx \tfrac12\,\Gamma\,S^2\big(\sigma_{\text{real}}^2 - \sigma_{\text{impl}}^2\big)\,dt \;+\; \big(\text{coupon} + \text{short rebate} - \text{borrow fee}\big)\,dt \;-\; \lambda(S)\,\text{JTD}\,dt ,
$$

where JTD is the loss at default net of the stock hedge's gain. The first term is the gamma trade, the second is carry, and the third is why the carry exists. Convert arb loses when realized vol undershoots implied while credit widens (2005), or when the borrow disappears and liquidity goes with it (2008, when emergency short-sale restrictions on financial stocks removed the hedge for part of the market).

> **View From Another Seat.** *The convertible desk and the replicator.* Two systematic seats look at the same convertible and see opposite things, and both have said so in public. The first is the convertible-arbitrage book inside a quantitative firm. A Two Sigma posting for a "Credit Analyst - Convertible Arbitrage" (undated; retrieved from the firm's careers pages in October 2026) describes a strategy that hedges "with equities, equity options, Treasury futures, corporate bonds and credit default swaps," and an analyst who does "fundamental credit analysis on convertible issuers, including capital structure, liquidity, covenants." That is a quant book paying a person to read what the model cannot, Theo's job description in another building, and it is how that seat keeps its idio: the covenant reading is the part no hedge replicates. The second seat is the replicator, who thinks the bond is already a bundle of things that trade more cheaply on their own. Bloomberg reported on 15 May 2019 that a paper by AQR's Roni Israelov found four exposures (government bonds, equities, equity volatility and bond volatility) explain up to 76% of corporate-debt returns, and that a Merton-style replication with futures and options suited investors "who desire enhanced liquidity and cash efficiency"; the same report quoted him that corporate bonds "may be more appropriate in many instances, including for those who want to express a view on individual bonds or desire steady cash flows," and said he would not say whether AQR would use the strategy in its funds (Bloomberg, as republished by WealthManagement.com). Put the two seats side by side and Moyer's trade splits cleanly. The replicator owns Dynkin's short straddle and nothing else, cheaply and liquidly. The convertible desk owns the straddle plus whatever the indenture says, and pays an analyst for the second part. Wolfspeed is a measure of what the second part can be worth.

**Case note: Wolfspeed, 2025, when the convertible is the fulcrum.** Wolfspeed's restructuring support agreement of June 22, 2025 was signed by holders of more than 97% of its senior secured notes, more than 67% of its convertible notes, and Renesas's U.S. subsidiary; the company filed a prepackaged Chapter 11 late in June 2025, targeting roughly \$4.6bn (about 70%) of debt reduction and about a 60% cut in annual cash interest, and the plan was reported effective on September 29, 2025 *(terms as reported; approx.)*. Under the reported terms the convertible holders took new notes and the bulk of the reorganized equity, shared with Renesas. The dated spine runs from 28 March 2025, when an out-of-court exchange failed and the stock fell about 50% to \$2.59, through 2 June, when the company skipped the interest on its 2029 converts and used the 30-day grace period, to the restructuring support agreement of 22–23 June; on 29 June the FY2025 10-K marked the three convertible issues at 26% of principal, inside the plan's own 25–30% recovery estimate. When the plan went effective on 29 September 2025 the new stock opened at \$18.00 and closed at \$22.10, against a plan value of \$22.02 a share (Wolfspeed 8-Ks; FY2025 10-K; closing prices). At \$2.59 the converts' conversion prices of \$47.32 to \$127.22 sat 18 to 49 times spot, so their delta was nil and they traded as recovery claims. For a convert-arb book, that is the trade's endgame inverted: the "bond floor" was not a floor, the convertible *was* the equity of the new company, and the short in the old stock was the profitable leg. The flags a systematic desk would watch in a name like this are the ones this chapter builds: convertibles trading below the straight-debt floor implied by the secured curve (the market pricing them as the fulcrum), a low-strike put floor in (23.8) implying a hazard far above the CDS-free model, and a CreditGrades $z$ that disagrees with the converts' price about how much option value the old equity will keep. We have not reconstructed those series for Wolfspeed; Exercise 5 asks you to.

> **Trend Watch.** *The convertible comeback.* After a lean 2022, the strategy and the market both revived. The HFRX Convertible Arbitrage index returned 10.1% in 2023, global issuance was about \$90bn that year (US about \$57bn), and issuers' effective cost through converts was roughly 3–4% against 7–9% in high yield over 2023–24, with short-sale rebates of 5% or more (Resonanz Capital, "Convertible Arbitrage: The 2023–2025 Comeback," July 10, 2025). Global issuance reached \$167.1bn across 264 deals in 2025, which Numerix called the strongest year on record, and 2026 issuance was reported at about \$131bn in the US through early September, about half from AI-linked issuers *(approx.; secondary reporting)*. *What it means:* the AI capex cycle is financing itself partly by selling volatility to convert-arb funds, so convertible supply is now a driver of single-name implied vol in the issuers' equity surfaces. If you trade those surfaces against CDS, the converts are a third leg you have to model.

## 23.8 When the Surface Lies: Banks, Runs, and Contractual Inversions

Everything so far assumes that default is a firm-value diffusion crossing a barrier, so that the equity surface and the credit curve are two views of one process. The surface lies exactly where that is false. There are three ways it fails, and an ex-RSSG analyst has an edge in all three, because in each one the contract or the run decides who gets paid, not the diffusion. The first is the tape Ines cut at 6:40 on a Thursday morning, and the cold open's cards are still face down in the middle of the desk.

### Case Study B: SVB, March 8–10, 2023

#### Long Scene: SVB, 8–17 March 2023 (replay, continued)

*The cold open's replay, run forward in jumps from 6:40 a.m. on Thursday, March 9, 2023, to Friday, March 17. The Federal Reserve's review, the FDIC's release, SVB Financial Group's filings and the dated events are real and cited; holdco bond prices are press-reported and approximate. The cards, quotes and positions and all dialogue are invented. Mags was on a desk that week and has told the story of her own small purchase elsewhere (Chapter 6). The ritual's rule is that you trade what the tape shows, not what you remember, and she plays it straight.*

*Thursday, to the close.* Ines releases the tape in one jump, to four o'clock. SIVB closes at \$106.04, down 60.4% from Wednesday's \$267.83. The Fed's review would later note that the stock had been "relatively stable" until March 8 "before deteriorating sharply," and that as of March 1 analysts carried 12 Buy, 11 Hold and 1 Sell ratings on it. The holding company's senior notes moved too, but nothing like as far: press reports had the 1.8% notes due 2026 about 115bp wider on the day, at 241bp *(approx.; secondary reports of TRACE prints)*. Same company, same afternoon. The stock said a coin flip on survival; the bonds said a bad week.

Then Ines turns over the part of Thursday that nobody on a trading floor could see, because it was happening inside the bank. In the Federal Reserve's words, "the bank faced a run by depositors on March 9. Deposit outflows were over \$40 billion on March 9, and management expected \$100 billion more" on March 10 (Federal Reserve, April 28, 2023). Kaz reads it twice. "So whoever was buying the puts wasn't pricing a distribution of asset values. They were counting phone calls."

Theo has spent the jump doing the other thing he is good at, which is reading what the notes actually are. The 10-K describes them as obligations of SVB Financial Group, the holding company, and of nothing else. The bank does not guarantee them, and against the bank's assets they stand behind every creditor of the bank: \$173.1 billion of deposits on the consolidated balance sheet and \$15.0 billion of Federal Home Loan Bank advances among them. The following Monday the company's own 8-K would put it in a line: the holding company's debt is "recourse only to the Company and ... not guaranteed by the Company's subsidiaries" (SVBFG 8-K, March 13, 2023). "The stock and the notes are both claims on the holdco," Theo says. "The holdco's big asset is the bank's equity. If the bank goes, both of them lose that. What separates them is whatever's left at the holdco without the bank, and the notes are trading on that." It is why the bonds moved 115bp and the stock moved 60%. Neither market was lying about its own claim.

*Friday.* Ines jumps to Friday morning. The stock is halted before the open. A vendor's pre-market report puts SIVB's 30-day implied volatility at 167, inside a 52-week range of 39 to 280 (Market Rebellion, pre-market IV report, March 10, 2023). Kaz holds it up against the number they backed out of Ines's fills in the cold open, north of 150, and says nothing for a while. By midday the California Department of Financial Protection and Innovation has closed Silicon Valley Bank and appointed the FDIC as receiver; at December 31, 2022 the bank had about \$209.0bn of assets and \$175.4bn of deposits (FDIC press release PR-23-016, March 10, 2023). The bank-level deposit figure is \$2.3 billion larger than the consolidated one in the 10-K, roughly the size of the holding company's own cash at the bank, which consolidation nets out; hold on to that number. By Friday's close press reports put the holdco notes at about 37–42, down from near 90 the week before by one account and from the mid-80s by another *(approx.; reports differ)*.

Before she turns the cards, Ines does what she does at the end of every hand: she prints the markouts. Every put the desk showed her at 6:40 on Thursday, she lifted, and the replay engine marks them to Thursday's close of \$106.04, the last price before the halt *(illustrative marks)*. Every strike the desk sold above that price is deep in the money, and Kaz's ladder, offered all the way up to the volatility Kaz had called absurd, has lost many times its premium. "Who at this table knew more than you?" she asks, and answers it herself. "Not me. I've read the Fed's review. In 2023 I'd guess the informed side was anybody who could see the run from the inside: a treasurer moving a payroll account, a fund telling its companies to move their cash. You can't know who. You can only see the markouts, and the markouts say the person lifting your puts wasn't guessing." Kaz, who sold every one of those puts, writes *who is lifting?* under *which F?* on the bezel.

Ines turns the cold-open cards over.

Kaz's card said the puts were lying: sell the one-month low strikes against the 12bp, small, wrong only "if F is wrong," the sticky note's question copied onto the card. Ines grades it slowly, because it is the most instructive card on the table. CreditGrades was not wrong about a diffusion. It was asked about the wrong entity: debt per share was the holding company's \$56, and the thing that could kill the stock was \$173 billion of bank deposits that the model, as ROBO ran it, treated as if they were equity. The third line, *if F is wrong*, earns the card its only marks, and they are real marks: Kaz named the way they would be wrong before the tape proved it.

Theo's card said the credit curve was lying and the surface was not: buy the puts, small, because nothing on the desk could hedge them, and wrong "if the depositors don't read the footnote." Full marks for the instrument and the sign. Ines docks him for size. He wrote "small" because he could not name a number, and on Friday small paid more than the desk made all month.

Mags's card has one word on it: *Holdco.* Ines reads it out and hands it back. Mags meant it as the answer to the first line. The instrument that was lying was neither the puts nor the notes but the column that put them on one company, and her cold-open line, "Recovery is what you get, eventually, after the FDIC," turns out to be literal. The holding company had about \$2 billion of its own cash on deposit at the bank, the number Theo was told to hold on to, and as of noon on Friday that cash was a claim against a receivership.

The reader's card is graded the same way. If you wrote that the put wing was right and the credit model was asked the wrong question, you have Theo's marks. If you wrote that the puts were rich, you have Kaz's, including the partial credit for naming what would make you wrong.

#### The Monday Card: Holdco Notes in the 40s

Over the weekend the Treasury, the Federal Reserve and the FDIC announced a systemic-risk exception that protected all of the bank's depositors, while making clear that shareholders and certain unsecured debtholders would not be protected (joint statement, March 12, 2023). Ines deals the second card. *Monday, March 13: the holdco notes are offered in the 40s. Do you buy, how much, and what is the recovery made of?*

Mags argues for buying, from the parent company's own balance sheet, which Chapter 6 lays out line by line: cash, a securities portfolio, SVB Capital and SVB Securities, and a pile of claims, against a little over \$3 billion of notes. "The non-bank businesses are real. Somebody will buy them. The 40s pay you for the fight."

Theo has one question, the one Chapter 6's waterfall turns on. "Is the holdco's cash at the bank the holdco's cash?" If it is, the notes are covered at book. If it is a deposit claim against a receivership, the coverage falls to about half, and part of the recovery is a lawsuit against a government agency. He writes *buy, a third of Mags's size; recovery = businesses + cash + a lawsuit we may lose.*

Kaz wants to wait for a model. "There's no CDS to read a curve from. The equity is halted. The only structural input I have is a bank the company no longer owns. Give me a week."

*The tape, to Friday the 17th.* On Monday, press reports put the notes anywhere from about 40 to 47–50 after the depositor guarantee *(approx.; reports differ)*. On Friday, March 17, SVB Financial Group filed for Chapter 11 in the Southern District of New York, and press reports had the notes around 60 by the end of that week *(approx.)*. Six weeks later the 3.50% notes due 2025 traded at 69 and the 1.800% notes due 2031 at 57, one claim at two prices (Debtwire, April 25, 2023, citing MarketAxess).

Ines grades the Monday cards against that tape and against what came after it. Mags bought the right claim at a price that worked. Theo bought less and wrote down the right ingredients: in late August 2026, after a bench trial, a federal court in California ruled that the liquidating trust could not recover its \$1.71 billion claim against the FDIC (as reported by American Banker and by Reuters via PYMNTS; Chapter 6 gives the citations). The lawsuit he priced as a maybe was lost, and the notes he sized for losing it were still worth more than he paid. Kaz's week was the week the notes went from the 40s to about 60; the model would have arrived after the trade. What the twelve-point gap between the 2025s and the 2031s says about reinstatement is Chapter 6's Warm-up A.

<!-- FIGURE (brief §3): ch23_svb_holdco_vs_putwing.png — holdco note prints (near 90 → 37–42 → 40/47–50 → about 60 → 69/57, 6 Mar to 25 Apr 2023, press-reported, approximate) against 30-day implied vol (39–50 → 167) and the stock (\$267.83 → \$106.04 → halt); caption must flag secondary sources. -->

Why was the surface model wrong about SVB, and the put wing right? Kaz puts three reasons on the whiteboard in increasing order of importance, and the desk has kept them in that order. First, the asset vol was wrong: Nagel and Purnanandam (2020, *Review of Financial Studies*) show that bank assets are themselves loans, short puts on borrowers' assets, so the bank's asset payoff is concave and its asset volatility *rises* after bad shocks; constant-volatility structural models "can seriously understate banks' default risk" in good times. Second, the leverage was wrong: for a bank, debt per share is mostly deposits, and ROBO's 12bp came from treating them as equity. Third, and decisively, the default event was wrong. SVB did not fail because $V_t$ crossed $F$; the HTM book was never marked to market before the closure. It failed because liquidity went negative:

$$
\text{default at } \tau = \inf\Big\{t : \text{outflows}_t > \text{cash}_t + \text{monetizable}_t\Big\}, \qquad \text{outflow rate}_t = \kappa\,\max(0, -r^E_t) + \rho\,\frac{D^{u}_0 - D^{u}_t}{D^{u}_0},
$$

where $D^u_t$ is uninsured deposits, $r^E_t$ is the equity return, and the second term is the panic feedback: depositors leave faster when other depositors have left. Equity vol in this model is an *output* of the run, not an input to it. A put surface that "makes no sense unless the stock is going to zero" was the only instrument pricing the run correctly.

Theo's 13-week cash flow model, which has followed him through this book on a USB stick, finally meets its natural habitat. A bank's default model *is* a liquidity runway: sources, uses, and the day the line crosses zero. For SVB the 13 weeks were two days. Figure 23.5, with the routine that draws it in the spec at the end of this section, lays out those two days for a bank loosely of SVB's size.

> **[SOURCE EXTRACTION]** *Bohn_Stein_Active_Credit_Portfolio_Management p.198:* "the assumption that equity prices are only affected by changes in the firm's underlying asset value may lead an analyst astray when the equity price becomes overwhelmed by liquidity or market bubble issues or when the information that informs the prices (e.g., the value of inventories, etc.) is observed imperfectly by market participants."
>
> **Annotation.** Bohn and Stein wrote this about the 1987, 2007, and 2008 sell-offs, and recommended hybrid models that add non-asset-value factors. For banks in 2023 the warning applies in the opposite direction: the equity price was *not* overwhelmed by noise, it was the first market to process a liquidity fact (uninsured, concentrated, networked depositors) that the asset-value model had no state variable for. The modern desk's fix is the hybrid they describe, specialized: for financials, route the name out of CreditGrades entirely and into a liquidity model whose state includes the uninsured share, HTM unrealized losses relative to CET1, the duration gap, and deposit beta, and let the equity surface be a check on that model rather than its input.

> **Docket Diary.** *SVB Financial Group, Chapter 11, filed March 17, 2023 (S.D.N.Y.).* The holding company, no longer owning the bank, filed with \$3,279mm of senior notes outstanding across seven series, and about \$2bn of its cash in accounts at the FDIC's bridge bank, which the FDIC froze; an interim order later gave limited access. Bond prices around 60 cents in the following week said the market expected the holdco's creditors to recover a large fraction of par from cash and non-bank businesses, not from the bank. The Ad Hoc Group, represented by counsel, would like to note for the record that it would like its \$2bn back.

One seat watched the same week without looking at the surface at all.

> **View From Another Seat.** *The opportunistic buyer of a holdco.* For the long-horizon credit investor, the useful sentence about that March came a month later, from Howard Marks of Oaktree: "The bottom line is that banks are, essentially, highly levered fixed income investors" (Marks, "Lessons from Silicon Valley Bank," Oaktree Capital memo, April 17, 2023). Read through this chapter, the sentence is a statement about the surface. The equity of a highly levered fixed-income investor is a thin call on a bond portfolio funded by money that can leave on a phone call, so its implied volatility measures interest rates and depositor nerves at once, and was never going to be a clean read of asset risk. The opportunistic seat does not try to read it. Press reports that week had distressed buyers paying around 30 cents for some of the holdco paper, and Debtwire, citing the *Wall Street Journal*, later named Centerbridge, Davidson Kempner and PIMCO among the holders who organized as a creditor group (Debtwire, April 26, 2023); what any of them concluded is not on the public record and is not guessed at here. The seat's question is one the surface cannot answer: how good is the inter-company claim, the holding company's deposit at its own failed bank? That is a question about a receivership, a set-off and a court, and it is where the holdco's recovery lived. Chapter 6's box sets the same notes between a distressed fund and a dealer desk; this one adds only the reason the fund could ignore the equity market.

### Case Study C: Credit Suisse AT1, March 19, 2023

*A second replay, dealt the same afternoon and cut at the close of Friday, March 17, 2023. FINMA's and UBS's releases are real and cited; the deck's AT1 mark, the proposed pair and all dialogue are invented and illustrative.*

Credit Suisse has spent the week in the headlines. Ines's deck shows one of its additional tier 1 bonds at 40 *(illustrative)* and the shares still trading at a positive price, and Kaz sees a pair before she has finished dealing. "Long the AT1 at 40, short the equity. AT1 is senior to equity. If the bank fails, the equity goes to zero before the AT1 loses a franc. If it survives, the AT1 is cheap. Hedge the bank, keep the seniority." Kaz drafts it in the Pair Book's format: hedge, the equity; idio, the gap between the price of the senior claim and the price of the junior one.

Theo asks for the prospectus, then for one clause in it: the write-down terms. He reads them out. The notes can be written down in full on a viability event, a determination made by the regulator rather than by a court, and the grant of extraordinary government support to the bank is one of the ways that event can happen. "Where does that sit in the waterfall?" Kaz asks.

"It doesn't. It sits in front of the waterfall. Seniority is what happens in a liquidation. This is what happens on a weekend so that there isn't one."

Kaz reads the clause over Theo's shoulder and asks the question the Desk Myth box below records. Mags, who has seen senior paper behave badly before, puts it more simply. "If someone in a government building can zero your bond while the stock gets bought, your bond isn't senior. It's an option the government holds. Don't do the trade." The desk declines, and Ines writes the declined pair into the ledger anyway, because the Pair Book keeps a line for the trades it refused: hedge, the equity; idio, none the desk could own; leak, the whole position, because a legal clause could invert the legs before any price moved.

Then she turns over Sunday. On March 19, 2023, FINMA ordered "a complete write-down of the nominal value of all AT1 debt of Credit Suisse in the amount of around CHF 16 billion," triggered by extraordinary government support, as UBS agreed to acquire the bank (FINMA press release, March 19, 2023). Shareholders received 1 UBS share per 22.48 Credit Suisse shares, CHF 0.76 per share, "a total consideration of CHF 3 billion" (UBS media release, March 19, 2023). A claim senior to equity received zero while equity received CHF 3bn. Kaz's pair would have lost its whole long and earned back only what a short earns when a stock is bought at a discount rather than written off. No Merton diagram, no CreditGrades barrier, and no Carr–Wu corridor produces that outcome, because all of them assume the waterfall is ordered by priority. The contract had a viability trigger, and the trigger reordered the waterfall.

<!-- FIGURE (brief §3): ch23_cs_at1_waterfall_inversion.png — liquidation priority (AT1 above equity) beside the 19 Mar 2023 outcome (AT1 about CHF 16bn written to zero; shareholders about CHF 3bn in UBS shares, 1 UBS share per 22.48 CS shares). Pending U4. -->

> **Desk Myth vs. Desk Reality.** *Myth:* AT1 is senior to equity, so an AT1 trading below the equity-implied recovery is an arbitrage. *Reality:* AT1 is senior to equity in liquidation. Before liquidation, its write-down clause lets a regulator's viability determination zero it while the equity is sold for consideration. Kaz, reading the prospectus, asked whether "point of non-viability" was a topology term. It is a legal one, and it is a strike the regulator sets.

### Case Study D: Hertz, 2020–21, the Happy Inversion

Hertz filed for Chapter 11 on May 22, 2020, with an equity that every model said was worthless; in June 2020 it announced, and then shelved, a \$500mm at-the-money stock offering into a market that kept bidding for its shares. Used-car prices and a bidding war among plan sponsors then raised the value of the estate. The plan, confirmed June 10, 2021 and effective June 30, 2021, repaid the unsecured notes in full in cash, and gave existing shareholders 14,133,075 shares of new common, about 3% of 471,102,514, plus, for those not in the rights offering, 89,049,029 warrants exercisable until June 30, 2051 at an initial \$13.80 (Hertz Form 8-K filed July 7, 2021); secondary reporting adds about \$239mm of cash to old equity *(approx.)*. The sponsors (Knighthead, Certares, Apollo) put in \$2.781bn of new common, \$1.5bn of Apollo preferred, and a \$1.635bn backstopped rights offering. The equity was a call on enterprise value that finished in the money. The surface that priced Hertz equity above zero in bankruptcy was not irrational; it was long volatility on an estate whose value distribution had a fat right tail. Mags's verdict: "Recovery is what you get, eventually, after the lawyers. Sometimes the lawyers are on your side."

> **View From Another Seat.** *The plan sponsor.* One seat in the Hertz case was long the right tail on purpose, and its instrument was a plan, not a listed option. Hertz's announcement of its emergence, filed as Exhibit 99.1 to a Form 8-K, said that Knighthead, Certares and Apollo-affiliated funds had committed "over \$5.9 billion of new equity capital," and that Hertz had paid "nearly \$19 billion of creditors in full." A sponsor in that seat is not buying a claim the surface prices. It is buying what the estate is worth after every creditor has been paid, at a strike the plan documents set and a price the bidding war set, which is the same right tail the listed equity was pricing in bankruptcy, bought through a different door. The \$2.781bn of common, the \$1.5bn of preferred and the \$1.635bn backstopped rights offering above are what the sponsors paid for that call. As the documents show it, Apollo's role was as a sponsor and preferred investor in a solvent estate, not as a creditor (Chapter 16 has the sequence). The filings record what the sponsors did; nothing here reports what they thought. For the cross-asset desk the lesson is the mirror image of SVB's: there the surface priced a left tail the credit model could not see, and here it priced a right tail that belonged, by the end, to the people who wrote the plan.

### Specification for AI Implementation (continued): the bank override

**Rule.** Any issuer with deposits above 50% of liabilities, or any instrument with a contractual write-down or conversion trigger, is routed out of the CreditGrades engine. Banks go to a liquidity-runway model; trigger instruments carry a `contractual_waterfall_override = True` flag, and the risk system refuses to net them against equity as if priority held. The code is purely illustrative: inputs are round numbers loosely scaled to a \$200bn bank, not SVB's balance sheet.

The default clock above is a definition, and a definition is not a number a risk system can use. The desk needs to know, for each deposit-funded name in the book, on which day the line crosses zero under a stressed equity path, and it needs to know it every morning, because the answer changes with the stock. This is the one place in the book where the restructuring banker's habit is the right tool: a cash runway, sources against uses, day by day. SVB's version of Theo's 13-week model had two days in it. The routine that follows is that model with a feedback term and a for-loop, and its job is to sit next to the Merton number and disagree with it loudly.

The function keeps three stocks: liquid cash, a pool of securities, and the uninsured deposits that can leave. Each day it does four things in a fixed order. It sets a run rate: `kappa` times the day's equity loss (nothing if the stock is up), plus `rho` times the share of uninsured deposits already gone, which is the panic feedback, capped at 100%. It multiplies that rate by the uninsured deposits still there to get the day's outflow. It sells securities, raising the lesser of what the pool fetches after the `haircut` and `max_monetize_per_day`, and adds the proceeds to liquidity. Then it tests: if the day's outflow exceeds the liquidity on hand, the bank defaults that day and the function returns the day and the path; otherwise it pays the outflow and carries the rest forward. If the equity returns run out first, the default day is `None`.

The example is a bank loosely scaled to \$200bn: \$13bn of cash, \$115bn of securities, a 10% haircut, \$30bn a day of selling capacity, \$165bn of uninsured deposits, and equity returns of $-60\%$, $-30\%$ and $-10\%$. On day one the outflow is about \$42bn against \$43bn of liquidity, and the bank survives with \$1.4bn. On day two the panic term pushes the run rate above 60% of what is left, about \$78bn goes out against \$31bn of liquidity, and the bank defaults. The Merton one-year default probability for the same balance sheet, at 4% asset volatility, is under 1%, because Merton is asking whether assets fall below debt, and nobody in this story was waiting for that. Figure 23.5 lays out the two days.

![Figure 23.5: A bank with \$13bn of cash, \$115bn of securities and \$165bn of uninsured deposits survives day 1 with \$1.4bn but fails on day 2, when the run rate jumps from 25% to 63%, although a Merton model for the same balance sheet puts the one-year default probability at 0.4%. Illustrative: the runway routine of this section with run parameters kappa 0.42 and rho 2.0, a 10% haircut, \$30bn a day of securities sales and equity returns of −60%, −30% and −10%; the Merton comparison uses assets of \$212bn, debt of \$196bn and asset volatility 4%.](assets/figures/ch23_bank_run_runway.png)

Use it to route and stress deposit-funded names, running many equity paths and a grid of `kappa` and `rho` to turn a scenario into a distribution. Do not read the default day as a forecast, and do not calibrate `kappa` and `rho` to one event; they are illustrative.

The edge case that bites is the haircut. It is one number applied to one pool for every day of the run, so the model sells securities at the same discount on day two as on day zero. In a real run the discount widens exactly when you need to sell, and the unrealized losses on a held-to-maturity book live entirely in that parameter. Stress it, or the function flatters the bank.

*The full listing is [Listing 23.5 in Appendix F](#code-23-5).*

## 23.9 Cross-Asset Trend: Does the Surface Lead the Spread?

SVB's put wing and Hertz's bankrupt equity had one thing in common: the option market moved first and the credit market caught up later. Most months the gap is smaller and duller, weeks rather than a weekend, and the duller version is a signal a systematic desk can run on every name. The last use of the surface is as a clock. If equity and credit are two strikes on one distribution but different investors trade them at different speeds, the faster market leads. The evidence says equity usually does: Dynkin's team finds that each +1% per month of sector equity momentum predicts about +5–8bp of subsequent bond excess return, stronger in US high yield (Dynkin_Systematic_Investing_in_Credit p.644). The specification is a panel lead–lag regression,

$$
r^{\text{xs}}_{i,t+1} = a + b\,r^{E}_{i,t} + c\,\Delta\sigma^{\text{impl}}_{i,t} + d\,\Delta\widehat{\lambda}^{\text{put}}_{i,t} + \epsilon_{i,t+1},
$$

where $r^{\text{xs}}$ is bond excess return over duration-matched Treasuries, $r^E$ the equity return, $\Delta\sigma^{\text{impl}}$ the change in implied vol, and $\Delta\widehat\lambda^{\text{put}}$ the change in the put-floor hazard from (23.8). The regression asks only whether this month's equity news helps predict next month's bond return; when its windows overlap, neighbouring observations share most of their data and ordinary standard errors flatter the answer, which is the problem Chapter 10's overlapping-window corrections solve, and the left side uses Chapter 8's IDO residuals because without them the regression rediscovers beta.

> **[SOURCE EXTRACTION]** *Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.25:* "equity performance often has a spillover into bond pricing."
>
> **Annotation.** Man's framing is the practical one: equity momentum in credit (the EMC factor of Ben Dor and co-authors, 2021) is a factor you can harvest because bond investors update slowly. The cross-asset surface sharpens it. Equity returns tell you the stock moved; the change in the put floor tells you whether the move was about the *tail*. A 10% stock drop with no change in the low-strike wing is a valuation event; a 10% drop with the wing doubling is a credit event that the bond market has not priced yet.

> **Trend Watch.** *Equity first, high yield second, private marks last (early 2026).* iCapital's February 6, 2026 *Market Pulse* dates the trigger to an AI product rollout by Anthropic on January 30, 2026: software stocks fell about 10% after it and were about 20% down year to date as of February 4, "the worst start to the year in history," with no software index member above its 200-day moving average. In credit, software high-yield spreads were about 400bp and technology about 340bp (iBoxx, February 4, 2026), against 264bp for broad high yield; software was about 20% of public BDC loans (LSEG/Bloomberg, September 30, 2025), and no loan-mark changes had been reported. *What it means:* this is the lead–lag in three speeds. Public equity repriced in days, public high yield in weeks, and private marks had not moved. For the desk, equity and put-surface signals are the earliest read on private-credit marks (Chapter 17), and the gap between them is a forecast of the next round of valuations.

## 23.10 Desk Debrief

The finder below lists each tool in the chapter with the place it is derived, the box that builds the intuition, the scene where somebody had to decide whether to trust it, and the listing that computes it. Read across a row and you have the chapter's promise for that tool: translate an equity price and volatility into a spread and back, turn a put spread into a default claim, read a hazard off the skew, put Greeks in spread units, run Yu's convergence trade knowing why single trades lose, and say why the surface broke in May 2005, March 2023 and the 2025–26 cycle.

| Concept | Equation | Intuition (box) | Judgment (scene) | Code |
| :-- | :-- | :-- | :-- | :-- |
| The capital structure as call spreads on one risk-neutral distribution; equity vol as leveraged asset vol | Payoff$_k$, (23.1)–(23.2) | The bookmaker's odds; why a wobble pays a curved claim (§23.1) | Sliding the assets down the table: a vol-targeting overlay "reads leverage as risk appetite" (§23.1) | [Listing 23.1](#code-23-1) |
| CreditGrades: from a stock to a CDS spread, and a CDS quote back to an implied vol | (23.3)–(23.5) | The drunk, the lamppost and the gutter (§23.2) | Which vol, which horizon, which debt: debt per share comes from the balance sheet, the barrier comes from the indenture (§23.2); ROBO's 12bp (cold open) | [Listing 23.1](#code-23-1) |
| Carr–Wu: a put spread inside the corridor is a unit recovery claim | (23.6)–(23.7) | Two tickets and no model (§23.3) | Ines's \$7.50/\$2.50 hand history (§23.3) | [Listing 23.2](#code-23-2) |
| The low-strike floor is the hazard | (23.8) | The Poisson clock and the compensating drift (§23.4) | Kaz prices the \$5 put twice; Dana's four days of `floor_ratio` (§23.4) | [Listing 23.2](#code-23-2) |
| Greeks in spread terms, the equity hedge ratio, and JTD | (23.9)–(23.10) | The slope under your feet (§23.5) | Theo's whiteboard and Mags's forty-recovery day: the stock hedges delta, nothing done with the stock hedges the jump (§23.5) | [Listing 23.3](#code-23-3) |
| Capital-structure arbitrage: the $z$-rule and its P&L decomposition | (23.11) | (the decomposition in §23.6) | Long Scene: GM, 3–5 May 2005, and the GM card; PB-04 closed (§23.6) | [Listing 23.4](#code-23-4) |
| Persistence: half-life, Sharpe decay and the 180-day stop | $\sqrt{(1-\phi)/(1+\phi)}$ (§23.6) | A stretched rubber band (§23.6) | Carvana, PB-05: a delta band that lost every quarter of 2023 (§23.6) | [Listing 23.4](#code-23-4) |
| Convertible arbitrage: the delta-hedged convertible | $d\Pi$ (§23.7) | (Moyer's extraction and its annotation, §23.7) | Mags's 1999 recall; the convert desk and the replicator; Wolfspeed, 2025 (§23.7) | — |
| Banks: the liquidity runway instead of the barrier | Runway equation (§23.8) | Theo's 13-week model meets its habitat (§23.8) | Long Scene: SVB, 8–17 March 2023, and the Monday card; Credit Suisse AT1, the declined pair; Hertz and the plan sponsor (§23.8) | [Listing 23.5](#code-23-5) |
| Does the surface lead the spread? | Lead–lag regression (§23.9) | (Chapter 10 owns overlapping windows) | Equity first, high yield second, private marks last (§23.9) | — |

- **The capital structure is one distribution sliced at different strikes.** Equity is the call, bonds are short puts, CDS is the put without rates, and a low-strike equity put is a CDS that forgot to tell anyone.
- **Equity vol is leveraged asset vol** ($\sigma_E E = \sigma_V V N(d_1)$). Cheap stocks are mechanically high-vol stocks, the skew is built in, and plugging $\sigma_E$ in for $\sigma_V$ overstates default risk by the leverage.
- **CreditGrades is the production bridge**, with honest warts: the time-zero ghost, a reported error in the published closed form, two different recoveries, and $\nu$ fitted on non-financials. Integrate the legs yourself and test against Monte Carlo.
- **A put spread inside the default corridor is a model-free default claim** (Carr–Wu). Match the payment convention (American pays at default, European at expiry) before you trade the basis against CDS.
- **The low-strike floor $P(K)/K$ is the hazard.** Jumps make it flatten to a constant; stochastic vol sends it to zero. Diagnose with prices, not implied vols.
- **Hedge ratios are the part of Merton that works.** Cap-structure arbitrage bets the ratio is right and the price is wrong; single trades lose, portfolios earn. Strip carry, simulate defaults, and stress the May 2005 vector (stock up, spread up).
- **The surface breaks where the process is not a diffusion:** runs (SVB), contractual triggers (Credit Suisse AT1), and estates whose value tail was fatter than anyone modeled (Hertz). The credit agreement, the prospectus, and the deposit base decide those cases, and reading them is the ex-RSSG analyst's edge.

**The Spec You Hand the Robot.** Build `ch23_cross_asset_surface`, numpy/scipy/pandas only, seeded RNG (`seed=23`), no network. (1) `cg_survival`, `cg_cds_spread`, `cg_implied_vol` per (23.3)–(23.5), with the leg integration monthly, the time-zero mass in the protection leg, `nan` outside the inversion range, and a Monte Carlo check with a Brownian-bridge correction. (2) `urc_from_puts` per (23.6), returning bid and ask bounds and a payment `convention`, and `urc_from_cds` per (23.7) with a matching `payment` argument; raise on convention mismatch. (3) `jtd_put_price` and `jtd_fit` per (23.8), fitting $(\sigma, \lambda)$ jointly on $P(K)/K$, with borrow backed out of at-the-money parity first and the `floor_ratio` diagnostic. (4) `spread_greeks` (CS01, convexity, DTS) and `cg_greeks` (shares per \$10mm, stock-space gamma, equity and asset vega), plus JTD per notional reported as its own line. (5) `capstruct_backtest` with Yu's rules, carry reported separately from convergence, defaults simulated at the CDS-implied hazard in production runs, and an event-sign stress (stock +20%, spread +30%). (6) A router that sends any issuer with deposits above 50% of liabilities to `bank_run_dd`, and flags any instrument with a contractual write-down trigger as `contractual_waterfall_override`. Inputs in decimals and years; outputs in bp, \$, and shares, with units in every column name. Every function raises on non-positive prices, vols, or debt.

### Exercises

1. **ROBO targets volatility.** ROBO is told to "keep each position at 10% annualized vol" and holds a stock whose asset vol is constant at 25%. Using (23.1) and the table in Section 23.1, compute how much ROBO sells as assets fall from 150 to 75. Explain in one sentence to the risk committee why the strategy is short the fulcrum.
2. **Chase the ghost.** Simulate the *true* CreditGrades model, a lognormal against a barrier drawn once at $t = 0$, and compare its $1 - \mathcal{S}(0)$ and 1- and 5-year spreads with (23.3) for $S_0 \in \{5, 30\}$, $\sigma_E = 40\%$, $F^{\text{ps}} = 30$. At what stock price does the time-shift approximation move the 1-year spread by more than 50bp?
3. **Trade the basis.** Given a European put chain generated by `jtd_put_price` with $\lambda = 6\%$ and a CDS quote of 250bp at 40% recovery, compute $\text{basis}_U$ in claim units and in bp, size a default-neutral put-spread-versus-CDS trade for \$10mm CDS notional, and explain what happens to it if the stock drifts slowly into the corridor, GM-style, instead of jumping through it.
4. **Kaz and the prospectus.** Kaz argues that an AT1 trading at 40 while the equity trades at a positive price is an arbitrage "because seniority." Write the `contractual_waterfall_override` logic, list the three prospectus fields it must parse, and show what CreditGrades would have said about Credit Suisse AT1 recovery on March 17, 2023 (use illustrative inputs and say so).
5. **Both legs, again.** Build a book that is long \$10mm of a convertible (approximated as a 5-year bond plus calls) and short delta in stock, plus \$10mm of sold CDS protection hedged with stock, on a \$30 name. Apply the May 2005 vector, stock +18% then spread +30%, using the block 3 Greeks, and decompose the loss by leg. Then reconstruct the convertible-floor, put-floor, and $z$ series a desk would have watched for Wolfspeed in the first half of 2025 from public data, and say which flag fired first.
6. **Three speeds.** Using the iCapital February 2026 figures, estimate the high-yield spread move per 10% of software equity drawdown, then state the private-mark markdown your lead–lag model would forecast for a software loan book at 97.8% of par, and the one assumption that would make your forecast wrong.

### Deep-Dive Resource Graph

**Podcasts**

- **Dan Davies On What Brought Down Silicon Valley Bank** (*Odd Lots*, Joe Weisenthal and Tracy Alloway with Dan Davies, March 14, 2023). Recorded within days of the run: why the bank's customer base "turned out to be so much more flighty than expected" and why it reached for yield, the setting for the contractual inversion in Case Study B (§23.8). https://omny.fm/shows/odd-lots/dan-davies-on-what-brought-down-silicon-valley-ban
- **The Regulatory Blunder That Gave Us the Silicon Valley Bank Disaster** (*Odd Lots*, with Lev Menand of Columbia Law, March 16, 2023). Menand on "the defanging of bank supervisors" in the run-up; pair it with Davies, one explains the depositors and the other the supervisors (Case Study B, §23.8). https://omny.fm/shows/odd-lots/the-regulatory-blunder-that-gave-us-the-silicon-va
- **Swiss AT1 Bond Carnage, Leisure Sector Risk** (*The Credit Edge*, Bloomberg Intelligence, March 23, 2023). Four days after the March 19 UBS takeover, which per the episode page "included pulling the pin on $17 billion" of AT1 CoCo bonds: a real-time account of the contractual inversion in Case Study C (§23.8). https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/swiss-at1-bond-carnage-leisure-sector-risk
- **Dean Curnutt - The Reflexivity of Equity Volatility (S6E16)** (*Flirting with Models*, Corey Hoffstein with Dean Curnutt of Macro Risk Advisors, September 11, 2023). Endogenous risk, reflexivity, crowding and options on variance across 1987, LTCM, 2008 and the XIV implosion; a second voice on the vol-targeting feedback loop of §23.1 and Exercise 1. https://www.flirtingwithmodels.com/episodes/l8s5fwO9IGb
- **Kris Abdelmessih - Life Through a Volatility Lens (S7E10)** (*Flirting with Models*, Corey Hoffstein with Kris Abdelmessih, July 29, 2024). A former option-pit market maker who later ran a relative-value volatility book, on reading trades through payoffs and optionality; the options-desk view behind the put-surface fit (§23.4) and the spread Greeks (§23.5). https://www.flirtingwithmodels.com/episodes/EdhZsWMO5mh
- No verified episode on convertible arbitrage or on capital-structure arbitrage was found for this chapter, so none is listed; Sections 23.6 and 23.7 rest on the papers below.

**Talks and Reports**

- **Applications of Option-Pricing Theory: Twenty-Five Years Later** (Robert C. Merton, Nobel Prize Lecture, December 9, 1997). The author of the structural model on what option-pricing theory had been applied to over twenty-five years; the primary-source opener for §23.1. https://www.nobelprize.org/prizes/economic-sciences/1997/merton/lecture/
- **Initial Findings from Independent Review of Silicon Valley Bank** (Michelle W. Bowman, Federal Reserve Vice Chair for Supervision, September 18, 2026). Announces the first report of an independent review by Starling Advisory Group (seven findings, the first in a series) and frames the failure as having spread to Signature and First Republic; the newest primary source for Case Study B (§23.8), so read the report itself before quoting findings. https://www.federalreserve.gov/newsevents/speech/bowman20260918b.htm
- **Report on the 2023 banking turmoil** (Basel Committee on Banking Supervision, October 5, 2023). The supervisors' assessment of causes, responses and initial lessons for SVB and Credit Suisse alike; the reference to cite beside both §23.8 case studies. https://www.bis.org/publications/report-2023-banking-turmoil

**Practitioner Writing**

- Matt Levine, *Money Stuff* (Bloomberg Opinion): the March 2023 columns on SVB's deposit run and on the Credit Suisse AT1 write-down, and his recurring explanations of capital-structure seniority. No specific column is cited here: none is in the verified-item dossier for this chapter, and Bloomberg pages could not be fetched to confirm a title and date.
- BIS *Quarterly Review*, June 2005, the overview and the box on the GM and Ford downgrades and CDS index tranches (pp.4–6).
- Board of Governors of the Federal Reserve System, *Review of the Federal Reserve's Supervision and Regulation of Silicon Valley Bank* (April 28, 2023). Root: https://www.federalreserve.gov
- FDIC press releases PR-23-016 (March 10, 2023, SVB) and PR-23-034 (May 1, 2023, First Republic). Root: https://www.fdic.gov
- FINMA press release and UBS media release, March 19, 2023, on Credit Suisse.
- Cboe press release, October 3, 2023, on the Credit VIX indices.
- Resonanz Capital, "Convertible Arbitrage: The 2023–2025 Comeback" (July 10, 2025); iCapital, "Market Pulse: Surveying the Software Space" (February 6, 2026).
- Finger, C. C. (ed.), V. Finkelstein, J.-P. Lardy, G. Pan, T. Ta, and J. Tierney (2002), *CreditGrades Technical Document*, RiskMetrics Group (hosted by MSCI).

**Academic Papers**

- Carr, P., and L. Wu (2011), "A Simple Robust Link Between American Puts and Credit Protection," *Review of Financial Studies* 24(2), 473–505. DOI 10.1093/rfs/hhq129.
- Carr, P., and L. Wu (2010), "Stock Options and Credit Default Swaps: A Joint Framework for Valuation and Estimation," *Journal of Financial Econometrics* 8(4), 409–449. DOI 10.1093/jjfinec/nbp010.
- Cruz López, J., and A. Ibáñez (2021), "European Puts, Credit Protection, and Endogenous Default," *Quarterly Journal of Finance* 11(1). DOI 10.1142/S2010139221500014.
- Yu, F. (2006), "How Profitable Is Capital Structure Arbitrage?" *Financial Analysts Journal* 62(5), 47–62. DOI 10.2469/faj.v62.n5.4282.
- Kapadia, N., and X. Pu (2012), "Limited Arbitrage between Equity and Credit Markets," *Journal of Financial Economics* 105(3), 542–564. DOI 10.1016/j.jfineco.2011.10.014.
- Duarte, J., F. A. Longstaff, and F. Yu (2007), "Risk and Return in Fixed-Income Arbitrage: Nickels in Front of a Steamroller?" *Review of Financial Studies* 20(3), 769–811. DOI 10.1093/rfs/hhl026.
- Schaefer, S. M., and I. A. Strebulaev (2008), "Structural Models of Credit Risk Are Useful: Evidence from Hedge Ratios on Corporate Bonds," *Journal of Financial Economics* 90(1), 1–19.
- Zhang, B. Y., H. Zhou, and H. Zhu (2009), "Explaining Credit Default Swap Spreads with the Equity Volatility and Jump Risks of Individual Firms," *Review of Financial Studies* 22(12), 5099–5131. DOI 10.1093/rfs/hhp004.
- Cremers, M., J. Driessen, P. Maenhout, and D. Weinbaum (2008), "Individual Stock-Option Prices and Credit Spreads," *Journal of Banking & Finance* 32(12), 2706–2715.
- Culp, C. L., Y. Nozawa, and P. Veronesi (2018), "Option-Based Credit Spreads," *American Economic Review* 108(2), 454–488. DOI 10.1257/aer.20151606.
- Nagel, S., and A. Purnanandam (2020), "Banks' Risk Dynamics and Distance to Default," *Review of Financial Studies* 33(6), 2421–2467. DOI 10.1093/rfs/hhz125.
- Collin-Dufresne, P., R. S. Goldstein, and F. Yang (2012), "On the Relative Pricing of Long-Maturity Index Options and Collateralized Debt Obligations," *Journal of Finance* 67(6), 1983–2014. DOI 10.1111/j.1540-6261.2012.01779.x.
- Linetsky, V. (2006), on pricing equity derivatives subject to bankruptcy in a CEV-with-default model; Andersen, L., and D. Buffum (2003), on calibrating and implementing convertible-bond models with stock-dependent hazard (titles not verified here).

**Data & Code**

- SEC EDGAR (Schedule 14D-9 and 13D filings for tender offers and activist stakes; Form 8-K for plan effectiveness): https://www.sec.gov/edgar
- CourtListener REST API, for Chapter 11 dockets such as SVB Financial Group (S.D.N.Y., 2023): https://www.courtlistener.com/help/api/
- FINRA TRACE, for corporate bond prints (price paths in Case Study B).
- OPRA consolidated options data, for listed put chains (the `OptionChain` schema).
- DTCC and clearing-house public CDS volume reports, and Cboe's Credit VIX index data, for the credit vol surface.
- Shelf cross-references: Dynkin_Systematic_Investing_in_Credit pp.87–88, 93, 644; Bohn_Stein_Active_Credit_Portfolio_Management pp.169, 198; Ben_Dor_Quantitative_Credit_Portfolio_Management p.70; Schmid_Credit_Risk_Pricing_Models p.154; Moyer_Distressed_Debt_Analysis p.260; Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.25.

<!-- STATUS: COMPLETE -->
