# Chapter 10: Trend-Following & Time-Series Momentum in Credit

<!-- WRITER PLAN (sections appended in order as drafted; resume after the last complete "## 10.x" section):
10.0 Cold open; 10.1 What a trend is in credit (+ Trend Watch: index CDS venue); 10.2 TSMOM engine adapted;
10.3 Vol scaling is DTS scaling; 10.4 Trend plus carry; 10.5 Equity -> credit lead-lag;
10.6 Crisis alpha and payoff shape (+ Trend Watch: CTAs 2024-2026); 10.7 Case studies 2008/2020/2022/Apr 2025;
10.8 Turnover, costs, capacity; 10.9 Trend in the LMT era; 10.10 Specification for AI Implementation;
10.11 Desk Debrief, The Spec You Hand the Robot, Exercises, Deep-Dive Resource Graph. -->

## 10.0 Cold Open: The Model Has No Amygdala

At 4:02 p.m. on Thursday, 15 October 2026, the desk's trend book did something it had not done since the spring: it bought protection on CDX HY. The position was not large, but it was large enough that Ines walked over holding her coffee the way she holds a chip she has not yet decided to bet.

"Theo. Why are we long protection? Is the model panicking?"

Theo had been on the desk three weeks, and he had learned to answer a question about a model with a chart before an opinion. "High yield has widened about fifty-five basis points in three weeks. ICE BofA HY OAS was 2.68% on September 22 and it's 3.23% today. The fast sleeve crossed."

"The model cannot panic," Kaz said without looking up. "It has no amygdala. It has a 60-day EWMA."

"A 60-day EWMA is what an amygdala looks like when a quant writes the spec," Ines said.

Mags spoke from the end of the row without turning her chair. "It looks like April of last year: a hundred and nineteen basis points in three sessions, and all of it back inside six weeks. It also looks like the summer of 2007, and it looks like nothing at all." Now she turned. "Back in my day we had trend-following in credit. It was called 'Sal stopped picking up the phone.' When your dealer stopped returning calls, you sold whatever you could and asked questions at Christmas."

"So which one is it?" Theo asked.

"That's the hand," Ines said. "What's the pot, what are the odds, and who at this table knows more than you?"

Theo looked at the position. In his old job a bond at 60 always had momentum, toward a process. It was never heading toward 40 or toward 80, but toward a lender call, a cleansing announcement, a filing, or a deal. Restructuring bankers watch prices move all day, and they never believe the move *is* the information. Now he sat on a desk with a robot that believed nothing else.

The rest of the chapter answers the question on Theo's screen: **when is a move in credit spreads information about the next move in credit spreads, and how much should you bet on it?**

By the end of this chapter you will be able to: build a time-series momentum (TSMOM) signal on credit excess returns without the sign, roll, and quoting errors that break most first attempts; show that volatility targeting in credit is DTS scaling under another name, and explain why that makes trend followers into forced sellers; combine trend with carry and value in a single forecast whose coefficients you estimate, without joining either tribe; use equity returns as a leading credit trend signal and test whether the lead is real or an artifact of stale bond marks; explain trend's crisis convexity, and its V-shaped failures, from the shape of the payoff; and hand ROBO a specification it can implement without inventing a decade of whipsaw.

## 10.1 What a Trend Is, in Credit

Start with the instinct the reader already has. Every RSSG banker has run a trend strategy without calling it one. When a client's bonds fell five points on a weak quarter, the question in the room was never "is this bond cheap?" It was "who is selling, and are they done?" A stop-loss is a trend rule. So is an issuer DTS cap, a "reduce on downgrade" policy, and a risk committee that meets after a bad month. The systematic desk takes that reflex, writes it down, gives it units, and asks the uncomfortable question the committee never asks: *does it make money, net of the times it sold the low?*

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

Kaz had once heard Ines say "Crossover" on a call and spent twenty minutes drafting what he believed was a cross-default clause. "It's 75 sub-investment-grade European names, Kaz," Ines told him. "The only thing it crosses is your P&L in March."

**Sign conventions, which cause more bugs than any model choice.** Spread up means price down. "Long risk" means you *sold* protection and are long credit. Throughout the chapter a weight $w>0$ is long risk and $w<0$ is long protection. CDX HY and the Crossover's price-quoted cousins move the opposite way to their spreads. ROBO will happily build a strategy that is long when spreads tighten and *also* long when the price rises, if both columns are named `level`. Name them `spread_dec` and `price_pts`.

### 10.1.2 Trend on returns, not on spread levels: the carry hurdle

The first derivation is short, and it reverses a desk intuition. Let $s_t$ be the spread in decimal, $D^{\text{spr}}$ the spread duration, and $\Delta t$ the accrual year fraction (ACT/360 for CDS premium). To first order, the excess return of a long-risk position over one period is

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

This is the **carry hurdle**. For high yield at $\bar s = 4.5\%$ with $D^{\text{spr}} = 4$ and a 12-month window ($h\,\Delta t = 1$), $\Delta s^*_{12} = 0.045/4 = 112.5$ bp *(illustrative)*. HY spreads must widen by more than about 110 bp over a year before a return-based 12-month trend follower goes short. A spread chart that "looks like it's trending wider" by 60 bp is, on a return basis, a modest uptrend, because the carry paid for the widening. For IG at 1.0% spread and $D^{\text{spr}}=7$, the hurdle is about 14 bp. That asymmetry matters: the same rule is quick to turn short in IG, where carry is small relative to duration, and slow in HY, where carry is large relative to duration.

Two consequences follow. First, a trend rule built on the 12-month change in OAS is a *different strategy* from one built on 12-month returns, and the difference is the carry hurdle. Write the one you mean in the spec. Second, high carry makes a trend follower structurally long credit in normal times, which is why, as §10.6 shows, much of credit trend's return is a credit beta that changes its mind.

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

In the first, $I_t$ is the cumulative excess-return index (never the spread), $f<s$ are fast and slow spans, and $\hat\sigma^{\text{lvl}}_t$ is the volatility of the gap between the two averages, which makes the argument a z-score. SG's published CTA "Trend Indicator" is a 20-day/120-day crossover (SG Prime Services, May 2025). In the second, $\mathcal H = \{1, 3, 6, 12\}$ months gives a signal in $\{-1, -\tfrac12, 0, \tfrac12, 1\}$ that scales down when horizons disagree. Dynkin's equity-momentum signal for credit (§10.5) uses the same multi-horizon idea for the same reason.

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

