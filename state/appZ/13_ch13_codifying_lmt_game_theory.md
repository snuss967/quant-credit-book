## Z.13 Chapter 13: Codifying Liability Management Transactions (LMTs)

Five exercises: Serta with the liens pulled apart, a three-member co-op's veto, a drop-down priced as a forward, Trinseo rebuilt on the clearing engine, and ROBO's empty portfolio. Every number below was recomputed in Python, using the chapter's own Listings 13.1 and 13.2 (Appendix F) wherever an exercise builds on them; we ran the listings first, and they print what the chapter says (70 events, PRS 0.903, $\mathbb{E}[\Delta R] = 0.220$, EPL 4.57 points). Where we had to choose an input, the solution says so. There are two notes for the editor, in Z.13.1 and Z.13.4. Write your answer down before you read ours.

**Z.13.1: Unblend Serta**

**Answer:** Let $a$ be the first-lien face in the \$1.2bn exchange and $b = 1{,}200 - a$ the second-lien face. At the stated exchange rates (74 and 39), the strike for the excluded first lien is

$$
K_1(a) = 200 + 0.74a + 0.39(1{,}200 - a) = 668 + 0.35a ,
$$

which runs from 930.5 (all \$450mm of the second lien exchanged) to 1,088 (no second lien exchanged). At the remand split ($a = 992$, $b = 208$), $K_1 = 1{,}015$ and the second-out is \$815mm, not \$875mm. At $V = 1{,}075$ the excluded first lien loses **50.3 points** on the June 2020 face of \$1,887mm, so the blend's 44.8 is **5.5 points too low**. The error passes **10 points once $a \gtrsim \$1{,}115$mm** (so $b \lesssim \$85$mm, or 93% of the exchange in first lien). On the 2016 face of \$1,950mm the line is $a \gtrsim \$1{,}155$mm. The only split that matches both exchange rates and the opinion's \$875mm is $a = 1{,}163$, $b = 37$. That puts $K_1$ back at 1,075, and the error is 12.2 points (10.3 on the 1,950 face). So the blend is more than 10 points wrong at the split the published total implies, and about half that wrong at the split the remand findings imply. For the excluded *second* lien the blend is wrong by the full 44.8 points at every split. Behind \$1,887mm of first lien it recovered nothing at $V = 1{,}075$ before the deal and nothing after.

**How:** Before the deal the excluded first lien held the first-lien ramp, $V/F_1$, and not the blended $V/2{,}400$. After it, the lien stands third, behind $K_1(a)$, with face $F_1 - a$:

$$
T(a) = \frac{1{,}075}{F_1} - \frac{\min\!\big((1{,}075 - K_1(a))^+,\ F_1 - a\big)}{F_1 - a}
= \frac{1{,}075}{1{,}887} - \frac{(407 - 0.35a)^+}{1{,}887 - a}.
$$

The first term is fixed at 57.0 cents. The second, which is what the excluded lien still collects at $V = 1{,}075$, falls from 12.7 cents at $a = 750$ to 6.7 at $a = 992$ and to zero at $a \ge 1{,}163$. Setting $T(a) - 44.8 = 10$ and solving gives $a^\star = 1{,}114.8$. The feasible range is $a > 943.5$, because the participants needed a majority of the first lien, and $a \le 1{,}200$. Across that range the blend is always too *low*, by 4.0 points at the smallest feasible $a$ and by up to 12.2. Even at $a = 750$, outside the range, it is only 0.5 points too high. The sensitivity runs entirely through $K_1$, because the second lien converted at 39 cents and the first at 74. Each \$100mm of the exchange that was first lien rather than second adds \$35mm to the strike.

NOTE (for the editor): In §13.3.1's unblending table, the middle row ("first-lien second-out only") builds $K_1 = 934$ from June 2020 holdings ($992 \times 0.74$) but divides by the 2016 face of 1,950, giving 47.9. On the June 2020 face of 1,887, the one the remand court's ratable share uses, the row reads $934/1{,}887 = 49.5$, and the sentence below the table would say "between five and twelve points" rather than "between three and twelve." The other two rows check (44.8 and 57.0).

**The trap:** Using one blended exchange ratio, $x = 875/1{,}200$, for both liens. Then $K_1 = 1{,}075$ at every split, the split seems not to matter, and you conclude the blend is off by a constant 12.2 points. The split matters only because the two liens converted at different rates. The second trap is dividing the excluded first lien's pre-deal recovery by 2,400. That treats it as pari passu with a second lien that sat behind it, and it is exactly the understatement the exercise asks you to measure.

**If you got this wrong, read:** §13.3, "The Full Derivation: the excluded lender's transfer" (the three regions), then §13.3.1, beat III and "Unblending the liens."

**Z.13.2: The 5% veto**

