## Z.2-B Chapter 2-B: Transaction Cost Analysis for Credit: Arrival, Cover, Shortfall and the Dealer Scorecard

Six exercises, all short arithmetic with a judgment call at the end. None carries a [Read]/[Derive]/[Build] tag; each has a topical tag instead (benchmarks, shortfall, patience, leakage, legging, participation), so there is no [Build] exercise to extend Listing 2-B.1, though it reproduces three of the answers. The chapter prints a check value and a two-line solution for every one. All six check out; the full versions below add the reasoning, the units and the usual wrong turn. One exercise title disagrees with its own data (Z.2-B.5). Everything here is realized, physical-measure arithmetic in basis points of price (cost positive, bad for us) or dollars; no risk-neutral pricing appears.

**Z.2-B.1: One sale, four benchmarks** *[benchmarks]*

**Answer:** In basis points of price, cost positive, the \$3mm sale at 94.10 costs $+21.2$ against arrival (94.30), $+15.9$ against the RFQ-time mid (94.25), $-10.6$ against the cover (94.00) and $-21.3$ against the next print (93.90). In dollars that is \$6,000, \$4,500, $-\$3,000$ and $-\$6,000$. The router is judged against the RFQ-time mid: $+15.9$ bp, \$4,500. The 5.3 bp between it and arrival (\$1,500) is the delay, a process cost that belongs on its own line.

**How:** A sale has $\eta = -1$, so the cost is $-(p - b)/b \times 10^4$ with $p = 94.10$:

$$
\frac{0.20}{94.30} = 21.2, \qquad \frac{0.15}{94.25} = 15.9, \qquad \frac{-0.10}{94.00} = -10.6, \qquad \frac{-0.20}{93.90} = -21.3 \text{ bp}.
$$

Each benchmark answers a different question. Arrival is the price of the decision, so it charges the whole path from signal to fill. The RFQ-time mid is the market at the door, so it forgives the delay and keeps the dealer's concession, which is what a router controls. The cover is the second-best bid, below the winner's by construction, so for a seller it can only come out negative; it measures how spread out the dealers were, not what you paid. The print says the market fell after you sold, so $-21.3$ is a favourable markout, not a saving, and one print is not a verdict. The first row minus the second, $21.2 - 15.9 = 5.3$ bp, is the $0.05$ the mid slid between `NEW` and `ROUTED`. I checked all four with `benchmarks_bp` in Listing 2-B.1 (`side = -1`). One more thing worth a look: 21.2 bp against arrival is above even the stress-day \$1–5mm bucket in §2B.5 (17.5 bp), so this ticket deserves a second glance, though a single fill is a draw, not a rating.

**The trap:** The sign. Feed a sale through the buy formula and you get $-21.2$, $-15.9$, $+10.6$, $+21.3$: the router "saved" 16 bp and the cover looks like a cost. The runner-up is answering "arrival" to the router question, which bills the router for 5.3 bp of waiting it did not choose, or crowing about $-10.6$ against the cover, which is Mags's "not one losing week" in miniature: a definition, not an achievement.

**If you got this wrong, read:** §2B.1.1 (Four prices, four counterfactuals), then §2B.1.3 (The cover is a survivor).

**Z.2-B.2: A shortfall with a hole in it** *[shortfall]*

**Answer:** The executed part is \$12,000: delay \$3,000, drift while quoting \$1,800, half-spread \$7,200. The unfilled part is \$36,000: beta \$12,000 and IDO \$24,000. The total is \$48,000 (about 48 bp of the \$10mm target), and three-quarters of it sits in the \$4mm that never traded. Units: dollars from face in \$mm and prices in points per 100; realized moves, physical measure.

**How:** Perold's shortfall is the paper portfolio minus the real one. Paper buys the full \$10mm at the arrival mid; real buys \$6mm at the fill price; both are marked at the retry mid $m_T$, which here is the 101.90 at which the remainder is abandoned (I read it as a mid). That gives

$$
\text{IS} = \underbrace{\tfrac{1}{100}\sum_k x_k\,(p_k - m_{\text{NEW}})}_{\text{executed}} + \underbrace{\tfrac{1}{100}\Big(X - \sum_k x_k\Big)(m_T - m_{\text{NEW}})}_{\text{opportunity}} .
$$

The filled piece telescopes along the log's stamps: $p - m_{\text{NEW}} = 0.20 = 0.05 + 0.03 + 0.12$ points, so \$6mm $\times$ each over 100 is \$3,000, \$1,800 and \$7,200. The unfilled \$4mm moved $101.90 - 101.00 = 0.90$ points, of which $0.30$ is the predicted market part and $0.60$ is what is left, so \$12,000 and \$24,000. The filled bonds are marked at the fill, not at $m_T$, because paper and real both own them from then on. `shortfall` in Listing 2-B.1 returns exactly these five lines. Leave out `m_end` and it returns \$12,000 with the flag `unfilled_unmarked`, which is the listing refusing to let zero stand in for "we did not look."

