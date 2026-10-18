# Chapter 27: System Construction, Low-Latency Infrastructure & ASICs/FPGAs

<!-- WRITER PLAN (sections appended in order; resume after the last complete "## 27.x" section):
27.0 cold open; 27.1 two clocks (Trend Watch 1); 27.2 ingestion and provenance (Trend Watch 2, code block 1);
27.3 bitemporal security master (Trend Watch 3, Serta case, block 2); 27.4 OMS/EMS and the order state machine;
27.5 latency budgets as queues (CME halts case, block 3); 27.6 FPGA trigger tables (Trend Watch 4,
2014 flash rally case, block 4); 27.7 kill switches as stopping rules (Knight and Citi cases, block 5);
27.8 observability, replay, deployment; 27.9 resilience beyond your walls; 27.10 Desk Debrief, Spec, Exercises;
27.11 Deep-Dive Resource Graph. -->

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

> **Trend Watch. The robots took the RFQ, then called in sick (2020–2026).** *What changed:* the quote clock itself was automated. Tradeweb's AiEX handled more than 40% of its institutional trades in 2025, against 30% in 2021 (Tradeweb 10-K, FY2025). Trumid executed 88% of eligible RFQ line items fully no-touch in September 2025 (The DESK, 2025-10-08). In October 2026 Vanguard reported about 70% of its traded volume automated, up from about 40%, while noting it sends nothing without a trader (The DESK, October 2026). *The stress test:* in a Coalition Greenwich survey of 51 corporate bond investors in Q4 2023, "improved auto-quoting" topped the buy side's wishlist for dealers. The same post recalls that in March 2020 "several of the largest banks famously shut down their auto-quoters" because their pricing algorithms could not cope with the volatility, a lesson that later let them handle bouts of volatility (Kevin McPartland, Coalition Greenwich, 2024-02-13). In October 2026, buy-side traders told FILS Europe that electronic liquidity providers "help mainly in normal markets." *What it means for the desk:* the auto-responder is a slow FPGA with better excuses. Its parameter file is a trigger table and its "stress mode" is a kill switch with a reputation. Both belong under the same governance as the fast path in §27.6–27.7, with explicit triggers, owners and audit trails, not a trader's intuition about when the market "feels weird." The full adoption series is in §18.7.

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

