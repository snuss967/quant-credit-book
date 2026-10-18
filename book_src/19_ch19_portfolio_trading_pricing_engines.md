# Chapter 19: Portfolio Trading & Basket Pricing Engines

*Friday 23 October 2026, the end of Theo's fifth week on the desk. The desk, its client, the basket and every number on it are invented (illustrative), and so is Wexcombe Coatings, the issuer behind line 117. The market facts the chapter cites later are real and sourced.*

It is 2:58 p.m. on the Friday before a lender call, and the inquiry lands on Ines Okafor's screen with all the subtlety of a fire alarm. Client sells. One hundred and fifty lines of high yield, \$212mm of par, one price, all or none. Eight dealers in competition. Response window: three minutes.

Ines reads the ticket out loud, flatly, the way she once read a board to herself before deciding whether she was in the hand. "One-fifty lines. Two-twelve par. Eight in comp. Three minutes. Client sells, AON." The client is a high-yield manager the desk has quoted eleven times this year and beaten the field on four *(illustrative)*. All or none means what it says: the winner takes the whole list at one price, and a dealer who wants only the good lines has to say so out loud.

"What's the pot, what are the odds, and who at this table knows more than you?" Ines says, to no one and everyone. "We have ninety seconds. The other ninety are for me to change my mind."

The first thing the engine paints, before any price, is a single number in the top corner: the basket's 30-day return correlation with HYG, the big high-yield ETF the desk would sell to hedge it. It reads 0.55 *(illustrative)*. Theo has seen this number before only on investment-grade lists, where a rebalance that looks like the index scores in the eighties against LQD (§19.2 has the published average). Ines looks at the 0.55 the way she looks at a player who has just raised from early position. "This list was not built to be hedged," she says. "It was built to be sold."

Kaz has already typed `cov = np.cov(returns)` into a notebook. The matrix is 150 by 150, and each bond has fourteen observed returns. "It's singular," Kaz reports, with the calm of someone who has been here before, "but if we just assume Gaussian..."

"Why fourteen?" Theo asks.

"Fourteen weeks this quarter in which enough of these bonds printed to give me a return at all. So fourteen rows and a hundred and fifty columns." Kaz scrolls, as if more rows might be hiding below the fold. "I am asking fourteen weeks to tell me eleven thousand three hundred and twenty-five separate facts about how these bonds move together. They can't. Most of this matrix is the data saying it has no idea, in a font that looks exactly like knowing."

"Then don't let it vote," says Ines, without turning round.

"Back in my day," says Mags Dunleavy from across the aisle, not looking up, "the basket was a fax. Forty pages. Page nine was always missing, and page nine was always where they'd put the bonds they actually wanted to sell."

Theo Marsh is scrolling the list, and he does not yet know what he is looking for, which is the usual condition of his first month. He slows at line 42 before he can say why. It is \$18mm, four times the size of the lines around it, and the last-print column says eight weeks: nobody has traded it since the end of August. He writes "42: big and quiet" in the notebook and keeps going. Line 117 stops him cold. Four million of Wexcombe Coatings 8.5% notes of 2028, marked at 82. He knows that issuer. Two months ago, from his old seat, he watched its lenders hire counsel. It was not his deal; it was a headline he read twice on a Tuesday in August, and that evening he rebuilt the company's cash runway from its public filings, out of habit. There is a lender call on Monday. The 13-week cash flow model on his USB stick, the one he carries for emotional support, puts the end of the issuer's liquidity runway about a quarter out. "Before we price this," he says, "what does the credit agreement say about line 117?"

Ines looks at him for a full second, which on this desk is a long time. "That," she says, "is the right question asked in the wrong ninety seconds. Ask it faster."

"He found page nine," Mags says to her own screen.

Nobody has typed a price. The clock in the corner of the inquiry reads 2:59:05. Ines tears a sheet off the pad by her keyboard and slides it across to Theo, and the gesture is so old-fashioned that Kaz looks up from the notebook. "Write three things before 3:00," she says. "What you bid, in basis points of market value. Which lines you want back. And why." She taps the pad once. "Then I'll show you what the engine wrote, and on Friday the tape will show us both who was right."

Write yours too, before you read on. You know as much as Theo does: one number that says the basket is hard to hedge, one matrix that cannot be inverted, one big bond nobody has traded in two months, one small bond whose lenders have counsel and whose company has a call on Monday, and a client who chose to sell all of it at once on a Friday afternoon.

The question this chapter answers is the one on Ines's screen: **what is one price for 150 bonds, how do you produce it in ninety seconds, and which two lines are paying for the whole trade?**

Here is what the desk will need in the next ninety seconds, in the order it will need it. It needs a way to write the basket bid as a certainty equivalent with four terms (fair value, liquidation cost, residual risk after the hedge, and adverse selection) and to see why a margin sits on top. It needs the per-line liquidation cost from a liquidity score at the line's real size, computed without the junior quant's habit of counting duration twice. It needs to collapse 150 lines into one hedgeable lump plus a residual, and to build a residual covariance for bonds that barely trade that is not lying to it. It needs an eviction loop that tells the client which lines to take back, a stress mode that turns one dial for liquidity, risk and basis together when the market seizes, and a way to find the mystery box, the line the client knows something about, before the desk owns it. Along the way it will replay two real stretches of tape, the 2022 reversal and the March 2020 and April 2025 stresses, and meet a pod whose short basket is nothing but the residual. And because the other side of the screen has a choice too, the chapter ends on the buy side's version of the same arithmetic: when the portfolio-trade premium is worth paying, decided as a calculation rather than a mood. The tape settles Theo's card a week from today.

## 19.1 What a Portfolio Trade Is (and Isn't)

A list RFQ is a buffet. A portfolio trade is a tasting menu: you eat the beet course or you go home. That one sentence carries most of the economics. In a list RFQ each line is priced separately, so every dealer bids the lines it likes, and the client's leftover is whatever nobody wanted. In a portfolio trade (PT), the client sends the list (identifiers, sides, sizes) to a handful of dealers. Each dealer returns one price for the whole basket, usually as a spread or a price-level concession against a reference composite. The winner takes every line as a single piece of risk. Nothing is cherry-picked. In 2019 roughly eight to ten dealers could price a basket this way, against the 70 to 80 that answered single-bond RFQs (The DESK, 2019-10-06, "The burgeoning portfolio trading business").

Later that afternoon, with the response gone and the screens quiet, Ines pulls the ticket back up and walks Theo through the parts he had no time to read. She starts at the top right, at a field that says `SPOT 15:00`.

"We agree a spread now and convert at three," she says, "so the rate leg is somebody else's problem." Spotting is the convention that makes a basket quote possible at all. The two sides agree a spread at, say, 13:30 and convert it to prices at 15:00, and the Treasury hedges on the rate leg are netted at the same moment, so neither side is paid or punished for what the ten-year did in the meantime. Spotting clusters at 15:00, 15:30 and 16:00 (Meli & Todorova, 2023, "Portfolio Trading in Corporate Bond Markets"). Theo's version is the one he would have used at PJT: the deal prices off a reference rate that gets fixed later, and nobody argues about the fixing. Ines's version is shorter. The engine prices *credit* risk and spots the rate leg separately, which is why the derivations below have no $r$ in them.

The next field is a flag the desk's trade-reporting system will set when the print goes out. Since 2023-05-15, TRACE has carried a mandatory portfolio-trade modifier for trades between two parties covering at least ten unique issues at a single basket price (FINRA Regulatory Notice 22-12). FINRA's market-structure advisory committee had asked for a flag three years earlier, on 2020-02-10, in a version that required at least thirty issuers and all-or-none terms (The DESK, 2020-03-31). Before the flag went live, researchers had to reconstruct portfolio trades from clusters of identical timestamps, so Ines treats every pre-2023 PT statistic as an estimate of a thing nobody could see directly. "If someone shows you a 2021 PT number to one decimal place," she says, "ask them how they found the baskets."

Then she scrolls to the list itself, and the conversation turns to what an ordinary basket looks like, because this one is not ordinary. The average PT that Barclays identified in 2021 TRACE had about 100 line items and about \$70mm notional, spread fairly evenly across bonds (The DESK, 2022-06-01, reporting Meli, Todorova, Mittal and Kelleher). Li's 2018 sample averages 112 unique CUSIPs from 80 issuers and \$57.9mm notional. About a third of her baskets mix dealer-buy and dealer-sell lines, and most mix IG and HY (Li, 2022, "Frictional Intermediation, Inventory Hedging, and the Rise of Portfolio Trading in the Corporate Bond Market"). Goldman Sachs, on a Coalition Greenwich webinar in January 2024, was credited with about 8,000 portfolio trades for more than 300 clients in 2023, averaging roughly \$60mm across about 100 CUSIPs (Greenwich's summary of the session). So the engine has to accept signed notionals, buys and sells in one list, and the cold open's one-sided, all-HY, \$212mm basket sits at the large and nasty end of the distribution. "Twice the usual size," Ines says, "all one way, all junk, on a Friday. Nobody sends that to be nice to us."

"Who does send them?" Theo asks.

The Federal Reserve asked the dealers. In its June 2025 Senior Credit Officer Opinion Survey (SCOOS), every active dealer said high-grade bonds frequently appear in baskets, and three-fifths said the same of high yield.

> **View From Another Seat.** *The insurer and the pension fund.* In the June 2025 SCOOS, about three-fifths of dealers active in credit portfolio trading named insurers and pensions or endowments as *frequent* users of the protocol. More than four-fifths pointed to ETF managers and mutual funds, and about three-quarters to hedge funds, as occasional or frequent users. The liability-driven seat explains the first answer. A pension's credit sleeve is rebalanced against a liability schedule, and the rebalance has to be complete on a date: a new duration target after a funding-ratio change, a transition between managers, a quarter-end that the trustees will read. To that seat a half-filled list is not a discount; it is an unhedged gap against the liabilities that it then has to explain. Paying a few basis points for all-or-none is buying a completion date, and the dealer who wins the basket is selling one. From this chair the price of the PT is not judged against each bond's best bid. It is judged against the cost of being 40% done on the day the hedge was due.

What a PT is not: it is not a list RFQ (above), and it is not an ETF creation or redemption, though the dealer may end up delivering part of the basket into one (Chapter 20). It is closest to the equity "risk bid" on a program trade: one price for a bundle, set by a dealer who means to hedge the bundle's market exposure and live with the rest.

> **[SOURCE EXTRACTION]** *Man_Revolutions_in_Credit_Trading_2023 p.2:* "2021 then became, in our view, the year of portfolio trading (Figure 2). We found that orders attracted high fill rates as competition for trades proliferated, not only among what we would consider tier-one counterparties but also those in the second tier, with aggressive pricing offered."
>
> **Annotation.** Read it as a statement about the *margin* term, not the cost terms. In the master equation of §19.2, a dealer's bid is its reservation price minus a margin $\pi$, and in a first-price auction among eight dealers $\pi$ is set by competition. The 2021 boom was second-tier dealers buying market share by bidding $\pi$ toward zero, and in some cases below the true reservation price. Man's next page (§19.6) records what happened in 2022 when they stopped. The modern desk's lesson: a PT hit rate is a function of your $\pi$ *and everyone else's balance sheet*. If you are winning everything, check whether you are the cheapest dealer or the most optimistic one. Those are different businesses, and only one survives the winner's curse (Chapter 18).

"So the basket is the cheap way to trade," Theo says, and Ines makes the face she makes when a player shows down a hand that was only good on the flop. "For some bonds. Ask which ones."

> **Desk Myth vs. Desk Reality.** *Myth:* PTs are always cheaper than trading the lines one by one. *Reality:* they are cheaper *for the bonds that go into them*. Meli & Todorova find a PT line costs 6.0bp less than the same bond traded by RFQ, against an average RFQ effective half-spread of 14.5bp: a 41.7% saving, rising to 55.2% (8bp) for illiquid bonds and falling to 19.3% (2.8bp) for liquid ones. Yet Man Numeric moved most of its flow back to electronic RFQ in 2022–23 and reports "significant savings in transaction costs versus portfolio trades" (Man_Revolutions_in_Credit_Trading_2023 p.5). Both are true. The PT saving is largest exactly where single-line RFQs work worst. For a book of liquid lines with a high electronic fill rate, the certainty you buy with a PT costs more than it is worth. §19.9 turns this into an inequality.

Theo's next question is how big the thing he has just walked into actually is, and the answer depends, as it always does in this market, on what you divide by.

> **Trend Watch: the basket protocol, 2018–2026.** *What changed:* PT went from a curiosity to standard risk-transfer plumbing. *How big:* about 1% of IG volume in 2018 and 7% in 2021 (Meli & Todorova, December 2023 version). PT was a record 5.4% of US corporate transactions in January 2021, against 2.2% a year earlier (Tradeweb data via IFR, 2021). Barclays' own PT desk went from "virtually zero" in 2018 to more than 2,000 inquiries and \$175bn in 2021, with PT about 8% of US credit volume by mid-2022 (The DESK, 2022-06-01). In 2024 PT was about 10% of IG and 8% of HY volume, and electronic PT averaged \$3.3bn a day, up 76% (Coalition Greenwich, January 2025). In March 2025 about 25% of institutionally sized US IG risk trades went via PT, up from just over 20% in January (Bloomberg *Market Dialogues*, 2025-07-07). PT was 12% of the \$89.7bn traded on 2025-04-08 (Coalition Greenwich, citing Trumid) and 18% of the \$84.7bn traded on 2025-09-30, which Coalition Greenwich's 2025 review lists as the record day. (The two "record" claims rest on different volume definitions. Chapter 22 untangles them.) The platform race is now a PT race. MarketAxess held about 13% of electronic PT in 2024, against Tradeweb's more than two-thirds (Coalition Greenwich, January 2025). It reported an estimated 20.9% share of US credit portfolio trading in January 2026 and 22.0% in May 2026 (MarketAxess monthly volume releases). *Dealer side:* nearly two-thirds of SCOOS dealers are active in PT, four-fifths of those increased PT provision after January 2023, and about four-fifths expect to do more (SCOOS, June 2025). *What it means for the desk:* PT share depends on the denominator (share of TRACE volume, about 10–18%, versus share of institutional risk trades, about 25%). Whoever owns the basket engine sets the marginal price of IG risk transfer, and increasingly HY.

## 19.2 The Master Equation: Four Terms, One Price

Back at 2:59:20, Theo is staring at the blank card, and the honest thing he could write on it is "I don't know how to price 150 bonds in a minute." Ines reads that over his shoulder without his writing it. "You do not own 150 bonds," she tells him. "You own one ETF you can't sell and 150 small arguments." Here is the first aha for the ex-RSSG reader. **The dealer is not pricing 150 bonds. The dealer is pricing one ETF-shaped lump plus a residual, and the residual is where everything you learned at PJT lives.** On an ordinary investment-grade list the lump is most of the basket. Meli & Todorova find that the average IG PT has a 30-day return correlation of 0.85 with LQD, and on average 60% of its bonds are held by LQD, even though LQD holds only about 30% of index bonds. That lump can be hedged in the same minute with ETF shares, index CDS, total return swaps or credit futures (§19.4). Today's 0.55 says the lump is smaller and the arguments are louder. What cannot be hedged is the 12 off-index lines, the two names with ad hoc groups forming, and the \$18mm line in a bond that last printed eight weeks ago. Math PhDs price the lump well. The reader prices the residual well. This chapter's job is to put both in one engine, and the engine starts from a question every dealer answers by instinct: how much would you pay not to own the risk?

> **Math, Gently.** *The certainty equivalent, or the price of not flipping.* Chapter 1 (§1.3.1) introduced the certainty equivalent as the sure amount you would swap a bag of outcomes for. Here is the same idea as a coin. Someone offers you a fair coin: heads you win \$1mm, tails you lose \$1mm. Its average is zero, and you would still pay something to walk away, because losing a million on a Friday hurts more than winning one helps. How much you would pay is your *risk aversion*, written $\gamma$, in units of "per dollar." A dealer whose $\gamma$ is $2\times10^{-7}$ per dollar charges $\tfrac12\gamma\sigma^2$ to hold a bet whose standard deviation is $\sigma$. With $\sigma=\$1\text{mm}$ that is $\tfrac12\times2\times10^{-7}\times(10^6)^2=\$100\text{k}$. So a bid \$100k below fair value is not meanness; it is the price of not flipping. Double the coin to \$2mm and the charge quadruples to \$400k, because risk is charged on the *square* of the size. The engine in this chapter runs at $\gamma=10^{-6}$ for high-yield baskets, five times as nervous, and at that setting the original \$1mm coin costs \$500k to hold. The four terms of the master equation are this coin with three more things attached, and the full version is next.

### 19.2.1 Derivation: the basket bid as a certainty equivalent

Kaz turns the coin into a basket on the whiteboard after the close, because Theo asked how the engine got its number and Kaz cannot answer a question like that without a marker. The board starts with one letter, $W$, the desk's profit or loss on the basket by the time it has been worked out of, and a picture of what $W$ might look like. The picture comes first because the formula is only as good as the shape it assumes.

> **Math, Gently.** *A week as a histogram, and the trapdoor in it.* (a) Chapter 5 (§5.1.1) drew a bond's year as a deck of cards. For a dealer the natural unit is the week: rerun next week a thousand times, write down the P&L each time, and stack the results into a histogram. That histogram *is* the distribution. The **normal** distribution is the bell you get when many small, independent pushes add up, and most weeks of most bonds look like a narrow bell. A bond with a lender call on Monday looks like a narrow bell with a trapdoor in the floor. Try it with a hundred days: ninety-nine quiet days of plus or minus 0.3 points and one day of minus 15. The mean is $-0.15$ points and the standard deviation about 1.5. Now draw a bell with that mean and width. It puts the 15-point day ten standard deviations out, an event too rare to happen in the life of the universe; the data say once in a hundred days. The bell got the width right and the shape wrong, because it spreads the trapdoor's risk evenly on both sides, as if a 15-point *gain* were just as likely. (b) The lopsidedness has its own number, the third cumulant $\kappa_3$, which is the skew in units of size cubed. For the bell it is zero. For the trapdoor bond it is about $-33$ cubic points, a skewness near $-9$ (Chapter 5, §5.1.3, has why credit is skewed by construction). Mean–variance stops at the second cumulant, so it charges for width and not for lopsidedness. That is the negative $\kappa_3$ in Step 2 below, and §19.8 puts it back into the price as a mean.

"For a hundred and forty-eight of these lines the bell is fine," Kaz says, a little defensively, as if the trapdoor were a personal remark. "It's the other two." Ines, passing with her coat on, asks the question that decides which bell. "Whose probabilities are you drawing it with? Ours, or the CDS market's?"

Kaz knows this one cold, which is half the problem. Chapter 5 (§5.1.1) and Chapter 6 (§6.2.2) build both kinds of probability in full. One is a weather forecast: how often, in the real world, do companies like this one default? That is $\mathbb{P}$, the physical measure. The other is an insurance price: what default probability does the CDS market charge for protection? That is $\mathbb{Q}$, the risk-neutral measure, and it runs higher because insurers charge for the fact that defaults arrive in clusters, in bad years, when everyone's other losses arrive too. For a single-B name the forecast might say 2% over five years while the CDS spread implies 5% *(illustrative)*; the gap is the market's price for bearing the risk. "We hold this for five days," Ines says. "I care what will happen, not what insurance costs. If you compute the expected P&L with the insurance price and *then* subtract our own risk charge, you've charged for the risk twice, once inside the probability and once outside it." This chapter is full of things charged twice by accident (duration in §19.3, variance in the same place); this is the first. So every expectation in this chapter is under the physical measure $\mathbb{P}$. The dealer is pricing its own P&L over a few days, not replicating a claim. ROBO, left alone, will discount at $r$ under $\mathbb{Q}$ and call it rigor.

The derivation below turns the coin into a basket. Its first result, equation (19.1), says that the most a dealer will pay for the basket is its fair value, less its liquidation cost, less the coin's risk charge $\tfrac12\gamma\,\mathbf{x}^\top\Sigma_T\mathbf{x}$ written for 150 bonds at once. Its second, the master equation (19.2), replaces the full covariance with what is left after the hedge, subtracts a charge for the mystery box, and subtracts a margin for the seven other dealers in the auction.

#### The Full Derivation

*Setup.* Let $\mathbf{x}\in\mathbb{R}^N$ be the signed par notional of the basket $\mathcal{B}$, in dollars, with $x_i>0$ meaning the dealer buys line $i$ (the client sells). The dealer pays $p_i$ per unit of par, holds and unwinds over a horizon of $T$ business days, and line $i$ is worth $\widetilde P_{i,T}$ (fraction of par) at the end. Liquidation costs total $C^{\text{liq}}(\mathbf{x})$ dollars. Terminal P&L is

$$
W \;=\; \sum_{i=1}^{N} x_i\big(\widetilde P_{i,T}-p_i\big)\;-\;C^{\text{liq}}(\mathbf{x}).
$$

*Assumptions.* (i) The composite mid is unbiased over the horizon: $\mathbb{E}^{\mathbb{P}}[\widetilde P_{i,T}\mid\mathcal{F}_t]=\widehat P_i$. The rate leg is spotted and hedged, and carry is second order for $T\le 10$ days. (ii) $\operatorname{Cov}^{\mathbb{P}}(\widetilde{\mathbf P}_T\mid\mathcal{F}_t)=\Sigma_T$, measured in (fraction of par)$^2$ over the horizon. (iii) The dealer has CARA utility $u(W)=-e^{-\gamma W}$ with absolute risk aversion $\gamma$ in units of $\$^{-1}$.

*Step 1 (certainty equivalent).* The CE is the sure amount with the same utility: $u(\text{CE})=\mathbb{E}^{\mathbb{P}}[u(W)]$, so

