## Chapter 23: Cross-Asset Convexity & the Volatility Surface

*Worked solutions. Numbers were recomputed from the chapter's equations and Listings 23.1–23.3. Inputs the exercise leaves open are stated as assumptions.*

**Z.23.1: ROBO targets volatility**

**Answer:** ROBO's target weight is $10\%/\sigma_E$. That is 21.7% of capital at $V = 150$, 13.7% at 100 and 8.5% at 75, a 61% cut in exposure. But ROBO never sells a share. The stock falls 86%, from 82.1 to 11.2, which shrinks the position faster than the target shrinks, so ROBO has to *buy*. Per \$100 of fixed risk capital the share count goes from 0.267 to 0.420 to 0.763. If it rebalances only at the three rows, with its losses flowing through NAV, the count goes 0.267, 0.364, 0.603. The sentence for the committee: *"The overlay sizes by equity vol, and equity vol is asset vol times leverage, so it always holds the same slice of the firm's asset risk (40% of NAV here); it has traded a call struck at the debt for a fixed slice of the assets, which makes it short exactly the convexity that sits at the fulcrum strike."*

**How:** The dollar vol of $n$ shares is $n\,\sigma_E E$, and (23.1) says $\sigma_E E = \sigma_V V N(d_1)$. To keep dollar vol at 10% of NAV,

$$
n = \frac{0.10\,\text{NAV}}{\sigma_V\, V\, N(d_1)} .
$$

Down the table the denominator falls from 37.5 to 23.8 to 13.1, so $n$ rises. The weight $nE/\text{NAV} = 0.10/\sigma_E$ falls only because $E$ falls faster than $n$ rises. With continuous rebalancing, $d\text{NAV} = n\,dE = n N(d_1)\,dV$, which gives $d\text{NAV}/\text{NAV} = (0.10/\sigma_V)\,dV/V = 0.4\,dV/V$, so $\text{NAV} \propto V^{0.4}$. From 150 to 75, NAV ends at $0.5^{0.4} = 75.8\%$ of where it started (a step-by-step simulation gives the same number). A power of 0.4 is concave in $V$, while the equity ROBO holds is convex in $V$, because it is a call struck at $F = 70$. Holding a constant mix is short gamma relative to holding the claim itself, and here that gamma sits at the debt strike.

**The trap:** Answering "ROBO sells 61%." That is the cut in the weight, mistaken for a trade. An investor who bought and held would see the weight fall further, to 3.7% of a NAV of 81.1, so measured against doing nothing ROBO is a buyer. It is a seller only against a constant-weight book, which would still hold 21.7%. That comparison is the one the committee sentence should make.

**If you got this wrong, read:** §23.1, "The Merton identity" (23.1) and "Sliding the assets down the table."

**Z.23.2: Chase the ghost**

**Answer:** Inputs: $\sigma_E = 40\%$, $F^{\text{ps}} = 30$, $\bar\ell = 0.5$, $\nu = 0.3$, $R = 40\%$, $r = 3\%$.

| | $S_0 = 5$, true model | $S_0 = 5$, (23.3) | $S_0 = 30$, true model | $S_0 = 30$, (23.3) |
| :-- | --: | --: | --: | --: |
| $1 - \mathcal{S}(0)$ | 13.4% | 25.0% | 0.007% | 0.013% |
| 1-year spread | 1,530bp | 2,306bp | 32.6bp | 32.7bp |
| 5-year spread | 555bp | 691bp | 161.0bp | 161.0bp |

The time shift moves the 1-year spread by more than 50bp once the stock falls below about **\$11.40**, which is $S_0/F^{\text{ps}} \approx 0.38$. For the 5-year spread the threshold is about \$7.05. At \$30 the approximation costs nothing. At \$5 it doubles the ghost and adds 776bp to the 1-year spread.

**How:** In the true model the barrier $L = \bar\ell F^{\text{ps}} e^{\nu Z - \nu^2/2}$ is drawn once, so the time-zero mass is exact:

$$
1 - \mathcal{S}(0) = N\!\Big(-\frac{\ln\big(V_0/\bar\ell F^{\text{ps}}\big) + \nu^2/2}{\nu}\Big),
$$

