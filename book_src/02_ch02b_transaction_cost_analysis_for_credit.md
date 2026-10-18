# Chapter 2-B: Transaction Cost Analysis for Credit: Arrival, Cover, Shortfall and the Dealer Scorecard

> **Prerequisites.** Chapter 2, in particular §2.3.2 (order statistics and the effective number of dealers), §2.5.1 (the router and its cost of failure $\kappa$), §2.9.1 (LCS units) and §2.9.3 (the April 2025 replay); §3.3 (markouts, IDO markouts and survivorship); §27.4.2 (the order state machine). Nothing else. Every new piece of mathematics is introduced from scratch in a Math, Gently box. The chapter ships `tca.py` through Appendix F.

*What is invented, once for the whole chapter.* The desk, its traders, its fills, its log, its dealer panel (anonymised A to K), its quarterly review, the salesperson who calls afterwards, the vendor report in §2B.9, and every number marked illustrative are fictional composites. So are Dov Adler's pod at Vantress Capital Management, its analyst Wen Zhao and its risk manager Marcus Oyelaran, and the invented issuers Kestrel Roofing and Halvorsen Packaging (Chapter 1-B). The papers, platform statistics, rules, dates and quoted public remarks are real and cited; where a real firm appears, it says only what a cited public document says it said, and none of them walks into a scene.

## Cold Open: Friday, 4:10 p.m., the Markout Meeting

*Friday 23 October 2026, the end of Theo's fifth week. The meeting is in the small conference room because the big one has a client in it, and the small one has a whiteboard nobody has fully erased since August.*

Every Friday at ten past four the desk reads its hand history (§3B.2). The markouts come first, dealer by dealer and signal by signal, and this week they are dull, which is the best thing a markout can be. Then Ines Okafor caps her pen and asks the question she saves for whoever looks most comfortable.

"Theo. What did our trading cost this week?"

Theo has spent five weeks on a systematic desk and six years in restructuring before that, and the restructuring years answer first. "Nothing. Bonds have no commissions. We paid the price, the price is in the P&L, and there's no fee line."

"Cost relative to what?"

He sees the trap a beat too late, and recovers the way he once recovered on creditor calls, by producing the one number in the system that looks as if it was built for the question. The execution system has a column labelled *cost vs composite*. He reads the week off it: 212 fills, notional-weighted, minus 0.8 basis points of price. "A gain, actually. We beat the composite."

Dr. Kasimir "Kaz" Lind does not look up. "Plus 2.1."

"Plus 2.1 what?"

"Same 212 fills, against the mid at the moment the optimiser decided to trade them." Kaz turns the laptop around: a notebook nobody else has seen, a column headed `decision_mid`. "We paid two basis points of price over where the bonds were when we chose them."

Marguerite "Mags" Dunleavy has been reading something with a great deal of red ink on it. She puts it down. "Against the cover we beat the market by one point nine. We beat the cover every week. Thirty years, and not one losing week against the cover."

"That," says Kaz, "is because the cover is the price we didn't take."

"It's still a price."

"It's the second-best price. We took the best one. Beating the second-best price is not an achievement, it's a definition."

Ines writes the three numbers in a column under the August doodle, which may once have been a yield curve: $-0.8$, $+2.1$, $-1.9$. Above them she writes *cost, positive is bad*, because two of the three were spoken with the opposite sign in mind.

"Three honest numbers," she says. "Same fills, same week, and none of them is a typo. Which one goes in the report?"

"The one the client will believe," Theo offers. Nobody laughs, which on this desk means everyone agrees the line was accurate and none of them enjoyed it.

"The composite tells you where the bond was," Ines says. "Arrival tells you what you decided. The cover tells you what the second dealer thought. And the print tells you who was right." She caps the pen. "Pick one and say why."

Theo looks at the column for a while, and the reasons come out of it one at a time. The execution system's column compares a buy with the composite's *offer* and a sale with its *bid*, so a fill that paid half the quoted spread shows up as a saving of the other half. Kaz's column starts the clock an hour earlier, at the decision, and so it charges the desk for the market's drift while the order sat in the router's queue. Mags's column cannot go above zero, ever, which is a strange property for a measure of cost. And none of the three columns has a row for the nine bonds the Wednesday rebalance tried to buy and could not.

"What did the ones we didn't fill cost?" he asks.

"That's the biggest number of the week," Ines says, "and it isn't in anybody's column."

