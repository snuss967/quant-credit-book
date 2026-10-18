## Chapter 4: Inside the Systematic Credit Industry

Six exercises. Each one checks a number that a pitch book tends to leave out: breadth, cost, capacity, the clip, the capture ratio and the filing date. Write your answer down before you read ours.

**Z.04.1: Effective breadth**

**Answer:** With $m = 2{,}400/600 = 4$ bonds per issuer, $BR_{\text{eff}} = 2{,}400/(1 + 3 \times 0.6) = 2{,}400/2.8 \approx 857$ independent bets. To reach an IR of 0.5 at $TC = 0.5$ you need $IC \approx 0.034$.

**How:** The design effect is $1 + (m-1)\rho = 1 + 3 \times 0.6 = 2.8$, so the 2,400 bonds diversify like 857 independent bets. That is only 1.4 times the 600 issuers, a long way from 2,400. Then invert (4.1):

$$
IC = \frac{IR}{\sqrt{BR_{\text{eff}}}\;TC} = \frac{0.5}{\sqrt{857.1}\times 0.5} = \frac{1}{29.28} \approx 0.0342 .
$$

The skill bar is $\sqrt{2.8} = 1.67$ times what the bond count suggests. Now run Kaz's Thursday check. At a stress-window $\rho$ near one, breadth collapses to the 600 issuers and the bar rises to $IC \approx 0.041$. Listing 4.1's `effective_breadth(2400, 600, 0.6)` returns the 857.

**The trap:** The usual mistake is to put the bond count straight into the law, which gives $IC = 0.5/(0.5\sqrt{2{,}400}) \approx 0.020$. That understates the skill you need by about 40%, and you would then lever the book to diversification you do not have. A second slip is to write $N/(1 + m\rho) = 706$. The "minus one" is there because a bond's correlation with itself is already counted in the $N$ variances; only its $m-1$ siblings add cross terms.

**If you got this wrong, read:** §4.3, "Scoring the breadth column: the fundamental law with issuer clustering," and its Full Derivation.

**Z.04.2: Kaz's Sharpe of 3.1**

**Answer:** An average cost of 32.5bp per dollar traded takes the IR to 0.5, and 38.75bp takes it to zero. A realistic HY half-spread is about 25bp to cross a liquid line, which is Ines's first number and an eighth to a quarter of a point in Chapter 4-D. The cheap-decile bonds a value signal buys cost more. At 25bp the IR is already down to 1.1, before size and fade. At Ines's all-in 50bp (25 + 10 + 15) it is $-0.9$. The sentence for Ines: "The 3.1 assumed free trading on sixteen dollars of turnover per dollar of book; a realistic half-spread takes it to about 1 and your all-in cost takes it below zero, so I'm putting the cost in the backtest and cutting the turnover before it goes anywhere near an allocator."

**How:** Costs do not change tracking error, so the IR is net alpha divided by 2%, and an IR of 0.5 means 1.0% of net alpha. One-way turnover of 8 is 8 sales plus 8 purchases, so the drag is $2T\bar c = 16\,\bar c$:

$$
6.2\% - 16\,\bar c = 0.5 \times 2\% \;\Rightarrow\; \bar c = \frac{5.2\%}{16} = 32.5\text{bp}, \qquad 6.2\% - 16\,\bar c = 0 \;\Rightarrow\; \bar c = \frac{6.2\%}{16} = 38.75\text{bp}.
$$

Each basis point of cost removes 16bp of alpha, or 0.08 of IR. The zero point is (4.6) read backwards: at $\bar c = 38.75$bp, $T_{\max} = 6.2\%/(2\bar c) = 8$. At 50bp, $T_{\max}$ is only 6.2 turns.

**The trap:** The usual mistake is dropping the 2 and dividing by 8 rather than 16, which gives 65bp and 77.5bp. Those look comfortably above a 25bp half-spread, and they would let Kaz tell Ines that costs don't matter. The subtler trap is to compare 32.5bp with the half-spread alone and call it safe. The half-spread is only the first of Man's three cost terms, and costs rise in exactly the months when a value or momentum book trades most.

