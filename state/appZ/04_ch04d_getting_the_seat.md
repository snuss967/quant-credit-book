## Z.4-D Chapter 4-D: Getting the Seat: Interviews for Market-Making and Systematic Credit, From Probability Puzzles to the Thirty-Minute Credit Pitch, and the Portfolio That Proves It

Use this bank the way the interview uses you. Do each problem cold, with a timer set to the minutes in the §4D.12 table (those are for a prepared reader, so allow half again if the idea is new), write your answer down, and only then read mine. Check the **Answer** line first; read **How** only if you missed. The bank has no inputs for a few problems, so where I had to pick numbers I say so and mark them illustrative. Throughout, $\mathbb{P}$ is the physical measure (what will actually happen) and $\mathbb{Q}$ is the risk-neutral measure (what the price implies); half the traps in this chapter are a number carried across that line.

**The problem bank (§4D.12)**

**Z.4-D.P1: The Q-default probability of a two-point bond [Read]**

**Answer:** $q_D = 25\%$. This is a risk-neutral ($\mathbb{Q}$) probability, one year, zero rates.

**How:** The price is the mean of the payoffs under the weights that make the bond a fair bet to someone who is indifferent to risk:

$$
85 = 100(1-q_D) + 40\,q_D = 100 - 60\,q_D \quad\Longrightarrow\quad q_D = \frac{15}{60}.
$$

Fifteen points of discount to par, divided by a sixty-point loss on default. Say the measure out loud when you answer; the interviewer's "In which measure?" is the whole question.

**The trap:** Answering "25% chance the company defaults." That is a statement about the price, not about the company. The physical probability is lower by whatever the market pays for the jump (P4 puts a number on it). The arithmetic slips are close behind: $15/40 = 37.5\%$ divides by the recovery instead of the loss, and $15\%$ treats the discount as a probability, which silently assumes a total loss.

**If you got this wrong, read:** §4D.2, then the $\mathbb{P}$ and $\mathbb{Q}$ box in §5.1.1.

**Z.4-D.P2: The same bond at a 4% continuous rate [Derive]**

**Answer:** $q_D = 19.2\%$ ($\mathbb{Q}$, one year, 4% continuous).

**How:** Today's price is the discounted $\mathbb{Q}$-expectation, so the undiscounted expected payoff is the price grown at the rate:

$$
85\,e^{0.04} = 88.47 = 100 - 60\,q_D \quad\Longrightarrow\quad q_D = \frac{11.53}{60} = 0.192.
$$

The rate has absorbed 5.8 points of the 25%; the chapter's "six points" is the same number rounded. With rates at 4%, part of the 15-point discount to par is just time value, and only 11.53 points of it is expected default loss.

**The trap:** Discounting the wrong way. Multiplying the price by $e^{-0.04}$ gives $81.67$ and a $q_D$ of $30.6\%$, which is the right formula run backwards. The other common slip is leaving the rate out and quoting 25% as if rates were zero; the interviewer's follow-up exists to catch exactly that.

**If you got this wrong, read:** §4D.2, paragraph beginning "The interviewer added two follow-ups".

**Z.4-D.P3: Add an exchange door at 70 [Derive]**

**Answer:** Any weights $(a,b,c)$ on par, the 70 exchange and the 40 default with $b = 0.5 - 2c$ and $a = 0.5 + c$, for $0 \le c \le 0.25$, price at 85 under $\mathbb{Q}$. Two of them: $(0.60, 0.30, 0.10)$, which has a 10% default probability, a 40% chance of not being paid in full and a standard deviation of 20.1 points; and $(0.50, 0.50, 0)$, which has no default probability at all and a standard deviation of 15.

**How:** Two equations, three unknowns. Set $a + b + c = 1$ and $100a + 70b + 40c = 85$, substitute $a = 1 - b - c$, and you get $15 = 30b + 60c$, i.e. $b + 2c = 0.5$. One weight is left free, and the price cannot pin it down. The corner $c = 0.25$, $b = 0$ is the original two-point bond.

**The trap:** Reading 25% off the price as "the" default probability once a third outcome exists. With the exchange door open, the same 85 is consistent with default probabilities anywhere from 0 to 25%. The price gives you the mean; the shape is a model, and the model's biggest input is whether the door exists, which is a question about the credit agreement.