**Price-quoted HY.** CDX HY quotes a price, $P_t = 100 + 100\,(c - s_t)\,\text{RPV01}_t$ in points. Build its return directly as $r_{t+1} = (P_{t+1} - P_t)/100 + c\,\Delta t$ and do not convert to spread and back. The conversion needs a curve and a recovery assumption, and the round trip is a quiet source of drift.

**Rolls.** A new on-the-run series starts every 20 March and 20 September, five years and three months long, with defaulted and downgraded names swapped out. ISDA notes that the roll window carries 25–50% of quarterly index notional. The new series quotes at a different spread: it is three months longer on an upward-sloping curve, and its constituents differ. *Never difference spreads across series.* Compute each day's return within one series, then switch series on the roll date, so that the total-return index is

$$
I_{t+1} = I_t\,\big(1 + r^{(k)}_{t+1}\big), \qquad k = \text{series held from } t \text{ to } t+1 .
$$

> **Ways This Blows Up.** *The spliced series.* An analyst downloads "CDX IG 5Y generic" spreads, which a vendor stitches across series, and differences them. Every roll day shows an artificial widening of a few basis points (the maturity extension), which with $\text{RPV01}\approx 4.5$ is a fake loss of about 0.1–0.2% *(illustrative)*, twice a year, every year. A 12-month trend signal sums two of those, so it carries a small bias toward short. Worse, a defaulted name dropping out of the HY series can show up as a fake *rally*. The fix is structural: store `series_id` on every row, and assert that no return is computed across two different `series_id` values. *The day count.* CDS accrues ACT/360. Over a weekend, three days of carry arrive on Monday. A strategy that ignores this treats Mondays as unusually good days, and a short-horizon signal will discover "the Monday effect in credit" and trade it.

**Lag and staleness.** The CDX close is a dealer-composite mark around 4 p.m. New York, and European indices close earlier. Cash bond OAS is a pricing-service evaluation, often of a bond that did not trade that day. The signal at $t$ should earn the return from $t+1$ to $t+2$ in production if your execution happens the next morning. Running the backtest with a one-day and a two-day lag and reporting both is cheap insurance. Dynkin's team runs the same check for equity-to-credit signals (§10.5).

## 10.3 Volatility Scaling Is DTS Scaling

Ines had watched the trend book through April 2025 and asked the question every credit PM asks a vol-targeted strategy exactly once: "Spreads went from 342 to 461 and the signal hadn't even flipped yet. Why did our notional fall by a quarter?"

Because the strategy was doing what credit risk managers have always done, with a formula instead of a meeting.

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

Three consequences follow, each one line.

*Constant DTS exposure.* The position's DTS exposure is $w_{i,t}\,\text{DTS}_{i,t} = (\sigma_{\text{tgt}}/\beta^{\text{DTS}})\,\text{sig}_{i,t}$, which does not depend on the spread. Volatility targeting in credit is a constant-DTS budget. Ines's quarter is arithmetic: at a fixed spread duration, notional scales as $342/461 \approx 0.74$.

*Exposure is anti-momentum in spreads.* Taking logs, $d\log|w_t| = -\,d\log s_t$ (holding duration fixed). A vol-targeted long-only credit book, with no trend signal at all, sells after widening and buys after tightening. It is half a trend follower before it has a signal. Kaz found this deeply satisfying and Theo found it alarming, which is the correct split.

*The P&L splits into a sign part and a timing part.* Write $w_t = \bar w\,\text{sig}_t + \bar w\,\text{sig}_t\,(\sigma_{\text{tgt}}/\hat\sigma_t - 1)$ with $\bar w = 1$. The first term is the pure sign strategy, and the second is a volatility-timing overlay. Kim, Tse, and Wald, *Time Series Momentum and Volatility Scaling*, report for 55 futures over 1985–2013 that TSMOM's monthly alpha is 1.27% *with* volatility scaling and 0.41% *without*: most of the headline result came from the scaling. In credit the timing term and the signal term point the same way after a widening (both cut long risk), so they compound. That is good in 2008 and expensive in April 2025.

> **[SOURCE EXTRACTION]** *Paleologo_Advanced_Portfolio_Management p.106:* "Volatility is persistent and partially predictable, while PnL has no strong relationship to volatility."
>
> **Annotation.** This is the general argument for volatility targeting, and credit satisfies both halves. Spread volatility is persistent, and because of the proportional law it is visible *in the spread itself* on the same day, without waiting for a window of returns. A DTS-based forecast reacts at once, while an EWMA forecast needs weeks of realized moves to catch up. The second half, that P&L has no strong relationship to volatility, is the part credit tests hardest. In credit, high volatility arrives with high spreads, and high spreads arrive with high expected returns (carry and the risk premium). Cutting risk when volatility rises therefore also cuts exposure to the periods with the highest subsequent returns, the post-crisis rebounds. That is the trade a restructuring banker knows from the other side: you bought the fallen angels in 2009 from people whose risk models told them to sell. The 2026 desk keeps volatility targeting for the trend sleeve, because trend needs it, and refuses to apply the same scaling mechanically to its carry sleeve (§10.4), where it would sell the premium at the wides.

### 10.3.2 The stop-loss that was already a trend rule

Ben Dor's group made the same point with a risk limit instead of a signal. Suppose the maximum DTS contribution from any issuer is 3.0, and you hold 0.5% of the portfolio in a bond at 100 bp with a duration of 5 years, a contribution of $100 \times 5 \times 0.5\% = 2.5$. If the spread widens past 120 bp, the limit forces a sale (Ben_Dor_Quantitative_Credit_Portfolio_Management p.291). Nobody in the risk meeting called it a trend strategy.

> **[SOURCE EXTRACTION]** *Ben_Dor_Quantitative_Credit_Portfolio_Management p.292:* "Generally, a momentum strategy like this one does well in trending markets and poorly in choppy markets. If enough market participants adopt this approach, it could lead to destabilizing behavior in which spread widening and asset sales reinforce each other in a vicious cycle."
>
> **Annotation.** This is the earliest shelf statement of trend crowding in cash credit, and it was written about risk limits, not hedge funds. Two lessons carry into 2026. First, the payoff description is exact. Hard DTS limits, rating-triggered sales, and vol-targeted trend sleeves all share the convex-in-trends, concave-in-chop profile that §10.6 derives formally. Second, the "vicious cycle" is a statement about market structure, not about any one book. When many holders run the same rule, their sales are the price move that triggers the next round of sales. In index CDS the cycle is damped, because dealers quote two-way all day and the instrument has no maturity wall or ratings cliff. In cash HY it is not damped, because the same bonds are held by mutual funds facing redemptions, insurers facing capital charges, and CLOs facing CCC buckets. The surrounding pages draw the conclusion explicitly for fallen angels: forced sellers sell too low, and patient holders recoup the loss. The modern desk runs trend in the index, where its selling does not move the price much, and keeps a patient, non-trend sleeve ready to buy what other people's limits force onto the market.

