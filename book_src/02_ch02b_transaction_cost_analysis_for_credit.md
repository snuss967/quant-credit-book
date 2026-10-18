# Chapter 2-B: Transaction Cost Analysis for Credit: Arrival, Cover, Shortfall and the Dealer Scorecard

> **Prerequisites.** Chapter 2, in particular §2.3.2 (order statistics and the effective number of dealers), §2.5.1 (the router and its cost of failure $\kappa$), §2.9.1 (LCS units) and §2.9.3 (the April 2025 replay); §3.3 (markouts, IDO markouts and survivorship); §27.4.2 (the order state machine). Nothing else. Every new piece of mathematics is introduced from scratch in a Math, Gently box. The chapter ships `tca.py` through Appendix F.

*What is invented, once for the whole chapter.* The desk, its traders, its fills, its log, its dealer panel (anonymised A to K), its quarterly review, the salesperson who calls afterwards, the vendor report in §2B.9, and every number marked illustrative are fictional composites. So are Dov Adler's pod at Vantress Capital Management, its analyst Wen Zhao and its risk manager Marcus Oyelaran, and the invented issuers Kestrel Roofing and Halvorsen Packaging (Chapter 1-B). The papers, platform statistics, rules, dates and quoted public remarks are real and cited; where a real firm appears, it says only what a cited public document says it said, and none of them walks into a scene.

## Cold Open: Friday, 4:10 p.m., the Markout Meeting

*Friday 23 October 2026, the end of Theo's fifth week. The meeting is in the small conference room because the big one has a client in it, and the small one has a whiteboard nobody has fully erased since August.*

Every Friday at ten past four the desk reads its hand history (§3B.2). The markouts come first, dealer by dealer and signal by signal, and this week they are dull, which is the best thing a markout can be. Then Ines Okafor caps her pen and asks the question she saves for whoever looks most comfortable.

"Theo. What did our trading cost this week?"

Theo has spent five weeks on a systematic desk and six years in restructuring before that, and the restructuring years answer first. "Nothing. Bonds have no commissions. We paid the price, the price is in the P&L, and there's no fee line."

"Cost relative to what?"

He sees the trap a beat too late and recovers the way he once did on creditor calls, with the one number in the system that looks built for the question, a column labelled *cost vs composite*. He reads the week off it: 212 fills, notional-weighted, minus 0.8 basis points of price. "A gain, actually. We beat the composite."

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

By the end of the chapter you will be able to rebuild the four benchmarks from one RFQ log; split a rebalance's shortfall into delay, drift, half-spread and the cost of what did not fill; test a leakage accusation against a placebo; build a dealer scorecard that does not reward fair-weather liquidity; fit cost curves that know their own sample sizes; read your participation in the market net of a moving denominator; and write a pair trade's two-leg cost as one line in a pod's ledger.

## 2B.1 Benchmarks for an RFQ Market

*Monday, before the 7:30 call. Kaz's desk, two chairs, one log.*

Kaz wants to rebuild Friday's three numbers from scratch and Theo wants to know why they disagree, so they start from the one object all three came from: the RFQ log, in which every inquiry the desk has sent walks through the order state machine of §27.4.2. Kaz calls it the desk's diary. Theo, who has read a lot of diaries in data rooms, calls it a docket, because every entry is time-stamped by someone who will later be asked to explain it.

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

Benchmarks, shortfall, scorecards, cost curves and capacity are five readings of this one table, the buy-side mirror of the dealer's log on which Chapter 18-B builds its quoting engine. The desk sees every response to its own inquiry. A dealer sees only its own quote and its own outcome, which Fermanian, Guéant and Pu sort into five bins in their study of European corporate-bond RFQs (FGP 2016, *Market Microstructure and Liquidity* 2(3–4); arXiv:1511.07773): **Done**, **Tied Traded Away**, **Covered**, **Other Traded Away** and **Not Traded**. One inquiry, read from both seats:

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

Each of the fill's numbers conditions on something different. Arrival conditions on the decision alone, so it charges the desk for its own delay; the RFQ-time composite conditions on the market at the door, so it forgives the delay and keeps the dealer's spread; the cover conditions on the desk having won; the print, on the future. A desk asking whether its *router* is good benchmarks against the RFQ-time mid; a desk asking whether its *process* is good, from signal to fill, benchmarks against arrival. Friday's meeting went wrong only because nobody had said which question was on the table.

Two of the four have a defect that is not about conditioning at all. Theo found the first; Kaz found the second.

### 2B.1.2 The composite that reads your mail

Theo's restructuring habit is to read the definitions before the covenants, because "EBITDA" means whatever the definition says it means. So on Monday he read the composite's. MarketAxess's CP+ is an algorithmic price built from trades, quotes and inquiries on its platform, and Jacobsen, Venkataraman and Xu (2025, "Illiquidity Meets Intelligence: AI-Driven Price Discovery in Corporate Bonds," SMU working paper, with data supplied by MarketAxess) show two things about it. The typical bond has no non-retail trade on about 60% of bond-days, so on most days the composite is a model rather than an observation. And requests that did *not* trade carry information the model uses: when a did-not-trade RFQ falls between two trades, CP+'s advantage over the last trade price grows by a factor of 1.4 to 5.0.

"So the number we grade ourselves against," Theo says, "is partly built from our own requests. Including the ones we didn't trade."

"On that platform, in that bond, on a quiet day, yes." Kaz pulls up a bond the desk had been buying in clips all week. Its composite had risen a little after each of the desk's inquiries, including two that expired. "We pushed it up and then beat it. That's not execution, that's homework we marked ourselves."

"Back in my day the composite was Steve," says Mags, passing behind them with coffee. Steve is the dealer who has been punishing her for something since 1997. "At least you knew whose opinion it was."

There is a corporate version of the same worry. ICE agreed on 29 July 2026 to buy MarketAxess for \$167 a share in cash, with closing expected in the first half of 2027 (MarketAxess 8-K, Exhibit 99.1). ICE already sells evaluated bond pricing, so two of the four or so composites a US desk is likely to use may soon share an owner, and averaging them will no longer buy the independence it seems to.

None of this makes the composite useless. For a bond that printed this morning, where the desk is one inquirer among dozens, it is the best neutral price available and the right benchmark for the router. It turns circular for a bond the desk has been working for three days. The repair Kaz and Theo settle on is modest: arrival is stamped at `NEW`, before today's inquiry has touched anything (which removes today's reflexivity, not yesterday's), and each composite's bias against the *subsequent* print is tracked bond by bond, so a composite that leads the desk's own flow is caught as a pattern rather than suspected as a feeling.

### 2B.1.3 The cover is a survivor

Kaz's defect is about Mags's column, and it comes from order statistics rather than from anybody's model. The cover exists only when at least two dealers answered and the desk traded; the winner is the best quote, so the cover is worse by construction. "Cost versus cover" is the distance between the first and second order statistics of the responses (§2.3.2). It measures how spread out the dealers were, its sign is fixed before the trade, and it is computed only on inquiries that survived to a fill: a survivor statistic in the sense of §3.3.5.

The dealer's version is worse. A dealer sees the cover only on the inquiries it won, so every likelihood it can write about its rivals is one-sided: it learns the shape of their quotes from the trades it did, never from the trades it lost. FGP's data also show how thin the table usually is. Only about 40% of the dealers asked actually answer, the chance of answering falls as the panel grows, and clients "often wait for only two answers." Their reservation value sits about 1.7 half-spreads from the composite mid (Bloomberg's CBBT in their data). With two answers, the cover is simply the other answer.

Hendershott and Madhavan's US data tell the same story at larger panels ("Click or Call? Auction versus Search in the Over-the-Counter Market," *Journal of Finance* 70(1), 2015, Table VI). In MarketAxess auctions in 2010–11, with 25 to 28 dealers invited, the response rate ran from 15% for micro trades to 29% for the largest; 8% to 15% of auctions drew no response; the fill rate fell from 73% to 51%; and cost fell from 24–45 bp with few responders to about zero beyond ten. Responses are correlated (the authors say dealers' decisions to bid "are not independent"), and a beta-binomial fit to Table VI (our arithmetic, illustrative) puts the correlation at about 0.06 for micro trades and 0.30 for the largest, so a panel of 26 acts like three to eleven independent dealers: §2.3.2's $n_{\text{eff}} = n/(1 + (n-1)\phi)$, applied to responses rather than quote levels.

"So the cover is fine," Theo says, "as long as nobody calls it a cost."

"The cover is excellent," says Kaz. "It's the best measurement of dispersion we own. It tells you how much the second dealer disagreed with the first. It just can't tell you what you paid."

Mags, who has drifted back to read over their shoulders, has the last word on it. "In 1996 the cover was the number the salesman told you after you'd hung up. 'You were close, we were a sixteenth behind.' Every salesman on the Street was a sixteenth behind for ten years." She considers the screen. "This one at least is written down before anybody hangs up."

