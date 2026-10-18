# Chapter 10: Trend-Following & Time-Series Momentum in Credit


## 10.0 Cold Open: The Model Has No Amygdala

*The desk, its cast and its positions are fictional; the spreads are ICE BofA via FRED.*

At 4:02 p.m. on Thursday, 15 October 2026, the desk's trend book did something it had not done since the spring: it bought protection on CDX HY. The position was not large, but it was large enough that Ines walked over holding her coffee the way she holds a chip she has not yet decided to bet.

"Theo. Why are we long protection? Is the model panicking?"

Theo had been on the desk three weeks, and he had learned to answer a question about a model with a chart before an opinion. "High yield has widened about fifty-five basis points in three weeks. ICE BofA HY OAS was 2.68% on September 22 and it's 3.23% today. The fast sleeve crossed."

"The model cannot panic," Kaz said without looking up. "It has no amygdala. It has a 60-day EWMA."

"A 60-day EWMA is what an amygdala looks like when a quant writes the spec," Ines said.

Theo pulled up the sleeve's blotter, partly to have something to do with his hands. The trend book was not one rule but a small committee of them, and the committee had not voted unanimously. The fast sleeve, a 20-day average of the CDX HY excess-return index set against a 120-day one, had crossed below zero at 3:41 and sent a ticket for protection *(illustrative, like every position in this scene)*. The slow sleeve, the one that asks only whether the index made money over the last twelve months, was still long risk. Until about 3:59 Theo had assumed that fifty-five basis points of widening would have turned it too.

"The twelve-month sleeve hasn't moved," he said. "Fifty-five basis points wider, and it still thinks we're in an uptrend."

"Does it?" Ines said.

