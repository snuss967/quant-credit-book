## Z.15 Chapter 15: Event-Driven M&A, Regulatory Spreads & Change-of-Control

Five exercises: one on the EA defeasance, one on the SMR gauge going blind, one on a regression design, one on the WBD ticking fee and one on Kaz's bell curve. Every number below was recomputed, from the chapter's Blocks 1 and 3 (Appendix F, Listings 15.1 and 15.3) where an exercise uses them and from the chapter's own inputs otherwise. Where we had to assume an input, the solution says so and labels it illustrative. Write your answer down before you read ours.

**Z.15.1: The defeasance arithmetic**

**Answer:** We price on Listing 15.1's illustrative Treasury curve, whose zero rates are 4.39% at 4.5 years and 4.49% at 24.5 years, plus a flat 350bp LBO spread. The post-close prices are 77.0 for the 1.85% 2031s and 45.3 for the 2.95% 2051s, so if the put triggers at close it is worth **24.0 points and 55.7 points**. At signing, with Block 1's check-(1) inputs ($\pi_d = 0.85$, $\pi_{\text{trig}\mid d} = 0.9$, close in nine months, $B = 0.970$), the put is worth **17.8 and 41.3 points**. With check (3)'s lognormal spread and logistic ratings leg it is worth 15.6 and 35.4 ($M \approx 1.05$). Turn on the `defeasance_prob` callable and both go to 0.00.

Defeasance costs the sponsor the scheduled cash flows at Treasury flat, **89.6 and 76.8** per 100, so it **saves 11.4 and 24.2 points** against 101. On the \$681mm and \$742mm left outstanding after the tender, that is about **\$258mm**, which matches Fancourt's "over \$250mm".

The 95% who stayed were not wrong. The 2051s' tender at about 74 sat within a few points of the defeased value: 76.8 at a 4.49% long zero, 70.5 at a flat 5%, with break-even at a flat 4.70%. So tendering versus holding was a quarter-point bet on long Treasury yields, not a call on credit. Holding also kept the slim chance that the sponsor would pay 101 after all. And an insurer is glad to own Treasury-backed duration. Only 9.2% of the 2031s and 1.1% of the 2051s were tendered, 5.1% of the \$1.5bn. The holders who lost were the ones who paid 90 for a 101 that a defeasance article had already knocked out.

**How:** This is Step 3 of §15.2.2. Price the bond for the life left after close on the post-close curve,

$$
P^{\text{post}} = \sum_i \tfrac{c}{2}\,e^{-(y^{\text{TSY}}_{t_i}+s^{\text{post}})t_i} + 100\,e^{-(y^{\text{TSY}}_{T}+s^{\text{post}})T},
$$

take $(101 - P^{\text{post}})^{+}$, and multiply by $\pi_d\,\pi_{\text{trig}\mid d}\,B$ for the signing value. A constant spread makes $M = 1$. In Block 1 these are `price_coc_put` calls with `maturity_years` of 5.25 and 25.25 and `t_close = 0.75`. The sponsor's alternative is a deposit that pays every scheduled cash flow, so it costs the same sum at a zero spread:

$$
D = P(s=0), \qquad \text{saving} = 101 - D .
$$

Multiply by the face still outstanding to get dollars. Then read the same arithmetic from the holder's seat. Compared with being paid 101, the holder loses $101 - D$. Compared with being left as unsecured LBO paper, the holder gains $D - P^{\text{post}}$, which is 12.6 and 31.5 points, because the deposit replaces the sponsor's credit with the Treasury's. For the tender, set 74 against $D$ at whatever long yield you expect on the settlement date, and solve $D(y) = 74$ for the break-even.

**The trap:** Saying the sponsor saves the put, 24 and 56 points. That discounts the defeased bond at the LBO spread, but a box of Treasuries is priced at Treasury yields. The put's value is $101 - P^{\text{post}}$, the sponsor's saving is $101 - D$, and the gap between them, $D - P^{\text{post}}$, is what the holder keeps. A close second is "defeasance pays in full, so the saving is one point". In full means the scheduled payments, and on a 2.95% coupon in a 4.5% world those are worth 77, not 100.

