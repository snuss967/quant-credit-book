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

**Answer:** Weights $(a,b,c)$ on par, the 70 exchange and the 40 default price at 85 under $\mathbb{Q}$ whenever $b = 0.5 - 2c$ and $a = 0.5 + c$, with $0 \le c \le 0.25$. Two of them: $(0.60, 0.30, 0.10)$, a 10% default probability, a 40% chance of not being paid in full, standard deviation 20.1 points; and $(0.50, 0.50, 0)$, no default probability at all, standard deviation 15.

**How:** Two equations, three unknowns: $a + b + c = 1$ and $100a + 70b + 40c = 85$. Substitute $a = 1 - b - c$ and you get $15 = 30b + 60c$, so $b + 2c = 0.5$. One weight stays free, and the price cannot pin it down. The corner $c = 0.25$, $b = 0$ is the original two-point bond.

**The trap:** Reading 25% off the price as "the" default probability once a third outcome exists. The same 85 is consistent with default probabilities anywhere from 0 to 25%. The price gives you the mean; the shape is a model, and its biggest input is whether the door exists, which is a question about the credit agreement.

**If you got this wrong, read:** §3.1.2 (three outcomes), then §4D.2, paragraph beginning "Now there's a third outcome."

**Z.4-D.P4: What a 10% physical PD says about the 85 bond [Derive]**

**Answer:** Under $\mathbb{P}$ (10% default, one year, zero rates) the expected payoff is 94, so a buyer at 85 expects $94/85 - 1 = 10.6\%$. It is paid for bearing the jump: default weighs 25% under $\mathbb{Q}$ and 10% under $\mathbb{P}$, and $(0.25 - 0.10) \times 60 = 9$ points of price is the risk premium.

**How:** Re-weight the same two outcomes with your probabilities:

$$
\mathbb{E}^{\mathbb{P}}[V] = 0.9(100) + 0.1(40) = 94, \qquad \frac{94 - 85}{85} = 10.6\%.
$$

That 10.6% averages two very different years, $+17.6\%$ if the bond survives and $-52.9\%$ if it does not. Nobody earns the average in any single year.

**The trap:** Calling the gap between 25% and 10% a forecasting error, or free money. The market is charging for a bond that can lose 60 points overnight, in the bad states where a dollar hurts most. Smaller slips: dividing the 9 points by 100 instead of by the price paid (9%), and forgetting the premium is earned only in expectation.

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

**Answer:** $\mathbb{Q}$ default probability, one year, zero rates: 18.8% at $R = 20$, 21.4% at 30, 25.0% at 40, 30.0% at 50, 37.5% at 60. The product $q_D(100 - R)$ is 15 in every row.

**How:** Extend Listing 4-D.1's `measure_drill` formula, $q_D = (100 - Pe^{r})/(100 - R)$, into `q_by_recovery(price, recoveries, rate=0.0)`, returning a dictionary keyed by recovery. Tests first: $R = 40$ gives 0.25; $r = 4\%$ at $R = 40$ gives 0.192; $q_D$ rises strictly with $R$; $q_D(100-R)$ equals $100 - Pe^{r}$ for every $R$; and a price at or below the recovery raises an error, since $q_D \ge 1$ is an arbitrage in the quote, not a probability. Expected output: the five rows above.

**The trap:** Treating 25% as a fact about the company. The price pins down one number, the 15-point expected loss, and a recovery assumption splits it into a probability and a severity. A higher assumed recovery raises the implied probability, which surprises people.

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

**The trap:** Updating on the second sale as if it were the first, which restarts at fifty-fifty and bids 64 again. It is the base-rate trap of §3.4.3 run in reverse: instead of ignoring the prior, Theo ignored the posterior. Another slip is adding the likelihood ratios ($1.5 + 1.5 = 3$) when they multiply ($1.5^2 = 2.25$).

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

**Answer:** The spread is the price of what the next trade can still teach you, and that shrinks as you near certainty. In the §4D.3 setup it runs 12.0, 11.5, 10.3, 8.6, 6.7, 5.1 and 3.7 points after zero to six sales (price points, $\mathbb{P}$).

**How:** The Glosten–Milgrom half-spread is proportional to the variance of the current belief. For a small informed fraction, $m - b \approx 2\pi\,p(1-p)\,\Delta$, so the full spread is about $48\,p(1-p)$ with $\pi = 0.2$ and $\Delta = 60$. It peaks at 12 when $p = \tfrac12$ and falls to 3.7 at $p = 0.92$. Information is variance reduction: a sale moves the mid (70 to 64 to 58.5), it does not widen the market.

