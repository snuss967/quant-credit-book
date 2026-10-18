## Z.07 Chapter 7: Machine Learning on Small-Sample, Non-Stationary Credit Data

This chapter has six exercises, all in the end-of-chapter set, and none carries a [Read]/[Derive]/[Build] tag. I recomputed every number in Python. That includes the warm-up count in Listing 7.1, the uniqueness sum in Listing 7.4, the purge-and-embargo condition in Listing 7.5, and the $SR^\ast$, PSR and MinTRL formulas in Listing 7.6 (all in Appendix F).

**Z.07.1: Count Kaz's hats**

**Answer:** (a) In the interior, $11 \times 63 = 693$ labels are live on any given day, so $\bar u_i \approx 1/693 \approx 0.0014$. Summed over all $11 \times 1{,}197 = 13{,}167$ labels, the interior value alone gives $13{,}167/693 = 19.0$. The exact sum, which gives the less crowded labels near the two ends of the sample their higher uniqueness, is $N_{\text{eff}} = 19.98 \approx T/h = 20$, and you get exactly the same 19.98 with one bond or with eleven. (b) Yes, they stay **one group**, keyed on the ultimate parent. What the drop-down creates is a new *within-parent* target: the OpCo–HoldCo basis, meaning the priming loss to the HoldCo notes relative to the OpCo notes. Inside this one family you can validate it only across time blocks (purged and embargoed walk-forward), because there is no other parent to hold out. (c) $(\sum w)^2/\sum w^2 = 10^2/40 = $ **2.5**. Five rows, two and a half opinions.

**How:** For (a), skip the interior approximation and use the identity that makes the hat count exact. Each covered day $t$ appears in $c_t$ label windows, and each of those labels counts it at $1/c_t$, so the day contributes exactly 1 to the double sum. With every window $L = 63$ days long ($t_1 = t_0 + 62$):

$$
N_{\text{eff}} = \sum_i \bar u_i = \frac{1}{L}\sum_i \sum_{t=t_{0,i}}^{t_{1,i}} \frac{1}{c_t} = \frac{1}{L}\sum_{t\ \text{covered}} c_t \cdot \frac{1}{c_t} = \frac{1{,}197 + 62}{63} = 19.98 .
$$

