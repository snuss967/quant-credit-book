## Z.08 Chapter 8: Stripping Beta to Isolate Pure IDO

Seven exercises. Every number below was recomputed in Python. Exercise 1(b) uses FRED daily data (BAMLH0A2HYB against DGS10, pulled 2026-10-18), and Exercises 3–5 use the Appendix F listings on seed 8 unless stated otherwise.

**Z.08.1: Theo's thirty-seven cents, three ways**

**Answer:** The full analytical hedge is $\text{DV01} = \$40\text{mm} \times 4.1 \times 0.0001 = \$16{,}400$. One TY contract carries $\$63/0.89 = \$70.8$, so $H = 1$ is 231.7 contracts.

- **(a) Ben Dor B, 1998–2009.** $\ell = -19.25$ and $H = -0.19$. That is a *long* of about 45 TY. In practice it means zero futures, because almost no desk buys Treasuries against a B bond.
- **(b) 2026 YTD B.** The Trend Watch's $H = 1.03$ is measured at the B index's own average spread, about 305 bp, and gives 239 contracts short (Table 8.2). Re-evaluated at Theo's 620 bp, with $\rho = +0.022$, $\sigma_s = 1.92\%$ and $\sigma_y = 4.45$ bp, so $\ell \approx +0.94$, it gives $H \approx 1.06$, about 245 contracts short.
- **(c) A 2022-style regime.** $\ell = +10.3$ and $H = 1.64$, about 380 contracts short.

What each hedge assumes about why rates move:

- (a) Rates move on growth scares and Fed easing, so yields fall exactly when spreads widen.
- (b) Rates move on news this bond does not care about.
- (c) Rates move on inflation, which pushes yields up and spreads wider on the same day.

**How:** Everything goes in decimals.

$$
H = 1 + s\,\ell, \qquad \ell = \rho\,\frac{\sigma_s}{\sigma_y} = -0.56 \times \frac{0.022}{0.00064} = -19.25, \qquad H_a = 1 + 0.062 \times (-19.25) = -0.19 .
$$

Contracts are $N = H \cdot \text{DV01}_{\text{target}}/(\text{DV01}_{\text{CTD}}/\text{CF}) = 231.7\,H$. For (b), the Trend Watch gives you $\rho$ and $H$ at the index's average spread but not $\ell$. Back $\ell$ out as $(H-1)/\bar s = 0.029/0.0305 \approx 0.94$, then re-evaluate at $s = 0.062$. Because $H$ is linear in $s$, the regime's tilt away from 1 doubles when the spread doubles. For (c), $\ell = 0.3 \times 0.022/0.00064 = 10.31$.

**The trap:** The most common mistake is to read Table 8.1's B row ($-0.04$) or the Trend Watch's 1.03 as if it were Theo's bond. Both are evaluated at the index's average spread, and the caption under Table 8.2 says so. A second trap is mixing routes. Ben Dor's regression gives $\beta + \gamma s = 0.15 - 0.03 \times 6.2 = -0.04$ at 620 bp, while the two-factor formula the exercise asks for gives $-0.19$. A third is units: typing $\sigma_y = 6.4$ instead of $0.00064$ gives $\ell \approx -0.002$ and $H \approx 1$, which puts you at the "nobody" table by unit error.

**If you got this wrong, read:** §8.2, "The two-factor derivation" and "Three regimes", then the Trend Watch table; §8.6, the Veronesi extraction on futures sizing, and Table 8.2.

**Z.08.2: Kaz's fulcrum**

**Answer:** $\lambda = c/R = 0.07/0.35 = 20\%$ a year. Check: $H^{\text{rec}} = 0.07/(0.07 + 0.20 \times 0.35) = 0.07/0.14 = 0.5$. The sentence for Kaz: *the fulcrum's value is the recovery itself, a share of the reorganized company that the plan values off enterprise value and not off any Treasury curve, so for that class $\lambda$ is effectively infinite, $c/(c + \lambda R)$ goes to zero, and a ratio of one-half belongs to a bond that still collects about half its value as coupons.*

