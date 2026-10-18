## Z.06 Chapter 6: Stochastic Calculus, Intensity Models & Structural Frameworks

Eight exercises: the two warm-ups, A and B, and the six numbered ones. I recomputed every number in Python. Where an exercise names an engine function, I ran it from Appendix F, Listings 6.1–6.7, seeded `default_rng(42)`. None of the chapter's exercises carries a [Read]/[Derive]/[Build] tag, so none appears below.

**Z.06.A: Warm-up A, the holdco at 40**

**Answer:** (a) Outside the bank, the holding company has $\$2{,}258+491+896+577=\$4{,}222$mm of assets against $\$3{,}370+305=\$3{,}675$mm of liabilities. Book recovery is therefore **1.15 per dollar (115%) with the cash** and $\$1{,}964/\$3{,}675=$ **0.53 (53%) without it**. The notes at 40 were pricing the no-cash world. They actually sat 13 points *below* it, a discount for time, fees, and claimants who had not filed yet. (b) A twelve-point gap implies a reinstatement probability of $12/17\approx$ **71%, "roughly 70%."**

**How:** For (a), add up the four non-bank assets and divide by the two liabilities. Then remove the cash, because a bank holding company keeps its cash at its bank, and from noon on 10 March that cash was a deposit claim on a receivership. For (b), use two states. With probability $p$ the bonds are reinstated (2025s worth 97, 2031s worth 80). Otherwise both pay the same liquidation value $L$ per dollar of claim:

$$
P_{25}=97p+L(1-p),\qquad P_{31}=80p+L(1-p)\;\Longrightarrow\;P_{25}-P_{31}=17p=12,\quad p=0.706 .
$$

The unknown $L$ cancels, and that is the whole trick: the *gap* identifies the probability without your knowing the recovery. Use only the gap. Put $p=0.706$ back into either price and the implied $L$ is under 2 cents, far below the 53% no-cash coverage, so the two-state model reads a probability from the spread but is not meant to fit the two price levels. I checked the reinstatement values. Priced at a 5% yield from 25 April 2023, a 3.50% note maturing January 2025 is worth 97.5 clean and a 1.800% note maturing February 2031 is worth 79.6, so 97 and 80 are fair. A low coupon kept to a long maturity is worth less when the market yields 5%.

**The trap:** In (a), the trap is the 115%: you read "par is in there" and buy at 40. That is Theo's first answer, before Mags asks where a bank holdco keeps its cash. In (b), the trap is to read the gap as an arbitrage between two identical claims. They are identical only in liquidation. The market was pricing a second state in which they are not.

**If you got this wrong, read:** §6.4.4, Beat 4 and "Decision point: the holdco at 40" (with Figure 6.4), then Beat 5, "the same claim at two prices."

**Z.06.B: Warm-up B, secured at 76.8 or stripped at par**

**Answer:** Exchanging is worth $0.768\times\$1{,}000\times0.90=$ **\$691** per \$1,000 of old face. Holding out is worth $\$1{,}000\times0.60=$ **\$600**, so the exchange wins by about \$91. The holdout breaks even at a stripped-note price of $0.768\times90=$ **69.1**. The sentence: *the holdout still owns \$1,000 of face, but it now stands behind about \$4.2bn of new secured notes with a lien it does not share, in an indenture whose covenants were stripped by exit consents. Its strike moved up and its barrier was deleted, so the face amount is the only thing that stayed the same.*

**How:** Put both choices on the same denominator, \$1,000 of *old* face:

$$
V_{\text{exchange}}=0.768\times P_{\text{sec}}\times1{,}000,\qquad V_{\text{hold}}=P_{\text{strip}}\times1{,}000,\qquad P^{*}_{\text{strip}}=0.768\times P_{\text{sec}}=69.1 .
$$