In equities, cost is a number. In credit, cost is a *choice of counterfactual*. Every bond fill can be judged against four prices that disagree: the composite when the request went out, the arrival mid when the decision was made, the cover, and the next print on the tape. The one a desk picks decides whether it looks skilled, lucky or leaky. **The question this chapter answers: how does a desk choose its counterfactual on purpose, and how does it then price the three things an equity TCA never has to price, namely the order that did not fill, the quote that was shopped, and the second leg of a pair?**

By the end of the chapter you will be able to rebuild all four benchmarks from one RFQ log and say what each conditions on; decompose a rebalance's implementation shortfall into delay, drift, half-spread and the opportunity cost of what did not fill, with the market's share stripped out of the last term; test an accusation of information leakage against a placebo before making it; build a dealer and protocol scorecard that does not reward fair-weather liquidity; fit size-bucketed cost curves that know how many observations sit behind each point; read your own participation in the market from your own fills, net of a moving denominator; and write the two-leg cost of a pair trade, legging term included, as one line in a pod's ledger.

## 2B.1 Benchmarks for an RFQ Market

*Monday, before the 7:30 call. Kaz's desk, two chairs, one log.*

Kaz wants to rebuild Friday's three numbers from scratch, and Theo wants to know why they disagree, so they agree to start from the only object all three were computed from. Every inquiry the desk has ever sent sits in one table, the RFQ log, and every row in it walks through the order state machine of §27.4.2. Kaz says the log is the desk's diary; Theo, who has read a lot of diaries in data rooms, says it is more like a docket, because every entry is time-stamped by someone who will later be asked to explain it.

| Field | What it records | Stamped at |
| :-- | :-- | :-- |
| `order_id`, `parent_id` | one row per child order; the legs of a pair share a parent | `NEW` |
| `side`, `target`, `bond`, `protocol` | buy or sell, face asked for, the bond, and the door: disclosed RFQ, all-to-all, PT line, voice, session | `NEW`, `ROUTED` |
| `known_at` | the time of every transition: `NEW`, `ROUTED`, `QUOTED`, terminal | each transition |
| `panel`, `n` | which dealers were invited, and how many | `ROUTED` |
| `responses` | each dealer's level and time, or "no quote" | `QUOTED` |
| `best`, `cover` ($C$) | the best response and the second best | `QUOTED` |
| `fill` | price, size, counterparty, and which terminal state ended the row | terminal |
| `composite` | mid and same-side level, with source and age, at every stamp | each stamp |
| `print_after` | the first TRACE print after the terminal stamp: lag, price, capped size | terminal plus minutes |
| `regime` | the stress label in force at `NEW` (§2B.5 defines it) | `NEW` |

Benchmarks, shortfall, scorecards, cost curves and capacity are five readings of this one table, and the rest of the chapter derives each of them from it. The table is the buy-side mirror of the dealer's RFQ log that Chapter 18-B builds its quoting engine on, and the two logs describe the same events from opposite sides of the screen. The desk sees every response to its own inquiry. A dealer sees only its own quote and its own outcome, which Fermanian, Guéant and Pu sort into five bins in their study of European corporate-bond RFQs (FGP 2016, *Market Microstructure and Liquidity* 2(3–4); arXiv:1511.07773): **Done**, **Tied Traded Away**, **Covered**, **Other Traded Away** and **Not Traded**. One inquiry, read from both seats:

| Our terminal state (the client's log) | What each dealer on the panel records (FGP's bins) |
| :-- | :-- |
| `FILLED` with dealer $j$ | $j$: Done. The second-best responder: Covered, or Tied Traded Away if level with the winner. Every other responder: Other Traded Away. |
| `PARTIAL`, then `EXPIRED_PARTIAL` | Done for the piece that traded; the remainder as for `EXPIRED`. |
| `EXPIRED` with quotes on the screen | every responder: Not Traded. |
| `DONE_AWAY` | every responder: Not Traded. In this desk's usage the trader closed a quoted inquiry without hitting it and worked the order elsewhere, by voice, in a portfolio trade or in a later inquiry; the panel may see the result on the tape fifteen minutes later. |
| `EXPIRED` with no quotes, `REJECTED`, `CANCELLED` | no outcome for anyone; a dealer that declined is a censored observation (§2.3.2). |

Kaz reads the table twice and then asks the question that has been bothering them since Friday. "Mags called my column 'arrival'. Is that the bond arriving? At the custodian?"

"That's settlement," Theo says. "T+1."

