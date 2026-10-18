## Chapter 17: Private Credit & the Public–Private Convergence

Six exercises: one on the smoothing kernel, two on reading a BDC's disclosures, one on the redemption game, one on takeout supply and one on the runway. Every number below was recomputed by running the chapter's five blocks (Appendix F, Listings 17.1 to 17.5) and extending them. Write your answer down before you read ours; the gap is your markout.

**Z.17.1: The year-long lag**

**Answer:** With $\theta_k=\tfrac14$ for $k=0,\dots,3$, the variance ratio is $\sum_k\theta_k^2=\tfrac14$. Reported volatility is therefore half the true figure, and the reported Sharpe ratio is $1/\sqrt{1/4}=2$ times the true one. The lag-one autocorrelation is $\rho^o_1=\tfrac34$; the lag-two and lag-three values are $\tfrac12$ and $\tfrac14$. ROBO's 2.1% is really **4.2%**. Measured in the same quarter, the vehicle's correlation with the loan index is **half** the true correlation. Sum the current quarter and the three lags (the whole kernel) and you get **all** of it back.

**How:** Each line comes from the §17.2.2 moments.

$$
\sum_k\theta_k^2=4\cdot\tfrac1{16}=\tfrac14,\qquad
\text{SR}^o=\frac{\text{SR}}{\sqrt{1/4}}=2\,\text{SR},\qquad
\rho^o_1=\frac{\theta_0\theta_1+\theta_1\theta_2+\theta_2\theta_3}{1/4}=\frac{3/16}{1/4}=\tfrac34 .
$$

Reported volatility is $\sigma/2$. The annualizing factor $\sqrt4$ multiplies both series equally, so the true figure is $2\times2.1\%=4.2\%$. In the same quarter, $\operatorname{Corr}(x^o_t,F_t)=\big(\theta_0/\sqrt{\sum_k\theta_k^2}\big)\rho=(\tfrac14/\tfrac12)\rho=\rho/2$. Against the summed index you get $\operatorname{Cov}\big(x^o_t,\sum_{k=0}^{3}F_{t-k}\big)=\beta\operatorname{Var}(F)\sum_k\theta_k=\beta\operatorname{Var}(F)$ with $\operatorname{Var}\big(\sum_{k=0}^{3}F_{t-k}\big)=4\operatorname{Var}(F)$ and $\operatorname{sd}(x^o)=\sigma/2$, so the correlation is $\beta\sigma_F/\sigma=\rho$. Put another way, a Dimson regression with $K=3$ has an $R^2$ of exactly $\rho^2$. We checked all of this with Listing 17.1's `simulate_smoothed` over 400,000 quarters. The measured correlations were 0.500 and 0.999 of the true correlation, and the simulated autocorrelations 0.749, 0.500 and 0.250.

**The trap:** The most common slip is to divide by the variance ratio instead of its square root, which gives $2.1\%/0.25=8.4\%$. A second is to think that calendar-year returns wash the smoothing out. They don't. A year of reported returns weights seven true quarters by $(1,2,3,4,3,2,1)/4$, so its volatility is $\sqrt{11/16}=0.83$ of the true annual figure: 3.5%, not 4.2%. A third is to stop one lag short. With lags 0 to 2 the summed correlation is only $\sqrt3/2=0.87$ of the truth, because a Dimson regression whose $K$ is smaller than the kernel's still under-reports.