**The trap:** Widening after being hit because "the market is moving against me, so I'm less sure." You have just learned something, so you are more sure. The dealer who widens pays the informed client at every step; the dealer who moves the mid pays once. (If you doubt $\pi$ itself, that is model uncertainty, a separate charge.)

**If you got this wrong, read:** §4D.3 (the Poker Table box), then §3.1.1 ("Information is variance reduction").

**Z.4-D.P14: Informed fraction uniform on 0 to 0.4: the bid [Derive]**

**Answer:** 64 (price points, $\mathbb{P}$), the same as for a known $\pi = 0.2$.

**How:** The bid depends on $\pi$ only through $\pi\sigma_V$, which is linear, so only $\mathbb{E}[\pi] = 0.2$ matters: $70 - 0.2 \times 30 = 64$. Integrating the joint likelihoods over $\pi$ agrees: the probability of a sale is $(1+\pi)/2$ in the bad state and $(1-\pi)/2$ in the good, both linear in $\pi$, so the posterior is $(1 + 0.2)/2 = 0.6$. In this symmetric setup a single sale carries no information about $\pi$ itself, since $P(\text{sale}) = \tfrac12$ for every $\pi$. If the same unknown $\pi$ sits behind two sales, the bid is 58.6 instead of 58.5.

**The trap:** Quoting for the worst case, $\pi = 0.4$, which bids 58 and hands the uninformed flow to a competitor. A subtler one: averaging the bids rather than the joint. With a lopsided prior (say $q = 0.7$, $\Delta = 20$) the posterior is a ratio, and averaging ratios gives a half-spread of 1.88 where the right answer is 1.83, the ratio at $\mathbb{E}[\pi]$.

**If you got this wrong, read:** §3.2.2 (making $\pi$ a function of the RFQ), then §3.2.1.

**Z.4-D.P15: The winner's curse with three dealers [Derive]**

**Answer:** The winning dealer's estimate is too high by $3\sigma/(2\sqrt{\pi}) = 0.846\,\sigma$ on average, where $\sigma$ is each dealer's error, in the units of the price (physical measure, common-value bond). With $\sigma = 1$ point the winner overpays 0.85 points.

**How:** Every dealer's estimate is unbiased, but the winner of a sell RFQ is the one with the highest bid, so it is the maximum of three independent errors. The expected maximum of $n$ standard normals is 0 for one dealer, 0.564 for two, 0.846 for three, 1.164 for five and 1.424 for eight (checked by quadrature). To break even you bid as though you already knew you had won: shade by that amount, and shade more as $n$ grows.

**The trap:** Reasoning that your estimate is unbiased, so your bid is fair. Unbiased before winning is not unbiased after winning; winning selects the most optimistic error. The cure is not a better estimate. It is shading, in proportion to $\sigma$ and increasing in the number of dealers in the room.

