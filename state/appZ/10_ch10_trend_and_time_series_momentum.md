## Z.10 Chapter 10: Trend-Following & Time-Series Momentum in Credit

Five exercises. Every number below was recomputed in Python. Exercise 5 also runs Listings 10.1–10.6 (Appendix F) on ICE BofA US HY OAS from FRED (`BAMLH0A0HYM2`, the copy pulled for Chapter 8), so the stylized V can be checked against the real tape. Write your card before you read ours.

**Z.10.1: The Crossover hurdle**

**Answer:** $\Delta s^*_6 = 0.03 \times 0.5 / 4.2 = 0.00357$, so about **36 bp** (35.7 bp; 36.2 bp if you accrue a true ACT/360 half-year of 182.5 days). Over six months, iTraxx Crossover has to widen by more than about 36 bp before a 6-month return signal goes short. A smaller widening gives you a chart trending wider and a ledger trending up, and the signal reads the ledger.

**How:** One period's excess return is carry minus duration times the spread change, $r^{ex} \approx s\,\Delta t - D^{\text{spr}}\,\Delta s$. Sum it over the window and ask when the total turns negative:

$$
\Delta s^*_h = \frac{\bar s\,h\,\Delta t}{D^{\text{spr}}} = \frac{0.03 \times 0.5}{4.2} = 35.7\text{ bp}.
$$

For the PM, put a number on it. A 20 bp widening over six months costs $4.2 \times 20 = 84$ bp of mark-to-market and pays $300 \times 0.5 = 150$ bp of carry, so the six-month excess return is $+66$ bp. "Spreads are trending wider" describes the chart. "The signal is long" describes the P&L, and the P&L is still up. The two agree only once the widening passes 36 bp. Strictly, $\bar s$ is the average spread over the window. If 300 bp is where the spread started, the widening lifts the average and the hurdle to about 38 bp. If 300 bp is where it ended, the hurdle is about 34 bp. The 36 bp sits in the middle of that range.

**The trap:** Using the Crossover's 500 bp fixed coupon as the carry gives 60 bp. The carry of index CDS is the par spread, not the coupon, because the upfront amortizes the difference (§10.2.3, Step 2). The second slip is forgetting the half-year and quoting the 12-month hurdle, 71 bp. The third is answering "zero" because you thought in spread changes. That is a different strategy: in Figure 10.1, the spread-change rule is short on 150 days where the return rule is short on 13.

**If you got this wrong, read:** §10.1.2 (the landlord box and the hurdle derivation), then §10.2.3 for why the par spread is the carry.

**Z.10.2: Sheppard's turnover**

**Answer:** $\rho_3 = 2/3$. A flip happens with probability $\arccos(2/3)/\pi = 0.268$, so annual turnover is $2 \times 12 \times 0.268 = 6.43$ units, and at 1.1 bp per unit the bill is **7.1 bp a year per unit of notional**. Costs stay under a tenth of expected return when

$$
\text{SR} \;>\; \frac{10\,c^{\text{tr}}\,\text{TO}}{\sigma_{\text{unit}}} \;=\; \frac{0.71\%}{\sigma_{\text{unit}}},
$$

where $\sigma_{\text{unit}}$ is the annualized volatility of one unit of notional. The 10% target cancels out. At $|w| = 1$, which needs an instrument that already runs at 10% volatility, the bar is **SR > 0.07**. At the 3.9% volatility AQR reports for the quietest CDS indices (§10.6.3), $|w| = 2.6$, the bill is 18 bp, and the bar is **SR > 0.18**. For CDX IG in a calm year, $\sigma_{\text{unit}} \approx 0.23 \times 4.5 \times 1\% \approx 1.0\%$. Then $|w| \approx 10$, which is the leverage cap, the bill is about 68 bp, and the bar is **SR > 0.7**.

