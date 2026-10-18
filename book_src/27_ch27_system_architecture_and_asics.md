# Chapter 27: System Construction, Low-Latency Infrastructure & ASICs/FPGAs


## 27.0 Cold Open: The Fastest Thing on the Desk

2:00 p.m., an FOMC Wednesday. Theo has a streaming bid live on an all-to-all portal: \$3mm of a BBB-rated 10-year industrial bond, priced off a composite, skewed by the desk's inventory model, refreshed by a pricing engine Kaz built *(illustrative)*. In his other ear, a lender call for a name the desk owns has reached the part where counsel to the Ad Hoc Group says, in unison, that they are "not in a position to comment at this time."

The statement hits the wires. TY futures drop six 32nds. HYG drops 14 cents. Theo's bid does not move.

"Your bid," says Ines, not looking up, "is now the best price in the market. That is never a compliment. Who just sold to you?"

The fill arrives before Theo can answer. Three million, done.

"The pricing engine averages forty milliseconds," Kaz offers.

"And the p99?"

Kaz types. Pauses. Types again. "About a second and a half. Under load. Which this is."

"So for a second and a half," Ines says, "you wrote a free put on a BBB bond to everyone in America with a futures screen, and someone with a faster screen exercised it. Nice hand. Terrible table."

Mags, from behind a stack of offering memoranda: "In 1998 the equivalent was leaving your phone off the hook while the Fed spoke. At least the guy who hit you had to dial."

Two seconds later the engine catches up and drops the desk's bid by three-eighths of a point. Theo has bought the bond 3/8 above where his own system now wants to buy it. Against the new mid, the markout is about −0.185 points, roughly \$5,500 on the position *(illustrative; derived in §27.6)*. That is less than an hour of lender-call billing and more than anyone wants to explain at the 4 p.m. risk meeting.

Theo takes the USB stick with his 13-week cash flow model out of his pocket, looks at it, and puts it back. "At PJT the dangerous moment was the lender call."

"Here," says Ines, "it's the second and a half after TY moves and before you do. So: how fast does each part of this desk need to be, how do you prove it, and what's the one thing that has to be faster than everything else?"

ROBO, asked last week to "make the system faster," has opened a ticket requesting an FPGA for the compliance archive.

By the end of this chapter you will be able to draw the two-clock architecture of a systematic credit desk and say which component lives on which clock. You will be able to design a bitemporal security master that survives a liability-management transaction without lying to your backtest, and turn "our pricing engine takes 40 ms" into a queueing statement with a p99 attached. You will derive the fixed-point trigger table that pulls a bond quote when TY, HYG or a credit future moves, and prove when its cheap version is safe. You will specify a kill-switch hierarchy with an explicit false-alarm rate and detection delay, and hand ROBO a spec it cannot misread. The short version: **the fastest thing on a credit desk should be the thing that says no.**

## 27.1 Two Clocks: Why Credit Latency Is Not Equity Latency

Ines draws two clocks on the whiteboard. One has a minute hand. The other has no hands at all, just a label: "µs."

The **quote clock** ticks in seconds to minutes. An RFQ arrives. The desk identifies the bond, looks up a composite, adds an inventory skew (Chapter 18) and an adverse-selection margin (Chapter 3), and answers inside a venue timer measured in minutes. The public record of what happened, the TRACE print, can arrive up to 15 minutes later with large sizes capped: FINRA confirmed in Regulatory Notice 25-17 (2025-12-04) that it is not moving forward with a one-minute outer limit, so 15 minutes stays (§27.2). Nothing on the quote clock improves when you shave a nanosecond.

The **hedge clock** ticks in microseconds. The instruments a credit desk hedges with trade on exchange matching engines: Treasury futures, HYG and LQD, CDX through its electronic venues, and since June 2024 listed credit index futures. On the London Stock Exchange, the FCA's study of latency-arbitrage races found that races are "extremely fast (the modal race lasts 5-10 millionths of a second)" (Aquilina, Budish and O'Neill 2020, FCA Occasional Paper 50). The moment the desk shows a firm bond price to the street, on an all-to-all venue or a streaming portal, that price becomes a free option written to anyone who sees the hedge clock move first. That is the cold open in one sentence.

There are two lazy architectures. The first is "make everything fast," which is expensive and pointless for a quote clock measured in minutes; it ends with ROBO's FPGA for the compliance archive. The second is "credit is slow, relax," which is how you get picked off on every streaming quote on every FOMC day. The right architecture is a **two-speed system**:

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

The FPGA does not price bonds. It compares numbers that the slow path computed and wrote into a table. The slow path can be clever, slow, and wrong in interesting ways; the fast path must be simple, fast, and wrong only in the safe direction. Kaz asks whether "fast path" is a defined term with a negative pledge. Ines says it should be: nothing else gets to put logic in it.

### 27.1.1 The price of a microsecond, derived

How fast is fast enough? The answer depends on what you are reacting to, and it can be derived in four lines.

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

Read the table vertically and you get the chapter. A trend book that executes a day late loses about $1 - e^{-1/60} \approx 1.7\%$ of its information ratio, which is real money and worth a careful execution process. The same book gains nothing from a microsecond. A stale streaming quote that waits 1.5 seconds for the pricing engine to notice TY loses $1 - e^{-1.5/(79\times 10^{-6})}$ of the edge, which is a number your calculator will display as 1. One desk, nine orders of magnitude, and a single budget meeting in which all of them are called "latency."

The table also explains the cold open without any microstructure jargon. Theo's half-spread bought him protection against *diffusion*, the slow drift of fair value during his quote's life, and none against a *jump*, a discrete public move that every participant sees at once. Against diffusion, a wider quote buys time. Against a jump, only being first helps, and being second is the same as being last. §27.6 makes both statements exact.

> **Trend Watch. The robots took the RFQ, then called in sick (2020–2026).** *What changed:* the quote clock itself was automated. Tradeweb says AiEX now handles a large and rising share of its institutional trades *(share not independently verified; Tradeweb 10-K, FY2025)*. Trumid executed 88% of eligible RFQ line items fully no-touch in September 2025 (The DESK, 2025-10-08). In October 2026 Vanguard reported about 70% of its traded volume automated, up from about 40%, while noting it sends nothing without a trader (The DESK, October 2026). *The stress test:* in a Coalition Greenwich survey of 51 corporate bond investors in Q4 2023, "improved auto-quoting" topped the buy side's wishlist for dealers. The same post recalls that in March 2020 "several of the largest banks famously shut down their auto-quoters" because their pricing algorithms could not cope with the volatility, a lesson that later let them handle bouts of volatility (Kevin McPartland, Coalition Greenwich, 2024-02-13). In October 2026, buy-side traders told FILS Europe that electronic liquidity providers "help mainly in normal markets." *What it means for the desk:* the auto-responder is a slow FPGA with better excuses. Its parameter file is a trigger table and its "stress mode" is a kill switch with a reputation. Both belong under the same governance as the fast path in §27.6–27.7, with explicit triggers, owners and audit trails, not a trader's intuition about when the market "feels weird." The full adoption series is in §18.7.

