## Z.09 Chapter 9: Factor Investing in Corporate Credit

Seven exercises. Every number below was recomputed in Python; the lab exercise was run on the Appendix F listings with the extension described in its solution.

### Z.09.1: Kaz's hedge, two ways

**Answer:** (a) Dollar-neutral beta $= (12 - 7.2)/8 = 0.6$. DTS-neutral short notional $= 100 \times 12/7.2 = \$166.7$mm per \$100mm long. (b) Net carry $= 3.0\% \times \$100\text{mm} - 0.9\% \times \$166.7\text{mm} = \$3.0\text{mm} - \$1.5\text{mm} = +\$1.5$mm a year, or 150bp on the long notional. You have built a short-duration (low-risk) factor, not a value or carry factor.

**How:** Beta is a ratio of DTS numbers, (9.1), so the dollar-neutral book's beta is the DTS gap over market DTS. Matching DTS means scaling the short leg by $12/7.2 = 1.667$. For carry, use (9.4): per unit of DTS, carry is $1/D^{\text{spr}}$. Both legs carry the same DTS, 12, so

$$
\text{net carry} = \text{DTS}^{\ast}\left(\frac{1}{D^{\text{spr}}_L} - \frac{1}{D^{\text{spr}}_S}\right) = 12\left(\frac14 - \frac18\right) = 1.5\%.
$$

The spreads cancel, and only the durations survive. In §9.2.3 the carry was zero because the legs had the same duration. Here the long leg is a 4-year bond and the short leg is an 8-year bond, so the 1.5% is what the market pays you for being short the long end of the credit curve. The book has no beta to the index, but it is a duration bet: it gains when long-dated spreads widen more than short-dated ones and loses when they tighten more.

**The trap:** One common wrong answer is 2.1% ($3.0\% - 0.9\%$), which is the carry of equal dollars and forgets the short leg's 1.667 scaling. The other is 0%, copied from §9.2.3 without noticing that the durations now differ. A third mistake is calling the 1.5% "value" or "carry alpha". By (9.4) it is the duration premium, and the box after (9.4) says to rename it before compliance does.

**If you got this wrong, read:** §9.2.2–§9.2.3 for the beta and the scaling, and §9.5.1 for (9.4) and why carry turns into a duration factor.

### Z.09.2: Can you afford it?

**Answer:** Break-even round-trip cost $c^\ast = (3.0\%/12)/0.40 = 0.625\%$. **Investment grade: it survives, barely.** The cost is $0.40 \times 0.608\% \times 12 = 2.92\%$ a year, which leaves +0.08% (8bp) net. **High yield: it fails.** The cost is $0.40 \times 0.941\% \times 12 = 4.52\%$ a year, which leaves −1.52% net. The high-yield turnover cap is $\text{TO}^\ast = (3.0\%/12)/0.941\% = 26.6\%$ a month. At that cap the cost equals the full 3.0% gross, so a buffer has to cut turnover by a third **without giving up any gross return** just to break even. More generally, the buffer can give up at most 11.3bp of annual gross return for each point of monthly turnover it removes.

**How:** Use (9.3), $\mathbb{E}[r^{\text{net}}] = \mathbb{E}[r^{\text{gross}}] - \text{TO}\cdot c$, with $\text{TO}$ the one-way monthly turnover and $c$ the round-trip cost. A liquidity cost score is a round-trip cost (§9.8.2), so it goes straight into $c$. Put everything in monthly units: gross is $3.0\%/12 = 0.25\%$ a month. The IG bill is $0.40 \times 0.608\% = 0.243\%$, so IG clears by 0.007% a month. The HY bill is 0.376%, so HY falls short by 0.126%. Invert (9.3) for the cap: $\text{TO}^\ast = 0.25\%/0.941\% = 26.6\%$. A buffer that trades turnover for gross return keeps the strategy alive only while

$$
G(\text{TO}) \;>\; 12 \times 0.941\% \times \text{TO} = 11.3\% \times \text{TO}.
$$

Barclays' buffers cost roughly a seventh of the gross IR (1.52 to 1.31, §9.8.3). Take 3.0% down by a seventh to about 2.6%, and the turnover has to fall to about 23% a month, not 26.6%.

**The trap:** One mistake is treating the LCS as a one-way cost and charging $2 \times \text{TO} \times \text{LCS}$. That gives an IG cost of 5.8% a year and the wrong verdict, "neither". The other is comparing the 3.0% annual gross with the 0.24% monthly bill and declaring victory in both markets. Also, do not read the IG result as comfortable. Eight basis points a year is well inside the error in any cost model, and it disappears in any month when costs rise above their average (§9.8.3, Trend Watch).

**If you got this wrong, read:** §9.4.2 for (9.3) and the taxi-meter box, §9.8.2 for what an LCS measures, and §9.8.3 for buffers.