This ignores coupons (the new notes' early PIK, the old 5.5% cash coupon), which is fine over a short horizon where the price gap dominates. In the language of §6.5.3, the left-behind payoff becomes $\min\big(\max(V_T-F^{+},0),F\big)$: the same $F$ of face, sitting on top of a new senior layer $F^{+}$.

**The trap:** One wrong answer compares prices and says "90 beats 60," which forgets that you get only 76.8 cents of new face per dollar of old. The mirror-image error is "\$1,000 of face beats \$768." The answer is always face times price. For the sentence, the trap is "same CUSIP, same coupon, same maturity, so same claim." Everything that made it a claim on the firm's value (rank, liens, guarantees, covenants) was changed around it.

**If you got this wrong, read:** §6.10.1, Beats 3–4 and "The Merton reading"; §6.5.3, "An uptier moves the barrier for someone else."

**Z.06.1: The vol trade inside a bond**

**Answer:** For the §6.2.4 firm, the Merton spread is **27 bp at $\sigma_V=15\%$** (27.4), 216 bp at 25%, and **531 bp at 35%**. Debt is worth 76.65, 75.22 and 72.89. The derivative is $\partial B_0/\partial\sigma_V=-V_0\,\phi(d_1)\sqrt T<0$, which is $-7.5$, $-19.9$ and $-26.0$ per unit of volatility at the three points. At 25%, one more vol point costs the bond about 0.20 and widens the spread by about 26 bp. The sentence for Theo: *your bond is par minus a put you wrote to the shareholders, and a put is worth more when the asset is more volatile, so every point of asset vol is money out of your pocket and into the equity's. A sponsor who owns the call knows that a risky acquisition financed at today's spread moves value from the bondholders to the sponsor before a single synergy shows up.*

**How:** $V_0$ does not depend on $\sigma_V$, so

$$
B_0=V_0-E_0\quad\Longrightarrow\quad\frac{\partial B_0}{\partial\sigma_V}=-\frac{\partial E_0}{\partial\sigma_V}=-\text{vega}.
$$

Differentiate the call. The identity $V_0\phi(d_1)=Fe^{-rT}\phi(d_2)$ kills the cross terms, and $\partial d_1/\partial\sigma_V-\partial d_2/\partial\sigma_V=\sqrt T$, so

$$
\text{vega}=V_0\,\phi(d_1)\sqrt T>0 .
$$

Equivalently, $B_0=Fe^{-rT}-\text{Put}$, and by put–call parity the put has the same vega as the call. For the spreads, use $s=-\tfrac1T\ln\!\big(B_0/Fe^{-rT}\big)$ with $Fe^{-rT}=76.86$. Notice the convexity: from 15% to 25% the spread rises by 189 bp, and from 25% to 35% by 315 bp. Listing 6.2's `merton_prices` reproduces all three spreads.

**The trap:** The most common wrong answer is "bondholders are long vol, because higher vol means a wider spread and a bigger coupon." That confuses the spread a *new* buyer demands with the value of the bond you already own, which falls. The second trap is algebraic: if you skip the identity $V_0\phi(d_1)=Fe^{-rT}\phi(d_2)$, you are left with a four-term mess and often a sign error.

**If you got this wrong, read:** §6.2.1, "Payoff diagrams" (the bondholder wrote a put); §6.2.3, the closed forms; §6.2.4, the worked example and Figure 6.3.

**Z.06.2: Is it cheap or is it the rake?**

**Answer:** At one year, $DD^{\mathbb{P}}=-N^{-1}(1.5\%)=2.170$. The shift is $\rho\,\text{SR}_M=0.175$, so $DD^{\mathbb{Q}}=1.995$ and **$\text{PD}^{\mathbb{Q}}_1=2.30\%$**. At five years, compounding the 1.5% gives **$\text{PD}^{\mathbb{P}}_5=7.28\%$**. The shift grows to $0.175\sqrt5=0.391$, so **$\text{PD}^{\mathbb{Q}}_5=14.4\%$**. On the CDS side, $\lambda^{\mathbb{Q}}=0.018/0.60=$ **3.0%**, which gives a five-year $\mathbb{Q}$-PD of **13.9%**. Compared raw, protection looks twice too expensive. The CDS hazard is 2.0 times the $\mathbb{P}$ hazard, and the $\mathbb{P}$-PD alone justifies only about 91 bp. But after the diffusive premium *alone*, the structural $\mathbb{Q}$-PD (14.4%, an average hazard of 3.10%, a fair spread near 186 bp) sits slightly *above* the CDS's 13.9%. So the CDS is about 6 bp tight, not wide. It is the rake.

Three things to strip before calling any residual alpha:

1. **The whole risk premium.** The CAPM shift removes the diffusive part. The jump premium of §6.3.3 is still in there, and removing it would make the CDS look tighter still.
2. **The recovery convention.** The 3.0% is conditional on the 40% quoting recovery, and a spread identifies only $\lambda(1-R)$. At $R=23\%$ the same 180 bp gives $\lambda=2.34\%$ and a five-year PD of 11.0%.
3. **Systematic factor exposure and liquidity.** Beta, the illiquidity premium, and the CDS–bond basis all sit in the gap. A high $\lambda^{\mathbb{Q}}/\lambda^{\mathbb{P}}$ in a risk-off week is "beta wearing a disguise." IDO or it didn't happen.

**How:** The Bohn–Stein shift is

$$
\text{PD}^{\mathbb{Q}}_T=N\!\Big(N^{-1}\big(\text{PD}^{\mathbb{P}}_T\big)+\rho\,\text{SR}_M\sqrt T\Big).
$$

At five years, first turn the one-year $\mathbb{P}$-PD into a five-year one with a constant hazard: $\lambda^{\mathbb{P}}=-\ln(0.985)=1.51\%$, so $\text{PD}^{\mathbb{P}}_5=1-0.985^5=7.28\%$. Only then shift, by $0.175\sqrt5$: $N(-1.455+0.391)=N(-1.064)=14.4\%$. For the CDS, the triangle gives $\lambda=s/(1-R)$ and survival $e^{-5\lambda}=e^{-0.15}$. To compare like with like, turn the structural $\mathbb{Q}$-PD back into a hazard: $-\ln(1-0.1437)/5=3.10\%$. Times $0.60$, that is 186 bp against the 180 bp quoted.

**The trap:** The trap is Theo's first week: you set a $\mathbb{P}$ number (1.5%) beside a $\mathbb{Q}$ number (3.0%) and sell protection because "the market is too scared." The gap is the premium you are paid to bear default in bad states, and it is not a mispricing. Two mechanical errors follow from it. If you drop the $\sqrt T$, the five-year $\text{PD}^{\mathbb{Q}}$ comes out at 10.0% and the CDS looks four points too wide. If you shift the CDS-implied 13.9% a second time, you get 24.4%, a double count that makes every bond look rich.

**If you got this wrong, read:** §6.3.1, Ines's napkin; §6.3.2, the Full Derivation and "What the shift does to a risky firm and a safe one"; §6.3.3 on the jump premium; §6.8.3, the credit triangle and "Forty percent recovery is a convention"; §6.9.1, the $\Pi_t$ ratio.

**Z.06.3: ROBO receives $\sigma_E=0.04$ for a CCC issuer**

**Answer:** These are the guards that should fire, in order:

1. **The input guard in `solve_kmv` (Listing 6.3).** It rejects any $\sigma_E$ outside 5%–300% with a `ValueError`, *before* `fsolve` runs. This is the one that fires.
2. **The post-solve bound $\sigma_V\in[1\%,300\%]$.** Without guard 1, this would raise a `RuntimeError` for any name whose equity is below roughly a third of its default point: $\sigma_V$ solves to 0.69% at $E/F=0.2$ and 0.95% at $E/F=0.3$. It passes at $E/F\ge0.4$ ($\sigma_V=1.18\%$), so treat it as a backstop. You cannot rely on it.
3. **Upstream, the spec's `sigma_frequency` field.** It should have said "daily" before the number reached the engine.

The `_d1d2` clamp at 0.0001 does *not* fire. The naive-DD fallback does not rescue you either, because it uses the same 4% and returns a PD of 0.07% at $E/F=0.2$. The message ROBO should print:

> ValueError: [issuer, as_of] sigma_E = 0.04 is outside [5%, 300%]. Is it annualized? If daily, 0.04 × √252 = 63.5%; if weekly, 0.04 × √52 = 28.8%. Check sigma_frequency on the vendor feed. No DD or PD written for this issuer.

Without any guard, the reported one-year PD is **0.00%**. In fact it is about $10^{-166}$ under $\mathbb{Q}$ for a CCC whose market cap is 20% of its default point, and below $10^{-144}$ for every equity-to-default-point ratio from 0.05 to 0.6. Annualize the same 4% as a daily figure (63.5%) and that balance sheet gives $\sigma_V=11.5\%$ and a $\mathbb{Q}$-PD of 5.9%.

**How:** The dangerous part is that the solver *converges*, with residuals around $10^{-15}$. As $\sigma_V\to0$ the call is worth its intrinsic value, $E_0\approx V_0-Fe^{-rT}$. Take $E_0=20$ and $F=100$: then $V_0\approx116.1$ and $\sigma_V\approx\sigma_E E_0/(N(d_1)V_0)=0.04\times20/116.1=0.69\%$, so

$$
d_2\approx\frac{\ln\!\big(1+E_0/Fe^{-rT}\big)}{\sigma_V}=\frac{\ln(116.08/96.08)}{0.0069}\approx27,\qquad N(-27)\approx10^{-166}.
$$

The numerator is positive for *any* positive equity, so $d_2\to\infty$ as $\sigma_V\to0$ on every balance sheet. That is why "any plausible CCC balance sheet" reports 0.00%. Through the desk's empirical DD map it would land in the safest bucket, an AA's default rate pinned on a CCC. That is the page for Mags's rating-agency file.

**The trap:** The usual wrong belief is that a bad input produces a failed solve and an error. It produces a clean, converged, fifteen-digit answer to the wrong question. The second wrong answer is "the fallback catches it," but the naive DD inherits the same $\sigma_E$. The third is accepting 4% as merely low. It is lower than the annual volatility of almost any listed stock, let alone a CCC's, which runs at 60% or more.

**If you got this wrong, read:** §6.1.3, "Annualize or die," and the `sigma_frequency` story; §6.11, Block 2, and "Edge cases ROBO must handle, in writing"; §6.4.3 on the empirical mapping; §6.12, item 2.

**Z.06.4: Covenants and uptiers as barrier mechanics**

**Answer:** **Covenant.** $V_0=8\times110=880$, the barrier is $K=(8/6)\times600=800$, and $x_0=\ln1.1=0.0953$. With zero log drift ($\mu=\tfrac12\sigma_V^2$ in `black_cox_pd`), the one-year breach probability is $2N(-0.381)=$ **70.3%**, matching §6.5.3. If you pass `mu=0` to `black_cox_pd` (zero drift in $V$), you get 73.6% instead.

**Uptier.** Under Merton with $T=3$, $r=4\%$, $\sigma_V=25\%$ and $V_0=880$ held fixed, the left-behind lenders' \$600mm falls from **\$514.5mm** to **\$465.0mm**. That is a loss of **\$49.5mm**, and with it their $\mathbb{Q}$-PD rises from 17.2% to 38.9% and their spread from 113 bp to 450 bp. The new \$200mm super-priority layer is worth \$177.4mm, almost riskless ($200e^{-0.12}=177.4$). With $V_0$ fixed, everyone beneath it pays for it: \$49.5mm comes from the left-behind lenders and \$127.9mm from the equity. So about \$49mm of the old lenders' value moved to the group that now ranks ahead.

**For Kaz: no.** In an open-market purchase, whoever sells gets the market price. The lenders who do not sell keep $\min(V_T,F)$, with the kink where it was (or lower, since less debt now sits beside them) and nothing new ahead of them. Here the left-behind diagram gained a dead zone from 0 to 200 and its kink moved from 600 to 800: the whole line slid \$200mm to the right. A purchase does not change the payoff of the holders who did not sell. A priming does, and this diagram is a priming.

**How:** The Black–Cox formula with $g=0$ and $T=1$ is

$$
\mathbb{P}(\tau\le1)=N\!\Big(\frac{-x_0-m}{\sigma_V}\Big)+e^{-2mx_0/\sigma_V^2}N\!\Big(\frac{-x_0+m}{\sigma_V}\Big)\;\xrightarrow{\;m=0\;}\;2N\!\Big(\frac{-0.0953}{0.25}\Big)=0.703 .
$$

In `black_cox_pd` (Listing 6.4), $m=\mu-\tfrac12\sigma_V^2-g$, so zero log drift means passing $\mu=0.03125$. For the uptier, write each claim as calls on the same $V$, with $C(K)$ the three-year Merton call from Listing 6.2:

$$
\underbrace{\min(V_T,600)}_{\text{before}}=V_T-(V_T-600)^+\;\Rightarrow\;V_0-C(600)=514.5,\qquad \underbrace{(V_T-200)^+-(V_T-800)^+}_{\text{after}}\;\Rightarrow\;C(200)-C(800)=465.0 .
$$

Value is conserved: $49.5+127.9=177.4=V_0-C(200)$. One extension worth knowing: suppose the \$177mm were real new money that stayed in the firm ($V_0=1{,}080$). The left-behind lenders would still lose about \$15mm (514 to 499), so priming moves value even when the cash is real.

**The trap:** For the covenant, there are two traps. One is the `mu=0` mistake above (73.6%). The other is using the Merton *terminal* probability, 35.2%, and forgetting that a monitored barrier roughly doubles it. For the uptier, the common wrong answer is pro-rata thinking: treat \$800mm as one class and give the old lenders three-quarters of it, $0.75\times(880-C(800))=\$481.8$mm, a loss of only \$32.7mm. That prices the new debt as pari passu. The whole point of the exercise is that it ranks ahead.

**If you got this wrong, read:** §6.5.2, the Math, Gently box and the three checks in the Full Derivation; §6.5.3, the loan's life from covenant to uptier, and the Docket Diary; Listing 6.4.

**Z.06.5: Mags's recovery**

**Answer:** Take a one-year contract quoted at 500 bp, with 4% flat discounting and quarterly coupons with accrual on default (Listing 6.6). The bootstrap gives **$\lambda=8.29\%$ at $R=40\%$** (the triangle says 8.33%) and **$\lambda=6.46\%$ at $R=23\%$** (the triangle says 6.49%). Both curves reprice the 500 bp quote to about $10^{-17}$. The upfront on a 100 bp standard coupon is $(s-c)\times\text{RPV01}$: **3.75 points at $R=40\%$** and **3.78 points at $R=23\%$**. Default pays **60 points versus 77**. The default payout is the number that changes when the name defaults tomorrow. The auction sets recovery, not the quoting convention, so if Mags is right the protection seller hands over 77 points, not 60. The jump-to-default is 17 points larger than a book marked at $R=40\%$ believes, while today's price barely moved.

**How:** A quote identifies only the product $\lambda(1-R)$, so the triangle gives $0.05/0.60$ and $0.05/0.77$. The bootstrap runs Brent on $\lambda$ until $\text{PV}_{\text{prot}}/\text{RPV01}=500$ bp. Coupons paid quarterly in arrears make the premium leg a little less valuable, so $\lambda$ lands just below the triangle. The upfront is

$$
U=(s-c)\cdot\text{RPV01}=0.04\times0.9363=3.75\ \text{pts}\quad(R=40\%),\qquad 0.04\times0.9447=3.78\ \text{pts}\quad(R=23\%).
$$

The two upfronts differ only because the annuities differ. A higher $\lambda$ means lower survival (92.0% against 93.7% at one year) and so a slightly smaller RPV01. At zero rates the upfronts are 3.84 and 3.87.

**The trap:** The most common wrong answer is "lower recovery is riskier, so the hazard goes up." For a *fixed* spread it goes down: each default costs more, so fewer defaults are needed to justify 500 bp. The arithmetic version of the same slip is dividing by $R$ instead of $1-R$, which gives $0.05/0.23=21.7\%$. A second trap is quoting the upfront as $5-1=4$ points and forgetting the RPV01. A third is believing a recovery change reprices the contract today. It reprices nothing until default, which is why you ship $R$ with every hazard curve.

**If you got this wrong, read:** §6.8.2 on the two legs and the upfront; §6.8.3, the bootstrap, the triangle, and "Forty percent recovery is a convention"; §6.6.3, "forty percent of what?"; Listing 6.6.

**Z.06.6: "A bankrupt company's equity is worthless."**

**Answer:** **$E_0=13.75\%$ of $F$**, which rounds to 13.8%. The rule of thumb gives 12% (the exact zero-rate value is 11.9%). The gap is the rate: at 4% the strike's present value is only $0.961F$, so the call starts about 4% of $F$ in the money on a forward basis. Adding roughly half of that to the rule gives 14.0%. The model being right about the value does not make the June 2020 trade good, for three reasons:

1. **Value is not price.** Merton says an at-the-money claim with a year until confirmation is worth something. It does not say that something is whatever the tape prints after a run of about 1,000% from \$0.59 to \$5.50.
2. **Look at who sold.** The most informed seller at the table, the company itself, offered shares under a prospectus saying they "could ultimately be worthless." Ines's markout reads that as a statement about information, not about value.
3. **Outcome is not decision.** The package that arrived (\$1.53 in cash, a share of 3% of the new company, warrants or rights) depended on a right-tail move in used-car prices and on plan sponsors choosing to pay creditors in full at a strike they negotiated. "The pot odds were terrible. The hand still hit." Post-petition equity after a 1,000% rally is, ninety-nine times in a hundred, the worst bet at the table. In Chapter 11 the strike is not fixed: the plan writes it, and Merton assumes it cannot.

**How:** With $V_0=F$, $\ln(V_0/F)=0$, so

$$
d_1=\frac{(r+\tfrac12\sigma_V^2)T}{\sigma_V\sqrt T}=\frac{0.04+0.045}{0.30}=0.2833,\qquad d_2=-0.0167,
$$

$$
\frac{E_0}{F}=N(0.2833)-e^{-0.04}N(-0.0167)=0.6115-0.9608\times0.4934=0.1375 .
$$

The rule of thumb is the zero-rate, at-the-money expansion: $E_0=V_0\big[N(\tfrac12\sigma_V\sqrt T)-N(-\tfrac12\sigma_V\sqrt T)\big]\approx\phi(0)\,\sigma_V\sqrt T\,V_0=0.399\times0.30\,V_0\approx0.12\,V_0$. Notice also that $N(-d_2)=50.7\%$. Under $\mathbb{Q}$ it is a coin flip whether equity finishes out of the money, and the call is still worth about a seventh of the debt.

**The trap:** One wrong answer is zero, the RSSG instinct that a filing means the strike has already been evaluated. Another is 12%, the rule of thumb without rates, which is Theo's number before Kaz corrects it. The deeper trap is concluding that because the model valued the claim correctly, buying it was correct. That mixes up a valuation with a price, and an outcome with a decision.

**If you got this wrong, read:** §6.2.1, "Payoff diagrams"; §6.2.3, the closed forms; §6.10.2, "Hertz: the hand that hit," and Ines's Poker Table box.

<!-- STATUS: COMPLETE -->