**If you got this wrong, read:** §15.2.2 Steps 3–4 for the post-close price and the coupon-vintage table, then cuts two and three of the EA case study in §15.2. PB-10 in the same section turns the two defeased values into a hedge ratio.

**Z.15.2: The blind thermometer**

**Answer:** The two legs meet after a **parallel rally of about 38bp from issue**. Take a three-year 4.60% tranche issued at par (4.60% bond-equivalent, a 4.548% continuous yield) with the ruling a quarter away. The legs meet when the close leg's yield has fallen to 4.21%, and both are then worth 101.09. At issue the ruler is not zero. It is 1.00 point long, 100.00 against 100.99, because the fail leg carries the one-point premium plus accrued. Each basis point of rally shortens it by about 0.026 points, the gap between the two legs' dollar durations (roughly 2.8 years against 0.25, on about 101). Measured from the worked example's marks instead (close leg at 99.00, $y_f = 4.60\%$), the blind spot is a **77bp** rally away. On Listing 15.1's Nelson–Siegel curve with a flat 23bp issuer spread, it is 42bp.

At the blind spot, $\hat\pi_f$ is undefined: the tranche is worth $P^{\text{close}}$ whatever $\pi_f$ is, so its price cannot tell you $\pi_f$. Within about 4bp of that point, a 0.10-point price error moves $\hat\pi_f$ by 100 percentage points or more. Even 20bp away the same error moves it by about 20 points.

Use another instrument whose ruler is long. The first choice is a **sibling SMR tranche of the same deal with a different duration**, which has the same issuer, the same deal and the same $\mathbb{Q}$. At this rate move, a seven-year 4.90% SMR tranche issued at par has a ruler of +1.16 points: its sign has flipped, but it still carries information. Failing that, use the target's equity merger-arbitrage spread, and name its contaminants: the takeover premium, the standalone value and borrow costs. A §15.5 hazard model is not a substitute, because it is a $\mathbb{P}$ number and the gauge is a $\mathbb{Q}$ number.

**How:** Under (B1)–(B2), a parallel Treasury move $\Delta$ shifts both legs' yields:

$$
P^{\text{close}}(\Delta) = \sum_i \tfrac{c}{2}\,e^{-(y+\Delta)t_i} + 100\,e^{-(y+\Delta)T},
\qquad
G_f(\Delta) = \big(101 + 1.15\big)\,e^{-(y_f+\Delta)T_f},
$$

with $\text{AI}_{T_f} = 4.60 \times 0.25 = 1.15$ and no coupon before $T_f = 0.25$. Solve $P^{\text{close}}(\Delta) = G_f(\Delta)$ by root-finding. The linear version gets you within a basis point:

$$
\Delta^{*} \approx -\frac{G_f - P^{\text{close}}}{P^{\text{close}}D^{\text{close}} - G_f T_f} \approx -\frac{0.995}{258} \approx -39\text{bp}.
$$

Why undefined: $\partial P_0/\partial\pi_f = G_f - P^{\text{close}} = 0$ there, so every $\pi_f$ gives the same price and the mixture cannot be inverted. Near that point the inversion is a ratio of two small, noisy numbers, and a price error $\delta P$ becomes $\delta\hat\pi_f = \delta P/|P^{\text{close}} - G_f|$. To hold a 0.10-point error to 10 percentage points you need a 1-point ruler, which means about 38bp of distance from the blind spot. That is the case at issue, and almost nowhere else nearby.

**The trap:** "Zero: the gauge goes blind when rates are back where they were at issue, because the bond is at par." At par the close leg is 100 and the fail leg is about 101, so the gauge reads perfectly well. The holder only turns short the digital once a rally has lifted the close leg above 101 plus the carry difference. The second trap is to clip, or report 0.5, at the blind spot. Clipping a ratio of two noises produces a confident number. The honest output is "no information".

