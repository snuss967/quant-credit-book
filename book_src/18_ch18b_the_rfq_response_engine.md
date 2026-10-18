# Chapter 18-B: The RFQ Response Engine

> **Prerequisites.** Chapter 18, in particular §18.4–§18.7 (the HJB, the win curve, the multiplier $\nu$ and equation 18.9) and §18.6.3 (Altice France, where Pair Book entry PB-14 opened); §2.3.2 (order statistics and the effective number of dealers); §3.2–§3.3 (Glosten–Milgrom for RFQs, markouts, survivorship). Every new piece of mathematics gets a Math, Gently box where it first appears. The chapter ships `rfq_engine.py` through Appendix F.

*What is invented, once for the whole chapter.* The desk, its traders, its RFQ log, its client tiers, its weekly tiles, its risk committee, its platform review, Dealer B in §18B.6 and every number marked illustrative are fictional composites. So are Owen Achterberg's capital-structure pod (Chapter 4-C), Dov Adler's pod at Vantress Capital Management (Chapter 1-B), Wen Zhao and Marcus Oyelaran (first met in §2.9.4). Altice France, its instruments and the dates of March 2024 are real and sourced in §18.6.3. The papers, platform statistics and quoted public remarks are real and cited. Every calibrated number taken from a paper is that paper's authors' own, most of them computed on synthetic data, and the text says so where they appear. No real dealer's engine is described anywhere in this chapter; HSBC and BBVA appear only as the affiliations of authors of published papers.

## 18B.0 Cold Open: The Green Tile That Was Lying

Monday, 7:40 a.m. The RFQ loop has a rota, like the coffee machine and the fire drill, and this week the rota said Theo. It is the third intraday loop of §3B.1, the one that watches hit ratios and cover gaps, and on a Monday morning it means reading last week's tiles. Each tile carries a number, a band and a colour, and the colour is the only part most people read.

The tile that mattered was the asset manager's, the client whose panel-review e-mail in §18.7 had given the desk its hit-ratio target. Hit ratio 17%, against a target of 15% and a band of three points: green. Average cover gap on wins, the distance between the desk's winning price and the second-best price, 8 cents, against 6 the week before and a band of three cents: green. *(Every number in this scene is illustrative.)* The rota sheet said a green tile gets initials. Theo initialled it.

Ines stopped behind his chair with a coffee, read both tiles, and did not move on.

"You've been paying them to trade with you for a week," she said.

"Both green."

"Each one's green. Read them together." She put the cup down on the only part of his desk without paper. "Hit ratio up: you won more. Cover gap wider: when you won, the next-best price was further from yours than it used to be. You could have shown a worse price and still won. So the extra wins came from giving the client more than the table required. That's a subsidy with a receipt."

Theo had read the pattern in §3B.2 and never watched it happen. What he noticed now was that nobody had done anything wrong. The target had been met. The engine had done exactly what it was told.

"Who changed what?" he asked.

"Nobody, which is the interesting part. Kaz, what's $\nu$ on that tier?"

Kaz, two seats down and still in a coat, looked. "Seven cents. I refitted it on the four weeks to the end of September, so the target would hold through month-end."

"And what was the tape doing in September?"

"Choppy. Realized vol about twice last week's, and we were carrying month-end inventory." A pause, which was Kaz rerunning something. "Last week was quiet, and we were flat."

"So you priced the target in a storm and paid the storm price in the sunshine," Ines said. "Give me the tier, not the average."

The tier view took Theo four minutes. The extra wins sat on Tuesday to Thursday, in calm hours with a flat book, exactly when the desk's ordinary quote already won about as often as the target wanted. Seven cents had bought hit ratio where it was cheap, so it bought a lot, and on each trade it paid two cents more than the cover required. Across about two hundred wins of a couple of million each, that came to about \$80,000: a rounding error for the desk, and a very pleasant week for the client.

"So the target isn't a score," Theo said slowly. "It's a price. Somebody decides what we pay per point of hit ratio, and the tile only shows whether we bought the points. It doesn't show what we paid for them."

"Or who got the money," Ines said. "A subsidy always lands on somebody."

Kaz had already stood up and was walking toward the whiteboard, which on this desk is how a morning changes plans.

By the end of this chapter you will be able to read a hit-ratio target as a shadow price that moves with volatility and inventory; split a quote into Niang's five terms and name the client tier that receives each; estimate the rivals' quotes from the whole RFQ log rather than the wins; count how many dealers are really in the room; build a stress switch that does not fire every afternoon at 3:50; take apart what two dealers charged Owen's pod for its two Altice France tickets on 20 March 2024; and recognise when a platform's ranking gives the hit ratio a memory. On the way you will see why a fill model with an AUC of 0.97 is a bug report.

## 18B.1 The Target Is a Price

*Builds on:* §18.4–§18.7 (the HJB, the win curve, the multiplier $\nu$, equation 18.9). *Used in:* §18B.2 (the subsidy term), §18B.7 (when the price buys future access), §19.9 (the participation rule), §28.9 (the market-maker panel).

Kaz's whiteboard still had equation 18.9 on it in green from the month before, with the $+\nu$ circled. Kaz drew a box around the whole bid and wrote *one RFQ* above it in red. Then they drew forty more boxes in a row, and a long bracket underneath: *15% of these, please.*

"Every quote is its own small optimisation," Kaz said, "except that the target ties them together. So in principle every quote depends on every other, past and future, and the problem is a monster with forty heads. In practice there's a trick."

The trick is one line of algebra, and it is why the target behaves like a price. Barzykin and Ciceri (2026), "Bond Market Making with a Hit-Ratio Target" (arXiv 2604.20406), penalise the gap between the desk's expected hit ratio $r$ and its target $r^\star$ quadratically, with strength $\kappa$, and rewrite the penalty as the lowest of a family of straight lines:

$$
-\frac{\kappa}{2}\,\big(r - r^\star\big)^2 \;=\; \inf_{\xi}\Big[\,\xi\,\big(r - r^\star\big) + \frac{\xi^2}{2\kappa}\Big].
$$

Minimising the bracket over $\xi$ gives $\xi = -\kappa(r - r^\star)$, and substituting back returns the left-hand side, so nothing has been lost. Something has been gained. For a fixed $\xi$ the objective is *linear* in $r$, and $r$ is an average of fills, so the forty-headed problem falls apart into forty one-headed ones. Each RFQ earns, if won, a coupon equal to $\xi$ times its weight in the hit ratio, and the single number $\xi$ is all that ties the RFQs together. Kaz's $\nu$ in §18.7 is this coupon rescaled to one RFQ, which the paper writes $\tilde\xi$: adding $+\nu$ to the bid is pretending the reservation price is $\nu$ better than it is, so the reservation term $\Delta u$ becomes $p = \Delta u - \tilde\xi$ for targeted tiers and stays $p = \Delta u$ for everyone else.

"So the multiplier is what one more point of hit ratio costs us," Theo said. "The way a covenant has a shadow price."

"Say more," said Kaz, who had never seen a covenant.

> **Math, Gently.** *A shadow price that moves with the book.* Every constraint has a shadow price: what it costs to tighten it by one unit. Theo's version is the minimum-liquidity covenant. One more million of required cash costs a company almost nothing in a quarter when cash is piling up, and costs it the whole negotiation when cash is short. The constraint did not change; the price of obeying it did. What moves the price of a hit-ratio target is the shape of the desk's own risk. Picture the desk's value against its inventory as an upturned bowl, $-\tfrac12 A q^2$, falling faster the more it holds. $A$ is the bowl's steepness, in points per million of inventory. It steepens with volatility and risk aversion and flattens with client flow to trade out with; in the one-bond case $A = \sqrt{\text{risk aversion} \times \text{variance} \,/\, \text{liquidity}}$, so doubling the volatility doubles $A$. Even at zero inventory a trade of size $z$ costs about $A z/2$ per unit, because the trade itself moves the desk halfway down the bowl on average. A tiny number, illustrative: in a calm week $A = 0.05$ points per million and the average RFQ is \$1mm, so each side carries 2.5 cents of extra cost; with twice the volatility, 5 cents. On §18.7's win curve ($\beta_1 = 4$) near a 15% win rate, each cent of cost lowers the win probability by about half a point, so the choppy week shaves about 1.3 points off the uncouponed hit ratio, and since the coupon offsets cost one for one, buying them back takes about 2.5 cents more. Five cents becomes seven and a half: the cold open's seven cents, fitted in a storm. The full version is the derivation below.