**If you got this wrong, read:** §4.7, "Break-even turnover" (4.6), and Ines's "Twenty-five to cross" a few paragraphs earlier. Chapter 4-D replays this same exercise as an interview question.

**Z.04.3: The fee-adjusted hot tub**

**Answer:** The client's net alpha after fees is zero at

$$
A_f = \frac{\mathcal{L}\,(g-f)^2}{8\,T^3\eta^2} = \tfrac94 A^{*}\Big(1-\frac{f}{g}\Big)^2, \qquad 0 < f < g,
$$

and no positive size works if $f \ge g$. For any $f > 0$ the bracket is below one, so $A_f < \tfrac94 A^{*}$. Take the §4.8 worked example ($g = 120$bp, $A^{*} \approx \$1.85$bn). A 20bp fee moves the zero from \$4.17bn to \$2.89bn. A 50bp fee moves it to \$1.42bn, which is below $A^{*}$ itself, because $A_f > A^{*}$ only when $f < g/3 = 40$bp. A manager paid only on assets earns $fA$, which rises without limit. With sticky assets it therefore wants to be as large as it can raise, even past $A_f$, where clients lose money after fees. Performance-chasing flows change this. Clients leave once net alpha after fees turns negative, so $A_f$ becomes a ceiling. A manager that also sets its fee then maximizes $f A_f$, and the maximum is at $f = g/3$, which puts the book exactly at $A^{*}$ and hands the manager the whole $\Pi(A^{*}) = gA^{*}/3 \approx \$7.4$mm a year while the client keeps nothing.

**How:** The fee is a transfer from client to manager. It does not cost the strategy anything, so the hill $\Pi(A)$ stays where it was; only the split of the dollars changes. Set the client's net to zero:

$$
g - 2T\eta\sqrt{2TA/\mathcal{L}} - f = 0 \;\Rightarrow\; \sqrt{A_f} = \frac{g-f}{2T\eta\sqrt{2T/\mathcal{L}}} \;\Rightarrow\; A_f = \frac{\mathcal{L}(g-f)^2}{8T^3\eta^2}.
$$

Dividing by $A^{*} = \mathcal{L}g^2/(18T^3\eta^2)$ gives $A_f/A^{*} = \tfrac{18}{8}(1-f/g)^2$. With $f = 0$ you recover the chapter's $\tfrac94$. When flows drive the client's surplus to zero, revenue is $R(f) = \tfrac94 A^{*} f(1-f/g)^2$. Its derivative is proportional to $(1-f/g)(1-3f/g)$, which is zero at $f = g/3$, and there $A_f = \tfrac94 \cdot \tfrac49 A^{*} = A^{*}$. This is Berk and Green's point in miniature: when flows are competitive, the manager captures the rent and the client gets the market return.

**The trap:** The common wrong answer is that the asset-paid manager chooses $A^{*}$. That size maximizes *total* dollar alpha, so it is the choice of a manager paid a share of alpha. A pure asset fee pays on $A$, and the only thing that stops growth is the client walking out. Two algebra slips are also common. One is charging the fee per dollar traded, so that it gets multiplied by $2T$. The other is treating the client's net at $A^{*}$, $g/3 - f$, as if it were the zero point.

**If you got this wrong, read:** §4.8, Ines's "Who gets paid on what?" and the Full Derivation of the capacity maximum. Listing 4.2's `net_alpha_curve` will draw the hill if you subtract $f$.

**Z.04.4: Split the clip**

**Answer:** Branch on the *signs* of EBITDA and net debt before you form any ratio. With $\ell_i = \text{ND}_i/\text{EBITDA}_i$ and a sourced floor $\ell_{\min}$ (say 0.5x, illustrative, not 0.1):