"Good. I'd hate to wait a day for my benchmark." Kaz writes *arrival = decision mid* in the notebook margin, under an older note that reads *springing lien = seasonal?* with the question mark heavily crossed out.

### 2B.1.1 Four prices, four counterfactuals

Each benchmark lives at a stamp. The **arrival mid** is the composite mid at `NEW`, the moment the optimiser emits the order, which makes it the price of the decision. The **RFQ-time composite** is the mid at `ROUTED`, when the request leaves the building, which makes it the price of the market as the desk entered it. The **cover** $C$ is the second-best response at `QUOTED`, which exists only when at least two dealers answered. The **post-trade print** is the first TRACE print after the terminal stamp, which arrives up to fifteen minutes late (§2.2) with its size capped.

> **Math, Gently.** *A benchmark is a counterfactual.* A cost is a difference between what happened and what would have happened otherwise, and "otherwise" is a story somebody has to choose. A commuter who walks in at 9:12 is twelve minutes late against the timetable, four minutes late against when she would have arrived had she left the moment she decided to, three minutes early against the train she did not take, and five minutes early against the colleague who came in on the next one. All four are true, and each answers a different question. Here is one fill scored the same way *(illustrative)*. The desk buys \$2mm of a bond at 98.42. The composite mid was 98.38 at `NEW` and 98.40 at `ROUTED`, with a composite offer of 98.43; the cover was 98.45; the next TRACE print, 22 minutes later, was 98.47. Write the cost in basis points of price as $\eta(p - b)/b \times 10^4$, where $p$ is the fill, $b$ the benchmark and $\eta = +1$ for a buy ($-1$ for a sale). The one fill then costs $+4.1$ bp against arrival, $+2.0$ against the RFQ-time mid, $-1.0$ against the composite offer, $-3.0$ against the cover and $-5.1$ against the next print. Nine basis points of disagreement about one ticket, and Friday's whiteboard in miniature. The full version, in which these differences become the terms of a sum that adds up to something, is §2B.2.

The commuter's four numbers disagree because each is conditioned on a different piece of information, and the same is true of the fill's. Arrival conditions on the decision and nothing after it, so it charges the desk for its own delay. The RFQ-time composite conditions on the market at the door, so it forgives the delay and keeps the dealer's spread. The cover conditions on the dealers having answered and the desk having won. The print conditions on the future. A desk that wants to know whether its *router* is good benchmarks against the RFQ-time mid; a desk that wants to know whether its *process* is good, from signal to fill, benchmarks against arrival. Friday's three numbers were three honest answers to three different questions, and the meeting went wrong only because nobody had said which question was on the table.

Two of the four have a defect that is not about conditioning at all. Theo found the first; Kaz found the second.

### 2B.1.2 The composite that reads your mail

Theo's restructuring habit is to read the definitions section before the covenants, because "EBITDA" in a credit agreement means whatever the definition says it means. So on Monday he read the definition of the composite. MarketAxess's CP+ is an algorithmic price built from trades, quotes and inquiries on its platform, and Jacobsen, Venkataraman and Xu (2025, "Illiquidity Meets Intelligence: AI-Driven Price Discovery in Corporate Bonds," SMU working paper, with data supplied by MarketAxess) show two things about it that matter for anyone who benchmarks against it. The typical bond has no non-retail trade on about 60% of bond-days, so on most days the composite is a model rather than an observation. And requests that did *not* trade carry price information the model uses: when a did-not-trade RFQ falls between two trades, CP+'s advantage over the last trade price grows by a factor of 1.4 to 5.0.

"So the number we grade ourselves against," Theo says, "is partly built from our own requests. Including the ones we didn't trade."

"On that platform, in that bond, on a quiet day, yes." Kaz pulls up a bond the desk had been buying in clips all week. Its composite had risen a little after each of the desk's inquiries, including two that expired. "We pushed it up and then beat it. That's not execution, that's homework we marked ourselves."

"Back in my day the composite was Steve," says Mags, passing behind them with coffee. Steve is the dealer who has been punishing her for something since 1997. "At least you knew whose opinion it was."

There is a corporate version of the same worry. ICE agreed on 29 July 2026 to buy MarketAxess for \$167 a share in cash, with closing expected in the first half of 2027 (MarketAxess 8-K, Exhibit 99.1). ICE already sells evaluated bond pricing, so once the deal closes, two of the four or so composites a US credit desk is likely to subscribe to may sit under one owner, and the independence a desk assumes when it averages them will be an assumption about a single company's model governance.

