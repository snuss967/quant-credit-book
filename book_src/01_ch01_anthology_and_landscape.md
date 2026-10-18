# Chapter 1: The Anthology of the Desk & The Modern Quant Credit Landscape

**2:58 p.m., a Friday, Theo Marsh's third week.**

The RFQ arrives the way bad news always arrives on a credit desk: politely, in a grey box, with a countdown. *Client sells \$15mm, Halvorsen Building Products 7.25% senior unsecured notes due 2029, B3/B-, all-to-all, five dealers in competition. Respond in 00:14.* (Halvorsen is fictional. The lender call that ended at 2:00 p.m. today is, sadly, a genre.)

Theo's hand goes to his pocket, where the USB stick with his old 13-week cash flow model lives "for emotional support." With the other hand he opens the credit agreement: 350 pages, 2019 vintage, a definition of "Consolidated EBITDA" that runs to four pages and has never once been in a hurry.

"Engine has us at 91.40," says Kaz, without looking up. "Residual vol is normal. Inventory is flat. Let's just assume Gaussian."

"The engine wasn't on the call," says Mags.

Ines rolls her chair over. "What's the pot, what are the odds, and who at this table knows more than you?"

"But what does the credit agreement say?" Theo asks.

"Nothing it didn't say at 1:59," Ines says. "The question is what got said at 2:00, and whether the person hitting our bid was on the line when it got said."

The timer reads 00:11. Theo's 13-week model has thirteen columns. The RFQ has eleven seconds. Ines taps the screen. "One of those is going to be reborn as something useful. Guess which."

At 00:06 the thought arrives, fully formed and in the wrong language. *If they were on the call, the right bid is a lot lower than 91.40, and I don't know how much lower.* He knows what an ad hoc group does with a 2019-vintage agreement and a four-page EBITDA definition. He knows that "supported by" in a press release usually means "drafted by." He has sat in the room, on the other side of the glass, while people decided which lenders would be invited in and which would read about it afterwards. What he does not have is a number, and the grey box accepts only numbers.

Theo does not answer, and in credit, not answering is also a price. The desk passes, another dealer prints the bonds at 91.25, and at 4:40 p.m. an 8-K announces a "comprehensive liability management transaction supported by an ad hoc group of lenders." The bonds open Monday at 78.

At 7:15 on Monday, with the 78 still glowing on the screen and his coffee going cold, Theo asks Ines what he should have done: bid lower, bid smaller, pick up the phone? Ines does not look away from her monitors. "You should have had a number for 'they were on the call.' This chapter is where you get one."

That is the whole chapter in one RFQ. Someone was selling. They were selling *now*. And the only question that mattered was not "is Halvorsen a good credit?" but **who is selling, why now, and what is that worth?**

The number Ines means is three bets stacked on top of each other: what the bond is worth, what it costs to hold, and what the seller knows that you don't. The chapter builds each one in turn, and on the train home four weeks later Theo writes down what he can do with them.

## 1.1 The Epistemological Clash: PJT RSSG vs. The Automated Market Maker

Theo's last Monday at PJT Partners (RSSG) in Midtown Manhattan began, as most of them had, with a credit agreement and a deadline that was not his. The unit of account on that floor is the **bespoke legal bottleneck**, and that week the bottleneck was a 350-page Senior Secured Credit Agreement from 2019. He had already spent 90 hours on the 13-week cash flow forecast. Now he was reading Section 7.06 for the fourth time, calculating the exact dollar capacity inside the *Available Amount* builder basket, because the whole engagement turned on one question: could an ad hoc group holding $50.1\%$ of the Term Loan B strip collateral coverage through an amendment and drop the intellectual property into an unrestricted subsidiary? Time on that floor moves in weeks. The unit of output is the negotiated outcome, and RSSG's role is to advise on it, not to own it. Somebody's client, on one side of the table or the other, ends up with a $20\text{-point}$ priming premium over left-behind minority lenders *(illustrative)*, or ends up as one of the left-behind lenders. Theo's real asset, which nobody had ever put on a balance sheet, was that he knew *which clause made the 20 points possible*, whichever side he had sat on.

His first Monday on the desk, a systematic credit market-making business that this book will follow for twenty-eight chapters (fictional, like everything the cast does), began with a login and a feed. The unit of account here is **conditional expected value per unit of inventory variance per day**. Nobody reads an indenture cover-to-cover during market hours. Instead, an automated pricing engine ingests real-time FINRA TRACE prints, CME Treasury futures ticks, OPRA single-stock option implied volatility surfaces, and HYG/LQD ETF creation-redemption baskets, and it produces a price for every bond in the universe before Theo has found the coffee machine. The clock is not the week; it is the RFQ. When a client sends an all-to-all Request for Quote on MarketAxess asking for a bid on $\$15\text{ million}$ notional of a stressed $B3/B-$ high-yield bond, the desk has **a few seconds** to solve an adverse selection problem. Ines showed him the equation on his first afternoon, written on the whiteboard in a hand that had once filled in tournament scorecards. Before we look at it, one piece of notation needs unpacking, because it carries most of the chapter.

> **Math, Gently.** *What does $\mathbb{E}[\,\cdot \mid \mathcal{F}_t, \mathcal{O}_t]$ mean?* The $\mathbb{E}$ is an average: the average of all the things that could happen, each weighted by how likely it is. The vertical bar means "given," and what comes after it is everything you are allowed to know when you take the average. $\mathcal{F}_t$ is the public information at time $t$: prices, filings, the tape. $\mathcal{O}_t$ is the order flow, and here it means one specific, slightly uncomfortable fact: *somebody just asked you for a bid.* That fact changes the average, because people do not ask at random. A tiny example: a coin pays 100 or 78 with equal odds, so on its own it is worth 89. Now suppose that, given that this particular person is offering it to you, there is a 60% chance they have already seen it land on 78. The coin is now worth $0.6 \times 78 + 0.4 \times 89 = 82.4$. Same coin, same public information; the only new fact is that someone chose to sell it to you, and it cost 6.6 points. The bid equation does the same arithmetic with the desk's numbers, and in §1.3 it turns Kaz's 91.40 into 83.60.

Here is what Ines wrote:

$$
\text{Quote Bid } B^* = \mathbb{E}[V_{t+\Delta t} \mid \mathcal{F}_t, \text{Order Flow } \mathcal{O}_t] - \frac{1}{2}\gamma \sigma^2_{\text{IDO}} (2q + \Delta q) - \Lambda_{\text{tox}}(\mathcal{O}_t)
$$

Where:

- $\mathbb{E}[V_{t+\Delta t} \mid \mathcal{F}_t, \mathcal{O}_t]$ is the posterior fair value of the bond (here $V$ is the bond's value, not the firm's assets; §1.3 renames it $m$ to keep the notation table honest) conditioned on public filtration $\mathcal{F}_t$ and the event that a counterparty is actively trying to sell size $\Delta q$.
- $\gamma$ is the desk's risk-aversion parameter, $\sigma^2_{\text{IDO}}$ is the unhedged idiosyncratic variance of the bond over the holding horizon after stripping Treasury duration and CDX beta, and $q$ is current desk inventory.
- $\Lambda_{\text{tox}}(\mathcal{O}_t)$ is the **Adverse Selection Penalty**: the probability that the seller has just left a lender call or analyzed a covenant trapdoor and knows an LMT or earnings miss is imminent, times the size of the move they know about.

Read the equation as three bets stacked on top of each other, because that is how the rest of this book is organized:

| Term | What it asks | Who on the desk owns it | Where the book builds it |
| :--- | :--- | :--- | :--- |
| Fair value $\mathbb{E}[\cdot]$ | What is this bond worth to a neutral holder? | Kaz (models), Mags (recoveries) | Part II (distributions, Merton, intensities), Part VI (vol surfaces, CDS basis) |
| Inventory skew $\tfrac12\gamma\sigma^2_{\text{IDO}}(2q+\Delta q)$ | What does it cost me to *hold* it until someone else wants it? | Ines (risk), the PM | Part III (stripping beta to get $\sigma_{\text{IDO}}$), Part V (microstructure), Part VIII (sizing) |
| Toxicity $\Lambda_{\text{tox}}$ | Does the seller know something I don't? | Theo, and everything he knows about credit agreements | Ch 3 (RFQ adverse selection), Part IV (LMTs), Part VII (NLP on dockets and documents) |

In the cold open, Kaz's engine got the first two terms right and set the third to zero. That is not a modeling error you can fix with more data. It is a modeling error you fix by knowing what a lender call is.

> **View From Another Seat.** *The multi-strategy relative-value pod (a generic seat, not a named firm).* A capital-structure pod inside a multi-manager fund sees the same Friday RFQ and asks a different question. It is not obliged to answer at all; nobody's franchise depends on it showing a bid in fourteen seconds. What it wants to know is whether the lender call means the capital structure is about to come apart: an uptier usually helps whoever ends up holding the new super-priority paper and hurts whoever is left behind, so the pod's question is not "what is this bond worth?" but "which Halvorsen instrument do I want to own on Monday, and what do I short against it?" The dealer has to price the third term because the RFQ is in its inbox. The pod gets to choose the hand. Much of this book is about the dealer's problem, because that is the seat Theo took, but it is worth remembering that the most dangerous seller on Friday afternoon may be someone who chose this hand very carefully.

### Why the Hybrid PJT RSSG + Quant Architect Owns the Future

The week after Halvorsen, Kaz spent a slow Wednesday afternoon reading Man Group's 2022 survey of quant credit, because the risk committee had asked for "context" and Kaz interprets requests literally, like ROBO with a doctorate. Near the end of the paper Kaz stopped and read a sentence aloud to the desk, in the tone of someone reporting a bug in somebody else's code.

"'Quant credit is yet to move into distressed debt.' Fine. 'This is a high-touch asset class.' What does high-touch mean? Is it a liquidity measure?"

"It means someone has to read the thing," Mags said, not looking up from a recovery waterfall. "All of it. Including the schedules."

"There are schedules?"

"There are always schedules."

Theo, who had once spent a long weekend on Schedule 1.01(b) of a credit agreement and could still recite its carve-outs, read the sentence over Kaz's shoulder and felt something he had not felt in three weeks on the desk: recognition. Here it is, in full:

> **[SOURCE EXTRACTION]** *Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.42:* "Quant credit is yet to move into distressed debt – this is a high-touch asset class that requires a significant degree of human intervention, but further data capture and analysis around restructurings and recovery may make this possible."
>
> **Annotation.** Read that sentence as a job description. "Human intervention" is the reader: someone who knows which basket in the negative covenants is the trapdoor and which "sacred right" is load-bearing. "Further data capture and analysis around restructurings and recovery" is Parts IV and VII of this book: the Priming Risk Score (Ch 13), regime-switching default and recovery distributions (Ch 14), and parsers that turn credit agreements and dockets into features (Ch 25). The 2022 boundary Man describes is not a law of nature. It is a backlog. Notice also *where* the boundary sits: precisely where the third term of the bid equation, toxicity, dominates the other two. In IG, the fair-value and inventory terms do most of the work and quants have been competitive for a decade. In distressed, $\Lambda_{\text{tox}}$ is most of the bid, and nobody has yet built a machine that reads a cooperation agreement. The modern desk departs from Man's 2022 framing in one respect: it does not wait for the data to be "captured" by someone else. It hires the person who already knows where the data is buried.

It is tempting to turn that sentence into a slogan about one tribe beating the other, and the first edition of this chapter did. The truth is less flattering to both tribes and more useful. A statistical model trained on yesterday's prices treats CUSIPs as exchangeable time series, and when a company executes a Serta-style uptier or a J.Crew-style trapdoor drop-down, the correlations it learned can break in a day: the event is a structural discontinuity, and a model with no column for "the documents permit this" cannot see it coming. Quants know this, which is why they build regime filters (§12.4 is the book's own answer). The banker's failure mode is the mirror image: treating every credit as an artisanal snowflake and refusing to turn judgment into a probability that a machine can use, compare, and be graded on. Neither failure is a law of nature. The interesting question is what happens when the two are made to work together, and on that question the industry has started to publish numbers rather than opinions.

The first number is about money. Barclays QPS estimates that funds using quantitative *screening* in IG and HY hold between \$90bn and \$140bn (Mateer et al., Barclays QPS & Credit Research, 2024, cited by Impax, 19 September 2025; see §4.1), several times the dedicated systematic pool. Most of the industry's quant money is not running a model; it is running a model *past* an analyst. The second number is about skill. In the same research, as reported by Impax, the issuer-level hit rate in US investment grade was about 58% overall, about 66% when analyst and quant signals agreed, and about 52% when they conflicted (see §28.8). Agreement between the two tribes was worth eight points of hit rate; disagreement nearly erased the edge. That is the hybrid's case, stated without marketing: the alpha in modern credit accrues to whoever can translate legal and structural mechanics into state-space features that an automated pricing and risk engine can consume, and then let the engine tell them when they are wrong.

> **Poker Table.** Ines draws it on the back of a markout report. "Two players at one seat. The quant sees every hand anyone has ever played, but only the cards that hit the table. The banker sees one hand at a time, but she can see the other players' faces: who's on the lender call, who just hired counsel, who stopped answering the phone. Put them in separate rooms and each loses to the player who has both. Put them in the same chair and argue about every hand, and you get the 66% when they agree, plus a cheap warning when they don't. The 52% is the hand history telling you to fold." She caps the pen. "The best seat at this table isn't the smartest one. It's the one that knows which information it's missing."

---

## 1.2 Evaluating the Market Set in Quantitative Credit

On Theo's second afternoon, before he had been allowed to touch a quote, Ines took the marker back to the whiteboard and drew six chairs around an oval. "This is the table," she said. "Before you play a hand, you learn who is sitting at it, what each of them has to do, and when. Nobody here is stupid. Most of them are just not free." She labelled the chairs, and then, instead of explaining all six, she wrote *Halvorsen, Fri 2:58, \$15mm* in the middle of the oval. "The table below is the map. Three of these chairs could have sent you that RFQ. Tell me what Friday looked like from each of their screens."

She tapped the first chair, which was the desk's own kind: another dealer or portfolio-trading desk. "Say it came from a desk like ours. They picked up \$40mm of Halvorsen in a portfolio trade on Tuesday *(illustrative)*, the name's volatility jumped on Thursday, and at 2:30 on Friday their single-B limit went red. They know nothing about any lender call. They're flattening because a number on a risk screen changed colour, and they want it gone before the close, because that's when limits are measured. From that chair, Friday was a limit breach. If that was the seller, Kaz's 91.40 was a fine bid." She paused. "Our own weakness, while we're here, is the one you watched: we're the person a well-informed seller wants to find."

The third chair was capital-structure arbitrage. "Say it came from a pod at a multi-strategy fund, long the bonds and short the stock, because the equity put skew said the bonds were cheap. At 1:30 the prime broker recalls the borrow on the stock, and the trade has to come off, both legs, today. From that chair, Friday was a funding problem. They always unwind at the worst time, because the worst time is what causes the recall."

Theo asked whether that was a law. "It's an observation," Ines said. "Laws are what you call observations that have cost you money twice."

The sixth chair was the open-end high-yield fund. "Say it came from a fund that took a redemption ticket on Thursday. They sell what they can sell, not what they want to sell, and Halvorsen was liquid enough to show five dealers. From that chair, Friday was a settlement date." She underlined *a known calendar date, or the day after a bad headline.* "You'll meet this chair again in March 2020, on the day its ETF was the only honest price in the market."

Then she drew an arrow from every chair to the desk's chair. "Three sellers, three screens, one RFQ in our inbox, and every one of them is forced by something: a limit, a recall, a redemption. When they sell, they sell to someone. Of the people sitting across from us right now, which ones are forced, and which ones are choosing?"

"And the one who was on the call?" Theo asked.

"Isn't on the board," Ines said. "That chair never sits in the same place twice."

