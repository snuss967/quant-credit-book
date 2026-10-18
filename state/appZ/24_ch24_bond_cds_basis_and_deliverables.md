## Chapter 24: Bond-to-CDS Basis & Deliverable Obligation Mechanics

Six exercises: one on the hedge ratio, one on a phantom signal, one on the band, one on an auction's rounding, and two on paper, because the legal layer is where this chapter's money is. Every number below was recomputed from the chapter's inputs and Listings 24.1 to 24.7 (Appendix F). Write your card before you read ours.

**Z.24.1: The over-hedge**

**Answer:** The JTD-neutral notional is $N^{\text{JTD}} = (0.72 - 0.35)/(1 - 0.35) = 0.569$, so \$5.69mm of protection per \$10mm face. If the auction (and with it the bond, which in bankruptcy recovers the same as everything else pari passu) comes in at 25 rather than 35, the package loses about \$431k. The bond loses 47 points (\$4.70mm), and the swap pays 75 points on \$5.69mm (\$4.27mm). The package is long recovery by $1 - N^{\text{JTD}} = (1-P)/(1-R) = 0.43$ of face, or about \$43k per point of recovery on \$10mm.

**How:** At default the bond goes from $P$ to $R$ and $N$ of protection pays $N(1-R)$, so the package's default P&L per unit face is

$$
\Pi(R) = (R - P) + N(1-R).
$$

Setting $\Pi(0.35) = 0$ gives $N^{\text{JTD}} = (P-R)/(1-R) = 0.37/0.65$. Now differentiate with respect to the recovery that actually happens:

$$
\frac{\partial \Pi}{\partial R} = 1 - N, \qquad 1 - N^{\text{JTD}} = \frac{1-P}{1-R} = \frac{0.28}{0.65} = 0.431 .
$$

Ten points of recovery miss times 0.431 times \$10mm is \$431k, which is the P&L above. The bond's sensitivity to recovery is one per unit face, but the swap's is only $N$. The two cancel only when $N = 1$, and $N^{\text{JTD}} = 1$ only when $P = 1$. Par-for-par (\$10mm) is the mirror image: it has no recovery delta at all, but it is long \$2.8mm of jump-to-default at any recovery. With one swap you can neutralize the jump or the recovery, not both, unless the bond is at par. That is Schmid's "a default swap is a par product" sentence turned into a Greek.

**The trap:** The usual slip is to say "I hedged JTD, so default can't hurt me." The hedge is flat at the recovery you assumed, not at the one the auction prints. The runner-up is hedging market value, \$7.2mm (bond price times face). That is neither JTD-flat (+\$0.98mm at 35) nor recovery-flat. A subtler slip is in the scenario itself. If the bond recovers 35 but the auction prices a cheaper deliverable at 25, the package *makes* \$0.57mm. That is §24.5's cheapest-to-deliver option, not a recovery delta, so keep the two apart.

**If you got this wrong, read:** §24.3.1, the Schmid p.159 annotation after the vintage table ($N^{\text{JTD}}$ and its recovery delta), and "Ways This Blows Up" (2) in §24.4 for JTD drift as the price moves; then §24.5.1 for when the bond and the auction stop recovering the same amount.

**Z.24.2: Vintage alpha that isn't**

**Answer:** Take $r = 4\%$, $\lambda = 5\%$, $R = 40\%$, $T = 5$ and nine semiannual bonds with coupons 2%, 3%, …, 10%, each priced off the hazard with `bond_price_hazard`. Prices run from 79.69 to 111.18, and the Z basis against the 297.4 bp CDS runs from +22.1 bp to −18.8 bp. Regress the Z basis on price and you get a slope of −1.29 bp per point, $t = -47$ and $R^2 = 0.997$. With coupons every 50 bp (17 bonds) the $t$-statistic is −72, and every 25 bp (33 bonds) it is −106. The PECS basis is zero, to about $3 \times 10^{-9}$ bp, on every bond. The "signal" is real, perfectly significant, and worth nothing: every bond earns exactly the same risk-adjusted return, because every bond was priced off the same hazard.