> **Desk Myth vs. Desk Reality.** *Myth:* A credit trend follower has a view on spreads. *Reality:* A good half of its P&L is a view on volatility, and credit volatility is spread times duration, so the position is sized by the very thing it is forecasting. Kaz, at the whiteboard: "Let's just assume Gaussian." The entire desk: "No." Spread changes are heteroskedastic by construction ($\sigma \propto s$), fat-tailed through jumps, and stale in cash. Gaussian i.i.d. returns are the one assumption under which the timing term does nothing.

> **Ways This Blows Up.** *Stale volatility, oversized position.* A cash-bond excess-return series built from evaluated prices understates realized volatility, because pricing services smooth. An EWMA on smoothed returns therefore says risk is low, and the inverse-vol weight makes the position too large, exactly in the least liquid part of the book. The same smoothing appears as positive autocorrelation, which a trend signal reads as a trend (§10.5.3 makes the artifact explicit). *Lagging volatility in a gap.* In April 2025, HY OAS moved from 3.42% on 2 April to 4.61% on 7 April (FRED, `BAMLH0A0HYM2`). A 60-day EWMA had about three new observations. A DTS forecast had the new spread on day one. *The guard:* forecast volatility as $\hat\sigma_t = \max\big(\hat\sigma^{\text{EWMA}}_t,\ \hat\beta^{\text{DTS}}\,\text{DTS}_t,\ \sigma_{\text{floor}}\big)$, and cap leverage. The max rule responds to whichever warning arrives first.

**Estimating $\beta^{\text{DTS}}$.** Regress a rolling realized volatility of spread changes on the spread level *through the origin*, as the source extraction instructs:

$$
\hat\beta^{\text{DTS}} = \frac{\sum_t \hat\sigma^{\Delta s}_t\, s_t}{\sum_t s_t^2}.
$$

Use non-overlapping windows when you want honest standard errors, and estimate by rating bucket, because the "constant" is constant only within a bucket and a regime.

## 10.4 Trend Plus Carry: Two Coefficients, No Tribes

There are two tribes in credit. The carry-and-value tribe buys after spreads widen, because the spread is wider and spreads mean revert. The trend tribe sells after spreads widen, because they are widening. Each can point to a decade that vindicates it. The systematic desk does not join a tribe. It writes down a model in which both effects exist and lets the data size each one.

### 10.4.1 The derivation

Let spreads follow a mean-reverting process with inertia, under $\mathbb{P}$:

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

The mean-variance position follows directly. With risk aversion $\gamma$ and $\operatorname{Var}_t(r^{ex}_{t+1}) = (D^{\text{spr}})^2(\beta^{\text{DTS}})^2 s_t^2\,\Delta t$,

$$
w^{*}_t = \frac{\mathbb{E}_t[r^{ex}_{t+1}]}{\gamma\,\operatorname{Var}_t(r^{ex}_{t+1})}
= \frac{1}{\gamma (\beta^{\text{DTS}})^2 D^{\text{spr}}}
\left[\frac{1}{D^{\text{spr}} s_t} + \frac{\kappa\,(s_t - \bar s)}{s_t^2\,\Delta t} - \frac{\phi\,\Delta s_t}{s_t^2\,\Delta t}\right].
$$

The carry term in the bracket decays like $1/s_t$, so mean-variance carry *also* de-risks as spreads widen, more gently than trend does. The value term is bounded: as $s_t\to\infty$ it behaves like $\kappa/(s_t\Delta t)$, so even a value investor stops adding in a true blowout. The trend term is a z-score of last period's spread change, scaled by the current level. Nothing in the formula picks a tribe; $\kappa$ and $\phi$ do.

### 10.4.2 Why you cannot estimate your way out of the argument

Estimate the model by regressing $\Delta s_{t+1}$ on a constant, $s_t$, and $\Delta s_t$. Then $\hat\kappa = -\hat b_{s}$, $\hat\phi = \hat b_{\Delta s}$, and $\hat{\bar s} = \hat a/\hat\kappa$. Now count the data. Twenty-five years of monthly OAS is 300 observations of a persistent series. The least-squares estimate of $\kappa$ is biased upward in small samples (the Kendall–Stambaugh bias of persistent regressors), and its standard error is of the same order as the coefficient. The estimate of $\phi$ is better behaved but swings by regime. The honest output is a *confidence region* for $(\kappa, \phi)$, not a point, and the honest strategy is a blend whose weights do not move much as you move around that region. Section 10.10's code estimates both on an expanding window, so the backtest never uses a coefficient it could not have known.

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

Momentum in cash bonds themselves is a weaker and more contested object. Jostova, Nikolova, Philipov, and Stahel (2013) report a momentum spread of 59 bp a month across all bonds over 1991–2011, 192 bp a month in non-investment-grade bonds, and almost nothing in IG, where Gebhardt, Hvidkjaer, and Swaminathan (2005) find reversal rather than continuation. Then came the audits. Dickerson, Robotti, and Rossetti (2026), *The Corporate Bond Factor Replication Crisis*, re-run the 6-month momentum factor on TRACE for August 2002–December 2024 and find that its 0.30% monthly premium is "entirely attributable to asymmetric ex-post winsorization": the base premium is 0.00%, and the 12-month version is −0.13% a month. Chapter 7 covers how a filter can manufacture a factor. Here the lesson is narrower: **trend in credit should be traded in instruments whose returns you can trust (indices, CDS) and signaled from markets that price information first (equity).** Bond-price momentum in the cross-section is the least trustworthy of the three.

### 10.5.2 Equity Momentum in Credit, from the shelf