**How:** Consecutive 3-month sums share two of their three monthly returns, so $\operatorname{Cov} = 2\sigma^2$, $\operatorname{Var} = 3\sigma^2$, and $\rho_3 = 2/3$. Sheppard's formula gives $\mathbb{P}(\text{flip}) = \arccos(2/3)/\pi = 0.2677$ (a two-million-draw simulation gives 0.2678). Each flip trades two units, and there are 12 decisions a year, so $\text{TO} = 6.43$. The large-$h$ approximation gives 6.24, but $h = 3$ is not large. A sleeve at 10% volatility holds $|w| = 0.10/\sigma_{\text{unit}}$ of notional. Its cost is $7.07\text{ bp} \times |w|$, and its expected return is $\text{SR} \times 10\% = \text{SR} \times |w|\,\sigma_{\text{unit}}$. Require cost $< 0.1 \times$ expected return, and $|w|$ cancels. Two effects push every bar above higher. Volatility scaling trades between flips, because the weight moves whenever $\hat\sigma$ moves. And 1.1 bp is a calm-market cost, while trend's trades cluster in the weeks when bid–offer has gapped (§10.8.1, the annotation).

**The trap:** The tempting move is to compare 7 bp with $\text{SR} \times 10\%$ directly and conclude that any SR above 0.07 will do. That treats the 10%-volatility sleeve as if it held one unit of notional. In CDX IG it holds several units, and every one of them pays the 7 bp. The other slip is counting flips (3.2 a year) instead of units traded (6.4): a flip from $+1$ to $-1$ trades two.

**If you got this wrong, read:** §10.8.1 for Sheppard's formula and the turnover expression, §10.8.2 for the 1.1 bp and the break-even arithmetic, and §10.3.1 for why notional per unit of risk depends on spread times duration.

**Z.10.3: Kaz's runway momentum**

**Answer:** Runway momentum earns a place only if three things hold. (i) The change in the median constituent's runway carries news about CDX HY constituents' default and LMT risk that equity prices have not already absorbed. (ii) That news arrives slowly enough to be a trend at a monthly horizon, rather than a persistent level. (iii) The signal can be built point-in-time from public filings. The test is a monthly regression of next-month CDX HY excess return on the runway signal, with equity momentum, credit's own trend and carry as controls. What decides it is an expanding-window, out-of-sample forecast race against the same model without runway. **The idea dies if the out-of-sample $R^2$ relative to the equity-only model is $\le 0$, or if the Clark–West test fails to reject at 5%.** It also dies if the result disappears when the filing lag is enforced, or if it survives only in 2008 and 2020. Power check: with about 150 out-of-sample months (2014–2026), passing at $t \approx 2$ needs an incremental monthly $R^2$ near 2.6%, a timing Sharpe of about 0.57. So write the kill rule down *before* the run.

**How:** Equity is the first market to price issuer-level news (§10.5.1). The inputs to a runway (cash, revolver availability, burn) arrive in 10-Qs, and the stock reads those filings on the day they are published. So "beyond equity momentum" needs a channel equity misses. The credible candidate is jumps: a runway extension through a priming deal can lift the stock while the excluded debt gaps down (§10.9). Ines has already pointed out that a runway is a memory horizon and not a trend horizon (§10.2.1), so the signal has to be the *change* in runway. With $\widetilde{\Delta R}^{(h)}_t$ the $h$-month change in the median runway, standardized and residualized on equity momentum using only data up to $t$:

$$
r^{\text{HY}}_{t+1} = a + b_R\,\widetilde{\Delta R}^{(h)}_t + b_E\,\text{EMC}_t + b_M\,\operatorname{sign}\!\big(M^{\text{HY},(12)}_t\big) + b_s\,s_t + u_{t+1},
$$

Use non-overlapping months, roll-safe returns (§10.2.3) and HAC errors. Because nobody tries only one runway definition, ask for $t > 3$ on $b_R > 0$. Then run the race. From month 120 on an expanding window, as in Listing 10.5, fit the restricted model ($b_R = 0$) and the full model, forecast $r_{t+1}$, and compare squared errors. Point-in-time means four things: each runway is dated on its filing date, which can be up to 45 days after quarter-end; index membership is taken as of each date, defaulters included; the specification is pre-registered; and no client model enters. That is why the USB stick stays home: Theo's 13-week models are non-public client work, they cannot be reproduced, and none of them existed on the dates the backtest needs.

**The trap:** The usual mistake is to regress CDX HY on runway momentum *alone*, find a $t$ of 2.5, and declare a signal. Any measure of deteriorating liquidity will correlate with equity momentum and with credit's own trend, so the regression has rediscovered both. The second mistake is dating runways at quarter-end instead of filing date, which hands the backtest six weeks of look-ahead, the "tomorrow's newspaper" bug of §10.2.1. The third is to build the median on today's index members: the names whose runway ran out defaulted and left the series, and survivorship deletes exactly the observations the signal exists for. Finally, the median may be the wrong statistic, because index losses come from the tail of the runway distribution. If you switch to the 10th percentile after seeing the results, that is a second hypothesis, and it has to be counted.

