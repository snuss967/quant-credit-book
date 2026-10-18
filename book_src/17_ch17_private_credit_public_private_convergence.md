# Chapter 17: Private Credit & the Public–Private Convergence

> *"Middle market direct lending (Private Credit): Proxy Index using S&P UBS Leveraged Loan B Index."* (Nuveen_Multi_Asset_Credit_Quant_Framework p.9)
>
> And, two pages earlier in the same framework's sector table, in the volatility column for middle-market direct lending: "N/A". (Nuveen_Multi_Asset_Credit_Quant_Framework p.2)

## Cold Open: Volatility N/A

*(A replay. The desk, its dialogue, the listed BDC, its notes and the \$25mm RFQ are fictional, and every price the desk sees on its own screens is illustrative. The fund in the headline and its numbers are real: InvestmentNews, June 23, 2026.)*

The desk keeps a folder called "Replays": real credit events cut off at a minute, with nothing inside that was not public by then. Ines runs one on a Friday afternoon every few weeks, and the rule never changes: nobody mentions anything that happened after the cut-off. This Friday in October, the week the Fed finally put private credit into its Financial Accounts, the folder on the big screen is labeled *Tuesday 23 June 2026, 2:40 p.m.* Mags and Kaz were on the desk that day. Theo was at RSSG, where the same headline arrived as somebody else's problem and stayed that way until dinner.

Ines starts the clock.

**2:40 p.m.** The headline crosses the news screen in the clipped grammar of a wire: Apollo Debt Solutions, a \$26 billion non-traded private credit fund, has received repurchase requests for 16.8% of its shares this quarter, about \$2.4 billion, and will pay 5%, which the story calls "the standard limit for such vehicles." Two other sponsors' funds appear further down the piece; the desk will get to them in §17.6.

Kaz reads it twice, the way Kaz reads anything with a percentage in it, and shrugs. "That's their fund. It isn't our bond. Their investors want out of a vehicle that only lets five in a hundred leave each quarter. Our bonds don't have investors who want out. They have a price."

It is a reasonable sentence, and Mags lets it sit on the desk for a while, the way you let a junior's bid sit on a screen to see who hits it.

**3:05 p.m.** The desk makes markets in the unsecured notes of a listed BDC that lends to the same kind of borrower as the fund in the headline: sponsor-backed, middle-market, heavy in software. The run sheet shows the 2029 notes quoted where they were at lunch, because nothing has printed since. The BDC's shares are down a little more than 2% since the headline, which is the only price anywhere on the screen that has moved.

Theo opens the BDC's last 10-Q, skips everything a normal person would read, and goes looking for the credit agreement behind the revolver, which the 10-Q mentions in two sentences and files as an exhibit to a different document. It takes him twenty minutes to find the definition of the borrowing base, and another ten to find the paragraph that matters, which is about what the bank will lend against and what it will not. Loans on non-accrual drop out. Loans that have been amended to pay in kind, interest that accrues as more debt instead of arriving as cash, are "Eligible Investments" only at a haircut, and the haircut gets worse the longer the PIK runs.

He reads it out loud, which is what he does when he finds the paragraph that matters. "What does the revolver say about borrowing-base eligibility for PIK loans? If the bank haircuts anything that's been amended into PIK, and a fifth of the book is software that's been amended into PIK, then the borrowing base shrinks exactly when the fund needs it. And these notes sit behind that line."

Nobody answers, because the question is a good one and the 10-Q does not say how much of the book is PIK by amendment rather than by design. Theo writes a sticky note and puts it under the one from Chapter 4 (*"price" = as of when, in what size, from whom?*): *whose number is it?*

**4:10 p.m.** Kaz has pulled the BDC's NAV history and the history of a loan index beside it, and is quietly pleased with the first chart and quietly annoyed with the second, because the second one moves.

**4:40 p.m.** The RFQ arrives: a client wants to sell \$25mm of the BDC's senior unsecured notes due 2029, two hours after the headline, twenty minutes before the close, from an account the desk sees about once a quarter.

Kaz has the NAV chart up. "I don't see the problem. NAV per share has moved less than one percent all quarter. I tried to pull the volatility of the loan book and the vendor field says N/A."

"N/A isn't zero," Ines says. "N/A means nobody looked. What's the pot, what are the odds, and who at this table knows more than we do? Somebody wants out of the bond of a vehicle that owns the same kind of loans as the fund that just got a run. They want out at 4:40 today, not at 9:30 tomorrow. That's the hand."

"In my day," Mags says without looking up, "we called a bond with no price a bond. You found out what it was worth when you tried to sell it. Then you found out who else was trying."

"Are you saying the NAV is wrong?" Kaz asks.

"I'm saying the NAV is a mark," Theo says. "It's marked quarterly, by the manager, who earns fees on it. The bond price is a price. Underneath, it's the same loans."

Ines nods at the screen. "Then the question isn't what the bond is worth. It's what the loans are worth, and which of the things we *can* trade already knows."

She stops the clock there, at 4:41, with the RFQ still blinking, and hands out index cards, because a replay is worthless if people get to answer after they have heard each other. "Write three things: what you bid, how much of the \$25mm, and which public thing you'd hedge it with. Then put the card face down. We turn them over at the end of the chapter."

Kaz writes quickly. Mags writes one line and folds the card. Theo looks at his sticky note for longer than he looks at his card, which is, Ines notes without saying so, the right order.

Four prices will be attached to the same loans before this chapter is done: the manager's NAV, the listed sibling's share price, a pension fund's bid at par, and a secondary buyer's bid for a fund's units at two-thirds of NAV. Each is honest about a different question, which is why Theo's sticky note is the right one.

The question this chapter answers: **what are the true value and risk of a portfolio whose only published price is set by its owner, and which public instruments let us trade our answer?**

By the end of this chapter you will be able to: write a private mark as a moving-average filter of an unobserved return and derive what that filter does to volatility, correlation, beta and Sharpe ratio; estimate the smoothing kernel from a few dozen quarterly marks without fooling yourself; turn a listed BDC's price-to-NAV ratio into an implied markdown on its loans, and its non-accrual disclosures into an implied carrying value for bad loans; forecast the direction of private-to-public refinancing flow from a public regime variable; price a semi-liquid fund's redemption queue as a run with a pro-rata cap; and assemble the book of public instruments that expresses all of it.

## 17.1 One Borrower Pool, Two Pricing Regimes

### 17.1.1 Desk framing: the same credit, measured twice

Start with the definitional trap, because every number in this chapter has to survive it. "Private credit" ranges from about \$1.3 trillion to more than \$3 trillion depending on whether you mean loans or assets under management, the US or the world, and whether you include dry powder. On October 16, 2026 the Federal Reserve settled the US loan number by putting private credit into the Financial Accounts (Z.1): \$1,493.5 billion of private-credit loans at the end of 2025, held by private debt funds (\$532B), BDCs (\$456B), the rest of the world (\$376B), interval and tender-offer funds (\$76B) and middle-market CLOs (\$54B) (Brinkman et al., FEDS Note, October 16, 2026). When someone tells you the size of private credit, ask which of those numbers they mean. It is the "but what does the credit agreement say?" of market sizing. Figure 17.1 shows who holds the \$1,493.5 billion and how fast each holder has grown since 2023.

