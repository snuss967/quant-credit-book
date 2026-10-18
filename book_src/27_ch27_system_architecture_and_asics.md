# Chapter 27: System Construction, Low-Latency Infrastructure & ASICs/FPGAs


## 27.0 Cold Open: The Fastest Thing on the Desk

*Fictional desk and cast. The meeting date comes from the Federal Reserve's published 2026 calendar; every price, fill, queue depth and engine statistic in this scene is illustrative.*

Monday, 26 October, 4:15 p.m. The model review is the meeting where numbers go to be believed. Kaz's slot comes after a vendor renewal and before the quarterly reconciliation of the bond-ETF basket, and Kaz uses ninety seconds of it. One slide: the pricing engine that refreshes the desk's streaming quotes, rebuilt over the summer, "forty milliseconds, mean, measured inside the pricing function, down from a hundred and ten." The chair says that is a very good number. Mags asks whether it is adjusted, is told that it is measured, and accepts this the way she accepts most things, provisionally. Theo writes *40 ms* in his notebook and draws a box around it, because at PJT a number the committee liked went in a box. Nobody asks what "inside the function" leaves out, or what the slowest request in a hundred looks like. The p99 is on slide 14 of the appendix. Nobody opens the appendix, because the vendor renewal ran long and the basket reconciliation does not tie.

Wednesday, 28 October, 1:58 p.m., an FOMC day, Theo's sixth week on the desk. He has a streaming bid live on an all-to-all portal: \$3mm of a BBB-rated 10-year industrial bond, priced off a composite, skewed by the desk's inventory model, refreshed by the pricing engine Kaz built. In his other ear, a lender call for a name the desk owns has reached the part where counsel to the Ad Hoc Group says, in unison, that they are "not in a position to comment at this time."

Hana is on the production rota this week. Between stretches of her own work on the risk-data pipeline she watches a second monitor full of numbers that are usually boring, and one of them is the depth of the quote-refresh queue: how many requests for a new price are waiting for Kaz's engine. On a normal afternoon it reads two or three. At 1:59:58 it reads 11. A second later it reads 38. Treasury futures are twitching in the last seconds before the statement, every twitch asks the engine to reprice every exposed quote, and the composite vendor is republishing at the same moment. She types "refresh queue 38 and climbing" into the ops channel. The message is correct, timestamped and read by nobody, because everyone who could act on it is watching the headline ticker.

The statement hits the wires. TY futures drop six 32nds. HYG drops 14 cents. Theo's bid does not move.

He can see half of why. On his left screen the TY contract has already printed lower; on his right the portal still shows his bid at the old level, in green, the colour the portal uses for a price the desk is proud of. Somewhere between the two screens is the queue Hana is watching, and his bid's refresh request is in it, thirty-odd places back, behind requests for bonds nobody is trying to trade. The bid is a promise. The thing that could take the promise back is waiting its turn.

"Your bid," says Ines, not looking up, "is now the best price in the market. That is never a compliment. Who just sold to you?"

The fill arrives before Theo can answer. Three million, done.

"The pricing engine averages forty milliseconds," Kaz offers.

"And the p99?"

Kaz types. Pauses. Types again. "About a second and a half. Under load. Which this is."

"So for a second and a half," Ines says, "you wrote a free put on a BBB bond to everyone in America with a futures screen, and someone with a faster screen exercised it. Nice hand. Terrible table."

She takes an index card from the stack beside her keyboard, the stack she keeps for exactly this, writes on it and slides it across. *Write three things: which component you would have made faster, by how much, and what it would have cost.* "Now, before anybody explains anything. You grade it after you've seen the table." Theo writes *the pricing engine; forty milliseconds down to ten; two more servers and a month of Kaz*, which is what nearly everyone writes. Your own card goes next to his.

Mags, from behind a stack of offering memoranda: "In 1998 the equivalent was leaving your phone off the hook while the Fed spoke. At least the guy who hit you had to dial."

Two seconds later the engine catches up and drops the desk's bid by three-eighths of a point. Theo has bought the bond 3/8 above where his own system now wants to buy it. Against the new mid, the markout is about −0.185 points, roughly \$5,500 on the position *(illustrative; derived in §27.6)*. That is less than an hour of lender-call billing and more than anyone wants to explain at the 4 p.m. risk meeting.

Ines writes the hand on the whiteboard the way she writes every hand she thinks will teach, as a list of times and who could see what. *2:00:00.000 statement. 2:00:00.003 TY prints. 2:00:00.2 our fill. 2:00:02 our engine.* "Four timestamps," she says. "The market needed three milliseconds to know. The seller needed two hundred to act. We needed two thousand to notice. Everyone at this table was faster than us, including counsel on the lender call."

Theo takes the USB stick with his 13-week cash flow model out of his pocket, looks at it, and puts it back. "At PJT the dangerous moment was the lender call."

"Here," says Ines, "it's the second and a half after TY moves and before you do. So: how fast does each part of this desk need to be, how do you prove it, and what's the one thing that has to be faster than everything else?"

ROBO, asked last week to "make the system faster," has opened a ticket requesting an FPGA for the compliance archive.

Two monitors over, Hana watches the refresh queue drain back to three and posts a second message to the channel: "queue normal." That one is also correct, and it is the more dangerous of the two.

The chapter walks the desk from its slowest clock to its fastest, through the feeds, the security master, the order machine, the queue that turned forty milliseconds into a second and a half, the trigger table and the kill switches, and through two days in other people's buildings when a machine or a screen could say yes and nothing could say no. Its short answer to Ines takes eight sections to earn: **the fastest thing on a credit desk should be the thing that says no.**

## 27.1 Two Clocks: Why Credit Latency Is Not Equity Latency

Ines draws two clocks on the whiteboard. One has a minute hand. The other has no hands at all, just a label: "µs."

The **quote clock** ticks in seconds to minutes. An RFQ arrives. The desk identifies the bond, looks up a composite, adds an inventory skew (Chapter 18) and an adverse-selection margin (Chapter 3), and answers inside a venue timer measured in minutes. The public record of what happened, the TRACE print, can arrive up to 15 minutes later with large sizes capped: FINRA confirmed in Regulatory Notice 25-17 (2025-12-04) that it is not moving forward with a one-minute outer limit, so 15 minutes stays (§27.2). Nothing on the quote clock improves when you shave a nanosecond.

The **hedge clock** ticks in microseconds. The instruments a credit desk hedges with trade on exchange matching engines: Treasury futures, HYG and LQD, CDX through its electronic venues, and since June 2024 listed credit index futures. On the London Stock Exchange, the FCA's study of latency-arbitrage races found that races are "extremely fast (the modal race lasts 5-10 millionths of a second)" (Aquilina, Budish and O'Neill 2020, FCA Occasional Paper 50). The moment the desk shows a firm bond price to the street, on an all-to-all venue or a streaming portal, that price becomes a free option written to anyone who sees the hedge clock move first. That is the cold open in one sentence.

Kaz, who has had an hour to recover, argues for the obvious fix. "Then make everything fast. Put the quote model on the FPGA, keep the composite in on-chip memory, load the security master into the network card. If nothing waits, the p99 is the mean."

"Or make nothing fast," says Mags. "I've traded credit since before it had a clock. The RFQ timer is minutes, so answer in minutes. Don't stream. Nobody ever picked off a telephone."

Ines lets them both finish, then writes a price under each name. Under Kaz's: eight figures of hardware to make a minute-long auction a microsecond quicker, a pricing model rewritten in a language that cannot change without a day of re-synthesis, and, at the end of the road, ROBO's FPGA for the compliance archive. Under Mags's: a desk that is never picked off on an FOMC afternoon because it never shows a firm price while TY can move, which means it never shows one on a streaming portal at all, so the flow that wanted a streaming price goes to whoever has one. "You're each right about half of the building," she says, and draws a horizontal line through the middle of the board. "The top half may be slow and clever, and it's the only half allowed to say yes. The bottom half may be fast because it's dumb, and all it's allowed to say is no." What she has drawn is a **two-speed system**:

```text
SLOW PATH  (milliseconds to minutes; rich, auditable; the only path allowed to say "yes")
  venue/TRACE/composite/run feeds -> normaliser -> bitemporal price store (27.2)
      -> security master (27.3) -> fair value -> quote model (inventory skew, Ch 18)
      -> pre-trade risk -> OMS/EMS (27.4) -> venues: RFQ, all-to-all, PT, streaming
      -> trigger-table builder ----- writes rows ----+
                                                     |
FAST PATH  (nanoseconds to microseconds; thin, dumb, provably bounded; may only say "no")
  hedge market data (TY, HYG/LQD, CDX, credit futures) -> compare against rows (27.6)
      -> pull or widen exposed quotes; hard limits; kill switch; cancel-on-disconnect (27.7)
```

The FPGA does not price bonds. It compares numbers that the slow path computed and wrote into a table. The slow path can be clever, slow, and wrong in interesting ways; the fast path must be simple, fast, and wrong only in the safe direction. Kaz asks whether "fast path" is a defined term with a negative pledge. Ines says it should be: nothing else gets to put logic in it. Figure 27.1 draws the two paths side by side.

![Figure 27.1: The slow path computes and may say yes, the fast path only compares and may say no, and the one thing that crosses from the first to the second is the trigger table that the slow path writes. Illustrative: schematic of the two-speed architecture of §27.1.](assets/figures/ch27_two_clocks.png)

> **View From Another Seat.** *The non-bank market maker: the two clocks are the business model.* Citadel Securities has made markets in US investment-grade credit since June 2023, streaming prices through MarketAxess and Tradeweb (The DESK, 19 July 2023). Its head of fixed income distribution, Jordan Cila, told the same publication that credit "lives at the nexus of our fixed income and ETF franchises." A buy-side skeptic in the same article, Antoine Marmoiton of Alken Asset Management, supplied the sentence that explains the model: "No one wants to hold much inventory that is not hedged very well." Virtu came through the same door, more slowly. Its chief executive, Doug Cifu, said on the Q4 2021 call, "We've enhanced and began to be a market maker in fixed income," and on the Q2 2022 call that "It's still very early in fixed income" (as quoted by The DESK, 23 January 2023, which ties the entry to fixed-income ETF volume). Virtu's FY2015 10-K describes the control underneath all of it, one that "automatically freezes the applicable trading strategy, cancels all applicable open orders." Read together, and this is our inference rather than any firm's statement, the non-banks enter credit where their fast clock already lives: ETFs, Treasury futures and index hedges, in bonds whose risk those hedges can carry. For them the split between a slow path that prices and a fast path that refuses is not a design choice. It is the reason they can quote at all, and it is why they quote investment grade long before they quote a single-B bond with a trapdoor in its documents.

### 27.1.1 The price of a microsecond, derived

How fast is fast enough? The answer depends on what you are reacting to, and it can be derived in four lines once one idea is in place.

> **Math, Gently.** *E-folding time, or how fast news goes cold.* Pour a cup of coffee at 80°C in a 20°C room. It does not lose a fixed number of degrees a minute. It cools in proportion to how much hotter than the room it still is: quickly at first, then more and more slowly. One number summarises the whole curve, the e-folding time $T$. After one $T$ the coffee has lost about 63% of its excess heat ($1 - e^{-1} \approx 0.63$), after two about 86%, after three about 95%. Now swap "excess heat" for "the part of a piece of news the rest of the market has not yet priced," and the cooling is the market catching up. The shape has one property that does most of this section's work: at the very start the curve is almost a straight line, so a lag of 1% of $T$ costs about 1% of the edge ($e^{-0.01} \approx 0.990$). A value signal that goes cold over about a quarter has $T \approx 63$ trading days, and 1% of its edge goes in about 0.6 of a day, most of a session, which a nightly batch handles easily. The race the cold open lost has $T$ of about 79 µs, the FCA's mean race length, and 1% of its edge goes in 0.8 µs. Same curve, same 1%: one lag is most of a trading day and the other is under a millionth of a second. In symbols, next.

Let a piece of information arrive at time $0$, and let the exploitable edge from acting on it with reaction lag $\ell$ (seconds) be

$$
\alpha(\ell) = \alpha_0\, e^{-\ell/T},
$$

where $\alpha_0$ is the edge at zero lag and $T$ is the information's e-folding time, the time over which the rest of the market incorporates it. Exponential decay is a first-order assumption; a race is closer to a step function, which only sharpens the conclusion. The value of shaving $\Delta\ell$ off the lag is

$$
\alpha(\ell) - \alpha(\ell + \Delta\ell) = \alpha_0 e^{-\ell/T}\left(1 - e^{-\Delta\ell/T}\right) \approx \alpha(\ell)\,\frac{\Delta\ell}{T}, \qquad \Delta\ell \ll T.
$$

So the **relative value of a latency improvement is $\Delta\ell/T$**. A lag of $0.01\,T$ costs about 1% of the edge. Now push it through the fundamental law (Chapter 9): with $\text{IR} = \text{IC}\cdot\sqrt{\text{BR}}$ and lag scaling the IC by $e^{-\ell/T}$ at fixed breadth,

$$
\text{IR}(\ell) = \text{IR}(0)\, e^{-\ell/T}.
$$

Latency is literally a term in the strategy's information ratio, and its weight is set by $T$, not by how much you enjoy hardware.

| What the desk reacts to | E-folding time $T$ (order of magnitude) | Lag costing 1% of edge | Right technology |
| :--- | :--- | :--- | :--- |
| Value or carry signal (Chapters 9, 11) | about a quarter (~63 trading days) | ~0.6 trading day | nightly batch, a PM, coffee |
| Trend signal (Chapter 10) | one to three months | a few hours | daily batch, disciplined execution |
| Client RFQ | the venue timer, ~minutes | ~1 second | auto-responder plus composite |
| Portfolio-trade inquiry (Chapter 19) | ~90 seconds | ~1 second | parallel pricing, bounded fan-out |
| Hedge-instrument jump while your quote is live | race length, 5–80 µs (OP50: mode 5–10 µs, mean 79 µs) | sub-microsecond | FPGA or gateway trigger |

*(Rows one to four are illustrative magnitudes; row five uses the OP50 race statistics quoted in §27.6.)*

Theo reads the table the way he used to read a capitalisation table, top to bottom, saying each row aloud. "Value signal: a day late costs nothing worth a server. Trend: a day late costs" (Kaz supplies $1 - e^{-1/60} \approx 1.7\%$ of the information ratio) "which is real money, and it buys a careful execution process, not hardware. The same book gains nothing from a microsecond. RFQ and portfolio trades: a second starts to matter." He reaches the last row and stops. "This one says the lag that costs one percent is under a microsecond. Mine was a second and a half."

"Then the loss is $1 - e^{-1.5/(79\times 10^{-6})}$," says Kaz, and types it. "My calculator says 1."

"One desk," says Ines, "nine orders of magnitude, and a single budget meeting in which all of them are called 'latency.'" Figure 27.2 plots the decay behind four of the table's rows.

![Figure 27.2: Share of the edge left after a reaction lag, exp(−lag/T): a 1.5-second lag costs the RFQ book about 1.5% of its edge, the value and trend signals nothing, and the hedge-jump trade all of it, and the dots mark the lag that costs 1%. Illustrative: the decay model α(ℓ) = α0·exp(−ℓ/T) of §27.1.1 with the table's T values (42 trading days for trend is the midpoint of one to three months; the hedge-jump T is the 79 µs mean race length of Aquilina, Budish and O'Neill 2020).](assets/figures/ch27_edge_decay.png)

The table also explains the cold open without any microstructure jargon. Theo's half-spread bought him protection against *diffusion*, the slow drift of fair value during his quote's life, and none against a *jump*, a discrete public move that every participant sees at once. Against diffusion, a wider quote buys time. Against a jump, only being first helps, and being second is the same as being last. §27.6 makes both statements exact.

Now grade the card. Theo wrote *the pricing engine, forty milliseconds down to ten*, and so do most readers. Make the engine four times faster and the queue shrinks with it, because the same flow now keeps it busy less than a fifth of the time; by §27.5's arithmetic the p99 falls from a second and a half to roughly a tenth of a second. Against the last row of the table that is still $e^{-0.1/(79\times 10^{-6})}$ of the edge kept, which is zero to any precision anyone will ever report. Two servers and a month of Kaz buy nothing against a jump. What would have helped is not a faster yes but a faster no: a component that prices nothing, compares TY's move with a number written down in advance, and pulls the bid within microseconds. It costs a network card with an FPGA on it and a table the slow path keeps filled, and §27.6 builds both. A card that said "pull the quote when TY moves" gets full marks, provided it also said what puts the quote back.

> **[SOURCE EXTRACTION]** *Man_Revolutions_in_Credit_Trading_2023 p.2:* "the biggest barriers to systematic approaches breaking through in credit have traditionally been execution and the ability to model transaction costs and liquidity within decades-old manual processes"
>
> **Annotation.** Our analysis: Man locates the bottleneck in the plumbing, not the alpha, and this chapter takes that literally. The three things the sentence names (execution, transaction-cost modelling, liquidity) are, respectively, the OMS/EMS and order state machine (§27.4), the cost model fed by provenance-typed prices (§27.2), and the fill-probability and streaming-eligibility services (§27.4, §27.6). On a 2026 desk the barrier has moved. Electronic execution exists, and the hard part is making the automated quote clock *safe*: knowing which prices are real, which quotes are exposed, and what stops the machine. A strategy that cannot be executed is a research note. A strategy that can be executed but not stopped is the opening paragraph of an SEC order (§27.7).

> **[SOURCE EXTRACTION]** *Blackstone_Systematic_Credit p.2:* "The proliferation of electronic bond trading, higher-quality pricing data, and improved computational power is allowing Blackstone to apply the same sophisticated..."
>
> **Annotation.** Our analysis: the sentence (cut where our source map cuts it) names the three inputs this chapter builds in order: the feed (electronic trading), the price store (pricing data), and compute. Note the order of dependence. Compute is the cheapest of the three and the one engineers most like to buy; pricing-data quality is the one that silently decides whether the backtest is real (§27.2–27.3, where Bohn and Stein warn about fitting "someone else's model"). The modern desk departs from the brochure in one respect: "sophisticated" is not a property of the model but of the whole pipeline, and the weakest link is usually a timestamp.

Man and Blackstone wrote about the plumbing as the barrier. In the years since, the quote clock itself was handed to machines, and the machines that answer RFQs turned out to have a fast-market problem of their own.

> **Trend Watch. The robots took the RFQ, then called in sick (2020–2026).** *What changed:* the quote clock itself was automated. Tradeweb says AiEX now handles a large and rising share of its institutional trades *(share not independently verified; Tradeweb 10-K, FY2025)*. Trumid executed 88% of eligible RFQ line items fully no-touch in September 2025 (The DESK, 2025-10-08). In October 2026 Vanguard reported about 70% of its traded volume automated, up from about 40%, while noting it sends nothing without a trader (The DESK, October 2026). *The stress test:* in a Coalition Greenwich survey of 51 corporate bond investors in Q4 2023, "improved auto-quoting" topped the buy side's wishlist for dealers. The same post recalls that in March 2020 "several of the largest banks famously shut down their auto-quoters" because their pricing algorithms could not cope with the volatility, a lesson that later let them handle bouts of volatility (Kevin McPartland, Coalition Greenwich, 2024-02-13). In October 2026, buy-side traders told FILS Europe that electronic liquidity providers "help mainly in normal markets." *What it means for the desk:* the auto-responder is a slow FPGA with better excuses. Its parameter file is a trigger table and its "stress mode" is a kill switch with a reputation. Both belong under the same governance as the fast path in §27.6–27.7, with explicit triggers, owners and audit trails, not a trader's intuition about when the market "feels weird." The full adoption series is in §18.7.

## 27.2 Ingestion: Feeds, Normalisation, and the Provenance Problem

Theo's first instinct, inherited from RSSG, is to ask where a number came from before asking what it is. On a restructuring the question is "is that the sponsor's EBITDA or ours?" On a desk it is "is that a print, a firm quote, a dealer run, or somebody's model?" The feed handler is the receptionist of the building: every price that enters must say who it is, where it came from, and when, or it does not get a badge.

### 27.2.1 The feed zoo

| Feed class | Typical transport *(general knowledge)* | Clock | Firm? | Characteristic failure |
| :--- | :--- | :--- | :--- | :--- |
| Venue RFQ and streaming (MarketAxess, Tradeweb, Trumid, Bloomberg) | FIX 4.4/5.0 sessions over TCP | milliseconds | Firm under venue rules, for the stated size and time | session drops, sequence gaps, resend duplicates |
| TRACE | FINRA or vendor feed | up to 15 minutes after the trade | Traded, historical | late; sizes capped (\$5mm IG, \$1mm HY); affiliate duplicates |
| Composites (CP+, Ai-Price, BVAL, ICE) | vendor APIs | seconds to minutes | Evaluated | you are fitting someone else's model |
| Dealer runs | chat and email, parsed (Chapter 25) | minutes | Not firm | stale by construction, optimistic by incentive |
| ETF quotes and iNAV | exchange feeds | milliseconds (quote), periodic (iNAV) | Firm (quote) / evaluated (iNAV) | iNAV built from evaluated bond prices |
| Futures (CME, Cboe) | UDP multicast market data (e.g., CME MDP 3.0) | microseconds | Firm | packet gaps and recovery; venue halts (§27.5) |