**If you got this wrong, read:** §15.4.2, the ruler box and "The sign flips with rates", then "Reading the gauge" for Ines's three-cent ruler, and the paragraph on Listing 15.3's `tol` guard.

**Z.15.3: The vintage anomaly**

**Answer:** The coupon coefficient is **positive** below the break-even coupon and **zero above it**. Low-coupon bonds trade *tight*, not cheap: with the put in the price, a higher coupon means a wider Z-spread,

$$
\frac{\partial z^{\text{obs}}}{\partial c} \;\approx\; \frac{\pi_d\,\pi_{\text{trig}\mid d}\,B\,M\,A(s^{\text{post}})}{P\,D_s} \;>\; 0 \quad (c < c^{*}), \qquad 0 \quad (c > c^{*}).
$$

To size it, take illustrative 5.25-year bonds (4.5 years left after a close nine months out) at a 150bp pre-deal Z-spread, with 350bp post-close, $\pi_{\text{trig}\mid d} = 0.9$, $B = 0.970$, $A = 3.72$ and $M = 1$. The slope is about **8bp of Z-spread per point of coupon at $\pi_d = 0.10$, 20bp at 0.25 and 38bp at 0.5**, and it goes flat beyond $c^{*} \approx 8.3\%$. At $\pi_d = 0.10$ the 1.85% bond trades 41bp inside the 6.875% bond, and at 0.25 it trades 100bp inside.

The test that separates the put from convexity and index eligibility uses issuer-by-date fixed effects and an interaction of coupon with the deal-and-trigger probability. The put lives in the interaction, in its kink at $c^{*}$ and in its jumps on deal-news dates. Convexity and index eligibility live in the plain coupon slope and in bond characteristics that do not change when the news arrives.

**How:** The put adds $V_{\text{CoC}}(c)$ to the price, and the Z-spread inverts price, so $dz = -dP/(P\,D_s)$ and $z^{\text{obs}} \approx z^{\text{straight}} - V_{\text{CoC}}(c)/(P\,D_s)$. Step 4 of §15.2.2 gives $\partial P^{\text{post}}/\partial c = A$, so each point of coupon takes $A$ points off the intrinsic value. With $V_{\text{CoC}} \approx \pi_d\,\pi_{\text{trig}\mid d}\,B\,M\,(K - P^{\text{post}})^{+}$, that makes $\partial V/\partial c = -\pi_d\,\pi_{\text{trig}\mid d}\,B\,M\,A$ below $c^{*}$ and zero above it. The chain rule then gives the sign. Now the design:

$$
z_{ijt} = \alpha_{it} + g(T_{ij}) + \beta\,c_{ij} + \gamma\,c_{ij}\,\hat\pi_{it} + \theta' X_{ijt} + \varepsilon_{ijt}.
$$

Here $\alpha_{it}$ is an issuer-by-date effect that absorbs the credit, $g$ is the maturity control, $\hat\pi_{it}$ is the deal-times-trigger probability (watch-list and rumour flags, sponsor versus strategic bidder), and $X$ holds each bond's computed convexity, amount outstanding, index flag, age and bid–ask. The put predicts $\gamma > 0$, of roughly the size $B\,M\,A/(P\,D_s)$, while convexity and index eligibility predict $\beta \neq 0$ and $\gamma = 0$. Cluster by issuer.

Identification comes from four places:

1. **Event dates.** The slope should steepen on the announcement and collapse when a strategic IG bidder appears ($\pi_{\text{trig}\mid d} \to 0$), when the deal breaks, or when a consent strip or defeasance is signalled, as with EA in February 2026. A bond's convexity and index membership do not change on those days.
2. **Placebos.** Use same-vintage bonds of the issuer without the CoC covenant, or with it stripped (WBD after June 2025), and non-watch-list issuers whose coupons are just as spread out.
3. **Shape.** The put is a hockey stick with a kink at $c^{*}$, and convexity is smooth in $c$.
4. **Rates.** A Treasury move shifts $c^{*}$ and the slope, while index eligibility does not move with rates.

