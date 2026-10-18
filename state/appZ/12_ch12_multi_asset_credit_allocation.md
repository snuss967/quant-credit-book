## Z.12 Chapter 12: Multi-Asset Credit Allocation

Six exercises. Every number below was recomputed in Python, with a simulation wherever a closed form needed checking. There is one note for the editor, in Z.12.5. Write your card before you read ours.

**Z.12.1: Read the chart**

**Answer:** At 40% recovery the loss given default is 0.6. If 2.55 is the expected credit loss, the implied physical default rate is $2.55/0.6 =$ **4.25% a year**. If 0.49 is the loss, it is **0.82% a year**. The first assignment survives: expected credit loss 2.55, rates MTM 0.37, spread MTM 0.49. To settle it without economics you need the PDF's *geometry*, not its text order. That means the page coordinates of each number and each category label (or the bar heights in the drawing layer, or simply the rendered image), so that each value can be snapped to the bar it sits on.

**How:** Invert the loss term of (12.1), $\lambda^{\mathbb{P}} = \text{EL}/(1-R)$. Then test the other label the same way. If 2.55 were the spread drag, the five-year widening it implies at $D^{\text{spr}} \approx 3.2$ would be

$$
\Delta s = \frac{2.55\% \times 5}{3.2} \approx 398\text{ bp},
$$

which more than doubles the index spread, and it would be the *central* forecast. The other assignment, 0.49, implies about 77 bp of widening, which is an ordinary assumption (Listing 12.1 uses 75 bp). A 4.25% default rate is in the range of long-run speculative-grade experience. A 0.82% rate is implausible for an index that is about half single-B and below. Both tests point the same way. Notice what the surviving reading implies: a 2.55% loss eats most of an index spread that stood near 2.8% (281 bp at year-end 2025, §12.3). That is why HY's 3.56% lands below the 3.68% implied cash rate in Figure 12.2. As for the PDF: the text layer lists the labels in reverse order, so the extraction order proves nothing. Word bounding boxes (an $x_0$ and a top for every string) let you match each value to its nearest category label. In the drawing layer, a 2.55 bar is about five times as tall as a 0.49 bar on the same axis.

**The trap:** The most common slip is dividing by the recovery instead of the loss given default, which gives $2.55/0.4 = 6.4\%$ and $0.49/0.4 = 1.2\%$. The ranking survives, but the numbers are wrong, and 6.4% would have you believing Nuveen assumes a recession. The subtler trap is thinking the arithmetic settles the question. $6.97 - 2.55 - 0.37 - 0.49 = 3.56$ ties under *both* assignments, because addition does not care about labels.

**If you got this wrong, read:** §12.2, "Theo's Tuesday rebuild" and the bookmaker's-odds box; then §12.3 for $\lambda^{\text{BE}} = s/(1-R)$.

**Z.12.2: The appraisal discount**

**Answer:** Under AR(1) smoothing, the lag-1 autocorrelation of the reported series *is* $\phi$, so $\phi = 0.6$ and $\xi = (1-\phi)/(1+\phi) = 0.4/1.6 =$ **0.25**. True volatility is $1.8\%/\sqrt{0.25} =$ **3.6% a year**, twice what was reported. The contemporaneous HY beta is understated by the factor $\theta_0 = 1-\phi =$ **0.4**, so the true beta is 2.5 times the reported one. The correlation with HY is understated by $\sqrt{1-\phi^2} = 0.8$.

**How:** With AR(1) weights $\theta_j = (1-\phi)\phi^j$, $\xi = \sum_j \theta_j^2 = (1-\phi)^2/(1-\phi^2)$. The reported 1.8% is a quarterly 0.9% multiplied by $\sqrt 4$. Desmoothed, that becomes $0.9\%/0.5 = 1.8\%$ a quarter and 3.6% a year. Beta sees only the part of each market move that is booked in the same quarter, $\operatorname{Cov}(r^o_t, m_t) = \theta_0\beta\sigma_m^2$, which is why its factor is smaller than the volatility's. A two-million-quarter simulation returns an autocorrelation of 0.600, a variance ratio of 0.250, a beta ratio of 0.400 and a correlation ratio of 0.800. To recover the beta, regress on current and four lagged HY returns and sum the coefficients (Dimson); that gets back $1 - 0.6^5 = 92\%$ of it.