The most complete practitioner implementation is the Barclays QPS "Equity Momentum in Credit" (EMC) signal in Dynkin and coauthors' *Systematic Investing in Credit*. Bonds of index constituents are sorted monthly by their issuer's trailing equity return. Over December 1992 to May 2017 the quintile long-short earns 6.34% a year with an information ratio of 1.56 in US IG, positive in both halves of the sample, and the effect is far stronger in high yield (about 15.9% a year before costs, Dynkin_Systematic_Investing_in_Credit pp.608–609). Sector elasticity is clean: each additional 1% a month of equity momentum adds "an extra 5 to 8bp of bond excess returns" (Dynkin_Systematic_Investing_in_Credit p.644). The construction uses several horizons at once, for the reason §10.2.2 gave. The signal is built to confirm itself: "combining momentum signals at different horizons helps to validate (confirm) trends in stock prices" (Dynkin_Systematic_Investing_in_Credit p.607). In our notation, with equity total returns $r^{\text{eq}}$,

$$
\text{EMC}_{i,t} = \frac{1}{3}\sum_{h\in\{1,3,6\}} \frac{M^{\text{eq},(h)}_{i,t}}{\sqrt{h}},
$$

where dividing by $\sqrt h$ is our default way to put the horizons on a common volatility scale. The book says only that the returns are "rescaled for different lengths of the respective formation periods," and does not give the exact rescaling, so treat $\sqrt h$ as a specification choice and say so in the spec.

> **[SOURCE EXTRACTION]** *Dynkin_Systematic_Investing_in_Credit p.610:* "an issuer with equity momentum in the top 10% (D10) has only a 17% probability of remaining top ranked after three months"
>
> **Annotation.** An equity momentum signal has the half-life of an ad hoc group: by the time counsel is retained, the top decile has left the building. The sentence continues with the complement, an 83% chance of leaving the top decile within three months. For a trend desk this is a cost statement before it is a signal statement. A cross-sectional EMC portfolio that holds only the top decile turns over constantly; the same book reports top-decile long-only turnover of about 73% a month and returns that turn negative after transaction costs (Dynkin_Systematic_Investing_in_Credit p.692). The modern desk uses three responses. It applies the signal at index or sector level, where turnover is cheap and sector timing earned 2.38% a year in US IG, 4.04% in US HY, and 1.77% in Euro IG over 2007–2017 before costs (p.647). It uses buffered entry and exit thresholds, buying at the 80th percentile and selling below the 50th instead of trading every rank change. And it treats a single-name EMC signal as a *veto or tilt* on a position held for other reasons, not as a reason to trade on its own.

### 10.5.3 The lead–lag regression, and the stale-mark artifact

The test is a two-equation VAR with Granger restrictions:

$$
r^{\text{cr}}_{t+1} = \pi_0 + \pi_{\text{eq}}\, r^{\text{eq}}_{t} + \pi_{\text{cr}}\, r^{\text{cr}}_{t} + \varepsilon_{t+1},
$$

and "equity Granger-causes credit" means rejecting $\pi_{\text{eq}} = 0$. Before you celebrate a rejection, derive what staleness alone produces.

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

Equity "leads" the bond mark with a coefficient of about $p(1-p)\beta^{\text{ce}}$ even though nothing leads anything. The artifact disappears at $p=1$ (always fresh) and at $p=0$ (never prints, no returns at all), and it peaks at $p = \tfrac12$: a bond that prints every other week. That is not an unusual bond. Section 10.10 simulates exactly this case and asserts that the fake lead is statistically significant on the marks and absent on the true prices.

Dynkin's team runs the right defenses, testing the signal with one- to three-day lags and conditioning on measures of how efficiently each bond trades (Dynkin_Systematic_Investing_in_Credit pp.621, 630). At index level the artifact is much smaller, because CDX prints hundreds of times a day. That is one more reason the cross-asset trend sleeve uses equity signals to trade *indices*.

### 10.5.4 Total versus residual equity momentum, and the turning-point risk

There is a subtler problem. Sorting bonds on total equity return loads on time-varying default risk: after an equity sell-off, the losers are the high-beta, high-leverage names, so a long-winners, short-losers credit book is short credit beta at the bottom. Dynkin's book shows the symptom, "the strategy net spread tends to decline and become negative during equity down‐cycles" (Dynkin_Systematic_Investing_in_Credit p.613).

> **[SOURCE EXTRACTION]** *Dynkin_Systematic_Investing_in_Credit p.631:* "Haesen et al. (2017) argued that this varying exposure can make the strategy vulnerable in periods of market turning points, for example when a market downturn is followed by a recovery."
>
> **Annotation.** Haesen, Houweling, and van Zundert (2017) propose sorting on *residual*, firm-specific equity momentum, which roughly halves the default-risk exposure, doubles the Sharpe ratio, and cuts the bear-to-bull drawdowns in their 1994–2013 sample. Dynkin's team reports a different result in their own data, and the honest desk puts both on the page instead of picking the convenient one. The disagreement is informative. Residualizing helps when the turning point is a sharp V and the losers' rebound is a beta rebound, as in 2009 (§10.7). It helps less when the cycle is slow and the losers really are deteriorating credits. The 2026 desk's practice is to residualize the equity signal against the market and sector, report the credit-beta exposure of the long-short book every day, and size the beta separately. It is the same rule as Chapter 8's "IDO or it didn't happen": a lead–lag alpha whose credit beta flips sign over the cycle is mostly market timing until you strip the beta.

> **[SOURCE EXTRACTION]** *Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.25:* "We generally find trends to be consistent across a capital structure and indeed across broader groups/ecosystems as well; these trends therefore tend to be less issue-specific and more at an issuer-level."
>
> **Annotation.** This is the practitioner's justification for the whole section. If trends live at the issuer level, the best place to observe an issuer's trend is the security that prices it fastest, which is almost always the equity and occasionally the CDS. The bond is the last to know. For the ex-RSSG reader the sentence also has a capital-structure reading: the senior secured loan, the unsecured notes, and the stock of a deteriorating issuer move together until the moment they do not, which is the liability-management event. An LMT is exactly the case where the trend is *not* consistent across the capital structure, because value is being moved from one class to another. Section 10.9 takes this up. A cross-asset trend engine needs an explicit flag for "the capital structure has stopped moving together," and the Priming Risk Score of Chapter 13 is that flag.

Pitkäjärvi, Suominen, and Vaittinen (2020), *Cross-asset signals and time series momentum*, give the template for doing this across asset classes. In 20 countries, past bond returns predict equity returns positively, past equity returns predict government bond returns negatively, and a cross-asset TSMOM strategy has a Sharpe ratio about 45% higher than the standard one. They attribute it to slow-moving capital. For credit, the natural cross-asset signal for CDX HY is the trailing return of the equity market, or better the equity of the index constituents, combined with credit's own trend, with each sleeve's weight estimated as in §10.4.