By the end of Monday the whiteboard on Kaz's side of the desk holds the table they will use for the rest of the quarter.

| Benchmark | Stamp | Conditions on | Honest when | Misleads when |
| :-- | :-- | :-- | :-- | :-- |
| Arrival mid | `NEW` | the decision | the composite at `NEW` is fresh and owes nothing to the desk's flow | the bond has not printed for days; `NEW` is stamped late |
| RFQ-time composite | `ROUTED` | the market at the door | delay is reported as its own line | the desk's own earlier inquiries moved it |
| Cover $C$ | `QUOTED`, fills only | the second dealer's view | it is read as dispersion | it is read as a cost: it can never be positive |
| Next print | terminal plus minutes | who was right | it is averaged over many trades as a markout | it is read as one trade's cost, or the print is the desk's own |

The table has a fifth row that neither of them writes down yet: the orders that never reached a fill have no benchmark at all, because every column above is measured from a fill price. That row is the subject of the next section.

*Builds on:* §2.2 (TRACE timing, caps), §2.3.2 ($n_{\text{eff}}$), §2.9.1 (units), §3.3.5 (survivorship), §27.4.2 (the state machine). *Used in:* §2B.2–§2B.6, Chapter 18-B (the dealer's log), §27.2.3 (timestamps), Appendix B (the RFQ-log schema).

## 2B.2 Implementation Shortfall, Credit Edition

*Wednesday 21 October, 9:40 a.m. The rebalance §27.4.2 uses as its example, retold from Theo's screen.*

At 8:10 the optimiser emitted the week's rebalance for the desk's systematic sleeve: forty child orders, twenty sales and twenty purchases, about \$90mm each way *(all sizes and prices in this section illustrative)*, each stamped `NEW` at 8:10. The router held them while the morning's new-issue announcements cleared and sent them between 9:15 and 9:35. By 9:40 the sales had gone, easily, as sales do: across every MarketAxess inquiry from 2017 to 2021, Kargar, Lester, Plante and Weill find that sells complete about twice as fast as buys ("Sequential Search for Corporate Bonds," FRB Philadelphia WP 25-08, 2025). Eleven purchases filled. Nine sat with quotes too far away to take, or none, and by eleven o'clock seven were `EXPIRED` and two `DONE_AWAY`: thirty-one of forty. Each of the nine terminal states fired a residual-risk event, and the optimiser put the nine back in the queue as retries for Thursday and Friday.

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

![Figure 2-B.1: The \$2mm fill of §2B.1.1's Math, Gently box as a timeline from `NEW` through `ROUTED`, `QUOTED` and `FILLED` to a TRACE print at +22 minutes and markouts at one hour and one day, with the arrival mid, the RFQ-time mid, the composite offer, the cover and the next print drawn as levels and the fill's cost in basis points against each beside them; beneath it, the rebalance's shortfall from the table above as stacked bars (delay, drift, half-spread, unfilled market part, unfilled IDO part) on Wednesday evening and at the Friday retry. Illustrative: the clock times and the one-hour and one-day mids are assumed.](assets/figures/ch02b_benchmark_ladder.png)

By Friday the unfilled line was \$113,400, larger than every executed line put together and 56% of the rebalance's cost; on Wednesday evening the same line had read as a \$36,450 gain. It is the only term whose sign changed with the date on which somebody looked, and both reasons are structural. The market part of an unfilled order is a beta position nobody chose, which the desk could have closed in a minute with an index trade; that is what §27.4.2's residual-risk event exists to prompt, and on this Wednesday it was logged and not acted on. The idiosyncratic part is adversely selected. About 30% of MarketAxess inquiries fail (Kargar et al. 2025), and not at random: a purchase fails when no dealer wants to sell, and dealers least want to sell the bonds they expect to rise. The router of §2.5.1 carried a failure cost $\kappa$ of 20 bp as an assumption. This week measured it: 17 bp of idiosyncratic drift, plus 11 bp of beta that a hedge could have neutralised.

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

**The patience premium.** Kargar et al. add the number that puts retry logic inside the fill service rather than in a trader's memory. A well-connected client buying an odd lot of investment grade takes about two days to complete after a failed inquiry (the least-connected 60%, nearly twice as long), and clients who reject the first quotes go on to trade later about 40% of the time at a price about 10 bp better than the best first offer. Whether patience pays depends on the signal. Count a rejection as worth $0.4 \times 10 = 4$ bp (treating the other 60% as no better, which is our simplification). The sleeve's value signal expects about 60 bp of price over three months with a half-life of roughly 45 trading days *(illustrative)*, so two days of waiting cost it about $60(1 - 2^{-2/45}) \approx 1.8$ bp, and patience wins. An event-driven signal worth 40 bp with a three-day half-life loses $40(1 - 2^{-2/3}) \approx 15$ bp in the same two days. One retry rule is right for one book and expensive for the other, and the shortfall ledger is where the difference shows.

*Builds on:* §2B.1, §2.5.1 ($\kappa$), §3.3.3 (stripping beta), §9.8.3 (buffers), §27.4.2 (residual-risk events). *Used in:* §2B.3 (placebos), §2B.5 (retry logic), §2B.7 (two legs), §9.8.2, Chapter 28 (the cost budget).

## 2B.3 The Leakage Test

*Tuesday 20 October, 10:52 a.m., the morning of Theo's Halvorsen buy in Chapter 2.*

The ticket was the sleeve's: sell \$4mm of a single-B chemicals bond, sent at 10:46 as a disclosed RFQ to five dealers *(the bond, the dealers and every level here are illustrative)*. Four answered. The best bid was half a point under the composite bid, and Theo, who had been on the desk five weeks and had opinions about being lowballed, passed. At 10:52 he closed the inquiry `DONE_AWAY` and gave the order to a voice dealer to work.

At 11:14 a print landed on TRACE: `1MM+`, a customer selling to a dealer, three-eighths of a point *below* the best bid Theo had passed on. By noon his voice dealer had sold his bonds a half-point lower still. Passing had cost about \$20,000.

"Somebody I showed that order to went out and sold ahead of me, or told someone who did, and every bid on the Street dropped," Theo says. "I want to know which one, and I want them off the panel."

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

*(bp of price, signed so that positive is against the desk.)* The residual is real and small, and largest when the desk shows a direction to many counterparties and then walks away, which is Theo's Tuesday exactly: a `DONE_AWAY` tells every losing dealer that a seller is still out there. The size agrees with the one public study we know of. Tradeweb's white paper on US investment-grade RFQs above \$1mm, January 2025 to April 2026, fits a GLM to five-minute changes in its Ai-Price spread between RFQ acceptance and TRACE publication and finds all-to-all impact "in the order of 0.1 to 0.3 basis points" of spread larger than voice, more for sells and for less liquid bonds (Caretti, Mahajan and Husveth, "Information Leakage in US Credit: Evidence from All-to-All RFQs," May 2026). On a six-year bond that is roughly 0.6 to 1.8 bp of price, the neighbourhood of the desk's 0.6 bp all-to-all excess over voice. The paper is vendor-authored and protocol choice was not randomised, so the bonds sent all-to-all may differ from those sent by voice in ways the model cannot see.

The economics of why a leak exists at all is cleaner than the measurement. Baldauf and Mollner ("Competition and Information Leakage," *Journal of Political Economy* 132(5), 2024) model the trade-off at the heart of every panel: one more dealer means more competition for the order and one more party who, on losing, can trade ahead of it. In their model the client's best response is to reveal no direction, which is why two-sided requests exist.

And Theo's print had an innocent explanation available all along. Matching 2019–20 dealer runs to TRACE, Hendershott, Li, Livdan, Schürhoff and Venkataraman find that the best-quoting dealer wins only about 15% of trades, and that trade-throughs, trades at a worse price than a firm quote under an hour old, run from about 17% to around 40% depending on dealer and size ("Quote Competition in Corporate Bonds," *Journal of Finance* 81(4), 2026). A customer selling to its relationship dealer three-eighths below the best bid on the Street is a trade-through, not a front-run. On the year's numbers a single high-yield sale's hundred-minute drift has a standard deviation of roughly 40 bp, and Theo's three-eighths sat a little less than one standard deviation from nothing at all.

Two more things came out of the week. The placebo is itself selected, since a trader who holds an order back usually has a reason, and the reason may be correlated with what the bond does next; Kaz proposed a cleaner sugar pill, a random 5% of the optimiser's marginal orders delayed by a day, and Ines approved it on condition that their opportunity cost goes into §2B.2's ledger as the price of knowing. And the one-off study became a standing alarm: §27.7.2's CUSUM on markouts now watches each dealer's sent-minus-placebo drift as well, so a dealer who trades on the desk's inquiries trips a threshold instead of a trader's temper.

> **Poker Table.** Ines puts it in a sentence and then in a hand. "Who saw your hand? Everyone you asked, and everyone they told." Every RFQ is a card shown to the table. Showing it to five players buys you five bids and gives four losers a look at what you are holding; showing it to all-to-all gives the look to whoever is watching. Whether that was a good trade depends on how much better the fifth bid was than the second, and that is a question the hand history answers only over thousands of hands. "One print is a tell," she says. "A placebo is a hand history. People get cut on hand histories."

Theo's dealer stayed on the panel. The \$20,000 went into the shortfall ledger as the cost of a `DONE_AWAY`, which is where it had been all along.

*Builds on:* §2B.2, §3.2 (the RFQ as a poker hand), §9.8.2–§9.8.3. *Used in:* §2B.4, §18.7 (hit rates), §19.8 (the mystery box), §27.7.2 (CUSUM on markouts), §27.8 (replay).

## 2B.4 Dealer and Protocol Scorecards

#### Quant-Shop Life: The Quarterly Dealer Review

*A fictional composite of a credit desk's quarterly counterparty review. The routine is drawn from the public research and platform statistics cited; the room, the people, the dealers (A to K) and every number are invented and illustrative.*

The most consequential meeting of the quarter is also the dullest. It happens on a Thursday at two o'clock in a conference room whose screen accepts one laptop in three, and the first eleven minutes go to an adapter. The agenda is one spreadsheet: a row per dealer per protocol per size bucket per regime, eleven dealers by five protocols by four buckets by two regimes, 440 rows, 61% of them resting on fewer than thirty inquiries. Somebody from compliance sits at the end of the table with the best-execution file and asks, twice, whether the methodology changed since last quarter. It did not. The next forty minutes go to whether "time to quote" runs from the desk's `ROUTED` stamp or from the platform's acknowledgement; the two clocks differ by 1.3 seconds because one server's clock had drifted, which is §27.2.3's four timestamps of a fill showing up in a meeting about people. Nobody enjoys this. Everybody agrees it matters, because at the end of the meeting the dealers are sorted into tiers, the tiers set who gets the desk's inquiries next quarter, and the sort is the only decision in the room that moves money.

The columns are the ones the log can supply: response rate; hit rate, the share of a dealer's quotes the desk traded on; cover distance, how far behind the winner a dealer's quote sat when it lost; residualised markouts at one, five and twenty days; no-quote rate on stress days; the dealer's share of the desk's `DONE_AWAY` outcomes; and time to quote. The same columns are computed for the protocols themselves (disclosed RFQ, all-to-all, PT line, voice, session), which turns §2.4's question of which door to use into a measured answer rather than a preference.

Two things went wrong this quarter, and both are worth more than the rest of the spreadsheet.

The first was Dealer C. By hit rate C topped the table: the desk had traded on 41% of C's quotes. By five-day residualised markout C was the worst dealer at the table, at $-4.2$ bp. Theo's first reading was that C was a skilled trader picking the desk off. Kaz's reading was that the comparison itself was broken.

> **Math, Gently.** *A collider: why conditioning on a win tangles things up.* Suppose film studios cast actors who are either very talented or very good-looking, and rarely anyone who is neither. Among *famous* actors, talent and looks will then appear negatively related, even if in the population they are unrelated: knowing that a famous actor is plain tells you he is probably talented, because something got him cast. "Got cast" is a *collider*, an outcome that two independent causes both feed, and conditioning on it manufactures a relationship between the causes. A dealer's quote wins when it is aggressive, and it can be aggressive for two unrelated reasons: the dealer wants the bonds for its inventory, or the dealer knows something the desk does not. Look only at wins and the two are tangled, so a dealer who wins often and a dealer who knows things look like the same dealer. Marín Martínez, Ardanza-Trevijano and Sabio make the dealer-side version precise in a causal graph fitted to 102,437 RFQs on European government bonds ("Causal interventions in bond multi-dealer-to-client platforms," *PLOS ONE* 21(1), 2026): the probability of a hit can be estimated from what the dealer observes, but the revenue on a hit cannot, because the win is a collider. The markout version of the same trap is §3.3.5, and Chapter 18-B meets it from the dealer's chair.

The client's seat has an advantage here that the dealer's lacks: the desk sees every response, not only the winner's. So every quote can be marked, not only the ones traded on. The counterfactual markout of a quote asks what the desk's five-day residualised markout would have been had it traded at that dealer's level, and it exists for C's losing quotes as well as its winning ones. Marked that way, C's average fell to the middle of the table. C quotes aggressively in bonds it wants, and the desk's router happens to send it many of the bonds C wants; the winners looked toxic because the desk only ever looked at winners. The desk's motto acquired a corollary on the whiteboard that afternoon: *IDO or the markout didn't happen*, and the markout that counts is the one on every quote.

The second thing was Dealer K, "the one who never answers." K's response rate for the quarter was 11%, the lowest on the panel, and the default sort put K in tier three. Ines asked for the stress column, empty because the quarter had no stress days, and then for the April 2025 replay of §2.9.3. On 9 April 2025, when MarketAxess's average US high-grade RFQ drew 6.6 prices instead of the usual 13.2 (*AxessPoint*, 14 July 2025), two of the eleven dealers on the desk's high-yield panel were still answering at 10:40. K was one of them. The other was Dealer E. Dealer F, which sat in tier one on calm-day numbers, answered nothing that morning.

![Figure 2-B.2: The dealer scorecard as a heatmap, dealers A to K against response rate, hit rate, cover distance, five-day residualised markout and done-away share, with a separate column for 9 April 2025 in which only two of eleven dealers were still answering the desk's high-yield inquiries at 10:40. Illustrative: the desk's log and its anonymised panel are fictional composites.](assets/figures/ch02b_dealer_scorecard_heatmap.png)

Buy-side traders say the same thing in public, without numbers. At a FILS Europe panel in October 2026, one said that "when it becomes very stressful, you see clearly a concentration to the usual banks," and that electronic liquidity providers and platforms "help more in quiet markets" (The DESK, 15 October 2026). The relationship literature puts a price on that concentration. Jurkatis, Schrimpf, Todorov and Vause find in UK regulatory data that the top 1% of a dealer's relationship clients pay transaction costs 51% below the median client, and that the discount more than doubles in stress ("Relationship discounts in corporate bond trading," BIS Working Paper 1140, 2023). A scorecard built from quiet days rewards fair-weather liquidity: it ranks dealers on the days when the desk's alternatives are plentiful, which are the days the ranking matters least.

The tier decision now weights the stress column at 40%, although stress days are about 4% of the sample: a judgment the desk writes down rather than hides in a default. Small cells are shrunk toward the panel with §3.3.4's empirical Bayes, so a dealer that went 7 for 12 reads as $(7 + 20 \times 0.35)/(12 + 20) \approx 0.44$, not 0.58, when the panel hits 35% of quotes and the prior is worth twenty inquiries. A ranking someone else publishes is a hypothesis to reproduce from the desk's own log. This quarter's example is Citadel Securities' self-reported 14.2% share of US investment-grade block risk transfer, on an unpublished denominator (as reported by The DESK, October 2026), which may be right for the market and still say nothing about this panel. Nor is automation the issue. Trumid reported 88% of eligible RFQ line items executed fully no-touch in September 2025 and Vanguard about 70% of its fixed-income volume automated (The DESK, 8 October 2025 and 14 October 2026), and Vanguard's trader at the FILS panel said the algorithms "stayed there" through April 2025. The machines answer on bad days. The stress column asks whether they answer *you*.

At 4:15, after the meeting, Dealer K's salesperson does not call, because K went up a tier. Dealer F's does. She is friendly, she has been covering the desk for six years, and she would like to understand why her firm dropped to tier two. Ines tells her, in order: F's residualised markouts on the desk's high-yield sales were the worst at the table once every quote was counted, and on 9 April 2025 F did not answer. "We still want to see your axes," Ines says, and means it. When she hangs up she turns to Theo. "Every dealer at that table has a stack. The one who folded on 9 April told you something about theirs."

> **View From Another Seat.** *The dealer desk, scoring us back.* From a dealer's chair the same quarter has a scorecard with this desk as one row among hundreds of clients, and the dealer does to client flow what the desk did to Dealer C: it splits markouts into factor, carry and rolldown, issuer relative value, index and ETF, and residual parts, and calls only the residual toxic. Niang ("Quality-Adjusted Hit-Ratio Targeting in Corporate Bond Market Making," arXiv:2605.30643, 2026; synthetic data, not yet replicated) turns that residual into a weight on each client's flow when a dealer targets its hit ratio, so a client whose sales keep falling after the trade is quoted wider, through the toxicity term $\Lambda_{\text{tox}}$ of Chapter 1's three-term bid; Chapter 18-B builds the engine. Ines sits in both chairs: the scorecard she reads on Thursday mirrors the one her own quoting engine reads every second. The sleeve's momentum footprint from §2B.3 is, on the dealer's sheet, a residual markout against the dealer, and the sleeve pays for it in every quote.

> **View From Another Seat.** *The insurer with one dealer.* A life insurer buying long investment-grade bonds to hold to maturity reads all of this with mild bafflement. Hendershott, Li, Livdan and Schürhoff ("Relationship Trading in Over-the-Counter Markets," *Journal of Finance* 75(2), 2020) find that about one-third of insurers trade with a single dealer, and that execution cost is not monotone in network size: it falls as an insurer adds dealers and rises again once the network passes about twenty. For a buy-and-hold book that trades rarely and in size, a relationship that answers in stress is worth more than a basis point shaved off a quiet Tuesday, and the insurer's scorecard has one row. The systematic desk's eleven rows and the insurer's one are the same trade-off at different trading frequencies.

*Builds on:* §2B.1, §2B.3, §3.3.3–§3.3.5, §2.4 (protocol choice), §2.9.3 (9 April 2025). *Used in:* §2B.8, §18.7, Chapter 18-B (client tiers), §27.7.2.

## 2B.5 Size-Bucketed Cost Curves and the Handoff

The scorecard decides who gets the desk's inquiries. Two other consumers want something narrower from the same log. The optimiser of §9.8 wants a cost function, $c_i(\text{size}, \text{regime})$, in basis points per side; the fill service of §27.4 wants a fill model, $\Pr(\text{fill} \mid \text{size}, \text{protocol}, \text{regime})$. Theo specified both to ROBO on Tuesday in one sentence: *fit the cost curve and the fill curve by size and regime from the RFQ log.*

What ROBO built from that sentence was exact. "Regime" had no definition, so ROBO fit one curve and labelled it `regime = all`. Told on Wednesday that regime meant "stress days, when high-grade bid-ask is above its 90th percentile," it split the sample, fit a square-root curve through each half, and reported that in stress, above \$10mm, impact was *negative*: bigger trades were cheaper per bond. The top stress bucket held four observations. Two were portfolio-trade lines carrying one basket price allocated pro rata, and one was a purchase into a sharp rally that filled below its arrival mid.

"Back in my day the dealers called that a block discount," says Mags. "They were lying too."

| Bucket | Calm: bp per side | Calm: count | Stress: bp per side | Stress: count |
| :-- | --: | --: | --: | --: |
| under \$1mm | 4.1 | 3,812 | 11.2 | 402 |
| \$1–5mm | 6.0 | 2,407 | 17.5 | 188 |
| \$5–10mm | 9.8 | 311 | 26 | 19 |
| \$10mm and up | 14 | 38 | $-3$ (prior: 42) | 4 |

*(Illustrative; half-spread plus impact against arrival, filled orders only.)* The repair has three parts, and each is about what the data can bear rather than about the model. Every point on the curve carries its count, and a bucket below a minimum count reports a prior instead of its own mean, flagged as such. The regime gets a definition the desk can compute at `NEW` and audit afterwards: a bid–ask percentile, a drop in the response count, and the ETF-to-cash volume ratio, the three signals that moved together in March 2020 and April 2025. And the top of the stress curve is a prior, not an estimate: the calm square-root curve of §4.8, scaled by the April 2025 envelope, in which US high-grade bid–ask widened by as much as 231% and the response count halved. Three times 14 bp is the 42 in the table. The two lowest buckets are estimates. The \$5–10mm stress bucket, at 19 orders against a floor of 30, is thin: its 26 bp is a mean shown with its count, to be read as a rough estimate, and `cost_curve` (§2B.10) would swap in the prior there. The top bucket is an opinion with a citation, and the curve says so.

![Figure 2-B.3: Half-spread plus impact against clip size (log scale) with square-root fits for calm 2024 and April 2025 and, dashed, the April 2025 envelope: the calm fit scaled by three, the book's rounding of a widening of up to 231% in US high-grade bid–ask with prices per RFQ halved from 13.2 to 6.6 (MarketAxess, *AxessPoint*, 14 July 2025). Bucket counts are printed on each point; the \$5–10mm stress point (n=19) is flagged as under the floor of 30 that §2B.10 states, and the thin top bucket is greyed and replaced by the prior. Illustrative: the chapter's table, with the envelope's widening and halving from MarketAxess and the fits ours.](assets/figures/ch02b_cost_curves_by_regime.png)

Protocol belongs in the curve, not beside it. Kozora, Mizrach, Peppe, Shachar and Sokobin found that dealer participation on alternative trading systems lowered customer costs by 24 to 32 bp (NY Fed Staff Report 938, 2020), and Hendershott and Madhavan's fill rates fall from 73% for micro trades to 51% for the largest (Table VI). The cost curve and the fill curve are two faces of one decision, because the cheapest protocol for a size is worth nothing at a fill rate of zero. Man's 2023 description of its own pre-trade filter is the buy-side ancestor of the fill service: whether a bond is actually available for RFQ, which participants are worth asking, how often the bond is requested and completed, and whether the size is digestible (the extraction is in §2.5).

> **Math, Gently.** *AUC, or how often the model ranks a fill above a miss.* A fill model outputs a probability for each inquiry. To ask whether it is any good without choosing a cut-off, pick one inquiry that filled and one that did not, at random, and ask whether the model gave the filled one the higher probability. Repeat many times; the share of correct orderings is the **AUC**. A coin scores 0.5 and a clairvoyant 1.0. Ciceri and colleagues report out-of-sample AUCs of about 0.63 for classical models on 1.07 million European corporate-bond RFQ responses (arXiv:2509.17715, 2025), and Marín Martínez et al. report 0.74 on government bonds. So 0.63 is what good looks like in credit. The same paper's 0.97, from quantum-transformed features, is one its own authors call questionable. The full version is §7-B.3 (power and calibration), and §7.7 covers the leaks that produce numbers like 0.97.

On Thursday Hana, the desk's junior quant, brought Kaz a fill model with an AUC of 0.96 and the expression of someone who suspects a gift. Kaz found the gift in eight minutes: one of the features was the number of responses, which the log stamps at `QUOTED`, after the moment the model is supposed to be predicting from. The model was reading the answer key. With the feature restricted to what was known at `ROUTED` the AUC fell to 0.64, which is the number that goes into production and the one the fill service can trust.

*Builds on:* §2B.2, §4.8 (the square-root law), §2.5–§2.5.1 (the router, Man's filter), §27.3 (bitemporal features). *Used in:* §9.8.2, §10.8, §11.9, §27.4 (the fill service), §2B.10.

## 2B.6 Capacity From Your Own Fills: the "We Are the Market" Detector

*Thursday afternoon, the September numbers. They arrive late every month.*

Mags keeps one chart on her second screen that nobody else looks at: for each sleeve, the desk's traded volume in the sleeve's bonds divided by all TRACE volume in the same bonds over the same month. She calls it the mirror. When the ratio gets large, the desk is looking at itself. In September the high-grade value sleeve's ratio jumped from 18.6% to 20.3%, over the 20% line that §4.8's capacity arithmetic had drawn as the point where the square-root law starts to bite *(illustrative)*.

"Back in my day you knew you were the market because the dealer called you by your first name," Mags says. "Nobody's called me Marguerite since August. So either we're not the market, or the dealers have got politer."

The detector the desk built after §4.8 does not fire on the ratio alone. It fires on three things at once: participation above the line, residualised markouts turning against the desk, and response counts falling in the sleeve's bonds. A desk that is really the market sees all three, because it is moving prices, being priced against, and wearing out its welcome. In September only the first moved. Markouts were flat and response counts were up.

The ratio had moved because its denominator had. FINRA's affiliate-principal indicator, approved by the SEC in July 2026, lets a firm flag the inter-affiliate leg of a trade so that TRACE disseminates only the trade with the outside customer; it became available on a voluntary basis on 31 August 2026 and becomes mandatory on 2 August 2027 (FINRA Regulatory Notice 26-16). FINRA's own baseline put such duplicate reports at up to 5.7% of 2025 transactions, counted in trades rather than dollars (SR-FINRA-2026-009), and MarketAxess reported that duplicates had inflated US high-grade TRACE volume by up to 8% in June 2026. September 2026 was the first month with the indicator in use. Tradeweb's September report footnoted that the change "lowered reported U.S. High Grade TRACE volumes" and that prior periods had not been restated. If 8% of the denominator vanishes, every participation ratio rises by $1/(1 - 0.08) - 1 \approx 8.7\%$ of itself, and $18.6\% \times 1.087 \approx 20.2\%$. Nearly all of Mags's jump was the market getting smaller on paper.

> **Math, Gently.** *A ratio with a moving denominator, and a dummy that says so.* A ratio changes when either of its parts changes, and only one of them is about you. If a rule removes duplicate trades from TRACE, the market's reported volume falls overnight and every share of it rises, with nobody trading differently. A **break dummy** is a column of zeros before the date of the change and ones after it. Put it into any regression or trend fitted to the series, and the jump at the break is absorbed by the dummy's coefficient instead of being read as a trend. In September's numbers, the dummy's coefficient comes out near 1.6 points of participation, and the trend underneath it is flat. The full version is Chapter 22, where FINRA's indicator, MarketAxess's decision to stop publishing monthly volumes after July 2026, and Tradeweb's unrestated series all appear as dated breaks.

The detector now carries a dummy at 31 August 2026 and another waiting at 2 August 2027, and the sleeve's capacity estimate is refitted on the dummied series. Mags, who distrusts anything called "adjusted," looks at the refitted chart for some time. "So we're not the market," she says. "We're just a bigger share of a smaller tape." She makes a note on the printout. "Fine." From Mags, *fine* is a standing ovation.

*Builds on:* §4.8 (this section is its measured half), §2B.5. *Used in:* §9.10, Chapter 22 (§22.2, series breaks), §11.9, Chapter 28.

## 2B.7 The Two-Leg Cost of a Pair

*Dov Adler's pod and Vantress Capital Management are fictional composites (Chapter 1-B); Kestrel Roofing and Halvorsen Packaging are invented issuers; every position, price, fee and P&L figure is illustrative. The April opening is a replay from the pod's own records as of April 2026; the borrow statistics and the 2005 events are real and sourced.*

On Thursday 22 October at 7:20 a.m., Marcus Oyelaran, the platform's risk manager, sent Dov a one-line email: *Your Pair Book has a friction column. Where does the transaction-cost number in it come from?* The honest answer was that it came from an assumption. §8D.6's capture ratio charges every pair "two legs of transaction cost," and for PB-01 the pod had been amortising a round number. Dov forwarded the email to Wen Zhao with three words, *make it measured*, and Wen, who keeps the recall history of every borrowed bond as a time series she calls the weather, started where she starts everything, with the oldest record.

PB-01 was opened on a Tuesday in April as one parent order with two children: buy \$60mm Kestrel 6% 2030, and sell \$39mm Halvorsen 7.25% 2029 borrowed through the prime broker. Dov decided at 9:30. The Kestrel block filled by voice at 9:50 at 96.00 against an arrival mid of 95.80: \$120,000. At 10:30 the prime broker called back: the lender that had shown the Halvorsen bonds at 8:30 had lent them elsewhere. Bond loans are recallable on demand, and in the custodian data Asquith, Au, Covert and Pathak studied, 31.2% of loans shrank before they closed ("The market for borrowing corporate bonds," *Journal of Financial Economics* 107(1), 2013). For ninety minutes the pod was outright long \$60mm of a single-B credit nobody had meant to own alone. Wen priced Halvorsen's CDS as the alternative short and Dov declined it: the contract shorts the issuer's deliverables, not these bonds, and swaps a borrow fee for a basis (Chapter 24). At 10:35 Dov bought CDX HY protection as a bridge; at 11:10 Wen found a second lender at 30 bp; at 11:20 the bonds were sold at 90.00, and at 11:25 the bridge came off.

The execution system had scored two clean tickets: Kestrel \$120,000 against its arrival, and Halvorsen \$140,000, 0.36 points against a mid of 90.36 at its own `NEW` stamp of 11:15, when the order was re-entered. That stamp is where the money went missing. The parent's arrival was 9:30, when Halvorsen's mid was 90.45. High yield widened about half a percent in relative terms while the pod waited, and Halvorsen fell with it: 0.09 points on \$39mm, about \$35,000, which is what half a percent is worth on the short leg's 71,600 of DTS. Net of what the bridge earned back after 10:35, the legging line is about \$21,000, and the bridge's two half-spreads on roughly \$51mm of index add \$16,000, booked in another system. Wen's total is about \$297,000 against the execution system's \$260,000, and the difference is the part of the trade that existed only because there were two legs.

> **Math, Gently.** *Legging risk: variance grows with time, its square root more slowly.* While one leg is filled and the other is not, the pair is an outright position, and the risk of an outright position over a short window is the market's volatility scaled to that window. Variances add over time, so the variance over 90 minutes is $90/390$ of a trading day's, and the standard deviation is the square root of that fraction, about 0.48 of a day's. Kestrel's 72,600 of DTS is \$72,600 of P&L per 1% relative move in spreads; if high-yield spreads move about 2.2% in relative terms on a typical day *(illustrative)*, a day's standard deviation on the open leg is about \$160,000 and ninety minutes' is about \$77,000. A bridge hedge removes the part of the risk it is correlated with: with an index bridge correlated 0.8 with the leg, what is left is $\sqrt{1 - 0.8^2} = 0.6$ of it, about \$46,000. Ninety minutes one-legged, bridge or no bridge, was a coin flip worth a sixth to a quarter of a quarter's thesis. The full version, the variance of a partial hedge, is §8.6.

> **The Pair.** *Pair Book PB-01, the 2:40 trim of Tuesday 13 October 2026 (Chapter 1-B), scored as one parent order. Fictional composite; numbers illustrative.* **Thesis.** Unchanged since April: Halvorsen needs its lenders before Kestrel does. **Legs.** Long \$60mm Kestrel; short Halvorsen, cut from \$39mm to \$35mm face by buying back \$4mm on an all-to-all RFQ at 78.75, then CDX HY protection sold to fill the 17,700 of DTS by which the short still outweighed the long (87,900 against 70,200). **What the hedge removes.** High-yield beta, through the DTS ratio plus the index sale. **What idio remains.** Halvorsen's documents and revolver against Kestrel's covenant room, now net of two half-spreads, not one. **What leaks.** Twelve minutes: the CDX sale went through at 2:52, and meanwhile the pair was 17,700 of DTS net short in a market that rallied a quarter of a percent, about \$4,400 (ex ante standard deviation about \$6,800). **What it costs.** Bond leg \$14,000 (0.30 points of half-spread and 0.05 of delay on \$4mm); CDX leg about \$1,900 (half a 1/32-point bid–ask on about \$12.4mm of index); legging \$4,400. Two-leg total about \$20,400, against the \$14,000 the execution report showed, because the CDX leg lives in the futures and swaps system. The standing cost dwarfs all three: borrow at 300 bp on about \$27mm of short market value, about \$820,000 a year or \$3,300 a business day, plus the 7.25% coupon owed. The fee was 50 bp on 6 October, and it is a function of the signal: Asquith et al. measure 173 bp in the thirty days before a bankruptcy filing and 245 bp after, against a mean of 33 bp and a median of 18 bp in ordinary times. The TCA line is the friction row of the morning explain (§8D.6; Chapter 8-C).

![Figure 2-B.4: PB-01's two-leg shortfall as a waterfall, for the April opening (Kestrel leg, Halvorsen leg against its own stamp, legging net of the bridge, the bridge's half-spreads) and for the 2:40 trim (bond leg, CDX leg, twelve minutes of legging), each beside the single-ticket total the execution report showed. Dov Adler's pod, Vantress, Kestrel and Halvorsen are fictional composites; all numbers illustrative.](assets/figures/ch02b_two_leg_shortfall.png)

Wen's arithmetic made one thing plain that the round number had hidden. Opening PB-01 cost about \$297,000; closing it will cost something similar; the thesis was sized at about 100 bp a year, roughly \$1.2mm. A round trip is half a year of thesis before the borrow is counted, so the pair's horizon is a cost decision as much as a view: a pair Dov expects to resolve in six weeks has to be several times as convicted as one he expects to hold for nine months. Figure 2-B.5 shows how fast that multiple falls with the hold.

![Figure 2-B.5: The conviction a pair needs to pay for its round trip, against how long the desk expects to hold it: PB-01's measured two-leg cost (\$297,000 each way) against a thesis worth \$1.2mm a year needs 4.3 times the sized thesis if the pair resolves in six weeks and 0.66 times if it runs nine months, and the cost the execution report showed (\$260,000 each way) would have made the break-even a few weeks too short; borrow is not included. Illustrative: the chapter's numbers.](assets/figures/ch02b_roundtrip_conviction.png)

Minutes are the gentle version of legging; the canonical failure took a day. On 4 May 2005 General Motors' stock rose 18% on Kirk Kerkorian's bid, and on 5 May S&P's downgrade of GM and Ford widened their bonds and CDS. Trades that held GM convertibles against a replicating portfolio "lost money on both legs," the hedge on the first day and the bonds on the second (BIS *Quarterly Review*, June 2005, box on the GM and Ford downgrade). A pair's legs are hedges of each other only while both of them exist and both of them trade.

> **View From Another Seat.** *The platform risk manager.* Marcus sees the April morning through a definition. On his x-ray, a parent order with one filled child older than thirty minutes stops being "a pair being legged" and becomes a position, with its own line on Chapter 8-B's limit sheet and its own phone call *(Vantress's thirty minutes is illustrative)*. He does not ask whether the second leg is coming; he asks what the book is long that it did not mean to be, and at 10:30 that April Tuesday the answer was \$60mm of Kestrel. The pod books legging as an execution cost. The platform books it as a limit breach with an execution explanation, sized by the open leg rather than by the pod's confidence in the other one.

*Builds on:* §2B.2, §8D.2 (the short-leg menu), §8D.6 (the capture ratio), §27.4.2 (one parent, two children), Chapter 1-B (the 2:40 trim). *Used in:* Chapter 8-C (the friction line), §18.6 (jump risk in the quote), Chapter 19, Chapter 24 (the CDS leg's basis), Chapter 28.

## 2B.8 Two Stress Days on the Scorecard: March 2020 and April 2025

*Thursday evening. Kaz replays the TCA engine over two weeks of history, using the replay harness of §27.8.*

March 2020 breaks the engine before it breaks anything else. For much of the second half of that month the composites behind the arrival benchmark were stale, and against them the desk's 2020 sales look catastrophic, a hundred basis points and more below mids nobody could have traded at. The only live price was the ETF's (§2.7; §20.5), and it was a poor ruler too: Todorov puts March 2020 bond-ETF tracking error above 200 bp against an average of 0.7 bp (*BIS Quarterly Review*, March 2021), and US high-grade bid–ask peaked at 44.62 bp (MarketAxess, *AxessPoint*, 14 July 2025). Ines, who ran an investment-grade book at a dealer that month, remembers going from principal to agency, "from a market maker to a phone book." The honest benchmark for those weeks is an ETF-implied price mapped to each bond by duration and beta, with an error band as wide as the tracking error, and the engine's job is to declare the arrival column fiction rather than compute it to two decimals.

April 2025 is the opposite kind of stress: short, deep and measured. §2.9.3 replays 9 April and its 10:40 decision, so the engine adds only what the scorecard saw. MarketAxess's average prices per US high-grade RFQ fell from 13.2 to 6.6 on 9 April and were back to 11.3 within a week. On its count 8 April was a \$55.9bn US high-grade TRACE day, the day after US fixed-income ETFs traded \$98.9bn; Greenwich, citing Trumid, put all US corporates at \$89.7bn that day, 12% through portfolio trades, a different definition over a different universe (Chapter 22 reconciles the record days). MarketAxess later reported that its Tradability model's predicted dealer responses fell roughly 20% market-wide between 2 April and the 8–10 April peak (*AxessPoint*, 23 March 2026), and the algorithms stayed on with wider parameters. The desk's scorecard that quarter scored dealers on the week as a whole, so a dealer who answered generously on Monday and Tuesday and vanished on Wednesday looked average, and the two of eleven still answering at 10:40 on the 9th were invisible in a weekly mean.

Hendershott and Madhavan saw the same shape fifteen years earlier: on their ten worst volatility days, response rates fell to between 12% and 26% depending on size. A handful of days decides the dealer tier, and a scorecard that averages them in with sixty calm days dilutes them out. The repair is the regime weighting of §2B.4, applied by day and not by week.

A third shape strains a quarterly scorecard most. European investment-grade bid–ask rose 88% in seven weeks in early 2026, from a median of 5.82 bp on 8 February to 10.92 bp on 29 March, as energy prices climbed (MarketAxess TraX data, via The DESK, 7 April 2026). Nothing gapped; spreads widened and sizes shrank, and the earlier research we drew on puts normalisation after such episodes at four to fourteen weeks, a range we have not re-verified. A label switched on by a slow grind stays on for a month or more, so a quarter's stress column can hold one long, mild episode instead of three violent days. The desk now records each stress's shape, fast or slow, beside its label.

> **Trend Watch.** *What a buy-side desk can measure about its own trading, 2018–2026.* **Aug 2020:** dealer participation on ATSs is found to lower customer costs by 24–32 bp (NY Fed Staff Report 938). **15 May 2023:** TRACE begins flagging portfolio trades, so PT lines become separable in public data. **9 Apr 2025:** prices per US high-grade RFQ halve, 13.2 to 6.6, and recover to 11.3 within a week (MarketAxess, 14 July 2025). **Sep 2025:** Trumid reports 88% of eligible RFQ line items executed fully no-touch (The DESK, 8 October 2025); an SMU working paper shows MarketAxess's CP+ draws on untraded RFQs (Jacobsen, Venkataraman and Xu). **May 2026:** Tradeweb publishes a leakage study of all-to-all RFQs (0.1–0.3 bp of spread). **29 Jul 2026:** ICE agrees to buy MarketAxess for \$167 a share. **30 Jul 2026:** MarketAxess ends its monthly volume releases. **31 Aug 2026:** FINRA's affiliate-principal indicator goes live on a voluntary basis, mandatory from 2 August 2027. **Oct 2026:** Vanguard reports about 70% of its fixed-income volume automated (The DESK, 14 October 2026). *What it means for the desk:* the desk's own log has become the best cost dataset it can get, while the public denominators and composites it is benchmarked against are consolidating, being restated, or going dark.

*Builds on:* §2.7, §20.5, §2.9.3, §2B.4, §27.8. *Used in:* Chapter 22 (record days), Chapter 28 (the stress playbook), §2B.10.

## 2B.9 When to Apply It, and When It Breaks

On the Monday after the replay a vendor's quarterly TCA report arrived for the desk *(the vendor and its report are fictional)*: forty pages, a cover chart in three shades of green, and a headline saying the desk had saved 1.3 bp against the composite. Theo read it the way he once read an adviser's fairness opinion, from the back. There were no unsent orders anywhere in the appendix, so no placebo, and the report's leakage page could not separate the desk's footprint from anyone's reaction to it. The quarter had no stress days in it, so the dealer rankings described fair weather only. The participation chart spliced across 31 August without a mark. The cover was reported as "price improvement." And the quarter's one hedged trade, a bond sale paired with an index hedge, appeared as a single bond ticket with a respectable cost, the index leg nowhere.

None of that made the report wrong. It made it a report about a different question from the one the desk was asking. TCA works when the log is complete and bitemporal, so that every stamp says what was known when; when the composite is independent of the desk's own flow, or its dependence is tracked; and when the sample contains stress days, so that rankings say something about the days that matter. It breaks on survivor statistics (the cover, winner-only markouts), on moved denominators (affiliate prints, platform series that stop or restate), on reflexive composites, on unfilled orders that never reach the report, and on two-leg trades scored as two one-leg trades. A practitioner who has been burned by each of these reads a TCA number by asking about the placebo first, the stress column second and the denominator third, and only then looks at the headline.

*Builds on:* §2B.1–§2B.8. *Used in:* §3B.7 (how the desk is measured), §26.8 (model risk), Chapter 28.

## 2B.10 The Engine: `tca.py`

### Specification for AI Implementation

*What ROBO built from the vague version.* The first spec Theo wrote for the engine said *minimise cost versus composite*. ROBO did exactly that. It learned that the composite lags in quiet bonds, and its router began holding orders until the composite had gone stale enough to beat, which is precisely when the composite was wrong. The cost column improved for three weeks while the shortfall against arrival worsened every day.

*The problem it solves, at this point in the story.* By the second Friday the desk had done this chapter's work in five notebooks, each with its own idea of a stamp, a sign and a unit. `tca.py` is those notebooks as one module that reads the RFQ log, so the 4:10 meeting starts from the same numbers each week and the argument is about the numbers' meaning rather than their arithmetic.

*What it computes, and why it is built this way.* Every number in this chapter is a difference between two stamps in the log, so the module is organised around the stamps. `benchmarks_bp` scores a fill against each benchmark, cost positive. `shortfall` is Perold's telescoping sum per child order, with the unfilled remainder split into a market part (from a beta move the risk model supplies, §3.3.3) and an IDO part, because one is a hedging failure and the other is adverse selection. `event_study` returns sent and placebo paths and their difference with a standard error at every horizon. `scorecard` marks every quote, shrinks small cells (§3.3.4) and keeps a stress column whose weight is an explicit argument. `cost_curve` reports counts and swaps in a stated prior, such as `sqrt_prior` (§4.8), below a minimum count. `participation` carries break dummies, and `we_are_the_market` fires only on §2B.6's three-way conjunction. `pair_line` adds the legging term and the standing cost to the legs' shortfalls under one parent arrival, and `legging_sd` gives the window's ex ante risk.

*Inputs and outputs.* In: `Order` records (face in \$mm, prices per 100, the composite mid at each stamp, cover, retry mid, beta move); drift matrices in bp of price signed against the desk; per-quote arrays; sizes and costs; volumes with ISO dates; DTS in dollars per 1% relative spread move. Out: dollar costs per term with flags, mean paths with standard errors, a row per dealer, buckets with counts, ratios with dummies, and a pair line.

*When it fits, and when it does not.* It is built for the weekly hand history, the quarterly dealer review and a pod's friction row, all of which average over hundreds of orders. It is the wrong tool for a single trade's post-mortem, where the event study's standard error is larger than any plausible effect (§2B.3), and for weeks like March 2020, where the arrival column is fiction and the engine's flags matter more than its numbers (§2B.8).

*The edge cases that bite.* An order with no composite at `NEW` falls back to the `ROUTED` mid and says so. A PT line's half-spread is an allocation of one basket price, not a quote, and is flagged. A `DONE_AWAY` with a single response has no cover. An unfilled remainder with no retry mid is flagged rather than scored at zero, because zero is the number that hid nine bonds on Wednesday. Affiliate-duplicate prints enter through the participation dummies. The case that bites hardest is the `NEW` stamp itself: an optimiser that stamps orders when the router picks them up, rather than when it decides, quietly deletes the delay term, and every report downstream looks better for it.

*The full python listing is [Listing 2-B.1 in Appendix F](#code-2b-1).*

*Builds on:* §2B.1–§2B.9, §3.3.3–§3.3.4, §4.8, §27.4.2. *Used in:* Appendix F (Listing 2-B.1), Appendix B (the RFQ-log schema), §27.8 (replay), Chapter 18-B (the dealer's mirror log), Chapter 8-C (`pnl_explain.py` reads `pair_line` as the friction row).

## 2B.11 Desk Debrief

The next Friday at 4:10 Ines asks the same question, and this time Theo does not give her a number. He gives her a table with four benchmark columns and a fifth for the orders that did not fill, the market part of that fifth column hedged by Wednesday lunchtime, a leakage line with a placebo and a standard error, and a note that the September participation jump was the denominator. Then he slides a second sheet across. It is thirteen columns wide, one per weekly rebalance for the coming quarter, and each column holds the expected shortfall: executed cost from the bucketed curves, expected unfilled cost from the fill model times the signal's decay, and a stress row priced from the April 2025 envelope. Theo's thirteen-week cash flow model has been reborn once more, this time as a cost budget.

Ines reads it twice, which from Ines is applause. "The first thirteen-week model on this floor that ever predicted anything," she says, and puts it in the PM's monthly forecast.

| Concept | Equation | Intuition (box) | Judgment (scene) | Code |
| :-- | :-- | :-- | :-- | :-- |
| Benchmark as counterfactual | $\eta(p - b)/b \times 10^4$ | Math, Gently: the commuter (§2B.1.1) | Friday's three numbers (Cold Open) | `benchmarks_bp` |
| Implementation shortfall | executed $+$ opportunity, telescoped by stamp | Math, Gently: the paper portfolio (§2B.2) | Wednesday's nine bonds (§2B.2) | `shortfall` |
| Leakage | sent minus placebo drift, with its standard error | Math, Gently: the sugar pill (§2B.3) | Theo's `DONE_AWAY` (§2B.3) | `event_study` |
| Collider, quote-level markouts | condition on the quote, not the win | Math, Gently: famous actors (§2B.4) | Dealers C, K and F (§2B.4) | `scorecard` |
| Cost curve with counts | bucket mean, or a stated prior below $n_{\min}$ | Math, Gently: AUC (§2B.5) | ROBO's negative impact; Hana's 0.96 (§2B.5) | `cost_curve`, `sqrt_prior` |
| Moving denominator | ratio plus break dummies | Math, Gently: the dummy (§2B.6) | Mags's mirror (§2B.6) | `participation`, `we_are_the_market` |
| Two-leg cost | legs $+$ DTS$_{\text{open}} \times$ relative move $+$ standing | Math, Gently: legging risk (§2B.7) | PB-01's opening and trim (§2B.7) | `pair_line`, `legging_sd` |

- **Cost is a choice of counterfactual.** Arrival prices the decision, the RFQ-time composite prices the router, the cover measures dispersion, and the print says who was right; a number without its benchmark is not yet a cost.
- **The unfilled order is usually the largest line**, and the only one whose sign changes with the day you look. Its market part is a hedge nobody placed; its IDO part is adverse selection.
- **A leak is a difference:** sent minus placebo, with a standard error. One print is a tell.
- **Every quote has a markout, not only the winners**, and a scorecard without a stress column rewards fair-weather liquidity. IDO or the markout didn't happen.
- **A cost curve is only as good as its counts.** The top bucket is a prior with a citation.
- **Denominators move.** Participation carries a dummy at 31 August 2026 and another waiting at 2 August 2027.
- **A pair has one arrival.** Two half-spreads, a legging term and a standing cost; scored as two tickets, the legging vanishes.

### The Spec You Hand the Robot

*Vague version:* "minimise cost versus composite." *What ROBO built:* a router that waited for the composite to go stale and then beat it. *The precise version:* "Implement `tca.py` per §2B.10 over §2B.1's RFQ log (face \$mm, prices per 100, bp of price, cost positive). Score fills against arrival, RFQ-time, cover and next print. Split Perold shortfall per child order into delay, drift, half-spread and opportunity, the last into beta and IDO; flag, never zero, an unmarked remainder. Leakage is sent minus placebo, with standard errors by protocol, panel and outcome. Scorecards mark every quote, shrink with a prior of $k$ inquiries and carry a weighted stress column. Cost buckets report counts and use a stated prior below 30. Participation carries break dummies at 2026-08-31 and 2027-08-02. A pair is one parent: legs, legging and standing cost, with the legging window's ex ante standard deviation."

### Exercises

**1. One sale, four benchmarks.** *[benchmarks]* The desk sells \$3mm at 94.10. The arrival mid was 94.30, the RFQ-time mid 94.25, the cover 94.00 and the next print 93.90. What is the cost against each, and which answers "was the router any good?" *Check:* $+21.2$, $+15.9$, $-10.6$, $-21.3$ bp. *Solution.* With $\eta = -1$, the cost is $-(p - b)/b \times 10^4$: $0.20/94.30$, $0.15/94.25$, $-0.10/94.00$, $-0.20/93.90$. The router is judged against the RFQ-time mid; the 5.3 bp between it and arrival is the delay, a process cost.

**2. A shortfall with a hole in it.** *[shortfall]* A \$10mm purchase fills \$6mm at 101.20, with arrival 101.00, `ROUTED` mid 101.05 and `QUOTED` mid 101.08. The remaining \$4mm is abandoned two days later at 101.90, when beta explains $+0.30$ points of the move. Split the shortfall. *Check:* executed \$12,000 (delay \$3,000, drift \$1,800, half-spread \$7,200); unfilled \$36,000 (beta \$12,000, IDO \$24,000); total \$48,000, three-quarters of it unfilled. *Solution.* $6\text{mm} \times 0.05/100$, $\times 0.03/100$, $\times 0.12/100$; $4\text{mm} \times 0.90/100$, split $0.30$ and $0.60$.

**3. Is patience worth it?** *[patience]* Rejecting the first quotes buys a 40% chance of trading two days later about 10 bp better (Kargar et al.). The signal is worth 80 bp with a 20-day half-life. Reject or accept, and at what half-life does the answer flip? *Check:* accept; about 27 days. *Solution.* Two days of decay cost $80(1 - 2^{-2/20}) \approx 5.4$ bp, more than the $0.4 \times 10 = 4$ bp expected saving. Break-even solves $80(1 - 2^{-2/h}) = 4$, so $2^{-2/h} = 0.95$ and $h = 2/\log_2(1/0.95) \approx 27$ days.

**4. A placebo that cannot help.** *[leakage]* Sent sales drift $+2.4$ bp at a hundred minutes ($n = 900$, s.d. 12 bp); placebos drift $+1.9$ ($n = 400$, s.d. 12). Estimate the leak and its $t$-statistic. How many placebos would bring the standard error down to 0.25 bp? *Check:* 0.5 bp, $t \approx 0.7$; none would. *Solution.* $\text{SE} = \sqrt{144/900 + 144/400} = \sqrt{0.52} \approx 0.72$. The sent sample alone contributes $\sqrt{144/900} = 0.40$ bp, so no number of placebos reaches 0.25; the desk needs more sent orders, which is to say more time.

**5. Ninety minutes on one leg.** *[legging]* A pair's long leg, 50,000 of DTS (dollars per 1% relative spread move), fills 45 minutes before the short. Relative spread changes have a daily standard deviation of 2.5%. What is the dollar standard deviation of the legging window, and with a CDX bridge correlated 0.75? *Check:* about \$42,500; about \$28,100. *Solution.* $50{,}000 \times 2.5 \times \sqrt{45/390} \approx 42{,}460$; times $\sqrt{1 - 0.75^2} \approx 0.661$.

**6. The mirror and the moving denominator.** *[participation]* A sleeve's September participation reads 19.0% against a 20% line, and the affiliate indicator is estimated to have removed 6% of the TRACE volume in its bonds. What is the like-for-like participation, and what else would the detector need to see before anyone says "we are the market"? *Check:* about 17.9%. *Solution.* $19.0\% \times 0.94$: the desk's share of the old denominator. The detector also needs residualised markouts turning against the desk and response counts falling (§2B.6); a ratio alone, on a moving denominator, is not evidence.

### Deep-Dive Resource Graph

**Podcasts**

- **Petter Kolm - 23/08/21** (*Risk.net Quantcast*, 25 August 2021). TCA that ignores partial fills "might be off by 20% to 30%": §2B.2's unfilled line. <https://soundcloud.com/user-393208363/petter-kolm-230821>
- **Why the True Price of a Bond Can Still Be Hard To Know** (*Odd Lots*, 5 April 2021). Evaluated prices disagree for thin bonds: §2B.1.2. <https://omny.fm/shows/odd-lots/why-the-true-price-of-a-bond-can-still-be-hard-to>
- **Jeremy Maletz** (*Money Stuff: The Podcast*, 9 October 2026). A market maker on adverse selection: the dealer's seat of §2B.4. <https://omny.fm/shows/money-stuff-the-podcast/jeremy-maletz>
- **How to Succeed at Multi-Strategy Hedge Funds** (*Odd Lots*, 20 May 2024, Giuseppe Paleologo). The x-ray Marcus reads in §2B.7. <https://omny.fm/shows/odd-lots/how-to-succeed-at-multi-strategy-hedge-funds>
- **A Longstanding Fear About The Corporate Debt Market May Finally Be Coming True** (*Odd Lots*, 23 March 2020, Chris White of Viable Markets). Recorded inside the March 2020 meltdown, when dealers stopped warehousing risk and the composites went stale: the setting for the first stress day of §2B.8. <https://omny.fm/shows/odd-lots/a-longstanding-fear-about-the-corporate-debt-marke>
- **What We Learned About Treasuries on the Night of April 8** (*Odd Lots*, 28 April 2025). Who sold and why when the safe-haven trade broke; the rates-market view of the week that §2B.8's second stress day scores for credit. <https://omny.fm/shows/odd-lots/what-we-learned-about-treasuries-on-the-night-of-april-8>
- **Ellen Correia Golay on All-to-All Trading and Treasury Market Liquidity** (*Macro Musings*, 21 September 2026, FRBNY Markets Group). All-to-all trading and principal trading firms in Treasuries, the March 2020 dash for cash included: the rates analogue of the all-to-all column in §2B.3's leakage test. <https://macromusings.libsyn.com/ellen-correia-golay-on>
- **Ralph Smith: Scientific Investing in Fixed Income (S5E7)** (*Flirting with Models*, 11 July 2022, BlueCove). Breadth and liquidity limits in credit, and how a bond's assumed availability can change a backtest: why §2B.5 hands the optimiser a cost curve by size and regime instead of a single number. <https://www.flirtingwithmodels.com/episodes/kAEkSoYuRwd>

**Blog Posts and Talks**

- **Overnight Corporate Bond Trading** (The Microstructure Exchange, Farshid Abdi with Marco Rossi and Botao Wu, 15 September 2026). Trades executed after 6:30 p.m. and before 8:00 a.m. are not disseminated through TRACE until the next morning: a current fact for the post-trade print of §2B.1.1. <https://microstructure.exchange/talks/2026-09-15>
- **Dealer Balance Sheets and Corporate Bond Liquidity Provision** (Liberty Street Economics, Adrian, Boyarchenko and Shachar, FRBNY, 24 May 2017). TRACE matched to dealer balance sheets shows post-crisis regulation reducing bond-level liquidity: the capacity context for reading a dealer's response rate in §2B.4. <https://libertystreeteconomics.newyorkfed.org/2017/05/dealer-balance-sheets-and-corporate-bond-liquidity-provision/>

**Practitioner Writing**

- MarketAxess, *AxessPoint*, "Credit markets showed resilience through April volatility" (14 July 2025). <https://www.marketaxess.com/article/axesspoint-credit-markets-showed-resilience-through-april-volatility>
- MarketAxess, *AxessPoint*, Tradability deep dive (23 March 2026). <https://www.marketaxess.com/article/axesspoint-tradability-deep-dive-insights-powered-by-an-enhanced-liquidity-metric>
- Caretti, Mahajan and Husveth, "Information Leakage in US Credit: Evidence from All-to-All RFQs" (Tradeweb, May 2026); vendor-authored, so read the design first. <https://www.tradeweb.com/49a042/globalassets/newsroom/market-insights/2026/5.13.26-credit-whitepaper/information-leakage-in-us-credit-5.13.26b-final-1.pdf>
- The DESK, "Don't rely on platforms or ELPs in stressed markets, buy-side traders say" (15 October 2026). <https://www.fi-desk.com/dont-rely-on-platforms-or-elps-in-stressed-markets-buyside-traders-say/>
- The DESK, "Citadel Securities reveals glimpse of credit platform broker rankings" (October 2026). <https://www.fi-desk.com/citadel-securities-reveals-glimpse-of-credit-platform-broker-rankings/>

**Academic Papers**

- Perold (1988), "The Implementation Shortfall: Paper versus Reality," *Journal of Portfolio Management* 14(3).
- Fermanian, Guéant and Pu (2016), *Market Microstructure and Liquidity* 2(3–4): outcomes and one-sided likelihoods. <https://arxiv.org/abs/1511.07773>
- Hendershott and Madhavan (2015), "Click or Call?", *Journal of Finance* 70(1): Table VI. <https://faculty.haas.berkeley.edu/hender/Click_Call_OTC.pdf>
- Kargar, Lester, Plante and Weill (2025), "Sequential Search for Corporate Bonds," FRB Philadelphia WP 25-08. <https://www.philadelphiafed.org/-/media/FRBP/Assets/working-papers/2025/wp25-08.pdf>
- Hendershott, Li, Livdan, Schürhoff and Venkataraman (2026), "Quote Competition in Corporate Bonds," *Journal of Finance* 81(4). <https://faculty.haas.berkeley.edu/hender/Quote_Competition.pdf>
- Jacobsen, Venkataraman and Xu (2025), "Illiquidity Meets Intelligence," SMU working paper. <https://microstructure.exchange/papers/JVX_20250904.pdf>
- Baldauf and Mollner (2024), "Competition and Information Leakage," *Journal of Political Economy* 132(5).
- Marín Martínez, Ardanza-Trevijano and Sabio (2026), *PLOS ONE* 21(1): the collider. <https://arxiv.org/abs/2506.18147>
- Jurkatis, Schrimpf, Todorov and Vause (2023), BIS Working Paper 1140. <https://www.bis.org/publ/work1140.htm>
- Hendershott, Li, Livdan and Schürhoff (2020), "Relationship Trading in Over-the-Counter Markets," *Journal of Finance* 75(2). <https://faculty.haas.berkeley.edu/hender/OTCRelations.pdf>
- Ciceri, Cottrell, Freeland et al. (2025), fill probabilities on 1.07 million RFQ responses. <https://arxiv.org/abs/2509.17715>
- Asquith, Au, Covert and Pathak (2013), "The market for borrowing corporate bonds," *Journal of Financial Economics* 107(1). <https://www.nber.org/papers/w16282>
- BIS *Quarterly Review*, June 2005, box on the GM and Ford downgrade. <https://www.bis.org/publications/qr-200506.pdf>

**Data & Code**

- FINRA, SR-FINRA-2026-009 (April 2026): the affiliate-principal baseline. <https://www.finra.org/sites/default/files/2026-04/SR-FINRA-2026-009.pdf>
- Tradeweb, September 2026 monthly data report (6 October 2026): the first month under the indicator. <https://www.tradeweb.com/4a8230/globalassets/newsroom/10.06.26-mar/september-2026-tradeweb-monthly-data-report.pdf>
- FINRA TRACE: <https://www.finra.org/filing-reporting/trace>
- This book: `tca.py` (Listing 2-B.1, Appendix F), which feeds `pnl_explain.py` (Chapter 8-C) and `pair_book.py` (Chapter 8-D) and runs in the replay harness of §27.8.

<!-- STATUS: COMPLETE -->