For the committee: "Your marks add up. The smoothing weights sum to one, so every dollar the loans gain or lose reaches the NAV eventually. Nothing is hidden; it is only spread over several quarters, which is what a prudent committee does when it anchors on last quarter's mark. Our mistake came later. We multiplied the quarterly standard deviation by two, the $\sqrt 4$ rule, and that rule assumes each quarter is independent news. Your quarters carry 60% of the last one forward. Annualizing a delay as if it were independence makes it look like calm." One refinement if they push back: even an autocorrelation-adjusted annualization of the *reported* series (Lo 2002) gives only 2.77% at one year, because part of this year's move is still sitting in next year's marks. The reported series catches up with the true risk only over long horizons; in simulation, 10-year sums reach 98% of the true volatility. Desmoothing quarter by quarter, $\hat r_t = (r^o_t - \phi r^o_{t-1})/(1-\phi)$, gives the 3.6% directly.

**The trap:** Applying one factor to everything. Most readers get the volatility right and then say the beta is understated by the same 0.5. It is understated by 0.4, a bigger factor. The other slip is dropping the square root. $1.8/0.25 = 7.2\%$ treats $\xi$ as a ratio of volatilities, but it is a ratio of variances.

**If you got this wrong, read:** §12.5, Step 4: "A thermometer with a lag" and the Full Derivation that follows it (Getmansky, Lo and Makarov).

**Z.12.3: Kaz's typo**

**Answer:** The expected durations are $1/(1-0.97) =$ **33.3 months** for calm and $1/(1-0.10) =$ **1.11 months** for stress. The stationary distribution puts $\pi^\star_{\text{stress}} = 0.03/(0.03 + 0.90) =$ **3.2%** on stress and **96.8%** on calm. A filter acting with a one-month delay can act on a stress month only if the month before was also stress, and that happens with probability $P_{22} = 0.10$. So it misses 90% of stress months, and 90% of the trades it makes "for stress" land in calm months. Per visit, it overlaps $1.11 - 1 = 0.11$ months of stress. If the delay is two months, as with a NAV that arrives six weeks late, the overlap falls to 0.011 months.

**How:** The filter can label month $t$ only after month $t$'s returns have printed, and it acts in month $t+1$. Even when it is certain at $t$, the predict step gives $\Pr(\text{stress at } t+1) = P_{22} = 0.10$. In general, the filter's deviation from the stationary mix decays at the chain's second eigenvalue, $\lambda_2 = P_{11} + P_{22} - 1 = 0.07$:

$$
\xi_{t+1\mid t} - \pi^\star = \lambda_2\,\big(\xi_{t\mid t} - \pi^\star\big).
$$

So 93% of whatever the filter has learned is gone by the time it is allowed to trade. In (12.2) with a 12-month horizon, a filter that is *certain* of stress moves the stress weight from 3.2% to 3.8%. Compare the fitted chain of Listing 12.4 (durations of 21.9 and 5.7 months), which keeps 43%. A three-million-month simulation agrees: 9.8% of stress months follow a stress month.