$$
\text{CE} \;=\; -\frac{1}{\gamma}\log \mathbb{E}^{\mathbb{P}}\big[e^{-\gamma W}\big].
$$

*Step 2 (cumulant expansion).* Write $\log\mathbb{E}[e^{-\gamma W}]=\sum_{n\ge1}\kappa_n(-\gamma)^n/n!$, where $\kappa_n$ are the cumulants of $W$. Then

$$
\text{CE} \;=\; \kappa_1 \;-\; \tfrac12\gamma\,\kappa_2 \;+\; \tfrac16\gamma^2\kappa_3 \;-\;\cdots
$$

For Gaussian $W$ every cumulant past the second vanishes, so $\text{CE}=\mathbb{E}[W]-\tfrac12\gamma\operatorname{Var}[W]$ exactly. Otherwise the truncation drops the skew term, and a line with jump-to-default risk has $\kappa_3<0$, which *lowers* the CE. Mean–variance therefore under-charges the line Theo is worried about. That missing term is exactly what the adverse-selection charge of §19.8 puts back.

*Step 3 (moments).* With $C^{\text{liq}}$ treated as deterministic for now (§19.7 makes it random), $\mathbb{E}[W]=\sum_i x_i(\widehat P_i-p_i)-C^{\text{liq}}(\mathbf{x})$ and $\operatorname{Var}[W]=\mathbf{x}^\top\Sigma_T\mathbf{x}$.

*Step 4 (indifference).* Write the basket's dollar price as $P^{\text{PT}}=\sum_i x_i p_i$. The dealer's reservation basket price sets $\text{CE}=0$:

$$
P^{\text{PT}}_{\text{res}} \;=\; \sum_i x_i\widehat P_i \;-\; C^{\text{liq}}(\mathbf{x}) \;-\; \tfrac12\gamma\,\mathbf{x}^\top\Sigma_T\,\mathbf{x}.
\tag{19.1}
$$

Only the *basket* price is pinned down. How the bid is split across lines is a reporting choice, which matters for best-execution files (§19.9), not an economic one.

*Step 5 (the master equation).* In §19.4 the dealer hedges and $\Sigma_T$ is replaced by the residual covariance $\Sigma^{\text{res}}_T$. In §19.8 the inclusion of informed lines adds an adverse-selection charge $\text{AS}(\mathcal{B})$. Competition subtracts a margin $\pi\ge0$:

$$
P^{\text{PT}}_{\text{bid}} \;=\; \underbrace{\sum_i x_i\widehat P_i}_{\text{fair value}} \;-\; \underbrace{\sum_i c_i(x_i)}_{\text{liquidation cost}} \;-\; \underbrace{\tfrac12\gamma\,\mathbf{x}^\top\Sigma^{\text{res}}_T\mathbf{x}}_{\text{residual risk}} \;-\; \underbrace{\text{AS}(\mathcal{B})}_{\text{mystery box}} \;-\;\pi .
\tag{19.2}
$$

With $n$ dealers in competition, the winner is the highest bidder in a first-price, common-value auction, so $\pi$ must include winner's-curse shading (the BWIC derivation in Chapter 18).

#### Reading the master equation at its edges

Ines's habit with any new equation is the one she has with a new player at the table: watch what it does at the extremes, before trusting it in the middle. With $N=1$, the risk term's gradient $\gamma(\Sigma^{\text{res}}_T\mathbf{x})_i$ is the vector version of the Avellaneda–Stoikov inventory skew in $r^{\text{res}}$ (Chapter 18), and the basket engine collapses to a single-name quote, which is reassuring: the big machine agrees with the small one. Flip $\mathbf{x}\to-\mathbf{x}$, so the client buys, and the fair-value term flips while the cost terms stay positive, so the dealer's ask is fair value *plus* costs; nobody hands out bonds below fair value because the arrows reversed. And set $\gamma\to0$, a dealer with no fear at all. That dealer still pays liquidation cost and still gets picked off. "Risk neutrality is not a cure for being picked off," Ines says, which is her way of saying it is not a cure for adverse selection; the fourth term of (19.2) survives a dealer with nerves of steel.

The bug the desk sees most often in this equation is not mathematical. It is units. $x_i$ is in dollars of par, $\widehat P_i$ in fraction of par, $\Sigma^{\text{res}}_T$ in (fraction of par)$^2$ over the horizon, and $\gamma$ in $\$^{-1}$. So $\gamma\,\mathbf{x}^\top\Sigma\mathbf{x}$ has units $\$^{-1}\cdot\$^2=\$$. Every term in (19.2) is in dollars, and the engine converts to basis points of gross market value only at the very end, which is the step ROBO skipped in the story under the Spec below.

> **[SOURCE EXTRACTION]** *Man_Revolutions_in_Credit_Trading_2023 p.2:* "We attribute this to a combination of the growth of bond ETF trading and the advances made by algorithmic market-making desks on fixed income. These developments helped dealers become more comfortable in their ability to price debt securities in near real time and in greater size, initially in investment grade and then eventually within high yield too."
>
> **Annotation.** The two technologies map onto two terms of (19.2). Bond ETFs (and later index derivatives) shrink the risk term by replacing $\Sigma_T$ with $\Sigma^{\text{res}}_T$. Algorithmic market making shrinks the *latency* of the fair-value term: an auto-pricer that already holds a live $\widehat P_i$ for 10,000 bonds turns a 150-line basket into lookups. Note the order Man gives, "investment grade and then eventually within high yield": HY baskets correlate less with HYG and JNK than IG baskets do with LQD, so their residual is larger and their adverse-selection tail fatter. The 2026 desk prices HY PTs routinely, but runs a different $\gamma$, a different eviction target and a far more paranoid $\text{AS}$ model for them.

### Specification for AI Implementation

**What ROBO built from the vague version.** Theo asked for "the basket's cost in bp." ROBO computed handling cost in basis points of par, risk in dollars and adverse selection in price points, summed them, and returned 412. That number is correct in no unit known to science. ROBO never complains and never guesses, so it did not ask.

**The precise spec.** The inquiry is a struct of arrays, one entry per line, all shape $(N,)$, plus model inputs from the overnight build: loadings $B\in\mathbb{R}^{N\times K}$, factor covariance $\Omega\in\mathbb{R}^{K\times K}$, hedge loadings $A\in\mathbb{R}^{H\times K}$ and hedge basis covariance $U\in\mathbb{R}^{H\times H}$.

| Field | Shape | Units | Guard |
| :--- | :--- | :--- | :--- |
| `ids` | $(N,)$ | security-master id | unique; must resolve; examples use synthetic ids, never real CUSIPs |
| `x` | $(N,)$ | \$ par, signed, $+$ = dealer buys | nonzero; $\lvert x_i\rvert\le$ amount outstanding |
| `mid` | $(N,)$ | composite mid, fraction of par | $(0,1.5]$; reject `97.0` (points sent as fraction) |
| `age` | $(N,)$ | business days since a print anchored the composite | $\ge0$; flag $>10$ |
| `print_frac` | $(N,)$ | share of last 60 business days with a print | $(0,1]$ |
| `lcs` | $(N,)$ | round-trip LCS at standard size, fraction of price | $\ge0$ |
| `oasd`, `oas` | $(N,)$ | years; decimal | finite |
| `sector` | $(N,)$ int | code in $[0,K-1)$ | |
| `sig_idio` | $(N,)$ | daily idiosyncratic price vol, fraction of par | $>0$ |
| `prs` | $(N,)$ | Priming Risk Score (Chapter 13) | $[0,1]$ |
| `days_to_call` | $(N,)$ | business days to next lender call | `inf` if none |
| `ad_hoc` | $(N,)$ | live ad hoc group or Rule 2019 statement | $\{0,1\}$ |

Basket-level fields: response deadline (seconds), number of dealers in competition, spotting time, and the client's identity, which keys the markout history in §19.8. All costs are returned in dollars, with a bp-of-gross-MV view computed last. The python blocks in this chapter run in order in one interpreter.

A table of guards is a promise, and a promise is worth what happens when somebody breaks it. At 2:58 p.m. the list arrives as a spreadsheet exported by a client whose operations team chose the units, and the engine has about ninety seconds to learn whether column D means 97.0 points or 0.97 of par before it multiplies a hundredfold error into a \$212mm bid. A human glances at the first few rows and decides they look right. A desk that wants the same answer at 3:02 p.m. next Friday, when the human is on a flight, writes the contract down once, as an object that refuses to exist if it is wrong, and makes every later calculation take that object as its only input.

Listing 19.1 has three parts. The `Basket` class holds the inquiry as thirteen parallel arrays, one per row of the table, with the units written beside each field. Its `__post_init__` is the gate. It rejects ragged lengths, non-finite values in the ten numeric fields (`days_to_call` is exempt, because `inf` is how the engine says "no lender call on the calendar"), zero-notional lines, a `mid` outside (0, 1.5], a `print_frac` outside (0, 1], a negative `lcs`, a `prs` outside [0, 1] and a non-positive `sig_idio`. The `mv()` method returns unsigned market value, and `drop()` returns a freshly built, freshly validated `Basket` without the named lines, which is what the eviction loop of §19.6 will lean on. The function `make_basket` manufactures the cold-open inquiry: 150 lognormal tickets around \$1mm, seeded so the numbers repeat, with line 42 hard-wired at \$18mm, forty days stale and printing on 5% of days, and line 117 at \$4mm, marked at 0.82, with a Priming Risk Score of 0.85, a lender call three days out, a live ad hoc group and a daily idiosyncratic volatility of 0.003 that looks perfectly calm. The other lines are rescaled so the gross lands on \$212mm exactly. The closing block confirms the sizes, checks that multiplying `mid` by 100 raises an error, and runs the Monte Carlo test of the certainty equivalent from §19.2.1: 400,000 Gaussian P&L draws with mean \$100k and standard deviation \$300k should give \$55k, which is the mean minus \$45k of risk charge.

Everything that follows enters through this door, and the door tests ranges, not meaning; it is not a security-master check. What slips through is the gap between the table and the constructor: the table promises unique ids, non-negative `age`, sector codes in range and an ad hoc flag in {0, 1}, and the code enforces none of them. A sector code of -1 sails through and then, in Listing 19.3, points at the market column instead of a sector, so the line silently loses its sector exposure. Those are the checks a desk adds before its first live Friday.