```python
# ch27_desk_system.py, block 1 of 5: provenance-typed prices, clock checks, TRACE dedupe.
# Seeded; numpy/scipy/pandas only; the five blocks run in order in one interpreter.
from dataclasses import dataclass
from enum import Enum
from typing import Optional
import math
import numpy as np
import pandas as pd
from scipy import stats

RNG = np.random.default_rng(27)


class PriceKind(str, Enum):
    TRADED = "traded"                  # a print: someone paid this
    FIRM_QUOTE = "firm_quote"          # executable at this size, now
    INDICATIVE_RUN = "indicative_run"  # dealer run: not firm (Man 2022 p.19)
    EVALUATED = "evaluated"            # matrix or evaluated vendor price (Bohn-Stein p.334)
    COMPOSITE = "composite"            # blended vendor composite


TRAINABLE = {PriceKind.TRADED, PriceKind.FIRM_QUOTE}   # allowed as labels, fills, cost targets


@dataclass(frozen=True)
class PriceRecord:
    instrument_key: str
    price: float
    price_type: str
    side: str
    size_mm: float
    kind: PriceKind
    source: str
    event_ns: int
    known_ns: int
    affiliate_flag: Optional[bool] = None


def latency_ms(rec: PriceRecord, clock_err_ms: float) -> float:
    """known_at - event_time in ms; a negative value beyond the clock-error bound is a clock fault."""
    lat = (rec.known_ns - rec.event_ns) / 1e6
    if lat < -clock_err_ms:
        raise ValueError(f"clock fault on {rec.instrument_key}: latency {lat:.3f} ms < -{clock_err_ms} ms")
    return lat


def training_labels(records):
    """Only traded prints and firm quotes may become labels or simulated fills."""
    return [r for r in records if r.kind in TRAINABLE]


def trace_regime(ts: pd.Timestamp) -> str:
    """Affiliate-indicator regime (voluntary 2026-08-31, mandatory 2027-08-02, per FINRA Notice 26-16)."""
    if ts < pd.Timestamp("2026-08-31"):
        return "no_flag"
    if ts < pd.Timestamp("2027-08-02"):
        return "flag_voluntary"
    return "flag_mandatory"


def dedupe_trace(prints: pd.DataFrame, window_s: float = 1.0) -> pd.DataFrame:
    """Mark (never delete) likely affiliate duplicates.
    Rule 1: affiliate_flag True -> duplicate leg.
    Rule 2 (no flag): same instrument, equal price and size, opposite sides, within window_s -> later leg."""
    df = prints.sort_values(["instrument_key", "event_time"]).reset_index(drop=True).copy()
    df["dup"] = df["affiliate_flag"].map(lambda v: v is True).astype(bool)
    df["dup_reason"] = np.where(df["dup"], "affiliate_flag", "")
    for _, g in df.groupby("instrument_key"):
        idx = g.index.to_list()
        for pos, a in enumerate(idx):
            if df.at[a, "dup"]:
                continue
            for b in idx[pos + 1:]:
                dt = (df.at[b, "event_time"] - df.at[a, "event_time"]).total_seconds()
                if dt > window_s:
                    break
                if (not df.at[b, "dup"] and df.at[b, "price"] == df.at[a, "price"]
                        and df.at[b, "size_mm"] == df.at[a, "size_mm"]
                        and df.at[b, "side"] != df.at[a, "side"]):
                    df.at[b, "dup"] = True
                    df.at[b, "dup_reason"] = "inferred_pair"
                    break
    df["regime"] = df["event_time"].map(trace_regime)
    return df


# Sanity 1: one inferred pair; size mismatch and a 5-second gap are not duplicates.
t0 = pd.Timestamp("2026-06-15 14:00:00")
ms = lambda k: pd.Timedelta(milliseconds=k)
prints = pd.DataFrame({
    "instrument_key": ["INS-000117"] * 5 + ["INS-000245"] * 2,
    "event_time": [t0, t0 + ms(300), t0 + ms(40_000), t0 + ms(40_200), t0 + ms(90_000), t0, t0 + ms(5_000)],
    "price": [97.25, 97.25, 97.10, 97.10, 97.00, 101.50, 101.50],
    "size_mm": [5.0, 5.0, 2.0, 1.0, 3.0, 1.0, 1.0],
    "side": ["S", "B", "S", "B", "S", "B", "S"],
    "affiliate_flag": [None] * 7,
})
deduped = dedupe_trace(prints)
assert int(deduped["dup"].sum()) == 1
assert deduped.loc[deduped["dup"], "dup_reason"].iloc[0] == "inferred_pair"
assert set(deduped["regime"]) == {"no_flag"}

# Sanity 2: provenance gate and clock-fault detection.
recs = [PriceRecord("INS-000117", 97.25, "PRICE", "B", 5.0, PriceKind.TRADED, "TRACE", 0, 2_000_000),
        PriceRecord("INS-000117", 97.40, "PRICE", "M", 0.0, PriceKind.COMPOSITE, "VENDOR_X", 0, 500_000),
        PriceRecord("INS-000117", 97.30, "PRICE", "B", 2.0, PriceKind.INDICATIVE_RUN, "RUN_PARSER", 0, 9_000_000)]
assert [r.kind for r in training_labels(recs)] == [PriceKind.TRADED]
assert abs(latency_ms(recs[0], clock_err_ms=0.001) - 2.0) < 1e-12
try:
    latency_ms(PriceRecord("INS-000117", 97.0, "PRICE", "B", 1.0, PriceKind.TRADED, "TRACE", 5_000_000, 0), 1.0)
    raise AssertionError("negative latency beyond the clock bound must raise")
except ValueError:
    pass
```