**How:** Set the ratio to one half and solve:

$$
\frac{c}{c + \lambda R} = \frac12 \;\Longrightarrow\; c + \lambda R = 2c \;\Longrightarrow\; \lambda = \frac{c}{R} .
$$

Notice that $r$ drops out. $H^{\text{rec}}$ depends only on how the bond's value flow splits between coupons and expected recovery. At $\lambda = 20\%$ (with $r = 4\%$, say) the bond is a stressed credit, not a fulcrum: $P = 0.14/0.24 = 58.3$, $y = 12\%$, a screen duration of 8.3 years against a true 4.2. Push the clock harder and the ratio falls: 0.17 at $\lambda = 100\%$ and 0.04 at $500\%$. In the limit $P \to R$ whatever $r$ is, which is "trades on dollar price."

**The trap:** One mistake is inverting to $\lambda = R/c = 500\%$. The subtler one is believing Kaz's earlier line that the ratio "goes through zero" at the fulcrum. Since $c/(c + \lambda R) > 0$ for every finite $\lambda$, the recovery route only *approaches* zero. A negative hedge ratio needs the correlation route. Calling $H = 0.5$ "half bond, half equity, so it must be the fulcrum" mixes up the bond whose value is split with the class whose whole value *is* the recovery.

**If you got this wrong, read:** §8.3, "Two routes to zero duration" and "The Full Derivation: the recovery route" (Figure 8.2).

**Z.08.3: When Scholes–Williams is enough**

**Answer:** With $\theta = (\theta_0, 1-\theta_0)$ and a serially uncorrelated factor, the three slopes converge to $b_{-1} \to 0$, $b_0 \to \theta_0\beta$ and $b_{+1} \to (1-\theta_0)\beta$, while $\rho_f \to 0$. So $\hat\beta_{\text{SW}} \to \beta$ exactly. Under $\theta = (0.5, 0.3, 0.2)$, $\hat\beta_{\text{SW}} \to 0.8\beta$: a bias of $-0.2\beta$ ($-20\%$), which is the third envelope that Scholes–Williams never opens. The code prints SW/true $= 0.810$. The extra 0.01 is sampling noise. The raw slopes are $-0.002$, $0.494$ and $0.279$, which sum to $0.771$, and dividing by $1 + 2\hat\rho_f = 0.952$ gives $0.810$. Here $\hat\rho_f = -0.024$ is sample noise, since the true value is 0. Figure 8.3's "0.52 rather than 0.49" is the same division.

**How:** Write $r^o_t = \theta_0 r_t + \theta_1 r_{t-1}$ with $r_t = \alpha + \beta f_t + \epsilon_t$. Then $\mathrm{Cov}(r^o_t, f_{t-k}) = \theta_k\beta\sigma_f^2$ for $k = 0, 1$. For the lead $k = -1$ the covariance is zero, because $f_{t+1}$ is independent of everything dated $t$ or earlier. Each univariate slope is that covariance over $\sigma_f^2$, so

$$
\hat\beta_{\text{SW}} \xrightarrow{p} \frac{0 + \theta_0\beta + (1-\theta_0)\beta}{1 + 2\cdot 0} = \beta .
$$

With a second lag the numerator becomes $(\theta_0 + \theta_1)\beta = (1 - \theta_2)\beta = 0.8\beta$. In general Scholes–Williams recovers one lag's worth of news, and Dimson with $L \ge q$ recovers all of it (1.005 in the printout).

**The trap:** Blaming the denominator. With $\rho_f = 0$ it is 1, and the whole bias is the lag the estimator never looks at. The lead term is there for a *stale factor*, so it cannot mop up a stale bond's second day. The opposite mistake is to read 0.81 as the theoretical value. The population answer is 0.80, and the printout sits 0.01 away because of a sample autocorrelation that should have been zero.