> **[SOURCE EXTRACTION]** *Man_Revolutions_in_Credit_Trading_2023 p.2:* "the biggest barriers to systematic approaches breaking through in credit have traditionally been execution and the ability to model transaction costs and liquidity within decades-old manual processes"
>
> **Annotation.** Our analysis: Man locates the bottleneck in the plumbing, not the alpha, and this chapter takes that literally. The three things the sentence names (execution, transaction-cost modelling, liquidity) are, respectively, the OMS/EMS and order state machine (§27.4), the cost model fed by provenance-typed prices (§27.2), and the fill-probability and streaming-eligibility services (§27.4, §27.6). On a 2026 desk the barrier has moved. Electronic execution exists, and the hard part is making the automated quote clock *safe*: knowing which prices are real, which quotes are exposed, and what stops the machine. A strategy that cannot be executed is a research note. A strategy that can be executed but not stopped is the opening paragraph of an SEC order (§27.7).

> **[SOURCE EXTRACTION]** *Blackstone_Systematic_Credit p.2:* "The proliferation of electronic bond trading, higher-quality pricing data, and improved computational power is allowing Blackstone to apply the same sophisticated..."
>
> **Annotation.** Our analysis: the sentence (cut where our source map cuts it) names the three inputs this chapter builds in order: the feed (electronic trading), the price store (pricing data), and compute. Note the order of dependence. Compute is the cheapest of the three and the one engineers most like to buy; pricing-data quality is the one that silently decides whether the backtest is real (§27.2–27.3, where Bohn and Stein warn about fitting "someone else's model"). The modern desk departs from the brochure in one respect: "sophisticated" is not a property of the model but of the whole pipeline, and the weakest link is usually a timestamp.

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

**Late data.** Records arrive late: TRACE by design, vendors by habit. Let lateness $X = \text{known\_at} - \text{event\_time}$ have distribution function $G$. A streaming job that closes each time bucket at watermark lag $L$ loses fraction $1 - G(L)$ of records to lateness. Choose $L$ at a high quantile of $G$ (say the 99.9th percentile of the last 20 sessions). Records later than the watermark go to a **correction stream** that writes new knowledge-time rows (§27.3) and never mutates the bucket that strategies already consumed. Overwriting yesterday's bucket with a late print is how a desk discovers that its backtest knew things its traders did not.

> **Trend Watch. The tape got later and dirtier (2022–2027).** *What changed:* the public tape's speed and cleanliness stopped improving. A proposal to cut the TRACE reporting outer limit from 15 minutes to one minute was floated in 2022 and approved in 2024, then shelved: FINRA Regulatory Notice 25-17 (2025-12-04) says FINRA is "not moving forward" with the one-minute limit, and 15 minutes remains. The same notice made aggregate allocation reporting optional from 2026-06-08, with dissemination caps of \$5mm for IG and \$1mm for HY. *How big:* duplicate affiliate trade reports inflated US high-grade TRACE volume by up to 8% in June 2026 (MarketAxess volume release). The SEC approved extending the TRACE affiliate-principal indicator on 2026-07-24; use is voluntary from 2026-08-31 and mandatory from 2027-08-02 (FINRA Notice 26-16). *What it means for the desk:* volume-based features (liquidity scores, turnover, Chapter 21's loan analogues) need a dedupe stage and a **regime tag**, because the same economic activity reports as different volumes before and after August 2027. And the desk's own fills, timestamped by its own hardware, are the only sub-second truth it will ever have about credit. Store them as if they were the most valuable dataset in the building, because they are.

### Specification for AI Implementation

**What ROBO built from the vague version.** Asked to "clean up TRACE duplicates," ROBO deleted every print with the same price and size as another print that day. Half of a block's legitimate partial fills vanished, and a liquidity score dropped 30% overnight. The spec below marks, never deletes; requires opposite sides and a time window; prefers the affiliate flag when it exists; and tags the regime so that features can be split at the flag dates.

**Schema (`price_record`).** `instrument_key: str` (surrogate, §27.3) · `price: float` (per 100 face if `price_type="PRICE"`, bp if `"SPREAD"`, decimal if `"YIELD"`) · `price_type: {"PRICE","SPREAD","YIELD"}` · `side: {"B","S","M"}` · `size_mm: float` (par, USD millions; TRACE-capped values flagged) · `kind: PriceKind` · `source: str` · `event_ns: int` · `known_ns: int` (both ns since epoch, PTP-disciplined) · `affiliate_flag: Optional[bool]` (None before the indicator existed). **Edge cases:** negative latency beyond the clock-error bound raises; capped sizes are never treated as exact; `EVALUATED`/`COMPOSITE` records cannot enter a training-label set.

Everything in the provenance rule so far is a promise about what a number is allowed to mean, and promises written in a spec get broken by the first engineer who is late for the open. The desk wants three of them to be impossible rather than discouraged: a dealer run cannot become a fill price, a negative latency cannot be quietly averaged into a mean, and a TRACE duplicate cannot be silently deleted along with the legitimate partial fills that resemble it. So the rules go into code at the door of the store, where every price either gets its badge or does not get in.

Listing 27.1 is that door. `PriceKind` is the five-way enum from §27.2.2, and `PriceRecord` is a frozen dataclass carrying the schema above, so a record cannot be edited after it is stamped. `TRAINABLE` holds two kinds, `TRADED` and `FIRM_QUOTE`, and `training_labels` is a filter against it: evaluated prices, composites and dealer runs may be features but never labels, simulated fills or cost targets. `latency_ms` turns `known_ns - event_ns` into milliseconds and raises if the answer is more negative than the clock-error bound the caller supplies. The bound is an argument, not a default, because the desk has to say how good its clocks are. A small negative number inside the bound is returned as it is, not clipped to zero.

`dedupe_trace` takes a table of prints and returns it with three new columns, `dup`, `dup_reason` and `regime`, and with no row removed. It sorts by instrument and event time, marks a print as a duplicate leg when `affiliate_flag` is true, and otherwise looks forward within `window_s` (one second by default) for an unflagged print with the same price, the same size and the opposite side. That later leg is marked `inferred_pair`, and each print is matched at most once. `trace_regime` stamps each print `no_flag`, `flag_voluntary` or `flag_mandatory` around the August 2026 and August 2027 dates, so volume features can be split where the reporting changed. The sanity block feeds in seven prints and expects exactly one pair: a 2mm and a 1mm print at the same price do not match, and neither do two prints five seconds apart.

Run it at ingest, before any liquidity or turnover feature is built, and treat its output as a proposal. The edge that bites is the inferred pair itself. A genuine customer round trip at the same price and size inside a second looks identical to an affiliate's double report, so rule 2 will sometimes mark a real print. Because it only marks, the cost is a decision for the feature builder rather than lost history. Count how many rows rule 2 touches in each regime before trusting a volume series that spans August 2027.