None of this makes the composite useless. For a bond that printed this morning, in a protocol where the desk is one inquirer among dozens, the composite is the best neutral price available, and the RFQ-time composite is the right benchmark for judging the router. It turns circular for a bond the desk has been working for three days, where the desk's own unfilled inquiries are a large share of the composite's recent information. The repair Kaz and Theo settle on is modest. Arrival is stamped at `NEW`, before today's inquiry has touched anything, which removes today's reflexivity, though not yesterday's. And each composite's bias against the *subsequent* print is tracked bond by bond, so a composite that systematically leads the desk's own flow is caught as a pattern rather than suspected as a feeling.

### 2B.1.3 The cover is a survivor

Kaz's defect is about Mags's column, and it is a property of order statistics rather than of anybody's model. For the desk, the cover exists only when at least two dealers answered and the desk traded. The winner is the best quote, so the cover is worse by construction, and "cost versus cover" is the distance from the first to the second order statistic of the responses (§2.3.2). It measures how spread out the dealers were, and its sign is fixed before the trade happens. It is a survivor statistic in the sense of §3.3.5: it is computed only on the inquiries that survived to a fill, which are the inquiries where somebody wanted to trade with the desk at a price the desk liked.

The dealer's version of the same problem is worse, and FGP is where it is clearest. A dealer sees the cover only on the inquiries it won, so every likelihood it can write about its rivals is one-sided: it learns the shape of their quotes from the trades it did, never from the trades it lost. FGP's European data also show how thin the table usually is. Only about 40% of the dealers asked actually answer, the probability of answering falls as the panel grows, and the expected number of answers stays close to two whatever the panel size, so clients "often wait for only two answers." The client's reservation value, the level beyond which it walks away, sits about 1.7 half-spreads from the composite mid (Bloomberg's CBBT in their data). With two answers, the cover is simply the other answer.

Hendershott and Madhavan's US numbers are the same story at larger panels ("Click or Call? Auction versus Search in the Over-the-Counter Market," *Journal of Finance* 70(1), 2015, Table VI). Across MarketAxess auctions in 2010–11, dealers invited per auction ran at about 25 to 28, but the response rate was only 15% for micro trades rising to 29% for the largest; 8% to 15% of auctions got no response at all; and the fill rate fell from 73% for micro trades to 51% for the largest. Cost fell from 24–45 bp with few responders to about zero beyond ten. In the language of §2.3.2, responses are correlated: the authors' own observation is that dealers' decisions to bid "are not independent," and a beta-binomial fit to Table VI (our arithmetic, illustrative) puts the response correlation at about 0.06 for micro trades and about 0.30 for the largest, so a panel of 26 behaves like somewhere between three and eleven independent dealers, the same $n_{\text{eff}} = n/(1 + (n-1)\phi)$ that §2.3.2 derived for quote levels.

"So the cover is fine," Theo says, "as long as nobody calls it a cost."

"The cover is excellent," says Kaz. "It's the best measurement of dispersion we own. It tells you how much the second dealer disagreed with the first. It just can't tell you what you paid."

Mags, who has drifted back to read over their shoulders, has the last word on it. "In 1996 the cover was the number the salesman told you after you'd hung up. 'You were close, we were a sixteenth behind.' Every salesman on the Street was a sixteenth behind for ten years." She considers the screen. "This one at least is written down before anybody hangs up."

By ten past seven the whiteboard on Kaz's side of the desk holds the table they will use for the rest of the quarter.

| Benchmark | Stamp | Conditions on | Honest when | Misleads when |
| :-- | :-- | :-- | :-- | :-- |
| Arrival mid | `NEW` | the decision | the composite at `NEW` is fresh and owes nothing to the desk's flow | the bond has not printed for days; `NEW` is stamped late |
| RFQ-time composite | `ROUTED` | the market at the door | delay is reported as its own line | the desk's own earlier inquiries moved it |
| Cover $C$ | `QUOTED`, fills only | the second dealer's view | it is read as dispersion | it is read as a cost: it can never be positive |
| Next print | terminal plus minutes | who was right | it is averaged over many trades as a markout | it is read as one trade's cost, or the print is the desk's own |

The table has a fifth row that neither of them writes down yet: the orders that never reached a fill have no benchmark at all, because every column above is measured from a fill price. That row is the subject of the next section.

