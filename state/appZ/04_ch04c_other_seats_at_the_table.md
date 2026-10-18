## Z.4-C Chapter 4-C: Other Seats at the Table: One Bond, Seven Owners

There are six exercises, all at the end of §4C.10; each already has a one-paragraph solution printed beside it, none carries a [Read]/[Derive]/[Build] tag, and none is embedded elsewhere in the chapter. Exercises 1 to 3 are arithmetic on the chapter's Math, Gently boxes; 4 asks you to name the leaks in the PB-02 pair and has more than one defensible answer; 5 is a definition with a small numerical check; 6 is conceptual and points at Listing 4-C.1 in Appendix F without asking you to extend it. Nothing here uses a risk-neutral probability: every number is a price in cents on the dollar, a dollar amount in \$mm, or a rule from an indenture or a capital table, so $\mathbb{P}$ versus $\mathbb{Q}$ never comes up. The printed solutions hold up on the arithmetic; where the chapter's text or listing disagrees with my computation I say so in a NOTE (for the editor).

**Z.4-C.1: The cheapest cure**

**Answer:** The excess is \$3.6mm. Keeping it costs the OC numerator \$1.62mm. Selling \$3.6mm of the loan at 90 costs \$0.36mm; selling \$3.6mm of the loan at 70 costs \$1.08mm. Measured against doing nothing, the sale at 90 recovers \$1.26mm and the sale at 70 only \$0.54mm, so sell the better loan. (Units: \$mm of OC numerator, prices in cents on the dollar. No probability measure is involved; this is an indenture rule applied to observed prices.)

**How:** The bucket holds $8.4\% \times 400 = 33.6$ and the limit allows $7.5\% \times 400 = 30.0$, so the excess is $3.6$. The indenture counts the excess at the lowest price in the bucket, 55, so keeping it costs

$$
3.6 \times (1 - 0.55) = 1.62.
$$

Selling that much par at price $p$ brings the bucket exactly to the limit, the haircut disappears, and all you give up is the discount you realize:

$$
\text{cost}(p) = 3.6\,(1-p) \quad\Longrightarrow\quad \text{cost}(0.90) = 0.36, \qquad \text{cost}(0.70) = 1.08.
$$

Net of the haircut you were carrying, the gain is $3.6\,(p - 0.55)$, which is \$1.26mm and \$0.54mm: the better the loan you sell, the more you get back. That is Kundu's improvement $g(\gamma-\beta)A/L$, with $\gamma$ the price sold and $\beta$ the worst price in the bucket. One piece of small print: the sale also shrinks the pool, so the 7.5% limit shrinks by 7.5% of the par burned, which leaves about \$0.03mm and \$0.08mm of fresh excess and another \$0.01mm and \$0.04mm of haircut. That is the $\bar c$ term in (21.6), and it changes no ranking.

**The trap:** Keeping the 90 and selling the 70 because the 70 is the weaker credit. That is the banker's instinct and here it is backwards: selling the 70 recovers less than half as much (\$0.54mm against \$1.26mm). The cousins of the same mistake are haircutting the whole 8.4% bucket instead of the \$3.6mm excess, and believing that selling the 55 loan cures anything; it merely turns the \$1.62mm haircut you already carry into a realized loss of the same size.

**If you got this wrong, read:** §4C.4 (the Math, Gently box "The OC test, and why the haircut picks the wrong loan"), then §21.4.1 and the cure-trade theorem in §21.4.2.

**Z.4-C.2: When does drift win?**