He did the arithmetic on the back of a cleansing-announcement template he still kept in his drawer, because old paper is good for new sums. CDX HY pays its spread every day, whether anyone is watching or not. At the four and a half percent of running spread this book uses as its working number for high yield, and a duration of about four, a year of that carry pays for roughly a hundred and twelve basis points of widening before the twelve-month return goes negative. (Today's OAS is lower than the working number, so the true hurdle is smaller; the napkin wants the order of magnitude.) "On the napkin, we've used up half of it," he said. "Fifty-five out of a hundred and twelve. The slow sleeve isn't ignoring the widening. It's being paid to sit through it."

Kaz wrote "55/112" on a yellow sticky note and stuck it to the bottom of their monitor, which from Kaz is the highest compliment available.

"And before you ask," Kaz said, turning the monitor so the row could see it, "the long was already smaller before anything flipped." On the screen was the sleeve's notional: a line that had drifted down for three weeks like a tide going out. "The risk forecast scales with the spread. Duration hasn't moved, spreads went from 2.68 to 3.23, so a position that targets constant risk is 2.68 over 3.23 of what it was." They typed it into the terminal's calculator, which is the only thing Kaz trusts less than a vendor feed. "Zero point eight three. We sold seventeen percent of the long without a single signal changing its mind."

"Who told it to do that?" Theo asked.

"Nobody. The volatility forecast. Wider spreads move more, so the same risk budget buys less." Kaz paused. "It is a forced seller with a very good excuse."

Mags spoke from the end of the row without turning her chair. "It looks like April of last year: a hundred and nineteen basis points in three sessions, and all of it back inside six weeks. It also looks like the summer of 2007, and it looks like nothing at all." Now she turned. "Back in my day we had trend-following in credit. It was called 'Sal stopped picking up the phone.' When your dealer stopped returning calls, you sold whatever you could and asked questions at Christmas."

She held up one finger for each future, the way she counts a creditor class. "April. The index was 3.42 on the second, the day of the Rose Garden, and 4.61 on the seventh. Three sessions. By the middle of May it was back near three, and anyone who sold on the seventh paid for the privilege." A second finger. "2007. Nothing happened in a hurry. It widened all summer, it widened all autumn, it was still widening a year later, and Baa paper did not stop until it was six hundred and sixteen over Treasuries on the fourth of December 2008. If you were short in August 2007 you had sixteen months of being right." A third finger. "Nothing. August 2024. The index touched 3.93 on a Monday, on a yen trade nobody in this building could have explained to you on the Friday, and by September you had to look at a chart to remember it."

"Same tape on the first day," Kaz said. "All three."

"Same tape on the first day," Mags agreed. "Different bonds by Christmas."

"So which one is it?" Theo asked.

"That's the hand," Ines said. "What's the pot, what are the odds, and who at this table knows more than you?"

Theo looked at the position. In his old job a bond at 60 always had momentum, toward a process. It was never heading toward 40 or toward 80, but toward a lender call, a cleansing announcement, a filing, or a deal. Restructuring bankers watch prices move all day, and they never believe the move *is* the information. Now he sat on a desk with a robot that believed nothing else.

The rest of the chapter answers the question on Theo's screen: **when is a move in credit spreads information about the next move in credit spreads, and how much should you bet on it?**

It answers it the only honest way available, which is not by telling Theo which of Mags's futures he is in. Each of her futures has a formula somewhere in the next fifty pages: the carry hurdle he just found on the back of a template, the volatility law that sold seventeen percent of the long while nobody was looking, the blend in which carry and value pull against trend exactly after a widening like this one, the equity market that tends to move before the bond prints, the payoff shape that pays in a 2007 and bleeds in an April, and the jump that makes all of it the wrong tool for a single name. None of the formulas picks a future. Together they say what the position is worth in each one, and how to keep the bet small until the market says which.

Ines put her coffee down on Theo's desk, the way she puts down a chip she has decided to bet, and slid a blank index card out from under it.

"By Monday," she said, "write three things: the size you want, the speed you want it to think at, and the print that makes you cover."

"And if I pick the wrong future?"

"Then you'll have been wrong in writing, which puts you ahead of most of this table." She picked the coffee back up. The card stayed on Theo's desk, white and blank. Across the row, the sticky note on Kaz's monitor still said 55/112.

## 10.1 What a Trend Is, in Credit

*A remembered meeting; the client, its bonds and its holders are fictional.*

Theo had sat in that room. In his third year at PJT a client he will not name, a packaging company with a sponsor and a revolver due in eighteen months, printed a quarter that missed by less than anyone had feared, and its bonds fell five points by lunch anyway. The CFO wanted to know whether the bonds were cheap. The managing director did not answer that question. He asked a different one, "who is selling, and are they done?", and over the next fortnight the answer arrived in pieces. A long-only manager had hit its stop-loss on the name. A relative-value fund had breached its issuer DTS cap without trading at all, because DTS rises with the spread and the widening had done the breaching for it. An insurance mandate had a "reduce on downgrade" clause and the agency had put the credit on watch. A hedge fund's risk committee had met after a bad month, as risk committees do, and come out smaller. Not one of those sellers would have called itself a trend follower. Each was running a rule that sold after the price fell, and between them they were the trend. Theo's managing director had a phrase for the moment the selling stopped, which was "the last guy with a rule is out," and he was usually right about it about a week late.

The systematic desk takes that reflex, writes it down, gives it units, and asks the uncomfortable question the committee never asks: *does it make money, net of the times it sold the low?*

Two words get used interchangeably on credit desks and should not be.

> **[SOURCE EXTRACTION]** *Paleologo_Advanced_Portfolio_Management p.74:* "“Momentum” has a different meaning from trend-following, because it is based on relative performance, whereas the latter is based on absolute performance."
>
> **Annotation.** This is the one distinction to get right before any code is written. Cross-sectional momentum, which is Chapter 9's subject, ranks bonds against each other: it buys the issuers that beat the index and sells the ones that lagged, and it can be fully long-short and market-neutral. Time-series momentum, or trend, compares each instrument only with its own past: if CDX HY's excess return over the last twelve months was positive, you are long risk, whatever happened to anything else. The two have different risk. A cross-sectional book in a 2008-style sell-off can be long the bonds that fell least and still lose money in a short squeeze. A trend book in the same sell-off ends up short the whole market, which is the point and also the danger. Credit makes the distinction sharper than equities do, for two reasons. The cross-section is a few hundred illiquid issuers with stale prints, so cross-sectional momentum lives in cash bonds and their cost structure. The time series can be traded in a handful of liquid indices, so trend lives mostly in CDX and iTraxx. They are different trades in different instruments with different P&L drivers. A 2026 desk keeps them in separate risk buckets and separate reports, and it does not let a good year in one excuse a bad year in the other.

### 10.1.1 The instruments, and why index CDS is the futures-like leg

Trend-following was born in futures because futures are cheap to trade, cheap to short, standardized, and continuously quoted. Credit has exactly one instrument family that passes all four tests:

| Instrument | Names | Fixed coupon | Quoted as | Role for trend |
| :--- | :--- | :--- | :--- | :--- |
| CDX.NA.IG | 125 | 100 bp | spread | Core US IG trend leg |
| CDX.NA.HY | 100 | 500 bp | price | Core US HY trend leg |
| iTraxx Europe (Main) | 125 | 100 bp | spread | European IG |
| iTraxx Crossover | 75 | 500 bp | spread | European HY |
| Cash index excess return (ICE BofA, Bloomberg) | thousands of bonds | n/a | OAS, excess return | Research and benchmarking, not trading |
| HYG / LQD and peers | ETF baskets | n/a | price | Tradable cash proxy, with an ETF basis |
| Cboe iBoxx futures (IBHY, IBIG); CME credit futures | index | n/a | price | Listed route for futures-only CTAs |

The on-the-run index CDS is *unfunded* (no cash changes hands beyond the upfront), *standardized* (fixed coupons, quarterly IMM payment dates, a new series every 20 March and 20 September), *cleared*, and quoted by dealers all day. It is born an excess return: there is no Treasury leg to hedge, because selling protection carries no interest-rate duration to first order. Every one of those properties is missing in a cash bond.

Kaz had once heard Ines say "Crossover" on a call and spent twenty minutes drafting what they believed was a cross-default clause. "It's 75 sub-investment-grade European names, Kaz," Ines told him. "The only thing it crosses is your P&L in March."

**Sign conventions, which cause more bugs than any model choice.** Spread up means price down. "Long risk" means you *sold* protection and are long credit. Throughout the chapter a weight $w>0$ is long risk and $w<0$ is long protection. CDX HY and the Crossover's price-quoted cousins move the opposite way to their spreads. ROBO will happily build a strategy that is long when spreads tighten and *also* long when the price rises, if both columns are named `level`. Name them `spread_dec` and `price_pts`.

#### Quant-Shop Life: The Tuesday of Roll Week

*Fictional composite: a systematic asset manager running long-only credit with a small index overlay. The firm, its vendor, the people, the ticket and every number are invented.*

The overnight job failed at 2:14 a.m. on Tuesday, 22 September 2026, and nobody noticed until Lucía Ferrer, a second-year research associate, got in at 7:40 and saw one red line on a dashboard of green ones. The job rebuilds the CDX HY excess-return history from the vendor's file every night, from the first series to yesterday, and then runs a suite of guards over it. The history is what the overlay's trend signal is computed from, and nobody wants to learn from the PM that it is wrong. The guard that failed was the dullest in the suite: on any day when the index's spread did not move, it insists that the day's return be the carry and nothing else, the spread times the days elapsed over 360. It had passed every night for three years. Last night it failed on exactly one day, Friday 20 September 2019.

She spent the morning finding out why. The answer was in a release note the vendor had sent the previous Friday, which nobody on her team had opened, because vendor release notes arrive at about four a week and are written to be ignored. From the September 2026 roll the vendor had changed how it labeled series, and it had applied the change to the whole history. On each roll date the file now carried two rows under the same generic label, the old series and the new, and her pipeline's de-duplication kept the second. On 20 September 2019 that meant subtracting the old series' Thursday close from the new series' Friday close. The new series is three months longer and holds a different hundred names, so it trades wider: about ten basis points wider that day *(illustrative)*. The pipeline booked the gap as a ten-basis-point widening that never happened, roughly forty cents of loss per hundred of notional at a duration near four. It fell on a day when the old series had closed unchanged, which is the only reason the guard could see it.

The guard saw one day. Lucía checked all of them. Every roll date in the restated history carried the same phantom, twice a year, every year: a fake widening on the day the series changed. On the roll dates when the overlay had been short, September 2008 and March 2020 among them, the phantom was a fake gain. The backtest's crisis alpha had been flattered by the calendar.

The fix was eleven lines: carry a `series_id` on every row and refuse to compute a return across two of them. The ticket took longer to write than the fix. She opened QR-3307, titled it "Vendor relabel splices series on roll dates; returns computed across series," attached the 2019 row and the list of forty-one roll dates, and, because she was already annoyed, added an item she had been meaning to raise for a month: the vendor annualizes volatility with 261 days and her code with 252, and the difference rescales every volatility-targeted weight by about 1.8%. Nobody had ever decided which was right. Somebody needed to.

At 4:30 she wrote the e-mail to the PM, which is the part of the job no recruiting brochure mentions. "Rebuilt CDX HY ER history after a vendor relabel. Backtest Sharpe of the overlay's trend sleeve moves from 0.61 to 0.58 (2006–2026). About two-thirds of the change is the roll-day fix, which removes fake gains on roll dates when the sleeve was short, mostly 2008 and 2020; the rest is moving annualization to 252 to match the risk system. Production computes returns within series, so no live position is affected." The PM replied at 4:41 with "thanks" and a question nobody could answer, which was why a vendor would restate twenty years of history during a roll week.

### 10.1.2 Trend on returns, not on spread levels: the carry hurdle

The first derivation is short, and it reverses a desk intuition, which is why the sticky note on Kaz's monitor says 55/112 and not 55/0.

> **Math, Gently.** *Excess return, and why a falling price can be a good year.* Picture a landlord whose house is worth 2% less at the end of the year than at the start, in a year in which it paid 4.5% in rent. Nobody calls that a losing year: the rent paid for the dent and then some. A long-risk credit position is that landlord. It collects the spread every day as rent (the *carry*), it marks itself down when spreads widen (the *price change*), and once a Treasury hedge has taken away the interest-rate part, what is left is the *excess return*: rent plus dent. Put numbers on it. High yield at 450 bp, spread duration 4, widens by 60 bp over a year. The dent is $-4 \times 60 = -240$ bp; the rent is $+450$ bp; the year's excess return is $+210$ bp. The spread chart went the wrong way all year and the ledger went the right way, so a rule that reads the chart calls this a downtrend and a rule that reads the ledger calls it an uptrend. In symbols, one period's excess return is carry minus duration times the spread change, $s\,\Delta t - D\,\Delta s$. Add up a year of those and ask how large the widening has to be before the sum turns negative: that number is the hurdle, and it is next.

Let $s_t$ be the spread in decimal, $D^{\text{spr}}$ the spread duration, and $\Delta t$ the accrual year fraction (ACT/360 for CDS premium). To first order, the excess return of a long-risk position over one period is

$$
r^{ex}_{t+1} \approx s_t\,\Delta t - D^{\text{spr}}\,\Delta s_{t+1}.
$$

TSMOM signals on the trailing cumulative excess return over $h$ periods, which we write $M^{(h)}_t$ (we use $M$ because $S$ is already taken by survival probability and the mid):

$$
M^{(h)}_t = \sum_{k=0}^{h-1} r^{ex}_{t-k} \approx \underbrace{\bar s\, h\,\Delta t}_{\text{carry earned}} - \underbrace{D^{\text{spr}}\,(s_t - s_{t-h})}_{\text{MTM}} ,
$$

where $\bar s$ is the average spread over the window. The signal turns short only when $M^{(h)}_t<0$, that is, when

$$
s_t - s_{t-h} > \frac{\bar s\,h\,\Delta t}{D^{\text{spr}}} \equiv \Delta s^{*}_h .
$$

This is the **carry hurdle**. For high yield at $\bar s = 4.5\%$ with $D^{\text{spr}} = 4$ and a 12-month window ($h\,\Delta t = 1$), $\Delta s^*_{12} = 0.045/4 = 112.5$ bp *(illustrative)*. HY spreads have to widen by more than about 110 bp over a year before a return-based 12-month trend follower goes short; the landlord's 60 bp year is comfortably inside it. For IG at 1.0% spread and $D^{\text{spr}}=7$, the hurdle is about 14 bp. Figure 10.1 plots the hurdle and shows, on two years of real HY data, how often it separates a rule on spread changes from a rule on returns.

![Figure 10.1: The carry hurdle is the widening a 12-month return rule needs before it goes short, about 14 bp for IG and 112.5 bp for HY (left), so over the 534 trading days with a full 12-month window a rule on spread changes was short on 150 days while a rule on returns was short on only 13 (right). Source: ICE BofA US High Yield OAS via FRED (BAMLH0A0HYM2), 2 October 2024 to 15 October 2026, with the hurdle computed as the trailing 252-day mean OAS divided by D = 4 (assumed). Illustrative: the left panel is the formula of §10.1.2 with the spreads and durations shown.](assets/figures/ch10_carry_hurdle.png)

Ines had the chart on the whiteboard by half past four that Thursday, two bars in blue marker, one short and one tall. "Fourteen," she said, tapping the short one, "and a hundred and twelve. Same rule, same twelve months. In IG the carry is small next to the duration, so the rule turns as soon as spreads lean on it. In HY the carry is large next to the duration, so the rule sits through a widening that would have flipped IG twice. A desk that runs one lookback across both is running two strategies under one name."

"Then the spec has to say which one it means," Theo said.

"It has to say which one it means. A rule on the twelve-month change in OAS and a rule on twelve-month returns are different strategies, and the difference between them is this bar." She drew an arrow from the tall bar to the edge of the board. "Now the part nobody likes. In normal times the rent keeps paying, so the HY rule stays long. For most of any year a credit trend follower is a credit-beta holder that has reserved the right to change its mind." (Section 10.6 turns that sentence into a payoff diagram.)

"IG prints five to nine hundred trades a day," Kaz said. "It can afford to change its mind often."

"It can afford to," Ines said. "Whether it ought to is a turnover question, and turnover has its own section." (It is §10.8.) She capped the marker. The venue Kaz was pointing at did not exist in that form five years ago, which is the subject of the box below.

> **Trend Watch: The index CDS market becomes the trend follower's venue, 2021–2026.** *What changed:* index CDS activity reached records while single-name activity stalled. ISDA's research note of 29 July 2026 puts total CDS trading at \$41.8tn in 2025, against a prior peak of \$38.7tn in 2022 and \$31.4tn in 2023. Index products were 93.3% of that, a record \$39.0tn (\$36.4tn in 2022, \$28.1tn in 2023), while single-name activity peaked at \$3.3tn in 2023 and fell to \$2.8tn in 2025. CDX.NA.IG was 43.4% of 2025 index activity, iTraxx Europe 32.4%, CDX.NA.HY 10.4%, and iTraxx Crossover 7.7%. CDX.NA.IG prints 500–900 trades a day, with more than 900 in Q2 2025. In stress the venue gets busier: index activity in Q1 2020 ran 78.1% above its trailing average, and in Q2 2025 it ran 20.9% above while single-name activity fell 20.7%. H1 2026 activity was \$27.4tn, up 27.8% year on year (ISDA, *CDS Market Dynamics: Five Years of Activity and a Record 2025*). Clearing and electronic execution are close to universal: more than 99% of the three benchmark indices cleared, and SEF share was 96.5–98.0% in H1 2025 (ISDA SwapsInfo H1 2025). Clarus reports cleared USD CDX of \$3.94tn in March 2026, up 46% year on year. *The listed route:* Cboe iBoxx credit futures block trades topped \$1bn a month for a second month in August 2026, and IBIG block activity overtook IBHY's for the first time (The DESK, 16 October 2026). *What it means for the desk:* the instrument trend needs, cheap two-way risk in size during a sell-off, now exists in credit at index level. It does not exist at single-name level, where activity is shrinking. Credit trend is an index strategy, and §10.9 explains why single-name trend has to be a different engine.

## 10.2 The TSMOM Engine, Adapted

### 10.2.1 The Moskowitz–Ooi–Pedersen template

Moskowitz, Ooi, and Pedersen (2012), *Time Series Momentum*, define the strategy the whole industry now benchmarks against. In 58 liquid futures (equity indices, currencies, commodities, and sovereign bonds), the past 12-month excess return predicts the next month's return, persistence lasts one to twelve months and then partially reverses, and a diversified portfolio "performs best during extreme markets." Their sample contains **no credit instruments**. Everything in this chapter is therefore an out-of-sample transplant, and the transplant has rejection risks.

For instrument $i$ with excess return $r^{ex}_{i,t}$, the template is

$$
\text{sig}^{(h)}_{i,t} = \operatorname{sign}\!\big(M^{(h)}_{i,t}\big), \qquad
w_{i,t} = \frac{\sigma_{\text{tgt}}}{\hat\sigma_{i,t}}\;\text{sig}^{(h)}_{i,t}, \qquad
r^{\text{TSMOM}}_{t+1} = \frac{1}{N}\sum_{i=1}^{N} w_{i,t}\, r^{ex}_{i,t+1}.
$$

Here $h$ is the lookback (12 months in the headline result), $\hat\sigma_{i,t}$ is the ex ante annualized volatility, and $\sigma_{\text{tgt}}$ is the volatility target per instrument. MOP estimate $\hat\sigma$ from an exponentially weighted average of squared daily returns with a center of mass of 60 days, and they set $\sigma_{\text{tgt}} = 40\%$ per instrument so that the diversified portfolio lands near a conventional overall volatility. Both are their choices, not laws. The weight is known at $t$ and earns the return from $t$ to $t+1$. Get that one-period lag wrong and the backtest will look wonderful, because you will have taught the model to read tomorrow's newspaper.

That one phrase, "exponentially weighted with a center of mass of 60 days," is doing most of the work in every volatility-targeted strategy in this book, including the one that sold seventeen percent of the long in the cold open.

> **Math, Gently.** *An EWMA is a memory with a half-life.* Picture a bucket with a slow leak. Every evening you pour in today's squared return; overnight the bucket loses one sixty-first of whatever it holds, so yesterday's pour is worth 60/61 of what it was, and the day before's is worth $(60/61)^2$. The level in the bucket is the variance estimate: a quiet month lets it drain, one violent day fills it at once, and nothing ever quite leaves. The leak rate sets the memory. With $\delta = 60/61$, a return from 60 trading days ago still counts for $\delta^{60} \approx 0.37$ of what today's counts for, one from 180 days ago for about $0.05$, and the half-life, the age at which a day's weight has halved, is about 42 trading days. A fixed 60-day window would count day 60 fully and day 61 not at all, and its estimate would lurch on the day a bad print aged out; the bucket fades the print instead. The formula below is the bucket written down, with 261 turning a daily variance into an annual one.

The EWMA with center of mass 60 days has decay $\delta$ satisfying $\delta/(1-\delta) = 60$, so $\delta = 60/61$, and

$$
\hat\sigma^2_{i,t} = 261 \sum_{k\ge 0} (1-\delta)\,\delta^{k}\,\big(r_{i,t-k}\big)^2 ,
$$

with 261 converting daily to annual (MOP's choice; this chapter's code uses the 252-day convention, and the difference is a 1.8% rescaling of every weight that a spec must pin down). MOP subtract an EWMA mean inside the square; in credit index returns that mean is small next to the dispersion, and we drop it.

Theo, reading this, pulled up his 13-week cash flow model. "Thirteen weeks is 65 trading days," he said. "That's within rounding of their 60-day window." Kaz was delighted. Ines was not. "Your model measures how long the cash lasts. Their window measures how long *volatility* lasts. Both are memory horizons, and neither one is a trend horizon. Your company didn't run out of cash because the last thirteen weeks trended." She was right, and the distinction recurs in §10.3: volatility is persistent over weeks, while returns trend over months, if they trend at all.

### 10.2.2 Smoother signals and ensembles

The sign function is a cliff. A return of +1 bp and one of +900 bp produce the same position, and a series sitting near zero flips back and forth, trading its whole size on noise. Two standard fixes:

$$
\text{sig}^{\text{xo}}_{t} = \tanh\!\left(\frac{\text{EWMA}_{f}(I_t) - \text{EWMA}_{s}(I_t)}{\hat\sigma^{\text{lvl}}_t}\right),
\qquad
\text{sig}^{\text{ens}}_{t} = \frac{1}{|\mathcal H|}\sum_{h\in\mathcal H}\operatorname{sign}\big(M^{(h)}_t\big).
$$

In the first, $I_t$ is the cumulative excess-return index (never the spread), $f<s$ are fast and slow spans, and $\hat\sigma^{\text{lvl}}_t$ is the volatility of the gap between the two averages, which makes the argument a z-score. If the sign function is a light switch, the tanh is a dimmer: near zero it turns the position up gradually, and far from zero it saturates at full size. SG's published CTA "Trend Indicator" is a 20-day/120-day crossover (SG Prime Services, May 2025). In the second, $\mathcal H = \{1, 3, 6, 12\}$ months gives a signal in $\{-1, -\tfrac12, 0, \tfrac12, 1\}$ that scales down when horizons disagree. Dynkin's equity-momentum signal for credit (§10.5) uses the same multi-horizon idea for the same reason.

### 10.2.3 Building the return series correctly

Every trend backtest in credit stands or falls on the return series. The signal is ten lines of code; the returns are a week of work.

**Index CDS return, derived.** Consider a long-risk (protection-sold) position per unit notional in an index with fixed coupon $c$ and par spread $s_t$. Its mark-to-market value is approximately $V_t = (c - s_t)\,\text{RPV01}_t$, where $\text{RPV01}_t$ is the risky annuity, the present value of 1 per year paid until default or maturity. It is a $\mathbb{Q}$ quantity, computed from the ISDA standard model. (We write RPV01 rather than $A$ because $A$ is the order-arrival parameter in this book's notation.) Over one period the position receives the coupon accrual $c\,\Delta t$ and changes value by $V_{t+1}-V_t$.

*Step 1, spreads unchanged.* With $s$ fixed, the annuity shortens by roughly $\Delta t$ (ignoring discounting and survival over one short period), so $V_{t+1} - V_t \approx (c - s)(\text{RPV01}_t - \Delta t) - (c-s)\text{RPV01}_t = -(c-s)\,\Delta t$. The upfront amortizes.

*Step 2, total carry.* Adding the coupon gives $c\,\Delta t - (c-s)\,\Delta t = s\,\Delta t$. The carry of index CDS is the *par spread*, not the fixed coupon. The upfront paid or received at entry is exactly the present value of the difference.

*Step 3, spread change.* Differentiating $V$ in $s$ gives $\partial V/\partial s = -\text{RPV01} + (c-s)\,\partial \text{RPV01}/\partial s \approx -\text{RPV01}$ near par, plus a small second-order term. Collecting,

$$
r^{ex}_{t+1} \approx \underbrace{s_t\,\Delta t}_{\text{carry}} \;-\; \underbrace{\text{RPV01}_t\,\Delta s_{t+1}}_{\text{mark-to-market}} \;+\; \underbrace{\tfrac12\,\Gamma_t\,(\Delta s_{t+1})^2}_{\text{convexity}},
\qquad \Gamma_t = \frac{\partial^2 V}{\partial s^2} > 0 .
$$

Because the position is unfunded, this already *is* an excess return. For a cash index the analogue is $r^{ex}_{t+1} \approx s_t\,\Delta t - D^{\text{spr}}_t\,\Delta s_{t+1}$ over duration-matched Treasuries, which is the definition behind the Bloomberg and ICE excess-return series. Signals and performance statistics in this chapter are all under $\mathbb{P}$: they are about what actually happens to returns. The one $\mathbb{Q}$ object is $\text{RPV01}$, which converts a spread change into money.

Lucía's ticket from §10.1.1 ended with a section headed "What the pipeline assumes," three short paragraphs she wrote so that the next associate would not have to discover them on a Tuesday. They are the rest of this section's rules, and they read better as her paragraphs than as a list.

The first was about the high-yield index. "CDX HY quotes a price, not a spread: $P_t = 100 + 100\,(c - s_t)\,\text{RPV01}_t$ in points. We build its return straight from the price, $r_{t+1} = (P_{t+1} - P_t)/100 + c\,\Delta t$, and we do not convert to spread and back. The conversion needs a curve and a recovery assumption, and the round trip is a quiet source of drift."

The second was the one that had just bitten her. "A new on-the-run series starts every 20 March and 20 September, five years and three months long, with defaulted and downgraded names swapped out. ISDA notes that the roll window carries 25–50% of quarterly index notional. The new series quotes at a different spread, because it is three months longer on an upward-sloping curve and its constituents differ. So each day's return is computed within one series, and the index switches series on the roll date. Spreads are never differenced across series." Written as an equation, the total-return index she rebuilt that afternoon is

$$
I_{t+1} = I_t\,\big(1 + r^{(k)}_{t+1}\big), \qquad k = \text{series held from } t \text{ to } t+1 .
$$

The gap between old and new series on roll day is not only a data hazard; it is a basis that dealers price and some funds trade, and Chapter 10-B owns it.

The third was about the calendar, and it was the guard that had caught her. "CDS accrues ACT/360. Over a weekend, three days of carry arrive on Monday, and the flat-spread guard checks exactly that amount."

> **Ways This Blows Up.** *The spliced series, in IG.* Lucía's phantom has a cousin in investment grade. An analyst downloads "CDX IG 5Y generic" spreads, which a vendor stitches across series, and differences them. Every roll day then shows an artificial widening of a few basis points (the maturity extension), which with $\text{RPV01}\approx 4.5$ is a fake loss of about 0.1–0.2% *(illustrative)*, twice a year, every year. A 12-month trend signal sums two of those, so it carries a small bias toward short. Worse, a defaulted name dropping out of the HY series can show up as a fake *rally*. The fix is the structural one in her eleven lines: a `series_id` on every row, and an assertion that no return is computed across two different `series_id` values. *The day count.* A strategy that ignores ACT/360 treats Mondays as unusually good days, and a short-horizon signal will discover "the Monday effect in credit" and trade it.

**Lag and staleness.** The CDX close is a dealer-composite mark around 4 p.m. New York, and European indices close earlier. Cash bond OAS is a pricing-service evaluation, often of a bond that did not trade that day. A signal computed on the close at $t$ and executed the next morning earns the return from $t+1$ to $t+2$, not from $t$ to $t+1$, and the backtest that pretends otherwise is trading on marks that were still being typed. Running it with a one-day and a two-day lag and reporting both is cheap insurance. Dynkin's team runs the same check for equity-to-credit signals (§10.5).

## 10.3 Volatility Scaling Is DTS Scaling

Ines had watched the trend book through April 2025 and asked the question every credit PM asks a vol-targeted strategy exactly once: "Spreads went from 342 to 461 and the signal hadn't even flipped yet. Why did our notional fall by a quarter?"

Because the strategy was doing what credit risk managers have always done, with a formula instead of a meeting.

> **Math, Gently.** *When the noise grows with the level.* Statisticians call it heteroskedasticity, which is a long word for a thermometer whose markings get wider as it gets hotter. At 300 bp an ordinary day might move a spread 6 bp; at 600 bp the same kind of day moves it 12. The size of a normal move is not a constant of nature but a fraction of where the spread already is. A risk manager can do the consequence on a napkin. If a day's move is proportional to the spread, a position that wants the same risk every day holds less of a wider credit. In April 2025 high yield went from 342 bp to 461 bp; with duration roughly unchanged the risk per unit of notional rose by 461/342, so a constant-risk position ended up holding $342/461 \approx 0.74$ of what it had held, a quarter smaller, and nobody touched a parameter. The law with a slope and an intercept comes next, and the surprise is the intercept.

### 10.3.1 The derivation

Ben Dor and coauthors' central empirical law for credit is that the volatility of spread changes is proportional to the spread level:

$$
\sigma(\Delta s_{i,t}) = \alpha + \beta^{\text{DTS}}\, s_{i,t}, \qquad \alpha \approx 0 .
$$

We write $\beta^{\text{DTS}}$ (relative spread volatility, annualized and dimensionless) to keep it apart from the factor loadings $\beta_{i,k}$ of Chapter 8.

> **[SOURCE EXTRACTION]** *Ben_Dor_Quantitative_Credit_Portfolio_Management p.74:* "The estimates of α are always insigniﬁcant, indicating once more that the relation between spread volatility and spread level is best described by a linear function that intersects the origin (i.e., α is equal to zero)."
>
> **Annotation.** This sentence is why DTS exists, and it is also why a credit trend follower behaves like a forced seller. A zero intercept means that a bond at 600 bp is, to first order, twice as volatile in spread terms as a bond at 300 bp, *whatever its rating*. Volatility belongs to the spread, not to the label. For the trend desk the consequence is mechanical: any rule that targets a constant volatility must hold a constant DTS, so its notional moves inversely to the spread. The modern desk departs from the original in two ways. First, it estimates $\beta^{\text{DTS}}$ by bucket and by regime instead of treating it as a constant. Relative spread volatility rose in 2008 and in March 2020, so a $\beta$ fitted to calm years understates risk exactly when the position needs to shrink. Second, at the very tightest IG spreads the proportional law makes forecast volatility collapse toward zero, which would make a vol-targeted position explode. The production fix is a volatility floor. Without it, a 60 bp index looks like a riskless asset to a formula that has never met a gap.

With $\sigma(r^{ex}_i) \approx D^{\text{spr}}_i\,\sigma(\Delta s_i)$ from §10.1.2, substitute the law:

$$
\sigma(r^{ex}_{i,t}) \approx D^{\text{spr}}_{i,t}\,\beta^{\text{DTS}} s_{i,t} = \beta^{\text{DTS}}\,\text{DTS}_{i,t}
\quad\Longrightarrow\quad
w_{i,t} = \frac{\sigma_{\text{tgt}}}{\beta^{\text{DTS}}\,\text{DTS}_{i,t}}\;\text{sig}_{i,t}.
$$

Read the weight and the position's DTS exposure falls out: $w_{i,t}\,\text{DTS}_{i,t} = (\sigma_{\text{tgt}}/\beta^{\text{DTS}})\,\text{sig}_{i,t}$, which does not depend on the spread. Volatility targeting in credit is a constant-DTS budget, and Ines's quarter is the thermometer's 0.74 with a date on it.

That budget makes the exposure anti-momentum in spreads before any signal has an opinion. Taking logs, $d\log|w_t| = -\,d\log s_t$ (holding duration fixed). A vol-targeted long-only credit book, with no trend signal at all, sells after widening and buys after tightening. It is half a trend follower before it has a signal. Kaz found this deeply satisfying and Theo found it alarming, which is the correct split.

Because the weight now moves for two reasons, the P&L can be split by reason, a sign part and a timing part. Write $w_t = \bar w\,\text{sig}_t + \bar w\,\text{sig}_t\,(\sigma_{\text{tgt}}/\hat\sigma_t - 1)$ with $\bar w = 1$. The first term is the pure sign strategy, and the second is a volatility-timing overlay. Kim, Tse, and Wald, *Time Series Momentum and Volatility Scaling*, report for 55 futures over 1985–2013 that TSMOM's monthly alpha is 1.27% *with* volatility scaling and 0.41% *without*: most of the headline result came from the scaling. In credit the timing term and the signal term point the same way after a widening (both cut long risk), so they compound. That is good in 2008 and expensive in April 2025. Figure 10.2 shows the proportional law on real rating-bucket data and the notional it implied through April 2025.

![Figure 10.2: Spread volatility is roughly proportional to spread level across rating buckets (left), so a constant-risk position must shrink as spreads widen: in April 2025 the DTS forecast cut notional to 0.74 and rebuilt it as spreads retraced, while a 60-day EWMA cut harder on the gap days (to 0.61 by 4 April) and was still at 0.70 at the end of June (right). Source: ICE BofA OAS via FRED (BAMLC0A1CAAA, BAMLC0A2CAA, BAMLC0A3CA, BAMLC0A4CBBB, BAMLH0A1HYBB, BAMLH0A2HYB, BAMLH0A3HYC for the left panel, quarterly windows from 17 October 2023 to 30 September 2026, line fitted through the origin (R² 0.62; log-log slope 0.86, a little under proportional); BAMLH0A0HYM2 for the right panel), with daily returns approximated as s/252 − 4Δs and the DTS coefficient estimated on 2023–24 data only.](assets/figures/ch10_dts_vol_scaling.png)

> **[SOURCE EXTRACTION]** *Paleologo_Advanced_Portfolio_Management p.106:* "Volatility is persistent and partially predictable, while PnL has no strong relationship to volatility."
>
> **Annotation.** This is the general argument for volatility targeting, and credit satisfies both halves. Spread volatility is persistent, and because of the proportional law it is visible *in the spread itself* on the same day, without waiting for a window of returns. A DTS-based forecast reacts at once, while an EWMA forecast needs weeks of realized moves to catch up. The second half, that P&L has no strong relationship to volatility, is the part credit tests hardest. In credit, high volatility arrives with high spreads, and high spreads arrive with high expected returns (carry and the risk premium). Cutting risk when volatility rises therefore also cuts exposure to the periods with the highest subsequent returns, the post-crisis rebounds. That is the trade a restructuring banker knows from the other side: you bought the fallen angels in 2009 from people whose risk models told them to sell. The 2026 desk keeps volatility targeting for the trend sleeve, because trend needs it, and refuses to apply the same scaling mechanically to its carry sleeve (§10.4), where it would sell the premium at the wides.

### 10.3.2 The stop-loss that was already a trend rule

Ben Dor's group made the same point with a risk limit instead of a signal. Suppose the maximum DTS contribution from any issuer is 3.0, and you hold 0.5% of the portfolio in a bond at 100 bp with a duration of 5 years, a contribution of $100 \times 5 \times 0.5\% = 2.5$. If the spread widens past 120 bp, the limit forces a sale (Ben_Dor_Quantitative_Credit_Portfolio_Management p.291). Nobody in the risk meeting called it a trend strategy.

> **[SOURCE EXTRACTION]** *Ben_Dor_Quantitative_Credit_Portfolio_Management p.292:* "Generally, a momentum strategy like this one does well in trending markets and poorly in choppy markets. If enough market participants adopt this approach, it could lead to destabilizing behavior in which spread widening and asset sales reinforce each other in a vicious cycle."
>
> **Annotation.** This is the earliest shelf statement of trend crowding in cash credit, and it was written about risk limits, not hedge funds. Two lessons carry into 2026. First, the payoff description is exact. Hard DTS limits, rating-triggered sales, and vol-targeted trend sleeves all share the convex-in-trends, concave-in-chop profile that §10.6 derives formally. Second, the "vicious cycle" is a statement about market structure, not about any one book. When many holders run the same rule, their sales are the price move that triggers the next round of sales. In index CDS the cycle is damped, because dealers quote two-way all day and the instrument has no maturity wall or ratings cliff. In cash HY it is not damped, because the same bonds are held by mutual funds facing redemptions, insurers facing capital charges, and CLOs facing CCC buckets. The surrounding pages draw the conclusion explicitly for fallen angels: forced sellers sell too low, and patient holders recoup the loss. The modern desk runs trend in the index, where its selling does not move the price much, and keeps a patient, non-trend sleeve ready to buy what other people's limits force onto the market.

Ben Dor's example is an asset manager's limit. Two other seats on the same bond run the same rule in different clothes, and neither of them would recognise it as a strategy.

> **View From Another Seat.** *Two trend rules that never heard the word.* On a US life insurer's investment desk, the widening reads as a capital bill. The insurer's charge on a bond is a lookup keyed to its NAIC designation: pre-tax, about 2.17% of book value at NAIC 2.C, the bottom rung of investment grade, and 3.15% at 3.A, the top rung of high yield, rising to 6.02% at 3.C (NAIC life RBC bond factors, as restated in the June 2026 working-group papers that set the new CLO factors). A downgrade across the line raises the cost of holding by nearly half on the day, before anyone in the building has formed a view on the issuer, and many mandates add a cap on below-investment-grade holdings on top. The portfolio manager does not decide to follow the trend; the capital model does it after the agency speaks. Down the road, a CLO manager sees the same widening as a bucket problem. A typical indenture lets about 7.5% of the portfolio sit in CCC-rated loans; above that, the excess is carried in the overcollateralization test at the *lowest* market price in the bucket, not at par. Kundu (2023), *The Externalities of Fire Sales: Evidence from CLOs*, finds the average CCC loan priced near 85 cents while the cheapest CCC loan in each CLO averages 58, so one downgrade that tips the bucket over the line can cost the junior tranches more than the downgraded loan's own price move, and the cheapest way out is to sell the *higher*-priced CCCs. Each seat runs a rule that sells after bad news. Put the insurer, the CLO manager and Ben Dor's DTS limit on the same issuer and the extraction's "vicious cycle" stops being a hypothesis: it is three compliance systems agreeing with each other.

None of those seats would survive the assumption Kaz reached for next.

> **Desk Myth vs. Desk Reality.** *Myth:* A credit trend follower has a view on spreads. *Reality:* A good half of its P&L is a view on volatility, and credit volatility is spread times duration, so the position is sized by the very thing it is forecasting. Kaz, at the whiteboard: "Let's just assume Gaussian." The entire desk: "No." Spread changes are heteroskedastic by construction ($\sigma \propto s$), fat-tailed through jumps, and stale in cash. Gaussian i.i.d. returns are the one assumption under which the timing term does nothing.

The assumption fails in a second, quieter way, inside the marks themselves, and it fails in the direction that makes positions too big.

> **Ways This Blows Up.** *Stale volatility, oversized position.* A cash-bond excess-return series built from evaluated prices understates realized volatility, because pricing services smooth. An EWMA on smoothed returns therefore says risk is low, and the inverse-vol weight makes the position too large, exactly in the least liquid part of the book. The same smoothing appears as positive autocorrelation, which a trend signal reads as a trend (§10.5.3 makes the artifact explicit). *Lagging volatility in a gap.* In April 2025, HY OAS moved from 3.42% on 2 April to 4.61% on 7 April (FRED, `BAMLH0A0HYM2`). A 60-day EWMA had about three new observations. A DTS forecast had the new spread on day one. *The guard:* forecast volatility as $\hat\sigma_t = \max\big(\hat\sigma^{\text{EWMA}}_t,\ \hat\beta^{\text{DTS}}\,\text{DTS}_t,\ \sigma_{\text{floor}}\big)$, and cap leverage. The max rule responds to whichever warning arrives first.

**Estimating $\beta^{\text{DTS}}$.** Regress a rolling realized volatility of spread changes on the spread level *through the origin*, as the source extraction instructs:

$$
\hat\beta^{\text{DTS}} = \frac{\sum_t \hat\sigma^{\Delta s}_t\, s_t}{\sum_t s_t^2}.
$$

Use non-overlapping windows when you want honest standard errors, and estimate by rating bucket, because the "constant" is constant only within a bucket and a regime.

## 10.4 Trend Plus Carry: Two Coefficients, No Tribes

There are two tribes in credit. The carry-and-value tribe buys after spreads widen, because the spread is wider and spreads mean revert. The trend tribe sells after spreads widen, because they are widening. Each can point to a decade that vindicates it. The systematic desk does not join a tribe. It writes down a model in which both effects exist and lets the data size each one.

### 10.4.1 The derivation

> **Math, Gently.** *A spring and a heavy door.* Picture a fire door on a spring closer. The spring always pulls the door back toward the frame, and pulls harder the further open the door is: that is mean reversion, and its strength is $\kappa$. The door is also heavy, so once it is swinging it keeps swinging for a while even as the spring pulls against it: that is inertia, which in a spread series is trend, and its weight is $\phi$. Where the door goes next depends on both, and they can disagree. Put HY spreads 100 bp wide of their long-run level after a month in which they widened 50 bp, with $\kappa = 0.03$ a month, $\phi = 0.25$ and a duration of 4. The spring says spreads come in by $0.03 \times 100 = 3$ bp, worth $4 \times 3 = +12$ bp of expected return. The swing says they go out another $0.25 \times 50 = 12.5$ bp, worth $-50$ bp. This month the door beats the spring. Carry, the landlord's rent from §10.1.2, is the third voice in the room. The equation below writes the door down, and a larger case follows it.

Let spreads follow a mean-reverting process with inertia, under $\mathbb{P}$, which here means the probabilities the desk believes about what spreads will actually do, not the ones a price implies (Chapter 6-B owns that distinction):

$$
\Delta s_{t+1} = \kappa\,(\bar s - s_t) + \phi\,\Delta s_t + \epsilon_{t+1},
\qquad \mathbb{E}_t[\epsilon_{t+1}] = 0,\quad \operatorname{Var}_t(\epsilon_{t+1}) = (\beta^{\text{DTS}})^2\, s_t^2\,\Delta t .
$$

Here $\kappa \ge 0$ is the speed of mean reversion toward a long-run level $\bar s$, $\phi$ is the persistence of spread changes (trend when $\phi>0$), and the shock variance follows the proportional law of §10.3. Taking the conditional expectation of $r^{ex}_{t+1} \approx s_t\,\Delta t - D^{\text{spr}}\,\Delta s_{t+1}$:

$$
\mathbb{E}_t\big[r^{ex}_{t+1}\big] =
\underbrace{s_t\,\Delta t}_{\text{carry}}
\;+\; \underbrace{D^{\text{spr}}\kappa\,(s_t - \bar s)}_{\text{value}}
\;-\; \underbrace{D^{\text{spr}}\phi\,\Delta s_t}_{\text{trend}} .
$$

Read the signs after a month of widening ($\Delta s_t>0$) that leaves spreads above their long-run level ($s_t>\bar s$). Carry is higher and says buy. Value is positive and says buy. Trend is negative and says sell. The tribes disagree *exactly* after large moves, which is when the disagreement is worth money.

Plug in monthly magnitudes for HY *(illustrative)*: $s_t = 4.5\%$, $\Delta t = 1/12$, $D^{\text{spr}} = 4$, $\kappa = 0.03$ per month, $\phi = 0.25$. Carry is 37.5 bp a month. Value, with spreads 200 bp wide of $\bar s$, is $4 \times 0.03 \times 2\% = 24$ bp. Trend, after a 100 bp widening month, is $-4 \times 0.25 \times 1\% = -100$ bp. In a quiet month with $\Delta s_t = 10$ bp, trend shrinks to $-10$ bp and carry dominates. So trend matters in large-move months and carry matters the rest of the time. 2008 and 2022 were $\phi$-years: changes kept coming in the same direction. March 2020 and April 2025 were $\kappa$-weeks: a central bank or a policy reversal pulled spreads back, and anyone with a large $\phi$ in their head sold the low.

The mean-variance position follows from this forecast and the variance law of §10.3; the full derivation is next.

#### The Full Derivation: the blended weight

With risk aversion $\gamma$ and $\operatorname{Var}_t(r^{ex}_{t+1}) = (D^{\text{spr}})^2(\beta^{\text{DTS}})^2 s_t^2\,\Delta t$,

$$
w^{*}_t = \frac{\mathbb{E}_t[r^{ex}_{t+1}]}{\gamma\,\operatorname{Var}_t(r^{ex}_{t+1})}
= \frac{1}{\gamma (\beta^{\text{DTS}})^2 D^{\text{spr}}}
\left[\frac{1}{D^{\text{spr}} s_t} + \frac{\kappa\,(s_t - \bar s)}{s_t^2\,\Delta t} - \frac{\phi\,\Delta s_t}{s_t^2\,\Delta t}\right].
$$

The carry term in the bracket decays like $1/s_t$, so mean-variance carry *also* de-risks as spreads widen, more gently than trend does. The value term is bounded: as $s_t\to\infty$ it behaves like $\kappa/(s_t\Delta t)$, so even a value investor stops adding in a true blowout. The trend term is a z-score of last period's spread change, scaled by the current level. Nothing in the formula picks a tribe; $\kappa$ and $\phi$ do.

### 10.4.2 Why you cannot estimate your way out of the argument

Estimating the model looks like one line of work. Regress $\Delta s_{t+1}$ on a constant, $s_t$ and $\Delta s_t$; then $\hat\kappa = -\hat b_{s}$, $\hat\phi = \hat b_{\Delta s}$, and $\hat{\bar s} = \hat a/\hat\kappa$. Twenty-five years of monthly OAS gives 300 observations, which sounds like plenty until you remember what kind of series it is.

> **Math, Gently.** *Why a short film overstates a slow spring.* Try to measure how hard a door closer pulls from a twenty-second video of a door that takes a minute to shut. The door has barely moved, and whatever drift it showed in those twenty seconds gets read as the spring: slow springs filmed briefly look stronger than they are. A regression on a persistent series has the same problem, and Kendall worked out its size in 1954. If a series' level carries over from month to month with persistence $\rho$, the least-squares estimate of $\rho$ from $T$ observations comes out too low by roughly $(1+3\rho)/T$, so the estimated pull $\hat\kappa = 1-\hat\rho$ comes out too high by about the same amount. Put in numbers: a monthly spread with a true $\kappa = 0.03$ has $\rho = 0.97$, and 300 months give a bias of about $(1 + 2.91)/300 \approx 0.013$. The estimate centres near 0.043 when the truth is 0.03, and its standard error, roughly $\sqrt{(1-\rho^2)/T} \approx 0.014$, is as large as the bias. (Stambaugh later showed a related bias in regressions on persistent predictors, which is why the desk says "Kendall–Stambaugh".) Twenty-five years of data, and the spring is still a guess.

*The model review is fictional; the coefficients are the desk's fictional run.* Kaz presented the fit at the Monday model review on 12 October, Theo's third Monday, with the confidence of someone whose regression had converged: $\hat\kappa = 0.041$, $\hat\phi = 0.22$, both "significant." Theo raised his hand, which nobody at the review did, and asked for the range. At PJT nobody had ever given a fairness committee a point estimate of enterprise value. They gave a range, and the range was the opinion.

"The standard error on kappa is 0.014," Kaz said, and then, because Kaz is honest, "and the estimate is biased up by about the same amount. Phi is better behaved. It also moves by regime: it was higher in the 2008 window and lower in the 2010s."

"So the true kappa is somewhere between nearly nothing and twice what's on the slide," Ines said.

That was the review's conclusion, and it became the desk's rule for the blend. The honest output is a *confidence region* for $(\kappa, \phi)$, not a point, and the honest strategy is a blend whose weights do not move much as you walk around that region. Kaz reran the weights at the region's corners that afternoon: the trend weight barely moved, and the value weight moved by a factor of three, so the value sleeve got the smaller allocation. Section 10.10's code estimates both coefficients on an expanding window, so the backtest never uses a coefficient it could not have known.

> **[SOURCE EXTRACTION]** *Nuveen_Multi_Asset_Credit_Quant_Framework p.4:* "Typically, the process begins with the assumption that spreads tend to mean revert over time, usually fluctuating within a historical range rather than continually widening or tightening."
>
> **Annotation.** Read this as a prior on $\kappa$, stated honestly as an assumption. It is not evidence against $\phi$. A process can mean revert over years and trend over months, and the D3 model above does both. Allocators (Chapter 12) live at the multi-year horizon, where $\kappa$ dominates. Trend desks live at one to twelve months, where $\phi$ can dominate for a whole cycle. The two views collide only when one desk borrows the other's horizon: a trend sleeve sized on a 20-year mean-reversion study, or a value sleeve rebalanced monthly into a falling knife. The modern desk writes the horizon into the spec next to the coefficient. The phrase "within a historical range" also deserves a red pen. The range is a sample statistic, and 2008 enlarged it in a single quarter.

### 10.4.3 What the literature says about the blend

Koijen, Moskowitz, Pedersen, and Vrugt (2018), *Carry*, define carry as the return an asset earns if its price does not change and show that it predicts returns across asset classes, including US credit. Across asset classes their carry strategies have positive value exposure but no momentum or time-series momentum exposure, which is the statistical case for holding both. (In the July 2012 working-paper version, US credit carry across eight corporate portfolios has a Sharpe ratio of 0.37–0.41 over January 1973 to February 2011; we cite that draft's figures, and the final version's may differ.) Baz, Granger, Harvey, Le Roux, and Rattray (2015), *Dissecting Investment Strategies in the Cross Section and Time Series*, at Man AHL, find that time-series momentum works, cross-sectional momentum works poorly, carry works in both dimensions, and the strategies are best combined. In corporate bond cross-sections, Brooks, Palhares, and Richardson (2018), *Style Investing in Fixed Income*, find carry's long-short Sharpe ratio is only 0.18, with a 0.90 correlation to the credit market. Credit carry, in other words, is mostly credit beta.

> **[SOURCE EXTRACTION]** *Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.26:* "Over the long run, Carry appears to offer a significant premium, but with incredibly high volatility of returns. This lack of consistency means that Carry as a signal can have fantastic years and also very poor years in terms of benchmark relative performance."
>
> **Annotation.** Carry's bad years and trend's good years overlap, and that overlap is the entire reason to hold them together. In D3 terms, carry's very poor years are $\phi$-years. Spreads widen month after month, the carry received is swamped by mark-to-market, and the value signal keeps saying "cheaper." Those are trend's best years. Carry's fantastic years are long, quiet tightenings in which trend is long and slightly late, earning less than carry. A blend does not need the two return streams to be negatively correlated on average; it needs them to be differently convex. Carry is short a put on the credit cycle, and trend is long a straddle on large moves (§10.6). The 2026 desk sizes them in a common risk budget and judges the blend on its drawdowns, because judging each sleeve on its own Sharpe ratio guarantees you fire the one that is currently doing its job.

Ines summarized it in her own language. "Carry is the blinds. You collect them every hand, and they add up, and one bad hand takes them all back. Trend is folding when the table turns against you. You need both, and the art is knowing which one the current hand is about." Then she added the part nobody writes on a slide: "And you don't know. That's why it's a blend."

## 10.5 Cross-Asset Trend: The Equity Market Moves First

> **Poker Table.** Ines draws the table on a napkin. "Who at this table knows more than you? In credit, it's the equity market, by about a week. The stock trades every second, the bond trades when somebody's PM gets back from lunch, and the CDS sits in between. Trend-following in credit is sitting to the equity market's left and calling its bets. You won't win every hand, but you'll see its cards before the bond desk does."

### 10.5.1 The evidence on who leads

The lead–lag literature points one way with a few well-defined exceptions. Hilscher, Pollet, and Wilson (2015), *Are Credit Default Swaps a Sideshow?*, find that equity returns lead CDS spread changes at daily and weekly horizons and not the reverse, although CDS reacts faster on salient news days. Norden and Weber (2009) find stocks leading both CDS and bond spreads over 2000–2002, with CDS leading bonds, more strongly for lower-rated and US firms. The exceptions matter for the single-name chapters. Acharya and Johnson (2007) find incremental information in CDS for bad news, rising with the number of bank relationships (the insider-trading channel), and Lee, Naranjo, and Velioglu (2018) find a one-way flow from CDS to bonds around rating events, strongest for private firms. At the index level the conclusion is simple: equities move first, then CDX, then cash. That ordering is the basis for using equity trend to trade credit.

Momentum in cash bonds themselves is a weaker and more contested object. Jostova, Nikolova, Philipov, and Stahel (2013) report a momentum spread of 59 bp a month across all bonds over 1991–2011, 192 bp a month in non-investment-grade bonds, and almost nothing in IG, where Gebhardt, Hvidkjaer, and Swaminathan (2005) find reversal rather than continuation. Then came the audits. Dickerson, Robotti, and Rossetti (2026), *The Corporate Bond Factor Replication Crisis*, re-run the 6-month momentum factor on TRACE for August 2002–December 2024 and find that its 0.30% monthly premium is "entirely attributable to asymmetric ex-post winsorization": the base premium is 0.00%, and the 12-month version is −0.13% a month. Chapter 7 covers how a filter can manufacture a factor. The lesson this desk took from the audits is narrower. It trades credit trend in instruments whose returns it can trust (indices, CDS), and it takes the signal from the market that prices information first (equity). Bond-price momentum in the cross-section is the least trustworthy of the three.

### 10.5.2 Equity Momentum in Credit, from the shelf

*The desk is fictional; the numbers are the shelf's.* Kaz brought the equity idea to Ines on the Wednesday, the day before the fast sleeve flipped, with the most complete practitioner implementation open on the desk and a pink tab on the page: the Barclays QPS "Equity Momentum in Credit" (EMC) signal in Dynkin and coauthors' *Systematic Investing in Credit*.

"They sort every bond in the index by its issuer's trailing stock return, every month," Kaz said. "December 1992 to May 2017. The top-minus-bottom quintile earns 6.34% a year in US IG with an information ratio of 1.56, positive in both halves of the sample, and in high yield it's about 15.9% a year before—" (Dynkin_Systematic_Investing_in_Credit pp.608–609)

"Before costs," Ines said. "How long does an issuer stay in the top bucket?"

Kaz had been about to get to that. A stock's momentum rank is a mood, and a portfolio that holds only the top of it spends its life trading cash bonds at cash-bond bid–offer; the page Kaz turned to next put a number on how short the mood is, and it is the extraction below. Kaz fought back with the cleanest result on the page, which is that the effect is smooth at sector level: each additional 1% a month of equity momentum adds "an extra 5 to 8bp of bond excess returns" (Dynkin_Systematic_Investing_in_Credit p.644). "Then that's where we trade it," Ines said, and the argument was over before anyone had said "turnover" out loud.

The construction uses several horizons at once, for the reason §10.2.2 gave. The signal is built to confirm itself: "combining momentum signals at different horizons helps to validate (confirm) trends in stock prices" (Dynkin_Systematic_Investing_in_Credit p.607). In our notation, with equity total returns $r^{\text{eq}}$,

$$
\text{EMC}_{i,t} = \frac{1}{3}\sum_{h\in\{1,3,6\}} \frac{M^{\text{eq},(h)}_{i,t}}{\sqrt{h}},
$$

where dividing by $\sqrt h$ is our default way to put the horizons on a common volatility scale. The book says only that the returns are "rescaled for different lengths of the respective formation periods," and does not give the exact rescaling, so treat $\sqrt h$ as a specification choice and say so in the spec.

> **[SOURCE EXTRACTION]** *Dynkin_Systematic_Investing_in_Credit p.610:* "an issuer with equity momentum in the top 10% (D10) has only a 17% probability of remaining top ranked after three months"
>
> **Annotation.** An equity momentum signal has the half-life of an ad hoc group: by the time counsel is retained, the top decile has left the building. The sentence continues with the complement, an 83% chance of leaving the top decile within three months. For a trend desk this is a cost statement before it is a signal statement. A cross-sectional EMC portfolio that holds only the top decile turns over constantly; the same book reports top-decile long-only turnover of about 73% a month and returns that turn negative after transaction costs (Dynkin_Systematic_Investing_in_Credit p.692). The modern desk uses three responses. It applies the signal at index or sector level, where turnover is cheap and sector timing earned 2.38% a year in US IG, 4.04% in US HY, and 1.77% in Euro IG over 2007–2017 before costs (p.647). It uses buffered entry and exit thresholds, buying at the 80th percentile and selling below the 50th instead of trading every rank change. And it treats a single-name EMC signal as a *veto or tilt* on a position held for other reasons, not as a reason to trade on its own.

Barclays is a dealer's research group writing about a signal. Two systematic managers have said in public what the same evidence looks like from the seat that has to own the bonds.

> **View From Another Seat.** *The systematic manager.* Man Group's 2022 paper on quantitative credit surveys what happens when equity factors are carried across to corporate bonds: they "generate positive alphas and Sharpe ratios higher than those of the corporate bond indices, but the only spill-over to achieve meaningful statistical significance is equity Momentum, which generates a higher alpha than corporate bond Momentum itself" (Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.31, citing Houweling and coauthors; it attributes the effect, after Bektić and coauthors (2016), to fundamentals showing up "more swiftly in equities than in bonds"). Read from a long-only manager's chair, that is a reason to take the momentum signal from the stock and leave the bond's own price history alone. Robeco's researchers went a step further in a note of 17 August 2012 on Haesen and Houweling's work: a plain equity-momentum sort quietly carries time-varying equity and bond-market exposure, and stripping it down to the firm-specific, *residual* part of the stock's return cut the strategy's volatility "with about 50%" and raised its Sharpe ratio. For a manager who has to hold the bonds rather than trade an index, the residual is the version worth owning, which is also where §10.5.4 ends up.

### 10.5.3 The lead–lag regression, and the stale-mark artifact

> **Math, Gently.** *A lead–lag regression, and a clock that is wound every other week.* A lead–lag regression asks one question of two time series: does knowing what A did today help predict what B does tomorrow, once you already know what B did today? If it does, A "leads" B, which econometricians call Granger causality, a name that promises more than it delivers, since it is about forecasting and not about cause. Now picture a wall clock that someone resets to the right time only every other week. Set it beside your phone and the clock "follows" the phone with a lag: whenever the phone has moved on and the clock has not, the next reset makes the clock jump the way the phone already went. A regression would say the phone leads the clock, though nothing causes anything; the clock is merely stale. A bond mark that updates only when the bond prints is that clock, and the stock price is the phone. The size of the fake lead, in a simple regression, turns out to be $p(1-p)\beta^{\text{ce}}$, where $p$ is the chance the bond prints in a period and $\beta^{\text{ce}}$ is how much the bond truly moves with the stock on the same day. With $\beta^{\text{ce}} = 0.3$, a bond that prints half the time shows a fake lead of $0.5 \times 0.5 \times 0.3 = 0.075$, and one that prints 90% of the time shows $0.9 \times 0.1 \times 0.3 = 0.027$. The four lines that produce the formula are below.

The test is a two-equation VAR with Granger restrictions:

$$
r^{\text{cr}}_{t+1} = \pi_0 + \pi_{\text{eq}}\, r^{\text{eq}}_{t} + \pi_{\text{cr}}\, r^{\text{cr}}_{t} + \varepsilon_{t+1},
$$

and "equity Granger-causes credit" means rejecting $\pi_{\text{eq}} = 0$. Before anyone celebrates a rejection, it is worth deriving what staleness alone produces.

Let the true credit price respond to equity only contemporaneously, $\Delta P_t = \beta^{\text{ce}} r^{\text{eq}}_t + e_t$, with no true lead. The observed mark $m_t$ updates to the true price only when the bond prints, which happens each period with probability $p$, independently. Write $U_t \in \{0,1\}$ for "printed at $t$." Then

$$
\Delta m_{t+1} = U_{t+1}\,\big(P_{t+1} - m_t\big),
\qquad
\mathbb{E}_t\big[\Delta m_{t+1}\big] = p\,\big(P_t - m_t\big),
$$

because $\mathbb{E}_t[\Delta P_{t+1}] = 0$. The gap $P_t - m_t$ contains this period's equity-driven move whenever the bond did not print at $t$, so

$$
\operatorname{Cov}\!\big(\Delta m_{t+1},\, r^{\text{eq}}_t\big) = p\,(1-p)\,\beta^{\text{ce}}\,\operatorname{Var}\!\big(r^{\text{eq}}_t\big) > 0 .
$$

Equity "leads" the bond mark with a simple-regression coefficient of about $p(1-p)\beta^{\text{ce}}$ even though nothing leads anything. (In the VAR above, the own lag is correlated with equity and rescales this by $1/(1-p^2R^2_{\text{ce}})$, where $R^2_{\text{ce}}$ is the share of the bond's true move that equity explains. The rescaling matters only when that share is large.) The artifact disappears at $p=1$ (always fresh) and at $p=0$ (never prints, no returns at all), and it peaks at $p = \tfrac12$: a bond that prints every other week. That is not an unusual bond. Section 10.10 simulates exactly this case and asserts that the fake lead is statistically significant on the marks and absent on the true prices.

*The desk is fictional.* Kaz's first run of the regression, on evaluated marks for the HY index's constituents, came back with a lead coefficient they were proud of and a t-statistic they were prouder of. Theo looked at it, then at the column of monthly print counts beside it, and sorted by the second column. The largest "leads" sat on the bonds that printed least. "Your lead is the bond's print schedule," he said. Kaz looked at the sorted column for a long moment and said, "Then we measure it where the clock is always wound." 

Dynkin's team runs the right defenses, testing the signal with one- to three-day lags and conditioning on measures of how efficiently each bond trades (Dynkin_Systematic_Investing_in_Credit pp.621, 630). At index level the artifact is much smaller, because CDX prints hundreds of times a day. That is one more reason the cross-asset trend sleeve uses equity signals to trade *indices*.

### 10.5.4 Total versus residual equity momentum, and the turning-point risk

There is a subtler problem. Sorting bonds on total equity return loads on time-varying default risk: after an equity sell-off, the losers are the high-beta, high-leverage names, so a long-winners, short-losers credit book is short credit beta at the bottom. Dynkin's book shows the symptom, "the strategy net spread tends to decline and become negative during equity down‐cycles" (Dynkin_Systematic_Investing_in_Credit p.613).

> **[SOURCE EXTRACTION]** *Dynkin_Systematic_Investing_in_Credit p.631:* "Haesen et al. (2017) argued that this varying exposure can make the strategy vulnerable in periods of market turning points, for example when a market downturn is followed by a recovery."
>
> **Annotation.** Haesen, Houweling, and van Zundert (2017) propose sorting on *residual*, firm-specific equity momentum, which roughly halves the default-risk exposure, doubles the Sharpe ratio, and cuts the bear-to-bull drawdowns in their 1994–2013 sample. Dynkin's team reports a different result in their own data, and the honest desk puts both on the page instead of picking the convenient one. The disagreement is informative. Residualizing helps when the turning point is a sharp V and the losers' rebound is a beta rebound, as in 2009 (§10.7). It helps less when the cycle is slow and the losers really are deteriorating credits. The 2026 desk's practice is to residualize the equity signal against the market and sector, report the credit-beta exposure of the long-short book every day, and size the beta separately. It is the same rule as Chapter 8's "IDO or it didn't happen": a lead–lag alpha whose credit beta flips sign over the cycle is mostly market timing until you strip the beta.

Man's credit team comes at the same question from the other end: not which part of the equity signal to keep, but where an issuer's trend lives in the first place.

> **[SOURCE EXTRACTION]** *Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.25:* "We generally find trends to be consistent across a capital structure and indeed across broader groups/ecosystems as well; these trends therefore tend to be less issue-specific and more at an issuer-level."
>
> **Annotation.** This is the practitioner's justification for the whole section. If trends live at the issuer level, the best place to observe an issuer's trend is the security that prices it fastest, which is almost always the equity and occasionally the CDS. The bond is the last to know. For the ex-RSSG reader the sentence also has a capital-structure reading: the senior secured loan, the unsecured notes, and the stock of a deteriorating issuer move together until the moment they do not, which is the liability-management event. An LMT is exactly the case where the trend is *not* consistent across the capital structure, because value is being moved from one class to another. Section 10.9 takes this up. A cross-asset trend engine needs an explicit flag for "the capital structure has stopped moving together," and the Priming Risk Score of Chapter 13 is that flag.

Pitkäjärvi, Suominen, and Vaittinen (2020), *Cross-asset signals and time series momentum*, give the template for doing this across asset classes. In 20 countries, past bond returns predict equity returns positively, past equity returns predict government bond returns negatively, and a cross-asset TSMOM strategy has a Sharpe ratio about 45% higher than the standard one. They attribute it to slow-moving capital. For credit, the natural cross-asset signal for CDX HY is the trailing return of the equity market, or better the equity of the index constituents, combined with credit's own trend, with each sleeve's weight estimated as in §10.4.

## 10.6 Crisis Alpha and the Shape of the Payoff

Mags has heard the phrase "crisis alpha" from every trend manager who ever visited the desk. "They say it the way bankers say 'synergies.' It's real about a third of the time, and they'd like to be paid for all of it." The useful question is *which* crises, and the answer comes from the shape of the payoff.

### 10.6.1 Trend is a straddle, and the smile is the receipt for momentum

> **Math, Gently.** *Part one: a bell, and a tilted cloud.* Take every daily excess return CDX HY has posted and stack them in a histogram, one bar for each tenth of a percent. You get a bell: most days near zero, fewer days further out, close enough to symmetric to fool you. That bell is what a *normal distribution* describes, and it needs only two numbers, a centre and a width (the standard deviation). Look at the edges, though. The real histogram has more days far out on the left than the bell allows, which is what "fat-tailed" means and why Chapter 5 spends a chapter on it. Now draw a different picture. For each month, put the trailing twelve-month return (the signal) on the horizontal axis and the next month's return on the vertical. If both are normal and related, the dots form a cloud shaped like an ellipse, and "jointly normal with correlation $\rho$" is a description of that ellipse: at $\rho = 0$ it is a round blob, and as $\rho$ rises it tilts and narrows along the diagonal. Momentum is a tilt.
>
> *Part two: what the tilt buys.* Fix next month's move and ask how often the signal was on the right side of it. For a move of one standard deviation with $\rho = 0.25$, the signal points the right way with probability $\Phi(0.258) \approx 0.60$ and the wrong way with probability 0.40, where $\Phi$ is the area under the bell to the left of a point. On average the strategy keeps $0.60 - 0.40 = 2\Phi(0.258) - 1 \approx 0.20$ of the move, about a fifth. For a three-standard-deviation move the same tilt gives $2\Phi(0.77) - 1 \approx 0.56$, more than half, because big moves are where a tilt shows. At $\rho = 0$ the signal is a coin and the strategy keeps nothing of any move. A growing share of a growing move is a smile.

That smile has a closed form, which comes from conditioning the tilted cloud on the move; the full derivation is next.

#### The Full Derivation: the smile

Take the sign strategy on one instrument, $r^{\text{TF}}_{t+1} = \operatorname{sign}(M_t)\, r_{t+1}$, and suppose $(M_t, r_{t+1})$ are jointly Gaussian with zero means and correlation $\rho$, so $\rho>0$ means momentum. Condition on the next-period market return:

$$
\mathbb{E}\big[r^{\text{TF}}_{t+1}\,\big|\, r_{t+1}\big] = r_{t+1}\,\mathbb{E}\big[\operatorname{sign}(M_t)\,\big|\,r_{t+1}\big]
= r_{t+1}\Big[2\,\mathbb{P}\big(M_t>0 \mid r_{t+1}\big) - 1\Big].
$$

For bivariate normals, $M_t \mid r_{t+1}$ is normal with mean $\rho\,(\sigma_M/\sigma_r)\, r_{t+1}$ and standard deviation $\sigma_M\sqrt{1-\rho^2}$, so

$$
\mathbb{E}\big[r^{\text{TF}}_{t+1}\,\big|\, r_{t+1}\big] = r_{t+1}\left[2\,\Phi\!\left(\frac{\rho\, r_{t+1}}{\sigma_r\sqrt{1-\rho^2}}\right) - 1\right],
$$

where $\Phi$ is the standard normal CDF. This function is even in $r_{t+1}$ and U-shaped. For small moves, use $2\Phi(x) - 1 \approx \sqrt{2/\pi}\,x$:

$$
\mathbb{E}\big[r^{\text{TF}}_{t+1}\,\big|\, r_{t+1}\big] \approx \sqrt{\frac{2}{\pi}}\;\frac{\rho}{\sigma_r\sqrt{1-\rho^2}}\; r_{t+1}^2 ,
$$

a parabola. For large moves, $2\Phi(\cdot)-1 \to \operatorname{sign}(r_{t+1})$ and the payoff tends to $|r_{t+1}|$, which is a straddle. The quadratic coefficient is positive *if and only if* $\rho > 0$. Convexity is not a separate property of trend; it is the receipt for momentum. If the market does not trend, the smile is flat. This is the formal version of Fung and Hsieh's reading of trend followers as holders of lookback straddles (Fung and Hsieh 2001, *The Risk in Hedge Fund Strategies: Theory and Evidence from Trend Followers*), and of Hamill, Rattray, and van Hemert's finding that trend returns are positively skewed and straddle-like. Figure 10.3 draws the payoff for several values of $\rho$ and for one simulated sample.

![Figure 10.3: Every round of a sign strategy pays +|r| or −|r|, and momentum only tilts the odds toward the right call when the move is large, so the expected payoff is a smile whose depth grows with ρ and which vanishes at ρ = 0. Illustrative: the bivariate-normal model of §10.6.1, with the right panel showing 400 simulated rounds at ρ = 0.25 (fixed seed) against the closed form.](assets/figures/ch10_trend_smile.png)

#### Testing for the smile

The empirical test is the regression

$$
r^{\text{TF}}_{t} = b_0 + b_1\, r^{\text{HY}}_{t} + b_2\, \big(r^{\text{HY}}_{t}\big)^2 + u_t, \qquad b_2 > 0 \ \text{is the smile},
$$

with Newey–West standard errors. Run it at the horizon where $\rho$ lives: quarterly or semiannual non-overlapping returns for a 12-month signal. A daily fit finds nothing, because day-to-day the correlation between a 12-month trailing return and tomorrow's return is close to zero. Kaz ran it daily first and announced that trend was not convex. Ines asked them to run it on quarters. They did, and have not mentioned it since.

**The credit twist.** Long credit is short a put on firm assets (Chapter 5's Merton model). The market return $r^{\text{HY}}$ has a positive drift (carry) and a fat left tail (defaults, gaps). A straddle on a negatively skewed asset earns most of its payoff on the left: the short-credit leg of trend is long that put, and it pays in the slow sell-offs where the put goes deep into the money over several months. The same asymmetry explains the losses. The rebound after a credit crash is a short-covering of that put, steep and fast, and a trend follower who is short is short the steepest part of the recovery. Daniel and Moskowitz (2016), *Momentum Crashes*, document the equity version: momentum crashes in panic states, after declines and at high volatility, when the losers rebound. Barroso and Santa-Clara (2015), *Momentum Has Its Moments*, show that managing momentum's own risk "virtually eliminates crashes and nearly doubles" its Sharpe ratio. In credit both effects show up most strongly in high yield, where the put is closest to the money.

### 10.6.2 Whipsaw arithmetic: why trend cannot trade a V

The straddle needs the move to last long enough for the signal to notice.

> **Math, Gently.** *The hiker in the valley.* Picture a hiker who cannot see the trail ahead and decides which way is downhill by looking back at the stretch she has just walked. Drop her at the lip of a valley, facing the wrong way. On the way down she spends a while walking the wrong way before she notices, then walks the rest of the slope the right way; at the bottom she overshoots by the same while before she notices the ground now rises, and then walks the rest of the climb the right way. Each slope costs her one lag of wrong-way walking and pays her whatever is left of the slope. If her lag is a quarter of the whole valley, half of each slope is wrong and half is right, and she breaks even. Put numbers on a credit V that lasts two months, one down and one up, against a signal that lags three weeks (0.75 of a month). On each slope she is wrong for 0.75 months and right for 0.25, so of the two months of available move she nets $(0.25 - 0.75) \times 2 = -1$ month's worth, a capture of $(2 - 4 \times 0.75)/2 = -50\%$. Same rule, same market, longer valley, and the sign flips; the equation below is the valley in symbols.

Make that precise with a stylized V. The credit excess-return index falls linearly by $d$ over $T/2$ months, then recovers linearly by $d$ over the next $T/2$. A trend follower reacts with effective lag $L < T/2$: it is long until $L$, short from $L$ to $T/2 + L$, and long again afterward. It enters long, as it would after a quiet tightening (February 2020 and February 2025 both qualify). Add up the four legs, with slope $d/(T/2)$ on each:

$$
\text{P\&L} = \frac{d}{T/2}\Big[\underbrace{-L}_{\text{long, falling}} + \underbrace{(T/2 - L)}_{\text{short, falling}} \underbrace{-\,L}_{\text{short, rising}} + \underbrace{(T/2 - L)}_{\text{long, rising}}\Big]
= \frac{2d\,(T - 4L)}{T}.
$$

The total available move is $2d$ (down $d$, up $d$), so the capture ratio is $(T-4L)/T$. It is negative whenever $L > T/4$. For a trailing-sum signal of length $h$ after a prior trend of similar slope, $L \approx h/2$, so a 12-month signal ($L \approx 6$ months) needs a V lasting more than about two years to break even, and a 3-month signal ($L\approx 1.5$) needs one longer than six months. March 2020 and April 2025 had $T \approx 2$ months, which no reasonable lookback beats. The 2007–2009 widening and recovery took closer to two years. Plug in $T = 20$: a 3-month signal captures $(20-6)/20 = 70\%$ of the round trip, and a 12-month signal loses $(20 - 24)/20 = -20\%$ of it *(stylized; real Vs are asymmetric and the lag depends on the preceding slope)*. Speed is a parameter, not a personality. Section 10.10 verifies the formula on a grid. Figure 10.4 draws the V, the two signals' positions, and the capture ratio as the V gets shorter or longer.

![Figure 10.4: A signal that lags a V by more than a quarter of its duration loses on the round trip, unless the V is so short that the signal never flips: against a 20-month V the 3-month signal captures 70% and the 12-month signal loses 20% (left), while against a two-month V (March 2020, April 2025) the 3-month signal loses half, the 12-month signal never turns and earns nothing, and even a two-week lag only breaks even (right). Illustrative: the stylized V of §10.6.2 with lags L = 0.5, 1.5 and 6 months; dots mark break-even at T = 4L; for L < T ≤ 2L the signal flips after the trough and the same legs give 2L/T − 2, and for T ≤ L it never flips and captures 0.](assets/figures/ch10_whipsaw_capture.png)

### 10.6.3 Is credit trend just beta?

The AQR team's out-of-sample test of trend in alternative markets, Babu, Levine, Ooi, Pedersen, and Stamelos (2020), *Trends Everywhere*, includes five CDS indices (CDX NA IG from October 2003, CDX NA HY from March 2004, iTraxx Europe and Crossover from June 2004, and an EM index from March 2004), with annualized volatilities of only 3.9–5.5%. Across all alternative assets, 12-month TSMOM earned a gross Sharpe of 1.34. Credit, however, was the weakest group once passive beta was removed. Regressed on an equal-volatility passive long portfolio, 12-month credit TSMOM had an annualized alpha of 4.4% with a *t*-statistic of 0.49, a beta of 0.52 (*t* = 8.84), and an $R^2$ of 33%, the highest of any group. Fidelity's decomposition of SG Trend Index returns (data to December 2025) finds that about 76% of a simple trend strategy's risk is beta timing, and puts the index's correlation with the S&P 500 at −0.11 unconditionally and −0.31 in down months.

The desk motto applies without modification. Trend is beta that changed its mind, and it is still beta. Strip it before you call it alpha. In credit there is a structural reason the stripping removes so much. The carry hurdle (§10.1.2) keeps the 12-month signal long through most of the cycle, so a large share of credit TSMOM's return is the credit risk premium, collected while spreads drift tighter. The genuine trend component lives in the minority of months in which the signal is short, which is why it matters so much whether those months are slow sell-offs or sharp Vs.

Hurst, Ooi, and Pedersen (2017), *A Century of Evidence on Trend-Following Investing*, give the long-run base rate. Across 67 markets from 1880 to 2016, TSMOM was profitable in every decade and positive in 8 of the 10 worst drawdowns of a 60/40 portfolio, which lasted about 15 months peak to trough on average, long enough for trend to flip short. It struggled in abrupt crashes such as October 1987. For credit, this is the whipsaw arithmetic stated as history.

> **Trend Watch: CTAs, speed, and crowding, 2024–2026.** CTAs, in SG's phrase, "showcase a level of adaptability akin to the Kardashians," and the last two years tested it. *The drawdown:* the SG Trend Index fell 4.9% in April 2025 and was down 9.3% for the year to that point (SG Prime Services, *CTA Industry Update*, May 2025). Its 12-month return to 30 April 2025 was −18.6%; the index had lost more than 15% over a rolling 12 months only twice in its history, this episode and January 2019 at −16.0% (Man Group, *Trend Following and Drawdowns: Is This Time Different?*). AlphaSimplex dates the peak-to-trough drawdown at −21.8% from 15 April 2024 to 14 May 2025 (Kaminski and Wen, June 2025). Cambridge Associates, measuring −20.4% from May 2024 to May 2025, calls it the second-largest drawdown since 2000. *The recovery:* for full-year 2025, SG Trend returned +2.39% against +17.89% for the S&P 500 total return, according to Top Traders Unplugged's compilation (23 January 2026). In 2026 trend made money during the Middle East energy shock, about +10% year to date by end-April while HY OAS peaked at only 3.46% on 30 March (FRED), and stood at +11.07% year to date at end-August (Top Traders Unplugged; secondary figures, check against SG Prime Services). *The crowding:* in July 2026 the SG Trend Index lost 1.12%, and the same compiler noted that "the programs were largely positioned the same way," so breadth across programs gave little protection. SG put the 2024 pairwise correlation of index constituents at 0.78, and Man reports that correlation was 0.87 before 2007. *The speed:* SG finds that since 2007 the index "behaves more like a much slower model," while faster models "delivered the best hypothetical returns" in 2020. Man finds that adding alternative markets, "such as power, synthetic credit indices and interest rate swaps," improved performance, more so for slower systems. *Scale:* SG cites industry AUM of about \$340bn (BarclayHedge, Q4 2024). Man AHL reports about \$39bn of trend-following AUM across "900+ traditional and alternative markets" as of mid-2026. *What it means for the desk:* the 2025 drawdown was not a credit event. Credit indices are a small, slow sleeve in CTA books, and HY OAS has spent 2024–2026 in a tight band (2.59–4.61%), with few trends long enough to pass the carry hurdle. The credit trend sleeve's job in this regime is to be cheap, small, and ready for the next slow sell-off, not to earn its keep in a market that keeps snapping back.

## 10.7 Case Studies: 2008, 2020, 2022, and the April 2025 Coda

The four episodes are told in two ways. The first and the last are scenes, because they are two of Mags's three futures and the desk learned them as hands. The middle two are short, because other chapters own their timelines; each says what trend did, what it ought to have been measured against, and what a 2026 systematic desk would have flagged. Spread levels before October 2023 come from secondary sources or Dynkin's tables and are marked approximate; the full ICE BofA history, which the §10.10 code reads from a local CSV, is the place to check them. Figure 10.5 puts the four episodes on one axis and one time scale, using a public daily series that does reach back that far.

![Figure 10.5: Four episodes, four shapes: a two-year ramp that a 12-month signal could follow (A), a two-month needle in 2020 (B), a grind to a July peak in 2022 (C) and a six-week gap in 2025 (D) that is shorter than even the 3-month lookback bar. Source: FRED BAA10Y (Moody's seasoned Baa yield less the 10-year Treasury), daily, used as a long-history proxy because ICE BofA history before October 2023 is no longer on FRED; SG Trend returns as cited in §10.7 (Cambridge Associates for 2008 and 2022, Hedgeweek for 2020, SG Prime Services for April 2025).](assets/figures/ch10_episodes_baa_spread.png)

### Case Study A: 2007–2009, the trend that paid and the rebound that charged

#### The replay: July 2007 to June 2009

*A replay, Ines's ritual: the desk cuts a real episode off at a date and trades it blind. The cast, their cards and the sleeve's positions are fictional (the desk's fictional run on the historical tape); every market number is sourced where it appears.*

Ines did not wait for Friday. At twenty past five on that Thursday, with the sticky note still on Kaz's monitor and Theo's index card still blank, she wheeled the spare screen to the end of the row and opened a folder called `2007`. Replays usually happen on Friday afternoons, when the market is closed enough to ignore. This one was happening because Mags had said "the summer of 2007" an hour earlier, and Ines wanted Theo to know what that future felt like from the inside, one cut at a time.

"Four cuts," she said. "At each one you see everything up to that date and nothing after it. You tell me what the trend book holds, how much, and why. Kaz runs the sleeve. Mags plays herself. Theo plays the new guy, which requires no preparation."

**Cut one: Friday, 10 August 2007.** The screen stopped on the day after a large French bank froze three of its funds because it could no longer put a value on what was in them. High yield had been widening since June. Kaz read the sleeve: the fast signal had turned short in the last days of July, and the slow one, the twelve-month return, was still long.

"Being paid to sit through it," Theo said, before he could stop himself.

"Same arithmetic as this afternoon," Kaz said. "Different year."

Mags had not looked at the screen. "This is when Sal stopped picking up the phone," she said. "Not all at once. First he was in a meeting. Then the meeting ran long. By the end of the month you could buy index protection from anybody with a pulse, and you could not sell a single bond to Sal. The index told you the truth every day. The bonds told you the truth in November." She wrote her card in four words, *sell what still trades*, and slid it across.

Theo's card said to keep the fast short and keep it small, because the slow sleeve disagreed and he did not know which sleeve was the summer and which was the year. Kaz's card said "per spec," which is what Kaz's cards always say.

**Cut two: Thursday, 4 December 2008.** Ines skipped sixteen months, and the room felt them go. Both signals had been short CDX HY since late 2007, and the equity-to-credit sleeve had got there first, which is what §10.5 says it should do. Nobody at the table knew that this Thursday would turn out to be the widest close of the whole episode on the long-history proxy the desk uses for it: Moody's Baa bonds at 6.16% over the ten-year Treasury (FRED, `BAA10Y`).

Kaz put the sleeve's notional on the screen, and Theo frowned at it. The short had been getting smaller for a year. "We were right the whole way," he said, "and the model kept buying back the short?"

"We were right the whole way and the risk kept rising," Kaz said. "Same budget, more volatility per unit, fewer units." High yield had gone from about 600 bp to about 1,800 bp *(approx.)*, and under the proportional law of §10.3 a constant-risk position at three times the spread holds a third of the notional. The forced-seller mechanics that make a long credit book sell after a widening also make a short one cover after a widening. Vol scaling has no opinion about which side of the trade is winning.

"So which short is it?" Ines asked. "The one in the index or the one in the bonds?"

That was Mags's question too, and she answered it with numbers she had not had in 2008. Dynkin's tables would later put the average CDX HY spread for 2008 at 788 bp against 899 bp for the cash HY index, and 950 bp against 991 bp for 2009 (Dynkin_Systematic_Investing_in_Credit pp.215–216). The cash–CDS basis had gone deeply negative and would, in Ben Dor's phrase, revert "back toward zero as the crisis abated" (Ben_Dor_Quantitative_Credit_Portfolio_Management p.390). Two pages earlier Ben Dor's group gives the reason in a single sentence.

> **[SOURCE EXTRACTION]** *Ben_Dor_Quantitative_Credit_Portfolio_Management p.388:* "However, during the crisis, spreads of cash bonds widened by much more than CDS due to liquidity effects."
>
> **Annotation.** For a trend follower this sentence decides which instrument to trade. A cash-bond trend sleeve in 2008 got short late, because its marks were stale, and then covered into a market where the bid had vanished, so it paid the liquidity widening twice, once in the mark and once in the exit. An index sleeve was short the cleaner instrument, and its liquidity improved relative to cash as the crisis deepened. The modern lesson generalizes: in credit, the trend signal and the trend vehicle should be chosen separately. You can signal from cash excess returns, equity, or both, but you execute in the instrument whose liquidity survives the move you are betting on. The basis is also its own signal. A cash–CDS basis that is very negative and starting to close is a $\kappa$-flag for §10.4: the forced selling is ending, and the trend sleeve's short is about to meet the patient buyers of §10.3.2.

Ines let that sit and then told them what the real trend followers had done with this tape, from the public record rather than from anyone's memory. Man AHL's Evolution programme, in its own account, took its credit exposure by selling protection on CDX and iTraxx, was short credit during 2008, and had "no hard-wired long credit bias" (*The Hedge Fund Journal*, 2013), so it could flip to buying protection when its signals said so. The SG Trend Index returned +20.9% in 2008 while MSCI ACWI fell 42.2% (Cambridge Associates, August 2025), and Man's Robertson (2023) puts the BTOP50 at +17% from July 2007 to February 2009. Trend, measured the way its managers measure it, had the year of its life.

Everyone's card at cut two said hold. Mags's added a line: *start a list of what you'd buy, and from whom.*

#### The card: Monday, 9 March 2009

**Cut three.** The screen stopped on a Monday. The US equity market had fallen by more than half from its 2007 peak. The cash–CDS basis, still negative, had begun to close. Ines wrote the card on the whiteboard, and the reader gets the same one.

*You are short CDX HY on a 12-month signal, DTS-scaled. The equity index has fallen by more than half from its peak. The cash–CDS basis has begun to close. Write three things: what you do, in what size, and what print makes you cover.*

Write yours before reading theirs.

Kaz's card was the spec, as ever. "Hold. The twelve-month signal is short, and the signal decides. Size is whatever the DTS forecast says, about a third of the 2007 notional. Cover when the twelve-month return turns positive."

Mags's card was not a card so much as a verdict. "Cover all of it. Then buy the bonds that are going to come back at par, at forty, from people whose models are telling them what yours is telling you." She tapped Kaz's monitor. "Back in my day we called that being the patient buyer. It sounds nobler than it is. It mostly means you had cash on the one day nobody else did."

Theo did not write anything for a while. Then he asked the question that would, it turned out, have been worth the most. "What does the equity signal say?"

Kaz checked. On that Monday the stock market's own trend was still down on every horizon the sleeve used. Nobody can see a low from inside it. Theo wrote his card anyway: *cut the short to half today, because the basis is closing and spreads are further from any long-run level than they have ever been; cover the other half on the first day the equity three-month return turns positive, whatever credit's own signal says.*

Ines advanced the tape. That Monday was the low. AlphaSimplex dates a "GFC Recovery" drawdown in the SG Trend Index of −11.3% starting the same day, 9 March 2009. Paleologo's account of the equity version reads like a description of the next three months on Ines's screen.

> **[SOURCE EXTRACTION]** *Paleologo_Advanced_Portfolio_Management p.77:* "During 2008, Momentum experienced higher volatility but did not lose money (see Figure 5.9). However, in 2009 the stocks that had experienced large losses in the previous year rallied as the market rebounded."
>
> **Annotation.** Paleologo's account is about cross-sectional equity momentum, but the mechanism transfers exactly to credit trend, and it is worse in credit. The 2008 losers were the highest-spread, highest-beta credits, the ones closest to Merton's default boundary. When the market turned, their equity rallied like deep out-of-the-money calls coming back to life, and their bonds and CDS followed. A trend book short the index was short that convexity at the moment it exploded. The systematic desk's defense is not to predict the turn. It is to let the faster information source turn first: the equity market bottomed on 9 March 2009, so an equity-to-credit signal flipped weeks before credit's own 12-month signal did. A second defense is the $\kappa$ term of §10.4, which by early 2009 was telling every blended book that spreads were extremely wide of any long-run level. The restructuring reader knows the rest of the story from the other side: early 2009 was when par-recovery bonds were bought at 40 from sellers whose models said "trend."

#### Grading the cards

**Cut four: June 2009.** The last screen showed the spring. High yield had rallied hard, and the losers of 2008 had led it.

Ines graded Kaz's card first, because it was the easiest. "Right for twenty months and wrong for the two that cost the most." Credit's own twelve-month signal held the short into the rebound, exactly as the whipsaw arithmetic of §10.6.2 says a long lookback must when the bottom is a V. The DTS scaling had already made the short a third of its old size, which is why the damage was survivable; the card's mistake was its cover rule, which waited for the slowest signal in the building. The exit rule was the strategy, and the card had borrowed it from the entry.

Mags's card got full marks on direction and a deduction she accepted with good grace. "You covered on a feeling," Ines said. "The feeling was right. The desk can't run a feeling at 4 p.m. on a Thursday without you." Mags said she had been marked down by better people, and named none of them.

Theo's card got the best grade at the table, and not because he was clever. He had asked which market knew more than the bond, and the answer on every horizon was the stock. In the desk's replay the equity-to-credit signal flipped weeks before credit's own, as the Paleologo annotation above argues it should; a book that covered on the equity turn kept most of what 2008 had paid it. His first half, cut on the basis and on the distance from any long-run level, was the $\kappa$ term of §10.4 doing its job, and those two flags had been arguing for a smaller short since late 2008. The shelf evidence for that grade is Dynkin's.

> **[SOURCE EXTRACTION]** *Dynkin_Systematic_Investing_in_Credit p.617:* "While the corporate index has average returns of –8.07%/yr in drawdown episodes and 4.12%/yr in recovery times, the EMC strategy performed well in both regimes: 11.53%/yr in credit drawdowns and 4.30%/yr in recoveries."
>
> **Annotation.** This is the strongest shelf evidence that an equity-signaled credit strategy is a crisis hedge rather than a crisis amplifier, and it explains why the systematic desk prefers to get its credit trend from the equity market. Two caveats keep it honest. First, these are averages over several down-cycles in IG, gross of costs, for a long-short issuer-selection strategy. They are not the return of a short-index trend sleeve, and they do not survive the top-decile turnover of §10.5.2 without buffering. Second, the recovery number (4.30% against 4.12%) is the interesting one: the strategy did not give back its drawdown gains in recoveries *on average*. The averages hide the specific turning point that hurts, 2009, when the losers rebounded fastest. The 2026 desk reads this page as a case for equity-signaled credit trend with residualized beta (§10.5.4), not as a promise that every recovery is free.

The reader's card is graded the same way. If it held the short because the twelve-month signal said so, it is Kaz's card and gets Kaz's grade. If it covered everything and bought bonds, it is Mags's, and it needs a rule someone other than Mags can run. If it cut on the basis and the distance from fair value and covered on the equity turn, it gets Theo's grade, and it also gets his question, which is the one Ines asked him next: whether he would have had the nerve to write it in March 2009, with the screen showing what it showed.

Theo looked at the blank card on his desk, the one for Monday, and did not answer. It was a quarter to seven. Mags had already gone home.

### Case Study B: February–June 2020, the V that trend could not trade

Chapter 20 owns the day-by-day March 2020 tape (§20.5, where the ETF was the only price in town); this case keeps only what the episode says about trend.

*What happened.* Spreads went from post-crisis tights to a late-March peak (ICE BofA HY OAS roughly 1,100 bp around 23 March 2020, *approx.; check against the full series*) and most of the way back by June. On 23 March the Federal Reserve announced its corporate credit facilities, which is the cleanest $\kappa$ shock in the history of the index. Index CDS activity in Q1 2020 ran 78.1% above its trailing average (ISDA). HY bid–ask spreads gapped wider in February–March and then normalized (Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.20). The BTOP50 lost 2% over February–March 2020 (Robertson 2023), SG Trend "did not contribute positively" during COVID (Fidelity), and SG Trend ended 2020 up 6.24% (Hedgeweek, January 2021). SG notes that faster models did best that year.

*Why.* The whipsaw arithmetic of §10.6.2 with $T \approx 2$ months. Any lag over two weeks loses money on the round trip, and the only trend that paid was fast. Fast trend is ruinous in cash credit, where bid–ask had gapped, and affordable in CDX, which dealers kept quoting at record volume. A long-protection trend position is not an open market purchase of anyone's bonds. It is a bet that the dealers who quote CDX IG hundreds of times a day keep doing so. In March 2020 they did, and the cash market did not.

> **What ROBO Built from the Vague Version.** Theo, early in his first month: "Follow the trend and don't get whipsawed." *What ROBO built:* a strategy with a 36-month lookback and a 200 bp dead band that traded twice in 18 years and was long protection on CDX HY at full risk on 24 March 2020, the morning after the Fed announcement. It was never whipsawed. It simply arrived after every trend had ended. Speed is a parameter with units, and "don't get whipsawed" is an objective that the cash-in-a-drawer strategy satisfies perfectly.

*What the 2026 desk would have flagged.* A fast sleeve (20/120-day crossover on CDX, cheap to trade) flipping short in late February. A slow sleeve flipping short near the wides, which is the expensive moment. A blended forecast (§10.4) whose value term by late March outweighed the trend term, so the blend was cutting the short as the slow signal was adding to it. An index-versus-cash execution rule that kept the whole sleeve out of cash bonds. Lesson: in a $\kappa$-week, the trend sleeve's job is to be small, and the blend makes it small without anyone having to forecast the Fed.

### Case Study C: 2022, trend's best year was mostly duration

Chapter 8 owns the duration lens on 2022 (§8.7, the year "negative duration" was positive); this case keeps only the trend accounting.

*What happened.* The SG Trend Index returned +27.4% in 2022 while MSCI ACWI fell 18.4% (Cambridge Associates). The gains came mainly from short bond and rate trends, long US dollar, and energy (Hedgeweek, January 2023). Credit was not a named driver. HY OAS widened to roughly 600 bp in early July 2022 *(approx.; check against the full series)* and then partly recovered. Inside the record year, AlphaSimplex dates a "Fed Inflation Fight Reversal" drawdown of −10.1% from 14 June to 10 August 2022. Index CDS trading set a then-record \$36.4tn (ISDA).

*Why it matters for credit.* A trend follower trading cash HY ETFs in 2022 got two trends at once: a duration trend (rates up) and a spread trend (spreads wider). CDX isolates the spread trend, and it was a much smaller one. Desks that reported "credit trend made money in 2022" from cash total returns were mostly reporting a rates trade. Strip the duration with the Chapter 8 machinery before awarding credit any credit. The spread move was also the kind that the carry hurdle filters. A widening of a few hundred basis points over a year clears the HY hurdle of about 110 bp, so the 12-month return signal went short. The summer rally then charged the trend sleeve, which is the whipsaw at the 2-month horizon inside a year that was convex at the 9-month horizon.

*What the 2026 desk would have flagged.* A credit trend sleeve reported on spread excess returns, separate from any rates trend. A 3-month signal giving back part of its gain in July–August. A 12-month signal holding the short through the summer at moderate cost. Lesson: convexity and whipsaw happen in the same year at different horizons, which is the argument for a multi-horizon ensemble with weights fixed in advance.

### Coda: April 2025, "Liberation Day" (FRED-verified spreads)

#### Liberation Day, and the week the Pair Book found out what it was long

*A replay for Theo and a flashback for the pod. The desk, Vantress Capital Management and its people (Dov Adler, Wen Zhao, Marcus Oyelaran) are fictional composites, and "the desk's fictional run" or "the platform's fictional run" labels every invented model output. The spreads are ICE BofA via FRED (`BAMLH0A0HYM2`, `BAMLC0A0CM`); the SG, Man and ISDA figures are as cited.*

Ines ran the second replay at 7:20 the next morning, Friday, before the open, which she does only when a replay looks too much like the tape. The folder was called `2025-04`. "Last night you traded the future that paid," she said to Theo. "This is the one Mags named first."

**Cut one: the close of Thursday, 3 April 2025.** The screen showed seven weeks of high yield. ICE BofA US HY OAS had been 2.62% on 18 February, near the tights of the cycle. It was 3.42% at the close on Wednesday 2 April, the afternoon of the Rose Garden tariff announcement, and 4.01% at Thursday's close. Kaz read the sleeve as it would have stood that evening (the desk's fictional run). The fast sleeve was one session from flipping short. The 60-day EWMA had exactly two violent days in its bucket and had barely noticed them. The DTS forecast had noticed at once, because it reads the spread itself: the long was already down to about $3.42/4.01 \approx 0.85$ of Wednesday's notional, before any signal had changed its mind. Figure 10.2 shows where the two forecasts would go from there, the DTS one to 0.74 at the wides and the EWMA, once its bucket filled, harder still, to 0.61 by 4 April.

"Same card as yesterday," Ines said. "Size, speed, and the print that makes you cover."

Theo wrote for two minutes. *Let the fast sleeve flip, at half its normal risk. Leave the slow sleeve alone: the carry hurdle says this is not a trend yet, and a gap is not a ramp. Cover the fast short when the index has given back half the gap.* He turned the card over and slid it across.

The others had lived this week, so they did not write cards. They told him what they had done.

"I cut the sleeve's risk to a third on the Thursday night," Ines said. "The pot was a policy announcement. Nobody at this table knew more than the next headline, and when nobody at the table knows more than anybody else, you play small and you watch."

"I wanted full risk on the flip," Kaz said. "The signal is the signal. That was the spec." A pause. "I have since read the spec again."

Mags had said hers on the Thursday afternoon and had not changed a word since. "Gaps don't trend. They get explained." She looked at Theo's card without picking it up. "Nothing built from returns before the second of April could have known what was said in the Rose Garden. Whatever your signal does next, it's doing it *after* the news. It's a commentator, not a forecaster."

**Cut two: Wednesday, 9 April.** Ines advanced the tape. High yield closed at 4.61% on Monday 7 April, the high of the year, a hundred and nineteen basis points in three sessions; the fast sleeve had flipped short into it, near the wides, which is where a sleeve that follows a gap always arrives. On Wednesday afternoon the administration announced a ninety-day pause on most of the new tariffs, and the equity market turned within the hour. HY closed the day at 4.37%, and IG OAS printed its own high of the episode, 1.21%, that same Wednesday, two sessions after HY's. By mid-May HY was back near 3.1%, and on 30 June it was 2.96%. The whole round trip took about six weeks.

"Write the whipsaw formula," Ines said, and Theo did: a V lasting $T \approx 1.5$ months, so any signal lagging by more than a quarter of that, about eight trading days, loses money on the round trip. A three-month credit signal would have flipped short within days, after the gap, and then sat in front of a six-week V. The public record of the real trend followers that month lines up with the arithmetic. The SG Trend Index lost 4.9% in April (SG Prime Services). Man reports that trend repositioned after the 2 April shock and was positive by 9 April. The venue, for its part, got busier: index CDS activity in Q2 2025 ran 20.9% above its trailing average while single-name activity fell 20.7% (ISDA). Everyone who wanted out of credit risk in a hurry went to the index, which is exactly what §10.1.1 says the index is for.

Theo looked at his card. His cover print, half the gap given back, was somewhere around 4.0%, and the tape had not reached it on the 9th. "I covered late," he said.

"You covered small," Ines said. "Hold that thought. The interesting part of this week happened on another floor."

**A flashback: Vantress, Thursday 10 April 2025, 7:12 a.m.** *(Theo knows this part only as Ines tells it; Ines's desk quotes Dov's pod most weeks.)* Marcus Oyelaran's overnight x-ray for the platform's credit pods carries a row of style factors under the market factors, and one of them is a credit trend sleeve: a 20/120 crossover on CDX HY, DTS-scaled, the same kind of thing Ines's desk runs. Dov Adler's book had never shown up on that row. On the morning of 10 April it did. Over the seven sessions from 1 to 9 April, the book's daily P&L had a correlation of −0.6 with the trend factor (the platform's fictional run), and the number was printed in orange.

Marcus called at 7:14. He did not ask what Dov thought of tariffs. He asked the only question he ever asks: "What are you long that you didn't mean to be?"

"Nothing," Dov said, and then, because he is honest before eight in the morning, "nothing on purpose." The book was twelve pairs, every one matched on market-value DTS at inception, the index trimmed with a small CDX HY position on top. The hedge had removed the index. What remained was supposed to be twelve separate views about twelve separate pairs of issuers, each one a sentence with a date in it.

Wen Zhao had the pairs on her screen by 7:20, and she found the leak in two passes. The first pass was the residuals. In calm months the twelve pairs' idiosyncratic P&L had correlated about 0.3 with each other, the common whisper Chapter 8 (§8.8) teaches a platform to listen for (the platform's fictional run). In those seven sessions every residual moved the same way, because in a gap the things that make one credit "idiosyncratically" weaker than another (more leverage, a nearer maturity, a sponsor with a reputation) all get repriced by the same headline at once. The second pass was the theses. Dov's sentences were different, but read together they rhymed. Every one of them, in some form, said "this one is too wide for what it is." Every pair was long the cheaper name and short the richer one, which is a value tilt (Chapter 9), and a value tilt in credit carries beta that DTS matching at inception does not see. In a gap the cheap names gapped further.

"So the book was long risk," Marcus said.

"The book was short protection," Wen said, "which is the same sentence in the language of that factor. The trend sleeve bought protection on the 4th. We were the other side of it, without anyone asking us."

The −0.6 was the sign of exactly that. While spreads gapped wider, the trend sleeve made money and the Pair Book lost it; when the pause came on the 9th, the sleeve gave money back and the book recovered. The book had been neutral at inception. That turned out to be a sentence about a day, not about a week.

Dov wrote one line in the notebook he keeps for lines like that: *a gap is a factor I did not hedge.* A year later, in April 2026, he opened the pair the Pair Book now calls PB-01, and the line is visible in how it was built.

> **The Pair.** *Pair Book entry PB-01 (printed in Chapter 1-B as entry 1B-1), Dov Adler's pod at Vantress Capital Management (fictional composite). Kestrel Roofing and Halvorsen Packaging are fictional; every number is illustrative.* **Legs and hedge.** Long \$60mm Kestrel 6% 2030; short \$39mm Halvorsen 7.25% 2029, borrowed through the platform's prime broker; matched on market-value DTS at inception in April 2026 (about 72,600 against 71,600, Chapter 1-B); residual beta trimmed in CDX HY. **What the hedge removes.** The index: high-yield spread beta, most of the building-products sector, most of the rate risk. **What idio remains.** Kestrel's credit against Halvorsen's, and this is where the present chapter's tool applies to a pair. With DTS-neutral weights and similar spread durations, the pair's spread carry nets to roughly nothing, in one line: $w_L\,D\,s_L = w_S\,D\,s_S \Rightarrow w_L\,s_L - w_S\,s_S = 0$, so the net spread carry is zero and $\Delta s^{*}_{\text{pair}} = 0$. The carry hurdle of §10.1.2 on the pair is zero, so a return-based trend rule on the pair's P&L and a spread-based rule on the differential are the same rule. Residual momentum in the differential is exactly what Dov is betting on when he lets a winning pair run. **The April 2025 lesson, built in.** PB-01 is long the *tighter* credit and short the wider one: the mirror image of the 2025 book's value tilt. In a gap it leans toward protection, not away from it. One pair is not a book, though: by September 2026 the rest of Dov's book had drifted back to a value loading that Marcus's x-ray would find again (Chapter 9, §9.7.2). And the mirror image leaks too. **What leaks.** The ruler. The trend sleeve's notional is re-cut every day by its volatility forecast (§10.3); the pair's DTS neutrality was fixed in April and has drifted ever since, because the short leg widened far more than the long (Halvorsen from 90 to 78 and about 1,400 bp, spread duration down to 2.3), and under the proportional law the wider leg's DTS grows faster. Nothing in the pair re-cuts it unless Dov does, which is how the x-ray's orange line on Tuesday 13 October 2026 came to say the pair was net short about 40% of a leg (Chapter 1-B). The gap correlation of 2025 has not gone away; it has changed sign. **What it costs to carry and to short.** Spread carry about zero, coupons against financing roughly flat (Chapter 1-B). The short leg's cost is the borrow: Wen's sheet showed the fee reset from 50 bp to 300 bp in the week of Halvorsen's lender call, about \$0.91mm a year (Chapter 22 treats the fee as the only crowding gauge the pod can see). The CDX trim adds a fraction of a basis point of half bid–offer each time the residual beta is cut (§10.8.2 uses 0.25 bp for CDX IG; HY is wider). **Ledger line.** PB-01, stressed in Chapter 10 (trend lens): carry hurdle zero; trend on the differential is the view; leak is ruler drift against a vol-scaled market, plus the 2025 gap correlation with its sign flipped; book-level note, calm residual correlation about 0.3, gap-week correlation to the trend factor −0.6 (the platform's fictional run, April 2025).

**Grading the cards, Friday 16 October, 7:55 a.m.** Back on Ines's floor, she graded in the order the market had.

Kaz's 2025 card, full risk on the flip, was graded on the P&L it would have produced: a full-size short at the wides in front of a six-week V, the round trip the formula prices as a loss. It had been saved only because Ines cut the sleeve on the Thursday night. Kaz accepted the grade. Mags's card, four words, got full marks, which she has received before and appears to find mildly disappointing. Ines's own card she did not grade, "because the house doesn't grade the house," but she said what it had bought: the sleeve that was small lost little. Theo's card got a mixed grade and a short speech. His cover rule was late, as any rule written in terms of a retracement will be in a V; his size was close to right, and his sentence about the slow sleeve was the best line on the card, because it was the carry hurdle doing its job, for one session: at the next close the twelve-month rule cleared the hurdle (106 bp of widening against about 75, up from 59) and was whipsawed, which is the 13 short days of Figure 10.1, all in April 2025. The reader's card is graded the same way: a large position on the flip loses, a small one barely matters, and a card that left the slow sleeve alone deserves the mark Theo got for it.

The pod got the last grade, and Ines gave it without a smile. "Neutral wasn't. Twelve views turned out to be one view, and it was the other side of our trade." Then she put the folder away. "That's the thing the replay is for. Not the trend sleeve. Everybody knows trend can't trade a gap. The thing nobody checks is what *else* in the building turns out to be trend, or the opposite of it, on the one week it matters."

Index trend sleeves that were *small* in April 2025, because the 2024–2025 spread range gave the vol-targeted, carry-hurdled signal little to do, lost little. The lesson for the 2026 desk is about expectations, not engineering. Trend does not hedge gaps. It hedges the slow sell-off that sometimes follows a gap, and in April 2025 none followed.

## 10.8 Turnover, Costs, and Capacity

### 10.8.1 How often does a sign flip?

Under the null of no trend, a sign strategy still trades, and that turnover sets the cost floor.

> **Math, Gently.** *A random walk, and why a no-trend signal still rarely flips.* A random walk is the null hypothesis behind every trend strategy: each period's return is a fresh draw that remembers nothing, a coin toss with a size attached, and the index is the running total of the tosses. Nothing in it trends. Yet a twelve-month signal on a random walk changes sign only now and then, for a reason that has nothing to do with markets. This month's twelve-month window and next month's share eleven of their twelve months, and two sums that share eleven-twelfths of their contents are nearly the same sum, so they nearly always have the same sign. Their correlation is $11/12 \approx 0.917$. An old result, Sheppard's, says how often two correlated bell-shaped numbers land on opposite sides of zero: the probability is the angle whose cosine is their correlation, divided by $\pi$. Here $\arccos(0.917)/\pi \approx 0.13$, so the signal flips in about one month in eight, roughly 1.6 times a year, with no trend anywhere to cause it. Those flips are what a trend strategy pays for even when it is wrong about everything, and the general version is two lines long.

Let returns be i.i.d. with variance $\sigma^2$, and let $M^{(h)}_t$ be the trailing $h$-period sum. Consecutive sums share $h-1$ terms, so

$$
\operatorname{Cov}\big(M^{(h)}_t, M^{(h)}_{t+1}\big) = (h-1)\,\sigma^2,
\qquad
\rho_h \equiv \operatorname{Corr}\big(M^{(h)}_t, M^{(h)}_{t+1}\big) = \frac{h-1}{h}.
$$

For a bivariate normal pair with correlation $\rho$, Sheppard's formula gives $\mathbb{P}(\text{signs differ}) = \arccos(\rho)/\pi$. Each flip of a unit position trades two units, so annual turnover of the pure sign strategy, with $n$ periods per year, is

$$
\text{TO}_h = 2\,n\,\frac{\arccos\!\big((h-1)/h\big)}{\pi} \;\approx\; \frac{2n}{\pi}\sqrt{\frac{2}{h}} \quad (h \text{ large}).
$$

For the monthly 12-month signal of the box, 1.6 flips a year is about 3.1 units of turnover. A 1-month signal flips half the time, about 12 units a year. A daily 20-day signal has $\arccos(0.95)/\pi \approx 0.101$, about 25 flips and 51 units a year. Real trends reduce these numbers, because persistence makes flips rarer. Volatility scaling adds turnover, because the weight moves even when the sign does not. Section 10.10 checks the formula by simulation.

> **[SOURCE EXTRACTION]** *Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.19:* "Within classic quant, Momentum tends to have the highest turnover of any factor approach while both Size and Quality see the least churn."
>
> **Annotation.** The sentence sits inside a paragraph whose real subject is that the higher a strategy's turnover, the more its results depend on the accuracy of modelled transaction costs and on the availability of liquidity. Trend is momentum's time-series cousin and shares the problem, with one important difference. Cross-sectional momentum in cash bonds pays the cash bid–ask on every rank change, and §10.5.2 showed that this is enough to make top-decile EMC negative after costs. Time-series trend in index CDS trades a few units a year in the most liquid credit instrument there is. The modern desk therefore treats "momentum is expensive" as true for the cash cross-section and mostly false for the index time series, and it specifies costs per instrument and per regime rather than as one number for the whole strategy. A cost model fitted to 2019's calm bid–ask will understate the cost of the trades a trend sleeve actually makes, which cluster in the weeks when bid–ask has gapped.

### 10.8.2 Break-even arithmetic

Let $c^{\text{tr}}$ be the cost per unit of notional traded, roughly the half bid–offer in spread times the risky annuity. The annual cost drag is $c^{\text{tr}}\times\text{TO}$. Illustrative magnitudes *(illustrative; replace with your own execution data)*: for CDX IG with a half bid–offer of 0.25 bp and $\text{RPV01} \approx 4.5$, $c^{\text{tr}} \approx 1.1$ bp of notional, so a 12-month sign strategy pays about $3.1 \times 1.1 \approx 3.5$ bp a year. For a cash IG bond with a half bid–offer of about an eighth of a point, $c^{\text{tr}} \approx 12.5$ bp, so the same strategy pays about 39 bp a year. A top-decile cash EMC book turning over 73% a month (about 8.8 units a year) pays about 110 bp a year, which is the arithmetic behind the negative net return of §10.5.2. On costs, trend lives in the index and dies in cash.

The documented index market supports the low-cost case. The CFTC's study of the Bloomberg SEF from May 2014 to September 2016 found average daily CDX IG volume of \$7.05bn across 108 trades, with a price impact for CDX HY trades above \$500mm of about 0.3 bp, about 0.5% of the spread (Haynes and McPhail, CFTC Office of the Chief Economist, 2017). By 2025, ISDA's figures imply roughly \$67bn a day of CDX IG activity on average (our arithmetic: 43.4% of \$39.0tn over about 252 trading days). The caveat comes from Collin-Dufresne, Junge, and Trolle (2020), *Market Structure and Transaction Costs of Index CDSs*. The market remains two-tiered: client trades are large, infrequent, and informed, and dealers price-discriminate on expected impact.

Ines replays the trend sleeve's April 2025 entry through markouts, as she replays every hand. "Look at the hand history," she tells Theo. "Every CTA's 20/120 crossover flipped within the same two days. The dealers knew you'd call before you did, because you told them in your marketing deck." She has sat in the other chair for most of her career, and from there it looks like this.

> **View From Another Seat.** *The index dealer.* A bank desk that makes markets in CDX IG quotes it hundreds of times a day and sees the two-tiered market of the studies above from the inside: large, infrequent, often informed tickets from real-money clients, and a smaller stream of tickets that are large, infrequent and *predictable*. Trend followers are the second stream. Their signals are close to public (moving-average crossovers at a handful of standard speeds), their flip dates cluster within a session or two of one another, and their size can be roughly inferred from their assets. To the dealer, predictable flow arrives gift-wrapped in the client's own marketing deck. The desk leans its quotes and its inventory into the flip before the first ticket lands, so the trend follower pays the spread twice: once in the quote, and once in the move the dealer has already made before quoting. What the dealer cannot pre-position against is flow that arrives at a random minute inside a window rather than at the close the signal flips, flow that stays out of the roll (where 25–50% of quarterly notional trades) and off the signal calendar, and large clips routed through futures blocks where the listed market is deep enough (§10.1's Trend Watch). Each of those is a choice the trend follower can make, and the dealer's way of grading whether it worked is the one Ines uses on her own desk: markouts at 5, 30 and 120 minutes after every fill.

**Capacity** follows from turnover. A 12-month trend sleeve trading 3 units a year at \$5bn of gross index notional *(illustrative)* trades about \$15bn a year, a few hours of CDX IG volume. Capacity binds in HY, in Crossover around the roll, and in any cash implementation. It does not bind for a desk-sized index sleeve.

## 10.9 Trend in the LMT Era: Jumps, Not Diffusions

Everything so far has treated spread changes as diffusions with level-dependent volatility. That is a good model of an index of 100 or 125 names. It is a bad model of a single issuer with a 2027 maturity wall, a cooperative ad hoc group, and a sponsor whose counsel has just discovered the phrase "open market purchase," still the most expensive three words in finance.

Theo saw this before Kaz did. "If the loan drops twelve points on an uptier, the trend signal flips short the next morning. That's when Mags buys."

"That's when I buy the *excluded* tranche at a price that already assumes I lose the lawsuit," Mags said. "Your robot sells it to me because it went down. Back in my day the sellers at least had the decency to have a reason."

### 10.9.1 The jump-diffusion correction to vol scaling

> **Math, Gently.** *Poisson jumps, and why variances add.* A Poisson process counts rare events that arrive at random at a steady average rate: defaults, distressed exchanges, the morning an uptier is announced. Its one parameter is the rate, here $\lambda^{\text{J}}$ a year. In a short period the chance of a jump is about the rate times the length of the period, and a jump this year says nothing about whether there will be one next year. Picture the index as a hundred coins and a single name as one coin, each weighted to land "jump" three times in a hundred years. Hold the one coin and a bad toss costs you seventy points; hold the hundred and the same toss costs a hundredth as much, because that coin is a hundredth of the book. The jump and the ordinary day-to-day wobble are independent, and independent risks add in variance, not in volatility, which is why the formula below has a plus sign between two squared things. Put numbers on a single-B name *(illustrative)*: jump rate 3% a year and a loss of 70 points give a jump variance of $0.03 \times 0.70^2 \approx 0.015$, a jump volatility near 12%. The same name's diffusion volatility, at a DTS of 0.18 and the $\beta^{\text{DTS}} \approx 0.23$ that Figure 10.2's calm-years fit gives, is about 4%. The jump is nine-tenths of the name's variance, and a position sized on the 4% alone is about three times too big. Spread across a hundred names, the jump's variance falls a hundredfold, to a volatility near 1.2%, and the diffusion is the larger part again. The index is a diffusion; the name is a coin.

Write the single-name excess return with a jump:

$$
r^{ex}_{i,t+1} = s_{i,t}\,\Delta t - D^{\text{spr}}_{i}\,\Delta s^{\text{diff}}_{i,t+1} - J_{i,t+1}\,\Delta N_{i,t+1},
$$

where $\Delta N_{i,t+1}\in\{0,1\}$ indicates a jump event (default, distressed exchange, or a liability-management transaction that moves value out of this tranche) with intensity $\lambda^{\text{J}}_{i,t}$ under $\mathbb{P}$, and $J_{i,t+1}$ is the loss per unit notional, for example $L = 1-R$ in a default. We add the superscript J because $\lambda_t$ is reserved for default intensity alone; an LMT jump is not a default. The conditional variance has two parts:

$$
\operatorname{Var}_t\big(r^{ex}_{i,t+1}\big) \approx (\beta^{\text{DTS}})^2\,\text{DTS}_{i,t}^2\,\Delta t + \lambda^{\text{J}}_{i,t}\,\Delta t\;\mathbb{E}\big[J^2_{i}\big].
$$

An EWMA estimates only the first part until a jump has happened, and a DTS forecast estimates only the first part, full stop. Both size the position as if the second part were zero. That error is largest in exactly the names where $\lambda^{\text{J}}$ is high, which are the names where a distressed-credit analyst would want the position to be *smallest*. The corrected weight is

$$
w_{i,t} = \frac{\sigma_{\text{tgt}}\;\text{sig}_{i,t}}{\sqrt{(\hat\beta^{\text{DTS}})^2\,\text{DTS}_{i,t}^2 + \hat\lambda^{\text{J}}_{i,t}\,\mathbb{E}[J_i^2]}},
$$

with variances annualized, so $\Delta t$ cancels. On the 2026 desk $\hat\lambda^{\text{J}}_{i,t}$ is a mapping from the Priming Risk Score of Chapter 13, $\hat\lambda^{\text{J}}_{i,t} = \lambda_0 + \lambda_1\,\text{PRS}_{i,t}$, calibrated on the post-2017 LMT sample, and $\mathbb{E}[J^2_i]$ comes from that tranche's position in the capital structure, since a non-participating first-lien loan in an uptier and a participating one have jumps of opposite sign. A trend signal from a diffusion model knows nothing about any of this. It needs to be told.

**At the index level the jump diversifies.** One default in CDX HY, with 100 equally weighted names and 30% recovery, costs $0.01 \times 0.70 = 0.70$ points of notional *(illustrative)*: a bad day, not a regime. Jumps scale like $1/N$ in variance, so the diffusion approximation is good for the index and poor for the name. That is the structural reason this chapter's trend engine trades indices, and the reason single-name trend is a different engine with a jump model attached.

**When the capital structure stops moving together.** Section 10.5 used Man's observation that trends are issuer-level and consistent across the capital structure. An LMT is the event that breaks that consistency, because value is being transferred between classes. During an uptier, the participating lenders' new super-priority debt rises, the excluded lenders' debt gaps down, and the equity may *rally* on the liquidity runway. A price trend in one tranche then says nothing about the issuer and a great deal about who was invited to the meeting. The cross-asset trend engine needs a decoupling flag (rolling correlation between the tranche and the issuer's equity falling below a threshold, or PRS above a threshold), and when the flag is up it switches the name from the trend engine to the event engine of Chapters 13 and 14.

> **[SOURCE EXTRACTION]** *Schmid_Credit_Risk_Pricing_Models p.48:* "Rating momentum means that prior rating changes may have predictive power for the direction of future rating changes. For example, downgrade rating momentum suggests that an obligor downgraded to B is more likely to be further downgraded than upgraded within the next year."
>
> **Annotation.** Rating momentum is a trend in the *intensity* $\lambda$, not in the price, and it is the one kind of single-name trend that survives the jump problem, because it trends the thing that drives the jumps. Schmid presents it as a departure from Markov rating transitions: the probability of the next move depends on the direction of the last one. For a trend desk it means a downgrade raises next year's downgrade probability, which raises $\hat\lambda^{\text{J}}$ in the weight formula above, which shrinks the position before the next jump instead of after. Lee, Naranjo, and Sirmans (2021), *CDS Momentum*, connect the two channels: CDS momentum of about 7.1% a year, strongest in liquid contracts ahead of slow-moving rating changes. Ratings move slowly, and the market partly anticipates them. The modern desk does not trade rating momentum as a stand-alone signal. Downgrades are public and their predictable part is priced fast in liquid names. It uses rating momentum, together with the PRS, as an input to the jump intensity that sizes everything else. It also remembers the RSSG lesson that ratings agencies are the last to arrive at a restructuring, usually just after the professionals have sent their invoices.

## 10.10 The Credit Trend Lab: A Reference Implementation

### Specification for AI Implementation

**The Spec You Hand the Robot.** Build `credit_tsmom.py`: a credit trend engine that (1) builds roll-safe, ACT/360 excess returns for spread-quoted and price-quoted indices; (2) computes sign, ensemble, and crossover trend signals; (3) sizes them with the maximum of an EWMA forecast, a DTS-law forecast, and a floor; (4) blends trend with carry and value using coefficients estimated only on past data; (5) tests equity-to-credit lead–lag with HAC standard errors and a Granger F-test; and (6) reports Sharpe ratio, drawdown, turnover, a convexity regression, and a crisis-window table. Weights known at $t$ earn returns from $t$ to $t+1$. Positive weight means long risk. Every guard below is an `assert`, and a failed guard stops the run.

| Object | Shape / type | Units and convention |
| :--- | :--- | :--- |
| `spread_dec` | `pd.Series[T]`, DatetimeIndex | decimal spread (0.045 = 450 bp), one `series_id` |
| `price_pts` | `pd.Series[T]` | points of par (CDX HY), coupon decimal (0.05) |
| `quotes` | DataFrame `[date, series_id, spread_dec]` | old and new series overlap on the roll date |
| `r` | `pd.Series[T-1]` | excess return per unit notional, long risk positive |
| `sig` | `pd.Series[T-1]` in $[-1,1]$ | known at close of $t$; NaN during warm-up |
| `vol` | `pd.Series[T-1]` | annualized decimal; floored at 0.5% |
| `w` | `pd.Series[T-1]` | notional per unit capital, capped at $\pm 10$ |
| `pnl` | `pd.Series` | `w.shift(1) * r`, warm-up dropped |

Edge cases the robot must handle and not guess: a return across two `series_id` values (raise); a missing quote for the held series on the roll date (raise with the date); non-positive or missing spreads (raise); exactly zero trailing returns (sign 0 is allowed but must be counted in turnover); FRED's "." for missing values (coerce and drop); the leverage cap binding (report the fraction of capped days). Numerical guards: volatility floor, leverage cap, `lstsq` rather than an explicit inverse in the expanding regression, and HAC standard errors whenever returns overlap.

The six blocks run in order in one interpreter. Blocks 1–5 are seeded simulations with asserted guards; block 6 adds the lead–lag, whipsaw, and convexity checks and runs on real data only when the FRED file is present.

The guard that failed at 2:14 a.m. on the Tuesday of roll week (§10.1.1) was one of the three in this block. A trend signal is one line of code, which is why the arguments about it happen in the other forty, and the first of those forty is the return series. With a vendor file of dates and spreads, the obvious move is to difference the spreads, multiply by duration, flip the sign, and call it a return. Lucía's ticket (§10.2.3) is the list of what that move gets wrong, and nothing on the list announces itself. The numbers come out looking like returns, and the backtest goes on to discover a Monday effect. A desk therefore writes the guards before the strategy and makes each one an `assert` that stops the run. ROBO will build exactly the series you describe, and it will not ask whether Mondays look suspiciously good.

Block 1 builds three return constructors and then tries to break them. `excess_returns` takes one spread series in decimals with a sorted `DatetimeIndex` and returns the carry on yesterday's spread, times the year fraction, minus duration times the spread change. The year fraction is read off the index itself, so a weekend is three days of carry and a holiday Monday is four. It raises on an unsorted index, a missing value, or a non-positive spread, because each of those would otherwise turn into a plausible-looking number. `cdx_price_returns` handles the price-quoted index directly: the price change over 100 plus the coupon times the same year fraction, with no round trip through spread. `roll_safe_returns` takes a long table of `[date, series_id, spread_dec]`, pivots it, and computes each day's return inside the highest-numbered series that was quoted the day before. No return ever spans two series. If that series has no quote on the next day, the function raises with the date.

The three guards are the point of the block. A flat 450 bp spread held for a year must earn exactly its ACT/360 carry. A CDX HY price pinned at 100 must earn exactly its 500 bp coupon. And two flat series, 350 bp and 360 bp, stitched the way a vendor stitches them, must show a fake loss of exactly duration times 10 bp, which is 0.40% of notional at $D=4$, while the roll-safe version earns pure carry on every day. On the desk this block is the only door through which returns enter the strategy. It is the wrong door for a single bond with accrued interest, pull-to-par or funding, because it is the linear excess-return approximation of §10.2.3 with no convexity term. Its one blind spot is the one Lucía met: `excess_returns` has never heard of a `series_id`, so a spliced series goes through it without complaint. The defense is structural, and it is her eleven lines: a `series_id` on every row, anything with more than one id routed through `roll_safe_returns`, and an overlap window that includes the roll date for both the old and the new series.

*The full listing is [Listing 10.1 in Appendix F](#code-10-1).*

The fast sleeve that crossed at 3:41 on Thursday 15 October, and the slow one that did not, were both built from this block. With clean returns in hand, the next problem is turning them into positions without fooling yourself. The template of §10.2 is a sign, and a sign is easy. What hurts is everything around it. When is the signal known, and which return does it earn? How big is the position when the tape goes quiet or goes mad? How often will the thing trade if there is no trend at all? Each question has a classic silent failure: a weight that earns the return that created it, a volatility forecast that sleeps through a gap, a turnover bill nobody added up before trading. Each also has an answer you can compute in advance. That combination, a well-known failure with a known right answer, is the best case for automation, so block 2 writes down the signals, the sizing and the scorekeeping, and then tests them against arithmetic.

Block 2 defines the machinery in layers. `tsmom_sign` is the sign of the trailing $h$-period sum of excess returns, NaN until a full window exists. `ensemble_sign` averages those signs across several lookbacks, so four lookbacks give positions in steps of one half, and it stays NaN until the longest lookback has data. `crossover_signal` takes the cumulative excess-return index, subtracts a slow EWMA (120 periods) from a fast one (20), divides the gap by its own rolling standard deviation, and passes it through `tanh`, which gives a smooth position in $(-1,1)$ instead of a flip. `ewma_vol` is the annualized zero-mean EWMA volatility, and `positions` sets the weight to the target divided by the larger of that volatility and a floor, times the signal, capped at plus or minus ten notional per unit of capital. `strategy_pnl` multiplies yesterday's weight by today's return. `sharpe`, `max_drawdown` and `turnover` do the bookkeeping, the last as the sum of absolute weight changes.

Three guards follow. On a synthetic path of 120 days of 1 bp tightening and then 200 days of 2 bp widening, the 60-day signal must be long during the tightening, short within one lookback of the turn, and the short must earn money every day after, Mondays included. A unit sign strategy must trade exactly two units per flip. And the flip rate of a 12-period sign on white noise must match Sheppard's $\arccos(11/12)/\pi \approx 13.1\%$ from §10.8.1, which is 3.1 units of turnover a year at monthly frequency. The block is built for index-level series at daily or monthly frequency; a single name needs the jump-aware forecast of §10.9.1 in place of the volatility. The line that matters most is the one-period shift inside `strategy_pnl`. The signal and the volatility both use the close of $t$, so the weight may only earn the return from $t$ to $t+1$. Remove that shift and the backtest improves dramatically, the live book does not, and the difference is the entire return of the strategy.

*The full listing is [Listing 10.2 in Appendix F](#code-10-2).*

When Kaz reported two "significant" coefficients at the 12 October model review, Theo's question was really about this block: what would the machine have said in a world where the answer is known? How do you know a trend pipeline works? Not by running it on CDX. The index has existed for about twenty-two years, which is twenty-two annual observations of a strategy whose Sharpe ratio you are trying to measure to within a few tenths. Luck and skill are indistinguishable at that sample size, and the first bug that happens to flatter the backtest will look like a discovery. The cheaper test is to build two worlds where you know the answer. In one, spread changes are a random walk, so no trend exists and the strategy must earn nothing. In the other, a widening month is followed by a smaller widening month, so trend exists and the strategy must earn something. If the machine reports a profit in the first world, it is peeking. If it finds nothing in the second, it is blind. This is the one place in the book where Kaz's habit of assuming Gaussian shocks is not a sin but the experimental design.

Block 3 runs that experiment. `simulate_ar1_changes` draws Gaussian monthly spread changes with persistence $\phi$, so that each change equals $\phi$ times the last one plus a fresh shock, and discards the first 200 draws as burn-in so the series starts in its stationary state. With $\phi=0$ spreads are a random walk. With $\phi=0.25$ a widening month is followed, on average, by a quarter as much widening. The shock size is set to 25% of a 450 bp level per year, about 32 bp a month. The returns are mark-to-market only, minus duration times the spread change, with no carry, so no drift can pass itself off as trend. The strategy is the ensemble sign over 1, 3, 6 and 12 months from block 2, unscaled, and its annualized Sharpe is computed over 6,000 months, or 500 years.

Two assertions carry the argument. The random-walk Sharpe must sit within $3.5/\sqrt{\text{years}}$ of zero, which is about 0.16, and the persistent world must beat it by at least 0.3. In the seeded run the two come out near 0.06 and 0.61. The block is a unit test for every change to the signal code, not evidence about credit. It says the machine can detect persistence of 0.25 if it exists, and nothing about whether credit has any; that estimation problem belongs to §10.4. The trap is the sample length. At 500 years the standard error of an annualized Sharpe is about 0.05. At CDX's age it is about 0.2, so the 0.3 gap this block detects with ease is one that real data cannot resolve. A real-data backtest deserves the confidence of twenty-two years, not of five hundred.

*The full listing is [Listing 10.3 in Appendix F](#code-10-3).*

The 0.83 on Kaz's screen in the cold open came out of the forecast this block tests. Picture the morning after a bad week. The index went from 450 to 650 bp over Thursday and Friday. A trailing EWMA of returns learns about it from realized moves, which means it has two loud days in a long quiet memory and needs weeks to catch up to the new regime. The spread level, which every screen on the desk shows in large type, knew on Friday afternoon: at 650 bp, a typical day's move is about 44% bigger than it was at 450 bp. Section 10.3 argued that in credit the second signal is better, because the standard deviation of a spread change is proportional to the spread. The desk wants two things from the code. First, that the proportionality can be recovered from data with a method you could actually run. Second, that sizing by it has a clean consequence, which is a constant spread-duration exposure whatever the signal says.

Block 4 tests both claims in a world built to satisfy them. `simulate_log_ou_spreads` runs a daily Euler step of an Ornstein–Uhlenbeck process on the log spread, with mean reversion of 0.5 a year around 450 bp and volatility $\sigma=0.25$. Exponentiating keeps spreads positive, and the spread change has a standard deviation proportional to the level, with $\beta^{\text{DTS}}=\sigma$ by construction. `beta_dts` recovers that coefficient the way a risk team would. It computes the 63-day rolling standard deviation of spread changes, annualizes it, and regresses it through the origin on the window's average spread level, using non-overlapping windows so the observations are not recycled. Forty simulated years must give a coefficient within 20% of 0.25.

Then the block sizes the 60-day trend signal three ways, each to a 10% target: the EWMA forecast, the DTS-law forecast $\hat\beta\,D\,s_t$, and the larger of the two. The realized volatility of the EWMA and DTS versions must land within 25% of target, and does, near 10%. The max version runs a little lower, about 9.6% in the seeded run, because taking the larger forecast is conservative by design. The last guard is the identity behind the chapter's claim. Wherever the leverage cap does not bind, $|w|\,D\,s$ equals the target divided by $\hat\beta$, here 0.4, whatever the signal does. The block belongs on index spreads, where the law holds; on single names jumps add a variance term (§10.9.1). Its quiet weakness is that `beta_dts` is estimated once on the whole sample and then used on every day. That is harmless in a simulation where $\beta$ is constant. On real data it lets later years leak into earlier sizing, which is why production re-estimates on an expanding window, and why block 6's real-data run, which reuses the full-sample estimate, counts as in-sample for that one parameter.

*The full listing is [Listing 10.4 in Appendix F](#code-10-4).*

On the afternoon of the 12 October review Kaz reran the blend at the corners of the confidence region; this block is the laboratory where that habit starts. Section 10.4 ended the tribal war with a regression: one equation, two coefficients, $\kappa$ for the value tribe and $\phi$ for the trend tribe, and a promise that the data would size each. Keeping that promise is harder than writing it. The coefficients have to be estimated at every date using only what was knowable at that date, and the one-month slip that lets a regression see the return it is forecasting is exactly the kind of bug that makes a blend look brilliant. Section 10.4.2 warned that $\kappa$ is the shaky one, with a standard error the size of the coefficient. The desk therefore wants a laboratory with known truth: simulate the model, estimate it the way production would, and check what comes back before anyone believes an estimate on real spreads.

Block 5 is that laboratory. `simulate_d3` generates 1,200 months of the D3 model of §10.4: each month's spread change is $\kappa(\bar s-s_t)$ plus $\phi$ times the last change plus a shock whose size is proportional to the spread, with $\kappa=0.03$, $\phi=0.25$, $\bar s=4.5\%$, $\beta=0.25$ and a 25 bp floor. `d3_components` then walks forward from month 120. At each date it regresses the next spread change on a constant, the spread level and the current change, using only pairs completed by that date and `lstsq` rather than an explicit inverse. From the fitted coefficients it builds three forecasts of next month's return: carry, $s_t\Delta t$; value, which is $-D$ times the fitted expected spread change and equals $D\kappa(s_t-\bar s)$ without ever dividing by $\hat\kappa$; and trend, $-D\hat\phi\,\Delta s_t$. It also returns $\hat\kappa$ and $\hat\phi$.

The block forms three sleeves, carry plus value, trend, and their sum. It weights each by forecast over DTS-law variance, the mean-variance rule of §10.4.1 with unit risk aversion, and lets each weight earn the next month's return. The assertions are modest: the blend equals the sum of its parts, and the final $\hat\phi$ exceeds 0.10. In the seeded run $\hat\phi$ is 0.238 against a true 0.25, and the trend and carry-plus-value P&Ls have a correlation of about $-0.03$, which is why the blend's Sharpe, about 1.1 against 0.8 and 0.7 for the sleeves, beats both. That is the no-tribes argument as arithmetic, in a world built to satisfy it. The ex post volatility scaling in the printout is display only. The block tests blending code; its Sharpe ratios are not a forecast for credit. The bug it exists to catch sits in the range of `k`. The regression pairs run up to $\Delta s_{t}$, not $\Delta s_{t+1}$. Extend the range by one and the estimate has seen the return it is predicting, and the blend improves for no reason except that it has cheated.

*The full listing is [Listing 10.5 in Appendix F](#code-10-5).*

Marcus's orange −0.6 on 10 April 2025 was a correlation over seven sessions of one shock, and the first question any model-review committee would ask about a number like that is the question this block answers: how much of it survives honest standard errors? The chapter has made four claims that such a committee would ask to see reproduced before it let the strategy near capital. Equity appears to lead credit, but stale marks can fake the lead. A trend follower cannot trade a V. The payoff of trend is a smile, and the smile is the receipt for momentum. And the strategy's behavior in 2008, 2020, 2022 and April 2025 is a table, not an anecdote. All four rest on regressions with overlapping or autocorrelated data, where a plain OLS t-statistic is cheerfully overconfident. The desk wants one inference tool that is honest about that, and one place where each claim is turned into something that can fail an assertion.

Block 6 starts with the tool. `ols_hac` fits OLS and reports Newey–West standard errors: the sandwich estimator with Bartlett-weighted autocovariances of the score up to a chosen lag, four by default. `granger_f` compares a regression of next-period $y$ on its own lag with and without the lag of $x$ and returns the F statistic and p-value for the one restriction. Four tests follow. In (a), weekly equity returns drive a "true" credit price contemporaneously only, and the observed mark updates with probability one half and otherwise stays stale. The lagged-equity coefficient on the marks is significant (t about 9.9 in the seeded run, asserted above 3) and on the true prices it is not (about $-0.6$). In (b), `v_capture` computes the P&L of a lagged follower on a stylized V and checks it against the closed form $2d(T-4L)/T$ for four combinations of width and lag. The follower profits only if its lag is under a quarter of the V. In (c), a regression of quarterly trend P&L on the market return and its square first proves it can find a smile built into a synthetic payoff, then runs on the persistent-trend simulation of block 3. A positive quadratic coefficient is printed, not asserted. In (d), `crisis_table` and `perf_summary` report window returns, drawdowns and turnover if the FRED file from block 1 is present.

The HAC tool belongs wherever returns overlap; its F-test is not HAC-robust and is not meant to be read as if it were. The quiet failure is in (d). Any crisis window with fewer than 20 observations is silently skipped, so a short data file produces a shorter table, not an error. FRED's "." for missing values is coerced and dropped, and the table that remains is only as complete as the file. Count the rows before you read the story.

*The full listing is [Listing 10.6 in Appendix F](#code-10-6).*

What the blocks demonstrate, in desk language: block 1 shows that a vendor-spliced series loses $D^{\text{spr}}\times 10$ bp on a flat roll that costs nothing; block 2 that turnover is arithmetic you can know before you trade; block 3 that the machinery finds nothing in a random walk and something when persistence is real; block 4 that inverse-volatility sizing in credit holds DTS constant; block 5 that $\phi$ is estimable on a long sample while $\kappa$ is noisy; and block 6 that half the "equity leads credit" result you will ever see in cash bonds can be manufactured by marks that print every other week.

## 10.11 Desk Debrief

**Finder.** Where each idea lives: its equation, the box that builds the intuition, the scene where someone has to use it, and the listing that implements it.

| Concept | Equation | Intuition | Judgment | Code |
| :--- | :--- | :--- | :--- | :--- |
| Carry hurdle | $\Delta s^*_h = \bar s\,h\,\Delta t / D^{\text{spr}}$ (§10.1.2) | The landlord (§10.1.2) | 55/112 in the cold open; Ines's two bars (§10.1.2); a zero hurdle on a DTS-neutral pair (PB-01, §10.7 Coda) | Listing 10.1 |
| Roll-safe returns | $I_{t+1} = I_t\,(1 + r^{(k)}_{t+1})$ (§10.2.3) | The flat-spread carry guard (§10.2.3) | Lucía's Tuesday of roll week (§10.1.1) | Listing 10.1 |
| TSMOM weight and EWMA volatility | $w_{i,t} = (\sigma_{\text{tgt}}/\hat\sigma_{i,t})\,\text{sig}^{(h)}_{i,t}$ (§10.2.1) | The leaky bucket (§10.2.1) | Thirteen weeks against 65 days (§10.2.1) | Listing 10.2 |
| Volatility scaling is DTS scaling | $w_{i,t} = \sigma_{\text{tgt}}\,\text{sig}_{i,t} / (\beta^{\text{DTS}}\,\text{DTS}_{i,t})$ (§10.3.1) | The thermometer (§10.3) | The 0.83 in the cold open; the insurer and the CLO manager (§10.3.2) | Listing 10.4 |
| Trend plus carry and value | $\mathbb{E}_t[r^{ex}_{t+1}] = s_t\Delta t + D\kappa(s_t-\bar s) - D\phi\,\Delta s_t$ (§10.4.1) | The spring and the door (§10.4.1); the short film (§10.4.2) | The 12 October model review (§10.4.2) | Listing 10.5 |
| Equity leads, stale marks fake it | fake lead $\approx p(1-p)\,\beta^{\text{ce}}$ (§10.5.3) | The wall clock (§10.5.3) | Kaz's EMC pitch (§10.5.2); Theo sorts by print count (§10.5.3) | Listing 10.6 |
| Trend is a straddle | $r_{t+1}\,[2\Phi(\cdot) - 1]$ (§10.6.1) | The bell and the tilted cloud (§10.6.1) | The GFC replay, 9 March 2009 card (§10.7, Case A) | Listing 10.6 |
| Whipsaw | capture $= (T - 4L)/T$ (§10.6.2) | The hiker in the valley (§10.6.2) | The Liberation Day replay and the pod's −0.6 (§10.7, Coda) | Listing 10.6 |
| Turnover under no trend | $\text{TO}_h = 2n\,\arccos\big((h-1)/h\big)/\pi$ (§10.8.1) | Shared windows (§10.8.1) | The index dealer (§10.8.2) | Listing 10.2 |
| Jumps in single names | variance adds $\lambda^{\text{J}}\,\mathbb{E}[J^2]$ (§10.9.1) | A hundred coins and one (§10.9.1) | Theo and Mags on the uptier (§10.9) | Spec, SINGLE NAMES |

*The desk is fictional.* At 4:02 p.m. on Friday 16 October, twenty-four hours after the fast sleeve bought its protection, Ines picked up Theo's index card from his desk and read it aloud to the row. *Size: the fast sleeve at half its normal risk, and let the DTS forecast keep cutting it; nothing on the slow sleeve, which has spent 55 of its 112. Speed: listen to the equity market first, the residual trend of the high-yield names' stocks, and let credit's own twelve-month signal vote last. Cover: the fast short on a close back inside 2.95%, half the move since 22 September; add only on a close above 3.46%, the March high, which would make this the first sustained credit trend since 2022. On the back: none of this applies to the single name Mags bought this morning (§10.9).* Kaz said it was a spec. Mags said it was a card, which from Mags is a grade. Ines did not grade it at all. "Ask me in a month," she said. "The week isn't over, and the market hasn't told us which future this is." She put the card in the folder where she keeps the others, between April 2025 and the summer of 2007.

- **Trend is absolute; momentum is relative.** Trade credit trend in indices (CDX, iTraxx, listed credit futures). Signal it from the markets that price information first: equity, then CDS, then cash.
- **Trend on returns, not spread levels.** The carry hurdle $\Delta s^*_h = \bar s\,h\,\Delta t / D^{\text{spr}}$ means 12-month HY trend goes short only after roughly 110 bp of widening *(illustrative)*. Write the version you mean.
- **Vol targeting in credit is a constant-DTS budget.** It sells after widening before any signal fires. Forecast volatility as $\max(\text{EWMA}, \beta^{\text{DTS}}\text{DTS}, \text{floor})$ and cap leverage.
- **Do not join a tribe.** $\mathbb{E}_t[r^{ex}_{t+1}] = s_t\Delta t + D\kappa(s_t-\bar s) - D\phi\Delta s_t$. Estimate $\kappa$ and $\phi$ on an expanding window and blend; carry and trend disagree exactly after large moves.
- **Equity leads credit, and stale marks fake it.** A bond that prints with probability $p$ shows a fake equity lead of about $p(1-p)\beta^{\text{ce}}$. Test on trades, or on the index.
- **Convexity is the receipt for momentum.** The smile coefficient is positive if and only if returns trend. A V captures $(T-4L)/T$ of the round trip. Trend hedges slow sell-offs, not gaps.
- **IDO or it didn't happen.** Credit TSMOM's alpha against passive beta had a *t*-statistic of 0.49 in AQR's test. Trend is beta that changed its mind. Strip it before you call it alpha.
- **Single names jump.** Add $\lambda^{\text{J}}\,\mathbb{E}[J^2]$ to the variance, map $\lambda^{\text{J}}$ from the Priming Risk Score, and switch engines when the capital structure stops moving together.

### The Spec You Hand the Robot

```text
TASK: credit_tsmom engine (index trend sleeve). Positive weight = long risk (sold protection).
INPUTS: daily spreads (decimal) or prices (points) per index and series_id; optional equity TR series;
        spread duration / RPV01 per day; coupon (IG 100 bp, HY 500 bp); FRED OAS CSV for research.
RETURNS: r_t = s_{t-1} * days/360 - D * (s_t - s_{t-1}) within one series_id; price-quoted:
         dP/100 + c * days/360. Never difference across series. Never use OAS level changes as returns.
SIGNALS (known at close t, applied to r_{t+1}; also report a 2-day lag run):
  sign TSMOM at 1, 3, 6, 12 months (21/63/126/252 days), ensemble mean; 20/120 EWMA crossover (tanh z);
  equity-to-credit: residualized equity momentum, horizons 1/3/6 months, each divided by sqrt(h).
SIZING: w = 0.10 / max(EWMA_vol(com=60), beta_DTS * DTS_t, 0.005) * sig; cap |w| <= 10;
        beta_DTS = zero-intercept fit of non-overlapping 63-day spread-change vol on spread level.
BLEND: f_t = s_t*dt - D*(a_t + b_t*s_t) - D*phi_t*ds_t, with (a, b, phi) from OLS on data up to t
       (min 120 months); w = f / (D * beta_DTS * s_t)^2 / dt, then scale to the risk budget.
SINGLE NAMES: variance += lambda_J * E[J^2], lambda_J = l0 + l1 * PRS; switch to the event engine when
       PRS > threshold or 63-day corr(tranche, equity) < threshold. Do not run index logic on names.
REPORT: Sharpe, vol, max drawdown, turnover/yr, % days capped, quadratic smile b2 (quarterly, HAC),
        alpha and beta vs passive long risk, crisis table (2007-06..2009-06, 2020-02..06, 2022-01..10,
        2025-02..05) where data cover the window.
GUARDS (assert, fail loudly): carry guard (flat spreads -> s*days/360, 1e-10); roll guard (no cross-series
        return); sign guard (monotone widening -> short within one lookback, positive P&L after);
        turnover = 2 x flips; random-walk Sharpe within 3.5/sqrt(years) of 0; realized vol within 25% of target.
DO NOT: forward-fill marks across days without a print flag; estimate anything with future data;
        "minimize whipsaw" (that objective is satisfied by holding cash forever).
```

### Exercises

1. **The Crossover hurdle.** iTraxx Crossover trades at 300 bp with a spread duration of 4.2. Compute the carry hurdle for a 6-month return-based trend signal, and explain to a PM why "spreads are trending wider" and "the trend signal is long" can both be true. *Check:* $\Delta s^*_6 = 0.03 \times 0.5 / 4.2 \approx 36$ bp. Any widening smaller than that over six months is, on a return basis, an uptrend paid for by carry.

2. **Sheppard's turnover.** For a monthly 3-month sign signal on i.i.d. returns, show that $\rho_3 = 2/3$ and that annual turnover is about 6.4 units. At a cost of 1.1 bp of notional per unit traded, what gross Sharpe ratio does a 10%-volatility sleeve need for costs to be under a tenth of its expected return? *Check:* $\arccos(2/3)/\pi \approx 0.268$, so turnover is $2 \times 12 \times 0.268 \approx 6.4$. The cost is about 7 bp a year at unit notional; scale it by your average $|w|$ before comparing with $\text{SR} \times 10\%$.

3. **Kaz's runway momentum.** Kaz proposes trading CDX HY on the trend of the median constituent's liquidity runway (Theo's 13-week model, aggregated). Write down what must be true for "runway momentum" to predict index excess returns *beyond* equity momentum, and specify the regression and the out-of-sample test that would kill the idea. Theo is not allowed to bring the USB stick to the review.

4. **The every-other-week bond.** Using §10.5.3, show that the spurious lead coefficient $p(1-p)\beta^{\text{ce}}$ is maximized at $p=\tfrac12$. Evaluate it for a bond that prints once every five weeks ($p = 0.2$). Then propose a sample filter that removes the artifact without discarding most of the HY universe. *Check:* $0.16\,\beta^{\text{ce}}$; condition on prints at both $t$ and $t+1$, or measure the lead on CDX, where $p\approx 1$.

5. **Liberation Day, priced.** Treat April–May 2025 as a V with $T \approx 1.5$ months. What effective lag makes the capture zero? If SG's 20/120-day crossover has an effective lag of a few weeks, what sign does the formula predict for its credit P&L over the episode, and why would a vol-targeted, carry-hurdled sleeve have lost less than the formula says? *Check:* $L = T/4 \approx 0.375$ months, roughly eight trading days. Any longer lag loses money on the round trip, and the loss is smaller for a sleeve that entered the episode small.

### Deep-Dive Resource Graph

**Podcasts**

- *Top Traders Unplugged*, Systematic Investor, episode 422, with Katy Kaminski, "Why Trend Following Rewards Patience" (17 October 2026): https://www.toptradersunplugged.com/podcast/why-trend-following-rewards-patience-ft-katy-kaminski/
- *Top Traders Unplugged*, with Patrick Welton, "Why Investors Keep Getting Trend Following Wrong" (30 September 2026): https://www.toptradersunplugged.com/podcast/why-investors-keep-getting-trend-following-wrong-ft-patrick-welton/
- *Flirting with Models* (Corey Hoffstein), Season 7, Episode 19, Jeff Rosenberg on systematic fixed income (18 August 2025): https://www.flirtingwithmodels.com/episodes/8V74zBaN4jN
- *Flirting with Models*, Season 7, Episode 25, Takahe Capital on trend-following spreads (12 January 2026): https://www.flirtingwithmodels.com/episodes/1iIqmQ7piJd
- **Lots More With Charlie McElligott on the Sharp, Strange Selloff** (*Bloomberg Odd Lots*, 21 March 2025). A positioning-flow reading of the March 2025 correction and of why momentum trades were hit, the cross-asset mechanism behind §10.5 and the dated coda in §10.7. https://omny.fm/shows/odd-lots/lots-more-with-charlie-mcelligott-on-the-sharp-str
- **Roberto Croce, Trend and Carry Within Assets, Across Assets, and Over Time (S6E8)** (*Flirting with Models*, 19 June 2023). Trend and carry as the two "super factors": combining signals of different speeds, weighing noise against continuation, and measuring bond carry correctly; the practitioner companion to §10.4 and the carry hurdle in §10.1.2. https://www.flirtingwithmodels.com/episodes/fN5gzryMqiE
- **137 Years of Trend: What the Evidence Really Shows, ft. Yoav Git** (*Top Traders Unplugged*, 5 September 2026). Revisits 137 years of trend following (diversification, risk management, oil squeezes, commodity market structure): the long-history frame for the "does it still work" argument in §10.1 and §10.6. https://www.toptradersunplugged.com/podcast/137-years-of-trend-what-the-evidence-really-shows-ft-yoav-git/
- **The Quarter That Tested Every Trend Follower, ft. Katy Kaminski & Harry Moore** (*Top Traders Unplugged*, 4 April 2026). Q1 2026 as an out-of-sample test, with sharp reversals, dispersion across CTAs, and the roles of market selection and speed; fresh material beside the dated coda in §10.7. https://www.toptradersunplugged.com/podcast/the-quarter-that-tested-every-trend-follower-ft-katy-kaminski-harry-moore/
- **Credit Microcycles at Diameter** (*Capital Allocators*, guest Jonathan Lewinsohn of Diameter Capital, 2 February 2026). The discretionary counterpart to a regime model: how a credit PM frames short cycles inside the long cycle, a contrast case for §10.9 and the regime filter. https://www.capitalallocators.com/podcast/credit-microcycles-at-diameter/

**Practitioner Writing**

- AQR, Hurst, Ooi, and Pedersen, "A Century of Evidence on Trend-Following Investing": https://www.aqr.com/Insights/Research/Journal-Article/A-Century-of-Evidence-on-Trend-Following-Investing
- AQR, Babu, Levine, Ooi, Pedersen, and Stamelos, "Trends Everywhere": https://www.aqr.com/Insights/Research/Journal-Article/Trends-Everywhere
- **Time-Series Momentum Works Everywhere** (QuantPedia, 16 June 2019). The accessible summary of the out-of-sample TSMOM test that includes five credit default swap indices among 82 new securities; cite the paper itself in the text and send readers here for the abstract (§10.2). https://quantpedia.com/time-series-momentum-works-everywhere/
- AQR, "You Can't Always Trend When You Want": https://www.aqr.com/Insights/Research/Journal-Article/You-Cant-Always-Trend-When-You-Want
- Man Group, "A Trend Following Deep Dive: The Dynamics of Dispersion": https://www.man.com/insights/deep-dive-trend-following ; "Trend Following and Drawdowns: Is This Time Different?": https://www.man.com/insights/is-this-time-different ; "Trend Following: Equity and Bond Crisis Alpha": https://www.man.com/insights/trend-following-equity-and-bond-crisis-alpha
- Kaminski and Wen (AlphaSimplex, June 2025), "Market Cycles and Managed Futures Drawdowns": https://www.alphasimplex.com/assets/files/2025.06---market-cycles-and-managed-futures---kaminski-and-wen.pdf
- Cambridge Associates (August 2025), "Does Trend Following's Recent Struggle Signal That the Strategy Is Structurally Broken?": https://www.cambridgeassociates.com/insight/does-trend-followings-recent-struggle-signal-that-the-strategy-is-structurally-broken/
- SG Prime Services (May 2025), "CTA Industry Update: Keeping Up with the Trend Followers": https://content.sgmarkets.com/CTA_UPDATE_KEEPING_UP_WITH_THE_TRENDFOLLOWERS_2025
- *The Hedge Fund Journal*, "AHL Evolution": https://thehedgefundjournal.com/ahl-evolution/
- ISDA (29 July 2026), "CDS Market Dynamics: Five Years of Activity and a Record 2025": https://www.isda.org/2026/07/29/cds-market-dynamics-five-years-of-activity-and-a-record-2025/
- Clarus FT (10 June 2026), March 2026 index CDS volumes: https://www.clarusft.com/us-firms-powered-march-2026-itraxx-swaps-volume-growth/
- The DESK (16 October 2026), Cboe iBoxx credit futures block trading: https://www.fi-desk.com/cboe-block-trading-has-arrived-in-credit-index-futures-2/
- Haynes and McPhail (CFTC Office of the Chief Economist, 2017), "The Liquidity of Credit Default Index Swap Networks": https://www.cftc.gov/sites/default/files/idc/groups/public/@economicanalysis/documents/file/oce_credit_swap_liquidity.pdf
- Top Traders Unplugged monthly trend-following performance reports (secondary compilations of SG and BTOP50 data; check against the index providers): https://www.toptradersunplugged.com/trend-following-performance-report-december-2025/

**Academic Papers**

- Moskowitz, Ooi, and Pedersen (2012), *Time Series Momentum*, *JFE* 104(2): https://ideas.repec.org/a/eee/jfinec/v104y2012i2p228-250.html
- Koijen, Moskowitz, Pedersen, and Vrugt (2018), *Carry*, *JFE* 127(2): https://ideas.repec.org/a/eee/jfinec/v127y2018i2p197-225.html
- Pitkäjärvi, Suominen, and Vaittinen (2020), *Cross-asset signals and time series momentum*, *JFE* 136(1): https://ideas.repec.org/a/eee/jfinec/v136y2020i1p63-85.html
- Daniel and Moskowitz (2016), *Momentum Crashes*, *JFE* 122(2): https://ideas.repec.org/a/eee/jfinec/v122y2016i2p221-247.html
- Barroso and Santa-Clara (2015), *Momentum Has Its Moments*, *JFE* 116(1): https://ideas.repec.org/a/eee/jfinec/v116y2015i1p111-120.html
- Moreira and Muir (2017), *Volatility-Managed Portfolios*, *JF* 72(4): https://ideas.repec.org/a/bla/jfinan/v72y2017i4p1611-1644.html
- Jostova, Nikolova, Philipov, and Stahel (2013), *Momentum in Corporate Bond Returns*, *RFS* 26(7): https://ideas.repec.org/a/oup/rfinst/v26y2013i7p1649-1693.html
- Haesen, Houweling, and van Zundert (2017), *Momentum spillover from stocks to corporate bonds*, *JBF* 79: https://ideas.repec.org/a/eee/jbfina/v79y2017icp28-41.html
- Hilscher, Pollet, and Wilson (2015), *Are Credit Default Swaps a Sideshow?*, *JFQA* 50(3): https://www.cambridge.org/core/journals/journal-of-financial-and-quantitative-analysis/article/abs/are-credit-default-swaps-a-sideshow-evidence-that-information-flows-from-equity-to-cds-markets/F7CCD2FFB20AAEACE1E093D12EEF7A31
- Norden and Weber (2009), *The Comovement of CDS, Bond and Stock Markets*, *EFM* 15(3): https://ideas.repec.org/a/bla/eufman/v15y2009i3p529-562.html
- Lee, Naranjo, and Sirmans (2021), *CDS Momentum: Slow-Moving Credit Ratings and Cross-Market Spillovers*, *RAPS* 11(2): https://ideas.repec.org/a/oup/rasset/v11y2021i2p352-401..html
- Lee, Naranjo, and Velioglu (2018), *When do CDS spreads lead?*, *JFE* 130(3): https://ideas.repec.org/a/eee/jfinec/v130y2018i3p556-578.html
- Collin-Dufresne, Junge, and Trolle (2020), *Market Structure and Transaction Costs of Index CDSs*, *JF* 75(5): https://ideas.repec.org/a/bla/jfinan/v75y2020i5p2719-2763.html
- Dickerson, Robotti, and Rossetti (2026), *The Corporate Bond Factor Replication Crisis*: https://openbondassetpricing.com/wp-content/uploads/2026/04/corp-bond-replication-crisis-dickerson.pdf
- Title only: Kim, Tse, and Wald, *Time Series Momentum and Volatility Scaling*; Baz, Granger, Harvey, Le Roux, and Rattray (2015), *Dissecting Investment Strategies in the Cross Section and Time Series*; Fung and Hsieh (2001), *The Risk in Hedge Fund Strategies: Theory and Evidence from Trend Followers*; Gebhardt, Hvidkjaer, and Swaminathan (2005), *Stock and bond market interaction: Does momentum spill over?*; Brooks, Palhares, and Richardson (2018), *Style Investing in Fixed Income*.

**Data & Code**

- FRED, ICE BofA US High Yield Index OAS: https://fred.stlouisfed.org/series/BAMLH0A0HYM2 ; ICE BofA US Corporate Index OAS: https://fred.stlouisfed.org/series/BAMLC0A0CM (FRED now serves only recent ICE history; the full series needs a licensed source).
- Open Source Bond Asset Pricing (bias-corrected bond factors and a TRACE daily panel): https://openbondassetpricing.com/
- ISDA SwapsInfo, H1 2025 credit derivatives volumes: https://www.isda.org/a/4cpgE/SwapsInfo-First-Half-of-2025-and-the-Second-Quarter-of-2025.pdf
- Chapter 7 (bond-factor replication), Chapter 8 (stripping beta), Chapter 9 (cross-sectional momentum), Chapter 13 (Priming Risk Score), and Appendix B (data atlas) are the in-book companions to this engine.

<!-- STATUS: COMPLETE -->
