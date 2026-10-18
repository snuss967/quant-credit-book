# Chapter 18-B: The RFQ Response Engine

> **Prerequisites.** Chapter 18, in particular §18.4–§18.7 (the HJB, the win curve, the multiplier $\nu$ and equation 18.9) and §18.6.3 (Altice France, where Pair Book entry PB-14 opened); §2.3.2 (order statistics and the effective number of dealers); §3.2–§3.3 (Glosten–Milgrom for RFQs, markouts, survivorship). Every new piece of mathematics gets a Math, Gently box where it first appears. The chapter ships `rfq_engine.py` through Appendix F.

*What is invented, once for the whole chapter.* The desk, its traders, its RFQ log, its client tiers, its weekly tiles, its risk committee, its platform review, Dealer B in §18B.6 and every number marked illustrative are fictional composites. So are Owen Achterberg's capital-structure pod and Dov Adler's pod at Vantress Capital Management, Wen Zhao and Marcus Oyelaran (Chapters 1-B and 4-C). Altice France, its instruments and the dates of March 2024 are real and sourced in §18.6.3. The papers, platform statistics and quoted public remarks are real and cited. Every calibrated number taken from a paper is that paper's authors' own, most of them computed on synthetic data, and the text says so where they appear. No real dealer's engine is described anywhere in this chapter; HSBC and BBVA appear only as the affiliations of authors of published papers.

## 18B.0 Cold Open: The Green Tile That Was Lying

Monday, 7:40 a.m. The RFQ loop has a rota, like the coffee machine and the fire drill, and this week the rota said Theo. The job is the third of the three intraday loops of §3B.1, the one that watches hit ratios and cover gaps, and at 7:40 on a Monday it is mostly a job of looking at last week. Each client tier gets a tile. Each tile carries a number, a band and a colour, and the colour is the only part most people read.

The tile that mattered was the asset manager's, the client whose panel-review e-mail in §18.7 had given the desk its hit-ratio target in the first place. Hit ratio 17%, against a target of 15% and a band of three points either side: green. Average cover gap on wins, the distance between the desk's winning price and the second-best price, 8 cents, against 6 the week before and a band of three cents: green. *(The tiles, targets, bands and every number in this scene are illustrative.)* The rota sheet said a green tile gets initials. Theo initialled it.

Ines stopped behind his chair with a coffee, read both tiles, and did not move on.

"You've been paying them to trade with you for a week," she said.

"Both green."

"Each one's green. Read them together." She put the cup down on the only part of his desk without paper. "Hit ratio up: you won more. Cover gap wider: when you won, the next-best price was further from yours than it used to be. You could have shown a worse price and still won. So the extra wins came from giving the client more than the table required. That's a subsidy with a receipt."

Theo had met the pattern in §3B.2, written down in the tone such sentences take: a hit ratio that creeps up while cover gaps widen means the desk is paying clients to trade with it. He had never watched it happen, and what he noticed now was that nobody had done anything wrong. The target had been met. The engine had done exactly what it was told.

"Who changed what?" he asked.

"Nobody, which is the interesting part. Kaz, what's $\nu$ on that tier?"

Kaz, two seats down and still in a coat, looked. "Seven cents. I refitted it on the four weeks to the end of September, so the target would hold through month-end."

"And what was the tape doing in September?"

"Choppy. Realized vol about twice last week's, and we were carrying month-end inventory." A pause, which was Kaz rerunning something. "Last week was quiet, and we were flat."

"So you priced the target in a storm and paid the storm price in the sunshine," Ines said. "Give me the tier, not the average."

The tier view took Theo four minutes. He split the week by day and by the book's inventory at the moment of each RFQ. The extra wins were not spread across the week. They sat on Tuesday to Thursday, in the calm hours when the desk was flat, which were exactly the hours in which its ordinary quote already won about as often as the target wanted. Seven cents had bought hit ratio where hit ratio was cheap, so it had bought a lot of it, and on each of those trades it had paid two cents more than the cover required. Across about two hundred wins of a couple of million each, that came to about \$80,000 *(illustrative)*: a rounding error for the desk, and a very pleasant week for the client.