**How:** This extends Listing 24.2. Loop `bond_price_hazard`, `z_spread` and `pecs` over the coupon grid, then run OLS of $b^{Z} = 10^4(s^{\text{CDS}} - Z)$ on $100P$. The slope comes from the recovery convention. The swap's loss is $1-R$ of face, but the Z-spread prices a loss of roughly $(P-R)/P$ of market value. That gives

$$
Z \approx \lambda\,\frac{P-R}{P}, \qquad b^{Z} \approx \lambda(1-R) - \lambda\,\frac{P-R}{P},
$$

which falls smoothly as $P$ rises. (This is the instantaneous version and it overstates the size, because the price pulls to par over the bond's life. Only the sign and the shape carry over.) A deterministic function of price, regressed on price, gives a $t$-statistic that grows like $\sqrt{n}$ as you add bonds. The 0.3% of variance the line misses is curvature (the quadratic term is positive), not noise. The zero crossing sits at a price of about 95.1, not 100. The ACT/360 CDS spread (297 bp) is below the 303 bp Z-spread of a par semiannual bond, which matches the Figure 24.1 caption. The "cheap-bond" sort, long negative-Z-basis bonds against short positive ones, is a sort on coupon: it is long premium bonds and short discount bonds, with zero expected excess return.

**The trap:** The trap is to read a big $t$ as a big effect. Significance measures how precisely you estimated a pattern, not whether the pattern pays. Here the precision is perfect because there is no noise at all. Note the sign as well. The convention makes discount bonds look *rich* (positive $b^{Z}$), not cheap. So if your screen says the 2021 low coupons are cheap, the recovery convention is not the cause. Look for something like Ruth's stale curve date. Either way, rerun the regression on $b^{\text{PE}}$: the slope goes to zero.

**If you got this wrong, read:** §24.3.1 (the box "forty back on what?" and *The Full Derivation: the vintage pattern*), then the Ruth vignette in §24.3 for what a vintage effect usually turns out to be.

**Z.24.3: The band in March 2020**

**Answer:** Before costs ($k^{-} = 0$), the negative edge $-\phi(1-h)$ moves from $-30 \times 0.90 = -27$ bp to $-150 \times 0.65 = -97.5$ bp. A −186 bp IG basis lay *outside* the band in both cases: by 159 bp before and by 88.5 bp after. So the band says the package should have been bought. It wasn't, at least not fast enough, and the gap is the term the exercise left out. At a 35% haircut the package's carry of 88.5 bp is only a 2.5% ROE over cash, against 15.9% at the old terms. For −186 to sit *on* the edge you need $k^{-} = 88.5$ bp. As a hurdle on the posted equity, that is $88.5/0.35 \approx 25\%$ a year over cash: a plausible price for scarce balance sheet that month *(illustrative)*.

**How:** Use the carry from §24.4.1, with the basis in bp of face:

$$
\pi^{-} = -b - \phi(1-h), \qquad \text{edge} = -\phi(1-h) - k^{-}.
$$

Before: $\pi^{-} = 186 - 27 = 159$ bp, and $\text{ROE}^{-} = 0.0159/0.10 = 15.9\%$. After: $\pi^{-} = 186 - 97.5 = 88.5$ bp, and $\text{ROE}^{-} = 0.00885/0.35 = 2.5\%$. Take the two moves one at a time. The repo spread alone (150 bp at $h = 10\%$) puts the edge at −135. The haircut alone (30 bp at $h = 35\%$) *narrows* it to −19.5, because you borrow less. The haircut does its damage through the divisor, not through the edge. It also bites through the mark-to-market: a further 100 bp of widening at $D^{\text{spr}} = 4.5$ costs 45% of equity at $h = 10\%$ and 12.9% at 35%. Writing $k^{-} = \rho h$ for a hurdle $\rho$ on equity, the edge becomes $-\phi(1-h) - \rho h$, and this is where the haircut widens the band.

**The trap:** One common slip is to compare −186 with $-\phi = -150$ and say "outside by 36," which forgets the $(1-h)$. The bigger one is to conclude "outside the band, so free money." The band as written prices the equity at the risk-free rate. In March 2020 equity was the scarce input: Mags's prime broker raised haircuts in the same week the basis widened. A basis outside a band that leaves out the price of balance sheet is a measurement of that price.

**If you got this wrong, read:** §24.4.1 (the band, the ROE line and the mark-to-market paragraph), Long Scene A in §24.4 for the same arithmetic on Ines's blotter, and "Ways This Blows Up" (1) in §24.4 on the haircut as a process.

**Z.24.4: ROBO rounds the IMM**

**Answer:** Listing 24.5's own eight-dealer book does it. The raw midpoint is exactly 26.8125, which is 214.5 eighths. Rounding halves up gives an IMM of 26.875, and Python's `round()` gives ROBO 26.75. Now add a rogue \$10mm bid at 30.0 against \$5mm of net selling open interest. The book clears at $p^{*} = 30.0$, the cap binds, and the final price is $\text{IMM} + 1$: 27.875 for the correct auction and 27.75 for ROBO's. Protection buyers are paid 72.125 rather than 72.25 points. On \$5bn of CDS outstanding *(illustrative)*, ROBO's auction moves $0.125\% \times \$5\text{bn} = \$6.25$mm from protection sellers to protection buyers. The crossing dealer's Adjustment Amount changes as well, to \$25,000 from \$22,500.

**How:** Sort the bids down and the offers up. The first pair, a 28.0 bid against a 27.0 offer, crosses and is discarded. That leaves seven pairs, of which you keep the best $h = \lceil 7/2 \rceil = 4$:

$$
\text{IMM}^{\text{raw}} = \frac{(26.25 + 26 + 26 + 25.75) + (27.25 + 27.5 + 27.75 + 28)}{8} = \frac{214.5}{8} = 26.8125 .
$$

That is a tie between 26.75 and 26.875. Halves-up goes to 26.875, and round-half-to-even goes to 214 eighths, or 26.75. In stage 2, OI $< 0$ walks the bids from the top. The rogue bid fills all \$5mm at 30.0, so $\text{FP} = \min(30.0,\ \text{IMM} + 1)$ and the whole rounding error passes through. The buy side works the same way. A rogue \$10mm offer at 24.0 against \$5mm of buying gives $\max(24.0,\ \text{IMM} - 1)$, which is 25.875 against 25.75.

**The trap:** One slip is to think a rounding error is at most a sixteenth. On a tie it is a full increment, because the two candidates are an eighth apart. Another is to assume the IMM error never reaches the final price. It doesn't when the cap is slack: at \$50mm of selling both versions clear at 23.0. It does whenever the final price *is* the IMM, which happens when OI is zero or the cap binds. Watch the units too: an eighth of a point is 0.125% of notional, so \$6.25mm, not \$625k.

**If you got this wrong, read:** §24.6.1 (the IMM formula and the cap cases), the ROBO paragraph in the Specification for the auction simulator, and Figure 24.4's right panel, which is this exact book.

**Z.24.5: Design a drop-down (on paper)**

**Answer:** *Design A (no Successor):* have NewCo assume exactly \$1,000mm, which is 25.0% of the \$4bn. "More than 25%" is strict, so `successors({"NEWCO": 0.25})` returns the swap unchanged. At \$1,000.01mm the swap splits. *Design B (two Successors):* have NewCo assume more than \$1.0bn and less than \$3.0bn, say \$2.0bn. NewCo is above 25% and the original keeps more than 25%, which is case 3, so each \$10mm swap becomes \$5mm on NewCo and \$5mm on the original. Stop short of \$3.0bn: at exactly 75%, NewCo takes the whole swap (case 1). For a protection buyer, **Design A is the more dangerous**, because its limit is an orphan and no rule ever fires on the way there.

**How:** Run Listing 24.7 on the shares $w = D_{\text{moved}}/\$4\text{bn}$ and walk the four cases. With one new entity, any $w \in (0.25, 0.75)$ leaves $w_0 = 1 - w > 0.25$ automatically, so the whole interval is case 3. Design B costs the buyer something visible. The DC announces the split, half the notional may sit on whichever entity the sponsor made safe (the Windstream/Uniti shape), and the buyer can reprice and re-hedge. Each half still references an entity with debt to default on and to deliver. Design A is invisible. The code even lets you repeat it: three subsidiaries at 25.0% each move \$3bn, or four move all \$4bn, and the code still prints "unchanged." The real Definitions would test that chain as a Steps Plan, which the code does not model. The assumption test decides the real case. Under the 2014 Definitions an entity *succeeds* to an obligation only if it becomes liable for it (by law or by agreement) or issues bonds or loans exchanged for it, and the reference entity then stops being an obligor or guarantor of it. If NewCo instead borrows new money and the proceeds *repay* the original's bonds, NewCo succeeds to nothing. Its share is 0% however much debt moved economically, so Design A has no \$1bn ceiling. The swap stays at full notional on a shell whose deliverable set shrinks toward empty: McClatchy's planned refinancing in §24.8.1. If the original stays a guarantor, there is no succession either, but the moved debt may stay deliverable, which helps the buyer.

**The trap:** One slip is to answer "\$1.0bn plus a dollar." That is 25.00000…1% and it splits the swap. Another is to put \$3.0bn into Design B, which hands the whole swap to NewCo. On the judgement, the common mistake is "no Successor means nothing happened, so A is safe." The step function is flat at 25.0%, and so is the screen, but that is exactly how an orphaning plan looks from the outside. A data trap sits underneath: compute shares from principal amounts as exact fractions, because a float that arrives as 0.2500000001 turns Design A into Design B.

**If you got this wrong, read:** §24.8.1 (the staircase box, the four-case table and the orphaning paragraph on McClatchy and Octus), then the Specification for the successor map, which routes Steps Plans and the assumption test to counsel.

**Z.24.6: Kaz writes a credit event**

**Answer:** Three levers, each of which works in both directions:

1. **Move the cash.** To manufacture the event, pay a dividend, prepay or buy back debt, fund an acquisition, or sweep cash to an unrestricted or non-guarantor subsidiary outside the model's perimeter. Runway falls below four weeks and creditworthiness hasn't changed. To avoid it, take a short-dated injection from a sponsor, or rescue money from a protection seller (the RadioShack pattern), that holds runway above four weeks until the swaps expire.
2. **Write the forecast.** The issuer writes the 13-week model. Front-loading disbursements, pushing receipts back a week, haircutting collections, or assuming the revolver is or isn't available are all defensible judgements, and each one moves runway by weeks.
3. **Time the test.** Draw the revolver, stretch payables, factor receivables or defer capex in the week the model is read, which is window dressing. Or let a facility lapse just before it, which is the reverse. "Less than four weeks" is a cliff, and 4.0 against 3.9 is a choice.

Kaz's trigger is **worse than Failure to Pay as a trigger, and better as evidence.**

**How:** Compare what each definition asks a committee to verify. Failure to Pay asks about a fact: was a payment of at least the \$1mm Payment Requirement missed after its grace period? Anyone can check it, and the issuer pays a real price to manufacture it, a default under its own documents (Hovnanian had to engineer a \$1.04mm missed coupon and a lender to pay for it). The 13-week model is a forecast. It is unaudited, unpublished, revised weekly, and every line of it belongs to the issuer, so it is cheaper to move in either direction and no Determinations Committee can verify it. What Kaz's version gets right is the link to creditworthiness. Hovnanian, at about 80 weeks of runway, could never have triggered it. That is the job of the 2019 NTCE Credit Deterioration Requirement, and it is how the chapter uses the model. Keep Failure to Pay as the hard trigger, and use the 13-week model as evidence for or against deterioration: the "more than 52 weeks of runway" flag in Listing 24.7.

**The trap:** The usual answer is "better, because it measures real distress." It does, in the issuer's own hand. A definition the issuer writes is a definition the issuer can game. Hovnanian showed that the gap between a contract's trigger and the company's condition is where the engineering goes. Kaz's version moves that gap from a payment date into a spreadsheet, where it is harder to see.

**If you got this wrong, read:** §24.8.2 (Long Scene B, Theo's runway model as evidence, and the Docket Diary), §24.8.4 on the Credit Deterioration Requirement and what it does not reach (manufactured non-defaults and orphaning), and the manufactured-event flags in the successor-map Specification.

<!-- STATUS: COMPLETE -->