**The trap:** Predicting a *negative* coefficient because deep-discount bonds look cheap. A low dollar price is not a wide spread. The put makes the low-coupon bond rich in Z-spread terms. The second trap is running one cross-section and crediting the whole slope to the put. In a single cross-section, index eligibility (the large 2020–21 benchmarks) and convexity both have a coupon slope of their own, and the convexity one can push either way depending on whether you measure it per dollar or per 100 face. Only variation in $\pi_d$ separates the three.

**If you got this wrong, read:** §15.2.2 Step 4 (the slope $A$, the hockey stick, $c^{*}$) and the Schmid annotation after it, then "The Full Derivation" for $M$. §7-B.1 covers the fixed effects and issuer clustering.

**Z.15.4: Was the ticking fee generous?**

**Answer:** From the signing on February 27, 2026, the meter starts at $t^{*}$ = September 30, **215 days** later. Fit a Weibull with a median of seven months (213 days) and the chapter's shape of 1.6: the scale is 268 days and the mean 240. Then $\mathbb{E}[(\tau_c - t^{*})^{+}] \approx 72$ days, so the **expected ticking is about \$0.20 a share**, roughly \$0.5bn on WBD's 2.51bn shares. The realized figure was **\$0.0167** (6 days, \$41.9mm), a twelfth of that. The realized close was an ordinary draw: the Weibull puts 52% of closings on or before day 221. The \$0.20 comes from the tail. Given that the deal is late at all, it is late by 146 days on average.

The shape matters: 1.1 gives \$0.36, 2.5 gives \$0.11 and 4 gives \$0.06. The careless readings both undershoot. At the median the meter reads zero (213 < 215), and at the mean it reads 25 days, or \$0.07.