"So the target isn't a score," Theo said slowly. "It's a price. Somebody decides what we pay per point of hit ratio, and the tile only shows whether we bought the points. It doesn't show what we paid for them."

"Or who got the money," Ines said. "A subsidy always lands on somebody."

Kaz had already stood up and was walking toward the whiteboard, which on this desk is how a morning changes plans.

By the end of this chapter you will be able to read a hit-ratio target as a shadow price that moves with the market's volatility and the desk's inventory, and to say when it needs re-solving; split a quote into the five terms that Niang (2026) gives it, and name the client tier that receives each one; estimate the rivals' quote distribution from the desk's whole RFQ log rather than from its wins; count how many dealers are really in the room, from the desk's own data, and see why the screen's number overstates it; build a stress switch that does not fire every afternoon at 3:50; take apart, quote by quote, what two dealers charged Owen's pod for its two Altice France tickets on 20 March 2024; and recognise when a platform's ranking turns the hit ratio into a state with memory. On the way you will see why a fill model with an AUC of 0.97 is a bug report.

## 18B.1 The Target Is a Price

*Builds on:* §18.4–§18.7 (the HJB, the win curve, the multiplier $\nu$, equation 18.9). *Used in:* §18B.2 (the subsidy term), §18B.7 (when the price buys future access), §19.9 (the participation rule), §28.9 (the market-maker panel).

Kaz's whiteboard still had equation 18.9 on it in green from the month before, with the $+\nu$ circled. Kaz drew a box around the whole bid and wrote *one RFQ* above it in red. Then they drew forty more boxes in a row, and a long bracket underneath: *15% of these, please.*

"Here's the problem," Kaz said. "Every quote is its own small optimisation, except for the target, which ties them all together. Win too few this quarter and the client reviews its panel. So in principle every quote depends on every other quote, past and future, and the control problem is a monster with forty heads."

"And in practice?"

"In practice there's a trick, and the trick is most of the chapter."

The trick is one line of algebra, and it is the reason the target behaves like a price. Barzykin and Ciceri (2026), "Bond Market Making with a Hit-Ratio Target" (arXiv 2604.20406), penalise the gap between the desk's expected hit ratio $r$ and its target $r^\star$ quadratically, with a strength $\kappa$, and then rewrite the penalty as the lowest of a family of straight lines:

$$
-\frac{\kappa}{2}\,\big(r - r^\star\big)^2 \;=\; \inf_{\xi}\Big[\,\xi\,\big(r - r^\star\big) + \frac{\xi^2}{2\kappa}\Big].
$$

Minimising the bracket over $\xi$ gives $\xi = -\kappa(r - r^\star)$, and substituting back returns the left-hand side, so nothing has been lost. Something has been gained. For any fixed $\xi$ the objective is now *linear* in $r$, and $r$ is an average of fills across RFQs, so the forty-headed problem falls apart into forty one-headed ones. Each RFQ earns, if it is won, a coupon equal to $\xi$ times its own weight in the hit ratio. The engine quotes each RFQ alone, with the coupon attached, and the only thing tying the RFQs together is the single number $\xi$. Kaz's $\nu$ in §18.7 is this coupon, rescaled to one RFQ; the paper writes it $\tilde\xi$. Equation 18.9 adds $+\nu$ to the bid, which is the same thing as pretending the desk's reservation price is $\nu$ better than it is. In the paper's notation the reservation term $\Delta u$ becomes $p = \Delta u - \tilde\xi$ for targeted tiers and stays $p = \Delta u$ for everyone else.

"So the multiplier is what one more point of hit ratio costs us," Theo said. "The way a covenant has a shadow price."

"Say more," said Kaz, who had never seen a covenant.