The bond count $B$ drops out, because eleven sibling labels cover the same days as one. If you count the window inclusively as 64 days ($t_1 = t_0 + 63$), you get $1{,}260/64 = 19.7$, which is still $\approx T/h$. For (b), the HoldCo and OpCo notes are claims on one enterprise value and react to the same news. The unrestricted subsidiary that received the assets maps to the parent too (§7.5's Model Review Tuesday). Put the HoldCo notes in training and the OpCo notes in test, and the model reads one side's answer off the other. Model the basis as a pair label on the two legs (§7.4's pair corridor). If you later collect drop-down events across many issuers (Chapter 13), group by parent again.

**The trap:** In (a), the trap is $11 \times 20 = 220$, or the 13,167 rows. More bonds feel like more evidence, but siblings formed on the same day are one issuer's news at eleven durations. In (b), the trap is to treat the drop-down as a new credit and split the family "because the documents now separate them". The documents separate the *claims*. The *information* is still one company's. In (c), the trap is to answer 5 because "there are five rows".

**If you got this wrong, read:** §7.6, "Hats, not rows", "Uniqueness, defined" and "The hat count"; §7.7, "Group by parent, not ticker, especially in the LMT era"; §7.5, Quant-Shop Life.

**Z.07.2: Memory after a closing night**

**Answer:** (a) The weights are $(1,\ -0.4,\ -0.12,\ -0.064,\ -0.0416)$. They sum to 0.3744, so after four lags about 37% of the level is still in the feature (27% at $d = 0.5$). (b) The partial sum is $\prod_{j=1}^{K}(j-d)/j$, a product of factors that each lie in $(0,1)$. It is therefore positive for every finite $K$ and decays like $K^{-d}/\Gamma(1-d) \to 0$. (c) The embargo must be **at least 280 days** (281 by Listing 7.1's count), because $\max(h, \text{FFD window}) = \max(63, 280)$. The embargo alone removes $280/315 = 89\%$ of a block, and 22% of the sample, after every test block except the last. Add the 63-day purge that sits in front of it, and the training data lost after each test block is about 343 days, more than a whole block. At $\tau = 10^{-3}$ the window is 54 days, so $h = 63$ sets the embargo again. The cost is memory: the truncated filter keeps 13.6% of the level instead of 7.0%, the series trends more, and the smallest $d$ that passes the unit-root test tends to rise.

**How:** For (a), start at $w_0 = 1$ and apply $w_k = -w_{k-1}(d-k+1)/k$: $w_1 = -0.4$, $w_2 = 0.4(-0.6)/2 = -0.12$, $w_3 = 0.12(-1.6)/3 = -0.064$, $w_4 = 0.064(-2.6)/4 = -0.0416$. For (b), write $a_k = (-1)^k\binom{d-1}{k}$. Pascal's rule turns each weight into a difference:

$$
w_k = (-1)^k\Big[\tbinom{d-1}{k} + \tbinom{d-1}{k-1}\Big] = a_k - a_{k-1}
\quad\Longrightarrow\quad
\sum_{k=0}^{K} w_k = a_K = \prod_{j=1}^{K}\frac{j-d}{j} = \prod_{j=1}^{K}\Big(1 - \frac{d}{j}\Big).
$$

For $d \in (0,1)$ every factor lies strictly between 0 and 1, so the product is positive. Its logarithm is at most $-d\sum_{j \le K} 1/j$, which goes to $-\infty$ like $-d\ln K$, so the product goes to zero. The Gamma-function form gives the rate, $K^{-d}/\Gamma(1-d)$: at $K = 280$ that is 0.0705 against an exact 0.0705. For (c), apply the Spec's rule, embargo $\ge \max(h, \text{longest feature lookback, FFD window included})$. The warm-up solves $k^{-1.4}/3.72 = 10^{-4}$, which gives $K \approx 281$. In Listing 7.5 a training label is removed when $t_{0,j} \le T_1 + \eta$ and $t_{1,j} \ge T_0$, where $T_1$ is the last test label's *end*. That inequality removes $h + \eta$ formation days after the block. On the time axis alone, the average training share per fold falls from about 66% with the 21-day embargo to about 50% with 281 days, before parent grouping takes its fifth.

**The trap:** In (a), the trap is alternating signs ($+0.12$ for $w_2$), carried over from the binomial theorem. For $0 < d < 1$, every weight after $w_0$ is negative. In (c), the trap is keeping block 5's `embargo=21` because the label horizon is "only" 63 days. The embargo covers the longest *lookback*, not just the label. The other trap is to confuse the two costs. The 280 NaN warm-up rows are paid once per series, at the start. The embargo is paid again after every test fold.

**If you got this wrong, read:** §7.3, "Math, Gently: the dial", "The warm-up cost, computed" and "The Full Derivation: the fractional weights"; §7.7, "The embargo" and Ways This Blows Up item (2); §7.12, the paragraph after block 5 on the `embargo=21` trap.

**Z.07.3: Size Theo's hand**

**Answer:** (a) **Without the meta-model**, Theo makes **+0.10% per trade**, or **+4.0% a year** over 40 trades. **With it**, he makes 15.3 trades at **+1.30% per trade**, for **+19.9% ≈ +20% a year**, from fewer than half the trades. (b) At $p = 0.75$, $z = 0.577$ and the size is **0.44**. At $p = 0.55$, $z = 0.100$ and the size is **0.08**. A 55% read is a tenth of a standard deviation away from a coin flip, so it earns a chip, not a stack. (c) Use **purged, embargoed folds grouped by ultimate parent**, with the unrestricted subsidiaries mapped to their parents. Shuffled K-fold trains on the answer to the test flag.

**How:** For (a), the expected value per trade is precision times the win plus one minus precision times the loss: $0.35(4) - 0.65(2) = 0.10$. The meta-model keeps $0.6 \times 14 = 8.4$ of the 14 winners. At 55% precision that implies $8.4/0.55 = 15.27$ trades, of which 6.87 are losers. It has cut 74% of the losers and 40% of the winners. The year is $8.4(4) - 6.87(2) = 19.85\%$. For (b):

$$
z = \frac{p - \tfrac12}{\sqrt{p(1-p)}},\qquad m = 2\Phi(z) - 1:\qquad
p = 0.75 \Rightarrow \tfrac{0.25}{0.433} = 0.577,\ m = 0.436;\qquad
p = 0.55 \Rightarrow \tfrac{0.05}{0.497} = 0.100,\ m = 0.080 .
$$

Near $p = \tfrac12$ the map is roughly $m \approx 1.6\,(p - \tfrac12)$, so a five-point edge buys about eight points of size, not 55. In Ines's terms, the size is your confidence that you have an edge, not your opinion about the bond. For (c), flags on one parent cluster in time around one corporate event, and the drop-down entity is the same family as the parent. A shuffled split or a ticker split therefore puts the event's neighbours in training. Generate the primary's flags out of sample before you build meta-labels; that is leak (1) in §7.5's list.

**The trap:** In (a), the trap is to keep 40 trades for the meta-model and report $40 \times 1.30 = 52\%$. A filter wins by trading *less*. In (b), the trap is "55% sure, so 55% of a full position", which bets the opinion and not the confidence. In (c), the trap is ticker grouping: the unrestricted subsidiary's flags land in training while the parent's land in test.

**If you got this wrong, read:** §7.5, "The math", the Poker Table box and Ways This Blows Up; §7.7, "The purge, formally" and "Group by parent, not ticker"; §7.5, Quant-Shop Life.

**Z.07.4: Deflate the honest number**

**Answer:** (a) $SR^\ast = 0.230$ a month (0.80 annualized), and the DSR is $\Phi(0.98) = $ **0.84**. (b) With 400 effective trials, $SR^\ast = 0.193$ a month (0.67 annualized) and the DSR is $\Phi(1.49) = $ **0.93**: better, and still short of 95%. (c) The MinTRL is $T^\ast \approx$ **292 months, about 24.4 years**. TRACE dissemination has run about 291 months (July 2002 to October 2026), and Kaz has 240, so Kaz is roughly four years short. (d) The DSR corrects for selection *across* trials. An in-sample Sharpe also contains overfitting *within* the trial. Deflate only return series that are already out of sample.

**How:** Here $V = 1/240$, so $\sqrt V = 0.0645$. For $N = 3{,}000$ the quantiles are $\Phi^{-1}(1 - 1/3000) = 3.403$ and $\Phi^{-1}(1 - 1/(3000e)) = 3.667$. The bracket is $0.423(3.403) + 0.577(3.667) = 3.555$, so $SR^\ast = 0.2295$. The shape term is $1 - (-0.5)(0.30) + \tfrac{5-1}{4}(0.30)^2 = 1.24$, with square root 1.114. Then

$$
\widehat{\text{DSR}} = \Phi\!\left[\frac{(0.30 - 0.2295)\sqrt{239}}{1.114}\right] = \Phi(0.979) = 0.836 .
$$

Against zero, the same number gives $\Phi(4.17) = 0.99998$, which is the naive report. For $N = 400$ the quantiles are 2.807 and 3.115, the bracket is 2.985, and $SR^\ast = 0.1927$, so $z = 0.1073 \times 15.46/1.114 = 1.49$. A Monte Carlo of the maximum of 400 and 3,000 standard normals, scaled by $\sqrt V$, gives 0.192 and 0.229, so the formula is accurate here. For (c):

$$
T^\ast = 1 + 1.24\left(\frac{1.645}{0.30 - 0.1927}\right)^2 = 1 + 1.24 \times 235.0 = 292 .
$$

For (d), the 2.9 is annualized, or 0.84 a month. Fed into the formula, it returns a DSR of $\Phi(6.5) \approx 1.0000$. The formula happily certifies trees that memorized 47 hats. That is a haircut applied to pro forma EBITDA that already includes the synergies.

**The trap:** The commonest error in (c) is to compute the MinTRL against $SR_0 = 0$: $1 + 1.24(1.645/0.30)^2 = 38$ months, "three years and done". The benchmark that matters is the noise bar, not zero. In (a) and (b), the traps are mixing units (an annualized 0.80 bar against a monthly 0.30 Sharpe) and plugging in excess kurtosis (2) where the formula wants raw kurtosis (5). In (b), expect less than you might from clustering. Cutting $N$ by a factor of 7.5 lowers the bar by only 16%, because $SR^\ast$ grows like $\sqrt{2\ln N}$.

**If you got this wrong, read:** §7.8, "The Full Derivation: PSR, DSR, MinTRL and PBO", the Paleologo annotation on clustering trials, and Figure 7.5; §7.12, block 6 (the paragraph on handing `deflated_sharpe` only the survivors).

**Z.07.5: The composite is not a clean gap**

**Answer:** (a) $\operatorname{Cov}(\tilde r_t, \tilde r^{\text{gap}}_{t+1}) = \operatorname{Cov}(r_t, r_{t^+ \to t+1}) - \rho\,\sigma_\delta\sigma_{\delta'}$. At $\rho = 0$ the bias is zero. At $\rho = 1$ with equal variances it is $-\sigma_\delta^2$, the full Roll bias of §7.9. On Theo's whiteboard, with equal noise, the fake long–short return is $\rho \times 1.00\%$ a month, so a composite with $\rho = 0.5$ still pays half a point a month out of noise. (b) In fire sales the composite converges slowly and inherits the stale print, so **$\rho$ rises exactly when dispersion is widest and the reversal strategy trades hardest**. Enter at the first executable institutional-size print, or at a dealer level you could actually have hit, and report the premium both ways.

**How:** Write both observed returns in terms of the noise:

$$
\tilde r_t = r_t + \delta_t - \delta_{t-1},
\qquad
\tilde r^{\text{gap}}_{t+1} = r_{t^+ \to t+1} + \delta_{t+1} - \delta'_{t^+}.
$$

Expand the covariance term by term. The true returns are independent of the noise, $\delta_{t+1}$ is a fresh draw, and the composite anchors on the *last* print, not the one before it, so $\operatorname{Cov}(\delta_{t-1}, \delta'_{t^+}) = 0$. The only surviving noise term is $\operatorname{Cov}(\delta_t, -\delta'_{t^+}) = -\rho\,\sigma_\delta\sigma_{\delta'}$. For the whiteboard number, write $\delta' = \rho(\sigma_{\delta'}/\sigma_\delta)\,\delta_t + \text{fresh noise}$. Bond A, marked 0.5% low, then has an expected gap return of $+\rho(\sigma_{\delta'}/\sigma_\delta) \times 0.5\%$, and B mirrors it. A two-million-draw Monte Carlo with $\sigma_\delta = 0.5\%$ and $\sigma_{\delta'} = 0.4\%$ matches $-\rho\,\sigma_\delta\sigma_{\delta'}$ at $\rho = 0, 0.5, 0.9, 1$.

**The trap:** The trap is to believe that any price with a later timestamp is a clean gap. A gap works only when it gives a *different draw* of the noise. A composite anchored on the last print is the same draw, partly re-served. Sign slips are the second trap: $+\rho\sigma\sigma'$ would say that anchoring *hides* reversal, when in fact it manufactures it.

**If you got this wrong, read:** §7.9, Math, Gently on covariance (the mis-zeroed scale), "Latent implementation bias" and "The fix is a gap"; §7.1, "Defect 1: the price is sometimes a rumor" (the SMU Cox study and AI composites); §7.11, Case Study C; §7.10, the Trend Watch entry on Composite+.

**Z.07.6: ROBO and the future**

**Answer:** One version, in 115 words:

> Every feature value carries `available_at`: the moment the desk could first have read it (filing time, release vintage, trade-report time), never the period it describes. Join features to a label formed at $t_0$ by as-of join only: the latest value with `available_at <= t0`. Never forward-fill across a release date and never use revised vintages. Purge training label $j$ if $[t_{0,j}, t_{1,j}]$ intersects $[T_0, T_1 + \eta]$, using the recorded $t_1$. The embargo $\eta$ is at least $\max(h, \text{longest feature lookback, FFD window included})$. Fit every preprocessing parameter ($d^\star$, winsorization cutoffs, scalers) inside the training fold. CI fails the build unless pure-noise features give `auc_shuffled > auc_purged + 0.03` and `|auc_purged - 0.5| < 0.06`.

**How:** Theo's draft names an intention. ROBO needs a mechanism, and the future does not live in a column, so deleting one cannot remove it. It lives in *timestamps*, and each of the five required pieces closes one door the chapter showed being opened. The `available_at` field and the as-of join close the door that Long Scene 1's misdated factor file and Case B's FRED vintages and period-end forward-fill came through. The purge closes the one Kaz's shuffled 1.8 came through, overlapping label windows. The embargo closes the door of trailing-window features formed just after the test span. The FFD window can stretch that lookback to 280 days (Z.07.2). The canary test is behavioural: it fails on what the pipeline *does* with noise, whatever the code looks like. The bonus line, fitting $d^\star$ and the winsorization cutoffs inside the fold, catches the quieter leak of §7.3's Ways box and of Kaz's full-sample winsorization in §7.9.

**The trap:** The commonest wrong answer is a better-worded intention, such as "use only data available at the time", with no field, no join and no test. ROBO will comply with it as literally as it complied with the first draft. The second is to key the join on the date a value *describes* (quarter-end, reference month), which is exactly Case B's leverage figure sitting in the panel forty-odd days before its 10-Q existed. The third is an embargo equal to the label horizon, which forgets the feature lookback.

**If you got this wrong, read:** §7.2, Long Scene 1 and "The one-day placebo"; §7.11, Case Study B; §7.7, "The purge, formally" and "The embargo"; §7.12, block 5; §7.13, "The Spec You Hand the Robot".

<!-- STATUS: COMPLETE -->