### Z.09.3: The measure trap

**Answer:** $\text{PD}^{\mathbb{Q}}_3 = 3.54\%$, so the fair spread **with** the $\mathbb{P}\to\mathbb{Q}$ step is **72bp** (71.6). **Without** it, the fair spread is **20bp** (20.1). At 65bp the bond is **not cheap**: it is about 7bp rich. A desk that skipped the step sees it as **45bp cheap**, and every other bond looks cheap to that desk too.

**How:** Turn the physical PD into a distance, shift it by $\theta\sqrt{T}$, and turn it back, following (9.2):

$$
N^{-1}(0.01) = -2.326, \qquad \theta\sqrt{T} = 0.3\sqrt3 = 0.520, \qquad \text{PD}^{\mathbb{Q}}_3 = N(-1.807) = 3.54\%.
$$

Then apply the recovery-of-Treasury fair spread from the derivation in §9.3.3:

$$
s^{\text{fair}} = -\tfrac13 \ln(1 - 0.0354 \times 0.6) = 71.6\text{bp}, \qquad s^{\text{fair}}_{\mathbb{P}} = -\tfrac13 \ln(1 - 0.01 \times 0.6) = 20.1\text{bp}.
$$

The market spread is a $\mathbb{Q}$ price, so it has to be compared with the $\mathbb{Q}$ fair spread: $65 - 72 = -7$bp. The 52bp gap between the two fair spreads is the credit risk premium. The desk that skipped the step counts it as alpha.

**The trap:** "65 is more than 20, buy." That is the measure trap itself. It shows every bond cheap by roughly the risk premium, so the desk ends up buying the index (§9.3.3). The quieter mistakes are using $\theta T$ instead of $\theta\sqrt{T}$, which gives a shift of 0.9, $\text{PD}^{\mathbb{Q}} = 7.7\%$ and a fair spread of 157bp, and forgetting to multiply by the 0.6 loss.

**If you got this wrong, read:** §9.3.3, both the gloss before (9.2), which works the same steps at 1% and four years, and the full derivation. Then read Chapter 6, §6.3, for why $\mathbb{Q}$ shades the odds toward default.

### Z.09.4: ROBO literalism

**Answer:** Here are three literal builds that satisfy the sentence and lose money.

1. *"Cheap" read as "wide".* ROBO buys the widest-spread decile and shorts the tightest, dollar-neutral. That is the cold-open book: a beta of 0.6 and carry on borrowed beta (§9.2.2). The long leg is also where the next defaults sit, and in the lab 19% of ESP's cheapest decile carries the hidden priming risk, against 5% of the universe (Listing 9.3 output). The book loses in the first selloff.
2. *The Treasury build.* ROBO reads "cheap" as a low dollar price, "avoid momentum crashes" as "hold nothing whose spread can gap", and "keep costs low" as "trade the asset with the lowest LCS" (Treasuries, 0.028%, §9.8.3 Trend Watch). It fills the book with deep-discount, low-coupon long Treasuries. All three clauses are satisfied, and the result is a long-duration rates book inside a credit mandate. In a 2022-style year (the Aggregate fell over 13%, §9.5.3) it loses double digits. The quieter version parks residual weight in bills and runs an unhedged duration gap nobody wrote down.
3. *The crash rule that is itself the crash.* ROBO "avoids momentum crashes" with a stop-loss that liquidates the sleeve after a drawdown and buys back after the rebound. It "keeps costs low" by pricing every trade at last year's average LCS. That is two round trips at stressed prices in exactly the month when immediacy is most expensive (March 2020, §9.10), plus the missed recovery.

**How:** Each failure comes from a word without a unit, a time stamp or a boundary. Here is the rewrite (§9.2.3 and §9.12 hold the full versions):

1. *Universe:* index corporates at the start of month $t$. Bonds above 1,000bp OAS leave DTS scaling and are sized on price and recovery. Residual weight sits in Treasuries matched to the benchmark's key-rate durations, never bills, and returns are excess returns over duration-matched Treasuries.
2. *Cheap:* the ESP residual of log OAS (OAS, never Z-spread) on rating × sector × maturity intercepts and three ratios lagged at least 3 months. Cells under 30 bonds pool with the adjacent rating, residuals are winsorized at 1/99, and negative EBITDA is set to 15× before the 0.1× floor. The signal uses a start-of-month composite mid, and returns use executable levels or a one-month skip.
3. *Momentum and crashes:* EMC over 1, 3 and 6 months, with no stop-loss. Crash protection is structural: DTS-neutral legs at 12 (years × %) per leg in each rating × sector cell, from start-of-month DTS, re-neutralized whenever a leg's DTS drifts more than 10% from target.
4. *Costs:* one-way cost $c_i = \text{LCS}_i/2$ from today's LCS, scaled up for non-standard tickets. One-way turnover $\tfrac12\sum_i|\Delta w_i| \le 10\%$ a month, entry at the 90th percentile and exit below the 80th, with no ticket below the desk minimum.
5. *Acceptance:* report gross, cost, net, turnover and beta, with $|\beta| < 0.10$. Anything unspecified: stop and ask.