which is $N(-1.109) = 13.4\%$ at $V_0 = 20$. Conditional on $Z$, put $y = \ln(L/V_0) < 0$ into the known-barrier formula of Step 3: $\mathcal{S}(t \mid Z) = N\big(\tfrac{-\sigma_V^2 t/2 - y}{\sigma_V\sqrt t}\big) - e^{-y} N\big(\tfrac{-\sigma_V^2 t/2 + y}{\sigma_V\sqrt t}\big)$. Then integrate over $Z$. A Monte Carlo run with 200,000 paths, daily steps and the Brownian-bridge correction agrees: a ghost of 13.2% and $\mathcal{S}(1) = 0.795$, against 0.793 from quadrature. Put both survival curves through the same monthly legs of (23.5) and root-find for the stock price at which the gap is 50bp. The factor of about 2 in the ghost (25.0% against 13.4%, and $1.3\times10^{-4}$ against $0.7\times10^{-4}$) is the drunk's mirror at work. The time-shifted walk counts every path that touched the barrier during the hidden interval $[-\xi, 0]$, including the ones that walked back, while the true model counts only the ones that start below it.

**The trap:** Running Listing 23.1's `cg_survival_mc` and concluding that the approximation is exact. That routine simulates the *time-shifted* process, for which (23.3) is exact, so it agrees by construction. The other common slip is to redraw the barrier at every time step, which builds a different model, not CreditGrades.

**If you got this wrong, read:** §23.2, "The Full Derivation of (23.3)–(23.5)" (Step 2), the drunk-and-gutter Math, Gently box, and the Ways This Blows Up box on the time-zero ghost.

**Z.23.3: Trade the basis**

**Answer:** Assume Listing 23.2's chain settings ($S_0 = \$100$, $\sigma = 30\%$, $T = 1$, $r = 3\%$, $q = 0$, strikes \$10 to \$150) and the corridor $A = 0$, $B = \$20$. Then:

- From the puts: $U^{\text{opt}} = P(20)/20 = 0.05651$, on the `at_expiry` convention.
- From CDS at 250bp and $R = 40\%$: $\lambda = 4.167\%$, and the at-expiry claim is $U^{\text{CDS}} = 0.03960$.
- The basis is $\text{basis}_U = +0.01691$ per \$1 of claim. In spread units the puts imply $\lambda = 6.00\%$, or 360bp, so the basis is **+110bp**.

The put spread is *rich*, so you sell it and buy protection. With $A = 0$ that means selling 300,000 \$20 puts (3,000 contracts) against \$10mm of bought CDS. You collect \$339k of premium for a claim that CDS values at \$238k, an edge of \$101k in present value. If the stock bleeds into the corridor instead of jumping through it, the trade stops being default-neutral and becomes a naked short put. At $S_T = \$10$ with no credit event, the puts cost \$3.0mm and the CDS pays nothing.

**How:** Size the trade so the default payoffs match:

$$
n(B - A) = (1 - R)N = 0.6 \times \$10\text{mm} \;\Rightarrow\; n = 300{,}000 .
$$

At 20% of spot the diffusion part of (23.8) is about $10^{-9}$, so $P(20)/20$ is the floor $e^{-rT}(1 - e^{-\lambda T})$. The CDS claim on the same European timing is $e^{-rT}(1 - e^{-s T/(1-R)})$. To convert back to spread, use $\lambda = -\ln(1 - U e^{rT})/T$ and $s = \lambda(1 - R)$. The match holds in amount, not in timing: the CDS pays at $\tau$ and the puts pay at $T$. In a slow bleed the put pays $B - S_T$ on paths where the firm survives, so the corridor proof breaks at its first line ("before default, $S_t > B$"). The protection you bought gains mark-to-market as the spread widens, but a 1-year contract with no credit event expires worthless. GM drifted from 2005 to 2009 through every corridor you could have drawn. The extra 110bp may be exactly the market's price for that path.

**The trap:** Sizing $n = N/B = 500{,}000$ and forgetting $1 - R$. That over-hedges the default by 67%, leaving you net short \$4mm of default payoff. A close second is mixing conventions: the at-default CDS claim, 0.04021, gives a basis of about 104bp, and the 6bp difference is pure timing. Also check the sign before you act. §23.3's "buy the put spread, sell CDS" is the trade for a *cheap* put spread.

**If you got this wrong, read:** §23.3, "The CDS side" and "The signal," (23.6)–(23.7); §23.4, Ways This Blows Up ("American exercise").

**Z.23.4: Kaz and the prospectus**

**Answer:** It is not an arbitrage. Seniority binds in a liquidation, and a write-down clause acts before there is one.

*The override logic.* Any instrument whose terms contain a contractual write-down or conversion trigger gets `contractual_waterfall_override = True`. The flag has four consequences:

1. The instrument leaves CreditGrades and every other priority-ordered model.
2. The risk system refuses to net it against the same issuer's equity. There is no "seniority hedge."
3. Its jump-to-default is booked as the full face at zero recovery, in a trigger state that can come before, and apart from, an equity default.
4. It needs a trigger-probability input (distance to the CET1 trigger, the regulator, the odds of state support) in place of a barrier.