> **Math, Gently.** *A shadow price that moves with the book.* Every constraint has a shadow price: what it costs you to tighten it by one unit. Theo's version is the minimum-liquidity covenant. Requiring a company to hold one more million of cash costs it almost nothing in a quarter when cash is piling up, and costs it the whole negotiation in a quarter when cash is short. The constraint did not change; the price of obeying it did. The hit-ratio target works the same way, and what moves its price is the shape of the desk's own risk. Picture the desk's value as a function of its inventory as an upturned bowl, $-\tfrac12 A q^2$: flat at zero inventory, falling faster the more it holds, because each extra million lands on a bigger position. The number $A$ is the bowl's steepness, in points of price per million of inventory. The bowl gets steeper when the market is more volatile or the desk more risk-averse, and flatter when there is plenty of client flow to trade out with. In the simplest one-bond case the steepness is a square root, $A = \sqrt{\text{risk aversion} \times \text{variance} \,/\, \text{liquidity}}$, so doubling the volatility (four times the variance) doubles $A$. Even at zero inventory a trade of size $z$ costs the desk about $A z/2$ per unit on each side, because the trade itself moves the desk halfway down the bowl on average, and the quote passes most of that cost on to the client as width. Now a tiny number, all of it illustrative. In a calm week $A = 0.05$ points per million and the average RFQ is \$1mm, so each side carries $0.05 \times 1/2 = 2.5$ cents of extra cost that a riskless desk would not have. In a week with twice the volatility $A = 0.10$, and the extra cost is 5 cents. On §18.7's win curve with $\beta_1 = 4$ per point, near a 20% win rate each cent of extra cost lowers the win probability by about half a point, so the choppy week shaves about 1.3 points off the hit ratio the desk would achieve with no coupon at all. The coupon offsets cost one for one, so buying those points back takes a coupon about 2.5 cents larger. Five cents becomes seven and a half. That is the seven cents in the cold open, fitted in a storm and paid in the sunshine. The full version, with the Riccati equation that sets $A$, is the derivation below.

The derivation says one more thing, and it is the thing the cold open tripped over. The multiplier is not a property of the client. It is a property of the client *and the desk's state*: the steepness of the bowl, which moves with volatility, and the inventory itself. Barzykin and Ciceri find on their synthetic book that a multiplier held constant fails when inventory is large, because the multiplier that would hit the target is roughly quadratic in the inventory. The mechanism is visible on the whiteboard. Inventory skews the quote, tightening one side and widening the other. Whether the two sides together win more or less often depends on where the tier sits on its S-shaped win curve. At low win probabilities, the convex part of the S, the tightened side gains more wins than the widened side loses, so a heavy book raises the hit ratio and the target gets cheaper. At high win probabilities the curve is concave and the effect reverses. Either way, a constant is wrong in both directions on different days. The desk's reading is mundane and slightly expensive: the multiplier is re-solved when the bowl changes shape, which on a credit desk means every morning, with the risk pack.

Two findings in the paper are cheerful. A tier the desk does not target at all, which Barzykin and Ciceri call background flow, cuts the inventory skew and raises the hit ratio achieved in the targeted tier; so does a correlated background bond. The intuition is that two-sided flow nobody is paying a coupon for drains the inventory that makes the bowl steep, and a flatter bowl makes the target cheaper. On Ines's desk the background flow is an index fund's rebalancing desk, which sends large, dull, two-sided inquiries around month-end, never complains about its hit ratio and has no idea that it is the desk's best hedge.

The numbers in the paper are synthetic, and the paper says so: a size ladder of \$1mm, \$5mm and \$20mm, arrival rates of 500, 200 and 50 RFQs a day, sigmoid fill curves, a target of $r^\star = 0.1$ and a one-day horizon, with no RFQ data and no public code. The closed-form approximation that the desk can run in production is, in the authors' phrase, "impressively accurate" against the exact numerical solution on that synthetic book. Nobody has replicated it on a real log. Kaz wrote *SYNTHETIC* next to every number on the whiteboard, in capitals, which is how Kaz labels things they intend to rely on anyway.

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

