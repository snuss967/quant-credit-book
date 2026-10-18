## Chapter 28: What a Desk Head / Senior PM Must Know to Extract Maximum Alpha

Five exercises, one per clause of Theo's term sheet: the band, the sizing, the runway, the error bars on the band, and the stop. Every number below was recomputed in Python from the chapter's inputs and Listings 28.3 to 28.6 (Appendix F). Write your card before you read ours.

**Z.28.1: The empty band**

**Answer:** At $r_{\min} = 5\%$ and the 2008 multiple ($m = 5.8$), the band has room only if $\overline{\text{LCS}} \le 0.33\%$ (exactly 0.329%; at that point floor and ceiling meet at 3.16). At the March 2020 multiple ($m = 3$) the limit would be 0.79%. With no liquidity charge, and the per-bet IR held at $2/\sqrt{40} = 0.316$, the band opens at $N_{\text{eff}} = 25.6$, where $\text{SR} = 1.6$. Adding names cannot rescue a band that liquidity has closed. With SR rising like $\sqrt{N_{\text{eff}}}$, the floor stays at 3.16 however many names you add, and the ceiling can only climb toward the speed limit $2\,\text{DD}_{\max}/((m-1)\overline{\text{LCS}})$. At $\overline{\text{LCS}} = 0.8\%$ that limit is 3.91, so on paper the band reopens. It does so only at $N_{\text{eff}} \approx 97$ with $\text{SR} \approx 3.1$, which is the $1/\rho_a = 100$ breadth ceiling of §28.2. Above $\overline{\text{LCS}} = 0.99\%$ the speed limit sits below the floor, and no number of names reopens the band.

**How:** Write the ceiling (28.23) as $G_{\max} = \text{DD}_{\max}/(c_1 + 1/A)$, with $1/A = \sigma_{\text{DTS}}(\kappa z_p - \text{SR})/\sqrt{N_{\text{eff}}}$ and $c_1 = \tfrac12(m-1)\overline{\text{LCS}}$. The floor is $F = \sqrt{N_{\text{eff}}}\,r_{\min}/(\sigma_{\text{DTS}}\text{SR})$. The band exists if and only if $c_1 \le \text{DD}_{\max}/F - 1/A$:

$$
c_1 \le \frac{\sigma_{\text{DTS}}}{\sqrt{N_{\text{eff}}}}\left[\frac{\text{DD}_{\max}\,\text{SR}}{r_{\min}} - (\kappa z_p - \text{SR})\right] = 0.00791\,(3 - 2) = 0.79\%,
$$

so $\overline{\text{LCS}} \le 0.79\%/2.4 = 0.33\%$. For the second part, set $\text{SR} = \text{IR}_b\sqrt{N}$. The floor becomes $r_{\min}/(\sigma_{\text{DTS}}\text{IR}_b) = 3.16$, with no $N$ left in it, so it is the side that does not move. The dry ceiling $\sqrt{N}\,\text{DD}_{\max}/(\sigma_{\text{DTS}}(\kappa z_p - \text{IR}_b\sqrt N))$ rises with $N$ and reaches the floor when $\text{SR} = r_{\min}\kappa z_p/(\text{DD}_{\max} + r_{\min}) = 0.2/0.125 = 1.6$, which is $N = (1.6/0.316)^2 = 25.6$. With the liquidity charge, $G_{\max} < \text{DD}_{\max}/c_1$ for every positive $1/A$. Breadth can only push the ceiling toward that limit, and getting there needs $\text{SR} \to \kappa z_p$ (here at $N_{\text{eff}} = 160$, beyond any breadth a 1% residual correlation allows).

**The trap:** Holding SR fixed at 2 while you add names. Then the floor and the dry ceiling both scale with $\sqrt{N}$, their ratio stays at $r_{\min}(\kappa z_p - \text{SR})/(\text{DD}_{\max}\text{SR}) = 2/3$, and you conclude that breadth makes no difference, or, reading only the floor, that breadth hurts. The second trap is treating the reopening at $N_{\text{eff}} \approx 97$ as a lever. It needs a Sharpe of 3.1 and every bet the residual correlation will allow. In practice a closed band gets reopened by cutting the cost of leaving, not by adding bonds.

**If you got this wrong, read:** §28.7, the *ceiling that moves when you lean on it* box, the band's Full Derivation and Theo's four levers; §28.2 for the $1/\rho_a$ ceiling; and `leverage_floor` and `leverage_ceiling` in Listing 28.6 (Appendix F).

**Z.28.2: Kaz's 93%, re-audited**