*The three prospectus fields.*

1. **Trigger definition:** the CET1 trigger level and the viability-event clause, including who makes the determination and whether extraordinary public support counts as a trigger.
2. **Loss-absorption mechanism:** write-down or conversion; full or partial; permanent or temporary; and the conversion price, if it converts.
3. **Conditionality and ranking:** whether the write-down requires equity to absorb losses first. Credit Suisse's did not.

*CreditGrades on 17 March 2023.* All inputs are illustrative: $S_0 = \text{CHF } 2.00$, $\sigma_E = 60\%$, debt per share CHF 35 excluding deposits, $\bar\ell = 0.5$, $\nu = 0.3$, $r = 1.5\%$, and a 9.75% AT1 priced as a 5-year bond to its call. The model says:

- a time-zero ghost of 56% and a 5-year default probability of 60%;
- CDS-equivalent spreads of about 7,900bp at 1 year and 1,790bp at 5 years;
- an AT1 fair value of **80** at $R = 40\%$, 68 at $R = 20\%$, and still **56 at $R = 0$** (about 50 even at $\sigma_E = 100\%$).

So CreditGrades tells Kaz that the AT1 at 40 is cheap, whatever recovery is typed in. It gives Sunday's outcome (AT1 at zero, equity at CHF 0.76) a probability of exactly zero. On the illustrative entry, Kaz's pair loses all 40 points on the long and makes CHF 1.24 a share on the short.

**How:** In (23.3)–(23.5), default is the asset value touching $\ell F^{\text{ps}}$. At that moment the equity is zero by construction and every debt claim receives its $R \ge 0$. To value the AT1, discount its coupons and principal at the CG survival probabilities, $\sum c\,e^{-rt}\mathcal{S}(t) + e^{-rT}\mathcal{S}(T)$, and add $R\big[1 - \mathcal{S}(0) + \int e^{-ru}(-d\mathcal{S})\big]$. The model has no state in which a junior claim keeps value while a senior one is zeroed. The viability clause creates exactly that state, and a regulator, not a diffusion, sets its strike.

**The trap:** Setting $R_{\text{AT1}} = 0$ and calling the model fixed. Even at zero recovery CG says 56, because its default event wipes out the equity first. What is wrong is the event, not the recovery number. Lowering $\nu$ for a financial, as the spec's override allows, *raises* the model value to 60 at $R = 0$, so the AT1 at 40 looks even cheaper.

**If you got this wrong, read:** §23.8, Case Study C and its Desk Myth box; §23.2, Ways This Blows Up ("Financials," "Two recoveries"); the bank-override spec at the end of §23.8.

**Z.23.5: Both legs, again**

**Answer:** On full revaluation the book loses about **\$0.59mm**; the Greeks say \$0.58mm. Day 1 (stock +18%) costs \$0.18mm and day 2 (spread +30%) costs \$0.41mm.

| Leg | Day 1 | Day 2 | Total |
| :-- | --: | --: | --: |
| Convertible: calls net of their own delta (gamma) | +\$50k | | |
| Convertible: stock hedge of the bond's credit delta | −\$113k | | |
| Convertible: bond floor | | −\$201k | |
| **Convertible leg** | | | **−\$264k** |
| CDS: short stock hedge | −\$117k | | |
| CDS: sold protection | | −\$206k | |
| **CDS leg** | | | **−\$323k** |

The only line with a plus sign is the convertible's long gamma. For Wolfspeed, the first flag you can date from public data is **the convertible floor**, on by 28 March 2025 at the latest, on a secondary report: the 2026s near 60 against a secured-curve floor of about 87. $z$ at \$2.59 comes out at about $-0.39$ to $-0.42$, which is inside Yu's lowest threshold and points the wrong way (buy the stock). These are single dated points under stated assumptions, not series: no free bond-price, CDS or option-surface history for Wolfspeed was found, so the put floor cannot be rebuilt.

**How:** The setup is Listing 23.3's \$30 name: $\sigma_E = 40\%$, $F^{\text{ps}} = \$30$, $R = 40\%$, $r = 3\%$, $T = 5$. That gives a CG spread of 161bp and $ds/dS = -4.96$bp per \$. The convertible is assumed: \$10mm face, a 2% coupon, and a bond floor of 88.24 at 161bp ($D^{\text{spr}} = 4.77$). The calls are on 266,667 shares struck at \$37.50, a 25% conversion premium, worth \$9.65 each with a delta of 0.643. The convertible's hedge is short $171{,}362 + 20{,}858$ shares. The second number is the bond's credit delta, $-D^{\text{spr}} B\, ds/dS$. `cg_greeks` puts the CDS hedge at short 21,589 shares, with an RPV01 of 4.35.