**Answer:** About $1{,}736$ trading days with the rounded drift of 0.036 a day, which is 6.9 years. With the unrounded drift $9/252$ it is exactly $1{,}764$ days, 7.0 years of 252 days. At that horizon the expected gain equals one standard deviation of the P&L, 63 points. (Physical measure $\mathbb{P}$: this is the two seats' shared opinion about the real path. Units: trading days; points of price.)

**How:** Expected gain is $\mu T$ and the one-standard-deviation swing is $\sigma\sqrt{T}$, so their ratio is

$$
\frac{\mu T}{\sigma\sqrt{T}} = \frac{\mu}{\sigma}\sqrt{T} = 1 \quad\Longrightarrow\quad T = \Big(\frac{\sigma}{\mu}\Big)^2 = \Big(\frac{1.5}{0.036}\Big)^2 \approx 1{,}736.
$$

In annual terms the gain-to-swing ratio after one year is $9/23.8 = 0.38$, and it grows only as $\sqrt{T}$, so it reaches one at $T = 1/0.38^2 \approx 7$ years. Two sanity checks make the answer honest. The chance of finishing ahead is $\Phi\big((\mu/\sigma)\sqrt{T}\big)$, which is $\Phi(0.38) = 65\%$ after one year and only $\Phi(1) = 84\%$ after seven, so even a right opinion loses money about a third of the time at the pod's own horizon. And 63 points of drift is three times the 21 points between 79 and par, so read the number as a statement about a ratio, not a forecast: the bond resolves long before the arithmetic does.

**The trap:** Dropping the square root. Setting $0.036\,T = 1.5$ gives $T \approx 42$ days, which is the horizon at which drift beats one day of noise, and the conclusion "the pod wins inside two months" is exactly the wrong lesson. The second slip is solving for $\sqrt{T} = 41.7$ and stopping there, reporting 42 days. The point of the exercise is that the patient seat is not counting on drift to beat noise; it is counting on not being forced out first.

**If you got this wrong, read:** §3.1.3 (a typical move grows like $\sqrt{h}$), then the Math, Gently box in §4C.1 with Figure 4-C.2; §28.6 has the hitting probability with drift that the box defers to.

**Z.4-C.3: Capital per spread**

**Answer:** The BBB private placement is the better use of capital: $230/1.3 \approx 177$ basis points of spread per point of capital charge, against $340/3.5 \approx 97$ for the BB. The BB ties at a factor of $340/177 \approx 1.92\%$. (Units: spreads in basis points over Treasuries, factors in percent of market value. This ratio is gross of expected loss.)

**How:** Rank by spread divided by the capital each bond consumes. The tie condition is

$$
\frac{340}{f} = \frac{230}{1.3} \quad\Longrightarrow\quad f = \frac{340 \times 1.3}{230} = 1.92\%.
$$

So the BB's factor would have to fall by 45%, from 3.5% to 1.92%; or, at its current factor, its spread would have to widen to $177 \times 3.5 \approx$ T+619. A second way to see it: the BB's extra 110 bp costs an extra 2.2 points of capital, which is 50 bp per point, barely a quarter of the 177 the private earns on its own capital, so the marginal dollar of capital belongs in the private. The ratio is a first screen, not a return on capital: it leaves out expected loss, and the BB's is larger, which only strengthens the ranking.

**The trap:** Picking the BB because 340 is more than 230. Spread is the numerator; the insurer's scarce input is capital, and the denominator is where the 3.5% sits. If you got the ranking right and then botched the tie, the usual slip is inverting the scaling, $1.3 \times 230/340 = 0.88\%$, which is the wrong direction: the BB has to get cheaper in capital, so its tie factor must be above the private's 1.3%.

**If you got this wrong, read:** §4C.5 (the Math, Gently box "Spread per unit of capital"), then §17.5.2 (the capital funnel).

**Z.4-C.4: Kaz's hedge**

**Answer:** Two clean ways, both while Owen is right about the patents. First, a flow that hits one leg before the default day: on day 12 the pair lost \$196,000 with the thesis unchanged, of which about \$163,000 was the CLO month-end landing on the long and about \$33,000 was the ruler (a ratio sized for default, not for an ordinary day). Second, the borrow: a recall when the unsecured holders organize forces a buy-in of the 2031s, and a fee reset to 6% takes net carry from about \$105,000 a year to about \$20,000. Friction is a third (a one-point half-spread on both legs costs about \$138,000 each way, more than a year of carry), and a rise in the financing haircut on the long is a fourth the chapter does not model. (P&L in \$mm; the hedge is a statement about the default state at Owen's own recoveries of 60 and 5.)

**How:** First read what "hedged" means. The ratio is $h = (79-60)/(55-5) = 0.38$ face per face, chosen so that the default-day P&L is zero:

$$
10\,(R_{\text{sec}} - 0.79) + 3.8\,(0.55 - R_{\text{unsec}}) = 0 \quad\text{at}\quad R_{\text{sec}} = 0.60,\; R_{\text{unsec}} = 0.05.
$$

So the pair is flat on one day, in one state, and says nothing about the weeks before. Now the day-12 leak. The long fell 5 points (−\$500,000) and the 2031s fell 8 (+\$304,000 on the \$3.8mm short): net −\$196,000. Scale the 2031s' 8 points by the ratio of each bond's distance from par to recovery, $8 \times 40/95 = 3.4$ points, and the long "should" have fallen \$337,000; the difference from the short's gain is the ruler, \$33,000, and the other 1.6 points on the long, \$163,000, is the CLOs' month-end. The carry arithmetic is the same kind of leak: $725 - 435 - 228 + 43 \approx 105$ in \$000 a year, and at a 6% fee the rebate on the \$2.13mm of collateral turns from $+43$ to $-43$, leaving about 20.

**The trap:** "It can only lose if Owen is wrong about the patents." That reads a hedge sized for one state on one day as a hedge for the whole life of the trade. The most common concrete answer, interest rates, is the weakest: the chapter puts the leftover rate exposure at about \$1,300 a basis point (I took that as given; the chapter lists no durations), less than an afternoon's bid-ask. The real leaks are the other seats' calendars, the ruler, the borrow and the carry.

NOTE (for the editor): The printed solution says the pair "was sized jump-to-default flat, not spread flat, and lost about \$200,000 on day 12." The \$196,000 is right, but the chapter's own "What leaks" paragraph attributes only about \$33,000 of it to the ruler; about \$163,000 is the CLO month-end landing on one leg. As worded, the solution sends the reader to the wrong cause. Suggest: "a flow that hits one leg before default (\$163,000 of the \$196,000 on day 12) and the ruler (\$33,000)".

NOTE (for the editor): In the same "What leaks" paragraph the long's implied move is "about three and a half" points and the remainder "a point and a half, about \$163,000". The scaling is $8 \times 40/95 = 3.37$ points, which leaves $5 - 3.37 = 1.63$ points, and 1.63 points on \$10mm is \$163,000; "a point and a half" on \$10mm would be \$150,000. The dollar figure is right and the two roundings are not. Suggest "about three and a third" and "about a point and two-thirds".

**If you got this wrong, read:** §4C.3 (the box "The Pair", especially "What leaks" and "What it costs"), §3B.6 (mistake 2, the jump-to-default hedge and the right ruler on the wrong day), and §8D.4 and §8D.5 (two jump processes; sizing to the stop).

**Z.4-C.5: Discount obligations**

**Answer:** A discount obligation is a loan the CLO buys well below par (the indenture sets the entry threshold, often 80 to 85 per §21.4.1) that the OC numerator carries at the price paid, not at par, until the loan trades above about 90 for more than 30 days. At 72 Halvorsen's loan is below every version of that threshold. So a purchase at 72 is neutral for the test, builds no par, and keeps the upside: the carrying value snaps to par on recovery, +\$2.8mm per \$10mm of par. That is why a manager with room in the CCC bucket may buy it, and why holding beats selling for a manager who is not in excess. (Units: \$mm of numerator per \$10mm par; prices in cents on the dollar.)

**How:** Buy \$10mm par at 72. Cash goes out at \$7.2mm, and principal cash counts at par in the numerator; the loan comes in carried at \$7.2mm. The change in the numerator is zero. Compare the same \$10mm bought at 85 and not caught by the rule: \$8.5mm of cash becomes \$10mm of counted par, a free +\$1.5mm, which is exactly the par-building the rule exists to stop. Then the paths for the loan bought at 72, per \$10mm par:

$$
\Delta_{\text{numerator}} = +2.8 \ \text{(trades above 90 for 30 days, carried at par)}, \qquad +1.3 \ \text{(sold at 85: cash 8.5 against carrying 7.2)}.
$$

On a default it is the lower of market and agency recovery. So the test sees the good tail and almost none of the bad, which is the barrier digital of §21.4.1. Two conditions make it a trade. The loan is Caa1, so it lands in the CCC bucket, and a pool already over the limit (Rachel's flagship at 7.9% against 7.5%) would only enlarge an excess haircut at its worst price; the buyer needs headroom. And "rather than sell" has a mirror image: a loan held since issue is counted at par whatever the screen says, so selling it at 72 converts 100 in the numerator into 72, a 28-point hit, unless it is part of the excess. Selling pays only where it removes a haircut bigger than the loss it realizes, which is the logic of Exercise 1.

**The trap:** Believing that buying at 72 builds 28 points of par, since \$7.2mm of cash "becomes" \$10mm of loan. The discount-obligation rule carries it at \$7.2mm until the price proves itself. The other wrong answers are Kaz's (a discount obligation is a loan with an embarrassingly low coupon) and "no CLO would buy a Caa1 loan"; the bucket allows it if there is room.

**If you got this wrong, read:** §21.4.1 (the discount set and equation 21.5), then §4C.4 (the numerator as Kundu states it: par, plus recovery value of defaulted loans, plus the purchase price of discount obligations, minus the CCC excess adjustment).

**Z.4-C.6: ROBO, again**

**Answer:** ROBO builds a list of every account that sold. That is a description of the tape, not a flag. "Forced" is a property of a vehicle's state before it trades (how much slack it has to a rule, and the date the rule is next checked), so the right object is a `SeatState` record per vehicle, summed into `forced_pressure`: a number in $[0, 1]$, the share of the issue held by CLO vehicles near a binding test inside the horizon, weighted by nearness. (Units: share of outstanding face; slack in decimal, so 0.02 is two points of cushion.)

**How:** The label "forced seller" cannot be read off who sold, because the sale is the outcome and the flag has to come before it; a flag built on the outcome sees Annika's guard-driven exit, Dana's limit-driven exit and a discretionary trim as the same thing. Listing 4-C.1 (Appendix F) keeps the state instead. Each record carries the vehicle, face, as-of date, rule, next check date and slack, and each CLO record that is under 45 days old, with a test date within 30 days, contributes

$$
\frac{\text{face}_i}{\text{outstanding}} \times \tau(s_i), \qquad \tau(s) = \begin{cases} 1 & s \le 0 \\ e^{-s/0.02} & s > 0. \end{cases}
$$

So a CLO at its limit counts fully, one with two points of cushion counts $e^{-1} = 0.37$ (about a third, as the chapter says), one with four points counts $0.14$. As an illustration with my own numbers, not the chapter's: five CLOs holding \$88mm of a \$900mm term loan, with cushions from 0.1 to 5 points, score only about 0.05, and the two largest holders, \$25mm and \$18mm sitting within half a point of the limit, provide 83% of it. The score is a statement about supply and nothing about value; it is poor for insurers and private placements, and the pre-emptive seller who still shows as a holder in last month's report is caught by cross-checking against TRACE volume since the as-of date.

**The trap:** Doing what was asked: returning the seller list. It is the answer the sentence invites and the one an unguided model produces, but every account that sold was by definition a seller, so the list explains nothing and predicts nothing. The close second is keying the score on manager names instead of vehicle-level state (the "logo" failure in "Ways This Blows Up").

NOTE (for the editor): The chapter says "On day 8, before the downgrade, Halvorsen's version of that number was already high" (§4C.4) and that "the day-8 `forced_pressure` reading had flagged" the CLO selling (the PB-02 box). The listing returns 0.0 whenever `rated_ccc` is false, and Halvorsen's loan was not cut to Caa1 until day 9. I ran Listing 4-C.1 on five illustrative CLO records: day-8 result 0.0 with `rated_ccc=False`, 0.0515 with `rated_ccc=True`. Even then the cushion used would be the reported one (Rachel's flagship at 7.3% against 7.5%, slack +0.2 points, tightness 0.90), when the pro-forma slack after the loan's own downgrade is $7.5\% - 7.9\% = -0.4$ points. To make the day-8 claim true the gate needs "one notch from CCC or on negative watch" (compare "Ways This Blows Up" (3) in §21.4.3) and a pro-forma slack field. Otherwise the text should say "day 9".

NOTE (for the editor): §4C.9 says "Chapter 21 uses the score as `forced_pressure` (§21.4, §21.7)". The string `forced_pressure` does not appear in Chapter 21; the index there is the Forced-Sale Pressure Index (FSPI) of §21.4.3, which weights each CLO by a logistic function of junior cushion and CCC excess, not by $e^{-s/0.02}$. Either rename or add a sentence saying that the two are the same idea with different functional forms.

**If you got this wrong, read:** §4C.9 ("The seat state vector", plus the Listing 4-C.1 text there), then §21.4.3 (the CLO Forced-Sale Pressure Index) for the calibrated version.

**Also checked in passing.** While verifying the boxes I recomputed every dollar figure in the chapter's Math, Gently boxes and the PB-02 box (Dana's \$1,987,500 and \$1,837,500, the \$240,000 transaction-cost line, the OC \$0.84mm, \$0.46mm and \$0.28mm, the LTV ladder 5% to 55% and 12% to 119%, the 61, 82 and 100 cents averaging 79, the insurer's 92, 81, 75.5, 72.75, and the pair's \$725,000, \$435,000, \$228,000, \$43,000 carry and \$114,000 coupon) and the stop-touch figures behind Figure 4-C.2 (touch probabilities of 0.42 and 0.41 with drift, drift captured 0.5 and 6.7 points, exit costs 1.3 and 1.2). All agree except the two items below.

NOTE (for the editor): The cold open says the carry line reads "+\$2,417, three days of coupon on \$12mm under 30/360". Annual coupon on \$12mm at 7.25% is \$870,000, which is \$2,416.67 per 30/360 day; three days is \$7,250. \$2,417 is one day. Either say "one day of coupon" or make the line +\$7,250 (Friday to Monday is three 30/360 days).

NOTE (for the editor): The seat table in §4C.9 gives the dealer's check as "Daily; committee on day 3". The text puts the risk committee on Wednesday, which is day 4 (the cold open fixes day 3 as Tuesday), and has Dana selling on Tuesday ahead of it. As I read it the table should say "committee on day 4; sold ahead of it on day 3".

<!-- STATUS: COMPLETE -->