**If you got this wrong, read:** §10.5.1 and §10.5.4 for why equity leads and why the residual is the version worth owning, §10.4.2 for estimating on an expanding window and reporting a range, §10.2.1 for the memory-versus-trend distinction, and §10.9 for the jump channel that is the idea's only real hope.

**Z.10.4: The every-other-week bond**

**Answer:** $f(p) = p(1-p)$ has $f'(p) = 1 - 2p = 0$ at $p = \tfrac12$ and $f''(p) = -2 < 0$, so the fake lead peaks there at $\beta^{\text{ce}}/4$. For a bond that prints once every five weeks, $p = 0.2$ and the lead is **$0.2 \times 0.8 \times \beta^{\text{ce}} = 0.16\,\beta^{\text{ce}}$**, which is 0.048 at the box's $\beta^{\text{ce}} = 0.3$. **Filter:** run the regression only on bond-weeks with a print at both $t$ and $t+1$. Then $m_t = P_t$, the stale gap is zero, and the fake lead goes with it. In simulation it fell from 0.048 to 0.001. A version that wastes less data uses trade-to-trade returns: regress each bond's return from one print to the next on the equity return in the week of the earlier print. That keeps every print of every bond, and its lead in simulation is 0.000. Or measure the lead on CDX, where $p \approx 1$.

**How:** The stale gap $G_t = P_t - m_t$ holds this week's equity-driven move whenever the bond did not print, which happens with probability $1-p$. Next week's print collects the gap with probability $p$. So $\operatorname{Cov}(\Delta m_{t+1}, r^{\text{eq}}_t) = p(1-p)\,\beta^{\text{ce}}\operatorname{Var}(r^{\text{eq}})$. Conditioning on $U_t = 1$ sets $G_t = 0$, which leaves $\Delta m_{t+1} = \Delta P_{t+1}$. That is independent of $r^{\text{eq}}_t$ when there is no true lead, and it keeps any lead that is real. The cost is sample size, not universe. A bond with $p = 0.2$ keeps $p^2 = 4\%$ of its weeks under the both-ends filter and $p = 20\%$ under the trade-to-trade version, but no bond is dropped. Report the lead by print-frequency bucket alongside it, as Theo did: an artifact rises as $p$ falls toward $\tfrac12$, and a real lead does not care.

NOTE (for the editor): $p(1-p)\beta^{\text{ce}}$ is the slope from a *simple* regression of $\Delta m_{t+1}$ on $r^{\text{eq}}_t$. In the VAR that §10.5.3 writes down, and that Listing 10.6(a) runs, the own lag $\Delta m_t$ is uncorrelated with $\Delta m_{t+1}$ but correlated with $r^{\text{eq}}_t$. It acts as a suppressor, and the equity coefficient becomes $p(1-p)\beta^{\text{ce}}/(1 - p^2 R^2_{\text{ce}})$, where $R^2_{\text{ce}}$ is the contemporaneous $R^2$ of true credit moves on equity. At the listing's parameters ($R^2_{\text{ce}} = 0.735$), the coefficient is 0.061 at $p = \tfrac12$, not 0.050 (simulation 0.0613), and it peaks at $p \approx 0.66$, not $\tfrac12$. At $p = 0.9$ it is 0.044 against the formula's 0.018. With the low $R^2_{\text{ce}}$ that real bonds show, the formula and the peak at $\tfrac12$ are close enough. The box might add "in a simple regression" so that a reader who checks the listing's coefficients is not surprised.

**The trap:** The tempting move is to filter on *bonds* by keeping only the names that print at least weekly. That throws away most of the HY universe, which is exactly the exercise's warning. It also biases the sample toward large, liquid issuers, so any lead you then find is a lead for a different universe. The other slip is to read $p = 0.2$ as "less stale, so less artifact" because it sits further from $\tfrac12$. In fact 0.16 is still about two-thirds of the maximum, 0.25. Infrequent printing does not save you until $p$ is near zero, and by then the bond has no returns to regress.

**If you got this wrong, read:** §10.5.3 (the wall-clock box and the four-line derivation), then Listing 10.6(a) in Appendix F, which plants the artifact at $p = \tfrac12$ and finds it at $t \approx 9.9$.

