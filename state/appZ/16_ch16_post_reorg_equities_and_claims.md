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

**Z.16.3: Four legs of the seat**

**Answer:** In expectation, and in \$mm on the \$500mm raise:

| Leg | Value | Share of the raise |
| :-- | --: | --: |
| Fee, paid in shares | +62.9 | 12.6% |
| Reserved allocation at a discount | +25.7 | 5.1% |
| Exclusivity option | +16.7 | 3.3% |
| The put | −10.5 | −2.1% |
| **All-in** | **+94.8** | **19.0%** |

The fee is the largest leg by a wide margin. Give it a 60% chance of surviving and it is worth \$37.7mm, still the largest, and the all-in falls to \$69.6mm (13.9%). A court can reach the fee directly. It can reach the reserved allocation and the exclusivity option only by opening the seat to the whole class, which spreads them pro rata rather than deleting them. It cannot reach the put, which is market risk borne by whoever sits in the seat. Nor can it reach the rights' own discount, which every holder already gets on equal terms.

**How:** Normalize $x_0 = 1$, so $K = 0.7$ and $m = 500/0.7 = 714.3$. A dilution factor of 0.6 makes $N_{\text{eff}} = 0.6\,m = 428.6$ and $S^{\text{post}} = 0.6\,x + 0.4\,K$. Under the chapter's driftless $\mathbb{P}$-lognormal, $\mathbb{E}[x] = 1$, so $\mathbb{E}[S^{\text{post}}] = 0.88$. The two linear legs then need no option model: the fee is $0.10 \times 714.3 \times 0.88$ and the reserved slice is $0.20 \times 714.3 \times 0.6\,(1 - 0.7)$. The other two legs use Block 2's `bs_call` and `bs_put` at $\sigma = 0.65$, $T = 0.3$ and zero rate:

$$
C_{\text{BS}}(1, 0.7) = 0.3245, \qquad \text{Put}(1, 0.7) = C - (x_0 - K) = 0.0245 .
$$

Then the exclusivity option is $0.8 \times 0.15 \times 714.3 \times 0.6 \times 0.3245 = 16.7$ and the put is $-428.6 \times 0.0245 = -10.5$, which is exactly the fair fee $f^{*} = 2.1\%$ of the raise. A million-path Monte Carlo (seed 16) matches every leg within \$0.05mm. So the seat is paid 10% for insurance worth 2.1%. Because it is paid in shares worth 0.88 rather than 0.70, the fee is really 12.6%: six times the put on its own, before the reserved slice and the exclusivity option are even counted.

**The trap:** Valuing the fee at cash, $f\,m\,K = \$50$mm. It is paid in shares, each worth $S^{\text{post}}$, not $K$. The runner-up is believing the chapter's Desk Myth that the fee is the smallest leg (see the note). The third is applying the 60% only to the fee and calling the seat "fixed". The reserved slice and the exclusivity option ride on the same exclusive seat.

NOTE (for the editor): §16.3.3's Desk Myth ("The fee is the smallest of four legs") and the Debrief's fourth sentence ("the fee is its smallest leg") contradict this exercise, where the fee is the *largest* leg and the put is the smallest in absolute value. They also contradict the chapter's own 25%/70%/six-month case. There the fee in shares is about $0.10 \times 0.91 = 9.1\%$ of the raise, against a put of 6.3%, and the reserved slice would beat the fee only if more than about 57% of the offering were reserved. The sentence probably means "the put (the fair fee) is the smallest leg." Separately, the $\Pi^{\text{BP}}$ formula charges the put on all $m$ shares, $-N_{\text{eff}}(K - x)^{+}$. The reserved slice's downside, though, is already in the linear second leg, so the put should be $-(1-a)\,N_{\text{eff}}(K-x)^{+}$. Here that gives a put leg of \$8.4mm, not \$10.5mm, and an all-in of \$96.9mm, not \$94.8mm. Our table follows the formula as printed.

**If you got this wrong, read:** §16.3.2 ("The all-in transfer" and the fair-fee derivation), the *ConvergeOne* bullet in §16.3.2's Trend Watch, and Listing 16.2 in Appendix F.

**Z.16.4: Kaz's funeral, formally**