**Answer:** With $\theta = \tfrac23$, blocking needs more than $\tfrac13$ of the class. The co-op holds 35%, but its best pair, A and B, holds only 30%, so the *only* blocking subset is all three: $\phi_A = \phi_B = \phi_C = \tfrac13$. C's veto dies once C sells A **just over $3\tfrac13$% of the class**, two-thirds of its 5% holding. A and B then hold more than $\tfrac13$ between them, C keeps less than $1\tfrac23$%, and the Shapley values jump to $(\tfrac12, \tfrac12, 0)$. C will ask for more than par because the loans carry a third of the co-op's blocking power on a seventh of its holdings. Selling that block hands over all of it, including the power of the slice C keeps.

**How:** List the subsets: A 20, B 10, C 5, A+B 30, A+C 25, B+C 15, A+B+C 35. Only the last exceeds $33\tfrac13$, so $v(T) = 1$ only for the full co-op, $T = \{A, B, C\}$. In every joining order the pivot is whoever walks in last, and each member is last in 2 of the $3! = 6$ orders. That is $\tfrac13$ each, which the chapter's `shapley([0.20, 0.10, 0.05], quota=1/3)` confirms. Now move $\delta$ from C to A. The pair A+B holds $30 + \delta$, and it blocks without C as soon as

$$
30\% + \delta > 33\tfrac13\% \quad\Longleftrightarrow\quad \delta > 3\tfrac13\% .
$$

At $\delta = 3\tfrac13\%$ exactly, the pair sits *at* the quota, and the strict inequality in $v(T)$ leaves C's veto intact. Above it, C is never pivotal (A+C and B+C are still short, and A+B already blocks), so $\phi_C = 0$. On price: C's pro rata share of the co-op is $5/35 = 14\%$, its power share 33%, 2.3 times as much. If the co-op's carve-out pot is $P$, C gives up $P/3$ by selling. A gains only $P/6$, because C's lost third splits evenly between A and B. B collects its sixth for free. So C's reservation price is par plus $P/3$ on the block, and A's limit is par plus $P/6$. This is why such vetoes tend to stay where they are.

**The trap:** Allocating power in proportion to holdings, (57%, 29%, 14%), or using $\tfrac23$ itself as the blocking quota. The co-op is not trying to pass anything; it is trying to stop the sponsor, which takes more than $1 - \theta$. The other slip is thinking C must sell everything to lose the veto. At 5% sold the values are again $(\tfrac12, \tfrac12, 0)$. Every sale above the threshold produces the same split, so C should never sell just past it at par.

**If you got this wrong, read:** §13.5, "Carve-out premiums are Shapley values" and the Math, Gently box on the Shapley value, then "The Full Derivation: bargaining weights and pivots."

**Z.13.3: Forward or digital?**

**Answer:** The lenders lose a net $L = T - \phi D_u - (T - D_u)^+ = 300 - 28 - 20 = 252$, so

$$
\Delta R(V) =
\begin{cases}
V/2{,}000, & V \le 252, \\
0.126, & 252 < V \le 2{,}000, \\
(2{,}252 - V)/2{,}000, & 2{,}000 < V < 2{,}252, \\
0, & V \ge 2{,}252 .
\end{cases}
$$

The plot is a short ramp, a long flat shelf at **12.6 points**, and a ramp back down. That is a forward, not a digital. It never exceeds $T/F = 15$ points; the 2.4-point gap is the 28 that comes back and the 20 of retained equity. Under block (b)'s lognormal (median \$1,500mm, $s = 0.45$), $\mathbb{E}[\Delta R] =$ **9.8 points** (0.0983; a 2-million-draw Monte Carlo gives 0.09825 ± 0.00004). PetSmart-style, suppose the same \$300mm of basket buys 36.5% of a subsidiary worth $300/0.365 = \$822$mm and releases its whole guarantee. The leak is then $822 - 28 - 20 = 774$, the shelf sits at **38.7 points**, and the expectation is **32.1 points**, 3.3 times as much. The share-count bound of 15 points fails by more than double; the honest cap is the guarantee's value, $822/2{,}000 = 41$ points.

**How:** Write the post-deal recovery as $\min\big((V - L)^+, F\big)/F$. Then $\Delta R = [\min(V,F) - \min((V-L)^+, F)]/F$, and since $L \le T$ the bound $\Delta R \le L/F \le T/F$ is immediate. The expectation is a quadrature with breakpoints at $L$, $F$ and $F + L$. The shelf supplies almost all of it: $0.126 \times \Pr(252 < V \le 2{,}000) = 0.126 \times 0.739 = 0.093$. The taper adds 0.005, and the ramp is negligible ($\Pr(V < 252) = 0.004\%$). Compare the uptier in the same listing, which costs 22 points on average but only in the low states: 74% of this law's mass sits on the drop-down's shelf. That is why the market prices a drop-down on announcement day and an uptier slowly. For PetSmart we assumed that the 63.5% stake left behind goes out of the collateral with the guarantee (the release of the share pledge is what the lenders feared). The general rule is $L = (\text{value whose guarantee or lien is released}) - \phi D_u - (\text{equity the lenders still reach})$. In this case $\Pr(V < 774) = 7\%$, so the ramp now carries weight as well.