The column that matters is "Firm?" Every row produces a number that looks like a price, and only some of them are.

**Quant-Shop Life (fictional composite): three rows before 7:30.** *A systematic credit asset manager, not the desk, on a Tuesday in October. The firm, the engineer and every number are invented; the failures are the ordinary kind.* Ilse's day starts at 6:05 a.m. with an email whose subject line she has learned to dread for its brevity: `DQ gate: FAIL (3)`. The nightly data-quality gate runs every price record that arrived since yesterday's close through a set of checks before the 7:30 signal run is allowed to read it. Three rows have failed. The run will not start until she clears them or quarantines them, and the portfolio manager will notice at 7:31.

Row one is the easy one. A vendor's evaluated price for a single-B bond reads 9.81 against 98.10 yesterday. The bond did not lose 90% of its value overnight; somebody's decimal moved. The gate catches it with its dullest check, a move larger than anything the bond's DTS and the day's index change could produce. With a spread duration of 4 and a high-yield index that widened 6 bp, a plausible move is a few tenths of a point, and this one is 88 points. She quarantines the row and opens a vendor ticket, and the model reads yesterday's evaluated price with a staleness flag.

Row two is the TRACE line of the table above, in miniature. Two prints in a BBB bond: same price, same \$2mm, opposite sides, 0.4 seconds apart, neither carrying an affiliate flag. The firm's turnover feature, which feeds its liquidity score, would count \$4mm of volume where perhaps one economic trade of \$2mm happened. Whether it was one trade reported twice by two affiliates of the same dealer or a genuine round trip, the tape cannot say. She marks the second print as an inferred pair, deletes nothing, and leaves the decision to the feature builder.

Row three takes an hour. An evaluated mark on a high-yield bond has not changed for nine sessions. Nine identical marks are not an error in themselves, since plenty of bonds sleep, but this one printed on TRACE twice last week, three-quarters of a point apart. A bond that trades while its mark does not move is a bond nobody is evaluating. She checks the vendor's coverage list, finds that the bond moved from one evaluator's sector to another's in a vendor reorganisation, and cannot tell whether the frozen value is the old evaluator's last word or a placeholder. She cannot classify it, so the runbook decides: the row enters the run as a feature, with its staleness counter at nine and a weight that decays with it, and never as a label. She files DATA-3107, *stale evaluated mark on a printing bond, cause unknown*.

The signal run starts at 7:28. Nobody downstairs knows there were three rows. At 7:40 the portfolio manager's message arrives, in full: "Anything I should know?" She types "No," deletes it, and types "Three rows. Two fixed, one filed." A data-quality gate earns its keep on the mornings when that is the whole answer.

> **[SOURCE EXTRACTION]** *Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.19:* "Corporate bond bid/ask prices are indicated by dealer runs that are not firm and actionable and therefore market participants often find that trades that appear profitable in practice are unprofitable once transaction costs are factored in."
>
> **Annotation.** Our analysis: this is the provenance problem stated as a P&L problem. A backtest that fills at run prices is filling at a price nobody promised. The architectural fix is not to throw runs away: runs are useful signals of dealer axes and inventory, and Chapter 25 parses them for exactly that. The fix is to type them. A run is an `INDICATIVE_RUN` and can inform a model as a feature; it cannot be used as a fill price or as a label for a cost model without an explicit waiver. The modern desk departs from 2022 only in volume: auto-quoters now generate firm responses at a scale that makes the firm/indicative boundary a database constraint rather than a trader's judgment.

### 27.2.2 The provenance rule

Every price record that enters the store carries, at minimum, an instrument key (an internal surrogate, §27.3), a value with its `price_type` (price, spread or yield; quoting conventions differ by venue and sector), a side, a size, a `price_kind` from the enum {`TRADED`, `FIRM_QUOTE`, `INDICATIVE_RUN`, `EVALUATED`, `COMPOSITE`}, a source, and **two timestamps**: `event_time` (when the venue says it happened) and `known_at` (when the desk committed it to the store and strategies could see it). The second timestamp is the one backtests must use, and it is the one most vendor files do not have.

> **[SOURCE EXTRACTION]** *Bohn_Stein_Active_Credit_Portfolio_Management p.334:* "Essentially, unwary modelers may inadvertently end up fitting someone else's model. ... Many supposedly profitable trading strategies end up being the result of an inadvertent fitting of a matrix model as reflected in matrix prices reported by a data vendor."
>
> **Annotation.** Our analysis: evaluated prices are smooth because they are model outputs, and a strategy that "predicts" them is predicting the vendor's interpolation, which is easy and worthless. The 2026 version of the trap is subtler, because composites such as CP+ and Ai-Price are now machine-learned and update intraday. A signal trained on composite changes can learn the composite's update rule. Hence the rule of this chapter: `EVALUATED` and `COMPOSITE` prices may be features, but labels, fills and cost-model targets come only from `TRADED` and `FIRM_QUOTE` records. When ICE agreed on 2026-07-29 to buy MarketAxess, "which composite priced this quote, at what staleness" became a provenance field rather than a footnote, because two of the market's composite and venue layers now share an owner.

### 27.2.3 Clocks, and the four timestamps of a fill

A fill on a credit desk has four natural timestamps: the venue's `event_time`; `received_at`, stamped by the network card in hardware; `known_at`, when the record is durable in the store; and the strategy's decision time. Measured latency is a difference of two of them, and its error is the sum of the two clocks' uncertainties. The regulatory floor is generous. FINRA Rule 4590 requires computer clocks to be synchronised to within one second of the NIST clock in general, and within 50 milliseconds for clocks recording events in NMS securities and OTC equities. TRACE events fall under the general one-second tolerance. A desk running Precision Time Protocol with hardware timestamping is three to six orders of magnitude finer than anything a regulator asks for, and that gap is where markout analysis lives. Two rules follow. Durations within one machine come from a monotonic clock, never from wall-clock subtraction, because wall clocks get stepped. Durations across machines carry an error bar, and a negative latency is a clock fault to alarm on, not a rounding curiosity.

> **Math, Gently.** *A watermark is the time the mail bag closes.* Picture a sorting office that closes each outgoing bag at a fixed time after the hour. Letters posted in that hour mostly reach the sorter within a few minutes, a few dawdle, and one or two turn up very late. Close the bag too early and many letters miss it; wait for every last letter and the bag never leaves. So the sorter's real decision is a quantile: how long after the hour until, say, 999 letters in 1,000 have arrived? The curve that answers it is the distribution of delays, written $G$: $G(L)$ is the share of letters, here prints, whose delay is at most $L$. If 99.9% of the TRACE prints in your feed arrive within 11 minutes of the trade, then $G(11\text{ min}) = 0.999$, and a watermark of 11 minutes closes each bucket with one print in a thousand still outside. That print is not lost. It goes to a correction stream instead of quietly reopening a bag that has already left. Close at 5½ minutes instead and, if 2% of prints arrive later than that *(illustrative)*, twenty in a thousand take the correction route. The whole trade-off is one curve read at one point, and the next paragraph says it in symbols.

**Late data.** Records arrive late: TRACE by design, vendors by habit. Let lateness $X = \text{known\_at} - \text{event\_time}$ have distribution function $G$. A streaming job that closes each time bucket at watermark lag $L$ loses fraction $1 - G(L)$ of records to lateness. Choose $L$ at a high quantile of $G$ (say the 99.9th percentile of the last 20 sessions). Records later than the watermark go to a **correction stream** that writes new knowledge-time rows (§27.3) and never mutates the bucket that strategies already consumed. Overwriting yesterday's bucket with a late print is how a desk discovers that its backtest knew things its traders did not.

### Specification for AI Implementation

**What ROBO built from the vague version.** Asked to "clean up TRACE duplicates," ROBO deleted every print with the same price and size as another print that day. Half of a block's legitimate partial fills vanished, and a liquidity score dropped 30% overnight. The spec below marks, never deletes; requires opposite sides and a time window; prefers the affiliate flag when it exists; and tags the regime so that features can be split at the flag dates.

**Schema (`price_record`).** `instrument_key: str` (surrogate, §27.3) · `price: float` (per 100 face if `price_type="PRICE"`, bp if `"SPREAD"`, decimal if `"YIELD"`) · `price_type: {"PRICE","SPREAD","YIELD"}` · `side: {"B","S","M"}` · `size_mm: float` (par, USD millions; TRACE-capped values flagged) · `kind: PriceKind` · `source: str` · `event_ns: int` · `known_ns: int` (both ns since epoch, PTP-disciplined) · `affiliate_flag: Optional[bool]` (None before the indicator existed). **Edge cases:** negative latency beyond the clock-error bound raises; capped sizes are never treated as exact; `EVALUATED`/`COMPOSITE` records cannot enter a training-label set.

Ilse's row two needed a policy at 6:20 in the morning, and a policy has to exist before the morning does. Everything in the provenance rule so far is a promise about what a number is allowed to mean, and promises written in a spec get broken by the first engineer who is late for the open. The desk wants three of them to be impossible rather than discouraged: a dealer run cannot become a fill price, a negative latency cannot be quietly averaged into a mean, and a TRACE duplicate cannot be silently deleted along with the legitimate partial fills that resemble it. So the rules go into code at the door of the store, where every price either gets its badge or does not get in.

Listing 27.1 is that door. `PriceKind` is the five-way enum from §27.2.2, and `PriceRecord` is a frozen dataclass carrying the schema above, so a record cannot be edited after it is stamped. `TRAINABLE` holds two kinds, `TRADED` and `FIRM_QUOTE`, and `training_labels` is a filter against it: evaluated prices, composites and dealer runs may be features but never labels, simulated fills or cost targets. `latency_ms` turns `known_ns - event_ns` into milliseconds and raises if the answer is more negative than the clock-error bound the caller supplies. The bound is an argument, not a default, because the desk has to say how good its clocks are. A small negative number inside the bound is returned as it is, not clipped to zero.

`dedupe_trace` takes a table of prints and returns it with three new columns, `dup`, `dup_reason` and `regime`, and with no row removed. It sorts by instrument and event time, marks a print as a duplicate leg when `affiliate_flag` is true, and otherwise looks forward within `window_s` (one second by default) for an unflagged print with the same price, the same size and the opposite side. That later leg is marked `inferred_pair`, and each print is matched at most once. `trace_regime` stamps each print `no_flag`, `flag_voluntary` or `flag_mandatory` around the August 2026 and August 2027 dates, so volume features can be split where the reporting changed. The sanity block feeds in seven prints and expects exactly one pair: a 2mm and a 1mm print at the same price do not match, and neither do two prints five seconds apart.

It runs at ingest, before any liquidity or turnover feature is built, and its output is a proposal. The inferred pair is where it can be wrong, and Ilse's row two is the reason: a genuine customer round trip at the same price and size inside a second looks identical to an affiliate's double report, so rule 2 will sometimes mark a real print. Because it only marks, the cost is a decision for the feature builder rather than lost history. Count how many rows rule 2 touches in each regime before trusting a volume series that spans August 2027.

*The full listing is [Listing 27.1 in Appendix F](#code-27-1).*

Ilse's two \$2mm prints are a small instance of a large and dated problem: the public tape stopped getting faster, and for a while it got dirtier.

> **Trend Watch. The tape got later and dirtier (2022–2027).** *What changed:* the public tape's speed and cleanliness stopped improving. A proposal to cut the TRACE reporting outer limit from 15 minutes to one minute was floated in 2022 and approved in 2024, then shelved: FINRA Regulatory Notice 25-17 (2025-12-04) says FINRA is "not moving forward" with the one-minute limit, and 15 minutes remains. The same notice made aggregate allocation reporting optional from 2026-06-08, with dissemination caps of \$5mm for IG and \$1mm for HY. *How big:* duplicate affiliate trade reports inflated US high-grade TRACE volume by up to 8% in June 2026 (MarketAxess volume release). The SEC approved extending the TRACE affiliate-principal indicator on 2026-07-24; use is voluntary from 2026-08-31 and mandatory from 2027-08-02 (FINRA Notice 26-16). *What it means for the desk:* volume-based features (liquidity scores, turnover, Chapter 21's loan analogues) need a dedupe stage and a **regime tag**, because the same economic activity reports as different volumes before and after August 2027. And the desk's own fills, timestamped by its own hardware, are the only sub-second truth it will ever have about credit. Store them as if they were the most valuable dataset in the building, because they are.

## 27.3 The Security Master Is the Credit Agreement of the System

Theo spent six years reading credit agreements for the one clause that reprices everything. On his third Tuesday on the desk, he finds it in a database. The desk's security master is keyed on CUSIP, has one row per bond, and overwrites that row when a field changes. "So when a company does an uptier," he asks, "where does the old loan go?"

"It stays," says Kaz. "We update the ranking."

"And the backtest from before the uptier?"

Kaz is quiet for a while, then opens the research archive. Last spring someone on the desk backtested Chapter 13's priming-risk screen over 2016 to 2022, on this master. Theo scrolls to June 2020 expecting to see the strategy holding Serta Simmons's first-lien term loan into the uptier, the way Mags's bank book did. It holds none. It never held any. From the day the loan entered the universe in 2016, the screen flagged it as sitting behind super-priority debt, and the strategy stayed away for four years while everyone else was paid a coupon.

"It's prescient," Theo says.

"It's a good backtest," says Kaz.

"It's a good database. The row was overwritten on 22 June 2020 and the backtest reads today's row on every date. The strategy didn't predict the uptier. It read the answer key." He scrolls up to the equity curve, which is smoother through June 2020 than anything Mags remembers about that June.

Every liability-management transaction, exchange offer and reorganisation creates new instruments, new rankings and new issuer–guarantor maps (Chapters 13–16). A security master that cannot represent "this loan was first lien until 22 June 2020 and something else afterwards, and we learned that at 6 p.m." will either lie about the present or lie about the past. Both lies end up in the P&L, one in live trading and one in the backtest that justified it.

### 27.3.1 What the master holds

Theo goes to the whiteboard and draws what he would have drawn at PJT on page four of a lender presentation, the capital-structure slide, and then spoils it by adding dates to every line. At the top he puts the **issuer**, with its LEI, and under it the **obligor group**: the borrower, the guarantors, the restricted and unrestricted subsidiaries. At PJT this was a list. Here each box gets an arrow to its parent with a date on the arrow, because the list changes, and the date it changed is the whole story. "A dated graph," he says, "not a list."

Hanging off the boxes go the **instruments**. Kaz wants to label each with its CUSIP. Theo labels each with a key the desk mints itself and never reuses, an **internal surrogate key**, and writes the CUSIP, ISIN and FIGI underneath in smaller letters, as attributes rather than names. He draws one bond three times, a 144A tranche, its Reg S twin and the registered exchange notes that will follow, and puts a bracket round them: three identifiers on one economic line, kept separate for settlement and TRACE and joined for risk. Under each instrument go its **terms**, coupon, maturity, call schedule, ranking, lien and the covenant flags the Chapter 25 parser extracts.

Last he draws a column down the right-hand side and heads it **events**: exchange, uptier, drop-down, distressed exchange, reorganisation, change of control. Each is a row in an event log with an effective date, a source document, and the instruments it creates, retires or re-ranks. He draws an arrow from a guarantor box to an unrestricted subsidiary and writes "drop-down" on it.

Kaz studies the arrow. "Is a drop-down the thing in the order ticket where you pick the venue?"

"It's the thing where the IP moves to an unrestricted subsidiary and your recovery moves with it."

### 27.3.2 The bitemporal model, derived

> **Math, Gently.** *Two time axes, or the newspaper archive and the wiki.* A wiki keeps one version of each page, the latest. If a company's page said "first lien" on Sunday and was edited on Monday evening to "behind super-priority debt," the wiki now says the second thing, and if you ask it what was true on Sunday it can only tell you what it believes *now* about Sunday. A newspaper archive works differently. It keeps every edition with its date. Sunday's front page still says "first lien," even though Monday's paper changed the picture, and you can pull Sunday's edition to see what a reader knew on Sunday morning. A bitemporal store keeps both kinds of date on every fact: *valid time*, when the fact was true in the world, and *knowledge time*, when the desk believed it. Serta in two lines: the 2016 loan ranked `first_lien_pari` until Monday 22 June 2020 and `first_lien_behind_super_priority` from then on, and the desk learned of the change at 6 p.m. that Monday *(illustrative time)*. Ask "what was the ranking on 23 June, as known at midnight at the start of 22 June?" and the archive answers `first_lien_pari`, because at midnight nobody on the desk had read Monday's paper. Ask "what was it on 23 June, as known today?" and it answers `first_lien_behind_super_priority`. A wiki can only ever give the second answer. A backtest needs the first. The two rules that keep the archive honest, and the short proof that it never rewrites a past edition, come next.

In symbols, a **fact** is a tuple

$$
f = \big(k,\ a,\ v,\ [t^{v}_{0}, t^{v}_{1}),\ [t^{k}_{0}, t^{k}_{1})\big),
$$

where $k$ is the instrument key, $a$ an attribute (ranking, coupon, guarantor set), $v$ its value, $[t^{v}_{0}, t^{v}_{1})$ the **valid-time** interval over which the fact was true in the world, and $[t^{k}_{0}, t^{k}_{1})$ the **knowledge-time** interval over which the desk believed it. An open interval ends at $+\infty$. (Superscripts $v$ and $k$ label the two time axes; they are not powers, and this $k$ is unrelated to the order-arrival parameter $k$ of Chapter 18.) The **as-of query** is

$$
Q(k, a;\ t^{v}, t^{k}) = \big\{\, v \;:\; f \in \mathcal{S},\ t^{v}_{0} \le t^{v} < t^{v}_{1},\ t^{k}_{0} \le t^{k} < t^{k}_{1} \,\big\},
$$

and the whole difference between the archive and the wiki is which $t^{k}$ you pass it.

#### The Full Derivation

The store $\mathcal{S}$ satisfies two invariants.

**(I1) Exclusion.** For each $(k,a)$, no two facts overlap in both intervals, so $|Q| \le 1$. In Postgres this is an exclusion constraint on the pair of ranges. In code it is an assert.

**(I2) Append-only knowledge.** A write at wall time $c$ may only (i) insert facts with $t^{k}_{0} = c$, and (ii) change an open $t^{k}_{1} = +\infty$ to $c$. No value, no valid-time bound and no closed knowledge bound is ever edited.

**Theorem (the past is immutable).** For any $t^{k} < c$, the snapshot $\{f : t^{k}_{0} \le t^{k} < t^{k}_{1}\}$ is the same whether computed before or after a write at time $c$.

*Proof.* An inserted fact has $t^{k}_{0} = c > t^{k}$, so it is excluded from the snapshot. A closed fact moves from $[t^{k}_{0}, \infty)$ to $[t^{k}_{0}, c)$, and since $t^{k} < c$, membership of $t^{k}$ is unchanged. No other operation exists under (I2). $\blacksquare$

**Corollary (no data-layer look-ahead).** Let the desk's information set at decision time $t$ be $\mathcal{F}_t$, the knowledge-time-$t$ snapshot. Any feature computed only from $Q(\cdot\,;\ t^{v} \le t,\ t^{k} = t)$ is $\mathcal{F}_t$-measurable, and by the theorem it gives the same answer in every future rerun of the backtest. The common bug is the other query, $Q(\cdot\,;\ t^{v} = t,\ t^{k} = \text{now})$, "what was true on date $t$, as we know it today." It silently imports every restatement, rating correction, re-ranking and late print learned after $t$. Vendor files labelled "point-in-time" are often point-in-*valid*-time only, which is the second query wearing the first one's name tag.

> **[SOURCE EXTRACTION]** *Ben_Dor_Quantitative_Credit_Portfolio_Management p.102 (note 10):* "This approach prevents 'look-ahead' bias. Following Ben Dor, Dynkin, and Hyman (2005b) spread changes are normalized by the larger of the spread level or 20 bps."
>
> **Annotation.** Our analysis: the note sits under a research design choice, which is where look-ahead is usually discussed. The bitemporal corollary says the same discipline must hold one layer down, in the data store, because a research design that is careful about timing can still read from a table that is not. The desk departs from the research convention in one way. Ben Dor's normalisation floor (20 bp) is a modelling choice made once; knowledge time is a property of every row, recorded at write time and impossible to reconstruct later. If the master did not store `known_at` in 2020, no amount of 2026 cleverness recovers it, and every backtest over that window carries an unquantified look-ahead term.