**If you got this wrong, read:** §17.2.2 (the porch-thermometer box and *The Full Derivation*), §17.2.3 (summing the canyon's echoes) and Listing 17.1 in Appendix F.

**Z.17.2: Marking the discount**

**Answer:** $m=(0.96-0.62)/2.25=0.34/2.25=$ **15.1%** of reported assets. The market is carrying a book that the manager marks near 100 at about 85. Once you admit that the unsecured notes are not money-good, the true markdown is **higher**, so 15.1% is a lower bound. To find out by how much, use the Merton model of Chapter 23 (§23.1, equity as a call on firm assets, with the machinery from Chapter 6), which is the "Merton-on-a-CLO" extension that §17.3.2 points to.

**How:** The thin slice says $P/\text{NAV}=(1-\phi)-m(1+\ell)$. The fee takes 4 of the 38 points of discount, which leaves 34 points that are about the loans, and dividing by $1+\ell=2.25$ turns the equity discount into an asset markdown. Listing 17.2's `implied_markdown(0.62, 1.25, 0.04)` returns 0.1511. For the second part, drop assumption (iii). If the notes can default, their market value $D^{\text{mkt}}$ is below face $D$, and

$$
P\cdot\text{shares}=A(1-m)-D^{\text{mkt}}-\phi E\;>\;A(1-m)-D-\phi E .
$$

The price is fixed, so $A(1-m)=P\cdot\text{shares}+D^{\text{mkt}}+\phi E$ must be smaller than in the money-good case, which makes $m$ larger. In option language, limited liability gives the equity time value on top of its intrinsic value, so part of the 0.62 is option value rather than asset value. As a size check (we computed this, though the exercise doesn't ask for it): with asset volatility of 8% and a 3-year horizon, the Merton-implied $m$ stays at 15.1% (it moves only in the fourth decimal place); at 15% volatility and 5 years it rises to 16.3%. The direction is certain. The size matters only when asset volatility is high, which is precisely when the market has stopped trusting the marks.

**The trap:** The first trap is reading the equity discount as the asset discount. That gives 38%, or 34% net of fees, and forgets that the equity is a thin slice on top of a levered book. The second is dropping the fee drag, which gives $0.38/2.25=16.9\%$. In the argument, the tempting wrong answer is "lower, because the noteholders absorb part of the loss." With the price held fixed, that sharing is exactly why the equity price is *less* sensitive to the loans, so a given discount implies a *bigger* loss on the loans. Don't set a $\mathbb{Q}$-measure BDC CDS spread beside this $\mathbb{P}$ markdown without saying which is which.

**If you got this wrong, read:** §17.3.2 (the thin-slice box and *Boundary conditions*), Listing 17.2, and Chapter 23 §23.1.

**Z.17.3: The bad bucket**

**Answer:** $\hat R^{\text{mark}}_{\text{NA}}=(1.0/3.1)\times0.97=$ **0.313**, so the non-accrual loans are carried at about 31 cents per dollar of cost, with a gap of $g=2.1$pp. That is 19 cents below Octus's ~50-cent restructuring recoveries, and close to OBDC's June 2026 figure of 28 cents. Octus's ~50 cents belongs in the Chapter 14 recovery model as the prior for the restructuring-date recovery, with a wide distribution and the §14.3 re-default clock applied on top. The 31-cent mark is a signal you compare against the model's output, not something to fit the model to. Neither number is a recovery. The 31 cents is a present value of loans that have not been resolved. The 50 cents is measured at a moment the borrower chose, on other managers' loans, before any second default.

**How:** The bucket's fair value over its cost is

$$
\hat R^{\text{mark}}_{\text{NA}}=\frac{w^{FV}_{\text{NA}}\,FV}{w^{C}_{\text{NA}}\,C}=\frac{0.010}{0.031}\times0.97=0.313 .
$$

Listing 17.2's `implied_nonaccrual_mark(0.010, 0.031, 0.97)` returns 0.3129. Why neither number is a recovery: a recovery is cash or value received at resolution, per dollar of claim. The mark is a valuation committee's present value today. It is quoted per dollar of cost rather than par, it moves on the §17.2 kernel, and it covers some loans that will cure. Discount 50 cents received two years from now at a distressed rate of 20–25% and you get $0.50/1.2^2=0.35$ to $0.50/1.25^2=0.32$, so the two numbers can both be right. Octus's figure is measured *at the restructuring*, which is §14.1's "recovery at the exchange." It comes before the second default that Pluralsight's new equity went through (written to zero by February 2026), and it is a cross-section of other managers' loans rather than this book's bucket.

**The trap:** The most common slip is to put the 31 cents into the model as a recovery (an LGD of 69%), which fits Chapter 14 to one manager's opinion, lagged. The second is to read the 1.0% fair-value share as "the bad bucket is small." What matters is the cost share, and the gap between the two. Dropping the $FV/C$ factor gives 32.3 cents. That error is small here, but it grows as the whole book is marked down.

**If you got this wrong, read:** §17.3.3 (the bowl box and the OBDC table), §14.1 (two recovery rates) and §14.3 (the re-default clock).

**Z.17.4: Kaz's fix**

**Answer:** With no redemptions the true value is $1-m=0.920$ of NAV per share. **Under a 5% cap** ($p=0.05$) the stayers hold $(0.92-0.05)/0.95=$ **0.9158**: they lose 0.42 points, and the transfer is $p\,m=0.40\%$ of NAV. **Under Kaz's 100% cap** ($p=0.40$) they hold $(0.92-0.40)/0.60=$ **0.8667**: they lose 5.33 points, and the transfer is $3.2\%$ of NAV, all of it borne by the 60% who stayed. The markdown left on the surviving shares compounds as $m/(1-p)$, to 8.4% after a capped quarter and to 13.3% after Kaz's.

**How:** Use $N^{\text{true}}_{\text{stay}}=N\big((1-m)-p\big)/(1-p)$ with $p=\min(a,c)$, which is Listing 17.4's `stayer_value(1.0, 0.08, 0.40, cap)`. The new markdown on the shares that stay is

$$
m'=1-\frac{(1-m)-p}{1-p}=\frac{m}{1-p}.
$$

The game has not ended, because requesting still dominates whenever $m>0$. Under the cap a requester gets $0.125\times1+0.875\times0.9158=0.926$ against 0.916 for staying, an edge of about 1 point. Under Kaz's cap she gets 1.00 against 0.867, an edge of 13 points. Without rationing the edge compounds: at 40% requests a quarter, $m$ goes 8% → 13.3% → 22.2% → 37.0% → 61.7% → above 100% in quarter five. At that point the fund cannot pay $N$ to everyone, and whoever is last gets nothing. Liquidity makes it worse. With cash at 0.2% and leverage of 0.9x, paying 40% of NAV means selling about $0.40/1.9\approx21\%$ of the loan book in one quarter, and the fire-sale discount raises the realized $m$. That is Diamond–Dybvig. With sequential service and illiquid assets, a run is a self-fulfilling equilibrium even when the marks are honest. Their remedies are suspension of convertibility, which is the gate, or the cap Kaz wants to remove, and deposit insurance or a lender of last resort (here, the sponsor's house money, like BCRED's \$400mm). They would have told Kaz that the queue is the visible price of preventing the run. To actually end the game you need $m=0$: faster marks, or paying redeemers nearer true value through a repurchase fee or swing price sized to $m$.

**The trap:** One slip is to give 0.92 under both caps, which forgets that leavers are paid at the smoothed NAV. Another is to use $p=a=0.40$ under the 5% cap as well and get 0.867 twice. The conceptual trap is to call the 100% cap "fairer because nobody is trapped." It is fairer only to the people who leave first.

**If you got this wrong, read:** §17.6.2 (the pizza box, *The game* and *The Full Derivation*), Listing 17.4, and Chapter 23 §23.8 (a run is not a diffusion).

**Z.17.5: Takeout season**

**Answer:** We used block 3's illustrative book (400 loans, seed 2023) with its spread differential $\Delta s=1$pp. Competing-risks supply at $\zeta=0$ is \$3,757mm, and it halves at $\zeta\approx$ **0.88**, which is 0.88 standard deviations of the excess loan premium. That is very close to the one-door shortcut $\ln2/|\psi_B|=\ln2/0.8=0.87$. The naive estimate overstates the competing-risks one by **1.3%** at $\zeta=-1$ (loose), 1.8% at $\zeta=0$, **2.6%** at $\zeta=+1$ (tight) and 3.6% at $\zeta=+2$. In dollars the overstatement *shrinks*, from \$105mm to \$44mm, because tight-regime supply (\$1,705mm) is about a fifth of loose-regime supply (\$8,091mm).

**How:** Supply is $S(\zeta)=\sum_i\text{Face}_i\,\kappa^{(B)}_i\Delta t\,g(\mathcal{K}_i\Delta t)$ with $g(y)=(1-e^{-y})/y$ and $\kappa^{(B)}\propto e^{-0.8\zeta}$. If $g$ were constant, supply would halve at $\ln2/0.8$. As $\zeta$ rises, the syndicated door narrows faster than the other doors widen. The face-weighted total hazard falls from 0.38 to 0.31, so $g$ rises slightly, and supply falls a little more slowly than $\kappa^{(B)}$. Root-finding on `bsl_supply` gives 0.878 (0.870 with $\Delta s=0$). For the overstatement, expand $g(y)\approx1-y/2$:

$$
\frac{1-e^{-\kappa^{(B)}\Delta t}}{\frac{\kappa^{(B)}}{\mathcal{K}}\big(1-e^{-\mathcal{K}\Delta t}\big)}=\frac{g(\kappa^{(B)}\Delta t)}{g(\mathcal{K}\Delta t)}\approx1+\tfrac12\big(\kappa^{(P)}+\kappa^{(X)}+\lambda\big)\Delta t .
$$

The overstatement is half of one quarter's hazard on the *other* doors. Because $\psi_P,\psi_X,\psi_D>0$, those doors widen as the market tightens: their face-weighted hazard rises from 0.109 to 0.210, and the approximation gives 1.4% and 2.6%, against the exact 1.3% and 2.6%. For a CLO-demand forecast (Chapter 21), the error points one way and is largest in proportion exactly when collateral is scarce, which is when the forecast matters. The loans it counts in are ones that were amended into PIK or defaulted, and neither kind is CLO collateral. The bias moves with the regime, so no constant calibrates it away. Keep the sizes in view, though. With these illustrative hazards the correction is 1–4%, while the regime itself moves supply by −79%, so get $\zeta$ right first. On the software-only subset the overstatement is already 3.1% at $\zeta=+1$, and a book whose other-door hazards are several times larger has a correction several times larger.

**The trap:** One wrong answer is $\zeta=\ln2/0.8=0.87$ from the syndicated hazard alone. It is close here, but only because $\mathcal{K}\Delta t$ is small, so say why it is close. Another is to compare dollar gaps and conclude that the naive estimate overstates *less* in the tight regime. "By more" only makes sense as a fraction of supply.

NOTE (for the editor): The exercise and §17.4.2 ("it overstates most in exactly the stressed regime") hold for block 3's parameters only in proportional terms: 1.30% at $\zeta=-1$ against 2.57% at $\zeta=+1$. In dollars the overstatement falls, from \$105.4mm to \$43.8mm, because tight-regime supply is \$1,705mm against \$8,091mm loose. Suggest "by a larger fraction" in both places.

**If you got this wrong, read:** §17.4.2 (the three-doors box and *Why the competition term matters*), Listing 17.3, and Chapter 21 for the CLO-demand side.

**Z.17.6: The thirteen-week model, reborn**

**Answer:** Your fund's numbers will differ, so here is a worked version on the chapter's illustrative stack: cash 0.2% of NAV, an undrawn line of 10%, a 10% sleeve haircut by 10%, 5% redemptions, unfunded draws of 2% a quarter, no maturities in the window and repayments of 3% a quarter. That gives $\mathcal{T}=0.192/0.04=$ **4.8 quarters**. Halve repayments to 1.5% and it falls to $0.192/0.055=$ **3.5 quarters**; with no repayments, 2.7. If the borrowing base excludes PIK and non-accrual loans, and that cuts the undrawn line from 10% to 6% of NAV, the runway falls to 3.8 and **2.8** quarters. Every version sits below the IMF's moderate-shock range of 5–7 quarters, and none of them should be trusted until you have read the credit agreement's eligibility and advance-rate definitions.

**How:** Fill in $\mathcal{T}=\big(\text{Cash}+\text{Undrawn}+\text{Sleeve}(1-h)\big)\big/\big(c\cdot\text{NAV}+\text{Unfunded draws}+\text{Maturities}-\text{Repayments}\big)$ from the 10-Q.

- Cash comes from the balance sheet.
- Undrawn lines come from the borrowings note or the MD&A liquidity section. Take availability *under the borrowing base*, not the commitment.
- The sleeve is the broadly syndicated, Level 2 loans in the schedule of investments.
- Unfunded commitments are in the commitments note. Convert them to a quarterly draw rate.
- Maturities are in the borrowings note.
- Trailing repayments are "repayments and sales" in the investment-activity table or the cash-flow statement.

The runway is convex in repayments, because $\partial\mathcal{T}/\partial\text{Rep}=\text{numerator}/\text{denominator}^2$. At 3% repayments, each point of NAV per quarter is worth 1.2 quarters of runway, which is why halving them costs 1.3 quarters. Listing 17.4's `runway_quarters` reproduces every figure above. Halving is, if anything, mild. In block 3 (Listing 17.3) the face-weighted quarterly probability of a syndicated or private takeout, which is what a repayment is, falls from 12.8% at $\zeta=-1$ to 4.6% at $\zeta=+1$, a cut of nearly two-thirds.

**The trap:** One trap is to treat the commitment as the undrawn line. The borrowing base usually excludes or haircuts PIK, non-accrual and over-concentrated loans, so availability shrinks exactly when the queue lengthens, which is Theo's question from the cold open. Another is to use trailing repayments from the 2024–25 refinancing wave as though they were a constant; they are the §17.4 hazards, and they fall when $\zeta$ rises. A third is to value the sleeve at par when every fund is selling the same loans the same week. Check also whether the facility sweeps repayments to pay down the line, because then they cannot be counted twice. The 1940 Act's 150% asset-coverage test is rarely the first constraint at 0.9x leverage; the borrowing base binds first.

**If you got this wrong, read:** §17.6.2 (*Liquidity runway* and *The Full Derivation*), Ways This Blows Up (3) in §17.6, §17.4.2 for the repayment hazards, and Listing 17.4 in Appendix F.

<!-- STATUS: COMPLETE -->