**Answer:** There are three numbers. (1) $\lambda^{\mathbb{Q}} = 0.045/0.6 = 7.5\%$, and (28.11) gives $f^\ast = 1/0.6 - 0.075/0.045 = 1.667 - 1.667 = 0$. A quarterly-premium bootstrap at a 4% rate gives 7.46% and $f^\ast = 0.008$, which is convention noise, not edge. (2) Under $\lambda^{\mathbb{P}} = 1.5\%$, $f^\ast = 1.667 - 0.333 = 1.33$ of NAV (1.31 with $\sigma = 5\%$). That is inside the average-loss boundary $1/0.6 = 1.67$. (3) Set $L = L_{\max}U$ with $L_{\max} = 1$ and $U \sim \text{Beta}(3, 2)$, Listing 28.3's shape with mean loss 0.6. Then $f^\ast = 1.00$: Kelly runs straight to the ruin boundary the documents imply, $1/L_{\max} = 1.0$. Defend the third number, and only after (28.13) halves it, to about 0.50 of NAV, with the cluster cap applied after that. The number belongs to Sunita. $L_{\max}$ and the shape of the recovery distribution are hers (§28.8: analysts own $L$ and $L_{\max}$), and they are what moved it. $\lambda^{\mathbb{P}}$ belongs to Kaz, and the desk head signs.

**How:** With a flat hazard and continuous premium, $s = \lambda^{\mathbb{Q}}L$ exactly. Since the bond's carry equals the CDS spread (zero basis), $f^\ast = 1/L - s/(Lc) = 0$. Under $\mathbb{P}$ the edge is $c - \lambda L = 4.5\% - 0.9\% = 3.6\%$ a year, so 80% of the spread is risk premium. Now put number (2) through the uptier: at $L = 1$ it loses 133% of NAV, which is past ruin. For random $L$ the first-order condition is $c = \lambda\,\mathbb{E}[L/(1 - fL)]$. At $f = 1/L_{\max}$ with $U \sim \text{Beta}(a, b)$, $\mathbb{E}[U/(1-U)] = a/(b-1)$, so

$$
\lambda\,\frac{a}{b-1} = 0.015 \times \frac{3}{1} = 0.045 = c,
$$

and the condition holds exactly at the cliff. The shape decides the answer. A mean-0.6 Beta with $b < 2$ puts enough weight near total loss to pull $f^\ast$ inside the cliff ($\text{Beta}(1.5, 1)$ gives 0.95). With $b \ge 2$, $f^\ast$ is pinned at 1.0. A Kelly fraction sitting on its cap tells you the model's tail is thinner than the documents' tail, and that is why the half is not optional here.

**The trap:** Defending 1.33 because it is "inside the ruin boundary of 1.67". That boundary is $1/\mathbb{E}[L]$. The credit agreement moved the worst case to $L = 1$, and there 1.33 is a 133% loss. The zero under $\mathbb{Q}$ tempts the other mistake: "fixing" it with a physical hazard while keeping the agency's average $L$, which is how Kaz got to 93% in the first place.

NOTE (for the editor): "a Beta recovery of mean 0.6" literally means 60% recovery (mean loss 0.4). The bond's base case and Listing 28.3's `kelly_random_loss(0.045, 0.031, 3.0, 2.0, 1.00)` both use a Beta *loss* of mean 0.6 (recovery 40%). The exercise also gives no shape, and the answer depends on it: at these inputs every mean-0.6 Beta with $b \ge 2$ returns the boundary (1.00) and $b < 2$ returns less ($\text{Beta}(1.5, 1)$: 0.95). The literal reading, with $\text{Beta}(2, 3)$, also gives 1.00. Suggest "a Beta(3, 2) loss of mean 0.6, as in Listing 28.3".

**If you got this wrong, read:** §28.4, the *P and Q* box and "Which measure, and which loss" (random $L$, and the ruin boundary set by the worst recovery); "Fractional Kelly is full Kelly for people with standard errors" for (28.13); Theo's card in the 2026 CCC case study; §28.8 for who owns which input; and `kelly_random_loss` in Listing 28.3 (Appendix F).

**Z.28.3: Your fund is the borrower**