On day 1 the market spread does not move, although the model's falls to 137bp. Every share shorted against a *credit* delta (42,447 shares) loses \$5.40 and nothing comes back. On day 2, $\Delta s = +48$bp: the bond loses $D^{\text{spr}} B\,\Delta s$ and the protection loses $\text{RPV01}\cdot N\cdot\Delta s$.

In §23.6's decomposition, the CDS leg is convergence of −\$103k on day 1 (the gap widens 23.7bp) plus −\$206k on day 2 (48bp), and gamma of about −\$13k. The two legs are the same trade twice, long credit and short stock, so the hedges compound instead of offsetting.

*Wolfspeed:*

- Debt per share is $6{,}658.2/156.48 = \$42.5$ (10-K stack, old shares).
- Convert floor (assumed: a 1 May 2026 maturity, and the secured notes' 10-K mark of 85 on 29 June, a yield of 16.4%, standing in for the March curve): the 2026s' cash flows give about 87, against a market near 60 around 28 March (a secondary report).
- CG with $\sigma_E$ assumed at 80–120% and $R$ assumed at 27% (inside the plan's 25–30% range for the converts): at the January ATM price of \$7.20 it already shows a 25% ghost and 3,700–5,100bp at 1 year. At \$2.59 the ghost is 55% and the 1-year spread 9,400–10,000bp (8,700–9,200bp at the converts' own 1.09-year tenor).
- The converts at 60 imply about 5,300bp (flat hazard to maturity, $R = 27\%$), so $z \approx -0.39$ to $-0.42$ at the same tenor.
- The put floor needs OPRA history. Borrow would distort it as well: short interest was quoted at 64% in May 2025.

**The trap:** Letting the market spread follow the model on day 1. Do that and the CDS leg loses only its \$13k of stock-space gamma and the convertible looks hedged. May 2005's whole lesson is that the market spread did not follow the model. On Wolfspeed, the trap is trusting $z$ at $S/F^{\text{ps}} = 0.06$, far inside the zone where Z.23.2 shows the time-zero ghost dominates the spread.

**If you got this wrong, read:** §23.5 (the Natenberg map, (23.10), and Theo's whiteboard on JTD); §23.6, the P&L decomposition and "The Tape, and the Cards Graded"; §23.7, the Wolfspeed case note.

**Z.23.6: Three speeds**

**Answer:** About **68bp of software high-yield spread per 10% of software equity drawdown**: a 136bp gap over a 20% drawdown. Treat that as an upper bound; with technology HY at 340bp as the control, it is about 30bp. Over the full 20% drawdown that is +136bp, and at a spread duration of about 3 it forecasts a markdown of roughly **4 points** for a software loan book at 97.8, to about **93.8**, arriving a quarter or so behind high yield. If private spreads move half as much as public ones, the forecast is about 2 points, to 95.8. The assumption that would make the forecast wrong: that the equity drawdown is a *credit* event. If the low-strike put floor did not move, the fall is multiple compression on equity that sits well below the first lien, and senior marks have no reason to follow.

**How:** iCapital gives levels, not changes. Software HY was at 400bp against 264bp for broad HY, while software equities were down 20% year to date. Attribute the 136bp gap to the drawdown and you get 6.8bp per 1%. That only works if software HY traded flat to the index on 1 January, which is why the estimate is a ceiling. Cross-check with §23.9: Dynkin's +1% of equity momentum buys 5–8bp of next-month bond excess return. At an HY spread duration of about 3.5, that is only 14–23bp of spread per 10%, so part of the 136bp was there before January or built up over more than a month. For the loan, use (23.9) at the assumed spread duration of 3:

$$
\Delta P \approx -D^{\text{spr}}\,\Delta s\,P = -3 \times 0.0136 \times 97.8 \approx -4.0 .
$$

The lag is the three speeds of the Trend Watch: equity in days, public HY in weeks, private marks at the next quarter-end valuation. Before you publish the forecast, test whether the drawdown was about the tail: look at $\Delta\widehat\lambda^{\text{put}}$, the change in the put-floor hazard, in the regression.

**The trap:** Dividing the whole 400bp by the 20% drawdown, which gives 200bp per 10% and treats a level as a move. The other common one is marking the loan down by the spread move itself, 1.36 points, and forgetting spread duration.

**If you got this wrong, read:** §23.9 (the lead–lag regression, the Man annotation on valuation versus credit events, and the "three speeds" Trend Watch); §23.5, (23.9) for spread duration; Chapter 17 for how private marks are made.

<!-- STATUS: COMPLETE -->