*Builds on:* §2.2 (TRACE timing and caps), §2.3.2 (order statistics, $n_{\text{eff}}$), §2.9.1 (units), §3.3.5 (survivorship), §27.4.2 (the state machine). *Used in:* §2B.2 (shortfall from the same stamps), §2B.4 (the cover as a dispersion statistic in the scorecard), Chapter 18-B (the dealer's log and FGP's likelihoods), §27.2.3 (the four timestamps of a fill), Appendix B (the RFQ-log schema).

## 2B.2 Implementation Shortfall, Credit Edition

*Wednesday 21 October, 9:40 a.m. The rebalance §27.4.2 uses as its example, retold from Theo's screen.*

At 8:10 the optimiser emitted the week's rebalance for the desk's systematic sleeve: forty child orders, twenty sales and twenty purchases, about \$90mm each way *(all sizes and prices in this section illustrative)*. Every order was stamped `NEW` at 8:10. The router held them while the morning's new-issue announcements cleared and sent them between 9:15 and 9:35. By 9:40 Theo is watching the blotter fill like a waterfall run in reverse. The sales went first and went easily, which is what sales do: Kargar, Lester, Plante and Weill find, in every MarketAxess inquiry from 2017 to 2021, that sells complete about twice as fast as buys ("Sequential Search for Corporate Bonds," FRB Philadelphia WP 25-08, 2025). Eleven purchases filled. Nine sat with quotes too far away to take, or none. By eleven o'clock seven of them were `EXPIRED` and two `DONE_AWAY`, and thirty-one of forty is the rebalance's final score. Each of the nine terminal states fired a residual-risk event, the optimiser re-ran, and the nine went back into the queue as retries for Thursday and Friday.

At 4:30 the execution system's report arrived: 31 fills, \$139.5mm, a cost of 6.4 bp against arrival, \$89,280. The nine were not in it, because a report built from fills has nowhere to put a trade that did not happen. The PM's paper-versus-real screen did have somewhere to put them, and it put them in the gain column. The market sold off after lunch, the nine bonds closed 9 bp of price below their 8:10 mids, and the \$40.5mm the desk had failed to buy was \$36,450 cheaper at the close. On Wednesday's numbers the failures paid for 40% of the fills.

"We didn't save anything," Kaz says, reading the screen over Theo's shoulder. "We sold the bonds these were meant to replace, and then we didn't buy the replacements. The book was underweight \$40mm of spread duration on a day the market fell. That's a market position. We just didn't choose it."

So they strip the market out, as §3.3.3 strips it out of a markout. The nine bonds' predicted systematic move from 8:10 to the close, their betas times the index's move, was $-15$ bp of price. They fell only 9. The idiosyncratic part was $+6$ bp: on a down afternoon the nine bonds the desk could not buy *outperformed* their peers. "Which is presumably why nobody wanted to sell them to us," Kaz adds. On Friday, when the retries finally filled, the nine stood 28 bp above their Wednesday 8:10 mids, 11 bp of it market and 17 bp their own.

| Line | Stamps | bp of price | Notional | \$ |
| :-- | :-- | --: | --: | --: |
| Delay | `NEW` → `ROUTED` | 0.7 | \$139.5mm filled | 9,765 |
| Drift while quoting | `ROUTED` → `QUOTED` | 0.5 | \$139.5mm | 6,975 |
| Half-spread | `QUOTED` mid → fill | 5.2 | \$139.5mm | 72,540 |
| **Executed** | | **6.4** | | **89,280** |
| Unfilled, market part, Wednesday close | `NEW` → close | $-15$ | \$40.5mm unfilled | $-60,750$ |
| Unfilled, IDO part, Wednesday close | | $+6$ | \$40.5mm | $+24,300$ |
| Unfilled, market part, Friday retry | `NEW` → retry | $+11$ | \$40.5mm | $+44,550$ |
| Unfilled, IDO part, Friday retry | | $+17$ | \$40.5mm | $+68,850$ |
| **Shortfall at the Friday retry** | | **11.3** | \$180mm target | **202,680** |