**If you got this wrong, read:** §3.1.2 (three outcomes), then §4D.2, paragraph beginning "Now there's a third outcome."

**Z.4-D.P4: What a 10% physical PD says about the 85 bond [Derive]**

**Answer:** Under $\mathbb{P}$ (10% default, one year, zero rates) the expected payoff is 94, so a buyer at 85 expects $94/85 - 1 = 10.6\%$. It is paid for bearing the jump: the market weights default at 25% ($\mathbb{Q}$) against your 10% ($\mathbb{P}$), and $(0.25 - 0.10) \times 60 = 9$ points of price is the risk premium.

**How:** Re-weight the same two outcomes with your probabilities:

$$
\mathbb{E}^{\mathbb{P}}[V] = 0.9(100) + 0.1(40) = 94, \qquad \frac{94 - 85}{85} = 10.6\%.
$$

The 10.6% is an average of two very different years: $+17.6\%$ if the bond survives, $-52.9\%$ if it does not. Nobody earns the average in any single year.

**The trap:** Calling the 15-point gap between 25% and 10% a forecasting error, or free money. The market is not wrong; it is charging for the right to hold a bond that can lose 60 points overnight, in the bad states where a dollar hurts most. The smaller slips are dividing the 9 points by 100 (9%) instead of by the price paid, and forgetting that the premium is earned only in expectation.

**If you got this wrong, read:** §5.1.1 ($\mathbb{P}$ and $\mathbb{Q}$ box), then §4D.2.

**Z.4-D.P5: Which measure for a hedge, a size, a forecast? [Read]**

**Answer:** CDS hedge: $\mathbb{Q}$. Kelly size: $\mathbb{P}$. P&L forecast: $\mathbb{P}$.

**How:** Ask what the number is for. A hedge ratio and any relative value against CDS are pricing questions: they use the weights that reproduce today's prices, which is $\mathbb{Q}$. A size and a forecast are statements about what will actually happen to your money, which is $\mathbb{P}$. Prices, hedges and relative value live in $\mathbb{Q}$; sizing, Kelly and your P&L live in $\mathbb{P}$. The hedged book is then forecast in $\mathbb{P}$ again: you price the hedge in $\mathbb{Q}$ and still have to say what you expect to earn.

**The trap:** Feeding a CDS-implied default probability into a Kelly size or an expected-return forecast. Under $\mathbb{Q}$ nobody has an edge by construction, so Kelly returns zero (P30), and the usual "fix" is to splice a market spread to a historical default rate and an agency recovery. The reverse error, a historical default rate inside a CDS relative-value trade, produces a mispricing that is really a confusion.

**If you got this wrong, read:** §4D.2 ("Math, Gently" box and the paragraph after it), then §28.4, subsection "Which measure, and which loss".

**Z.4-D.P6: Hazard rate from a 300 bp spread [Derive]**

**Answer:** $\lambda^{\mathbb{Q}} \approx 0.03/0.60 = 5\%$ a year, a risk-neutral intensity.

**How:** The credit triangle says spread $\approx$ hazard $\times$ loss given default, $s = \lambda(1-R)$. With $s = 300$ bp and $R = 40\%$,

$$
\lambda^{\mathbb{Q}} = \frac{0.03}{0.60} = 0.05.
$$

For a flat curve with continuous premium the relation is exact; with quarterly coupons it is a hair off. Risk-neutral survival to one year is $e^{-0.05} = 95.1\%$, so the $\mathbb{Q}$ one-year default probability is 4.9%. Remember the 40% is a quoting convention: a CDS spread identifies only the product $\lambda(1-R)$. If you change $R$, $\lambda$ moves the other way.

**The trap:** Dividing by the recovery ($0.03/0.40 = 7.5\%$) instead of the loss, or reading the 5% as a physical default rate. It is a $\mathbb{Q}$ number, so the actual default rate for this credit is lower.

**If you got this wrong, read:** §6.8.3 (the bootstrap and the credit triangle).

**Z.4-D.P7: Variance of the two-point and three-point bonds [Derive]**

**Answer:** Both bonds are priced at 85 under $\mathbb{Q}$. Two-point (100 or 40, weights 0.75/0.25): variance 675, standard deviation 26.0 points. Three-point (100, 70, 40 with weights 0.6/0.3/0.1): variance 405, standard deviation 20.1 points.