**If you got this wrong, read:** §8.5, "The Full Derivation: Scholes–Williams and Dimson under a smoothing model", and Figure 8.3.

**Z.08.4: The regime-switching robot**

**Answer:** These figures are for the listing's bond at 6% and $D = 4$.

- **Population hedge ratios.** $H = 0.20$ in the first half ($\rho = -0.4$) and $1.60$ in the second ($\rho = +0.3$). The pooled $\rho \approx -0.05$ puts the full-sample $H$ near 0.90.
- **On the listing's seed.** The regression gives 0.95 for the full sample, 0.21 for the first half and 1.64 for the second.
- **How badly the full-sample number hedges.** Hedged at 0.95, the first half's variance is 15.5% above that half's best hedge. That is worse than no Treasury hedge at all, which costs only 1.3%. The second half's variance is 14.6% above its best.
- **Rolling 60-day $H$.** On seed 8 it first touches 1 on day 30 after the switch, dips back, and stays above 1 from day 43. Across 500 seeds the median first crossing is day 35 (interquartile range 27–42, 5th–95th percentile 16–51), close to the back-of-envelope figure of 34.

**How:** In the setup block of Listing 8.3 (Appendix F), make `RHO` a vector, $-0.4$ for $t < 1250$ and $+0.3$ after. Then build $x_t = \ell_t\,\Delta y_t + \sigma_s\sqrt{1-\rho_t^2}\,z_t$ and refit `empirical_duration` on each half and on the whole sample. The hedged return is $R + H D\,\Delta y$. Its excess variance over a half's best hedge is $(D\sigma_y)^2(H - H_{\text{half}})^2$. With $D\sigma_y = 0.0024$ and a gap of about 0.7, that comes to $3\times10^{-6}$ against a spread-driven base near $2\times10^{-5}$, which is the 15%. For the window, use equal volatilities and let $k$ days of the new regime sit inside 60:

$$
\rho_{\text{roll}}(k) \approx \frac{(60-k)(-0.4) + k\,(0.3)}{60} = 0 \;\Longrightarrow\; k = \frac{24}{0.7} \approx 34 \text{ trading days.}
$$

The link to Case Study C: April 2025 flipped the sign twice in seven sessions. A 60-day window needs about seven weeks to cross 1, so it could not see a regime that lasted three days. It moved only after the event (the CCC rolling $H$ hit $-0.78$ on May 23). That is why the desk's answer was to lower its confidence in $H$, by raising $\eta$, widening the no-trade band and leaning on CDX, rather than to re-estimate harder.

**The trap:** Thinking "0.95 is close to 1, so the full-sample number is a fair compromise." It is close to 1 only because a flight table and an inflation table cancel into something that looks like the nobody table. It hedges each half worse than that half's own number, and the first half worse than not hedging. The second trap is treating the first noisy touch of 1 as detection. On seed 8, the estimate prints 1.05 on day 30, falls back to 0.88 by day 36, and only commits on day 43.

**If you got this wrong, read:** §8.2, "Three regimes"; §8.7, Case Study C and Figure 8.4; §8.9, the notes on Listing 8.3 and the closing "Ways This Blows Up".

**Z.08.5: The duration-hedged future as a sixth column**

