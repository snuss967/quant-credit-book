# Chapter 18: OTC Credit Microstructure & the Market Maker's Equations

*What is invented in this scene: Halvorsen Packaging, its notes, its lender call, the 12:07 headline, the client and every quote are fictional, and so is the desk. The grey box, the timer and the tick size are real.*

*11:52 a.m.* The RFQ arrived the way bad news always arrives on a credit desk: politely, in a grey box, with a countdown timer. *Client sells \$8mm Halvorsen Packaging 7.25% Senior Notes due 2029 (senior unsecured, B3/B−), disclosed, five dealers in competition, three minutes to respond.* The composite said 91.25.

For fifty seconds nobody spoke, which on a market-making desk is a long silence. Theo spent it the way he had spent every spare minute of six years at PJT, on the document. He had the indenture open on his second monitor, because he always had a credit document open on his second monitor, and he scrolled to the clause he had flagged on Monday, the one a restructuring banker reads first and a market maker reads last. *Nothing in this Indenture shall restrict the Issuer or any of its Affiliates from purchasing Notes in open market purchases, privately negotiated transactions or otherwise, at any price.* No cap. No pro rata sharing. No promise to offer every holder the same price. A company with that sentence and a reason to shrink its debt can buy its own bonds at 85 from whoever is nervous enough to sell them at 85.

On his third monitor sat a window the desk had stopped teasing him about: the Priming Risk Score he had been building in the evenings, the 13-week cash flow model in its newest body (Chapter 13). On Monday it had read 0.31 for Halvorsen *(illustrative)*. Overnight the text pipeline had finished last Thursday's earnings-call transcript and tripped on one sentence from the CFO, who was "committed to a leverage target of four times, using all tools available to us." The score now read 0.44. Theo had posted the number in the desk chat at 7:40 a.m. Nobody had replied, because at 7:40 a.m. nobody on a market-making desk replies to anything that is not a price.

At the fifty-second mark Kaz's auto-quoter filled in a bid of 90.875. "Avellaneda–Stoikov," Kaz said, with the calm of someone whose model has never been subpoenaed. "We're long three million already. Twenty-day realized vol, half-spread from the fitted win curve, rounded to the nearest eighth, because this market is a medieval guild."

"Their lender call is at noon," Theo said. "And the indenture lets them buy back notes below par through open market purchases, with no cap. Last week the CFO put 'leverage target' and 'all tools' in the same sentence. If they announce a discounted repurchase at noon, today's sellers are the people who were told first."

"Is an open market purchase like open outcry?" Kaz asked. "Do they have to shout?"

"They have to pay less than you," Theo said.

"So the seller may know something," said Ines, without looking up. "What's the pot, what are the odds, and who at this table knows more than you?"

"The client," Theo said. "Maybe four of the five dealers. Definitely not the auto-quoter."

From across the row, Mags did not look up either. "Back in my day we'd just not pick up the phone."

The timer said 1:58. Ines did what she did with every new hire at least once, whenever the clock allowed it and sometimes when it did not. She took an index card from the stack beside her keyboard, wrote on it, and slid it across. *You are the fifth dealer. Write your bid, your size, and the one fact that would change it.* Theo wrote *90, all eight, the noon call*, and slid it back. She tucked it under her keyboard without reading it. If you are reading this with a pen, write your own card now, before the cover comes back.

Ines dragged the bid to 90.25 and sent it with eleven seconds on the clock. It did not trade; someone covered at 90.50. Kaz's face did the small thing faces do when a model has just been overruled by a human and the human has just lost.

*12:00.* Theo had the public dial-in on speaker. The CFO's voice had the even cadence of a script that had been through two rounds of legal review. The company was "evaluating a range of balance-sheet initiatives," had "engaged advisers to assist," and would "consider all options consistent with the leverage target." Nobody said the word *discount*. Nobody needed to.

*12:07.* A headline crossed the news terminal in capitals: HALVORSEN EXPLORING DISCOUNTED DEBT REPURCHASES; ENGAGES ADVISERS. Two dealer runs flipped from offers to "no offer." The composite stopped updating, which is what a composite does when nobody it averages is willing to be averaged.

*12:12.* A print crossed the tape at 86, size shown only as `1MM+`, because the tape caps high-yield size at a million (§18.8). The chat windows filled with the noise a market makes when it finds out who the patsy was. On \$8mm, the winner had just bought a \$360,000 lesson *(illustrative)*.

Ines slid Theo's card out from under her keyboard and read it for the first time. "Right fact," she said. "The number was a quarter too scared. Today that cost nothing. On a quiet Tuesday it costs you the client." If your own card was above 90.50, you won the bonds, and the chat is about you.

Kaz stared at the screen. "The model was right about the inventory."

"The model was right about the part you asked it about," Ines said. "A quote is four things glued together. You priced one."

That is the question this chapter answers: *what is the right bid, and how much of it is fear, how much greed, how much suspicion, and how much the price of being asked again tomorrow?*

By the end of this chapter you will be able to look at any bid and name the numbers inside it. Harris's taxonomy and Roll's trick tell you who is selling and what the spread is when nobody will show you one; Kyle and Glosten–Milgrom price the suspicion; Avellaneda–Stoikov (AS), derived from the Hamilton–Jacobi–Bellman (HJB) equation, the Guéant–Lehalle–Fernandez-Tapia (GLFT) inventory-bounded model solved as a linear ODE system, and their jump-to-default extension price the fear and the greed; a fitted RFQ win curve and a hit-ratio multiplier price the franchise. TRACE and BWICs are where the data comes from and where the auction turns inside out, a first-price auction with a leaky list. The Finder table at the top of the Desk Debrief (§18.10) maps each tool to its equation, its box, its scene and its listing, and every engine ends in a spec that leaves ROBO nothing to guess.
By the end of this chapter you will be able to: map Harris's trader taxonomy onto the credit ecosystem and say who is a forced seller to whom; estimate an effective spread from TRACE prints with Roll's trick, and know when the estimator is lying; derive Kyle's $\lambda$ and estimate it from markouts; derive the Avellaneda–Stoikov (AS) quotes from the Hamilton–Jacobi–Bellman (HJB) equation without skipping steps; solve the Guéant–Lehalle–Fernandez-Tapia (GLFT) inventory-bounded problem as a linear ODE system; extend both to jump-to-default; fit an RFQ win curve and price a hit-ratio target; decode a TRACE file into features; and model a BWIC as a first-price auction with a leaky list. You will also be able to hand all of it to ROBO in a spec that leaves it nothing to guess.

## 18.1 Harris's Zoo, Relabeled for Credit

A restructuring banker learns to ask *who holds the paper and what are they forced to do*. A market maker asks the same question, but at the speed of a timer and about everyone at once. Larry Harris's *Trading and Exchanges* (2003), the standard practitioner text on market microstructure, sorts traders by *why* they trade. **Utilitarian traders** trade for some reason other than profiting from the trade itself: hedging, investing cash, meeting a redemption, or obeying a regulator. **Profit-motivated traders** trade because they think the price is wrong or about to move. These include the *informed*, who know something about value; *order anticipators*, who know something about other people's orders; and *bluffers*, who want you to believe they know something. Between them stand the **dealers**, who sell immediacy, and the **arbitrageurs**, who sell convergence. Harris adds four dimensions of liquidity: **immediacy** (how fast you can trade), **width** (the cost of a round trip), **depth** (how much size you can do at that cost), and **resiliency** (how fast the price recovers after you trade).

Relabeled for the credit ecosystem of Chapter 1, the zoo looks like this.

| Harris type | Credit population (2026) | What they want | What they cost the dealer |
| :--- | :--- | :--- | :--- |
| Utilitarian, uninformed | Insurers selling fallen angels for capital reasons; index funds at month-end; CLOs curing CCC buckets; LDI-linked holders meeting margin calls | Immediacy at a fair price, predictably timed | Little in expectation. This is the dealer's bread. |
| Utilitarian, arbitrage | ETF authorized participants (Chapter 20); portfolio-trade desks (Chapter 19); CDS–bond basis traders | Convergence of a basket to its NAV | Basket risk and the mystery-box problem, but rarely issuer-level information |
| Profit-motivated, mostly uninformed about issuers | Systematic factor pods trading momentum, value, and carry baskets (Chapters 9–11) | Factor exposure | Factor beta, which the dealer can hedge. IDO or it didn't happen: their markouts are mostly not toxic once you strip the factor. |
| Profit-motivated, informed | Distressed and crossover funds; LMT participants; anyone who has actually read the indenture | To trade before the information is in the price | The residual markout, which is the whole adverse-selection problem |
| Order anticipators | Anyone who has seen a BWIC list, a leaked run, or a large RFQ shopped to too many dealers (§18.9) | To trade ahead of known flow | Pre-auction drift, paid by the seller |
| Dealers | Bank dealers; non-bank liquidity providers, about 10% of credit market-making revenue in 2024 *(approx.; industry dossier)* | Spread, and future flow | Competition. Non-banks bring a different $\gamma$ and a different $k$ (§18.4). |

Theo spent part of the afternoon after the 86 print rereading that table with a question he had never needed at PJT: of everyone who could have sent the Halvorsen RFQ, whom should the desk have been glad to see? Ines found him at it, took a pencil, and walked him down the printout one row and one real seller at a time.

"Start at the top," she said, tapping *utilitarian, uninformed*. "The sellers we're paid to love. In the first week of October 2022, British pension funds running liability-driven strategies sold CLO tranches in size, because their gilt hedges were calling for cash. Not one of them had a view on a single loan inside those CLOs. That week gets its own scene in §18.9. What did they want from a dealer?"

"Speed," Theo said.

"Harris calls it immediacy. In our engine it's the *win probability* inside the timer: the chance we answer, at a price they'll take, before the clock runs out. And they wanted it in size, which is Harris's *depth*. Depth is why the reservation price has to move with the block, not with one more lot. A dealer who prices the fortieth million like the first is about to own forty million at the first million's price."

She moved the pencil to the CLOs in the same row. "Same row, different calendar. A CLO whose loan has just been cut to CCC, with a thin overcollateralization cushion, sells. Elkamhi and Nozawa (2022, *Journal of Financial Economics*) found that CLOs with little OC slack are significantly more likely to sell a loan downgraded to CCC within about three months, that the price falls and then comes back, and that because CLOs own overlapping portfolios the constraint binds for many of them in the same weeks. Chapter 21 owns the mechanics. The coming back is Harris's *resiliency*, how fast the price recovers after someone trades. On an exchange the spring is the order book refilling, which is the spring Paleologo describes for equities (Paleologo p.152–153)." She tapped her own monitor, where the desk's positions lived. "Here the spring is our inventory. The price relaxes when we find the other side, and not one minute before."

"And the bottom row?" Theo asked. "The informed."

"The row nobody admits to sitting in." She thought about it. "The cleanest public example I know isn't a seller at all. In March 2024 Altice France held an investor call that knocked its debt down hard, and by that evening a group of creditors had formed a cooperation agreement (IFR; §18.6.3 tells the day). Nobody in that group needed a secret. They had read the capital structure before the call and they read the call faster than the market did. That is what *informed* means on this table most days: someone who did the reading you didn't. Today it was a client with an indenture and a calendar."

"So width is where they hurt us."

"Width is what a round trip costs, and in our engine it's the *reservation spread* plus the markup. The bottom row is the reason a third charge sits on top of both." She put the pencil down. "Four dimensions, four things the engine has to estimate before it answers anything. The rest of the chapter builds a model for each."

> **Desk Myth vs. Desk Reality.** *Myth:* "The bid–ask spread is the dealer's profit." *Reality:* The quoted spread is four charges, and only one of them is profit. **Fear** is the inventory risk premium, $\gamma\sigma^2(T-t)$ in §18.4. **Greed** is the markup a dealer with some pricing power can charge, $\tfrac{2}{\gamma}\ln(1+\gamma/k)$. **Suspicion** is the expected adverse markout, $2\pi\sigma_V$ in Glosten–Milgrom (§18.3). **Franchise** is a *negative* charge: the subsidy a dealer pays to keep winning enough RFQs to stay on the client's list (§18.7). Realized profit is the spread minus the markout. On a toxic RFQ it is negative, which is why "the dealer made the spread" is something only people who have never been a dealer say.

> **[SOURCE EXTRACTION]** *Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.19:* "the bond market is structured around a Request for Quotation (RFQ) process that has hardly changed for decades. Corporate bond bid/ask prices are indicated by dealer runs that are not firm and actionable"
>
> **Annotation.** Our analysis: the Man authors are right about the *protocol* and, by 2026, wrong about the *responder*. The disclosed RFQ is still a sealed-bid auction among a handful of dealers. What changed between 2022 and 2026 is who answers it. Trumid reports that most eligible RFQ line items now execute with no human touch, and Tradeweb says AiEX handles a large and rising share of its institutional trades (figures and sources in the Trend Watch, §18.7). The runs are still "not firm and actionable", which is why §18.2 has to recover spreads from prints rather than quotes. The same page also complains about "if filled" trades. That complaint is the reason the modern engine treats fill probability as a modeled variable rather than as noise: in §18.7 the win curve $P(x)$ is a first-class input to the quote, not an afterthought in the backtest.

## 18.2 Roll's Trick: Seeing the Spread When No One Will Show You One

Equities show you a spread. Credit shows you a *print*, fifteen minutes late, with the size capped and the side sometimes ambiguous, and asks you to infer the spread from it, like a sommelier asked to name the vintage from the cork. Roll (1984), "A Simple Implicit Measure of the Effective Bid-Ask Spread in an Efficient Market" (*Journal of Finance* 39(4)), found that the spread leaves a fingerprint in the *autocovariance* of price changes. A trade at the bid tends to be followed by a trade at the ask, so prices bounce, and the bounce is negatively autocorrelated.

> **Math, Gently.** *Covariance, and a ball between two walls.* Picture a ball bouncing between two walls 0.20 points apart: the bid wall at 90.90 and the ask wall at 91.10, with the true mid sitting still at 91.00 between them. Each print lands on one wall or the other, at random, like a coin toss. Now watch the *changes* between prints. A change of +0.20 happens only when a bid print is followed by an ask print. The ball is then at the ask wall, so the next change is either 0 (another ask) or −0.20 (back to the bid). An up-tick is followed by a down-tick or by nothing, never by another up-tick. *Covariance* is the statistician's name for this habit: multiply each change by the next one and average the products (the changes average zero here, so nothing has to be subtracted first). Neighbours that move together give a positive average; neighbours that undo each other, as these do, give a negative one. The whole calculation fits in the margin. Half the changes are 0, a quarter are +0.20 and a quarter are −0.20. After an up-tick, the product with the next change is 0 or −0.04, equally likely, so −0.02 on average; the same after a down-tick; after a flat change it is 0. The average product is $\tfrac14(-0.02) + \tfrac14(-0.02) = -0.01$, which is $-S^2/4$ with $S = 0.20$. Run it backwards and $S = 2\sqrt{0.01} = 0.20$: the spread, recovered from prints alone, without anyone showing you a quote. The failure is the useful part. When changes start following each other in one direction, the covariance comes out *positive*, the formula asks for the square root of a negative number, and that NaN is the most useful thing Roll ever tells you (Figure 18.1, right panel). The algebra, and the two ways credit breaks it, come next.

### 18.2.1 Derivation

Let $m_t$ be the efficient mid, a random walk $m_t = m_{t-1} + \varepsilon_t$ with $\varepsilon_t$ i.i.d., mean zero, variance $\sigma_\varepsilon^2$. Let $I_t \in \{-1,+1\}$ indicate whether print $t$ was a customer sell (at the bid) or a customer buy (at the ask). Let $c = S/2$ be the effective half-spread in price points. The print is

$$
p_t = m_t + c\,I_t .
$$

Then $\Delta p_t = \varepsilon_t + c\,(I_t - I_{t-1})$. Assume first, as Roll did, that $I_t$ is i.i.d. with $\mathbb{P}(I_t = 1) = \tfrac12$, independent of $\varepsilon$. Then $\text{Var}(I_t) = 1$ and all cross-covariances vanish, so

$$
\text{Cov}(\Delta p_t, \Delta p_{t+1}) = c^2\,\text{Cov}(I_t - I_{t-1},\, I_{t+1} - I_t) = -c^2\,\text{Var}(I_t) = -\frac{S^2}{4}.
$$

Solving for the spread gives Roll's estimator:

$$
\widehat{S}^{\text{Roll}} = 2\sqrt{-\widehat{\text{Cov}}(\Delta p_t, \Delta p_{t+1})}.
$$

Bao, Pan & Wang (2011), "The Illiquidity of Corporate Bonds" (*Journal of Finance* 66(3)), use the same covariance directly as an illiquidity measure, $\gamma^{\text{BPW}} = -\text{Cov}(\Delta p_t,\Delta p_{t+1})$ computed on TRACE prices. They find bond illiquidity far larger than quoted spreads suggest, and priced in the cross-section. (Their $\gamma$ is not our risk aversion $\gamma$, hence the superscript.)

Now break the assumption the way credit breaks it. Large customer orders are *split*: a \$25mm sell goes out as five \$5mm RFQs over an afternoon. Model the trade signs as a symmetric two-state Markov chain with lag-one autocorrelation $\rho \in [0,1)$, so that $\text{Cov}(I_t, I_{t+j}) = \rho^{|j|}$. Expanding term by term,

$$
\text{Cov}(I_t - I_{t-1},\, I_{t+1} - I_t) = \rho - 1 - \rho^2 + \rho = -(1-\rho)^2,
$$

so $\text{Cov}(\Delta p_t,\Delta p_{t+1}) = -c^2(1-\rho)^2$ and

$$
\widehat{S}^{\text{Roll}} \;\to\; S\,(1-\rho).
$$

Order splitting makes Roll *underestimate* the spread by the factor $(1-\rho)$. Add informed flow that moves the mid in the direction of the trade over several prints, so that the $\varepsilon_t$ are positively autocorrelated, and the covariance can turn positive. The square root then has no real solution. That is not a numerical accident. It is the estimator telling you that the bounce has been overwhelmed by momentum, which is information in its own right (§18.3). Dynkin's team makes the same point from the other side when it uses return autocorrelation as an illiquidity proxy: investors split trades, which produces positive autocorrelation, and stale prices do the same (Dynkin p.771). Figure 18.1 shows both failures in simulation.