**How:** For two points, $\operatorname{Var} = p(1-p)\,\Delta^2 = 0.75 \times 0.25 \times 60^2 = 675$. For three points with no spread inside each outcome the law of total variance has only its between-scenario term:

$$
0.6(15)^2 + 0.3(15)^2 + 0.1(45)^2 = 135 + 67.5 + 202.5 = 405.
$$

The exchange door put 30% of the weight halfway down, so the typical surprise shrinks even though there are more outcomes.

**The trap:** Assuming the same price means the same risk, or that adding an outcome adds variance. Same mean, different variance, different default probability (25% against 10%). Other weightings that price at 85 give other answers; $(0.5, 0.5, 0)$ gives 15.

**If you got this wrong, read:** §3.1.1 (variance of a two-point distribution), then §3.1.2 (the law of total variance).

**Z.4-D.P8: Q-PD across recoveries 20 to 60 at a price of 85 [Build]**

**Answer:** $\mathbb{Q}$ default probability, one year, zero rates: 18.8% at $R = 20$, 21.4% at 30, 25.0% at 40, 30.0% at 50 and 37.5% at 60. The product $q_D(100 - R)$ is 15 in every row.

**How:** Extend Listing 4-D.1's `measure_drill` formula, $q_D = (100 - P e^{r})/(100 - R)$, into a function `q_by_recovery(price, recoveries, rate=0.0)` that returns a dictionary keyed by recovery. Write the tests first: $R = 40$ gives exactly 0.25; $r = 4\%$ at $R = 40$ gives 0.192; $q_D$ rises strictly with $R$; the loss rate $q_D(100-R)$ equals $100 - Pe^{r}$ for every $R$; and a price at or below the recovery raises an error, because the formula returns $q_D \ge 1$ and that is an arbitrage in the quote, not a probability. The expected output is the five-row table above.

**The trap:** Treating the 25% as a fact about the company. The price pins down one number, the expected loss of 15 points, and a recovery assumption splits it into a probability and a severity. A higher assumed recovery raises the implied probability, which surprises people.

**If you got this wrong, read:** §4D.2, then §5.5.6 (the 40% that is neither a $\mathbb{P}$ nor a $\mathbb{Q}$ recovery).

**Z.4-D.P9: One seller in five is informed: bid and ask [Derive]**