**If you got this wrong, read:** §3.2.3 (many dealers, the winner's curse), then §18.9 (the BWIC as a first-price auction).

**Z.4-D.P16: Simulate fifty RFQs and plot the hand history of posteriors [Build]**

**Answer:** `hand_history(n=50, pi=0.2, v_lo=40, v_hi=100, seed=None)` returns, per RFQ, the flow, the posterior on the low state and the next bid and ask, and plots the posterior with the quote band around it and sells and buys marked.

**How:** This is the §4D.3 recursion in miniature (Listing 3.2 is its large-scale cousin). Draw the true value once. Each arrival is informed with probability $\pi$ (sells only if the value is low, buys only if high) or a fair coin. A sale multiplies the odds of the low state by $(1+\pi)/(1-\pi) = 1.5$; a buy divides by 1.5. Tests first: quotes 64/76 before any trade; one sale gives posterior 0.6 and next quotes 58.46/70.0; sell-then-buy returns to 0.5; $\pi = 0$ never moves the posterior; the spread tracks $48\,p(1-p)$. Expected over 20,000 hands: mean final posterior 0.89 in low-state hands, 0.11 in high-state hands, 0.51 overall (a martingale). A dealer quoting from the posterior earns $-0.01 \pm 0.01$ points a fill at true $\pi = 0.2$; at a planted $\pi = 0.5$ it loses 1.38 a fill, and a dealer frozen at 64/76 loses 9.03.

**The trap:** Checking only that the plot looks plausible. The markout test that recovers the planted toxicity is the one that fails when the update is wrong.

**If you got this wrong, read:** §3.3 (markouts, the hand history), then §4D.3 and Figure 4-D.3.

**Z.4-D.P17: A 90% interval for US HY index issuers, May 2018 [Read]**

**Answer:** 784 issuers on 31 May 2018, of which 576 had public equity (Dynkin, quoted in §7.1). An interval written before looking, such as 500 to 1,200, would have caught it.

**How:** A defensible chain: the index held roughly two thousand bonds with a few bonds per issuer, so a few hundred to about a thousand issuers, not tens of thousands. The point is the unit. For a model the count that matters is issuers (fewer after grouping by ultimate parent, fewer again for anything needing an equity price), not bonds or bond-months. With forty thousand bond-months and 784 issuers, rows are not observations; issuers are, and slowly.

**The trap:** Answering in bonds or CUSIPs, where the figure is two to three times larger, or being overconfident: a "90%" interval of 700 to 800 feels competent and misses most of the time (P22). Write your interval down before you read the source, then record whether it caught the number.

**If you got this wrong, read:** §7.1 (Defect 2, "the issuer is the observation"), then §7.6 for $N_{\text{eff}}$.

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

A risk-neutral dealer facing demand $Ae^{-k\delta}$ maximizes $\delta A e^{-k\delta}$ at $\delta^* = 1/k$, so this is pure market power and $k$ is the price elasticity of RFQ wins. Set the two greed terms (0.666) against the fear term $\gamma\sigma^2\tau = 0.0064$ per lot and greed is over 100 times larger: Kaz's quote was 94% greed.

**The trap:** Counting the per-side markup as the whole greed in the spread (it is half), or thinking a risk-neutral dealer quotes zero spread. With $\gamma = 0$ the markup is still $1/k$. The other slip is dropping the $1/\gamma$ prefactor, which gives $\ln(1.0017) = 0.0017$.

**If you got this wrong, read:** §18.4.2, "Limit 1: $\gamma \to 0$".

**Z.4-D.P20: A quote whose number has a document answer [Read]**

**Answer:** The page count of the 2016 Serta first-lien term loan agreement (Theo's cold open). Others from the chapter: an RFQ on a bond where the indenture answers "is the 2029 note structurally senior?" or "does the exchange need the holder's consent?"

**How:** A page count is not a random variable; it is a fact printed on a page, and the person asking may have the page. A quote on such a number is a market on a number that has an answer, and a counterparty who keeps buying is telling you so. The defense is the sentence Theo eventually said: name the fact that moves your number and which way, then go and read it. Until then, price as if the other side has already read it, which means $\pi$ near one.

**The trap:** Treating it as ordinary uncertainty and widening. Every extra lift then pays the holder of the document to correct you. The fact that moves your number is rarely the one you were quoting; for Theo it was the exhibits stapled to the back.

**If you got this wrong, read:** §4D.4 (the "Ways This Blows Up" box on the number with a document answer), then §3.6.

**Z.4-D.P21: A 25% hit-ratio target: what does its shadow price buy? [Derive]**

**Answer:** Take §18.7's cold-open RFQ (illustrative: eight lots, $\beta_0 = 0$, $\beta_1 = 4$, credit view plus fear plus suspicion $d = 0.83$ points, every RFQ in the tier alike). A 25% win probability needs a bid only $x = \ln 3/\beta_1 = 0.275$ points under the composite, against 1.03 today (1.6%). The multiplier that gets there is $\nu = d + \text{greed}(x) - x = 0.83 + 0.33 - 0.275 = 0.89$ points per win, 18 times Ines's 0.05. It buys a bid near 90.98 instead of 90.22, at about 0.14 points of expected P&L per RFQ.

**How:** Invert $x^* = d - \nu + \text{greed}(x^*)$: pick $P$, read $x$ off the logistic, solve for $\nu$. By the envelope theorem $\nu$ is the slope of best attainable profit against the target. A coupon passes only $(1-P)$ of itself into the bid, so a 10-cent coupon adds 0.6 points of win probability at 1.6% but 5.6 points near 25%: the next point of hit ratio gets steeply dearer.

**The trap:** Paying the raw $\nu$ on every RFQ. It buys hit ratio fastest where other dealers shade hardest, in the toxic tiers (Niang). Pay it on clean tiers and withhold it elsewhere.

**If you got this wrong, read:** §18.7, then §18B.1 (the target is a price).

**Z.4-D.P22: Four of your ten "90%" intervals missed [Derive]**

**Answer:** Quite surprised. If the intervals were truly 90%, misses are Binomial(10, 0.1): mean 1, standard deviation 0.95, and $P(X \ge 4) = 1.3\%$, about one chance in 78 (exactly four: 1.1%). The evidence says your "90%" intervals behave like 60% intervals ($\mathbb{P}$, calibration).

**How:** $P(0) = 0.349$, $P(1) = 0.387$, $P(2) = 0.194$, $P(3) = 0.057$, which sum to 0.987. Taking 6 hits in 10 at face value, a 60% interval has half-width $0.84\sigma$ and a 90% interval $1.645\sigma$, so widen by roughly $1.645/0.84 \approx 2$. Alpert and Raiffa found people miss far more than one time in ten because narrowness feels like competence. Theo's page-count market of 130 to 480 looked ugly because it was honest.

**The trap:** Shrugging it off as small-sample noise: a 1-in-78 event is not noise. The opposite error is demanding zero misses; that happens 35% of the time even for a perfectly calibrated forecaster, and an interval that never misses is too wide to trade on. Two misses ($P(X \ge 2) = 26\%$) would be nothing.

**If you got this wrong, read:** §4D.4 (the paragraph on his first market), then §28.2, "How noisy is your hit rate?"

**Z.4-D.P23: The page-count game against an informed buyer, scored by markouts [Build]**

**Answer:** `play_page_game(policy, rounds, seed)` runs a document with lognormal page count (median 250, log standard deviation $\ln 1.5$) against a buyer who is informed with probability one half. An informed buyer lifts the offer if $N$ is above it and hits the bid if below; an uninformed one takes a random side whatever the price. The score is the sum of markouts in pages (offer minus $N$ on a lift).

**How:** Four policies: frozen at $250 \pm 40$; widen only; move the mid to the posterior median and keep $\pm 40$; zero-profit Glosten–Milgrom quotes from a grid posterior over $(N, \text{type})$. Tests first: frozen loses exactly offer minus $N$ on each lift; given an informed buyer, the posterior after lifts is the prior truncated at the highest lifted offer; zero-profit quotes average zero ($+2 \pm 9$ pages per six-round game). Cold-open replay ($N = 420$, three lifts, informed buyer): frozen $-390$ pages, widen only $-320$, move the mid $-213$, zero-profit $-201$.

**The trap:** Noise flow that ignores width crowns the widener ($+339$ pages a game against $+2$). Make uninformed flow fall as the market widens (Listing 18.5's `win_prob` will do), or markouts alone reward the dealer nobody trades with.

**If you got this wrong, read:** §4D.4, then §18.7 (the franchise term) and §3.3.

**Z.4-D.P24: Jump-to-default in the reservation price of a B3 bond [Derive]**

**Answer:** The jump adds about 0.05 points of fear for a long of three lots, against 0.019 from the diffusion: total fear is 3.7 times what Avellaneda–Stoikov alone charges, from an event with a 3.1% annual chance. Inputs are mine (illustrative): §4D.5's bond at 98 with recovery 40 ($J = 58$ points), $\lambda^{\mathbb{P}} = 3.1\%$ a year, one-week hold $\tau = 5/252$, $\sigma^2\tau = 1.27$, $\gamma = 0.005$, $q = +3$ lots of \$1mm.

**How:** The §18.6 line is $r^{\text{res}} \approx s + \mu\tau - \lambda^{\mathbb{P}}J\tau - q\gamma(\sigma^2 + \lambda^{\mathbb{P}}J^2)\tau$. Jump variance $\lambda^{\mathbb{P}}J^2 = 104$ against $\sigma^2 = 64$, so it outweighs the diffusion. With $\gamma qJ = 0.87$ the exact (18.7) factor $e^{\gamma qJ} = 2.39$ lifts the jump charge from 0.031 to 0.051. Against a $\mathbb{Q}$-fair composite the level term is only the credit view, $-(\lambda^{\mathbb{P}} - \lambda^{\mathbb{Q}})J\tau$ (0.036 if the mid carries no jump).

**The trap:** Leaving out the jump variance. A second trap is charging $\lambda J\tau$ on a mid that already carries it, or using CDS-implied $\lambda^{\mathbb{Q}}$ in the variance, which charges the market's fear twice. Third, the small-$\gamma$ line understates a three-lot long by 40%.

**If you got this wrong, read:** §18.6 (jump-to-default inside the HJB), then §4D.4.

**Z.4-D.P25: Kelly at carry 4.5%, PD 3.1%, recovery 40% [Derive]**

**Answer:** $f^* = 0.926$, i.e. 93% of NAV ($\mathbb{P}$ measure, one year, carry over financing, $L = 0.6$).

**How:** Maximize $g(f) = p\ln(1 + fc) + q\ln(1 - fL)$. Setting $g'(f) = 0$ and cross-multiplying gives $f^* = (pc - qL)/(cL)$:

$$
f^* = \frac{p}{L} - \frac{q}{c} = \frac{0.969}{0.6} - \frac{0.031}{0.045} = 1.615 - 0.689 = 0.926 .
$$

The bet has an edge as long as $q < c/(c+L) = 7.0\%$, and 0.926 sits inside the ruin boundary $1/L = 1.67$, which is why Kaz called it "technically prudent". The arithmetic is correct. The inputs come from three worlds: the carry from the market, the PD from an agency cohort table, the recovery from an agency average.

**The trap:** Treating 93% as a position. It is a ceiling on conviction, and the answer to "how much do you put in?" is the stop (P28 gives \$8.6mm on \$200mm, 4.3%). Ines: it is not aggressive, it is a resignation letter.

**If you got this wrong, read:** §28.4 (discrete Kelly for a bond), then §4D.5.

**Z.4-D.P26: Kelly's sensitivities to $L$ and to PD [Derive]**

**Answer:** $\partial f^*/\partial L = -p/L^2 = -2.69$ per unit of loss given default; $\partial f^*/\partial q = -(1/L + 1/c) = -23.9$ per unit of default probability, i.e. $-0.24$ of NAV per point of PD ($\mathbb{P}$, at carry 4.5%, PD 3.1%, $L = 0.6$). Exact moves: PD at 4.6% takes $f^*$ from 0.926 to 0.568; recovery 25 ($L = 0.75$) takes it to 0.603.

**How:** Differentiate $f^* = (1-q)/L - q/c$. It is linear in $q$, so 23.9 per unit is exact: 1.5 points of PD moves $f^*$ by 36 points of NAV. It is convex in $L$, so the exact fifteen-point recovery move is $-0.32$, where the slope would give $-0.40$. The two uncertainties are the same size, and only one of them, the recovery, shrinks by reading the intercreditor agreement.

**The trap:** Comparing the raw derivatives, 23.9 against 2.69, and concluding that PD matters nine times more. The derivatives have different units, and what counts is the size of your ignorance times the slope: a B3 PD is known to a point and a half, a recovery to fifteen points. Using the slope for the L move overstates it by a quarter.

**If you got this wrong, read:** §28.4 (the sensitivities after the discrete Kelly derivation), then §4D.5.

NOTE (for the editor): §28.4 pairs the slope $-2.69$ with "a recovery is known to perhaps $\pm 15$ points, which moves it by about 32". Multiplying 2.69 by 0.15 gives 40, not 32. The 32 is the exact move to $L = 0.75$ ($0.969/0.75 - 0.969/0.6 = -0.323$), which is smaller because $f^*$ is convex in $L$. The 36 for PD, by contrast, is slope times change. One clause in §28.4 saying the recovery figure is the exact change would stop a careful reader from checking it against the slope. §4D.5's "takes it to 60%" is exact and fine.

**Z.4-D.P27: The ruin boundary at $L = 0.75$ and at $L = 1$ [Derive]**

**Answer:** $f = 1/L$: 133% of NAV at $L = 0.75$ (recovery 25), 100% at $L = 1$ (recovery nothing), against 167% at the agency's $L = 0.6$. Kelly at $L = 0.6$, $0.75$ and $1$ is 0.926, 0.603 and 0.280.

**How:** A default takes wealth to $1 - fL$. At $f = 1/L$ that is zero, $\ln 0 = -\infty$, and no carry outweighs it. Kelly always sits inside the boundary, but it knows where the boundary is only if you gave it the right $L$, and the boundary is set by the worst recovery the documents allow, not the average one. If they permit a non-pro-rata uptier, a lender left outside recovers close to nothing, $L \to 1$, and the boundary drops to the unlevered position. At $L = 1$ the Kelly fraction is $0.969 - 0.689 = 0.28$ (§4D.13, Exercise 2). The intercreditor agreement is the ruin boundary, priced in leverage.

**The trap:** Reading "93% is inside the 167% boundary, so it is prudent" (Kaz's version), or setting the boundary from the average recovery. The first is true and useless; the second is exactly the document variable the pitch is supposed to catch.

**If you got this wrong, read:** §4D.5 (the paragraph on the trapdoor), then §28.4, "Which measure, and which loss".

**Z.4-D.P28: Largest long on \$200mm at a 7.5% line [Derive]**

**Answer:** \$15mm / 0.58 = \$25.9mm of face (market value \$25.3mm at a price of 98), the largest single long that does not breach the 7.5% line (\$15mm) on its own default. Under a 2.5% single-default line (\$5mm) it is \$8.6mm of face.

**How:** The stop turns a loss budget into a size before conviction gets a vote. A bond bought at 98 that recovers 40 loses $98 - 40 = 58$ points on default, so each dollar of face costs \$0.58. Size $= \text{budget} / \text{loss per dollar of face}$: $15/0.58 = 25.86$ and $5/0.58 = 8.62$. Note that the loss is price minus recovery, not par minus recovery. The line is the press-reported shape for one large platform (capital halved at 5%, closed at 7.5%), not a rule anyone discloses.

**The trap:** Using the 60-point loss from par (\$15mm / 0.60 = \$25.0mm), dividing by the 40-point recovery, or reporting Kelly's \$185mm. The 2.5% stop, \$8.6mm, is twenty times smaller than Kelly's \$185mm, and it arrives without being told the carry, the PD or the recovery distribution, because it does not care why the P&L moved.

**If you got this wrong, read:** §8D.5 (sizing to the stop), then §4D.5.

**Z.4-D.P29: Fractional Kelly with a 50% relative error in the edge [Derive]**

**Answer:** Bet $\theta^* = 1/(1 + s^2) = 1/1.25 = 0.80$ of full Kelly, i.e. 74% of NAV at the B3 inputs, keeping 80% of the full-Kelly growth ($\mathbb{P}$, relative standard error $s = 0.5$ in the edge).

**How:** Near its maximum any growth function is quadratic, $g(\theta f^*) = g^*(2\theta - \theta^2)$. If the edge carries a relative error $\varepsilon$ with standard deviation $s$, expected growth is $g^*(2\theta - \theta^2(1 + s^2))$, maximized at $\theta^* = 1/(1+s^2)$. At $\theta^*$ the growth is $g^*/(1 + s^2) = 0.8\,g^*$. Full Kelly keeps 0.75 and half Kelly 0.69, so the curve is flat nearby. At $s = 1$ the answer is one half, the chapter's "half Kelly", and full Kelly earns zero growth.

**The trap:** Saying "half Kelly, always", or $1/(1+s) = 0.67$. The shrinkage depends on the variance of the error, $s^2$, not on $s$. And do not stop at 74%: the stop in P28 allows 4.3% of capital, so the stop wins.

**If you got this wrong, read:** §28.4, "Fractional Kelly is full Kelly for people with standard errors", then §4D.5.

**Z.4-D.P30: Why a Q default intensity makes Kelly zero [Read]**

**Answer:** Under $\mathbb{Q}$ the credit triangle holds, $c \approx \lambda^{\mathbb{Q}}L$, so the edge $c - \lambda^{\mathbb{Q}}L$ is zero for every bond and $f^* = 1/L - \lambda/c = 0$.

**How:** Kelly sizes the edge, and the risk-neutral measure is the one in which nobody has an edge by construction: every price is a fair bet at the risk-free rate. A 300 bp spread with $L = 0.6$ gives $\lambda^{\mathbb{Q}} = 5\%$; at a 3% carry, $f^* = 1/0.6 - 0.05/0.03 = 0$. The edge Kelly can use is $c - \lambda^{\mathbb{P}}L$, the credit risk premium plus whatever your information adds. A Kelly fraction is a statement about $\mathbb{P}$ or it is a statement about nothing.

**The trap:** "Fixing" the zero by mixing a market spread with a historical default rate and an agency recovery. That is how you get 93%: three numbers from three different worlds, each defensible alone. The zero fails safe; the repaired number does not.

**If you got this wrong, read:** §28.4, "Which measure, and which loss", then §4D.2.

<!-- Z4D PART 1 COMPLETE -->