![Figure 18.1: Roll's estimate shrinks as order splitting rises (left, the estimate is S(1 − ρ)) and stops returning a spread at all once informed drift makes the covariance positive (right, beyond φ ≈ 0.62 for these inputs). Illustrative: simulated from the model in §18.2.1 and Listing 18.1 with S = 0.20 points, mid-price innovation volatility 0.10 points, and 200,000 prints per point (mean of 5 runs).](assets/figures/ch18_roll_splitting_momentum.png)

> **[SOURCE EXTRACTION]** *Ben_Dor_Quantitative_Credit_Portfolio_Management p.120:* "for most bonds the time between a broker-dealer buy and sell transaction for a given CUSIP can be very long, so it is difficult to calculate an accurate bid-ask spread using TRACE."
>
> **Annotation.** Our analysis: this is the practical objection to Roll in credit, and it bites harder than it looks. Roll's algebra assumes the mid barely moves between consecutive prints, so that $\sigma_\varepsilon^2$ is small next to $c^2$. When a dealer's round trip spans three days, the mid diffuses between prints and the bounce is buried. The covariance estimate is unbiased in theory and useless in practice, because its standard error scales with $\text{Var}(\Delta p)$, which is now dominated by $\sigma_\varepsilon^2$. Ben Dor's team responded by building Liquidity Cost Scores from trader *indications* rather than prints. The 2026 desk has a third option the 2010 authors lacked: dense electronic RFQ logs, its own and the platforms', where both sides of the market are observed within seconds. Use Roll on TRACE as a cross-check and a stress indicator, not as your spread.

> **[SOURCE EXTRACTION]** *Dynkin_Systematic_Investing_in_Credit p.702:* LCS "measures the cost of an immediate round-trip transaction of a typical institutional size and is expressed as a percentage of a bond price"
>
> **Annotation.** Our analysis: notice the three qualifiers, *immediate*, *round-trip*, and *typical institutional size*. Roll measures none of them exactly: it measures the average bounce across whatever sizes printed, with no immediacy constraint. For spread-quoted bonds, LCS is the bid–offer spread times spread duration. Ben Dor p.123 then multiplies the indications of non-benchmark bonds by an adjustment factor between 1.50 and 1.83, which is the industry admitting in writing that dealer indications are tighter than dealer markets. The modern desk uses LCS-type composites as the prior and its own RFQ fills as the likelihood.

Kaz met that NaN on a Friday replay. Ines had cut the tape on Altice France's opco secured notes in the week before the company's March 2024 results call (the whole day is §18.6.3's long scene), and Kaz ran Roll on each of the last five sessions. Two came back with spreads. Three in a row came back NaN *(the desk's fictional run)*.

"Is it broken?" Theo asked.

"It's telling you the bounce lost," Ines said. "Splitting a big order only shrinks Roll's number. To flip the sign you need the sells to keep coming and the price to keep following them. Who sells a first-lien note in pieces for a week?"

Theo answered the way he would have at PJT. "Someone who read the public numbers and decided not to wait for the call. Or a CLO with a ratings problem. Either way, someone who isn't coming back to buy."

"Either way, a feature," Kaz said, and wrote it down, which for Kaz is the highest compliment: *sign of the Roll covariance, rolling five sessions.* It became a column in the TRACE decoder of §18.8. "A NaN is a reading," Kaz added. "Not an error."

> **Ways This Blows Up.** (1) *Taking the absolute value.* When the sample covariance is positive, someone always writes `2*sqrt(abs(cov))`. That reports a spread when the data are reporting momentum. Return NaN and log the sign. (2) *Mixing sizes.* Odd lots pay more than blocks (Edwards, Harris & Piwowar 2007), and "5MM+" capped prints are a different market from \$50k retail prints. Estimate by size bucket. (3) *Interdealer double counting.* Both dealers report an interdealer trade. Leave both legs in and you manufacture a bounce of exactly zero width between two identical prices, which biases the covariance toward zero (§18.8). (4) *Stale prints.* Prints days apart measure diffusion, not bounce. Cap the gap between consecutive prints or weight by it.

### Specification for AI Implementation (Roll estimator)

**The Spec You Hand the Robot.** *What ROBO built from the vague version ("estimate the bid–ask spread from TRACE"):* it averaged (ask print − bid print) over all prints on the same day, on a bond that traded twice a week, and reported a spread of zero for every day with one print. The precise spec: input a time-ordered vector of cleaned prices (points per 100 par) for one bond and one size bucket. Output `(spread, autocov)` in points. Require at least `min_obs` price changes. Return `NaN` when the autocovariance is non-negative, and never take an absolute value. Sanity checks: recover a known spread on simulated Roll data, recover $S(1-\rho)$ under order splitting, and return `NaN` under momentum.

Somewhere in the book is a B3 bond that prints twice a week, and nobody will tell you what it costs to get out of it. The derivation says the answer is hiding in the way consecutive prices bounce, but a derivation is not a nightly job. A desk that holds a few thousand bonds needs a spread estimate for each one, in each size bucket, before the morning risk meeting, and it needs the estimate to say "I don't know" in the same way every time, not only when the analyst on call happens to notice. That is the case for putting Roll's trick into a function and surrounding the function with tests that can fail.

Listing 18.1 has two working parts. `roll_spread` takes a time-ordered vector of prices in points per 100 par, discards anything that is not finite, and declines to answer unless at least `min_obs + 2` prices survive, which leaves `min_obs` pairs of consecutive price changes. It differences the prices, takes the sample covariance between each change and the one before it, and returns the pair `(spread, autocov)`. When the covariance is negative, the spread is twice the square root of its magnitude, which is the estimator derived above. When the covariance is zero or positive, the spread is `NaN` and the covariance comes back anyway, so the caller can log the sign. The function never takes an absolute value, because a positive covariance is the data reporting momentum, and a spread built from it would be fiction with a confident decimal point.

The second part, `simulate_roll`, is the test bench. It builds prices as a random-walk mid plus half a spread times a trade sign. The signs come from a two-state Markov chain whose persistence `rho` stands for order splitting (`rho = 0` is Roll's original i.i.d. world), and the mid increments pass through an AR(1) filter with coefficient `phi_mid`, so a positive value plays the informed trader who keeps pushing the mid in the direction of the flow. Three assertions pin the estimator to the algebra. With i.i.d. signs, it recovers a 0.50-point spread to within 0.02. With `rho` of 0.6, it returns about 0.20, which is $S(1-\rho)$. With strong drift, it returns `NaN` and a positive covariance. The last line defines the Bao–Pan–Wang illiquidity measure as minus the autocovariance, in points squared.

Use it on TRACE prints for one bond in one size bucket, as a cross-check and a stress indicator rather than as the spread you quote from. The edge case that bites is that the function sees prices and nothing else. It has no timestamps, so a print from Monday and a print from Thursday are treated as neighbours, and dropping a non-finite price silently glues the series across the hole. The mid has diffused in the meantime, the bounce is buried under $\sigma_\varepsilon^2$, and the function returns a number that is mostly noise. The caller must bucket by size and cap the gap before the vector arrives. Remember too that a sample covariance is noisy: a single `NaN` is not proof of informed flow, and a run of them across many bonds on the same day says more than any one.

*The full listing is [Listing 18.1 in Appendix F](#code-18-1).*

The third check is worth working by hand. With $S = 0.10$ and $\rho = 0.6$, the bounce contributes $-c^2(1-\rho)^2 = -0.0025 \times 0.16 = -0.0004$ to the autocovariance. The mid increments have stationary variance $0.01/(1-0.16) \approx 0.0119$ and lag-one autocovariance $0.4 \times 0.0119 \approx 0.0048$. Momentum wins by a factor of twelve, and a well-behaved estimator says so by refusing to answer.

> **Trend Watch: the great spread compression, and its stress reversals (2004–2026).** *What changed:* TRACE dissemination was phased in from 2002 to 2005. Edwards, Harris & Piwowar (2007, *Journal of Finance* 62(3)) and Goldstein, Hotchkiss & Sirri (2007, *Review of Financial Studies* 20(2)) find that transparency helped liquidity, though not uniformly: the first reports lower trading costs once TRACE disseminates prices, and the second a neutral-to-positive effect, with spreads narrowing except for very large trades and very infrequently traded bonds (magnitudes vary by sample and bond type; see the papers). *How big, then:* Chen, Lesmond & Wei (2007) estimate bid–ask spreads of about 25 bp for AAA bonds and 180 bp for CCC; Man's 2022 authors note that spreads are "markedly tighter in the current market" (Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.20). *The stress reversal:* the same Man page charts a 20-day average HY bid–ask (Bloomberg data, 1 July 2017 to 2 February 2021) that gaps out in February–March 2020 and then normalizes. Kargar et al. (2021, *Review of Financial Studies*) estimate that at the March 2020 peak, customers' willingness to pay for immediacy rose by roughly 200 bp per dollar traded, and flow shifted from risky-principal to slower agency trades. *2026:* MarketAxess data reported by The DESK (2026-10-01) show the median EUR IG bid–ask down from 0.0879 to 0.0673 price % of par (−23.5%), comparing the 34 weeks to 2026-08-23 with the same weeks of 2025. In the March 2026 stress, however, EUR IG bid–ask hit 64% above its January average, and recovery took 4 weeks (EUR IG), 6 (US HY), 8 (US IG), 13 (EUR HY), and 14 (EM, which then widened again and has been above its January level in 21 of the 22 weeks since the peak). *What it means for the desk:* the median spread is a fair-weather number. A cost model calibrated on a calm window, by Roll or anything else, underprices exactly the trades you most need to price. Make the spread estimator regime-conditional, and carry the stress multiplier as a parameter.

## 18.3 Who Knows More Than You: Glosten–Milgrom Recalled, Kyle Derived

Roll measured the spread and assumed nobody knew anything. The next two models put knowledge back in. Glosten–Milgrom asks *whether* the person on the other side knows more than you. Kyle asks *how much* their size tells you. In an RFQ market you get to see both the side and the size before you quote, which is a gift Kyle's market maker never received, and also a trap, because the client knows you are looking.

### 18.3.1 Glosten–Milgrom in one line

Chapter 3 derived the RFQ version (§3.2.1), and its whole content fits in one sentence: the bid is the average value of the bond *given that someone chose to sell it to you*. Let the bond's value be $V = m \pm \sigma_V$ with equal probability, and let a fraction $\pi$ of RFQs come from clients who know which. A zero-profit dealer sets each quote to the conditional expectation of value given the side of the trade:

$$
p^{b} = \mathbb{E}^{\mathbb{P}}[V \mid \text{client sells}] = m - \pi\sigma_V, \qquad p^{a} = m + \pi\sigma_V .
$$

The suspicion spread is $2\pi\sigma_V$. With $\pi = 0.2$ and $\sigma_V = 2$ points it is 0.8 points, charged before the dealer owns a single bond. It is the price of not knowing which hand you are facing, and it exists even for a dealer with zero inventory and zero risk aversion. Remember that fact for §18.5, where dealer inventory goes to zero and the spread does not.

### 18.3.2 Kyle (1985), derived

Kyle's market maker does not see individual orders. It sees only the total order flow. One informed trader knows the liquidation value $v \sim \mathcal{N}(p_0, \Sigma_0)$, with $\sigma_v = \sqrt{\Sigma_0}$. Noise traders submit $u \sim \mathcal{N}(0,\sigma_u^2)$, independent of $v$. The insider submits $x$, the market maker sees $y = x + u$ and sets a price $p$ equal to $\mathbb{E}[v \mid y]$, and the insider maximizes expected profit $\mathbb{E}[(v - p)\,x \mid v]$.

> **Math, Gently.** *The best guess is a straight line.* Kyle's market maker sees one number, the total order flow $y$, and has to guess the value $v$ from it. Picture a scatter with one dot per day: order flow along the bottom, the value revealed later up the side. The dots slope upward, because the insider's buying is in there somewhere, but they are smeared sideways by noise traders who buy and sell for reasons of their own. The straight line that makes the squared misses smallest has slope $\text{Cov}(v,y)/\text{Var}(y)$: how much value and flow move together, divided by how much flow moves on its own. That is the regression slope of Chapter 1's box (§1.4), and when $v$ and $y$ are both normal it is the best guess of any shape, not merely the best line. Kyle's $\lambda^{K}$ is that slope. A number for the margin: if the value is uncertain by $\sigma_v = 2$ points and noise flow by $\sigma_u$ = \$5mm, the derivation below lands on $\lambda^{K} = \sigma_v/(2\sigma_u) = 0.2$ points per \$mm, so a \$10mm buy moves the price 2 points. The surprise comes at the end of the derivation: an insider who knows the line trades just hard enough that the market learns exactly half of what the insider knew.

*Notation.* The book reserves $\lambda$ for default intensity. Kyle's price-impact slope is therefore $\lambda^{K}$.

Guess linear strategies: $x = \beta(v - p_0)$ and $p = p_0 + \lambda^{K} y$.

*Insider's problem.* Given $v$, the insider chooses $x$ to maximize $\mathbb{E}[x(v - p_0 - \lambda^{K}(x + u))] = x(v - p_0) - \lambda^{K}x^2$. The first-order condition gives

$$
x = \frac{v - p_0}{2\lambda^{K}} \quad\Longrightarrow\quad \beta = \frac{1}{2\lambda^{K}} .
$$

*Market maker's problem.* Projection of $v$ on $y$ gives

$$
\lambda^{K} = \frac{\text{Cov}(v, y)}{\text{Var}(y)} = \frac{\beta\Sigma_0}{\beta^2\Sigma_0 + \sigma_u^2}.
$$

*Fixed point.* Substitute $\beta = 1/(2\lambda^{K})$:

$$
\lambda^{K}\left(\frac{\Sigma_0}{4(\lambda^{K})^2} + \sigma_u^2\right) = \frac{\Sigma_0}{2\lambda^{K}}
\;\Longrightarrow\; \lambda^{K}\sigma_u^2 = \frac{\Sigma_0}{4\lambda^{K}}
\;\Longrightarrow\; \lambda^{K} = \frac{\sigma_v}{2\sigma_u}, \qquad \beta = \frac{\sigma_u}{\sigma_v}.
$$

Market depth is $1/\lambda^{K}$: the flow needed to move the price one point. The posterior variance is $\text{Var}(v \mid y) = \Sigma_0/2$, so the trade reveals exactly half of the insider's information. The insider earns $\mathbb{E}[x(v-p)] = \tfrac12\sigma_v\sigma_u$, which the noise traders pay, while the market maker breaks even. The insider scales trading to the amount of camouflage: double the noise and the insider trades twice as much, at the same impact per unit of private information. That is why informed credit flow loves month-end and index rebalance days.

### 18.3.3 Translating Kyle to the RFQ

The morning after the 86 print, Theo asked Ines whether the desk could have known. She took a napkin from the coffee tray and drew Kyle's market on it: a box marked *insider*, a cloud marked *noise*, two arrows into a box marked *us*. Then she crossed out the cloud.

"Kyle's market maker sees the total," she said. "We see the client: name, side and size, every time, on a disclosed RFQ. So what Kyle hides in $u$ isn't noise to us. It's a list of people, and every one of them has a history." She wrote $\pi_c$ beside the crossed-out cloud. "Glosten–Milgrom's $\pi$, one per client tier, estimated from that tier's hand history. Telling noise from information stops being an equilibrium and becomes a classification problem. The name is the tell."

"Kyle also has $v$," Theo said. "The liquidation value. We never see that."

"We see where the bond went." She drew a line from the trade to a dot a few days to the right. "The $h$-day markout of a trade is the change in the bond's mid from the trade time to $h$ days later. But first you strip the rates move and whatever the factor model of Chapter 9 said the bond should have done. If all of high yield sold off on Tuesday, the client didn't know anything about Halvorsen. They knew it was Tuesday. A markout that is factor beta is not information about the issuer."

"IDO or it didn't happen," Theo said.

"So your $v$ is a future IDO-adjusted mid, and reading the hand history is a regression." She wrote it along the bottom of the napkin, markouts on signed size scaled by average daily volume, and Kaz, passing with a coffee, corrected a subscript:

$$
\text{MO}_{i,h} = a_h + \lambda^{K}_{h}\,\frac{y_i}{\text{ADV}_i} + \mathbf{b}_h^{\top}\mathbf{z}_i + e_{i,h},
$$

where $y_i > 0$ is a customer buy and $\mathbf{z}_i$ holds controls (rating, age, ETF flow, time of day), run at $h \in \{1, 5, 20\}$ days. "Measure from the *pre-trade* mid and the slope is the information content, $\lambda^{K}$," Ines said. "Measure from the *trade price* and an efficient dealer sees a slope of zero. If it's positive, the street under-reacted to the flow and the bond *drifts* after informed trades. If it's negative, the street over-reacted, or charged for inventory, and the price *bounces back*." Theo folded the napkin into his notebook, next to the USB stick, and asked for the Halvorsen seller's tier.

This is momentum and reversal at the microstructure scale, and it is the same fork Chapter 10 meets at monthly horizons. Post-RFQ drift is momentum conditional on informed flow. Roll's bounce is reversal conditional on uninformed flow. The desk's job is to tell them apart in three seconds.

Guo, Lehalle & Xu (2021), *Transaction Cost Analytics for Corporate Bonds* (arXiv 1903.09140), estimate exactly this kind of curve on Enhanced TRACE. The transient impact jumps at the trade and then decays toward a permanent level. In the language of this chapter, the jump is the dealer's suspicion and inventory charge, the decay is Harris's resiliency, and the permanent level is Kyle's information. Their headline finding is an *asymmetry* between customer-buy and customer-sell impact, which a symmetric $\lambda^{K}$ cannot capture, so the desk estimates $\lambda^{K}_{\text{buy}}$ and $\lambda^{K}_{\text{sell}}$ separately.

> **Poker Table.** Ines draws it on a napkin. "The number of dealers in comp is the number of players. The size is the bet. The client's name is the tell. And the cover, the second-best price you only learn after you lose, is the hand you didn't get to see." Winning an RFQ against four other dealers means you were the most optimistic of five people looking at the same cards. "If you win every hand at a five-handed table," she says, "you aren't good. You are the one paying for everyone's information." Hendershott & Madhavan (2015, *Journal of Finance* 70(1)) find that electronic auctions are used mainly for smaller, more liquid, less information-sensitive trades, while larger tickets go to voice, where fewer players see the cards. Fermanian, Guéant & Pu (2017, arXiv 1511.07773) model one European dealer's multi-dealer-to-client RFQ data and find that dealers quote more conservatively as the number of requested dealers rises. That is the winner's curse, priced in at the table (§18.9 does the arithmetic).

### Specification for AI Implementation (Kyle estimator)

Input: arrays of markouts (points, IDO-adjusted, horizon $h$ stated in the column name) and signed flow (customer buy positive; USD mm or ADV-normalized; state which). Output: slope and $t$-statistic. In production, use heteroskedasticity-robust errors clustered by issuer and day. The simulation below checks the closed form, the absence of post-trade drift under efficient pricing, and the insider's profit $\tfrac12\sigma_v\sigma_u$.

Theo's first markout study was the Halvorsen seller's tier, thirty-eight RFQs over a year *(illustrative)*, and it came back with a slope and a $t$-statistic of 4.1. He was pleased for about a minute. Kaz asked whether the regression would find a number Theo had planted himself, in a world where the answer was known, and Theo admitted he had not checked. A desk never sees how much the other side knows. It sees a signed size, a price, and, if it waits, where the bond went. Kyle's model is the bridge from those observables to the thing you care about, and the bridge holds only if the estimator has been tested where the truth is known. So the desk builds that world first: an insider, a crowd of noise, a market maker, and a planted $\lambda^{K}$. Then it asks whether its own estimator can find the number it just hid.

Listing 18.2 does this with two small functions and one simulation. `kyle_equilibrium` returns the closed form from §18.3.2, $\lambda^{K} = \tfrac12\sigma_v/\sigma_u$ in points per unit of flow and $\beta = \sigma_u/\sigma_v$ in flow per point, and it raises an error on non-positive volatilities instead of returning a number that looks like depth. `estimate_kyle_lambda` is the tool the desk would actually reuse: ordinary least squares of a markout, in points, on signed flow, with an intercept, returning the slope and its t-statistic.

The simulation sets the value volatility at 2 points and the noise volatility at USD 5mm, so the planted $\lambda^{K}$ is 0.2 points per USD mm. For 100,000 draws it generates a true value around a starting price of 90, an insider who trades $\beta$ times the surprise, noise traders who add their flow, and a market maker who prices at the starting price plus $\lambda^{K}$ times total flow. Four assertions follow. Regressing the move from the pre-trade mid on total flow recovers $\lambda^{K}$ within 3 percent, which is the information content of flow. Regressing the move from the trade price on the same flow gives no significant slope, which is the no-drift test for an efficient dealer. The insider's average profit lands on $\tfrac12\sigma_v\sigma_u$. And the variance of value left over after the trade is half the prior variance, the "half the information is revealed" result.

The simulation passed, and Theo's 4.1 still did not survive the afternoon. The listing's $t$-statistic is the textbook one, and real markouts are fat-tailed, heteroskedastic, and clustered by issuer and day. When Kaz swapped in errors clustered by issuer and day, the Halvorsen tier's statistic fell to 1.6 *(illustrative)*: a hint, not a licence to trade on a slope, and certainly not a reason to move a quote. The estimator earns its keep on markouts at a stated horizon, one bond tier at a time, with the benchmark written into the column name, because the benchmark matters as much as the errors. Measure from the pre-trade mid and you recover information; measure from the trade price and a good dealer recovers zero; a column that mixes the two means neither.

*The full listing is [Listing 18.2 in Appendix F](#code-18-2).*

## 18.4 Avellaneda–Stoikov, Derived Without Skipping Steps

Kaz's auto-quoter was an Avellaneda–Stoikov engine. Avellaneda & Stoikov (2008), "High-frequency trading in a limit order book" (*Quantitative Finance* 8(3): 217–224), built on the dealer-inventory model of Ho & Stoll (1981). It is the most-cited model on the desk and the least-read. We read it now, one step at a time.

> **Math, Gently.** *A wobble measured in points, and a phone that rings less the farther away you stand.* Two distributions run every quote in this section, and they answer different questions. *How far will the bond go?* is a question about a level, and the model's answer is the normal distribution of a random walk (Chapter 1's normal and Poisson bags, Chapter 6's random-walk box, §6.1.1). If the mid wobbles with $\sigma = 8$ points per $\sqrt{\text{yr}}$, the typical move over a horizon $\tau$ is $\sigma\sqrt{\tau}$, and over one trading week that is $8\sqrt{5/252} = 1.13$ points: the bond's weekly shiver. The walk here is *arithmetic*, adding points, rather than the lognormal that multiplies percentages, because a bond is quoted in points and lives between its recovery value and a little above par, where a percentage wobble buys nothing but algebra. *How many clients will hit me?* is a question about a count, and its answer is the Poisson distribution: events that arrive one at a time, independently, at some average rate. Here the rate depends on how far from the mid you quote, $\Lambda(\delta) = Ae^{-k\delta}$, and the exponential makes business fall off a cliff as you back away. With $A = 500$ RFQs a year at zero distance and $k = 3$ per point, quote a third of a point away and you keep $500e^{-1} \approx 184$ of them. Normal is for *how far*, Poisson is for *how many*, and every quote is a bet on both at once. The setup writes them down.

### 18.4.1 Setup

Work under $\mathbb{P}$, with time in years.

- **Mid.** $dS_t = \sigma\,dW_t$, arithmetic Brownian motion in price points. Here $\sigma$ is in points per $\sqrt{\text{yr}}$. (Jumps are added in §18.6.)
- **Quotes.** The dealer posts a bid $p^b_t = S_t - \delta^b_t$ and an ask $p^a_t = S_t + \delta^a_t$, with $\delta^b,\delta^a$ in points.
- **Fills.** Counting processes $N^b_t$ and $N^a_t$ jump by one lot when the bid or ask is hit, with intensities $\Lambda(\delta^b_t)$ and $\Lambda(\delta^a_t)$, where $\Lambda(\delta) = A e^{-k\delta}$. $A$ is the arrival rate at zero distance (RFQs per year per side), and $k$ (per point) is how fast business decays as you quote away.
- **Inventory and cash.** $q_t = N^b_t - N^a_t$ in lots, and $dX_t = p^a_t\,dN^a_t - p^b_t\,dN^b_t$.
- **Objective.** Exponential utility of terminal wealth, with risk aversion $\gamma$ per point-lot:

$$
u(t,x,s,q) = \sup_{\delta^b,\delta^a}\; \mathbb{E}^{\mathbb{P}}_t\!\left[-\exp\!\big(-\gamma(X_T + q_T S_T)\big)\right].
$$

Theo read the objective twice. "So the bond shivers about a point a week, the phone rings less the farther away I stand, and the fear is hiding in that exponential."

"The fear is the exponential," Kaz said. "Everything else is bookkeeping."

> **Math, Gently.** *Fear as a number, and planning backwards from the bell.* Exponential utility, $-e^{-\gamma W}$, is a way of writing down how much a dealer minds a loss. The one number to carry around is $1/\gamma$, roughly the size of position at which you start to care: with $\gamma = 0.005$ per point-lot, $1/\gamma = 200$ point-lots, which with \$1mm lots is \$2mm of one-point moves. Its gift is that a normal wobble has a *certainty equivalent*. A dealer holding $q$ lots for $\tau$ years is exactly as happy as if the position were swapped for its expected value minus $\tfrac12\gamma q^2\sigma^2\tau$. With $q = 3$ and $\sigma^2\tau = 1.27$ point$^2$ (the weekly shiver, squared), the penalty is $\tfrac12 \times 0.005 \times 9 \times 1.27 = 0.029$ points on the whole position: pennies. Hold on to that word; it is the punch line of the worked example. The other idea is *dynamic programming*. You cannot choose today's quote without knowing what the position will be worth tomorrow, so you start at the end, where the value is simply what you hold, and work backwards one instant at a time. The equation that does the working backwards is the HJB of §18.4.3. Its $\tfrac12\sigma^2\partial_{ss}$ term is the curvature tax that any curved function of a wobble pays, the same $\tfrac12\sigma^2$ that Itô charges in Chapter 6 (§6.1.1). The answer comes next; the working backwards follows it.

### 18.4.2 The answer first: fear, greed, and Kaz's quote

Here is where the derivation lands, before the algebra that gets it there. Avellaneda and Stoikov set the bid and the ask around a centre that slides away from the mid as inventory builds:

$$
p^{b} = s - \big(q + \tfrac12\big)\gamma\sigma^2\tau - \frac{1}{\gamma}\ln\!\Big(1+\frac{\gamma}{k}\Big),
\qquad
p^{a} = s - \big(q - \tfrac12\big)\gamma\sigma^2\tau + \frac{1}{\gamma}\ln\!\Big(1+\frac{\gamma}{k}\Big),
$$

so the spread is two charges and nothing else:

$$
p^{a} - p^{b} = \underbrace{\gamma\sigma^2\tau}_{\text{fear}} + \underbrace{\frac{2}{\gamma}\ln\!\Big(1+\frac{\gamma}{k}\Big)}_{\text{greed}}. \tag{18.4}
$$

The centre of the two quotes is the reservation price (18.1), $r^{\text{res}} = s - q\gamma\sigma^2\tau$, and its slide with $q$ is the skew. These are the AS quotes, which use the frozen-inventory reservation prices of Step 1 in place of exact ones; the exact versions need the full value function, which GLFT solve in §18.5.

*Limit 1: $\gamma \to 0$.* A Taylor expansion gives $\tfrac{1}{\gamma}\ln(1+\gamma/k) = \tfrac1k - \tfrac{\gamma}{2k^2} + O(\gamma^2) \to \tfrac1k$. A risk-neutral dealer facing demand $Ae^{-k\delta}$ maximizes $\delta A e^{-k\delta}$, whose maximizer is $\delta^{*} = 1/k$. So the second half of the spread is the monopoly markup. It is pure market power, and $k$ is the price elasticity of your RFQ wins. A more competitive market (larger $k$) means a smaller markup, and a dealer with no risk aversion still charges it.

*Limit 2: $t \to T$.* The fear term and the skew both vanish. The AS dealer becomes fearless at the bell.

**Worked example (the cold open).** Take $\sigma = 8$ points$/\sqrt{\text{yr}}$, which is roughly what a B2 bond with spread duration near 4 and spread volatility near 200 bp a year implies *(illustrative)*. Take $\tau = 5/252$ years, a one-week expected holding period rather than the time to the close. Take $\gamma = 0.005$ per point-lot, with a lot of \$1mm, so the dealer's risk tolerance $1/\gamma$ is 200 point-lots, or \$2mm. Take $k = 3$ per point and $q = +3$. Then $\sigma^2\tau = 1.270$ point$^2$, so the fear per lot is $\gamma\sigma^2\tau = 0.0063$ points and the inventory part of the bid distance is $(q+\tfrac12)\gamma\sigma^2\tau = 0.022$ points. The greed per side is $200\ln(1.001667) = 0.333$ points. The bid is $91.25 - 0.022 - 0.333 = 90.895$, which rounds to 90.875 on the eighths grid. That is Kaz's quote.

Notice the proportions: Kaz's quote was 94% greed and 6% fear. In a bond, the diffusive inventory term is usually pennies. The AS dealer is a monopolist with a nervous tic. The real fear lives in jumps (§18.6) and in the client (§18.7), neither of which the formula was given.

### 18.4.3 The Full Derivation

The rest of this subsection is the algebra behind (18.1) to (18.4), one step at a time, with nothing skipped. The setup of §18.4.1 is the starting point; the payoff is Step 4, which turns (18.3) into the quotes of §18.4.2.

#### The HJB equation

Dynamic programming gives the diffusion term from $S$ and one jump term per counting process. When the bid is hit, cash falls by $s - \delta^b$ and inventory rises by one; when the ask is lifted, cash rises by $s + \delta^a$ and inventory falls by one:

$$
\partial_t u + \tfrac12\sigma^2\partial_{ss}u
+ \sup_{\delta^b}\Lambda(\delta^b)\big[u(t,x - s + \delta^b, s, q+1) - u\big]
+ \sup_{\delta^a}\Lambda(\delta^a)\big[u(t,x + s + \delta^a, s, q-1) - u\big] = 0,
$$

with terminal condition $u(T,x,s,q) = -\exp(-\gamma(x + qs))$.

#### Step 1: the frozen-inventory value and the reservation prices

> **Math, Gently.** *The exponential of a wobble, and Jensen's inequality.* Step 1 rests on one identity: if $Z$ is a standard normal draw, $\mathbb{E}[e^{aZ}] = e^{a^2/2}$. In words, the average of an exponential of a wobble is bigger than the exponential of the average wobble. With $a = 1$ the average wobble is zero and $e^0 = 1$, but the average of $e^{Z}$ is $e^{0.5} \approx 1.65$, because the curve bends upward: a draw of +1 lifts $e^Z$ by $e - 1 = 1.72$, a draw of −1 lowers it by only $1 - e^{-1} = 0.63$, and the good draws outweigh the bad. That is Jensen's inequality, $\mathbb{E}[f(Z)] \ge f(\mathbb{E}[Z])$ for any function $f$ that curves upward, and the identity is its exact price for a normal wobble. For a dealer whose disutility is $e^{-\gamma q S_T}$, the bend is the fear: uncertainty about $S_T$ costs more than its average suggests, and the extra cost is the $\tfrac12\gamma^2q^2\sigma^2\tau$ in the exponent below. The same inequality returns in §18.6, where *uncertain* recovery costs inventory more than recovery fixed at its average (the Beta distribution that models recovery belongs to Chapter 5, §5.5.2).

Suppose first that the dealer cannot trade. Using $\mathbb{E}[e^{aZ}] = e^{a^2/2}$ for standard normal $Z$, with $\tau = T - t$,

$$
v(t,x,s,q) = \mathbb{E}\big[-e^{-\gamma(x + qS_T)}\big] = -\exp\!\Big(-\gamma x - \gamma q s + \tfrac12\gamma^2 q^2\sigma^2\tau\Big).
$$

The **reservation bid** $r^b$ is the price at which the dealer is indifferent to buying one more lot: $v(t, x - r^b, s, q+1) = v(t,x,s,q)$. Equating exponents,

$$
\gamma r^b - \gamma s + \tfrac12\gamma^2\sigma^2\tau\big[(q+1)^2 - q^2\big] = 0
\;\Longrightarrow\;
r^b = s - (1+2q)\,\frac{\gamma\sigma^2\tau}{2}.
$$

The same argument for selling one lot gives $r^a = s + (1-2q)\,\gamma\sigma^2\tau/2$. Their average is the famous **reservation price**:

$$
r^{\text{res}} = s - q\,\gamma\sigma^2\tau. \tag{18.1}
$$

A long dealer ($q>0$) values the bond below the mid, and by an amount proportional to inventory, risk aversion, variance, and time left. This is the skew.

Ines, reading over Kaz's shoulder, put it in desk language. "The skew is the dealer's tell. A run that keeps offering one bond lower is a dealer telling you what it owns."

#### Step 2: the exponential ansatz

Try $u = -\exp(-\gamma(x + \theta(t,s,q)))$ with $\theta(T,s,q) = qs$. Then $\partial_t u = -\gamma u\,\theta_t$ and $\partial_{ss}u = u(\gamma^2\theta_s^2 - \gamma\theta_{ss})$. The jump terms factor as

$$
u(t, x - s + \delta^b, s, q+1) - u = u\left[e^{-\gamma(\delta^b - s + r^b)} - 1\right], \qquad r^b \equiv \theta(t,s,q+1) - \theta(t,s,q),
$$

and similarly on the ask, with $r^a \equiv \theta(t,s,q) - \theta(t,s,q-1)$. These $r^b, r^a$ are the indifference prices of the *true* value function, not of the frozen one. Because $u<0$, dividing the HJB by $-\gamma u > 0$ preserves the supremum and gives

$$
\theta_t + \tfrac12\sigma^2\theta_{ss} - \tfrac12\gamma\sigma^2\theta_s^2
+ \sup_{\delta^b}\frac{\Lambda(\delta^b)}{\gamma}\Big[1 - e^{-\gamma(\delta^b - (s - r^b))}\Big]
+ \sup_{\delta^a}\frac{\Lambda(\delta^a)}{\gamma}\Big[1 - e^{-\gamma(\delta^a - (r^a - s))}\Big] = 0 .
$$

Read the bracket on the bid: $\delta^b - (s - r^b) = r^b - p^b$ is the profit from buying at $p^b$, measured at the dealer's own reservation value, passed through the utility.

#### Step 3: the first-order condition

Write $y = \delta - \Delta$, with $\Delta = s - r^b$ on the bid. Maximize $f(\delta) = \Lambda(\delta)(1 - e^{-\gamma y})$. Setting $f'(\delta) = 0$:

$$
\Lambda'(\delta)\big(1 - e^{-\gamma y}\big) + \gamma\Lambda(\delta)e^{-\gamma y} = 0
\;\Longrightarrow\;
y^{*} = \frac{1}{\gamma}\ln\!\left(1 - \gamma\,\frac{\Lambda(\delta^*)}{\Lambda'(\delta^*)}\right). \tag{18.2}
$$

Equation (18.2) holds for *any* decreasing intensity, and §18.7 uses it with a logistic win curve. Since $f = 0$ at $y = 0$, $f \to 0$ as $\delta \to \infty$, and $f > 0$ in between, the unique critical point is a maximum. For the exponential intensity, $\Lambda'/\Lambda = -k$, so

$$
p^{b} = r^{b} - \frac{1}{\gamma}\ln\!\Big(1 + \frac{\gamma}{k}\Big), \qquad
p^{a} = r^{a} + \frac{1}{\gamma}\ln\!\Big(1 + \frac{\gamma}{k}\Big). \tag{18.3}
$$

The parameter $A$ has cancelled: how *often* you are asked does not enter the markup. Hold that thought.

> **Math, Gently.** *Why $\ln(1+x)$ is almost $x$, and why a fearless dealer still has a spread.* For a small number $x$, $\ln(1+x)$ is very nearly $x$, because the logarithm's curve is almost straight near 1. With Kaz's numbers, $x = \gamma/k = 0.005/3 = 0.001667$ and $\ln(1.001667) = 0.001665$. Multiply by $1/\gamma = 200$ and the markup per side in (18.3) is 0.333 points, almost exactly $1/k = 1/3$. So Kaz's greed barely depends on Kaz's fear. It depends on $k$, how quickly clients go elsewhere when you quote away. A dealer with no fear at all still charges $1/k$: the monopoly markup, the price of being the only shop open when somebody needs to trade. Why the fearless limit is exactly $1/k$ is Exercise 1.

#### Step 4: the AS approximation

The exact $r^b, r^a$ require solving for $\theta$ (GLFT do this in §18.5). Avellaneda and Stoikov approximate them by the frozen-inventory values of Step 1, which is accurate when $\gamma$ or the fill intensity is small. Substituting $r^b = s - (1+2q)\gamma\sigma^2\tau/2$ and $r^a = s + (1-2q)\gamma\sigma^2\tau/2$ into (18.3) gives the two quotes displayed in §18.4.2, and subtracting them gives the spread (18.4): the $q$ terms cancel, the two half-fears add to one $\gamma\sigma^2\tau$, and the two markups add to $\tfrac{2}{\gamma}\ln(1+\gamma/k)$.

### 18.4.4 What the formula was not told

Kaz's quote was correct for the world it was given, and the world it was given left out units, clocks, and clients. Each omission turns, sooner or later, into a bad afternoon, and the boxes below are those afternoons written down in advance.

> **Units box: what ROBO did with the volatility.** $\sigma$ is the price volatility of the mid in **points per $\sqrt{\text{yr}}$**; $\tau$ is in **years**; $\gamma$ is per **point × lot**; $k$ is per **point**; $q$ is in **lots** (state the lot size); $A$ is in **RFQs per year per side**. Convert spread volatility to price volatility with $\sigma_P \approx D^{\text{spr}}\,P\,\sigma_s$, where $\sigma_s$ is the decimal spread volatility; for $D^{\text{spr}} = 4$, $P = 91.25$ and $\sigma_s = 0.02$, that gives $\sigma_P \approx 7.3$ points. ROBO was told "use the bond's volatility" and fed 200, the spread vol in bp. The fear term rose by a factor of 625, and the bid came out at 77.03 on a bond at 91.25. ROBO was, technically, being prudent.

> **Ways This Blows Up.** (1) *Terminal time is a calendar artifact.* With $T$ set to 4 p.m., the skew collapses into the close, so the dealer gets brave at 3:55 p.m., the least liquid minutes of the HY day. Set $\tau$ to the expected holding period or use the stationary GLFT quotes (§18.5). (2) *The skew can cross the market.* The spread in (18.4) is positive, but the center $r^{\text{res}}$ moves by $q\gamma\sigma^2\tau$. A desk short 50 lots can produce a bid above the composite offer. Clip quotes to a band around the composite and route breaches to a human. (3) *$A$ does not enter.* AS quotes the same in a bond asked about once a month as in one asked about a hundred times a day. For illiquid bonds this is plainly wrong, and §18.5 fixes it. (4) *$\sigma$ must be a $\mathbb{P}$ forecast of mid price volatility* over the holding period, not CDS implied vol and not spread vol in bp. (5) *The exponential intensity is local.* A real RFQ win curve saturates at one when you bid through the composite. Use (18.2) with the fitted curve (§18.7). (6) *One lot is not a block.* AS prices the marginal lot. The client is selling eight (§18.7).

The skew in (18.1) is not only a theorem. Ben Dor's team saw it in the wild, in dealer indications, and treated it as dirt to be washed out.

> **[SOURCE EXTRACTION]** *Ben_Dor_Quantitative_Credit_Portfolio_Management p.120:* "If a trader were temporarily long inventory of a particular bond, then the trader might quote the bond with a tighter spread (i.e., a higher offered spread) to entice a bid, and vice versa."
>
> **Annotation.** Our analysis: this is the AS skew observed in the wild, written down by people who wanted to remove it. A long trader moves the offer toward the bid to attract buyers, which in spread terms means raising the offered spread. That is (18.1) acting on one side of the market. To Ben Dor's team the skew is contamination in a liquidity measure, and they average a month of indications to wash it out. To a market maker it is the optimal policy, and, as Ines says after (18.1), it carries information. The 2026 desk can turn the observation around and estimate street inventory from the skew of composite contributors, then use it as a feature (§18.8). One caveat about the quotation's world: these were indications, not firm quotes. A dealer can skew a run for free; a firm streaming quote has to pay for the skew when it is hit.

*A fictional first morning, and a boring one.* The auto-quoter's first live day began with a page at 9:31 a.m. The quote monitor had fired on a pattern no human trader could have produced: at 9:30:00, with no trade and no move in any composite, every streaming quote on the desk had widened at once *(illustrative)*. Kaz found the cause in four minutes and spent forty explaining it to the risk manager, who wanted to know why the number was different from yesterday's. The engine's horizon was $\tau = T - t$ with $T$ set to 4 p.m. New York, so the model believed the world ended every afternoon. At the previous close $\tau$ had shrunk to zero, taking the fear term with it, and at the open it snapped back to a full day. "Whose four o'clock?" Ines asked. By lunch $\tau$ was the expected holding period, and the page had become a line in the Spec.

### Specification for AI Implementation (AS quoting core)

**The Spec You Hand the Robot.** *Vague version:* "quote bonds using Avellaneda–Stoikov." *What ROBO built:* the 9:31 page above, with a σ taken from the CDS ladder for good measure. *Precise version:* inputs are the composite mid $s$ (points), inventory $q$ (lots of \$1mm), price volatility $\sigma$ (points/$\sqrt{\text{yr}}$, 20-day $\mathbb{P}$ forecast), $\gamma$ (per point-lot), $k$ (per point, from the fitted win curve), and holding-period horizon $\tau$ (years, never the time to the close). Outputs are bid, ask, $r^{\text{res}}$, and the fear and greed split, all in points, plus prices rounded to the instrument's tick. Guards: reject negative inputs; use the $1/k$ limit when $\gamma < 10^{-12}$; never let unit conversion happen inside the function.

Kaz's quote took a page of arithmetic, and it was a quote for one bond, one inventory, one afternoon. A desk streaming prices on a few hundred bonds needs that arithmetic redone every time a fill changes $q$ or the volatility forecast ticks, with nobody around to notice that the 200 should have been a 7. The formulas are short, which is the dangerous part: short formulas get typed into spreadsheets, and spreadsheets do not have units. So the quoting core lives in a function with a narrow contract and a few tests, which makes the arithmetic boring and turns every bad input into somebody's explicit decision.

Listing 18.3 is that function. `as_greed` computes the per-side markup $\tfrac{1}{\gamma}\ln(1+\gamma/k)$ using `log1p` for accuracy, raises an error if $k$ is not positive, and falls back to the limit $1/k$ when $\gamma$ is below $10^{-12}$, so a risk-neutral setting does not divide by zero. `as_quotes` then takes the composite mid, inventory in lots, price volatility, risk aversion, the win-curve decay $k$, and the horizon $\tau$ in years. It computes the fear term $\gamma\sigma^2\tau$, shifts the center to $r^{\text{res}} = s - q\cdot\text{fear}$, and sets the bid and ask half the fear plus one greed away from that center. It returns the reservation price, both quotes, and the spread split into fear and greed, where `greed` is the two-sided total. The helper `to_eighth` rounds to the grid.

The tests reproduce Kaz's bid of 90.8947, which rounds to 90.875. They confirm that the spread is fear plus greed, that greed is over 90 percent of it, that greed approaches $1/k$ as $\gamma \to 0$, and that the center collapses to the mid when $\tau = 0$. A brute-force check then maximizes the general first-order objective numerically for the exponential intensity and finds that the optimum sits at the reservation offset plus `as_greed`, whatever the value of $A$. The last assertion feeds in 200 as volatility and confirms the bid drops below 78.

The function prices the marginal lot in a bond liquid enough that $A$ does not matter, with $\tau$ set to the holding period; bonds where $A$ matters belong to §18.5, and blocks to §18.7. Its last assertion records the unit mistake without preventing it. The function checks only that $\sigma$, $\gamma$, and $\tau$ are non-negative, so a volatility in basis points is a perfectly legal input, exactly as ROBO found in the Units box. Nor does it clip to the composite or round to the tick, so a large inventory can return a bid above the market. Those guards live in the caller, which is also where the 9:31 page was fixed.

*The full listing is [Listing 18.3 in Appendix F](#code-18-3).*

## 18.5 GLFT: Inventory Bounds, Linear ODEs, and the Stationary Dealer

Two things about Kaz's engine bothered Ines from the first week, and neither was in the formula. The desk has a risk limit, a number of lots past which the risk manager calls, and AS does not know it exists. And the desk has no close. A bond book is not flattened at 4 p.m.; it is carried overnight, over weekends, sometimes for months, so the horizon $\tau$ that AS needs is a guess wearing a parameter's clothes. The model she wanted would know the wall, would have no bell, and would quote a bond that clients ask about twice a week differently from one they ask about twice an hour.

> **Math, Gently.** *A marble in a bowl, and how fast the street forgets.* Picture the desk's inventory as a marble sitting in a bowl. The bowl is the fear: its sides rise like $\alpha q^2$, so every extra lot in either direction costs more than the last. Client flow knocks the marble one step left or right at a rate set by $\eta$, which grows with how often the bond is asked about. GLFT write the dealer's value at each inventory level as one entry in a list running from $-Q$ to $+Q$, and the list evolves by a *tridiagonal* matrix: each level talks only to itself and its two neighbours, because a trade moves inventory one lot at a time. Any pattern on that list can be broken into *modes*, shapes that keep their form and simply fade, each at its own rate; those rates are the matrix's eigenvalues. Wait long enough and every mode but the slowest has faded, and the survivor is the stationary dealer's valuation. The distance between the slowest rate and the next one, the *spectral gap*, is how fast the street forgets your position, and its inverse is a horizon. With this section's inputs (per trading day: $\sigma^2 = 64/252 = 0.254$, $\gamma = 0.005$, $k = 3$, $A = 2$), the bowl's steepness is $\alpha = \tfrac12 k\gamma\sigma^2 = 0.0019$ and the knocking rate is $\eta = 0.735$, so the gap is $2\sqrt{\alpha\eta} = 2\sqrt{0.0014} = 0.075$ per day and the horizon is $1/0.075 \approx 13$ trading days. Quadruple $A$ and $\eta$ quadruples, the gap doubles, and the horizon halves: a bond asked about four times as often forgets your position twice as fast. The derivation that turns this picture into (18.5) is below.

Guéant, Lehalle & Fernandez-Tapia (2013), "Dealing with the inventory risk: a solution to the market making problem" (*Mathematics and Financial Economics*; arXiv 1105.3115), solve exactly that problem, with $|q| \le Q$. The surprise is that the nonlinear HJB collapses into *linear* ODEs, (18.5) in the derivation below. Let the horizon run to infinity, so the bell disappears, and the quotes of the stationary dealer are

$$
\delta^{b}_\infty(q) \approx \frac1\gamma\ln\!\Big(1+\frac\gamma k\Big) + \frac{2q+1}{2}\,\omega, \quad
\delta^{a}_\infty(q) \approx \frac1\gamma\ln\!\Big(1+\frac\gamma k\Big) - \frac{2q-1}{2}\,\omega, \quad
\omega = \sqrt{\frac{\sigma^2\gamma}{2kA}\Big(1+\frac\gamma k\Big)^{1+\frac k\gamma}}. \tag{18.6}
$$

The skew per lot is $\omega$, and **$A$ is back**. Set the AS skew $\gamma\sigma^2\tau$ equal to $\omega$ and solve for the horizon:

$$
\tau_{\text{eff}} = \frac{\omega}{\gamma\sigma^2} = \frac{1}{\sqrt{2k\gamma\sigma^2\eta}} = \frac{1}{2\sqrt{\alpha\eta}},
$$

the inverse spectral gap of $M$, the tridiagonal matrix of the box (written out in the derivation below, with $\alpha = \tfrac12 k\gamma\sigma^2$ and $\eta = A(1+\gamma/k)^{-(1+k/\gamma)}$). The effective horizon is how long the street takes to forget your position, and it shrinks like $A^{-1/2}$: a bond asked about four times as often needs half the skew. With $\sigma = 8/\sqrt{252}$ points per $\sqrt{\text{day}}$, $\gamma = 0.005$, $k = 3$, and $A = 2$ fills per day per side at zero distance *(illustrative)*, we get $\eta \approx 0.735$, $\omega \approx 0.017$ points per lot, and $\tau_{\text{eff}} \approx 13$ trading days. That is longer than the one-week guess Kaz plugged into AS. On a Friday afternoon $A$ drops to zero for 60 hours, $\tau_{\text{eff}}$ blows up, and the stationary dealer widens on its own. Credit Suisse's AT1 holders learned why one weekend in 2023 (§18.6). Figure 18.2 shows the tilt and the horizon side by side.

![Figure 18.2: The stationary GLFT dealer tilts its whole quote ribbon about 2.7 times harder per lot than the one-week AS dealer (left), because its effective horizon is the inverse spectral gap, about 13 trading days at A = 2, and that horizon shrinks like A^(−1/2) as the bond gets busier (right). Illustrative: quotes computed from the models of §18.4 and §18.5 with σ = 8 points per √yr, γ = 0.005, k = 3, and A = 2 fills per day per side at zero distance in the left panel.](assets/figures/ch18_quote_ladder_glft_horizon.png)

#### The Full Derivation

**Derivation.** Guess $u(t,x,s,q) = -\exp(-\gamma(x+qs))\,v_q(t)^{-\gamma/k}$, which is the §18.4 ansatz with $\theta = qs + \tfrac1k\ln v_q(t)$. Then $\theta_s = q$, $\theta_{ss} = 0$, $\theta_t = \dot v_q/(k v_q)$, and the reservation prices are $r^b = s + \tfrac1k\ln(v_{q+1}/v_q)$ and $r^a = s - \tfrac1k\ln(v_{q-1}/v_q)$. Equation (18.3) gives the quotes:

$$
\delta^{b}_q(t) = \frac1k\ln\frac{v_q(t)}{v_{q+1}(t)} + \frac1\gamma\ln\!\Big(1+\frac\gamma k\Big), \qquad
\delta^{a}_q(t) = \frac1k\ln\frac{v_q(t)}{v_{q-1}(t)} + \frac1\gamma\ln\!\Big(1+\frac\gamma k\Big).
$$

At the optimum, $e^{-\gamma y^*} = k/(k+\gamma)$, so each supremum equals $A e^{-k\delta^*}/(k+\gamma)$. Substituting $e^{-k\delta^{b*}} = (v_{q+1}/v_q)(1+\gamma/k)^{-k/\gamma}$, the bid supremum becomes $\tfrac{\eta}{k}\,v_{q+1}/v_q$, with $\eta = A(1+\gamma/k)^{-(1+k/\gamma)}$. The reduced HJB, multiplied by $k v_q$, is

$$
\dot v_q(t) = \alpha q^2\, v_q(t) - \eta\big(v_{q-1}(t) + v_{q+1}(t)\big), \qquad \alpha = \tfrac12 k\gamma\sigma^2, \qquad v_q(T) = 1, \tag{18.5}
$$

for $q \in \{-Q,\dots,Q\}$. At $q = Q$ there is no bid, so the $v_{Q+1}$ term is dropped, and symmetrically at $-Q$. In matrix form, $\dot{\mathbf v} = M\mathbf v$ with $M$ symmetric tridiagonal ($\alpha q^2$ on the diagonal, $-\eta$ off it), so $\mathbf v(t) = e^{-M(T-t)}\mathbf 1$. Inventory risk has become a linear algebra problem.

**The stationary dealer.** A bond desk has no close: $T$ is an artifact, and the right object is the limit $T - t \to \infty$. There $\mathbf v \propto \mathbf f_0$, the ground state of $M$ (positive, by Perron–Frobenius), and the quotes stop depending on time. For a closed form, treat $q$ as continuous: $f_{q+1} + f_{q-1} \approx 2f + f''$, so $-\eta f'' + \alpha q^2 f = (\kappa + 2\eta) f$ for an eigenvalue $\kappa$ of $M$. That is the quantum harmonic oscillator, with ground state $f_0 \propto \exp(-\tfrac12\sqrt{\alpha/\eta}\,q^2)$ and eigenvalue spacing $2\sqrt{\alpha\eta}$. Then $\ln(f_q/f_{q+1}) = \tfrac12\sqrt{\alpha/\eta}\,(2q+1)$, which, with the markup of (18.3) added on each side, gives the stationary quotes (18.6) stated above.

Guéant (2017), "Optimal market making" (*Applied Mathematical Finance*; arXiv 1605.01862), extends the result to general intensity functions and many assets, and applies it to two credit indices. Guéant & Manziuk (2019, arXiv 1910.13205) note that for a large bond universe "classical finite difference methods … cannot be used" and switch to model-based deep actor–critic methods. Chapter 19 inherits that curse of dimensionality.

> **View From Another Seat.** *A mid-sized dealer desk, in its own published words.* Ines prices fear as if she had a balance sheet to be afraid with. A mid-sized dealer reads the same equations with a smaller $Q$. Jefferies' global head of fixed income, Fred Orlan, put the economics plainly in a 2023 profile: "It's hard for investment banks to run large balance sheets in this environment because it isn't making a lot of money," and "You're really making your money trading with and helping clients, which requires good ideas and good execution" (The DESK, 26 Oct 2023). From the top of the league table, Jamie Dimon wrote in JPMorgan Chase's 2025 shareholder letter that "brokerage inventories are far smaller as a percentage of investments than ever before and, as a result, market makers are less able to intermediate in extremely volatile markets" (6 Apr 2026). In this section's language, and this reading is ours rather than theirs, both sentences are about two parameters. A small inventory bound $Q$ puts the wall close to the bottom of the bowl, so the dealer lives on turnover, which is $A$: a desk that cannot hold risk is paid by how often it is asked, and its skew per lot shrinks only as fast as $\sqrt{A}$ grows. Dimon's "less able to intermediate" is the Friday afternoon generalized: when $A$ falls in a volatile market, $\tau_{\text{eff}}$ lengthens, the skew per lot widens, and a dealer with a small $Q$ steps back. Figure 18.3, below, is the whole street's $Q$ going negative at the long end.

The street has been moving toward Orlan's model since the crisis, and the Fed's weekly dealer statistics show how far.

> **Trend Watch: the vanishing, then negative, dealer inventory (2007–2026).** *What changed:* post-crisis capital rules pushed bank dealers from warehousing risk toward matching it. Bessembinder, Spatt & Venkataraman (2020, *JFQA* 55(1)) report that non-bank dealers' share of customer–dealer volume rose several-fold after the crisis (as summarized in our industry dossier). *Stress test:* in March 2020, Kargar et al. (2021) find risky-principal costs "increased dramatically" and flow shifted to agency trades. *How big, now:* The DESK (2024-11-20) reported primary dealers net short US\$3.8bn of IG bonds over five years, and quoted Crisil Coalition Greenwich's Kevin McPartland: "Our research continues to point to a corporate bond market that is agency (or at most, riskless principal)." Hedgeweek (2026-07-13), on Crisil Coalition Greenwich analysis of Fed data, reported primary dealers net short US corporates on average in 2026, about \$4bn, for the first time in at least 25 years, against an average net long of about \$16bn in 2017: roughly \$13.7bn short over five years and \$9.7bn long in shorter paper. *What it means:* the market's average fear term, $q\gamma\sigma^2\tau$ summed over dealers, is near zero and in the long end negative, so a typical dealer is *eager to buy* long paper. The spreads that remain are suspicion, greed, and franchise. Agency trading is the $\tau_{\text{eff}} \to 0$ limit of GLFT, where only the constant $\tfrac2\gamma\ln(1+\gamma/k)$ survives. A net-short street also creates squeeze risk if spreads tighten, because pensions and insurers rarely sell long paper. That point was raised in the Hedgeweek piece, and the inventory model prices it as a short-side $\omega$ that nobody budgeted for.

![Figure 18.3: Primary dealers' net position in corporate bonds due beyond five years swung from a small long (+\$4.1bn on average in 2017) to a net short (−\$12.1bn on average in 2026 to date, with the 13-week average near −\$16bn in spring 2026), while paper due within five years stayed long (+\$9.8bn on average in 2026). The box's −\$13.7bn and +\$9.7bn match this series averaged over the first 25 weeks of 2026 only. The dashed line marks mid-March 2020, the Covid dislocation. Source: NY Fed Primary Dealer Statistics, weekly net positions (long minus short) in investment-grade and below-investment-grade corporate bonds, notes and debentures, series PDPOSCSBND-* (retrieved 18 October 2026), January 2015 to 7 October 2026; lines are 13-week averages.](assets/figures/ch18_dealer_net_inventory_nyfed.png)

## 18.6 Jump-to-Default Inside the HJB

Kaz's model has one source of risk, $\sigma\,dW_t$. A B2 bond has two. The second is the Tuesday a company announces it would prefer you take 70 cents. Add a Poisson jump to the mid:

$$
dS_t = \mu\,dt + \sigma\,dW_t - J\,dN_t, \qquad N_t \text{ Poisson with } \mathbb{P}\text{-intensity } \lambda^{\mathbb{P}},
$$

where $J > 0$ is the gap in points (default to recovery, or an LMT repricing), and $\mu$ is a drift we come back to. The jump does not change the *structure* of AS. It changes the variance and adds a drift.

> **Math, Gently.** *The jump's exponential, and whose odds you are using.* **Part one: a count inside an exponential.** Box 5's trick priced a normal wobble inside an exponential. A jump is a count instead: $N_\tau$, the number of defaults or LMT-style gaps over the horizon, is Poisson, and with $\lambda^{\mathbb{P}}\tau = 0.10$ it is 0 about 90.5% of the time ($e^{-0.10}$) and almost never more than 1. The count has its own version of the trick, $\mathbb{E}[e^{cN_\tau}] = \exp\!\big(\lambda\tau(e^{c}-1)\big)$, and for a dealer the $c$ that matters is $\gamma qJ$, risk aversion times inventory times the size of the gap. With $\gamma = 0.005$, $q = 5$ lots and $J = 21$ points, $c = 0.525$ and $e^{0.525} = 1.69$. That 1.69 multiplies the jump charge on the next lot, so a long dealer's fear of the next lot is 69% larger than a flat dealer's. Nothing like it happens in the Gaussian world, where the next lot costs a little more per lot already held; here it costs more *multiplicatively*, because the gap hits everything you own at once. **Part two: the forecast and the bookmaker.** A weather forecast says what will happen; a bookmaker's odds say what the bet costs, fear and margin included (Chapter 5's two kinds of probability, §5.1.1; Chapter 6's risk-neutral pricing, §6.2.2). The composite mid is the bookmaker: it already prices a jump intensity under $\mathbb{Q}$, say $\lambda^{\mathbb{Q}}\tau = 0.03$. Your forecast, built from the documents and the calendar, says $\lambda^{\mathbb{P}}\tau = 0.10$. Only the difference is news, and $(0.10 - 0.03) \times 21 = 1.47$ points is your *credit view*. Feed the bookmaker's odds in as your forecast and you charge the market's fear on top of the market's price, which is a reliable way never to win an RFQ in a name everyone is already worried about.

For a dealer who is not very risk-averse, everything the jump does to the reservation price fits on one line:

$$
r^{\text{res}} \approx s + \mu\tau - \lambda^{\mathbb{P}}J\tau - q\gamma\big(\sigma^2 + \lambda^{\mathbb{P}}J^2\big)\tau .
$$

Expected loss moves the centre; jump variance adds to the fear. The term $\lambda^{\mathbb{P}}J\tau$ shifts the price for every dealer, long or flat. Jump *variance* $\lambda^{\mathbb{P}}J^2$ adds to $\sigma^2$ in the inventory penalty, even for a dealer whose view is neutral. This is the $q\lambda J$ term promised in the Part V opener, multiplied by the $\gamma J$ that converts a loss into a fear. The exact version, (18.7), keeps the multiplicative $e^{\gamma qJ}$ of the box, and the GLFT version, (18.8), puts it on the diagonal of the matrix.

### 18.6.1 The Full Derivation: exact reservation prices

Freeze inventory and use the Poisson moment generating function $\mathbb{E}[e^{cN_\tau}] = \exp(\lambda\tau(e^c - 1))$:

$$
\mathbb{E}\big[e^{-\gamma q S_T}\big] = \exp\!\Big(-\gamma q (s + \mu\tau) + \tfrac12\gamma^2 q^2\sigma^2\tau + \lambda^{\mathbb{P}}\tau\big(e^{\gamma q J} - 1\big)\Big).
$$

So the certainty-equivalent function becomes

$$
\theta(q) = q(s + \mu\tau) - \tfrac12\gamma q^2\sigma^2\tau - \frac{\lambda^{\mathbb{P}}\tau}{\gamma}\big(e^{\gamma q J} - 1\big),
$$

and, as in §18.4, $r^b = \theta(q+1) - \theta(q)$:

$$
r^{b} = s + \mu\tau - (1+2q)\frac{\gamma\sigma^2\tau}{2} - \frac{\lambda^{\mathbb{P}}\tau}{\gamma}\,e^{\gamma q J}\big(e^{\gamma J} - 1\big),
\qquad
r^{\text{res}} = s + \mu\tau - q\gamma\sigma^2\tau - \frac{\lambda^{\mathbb{P}}\tau}{\gamma}\,e^{\gamma qJ}\sinh(\gamma J). \tag{18.7}
$$

The factor $e^{\gamma qJ}$ makes the reservation price *asymmetric* in inventory. Comparing $q$ with $-q$, the long dealer's discount exceeds the short dealer's premium by $\tfrac{2\lambda^{\mathbb{P}}\tau}{\gamma}\sinh(\gamma J)\cosh(\gamma qJ)$. A long dealer fears the next bond more than a short dealer wants it.

**Small $\gamma$.** Expanding $\tfrac1\gamma e^{\gamma qJ}(e^{\gamma J}-1) = J + \gamma J^2(q + \tfrac12) + O(\gamma^2)$, and the same for the ask, then averaging the two, gives the one-line approximation stated at the top of this section.

**The measure question.** If the composite $s$ is already the $\mathbb{Q}$-fair mid, then $s$ is a $\mathbb{Q}$-martingale and its compensator drift is $\mu = \lambda^{\mathbb{Q}}J$. The expected-loss term becomes

$$
\mu\tau - \lambda^{\mathbb{P}}J\tau = -\big(\lambda^{\mathbb{P}} - \lambda^{\mathbb{Q}}\big)J\tau .
$$

This is the dollar value of a private read of the credit documents. If you plug CDS-implied intensities in as $\lambda^{\mathbb{P}}$, you charge the jump twice, once in the composite and once in your skew, and you never win an RFQ in a name the market is already worried about. The variance term, by contrast, needs $\lambda^{\mathbb{P}}$, because risk is borne under the physical measure.

**Random jump sizes.** For default, $J = s - 100R$ with recovery $R \sim \text{Beta}(a,b)$ (Chapter 5, §5.5.2). Replace $e^{\gamma qJ}$ with the moment generating function $M_J(\gamma q) = \mathbb{E}[e^{\gamma q J}]$, computed by quadrature. By Jensen's inequality $M_J(\gamma q) \ge e^{\gamma q\,\mathbb{E}[J]}$, so recovery *uncertainty* costs inventory on top of expected recovery. Mags: "Price is what you pay. Recovery is what you get, eventually, after the lawyers." The MGF is how the lawyers enter the HJB.

**Inside GLFT.** The jump adds $\lambda^{\mathbb{P}}[u(s-J) - u] = \lambda^{\mathbb{P}}u(e^{\gamma qJ} - 1)$ to the HJB, and the drift adds $\mu\,\partial_s u$. Repeating §18.5 gives

$$
\dot v_q = \Big[\alpha q^2 - k\mu q + \frac{k\lambda^{\mathbb{P}}}{\gamma}\big(e^{\gamma qJ} - 1\big)\Big]v_q - \eta\big(v_{q-1} + v_{q+1}\big). \tag{18.8}
$$

The system is still linear and still symmetric. The potential is tilted toward short inventory, and its curvature at $q=0$ is $\alpha + \tfrac12 k\gamma\lambda^{\mathbb{P}}J^2$. With our numbers, jump variance contributes about eight times the diffusive curvature.

### 18.6.2 Where $\lambda^{\mathbb{P}}$ comes from: the RSSG bridge

Here Theo's old job pays rent. A dealer's $\lambda^{\mathbb{P}}$ should not be a constant. It is a *Poisson process with an appointment book*: a baseline from the default model of Chapter 6, plus bumps on scheduled dates (earnings calls, lender calls, coupon dates, maturity walls) scaled by the Priming Risk Score of Chapter 13. The 13-week cash flow model, still on its USB stick, is reborn once more as the liquidity-runway input to that score. When the PRS of a name spikes before its lender call, $\lambda^{\mathbb{P}} - \lambda^{\mathbb{Q}}$ is positive *before the market reprices*, and the bid moves for reasons the auto-quoter never saw. That is what Theo did in the cold open, in his head, in eleven seconds.

### 18.6.3 Case Study: Altice France (March 2024) and Credit Suisse AT1s (March 2023)

#### Long Scene: Altice France, 20 March 2024 (replay)

*Pair Book entry PB-14, a replay cut off at 10:30 London time on Wednesday 20 March 2024. The desk's 2024 blotter, its quotes, its inventory, its model outputs and every size, mark and P&L figure below are fictional and illustrative (the desk's fictional run); so are Owen Achterberg's capital-structure pod at Vantress (Chapter 4-C) and its trades. Altice France, Altice France Holding, their instruments, the dates, the call and the reported price moves are real and sourced. The pod is an outside holder in no group; nobody on the desk sits in one either.*

Ines's Friday replay had a guest again. Owen Achterberg had come across after his own close, and for once he had a personal stake in the hand, because the client on the blotter was his pod. In March 2024 the desk still kept a seat in London for European high yield *(illustrative)*, and its blotter for that Wednesday had two lines from Vantress, forty minutes apart. Ines had cut the tape at 10:30 London, ten minutes before the first one. Mags read the ticker on the first slide, said "I was there," and rolled her chair back to the wall, which is the replay rule for people with memories.

The slide had the capital structure on it, because Theo had asked for it before he would look at anything else. Altice France, the French telecom group behind SFR, carried about €24bn of debt: roughly €10.9bn of senior secured notes in eleven series due 2027 to 2029, about €7.1bn of term loans, a revolver, and, one floor up the organization chart at Altice France Holding (AFH), about €4bn of unsecured notes (IFR; Elevenflo). The secured notes had claims on the operating company. The holdco notes had a claim on the holdco, whose main asset was its equity in the operating company, which is a polite way of saying they were paid from whatever the secured creditors left. The calendar row said: fourth-quarter results that day, and a call for debt investors at 14:00 Paris time, 13:00 in London (Altice France, Q4 2023 results release, 20 March 2024). Theo's Priming Risk Score had the name at 0.58 on the leverage and the 2027 maturities in the public filings *(the desk's fictional run)*. Kaz's Roll estimator, as §18.2 told, had returned NaN on the secured notes three sessions running.

*10:40.* The first RFQ. *Vantress buys €5mm Altice France 2027 first-lien notes, disclosed, four dealers.* The client tier said *fast money, mid tier*. The desk was long exactly €5mm of the same notes from the week before, marked near 69 on the composite *(illustrative)*.

Kaz's AS engine, which in the replay was quoting as if it had been there, offered a few cents through the composite and said, in effect, that five lots of diffusive inventory cost pennies to hold. "It wants to keep them," Kaz said. "Or rather, it doesn't care."

"I care," Ines said. "It's a scheduled event with a jump in it. Look at (18.7)." She did not need the formula to know what it said; she had sold the five lots at 10:41 in 2024 and remembered why. A long dealer's reservation price falls with inventory far faster when a jump is in the model, so at five lots into a call the desk's own value for the bonds sat well below the composite. Any offer near the composite was the desk being paid to get flat. The replay offer went out a quarter through the composite, and the blotter showed the same thing had happened in 2024: Vantress lifted it, and the desk went into the call owning nothing.

*11:20.* The second RFQ. *Vantress sells €3mm Altice France Holding 8% notes due 2027, disclosed, four dealers.* The holdco composite had drifted down since the open *(illustrative)*; so, a little, had the secured. The desk was flat the holdco.

Ines dealt the cards. *You are the dealer. Write your bid on the holdco, your size, and whether the fact that this client just bought the secured changes your number.* One went to Owen, who looked at it, laughed, and put it face down without writing. It is hard to bid against yourself.

Theo wrote *composite minus 2, all three, yes: it's one trade in two tickets.* Kaz wrote *AS: composite minus 0.4. No. A client is a client.* Then Kaz looked at Theo's card, which was also face down, and added a question mark.

"Talk me through yours," Ines said to Theo.

"Same client, same morning, long the senior and short the junior, two hours before a call about leverage," Theo said. "At PJT that's the first thing anyone does when they think a company is going to ask creditors for a discount: own the claim that gets asked last and sell the one that gets asked first. It doesn't need anyone to know anything. It needs someone to have read the capital structure before the call instead of after."

"Which is what *informed* means at this table most days," Ines said. She turned to Owen. "Is that what it was?"

"Public filings, a leverage number, and a calendar," Owen said. "We thought the call would talk about the discount and the market would find out where it landed. We didn't know where it would land. We knew the holdco was further from the money."

"Then the first ticket is the tell," Ines said, "and the second ticket is the one that hurts."

*13:00.* The call. The tape ran forward. Management set out a target to bring leverage, then above six times EBITDA, below four, and finance executives said that creditors would need to take part in "discounted transactions" to get there (BNN Bloomberg, 20 March 2024; CreditSights). The group's debt fell about 20 points in the session (IFR). Press reports put the €1.3bn first-lien notes due 2027 down about 21 points to around 48, their largest drop since they were issued in 2020, though a later report attributed a 21-point fall to the unsecured bonds instead; CreditSights described the unsecureds that day as in freefall, and some of the group's bonds went on to trade below 30 (BNN Bloomberg, 20 and 26 March 2024). By that evening a group of creditors had signed a cooperation agreement. It grew to about two hundred institutions holding about €19bn of the operating company's secured debt (IFR). *(Cooperation agreements signed on the page in this book: still two. Altice France's is one of the forty-five Chapter 14 counts for 2024.)*

Mags had been in her chair against the wall the whole time. "I heard about the co-op from a dealer's evening note, like everyone else who wasn't in it," she said. "Back in my day the co-op was three people and a fax. Now it's two hundred institutions and a WhatsApp group with a lawyer in it." She paused. "This is better. Faster. Worse for whoever's left outside."

Kaz had a calculator open. On the secured, the reported one-day move was about 21 points. Kaz's Gaussian, at 8 points a year, puts a one-day 21-point move at about 42 standard deviations: an event that happens under the normal distribution roughly never and in credit most springs. "Let's just assume Gaussian," Kaz said, to nobody, as an epitaph.

*The autopsy.* Ines turned the cards over and graded them against the blotter. In 2024 the desk had bid four points under the holdco composite for the €3mm *(illustrative)*, which was the formula's number for the holdco plus a charge for the first ticket, and it had lost: another dealer covered a point and a half under the composite and bought the bonds forty minutes before they fell at least as far as the secured did. Theo's card would have won the trade and owned it into the call. Kaz's card would have won it by more and lost by more. "Right fact," Ines told Theo, as she had on the Halvorsen card. "The first ticket changes the number. You just didn't let it change it enough."

Then she went back to the ticket the desk had *not* lost, the five lots of secured it sold at 10:41, and made Kaz price what holding them would have meant. Into the call, take $\lambda^{\mathbb{P}}\tau = 0.10$ (a desk read of a one-in-ten chance that the call signals an LMT), $\lambda^{\mathbb{Q}}\tau = 0.03$, $J = 21$ (the gap that actually came), $q = 5$, $\gamma = 0.005$, and a one-day $\tau$. Equation (18.7) puts the reservation price about 2.9 points below the composite: 1.47 points of credit view, $(0.10 - 0.03)\times 21$, and 1.46 points of jump-risk premium. That is still a long way from 21, and it should be. The engine's job was not to predict the call. It was to bid low enough to be paid for the chance, and to shrink $q$ into a scheduled event, which is what the 10:41 sale did. Had the desk kept its five lots at 69, the 21-point gap would have cost about €1.05mm overnight *(illustrative)*. A systematic desk would have flagged the name on three features, all of them public: the calendar bump, a PRS input from the leverage language (Chapter 13's NLP), and the Roll estimator's run of NaNs on the secured notes in the preceding sessions (§18.2.1). Figure 18.4 plots the reservation price against inventory.

![Figure 18.4: Once a jump is in the model, a long dealer's reservation price falls with inventory far faster than the flat Gaussian AS skew, and the penalty is asymmetric: the jump-risk premium turns into a payment for a short dealer, whose reservation price rises above the composite until the desk's credit view pulls it back to about the composite. At q = +5 with the Altice inputs the price sits 2.93 points below the composite, 1.47 of credit view and 1.46 of jump-risk premium, against a reported one-day move of about 21 points (§18.6.3). Illustrative: Equation (18.7) with J = 21 points, γ = 0.005, σ = 8 points per √yr, a one-day horizon, P-intensity times horizon 0.10, and Q-intensity times horizon 0.03.](assets/figures/ch18_jtd_reservation_price.png)

"So the desk got out of the secured because of the jump," Theo said, "and I'd have walked into the holdco because I forgot the jump was bigger one floor up."

"And Owen," Ines said, "did both of those things on purpose, in the other direction, and paid us for the privilege. Owen, your card."

Owen's question for the room was the pod's, not the dealer's, and it was the one he had faced at 10:35 that morning in 2024. *Leg it, or wait for both sides to show at once and pay the wider print? Write three things: which leg first, how long you would wait for the second, and what you would pay not to wait.* Theo wrote *secured first, the long dealer wants out; ten minutes; a point.* Kaz wrote *both at once, as a package; no waiting; whatever the package costs.* Mags, from the wall, said, "The holdco first. It's the one nobody will want to lend you at two o'clock."

> **The Pair.** *PB-14, Owen's pod: long Altice France 2027 first-lien notes, short Altice France Holding 8% 2027 notes (borrowed through the prime broker). Sizes, marks, recoveries and P&L are illustrative; instruments, dates and plan terms are real.* **The hedge.** Recovery-weighted market value, so that a default on the day costs the pair nothing: long €5mm of the secured at 69 with a model recovery of 55 risks €0.70mm; short €3mm of the holdco at 50 with a model recovery of 27 gains €0.69mm. The ratio is 0.6 by face, chosen by recoveries, not by duration or beta (Chapter 12-B's rule near default; the full ruler menu is §8D.3). **What the hedge removes.** Default itself, on the day, at the model's recoveries. The direction of Altice France stops mattering. **What idio remains.** How the discount would be allocated across the structure: whether management's "discounted transactions" would land on the holdco harder than on the secured. The plan that was eventually implemented on 1 October 2025 answered it: secured holders received about 7.6% in cash plus about 77% of principal in new secured debt and about 31% of the new equity; AFH holders received 2.5% in cash, 20% in new 2033 debt and 14% of the equity (`case_lmt_private_and_european_2024_2026` §3; Paperjam, Delano, Elevenflo). The gap between those two lines is the trade, and nothing else is. **What leaked.** *Legging.* The secured leg filled at 10:41 from a dealer that wanted out. The holdco leg filled at 11:20, after its composite had drifted and after the dealer had seen the first ticket and charged the second for it, so the short went off about a point and a half below where it was quoted at 10:40 *(illustrative)*. The pod paid for the jump twice, once in the drift and once in the winning dealer's fear, and on the day of the call the pair still lost money, because a fall of similar size in points was taken on €5mm of the long and only €3mm of the short. **What it costs to carry and to short.** The long earns the secured coupon; the short pays the holdco's 8% for as long as the holdco pays it, which ended when AFH missed its interest on 15 May 2025 (a short owes the coupon the bond pays, and it paid none). The borrow is the real bill. Asquith, Au, Covert and Pathak (2013) find corporate-bond borrowing costs of 18 to 33 bp a year on average but 173 bp in the thirty days before a bankruptcy filing and 245 bp after, with every loan recallable on demand; a holdco bond in a restructuring is exactly the bond whose lender recalls. The CDS alternative carries its own basis (Chapter 24): Altice France's protection settled in an auction at 87.75 on 27 August 2025, paying 12.25 per 100, while the Determinations Committee found a Failure to Pay on the AFH notes and held no AFH auction at all (`case_lmt_private_and_european_2024_2026` §3). A short leg in holdco CDS would have been a negotiation, not a hedge. *Ledger:* opened in this chapter, stressed in Chapter 18-B, which decomposes the desk's two quotes to the pod tier by tier and shows why the second RFQ is the toxic one, and closed here, after the August 2025 approval of the plans.

Ines graded the pod's cards against what happened. Owen had legged, secured first, exactly as Theo wrote, and the leak was the point and a half plus the dealer's shade, a few tens of thousands of euros on €3mm *(illustrative)*. Kaz's package would have been the cleaner trade on paper, and on that Wednesday it did not exist: no dealer would quote both legs as one ticket two hours before a call, and after 13:00 there was no pre-call price for either leg at any size. Mags's answer was the one Owen wished he had given in 2024. The short leg was the scarcer one, the borrow was the thing that could vanish, and the side that is hard to get is the side you get first. "You were right about which leg would leak," Owen told her.

"I was right about which leg I couldn't borrow in 2008," Mags said. "Same thing."

#### Credit Suisse AT1s, 17 to 19 March 2023 (replay)

*A replay cut off at the close on Friday 17 March 2023. The desk's position, its model outputs and every number attached to them are illustrative; Credit Suisse, UBS, FINMA, the dates and the write-down are real. Chapter 23 tells the whole case (§23.8, Case Study C); this is only the market maker's weekend.*

The second hand of the replay was shorter, and Ines dealt it standing up. The slide showed the close on Friday 17 March 2023, at the end of a week of heavy selling in Credit Suisse's shares and bonds, and the desk's 2023 blotter: a few lots of the bank's additional tier 1 notes, bought from clients who had been selling all week *(illustrative)*. "It's 4:59," she said. "The next bid anyone asks you for is Monday. What's $A$?"

"Zero," Kaz said. "Nobody sends an RFQ on a Saturday." Kaz pulled the GLFT engine of §18.5 onto the big screen and set the arrival rate to zero for sixty hours. The knocking rate $\eta$ is proportional to $A$, so it went to zero with it; the spectral gap $2\sqrt{\alpha\eta}$ closed; the effective horizon went to infinity; and the skew per lot in (18.6), which grows like $1/\sqrt{A}$, ran off the top of the chart. "The stationary dealer says anything you carry into Saturday you carry forever," Kaz said. "It wants to be flat at five and would pay nearly any price to get there."

"Would it be right?"

"It's a diffusion model with no clock. It doesn't know what happens on a weekend. It just knows nobody will be there."

Theo had the prospectus open, because of course he did, and he had found the clause before anyone asked. "The notes can be written down in full if the regulator decides the bank needs extraordinary public support to stay solvent. They call it a Viability Event." He scrolled. "Written down. Not converted into shares. Down."

"Is a viability event a biology term?" Kaz asked.

"It's the moment the bank stops being viable without the government," Theo said. "And it doesn't say anything about what the shareholders get. That's the part I'd want a lawyer for."

"Cards," Ines said. *Write one thing: the price at which you sell the desk's AT1s at 4:59.* Theo wrote *anything above zero.* Kaz wrote *undefined*, and then, after a moment, *see Theo.*

The tape ran forward. On Sunday 19 March 2023 UBS agreed to take over Credit Suisse, and FINMA ordered the bank's AT1 bonds, about CHF 16bn of them, written down to zero, triggered by the extraordinary government support, while shareholders received UBS shares (FINMA and UBS releases of 19 March 2023, quoted in §23.8; Basel Committee on Banking Supervision, *Report on the 2023 banking turmoil*, 5 Oct 2023). Bloomberg's *The Credit Edge*, recorded four days later, called it pulling the pin on \$17 billion of AT1s (23 Mar 2023). Litigation followed. A claim senior to equity received nothing while the equity received something, which is the textbook waterfall turned upside down by a paragraph in a prospectus.

In 2023, Ines said, the desk had sold half of its lots into Friday's close at a price she hated and carried the rest, because the bid for the rest was worse than her view *(illustrative)*. By Monday morning the rest was a lawsuit. "I priced the jump," she said. "I just priced it off the waterfall I assumed, not the one in the document." She looked at Theo's card for a long moment. "Anything above zero. That's the right answer, and I'd never have got a desk to agree to it at 4:59 on a Friday."

For a market maker this is the cleanest $J = $ *everything* case: the jump took the whole price, it happened on a weekend when $A = 0$, and it inverted the waterfall. In (18.7), $J$ equal to the full price makes $e^{\gamma qJ}$ enormous for any long inventory. The lesson for the GLFT dealer is (18.6): with $A \to 0$ over a weekend, the skew per lot goes to infinity. Inventory carried into a weekend is pure jump exposure, and a bond's JTD term has to be priced on the *contract's* loss distribution, not on the waterfall you assume. Theo's question, "But what does the prospectus say?", was the only input that would have moved the number in the right direction.

> **Ways This Blows Up.** (1) *Double counting the measure:* $\lambda^{\mathbb{Q}}$ from CDS used as $\lambda^{\mathbb{P}}$ in the drift charges the market's fear twice. (2) *Overflow:* $e^{\gamma qJ}$ with $q = 50$ lots, $\gamma = 0.05$, and $J = 60$ is $e^{150}$. Compute in logs, cap $|q|$ at $Q$, and treat any reservation price below recovery as a hard "no bid, call a human." (3) *A constant $\lambda$:* jumps cluster on calendar dates. A flat intensity under-charges on the call date and over-charges the other 250 days, so you lose the business you should win and win the business you should lose. (4) *Gaussian recovery:* recovery is bounded on $[0,1]$ and bimodal for first liens in LMTs (Chapter 13). Use Beta, or a mixture, and integrate the MGF numerically.

### Specification for AI Implementation

This is the chapter's core inventory engine: GLFT with jump-to-default, plus exact block reservation prices.

**The Spec You Hand the Robot.** *Vague:* "add default risk to the market maker." *What ROBO built:* it multiplied σ by 1.5. *Precise:* (a) `jtd_reservation(s, q, n, sigma, gamma, tau, lam_P, J, lam_Q)` returns the frozen-inventory reservation bid and ask for a block of `n` lots, from $\theta(q)$ in §18.6.1; $\mu = \lambda^{\mathbb{Q}}J$ when `s` is a $\mathbb{Q}$-fair composite. (b) `glft_quotes` and `glft_stationary` solve (18.8) by symmetric eigendecomposition, rescaled by the smallest eigenvalue to prevent overflow, and return bid and ask distances (points from mid) per inventory level, with NaN where $v$ is numerically untrustworthy or the inventory bound forbids a side. (c) Units must be consistent: per trading day throughout the GLFT block. (d) Sanity checks: short-horizon GLFT equals AS; long-horizon GLFT equals the ground state; the ground state matches (18.6) near $q = 0$; quotes are symmetric without jumps; jumps make the dealer less eager to buy and more eager to sell; the small-$\gamma$ expansion holds; inventory asymmetry holds; and Beta-recovery quadrature matches Monte Carlo and obeys Jensen.

Altice France showed what the diffusive model leaves out, and Credit Suisse showed what it leaves out when the answer is everything. Putting the jump into the quote is not hard on paper: one extra term in the reservation price, one extra term on the diagonal of a matrix. The trouble is that the desk needs two products from the same ingredients. A client has just asked for a bid on eight lots, and the platform timer is running. The streaming engine, meanwhile, needs a table of quotes for every inventory level from short twenty to long twenty, refreshed whenever volatility or the jump view moves. Both are linear algebra on the same parameters, and both fail quietly when the units disagree. So they share a listing.

Listing 18.4 has two halves. The first is the block pricer. `jtd_reservation` evaluates $\theta(q)$ from §18.6.1, with drift, diffusion penalty, and the jump term computed by `expm1`, falling back to the linear limit when $\gamma$ is negligible. It returns the average price per lot for buying `n` more lots, $[\theta(q+n)-\theta(q)]/n$, and for selling `n`, $[\theta(q)-\theta(q-n)]/n$. That prices the block against current inventory, not the marginal lot. `jump_mgf_beta` handles uncertain recovery by integrating $e^{uJ}$ against a Beta density, with $J = s - 100R$.

The second half is the streaming engine. `glft_matrix` builds the tridiagonal matrix of (18.8) on a grid from $-Q$ to $Q$. The diagonal carries the diffusive curvature, the drift tilt, and, if an intensity is supplied, the jump potential. The off-diagonals are $-\eta$. `glft_quotes` computes $e^{-M\tau}\mathbf 1$ by symmetric eigendecomposition, subtracting the smallest eigenvalue first so nothing overflows. `glft_stationary` takes the lowest eigenvector instead, the $\tau \to \infty$ limit. Both feed `_quotes_from_logv`, which turns log ratios of neighbouring inventories into bid and ask distances, adds the `as_greed` markup from Listing 18.3, and leaves `NaN` where the limit forbids a side or `_safe_log` finds $v$ below $10^{-12}$ of its maximum.

The tests mirror the spec. Short horizons reproduce AS, long ones match the ground state, the effective horizon comes out near 13 trading days, quotes are symmetric without jumps, and jumps push the bid away and the ask in. The 8-lot bid of 90.5716 used in §18.7 is pinned, along with the small-$\gamma$ expansion, the long-versus-short asymmetry, and quadrature against Monte Carlo, with Jensen's inequality checked.

Use the pricer for a block at one instant and the matrix for streaming quotes under a hard limit. Neither scales to thousands of bonds. The edge case that bites is `lam_Q`. Its default of zero does not mean "no credit view." It means no compensator drift, so with a $\mathbb{Q}$-fair composite you must pass $\lambda^{\mathbb{Q}}$ or the function charges the market's own expected loss a second time. Intensities must also be rates in the same time unit as $\tau$: the block test passes a horizon probability divided by the horizon, not the probability itself.

*The full listing is [Listing 18.4 in Appendix F](#code-18-4).*

## 18.7 RFQ Hit Rates and the Price of Staying at the Table

An RFQ is not a limit order book. You do not sit at a price and wait. You answer one auction and either win or lose. Replace $\Lambda(\delta)$ with a **win curve**. Let $x = s - p^b$ be the bid's distance below the composite:

$$
P(x) = \frac{1}{1 + \exp\!\big(-(\beta_0 - \beta_1 x + \boldsymbol\beta_z^{\top}\mathbf z)\big)},
$$

where $\mathbf z$ holds the number of dealers in competition, size, client tier, protocol, and time of day. It is fitted by maximum likelihood on the desk's own RFQ log, including the losses and their covers.

> **Math, Gently.** *A win curve, and a constraint that is a price.* Picture the desk's RFQ log as a scatter of wins and losses against how far below the composite each bid was. Close to the composite the desk wins often, far below it almost never, and in between the share of wins slides down an S-shaped hill. The logistic curve is the standard way to draw that hill, and $\beta_1$ sets how steep the slide is. With $\beta_0 = 0$ and $\beta_1 = 4$, a bid one point under the composite wins $1/(1+e^{4}) \approx 1.8\%$ of the time, and a bid 1.03 points under wins $1/(1+e^{4.12}) \approx 1.6\%$. *Maximum likelihood* is how the curve gets fitted: of all the S-curves you could draw, pick the one under which the desk's actual history of wins and losses would have been least surprising. Every win at a large distance and every loss at a small one is a surprise, and the fit moves $\beta_0$ and $\beta_1$ until the total surprise, minus the log of the probability the curve gave to what actually happened, is as small as it can be. The last idea is the multiplier $\nu$. Sales wants the desk to win, say, one RFQ in four from a client, or the client stops asking. That target is a constraint, and every constraint has a price: $\nu$ is the expected profit per RFQ the desk gives up to stay on the list. At $\nu = 0.05$ points the desk quotes as if each RFQ came with a five-cent coupon for turning up, which is the franchise line in the table below.

**The markup.** Equation (18.2) applies directly, because $P'/P = -\beta_1(1-P)$. For a block of $n$ lots, the utility gain from a win scales by $n$, so

$$
\text{greed}(x) = \frac{1}{\gamma n}\ln\!\Big(1 + \frac{\gamma n}{\beta_1(1-P(x))}\Big) \;\xrightarrow{\;\gamma\to0\;}\; \frac{1}{\beta_1(1-P(x))}.
$$

When winning is unlikely ($P \to 0$) this is the exponential case with $k = \beta_1$. When you are the favorite, the markup rises, because you have pricing power.

**Suspicion, conditional on winning.** Let $a_c$ be the expected *residual* markout from client tier $c$, conditional on winning. Conditioning on winning matters: you win when you are the most optimistic of $n$ dealers, which is exactly when the client's information is most likely against you (§18.9 does the arithmetic). Strip factor beta, carry, and index and ETF effects first, and count only the residual as toxicity. That is "IDO or it didn't happen," applied to markouts.

**Franchise.** Clients route flow to dealers who answer and sometimes win, so desks run a hit-ratio target $h^*$. Maximize expected profit subject to $\mathbb{E}[P] \ge h^*$, with multiplier $\nu \ge 0$. The Lagrangian adds $\nu P(x)$ to each RFQ's objective, and the first-order condition becomes

$$
x^* = d - \nu + \text{greed}(x^*), \qquad d = (s - r^b) + a_c .
$$

The hit-ratio constraint is a *subsidy*: you quote as if your reservation price were $\nu$ points better. Barzykin & Ciceri (2026), "Bond Market Making with a Hit-Ratio Target" (arXiv 2604.20406), formalize this on a size ladder. "Dualizing the hit ratio target term" keeps the HJB separable, and the linearized quotes decompose into "riskless spread, inventory-risk correction, and hit-ratio correction." Niang (2026), "Quality-Adjusted Hit-Ratio Targeting in Corporate Bond Market Making" (arXiv 2605.30643), shows in synthetic simulations that *raw* hit-ratio targeting subsidizes toxic flow, and replaces it with a hit ratio adjusted for residual quality. The quotes then gain a credit-alpha skew and a residual-toxicity charge.

The hit ratio arrived on Ines's desk the way most constraints do, as an e-mail from sales. One of the desk's larger asset-manager clients had noticed that the desk won 9% of its RFQs, against what the client called a street average of 20%, and it was "reviewing its dealer panel" *(illustrative)*. Theo, who had once spent a week negotiating a consent fee, recognised a negotiation. Kaz recognised a constraint. "Give me a target and I'll give you a $\nu$."

"Give it a raw target," Theo said, "and it will find the cheapest way to win."

"Which is?"

"The RFQs nobody else wants." He already had the hand history up, sorted by client tier and residual markout. The desk's losses with that client were mostly RFQs that later moved against whoever won them; its wins were mostly fills whose markouts were flat. A raw hit-ratio subsidy pays the same $\nu$ on every RFQ, so it raises the win rate fastest exactly where the other dealers are shading hardest, in the tiers whose flow knows something. That is Niang's point, and Kaz showed it on the desk's own tiers by running the last block of Listing 18.5's tests on the real log instead of the synthetic one. The shape was the same: $\nu$ paid everywhere bought hit ratio and paid for it in markouts, while $\nu$ withheld from the toxic tier bought less hit ratio and kept the money. Ines set $\nu = 0.05$ for the client's index and rebalancing flow and zero for its event-driven sleeve, then answered sales with a note that used the phrase *quality-adjusted* three times. "Tell them we answer everything," she said, "and we win the hands we should."

**The market maker's equation.** Putting §18.4–§18.7 together, the bid on a client-sell RFQ of $n$ lots is

$$
p^{b} = s
- \underbrace{(\lambda^{\mathbb{P}}-\lambda^{\mathbb{Q}})J\tau}_{\text{credit view}}
- \underbrace{\big[(s - r^b_n) - (\lambda^{\mathbb{P}}-\lambda^{\mathbb{Q}})J\tau\big]}_{\text{fear (diffusive + jump)}}
- \underbrace{a_c}_{\text{suspicion}}
- \underbrace{\tfrac{1}{\gamma n}\ln\!\big(1 + \tfrac{\gamma n}{\beta_1(1-P)}\big)}_{\text{greed}}
+ \underbrace{\nu}_{\text{franchise}}, \tag{18.9}
$$

with $r^b_n = [\theta(q+n) - \theta(q)]/n$ from §18.6. The result is then rounded to the tick, because the guild insists.

**The cold open, solved.** Take $s = 91.25$, $q = 3$, $n = 8$, $\sigma = 8$, $\gamma = 0.005$, $\tau = 5/252$, $J = 20$, $\lambda^{\mathbb{P}}\tau = 0.025$ (Theo's read of the noon call), $\lambda^{\mathbb{Q}}\tau = 0.02$, $a_c = 0.15$, $\nu = 0.05$, $\beta_0 = 0$, $\beta_1 = 4$ *(all illustrative)*.

| Term | Points | Comment |
| :--- | ---: | :--- |
| Credit view | 0.10 | $(0.025-0.02)\times 20$ |
| Fear | 0.58 | 0.04 diffusive (block of 8, not 1) + 0.53 jump premium |
| Suspicion | 0.15 | residual markout, this client, pre-call |
| Greed | 0.25 | win probability ≈ 1.6% |
| Franchise | −0.05 | hit-ratio subsidy |
| **Bid** | **90.22 → 90.25** | Ines's number |

Kaz's 90.875 priced 0.355 points of the 1.03 points. Ines priced all of it, rounded to the eighth. Figure 18.5 draws the same five terms.

![Figure 18.5: Ines's bid is five charges stacked below the 91.25 composite (credit view 0.10, fear 0.58, suspicion 0.15, greed 0.25, franchise −0.05, total 1.03). Kaz's quote of 90.875 sat only 0.375 below the composite (his model's unrounded bid, 90.8947, was 0.355 below), so it would have beaten the 90.50 cover and won the trade; Ines's 90.22 wins about 1.6% of the time. Illustrative: Equation (18.9) evaluated with the parameters of the cold-open worked example in §18.7.](assets/figures/ch18_cold_open_bid_waterfall.png)

> **Poker Table: Ines's hand history.** The bond printed 86 twenty minutes later. *Kaz's 90.875* would have beaten the 90.50 cover and bought \$8mm at a markout of −4.875 points: **−\$390,000**. *The 90.50 cover* won and paid −\$360,000. *Ines's 90.25* lost and paid nothing. "Losing that hand was the best trade of the day," she says. "The equation said we'd win one time in sixty. The table said someone else wanted to pay for the lesson. Let them."

Ines's desk is not the only kind of player at that table, and the others read the same win curve from different chairs.

> **View From Another Seat.** *The electronic market maker, in its own published words.* Jane Street describes its fixed income business as "trading more than \$900 billion with clients globally in 2025," pricing "more than 25,000 bonds," and calls itself "a consistent fixed income liquidity provider for clients in all market environments" (janestreet.com, firm pages, fetched 18 Oct 2026). The reading that follows is ours, not the firm's. A shop that also makes markets in HYG, in CDX and in issuers' equity does not see a bond RFQ the way Ines does. It sees one leg of a basket with a cheap hedge and a cheap exit next door, so its inventory fear is small and its win curve steep: it can quote tight and small, win often, and live on a greed term squeezed close to nothing. The term the basket cannot hedge is the jump. When a model sees a jump-to-default rather than a diffusion, an ETF hedge stops being a hedge, and in this section's terms the seat's $\beta_1$ falls exactly when $J$ appears. For Ines's desk the point is less about matching that seat on every RFQ than about recognising it at the table: in a quiet market it raises $\beta_1$ and pushes everyone's greed toward zero, and the RFQs it declines to win are information too.

### Specification for AI Implementation (win curve, hit-ratio dual, quote assembly)

The table above is one RFQ, solved by hand over a page. The desk gets thousands a day, each with its own size, client, and distance to the composite, and each needs an answer inside the platform's timer. Three pieces have to be automated, and they lean on each other. The win curve must be fitted from the desk's own log. The quote must be solved against that fitted curve, not the textbook exponential. And the hit-ratio target that sales keeps asking about must be enforced without handing free money to the clients who know the most.

Listing 18.5 builds this in four steps. `win_prob` is the logistic curve of §18.7 in the distance `x`, composite minus bid in points. `fit_win_curve` estimates its two coefficients by maximum likelihood on the RFQ log, writing the negative log likelihood with `logaddexp` for numerical stability and handing it to BFGS. `markup` is equation (18.2) for this curve and a block of $n$ lots, with the $\gamma \to 0$ limit built in. Because the markup depends on the win probability, which depends on the distance, `optimal_distance` solves the fixed point $x = d - \nu + \text{markup}(x)$ by bisection, over arrays of RFQs at once. The markup falls as $x$ rises, so the root is unique.

`rfq_bid` then assembles (18.9). It takes the block reservation bid from Listing 18.4, computes the credit view as $(\lambda^{\mathbb{P}}-\lambda^{\mathbb{Q}})J\tau$, calls the rest of the gap between mid and reservation price fear, adds the suspicion charge to the distance, solves for $x$, and returns the five terms, the bid, the tick-rounded bid, and the probability of winning.

The tests make three claims. A fit on 20,000 simulated RFQs recovers the planted coefficients, 0.3 and 4.0. The cold open comes out at 90.219, rounds to 90.25, wins under 3 percent of the time, and its five terms sum exactly to mid minus bid. The last block is Niang's argument in miniature. In a 4,000-RFQ book with 30 percent toxic flow, one multiplier is tuned so that the raw hit ratio is exactly 25 percent. Then the subsidy is removed on the toxic flow only. Clean flow is priced identically, expected margin over the reservation price rises, and the toxic share of wins falls, though the overall hit ratio lands below 25 percent. That shortfall is the price of not paying for information.

The first time Kaz fitted the curve on the desk's real log, the intercept came back at 41 and still climbing *(illustrative)*. The log had been exported from the trade blotter, which records fills and only fills, so `won` was one on every row; the likelihood had no maximum, and BFGS marched the intercept toward infinity without complaint. Perfect separation by distance does the same thing more quietly. `fit_win_curve` assumes both outcomes appear, and nothing in the listing checks that they do or that the fitted slope is positive; the caller has to, and the fit belongs to one segment at a time (dealer count, size, client tier), never to the whole log at once.

*The full listing is [Listing 18.5 in Appendix F](#code-18-5).*

> **Trend Watch: the auto-quoting arms race (2021–2026).** *What changed:* the RFQ win curve is now fitted by machines on both sides. *How big:* Tradeweb says AiEX now handles a large and rising share of its institutional trades *(share not independently verified; Tradeweb 10-K, FY2025)*. MarketAxess dealer algorithmic responses rose from 32.5m (2023) to 40.9m (2024), and the number of clients using automated solutions went 204, 245, 261 over 2023–25 (MarketAxess 10-Ks). Coalition Greenwich (June 2024) put about 30% of dealer volume at no human touch, 57% at top-tier dealers and 70% at non-bank LPs, on about 30,000 inquiries a day (as summarized in our Chapter 3 brief). Trumid executed 88% of eligible RFQ line items fully no-touch in September 2025 (The DESK, 2025-10-08). A Q3-2024 Barclays survey found 60% of credit participants using auto-execution, up from 40% (The DESK, 2025-01-16). In October 2026, Vanguard reported about 70% of traded volume automated but nothing sent without a trader, while buy-side traders said ELPs "help mainly in normal markets" (The DESK, October 2026). Citadel Securities proposed LP reliability metrics (non-quote rates, market share, execution cost savings, hit rates, risk executed) and self-reported a 14.2% share of IG block risk transfer (The DESK, 2026-10-08; self-reported). *What it means:* competition raises $\beta_1$, so greed falls. In stress, auto-quoters switch to wider parameters or switch off, $\beta_1$ collapses, and greed returns, along with the 64% spread spike of March 2026 (§18.2). Hit rate, the metric Citadel wants published, is exactly the variable Niang warns you not to target raw.

## 18.8 Decoding TRACE

TRACE is not a tape. It is a censored, lagged, double-counted ledger with a rulebook, and the rulebook is data. Before anyone on a trading desk reads a TRACE print, somebody in operations has usually already argued with it.

> **Quant-Shop Life: the fifteen-minute clock.** *A fictional composite: the operations and compliance row of a bank's credit-trading desk, and an analyst, Marisol Ochoa, invented for this box. The rules and their quoted wording are FINRA's.* At 8:02 on a Tuesday, Marisol's TRACE exception queue held eleven items, which is a good day. FINRA Rule 6730 gives a dealer "as soon as practicable, but no later than within 15 minutes of the Time of Execution" to report a trade; a trade done before 8:00 a.m. Eastern or in the last fifteen minutes of the session rolls to after the next open; anything reported later goes in as an "as/of." Item one was a riskless-principal trade reported as principal, because a trader had picked the wrong line from a drop-down; capacity is a required field, so she cancelled and corrected it, and the correction went out with a new message sequence number pointing at the old one. Item four was a trade executed at 3:44 p.m. whose ticket had been keyed at 4:03, nineteen minutes later, so it had gone out as an as/of. She wrote the late-report note, because the rule says that "a pattern or practice of late reporting" can be a violation of Rule 2010, and patterns begin life as notes. Items five through eleven were price typos, each corrected inside the window. By ten the queue was empty and stayed that way until lunch. The afternoon belonged to the quarterly best-execution pack. FINRA Rule 5310 asks a firm that does not review every order to conduct "regular and rigorous" reviews, "at a minimum ... quarterly," security by security and by type of order, and her pack was built from the same RFQ log the traders used for their hit-ratio dashboard: the desk's quote, the cover, the winning price, and where the bond traded one, five and twenty days later, by client tier. Her manager's only question, at 5:40, was why this quarter's average cost to clients was different from last quarter's. The answer, after an hour, was that the composite vendor had changed its methodology in the second month. Nobody outside her row ever saw the queue or the pack, and every quant who later back-tested a flow signal on that desk's prints inherited both. Each cancel and correction she filed is a row the decoder below has to apply in the right order; each as/of is a print whose timestamp says less about when the market knew than it appears to. And the best-execution pack is a markout study with a compliance cover sheet: the same log, the same horizons, the question of §18.3, answered for a regulator instead of for the P&L.

Theo read the rulebook itself on a Tuesday of his own, the way he used to read a credit agreement, definitions first, and it read like one. Rule 6750 decides what prints at all: TRACE-eligible transactions, 144A included, are disseminated "immediately upon receipt," with listed exclusions such as affiliate-principal-indicator trades and list or fixed-offering-price transactions. The size field is censored. Anything over \$5mm in investment grade or \$1mm in high yield shows as "5MM+" or "1MM+", and the uncapped sizes reach the Historic Corporate Bond Data Set only "six months after the calendar quarter in which the transactions are reported" (Regulatory Notice 25-17). The clock is the one Marisol lives by: the 15-minute outer limit survives, because FINRA is "not moving forward" with one-minute reporting (RN 25-17). Then the flags, which are where the rulebook has been busiest. The portfolio-trade modifier has been mandatory since 15 May 2023 (RN 22-12). Optional aggregate allocation reports started on 8 June 2026 (RN 25-17). The expanded affiliate indicator is voluntary from 31 August 2026 and mandatory from 2 August 2027 (RN 26-16), because duplicate affiliate prints inflated US HG volume by up to 8% in June 2026 (MarketAxess Q2-2026 release). Last came the dataset researchers use. Academic TRACE masks dealer identities but keeps them consistent, which is what lets anyone study dealer inventories at all. "It's an indenture," Theo told Kaz. "Every defined term is somebody's old argument."

> **[SOURCE EXTRACTION]** *Ben_Dor_Quantitative_Credit_Portfolio_Management p.364, n.8:* "TRACE truncates the sizes of large transactions at \$1 million and \$5 million for high-yield and investment-grade bonds, respectively"
>
> **Annotation.** Our analysis: the footnote goes on to impute the average true size of capped prints by matching aggregate volume, about \$4mm for HY and \$12.5mm for IG, and to drop trades under \$100k to focus on institutions. Two lessons follow for 2026. First, the cap is a feature, not just a nuisance: a "1MM+" print in a HY bond is a block indicator, and blocks are where Kyle's $\lambda^{K}$ lives. Second, any real-time imbalance computed on capped sizes understates block flow. Carry a capped-share feature, and rebuild the uncapped history quarterly once FINRA's six-month lag expires. The caps in the footnote are the same caps in force in 2026.

**Pipeline.** The decoder follows the rulebook in order. Cancels and corrections are applied by message sequence; one leg of each interdealer trade is kept; capped sizes, portfolio-trade prints and ATS prints are flagged; and each bond gets a row of features: customer imbalance, capped share, PT share, ATS share, minutes since the last print, and the Roll-sign column Kaz added in §18.2.1. Reading informed flow then becomes concrete. In the Altice replay (§18.6.3) the features that mattered were a one-sided customer imbalance, a jump in capped share, and the run of Roll NaNs of §18.2.1.

> **Ways This Blows Up.** Corrections applied before the trades they correct; agency and riskless-principal pairs counted as two trades; affiliate duplicates counted as volume (up to 8% in June 2026); the Dick-Nielsen cleaning steps (Dick-Nielsen 2009, "Liquidity Biases in TRACE"; Dick-Nielsen 2014, "How to Clean Enhanced TRACE Data") applied to a 2026 file without the new flags; and "processed" platform volume mistaken for executed risk.

### Specification for AI Implementation (TRACE decoder)

Schema (one row per report): `msg_seq` int, `orig_msg_seq` int (−1 if none), `status` in {T, X, C}, `bond_id` str (internal id, never an invented CUSIP), `rating_class` in {IG, HY}, `minute` int, `price` float (points), `reported_qty` float (USD mm, capped), `side` in {B, S} (reporting dealer's view), `contra` in {C, D}, `ats` bool, `pt` bool.

Every shop that uses TRACE has a version of the same week: someone builds a flow feature, the volume does not tie to the vendor, and four days later the cause turns out to be a correction applied to the wrong trade, or two dealers' reports of one trade counted as two. The rulebook above is easy to read and tedious to obey, and the cost of getting it wrong is silent, because a feature built on dirty prints still looks like a number. The way to stop relitigating it is to write the decoder once, feed it a file where the right answer is known, and make it prove it can recover that answer before it touches the real feed.

Listing 18.6 does both jobs, and the test file comes first. `make_synthetic_trace` draws 400 trades across eight placeholder bonds, four IG and four HY, with lognormal sizes, a 70/30 customer-to-dealer mix, and small shares of ATS and portfolio-trade prints. It expands each trade into the reports a dealer would file: one for a customer trade, two for an interdealer trade. Sizes are capped at \$5mm for IG and \$1mm for HY. It then corrupts the file in the two ways the pipeline names. Twenty reports are duplicated by mistake, and each duplicate is followed by a cancel pointing at it. Twenty originals are mispriced by a point and followed by a correction carrying the right price.

`clean_trace` is the pipeline in four lines. It collects every message sequence number that a cancel or correction refers to, drops the cancel records and everything they referenced, and keeps the corrections as the replacements. It then keeps only the sell-side leg of interdealer trades, flags prints at the cap, and sorts by bond, minute, and sequence. `trace_features` turns the clean file into one row per bond: customer imbalance from the dealer's side flag, the capped, portfolio-trade, and ATS shares, the print count, and minutes since the last print against a 390-minute session.

The tests ask that one row survive per true trade, that prices equal the true prices, that no size exceeds its cap, and that imbalance stays between minus one and one.

Marisol's queue is the reason the listing is the skeleton of a daily decoder rather than the decoder: it passes only the messes it was taught. Dropping the buy-side leg assumes the sell-side leg is also in the file, and where it is missing the trade vanishes from volume entirely. The synthetic file has no riskless-principal pairs, no capacity errors like her item one, and no affiliate duplicates, so the equality of row counts proves the logic, not the feed. Imbalance is computed on capped sizes, so it is blind to blocks, which is why `capped_share` travels beside it.

*The full listing is [Listing 18.6 in Appendix F](#code-18-6).*

## 18.9 BWICs: First-Price Auctions With a Leaky List

A bid-wanted-in-competition is the RFQ turned inside out. The seller circulates a list, dealers and investors submit sealed bids by a deadline, the best bid wins, and the market later learns the "cover" (second-best bid) or "DNT" (did not trade). Saunders, Srinivasan & Walter (1998), in a field study of the US inter-dealer corporate bond market (NYU Stern FIN-98-089), found that trading "closely resembles a first-price sealed-bid auction," and measured competition as the gap between the best and second-best bid. Mags has a shorter version: "A BWIC is a lender call where everyone talks at once and nobody says anything."

The sealed envelope changes one thing about bidding that every dealer learns once, usually on a list they won. In an RFQ the desk loses to a better price and never finds out how wrong it was. In a BWIC the desk that wins finds out, a week later, that it was the only one at the table who liked the bond that much.

> **Math, Gently.** *The winner is the most wrong.* In 1906 Francis Galton collected about eight hundred tickets from a weight-judging contest at a Plymouth fair and found that the middle guess for the ox's dressed weight was within one percent of the truth (Galton 1907, "Vox Populi," *Nature*). Nobody wrote up the person who guessed highest, though in an auction that is the person who takes the ox home. Picture eight dealers each looking at the same bond through a slightly smudged window. Each one's read is the true value plus a private error, as often too high as too low, so each read is honest on average. The highest read is not, because it was picked for being highest, and the easiest way to be highest is to have the biggest error upward. A coin version fits in a margin. Let each bidder's error be $+1$ or $-1$ point with even odds. With two bidders the top error is $+1$ unless both coins land $-1$, which happens a quarter of the time, so the winner is on average $\tfrac34 - \tfrac14 = 0.5$ points too high. With three bidders it is $\tfrac78 - \tfrac18 = 0.75$. With eight it is $\tfrac{255}{256} - \tfrac{1}{256} \approx 0.99$, nearly the whole point, because with eight coins somebody almost always lands on $+1$. Real errors have tails rather than a ceiling, so the winner's error keeps stretching as bidders join: with normal errors of 1 point, the top of three bidders sits 0.85 above the truth on average, the top of five 1.16, the top of eight 1.42. Those three numbers are the $e_n$ of the next paragraph.

A bid, then, answers a different question from a valuation. The valuation asks what the bond is worth given what the desk sees. The bid asks what it is worth given what the desk sees *and* the news that nobody else saw as much, and the answer is the desk's read less the winner's expected error, $\sigma_\varepsilon e_n$ (Milgrom & Weber 1982, "A Theory of Auctions and Competitive Bidding"). With $\sigma_\varepsilon = 1$ point, an eight-bidder list requires about 1.4 points of shading *before* strategic shading, the further shade every first-price bidder takes because she pays her own bid rather than the next one down. The correction grows with $n$, which is why quotes get more conservative as more dealers are asked (§18.3).

#### The Full Derivation

**The winner's curse, derived.** Bidder $i$ sees a signal $x_i = V + \varepsilon_i$ with $\varepsilon_i \sim \mathcal N(0,\sigma_\varepsilon^2)$ i.i.d. and a diffuse prior on $V$. Conditional on $x_i = x$, $V \sim \mathcal N(x,\sigma_\varepsilon^2)$. Conditional also on $x_i$ being the highest of $n$ signals, the posterior density of $\varepsilon_i = x - V$ is proportional to $\phi(\varepsilon/\sigma_\varepsilon)\,\Phi(\varepsilon/\sigma_\varepsilon)^{n-1}$, which is the density of $\sigma_\varepsilon$ times the maximum of $n$ standard normals. So

$$
\mathbb{E}[V \mid x_i = x,\ i \text{ wins}] = x - \sigma_\varepsilon\, e_n, \qquad e_n = \int_{-\infty}^{\infty} z\, n\,\phi(z)\Phi(z)^{n-1}\,dz,
$$

with $e_3 \approx 0.85$, $e_5 \approx 1.16$, and $e_8 \approx 1.42$, the box's three numbers. For $n = 3$ the integral has a closed form, $3/(2\sqrt{\pi})$.

#### The leak, the reserve, and the survivors

**Leakage.** Once the list circulates, anyone who sees it is an order anticipator. If they pre-sell a fraction $\phi$ of the expected flow $Q\,p_{\text{trade}}$, Kyle's impact gives a pre-auction drift of $\Delta P = -\lambda^{K}\phi\,p_{\text{trade}}\,Q$, which the seller pays on the whole list; the replay below puts numbers on it. A DNT reveals that the reserve was above the best bid, which is a reserve-price signal. BWIC prints are survivors: in stress the bonds that fail reserves are the weak ones, so marks built from BWIC covers are biased upward precisely when it matters, and §18.9.1 shows what that does to a desk that trusts its composite.

### 18.9.1 Long Scene: The LDI BWIC Week, 27 September to 7 October 2022 (replay)

*A replay, cut off at 8:00 a.m. London on Monday 3 October 2022 and run on a Friday afternoon in October 2026. The desk's 2022 structured-credit seat, the 38-line list and its seller, every bid, size, cover and fill, and the numbers on Kaz's whiteboard are fictional and illustrative (the desk's fictional run). The mini-Budget, the Bank of England's operation, the market-wide BWIC volumes, the pattern of what traded and what did not, and the quotations are real and sourced, chiefly to TwentyFour Asset Management's note of 5 October 2022 and to Reuters. The desk was one of many dealers on the list and an outside bidder in every sense.*

Ines put dates on the first slide and nothing else, because the dates were the hand. Friday 23 September 2022: the UK government's mini-Budget, and a sell-off in long-dated gilts violent enough that within days the central bank was buying them. The days after: British pension funds running liability-driven investment (LDI) strategies, whose gilt hedges were leveraged, facing collateral calls they had to meet in cash. Wednesday 28 September: the Bank of England announcing temporary purchases of long-dated gilts, due to end on 14 October. And over the week of 26 September, more than €1.5bn of European CLO tranches listed for sale through BWICs, with close to another €1bn believed to have traded away from the broader market (TwentyFour AM, 5 Oct 2022).

"Why CLOs?" Theo asked. In October 2022 he had been at PJT, and the gilt crisis had been something he read on his phone between drafts of a cleansing deck.

"Because they were the most liquid thing those funds owned that wasn't a gilt," Ines said. "Triple-A and double-A European CLO paper, held for the spread. When the margin call comes you sell what will sell."

The second slide was the list. In 2022 the desk had kept a small structured-credit seat in London that bid CLO lists for its own book *(illustrative)*, and on the Monday morning a manager acting for a pension client had sent it, along with every other desk the manager could think of, 38 lines of European CLO tranches: eleven AAA, fifteen AA, six A, four BBB and two BB, about €300mm of face in all, bids due at 2 p.m. London on Tuesday *(illustrative)*. Each line carried the CLO manager's name, the deal's vintage, and a column the desk's system had filled in overnight: the composite, built from dealer runs and from the covers of the last few weeks' auctions.

Kaz had the spreadsheet open before Ines finished the slide. "This is the easy one. We have a composite for every line. Composite minus $\sigma_\varepsilon e_n$, eight bidders, one point of noise, round, send. Thirty-eight bids by lunch."

"Eight bidders on every line?"

"It's a big list. Everybody got it."

"Everybody got it," Ines agreed. "Did everybody want all of it?" She left the question on the table and dealt the cards.

*Pick three lines to bid. For each, write your bid against the composite, and how many bidders you think are on it.*

The reader gets a card too. The list is mostly double-A, the seller is on a margin clock, and the composites were built from last month's covers. Three lines, three shades, three guesses at $n$, before the tape runs on.

Theo took the longest. He sorted the list by yield at the composite, and the two BB lines sat at the bottom of the screen, yielding far more than anything else on it. His reasoning was a restructuring banker's: the seller was forced, forced sellers take what they are offered, and the deepest discount would be in the paper furthest from the money. He bid both BBs four points under the composite and one BBB two under, and wrote $n = 3$ beside each, "because BB is a specialist's market."

Mags read his card over his shoulder, which the replay rules did not forbid. "Cheap to what?"

"To the composite."

"And the composite is what? The last print that *traded*." She tapped the BB column. "In a week like this, the BB lines nobody wants don't print. They go back to the seller with a DNT and leave no mark. So the only BB covers in that number are the ones somebody liked. You're taking four points off a price that was flattered before you touched it."

Kaz's card had eight lines, all AAA and AA, each at the composite minus 1.42, with *$n = 8$, $\sigma_\varepsilon = 1$, see §18.9* written underneath. Mags's card had three lines, the three largest AA positions on the list, €25mm each, bid "in the 80s, whatever the coupon," and below them: *The seller isn't selling a bond. He's selling a margin call.* She had left the $n$ column blank. Asked, she wrote *everybody with a balance sheet and no gilts*.

Ines collected the cards without reading them, put them in an envelope, and ran the tape forward a day.

*Tuesday 4 October.* The selling had not stopped. That day alone about €400m of predominantly AA CLO tranches were listed through BWICs across the market (TwentyFour AM, 5 Oct 2022). On the replay's tape the desk's salesperson heard by nine that "the thirty-eight-line list" was being discussed on two other desks, and that AA paper from the same managers was being offered out of competition, below Monday's composite *(illustrative)*. TwentyFour's note caught the texture of the day in one sentence: "the cost of what liquidity there was increased every few hours as spreads were rapidly adjusted to the new situation."

Kaz had a proposal. "We own €20mm of AA from two of these managers already. If we win fifteen AA lines at two o'clock we'll be very long. Sell the twenty now, while there are bids, and then bid the list flat."

"Sell to whom?"

"Whoever's bidding."

"The same accounts who will bid this list at two," Ines said. "Look at Harris's table again. You've just moved yourself into the row called *order anticipators*. Price it."

Kaz priced it on the whiteboard, in dollars, because Listing 18.7 works in dollars and the euro was trading close to parity that week. A list of \$300mm. A probability of 0.9 that any line trades. Suppose everyone who has seen the list pre-sells, between them, a fraction $\phi = 0.3$ of the flow they expect it to release, into a market whose Kyle $\lambda^K$ is 0.5 points per \$100mm. The pre-auction drift is

$$
\Delta P = -\lambda^{K}\phi\,p_{\text{trade}}\,Q = -\frac{0.5}{100}\times 0.3\times 0.9\times 300 = -0.405 \text{ points},
$$

and because the drift lands on every line, the seller pays about \$1.215mm *(illustrative)* before a single envelope is opened.

Theo read it twice. "So the leak is a fee the pension fund pays to everyone who read its list."

"And your pre-hedge," Ines said to Kaz, "is us collecting a share of that fee from a client whose list we're about to bid, by selling into the same bids that will set our cover." She drew a line under the 0.405. "This is the seller's dilemma. Send the list to three desks and you get three envelopes and a fat $e_n$-sized discount from each of them. Send it to thirty and you get competition, and you pay this. The manager chose thirty. In that week I'd have chosen thirty too."

Kaz crossed out the pre-hedge. Mags said, to nobody in particular, "Back in my day a BWIC was a fax with a deadline, and the leak was whoever stood next to the fax machine." Then, after a moment: "It was cheaper. It wasn't better."

*Two o'clock.* Ines opened the envelope she had sealed in 2022. It held the desk's results on the list, and a printout of the TwentyFour note from the next morning, Wednesday 5 October. The note set out the market-wide pattern: almost all AAA and AA CLO bonds that were auctioned traded, a large number of BBs and Bs did not meet reserves, and "however high the coupon was on a AA bond, the cash price bid would likely still be in the 80s." The desk's own list had done what the market did *(illustrative)*. All eleven AAA lines traded, covering within half a point of Monday's composite, mostly, the 2022 salesperson's notes said, to bank treasuries. Fourteen of the fifteen AA lines traded, between 82 and 87, two to four points below the composite. Both BBs came back DNT.

Ines graded Kaz first, because Kaz's card was the cleanest piece of mathematics in the envelope and the most instructive way to lose money. On the AAA lines, a crowd of bidders had agreed on value to within a quarter of a point. With $\sigma_\varepsilon$ near 0.25 the honest shade for eight bidders was about 0.36 points, so Kaz's 1.42 left every AAA line to someone else by a point. On the AA lines the problem ran the other way. Kaz's bids at composite minus 1.42 would have been the best bids on four of them, a point and a half above the covers. "You'd have won," Ines said. "Congratulations. Now tell me what the second-best bidder knew."

"That the composite was stale," Kaz said slowly. "It was built from covers before the repricing. That isn't private noise. Everybody's composite was wrong by the same amount. Shading by $e_n$ fixes the error that's *mine*. It does nothing for the error that's *ours*."

"Which is why the curse has two halves," Ines said. "The half the integral handles, and the half where everybody in the room is using last week's price."

Theo's BBs had failed reserve, and he had expected to be told he had been lucky. Ines read the DNT another way. "A DNT is a price. It says the seller's reserve sat above the best bid, yours included. Your forced seller wasn't forced on the BBs. He was forced on the paper that would clear, which was the senior paper. The reserve tells you which part of the list is the margin call." Theo wrote that on the back of his card, under the four points he would have lost on a flattering composite if the reserve had not saved him from himself.

Mags had bid where the seller was forced, in size, at a price set by the seller's clock rather than by Monday's mark. Her three AA lines would have won two at 84 and 85 and been covered on the third *(illustrative)*. TwentyFour's note reported that dealers were already seeing better execution and broader client engagement, and its author read that as a sign valuations had bottomed for now. Six weeks later Reuters reported that the biggest discounts had come at the height of the LDI crisis and that prices on the tranches had since recovered somewhat (Reuters, 18 Nov 2022). Mags accepted the grade with the expression of someone who had been right about forced sellers before and had not enjoyed it then either.

If your three lines were AA, your $n$ was large and your shade came from the seller's clock rather than the composite, you bid the way that market cleared. If you went to the bottom of the list for value, you sat in Theo's chair, and the reserve did you the favor it did him. If you shaded every line by the same amount, you were Kaz, and you were careful, and the care was spent on the wrong error.

Ines finished the replay by opening the franchise line of (18.9), the $\nu$ that §18.7 set for a client's index flow, and setting it for a new tier the desk's system had never had: *forced seller, exogenous clock*. "Positive," she said. "A seller who's selling because of a gilt knows nothing about the loans inside a CLO, so $a_c$ is about zero. And the manager who sent this list will send another one next year and remember who bid in the week it mattered."

"Why subsidize a seller at all?" Theo asked. "That's money."

"It costs us the $\nu$. Pay the same $\nu$ to an Altice co-op member on the morning of the call and it costs us the bond. A utilitarian seller deserves a subsidy and an informed one deserves a charge, and the only hard part of the job is telling them apart before two o'clock."

> **View From Another Seat.** *The buyers' side of the same week: a CLO investor, and an insurer.* TwentyFour Asset Management, a fixed-income manager that invests in European CLOs, published its read of the week on 5 October 2022, while the selling was still going on (Aza Teeuwen, "Where are CLOs trading after the Truss Tantrum?"). Its account of who was buying is a census of balance sheets without a gilt clock: "mostly US investors seeing value in European CLOs," hedge funds "using cheap leverage for IG assets," "bank treasuries for AAAs," and European insurance companies "reportedly becoming more active at these levels." The note also saw the spread tiering between the best- and worst-regarded CLO managers widen, longer deals widen more than shorter ones, and BBB tranches yield "almost 10% in euros," nearly what CLO equity had yielded at the start of that year. Six weeks later Reuters reported that Apollo's co-president Scott Kleinman had put CLO trading volume during the crisis at 800% above average levels, and that Athene, Apollo's annuities business, had bought \$1.1 billion of AAA and AA CLO tranches (Reuters, Nell Mackenzie, 18 Nov 2022). Seen from an insurer's chair, the list that was a margin call to its seller was a rare offer: senior, rated, floating-rate paper at a cash price in the 80s, sold by someone who needed cash rather than someone who knew something. The insurer in §18.1's table is a utilitarian *seller* of fallen angels. In October 2022 a balance sheet of the same kind was the patient buyer, because the seller across the table had a collateral call and it had none. Which row of Harris's table a firm sits in depends on its liabilities that week more than on its views. For a dealer bidding the same list, it meant that the toughest competition on the senior lines came from buyers with no inventory limit and no 4 p.m.

*Autopsy.* The beats priced the hand; the autopsy asks what a machine could have seen before the list arrived. The gilt sell-off and the stress in credit ETFs were public before the first list landed, and both said the same thing: sellers with an exogenous clock. A systematic desk reading them as a regime switch would have set the tier's $a_c$ near zero and its $\nu$ above zero before Monday, widened the $\sigma_\varepsilon$ it assumed on junior lines, and marked down its confidence in every composite built from covers. Leakage was enormous all week, because every list told the street that more lists were coming, so each seller paid the drift for the sellers behind it as well as for itself.

> **Trend Watch: BWIC supply, 2021–2026.** *2021:* total BWIC volume averaged \$5.2bn a quarter; *Q2-2022:* \$6.8bn, with CLOs 55% of volume (TwentyFour AM, 2022-07-11). *Late September 2022:* the UK mini-Budget triggered the gilt and LDI crisis, and the Bank of England began temporary long-gilt purchases on 28 September. *The following week:* more than €1.5bn of CLOs were listed via BWICs, with perhaps another €1bn traded away from the broader market; one Tuesday alone saw about €400m listed, predominantly AA. "Sales over the past week-and-a-half could exceed the previous three months combined." Almost all AAA and AA paper traded, while many BB and B bonds "didn't meet reserves." AA cash prices were "in the 80s," and some sellers "seemed to have no choice but to sell in order to meet liquidity needs" (TwentyFour AM, 2022-10-05). *2025–2026:* 9fin (2025-12-02) reported an insurer listing more than \$1bn of triple-A US CLOs in a single BWIC, and SCI (2026-02-16) headlined a \$56bn twelve-month US BSL CLO BWIC total led by triple-A supply *(headline-level figures; the twelve-month window was not verified)*. *What it means:* the BWIC is now a primary liquidity venue for structured credit, and its leak rate is a cost line.

### Specification for AI Implementation (BWIC shading and leakage)

The shading constant $e_n$ and the leakage bill are the two numbers a BWIC desk wants on screen before it bids, and neither deserves trust until it has been checked against something other than itself. Listing 18.7 integrates the expected maximum of $n$ standard normals numerically and tests it against the closed form $3/(2\sqrt{\pi})$ for three bidders and a Monte Carlo draw for eight, then computes the pre-auction drift and the seller's cost, reproducing the \$300mm example above to the decimal (0.405 points, \$1.215mm).

*The full listing is [Listing 18.7 in Appendix F](#code-18-7).*

## 18.10 Desk Debrief

**Finder.** One row per tool: where its equation lives, the picture that explains it, the scene where it worked or broke, and its listing.

| Concept | Equation | Intuition (box) | Judgment (scene) | Code |
| :--- | :--- | :--- | :--- | :--- |
| Roll's effective spread | $S = 2\sqrt{-\text{Cov}(\Delta p_t,\Delta p_{t-1})}$, §18.2.1 | A ball between two walls (§18.2) | The NaN on Altice France's secured notes, three sessions running (§18.2.1) | [Listing 18.1](#code-18-1) |
| Kyle's $\lambda^K$ | $\lambda^K = \text{Cov}(v,y)/\text{Var}(y) = \tfrac12\sigma_v/\sigma_u$, §18.3.2 | The best guess is a straight line (§18.3.2) | Ines's napkin and Theo's first markout study of the Halvorsen seller (§18.3.3) | [Listing 18.2](#code-18-2) |
| AS spread: fear and greed | (18.1)–(18.4), §18.4 | A wobble in points and a phone that rings less; fear as a number; the exponential of a wobble; $\ln(1+x) \approx x$ (§18.4) | The cold open's 90.875, and the 9:31 page (§18.4.4) | [Listing 18.3](#code-18-3) |
| GLFT effective horizon | (18.5)–(18.6), $\tau_{\text{eff}} = 1/(2\sqrt{\alpha\eta})$, §18.5 | A marble in a bowl (§18.5) | The Credit Suisse AT1 weekend, when $A = 0$ (§18.6.3) | [Listing 18.4](#code-18-4) |
| JTD reservation price | (18.7)–(18.8), §18.6 | The jump's exponential, part one (§18.6) | Altice France, two RFQs forty minutes apart (§18.6.3) | [Listing 18.4](#code-18-4) |
| $\mathbb{P}$ versus $\mathbb{Q}$, charged once | $(\lambda^{\mathbb{P}}-\lambda^{\mathbb{Q}})J\tau$ in (18.9), §18.6–§18.7 | Whose odds you are using, part two (§18.6) | Altice's 1.47 points of credit view (§18.6.3); the RSSG bridge (§18.6.2) | [Listing 18.5](#code-18-5) |
| Win curve and the franchise $\nu$ | Logistic $P(x)$ and $x^* = d - \nu + \text{greed}(x^*)$, §18.7 | A win curve, and a constraint that is a price (§18.7) | The panel-review e-mail (§18.7); the forced-seller tier (§18.9.1) | [Listing 18.5](#code-18-5) |
| TRACE caps and flags | No equation: "5MM+" and "1MM+" caps, the 15-minute clock, the flags, §18.8 | The fifteen-minute clock (Quant-Shop Life, §18.8) | Theo's Tuesday with the rulebook (§18.8) | [Listing 18.6](#code-18-6) |
| Winner's curse and leakage | $x - \sigma_\varepsilon e_n$; $\Delta P = -\lambda^K\phi\,p_{\text{trade}}\,Q$, §18.9 | The winner is the most wrong (§18.9) | The LDI BWIC week (§18.9.1) | [Listing 18.7](#code-18-7) |

The bullets below are the same chapter with the scenes taken out, short enough to tape to a monitor.

- **A quote is five numbers, not one:** credit view, fear, suspicion, greed, and franchise. Equation (18.9) on one line. If you can't name all five, you priced one.
- **In bonds, diffusive fear is pennies.** The AS spread is mostly greed, $\tfrac2\gamma\ln(1+\gamma/k) \to 2/k$. The real fear is the jump term $\lambda^{\mathbb{P}}J^2$ and the factor $e^{\gamma qJ}$.
- **Charge the jump once.** Use $(\lambda^{\mathbb{P}} - \lambda^{\mathbb{Q}})J\tau$ against a $\mathbb{Q}$-fair composite, and $\lambda^{\mathbb{P}}$ for the variance. A CDS-implied $\lambda$ in the drift charges the market's fear twice.
- **There is no 4 p.m. in credit.** Use the stationary GLFT dealer. Its effective horizon is the inverse spectral gap, it shrinks like $A^{-1/2}$, and it goes to infinity on Friday night.
- **Roll returning NaN is information.** A positive autocovariance means split orders or informed drift. Never take an absolute value.
- **Hit ratios are a subsidy, and raw ones subsidize the wrong people.** Target quality-adjusted hit ratios on residual markouts. IDO or it didn't happen.
- **TRACE's censoring is the signal.** "5MM+" and "1MM+" are block flags; the six-month uncapped release is your quarterly recalibration.
- **A BWIC is a first-price auction with a leak.** Shade by $\sigma_\varepsilon e_n$, price the leak with $\lambda^{K}$, and distrust survivor marks.

**The Spec You Hand the Robot.** *Vague:* "Build an RFQ auto-quoter." *What ROBO built:* it maximized the hit ratio, bid par for everything, and owned the bond market by Thursday. *Precise:* Build `rfq_engine.quote(rfq, state) -> Quote`. **Inputs:** `rfq` = {bond_id, side, size_lots, n_dealers, client_tier, protocol, timer_s}; `state` = {composite_mid (points, $\mathbb{Q}$-fair), inventory_lots, sigma_pts_per_sqrt_yr (20-day $\mathbb{P}$ forecast), gamma_per_pt_lot, holding_tau_yr, lam_P_per_yr (baseline + event calendar × PRS), lam_Q_per_yr (CDS/composite-implied), jump_pts or recovery Beta(a, b), a_tox_pts[client_tier] (residual markout conditional on win), win-curve coefficients, nu_pts[client_tier] (quality-adjusted hit-ratio dual), tick}. **Computation:** block reservation price from $\theta(q)$ (§18.6) in logs; the markup from (18.2) with the logistic curve; the five terms of (18.9); round to tick. **Guards:** no quote if the reservation price is below recovery or $|q + n| > Q$; clip to composite ± band; widen or stop when the stress regime is on (ETF discount z-score, bid–ask percentile); stop a session when realized markouts breach 3σ of their forecast. **Logs (the hand history):** every term, $P(\text{win})$, the cover when lost, and 1/5/20-day IDO markouts. **Tests:** the asserts in this chapter, plus one that raw hit-ratio targeting fails on a synthetic toxic tier.

### Exercises

1. *(Warm-up)* Show that $\tfrac1\gamma\ln(1+\gamma/k) \to 1/k$ as $\gamma \to 0$, and that $1/k$ maximizes $\delta Ae^{-k\delta}$. Explain to Kaz why a risk-neutral dealer still has a spread.
2. *(Stretch)* Re-derive (18.7) with $J = s - 100R$, $R \sim \text{Beta}(a,b)$. Show that the MGF $M_J(\gamma q)$ replaces $e^{\gamma qJ}$, and use Jensen to sign the effect of recovery uncertainty on the bid.
3. *(Core, data)* On a TRACE extract with "5MM+" caps, estimate the Roll spread by size bucket ($<$\$100k, \$100k–\$1mm, \$1–5mm, capped). Which buckets return NaN, and why does order splitting make the capped bucket's estimate *too small*?
4. *(Core)* Compute the winner's-curse shading for a 3-dealer versus an 8-dealer BWIC with $\sigma_\varepsilon = 0.75$ points. Then argue whether the *equilibrium* bid rises or falls with $n$.
5. *(Warm-up)* ROBO has been told to "maximize the hit ratio." Describe its inventory one week later, its markouts, and the email from risk. Then write the one-line constraint that fixes it.
6. *(Stretch, code)* Using `glft_stationary`, find the $A$ at which a dealer's stationary skew per lot equals the AS skew with a one-week horizon. Interpret the answer as "how often must this bond be asked about for AS to be right?"

### Deep-Dive Resource Graph

**Podcasts**
- **"What We Can Learn About Market Liquidity By Looking At Everyday Life"** (*Odd Lots*, 2017-10-09). Karthik Shashidhar, author of *Between The Buyer And The Seller*, frames liquidity as the ability to transact without moving the price and asks why it sometimes evaporates with little notice, using Uber and dating-app matching: a non-credit opener for §18.1 and §18.3 (the spread as a price for being picked off). https://omny.fm/shows/odd-lots/what-we-can-learn-about-market-liquidity-by-lookin
- **"Thao Tran: Market Making Illiquid, Non-Fungible Assets (S7E14)"** (*Flirting with Models*, 2025-02-03). Inventory risk and the features that drive spreads when every unit is unique, the closest public analogue to quoting an off-the-run bond; an analogy, not credit, so read it beside §18.4. https://www.flirtingwithmodels.com/episodes/eNEcTaLcPCU
- **"Toby Nangle on What We Just Learned From Gilt Market Madness"** (*Odd Lots*, 2022-10-06). Gilts and sterling moved once-in-a-generation distances after the mini-budget and rebounded after the Bank of England stepped in: a forced-seller schedule meeting a backstop in real time, the market behind the LDI BWIC week of §18.9.1. https://omny.fm/shows/odd-lots/toby-nangle-on-what-we-just-learned-from-gilt-mark
- **"Swiss AT1 Bond Carnage, Leisure Sector Risk"** (*The Credit Edge*, 2023-03-23). Recorded four days after the UBS takeover, with Bloomberg News's account of the $17 billion AT1 write-down: the real-time version of the $J$ = everything case in §18.6.3. https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/swiss-at1-bond-carnage-leisure-sector-risk
- **"Jeremy Maletz"** (*Money Stuff: The Podcast*, 2026-10-09). Susquehanna's head of prediction markets on flow versus bespoke trading and adverse selection: a market maker explaining why a quote is a posterior about who is on the other side (§18.3, §18.9). https://omny.fm/shows/money-stuff-the-podcast/jeremy-maletz

**Practitioner Writing**
- **"How Does Information Affect Liquidity in Over-the-Counter Markets?"** (NY Fed *Liberty Street Economics*, Michael Lee and Antoine Martin, 2020-01-13). A short read on dealers facing two impediments, informed traders and the balance-sheet cost of holding inventory: the Glosten–Milgrom half is §18.3, the inventory-cost half is the $\gamma$ term of §18.4. https://libertystreeteconomics.newyorkfed.org/2020/01/how-does-information-affect-liquidity-in-over-the-counter-markets/
- **"Guide to the Avellaneda & Stoikov Strategy"** (Hummingbot, 2021-04-13). Walks the reservation-price and optimal-spread formulas with risk aversion $\gamma$ and order-book liquidity $\kappa$ as an open-source bot implements them (limit-order-book setting, not RFQ, the book's own point in §18.4.4); shows what an implementer must parameterize before the AI-specification box. https://hummingbot.org/blog/guide-to-the-avellaneda--stoikov-strategy/
- **"Electronic trading in fixed income markets"** (BIS Markets Committee Papers No. 7, Study Group chaired by Joachim Nagel, 2016-01-21). The central-bank baseline for the RFQ-versus-CLOB framing of §18.1 and §18.7: electronic trading tends to improve market quality "with exceptions," and liquidity may have become less robust (50 pages; read the executive summary). https://www.bis.org/publications/electronic-trading-fixed-income-markets
- **"Overnight Corporate Bond Trading"** (The Microstructure Exchange webinar, Farshid Abdi with Marco Rossi and Botao Wu, 2026-09-15). Trades between 6:30 p.m. and 8:00 a.m. are not disseminated on TRACE until the next morning, are larger, move prices more persistently and predict returns on the issuer's other bonds: a new latency-and-information fact for §18.8 and §18.3; the season page links the recording and the paper. https://microstructure.exchange/season
- The DESK: "Dealers struggle to unpick impact of runs sent to rivals" (2023-12-07); "Measuring implicit costs and market impact in credit trading" (2024-10-23); "IG credit dealers go short before Fed cuts" (2024-11-20); Citadel Securities LP-metrics coverage (2026-10-08); Vanguard automation (https://www.fi-desk.com/fils-europe-vanguard-automates-70-of-trades-others-urge-caution/).
- Hedgeweek, "Banks turn net short corporate bonds for first time as market structure shifts" (2026-07-13).
- TwentyFour AM, "Liquidity is expensive, but it's there" (2022-07-11) and "Where are CLOs trading after the Truss Tantrum?" (2022-10-05).
- Barclays (Dynkin et al.) and Ben Dor et al. on Liquidity Cost Scores (shelf: Dynkin p.702, Ben_Dor p.120–123).

**Academic Papers**
- Roll (1984), *JF* 39(4) (https://doi.org/10.1111/j.1540-6261.1984.tb03897.x); Glosten & Milgrom (1985), *JFE* 14(1) (https://doi.org/10.1016/0304-405X(85)90044-3); Kyle (1985), *Econometrica* 53(6) (https://doi.org/10.2307/1913210); Ho & Stoll (1981), *JFE* 9(1) (https://doi.org/10.1016/0304-405X(81)90020-9).
- Avellaneda & Stoikov (2008), *Quantitative Finance* 8(3) (https://doi.org/10.1080/14697680701381228); Guéant, Lehalle & Fernandez-Tapia (2013) (https://arxiv.org/abs/1105.3115); Guéant (2017) (https://arxiv.org/abs/1605.01862); Guéant & Manziuk (2019) (https://arxiv.org/abs/1910.13205); Cartea, Jaimungal & Penalva (2015), *Algorithmic and High-Frequency Trading* (Cambridge UP).
- Fermanian, Guéant & Pu (2017) (https://arxiv.org/abs/1511.07773); Barzykin & Ciceri (2026) (https://arxiv.org/abs/2604.20406); Niang (2026) (https://arxiv.org/abs/2605.30643); Guo, Lehalle & Xu (2021) (https://arxiv.org/abs/1903.09140).
- Bao, Pan & Wang (2011), *JF* 66(3) (https://doi.org/10.1111/j.1540-6261.2011.01655.x); Edwards, Harris & Piwowar (2007) (https://doi.org/10.1111/j.1540-6261.2007.01240.x); Goldstein, Hotchkiss & Sirri (2007) (https://doi.org/10.1093/rfs/hhl020); Hendershott & Madhavan (2015) (https://doi.org/10.1111/jofi.12164); Kargar et al. (2021), NBER WP 27355; Choi, Huh & Shin (2024) (https://doi.org/10.1287/mnsc.2022.4646); O'Hara & Zhou (2021), "The electronic evolution of corporate bond dealers" (https://doi.org/10.1016/j.jfineco.2021.01.001); Bessembinder, Spatt & Venkataraman (2020) (https://doi.org/10.1017/S0022109019000231); Saunders, Srinivasan & Walter (1998), NYU Stern FIN-98-089; Milgrom & Weber (1982), "A Theory of Auctions and Competitive Bidding"; Harris (2003), *Trading and Exchanges* (Oxford UP).

**Data & Code**
- FINRA TRACE hub (https://www.finra.org/filing-reporting/trace): End-of-Day file, Academic Corporate Bond TRACE, Historic TRACE, Fact Book; Regulatory Notices 22-12, 25-17, 26-16; Rule 6750.
- NY Fed Primary Dealer Statistics (weekly dealer positions; Trend Watch §18.5).
- SEC EDGAR (https://www.sec.gov/edgar) for MarketAxess and Tradeweb 10-K automation statistics.
- Dick-Nielsen (2009, 2014), TRACE cleaning procedures (title only; SSRN).

<!-- STATUS: COMPLETE -->