**The trap:** Reporting \$12,000, the number an execution report built from fills would print. It is a quarter of the truth, and it is Wednesday's nine bonds all over again: the unfilled line is the biggest one and it is not in anybody's column. Other slips: applying the 0.90 to the whole \$10mm (\$90,000), or calling the whole \$36,000 "adverse selection" when a third of it is beta that an index trade could have hedged.

**If you got this wrong, read:** §2B.2, including The Full Derivation; §3.3.3 for stripping beta before calling the rest idiosyncratic.

**Z.2-B.3: Is patience worth it?** *[patience]*

**Answer:** Accept the first quotes. Rejecting is worth $0.4 \times 10 = 4$ bp in expectation; two days of waiting costs the signal $80\,(1 - 2^{-2/20}) = 5.36$ bp, so patience loses about 1.4 bp. The answer flips at a half-life of $h = 2/\log_2(1/0.95) \approx 27.0$ days: a slower signal rewards waiting, a faster one does not. At 20 days you are on the accept side. Units: bp of price, trading days, an expected (physical-measure) decay.

**How:** A signal worth 80 bp now is worth $80 \cdot 2^{-t/h}$ after $t$ days, so waiting two days forfeits

$$
80\,\big(1 - 2^{-2/h}\big) \text{ bp}.
$$