**Answer:** We built the product as an HY index return (HYG's loadings, its own 5 bp/day tracking noise, no ETF basis) plus a short TY overlay at a fixed $H = 1$ *(illustrative methodology)*. What is left is $-0.11\,x + \text{noise}$, a near-twin of CDX (correlation 0.96). On the listing's seed:

- **Condition number and penalty.** Raw $\text{cond}(C)$ goes from $9.2\times10^{6}$ to $1.2\times10^{7}$. It barely moves because the HYG–JNK twin already sets the smallest eigenvalue. The penalty $\eta$ needed to cap it at 50 rises from 0.059 to 0.074.
- **CDX weight.** Under ridge it falls from 1.10 to 0.67 while the new column takes 0.72. Under OLS it falls from 1.50 to 0.98, and the drift in the OLS weights between the two halves of the sample rises from 12.3 to 32.9.
- **Out-of-sample hedged variance.** It goes from 0.364 to 0.358 of unhedged, which is no real gain.
- **With JNK removed the effect is clean.** $\text{cond}(C)$ goes from 25 to 82, $\eta$ from 0 to 0.025, and the CDX weight from 1.50 to 0.82.
- **If the product is literally $\text{HYG} - (3.2/6.5)\,\text{TY}$.** $C$ is singular ($\text{cond} \approx 10^{16}$), and OLS posts $-4.7$ in the product against $+3.6$ in HYG.

**How:** Append the column to `R_H` in Listing 8.6 (Appendix F), drawing its noise from a separate generator so the listing's own draws do not change, then rerun `hedge_matrix`. Everything the product holds lies close to the span of the existing columns $\{\text{CDX}, \text{TY}, \text{HYG}\}$. Ridge therefore splits one job, the spread hedge, between two near-substitutes, and the CDX weight stops meaning "the spread-beta hedge." Note also that a fixed $H = 1$ overlay makes the product rate-neutral only on paper. In this flight-table simulation ($\rho = -0.4$), its spread leg moves with yields, so its empirical duration is $-1.5$ years.

A fixed-$H$ product is worse than building the hedge yourself in four cases:

- **Your objective is `min_total_variance` and $\rho$ is far from zero.** Here the book's minimum-variance $H$ is 0.2. The product imposes 1, so you buy TY back to undo it and pay two bases for nothing. Product plus TY leaves 0.382 of variance out of sample, against 0.361 for CDX plus TY.
- **Its index is not your book.** An index at about 300 bp of very liquid names is not Theo's 620 bp B3.
- **It is small and its overlay runs on its own clock.** HYGH has about \$652mm against \$17.2bn for HYG, and the overlay rebalances on the methodology's schedule, not yours.
- **The regime moves and the methodology does not.**

The product is *not* worse when your objective is `zero_rates_zero_spread`, your book looks like its index, and your mandate rules out futures. In that case it is Theo's two-instrument hedge, sold pre-assembled.

**The trap:** Assuming that more instruments make a better hedge. The sixth column adds collinearity, not information. The CDX weight falls because ridge shares one job between twins, not because CDX became a worse hedge. The other trap is reading "duration-hedged" as "rate-neutral." $H = 1$ is a bet that $\rho = 0$, which is the nobody table.

**If you got this wrong, read:** §8.6, "Math, Gently" (the condition number), "The Full Derivation: minimum variance, ridge, and hedging less", and the Trend Watch "Listed Credit Beta and the Duration-Hedged Index Family"; §8.8 on the two-instrument hedge.

**Z.08.6: ROBO and the flat line**

**Answer:** The sentence: *"For an IDO book the OBJECTIVE is `zero_rates_zero_spread`: size every hedge from a named exposure (TY from DV01 at $H = 1$, CDX HY from $\text{DTS}_{\text{book}}/\text{DTS}_{\text{CDX}}$), never from a regression of the book's own P&L on the hedge instruments, because whatever that regression leaves behind is the thing we are paid for."* The test: plant a known IDO stream in a synthetic book and assert that the hedge leaves it intact.

**How:** First notice that \$38mm of HYG against \$40mm of the cold-open bond matches no named exposure. A rates-neutral HYG hedge is $40 \times 4.1/3.20 = \$51.3$mm. A DTS-neutral one is $40 \times 0.248/(3.20 \times 0.0284) = \$109$mm. A size that matches neither is a statistical fit, and a fit to the book's own P&L removes whatever moved with HYG in the sample, the view included (Ines's napkin, §8.2).

The test, written in prose:

