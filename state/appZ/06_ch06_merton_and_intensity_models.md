## Z.06 Chapter 6: Stochastic Calculus, Intensity Models & Structural Frameworks

Eight exercises: the two warm-ups, A and B, and the six numbered ones. I recomputed every number in Python. Where an exercise names an engine function, I ran it from Appendix F, Listings 6.1–6.7, seeded `default_rng(42)`. None of the chapter's exercises carries a [Read]/[Derive]/[Build] tag, so none appears below.

**Z.06.A: Warm-up A, the holdco at 40**

**Answer:** (a) Outside the bank, the holding company has $\$2{,}258+491+896+577=\$4{,}222$mm of assets against $\$3{,}370+305=\$3{,}675$mm of liabilities. Book recovery is therefore **1.15 per dollar (115%) with the cash** and $\$1{,}964/\$3{,}675=$ **0.53 (53%) without it**. The notes at 40 were pricing the no-cash world. They actually sat 13 points *below* it, a discount for time, fees, and claimants who had not filed yet. (b) A twelve-point gap implies a reinstatement probability of $12/17\approx$ **71%, "roughly 70%."**

**How:** For (a), add up the four non-bank assets and divide by the two liabilities. Then remove the cash, because a bank holding company keeps its cash at its bank, and from noon on 10 March that cash was a deposit claim on a receivership. For (b), use two states. With probability $p$ the bonds are reinstated (2025s worth 97, 2031s worth 80). Otherwise both pay the same liquidation value $L$ per dollar of claim:

$$
P_{25}=97p+L(1-p),\qquad P_{31}=80p+L(1-p)\;\Longrightarrow\;P_{25}-P_{31}=17p=12,\quad p=0.706 .
$$

The unknown $L$ cancels, and that is the whole trick: the *gap* identifies the probability without your knowing the recovery. I checked the reinstatement values. Priced at a 5% yield from 25 April 2023, a 3.50% note maturing January 2025 is worth 97.5 clean and a 1.800% note maturing February 2031 is worth 79.6, so 97 and 80 are fair. A low coupon kept to a long maturity is worth less when the market yields 5%.

**The trap:** In (a), the trap is the 115%: you read "par is in there" and buy at 40. That is Theo's first answer, before Mags asks where a bank holdco keeps its cash. In (b), the trap is to read the gap as an arbitrage between two identical claims. They are identical only in liquidation. The market was pricing a second state in which they are not.

**If you got this wrong, read:** §6.4.4, Beat 4 and "Decision point: the holdco at 40" (with Figure 6.4), then Beat 5, "the same claim at two prices."

NOTE (for the editor): The gap arithmetic agrees with the check (70.6%). The inputs, though, are not consistent with the levels. Fit both prices with $p=12/17$ and the implied liquidation value is $L=(69-0.706\times97)/0.294\approx1.8$ cents for *both* bonds. That contradicts part (a)'s 53% no-cash coverage and the 30s–40s trading levels of March. At $L=40$ the two levels imply $p=51\%$ (2025s) and $p=43\%$ (2031s), not one common $p$. A reader who checks the levels will be confused. One option is to add "use only the gap; the two-state model is not meant to fit the levels." Another is to adjust the reinstatement values.

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