**Answer:** Base case: $(150 + 0.97 \times 400)/(10 + 25) = 538/35 = 15.4$ weeks. Stressed: the haircut becomes $3\% \times 5.8 = 17.4\%$, so the sleeve raises \$330.4mm and the weekly burn is \$45mm, giving $480.4/45 = 10.7$ weeks. That is under 13, so by Theo's standard the fund is a going-concern question: the first-day-of-engagement conversation, not a strategy meeting. Most of the damage comes from the margin side. Doubling the margin alone takes the runway to 12.0 weeks; the 2008 haircut alone leaves it at 13.7. At the stressed haircut, 13 weeks of runway allows a burn of no more than \$37mm a week.

**How:** Block 4's runway is (cash + $(1-h)\times$ liquid sleeve) / weekly burn, and the burn is margin calls plus redemptions. The stress hits both sides at once. The denominator rises 29% (\$35mm to \$45mm) and the numerator falls 11% (\$538mm to \$480mm). Using the exact 2007–08 ratio $3.40/0.59 = 5.76$ instead of 5.8 gives a 17.3% haircut and the same 10.7 weeks. Cash alone covers 4.3 weeks in the base case and 3.3 in stress. Everything after that depends on selling a \$400mm sleeve in the very weeks its bid has moved 5.8 times. That is Third Avenue's gap between the runway clock and the days-to-liquidate clock, and the formula hides a second assumption: that the whole sleeve converts to cash at once. Run (28.17) on the sleeve before you believe even the 10.7.

**The trap:** Dividing by redemptions alone, $538/25 = 21.5$ weeks, and calling the fund comfortable. The margin calls are this borrower's debt service, and they are the part of the burn that doubles in stress. Smaller slips: leaving out the haircut ($550/35 = 15.7$), or applying the 5.8 to the margin calls as well as the sleeve, which counts one stress twice.