## 10.6 Crisis Alpha and the Shape of the Payoff

Mags has heard the phrase "crisis alpha" from every trend manager who ever visited the desk. "They say it the way bankers say 'synergies.' It's real about a third of the time, and they'd like to be paid for all of it." The useful question is *which* crises, and the answer comes from the shape of the payoff.

### 10.6.1 Trend is a straddle, and the smile is the receipt for momentum

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

a parabola. For large moves, $2\Phi(\cdot)-1 \to \operatorname{sign}(r_{t+1})$ and the payoff tends to $|r_{t+1}|$, which is a straddle. The quadratic coefficient is positive *if and only if* $\rho > 0$. Convexity is not a separate property of trend; it is the receipt for momentum. If the market does not trend, the smile is flat. This is the formal version of Fung and Hsieh's reading of trend followers as holders of lookback straddles (Fung and Hsieh 2001, *The Risk in Hedge Fund Strategies: Theory and Evidence from Trend Followers*), and of Hamill, Rattray, and van Hemert's finding that trend returns are positively skewed and straddle-like.

The empirical test is the regression

$$
r^{\text{TF}}_{t} = b_0 + b_1\, r^{\text{HY}}_{t} + b_2\, \big(r^{\text{HY}}_{t}\big)^2 + u_t, \qquad b_2 > 0 \ \text{is the smile},
$$

with Newey–West standard errors. Run it at the horizon where $\rho$ lives: quarterly or semiannual non-overlapping returns for a 12-month signal. A daily fit finds nothing, because day-to-day the correlation between a 12-month trailing return and tomorrow's return is close to zero. Kaz ran it daily first and announced that trend was not convex. Ines asked him to run it on quarters. He did, and has not mentioned it since.