There are two ways to repair it. (a) *Weekly data.* Keep the calendar and change the clock. A two-month stress becomes $P_{22} \approx 1 - 1/8.7 = 0.885$ per week, and calm becomes $P_{11} \approx 0.993$. A one-week delay now costs one week of a nine-week episode, and the filter acts on about 88% of stress weeks. Kaz's weekly rerun on the BB/B/CCC vector crossed one half in the third week of March 2025 (§12.9). The costs: weekly returns are noisier and less Gaussian, so there are more false alarms, each paid for in LCS. Loans, CLO mezzanine and the BDC have no honest weekly price and must leave the regime vector. A $P_{11}$ near one is estimated imprecisely. And stale prints in weekly bond data can masquerade as persistence. (b) *A prior on $P_{22}$.* Put a Beta$(a,b)$ prior on it and run MAP-EM, which replaces the M-step with $\hat P_{22} = (n_{22} + a - 1)/(n_{2\cdot} + a + b - 2)$. To illustrate: with ten one-month stress visits in the sample ($n_{22} = 1$, $n_{21} = 10$), a Beta(16, 4) prior (mean 0.8) pulls $\hat P_{22}$ to 0.55. That is a 2.2-month duration, and $\lambda_2$ becomes 0.52. The cost is that the stress duration is now partly your assumption rather than a finding. The model holds stress longer, so it is late *out* of stress, which is the BlackRock warning of §12.8 and the two-session snap-back of April 2025. And if Kaz was right that stress is one-month noise, the prior has manufactured a regime. Report the prior, and show $\hat P_{22}$ under two of them.

**The trap:** Inverting the wrong probability: $1/P_{22} = 10$ months for stress and $1/P_{11} \approx 1.03$ months for calm. That reverses the story, because a ten-month stress looks perfectly tradable with a one-month lag. A visit ends at the first "leave", so the duration is $1/(1 - \text{stay})$. The second slip is "the filter will catch it next month". The first stress month is always over before the filter can see it, and with $P_{22} = 0.10$ there is usually no second month.

**If you got this wrong, read:** §12.4: the weather coin, "Bayes, every evening" (the predict step that evaporates the alarm) and (12.2) with its stationary limit. Then Case Study A in §12.9 for the weekly rerun.

**Z.12.4: Two-asset ERC**

**Answer:** $w_{\text{HY}} = 0.22/(0.096 + 0.22) =$ **69.6%** and $w_{\text{CLO}} =$ **30.4%**, whatever the correlation. Each sleeve then carries the same DTS contribution, 0.0668. The 50/50 market-value book puts 69.6% of its DTS in the CLO tranche, and its risk share goes to CLO in the same way: 70% at $\rho = 1$, 71% at $\rho = 0.8$ and 84% at $\rho = 0$. Getting from 50/50 to ERC means moving about 20 points of NAV from CLO into HY. At $\rho = 1$ the ERC book also has 15% less volatility (DTS 0.134 against 0.158).

**How:** Write out the two risk contributions:

$$
w_1(\Sigma w)_1 = w_1^2\sigma_1^2 + w_1w_2\,\rho\,\sigma_1\sigma_2, \qquad
w_2(\Sigma w)_2 = w_2^2\sigma_2^2 + w_1w_2\,\rho\,\sigma_1\sigma_2 .
$$

The cross term is the same in both, so setting them equal leaves $w_1^2\sigma_1^2 = w_2^2\sigma_2^2$. With positive weights that is $w_1\sigma_1 = w_2\sigma_2$, so $w_i \propto 1/\sigma_i$, and $\rho$ has dropped out (for any $\rho > -1$; at $-1$ the portfolio has zero variance and the shares are undefined). Under (12.3), $\sigma_i = \text{DTS}_i\,\sigma(\Delta s/s)$. The common $\sigma(\Delta s/s)$ cancels too, leaving $w_i \propto 1/\text{DTS}_i$. So two-asset ERC is simply *equal DTS contributions*, which is Ben Dor's consistency argument (p.63) for a book of two sleeves. Under 50/50, HY's risk share is $(\sigma_1^2 + \rho\sigma_1\sigma_2)/(\sigma_1^2 + \sigma_2^2 + 2\rho\sigma_1\sigma_2)$: 16.0% at $\rho = 0$, 28.6% at 0.8 and 30.4% at 1. From three sectors on, the correlations no longer cancel, which is why Listing 12.5's `optimize_erc` solves the problem by Newton's method. Two caveats from the chapter apply. The DTS-implied volatility of a mezzanine tranche is a floor, because tranches gap in stress (§12.5), so an honest ERC weight on CLO is *below* 30%. And Nuveen's bounds cap CLO at 10% anyway.