*The full listing is [Listing 27.1 in Appendix F](#code-27-1).*

## 27.3 The Security Master Is the Credit Agreement of the System

Theo spent four years reading credit agreements for the one clause that reprices everything. On his third Tuesday on the desk, he finds it in a database. The desk's security master is keyed on CUSIP, has one row per bond, and overwrites that row when a field changes. "So when a company does an uptier," he asks, "where does the old loan go?"

"It stays," says Kaz. "We update the ranking."

"And the backtest from before the uptier?"

Kaz is quiet for a while. Then: "Is a drop-down the thing in the order ticket where you pick the venue?"

"It's the thing where the IP moves to an unrestricted subsidiary and your recovery moves with it."

Every liability-management transaction, exchange offer and reorganisation creates new instruments, new rankings and new issuer–guarantor maps (Chapters 13–16). A security master that cannot represent "this loan was first lien until 22 June 2020 and something else afterwards, and we learned that at 6 p.m." will either lie about the present or lie about the past. Both lies end up in the P&L, one in live trading and one in the backtest that justified it.

### 27.3.1 What the master holds

The entities are the ones Theo already knows from a capital-structure slide, made explicit:

- **Issuer** (with LEI) and **obligor group**: borrower, guarantors, restricted and unrestricted subsidiaries, as a dated graph rather than a list.
- **Instrument**, keyed by an **internal surrogate key** that the desk mints and never reuses. CUSIP, ISIN and FIGI are attributes of the instrument, not its identity. A 144A tranche, its Reg S twin and the registered exchange notes that follow are three identifiers on one economic line. They stay separate for settlement and TRACE, and are joined for risk.
- **Terms**: coupon, maturity, call schedule, ranking, lien, and covenant flags (from the Chapter 25 parser).
- **Events**: exchange, uptier, drop-down, distressed exchange, reorganisation, change of control. Each is a row in an event log with an effective date, a source document and the instruments it creates, retires or re-ranks.

### 27.3.2 The bitemporal model, derived

A **fact** is a tuple

$$
f = \big(k,\ a,\ v,\ [t^{v}_{0}, t^{v}_{1}),\ [t^{k}_{0}, t^{k}_{1})\big),
$$

where $k$ is the instrument key, $a$ an attribute (ranking, coupon, guarantor set), $v$ its value, $[t^{v}_{0}, t^{v}_{1})$ the **valid-time** interval over which the fact was true in the world, and $[t^{k}_{0}, t^{k}_{1})$ the **knowledge-time** interval over which the desk believed it. An open interval ends at $+\infty$. (Superscripts $v$ and $k$ label the two time axes; they are not powers, and this $k$ is unrelated to the order-arrival parameter $k$ of Chapter 18.) The **as-of query** is

$$
Q(k, a;\ t^{v}, t^{k}) = \big\{\, v \;:\; f \in \mathcal{S},\ t^{v}_{0} \le t^{v} < t^{v}_{1},\ t^{k}_{0} \le t^{k} < t^{k}_{1} \,\big\},
$$

and the store $\mathcal{S}$ satisfies two invariants.

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

The facts, from our LMT dossier (Proskauer, 2025-01-02): on 2020-06-22, Serta Simmons Bedding closed a transaction with a majority group of its lenders. Participating lenders provided \$200mm of new-money first-out super-priority debt and exchanged about \$1.2bn of their first- and second-lien term loans into about \$875mm of second-out super-priority debt. Non-participating lenders stayed in the original 2016 facilities, which now ranked behind both new tranches. The transaction relied on the credit agreement's "open market purchase" language. On 2024-12-31 the Fifth Circuit held that it was not an open market purchase (Chapter 13 has the litigation). The most expensive three words in finance have now also become a row in a database.

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

A CUSIP-keyed, overwrite-in-place master gets question 2 wrong. It reports the post-exchange ranking for a decision made before anyone knew of it, so a backtest of an "avoid priming risk" strategy (Chapter 13's PRS) looks prescient by construction. The Ad Hoc Group, represented by counsel, would like it noted that they also knew before the desk did. That is what a Rule 2019 statement is for. Hertz's 2021 emergence gives the mirror image: new post-reorganisation equity and warrants whose economic predecessor is a claim, not a security. Chapter 16 handles the valuation; the master handles the lineage, as an event row linking predecessor and successor keys.

> **Trend Watch. Identifiers become contested infrastructure (2022–2026).** *What changed:* the identifier your master is keyed on turned out to be a licensed, litigated asset. In March 2022, Dinosaur Financial Group, Hildene Capital Management and Swiss Life Investment Management sued CUSIP Global Services, S&P Global, FactSet and the American Bankers Association (*Dinosaur Financial Group LLC et al. v. S&P Global Inc. et al.*, S.D.N.Y. No. 1:22-cv-01860). The court dismissed most claims but let a Sherman Act §2 monopolisation claim proceed, and a later ruling certified a class of end-user firms and data vendors (ruling dates: see the docket). *The regulatory crack:* in Release No. 34-95148 (adopted 2022-06-23), the SEC let Form 13F filers report a FIGI for each security, optional and in addition to, not instead of, the CUSIP, with the amended form effective 2023-01-03. OpenFIGI distributes its symbology "under the MIT Open Source license at no cost and as a public good." In a 2024 SEC comment letter (file S7-2024-05), the plaintiffs' counsel backed requiring FIGI in regulatory filings. *What it means for the desk:* key the master on an internal surrogate and treat CUSIP, ISIN and FIGI as crosswalk attributes with their own valid-time history. Switching or adding an identifier scheme then becomes a data migration, not a rewrite of every join in the building.

### Specification for AI Implementation (bitemporal master)

**What ROBO built from the vague version.** Asked for "a security master with history," ROBO added an `updated_at` column and overwrote rows. It had history in the sense that a shredder has history. The spec: two time axes, append-only knowledge, an exclusion check, and three tests that encode the Serta questions above.

The three Serta questions are the test a security master has to pass, and they are unforgiving in one particular way: each asks a different pair of dates, and a table with one date column can answer at most one of them. The desk could read the definition of bitemporality, nod, and end up with an `updated_at` column, which is how most desks get there. Or it could make the store physically unable to rewrite what it once believed, and then put Theo's Tuesday question to it. Listing 27.2 does the second.

`BitemporalMaster` keeps a list of rows with seven fields: instrument key, attribute, value, a valid interval and a knowledge interval, where an open interval ends at `OPEN`, the largest timestamp pandas allows. Its one write method, `assert_fact`, refuses an empty valid interval and refuses any `known_at` earlier than the previous write, so the knowledge axis only moves forward. It then finds every currently believed row for the same key and attribute whose valid interval overlaps the new one. Each is closed by setting its `known_to` to the write time, the parts of its valid interval that the new fact does not cover are re-inserted as fresh rows, and the new fact is appended. The only edit ever made to an existing row is closing an open `known_to`. That is invariant (I2) of §27.3.2, and it is why the past is immutable.

`as_of` answers $Q$: given a key, an attribute, a valid date and a knowledge date, it returns the one matching value, `None` if there is none, and raises if there are two. `snapshot` returns the whole table as it stood at one knowledge time. `check_exclusion` scans pairs of rows for the same key and attribute that overlap on both axes, which is invariant (I1). The sanity block loads the Serta rows, with the closing known at 6 p.m. on 2020-06-22 *(illustrative)*, and asserts the answers: the post-exchange ranking for live risk, `first_lien_pari` for a decision at midnight, and a second-out tranche that does not yet exist. It then adds a litigation fact in 2025, checks that the 2020 snapshot is unchanged, and checks that writing into the past of the knowledge axis raises.

Use it for anything a backtest or a live risk run reads that can later be restated: rankings, coupons, guarantor sets, ratings. Do not mistake it for production storage. The scans are linear, and a real master puts the same two invariants into Postgres range-exclusion constraints. The edge that bites is `known_at`, which defaults to `None`. Pandas turns that into `NaT`, every comparison against `NaT` is false, the monotonic guard goes quiet, and the row gets a knowledge time that no query will ever match. Always pass it, and stamp a migrated legacy table with the migration date, not with a date you wish you had recorded.

*The full listing is [Listing 27.2 in Appendix F](#code-27-2).*

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

**FIX for bonds, the fields that bite** *(general knowledge; confirm against each venue's rules of engagement)*. `SecurityIDSource` (tag 22) says which identifier `SecurityID` (48) is, so the gateway must translate surrogate keys through the crosswalk of §27.3 on every message. `SecurityType` (167) = `CORP`. `PriceType` (423) distinguishes percentage of par (1), spread (6) and yield (9), and a spread quote also needs its benchmark (`BenchmarkSecurityID`, 699). `SettlDate` (64) must reflect T+1 for US corporates since May 2024 (Chapter 22). The classic credit gateway bug is a spread quote interpreted as a price. A bid of "105" meant as a spread of 105 bp over the 10-year, read as a price of 105 points, is a 10-point gift on a bond trading near 95. That is a fat finger made by a parser.

**Pre-trade checks live in the gateway.** The first tier of the kill-switch hierarchy (§27.7) sits here, before any message leaves the building. SEC Rule 15c3-5 (Release No. 34-63241, 2010-11-03) requires controls "reasonably designed to prevent the entry of orders that exceed appropriate pre-set credit or capital thresholds, or that appear to be erroneous," and requires that they be "under the direct and exclusive control of the broker or dealer with market access." In credit terms: price collars against composite *and* against the desk's own last fill, notional and DV01 caps per order and per minute, a `PriceType` sanity check (a "price" below 10 or above 200 is probably a spread), and a duplicate-order detector. Mags notes that in 1997 the pre-trade check was a senior trader saying "you want to do *what*?" loud enough for the floor to hear. It had excellent recall and terrible uptime.

## 27.5 Latency Budgets Are Queues, Not Numbers

Kaz's "forty milliseconds" was true and useless. It is the time the pricing engine spends *working* on a request. The counterparty experiences the time the request spends *in the building*, and on an FOMC afternoon most of that is spent waiting. Ines puts it in her terms: "The average is the hand you expect. The p99 is the hand you get when someone at the table knows something."

### 27.5.1 Little, Pollaczek–Khinchine, and the p99, derived

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

**Kaz's engine.** With $\mathbb{E}[S] = 40$ ms, $c_s^2 = 4$ (most refreshes are trivial, a few hit a callable bond's lattice) and $\rho = 0.7$: $\mathbb{E}[W_q] = \tfrac{0.7}{0.3}\cdot\tfrac{5}{2}\cdot 40 \approx 233$ ms, and $t_{0.99} \approx \tfrac{233}{0.7}\ln 70 \approx 1{,}420$ ms. Add the service itself and the p99 sojourn is about a second and a half, the cold open's number. At $\rho = 0.5$ the same engine has a p99 wait near 0.8 s; at $\rho = 0.9$, about 4.5 s. Now notice when $\rho$ goes to 0.9: when TY moves, every exposed quote needs repricing at once. **Load and danger are positively correlated**, so the engine is slowest exactly when slowness is expensive. That is why the fast path exists. It does not reprice anything, so it has no queue to fill up.

**Fan-out.** A portfolio trade of $n$ lines that waits for all $n$ pricing calls is slow if any one is. If each is slow with probability $p$,

$$
\mathbb{P}(\text{request slow}) = 1 - (1-p)^n .
$$

Dean and Barroso's "The Tail at Scale" (*Communications of the ACM*, 2013) made this famous with a server that is slow one time in a hundred: at 100-way fan-out, 63% of requests are slow. A 150-line PT inside Chapter 19's 90-second budget is slow 78% of the time. Inverting the formula, the end-to-end p99 of the PT requires each line's latency at the $0.99^{1/150} \approx 0.99993$ quantile. **A 150-line PT's p99 is each pricing call's p99.993.** Remedies from the same literature: hedged requests (send a backup after the p95), bounded fan-out (price lines in correlated clusters and interpolate), and a hard deadline after which a line is quoted from the cluster proxy and flagged.

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

*(Times are illustrative except where sourced.)* Both columns are correct, and they differ by about five orders of magnitude. The RFQ column has slack everywhere except the human, which is why automation took the quote clock first (Trend Watch, §27.1). The hedge column has no slack anywhere, which is why it contains no model.

### 27.5.3 Case Study: CME Globex halts, 2019 and 2025, a budget with an infinite term

On the evening of 2019-02-26, a technical error halted CME Globex for about three hours, from 6:39 p.m. to 9:45 p.m. CT, covering Treasury and S&P 500 futures, before iLink gateways restarted. In Thanksgiving week of 2025 (2025-11-27/28), a cooling failure at a CyrusOne data centre near Chicago stopped Globex for a reported ten hours or so, halting Treasury and SOFR futures (Hedgeweek; duration per press reports). For a credit desk, the danger is not that the hedge is unavailable. The danger is that the fast path goes *quiet*. A trigger table compares hedge ticks with reference prices; with no ticks, nothing ever crosses a threshold, and every streaming bond quote stays live with no hedge and no guard. An FPGA watching a dead feed is a smoke detector in a building with no air. The fix is a Tier-2 rule (§27.7): if the hedge feed's heartbeat or sequence numbers stop for longer than a set gap, pull or widen every quote whose trigger row references that venue, and re-arm only when the slow path re-prices against a live hedge or an explicit substitute (CDX in place of credit futures, cash Treasuries in place of TY).

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

where $\beta_{ij}$ is in bond points per hedge-instrument point. Hedge ratios are ratios of dollar durations (Veronesi defines dollar duration as $D^{\$}_P = -dP/dr$ and relates it to duration by $D^{\$}_P = P \times D_P$; Veronesi_Fixed_Income_Securities p.120). For a rate hedge, with $\kappa_i^{\text{rate}}$ the empirical rate beta of Chapter 8 (empirical over model duration),

$$
\beta_{i,\text{TY}} = \frac{\text{DV01}_i}{\text{DV01}_{\text{TY}}}\,\kappa_i^{\text{rate}} .
$$

For a credit-ETF hedge, write $\Delta P_i \approx -P_i D^{\text{spr}}_i \Delta s_i$, $\Delta s_i = \kappa^{\text{cr}}_i\,\Delta s_{\text{HY}}$ (the DTS beta of Chapter 9, $\kappa^{\text{cr}}_i \approx s_i/s_{\text{HY}}$), and $\Delta H \approx -H D_H \Delta s_{\text{HY}}$; eliminating $\Delta s_{\text{HY}}$,

$$
\beta_{i,\text{HYG}} = \frac{P_i\,D^{\text{spr}}_i\,\kappa^{\text{cr}}_i}{H\,D_H}.
$$

**The cold open, as numbers** *(all inputs illustrative)*. A bond at $P_i = 95$ with $D^{\text{spr}}_i = 8$ has $\text{DV01}_i = 0.076$ points per bp. With a TY futures DV01 of 0.065 points per bp and $\kappa^{\text{rate}} = 0.9$, $\beta_{\text{TY}} \approx 1.05$. With the bond at 130 bp, the HY index at 325 bp ($\kappa^{\text{cr}} = 0.4$), HYG at \$80 and $D_H = 3$, $\beta_{\text{HYG}} \approx 1.27$. TY down six 32nds and HYG down 14 cents give $\Delta\hat P \approx 1.05(-0.1875) + 1.27(-0.14) \approx -0.375$: three-eighths.

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

The price of safety is false pulls, and they come exactly when moves offset. In a flight to quality TY rallies and HYG falls, and an IG bond's fair value barely moves, so the cheap rule panics at the one moment the bond is calm. It is a smoke detector that goes off when you open a window. **Allocating the budget.** Under diffusion over a short horizon, instrument $j$ alone fires with probability $2\Phi(-\tau_{ij}/\sigma_j)$, where $\sigma_j$ is its volatility over that horizon. Equalising the standardised distances $\tau_{ij}/\sigma_j = c$ gives $\theta_{ij} = c\,|\beta_{ij}|\,\sigma_j$ with $c = \theta_i/\sum_j |\beta_{ij}|\sigma_j$, which stops one noisy hedge from owning the whole budget.

**The guard band $\varepsilon$.** Two errors separate the hardware's number from the truth. *Fixed point:* with $\beta$ stored as integers with $f$ fractional bits (bond points per hedge tick) and moves as integer ticks $n_j$, rounding error is at most $2^{-f-1}\sum_j |n_j|$; at $f = 16$ and a few hundred ticks this is about $10^{-3}$ points or less. *Convexity:* Veronesi's second-order term (S14 below) is $\tfrac12 C P (\Delta r)^2$; for $C = 80$, $P = 95$ and a 10 bp move it is $\tfrac12\cdot 80\cdot 95\cdot 10^{-6} \approx 0.004$ points *(illustrative)*. Set $\varepsilon$ above the sum, say 0.01 points, and the linear rule can never be fooled into keeping a quote that the exact rule would pull.

**Re-arming.** The fast path may only pull. A pulled quote comes back only when the slow path reprices it and writes a new row with new reference prices. This kills flapping (pull, re-quote, pull) for free and preserves the chapter's invariant: the fast path says no, and only the slow path says yes.

> **[SOURCE EXTRACTION]** *Veronesi_Fixed_Income_Securities p.152:* "Fact 4.1 An approximation of the percentage impact of interest rates on the price of a security is given by dP/P = −D × dr + ½ × C × dr²"
>
> **Annotation.** Our analysis: the FPGA implements the first term and ignores the second, and Veronesi's own footnote ("stems directly from the application of a second-order Taylor expansion") tells you how large the neglected term can be. That makes convexity a *threshold-error budget*, not a pricing input. The desk departs from the textbook use in two ways. The relevant "duration" is empirical and spread-adjusted (Chapter 8), not the analytic one, because IG spreads partly offset rate moves. And for callable or distressed bonds the second-order term is neither small nor stable, which is the honest reason such bonds should not be streamed from a linear table at all.

### 27.6.2 What a stale quote costs: diffusion versus tournament

Let fair value over the exposure window $\Delta$ (seconds) follow Bachelier dynamics under $\mathbb{P}$, $\hat P_{t+\Delta} = \hat P_t + \sigma\sqrt{\Delta}\,Z$ with $Z \sim N(0,1)$ and $\sigma$ in points per $\sqrt{\text{s}}$. An informed taker sells to the bid iff $\hat P_{t+\Delta} < b = \hat P_t - h$. The expected loss per exposure, against new fair value, is

$$
\mathbb{E}\big[(b - \hat P_{t+\Delta})^{+}\big] = \mathbb{E}\big[(-h - \sigma\sqrt{\Delta}\,Z)^{+}\big] = \sigma\sqrt{\Delta}\,\big[\varphi(x) - x\,\Phi(-x)\big], \qquad x = \frac{h}{\sigma\sqrt{\Delta}},
$$

the Bachelier put with the strike $h$ out of the money. Using $\Phi(-x) = \varphi(x)\big(x^{-1} - x^{-3} + O(x^{-5})\big)$, the bracket is $\approx \varphi(x)/x^2$ for large $x$, which is smaller than exponential. Take a fair-value volatility of 0.5 points a day over a 23,400-second session *(illustrative)*, so $\sigma \approx 0.0033$, and $h = 0.19$. At $\Delta = 1.5$ s, $x \approx 47$ and the loss is zero to machine precision. Even over a two-minute RFQ timer, $x \approx 5.3$ and the loss is about $10^{-9}$ points. **Against diffusion, the half-spread is an impregnable wall.**

Now a *jump*: a public, discrete move of fair value $J_i = \boldsymbol\beta_i^{\top}\Delta\mathbf H$, seen by everyone at once. If the quote is still live, the taker wins with probability $\pi$, the probability that their order reaches the venue before your cancel, and the loss is

$$
\pi\,\big(|J_i| - h_i\big)^{+}.
$$

In the cold open, $\pi \approx 1$ (a 1.5-second reaction against takers measured in microseconds to milliseconds), and the loss is $(0.375 - 0.19) \times \$3\text{mm}/100 \approx \$5{,}500$. Latency enters the two regimes in completely different ways. Under diffusion it enters smoothly through $\sqrt{\Delta}$, and a wider $h$ compensates. Under jumps it enters only through $\pi$, which depends on your *rank* among responders and not on your level of speed: being second is the same as being last. This is the sniping mechanism of Budish, Cramton and Shim (2015, *Quarterly Journal of Economics*), and the FCA study puts numbers on it for equities: modal race 5–10 µs, median 46 µs, mean 79 µs, 90th percentile about 200 µs; races are about 20% of volume, and the latency-arbitrage "tax" is 0.42 bp of total volume against an average effective spread just over 3 bp (Aquilina, Budish and O'Neill 2020). A credit desk's half-spread is far wider, but so is the jump in a hedge instrument during a quote's life. The trigger table exists to turn $\pi$ from 1 into something near 0 by pulling while the race is still being run.

> **[SOURCE EXTRACTION]** *Dynkin_Systematic_Investing_in_Credit p.702:* "LCS measures the cost of an immediate round-trip transaction of a typical institutional size and is expressed as a percentage of a bond price. ... For bonds quoted on spread, LCS is calculated as a product of bid–offer spread and spread duration."
>
> **Annotation.** Our analysis: this pins down $h_i$ with units. LCS is a round trip as a percentage of price, so the half-spread in points is $h_i = \tfrac12\,\text{LCS}_i \times P_i/100$: an LCS of 0.4% on a 95 bond gives $h = 0.19$, the number used throughout this section. LCS also decides *which bonds get streamed*. A bond whose $h_i$ is small relative to the typical hedge-implied jump $|J_i|$ is a bond whose streaming quote is a donation, and it should stay RFQ-only. Ben Dor makes the complementary point that a trader who must "commit to making a market in a bond for a time going forward" should prefer the higher-volume bond at similar LCS (Ben_Dor_Quantitative_Credit_Portfolio_Management p.160). Volume shortens the time inventory waits; it does not shrink the jump.

### 27.6.3 Case Study: The 15 October 2014 Treasury flash rally, replayed against a trigger table

Between 9:33 and 9:45 a.m. ET on 2014-10-15, the 10-year Treasury yield fell 16 bp and then rebounded, "without a clear cause," on a day when it traded in a 37 bp range and closed 6 bp below its open. Principal trading firms accounted for more than half of traded volume in the electronic interdealer market (Fleming, Johansson, Keane and Meyer, *Liberty Street Economics*, 2019-10-15, looking back at the Joint Staff Report released 2015-07-13). For a credit desk this is the canonical hedge-clock event, and it happened in the instrument the desk hedges with.

Replay the cold-open bond's row with $\theta = 0.14$ and the budget split as above. A 16 bp rally moves TY by roughly a point (at 0.065 points per bp), so the bond's rate-implied fair value rises by about a point, and every streaming *offer* becomes a gift within the first bp or two of the move. The TY threshold $\tau_{\text{TY}} \approx 0.07$ TY points is about 1 bp of yield, so the per-instrument rule pulls the offer within microseconds of the first meaningful ticks. The interesting question is the next twelve minutes. The slow path wants to re-arm at a new fair value, but its composite is stale, TRACE is up to 15 minutes behind, and the hedge itself is about to reverse. The right re-arm rule is therefore **volatility-gated**: re-quote only when realised hedge volatility over the last $N$ seconds is below a threshold, and then at a wider $h$. A desk that pulled and waited lost nothing but opportunity. A desk that kept streaming was picked off on the way up and again on the way down. The market itself behaved like a giant trigger table that day, with liquidity providers pulling and re-quoting in waves. That is not a bug in the market; it is what rational quote-pulling looks like when everyone has the same table.

> **Trend Watch. Credit gets a listed hedge (2018–2026).** *What changed:* for most of its history the credit desk's fast hedge was rates (TY) plus an ETF; credit beta itself had no exchange-traded future. Cboe listed iBoxx iShares futures on HY (IBHY, 2018) and later IG (IBIG). CME launched Bloomberg US corporate index futures (IG and HY, including duration-hedged variants) in June 2024. *How big:* record open interest of 3,200 contracts (about \$320mm notional) in March 2025. A CME factsheet reported more than 580,000 contracts traded since launch as of 2025-10-10, open interest above 6,800 contracts (more than \$730mm notional), and Q3-2025 ADV above 2,900 contracts (CME press releases 2025-03-17 and 2025-09-08). Cboe's IBHY/IBIG block trades topped \$1bn a month for two consecutive months in July–August 2026, with IBIG block volume passing IBHY for the first time (The DESK, 2026-10-16, Cboe-sponsored content). *What it means for the desk:* a credit-beta hedge now executes on a matching engine with microsecond order entry and a public book. That gives the trigger table a credit column that is not an ETF with its own premium/discount dynamics. It also means credit-index futures can jump on their own, so they belong in $\Delta\mathbf H$, with their own $\beta_{ij}$ and their own heartbeat rule (§27.5.3).

### Specification for AI Implementation (trigger tables)

**What ROBO built from the vague version.** Asked to "pull quotes when the market moves," ROBO pulled every quote whenever any instrument ticked. It was perfectly safe and quoted for a total of eleven seconds on its first day. The spec: sensitivities in bond points per hedge point, a joint rule and a provably safe per-instrument rule, fixed-point arithmetic with a stated error bound, pull-only semantics, and the cold open as a regression test.

A trigger table is a small piece of arithmetic that has to be right in three places at once: on paper, in a reference implementation, and in fixed-point hardware that will never see a float. The slow path computes the table and the FPGA only reads it, so nobody gets a second chance to find out that a sign was wrong. The desk therefore wants one reference that states every sensitivity in bond points per hedge point, runs both pull rules against the same moves, and proves the cheap rule safe by brute force before a bitstream is synthesised. Ines would call it checking the odds before sitting down.

Listing 27.4 starts with the sensitivities. `beta_rate` is the dollar-duration ratio times the empirical rate beta, and `beta_credit` is the ETF version: bond price times spread duration times DTS beta, over the ETF's price times its spread duration. `allocate_tau` splits the pull budget $\theta$ across hedges in proportion to $|\beta_j|\sigma_j$ and divides each share by $|\beta_j|$, which gives thresholds in each hedge's own units. `joint_pull` is the exact rule: the dot product of $\boldsymbol\beta$ and the hedge move, compared with minus $\theta$, with `side` flipping the sign for an offer. `box_pull` is the cheap rule: any hedge move beyond its own threshold. `bachelier_pickoff` is the closed form of §27.6.2.

The checks replay the cold open with $\theta = 0.19 - 0.04 - 0.01 = 0.14$ points. TY down six 32nds and HYG down 14 cents move fair value by about three-eighths, and both rules pull the bid. In a flight to quality, fair value barely moves, the joint rule stays quiet and the cheap rule pulls, which is its false alarm on display. Then 200,000 correlated, fat-tailed moves, rounded to tick grids, confirm that the joint rule never fires without the cheap one and measure the false pulls that safety costs. A Q.16 integer version shows that the hardware's decision differs from the exact one only inside the stated error bound, for moves up to two points per refresh; larger ones meet the Tier-0 collars first. The last block checks the diffusion pick-off loss against Monte Carlo at 15 minutes, finds it zero at 1.5 seconds, and prices the jump loss at about \$5,500.

Use the pair of rules for streamed, linear bonds. Do not use them for callables or distressed paper, where convexity swamps the guard band. The edge that bites is a zero beta: `allocate_tau` then divides zero by zero, and that hedge's threshold comes back as NaN with a warning. Comparisons against NaN are false, so the hedge never pulls, which happens to be right, but hardware has no NaN. Give the table an explicit "never" sentinel for any hedge a bond does not use.

*The full listing is [Listing 27.4 in Appendix F](#code-27-4).*

## 27.7 Kill Switches as Stopping Rules

"Folding before the river," Ines says, "is not cowardice. It's a stopping rule with a measure attached. You decide in advance what evidence makes you get up from the table, and how often you're willing to get up for nothing." The kill switch is the sacred right of the system: no majority of components can amend it, and no single component can waive it. Kaz asks whether that means it needs unanimous consent to change. "It means it needs two humans to turn back *on*," says Ines. "Anyone can turn it off."

### 27.7.1 The hierarchy

| Tier | What fires it | Where it lives | Time scale | Example controls |
| :--- | :--- | :--- | :--- | :--- |
| 0: hard limits | a single message violates a pre-set bound | gateway / FPGA, before the wire | ns–µs | price collar vs composite and last fill; max order value and volume; message-rate throttle; notional and DV01 caps; `PriceType` sanity |
| 1: sequential tests | accumulating evidence of being picked off or of abnormal fills | risk engine, streaming | seconds–minutes | CUSUM on markouts; fill-ratio and child-to-parent ratio tests |
| 2: system health | the machine is not the machine you tested | ops plane | seconds | version and config-checksum skew across servers; hedge-feed heartbeat lost; clock fault; venue session down |
| 3: loss limits | the strategy, not the plumbing, is failing | PM and risk committee | days | drawdown stop-loss (Paleologo), capital reallocation (Chapter 28) |

**Authority** is part of the design, not an org chart. Anyone and anything (a human, a monitor, ROBO) may *trip* any tier, instantly, and a trip cancels all live orders and quotes in its scope. Only the slow path, with two distinct authorised humans, may *re-arm*. Every trip records who, what and why, and every order carries the algorithm, trader and desk responsible for it. This is the regulator's floor, and it is a good design anyway. MiFID II RTS 6 (Delegated Regulation (EU) 2017/589, applying from 2018-01-03) requires the ability to "cancel immediately, as an emergency measure, any or all of its unexecuted orders" (Art. 12), pre-trade price collars, maximum order values and volumes and message limits (Art. 15), and states that "Real-time alerts shall be generated within five seconds after the relevant event" (Art. 16). SEC Rule 15c3-5 is principles-based and puts no number on alert latency. RTS 6's five seconds is the only regulatory clock on the slow lane, and a desk should treat it as a ceiling, not a target.

### 27.7.2 CUSUM on markouts, derived

Let fill $k$ have a markout $m_k$ (points, against hedge-implied fair value one minute after the fill, signed so that positive is good for the desk). It arrives long before TRACE does. Healthy: $m_k \sim N(\mu_0, \sigma^2)$ i.i.d. Picked off: $m_k \sim N(\mu_1, \sigma^2)$ with $\mu_1 < \mu_0$. The log-likelihood ratio of one observation is

$$
\ell_k = \ln\frac{f_1(m_k)}{f_0(m_k)} = \frac{\mu_0 - \mu_1}{\sigma^2}\left(\frac{\mu_0 + \mu_1}{2} - m_k\right) = \delta\left(z_k - \frac{\delta}{2}\right),
\qquad z_k = \frac{\mu_0 - m_k}{\sigma},\quad \delta = \frac{\mu_0 - \mu_1}{\sigma}.
$$

Page's CUSUM accumulates the evidence and forgets it whenever it favours health:

$$
G_k = \max\!\Big(0,\ G_{k-1} + z_k - \tfrac{\delta}{2}\Big),\quad G_0 = 0, \qquad K_c = \inf\{k : G_k \ge c\}.
$$

(We write the alarm index as $K_c$ because $\tau$ is reserved for default time.) It is a sequence of SPRTs, each restarted at zero, and it minimises the worst-case detection delay among all procedures with the same false-alarm rate (Lorden 1971; Moustakides 1986). The average run length for increments $N(\mu_G, 1)$ has Siegmund's approximation

$$
\text{ARL}(\mu_G) \approx \frac{e^{-2\mu_G b} + 2\mu_G b - 1}{2\mu_G^2}, \qquad b = c + 1.166,
$$

with $\mu_G = -\delta/2$ when healthy ($\text{ARL}_0$, the mean time between false alarms) and $\mu_G = +\delta/2$ when picked off ($\text{ARL}_1$, the detection delay). For a one-standard-deviation deterioration ($\delta = 1$) and $c = 5$: $\text{ARL}_0 \approx 938$ fills and $\text{ARL}_1 \approx 10.3$ fills. At 200 auto-quoted fills a day *(illustrative)*, that is a false alarm about every five trading days and detection within about ten bad fills. Raise $c$ to 6 and $\text{ARL}_0 \approx 2{,}570$ fills (about 13 days) while $\text{ARL}_1 \approx 12.3$. **Tripling the quiet time costs two fills of delay**, because to first order the delay grows only with the log of the false-alarm interval, $\text{ARL}_1 \approx \ln(\text{ARL}_0)/\mathcal{K}$ with $\mathcal{K} = \delta^2/2$ the Kullback–Leibler information per fill. The desk head chooses $c$, and in doing so chooses both numbers. Ines calls this reading the hand history in real time. The river is the bad fill that would have cost you the session; the CUSUM folds about ten bad fills in, which is long before the river and long after your ego would have liked.

> **[SOURCE EXTRACTION]** *Paleologo_Advanced_Portfolio_Management p.164:* "Stop-loss rules are a partial hedge for the PM call option. ... Since the value of the option increases with the volatility of the underlying asset, it is in the interest of the manager to run with the highest possible volatility, independently of her skill. The stop-loss is a constraint that limits the value of this option."
>
> **Annotation.** Our analysis: Tier 3 is Paleologo's stop-loss moved from the PM's contract to the machine, and the option argument applies to algorithms too. An auto-quoter rewarded on volume or hit rate holds a call option on its own variance, and will "run with the highest possible volatility" if its parameters let it, through wider size and tighter quotes in fast markets. The tiers below are the faster, finer versions of the same constraint. The modern desk departs from the PM framing in one respect: the stop-loss for an algorithm must be paired with an *automatic* re-arm prohibition. A human PM who is stopped out goes home and thinks. An algorithm that is stopped out will be restarted by a well-meaning engineer at 10:02 a.m. unless the design says only two humans and the slow path can do that.

### 27.7.3 Case Study: Knight Capital (2012) and Citigroup (2022), mapped to tiers

**Knight, 2012-08-01** (SEC Release No. 34-70694, 2013-10-16). While processing 212 small retail orders, Knight's SMARS router "routed millions of orders into the market over a 45-minute period, and obtained over 4 million executions in 154 stocks for more than 397 million shares." Knight ended up net long about \$3.5bn in 80 stocks and net short about \$3.15bn in 74, and "lost over \$460 million." The new code reused a flag that had once activated "Power Peg," functionality Knight "had discontinued using many years earlier." A technician "did not copy the new code to one of the eight SMARS computer servers," there was no second-technician review, and orders that reached the eighth server ran the dormant code. Before the open, the system sent 97 automated e-mails referencing the error to a group of Knight personnel, and Knight "did not design these types of messages to be system alerts." Throughout, "Knight remained connected to the markets and continued to send orders." The civil money penalty was \$12mm. Chapter 26 told this as a story about specifications. Here it is a story about four missing tiers. *Tier 2* (version skew) would have refused to open with one server out of eight on different code. *Tier 1* (a child-to-parent fill-ratio test) would have fired within seconds, because Power Peg kept sending child orders without counting fills. *Tier 0* (cumulative notional caps per strategy) would have stopped the position long before \$3.5bn. And *authority* would have answered the question nobody did for 45 minutes: who is allowed to pull the plug, and does pulling it actually disconnect?

**Citigroup, 2022-05-02** (FCA final notice 2024-05-22, as reported in coverage of the notice; figures to be checked against the notice itself). A trader meant to sell a basket worth \$58mm, and an input error produced one worth \$444bn. Controls blocked \$255bn; \$189bn reached an algorithm; about \$1.4bn of shares sold on European venues before the trader cancelled, coinciding with a brief, sharp drop in several European indices. The FCA found no hard block that would have rejected the whole basket, a pop-up warning the trader could click through without reading, and real-time monitoring that was too slow to escalate. Fines from the FCA (£27.77mm) and PRA (£33.9mm) totalled about £61.6mm. The lesson fits in one line of the spec below: **a warning that can be clicked past is a suggestion, not a control.** The Tier-0 function takes no override argument.

### Specification for AI Implementation (kill switch)

**What ROBO built from the vague version.** Asked to "add a kill switch," ROBO added a button that set `enabled = False` in the pricing loop. Live quotes on the venues stayed live, because nothing cancelled them. The button worked perfectly and changed nothing, which is Knight's 45 minutes in one line. The spec: trip cancels everything in scope; Tier 0 has no override; a dead-man heartbeat trips Tier 2; anyone may trip; only two distinct humans plus a passing slow-path check may re-arm; and CUSUM run lengths are checked against Siegmund.

Knight and Citigroup reduce to a short list of checks that a machine can run without asking anyone's permission: a hard limit on each message, a sequential test on the stream of fills, a heartbeat on the plumbing, and a rule about who may turn things back on. Two of those are statistics and should be tuned like statistics, with the false-alarm interval stated, not with a hunch that five seems about right. The other two are authority, and authority has to be code, because at 10:02 a.m. the engineer who wants to restart the quoter is always well meaning.

Listing 27.5 has two halves. The first checks the CUSUM arithmetic of §27.7.2. `siegmund_arl` is Siegmund's approximation, with the 1.166 shift added to the alarm level, and `simulate_arl` runs thousands of CUSUMs side by side on normal increments with a given drift until each crosses the level, then averages the alarm times. For a one-standard-deviation deterioration and a level of 5, the checks require about 938 fills between false alarms and about 10 fills to detect a real problem, with simulation agreeing within 10 percent. Moving the level to 6 must more than 2.5 times the quiet time while adding under 2.5 fills of delay.

The second half is `KillSwitch`, a state machine with two states, `ARMED` and `TRIPPED`. `pre_trade` is Tier 0. It refuses everything once tripped, throttles message rate over a one-second window (the only check that trips the whole switch), and then tests price sanity, a collar around the reference price, a maximum order size and a maximum live notional. It takes no override argument, so a caller who passes one gets a `TypeError`. `check_deadman` trips Tier 2 when the heartbeat is older than the limit. A trip cancels every live order and clears any re-arm votes. `trip` lets anyone on the allowed list do it, while `rearm` accepts only listed humans, counts distinct voters, and succeeds only with two of them and a passing slow-path check. The checks include a 444,000mm basket stopped by the order-size limit, a 105 bp spread read as 105 points stopped by the collar, a monitor denied the right to re-arm, and one human voting twice still counting once.

Use it as the reference the production gateway is tested against, not as the gateway. The edge that bites is the message-rate trip: `pre_trade` trips the switch and cancels live orders, but returns only `(False, "message_rate")`. The cancelled order IDs are not in that return value, and the log records the tier and reason without them. Whatever sends cancels to the venues must be driven by the state change, not by the answer to the order that happened to cross the line.

*The full listing is [Listing 27.5 in Appendix F](#code-27-5).*

## 27.8 Observability, Deployment, and Resilience Beyond Your Walls

**Replay.** Every input carries `known_at` (§27.2) and every decision is a pure function of the knowledge-time snapshot plus the code and configuration version. So any minute of any day can be replayed bit-for-bit, and "why did we bid that?" has an answer that is not a shrug. Configuration is code: versioned, checksummed, and compared across every server before the open. The Tier-2 version-skew check is just this comparison with teeth.

**Paper versus live.** The most important system metric is not latency. It is the gap between the paper portfolio and the dollar portfolio.

> **[SOURCE EXTRACTION]** *Paleologo_Advanced_Portfolio_Management p.145:* "If these skills are there pro forma in a paper portfolio, but are not realized in the dollar portfolio, then we can be assured that this has to do with the deployment of the strategy – maybe its capacity is lower than we thought – or with the execution of the strategy itself"
>
> **Annotation.** Our analysis: Paleologo writes this about a PM's skill, but it is also the definition of an infrastructure bug. Paper minus live, attributed by component (fill probability, cost model, latency-driven pick-offs, unfilled residuals from §27.4), is the desk's integration test, and it should be a dashboard line, not a quarterly post-mortem. The departure for credit is that the paper portfolio must be simulated with *provenance-typed* fills (§27.2). A paper book filled at composites will always beat the live book, and the gap will be blamed on execution when it is really the data.

**Deployment discipline.** Knight's eighth server is the archetype, and the modern one is outside the trading stack entirely. On 2024-07-19 a defective CrowdStrike content update for Windows hosts disrupted airlines and banks, and SGX's clearing arm suffered an operational failure of five hours and six minutes (Risk.net). A kernel-mode agent your security team installed is part of your latency and availability budget, whether or not anyone told the desk. Hence rings and canaries for *every* change that touches a trading host, including vendor agents, and a deployment kill switch that halts a rollout when the canary's markouts, rejects or latency drift. Finally, the "97 e-mails" rule: **an alert without an owner and an action is a log line.** Every alert names who acts, what they do, and the deadline (RTS 6 Art. 16's five seconds is a fine default for anything that can lose money).

**Beyond your walls.** On 2023-11-08/09, LockBit ransomware hit ICBC Financial Services, the US broker-dealer arm of ICBC. BNY Mellon, its Treasury settlement agent, disconnected it and settled its trades manually; ICBC FS owed BNY about \$9bn in unsettled trades until the parent injected capital (Reuters and other coverage). On 2015-04-17, Bloomberg terminals went dark for several hours from about 8:30 a.m. London, and the UK Debt Management Office postponed a gilt operation of about £3bn, citing "ongoing issues with the third-party platform supplier." And the composite and venue layer is consolidating: ICE agreed on 2026-07-29 to buy MarketAxess. Each case is the same lesson. Your fastest system is bounded by your slowest counterparty's recovery plan, so every external dependency (settlement agent, chat and pricing terminal, composite vendor, hedge venue) needs a named fallback and a Tier-2 trigger that says what happens to live quotes when it disappears.

Mags listens to all of this with her arms folded. "Back in my day the kill switch was the head trader unplugging the phone bank, and the dead-man switch was the head trader going to lunch. Nothing traded until he came back." A pause. "Fine. Yours doesn't go to lunch."

## 27.9 Desk Debrief

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

## 27.10 Sources and Links

### Deep-Dive Resource Graph

**Podcasts**

- Bloomberg *Odd Lots* (series): episodes on bond-market electronification, portfolio trading and high-frequency trading. No specific episode was verified for this chapter; search the archive by topic.
- *Flirting with Models* (Corey Hoffstein, series): practitioner interviews on systematic implementation and execution. Series-level pointer only.

**Practitioner Writing**

- Kevin McPartland, "What the buy side wants from their bond dealers," Coalition Greenwich blog, 2024-02-13. https://www.greenwich.com/blog/what-buy-side-wants-their-bond-dealers
- Fleming, Johansson, Keane and Meyer, "From the Vault: A Look Back at the October 15, 2014 Flash Rally," *Liberty Street Economics*, 2019-10-15. https://libertystreeteconomics.newyorkfed.org/2019/10/from-the-vault-a-look-back-at-the-october-15-2014-flash-rally/
- Man Group papers on systematic credit (2022 and 2023), cited from the shelf as Man_Quantitative_Credit_Alpha_Early_Mover_2022 and Man_Revolutions_in_Credit_Trading_2023.
- Arista Networks, 7130 Series product documentation (Layer 1+ devices; vendor latency specifications). Title only.
- AMD and Exegy, STAC-T0 tick-to-trade benchmark announcements (2024). Vendor claims; title only.
- The DESK coverage of auto-quoting, no-touch rates and credit futures blocks (2025-10-08, 2026-10-08, 2026-10-16), as cited in the Trend Watch boxes. Title only.

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
- SEC, Risk Management Controls for Brokers or Dealers with Market Access (Rule 15c3-5), Release No. 34-63241 (2010-11-03). https://www.sec.gov/rules/final/2010/34-63241.pdf
- SEC press release 2014-260, adoption of Regulation SCI (2014-11-19). https://www.sec.gov/news/press-release/2014-260
- Commission Delegated Regulation (EU) 2017/589 (MiFID II RTS 6, algorithmic trading). https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32017R0589
- FINRA Rule 4590, Synchronization of Member Business Clocks. https://www.finra.org/rules-guidance/rulebooks/finra-rules/4590
- FINRA TRACE overview and specifications. https://www.finra.org/filing-reporting/trace (Regulatory Notices 25-17 and 26-16: title only.)
- OpenFIGI symbology and mapping API. https://www.openfigi.com/ and https://www.openfigi.com/api
- CourtListener REST API, for the docket of *Dinosaur Financial Group LLC v. S&P Global Inc.*, S.D.N.Y. No. 1:22-cv-01860. https://www.courtlistener.com/help/api/
- This chapter's reference implementation: `ch27_desk_system.py`, blocks 1–5 above (provenance and dedupe, bitemporal master, queueing, trigger tables, kill switch).

<!-- STATUS: COMPLETE -->