$$
\text{score}_i =
\begin{cases}
\text{OAS}_i/\ell_i & \text{EBITDA}_i > 0,\ \ell_i \ge \ell_{\min} \quad\text{(ordinary)}\\
\text{OAS}_i/\ell_{\min},\ \text{flag low\_lev} & \text{EBITDA}_i > 0,\ 0 < \ell_i < \ell_{\min} \quad\text{(low positive leverage)}\\
\text{peer-relative spread } \tilde V_i \text{ only, flag net\_cash} & \text{EBITDA}_i > 0,\ \text{ND}_i \le 0 \quad\text{(net cash)}\\
\text{no value score} \rightarrow \text{distressed model} & \text{EBITDA}_i \le 0 \quad\text{(negative EBITDA)}
\end{cases}
$$

Missing or stale inputs get no score in any branch. The negative-EBITDA branch passes the distressed model what a recovery analysis needs, not what a ratio needs: the CUSIP mapped to issuer and class (lien, guarantors, structural position, from the security master); price rather than OAS, with its knowledge time; debt by class and maturity; liquidity (cash plus undrawn revolver) and cash burn; covenant headroom; the document flags for LMT capacity; and the knowledge times of the fundamentals. The distressed model returns price against expected recovery by class. The bond leaves the value ranking entirely. One assert that would have caught the 15,000: `assert not np.any((ebitda <= 0) & np.isfinite(value_score))`, meaning no issuer with non-positive EBITDA comes out of the value screen with a score. The distributor's EBITDA of $-\$20$mm trips it.

**How:** The ratio $\text{ND}/\text{EBITDA}$ is negative in two opposite worlds. A net-cash issuer has $\text{ND} < 0$ and $\text{EBITDA} > 0$, and is very strong. A company like the distributor has $\text{ND} > 0$ and $\text{EBITDA} < 0$, and is in distress. Separately, the ratio explodes as EBITDA approaches zero from above. A single `max(., 0.1)` sends all three cases to the same number. That is how the BB scores $250/4 = 62.5$, the net-cash IG name $900$, and the CCC $1{,}500/0.1 = 15{,}000$: 240 times the BB and 17 times the next-best name. The cure is to test the components before you divide, so the branches are decided by sign and size rather than by the clipped ratio. Within each branch, neutralize against peers as usual.

**The trap:** One common fix is to raise the clip, to 0.5 say. The CCC then scores 3,000 and still tops the list. Another is to take the absolute value of leverage: $|-30| = 30$ gives the CCC a score of 50, which looks like an unremarkable rich BB and quietly leaves a restructuring candidate in the value ranking. The third mistake is to route every negative ratio to the distressed model, which sends the net-cash IG issuer to a restructuring desk.

**If you got this wrong, read:** §4.4, "Value is the gap between Q and P," from the edge cases through Theo's building-products distributor. Chapter 13 covers what the distressed model has to see about priming.

**Z.04.5: Capture-ratio forensics**

**Answer:** $a \approx 15.4$bp a month (about 1.85% a year) and $\beta \approx 0.93$. Read through the linear model, this is not mainly beta. Of the 15 points of down-capture "defense," about 7 come from the slope ($1 - 0.93$) and about 8 from the alpha cushion ($a/\bar d = 0.081$). With BlackRock's mix of 168 up and 72 down months, $\mathbb{E}[r_m] = 0.34\%$, and the manager beats the index by about 13bp a month (1.6% a year), against roughly $-1$bp for BlackRock's average manager. That is top-decile HY, and that should make you suspicious. A capture pair with $UC > 1 > DC$ is just what a backtest with regime bins defined after the fact produces. It also fits asymmetric beta with no alpha at all ($\beta_{\text{up}} = 1.05$, $\beta_{\text{down}} = 0.85$). Two numbers cannot tell these stories apart. To tell them apart you need:

- the monthly manager and index returns, with the index named and the bins set by its sign;
- the counts of up and down months;
- a gross/net and live/simulated label;
- a regression with separate up and down slopes;
- the down months one by one, to see whether one month carries the result;
- holdings, to look for cash, IG, CDX protection or duration that rallies in risk-off.

**How:** Subtract the two capture equations of (4.7), using $\bar d > 0$:

$$
UC - DC = a\Big(\frac{1}{\bar u} + \frac{1}{\bar d}\Big) \;\Rightarrow\; a = \frac{0.20}{1/0.013 + 1/0.019} = \frac{0.20}{129.55} = 0.00154,
$$

then $\beta = UC - a/\bar u = 1.05 - 0.119 = 0.931$. Check: $DC = 0.931 - 0.00154/0.019 = 0.850$. Once you allow $\beta_{\text{up}} \ne \beta_{\text{down}}$, (4.7) has three unknowns and two equations, so it cannot separate alpha from convexity. A long HY book is short its issuers' default puts and should be *concave*, which makes the 20-point convex gap the claim that most needs explaining.

**The trap:** The common mistake is to read 85% downside capture as a beta of 0.85, which is the $a = 0$ reading, and call it a smaller long. That is BlackRock's average manager, not this one. A sign slip catches people too. Plugging $\bar d = -1.9\%$ into the formula gives $a = 0.20/(76.9 - 52.6) \approx 82$bp a month and $\beta \approx 0.42$, which no HY manager has ever had.

**If you got this wrong, read:** §4.9, "A line through the months," (4.7) and its Full Derivation, then "Seventy-two down months, and the one that matters."

**Z.04.6: The 10-Q join**

**Answer:** A non-accelerated filer has 45 days after quarter end to file its 10-Q and 90 days after year end to file its 10-K, and such filers usually file close to the deadline. A join on the fiscal quarter end therefore gives the backtest about 45 days of foresight in three quarters and about 90 in the fourth, roughly 56 days on average. If every filing uses the Form 12b-25 extension (5 more days for a 10-Q, 15 for a 10-K), that rises to about 64. At monthly rebalancing, 9 of every 12 month-ends trade on a leverage number nobody outside the company had. The join breaks the first of the Friday spec lines in §4.5: every field carries a knowledge time, and every join is an as-of join on it, so $s_{i,t} = f(\{x : t^{\text{kn}}(x) \le t - \ell\})$. Joining on event time is a lead error. The bias is largest for deteriorating credits for three reasons:

1. They file latest, through NT filings, going-concern work with the auditor and covenant waivers negotiated before the filing, and sometimes they never file at all.
2. Their leverage moves most from one quarter to the next, so the leaked number is the news.
3. A spread-over-leverage screen ranks them cheap in real time because the spread has already widened while the denominator is stale.

So the honest backtest buys the value trap and takes the loss when the 10-Q lands. The leaky one already sees the higher leverage, cuts the score and steps out of the way.

**How:** Take the quarter ending 30 June, with the 10-Q accepted by EDGAR around 14 August. The leaky join uses Q2 leverage at the 30 June and 31 July rebalances, and the honest join first uses it at 31 August, so two of the three month-ends leak. For the 10-K quarter, the 31 December, 31 January and 28 February rebalances all leak. That is $3 \times 2 + 3 = 9$ of 12. Put a number on it *(illustrative)*: a bond at 600bp with last-filed leverage of 4.0x scores 150 and sits in the cheap decile. If the unfiled Q2 leverage is 6.0x, the leaky backtest scores it 100 six weeks before anyone could have, and the bond is out of the long leg before the bad 10-Q lands. The error is correlated with the next month's return, so it does not average out. It inflates the value premium, and it does so in the long leg's worst names.

**The trap:** "Forty days" is the deadline for accelerated filers, not non-accelerated ones. A more expensive mistake is to "fix" the join with a fixed 90-day lag. That is too slow for early filers, and it still leaks for a 10-K filed under an NT extension (90 + 15 = 105 days). The honest fix is each filing's own EDGAR acceptance timestamp, or the earnings release where that release actually contains the field, plus a processing lag $\ell$.

**If you got this wrong, read:** §4.5, the "sealed envelope" box and the knowledge-time formula, then Thursday of "Rerunning Kaz's backtest on the clean panel," where Theo finds this exact join.

<!-- STATUS: COMPLETE -->