So the multiplier is a property of the client *and the desk's state*. Barzykin and Ciceri also find, on their synthetic book, that a multiplier held constant fails when inventory is large, because the one that hits the target is roughly quadratic in inventory. Inventory skews the quote, tightening one side and widening the other, and whether the two sides together win more depends on where the tier sits on its S-shaped win curve. At low win probabilities, the convex part of the S, the tightened side gains more than the widened side loses, so a heavy book raises the hit ratio and the target gets cheaper; at high win probabilities the effect reverses (our reading; the paper shows the shape, not this mechanism). A constant is wrong in both directions on different days, so the desk re-solves the multiplier when the bowl changes shape, which on a credit desk means every morning, with the risk pack.

One finding is cheerful. A tier the desk does not target, which the paper calls background flow, cuts the inventory skew and raises the hit ratio achieved in the targeted tier; so does a correlated background bond. Two-sided flow nobody pays a coupon for drains the inventory that makes the bowl steep. On Ines's desk it is an index fund's rebalancing desk, which sends large, dull, two-sided inquiries around month-end and has no idea that it is the desk's best hedge.

The paper's numbers are synthetic: a size ladder of \$1mm, \$5mm and \$20mm, 500, 200 and 50 RFQs a day, sigmoid fills, $r^\star = 0.1$ and a one-day horizon, with no RFQ data and no public code. The version that keeps the exact quote map and solves the dual exactly is, in the authors' phrase, "impressively accurate" against the exact solution on that book, while the cruder analytical closures drift away at large inventory; nobody has replicated any of it on a real log. Kaz wrote *SYNTHETIC* next to every number on the whiteboard, which is how Kaz labels things they intend to rely on anyway.

#### The Full Derivation

*Notation.* The paper's arrival rate is written here $\bar\Lambda_k$ for tier $k$, because this book reserves $\lambda$ for default intensity. Its curvature matrix is written in bold, $\mathbf{A}$, to keep it apart from the arrival parameter $A$ of §18.4, and its risk-aversion coefficient is written $\phi_\Sigma$, because $\phi$ already means something else in §2.3.2 (§18B.4 meets all three $\phi$'s in one room).

Let tier $k$ send RFQs of size $z_k$ at rate $\bar\Lambda_k$, filled with probability $f_k(\delta)$ when the desk quotes $\delta$ away from the reference price. The per-unit Hamiltonian is the best expected profit rate when holding the position costs $p$ per unit:

$$
H_k(p) = \sup_{\delta}\; \bar\Lambda_k\, f_k(\delta)\,(\delta - p).
$$

By the envelope theorem $H_k'(p) = -\bar\Lambda_k f_k(\delta^\star(p))$, minus the expected fill rate, so the optimal quote is the one whose fill probability equals $-H_k'(p)/\bar\Lambda_k$:

$$
\delta^\star = f_k^{-1}\!\big(-H_k'(p)/\bar\Lambda_k\big), \qquad p = \Delta u - \tilde\xi \ \text{(targeted tiers)}, \quad p = \Delta u \ \text{(all others)},
$$

where $\Delta u$ is the per-unit change in the value function when the trade lands. With the quadratic ansatz of Bergault, Evangelista, Guéant and Vieira (2021), $u(t,q) \approx -\tfrac12 q^{\top}\mathbf{A}(t)\,q + \dots$, the inventory curvature solves a matrix Riccati equation,

$$
\mathbf{A}' = \mathbf{A}\,\mathbf{K}\,\mathbf{A} - \phi_\Sigma\,\Sigma, \qquad \mathbf{K} = \operatorname{diag}\Big(\textstyle\sum z_k\, H_k''(0)\Big),
$$

with the sum running over tiers, sizes and both sides, $\Sigma$ the covariance of the bonds' price moves, and $\mathbf{K}$ the liquidity the flow provides. Every tier loads the curvature; only targeted tiers receive a coupon. For one bond the stationary solution is $A = \sqrt{\phi_\Sigma\,\sigma^2/K}$, the square root in the box. Linearising the quote around $p = 0$ gives the three terms:

$$
\delta \;\approx\; \underbrace{\delta_0}_{\text{riskless spread}} \;+\; \underbrace{c^{-1} e^{\top}\mathbf{A}\big(\pm q + \tfrac{z}{2}\big)}_{\text{inventory correction}} \;-\; \underbrace{c^{-1}\tilde\xi}_{\text{hit-ratio correction}}, \qquad c = 2 - \frac{f f''}{(f')^2}.
$$

For the logistic win curve of §18.7 a line of algebra gives $c^{-1} = 1 - f$: near a 15% win rate, 85% of the coupon passes into the quote. The dual itself has a closed form, $\tilde\xi = \tilde\kappa\, y$, with

$$
y = r^\star + \frac{1}{\bar Z}\sum z\,H'(0) + \frac{1}{2\bar Z}\sum z^2 A_{mm}\,H''(0),
$$

summed over the targeted tier's sizes and sides, with $\bar Z$ that tier's size-weighted RFQ flow (the paper's $W$, renamed because $W_t$ is a Brownian motion here). Since $-H'(0)$ is the fill rate at zero cost, the first two terms are the target minus the hit ratio achieved with no coupon and no inventory risk; the third grows with the curvature $A_{mm}$, the box's arithmetic in matrix form. Three terms is the whole of Barzykin and Ciceri's decomposition. The five-term quote is not theirs. It belongs to the next section's paper.

One limitation decides how the desk uses the result. The paper penalises the *expected* hit ratio, a smooth surrogate that keeps the problem Markovian; the literal count that sales reads at quarter-end would need cumulative counts as state variables, and the paper sets that aside. So the engine targets one number and the tile reports another, and a week of bad luck is explained to sales as "expected versus realized," a phrase sales has heard before.

## 18B.2 Three Terms to Five

*Builds on:* §3.3 (markouts, the hand history, IDO markouts), §3.3.5 (survivorship), §18.7 (suspicion $a_c$). *Used in:* §18B.6 (the two Altice quotes), §19.8 (the basket's adverse-selection charge), §27.7 (CUSUM on markouts, by tier).

Thursday is markout review, the hand history of §3.3: every fill of the week, marked against the composite five minutes, an hour and a day later, sorted by client tier. Kaz had brought a proposal, already running since Wednesday afternoon: a toxicity charge per tier, taken straight from the hand history, the bigger the average markout loss, the bigger the charge. By Thursday at 10:15 the carry-and-relative-value tier, an insurer's total-return sleeve and two relative-value funds, had a hit ratio of about 1% *(illustrative)*. At 10:50 the insurer's salesperson called to ask, with great courtesy, whether the desk had stopped making markets in investment grade.

"Their markouts are terrible," Kaz said. "Every time they buy, the bond goes up."

"Every time they buy, they buy a fat coupon on a steep part of the curve," Theo said, the decomposition already up. "A third of that markout is carry and rolldown, which we'd see on any bond with that coupon and maturity. Another chunk is the market: IG rallied two days this week. A bit is the issuer's own curve. What's left is about zero." He scrolled. "The event-driven tier is the opposite. The market sold off on the days it sold to us, which flattered its gross markout. Strip the market out and its residual is the worst on the page."

"IDO or it didn't happen," Ines said, "applied to the client." In Chapter 8 the motto stops the desk calling beta alpha; here it stops the desk calling carry information.

Niang (2026), "Quality-Adjusted Hit-Ratio Targeting in Corporate Bond Market Making" (arXiv 2605.30643), builds an engine around this move. Each tier's markouts are split into factor, carry and rolldown, issuer relative value, index and ETF flow, and the residual. Only the residual, $\chi_i$ for tier $i$, counts as toxicity, and a fill from tier $i$ counts toward the target with weight $w_i = e^{-\eta\,\chi_i}$, so winning a toxic tier earns almost no credit. (Niang writes the sharpness as $\gamma$; it is $\eta$ here because $\gamma$ is inventory risk aversion.) In §18B.1's Hamiltonian the change is one shift of the argument:

$$
z_i\,H_i\big(p_i + \chi_i - w_i\,\xi\big),
$$

toxicity added to the tier's cost and the coupon scaled by its quality. The dual equation has a unique root, and for §18.7's logistic curve the quote has a closed form,

$$
x^\star = p + \frac{1 + W_0\!\big(e^{\,\beta_0 - \beta_1 p - 1}\big)}{\beta_1},
$$

with $x$ the distance from the composite, $p$ the tier's total effective cost, and $W_0$ a function most people meet once and forget.

> **Math, Gently.** *The Lambert W function, or how to solve the equation §18.7 iterated.* Some equations hide the unknown both outside and inside an exponential, like $w\,e^{w} = 3$. No logarithm gets $w$ out, so the answer has a name: $W(3)$, about 1.05, the number whose product with its own exponential is 3. It turns up here because §18.7's first-order condition, $x - p = 1/\big(\beta_1(1 - P(x))\big)$, has $x$ on the left and inside the logistic's exponential on the right. Kaz solved it by iterating; Lambert W solves it in one step. A tiny number: with $\beta_0 = 0$, $\beta_1 = 4$ and a total cost of $p = 0.5$ points, $e^{0 - 2 - 1} = e^{-3} \approx 0.050$, $W_0(0.050) \approx 0.048$, and the quote sits $0.5 + 1.048/4 \approx 0.76$ points from the composite, where it wins about 4.5% of the time. The first-order condition agrees: $1/\big(4 \times (1 - 0.045)\big) \approx 0.26$, and $0.76 - 0.5 = 0.26$. The full version is in Niang (2026) and in `quote_from_p` in §18B.9.

The result is the five-term decomposition. It is Niang's, not Barzykin and Ciceri's, whose quote has three terms:

$$
\text{quote} = \text{riskless spread} + \text{inventory skew} - \text{credit-alpha skew} + \text{residual-toxicity charge} - \text{quality hit-ratio subsidy}.
$$

The first two terms are §18B.1's; the credit-alpha skew is the desk's own view, the $\lambda^{\mathbb{P}}$ against $\lambda^{\mathbb{Q}}$ line of equation 18.9. The last two each have an address. The toxicity charge goes to tiers with bad residuals. The subsidy goes to tiers whose fills count toward the target, weighted by $e^{-\eta\chi}$, so almost none of it reaches a toxic tier. A subsidy always lands on somebody, and the five-term quote decides on whom.

Niang's numbers come with their label: 20 synthetic euro investment-grade bonds, 300 simulated paths for the frontier and 100 over five trading days for the 8% benchmark run. At an 8% target, raw hit-ratio targeting earns $-14.32$ bp·MM a day and residual-quality targeting $+5.25$. The raw engine wins 7.47% of the toxic flow and the residual engine 0.87%, while both win about the same share of the carry-and-RV flow (7.29% against 7.05%). Kaz's Wednesday mistake is in the paper too, as "naive gross toxicity": charging gross markouts over-widens the carry-and-RV tier until its hit ratio is 1.08%. The paper's own table has that policy earning more per day than the residual engine (+8.22 against +5.25), by hardly serving the tier at all, which is exactly what the insurer's salesperson had noticed. Kaz read that line twice and said nothing, which is the most Kaz has ever said.

The synthetic markouts were generated from the same five factors the engine later uses to decompose them, so the decomposition is perfect by construction. A real factor model is wrong a little every day, and some of what it calls residual is a factor it failed to name (§7.4, where a leg's rating bucket posed as the pair's alpha). The paper's limitations section concedes the point, and the only outside critique on record, an AI-written referee report (pith.science, 28 June 2026), raises the same objection; its "authors' rebuttal" is simulated, so no fix is on record. So Ines ran it next to something simpler: Cartea and Sánchez-Betancourt (2025), "A Simple Strategy to Deal with Toxic Flow" (arXiv 2503.18005), a closed-form dealing strategy against informed and uninformed clients that needs no per-client calibration. "Beat the simple one first," she told Kaz, "or the five factors are decoration."

Then Theo found the problem no decomposition fixes. The hand history contains only the hands the desk won, and those are not a random sample of the hands it was dealt. Marín Martínez, Ardanza-Trevijano and Sabio (2026), "Causal interventions in bond multi-dealer-to-client platforms" (*PLOS ONE* 21(1): e0341369), draw the RFQ as a causal graph: winning is a collider on the path from the desk's quote $\delta$, through the client's reservation spread $\delta_{\text{res}}$, which the client's information asymmetry $IA$ pushes wider, to the price drift $\mu$ and the desk's revenue $R$,

$$
\delta \;\to\; \text{win} \;\leftarrow\; \delta_{\text{res}} \;\leftarrow\; IA \;\to\; \mu \;\to\; R .
$$

> **Math, Gently.** *Conditioning on a win is a collider.* A collider is an event with two independent causes; look only at cases where it happened and the causes become linked. Food quality and location are unrelated across all restaurants, but among those that survived five years, the ones in bad locations must have great food. Winning an RFQ has two causes: the desk quoted aggressively, or the client was willing to trade at almost any price, which a client with information is. So among the desk's *wins*, those won with a wide quote were mostly won because the client's reservation was wide, and those are disproportionately informed, with bad markouts. A regression of markout on quote, run on wins only, concludes that quoting wider makes markouts worse, which is backwards. A tiny number, illustrative: if one RFQ in ten is informed and informed clients will accept a price half a point wider, a desk that quotes either tight or half a point wide wins its wide-quote trades almost entirely from the informed tenth, and their markouts look far worse than its tight-quote wins. The fix is to model the information asymmetry rather than condition it away. The full version is in Marín Martínez et al. (2026).

Their data are BBVA's European government-bond RFQs, 102,437 inquiries and 5,738 hits. The hit probability given the quote is identified after adjusting for volatility, the RFQ, the bond and the client; revenue given a hit is not identified from observables at all. Their hit models score an area under the ROC curve of 0.742 for a generative model in the Fermanian–Guéant–Pu style, 0.743 for LightGBM and 0.684 for logistic regression, and the boosted trees are not monotone in the quote: sometimes a worse price wins more often. Client features carried no signal and cover-price features did not help. Government bonds and one dealer, so the desk took the graph and left the numbers.

One quote, owed since Chapter 4-C, belongs here. Dana Rourke's desk bid for \$15mm of Halvorsen at 2:58 on the Friday before the 8-K with one adjustment: fifteen cents, for the chance that the seller knew something (§4C.1). In the five terms, those fifteen cents were the whole toxicity charge, for a fund tier whose residual in front of a lender call was worth a point or more *(illustrative)*. Her inventory skew was the one her ten-point, two-day rule implied, a much steeper bowl than spread duration suggests. Her credit-alpha skew, the advisors' silence after the call, was priced at nothing. And the term she never wrote down was the subsidy: the client sat in the desk's top twenty, and the quarterly ranking rewarded showing a bid when others would not. Four terms push a bid down. The fifth pushed hers up, and it was paid to a client who knew more than she did.

## 18B.3 The Cover Price Is One-Sided Data

*Builds on:* §2.3.2 (order statistics), §3.2.3 (the winner's curse with many dealers), §3.3.5 (survivorship). *Used in:* Chapter 2-B §2B.1 (the same inquiry from the client's screen), §27.4 (the RFQ log as an order state), Appendix B (the RFQ-log schema).

> **Quant-Shop Life (fictional composite): the column called cover.** *Friday, 2:15 p.m. The desk, its log, its venues' exports and ROBO's output are invented.* The RFQ log comes from two venues whose exports agree on almost nothing. One stamps in New York time and one in UTC. One calls a withdrawn inquiry *cancelled* and the other *not traded*. Theo spent an hour on a reconciliation that did not tie by forty-one rows: inquiries clients pulled before the timer expired, logged by one venue and silently dropped by the other. It was the dullest hour of his month and the most useful, because the dropped rows were, by construction, RFQs nobody traded, and Kaz's estimator was about to need every one. Then Theo asked ROBO for "a column `cover_px` for every RFQ." On *Done* rows ROBO filled in the best rival's price, as meant. On *Covered* rows it filled in the desk's own price, because when the desk is covered the desk *is* the cover. On *Traded Away* rows it left a blank. Kaz's first fit read the column as "rivals' prices" and estimated the rivals partly from the desk's own quotes. ROBO had done precisely what was asked.

The fix was a schema, now in Appendix B. Every inquiry gets one row whatever happened to it: venue, client tier, side, size, dealers in competition as shown, whether the desk answered, its price, the composite at receipt, the best rival's price only where the venue reveals it, and an outcome from a fixed list. The list is the taxonomy of Fermanian, Guéant and Pu (2016), "The behavior of dealers and clients on the European corporate bond market: the case of Multi-Dealer-to-Client platforms" (*Market Microstructure and Liquidity* 2(3–4)): *Done*, *Tied Traded Away* (the desk tied for best and lost the tie), *Covered* (second best), *Other Traded Away* (further back) and *Not Traded* (the client traded with nobody).

"Covered," Kaz said, reading the list. "As in, we were insured?"

"As in, we came second," Theo said.

"And *Tied Traded Away* is a knot?"

"We tied for best and the client picked the other dealer. Usually because it likes them more."

Kaz wrote *relationship = tiebreaker* on a sticky note, which is a better definition than most.

The paper is the only public likelihood for the cover price, built on BNP Paribas's role as a reference dealer on Bloomberg FIT in 2014–15, up to six dealers per inquiry: 209,069 client buys and 272,189 client sells. The buys counted 44,745 Done, 2,892 Tied Traded Away, 44,054 Covered, 69,716 Other Traded Away and 47,662 Not Traded. Rivals' quotes are independent draws from $F$ (density $f$) on the half-spread scale around the CBBT mid, and the client's reservation value is a draw from $G$ (density $g$). A *Done* at the desk's quote $Y$, with the best rival's price $C$ revealed as the cover, has likelihood

$$
n\,f(C)\,\big(1 - F(C)\big)^{n-1}\,\big(1 - G(Y)\big),
$$

one rival at $C$, all the others worse, and a client willing to pay $Y$. *Not Traded* has likelihood $\int^{Y} \big(1 - F(v)\big)^n g(v)\,dv$: the client's reservation value $v$ fell short of the desk's price and of every rival's. *Covered* and *Other Traded Away* contribute the probability that one rival, or more than one, beat $Y$ and the client took the best of them.

> **Math, Gently.** *The cover is the best of $n$ draws, and seeing it only when you win hides half of it.* Each rival's quote is a random draw, and the cover is the best of them, an order statistic (§2.3.2). On a win the desk sees the cover; on a loss it sees, at most, that someone beat it. So the covers in the file are draws of "the best rival quote, given that it was worse than ours." A tiny number: two rivals quoting evenly between 0 and 1 point from mid, and a desk that always quotes 0.4. The true average best rival quote is 1/3 of a point. The desk wins only when both rivals are worse than 0.4, and then the cover averages $0.4 + 0.6/3 = 0.6$. Wins alone say the best rival sits at 0.6, nearly twice the truth: rivals look lazy and winning looks safe. The losses carry the other half of the distribution, and the likelihood above puts them back. The full version is in Fermanian, Guéant and Pu (2016), Section 3.

That is exactly what Kaz's first fit did. On the Done rows alone the rivals came out wide, the shading near zero, and the model announced that the desk never suffered a winner's curse. Ines laughed for the first time that week. "Every dealer who ever went broke believed that number." Refitted with the Covered, Traded Away and Not Traded rows supplying the other side of $F$, the rivals tightened and the shading came back. The blotter lists the hands the desk won; the estimator needs every hand it was dealt.

Two results changed the desk's model of its competition. Only about 40% of the dealers asked actually answer (0.400 on client buys, 0.424 on sells), and the rate falls as the panel grows: $p(n)$ = 1.00, 0.655, 0.498, 0.417 and 0.351 for one to five rivals, so the expected number of answers, $(n+1)\,p(n)$, is about two at every panel size (2.0, 1.97, 1.99, 2.09, 2.11). Clients, the authors conclude, "often wait for only two answers before dealing." And the client's mean reservation value sits about 1.7 half-spreads from the CBBT mid.

A toy calculation shows why the answer rate dominates *(ours, on the paper's published shares; illustrative)*. From the Table 1 counts, the desk's Done share falls from 35.1% with one rival to 19.0% with five. Suppose the desk quotes at the rivals' median and the client accepts 70% of the time. With one rival who always answers: $0.5 \times 0.7 = 35\%$, close to the data. If all five rivals always answered: $0.5^5 \times 0.7$, about 2%, nowhere near 19%. At the paper's answer rate of 0.351 the share is $(1 - 0.351 \times 0.5)^5 \times 0.7 \approx 27\%$, and matching 19% needs the desk's quote at about the 65th percentile of answered quotes. The rivals who answer quote tighter when the panel is bigger.

That is the paper's partial-participation result, and it corrects this book. Chapter 3 (§3.2.3) reports that dealer quotes "become more conservative as the number of requested dealers rises," which is the *full-participation* model's finding, an artefact of treating a dealer who did not answer as one who quoted badly. In the preferred partial-participation model the mean answered quote *tightens* with $n$, from 1.36 to 0.647 half-spreads on the buy side. Read §3.2.3's sentence as the full-participation result only.

The client sees the same inquiry from the other side of the screen, and Chapter 2-B reads it from there (§2B.1, with the survivor problem in §2B.1.3). Jacobsen, Venkataraman and Xu (2025), "Illiquidity Meets Intelligence: AI-Driven Price Discovery in Corporate Bonds" (SMU working paper, MarketAxess data, not peer-reviewed), give one more reason to keep every row: when an inquiry that did not trade falls between two trades, the CP+ composite's advantage over the last trade grows by 1.4 to 5.0 times. Theo's forty-one dropped rows had been information all along.

## 18B.4 How Many Dealers Are in the Room

*Builds on:* §2.3.2 ($n_{\text{eff}}$, the anchoring share $\phi$, the scale $\theta$), §3.2.3 (winner's-curse shading). *Used in:* §18B.5 (the stress switch), Chapter 2-B §2B.4 (the dealer scorecard), §19.9 ($\text{Leak}(n_{\text{eff}})$ in the participation rule).

Model review happens in a conference room with a broken blind and a screen that takes four minutes to find the laptop. The risk committee had read the engine's documentation, which is more than most committees do, and its first question was on the agenda. *Why is the competition parameter 4 when the platform screen says 27 dealers in competition?*

Theo's slide began with a data set from 2010. Hendershott and Madhavan (2015), "Click or Call? Auction versus Search in the Over-the-Counter Market" (*Journal of Finance* 70(1)), matched every US corporate-bond trade from January 2010 to April 2011 with MarketAxess's auction records. In their Table VI clients queried 25 to 28 dealers per auction; only 15.2% to 28.9% responded, rising with trade size; and 8.2% to 14.7% of auctions drew no response at all. High yield was worse, with response rates of 8.7% to 15.8% and about 60% of auctions drawing two bids or fewer. Dealers' decisions to bid, the authors note, "are not independent": in Table VII responses grow with the log of the number queried, with coefficients of 0.54 in investment grade and 0.45 in high yield. Invitations multiply; answers creep.

The independence check is the slide's punchline. In an investment-grade round-lot auction with about 27 invitees and a 26% response rate, independent dealers would all stay silent with probability $0.74^{27}$, about 0.03%. In the data, close to 9% of such auctions get no answer, roughly three hundred times as often. Dealers read the same market, run the same kinds of auto-quoter, and go quiet together.

> **Math, Gently.** *Correlation makes a crowd smaller, and a Beta distribution says how.* A **Beta distribution** describes an uncertain probability, a number between 0 and 1. Beta(1, 1) is flat; Beta(1, 3) leans toward small values, with mean $1/(1+3) = 0.25$. It is a natural model for "today's appetite." The **beta-binomial** model has each RFQ draw its own appetite $\pi$ from a Beta($a$, $b$), and then each of the $n$ invited dealers answers independently with probability $\pi$. Answers are independent *given* the appetite and correlated because they share it, with correlation $\rho = 1/(a + b + 1)$ between any two dealers. The number of answers is then as noisy as it would be with $n/(1 + (n-1)\rho)$ independent dealers: the same design effect as §2.3.2's eleven anchored dealers worth two and §28.2's effective breadth. A tiny number: with Beta(1, 3), the response rate averages 25% and $\rho = 0.2$. All 27 invitees stay silent with probability $B(1, 30)/B(1, 3) = (1/30)/(1/3) = 10\%$, against 0.04% under independence, and 27 invitations behave like $27/(1 + 26 \times 0.2) \approx 4.4$ independent ones. That is the committee's 4. The full version is `fit_response_corr` in §18B.9.

Fitted to Table VI, the beta-binomial gives a response correlation from about 0.06 for micro lots to 0.30 for the largest trades, so between 3 and 11 effective independent invitees out of 25 to 28 *(our arithmetic on their published means; illustrative)*. Index CDS is a different world: Riggs, Onur, Reiffen and Zhu (2020) find clients querying 4.1 dealers and receiving 3.6 responses. A bond panel's nominal size is a poor guide to its competition, and the gap is the parameter the desk estimates.

"This $\phi$," said the committee's newest member, pointing. "Is it the same $\phi$ as in the Riccati equation on page 3? And the one in your appendix?"

It was three different numbers. Barzykin and Ciceri use $\phi$ for risk aversion; Chapter 2 uses it for the anchoring share, the part of every quote distance that comes from a shared composite; and the beta-binomial correlation measures whether dealers *answer* together, not what they *say*. The engine now writes $\phi_\Sigma$, $\phi$ and $\phi^{\text{ans}}$. Kaz observed that Greek letters were running out. Ines suggested the committee be told that only one of them moved daily.

The two crowd-shrinkers do different jobs. $\phi^{\text{ans}}$ governs how many dealers show up, which the stress switch of §18B.5 watches; $\phi$ governs how many independent opinions they represent, which the winner's curse cares about. For an investment-grade round lot, 26.6 invitations at 26.1% give about 6.9 expected answers, and 6.9 answers anchored at $\phi = 0.45$ count as $6.9/(1 + 5.9 \times 0.45) \approx 1.9$ independent ones *(illustrative)*: about two, the number Fermanian, Guéant and Pu found clients waiting for. The engine shades its winner's-curse term (§3.2.3) by that, not by 27. The counts come from venues that report how many prices an inquiry drew and from the desk's own outgoing inquiries, which Chapter 2-B logs from the client's screen (§2B.4). The research behind this chapter found no published paper that estimates these numbers from a dealer's own log, so §18B.9's estimator is this book's construction, offered as one.

The committee's last question was the one every committee asks: why was the parameter 4.4 on Tuesday's pack and 3.9 on Wednesday's? "Because $\phi^{\text{ans}}$ moved," Theo said. "Wednesday afternoon a lot of dealers went quiet at once." The committee wrote this down and seemed, for once, satisfied by an honest answer.

> **View From Another Seat.** *The client that calls two.* From the buy side the 27 is a choice, and theory says it is the wrong one. In Wang (2023), "The limits of multi-dealer platforms" (*Journal of Financial Economics* 149(3)), each extra contact lowers every dealer's chance of responding, and in equilibrium the client contacts only two; no platform design improves its payoff. Baldauf and Mollner (2024), "Competition and Information Leakage" (*Journal of Political Economy* 132(5)), add the cost of asking: every extra contact is one more dealer who learns the client's direction and, if it loses, can trade ahead of it. The insurer is the extreme case: Hendershott, Li, Livdan and Schürhoff (2020), "Relationship Trading in Over-the-Counter Markets" (*Journal of Finance* 75(2)), find a third of insurers trading with a single dealer, and execution costs falling as a network grows and rising again past about 20 dealers. The client that sends 27 invitations buys a screen full of names; the client that calls two buys two dealers who believe they might win.

![Figure 18-B.1: How many dealers are in the room. The effective number of dealers $n/(1 + (n-1)\phi)$ against the nominal count for $\phi$ = 0, 0.06, 0.30 and 0.45; Hendershott and Madhavan's Table VI size buckets as dots at their fitted response correlations; and MarketAxess's April 2025 path (13.2, 6.6, 11.3 prices per RFQ) as three points on the 0.45 curve, which barely move. Illustrative: the design-effect formula of §2.3.2 and §18B.4, with the book's arithmetic on the published means.](assets/figures/ch18b_neff_map.png)

## 18B.5 Stress-Day Response Counts and the Switch

*Builds on:* §2.3.2 and §2.9.3 (9 April 2025 through $n_{\text{eff}}$), §18B.4. *Used in:* §27.7 (kill switches as stopping rules), §28.9 (the market-maker panel).

The second agenda item said *Stress parameters*, and Kaz had built the switch from public numbers, because the desk's own stress history was short. MarketAxess published the April 2025 episode in detail. Average prices received per US high-grade RFQ "dropped from 13.2 to 6.6 on April 9" and "rebounded to 11.3 within a week"; high-grade bid–ask spreads widened "by as much as 231%" to an average of 9.11 bp, against 44.62 bp at the COVID peak; and algorithmic responses were "consistently around 80%" of the liquidity (MarketAxess *AxessPoint*, 14 July 2025). In March 2026 the platform described Tradability, its machine-learning model of how many dealer responses an RFQ can expect: predictions fell "roughly 20% on a market-wide basis" between 2 April 2025 and the 8–10 April peak, and moved by "nearly an entire response" from one hour to the next within the day (MarketAxess *AxessPoint*, 23 March 2026).

Chapter 2 has already pushed 13.2, 6.6 and 11.3 through the effective-dealer formula (§2.3.2): at $\phi = 0.45$, $n_{\text{eff}}$ moved only from about 2.0 to about 1.9 and back, so the damage that day sat in the scale of everyone's quotes, $\theta$, and in $\phi$ itself, as the composites stopped deserving trust. The day is told elsewhere as a replay of the tape (§2.9.3), a cross-asset snap-back (§12.9, Beat 4) and a regulatory stress (§22.6.2). Here it is an input.

ROBO's first switch was built from the vague spec *go to stress parameters when responses drop.* It switched when fewer than seven dealers answered, and on its first live day it fired at 3:50 p.m. On its second live day it fired at 3:50 p.m. too. Afternoon panels are thin every day, because half of Europe has gone home. The switch had learned the clock, not the market.

The second version switches on a residual: the observed response count minus the count expected for that tier at that hour in a normal market, divided by its usual noise, which is Tradability's idea built from the desk's own log. It turns on after two consecutive hours more than two standard deviations below normal and off only after two hours back within one, so it does not flicker. When it is on, the engine widens its toxicity charge, shrinks its maximum size by tier and narrows its inventory band, and outside the band it stops internalising and hedges the excess in CDX or the ETF. The band comes from Barzykin, Bergault and Guéant's dealer-market papers (2023; FX tiers, 2021–23), in which "the larger the franchise, the wider the inventory range suitable for pure internalization." Their calibration is to FX, so the band's width on this desk is a judgment, revisited at each review.

What the switch cannot see is who leaves first. At a FILS Europe panel in October 2026, buy-side traders said electronic liquidity providers and platforms "help more in quiet markets," and one put the stressed version plainly: "When it becomes very stressful, you see clearly a concentration to the usual banks" (*The DESK*, 15 October 2026). A Bank of Canada working paper reaches the same place by theory: non-bank entry improves liquidity "more during normal times than in stress, leading to a bifurcation of liquidity" (Brolley and Cimon, Staff Working Paper 2025-2). A count that halves can mean everyone shaded or one kind of dealer left, which is why the switch tracks the residual by tier. Tradeweb also blogged about the April week, but its numbers could not be checked for this chapter, so none are used.

> **View From Another Seat.** *The buy-side automation desk.* The clients' robots have an off switch too. In The DESK's reports from the same FILS Europe event, Vanguard's fixed-income trader put the low-touch and no-touch share of its desks' volume (portfolio trades and RFQ lists, and auto-execution within preset parameters) at "more like 70%", against "maybe 40%" historically, and contrasted April 2025, when "a lot of that stayed there," with the Russia–Ukraine period, when "a lot of algos and PT execution got turned off" (*The DESK*, 14 and 15 October 2026). For a dealer this is the other half of the stress day. Many inquiries come from a client's automation with its own switch, and when it flips, the client's flow changes tier: the patient rebalancer becomes an urgent seller. The two switches turn on in the same hour, read the same tape, and do not consult each other.

## 18B.6 The Pod's Pair Hits Two Engines

*Builds on:* §18.6.3 (PB-14 opened, the Altice France morning), §18B.2 (the five terms), §18B.3 (the Covered state). *Used in:* Chapter 8-D §8D.7 (legging), §19.8 (the basket version), §27.7 (a price-reading kill switch).

*Pair Book entry PB-14, a replay cut off at 10:30 London time on Wednesday 20 March 2024, now told from the dealers' side. The desk, Dealer B, both engines, every quote, size, mark and P&L figure, and Owen Achterberg's pod at Vantress with Wen Zhao and Marcus Oyelaran are fictional composites; nobody on the desk saw Dealer B's screen, and its engine below is the desk's model of an engine with B's log. Altice France, Altice France Holding, their instruments, the dates and the 13:00 call are real and sourced in §18.6.3. The pod is an outside holder in no group.*

Ines ran the Altice replay a second time, a month after the first, with the 18-B engine bolted on. In §18.6.3 the desk was one dealer answering two tickets. This time she dealt two tables.

*10:40.* *Vantress buys €5mm Altice France 2027 first-lien notes, four dealers.* Dealer A was the desk itself, long exactly €5mm of the secured into a scheduled call, and its engine wanted out: the inventory skew pushed the offer a quarter of a point through the composite (§18.6.3 has the jump arithmetic). A filled at 10:41. Dealer B, a fictional mid-sized European bank desk, was flat, offered wider and came second. Its log recorded *Covered*.

"Second table," Ines said. "What does B know at 10:42?"

"That this client bought €5mm of the senior secured from someone tighter," Theo said. "The client, the direction, the size and roughly the price."

"Baldauf and Mollner's losing dealer," Ines said. "It lost the hand and saw the cards."

*11:20.* *Vantress sells €3mm Altice France Holding 8% notes due 2027, four dealers.* A and B were both on the panel again. The holdco composite had drifted from 50 at 10:40 to 49.5 *(illustrative)*. Theo put the two engines' bids on the screen, five terms each, in points below the 11:20 composite.

| Term | Dealer A (the desk) | Dealer B |
| :--- | ---: | ---: |
| Riskless spread | 0.35 | 0.35 |
| Inventory skew (with jump risk) | 1.45 | 0.15 |
| Credit-alpha skew | 0.70 | 0.10 |
| Residual-toxicity charge | 1.50 | 0.70 |
| Quality hit-ratio subsidy | 0.00 | −0.30 |
| **Bid below composite** | **4.00** | **1.00** |

*Table 18-B.1. Two engines price the same holdco RFQ at 11:20 on 20 March 2024 (replay; every number illustrative). Dealer B's toxicity line includes 0.10 of price-reading charge.*

Both engines priced the second ticket as the toxic one, and both were right. They disagreed about everything else. A's inventory line carried the jump, equation 18.7 with a holdco $J$ bigger than the secured's; B's engine was diffusive and charged the block like any other Wednesday. A's toxicity charge was larger because A had *filled* the first ticket and knew the direction for certain; B knew it as a Covered row, a strong hint. B's charge had a second, smaller part from the price-reading channel of Barzykin, Bergault, Guéant and Lemmel (arXiv 2508.20225, forthcoming in *Risk*): a tier that sees a dealer's quotes learns its appetite, and Vantress had seen B's 10:40 offer. And B paid a subsidy, because its ranking with hedge-fund clients had slipped and its engine was campaigning to win their flow back (§18B.7). So B's 48.5 won, a point and a half below the 10:40 composite: half a point of drift and a point of B's fear, net of B's generosity. A's 45.5 lost, which the desk's hand history now records as its best trade of the day.

"One hand at two tables," Ines said, "and the dealer at the second table had watched your first hand to the showdown."

Owen, back for the replay, did the pod's arithmetic. Legging cost a point and a half on €3mm, about €45,000 *(illustrative)*: half a point to drift and a point to having told B its direction by asking B twice. Tradeweb's researchers measure all-to-all leakage on US investment grade at "in the order of 0.1 to 0.3 basis points" within 100 minutes, larger for sells and less liquid bonds (Caretti, Mahajan and Husveth, Tradeweb white paper, May 2026; vendor-authored). Beside a point, that is a rounding error. The information did not leak through the tape. It leaked through the log.

From B's chair the story was worse. B's engine was right about the ticket and wrong about the size: 0.70 for toxicity, nothing for the jump, 0.30 paid to a tier it was courting, and €3mm of holdco bought an hour and forty minutes before the call that sent Altice's debt down about twenty points (§18.6.3). The pod's idiosyncratic view, *the discount lands harder on the holdco*, was exactly the toxicity B's engine was trying to price, and its subsidy paid the pod to hand it over. The pod's alpha is the dealer's toxicity charge, measured from the other side of the same ticket.

> **The Pair.** *PB-14 from the dealer's side, Owen's pod: long Altice France 2027 first-lien notes, short Altice France Holding 8% 2027 notes (borrowed through the prime broker). Sizes, marks and P&L are illustrative; instruments and dates are real.* **What the hedge removes.** Default itself, on the day, at the model's recoveries: €5mm of secured at 69 with a recovery of 55 against €3mm of holdco at 50 with a recovery of 27, sized by recovery-weighted market value (§18.6.3). **What idio remains.** How the discount is allocated across the structure, and nothing else. **What leaked.** Legging, priced by two engines. Between 10:41 and 11:20 the pod held only the long leg. The second leg went off 1.5 points below the 10:40 composite: 0.5 of drift and 1.0 of Dealer B's quote, whose largest line was a residual-toxicity charge earned by the first ticket. On €3mm that is about €45,000. The dealer's engine read the pod's idio as toxicity and charged for it, so part of the pod's alpha was spent before the call began. **What it costs to carry and to short.** As in §18.6.3: the long's coupon against the holdco's 8% owed on the short, and a borrow that is cheap on average and dear and recallable exactly when a holdco enters a restructuring (Asquith, Au, Covert and Pathak, 2013). **The dealer's mirror.** B, hedged in iTraxx Crossover if at all, removed the beta of its €3mm and kept the pod's idio inverted: long the leg the pod believed was further from the money. *Ledger:* opened in Chapter 18, stressed here, closed in Chapter 18.

> **View From Another Seat.** *The pod, reading its own fills.* Wen Zhao keeps the recall history of every borrowed bond as a time series and calls it the weather. Her weather on the holdco that morning was stormy: the borrow was located at 10:35, but its lenders had recalled twice in the past month *(illustrative)*. The pod did the secured first anyway, because Dealer A was offering it through the composite. "We legged in the order the prices made cheap," she said, "and the weather said to do the scarce one first." Marcus Oyelaran, the platform risk manager, read the morning off his x-ray and asked his usual question: what was the book long that it did not mean to be? Between 10:41 and 11:20, Altice France, outright. For thirty-nine minutes a capital-structure pod was a long-only high-yield fund in one name, €0.70mm of jump-to-default at the model's recovery, two hours before a call about discounts. The position was inside every limit. It was not the trade.

§19.8 runs the same logic on a basket, where the dealer's adverse-selection charge finds line 117, the one the client most wanted to be rid of. In both, the engine's toxicity term is a reading of the client's idio.

![Figure 18-B.2: The Altice France morning of 20 March 2024 from two dealers' seats. At 10:41 Dealer A fills the pod's secured buy; Dealer B's log records Covered. At 11:20 both bid for the pod's holdco sell: A's four points below the composite decompose into riskless spread, jump-laden inventory risk, credit view and a toxicity charge from the ticket it filled; B's one point is mostly toxicity, net of a subsidy. The pod's legging cost is shaded in two parts: 0.5 of drift and 1.0 of B's quote. Replay; fictional desks and pod; every number illustrative.](assets/figures/ch18b_two_engines_timeline.png)

## 18B.7 Gates, Campaigns and the Relationship Discount

*Builds on:* §18B.1 (the multiplier), §18B.6 (B's campaign). *Used in:* Chapter 2-B §2B.4 (scorecards from the client's side), §28.9 (the market-maker panel).

Once a quarter a platform sends the desk a slide with its rank among dealers for a client segment. This quarter's said seventh, down from fourth *(illustrative)*. Sales forwarded it with one word, *thoughts?*, which in sales means *panic*.

"Back in my day," Mags said, reading over Theo's shoulder, "the hit ratio was whether Sal picked up on the second ring." She read the slide again. "At least Sal didn't rank us."

The desk had run a campaign the previous spring to climb back from a similar slide: a larger $\nu$ for the segment for six weeks, enough to win its way up the list. It worked, and then the desk tried to harvest, cutting $\nu$ back to collect wider quotes from the flow the rank brought in. Within a month the rank fell again and the flow went with it. The desk could hold the rank or harvest it, not both, and the cost of the campaign was never recovered.

Barzykin (2026), "Win-score promotion gates in aggregator-routed RFQ markets: A two-tier stochastic control model" (arXiv 2603.10569), explains why. In his model, written for FX aggregators, one tier's flow is multiplied by a gate $G(R)$ of the dealer's slow-moving win score $R$; the other tier is ungated. When the gate is steep, the dealer's best policy has two stable states, promoted and demoted, and a fold between them: the quoting that keeps a promoted dealer promoted is not enough to promote a demoted one. The author calls the pattern "campaign vs. harvest." Applying it to bonds is an inference, but the desk's spring fits it uncomfortably well.

> **Math, Gently.** *Hysteresis: a thermostat with memory.* A thermostat set to 20°C does not switch the heating on at 19.99 and off at 20.01, or it would click all day. It switches on at 19 and off at 21, so in between, whether the heating is on depends on where the temperature came from, not just where it is. That dependence on the path is hysteresis. A ranked dealer has the same shape: between the subsidy that keeps a promoted desk on the list and the larger subsidy that gets a demoted desk back on, which state the desk is in depends on its history. Tiny number, illustrative: if staying promoted costs $\nu = 0.04$ and getting promoted costs $\nu = 0.09$, a desk at $\nu = 0.06$ stays where it is, promoted or not. The full version is Barzykin (2026), and the stress switch of §18B.5 uses the same trick on purpose.

If the platform ranks on hit ratio, then $\xi$ prices future access as well as this quarter's ratio, and the hit ratio is a state variable with memory rather than a score. The public evidence says the access is real and the score is a poor measure of it. Hendershott, Li, Livdan, Schürhoff and Venkataraman (2026), "Quote Competition in Corporate Bonds" (*Journal of Finance* 81(4)), using BondCliQ dealer runs, find that quoting a bond raises a dealer's chance of trading it that day by 4.8 percentage points and improves clients' execution by 6 to 7 bp, yet the best-quoting dealer gets only 15% of trades, and, depending on the dealer and the trade size, 16% to 40% of trades execute at a price worse than the best quote of the past hour. Relationships carry much of the rest. Jurkatis, Schrimpf, Todorov and Vause (2023), "Relationship discounts in corporate bond trading" (BIS Working Paper 1140), find that the top 1% of relationship clients pay 51% less than the median client, that the discount more than doubles in stress, and that it is larger for clients who help dealers manage inventory, with no sign that dealers discount clients to learn their information. In FX derivatives, Hau, Hoffmann, Langfield and Timmer (2021) find the median non-financial client paying 10.9 pips more than blue-chip firms. Dealers also publish their own league tables now: in autumn 2026 Citadel Securities reported, by its own estimates and as relayed by The DESK, a 14.2% share of US investment-grade block risk transfer, a self-reported figure with no denominator stated.

> **View From Another Seat.** *The platform, in its own words.* MarketAxess describes Tradability as a machine-learning model of the dealer responses an RFQ can expect, whose movements reflect "uncertainties felt by liquidity providers" (*AxessPoint*, 23 March 2026). From the venue's seat the dealer panel is a supply curve to be forecast and routed, and a dealer's hit ratio and response record are inputs to that forecast. The desk's multiplier is, from there, a bid for a place in the router's model.

## 18B.8 Fill Curves, and What Happens When Every Desk Runs This

*Builds on:* §18.7 (the logistic win curve), §18B.2 (monotonicity). *Used in:* Chapter 22 (regulatory scrutiny of algorithmic quoting), Chapter 26 (evaluation hygiene), §27.4 (the fill service).

A junior on Kaz's team brought a fill model to the Tuesday research meeting with an out-of-sample AUC of 0.97. Kaz asked one question: what happens if the test set starts four days after the training set ends instead of the next morning? By four days the AUC was 0.66. The model had been reading tomorrow's composite through a feature stamped with today's date. A score that decays as the gap between training and testing widens is a leak, not a signal.

The honest benchmark is public. Ciceri, Cottrell, Freeland and coauthors (2025), an HSBC and IBM Quantum team (arXiv 2509.17715), fit 1,073,926 European corporate-bond RFQ responses over 294 trading days with 216 features: logistic regression, gradient boosting, random forests and neural networks all reach an out-of-sample AUC of about $0.63 \pm 0.04$, flat across zero to four days of blinding. Their quantum-transformed features lift it to 0.97 in one configuration, an uplift the authors call "questionable" and do not explain. On government bonds, Marín Martínez et al. reach 0.74 with nine features, the quote itself among them (§18B.2). Credit fills are hard to predict, and a model that is not monotone in the quote has to be wrapped until it is before the engine inverts it.

The last problem is the one no backtest shows. Every engine in this chapter takes the rivals' fill curve as given. If every desk fits the same curve on the same platform and quotes off it, the curve is the engines' joint output. Cont and Xiong (2024), "Dynamics of market making algorithms in dealer markets: Learning and tacit collusion" (*Mathematical Finance* 34(2)), show in simulation that independent learning quoters, sharing no information, "may give rise to tacit collusion, with spread levels strictly above the competitive equilibrium level." Chapter 22 takes up the regulators' interest in exactly that.

> **Trend Watch.** *The quoting frontier, 2025–2026.* **9 April 2025:** average prices per US high-grade RFQ on MarketAxess fall from 13.2 to 6.6 and recover to 11.3 within a week (§18B.5). **22 September 2025:** HSBC and IBM publish fill-probability AUCs of about 0.63 on 1.07 million corporate RFQ responses. **27 January 2026:** Marín Martínez et al. publish the causal graph for RFQ hits in *PLOS ONE*. **11 March 2026:** Barzykin's win-score gates. **22 April 2026:** Barzykin and Ciceri's hit-ratio-targeted HJB (revised 27 July 2026). **13 May 2026:** Tradeweb's all-to-all leakage study, 0.1 to 0.3 bp. **28 May 2026:** Niang's five-term, quality-adjusted quote. **August 2026:** Hendershott et al.'s quote-competition paper appears in the *Journal of Finance*. **15 October 2026:** buy-side traders at FILS Europe report that platforms and electronic liquidity providers help more in quiet markets than in stress. What it means for the desk: the papers above arrived within about eighteen months, and all of the quoting theory in them is calibrated on synthetic or proprietary data, so the replication burden falls on whoever runs it.

## 18B.9 The Quoting Game

*Builds on:* every section above. *Used in:* Chapter 2-B §2B.4, §19.9, §27.4 and §27.7, Appendix B.

The first spec Theo wrote for the engine said *target hit ratio 25% on the asset manager's account.* ROBO met it in two days. The account's hit ratio was 25%, and almost all the new wins came from the account's event-driven sleeve, where the other dealers shade hardest and a cent of coupon buys the most wins. ROBO had found the cheapest RFQs to win, which were the most expensive ones to own.

The game in `rfq_engine.py` is that spec failure, made into something a reader can play. It solves the problem this chapter has been circling: given a book of client tiers, how much is a hit-ratio target worth, who receives the subsidy, and how much does it cost when the wrong tier receives it. It computes six things, one per section. `fit_response_corr` fits the beta-binomial of §18B.4 to answer counts and returns the answer rate, $\phi^{\text{ans}}$ and the effective number of invitees. `cover_loglik` and `fit_rival_scale` are §18B.3's likelihood over every outcome, with exponential rival quotes, a probability of answering and an exponential client reservation, so the rivals' scale comes from the whole log; `simulate_log` writes a synthetic log and keeps, beside it, the best rival quote that no desk ever sees, so the win-only estimate can be graded against the truth. `tier_dual` solves the one-bond Riccati curvature and the hard-target multiplier for a tier at any inventory. `quote_decompose` prices an RFQ cumulatively through Niang's five terms, so the terms add up exactly to the quote. `stress_switch` is §18B.5's residual switch with hysteresis. `play` runs the game: three tiers (an index rebalancer, the asset manager and an event-driven pod with a planted residual toxicity of 0.8 points), one account target, and two engines, raw and residual. It works in expected values rather than simulated fills, so its grade is deterministic. The asserts at the bottom are the grade: the residual engine earns more at every target, wins a sixth as much of the toxic tier, and serves the asset manager better.

It is built from closed forms on purpose. The Lambert-W quote and the Riccati square root make every number traceable by hand, which matters more on a model-review slide than a second decimal of accuracy. Its inputs are tier dictionaries (arrival rate, size, win-curve intercept and slope, residual toxicity), a variance and a risk aversion, and for the estimators an RFQ log in the Appendix B schema. Its outputs are prices in points, ratios and P&L in points times millions per day, every one illustrative.

It is the right tool for a desk deciding *whether* a target is worth paying for and *whom* to pay, and for a model review that wants to see the five terms add up. It is the wrong tool for live quoting: it has one bond, no inventory dynamics in the game, logistic curves that a real tier will not obey, and a toxicity that is known rather than estimated with error. The edge case that bites is the order of the five terms. Because the win curve is nonlinear, pricing the toxicity before the subsidy gives slightly different term sizes from pricing it after; only the total is order-free. The listing fixes the order to match the formula, and a desk comparing two decompositions has to use the same order in both.

![Figure 18-B.3: The same bond's bid priced for three tiers, as five cumulative terms from `quote_decompose`: the index rebalancer gets the riskless spread and inventory skew only; the asset manager also receives a subsidy bar, because its fills count toward the target; the event-driven pod pays a toxicity bar and receives almost no subsidy, because its weight $e^{-\eta\chi}$ is close to zero. Illustrative: the synthetic book of §18B.9 at an inventory of +\$5mm.](assets/figures/ch18b_five_terms_by_tier.png)

*The full python listing is [Listing 18-B.1 in Appendix F](#code-18b-1).*

### When the engine fits, and when it breaks

The engine earns its keep where flow is tiered, repeated and large enough to estimate: a few thousand RFQs a month per tier, residual markouts with stable signs, and a target that sales will keep for more than a quarter. It breaks in four places the desk has now visited. A factor model that misses a factor turns that factor into "toxicity" and starves a good client (§18B.2). A log without its losses estimates rivals who do not exist (§18B.3). A switch on raw counts learns the clock (§18B.5). And a ranked platform makes the multiplier path-dependent, so a campaign priced as this quarter's cost is underpriced (§18B.7). A seasoned trader looking at a new engine asks to see two things before any P&L: the five terms for one toxic RFQ, and the hit ratio by tier for the week the target was met.

## 18B.10 Desk Debrief

- A hit-ratio target is a price per point of hit ratio. It rises when the bowl steepens and bends with inventory, so it is re-solved with the morning risk pack, not once a quarter. [L5]
- Five terms, five addresses: the subsidy goes to targeted tiers, weighted by quality, and the toxicity charge goes to the residual after factor, carry, issuer RV and index flow are stripped. IDO or it didn't happen, applied to the client. [L1, L5]
- Markouts on wins sit behind a collider, and covers are seen only on wins. The Covered, Traded Away and Not Traded rows are the estimator; the blotter is not. [L14]
- Twenty-seven invitations behave like about four independent coins and about two independent opinions. The winner's curse is shaded by the answer rate and $n_{\text{eff}}$, never by the screen's count. [L2, L5]
- A stress switch keys on the residual against the expected count for that tier and hour, with hysteresis, or it learns the clock. [L11]
- A pair's two RFQs are two engines sharing a log; the second leg pays for the first, and the dealer's toxicity charge is the pod's legging cost. [L5, L6]
- *Pair Book, PB-14 (stressed here):* legging leak 1.5 points on €3mm of holdco, 0.5 of drift and 1.0 of Dealer B's toxicity-led quote, about €45,000 *(illustrative)*; thirty-nine minutes long Altice France outright; the dealer that won the second leg inherited the pod's idio, inverted.

### The Spec You Hand the Robot

Build `rfq_engine.py` to quote one bond for a book of client tiers. Inputs: tier records (arrival rate, size, logistic win-curve intercept and slope, residual toxicity in points, targeted or not), price variance per day, risk aversion, inventory, the desk's credit view, a hit-ratio target, and an RFQ log in the Appendix B schema with all five outcomes. Outputs: the curvature $A$, the target's multiplier for each targeted tier at the current inventory (zero when slack), the five-term decomposition of any quote with terms summing to the quote, the rivals' quote scale from the full-log likelihood, the answer correlation $\phi^{\text{ans}}$ and effective invitees, and a stress flag from the residual of responses by tier and hour. Weight the subsidy by $e^{-\eta\chi}$. Never estimate rivals from wins alone. Label every calibrated number with its source.

### Exercises

1. **The price of a storm.** On §18.7's curve ($\beta_0 = 0$, $\beta_1 = 4$) near a 15% win rate, $A = 0.06$ points per \$mm and RFQs average \$2mm. Volatility doubles. By how much does the multiplier rise to hold the hit ratio, and what happens to the hit ratio if it does not? *Solution.* The per-unit cost $Az/2$ rises from 0.06 to 0.12 points. The coupon offsets cost one for one, so $\nu$ rises about 6 cents; left alone, the hit ratio falls about $0.51 \times 6 \approx 3$ points.
2. **Kaz's win-only fit.** Three rivals quote uniformly between 0 and 1 point and the desk always quotes 0.25. What is the true mean best rival quote, and what does the average cover on wins say it is? *Solution.* $1/4$ against $0.25 + 0.75/4 = 0.4375$: the win-only estimate overstates the rivals by 75%.
3. **The committee's number.** Answer appetite is Beta(1, 4) and 25 dealers are invited. Find the mean answer rate, $\phi^{\text{ans}}$, the chance of no answers, the same chance under independence, and the effective number of invitees. *Solution.* 0.2; $1/6$; $B(1,29)/B(1,4) = 4/29 \approx 14\%$ against $0.8^{25} \approx 0.4\%$; $25/(1 + 24/6) = 5$.
4. **An honest Dealer B.** In Table 18-B.1, give Dealer B Dealer A's inventory line (1.45) instead of 0.15. What does B bid, and if a third dealer bid 2.5 below the composite, who wins and what is the pod's legging leak? *Solution.* B bids 2.30 below 49.5, at 47.2, and still wins against 47.0; the leak becomes $50 - 47.2 = 2.8$ points, about €84,000. Engines that price the jump make legging dearer.
5. **ROBO's 25%.** In `play`, why do the raw engine's extra wins land in the event-driven tier? *Solution.* Its win curve has a higher intercept ($\beta_0 = 1.5$: rivals shade hard there), so each cent of coupon buys more wins, and the account-average toxicity undercharges it. The residual engine's weight $e^{-5 \times 0.8} \approx 0.02$ removes the coupon there.

### Deep-Dive Resource Graph

**Podcasts**
- **"Jeremy Maletz"** (*Money Stuff: The Podcast*, 2026-10-09). A Susquehanna market maker, from its prediction-markets desk, on flow versus bespoke trading and adverse selection: the toxicity term of §18B.2 from a practitioner. https://omny.fm/shows/money-stuff-the-podcast/jeremy-maletz
- **"Why the True Price of a Bond Can Still Be Hard To Know"** (*Odd Lots*, 2021-04-05). Evaluated prices disagree for thin bonds, which is why every engine here anchors to a composite and why $\phi$ is large (§18B.4). https://omny.fm/shows/odd-lots/why-the-true-price-of-a-bond-can-still-be-hard-to
- **"How Investors Fall Into Bias Traps with Economists Richard Thaler & Alex Imas"** (*Masters in Business*, 2026-01-16). The winner's curse in plain language, the intuition behind §18B.3's one-sided covers. https://omny.fm/shows/masters-in-business/how-investors-fall-into-bias-traps-with-economists-richard-thaler-alex-imas
- **"BlackRock Sees Credit Pain as Tariff Confusion Reigns"** (*The Credit Edge*, Bloomberg Intelligence, 2025-04-24). The April 2025 week behind §18B.5's response counts, from a buy-side seat.

**Practitioner Writing**
- MarketAxess, "Credit markets showed resilience through April volatility" (*AxessPoint*, 2025-07-14): the 13.2, 6.6 and 11.3. https://www.marketaxess.com/article/axesspoint-credit-markets-showed-resilience-through-april-volatility
- MarketAxess, "Tradability deep dive" (*AxessPoint*, 2026-03-23): expected responses as a model. https://www.marketaxess.com/article/axesspoint-tradability-deep-dive-insights-powered-by-an-enhanced-liquidity-metric
- The DESK, "Don't rely on platforms or ELPs in stressed markets, buyside traders say" (2026-10-15), https://www.fi-desk.com/dont-rely-on-platforms-or-elps-in-stressed-markets-buyside-traders-say/ , and "FILS Europe: Vanguard automates 70% of trades, others urge caution" (2026-10-14), https://www.fi-desk.com/fils-europe-vanguard-automates-70-of-trades-others-urge-caution/
- Caretti, Mahajan and Husveth, "Information Leakage in US Credit: Evidence from All-to-All RFQs" (Tradeweb, May 2026; vendor-authored). https://www.tradeweb.com/49a042/globalassets/newsroom/market-insights/2026/5.13.26-credit-whitepaper/information-leakage-in-us-credit-5.13.26b-final-1.pdf
- Brolley and Cimon, Bank of Canada Staff Working Paper 2025-2 (2025-01-08), the bifurcation of liquidity. https://www.bankofcanada.ca/wp-content/uploads/2025/01/swp2025-2.pdf
- Lee and Martin, "How Does Information Affect Liquidity in Over-the-Counter Markets?" (NY Fed *Liberty Street Economics*, 2020-01-13). https://libertystreeteconomics.newyorkfed.org/2020/01/how-does-information-affect-liquidity-in-over-the-counter-markets/

**Academic Papers**
- Barzykin and Ciceri (2026), "Bond Market Making with a Hit-Ratio Target," https://arxiv.org/abs/2604.20406 ; Niang (2026), "Quality-Adjusted Hit-Ratio Targeting in Corporate Bond Market Making," https://arxiv.org/abs/2605.30643 ; Barzykin, Bergault, Guéant and Lemmel, "Optimal Quoting under Adverse Selection and Price Reading," https://arxiv.org/abs/2508.20225 ; Barzykin (2026), win-score gates, https://arxiv.org/abs/2603.10569 .
- Fermanian, Guéant and Pu (2016), *Market Microstructure and Liquidity* 2(3–4), https://arxiv.org/abs/1511.07773 ; Marín Martínez, Ardanza-Trevijano and Sabio (2026), *PLOS ONE* 21(1), https://arxiv.org/abs/2506.18147 ; Ciceri et al. (2025), fill probabilities with quantum features, https://arxiv.org/abs/2509.17715 ; Cartea and Sánchez-Betancourt (2025), https://arxiv.org/abs/2503.18005 ; Bergault, Evangelista, Guéant and Vieira (2021), https://arxiv.org/abs/1810.04383 .
- Hendershott and Madhavan (2015), *Journal of Finance* 70(1), https://faculty.haas.berkeley.edu/hender/Click_Call_OTC.pdf ; Hendershott, Li, Livdan, Schürhoff and Venkataraman (2026), "Quote Competition in Corporate Bonds," https://faculty.haas.berkeley.edu/hender/Quote_Competition.pdf ; Hendershott, Li, Livdan and Schürhoff (2020), https://faculty.haas.berkeley.edu/hender/OTCRelations.pdf ; Jurkatis, Schrimpf, Todorov and Vause (2023), BIS WP 1140, https://www.bis.org/publ/work1140.htm .
- Without links: Wang (2023), *JFE* 149(3); Baldauf and Mollner (2024), *JPE* 132(5); Riggs, Onur, Reiffen and Zhu (2020), *JFE* 137(3); Hau, Hoffmann, Langfield and Timmer (2021), *Management Science* 67(11); Cont and Xiong (2024), *Mathematical Finance* 34(2); Asquith, Au, Covert and Pathak (2013), *Journal of Financial Economics* 107(1).

**Data & Code**
- `rfq_engine.py` (Appendix F), with the RFQ-log schema in Appendix B. Jacobsen, Venkataraman and Xu (2025), working paper with MarketAxess data, https://microstructure.exchange/papers/JVX_20250904.pdf . Man's buy-side RFQ filter on frequency and completion rate (shelf: `Man_Revolutions_in_Credit_Trading_2023` p.5).

<!-- STATUS: COMPLETE -->