> **[SOURCE EXTRACTION]** *Bohn_Stein_Active_Credit_Portfolio_Management p.334:* "It is important to determine collaboratively with the data vendor which data are actual prices, which are matrix or evaluated, and which are quotes, which deserve special mention."
>
> **Annotation.** Our analysis: the `price_kind` enum of §27.2 is a lesson from the 2000s, not the 2020s, and Bohn and Stein make it a negotiation with the vendor rather than an inference by the desk. That is still right. The modern extension is to ask the vendor for knowledge time as well as kind: when did this evaluated price become available to subscribers, and was it ever revised? A vendor that cannot answer is selling valid-time data, and the master should flag every row from it as `known_at = unknown` rather than inventing a timestamp.

### 27.3.3 Case Study: Serta Simmons, 22 June 2020, as a sequence of master-table rows

The facts, from our LMT dossier (Proskauer, 2025-01-02): on 2020-06-22, Serta Simmons Bedding closed a transaction with a majority group of its lenders. Participating lenders provided \$200mm of new-money first-out super-priority debt and exchanged about \$1.2bn of their first- and second-lien term loans into about \$875mm of second-out super-priority debt. (That \$875mm is all the second-out issued, to first- and second-lien participants alike; the \$734mm the bankruptcy court used on remand in 2026 is consistent with the first-lien participants' share, and §5.6.2 reconciles the two.) Non-participating lenders stayed in the original 2016 facilities, which now ranked behind both new tranches. The transaction relied on the credit agreement's "open market purchase" language. On 2024-12-31 the Fifth Circuit held that it was not an open market purchase (Chapter 13 has the litigation). The most expensive three words in finance have now also become a row in a database.

Here is what a bitemporal master holds after the desk's event feed confirms the closing at 6 p.m. on the day *(the 6 p.m. knowledge time and the 2016 onboarding date are illustrative; instrument keys are internal surrogates, never invented CUSIPs)*:

| Key | Attribute | Value | Valid from | Valid to | Known from | Known to |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| INS-SERTA-TL1-2016 | ranking | first_lien_pari | 2016-11-01 | ∞ | 2016-11-01 | 2020-06-22 18:00 |
| INS-SERTA-TL1-2016 | ranking | first_lien_pari | 2016-11-01 | 2020-06-22 | 2020-06-22 18:00 | ∞ |
| INS-SERTA-TL1-2016 | ranking | first_lien_behind_super_priority | 2020-06-22 | ∞ | 2020-06-22 18:00 | ∞ |
| INS-SERTA-FO-2020 | ranking | super_priority_first_out | 2020-06-22 | ∞ | 2020-06-22 18:00 | ∞ |
| INS-SERTA-SO-2020 | ranking | super_priority_second_out | 2020-06-22 | ∞ | 2020-06-22 18:00 | ∞ |

Row one is never deleted. It is closed in knowledge time, which is how the database says "we used to believe this was permanent." Now ask the three questions a desk actually asks:

1. *Live risk on 2020-06-23:* $Q(\text{TL1}, \text{ranking};\ 2020\text{-}06\text{-}23,\ \text{now})$ returns `first_lien_behind_super_priority`. The recovery model (Chapter 14) reprices the left-behind loan.
2. *A backtest decision at midnight on 2020-06-22:* $Q(\text{TL1};\ 2020\text{-}06\text{-}23,\ 2020\text{-}06\text{-}22\ 00{:}00)$ returns `first_lien_pari`, because the desk did not yet know. The second-out tranche does not exist in that snapshot at all.
3. *A historical study of 2019 rankings, run today:* $Q(\text{TL1};\ 2019\text{-}06\text{-}01,\ \text{now})$ returns `first_lien_pari`, which is true then and known now.

A CUSIP-keyed, overwrite-in-place master gets question 2 wrong. It reports the post-exchange ranking for a decision made before anyone knew of it, so a backtest of an "avoid priming risk" strategy (Chapter 13's PRS) looks prescient by construction, which is what Theo found in the archive. Figure 27.3 shows where each of the three questions lands on the two time axes. The Ad Hoc Group, represented by counsel, would like it noted that they also knew before the desk did. That is what a Rule 2019 statement is for. Hertz's 2021 emergence gives the mirror image: new post-reorganisation equity and warrants whose economic predecessor is a claim, not a security. Chapter 16 handles the valuation; the master handles the lineage, as an event row linking predecessor and successor keys.

*Fictional cast; Mags's position is the one Chapters 1 and 5 describe, and the report details are invented.* Mags has been listening with the expression she uses for vendor presentations. "Fifteen million of that first lien sat on my bank's loan book that June," she says. "Which of your three questions did my P&L report ask that week?"

Theo thinks about it the way he would think about a covenant, by asking what the report was for. The Tuesday mark was live risk, question 1, and it was right: the loan was behind super-priority debt and priced like it. The trouble was the explain, the column that says why Tuesday's number differs from Monday's. "If the bank's master was overwritten on Monday night," he says, "then when the explain reran Monday it saw the new ranking on Monday too. Same ranking both days. So the whole drop gets called market."

"It did," says Mags. "The report said the loan had been second-class since 2016 and the market had finally noticed. I sold half at about twenty the following January, and when the committee asked why, nobody could find a report from May that showed it as a first lien, because by then the report from May said otherwise too." She taps the table. "Live risk asks your first question. Anything that judges a decision asks the second: the backtest, the explain, the post-mortem on my sale. The third is for historians. If someone can't tell me which question a report asks, it's the wiki."

![Figure 27.3: The Serta rows on the two time axes: the ranking the desk believed at midnight on 22 June 2020 (query 2) is not the one it knows today (query 1), while a 2019 study run today (query 3) still correctly sees first_lien_pari. Illustrative: the rows of §27.3.3 (Serta facts from Proskauer, 2025-01-02; the 6 p.m. knowledge time and the 2016 onboarding date are assumed, and the axes are not to scale).](assets/figures/ch27_bitemporal_serta.png)

### Specification for AI Implementation (bitemporal master)

**What ROBO built from the vague version.** Asked for "a security master with history," ROBO added an `updated_at` column and overwrote rows. It had history in the sense that a shredder has history. The spec: two time axes, append-only knowledge, an exclusion check, and three tests that encode the Serta questions above.

The three Serta questions are the test a security master has to pass, and they are unforgiving in one particular way: each asks a different pair of dates, and a table with one date column can answer at most one of them. The desk could read the definition of bitemporality, nod, and end up with an `updated_at` column, which is how most desks get there. Or it could make the store physically unable to rewrite what it once believed, and then put Theo's Tuesday question to it. Listing 27.2 does the second.

`BitemporalMaster` keeps a list of rows with seven fields: instrument key, attribute, value, a valid interval and a knowledge interval, where an open interval ends at `OPEN`, the largest timestamp pandas allows. Its one write method, `assert_fact`, refuses an empty valid interval and refuses any `known_at` earlier than the previous write, so the knowledge axis only moves forward. It then finds every currently believed row for the same key and attribute whose valid interval overlaps the new one. Each is closed by setting its `known_to` to the write time, the parts of its valid interval that the new fact does not cover are re-inserted as fresh rows, and the new fact is appended. The only edit ever made to an existing row is closing an open `known_to`. That is invariant (I2) of §27.3.2, and it is why the past is immutable.

`as_of` answers $Q$: given a key, an attribute, a valid date and a knowledge date, it returns the one matching value, `None` if there is none, and raises if there are two. `snapshot` returns the whole table as it stood at one knowledge time. `check_exclusion` scans pairs of rows for the same key and attribute that overlap on both axes, which is invariant (I1). The sanity block loads the Serta rows, with the closing known at 6 p.m. on 2020-06-22 *(illustrative)*, and asserts the answers: the post-exchange ranking for live risk, `first_lien_pari` for a decision at midnight, and a second-out tranche that does not yet exist. It then adds a litigation fact in 2025, checks that the 2020 snapshot is unchanged, and checks that writing into the past of the knowledge axis raises.

It belongs under anything a backtest or a live risk run reads that can later be restated: rankings, coupons, guarantor sets, ratings. It is not production storage. The scans are linear, and a real master puts the same two invariants into Postgres range-exclusion constraints. The trap is `known_at`, which defaults to `None`. Pandas turns that into `NaT`, every comparison against `NaT` is false, the monotonic guard goes quiet, and the row gets a knowledge time that no query will ever match. Always pass it, and stamp a migrated legacy table with the migration date, not with a date you wish you had recorded.

*The full listing is [Listing 27.2 in Appendix F](#code-27-2).*

The surrogate key in Theo's drawing was not a matter of taste. Since 2022 the identifier most masters are keyed on has been a licensed asset in litigation.

> **Trend Watch. Identifiers become contested infrastructure (2022–2026).** *What changed:* the identifier your master is keyed on turned out to be a licensed, litigated asset. In March 2022, Dinosaur Financial Group, Hildene Capital Management and Swiss Life Investment Management sued CUSIP Global Services, S&P Global, FactSet and the American Bankers Association (*Dinosaur Financial Group LLC et al. v. S&P Global Inc. et al.*, S.D.N.Y. No. 1:22-cv-01860). The court dismissed most claims but let a Sherman Act §2 monopolisation claim proceed, and a later ruling certified a class of end-user firms and data vendors (ruling dates: see the docket). *The regulatory crack:* in Release No. 34-95148 (adopted 2022-06-23), the SEC let Form 13F filers report a FIGI for each security, optional and in addition to, not instead of, the CUSIP, with the amended form effective 2023-01-03. OpenFIGI distributes its symbology "under the MIT Open Source license at no cost and as a public good." In a 2024 SEC comment letter (file S7-2024-05), the plaintiffs' counsel backed requiring FIGI in regulatory filings. *What it means for the desk:* key the master on an internal surrogate and treat CUSIP, ISIN and FIGI as crosswalk attributes with their own valid-time history. Switching or adding an identifier scheme then becomes a data migration, not a rewrite of every join in the building.

## 27.4 Pricing, Risk, OMS/EMS, and the Order State Machine

Theo's RSSG instinct about waterfalls turns out to be the right instinct about orders. In a waterfall every dollar ends in a bucket, and "unallocated" is a bucket, not a rounding error. In an order management system every unit of target exposure ends in a state, and "unfilled" is a state with risk attached.

> **[SOURCE EXTRACTION]** *Man_Revolutions_in_Credit_Trading_2023 p.4:* "Two of the key challenges for such systematic techniques are having a high certainty of execution and having a relatively good sense of the likely transaction costs"
>
> **Annotation.** Our analysis: read this as two service-level agreements the architecture owes the strategy. *Certainty of execution* is the fill-probability service plus an order state machine that reports partial and failed fills back to the optimiser in time to matter. *A good sense of transaction costs* is the cost model plus the provenance rule of §27.2, without which the cost model is trained on runs and composites. A modern desk adds a third SLA the 2023 text does not need to state: *bounded exposure*, meaning that no firm quote stays live longer than the trigger table allows (§27.6).

### 27.4.1 The reference architecture

Man's own process description (Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.7) is a usable reference design, which we redraw with the desk's components:

```text
PM / signal research (slow clock: days)
  -> portfolio optimiser with TC model and fill-probability inputs
  -> central trading desk (humans + auto-execution rules)
  -> OMS: orders, allocations, compliance, state machine        <- risk engine (positions, DTS, limits)
  -> EMS / venue gateways: RFQ, all-to-all, portfolio trade, principal, agency, streaming
  -> fills, rejects, expiries, done-aways  ->  back to OMS, risk, optimiser, markout store
```

> **[SOURCE EXTRACTION]** *Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.7:* "whereas you can model the concept of probability of fill in quant equity strategies with fairly simple heuristics for fill rates, the concept is decidedly far more challenging in credit given the time varying nature of liquidity and a fairly large illiquid tail."
>
> **Annotation.** Our analysis: this is why the fill-probability service is a first-class component rather than a constant in the optimiser. It must be conditional on bond (liquidity score, Chapter 18's win curve), size, venue, protocol and *regime*, because "time varying" means the March 2020 fill curve is a different function, not the same function with noise. The modern departure is the data: a desk's own RFQ log (who was asked, who answered, at what level, how far from cover) is now rich enough to fit this service directly, and it is the one dataset nobody can sell you.

### 27.4.2 The order state machine

| State | Entered when | Leaves to | Risk consequence |
| :--- | :--- | :--- | :--- |
| `NEW` | optimiser emits a child order | `ROUTED`, `REJECTED` | none yet; reserved against limits |
| `ROUTED` | EMS sends RFQ or order to venue(s) | `QUOTED`, `EXPIRED`, `REJECTED` | information leakage clock starts |
| `QUOTED` | at least one dealer response is live | `FILLED`, `PARTIAL`, `DONE_AWAY`, `EXPIRED`, `CANCELLED` | the client side holds a short-dated option on the responses |
| `PARTIAL` | some size executed | `FILLED`, `EXPIRED_PARTIAL`, `CANCELLED` | residual exposure is now *unhedged intent* |
| terminal: `FILLED`, `EXPIRED`, `EXPIRED_PARTIAL`, `DONE_AWAY`, `REJECTED`, `CANCELLED` | as named | none | every non-`FILLED` terminal emits a residual-risk event |

Two rules make this table safe. First, every transition is an event with `known_at`, written to the same bitemporal store as prices, so the optimiser's view of "what we own and what we tried to own" is reproducible in replay (§27.8). Second, a terminal state other than `FILLED` is not a quiet failure. It is a **risk event** that updates the risk engine's expected position and re-invokes the optimiser, because the portfolio it just optimised no longer exists.

> **[SOURCE EXTRACTION]** *Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.19:* "when probability of fill is not 100%, and portfolio optimisers choose certain bonds, the solution the optimiser comes up with is no longer really optimal if that bond is not available for purchase. In addition, unfilled orders can lead to unintended and potentially unmodelled risk exposures."
>
> **Annotation.** Our analysis: the second sentence is the architectural one. If a 40-bond rebalance fills 31 bonds, the book holds the sells of the nine that failed and none of their replacements. That position nobody chose, typically short spread duration in exactly the names that were hardest to buy. The fix is a closed loop: residual-risk events re-enter the optimiser within one quote-clock cycle, with the failed bonds' fill probabilities marked down. The departure from 2022 is portfolio trading (Chapter 19), where the whole basket fills or fails at once and the residual risk is binary, which makes the loop easier to write and the failure larger.

A pair trade makes that residual-risk event concrete, because a pair is two orders that are only safe together.

> **The Pair.** *Pair Book PB-01, Dov Adler's pod at Vantress (fictional composite from Chapter 1-B; Kestrel and Halvorsen are invented issuers, and every size and date inside the pod is illustrative).* Long \$60mm Kestrel Roofing 6% 2030, short \$39mm Halvorsen Packaging 7.25% 2029 in bonds borrowed through the prime broker, matched on market-value DTS at inception, with the residual high-yield beta soaked up by CDX HY. **What the hedge removes:** the housing cycle and the high-yield market's move, which both legs share. **What remains:** Halvorsen's own news, its 2027 revolver and its documents, against Kestrel's covenant room. **What leaks:** DTS drift as the short's view pays (Figure 1-B.2), the CDX series roll basis (Chapter 10-B), and this chapter's leak, *the roll as a bitemporal bug*. In roll week (Chapters 1-B and 8-C) Dov's OMS believed the book held the new CDX series from Friday at 3 p.m., while the FCM's record said Monday: one hedge, two valid-time intervals, two knowledge times, and an unexplained line on Monday's morning explain. The fourteen-month-old ticket *auto-sync roll dates between OMS and FCM* is an (I2) problem with a Jira number, two stores that are each append-only on their own and that disagree about when the world changed. **In the state machine:** the pair is one parent order with two children. If the Kestrel buy reaches `FILLED` and the Halvorsen borrow-and-sell reaches `EXPIRED`, the parent is `PARTIAL` and its residual-risk event is an outright long of \$60mm Kestrel, a market position Dov never chose. A kill switch scoped to a child leg therefore manufactures beta. Its scope has to be the parent, and a trip that cannot cancel both legs either cancels neither (an atomic cancel) or hedges the survivor with CDX inside one quote-clock cycle. **What it costs to carry and to short:** two half-spreads on the way in, the Halvorsen borrow (Chapter 22's fee ladder, 50 bp rising to 300 bp when the short gets crowded), and CDX roll friction twice a year.

**FIX for bonds, the fields that bite** *(general knowledge; confirm against each venue's rules of engagement)*. *The incident is fictional and its cost illustrative.* The desk learned which fields bite on a Thursday last spring, before Theo arrived. A client inquiry came in on a venue that quotes investment grade on spread, and the desk's response carried "105," meant as 105 bp over the 10-year. The message builder set `PriceType` (tag 423) to 1, percentage of par, instead of 6, spread, so on a bond trading near 95 the desk was bidding 105 points, a 10-point gift. The client took it inside a second, as clients do. Hana found it eleven minutes later, not from an alert but from the markout line on her screen, where one fill sat ten points below every other fill like a typo in a column of figures. The trade was \$1mm, and the desk ate about \$100,000 and an uncomfortable phone call. A fat finger made by a parser. The gateway now checks the fields as a set rather than one at a time. `SecurityIDSource` (tag 22) says which identifier `SecurityID` (48) is, so every message translates surrogate keys through the crosswalk of §27.3. `SecurityType` (167) = `CORP`. `PriceType` (423) distinguishes percentage of par (1), spread (6) and yield (9), and a spread quote also needs its benchmark (`BenchmarkSecurityID`, 699), so a spread that arrives without one is refused. `SettlDate` (64) has to reflect T+1 for US corporates since May 2024 (Chapter 22). And the price collar described next, set against the composite and against the desk's own last fill, would have caught "105" on its own, ten points from both.

**Pre-trade checks live in the gateway.** The first tier of the kill-switch hierarchy (§27.7) sits here, before any message leaves the building. SEC Rule 15c3-5 (Release No. 34-63241, 2010-11-03) requires controls "reasonably designed to prevent the entry of orders that exceed appropriate pre-set credit or capital thresholds, or that appear to be erroneous," and requires that they be "under the direct and exclusive control of the broker or dealer with market access." In credit terms: price collars against composite *and* against the desk's own last fill, notional and DV01 caps per order and per minute, a `PriceType` sanity check (a "price" below 10 or above 200 is probably a spread), and a duplicate-order detector. Mags notes that in 1997 the pre-trade check was a senior trader saying "you want to do *what*?" loud enough for the floor to hear. It had excellent recall and terrible uptime.

**The OMS box has three jobs besides state.** The diagram says "orders, allocations, compliance," and the words weigh more than the collars above. *(General knowledge and the fictional composite of §3.6.3; each firm's compliance manual and venue rules govern.)*

*Compliance: the restricted list is the check that matters.* A price collar protects the desk from its typos; the restricted list protects it from its knowledge. When the desk has been brought over the wall (§3.6.3), or holds a private-side loan position and so receives the borrower's non-public information, the issuer goes on the list, and the pre-trade check blocks every order and RFQ response in that issuer's securities. The flag lives on the issuer and obligor group of §27.3.1, not on the CUSIP, because a restriction earned through a term loan covers every line of the borrower's debt, and a check keyed to one identifier fails open on the siblings. It is bitemporal, so replay (§27.8) can show what the list said at the minute of any quote. And it sits upstream of every path that can emit a message: an algorithm that keeps answering RFQs in a restricted name is the breach, whatever the humans know.

*Allocation.* A block trades at one price for many owners, and, to Theo's waterfall eye, "unallocated" is a bucket. The OMS allocates by a rule written before the order leaves (pro rata to target, with a stated rounding rule), stamped with its `known_at` and applied unchanged to every partial fill. An allocation chosen after the fill prices are known is a decision about which account gets the good trade, which makes it a compliance object. It also changes the `PARTIAL` row: the unhedged intent belongs to particular accounts, so the residual-risk event carries one residual per account.

*Post-trade affirmation.* `FILLED` is terminal for the trading machine and not for the trade. Under T+1 (Chapter 22), SEC Rule 15c6-2 requires broker-dealers to have agreements or procedures designed to complete allocations, confirmations and affirmations as soon as technologically practicable and no later than the end of the trade date, so the buy side inherits the deadline. A slower machine runs after the first (`ALLOCATED`, `CONFIRMED`, `AFFIRMED`, `SETTLED`), and a trade not `AFFIRMED` by its cutoff is a risk event for operations: a settlement fail in waiting.

## 27.5 Latency Budgets Are Queues, Not Numbers

Kaz's "forty milliseconds" was true and useless. It is the time the pricing engine spends *working* on a request. The counterparty experiences the time the request spends *in the building*, and on an FOMC afternoon most of that is spent waiting. Ines puts it in her terms: "The average is the hand you expect. The p99 is the hand you get when someone at the table knows something."

### 27.5.1 Little, Pollaczek–Khinchine, and the p99, derived

> **Math, Gently.** *Queues, in two parts.* **(a) Little's law and utilisation.** A supermarket has one till. Seven customers an hour reach it, and each takes six minutes on average to ring up. The till is busy 7 × 6 = 42 minutes of every 60, a utilisation of $\rho = 0.7$, and idle for the rest. That sounds comfortable, and it is not. With customers arriving at random and checkouts that vary the way real ones do (the exponential clock of §5.3.3, where a short checkout tells you nothing about the next one), the average shopper waits about 14 minutes before reaching the till, more than twice as long as the checkout itself. Count the people waiting at random moments and you find about 1.6 on average, which is seven an hour times 14 minutes ($7/60 \times 14 \approx 1.6$). That is Little's law: the average number in a system equals the arrival rate times the average time each arrival spends there, whatever the queue's rules. A till that is idle 30% of the time can still have a queue, because the customers do not arrive during the idle moments on purpose. **(b) Why the slow jobs matter more than their share.** Buses that come every ten minutes *on average*, but irregularly, make you wait more than five minutes on average, because you are more likely to turn up during one of the long gaps: long gaps cover more of the clock. A request reaching a busy pricing engine has the same luck. It is more likely to land while the engine is chewing on one of the rare slow jobs, a callable bond's lattice, than during a trivial refresh. One number measures how lumpy the service is, the squared coefficient of variation $c_s^2$: zero if every request took exactly 40 ms, one for the exponential clock, and four for Kaz's engine, where most refreshes are trivial and a few are lattices. Waiting scales with $(1 + c_s^2)/2$, so lumpiness alone makes Kaz's engine two and a half times slower to wait for than a perfectly regular one. Put the pieces together. Mean service 40 ms, $c_s^2 = 4$ and $\rho = 0.7$ give a mean wait of $\tfrac{0.7}{0.3}\times 2.5\times 40 \approx 233$ ms, the slowest request in a hundred waits about 1.42 s, and with its own service the p99 is about a second and a half, the cold open's number. At $\rho = 0.5$ the p99 wait is near 0.8 s; at $\rho = 0.9$ it is about 4.5 s. Requests are assumed to arrive the way raindrops do, independently at a steady average rate, which is the Poisson process of §5.3.2. The formula and its proof come next.

In symbols, with Poisson arrivals at rate $\Lambda^{\text{q}}$, utilisation $\rho = \Lambda^{\text{q}}\mathbb{E}[S]$ and service variability $c_s^2$, the Pollaczek–Khinchine formula says the mean wait is $\mathbb{E}[W_q] = \frac{\rho}{1-\rho}\cdot\frac{1+c_s^2}{2}\cdot\mathbb{E}[S]$, and an exponential tail turns that mean into a p99.

#### The Full Derivation

Notation: requests (RFQs, quote refreshes, PT lines) arrive at rate $\Lambda^{\text{q}}$ per second. The superscript separates it from the order-arrival intensity $\Lambda(\delta)$ of Chapter 18, and $\lambda$ stays reserved for default. Service times $S$ have mean $\mathbb{E}[S]$ and squared coefficient of variation $c_s^2 = \operatorname{Var}(S)/\mathbb{E}[S]^2$. Utilisation is $\rho = \Lambda^{\text{q}}\mathbb{E}[S] < 1$.

**Little's law.** Over a long window $[0, \mathcal{T}]$, the area under the number-in-system curve $N(t)$ can be counted two ways: by time, $\int_0^{\mathcal{T}} N(t)\,dt = \mathcal{T}\bar N$; or by request, as the sum of the requests' sojourn times $\approx \Lambda^{\text{q}}\mathcal{T}\,\bar W$. Hence

$$
\bar N = \Lambda^{\text{q}}\,\bar W,
$$

for any queue discipline and any distributions, as long as averages exist.

**Mean waiting time (Pollaczek–Khinchine).** With Poisson arrivals, an arriving request sees the time-average state (PASTA). It waits for (i) the residual service of whoever is being served, which has mean $\rho\,\mathbb{E}[S^2]/(2\mathbb{E}[S])$ (the server is busy with probability $\rho$, and the inspection paradox makes the residual of a length-biased service $\mathbb{E}[S^2]/(2\mathbb{E}[S])$), plus (ii) the full service of the $\mathbb{E}[N_q]$ requests already queued. By Little, $\mathbb{E}[N_q] = \Lambda^{\text{q}}\mathbb{E}[W_q]$. So

$$
\mathbb{E}[W_q] = \frac{\rho\,\mathbb{E}[S^2]}{2\mathbb{E}[S]} + \Lambda^{\text{q}}\mathbb{E}[W_q]\,\mathbb{E}[S]
\quad\Longrightarrow\quad
\mathbb{E}[W_q] = \frac{\rho}{1-\rho}\cdot\frac{1 + c_s^2}{2}\cdot\mathbb{E}[S].
$$

Kingman's heavy-traffic approximation for general arrivals replaces $1 + c_s^2$ with $c_a^2 + c_s^2$, where $c_a^2$ measures arrival burstiness. **The tail.** For M/M/1, $\mathbb{P}(W_q > t) = \rho\, e^{-\rho t/\mathbb{E}[W_q]}$ exactly, and the same form is a serviceable approximation for M/G/1. The waiting-time quantile at level $q$ is then

$$
t_q \approx \frac{\mathbb{E}[W_q]}{\rho}\,\ln\!\frac{\rho}{1-q}.
$$

For Kaz's engine the quantile formula gives $t_{0.99} \approx \tfrac{233}{0.7}\ln 70 \approx 1{,}420$ ms, the box's number. Now notice when $\rho$ goes to 0.9: when TY moves, every exposed quote needs repricing at once. **Load and danger are positively correlated**, so the engine is slowest exactly when slowness is expensive. That is why the fast path exists. It does not reprice anything, so it has no queue to fill up.

> **Math, Gently.** *A relay team is as slow as its slowest leg.* Give each of a hundred runners a 1% chance of having a bad day. The chance that all hundred have a good day is $0.99^{100} \approx 0.37$, so the team has a bad day 63% of the time, although each runner almost never does. A request that waits for a hundred pricing calls is that relay team. Chapter 19's 150-line portfolio trade is a bigger team, and $1 - 0.99^{150} \approx 0.78$: it is slow 78% of the time. The arithmetic is only "one minus the chance that everything went right," and it comes next in symbols.

**Fan-out.** A portfolio trade of $n$ lines that waits for all $n$ pricing calls is slow if any one is. If each is slow with probability $p$,

$$
\mathbb{P}(\text{request slow}) = 1 - (1-p)^n .
$$

Dean and Barroso's "The Tail at Scale" (*Communications of the ACM*, 2013) made this famous with a server that is slow one time in a hundred, which is the box's relay team, and a 150-line PT inside Chapter 19's 90-second budget is the bigger team. Inverting the formula, the end-to-end p99 of the PT requires each line's latency at the $0.99^{1/150} \approx 0.99993$ quantile. **A 150-line PT's p99 is each pricing call's p99.993.** Remedies from the same literature: hedged requests (send a backup after the p95), bounded fan-out (price lines in correlated clusters and interpolate), and a hard deadline after which a line is quoted from the cluster proxy and flagged. Figure 27.4 plots both effects.

![Figure 27.4: Left, Kaz's engine is far slower in the tail than on average and slowest exactly when load rises (p99 of 4.5 s at ρ = 0.9 against 1.5 s at 0.7), and variability multiplies the tail; right, a request that waits for many calls is almost always slow. Illustrative: the Pollaczek–Khinchine mean wait and exponential-tail p99 of §27.5.1 with E[S] = 40 ms (sojourn = wait + E[S]), and 1 − (1 − p)^n for the fan-out.](assets/figures/ch27_queue_tail.png)

### 27.5.2 Two budgets on one desk

| Hop | RFQ path (quote clock) | Hedge path (hedge clock) |
| :--- | :--- | :--- |
| Market data in | FIX parse, ~1 ms | L1 switch port-to-port, as low as 4 ns per hop (Arista 7130 vendor specification) |
| Lookup | security master, ~0.1 ms | trigger-table row in on-chip memory, a few ns |
| Fair value | composite fetch, ~5 ms | none: reference prices are already in the row |
| Model | quote model, 40 ms mean, ~1.5 s p99 at $\rho = 0.7$ | fixed-point compare or multiply-accumulate, ~100 ns |
| Risk | pre-trade check, ~10 ms | hard limits in the gateway, sub-µs |
| Decision | auto-responder, or a human in ~20 s | none: the row already decided |
| Out | venue session, ms | order entry to the venue; vendor STAC-T0 tick-to-trade claims are in the tens of nanoseconds (AMD/Exegy, 2024; vendor-reported) |
| **Budget against** | **venue timer: minutes** | **race length: 5–80 µs (OP50)** |

Ines reads the model row aloud, left column then right, the way she would read two players' stacks. "Quote model: forty milliseconds on average, a second and a half at the p99 when the table gets busy. Hedge path: a hundred nanoseconds, and no model at all." She puts the pen down. "One of these is a player who thinks. The other is a player who folds. Both are on our side of the table."

*(Times are illustrative except where sourced.)* Both columns are correct, and they differ by about five orders of magnitude. The RFQ column has slack everywhere except the human, which is why automation took the quote clock first (Trend Watch, §27.1). The hedge column has no slack anywhere, which is why it contains no model.

### 27.5.3 Case Study: CME Globex halts, 2019 and 2025, a budget with an infinite term

*A replay drill on the desk's simulator. The halt dates, times and durations are the public record cited below; the desk's evening book, its trigger-table logs and the cast's answers are invented.*

Ines runs a halt drill once a quarter, on an afternoon when nothing is moving and everyone would rather be elsewhere. This quarter's falls on the Thursday of Theo's sixth week, the day after the FOMC. She loads the tape of 26 February 2019 into the simulator, gives the desk an evening book of twenty streaming investment-grade bids (a drill assumption; the desk does not normally stream at that hour), and lets it run up to the moment the public record makes interesting. On the evening of 2019-02-26, a technical error halted CME Globex for about three hours, from 6:39 p.m. to 9:45 p.m. CT, covering Treasury and S&P 500 futures, before iLink gateways restarted.

At 6:39 on the simulator's clock the Treasury futures feed stops. There is no crash, no gap message, no error code. The ticks simply stop arriving.

Kaz watches the trigger-table monitor. Every row is green. "No pulls," Kaz reports. "Nothing has crossed a threshold."

Hana, on the rota again, types "trigger table quiet" into the drill log. It is the same reflex as Wednesday's "queue normal": the monitor showed a number, and the number was calm.

"What does a quiet table mean?" Ines asks.

"That TY hasn't moved," says Kaz.

"That you haven't *heard* TY move. Those are different sentences. The table compares ticks with reference prices. No ticks, no comparisons; no comparisons, no pulls. An FPGA watching a dead feed is a smoke detector in a building with no air, and it is reporting no smoke."

Theo looks at the twenty bids, every one live and every one priced against a TY reference that is now a minute old and getting older, with nothing on the screen to say how far the truth has wandered. For a credit desk, the danger is not that the hedge is unavailable. The danger is that the fast path goes *quiet*, so every streaming bond quote stays live with no hedge and no guard. Ines takes a card from the stack.

*The hedge feed has sent no sequence number for 400 ms. Write what you do to live quotes, and what re-arms them.*

Kaz writes: widen every quote by a typical three-hour TY move and keep streaming. Hana writes: page the on-call engineer. Mags, who was not asked, says that in 1998 you rang the pit and asked whether anyone was there. Theo writes: pull every quote whose row references TY; re-arm when TY comes back.

Ines grades them in turn. Kaz's answer prices a diffusion, and the risk in the dark is a jump: three hours of news with no tape, released in the first tick after the restart. Hana's answer is a good second step, but a page takes minutes and the bids are live now. Mags's answer is the right idea with 1998's latency. Theo's first half is the answer. His second half is the trap, because when TY comes back, every reference price in every row is three hours stale, and the first prints after a restart are the likeliest prints of the evening to be a jump. What she wants on the card is the desk's **Tier-2 rule** (§27.7): if the hedge feed's heartbeat or sequence numbers stop for longer than a set gap, pull or widen every quote whose trigger row references that venue, and re-arm only when the slow path re-prices against a live hedge or an explicit substitute (CDX in place of credit futures, cash Treasuries in place of TY). The fast path says no on silence. Only the slow path, with a fresh price, says yes again.

The second halt in the drill is shorter on the simulator and longer in life. In Thanksgiving week of 2025 (2025-11-27/28), a cooling failure at a CyrusOne data centre near Chicago stopped Globex for a reported ten hours or so, halting Treasury and SOFR futures (Hedgeweek; duration per press reports). Mags reads the headline off Ines's screen. "Ten hours," she says. "Longer than a lender call, and with fewer lawyers." A budget that assumed the hedge venue would always be there had an infinite term in it, and nobody had written it down.

### Specification for AI Implementation (latency as a queue)

**What ROBO built from the vague version.** Asked to "report latency," ROBO reported the mean of the service time, measured inside the pricing function. It was 40 ms on the day the desk was picked off. The spec: measure sojourn (arrival to response), report p50/p99/p99.9 per utilisation band, and check the queueing model against simulation before trusting it.

Kaz's forty milliseconds measured the wrong thing, and the spec asks for the right one: time from arrival to response, reported as p50, p99 and p99.9 by utilisation band, and checked against a simulation before anyone believes the formula. The desk has a reason to automate that beyond tidiness. The Pollaczek–Khinchine result is a pen-and-paper argument, and every risk meeting that leans on it eventually asks what happens if arrivals are burstier than Poisson. It is cheaper to have the answer in a file than in Kaz's head.

Listing 27.3 has four small functions and a block of checks. `pk_mean_wait` is the closed form of §27.5.1: utilisation over one minus utilisation, times half the sum of arrival and service variability, times the mean service time. With `ca2` left at 1 it is exact for Poisson arrivals, and any other value turns it into Kingman's heavy-traffic approximation. It raises at utilisation of 1 or more, because there is no steady state to report. `wait_quantile_approx` inverts the exponential tail and returns zero when the requested tail probability exceeds the utilisation, since most requests then do not wait at all.

`simulate_mg1` is the cross-check. It draws gamma service times with the requested mean and squared coefficient of variation, draws exponential gaps between arrivals, and runs the Lindley recursion in a vectorised line: the wait before each request is a running sum minus its running minimum. It returns waits and service times, so the caller can add them to get sojourn. `fanout_slow_prob` is the one-line $1-(1-p)^n$.

The checks run Kaz's engine: 40 ms mean service, squared variation of 4, utilisation 0.7. They require a mean wait of 233 ms; a million simulated requests that agree with it within 10 percent after a burn-in; a tail-formula p99 between three-quarters and four-thirds of the simulated one; and a p99 sojourn between one and 2.4 seconds. Moving utilisation to 0.9 must multiply the mean wait by more than three and a half. The fan-out lines reproduce 63 percent slow at 100 calls and 78 percent at 150, by formula and by Monte Carlo.

Use it to set a utilisation ceiling before the busy hour, not to forecast the busy hour. The edge that bites is the utilisation you feed it. Averaged over the day the engine looks comfortable at 0.3. On an FOMC afternoon, when every exposed quote needs repricing at once, it is 0.9, and the mean wait is nearly four times the 0.7 case. Feed the function the stress window's arrival rate, and raise `ca2` for bursts, or it will reassure you in the one hour you do not want reassurance.

*The full listing is [Listing 27.3 in Appendix F](#code-27-3).*

## 27.6 FPGA Trigger Tables for Quote-Pulling

An FPGA is a chip whose logic you configure: a grid of lookup tables, registers, small memories and multiply-accumulate blocks that you wire into a pipeline. It is very good at fixed-point arithmetic, comparisons, and doing the same thing every few nanoseconds with no operating system, no garbage collector and no jitter. It is very bad at pricing a callable bond, running a loop of unknown length, or anything whose logic changes every day; changing the logic means re-synthesising the design, which takes hours and a change-control meeting nobody enjoys. An ASIC is the same idea cast permanently in silicon, which is why desks buy ASIC-based switches and build almost nothing in ASICs themselves. The design principle follows from both lists: **the table is data and the logic is fixed.** The slow path rewrites rows as often as it likes. The comparator that reads them is synthesised quarterly and tested like a bridge.

### 27.6.1 The trigger table, derived

Let exposed quotes be indexed by $i$ (streaming bids and offers, live firm RFQ responses) and hedge instruments by $j = 1, \dots, J$ (TY, HYG, LQD, CDX, credit futures). When the slow path prices quote $i$, it records the bond's fair value $\hat P_i$, the half-spread $h_i$, and the hedge reference prices $H_j^{\text{ref}}$. For small moves $\Delta H_j = H_j - H_j^{\text{ref}}$, fair value moves by

$$
\Delta \hat P_i \approx \sum_{j=1}^{J} \beta_{ij}\,\Delta H_j = \boldsymbol\beta_i^{\top}\Delta\mathbf H,
$$

where $\beta_{ij}$ is in bond points per hedge-instrument point. Hedge ratios are ratios of dollar durations, the DV01 ratios that Chapter 8 builds for the desk's hedges and Chapter 24 uses across the basis, borrowed here as they stand (Veronesi defines dollar duration as $D^{\$}_P = -dP/dr$ and relates it to duration by $D^{\$}_P = P \times D_P$; Veronesi_Fixed_Income_Securities p.120). For a rate hedge, with $\kappa_i^{\text{rate}}$ the empirical rate beta of Chapter 8 (empirical over model duration),

$$
\beta_{i,\text{TY}} = \frac{\text{DV01}_i}{\text{DV01}_{\text{TY}}}\,\kappa_i^{\text{rate}} .
$$

For a credit-ETF hedge, write $\Delta P_i \approx -P_i D^{\text{spr}}_i \Delta s_i$, $\Delta s_i = \kappa^{\text{cr}}_i\,\Delta s_{\text{HY}}$ (the DTS beta of Chapter 9, $\kappa^{\text{cr}}_i \approx s_i/s_{\text{HY}}$), and $\Delta H \approx -H D_H \Delta s_{\text{HY}}$; eliminating $\Delta s_{\text{HY}}$,

$$
\beta_{i,\text{HYG}} = \frac{P_i\,D^{\text{spr}}_i\,\kappa^{\text{cr}}_i}{H\,D_H}.
$$

**The cold open, as numbers** *(all inputs illustrative)*. A bond at $P_i = 95$ with $D^{\text{spr}}_i = 8$ has $\text{DV01}_i = 0.076$ points per bp. With a TY futures DV01 of 0.065 points per bp and $\kappa^{\text{rate}} = 0.9$, $\beta_{\text{TY}} \approx 1.05$. With the bond at 130 bp, the HY index at 325 bp ($\kappa^{\text{cr}} = 0.4$), HYG at \$80 and $D_H = 3$, $\beta_{\text{HYG}} \approx 1.27$. TY down six 32nds and HYG down 14 cents give $\Delta\hat P \approx 1.05(-0.1875) + 1.27(-0.14) \approx -0.375$: three-eighths.

> **Math, Gently.** *Two detours are never shorter than the straight road.* Walk from your door to the station by any route you like and you cannot beat the straight line. Read backwards, that is a promise: cap the length of each leg of the walk and you have capped how far from the door you can end up. The cheap trigger rule below runs on that promise. The bond's fair value moves by the TY move times its TY sensitivity plus the HYG move times its HYG sensitivity, and the two pieces can add up or partly cancel. In the worst case they add. So give each hedge its own lane. Let TY move at most 0.07 of a point (about 1 bp of yield) before the quote is pulled, which can move the bond by at most $1.05 \times 0.07 \approx 0.074$ points, and let HYG move at most 5 cents, which can move it by at most $1.27 \times 0.05 \approx 0.064$ *(illustrative split of the §27.6 checks)*. The two lanes add up to about 0.14, the whole budget. If neither hedge has left its lane, the bond cannot have moved more than 0.14 points, whatever the combination, so the cheap rule never misses a pull the exact rule would make. It does sometimes pull when one hedge leaves its lane while the other cancels it and the bond is fine, and that is the price of the promise. The proof below is the same sentence in one line of algebra.

**The joint rule.** The bid $b_i = \hat P_i - h_i$ becomes a gift when fair value falls more than the edge we insist on keeping. With a minimum margin $m_i \ge 0$ and a guard band $\varepsilon$ (derived below), define $\theta_i = h_i - m_i - \varepsilon$ and

$$
\text{pull bid } i \iff \boldsymbol\beta_i^{\top}\Delta\mathbf H < -\theta_i, \qquad \text{pull offer } i \iff \boldsymbol\beta_i^{\top}\Delta\mathbf H > \theta_i .
$$

**The per-instrument rule.** The joint rule needs a multiply-accumulate per quote per tick. The cheaper rule needs only compares. Split the budget $\theta_i = \sum_j \theta_{ij}$ with $\theta_{ij} \ge 0$, and set thresholds in each hedge instrument's own price units, $\tau_{ij} = \theta_{ij}/|\beta_{ij}|$. Pull if any $|\Delta H_j| > \tau_{ij}$.

**Theorem (the cheap rule is safe).** If no per-instrument trigger fires, the joint rule does not fire either.

*Proof.* If $|\Delta H_j| \le \tau_{ij}$ for all $j$, then by the triangle inequality

$$
\big|\boldsymbol\beta_i^{\top}\Delta\mathbf H\big| \le \sum_j |\beta_{ij}|\,|\Delta H_j| \le \sum_j |\beta_{ij}|\,\tau_{ij} = \sum_j \theta_{ij} = \theta_i . \qquad\blacksquare
$$

The price of safety is false pulls, and they come exactly when moves offset. In a flight to quality TY rallies and HYG falls, and an IG bond's fair value barely moves, so the cheap rule panics at the one moment the bond is calm. It is a smoke detector that goes off when you open a window. **Allocating the budget.** Under diffusion over a short horizon, instrument $j$ alone fires with probability $2\Phi(-\tau_{ij}/\sigma_j)$, where $\sigma_j$ is its volatility over that horizon. Equalising the standardised distances $\tau_{ij}/\sigma_j = c$ gives $\theta_{ij} = c\,|\beta_{ij}|\,\sigma_j$ with $c = \theta_i/\sum_j |\beta_{ij}|\sigma_j$, which stops one noisy hedge from owning the whole budget. Figure 27.5 draws both rules in the (TY, HYG) plane.

![Figure 27.5: The cheap rule's no-pull box sits inside the exact rule's no-pull band and touches it at two corners, so it never misses a pull, and its false pulls fill the diagonal corridor where TY and HYG offset, as in a flight to quality. Illustrative: β_TY = 1.05 and β_HYG = 1.27 from the cold-open numbers of §27.6.1, and θ = 0.14 points (half-spread 0.19 less margin 0.04 and guard band 0.01, as in the §27.6 checks), with assumed hedge volatilities of 0.06 TY points and 0.05 HYG dollars to split the budget.](assets/figures/ch27_trigger_geometry.png)

Hardware has no floating-point unit to spare, so the table stores its numbers in *fixed point*: every quantity is an integer count of one small unit. (This is fixed-point arithmetic, not the fixed point of an equation that Chapters 6-B and 18 solve for.) With sixteen binary places, the format the desk calls Q.16, the unit is $2^{-16} = 1/65{,}536 \approx 1.5\times 10^{-5}$ of a point, so a sensitivity of 1.05 is stored as the integer 68,813 and is wrong by at most half a unit. Multiplied by a few hundred ticks of hedge move, that rounding stays near a thousandth of a point, which is the first half of the guard band.

**The guard band $\varepsilon$.** Two errors separate the hardware's number from the truth. *Fixed point:* with $\beta$ stored as integers with $f$ fractional bits (bond points per hedge tick) and moves as integer ticks $n_j$, rounding error is at most $2^{-f-1}\sum_j |n_j|$; at $f = 16$ and a few hundred ticks this is about $10^{-3}$ points or less. *Convexity:* Veronesi's second-order term (S14 below) is $\tfrac12 C P (\Delta r)^2$; for $C = 80$, $P = 95$ and a 10 bp move it is $\tfrac12\cdot 80\cdot 95\cdot 10^{-6} \approx 0.004$ points *(illustrative)*. Set $\varepsilon$ above the sum, say 0.01 points, and the linear rule can never be fooled into keeping a quote that the exact rule would pull.

**Re-arming.** The fast path may only pull. A pulled quote comes back only when the slow path reprices it and writes a new row with new reference prices. This kills flapping (pull, re-quote, pull) for free and preserves the chapter's invariant: the fast path says no, and only the slow path says yes.

> **[SOURCE EXTRACTION]** *Veronesi_Fixed_Income_Securities p.152:* "Fact 4.1 An approximation of the percentage impact of interest rates on the price of a security is given by dP/P = −D × dr + ½ × C × dr²"
>
> **Annotation.** Our analysis: the FPGA implements the first term and ignores the second, and Veronesi's own footnote ("stems directly from the application of a second-order Taylor expansion") tells you how large the neglected term can be. That makes convexity a *threshold-error budget*, not a pricing input. The desk departs from the textbook use in two ways. The relevant "duration" is empirical and spread-adjusted (Chapter 8), not the analytic one, because IG spreads partly offset rate moves. And for callable or distressed bonds the second-order term is neither small nor stable, which is the honest reason such bonds should not be streamed from a linear table at all.

### 27.6.2 What a stale quote costs: diffusion versus tournament

> **Math, Gently.** *A random walk, and why its typical distance grows with the square root of time.* A man leaves a bar and takes one step a second, each step left or right at random. After 100 steps he is not 100 steps from the lamppost, because most of the steps cancel; his typical distance is about $\sqrt{100} = 10$ steps. After 400 steps it is about 20. Distance grows with the square root of the number of steps, because the variances of independent steps add while their directions mostly cancel. A bond's fair value over a few seconds with no news behaves like that walk, nudged up or down each second by small, unrelated orders and quotes. If one second's typical nudge is $\sigma = 0.0033$ points *(illustrative: half a point a day spread over a 23,400-second session)*, then over the 1.5 seconds the cold open's quote was stale the typical move is $0.0033 \times \sqrt{1.5} \approx 0.004$ points. Theo's half-spread was 0.19 points, about 47 typical moves away. Diffusion is not going to walk 47 typical distances in a second and a half, so against drift the half-spread is a wall. Against a jump it is a curtain: TY moved six 32nds in one step, and the walk has nothing to say about that. One modelling choice is hiding in the picture. Over seconds, price changes add (a bond moves by 0.004 points, not by 0.004 percent of itself), so the right walk is in price, the normal or *Bachelier* model, rather than in the logarithm of price, the lognormal model that suits long horizons and quantities that must stay positive (§5.2.3 owns that distinction). The normal model allows a negative price in principle, which over 1.5 seconds on a bond at 95 is a risk nobody needs to price.

Put in symbols, the expected loss of a stale bid under diffusion is an out-of-the-money Bachelier put on fair value, $\sigma\sqrt{\Delta}\,[\varphi(x) - x\,\Phi(-x)]$ with $x = h/(\sigma\sqrt{\Delta})$ the half-spread measured in typical moves, and at $x \approx 47$ it is zero to machine precision. **Against diffusion, the half-spread is an impregnable wall.** A jump is a different animal.

Now a *jump*: a public, discrete move of fair value $J_i = \boldsymbol\beta_i^{\top}\Delta\mathbf H$, seen by everyone at once. If the quote is still live, the taker wins with probability $\pi$, the probability that their order reaches the venue before your cancel, and the loss is

$$
\pi\,\big(|J_i| - h_i\big)^{+}.
$$

In the cold open, $\pi \approx 1$ (a 1.5-second reaction against takers measured in microseconds to milliseconds), and the loss is $(0.375 - 0.19) \times \$3\text{mm}/100 \approx \$5{,}500$. Latency enters the two regimes in completely different ways. Under diffusion it enters smoothly through $\sqrt{\Delta}$, and a wider $h$ compensates. Under jumps it enters only through $\pi$, which depends on your *rank* among responders and not on your level of speed: being second is the same as being last. This is the sniping mechanism of Budish, Cramton and Shim (2015, *Quarterly Journal of Economics*), and the FCA study puts numbers on it for equities: modal race 5–10 µs, median 46 µs, mean 79 µs, 90th percentile about 200 µs; races are about 20% of volume, and the latency-arbitrage "tax" is 0.42 bp of total volume against an average effective spread just over 3 bp (Aquilina, Budish and O'Neill 2020). A credit desk's half-spread is far wider, but so is the jump in a hedge instrument during a quote's life. The trigger table exists to turn $\pi$ from 1 into something near 0 by pulling while the race is still being run.

#### The Full Derivation

Let fair value over the exposure window $\Delta$ (seconds) follow Bachelier dynamics under $\mathbb{P}$, $\hat P_{t+\Delta} = \hat P_t + \sigma\sqrt{\Delta}\,Z$ with $Z \sim N(0,1)$ and $\sigma$ in points per $\sqrt{\text{s}}$. An informed taker sells to the bid iff $\hat P_{t+\Delta} < b = \hat P_t - h$. The expected loss per exposure, against new fair value, is

$$
\mathbb{E}\big[(b - \hat P_{t+\Delta})^{+}\big] = \mathbb{E}\big[(-h - \sigma\sqrt{\Delta}\,Z)^{+}\big] = \sigma\sqrt{\Delta}\,\big[\varphi(x) - x\,\Phi(-x)\big], \qquad x = \frac{h}{\sigma\sqrt{\Delta}},
$$

the Bachelier put with the strike $h$ out of the money. Using $\Phi(-x) = \varphi(x)\big(x^{-1} - x^{-3} + O(x^{-5})\big)$, the bracket is $\approx \varphi(x)/x^2$ for large $x$, which is smaller than exponential. Take a fair-value volatility of 0.5 points a day over a 23,400-second session *(illustrative)*, so $\sigma \approx 0.0033$, and $h = 0.19$. At $\Delta = 1.5$ s, $x \approx 47$, the box's 47 typical moves, and the loss is zero to machine precision. Even over a two-minute RFQ timer, $x \approx 5.3$ and the loss is about $10^{-9}$ points. The wall holds.

> **[SOURCE EXTRACTION]** *Dynkin_Systematic_Investing_in_Credit p.702:* "LCS measures the cost of an immediate round-trip transaction of a typical institutional size and is expressed as a percentage of a bond price. ... For bonds quoted on spread, LCS is calculated as a product of bid–offer spread and spread duration."
>
> **Annotation.** Our analysis: this pins down $h_i$ with units. LCS is a round trip as a percentage of price, so the half-spread in points is $h_i = \tfrac12\,\text{LCS}_i \times P_i/100$: an LCS of 0.4% on a 95 bond gives $h = 0.19$, the number used throughout this section. LCS also decides *which bonds get streamed*. A bond whose $h_i$ is small relative to the typical hedge-implied jump $|J_i|$ is a bond whose streaming quote is a donation, and it should stay RFQ-only. Ben Dor makes the complementary point that a trader who must "commit to making a market in a bond for a time going forward" should prefer the higher-volume bond at similar LCS (Ben_Dor_Quantitative_Credit_Portfolio_Management p.160). Volume shortens the time inventory waits; it does not shrink the jump.

### 27.6.3 Case Study: The 15 October 2014 Treasury flash rally, replayed against a trigger table

*A replay. The dates, the yield path and the volume share are the public record cited below; the desk's book, its trigger-table timings and the cast's choices are invented.*

Ines runs the second replay of the week on the Friday, and she runs it the way she runs the halts: tape loaded, book live, clock stopped at a moment the public record makes interesting. The tape is Wednesday 15 October 2014. The book is the cold-open bond, a bid and an offer streaming either side of fair value with the row of §27.6.1, $\theta = 0.14$ and the budget split as above. The clock stops at 9:33 a.m. Eastern. "This is the canonical hedge-clock event," she says, "and it happened in the instrument we hedge with."

She starts the clock. Treasury yields begin to fall, and fast. TY rallies, and because the bond's fair value moves with TY at 1.05 points per TY point, every streaming *offer* starts to become a gift within the first basis point or two of the move: buyers can lift the desk's offer at a price set before the rally and sell the bond back later at the new one. The TY threshold, $\tau_{\text{TY}} \approx 0.07$ TY points, is about 1 bp of yield, so the per-instrument rule pulls the offer within microseconds of the first meaningful ticks. On the simulator's log the offer is gone two microseconds after the tick that crossed the line *(illustrative)*. The bid stays up. In a rally the bid is the safe side, the side nobody wants to hit.

Theo watches the offer vanish and feels, for the first time this week, that the machine did something right on purpose.

Then nothing much happens to the desk for twelve minutes, and everything happens to the market. The 10-year yield keeps falling. A 16 bp rally moves TY by roughly a point at 0.065 points per bp, so the bond's rate-implied fair value rises by about a point. The desk is out of the offer side of a market that is moving its way, and the sales coverage line is ringing.

Hana, asked to check the composite, reports that its last update on the bond is time-stamped 9:31 and that the vendor's status page says "all systems normal," which is true of the systems and says nothing about the price.

Kaz wants back in. "Fair value is up a point. Re-arm at the new fair value with the normal half-spread. We're missing the flow, and the table has done its job."

Mags wants out, by phone. "Forget the screen. Ring three accounts and offer them the bonds at a level that looked rich this morning. In a rally like this they'll take them, and whatever this is, it isn't a fundamental reason for a BBB industrial to be worth a point more."

Ines asks the question she asks at every table. "Who here knows more than you right now?" Then she answers it herself, slowly, so that Theo can write it down. The composite the slow path would use to set a new fair value is stale, because the evaluators are looking at the same screen and have not moved. TRACE is up to 15 minutes behind, so the public tape of the bond itself is describing a market from before the rally. The only live evidence on the desk is TY, and TY is moving in a way nobody on the desk can explain. She takes a card from the stack.

*Write the re-arm rule: when, at what $h$, and what evidence.*

Kaz writes: when the slow path has a new fair value; the usual $h$; the composite. Mags writes nothing, on principle, and says the phone is the rule. Theo writes: when TY stops moving; a wider $h$; TY itself.

Ines restarts the clock. Between 9:33 and 9:45 a.m. ET on 2014-10-15, the 10-year Treasury yield fell 16 bp and then rebounded, "without a clear cause," on a day when it traded in a 37 bp range and closed 6 bp below its open. Principal trading firms accounted for more than half of traded volume in the electronic interdealer market (Fleming, Johansson, Keane and Meyer, *Liberty Street Economics*, 2019-10-15, looking back at the Joint Staff Report released 2015-07-13). On the simulator Ines runs Kaz's branch beside the desk's: Kaz's offer, re-armed at the new fair value a few minutes into the rally, is lifted on the way up as TY ticks higher, and when the move reverses the bid at the same stale level is hit on the way down. A desk that pulled and waited lost nothing but opportunity. A desk that kept streaming was picked off on the way up and again on the way down.

Mags's branch is harder to grade, and Ines says so. On this day the yield came back, so bonds sold by phone into the rally would have looked clever by lunch. "That's a view," Ines says, "and maybe a good one. It isn't a re-arm rule. You'd have been right for a reason you couldn't have written on the card at 9:38." Mags allows that this is true of most of her best trades.

Theo's card is closest. The right re-arm rule is **volatility-gated**: re-quote only when realised hedge volatility over the last $N$ seconds is below a threshold, and then at a wider $h$. The evidence is the hedge's own tape, the one input that is live, rather than the composite or TRACE, which are describing a market that no longer exists. What Theo missed is that "when TY stops moving" needs a number and a window before it can be a rule, and on this desk both are parameters with an owner, not a feeling.

The market itself behaved like a giant trigger table that day, with liquidity providers pulling and re-quoting in waves. That is not a bug in the market; it is what rational quote-pulling looks like when everyone has the same table.

### Specification for AI Implementation (trigger tables)

**What ROBO built from the vague version.** Asked to "pull quotes when the market moves," ROBO pulled every quote whenever any instrument ticked. It was perfectly safe and quoted for a total of eleven seconds on its first day. The spec: sensitivities in bond points per hedge point, a joint rule and a provably safe per-instrument rule, fixed-point arithmetic with a stated error bound, pull-only semantics, and the cold open as a regression test.

A trigger table is a small piece of arithmetic that has to be right in three places at once: on paper, in a reference implementation, and in fixed-point hardware that will never see a float. The slow path computes the table and the FPGA only reads it, so nobody gets a second chance to find out that a sign was wrong. The desk therefore wants one reference that states every sensitivity in bond points per hedge point, runs both pull rules against the same moves, and proves the cheap rule safe by brute force before a bitstream is synthesised. Ines would call it checking the odds before sitting down.

Listing 27.4 starts with the sensitivities. `beta_rate` is the dollar-duration ratio times the empirical rate beta, and `beta_credit` is the ETF version: bond price times spread duration times DTS beta, over the ETF's price times its spread duration. `allocate_tau` splits the pull budget $\theta$ across hedges in proportion to $|\beta_j|\sigma_j$ and divides each share by $|\beta_j|$, which gives thresholds in each hedge's own units. `joint_pull` is the exact rule: the dot product of $\boldsymbol\beta$ and the hedge move, compared with minus $\theta$, with `side` flipping the sign for an offer. `box_pull` is the cheap rule: any hedge move beyond its own threshold. `bachelier_pickoff` is the closed form of §27.6.2.

The checks replay the cold open with $\theta = 0.19 - 0.04 - 0.01 = 0.14$ points. TY down six 32nds and HYG down 14 cents move fair value by about three-eighths, and both rules pull the bid. In a flight to quality, fair value barely moves, the joint rule stays quiet and the cheap rule pulls, which is its false alarm on display. Then 200,000 correlated, fat-tailed moves, rounded to tick grids, confirm that the joint rule never fires without the cheap one and measure the false pulls that safety costs. A Q.16 integer version shows that the hardware's decision differs from the exact one only inside the stated error bound, for moves up to two points per refresh; larger ones meet the Tier-0 collars first. The last block checks the diffusion pick-off loss against Monte Carlo at 15 minutes, finds it zero at 1.5 seconds, and prices the jump loss at about \$5,500.

Use the pair of rules for streamed, linear bonds. Do not use them for callables or distressed paper, where convexity swamps the guard band. The edge that bites is a zero beta: `allocate_tau` then divides zero by zero, and that hedge's threshold comes back as NaN with a warning. Comparisons against NaN are false, so the hedge never pulls, which happens to be right, but hardware has no NaN. Give the table an explicit "never" sentinel for any hedge a bond does not use.

*The full listing is [Listing 27.4 in Appendix F](#code-27-4).*

In 2014 the only fast hedge the cold-open bond had was rates. Since then credit beta has acquired a matching engine of its own.

> **Trend Watch. Credit gets a listed hedge (2018–2026).** *What changed:* for most of its history the credit desk's fast hedge was rates (TY) plus an ETF; credit beta itself had no exchange-traded future. Cboe listed iBoxx iShares futures on HY (IBHY, 2018) and later IG (IBIG). CME launched Bloomberg US corporate index futures (IG and HY, including duration-hedged variants) in June 2024. *How big:* record open interest of 3,200 contracts (about \$320mm notional) in March 2025. A CME factsheet reported more than 580,000 contracts traded since launch as of 2025-10-10, open interest above 6,800 contracts (more than \$730mm notional), and Q3-2025 ADV above 2,900 contracts (CME press releases 2025-03-17 and 2025-09-08). Cboe's IBHY/IBIG block trades topped \$1bn a month for two consecutive months in July–August 2026, with IBIG block volume passing IBHY for the first time (The DESK, 2026-10-16, Cboe-sponsored content). *What it means for the desk:* a credit-beta hedge now executes on a matching engine with microsecond order entry and a public book. That gives the trigger table a credit column that is not an ETF with its own premium/discount dynamics. It also means credit-index futures can jump on their own, so they belong in $\Delta\mathbf H$, with their own $\beta_{ij}$ and their own heartbeat rule (§27.5.3).

## 27.7 Kill Switches as Stopping Rules

"Folding before the river," Ines says, "is not cowardice. It's a stopping rule with a measure attached. You decide in advance what evidence makes you get up from the table, and how often you're willing to get up for nothing." The kill switch is the sacred right of the system: no majority of components can amend it, and no single component can waive it.

> **View From Another Seat.** *The bank dealer desk in March 2020: the kill switch was a person.* A bank's credit desk runs the same two clocks as ours, with one difference that matters in a crisis: its auto-quoter sits inside a balance sheet with capital charges, a risk committee, and clients who will remember who answered the phone. In March 2020, in Coalition Greenwich's account, "several of the largest banks famously shut down their auto-quoters" because their pricing algorithms could not cope with the volatility, a lesson the same post says later let them handle bouts of volatility (Kevin McPartland, 2024-02-13). Nobody outside those banks knows who decided, at what minute or on what evidence; the public record is the outcome. Read generically, and this is our inference, the switch in 2020 was a senior person on an e-trading desk deciding that the machine's prices could no longer be trusted, and the flow went back to voice, where humans priced it wider or not at all. Six years later buy-side traders told FILS Europe that electronic liquidity providers "help mainly in normal markets" (October 2026), the same observation from the client's chair. The question this section puts to the dealer's seat is whether that decision should have been a parameter: a Tier-3 threshold with a named owner, written down in a calm market, rather than a judgment made in the worst hour of the year by whoever was senior and awake. The bank has a reason to prefer the person, who can weigh the franchise. The parameter has a reason too. It fires on the same evidence every time, and somebody has to say in advance what that evidence is.

### 27.7.1 The hierarchy

| Tier | What fires it | Where it lives | Time scale | Example controls |
| :--- | :--- | :--- | :--- | :--- |
| 0: hard limits | a single message violates a pre-set bound | gateway / FPGA, before the wire | ns–µs | price collar vs composite and last fill; max order value and volume; message-rate throttle; notional and DV01 caps; `PriceType` sanity |
| 1: sequential tests | accumulating evidence of being picked off or of abnormal fills | risk engine, streaming | seconds–minutes | CUSUM on markouts; fill-ratio and child-to-parent ratio tests |
| 2: system health | the machine is not the machine you tested | ops plane | seconds | version and config-checksum skew across servers; hedge-feed heartbeat lost; clock fault; venue session down |
| 3: loss limits | the strategy, not the plumbing, is failing | PM and risk committee | days | drawdown stop-loss (Paleologo), capital reallocation (Chapter 28) |

Most of the table reads like paperwork, and the row that reads most like paperwork is Tier 2. *The incident below is fictional; the servers and files are invented.* The desk learned its value on Tuesday 29 September, Theo's second week, at 7:52 a.m., eight minutes before the quoting engine was due to start streaming. Hana's pre-open check compares the checksum of the configuration file on each of the four quoting servers. Three agreed. The fourth carried the previous week's file, with the old half-spread table from before Kaz widened the high-yield rows after a bad Friday: the deployment job had restarted that server overnight after a kernel patch and restored its configuration from a snapshot taken before the change. The check did nothing clever. It refused to arm the engine and paged Hana and Kaz. Kaz pushed the current file, the checksums agreed at 8:06, the engine armed at 8:07, and the desk streamed seven minutes late on a quiet morning, at a cost of perhaps one inquiry.

Mags heard about it at lunch and asked what would have happened without the check. "Nothing dramatic," said Kaz. "One server in four quoting high yield three-eighths tighter than the rest."

"So a quarter of our high-yield quotes too tight all day, and nobody looking," said Mags. It was Knight's eighth server played the other way round, one machine out of step with the rest, found at 7:52 instead of in the first minutes of trading (§27.7.3 tells that morning).

Kaz, still working on the sacred-rights metaphor, asked afterwards whether the kill switch therefore needs unanimous consent to change. "It means it needs two humans to turn back *on*," said Ines. "Anyone can turn it off." That answer is the design. **Authority** is part of the design, not an org chart. Anyone and anything (a human, a monitor, ROBO) may *trip* any tier, instantly, and a trip cancels all live orders and quotes in its scope. Only the slow path, with two distinct authorised humans, may *re-arm*. Every trip records who, what and why, and every order carries the algorithm, trader and desk responsible for it. This is the regulator's floor, and it is a good design anyway. MiFID II RTS 6 (Delegated Regulation (EU) 2017/589, applying from 2018-01-03) requires the ability to "cancel immediately, as an emergency measure, any or all of its unexecuted orders" (Art. 12), pre-trade price collars, maximum order values and volumes and message limits (Art. 15), and states that "Real-time alerts shall be generated within five seconds after the relevant event" (Art. 16). SEC Rule 15c3-5 is principles-based and puts no number on alert latency. RTS 6's five seconds is the only regulatory clock on the slow lane, and a desk should treat it as a ceiling, not a target.

### 27.7.2 CUSUM on markouts, derived

> **Math, Gently.** *Evidence that adds up and forgets.* Ines, across a card table, suspects a player of bluffing. Each hand gives her a little evidence. A tell adds to her count; a hand where he shows down an honest holding takes some away; and the count never goes below zero, because a run of honest hands earns him no credit against tomorrow's bluff. When the count reaches a line she drew before she sat down, she acts. The desk does the same with fills. Score each fill by how much worse its one-minute markout was than a healthy fill's, in standard deviations, and subtract a small allowance, half the size of the deterioration you are looking for (here 0.5), so that ordinary noise drifts the count down. Five fills scoring 1.6, 0.9, 2.1, 1.4 and 1.5 move the count to 1.1, 1.5, 3.1, 4.0 and 5.0, and with the line at 5 the fifth fill trips the switch. Where to draw the line is the whole decision. At 5, a healthy desk's count wanders up to the line by chance about once every 938 fills, a false alarm every five trading days at 200 fills a day *(illustrative)*, and a real one-standard-deviation deterioration is caught after about 10 bad fills. Move the line to 6 and false alarms come about every 2,570 fills, nearly three times rarer, for about two more bad fills before the alarm. That lopsided trade is the reason the method is worth knowing.

In symbols, with $z_k$ the fill's markout shortfall in standard deviations and $\delta$ the deterioration being watched for, the count and the alarm are

$$
G_k = \max\!\Big(0,\ G_{k-1} + z_k - \tfrac{\delta}{2}\Big),\quad G_0 = 0, \qquad K_c = \inf\{k : G_k \ge c\},
$$

and the desk head picks the line $c$.

#### The Full Derivation

Let fill $k$ have a markout $m_k$ (points, against hedge-implied fair value one minute after the fill, signed so that positive is good for the desk). It arrives long before TRACE does. Healthy: $m_k \sim N(\mu_0, \sigma^2)$ i.i.d. Picked off: $m_k \sim N(\mu_1, \sigma^2)$ with $\mu_1 < \mu_0$. The log-likelihood ratio of one observation is

$$
\ell_k = \ln\frac{f_1(m_k)}{f_0(m_k)} = \frac{\mu_0 - \mu_1}{\sigma^2}\left(\frac{\mu_0 + \mu_1}{2} - m_k\right) = \delta\left(z_k - \frac{\delta}{2}\right),
\qquad z_k = \frac{\mu_0 - m_k}{\sigma},\quad \delta = \frac{\mu_0 - \mu_1}{\sigma}.
$$

That is why Page's CUSUM, the recursion stated above, accumulates the evidence and forgets it whenever it favours health. (We write the alarm index as $K_c$ because $\tau$ is reserved for default time.) It is a sequence of SPRTs, each restarted at zero, and it minimises the worst-case detection delay among all procedures with the same false-alarm rate (Lorden 1971; Moustakides 1986). The average run length for increments $N(\mu_G, 1)$ has Siegmund's approximation

$$
\text{ARL}(\mu_G) \approx \frac{e^{-2\mu_G b} + 2\mu_G b - 1}{2\mu_G^2}, \qquad b = c + 1.166,
$$

with $\mu_G = -\delta/2$ when healthy ($\text{ARL}_0$, the mean time between false alarms) and $\mu_G = +\delta/2$ when picked off ($\text{ARL}_1$, the detection delay). For a one-standard-deviation deterioration ($\delta = 1$) and $c = 5$: $\text{ARL}_0 \approx 938$ fills and $\text{ARL}_1 \approx 10.3$ fills. At 200 auto-quoted fills a day *(illustrative)*, that is a false alarm about every five trading days and detection within about ten bad fills. Raise $c$ to 6 and $\text{ARL}_0 \approx 2{,}570$ fills (about 13 days) while $\text{ARL}_1 \approx 12.3$. **Tripling the quiet time costs two fills of delay**, because to first order the delay grows only with the log of the false-alarm interval, $\text{ARL}_1 \approx \ln(\text{ARL}_0)/\mathcal{K}$ with $\mathcal{K} = \delta^2/2$ the Kullback–Leibler information per fill. The desk head chooses $c$, and in doing so chooses both numbers. Ines calls this reading the hand history in real time. The river is the bad fill that would have cost you the session; the CUSUM folds about ten bad fills in, which is long before the river and long after your ego would have liked.

> **[SOURCE EXTRACTION]** *Paleologo_Advanced_Portfolio_Management p.164:* "Stop-loss rules are a partial hedge for the PM call option. ... Since the value of the option increases with the volatility of the underlying asset, it is in the interest of the manager to run with the highest possible volatility, independently of her skill. The stop-loss is a constraint that limits the value of this option."
>
> **Annotation.** Our analysis: Tier 3 is Paleologo's stop-loss moved from the PM's contract to the machine, and the option argument applies to algorithms too. An auto-quoter rewarded on volume or hit rate holds a call option on its own variance, and will "run with the highest possible volatility" if its parameters let it, through wider size and tighter quotes in fast markets. The tiers below are the faster, finer versions of the same constraint. The modern desk departs from the PM framing in one respect: the stop-loss for an algorithm must be paired with an *automatic* re-arm prohibition. A human PM who is stopped out goes home and thinks. An algorithm that is stopped out will be restarted by a well-meaning engineer at 10:02 a.m. unless the design says only two humans and the slow path can do that.

### 27.7.3 Case Study: Knight Capital (2012) and Citigroup (2022), mapped to tiers

#### Long Scene: Forty-five minutes, 1 August 2012

*A fictional desk replaying the public record. Every Knight fact below comes from the SEC's order, Release No. 34-70694 (2013-10-16); no words are attributed to anyone at Knight, the minute-by-minute position screen is the cast's illustration built from the order's totals, and all dialogue belongs to the cast.*

Ines saves the last replay of the week for the Monday after it, 2 November, at 4:30 p.m., when the desk is tired enough to be honest. She chooses an equity firm on purpose. "Credit people think this can't happen to them because their machines are slow," she says. "This machine was fast. What cost the money was how slow everything around it was." Chapter 26 told the same morning as a story about specifications, a deployment nobody reviewed and an invariant nobody wrote down. Tonight's question is a different one: when a machine starts saying yes to the whole market, who is allowed to make it stop, and what does stopping mean?

**The week before.** NYSE's Retail Liquidity Program was due to start on 1 August 2012, and Knight Capital changed its SMARS router to take part. SMARS was, in the order's words, "an automated, high speed, algorithmic router" that took "parent" orders from the rest of Knight's platform and sent "child" orders to venues. Beginning on 27 July, Knight deployed the new code in stages, a few servers a day. The new code replaced old code for a functionality called "Power Peg," which Knight "had discontinued using many years earlier," and it reused the flag that had once switched Power Peg on. One of Knight's technicians "did not copy the new code to one of the eight SMARS computer servers." No second technician reviewed the deployment, and no written procedure required one.

Ines reads one more paragraph aloud, because it is the one Kaz will care about. Power Peg used to stop sending child orders once a cumulative-quantity function said the parent was filled. In 2005 Knight moved that function to an earlier point in the code and did not retest Power Peg afterwards.

"So the eighth server has a loop with no exit condition," says Kaz, "and a flag that now means 'enter the loop.'"

"Waiting for Wednesday," says Ines.

**Before the open.** On 1 August, beginning at about 8:01 a.m. Eastern, an internal Knight system began generating automated e-mails, called "BNET rejects," that referenced SMARS and described an error as "Power Peg disabled." It sent 97 of them to a group of Knight personnel before the 9:30 open. Knight "did not design these types of messages to be system alerts," and the order says personnel generally did not review them when they arrived. They were sent in real time, they were caused by the deployment failure, and the order calls them a potential opportunity to find and fix the problem before the market opened.

Hana, who is on the rota again and has been since the cold open, says the number back to herself. "Ninety-seven." Five days ago she sent one message, "refresh queue 38 and climbing," that was read by nobody, and she has been thinking about it since. "I sent one. They sent ninety-seven, and it made no difference how many."

"Every one of them went to someone who wasn't expecting it," says Ines. "That's the definition of a message nobody reads."

One more fact from before the open matters, and Theo finds it, because it is the kind of exception a credit lawyer would have found. Knight did have a hard limit in SMARS: it capped the limit price of a parent order, and so of its child orders, at 9.5% through the national best bid or offer. That control did not apply to the 212 orders in question, which Knight received before the open and intended for the opening auction at each stock's primary exchange. "The one covenant they had," Theo says, "had a carve-out for exactly this basket."

**The open, and the card.** Ines starts the clock at 9:30. On the desk's big screen she has built a position monitor from the order's totals, a gross long and a gross short that grow, in her illustration, the way the order says they grew: steeply. The 212 parent orders begin reaching the eighth server. The seven servers with the new code handle their orders correctly. The eighth sends child order after child order, each parent's children routed without regard to how many shares have already been filled, because the part of the system that knew the parents were filled was not telling SMARS.

At 9:34 she stops the clock. The screen shows a long position and a short position, each already in the hundreds of millions on her illustration, and both still climbing when the clock froze. She deals a card to each of them.

#### Decision point: 9:34 a.m., 1 August 2012

*You run the desk. The position screen is building. Write who may pull the plug, what "pulled" means on the venues, and how you verify it.*

Kaz writes first, quickly, the way Kaz writes anything that looks like an engineering question. *Who: me, or whoever owns the router. Pulled: set the strategy's enabled flag to false. Verify: the flag reads false.*

Theo reads Kaz's card upside down and asks the question that turns out to be the evening's. "When you set the flag, do the orders already on the venues die with it?"

Kaz thinks about it for longer than they would like. "No. The flag stops new child orders. The ones already sent are resting on other people's matching engines. They live until they fill, expire or are cancelled, and a flag in our router cancels nothing."

"So the button stops the machine and leaves its orders behind," says Theo.

Mags has written three words. *Unplug the phones.* "In 1998, when a trader went wrong, the head trader pulled the jacks out of the turret. Nobody could buy anything, including the people who should have been buying. Crude. Worked."

Hana writes about verification, because that is where her week has been. *Watch the position screen stop growing.*

Ines collects the cards. "Kaz, your card is what ROBO builds when you tell it to add a kill switch. Mags, yours is right in the one way that matters: it acts on the venues, not on your own code. Pulling the jacks is a disconnect, and on an electronic venue a disconnect plus cancel-on-disconnect is the nearest thing to a button that actually takes your orders out of other people's books. Theo asked the question that decides whether a kill switch is a kill switch." She turns to Hana. "And yours is the hardest, because the screen you'd watch is the screen they had."

She reads the order's description of it. Knight's primary risk monitoring tool, PMON, was a post-execution position monitor. Senior personnel saw a large volume of positions accruing in an account called the 33 Account at the open. PMON was not linked to order entry, so nothing stopped orders when capital thresholds or gross position limits were exceeded. It relied entirely on human monitoring, it generated no automated alerts about the firm's exposure, and it did not display the limits, so the person watching had to know them. During high-volume events it ran late, and its reports were inaccurate. The 33 Account itself had a \$2 million gross position limit, and the limit was connected to no automated control at all.

"Verification can't be your own screen," Ines says. "It has to be the venues telling you that your open-order count is zero."

**What happened next.** She restarts the clock. The order is plain about the next forty minutes. Knight had no supervisory procedures for incident response, so it relied on its technology team to find and fix the problem in a live market. While they worked, "Knight remained connected to the markets and continued to send orders." In one attempt at a fix, Knight uninstalled the new code from the seven servers where it had been deployed correctly. That made things worse: incoming parent orders now woke the Power Peg code on those servers too.

Theo puts his pen down. "They made a deployment to fix a deployment."

"In a fire," says Ines, "the only safe action is the one that can only say no. Changing the code is saying yes to something you haven't tested, at the worst possible moment."

The rest is arithmetic, and the order does it. For the 212 incoming parent orders, SMARS "routed millions of orders into the market over a 45-minute period, and obtained over 4 million executions in 154 stocks for more than 397 million shares." For 75 of those stocks Knight's executions were more than 20% of the volume and contributed to moves of more than 5%; for 37, the moves exceeded 10% and Knight was more than half the volume. When the orders stopped, Knight was net long about \$3.5bn in 80 stocks and net short about \$3.15bn in 74. It "lost over \$460 million," had net capital problems, and in October 2013 agreed to a civil money penalty of \$12mm. A footnote in the order adds the detail Mags likes best: Knight did have automatic shutdown, by P&L limit, for certain strategies of one of its trading groups. It had a stop-loss for some of its traders and none for its router.

Theo tries to translate it into credit, which is the only way he can feel it. A credit desk has no router spraying child orders; its fast yes is the auto-responder. Suppose the fourth server of his second week had not been caught at 7:52, and had answered every high-yield inquiry three-eighths through the rest of the desk all day.

"It wouldn't be four million executions," says Kaz. "Forty fills, perhaps."

"Forty fills of two million at three-eighths is three hundred thousand dollars," says Mags, who does this kind of arithmetic in her head out of spite. "And the clients would remember it longer than the money."

"And every one of the forty would be someone who knew," says Ines. "Knight's machine traded with everyone in the market. Ours would trade only with the people who ought to worry us. Smaller pot, worse table."

**The grade.** Ines grades the cards against the four tiers of §27.7.1, which is to say against four lines that did not exist that morning. *Tier 2*, version skew, would have refused to open with one server out of eight on different code; it is Hana's 7:52 checksum on 29 September, in a bigger building. *Tier 1*, a child-to-parent fill-ratio test, would have fired within seconds, because Power Peg kept sending child orders without counting fills, and the order notes that Knight had no control comparing orders leaving SMARS with those that entered it. *Tier 0*, cumulative notional caps per strategy enforced at the gateway, would have stopped the position long before \$3.5bn; the \$2 million limit on the 33 Account shows that someone had thought of a number and wired it to nothing. And *authority* would have answered the question nobody answered for 45 minutes: who is allowed to pull the plug, and does pulling it actually disconnect? Kaz's card fails all four. Mags's card passes Tier 0 by other means. Theo's question is the authority row in one sentence. Hana's card, amended to "the venues report zero open orders," is how you know.

Kaz has one more question, and it is about Tier 1. "If the CUSUM had been there, why not set its line low, at two, so it trips on the first few bad fills?"

"Because then it trips every morning on noise," says Ines, "and by the third week someone turns it off, or learns to re-arm it without reading why. A false alarm every five trading days is a number a desk will live with. One a day is a number it will route around. The detection delay is what you pay for that tolerance, and it grows only with the log of the quiet time, so you can afford a lot of quiet. Knight's problem wasn't a line set too high." She taps the frozen screen. "It had no line."

#### Long Scene: The default field, 11 August 2020

*The desk was not a lender of record in Revlon's 2016 term loan and received nothing on 11 August 2020; the cast argues over the public record. Facts come from the Second Circuit's opinion in Citibank, N.A. v. Brigade Capital Management (No. 21-487, 8 September 2022) and Revlon's annual report for 2020. People at Citibank and its contractor appear only by role, as the opinion describes them; no words are put in their mouths.*

On Wednesday 4 November it is Theo's turn to choose the replay, and he chooses the one from his own world. "Knight was a machine that could say yes and nothing could say no," he says. "This one is three people and a screen, and the yes was a default nobody chose."

**May 2020: the collateral walks.** He starts where an RSSG banker would, with the documents. Revlon's 2016 term loan was a seven-year, \$1.8bn syndicated facility with Citibank as administrative agent, maturing in September 2023. On 7 May 2020 Revlon signed a new BrandCo credit agreement, with Jefferies as agent and holders of the 2016 loan as its lenders: \$815mm of new-money term loans, a \$950mm roll-up commitment that let 2016 lenders swap their loans at par into 2025 paper, and a small junior roll-up. Elizabeth Arden and other brand intellectual property moved into BrandCo subsidiaries that did not guarantee the 2016 loan. Lenders who joined moved up. Lenders who stayed in the 2016 loan kept a claim whose best collateral had left the building. By August, the opinion records, the 2016 loan was trading between 20 and 30 cents on the dollar.

Kaz, who has been warned about drop-downs, nods at the right moment and asks nothing.

**11 August: a roll-up that had to pretend to be a payoff.** On 11 August five holders of the 2016 loan, all managed by Angelo Gordon, were rolling their positions into the new facility. In a roll-up the borrower pays the exchanging lender its accrued interest but not its principal; the principal becomes the new loan. For administrative convenience Revlon decided to pay accrued interest to *all* the 2016 lenders that day, although none was due to the ones staying behind, and it directed Citibank, as agent, to carry out the roll-up. The other lenders were not told it was happening.

Citibank's loan-operations team processed payments in a system called Flexcube, and the opinion describes "the easiest (or perhaps only)" way to enter the transaction there: as if Revlon were paying the 2016 loan off in full, so that every lender's accrued interest was paid, while the principal, about \$894mm, went to a "wash account," an internal account for cashless entries, so that the money never left the bank. The loan would then be rebuilt with the five roll-up holders gone.

Theo stops and draws two rows on the whiteboard, because this is §27.3 in an operations costume. "Their system couldn't write the fact 'five holders leave the 2016 loan, everyone else stays.' So it wrote 'everyone is repaid' and planned to un-write it afterwards. It's the overwrite master. To change one fact it had to tell a big lie for an hour and then take it back."

"And the lie had a wire attached," says Ines.

"Why not make the roll-up a transaction the system understands?" asks Kaz.

"Because roll-ups are rare," says Theo, "and nobody budgets for the rare case until it costs them nine hundred million dollars."

It did, because of a default. Most payments that Citibank sent through Flexcube went to third parties, so, in the opinion's words, the default option, "unless suppressed, causes any payment entered into the system to be transferred as a wire payment." The bank's own manual said how to suppress it for principal: "ALL of the below field[s] must be set to the wash account: FRONT [;] FUND [; and] PRINCIPAL." The transaction went through Citibank's "six-eye" procedure: a maker entered it, a checker verified it, and an approver, a senior manager, gave the final sign-off. Several members of the team, including the maker and the checker, were employees of Wipro working exclusively on Citibank matters. All three people believed that setting the PRINCIPAL field alone was enough. The maker set PRINCIPAL and not FRONT or FUND. The checker reviewed it and believed the principal was going to the wash account. The approver believed the same and approved.

Then the screen asked a question. When the checker took the final step, a warning appeared, which the opinion says was referred to as a "stop sign": "Account used is Wire Account and Funds will be sent out of the bank. Do you want to continue?" It showed no amount. It did not say whether the funds leaving the bank were the interest, which was meant to leave, or the principal, which was not, or both. Interest was meant to leave the bank, so the checker clicked yes.

Theo reads it the way he would read a closing checklist. "Three humans, one screen, one default," he says. "On every closing I worked on there was a funds-flow memo, forty wires on a spreadsheet, and three of us initialled every page. I used to think the initials were why nothing went wrong. It was the bank on the other end, which rang to read back every amount over a million, digit by digit, before it released anything. The initials were the check. The read-back was the block."

"And if the read-back didn't match?" asks Kaz.

"Nothing moved. That was the whole point. Nobody can click past a phone call."

About \$894mm of principal and \$7.8mm of interest went out, and the principal was Citibank's own money, since Revlon had no intention of paying it. The amount each lender received matched, to the penny, the principal and accrued interest it was owed on the 2016 loan. The notices sent to lenders that afternoon mentioned only interest.

**12 August: a reconciliation, and a lawsuit.** Here Hana sits up, because the hero of the next morning is her kind of job. At about 9 a.m. on 12 August, as part of a routine reconciliation of the previous day's cash, looking for "cash breaks" between expected and actual debits and credits, the checker found discrepancies in very large amounts. Within the hour the bank knew the principal had gone. That afternoon, at about 2:06 p.m., roughly twenty hours after the wire, UMB Bank filed a complaint against Revlon on behalf of 2016 lenders, alleging among other things that the May transaction had stripped their collateral and that an event of default had already occurred. The lenders had authorised it between 30 July and 10 August. Citibank began sending recall notices, asking the recipients to return the principal, at about 2:25 p.m.

"The most important control in the story," Hana says, "is a morning reconciliation."

"It usually is," says Mags. "Nobody makes a film about it."

Some recipients sent the money back. Others did not; Revlon's annual report for 2020 puts the principal not returned at about \$504mm, and Citibank sued the loan managers whose funds held it. On 16 February 2021 Judge Furman, in the Southern District of New York, held that New York's discharge-for-value rule (*Banque Worms*) let them keep it.

Ines cuts the replay there, the evening of 16 February 2021, with the money where Judge Furman left it, and turns to Mags.

"You've held a lot of loans at 25," she says. "Something like this lands in your account. What do you think it is?"

Mags has never held Revlon and says so first. "A borrower at 25 does not prepay at par on a Tuesday. Not three years early, not without the notice the agreement requires, not the day before my own lawyers sue it. When money arrives that the documents say can't arrive, it's somebody's mistake until proven otherwise. You ring the agent and ask."

Theo has the agreement's language from the opinion. Section 2.11(a), "Optional Prepayments," let Revlon prepay only "upon irrevocable written notice" to the agent three business days ahead, and the agent then had to notify each lender promptly. No such notice had come. "So the credit agreement had the control," he says. "Principal doesn't leave without a notice on file. It just wasn't wired to the payment screen."

#### Decision point: the agent's payment screen

Ines deals the card.

*You are designing the agent's payment screen. Write the field that defaults, the review that is a check, and the one that is a block.*

Kaz writes the most engineering card of the week. *Default: nothing leaves the bank unless a field says so explicitly; the wash account is the default. Check: the six-eye review, with the screen showing the amount and its parts. Block: any principal sent to an external account on a loan with no prepayment or maturity record on file is refused, with no override argument; only a second system holding the agreement's notices can release it.* "The stop sign with no amount on it is a pop-up you click through," Kaz says. "A warning is a question. A block is an answer."

Theo's card ties the block to the document. *Block: principal out only against a 2.11(a) notice in the register, received three business days earlier, with each lender's notification logged.* "That's a bitemporal fact," he adds. "The notice has a valid time, the payment date, and a knowledge time, when the agent received it. If the register can't answer 'did we know about a prepayment before we paid it,' the block has nothing to check."

Hana's card is about the check. *The check fails when the three reviewers share the same mistake. Make one of them check something different: the cash total against expected interest.*

Ines grades them together. The default should fail safe: on this desk the default for a quote is *not live*, and on an agent's screen the default for principal should be *not leaving*. A review is a check, and checks are correlated: three people who all believe one field is enough are one reviewer with three signatures, which is why Hana's version, a reviewer who compares a different number, is worth more than a fourth signature. The block belongs to Tier 0. It is a rule on the data (principal outflow against a notice on file), it fires before the money moves, and it takes no override argument, which is Kaz's card. And the data it reads is the security master's job: the lender register and the posting state of every amendment are facts with two time axes. The agent's question "who is a 2016 lender today" is query 1 of §27.3.3, and the five Angelo Gordon holders leaving the loan on 11 August is a knowledge-time event that the register should have recorded as one row, not as a payoff and a rebuild.

Then she plays the rest of the tape. The Second Circuit (Judges Leval, Sack and Park) vacated Judge Furman's judgment on 8 September 2022. Discharge-for-value did not protect recipients who were on inquiry notice, and these were: a full repayment of principal three years before maturity, without the notice the agreement required, from a borrower the market priced at 20 to 30 cents, arriving the day before the lenders' own suit; and they were not owed the money then. Rehearing was denied on 12 October 2022, and the money went back. Mags's sentence about Tuesdays turned out to be close to the court's reasoning, which she accepts without visible pleasure.

> **View From Another Seat.** *The administrative agent: a servant of the syndicate with a payments system built for the common case.* From the agent's chair, as the Second Circuit's opinion describes it, a roll-up for a handful of lenders is a servicing event, not a credit view. The agent does not own the loan. It moves the borrower's money to the lenders, keeps the register, and passes on notices. Its systems are built for the common case, and in Flexcube the common case was a payment to a third party, so the wire was the default. The unusual case, paying interest to everyone while principal stays inside the bank, had to be built from the common one by suppressing the default in three fields. The six-eye procedure existed and was followed; the manual existed and said the right thing; the warning screen existed and asked a question. Each control was present, and each passed the mistake along, because each depended on the same belief about one field. The agent's exposure was not Revlon's credit at all: the \$894mm was Citibank's own money the moment it left. For a systematic desk the agent's seat holds the data the desk most needs in an LMT and can least easily get, the register of who holds what and the posting state of each amendment, and it shows why that data deserves a knowledge-time column. An agent whose system can only say "everyone was repaid" for an hour has, for that hour, a register that lies.

The pop-up that cannot stop anything did not stay in loan operations. Ines closes with a coda from equities, because it is the same control in another costume.

**Coda: Citigroup, 2 May 2022.** As reported in coverage of the FCA final notice of 2024-05-22, a trader meant to sell a basket worth \$58mm, and an input error produced one worth \$444bn. Controls blocked \$255bn; \$189bn reached an algorithm; about \$1.4bn of shares sold on European venues before the trader cancelled, coinciding with a brief, sharp drop in several European indices. The FCA found no hard block that would have rejected the whole basket, a pop-up alert the trader could override without being required to scroll down, and real-time monitoring that was ineffective and so too slow to escalate. Fines from the FCA (£27.77mm) and PRA (£33.9mm) totalled about £61.6mm. "Same group, different building, same screen," says Kaz. "A question where there should have been an answer." The lesson fits in one line of the spec below: **a warning that can be clicked past is a suggestion, not a control.** The Tier-0 function takes no override argument.

### Specification for AI Implementation (kill switch)

**What ROBO built from the vague version.** Asked to "add a kill switch," ROBO added a button that set `enabled = False` in the pricing loop. Live quotes on the venues stayed live, because nothing cancelled them. The button worked perfectly and changed nothing, which is Knight's 45 minutes in one line. The spec: trip cancels everything in scope; Tier 0 has no override; a dead-man heartbeat trips Tier 2; anyone may trip; only two distinct humans plus a passing slow-path check may re-arm; and CUSUM run lengths are checked against Siegmund.

At 9:34 the question was whether the button cancelled anything. Knight, Revlon's agent and Citigroup reduce to a short list of checks that a machine can run without asking anyone's permission: a hard limit on each message, a sequential test on the stream of fills, a heartbeat on the plumbing, and a rule about who may turn things back on. Two of those are statistics, tuned the way Ines tuned the line at the end of the Knight replay, with the false-alarm interval stated. The other two are authority, and authority has to be code, because at 10:02 a.m. the engineer who wants to restart the quoter is always well meaning.

Listing 27.5 has two halves. The first checks the CUSUM arithmetic of §27.7.2. `siegmund_arl` is Siegmund's approximation, with the 1.166 shift added to the alarm level, and `simulate_arl` runs thousands of CUSUMs side by side on normal increments with a given drift until each crosses the level, then averages the alarm times. For a one-standard-deviation deterioration and a level of 5, the checks require about 938 fills between false alarms and about 10 fills to detect a real problem, with simulation agreeing within 10 percent. Moving the level to 6 must more than 2.5 times the quiet time while adding under 2.5 fills of delay.

The second half is `KillSwitch`, a state machine with two states, `ARMED` and `TRIPPED`. `pre_trade` is Tier 0. It refuses everything once tripped, throttles message rate over a one-second window (the only check that trips the whole switch), and then tests price sanity, a collar around the reference price, a maximum order size and a maximum live notional. It takes no override argument, so a caller who passes one gets a `TypeError`. `check_deadman` trips Tier 2 when the heartbeat is older than the limit. A trip cancels every live order and clears any re-arm votes. `trip` lets anyone on the allowed list do it, while `rearm` accepts only listed humans, counts distinct voters, and succeeds only with two of them and a passing slow-path check. The checks include a 444,000mm basket stopped by the order-size limit, a 105 bp spread read as 105 points stopped by the collar, a monitor denied the right to re-arm, and one human voting twice still counting once.

It is the reference the production gateway is tested against, not the gateway itself. The edge that bites is the message-rate trip: `pre_trade` trips the switch and cancels live orders, but returns only `(False, "message_rate")`. The cancelled order IDs are not in that return value, and the log records the tier and reason without them. Whatever sends cancels to the venues must be driven by the state change, not by the answer to the order that happened to cross the line.

*The full listing is [Listing 27.5 in Appendix F](#code-27-5).*

## 27.8 Observability, Deployment, and Resilience Beyond Your Walls

**Quant-Shop Life (fictional composite): eleven percent.** *A non-bank credit market maker's production rota, a Thursday in October. The firm, Tomasz and every number are invented. The quoted lines come from a public podcast about a different firm's business (Jane Street's* Signals and Threads, *Episode 20, with production engineer Liora Friedberg, 7 October 2024) and are used as an analogy, not as a description of credit practice.*

Tomasz is on rotation this week, which at his firm means roughly what Friedberg described at hers: "between a quarter and a third of your time you'll actually be on rotation," and not overnight on-call so much as being present "during the trading day" and "responding to issues that are popping up live." His firm streams investment-grade bonds against Treasury futures and credit ETFs, and the rota owns everything between the feed handlers and the venue gateways.

The first page arrives at 8:12: composite staleness above 90 seconds on twelve bonds. He opens the dashboard, and by the time it has loaded the composite has updated and the page has closed itself. At 8:19 the same page fires on nine bonds and closes before he has read the list. At 8:40 the p99 response time on one venue session crosses 400 ms for forty seconds. At 9:05 the TRACE lag crosses twelve minutes, which nobody at the firm can do anything about, and the page closes when the next print lands. By 10:30 he has acknowledged twenty-six pages and resolved none of them, because none of them needed resolving. Friedberg's description fits exactly: "pages will open and close and you did nothing to resolve them," and each one takes up a little space in his head.

At 10:45 he builds the report her episode describes engineers building, the one that asks "What percentage of alerts are we actually actioning?" He pulls ninety days of page history from the alerting system's log, 4,180 pages, and for each one checks whether anybody did anything within fifteen minutes: a ticket, a configuration change, a manual pull, a restart. Four hundred and sixty did. That is 11%. Most of the rest closed themselves inside five minutes. The composite-staleness page alone accounts for 1,900 of them and was actioned fourteen times. At the other end of the chart sits the hedge-heartbeat page, a gap of more than 400 ms in the Treasury futures feed's sequence numbers. It fired six times in ninety days and was actioned six times: twice for an exchange-side problem, three times for the firm's own multicast line, once during a vendor upgrade.

He is tempted to tidy everything, and does not. He writes one change ticket, moving the composite-staleness threshold from 90 to 240 seconds for bonds that print fewer than five times a day on TRACE, whose composites update slowly by nature, and attaches the report. Projected effect: about twenty-one pages a day become about three. In the ticket he names the page he is leaving alone, the hedge heartbeat, and why: six of six actioned, the one alarm on the list whose false-alarm rate is not worth buying down. His lead approves at 2:30 after asking a single question, what the old setting caught that the new one misses. Tomasz's answer is that a dead composite on a liquid bond still pages at 90 seconds, and on an illiquid bond the next inquiry would surface it within minutes anyway.

At 4:10 the heartbeat page fires on a 1.1-second gap in the futures line. The gateway has already pulled every quote that references TY by the time he looks. He confirms that the quotes came back only after the slow path had repriced them, notes the gap in the log, and closes the page four minutes after it opened. He goes home with nothing interesting to say about his day, which at his firm is the measure of a good one.

The report Tomasz built is the CUSUM's false-alarm interval measured in the wild. Knight's 97 unread e-mails, Hana's unread "refresh queue 38" and the composite page that cried wolf 1,900 times are one calibration problem: an alarm has a false-alarm interval and a detection delay, and when the false alarms come every few minutes, the people who should act learn not to.

Back on the desk, on Friday 6 November, Ines walks Theo along the wall of screens the desk calls the ops plane, the part of the building that watches the building.

The first screen answers the question the 4 p.m. risk meeting asked about the cold-open fill: why did we bid that? Every input carries `known_at` (§27.2) and every decision is a pure function of the knowledge-time snapshot plus the code and configuration version, so Hana can replay 1:59:58 to 2:00:02 on 28 October bit for bit, and "why did we bid that?" has an answer that is not a shrug. Configuration is code: versioned, checksummed, and compared across every server before the open. The Tier-2 version-skew check that stopped the fourth server on 29 September is just this comparison with teeth.

The second screen holds the number Ines thinks matters most, and it is not latency. It is the gap between the paper portfolio and the dollar portfolio.

> **[SOURCE EXTRACTION]** *Paleologo_Advanced_Portfolio_Management p.145:* "If these skills are there pro forma in a paper portfolio, but are not realized in the dollar portfolio, then we can be assured that this has to do with the deployment of the strategy – maybe its capacity is lower than we thought – or with the execution of the strategy itself"
>
> **Annotation.** Our analysis: Paleologo writes this about a PM's skill, but it is also the definition of an infrastructure bug. Paper minus live, attributed by component (fill probability, cost model, latency-driven pick-offs, unfilled residuals from §27.4), is the desk's integration test, and it should be a dashboard line, not a quarterly post-mortem. The departure for credit is that the paper portfolio must be simulated with *provenance-typed* fills (§27.2). A paper book filled at composites will always beat the live book, and the gap will be blamed on execution when it is really the data.

Theo asks the obvious question: a paper portfolio has no dealers on the other side, so how does a paper RFQ get filled? The attribution needs a fill rule that is written down, and the desk's is this. *(Illustrative; only as good as the desk's own RFQ log.)* Each paper child order gets four draws. *Whether:* the fill-probability service of §27.4 returns $\hat p$ for the order's bond, size, venue, protocol and regime, and the order fills if a uniform draw falls below it. *Who:* given a fill, the winning dealer is drawn from the dealers the live router would have asked, weighted by their logged win shares in the same liquidity and size bucket. *At what level:* the fill is that dealer's logged markup to the composite, not the composite itself (the provenance rule of §27.2, applied to simulation). *Against what cover:* the draw records the second-best response from the logged cover gap, and a one-dealer panel is flagged as having none. A failed or partial draw runs the same state machine and emits the same residual-risk event as a live one. Draws are seeded by order id and use only log rows whose `known_at` precedes the order, so the run replays bit-for-bit. The payoff is attribution: a paper-live disagreement on an order belongs to the draw that differed, and what no draw explains is latency, whose pick-offs (§27.6) stay their own line.

The third screen is Kaz's, and it tracks every change on its way to production. Knight's eighth server is the archetype of what goes wrong there, and the modern one is outside the trading stack entirely. On 2024-07-19 a defective CrowdStrike content update for Windows hosts disrupted airlines and banks, and SGX's clearing arm suffered an operational failure of five hours and six minutes (Risk.net). A kernel-mode agent your security team installed is part of your latency and availability budget, whether or not anyone told the desk. So the desk deploys in rings, with canaries, for *every* change that touches a trading host, including vendor agents, and a deployment kill switch halts a rollout when the canary's markouts, rejects or latency drift. Beside it hangs the rule the desk took from Knight's 97 e-mails and Tomasz's report: **an alert without an owner and an action is a log line.** Every alert names who acts, what they do, and the deadline, and RTS 6 Art. 16's five seconds is the default for anything that can lose money.

The last screen is not a screen but a whiteboard list of everyone outside the building the desk depends on, each with a named fallback, and Ines explains it with three dates. On 2023-11-08/09, LockBit ransomware hit ICBC Financial Services, the US broker-dealer arm of ICBC. BNY Mellon, its Treasury settlement agent, disconnected it and settled its trades manually; ICBC FS owed BNY about \$9bn in unsettled trades until the parent injected capital (Reuters and other coverage). On 2015-04-17, Bloomberg terminals went dark for several hours from about 8:30 a.m. London, and the UK Debt Management Office postponed a gilt operation of about £3bn, citing "ongoing issues with the third-party platform supplier." And the composite and venue layer is consolidating: ICE agreed on 2026-07-29 to buy MarketAxess. Each case is the same lesson. A desk's fastest system is bounded by its slowest counterparty's recovery plan, which is why every external dependency on the whiteboard (settlement agent, chat and pricing terminal, composite vendor, hedge venue) has a named fallback and a Tier-2 trigger that says what happens to live quotes when it disappears.

Mags listens to all of this with her arms folded. "Back in my day the kill switch was the head trader unplugging the phone bank, and the dead-man switch was the head trader going to lunch. Nothing traded until he came back." A pause. "Fine. Yours doesn't go to lunch."

## 27.9 Desk Debrief

**Finder.** Where each tool lives in the chapter: the equation, the box that builds the intuition, the scene where someone used it or broke it, and the code.

| Concept | Eq. | Intuition (box) | Judgment (scene) | Code |
| :-- | :-- | :-- | :-- | :-- |
| Two clocks | none; the two-path diagram and Figure 27.1 (§27.1) | The cold open's second and a half (§27.0); the non-bank market maker's seat (§27.1) | Kaz's "make everything fast" against Mags's "make nothing fast" at the whiteboard (§27.1): only the slow path may say yes, and only the path that says no has to be fast | The Spec You Hand the Robot, items 4–5 |
| E-folding time | $\alpha(\ell) = \alpha_0 e^{-\ell/T}$; speed is worth $\Delta\ell/T$ of the edge (§27.1.1) | The cooling coffee, §27.1.1 (1% of a 63-day signal is 0.6 of a day; of a 79 µs race, 0.8 µs) | Theo reads the table top to bottom and the cold-open card is graded (§27.1.1): a pricing engine four times faster buys nothing against a jump | none |
| Provenance and late data | loss to lateness $1 - G(L)$ at watermark $L$ (§27.2.3) | The mail bag that closes on time, §27.2.3 | Ilse's three rows before 7:30 (§27.2.1): the duplicate is marked, not deleted, and the row nobody can classify is filed rather than guessed | Listing 27.1 |
| Bitemporal master | fact tuple $f$ and as-of query $Q(k, a;\ t^{v}, t^{k})$; (I1), (I2) and the theorem (§27.3.2) | The newspaper archive and the wiki, §27.3.2 | Theo's "prescient" Serta backtest (§27.3) and Mags's question about her own P&L report (§27.3.3): live risk asks query 1; the backtest, the explain and the post-mortem ask query 2 | Listing 27.2 |
| Order state machine and the pair | the state table: every terminal state other than `FILLED` is a risk event (§27.4.2) | The Pair, PB-01 (§27.4.2) | Hana and the "105" that was a spread (§27.4.2): fields checked as a set; a kill switch scoped to one leg of a pair manufactures beta, so its scope is the parent | none (Exercise 7) |
| Queue p99 | Little's $\bar N = \Lambda^{\text{q}}\bar W$; Pollaczek–Khinchine $\mathbb{E}[W_q]$; tail quantile $t_q$ (§27.5.1) | Queues in two parts, §27.5.1: one till, and the long bus gap | Kaz's "forty milliseconds" that nobody asked the p99 of, and Hana's "queue normal" (§27.0): sojourn by utilisation band, fed with the stress hour's load rather than the day's | Listing 27.3 |
| Fan-out | $1 - (1-p)^n$ (§27.5.1) | The relay team, §27.5.1 (100 legs: 63% slow; 150: 78%) | Ines reads the two budgets aloud (§27.5.2): a 150-line PT's p99 is each call's p99.993, which is why the fan-out gets hedged or bounded | Listing 27.3 |
| Trigger table | $\boldsymbol\beta_i^{\top}\Delta\mathbf H$ against $\theta_i$; joint and per-instrument rules; the cheap rule is safe (§27.6.1) | Two detours are never shorter than the straight road, §27.6.1 | The halt drill (§27.5.3): a quiet table can be a deaf one, so a silent hedge feed pulls quotes as a Tier-2 event | Listing 27.4 |
| Diffusion versus jump | Bachelier put $\sigma\sqrt{\Delta}\,[\varphi(x) - x\,\Phi(-x)]$ against $\pi\,(\lvert J_i\rvert - h_i)^{+}$ (§27.6.2) | The walk home from the bar, §27.6.2 (47 typical moves inside the half-spread) | The flash-rally replay (§27.6.3): pull on the first basis point; re-arm only when realised hedge volatility is quiet, at a wider $h$, on the evidence of the hedge tape | Listing 27.4 |
| CUSUM and the tiers | $G_k$ and $K_c$; Siegmund's ARL (§27.7.2); the tier table (§27.7.1) | Evidence that adds up and forgets, §27.7.2 ($c = 5$: a false alarm every 938 fills, detection in about 10) | Hana's 7:52 checksum (§27.7.1); Knight at 9:34 and Ines on why the line is not set at two (§27.7.3); the agent's payment screen (§27.7.3); Tomasz's eleven percent (§27.8): a threshold nobody acts on stops being a threshold | Listing 27.5 |

- **Two clocks, one desk.** The quote clock runs in seconds to minutes; the hedge clock runs in microseconds. Speed is worth $\Delta\ell/T$ of your edge, so buy it in proportion to $1/T$ of the information you act on, not in proportion to how much you enjoy hardware.
- **The fastest thing on the desk is the thing that says no.** The fast path compares precomputed numbers and may only pull. Only the slow path, which can be audited, may say yes again.
- **Every price says what it is and when you knew it.** `price_kind` plus `known_at`, or it does not get a badge. Labels, fills and cost targets come from prints and firm quotes only.
- **The security master is the credit agreement of the system.** Use internal surrogate keys, bitemporal rows and append-only knowledge time. Serta's 22 June 2020 is a test case, not an anecdote.
- **The p99 is the number the sniper trades against, and it is worst when the market moves.** Little, Pollaczek–Khinchine and fan-out turn "40 ms" into "1.5 seconds on FOMC day, and 78% of PTs slow."
- **The cheap trigger rule is safe by the triangle inequality, and it costs false pulls in a flight to quality.** Store dollar sensitivities, budget the threshold, and set a guard band above fixed-point and convexity error.
- **A kill switch is a stopping rule with two numbers attached.** The desk head picks the false-alarm interval, and the detection delay comes with it, growing only with its log. Anyone can trip, two humans re-arm, and nothing can be clicked past.
- **Silence is not safety.** A dead hedge feed, a missing eighth server or a counterparty in manual settlement is a Tier-2 event with a named owner and a five-second deadline.

### The Spec You Hand the Robot

```text
SYSTEM: two-clock quoting engine for a systematic credit desk. Implement exactly this; ask before guessing.

1. PRICE STORE. Every record: instrument_key (internal surrogate), value, price_type in {PRICE, SPREAD, YIELD},
   side, size_mm (USD mm par; flag TRACE-capped), price_kind in {TRADED, FIRM_QUOTE, INDICATIVE_RUN, EVALUATED,
   COMPOSITE}, source, event_ns, known_ns. Only TRADED and FIRM_QUOTE may be labels, fills or cost targets.
   Late records go to a correction stream; never overwrite. TRACE affiliate duplicates are MARKED, never deleted;
   tag regime {no_flag, flag_voluntary (from 2026-08-31), flag_mandatory (from 2027-08-02)}.
2. SECURITY MASTER. Bitemporal facts (key, attr, value, valid [from, to), known [from, to)); knowledge time
   non-decreasing; exclusion constraint per (key, attr). Backtests query as_of(valid <= t, known = t) only.
   Test: Serta 2016 first-lien loan as of 2020-06-23 known 2020-06-22 00:00 returns first_lien_pari.
3. LATENCY. Measure sojourn (arrival to response), not service time. Report p50/p99/p99.9 by utilisation band.
   Alert when the p99 at current load exceeds the trigger-table refresh budget.
4. TRIGGER TABLE (fast path). Per exposed quote i: side, hedge reference prices H_ref[j], beta[i,j] in bond points
   per hedge point, theta_i = h_i - m_i - guard (points), tau[i,j] = theta_ij / |beta[i,j]| with
   theta_ij proportional to |beta[i,j]| * sigma_j. Pull if any |H_j - H_ref_j| > tau[i,j] (or if the joint rule
   |beta_i . dH| > theta_i fires). Fixed point Q.16; guard >= rounding bound + convexity bound. Pull only;
   re-arm only by a new row from the slow path, gated on realised hedge volatility.
5. KILL SWITCH. Tier 0 (no override argument): price collar, PriceType sanity, max order, max live notional,
   message rate. Tier 1: CUSUM on 1-minute markouts, delta and c from config; log ARL0 and ARL1. Tier 2: version or
   config skew, hedge-feed heartbeat gap, clock fault, venue down -> pull all quotes referencing it. Tier 3:
   drawdown stop-loss. Any authorised human or monitor may trip; trip cancels everything in scope;
   re-arm requires two distinct humans plus a passing slow-path check. Every alert has an owner and a 5 s deadline.
6. TESTS. The asserts in blocks 1-5 of this chapter, plus the cold open: TY -6/32, HYG -14c must pull the bid.
```

### Exercises

1. **Kaz's engine on a CPI morning.** With $\mathbb{E}[S] = 40$ ms and $c_s^2 = 4$, find the utilisation $\rho$ at which the approximate p99 *waiting time* equals 500 ms. If the trigger-table refresh budget is 500 ms, what fraction of quote refreshes must be shed or batched when load rises from $\rho = 0.5$ to $\rho = 0.9$? Then rerun block 3 with $c_s^2 = 1$ and explain, in one sentence for the risk meeting, why "make the slow requests less slow" beats "make the average request faster."
2. **Add LQD and CDX IG to the table.** Derive $\beta_{i,\text{LQD}}$ by the method of §27.6.1, allocate $\theta_i$ across TY, LQD and CDX IG, and construct a move vector for which the per-instrument rule pulls and the joint rule does not. Using a covariance of your choosing (state it), estimate the false-pull rate by simulation, and show that it never misses a joint-rule pull.
3. **The J.Crew drop-down as rows.** Write the bitemporal rows for an IP transfer to an unrestricted subsidiary (Chapter 13), including the guarantor-map change and the event row. Which as-of query must a backtest of Chapter 25's covenant-flag signal use? What specifically goes wrong if the vendor's "point-in-time" file is valid-time only?
4. **Your PM says "never false-alarm."** Compute the CUSUM detection delay as $c \to \infty$, then explain the result to her using only poker terms. Then choose $c$ so that, at 200 fills a day and $\delta = 0.75$, false alarms average no more than one a month (21 trading days), and report $\text{ARL}_1$.
5. **ROBO and the zero-pick-off mandate.** ROBO receives the spec "make sure we never get picked off." Describe what it builds (hint: §27.6.2 has a closed form for the expected loss of a quote that is never shown). Then rewrite the spec with units, a loss budget per day, and boundary conditions so that the optimal policy is not "quote nothing."
6. **Kaz wants the callable-bond OAS model on the FPGA.** Write the one-paragraph memo declining the request. It should cite the convexity term, the re-synthesis cycle and the "table is data, logic is fixed" principle, and offer the alternative: stream callables from the slow path at a wider $h$, or not at all.
7. **PB-01 with one leg missing.** *(Fictional pair from Chapter 1-B; every number illustrative.)* Dov sends PB-01 as one parent order with two children: buy \$60mm Kestrel 6% 2030 at 96 (about 350 bp, spread duration 3.6) and borrow-and-sell \$39mm Halvorsen 7.25% 2029 at 90 (600 bp, spread duration 3.4), matched at inception on market-value DTS (about 72,600 on the long against about 71,600 on the short; face in \$mm × price/100 × spread duration × spread in bp, as in Chapter 1-B). The Kestrel child reaches `FILLED`. The Halvorsen child reaches `EXPIRED` at 4:58 p.m. because the locate came back empty. Compute the market-value DTS the pod now carries net, its CS01 in dollars per basis point, and what an overnight 10% proportional widening of high-yield spreads would cost it, using DTS's rule that spreads move in proportion to their level. Write the residual-risk event the parent order should emit, with its fields. Then name the tier of §27.7.1 that should have caught the position before the close, say why it is not Tier 1, and size the CDX HY hedge (a purchase of protection, which is a short in the index) that would hedge the surviving long inside one quote-clock cycle, stating the index spread duration and spread you assume. Finally, say in one sentence what that hedge leaves the pod holding that it never wanted: is it still a pair?

## 27.10 Sources and Links

### Deep-Dive Resource Graph

If only one item gets your commute, it is Brian Nigito on multicast: why electronic exchanges came to run on single-threaded programs and multicast networking, which is this chapter's thin, dumb fast path heard from the exchange's side of the wire. The rest are grouped by the section they feed.

**Podcasts**

- **"Inside Hudson River Trading's Blistering Token Burn"** (Bloomberg *Odd Lots*, 2026-06-05, feed date; the earlier episode, "How Hudson River Trading Actually Uses AI" with Iain Dunning, is 2025-10-31). A major market maker on token spend per employee, compute and memory bottlenecks and possible in-house chips: a firm's infrastructure budget and constraints, told aloud, for §27.6 and §27.8. https://omny.fm/shows/odd-lots/inside-hudson-river-tradings-blistering-token-burn ; https://omny.fm/shows/odd-lots/how-hudson-river-trading-actually-uses-ai
- **"Angana Jacob - Data as the True Competitive Moat (S7E26)"** (*Flirting with Models*, 2026-02-09). Data "sourced, cleaned, standardized, linked, and delivered" is the moat once models commoditise: the audio case for the provenance rule (§27.2.2) and the security master (§27.3). https://www.flirtingwithmodels.com/episodes/DLtqprallYi
- **"Multicast and the markets with Brian Nigito"** (*Signals and Threads*, Jane Street, 2020-09-23). Why electronic exchanges rely on single-threaded programs and multicast networking, from a veteran of early electronic exchanges; the feed handler's world for §27.2.1 and the single-writer logic behind §27.4. https://signalsandthreads.com/multicast-and-the-markets/
- **"Programmable hardware with Andy Ray"** (*Signals and Threads*, Ron Minsky with Andy Ray of Jane Street, 2020-09-09). FPGAs, hardware tooling and "the economics of FPGAs": the best audio primer for the trigger-table section (§27.6) and the build-versus-buy of hardware. https://signalsandthreads.com/programmable-hardware/
- **"State Machine Replication, and Why You Should Care with Doug Patti"** (*Signals and Threads*, 2022-04-20, feed date). Jane Street's Concord and Aria, built on state-machine replication for reliability, scalability and speed: a real-world instance of the deterministic order state machine of §27.4.2. The page renders by script; the feed carries the description and date. https://signals-threads.simplecast.com/episodes/state-machine-replication-and-why-you-should-care-with-doug-patti-ddqeDcTw
- **"Solving Puzzles in Production" with Liora Friedberg** (*Signals and Threads*, Ep 20, Jane Street, 2024-10-07). A production engineer on the intraday support rota, alerts that open and close by themselves, and the question "What percentage of alerts are we actually actioning?": the public account behind the eleven-percent vignette of §27.8, about a market maker's business rather than credit, and the same calibration as the CUSUM line of §27.7.2. https://signalsandthreads.com/solving-puzzles-in-production/
- **"Christian Hauff, Co-Founder of Quantitive Brokers"** (sic, as titled; *Alpha Exchange*, host Dean Curnutt, 2019-02-14). The trader's dilemma of executing now or working the order, implementation shortfall, and the firm's research on the Treasury flash rally of 15 October 2014: an execution specialist's view of the morning §27.6.3 replays against a trigger table. https://alphaexchange.simplecast.com/episodes/christian-hauff-co-founder-of-quantitive-8968b07c

**Practitioner Writing**

- Kevin McPartland, "What the buy side wants from their bond dealers," Coalition Greenwich blog, 2024-02-13. https://www.greenwich.com/blog/what-buy-side-wants-their-bond-dealers
- Fleming, Johansson, Keane and Meyer, "From the Vault: A Look Back at the October 15, 2014 Flash Rally," *Liberty Street Economics*, 2019-10-15. https://libertystreeteconomics.newyorkfed.org/2019/10/from-the-vault-a-look-back-at-the-october-15-2014-flash-rally/
- Ahmed, Chaboud, Dobrev, Fiorica, Fleming, Keane, McMorrow, Prasanna, Schaumburg, Wuerffel and Yang, "Just Released: The U.S. Treasury Market on October 15, 2014," *Liberty Street Economics*, 2015-07-20. The summary of the joint Treasury, Fed, SEC and CFTC staff report, and the primary-source pointer for the replay in §27.6.3. https://libertystreeteconomics.newyorkfed.org/2015/07/just-released-the-us-treasury-market-on-october-15-2014/
- The DESK, "Exclusive: What do buy-side traders think about Citadel's entry into credit?" (2023-07-19) and "Market structure: The alternatives in market-making" (2023-01-23). The non-bank market maker's seat in §27.1, with the buy-side reaction and Virtu's early fixed-income remarks as the trade press reported them. https://www.fi-desk.com/exclusive-what-do-buy-side-traders-think-about-citadels-entry-into-credit/ ; https://www.fi-desk.com/market-structure-the-alternatives-in-market-making/
- Virtu Financial, Annual Report on Form 10-K for fiscal year 2015: the strategy-freeze-and-cancel control quoted in §27.1. Title only.
- Man Group papers on systematic credit (2022 and 2023), cited from the shelf as Man_Quantitative_Credit_Alpha_Early_Mover_2022 and Man_Revolutions_in_Credit_Trading_2023.
- Arista Networks, 7130 Series product documentation (Layer 1+ devices; vendor latency specifications). Title only.
- AMD and Exegy, STAC-T0 tick-to-trade benchmark announcements (2024). Vendor claims; title only.
- The DESK coverage of auto-quoting, no-touch rates and credit futures blocks (2025-10-08, 2026-10-08, 2026-10-16), as cited in the Trend Watch boxes. Title only.
- **"The LMAX Architecture"** (Martin Fowler, 2011-07-12). A trading platform whose Business Logic Processor handles "6 million orders per second on a single thread", in memory, with event sourcing and lock-free Disruptors: the canonical open description of a single-writer, replayable core; read before §27.3-§27.5. https://martinfowler.com/articles/lmax.html
- **"Can you design a chip? Announcing the protocol emulator ASIC competition"** and **"Results from the ASIC puzzle"** (Jane Street blog, 2026-09-10 and 2026-10-02). A market maker inviting chip designs ("we'll pay to fabricate our favorite designs"), then a puzzle on reverse-engineering a chip from its layout: a dated sign that a top trading firm is openly working on custom silicon; read it as a marker of where the latency frontier sits, not as a design source (§27.6). https://blog.janestreet.com/protocol-emulator-asic-competition/ ; https://blog.janestreet.com/asic-puzzle-results/ (an earlier marker on the same road: "Advent of FPGA," 2025-11-24, https://blog.janestreet.com/advent-of-fpga-challenge-2025/ )
- **"Knightmare: A DevOps Cautionary Tale"** (Doug Seven, 2014-04-17). The 1 August 2012 deployment failure told as an engineering story (deployment, feature flags, humans reading checklists); check its figures against the SEC order listed under Regulation, Data & Code before quoting (§27.7.3). https://dougseven.com/2014/04/17/knightmare-a-devops-cautionary-tale/

**Academic Papers**

- Matteo Aquilina, Eric Budish and Peter O'Neill (2020), "Quantifying the High-Frequency Trading 'Arms Race': A Simple New Methodology and Estimates," FCA Occasional Paper 50; later published in the *Quarterly Journal of Economics*. https://www.fca.org.uk/publication/occasional-papers/occasional-paper-50.pdf
- Eric Budish, Peter Cramton and John Shim (2015), "The High-Frequency Trading Arms Race: Frequent Batch Auctions as a Market Design Response," *Quarterly Journal of Economics* 130(4).
- Jeffrey Dean and Luiz André Barroso (2013), "The Tail at Scale," *Communications of the ACM* 56. https://research.google/pubs/the-tail-at-scale/
- John D. C. Little (1961), "A Proof for the Queuing Formula: L = λW," *Operations Research* 9(3).
- J. F. C. Kingman (1961), "The Single Server Queue in Heavy Traffic," *Proceedings of the Cambridge Philosophical Society* 57.
- E. S. Page (1954), "Continuous Inspection Schemes," *Biometrika* 41; Gary Lorden (1971), "Procedures for Reacting to a Change in Distribution," *Annals of Mathematical Statistics* 42; George Moustakides (1986), "Optimal Stopping Times for Detecting Changes in Distributions," *Annals of Statistics* 14.
- David Siegmund (1985), *Sequential Analysis: Tests and Confidence Intervals*, Springer (the ARL approximation used in §27.7).
- Lockwood, Gupte, Mehta, Blott, English and Vissers (2012), "A Low-Latency Library in FPGA Hardware for High-Frequency Trading (HFT)," IEEE Symposium on High-Performance Interconnects.
- Richard T. Snodgrass (1999), *Developing Time-Oriented Database Applications in SQL*, Morgan Kaufmann (the bitemporal model of §27.3).

**Regulation, Data & Code**

- SEC, *In the Matter of Knight Capital Americas LLC*, Release No. 34-70694 (2013-10-16). https://www.sec.gov/litigation/admin/2013/34-70694.pdf
- *Citibank, N.A. v. Brigade Capital Management, LP*, No. 21-487 (2d Cir. 2022-09-08), the opinion vacating the discharge-for-value judgment, and the source for every fact about the 11 August 2020 wire in §27.7.3. https://www.courthousenews.com/wp-content/uploads/2022/09/21-487_complete_opn.pdf
- Revlon, Inc., Annual Report on Form 10-K for 2020 (the BrandCo transaction and the amounts not returned after the wire, §27.7.3). https://www.sec.gov/Archives/edgar/data/887921/000088792121000003/rev-20201231.htm
- SEC, Risk Management Controls for Brokers or Dealers with Market Access (Rule 15c3-5), Release No. 34-63241 (2010-11-03). https://www.sec.gov/rules/final/2010/34-63241.pdf
- SEC press release 2014-260, adoption of Regulation SCI (2014-11-19). https://www.sec.gov/news/press-release/2014-260
- Commission Delegated Regulation (EU) 2017/589 (MiFID II RTS 6, algorithmic trading). https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32017R0589
- FINRA Rule 4590, Synchronization of Member Business Clocks. https://www.finra.org/rules-guidance/rulebooks/finra-rules/4590
- FINRA TRACE overview and specifications. https://www.finra.org/filing-reporting/trace (Regulatory Notices 25-17 and 26-16: title only.)
- OpenFIGI symbology and mapping API. https://www.openfigi.com/ and https://www.openfigi.com/api
- CourtListener REST API, for the docket of *Dinosaur Financial Group LLC v. S&P Global Inc.*, S.D.N.Y. No. 1:22-cv-01860. https://www.courtlistener.com/help/api/
- This chapter's reference implementation: `ch27_desk_system.py`, blocks 1–5 above (provenance and dedupe, bitemporal master, queueing, trigger tables, kill switch).

<!-- STATUS: COMPLETE -->