1. Simulate 2,500 days of a book whose return is $-4.1\,\Delta y - 0.248\,x$ plus a planted IDO of 30 bp a day.
2. Fit the engine on the first 2,000 days and score it on the last 500.
3. Assert that each hedge notional is within 5% of its exposure-implied size.
4. Assert that, out of sample, the hedged P&L correlates above 0.9 with the planted IDO.
5. Assert that hedged variance is at least 0.9 times the planted IDO variance. A hedged book quieter than its own idio has hedged away the alpha.

We ran it: the exposure-sized two-instrument hedge scores a correlation of 0.96 and a variance ratio of 1.07, so it passes. A flat line fails the variance-floor assertion by construction. Running Listing 8.7's planted-IC ledger on the *hedged* P&L is the same test in IC units.

**The trap:** Writing a better version of the bad objective, such as "minimize variance, but cap the hedge at 1×." The fix is to *name* the objective, which is why §8.10's spec makes OBJECTIVE a required field with no default. The matching test-writing trap is asserting that hedged variance went *down*. That is the test ROBO's flat line passes with honours.

**If you got this wrong, read:** §8.9, "Specification for AI Implementation" (what ROBO built); §8.10, "The Spec You Hand the Robot" (OBJECTIVE and TESTS); §8.2, the Poker Table and the Ben Dor p.219 extraction; §8.8, "The IDO ledger: proving it".

**Z.08.7: The crate, at book scale**

**Answer:**

- **(a)** \$400k if the residuals are independent; \$800k at a correlation of 0.2.
- **(b)** 80%.
- **(c)** A minimum-variance hedge removes $0.5^2 = 25\%$ of the component, leaving the book's idio volatility at about \$716k.

**The two legs:**

- Short HYG, with the shares borrowed.
- Sell CDX HY protection sized to the same DTS, so market beta cancels.

Add TY futures to take out HYG's rate duration. The package is short cash bonds and long the contract: short the price of *holding paper*, which is what the pairs are long.

**What leaks:**

- The ETF's premium or discount to NAV (3–5% below NAV for the big credit ETFs on 12 March 2020).
- The CDX–cash basis and the 20 March / 20 September roll.
- The borrow, both its fee and the risk of recall.
- Three quarters of the component, which the package never touches.

**How:** In units of \$100k, so that the variance units are $(\$100\text{k})^2$:

$$
\sigma^2_{\text{book}} = N\sigma^2\,[1 + (N-1)\rho] = 16\,[1 + 15 \times 0.2] = 64, \qquad \text{common share} = \frac{N\rho}{1 + (N-1)\rho} = \frac{3.2}{4} = 0.8 .
$$

With $\rho = 0$ the variance is 16, giving \$400k, and 64 gives \$800k. In the one-factor reading the book's common component has variance $N^2\rho\sigma^2 = 51.2$ out of 64. A proxy that correlates $\rho_h = 0.5$ with the component removes $\rho_h^2$ of the component's variance, $0.25 \times 51.2 = 12.8$. That leaves $64 - 12.8 = 51.2$, and $\sqrt{51.2} = 7.155$, so \$716k. A 200,000-draw simulation returns \$800k, 0.80, \$716k and 24.9%.

**The trap:**

- **(a)** Adding the vols to get \$1.6mm. That assumes a correlation of 1, not 0.2.
- **(b)** Answering 20%, or answering 75% by counting only the off-diagonal covariance, $48/64$. The common factor lives on the diagonal too: $0.2 \times 16 = 3.2$ of the 16.
- **(c)** Either "a correlation of 0.5 removes half," or taking 25% off the *whole* book, $\sqrt{48} \to \$693$k. The hedge only acts on the common part.

**If you got this wrong, read:** §8.8, "The common whisper, at book scale" (Twelve Residuals: the same arithmetic at 12 pairs and 0.28); §8.6, "Why you hedge less than the naive amount".

<!-- STATUS: COMPLETE -->