The whiteboard became the table below, and it is the chapter's map. Its job is to let the desk isolate pure Idiosyncratic Return (**IDO**) by first understanding each player's mechanical constraints. The last column is the one that matters most: it says what each player is *contractually or regulatorily forced* to do, and on what clock. The "Representative Firms" column names a firm or fund only where this chapter cites it (Man's and BlackRock's own papers, Apollo's earnings call, the ETFs in the March 2020 data); elsewhere it describes the seat generically, because a table of employers deserves sources (Chapter 4 maps the industry properly).

| Strategy / Desk Archetype | Representative Firms | Holding Horizon | Primary Edge | Structural Vulnerability (How You Arb Them) | Forced to Do What, and When |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Automated OTC Market Makers & PT Desks** | *Generic:* electronic market makers and bank portfolio-trading desks | Milliseconds to 10 Days | ETF Creation/Redemption loops, Portfolio Trading (PT) pricing speed, cross-asset latency | Exposed to **toxic fundamental flow** on bespoke LMTs, covenant priming, and bankruptcy docket surprises | Flatten inventory against risk and balance-sheet limits; widen or pull quotes when toxicity spikes. Clock: intraday to days. |
| **Systematic Factor Credit Pods** | Man Numeric (Man 2022, 2023, §1.1, §1.6); BlackRock Systematic (§1.5); other quant asset managers | 1 to 6 Months | Cross-sectional factor harvesting (Value, Equity-to-Credit Momentum, Carry, Quality) across 2,000+ issuers | Slow to react to discrete structural breaks (M&A CoC waivers, drop-down rumors); mechanical rebalancing creates predictable flow | Rebalance on schedule and de-gross on drawdown or gross-leverage limits. Clock: the rebalance date, which other people can also read. |
| **Capital Structure & Volatility Arbitrage** | *Generic:* multi-strategy pods and credit relative-value hedge funds | 5 Days to 6 Months | Merton-model dislocations, Equity Put Skew vs. High-Yield Spreads, CDS-to-Bond Basis, Orphan CDS | Vulnerable to squeeze dynamics in repo/borrow markets and basis blowouts during liquidity crunches | Unwind when borrow is recalled, margin rises, or the basis breaches a stop. Clock: days, and always at the worst time. |
| **CLO Vehicles (Par-Constrained Institutional Buyers)** | *Generic:* broadly syndicated loan CLO managers (independent, bank-, insurer- and asset-manager-affiliated) | Buy-and-Hold (Reinvestment Period) | Structural leverage via AAA-to-Equity tranche arbitrage | **Forced mechanical sellers** when CCC buckets exceed $7.5\%$ or upon default; cannot easily fund new-money post-reorg equity rights offerings | Carry CCC excess at market value in OC tests; divert cash to senior notes on breach; sell or stop reinvesting to cure. Clock: the next test or payment date. |
| **Insurers & Annuity Writers (Ratings- and Capital-Constrained)** | Athene (Apollo's annuity affiliate; Apollo Q4 2025 call, 9 Feb 2026); other life and annuity writers | Hold to maturity (liability-matched, 5 to 30 years) | Liability-matched spread capture; illiquidity premium from private placements | Capital charges jump at the IG/HY line, so downgrades produce slow, concentrated selling of the same bonds by many holders | Sell, or hold more capital, after a downgrade to speculative grade. Clock: quarters, not days. |
| **Open-End HY Funds & Bond ETFs (NAV-Redemption Sellers)** | iShares (HYG, LQD; §1.8); other HY mutual fund and ETF complexes | Daily liquidity to end-investors | Cheap beta delivery; daily liquidity on illiquid assets | Liquidity mismatch: they sell what is liquid, not what is expensive; ETF prices gap below NAV when authorized participants stop arbitraging | IG index funds sell fallen angels at the month-end rebalance and HY index funds buy them at inclusion; open-end funds meet redemptions within days. Clock: a known calendar date, or the day after a bad headline. |

Everyone in that table is smart. Most of them are not the problem. The problem is the last column: every row has a trigger that converts a rating, a test, or a redemption into a sale, at a time you can often predict and in a size you can often estimate. A forced sale is **information-free about the bond and information-rich about the seller**. The rest of this chapter is about telling those two kinds of information apart, at speed, for money.

> **View From Another Seat.** *The CLO manager (a generic seat; no manager is named).* Imagine the same Friday from the fourth chair, and suppose the RFQ is not for Halvorsen's unsecured notes but for its term loan, which a CLO is far likelier to own, and which the agencies have just cut one notch, from B3 into Caa1 territory. The CLO is the marginal buyer of new leveraged loans: CLO managers buy "nearly three-quarters of all leveraged loans issued" (Deutsche Bank Flow, 7 Oct 2025), so their rulebook shapes loan prices in a way no single fundamental view can. The rulebook says that CCC and Caa1 loans above the typical 7.5% limit are marked, in the over-collateralization numerator, at the *lowest* market value in the CCC bucket, not at their own price (Kundu, ESRB Working Paper No. 141, Mar 2023, pp. 7–8). Kundu finds that the average CCC loan in the sample was priced at 85 while the cheapest CCC loan in each CLO averaged 58, which means the haircut can reward selling a *higher*-priced CCC to shrink the excess. The bucket is a soft wall, not a cliff: S&P Global Ratings reported in September 2023 that about 42% of the 554 reinvesting US BSL CLOs in its index had CCC exposure above 7.5%, yet just over 1% were failing a junior OC test (S&P, CLO Insights, 29 Sep 2023). So the manager is not panicking. She is optimizing, against a test date. Her view of the RFQ, if she could type it into the box: "I am not selling because I think it's cheap or rich. I am selling because my CCC bucket is 7.9% and the test date is Thursday." From the desk's chair that is close to the best sentence a seller can say. It means $\pi$ is low, the size is predictable, and the price pressure will fade once Thursday passes. The danger is assuming every CLO sale sounds like that one. A manager who sells *before* the downgrade, a week ahead of the agencies, is a different kind of seller, and Chapter 21 shows how to tell them apart in the flow.


---

## 1.3 The Bid Equation, Derived

The seed equation in §1.1 looks like something a vendor would put on a slide. It is better than that: it is the reservation price of a risk-averse dealer, plus one application of Bayes' rule, plus a cost. Derive it once and every later chapter becomes a commentary on one of its terms.

### 1.3.1 Setup and units (measure: $\mathbb{P}$, the desk's own beliefs)

Everything in this section is a physical-measure object. The mid $S_t$ may come out of a risk-neutral ($\mathbb{Q}$) model, but the question "will I lose money on this trade over the next week?" is a $\mathbb{P}$ question, and the markout that answers it is measured in $\mathbb{P}$.

- $S_t$: the desk's mid for the bond, in **price points per 100 of par**.
- $q$: current inventory in **\$mm of par** (long positive). $\Delta q > 0$: the size the client wants to sell to us.
- $h$: the expected holding horizon in **years** (five trading days is $h = 5/252$).
- $\sigma_{\text{IDO}}$: the standard deviation of the bond's price change *after* the hedges (Treasury futures for rates, CDX or an ETF for spread beta), in **points per $\sqrt{\text{year}}$**. Chapter 8 is entirely about getting this number right.
- P&L is measured in **\$mm·points**: one point on \$1mm of par is one unit, which is \$10,000. The risk aversion $\gamma$ is then in units of $1/(\$\text{mm}\cdot\text{pt})$.

> **Math, Gently.** *What is a distribution, and what is a certainty equivalent?* Think of the desk's P&L over the next five days as a bag of possible outcomes, each written on a slip of paper, with more slips for the likelier outcomes. That bag is a **distribution**. Its **mean** is where the bag is centred: shake out every slip, add them up, divide by the number of slips. Its **variance** is how wide the bag is: the average squared distance of a slip from the mean, and the **standard deviation** is the square root of that, back in points. A **certainty equivalent** is the sure amount you would accept in exchange for the whole bag. A risk-averse desk will swap a bag for less than its mean, and the mean–variance rule says how much less: subtract $\tfrac12\gamma$ times the variance. A tiny number: a position with expected P&L of $+1.0$ and a standard deviation of $2.0$ (so variance $4$), held by a desk with $\gamma = 0.5$, has $\text{CE} = 1.0 - \tfrac12 \times 0.5 \times 4 = 0$. The desk is exactly indifferent between holding it and not; it would want to be paid something extra to take it on. That "paid extra" is the inventory term, and §1.3.2 computes it. Not every bag has the same shape. This chapter will meet the normal (many small wiggles), the lognormal (proportional wiggles that cannot go below zero), the Poisson (rare jumps), and the fat-tailed bags that real credit P&L comes in, and each gets its own box when it first appears.

Assume the desk evaluates a position with a mean–variance certainty equivalent, $\text{CE}(X) = \mathbb{E}^{\mathbb{P}}[X] - \tfrac12\gamma\,\mathrm{Var}^{\mathbb{P}}(X)$. This is exact for exponential (CARA) utility with Gaussian P&L, and it is the standard first-order approximation otherwise (the "otherwise" is the Ways This Blows Up box below). Let $m = \mathbb{E}^{\mathbb{P}}[S_{t+h}\mid\mathcal{F}_t, \mathcal{O}_t]$ be the fair value **conditional on the fact that this RFQ arrived**. That conditioning is the whole game, and we will come back to it.

### 1.3.2 The inventory term

> **Math, Gently.** *Pricing by indifference.* Here is a trick that runs through the whole book. You do not ask "what is this bond worth?" in the abstract. You ask: at what price would I feel exactly the same about doing the trade and not doing it? Below that price, you are happy to buy; above it, you would rather pass. To find it, write down how you feel about the world without the trade (your current inventory, with its risk), write down how you feel about the world with it (more inventory, more risk, less cash), and set the two equal. Everything that makes the second world worse, the extra variance in particular, gets charged to the seller as a lower bid. With the cold open's numbers ($\gamma = 0.02$, and $\sigma^2_{\text{IDO}}h = 1.270$ pt² over the five-day holding period), every \$mm the desk *already* holds costs $0.02 \times 1.270 \approx 0.025$ points of bid, because the new bonds will wobble together with the old ones. The \$15mm block costs half that per \$mm on itself, about $0.0127$ points per \$mm, or $0.19$ points in all, because a position's variance grows with the square of its size and you are only paying for the new part of the square. Add $5 \times 0.025$ for the five bonds already held and you get, to rounding, the 0.317 the desk computes in §1.3.3. The algebra is next.

The desk is indifferent between not trading and buying $\Delta q$ at price $B$ when the certainty equivalents match. Holding $q + \Delta q$ until $t+h$ is worth $(q+\Delta q)\,m$ in expectation, costs $B\,\Delta q$ in cash today, and carries variance $(q+\Delta q)^2\sigma^2_{\text{IDO}}h$:

$$
(q+\Delta q)\,m \;-\; B\,\Delta q \;-\; \tfrac12\gamma\,\sigma^2_{\text{IDO}}h\,(q+\Delta q)^2 \;=\; q\,m \;-\; \tfrac12\gamma\,\sigma^2_{\text{IDO}}h\,q^2 .
$$

Cancel $q\,m$ from both sides and expand $(q+\Delta q)^2 - q^2 = \Delta q\,(2q+\Delta q)$:

$$
\Delta q\,(m - B) \;=\; \tfrac12\gamma\,\sigma^2_{\text{IDO}}h\,\Delta q\,(2q+\Delta q).
$$

Divide by $\Delta q > 0$:

$$
B^{\text{res}} \;=\; m \;-\; \tfrac12\,\gamma\,\sigma^2_{\text{IDO}}\,h\,(2q+\Delta q). \tag{1.1}
$$

Three things fall out immediately. First, the bid falls one-for-one in $q$: a desk that is already long is a worse buyer, by $\gamma\sigma^2_{\text{IDO}}h$ per \$mm of existing inventory. Second, the bid falls in the client's size, by $\tfrac12\gamma\sigma^2_{\text{IDO}}h$ per \$mm; this is the "block discount," and it is the term most often dropped by people who linearize too early. Third, letting $\Delta q \to 0$ gives the reservation mid $r^{\text{res}} = m - \gamma\sigma^2_{\text{IDO}}h\,q$, which is the Avellaneda–Stoikov reservation price with the trading horizon $T-t$ replaced by the expected holding period $h$. (The notation table reserves $r$ for interest rates, so the reservation price wears a superscript.) The same algebra for a client *buying* $\Delta q$ from us gives the ask $A^{\text{res}} = m' + \tfrac12\gamma\sigma^2_{\text{IDO}}h\,(\Delta q - 2q)$, where $m'$ conditions on a buy RFQ: a long desk is a keen seller.

**Whose five days?** The Tuesday after the 8-K, Halvorsen stopped trading: no prints, no RFQs, one indicative offer at 80 from a dealer who plainly did not want to sell. The desk still held its \$5mm, and the engine still charged for it with $h = 5/252$, as though the bonds could be sold by Monday. Ines stopped behind Kaz's chair and read the input off the screen. "Whose five days?"

"The model's," Kaz said.

"The market's are about a quarter," Ines said, "and nobody asked us." Kaz set $h$ to $63/252$, and the charge for each \$mm already held went from 0.025 points to 0.32 *(illustrative)*.

"And that's still a charge for wiggles," Mags said from across the desk, "on a bond that just fell through a trapdoor, hedged with CDX it stopped following at 4:40 on Friday." Nobody had re-estimated $\sigma_{\text{IDO}}$ since the call. Kaz wrote three words on a sticky note, *hedge, horizon, jump*, and stuck it on the inventory term's unit test; the third word is the Ways This Blows Up box at the end of §1.3.3.

### 1.3.3 The toxicity term: Bayes on the RFQ

Now the conditioning. Suppose RFQ senders come in two types. An **uninformed** seller (a fund meeting redemptions, an insurer selling a downgraded bond, a CLO curing a test) carries no news: $\mathbb{E}^{\mathbb{P}}[S_{t+h}\mid\text{uninformed}] = S_t$, where $S_t$ already prices everything public. An **informed** seller knows the price is going to $S_t - J$, for a jump $J > 0$ points (the post-LMT mark, the earnings miss, the docket filing). Let $\pi = \mathbb{P}(\text{informed}\mid\text{this RFQ},\mathbf{x})$ be the posterior that this particular seller is informed, given observable features $\mathbf{x}$. Then

$$
m \;=\; \pi\,(S_t - J) + (1-\pi)\,S_t \;=\; S_t - \pi J .
$$

> **Math, Gently.** *Bayes' rule, in the form a trader can do in his head.* Bayes' rule is how you update a belief when evidence arrives, and it is easiest in **odds** rather than probabilities. Odds are "for" divided by "against": a 20% chance is odds of $0.2/0.8 = 0.25$, or "one to four." The rule is then a single multiplication: *posterior odds = prior odds × likelihood ratio*, where the likelihood ratio of a piece of evidence is how much more often you would see it from an informed seller than from an uninformed one. Several independent pieces of evidence simply multiply. A tiny worked example: suppose 5% of sellers in some name are informed, so the prior odds are $0.05/0.95 \approx 0.0526$. The RFQ arrives the morning after an amendment request went out, which you judge to be 6 times likelier from an informed seller: odds become $0.0526 \times 6 \approx 0.316$. It is twice the account's usual size, a further factor of 2: odds $\approx 0.63$. Converting back, $\pi = 0.63/(1 + 0.63) \approx 0.39$. A 5% prior became a 39% posterior from two observations. Now take logarithms: multiplying odds becomes *adding* log-odds, and "add up the evidence on the log-odds scale" is all a logistic regression is. The derivation is next.

Where does $\pi$ come from? From Bayes' rule, and this is the step that turns an RSSG banker's instincts into a model. Let $\mu$ be the prior share of informed senders, and let $a_I(\mathbf{x})$ and $a_U(\mathbf{x})$ be the likelihoods that an informed or uninformed account would send *this* RFQ: this size, this bond, at 2:58 p.m., 58 minutes after a lender call, five dealers in competition. Then

$$
\pi(\mathbf{x}) \;=\; \frac{\mu\,a_I(\mathbf{x})}{\mu\,a_I(\mathbf{x}) + (1-\mu)\,a_U(\mathbf{x})}
\quad\Longleftrightarrow\quad
\operatorname{logit}\pi(\mathbf{x}) \;=\; \operatorname{logit}\mu \;+\; \ln\frac{a_I(\mathbf{x})}{a_U(\mathbf{x})} .
$$

If the log-likelihood ratio is (approximately) additive across features, $\ln(a_I/a_U) = \theta^\top\mathbf{x}$, the posterior is exactly a logistic regression, $\pi(\mathbf{x}) = (1+e^{-\theta_0-\theta^\top\mathbf{x}})^{-1}$ with $\theta_0 = \operatorname{logit}\mu$. That is why every RFQ toxicity model on the Street is, under the hood, a logistic regression or a tree ensemble pretending not to be one.

Which features? Ines did not give Theo a list. On the Monday after Halvorsen she gave him the Friday RFQ again, on paper, and asked one question at a time: "What would you have wanted to know?"

"When the lender call ended," Theo said. "Or when the amendment request went out. The closer the RFQ is to the call, the likelier the seller heard something on it." Minutes since a lender call or an amendment request: the first feature.

"What else?"

"Whether earnings are next week." Days to earnings: the second.

"Who is selling?"

"Whether the account is in the group." Theo thought about it. "You can know that, sometimes. When an ad hoc group appears in court, its counsel files a Rule 2019 statement listing the members." Whether the account sits in a known ad hoc group, from Rule 2019 statements scraped off the docket (Chapter 25): the third, and usually the one with the largest likelihood ratio.

"And if you don't know the account at all?"

"Then I'd want to know how its last hundred trades went for whoever bought from it." The account's own past markouts: the fourth. Ines nodded; that one is the hand history.

"How big?"

"Relative to the issue, not in dollars. Fifteen million of a 300 million issue is a different statement from fifteen million of three billion." Size relative to the issue: the fifth.

"Last one. How did they ask?"

Theo hesitated, then saw it. "Five dealers at once. Someone who wants a quiet exit shows it to one dealer at a time. Someone who wants out *before Monday* blasts it." How many dealers were put in competition: the sixth. A seller who shows the bond to one dealer at a time and a seller who blasts it to twenty are telling you different things.

"Good," Ines said. "Every one of those is a likelihood ratio. Your job is to know which ones are big. Kaz's job is to estimate them. And the markouts' job is to tell both of you when you're wrong."

Adding a cost $c(\Delta q)$ for the hedge half-spread and expected liquidation cost (Ben Dor's liquidity cost score is one estimate, §1.4) gives the full bid:

$$
B^* \;=\; S_t \;-\; \underbrace{\pi(\mathbf{x})\,J}_{\Lambda_{\text{tox}}} \;-\; \underbrace{\tfrac12\gamma\,\sigma^2_{\text{IDO}}\,h\,(2q+\Delta q)}_{\text{inventory}} \;-\; \underbrace{c(\Delta q)}_{\text{cost}} . \tag{1.2}
$$

This is the seed's equation from §1.1 with the per-horizon variance written out. Its comparative statics are the unit tests: $\partial B^*/\partial\pi = -J < 0$; $\partial B^*/\partial q = -\gamma\sigma^2_{\text{IDO}}h < 0$; $\partial B^*/\partial\Delta q = -\tfrac12\gamma\sigma^2_{\text{IDO}}h - c'(\Delta q) < 0$; and with $\gamma = 0$ and $\pi = 0$, $B^* = S_t - c$.

**The cold open, in numbers** *(illustrative)*. At 7:30 on Monday, with the 8-K open on one screen and the 78 on the other, the desk redid Friday's trade with a pencil, the way you replay a hand you lost. Kaz typed; everyone else talked.

"Inputs first," Kaz said. "Composite mid $S_t = 91.97$. We were long $q = +5$. Client wanted to sell $\Delta q = 15$. Residual vol after the hedges, $\sigma_{\text{IDO}} = 8$ points per $\sqrt{\text{yr}}$. Holding period five days, so $h = 5/252$. Risk aversion $\gamma = 0.02$. Cost $c = 0.25$." Kaz hit return. "Then $\sigma^2_{\text{IDO}}h = 1.270$ pt², the inventory term is $0.01 \times 1.270 \times 25 = 0.317$ points, and with $\pi = 0$ the bid is $91.97 - 0.317 - 0.25 = 91.40$. That is my engine. It did exactly what it was told."

"Now let Theo's features in," Ines said.

Theo went through them. The account was in the lender group: a large likelihood ratio. The call had ended 58 minutes before the RFQ: large. The bond went to five dealers at once: moderate. "Call it $\pi = 0.6$," he said, and nobody argued, because nobody had a better number and Theo had at least said where his came from.

"And $J$?" Kaz asked.

Mags answered without looking up. "The last comparable uptier I traded, the left-behind paper gapped about thirteen points on the announcement. Different company, same lawyers. Use $J = 13$."

Kaz typed. The toxicity term is $0.6 \times 13 = 7.8$ points and $B^* = 83.60$. A desk that can only show 91.40 or nothing should show nothing. Passing was the right trade; Theo just did not know why yet.

<!-- FIGURE: ch01_bid_decomposition.png (waterfall 91.97 → −0.317 inventory → −0.25 cost → 91.40 → −7.8 toxicity → 83.60; Monday's 78 dashed) -->

Drawn as a waterfall, the decomposition makes the point the chapter has been circling. Start at the mid of 91.97. Step down a third of a point for inventory and a quarter for cost, and you are at Kaz's 91.40: two small, well-behaved steps that every engine on the Street computes. Then comes the third step, 7.8 points, more than ten times the other two combined, and it lands at 83.60. Monday's open at 78 sits below even that, a reminder that $\pi J$ is an expectation and Friday's hand was the bad outcome. The third term is most of the bid. It was also the only one nobody on the desk had a number for.

> **Poker Table.** "An RFQ from a lender who was on the 2 p.m. call is a raise from a player who just looked at the river card," Ines says. "You don't need to know what he saw. You need to know he saw it." The lesson is in the Bayes step: $\pi$ is a function of observable *counterparty state*, not of the bond. Two identical RFQs on the same CUSIP can deserve bids ten points apart because of who sent them and when. Ines's hand history, replayed through markouts, is the test: if you had bought at 91.40, your five-day markout would have been $78 - 91.40 = -13.4$ points on \$15mm, or about \$2.0mm. Across a thousand such hands the average markout on each feature bucket *is* $-\pi J$, and that is how you estimate $\pi$ without ever reading anyone's mind.

> **Math, Gently.** *Normal bags and Poisson bags.* A **normal** (Gaussian) distribution is what you get when many small, independent wiggles add up: most outcomes cluster near the middle, and big surprises are so rare that a move of seven standard deviations essentially never happens. A **Poisson** process is the opposite kind of bag: "nothing, nothing, nothing, then one big thing." It counts rare events (defaults, lender calls, downgrades) arriving at some average rate, and the damage comes all at once. The two can have exactly the same mean and the same variance and still be completely different experiences. A tiny number: a 2% chance of losing 50 points has an expected loss of $0.02 \times 50 = 1$ point, the same as losing 1 point for certain. Its standard deviation is about 7 points ($\sqrt{0.02 \times 0.98 \times 50^2} = 7$). A normal bag with a mean of $-1$ and a standard deviation of 7 looks identical to the mean–variance rule: same mean, same variance, same penalty. But in the normal bag, losing 50 points is a seven-standard-deviation event, far rarer than one in a billion; in the Poisson bag it happens one time in fifty. A quadratic penalty cannot tell the two apart, and the box below shows what that costs. Chapter 5 gives both distributions their full treatment.

> **Ways This Blows Up.** *Kaz: "Let's just assume Gaussian."* The mean–variance certainty equivalent treats a 50-point jump to default as if it were a lot of small wiggles. For a small position the error is small, because a risk-averse desk barely notices the difference between a rare small loss and a spread of tiny ones. But the honest penalty for a jump grows *exponentially* in the size of the position times the size of the jump, while the quadratic penalty grows only with its square, so the gap between them opens quickly and then explodes. Large blocks in jumpy names are exactly where this matters, which is why real desks cap jump-to-default exposure with hard limits rather than trusting a quadratic penalty. Kaz: "...I regret it already." Chapter 18 rebuilds the market maker's problem with a jump term, and Chapter 28 turns the limit into a sizing rule.
>
> **The Full Derivation.** Do the exact CARA calculation instead. Let the hedged price change be $\sigma_{\text{IDO}}\sqrt{h}\,Z - \ell\,(N_h - \lambda h)$, where $N_h$ is a Poisson count with default intensity $\lambda$ and $\ell = P - 100R$ is the jump-to-default in points (the compensator $\lambda h$ keeps the mean in $m$). For a position $q$, the exact certainty equivalent is
>
> $$
> \text{CE} = \mathbb{E}^{\mathbb{P}}[X] - \tfrac12\gamma q^2\sigma^2_{\text{IDO}}h - \frac{\lambda h}{\gamma}\Big(e^{\gamma q \ell} - 1 - \gamma q \ell\Big),
> $$
>
> whose last term equals the Gaussian-style $\tfrac12\gamma\lambda h q^2\ell^2$ only when $\gamma q\ell \ll 1$. At $\gamma q\ell = 0.6$ the Gaussian version under-charges the jump by about 19%; at $\gamma q\ell = 3$ it under-charges by a factor of about 3.6, and the gap grows exponentially in size.

### Specification for AI Implementation

> **Quant-Shop Life (fictional composite): a market-making desk, Tuesday, 7:40 a.m.** *Everything that happens on this desk is invented, assembled from the ordinary texture of many shops. The two podcast details are public statements by Jane Street engineers, cited as such.*
>
> The build is red. It is the first thing Theo sees when he sits down, before the coffee, before the overnight Asia summary: a small red square on the desk's dashboard next to the words `pricing-kernel nightly`. Kaz is already there, which means Kaz has been there for a while.
>
> "Someone edited the inventory term," Kaz says. Kaz does not say *who*; the commit log says it was a well-meaning developer on the risk team who had read, correctly, that a dealer's bid should never exceed the mid less costs, and had added a line to clip it there. The line made the code look safer. It also meant that a desk running short inventory now bid exactly the same whether it was short \$5mm or short \$50mm, and the comparative-statics test, the one that insists the bid must fall as inventory rises, failed at 2:13 a.m. with the message `dB/dq >= 0 for q < 0`. The test did its job. The chapter's spec (§1.10) says never clip a short desk's bid above $S - c$; a short desk *should* pay up to cover. Nobody had read that far. Kaz reverts the commit, writes a two-line comment above the test explaining why it exists, and opens a ticket titled "do not do this again (please)". It is 7:52.
>
> At 8:05 an operations analyst leans over with a printout, which is how you know it is serious. The TRACE exception queue has three prints from Monday afternoon with the wrong capacity flag: reported as agency, booked as principal. Under FINRA Rule 6730 a dealer reports a corporate bond trade "as soon as practicable, but no later than within 15 minutes of the Time of Execution," and the report carries, among other fields, the contra-party and the capacity in which the dealer acted; a correction filed later goes in as an "as/of" report. The three prints are corrected by 8:40. Nobody will ever write a paper about it.
>
> The markout report is the third thing, and the one that matters to Ines. It is off by one trade. The desk's five-day markout for the "lender-group account" bucket shows 41 trades; the blotter shows 42. Theo spends forty minutes finding it: an as/of correction to a trade from the previous Wednesday arrived after the 6 a.m. snapshot that feeds the report, so the report and the blotter disagree about what happened, and both are, in their own way, right. He reruns the report against a snapshot that keeps each print *with the time it arrived*, and the missing trade reappears. It was a bad one. The bucket's average markout moves from −1.9 points to −2.3.
>
> "That," says Ines, when he shows her, "is the hand history. If the tape is dirty, the hand history is dirty, and every $\pi$ we estimate from it is wrong in the direction that loses money." Then she goes back to her screens, because it is 9:00 and the risk meeting is about to ask why yesterday's VaR is different from today's, and the honest answer is "one trade, arriving late."
>
> None of this is glamorous, and none of it is rare. Jane Street's own engineers describe the same species of work in public. On the firm's *Signals and Threads* podcast, a production engineer said that "between a quarter and a third of your time you'll actually be on rotation," responding during the trading day to issues "popping up live," and that the team built a tool to ask what share of alerts were actually being actioned, as opposed to snoozed or ones that "close themselves" (Ep 20, 7 Oct 2024). In a later episode a desk developer recalled that a commodities risk system had once been "a large Microsoft Excel spreadsheet, uscommoditiesrisk.xlsm," where "you'd press a button" and "sometimes it was slow," before it was rebuilt from first principles (Ep 29, 2 Sep 2026). The same episode makes the point Theo has just learned the hard way: keep all the data *along with the time you received it*, or your back-test becomes a time machine.
>
> By 10:15 the build is green, the queue is empty, the markout report ties, and the desk has not quoted a single bond that it would not have quoted yesterday. That is a good morning. Most of them look like this.

**What ROBO built from the vague version.** Spec: "write a function that gives a fair bid for an RFQ." ROBO returned `return mid`, with a docstring noting that the mid is, by construction, fair. It is. It is also the price at which the cold open loses \$2mm.

The spec that fixes it, with the units written into the contract and the inputs on which the function must refuse to answer, is the chapter's spec in §1.10.

The cold open's arithmetic was done with a pencil, on a Monday, and the pencil is the problem. At 2:58 p.m. on a Friday there is no pencil: the RFQ is on the screen, five dealers are in competition, and the number has to leave the building before the other four. The arithmetic of (1.2) is not hard; it is easy to get wrong in a hurry. Charge the toxicity twice, once in a composite mid that already marked down when the lender call ended and again as $\pi J$, and the bid is lawful and quietly uncompetitive: the desk stops winning the flow it wants and nobody can say why. Forget the block discount, or quote in dollars what the equation wants in points, and the bid is simply wrong. A desk automates the bid for the reason it automates anything it cannot afford to get wrong once, and the tests are the part that matters. Tuesday's red build was one of them doing its job.

**Reading Listing 1.1.** The test that failed at 2:13 a.m. lives here, next to the function it guards. `reservation_bid` takes the fair-value mid `S`, the inventory `q`, the client's block `dq`, the risk aversion `gamma`, the post-hedge `sigma_ido`, the holding period `h_years`, the toxicity posterior `pi`, the informed jump `J` and the cost `c`, and returns one number: the bid, in points per 100 par. After validating its inputs it does three things. It shades the mid to the Glosten–Milgrom posterior mean, `S - pi*J`. It subtracts the inventory charge, one half of `gamma` times the horizon variance times `2q + dq`, which is the average marginal charge over the dollars you are about to buy: the inventory you already hold counts in full, the new block at half. And it subtracts `c`. Three helpers keep it honest. `posterior_informed` turns a prior and a log-likelihood ratio into `pi` by adding them on the logit scale. `glosten_milgrom_markout` simulates sellers who are informed with probability `pi`, hands the buyer the hedged noise plus a loss of `J` from the informed ones, and returns the mean markout with its standard error, which must land within three standard errors of `-pi*J`: Ines's hand history in miniature. `jump_penalty_ratio` divides the exact exponential-utility jump charge by its quadratic cousin. The script then reproduces the cold open (91.40 for Kaz's engine, 83.60 once Theo's features are in) and asserts the signs from the comparative statics, including that a short desk bids above the mid.

In production it is the pricing kernel behind a quote, fed by a toxicity model and a risk system. It estimates none of `pi`, `J` or `sigma_ido`; it quotes one bond to one client with no model of the competing dealers; and it charges inventory risk with a quadratic term only, so the ratio function is a smoke alarm that tells you how badly that under-charges, not a charge itself.

The numerical guards are deliberate. `np.expm1` keeps the jump penalty accurate when $\gamma q\ell$ is tiny (a naive `exp(x) - 1 - x` loses every significant digit below about $10^{-8}$), and `posterior_informed` refuses a prior of exactly 0 or 1, because a desk that is certain nobody is informed has already lost the hand.

*The full listing is [Listing 1.1 in Appendix F](#code-1-1).*

### Deep-Dive Resource Graph

- **Podcasts.** *Flirting with Models* (Corey Hoffstein), https://www.flirtingwithmodels.com/ , systematic practitioners on process.
- **Practitioner Writing.** Man Institute (Robert Lam and Paul Kamenski), *The Revolutions in Credit Trading* (2023), https://www.man.com/insights/revolutions-in-credit-trading .
- **Academic Papers.** Glosten and Milgrom (1985), *Bid, Ask and Transaction Prices in a Specialist Market with Heterogeneously Informed Traders*, JFE. Ho and Stoll (1981), *Optimal Dealer Pricing under Transactions and Return Uncertainty*, JFE. Avellaneda and Stoikov (2008), *High-Frequency Trading in a Limit Order Book*, Quantitative Finance.
- **Data & Code.** FINRA TRACE, https://www.finra.org/filing-reporting/trace , the tape every markout is computed against.

---

## 1.4 The Anthology, Part A: Measuring the Risk You Catch (Ben Dor; Veronesi)

Here is how to read the shelf. Every book on it answers one question about the forced seller on the other side of your bid. Ben Dor answers the first: *if I catch this flow, how much risk did I just buy?* The intuitive answer, "spread duration times the spread move," is correct and useless, because it leaves open which spread move. Ben Dor's team at Barclays spent a decade showing that the answer is *a move proportional to the spread you already have*.

The argument reached the desk on a Thursday, through the risk report. Mags had circled two lines in red: a seven-year BBB at 120 bp and a four-year single-B at 450 bp, with the BBB ranked as the bigger risk because its spread duration was seven and the single-B's was four.

"When I started," Mags said, "this is how the risk report worked. A seven-year BBB is riskier than a four-year single-B. Everybody knew that, because the report said so, and the report had a logo on it."

"Everybody was measuring the wrong move," Kaz said. "Duration tells you how much the bond loses per basis point. It doesn't tell you how many basis points to expect. A single-B doesn't move one basis point when the BBB moves one."

"Then how many?"

"Proportionally more. That's the whole of Ben Dor." Kaz pulled up the page, and the argument, as arguments on a desk should, turned into arithmetic.

> **Math, Gently.** *Additive moves and proportional moves.* There are two natural ways for a number to wiggle. In an **additive** world, the size of a typical move does not depend on where you start: a spread at 100 bp and a spread at 1,000 bp both move about 20 bp on a bad day. That is the world of the normal distribution, where you add shocks. In a **proportional** world, moves scale with the level: a bad day is "spreads 10% wider," which is 10 bp at 100 bp and 100 bp at 1,000 bp. That is the world of the **lognormal** distribution, where you multiply by shocks, and it has the convenient property that the number can never go below zero. Picture it: a 20 bp move is enormous for a bond at 100 bp (a fifth of its spread) and barely noticeable for one at 1,000 bp. Credit spreads, it turns out, live mostly in the proportional world. A tiny number: if relative spread volatility is $\sigma_{\text{rel}} = 8\%$ a month, a bond at 120 bp has a typical monthly move of about $0.08 \times 120 \approx 10$ bp, and a bond at 450 bp about $0.08 \times 450 = 36$ bp. Same percentage, very different basis points. Ben Dor's page, next, is the evidence; the lognormal itself gets its proper treatment in Chapter 5.

> **[SOURCE EXTRACTION]** *Ben_Dor_Quantitative_Credit_Portfolio_Management p.61:* "we demonstrate that spread changes are proportional to the level of spread. Systematic changes in spread across a sector tend to follow a pattern of relative spread change, in which bonds trading at wider spreads experience larger spread changes."
>
> **Annotation.** This is the single most useful empirical regularity in corporate credit, and it is the reason the inventory term of (1.2) cannot use a single $\sigma$ for every bond. The derivation is two lines. A bond's excess return over duration-matched Treasuries is, to first order, $r^{\text{xs}} \approx -D^{\text{spr}}\,\Delta s$. If spread changes are proportional, $\Delta s = s\,\varepsilon$ with $\varepsilon$ a relative change whose volatility $\sigma_{\text{rel}}$ is roughly common across bonds, then
>
> $$
> \sigma(r^{\text{xs}}) \;\approx\; D^{\text{spr}}\,s\,\sigma_{\text{rel}} \;=\; \text{DTS}\cdot\sigma_{\text{rel}}, \qquad \text{DTS}_i = D^{\text{spr}}_i\,s_i . \tag{1.3}
> $$
>
> Units: with $D^{\text{spr}}$ in years and $s$ in bp, DTS is in bp·years and (1.3) gives excess-return volatility in bp per period of $\sigma_{\text{rel}}$. A BBB bond at 120 bp with a seven-year spread duration has DTS 840; a single-B bond at 450 bp with a four-year duration has DTS 1,800 *(illustrative)*. Spread duration says the BBB is the riskier bond (7 versus 4). DTS says the single-B is more than twice as risky, and DTS is right. A portfolio's exposure to a sector-wide relative move is $\sum_i w_i\,\text{DTS}_i$, which is why Ben Dor's issuer limits are written on DTS: a cap of 5 on market-value % × spread (in %) × duration lets a 100 bp, five-year bond be 1% of the portfolio but holds a 150 bp, ten-year bond to 0.33% (same page).

Mags read the two numbers, 840 and 1,800, for a while. "Fine," she said eventually, which from Mags is a standing ovation. "Back in my day we found that out by losing money on the single-B. This is cheaper." Then, because she could not leave it there: "Ask him what happens to his eight percent in a bad month."

> **[SOURCE EXTRACTION]** *Ben_Dor_Quantitative_Credit_Portfolio_Management p.39:* "absolute spread volatility is highly unstable and tends to rise with increasing spread. Computing volatilities based on relative spread change generates a more stable time series."
>
> **Annotation.** Stability is the property a specifier should care about most, because a parameter that moves is a parameter the model will mis-estimate exactly when it matters. On the same page Ben Dor reports sector relative volatilities "quite tightly clustered, ranging from 5% to a bit over 10%" per month, against absolute volatilities from 5 bp to more than 20 bp per month. For the desk this means one number, $\sigma_{\text{rel}}$, plus each bond's DTS, gives a first-pass $\sigma_{\text{IDO}}$ prior for thousands of CUSIPs that never trade, before any bond-specific data arrives. Chapter 8 replaces the prior with a posterior.

"It gets bigger," Kaz admitted, answering Mags's question. "For everyone at once. Ben Dor checked it through the 2007–2009 crisis."

> **[SOURCE EXTRACTION]** *Ben_Dor_Quantitative_Credit_Portfolio_Management p.26:* "We find that the relationship between spread and spread volatility remains strongly linear, albeit with a steeper slope."
>
> **Annotation.** This is the out-of-sample test through 2007–2009, and the "albeit" is where the money is. The *shape* survives a crisis; the *slope*, $\sigma_{\text{rel}}$, does not. A book that is DTS-neutral in calm markets is not crisis-neutral, because $\sigma_{\text{rel}}$ jumps for everyone at once, and it jumps exactly when forced sellers arrive. In the bid equation, that is the moment the inventory term and the cost term explode together (Case Study B, §1.8).

**Empirical duration: the CCC bond that wears a tie.** The rates hedge has the same problem from the other side. Analytical (modified) duration says a five-year bond loses about five points per 100 bp rise in Treasury yields. Empirically, high-yield bonds barely care, and sometimes move the wrong way, because rates tend to rise on good economic news that also tightens spreads. Ben Dor estimates empirical duration by regressing price returns on Treasury yield changes, $\Delta P/P = -D^{\text{emp}}\,\Delta y^{\text{TSY}} + \epsilon$, and finds it falls with spread level: "when Ba spreads topped 600 bps in 2002, the corresponding empirical duration was as low as −2" (*Ben_Dor_Quantitative_Credit_Portfolio_Management p.200*). A CCC bond is an equity option that wears a tie to work: it has a coupon and a maturity date, and it trades on the equity's mood. Hedge it with Treasury futures at its analytical duration and you have not removed rates risk; you have added a short Treasury position. That error goes straight into $\sigma_{\text{IDO}}$ and inflates the inventory charge. Chapter 8 builds the hedge ratios properly.

> **Math, Gently.** *What a regression slope is.* A regression asks one question of a cloud of points: if you had to draw a single straight line through them, which line would leave the smallest total of squared misses? Put Treasury yield changes on the horizontal axis and the bond's price returns on the vertical one, one dot per day or month. The slope of the best line is how much the price typically moves for each unit the yield moves, and with a minus sign in front it is the bond's *empirical* duration. Analytical duration is what the bond's cash flows say the slope should be; empirical duration is what the dots say it was. For an IG bond the two agree closely. For a high-yield bond the dots can slope the wrong way, because on the days yields rose, spreads often tightened. A tiny number, with the smallest cloud there is: two months. In one, Treasury yields rose 50 bp and a high-yield bond rose 0.5%; in the other, yields fell 50 bp and the bond fell 0.5%. The line through the two dots climbs one percent of price per percentage point of yield, a slope of $+1$, so the empirical duration is $-1$: a bond with *negative* duration, which gains when rates rise, although its cash flows say it should lose about five points. Chapter 7-B is where regressions are built, and doubted, properly.

> **[SOURCE EXTRACTION]** *Ben_Dor_Quantitative_Credit_Portfolio_Management p.112:* "We define LCS as the bond's OASD multiplied by this spread. Consequently, a bond's LCS can be interpreted as the cost, in percentage points, of immediately executing a roundtrip transaction."
>
> **Annotation.** The liquidity cost score is the $c(\Delta q)$ term of (1.2) for a normal-sized trade: the bid–ask spread quoted in spread terms, times option-adjusted spread duration, gives a round-trip cost as a percentage of price. Ben Dor's formal definition (p.118) has a second branch that matters more to this book than the first: for a bond that is **price-quoted**, LCS is simply (ask − bid)/bid. Bonds switch from spread quotes to price quotes when they become distressed, and at that moment DTS stops being the right risk measure, because "spread" has stopped meaning anything. Mags's version: "Below 70, nobody quotes you a spread. They quote you a recovery and a grudge." The risk moves to price-and-recovery space, which is where Part IV lives.

> **[SOURCE EXTRACTION]** *Veronesi_Fixed_Income_Securities p.120:* "We will rarely use the variation in the semi-annually compounded yield to maturity for risk management purposes, and rather use the variation in the continuously compounded spot curve."
>
> **Annotation.** A sentence about conventions is the most important sentence on the shelf for anyone directing a coding agent. "Duration" is not one number; it is a derivative with respect to *some* curve under *some* compounding. If the Treasury hedge is sized off a spot-curve duration and the bond's risk is computed off a semi-annual yield-to-maturity duration, the residual is a phantom position that nobody chose. The spec must name the curve, the compounding, and the bump (parallel, key-rate, or empirical). ROBO will not guess, which is good, because it would guess differently each time.

> **Desk Myth vs. Desk Reality.** *Myth:* "Spread duration is the risk measure; a seven-year bond is riskier than a four-year bond." *Reality:* Spread changes scale with spread, so the risk measure is DTS, and below about 70 points the bond stops being a spread instrument at all. The four-year single-B is the riskier bond, and the four-year CCC is mostly an equity claim with a coupon.

Theo built the column himself that afternoon, in a copy of the risk report, because that is what a banker does with a new idea. Spread duration times spread, pasted down four thousand rows, then times 8% for a bad month. The single-B came out at 1.44.

"One point four four what?" Kaz asked, passing behind him.

"Basis points a month. The report's in basis points."

"The report is. Your spread column is in percent." Kaz leaned in. "On this desk DTS is bp-years, and the single-B's is 1,800. You've got 18 percent-years, and a single-B at 450 that moves a basis point and a half in a bad month. It moves 144." Kaz scrolled down. Row 3,112 was a bond quoted at 41, carrying a "spread" of 2,900 bp and a DTS larger than the rest of its sector put together. "And that one stopped being a spread instrument in the spring. A spreadsheet will multiply anything by anything."

By the evening the column was a function, with its units in the docstring. Row 3,112 stayed the caller's problem.

> **Math, Gently.** *Monte Carlo: roll the dice many times and count.* Some questions are easier to answer by experiment than by algebra. "If spread moves are lognormal with an 8% monthly volatility, what is the volatility of this bond's excess return?" has a formula, (1.3), but the formula is an approximation, and the honest way to check it is to make the computer roll the dice: draw 200,000 random relative moves from the assumed distribution, turn each into a spread change and then into a return, and measure the spread of the results directly. That is **Monte Carlo** simulation, named, with a gambler's sense of humour, after the casino. Its accuracy improves with the square root of the number of draws, so four times the draws halves the error. A tiny number: with 200,000 draws, the sampling error in an estimated standard deviation is about $1/\sqrt{2 \times 200{,}000} \approx 0.16\%$, which is why a 2% tolerance in the test below is generous and a failure means the formula, not the dice, is wrong. Listing 1.1's markout simulator already used the same trick quietly. Seeds, which make a simulation reproducible, are a Chapter 7-B story.

**Reading Listing 1.2.** Mags's two circled lines are the listing's first test: the script checks that the four-year single-B at 450 bp is more than twice as volatile as the seven-year BBB at 120 bp, 144 bp against 67 bp at an 8% relative move, which is the number Theo's percent column hid. `dts` multiplies spread duration in years by spread in basis points and returns bp-years. `dts_vol` multiplies that by `sigma_rel` to give (1.3): excess-return volatility in bp per period. `lcs` returns Ben Dor's liquidity cost score in percent of price and has two branches that the caller selects with `price_quoted`. For a spread-quoted bond it takes bid and ask spreads in bp (the bid spread is the wider one, because the dealer's bid is the lower price) and multiplies the width by OASD, so a 10 bp market on a four-year bond costs 0.40% round trip. For a price-quoted bond it takes the width in price over the bid, so 62 bid and 64 offered costs 3.23%, with no duration anywhere. The script then simulates 200,000 lognormal relative spread moves to confirm that DTS times `sigma_rel` reproduces the simulated volatility within 2%, and checks the issuer-limit arithmetic: a cap of 5 allows 1% of the portfolio in the 100 bp, five-year bond and 0.33% in the 150 bp, ten-year one.

The functions rank, set limits and supply the first-pass prior on `sigma_ido`, and none of them knows when to stop. `dts` would have multiplied row 3,112's 2,900 bp by a duration and returned a perfectly formatted number that means nothing, and `lcs` reports a negative cost for a swapped bid and ask. The switch from spread quotes to price quotes is the caller's job.

*The full listing is [Listing 1.2 in Appendix F](#code-1-2).*

---

## 1.5 The Anthology, Part B: Pricing the Default You Might Be Catching (Bohn–Stein; Schmid; Bolder; BlackRock)

The second question about the forced seller: *if the seller is not informed, what is the bond actually worth?* That is the fair-value term, and the shelf offers two families of answers that have been arguing since the 1970s.

Theo met the first family on a Tuesday when Halvorsen's bonds did not trade at all. The engine still showed a mid, and it moved during the day. He asked Kaz how a bond with no prints could have a price that changed at 11:20 a.m.

"The equity traded," Kaz said. "Forty thousand times. The equity market is a very large committee that votes every second on what the whole firm is worth. If you know what the firm is worth and what it owes, you know something about the bond." Kaz drew a hockey stick on the whiteboard. "Shareholders own the firm after the lenders are paid. So the equity is a call option on the assets, struck at the debt."

"And the bond?"

"Is the assets minus the call. Everything else is getting the inputs right." One idea sits underneath Kaz's sentence, and it is worth a box before the formula arrives.

> **Math, Gently.** *Equity is a call option.* A call option pays $\max(V - F, 0)$: the excess of something's value over a strike, or nothing. At maturity, shareholders receive exactly that, with $V$ the firm's assets and $F$ the face value of its debt, because limited liability means they can walk away from a firm worth less than its debt. A tiny number: assets of 150 against debt of 100. If nothing were uncertain, equity would be worth $150 - 100 = 50$. Now suppose the assets could end at 80 or at 220 with equal odds (still 150 on average). Equity pays 0 or 120, so it is worth 60 on average, *more* than 50, because shareholders keep the upside and hand the downside to the lenders. The debt, which is assets minus equity, is worth $150 - 60 = 90$ on average, less than its face of 100. Volatility moves value from lenders to shareholders, which is the one sentence of option theory every restructuring banker already knows by instinct. Merton gets its full build in §6.2, and the options behind it in Chapter 6-B.

"And the inputs?" Theo asked.

"Two of them you'll meet properly in Chapter 6," Kaz said, and wrote them under the hockey stick. "The assets wander like a random walk, so their uncertainty grows with the square root of the horizon, not the horizon: that's why the formula divides by $\sigma_V\sqrt{T-t}$. And proportional noise drags the typical path below the average one by half the variance, which is why the drift reads $\mu_V - \tfrac12\sigma_V^2$: up ten percent and down ten percent leaves you at 99, not 100. Itô's lemma is the bookkeeping for that drag. Section 6.1.1 does both with a coin and a pencil. Today you need only the shape."

> **[SOURCE EXTRACTION]** *Bohn_Stein_Active_Credit_Portfolio_Management p.128:* "we need only stipulate that the market is attempting to fairly value a firm, most typically through its equity."
>
> **Annotation.** This is the structural model's entire philosophical cost, and it is cheap. If the equity market is trying to value the firm, then equity is a call option on the assets struck at the debt, $E_t = V_t N(d_1) - F e^{-r(T-t)} N(d_2)$, and the bond is the assets minus that call. Replace the risk-free drift with the physical asset drift $\mu_V$ and you get the distance to default, the number of asset-volatility standard deviations between the firm and its default point:
>
> $$
> \text{DD}_t = \frac{\ln(V_t/F) + (\mu_V - \tfrac12\sigma_V^2)(T-t)}{\sigma_V\sqrt{T-t}}, \qquad \text{PD}^{\mathbb{P}}_{\text{Gauss}} = N(-\text{DD}). \tag{1.4}
> $$
>
> $V_t$ and $\sigma_V$ are not observed; they are backed out of equity value and equity volatility using $\sigma_E E_t = \sigma_V V_t N(d_1)$ (Chapter 6 and Chapter 23 do it properly). The default point $F$ is a convention; the KMV choice commonly reported is short-term liabilities plus half of long-term debt. The desk use is immediate: equity trades every millisecond and the bond trades twice a week, so the equity market gives you a fresh fair-value input for the bid between bond prints.

> **Math, Gently.** *Thin tails, fat tails, and what $N(-4)$ really says.* The function $N(\cdot)$ is the standard normal cumulative distribution: $N(-\text{DD})$ is the probability that a bell-curve draw lands more than DD standard deviations below its mean. The bell curve's tails thin out astonishingly fast. One standard deviation down happens about 16% of the time; two, about 2.3%; three, about 0.13%; four, about 0.003%, or 3 times in 100,000. If firms' assets really wandered like a bell curve, a firm four standard deviations from its default point would essentially never default. Real default data have **fat tails**: extreme outcomes come far more often than the bell curve allows, because the world contains jumps, fraud, lawsuits and lender calls, and because the inputs ($V_t$, $\sigma_V$) are themselves uncertain. The empirical record that Moody's KMV built says a DD of 4 corresponds to a default frequency of almost 1 in 100. Same distance, a factor of about 300 in probability. That is the next extraction.

> **[SOURCE EXTRACTION]** *Bohn_Stein_Active_Credit_Portfolio_Management p.138:* "under MKMV's empirical distribution and using the VK model described later in this chapter, a DD of 4 converts into an EDF of almost 1 percent."
>
> **Annotation.** Under the Gaussian map, $N(-4) \approx 0.003\%$. Under the empirical map, it is almost $1\%$: a factor of roughly 300. Kaz, on hearing this: "Let's just assume Gaussian... I regret it already." The lesson for a specifier is that the structural model is excellent at *ranking* firms and terrible at *calibrating* them, so production systems keep the DD and replace $N(\cdot)$ with an empirically fitted, monotone map from DD to default frequency. If ROBO is told to "compute PD from Merton," it will use $N(-\text{DD})$, and every IG name in the book will look immortal.

Mags had been half-listening from the recovery waterfall. "Ranking I'll give you," she said. "A DD that falls every week for a month, I want to hear about. Now try it on Halvorsen this week. The stock isn't a claim on the assets any more; it's a lottery ticket on the plan, priced on whatever the restructuring might leave shareholders. Back $V_t$ out of that and you've measured the rumour, not the firm." She went back to the waterfall, then added, without looking up: "And check what's in your $F$. A drop-down can create senior debt overnight."

Kaz had no answer to either, and turned to the other family, the one that does not need the stock at all.

> **[SOURCE EXTRACTION]** *Schmid_Credit_Risk_Pricing_Models p.128:* "the default time is unpredictable and therefore the behavior of credit spreads for short maturities can be captured more realistically." ... "their main draw-back is the missing link between firm value and corporate default."
>
> **Annotation.** The other family. Intensity (reduced-form) models skip the balance sheet and let default arrive as the first jump of a Poisson process with intensity $\lambda_t$. Their virtue is that a pure diffusion can never default by surprise tomorrow, so structural models imply near-zero short-dated spreads, which the market flatly contradicts. With a constant $\lambda$ under $\mathbb{Q}$, a flat rate $r$, recovery $R$ of par paid at default, and a continuously paid premium $s$, equate the two legs of a CDS and you get the credit triangle, $s = \lambda(1-R)$, eq. (1.5), derived in full below once its two ingredients have been unpacked. It invites two errors. Kaz commits the first a few paragraphs from here, and is off by 88 bp: (1.5) is a $\mathbb{Q}$ relation, and risk-neutral intensities run well above physical ones for IG (Chapter 6 derives why). The second is treating "40% recovery" as a fact about the bond rather than a CDS quoting convention (Chapter 5).

> **Math, Gently.** *Waiting for the phone to ring: exponential times and intensity.* Imagine a phone that rings at random, at an average rate of $\lambda$ rings per year, with no memory: the chance it rings in the next minute is the same whether it last rang an hour ago or never. Default in an intensity model is the first ring. The rate $\lambda$ is the **intensity** or **hazard rate**: roughly, the probability of default in the next short interval, per unit of time, given survival so far. The waiting time to the first ring has an **exponential** distribution, and the probability that the phone has *not* rung by time $t$ is $S(t) = e^{-\lambda t}$. The number of rings in a period has a Poisson distribution, the bag from the Ways This Blows Up box. A tiny number: with $\lambda = 2\%$ a year, the one-year survival probability is $e^{-0.02} \approx 98.0\%$; over five years it is $e^{-0.10} \approx 90.5\%$. If a default costs a lender 60% of par ($R = 40\%$), the spread that compensates for that risk is about $\lambda(1-R) = 2\% \times 60\% = 1.2\%$, or 120 bp. That is the credit triangle before it has been proved; the proof is a page away, and §6.6 gives intensities their full treatment.

Kaz tried the triangle at once, on the nearest investment-grade name on the screen: a seven-year BBB to which the vendor's model gave a one-year EDF of 0.2% *(illustrative)*. Two-tenths of a percent times sixty percent: 12 bp. The screen had the bond at 100.

"Which number is lying?" Mags asked.

"Neither," Ines said, before Kaz could defend either one. "One of them is a forecast and the other is a price. Kaz just fed the forecast into the price formula."

> **Math, Gently.** *What "risk-neutral" really means.* The $\mathbb{Q}$ in "a constant $\lambda$ under $\mathbb{Q}$" is not a forecast. It is the set of probabilities that would make today's market prices fair *if everyone were indifferent to risk*. Real investors are not indifferent; they demand to be paid for bearing default risk, for illiquidity, and for the bad timing of defaults, which cluster in recessions. So the probabilities implied by prices, $\mathbb{Q}$, are higher than the real-world probabilities, $\mathbb{P}$, and the gap is the risk premium. Kaz's bond is the tiny number: a real-world default probability of about 0.2% a year and 40% recovery give an expected loss of about $0.2\% \times 60\% = 12$ bp a year, yet the bond trades at 100 bp. Backing an intensity out of the price gives $\lambda^{\mathbb{Q}} \approx 100/60 \approx 1.7\%$, about eight times the physical rate *(illustrative)*. Both numbers are right; they answer different questions. $\mathbb{Q}$ prices the bond; $\mathbb{P}$ tells you how often you will actually lose. Kaz's 12 bp is a $\mathbb{P}$ number fed into a $\mathbb{Q}$ formula, and Chapter 6 makes the change of measure precise (§6.3).

**The Full Derivation: the credit triangle.** A CDS has two legs. The protection buyer pays a premium $s$ per year, continuously, for as long as the firm survives; each instant's payment is discounted at $e^{-rt}$ and paid only with survival probability $e^{-\lambda t}$, so the premium leg is worth $s\int_0^T e^{-(r+\lambda)t}\,dt$. The protection seller pays $1-R$ at the moment of default; the probability of default in a small interval around $t$ is $\lambda e^{-\lambda t}\,dt$, and the payment is discounted at $e^{-rt}$, so the protection leg is worth $(1-R)\int_0^T \lambda\,e^{-(r+\lambda)t}\,dt$. At the par spread the two legs are equal:

$$
s\int_0^T e^{-(r+\lambda)t}\,dt \;=\; (1-R)\int_0^T \lambda\,e^{-(r+\lambda)t}\,dt \quad\Longrightarrow\quad s = \lambda\,(1-R). \tag{1.5}
$$

The integrals are identical, so they cancel exactly, at every maturity: this is the credit triangle. With quarterly ACT/360 premium accrual it becomes an approximation.

> **[SOURCE EXTRACTION]** *Bolder_Credit_Risk_Modelling p.597:* "If one assumes independence of default, then default risk is entirely idiosyncratic." ... "Relaxing this unrealistic choice, however, is the source of most of the complexity in this field."
>
> **Annotation.** For a desk catching forced flow, correlation is not a portfolio-risk nicety; it is the reason forced sellers arrive in herds. The one-factor threshold model makes it concrete (the box and the derivation below), and its message fits in one clause: a bad draw of the common factor moves *every* PD at once, and with it every downgrade, every CCC bucket, and every redemption. Bolder's chapter opens with Richard Feynman's line, "What I cannot create, I do not understand," which belongs on the wall of anyone who specifies models for a coding agent: if you cannot write the simulation, you do not understand the model, and neither will ROBO.

> **Math, Gently.** *Correlation and the common factor.* Picture a hundred coins, each of which comes up "default" 2% of the time. If they are truly independent, you expect two defaults, and twelve would be a freak event. Now suppose each coin secretly watches the same weather before it lands: on sunny days every coin is a little less likely to come up "default," and on stormy days every coin is a little more likely. On average, nothing has changed; across all weathers, each coin still defaults 2% of the time. But the *spread* of outcomes has changed completely, because in a storm the coins fail together. That shared weather is the **common factor**, and **correlation** $\rho$ measures how much each coin listens to it. A tiny number: with $p = 2\%$ and $\rho = 0.2$, a bad factor draw two standard deviations below normal (the kind of weather you get roughly once every forty years) raises every firm's conditional default probability from 2% to about 9.7%. The average is unchanged; the bad year is five times worse. For the desk, that bad year is the one in which every CLO, every insurer and every index fund is a forced seller in the same month. The derivation is next.

**The Full Derivation: the one-factor threshold model.** Firm $i$ defaults when $\sqrt{\rho}\,Y + \sqrt{1-\rho}\,\varepsilon_i < N^{-1}(p)$, with a common factor $Y$ and idiosyncratic $\varepsilon_i$, both standard normal. The left-hand side is itself standard normal (its variance is $\rho + (1-\rho) = 1$), so each firm's unconditional default probability is exactly $p$. Fix the factor at a value $Y$ and the only remaining randomness is $\varepsilon_i$: firm $i$ defaults when $\varepsilon_i < \big(N^{-1}(p) - \sqrt{\rho}\,Y\big)/\sqrt{1-\rho}$. Conditional on the factor, defaults are therefore independent with probability

$$
p(Y) = N\!\left(\frac{N^{-1}(p) - \sqrt{\rho}\,Y}{\sqrt{1-\rho}}\right),
$$

so a bad draw of $Y$ moves every PD at once. With $p = 0.02$, $\rho = 0.2$ and $Y = -2$: $N^{-1}(0.02) \approx -2.054$, the numerator is $-2.054 + 0.447 \times 2 \approx -1.159$, dividing by $\sqrt{0.8} \approx 0.894$ gives about $-1.296$, and $N(-1.296) \approx 0.097$.

> **[SOURCE EXTRACTION]** *BlackRock_Systematic_High_Yield_Credit p.6:* "Our proprietary probability of default signal that has underpinned all of our credit strategies for over 20 years has successfully identified 77% of the defaulted bonds in the ICE BofA High Yield Index within 24 months of its default since 2010."
>
> **Annotation.** This is the structural lineage in production, reported by the manager about its own signal (treat it as a self-reported hit rate, not an audited one, and note that a hit rate without a false-positive rate is half a confusion matrix). The point for Chapter 1 is what the signal is *for*: in high yield, avoiding the default you might be catching is worth more than any factor tilt, because a 50-point jump to default erases years of carry. Chapter 11 builds the defensive book around it.

**Reading Listing 1.4.** Kaz's 12 bp is the reason this listing exists. `credit_triangle_check(lam, R, r, T, n)` would have returned it without complaint. It integrates both legs of a CDS numerically on a fine grid (measure $\mathbb{Q}$) and returns the par spread as a decimal, which must equal $\lambda(1-R)$ to ten decimal places; it integrates rather than using the closed form because the point is to show that the two integrals cancel, not to assume it. Nothing in a number says which measure it came from, so the guard against Kaz's error lives in the spec, which names the measure of every input.

The listing checks two more of the section's claims by brute force, so that nobody on the desk, and certainly not ROBO, has to take the algebra on faith. `distance_to_default(V, F, mu_V, sigma_V, T)` evaluates eq. (1.4) under $\mathbb{P}$ and returns a unitless number of standard deviations. An illustrative firm with assets of 150 against a default point of 100, 6% drift and 10% asset volatility must have a DD above 4 and a Gaussian PD below one in ten thousand: the annotation's "immortal IG name," made executable. That is why the function belongs in the regression tests for the DD and hazard-rate code of Chapters 5 and 6 and nowhere near a trading book's PD: it estimates neither $V_t$ nor $\sigma_V$ from equity, and it maps through $N(\cdot)$, which Bohn–Stein put out by a factor of about 300 at DD = 4. The last block simulates the one-factor threshold model, 20,000 draws of the common factor $Y$ with 500 firms per draw, $p = 2\%$ and $\rho = 0.2$, and asserts that the average default rate across worlds matches $p$ (the factor leaves the mean alone) while the 99th-percentile world loses more than five times $p$ (it changes the tail enormously).

*The full listing is [Listing 1.4 in Appendix F](#code-1-4).*

---

## 1.6 The Anthology, Part C: Which Flows Are Harvestable (Dynkin; Man; Paleologo)

Theo found the fallen-angel trade in his fourth week, the way everyone finds it: in a chart. He had pulled the excess returns of bonds downgraded from BBB to BB over the following year, set them against the high-yield index, and found a gap of about three percent a year *(illustrative)*. He brought it to the morning meeting the way a cat brings a bird to the kitchen door. "Fallen angels beat high yield by three percent a year." Kaz's reply arrived later that morning, in one sentence, and it is quoted below, because it took most of the section to earn.

The question behind Theo's chart is the third one the shelf answers: *is there a systematic way to be on the other side of forced flow, often enough, at a price that pays?* Dynkin, Ben Dor and the Barclays QPS team answer yes, and the cleanest example is the fallen angel.

> **[SOURCE EXTRACTION]** *Ben_Dor_Quantitative_Credit_Portfolio_Management p.349:* "The primary driver of this phenomenon does not seem to be overreaction to information, but rather the structural inefficiency stemming from the segmentation between the investment and non-investment-grade markets."
>
> **Annotation.** Read "segmentation" as "a graph edge with a capacity limit." When a bond crosses from BBB- to BB+, the holders whose mandates end at the IG line must sell, and the holders whose mandates begin there are fewer, smaller, and not in a hurry. The price falls below its equilibrium level and then reverses as the bond finds its new owners. That reversal is a *liquidity provision premium*, not a forecast of fundamentals, which is why it survives: you cannot arbitrage it away by being smarter, only by having a balance sheet that does not care about ratings. Dynkin adds the conditional version: forced selling "should not uniformly affect all issuers. Poor performers during the formation period were more likely to be subject to forced selling and, therefore, to experience a subsequent reversal, unlike top performers" (*Dynkin_Systematic_Investing_in_Credit p.158*). The reversal is concentrated where the forced supply is.

> **[SOURCE EXTRACTION]** *Dynkin_Systematic_Investing_in_Credit p.361:* "For Baa‐rated debt, the probability that a forced sale will occur at some time over the five‐year horizon is 23.7% if forced to sell upon any downgrade to Ba or lower, and 7.2% under the less aggressive policy of selling upon a downgrade to B or lower."
>
> **Annotation.** This is the RSSG banker's favorite kind of number: a contractual trigger, converted into a probability over a horizon. It is also the forced-supply function of §1.8 for one holder type, one trigger, and one cohort. A 23.7% five-year chance of being a forced seller is a cost the IG-only investor pays every year in the form of selling at the bottom. Dynkin's broader point (p.135) is that "the long‐term risk/return performance of a given asset class is determined in part by the sell discipline that is in place for the portfolio." The sell rule is part of the asset class, which means somebody else's sell rule is part of your opportunity set.

**Equity momentum: the flow you can see coming.** The second harvestable flow is slower. Equity markets digest bad news faster than bond markets (more trading, more short sellers, more analysts), so bond prices lag equity prices. Dynkin's decile sorts show it plainly: the bottom equity-momentum decile of US HY "delivered negative average excess return of –4.7% per year between 1993 and 2017. In contrast, the average excess return of the top decile portfolio (D10), with the strongest equity momentum, was +4.01% per year" (*Dynkin_Systematic_Investing_in_Credit p.606*). Man's own factor research finds the same: "the only spill-over to achieve meaningful statistical significance is equity Momentum, which generates a higher alpha than corporate bond Momentum itself" (*Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.31*). In the language of the bid equation, equity momentum is a public feature that updates the fair-value term before the bond trades. Man's backtested factor ladder (p.28) reports information ratios of 2.15 for value, 1.69 for momentum, 1.55 for quality, and 0.79 for its "informed investor" signal, combining to 2.35; those are model returns from the manager's own backtest, and the Trend Watch below explains why a 2026 reader should haircut them.

> **Math, Gently.** *Decile sorts and the information ratio.* A **decile sort** is the simplest experiment in finance. Take every bond in the universe, rank them by a signal (here, the issuer's equity momentum), cut the ranking into ten equal buckets, and track each bucket's return over the next period. If the signal means anything, the top bucket (D10) should beat the bottom one (D1), and the gap should be roughly monotone in between. Dynkin's numbers are a gap of about $4.01 - (-4.7) \approx 8.7$ percentage points a year between the top and bottom deciles. The **information ratio** then asks how *reliably* a strategy earns its excess return: it is the average annual excess return divided by its annual standard deviation, the "wobble" around the benchmark. Return per unit of wobble. A tiny number: a strategy that earns 3% a year over its benchmark with a 2% annual wobble has an IR of $3/2 = 1.5$; one that earns 6% with a 12% wobble has an IR of 0.5, and is the worse strategy to lever, because the wobble is what gets you fired. An IR above 1 sustained out of sample is rare; above 2 it is usually a backtest. Chapter 9 puts both tools to work, and runs the audit.

None of it had been tradable when Theo's chart began, and Kaz, who had been reading Man's 2023 paper for the risk committee, put the sentence that explained why on the desk chat before Theo could ask.

> **[SOURCE EXTRACTION]** *Man_Revolutions_in_Credit_Trading_2023 p.2:* "The greatest barriers to systematic approaches breaking through in credit have traditionally been execution and the ability to model transaction costs and liquidity within decades-old manual processes."
>
> **Annotation.** Every premium above is a premium *before* costs, and in 2015 the costs ate most of them. What changed is plumbing. Once a manager can send a 400-line list to a portfolio-trading desk and get a single price in minutes, the cost term $c(\Delta q)$ of the bid equation falls for the *buyer of liquidity*, and the systematic investor can finally harvest premia that were always there on paper. The same paper puts it as an aphorism: "an optimised portfolio is not optimal if you can't trade it" (p.4).

> **View From Another Seat.** *The systematic fund, in its own published words.* A systematic credit manager does not see the fallen angel as a story about one company. It sees a cross-section in which some bonds have been pushed away from fair value by somebody's rulebook, and it sees a cost of trading that, until recently, ate the premium. Two published statements describe the seat. Man Group's 2023 paper reports that Man Numeric moved from roughly 30% of its HY and 60% of its IG order flow on electronic venues to over 90% (*Man_Revolutions_in_Credit_Trading_2023 p.3*): the seat exists because the cost term fell. And Blackstone's systematic credit paper describes what its optimizer does when forced sellers arrive: it "naturally acts as a contrarian liquidity provider," and "when credit spreads widen aggressively (often due to market panic rather than fundamental deterioration), the model algorithmically increases credit exposure" (*Blackstone_Systematic_Credit p.1*; §1.8 returns to it). From that seat, Theo's Halvorsen RFQ is one line in a list of four hundred, and its toxicity is a risk to be diversified, not a hand to be read. The trade-off is the one this chapter keeps finding: diversification protects the systematic fund against any single informed seller, but it cannot protect it against a *market* full of them, and the parenthesis in Blackstone's sentence ("rather than fundamental deterioration") is the bet that the sellers are forced.

Kaz's reply arrived at 11:40, in the desk chat, under a screenshot of Theo's chart, with the page it came from pasted in first.

> **[SOURCE EXTRACTION]** *Paleologo_Advanced_Portfolio_Management p.111:* "Performance can be decomposed into systematic and idiosyncratic components. Most importantly, these components are investable." ... "your investors are not paying you to replicate the market, ride momentum, or short already shorted stocks."
>
> **Annotation.** Paleologo writes about equities; the logic transfers whole. Theo, proudly: "Fallen angels beat high yield by three percent a year." Kaz: "Strip the HY beta, the DTS, and the index-inclusion bid, then tell me." IDO or it didn't happen. Part of the fallen-angel premium is plain spread beta (fallen angels are long-duration BBs), part is the liquidity premium you are paid for being there on the rebalance date, and only the residual is skill. Paleologo's sharper version (p.139) is the desk motto's parent: "factors can find infinite ways to mar your performance, but cannot tell you how to be profitable." The bid equation's $\sigma_{\text{IDO}}$ is that decomposition applied to a single trade.

Theo took the chart back to his desk and started stripping. Two things had changed since the years in his sample, and both come with dates.

> **Trend Watch: The execution revolution, 2018–2026.** *What changed:* US corporate bonds went from phone-and-chat to a market where half of IG volume trades electronically and portfolio trades are a standard protocol. *How big:* Coalition Greenwich put IG e-trading at 34% and HY at 25% in 2021 (its restated series) and at 48% and 33% in 2024, with average daily notional volume (ADNV) of \$46bn, up 21%, and daily turnover rising from 0.33% of outstanding (2021) to 0.44% (2024) (The DESK, 21 Jan 2025). In 2025 ADNV passed \$50bn for the first time, IG e-trading sat just under 50% and HY at 32%, and disclosed RFQ slipped to roughly 40% of electronic volume (Coalition Greenwich via The DESK, 30 Jan 2026). The single-day record of \$84.7bn on 30 Sep 2025 was 18% portfolio trades (Coalition Greenwich, 27 Jan 2026). Portfolio trading rose from 11% of US corporate bond volume in 2024 to 15% in 2025, peaking at 17% in July 2025 (Morgan Stanley via The DESK, 19 Feb 2026); Barclays counts a portfolio trade every few minutes in 2025, against roughly one every 40 minutes in 2020 (IFR, 2025). January 2026 then set another record, ADNV up more than 20% year on year (Coalition Greenwich, 17 Feb 2026). *What it means for the desk:* the cost term fell, so premia that were paper alpha in 2015 became tradable; and the RFQ in the cold open is now one of tens of thousands per day, which makes toxicity screening an automated, statistical job rather than a trader's hunch. Mags: "Back in my day a portfolio trade was a fax with forty CUSIPs and a prayer. Now it's four thousand line items and no prayer. The pricing is better. I hate it." (Tradeweb reported a single portfolio trade with several thousand line items; IFR, 2025.)

> **Trend Watch: The corporate bond factor replication crisis, 2019–2026.** *What changed:* the academic foundation under credit factors is being re-audited with cleaned TRACE data. Dickerson, Mueller and Robotti (2023, *Journal of Financial Economics*) found that previously proposed corporate bond factors add little beyond the bond market factor; the 2019 JFE factor paper by Bai, Bali and Wen was retracted in 2023 after a data-timing error surfaced in replication. On 9 April 2026, Dickerson, Robotti and Rossetti posted *The Corporate Bond Factor Replication Crisis* (arXiv:2604.07880), which tests 108 signals and finds that most previously documented factors lose statistical significance in bond-CAPM alphas once transaction-price measurement error and asymmetric ex-post return filtering are corrected. *What it means for the desk:* every backtested IR in this section, Man's included, should be re-estimated on error-corrected data before it earns capital (the Open Source Bond Asset Pricing project publishes such data). The flows in this chapter, fallen angels and forced sales, are more robust than the factor zoo for a structural reason: they are paid for by someone's mandate, not discovered in a regression. Chapter 9 runs the audit.

---

## 1.7 The Anthology, Part D: Where the Flows End Up (Moyer; Houlihan Lokey)

The last question: *when the company breaks, who is left holding what, and who has to sell it?* This is home turf for the reader, and Moyer's distressed-debt classic is honest about how far the quants had come when it was written.

> **[SOURCE EXTRACTION]** *Moyer_Distressed_Debt_Analysis p.275:* "As much as the quantitative approach of financial econometricians would suggest that investing is fundamentally a science, in distressed investing it is more of an art." ... "This is why knowledge of the process, experience, and judgment are often more critical to investment success than tedious hours of financial modeling."
>
> **Annotation.** This book agrees with every word and draws the opposite conclusion. "Knowledge of the process" is exactly what can be written down: exclusivity periods, voting thresholds, DIP roll-ups, plan classes, and which creditor has the hold-up value. Once written down, process knowledge becomes features, transition probabilities, and a prior over $J$ in the bid equation. What stays an art is the judgment about which features matter in *this* case, and that is the job description for the human in Man's quote from §1.1. Moyer also tells us where to look for mispricing: "when the news is very bad, the market often will trade down to the worst-case scenario valuations" (p.257), because sellers who need out meet buyers who demand a discount for uncertainty. That is a forced-seller edge with a docket number.

> **[SOURCE EXTRACTION]** *Moyer_Distressed_Debt_Analysis p.370:* "Banks and collateralized debt obligations (CDOs) are not natural holders of equity securities." ... "when such entities are known to be large holders of the postreorganization equity, other market participants will certainly consider their net sell disposition."
>
> **Annotation.** The forced-seller graph does not end at default; it rewires. Loans convert into post-reorganization equity, and the holders of those loans (CLOs, banks) are often barred from, or penalized for, holding equity. So the most predictable seller of a newly reorganized stock is its largest holder, and everybody knows it. Moyer's other forced seller is smaller and sadder: the trade creditor who "may not have the financial wherewithal to wait until the completion of a bankruptcy case to realize full value of the claim and thus is a forced seller" (p.310). Claims trading is that edge in pure form (Chapter 16).

> **[SOURCE EXTRACTION]** *Houlihan_Lokey_Distressed_MA p.35:* "Under Section 363, for example, a debtor with Court approval may sell assets free and clear of all liens, claims and encumbrances (which attach only to the proceeds of such sales)."
>
> **Annotation.** One clause, and it converts the *assets* of a broken firm into a clean asset sale while the *claims* follow the cash. For the flow graph, a 363 sale is a node where the holder set changes completely: the buyer gets the assets with no legacy creditors, and the old creditors get a claim on a pot whose size the auction sets. Pricing the claim means pricing the auction.

Kaz, reading over Theo's shoulder: "A fulcrum is where a lever balances. So the fulcrum security is the tranche with zero duration?" Mags: "It's the tranche that gets the equity and the lawsuits." (The fulcrum is the class whose recovery straddles the enterprise value: everything senior is covered, everything junior is out of the money, and the fulcrum becomes the new owner. It has more duration than anything, measured in years of litigation. Chapter 12-B gives the definition its full waterfall.)

> **View From Another Seat.** *The opportunistic credit fund.* The far end of the distressed edges is where patient capital sits, and some of it has said in public how it thinks. Marc Rowan, Apollo's chief executive, on the firm's fourth-quarter 2025 earnings call (9 Feb 2026): "A principal's mindset approaches every asset and every asset class as if they're going to own it for the long term because they do." Apollo's own description of its business slices a capital structure by loan-to-value and places the dislocation-driven end of credit at 0–50% LTV, "often more liquid and shorter holds" (apollo.com, credit and hybrid-value strategy pages). Howard Marks, in his Oaktree memo *Cockroaches in the Coal Mine* (6 Nov 2025), put the cycle in one line: "The worst of loans are made in the best of times." What the two sentences share is horizon. A seat that expects to own what it buys does not ask what a bond will do over the next 20 days. It asks whether it would own this claim to maturity at this price, through a restructuring if it comes to that, and whether some structure (more collateral, a different place in the capital stack, a new-money tranche) could turn single-B risk into something closer to BBB risk. That seat is the kind of absorber Moyer's forced sellers need: when banks and CLOs must get rid of a post-reorganization stake, this is the kind of buyer that can take it. A public example of the seat at work, as a plan sponsor rather than a buyer from forced sellers: when Hertz left Chapter 11 in 2021, Knighthead, Certares and Apollo-affiliated funds committed "over \$5.9 billion of new equity capital," while Hertz paid "nearly \$19 billion of creditors in full" (Hertz Form 8-K, Ex. 99.1, 2021). For the desk, such funds are natural buyers of blocks when spreads gap, and a reminder that the toxicity term cuts both ways: a patient buyer who has done six weeks of work on a capital structure is also, on the day it buys from you, the best-informed player at the table.

Theo wrote the four questions on a Post-it (*How much risk did I buy? What is it worth? Can I harvest it? Where does it end up?*) and stuck it to his monitor beside the USB stick. Ines took it off the next morning, turned it over, and drew boxes and arrows on the back. "Four questions," she said. "One picture."

---

## 1.8 The Ecosystem as a Forced-Seller Flow Graph

Put the four parts of the anthology together and the market stops looking like a crowd and starts looking like plumbing. Each holder type is a node. Each trigger (a downgrade to HY, a downgrade to CCC, a default, a redemption wave) opens a set of edges with a known direction, an estimable size, and a response window. The Blackstone sentence from §1.6 describes the machine built to sit at the end of those edges, and its parenthesis is the bet this section prices: that the seller is forced, not informed.

### 1.8.1 The model (measure: $\mathbb{P}$)

> **Math, Gently.** *Conservation: the one law of the plumbing.* Before the notation, the idea, which is the whole model. Every bond that is sold is bought by someone. When a downgrade forces a group of holders to sell, there are only two places the bonds can go: to a buyer who wanted them (an absorber with capacity), or onto a dealer's balance sheet, which is the buyer of last resort and charges accordingly. Nothing disappears, and nothing is created. So if you can estimate how much *must* be sold and how much the willing buyers *can* take, the difference is not a mystery: it is the amount that lands on the dealers, and the price has to fall far enough to make someone hold it. A tiny number, from the demo later in this section: holders must sell \$12.9bn, absorbers can take \$6.5bn, so \$6.4bn lands on the dealers. That third number is the one that moves the price. Physicists would recognize the structure, and so would anyone who has ever run a waterfall: what flows in must flow out or pool somewhere.

Let holder types be $i = 1,\dots,n$, bond segments $k$, and triggers $\tau$. Holdings $H_{k,i}$ are in \$bn of par; $f_i(\tau)\in[0,1]$ is the fraction holder $i$ must sell after trigger $\tau$, over a window $w_i(\tau)$ (insurers: quarters; index funds: the month-end rebalance; CLOs: the next test date; open-end funds: days). Natural absorbers $j$ have capacity $A_{k,j}(\tau)$: HY index funds that must *buy* at inclusion (Moyer p.35's "forced" buyers), fallen-angel programs, crossover and distressed funds, and dealers' balance sheets. Then

$$
Q^{\text{sell}}_k(\tau) = \sum_i H_{k,i}\,f_i(\tau), \qquad
I_k(\tau) = Q^{\text{sell}}_k(\tau) - \sum_j A_{k,j}(\tau). \tag{1.6}
$$

The positive part of the imbalance $I_k$ must be absorbed at a price concession. Model the price as a fundamental value $p^*$ minus a temporary pressure term that decays at rate $\theta$ (per day) after the trigger date $t_0$:

$$
p_t = p^* - \kappa\,\frac{\max(I_k,0)}{\text{ADV}_k}\,e^{-\theta(t-t_0)}, \qquad t \ge t_0, \tag{1.7}
$$

where $\text{ADV}_k$ is the segment's average daily volume and $\kappa$ is price impact in points per day of volume. The absorber who buys at $t_0$ and holds for $T$ days earns the recovered pressure, $\kappa\,(I_k^+/\text{ADV}_k)(1-e^{-\theta T})$. That is the drop-and-reversal that Ben Dor (p.349) and Dynkin (p.158) document for fallen angels, and that Ellul, Jotikasthira and Lundblad (2011) tie to insurers' regulatory constraints. Note what (1.7) leaves out: a *permanent* component. If the seller is informed, part of the drop never reverses, and that is the toxicity term $\pi J$ from (1.2). The forced-seller graph prices the temporary component; the RFQ model prices the permanent one. A desk needs both.

> **Math, Gently.** *Exponential decay and half-life.* The factor $e^{-\theta(t-t_0)}$ says the price pressure fades by the same *fraction* every day, the way a cup of coffee cools or a medicine leaves the bloodstream: fast at first, then slowly, never quite reaching zero. The natural way to talk about it is the **half-life**, the time for the pressure to halve, which is $\ln 2/\theta \approx 0.69/\theta$. With $\theta = 1/20$ per day, the pressure halves about every 14 days: half gone after two weeks, three-quarters after four, seven-eighths after six. A tiny number from the Listing 1.3 demo: the price opens 5.12 points under $p^*$ on the trigger date; by day 60 (about four half-lives, $e^{-3} \approx 5\%$ left) it has recovered 4.87 of those points, and that recovery is exactly what the absorber who bought on day 0 is paid for. The same function describes survival under a constant hazard rate in §1.5; the phone that has not rung and the dent that is healing are the same curve.

**Where this blows up.** Act 3 of the replay below shows the first two failures happening on a Saturday: a holder counted twice, and a window that fires on the wrong date. The third is worse. Absorption capacity is *state-dependent*: it collapses exactly when supply peaks, because the absorbers are also being redeemed, and $\kappa$ moves with it. A model with constant $A$ and constant $\kappa$ is a fair-weather model. Moyer (p.55) gives the CLO version of the trigger: "When an investment in the portfolio is downgraded to B– or CCC, the manager may be forced to sell something (again without regard to the portfolio manager's view of fair value) to remain in compliance with the CDO-ORs." A CLO is a buy-and-hold investor with a 7.5% allergy. It does not sell because it wants to; it sells because the indenture sneezes.

> **Trend Watch: Who holds credit now, 1993–2026.** *What changed:* the holder graph got more mechanical. CDOs and CLOs held about 3% of low-rated loans and bonds in 1993 and more than 20% by the early 2000s (*Moyer_Distressed_Debt_Analysis p.55*, Figure 2-18); by 2026 US CLOs held roughly \$1tn, about 65% of a roughly \$1.5tn institutional leveraged loan market (Maples/Nuveen Q&A, 13 Apr 2026). CLO ETF assets grew roughly ten-fold between 2023 and end-2024 (Deutsche Bank Flow, 11 Feb 2025). US fixed income ETF assets reached about \$2tn by mid-2025 (as reported by The Daily Upside, 2 Jul 2025). Life insurers' private placements rose from 14% (2016) to 22% (2024) of their corporate bond holdings (Chicago Fed Insights, May 2026), and privately placed bonds reached 48.4% of life-industry bonds at YE2025 against 37.4% five years earlier (S&P Global Market Intelligence via Insurance Business, 10 Aug 2026). Dealers, meanwhile, swung sharply *net short* in corporate bonds in early 2026 (Coalition Greenwich, 17 Feb 2026). And the fallen-angel pipeline reopened: tens of billions of dollars of fallen-angel supply arrived in 2026 through mid-year (Insight Investment/BNY, Aug 2026). *What it means for the desk:* more of the market sits with holders whose sales are triggered by rules (CLO tests, ETF flows, NAIC capital), and less with dealers whose balance sheet used to absorb them. More predictable forced supply, less natural absorption: that is a bigger $I_k$ for the same shock, and a bigger premium for whoever has the capacity.

### Specification for AI Implementation

**What ROBO built from the vague version.** Spec: "map the forced sellers." ROBO returned a graph with one node, labeled "Everyone, March 2020," and a self-loop.

**The Spec You Hand the Robot.** Build `ForcedSellerGraph(holdings, rules, capacity)`. `holdings`: a DataFrame, index = segment, columns = holder, values in \$bn par, all $\ge 0$. `rules`: `{holder: {trigger: (fraction, window_days)}}` with `0 <= fraction <= 1` and `window_days > 0`; a holder with no rule for a trigger sells nothing. `capacity`: `{trigger: DataFrame(index = segment, columns = absorber)}` in \$bn, all $\ge 0$. `run(trigger, segment, stress=False)` returns sells by holder, buys by absorber, `dealer_residual` (the positive imbalance), and a list of `(seller, buyer, size)` edges, allocating supply to absorbers pro rata to capacity and the remainder to `dealer_residual`. Assertions that must hold on every call: (a) **conservation**, total sells equal total buys plus `dealer_residual` to $10^{-9}$, and the edge sizes sum to total sells; (b) no holder sells more than it holds; (c) `price_path` per (1.7) returns to within 0.01 points of $p^*$ by `10/theta` days; (d) `stress=True` zeroes all capacity, and then `dealer_residual` equals forced supply exactly. All numbers in the demo are *illustrative*.

Run the cold open one level up. Theo's RFQ was one seller and one bond; a downgrade trigger is every rules-bound holder of an issuer's debt being told to sell on its own schedule. The question a desk asks the week a large BBB- name goes on watch is not "will it fall?" but "who has to sell, who has to buy, and how much of the difference lands on my balance sheet?" Answered by hand, that lives in a spreadsheet with a row labeled "Everyone" and a total nobody can reconcile. Answered as a graph, it obeys a conservation law: every dollar sold is bought by someone or left with the dealer. A machine can check that law on every run, switch the absorbers off to replay March 2020, and repeat the exercise for every segment and trigger in the book. A spreadsheet will do it once, for the segment its author cared about, in a cell whose formula has since been overwritten.

**Reading Listing 1.3.** On the Saturday of the Ford replay, the bug that mattered was a fund counted twice, and every assertion in this listing passed anyway (Act 3, below): the listing checks the plumbing, not the census. `ForcedSellerGraph` takes three tables. `holdings` is segments by holder, in \$bn of par. `rules` maps each holder and trigger to the fraction it must sell and a response window. `capacity` maps each trigger to segments by absorber, in \$bn. The constructor refuses negative holdings or capacity, fractions outside $[0,1]$ and non-positive windows. `forced_supply` is the first half of (1.6): each holder's fraction for the trigger (zero if it has no rule) times its holding in the segment. `run` totals that to get $Q^{\text{sell}}$, takes the absorbers' capacity (zeroed when `stress=True`, the March 2020 toggle), fills absorbers pro rata to capacity until the supply is met, and calls the remainder `dealer_residual`, the positive imbalance $I_k$. It then splits each seller's sale across the buyers in proportion to size, which yields the list of (seller, buyer, size) edges you can draw, and asserts conservation twice. `price_path` is (1.7): the pressure `kappa * imbalance / adv`, decaying at rate `theta`, subtracted from `p_star`.

The demo is a Ford-sized fallen angel with illustrative numbers. Holders must sell \$12.9bn against \$6.5bn of absorber capacity, leaving \$6.4bn for the dealer; with stress on, all \$12.9bn lands there. At \$0.5bn of daily volume, a `kappa` of 0.4 and a 20-day decay, the price opens 5.12 points under `p_star` and hands back 4.87 of them by day 60, which is what the absorber is paid for. The last assertion reuses `reservation_bid` from Listing 1.1, so run the blocks in order.

It sizes capacity before a trigger date; it does not forecast the price, because capacities are inputs held constant within a run and absorbers vanish when supply peaks. The `window_days` field is validated and then unused; timing enters only through the single `theta` you pick. Silence is the failure the replay did not hit. A holder with no rule for a trigger sells nothing by design, so a misspelled trigger or holder name sells nothing by accident, every assertion passes on zeros, and the graph reports a calm market in the middle of the wave.

*The full listing is [Listing 1.3 in Appendix F](#code-1-3).*

### 1.8.2 Case Study A: Ford and the March 2020 Fallen-Angel Wave

#### Long Scene 1: The Month Every Edge Lit Up

*The desk, its people and its positions are fictional, and every number attributed to the desk is illustrative. Every dated market fact is sourced, and nothing a real firm did is invented.*

Once a quarter, on a Saturday, Ines runs what the desk calls a replay. The rules are simple and strictly enforced. Pick a historical episode. Put the calendar back to the first day of it. Then trade it, out loud, using only what was known on each day, and anyone who mentions the ending pays for lunch. "It's how you practise a hand you can never play again," Ines says. "Poker players do it with hand histories. Pilots do it in simulators. Credit people mostly do it at the bar, badly."

This quarter it was March 2020, and the reason was Mags. She had traded it, from the distressed loan-and-bond desk of a dealer she describes only as "a bank with good coffee and bad risk limits," and she arrived at 9:00 a.m. with a cardboard box of printed run sheets she had kept for six years, in the way some people keep letters. Kaz had the flow-graph code from §1.8.1 on the projector.

"Back in my day," Mags said, sitting down, and for once nobody groaned, because for once her day was the subject. "Back in my day, which is this month, the problem wasn't that nobody had a model. Everybody had a model. The problem was that every model assumed somebody would be on the other side."

**Act 1: Thursday, 12 March 2020.** Ines put the date on the whiteboard. "It's the close. What do you see?"

Kaz had the numbers ready. On 12 March 2020, the iShares iBoxx \$ Investment Grade Corporate Bond ETF, LQD, closed at a 5.0% discount to its net asset value. The Vanguard and SPDR intermediate corporate funds, VCIT and SPIB, were at discounts of 3.2% and 3.1% (WealthManagement.com, 16 Mar 2020). "Five points," Kaz said. "On one of the most liquid IG products in the world. Buy the ETF, short the basket, deliver the bonds, collect five points. It's an arbitrage. It's the cleanest one I've ever seen."

"Short what basket?" Mags asked. "With what borrow? At whose price?"

"At NAV."

"NAV is a number somebody's pricing service computed at four o'clock from bonds that didn't trade." Mags pulled a run sheet from the box and slid it across: a dealer's offering sheet from that week, a column of IG corporates with bids and, under most of the offers, nothing at all. "That's what the basket looked like. You want to sell me the basket at NAV? I'll buy all of it. I'll buy it all day."

Kaz looked at the sheet for a long time. Theo, who had once spent a week reconciling a borrower's reported cash to its actual bank statements, recognized the expression: the moment you realise the number in the model is a description of a world that is no longer there.

The BIS later measured how far that world had drifted. Todorov's study of bond ETF arbitrage (BIS Quarterly Review, March 2021) found that corporate bond ETF creation baskets covered about 20% of holdings and redemption baskets about 35%, that across bond ETFs the bid–ask spreads of the holdings were about 17 times those of the ETF shares, and that tracking error rose above 200 bp for some funds in March–April 2020, against a historical average of 0.7 bp. The ETF was trading. The bonds were not. The authorized participants who normally close the gap had stopped, because they could not sell the underlying bonds at NAV either.

"So which price is right?" Ines asked.

"The one that trades," Theo said, slowly. "The ETF."

"Write that down," Ines said, and moved the clock forward one day. "Friday, 13 March. Close."

On 13 March the LQD discount was 0.19% (WealthManagement.com). Kaz started to say "so the arb worked," and Mags raised one finger. "The gap closed because the NAV came down to meet the ETF. The bonds caught up with the truth. If you'd bought the ETF and shorted the basket at Thursday's NAV, you'd have needed to *find* those bonds to deliver, at Friday's prices, in a market with no offers." Kaz conceded the point, which on this desk is entered in the minutes. (The technical post-mortem of Act 1 is §1.8.3.)

**Act 2: Monday, 23 March 2020.** "Eleven days later," Ines said. "Things have not improved. What's new?"

What was new was an absorber. On 23 March 2020 the Federal Reserve established the Secondary Market Corporate Credit Facility (Federal Reserve). Kaz added a node to the graph on the projector: a dashed box labelled *Fed (SMCCF)*, with an arrow into the IG segment and a capacity so large that the line width broke the plotting library's default scale.

"Back in my day," Mags said, "I read that announcement on my phone in an elevator, and when the doors opened I knew two things. One, the IG market was going to stop falling. Two, anything that wasn't IG was going to fall harder, because everybody would sell what the Fed wouldn't buy to raise cash for what it would."

"Is that in the model?" Theo asked.

"It's in the edges," Kaz said, and showed him. The facility was for investment-grade issuers. In equation (1.6), a new absorber with a very large $A$ had appeared, but only in the segments it was allowed to buy. Everything outside that boundary still had the old, exhausted absorbers: high-yield funds that were themselves facing record outflows, crossover funds the model assumed had little dry powder left, and dealers whose balance sheets the model assumed were full. "The Fed made the IG imbalance small," Kaz said. "It made the boundary very important."

"Which brings us to the boundary," said Ines.

**Act 3: Wednesday, 25 March 2020.** On 25 March 2020 S&P cut Ford to BB+ (as reported by Bloomberg). With two high-yield ratings, roughly \$36bn of Ford debt would leave the investment-grade index at the month-end rebalance (T. Rowe Price, Nov 2020). Ford was not alone; it was the headline. More than \$90bn of debt fell from investment grade in that one month, nearly twice the prior monthly record of \$48bn set in 2005, and the first half of 2020 would reach \$197bn, the largest on record (J.P. Morgan data via T. Rowe Price, Nov 2020).

Kaz read the mechanism aloud from Man's paper, because it describes the next six days exactly:

"'When a company is downgraded to below investment grade status by the ratings agencies, it drops out of the index at the next monthly rebalancing and there is a significant wave of forced selling around the event'" (*Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.38*).

"That's a date," Theo said. "It's on a calendar. Anyone could have read it."

"Everyone did," Mags said. "That's the point. A forced sale you can see coming is still a forced sale. The seller has no choice about *whether*. They only have a choice about how badly to do it."

Kaz ran the graph with the demo numbers from Listing 1.3, which are Ford-sized and illustrative: holders forced to sell \$12.9bn; absorbers with \$6.5bn of capacity; \$6.4bn left over for the dealers. At \$0.5bn of daily volume and an impact of 0.4 points per day of volume, the imbalance of 12.8 days' volume opened a dent of 5.12 points below fair value. With the stress toggle on, every absorber switched off, the March 2020 setting, all \$12.9bn went to the dealers, and the dent more than doubled.

"Which is it?" Theo asked. "Stress or not?"

"That," said Ines, "is the only question that matters this week, and the model can't answer it. The model can tell you what each answer costs."

Then came the part of the replay that nobody puts in a war story, which took most of the next hour. Theo, reading down the holdings table Kaz had loaded, noticed that one large fund appeared twice: once in the "IG index funds" column and again in "IG active," because the vendor's holdings file classified a fund-of-funds by its wrapper rather than by its rulebook. The forced supply was overstated by the size of that fund. Kaz fixed the mapping, re-ran the graph, and the conservation assertion, which had been passing all along, kept passing, because a double-counted seller is still perfectly conserved: it sells twice and someone buys twice. "The assertion checks the plumbing," Kaz said, a little defensively, "not the census." Then Mags pointed out that the insurers' edge was firing on the rebalance date, when every insurer she had known in 2020 sold over the following quarters, if at all, because a higher capital charge makes holding costly but not impossible. Kaz split the insurer edge into a slow window, which shrank the day-one imbalance and fattened the tail of the pressure curve. Neither fix was clever. Both changed the answer by more than any parameter Kaz had spent the morning tuning. That is what the "Where this blows up" paragraph in §1.8.1 looks like on a Saturday: holders double-counted, windows misaligned, and a model that is exactly as good as its census.

<!-- FIGURE: ch01_march2020_timeline.png (12 Mar LQD −5.0% / VCIT −3.2% / SPIB −3.1%; 13 Mar −0.19%; 23 Mar SMCCF; 25 Mar Ford to BB+; 31 Mar index rebalance; 12 May ETF purchases begin; Jun bonds; 31 Dec purchases end) -->

#### Decision point: 30 March 2020

**Act 4: Monday, 30 March 2020.** Ines wiped the board and wrote one line. "Rebalance is tomorrow. Who has to sell, who has to buy, and what do we bid?"

Kaz went first, because Kaz always goes first. "The sellers are IG index funds and ETFs. They are the textbook uninformed seller. They don't know anything about Ford; they know about a rulebook. So $\pi \approx 0$. The toxicity term vanishes. The bid is fair value minus inventory minus cost, and the only hard part is sizing the inventory term, because $\sigma_{\text{IDO}}$ is enormous right now. Use DTS, with the crisis slope." Kaz sat back. "Buy. Size by DTS. Collect the reversal."

Mags shook her head, not in disagreement exactly. "I've seen fallen angels stay fallen," she said. "Your $\pi$ is about the *seller*. It says the index fund isn't selling because it knows something. Fine. But the seller doesn't have to know anything for the bond to be worth less next month. Ford sells cars. In March 2020 nobody was buying cars. The fair-value term is moving under you while you're busy congratulating yourself about the toxicity term." She tapped the run sheet. "A forced seller is information-free about the bond. It isn't a guarantee about the bond."

"So the distance to default matters," Theo said.

"Distance to default, equity momentum, whether anyone in the capital structure has hired counsel," Mags said. "All the things that tell you whether this is a fallen angel or a falling knife."

Theo had been quiet, drawing the graph in his notebook. Then he asked the question the replay was designed to provoke. "The Fed's facility is for IG issuers. Ford isn't IG any more. But what if the Fed decides that bonds which were IG a week ago still count? What does that do to $A$?"

"Is that a question," Kaz asked, "or are you buying lunch?"

"It's a question. It's 30 March. I'm asking what *could* happen."

The room went quiet in the way a room does when someone has asked the right question for the wrong reason, or the wrong question for the right one. "If that happened," Kaz said, "there would be a new absorber, with a very large $A$, on the high-yield side of the boundary. The imbalance would collapse. The dent would heal faster. And the reversal you were about to be paid for would be paid to you by the central bank, not earned by your balance sheet."

"So do you want it to happen or not?" Ines asked.

"I want it to happen," Theo said. "I just don't want to pretend I'm smart if it does."

Ines handed out index cards. "It is 30 March 2020. The rebalance is tomorrow. You do not know what the Fed will do in April. Write three things: what you bid, in what size, and why. Then we'll look at what happened."

The question is the reader's too. Before turning the page, write your own card: *what would you bid, in what size, and why?*

<!-- FIGURE: ch01_forced_seller_flow_graph.png (holders: IG index funds, IG active, insurers, CLOs, open-end HY; absorbers: HY index funds, fallen-angel programs, crossover/distressed, dealer residual; Fed dashed from t0+10; widths from the Listing 1.3 demo: USD 12.9bn supply, USD 6.5bn capacity, USD 6.4bn dealer residual) -->

**What happened, and the answer.** Theo's question was the one that mattered. In April the Fed extended its corporate facilities to issuers that had been investment grade as of 22 March, which covered Ford. A forced-seller event became a forced-buyer event by announcement. In (1.6), a new absorber with very large $A$ appeared on the high-yield side of the boundary, and $I_k$ went from huge to manageable before most of the selling had happened. The one absorber the Acts left out was the most mechanical: HY index funds were forced to add the bonds at inclusion, which made Ford one of the largest issuers in HY indices overnight.

*How a systematic desk would have flagged it:* distance to default collapsing through February and March as equity fell and equity volatility rose (§1.5); Ford's equity in the bottom momentum decile (§1.6); the rating-agency watch list giving the trigger date, and the index calendar giving the window. *How it would have traded it:* Kaz's card, with the census fixed: estimate $Q^{\text{sell}}$ by holder, stand ready to absorb at the rebalance with $\pi$ near zero, and size with DTS rather than duration. IDO or it didn't happen: the profit that followed was mostly the Fed and spread beta, and a desk that booked it as alpha learned nothing.

The cards, when Ines turned them over, were instructive. Kaz had bid for full size at a DTS-scaled concession and written "$\pi = 0$" with a box around it. Mags had bid for a third of Kaz's size, written "fallen angel or falling knife?" and drawn an arrow to Ford's distance to default. Theo had bid for half, and under "why" he had written: *the seller is forced; the bond is not safe; the absorber I'm counting on might be me.* Ines read it twice and pinned it to the board. "That's the trade," she said. "Not because it made the most money. It didn't; Kaz's did, because the Fed bailed out the size. It's the trade because it would have survived the version of April where the Fed didn't come."

Mags packed the run sheets back into the box. "Back in my day we did all of this on the phone, by memory, and half of us got it wrong," she said. "This is better."

### 1.8.3 Case Study B: Post-mortem of Act 1 (LQD at a 5% Discount)

Read Act 1 back through the bid equation and it is the most uncomfortable case in the chapter. The ETF was not mispriced; the NAV was. Every term in (1.2) is measured from $S_t$, and $S_t$ is a mid built from exactly the kind of evaluated prices that made up the NAV; on 12 March 2020 the mid itself was the lie. A perfect toxicity model and a perfectly sized inventory term would both have been subtracted from the wrong number, so neither $\pi$ nor $q$ could save you: the only defence was to notice that the one live price in the market, the ETF's, disagreed with your mid by five points, and to believe the price that traded.

In the bid equation, both the inventory term and the cost term exploded at once: $\sigma_{\text{IDO}}$ jumped because DTS-scaled volatility jumps in a crisis (Ben Dor p.26), and $c(\Delta q)$ jumped because the exit was the same crowded door. In the flow graph, open-end funds and ETFs became sellers of whatever was liquid, and the absorber of last resort arrived only by announcement: the SMCCF of Act 2 began buying ETFs on 12 May 2020 (New York Fed, 11 May 2020) and corporate bonds in June, and ceased purchases on 31 December 2020 (Federal Reserve). Chapter 20 rebuilds the creation–redemption arbitrage band and shows why it widens exactly when you want to use it.

### Deep-Dive Resource Graph

- **Podcasts.** Bloomberg *Odd Lots* has covered fallen angels, credit ETFs and the March 2020 dash for cash in several episodes (search the archive by topic; we do not cite episode numbers).
- **Practitioner Writing.** T. Rowe Price, *Navigating the Fallen Angels in the Post-Coronavirus Landscape* (Nov 2020), https://www.troweprice.com/institutional/ch/en/insights/articles/2020/q4/navigating-fallen-angels-post-coronavirus-landscape.html . WealthManagement.com on IG ETF discounts (16 Mar 2020), https://www.wealthmanagement.com/etfs/under-market-stress-fixed-income-etfs-trade-with-wide-discount . Vontobel, *CLOs: Lessons from the Past* (20 Mar 2020), https://am.vontobel.com/insights/clos-lessons-from-the-past . Chicago Fed Insights on life insurers' interconnectedness (May 2026), https://www.chicagofed.org/publications/chicago-fed-insights/2026/assessing-life-insurers-interconnectedness . Insight Investment (BNY), *Hidden in Plain Sight: Seeking Opportunities in Fallen Angels* (Aug 2026), https://www.bny.com/investments/us/en/institutional/articles/fixed-income/hidden-in-plain-sight-seeking-opportunities-in-fallen-angels.html .
- **Academic Papers.** Ellul, Jotikasthira and Lundblad (2011), *Regulatory Pressure and Fire Sales in the Corporate Bond Market*, Journal of Financial Economics 101(3). Ambrose, Cai and Helwege (2008), *Forced Selling of Fallen Angels*, Journal of Fixed Income. Coval and Stafford (2007), *Asset Fire Sales (and Purchases) in Equity Markets*, Journal of Financial Economics. Haddad, Moreira and Muir (2021), *When Selling Becomes Viral: Disruptions in Debt Markets in the COVID-19 Crisis and the Fed's Response*, Review of Financial Studies. O'Hara and Zhou (2021), *Anatomy of a Liquidity Crisis: Corporate Bonds in the COVID-19 Crisis*, Journal of Financial Economics. Kargar, Lester, Lindsay, Liu, Weill and Zúñiga (2021), *Corporate Bond Liquidity during the COVID-19 Crisis*, Review of Financial Studies 34(11).
- **Data & Code.** Federal Reserve, Secondary Market Corporate Credit Facility, https://www.federalreserve.gov/monetarypolicy/smccf.htm . New York Fed SMCCF notice of 11 May 2020, https://www.newyorkfed.org/newsevents/news/markets/2020/20200511 . Federal Reserve Z.1 Financial Accounts (holders of corporate bonds by sector), https://www.federalreserve.gov/releases/z1/ .

---

## 1.9 Toxic Flow: When the Seller Knows

The forced-seller graph is the good news: flows you can see coming, from sellers who know nothing. The cold open was the bad news: a seller who knew everything. The difference between them is the permanent component that (1.7) leaves out and (1.2) charges for.

### 1.9.1 Case Study C: Serta Simmons, 2016–2026 (the Counterparty Who Knew)

> **Docket Diary.** *November 2016:* Serta Simmons Bedding borrows under a \$1.95bn first-lien term loan. *June 2020:* a majority group holding about 52.6% of the roughly \$1.887bn first-lien loans exchanges about \$992mm of them into about \$734mm of new super-priority "first lien second out" debt (\$734mm is the first-lien participants' share; all second-out issued, to first- and second-lien participants alike, was about \$875mm; §5.6.2 reconciles the two), alongside \$200mm of new money; the excluded lenders, about 47.4% (roughly \$895mm), are primed. *31 December 2024:* the Fifth Circuit holds that the exchange was not an "open market purchase" and that the excluded lenders' sacred right to pro rata sharing was breached. *7 July 2026:* on remand, the participating lenders are held liable for \$261.13mm of damages as of 22 June 2020, plus 9% New York prejudgment interest, with the cashless exchange treated as a "payment" (Mayer Brown, July 2026). The Ad Hoc Group, in unison: "We were represented by counsel. We were not, the Fifth Circuit has now clarified, represented in an open market."

#### Long Scene 2: The Counterparty Who Knew

*Mags's story is fictional: the dealer, both accounts, every RFQ, every bid and every conversation are invented, and no real lender is depicted sending or answering any of them. The Serta facts around the story are from the court record and the sources cited in the Docket Diary above and the coda below.*

It came up three hours into the quarterly review of the toxicity model, when Kaz, defending it, said something that sounded reasonable. "The informed seller is a theoretical construct. We estimate a probability. We have never actually *met* one."

Mags put her pen down. "I have," she said. "Twice in one afternoon. Only one of them was."

The Risk analyst, who had a train to catch, looked at the clock, and stayed.

"June 2020," Mags said. "The week before the 22nd. I was running the distressed loan book at the bank I told you about in March, the one with the coffee. Serta Simmons Bedding. Mattresses. You heard things that spring, and I'm not going to repeat them, because half of them turned out to be wrong. What I can tell you is what the documents said, because the documents were public, and nobody read them."

"What did they say?" Theo asked, because somebody had to.

"The 2016 credit agreement had a pro rata sharing clause, a sacred right that needed every affected lender's consent to change. It also let the company buy back its own loans on a non-pro-rata basis, two ways: through a Dutch auction open to all lenders, which it defined, or through 'open market purchases,' which it didn't." She drew two boxes on the whiteboard and wrote *defined* in one and *undefined* in the other. "One defined term next to one undefined phrase. Put a restructuring adviser in front of that page, someone like Theo, and they'd have circled the undefined one in the first hour. On a trading desk in June 2020, I don't think anyone circled anything. We were still recovering from March."

Theo, who had been on exactly that kind of team, said nothing, but he wrote *open market purchase* in his notebook and underlined it twice.

**10:40 a.m.** "First RFQ," Mags said. "An account sells ten million of the first-lien term loan. I knew the account, or I thought I did: a CLO manager's trading desk, a steady seller of names that had slid toward the bottom of the rating scale, always polite, always the same size, always at the same time of the month. I assumed it was trimming a CCC bucket. Everything about it looked like the CLO seat Ines drew for you: a rulebook selling, not a person." She shrugged. "Loans settle slowly; you agree a price on the phone or the platform and the paperwork takes a week or more. So you're not just buying the loan. You're buying a week of not being able to change your mind."

**11:45 a.m.** "Second RFQ. A different account. Same facility, same size, ten million. Same screen price, because the screen hadn't moved in two days." Mags tapped the whiteboard. "This one I knew less well. A fund that had been in lender groups before, on other names, and that I learned afterwards had been pitched the Serta deal and passed. Quiet on Serta for weeks. And then a call, not a platform request: 'need it done today,' and a tone I'd heard before."

"What tone?" Kaz asked.

"The tone of someone who wants out before something, rather than out of something." She paused. "Here's what you need to understand about the inside of these deals. A lender who has been brought over the wall, who has signed a confidentiality agreement and heard the terms, is usually restricted from trading. That's the rule, and most people follow it. So the dangerous seller is rarely the one in the room. It's the one who was pitched and passed. Or the one who has just found out that the room is full and the door is closed. Or the one who simply read the agreement more carefully than you did and drew the obvious conclusion. None of them has to have done anything wrong. All of them know more than you."

(The Ad Hoc Group, the book's Greek chorus, offers its customary comment at this point, in unison and through counsel: "We do not comment on market rumours. We are, however, available for a call at 2 p.m.")

#### Decision point: two sellers, an hour apart (June 2020)

Ines did the thing she does at every decision point. She turned to the room. "Same facility. Same size. Same screen price. Two sellers, an hour apart. Bid both, bid one, or pass? And what would you need to know to tell them apart?"

Write your own card before reading on: bid both, bid one, or pass, and what would tell the two sellers apart?

Kaz answered first, carefully. "From the loan's price history, nothing. The two trades are identical. Same instrument, same size, same price, same day. Any model that only looks at the loan gives them the same bid. So the information has to be in the features of the *sender*, not the loan."

"Which features?" Ines asked.

Theo had them before she finished, and he gave them the way she had taught him to, one likelihood ratio at a time. "Whether the account is in the group, or has been in groups like it. Whether it called or used the platform, and whether it showed the loan to one dealer or to everyone. How close the request is to any lender meeting we know about. The account's own markout history with us: what happened to the last twenty things we bought from it. And the document itself, because the document tells you how big $J$ can be. If the agreement lets the company do a non-pro-rata deal with a bare majority, then the left-behind lenders can lose a great deal, and anyone who knows a deal is coming knows which side of it they don't want to be on."

"Then pass on both," Theo said. "If I can't tell them apart with confidence, I don't play."

"Passing is a price too," Ines said. "You learned that on a Friday. Here's the other half of the lesson. If you pass on the CLO, the CLO calls someone else next month, and the month after. A dealer who refuses every seller in a stressed name ends up being shown only the flow nobody else wanted, because the good flow goes to whoever bids for it. That's adverse selection on the *franchise*, not the trade. You pass your way into a book of nothing but toxic RFQs."

"Then bid both at the same price," Kaz said, "and let diversification work. Over a thousand hands, the informed ones are a small fraction."

"Diversification works across independent hands," Ines said. "The informed seller isn't an independent hand. She's a player who chooses *when* to sit at your table, and she sits down exactly when the hand is worth the most to her and least to you. If you show everyone the same price, the people who know more than you will take it on precisely the days it's wrong." She turned to Mags. "So what's left?"

"What's left is the only thing that ever works," Mags said. "Different prices for different senders. Which means you need a number for each of them."

"Good," said Ines. "Now put numbers on it."

Kaz did, on the whiteboard, labelled *(illustrative)* in large letters because the Risk analyst was watching. Prior share of informed sellers in a stressed loan in a quiet week: 3%. The first account: a known CLO seller, platform request, the usual size and day of the month, no lender meeting on the calendar that the desk knew of. Each of those features has a likelihood ratio near or below one. Call the product 0.5. Posterior odds about 0.015; $\pi \approx 1.5\%$. The second account: a lender-group regular, a phone call rather than a platform request, urgency, weeks of silence. Kaz assigned 4 for group history, 2 for the urgency and channel, 1.5 for the silence. Posterior odds about $0.031 \times 12 \approx 0.37$; $\pi \approx 27\%$.

"And $J$?" Ines asked.

"That's the hard part," Mags said. "Back in my day, which is still this story, I didn't know $J$. I knew it could be large, because the document allowed a majority to prime the minority. In the end the remand court valued what the left-behind lenders kept at about 25 cents on the dollar as of 22 June 2020: \$223.75mm on \$895mm of loans (Mayer Brown, July 2026). You don't need to know that number to know that $J$ was not a two-point move."

Kaz finished the arithmetic. With any $J$ in the tens of points, the first account's toxicity charge was a fraction of a point and the second's was several points. Same facility, same screen, two bids several points apart.

"So what did you do?" Theo asked.

"I bid the first one at my normal concession and bought it. I showed the second one a bid well below the screen, the bid my gut said, which was about what Kaz's board says now. They didn't hit it. Somebody else bought it at the screen price an hour later; I saw it go."

"So you were right," Kaz said.

"I was half right, which on a loan desk is the same as being wrong with better manners." Mags looked at the board. "On 22 June the transaction closed. The majority group, about 52.6% of the first-lien class, exchanged its loans into new super-priority debt and put in \$200mm of new money. The rest of us, about 47.4%, were primed. *Including* the ten million I bought from the CLO."

There was a silence in the room. Theo broke it, because he had worked it out and could not help himself. "The CLO wasn't informed. It just sold you a loan that was about to be primed."

"Right. And that's the lesson I took the longest to learn." Mags drew the coin from §1.1 on the board, the one that pays 100 or 78. "The CLO sold me a fair coin that came up tails. The second account offered me a coin it had already looked at. On the day, I lost money on the fair coin, and I would have lost more on the other. But the fair coin is a coin you can flip a thousand times and come out even, because across a thousand CLO sales the screen price is right on average. The coin someone has looked at is a coin you lose on *every time you play*. My markout on the first trade was bad luck. My markout on the second, if I'd done it, would have been bad selection. The hand history can tell those apart, but only over many hands, and only if you bucket the trades by who sent them."

Ines nodded slowly. "Which is the whole of the toxicity term."

"Which is the whole of the toxicity term," Mags agreed. "I just paid for it by the trade instead of by the model."

The Risk analyst missed the train. In the minutes, under *Action items*, someone wrote: "Bucket markouts by sender, not by name. (Mags, June 2020.)" Ines added a second line underneath, in the tournament-scorecard hand: *Five-day markouts on every RFQ, bucketed by Theo's features; the average per bucket is* $-\pi J$*. Kaz: the toxicity model (Ch 3). Theo: the Priming Risk Score that feeds it (Ch 13).*

#### Coda, 2023–2026: what the words cost

The story did not end on 22 June 2020. Serta filed for Chapter 11 in the Southern District of Texas on 23 January 2023, about 31 months after the uptier. The bankruptcy court in Houston upheld the transaction in 2023; on 31 December 2024 the Fifth Circuit reversed, holding that an open market purchase "occurs on the secondary market for syndicated loans" and that the 2020 uptier did not qualify (Fifth Circuit opinion, 31 Dec 2024); rehearing was denied on 18 February 2025, and the Supreme Court denied certiorari on 10 November 2025. The coalition arithmetic was brutal while it lasted: non-participating lenders' recoveries were about 0.6–2.4%, against 100% and about 75% for the participants' tranches (Skadden). Then the July 2026 remand put a price on the phrase.

The same day the Fifth Circuit ruled on Serta, New York's Appellate Division upheld Mitel's uptier, because Mitel's agreement let it "purchase" loans with no "open market" qualifier at all (Mayer Brown, May 2025); and in December 2025 a federal district court reversed the bankruptcy court and blessed the multi-step Wesco/Incora uptier (Mayer Brown, January 2026). Three courts, three documents, three outcomes. "Open market purchase" has become the most expensive three words in finance: on the Serta remand they were priced at \$261.13mm plus nine percent a year since June 2020, for a phrase nobody had defined.

Kaz read the Fifth Circuit's sentence twice and asked the question every quant asks once. "So the 'open market' is a place. Is there an address? Did they try to find it and fail?"

"Nobody could find it," Mags said. "That's more or less what the court said."

"Then why didn't the agreement just say where it was?"

"Because in 2016 nobody imagined they'd need to." Mags put the run sheets away. "That's what you're paying for when you read a credit agreement, Kaz. Not what the words say. What nobody imagined they'd need them to say."

(Cooperation agreements signed in this book so far: 0. The lenders left behind in Serta went to court afterwards, as plaintiffs, and the counter stays at 0; Chapter 13 builds the question of who was organized before the deal into the Priming Risk Score.)

> **Trend Watch: Liability management takes over the default statistics, 2024–2026.** *What changed:* most "defaults" are now negotiated. Distressed exchanges were more than 60% of default volume in 2024 through mid-December, the highest share since at least 2000; the 2024 HY default rate was 1.4% including distressed exchanges against 0.3% excluding them, and for loans 4.0% against 1.5% (Marquette Associates, 18 Dec 2024). Moody's (18 May 2026) put distressed restructurings at about 65% of 2025 corporate defaults, and in its sample of 1,173 borrowers with soft credit events since 1979, about one in four ended in a hard default, with more than 70% of eventual hard defaults after a distressed restructuring arriving within two years. *What it means for the desk:* the jump $J$ in the bid equation is increasingly a *negotiated* jump, timed by lender calls and documents rather than by a missed coupon, which makes counterparty state the dominant feature in $\pi(\mathbf{x})$ and makes "default" a poor label for anything you train on. Chapter 14 models the regime shift.

A market in which the jump is negotiated is a market in which the most important fact about any RFQ is who was in the negotiation, which is why Scene 2, the counterparty who knew, is the chapter's last word, not Scene 1.

---

## 1.10 Desk Debrief

**Finder.** Where each tool lives in the chapter: the equation, the box that builds the intuition, the scene where someone used it (or broke it), and the code.

| Concept | Eq. | Intuition (box) | Judgment (scene) | Code |
| :-- | :-- | :-- | :-- | :-- |
| Bid equation | (1.2) | Conditional expectation, §1.1 (the coin worth 82.4) | Halvorsen, Friday 2:58: 91.40 versus 83.60; passing is also a price | Listing 1.1 |
| Inventory term | (1.1) | Pricing by indifference, §1.3.2 | "Whose five days?" (§1.3.2): trust it only while the hedge is real, the residual wiggles rather than jumps, and the horizon is yours; on a book, use the book's variance (Ch 8, 28) | Listing 1.1 |
| Toxicity and Bayes | (1.2), logit form in §1.3.3 | Bayes in odds, §1.3.3 (5% becomes 39%) | Serta, two RFQs an hour apart (§1.9.1): price the sender, and bucket markouts by sender | Listing 1.1 |
| DTS | (1.3) | Additive versus proportional, §1.4 | Mags's two circled lines and Theo's percent column (§1.4): rank and set limits with it while the bond is a spread instrument in a calm month; the crisis steepens the slope | Listing 1.2 |
| Liquidity cost score | Ben Dor p.112, p.118 | (none; the annotation) | "A recovery and a grudge" (§1.4): switch to the price-quoted branch below about 70 | Listing 1.2 |
| Distance to default | (1.4) | Equity is a call; fat tails, §1.5 | Mags on Halvorsen (§1.5): ranks well, calibrates badly; is the stock a claim on the firm or a lottery ticket on the plan, and is the new senior debt in $F$? | Listing 1.4 |
| Credit triangle | (1.5) | Waiting for the phone; risk-neutral, §1.5 | Kaz's 12 bp (§1.5): feed it $\mathbb{Q}$ intensities only | Listing 1.4 |
| One-factor model | $p(Y)$, §1.5 | Correlation and the common factor, §1.5 (2% becomes 9.7%) | Forced sellers arrive in herds: the bad-factor year is the one in which every CLO, insurer and index fund sells | Listing 1.4 |
| Forced-seller flow graph | (1.6) | Conservation, §1.8.1 | Ford, Act 3 (§1.8.2): a double-counted fund passes the conservation test; check the census | Listing 1.3 |
| Price pressure and the fallen-angel reversal | (1.7) | Exponential decay and half-life, §1.8.1 | Ford, Act 4, "fallen angel or falling knife?": buy when the trigger is a mandate, the absorbers have capacity, and nobody has hired counsel; strip the beta before calling it alpha | Listing 1.3 |

On the Friday train home, four weeks after Halvorsen, Theo found the old term sheet for the Halvorsen notes folded inside his notebook, where he had kept it since the Monday the bonds opened at 78. The USB stick was in his pocket, as always. He turned the term sheet over and wrote, in the small, square hand he had once used for margin notes on credit agreements, three lines. *Fair value: what is it worth to someone who knows only what's public?* *Inventory: what does it cost me to hold it until someone else wants it?* *Toxicity: who is selling, why now, and what do they know?* Under the third line he wrote *this one is mine*, then crossed out *mine* and wrote *ours*, because Ines had been right about that too.

The train stopped between stations, as it does, and he used the time to write down what he could do now that he could not do on the Friday. He could derive the bid, from an indifference price and one application of Bayes' rule, and say which part of the book builds each of its three terms. He could read the shelf, Ben Dor, Bohn–Stein, Schmid, Bolder, Veronesi, Dynkin, Paleologo, Moyer, Houlihan Lokey and the five industry papers, as one long argument about forced flows rather than fourteen unrelated textbooks. He could draw a downgrade as a **forced-seller flow graph**, with holders, triggers, response windows and absorption capacity, so that it became a map of who must sell to whom. He could put dated, sourced numbers on how that graph had changed between 2018 and 2026, which is the difference between an opinion and a view. And he could hand ROBO a spec precise enough to build the graph instead of a single node labeled "Everyone, March 2020", which, when he thought about it, was the test of the other four. Under that he wrote the list that follows, and taped it to his monitor on Monday.

- **Every bid is three bets.** Fair value, inventory, toxicity: $B^* = S_t - \pi J - \tfrac12\gamma\sigma^2_{\text{IDO}}h(2q+\Delta q) - c$. Kaz's engine got two of them right; the third cost \$2mm.
- **A forced sale is information-free about the bond and information-rich about the seller.** Price the seller, not just the CUSIP.
- **$\pi$ is a function of who is on the call.** The Bayes step turns counterparty state into a logistic regression; markouts by feature bucket are how you estimate it.
- **Risk scales with spread.** Use DTS, not spread duration, and remember that the slope steepens in a crisis. Below about 70, stop quoting spreads and start modeling recoveries.
- **Calibrate, don't just rank.** A Gaussian DD of 4 says 0.003%; an empirical map says almost 1%. Feed only $\mathbb{Q}$ quantities into the credit triangle.
- **The holder graph is getting more mechanical.** CLOs (about 65% of loans), ETFs (about \$2tn), insurers' private placements (48% of life-industry bonds) and sharp dealer net shorts mean more rule-driven supply and less natural absorption.
- **Execution made it possible; replication will decide what survives.** Half of IG trades electronically and PT is 15% of volume, but most published bond factors fail on clean data. Flows paid for by someone's mandate are sturdier than factors found in a regression.
- **IDO or it didn't happen.**

### The Spec You Hand the Robot

> Build a Python module `desk_core` (numpy, pandas, scipy; seeded; no I/O). (1) `reservation_bid(S, q, dq, gamma, sigma_ido, h_years, pi, J, c)` per eq. (1.2), measure $\mathbb{P}$; units: points per 100 par, \$mm par (long positive; `dq > 0` = client sells), points per $\sqrt{\text{year}}$ *post-hedge* for `sigma_ido`, $1/(\$\text{mm}\cdot\text{pt})$, years; raise on `dq <= 0`, `pi` outside $[0,1]$, `h_years <= 0`, negative scale inputs; never clip a short desk's bid. (2) `posterior_informed(mu, log_lr)` in logit form; reject `mu` in $\{0,1\}$; `jump_penalty_ratio`, tending to 1 as $\gamma q\ell \to 0$ and rising in $q$. (3) `dts_vol(D_spr, s_bp, sigma_rel)` per eq. (1.3), result in bp per period; `lcs()` with spread-quoted and price-quoted branches. (4) `ForcedSellerGraph(holdings, rules, capacity)` per eqs. (1.6)–(1.7) with pro rata absorption, a `dealer_residual` node, `edges`, and `price_path`. Mandatory assertions: comparative statics of the bid ($\partial B/\partial q<0$, $\partial B/\partial\pi<0$, $\partial B/\partial\Delta q<0$); simulated markout equals $-\pi J$ within 3 s.e.; lognormal Monte Carlo reproduces DTS·$\sigma_{\text{rel}}$ within 2%; conservation of flow to $10^{-9}$; stress toggle sends all supply to `dealer_residual`; price path reverts to within 0.01 points by `10/theta` days. Do not condition on the RFQ twice. Label every demo number illustrative.

### Exercises

1. **(Derivation.)** Derive the dealer's *ask* for a client buying $\Delta q$, and show that the bid–ask midpoint for a two-sided quote of size $\Delta q$ equals the reservation mid $r^{\text{res}} = m - \gamma\sigma^2_{\text{IDO}}h\,q$ when both sides carry the same $m$. What happens to the midpoint when the buy-side RFQ carries a different toxicity $\pi'$?
2. **(Bayes, with a poker face.)** The prior share of informed sellers is 3%. An account in a known ad hoc group sells 58 minutes after a lender call, which you estimate multiplies the likelihood ratio by 12, and shows the bond to five dealers, which multiplies it by 1.5. Compute $\pi$. At $J = 13$ points, how many points does toxicity take off the bid? Would you rather know the jump size or the counterparty?
3. **(DTS.)** A portfolio holds equal market values of a 10-year BBB at 140 bp and a 3-year CCC quoted at 68. Explain why DTS is meaningful for the first and not the second, and propose a single risk measure that covers both (hint: Ben Dor's two-branch LCS is a clue).
4. **(Flow graph.)** Re-run the Ford-sized example with the Fed added as an absorber with \$5bn of capacity from day 10. Modify `run` so capacity can arrive on a date, and show how the drop and the 60-day reversal change. Who earned the reversal: the desk, or the central bank?
5. **(ROBO literalism.)** Write the one-sentence vague spec that would make ROBO fit a toxicity model with a perfect in-sample markout and zero out-of-sample value. Then write the two clauses that prevent it (one concerns issuer-grouped cross-validation, Chapter 7; the other concerns the label window).
6. **(Courtroom quant.)** Using the Serta and Mitel facts, write a binary feature "credit agreement permits non-pro-rata purchases without an open-market qualifier," and argue whether it belongs in $\pi(\mathbf{x})$, in $J$, or in both.

### Deep-Dive Resource Graph

- **Podcasts.** Bloomberg *Odd Lots* episodes on corporate bond market structure, portfolio trading, liability management and private credit (search by topic; episode numbers deliberately omitted). *Flirting with Models* (Corey Hoffstein), https://www.flirtingwithmodels.com/ .
- **Practitioner Writing.** Coalition Greenwich, *U.S. corporate bond trading in 2025 by the numbers* (27 Jan 2026), https://www.greenwich.com/node/158274 , and *Dealer net short in corporate bonds sets record* (17 Feb 2026), https://www.greenwich.com/node/158326 . The DESK on 2025 credit e-trading (30 Jan 2026), https://www.fi-desk.com/?p=27374 , and on portfolio trading (19 Feb 2026), https://www.fi-desk.com/ig-credit-sees-portfolio-trading-plateau-while-hy-hits-records/ . IFR, *Portfolio trading continues dizzying growth* (2025), https://www.ifre.com/topic-codes/2293541/portfolio-trading-continues-dizzying-growth . Mayer Brown on Serta's damages ruling (Jul 2026), https://www.mayerbrown.com/en/insights/publications/2026/07/serta-simmons-bedding-the-fifth-circuits-uptier-decision-and-the-landmark-damages-ruling-on-remand , on Serta and Mitel (May 2025), https://www.mayerbrown.com/en/insights/publications/2025/05/serta-and-mitel-the-latest-major-court-decisions-on-uptier-transactions , and on Wesco (Jan 2026), https://www.mayerbrown.com/en/insights/publications/2026/01/the-state-of-play-on-uptiers-district-court-reversal-in-wesco-blesses-multistep-transactions . Proskauer, *The End of Non-Pro Rata Uptiers?* (2 Jan 2025), https://www.proskauer.com/alert/the-end-of-non-pro-rata-uptiers . Marquette Associates, *A Damsel in Distress* (18 Dec 2024), https://www.marquetteassociates.com/damsel-in-distress/ . Moody's, *Lend, extend, and then...* (18 May 2026), https://www.moodys.com/web/en/us/insights/credit-risk/private-credit/lend-extend-and-then.html . Matt Levine, *Money Stuff* (Bloomberg Opinion), on uptiers and "open market purchases"; *Petition* on restructuring.
- **Academic Papers.** Dickerson, Robotti and Rossetti (2026), *The Corporate Bond Factor Replication Crisis*, arXiv:2604.07880, https://arxiv.org/abs/2604.07880 . Dickerson, Mueller and Robotti (2023), *Priced Risk in Corporate Bonds*, Journal of Financial Economics 150(2). Jostova, Nikolova, Philipov and Stahel (2013), *Momentum in Corporate Bond Returns*, Review of Financial Studies 26(7). Kelly, Palhares and Pruitt (2023), *Modeling Corporate Bond Returns*, Journal of Finance 78(4). Houweling and van Zundert (2017), *Factor Investing in the Corporate Bond Market*, Financial Analysts Journal 73(2). Israel, Palhares and Richardson (2018), *Common Factors in Corporate Bond Returns*, Journal of Investment Management 16(2).
- **Data & Code.** Open Source Bond Asset Pricing (error-corrected TRACE and bond factors), https://openbondassetpricing.com/ . FINRA TRACE, https://www.finra.org/filing-reporting/trace . SEC EDGAR, https://www.sec.gov/edgar . CourtListener REST API, https://www.courtlistener.com/help/api/ .

<!-- STATUS: COMPLETE -->
