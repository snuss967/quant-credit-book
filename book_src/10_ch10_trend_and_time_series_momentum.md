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

The most complete practitioner implementation is the Barclays QPS "Equity Momentum in Credit" (EMC) signal in Dynkin and coauthors' *Systematic Investing in Credit*. Bonds of index constituents are sorted monthly by their issuer's trailing equity return. Over December 1992 to May 2017 the quintile long-short earns 6.34% a year with an information ratio of 1.56 in US IG, positive in both halves of the sample, and the effect is far stronger in high yield (about 15.9% a year before costs, Dynkin_Systematic_Investing_in_Credit pp.608–609). Sector elasticity is clean: each additional 1% a month of equity momentum adds "an extra 5 to 8bp of bond excess returns" (Dynkin_Systematic_Investing_in_Credit p.644). The construction uses several horizons at once, for the reason §10.2.2 gave:

The signal is built to confirm itself: "combining momentum signals at different horizons helps to validate (confirm) trends in stock prices" (Dynkin_Systematic_Investing_in_Credit p.607). In our notation, with equity total returns $r^{\text{eq}}$,

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