**If you got this wrong, read:** §28.5, the Third Avenue case study (folder one, then Ines's four clocks after the card); `runway_weeks` and `days_to_liquidate` in Listing 28.4 (Appendix F); and the Runway row of the §28.9 dashboard.

**Z.28.4: Mags's adjusted number**

**Answer:** The three estimates are $\text{SR}$, $\kappa z_p$ and $N_{\text{eff}}$. Everything else in (28.22) is either policy ($\text{DD}_{\max}$, $r_{\min}$), read off quotes ($\overline{\text{LCS}}$), or a named scenario ($m$).

- $\text{SR} = 2 \pm 0.58$: three years under §28.9's $1/\sqrt{Y}$ rule. Lo's correction at a Sharpe of 2 widens this to $\pm 1.0$.
- $\kappa z_p = 4 \pm 1$: nobody has measured $\kappa$, and Paleologo's own range for $-\kappa F^{-1}$ runs from 4 to 6.
- $N_{\text{eff}} = 40 \pm 8$: a residual correlation of $\rho_a = 0.010 \pm 0.005$ maps to 33–49, and Marcus's dashboard went from 41 to 27 to 33 in one night.

Take Theo's reopened band ($\overline{\text{LCS}} = 0.4\%$, $r_{\min} = 4\%$), which runs from 2.53 to 2.95. The ceiling's standard error in logs is 0.36. One standard error each way gives 2.1 to 4.3, and a simulation gives a 90% interval of 1.8 to 5.7. In 4% of the draws $\kappa z_p \le \text{SR}$, and then there is no ceiling at all. The floor's 90% interval is 1.65 to 4.9. The band is 0.42 turns wide, and its uncertainty is about ten times that. The probability that it is empty is about 41%. With SR one standard error lower it is certainly empty: the floor is 3.56 and the ceiling 2.50. So it is not a band. It is a probability, and the dashboard's Skill row is right to show it again at one standard error lower.

**How:** Write the ceiling as $G_{\max} = \text{DD}_{\max}/\big(c_1 + (\kappa z_p - \text{SR})\,\sigma_{\text{DTS}}/\sqrt{N_{\text{eff}}}\big)$ and apply the delta method to its log:

$$
\text{se}(\ln G_{\max}) = \frac{\sigma_{\text{DTS}}/\sqrt{N_{\text{eff}}}}{c_1 + (\kappa z_p - \text{SR})\,\sigma_{\text{DTS}}/\sqrt{N_{\text{eff}}}}\sqrt{\text{se}_{\text{SR}}^2 + \text{se}_{\kappa z}^2 + \left(\frac{(\kappa z_p - \text{SR})\,\text{se}_{N}}{2N_{\text{eff}}}\right)^2} = 0.311 \times 1.17 = 0.365 .
$$

Taken one at a time, $\kappa z_p$ contributes 0.31 of that, SR 0.18 and $N_{\text{eff}}$ 0.06. The input nobody has measured carries most of the error. For the floor, $\text{se}(\ln F) = \sqrt{(\text{se}_N/2N_{\text{eff}})^2 + (\text{se}_{\text{SR}}/\text{SR})^2} = 0.31$. The floor and the ceiling share SR with opposite signs, so their intervals are not independent. That is why the empty-band probability comes from a joint simulation: two million independent normal draws of the three inputs, keeping only the draws with $\kappa z_p > \text{SR}$. The right tail of the ceiling is bounded by the speed limit, 7.8.

**The trap:** Naming $\text{DD}_{\max}$, $r_{\min}$ or the LCS. The first two are decisions the desk makes, so an "error" in them is a choice, and the LCS is read off the screen. The subtler trap is to put error bars on the floor and the ceiling separately and report that "the intervals overlap but the point estimates don't". The number that matters is $\Pr(\text{floor} > \text{ceiling})$. A lower SR raises the floor and lowers the ceiling at the same time, so the band empties faster than either interval suggests.

**If you got this wrong, read:** §28.7, Kaz on $\kappa$ and the Paleologo extraction that follows; §28.9's Skill row and the paragraph after the dashboard on SR as a pair; *The Map, Not the Territory* in §28.2 for $N_{\text{eff}}$ as a model output; and §7.8 for the standard error of a Sharpe ratio.

**Z.28.5: ROBO and the stop-loss**

**Answer:** Over a one-year allocation, the book with no rule earns 6.00%. Paleologo's two-threshold rule earns 5.53% (expected capital-time 0.922). ROBO earns 5.08% (expected capital-time 0.846). ROBO's rule costs **46 bp a year**, or 40 bp in Listing 28.5's daily-monitored Student-t(6) setup, and it doubles the price of safety from 7.8% to 15.4% of expected P&L. What it buys is small: the chance of a 7.5% loss within the year falls from 0.65% to zero. Over a career the gap is larger, because ROBO never restarts. It ends the PM's capital with probability $e^{-1.25} = 29\%$, against $e^{-3.75} = 2.4\%$ under the two-threshold rule. The spec sentence: *"The stop-loss is the platform's survival constraint, not the book's objective. Implement the two-threshold rule exactly: halve allocated capital at a loss of $x/2$ and liquidate at $x$, both measured on initial allocated capital. Never cut earlier, deeper or for longer than the rule says, and submit any proposed change with its price of safety, $\mu$ times the expected capital-time it removes."*

**How:** Capital $c_t$ is set from past P&L, and $\mathbb{E}[dX_t \mid \text{past}] = \mu\,dt$, so $\mathbb{E}[\text{P\&L}] = \mu\,\mathbb{E}\big[\int_0^T c_t\,dt\big]$. The two rules are identical until the first touch of $-3.75\%$, which happens in 23.7% of years by (28.19). After that, Paleologo's rule keeps half the capital until the underlying return falls a further 7.5%, because at half capital that is the next 3.75% of P&L. ROBO keeps none. So the whole difference is

$$
\Delta\,\mathbb{E}[\text{P\&L}] = \mu \cdot \tfrac12\,\mathbb{E}\big[(\tau_2 \wedge T) - (\tau_1 \wedge T)\big] = 0.06 \times 0.076 = 0.46\%,
$$

which you get by integrating the first-passage density of $\tau_1$ against $\int_0^{T-s}\big(1 - \Pr(\text{hit } 7.5\% \text{ by } u)\big)\,du$, with $\Pr(\text{hit})$ taken from (28.19). The lifetime figures use the limit of (28.19): ROBO is switched off for good the first time its line is touched, $e^{-2\mu(0.0375)/\sigma^2} = e^{-1.25}$. The two-threshold rule liquidates only if both legs are hit, $e^{-1.25}\,e^{-2.5} = e^{-3.75}$.

**The trap:** "ROBO's rule is safer and costs nothing, because it acts at the same 3.75% line." The first touch is where the two rules *start* to differ, and the whole cost lies in the capital-time after it. The deeper error is counting the "losses avoided" as a gain. Under the identity, a stop never changes the return earned per unit of capital-time. All it can do is remove capital-time, so for a PM with $\mu > 0$ it can only cost. As Paleologo puts it, stops exist for the firm's survival, not to improve performance.

**If you got this wrong, read:** §28.6, the Paleologo p.167 extraction and its annotation (the identity), "Setting the stop with drift" for (28.19) and (28.20), and `simulate_two_threshold` in Listing 28.5 (Appendix F), which this exercise reruns with ROBO's rule beside the platform's.

<!-- STATUS: COMPLETE -->