summed over the targeted tier's sizes and sides, with $\bar Z$ that tier's size-weighted RFQ flow (the paper's $W$, renamed here because $W_t$ is a Brownian motion in this book). Since $-H'(0)$ is the fill rate at zero cost, the first two terms are the target minus the hit ratio the desk would achieve with no coupon and no inventory risk. The third grows with the curvature $A_{mm}$. A steeper bowl makes the target dearer, which is the box's arithmetic in matrix form. Three terms is the whole of Barzykin and Ciceri's decomposition. The five-term quote that §18.7 and the Edition 2 plan both credited to them belongs to the next section's paper, and §18.7's attribution gets a one-clause fix in this edition.

One limitation decides how the desk uses the result. The paper penalises the *expected* hit ratio, a smooth surrogate that keeps the problem Markovian; the literal count that sales reads at quarter-end, wins over requests in a window, would need cumulative counts as state variables, and the paper sets that aside. So the engine targets one number and the tile reports another. A week of bad luck shows up as a miss on the tile that the engine never saw coming, and the desk explains it to sales with the phrase "expected versus realized," which sales has heard before.

## 18B.2 Three Terms to Five

*Builds on:* §3.3 (markouts, the hand history, IDO markouts), §3.3.5 (survivorship), §18.7 (suspicion $a_c$). *Used in:* §18B.6 (the two Altice quotes), §19.8 (the basket's adverse-selection charge), §27.7 (CUSUM on markouts, by tier).

Thursday is markout review, which on Ines's desk means the hand history (§3.3): every fill of the week, marked against the composite five minutes, an hour and a day later, sorted by client tier. Theo had brought it sorted the new way, by tier and then by residual. Kaz had brought a proposal.

The proposal was to give the engine a toxicity term per tier, so that a client whose fills tended to move against the desk paid for it in the quote, and to take the toxicity from the hand history directly: average markout per tier, the bigger the loss, the bigger the charge. It was simple, it was data-driven, and it ran in production on Wednesday afternoon. By Thursday at 10:15 the carry-and-relative-value tier, an insurer's total-return sleeve and two relative-value funds, had a hit ratio of about 1% *(illustrative)*. At 10:50 the salesperson who covers the insurer called to ask, with great courtesy, whether the desk had stopped making markets in investment grade.

"Their markouts are terrible," Kaz said. "Every time they buy, the bond goes up."

"Every time they buy, they buy a bond with a fat coupon on a steep part of the curve," Theo said. He had the decomposition up. "A third of the markout is carry and rolldown: the bond accretes toward where the curve says it should be, a little every day, and we'd see it on any bond with that coupon and that maturity. Another chunk is the market: IG rallied two days this week. A bit is the issuer's own curve. What's left after that is about zero." He scrolled. "The event-driven tier is the opposite. Its gross markout looks mild because the market sold off on the days it sold to us, which flattered it. Strip the market out and its residual is the worst on the page."

"IDO or it didn't happen," Ines said, "applied to the client." It is the desk motto's second job. The first job, in Chapter 8, is to stop the desk from calling beta alpha. The second is to stop it from calling carry information.

This is the move Niang (2026), "Quality-Adjusted Hit-Ratio Targeting in Corporate Bond Market Making" (arXiv 2605.30643), builds an engine around. Each tier's markouts are split into five parts: factor, carry and rolldown, issuer relative value, index and ETF flow, and the residual. Only the residual, written $\chi_i$ for tier $i$, counts as toxicity. The hit-ratio target is then reweighted by quality: a fill from tier $i$ counts toward the target with weight $w_i = e^{-\eta\,\chi_i}$, so a tier whose residual markouts are bad earns the desk almost no credit for winning it. (Niang writes the weight's sharpness as $\gamma$; it is $\eta$ here because $\gamma$ is the desk's inventory risk aversion.) In the Hamiltonian of §18B.1 the change is one shift of the argument:

$$
z_i\,H_i\big(p_i + \chi_i - w_i\,\xi\big),
$$

the residual toxicity added to the tier's cost and the coupon multiplied by its quality. Under a strictly increasing fill curve the dual equation has a unique root. For the logistic curve of §18.7 the quote even has a closed form,

$$
x^\star = p + \frac{1 + W_0\!\big(e^{\,\beta_0 - \beta_1 p - 1}\big)}{\beta_1},
$$

written here with §18.7's win-curve parameters and $x$ measured as the distance from the composite, where $p$ is the tier's total effective cost and $W_0$ is a function most people meet once and then forget.

> **Math, Gently.** *The Lambert W function, or how to solve the equation §18.7 iterated.* Some equations hide the unknown both outside and inside an exponential, like $w\,e^{w} = 3$. No combination of logarithms gets $w$ out, so mathematicians gave the answer a name: $W(3)$ is the number whose product with its own exponential is 3, about 1.05. It is a function like $\sqrt{\cdot}$, with a button on serious calculators and a two-line Newton iteration everywhere else. It turns up in the RFQ problem because §18.7's first-order condition, $x - p = 1/\big(\beta_1(1 - P(x))\big)$, has $x$ on the left and $x$ inside the logistic's exponential on the right. In §18.7 Kaz solved it by iterating. Lambert W solves it in one step. A tiny number: with $\beta_0 = 0$, $\beta_1 = 4$ and a total cost of $p = 0.5$ points, $e^{0 - 2 - 1} = e^{-3} \approx 0.050$, $W_0(0.050) \approx 0.048$, and the quote sits $0.5 + 1.048/4 \approx 0.76$ points from the composite, where it wins about 4.5% of the time. Check: $1/\big(4 \times (1 - 0.045)\big) \approx 0.26$, and $0.76 - 0.5 = 0.26$. The full version is in Niang (2026) and in `quote_from_p` in §18B.9.

What the quote looks like after all this is the five-term decomposition that §18.7 and the Edition 2 plan both attributed to Barzykin and Ciceri. It is Niang's:

$$
\text{quote} = \text{riskless spread} + \text{inventory skew} - \text{credit-alpha skew} + \text{residual-toxicity charge} - \text{quality hit-ratio subsidy}.
$$

The first two terms are §18B.1's. The credit-alpha skew is the desk's own view of the bond, the $\lambda^{\mathbb{P}}$ against $\lambda^{\mathbb{Q}}$ line of equation 18.9. The last two are the new ones, and each has an address. The toxicity charge goes to the tiers whose residual markouts are bad. The subsidy goes to the tiers whose fills count toward the target, and because the subsidy is weighted by $e^{-\eta\chi}$, almost none of it reaches a toxic tier. That is the answer to Ines's question in the cold open. A subsidy always lands on somebody, and the five-term quote decides on whom.

Niang's own numbers are worth having, with their label attached. On 20 synthetic euro investment-grade bonds and 300 simulated paths, at an 8% target, raw hit-ratio targeting earns $-14.32$ bp·MM a day and residual-quality targeting earns $+5.25$. The raw engine wins 7.47% of the toxic flow; the residual engine wins 0.87% of it, while winning about the same share of the carry-and-RV flow (7.29% against 7.05%). Kaz's Wednesday mistake is in the paper too, under the name "naive gross toxicity": an engine that charges gross markouts over-widens the carry-and-RV tier until its hit ratio is 1.08%. Kaz read that line twice and said nothing, which is the most Kaz has ever said.

The limits are as clear as the numbers. The synthetic markouts were generated from the same five factors that the engine later uses to decompose them, so the decomposition is perfect by construction. On a real desk the factor model is wrong a little every day, and some of what the engine calls residual is a factor it failed to name (Chapter 7-B's warning, T3 of the relative-value thread). The only critique on record, an automated referee report, raises exactly this objection; a perturbation test is reportedly planned and has not appeared. So the desk ran it the way Ines runs anything that looks too good: next to something simpler. Cartea and Sánchez-Betancourt (2025), "A Simple Strategy to Deal with Toxic Flow" (arXiv 2503.18005), derive a closed-form dealing strategy against a mix of informed and uninformed clients that sidesteps calibrating each client's parameters. "Beat the simple one first," Ines told Kaz. "If the five-factor version can't beat a strategy with no client parameters on our own log, the five factors are decoration."

Then Theo found the problem that no amount of decomposition fixes.

The hand history contains only the hands the desk won. A fill has a markout; a loss has none. And the hands the desk wins are not a random sample of the hands it was dealt. Marín Martínez, Ardanza-Trevijano and Sabio (2026), "Causal interventions in bond multi-dealer-to-client platforms" (*PLOS ONE* 21(1): e0341369), draw the RFQ as a causal graph and show where the trouble sits: winning is a collider on the path from the desk's quote $\delta$, through the rivals' quotes and the client's information asymmetry $IA$, to the price drift $\mu$ and the desk's revenue $R$,

$$
\delta \;\to\; \text{win} \;\leftarrow\; \delta_{\text{rivals}} \;\leftarrow\; IA \;\to\; \mu \;\to\; R .
$$

> **Math, Gently.** *Conditioning on a win is a collider.* A collider is an event with two independent causes. Look only at the cases where the event happened and the two causes become linked, even though nothing links them in the world. The standard example is restaurants: food quality and location are unrelated across all restaurants, but among the ones that survived five years, the ones in bad locations must have great food, so among survivors the two look negatively related. Winning an RFQ has two causes: the desk's quote was aggressive, or the rivals' quotes were wide. Rivals quote wide when they smell information. So among the RFQs the desk *won*, the ones it won with a wide quote were mostly won because the rivals were wider still, and those are disproportionately the informed ones, with bad markouts. A regression of markout on quote, run on wins only, concludes that quoting wider makes markouts worse, which is backwards: quoting wider can only help the desk on any given trade. A tiny number, illustrative: if one RFQ in ten is informed, rivals widen by half a point on informed RFQs, and the desk quotes either tight or half a point wide, then the desk's wide-quote wins come almost entirely from the informed tenth, and their average markout looks much worse than its tight-quote wins, the reverse of the true effect. The fix is to model the information asymmetry instead of conditioning it away. The full version is in Marín Martínez et al. (2026).

Their data are BBVA's European government-bond RFQs: 102,437 inquiries and 5,738 hits. The probability of a hit given the quote is identified once volatility, the RFQ, the bond and the client are adjusted for. Revenue given a hit is not identified from observables at all; information asymmetry has to be modelled. Their hit models score an area under the ROC curve of 0.742 for a generative model in the Fermanian–Guéant–Pu style, 0.743 for LightGBM and 0.684 for logistic regression; the boosted trees, for all their accuracy, are not monotone in the quote, which means the model sometimes says a worse price wins more often. Client features carried no signal on that data, and cover-price features did not help. These are government bonds, not credit, and one dealer's data, so the desk took the graph and left the numbers.

One more quote, owed since Chapter 4-C, belongs here. On the Friday before the Halvorsen 8-K, Dana Rourke's desk bid for \$15mm at 2:58 with one adjustment: fifteen cents, for the possibility that the seller knew something (§4C.1). In the five terms, Dana's fifteen cents was the whole of the toxicity charge, set by instinct for a fund tier whose residual on a name in front of a lender call was worth a point or more *(illustrative)*. Her inventory skew was the one her limits implied: a \$15mm block in a single-B name, on a desk with a ten-point, two-day rule, sits on a much steeper bowl than its spread duration suggests. Her credit-alpha skew was the silence after the call, which she read and priced at nothing. And the term she never wrote down was the subsidy: the client sat in the desk's top twenty, and the quarterly ranking gave credit for showing a bid when others would not. That term was pulling her quote *up* while the other three pulled it down. The engine would not have known about the 8-K. It would have shown her that four of her five terms were pointing the same way and the fifth was being paid to a client who knew more than she did.

## 18B.3 The Cover Price Is One-Sided Data

*Builds on:* §2.3.2 (order statistics), §3.2.3 (the winner's curse with many dealers), §3.3.5 (survivorship). *Used in:* Chapter 2-B §2B.1 (the same inquiry from the client's screen), §27.4 (the RFQ log as an order state), Appendix B (the RFQ-log schema).

> **Quant-Shop Life (fictional composite): the column called cover.** *Friday, 2:15 p.m., a quiet afternoon on the desk. The desk, its log, its venues' exports and ROBO's output are invented.* The RFQ log comes from two venues, and the two exports agree on almost nothing. One stamps in New York time and one in UTC. One calls a withdrawn inquiry *cancelled* and the other calls it *not traded*. One reports the number of dealers in competition and the other reports it only when the client chose to disclose it. Theo spent the first hour of Friday afternoon on a reconciliation that did not tie by forty-one rows, which turned out to be inquiries clients pulled before the timer expired, logged by one venue and silently dropped by the other. It was the dullest hour of his month and the most useful, because the dropped rows were, by construction, the RFQs nobody traded, and Kaz's estimator was about to need every one of them. Then Theo asked ROBO for "a column `cover_px` for every RFQ." ROBO produced it. On *Done* rows it held the best rival's price, which was what Theo meant. On *Covered* rows it held the desk's own price, because when the desk is covered the desk *is* the cover. On *Traded Away* rows it was blank. Kaz's first fit read the column as "rivals' prices" and estimated the rivals partly from the desk's own quotes. ROBO had done precisely what was asked, which is the thing ROBO does.

The fix was a schema rather than a column, and it now sits in Appendix B. Every inquiry gets one row, whatever happened to it: the venue, the client tier, the side and size, the number of dealers in competition as the venue showed it, whether the desk answered, the desk's price, the composite at receipt, an outcome drawn from a fixed list, and the best rival's price only on the rows where the venue reveals it. The fixed list is the outcome taxonomy of Fermanian, Guéant and Pu (2016), "The behavior of dealers and clients on the European corporate bond market: the case of Multi-Dealer-to-Client platforms" (*Market Microstructure and Liquidity* 2(3–4)): *Done* (the desk traded), *Tied Traded Away* (the desk matched the best price and lost the tie), *Covered* (the desk was second best), *Other Traded Away* (the desk was further back) and *Not Traded* (the client traded with nobody).

"Covered," Kaz said, reading the list. "As in, we were insured?"

"As in, we came second," Theo said.

"And *Tied Traded Away* is a knot?"

"It's what happens when we tie for best and the client picks the other dealer. Usually because it likes them more."

Kaz wrote *relationship = tiebreaker* on a sticky note, which is a better definition than most.

The paper is the only public likelihood for the cover price, built on BNP Paribas's role as a reference dealer on Bloomberg FIT in 2014–15, with up to six dealers per inquiry: 209,069 client buys and 272,189 client sells after filtering. For the buys, the five outcomes counted 44,745 Done, 2,892 Tied Traded Away, 44,054 Covered, 69,716 Other Traded Away and 47,662 Not Traded. The model treats the rivals' quotes as independent draws from a distribution $F$ (density $f$) on the half-spread scale around the CBBT mid, and the client's reservation value as a draw from $G$ (density $g$). Each outcome then has its own probability. A *Done* at the desk's quote $Y$, with the best rival's price $C$ revealed as the cover, has likelihood

$$
n\,f(C)\,\big(1 - F(C)\big)^{n-1}\,\big(1 - G(Y)\big),
$$

one rival at $C$, all the others worse, and a client willing to pay $Y$. *Not Traded* has likelihood $\int^{Y} \big(1 - F(v)\big)^n g(v)\,dv$: the client's reservation value $v$ fell short of the desk's price and of every rival's. *Covered* and *Other Traded Away* contribute the probability that one rival, or more than one, beat $Y$ and the client took the best of them.

> **Math, Gently.** *The cover is the best of $n$ draws, and seeing it only when you win hides half of it.* Each rival's quote is a random draw; the cover is the best rival's draw, an order statistic (§2.3.2). On a win, the desk sees the cover. On a loss it sees, at most, that someone beat it. So the covers in the desk's file are not draws of "the best rival quote"; they are draws of "the best rival quote, given that it was worse than ours." A tiny number: two rivals whose quotes are spread evenly between 0 and 1 point from mid, and a desk that always quotes 0.4. The true average best rival quote is 1/3 of a point. The desk wins only when both rivals are worse than 0.4, and then the cover averages $0.4 + 0.6/3 = 0.6$. An estimate built from wins alone says the best rival sits at 0.6, nearly twice the truth, and concludes that rivals are lazy and winning is safe. The losses carry the other half of the distribution, and the likelihood above is how they are put back. The full version is in Fermanian, Guéant and Pu (2016), Section 3.

This is exactly what Kaz's first fit did. Estimated on the Done rows alone, the rivals' distribution came out wide, the desk's shading came out near zero, and the model announced that the desk never suffered a winner's curse. Ines read the output and laughed for the first time that week. "Every dealer who ever went broke believed that number." Refitted on the whole log, with the Covered, Traded Away and Not Traded rows supplying the other side of $F$, the rivals tightened and the shading came back. The blotter is a list of the hands the desk won. The estimator is the list of every hand it was dealt.

Two of the paper's empirical results changed the desk's model of its own competition. First, only about 40% of the dealers asked actually answer (0.400 on client buys and 0.424 on client sells), and the answer rate falls as the panel grows: $p(n)$ = 1.00, 0.655, 0.498, 0.417 and 0.351 for one to five rivals. Multiply through, $(n+1)\,p(n)$, and the expected number of answers is about two at every panel size: 2.0, 1.97, 1.99, 2.09, 2.11. Clients, the authors observe, "often wait for only two answers." Second, the client's mean reservation value sits about 1.7 half-spreads from the CBBT mid, roughly 90% of the full bid–ask spread.

A small piece of arithmetic shows why the answer rate dominates *(a toy calculation of ours on the paper's published shares; illustrative)*. From the Table 1 counts, the desk's Done share falls from 35.1% with one rival to 19.0% with five. Suppose the desk always quotes at the median of the rivals' answered quotes and the client accepts its price 70% of the time. With one rival who always answers, the desk wins half the time: $0.5 \times 0.7 = 35\%$, close to the data. If all five rivals answered every time, the desk would win $0.5^5 \times 0.7$, about 2%, nowhere near 19%. With the paper's answer rate of 0.351, each rival beats the desk only $0.351 \times 0.5$ of the time, and the Done share is $(1 - 0.1755)^5 \times 0.7 \approx 27\%$, too high now. To get down to the observed 19% the desk's quote would have to sit at about the 65th percentile of the answered rival quotes rather than the median. The rivals who do answer quote tighter when the panel is bigger.

That last sentence is the paper's partial-participation result, and it corrects a sentence in this book. Chapter 3 (§3.2.3) reports that dealer quotes "become more conservative as the number of requested dealers rises." That is what Fermanian, Guéant and Pu find in their *full-participation* model, which treats a dealer who did not answer as one who quoted badly; the authors attribute the widening to non-answering. In their preferred partial-participation model, the mean answered quote *tightens* with $n$, from 1.36 to 0.647 half-spreads on the buy side. Competition among the dealers who answer gets stronger, and the crowd of dealers who do not answer is what makes the full-participation model look conservative. §3.2.3 is corrected in this edition.

The client sees the same inquiry from the other side of the screen, with every response visible and none of the desk's inventory, and Chapter 2-B (§2B.1, and the survivor problem in §2B.1.3) reads it from there. Jacobsen, Venkataraman and Xu (2025), "Illiquidity Meets Intelligence: AI-Driven Price Discovery in Corporate Bonds" (SMU working paper, with data supplied by MarketAxess, not peer-reviewed), add a reason to keep every row. When an inquiry that did not trade falls between two trades, MarketAxess's CP+ composite beats the last trade by 1.4 to 5.0 times as much as it otherwise does. An RFQ that nobody filled still carries price information. Theo's forty-one dropped rows had been information all along.