**The trap:** Inverse-variance weights, $w \propto 1/\sigma^2$, which give 84/16. That is the minimum-variance answer at $\rho = 0$, not ERC, and it starves the riskier sleeve until it contributes only 16% of the risk. The other trap is believing that equal weights mean equal risk. The 50/50 book hands about 70% of its risk to the CLO tranche.

**If you got this wrong, read:** §12.6 on risk budgeting and its Full Derivation, then §12.3 and §12.5 (Step 1) on DTS as the common unit of risk.

**Z.12.5: The gate as a queue**

**Answer:** Under strict pro-rata fills, **never**. This quarter fills $5/15 = 1/3$ of the request, and every later quarter fills $5/10 = 1/2$ of what is left. After $n$ quarters the unpaid share is $\tfrac23\left(\tfrac12\right)^{n-1}$: half is out after 2 quarters, 90% after 4, 95% after 5 and 99% after 8. The dollar-weighted mean exit time is $2\tfrac13$ quarters, about **213 days**. The optimizer should use that mean as $\tau$ in its days budget, which is a linear average. The stress test should use a tail number: 95% out takes 5 quarters, about **456 days**. Both should be computed as functions of the request ratio $Q/g$ and re-estimated every tender cycle. A constant is wrong because $Q$ is set by other holders, and it rises exactly when you most want to leave.

**How:** Pro-rata means you receive $g/Q_t$ of whatever you ask for each quarter. Unfilled requests are not carried over, so you resubmit the remainder, and $R_n = R_{n-1}(1 - g/Q_n)$. With a constant fill $p$, the wait is geometric with mean $1/p = Q/g$ quarters. Here, therefore,

$$
\bar\tau = 1 \cdot \tfrac13 + \tfrac23\,(1 + 2) = 2\tfrac13 \text{ quarters}.
$$

The chapter's "at least three quarters" (§12.7) is the case where the line *drains*: fills of 1/3, then 5/10, then 5/5. In this exercise the line refills to 10% every quarter, so the fill never reaches one. If the 10% were new requests *on top of* the resubmissions, the line would grow and the exit would take longer still. Now feed this into the engine. At a 15% weight, $0.15 \times 213 = 32$ days, which is Listing 12.5's entire $\bar\tau$, against 27 days at Listing 12.1's constant of 180. At the 95%-out figure, $0.15 \times 456 = 68$ days, and the days budget alone would cap the sleeve near 7%. A constant fails for four reasons. $Q$ is endogenous: HPS's flagship went from requests of about 4% of shares in the fourth-quarter cycle to about 9% in the first, and Blue Owl's technology fund from above 15% to about 40% (§12.7). $Q$ moves with the news and with the spread factor, so the exit is longest in the state where you need it (Ben Dor p.296). The line refills itself through resubmissions. And the gate is a decision: the IMF noted managers who paid out more than 5%. A constant 90 days describes a world where $Q \le g$.

NOTE (for the editor): In "The Queue" (§12.7), the grading of Kaz's card says a 90-day $\tau$ "would have been wrong ... by something nearer seven at the technology fund." With requests of about 40% of shares against a 5% gate, $Q/g = 8$. That is both the dollar-weighted mean exit (in quarters) under a stationary line and the number of quarters to drain a line that stops growing, so the text should say "nearer eight" unless the request share was nearer 35%. The HPS figure checks: $9/5 = 1.8$, "a factor of two."

**The trap:** Answering "three quarters" ($15/5$), as if the line were a stock that drains. That is the lower bound in the §12.7 annotation, and it holds only if nobody new joins. With the line refilling to 10%, you get half of what is left each quarter, forever. A related slip is "twenty quarters", which reads the gate as 5% of *your* position rather than 5% of the fund.

**If you got this wrong, read:** §12.7: the annotation to Ben Dor p.296, the constraint set (12.4) and "Long Scene: The Queue" (Theo's card and Ines's).