**The trap:** Scaling $T$ to 822 in the chapter's formula and keeping $D_u = 280$. The term $(T - D_u)^+ = 542$ then hands the released value straight back as "retained equity," and the leak comes out at 252 again: the release clause appears to cost nothing. That term assumes the restricted group keeps the subsidiary's equity *as collateral*, which is exactly what a guarantor release takes away. The release clause, not the share count, determines $T$.

**If you got this wrong, read:** §13.6, "The arithmetic" and "PetSmart and the guarantee lever"; Figure 13.4 for the two shapes side by side; §13.3 for the digital you are comparing against.

**Z.13.4: Rebuild Trinseo**

**Answer:** Three parameters move the two recoveries. They are OpCo's value after the revolver, $r$; the value upstairs that only Super HoldCo can reach, $U$; and the allowed intercompany claim, $I$. Below the caps,

$$
\rho_{\text{OpCo}} = \frac{r}{1{,}982 + I}, \qquad R_{\text{SH}} = \frac{U + (1{,}266 + I)\,\rho_{\text{OpCo}}}{1{,}266}.
$$

Both ranges (OpCo 2–9%, Super HoldCo 60–78%) hold for **total value $V = 348 + r + U$ between \$1,122mm and \$1,400mm** (6.9 to 8.6 times 2025 EBITDA) and for **any allowed claim from 0 to \$1,508mm**. The split of $V$ is what changes with $I$. At $I = 1{,}508$: $r \in [70, 314]$ and $U \in [510, 932]$, jointly $760 \le U + 0.795\,r \le 987$. At $I = 948$: $r \in [59, 264]$, $U \in [560, 943]$. At $I = 0$: $r \in [40, 178]$, $U \in [646, 962]$. **The parameter that matters most is $U$.** With $U = 0$, Super HoldCo cannot pass 19.7% even with the full \$1,508mm note; reaching 60% would take an allowed claim of about \$7.2bn. The allowed claim, the number the lawsuit is about, matters least: at the whiteboard's $r = 175$, $U = 735$, every $I$ from zero to \$10bn keeps both recoveries inside their ranges.

**How:** The graph has three entities. The top holding company has value $U$ and owns OpCo (value $348 + r$) and the SPV (value 0). OpCo owes the \$348mm revolver at rank 1. At rank 2 it owes a pari pool: the \$716mm 2028 term loans, a \$1,266mm guarantee of the Super HoldCo debt, and the note $I$, whose creditor is the SPV (the pledge). At rank 3 come the \$390mm of notes. The top entity guarantees \$1,266mm, and the SPV's own \$1,266mm term loan carries `reduce_by` on both guarantees. Run through `waterfall_clearing`, this reproduces the whiteboard to the cent: 5.01% and 69.04% at $(r, U, I) = (175, 735, 1{,}508)$, 62.45% at $r = 70$, and Ines's 6.0 and 8.8 at $I = 948$ and 0. Conservation gives the $V$ range without a search, because the notes and the equity get nothing: $V = 348 + 716\rho_{\text{OpCo}} + 1{,}266R_{\text{SH}}$, which does not contain $I$. Sensitivities at the whiteboard point: \$100mm more $U$ moves Super HoldCo up 7.9 points and OpCo not at all; \$100mm more $r$ moves OpCo 2.9 points and Super HoldCo 6.3; striking the whole note ($1{,}508 \to 0$) moves OpCo up 3.8 and Super HoldCo down 2.2.

NOTE (for the editor): The whiteboard's arithmetic puts the guarantee in OpCo's pool at its full \$1,266mm on top of the \$735mm collected upstairs, and "Ways This Blows Up" item (2) says the engine assumes full face against each obligor. Listing 13.1's pari-plus wiring does the opposite: `opco_guar` carries `reduce_by=["fsub_guar"]`, and §13.7 describes it as "double-dip OpCo for the deficiency." A reader who copies `dd_recoveries` gets OpCo 6.35% and Super HoldCo 68.3% at the whiteboard inputs, not 5.0% and 69%. With the note struck the gap is wider (14.0% against 8.8%). Suggest saying in the pari-plus paragraph, or in item (2), that the listing nets and the whiteboard does not.

**The trap:** Hunting for the multiple in the intercompany claim. However large it is allowed to be, the note scales Super HoldCo's take from OpCo by at most $(1{,}266 + I)/1{,}266$, which is 2.19 at \$1,508mm. The rest of the 7-to-39 multiple is the value upstairs divided by a small OpCo residual. That is also why the ranges cannot tell you what the court will do with $I$.

**If you got this wrong, read:** §13.7, "The closed form" and "Pari-plus," then §13.7.1 from "Where's the revolver?" to Ines's count-by-count pricing; "Ways This Blows Up" items (2) and (5).