By Friday the unfilled line was \$113,400, larger than every executed line put together and 56% of the rebalance's cost. On Wednesday evening the same line had read as a \$36,450 gain. Of the four terms in the table, it is the largest, and it is the only one whose sign changed with the date on which somebody looked. That is not bad luck; it has two causes, and both are structural. The market part of an unfilled order is a beta position that nobody chose and that the desk could have closed in a minute with an index trade, which is what the residual-risk event of §27.4.2 exists to prompt; on this Wednesday the event was logged and nobody acted on it, so a cost line spent two days as a market bet. And the idiosyncratic part is adversely selected. About 30% of MarketAxess inquiries fail (Kargar et al. 2025), and the failures are not a random draw: a purchase fails when no dealer wants to sell, and dealers least want to sell the bonds they expect to rise. The router of §2.5.1 carried a failure cost $\kappa$ of 20 bp as an assumption. This week measured it: 17 bp of idiosyncratic drift, plus 11 bp of beta that a hedge could have neutralised.

> **Math, Gently.** *A telescoping sum, and the paper portfolio.* Picture two portfolios. One is real. The other, drawn as a dotted line, is the portfolio the optimiser imagined: every order filled in full, instantly, at the arrival mid, with no spread. The paper portfolio is the counterfactual of §2B.1 made into a whole book, and the *implementation shortfall* is the gap between the two (Perold 1988). For a filled order the gap is the fill price minus the arrival mid, and it can be walked one stamp at a time, the way the distance from home to office is the sum of home-to-coffee-shop and coffee-shop-to-office. If arrival is 100.00, the mid at `ROUTED` is 100.03, the mid at `QUOTED` is 100.05 and the fill is 100.15, then the purchase cost 15 cents: 3 for waiting (delay), 2 for the market moving while the dealers looked (drift), 10 for crossing the spread (half-spread). The intermediate mids cancel in pairs, which is what *telescoping* means, so the pieces always add up to the whole. For the part that never filled, the paper portfolio owns it and the real one does not, so the gap is whatever the bond did between the decision and the moment the order was retried or abandoned. The full version follows.

#### The Full Derivation

Take one order with side $\eta$ ($+1$ to buy, $-1$ to sell), target face $X$, fills $x_k$ at prices $p_k$ (per 100 of face), and arrival mid $m_{\text{NEW}}$. Let $T$ be the time at which the unfilled remainder is retried or abandoned, with mid $m_T$. The paper portfolio trades $X$ at $m_{\text{NEW}}$; the real one trades $\sum_k x_k$ at the $p_k$; both are marked at $m_T$. Paper P&L is $\eta X (m_T - m_{\text{NEW}})/100$ and real P&L is $\eta \sum_k x_k (m_T - p_k)/100$, so the shortfall, in dollars, is

$$
\text{IS} = \frac{\eta}{100}\sum_k x_k\,(p_k - m_{\text{NEW}}) \;+\; \frac{\eta}{100}\Big(X - \sum_k x_k\Big)(m_T - m_{\text{NEW}}).
$$

The first term is the executed cost; the second is the opportunity cost. The log's stamps split each executed piece by telescoping,

$$
p_k - m_{\text{NEW}} = \underbrace{(m_{\text{ROUTED}} - m_{\text{NEW}})}_{\text{delay}} + \underbrace{(m_{\text{QUOTED}} - m_{\text{ROUTED}})}_{\text{drift while quoting}} + \underbrace{(p_k - m_{\text{QUOTED}})}_{\text{half-spread}},
$$

and the opportunity term splits along §3.3.3's line into a market part and an IDO part, $m_T - m_{\text{NEW}} = \beta_{\text{pred}} + \epsilon$, where $\beta_{\text{pred}}$ is the bond's beta times the index's price move over the same interval and $\epsilon$ is what is left. An order filled in several clips adds one more effect, *impact*: the drift between one clip's `QUOTED` stamp and the next clip's `ROUTED` stamp, which the desk's own earlier clips may have caused. The post-fill markout, the print an hour or a day later, does not enter this order's shortfall at all, because paper and real both own the filled bonds from then on. It belongs to the scorecard (§2B.4) and to the leakage test (§2B.3).

**The patience premium.** Kargar et al. add one more number, and it is the reason retry logic belongs inside the fill service rather than in a trader's memory. A well-connected client buying an odd lot of investment grade takes about two days to complete after a failed inquiry; the least-connected 60% take nearly twice as long. And clients who reject the first quotes go on to trade later about 40% of the time at a price about 10 bp better than the best first offer. Whether patience pays depends on the signal. Count the rejection as worth $0.4 \times 10 = 4$ bp (treating the other 60% as no better, which is our simplification, not the paper's finding). The sleeve's value signal expects about 60 bp of price over three months and decays with a half-life of roughly 45 trading days *(illustrative)*, so two days of waiting cost it about $60 \times (1 - 2^{-2/45}) \approx 1.8$ bp of alpha: patience wins. An event-driven signal worth 40 bp with a three-day half-life loses $40 \times (1 - 2^{-2/3}) \approx 15$ bp in the same two days: patience loses badly. The same retry rule is right for one book and expensive for the other, and the shortfall ledger is where the difference shows up.