**Answer:** The call is strictly increasing in the rate, so $C_{\text{BS}}(r + \lambda) > C_{\text{BS}}(r)$ for any $\lambda > 0$. At the Hertz inputs ($S = 10$, $K = 13.80$, $T = 30$, $r = 2\%$, $\sigma = 52\%$, $\lambda = 2\%$), the correct jump price is \$9.03, the no-jump call is \$8.66 and Kaz's haircut price is \$4.75. The going-concern spot that makes Kaz right is

$$
S^{\text{GC}} = S\,e^{\lambda T} = 10\,e^{0.6} = \$18.22, \qquad S^{\text{GC}}/S = 1.82,
$$

whatever $\sigma$ and $K$ are. In one sentence: the \$10 on the screen already prices the second Chapter 11; it is an \$18.22 value-if-Hertz-survives-to-2051 times the 55% chance it does, so Kaz's haircut belongs only on a DCF that assumes survival, and that DCF would sit 82% above the screen.

**How:** The rate sensitivity is

$$
\frac{\partial C_{\text{BS}}}{\partial r} = K\,T\,e^{-rT}\,\Phi(d_2) > 0,
$$

which is 21.0 at these inputs. Raising the rate shrinks the present value of a strike that is paid only at expiry. By the mean value theorem, any $\lambda > 0$ gives a strict increase. For the spot, put $S' = S\,e^{\lambda T}$ into Kaz's price. Then $\ln(S'/K) = \ln(S/K) + \lambda T$, so $d_1'$ and $d_2'$ are exactly the $d_1$ and $d_2$ of the call at rate $r + \lambda$, and

$$
e^{-\lambda T}\left[S e^{\lambda T}\Phi(d_1) - K e^{-rT}\Phi(d_2)\right] = S\,\Phi(d_1) - K e^{-(r+\lambda)T}\Phi(d_2) = C_{\text{BS}}(S, K, T, \sigma, r + \lambda).
$$

Kaz's price rises with $S'$, so this root is the only one, and `brentq` returns 18.2212 at 52%, 53.0% and 51.6% volatility alike. In words: a pre-default stock that drifts at $r + \lambda$ from \$10 reaches the same forward as a stock that never dies and drifts at $r$ from \$18.22.

**The trap:** Solving numerically at one volatility and reporting \$18.22 as if it were a fact about Hertz's volatility. It is a fact about survival alone: $e^{\lambda T}$. The bigger trap is Kaz's own, believing a jump to zero must make a call cheaper. That holds only when the spot ignores the jump. A market spot has already paid for the funeral, and with the dilution fixed point of Listing 16.3 the ordering survives: \$8.97 with the jump, \$8.56 without, \$4.70 haircut.

**If you got this wrong, read:** §16.4.2 ("The jump to zero" and *The Full Derivation*), with Chapter 6, §6.1.4 for the memoryless default clock.

**Z.16.5: The boat and the truck**

**Answer:** Vendor A, the boat, holds the 503(b)(9) claim. Vendor B, the truck, holds a general unsecured claim. We assume clean paperwork ($p_A = 1$) and no administrative insolvency, since the exercise gives neither. On those assumptions Block 4 prices A's claim at $0.926$ per dollar (\$1.852mm on \$2mm) and B's at $0.393$ (\$0.787mm). The slower ship was worth **\$1.07mm**, a little over half the invoice. Using the listing's own illustrative allowance and insolvency inputs (0.97 and 0.95; 5% times 50%) instead, the gap is \$1.00mm.

**How:** Under *World Imports*, goods are "received" when the debtor takes physical possession, not when title and risk pass at a foreign port. A's container was unloaded 18 days before the petition, inside the 20-day window. B's truck was unloaded 22 days out, outside it. Both claims share the timing factor

$$
\frac{h}{h + r + \psi} = \frac{1.5}{1.5 + 0.04 + 0.08} = 0.9259 .
$$

The 503(b)(9) claim is paid in full in cash on the effective date (§1129(a)(9)(A)), so its price is the timing factor alone. The GUC multiplies the timing factor by the random-pool recovery

$$
\mathbb{E}[R] = \Phi\!\left(\frac{\mu_Y}{s_Y}\right) + e^{\mu_Y + s_Y^2/2}\,\Phi\!\left(-\frac{\mu_Y}{s_Y} - s_Y\right) = 0.0044 + 0.4253 \times 0.9883 = 0.4247,
$$

with $\mu_Y = \ln 0.4$ and $s_Y = 0.35$. That gives $0.9259 \times 0.4247 = 0.3933$. Notice $0.4247 > 0.40$: this class sits deep on the impaired side of the kink, where pool uncertainty is a small gift.

**The trap:** Following the bill of lading. Title passed to the retailer 25 days out, so A "must" be outside the window, and B, at 22 days, looks only slightly late. Both readings swap the contract for the dock: the statute asks when the debtor *held* the goods. On the pricing side, the usual slips are to use $e^{\mu_Y} = 0.40$ as the recovery, which ignores Jensen's 2.5 points, or to discount at the mean wait, $e^{-0.12/1.5} = 0.923$ rather than $h/(h + r + \psi) = 0.926$. Together those slips give \$0.739mm for the GUC.

**If you got this wrong, read:** §16.5.2 (the statute block: the loading dock and §1129(a)(9)(A)), §16.5.3 ("Pricing the claim" and the closed form for $\mathbb{E}[R]$), and Listing 16.4 in Appendix F.

**Z.16.6: Short a call, paid nothing**

**Answer:** The call the customer wrote, on 1.2 BTC struck at the petition-date \$17k for 2.5 years at 60% volatility, was worth **\$7,441** at a zero rate ($1.2 \times \$6{,}201$), or \$8,094 at 4%. That is 44% of the \$17k claim. A claims buyer at 15 cents paid \$2,550 for the *whole* claim, so the call alone was worth 2.9 times the buyer's price, and the buyer turned \$2,550 into \$20,400 in cash, eight times the money. The customer was the one short volatility. Dollarization made him write the call, and selling at 15 cents also sold the estate's recovery, which the crypto rally was about to lift. The buyer was long that recovery, so in substance he held the long side of the customer's option, capped at par plus interest.

**How:** Compare the cash the customer gets with what 1.2 BTC in kind would pay. By put-call parity,

$$
1.2 \times 17{,}000 = 1.2\,A_T - 1.2\,(A_T - 17{,}000)^{+} + 1.2\,(17{,}000 - A_T)^{+},
$$

so the dollar claim is long 1.2 BTC, short 1.2 calls and long 1.2 puts at the petition price. With $\sigma\sqrt{T} = 0.949$ and zero rate, $d_{1,2} = \pm 0.474$ and $C = 17{,}000\,[\Phi(0.474) - \Phi(-0.474)] = \$6{,}201$ a coin (`bs_call` from Listing 16.2). At the money and at zero rate the put is worth the same \$7,441. The customer's protection came from the estate, though, and the estate's assets were largely the same crypto. So the put was weakest exactly when it would have paid, which is the wrong-way risk the 15-cent print was pricing, while the call was given away in full. Ex post, \$20,400 against a coin near \$100k is the chapter's 20.4% in-kind recovery.

**The trap:** Valuing the call with hindsight, at $1.2 \times (100{,}000 - 17{,}000) = \$99{,}600$. That is the realized cost of the option the customer wrote, not its value on the day it was written. The smaller slips are pricing one coin instead of 1.2 (\$6,201), or putting a \$20.4k strike on one coin (\$5,237). Both confuse the 120% payout with the 1.2-coin notional.

NOTE (for the editor): §16.5.3 says the dollarized claimant is "short a call on the asset, struck at the petition-date price, and was paid nothing for it." Against a solvent payer that is not quite right: dollarization also hands the claimant a put at the same strike, and at zero rate the at-the-money call and put are both worth \$7,441, so the swap would be fair. It is "paid nothing" because the put was written by an insolvent estate holding the same asset. Suggest adding a clause such as "except a put written by an estate holding the same asset."

**If you got this wrong, read:** §16.5.3 ("Denomination risk"), the Trend Watch "Claims trading went crypto, 2023–2026" that follows it, and §16.3.2's *The Full Derivation* for the Black–Scholes arithmetic.

<!-- STATUS: COMPLETE -->