*The full listing is [Listing 19.1 in Appendix F](#code-19-1).*

The Monte Carlo check is not decoration. If someone later swaps the Gaussian P&L for a jump-to-default mixture, the same check fails, and the size of the failure is the $\tfrac16\gamma^2\kappa_3$ term from Step 2: the skew that mean–variance ignores and that §19.8 charges for explicitly.

## 19.3 Per-Line Liquidation Cost: LCS, Size, and the Fat Tail

Ines calls the per-line cost "the rake": the house's cut of each hand, small, boring, and the reason the house still exists. For an ex-RSSG banker the instinct is to see line 83 as a claim with a recovery. The engine sees it first as a number, the cost of getting out, and the canonical seed for that number is Barclays' Liquidity Cost Score.

> **[SOURCE EXTRACTION]** *Ben_Dor_Quantitative_Credit_Portfolio_Management p.112:* "We define LCS as the bond's OASD multiplied by this spread. Consequently, a bond's LCS can be interpreted as the cost, in percentage points, of immediately executing a roundtrip transaction."
>
> **Annotation.** The spread-quoted branch is $\text{LCS}_i=D^{\text{spr}}_i\,(s^{\text{ask}}_i-s^{\text{bid}}_i)$, which is *already in price space*: a 4-year spread duration times a 25bp bid–ask is 1.00% of price. Every desk has a junior quant who multiplies it by duration again to "convert to price," producing a 4% round-trip cost and a PT bid that never wins. For HY and distressed lines quoted on price, the branch is $(P^{\text{ask}}-P^{\text{bid}})/P^{\text{bid}}$ (Ben_Dor p.118; Dynkin_Systematic_Investing_in_Credit p.702 gives the same two branches). Ben Dor also pins the size: LCS is the cost "for a 'normal-sized' transaction amount (e.g., \$3 to \$5 million par)" (p.118). On a 2026 desk the gap is coverage. LCS is a dealer-quote-based score built for index constituents, while a PT drags in off-index lines, so the engine needs a fallback cost model for lines without a score: TRACE-derived effective spreads (Chapter 18's Roll and Kyle estimators) with an explicit staleness flag.

On this desk the junior quant in that annotation has a name, and Ines tells the story with the date attached so that nobody mistakes it for a parable. On Tuesday 13 January 2026, in Hana's second month, the engine bid a 60-line high-yield list and lost it by almost three points of price, not basis points *(illustrative)*. Ines noticed because a bid that loses by more than a whole bond's bid–ask is not a bad bid; it is a different calculation. It took twenty minutes to find. Hana had multiplied every spread-quoted LCS by duration again "to put it in price terms," so a 1% round trip had become 4%. The mistake cost the desk nothing but a lost auction and a client who did not send another list for a month. Hana now owns the unit test that catches it, and the sentence on the whiteboard above her desk reads: "LCS is already in points. Don't convert what's already converted."

The size of the ticket is the other half of the rake, and it is where line 42 lives.

### 19.3.1 Derivation: from a standalone score to a basket cost

> **Math, Gently.** *The size exponent, or the door that narrows.* Carrying one box out of a room takes a minute. Carrying four boxes takes four minutes, if the door is wide. If the door narrows as the pile grows, because every buyer you call now knows you are carrying a pile, the fourth box takes longer than the first. Market impact is that door. Chapter 4 (§4.8) showed why the evidence favours a square root: the total cost of selling $X$ grows like $X^{3/2}$, so the cost *per dollar* grows like $X^{1/2}$. A linear-impact world makes the per-dollar cost grow like $X^{1}$ instead. The exponent $\eta$ in (19.3) is the dial between them. Try line 42: \$18mm against a standard size of \$4mm is 4.5 standard tickets. At $\eta=\tfrac12$ each dollar costs $4.5^{0.5}\approx2.1$ times the standard rate; at the engine's middle setting $\eta=0.75$ it costs $4.5^{0.75}\approx3.1$ times; at $\eta=1$ it costs 4.5 times. That 3.1 is the multiplier Figure 19.1 draws for line 42. Below standard size the dial does nothing: a \$1mm ticket pays the standard rate, not a quarter of it, because odd lots never get cheaper. The full version is next.

Put together, the derivation below says one thing, which equation (19.3) writes out: a line's handling cost is a handling share $\omega$ of half its LCS, times its market value, times a size multiplier that is flat up to standard size and rises as size to the power $\eta$ beyond it.

#### The Full Derivation

*Step 1 (one way).* LCS is a round trip at standard size $x^{\text{std}}$. The dealer buying the basket pays half of it on the way out, so the naive one-way cost of line $i$ in dollars is $\tfrac12\,\text{LCS}_i\,\widehat P_i\,\lvert x_i\rvert$.

*Step 2 (do not charge risk twice).* LCS is a *standalone* price. A dealer quoting one bond alone charges for handling (search, balance-sheet usage, operational cost) and for holding that bond unhedged and undiversified. Write the standalone half-spread as handling plus a standalone inventory charge. Inside a basket, (19.2) already prices inventory risk at the portfolio level through $\tfrac12\gamma\,\mathbf{x}^\top\Sigma^{\text{res}}_T\mathbf{x}$. Charging the full half-LCS *and* the risk term counts the inventory charge twice. So the cost term keeps only the handling share $\omega\in(0,1]$:

$$
c_i(x_i) \;=\; \omega\cdot\tfrac12\,\text{LCS}_i\;\widehat P_i\;\lvert x_i\rvert\;\max\!\Big(1,\frac{\lvert x_i\rvert}{x^{\text{std}}}\Big)^{\eta},
\qquad \eta\in[\tfrac12,1].
\tag{19.3}
$$

*Step 3 (size).* The bracket is flat below standard size, because an institutional half-spread does not get cheaper for smaller tickets (odd lots, if anything, pay more), and it steepens above it. The exponent $\eta$ brackets the two canonical impact models. With linear temporary impact (Almgren & Chriss, 2000, "Optimal Execution of Portfolio Transactions"), a linear unwind of $X$ over $T$ costs $\varepsilon X+\tfrac12\theta_0X^2+\theta_1X^2/T$ in expectation, where $\varepsilon$ is the fixed half-spread and $\theta_0$, $\theta_1$ are permanent and temporary impact coefficients. Per dollar this grows linearly in $X$, so $\eta=1$. With square-root impact (below) the total cost grows like $X^{3/2}$, so the per-dollar cost grows like $X^{1/2}$ and $\eta=\tfrac12$. For line 42, \$18mm against $x^{\text{std}}=\$4$mm, the per-dollar cost is $4.5^{\eta}$ times the standard rate, between 2.1× and 4.5×.

*Step 4 (calibrating $\omega$).* Meli & Todorova's 41.7% saving says an IG PT line costs on average about 58% of its RFQ half-spread, all in. That all-in figure includes risk and adverse selection, so the pure handling share sits below it. We use $\omega=0.5$ in the HY example *(illustrative)*. On your own data, regress realized PT line costs, measured as markouts to the next composite, on half-LCS at size, with the residual-risk contribution $\gamma x_i(\Sigma^{\text{res}}_T\mathbf{x})_i$ as a control.

*Step 5 (horizon).* Almgren–Chriss also hands us $T$. Optimal schedules trade off impact against variance, and Li (2022) finds PT bonds "stay in dealer inventories for 5.3 days longer" than voice bonds, because a hedged lump is cheap to hold. So $T\approx5$ business days for residual lines is empirically grounded. **All variance lives in $\Sigma^{\text{res}}_T$** (§19.4–19.5). Almgren–Chriss contributes only the expected cost and the choice of $T$. Put $\sigma_i^2$ in both places and you have charged it twice, which is the variance version of the duration mistake.

#### Volume, composites, and the stale price

> **[SOURCE EXTRACTION]** *Paleologo_Advanced_Portfolio_Management p.193:* "TC : market impact model. TC(x) = κ Σ_i σ_i^β (|x_i|/v_i)^γ where v_i is the average daily trading volume (in dollars), σ_i the volatility, β ≃ 1, γ ≃ 3/2 and κ > 0 a region-calibrated constant."
>
> **Annotation.** Paleologo's exponent $\gamma\simeq3/2$ is our $1+\eta$ with $\eta=\tfrac12$. We rename it because $\gamma$ is risk aversion in this book. The equity law scales size by average daily volume $v_i$, which in credit is the weakest number on the screen. Most bonds do not trade daily, TRACE volume includes the PT prints themselves, and MarketAxess reported that duplicate trade reports "inflated U.S. high-grade TRACE volumes by up to 8% in June 2026" (Q2-2026 results). So credit swaps the denominator to $x^{\text{std}}$ and the volatility to LCS, a dealer-quote-based object that already embeds the bond's riskiness. Volume survives as a *feature* of the cost model: Ben Dor notes that "LCS is negatively related to a bond's trading volume" (Ben_Dor p.128). It should not be the cost itself.

Composite fair values (dealer-composite and evaluated-pricing services) make the first term of (19.2) a lookup. They also create *composite reflexivity*: when the auto-quoter, the price-improvement benchmark and the PT reference all key off the same composite, a composite error becomes a correlated execution error across every line that uses it. The engine therefore treats a stale composite as a source of *variance* (§19.5), not as a fixed haircut. A stale price is not a wrong price. It is a price with a confidence interval that nobody printed.

> **Ways This Blows Up.** (1) **Duration twice:** LCS for a spread-quoted bond is already a fraction of price. (2) **Size ignored:** LCS at \$4mm applied unscaled to a \$25mm line understates its cost by $6.25^{\eta}$, between 2.5× and 6.25×. (3) **Stale fair value:** an evaluated price for a bond that last traded 40 days ago enters the bid at full confidence unless `age` feeds the covariance. (4) **Contaminated volume:** liquidity features built on raw TRACE volume pick up duplicate affiliate prints and the basket's own PT prints, so the bond looks liquid *because it was in last month's PT*. Deduplicate with the affiliate indicator (voluntary from 2026-08-31, mandatory 2027-08-02, per FINRA Regulatory Notice 26-16) and strip PT-flagged prints. (5) **Points as fractions:** a mid of `97.0` instead of `0.97` raises fair value a hundredfold. The `Basket` guard catches it, and that guard is not optional.

### Specification for AI Implementation (handling cost)

Equation (19.3) is one line of algebra, which is exactly why it ends up typed four different ways in four different notebooks, and why one of the four multiplies by duration a second time. A desk writes the line once, gives it a name and a set of refusals, and lets the rest of the engine call it. The point is not that the arithmetic is hard. The point is that line 42 is about to be priced, and nobody wants an argument at 3:01 p.m. over which notebook's rake is the real one.

Listing 19.2 is `handling_cost`, equation (19.3) vectorized over the whole basket. It takes the `Basket`, the handling share `omega` (default 0.5), the size exponent `eta` (default 0.75, halfway between the square-root and linear impact laws), the standard size `X_STD` of \$4mm, and a liquidity multiplier `m` that sits at 1 in calm markets and is the dial §19.7 turns in stress. It refuses an `omega` outside (0, 1], an `eta` outside [0.5, 1] and a non-positive `m`, so a typo cannot quietly produce a free lunch. Step by step, it expresses each line's size in units of standard size, takes the larger of that and one, raises it to `eta`, and multiplies by half of `lcs`, the mid, the absolute notional, `omega` and `m`. The output is one non-negative dollar cost per line. The sign of `x` is ignored, because handling a bond costs the same whichever way the client trades it. The asserts then check the flat region below \$4mm, the \$18mm multiple of 4.5 to the power 0.75 (about 3.1), and a comparison with the 25 cheapest lines.

It prices the handling share and nothing else; all variance lives in the covariance matrix of §19.5. Its blind spot is `lcs` itself. The function trusts the field to be a fraction of price at standard size, and the `Basket` gate checks only that it is not negative. A spread-quoted score that someone already multiplied by duration (Hana's January bug in §19.3), or a dealer-quote score carried over from an index bond to an off-index line, flows straight through and comes out the other end as a precise dollar figure.

*The full listing is [Listing 19.2 in Appendix F](#code-19-2).*

The last assert is the fat tail in one line. Line 42 has about 8% of the notional and, by hand arithmetic on this synthetic basket, roughly 40% of the handling cost *(illustrative)*. Section 19.6 will want to talk to it. Figure 19.1 shows the size multiplier behind that number on the left, and where line 42 sits in the cost ranking on the right.

![Figure 19.1: Handling cost steepens with ticket size, so one stale \$18mm line (orange) pays about 3.1 times the standard rate per dollar at the middle exponent and carries about 40% of the basket's handling cost on 8% of its notional. Illustrative: eq. 19.3 evaluated on the synthetic cold-open basket of Listings 19.1 and 19.2.](assets/figures/ch19_handling_cost_fat_tail.png)

## 19.4 The Hedge: Collapsing 150 Lines into One Lump

The hedge is how the dealer gets rid of the ETF it cannot sell (§19.2). At the walkthrough that evening Ines turns the card over and draws two columns on the back, one headed *instrument* and one headed *what it kills*, because a hedge menu read in the order the instruments were invented is useless and a menu sorted by the term of (19.2) it touches is a decision.

The top row is the ETF itself: LQD for an investment-grade list, HYG, JNK and USHY for high yield. It kills systematic spread risk at a 1–2bp half-spread in calm markets, and it carries a premium/discount basis that becomes the main risk in stress. Next comes index CDS, CDX IG and CDX HY, which kills the same systematic spread risk with no cash basis but with a CDS–bond basis of its own, and does nothing for the cash bonds' liquidity. Ines writes the iBoxx total return swaps on the third line, standardized from 2015 (Li, 2022), and options on corporate bond ETFs beside them. On the fourth she writes the newest entry, the Cboe iBoxx credit futures, IBIG and IBHY: listed, blockable, and growing (the Trend Watch at the end of this section has the numbers). At the bottom, almost as an afterthought, go Treasury futures for the spotted rate leg, which the engine treats as already done.

Theo reads down the right-hand column twice. Spread risk, spread risk, spread risk, spread risk, rates. "What kills the liquidity term?" he asks. "The thing that happens when every bond on this list gets harder to sell at once?"

"Nothing on this card," Ines says. "Ben Dor looked."

> **[SOURCE EXTRACTION]** *Ben_Dor_Quantitative_Credit_Portfolio_Management p.166:* "To hedge default-related risks at the issuer level, investors may use the issuer's CDS. For hedging systemic liquidity risks, VIX futures might be a more appropriate instrument… the correlation between LCS and VIX from January 2007 to April 2009 was 0.90."
>
> **Annotation.** This is the hedge menu sorted by *which term of (19.2) it touches*. Index instruments attack the systematic part of $\Sigma_T$. Single-name CDS could attack line 117's jump, if it trades, if it is not itself being manufactured by the same ad hoc group (Chapter 24), and if you can buy protection in 90 seconds, which you cannot. Nothing on the menu hedges the *liquidity* term: the 0.90 LCS–VIX correlation says the cost multiplier of §19.7 is one systematic factor, and the engine has no instrument that pays off when it rises. The 2026 desk proxies it with ETF discounts and VIX, and prices what it cannot hedge.

### 19.4.1 Derivation: the minimum-variance hedge and the residual

> **Math, Gently.** *A hedge ratio is a slope, and the residual is what the slope leaves.* (a) Chapter 1 (§1.4) drew a regression slope as the best straight line through a cloud of points. Plot the basket's daily P&L against HYG's, and the slope of that line is the hedge ratio: how many dollars of ETF to sell per dollar of basket. If the basket moves 0.9 for every 1.0 of the ETF and nothing else is going on, sell \$0.90 of HYG per dollar and the wobble is gone. Figure 19.2 draws the same idea as a bowl: hedge too little and you keep the market, hedge too much and you are short it, and the bottom of the bowl is the slope. (b) Now add basis noise, days when the ETF wobbles for reasons of its own (a big redemption, a closing auction). Two things happen. The slope you estimate *shrinks*, because some of the ETF's movement has nothing to do with your bonds and the regression rightly trusts it less; statisticians call this errors-in-variables attenuation. And a residual survives that no amount of ETF will remove. The share that survives is $1-R^2$, where $R$ is the correlation. At Meli & Todorova's average of 0.85 for IG lists against LQD, $R^2=0.72$, so 28% of the variance stays on the desk, which is $\sqrt{0.28}\approx53\%$ of the volatility: a hedge that "explains" most of the risk still leaves half the swings. That leftover is the Schur complement in (19.4), written for one bond and one hedge. The matrix version is next.

The 0.55 on Ines's screen in the cold open is the same idea read off a history of composite prices, and it is pessimistic for a reason §19.5 will make precise: bonds that rarely print have smoothed, stale returns, and stale returns understate how much a bond really moves with the market. The engine's factor model, which loads each bond on the market by its DTS instead of by its tape, says the hedge can take out well over half the basket's volatility (Figure 19.2 below). Both numbers are right about different things. The 0.55 says how the basket has looked; the factor model says what it is made of. Ines trusts the second for the hedge and the first for her mood.

Equation (19.4), derived next, says that the best hedge sells $\Sigma_{ff}^{-1}\Sigma_{fx}\mathbf{x}$ dollars of the hedge instruments and leaves a residual covariance $\Sigma^{\text{res}}$ that is the covariance of the bonds *after* everything the hedges can explain has been taken out.

#### The Full Derivation

Let $\mathbf{r}\in\mathbb{R}^N$ be bond price changes over the horizon (fraction of par) and $\mathbf{f}\in\mathbb{R}^H$ the returns of $H$ hedge instruments per dollar notional, with joint covariance

$$
\operatorname{Cov}^{\mathbb{P}}\begin{pmatrix}\mathbf{r}\\ \mathbf{f}\end{pmatrix}=\begin{pmatrix}\Sigma_{xx} & \Sigma_{xf}\\ \Sigma_{fx} & \Sigma_{ff}\end{pmatrix},\qquad \Sigma_{fx}=\Sigma_{xf}^\top .
$$

The dealer is long $\mathbf{x}$ and sells $\mathbf{h}$ dollars of hedges, so the hedged P&L is $\mathbf{x}^\top\mathbf{r}-\mathbf{h}^\top\mathbf{f}$ with variance

$$
V(\mathbf{h}) \;=\; \mathbf{x}^\top\Sigma_{xx}\mathbf{x} \;-\; 2\,\mathbf{h}^\top\Sigma_{fx}\mathbf{x} \;+\; \mathbf{h}^\top\Sigma_{ff}\mathbf{h}.
$$

*First-order condition.* $\nabla_{\mathbf h}V=-2\Sigma_{fx}\mathbf{x}+2\Sigma_{ff}\mathbf{h}=0$. Since $\Sigma_{ff}\succ0$, this is a minimum and

$$
\mathbf{h}^\star=\Sigma_{ff}^{-1}\Sigma_{fx}\mathbf{x},\qquad
V(\mathbf{h}^\star)=\mathbf{x}^\top\underbrace{\big(\Sigma_{xx}-\Sigma_{xf}\Sigma_{ff}^{-1}\Sigma_{fx}\big)}_{\Sigma^{\text{res}}}\mathbf{x}.
\tag{19.4}
$$

$\Sigma^{\text{res}}$ is the Schur complement of $\Sigma_{ff}$. Under joint Gaussianity it is the conditional covariance $\operatorname{Cov}(\mathbf{r}\mid\mathbf{f})$, which has a useful consequence: **$\mathbf{x}^\top\Sigma^{\text{res}}\mathbf{x}$ is the optimally re-hedged variance for any basket $\mathbf{x}$.** When §19.6 evicts a line, the hedge re-optimizes for free, with no second solve. The hedge's own cost, $c_h=\sum_j\lvert h^\star_j\rvert\,\text{hs}_j$ with $\text{hs}_j$ the half-spread per dollar notional, is added to (19.2). It is small for LQD and CDX and not small for a futures block in a thin month.

*The one-factor case, and why basis attenuates the hedge.* Let $r_i=\beta_i g+\epsilon_i$, with $\beta_i=-\widehat P_i\,\text{DTS}_i$ the price sensitivity to a common relative-spread move $g$ (the DTS model of Chapters 8–9), and one hedge with return $f=\beta_h g+u$, where $u$ is basis noise with variance $\sigma_u^2$. Then

$$
h^\star=\frac{\beta_h\sigma_g^2}{\beta_h^2\sigma_g^2+\sigma_u^2}\sum_i x_i\beta_i,
\qquad
\Sigma^{\text{res}}_{ij}=\beta_i\beta_j\,\frac{\sigma_g^2\,\sigma_u^2}{\beta_h^2\sigma_g^2+\sigma_u^2}+\delta_{ij}\,\sigma^2_{\epsilon,i}.
$$

With no basis ($\sigma_u\to0$), $h^\star=\sum_i x_i\beta_i/\beta_h$, the DTS-matched hedge, and the residual is purely idiosyncratic. Its variance grows like $N$ while the basket's dollar size grows like $N$, so the risk per dollar falls like $1/\sqrt{N}$. That is the one-line reason a dealer can quote a diversified, hedgeable basket *inside* the sum of its line half-spreads. With basis, the hedge ratio shrinks (classic errors-in-variables attenuation), and a rank-one systematic residual survives that does *not* diversify. In March 2020 bond ETF tracking error exceeded 200bp against a 0.7bp average (Todorov, BIS Quarterly Review, March 2021, "The anatomy of bond ETF arbitrage"). In the formula above, $\sigma_u$ went from a rounding error to the dominant term. Figure 19.2 draws both halves of the point: the bowl the hedge solve finds the bottom of, and what basis noise does to it.

![Figure 19.2: Left, the 5-day P&L risk of the cold-open basket falls from \$1.37mm unhedged to \$0.52mm at the optimal hedge and rises again if the dealer over-hedges. Triple the basis noise on both hedges and the optimum shrinks to half the size, with a \$1.03mm floor. Right, the one-factor formula: as basis noise grows relative to the hedge's factor risk, the hedge ratio kept falls and a systematic residual survives. Illustrative: Listing 19.3 (left) and the one-factor case of section 19.4.1 (right).](assets/figures/ch19_hedge_bowl_and_basis.png)

#### Why the lump is cheap, and who finds it cheapest

*Two theories of why PT works, both in this equation.* Meli & Todorova link PT's cost advantage to the ETF ecosystem: baskets that are "closer" to ETFs are cheaper, both because ETFs give real-time prices and hedges and because creation/redemption is an outlet for less liquid bonds. Li (2022) finds that only 20–30% of PT bonds overlap with realized ETF creation/redemption baskets, that voice costs respond to dealer inventory shocks while PT costs do not, and attributes the rise of PT to inventory hedging with index derivatives. The SCOOS answers split the difference. About four-fifths of active dealers call trading the individual constituents through other protocols a *very important* way to work off PT inventory. ETF creation/redemption and offsetting PTs are at least somewhat important for about three-quarters and one-half respectively. Three-fifths "frequently hedge credit portfolio trades with credit ETFs," and about half use CDS in at least a few situations. In engine terms, Li is about $\Sigma_{ff}$ (the hedge shrinks the risk term) and Meli–Todorova is partly about $c_i$ (the creation/redemption window lowers the liquidation cost of the residue). Both terms are in (19.2), so you do not have to pick a side.

> **View From Another Seat.** *The ETF market maker.* To a non-bank liquidity provider that already makes markets in the ETF, a portfolio trade is not 150 bonds plus a hedge. It is one leg of a triangle whose other two legs, the ETF and the index CDS, it trades all day anyway. Jane Street describes its fixed-income offering in exactly those terms: "Our leading presence in electronic trading, portfolio trading, and ETF trading, combined with our disciplined approach to risk management, allows us to be a consistent fixed income liquidity provider for clients in all market environments" (client-offering page, fetched 18 October 2026). Flow Traders' annual report for 2025, signed 12 March 2026, lists among its credit-trading plans "distributing pre-trade portfolio trading levels to expedite portfolio construction," and the same report says the firm reduced the capital it deployed to fixed income in 2025 in favour of other asset classes. Read through (19.4), the seat's advantage and its exposure are the same object. Its $\Sigma_{ff}$ is cheap, because the hedge is its home market and, where it acts as an authorized participant, creation and redemption give the residue an exit. Its risk is the basis $\sigma_u$, because when the ETF and the bonds part company it is long one and short the other. A bank desk asks whether it can hedge the basket; this seat asks whether the triangle will hold this week, and its capital follows the answer.

The bank desk's version of the same worry is shorter and more embarrassing, because it is a list of the ways its own hedge solve has already failed.

> **Ways This Blows Up.** (1) $\Sigma_{ff}$ estimated from ETF *price* returns in a calm window carries a basis variance near zero, so the engine over-hedges in exactly the week the basis explodes. Model the basis as its own regime-dependent variance (`basis_scale` below). (2) A dealer that is not an authorized participant cannot deliver residue into a creation basket, so its $T$ is longer and its $c_i$ higher. (3) HY baskets correlate less with HYG and JNK, and less stably, than IG baskets with LQD. Meli–Todorova's 0.85 is an IG number. (4) Two nearly collinear hedges (an HY ETF and CDX HY) make $\Sigma_{ff}$ ill-conditioned, and $\mathbf{h}^\star$ becomes a large long–short position in two instruments that differ only by their basis noise. Guard the condition number.

> **Trend Watch: the hedge stack, 2015–2026.** *What changed:* the instruments that turn a basket into "one lump plus a residual" multiplied, and the ETF lost its monopoly. *When and how big:* standardized iBoxx TRS from 2015 and corporate bond ETF options gave dealers index hedges for cash inventory (Li, 2022). The credit-ETF-to-cash volume ratio fell from 23.2% in 2022 to 16.6% in 2024 as PT absorbed risk transfer that used to route through ETFs (Coalition Greenwich, January 2025). On stress days ETFs re-dominate: \$99bn of fixed income ETFs traded on 2025-04-07, about 60% of it in iShares (The DESK, 2025-06-10). In the June 2025 SCOOS, three-fifths of active PT dealers said they frequently hedge with credit ETFs and about half used CDS in at least a few situations. By August 2026, Cboe iBoxx credit futures block trades topped \$1bn a month for the second month running, and IBIG block volume passed IBHY for the first time (Cboe sponsored content in The DESK, 2026-10-16; treat as vendor-reported). *What it means:* $H$ in (19.4) is now 3–5 instruments, not 1. The hedge solve chooses among them by basis risk and cost, and the engine must carry each instrument's basis as its own variance.

### Specification for AI Implementation (factor model and hedge)

Shapes: $B$ is $(N,K)$ with $K=1+8$ (market plus eight sectors), $\Omega_T$ is $(K,K)$, $A$ is $(H,K)$ with $H=2$ (an HY ETF and CDX HY, both in the long-risk convention, so a positive $h$ sells risk), and $U$ is $(H,H)$. All covariances are over the horizon $T$. Factor and basis volatilities are *illustrative*.

Kaz's notebook failed because it tried to learn 11,325 covariances from fourteen observations. The cure in the derivation is to stop learning and start assuming: bonds move together because they share a few spread factors, and the hedge exists to remove exactly those. That leaves four matrices to build before the dealer can say how much of the \$212mm is one lump and how much is 150 small arguments: the loadings $B$, the factor covariance $\Omega_T$, the hedge loadings $A$ and the basis covariance $U$. The hedge ratio is also the number the trader will read aloud to the ETF desk, and it had better be the same number the risk term uses. So the desk builds the matrices, runs the solve and proves the two agree in one place, before anyone is allowed to type a price.

Listing 19.3 does exactly that. `loadings` turns each bond into a row of `B` with the DTS rule: price change per unit relative spread move is minus the mid times OAS duration times OAS. A bond loads that amount on the market factor and the same amount on its own sector's factor, and on nothing else. `factor_cov` returns a diagonal $\Omega_T$, with illustrative daily volatilities of 1.5% for the market and 0.8% for each sector, scaled by the five-day horizon. `hedge_book` returns `A` for two instruments, an HY ETF with index DTS 0.16 and CDX HY with 0.14, each spread equally across the sectors, and `U`, the basis covariance, whose `basis_scale` argument is the stress dial. `joint_cov` assembles $\Sigma_{xx}=B\Omega_TB^\top+D$, $\Sigma_{xf}$ and $\Sigma_{ff}$, and stops if the hedge block's condition number passes $10^8$. `residual` forms the Schur complement of (19.4) with a linear solve rather than an inverse, and `min_var_hedge` returns the dollar hedge, positive meaning sell risk. The closing block runs the cold-open basket before any staleness is added: the hedge sells about \$80mm of the ETF and \$157mm of CDX, and the standard deviation of P&L falls from about \$1.37mm to about \$0.52mm *(illustrative)*. Two asserts follow. The residual quadratic form must equal the hedged variance computed by hand, and the hedge must remove more than half the variance.

It is built for a hedge menu of a handful of linear instruments and factors that hold still. Options-based hedges are outside it, and so is a factor covariance estimated in a calm window and used in a loud one, which is the week Two Tapes replays (§19.7.2). The subtle failure sits in `hedge_book`. The two rows of `A` are exactly proportional, so the ETF and CDX are distinguished only by their basis noise, and `U` alone keeps $\Sigma_{ff}$ invertible. Let a calm-window estimate push `basis_scale` toward zero and the guard fires, which is the right outcome: the engine stops instead of handing the trader a hedge that rests on a basis variance of nothing.

*The full listing is [Listing 19.3 in Appendix F](#code-19-3).*

### Deep-Dive Resource Graph

**Podcasts**

- Bloomberg Professional, *Market Dialogues*, "How is portfolio trading changing the fixed income landscape?" (2025-07-07; recorded at the Pricing & Valuations Summit): https://professional.content.cirrus.bloomberg.com/professional2023/insights/markets/how-is-portfolio-trading-changing-the-fixed-income-landscape/
- **Giuseppe Paleologo - Multi-Manager Hedge Funds & Thinking Deeply About Simple Things (S7E11)** (*Flirting with Models*, 2024-09-02). The most technical audio on factor models in hedging, crowding risk and portfolio construction, from the author of the Paleologo text cited in §19.3 and §19.5, and the audio companion to this section's factor hedge. https://www.flirtingwithmodels.com/episodes/l2l3xUqwZbz
- **The Present and Future State of Corporate Bond Portfolio Trading** (Coalition Greenwich webinar, host Kevin McPartland with Paris Pender of Trumid, 2024-01-17; summarized on Trumid's site). Pender calls dealers "very efficient in providing quotes" on baskets, which is the efficiency this section's hedge-to-one-lump step explains; the 8%-of-TRACE share for Q4 2023 is vendor-sourced. https://www.trumid.com/news/2024/coalition-greenwich-webinar-the-present-and-future-state-of-corporate-bond-portfolio-trading/

**Practitioner Writing**

- Man Group (2023), *Revolutions in Credit Trading* (on the shelf as `Man_Revolutions_in_Credit_Trading_2023`).
- **Changes in the Returns to Market Making** (Adrian, Fleming, Shachar, Stackman and Vogt, NY Fed *Liberty Street Economics*, 2015-10-07). Estimates market-making returns in equities and corporate bonds; a sourced prior for how thin a dealer's edge per trade is, which is the scale the residual risk left after the hedge has to be priced against. https://libertystreeteconomics.newyorkfed.org/2015/10/changes-in-the-returns-to-market-making/
- The DESK (2019-10-06), Lynn Strongin Dodds, "The burgeoning portfolio trading business": https://www.fi-desk.com/trading-protocols-portfolio-trading-lynn-strongin-dodds/
- The DESK (2022-06-01), Dan Barnes, "Barclays: Portfolio trading 8% of US credit market volume": https://www.fi-desk.com/barclays-portfolio-trading-8-of-us-credit-market-volume/
- Todorov (2021), "The anatomy of bond ETF arbitrage," *BIS Quarterly Review*, March 2021.

**Academic Papers**

- Meli & Todorova (2023), "Portfolio Trading in Corporate Bond Markets," AEA 2024 program: https://www.aeaweb.org/conference/2024/program/paper/a7z3SGGN
- Li, J. S. (2022), "Frictional Intermediation, Inventory Hedging, and the Rise of Portfolio Trading in the Corporate Bond Market," AEA 2023 program: http://www.aeaweb.org/conference/2023/program/paper/9TfsndSa
- Almgren & Chriss (2000), "Optimal Execution of Portfolio Transactions," *Journal of Risk* 3(2).

**Data & Code**

- FINRA Regulatory Notice 22-12 (TRACE portfolio-trade modifier) and Regulatory Notice 26-16 (affiliate indicator), via the FINRA notices index.
- Federal Reserve SCOOS, June 2025, special questions on credit portfolio trading: https://www.federalreserve.gov/data/scoos/files/scoos_202506.pdf

## 19.5 Residual Covariance for 150 Stale Bonds

Kaz's `np.cov` is not just singular. It is lying with confidence. One hundred and fifty bonds with fourteen observed returns each give a sample matrix of rank at most 13, so 137 of its eigenvalues are exactly zero. Those are directions in which the basket appears to carry *no risk at all*. Any optimizer that touches the inverse (the hedge solve, the eviction loop) will find those directions and bet the desk on them.

"Fine," says Kaz, at the whiteboard after the close, "we regularize." Then, because line 117 is still on the screen and the word is in its covenant summary, Kaz adds, "Springing lien. Not seasonal. I was told." It is said with the pride of someone who has learned a vocabulary word and wants credit for it. "But is it a kind of jump process?"

Theo puts down the pen he has been chewing. "It's a lien that doesn't exist yet. It springs into existence on certain assets if a test trips, say leverage above a level on a test date. Until then the lenders are unsecured on those assets. After, they're not."

"So the event is defined by the path of something observable, and you know whether it has happened by looking at today's information, without peeking at tomorrow's."

"I suppose."

"So it's a stopping time," Kaz says, satisfied, and writes $\tau_{\text{spring}}$ on the board with a small flourish.

It sort of is; a stopping time is exactly a random date whose arrival you can confirm from what you know at that date, and a covenant test is that. "Then it doesn't go in this matrix," Ines says, from the door. "A covariance matrix is for things that wobble. That thing *jumps*. It goes in §19.8." Kaz looks at the matrix, which has 137 zeros in it, and concedes that it has enough problems already.

> **Math, Gently.** *Fourteen photographs of 150 people.* (a) Suppose you want to know the height of each of 150 people, and all you have is fourteen group photographs, each showing everyone standing together. Each photo gives you one equation linking all 150 heights. Fourteen equations cannot pin down 150 unknowns; at most fourteen independent combinations are knowable, and every other direction is a blank the photos say nothing about. A covariance matrix built from fourteen weekly returns has the same problem: its *rank* (the number of independent directions it has information about) is at most 13, one being spent on the average, so 137 of its 150 eigenvalues are exactly zero. A zero eigenvalue is the matrix claiming that some long–short mix of these bonds carries no risk at all. The optimizer believes it, finds that mix, and puts the desk in it. (b) The cure is to stop asking the photos for 150 separate facts. A factor model says bonds move together because they share a few common drivers, so you estimate those drivers on the whole universe of several thousand bonds and only a variance per bond from its own history. Count the numbers. A full covariance for 150 bonds needs $150\times151/2=11{,}325$ of them. With $K=20$ factors you need $20\times21/2=210$ for the factor covariance plus 150 idiosyncratic variances, 360 in all, and every one of them is estimated on data that exists. The full version is in the derivation below.

### 19.5.1 Derivation: factor structure, staleness, shrinkage

The derivation below builds the idiosyncratic variance of each line in four moves, and equation (19.5) is where they land: the daily idiosyncratic variance, times the horizon plus a share of the days since the last print, inflated for bonds that rarely trade, plus a small ridge. The ridge is shrinkage, the trick Chapter 7-B (§7-B.5) derives in five lines: pull a noisy estimate part of the way toward a sensible target, and the matrix becomes invertible without becoming fiction.

#### The Full Derivation

*Structure.* Write $\Sigma_{xx}=B\,\Omega_T\,B^\top+D$. Here $B\in\mathbb{R}^{N\times K}$ holds the loadings on $K\approx10$–$30$ factors (rating × sector × duration-bucket excess-return factors, DTS-scaled as in Chapters 8–9). $\Omega_T$ is the $K\times K$ factor covariance, estimated on the *whole* universe of several thousand bonds, so it is well conditioned. $D=\operatorname{diag}(d_i)$ holds the idiosyncratic variances, the only part estimated from each line's own sparse history. This cuts the parameter count from $N(N+1)/2=11{,}325$ to $K(K+1)/2+N$, and every one of those parameters is estimated on data that exists.

*Staleness is variance.* Let $\widehat P_i$ be a composite last anchored by a print $a_i$ business days ago. Evaluated-pricing services move a stale bond with its comparables, so the *factor* part of its drift since the last print is captured. The idiosyncratic part is not. If a share $\kappa\in(0,1]$ of the idiosyncratic variance escapes the evaluator's matrix pricing, then $\operatorname{Var}(\widehat P_i-P_i^{\text{true}})\approx\kappa\,\sigma^2_{\epsilon,i}\,a_i$, where $\sigma^2_{\epsilon,i}$ is the daily idiosyncratic variance. This error is still unresolved at the moment the dealer buys, so it adds to the horizon variance.

*Non-synchronous trading.* A bond that prints on a fraction $\phi_i$ of days has smoothed observed returns, and its estimated $\sigma^2_{\epsilon,i}$ is biased down. Correct with summed lagged betas (Dimson; Scholes–Williams; Chapter 8) and inflate by $\phi_i^{-\xi}$, where $\xi\in[0.5,1]$ is calibrated on bonds whose print frequency changed.

*Shrinkage.* Ledoit & Wolf (2004, "A Well-Conditioned Estimator for Large-Dimensional Covariance Matrices," *JMVA* 88(2)) shrink the sample matrix $S$ toward a target $F$: $\Sigma^{\text{LW}}=(1-\delta)S+\delta F$, with optimal intensity

$$
\delta^\star=\max\Big\{0,\min\Big\{1,\;\frac{\hat\pi-\hat\rho}{\hat\zeta\,T_{\text{obs}}}\Big\}\Big\}.
$$

Here $\hat\pi$ sums the asymptotic variances of the entries of $S$, $\hat\rho$ is their covariance with the target, and $\hat\zeta=\lVert S-F\rVert_F^2$ is the misspecification. Ledoit and Wolf call that last quantity $\gamma$; we rename it because $\gamma$ is risk aversion. With the factor model as the target, shrinkage amounts to a ridge $\tau^2$ on the idiosyncratic block. Putting the pieces together, the idiosyncratic variance over the horizon is

$$
d_i \;=\; \sigma^2_{\epsilon,i}\,\big(T+\kappa\,a_i\big)\,\phi_i^{-\xi}\;+\;\tau^2 .
\tag{19.5}
$$

#### What the engine is saying about line 42

The factor model fixes the photographs. It does not fix line 42, whose problem is not too few photographs but an old one: nobody has photographed it since August.

> **Math, Gently.** *Staleness is variance: the drunk and the lamppost.* A random walk is a drunk leaving a lamppost (Chapter 4, §4.6, and Chapter 5 build it in full): every step is a coin flip, left or right, and the distance from the lamppost after $n$ steps is typically $\sqrt{n}$ steps, not $n$, because the lefts and rights partly cancel. A bond's idiosyncratic price is a drunk too, taking one step a day that nobody records when nobody trades it. Give line 42 a daily idiosyncratic volatility of 0.3 points and forty business days without a print. The composite has been dragged along with its sector, but its own wandering since the last print is unrecorded, and that wandering is typically $\sqrt{40}\times0.3\approx1.9$ points: an uncertainty nobody printed. The rule underneath is that *variances* add across independent days ($40\times0.3^2=3.6$ square points) and volatilities do not (forty times 0.3 would be 12 points, far too many). That is why staleness enters (19.5) as a term proportional to the days since the last print, added to the horizon. It has nothing to do with Itô's $\tfrac12\sigma^2$, which is a correction for compounding and is Chapter 6's business (§6.1.1).

For line 42 ($a=40$, $\phi=0.05$, $\kappa=\xi=0.5$, $T=5$) the bracket and the inflation multiply the naive $\sigma^2_\epsilon T$ by $(25/5)\times\sqrt{20}\approx22$. The engine is not saying line 42 is a bad bond. It is saying nobody knows what line 42 is worth, and pricing that ignorance.

> **[SOURCE EXTRACTION]** *Paleologo_Advanced_Portfolio_Management p.186:* "It is possible to obtain the same solution starting from different assumptions. The first one is the linear Ledoit-Wolf shrinked covariance matrix approach [Ledoit and Wolf, 2003]."
>
> **Annotation.** Paleologo's point is that several roads (linear shrinkage, a ridge penalty, a Bayesian prior on idiosyncratic variance) lead to the same regularized matrix. For a PT engine that is a licence to choose the road that can be *audited*. A ridge $\tau^2$ that rises with a line's staleness is something a trader can read and challenge ("why is line 42's $\tau$ so big?"), while a global $\delta^\star$ is not. The equity setting has daily closes for every name. Credit has 150 lines and a dozen prints, so the factor target carries most of the weight, and the shrinkage intensity for the median HY line is close to one.

The ridge is the part of this a trader can argue with, which is the point. The other part, how large $\gamma$ itself should be, is the argument that never ends, and an old book on credit portfolios supplies a way to have it.

> **[SOURCE EXTRACTION]** *Bohn_Stein_Active_Credit_Portfolio_Management p.48:* "Developing these strategies in the context of portfolio trades helps reduce the idiosyncratic impact of inexplicable behaviors of particular securities. A portfolio perspective complemented with quantitative systems sets the stage for generating high Sharpe… and Vasicek (return per unit of tail-risk contribution or return per unit of capital) ratios."
>
> **Annotation.** Two ideas for the risk term. First, diversification: the idiosyncratic block of $\mathbf{x}^\top\Sigma^{\text{res}}\mathbf{x}$ grows like $N$ while the notional grows like $N$, which is why the basket's per-dollar risk charge is far below the average line's standalone charge. Second, the Vasicek ratio names the right denominator for $\gamma$: capital, or tail-risk contribution. If the desk's capital is $z\,\sigma_W$ at a hurdle $\rho$ per year, matching $\tfrac12\gamma\sigma_W^2$ to the capital cost $\rho z\sigma_W T/252$ gives $\gamma=2\rho zT/(252\,\sigma_W)$. On illustrative numbers ($\rho=15\%$, $z=2.33$, $T=5$, $\sigma_W=\$500$k) that is about $3\times10^{-8}$ per dollar, roughly thirty times smaller than the $10^{-6}$ this chapter uses. The gap is what desks mean by "balance-sheet appetite." It is why $\gamma$ is backed out of won and lost PTs (the revealed-preference bid), not out of the capital plan. It is also why $\gamma$ jumps in stress, when SCOOS dealers cite balance-sheet availability as a very important decline reason.

None of this protects the matrix from the people who use it.

> **Ways This Blows Up.** (1) A trader bumps one line's volatility by hand, and a negative eigenvalue appears. Re-project to positive semi-definite (PSD) and recheck the condition number after *every* edit. (2) A bond downgraded last week still carries last month's IG-sector loading. Refresh $B$ on rating-change events, not on a calendar. (3) Kaz's Gaussian: inflating line 117's $\sigma_\epsilon$ to "account for the LMT risk" both under-charges the jump (variance is the wrong moment) and mis-ranks it for eviction (the loop now thinks line 117 is noisy, not toxic). Jumps go in $\text{AS}$.

### Specification for AI Implementation (residual covariance)

The argument of §19.5 ends on a promise: nobody knows what line 42 is worth, and the engine should price that ignorance instead of hiding it. The usual hiding place is a haircut, a flat number a trader types into a spreadsheet at 3:00 p.m. that survives, unsourced, until the model review where the risk committee asks why one bond's price has a mystery in it. The alternative is to let staleness enter where uncertainty belongs, in the variance, through a formula a skeptic can read and challenge, and to build the result into a matrix that is guaranteed to be invertible. This is the matrix the hedge solve and the eviction loop will touch most often, so it is where the desk wants its guards.

Listing 19.4 turns equation (19.5) and the factor model of Listing 19.3 into the covariance matrix the rest of the chapter uses. `idio_var` takes each line's daily idiosyncratic variance and multiplies it by the horizon plus half the line's staleness in business days (`kappa_stale`, 0.5), then by the inverse square root of its print frequency (`xi`, 0.5), then adds a ridge `tau2` that defaults to zero. `build_residual_cov` feeds that vector into `joint_cov`, forms the Schur complement, passes it through `psd_project`, and refuses to return a matrix whose condition number exceeds $10^6$. `psd_project` symmetrizes, takes an eigendecomposition, lifts any eigenvalue below $10^{-10}$ of the largest up to that floor, rebuilds, and symmetrizes again. The inputs are a `Basket` plus the horizon, basis scale and staleness parameters. The outputs are $\Sigma_{xx}$, $\Sigma_{xf}$, $\Sigma_{ff}$ and the guarded $\Sigma^{\text{res}}$.

The asserts are the section's claims in code. Every eigenvalue is positive. Line 42's residual variance is more than five times its naive value, which is the section's claim that staleness is variance and not a haircut. Every diagonal entry of $\Sigma^{\text{res}}$ is at least that line's own idiosyncratic variance. And Kaz's matrix, built from 14 observations on 150 bonds, has rank at most 13. On the synthetic basket, line 42 carries about three-fifths of the residual variance on 8.5% of the notional, and the risk charge at $\gamma=10^{-6}$ rises from about \$133k to about \$293k once staleness is priced *(illustrative)*.

The matrix is for any book whose history is shorter than the book itself, which in credit is every book. It knows nothing about jumps: line 117's lender call is not in it, and §19.8 is where that gets charged. The quiet trap is the projection. On a clean build it is a no-op up to rounding, because a Schur complement of a valid matrix is already valid. It earns its keep after a human edits the matrix by hand. Once it clips anything, `Sres` is no longer exactly the Schur complement, and the promise that $\mathbf{x}^\top\Sigma^{\text{res}}\mathbf{x}$ is the optimally re-hedged variance holds only approximately. So the desk edits the inputs and rebuilds, and leaves the output alone.

*The full listing is [Listing 19.4 in Appendix F](#code-19-4).*

## 19.6 Eviction: Which Lines to Kick Out, and the Price of Keeping Them

The dealer's best tool is not a better bid. It is a counter-proposal. "Clients may get better pricing if they accept suggested portfolio tweaks," as IFR put it in 2021 (Whittall, "US banks reap boom in bond portfolio and algo trading"). Translated: *take back lines 42 and 117 and I'll pay you more for the other 148.* The ex-RSSG reader knows this move from the other side of the table. It is the plan sponsor carving the fulcrum class to get the vote. The engine's job is to find the carve in under a second.

A carve is easy to propose and hard to price, and Theo, who has drawn class lines for a living, wants to know how anyone can tell in ninety seconds which carve is worth asking for. Ines's answer is that you learn it the way you learn anything at a card table: by losing, slowly, and keeping the hand histories. "I keep a 2022 tape for this," she says. "Every basket we were shown in the first half of that year, what the engine asked to hand back, what the client said, and what the lines did after. It's the best education I own, and it cost a fortune." The tape is the subject of §19.6.2. First the arithmetic it was teaching, because the counter-proposal on Friday afternoon came out of the same loop.

### 19.6.1 Derivation: marginal cost, exact removal saving, greedy loop

> **Math, Gently.** *The slope of the hill and the walk back to the car.* Standing halfway up a hill, the slope under your feet tells you what the *next* step costs. It does not tell you what it saves to walk all the way back down to the car, because the ground flattens as you descend, and each step down saves a little less than the last. Risk works the same way. The engine's gradient, $\gamma(\Sigma\mathbf{x})_j$, is the slope: the risk cost of one more dollar of line $j$, given everything else in the basket. Multiply it by the whole position and you get the "slope times distance" guess at what evicting the line saves. Try a \$3mm line in a basket where that guess, $\gamma\,x_j(\Sigma\mathbf{x})_j$, comes to \$18k. Part of the slope is the line's covariance with *itself*, and that part flattens as you walk the line out. With $\gamma=2\times10^{-7}$ and a line whose own five-day swing is about 4.7 points (a bond with news in it), the flattening is $\tfrac12\gamma\,\Sigma_{jj}x_j^2=\tfrac12\times2\times10^{-7}\times0.047^2\times(3\times10^6)^2\approx\$2\text{k}$. So the exact risk saving is \$18k minus \$2k, \$16k, and the full saving $\Delta_j$ adds the line's handling cost and its adverse-selection charge on top. A loop that ranked lines by slope alone would overpay for evicting the noisiest ones. The algebra is next.

Equation (19.6) collects the cost terms of (19.2) into one function and takes its slope; equation (19.7) is the exact saving from evicting one line, the slope-times-distance guess less the flattening. The derivation also shows why evicting the worst line by that measure always helps a one-sided basket, and why the same inequality, run backwards, is the buy side's sweetener.

#### The Full Derivation

Total cost of carrying the basket, collecting (19.2)'s cost terms:

$$
\mathcal{C}(\mathbf{x})=\sum_i c_i(x_i)+\tfrac12\gamma\,\mathbf{x}^\top\Sigma^{\text{res}}_T\mathbf{x}+\sum_i \text{AS}_i,
\qquad
\text{MC}_i\equiv\frac{\partial\mathcal{C}}{\partial x_i}=c_i'(x_i)+\gamma\big(\Sigma^{\text{res}}_T\mathbf{x}\big)_i+\frac{\partial\,\text{AS}_i}{\partial x_i}.
\tag{19.6}
$$

$\text{MC}_i$ is the vector inventory skew. Eviction is discrete, though, so we want the *exact* saving from setting $x_j$ to zero. Write $\mathbf{x}'=\mathbf{x}-x_j\mathbf{e}_j$ and expand the quadratic:

$$
\tfrac12\gamma\big(\mathbf{x}^\top\Sigma\mathbf{x}-\mathbf{x}'^\top\Sigma\mathbf{x}'\big)=\gamma\,x_j(\Sigma\mathbf{x})_j-\tfrac12\gamma\,\Sigma_{jj}x_j^2 ,
$$

so

$$
\Delta_j \;=\; c_j+\text{AS}_j+\gamma\,x_j\big(\Sigma^{\text{res}}_T\mathbf{x}\big)_j-\tfrac12\gamma\,\Sigma^{\text{res}}_{jj}\,x_j^2 .
\tag{19.7}
$$

The gradient term double-counts the line's own variance, and the $-\tfrac12\gamma\Sigma_{jj}x_j^2$ correction removes it. Because $\Sigma^{\text{res}}$ is the re-hedged covariance (§19.4), $\Delta_j$ already includes the re-optimized hedge.

*The greedy step is a descent step.* Let $M=\sum_i \text{MV}_i$ be gross market value. Evicting $j$ lowers the per-dollar cost $\mathcal{C}/M$ if and only if $(\mathcal{C}-\Delta_j)/(M-\text{MV}_j)<\mathcal{C}/M$, i.e. $\Delta_j/\text{MV}_j>\mathcal{C}/M$. Summing (19.7) over $j$ gives

$$
\sum_j\Delta_j=\mathcal{C}+\tfrac12\gamma\sum_{i\ne j}x_i\Sigma^{\text{res}}_{ij}x_j .
$$

When the off-diagonal risk is nonnegative (a one-sided basket of positively correlated bonds), $\sum_j\Delta_j\ge\mathcal{C}$. The MV-weighted average of the ratios $\Delta_j/\text{MV}_j$ is then at least $\mathcal{C}/M$, so the largest ratio is too, and the best eviction always helps. The loop: rank by $\Delta_j/\text{MV}_j$, evict the top line, update $\Sigma\mathbf{x}\leftarrow\Sigma\mathbf{x}-\Sigma_{:,j}x_j$ in $O(N)$ (the coupling term changes after every eviction, so never sort once), and stop when $\mathcal{C}/M$ reaches the competitive target $\kappa^\star$, when evicted notional reaches the client's tolerance $\alpha$, or when the count reaches $k_{\max}$. The exact problem is a knapsack. Greedy is the 90-second answer, and with $k_{\max}\le10$ it is usually the right one.

*The buy-side mirror is the sweetener.* Adding a liquid, ETF-heavy line with $\Delta/\text{MV}$ below the basket average lowers $\mathcal{C}/M$, by the same inequality run backwards. That is Meli & Todorova's "crowd-sourcing liquidity": even among illiquid PTs, the median share of liquid bonds is 37%, so "the more liquid bonds cross-subsidize the less liquid bonds." Barclays found 49% of IG PTs but only 18% of HY PTs fit the crowd-sourcing pattern, because HY portfolios "need many more liquid bonds to offset illiquid ones, because the far tail of the LCS distribution is thicker in HY" (The DESK, 2022-06-01).

#### What a liquidity score cannot see

> **[SOURCE EXTRACTION]** *Dynkin_Systematic_Investing_in_Credit p.704:* "TES blend LCS and trading volume of a bond into a single relative score that reflects both the cost and flow. Bonds with higher trading volume and lower LCS per unit of duration have lower TES."
>
> **Annotation.** The Trade Efficiency Score is a ready-made prior for the eviction ranking. A high-TES line is expensive *and* rarely traded, which describes the residual nobody wants to own for five days. On the same page Dynkin notes that LCS varies widely across bonds even at a single date, "so rebalancing costs… greatly depend on its composition." That is the fat tail of §19.3 restated as a portfolio fact. Our $\Delta_j$ improves on TES in two ways. It prices *covariance with the rest of the basket* (a high-TES line that hedges the others is worth keeping), and it carries the AS term, which no liquidity score can see. Sorting by TES alone evicts line 42 and keeps line 117, which is exactly the mistake the next section is about.

### 19.6.2 Case Study: The H1 2022 Reversal

#### Long Scene: The Year the Second Tier Went Home (H1 2022)

*A replay, played on Friday 23 October 2026 after the close: Ines's desk blotter, cut off at 2:40 p.m. on Tuesday 17 May 2022, a date chosen for the drill with no market event attached to it. Dov Adler's pod and Vantress Capital Management are fictional composites, and so is Halvorsen Packaging; the desk's hit rates, the basket, its sizes, fees and P&L are illustrative. The dated market facts and the quoted words of real people come from the sources cited.*

**The party.** Ines does not start the tape in 2022. A replay that begins at the turn, she says, teaches you the turn and nothing about why everyone missed it, so she starts in the last quarter of 2021 and lets the room feel how good it was. The desk's blotter for high-yield baskets that quarter shows a hit rate of 38% *(illustrative)*: more than one auction in three, at margins that would have embarrassed a market maker in 2019. The public numbers were just as cheerful. Portfolio trading's share of US corporate transactions had more than doubled in the year to January 2021, and Barclays' own basket desk had gone from almost nothing to one of the busiest in the Street (the counts are in the Trend Watch at the end of §19.1). Man called 2021 "the year of portfolio trading," and the extraction in §19.1 names the reason: competition "not only among what we would consider tier-one counterparties but also those in the second tier, with aggressive pricing offered" (§19.1). Mags has already told Theo what that looked like from the distressed seat, salesman's punchline and all (Chapter 2, §2.6.2), and she spares him the encore.

"In poker," Ines says, "when a new player sits down and calls everything, you don't learn anything about the cards. You learn that he's buying chips. Second-tier banks in 2021 were buying share. You can see it in $\pi$." She points at the master equation, still on the whiteboard from the afternoon. The margin is the term competition sets, and in 2021 competition set it near zero, for some houses below their own reservation price.

**The turn.** She advances the tape to the spring. By 17 May 2022 the desk knew what anyone with a screen knew: the Federal Reserve had raised its policy rate by 25bp on 16 March and by 50bp on 4 May, and had announced on 4 May that its balance sheet would begin to shrink on 1 June. Volatility was up, the war in Ukraine was in its third month, and dealers were rethinking how much inventory they wanted to finance. Ines's own desk had raised its $\gamma$ in April, because the firm's treasury had raised what it charged the desk to finance bonds. It had left $\pi$ where it was.

The blotter tells what happened next in one number. At the same margin, the desk's hit rate on high-yield baskets had fallen to 11% *(illustrative)*.

"We're wide," Kaz says at once, playing the drill as if the date were real. "Eleven percent at a constant margin means the field is inside us. Cut $\pi$ and win back our share."

"Look at what moved," Ines says. "Not $\pi$. Our $\gamma$ moved, so our reservation price moved, so our bids moved. Most of the street's moved too; Man's account of that spring is that costs rose." She taps the hit rate. "We're not losing to the street. We're losing to the one house that hasn't moved its $\gamma$ yet. That's the winner's curse wearing a hit rate. If I cut $\pi$ to beat him, I become him."

"Balance sheet moved," Mags says, not looking up from her own card. "Before you argue about margins, ask the repo desk what the bonds cost to hold now. In my day you found that out from the treasurer, in person, and he enjoyed it."

Theo has been reading the other columns on the blotter, the ones nobody is arguing about. The engine's eviction ranking, which in 2021 had a short, thin top decile, has fattened: more lines per basket now cost more per dollar than the basket average, and they cost a lot more. A note in Ines's handwriting beside March says *custom creation baskets: none since Feb* *(illustrative)*. "Why do the creation baskets matter?" he asks. "We're not an ETF."

"Because they were the back door," Ines says. In 2021 a dealer that bought a basket full of bonds nobody wanted could deliver some of them into an ETF's custom creation basket, and ETF managers liked to put exactly the illiquid ones there (the evidence is in the annotation below the card). That was the outlet for the residue. When customization dried up, every unwanted line had to be sold one RFQ at a time, which in the master equation is the liquidation cost $c_i$ of the tail going up. "In 2021 the bad lines had an exit," Ines says. "In 2022 you owned them."

**The basket.** At 2:40 p.m. on the replay Tuesday a list arrives. Twenty-two lines of high yield, \$31mm of face, client sells, five dealers, all or none. The client is Dov Adler's pod at Vantress, which the desk quotes most weeks.

"Dov never sells us anything he owns," Ines says before anyone opens the list. "His book is flat. When a pod sends a one-way list, it's a short basket: every bond on it is one he thinks will fall, and he's selling it to us so the market can't see him do it one line at a time."

The engine paints the number in the corner: correlation with HYG, 0.4 *(illustrative)*. Theo has seen 0.55 once already today and 0.85 in a paper. "Lower than ours," he says.

"It's supposed to be. He built it to have nothing in common with the index. That's what he's paid for." The engine agrees. Its hedge solve removes almost nothing, because the lump is small by construction; the residual-risk term of (19.2) is nearly the whole quote. Then the adverse-selection model lights one line. Halvorsen Packaging 7.25% notes of 2029, \$3.5mm at 94, three times the basket's median line. The model's features are the ones it uses on any client: the line's size against the basket median and the client's own markout history in the name. The desk has bought Halvorsen from this pod twice in eighteen months and lost money both times *(illustrative)*. The engine prices the full list at 112bp of market value, evicts Halvorsen first, and prices the remaining twenty-one at 53bp.

> **The Pair.** *The pod's short basket. Dov Adler's pod at Vantress Capital Management (fictional composites); a replay as of Tuesday 17 May 2022, recorded in the Pair Book as a Chapter 19 note rather than a numbered pair. Halvorsen is fictional; positions, prices, fees and P&L are illustrative.* **Thesis.** After the quarter-end resize the pod is re-establishing the short legs of its pairs in one print instead of twenty-two RFQs. The biggest short is Halvorsen 7.25% 2029, a credit with an aggressive sponsor that Dov thinks the market is still pricing like its peers; four years later the pod will be short the same bond again, as the short leg of PB-01 (Chapter 1-B). **Legs.** The pod is long a matched set of bonds it already owns and sells \$31mm face of borrowed bonds in the basket, about \$29.5mm of market value, \$3.29mm of it Halvorsen. **What the hedge removes.** On the pod's side, market and sector beta: the longs carry the same DTS as the shorts, so the book is flat and what it sends is one-sided by design. On the dealer's side, almost nothing: a basket correlated 0.4 with HYG has an $R^2$ of 0.16, and the hedge takes out a sixth of its variance. **What idio remains.** Nearly all of it, which for the pod is the point and for the dealer is the quote. **What leaks.** First, the list itself: five dealers now know what the pod is short, and BlueBay's Campbell said what that costs when a basket is lost, "one house now knows my intentions" (The DESK, 2019-10-06). Second, the best idea: the dealer's adverse-selection model finds the line where the pod's conviction is concentrated and hands it back, so the pod's best short is the one line it cannot print, and it has to leg Halvorsen by RFQ the next morning at a worse level, the legging cost Chapter 18 (§18.6) describes and Chapter 18-B prices from the dealer's side. **What it costs.** On each short the pod owes the coupon, 7.25% on Halvorsen's \$3.5mm or about \$254k a year, plus a borrow fee off the prime broker's morning availability sheet (the call Wen Zhao makes for the pod today), 150bp on Halvorsen's market value or about \$49k a year, against Chapter 22's 50–300bp range; and the lender can recall the bonds on a day's notice, which the pod's analysts call the weather. The longs earn their coupons less funding. The basket itself costs the dealer's four terms plus $\pi$: 112bp of market value on the full list, about \$330k.

Put Dov's monitor and Ines's screen side by side, which in real life nobody ever can, and the two of them are computing the same number from opposite sides. The pod's own model expects the short basket to earn about 120bp of idio over the quarter, about \$355k, and a little more than half of it, about \$200k, from Halvorsen. The dealer's charge for the list is about \$330k, and its adverse-selection charge on Halvorsen alone comes to about \$190k *(all illustrative)*. The dealer is pricing the pod's alpha, and pricing it within about 8bp of market value. Eviction, seen from the pod's side, is the dealer refusing to be the counterparty to the pod's idio, which is the one thing the pod is paid to have.

**The card.** Ines stops the tape. "Bid or decline. If you bid, give me $\pi$ in basis points, the lines you want back, and the reason in one sentence."

Kaz bids all twenty-two at $\pi$ of 5bp: "Win back share; the field is wide." Mags declines: "A pod's short list is a list of bonds somebody clever thinks will fall. I don't buy those as a favour." Theo writes the longest card. He bids the twenty-one at $\pi$ of 15bp and hands back Halvorsen, and his reason is the sponsor's history of aggressive documents, which he knows because he has read them. Then he adds, in smaller letters, "15 is what we got paid in 2021."

Write yours before you read the grading.

> **[SOURCE EXTRACTION]** *Man_Revolutions_in_Credit_Trading_2023 p.3:* "The new market environment of higher volatility and quantitative tightening may also have left dealers inclined to commit less of their balance sheets to bond trading. The loss of customised baskets for the ETF creation/redemption process is likely to have been another aggravating factor."
>
> **Annotation.** Man's p.3 opens the story: "transaction costs for portfolio trading generally increased through the first half of the year… ultimately pricing backed off." Read it as three terms of (19.2) moving together. Balance sheet withdrawn means $\gamma$ up, so the risk term grows. The loss of custom creation baskets closes the dealer's outlet for illiquid residue, so $c_i$ for the tail rises (Koont, Ma, Pástor and Zeng show bond ETFs tilt creation/redemption baskets toward illiquid bonds, so losing customization hits exactly those lines). Competition easing means $\pi$ rises. A dealer running this chapter's engine in Q1 2022 would have seen its eviction loop hit its $\alpha$ budget or its $k_{\max}$ cap before reaching $\kappa^\star$ on HY baskets: the machine's way of saying *decline, or quote wide and lose*.

Then Ines plays the rest of the tape. Her 2022 self bid the twenty-one at $\pi$ of 25bp, ten basis points over the 2021 margin she had been holding, and handed back Halvorsen. Two of the five dealers declined. One bid all twenty-two, about 40bp wider than Ines on the whole list. Dov took Ines's counter-proposal and legged Halvorsen by RFQ at 9:10 the next morning, three-quarters of a point below where the basket would have paid, the price of being the only seller of a bond the whole street had just been shown. Halvorsen was down six points by the end of June. The twenty-one lines, net of the hedge, marked out within noise, and the desk kept about its margin *(all illustrative)*.

The grading is short, and it is Ines's. Kaz's card would have won the auction and owned the pod's best idea at the pod's price. "You'd have been the house that didn't move its $\gamma$," she says, and Kaz writes that down, which on this desk is applause. Mags's card was safe and earned nothing, which in May 2022 was not the worst outcome on the Street. Theo's card picked the right line for the right reason and charged 2021's margin for 2022's balance sheet. "Right card, wrong price," Ines says. "Liquidity tells you which line is expensive. Only the client tells you which line is informed. Evict the second kind first, and then charge what this year costs, not what last year paid." If your card bid all twenty-two at a thin margin, you were the second tier. If it declined, you were Mags. If it handed back Halvorsen, the hand history agrees with you.

The rest of the half-year graded the protocol itself. Pricing, in Man's word, "backed off," and the second tier went home. On the buy side, Man routed its flow back to electronic RFQ (§19.9 has its numbers), which is the client's own eviction decision applied to the whole protocol. The dealers' own account came four years later, when the Fed asked them what decides whether they take a basket. Composition is "very important" to four-fifths of active dealers, market conditions to two-thirds, and relationship and balance sheet to about one-half each (SCOOS, June 2025). Composition is the eviction term, market conditions are $m$ and $\gamma$ (§19.7), and balance sheet is $\gamma$ again. Ines closes the folder. "Every one of those answers," she says, "is a line on that card."

> **View From Another Seat.** *The dealer desk, in its own words.* The bank seat describes the same arithmetic from inside the balance sheet. Jefferies' global head of fixed income, Fred Orlan, put the constraint plainly in October 2023: "It's hard for investment banks to run large balance sheets in this environment because it isn't making a lot of money," and his EMEA colleague Fred Jallot said clients "would like to see us offering portfolio trading and blocks" (The DESK, 2023-10-26). Trumid's Paris Pender named the problem that follows on a Coalition Greenwich webinar in January 2024: "that risk ultimately needs to find a home," because "clients initiate portfolio trades, but dealers cannot send them back in the other direction." By February 2026 he described the protocol as one in which "margins have compressed and balance sheets have ballooned, elevating the importance of efficiently recycling residual risk" (Trumid, 2026-02-10). JPMorgan's co-head of credit systematic trading, Peter Grant, recorded during the April 2025 stress, called it "a liquidity aggregation problem" (J.P. Morgan *Making Sense*, recorded 2025-04-23). Read through (19.2), all four are talking about who sets $\pi$. The margin in a basket auction is set by the house with the cheapest exit for the residue. In 2021 that exit was the custom creation basket; in 2025 it is recycling the leftover lines to the next dealer, or to an all-to-all pool, before the risk term has had time to bite. A desk without an exit pays for the one it lacks in $\gamma$.

### Specification for AI Implementation (greedy eviction)

The counter-proposal has to be on Ines's screen before the response window closes, and it has to be right, because the client will take back exactly the lines the engine names. By feel, a trader can carve five lines out of a list of twenty. At 150 lines the cost of any one bond depends on all the others through the hedge residual, so the ranking changes after every removal. Sorting once and striking the top ten is wrong, and re-solving the whole hedge for each candidate is too slow for ninety seconds. The derivation gives an exact saving for each line and a cheap way to update the ranking after each eviction. What is left is a loop, which a desk automates precisely so that nobody argues about it while the clock runs.

Listing 19.5 is `evict_greedy`. It takes the `Basket`, the residual covariance from Listing 19.4, a vector `as_vec` of per-line adverse-selection charges in dollars, and the policy knobs: risk aversion `gamma`, the handling parameters, the liquidity multiplier `m`, a tolerance `alpha` for evicted market value (15% of gross), a cap `k_max` of ten lines and a cost target of 45bp of market value. Zeros are a legal value for `as_vec`, which is the trap the paragraph after the listing walks into. The function computes handling costs once, caches the coupling vector `Sres @ x`, and then loops. Each pass evaluates equation (19.7) for every line, divides by market value, masks out lines already evicted and lines too large for the tolerance still unspent, and picks the largest ratio. It stops if nothing is eligible or if the best ratio no longer beats the basket's current cost per dollar. Otherwise it subtracts one scaled column of `Sres` from the coupling vector, an $O(N)$ update, zeroes the line and recomputes. An assert inside the loop demands that the realized fall in total cost equals the predicted saving, so a later edit that breaks the algebra fails loudly. The outputs are the evicted indices in order and the path of cost per dollar. On the cold-open basket with no adverse-selection model, one eviction is enough: line 42 goes, and cost per dollar falls from about 55bp to about 32bp, under target *(illustrative)*.

It builds the counter-proposal before the quote goes out, and on the buy side it shows which lines a client is paying the dealer to take, which is how Wen chose her sweetener in §19.9.1. It is a greedy answer to a knapsack, which is fine at ten lines or fewer. Its blind spot is the sign structure. The guarantee that the best eviction always helps assumes non-negative off-diagonal risk, a one-sided basket, and about a third of real baskets mix buys and sells. In a mixed basket, offsetting lines hedge each other, and a removal can raise the cost per dollar. The stop rule exists for that case. When it fires early, the engine is telling you the basket is cheaper whole than carved.

*The full listing is [Listing 19.5 in Appendix F](#code-19-5).*

Hold on to that last assert. The engine, run without an AS model, evicts the stale \$18mm line and is satisfied: the basket is now below its 45bp target, and line 117 stays in. Line 117 looks like a model citizen. Its realized volatility is ordinary, its LCS is unremarkable, and it diversifies nicely. Everything the covariance matrix can see about it is fine. That is the point.

## 19.7 Stress Liquidity Commonality: When Every $c_i$ Moves Together

"In October 2008," Mags says, "we priced baskets by phone and by grudge, and the grudge was the only thing with a bid." Grudging respect follows: "Your matrix at least knows which bonds it can't sell. We had to find out one call at a time."

In calm markets the four terms of (19.2) are small and nearly independent. In stress they collapse into one term, and the reason is the difference between a hundred and fifty small pieces of bad luck and one large piece shared by all of them.

> **Math, Gently.** *Why the common multiplier does not diversify, and how long it lasts.* (a) Give each of 150 equal lines a cost that wobbles by 10bp around its average, each for its own reasons: one dealer is on holiday, another is long the bond already. Add them up and the wobbles partly cancel, so the basket's average cost per dollar wobbles by only $10/\sqrt{150}\approx0.8$bp. That is diversification, and it is why a basket can be cheaper than its lines. Now add one more ingredient, a market-wide multiplier that doubles every line's cost on the same afternoon. Nothing cancels it, because every line feels it in the same direction: the basket's cost doubles too, all 150 lines at once. Averaging shrinks noise that is different everywhere; it cannot shrink noise that is the same everywhere. (b) The multiplier is also slow. If a stress takes six weeks to recover half of the way back, the share of today's shock still present a week from now is $\varphi=2^{-1/6}\approx0.89$. After the five business days a dealer needs to work out of a basket, about nine-tenths of the stress is still there. You cannot wait it out; you can only price it. The algebra is next.

### 19.7.1 Derivation: a common multiplier in costs, a rank-one spike in risk

Equation (19.8) writes the basket's liquidation cost with a common multiplier $m$ and shows that its variance has one term that grows with the square of the basket's size and one that grows only with its size. Equation (19.9) carries the same shock into prices: nothing in the hedge menu spans it, so it lands in the residual covariance as a single extra direction of risk that no amount of diversification removes.

#### The Full Derivation

Let each line's cost carry a common liquidity multiplier: $c_{i,t}=\bar c_i\,m_t+\varepsilon_{i,t}$, with $m_t>0$, $m\approx1$ in calm markets, and $\log m_{t+1}=\varphi\log m_t+\xi_{t+1}$. The basket's liquidation cost is $L=m\sum_i\lvert x_i\rvert\bar c_i+\sum_i\lvert x_i\rvert\varepsilon_i$, with independent $\varepsilon_i$, so

$$
\operatorname{Var}(L)=\Big(\sum_i\lvert x_i\rvert\,\bar c_i\Big)^2\sigma_m^2+\sum_i x_i^2\,\sigma^2_{\varepsilon,i}.
\tag{19.8}
$$

The first term grows like $N^2$ and the second like $N$. **The liquidity factor does not diversify.** Adding lines to a basket dilutes idiosyncratic cost noise and leaves the common multiplier exactly where it was. The same shock moves prices: illiquid bonds fall more when $m$ jumps, by about $g_i=-\theta\,\text{LCS}_i\widehat P_i$ per unit of $m$. Nothing in the hedge menu spans $m$ (§19.4), so it survives into the residual as a rank-one spike:

$$
\Sigma^{\text{res}}_{\text{stress}}=\Sigma^{\text{res}}_{\text{calm}}+\sigma_m^2\,\mathbf{g}\mathbf{g}^\top .
\tag{19.9}
$$

Because $\mathbf{x}^\top\mathbf{g}\mathbf{g}^\top\mathbf{x}=(\mathbf{g}^\top\mathbf{x})^2$, a one-sided basket of illiquid bonds has the spike at full strength. A mixed buy/sell basket nets it, which is one more reason dealers love two-way baskets. The persistence parameter comes from recovery half-lives $h$ in weeks, $\varphi=2^{-1/h}$. The March 2026 episode's 4–14-week half-lives (below) give weekly $\varphi\in[0.84,0.95]$. So stress lasts longer than any PT unwind horizon, and the dealer cannot simply wait it out.

#### The warning in the LCS series

> **[SOURCE EXTRACTION]** *Ben_Dor_Quantitative_Credit_Portfolio_Management p.112:* "Over this time period, the LCS for the IG Index ranged from 0.59% to 3.40%. Although the spike in illiquidity that occurred in October 2008 is painfully clear, the index's LCS values had already doubled between June 2007 and September 2007, in the very early stages of the credit crisis."
>
> **Annotation.** Here are two calibration targets and one warning. The range $3.40/0.59\approx5.8$ is the empirical ceiling for $m$ at the *index* level, and the regime map below hits exactly 5.8 at its cap. With the LCS–VIX correlation of 0.90 (p.166), it licenses a one-factor liquidity model keyed to observable stress. The warning is the second sentence: LCS doubled *months before* the obvious crisis. A regime trigger keyed only to headline volatility arrives late. Key it to the cost data itself (bid–ask percentiles, ETF discounts) and expect $m$ to drift up before it jumps. Cotelioglu (2024, *Journal of Empirical Finance* 78) adds the mechanism a 2026 desk must respect: ETF ownership raises liquidity *commonality* in IG bonds. The plumbing that makes the lump cheap to hedge in calm markets also makes the residue's costs move together in stress.

### 19.7.2 Case Study: March 2020 and the April 2025 Tariff Week

#### Long Scene: Two Tapes (12 March 2020 and 7 April 2025)

*A replay, played at 1 p.m. on Friday 30 October 2026 while the week's markouts settle: the cold-open basket, run through two real weeks and cut off at the close of Thursday 12 March 2020 and of Monday 7 April 2025. The basket, the desk's regime readings and every engine output are illustrative; the dated market facts and the quoted words of real people come from the sources cited.*

The desk has replayed both weeks before, from the single-bond side, with a router and an RFQ log (Chapter 2, §2.9.3). Today Ines replays them from the basket side, and she makes one change to the tape before she starts. She takes Friday's 150 lines, the same synthetic basket that is still settling on the other screen, and drops it into the two weeks as if a client had sent it. For the 2020 tape she swaps one line for a split-rated Ford Motor Credit note on its way out of the investment-grade index, because a March 2020 basket without a fallen angel in it would be a lie (Chapter 1, §1.8.2, tells how Ford became one). On the other screen Friday's real markouts are ticking toward the close, and Theo keeps glancing at line 117 until Ines turns that monitor off.

"Same basket, two tapes," she says. "Your card is the same for both. Give me a regime score $s$ for each day. Tell me which of $m$, $\gamma$ and the basis you move, and by how much. And decide whether we quote at all." Write yours as the tapes run; the grading waits until both are done.

**Tape one: Thursday 12 March 2020.** The screen fills with a week every person in the room remembers from a different chair. Ines lived it from an investment-grade book at a dealer, the week her desk went from principal to "a phone book"; Mags lived it from a distressed desk; Kaz lived it in a university library, emailing a friend "free money?" about the discount on LQD (all three are in Chapter 2, §2.7.1). This afternoon nobody tells the stories again. The tape tells them instead. LQD closed that Thursday about 5% under a net asset value that nobody believed, and it traded almost 90,000 times that day while its five largest holdings traded an average of 37 times each (BlackRock's Q1 2020 earnings call, 16 April 2020; Chapter 20 has the day-by-day table). Every client who needed cash sold what it could sell, which was the ETF, and every order on the tape went the same way.

Kaz goes first and keys the regime score to the VIX, which is printing numbers last seen in 2008. "Volatility is the stress. The VIX says $s=2$, the cap. That's a risk event, so I move $\gamma$, four times calm, and leave the other two dials alone. The costs are the costs."

Mags is shaking her head before Kaz finishes. "The VIX is a headline. You want the thing that's actually expensive." She has the Ben Dor extraction from §19.7.1 open, the one about the index LCS that "had already doubled between June 2007 and September 2007, in the very early stages of the credit crisis." "Liquidity cost doubled in the summer, and the headlines came in October. If your thermometer is the VIX, you find out the patient has a fever when he's already in the ambulance. Key it to the cost data. Bid–ask percentiles. ETF discounts. The things that cost us money." By her reading the engine's own regime map (Listing 19.6) says the same as Kaz's VIX on this particular Thursday, $s=2$, with the ETF discount many standard deviations deep and the bid–ask at the top of its history, but it got there from the right place, and in the summer of 2007 it would have got there first.

Theo has been looking at the hedge column, because something about it bothers him. "If the ETF is 5% under its NAV," he asks, "what's the hedge? We sell HYG against the basket. But the HYG we're selling is itself the thing that's broken."

It is the best question of the afternoon, and Ines lets Kaz answer it, because Kaz wrote the formula. The one-factor version of the hedge in §19.4.1 says the hedge ratio shrinks, and a residual survives, in proportion to the basis noise $\sigma_u$ relative to the ETF's factor risk. In a calm month $\sigma_u$ is a rounding error. In March 2020 bond-ETF tracking error ran above 200bp against an average of 0.7bp (§19.4.1 has the source), so $\sigma_u$ became the dominant term. "The hedge didn't stop working," Kaz says slowly, working it out aloud. "It turned into a second position. You're long the bonds and short a thing that's moving for its own reasons. The residual isn't just idiosyncratic any more. It has the ETF's discount in it, and the discount is the same for every bond." So the basis dial has to move with the other two, and by the engine's map it moves to five times calm.

At $s=2$ the engine's three multipliers sit at their caps: liquidation cost $m=5.8$, risk aversion four times calm, basis five times calm. Run on Friday's basket the eviction loop stops at its $k_{\max}$ cap of ten lines, 14% of the market value handed back, long before the basket's cost falls anywhere near the 45bp target. Even at a regime score of 1, half the cap, Figure 19.5 shows the full list at 257bp and ten evictions leaving 148bp.

The cards for tape one come in. Kaz quotes, with $\gamma$ four times calm and costs at calm, a price that looks careful and is nearly 200bp too generous on the liquidation term alone, because the calm handling cost of about 40bp should have been multiplied by 5.8 *(illustrative)*. Mags declines. Theo moves all three dials to the cap, watches the loop run out of evictions, and declines the basket, but writes a second line on the card: offer to work the list for the client as agent, line by line, for a fee. Ines reads it and says nothing, because it is what her own desk did in March 2020 (Chapter 2).

**Tape two: Monday 7 April 2025.** Ines advances five years. The tariff announcement had come on Wednesday 2 April and the market had spent Thursday and Friday finding out what it meant. On the Monday the tape lights up. Fixed-income ETFs traded about \$99bn that day (The DESK, 2025-06-10; the figure is in the hedge-stack Trend Watch of §19.4). The next day US corporate bonds traded \$89.7bn, then a record, and 12% of it went through portfolio trades (Coalition Greenwich, citing Trumid; Chapter 22 explains why another day also gets called the record). Inside the same stress, JPMorgan's Olivier Cajfinger, whose remit covered investment-grade credit sales, said on a podcast recorded on 23 April that "there were days where portfolio trading made up to 25% of trades flow" (J.P. Morgan *Making Sense*, published 2025-05-09). On Wednesday 9 April the administration paused most of the new tariffs, which is context the cards are not allowed to know.

The engine's regime reading for Monday is an ETF discount about 2.5 standard deviations deep and a bid–ask at its 90th percentile, which the map turns into $s=1$ exactly: liquidation cost 3.4 times calm, risk aversion 2.5 times, basis 3 times *(illustrative; it is the worked example under Listing 19.6)*. Kaz's VIX score says $s=2$ again, and Kaz notices. "Same VIX story, half the cost story. So in 2020 my VIX score was right by accident."

"In 2020 it was late by accident," Mags says. "Today it's wrong on purpose."

"Why CDX and not the ETF?" Theo asks, when it is his turn. "The ETF's only 2.5 sigma rich to its NAV today, not 5% off."

"Because 2.5 sigma is still a basis," Kaz says, "and CDX's basis is a different one. Two hedges with different noise are better than one hedge with the same noise twice." The solve in Listing 19.3 does exactly that when it is given more than one instrument: it leans on whichever hedge's basis is quieter, and it refuses outright if the two are so alike that only their noise tells them apart.

What has changed underneath is the hedge menu and the clients. The desk in 2025 can hedge a basket with the ETF, CDX, total return swaps and, in small size, the listed credit-index futures that exchanges began offering in 2024, so the basis variance no longer sits in one instrument; the hedge solve spreads it across three or four, and the basis dial matters less for the same score. And the buy side has not switched its robots off. It has switched them to "stress parameters" (§19.10's Trend Watch has the source), so baskets keep arriving, and arriving two-way often enough to net part of the liquidity spike in (19.9). The dealers' own account, a few weeks later, was a dent: on net one-fifth of active dealers said their willingness to do portfolio trades relative to single-name market making had "decreased somewhat" (SCOOS, June 2025).

The tape-two cards: Kaz quotes with $\gamma$ at four times calm and the other dials flat, and is too wide on risk and too tight on cost at the same time. Mags quotes, small, with all three dials at $s=1$, and asks for a human signature. Theo quotes the whole basket at $s=1$, hedged in CDX rather than the ETF, and hands back the five lines whose cost per dollar the stress multiplier hits hardest.

**The grading.** Ines does tape one first. "In 2020 the right engine loses." A desk running this engine in March 2020 should have watched its regime score hit the cap, its eviction loop run into its $\alpha$ budget or its $k_{\max}$ cap on every high-yield basket, and its quotes widen until they stopped winning. That is the correct outcome. A PT engine that keeps winning in March 2020 at calm-market prices is subsidizing its clients' exits with its own capital. The tape agrees. Meli & Todorova's initial results show that portfolio trades had no cost advantage that month, with flows one-sided (the Trend Watch below has the passage). Somebody was buying all the same: quant funds traded \$116.5bn on MarketAxess Open Trading in the first three quarters of 2020, up 150% (Man, 2022, citing Business Insider). The relief came from outside the engine. The Fed announced its corporate credit facilities on 23 March and on 9 April extended them to fallen angels and high-yield ETFs (Chapter 20 has the dates and what the ETFs did on each), and Ford, cut to BB+ by S&P on 25 March, was exactly the kind of bond the extension now covered. Mags's card, decline, gets full marks. Theo's gets full marks and a look; the agency line is the one a client remembers. Kaz's loses money on every line, because the price looked prudent about risk and was reckless about cost.

Tape two is the one Ines cares about. "In 2025 the right engine quotes." The mature stack came through with wider parameters and a deeper hedge menu, and the protocol kept a double-digit share of the record day. Theo's card wins and makes money *(illustrative)*; Mags's wins less and makes money; Kaz's is the only one that is wrong in both directions at once.

Kaz looks at the two rows of grades for a long time. "My score was right about the temperature both times," Kaz says. "It was wrong about which dials the temperature turns."

"That's the whole lesson," Ines says. "One score. Three dials. They move together, because they're the same weather." Calibrate the cost multiplier, the risk aversion and the basis separately, and the engine comes out calm about costs and panicked about risk, or the reverse, and either one is wrong in both tapes. Kaz writes that down.

Grade your own card the same way. If you moved one dial, you were Kaz. If your 2020 card quoted the high-yield half at any price, the tape says you paid for someone else's exit. If your 2025 card declined, you were right in 2020 and five years out of date in 2025. The audio companion to the 2025 tape is in the Resource Graph at the end of the chapter.

### Specification for AI Implementation (regime and stress covariance)

The case studies end on a lesson that sounds easy and is not: the cost multiplier, the dealer's risk aversion and the ETF basis move together, from one regime score. The org chart works against it. The execution team owns the cost dial, the risk team owns the risk-aversion dial and the ETF desk owns the basis dial, each calibrated in a different quarter by a different person, and the quote that comes out is calm about costs and panicked about risk, or the reverse. A model review cannot tie three free dials to anything the committee can look at. So the desk builds one score from two things anybody can read off a screen at 3 p.m. without calling a counterparty: how deep the credit ETFs trade below their NAV, and where today's bid-ask sits in its own history. One score, three multipliers, no argument about whose dial it is.

Listing 19.6 has two functions. `regime` maps the ETF discount z-score and the bid-ask percentile to a stress score $s\in[0,2]$. The ETF channel is zero until the z-score falls below $-1$ and then adds one third per standard deviation, reaching 1 at $-4$. The bid-ask channel is zero until the percentile passes 80% and then rises linearly to 1 at the 100th. The two add, capped at 2. The score drives three multipliers, each a straight line in $s$: liquidity `m = 1 + 2.4 s`, risk aversion `1 + 1.5 s` and basis `1 + 2 s`. At the cap, `m` is 5.8, the ratio of Ben Dor's 3.40% to 0.59% IG LCS range *(illustrative calibration)*. The example in the asserts, a discount of 2.5 standard deviations and a 90th-percentile spread, scores exactly 1, which means `m` of 3.4, risk aversion 2.5 times calm and basis 3 times calm.

`stress_cov` implements (19.9). It builds the vector $g=-\theta\,\text{LCS}\times\text{mid}$ with $\theta=0.8$ *(illustrative)* and adds $(0.25s)^2\,gg^\top$ to the calm residual covariance, so the liquidity shock's volatility grows with the score. The result is the calm matrix plus exactly one rank. The asserts check that the spike is rank one and that it does not diversify. At $s=1$ on the cold-open basket it makes up about 28% of the basket's variance but only about 2% of the sum of the line variances, which is equation (19.8) in two numbers. Figure 19.3 plots the regime map on the left and that failure to diversify on the right.

![Figure 19.3: Left, one stress score s sets the liquidity multiplier, the dealer's risk aversion and the ETF basis together, reaching 5.8, 4.0 and 5.0 times calm at the cap. Right, adding lines shrinks the idiosyncratic residual risk per dollar from about 45bp to about 8bp, while the rank-one liquidity spike at s = 1 stays near 20bp and comes to dominate. Illustrative: Listings 19.4 and 19.6 on random subsets of the 148 ordinary lines of the synthetic basket.](assets/figures/ch19_stress_commonality.png)

It widens the quote continuously instead of flipping a stress switch, and it is a thermometer, not a forecast. Its weak spot is the dead zone. Below a one-sigma discount and the 80th percentile, `regime` returns exactly 1.0 on every multiplier, and a premium never counts at all. Ben Dor's warning in §19.7.1 is that LCS doubled months before the obvious crisis, so a map with flat floors will sit calm while the cost data drifts up. That is Mags's objection in Two Tapes (§19.7.2), and the answer is to move the thresholds, or add a slow-moving cost input, before the desk relies on the map.

*The full listing is [Listing 19.6 in Appendix F](#code-19-6).*

> **Trend Watch: PT in four stresses.** *March 2020:* Meli & Todorova's initial results show PTs "did not have lower transaction costs during March 2020, when volatility spiked due to the Covid-19 outbreak, and flows were one-sided." Bond ETF tracking error exceeded 200bp against a 0.7bp average (Todorov, BIS, 2021). *H1 2022:* PT costs rose as dealers committed less balance sheet and custom creation baskets disappeared (Man_Revolutions_in_Credit_Trading_2023 p.3; §19.6.2). *April 2025:* the tariff shock produced record volume days with 12% of 2025-04-08 volume via PT, and \$99bn of fixed income ETFs traded on 2025-04-07. On net, only one-fifth of active PT dealers said their willingness to do PT (relative to single-name market making) "decreased somewhat" (SCOOS, June 2025). *March 2026:* EUR IG bid–ask spiked 64% above its January average. Recovery took about 4 weeks in EUR IG, 6 in US HY, 8 in US IG, 13 in EUR HY and 14 or more in EM (MarketAxess data via The DESK, 2026-10-01). *What it means:* each episode is a jump in $m$ and $\gamma$, and the protocol's resilience has improved. In 2020 PT lost its cost edge outright. In 2025 most dealers kept quoting, with wider parameters.

## 19.8 Adverse Selection in Baskets: The Mystery Box

> **Poker Table.** "In a single-name RFQ," Ines says, "the player chose to bet. In a basket the player also chose *which cards to put face down among 150 face up*. You can't see the face-down cards. You can count how often this player has shown you a hand like this, and where it cost you." A PT is a bundle of 148 face-up cards that pay for the privilege of hiding two. The client is not cheating. That is the game. The dealer's edge is knowing which seats at the table hide cards, and what the cards usually are.

Glosten–Milgrom (Chapter 18) says the dealer's bid for one bond is $\mathbb{E}[V_i\mid\text{client sells }i]$. In a basket, the conditioning event is richer: the client sold *this bundle*, and chose to include line $i$. The good news is in the evidence. Li (2022) finds that PT-versus-voice cost differentials in IG do not respond to private-information proxies, so in IG baskets the inclusion signal is weak and a small AS charge suffices. The bad news is HY, where a line with an ad hoc group forming and a lender call on Monday is exactly the kind of card a well-informed seller hides in a stack of 149 others. For the ex-RSSG reader this is home turf. The toxicity features are Chapter 13's Priming Risk Score, the docket and the credit agreement.

### 19.8.1 Derivation: the inclusion model and the AS charge

> **Math, Gently.** *Log-odds and the logistic: a dial from "never" to "always."* Chapter 1 (§1.3.3) did Bayes in odds form, in a trader's head, and Chapter 5 (§5.5.3) stretched a probability so a straight line could fit it. The inclusion model uses both. Picture a dial whose left stop says "never" and right stop says "always." Each feature of a line turns the dial a fixed amount: a high Priming Risk Score turns it right, a lender call on Monday turns it further, a size three times the basket median a little more, a quiet calendar not at all. Add up the turns and you have a *score*, measured in log-odds. The logistic function $\sigma(\cdot)$ converts the score into a probability, and it does so in a way that can never leave the dial: a score of 0 is even odds, 1:1, a probability of 0.5; every step of 1.1 to the right multiplies the odds by three. So a score of 1.1 is odds of 3:1, a probability of 0.75, which is the number the engine will print for line 117. A score of $-4.6$ is odds of about 1:100, a probability near 1%, which is a quiet line. Twice the evidence does not mean twice the probability; it means the odds multiply again. The equations are next.

Equation (19.10) turns the dial into dollars. It says the dealer should expect line $i$ to be worth its composite mid less the probability that the client put it in the basket *because* of what it knows, times the size of the informed move; summed over lines, that expected shortfall is the adverse-selection charge $\text{AS}(\mathcal{B})$, the mystery-box term of (19.2). The hand history that checks it afterward is the by-line markout, defined in the same derivation.

#### The Full Derivation

Let $I_i$ indicate that line $i$ was included *because* the client holds adverse information. Model $\Pr(I_i\mid\mathbf{z}_i)=\sigma(\mathbf{w}^\top\mathbf{z}_i)$, logistic in observable toxicity features $\mathbf{z}_i$: PRS, proximity to a lender call, a live ad hoc group or Rule 2019 statement, log size relative to the basket median, and (in production) the client's own markout history in the name. Conditional on $I_i$, the expected informed move is $J_i$ (fraction of par), and otherwise zero. Then

$$
\mathbb{E}^{\mathbb{P}}\big[\widetilde P_{i,T}\mid i\in\mathcal{B},\mathbf{z}_i\big]=\widehat P_i-\Pr(I_i\mid\mathbf{z}_i)\,J_i\,\widehat P_i ,
\qquad
\text{AS}(\mathcal{B})=\sum_{i\in\mathcal{B}}\text{MV}_i\,\Pr(I_i\mid\mathbf{z}_i)\,J_i .
\tag{19.10}
$$

This is the first moment of the jump that Step 2 of §19.2 warned mean–variance would miss. Put the jump in the mean and the skew stops hiding. For a dealer *sell* (the client buys), the informed move is up, and the same charge applies with the sign of $J_i$ flipped.

*The hand history.* The diagnostic is the by-line markout, net of the hedge:

$$
\text{MO}_i(\tau)=x_i\big(\widehat P_{i,t+\tau}-p_i\big),\qquad \tau\in\{1,5,20\}\ \text{business days},
$$

measured on the residual after the factor and hedge P&L are stripped out. IDO or it didn't happen: a basket-level markout averages away the two lines that matter, and an unhedged markout is mostly the market. The "two cards face-down" signature is realized AS concentrated in one or two lines, at a scale far outside their idiosyncratic volatility.

#### Where the charge goes

The first time Kaz wired up the inclusion model, Kaz's instinct was to be fair to the client. "Why not spread it? Charge every line a little AS and nobody can say we singled them out." Ines ran the number in front of Kaz: the uniform charge widened the whole quote past every competitor and still left line 117 under-charged, because a small charge spread over 150 lines is a large charge on 148 innocent ones and a small one on the guilty line. The charge goes on the flagged tail, or it does no work at all. Ines's other rule is about the auction, not the lines. "Winner's curse is a different animal," she tells Theo. "That's the other seven dealers knowing something about the *whole* basket. It lives in $\pi$. The mystery box lives in the lines. Fold one into the other and you'll never find out which one was costing you."

### 19.8.2 Case Study: The Mystery Box at Line 117 (illustrative)

#### The Hand History: Friday 30 October 2026

*The cold open's basket, one week on. Every number in this case is illustrative, and Wexcombe Coatings, its lenders and its lender call are fictional. The mechanics are anchored in the real liability-management transactions of Chapter 13, such as the Serta Simmons 2020 uptier, in which a majority group exchanged into new super-priority debt under the agreement's "open market purchase" language (the most expensive three words in finance) and excluded lenders' first-lien paper repriced sharply; Chapter 13 has the sourced price path.*

Go back to 3:00:10 on the Friday before, when the engine had finished and Theo's card was face down on the desk. Line 117 has the fact pattern Chapter 13 taught the desk to fear: a Priming Risk Score of 0.85, an ad hoc group with a live Rule 2019 statement, and a lender call in three business days. Theo's 13-week model, now a liquidity-runway input to the PRS, puts the cash cliff about a quarter out. The engine's inclusion model puts $\Pr(I_{117})\approx0.75$, against a median line's 1%. With $J_{117}=1\%+15\%\times0.85\approx13.75$ points, the AS charge is about $3.28\text{mm}\times0.75\times0.1375\approx\$0.34$mm. That is roughly 16bp of the whole basket's market value, from a line with 1.6% of it. Add the stale line 42 and two lines with about 10% of the market value carry, by hand arithmetic, more than half of the basket's total cost: roughly 74bp all in, falling to about 35bp once both are evicted. (These are hand estimates on the synthetic basket. Your run will differ in the second digit.) These are the two lines paying for the whole trade. Figure 19.4 shows the eviction ranking that finds them, with and without the adverse-selection term.

![Figure 19.4: Ranked by the exact removal saving per dollar of market value, line 42 (orange) leads when only liquidity and risk are priced, while line 117 (violet) sits eighth, barely above the basket average. Add the adverse-selection term and line 117 jumps to the top at about 1,090bp. Illustrative: eq. 19.7 and Listings 19.5 and 19.7 on the synthetic basket.](assets/figures/ch19_eviction_ranking_flip.png)

At 3:00:20 the counter-proposal went out the way it always reads: *we bid the 148 at a 35bp concession; lines 42 and 117 we will work separately, or not at all.* Theo turned his card over beside it. It said: *148 at 50bp. Give back 117 and 42. 117: counsel hired, call Monday, runway a quarter. 42: big and quiet.* Right lines, right reasons, and 15bp too wide on the rest, which on a Friday with seven other dealers in the auction would have lost the 148 to somebody.

The client's answer came back thirty seconds later, and Ines read it aloud the way she reads a bet. "All or none, final." The response is itself information. A client who says "fine, keep the rest" was rebalancing. A client who says "all or none, final" may be telling you which card is face down. With fifty seconds left on the clock Ines bid the whole list at the engine's full cost plus a thin margin, about 80bp, and lost the auction to a dealer who bid about 50bp *(illustrative)*. "That's a fold," she said, and went to get coffee.

Monday's lender call took forty minutes. Wexcombe's management gave a liquidity update, said the company was "evaluating a range of options with the support of its advisors," and declined to take questions about the documents. On Tuesday morning the headline said the company was in talks with a group of lenders about a new-money financing. Nobody on the desk needed it translated.

By Friday afternoon the hand history is ready, and Ines runs it on her own losing bid, as if she had won, because a lost quote is a free experiment. The by-line markouts, net of the factor and hedge P&L, at one and five business days: 148 lines within their own noise; line 42 flat; line 117 down about one point after the first day and about five after the fifth. Unhedged and averaged across the basket, the same week reads as a mildly bad week for high yield, which it was, and which explains nothing.

Theo stares at line 42 for a while. "It's flat because nobody's printed it," he says. "Not because it was fine. It's still the same unknown it was last Friday, a week older." Then he looks at the unhedged basket number and says, before Ines can, "That's just the market. Strip it out and there's one line left. IDO or it didn't happen." Ines nods once.

"The client wasn't cheating," she says, replaying it for him as she replays every hand. "That's the game. They had a card they knew and we didn't, and they put it in a stack of 149 others because that is what a stack is for. We charged for it. The house that won didn't, and this week that line cost it about \$200k, more than its whole margin on the other 149 *(illustrative)*. If you have to be wrong about a basket, be wrong by losing it."

The judgment about where the adverse-selection model is worth running sits in the tape too. In investment grade, Li (2022) found that basket costs do not respond to private-information proxies (§19.8 has the finding), so an AS charge there is mostly noise added to a good quote. The model earns its keep in high yield, and only when it is charged to the flagged tail, one or two lines, the way the engine charged line 117 and nothing else.

Mags has watched the whole replay from her chair with her arms folded. "Back in my day," she says, "we found page nine about a month later, when the bond was in the low seventies and the salesman had stopped returning calls." She looks at the engine's eviction ranking, with line 117 at the top, for long enough that Kaz starts to fidget. "Fine," she says, and in Mags's vocabulary that is a standing ovation.

Grade your own card. If you named 117 and 42, you found both cards. If you named only 42, you were the engine without its adverse-selection term, which is the left half of Figure 19.4. If you bid all 150 near 35bp, you were the house that won.

### Specification for AI Implementation (adverse selection and hand history)

Everything the covariance matrix knows about line 117 is reassuring, and everything Theo knows about it is in his head, the credit agreement and a docket. That is a bad place to keep a number the desk charges for. When Theo is on vacation, the engine has to ask the same question he would ask, in dollars, in under a second. And afterward, when the basket has settled, the desk needs a record of whether the suspicion paid off, because a suspicion that is never scored cannot be calibrated. The charge before the trade and the markout after it are two halves of one control loop, and a desk that builds only the first has an opinion, not a model.

Listing 19.7 has those two halves. `as_charge` implements equation (19.10) in three steps. It first turns the toxicity features into inputs: PRS, a `call_soon` term equal to $e^{-\text{days}/5}$ (zero when no call is on the calendar and approaching one as the call nears), the ad hoc flag, and the log of the line's size relative to the basket median. A logistic function with hand-set weights then gives the probability that the line is in the basket because the client knows something. The constant of $-5$ puts a quiet line below 1%. Finally the probability is multiplied by market value and by an informed move of one point plus fifteen points times PRS. It returns the dollar charge and the probability for every line. The weights are *illustrative*, and nothing in the listing fits them. On the cold-open basket line 117 comes out at a probability of 0.75 against a median of 1%, and a charge of about \$339k, which is 81% of the basket's total. Hand that vector to the loop in Listing 19.5 and the order flips: line 117 is evicted first, then line 42, and cost per dollar falls from about 76bp to 59bp to 36bp *(illustrative)*.

`markouts` is the second half. For each line and each horizon of 1, 5 and 20 business days it returns signed notional times the later mid minus the traded price. The example draws 149 lines of noise scaled to their own idiosyncratic volatility, drops line 117 by 1, 5 and 14 points, and asserts that line 117 has the worst per-dollar markout at 20 days.

The charge runs before the quote, the markout after settlement, and the pile of markouts refits the weights client by client. The trap is written in the docstring: `markouts` takes its mid path as given and strips nothing out. It assumes the factor and hedge P&L are already removed. Feed it raw mids and the market's own moves swamp the one line that matters, and you will conclude that the client is fine and the hedge is broken.

*The full listing is [Listing 19.7 in Appendix F](#code-19-7).*

Replayed through the markouts, Ines's hand history reads the way she expected: 149 lines of noise and one line with a 17% per-dollar loss at 20 days. The basket-level markout, averaged over \$200mm, would have called it a mildly unlucky week.

### Deep-Dive Resource Graph

**Podcasts**

- **Jeremy Maletz** (*Money Stuff: The Podcast*, 2026-10-09). A Susquehanna market maker on flow versus bespoke trading and adverse selection; a quote is a posterior about who is on the other side, which is the mystery-box logic of this section. https://omny.fm/shows/money-stuff-the-podcast/jeremy-maletz
- **How Investors Fall Into Bias Traps with Economists Richard Thaler & Alex Imas** (*Masters in Business*, 2026-01-16). The plain-language route to the winner's curse: winning an all-or-none bid is itself information about what is in the box. https://omny.fm/shows/masters-in-business/how-investors-fall-into-bias-traps-with-economists-richard-thaler-alex-imas
- **What We Can Learn About Market Liquidity By Looking At Everyday Life** (*Odd Lots*, guest Karthik Shashidhar, 2017-10-09). A non-credit opener on why liquidity "sometimes just evaporates with little notice", and on the spread as the price of being picked off. https://omny.fm/shows/odd-lots/what-we-can-learn-about-market-liquidity-by-lookin

**Practitioner Writing**

- IFR (2021), Christopher Whittall, "US banks reap boom in bond portfolio and algo trading": https://www.ifre.com/bonds/1968608/us-banks-reap-boom-in-bond-portfolio-and-algo-trading
- **How Does Information Affect Liquidity in Over-the-Counter Markets?** (Michael Lee and Antoine Martin, NY Fed *Liberty Street Economics*, 2020-01-13). A short read on a model where dealers face informed traders and inventory cost; the Glosten-Milgrom half is the single-bond version of the basket charge in this section. https://libertystreeteconomics.newyorkfed.org/2020/01/how-does-information-affect-liquidity-in-over-the-counter-markets/

**Academic Papers**

- Li, O'Hara, Rapp & Zhou (2023), "Bond Market Illiquidity: Is Portfolio Trading the Solution?" (SMU Scholar record): https://scholar.smu.edu/business_finance_research/251
- Koont, Ma, Pástor & Zeng, "Steering a Ship in Illiquid Waters: Active Management of Passive Funds," NBER WP 30039; *Review of Financial Studies* (2025): https://www.nber.org/papers/w30039
- Cotelioglu (2024), "Do mutual funds and ETFs affect the commonality in liquidity of corporate bonds?" *Journal of Empirical Finance* 78: https://ideas.repec.org/a/eee/empfin/v78y2024ics0927539824000550.html
- Glosten & Milgrom (1985), "Bid, Ask and Transaction Prices in a Specialist Market with Heterogeneously Informed Traders," *Journal of Financial Economics*.

**Data & Code**

- scikit-learn `LedoitWolf` reference: https://scikit-learn.org/stable/modules/generated/sklearn.covariance.LedoitWolf.html

## 19.9 The Buy Side: When to Use a PT, and How to Build One the Dealer Will Love

Theo has one question left over from the hand history, and it is about the other side of the screen. "The client paid the winner about 50bp to take the whole list in one print," he says. "Most of those lines would have gone by RFQ for less, one at a time. Why does anyone send a list?"

"Because a week is a long time to own half a rebalance," Ines says. "You're asking what certainty costs. Go and read somebody who bought it for a year and then stopped."

Here is the second aha, and it belongs to the buy side. **The PT premium is the shadow price of all-or-none certainty.** Man moved its flow *into* PTs in 2021 and *back out* to RFQs in 2022–23, and both decisions were right, because the price of certainty and the cost of going without it both moved between the two years.

> **[SOURCE EXTRACTION]** *Man_Revolutions_in_Credit_Trading_2023 p.4:* "Two of the key challenges for such systematic techniques are having a high certainty of execution and having a relatively good sense of the likely transaction costs, as quantitative approaches depend on being able to model accurately which securities can be traded and at what cost. Furthermore, unfilled orders may create unintended and potentially unmodelled risk exposures in the portfolio."
>
> **Annotation.** The second sentence is the whole buy-side case for PT, and it can be priced. A partially filled rebalance leaves a random residual portfolio that the optimizer never chose. Its risk is real, and its cost is measured in tracking error, not bid–ask. The modern quant buy side therefore runs *both* routes through the same transaction-cost model and lets an inequality pick, rather than a relationship or a habit. Man's own p.5 verdict ("The vast majority of our trades are now sent as RFQs") is that inequality evaluated on a book whose electronic fill rates had risen.

Man's own trip from one protocol to the other is worth reading slowly, because it is the same inequality seen from a seat that runs it every night.

> **View From Another Seat.** *The systematic asset manager, in its own published words.* Man's account of its credit trading (*The Revolutions in Credit Trading*, June 2023) reads like the premium side of the inequality below moving through time. In 2021 "the majority of our order flow duly switched from voice based to portfolio trading" (p.2). In 2022 electronic venues began "delivering best execution from a transaction-cost perspective by slicing up trades more efficiently," and the firm went from roughly 30% of its high-yield flow and 60% of its investment-grade flow on electronic venues to more than 90% of all of it (p.3; Man Numeric data as of 1 May 2023). With that much flow electronic it could "make more frequent, smaller trades than was previously possible" (p.4), and its router now screens each order on whether the bond is actually available for RFQ, the quality of the responders, how often RFQs in it complete, and "whether a given trade size is digestible in RFQ form" (p.5). Vanguard's desk, which automates most of its traded volume (the figure is in §19.10's Trend Watch), describes the same machine from a larger seat. The seat's reading is that the PT decision is not made once, over lunch with a salesperson. It is evaluated every night, line by line, on fill probabilities the firm measures itself, and the basket wins only on the lines and the days where the dealer's premium is smaller than what the router expects to lose by slicing. A relationship enters the calculation as a fill rate or not at all.

### 19.9.1 Derivation: the all-or-none inequality

The inequality is a comparison a client can do on the back of the ticket. On one side sits the premium the list costs over sending every line by RFQ. On the other sits what the client loses by not paying it: the risk of whatever is left unfilled, the cost of trying again, and what the street learns from watching it try. The middle term is the one people misjudge, and a small number shows why. Suppose every line fills by RFQ with probability 0.9. Any one line is left over with probability 0.1, but any particular *pair* of lines is left over together with probability $0.1\times0.1=0.01$. So the unfilled residual is rarely a portfolio. It is one or two lonely lines, and its variance counts each line's own variance at a tenth of its weight and the covariance between any two lines at a hundredth. For a long-only fund holding hundreds of small lines, a lonely line is a nuisance. For a pod, where every line is half of a pair, a lonely line is a naked single-name position. Equation (19.11) says the list is worth its premium exactly when the premium is no larger than those three costs added up, and the derivation is next.

#### The Full Derivation

Take a target program $\mathbf{x}$. The RFQ route fills line $i$ with probability $\phi_i$ at cost $c^{\text{RFQ}}_i$, leaving a random unfilled residual $u_i=(1-\mathbb{1}_i)x_i$, with $\mathbb{1}_i\sim\text{Bernoulli}(\phi_i)$ independent. The PT route fills everything at $\sum_i c^{\text{RFQ}}_i+\Pi$. With the buy side's own risk aversion $\gamma_B$ and covariance $\Sigma$ over the time to re-trade, $\mathbb{E}[u_iu_j]=x_ix_j(1-\phi_i)(1-\phi_j)$ for $i\neq j$ and $x_i^2(1-\phi_i)$ for $i=j$. So

$$
\mathbb{E}[\mathbf{u}^\top\Sigma\mathbf{u}]=\sum_{i\ne j}x_ix_j(1-\phi_i)(1-\phi_j)\Sigma_{ij}+\sum_i x_i^2(1-\phi_i)\Sigma_{ii},
$$

and the PT is worth it if and only if

$$
\Pi\;\le\;\tfrac12\gamma_B\,\mathbb{E}[\mathbf{u}^\top\Sigma\mathbf{u}]\;+\;\sum_i(1-\phi_i)\,c^{\text{retry}}_i\;+\;\text{Leak}(N),
\tag{19.11}
$$

where $c^{\text{retry}}_i$ is the expected extra cost of re-trading an unfilled line and $\text{Leak}(N)$ is the information cost of showing $N$ separate RFQs to the street (Chapter 18). As $\phi_i\to1$ the right-hand side goes to zero and no premium is worth paying. That is 2022–23, when electronic RFQ fill rates and no-touch execution rose (Trumid's no-touch share is in §19.10's Trend Watch). In 2021, $\Pi$ was competed toward zero (§19.1), and the inequality held almost everywhere. Man's switch is (19.11) flipping sign, a calculation and not a mood.

#### Wen's Month-End List: Friday 30 October 2026

*The same Friday as the hand history, seen from a client's chair: the last business day of the month, at Vantress Capital Management. Vantress, Dov Adler's pod, Wen Zhao, Bea Castellanos and every pair, size and cost below are fictional composites, and the numbers are illustrative; the dated market facts and the quoted words of real people come from the sources cited.*

At 7:40 a.m. Wen Zhao has Dov's instruction from the night before on one screen and the Pair Book wall behind her. It is one sentence with a date, like all his instructions: close the five pairs whose residuals load hardest on the common component, by tonight's close, so the book is on its way to the number he promised Marcus for 30 November (Chapter 8, §8.8). That is ten legs: five long bonds to sell, and five borrowed bonds to buy back and return to their lenders. Each of them alone is a routine RFQ. Wen does not want ten routine RFQs, and she knows exactly why, because she has read the Pair Book's note on May 2022 twice. The pod sent a short basket to five dealers, got its best idea handed back, and paid three-quarters of a point to sell it alone the next morning (§19.6.2). The lesson she took from the note was not "never send a list." It was that whoever receives a list prices it through the four terms of (19.2), so a client might as well build the list to be cheap in each of them.

By 7:50 the list is two-way. A one-way list from a pod reads as a short basket or a fire sale, and a dealer's engine prices it as one or the other. A list that sells five longs and buys back five shorts, matched on DTS because the pairs were, has almost no lump at all. The buys hedge the sells, the dealer's hedge solve comes back nearly empty, and what is left is the pairs' own residual, which the pod is giving up precisely because it has turned out to be less idiosyncratic than advertised. That is the logic of Meli and Todorova's first lever (an interquartile increase in a portfolio's correlation with LQD improves its PT execution by 12%) taken to its end: the cheapest hedge is the one the list brings with it. "The one day our book looks like the index," Wen says to nobody, "is the day we sell the part of it that looks like the index."

At 7:55 Dov arrives with his coffee and finds that she has taken a pair out. Bea's note on the long leg of the fourth pair says its issuer amended a covenant definition in September in a way Bea does not like *(illustrative)*, and Dov's reason for closing that pair is half the common component and half Bea. "That's a card," Wen says. "If it's in the list, somebody's model finds it, hands it back, and four desks know we're out of it before we are."

Dov was at Vantress in 2022, which Wen was not. "Three-quarters of a point on Halvorsen," he says. "Side door." The fourth pair will leave by RFQ, one leg at a time, from 9:00: the leg-it-or-wait question of §18.6.3, answered on two lines, instead of an adverse-selection charge that would have landed on the one line the pod least wanted priced in public.

At 8:30 she goes looking for sweeteners. On a pod a sweetener cannot be a liquid bond the pod does not own; it is a bond the pod was going to sell anyway. The pair Dov had scheduled to close next Friday has both legs in the big high-yield ETFs, heavily owned and printed most days, so she pulls it forward. That is the second lever in the same paper, an interquartile increase in ETF ownership improving execution by 15%, and the move §19.6.1 described from the dealer's side as the sweetener: a line whose removal saving sits below the basket average lowers $\mathcal{C}/M$ for everything else. Meli and Todorova measured it in investment grade. Wen applies it to high yield on the strength of the pod's own fills, which is faith with a data set attached. The list is ten lines again, a different ten, about \$44mm gross.

At 9:20 Dov wants it sent. "Not now," Wen says. "At two o'clock every dealer has four index rebalances on the screen." Month-end is when standardized basket demand peaks: on MarketAxess, PT share in the last three days of the month was 7% higher than on other days in 2022 to date, and 67% higher in 2021 (The DESK, 2022-11-08).

"So they'll be busy," Dov says.

"They'll be busy pricing lists that look like the index, with hedges they already have on. Ours looks like the index today. I want it in that queue, not alone at nine in the morning."

The dealer count is the next argument. Dov wants eight, on the theory that more dealers mean a tighter price. Wen wants four. "Eight is the price of telling eight desks which pairs we're closing," she says. The losers learn as much as the winner, which is what BlueBay's Campbell meant by the line quoted in §19.6.2. She picks the four with the cleanest markouts against the pod's flow and an outlet for the residue in ETFs or CDX, because the house with the cheapest exit sets the margin (the dealer's seat in §19.6).

At eleven Dov asks the question Ines asked from the other side of the screen: why a list at all? Wen runs (19.11) on the pod's own fill history. Each line fills by RFQ with probability about 0.9, so one line in ten is expected to miss, and two together hardly ever. For the pod a missed line is half a pair, a single name with its own jump risk sitting naked over a weekend, and the risk term comes to about \$11k. Trying the missed line again costs about \$6k. The leak is the big one. Ten RFQs to five dealers each, over a morning, at month-end, and the pairs reassemble on any attentive blotter by lunch; she prices that at about \$22k. Together that is about \$39k of reasons to pay a premium. The pod's own history of two-way month-end lists puts the premium at about 7bp of \$44mm, about \$31k *(all illustrative)*. "Eight thousand dollars of certainty," Wen says, "and most of it is the leak. If this were Man's book it would go by RFQ. It isn't."

The platform's best-execution file asks one more thing of her, which Amundi's Minieri put in a sentence in the same 2019 piece as Campbell: "every line needs to be justified." Wen asks for the dealers' per-line levels with the quote. The engine on the other side of the screen has already computed each line's removal saving $\Delta_j$; it is the justification, and asking for it costs her nothing.

At 2:04 p.m. the list goes to four dealers. Three bid all ten lines, none hands one back, and the fourth declines. The winning premium is about 5bp, inside the pod's estimate, and Ines's desk comes second *(illustrative)*. On the blotter Theo watches his own engine price the lump at almost nothing and the residual at almost everything, and remembers Ines saying that Dov never sells the desk anything he owns. This time he did, with the shorts attached. The side-door pair came out at 9:00 and 10:15, about half a point worse than the pod's mark on the long leg *(illustrative)*, which is the price of not letting four desks learn about Bea's covenant at once.

At 4:30 Wen writes the execution note on the Pair Book wall: *List: ten lines, four dealers, two-way, month-end. Side door: one pair. The card stays out of the stack.* Dov reads it on his way out. "That's 2022," he says, "in one line."

## 19.10 Engineering for 90 Seconds

Here is the third aha. **"Ninety seconds" is a data-architecture statement, not a compute statement.** The product $\mathbf{x}^\top\Sigma\mathbf{x}$ for $N=150$ is 22,500 multiply-adds, which a phone does in microseconds. The ninety seconds go to *staleness*: whether line 83's composite is from today, whether its LCS applies at this size, whether its loading still reflects last week's downgrade, whether the hedge basis is quoted *now*. Everything $O(N^2)$ over the universe, or $O(\text{universe})$, is precomputed overnight and refreshed on events. The live path is lookups, one Schur complement, one quadratic form, a $2\times2$ to $5\times5$ hedge solve and a greedy loop. Pricing a PT in 90 seconds is 89 seconds of precomputation and human judgment, and one second of linear algebra. (The 90-second figure is this book's design target, not a sourced market statistic.)

| Step | Where it lives | Cost | Budget |
| :--- | :--- | :--- | :--- |
| Resolve 150 ids against the security master | precomputed index | $O(N)$ lookups | < 50 ms |
| Composite mid, `age`, `print_frac` | intraday cache, event-refreshed | $O(N)$ | < 50 ms |
| LCS at size, loadings $B$, $d_i$, PRS features | overnight + rating/docket events | $O(NK)$ | < 10 ms |
| $\Sigma^{\text{res}}$: Schur complement, PSD projection, condition guard | live | $O(N^2K+N^3)$ | < 50 ms |
| Hedge solve, AS model, greedy eviction ($k\le10$) | live | $O(H^3+kN^2)$ | < 30 ms |
| Human review: the flagged lines only | Theo and Ines | – | about 60 s |
| Slack for re-pulling stale composites and re-quoting | desk | – | about 25 s |

Down the last column, the human rows dwarf the machine rows, which is the point: almost all of the budget is spent deciding whether to believe the numbers, not computing them. Mags remembers when the whole table was one row, "a salesman and a fax," and it took half an hour.

> **Trend Watch: from 30 minutes to 90 seconds.** *2019:* a dealer could return a live, executable basket quote in about 30 minutes, and about eight to ten dealers could price baskets at all (The DESK, 2019-10-06). *2021:* "A client can sell hundreds of securities, sometimes over US\$2bn in an hour." Morgan Stanley's algorithmic pricing engine, live since 2017, had grown from about 500 bonds to more than 10,000 (IFR, 2021). *2024:* investors "expect near-instant liquidity, so dealers must price and quote faster than a human can by point-and-click" (Coalition Greenwich, 2024-06-11). *2025–26:* Trumid executed 88% of eligible RFQ line items fully no-touch (September 2025). Buy-side desks such as Vanguard automate about 70% of traded volume but switch the robots to "stress parameters" when markets gap (The DESK, October 2026). *What it means:* about a 20× compression in six years, delivered almost entirely by precomputation and cached fair values, not by faster arithmetic. The binding constraint now is data freshness and the kill switch.

The compression in that Trend Watch was bought with precomputation, which makes the overnight job part of the product. Most nights nobody sees it.

> **Quant-Shop Life.** *The Wednesday the liquidity doubled. A fictional composite: the bank, its systematic trading group, Yusuf, and every count and time below are invented. The seat is real (large dealers run credit systematic trading groups, and JPMorgan's co-head of one is quoted in §19.6); the market-structure facts are sourced.*
>
> The overnight job that feeds the basket engine starts at 3:30 a.m. and is supposed to finish by 4:45, and on most nights the only sign that it ran is a green line in the morning email. On this Wednesday in October 2026 the line is red. The job has failed its own row-count check: the table of per-bond liquidity features, which has one row per bond in the universe, has forty more rows than the universe has bonds *(illustrative)*. The engine does what it was built to do on a red morning. It loads yesterday's features, stamps every quote with a staleness flag, and waits for someone to care.
>
> The someone is Yusuf, a second-year quant who owns the liquidity features because the person who owned them before him moved to the rates desk. He finds the forty bonds by 8:15. Each appears twice, and for each the trailing-volume feature has roughly doubled overnight. By ten he has the prints: the same trade, at the same time, size and price, reported once as the outside trade and once as a transfer between two affiliates of one dealer. He is not the first to notice. MarketAxess said in its Q2-2026 results that duplicate trade reports "inflated U.S. high-grade TRACE volumes by up to 8% in June 2026," and FINRA's Regulatory Notice 26-16 extends the affiliate indicator that suppresses the duplicate leg, voluntary from 31 August 2026 and mandatory from August 2027. In the gap between voluntary and mandatory a feed can carry both kinds of dealer, and the group's dedup key had not needed to know which was which.
>
> The second discovery takes the afternoon, and it is worse. All forty bonds were in one basket the desk won at the end of September. The prints carry the PT modifier (§19.1), but the group's `print_frac`, the share of recent days with a print, had not looked at it, so it counted the basket's own prints, and the inventory moved between affiliates afterwards, as evidence that these bonds trade. Last month's portfolio trade was manufacturing this month's liquidity. Had the job passed, the engine would have priced those forty bonds as if they printed twice as often as they do, and the lines it trusted most would have been the ones the desk had most recently been paid to take off somebody's hands.
>
> The fix is two lines of logic and six hours of proving them. The dedup key gains the affiliate flag and the reporting-side fields, and `print_frac` is recomputed with inter-affiliate legs dropped and with PT-modified prints no longer counted as evidence that a bond trades on its own. Yusuf reruns ninety days of features, diffs them against the old ones, and writes a one-paragraph note on why 212 bonds moved by more than a tick of LCS *(illustrative)*. The ticket closes at 7:40 p.m. Nobody says thank you. The next morning the line in the email is green, and the only person who reads it is Yusuf.
>
> At 12:40 that day, with the job still red and half the desk at lunch, an investment-grade basket had come in anyway. Lunch is no longer quiet: Barclays found that the share of US IG volume traded between noon and one had risen from 11.3% to 12.5% since 2022 (The DESK, 2025-09-17). The engine priced the list on yesterday's features, the staleness flag tripped the group's lunch-hour auto-quote limit, and the quote went out only after a trader came back with a sandwich and signed it. Ninety seconds, this section says, is mostly precomputation. This is what the precomputation looks like on the day it goes wrong: a red line at 4:45, a check that refuses to pass, and one person's Wednesday.

**What ROBO built from the vague version.** Theo asked ROBO to "price the basket fast." ROBO cached yesterday's composites, skipped the staleness fields because they slowed the parse, and returned a confident bid in four milliseconds. Eleven lines had not printed in a month. It was fast. It was also an answer to a question nobody had asked.

**The precise spec** adds kill switches. Refuse to auto-quote if more than 20% of gross MV has `age > 10`. Require human sign-off if regime score $s\ge1$, if any line has $\text{PRS}>0.7$, or if any line carries more than 25% of total cost. Refuse outright if the condition guard fails. Log the four-term decomposition for every quote, won or lost, because losing quotes are how $\gamma$ and $\pi$ get calibrated.

### Specification for AI Implementation (the full engine)

Seven listings in, the engine is still a parts bin. The product the desk sells is one call: the inquiry and two readings off the tape go in, and a price, a list of lines to hand back, a hedge and a reason come out, all inside the budget in the table above while Theo and Ines review the flagged lines. That call also has to leave a record. The quotes the desk loses are the only data it will ever get on $\gamma$ and $\pi$, so every quote, won or lost, gets its four-term decomposition logged. The last listing is therefore deliberately dull. It calls everything above in order, and the interesting part is what it hands back.

Listing 19.8 is `price_pt`, which runs the chain in the order the chapter built it. It reads the regime from the ETF discount and the bid-ask percentile, and scales risk aversion and the liquidity multiplier by it. It builds the residual covariance with the regime's basis multiplier (Listing 19.4), adds the liquidity spike if the score is above zero (19.6), computes the adverse-selection charges (19.7) and runs the greedy loop unless told not to (19.5). It then drops the evicted lines, re-solves the hedge on the survivors, and assembles the four terms of (19.2) in dollars: handling, risk, adverse selection and hedge half-spread. The output is a dictionary with the cash for the kept basket (fair value less cost), each term, the cost in basis points of kept gross market value, the hedge, the evicted ids, a `hit_target` flag, the regime and the elapsed milliseconds.

The asserts walk the whole chapter. The bid sits below fair value, and the four terms sum to the cost. The calm run evicts L117 and then L042 and meets the target, and the counter-proposal costs less per dollar than the full basket. The same basket at a regime score of 1 costs more than twice as much. The client-buys mirror image has an identical cost and an ask above fair value. On the cold-open basket, the full list costs about \$1.56mm, or 76bp: \$829k of handling, \$420k of adverse selection, \$293k of risk and \$16k of hedge. Without lines 117 and 42 it costs about \$0.67mm, or 37bp *(illustrative)*. Figure 19.5 stacks those terms for the full list and the counter-proposal, in calm and in stress.

![Figure 19.5: The four terms of the bid for the same basket in four situations (the hedge half-spread, under 1bp, is too thin to see). Evicting lines 117 and 42 halves the calm cost to 37bp, under the 45bp target, but at a stress score of 1 the full list costs 257bp and even ten evictions leave 148bp, so the engine cannot reach its target. Illustrative: price_pt (Listing 19.8) on the synthetic basket.](assets/figures/ch19_cost_stack_by_scenario.png)

It is the core of the live path and the replay engine for lost quotes, the one Ines ran on her losing bid in the hand history. Its blind spot is that the listing ends at the number. Of the kill switches in the spec above, only the condition guard is coded, and it raises. Nothing refuses a quote on stale composites, a PRS above 0.7 or a regime score of 1. The function reports them through `hit_target` and `regime`, then returns a confident cash figure anyway. In stress, ten evictions are not enough, `hit_target` goes false, and the number still arrives with a straight face. Adverse selection and the hedge half-spreads are also not scaled by the regime. Reading those flags, and declining or escalating, is a wrapper's job.

*The full listing is [Listing 19.8 in Appendix F](#code-19-8).*

### Deep-Dive Resource Graph

**Practitioner Writing**

- Coalition Greenwich (2024-06-11), Kevin McPartland, "Corporate Bond Dealers Focus on Trade Automation": https://www.greenwich.com/node/150811
- Coalition Greenwich (2026-02-17), Kevin McPartland, "Dealer net short in corporate bonds sets record": https://www.greenwich.com/node/158326
- **Hitting Its Stride: Portfolio Trading's Next Phase** (Paris Pender, Trumid, 2026-02-10). A venue's own view: PT above 21% of US electronic corporate-bond trading in early 2025 versus 6% in 2021, plus three 2026 predictions; read it as a dated vendor claim to check against TRACE, which sets the flow the 90-second engine has to quote. https://www.trumid.com/news/2026/trumid-pt-viewpoint-february-2026/
- **Electronic trading in fixed income markets** (BIS Markets Committee Papers No. 7, Study Group chaired by Joachim Nagel, 2016-01-21). The central-bank baseline for the electronic RFQ protocols the engine answers inside: better market quality "with exceptions", and liquidity that may have become less robust; read the executive summary. https://www.bis.org/publications/electronic-trading-fixed-income-markets

**Data & Code**

- MarketAxess monthly volume release, May 2026, with the estimated share of US credit portfolio trading: https://s201.q4cdn.com/767283836/files/doc_news/2026/06/05_2026_Volume_Release-Final.pdf
- **Trading Volume Statistics for March and First Quarter 2026** (MarketAxess volume release, 2026-04-07). Record total PT ADV of \$2.3 billion and an estimated 21.9% share of US credit PT; Table 1C gives TRACE PT ADV of \$8,478 million in March 2026 against \$6,608 million a year earlier, a free denominator for sizing the flow (vendor-reported, so cite the table, not the headline). https://s201.q4cdn.com/767283836/files/doc_news/2026/MKTX-Volume-Release-March-2026-Final.pdf
- **Monthly Activity Report, May 2026** (Tradeweb, PDF dated 2026-06-04; the page prints only the month). Global cash credit PT ADV up 41.5% YoY, and a footnote defining "non-comp PT" as a portfolio trade sent to a single dealer at a lower fee, a reminder that the same word covers protocols in which the engine faces different competition. https://www.tradeweb.com/49c163/globalassets/newsroom/monthly-activity-reports/2026/may/may-2026-tradeweb-monthly-data-report.pdf

## 19.11 Desk Debrief

**Finder.** One row per tool: where its equation lives, the picture that explains it, the scene where it worked or broke, and its listing.

| Concept | Equation | Intuition (box) | Judgment (scene) | Code |
| :--- | :--- | :--- | :--- | :--- |
| The master equation: four terms and a margin | (19.1)–(19.2), §19.2.1 | The price of not flipping (§19.2); a week as a histogram, and the trapdoor in it (§19.2.1) | Theo's card in the cold open, graded in the hand history (§19.8.2); Ines at the equation's edges (§19.2.1) | [Listing 19.1](#code-19-1), [Listing 19.8](#code-19-8) |
| Handling cost at size | (19.3), §19.3.1 | The door that narrows (§19.3.1) | Hana's duration-twice bug, 13 January 2026 (§19.3) | [Listing 19.2](#code-19-2) |
| The hedge and the residual | (19.4), §19.4.1 | A hedge ratio is a slope, and the residual is what the slope leaves (§19.4.1) | The hedge with the ETF at a 5% discount, in Two Tapes (§19.7.2) | [Listing 19.3](#code-19-3) |
| Staleness as variance | (19.5), §19.5.1 | Fourteen photographs of 150 people (§19.5); the drunk and the lamppost (§19.5.1) | Line 42's 22× (§19.5.1); Kaz's springing lien (§19.5) | [Listing 19.4](#code-19-4) |
| Eviction on exact removal savings | (19.6)–(19.7), §19.6.1 | The slope of the hill and the walk back to the car (§19.6.1) | The Year the Second Tier Went Home, H1 2022 (§19.6.2) | [Listing 19.5](#code-19-5) |
| The stress spike | (19.8)–(19.9), §19.7.1 | Why the common multiplier does not diversify, and how long it lasts (§19.7) | Two Tapes, 12 March 2020 and 7 April 2025 (§19.7.2) | [Listing 19.6](#code-19-6) |
| The adverse-selection charge and the hand history | (19.10) and the by-line markout, §19.8.1 | A dial from "never" to "always" (§19.8.1) | The Hand History, Friday 30 October 2026 (§19.8.2); where the charge goes (§19.8.1) | [Listing 19.7](#code-19-7) |
| The all-or-none inequality | (19.11), §19.9.1 | Ten lonely lines, in prose (§19.9.1) | Wen's Month-End List (§19.9.1); Man's seat (§19.9) | Exercise 5 |

The bullets below are the same chapter with the scenes taken out, short enough to tape to a monitor.

- **A PT bid is four terms plus a margin:** fair value, minus liquidation cost, minus residual risk *after the hedge*, minus adverse selection, minus $\pi$. Every term is in dollars until the very last line.
- **You are pricing one lump and a residual.** The hedge turns $\Sigma$ into $\Sigma^{\text{res}}$, and $\Sigma^{\text{res}}$ is the re-hedged covariance for *any* basket, so eviction re-hedges for free.
- **LCS is a standalone price.** Use only its handling share inside a basket, scale it for size, and never multiply it by duration again.
- **Staleness is variance, not a haircut.** Line 42 is not a bad bond; nobody knows what it is worth, and that ignorance is what the engine prices.
- **Evict on exact removal savings, and recompute after every eviction.** Liquidity scores evict line 42. Only the AS term evicts line 117.
- **The liquidity factor does not diversify.** In stress, one regime score must move $m$, $\gamma$ and the basis together.
- **The hand history is by line and net of the hedge.** A basket-level markout averages away the two cards that were face down. IDO or it didn't happen.
- **Ninety seconds is 89 seconds of precomputation and judgment, and one second of linear algebra.**

### The Spec You Hand the Robot

> Build `price_pt(inquiry, model_state, market_state) -> Quote`. **Inputs:** a struct-of-arrays inquiry ($N\le500$ lines: id, signed par \$, composite mid as a fraction of par, age in business days, print fraction, LCS at \$4mm, OASD, OAS, sector, daily idiosyncratic vol, PRS, days to lender call, ad hoc flag). Also: overnight loadings $B$ $(N,K)$, factor covariance $\Omega$ $(K,K)$, hedge loadings $A$ $(H,K)$ and basis covariance $U$ $(H,H)$, plus live ETF discount z-score and bid–ask percentile. **Compute (all under $\mathbb{P}$, all in dollars):** handling cost (19.3); idiosyncratic variance with staleness, print-frequency inflation and ridge (19.5); $\Sigma^{\text{res}}$ by Schur complement (19.4), PSD-projected, with $\operatorname{cond}\le10^6$; the stress spike (19.9) from one regime score that also scales $\gamma$ and the basis; the AS charge (19.10) from a logistic inclusion model; greedy eviction on exact removal savings (19.7), stopping at the target cost per dollar, $\alpha$ of MV, or $k_{\max}$ lines; and the minimum-variance hedge of the kept basket. **Return:** cash, cost in \$ and in bp of gross MV, the four-term decomposition, hedge notionals, evicted ids, a `hit_target` flag and latency. **Refuse** if mids look like points, if more than 20% of MV has age $>10$, or if a guard fails. **Escalate to a human** if $s\ge1$, if any $\text{PRS}>0.7$, or if one line carries more than 25% of cost. **Tests:** CE matches Monte Carlo under Gaussian P&L; hedged variance equals the Schur form; costs are side-symmetric; eviction strictly lowers cost per dollar; stress cost is at least 2× calm on the reference basket; the live path runs in under 1 s.

### Exercises

1. **Find the two lines.** Using `price_pt(b0, evict=False)`, attribute total cost to lines with the exact removal savings (19.7). Show that their sum exceeds $\mathcal{C}$, and explain the excess using the off-diagonal term in §19.6. Then find the two lines with the largest $\Delta_j/\text{MV}_j$ without reading the cold open.
2. **The ETF goes to a 5% discount.** Suppose HYG trades at a 5% discount to NAV with a z-score of $-4$. Run the engine with `etf_disc_z=-4.0, bidask_pct=0.97`. Which term of (19.2) grows most? Does eviction still reach the 45bp target within $\alpha=15\%$? If not, what should the desk tell the client, and is "decline" a valid quote?
3. **ROBO and the stale universe.** Set every line's `age` to 30 and `print_frac` to 0.05, and price the basket. ROBO returns a number. Write the kill-switch test that should have stopped it, and decide whether it belongs in `Basket.__post_init__` or in `price_pt`.
4. **Kaz's springing lien.** Kaz proposes modelling line 117's priming risk by multiplying its `sig_idio` by 10 instead of using the AS term. Compare the two quotes and the two hedges. Explain, with Step 2 of §19.2, why the variance version both under-charges the jump and distorts the eviction ranking and, if applied to the whole return series, $\mathbf{h}^\star$.
5. **Flip the inequality.** Take the cold-open basket `b0` as the program, with RFQ fill probabilities $\phi_i=0.9$, $\gamma_B=5\times10^{-7}$ per dollar, a retry cost of 5bp per dollar and $\Sigma$ from §19.5 over a one-day re-trade horizon, and compute the maximum PT premium $\Pi$ the buy side should pay under (19.11), ignoring leakage. Then lower $\phi_i$ to 0.6 and recompute. Which year, 2021 or 2023, does each number describe?
6. **The mixed basket.** Make 50 of the 150 lines client *buys*. Show that the stress spike $(\mathbf{g}^\top\mathbf{x})^2$ shrinks, and explain why a dealer should bid tighter for a two-way basket even when every line's LCS is unchanged.

### Deep-Dive Resource Graph

**Podcasts**

- Bloomberg Professional, *Market Dialogues* (2025-07-07), "How is portfolio trading changing the fixed income landscape?" with David Krein, Anna Han and Shahaan Kazi: https://professional.content.cirrus.bloomberg.com/professional2023/insights/markets/how-is-portfolio-trading-changing-the-fixed-income-landscape/
- **BlackRock Sees Credit Pain as Tariff Confusion Reigns** (*The Credit Edge*, Bloomberg Intelligence, 2025-04-24). Mitch Garfin of BlackRock with James Crombie and Robert Schiffman on credit spreads widening under trade-war uncertainty, with portfolio trading among the topics; the audio companion to the April 2025 tariff week of §19.7.2. https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/blackrock-sees-credit-pain-as-tariff-confusion-reigns
- **The Present and Future State of Corporate Bond Portfolio Trading** (Coalition Greenwich webinar, host Kevin McPartland with Paris Pender of Trumid, 2024-01-17; summarized on Trumid's site). A dated share datapoint for the Trend Watch in §19.1 (PT at 8% of TRACE volume in Q4 2023, vendor-sourced) and a dealer-side view that quoting baskets had become routine. https://www.trumid.com/news/2024/coalition-greenwich-webinar-the-present-and-future-state-of-corporate-bond-portfolio-trading/

**Practitioner Writing**

- Man Group (2023), *Revolutions in Credit Trading* (shelf: `Man_Revolutions_in_Credit_Trading_2023`).
- The DESK (2019-10-06), "The burgeoning portfolio trading business": https://www.fi-desk.com/trading-protocols-portfolio-trading-lynn-strongin-dodds/
- The DESK (2022-06-01), "Barclays: Portfolio trading 8% of US credit market volume": https://www.fi-desk.com/barclays-portfolio-trading-8-of-us-credit-market-volume/
- IFR (2021), "US banks reap boom in bond portfolio and algo trading": https://www.ifre.com/bonds/1968608/us-banks-reap-boom-in-bond-portfolio-and-algo-trading
- Meli & Todorova (2022), "Portfolio Trading: Part III — In Crisis and Calm," Barclays Research (title only).
- **Hitting Its Stride: Portfolio Trading's Next Phase** (Paris Pender, Trumid, 2026-02-10). A venue's own view of PT's share (above 21% of US electronic corporate-bond trading in early 2025 versus 6% in 2021) and three 2026 predictions; a dated vendor claim to check against TRACE, useful for §19.1 and §19.9. https://www.trumid.com/news/2026/trumid-pt-viewpoint-february-2026/
- **Overnight Corporate Bond Trading** (Farshid Abdi with Marco Rossi and Botao Wu, Microstructure Exchange webinar, 2026-09-15). Trades between 6:30 p.m. and 8:00 a.m. are not disseminated on TRACE until the next morning, are larger and move prices more persistently, and predict returns on the issuer's other bonds; a fresh fact for the staleness and age inputs of §19.5. The season page links the recording and the paper. https://microstructure.exchange/season

**Academic Papers**

- Meli & Todorova (2023), "Portfolio Trading in Corporate Bond Markets": https://www.aeaweb.org/conference/2024/program/paper/a7z3SGGN
- Li, J. S. (2022), "Frictional Intermediation, Inventory Hedging, and the Rise of Portfolio Trading in the Corporate Bond Market": http://www.aeaweb.org/conference/2023/program/paper/9TfsndSa
- Li, O'Hara, Rapp & Zhou (2023), "Bond Market Illiquidity: Is Portfolio Trading the Solution?": https://scholar.smu.edu/business_finance_research/251
- Koont, Ma, Pástor & Zeng, "Steering a Ship in Illiquid Waters: Active Management of Passive Funds": https://www.nber.org/papers/w30039
- Cotelioglu (2024), "Do mutual funds and ETFs affect the commonality in liquidity of corporate bonds?": https://ideas.repec.org/a/eee/empfin/v78y2024ics0927539824000550.html
- Ledoit & Wolf (2004), "A Well-Conditioned Estimator for Large-Dimensional Covariance Matrices," *Journal of Multivariate Analysis* 88(2), 365–411.
- Almgren & Chriss (2000), "Optimal Execution of Portfolio Transactions," *Journal of Risk* 3(2).
- Dick-Nielsen, Feldhütter & Lando (2012), "Corporate Bond Liquidity Before and After the Onset of the Subprime Crisis," *Journal of Financial Economics* 103(3).

**Data & Code**

- Federal Reserve SCOOS, June 2025 (special questions on credit portfolio trading): https://www.federalreserve.gov/data/scoos/files/scoos_202506.pdf
- FINRA TRACE: Regulatory Notice 22-12 (portfolio-trade modifier, effective 2023-05-15) and Regulatory Notice 26-16 (affiliate indicator), via https://www.finra.org/
- scikit-learn `LedoitWolf`: https://scikit-learn.org/stable/modules/generated/sklearn.covariance.LedoitWolf.html
- MarketAxess monthly volume releases (estimated share of US credit portfolio trading): https://s201.q4cdn.com/767283836/files/doc_news/2026/06/05_2026_Volume_Release-Final.pdf
- **Trading Volume Statistics for March and First Quarter 2026** (MarketAxess volume release, 2026-04-07). Record total PT ADV of \$2.3 billion and an estimated 21.9% share of US credit PT; Table 1C gives TRACE PT ADV of \$8,478 million in March 2026 against \$6,608 million a year earlier, the best dated free denominator for the Trumid figures (vendor-reported, so cite the table, not the headline). https://s201.q4cdn.com/767283836/files/doc_news/2026/MKTX-Volume-Release-March-2026-Final.pdf
- **Monthly Activity Report, May 2026** (Tradeweb, PDF dated 2026-06-04; the page prints only the month). Global cash credit PT ADV up 41.5% YoY, and a footnote defining "non-comp PT" as a portfolio trade sent to a single dealer at a lower fee; read it beside the MarketAxess release, since the same word covers protocols with different competition (§19.1, §19.9). https://www.tradeweb.com/49c163/globalassets/newsroom/monthly-activity-reports/2026/may/may-2026-tradeweb-monthly-data-report.pdf

<!-- STATUS: COMPLETE -->
