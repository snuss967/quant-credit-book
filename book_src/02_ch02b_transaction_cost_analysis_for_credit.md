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