**The credit twist.** Long credit is short a put on firm assets (Chapter 5's Merton model). The market return $r^{\text{HY}}$ has a positive drift (carry) and a fat left tail (defaults, gaps). A straddle on a negatively skewed asset earns most of its payoff on the left: the short-credit leg of trend is long that put, and it pays in the slow sell-offs where the put goes deep into the money over several months. The same asymmetry explains the losses. The rebound after a credit crash is a short-covering of that put, steep and fast, and a trend follower who is short is short the steepest part of the recovery. Daniel and Moskowitz (2016), *Momentum Crashes*, document the equity version: momentum crashes in panic states, after declines and at high volatility, when the losers rebound. Barroso and Santa-Clara (2015), *Momentum Has Its Moments*, show that managing momentum's own risk "virtually eliminates crashes and nearly doubles" its Sharpe ratio. In credit both effects show up most strongly in high yield, where the put is closest to the money.

### 10.6.2 Whipsaw arithmetic: why trend cannot trade a V

The straddle needs the move to last long enough for the signal to notice. Make that precise with a stylized V. The credit excess-return index falls linearly by $d$ over $T/2$ months, then recovers linearly by $d$ over the next $T/2$. A trend follower reacts with effective lag $L < T/2$: it is long until $L$, short from $L$ to $T/2 + L$, and long again afterward. It enters long, as it would after a quiet tightening (February 2020 and February 2025 both qualify). Add up the four legs, with slope $d/(T/2)$ on each:

$$
\text{P\&L} = \frac{d}{T/2}\Big[\underbrace{-L}_{\text{long, falling}} + \underbrace{(T/2 - L)}_{\text{short, falling}} \underbrace{-\,L}_{\text{short, rising}} + \underbrace{(T/2 - L)}_{\text{long, rising}}\Big]
= \frac{2d\,(T - 4L)}{T}.
$$

The total available move is $2d$ (down $d$, up $d$), so the capture ratio is $(T-4L)/T$. It is negative whenever $L > T/4$. For a trailing-sum signal of length $h$ after a prior trend of similar slope, $L \approx h/2$, so a 12-month signal ($L \approx 6$ months) needs a V lasting more than about two years to break even, and a 3-month signal ($L\approx 1.5$) needs one longer than six months. March 2020 and April 2025 had $T \approx 2$ months, which no reasonable lookback beats. The 2007–2009 widening and recovery took closer to two years. Plug in $T = 20$: a 3-month signal captures $(20-6)/20 = 70\%$ of the round trip, and a 12-month signal loses $(20 - 24)/20 = -20\%$ of it *(stylized; real Vs are asymmetric and the lag depends on the preceding slope)*. Speed is a parameter, not a personality. Section 10.10 verifies the formula on a grid.

### 10.6.3 Is credit trend just beta?

The AQR team's out-of-sample test of trend in alternative markets, Babu, Levine, Ooi, Pedersen, and Stamelos (2020), *Trends Everywhere*, includes five CDS indices (CDX NA IG from October 2003, CDX NA HY from March 2004, iTraxx Europe and Crossover from June 2004, and an EM index from March 2004), with annualized volatilities of only 3.9–5.5%. Across all alternative assets, 12-month TSMOM earned a gross Sharpe of 1.34. Credit, however, was the weakest group once passive beta was removed. Regressed on an equal-volatility passive long portfolio, 12-month credit TSMOM had an annualized alpha of 4.4% with a *t*-statistic of 0.49, a beta of 0.52 (*t* = 8.84), and an $R^2$ of 33%, the highest of any group. Fidelity's decomposition of SG Trend Index returns (data to December 2025) finds that about 76% of a simple trend strategy's risk is beta timing, and puts the index's correlation with the S&P 500 at −0.11 unconditionally and −0.31 in down months.

The desk motto applies without modification. Trend is beta that changed its mind, and it is still beta. Strip it before you call it alpha. In credit there is a structural reason the stripping removes so much. The carry hurdle (§10.1.2) keeps the 12-month signal long through most of the cycle, so a large share of credit TSMOM's return is the credit risk premium, collected while spreads drift tighter. The genuine trend component is the 10–20% of months in which the signal is short, which is why it matters so much whether those months are slow sell-offs or sharp Vs.

Hurst, Ooi, and Pedersen (2017), *A Century of Evidence on Trend-Following Investing*, give the long-run base rate. Across 67 markets from 1880 to 2016, TSMOM was profitable in every decade and positive in 8 of the 10 worst drawdowns of a 60/40 portfolio, which lasted about 15 months peak to trough on average, long enough for trend to flip short. It struggled in abrupt crashes such as October 1987. For credit, this is the whipsaw arithmetic stated as history.

> **Trend Watch: CTAs, speed, and crowding, 2024–2026.** CTAs, in SG's phrase, "showcase a level of adaptability akin to the Kardashians," and the last two years tested it. *The drawdown:* the SG Trend Index fell 4.9% in April 2025 and was down 9.3% for the year to that point (SG Prime Services, *CTA Industry Update*, May 2025). Its 12-month return to 30 April 2025 was −18.6%, a level it had breached only twice before (Man Group, *Trend Following and Drawdowns: Is This Time Different?*). AlphaSimplex dates the peak-to-trough drawdown at −21.8% from 15 April 2024 to 14 May 2025 (Kaminski and Wen, June 2025), and Cambridge Associates calls it the second-largest since 2000. *The recovery:* for full-year 2025, SG Trend returned +2.39% against +17.89% for the S&P 500 total return, according to Top Traders Unplugged's compilation (23 January 2026). In 2026 trend made money during the Middle East energy shock, +10.13% year to date by end-April while HY OAS peaked at only 3.46% on 30 March (FRED), and stood at +11.07% year to date at end-August (Top Traders Unplugged; secondary figures, check against SG Prime Services). *The crowding:* in July 2026 the SG Trend Index lost 1.12%, and the same compiler noted that "the programs were largely positioned the same way," so breadth across programs gave little protection. SG put the 2024 pairwise correlation of index constituents at 0.78, and Man reports that correlation was 0.87 before 2007. *The speed:* SG finds that since 2007 the index "behaves more like a much slower model," while faster models "delivered the best hypothetical returns" in 2020. Man finds that adding alternative markets, "such as power, synthetic credit indices and interest rate swaps," improved performance, more so for slower systems. *Scale:* SG cites industry AUM of about \$340bn (BarclayHedge, Q4 2024). Man AHL reports \$39.4bn of trend-following AUM across "900+ traditional and alternative markets" as of 30 June 2026. *What it means for the desk:* the 2025 drawdown was not a credit event. Credit indices are a small, slow sleeve in CTA books, and HY OAS has spent 2024–2026 in a tight band (2.59–4.61%), with few trends long enough to pass the carry hurdle. The credit trend sleeve's job in this regime is to be cheap, small, and ready for the next slow sell-off, not to earn its keep in a market that keeps snapping back.

## 10.7 Case Studies: 2008, 2020, 2022, and the April 2025 Coda

All four episodes are told the same way: what trend did, what it should have been measured against, and what a 2026 systematic desk would have flagged. Spread levels before October 2023 come from secondary sources or Dynkin's tables, are marked approximate, and should be checked against the full ICE BofA history, which the §10.10 code reads from a local CSV.

### Case Study A: 2007–2009, the trend that paid and the rebound that charged

*What trend did.* The SG Trend Index returned +20.9% in 2008 while MSCI ACWI fell 42.2% (Cambridge Associates, August 2025). Man's Robertson (2023) puts the BTOP50 at +17% from July 2007 to February 2009. Man AHL's Evolution programme got its credit exposure by selling protection on CDX and iTraxx, was short credit during 2008, and states that it had "no hard-wired long credit bias" (*The Hedge Fund Journal*, 2013). The equity-to-credit signal did what §10.5 predicts.

> **[SOURCE EXTRACTION]** *Dynkin_Systematic_Investing_in_Credit p.617:* "While the corporate index has average returns of –8.07%/yr in drawdown episodes and 4.12%/yr in recovery times, the EMC strategy performed well in both regimes: 11.53%/yr in credit drawdowns and 4.30%/yr in recoveries."
>
> **Annotation.** This is the strongest shelf evidence that an equity-signaled credit strategy is a crisis hedge rather than a crisis amplifier, and it explains why the systematic desk prefers to get its credit trend from the equity market. Two caveats keep it honest. First, these are averages over several down-cycles in IG, gross of costs, for a long-short issuer-selection strategy. They are not the return of a short-index trend sleeve, and they do not survive the top-decile turnover of §10.5.2 without buffering. Second, the recovery number (4.30% against 4.12%) is the interesting one: the strategy did not give back its drawdown gains in recoveries *on average*. The averages hide the specific turning point that hurts, 2009, when the losers rebounded fastest. The 2026 desk reads this page as a case for equity-signaled credit trend with residualized beta (§10.5.4), not as a promise that every recovery is free.

*The venue.* Trend in CDX was a very different trade from trend in cash. Dynkin's tables put the 2008 average CDX HY spread at 788 bp against 899 bp for the HY cash index, and 950 bp against 991 bp in 2009 (Dynkin_Systematic_Investing_in_Credit pp.215–216). The cash–CDS basis went deeply negative, then "reverted back toward zero as the crisis abated" (Ben_Dor_Quantitative_Credit_Portfolio_Management p.390).

> **[SOURCE EXTRACTION]** *Ben_Dor_Quantitative_Credit_Portfolio_Management p.388:* "However, during the crisis, spreads of cash bonds widened by much more than CDS due to liquidity effects."
>
> **Annotation.** For a trend follower this sentence decides which instrument to trade. A cash-bond trend sleeve in 2008 got short late, because its marks were stale, and then covered into a market where the bid had vanished, so it paid the liquidity widening twice, once in the mark and once in the exit. An index sleeve was short the cleaner instrument, and its liquidity improved relative to cash as the crisis deepened. The modern lesson generalizes: in credit, the trend signal and the trend vehicle should be chosen separately. You can signal from cash excess returns, equity, or both, but you execute in the instrument whose liquidity survives the move you are betting on. The basis is also its own signal. A cash–CDS basis that is very negative and starting to close is a $\kappa$-flag for §10.4: the forced selling is ending, and the trend sleeve's short is about to meet the patient buyers of §10.3.2.

*The rebound.* Then came 2009. AlphaSimplex dates a "GFC Recovery" drawdown in the SG Trend Index of −11.3% starting 9 March 2009, the day of the equity market low.

> **[SOURCE EXTRACTION]** *Paleologo_Advanced_Portfolio_Management p.77:* "During 2008, Momentum experienced higher volatility but did not lose money (see Figure 5.9). However, in 2009 the stocks that had experienced large losses in the previous year rallied as the market rebounded."
>
> **Annotation.** Paleologo's account is about cross-sectional equity momentum, but the mechanism transfers exactly to credit trend, and it is worse in credit. The 2008 losers were the highest-spread, highest-beta credits, the ones closest to Merton's default boundary. When the market turned, their equity rallied like deep out-of-the-money calls coming back to life, and their bonds and CDS followed. A trend book short the index was short that convexity at the moment it exploded. The systematic desk's defense is not to predict the turn. It is to let the faster information source turn first: the equity market bottomed on 9 March 2009, so an equity-to-credit signal flipped weeks before credit's own 12-month signal did. A second defense is the $\kappa$ term of §10.4, which by early 2009 was telling every blended book that spreads were extremely wide of any long-run level. The restructuring reader knows the rest of the story from the other side: early 2009 was when par-recovery bonds were bought at 40 from sellers whose models said "trend."

*What the 2026 desk would have flagged.* Three-month and 12-month credit signals short CDX HY by late 2007, with notional falling as DTS rose: a widening from about 600 bp to about 1,800 bp *(approx.)* cuts notional by two-thirds at constant risk. Equity-to-credit signal leading both into the trough and out of it. Basis and $\kappa$ flags arguing for a smaller short from late 2008. Lesson: trend was right for twenty months and wrong for the two that cost the most. The exit rule is the strategy.

### Case Study B: February–June 2020, the V that trend could not trade

*What happened.* Spreads went from post-crisis tights to a late-March peak (ICE BofA HY OAS roughly 1,100 bp around 23 March 2020, *approx.; check against the full series*) and most of the way back by June. On 23 March the Federal Reserve announced its corporate credit facilities, which is the cleanest $\kappa$ shock in the history of the index. Index CDS activity in Q1 2020 ran 78.1% above its trailing average (ISDA). HY bid–ask spreads gapped wider in February–March and then normalized (Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.20). The BTOP50 lost 2% over February–March 2020 (Robertson 2023), SG Trend "did not contribute positively" during COVID (Fidelity), and SG Trend ended 2020 up 6.24% (Hedgeweek, January 2021). SG notes that faster models did best that year.

*Why.* The whipsaw arithmetic of §10.6.2 with $T \approx 2$ months. Any lag over two weeks loses money on the round trip, and the only trend that paid was fast. Fast trend is ruinous in cash credit, where bid–ask had gapped, and affordable in CDX, which dealers kept quoting at record volume. A long-protection trend position is not an open market purchase of anyone's bonds. It is a bet that the dealers who quote CDX IG hundreds of times a day keep doing so. In March 2020 they did, and the cash market did not.

> **The Spec You Hand the Robot (vague version).** Theo, early in his first month: "Follow the trend and don't get whipsawed." *What ROBO built:* a strategy with a 36-month lookback and a 200 bp dead band that traded twice in 18 years and was long protection on CDX HY at full risk on 24 March 2020, the morning after the Fed announcement. It was never whipsawed. It simply arrived after every trend had ended. Speed is a parameter with units, and "don't get whipsawed" is an objective that the cash-in-a-drawer strategy satisfies perfectly.

*What the 2026 desk would have flagged.* A fast sleeve (20/120-day crossover on CDX, cheap to trade) flipping short in late February. A slow sleeve flipping short near the wides, which is the expensive moment. A blended forecast (§10.4) whose value term by late March outweighed the trend term, so the blend was cutting the short as the slow signal was adding to it. An index-versus-cash execution rule that kept the whole sleeve out of cash bonds. Lesson: in a $\kappa$-week, the trend sleeve's job is to be small, and the blend makes it small without anyone having to forecast the Fed.

### Case Study C: 2022, trend's best year was mostly duration

*What happened.* The SG Trend Index returned +27.4% in 2022 while MSCI ACWI fell 18.4% (Cambridge Associates). The gains came mainly from short bond and rate trends, long US dollar, and energy (Hedgeweek, January 2023). Credit was not a named driver. HY OAS widened to roughly 600 bp in early July 2022 *(approx.; check against the full series)* and then partly recovered. Inside the record year, AlphaSimplex dates a "Fed Inflation Fight Reversal" drawdown of −10.1% from 14 June to 10 August 2022. Index CDS trading set a then-record \$36.4tn (ISDA).

*Why it matters for credit.* A trend follower trading cash HY ETFs in 2022 got two trends at once: a duration trend (rates up) and a spread trend (spreads wider). CDX isolates the spread trend, and it was a much smaller one. Desks that reported "credit trend made money in 2022" from cash total returns were mostly reporting a rates trade. Strip the duration with the Chapter 8 machinery before awarding credit any credit. The spread move was also the kind that the carry hurdle filters. A widening of a few hundred basis points over a year clears the HY hurdle of about 110 bp, so the 12-month return signal went short. The summer rally then charged the trend sleeve, which is the whipsaw at the 2-month horizon inside a year that was convex at the 9-month horizon.

*What the 2026 desk would have flagged.* A credit trend sleeve reported on spread excess returns, separate from any rates trend. A 3-month signal giving back part of its gain in July–August. A 12-month signal holding the short through the summer at moderate cost. Lesson: convexity and whipsaw happen in the same year at different horizons, which is the argument for a multi-horizon ensemble with weights fixed in advance.

### Coda: April 2025, "Liberation Day" (FRED-verified spreads)

The spread path is clean and verified. ICE BofA US HY OAS was 2.62% on 18 February 2025, 3.42% on 2 April, 4.01% on 3 April, and 4.61% on 7 April, the high for the year, before easing to 4.37% on 9 April. It was back near 3.1% by mid-May and at 2.96% on 30 June. IG OAS peaked at 1.21% on 9 April (FRED `BAMLH0A0HYM2`, `BAMLC0A0CM`). HY moved 119 bp in three sessions and completed the round trip inside about six weeks. In the same window the SG Trend Index lost 4.9% in April (SG Prime Services). Man reports that trend repositioned after the 2 April shock and was positive by 9 April, and index CDS activity in Q2 2025 ran 20.9% above its trailing average while single-name activity fell 20.7% (ISDA).

These sources should be read together, not as a verdict. A gap of this kind is not tradable by trend in advance: no signal built from returns before 2 April could know about a policy announcement. A 3-month credit signal would have flipped short within days, after the gap, and then faced a six-week V. The whipsaw formula with $T \approx 1.5$ months says the round trip was a loss for any lag longer than about ten days. Index trend sleeves that were *small* in April 2025, because the 2024–2025 spread range gave the vol-targeted, carry-hurdled signal little to do, lost little. The lesson for the 2026 desk is about expectations, not engineering. Trend does not hedge gaps. It hedges the slow sell-off that sometimes follows a gap, and in April 2025 none followed.

## 10.8 Turnover, Costs, and Capacity

### 10.8.1 How often does a sign flip?

Under the null of no trend, a sign strategy still trades, and that turnover sets the cost floor. Let returns be i.i.d. with variance $\sigma^2$, and let $M^{(h)}_t$ be the trailing $h$-period sum. Consecutive sums share $h-1$ terms, so

$$
\operatorname{Cov}\big(M^{(h)}_t, M^{(h)}_{t+1}\big) = (h-1)\,\sigma^2,
\qquad
\rho_h \equiv \operatorname{Corr}\big(M^{(h)}_t, M^{(h)}_{t+1}\big) = \frac{h-1}{h}.
$$

For a bivariate normal pair with correlation $\rho$, Sheppard's formula gives $\mathbb{P}(\text{signs differ}) = \arccos(\rho)/\pi$. Each flip of a unit position trades two units, so annual turnover of the pure sign strategy, with $n$ periods per year, is

$$
\text{TO}_h = 2\,n\,\frac{\arccos\!\big((h-1)/h\big)}{\pi} \;\approx\; \frac{2n}{\pi}\sqrt{\frac{2}{h}} \quad (h \text{ large}).
$$

For a monthly 12-month signal, $\arccos(11/12)/\pi \approx 0.131$, which is about 1.6 flips and 3.1 units of turnover a year. A 1-month signal flips half the time, about 12 units a year. A daily 20-day signal has $\arccos(0.95)/\pi \approx 0.101$, about 25 flips and 51 units a year. Real trends reduce these numbers, because persistence makes flips rarer. Volatility scaling adds turnover, because the weight moves even when the sign does not. Section 10.10 checks the formula by simulation.

> **[SOURCE EXTRACTION]** *Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.19:* "Within classic quant, Momentum tends to have the highest turnover of any factor approach while both Size and Quality see the least churn."
>
> **Annotation.** The sentence sits inside a paragraph whose real subject is that the higher a strategy's turnover, the more its results depend on the accuracy of modelled transaction costs and on the availability of liquidity. Trend is momentum's time-series cousin and shares the problem, with one important difference. Cross-sectional momentum in cash bonds pays the cash bid–ask on every rank change, and §10.5.2 showed that this is enough to make top-decile EMC negative after costs. Time-series trend in index CDS trades a few units a year in the most liquid credit instrument there is. The modern desk therefore treats "momentum is expensive" as true for the cash cross-section and mostly false for the index time series, and it specifies costs per instrument and per regime rather than as one number for the whole strategy. A cost model fitted to 2019's calm bid–ask will understate the cost of the trades a trend sleeve actually makes, which cluster in the weeks when bid–ask has gapped.

### 10.8.2 Break-even arithmetic

Let $c^{\text{tr}}$ be the cost per unit of notional traded, roughly the half bid–offer in spread times the risky annuity. The annual cost drag is $c^{\text{tr}}\times\text{TO}$. Illustrative magnitudes *(illustrative; replace with your own execution data)*: for CDX IG with a half bid–offer of 0.25 bp and $\text{RPV01} \approx 4.5$, $c^{\text{tr}} \approx 1.1$ bp of notional, so a 12-month sign strategy pays about $3.1 \times 1.1 \approx 3.5$ bp a year. For a cash IG bond with a half bid–offer of about an eighth of a point, $c^{\text{tr}} \approx 12.5$ bp, so the same strategy pays about 39 bp a year. A top-decile cash EMC book turning over 73% a month (about 8.8 units a year) pays about 110 bp a year, which is the arithmetic behind the negative net return of §10.5.2. On costs, trend lives in the index and dies in cash.

The documented index market supports the low-cost case. The CFTC's study of the Bloomberg SEF from May 2014 to September 2016 found average daily CDX IG volume of \$7.05bn across 108 trades, with a price impact for CDX HY trades above \$500mm of about 0.3 bp, about 0.5% of the spread (Haynes and McPhail, CFTC Office of the Chief Economist, 2017). By 2025, ISDA's figures imply roughly \$67bn a day of CDX IG activity on average (our arithmetic: 43.4% of \$39.0tn over about 252 trading days). The caveat comes from Collin-Dufresne, Junge, and Trolle (2020), *Market Structure and Transaction Costs of Index CDSs*. The market remains two-tiered: client trades are large, infrequent, and informed, and dealers price-discriminate on expected impact.

Ines replays the trend sleeve's April 2025 entry through markouts, as she replays every hand. "Look at the hand history. Every CTA's 20/120 crossover flipped within the same two days. The dealers knew you'd call before you did, because you told them in your marketing deck. Predictable flow pays the spread twice: once in the quote, and once in the move the dealer makes before quoting you." The defenses are mechanical. Spread execution randomly over a window instead of trading at the close the signal flips. Keep the roll (where 25–50% of quarterly notional trades) out of the signal calendar. Route large clips through futures blocks where the listed market is deep enough (§10.1's Trend Watch). Measure all of it the same way the market-making desk does, with markouts at 5, 30, and 120 minutes.

**Capacity** follows from turnover. A 12-month trend sleeve trading 3 units a year at \$5bn of gross index notional *(illustrative)* trades about \$15bn a year, a few hours of CDX IG volume. Capacity binds in HY, in Crossover around the roll, and in any cash implementation. It does not bind for a desk-sized index sleeve.

## 10.9 Trend in the LMT Era: Jumps, Not Diffusions

Everything so far has treated spread changes as diffusions with level-dependent volatility. That is a good model of an index of 100 or 125 names. It is a bad model of a single issuer with a 2027 maturity wall, a cooperative ad hoc group, and a sponsor whose counsel has just discovered the phrase "open market purchase," still the most expensive three words in finance.

Theo saw this before Kaz did. "If the loan drops twelve points on an uptier, the trend signal flips short the next morning. That's when Mags buys."

"That's when I buy the *excluded* tranche at a price that already assumes I lose the lawsuit," Mags said. "Your robot sells it to me because it went down. Back in my day the sellers at least had the decency to have a reason."

### 10.9.1 The jump-diffusion correction to vol scaling

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