The gain from rejecting is the probability of a later trade times the improvement, $0.4 \times 10 = 4$ bp, and the other 60% is treated as no better (the chapter's own simplification). Set the two equal: $1 - 2^{-2/h} = 0.05$, so $2^{-2/h} = 0.95$ and $h = 2/0.0740 = 27.0$ days. Same trade-off as the chapter's two books: the value sleeve (60 bp, 45 days) loses 1.8 bp to two days and should be patient; the event signal (40 bp, 3 days) loses 14.8 bp and should not. The margin here is 1.4 bp against inputs ("about 10 bp", "about 40%") that are each rougher than that, so this is a lean, not a law. And the simplification flatters patience: if the 60% never trades, the signal's decay is a real loss on top.

**The trap:** Reading "10 bp better" as a sure thing. Ten beats 5.4, so you reject, and you have priced a 40% chance as a certainty. The other slip is treating 20 days as the e-folding time instead of the half-life: $80(1 - e^{-2/20}) = 7.6$ bp and a break-even near 39 days. The verdict stays "accept," but the flip point is out by $1/\ln 2$.

**If you got this wrong, read:** §2B.2, the paragraph headed "The patience premium."

**Z.2-B.4: A placebo that cannot help** *[leakage]*

**Answer:** The leak is $2.4 - 1.9 = 0.5$ bp of price against the desk at a hundred minutes, with a standard error of 0.72 bp and $t \approx 0.69$. That is nothing you can tell from zero (a 95% interval of about $-0.9$ to $+1.9$ bp). No number of placebos gets the standard error to 0.25 bp: the sent sample alone contributes 0.40. Even with unlimited placebos you would need $(12/0.25)^2 = 2{,}304$ sent orders, 2.6 times what you have; at the desk's 900-to-400 mix it is about 7,500 sent and 3,300 placebos. Units: bp of price, signed so positive is against the desk; physical measure.

**How:** The sent and placebo means are independent, so their variances add:

$$
\text{SE} = \sqrt{\frac{12^2}{900} + \frac{12^2}{400}} = \sqrt{0.16 + 0.36} = 0.72 .
$$

Sending more placebos shrinks only the 0.36 term. Let $n_p \to \infty$ and the SE bottoms out at $12/\sqrt{900} = 0.40$, still above 0.25, so the only lever is more sent orders, which is to say more months of trading. The chapter's own example (4,600 sent, 2,300 placebos, s.d. 10) lands at 0.26 for the same reason. Two honest caveats. This SE treats orders as independent, but orders in the same bond or on the same day share their drift, so the true SE is larger. And the placebo is itself a selected sample (§2B.3), so the 0.5 is an estimate of the leak plus whatever made a trader hold those orders back.

**The trap:** Quoting 2.4 bp as "the leak." That is the cold, not the medicine: 1.9 of those 2.4 bp is what unsent orders did anyway. The second slip is reading $t = 0.7$ as "no leak." It says this sample cannot tell 0.5 bp from zero, not that the dealers are clean. Nobody gets cut on one print, or on one t-statistic.

**If you got this wrong, read:** §2B.3 (The Leakage Test), especially the Math, Gently box on the sugar pill.

**Z.2-B.5: Ninety minutes on one leg** *[legging]*

**Answer:** The 45-minute window has a one-standard-deviation dollar P&L of about \$42,500 unhedged and about \$28,100 with a CDX bridge correlated 0.75 with the leg. These are physical-measure standard deviations of P&L over the window, in dollars. If you take the title at its word and use 90 minutes instead, the numbers are about \$60,000 and \$39,700 (see the NOTE).

**How:** DTS of 50,000 means \$50,000 of P&L per 1% relative spread move, and a day's standard deviation of relative moves is 2.5%, so a full day's standard deviation is $50{,}000 \times 2.5 = \$125{,}000$. Variance accrues linearly in time, so a 45-minute window out of a 390-minute session carries $45/390$ of a day's variance and $\sqrt{45/390} = 0.340$ of its standard deviation:

$$
\sigma_{\text{window}} = 50{,}000 \times 2.5 \times \sqrt{45/390} \approx \$42{,}460 .
$$

A bridge hedge removes the part of the risk it is correlated with. Sized at the minimum-variance ratio (§8.6's regression), the residual variance is $(1 - \rho^2)$ of the original, so the residual standard deviation is $\sqrt{1 - 0.75^2} = 0.661$ of the unhedged one: \$28,085. A 0.75 correlation removes only about a third of the standard deviation (56% of the variance). If both legs have the same relative volatility, that minimum-variance bridge carries $0.75 \times 50{,}000 = 37{,}500$ of DTS, less than a DTS-matched hedge; matching the full 50,000 would leave $\sqrt{2(1 - 0.75)} = 0.71$ of the risk, about \$30,000. `legging_sd(50000, 45, 0.025, rho_bridge=0.75)` in Listing 2-B.1 returns 28,085.

**The trap:** Scaling a day's risk linearly with time: $125{,}000 \times 45/390 = \$14{,}400$, a third of the truth. Variances add over time; standard deviations scale with the square root. On the hedge, the common slips are leaving out the square root ($1 - \rho^2$ times the unhedged figure gives \$18,600) or using $1 - \rho$ ($\$10{,}600$). Neither is a standard deviation of anything.

**If you got this wrong, read:** §2B.7 (the Math, Gently box on legging risk); §8.6 for the residual variance of a partial hedge; §8.4 for DTS.

NOTE (for the editor): This exercise is titled "Ninety minutes on one leg," but the text says the long leg fills "45 minutes before the short," and the chapter's check (\$42,500 and \$28,100) uses 45. The 90 comes from the April PB-01 opening in §2B.7, where the pod was one-legged from 9:50 to 11:20. At 90 minutes the same inputs give \$60,048 unhedged and \$39,718 with the 0.75 bridge. The check values are right for 45 minutes; the title should say "Forty-five minutes" or the text should say 90.

**Z.2-B.6: The mirror and the moving denominator** *[participation]*

**Answer:** The like-for-like participation is $19.0\% \times 0.94 \approx 17.9\%$, on the old, duplicate-inclusive tape the 20% line was drawn on. Equivalently, the line on the new tape is $20\%/0.94 = 21.3\%$, and 19.0% sits 2.3 points under it. Before anyone says "we are the market," the detector also needs residualised markouts turning against the desk and response counts falling in the sleeve's bonds. It fires only on all three. Units: share of TRACE dollar volume in the sleeve's bonds.

**How:** Participation is the desk's volume $V_d$ over TRACE volume $V_T$. The affiliate indicator removed 6% of the old volume, so $V_T^{\text{new}} = 0.94\,V_T^{\text{old}}$ and the number printed is inflated:

$$
\frac{V_d}{V_T^{\text{new}}} = \frac{1}{0.94}\cdot\frac{V_d}{V_T^{\text{old}}} \quad\Longrightarrow\quad \frac{V_d}{V_T^{\text{old}}} = 0.94 \times 19.0\% = 17.9\% .
$$

The answer is robust to the size of the cut: at FINRA's 5.7% baseline it is 17.9%, at MarketAxess's "up to 8%" it is 17.5%. In practice you do not rescale by hand but carry a break dummy at 31 August 2026 (and one waiting at 2 August 2027) in the series and refit capacity on it. Listing 2-B.1's `participation` returns the raw ratio and the dummies, and `we_are_the_market` takes the adjusted series plus the two trends, so the markout and response-count conditions are inputs you must supply, not things the ratio can stand in for.

**The trap:** Adjusting in the wrong direction. Dividing, $19.0\%/0.94 = 20.2\%$, puts the sleeve "over the line," which is the right calculation run backwards (it is how the chapter turns 18.6% into 20.2%, old to new). The tape got smaller on paper, so the printed ratio is too high and you shrink it. Subtracting six points (13%) is the other common slip: the cut is a fraction of the denominator, not points of participation.

**If you got this wrong, read:** §2B.6 (Capacity From Your Own Fills), then §4.8 for where the 20% line comes from.

NOTE (for the editor): §2B.6 concludes that "nearly all of Mags's jump was the market getting smaller on paper," using an 8% cut: $18.6\% / 0.92 = 20.2\%$, which is 1.6 of the 1.7 points observed (95%). But 8% is the top of MarketAxess's "up to 8%" for June 2026, and FINRA's own baseline is up to 5.7% (in trades, not dollars). At 5.7%, 18.6% becomes 19.7%, only 1.1 points or 66% of the jump, and September's like-for-like reading is 19.1%, not 18.6%. "Inflated by up to 8%" can also mean reported volume was 1.08 times true, which is 7.4% removed and gives 20.1%. Consider "most of" in place of "nearly all," or say which reading of the 8% is used.

<!-- STATUS: COMPLETE -->