*Builds on:* §2B.1 (the stamps), §2.5.1 (the failure cost $\kappa$), §3.3.3 (stripping beta), §27.4.2 (terminal states and residual-risk events), §9.8.3 (buffers: the orders the optimiser chose not to send). *Used in:* §2B.3 (unsent orders as a placebo), §2B.5 (the fill service's retry logic), §2B.7 (the two-leg version), §9.8.2 (what a trade costs), Chapter 28 (the cost budget on the PM dashboard).

## 2B.3 The Leakage Test

*Tuesday 20 October, 10:52 a.m., the morning of Theo's Halvorsen buy in Chapter 2.*

The ticket was the sleeve's: sell \$4mm of a single-B chemicals bond, sent at 10:46 as a disclosed RFQ to five dealers *(the bond, the dealers and every level here are illustrative)*. Four answered. The best bid was half a point under the composite bid, and Theo, who had been on the desk five weeks and had opinions about being lowballed, passed. At 10:52 he closed the inquiry `DONE_AWAY` and gave the order to a voice dealer to work.

At 11:14 a print landed on TRACE: `1MM+`, a dealer selling to a customer, three-eighths of a point *below* the best bid Theo had passed on. By noon his voice dealer had sold his bonds a half-point lower still. Passing had cost about \$20,000.

"Somebody I showed that order to went straight out and dumped their own inventory ahead of me," Theo says. "They knew a seller was coming. I want to know which one, and I want them off the panel."

"Done away?" Kaz looks up. "As in done away with? Which dealer died?"

"None yet," says Theo.

Ines, from across the desk: "The test comes before the accusation. Nobody gets cut on one print."

The test Kaz builds that afternoon is an event study, and the version they end up trusting takes the rest of the week.

> **Math, Gently.** *An event study, and why it needs a sugar pill.* An event study lines up many episodes at the moment something happened, here the `ROUTED` stamp, and averages what the price did afterwards, minute by minute. Sign each path so that a positive number means "moved against us" (down after we tried to sell, up after we tried to buy), and the average path shows how much the market tends to run away once the desk shows its hand. The trap is that the market might have run away anyway. A cold goes away in a week whether or not you take the medicine, which is why drug trials give a control group a sugar pill: the drug's effect is the *difference* between the two groups, not the treated group's recovery. Here the sugar pill is a **placebo order**, one the optimiser generated but nobody sent. If the average sent sale drifts 1.9 bp against the desk in a hundred minutes and the average unsent one drifts 1.4 bp, the inquiry's own effect is about 0.5 bp *(illustrative)*, and the other 1.4 bp is the cold getting better on its own. With 4,600 sent orders, 2,300 placebos and a per-order standard deviation near 10 bp, the uncertainty on that 0.5 is about $\sqrt{10^2/4600 + 10^2/2300} \approx 0.26$ bp. The full version is in §2B.10's engine.

Kaz runs it on a year of the log: every order's composite mid from `ROUTED` to its terminal stamp and on to a hundred minutes later, split by protocol, panel size and outcome. The placebo is the set of orders the optimiser emitted that never left the building, mostly lines the buffer of §9.8.3 suppressed or a trader held back.

The first surprise is that the placebo drifts in the same direction as the real orders, and by most of the same amount. Theo's instinct says that is impossible, since nobody saw the placebo. Kaz's answer is that nobody needed to. The sleeve's signal has momentum in it, and §9.8.2's dealer-seat box makes the point from the other chair: a book that sold a name yesterday will very likely sell it and its cousins today, because the signal that told it to sell is still there and so is every other book running something similar. The sleeve's sales are in bonds that were already falling. Most of the "leak" is the strategy's own footprint, the cold that was going away by itself.

| Slice of the year *(illustrative)* | Sent: drift at +100 min | Placebo | Difference | Std. error |
| :-- | --: | --: | --: | --: |
| All orders | 1.9 | 1.4 | 0.5 | 0.26 |
| Disclosed RFQ, up to 5 dealers | 1.7 | 1.4 | 0.3 | 0.4 |
| Disclosed RFQ, 6 or more | 2.0 | 1.4 | 0.6 | 0.5 |
| All-to-all | 2.2 | 1.4 | 0.8 | 0.4 |
| PT line | 1.5 | 1.4 | 0.1 | 0.6 |
| Voice | 1.6 | 1.4 | 0.2 | 0.6 |
| Outcome `DONE_AWAY` | 2.5 | 1.4 | 1.1 | 0.7 |

*(bp of price, signed so that positive is against the desk.)* The residual is real and small. It is largest when the desk shows a direction to many counterparties and then walks away, which is exactly Theo's Tuesday: a `DONE_AWAY` tells every losing dealer that a seller is still out there. The order of magnitude agrees with the one public study of the question we know of. Tradeweb's white paper on US investment-grade RFQs above \$1mm, January 2025 to April 2026, fits a GLM to five-minute cumulative changes in its Ai-Price spread between RFQ acceptance and TRACE publication, and finds same-direction impact for all-to-all inquiries "in the order of 0.1 to 0.3 basis points" of spread larger than for voice, more for sells and for less liquid bonds (Caretti, Mahajan and Husveth, "Information Leakage in US Credit: Evidence from All-to-All RFQs," May 2026). On a six-year bond, 0.1 to 0.3 bp of spread is roughly 0.6 to 1.8 bp of price, the same neighbourhood as the desk's 0.6 bp all-to-all excess over voice. Two caveats travel with the paper: it is vendor-authored, and protocol choice was not randomised, so the bonds sent all-to-all may differ from the bonds sent by voice in ways the model does not see.

The economics of why a leak exists at all is cleaner than the measurement. Baldauf and Mollner ("Competition and Information Leakage," *Journal of Political Economy* 132(5), 2024) model the trade-off at the heart of every panel: one more dealer means more competition for the order and one more party who, on losing, can trade ahead of it. In their model the client's best response is to reveal no direction, which is why two-sided requests exist.

And Theo's single print had an innocent explanation available all along. Hendershott, Li, Livdan, Schürhoff and Venkataraman ("Quote Competition in Corporate Bonds," *Journal of Finance* 81(4), 2026) find, in dealer runs from 2019–20 matched to TRACE, that the best-quoting dealer wins only about 15% of trades, and that trade-throughs, trades at a worse price than a firm quote under an hour old, run from about 17% for the best-quoting dealer to around 40% for small trades with other dealers. A customer selling to its own relationship dealer three-eighths below the best bid is a trade-through, not a front-run. On the year's numbers, a single high-yield sale's hundred-minute drift has a standard deviation of roughly 40 bp, and the placebo-adjusted expectation for a sent sale is a few basis points. Theo's three-eighths sat a little less than one standard deviation away from nothing at all.

Two more things come out of the week. The placebo itself is selected: a trader who holds back an order usually has a reason, and the reason may be correlated with what the bond does next. Kaz proposes a cleaner sugar pill, a randomly chosen 5% of the optimiser's marginal orders delayed by a day, and Ines approves it on the condition that the delayed orders' opportunity cost goes into §2B.2's ledger, where it belongs, as the price of knowing. And the one-off event study becomes a standing alarm: §27.7.2's CUSUM on markouts is already watching each dealer's residualised fills, and it now watches the sent-minus-placebo drift as well, so a dealer who starts trading on the desk's inquiries trips a threshold instead of a trader's temper.

> **Poker Table.** Ines puts it in a sentence and then in a hand. "Who saw your hand? Everyone you asked, and everyone they told." Every RFQ is a card shown to the table. Showing it to five players buys you five bids and gives four losers a look at what you are holding; showing it to all-to-all gives the look to whoever is watching. Whether that was a good trade depends on how much better the fifth bid was than the second, and that is a question the hand history answers only over thousands of hands. "One print is a tell," she says. "A placebo is a hand history. People get cut on hand histories."

Theo's dealer stayed on the panel. The \$20,000 went into the shortfall ledger as the cost of a `DONE_AWAY`, which is where it had been all along.

*Builds on:* §2B.2 (unsent orders), §3.2 (the RFQ as a poker hand), §9.8.2 (the predictable book), §9.8.3 (buffers). *Used in:* §2B.4 (leakage-adjusted dealer scores), §18.7 (hit rates and staying at the table), §19.8 (the mystery box: adverse selection in baskets), §27.7.2 (CUSUM on markouts as the standing alarm), §27.8 (replay).