**Answer:** Bid 64, ask 76, in price points, under $\mathbb{P}$ (the dealer's own beliefs). The 12-point spread has no fee in it.

**How:** Prior one-half on 40 or 100, so the mid is 70 and $\sigma_V = 30$. On a bad day (value 40) a sale arrives 20% + 80% $\times$ 0.5 = 60% of the time; on a good day only 80% $\times$ 0.5 = 40%. Bayes gives a posterior of 0.6 on the bad state, so

$$
b = 0.6(40) + 0.4(100) = 64, \qquad a = 76 .
$$

This is Glosten–Milgrom, $b = m - \pi\sigma_V = 70 - 0.2 \times 30$. The dealer has no inventory cost, no risk aversion and no funding bill, and the spread is still 12 points: it is insurance against the one seller in five who knows.

**The trap:** Bidding the unconditional average, 70. A dealer who does that pays for the seller's decision to sell every time. The fact that someone chose to sell to you is itself evidence about the bond.

**If you got this wrong, read:** §3.2.1 (the binary model), then §4D.3.

**Z.4-D.P10: The bid after a second sale from a new seller [Derive]**

**Answer:** 58.5 (58.46), under $\mathbb{P}$. The posterior on the bad state is 0.692.

**How:** Each sale multiplies the odds of the bad state by the same likelihood ratio, $0.6/0.4 = 1.5$. One sale takes the odds from 1 to 1.5; a second takes them to $1.5^2 = 2.25$, a posterior of $2.25/3.25 = 0.692$, and

$$
b_2 = 100 - 60 \times 0.692 = 58.46 .
$$

Odds are the natural currency here because independent evidence multiplies. The ask after one sale is exactly 70: a buy undoes the sale and returns the posterior to one-half, so the spread has narrowed from 12 to 11.5.

**The trap:** Updating on the second sale as if it were the first, which restarts at fifty-fifty and bids 64 again. It is the base-rate trap of §3.4.3 run in reverse: instead of ignoring the prior, Theo ignored the posterior. Another slip is adding probabilities ($0.6 + 0.1$) when the odds multiply.

**If you got this wrong, read:** §4D.3, then §3.4.3 (the base-rate trap).

**Z.4-D.P11: The bid after a second sale from the same seller [Derive]**

**Answer:** Posterior $2/3$ on the bad state, so a value (and bid) of 60 under $\mathbb{P}$, against 58.5 for two strangers.

**How:** A single counterparty has one type. If the seller is informed (20%), it sells twice whenever the value is low; if uninformed (80%), each sale is an independent coin. So

$$
P(\text{two sells} \mid 40) = 0.2 + 0.8 \times 0.25 = 0.4, \qquad P(\text{two sells} \mid 100) = 0.8 \times 0.25 = 0.2,
$$

and the posterior is $0.4/(0.4 + 0.2) = 2/3$, giving $100 - 60 \times 2/3 = 60$. An informed seller would have sold twice anyway, so the repeat carries less fresh news than a second stranger does.

**The trap:** Treating the repeat as a new seller and bidding 58.5. The two sales are not independent evidence: the second is partly the same fact as the first. It is the opposite of Theo's Monday error, where he forgot the first sale altogether.

**If you got this wrong, read:** §4D.13, Exercise 3 (the same seller twice), then §3.2.1.

**Z.4-D.P12: How many sales push the value below 50? [Derive]**

**Answer:** Four sales from four new sellers, under $\mathbb{P}$. The value is 53.7 after three and 49.9 after four.

**How:** Value $= 100 - 60p$ with $p = 1.5^n/(1 + 1.5^n)$. Setting the value below 50 needs $p > 5/6$, i.e. posterior odds above 5, so

$$
1.5^n > 5 \quad\Longrightarrow\quad n > \frac{\ln 5}{\ln 1.5} = 3.97 .
$$

The fourth sale clears it by a whisker: $1.5^4 = 5.06$. Six sales take the value to 44.8, which is the chapter's "about 45".

**The trap:** Rounding 3.97 down to 3. Three sales leave the value at 53.7, nearly four points short. Or treating each sale as worth a fixed six points (the first one is): the sixth sale is worth only 2.1, because the posterior saturates as it nears certainty.

**If you got this wrong, read:** §4D.3, including the Poker Table box.

**Z.4-D.P13: Why the spread narrows as the posterior moves [Read]**

**Answer:** The spread is the price of what the next trade can still teach you, and that shrinks as you approach certainty. In the §4D.3 setup it runs 12.0, 11.5, 10.3, 8.6, 6.7, 5.1 and 3.7 points after zero to six sales (price points, $\mathbb{P}$).

**How:** The half-spread in Glosten–Milgrom is proportional to the variance of the current belief. For a small informed fraction, $m - b \approx 2\pi\,p(1-p)\,\Delta$, so the full spread is about $48\,p(1-p)$ with $\pi = 0.2$ and $\Delta = 60$. It peaks at 12 when $p = \tfrac12$ and falls as $p$ heads to 0.92, where $p(1-p) = 0.074$. Information is variance reduction. A sale moves the mid (70 to 64 to 58.5); it does not widen the market.

**The trap:** Widening after being hit, on the instinct that "the market is moving against me, so I'm less sure." You have just learned something, so you are more sure, and the dealer who widens pays the informed client at every step while the dealer who moves the mid pays once. The converse trap is never widening at all: if you doubt $\pi$ itself, that is model uncertainty and is a separate charge.

**If you got this wrong, read:** §4D.3 (the Poker Table box), then §3.1.1 ("Information is variance reduction").

**Z.4-D.P14: Informed fraction uniform on 0 to 0.4: the bid [Derive]**

**Answer:** 64 (price points, $\mathbb{P}$), the same as for a known $\pi = 0.2$.

**How:** The bid depends on $\pi$ only through $\pi\sigma_V$, which is linear, so only $\mathbb{E}[\pi] = 0.2$ matters: $70 - 0.2 \times 30 = 64$. Integrating the joint likelihoods over $\pi$ agrees: the probability of a sale is $(1+\pi)/2$ in the bad state and $(1-\pi)/2$ in the good, both linear in $\pi$, so the posterior is $(1 + 0.2)/2 = 0.6$. In this symmetric setup a single sale carries no information about $\pi$ itself, since $P(\text{sale}) = \tfrac12$ for every $\pi$. If the same unknown $\pi$ sits behind two sales, the bid is 58.6 instead of 58.5.

**The trap:** Quoting for the worst case, $\pi = 0.4$, which bids 58 and loses every uninformed seller. A subtler one: averaging the bids rather than the joint. With a lopsided prior (say $q = 0.7$, $\Delta = 20$) the posterior is a ratio, and averaging ratios gives a half-spread of 1.88 where the right answer is 1.83, the ratio at $\mathbb{E}[\pi]$.

**If you got this wrong, read:** §3.2.2 (making $\pi$ a function of the RFQ), then §3.2.1.

**Z.4-D.P15: The winner's curse with three dealers [Derive]**

**Answer:** The winning dealer's estimate is too high by $3\sigma/(2\sqrt{\pi}) = 0.846\,\sigma$ on average, where $\sigma$ is each dealer's error, in the units of the price (physical measure, common-value bond). With $\sigma = 1$ point the winner overpays 0.85 points.

**How:** Every dealer's estimate is unbiased, but the winner of a sell RFQ is the one with the highest bid, so it is the maximum of three independent errors. The expected maximum of $n$ standard normals is 0 for one dealer, 0.564 for two, 0.846 for three, 1.164 for five and 1.424 for eight (checked by quadrature). To break even you bid as though you already knew you had won: shade by that amount, and shade more as $n$ grows.

**The trap:** Reasoning that your estimate is unbiased, so your bid is fair. Unbiased before winning is not unbiased after winning; winning selects the most optimistic error. The cure is not a better estimate. It is shading, in proportion to $\sigma$ and increasing in the number of dealers in the room.

**If you got this wrong, read:** §3.2.3 (many dealers, the winner's curse), then §18.9 (the BWIC as a first-price auction).

**Z.4-D.P16: Simulate fifty RFQs and plot the hand history of posteriors [Build]**

**Answer:** A function `hand_history(n=50, pi=0.2, v_lo=40, v_hi=100, seed=None)` that returns, per RFQ, the flow (sell or buy), the posterior on the low state, and the next bid and ask. It plots the posterior as a line with the quote band around it and the sells and buys marked.

**How:** Draw the true value once. Each arrival is informed with probability $\pi$ (it sells only if the value is low, buys only if high) or a fair coin otherwise. The posterior odds of the low state are multiplied by $(1+\pi)/(1-\pi) = 1.5$ on a sale and divided by 1.5 on a buy. Tests first: quotes 64/76 before any trade; one sale gives a posterior of 0.6 and next quotes 58.46/70.0; sell-then-buy returns to 0.5 (only the net count matters); $\pi = 0$ leaves the posterior at 0.5; the spread tracks $48\,p(1-p)$. Over 20,000 hands, the mean final posterior is 0.89 in low-state hands (77% above 0.9), 0.11 in high-state hands and 0.51 overall (the posterior is a martingale). A dealer quoting from the posterior earns −0.01 ± 0.01 points a fill when the true $\pi$ is 0.2. Plant $\pi = 0.5$ and the same dealer loses 1.38 a fill, while a dealer frozen at 64/76 loses 9.03.

**The trap:** Testing only that the plot looks plausible. The markout test, which recovers the planted toxicity, is the one that fails when the update is wrong.

**If you got this wrong, read:** §3.3 (markouts, the hand history), then §4D.3 and Figure 4-D.3.

**Z.4-D.P17: A 90% interval for US HY index issuers, May 2018 [Read]**

**Answer:** 784 issuers on 31 May 2018, of which 576 had public equity (Dynkin, as quoted in §7.1). A calibrated interval made before looking, for instance 500 to 1,200, would have caught it.

**How:** The chain behind a good guess: the index held roughly two thousand bonds, and issuers have a few bonds each, so a few hundred to about a thousand issuers, not tens of thousands. The point of the exercise is the units. The count that matters for a model is issuers (and fewer still after grouping by ultimate parent, and fewer again for anything needing an equity price), not bonds or bond-months. With forty thousand bond-months in a panel and 784 issuers, rows are not observations; issuers are, and slowly.

**The trap:** Answering in bonds or CUSIPs, where the true figure is two to three times larger. The other trap is overconfidence: a "90%" interval of 700 to 800 feels competent and misses most of the time (see P22). Check your interval after reading the source, then record whether it caught the number.

**If you got this wrong, read:** §7.1, Defect 2 ("the issuer is the observation"), then §7.6 for $N_{\text{eff}}$.

**Z.4-D.P18: Reservation-price shift at $q = -2$ [Derive]**

**Answer:** The reservation price sits $+0.0127 \approx 0.013$ points above the mid (price points, $\mathbb{P}$, short two \$1mm lots).

**How:** The Avellaneda–Stoikov reservation price is $r^{\text{res}} = S_t - q\,\gamma\,\sigma^2(T-t)$. With $q = -2$, $\gamma = 0.005$ per point-lot and $\sigma^2\tau = 1.27$ points squared,

$$
r^{\text{res}} - S_t = -(-2)(0.005)(1.27) = +0.0127 .
$$

A short dealer quotes higher to be bought back in. Here $\sigma^2\tau$ is already a variance times a time (a week's variance), so do not square or scale it again.

**The trap:** A sign error, or reaching for $(q + \tfrac12)$, which is the bid's distance in the AS quote, not the reservation price. The bigger trap is thinking it matters. One cent and a bit is pennies against the six points that Monday's single sale moved the value. In a bond, the client's information is large and the inventory skew is small, which is why a candidate who skews for inventory and not for information has the right formula for the wrong game.

**If you got this wrong, read:** §18.4.2 (the answer first), then §4D.4.

**Z.4-D.P19: The greed term at $k = 3$, $\gamma = 0.005$ [Derive]**

**Answer:** $\tfrac{1}{\gamma}\ln(1 + \gamma/k) = 200\ln(1.001667) = 0.333$ points per side, 0.666 points across the two sides (price points, $\mathbb{P}$).

**How:** This is the markup term of the AS spread, the part that survives when risk aversion goes to zero. Expand $\ln(1+x) \approx x - x^2/2$ to see it:

$$
\frac{1}{\gamma}\ln\!\Big(1 + \frac{\gamma}{k}\Big) \approx \frac{1}{k} - \frac{\gamma}{2k^2} = 0.3333 - 0.0003 .
$$

A risk-neutral dealer facing demand $Ae^{-k\delta}$ maximizes $\delta A e^{-k\delta}$ at $\delta^* = 1/k$, so this is pure market power and $k$ is the price elasticity of RFQ wins. Set it against the fear term $\gamma\sigma^2\tau = 0.0064$ per lot and greed is over 100 times larger: Kaz's quote was 94% greed.

**The trap:** Counting the per-side markup as the whole spread (it is half of the greed), or thinking a risk-neutral dealer quotes zero spread. With $\gamma = 0$ the markup is still $1/k$. The other slip is dropping the $1/\gamma$ prefactor, which gives $\ln(1.0017) = 0.0017$.

**If you got this wrong, read:** §18.4.2, "Limit 1: $\gamma \to 0$".

**Z.4-D.P20: A quote whose number has a document answer [Read]**

**Answer:** The page count of the 2016 Serta first-lien term loan agreement (Theo's cold open). Other examples from the chapter: an RFQ on a bond where the indenture answers "is the 2029 note structurally senior?" or "does the exchange need the holder's consent?"

**How:** A page count is not a random variable; it is a fact printed on a page, and the person asking may have the page. Any quote whose number the document settles is a market on a number that has an answer, and a counterparty who keeps buying is telling you so. The defense is the sentence Theo eventually said out loud: name the fact that moves your number and which way, then go and read it. Until you have, price it as if the other side has already read it, which is $\pi$ close to one.

**The trap:** Treating it as ordinary uncertainty and widening: every extra lift then pays the person holding the document to correct you. The fact that moves your number is rarely the one you were quoting; for Theo it was the exhibits stapled to the back.

**If you got this wrong, read:** §4D.4 (the "Ways This Blows Up" box on the number with a document answer), then §3.6 (who at this table knows about the LMT).
