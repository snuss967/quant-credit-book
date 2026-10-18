## Chapter 16: Post-Reorganization Equities, Rights Offerings & Bankruptcy Claims

Six exercises: two on the forced seller, one on the backstop seat, one on warrants, one at the loading dock and one on a dollarized crypto claim. Every number below was recomputed from the chapter's Blocks 1 to 5 (Appendix F, Listings 16.1 to 16.5). Write your answer down before you read ours; the gap is your markout.

**Z.16.1: The CLO that wanted a term loan**

**Answer:** (a) $\phi^{\text{OH}} = 30/65 = 46.2\%$. (b) The expected total abnormal return is $\kappa Q_0/M = 0.3 \times \tfrac12 = 15\%$, half of it earned in the first $\ln 2/3.4 = 0.20$ years (2.4 months), with a starting drift of 51% a year. (c) Electing CLOs leave 6 points of the class in CLO hands, so $\phi^{\text{OH}} = 6/(6 + 35) = 14.6\%$. With the arbitrage capital unchanged, the total abnormal return falls to $0.3 \times 6/60 = 3\%$. The half-life is still 2.4 months.

**How:** The float is everything that is neither controlled nor locked, $n^{\text{float}} = n^{\text{out}} - n^{\text{lock}}$, and that is the CLOs plus the free holders: $30 + 35 = 65$. Block 1 with constant capital ($\rho = 0$, $M_0 = M^{*} = M$) has the closed form

$$
\int_{t_0}^{\infty}\mu_t\,dt = \frac{\kappa Q_0}{M} = 0.3 \times \frac{Q_0}{2Q_0} = 0.15 .
$$

Here $\theta$ sets only the timing, not the size. In (c), 80% of the CLOs, 24 points of the class, take the term loan *instead of* stock, so those shares are never issued. The share pie becomes $6 + 35 + 35 = 76$ and the float becomes $6 + 35 = 41$. The overhang falls to $Q_0' = 0.2\,Q_0$, while $M$, the patient money willing to absorb it, has not changed: $\kappa Q_0'/M = 0.3 \times 0.2/2 = 3\%$. So the election moved four-fifths of the forced supply into an instrument the sellers are allowed to hold. At the open, every share the sponsor and the free holders own is marked 12 points closer to fundamental value, and there is much less of a seller for anyone to wait out. A buyer of the open loses the flow trade, and every holder of the stock gains.

**The trap:** Re-scaling capital to "twice the *new* overhang" gives 15% again and makes the election look irrelevant. $M$ belongs to the market, not to the seller, and it does not shrink because the CLOs sold less. The runner-up mistake in (a) is $30/100 = 30\%$, which forgets that the sponsor's locked 35% cannot trade. In (c) it is $6/65 = 9.2\%$, which keeps the electing CLOs' never-issued shares in the float.

**If you got this wrong, read:** §16.1.1 (the overhang share), §16.2.2 (the constant-capital closed form) and §16.2.1 (Mags: "Did they elect?").

**Z.16.2: Two speeds**

**Answer:** We used Block 1's other inputs ($Q_0 = 30$, $\kappa = 0.3$, $\theta = 3.42$ from the fallen-angel calibration), plus $\rho = 0.5$, $M_0 = 30$ and $M^{*} = 60$. The model's three six-month reversals are then $25.56\%$, $3.74\%$ and $0.588\%$. A single exponential through the first two gives $\hat\theta = 3.84$ and predicts $w_3 = 0.547\%$, so it falls 7% short of the true third window. The joint `least_squares` fit returns $\theta = 3.42 \pm 0.02$ and $\rho = 0.50 \pm 0.03$. It ran on the mean of a 200-name, 1.5-year panel with 2% daily noise, from a fresh `default_rng(16)`, with $\kappa$, $Q_0$, $M_0$ and $M^{*}$ held at their true values. The third window identifies $\rho$.

**How:** This extends Listing 16.1: `simulate_residual_panel` builds the panel, and the residual for `least_squares` is `ForcedSellerOverhang(...).discount(s)` minus the cross-sectional mean. The discount decays at a rate that changes over time:

$$
-\frac{d}{ds}\ln\frac{\kappa Q_s}{M_s} = \theta + \frac{\dot M_s}{M_s} = \theta + \frac{\rho\,(M^{*} - M_s)}{M_s},
$$

which falls from 3.92 at $s = 0$ to 3.57 at $s = 1.5$ as the capital settles. A single exponential through $w_1$ and $w_2$ reads the early, faster rate, so it underpredicts $w_3$. To see which parameter the third window pins down, differentiate the two log ratios. Both $\ln(w_2/w_1)$ and $\ln(w_3/w_2)$ load about $-0.49$ on $\theta$, but they load $-0.35$ and $-0.13$ on $\rho$. Their difference, which is the bend in the decay that only a third window can show, therefore loads $+0.22$ on $\rho$ and $-0.003$ on $\theta$. Two windows give one combination of the two speeds. The third separates them, and what it adds is $\rho$.

**The trap:** Reading $w_3$ straight off the panel by differencing the cross-sectional mean on two single days. Each daily mean carries noise of $0.02/\sqrt{200} \approx 0.14$ points, so the difference carries about 0.2 points, which is as large as $w_3$ itself. With seed 16 it prints 0.33% and seems to say the opposite. Use the fitted curve, or average several days at each end. The second trap is to hear "the third window identifies $\rho$" as "the tail decays at $\rho$". It does not; see the note.

NOTE (for the editor): §16.2.3 says the capital-arrival term $Q_t\dot M_t/M_t^2$ "decays at the speed of the slow money ($\rho$), not the speed of the sellers ($\theta$)", and this exercise says the model's single-exponential undershoot is like Dynkin's. In the model, that term decays at $\theta + \rho$, and the whole discount decays at $\theta + \dot M/M \ge \theta$, so $w_3/w_2 < e^{-\theta\Delta}$ always. At $\theta = 3.42$ and $w_2 = 1.04\%$, the third window can be at most 0.188%, while the data show 0.86% (checked by grid search over $\rho$ and $M_0/M^{*}$). Here slow capital lifts $w_3$ by 7.5% (0.588% against 0.547%), whereas Dynkin's third window is 4.5 times the single-exponential line (0.86% against 0.19%). Fitting Dynkin's three numbers inside this model needs $\theta \le 0.38$ a year, with capital as the *fast* component; one exact fit is $\theta = 0.38$, $\rho \approx 25$, $M_0/M^{*} \approx 0.62$. That is the opposite of the chapter's labeling, and of Ines's "fast decay is the seller, slow decay is the table filling up." Suggest rewording §16.2.3, or adding a second, slower seller compartment to the model.

**If you got this wrong, read:** §16.2.2 (*The Full Derivation*: the quotient rule behind the two drift terms), §16.2.3, and Listing 16.1 in Appendix F.