Against cash: the per diem annualizes to \$1.014, **3.27% on \$31**, below a 2026 cash yield of about 4% (Listing 15.1's illustrative three-month zero is 3.97%). Even while it runs, the meter covers only about 82% of a holder's cost of carry. It pays nothing for the 215 days before $t^{*}$ and nothing for break risk. **Not generous. Paramount Skydance wrote the better option.** It priced the meter below cash, started it at about the median closing date, and in the event paid for six days.

**How:** Count $t^{*}$ in calendar days from signing. For a Weibull, $S(t) = e^{-(t/\lambda)^{k}}$ and the median is $m = \lambda(\ln 2)^{1/k}$, so $\lambda = m/(\ln 2)^{1/k}$. The expected positive part is the area under the survival curve past the grace period:

$$
\mathbb{E}\big[(\tau_c - t^{*})^{+}\big] = \int_{t^{*}}^{\infty} S(t)\,dt, \qquad
\mathbb{E}[\text{ticking}] = 0.00277778 \times \int_{t^{*}}^{\infty} e^{-(t/\lambda)^{k}}\,dt .
$$

The \$0.25-per-90-days cap is exactly 90 times the per diem, so it never binds. For a full price, multiply by the closing probability (no close, no ticking) and discount from the close date. Both trim a few percent, leaving the answer in the high teens of cents. For the cash comparison, set the per diem against $31\,r/365$ a day. The realized figure is $6 \times 0.00277778 = 0.01666668$, which matches the \$31.01666668 closing price.

**The trap:** Reading the meter at the expected or median closing date and getting \$0.07 or zero. The meter never runs backwards, so $\mathbb{E}[(\tau_c - t^{*})^{+}] \ge (\mathbb{E}\tau_c - t^{*})^{+}$, and the gap is the right tail. The second trap is to judge the fee by the one realized draw. \$0.0167 against \$0.20 says the deal closed at about its median, not that the fee was stingy. It was stingy because 3.27% is below cash.

**If you got this wrong, read:** §15.8, the parking-meter box and "Pricing the ticking fee", then §15.5.2 for the Weibull of shape 1.6 and why deal hazards ripen. Chapter 5 owns the distribution.

**Z.15.5: Kaz assumes Gaussian**

**Answer:** FY2025 had 1,944 adjusted transactions and 41 Second Requests, which gives weights of 0.979 and 0.021. Model "cleared in the initial period" as centred at 28 days (sd 5) and "Second Request" as centred at a year (sd 120 days, Kaz's own); both are illustrative. The **best** Gaussian is the maximum-likelihood one, with mean 35 days and sd 52, and it scores −10,428 nats. The two-component mixture scores at least −6,216, so it wins by **at least 4,212 nats, about 2.2 per deal**. Three extra parameters cost about 11 nats under BIC.

The margin does not depend on the illustrative choices. With within-component sds from 2 to 10 days, Second Request means from 180 to 540 days and sds from 60 to 240, it never falls below about 1,550 nats. FY2024's counts (1,973 transactions and 59 Second Requests) give 4,490.

On clearing before filing: Kaz's $\mathcal{N}(270, 120^2)$ puts **1.2%** of deals clearing before they file and 1.05% in the first thirty days, against about 98% in the data. Fitting the Gaussian to the HSR universe makes the first number worse. The best Gaussian, mean 35 and sd 52, puts **25% of deals clearing before they file** and only 46% by day 30.

**How:** Every Gaussian is a mixture with all its weight on one component, so the best mixture cannot lose. The only question is by how much. The best Gaussian's log-likelihood depends only on the total variance:

$$
\ell_G^{*} = -\tfrac{n}{2}\big[\ln(2\pi\hat\sigma^2) + 1\big], \qquad \hat\sigma^2 = W + B,
$$

where $W = \sum_j w_j s_j^2$ is the within-group variance and $B = w_1 w_2 (m_2 - m_1)^2$ is the between-group variance. For the mixture, the density at each deal is at least that of its own component, $p(x) \ge w_j\,\mathcal{N}(x; m_j, s_j^2)$. That gives $\ell_{\text{mix}} \ge -nH(w) - \sum_j \tfrac{n_j}{2}\big[\ln(2\pi s_j^2) + 1\big]$, where $H(w) = 0.102$ nats is the entropy of the weights. Subtract, and use Jensen's inequality, $\ln W \ge \sum_j w_j \ln s_j^2$:

$$
\ell_{\text{mix}} - \ell_G^{*} \;\ge\; n\Big[\tfrac12\ln\!\Big(1 + \frac{B}{W}\Big) - H(w)\Big].
$$

The mixture wins whenever $B/W > e^{2H} - 1 = 0.23$. Here $B \approx 2{,}345$ and $W \approx 328$ days², so $B/W \approx 7.1$, and the bound alone guarantees 1,840 nats. It holds for any Second Request sd below about 700 days. The between-group term is the gap between "a month" and "a year". It inflates $\hat\sigma$, and the Gaussian pays for that on every one of the 1,903 quick clearances. The share of deals clearing before they file is $\Phi(-\mu/\sigma)$.

**The trap:** Beating Kaz's $\mathcal{N}(270, 120^2)$ and declaring victory. His bell is not the best Gaussian on HSR data, and "every Gaussian" means you must beat the maximum-likelihood one, at 35 and 52 days. The follow-on trap is assuming the better-fitted Gaussian fixes the negative-days problem. It makes it twenty times worse. A symmetric distribution fitted to a positive, skewed waiting time whose sd exceeds its mean has to put mass below zero. A third trap is crediting the win to the extra parameters: they cost about 11 nats, and the win is in the thousands.

**If you got this wrong, read:** §15.5.1 at 10:30 a.m. (Kaz's bell, and Mags on the sprinter and the marathon runner) and the HSR table above it, then §15.5.2's Cox paragraph, where the bell "belongs nowhere" because waiting times cannot be negative. Chapter 5 owns mixtures.

<!-- STATUS: COMPLETE -->