**The trap:** The usual failure is a rewrite that only adds adjectives ("truly cheap", "low-cost execution"). A spec is fixed only when every noun has a unit (years × %, decimal OAS, fraction of value), every number has a time stamp (start of month, lagged a quarter), and every rule has an edge case (thin cells, distressed names, defaults). Being "more careful" is not a fix.

**If you got this wrong, read:** the Spec You Hand the Robot box in §9.2.3 (ROBO's two-year Treasuries), the 2022 replay in §9.5.3 (the bills), the March 2020 replay in §9.10, and the full spec in §9.12.

### Z.09.5: Extend the lab

**Answer:** The signal built from bond prices is the one the noise moves, by roughly sixty times as much as the equity-data signal. With the independent errors of Listing 9.7, though, the noise moves it **down**, not up. In my run (lab noise of 0.4% for IG and 1.2% for HY, DTS-neutral deciles) bond momentum went from +0.05% a year ($t = 0.2$) on clean prices to −5.4% a year ($t = -17.6$) on noisy ones, a gap of −46bp a month. The equity-short-interest signal went from 2.71% to 2.80% a year, a gap of +0.7bp a month, with $t$ unchanged at 6.3. The pure Blume–Stambaugh level term ($\sigma_u^2$, at most 1.4bp a month here) is the only bias ESI carries. It is tiny, and it nets to near zero across legs for both signals.

**How:** This builds on Listing 9.7, with signals in the style of Listing 9.3 and the Listing 9.2 engine. I planted the ESI link in `simulate` by adding $+0.01\,w_{j,t-1}$ to the issuer residual, with $w$ drawn from its own seed. I observed ESI at the start of month $t$ as $0.02 + 0.01\,\text{rating} + 0.01\,w_{j,t} + \text{noise}$ and traded it z-scored within rating, short the high-SI names. Bond momentum is the sum of the last six months' returns, computed from the same price series (clean or noisy) on which it is graded. On noisy prices the six-month sum telescopes:

$$
\textstyle\sum_{k=0}^{5}\tilde r_{t-k} \;\approx\; \sum_{k=0}^{5} r_{t-k} \;+\; u_t - u_{t-6}, \qquad \tilde r_{t+1} \;\approx\; r_{t+1} + u_{t+1} - u_t ,
$$

so the latest mark error enters the signal with a plus sign and the next return with a minus sign. By §9.9's Mechanism 2 that contributes $-\sigma_u^2$ to the covariance: the "winners" are partly bonds marked too high, and they give the error back. Skip a month and the shared price disappears (gap +0.3bp a month). ESI comes from the equity market, so its errors are independent of the bond marks. Noise in the returns then adds variance but no covariance with the signal, and the only bias left is the $\sigma_u^2$ level term weighted by how differently noisy the two legs are.

**The trap:** "Bond momentum is inflated, because noise makes everything look better." Under independent errors the shared price makes momentum look *worse*, the mirror image of how it manufactures short-term reversal. A second trap is calling ESI immune. Its returns are still measured on bond marks, and when I made the marks stale instead of noisy (not updated with probability 0.2 in IG and 0.5 in HY), ESI's gross fell from 2.71% to 1.78% a year. Stale marks book the planted widening after the position has rotated out. Bond momentum fell further still, to −6.6% a year.

NOTE (for the editor): the exercise asks which signal the Blume–Stambaugh mechanism "inflates" more. On the chapter's own noise model (Listing 9.7, iid errors), my run of the extension moves bond momentum by −46bp a month (−5.4% a year against +0.05% clean) and ESI by +0.7bp a month. The noise deflates the bond-price signal, as the $-\sigma_u^2$ covariance of §9.9 predicts for a buy-winners sort. Consider "distort" for "inflate", or ask the reader to predict the sign first.

**If you got this wrong, read:** §9.9, Mechanisms 1 and 2 and the Full Derivation, then §9.11 on Listing 9.7, including its paragraph on why stale marks are not cleared by a one-month skip.

### Z.09.6: First-day declaration

**Answer:** A declaration the Ad Hoc Group of Replicators cannot pick apart has three sections, and each claim in it carries a number or a test.

1. *Cause of distress.* (i) Timing. Two of the four published factor series led returns by a month and a third lagged, and an after-the-fact filter capped losses. The paper was retracted in December 2023 (§9.9; Chapter 7). (ii) Noisy month-end marks. Each mark adds $\sigma_u^2$ to average returns, which is 9bp a month (about 1.1% a year) at $\sigma_u = 3\%$, by (9.6). Signals and returns that share a price also manufacture reversal and "value" from the mark error alone. (iii) Filters that peek and defaults that vanish, which remove exactly the left tail that value and carry portfolios hold. (iv) False discovery. Only 23% of significant literature factors keep a significant alpha in a clean framework (Dick-Nielsen, Feldhütter, Pedersen and Stolborg), and 25 of the 26 survivors of the 2026 audit are within-firm sorts.
2. *DIP financing (the clean data).* Open Bond Asset Pricing's cleaned TRACE panels, its corrected Bai–Bali–Wen factors and its duration-matched Treasury returns, pinned to a release (v4.2.1). Point-in-time fundamentals stamped with `available_at` and lagged at least a quarter. Composite mids for signals, and executable levels (or a skip month) for returns.
3. *Plan of reorganization (the five rules).* Signal and return never share a price. No ex-post filters: cleaning rules are written before any return is seen, and outliers are reviewed by a person. Defaults stay in: recovery minus last price in the default month, and the bond leaves the panel the next month, never retroactively. Double-sort on DTS or rating. Replicate in CI: the four corrected factors are rebuilt nightly to four decimals, and every candidate passes the placebo (in the lab, a lag-one reversal must show $t > 5$ and its skip-month twin a $t$ near zero).

**How:** Write it the way a first-day declaration is written. Each cause names a mechanism and its size. The financing names a source, a version and a timing convention. Each plan provision is paired with the cause it cures: rule 1 cures (ii), rule 2 cures (i) and (iii), rule 3 cures (iii), rule 4 cures the cold open's beta, and rule 5 makes the whole plan auditable. One page is enough if every sentence carries a number or a test.

**The trap:** "Data quality issues were identified and have been remediated" is the answer the Group objects to, and it will win. A vague cause cannot be matched to a cure. The second trap is declaring the whole estate worthless. The survivors (equity-derived signals, value on clean prices with DTS control, and low-risk) are the reorganized company, and the plan should name them.

**If you got this wrong, read:** §9.9, Mechanisms 1–3 and the red build with Kaz's whiteboard, then Chapter 7, §7.11, for the retraction itself.

### Z.09.7: The second x-ray

**Answer:** (a) Without value, $\text{BR}_{\text{eff}} = 12/(1 + 11 \times 0.25) = 3.2$. With value, $12/(1 + 11 \times 0.15) = 4.5$. (b) Idio share $= 1 - 0.6^2 - 0.20 = 0.44$. (c) Borrow costs $\$300\text{mm} \times 1.00\% = \$3.0$mm a year. Rebalancing costs $2 \times \$300\text{mm} \times 5\% \times 0.8\% \times 12 = \$2.9$mm a year. That is **\$5.9mm a year** to give away a \$4mm premium, so the hedge loses. **Shrink** the pairs where value is incidental, and **admit** the ones whose thesis is cheapness. For the hedge to win, the cheap quintile's borrow fee would have to fall below about **37bp**, roughly what the rich, liquid shorts cost (§9.7.2), or someone would have to list an instrument that is mostly value.

**How:** Treating the twelve pairs as one issuer-like cluster, §9.7.2's formula has $N = \bar n = 12$, and naming value buys about 1.3 extra hats. For (b), a loading on unit-volatility series is a correlation, so its variance share is the square: $0.6^2 = 0.36$. Then $1 - 0.36 - 0.20 = 0.44$. For (c), use the chapter's turnover convention. One-way turnover of 5% means selling 5% and buying 5% of each side, so each side pays $5\% \times$ the round trip ($2 \times 0.4\% = 0.8\%$) a month, as in (9.3) and in Wen's own pricing in the scene. The break-even fee comes from

$$
300 \times f + 2.88 = 4.0 \quad\Longrightarrow\quad f = 0.37\%.
$$

Even at a zero fee, the rebalancing alone eats 72% of the premium.

**The trap:** In (b), using the loading without squaring it gives $1 - 0.6 - 0.2 = 0.2$. In (a), dividing by $1 + \bar\rho$ or keeping twelve hats. In (c), charging the 0.4% once on the 5% gives \$1.44mm of rebalancing, \$4.44mm all-in and a break-even fee of 85bp. The verdict survives that reading, but it understates the bill by half. The bigger mistake is reading "hedge" as free because value turns over slowly. The bill is the borrow, because the short leg is the cheapest quintile, the wide, thin end of every cell that nobody lends cheaply.

**If you got this wrong, read:** §9.7.2, "The Pair Book: One View, Twelve Times" (Wen's pricing of the hedge, and the shrink and admit doors), then Chapter 8-D, §8D.2, for why the fee climbs toward the bonds you most want to short.

<!-- STATUS: COMPLETE -->