![Figure 17.1: Private debt funds still hold the most (\$532B at the end of 2025), but BDCs and interval and tender-offer funds, the two holder types that reach retail investors, grew fastest, 1.9 and 2.2 times in two years. Source: Brinkman et al., FEDS Note (16 October 2026), Table F4.4.s of the Federal Reserve's Financial Accounts (Z.1), holder-side values in \$ billions at year-end; the borrower-side split in the same table is estimated.](assets/figures/ch17_z1_holders.png)

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

Mags has heard this argument before, in a different decade. "When I started, loans were priced by phone and by grudge. The bid you got depended on whether the man on the other end had been stuck with your last one. Terrible system. But every one of those numbers came from somebody who'd lose money if it was wrong."

"Who loses money if a private mark is wrong?" Theo asks. He means it as a real question: in a restructuring, the first thing anyone asks about a valuation is who paid for it.

Kaz starts to answer and then stops, because the honest answer is *nobody, this quarter*. If the manager carries a loan at 97 and it is worth 85, no trade happens at 97, no one is filled at the wrong price, and the fee is still charged on 97. The error does not show up as a loss to anyone; it shows up as a mark that is twelve points too high and a volatility series that is too smooth, and it gets corrected later, by a committee, in an amount and at a speed the committee chooses.

"Oh," Kaz says. "That's the whole problem. A public loan is *priced*: daily, noisily, by people who lose money when they're wrong, so the error is roughly mean zero. A private loan is *marked*: quarterly, from a model, smoothed, by the party that owns it and earns a fee on the number. Nobody is paid to make the error go away, so it doesn't go away. It just arrives late."

Everything in this chapter is the mathematics of that difference. Ines gives Theo the one sentence for his monitor, and he tapes it under the sticky note: *private credit is public credit with the price removed, and our job is to put the price back and get paid by whoever still believes it was never there.*

Theo will find the structure familiar, because he has seen it on the other side of the table. A BDC is, in the Boston Fed's phrase, "a CLO in which banks hold the top tranche" (Fillat, Landoni, Levin and Wang, Boston Fed Current Policy Perspectives 25-8, May 21, 2025): a bank revolver on top, unsecured notes in the middle, listed or non-listed equity at the bottom, and a manager who both picks the collateral and marks it. The redemption queue that made the cold open's seller nervous turns that structure into a borrower with a maturity wall, and §17.6.1 is where Theo's USB stick gets its next job. And "selective default" (PIK amendments, amend-and-extends, covenant holidays) is the bilateral market's liability management transaction: the same redefinition of default Theo watched in Serta and Incora, done quietly, with one lender and no docket.

### 17.1.2 What "private" actually buys: access and patience

There is an honest case for private credit, and it is worth stating before we spend thirty pages being rude about marks. The post-crisis evidence says borrowers went to nonbanks for *access*, not price. In 2010–2015 about one-third of middle-market loans came directly from nonbanks, those loans priced about 190bp above comparable bank loans after controls, and the probability of borrowing from a nonbank rose sharply when EBITDA turned negative (Chernenko, Erel and Prilmeier, NBER w26458; RFS 2022). Private lenders write cash-flow loans that banks will not, with real maintenance covenants (Block, Jang, Kaplan and Schulze, NBER w30868). The lender is paid for underwriting what the syndicated market won't take, and for holding what nobody can sell.

> **[SOURCE EXTRACTION]** *Ben_Dor_Quantitative_Credit_Portfolio_Management p.166:* "Long-term investors, with reduced mark-to-market constraints, can choose to provide liquidity to the market and buy the bond, comfortable with the low default risk."
>
> **Annotation.** This is the respectable theory of the illiquidity premium: patient capital that does not have to mark to market earns a premium for absorbing assets that forced sellers must dump. Ben Dor and coauthors are writing about public bonds after downgrades, but the logic is the original pitch for private credit, and it has two conditions. The investor must have *reduced mark-to-market constraints*, and the default risk must be *low*. The 2020s growth of semi-liquid retail vehicles quietly removed the first condition: a fund that promises quarterly liquidity at NAV has re-imported the mark-to-market constraint while keeping the mark smoothed. The 2025–26 cycle tested the second, through software borrowers exposed to AI disruption. The modern desk departs from the shelf here. It treats the illiquidity premium as real but *conditional* on the holder's liability structure, and it prices the premium separately for a drawdown fund (patient), an insurer (patient but rating-constrained) and a perpetual BDC (patient until the redemption queue says otherwise).

Ben Dor's patient investor has a modern name, and it holds earnings calls. Theo reads one of them the way he used to read a lender presentation: for what the lender says it will refuse to do.

> **View From Another Seat.** *The direct lender.* From the chair of Ares Capital, one of the largest listed BDCs, the edge is documents and patience, and the managers say so in public. On Ares Capital's fourth-quarter 2025 call (4 February 2026), its president Jim Miller said, "We will walk away from transactions based on documentation terms," put the portfolio's first-lien loan-to-values "in the high 30% to low 40% range," and reported non-accruals of 1.8% at cost against a 3.8% average for BDCs. A loan with sixty cents of equity value under it and a covenant package negotiated line by line does not need a daily price to be a good loan, and a lender that can hold it to refinancing does not need to sell it to anyone. The same seat is candid about where the weakness lives, and it is not in the loans. On the Ares Management call of 31 July 2026, chief executive Michael Arougheti said "there is a risk that some of the wealth flows could be more pro-cyclical than people thought they were." That sentence is the hinge of this chapter. The direct lender's assets are patient; a growing share of its liabilities, the retail money in perpetual vehicles, is not, and the place where a public desk meets the private lender is the funding side, where §17.6's queue lives. (Quoted words are the speakers' own, from the calls cited; the reading of them is ours.)

The dishonest version of the case is the one the Nuveen table hints at. If the volatility cell says "N/A," an optimizer that needs a number will use whatever is smoothest, and the smoothest series in the world is one nobody updates. Cliffwater's direct lending index (CDLI), which aggregates BDC portfolio marks, returned 9.3% in 2025, 10.4% of it from interest income, with a 20-year average of 9.5% and one negative year (Cliffwater release, March 31, 2026). Those are real returns to real loans. The question §17.2 answers is how much real *risk* sits behind them, and why the reported series cannot tell you.

> **Trend Watch.** *From niche to a Z.1 line item, 2010–2026.* Private-credit vehicle AUM grew from about \$350 billion in 2012 to more than \$2.6 trillion (Brinkman et al., FEDS Note, October 16, 2026). The number of loans held by private-credit BDCs rose from roughly 1,400 in 2010 to roughly 20,000 in 2022 (Ellias and de Fontenay, *The Credit Markets Go Dark*, 134 Yale L.J., January 2025). On the Fed's new Z.1 basis, US private-credit loans were \$1,042.6B (2023), \$1,253.6B (2024) and \$1,493.5B (2025), growth of about 20% a year, and private credit is now 6% of nonfinancial business debt against 3% for syndicated loans (Brinkman et al.). The retail channel grew fastest: semi-liquid fund net assets rose from about \$15B in 2018 to \$388B in 2025 (George and Shin, FEDS Note, October 14, 2026). Globally, AUM passed \$2.2T in March 2025 with a \$4.5T forecast for 2030 (BlackRock *Private Credit Primer*, January 2026). **What it means for the desk:** private credit now has official holder-level series (Z.1 codes FL893167205 for the total, FL453067203 for BDCs, FL443067205 for private debt funds, FL673067205 for middle-market CLOs; see Appendix B), which makes it a flow-of-funds variable like any other. The forced-seller graph in Chapter 1 needs five new nodes, and the largest of them, BDCs, files a schedule of every loan it owns every quarter.

### Deep-Dive Resource Graph

- **Podcasts:**
  - **"The Black Hole of Private Credit That's Swallowing the Economy"** (*Odd Lots*, 2024-09-02). Jared Ellias and Elisabeth de Fontenay on their paper "The Credit Markets Go Dark," listed below: the argument that private credit is already changing corporate governance and dynamism, so the audio on-ramp to what "private" costs as well as what it buys (§17.1.2). https://omny.fm/shows/odd-lots/the-black-hole-of-private-credit-thats-swallowing
  - **"Blackstone's Michael Zawadzki on How Private Credit Got so Big"** (*Odd Lots*, 2026-01-23). Blackstone's global CIO for credit and insurance on what it took to build the business and the advantages that accrue to large players: the lender's answer to the access-and-patience question of §17.1.2. https://omny.fm/shows/odd-lots/blackstones-michael-zawadzki-on-how-private-credit-got-so-big
  - **"Dimensional Says High-Yield Public Debt Has the Edge Over Private"** (*The Credit Edge*, 2025-05-29). Savina Rizova of Dimensional: "There is no outperformance relative to high-yield public bonds," with public-market liquidity and transparency as the offset; a dated sceptic's prior (her claim, not a study, so weigh it against Erel, Flanagan and Weisbach in §17.8). https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/dimensional-says-public-debt-has-the-edge-over-private
- **Memos and Talks:**
  - **"What's Going on in Private Credit?"** (Howard Marks, Oaktree memo, 2026-04-09). Traces sub-investment-grade credit from the 1970s to direct lending after the GFC, the issues created by rapid deployment, and the entwined fates of direct lending and private equity: the long-cycle frame for §17.1 and for the closing argument of §17.9. https://www.oaktreecapital.com/insights/memo/whats-going-on-in-private-credit
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

Kaz looks at the overlay and says the natural thing. "So the NAV is just a lagged index. Let's regress it on the index with a few lags and call the sum of coefficients the true beta." Then, after a pause that everyone on the desk recognizes: "And let's just assume Gaussian." This time Kaz is mostly right, and §17.2.2 says why. The part they will regret comes in §17.2.4.

### 17.2.2 Derivation: the Getmansky–Lo–Makarov smoothing model

> **Math, Gently.** *A thermometer with a lag, and why risk adds up in squares.* **Part 1, the filter.** Picture an old thermometer on a porch that never quite keeps up. When the temperature drops, the dial shows half of today's change today, three-tenths of it tomorrow and the last fifth the day after. Nothing is lost: the dial ends up in the right place. It just gets there late. Now let the temperature be the true value of a loan book and the dial be the manager's mark. A true loss of 4 points shows up as 2.0 points in this quarter's mark, 1.2 in the next and 0.8 in the one after. The first mark carries half the loss, and the rest is still in the pipe. A list of weights like (0.5, 0.3, 0.2) is called a *kernel*, and a mark built this way is a *moving average* of the true returns. **Part 2, the squares.** Flip one fair coin for a dollar and the result swings a full dollar either way. Flip three independent coins for a third of a dollar each and the total still averages zero, but it rarely reaches the extremes, because the coins partly cancel. Behind that calm is a rule: the variance of a weighted sum of uncorrelated pieces is the sum of the *squared* weights times the variance of one piece. Squares, because variance measures squared distance, so a third of a coin contributes a ninth of a coin's variance. Three equal thirds give $3\times\tfrac19=\tfrac13$ of the variance, and the volatility, its square root, is $1/\sqrt3\approx0.58$ of one coin's. Now do the porch thermometer in the margin: $0.5^2+0.3^2+0.2^2=0.25+0.09+0.04=0.38$, and $\sqrt{0.38}\approx0.62$. A lagged mark reports about 62% of the true volatility of the thing it marks, and nobody has to lie for that to happen. The full version is next.

**Notation.** In this chapter $t$ counts **quarters**, not years; we convert explicitly when comparing with monthly public data. We write returns as $x$ rather than $r$, because this book reserves $r$ for the short rate and $R$ for recovery. All expectations are under the physical measure $\mathbb{P}$: there is no liquid hedge for a single private loan, so nothing here is priced under $\mathbb{Q}$. (Physical measure here simply means the odds you actually face; the risk-neutral odds a hedge would imply belong to Chapters 6 and 23.)

**Assumptions.** Let $x_t$ be the true, unobservable quarterly excess return on the loan portfolio, covariance-stationary with mean $\mu$ and variance $\sigma^2$, and serially uncorrelated. Let $F_t$ be the excess return on a public factor (the leveraged loan index, say), also serially uncorrelated, with $x_t=\beta F_t+\epsilon_t$, where $\epsilon_t$ is idiosyncratic and independent of $F$ at all leads and lags. The reported (marked) return is a finite moving average of true returns:

$$
x^{o}_t=\sum_{k=0}^{K}\theta_k\,x_{t-k},\qquad \theta_k\in[0,1],\qquad \sum_{k=0}^{K}\theta_k=1 .
$$

Here $\theta_0$ is the share of today's true return that shows up in today's mark, $\theta_1$ the share that shows up next quarter, and so on. The unit-sum constraint says the marks *eventually* catch up: nothing is hidden forever, only delayed. (When the constraint fails, with $\sum_k\theta_k<1$, the marks never catch up, because the collateral was never there. That is the fraud case, and §17.8 returns to it.)

Kaz copies the kernel onto the whiteboard and asks the obvious question: what does it do to each number on a risk report? The answers fit on a line each, and the algebra behind them is in the Full Derivation at the end of this subsection. The **mean** is untouched, $\mathbb{E}[x^o_t]=\mu$, which is why the CDLI's 9.3% can be a perfectly good estimate of the average return while being useless for risk. The **variance** is deflated by the sum of squared weights, $\operatorname{Var}(x^o_t)=\sigma^2\sum_k\theta_k^2$, so reported volatility is the truth times $\sqrt{\sum_k\theta_k^2}\le1$, which is Part 2 of the box. The **Sharpe ratio** is inflated by the reciprocal, $\text{SR}^o=\text{SR}/\sqrt{\sum_k\theta_k^2}$, because the mean survived and the volatility did not.

> **Math, Gently.** *Autocorrelation: does last quarter's number predict this one?* The lag-one autocorrelation of a series is its correlation with itself one step earlier: close to +1 if up quarters follow up quarters, zero if last quarter tells you nothing, negative if the series zigzags. Think of footprints in fresh snow. A walker who stamps each print in new snow leaves prints that tell you nothing about each other. A walker whose stride is shorter than her foot leaves prints that overlap, so neighbours share some of the same snow. A smoothed mark is the second walker: this quarter's mark and last quarter's both contain a slice of last quarter's true return, so they move together even when the true returns are pure noise. Take a two-quarter kernel, (0.6, 0.4), a different porch from the one above. Two neighbouring marks share exactly one true return, weighted 0.6 in one and 0.4 in the other, so their covariance is $0.6\times0.4=0.24$ units of true variance, while each mark's own variance is $0.6^2+0.4^2=0.52$ units. Their ratio, $0.24/0.52\approx0.46$, is the lag-one autocorrelation of a series whose truth has none. The full version is next.

That is the general result: every reported **autocorrelation** is non-negative and vanishes beyond lag $K$, with $\rho^o_j=\sum_l\theta_l\theta_{l+j}\big/\sum_k\theta_k^2$. Call it what it is. NAV "momentum" in a smoothed series is a property of the measurement, not of information, and a strategy that trades it inside the private wrapper is trading the valuation calendar. Finally, the **beta** to public credit measured in the same quarter is attenuated by exactly the first weight, $\beta^o_0=\theta_0\beta$. The rest of the beta has not vanished; it is parked at lags $1,\dots,K$, and the same-quarter correlation shrinks by $\theta_0/\sqrt{\sum_k\theta_k^2}$. Those two facts are what Kaz's regression in §17.2.3 is built to undo.

**Worked check.** Take $\theta=(0.5,0.3,0.2)$, the porch thermometer. The thermometer box already did the variance, $\sum_k\theta_k^2=0.38$, so reported volatility is $\sqrt{0.38}=0.616$ of true volatility and the reported Sharpe ratio is inflated by $1/0.616=1.62$. The autocorrelations are $\rho^o_1=(0.5\cdot0.3+0.3\cdot0.2)/0.38=0.21/0.38=0.553$ and $\rho^o_2=(0.5\cdot0.2)/0.38=0.263$. The contemporaneous beta is half the true beta, and the contemporaneous correlation is $0.5/0.616=0.81$ of the true one.

Those are not exotic numbers. A two-quarter lag in the marks, which any valuation committee can produce without anyone doing anything wrong, turns an asset with the risk of a single-B loan portfolio into one that reports 62% of the volatility, half the beta and 1.6 times the Sharpe ratio. That is how a vendor field ends up saying "N/A": the honest answer would have been "about 1.6 times what you see, and correlated with things you already own, a quarter later." Figure 17.2 shows both effects: the lagged, shallower path (left) and the pending mark after a single shock (right).

![Figure 17.2: A mark that recognizes each true return over three quarters falls later and less than the true value (left), and after a 4% shock the first mark carries only 2.0 points of the loss, leaving 2.0 still to come (right). Illustrative: the §17.2.2 model with θ = (0.5, 0.3, 0.2); true quarterly returns drawn as N(1.8%, 1.2%) (seed 17) with two stress quarters of −6% and −4%; the right panel is the cumulative kernel weight times a 4% loss.](assets/figures/ch17_smoothing_staircase.png)

#### The Full Derivation

Each line above, worked from the assumptions.

**Mean.** By linearity, $\mathbb{E}[x^o_t]=\sum_k\theta_k\,\mathbb{E}[x_{t-k}]=\mu\sum_k\theta_k=\mu$. Smoothing does not change the average return.

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

Every autocorrelation of the reported series is non-negative, and it is zero beyond lag $K$. Positive autocorrelation in a NAV series is therefore *mechanical*: it would appear even if the true returns were pure noise.

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

> **Desk Myth vs. Desk Reality.** *Myth:* Private credit has low volatility and low correlation with public credit, so it diversifies a high-yield book. *Reality:* It has low *measured* volatility because $\sum_k\theta_k^2<1$, and low *contemporaneous* correlation because $\theta_0<1$. Sum the lagged betas and the correlation comes back. Cliff Asness has made the uncomfortable version of the point: "What if investors will actually pay a higher price and accept a lower expected return for very illiquid assets?" and "Attractive smoothness of returns may not come for free" (Asness, "The Illiquidity Discount?", AQR, December 19, 2019). If investors value not seeing the volatility, the smoothing is a product feature, and somebody is paying for it. The desk's job is to find out who, and to be on the other side when the feature is withdrawn.

### 17.2.3 Recovering the beta: Dimson sums and the public-leads-private test

> **Math, Gently.** *A regression slope, and summing the echoes.* A regression slope answers one question: when $X$ moves by one unit, how far does $Y$ move, on average? Numerically it is the covariance of the two divided by the variance of $X$, which is the same thing said with less charm. Now picture shouting into a canyon. Your voice comes back not once but three times, each echo fainter and later than the last. If you measure only the first echo, you conclude that the canyon returns 30% of your voice; add up all three and it returns 60%. The marks of a private fund behave like the canyon. Suppose the loan index moves by 1 point and the fund's marks answer with 0.30 points this quarter, 0.18 next quarter and 0.12 the quarter after. A regression of the mark on the same-quarter index finds a slope of 0.30 and calls it the beta. Give the regression last quarter's index and the quarter before as two more inputs, and it finds three slopes, 0.30, 0.18 and 0.12, one per echo. Their sum, $0.60$, is the true beta, and each slope divided by the sum, $0.30/0.60=0.5$, then $0.3$ and $0.2$, is the kernel the porch thermometer used. One regression, two answers. The full version is next.

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

which is known at $t$ because it uses only $F_t,F_{t-1},\dots$. The next NAV print is partly *already in the public data*. A desk that knows the index fell 3% this quarter and that $b_1\approx0.3$ knows the next mark will carry about $0.9\%$ of that fall, before the valuation committee meets. The residual $u_t$ is serially correlated (it is an MA($K$) in $\epsilon$), so ordinary least-squares standard errors understate the uncertainty, and HAC (heteroskedasticity- and autocorrelation-consistent) errors with at least $K$ lags are the honest ones. The desk found out what the difference is worth on a Thursday.

#### Kaz's first Dimson run

*(The desk's fictional run: the vehicle, its 36 quarters and every statistic in this scene are illustrative.)*

Kaz's first real run is on a listed BDC with 36 quarters of NAV history, regressed on the leveraged loan index with two lags. The output fits on one screen, and Kaz turns the screen so the desk can see it. The same-quarter slope is 0.31. The lag-one slope is 0.19 with a $t$-statistic of 1.9; the lag-two slope is 0.08 and insignificant. The sum is 0.58.

"So the lag is real," Kaz says. "Point one nine of last quarter's index shows up in this quarter's mark. That's a forecast."

"What's the second $t$-stat?" Theo asks, because there is a second column, and in his experience the second column is where the bad news lives.

"HAC. Newey–West, two lags. It's 1.3." Kaz pauses. "The residual is a moving average of the idiosyncratic returns, so neighbouring residuals share pieces. The plain errors pretend they don't."

Ines leans back. "Which one do you bet on?"

"The one that was still true after the lawyers," Mags says, which is her answer to most questions and, this time, a precise one. She means the number that survives the honest standard error. The lag-one coefficient does not; the sum does, at 0.58 with a HAC standard error of 0.14 *(illustrative)*, because the individual lags are nearly collinear in calm quarters while their total is pinned down by every big move in the sample.

Ines's view of when the tool earns its keep comes out as a question for each of them. Twenty quarters or more? Thirty-six, yes. A public factor that plausibly drives the book? A first-lien sponsor lender against the loan index, yes. Then Mags asks the one nobody has: did anything change inside those 36 quarters? Theo pulls the 10-Ks. In the twenty-second quarter the vehicle replaced its third-party valuation firm, and over the following two years its software share doubled. A new valuer means a new kernel, a strategy drift means a new beta, and either one splits the sample into pieces of 21 and 15 quarters, both short of the thirty observations the Spec below requires for $K=2$. And the vehicle co-holds most of its large loans with three other BDCs, so its marks share a common smoothing with theirs, the problem §17.2.4 returns to.

Kaz keeps the sum, files the lag-one forecast under "not yet," and rewrites the output so that the individual lag coefficients are printed in grey.

Note what the forecast does *not* say. It does not say you can buy the NAV low and sell it high, because inside a non-traded fund you transact at the smoothed NAV in both directions, subject to a cap. It says that any *public* instrument whose price is tied to that NAV (a listed BDC's equity, its bonds, a fund-of-BDCs ETF) will be repriced by a number you can forecast. §17.9 builds the book on that.

### 17.2.4 Unsmoothing, and why you should do less of it than you want to

The other direction is to invert the filter and recover $x_t$ from $x^o_t$. The workhorse is Geltner's (1991, 1993) appraisal-smoothing model from real estate, which is the GLM model with geometric weights, $\theta_k=(1-\theta)\theta^k$ for $k=0,1,2,\dots$ and $0\le\theta<1$. Those weights sum to one, and the model collapses to a recursion with a plain-English reading: this quarter's mark is a blend of this quarter's truth, with weight $1-\theta$, and last quarter's mark, with weight $\theta$. Run the blend backwards, subtracting $\theta$ times last quarter's mark and scaling what is left by $1/(1-\theta)$, and out comes an estimate of the true return. For this kernel $\theta$ is simply the first-order autocorrelation of the reported returns, so a single number, measurable from the marks alone, both describes the smoothing and undoes it. That is the attraction. Here is the catch.

> **Math, Gently.** *Why unsmoothing turns up the hiss.* Anyone who has played a quiet cassette at full volume knows the sound: the music comes back, and so does the tape hiss, louder than anyone ever heard it. Unsmoothing is a volume knob. It takes this quarter's mark, subtracts $\theta$ times last quarter's, and divides by $1-\theta$, which is small when $\theta$ is large. Every rounding error, one-off valuation call or change of valuer that sits in the marks goes through the same arithmetic, and it brings last quarter's error along with this quarter's. In the margin, at $\theta=0.6$: the divisor is $0.4$, so the signal is scaled up by $1/0.4=2.5$, while a speck of noise this quarter and an independent speck last quarter combine into noise whose variance is $(1+0.6^2)/0.4^2=1.36/0.16=8.5$ times the original, about 2.9 times in volatility. The noise is turned up more than the music, because it arrives from two quarters at once. The full version is next.

Now the regret. Real marks contain measurement noise $\eta_t$ (rounding, one-off valuation calls, the quarter a third-party valuer was replaced), so we observe $x^o_t+\eta_t$. The inversion is linear, so the noise passes straight through it, and its variance is multiplied by $(1+\theta^2)/(1-\theta)^2$. At $\theta=0.6$ that is the box's $8.5\times$; at $\theta=0.7$, $16.6\times$; at $\theta=0.9$, $181\times$. Unsmoothing a heavily smoothed series does not reveal the truth. It reveals the noise, enlarged. This is the place Kaz's Gaussian assumption bites: valuation noise is not Gaussian, it is lumpy (a single large write-down on a concentrated position), and the inversion turns a lump into a spike followed by an echo of the opposite sign.

#### The Full Derivation

The geometric kernel turns the moving average into a first-order recursion, which inverts directly:

$$
x^o_t=(1-\theta)\,x_t+\theta\,x^o_{t-1}
\quad\Longrightarrow\quad
\hat x_t=\frac{x^o_t-\theta\,x^o_{t-1}}{1-\theta}.
$$

For the geometric kernel, $\sum_k\theta_k^2=(1-\theta)^2\sum_k\theta^{2k}=(1-\theta)/(1+\theta)$ and $\rho^o_j=\theta^j$, so $\theta$ is just the first-order autocorrelation of reported returns. The variance of the unsmoothed series follows from $\operatorname{Var}(a-\theta b)=\operatorname{Var}(a)+\theta^2\operatorname{Var}(b)-2\theta\operatorname{Cov}(a,b)$:

$$
\operatorname{Var}(\hat x_t)=\frac{(1+\theta^2)\operatorname{Var}(x^o_t)-2\theta\operatorname{Cov}(x^o_t,x^o_{t-1})}{(1-\theta)^2}.
$$

With measurement noise in the observed marks, the same linear inversion gives the error of the unsmoothed series and its variance:

$$
\hat x_t-x_t=\frac{\eta_t-\theta\,\eta_{t-1}}{1-\theta},\qquad
\operatorname{Var}(\hat x_t-x_t)=\frac{1+\theta^2}{(1-\theta)^2}\,\sigma_\eta^2 .
$$

#### The quarter Kaz unsmoothed one fund

*(Illustrative: the vehicle, its marks and the committee are a fictional composite.)*

The first time Kaz unsmoothed a single vehicle there were 28 quarters of marks, and the estimate came back at $\hat\theta=0.71$. Kaz liked it. Under the geometric kernel the true volatility is the reported one times $\sqrt{(1+\theta)/(1-\theta)}$, here about 2.4, a number with a story attached. Theo asked the question he used to ask about a sponsor's EBITDA add-backs: what's the range? He did the arithmetic at a round thirty quarters, which flatters Kaz's 28. With $n=30$ and $\rho_1=0.5$, the standard error of $\hat\rho_1$ is about $\sqrt{(1-\rho_1^2)/n}=0.16$, so a 90% interval for $\theta$ runs from roughly 0.24 to 0.76. Across that interval the true volatility runs from about 1.3 times the reported figure to about 2.7 times, and the noise amplification from under $2\times$ to about $27\times$. The risk committee looked at the interval, declined to put any single unsmoothed volatility in the report, and asked for the interval instead. Kaz took it personally for about a day.

Ines added the two things the committee had not thought to ask. "Funds that hold the same loans share their smoothing, so unsmoothing them one at a time leaves the same lag in all of them. Fit it on the panel of co-holders." She was paraphrasing Couts, Gonçalves and Rossi ("Unsmoothing Returns of Illiquid Funds," *Review of Financial Studies* 37(7), 2024), who show that fund-by-fund unsmoothing leaves correlated lag in the residuals and understates systematic risk; for BDCs, which co-hold many of the same facilities, the cross-holder panel is the natural fix. "And a quarterly autocorrelation isn't a monthly one. If you're comparing it with the shelf's monthly buckets for public bonds, aggregate first."

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

Here is the awkward position the section has put Theo in. He now owns a regression that is supposed to return a fund's true beta and the shape of its smoothing kernel, and an inversion that is supposed to hand back the true quarterly return. Both claims are algebra. Neither has ever been tested against a fund whose true returns he can see, because for a real fund nobody can see them; that is the entire problem. A desk that runs this across forty vehicles every quarter cannot take the algebra on faith, and it cannot debug the code on live data, where a wrong answer looks exactly as plausible as a right one. So the first thing worth automating is a laboratory: manufacture a world where the truth is known, smear it through a kernel of our choosing, and check that each tool gives back what we put in. Ines would call it playing a hand face-up before you sit down at the table for money.

The listing builds that laboratory from six small functions. `simulate_smoothed` draws a public factor $F_t$ and true returns $x_t=\beta F_t+\epsilon_t$, then smooths them. It validates the kernel (non-empty, non-negative, positive sum), rescales it to sum to one so that marks eventually catch up, and sets each reported return to the kernel-weighted sum of today's true return and the previous $K$, with `theta[0]` multiplying today. The first $K$ reported values are NaN because the kernel is not yet full. `glm_moments` returns the closed-form predictions for any kernel: the variance ratio $\sum_k\theta_k^2$, the autocorrelation at each lag, the Sharpe inflation $1/\sqrt{\sum_k\theta_k^2}$, and $\theta_0$, the attenuation of a same-quarter beta. `autocorr` measures the same autocorrelations on a simulated series, dropping the NaN prefix first. `dimson_beta` regresses reported returns on the current and $K$ lagged factor returns by `lstsq`, returns the individual coefficients and their sum, and refuses to run when $T-K$ is below $10(K+1)$. `kernel_from_dimson` divides the coefficients by their sum, clips them to $[0,1]$, renormalizes, and returns a flag saying whether the clip bound, so a caller can tell a clean estimate from a repaired one. `unsmooth_ar1` applies Geltner's inversion and refuses any $\theta\ge0.9$.

The checks at the bottom push a kernel of $(0.5,0.3,0.2)$ through 20,000 simulated quarters and compare simulation with formula: a variance ratio of 0.38, matching lag-one and lag-two autocorrelations, a no-lag Dimson beta near 0.5, a two-lag sum near 1.0, the kernel recovered to within 0.05, and an exact Geltner round trip. The last test adds a whisper of noise to a perfectly AR(1)-smoothed series and confirms that the inversion inflates it by $(1+\theta^2)/(1-\theta)^2=8.5$.

Its natural home is as a regression test that runs whenever the estimation code changes, and as a power calculator for how long a series has to be before the estimator deserves trust. It is not evidence about any real fund: its world has Gaussian noise, one fixed kernel and no restatements. The trap is in `kernel_from_dimson`. It divides by the aggregate beta, and a fund whose sensitivity to the chosen public factor is near zero (a hedged book, or simply the wrong factor) has coefficients that sum to a small, noisy number, so the "kernel" is a ratio of noise to noise. The function raises only when the sum is below $10^{-12}$; long before that the weights can be wild, and the clip flag is the only warning you get.

*The full listing is [Listing 17.1 in Appendix F](#code-17-1).*

**Why each check is there.** The variance ratio and the two autocorrelations are the closed-form identities; if the simulation disagrees, the kernel's time index is reversed (the most common bug: `theta[0]` multiplying the oldest return). The two Dimson runs show attenuation ($\theta_0\beta$) and recovery ($\sum_k b_k\to\beta$) in one picture. The Geltner pair shows that the inversion is exact on clean data and that it amplifies noise by the predicted factor on dirty data.

**Second-stage spec (text only).** `estimate_theta_panel(nav_returns_by_fund, F, K)` fits a shared MA($K$) kernel across funds by pooled OLS of $x^o_{i,t}$ on $F_{t-k}$ with fund fixed effects, following the Couts–Gonçalves–Rossi logic. It returns $\hat\theta_k=\hat b_k/\sum_l\hat b_l$ with a block bootstrap over quarters (block length 4), and it refuses to report a point estimate when the 90% interval for $\theta_0$ is wider than 0.4. ROBO will otherwise report $\hat\theta_0=0.47$ to three decimals from 22 observations, and someone will put it in a pitch book.

> **Ways This Blows Up.** (1) *The calm-regime collinearity trap.* In a quiet stretch, $F_t$, $F_{t-1}$ and $F_{t-2}$ are tiny and nearly collinear, the individual $\hat b_k$ swing wildly, and only their sum is stable; never trade a single lag coefficient. (2) *Breaks in the kernel.* Valuation policy changes when a new third-party valuer is hired or an auditor pushes back, and $\theta$ shifts with it. A kernel fitted on 2015–2021 will understate the speed of marks after an episode like 2026, when listed prices forced faster recognition. (3) *Asymmetric smoothing.* Managers mark gains and losses at different speeds (write-downs tend to arrive in lumps, recoveries gradually). A symmetric MA kernel then misreads a single large write-down as low $\theta$. Fit up-quarters and down-quarters separately before believing either.

### Deep-Dive Resource Graph

- **Podcasts:**
  - **"Boaz Weinstein"** (*Money Stuff: The Podcast*, 2026-03-19). Matt Levine and Katie Greifeld with Saba Capital's Boaz Weinstein on private-credit NAVs, reflexivity and "volatility laundering": the practitioner's name for what the smoothing filter of §17.2.2 does to a return series. https://omny.fm/shows/money-stuff-the-podcast/boaz-weinstein
  - **"Man Not Bird"** (*Money Stuff: The Podcast*, 2026-03-13). Closed-end funds that trade at a discount, then marking private credit to market and NAV arbitrage: the price-versus-mark gap that §17.3 turns into an implied markdown. https://omny.fm/shows/money-stuff-the-podcast/man-not-bird
  - **"Why the True Price of a Bond Can Still Be Hard To Know"** (*Odd Lots*, 2021-04-05). Morningstar's Maciej Kowara and Eric Jacobson on their report "Bond Pricing: Agreeing To Disagree": evaluated prices differ by firm for bonds that rarely trade, the stale-price mechanism behind the non-synchronous betas of §17.2.3 (Dimson; Scholes and Williams). https://omny.fm/shows/odd-lots/why-the-true-price-of-a-bond-can-still-be-hard-to
- **Academic Papers:** Getmansky, Lo and Makarov, "An Econometric Model of Serial Correlation and Illiquidity in Hedge Fund Returns" (NBER w9571, 2003; *Journal of Financial Economics*, 2004), https://www.nber.org/papers/w9571 ; Couts, Gonçalves and Rossi, "Unsmoothing Returns of Illiquid Funds," *Review of Financial Studies* 37(7), 2024; Dimson, "Risk Measurement When Shares Are Subject to Infrequent Trading," *Journal of Financial Economics* (1979); Scholes and Williams, "Estimating Betas from Nonsynchronous Data," *Journal of Financial Economics* (1977); Geltner, "Smoothing in Appraisal-Based Returns," *Journal of Real Estate Finance and Economics* (1991).
- **Practitioner Writing:** Asness, "The Illiquidity Discount?" AQR Perspectives (Dec 19, 2019), https://www.aqr.com/Insights/Perspectives/The-Illiquidity-Discount
- **Data & Code:** SEC EDGAR full-text search and APIs for BDC 10-Q schedules of investments, https://www.sec.gov/edgar

## 17.3 Marking the Unmarked: BDC P/NAV, Implied Markdowns and the Non-Accrual Gap

### 17.3.1 Desk framing: a listed CLO with the manager holding the pen

The BDC is the one place where a private loan book has a public price attached. Read it as Theo would read a capital structure. At the top sits a secured revolver from banks; bank loans are about 40% of BDC debt, up from about 20% a decade earlier, and the ten largest banks provide 82% of BDC commitments (Haque and Wang, FEDS Note, August 7, 2026). Below that sit unsecured notes, typically investment-grade rated and issued in \$300–\$400mm clips. At the bottom sits equity, listed for a public BDC and redeemable at NAV, subject to a cap, for a non-traded one. Since the 2018 change that let BDCs run 2:1 debt to equity, sector leverage has risen from about 0.4x to above 1x (Avalos, Doerr and Pinter, BIS Quarterly Review, March 2025).

Two features make it different from the CLOs of Chapter 21. The manager both selects and *marks* the collateral, and the NAV is the sum of those marks. And the equity pays a management fee on gross assets and an incentive fee on income. That fee stream is a claim senior to the shareholder in every state of the world, so even a perfectly marked BDC should trade below NAV unless the manager adds value. The listed equity is therefore a price on three things at once: the loans, the fees, and the market's opinion of the marks. The trick is to separate them.

Kaz, reading the latest 10-Q, wants to know whether a "tender offer" is an offer made gently. In a sense it is: it is the non-traded BDC's quarterly offer to buy back up to 5% of its shares at NAV, made politely, and suspended without much ceremony when something more important comes up, such as a merger.

### 17.3.2 Derivation: from a listed price to an implied asset markdown

> **Math, Gently.** *The thin slice.* Theo has known this one since his first leveraged buyout model, though nobody called it math. A house worth \$210 with a \$110 mortgage is \$100 of equity. If a buyer offers \$80 for the equity, and the mortgage still has to be paid in full, the buyer is saying the house is worth \$80 + \$110 = \$190. That is a haircut of \$20 on a \$210 house, about 9.5%, not 20%. The equity is a thin slice on top of a big asset, so a large percentage move in the slice is a small percentage move in the asset underneath. A BDC is the same house: loans on the bottom of the balance sheet, a bank line and notes as the mortgage, NAV as the equity. Its leverage $\ell$ is debt over equity, $110/100 = 1.1$ here, and the translation from an equity discount to an asset markdown divides by $1+\ell=2.1$. One more wrinkle makes it a BDC rather than a house: the manager takes fees before the shareholder sees anything, which is worth, say, 5% of NAV to a buyer. So of the 20-point equity discount, 5 points are the fee and only 15 are about the loans, and $15/2.1\approx7.1\%$ is what the market is taking off the manager's marks. The full version is next.

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

**Numbers.** Blue Owl Capital Corporation (OBDC) bought back about \$148mm of its own stock in the fourth quarter of 2025 at "86% of price-to-book value," with net debt to equity of 1.19x (company release, February 18, 2026). With an illustrative fee drag $\phi=0.05$, $m=(0.95-0.86)/2.19=4.1\%$ of assets. Octus reported on April 16, 2026 that BDCs traded "at nearly a 20% discount to net asset value, with certain large names approaching a 50% discount." At $P/\text{NAV}=0.80$ and an illustrative $\ell=1.1$, the thin-slice box's arithmetic gives $m=7.1\%$; at $0.50$, $m=(0.95-0.50)/2.1=21.4\%$. The second number is the market saying that a book the manager carries at 98–100 is worth about 78. A widely reported tally put the median listed BDC at about 0.74 times *forward* NAV at the end of March 2026 (Reuters/LSEG; not independently verified for this edition), which maps to $m\approx10\%$. Figure 17.3 draws the formula at three leverage levels with these price points on it.

![Figure 17.3: Because the equity is levered, a point of discount to NAV is worth less than a point off the loans: at 1.1x leverage a 20% discount implies about 7% and a 50% discount about 21%, and the slope flattens as leverage rises. Source: the §17.3.2 formula m = ((1 − φ) − P/NAV)/(1 + ℓ) with an illustrative fee drag φ = 5% (leverage of 0.6x and 1.6x shown for contrast); OBDC's 86% of book and 1.19x net leverage are from Blue Owl's release of 18 February 2026, and the 20% and 50% discounts are from Octus (16 April 2026), plotted at an assumed 1.1x.](assets/figures/ch17_implied_markdown.png)

**Boundary conditions.** If $P/\text{NAV}>1-\phi$, the formula returns $m<0$. Floor it at zero and attribute the premium to franchise value: net investment income in excess of the dividend, a lower-cost internal management structure, or a growing fee base. Main Street Capital, an internally managed BDC, has historically traded well above NAV, and nobody believes its loans are worth more than par. If the debt is *not* money-good, relax assumption (iii): equity becomes a call option on $A(1-m)$ struck at the debt, worth more than its intrinsic value, so a given price is consistent with a *larger* $m$. The money-good formula is then a lower bound on the markdown. That Merton-on-a-CLO extension, and the $\mathbb{Q}$-measure link to BDC CDS spreads, belongs to Chapter 23. A $\mathbb{Q}$ spread set beside this $\mathbb{P}$ markdown without saying so is the classic way to get both wrong.

### 17.3.3 Derivation: the non-accrual gap and the implied carrying value of bad loans

> **Math, Gently.** *A ratio of two shares.* Picture a bowl of loans that cost \$100, of which \$2 are bruised: loans that have stopped paying, "on non-accrual." That is 2.0% *at cost*. Now the manager marks the whole bowl, and it is carried at \$98, so fair value over cost for the portfolio is 0.98. The report also says the bruised loans are 1.0% of the bowl *at fair value*, which is \$0.98 of the \$98. So two dollars of bad loans are carried at ninety-eight cents: 49 cents on the dollar. That is all the formula below does: the fair-value share over the cost share, times the bowl's overall ratio, $1.0/2.0\times0.98=0.49$. The interesting case is the one where the two shares move in opposite directions. OBDC's June 2026 release, in the table below, has non-accruals at 0.8% of fair value, the lowest in its series, and 2.8% of cost, the highest: $0.8/2.8\times0.98=0.28$. The headline number fell, and the hole got deeper, because the new bad loans arrived already marked down hard. The full version is next.

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

The June row is the box's quarter: the headline fell, and the implied carrying value of the bad bucket fell with it, from about 49 cents to about 28. While much of the industry was still quoting 70-cent recoveries, Octus estimated private-credit restructuring recoveries at "approximately 50 cents on the dollar," "well below the 70% previously cited by many managers" (Octus, April 16, 2026). The mark was moving toward the evidence; it just moved at the speed of the kernel.

Octus also put a number on the cross-holder problem. Adjusting for loans held by several BDCs raised sector non-accruals from 1.45% to 2.18% of cost, and it found "pricing gaps of nearly 40 points as measured by fair value divided by par" in widely held stressed loans. Two managers, one loan, forty points apart. One of them is wrong, and the listed price of each BDC is a vote on which. Figure 17.4 shows a real case: one loan, seven managers, seven marks.

#### The Medallia ledger

*(Theo's reading, the dialogue and the desk's spreadsheet are fictional. Every mark is fair value over par from the seven vehicles' 10-Q and 10-K schedules of investments on EDGAR, multi-lot positions summed, as in Figure 17.4.)*

It is a Wednesday in Theo's fourth week, and the job sounds like punishment: find every public vehicle that holds Medallia, a software company taken private in 2021, and copy its first-lien term loan out of each schedule of investments, every quarter, from the end of 2024 to June 2026. EDGAR's full-text search finds seven: Blackstone's BCRED and BXSL, HPS's HLEND, FS KKR, Apollo Debt Solutions, Onex Direct Lending and Monroe Capital Income Plus. Together they show about \$1.97 billion of par. Theo builds the table the way he used to build a claims register, one row per holder, and then reads it across, which is the part nobody does.

At the end of 2024 the seven marks run from 86.8 to 98.8. By September 2025 they run from 77.3 to 91.2. By December, by which time the schedules show the 4% PIK component gone and a cash coupon of SOFR plus 6.00% in its place, they run from 73.0 to 79.2. Then the first quarter of 2026: the two Blackstone vehicles take the loan from about 77.8 to 60.2 and 60.3, and both flag it as on non-accrual. In the second quarter they are at 49.5, HPS and FS KKR at 49 to 50, and Apollo's ADS, Onex and Monroe at 39 to 41. The par-weighted mark across all seven goes from 77.8 in December to 49.2 in June.

"Why do the two Blackstone funds agree to a tenth of a point?" Kaz asks. "Every quarter."

"Because it's one valuation," Theo says. "Same adviser, same committee, same third-party review. That's two rows in the spreadsheet and one opinion. If you count it as two independent marks, your dispersion statistic is lying to you." Kaz writes *cluster by adviser* on the whiteboard, under the Couts–Gonçalves–Rossi note from §17.2.4.

Then Theo finds the row that matters for the next page of this chapter. ADS carried the loan at 86.8 at the end of 2024 and at 86.8 again in June 2025, while the other six moved by between four and ten points. One unchanged mark is not evidence of anything. A run of them, while every co-holder moves, is a mark nobody looked at that quarter.

Mags reads the table over his shoulder, twice, which is applause. "The move from 94 to 77 took a year. 77 to 49 took six months. That's not a loan getting worse. That's a committee catching up."

She is describing the kernel of §17.2 in a sentence: the true loss arrived over 2025, and the marks recognized it on a lag, then all at once when a non-accrual flag forced the issue. The dispersion is the other half. At every date the highest and lowest marks sit 5 to 14 points apart, which is wide for a single first-lien loan with one coupon and one maturity, and which is not unusual. PIMCO's Lotfi Karoui, in "Daily Pricing Is Not Daily Liquidity" (11 May 2026), put marks for the same instrument across BDC portfolios at the end of 2025 "about five points apart" on average, and estimated that "83% of loans held by at least two BDCs are priced within a two-point range," with the rest skewed upward. That is the base rate: most co-held loans are marked alike, and the ones that are not are where the information is. Medallia was one of the 17%.

Theo saves the spreadsheet with a name that has the date in it, the habit of a man who has been asked for a "final final v3" at 2 a.m., and adds two columns he did not have that morning: one counting consecutive unchanged marks, one counting distinct valuation processes.

![Figure 17.4: Seven BDCs held the same Medallia first-lien term loan and all marked it down, from between 87 and 99 in December 2024 to between 39 and 50 in June 2026, yet at every date shown the highest and lowest marks sat 5 to 14 points apart, and by June 2026 they had split into two groups about nine points apart (blue: 49 to 50; orange: 39 to 41). Source: fair value over par from each BDC's 10-Q schedule of investments on EDGAR (BCRED, BXSL, HLEND, FS KKR, Apollo Debt Solutions, Onex Direct Lending, Monroe Capital Income Plus), with multi-lot positions summed; Monroe's par rose from \$12.7M to \$15.0M in June 2026, so that point needs care.](assets/figures/ch17_medallia_marks.png)

> **[SOURCE EXTRACTION]** *Ben_Dor_Quantitative_Credit_Portfolio_Management p.208:* "all bonds comprising the Corporate and High Yield indexes with a sequence of five or more unchanged quotes in any month are excluded from the eligible population of bonds for that month."
>
> **Annotation.** For public index research, a run of unchanged quotes means the price is stale and the observation is discarded. On a schedule of investments the same rule becomes a *signal*: a facility marked at the same fair value over par for five consecutive quarters, while its public comparables and its co-holders' marks moved, is a mark that has not been looked at. Those are the candidates for mark convergence, and they cluster in vehicles whose other marks are also slow. The desk departs from Ben Dor in what it does with the flag. It does not drop the observation; it adds it to the vehicle's stale-mark share, a per-BDC feature in the §17.9 relative-value model.

### Case Study: OBDC and OBDC II, November 2025 to August 2026: Same Loans, Four Prices

This is the natural experiment of the cycle. Every Blue Owl number below is from the company's own releases and SEC filings unless marked, and the desk replays it the way it replays everything, one date at a time.

#### Long Scene 1: Same Loans, Four Prices (5 Nov 2025 – 6 Mar 2026)

*(A replay, run in four sittings and cut off at each date below. The desk's cards, dialogue and hypothetical trades are fictional; the Blue Owl facts are from its releases and filings, and the trade-press and BIS figures are labeled where they appear.)*

**Beat 1: Wednesday 5 November 2025, after the close.** Ines's folder for this one is thin on purpose: one press release, one investor presentation, OBDC's last 10-Q, OBDC II's last tender-offer filing, and a screen of listed-BDC prices as of the close. "Same rules," she says. "It's the evening of the fifth. Nothing after."

The release is short. Blue Owl proposes to merge Blue Owl Capital Corporation II, a non-traded BDC, into Blue Owl Capital Corporation, its listed sibling, ticker OBDC. The two portfolios overlap by about 98%, because the adviser has been allocating the same investments to both since OBDC II's inception. The exchange will be NAV for NAV as long as OBDC trades at or below its own NAV. And OBDC II suspends its quarterly tender offers until the deal closes.

Kaz reads it and finds nothing to price. "Nothing changed. Same loans, same manager, same marks. They're stapling two piles of the same loans together, NAV in, NAV out. It's an accounting event." Then, because Kaz is honest about the float even when bored by the loans: "Except that a lot of people who were queuing to leave OBDC II are about to be handed a share they can sell on an exchange. Some of them will."

"It's a disclosure," Theo says. He has read more merger proxies than anyone at the table, and the first thing he learned was that the exchange ratio is where the seller tells you what it thinks. "Look at the condition: NAV for NAV *if OBDC trades at or below NAV*. OBDC trades below NAV. So an OBDC II holder hands over a dollar of NAV and gets back a dollar of OBDC NAV, which the stock market values at less than a dollar. Until today, that holder could tender at NAV, five percent a quarter, and nobody had ever shown them what the same loans fetched on an exchange. The ratio just did. It's a disclosure of the discount to people who had never seen one."

Mags puts it more briefly. "They just told every retail holder in that fund there's a mirror." She taps the last paragraph of the release. "And they shut the door while they did it."

Ines lets that settle, then hands out cards. "Three lines. What you do in OBDC equity. What you do in OBDC's unsecured notes. And what you tell an OBDC II holder who calls you tomorrow morning, because one will." She looks down the row to the empty chair at the end, which on this desk is where the reader sits. "You too. Write it before you read on."

The cards go face down. Kaz's says: *short OBDC equity, the merger hands listed shares to holders who wanted out; nothing in the notes; tell the holder nothing has changed in the loans.* Theo's says: *nothing in the equity; buy the notes on any weakness, a merger with its own sibling is a deleveraging story for a bondholder; tell the holder the truth, that the listed price of the same loans is below NAV and the door is closed.* Mags's says, in full: *Nothing until the tenders come back. Tell the holder not to sell to anyone at a discount before then.*

**Beat 2: Wednesday 19 November 2025.** Fourteen days later the merger is terminated: "we are no longer pursuing the merger at this point given current market conditions." OBDC II will reinstate tenders in the first quarter of 2026, subject to board approval, and the release notes that "every quarterly tender since inception has been fully satisfied." It does not mention the share price or the exchange ratio, which were the whole story.

"What market conditions changed in fourteen days?" Kaz asks.

"The release doesn't say," Theo says. "It doesn't have to. The only new information in those two weeks was that people had read the ratio."

"Nobody terminates a deal that's going well because of the weather," Mags says.

Ines grades the cards on the hand, not on the river. Kaz's short was a trade on the float, and the float trade died on the nineteenth: a fourteen-day trade with no exit written on the card. Worse, as written it was a short of the whole listed-BDC sector, because OBDC's share price moves with every BDC on the screen. "If the view is about this merger," Ines says, "then short OBDC against a basket of other listed BDCs, and cover when the merger dies. Then what you made or lost is about the merger, and not about whether people liked BDCs that week. IDO or it didn't happen." Theo's card was the right instrument in the wrong month: nothing in November had changed OBDC's leverage or its assets, so there was nothing yet for a bondholder to be paid for. Mags's card looked best of the three on the nineteenth, because the tenders were coming back. Ines writes *hold* beside it.

The third line is the one she cares about. Kaz told the holder nothing had changed, which was true of the loans and false of the holder's position. Theo told the holder the price of the same loans in a different wrapper and that the exit was shut. "That's the only line on any card that will still be right in March," Ines says, and moves on before anyone can ask her how she knows.

**Beat 3: February 2026.** The folder for the third sitting is fatter. In the first week of February an AI company released tools that automated legal, sales and data-analysis work, software equities sold off, and BDCs, which are large lenders to software companies, went down with them. Trade press reported Blue Owl down as much as 13% at one point and vehicles run by Ares, KKR, Blackstone, TPG and Apollo down 8 to 10%. The BIS's count, published in March, is the cleaner one: software equities fell almost 30% between October and February while BDC shares fell about 10%, with software-heavy BDCs lagging by around five points, and private credit funds had lent over \$500 billion to software borrowers, 19% of direct loans.

Kaz looks at the BIS chart and reaches for §17.2 without being asked. "That's the public factor moving. A thirty percent fall in the borrowers' equity. Almost none of it is in any NAV yet. The marks will get there, on the kernel's schedule." It is the first time anyone on the desk has heard Kaz describe a NAV as a forecast rather than a fact.

Then **Wednesday 18 February 2026**, and Blue Owl answers with three numbers in one day. OBDC reports fourth-quarter NAV of \$14.81 a share and says it bought back about \$148mm of its own stock at "86% of price-to-book value." That is the first price: the listed market, at 0.86 of the marks. The marks themselves are the second price, at 1.00 of book by definition. The third is a transaction. The same day, three Blue Owl BDCs agree to sell \$1.4 billion of partial interests in loans to 128 companies (97% senior secured, an average position of about \$5mm, internet software and services the largest industry at 13%) to four North American pension and insurance investors. "The investments will be sold at fair value, which is equivalent to 99.7% of par value as of February 12, 2026." OBDC II's share is \$600mm, about 34% of its commitments including unfunded ones, sold with a fairness opinion, and it funds a return-of-capital distribution of up to \$2.35 a share, about 30% of NAV and "about six times" a planned 5% tender. The board says it will use quarterly return-of-capital distributions instead of tender offers from now on, and in the same filing OBDC II cuts its revolver from \$225mm to \$75mm. *(Cooperation agreements signed in this chapter: 0; the book's counter overflowed in Chapter 14. Return-of-capital distributions substituted for tender offers: 1.)*

"Par," Kaz says. "Ninety-nine point seven. So the marks were right."

"The marks on the slices a pension fund agreed to buy were right," Ines says. "A seller who needs liquidity sells what the buyer will take. The buyer picks what it's willing to own. The price on the chosen slices tells you nothing about the ones left behind. That's showing your two best cards to prove your hand is strong."

Theo has the release open at the line about 128 companies. "Five million dollars average. They didn't sell loans, they sold slices of a lot of loans. Which keeps the sold book looking like the kept book, on paper." He scrolls down. "And OBDC's leverage is 1.19 times, down from 1.22 at September. Assets out at par, debt down, a revolver at the sibling cut by two-thirds. That's the bondholder's quarter." His November card had been early; February is the month it was written for, and the trade it describes is now the obvious one: long OBDC's unsecured notes against short OBDC's equity, because deleveraging and asset sales at par are good for the bonds and neutral at best for the shares.

Mags picks up her card from November and reads it out. "*Nothing until the tenders come back.*" She puts it down. "The tenders aren't coming back. They just turned into a distribution. I'd have waited a long time." She does not tear it up. Mags keeps her wrong cards in the same folder as her right ones, on the theory that the wrong ones are better reading.

**Beat 4: Friday 6 March 2026.** The last document in the folder is a tender-offer filing by Cox Capital, an affiliate of Saba Capital, bidding \$3.80 a share for up to 8 million shares of OBDC II, more than 30% below the fund's NAV. Later filings show that all the shares tendered were taken. Kaz divides and gets about two-thirds. The fund's own filings show the return of capital continuing in instalments that took the total to about 35% of NAV, and by the end of March OBDC II's NAV per share was \$5.57, down from \$8.27 at the end of December, most of the difference being the capital it had handed back.

"So who was right?" Kaz asks. "Two-thirds of NAV, or par?"

Ines writes four prices on the whiteboard, one under the other, and beside each the question it answers. *99.7 of par* is what the loans are worth to a pension fund that wants yield, for the slices it chose. *1.00 of NAV* is what the manager says. *About 0.68 of NAV* is what a claim on the fund is worth to someone who cannot leave. And *0.86 of book* in the fourth quarter of 2025, and about 0.71 by mid-October 2026 on an aggregator's quote, is what it is worth to someone who can sell tomorrow.

"None of them is wrong," she says. "Each answers a different question. The holder who called you in November wanted to know which question they were in." Theo takes the sticky note off his monitor, *whose number is it?*, and sticks it on the whiteboard under the fourth line.

Then the cards, one last time. Kaz's equity line, rewritten as a pair against the BDC basket and closed on the nineteenth, was a respectable fourteen-day trade; written as an outright short, it was a bet on every BDC on the screen. Theo's notes line was the trade of the first quarter. Mags's wait-for-the-tender line was the honest mistake of someone who believed a release that said tenders would return, which is what releases are for. And the reader's card is graded on its third line. If it told the OBDC II holder that the same loans had a public price below NAV and that the exit was a queue the fund controlled, full marks. If it told them to sell to the first bidder, it was the bidder's card.

Kaz, who began this chapter thinking NAV was a price, says the thing Ines has been waiting three sittings to hear. "NAV is a price for exactly one transaction: the one where the fund buys your share back. And they just stopped doing those."

**Reading it with the engine.** §17.3.2 turns OBDC's 0.86 into an implied markdown of about 4% of assets, and §17.3.3 turns the June 2026 non-accrual pair into a 28-cent carrying value on the bad bucket; the par print, read through adverse selection, is an upper bound on the kept book's marks, never a confirmation of them (the second warning in §17.9). **How a systematic desk would have traded it** is the three graded cards: short OBDC against a diversified BDC basket into the announcement and covered on termination; long the unsecured notes against short the equity through the first quarter of 2026; and, throughout, the redemption queues of Blue Owl's other non-traded vehicles as the leading indicator of further sales (§17.6). Ines replays the hand through markouts, and the trade that paid was the one that read the merger terms as a statement about the marks.

The fourth price on Ines's whiteboard belonged to a seat the desk does not sit in, and it is worth a paragraph from that chair.

> **View From Another Seat.** *The secondary buyer.* For an opportunistic fund that buys other people's illiquidity, the OBDC II episode is not a puzzle about marks; it is a holder who cannot leave and a price for letting them. Saba's Boaz Weinstein discussed exactly this on *Money Stuff: The Podcast* (19 March 2026), in an episode whose description opens, "Matt and Katie talk to Boaz Weinstein of Saba Capital Management about his tenders for OBDC II and SREIT," and lists semi-liquid fund liquidity, reflexivity, permanent capital, private-credit NAVs, public versus private BDC discounts and volatility laundering among the topics. (We quote the episode's description, not the conversation; the reading of the seat that follows is ours, and generic.) The secondary buyer's arithmetic does not require the marks to be wrong. If a fund's NAV is honest and the fund is returning capital at NAV, then a claim bought at two-thirds of NAV earns the discount as the capital comes back, and the faster the fund liquidates at NAV, the better the trade. If the NAV is too high, the discount is the buyer's cushion against it. Either way the buyer is selling liquidity to people who need it, at a price set by how badly they need it, which is the same business a market maker is in with a slower clock. HarbourVest's head of credit secondaries, Greg Ciesielski, described 2026 to *The Credit Edge* (7 May 2026) as "a buyer's market," with secondaries volume "run-rating above \$50 billion" for the year; the 0.68 was that market's price on one fund.

A third seat watched the same November headline and did the opposite of Kaz's card.

> **The Pair.** *Pair Book entry PB-16, Dov Adler's pod (a fictional composite; Vantress and the pod are invented, and the sizes, betas and costs are illustrative; OBDC, HYG and the dated events are real). A replay from the pod's ledger, as written on Thursday 6 November 2025; Chapter 17-B stresses it.* **Thesis.** OBDC trades about 14% below NAV (the fourth-quarter buybacks were later reported at 86% of book); the public data say the marks will fall by less than that discount implies, so the discount is partly mark lag and partly overshoot, and the overshoot should narrow. **Legs.** Long \$20mm of OBDC common; short \$26mm of HYG, the high-yield bond ETF, borrowed through the prime broker. **What the hedge removes.** Most of the credit-spread beta: \$26mm is OBDC's estimated daily beta to HYG, about 1.3, times the long. It is an admitted proxy, because OBDC owns floating-rate middle-market loans and HYG owns fixed-rate public bonds. **What idio remains.** The gap §17.8.3 calls $G$: the listed discount minus the markdown the public factor says is still pending, plus OBDC's own buybacks and deleveraging. **What leaks.** Three things, all written down on day one. Listed-BDC equity beta: OBDC sells off with the stock market, and HYG does not hedge an equity drawdown. Floating rate: if short rates fall, OBDC's income falls while HYG's fixed coupons gain, so the short loses on the day the long does. And the proxy shorts the wrong thing: HYG holds almost no middle-market software, so a software shock hits the long and misses the short. **What it costs to carry and to short.** The long earns OBDC's dividend on about \$20mm; the short owes HYG's distributions on \$26mm to the lender; HYG's borrow fee is usually tens of basis points, and both legs trade at a few cents of half-spread. The pair carries positively by a few percent a year on the long's market value, which is the market paying the pod to hold the one risk the hedge cannot reach.

Back on the desk, the arithmetic of the February sitting had to be done eleven more times before anyone went home.

The second week of February 2026 is when the desk wanted this code and did not have it. About a dozen listed BDCs reported inside five days, each in a slightly different format, and Kaz, who was on the desk then, did the arithmetic by hand for four of them before the fifth reported gross rather than net leverage and the sixth gave its non-accruals as text. What the desk wanted was every release translated into the same two units: how many points of asset value the market is taking off the manager's marks, and how many cents the manager is carrying the bad loans at. The arithmetic is trivial. What automation buys is that it is done identically every time, that a vehicle with no price gets a blank instead of an accidental par, and that the checks needing a whole schedule of investments (the cross-holder gap, the frozen mark) run at all, because nobody ever finds time to do them by hand.

The listing has four functions and a worked example. `implied_markdown` is the §17.3.2 formula, $m=\big((1-\phi)-P/\text{NAV}\big)/(1+\ell)$, taking the price-to-NAV ratio, net leverage and a fee drag. It returns NaN for a missing price, raises if leverage is negative or the fee drag falls outside $[0,1)$, and floors the answer at zero, so a premium name reports no markdown rather than a negative one. The fee drag defaults to zero, which overstates $m$; the checks pass the chapter's illustrative 0.05. `implied_nonaccrual_mark` is the §17.3.3 ratio: the fair-value share of non-accruals over the cost share, times a portfolio-wide fair-value-to-cost factor (default 1.0), and NaN when the cost share is not positive. `cross_holder_dispersion` takes a schedule-of-investments table, computes fair value over par for each row, groups by `facility_id`, and for every facility with at least two rows returns the count, mean, standard deviation and range. `stale_mark_flag` walks one facility's marks in quarter order and turns True from the fifth consecutive quarter carrying the same mark, judged against the prior quarter within a tolerance of 0.0001.

The worked example rebuilds the OBDC table from the chapter, derives the gap in percentage points and the implied mark with the approximate 0.98 factor, and asserts the headline numbers: 4.1% for the February buyback print, 21.4% for a name trading at half of NAV, a zero floor for a premium, NaN for a non-traded vehicle, about 28 cents on the bad bucket in June 2026, and a 40-point range on a toy facility held by three vehicles.

It earns its keep on listed vehicles with a disclosed schedule and a price. On a non-traded fund `implied_markdown` correctly says nothing, and when the debt is not money-good it is only a lower bound. The trap is in `stale_mark_flag`, and Tomasz walks into it in §17.8.1. The function compares each quarter with the one before, and any comparison involving NaN is false, so a single missing quarter silently resets the run. A facility frozen at the same mark for a year can go unflagged because one parser dropped one row, which is why the gaps get filled explicitly, or counted as their own signal, before anyone believes the flag.

*The full listing is [Listing 17.2 in Appendix F](#code-17-2).*

> **Ways This Blows Up.** (1) *Gross versus net leverage.* Use net debt to NAV as reported, and say so; gross leverage overstates $\ell$ and understates $m$. (2) *Forward versus trailing NAV.* Price-to-forward-NAV and price-to-last-reported-NAV differ by a quarter of markdowns, which in 2026 was most of the signal. (3) *Buybacks.* Repurchases below NAV are accretive: they mechanically raise NAV per share, so $P/\text{NAV}$ can fall while NAV rises. OBDC's buyback was, technically, an open market purchase, the most expensive three words in finance, deployed here to make money for the holders who stayed. Adjust NAV per share for the accretion before computing $m$. (4) *Off-balance-sheet claims.* Unfunded commitments are not in $A$ but are a call on liquidity; joint ventures and preferred equity sit between debt and equity and break the two-layer algebra. (5) *Fee drag is not a constant.* The incentive fee falls away when income approaches the hurdle, so $\phi$ shrinks exactly in stress; holding it fixed overstates $m$ in bad quarters.

### Deep-Dive Resource Graph

- **Podcasts:**
  - **"Bat Tat: Labubu, OBDC, Frank"** (*Money Stuff: The Podcast*, 2025-11-21). Publicly traded private credit, OBDC, OBDC II and private-credit marks, published two days after the November 19, 2025 merger termination in the case study above: the opening scene as Matt Levine and Katie Greifeld heard it. https://omny.fm/shows/money-stuff-the-podcast/bat-tat-labubu-obdc-frank
  - **"EP 28 | BDC Trust Gap, Carl's Jr. Collapse & The Pitt"** (*The Octus Download*, 2026-04-22). Octus's Mark Fischer on floating-rate loans repricing into distress and BDC marks on the same asset 40 points apart by holder (the episode's own figure): the dispersion that the cross-holder feature of §17.3 is built to measure. https://share.transistor.fm/s/b845e0e3
  - **"Investors Keeping Score on 'Bad PIK', Benefit Street Partners' Kumar Says"** (*The Credit Edge*, 2026-08-06). Anant Kumar on PIK used to mask stress ("you can probably fool some of the people some of the time") and a transparency push that forces dubious marks to be addressed faster: the qualitative twin of the non-accrual gap in §17.3.3. https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/investors-keeping-score-on-bad-pik-and-stale-marks-benefit-street-partners-kumar-says
  - **"Getting real about synthetic PIKs"** (*Cloud 9fin*, 2024-09-18). What synthetic PIKs are, how lenders use them and whether they will last: vocabulary for reading the PIK flags on a BDC's schedule of investments before building the gap series of §17.3.3. https://share.transistor.fm/s/86021e09
- **Posts:**
  - **"Lend, extend, and then..."** (Moody's Ratings, David Hamilton, 2026-05-18). Of 1,173 borrowers with a soft credit event in 1979 to 2026, roughly two-thirds had no hard default or repeat event within a decade and about one in four ended in hard default (the note's own figures; cite Moody's data, not the note): a base rate to set beside a BDC's non-accrual and PIK trail. https://www.moodys.com/web/en/us/insights/credit-risk/private-credit/lend-extend-and-then.html
- **Practitioner Writing:** Octus, "BDCs Trading at 50% Discount to NAV but Nonaccruals Ticking Downward" (Apr 16, 2026), https://octus.com/resources/blog/bdcs-trading-at-50-discount-to-nav-but-nonaccruals-ticking-downward/ ; Blue Owl Capital Corporation press releases (merger termination, Nov 19, 2025; \$1.4B asset sale and Q4 2025 results, Feb 18, 2026), https://www.blueowlcapitalcorporation.com/investors/news-events/press-releases
- **Academic Papers:** Haque and Wang, "The Price of Bank Funding behind Private Credit: Evidence from Business Development Companies," FEDS Note (Aug 7, 2026), https://www.federalreserve.gov/econres/notes/feds-notes/the-price-of-bank-funding-behind-private-credit-evidence-from-business-development-companies-20260807.html ; Fillat, Landoni, Levin and Wang, Boston Fed CPP 25-8 (May 21, 2025), https://www.bostonfed.org/publications/current-policy-perspectives/2025/could-the-growth-of-private-credit-pose-a-risk-to-financial-system-stability.aspx
- **Data & Code:** SEC EDGAR (10-Q/10-K schedules of investments; 8-K earnings exhibits), https://www.sec.gov/edgar

## 17.4 Two-Way Takeouts: PC↔BSL Migration as a Regime-Conditional Flow

### 17.4.1 Desk framing: the border moves, and a public variable moves it

If the two markets share one borrower pool, the interesting question is which way borrowers are crossing the border this quarter, and why. The Fed's 2026 substitution study gives the cleanest answer available. It dates a "tight leveraged-loan" regime from the syndicated market's excess loan premium, the part of loan spreads not explained by fundamentals, and finds it ran from May 2022 to September 2024. Inside that window, switching from leveraged loans to private credit peaked at about half of leveraged-loan borrowers in early 2023 (Banegas et al., August 11, 2026). Lenders call a syndicated borrower refinanced into a unitranche a "steal," and KBRA's count of steals has risen steadily since 2019. When syndicated spreads compressed in 2024, the flow reversed: takeouts in both directions were "considerably balanced" through the first nine months of 2025 (BlackRock *Private Credit Primer*, January 2026, citing LCD and KBRA).

This is RSSG home ground. Theo has run dual-track processes, a syndicated deal and a private club working in parallel with the sponsor choosing at the end, and he knows the choice turns on certainty of execution as much as spread. The quant upgrade is to stop treating each choice as a story and start treating the population of choices as a flow with a forecastable rate. That flow matters to a public desk for a concrete reason: **a private-to-syndicated takeout is new supply of syndicated loans**, and syndicated loan supply is the denominator of every CLO-demand and repricing model in Chapter 21.

### 17.4.2 Derivation: competing exits with a regime covariate

> **Math, Gently.** *A room with three doors, and a loan that can leave only once.* A hazard rate is the chance, per unit of time, that something happens to a loan that has not happened yet; Chapter 5 owns the idea and its arithmetic. Here the "something" is leaving the private book, and there is more than one way out. Picture a room with three doors. One is marked *syndicated*: the borrower refinances into the broadly syndicated loan market. One is marked *private*: another private lender takes it out. The third is marked *amended into PIK*, and on a bad day there is a fourth for default. Every door has its own hazard, and a loan can walk through only one of them, once. Give the syndicated door a hazard of 0.2 a year and the private door 0.1, and look at one quarter. The total hazard is $0.3\times0.25=0.075$, so the chance the loan leaves at all is $1-e^{-0.075}\approx7.2\%$, and the doors split it in proportion to their hazards: two-thirds, about 4.8%, through the syndicated door. The naive calculation that looks only at the syndicated door says $1-e^{-0.2\times0.25}=1-e^{-0.05}\approx4.9\%$. The gap is small here, a tenth of a point, because the other doors are narrow. Widen them, as a tight market does when amendments and defaults pile up, and the naive count keeps sending loans through the syndicated door that have already left by another one. The full version is next.

**Setup.** Each private loan $i$ outstanding at time $t$ can leave the private book in one of four ways: refinanced into the syndicated market ($B$), refinanced by another private lender ($P$), amended and extended ($X$), or defaulted. To respect the book's notation, we write the three non-default exit hazards as $\kappa^{(j)}_i(t)$ for $j\in\{B,P,X\}$ and keep $\lambda_i(t)$ for default. Hazards are annualized, so here $t$ is in years and a quarter is $\Delta t=1/4$. Cause-specific proportional hazards with a public regime covariate $\zeta_t$ (the excess loan premium, standardized, or its sign relative to its median) and the private-minus-syndicated spread differential $\Delta s_t$ (in percentage points) give

$$
\kappa^{(j)}_i(t)=\kappa^{(j)}_0\exp\!\big(\psi_j\,\zeta_t+\chi_j\,\Delta s_t+\boldsymbol{\omega}_j^{\top}\mathbf{v}_i\big),\qquad j\in\{B,P,X\},
$$

with the same form for $\lambda_i(t)$, where $\mathbf{v}_i$ holds borrower covariates (log size, software flag, credit estimate, sponsor, years to maturity). The signs the theory predicts are $\psi_B<0$ (a tight syndicated market slows takeouts into it), $\chi_B>0$ (a wider private premium pulls borrowers toward the syndicated market) and a positive size loading for $B$ (only larger borrowers can clear a syndicated book).

Over a quarter, then, the chance that a loan leaves by the syndicated door is that door's share of the total hazard times the chance the loan leaves at all; summed over the book, weighted by face, it is next quarter's syndicated supply from private takeouts, and it is never larger than the naive one-door count. The algebra follows.

#### The Full Derivation

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

**Assumptions and estimation.** Hazards are proportional within a regime, and the exit cause is observed with a lag (announcements, not closings). Estimate each cause-specific hazard by partial likelihood, treating the other exits as censoring.

#### Theo's dual track

*(Theo's memory is a composite of generic RSSG work; no real mandate, sponsor or borrower is described.)*

Kaz has the model fitted on a toy book by the time Theo comes back from lunch, and asks him the question the algebra cannot answer: what does an exit look like from inside? Theo has run dual tracks, and the one he remembers best was a sponsor-owned software company. The syndicated loan launched on a Monday with a lead-left bank, a roadshow and a price talk; a private club sat in a separate data room the whole time. For six weeks every banker on the deal called it a syndication. Then on a Thursday the sponsor signed the unitranche, because the club would commit to the whole size at a fixed spread and the syndicate would not. "In your data," Theo says, "that's a private exit that looked like a syndicated exit for six weeks. You only know the cause after the fact."

The rest comes out of the same memory. The sponsor's model at launch used the market conditions of launch week, not the revised series a statistician would publish a year later, so the regime variable has to be the vintage available at $t$ or the backtest knows something the sponsor did not. Mags, listening, adds the one nobody wants: "You've got one tight window in your data. May 2022 to September 2024. One." That makes $\psi_j$ a two-regime estimate with wide intervals. And the data are messier than the math: an exit appears on a BDC's schedule of investments as a facility that has quietly vanished, and matching it to a new syndicated loan requires the borrower-name join of §17.2's schema. "My data room was one deal," Theo says. "Yours is four hundred, and nobody tells you which ones ended.\"

### Case Study: Finastra 2023, the Steal, and the 2024 Reversal

On September 14, 2023, Kirkland & Ellis announced that it had advised Finastra, "a Vista Equity Partners portfolio company," on "a \$4.82 billion senior secured unitranche term loan facility" and "a \$500 million senior secured multicurrency revolving credit facility," used for "the refinancing of its existing credit facilities," with "more than twenty lenders and borrowers in multiple jurisdictions" (Kirkland release, September 14, 2023). The facilities being refinanced had been raised in the US and European syndicated loan markets. That is a steal of textbook size, and it was widely reported at the time as the largest private credit loan to date (KBRA DLD via press reports; not independently verified for this edition, nor were the lender names).

Put it on the regime clock. September 2023 sits in the middle of the Fed's tight window, when the excess loan premium was high and the syndicated market was charging for uncertainty as much as for credit. A software borrower with a large, aging capital structure could get certainty and size from a club of private lenders at a spread the syndicated market could not reliably match. The model's $\psi_B<0$ and $\psi_P>0$ are the formal version of that sentence.

Then the regime flipped. When syndicated spreads compressed through 2024, borrowers ran dual tracks and refinanced in both directions, and by 2024–9M2025 the takeouts were roughly balanced. A desk that carried the excess loan premium as a live input would have forecast both waves: the 2023 drain of syndicated supply into private credit, which supported CLO loan prices by shrinking the pool, and the 2024 return flow, which added supply just as CLO issuance was strong. **How to trade it:** the takeout forecast is a supply forecast. Ahead of a predicted private-to-syndicated wave, lean against repricing-sensitive loan prices and CLO equity, whose arbitrage depends on scarce collateral, and toward CLO senior tranches, which benefit from more issuance at tight liability spreads. Chapter 21 owns the CLO side; this section owns the supply number.

#### The private-side J.Crew: Pluralsight, replayed

Finastra left the syndicated market by the private door. The loan in the next replay left the private book by the third door, the one marked *amended*, and it is the case that earns the cross-holder dispersion feature of §17.3.

*(A replay cut off on Monday 3 June 2024. The desk's cards and dialogue are fictional. The marks are from the BDCs' 10-Q schedules of investments, and the deal facts from those filings, KBRA's commentary and the press reports cited; where reports differ, the text says so.)*

Mags was on the desk in the spring of 2024, so for her the rule about the cut-off is a matter of discipline; Kaz and Theo were elsewhere and play it cold. The folder holds a loan nobody on the desk could ever have bought. Vista Equity Partners took Pluralsight, an online technology-training company, private in April 2021, financed in part by a \$1.175 billion first-lien term loan of the "recurring revenue" kind, sized on subscription revenue and liquidity rather than on EBITDA, paying SOFR plus 800 and maturing in April 2027. An ARR loan, as lenders call it, is a bet that the subscriptions keep renewing; trouble shows up first as a renewal or revenue miss, long before it shows up as a missed coupon.

Theo goes to the schedules first, because that is where the lenders write down what they think. At the end of 2023, Ares Capital carried its piece of the loan, about \$106mm, at 89.0. Blue Owl's BDC carried the same loan, same coupon, same maturity, at 96.8. "Seven point eight points," Theo says. "On one first-lien loan. Before anything public happened." At the end of March 2024, in the schedules filed in May, KBRA's count of seven BDC holders ran from 83.4 to 97.0, a spread of 13.6 points, with Ares at 84.9 and Blue Owl at 83.5. The last item in the folder is a Bloomberg report from that morning, 3 June: Vista is in talks to hand control of Pluralsight to its lenders.

Ines writes the card on the whiteboard. "It's the third of June. You hold this loan in a fund that marks it, or you hold a BDC that does. Two lines. What mark do you override it to, and what public thing do you do about it?"

Kaz overrides to the average of the seven March marks, about 90, on the grounds that averaging independent estimates reduces noise. Theo overrides to the lowest, 83.4, and adds a flag for the dispersion, on the grounds that the lowest mark belongs to whoever looked hardest. Mags writes a single number, 50, and under it: *If the sponsor is handing over the keys, the equity is zero and the loan is the company.* For the second line Kaz writes *short OBDC*, and Theo writes *nothing exists*.

Then Ines opens the rest of the folder. Over the late spring and early summer, Pluralsight's intellectual property had moved into a new subsidiary, with about \$50mm from Vista funding an interest payment (reports differ on whether it came as a loan or as preferred equity). KBRA called these "reasonable and allowable stopgap measures"; creditors reportedly disputed the value of what had moved. Vista's own fund documents, reported later, had valued its equity at \$2.3 billion in the first quarter of 2023, \$1.5 billion at the end of 2023, and zero in an update dated 28 May 2024. At 30 June the BDCs marked the loan near 47 to 48: Ares at 48.0, Blue Owl at 47.0. Around 22 August a lender group led by Blue Owl and Ares took ownership, putting in about \$275mm of new money and converting about \$1.2 billion of debt into equity, with lenders at about 85% and management about 15% (Bloomberg); Vista and its co-investors lost about \$4 billion. On 30 September Ares held about \$54.7mm of new paper at cost against about \$106.5mm of old cost, and booked a realized loss of about \$60mm. Goodwin, in its client alert, called it "one of, if not, the first sponsor funded LME" in private credit: a drop-down with no court, no excluded-holder vote and no ruling, which is a liability management transaction of the kind Part IV autopsies, done in a conference room.

"So who was right?" Kaz asks, already knowing.

Mags was, on the first line, within three points and two months early. Theo was less wrong than Kaz, and his flag was the most useful thing on any card, because the 7.8-point gap at the end of 2023 and the 13.6-point spread in March were the only public signals that anything was happening, and they were sitting in schedules anyone could read. Averaging the marks, Kaz's answer, is exactly backwards for a loan held by several managers: when one committee is looking harder than the others, the dispersion is the information, and the average throws it away.

The second line is the lesson that does not fit on a card. There was no tradeable short. Pluralsight had no bonds and no CDS. Blue Owl's position was 1.7% of its BDC's net assets in March and 0.8% by June, so shorting OBDC to express a view on this loan would have meant shorting a wrapper in which the loan was less than two percent and everything else, the equity beta, the other loans, the fees, was noise as far as this trade was concerned. "The idio you wanted," Ines says, "was under two percent of the thing you could short. That's not a hedge. That's a lottery ticket on the other ninety-eight." The right answer was an internal one: override the mark to about 50, raise the cross-holder dispersion flag on every vehicle that held the loan, and carry both into the BDC relative-value model of §17.9, two months before the June 10-Qs showed 47 and 48.

The story did not stop at the conversion. By press accounts Ares and Oaktree wrote the new equity to zero in February 2026, and the restructured position kept stepping down in Ares's later schedules. "A restructured loan," Mags says, "is a loan that gets to default twice." Chapter 14 has the clock for that.

Back to the takeouts, and to the morning this listing was written for. It is a Tuesday, the Fed's regime variable has moved, and a CLO desk planning next quarter's collateral purchases wants to know how many private loans will arrive in the syndicated market. Theo's first instinct for answering is the one he built at the bank: walk the book name by name, call the sponsors, ask which ones are running a dual track and which are about to amend. That works for twenty names, and it produces a number nobody can re-run the next time the regime variable moves. The CLO desk does not want twenty opinions. It wants a single dollar figure, recomputed the morning the excess loan premium changes, for a private book of four hundred loans, that moves with the regime, the spread and each loan's own size and sector. That is a job for a function, and the function has one subtle duty: it must remember that a loan can leave only once.

The listing implements the competing-exit model of §17.4.2 in three functions. `cause_specific_hazards` takes baseline hazards for each exit cause, the regime and spread loadings `psi` and `chi`, a matrix of borrower loadings `omega`, today's regime value `zeta`, the spread differential `ds`, and a borrower-covariate matrix `V`. It forms one linear predictor per loan per cause, clips it to $[-30,30]$ so a wild covariate cannot overflow the exponential, and multiplies it into the baseline, returning an annualised hazard for every loan and cause. It rejects negative baselines. `exit_probabilities` converts those hazards into quarterly probabilities: total hazard per loan, the chance of any exit in $\Delta t$, that chance split in proportion to each cause's share of the total, and a last column for the probability the loan is still outstanding. A loan with zero total hazard gets zero exit probabilities and stays put, rather than a division error. `bsl_supply` multiplies face amounts by the probability of exit into the syndicated market and sums. Its `naive` switch uses $1-e^{-\kappa\Delta t}$ for that one cause alone, so the overstatement from ignoring competing exits can be measured rather than argued.

The checks simulate 400 illustrative loans, with log size and a software flag as covariates, and verify that each row of probabilities sums to one, that a single hazard of 0.2 yields $1-e^{-0.05}$, that all-zero hazards leave the loan outstanding with probability one, that the tight regime produces less supply than the loose one, and that the naive figure is never smaller than the competing one.

It belongs at the last step of a pipeline: the parameters come from the partial-likelihood fits the chapter describes, and the function only turns them into dollars. It is a one-quarter forecast on the loans already outstanding, with hazards held constant, and it knows nothing about new originations. The trap is positional. `bsl_supply` reads column zero of the hazard matrix as the syndicated exit, and `V` must line up column for column with the rows of `omega`. Reorder the exit causes, or feed `V` columns in a different order from the rows of `omega`, and nothing raises as long as the shapes still agree. You get a confident, wrong supply number.

*The full listing is [Listing 17.3 in Appendix F](#code-17-3).*

### Deep-Dive Resource Graph

- **Podcasts:**
  - **"Why Private Credit's Been Booming Even as Interest Rates Go Up"** (*Odd Lots*, 2023-11-20). Laura Holson of New Mountain Capital on how private credit differs from broadly syndicated loans and corporate debt, how it copes with higher rates and what could make it wobble, published two months after the Finastra refinancing in the case study above. https://omny.fm/shows/odd-lots/why-private-credits-been-booming-even-as-interest
  - **"What's Actually Going On With Private Credit"** (*Odd Lots*, 2026-04-27). Osterweis portfolio managers John Sheehan and Craig Manchuck on private credit before and after 2008, its links with private equity and insurance, and what it has done to other types of corporate debt: the public-credit manager's view of the border that §17.4 models. https://omny.fm/shows/odd-lots/whats-actually-going-on-with-private-credit
  - **"PGIM Sees 'Chilling Effect' on Private Credit From BDC Storm"** (*The Credit Edge*, 2026-04-02). Matt Harvey, PGIM's head of middle-market direct lending, says BDC turmoil leaves lenders "a little bit more conservative" on how they structure and price assets: a supply-side shock to read beside the public regime variable of §17.4.2. https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/pgim-sees-chilling-effect-on-private-credit-from-bdc-storm
- **Practitioner Writing:** Kirkland & Ellis press release on the Finastra \$5.3 billion refinancing (Sep 14, 2023), https://www.kirkland.com/news/press-release/2023/09/kirkland-advises-finastra-group-on-53-billion-refinancing ; BlackRock, *Private Credit Primer* (Jan 2026), https://www.blackrock.com/gls-download/literature/market-commentary/private-credit-primer-january-2026.pdf
- **Academic Papers:** Banegas et al., FEDS Note (Aug 11, 2026), as in §17.1; for the estimation machinery, any graduate survival-analysis text on cause-specific hazards and the Fine–Gray subdistribution alternative (Fine and Gray, *Journal of the American Statistical Association*, 1999).
- **Data & Code:** PitchBook LCD and KBRA DLD (subscription) for steals and takeouts; BDC schedules of investments on EDGAR for exits.

## 17.5 Banks Moved Up the Stack, Insurers Moved Down the Funnel

### 17.5.1 Desk framing: nobody left; everybody changed seats

The story told in 2021 was that private credit was eating the banks' lunch. The flow graph says the banks moved to a different seat at the same table, and the easiest way to see the new seat is to read the banks' own announcements the way a restructuring banker reads a commitment letter: for what they leave out.

#### Two Bank Partnerships, Read as Term Sheets

*(Theo's reading and margin notes are a fictional device; every quotation and number is from the releases and Federal Reserve papers cited.)*

Theo has two press releases open side by side and a pen, which on this desk counts as an affectation. The first is Citi's, dated 26 September 2024: Citi and Apollo announce a \$25 billion private credit and direct lending program, "initially in North America," with Mubadala as a strategic partner and Athene participating, and "the flexibility to significantly expand the size of the program beyond the initial \$25 billion." The purpose, the release says, is "to significantly enhance access for corporate and sponsor clients to the private lending capital pool." Theo reads it twice and writes in the margin: *size, geography, participants. Nothing about who holds which risk.* In a commitment letter, that is the paragraph you go looking for first.

The second is J.P. Morgan's, from 24 February 2025. The bank raises its direct-lending balance-sheet commitment to \$50 billion, plus "nearly \$15 billion from multiple co-lenders," having deployed "over \$10 billion across more than 100 private credit transactions" since 2021, and it notes that "additional details around the co-lending arrangements have not been disclosed." Its most informative line is Jamie Dimon's: "We proudly bank 80,000 companies globally through our Commercial and Investment Bank." Theo underlines it. That is the origination funnel. The bank's edge in private credit is not its balance sheet; it is that it already sees the borrowers' cash management, revolvers and M&A plans, and can route each one to whichever pocket pays best: syndicated, balance sheet, or partner fund. In the margin he translates it for the model of §17.4: *a borrower whose relationship bank runs a direct-lending program has a higher $\kappa^{(P)}$, and a bank-aligned choice of door.*

The rest of the margin fills up with the Fed's numbers, because the releases tell him what the banks want to be seen doing and the Fed papers tell him where they actually sit. Committed bank lines to private-credit vehicles were about \$95 billion at the end of 2024, \$56 billion of it drawn, up 145% in five years, with about 60% at five global systemically important banks (Berrospide, Cai, Lewis-Hayre and Zikes, FEDS Note, May 23, 2025). Of the bank exposure to BDCs reported in the Fed's Y-14 data, 97% is first-lien senior secured, and every public BDC borrowed from at least one Y-14 bank over 2013–2023 (Boston Fed CPP 25-8). Theo draws a box around the 97% and writes the sentence a CLO analyst would: *the bank is the AAA tranche of a CLO-shaped stack, paid a fee to originate and a spread to sit on top.*

The last two notes are the ones that matter to a desk that trades BDC paper, and they belong together. In the 2022 tightening, banks charged BDCs about 1.1 percentage points more than matched borrowers with the same bank, quarter and internal rating, and BDC line utilization rose 14.2 points more (Haque and Wang, August 7, 2026). The line got more expensive exactly when the BDC drew on it. For the banks themselves, a \$36 billion drawdown shock costs only about 2bp of aggregate CET1 (Berrospide et al.). So the seat is not free of risk, but the risk is mostly the BDC's. Theo writes the conclusion across the bottom of both pages, and it is the one the cold open's borrowing-base clause was hinting at: *the bank revolver is a liquidity put the BDC bought, struck where the bank chooses, repriced when exercised.*

> **Trend Watch.** *The bank–private credit partnership wave, 2023–2026.* September 26, 2024: Citi and Apollo announce a \$25 billion private credit and direct lending program, "initially in North America," with Mubadala as a strategic partner and Athene participating, and "the flexibility to significantly expand the size of the program beyond the initial \$25 billion" (Citi press release). February 24, 2025: J.P. Morgan raises its direct-lending balance-sheet commitment to \$50 billion plus "nearly \$15 billion from multiple co-lenders," having deployed "over \$10 billion across more than 100 private credit transactions" since 2021 (J.P. Morgan release). May 2025: committed bank lines to private-credit vehicles reach about \$95 billion (Fed). May 8, 2026: bank commitments to nonbank financial institutions total \$2.6 trillion, with private equity, BDCs and private credit the largest category after a \$261 billion upward revision (Fed *Financial Stability Report*). August 7, 2026: bank loans are about 40% of BDC debt, double their share a decade earlier (Haque and Wang). **What it means for the desk:** a "partnership" is an origination-and-distribution agreement plus a senior tranche, not a retreat. Model it as an edge in the forced-seller graph that runs both ways: banks feed loans into private vehicles at origination and pull liquidity back out through line pricing and borrowing-base haircuts in stress.

### 17.5.2 Insurers: the capital funnel and the ratings passport

Insurers sit lower in the funnel and buy the middle of the stack. Packaging middle-market loans into a CLO or BDC structure can cut the risk-based capital charge on the same underlying loans by about ten times; insurers with affiliated CLO or BDC managers control \$4.1 trillion, 72% of industry general-account assets; and affiliated BDCs hold more than \$100 billion, about 40% of BDC assets (Carlino, Foley-Fisher, Heinrich and Verani, FEDS Note, March 21, 2025). The passport that makes the capital arithmetic work is the private letter rating, which feeds an NAIC designation through the filing-exemption process.

Theo's bank sits at the top of the pipe. The insurer sits in the middle of it, and from there the same loans look nothing like a price.

> **View From Another Seat.** *The insurer.* From an annuity writer's chair a loan is not a mark to be argued about; it is a spread to be earned against a liability, after a capital charge. Apollo's chief executive Marc Rowan put the whole model in one sentence on the firm's fourth-quarter 2025 call (9 February 2026): "Spread is created by having an asset origination machine, by having a liability origination machine at a low cost, and by having a low OpEx." The liability machine is Athene, whose net invested assets were \$292 billion at year-end 2025, by the figures given on the same call. The seat's question about any piece of credit is capital charge per unit of spread: a privately rated BBB-minus placement with a clean NAIC designation can beat a public BB at a wider spread, and the insurer does not sell because a position moved five points. It sells when a designation, a rating or a downgrade raises the charge. The live example of the middle of the stack is in this chapter's Long Scene 1: the four North American pension and insurance investors who bought \$1.4 billion of slices of Blue Owl's loans at 99.7% of par in February 2026 were buying exactly what this seat buys, senior secured, diversified, held to maturity and priced against a liability rather than a screen. From the insurer's chair that print was not a statement about anyone's marks. It was a yield. (Rowan's words are his own, from the call; the reading of the seat is ours.)

The private-rating passport is now being inspected. In 2024 the NAIC "authorized regulators to challenge or override NAIC Designations assigned through the filing exemption process" (NAIC private credit resource page). By August 13, 2026 its working group reported that the "ability to implement discretion over NAIC Designations assigned through the Filing Exemption Process is operational," with an amendment on the treatment of CLOs exposed for comment through September 14, 2026 (NAIC IDAWG summary). FactSet's analysis of statutory filings found that "at year-end 2025, 19.7% of all filings were unresolved," that "private investments reached 38.7% of corporate bond holdings in 2024," and that new reporting Item 2025-19, effective December 31, 2026, "will require insurers to quantify every private placement on their books" supported only by private ratings (Johnson, FactSet Insight, May 29, 2026).

Mags has seen this movie. "Back in my day the rating agencies were paid by the issuer and everybody pretended that was fine. Now the rating is private, the issuer pays, and nobody even has to pretend. The regulator showing up to check is the first new idea in thirty years." Grudging respect: it is a good idea. **For a public desk it is a calendar.** If designation challenges or the CLO amendment push capital charges up, insurers will rotate out of privately rated paper and middle-market CLO mezzanine and into public BBB and BB credit. That is a forced flow with dates attached, which is the only kind of flow a systematic desk should pre-position for.

### Deep-Dive Resource Graph

- **Podcasts:**
  - **"How Banks and Private Credit Became the Best of Frenemies"** (*Odd Lots*, 2024-10-24). Huw van Steenis of Oliver Wyman on why more than a dozen big banks teamed up with private credit in a single year and how much of a threat private credit really is to banks: the audio companion to the partnership Trend Watch in §17.5.1. https://omny.fm/shows/odd-lots/102424-odd-lots-huw-van-steenis-master-3
  - **"Why Private Credit Got Entangled With Insurance"** (*Odd Lots*, 2026-07-31). Andrew Granato (UT Austin Law) and Pranjal Drall (Yale), authors of "Private Credit's State Backstop: How Private Equity Socializes Risk Through Insurers," on why PE wanted insurers and who ends up holding the risk: the regulatory flip side of the §17.5.2 funnel. https://omny.fm/shows/odd-lots/why-private-credit-got-entangled-with-insurance
- **Talks:**
  - **"When Regulation Reshapes Markets: The Migration of Corporate Lending"** (Michelle W. Bowman, Fed Vice Chair for Supervision, Hoover Institution Annual Monetary Policy Conference, 2026-05-08). A bank supervisor on why corporate lending migrates to private credit funds and BDCs, what banks exiting those services implies and the Fed's policy response; she calls private credit "still a small fraction of overall corporate borrowing": the primary-source anchor for the "banks moved up the stack" argument. https://www.federalreserve.gov/newsevents/speech/bowman20260508a.htm
  - **"Reflections on Financial Stability"** (Lisa D. Cook, Fed Governor, Yale Program on Financial Stability, 2026-03-26). How the Board tracks private credit arrangements and bank-nonbank links, including bank loan commitments to nonbank financial institutions growing at an annualized rate of about 9%, roughly three times the pace of C&I lending (her figures): supports the bank-funding leg of §17.5.1. https://www.federalreserve.gov/newsevents/speech/cook20260326a.htm
- **Practitioner Writing:** Citi, "Citi and Apollo Announce \$25 Billion Private Credit, Direct Lending Program" (Sep 26, 2024), https://www.citigroup.com/global/news/press-release/2024/citi-and-apollo-announce-25-billion-private-credit-direct-lending-program ; J.P. Morgan, "JPMorgan Increases Direct Lending Commitment to \$50 Billion" (Feb 24, 2025), https://www.jpmorgan.com/about-us/corporate-news/2025/jpmorgan-increases-direct-lending-commitment-to-50-billion ; Johnson, "Almost One-Fifth of Insurer-Held Private Securities Are Not Rated, but Disclosure Is Changing," FactSet Insight (May 29, 2026), https://insight.factset.com/almost-one-fifth-of-insurer-held-private-securities-are-not-rated-but-disclosure-is-changing
- **Academic Papers:** Berrospide, Cai, Lewis-Hayre and Zikes, FEDS Note (May 23, 2025), https://www.federalreserve.gov/econres/notes/feds-notes/bank-lending-to-private-credit-size-characteristics-and-financial-stability-implications-20250523.html ; Carlino, Foley-Fisher, Heinrich and Verani, FEDS Note (Mar 21, 2025), https://www.federalreserve.gov/econres/notes/feds-notes/life-insurers-role-in-the-intermediation-chain-of-public-and-private-credit-to-risky-firms-20250321.html
- **Data & Code:** NAIC private credit resource center, https://content.naic.org/resource-center/private-credit-insurance-regulation

## 17.6 Semi-Liquid Vehicles and the Redemption Game

### 17.6.1 Desk framing: the failure mode moved from defaults to redemptions

Retail money became the marginal private-credit dollar. Semi-liquid vehicles (perpetual non-traded BDCs and interval funds) held about \$425 billion gross and \$241 billion net by the Fed's May 2026 count, about one-fifth of private credit's net AUM, and in the first quarter of 2026 accepted redemptions exceeded inflows for the first time (Fed *Financial Stability Report*, May 8, 2026). Non-traded BDCs hold about 0.2% of assets in short-term liquid instruments, with debt to equity of 0.90 (George and Shin, October 14, 2026). Their liquidity is not cash. It is bank lines, loan repayments and a sleeve of syndicated loans held to be sold.

That changes what can go wrong. A drawdown fund with ten-year locked capital fails, if it fails, through defaults. A semi-liquid fund that promises quarterly repurchases at NAV can fail through *redemptions* while its loans perform, because the NAV it pays out is smoothed and everyone knows it. The IMF put the mechanism precisely: slow-moving valuations create a first-mover advantage, and discretionary gating "may erode investor confidence across the broader industry" (IMF *Global Financial Stability Report*, April 2026, ch. 1).

Theo recognizes the problem instantly, which is a strange feeling for a man three weeks into a quant desk. A fund facing a redemption queue is a borrower facing a maturity wall, and his thirteen-week cash flow model, still on the USB stick, needs only three row renames: "revolver availability" becomes undrawn lines, "asset sales" becomes the syndicated sleeve, and "maturities" becomes the redemption cap. The model that refuses to die has found its next body: a liquidity runway measured in quarters.

### 17.6.2 Derivation: a run with a pro-rata cap

> **Math, Gently.** *Who pays for an early exit, and why the line gets longer.* **Part 1, the transfer.** Picture a pizza cut into 100 slices. The box says each slice is worth a dollar, but the pizza has been sitting out and each slice is really worth 95 cents. The rule is that anyone who leaves the table is paid a dollar a slice, in cash, out of the pizza. Five people leave with one slice's worth each: they take \$5 of value, though their slices were worth only \$4.75, and the extra quarter comes out of everyone else's cheese. Put it in the chapter's units: a markdown $m=5\%$ and redemptions $p=5\%$ leave the stayers holding $(0.95-0.05)/0.95\approx0.947$ of NAV per share instead of 0.95, and the total transfer is $p\times m=0.25\%$ of NAV. Small in one quarter; the point is that it is never negative, so leaving early is always at least as good as staying. **Part 2, the queue.** Start with 100 shares. Requests come in for 16.8, the cap pays 5, so 11.8 shares wait in line and 95 shares remain. Next quarter, suppose a tenth of the 83.2 shares that are not already in line join it: that is 8.3 new requests on top of the 11.8, a demand of 20.1, and the cap now pays 5% of 95, or 4.75. The fill rate has fallen from 30% to about 24% with nobody new panicking harder than before. The full version is next.

**Notation.** NAV per share is $N$ (smoothed); the true value per share is $N(1-m)$, with $m$ the markdown of §17.3. The quarterly cap is $c$ (typically 5% of shares). The request fraction is $a_t$, which we deliberately do not call $q$, a letter this book reserves for dealer inventory. The fill fraction is $f_t=\min(1,c/a_t)$, and the share of the fund actually redeemed is $p_t=f_ta_t=\min(a_t,c)$.

**The transfer**, in one line: write $N^{\text{true}}_{\text{stay}}$ for the true value of each share left behind after a quarter's redemptions. Because leavers are paid the smoothed $N$ while the shares are worth $N(1-m)$, $N^{\text{true}}_{\text{stay}}$ falls below $N(1-m)$ whenever $p_t\,m>0$, and the stayers hand $p_t\,m$ of NAV per share to the leavers each quarter. The pizza did it in the margin; the algebra is in the Full Derivation below.

**The game.** An investor who requests gets $N$ on a fraction $f_t$ of her shares and $N^{\text{true}}_{\text{stay}}$ on the rest; one who does not gets $N^{\text{true}}_{\text{stay}}$ on everything. Since $N>N(1-m)>N^{\text{true}}_{\text{stay}}$ when $m>0$, requesting pays $f_t\big(N-N^{\text{true}}_{\text{stay}}\big)>0$ more, for any $f_t>0$. **Requesting is a dominant strategy as soon as $m>0$ is believed**, net of whatever small early-repurchase fee or tax friction applies. The cap does not remove the first-mover advantage; it rations it. If everyone requests, $a_t=1$, $f_t=c$, and the fund pays out $c$ per quarter: a 5% cap turns a run into a twenty-quarter queue.

Why, then, do request fractions sit at 6% or 17% rather than 100%? Because $m$ is not common knowledge. Most holders came through an advisor, few read the 10-Q, and many do not know a listed sibling exists. The request fraction $a_t$ is therefore a *belief* variable: the share of holders who are both attentive and persuaded that $m>0$. It jumps when a public signal coordinates beliefs, which is why a listed sibling printing 0.86 of book, or a merger at NAV-for-NAV, moves the non-traded fund's queue.

**Queue dynamics.** Unfilled tender requests usually lapse and must be resubmitted, and in practice most are, which behaves like a rolling backlog $\mathcal{B}_t$. With new requests arriving as a fraction $a^{\text{new}}_t$ of non-queued shares, demand is $\mathcal{B}_t+a^{\text{new}}_t(S_t-\mathcal{B}_t)$, payouts are $\min(\text{demand},cS_t)$, the backlog carries the rest, and $S_{t+1}=S_t-\text{payout}$. Fill rates fall quarter after quarter even if new requests are steady, and that falling fill is itself a public signal that feeds the next quarter's $a^{\text{new}}$.

**Liquidity runway** is the number of quarters a vehicle's liquid resources cover its quarterly outflows: cash, undrawn bank lines and the syndicated sleeve after a stress haircut $h$, against capped redemptions, unfunded commitments drawn and debt maturing, net of loan repayments. Its formula, $\mathcal{T}$, is in the Full Derivation. The IMF's calibration target is 9–11 quarters of 5% redemptions under mild stress and 5–7 under a moderate shock. The repayment term links this section to §17.4: repayments *are* the private book's exit hazards, $\kappa^{(B)}+\kappa^{(P)}$, and those fall in a tight-loan regime, exactly when redemptions rise. The haircut $h$ is reflexive: when several funds sell their sleeves at once, the sale *is* the spillover into public loan prices, and the haircut rises because of the selling it is meant to measure. And the fund can change $c$: OBDC II's move from tenders to return-of-capital distributions changed the payout rule, and with it the game.

#### The Full Derivation

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

**Liquidity runway.** In quarters, for a vehicle with NAV normalized to one,

$$
\mathcal{T}=\frac{\text{Cash}+\text{Undrawn lines}+\text{Sleeve}\times(1-h)}{c\cdot\text{NAV}+\text{Unfunded draws}+\text{Debt maturities}-\text{Repayments}},
$$

where $h$ is the haircut on the syndicated sleeve under stress and every flow in the denominator is per quarter. If the denominator is zero or negative, the runway is unbounded.

Ines has a way of drawing all of this that does not need a single symbol, and it is the one the desk remembers.

> **Poker Table.** Ines draws the redemption queue as a hand. "Twenty players, one pot, and the dealer will only pay five percent of the pot per round, pro rata among whoever stands up. Everyone can see a card face down in the middle; it's the true NAV. Nobody can turn it over, but there's a mirror across the room, the listed sibling's price, and it says the card is worse than the dealer claims. The first players to believe the mirror stand up first and get paid at the dealer's number. Everyone else is subsidizing them. You don't win this hand by being right about the card. You win by being early about the mirror." Then she replays it through markouts: in the first quarter of 2026, the investors who requested in January were filled at a NAV that later quarters marked down.

### Case Study: The Redemption Quarters of 2026

#### Long Scene 2: The Queue (Jan – Sep 2026)

*(A review rather than a blind replay: everyone at the table has seen the ending, so Ines grades the cards on arithmetic rather than on surprise. The cast, dialogue, cards and the desk's table are fictional; the fund facts are from the funds' filings and letters, the Federal Reserve and the IMF, and press reports where marked.)*

Ines calls the folder "The Queue," and it is the only one on the shared drive that has grown every week since Theo arrived. The Friday she runs it, she makes a rule she has never made before: the cards will be arithmetic. "We all know how this year went," she says. "So nobody gets credit for knowing. You get credit for doing the sums the way you'd have done them that day."

**Beat 1: the first quarter, January to May 2026.** The first document is Bloomberg Law's of 26 March. Investors had sought about \$13 billion from "over a dozen funds," and with quarterly caps around 5% of net assets, "more than \$4.6 billion of investor capital" was trapped behind withdrawal limits. Then the individual funds, as the press and their own filings told it. Blackstone's flagship BCRED received requests for 7.9% of its shares by press reports; its board upsized the offer to 7%, and Blackstone and its employees put about \$400 million into a feeder fund to cover the rest. Barings capped a private credit fund at 5% after requests reported at 11.3% of shares. In early April, press reports said Moody's had moved its outlook on a large Blue Owl non-traded BDC to negative. And on 8 May the Fed's *Financial Stability Report* put the quarter in one sentence: for perpetual BDCs, accepted redemptions exceeded new inflows for the first time since those vehicles were created, and several funds had received requests "much larger than 5 percent of NAV."

Kaz builds a table while Ines reads, which is how Kaz listens. One row per fund per quarter: the request percentage, the cap, the fill, the date the filing landed. It takes most of an afternoon, mostly spent learning that a tender-offer filing reports its result in an amendment, that the amendment sometimes gives requests in dollars and sometimes in shares, and that a fund letter sometimes rounds. "This is the cheapest data in the chapter," Kaz says when it is done, sounding surprised. "Every number is public. It lands in an 8-K, a Schedule TO amendment or a letter within days of the quarter's deadline. And it's the most direct measure there is of how many holders believe $m>0$, which is why it leads the listed BDC shares and the BDC bonds. Highest signal-to-noise of anything we've got."

"Then why isn't it in the risk system?" Theo asks.

"Because it doesn't come from a vendor," Mags says, "and nobody gets fired for not having data that doesn't come from a vendor." She is right about the incentive and wrong about the value, and she knows it; she asks Kaz to send her the table.

**Beat 2: the second quarter, to 23 June.** The second sitting's documents arrive in the order the desk saw them. In April, Blue Owl's two non-traded BDCs drew exit requests of "roughly 20% and 40%." Morgan Stanley's North Haven Private Income Fund had limited repurchases to 5% in March. On 10 June, at an industry conference, Ares's Michael Arougheti was reported to have said that requests for about 11% of the shares of Ares's non-traded BDC had come from fewer than 5% of its investors, and that draining liquidity to meet them would hurt the 95% who stay (a secondary account of the remarks; we paraphrase it). And on 23 June, InvestmentNews: Apollo Debt Solutions, a \$26 billion fund, saw requests reach "16.8%, equivalent to \$2.4 billion," capped at 5% of shares, "the standard limit for such vehicles"; Blackstone's \$79 billion BCRED had received repurchase requests "amounting to 10% of shares outstanding" for the quarter to 30 June.

"Arougheti's number is the interesting one," Theo says. "Fewer than five percent of the holders asking for eleven percent of the fund. That's not a run. That's a handful of large accounts who read the 10-Q."

"Or a handful of advisors with a lot of clients each," Ines says. "Either way, it's the direct lender's answer to our question. He's telling you the queue is concentrated, and that the people in it are the attentive ones." She lets that sit. "Which is exactly what the model says the people in the queue should be."

**Beat 3: the summer, and the resubmissions.** The third sitting is the one that changes Kaz's mind. By the third quarter the fund letters had started to describe who was in the queue, and the answer was: mostly the same people. Nearly two-thirds of Morgan Stanley North Haven's third-quarter requests came from holders who had been prorated before. Blue Owl described "the vast majority" of OCIC's requests the same way. Unfilled requests are not automatically carried over in most of these documents, so a holder who wants out and was prorated has to ask again, and they do.

Kaz stares at the table for a long time, then deletes a column. "I had new requests as a fraction of shares. That's wrong. It's a fraction of shares *not already in the line*, and the line refills itself. A holder who asked in March and got thirty percent filled is going to ask again in June, and in September. The request percentage isn't new information every quarter. Most of it is last quarter's information, resubmitted." Then, more quietly: "And $a_t$ isn't a number about the fund. It's a number about what the holders believe. It only jumps when something tells them to believe something different."

The summer's numbers fill in the rest. BCRED received \$4.5 billion of requests in the second quarter, paid about half and carried a \$2.3 billion backlog into the third. At Blue Owl's software-focused OTIC, 38 to 40% of shares were tendered in two straight quarters, and fills ran 13 to 14%. At the other end, a widely circulated tracker showed Golub, Goldman Sachs and Fidelity vehicles with requests of 3 to 5% and paid in full. The asset class did not run. Funds with software exposure, retail distribution and a headline did.

![Figure 17.5: Every fund plotted drew requests of 9% to 40% of shares against the 5% cap, so each prorated and its fill rate was about the cap divided by requests (left); if unfilled requests are resubmitted, the queue grows and the fill rate keeps falling even with steady new demand (right). Source (left): Schedule TO-I/A filings, requests as a share of shares outstanding; Q3 2026 points are preliminary; BCRED's Q1 request is not shown, its Q2 and Q3 requests were both about 10% (the dots coincide), and its Q2 fill is its letter's "approximately half". Illustrative (right): the §17.6.2 backlog recursion with a 5% cap and new requests of 10% of non-queued shares each quarter.](assets/figures/ch17_redemption_queue.png)

Mags reads the sponsors' responses aloud, the way she reads a plan of reorganization, by asking who pays. There were five tools, and each fund reached for some of them. Upsizing the cap with house money, as BCRED did in the first quarter. Return of capital in place of tenders, as OBDC II did in February. Selling loans at par, as Blue Owl did. Buying back the listed share below NAV, as OBDC did at 86% of book. And cutting the distribution, as BCRED did in the third quarter, from 10.0% to 9.1%. "Every one of those moves money between the people who stay and the people who leave," she says. "Some of them move it the right way. None of them makes it disappear." The IMF, in April, had already read the gate the same way: recent cases in which managers "either accommodated redemptions above the 5 percent limit or gated them despite apparent balance sheet capacity highlight the discretionary nature of these programs." A decision, not a wall.

**Beat 4: back to Tuesday 23 June, 2:40 p.m.** Ines closes the folder and opens the cold open's, at the minute the headline crossed. "Same moment. But this time you've got the model. Card." She writes it on the whiteboard: *For the fund in the headline, write the fill rate, the quarterly transfer at an illustrative $m$ of 5%, and the runway in quarters. Then say what you do in the listed BDC basket, and which syndicated loans you expect to see for sale.*

The arithmetic part is quick, and the desk's cards agree on it. The fill is $0.05/0.168\approx30\%$, which is about what Apollo Debt Solutions' filings later showed. At $m=5\%$ and $p=5\%$ the stayers' true value per share falls from 0.950 to 0.947 of NAV and the transfer is $p\,m=0.25\%$ of NAV, exactly the pizza of §17.6.2. That is small in a quarter and corrosive over five. The runway is where the cards split. Kaz writes the desk's illustrative runway check, described with the listing below: under three quarters with no loan repayments, 4.8 with repayments of 3% of NAV a quarter, just under the IMF's moderate-shock range of 5 to 7 and nowhere near its mild-stress 9 to 11. Theo writes *depends on the borrowing base*, and underneath it the cold open's question about PIK eligibility. Ines gives Theo the better mark, because the runway of a real fund is a number you cannot get from a headline, and a card that says so, and says which document would settle it, is worth more than a card with a confident illustrative figure on it.

The trade lines are where the year grades them. Kaz's card says *short the listed BDC basket*. Theo's says *long the listed BDCs with the least software and the most borrowers, short the rest; expect sales from the funds' liquid sleeves, the syndicated loans that sell nearest par.* Mags's says *buy what the queues force out, a quarter later.* The listed discounts stayed wide all year: the 0.74 median and the Octus figures of §17.3.2 in the spring, and, on an aggregator's mid-October quotes, a median near 0.76 of book for externally managed names, with OBDC near 0.71 and FS KKR near 0.56. But Kaz's outright short was a short of everything the listed BDCs share with the equity market, and Theo's dispersion trade was the one that isolated what the queue was actually about: which vehicles' holders had reason to believe $m>0$. On the loans, the year marked Theo down. The sponsors mostly reached for tools that kept loans off the syndicated market, house money, return of capital, distribution cuts and par sales of private slices to buyers who wanted them, which is to say the forced selling Theo's card predicted was absorbed by the sponsors' own choices before it reached the tape. Mags's card was right about the shape and wrong about the venue: what the queues forced out, they forced out privately, at par, to an insurer.

"So the model was right and the trade was wrong?" Kaz asks.

"The model was right about who wanted to leave and what it cost the people who stayed," Ines says. "It said nothing about how the sponsor would choose to pay for it. That's not in the algebra. That's in the letters."

The listing exists for the morning an 8-K lands. A fund has published its request percentage, the risk committee wants to know by lunch how many quarters of this the vehicle can survive, and the desk has thirty such vehicles. One quarter is easy on a calculator, as Beat 4 showed: 16.8% requested, a 30% fill, a quarter of a point of NAV moved from stayers to leavers. The hard part is the sequel. Unfilled requests come back next quarter, the share count shrinks, and the fill rate falls even if nobody new panics, which is Kaz's deleted column from Beat 3. Those are recursions, and recursions are where hand arithmetic quietly stops tying. Theo's thirteen-week model had the same shape, a balance rolling forward with a backlog on one side and a liquidity cushion on the other, which is why he can read the listing's logic before he reads its syntax. A desk wants it as code for a plainer reason: the request percentage is the cheapest, highest-signal series in the chapter, and the only way to use it across thirty vehicles is to turn each new print into a queue and a runway without anyone opening a spreadsheet.

The listing is four functions. `redemption_fill` is the fill fraction $f=\min(1,c/a)$, returning 1 when nothing is requested. `stayer_value` computes the true value per remaining share after pro-rata redemptions paid at smoothed NAV, $N\big((1-m)-p\big)/(1-p)$ with $p=f\,a$. `queue_path` is the backlog recursion. Starting from one unit of shares, each quarter's new requests are a fraction of the shares *not already in the queue*; demand is backlog plus new; the payout is the smaller of demand and the cap times current shares; the remainder carries forward and the share count falls by the payout. It returns one row per quarter with shares, new requests, demand, paid, fill and ending backlog, and it rejects any request fraction outside $[0,1]$. `runway_quarters` divides liquid resources (cash, undrawn lines and the sleeve after its haircut) by the quarterly outflow (capped redemptions, unfunded draws and maturities, less repayments), and returns infinity when the outflow is zero or negative.

The checks confirm the chapter's numbers: a 30% fill at 16.8% requests, a stayer value of 0.947, zero transfer when marks are honest, stayers' loss equal to $p\,m$, requesting strictly better than waiting, payouts never above the cap, new requests reconciling exactly to payouts plus the final backlog, fills that fall monotonically under steady demand, and the two runway figures read out below.

`queue_path` and `runway_quarters` fit a vehicle with a published cap and a disclosed liquidity stack; they do not predict $a$, which the listing takes as given. The trap is the definition of the input, and it is Kaz's deleted column. `queue_path` wants each quarter's requests as a fraction of non-queued shares. A filing that reports requests as a percentage of all shares outstanding may already include resubmitted backlog, and feeding that figure in after the first quarter counts the queue twice.

*The full listing is [Listing 17.4 in Appendix F](#code-17-4).*

The runway check is a non-traded BDC with 0.2% cash, an undrawn line of 10% of NAV and a 10% syndicated sleeve haircut by 10%, paying 5% redemptions and 2% of NAV a quarter in unfunded draws *(illustrative)*. With no repayments it lasts under three quarters; with repayments of 3% of NAV a quarter it lasts 4.8, just under the IMF's moderate-shock range. Everything turns on the repayment rate, and the repayment rate is the hazard model of §17.4.

> **Ways This Blows Up.** (1) *Treating the sleeve as cash.* The haircut is a function of how many other funds are selling the same loans that week. (2) *Assuming the rules are fixed.* Boards can suspend tenders, switch to return-of-capital distributions, or (in some structures) raise the cap; each changes the game mid-hand. (3) *Ignoring the bank.* A borrowing-base haircut on PIK or non-accrual loans shrinks the undrawn line exactly when the queue lengthens, which is the question Theo asked in the cold open. (4) *Reading low requests as health.* A falling $a_t$ after a gate may mean investors gave up, not that they were reassured; check whether the backlog was resubmitted.

The year in dates, for the tracker in Appendix C:

> **Trend Watch.** *The listed discount and the redemption queue, November 2025 to September 2026.* November 5–19, 2025: the OBDC/OBDC II NAV-for-NAV merger is announced and terminated within fourteen days (Blue Owl releases). February 18, 2026: OBDC repurchases stock at a reported 86% of book (check against the OBDC Q4 release); OBDC II replaces tender offers with return-of-capital distributions (Blue Owl releases). March 26, 2026: about \$13 billion of first-quarter requests, more than \$4.6 billion trapped (Bloomberg Law). End of March 2026: the median listed BDC is reported at about 0.74 times forward NAV, the widest since 2020 (Reuters/LSEG; not independently verified). April 14, 2026: the IMF estimates non-traded BDCs can meet 5% quarterly redemptions for 9–11 quarters under mild stress and 5–7 under a moderate shock. April 16, 2026: listed BDCs at "nearly a 20% discount," some large names "approaching a 50% discount" (Octus). May 8, 2026: the Fed FSR reports that, for perpetual BDCs, accepted redemptions exceeded inflows in Q1 2026, the first time since those vehicles were created. June 23, 2026: a \$26 billion fund at 16.8% requests and a \$79 billion fund at 10% (InvestmentNews). **What it means for the desk:** the dispersion of listed discounts, not their mean, is the tradable signal (§17.9), and the redemption series is its leading indicator.

### Deep-Dive Resource Graph

- **Podcasts:**
  - **"EP 28 | BDC Trust Gap, Carl's Jr. Collapse & The Pitt"** (*The Octus Download*, 2026-04-22). A Blue Owl technology fund facing repurchase requests on 40% of shares against a 5% limit, and Saba tendering at a 33% discount (the episode's own numbers): the pro-rata cap of §17.6.2 in a live case. https://share.transistor.fm/s/b845e0e3
  - **"Kieran Goodwin – Private Credit Concerns (EP.494)"** (*Capital Allocators*, 2026-03-30). A Saba Capital partner on private credit's rapid growth, asset-liability mismatches, pricing marks, leverage, liquidity and the potential for reflexive problems, and on how he positions for them: the run mechanics of §17.6 from a firm that trades the discounts. https://www.capitalallocators.com/podcast/private-credit-concerns/
  - **"BDC Veteran Expects Private Credit Fund Stress as Banks Pull Back"** (*The Credit Edge*, 2026-03-19). SLR Investment's co-CEO Michael Gross on banks getting nervous and pulling back at a time when BDCs were already reeling from a wave of redemptions, which raises everyone's cost of capital: the bank-line leg of a semi-liquid fund's liquidity runway. https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/bdc-veteran-expects-private-credit-fund-stress-as-banks-pull-back
  - **"HarbourVest Expects Private Credit Secondaries Volume to Double"** (*The Credit Edge*, 2026-05-07). Greg Ciesielski, HarbourVest's head of credit secondaries: "run-rating above \$50 billion" for the year and "a buyer's market" (his words): the secondary bid is the other exit when a redemption queue is capped. https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/harbourvest-expects-private-credit-secondaries-volume-to-double
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

*(The walk-through and dialogue are fictional; the facts about each source are from the releases, filings and fund pages cited.)*

Appendix B's data atlas has a page for private credit now, and Theo's job on a Thursday afternoon is to wire it into the desk's screens. Mags sits beside him for the whole of it, which she describes as supervision and everyone else describes as heckling. He takes the five sources in the order a trader meets them, and she makes him say out loud what each one measures before he is allowed to give it a column.

The first is the one the desk already trades: listed BDC equity and bonds. "Price," Theo says. "Set by people who lose money if they're wrong. On a wrapper that includes fees and leverage, so it isn't the loans' price, but it's a price." §17.3 is how the desk inverts it. Mags nods, which is the most she does for anything that is merely correct.

The second is new. Apollo extended daily pricing from its investment-grade products, on July 1, 2026, to its direct lending, asset-backed finance, multi-credit and opportunistic vehicles on October 1, 2026, with asset-level pricing from October 30. The release is careful to call the number an internal estimated fair value, "not a market-clearing price" (Apollo release, October 1, 2026). "Mark," Theo says, and types it into the label field. "A daily one."

"A daily mark is still a mark," Mags says. "It stair-steps on smaller stairs." Then, because she has been reading PIMCO's May note, she quotes Lotfi Karoui at him: "Daily pricing is not price discovery." Theo writes both sentences in the column's description, which is the closest the atlas comes to an argument.

The third is plumbing, and the most useful of the five. ICE's private credit service had issued more than 5,000 ICE IDs by March 2026, and Apollo reported more than \$30 billion of secondary trading since 2024 (same release). "Identifier," Theo says. "And a secondary market, small." Identifiers matter more than they sound. They are the join key that turns fifty BDC schedules of investments into one panel, which is what the cross-holder dispersion of §17.3 needs, and what Theo spent a Wednesday doing by hand for Medallia.

The fourth is a promise. The SPDR SSGA IG Public & Private Credit ETF, PRIV, launched in February 2025 with a 10–35% private-credit policy. At October 15, 2026 it held \$802.8 million in 363 positions, about 22.1% sourced from Apollo, and Apollo must post daily firm, executable bids on those assets and buy them back at those bids within stress-redemption limits (State Street fund page). "Bid," Theo says. "Contractual. So the smoothing problem becomes a counterparty problem: the private sleeve is worth what Apollo's bid is worth, up to the facility's limits."

Mags has the sceptic's line ready, and this time it is the regulator's. In the days around the fund's launch, SEC staff wrote (27 February 2025) that the registration statement had gone effective "without resolution of staff comments," that the as-filed Apollo agreement was redacted so heavily that its material terms were not public, and that the staff did not believe it "sufficient" for the fund's liquidity program "to rely solely on bids from Apollo." The fund's counsel replied the next day, describing the arrangement in the fund's own words: Apollo must provide three bids a day, each open for fifteen minutes, with discretion over the bid amount, and the fund "expressly contemplates situations where the bid and the Adviser's assessment of a position's value might diverge significantly." The staff answered by email that it had "no further comments." "I said we'd have killed for a firm bid," Mags says. "I didn't say one you can see for fifteen minutes. This is the part where you check who's on the other side of it."

The fifth is the only one quoted in spread. S&P Dow Jones Indices announced a CDX Financials index in early 2026, reported to contain 25 North American financial names including BDCs and private-credit managers, with trading from April 2026 (S&P DJI announcement, February 25, 2026; constituents and weights not verified for this edition). "Spread," Theo says. "Risk-neutral. The first $\mathbb{Q}$-measure instrument with private credit inside it." Mags asks how much private credit is inside it, and Theo does not know, which is the right answer; §17.9 explains why it is a worse hedge than it looks.

By five o'clock the page has five columns and five labels: price, mark, identifier, bid, spread. Mags reads it twice. "Fine," she says, which on her scale is two levels above good.

> **Trend Watch.** *From "no price" to five price sources, 2022–2026.* 2022: Man notes daily vendor pricing on 6,500 syndicated loan facilities and calls private credit "problematic from a data availability perspective" (Man p.41). February 2025: PRIV launches with a manager's firm bid on its private sleeve (State Street). March 2026: ICE passes 5,000 private-credit identifiers (Apollo release). April 2026: CDX Financials begins trading, reportedly with BDCs among its names (S&P DJI; details unverified). July 1 and October 1, 2026: Apollo daily pricing reaches investment-grade and then all credit vehicles; asset-level from October 30 (Apollo). October 16, 2026: private credit enters the Fed's Z.1 with holder-level series (Brinkman et al.). **What it means for the desk:** for the first time there are enough *public* observations of *private* marks to estimate the kernel, the gap and the lead–lag on live data rather than on CDLI back-fills. Wire each source into Appendix B's data atlas with its own measurement label: price, mark, bid or spread.

## 17.8 Systematic Approaches to Private Credit

### 17.8.1 Desk framing: four marks a year and a lot of footnotes

What can "systematic" mean for an asset that reports four times a year? Not high-frequency anything. It means a **look-through security master** built from BDC schedules of investments (every facility, every quarter, with cost, fair value, spread, lien and PIK flags) plus a set of slow, fundamental features computed on it. The corpus is research-grade: Davydiuk, Marchuk and Rosen used BDC schedule-of-investment data to show that BDC capital substitutes for bank credit after regulatory and lender-specific supply shocks ("Direct Lenders in the U.S. Middle Market," *Journal of Financial Economics* 162, 2024). Chapter 25's parser builds the table; this section says what to compute on it.

> **[SOURCE EXTRACTION]** *Bohn_Stein_Active_Credit_Portfolio_Management p.235 (fn. 11):* "it would be unusual in the private credit risk setting to have more than 10 year-end financial statements and quarterly financial statements."
>
> **Annotation.** Bohn and Stein are describing borrower-level data for private-firm default models, and the warning transfers directly to vehicle-level work: forty quarterly NAVs is a long history for a BDC, and many semi-liquid funds have fewer than twenty. Every estimate in this chapter (the kernel, the lead–lag, the hazard loadings) is a small-sample estimate, so the 2026 desk departs from single-vehicle modeling altogether. It pools across vehicles that hold the same loans, as Couts, Gonçalves and Rossi recommend; it uses purged, embargoed cross-validation with quarterly blocks (Chapter 7); and it reports intervals. The breadth of a private-credit strategy comes from the cross-section of vehicles and facilities, not from the time series of any one of them.

#### Quant-Shop Life: Forty Schedules and a Ticket

*(A fictional composite of a systematic credit asset manager in BDC earnings week. The shop, its people, its agent, its tickets and its meeting are invented; the Medallia marks and the Monroe par figures are from the 10-Q schedules behind Figure 17.4.)*

The second week of August is the week the BDCs file their second-quarter 10-Qs, and at a mid-sized systematic credit manager two floors above a dentist, it belongs to Tomasz, eleven months out of a master's program, and to the shop's coding agent, a literal-minded cousin of ROBO. Their job is the look-through security master: every facility in every schedule of investments of forty BDCs, one row per facility per quarter, ready for the Friday risk meeting.

Tuesday is downloading and parsing, and it goes fine until the names. The same loan appears as "Medallia, Inc.", as "Medallia Inc" and as "Medallia, Inc. (First Lien Term Loan)", and fewer than half the rows carry an ICE ID. The agent, asked to "match the same loan across vehicles," matches on exact borrower name and finds that seven holders of one loan are four different loans. Tomasz rewrites the request in the Spec's terms (borrower name normalized, then maturity, then spread, with the ID winning whenever there is one) and the four become one. Then the lots: three of the vehicles hold the loan in more than one lot, bought at different times, and the fair value over par has to be computed on the summed lot, not on each lot, or one vehicle shows two marks for one loan.

Wednesday is Monroe. Its par in the Medallia loan rises from \$12.7 million in March to \$15.0 million in June, in the same quarter its mark falls into the low forties. A purchase, capitalized interest, or a parsing error? The schedule does not say, and the footnotes do not settle it. Tomasz flags the point rather than guessing, which is also what the caption of Figure 17.4 does. Later the same afternoon he finds that one vehicle's 10-Q breaks a table across two pages and the parser has dropped the row that straddles the break. That facility now has a missing quarter in the middle of its history, and the frozen-mark counter has quietly started again from zero, exactly the edge case the Listing 17.2 explanation warns about. He backfills the row by hand and writes it down.

Thursday is recomputation. The cross-holder dispersion for the software bucket comes out at a different number for the first quarter than the one the shop reported in May, because two facilities that were unmatched then are matched now. Tomasz keeps both vintages, as the master's rules require, and annotates the difference.

Friday at ten, the risk meeting gets to the dispersion feature at 10:40. The head of risk asks the question every risk meeting asks: "Why is this number different from last quarter's?" Tomasz explains the matching change in two sentences, shows the old and new vintages side by side, and the meeting moves on to the next item, which is about a vendor invoice.

The week ends with one change-log entry (*name-matching rule v3: normalized name + maturity + spread; ID wins*), one new ticket (*Monroe Medallia par, Q2 2026: confirm source of increase*), and a comment on an old one about page-break parsing that has been open since before Tomasz joined. Nothing dramatic happens. That is what a working security master looks like from the inside, and it is why the features below can be computed at all.

### 17.8.2 The features worth computing

*(Ines's review and its dialogue are fictional; every figure is from the source cited beside it.)*

On the desk, the security master's output arrives as a list of candidate features, and Ines reviews it on a Friday afternoon the way she reviews a hand history: one line at a time, and nobody moves on until the line has earned its place. Theo has written six. Kaz has written the code for all six and would like to talk about none of them.

The first is **sector and AI exposure**, and Theo carries the number in with him. "About one-fifth of direct-lending loans are to software companies, and in some levered vehicles software can be more than half of NAV. That's the IMF, April." He has the Fed's May report open too, because it says something more useful than a level: public markets repriced first. Syndicated loan spreads widened, the Fed wrote, "reflecting a high concentration of leveraged loan borrowers in the software industry," before private-credit new-loan spreads "ticked up." Ines approves it as a sector factor in Chapter 9's framework, a per-vehicle software loading, and adds the caveat that will matter in §17.8.3: the public side has a software factor and the private side does not report one.

The second is **diversification**. "BDCs with more than 200 borrowers averaged a 9.5% return on equity in 2025," Theo says, "against 6.1% for those with fewer than 100. Cliffwater's data, by way of BlackRock's primer in January." Kaz suggests that this is survivorship in a better suit. Ines thinks it is scale, because scale buys both diversification and bargaining power with sponsors, and says so: scale is a factor, not a footnote. It goes in, with Kaz's objection logged as a test.

The third is **hidden default**, and it is the one Theo wanted to write. PIK interest was 7.3% of the CDLI's income in 2025 (Cliffwater, March 31, 2026). Of investments paying PIK at the end of 2025, 58.3% carried what the industry has started calling "bad PIK": PIK amended in after closing rather than agreed at origination (Lincoln International data via BlackRock's *Credit Currents* chartbook, 1H2026).

"So there's a good PIK?" Kaz asks.

"There is," Theo says. "A PIK toggle priced into the original deal is a contract term. Everyone knew it was there and charged for it. A PIK amended in after closing is a borrower who couldn't pay cash and a lender who preferred not to call it a default." He taps the feature definition. "So the whole feature is one question: what does the amendment say?" Ines points out that this is the first time his catchphrase has been converted directly into a column name, and approves it.

Mags, who has been reading over Kaz's shoulder, asks the question this feature always provokes. "Which default?" The private-credit default rate in 2026 depended on who was counting. Proskauer's index counted 2.51% in the second quarter, across 716 loans. KBRA's forward-looking rate was 3.5% in August. A Moody's analysis of middle-market CLO obligors counted 4.0%, or 5.8% once PIK amendments and extensions were included. Fitch's rate was reported at 6.3% in August, with PIK and deferrals 47% of its events. PIMCO's shadow default rate for BDC loans was about 19% at the end of March. "None of them is wrong," Mags says. "It's a menu. It's the same menu as the LMT chapters, moved into a market with no docket." Theo writes the basis of each number into the feature's metadata, the way a bond price carries a day count.

The fourth is **mark quality**, and it is already built: the stale-mark share and the cross-holder dispersion of §17.3, and the gap series $g_t$. Tomasz's week, a few pages back, is what it costs. Ines approves it without discussion, which Kaz takes as the highest praise available.

The fifth is the desk motto with a citation attached: **net-of-fee reality**. Private debt funds' net-of-fee abnormal returns are statistically insignificant; gross alpha is positive, and so is alpha against a debt-only benchmark, which reflects embedded equity risk (Erel, Flanagan and Weisbach, NBER w32278, 2024). "IDO or it didn't happen," she says. "Strip the leveraged-loan beta, the rates and the equity-like tail before you call anything alpha. If what's left is zero after fees, the feature is telling you the product, not the loans."

The sixth is **collateral uniqueness**, and nobody on the desk likes it, because it is not a statistic. The unit-sum constraint of §17.2 says the marks eventually catch up; it fails when the collateral was never there. First Brands (Chapter 11, September 2025), Tricolor and the UK lender Market Financial Solutions were all accompanied by allegations that receivables or loans had been pledged to more than one lender (press and court reports; amounts not verified for this edition, and allegations only). The dealer seat learned this through an affiliate rather than a trading book: Jefferies' Point Bonita fund had bought First Brands receivables, and its chief executive, Rich Handler, said "we believe we were defrauded." On JPMorgan's earnings call of 14 October 2025, after a \$170 million write-off on Tricolor, Jamie Dimon said that when you see one cockroach there are probably more, a sentence that arguably did more to retail investors' beliefs about $m$ than any default statistic. No smoothing kernel catches a double pledge. A UCC lien-overlap check and a flag for receivables bought off-platform do, and Ines approves the feature on the grounds that the cheapest time to run a lien search is before the cockroach.

By six the list has six approved features and one logged objection. Kaz asks whether they can now talk about the regression. Ines says yes, next section.

### 17.8.3 Derivation: what the public data already knows about the next marks

> **Math, Gently.** *How much weather hasn't reached the dial yet?* Go back to the porch thermometer of §17.2.2, the one that shows half of a change today, three-tenths tomorrow and the last fifth the day after. Ask it a new question: of the weather of the last two days, how much has not yet shown on the dial? For today's change, the dial has shown half, so half is still to come. For yesterday's, it has shown half plus three-tenths, so a fifth is still to come. For anything older, nothing: it has all arrived. Those leftovers, 0.5 and 0.2, are the *cumulative* weights still owed, each one the sum of the kernel's later entries. Now make it a loan book with a beta of $\beta$ to the loan index. If the index fell 3% this quarter and 2% last quarter, the marks still owe $\beta\,(0.5\times-3\%+0.2\times-2\%)=-1.9\%\times\beta$. That number is known today, from public prices, before any valuation committee meets. The full version is next.

The chapter's main engine combines §17.2 and §17.3. The **pending mark** $\Pi_t$ is the box's leftover arithmetic for a whole book: $\beta$ times the public factor's recent returns, each weighted by the share of the kernel the marks have not yet recognized. With $\theta=(0.5,0.3,0.2)$, $\Pi_t=\beta(0.5F_t+0.2F_{t-1})$. If the loan index fell 4% this quarter and was flat last quarter, a unit-beta book still has 2% of markdowns to come. The derivation is short and comes next; the signal built on it, and the judgment about when to trust it, follow.

#### The Full Derivation

Under the smoothing model, the true value change through quarter $t$ is $\beta\sum_{s\le t}F_s$ (ignoring the idiosyncratic part, which has mean zero), and the marks through $t$ have recognized $\beta\sum_{s\le t}F_s\sum_{k=0}^{t-s}\theta_k$ of it. The difference is the **pending mark**:

$$
\Pi_t=\beta\sum_{s\le t}F_s\Big(1-\sum_{k=0}^{t-s}\theta_k\Big)=\beta\sum_{j=0}^{K-1}\bar\Theta_{j+1}\,F_{t-j},
\qquad \bar\Theta_{j}\equiv\sum_{k=j}^{K}\theta_k ,
$$

using $j=t-s$ and the unit-sum constraint, so that $1-\sum_{k=0}^{j}\theta_k=\bar\Theta_{j+1}$. $\Pi_t$ is the sum of all future reported returns already implied by public factor returns, known at $t$.

#### The mark-gap signal

The **mark-gap signal** compares that mechanical catch-up with what the listed price implies:

$$
G_{i,t}=m_{i,t}-\max\!\big(0,-\Pi_{i,t}\big).
$$

When $G_{i,t}>0$, the price discounts more than the public data says the marks will fall: either the market knows something about this book beyond its beta (high software share, bad PIK, stale marks), or it is overreacting. The cross-sectional regression of $G$ on the §17.8.2 features separates the two, and the residual is the relative-value signal. When $G_{i,t}<0$, the price has not caught up with marks that are coming, which is the cleanest short in the book.

Kaz runs the pending mark across the listed BDCs on a Monday and brings Ines a ranked list. Theo looks at the top of it and then at the bottom, and stops at a vehicle with half its book in software, whose pending mark is almost exactly zero.

"That can't be right," he says. "Software equities fell thirty percent between October and February. If anything has markdowns coming, it's this one."

"It's right for the factor I gave it," Kaz says. "The pending mark is beta times the leveraged loan index's recent returns, and the loan index is mostly not software, so a software shock shows up in it diluted. Not much fell, so not much is pending." A pause, of the kind the desk has learned to recognize. "The right factor for this book is a software-loan index, and there isn't one. So I used the loan index, and the forecast is biased toward zero for exactly the vehicles where it matters most."

Ines draws the line where she always does, at the point where the tool's assumptions stop being true. The pending mark earns its place where the kernel's interval is narrow, which in practice means the pooled co-holder estimate of §17.2.4 rather than one vehicle's 28 quarters, and where the public factor matches the book's sector. Elsewhere it is a floor on the markdown, not an estimate of it, which is why $G$ uses $\max(0,-\Pi)$ and why the software loading sits beside it as a feature in the cross-sectional regression. "When the factor's wrong," Mags says, "the model is a very precise way of saying nothing has happened."

Kaz's Monday ranking came out of Listing 17.5, which is the two displayed equations in code: `pending_mark` normalizes the kernel, builds the tail sums $\bar\Theta_{j+1}$ and dots them with the latest $K$ factor returns, while `mark_gap_signal` subtracts that catch-up from the markdown that `implied_markdown` (Listing 17.2) reads off the price, and its checks reproduce the 2% pending mark and confirm that a single shock's later reported returns sum to exactly that figure. The function raises unless you pass exactly $K$ factor returns, but it cannot check that they are newest first; reverse them and you get a plausible, wrong number.

*The full listing is [Listing 17.5 in Appendix F](#code-17-5).*

### Deep-Dive Resource Graph

- **Podcasts:**
  - **"Decoding the software lending shock in private credit with MSCI"** (*Cloud 9fin*, 2026-04-03). Anna Russi with Patrick Warren, MSCI's head of private credit research, on new data showing stress in software lending and venture debt and how valuation marks "could be masking underlying pressures": the data-vendor view of the sector-exposure feature of §17.8.2. https://share.transistor.fm/s/3914343b
  - **"Bain Sees Software Debt Defaults Spiking"** (*The Credit Edge*, 2026-02-26). Bain Capital's Angelo Rufino expects software default rates could reach double digits as AI disruption spreads and loans come due (a forecast, not a measurement): the downside scenario to run through a per-vehicle software loading. https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/bain-sees-software-debt-defaults-spiking
  - **"Acadian Sees Quants Moving to Loans, CLOs"** (*The Credit Edge*, 2026-02-19). Scott Richardson, Acadian's director of systematic credit, on taking an issuer approach to leveraged loans and structured credit, plus alternative data and private credit: a quant manager's answer to the question §17.8.1 opens with, what "systematic" can mean here. https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/acadian-sees-quants-moving-to-loans-clos
  - **"Frisky Dentists"** (*Money Stuff: The Podcast*, 2026-05-15). One of several topics in Levine and Greifeld's conversation is trading private credit and daily pricing (the feed also lists CLOs and structured-finance innovations): the conversation behind the new daily-pricing data discussed in §17.7, to hear beside the Apollo release listed below. https://omny.fm/shows/money-stuff-the-podcast/frisky-dentists
- **Academic Papers:** Davydiuk, Marchuk and Rosen, "Direct Lenders in the U.S. Middle Market," *Journal of Financial Economics* 162 (2024), DOI 10.1016/j.jfineco.2024.103946; Erel, Flanagan and Weisbach, "Risk-Adjusting the Returns to Private Debt Funds" (NBER w32278), https://www.nber.org/papers/w32278
- **Practitioner Writing:** BlackRock, *Credit Currents* private credit chartbook (1H2026), https://www.blackrock.com/gls-download/literature/market-commentary/1h2026-credit-currents-chartbook-stamped.pdf
- **Data & Code:** Apollo daily pricing release (Oct 1, 2026), https://www.apollo.com/insights-news/pressreleases/2026/10/apollo-expands-daily-pricing-to-all-credit-assets-advancing-transparency-in-private-credit-3372805 ; State Street PRIV fund page, https://www.ssga.com/us/en/intermediary/etfs/spdr-ssga-ig-public-private-credit-etf-priv

## 17.9 What a Public-Markets Quant Desk Can Arbitrage

You cannot buy the loans. You can trade every public instrument whose price is a function of private marks, and by now each row of the menu below has a story behind it. Long Scene 1 earned three of them: the BDC equity relative-value row (with the Medallia ledger's dispersion as its signal), the BDC capital-structure row that Theo's November card was early to, and the event-driven row that read a NAV-for-NAV exchange ratio as a statement about the marks. Long Scene 2 earned the gate-driven selling row, and its ending, forced selling absorbed at par by pension and insurance buyers, is why the insurer-rotation row sits beside it. Finastra and Pluralsight earned the takeout-supply row, from both doors. The two rows in between, the index-versus-basket and wrapper rows, came out of Theo's afternoon with the data atlas in §17.7.2. Here is the menu, with the signal from this chapter that drives each one:

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

- **Podcasts:**
  - **"Boaz Weinstein"** (*Money Stuff: The Podcast*, 2026-03-19). Matt Levine and Katie Greifeld with Saba Capital's Boaz Weinstein on his tenders for OBDC II and SREIT, semi-liquid fund liquidity, public versus private BDC discounts and "volatility laundering": the practitioner statement of what a listed-leg desk can trade, and the first row of the menu above. https://omny.fm/shows/money-stuff-the-podcast/boaz-weinstein
  - **"The Apollo ETF Landing"** (*Trillions*, 2024-09-26). Eric Balchunas and Joel Weber with Bloomberg's Vildana Hajric on the State Street and Apollo filing, why more filings were expected and what Apollo's "liquidity backstop" is: the origin of the wrapper premium/discount row. https://omny.fm/shows/trillions/the-apollo-etf-landing
  - **"Funny Business Is My Business: PRIV, HHH, WARS"** (*Money Stuff: The Podcast*, 2025-02-28). Levine and Greifeld on the launch of Apollo and State Street's private credit exchange-traded fund; read it with the State Street PRIV page listed below. https://omny.fm/shows/money-stuff-the-podcast/funny-business-is-my-business-priv-hhh-wars
  - **"Janus Is Skeptical of Private Credit's Push Into ETFs"** (*The Credit Edge*, 2025-04-03). John Kerschner of Janus Henderson: "The underlying isn't nearly as liquid and hasn't really been tested throughout a real dislocation credit cycle": the sceptic's case against the wrapper row, a liquid shell around an underlying that has not yet been through a dislocation. https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/janus-is-skeptical-of-private-credit-s-push-into-etfs
- **Academic Papers:** Avalos, Doerr and Pinter, "The Global Drivers of Private Credit," *BIS Quarterly Review* (Mar 2025), https://www.bis.org/publications/qr-202503/global-drivers-private-credit
- **Data & Code:** FINRA TRACE for BDC unsecured bond prints, https://www.finra.org ; SEC EDGAR for 8-K and Schedule TO filings, https://www.sec.gov/edgar

## 17.10 Desk Debrief

**Finder.** One row per tool: where its equation lives, the picture that explains it, the scene that shows when it works and when it breaks, and its listing.

| Concept | Equation | Intuition | Judgment (scene) | Code |
| :--- | :--- | :--- | :--- | :--- |
| Smoothing kernel | $x^o_t=\sum_k\theta_k x_{t-k}$; variance, autocorrelation, Sharpe and beta, §17.2.2 | The porch thermometer and the squares; footprints in snow (boxes) | The cold open's "N/A"; Desk Myth vs. Desk Reality (§17.2.2) | [Listing 17.1](#code-17-1) |
| Dimson sum | $\hat\beta^{\text{agg}}=\sum_k\hat b_k$, $\hat\theta_k=\hat b_k/\sum_l\hat b_l$, §17.2.3 | Summing the canyon's echoes (box) | Kaz's first Dimson run: OLS against HAC, and the valuer who changed (§17.2.3) | [Listing 17.1](#code-17-1) |
| Unsmoothing | Geltner inversion; noise $\times(1+\theta^2)/(1-\theta)^2$, §17.2.4 | The cassette hiss (box) | The quarter Kaz unsmoothed one fund (§17.2.4) | [Listing 17.1](#code-17-1) |
| Implied markdown | $m=\big((1-\phi)-P/\text{NAV}\big)/(1+\ell)$, §17.3.2 | The thin slice (box) | Long Scene 1: four prices for the same loans (§17.3) | [Listing 17.2](#code-17-2) |
| Non-accrual gap | $\hat R^{\text{mark}}_{\text{NA}}=(w^{FV}/w^{C})(FV/C)$ and $g_t$, §17.3.3 | Bruised loans in the bowl (box) | The Medallia ledger (§17.3.3); Pluralsight's dispersion flag (§17.4) | [Listing 17.2](#code-17-2) |
| Competing exits | $\frac{\kappa^{(B)}}{\mathcal{K}}\big(1-e^{-\mathcal{K}\Delta t}\big)$ and $Q^{P\to B}$, §17.4.2 | A room with three doors (box) | Theo's dual track (§17.4.2); Finastra and Pluralsight (§17.4) | [Listing 17.3](#code-17-3) |
| Redemption transfer | $N^{\text{true}}_{\text{stay}}=N\big((1-m)-p_t\big)/(1-p_t)$, §17.6.2 | The pizza (box, Part 1); the mirror (Poker Table) | Long Scene 2, the 23 June card (§17.6) | [Listing 17.4](#code-17-4) |
| Backlog and runway | Backlog recursion and $\mathcal{T}$, §17.6.2 | The line that refills (box, Part 2) | Long Scene 2, the resubmissions; "depends on the borrowing base" (§17.6) | [Listing 17.4](#code-17-4) |
| Pending mark and mark gap | $\Pi_t=\beta\sum_j\bar\Theta_{j+1}F_{t-j}$ and $G_{i,t}$, §17.8.3 | Weather the dial still owes (box) | Kaz's Monday ranking and the software factor that does not exist (§17.8.3) | [Listing 17.5](#code-17-5) |

Then the cold open's cards come face up, at last, and Ines replays the hand. The desk bid the \$25mm of notes two points back of the screen and hedged half the risk with a short in the BDC's own equity, on the view that the seller knew about the redemption queue at a sibling-type vehicle and the equity would reprice before the bonds. The markouts said they were right about the direction and wrong about the ratio: the equity fell more than the bonds, as the capital-structure algebra predicts when the debt is money-good. The hand history goes in the file. *(The trade is illustrative.)*

Mags's one line, it turns out, was the desk's trade. The other two cards are worth reading out, because of where their authors started. Kaz's said *bid close to the screen, all \$25mm, hedge with the loan index*, because at 4:41 on the replay's clock Kaz still thought a NAV was a price that happened to be published slowly. Theo's said *no bid*, because he thought a NAV was a lie with a fee attached. Neither is what the desk did, and neither is where they ended the chapter. Theo takes the sticky note down from the whiteboard, *whose number is it?*, and writes the answer under it in the small capitals he used to use for defined terms: *a slow signal; measure the speed.* Kaz, reading over his shoulder, adds the kernel, $\theta=(0.5,0.3,0.2)$, and an interval. Ines says nothing, which on this desk is how you know a hand was played correctly.

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

- **Podcasts:**
  - **"What's Actually Going On With Private Credit"** (*Odd Lots*, 2026-04-27). Osterweis portfolio managers John Sheehan and Craig Manchuck on the history of private credit before and after 2008, its links with private equity and insurance, the prospect of higher defaults and what to watch for now: the one-episode primer for the whole chapter. https://omny.fm/shows/odd-lots/whats-actually-going-on-with-private-credit
  - **"How Banks and Private Credit Became the Best of Frenemies"** (*Odd Lots*, 2024-10-24). Huw van Steenis of Oliver Wyman on the bank–private credit relationship that §17.5 maps. https://omny.fm/shows/odd-lots/102424-odd-lots-huw-van-steenis-master-3
  - **"Howard Marks – Navigating Private Credit (EP.439)"** (*Capital Allocators*, 2025-04-07). Marks on the rise of private credit and the pendulum swings in investor sentiment, with themes from his memo "Gimme Credit": the allocator's long-cycle frame, a year before the April 2026 memo listed below. https://www.capitalallocators.com/podcast/navigating-private-credit/
  - **"Kieran Goodwin – Private Credit Concerns (EP.494)"** (*Capital Allocators*, 2026-03-30). A Saba Capital partner on growth, asset-liability mismatches, pricing marks, leverage, liquidity and reflexive problems in private credit: the risk checklist of a firm that trades the BDC discounts (§17.6, §17.9). https://www.capitalallocators.com/podcast/private-credit-concerns/
  - **"Jeff Rosenberg - The Past, Present, and Future of Systematic Fixed Income (S7E19)"** (*Flirting with Models*, 2025-08-18). BlackRock Systematic Fixed Income on why factor investing exists mainly in credit and why "characteristic specificity" matters in fixed income: the systematic baseline for the feature work of §17.8. https://www.flirtingwithmodels.com/episodes/8V74zBaN4jN
  - **"Oaktree Says Boring is Beautiful In Dicey Private Credit Market"** (*The Credit Edge*, 2026-06-11). A special episode recorded June 3 at Bloomberg's Global Credit Forum: private lenders going "back to basics" as debt trouble spreads, with guests on AI debt risks and software distress. https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/oaktree-says-boring-is-beautiful-in-dicey-private-credit-market
- **Memos and Frameworks:**
  - **"What's Going on in Private Credit?"** (Howard Marks, Oaktree memo, 2026-04-09). The long-cycle frame for the chapter: sub-investment-grade credit from the 1970s to direct lending after the GFC, the issues created by rapid deployment, and the entwined fates of direct lending and private equity. https://www.oaktreecapital.com/insights/memo/whats-going-on-in-private-credit
  - **"Multi-asset credit investing: A quantitative framework"** (Nuveen, Mark Zheng, 2025-12-19). The public form of the Nuveen multi-asset framework quoted in the Cold Open (the quotes come from the shelf copy, so check the page before citing it): more than 20 sectors from high yield to private credit, with capital-market assumptions, risk modelling and optimization. https://www.nuveen.com/global/insights/fixed-income/multi-asset-credit-investing
- **Practitioner Writing:** Asness, "The Illiquidity Discount?" (AQR, 2019), https://www.aqr.com/Insights/Perspectives/The-Illiquidity-Discount ; Octus on BDC discounts and non-accruals (Apr 16, 2026), https://octus.com/resources/blog/bdcs-trading-at-50-discount-to-nav-but-nonaccruals-ticking-downward/ ; Blue Owl Capital Corporation press releases, https://www.blueowlcapitalcorporation.com/investors/news-events/press-releases ; IMF blog, "Fast-Growing \$2 Trillion Private Credit Market Warrants Closer Watch" (Apr 8, 2024), https://www.imf.org/en/Blogs/Articles/2024/04/08/fast-growing-USD2-trillion-private-credit-market-warrants-closer-watch ; Man Group, *Quantitative Credit Alpha: Early Mover* (2022, shelf); Nuveen, *Multi-Asset Credit Quant Framework* (shelf).
- **Academic Papers:** Getmansky, Lo and Makarov (NBER w9571), https://www.nber.org/papers/w9571 ; Couts, Gonçalves and Rossi, *Review of Financial Studies* 37(7), 2024; Cai and Haque, "Private Credit: Characteristics and Risks," FEDS Note (Feb 23, 2024), https://www.federalreserve.gov/econres/notes/feds-notes/private-credit-characteristics-and-risks-20240223.html ; Block, Jang, Kaplan and Schulze (NBER w30868), https://www.nber.org/papers/w30868 ; Erel, Flanagan and Weisbach (NBER w32278), https://www.nber.org/papers/w32278 ; Ellias and de Fontenay, 134 Yale L.J. (2025), https://www.yalelawjournal.org/article/the-credit-markets-go-dark ; Davydiuk, Marchuk and Rosen, *JFE* 162 (2024).
- **Data & Code:** Federal Reserve Z.1 (private credit series FL893167205, FL453067203, FL443067205, FL673067205), https://www.federalreserve.gov/releases/z1/ ; Fed FEDS Notes index, https://www.federalreserve.gov/econres/notes/feds-notes/default.htm ; Fed *Financial Stability Report*, https://www.federalreserve.gov/publications/financial-stability-report.htm ; SEC EDGAR (schedules of investments, 8-K, Schedule TO, N-PORT), https://www.sec.gov/edgar ; NAIC private credit resource center, https://content.naic.org/resource-center/private-credit-insurance-regulation ; Cliffwater Direct Lending Index and KBRA DLD (subscription; no link).

<!-- STATUS: COMPLETE -->
