# Chapter 3: Cognitive Rewiring, From PJT RSSG to Systematic Desk Head

*Friday, 2:58 p.m. Lender call Monday at 9:00 a.m. The desk smells like cold coffee and DV01.*

The RFQ arrives on the all-to-all platform with the little chime that Theo Marsh has already learned to hate: **client sells \$15mm, Brambleworth Packaging 9.25% senior secured notes, B3.** (Brambleworth is fictional. The chime is real.) Eight dealers in competition. Two minutes on the clock.

Theo does what three years at PJT RSSG trained him to do. He opens the credit agreement. He has the PDF bookmarked at the definition of "Permitted Investments," because that is where the unrestricted-subsidiary basket lives and where the bodies are buried. He gets as far as clause (q) of the definition, which incorporates by reference the "Available Amount," which is defined forty pages earlier, which—

"Theo." Ines Okafor has not looked up from her screen. "What's the pot, what are the odds, and who at this table knows more than you?"

"The pot is fifteen million face. The odds depend on whether the sponsor can drop the IP into an unrestricted sub before the—"

"No. The odds depend on why this person is selling fifteen million at two fifty-eight on the Friday before a lender call. You have a hundred and ten seconds. The credit agreement will still be there Monday. The client won't."

Across the aisle, Dr. Kasimir "Kaz" Lind spins their chair around. "Let's just assume Gaussian. Mid is 87, daily vol is a point and a half, quote 86 and a quarter, done."

"The seller isn't Gaussian," says Ines. "The seller is a person. Persons have reasons."

Marguerite "Mags" Dunleavy, who has been pricing distressed paper since the bonds came with coupons you could physically clip, does not look up either. "Back in my day the seller had a name. His name was Steve. Steve called three dealers and sold to the one who hadn't read the 8-K. Now Steve is an algorithm and he calls eight of you at once."

Theo pulls the USB stick out of his pocket, the one with his old 13-week cash flow model on it, and holds it for a moment, for emotional support. Then he puts it back. He bids 85½, three-quarters of a point behind Kaz's Gaussian. He is covered: someone else paid 85¾. He has no idea whether that was a good outcome.

Neither do you, yet. **The question this chapter answers: what is a bid, and how do you know afterward whether it was a good one?**

By the end of this chapter you will be able to: translate the RSSG survival question into a probability distribution whose *variance* is the thing a dealer is paid to bear; derive the Glosten–Milgrom bid for a request for quote and extend it to many dealers and to a feature-dependent probability that the sender is informed; run a markout study that strips beta before it accuses anyone of anything; update a default probability from a Form 8-K with a correctly calibrated likelihood ratio; build the RSSG Edge Ledger, the inventory of what you know that the PhDs don't and how fast it decays; and specify, for a coding agent, a sequential detector for the flow that precedes a liability management transaction.

## 3.1 From Survival Questions to Distributions

The RSSG question set has a shape. Will the company file? When does the liquidity run out? Where is the fulcrum? Who provides the DIP, and does it roll up the prepetition loans? Who holds the blocking position in each class? Each of these questions is about a *state of the world*, and each answer is a scenario with a narrative and a waterfall. You have answered them for years with a 13-week cash flow model, a capital structure table, and a credit agreement annotated in three colors of highlighter.

The desk asks one question, over and over, in three seconds: *given that someone just asked me for a bid, what is the conditional distribution of this bond's value over the time I will hold it?* That question has two pieces the RSSG question lacks. It has a **time index** (the holding horizon $h$, measured in days, not in the months it takes a plan to be confirmed) and it has a **counterparty** (the person who sent the RFQ, whose decision to send it is itself information). Strip those two pieces away and the questions are the same. The banker has been pricing distributions all along. The vocabulary was just "upside" and "downside."

Moyer makes this explicit in a footnote that every RSSG analyst should tape to the inside of a credit agreement binder.

> **[SOURCE EXTRACTION]** *Moyer_Distressed_Debt_Analysis p.407:* "Those with a penchant for probabilities will discern that if the upside/downside ratio is 15/25, the implicit expected probability that the refinancing will occur is better than 50/50 (62.5%, to be exact). In an efficient market, the probability-weighted value of each outcome should be equal: 15 × 0.625 = 25 × 0.375."
>
> **Annotation.** The setup is a distressed issuer with two pari passu bonds: one matures in three months and trades at 85, the other matures in three years and trades at 60. If the near bond is refinanced it pays 100; if not, the company restructures and the near bond collapses to the level of its pari passu sibling. Solve $85 = 100\,p + 60\,(1-p)$ and you get $p = 25/40 = 0.625$. This is a two-point distribution, and its mean is the price. Three things the 2026 desk adds. First, the probability is a $\mathbb{Q}$-probability (it is backed out of a price, with no discounting and no risk premium), so if you want the $\mathbb{P}$-probability that the refinancing happens you need a view on how much the market charges for bearing this binary, and that charge is large for exactly the binaries a restructuring banker cares about. Second, the downside of 60 is not a constant: it is the price of the long bond *conditional on no refinancing*, and that price is itself a random variable with a recovery distribution underneath it. Third, and most important for this chapter, the footnote's "efficient market" is a market with no counterparty. On the desk, the price at which *you* can trade is the mean of the distribution conditional on someone choosing to trade with you. That conditioning is the whole job.

### 3.1.1 The two-point distribution and the variance it hides

Write the near bond's value at resolution as $V \in \{V^+, V^-\}$ with $\mathbb{Q}(V = V^+) = p$. The price is the mean,

$$
P = p\,V^+ + (1-p)\,V^-,
$$

and the variance is

$$
\operatorname{Var}(V) = p(1-p)\,(V^+ - V^-)^2 .
$$

For Moyer's numbers, $\operatorname{Var}(V) = 0.625 \times 0.375 \times 40^2 = 375$ points squared, a standard deviation of about 19.4 points on a bond priced at 85. Notice what the variance depends on: the *gap* between outcomes and the product $p(1-p)$, which is maximized at $p = \tfrac12$. A restructuring banker who moves the market's $p$ from 0.5 to 0.9 has not just changed the price; they have cut the variance from $0.25\Delta^2$ to $0.09\Delta^2$. Information is variance reduction. Remember that sentence. It is the reason a dealer charges a spread at all.

### 3.1.2 Three outcomes, and the law of total variance

Real distressed situations have more than two endings. Take a stylized B3 issuer with three scenarios over the next year: a clean refinancing ($k = 1$), an out-of-court distressed exchange or uptier ($k = 2$), and a Chapter 11 filing ($k = 3$). Let scenario $k$ have probability $p_k$ and, within it, a value distribution with mean $\mu_k$ and standard deviation $\sigma_k$. The price is the mixture mean and the variance splits by the law of total variance:

$$
P = \sum_{k} p_k\,\mu_k, \qquad
\operatorname{Var}(V) = \underbrace{\sum_k p_k\,\sigma_k^2}_{\text{within-scenario}} + \underbrace{\sum_k p_k\,(\mu_k - P)^2}_{\text{between-scenario}} .
$$

Plug in illustrative numbers: $p = (0.55, 0.25, 0.20)$, $\mu = (100, 70, 45)$, $\sigma = (0.5, 6, 12)$ points *(illustrative)*. The price is $55 + 17.5 + 9 = 81.5$. The within-scenario variance is $0.1375 + 9 + 28.8 \approx 37.9$. The between-scenario variance is $0.55(18.5)^2 + 0.25(11.5)^2 + 0.20(36.5)^2 \approx 487.8$. Total variance $\approx 525.7$, a standard deviation of about 22.9 points.

Ninety-three percent of the variance is the question "which scenario are we in?" That is the RSSG question. The recovery distribution *inside* Chapter 11, the thing the plan-valuation fight is about, contributes only seven percent. This is the first aha of the chapter, and it explains why the ex-RSSG hire is valuable on a systematic desk: the expensive uncertainty in high-yield credit is overwhelmingly about discrete states, and a banker who reads the documents and the docket can shift probability mass between states faster and more accurately than a model fit to spread time series. Kaz's "assume Gaussian" collapses a three-humped mixture into one bell curve with the right mean and the right variance and the wrong everything else: a Gaussian puts its mass at 81.5, the one price at which this bond will almost certainly *not* settle.

### 3.1.3 Horizon: the desk does not hold to resolution

A dealer who buys the bond on Friday does not care about its value at resolution next year; they care about the value at which they can sell it in $h$ days. Let $\mathcal{F}_t$ be the public information at $t$. The relevant uncertainty is the variance of the *price change* over the horizon,

$$
\sigma_V^2(h) = \operatorname{Var}\!\left(\mathbb{E}[V \mid \mathcal{F}_{t+h}] - \mathbb{E}[V \mid \mathcal{F}_t]\right),
$$

which is at most $\operatorname{Var}(V)$ and equals it only if everything resolves within the horizon. If the scenario will be revealed within $h$ with probability $\rho(h)$ and otherwise the price drifts with diffusive volatility $\sigma_{\text{d}}$ per square-root day, a reasonable first approximation is $\sigma_V^2(h) \approx \rho(h)\,\operatorname{Var}_{\text{between}} + h\,\sigma_{\text{d}}^2$. A lender call on Monday is precisely an event that pushes $\rho(h)$ toward one for a weekend horizon. That is why Ines asked about the calendar before she asked about the covenant: the Friday before a lender call is the moment $\sigma_V$ for a 3-day hold jumps from "a point and a half" to "a good fraction of twenty."

### 3.1.4 The USB stick gets a job

Every scenario probability in the mixture is a function of something the banker already models. The probability of a clean refinancing depends on how many weeks of liquidity the company has left, how much of the revolver is available, and whether the sponsor has a reason to defend the equity. Theo's 13-week model computes the first of these, so it gets demoted from emotional support to a covariate:

$$
\texttt{liquidity\_runway\_weeks} = \frac{\text{cash} + \text{revolver availability}}{\text{weekly operating burn}} .
$$

"Congratulations," Ines says when Theo shows her. "Your spreadsheet is now a feature." It will be the first column of the Edge Ledger in §3.5, and it will come back, more rigorous each time, as a survival-curve input in Chapters 5 and 6, a state-space variable in Chapter 25, and a liquidity-runway term in the Priming Risk Score in Chapter 13.

The second input the banker has is less comfortable to write down: what other people know. Moyer is admirably blunt about it in the context of the same refinancing trade.

> **[SOURCE EXTRACTION]** *Moyer_Distressed_Debt_Analysis p.265:* "who indicated that, while no decisions or commitments had been made, the bank would prefer to avoid a chapter 11 and was considering extending a \$500 facility, thereby enabling a refinancing of the ’04 seniors."
>
> **Annotation.** In Moyer's version of the trade the near bond trades at 85 and the far bond at 70, which prices a 50/50 refinancing. His investor believes the odds are better, and the reason given is a conversation with the bank. In 2002 this was offered as a description of how distressed investors form views. In 2026 it is a description of the information set that makes the person on the other side of your RFQ dangerous. Read it from the dealer's chair: somewhere in the market there is a holder whose posterior on the refinancing is 0.8 while yours is 0.5, and that holder's buy or sell decision is a function of the difference. Glosten and Milgrom turned this into a pricing rule in 1985, and §3.2 rebuilds it for RFQs. Note also the compliance subtext, which the 2024 SEC actions in §3.6 make explicit: information obtained from a lender relationship can be material non-public information, and a desk must model it as something *other people* may have, never as something it acts on itself.

## 3.2 The RFQ as a Poker Hand: Glosten–Milgrom for Request-for-Quote

An RFQ looks like a request for a price. It is better understood as a request for information that the requester is offering to pay for with a trade. When a client asks eight dealers for a bid on \$15mm, the client learns eight things about the market (or two, since most dealers will not answer; see below), and the dealer who wins learns one thing about the client: that the client wanted to sell at that price, right now, to them. Ben Dor's discussion of trader indications says the quiet part out loud, from the other side of the same exchange.

> **[SOURCE EXTRACTION]** *Ben_Dor_Quantitative_Credit_Portfolio_Management p.121:* "This indicative quote is usually tighter than a market quote because a trader can use an attractive indication to generate inquiries (which provide the trader with information)."
>
> **Annotation.** Ben Dor raises this as a data-quality problem for liquidity cost scores: indications are biased tight because they are bait. Read it as microstructure and it is a theory of the RFQ. Information flows both ways across a quote. The dealer's indication buys inquiries, and the client's inquiry buys quotes. On a 2026 desk the indication is an axe published to the platforms' dealer-inventory feeds, the inquiry is an RFQ routed by an algorithm, and the information both sides extract is logged, timestamped and fed into models. Ines's version is shorter: "A quote is a question you pay to ask." Kaz objects that in equilibrium the dealer is *paid* to answer. "Only if you charge $\pi\sigma_V$," says Ines. "Otherwise you are the client's free data vendor." The rest of this section derives what $\pi\sigma_V$ means.

### 3.2.1 The binary model

Work under the desk's physical measure $\mathbb{P}$ (these are the dealer's beliefs, not risk-neutral prices). A client sends a sell RFQ for bond $i$. The dealer's prior on the bond's value at the end of the holding horizon is two-point: $V \in \{m + \sigma_V,\ m - \sigma_V\}$ with equal probability, so the prior mean is the mid $m$ and the prior standard deviation is $\sigma_V$. With probability $\pi$ the sender is **informed** and knows $V$; with probability $1-\pi$ the sender is **uninformed** and sends a sell RFQ with probability $\tfrac12$ for reasons that have nothing to do with $V$ (redemptions, a rebalance, a CLO manager trimming a CCC bucket). An informed sender sells only when $V = m - \sigma_V$.

**Step 1: likelihoods.** The probability of seeing a sell RFQ in each state is

$$
\mathbb{P}(\text{sell} \mid V = m+\sigma_V) = \frac{1-\pi}{2}, \qquad
\mathbb{P}(\text{sell} \mid V = m-\sigma_V) = \frac{1-\pi}{2} + \pi .
$$

**Step 2: posterior.** By Bayes' rule with the equal prior, the two likelihoods sum to $1 - \pi + \pi = 1$, so

$$
\mathbb{P}(V = m+\sigma_V \mid \text{sell}) = \frac{\tfrac12 \cdot \tfrac{1-\pi}{2}}{\tfrac12 \cdot \tfrac{1-\pi}{2} + \tfrac12\left(\tfrac{1-\pi}{2} + \pi\right)} = \frac{1-\pi}{2} .
$$

**Step 3: the zero-profit bid.** A competitive dealer who expects to make zero on average sets the bid equal to the expected value conditional on the trade:

$$
b = \mathbb{E}^{\mathbb{P}}[V \mid \text{sell}] = (m + \sigma_V)\,\frac{1-\pi}{2} + (m - \sigma_V)\,\frac{1+\pi}{2},
$$

which simplifies to

$$
b^{\text{GM}} = m - \pi\,\sigma_V, \qquad a^{\text{GM}} = m + \pi\,\sigma_V . \tag{3.1}
$$

The half-spread is the probability that the sender is informed times the uncertainty the informed sender is resolving. This is Glosten and Milgrom (1985), and it is the $\Lambda_{\text{tox}}$ term in the bid equation of Chapter 1, now with a formula attached. Notice what it does *not* contain: inventory, risk aversion, or funding cost. A dealer who is risk-neutral, has infinite balance sheet, and pays nothing to carry a position still quotes a positive spread, purely because some of the people who want to trade with them know more than they do. That spread is not a fee. It is an insurance premium against the informed fraction of the flow, collected from everyone, and paid out to the informed.

The joke, which is also the point: the uninformed seller pays $\pi\sigma_V$ for the privilege of trading in a market that contains informed sellers. The pension fund rebalancing on the first of the month is subsidizing the distressed fund that just left a lender call. Market making is the business of running that cross-subsidy at a profit of exactly zero, which is why desks that do it well care so much about the "exactly."

**The asymmetric version.** Distressed bonds are rarely symmetric. Let the prior be $q = \mathbb{P}(V = V^+)$ with gap $\Delta = V^+ - V^-$, so $m = qV^+ + (1-q)V^-$. Repeating Steps 1–3,

$$
m - b = \Delta\,\frac{q(1-q)\,\pi}{\tfrac{1-\pi}{2} + \pi(1-q)} \;\approx\; 2\pi\,q(1-q)\,\Delta \qquad (\pi \text{ small}).
$$

With $q = \tfrac12$ and $\Delta = 2\sigma_V$ this collapses to (3.1). The small-$\pi$ form connects directly to §3.1: $q(1-q)\Delta^2$ is the variance of the two-point distribution, so the half-spread is roughly $2\pi \times \text{variance} / \text{gap}$. A bond near a binary event with $q$ near one half has the largest adverse-selection charge for a given gap, which is exactly the bond that ex-RSSG intuition flags as "this one is a coin flip and somebody knows which way it lands."

**Units.** Equation (3.1) is in price points if $\sigma_V$ is in price points. If your risk system gives you spread volatility $\sigma_s$ (in decimal per horizon), convert with spread duration: $\sigma_V \approx D^{\text{spr}}\,\sigma_s\,P$. For a bond at 87 with $D^{\text{spr}} = 3.5$ and a horizon spread volatility of 150bp, $\sigma_V \approx 3.5 \times 0.015 \times 87 \approx 4.6$ points *(illustrative)*. Mixing a spread-unit $\sigma_V$ with a price-unit $m$ is the single most common bug in RFQ engines written by coding agents, and it is silent: the bid is merely wrong by a factor of a few hundred.

### 3.2.2 Making $\pi$ a function of the RFQ

A constant $\pi$ is a teaching device. In practice the probability that the sender is informed is a function of what the dealer can observe about the request. Let $x$ be the RFQ's feature vector and write the posterior as a logistic model, or equivalently, under conditional independence of the features, as naive Bayes in odds form:

$$
\pi(x) = \frac{1}{1 + e^{-(\beta_0 + \beta^\top x)}}, \qquad
\frac{\pi(x)}{1 - \pi(x)} = \frac{\pi_0}{1 - \pi_0}\prod_{k} \text{LR}_k(x_k) .
$$

The features that belong in $x$, and the reason for each:

- **Size relative to average daily volume**, $\log(Q/\text{ADV})$. Easley and O'Hara (1987) showed that informed traders prefer size, so size is a signal. The empirical corporate-bond evidence of a "size penalty" within client (Pintér, Wang and Zou, Bank of England Staff Working Paper 970, 2022) points the same way.
- **Time to the next scheduled event and time since the last filing**: hours to earnings, a lender call, a coupon date, a grace-period expiry; days since the last 8-K. Informed bond trading concentrates before earnings announcements (Wei and Zhou, 2016).
- **Counterparty type**: dealer, systematic fund, distressed fund, CLO manager, ETF authorized participant, retail aggregator. Di Maggio, Kermani and Song (2017) show trading relationships price liquidity differently in stress.
- **Number of dealers in competition**, $n$, which the client chooses and which is therefore itself a signal (below).
- **The sender's trailing, shrunken markout score**, built in §3.3.
- **Axe alignment**: is the RFQ *against* the dealer's published axe? A client selling into your advertised bid is ordinary; a client selling when you have advertised an offer is asking you to take the other side of your own view.
- **The issuer's Priming Risk Score**, $\text{PRS} \in [0,1]$ (Chapter 13), which says how exposed this tranche is to being left behind in a liability management transaction.

Each $\text{LR}_k$ is estimated from the desk's own labeled history. The natural label is the sign of the realized 20-day IDO markout, defined in §3.3. Under the symmetric model the link between the two is exact: a filled sell RFQ is followed by a down-move with probability $(1 + \pi)/2$, so a model for the probability of an adverse markout, $\hat{p}_{\text{adv}}(x)$, implies $\hat\pi(x) = 2\hat{p}_{\text{adv}}(x) - 1$, clipped to $[0, 1]$.

### 3.2.3 Many dealers: the winner's curse

An RFQ to $n$ dealers is a first-price auction, and a dealer only trades when its bid is the highest. Winning is information. Conditional on winning, the other $n - 1$ dealers' signals were lower than yours, and since everyone is bidding on a common value, that means your own signal was more likely too high. The equilibrium response, from Milgrom and Weber's (1982) auction theory, is to bid the expectation conditional on winning:

$$
b_n^{*} = \mathbb{E}\!\left[V \;\middle|\; s_i,\ \max_{j \neq i} s_j \le s_i\right] \;<\; \mathbb{E}[V \mid s_i],
$$

with the shading increasing in $n$. Combining this with (3.1) and the Avellaneda–Stoikov inventory term previewed from Chapter 18 gives the compact quoting rule this chapter's engine implements:

$$
b^{*}(x, n) = m - \pi(x)\,\sigma_V - w(n)\,\sigma_V - \tfrac12\,\gamma\,\sigma_{\text{IDO}}^2\,(2q + Q), \tag{3.2}
$$

where $w(n) \ge 0$ is a monotone increasing winner's-curse shading calibrated from cover prices, $\gamma$ is risk aversion, $\sigma_{\text{IDO}}^2$ is the residual variance after hedging rates and index beta, $q$ is current inventory and $Q$ is the RFQ size (positive when the dealer is buying). State loudly, in every spec, that $\sigma_V$ here is the dealer's *physical* uncertainty over the holding horizon, not an implied volatility.

The empirical record supports both halves of the story. Hendershott and Madhavan (2015, *Journal of Finance*), using every U.S. corporate bond trade from January 2010 to April 2011 with 467,614 on MarketAxess, find that clients queried roughly 25 to 28 dealers per electronic auction, that only 15% to 29% of queried dealers responded (lower for high yield), that the modal number of investment-grade responses was three, and that about 60% of high-yield auctions drew two or fewer bids. Price impact rose with the number of dealers contacted, consistent with information leaking to everyone who sees the request. Fermanian, Guéant and Pu (2016), working with BNP Paribas's European corporate RFQ data, find that dealer quotes become more conservative as the number of requested dealers rises, that each dealer is less likely to answer as $n$ grows, and that the average number of answers clients wait for is "always around 2."

> **Poker Table.** "Everyone invites six dealers to the table and plays the first two cards they see," says Ines. "Be the first card or be the better one. Being the third is charity." The number of dealers in competition is the number of players at the table. The cover price, the second-best quote that a platform reports back to the winner, is the hand you didn't see, shown to you after the pot is pushed. A desk that logs its cover distance on every win is building the dataset that calibrates $w(n)$: if you routinely win by two points over the cover in eight-dealer auctions, you are not a great trader, you are the patsy who overpaid by two points. Theo's Friday 85½ was the cover; the winner paid 85¾. In a poker room that is called "folding correctly"; whether it was correct depends on where the bond is in five days, which is the subject of §3.3.

> **Trend Watch.** **The machines answer first (2016–2026).** In 2016 only about 19% of U.S. investment-grade trading was electronically facilitated, mostly by RFQ (Greenwich, cited in Bessembinder, Spatt and Venkataraman, 2020). Coalition Greenwich's annual review puts the electronic share of U.S. IG volume at 34%, 41%, 45% and 48% for 2021–2024 (2021–22 values read from a chart, approx.), and 52% in June 2025; high yield was stuck near 30–33% throughout. In June 2024 Coalition Greenwich reported that nearly 30% of bond dealer trading volume was executed without human intervention, with top-tier U.S. corporate desks fielding roughly 30,000 inquiries per day, top-tier dealers executing 57% of volume with no human, and non-bank liquidity providers 70%. MarketAxess reported that its automation suite handled over 36% of clients' global RFQ tickets in 2025 year to date (September 22, 2025), that 261 client firms used its automated or algorithmic tools in 2025 (204 in 2023), and that dealer algorithmic responses rose from 32.5 million in 2023 to 40.9 million in 2024 (Form 10-K filings). Trumid reported 88% of eligible RFQ line items executed fully no-touch in September 2025 (as reported by The DESK). **What it means for the desk:** the small, boring, uninformed ticket is now answered by an algorithm in milliseconds at a spread close to the GM minimum for $\pi \approx 0$. Adverse selection did not go away. It concentrated in what is left for humans: large, stressed, event-adjacent tickets in high yield and loans, exactly where $\pi(x)$ is large and exactly where the ex-RSSG reader's document knowledge moves the posterior. Automation turned market making into a two-tier business, and the second tier is the RSSG reader's home game.

> **[SOURCE EXTRACTION]** *Man_Revolutions_in_Credit_Trading_2023 p.5:* "Over the past year, intense investment by the sell side and the growth of algorithmic trading desks have greatly increased RFQ responses."
>
> **Annotation.** Man's point is about execution quality for a systematic investor: more responders means better fills and more data on which to build cost models, and the same page describes filtering "to only high-quality RFQ participants." Turn the telescope around. More algorithmic responders means more dealers who answer every RFQ with the same model, which means quote competition on the uninformed flow is brutal and margins on it approach zero. Hendershott and Madhavan found response rates of 15% to 29% in 2010–2011; a desk that today runs an auto-responder on every eligible RFQ has, in effect, set its own response rate to one and handed its adverse-selection defense to $\pi(x)$. That is fine if $\pi(x)$ is good. If it is a constant, the algorithm is the client's free data vendor at industrial scale. The modern desk departs from Man's buy-side framing in one respect that matters for this chapter: the desk must also model *which* RFQs its algorithm should refuse to answer, because a well-calibrated "no quote" on the informed tail is worth more than a tight quote on the rest.

## 3.3 Markouts: The Hand History

Every poker player who wins over a career keeps hand histories. Ines calls the markout "the hand history," and she means it literally: it is the record of every trade you did, replayed against where the market went afterward, so you can find out which of your decisions were good and which were merely lucky. A trader who does not look at markouts is a poker player who only remembers the pots they won.

### 3.3.1 Definition and sign convention

For a dealer fill at price $p_0$ at time $t_0$, let $\eta = +1$ if the dealer bought and $\eta = -1$ if it sold, and let $m_t$ be a reference mid. The markout at horizon $h$, in basis points of price, is

$$
\text{MO}_h = \eta\,\frac{m_{t_0+h} - p_0}{p_0} \times 10^4, \qquad h \in \{1, 5, 20\} \text{ business days}.
$$

Positive is good for the dealer. A dealer that bought at 85.75 and sees the mid at 87 five days later has a markout of $+146$bp of price; one that sees the mid at 81 has $-554$bp.

The horizons need a justification, because equity desks measure markouts in seconds and the habit travels badly. Corporate bonds trade so rarely that a sub-day mid is mostly a model, and the time it takes a client to finish trading after a failed attempt is measured in days: Kargar, Lester, Plante and Weill (2025, *Sequential Search for Corporate Bonds*, FRB Philadelphia Working Paper 25-08) find, using MarketAxess inquiry data, that "it takes 2-3 days to complete a transaction after an unsuccessful attempt." A one-day markout therefore captures the immediate information content of the trade, a five-day markout captures the completion of the client's search and the dealer's typical unwind, and a twenty-day markout captures the slow information (the downgrade, the 8-K, the lender call) that an informed seller was actually trading on.

### 3.3.2 The decomposition

Add and subtract the mid at the time of the trade:

$$
\text{MO}_h \propto \underbrace{\eta\,(m_{t_0} - p_0)}_{\text{captured half-spread}} \;+\; \underbrace{\eta\,(m_{t_0+h} - m_{t_0})}_{\text{post-trade drift}} .
$$

The first term is what you charged. The second is what the market charged you back: adverse selection plus noise. Under the Glosten–Milgrom model with the zero-profit bid (3.1), if the reference mid converges to the true value by the horizon, then for a filled sell RFQ

$$
\mathbb{E}[\text{MO}_h \mid \text{fill}] \propto \mathbb{E}[V \mid \text{sell}] - b^{\text{GM}} = 0,
$$

because the half-spread $\pi\sigma_V$ exactly pays for the expected drift $-\pi\sigma_V$. If instead the dealer bids at the mid (it assumes $\pi = 0$), the expected markout is $-\pi\sigma_V$: the full adverse-selection cost lands in the post-trade drift. This gives the markout its diagnostic power. **A persistently negative long-horizon markout against a set of counterparties means your $\pi(x)$ for them is too low.** A persistently positive one means it is too high, and you are leaving trades, and franchise, on the table.

### 3.3.3 IDO markouts: strip beta before you accuse anyone

Theo's first markout report flags a pension fund as toxic: every bond it sold the desk in June fell over the next five days. Ines reads the report for ten seconds. "CDX widened twelve basis points that week and Treasuries sold off. You've just accused a pension fund of insider trading for owning beta."

The desk motto, "IDO or it didn't happen," applies to markouts as much as to alpha. Replace the raw mid with a beta-stripped reference:

$$
m^{\text{IDO}}_t = m_t - P_{t_0}\left(-D^{\text{spr}}_i\,\beta_i\,\Delta s^{\text{index}}_{[t_0,t]} - D^{\text{mod}}_i\,\Delta y^{\text{TSY}}_{[t_0,t]}\right),
$$

where $\Delta s^{\text{index}}$ is the change in the index spread (CDX or a cash index), $\beta_i$ is the bond's empirical spread beta to it (Chapter 8 builds this properly, and shows that for CCCs the analytical duration badly overstates the true sensitivity), and $\Delta y^{\text{TSY}}$ is the matched-maturity Treasury yield change. The bracket is the systematic price return predicted by the market moves, so subtracting it leaves the idiosyncratic part. The IDO markout is the markout computed against $m^{\text{IDO}}$. A client who sells you a bond the day before the whole market rallies is not informed; a client who sells you a bond the day before *only that issuer* gaps down is.

### 3.3.4 Counterparty scores, shrunk

You want a per-counterparty toxicity score to feed into $\pi(x)$. The naive estimate, the average IDO markout over that counterparty's fills, is noisy: a counterparty with three fills and an average of $-300$bp is probably unlucky, not informed. Treat the true counterparty effect as a random effect, $\theta_c \sim \mathcal{N}(0, \tau^2)$, observed through $n_c$ fills with per-fill noise variance $\sigma^2_{\text{MO}}$. The posterior mean is the classic empirical-Bayes shrinkage:

$$
\hat\theta_c = \frac{n_c}{n_c + \sigma^2_{\text{MO}}/\tau^2}\;\overline{\text{MO}}_c .
$$

Estimate $\tau^2$ by the method of moments across counterparties: the cross-sectional variance of the counterparty means minus the average sampling variance $\sigma^2_{\text{MO}}/n_c$, floored at zero. When $\tau^2 = 0$ every counterparty is shrunk to zero, which is the correct answer when your data cannot tell them apart. Andersen and Bondarenko (2014) are the cautionary tale for the equity version of this exercise: flow-toxicity metrics can look predictive purely because of how they are built, so any score must be validated out of sample against markouts it was not fit on.

> **[SOURCE EXTRACTION]** *Ben_Dor_Quantitative_Credit_Portfolio_Management p.120:* "If a trader were temporarily long inventory of a particular bond, then the trader might quote the bond with a tighter spread (i.e., a higher offered spread) to entice a bid, and vice versa."
>
> **Annotation.** Ben Dor's concern is that inventory-driven quotes make a bond look more liquid than it is. The markout analyst should worry about the mirror image: the dealer's own inventory contaminates the dealer's own markouts. A desk that is long and skewing its offer down to get out will sell at prices that look aggressive, and the subsequent markouts will look good because the price was set below where the market would otherwise clear. Conversely, a desk that is short and bidding up to cover will buy at prices that guarantee poor markouts against clients who did nothing wrong. Before you attribute a markout to the counterparty, control for your own inventory skew at the time of the quote, the $\tfrac12\gamma\sigma_{\text{IDO}}^2(2q + Q)$ term of (3.2). Otherwise the toxicity score partly measures your own position.

### 3.3.5 Survivorship: only fills have markouts

The markout sample is adversely selected by construction. You only observe markouts on RFQs you won, and you win disproportionately when your quote is the most generous, which is disproportionately when you are wrong. The fix comes from Fermanian, Guéant and Pu's outcome taxonomy: every RFQ ends as **Done** (you traded), **Covered** (your quote was second best), **Traded Away** (someone else won and you were not second), or **Not Traded**. Platforms typically report the cover price to the winner and, for some protocols, enough information to know you were covered. Compute *counterfactual* markouts for Covered and Traded Away RFQs from your own quote. If the RFQs you lost have systematically better counterfactual markouts than the ones you won, you are not unlucky: your bids are winning precisely the hands you should fold.

> **Ways This Blows Up.** (1) **Stale mids.** A bond that has not printed in ten days has a composite mid that is a model. Its markout is the error of your model against someone else's model. Flag markouts whose reference mid has no trade within the horizon and down-weight them. (2) **Mixed units.** Price markouts and spread markouts are not interchangeable across bonds with different durations; a 10bp spread markout on a 2-year bond and on a 10-year bond are different amounts of money. Store both, report price bp. (3) **Size-weighting.** A \$50k odd lot and a \$15mm block are not the same observation. Weight by notional, or model them separately. (4) **Your own footprint.** At the one-day horizon, the mid partly reflects your own hedging and unwind. A desk that dumps a block into the street and then measures its markout has measured its own market impact. (5) **Label leakage.** If $\pi(x)$ is fit on 20-day markouts and then evaluated on the same RFQs, the toxicity feature will look magnificent. Purge by time (Chapter 7).

**The hand, replayed.** Here is Theo's Friday with five days of hindsight *(illustrative numbers)*. Mid at the time was 87. The winner bought at 85.75, a captured half-spread of 1.25 points. The lender call on Monday went badly, and by Thursday the mid was 81: a raw drift of $-6$ points. Over the same days CDX widened 20bp and Treasuries rallied 10bp. With $\beta = 1.3$, $D^{\text{spr}} = 3.5$ and $D^{\text{mod}} = 3.6$, the systematic move was about $87 \times (-3.5 \times 1.3 \times 0.0020 + 3.6 \times 0.0010) \approx -0.48$ points. So the IDO drift was about $-5.5$ points, and the winner's IDO markout was roughly $1.25 - 5.5 = -4.3$ points, or about $-500$bp of price. Theo's counterfactual markout at 85.5 would have been about $-4.0$ points. He lost the auction and won the hand. One hand is an anecdote, not a hand history; the hand history is the next five thousand, which is why §3.8 builds the engine.

## 3.4 The Bayesian 8-K: Updating a Default Distribution in Four Business Days (or Four Minutes)

An RSSG analyst reads an 8-K the way a radiologist reads an X-ray: not for what it says, but for what the company's lawyers were forced to say. "Entry into a Material Definitive Agreement" can mean a new customer contract or a forbearance agreement with the lenders, and the difference is on page three of Exhibit 10.1. The desk version of that skill is a likelihood-ratio table, a parser that fires within minutes of the filing hitting EDGAR, and a Bayes update that moves the default distribution by the right amount, not by the amount the headline suggests.

### 3.4.1 The 8-K as a set of signals

Form 8-K requires a current report "to be filed or furnished within four business days" of a triggering event (Form 8-K, General Instruction B.1). The items that matter most to a credit desk:

| Item | Title (abridged) | Why the desk cares |
| :--- | :--- | :--- |
| 1.01 / 1.02 | Entry into / termination of a material definitive agreement | Forbearance agreements, amendments, cooperation-agreement-adjacent deals, RSAs |
| 1.03 | Bankruptcy or receivership | The event itself; by now the price already knows |
| 2.03 | Creation of a direct financial obligation | New money, including priming facilities raised out of court |
| 2.04 | Triggering events that accelerate or increase a direct financial obligation | Acceleration, cross-default; the item requires the amount and terms of the acceleration |
| 2.06 | Material impairments | Asset values in the recovery waterfall just moved |
| 3.01 | Notice of delisting | Equity cushion signal; often precedes a restructuring |
| 4.02 | Non-reliance on previously issued financial statements | The covenant compliance certificate you modeled may be fiction |
| 5.02 | Departure of directors or certain officers | CFO departures before a liquidity event are a classic tell |
| 7.01 / 8.01 | Regulation FD / other events | Catch-alls; cleansing disclosures after lender negotiations often land here |

Two warnings belong in every parser spec. Items 2.02 and 7.01 are **furnished**, not filed, which changes the liability attached to them and, in practice, how carefully they are drafted. And companies do not always put content where the taxonomy says they should: material acceleration language can turn up under 8.01. Parse the text, not just the item number.

Kaz, reading over Theo's shoulder, finds a "springing lien" in an exhibit and asks whether the lien is seasonal. Mags answers without looking up: "It springs into existence when the borrower trips a trigger, a downgrade or a leverage test. Like a mousetrap, except the mouse signed it and paid the lawyers."

### 3.4.2 The update

Let the prior probability of default within horizon $T$ (in years) come from a physical hazard $\lambda$, for example an EDF-style model (Chapter 6):

$$
p = 1 - e^{-\lambda T} .
$$

An 8-K event $E$ has a likelihood ratio

$$
\text{LR}_E = \frac{\mathbb{P}(E \mid \tau \le T)}{\mathbb{P}(E \mid \tau > T)},
$$

the ratio of how often filings like this one appear before defaults to how often they appear at companies that do not default within $T$. Bayes' rule in odds form gives the posterior, and inverting the survival relationship gives the posterior hazard:

$$
\frac{p'}{1-p'} = \text{LR}_E \cdot \frac{p}{1-p}
\quad\Longrightarrow\quad
p' = \frac{\text{LR}_E\,p}{1 - p + \text{LR}_E\,p}, \qquad
\lambda' = -\frac{1}{T}\ln(1 - p') . \tag{3.3}
$$

Translating the hazard move into a spread move requires leaving $\mathbb{P}$. The credit triangle says $s \approx L\,\lambda^{\mathbb{Q}}$, where $L = 1 - R$ is loss given default, and the risk-neutral hazard differs from the physical one by a default risk premium. Write $\lambda^{\mathbb{Q}} = \kappa\,\lambda^{\mathbb{P}}$ with $\kappa > 1$ a time-varying ratio; then

$$
\Delta s \approx L\,\kappa\,(\lambda' - \lambda) .
$$

Say this explicitly in every spec, because the lazy version, which treats the 8-K as moving the $\mathbb{Q}$-hazard one for one, silently assumes $\kappa = 1$ and understates the spread move.

**Worked example** *(illustrative)*. A B3 issuer has a one-year physical PD of 6%, so $\lambda = -\ln(0.94) \approx 0.0619$. It files an 8-K under Item 1.01 attaching a forbearance agreement, and the desk's calibrated likelihood ratio for that event type in this rating bucket is 2.5. Prior odds $0.06/0.94 = 0.0638$; posterior odds $0.1596$; $p' \approx 13.8\%$; $\lambda' = -\ln(1 - 0.1376) \approx 0.148$. With $L = 0.6$ and $\kappa = 2$, the implied spread move is $0.6 \times 2 \times 0.0862 \approx 0.103$, about 1,030bp. That sounds enormous, and for a B3 that just told the world it needed its lenders' permission to keep operating, it is about right. The trading question is not whether the spread should move 1,030bp; it is how much of that move was already in the price before the filing, which is a question about who knew first (§3.6).

**Where the edge is, and is not.** The 8-K is public. By the time your parser fires, the fastest readers have read it. The edge is in two places: parse latency (minutes, not hours, for an exhibit buried in a 300-page PDF) and the calibration of $\text{LR}_E$, which requires a labeled corpus and, crucially, conditioning on the issuer. The phrase "liability management transaction" in an investment-grade telecom's 8-K usually describes a routine tender offer. The same phrase in a sponsor-backed B3's 8-K usually means somebody is about to be primed. The likelihood ratio of a token is conditional on the issuer's rating and its Priming Risk Score, which is why a bag-of-words model trained across the whole EDGAR universe is worse than useless for distressed names: it averages the LR of AT&T with the LR of a company whose lenders just hired restructuring counsel.

### 3.4.3 The base-rate trap

The likelihood ratios come from a training corpus, and training corpora for default models are built with far more defaults than the live book contains, because otherwise there would be nothing to learn from. A model fit on a sample with default rate $S$ produces probabilities calibrated to $S$, and the live book has default rate $T$. The tempting fix is to scale, $p^{*} = (T/S)\,p$. Bohn and Stein show why this fails and give Elkan's (2001) correction, which in our notation is

$$
p^{*} = \frac{T\,(p - pS)}{S - pS + pT - ST} . \tag{3.4}
$$

It is worth seeing where (3.4) comes from, because it is the same update as (3.3). Changing the base rate from $S$ to $T$ multiplies the odds by the ratio of prior odds:

$$
\frac{p^{*}}{1-p^{*}} = \frac{p}{1-p}\cdot\frac{T/(1-T)}{S/(1-S)} .
$$

Solve for $p^{*}$, multiply through by $S(1-S)$, and the denominator collects to $pT(1-S) + (1-p)(1-T)S = S - pS + pT - ST$. The base-rate correction *is* a likelihood-ratio update, applied to the whole model at once. The scaling shortcut is its first-order approximation for small $p$, which is why it works for IG and breaks for exactly the names this chapter cares about.

> **[SOURCE EXTRACTION]** *Bohn_Stein_Active_Credit_Portfolio_Management p.253:* "This adjustment, in addition to being grounded a bit more rigorously in probability theory, has the attractive property that it can never exceed 1.0."
>
> **Annotation.** On the preceding page Bohn and Stein show that the simple $T/S$ scaling produces probabilities above one whenever the model output exceeds $S/T$, and that it overstates probabilities increasingly as model output rises when the true base rate is above the sample rate. For a desk updating PDs from 8-Ks, that is not an academic nicety. A stressed-name model with a sample default rate of 2% deployed into a 2025–2026 book where the all-in default rate including distressed exchanges was running several times its ex-DE level will, with naive scaling, assign probabilities above one to the names you most need to price. The modern wrinkle Bohn and Stein did not face is that $T$ itself depends on the default definition. Moody's reported a June 2025 speculative-grade default rate of 5.8% including distressed exchanges and 2.1% excluding them, so "the" base rate is a modeling choice. Pick the definition that matches the payoff you are pricing: a distressed exchange is a default for a CDS holder and for a left-behind lender, and a non-event for nobody.

> **Trend Watch.** **"Liability management" goes mainstream in the 8-K corpus (2019–2026).** An EDGAR full-text search for the exact phrase "liability management transaction" in Form 8-K filings (queried October 17, 2026; counts are documents, including exhibits) returns 4 hits in 2019, 9 in 2020, 23 in 2021, 15 in 2022, 14 in 2023, 55 in 2024, 54 in 2025 and 37 in 2026 through October 16. The number of distinct filers runs 4, 6, 16, 12, 8, 24, 27 and 24. The 2024 step-up coincides with what Wachtell Lipton describes as the high-water mark of 38 LMEs in 2024 (24 in 2025; "Liability Management 2026: For Better or Worse," February 3, 2026). **What it means for the desk:** the filer list mixes investment-grade issuers running routine tender offers with sponsor-backed high-yield issuers running uptiers and drop-downs, so the raw count is a terrible signal and the conditional count is a good one. Condition on rating, sponsor ownership and PRS before you let the token into $\pi(x)$. Kaz's bag-of-words model will learn that "liability management" predicts default, then short every investment-grade issuer that ever ran a tender offer.

## 3.5 The RSSG Edge Ledger

Every skill the reader brings from RSSG is a likelihood ratio waiting to be written down. The Edge Ledger is the place it gets written down: one row per skill, with the feature it becomes, where the data comes from, how often it refreshes, how fast its predictive power decays, and who else already has it. The last column is the one bankers skip and traders never do. An edge that every covenant-analytics vendor sells by subscription is not an edge; it is a cost of doing business.

| RSSG skill | Codable feature | Data source | Refresh | Decay horizon (IC half-life) | Who else has it |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 13-week cash flow model | `liquidity_runway_weeks` | 10-Q/10-K, 8-K Item 2.03, compliance certificates | Quarterly + events | Months | Rating agencies, equity analysts (partially) |
| Reading the credit agreement | Blocker flags (J.Crew, Serta, Chewy), "open market purchase" token, restricted-payments and Available Amount capacity | EDGAR exhibits, Chapter 25 parser | On each amendment | Long until the document changes, then zero | Covenant-analytics vendors, for the documents they cover |
| Knowing who the advisers are | Adviser-hire event timestamps (company side and creditor side) | Press, restructuring news services, dockets | Event | Days to weeks | Every news terminal, within hours |
| Mapping the holders | Holder-concentration vector; ad hoc group formation; Rule 2019 disclosures | Dockets (CourtListener/RECAP), CLO trustee reports | Event / monthly | Weeks | Distressed funds, restructuring news services |
| Finding the fulcrum | Recovery sensitivity $\partial R / \partial \text{EV}$ by tranche | Cap table + plan-value model | Quarterly | Months | Distressed PMs; almost no systematic models |
| Knowing the sponsor | Sponsor's historical LMT propensity | Deal history database | Static, updated per deal | Years | Few, and none systematically |
| Watching payables | Days-payable-outstanding stretch | 10-Q | Quarterly | Months | Equity short sellers |
| Watching the equity tape | Equity short interest percentile within rating bucket | Exchange short-interest data, securities lending | Bi-monthly / daily | 3–12 months (Dynkin p.794) | Every quant equity desk |
| Reading the room | Shrunken counterparty markout score; informed-type net flow | Own RFQ logs, TRACE | Daily | Days to weeks | Only you: it is your own flow |

Three columns carry the economics. **Decay horizon** decides where the feature lives in the stack: a feature with a half-life of days belongs in the RFQ engine's $\pi(x)$ and must be computed in real time; a feature with a half-life of months belongs in the portfolio model and can be refreshed overnight. **Refresh** decides how stale the feature can be when it is used, which is the source of half the bugs in production credit models. **Who else has it** decides how much the feature is worth after costs.

To make the decay column operational, model the information coefficient as a function of horizon $h$ with half-life $h_{1/2}$:

$$
\text{IC}(h) = \text{IC}_0 \cdot 2^{-h/h_{1/2}} .
$$

A feature used at horizon $h$ earns $\text{IC}(h)$, not $\text{IC}_0$. Two practical consequences follow. First, comparing features with different native horizons requires putting their forecasts on a common clock, which Paleologo spells out for equities and which applies unchanged to bonds.

> **[SOURCE EXTRACTION]** *Paleologo_Advanced_Portfolio_Management p.90:* "whenever forecasts for different stocks are at different horizons, they should be adjusted so that longer-horizon forecasts get adjusted downward compared to short-horizon ones"
>
> **Annotation.** Paleologo's procedure divides each forecast's expected return by its horizon, $\alpha = r/T$, so that a 20% return expected over a year and a 5% return expected over a month are compared as rates. In the Edge Ledger, the fulcrum analysis that says "this second lien is worth 40 in a plan eighteen months from now" and the flow signal that says "this second lien will be two points lower by Friday" are both alpha, and they cannot be added until they share a clock. The ex-RSSG reader's characteristic error is to treat the long-horizon view as the important one because it is the one that took ninety hours to build. Per unit of time, the five-day flow signal is often larger, and it is the one that tells you whether to bid for the paper today. The modern desk departs from Paleologo in one way: credit forecasts are horizon-dependent not just in scale but in sign, because the path to a good restructuring outcome often runs through a bad month.

Second, simple features decay faster than complex ones, because more people can compute them. Man's survey of quant credit managers makes the point bluntly.

> **[SOURCE EXTRACTION]** *Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.30:* "On the one hand, simple models tend to experience faster alpha decay (as we have seen in the equity markets)."
>
> **Annotation.** The sentence continues with the other hand: sophisticated models risk overfitting and a loss of transparency. The Edge Ledger is a way to escape the dilemma rather than split it. The features in the RSSG rows are not complex in the statistical sense. A blocker flag is a single bit. They are complex in the *extraction* sense: computing them requires reading a document that most quant teams cannot parse, or understanding a process that most quant teams have never sat through. That kind of complexity decays slowly, because the barrier to entry is expertise, not compute. It is also exactly the kind of feature that an AI coding agent can help scale once a human has specified it correctly, which is the subject of Chapter 25 and the reason this book teaches you to write specs.

Man's own "Informed Investor" style factor (Man 2022, p.27) and Dynkin's equity-short-interest signal (Dynkin p.794: issuers with the highest short interest within their rating category "are the most likely issuers to be downgraded over the next three to 12 months") are the published, slow versions of the Ledger's flow rows. The Ledger's contribution is to make them fast and conditional: the same short-interest spike means something different for a name with a Serta blocker than for one without.

Mags reads the Ledger over Theo's shoulder. "Back in my day the Edge Ledger was a Rolodex. Each card said who owed you a favor and who had lied to you. The decay horizon was how long you held a grudge." She taps the last row. "Steve's card never decayed." A pause. "Fine. Your spreadsheet holds a grudge better than I do. Add a column for who lied."

## 3.6 Who at This Table Knows About the LMT?

Ines's third question, "who at this table knows more than you?", has a specific and expensive answer in leveraged credit: the lenders who are about to do a liability management transaction to the lenders who are not. An LMT is the purest adverse-selection event in the asset class. A majority of a class negotiates privately with the borrower, and on announcement the paper held by the majority and the paper held by everyone else become, economically, different securities. Before announcement they trade at one price.

> **[SOURCE EXTRACTION]** *Moyer_Distressed_Debt_Analysis p.228:* "Exchange offers are “coercive” when they compel cooperation by exposing nonparticipants to the risk of being made worse off."
>
> **Annotation.** Moyer was writing about exit consents and old-fashioned exchange offers, where the coercion was that holdouts were left with a stripped indenture. The 2020s uptier and drop-down are the same idea with the coercion turned up: nonparticipants are not just stripped of covenants but primed, subordinated to new money and to the participants' exchanged debt. For the desk, "the risk of being made worse off" has a price, and the price is exactly the gap between the inside and outside paper after announcement. Before announcement, a holder who knows the deal is coming knows which side of that gap they will be on. That is $V$ in the Glosten–Milgrom model, and the participating lenders know it.

### 3.6.1 The anatomy of pre-LMT flow

The flow that precedes a non-pro-rata transaction has a recognizable shape, because the transaction needs votes:

1. **Accumulation to a threshold.** "Required Lenders" under a typical credit agreement means lenders holding more than 50% of the loans; many indenture amendments, including lien releases, need two-thirds; sacred rights need each affected lender. A group that holds 45% and needs 50.1% must buy, and must buy in one tranche.
2. **The left-behind signature.** One-sided buying by counterparty types prone to these deals (distressed and credit-opportunity funds, sponsor-affiliated accounts, prior cooperation-agreement signatories), concentrated in a single tranche, while the issuer's equity and CDS are relatively quiet. The buyers are not betting on the company. They are betting on the vote.
3. **Silence where there used to be noise.** Holders who have been wall-crossed into negotiations are restricted. Their usual flow, axes and bids stop. The absence is informative.
4. **Post-announcement dispersion.** On announcement, inside and outside paper separate. The outside paper's drop is the realized adverse selection on every dealer who was long it.

Notice what the dealer should and should not do with this. The informed accumulator is a *buyer*. A dealer who sells to them and stays short the outside paper does fine, because the outside paper will fall. The dealer who is hurt is the one who keeps *buying* outside paper from everyone else, building long inventory into the announcement. So the detector's output enters $\pi(x)$ for sell RFQs in the vulnerable tranche, and it triggers a separate flag: stop building long inventory in the paper most likely to be left behind.

### 3.6.2 A sequential detector

Let $y_t$ be day-$t$ net buying of tranche $i$ by counterparties in the LME-prone set, scaled by trailing average daily volume. Under the null of no deal, $y_t \sim \mathcal{N}(0, \sigma_y^2)$ independently; under the alternative of accumulation toward a threshold, $y_t \sim \mathcal{N}(\mu_1, \sigma_y^2)$. The log-likelihood ratio of one day's observation is

$$
\ell_t = \ln\frac{\phi\big((y_t - \mu_1)/\sigma_y\big)}{\phi\big(y_t/\sigma_y\big)} = \frac{\mu_1}{\sigma_y^2}\left(y_t - \frac{\mu_1}{2}\right),
$$

where $\phi$ is the standard normal density; the quadratic terms in $y_t$ cancel, leaving a linear statistic. Page's CUSUM accumulates evidence and resets when evidence turns against the alternative:

$$
S_t = \max\!\left(0,\; S_{t-1} + \ell_t\right), \qquad S_0 = 0, \qquad \text{alarm at the first } t \text{ with } S_t > h . \tag{3.5}
$$

Two properties make (3.5) the right tool. Its false-alarm average run length under the null is at least $e^{h}$ (Lorden, 1971), so a threshold of $h = 4$ gives at least 55 trading days between false alarms on a single tranche, and in practice many more. And its expected detection delay under the alternative is approximately $h / K$, where $K = \mu_1^2 / (2\sigma_y^2)$ is the Kullback–Leibler divergence per day; with $\mu_1 = \sigma_y$ and $h = 4$, about eight trading days. Eight trading days is short relative to the weeks it takes a group to accumulate, document and sign a transaction.

**The prior.** Not every tranche is equally exposed. The Priming Risk Score from Chapter 13, $\text{PRS} \in [0,1]$, is the prior probability that the tranche's documents and holder base permit a non-pro-rata deal. Fold it in as prior log-odds: alarm when $S_t + \operatorname{logit}(\text{PRS}) > h_0$, that is, use the threshold

$$
h(\text{PRS}) = h_0 - \ln\frac{\text{PRS}}{1 - \text{PRS}},
$$

floored at a minimum so a single noisy day can never fire the alarm. A tranche with no blockers, a loose "open market purchase" exception and a concentrated holder base gets a low threshold. A tranche with a Serta blocker gets a high one. This is where the ex-RSSG reader's document knowledge enters the flow model: the PRS is the thing they know how to compute and the quant does not.

**Error-prone spots.** Label event dates from 8-Ks and press releases, never from when the desk noticed. The LME-prone counterparty set drifts as funds change strategy, so re-estimate it with a lag. And the training set is survivorship-biased toward deals that happened; accumulations that ended in a pro rata deal, or in nothing, are the null hypothesis and must be in the sample.

> **Trend Watch.** **Defaults are now mostly negotiated (2024–2026).** Moody's reported that distressed exchanges were 64% of all defaults in the first half of 2025, about the same pace as 2024, "which itself was the highest annual share on record," and that the June 2025 speculative-grade default rate of 5.8% fell to 2.1% once the 51 distressed restructurings were removed ("US Credit Review & Outlook," July 2025). Moody's later put distressed restructurings at approximately 65% of all 2025 defaults (April 28, 2026). Wachtell Lipton counts LMEs falling from a high-water mark of 38 in 2024 to 24 in 2025 while remaining about two-thirds of default activity by issuer count ("Liability Management 2026," February 3, 2026). The aftermath is not benign: in a sample of 1,173 borrowers with soft credit events since 1979, Moody's finds "about one in four soft credit events ultimately ends in hard default," and that more than 70% of eventual hard defaults after a distressed restructuring occur within two years ("Lend, extend, and then...," May 18, 2026). **What it means for the desk:** the pre-LMT state is no longer a once-a-cycle tail; it is a recurring regime that a meaningful slice of the high-yield and loan universe is in at any given time. A market maker in sponsor-backed paper without a pre-LMT detector is a poker player who has not noticed that a third of the table is playing as a team.

### 3.6.3 The information wall is a feature

The detector must only ever use information the desk is allowed to use: public data and its own flow. The SEC has made clear that lender-group membership is an information channel regulators watch. In its settled action against Sound Point Capital Management (August 26, 2024; \$1.8mm civil penalty), the SEC found that the firm regularly participated in lender groups and creditors' committees, sometimes received material non-public information about companies whose loans were in CLOs it traded, and lacked adequate written policies to address that risk. A month later it settled with Marathon Asset Management (September 30, 2024; \$1.5mm penalty) for lacking policies "reasonably designed to address" MNPI risk from ad hoc creditors' committee participation.

Read those orders as a modeling specification. Counterparties *on* a committee should be modeled as restricted: their silence is a feature. Counterparties *not* on the committee who trade the same tranche heavily just before an announcement are the live adverse-selection risk, because they are the ones reading the tape. And the desk itself, the moment it is wall-crossed, stops quoting the name, which is a compliance rule and also, conveniently, the only way to keep $\pi(x)$ honest.

> **Poker Table.** "The player who suddenly stops betting is telling you something too," says Ines. Theo asks the Ad Hoc Group, which has formed in the corner of the trading floor as it always does, whether it is buying first-lien paper. The Ad Hoc Group answers in unison: "We are represented by counsel." Theo updates $\pi$ to 0.9 anyway. A press report that a lender group has retained counsel is a likelihood ratio with a timestamp. A Rule 2019 statement, if it comes to that, is a likelihood ratio with a docket number.

## 3.7 Case Study: Serta Simmons, June 22, 2020, Seen From a Market Maker's Blotter

Chapter 13 owns the full legal and game-theoretic autopsy of Serta. This section asks a narrower question: what did the uptier look like from a dealer's blotter, and what would the machinery of this chapter have done with it?

> **Docket Diary.** **November 2016:** Serta Simmons Bedding refinances, borrowing \$1.95bn under a first-lien term loan agreement. **June 22, 2020:** the uptier closes. Serta receives \$200mm of new money as first-out super-priority debt; participating lenders exchange first- and second-lien loans (about \$1.2bn in total) into roughly \$875mm of second-out super-priority debt (Fifth Circuit opinion). On the first-lien side, the participants held about \$992mm (52.6%) of the class and exchanged it for roughly \$734mm face of new first-lien second-out debt; the excluded lenders held about \$895mm (47.4%) (Mayer Brown, July 2026). The credit agreement allowed non-pro-rata buybacks only through a Dutch auction open to all lenders or through "open market purchases." **January 2023:** Serta files for Chapter 11 in the Southern District of Texas, and the bankruptcy court upholds the transaction later that year. **December 31, 2024:** the Fifth Circuit reverses (No. 23-20181; opinion revised February 14, 2025), reading "open market purchase" as a purchase in the secondary market for syndicated loans and holding that a privately negotiated exchange with a subset of lenders falls outside it, breaching the sacred right of pro rata sharing. **July 7, 2026:** on remand, the bankruptcy court awards the excluded lenders \$261.13mm, measured at the June 22, 2020 breach date, plus New York statutory prejudgment interest at 9% per annum from that date. *The Ad Hoc Group, through counsel, wishes to state that it has always supported pro rata treatment, in principle, for other people.*

Kaz, reading the Docket Diary, asks who enforces sacred rights. "Is there a priest?" Mags: "The Fifth Circuit, apparently. Four and a half years later, at nine percent simple." The arithmetic is worth doing, because it is the recovery distribution Kaz will later try to model as a Gaussian. Simple interest at 9% for the roughly 6.04 years from June 22, 2020 to July 7, 2026 adds about 54% to the award, taking it to roughly \$403mm *(our arithmetic; approx.)*. The excluded lenders' recovery on this claim was not a draw from a bell curve. It was a mass point at zero for four and a half years, then a judgment, delivered six years after the breach, whose size depended on two words in a 2016 credit agreement. "Open market purchase": the most expensive three words in finance, \$261.13 million before interest, according to a court that had six years to think about it.

The same day the Fifth Circuit ruled, a New York appellate court upheld Mitel's 2022 uptier (*Ocean Trails CLO VII v. MLN Topco*, App. Div. 1st Dept., December 31, 2024), because Mitel's exception permitted a "purchase" with no "open market" qualifier. "So the difference between a quarter of a billion dollars of damages and zero is two words?" asks Kaz. "Two words and a forum," says Mags. This is the strongest argument in the book for putting a document-reading human in the loop of a systematic model: the likelihood ratio of "sponsor-backed loan, 52% holder concentration, quoted in the 40s" is not a number until you have read the pro rata sharing section.

**What the blotter would have shown.** Run the chapter's machinery on the spring of 2020 *(stylized; the pre-deal price path below is illustrative, not taken from the record)*.

*The prior.* A first-lien term loan with no uptier blocker, an undefined "open market purchase" exception, a sponsor under liquidity pressure in a pandemic, and a holder base where one group could plausibly reach a majority: the PRS is high, so the CUSUM threshold $h(\text{PRS})$ is low.

*The flow.* To take a 52.6% position into a deal, a group needs to hold it, and any group short of a majority needs to buy. The signature the detector looks for is net buying in the first-lien tranche concentrated in a few counterparty types, with the issuer's other instruments relatively quiet. Whether the actual flow in May and June 2020 looked like this is an empirical question this book has not answered (the event study is on the Edition 2 list); the point is that the detector is designed to ask it.

*The quote.* Suppose the desk's horizon prior on the loan is two-point: about 45 if no non-pro-rata deal happens and about 25 if it does and the desk's lot is left outside, with a 70% prior on no deal *(illustrative)*. The mid is $0.7 \times 45 + 0.3 \times 25 = 39$. With a feature-implied $\pi(x) = 0.3$ for a sell RFQ in this tranche, the asymmetric GM formula gives a half-spread of

$$
m - b = 20 \times \frac{0.7 \times 0.3 \times 0.3}{0.35 + 0.3 \times 0.3} \approx 2.9 \text{ points},
$$

a bid near 36, against a desk that, assuming $\pi = 0$, would bid close to the 39 mid. Both bids lose money if the deal happens. The difference is that the first one is priced to lose money only as often as the model says it should.

*The hand history.* Any dealer that carried long inventory of the excluded paper into June 22, 2020 had its markout delivered in one print. The 2026 remand's breach-date valuation of the excluded loans at 25 cents on the dollar is the closest thing to an official markout this market produces.

*After the announcement.* The remand opinion's mitigation testimony gives a rare look at post-LMT liquidity. Barclays was described as the lead market maker in Serta debt. Up to \$186mm face of first-lien term loans traded between June 2020 and December 31, 2021, and defense experts argued the excluded lenders could have sold 29% to 43% of that observed volume, or \$62mm to \$94mm, against holdings of about \$895mm. In other words, even a holder who wanted out could have sold at most about a tenth of the position over eighteen months. Left-behind paper is not just cheaper. It is stuck, and a market maker's inventory limit in it is set by that fact, not by a volatility estimate.

**The counter-technology.** Holders learned. Excluded-lender risk is now managed before the fact, through cooperation agreements in which a majority of a class agrees to negotiate only together, and through blockers written into new documents. (Cooperation agreements signed in this book so far: 1.) For the detector, a cooperation agreement is a regime change: it raises the bar for a non-pro-rata deal, which lowers the PRS, and it also creates a large restricted population whose silence the model must not mistake for calm.

## 3.8 The Engine: RFQ Adverse Selection, Markouts, 8-K Updates and the Pre-LMT Detector

### Specification for AI Implementation

**The Spec You Hand the Robot.** Theo's first attempt at a spec was one line: "Build a quoting engine that minimizes markouts." ROBO built exactly that. It quoted every bid forty points below the mid. Markout on fills: zero, because there were no fills. Hit rate: zero. Franchise: zero. ROBO did not complain, and it did not guess; it minimized the objective it was given. The precise version maximizes expected PnL *subject to* a hit-ratio target, which is how Barzykin and Ciceri (HSBC) formulate bond market making with a hit-ratio constraint (arXiv 2604.20406, 2026): dualize the target into a Lagrange multiplier and the quote decomposes into a riskless spread, an inventory correction and a hit-ratio correction. Ines calls the multiplier "paying to stay at the table." This chapter's engine implements the riskless-spread and inventory pieces, (3.1)–(3.2); Chapter 18 adds the hit-ratio term.

**Module.** `ch03_rfq_adverse_selection.py`; numpy, scipy and pandas only; one seeded generator `rng = np.random.default_rng(3)` shared by all blocks; blocks run in order in one interpreter.

**RFQ record schema (one row per RFQ, `float64` unless stated).**

| Field | Type / units | Notes |
| :--- | :--- | :--- |
| `rfq_id`, `cpty`, `issuer`, `tranche` | string | `cpty` is an internal id, never a name in logs shipped off-desk |
| `ts` | UTC timestamp, ms | RFQ arrival; all features must be computable from data with timestamps strictly before `ts` |
| `eta` | int8 in $\{+1, -1\}$ | $+1$ if the dealer would buy (client sells) |
| `size` | \$mm face | Signed by `eta` in inventory formulas |
| `mid`, `sigma_v`, `sigma_ido` | price points | `sigma_v` is physical, over the holding horizon; never an implied vol, never spread units |
| `n_dealers` | int | Number of dealers in competition, as reported by the platform |
| `x_*` | float | Features of §3.2.2, each with its own as-of timestamp |
| `outcome` | category | Done / Covered / Traded Away / Not Traded |
| `cover` | price points or null | Second-best price, when reported |
| `mid_1d`, `mid_5d`, `mid_20d`, `sys_*d` | price points | Horizon mids and systematic moves for IDO markouts |

**Edge cases and guards.** Reject `pi` outside $[0,1]$, `q` outside $(0,1)$ and negative gaps; never let a spread-unit `sigma_v` reach a price-unit formula (unit-tag the column). Compute the logistic function through `tanh` to avoid overflow. Fit likelihoods on means, not sums, so optimizer tolerances are scale-free. Counterparty scores must be shrunk, and the shrinkage intensity floored at zero, never negative. CUSUM thresholds are floored so that no single observation can trigger an alarm. Every feature must be point-in-time: an 8-K's `file_date` and acceptance time, not its period-of-report date.

**Block 1: the quote.** Equation (3.1) and its asymmetric form, the winner's-curse shading and equation (3.2).

```python
import numpy as np
import pandas as pd
from scipy import optimize

rng = np.random.default_rng(3)


def sigmoid(z):
    """Overflow-safe logistic function."""
    return 0.5 * (1.0 + np.tanh(0.5 * np.asarray(z, dtype=float)))


def gm_half_spread(pi, q, delta):
    """Exact Glosten-Milgrom half-spread m - b for a SELL RFQ (eq. 3.1, asymmetric form).
    pi: P(sender informed); q: P(V = V+); delta: V+ - V- in price points.
    For a BUY RFQ the ask-side half-spread is gm_half_spread(pi, 1 - q, delta)."""
    pi, q, delta = (np.asarray(a, dtype=float) for a in (pi, q, delta))
    if np.any((pi < 0) | (pi > 1)) or np.any((q <= 0) | (q >= 1)) or np.any(delta < 0):
        raise ValueError("require 0 <= pi <= 1, 0 < q < 1, delta >= 0")
    return delta * q * (1.0 - q) * pi / (0.5 * (1.0 - pi) + pi * (1.0 - q))


def winners_curse_w(n_dealers, w_per_log=0.15):
    """Shading in units of sigma_v: w(1) = 0, increasing in n. Calibrate w_per_log from cover prices."""
    n = np.maximum(np.asarray(n_dealers, dtype=float), 1.0)
    return w_per_log * np.log(n)


def gm_bid(mid, sigma_v, pi_hat, n_dealers, q_inv, size, gamma, sigma_ido, w_per_log=0.15):
    """Eq. (3.2), vectorized over RFQs. Prices and sigmas in points over the holding horizon;
    q_inv and size in $mm face (size > 0 means the dealer buys); gamma in 1/(point * $mm)."""
    sigma_v = np.asarray(sigma_v, dtype=float)
    adverse = gm_half_spread(pi_hat, 0.5, 2.0 * sigma_v)
    curse = winners_curse_w(n_dealers, w_per_log) * sigma_v
    inventory = 0.5 * gamma * np.asarray(sigma_ido, dtype=float) ** 2 * (2.0 * np.asarray(q_inv, dtype=float) + size)
    return np.asarray(mid, dtype=float) - adverse - curse - inventory


# Sanity checks against the closed forms in the text
assert np.isclose(gm_half_spread(0.12, 0.5, 2 * 1.5), 0.12 * 1.5)          # eq. (3.1): pi * sigma_v
assert np.isclose(gm_half_spread(0.3, 0.7, 20.0), 20 * 0.063 / 0.44)       # Serta stylized: ~2.86 points
ratio = gm_half_spread(1e-5, 0.7, 20.0) / (2 * 1e-5 * 0.7 * 0.3 * 20.0)
assert abs(ratio - 1.0) < 1e-3                                              # small-pi approximation
assert np.all(np.diff(gm_half_spread(np.linspace(0, 1, 11), 0.5, 3.0)) > 0)  # monotone in pi
assert np.isclose(gm_bid(87.0, 1.5, 0.0, 1, 0.0, 0.0, 0.0, 1.0), 87.0)      # no information, no risk: bid = mid
```

**Block 2: a simulated RFQ tape, the zero-profit property and the winner's curse.** Informed senders know the two-point value; uninformed senders pick a side at random; the true $\pi(x)$ is logistic in three features. Competitors share a weak signal about the value, which is what creates the winner's curse.

```python
BETA_TRUE = np.array([-2.5, 0.6, 1.0, 1.2])   # intercept, size z-score, event window, distressed counterparty
SIGMA_V = 1.5                                  # points over the horizon


def simulate_rfq_flow(n_rfq=200_000, sigma_v=SIGMA_V, noise_sd=0.25, rho=0.3, rng=rng):
    """Simulated RFQ tape (prices in points). eta = +1 when the DEALER buys (client sells)."""
    size_z = rng.standard_normal(n_rfq)
    event = (rng.random(n_rfq) < 0.20).astype(float)        # within 72h of a scheduled event
    distressed = (rng.random(n_rfq) < 0.25).astype(float)   # distressed-fund counterparty flag
    X = np.column_stack([np.ones(n_rfq), size_z, event, distressed])
    pi_true = sigmoid(X @ BETA_TRUE)
    informed = rng.random(n_rfq) < pi_true
    u = np.where(rng.random(n_rfq) < 0.5, 1.0, -1.0)        # V = mid + u * sigma_v
    mid = rng.uniform(70.0, 100.0, n_rfq)
    client_sells = np.where(informed, u < 0, rng.random(n_rfq) < 0.5)
    eta = np.where(client_sells, 1.0, -1.0)
    n_dealers = rng.integers(2, 9, n_rfq)                   # 2..8 dealers in competition
    mid_h = mid + u * sigma_v + noise_sd * rng.standard_normal(n_rfq)
    # Competitors' price concessions (lower = better for the client); they share a signal about u.
    conc = sigma_v * (0.08 + 0.10 * np.abs(rng.standard_normal((n_rfq, 7))))
    conc[np.arange(7)[None, :] >= (n_dealers - 1)[:, None]] = np.inf
    eff = conc - (eta * rho * sigma_v * u)[:, None]
    eff_sorted = np.sort(eff, axis=1)
    tape = pd.DataFrame({"size_z": size_z, "event": event, "distressed": distressed,
                         "pi_true": pi_true, "informed": informed, "mid": mid, "eta": eta,
                         "n_dealers": n_dealers, "mid_h": mid_h,
                         "best_comp": eff_sorted[:, 0], "second_comp": eff_sorted[:, 1]})
    return tape, X


def se(x):
    x = np.asarray(x, dtype=float)
    return x.std(ddof=1) / np.sqrt(x.size)


df, X = simulate_rfq_flow()

# Test A: a single dealer that fills every RFQ. GM with the true pi(x) is zero-profit; quoting mid is not.
h_gm = gm_half_spread(df["pi_true"].to_numpy(), 0.5, 2 * SIGMA_V)
px_gm = df["mid"].to_numpy() - df["eta"].to_numpy() * h_gm       # bid if the dealer buys, ask if it sells
mo_gm = df["eta"].to_numpy() * (df["mid_h"].to_numpy() - px_gm)
mo_mid = df["eta"].to_numpy() * (df["mid_h"].to_numpy() - df["mid"].to_numpy())
assert abs(mo_gm.mean()) < 3 * se(mo_gm), mo_gm.mean()
assert abs(mo_mid.mean() - (-SIGMA_V * df["pi_true"].mean())) < 3 * se(mo_mid)
assert mo_mid.mean() < -10 * se(mo_mid)                           # assuming pi = 0 loses, unmistakably


# Test B: competition. Outcomes follow the Done / Covered / Traded Away taxonomy.
def rfq_outcomes(h_ours, best_comp, second_comp):
    done = h_ours < best_comp
    covered = (~done) & (h_ours < second_comp)
    return np.where(done, "Done", np.where(covered, "Covered", "Traded Away"))


df["outcome"] = rfq_outcomes(h_gm, df["best_comp"].to_numpy(), df["second_comp"].to_numpy())
df["mo_gm"] = mo_gm
fills = (df["outcome"] == "Done").to_numpy()
mo_fill, mo_lost = mo_gm[fills], mo_gm[~fills]                    # lost RFQs: counterfactual markouts
assert 0.02 < fills.mean() < 0.98
assert mo_fill.mean() < -3 * se(mo_fill)        # right pi(x), still losing on fills: the winner's curse
assert mo_lost.mean() > mo_fill.mean()          # the hands you lose are better than the hands you win
h_shaded = h_gm + winners_curse_w(df["n_dealers"].to_numpy()) * SIGMA_V
fills_shaded = h_shaded < df["best_comp"].to_numpy()
print(df["outcome"].value_counts(normalize=True).round(3).to_dict())
print(f"fills {fills.mean():.3f}, mean markout {mo_fill.mean():+.3f} pts; "
      f"lost (counterfactual) {mo_lost.mean():+.3f} pts; "
      f"with w(n) shading: fills {fills_shaded.mean():.3f}, "
      f"markout {(df['eta'].to_numpy() * (df['mid_h'].to_numpy() - (df['mid'].to_numpy() - df['eta'].to_numpy() * h_shaded)))[fills_shaded].mean():+.3f} pts")
```

**Block 3: fitting $\pi(x)$ from markout signs.** Under the symmetric model, a filled RFQ is followed by an adverse move with probability $(1 + \pi(x))/2$, so we fit that link directly by maximum likelihood rather than forcing a plain logistic regression onto the adverse-sign label.

```python
def fit_pi(X, adverse):
    """MLE of beta in P(adverse | x) = (1 + sigmoid(x'beta)) / 2 (Sec. 3.2.2).
    Returns (beta_hat, standard errors from the expected Fisher information)."""
    X = np.asarray(X, dtype=float)
    y = np.asarray(adverse, dtype=float)
    n, eps = X.shape[0], 1e-12

    def nll_and_grad(b):
        s = sigmoid(X @ b)
        p = np.clip(0.5 * (1.0 + s), eps, 1.0 - eps)
        dp = 0.5 * s * (1.0 - s)
        nll = -np.mean(y * np.log(p) + (1.0 - y) * np.log(1.0 - p))
        grad = -(X.T @ ((y / p - (1.0 - y) / (1.0 - p)) * dp)) / n
        return nll, grad

    res = optimize.minimize(nll_and_grad, np.zeros(X.shape[1]), jac=True, method="L-BFGS-B")
    assert np.isfinite(res.fun)
    s = sigmoid(X @ res.x)
    p = 0.5 * (1.0 + s)
    weight = (0.5 * s * (1.0 - s)) ** 2 / (p * (1.0 - p))
    info = X.T @ (X * weight[:, None])
    return res.x, np.sqrt(np.diag(np.linalg.inv(info)))


adverse = (df["eta"].to_numpy() * (df["mid_h"].to_numpy() - df["mid"].to_numpy()) < 0).astype(float)
beta_hat, beta_se = fit_pi(X, adverse)
assert np.all(np.abs(beta_hat - BETA_TRUE) < 4 * beta_se), (beta_hat, beta_se)
pi_hat = sigmoid(X @ beta_hat)
assert np.corrcoef(pi_hat, df["pi_true"].to_numpy())[0, 1] > 0.95

# Theo's Friday RFQ: large, inside a lender-call window, from a distressed-fund account; 8 dealers.
x_theo = np.array([1.0, 1.5, 1.0, 1.0])
pi_theo = float(sigmoid(x_theo @ beta_hat))
bid_theo = float(gm_bid(87.0, 6.0, pi_theo, 8, q_inv=5.0, size=15.0, gamma=0.002, sigma_ido=3.0))
assert 0.0 < pi_theo < 1.0 and bid_theo < 87.0
print(f"pi_hat = {pi_theo:.2f}; GM bid with a weekend sigma_v of 6 points = {bid_theo:.2f}")
```

**Block 4: IDO markouts and shrunk counterparty scores.** The IDO reference implements §3.3.3; the hand from §3.3 is the regression test.

```python
def ido_reference_move(p_ref, d_spr, beta, d_index_spread, d_mod, d_tsy):
    """Systematic price move (points) implied by index-spread and Treasury-yield changes (decimals)."""
    return p_ref * (-d_spr * beta * d_index_spread - d_mod * d_tsy)


def markouts_bp(fills_df, horizons=(1, 5, 20)):
    """Columns needed: p0, eta, mid_{h}d; optional sys_{h}d (systematic move, points) for IDO markouts."""
    out = {}
    for h in horizons:
        ref = fills_df[f"mid_{h}d"] - fills_df.get(f"sys_{h}d", 0.0)
        out[f"mo_{h}d_bp"] = fills_df["eta"] * (ref - fills_df["p0"]) / fills_df["p0"] * 1e4
    return pd.DataFrame(out, index=fills_df.index)


hand = pd.DataFrame({"p0": [85.75], "eta": [1.0], "mid_5d": [81.0],
                     "sys_5d": [ido_reference_move(87.0, 3.5, 1.3, 0.0020, 3.6, -0.0010)]})
assert np.isclose(hand["sys_5d"].iloc[0], -0.4785, atol=1e-3)
assert -510 < markouts_bp(hand, horizons=(5,)).iloc[0, 0] < -490     # about -500bp of price


def shrunk_cpty_scores(fills_df, col="mo_bp"):
    """Empirical-Bayes shrinkage of per-counterparty mean markouts (Sec. 3.3.4)."""
    g = fills_df.groupby("cpty")[col]
    n_c, mean_c = g.size(), g.mean()
    dof = (n_c - 1).sum()
    sigma2 = float((g.var(ddof=1).fillna(0.0) * (n_c - 1)).sum() / max(dof, 1))   # pooled per-fill variance
    tau2 = max(float(mean_c.var(ddof=1) - (sigma2 / n_c).mean()), 0.0)
    k = n_c / (n_c + sigma2 / tau2) if tau2 > 0 else n_c * 0.0
    return pd.DataFrame({"n": n_c, "raw": mean_c, "shrink": k, "theta_hat": k * mean_c}), tau2, sigma2


n_cp, tau_true, sig_mo = 400, 20.0, 150.0                    # bp
theta = rng.normal(0.0, tau_true, n_cp)
n_fills = rng.geometric(1 / 40, n_cp)                        # every counterparty has at least one fill
cp = np.repeat(np.arange(n_cp), n_fills)
panel = pd.DataFrame({"cpty": cp, "mo_bp": theta[cp] + sig_mo * rng.standard_normal(cp.size)})
scores, tau2_hat, sigma2_hat = shrunk_cpty_scores(panel)
assert scores["shrink"].between(0.0, 1.0).all() and tau2_hat >= 0.0
mse_raw = np.mean((scores["raw"].to_numpy() - theta) ** 2)
mse_eb = np.mean((scores["theta_hat"].to_numpy() - theta) ** 2)
assert mse_eb < mse_raw
print(f"tau_hat = {np.sqrt(tau2_hat):.1f}bp (true {tau_true}); MSE raw {mse_raw:.0f} vs shrunk {mse_eb:.0f}")
```

**Block 5: the Bayesian 8-K and the base-rate correction.** Equations (3.3) and (3.4), with the worked example of §3.4.2 as a regression test.

```python
def elkan(p, S, T):
    """Eq. (3.4): re-base a PD calibrated to sample default rate S onto live base rate T."""
    p = np.asarray(p, dtype=float)
    return T * (p - p * S) / (S - p * S + p * T - S * T)


def update_pd_from_8k(p_prior, lr, S=None, T=None):
    """Eq. (3.3). Optional Elkan re-basing of the prior first. lr = P(E | default) / P(E | no default)."""
    p = np.asarray(p_prior, dtype=float)
    lr = np.asarray(lr, dtype=float)
    if np.any((p < 0) | (p > 1)) or np.any(lr < 0):
        raise ValueError("require p in [0, 1] and lr >= 0")
    if S is not None and T is not None:
        p = elkan(p, S, T)
    return lr * p / (1.0 - p + lr * p)


def hazard_from_pd(p, horizon_years=1.0):
    return -np.log1p(-np.asarray(p, dtype=float)) / horizon_years


grid = np.linspace(0.0, 1.0, 101)
assert np.allclose(update_pd_from_8k(grid, 1.0), grid)                         # LR = 1 is no news
assert np.all(np.diff(update_pd_from_8k(0.06, np.linspace(0.1, 10.0, 50))) > 0)  # monotone in LR
p_post = float(update_pd_from_8k(0.06, 2.5))
assert np.isclose(p_post, 0.1376, atol=5e-4)
ds_bp = 0.6 * 2.0 * (hazard_from_pd(p_post) - hazard_from_pd(0.06)) * 1e4      # L = 0.6, kappa = 2
assert 1000 < ds_bp < 1070                                                       # about 1,030bp
S_, T_ = 0.02, 0.05
e = elkan(grid, S_, T_)
assert np.all((e >= -1e-12) & (e <= 1 + 1e-12)) and np.isclose(elkan(0.5, 0.2, 0.2), 0.5)
assert np.all((T_ / S_) * grid[grid > S_ / T_ + 1e-9] > 1.0)                    # the T/S shortcut breaks the bound
odds = lambda z: z / (1.0 - z)
inner = grid[1:-1]
assert np.allclose(odds(elkan(inner, S_, T_)), odds(inner) * odds(T_) / odds(S_))  # (3.4) is an odds update
print(f"posterior PD {p_post:.4f}; implied spread move {ds_bp:,.0f}bp")
```

**Block 6: the pre-LMT detector.** Page's CUSUM (3.5), vectorized over paths, the Lorden false-alarm bound as a test, and the PRS-dependent threshold.

```python
def cusum_lmt_detector(y, mu1, sigma_y, h):
    """Eq. (3.5) on a (T,) or (T, n_paths) array of ADV-scaled net informed-type buying.
    Returns (statistic path, first alarm index per path or -1)."""
    y = np.asarray(y, dtype=float)
    y2 = y.reshape(y.shape[0], -1)
    llr = (mu1 / sigma_y ** 2) * (y2 - 0.5 * mu1)
    stat = np.empty_like(y2)
    s = np.zeros(y2.shape[1])
    for t in range(y2.shape[0]):
        s = np.maximum(0.0, s + llr[t])
        stat[t] = s
    thresh = np.broadcast_to(np.asarray(h, dtype=float), (y2.shape[1],))
    hit = stat > thresh[None, :]
    first = np.where(hit.any(axis=0), hit.argmax(axis=0), -1)
    return stat.reshape(y.shape), first


def prs_threshold(prs, h0=6.0, h_min=2.5, h_max=10.0):
    """h(PRS) = h0 - logit(PRS), floored so that one noisy day cannot fire the alarm."""
    prs = np.clip(np.asarray(prs, dtype=float), 1e-6, 1.0 - 1e-6)
    return np.clip(h0 - np.log(prs / (1.0 - prs)), h_min, h_max)


h_design, mu1, sig_y, t_max, n_paths = 4.0, 1.0, 1.0, 6000, 500
_, first_h0 = cusum_lmt_detector(rng.standard_normal((t_max, n_paths)), mu1, sig_y, h_design)
run_len = np.where(first_h0 >= 0, first_h0 + 1, t_max)       # censored paths count as t_max (conservative)
assert run_len.mean() >= np.exp(h_design)                     # Lorden: ARL to false alarm >= e^h
_, first_h1 = cusum_lmt_detector(mu1 + rng.standard_normal((400, n_paths)), mu1, sig_y, h_design)
kl = mu1 ** 2 / (2 * sig_y ** 2)
assert np.all(first_h1 >= 0) and (first_h1 + 1).mean() < 2 * h_design / kl + 5
p_grid = np.linspace(0.05, 0.95, 19)
assert np.all(np.diff(prs_threshold(p_grid)) <= 0) and np.isclose(prs_threshold(0.5), 6.0)
print(f"ARL0 >= {run_len.mean():.0f} days (bound {np.exp(h_design):.0f}); "
      f"mean detection delay {(first_h1 + 1).mean():.1f} days (h/KL = {h_design / kl:.0f})")
```

**What the coding agent must not do.** It must not fit $\pi(x)$ on fills only and call the result unbiased (Block 2 shows why). It must not compute markouts against a mid it has not checked for staleness. It must not let the 8-K parser use a filing's period-of-report date as its event time. It must not feed restricted-list names into the detector's counterparty set as if their silence were absence of interest. And it must not "improve" the zero-profit bid by removing the adverse-selection term because a backtest on fills says it is too wide; that backtest is the winner's curse talking.

## 3.9 Desk Debrief

*Thursday, 4:40 p.m. The lender call was Monday. The Brambleworth mid is 81.*

Theo has printed the markout. He knows that printing things is a banker's tell, and he does it anyway, because some numbers deserve paper. The dealer who won Friday's auction bought fifteen million at 85¾ and is now sitting on an IDO markout of about $-500$bp of price. Theo's counterfactual at 85½ is about $-470$bp. He lost the auction by a quarter of a point and, in doing so, avoided roughly \$600,000 of idiosyncratic loss *(illustrative; the hand of §3.3)*.

"I was right," he says.

"You were second," says Ines. "Second is not a strategy. Second is a coin that landed well. Why did you bid three-quarters under Kaz?"

Theo thinks about it honestly. "It felt wrong. Friday, lender call Monday, a distressed-fund account, fifteen million."

"That's four features and a flinch. The flinch was $\pi(x)$ with no calibration. Everything in this chapter is the flinch, written down, fitted and checked against the hand history. Do it on the next five thousand RFQs, then tell me you were right."

Kaz, without turning around: "I've replaced the Gaussian with a two-point mixture."

"Progress," says Mags. "Now it can be wrong in two places at once."

Theo puts the USB stick on the desk next to the printout. It still holds the 13-week model, and it now also holds a column called `liquidity_runway_weeks`. It is no longer emotional support. It has a refresh cadence and a decay horizon, which is more than most emotional support can say.

- **A survival question is a distribution with the variance left out.** The price is the mean. The dealer is paid for the conditional variance over the *holding horizon*, $\sigma_V^2(h)$, not over the life of the case, and a calendar event inside the horizon (a lender call, an 8-K deadline, a grace-period expiry) moves that variance more than any covenant does. Moyer's 62.5% was always a two-point distribution.
- **A bid is a posterior, not a markup.** $b = \mathbb{E}^{\mathbb{P}}[V \mid \text{client sells}]$, which for a symmetric two-point value is $m - \pi\,\sigma_V$ (3.1). The uninformed seller pays $\pi\sigma_V$ for the privilege of trading in a market that contains informed sellers. Charging it is what keeps you at zero; skipping it makes you the client's free data vendor.
- **Winning is information.** With $n$ dealers in competition, condition on winning: shade by $w(n)\,\sigma_V$ and carry the inventory term (3.2). The hands you lose look better than the hands you win. That is the winner's curse, and a backtest run on fills alone cannot see it.
- **Markouts are the hand history; IDO markouts are the honest hand history.** Measure at 1, 5 and 20 business days, strip index-spread and Treasury beta first, shrink counterparty scores toward zero, and never compute a markout against a mid you have not checked for staleness. A raw markout will accuse a pension fund of insider trading for owning beta.
- **An 8-K is a likelihood ratio with a filing date.** Update in odds (3.3), re-base with Elkan (3.4) when the training sample's default rate is not the live one, use the acceptance timestamp as the event time, and say out loud what $\kappa$ is when you cross from $\mathbb{P}$ to $\mathbb{Q}$. The lazy version sets $\kappa = 1$ and understates the spread move by a factor of $\kappa$ (by half, at the worked example's $\kappa = 2$) without telling anyone.
- **The Edge Ledger prices what you know.** Every RSSG skill becomes a feature with a data source, a refresh cadence, a half-life and a list of who else has it. Put features on a common clock before you add them, and remember that the edge in a document-derived feature is the cost of extracting it, which decays far more slowly than a statistic anyone can compute.
- **Pre-LMT flow is the purest adverse selection in credit, and it is sequentially detectable.** Run a CUSUM (3.5) on ADV-scaled net buying by LME-prone, *unrestricted* counterparties, with the threshold lowered by the Priming Risk Score. A restricted counterparty's silence is a feature, not calm.
- **The document matters more on the desk than it did at the bank.** Serta and Mitel were decided on the same day on different words, and two of them, "open market," were worth \$261.13mm before interest. The likelihood ratio of a flow pattern is conditional on the pro rata sharing section, which is the one input the ex-RSSG reader parses faster than any model in the building.

### The Spec You Hand the Robot

*The vague version.* Theo's first draft of the detector spec was one sentence: "Flag counterparties who know about an LMT before it happens." ROBO built it exactly. On its first morning in production, the top alert was the desk itself, because the most concentrated net buyer of distressed first-lien paper in the RFQ log was the dealer making markets in it. The second alert was the Ad Hoc Group, which was correct and useless: compliance had restricted the desk from trading against it three weeks earlier, and the alert was a well-calibrated description of a wall the firm had built on purpose. ROBO did not complain. It had been told to find concentrated buyers, and it found them.

The precise version, ready to paste:

> Build a Python module `ch03_rfq_adverse_selection` (numpy, scipy, pandas only; one generator `np.random.default_rng(3)`; pure, vectorized functions; no network or file I/O in the core). All expectations are under $\mathbb{P}$, the desk's physical beliefs, except the spread translation in (6). Prices are in points per 100 par, sizes in \$mm face, horizons in business days.
>
> 1. `gm_half_spread(pi, q, delta)`: the exact asymmetric Glosten–Milgrom half-spread for a sell RFQ (§3.2.1); the buy side is `gm_half_spread(pi, 1 - q, delta)`. Raise on `pi` outside $[0,1]$, `q` outside $(0,1)$, or `delta < 0`.
> 2. `gm_bid(mid, sigma_v, pi_hat, n_dealers, q_inv, size, gamma, sigma_ido, w_per_log)`: equation (3.2). `sigma_v` is the physical value volatility over the holding horizon in points; the column is unit-tagged and a spread-unit input raises. `size > 0` means the dealer buys; `gamma` is in $1/(\text{point}\cdot\$\text{mm})$. Return the bid *and* its three components (adverse selection, winner's curse, inventory) for logging.
> 3. `fit_pi(X, adverse)`: maximum likelihood for $\mathbb{P}(\text{adverse} \mid x) = \tfrac12(1 + \sigma(x^\top\beta))$, fitted on Done RFQs **and** on counterfactual markouts of Covered and Traded Away RFQs; mean log-likelihood; return $\hat\beta$ and Fisher standard errors. Every feature is point-in-time: computable from data stamped strictly before the RFQ's `ts`.
> 4. `markouts_bp(fills, horizons=(1, 5, 20))` with an IDO variant per §3.3.3. A mid older than `max_stale_days` (default 5) is flagged and excluded, never used.
> 5. `shrunk_cpty_scores(fills)`: empirical-Bayes shrinkage of per-counterparty mean IDO markouts; between-counterparty variance floored at zero; output `n`, `raw`, `shrink`, `theta_hat`. Counterparty names never leave the desk; logs carry internal ids.
> 6. `update_pd_from_8k(p_prior, lr, S=None, T=None)`: equation (3.3), with optional Elkan re-basing (3.4). The event time is the filing's EDGAR acceptance timestamp, never the period-of-report date. A companion `spread_move(p_prior, p_post, L, kappa)` returns $L\,\kappa\,(\lambda' - \lambda)$ in bp; `L` and `kappa` are required arguments with no defaults, because $\kappa = 1$ must be a decision, not an accident.
> 7. `cusum_lmt_detector(y, mu1, sigma_y, h)` and `prs_threshold(prs, h0, h_min, h_max)`: equation (3.5). `y` is ADV-scaled net *client* buying of one tranche by LME-prone counterparties that are not on the restricted list. Exclude the desk's own principal flow and all inter-dealer prints. Restricted counterparties enter as a separate "silence" feature (the drop in their usual axe and inquiry frequency), never as zeros in `y`. The floor `h_min` guarantees that no single observation can fire an alarm.
>
> **Tests that must pass.** On a simulated tape, a single dealer quoting GM with the true $\pi(x)$ earns zero within three standard errors, and quoting mid loses about $\bar\pi\,\sigma_V$; under competition, mean fill markouts are negative and lost-RFQ counterfactuals are better; $\hat\beta$ is within four standard errors of the truth; shrunk scores beat raw scores in mean squared error; a likelihood ratio of one is the identity; the worked 8-K example gives $p' = 0.1376$ and about 1,030bp at $L = 0.6$, $\kappa = 2$; on null paths the CUSUM's average run length is at least $e^{h}$, and on alternative paths the mean delay is close to $h/K$.
>
> **Per-RFQ log.** $\hat\pi$; each bid component; outcome (Done, Covered, Traded Away, Not Traded); cover price where reported; raw and IDO markouts at 1, 5 and 20 days; detector state and threshold for every tranche of the issuer.
>
> **Do not.** Fit $\pi$ on fills only. Remove the adverse-selection term because a fills-only backtest says the bid is too wide. Use period-of-report dates. Let one observation fire an alarm. Read a cooperation agreement's restricted population as calm. Add a hit-ratio target; that is Chapter 18's job. Until then the engine quotes the zero-profit bid and reports its hit ratio, and nobody asks it to minimize markouts, which is how ROBO ended up bidding forty points below the mid.

### Exercises

1. **(Moyer's footnote, with a clock.)** The near-dated bond trades at 85. Model A is Moyer's two-point distribution: 100 with probability 0.625, 60 with probability 0.375. Model B has three outcomes: refinancing at 100 (probability 0.50), a distressed exchange worth 80 (0.25) and Chapter 11 worth 60 (0.25). (a) Show that both models price the bond at 85 and compute their standard deviations. (b) For Model A, compute the exact asymmetric Glosten–Milgrom half-spreads at $\pi = 0.1$ for a sell RFQ and for a buy RFQ, and compare them with the symmetric approximation $\pi \times \text{sd}$. Explain in one sentence why the sell side is wider. (c) Suppose only 20% of the between-scenario variance resolves within a five-day hold and the diffusive volatility is 1.5 points per square-root day. Use §3.1.3 to compute $\sigma_V(5)$ for each model and the approximate zero-profit bid at $\pi = 0.1$. Which moves the quote more, the choice between Models A and B or the horizon?
   *Answer check:* (a) 19.36 and 16.58 points. (b) 1.92 points for a sell RFQ and 1.83 for a buy, against 1.94: with $q = 0.625$ the bad state is the less likely one, so a sell, which points toward it, moves the posterior further than a buy, which points where the prior already leans. (c) $\sigma_V(5) \approx 9.29$ and 8.14 points, bids of about 84.07 and 84.19. The model choice moves the bid by about a tenth of a point and the horizon moves it by about a point. The banker's instinct to argue about scenario probabilities is right about the case and wrong about the quote.

2. **(Switch off the winner's curse.)** In Block 2 of §3.8, set `rho=0`, so that competitors' quotes carry no information about the value. (a) Which assertion in Test B fails, and why is that the correct failure? (b) Using Milgrom and Weber's (1982) distinction between private and common values, explain why a winner's curse needs a common-value component, and argue that the post-trade value of a bond is almost purely a common value. (c) A platform reports the cover price to the winner of each Done RFQ. Explain how covers let you evaluate a *larger* shading $w(n)$ on historical data without re-running any auction, and why they cannot tell you what a *smaller* $w(n)$ would have won.
   *Answer check:* (a) `mo_fill.mean() < -3 * se(mo_fill)` fails. With `rho = 0`, whether you win depends only on $x$ and on noise independent of the value, so $\mathbb{E}[\text{MO} \mid \text{fill}, x] = \mathbb{E}[\text{MO} \mid x] = 0$. A test that still passed with its effect switched off would be testing nothing. (c) A won RFQ stays won under extra shading $\Delta$ exactly when the shaded price still beats the cover, so you can recompute the Done set and its markouts for any larger $w$. Whether a tighter quote would have won an RFQ you lost depends on the winning level, which many protocols never show the losers, so the curve is identified in one direction only. Ines: "The cover is the hand you didn't see. It only gets shown to the player who won the pot."

3. **(Kaz's bag of words, de-biased.)** Kaz trains a classifier on a *balanced* sample of 8-Ks containing the phrase "liability management": half from filers that defaulted within a year and half from filers that did not, so $S = 0.5$. In the live corpus the one-year default rate among filers using the phrase is $T = 0.03$ *(illustrative)*, because most of them are investment-grade issuers running tender offers (see the Trend Watch in §3.4). (a) A filing scores $p = 0.9$. Compute the Elkan-corrected probability (3.4). (b) Compute Kaz's shortcut $p\,T/S$, say in which direction it errs, and explain why the error grows as $p \to 1$. (c) Theo conditions the live base rate on "sponsor-backed and rated B3 or below," for which $T = 0.15$ *(illustrative)*. Recompute both numbers. (d) Using one-year hazards, $L = 0.6$ and $\kappa = 2$, how many basis points of spread separate the corrected answer in (a) from the shortcut? (e) Explain to Kaz, in one sentence and without the word "prior," why a balanced training set is not a balanced world.
   *Answer check:* (a) 0.218. (b) 0.054, too low: the correction acts on odds, and the shortcut rescales probabilities; as $p \to 1$ the corrected value tends to one while the shortcut tends to $T/S$. (c) 0.614 against 0.27. (d) About 2,280bp, roughly the difference between a single-B quoted on spread and a bond that trades on price. (e) One answer: "The model learned how much more often defaulters use the phrase than survivors do, not how often users of the phrase default, and only the second number trades."

4. **(Put the Ledger on a clock.)** Two Edge Ledger features describe the same second-lien: a flow signal with $\text{IC}_0 = 0.10$ and a half-life of 3 business days, and a fulcrum view with $\text{IC}_0 = 0.04$ and a half-life of 120 business days *(illustrative)*. (a) Compute each feature's IC at horizons of 1 and 5 days. (b) Find the crossover horizon $h^\star$ at which the two ICs are equal, in closed form and numerically. (c) The RFQ engine's markout horizons are 1, 5 and 20 days. Which feature belongs in $\pi(x)$, which in the portfolio model, and which in both? (d) Mags asked for a column for who lied. Define "lied" as a quantity you can compute from your own RFQ and axe logs, and say what its decay horizon should be.
   *Answer check:* (a) Flow 0.079 and 0.031; fulcrum 0.040 and 0.039. (b) $h^\star = \ln(\text{IC}^{\text{flow}}_0/\text{IC}^{\text{fulcrum}}_0) \,/\, \big[\ln 2\,(1/h^{\text{flow}}_{1/2} - 1/h^{\text{fulcrum}}_{1/2})\big] \approx 4.1$ days. (c) From about day four onward the fulcrum view is the stronger signal, even at the RFQ engine's own five-day horizon, so it belongs in both; the flow signal belongs in $\pi(x)$ only. Your ninety-hour fulcrum analysis beats the tape after four days. Frame that result; it is the only time this chapter flatters you. (d) One answer: the shrunk rate at which a counterparty's shown axes are followed, within $k$ days, by its trades in the opposite direction. Its half-life should be long, because, as Mags would tell you, so is a grudge.

5. **(Detector economics, or how to get restricted by your own compliance department.)** You run the CUSUM (3.5) with $\mu_1 = \sigma_y$ on each of 400 sponsor-backed tranches. (a) Using Lorden's bound, give an upper bound on false alarms per year (252 trading days) across the universe at $h = 4$ and at $h = 8$. (b) With $K = \mu_1^2/(2\sigma_y^2)$, compute the approximate detection delay at each threshold. If a group needs about 30 trading days from first accumulation to signing *(illustrative)*, how much warning does each leave? (c) With `prs_threshold` and $h_0 = 6$, compute the thresholds and delays for $\text{PRS} = 0.9$, $0.5$ and $0.1$. (d) Compliance will investigate every alarm and has the staff for one a week. Find the smallest uniform $h$ that keeps the null bound at or below 52 alarms a year, and explain why the realized false-alarm rate will be lower than the bound.
   *Answer check:* (a) At most $400 \times 252 / e^{4} \approx 1{,}846$ a year at $h = 4$, and about 34 at $h = 8$. Compliance, handed 1,846 alarms a year, will do what compliance does with 1,846 alarms a year, which is restrict you from the sector. (b) $K = 1/2$, so about 8 and 16 days, leaving about 22 and 14 days of warning. (c) $h = 3.80$, $6.00$ and $8.20$, with delays of about 7.6, 12 and 16.4 days: the document work that sets the PRS buys about nine days of warning at the top of the range. (d) $e^{h} \ge 400 \times 252 / 52 \approx 1{,}938$, so $h \ge 7.57$. Lorden's $e^{h}$ is a lower bound on the average run length, so the realized false-alarm rate sits below the bound, and Block 6's null simulation measures by how much.

6. **(ROBO and the lucky client.)** Theo tells ROBO: "Quote tighter for good clients." (a) Describe what ROBO builds, and what happens to the client whose only fill so far marked out at $+300$bp. (b) With a per-fill markout standard deviation of 150bp and a between-client standard deviation of 20bp (Block 4's values), compute the shrinkage factor $k = n/(n + \sigma^2/\tau^2)$ for $n = 1$, 10 and 100, and the shrunk score of the one-fill client. (c) Write the two-sentence spec that fixes it, with units and the IDO requirement. (d) Explain why the client who wins your tightest quote is the one whose score you should trust least.
   *Answer check:* (a) ROBO ranks clients by raw mean markout, so the one-fill client gets the tightest quote on the platform and keeps getting it until its second trade, which arrives promptly, because it is now being shown the best price on the platform. (b) $\sigma^2/\tau^2 = 56.25$, so $k \approx 0.017$, $0.151$ and $0.640$; the one-fill client's shrunk score is about $+5$bp. (c) For example: "Score each counterparty by the empirical-Bayes shrunk mean of its 5-day IDO markouts in bp of price, re-estimating the between-counterparty variance monthly and flooring it at zero. Tighten quotes by at most `c` bp per bp of shrunk score, never on a raw mean, and log every override for a counterparty with fewer than `n_min` fills." (d) Picking the maximum of many noisy estimates selects for noise. It is the winner's curse again, with you as the auctioneer and your own scores as the bidders.

### Deep-Dive Resource Graph

Grouped by type; the section tags say where each item plugs into the chapter. Links are given only where verified; everything else is title and author, so search by title.

- **Podcasts.** Bloomberg *Odd Lots* episodes on liability management, creditor-on-creditor violence and the electronification of bond trading (§3.2, §3.6–3.7; search by topic, episode titles and dates deliberately omitted). Bloomberg Intelligence, *The Credit Edge* (credit fundamentals and default outlooks; §3.4, §3.6). The Octus (formerly Reorg) and 9fin podcasts on LMEs and documentation terms (§3.6–3.7). *Flirting with Models* (Corey Hoffstein), https://www.flirtingwithmodels.com/ , for the systematic-manager habit of asking what decays and why (§3.5); no credit-microstructure episode is claimed here.
- **Practitioner Writing.** Coalition Greenwich, *Bond Dealers Increasingly Automate Trading* (June 11, 2024), https://www.greenwich.com/press-release/bond-dealers-increasingly-automate-trading (§3.2 Trend Watch). MarketAxess, *Automated Trading—Why the sum is greater than the value of individual parts* (September 22, 2025), https://www.marketaxess.com/article/automated-trading-why-the-sum-is-greater-than-the-value-of-individual-parts (§3.2). Man Institute, *The Revolutions in Credit Trading* (June 2023), and Man Group's 2022 survey of quantitative credit managers (shelf: Man_Quantitative_Credit_Alpha_Early_Mover_2022) (§3.5). Moody's, *US Credit Review & Outlook* (July 2025), https://www.moodys.com/web/en/us/insights/resources/us-report-july-2025.pdf ; *Default rates are easing. Credit risk is fragmented and fragile across markets* (April 28, 2026), https://www.moodys.com/web/en/us/insights/credit-risk/private-credit/us-corporate-default-risk-in-2026.html ; and *Lend, extend, and then...* (May 18, 2026), https://www.moodys.com/web/en/us/insights/credit-risk/private-credit/lend-extend-and-then.html (§3.6 Trend Watch). Wachtell Lipton, *Liability Management 2026: For Better or Worse* (February 3, 2026) (§3.4, §3.6). Wellington Management, *The impact of LMEs*, https://www.wellington.com/en-us/institutional/insights/the-impact-of-lmes (§3.6). Mayer Brown, *Serta Simmons Bedding: the Fifth Circuit's uptier decision and the landmark damages ruling on remand* (July 2026), https://www.mayerbrown.com/zh-hans/insights/publications/2026/07/serta-simmons-bedding-the-fifth-circuits-uptier-decision-and-the-landmark-damages-ruling-on-remand (§3.7). Paul Weiss, *Appellate Review of Uptier Transactions: Serta and Mitel Decisions Reversed on Appeal* (January 10, 2025), and Proskauer, *The End of Non-Pro Rata Uptiers?* (January 2, 2025) (§3.7). Matt Levine, *Money Stuff*, columns on Serta and uptiers (§3.7). SEC press releases on Sound Point Capital Management (August 26, 2024), https://www.sec.gov/newsroom/press-releases/2024-106 , and Marathon Asset Management (September 30, 2024), https://www.sec.gov/newsroom/press-releases/2024-158 (§3.6.3). Markout glossaries from Databento, https://databento.com/microstructure/markout , and KX, https://kx.com/glossary/what-is-markout-and-how-is-it-calculated/ (§3.3).
- **Academic Papers.** *Theory (§3.2).* Glosten and Milgrom (1985), *Bid, ask and transaction prices in a specialist market with heterogeneously informed traders*, Journal of Financial Economics 14(1), https://doi.org/10.1016/0304-405X(85)90044-3 . Kyle (1985), *Continuous Auctions and Insider Trading*, Econometrica 53(6), https://doi.org/10.2307/1913210 . Easley and O'Hara (1987), *Price, trade size, and information in securities markets*, Journal of Financial Economics 19(1), https://doi.org/10.1016/0304-405X(87)90029-8 . Milgrom and Weber (1982), *A Theory of Auctions and Competitive Bidding*, Econometrica. *RFQ empirics (§3.2–3.3).* Hendershott and Madhavan (2015), *Click or Call? Auction versus Search in the Over-the-Counter Market*, Journal of Finance 70(1), https://doi.org/10.1111/jofi.12164 . Fermanian, Guéant and Pu (2016), *The Behavior of Dealers and Clients on the European Corporate Bond Market: The Case of Multi-Dealer-to-Client Platforms*, Market Microstructure and Liquidity 2(3n04), https://doi.org/10.1142/S2382626617500046 (preprint https://arxiv.org/abs/1511.07773 ). Kargar, Lester, Plante and Weill (2025), *Sequential Search for Corporate Bonds*, FRB Philadelphia Working Paper 25-08, https://doi.org/10.21799/frbp.wp.2025.08 . Bessembinder, Spatt and Venkataraman (2020), *A Survey of the Microstructure of Fixed-Income Markets*, Journal of Financial and Quantitative Analysis 55(1), https://doi.org/10.1017/S0022109019000231 . O'Hara and Zhou (2021), *The electronic evolution of corporate bond dealers*, Journal of Financial Economics 140(2), https://doi.org/10.1016/j.jfineco.2021.01.001 . Kozora, Mizrach, Peppe, Shachar and Sokobin (2020), *Alternative Trading Systems in the Corporate Bond Market*, FRBNY Staff Report 938, https://www.newyorkfed.org/research/staff_reports/sr938 . Pintér, Wang and Zou (2022), *Size discount and size penalty: trading costs in bond markets*, Bank of England Staff Working Paper 970, https://www.bankofengland.co.uk/working-paper/2022/size-discount-and-size-penalty-trading-costs-in-bond-markets . Marín Martínez, Ardanza-Trevijano and Sabio (2026), *Causal interventions in bond multi-dealer-to-client platforms*, PLOS ONE 21(1). HSBC and IBM researchers (2025), *Enhanced fill probability estimates in institutional algorithmic bond trading using statistical learning algorithms with quantum computers*, https://arxiv.org/abs/2509.17715 . *Quoting engines (§3.8, Chapter 18).* Guéant (2017), *Optimal market making*, Applied Mathematical Finance 24(2), https://doi.org/10.1080/1350486X.2017.1342552 . Bergault and Guéant, *Size matters for OTC market makers*, https://arxiv.org/abs/1907.01225 . Barzykin, Bergault and Guéant, *Algorithmic market making in dealer markets with hedging and market impact*, https://arxiv.org/abs/2106.06974 . Barzykin and Ciceri (2026), *Bond Market Making with a Hit-Ratio Target*, https://arxiv.org/abs/2604.20406 . *Toxicity and informed credit trading (§3.3, §3.6).* Easley, Kiefer, O'Hara and Paperman (1996), *Liquidity, Information, and Infrequently Traded Stocks*, Journal of Finance 51(4), https://doi.org/10.1111/j.1540-6261.1996.tb04074.x . Andersen and Bondarenko (2014), *Reflecting on the VPIN dispute*, Journal of Financial Markets 17, https://doi.org/10.1016/j.finmar.2013.08.002 . Acharya and Johnson (2007), *Insider trading in credit derivatives*, Journal of Financial Economics 84(1), https://doi.org/10.1016/j.jfineco.2006.05.003 . Ivashina and Sun (2011), *Institutional stock trading on loan market information*, Journal of Financial Economics 100(2), https://doi.org/10.1016/j.jfineco.2010.11.004 . Massoud, Nandy, Saunders and Song (2011), *Do hedge funds trade on private information? Evidence from syndicated lending and short-selling*, Journal of Financial Economics 99(3), https://doi.org/10.1016/j.jfineco.2010.10.002 . Han and Zhou (2014), *Informed Bond Trading, Corporate Yield Spreads, and Corporate Default Prediction*, Management Science 60(3), https://doi.org/10.1287/mnsc.2013.1768 . Wei and Zhou (2016), *Informed Trading in Corporate Bonds Prior to Earnings Announcements*, Financial Management 45(3), https://doi.org/10.1111/fima.12123 . Di Maggio, Kermani and Song (2017), *The value of trading relations in turbulent times*, Journal of Financial Economics 124(2), https://doi.org/10.1016/j.jfineco.2017.01.003 . *Statistics (§3.4, §3.6).* Page (1954), *Continuous Inspection Schemes*, Biometrika. Lorden (1971), *Procedures for Reacting to a Change in Distribution*, Annals of Mathematical Statistics. Elkan (2001), *The Foundations of Cost-Sensitive Learning*, IJCAI.
- **Data & Code.** SEC EDGAR, https://www.sec.gov/edgar , and its full-text search endpoint, https://efts.sec.gov/LATEST/search-index (the source of the §3.4 Trend Watch counts; return fields include `file_date`, `items` and `adsh`). Form 8-K and its General Instructions, https://www.sec.gov/files/form8-k.pdf (§3.4). FINRA TRACE, https://www.finra.org/filing-reporting/trace (§3.3 reference mids). CourtListener REST API, https://www.courtlistener.com/help/api/ (Rule 2019 statements and dockets for §3.6–3.7). MarketAxess FY2025 Form 10-K, https://www.sec.gov/Archives/edgar/data/1278021/000119312526067009/mktx-20251231.htm (§3.2 Trend Watch). PJT Partners FY2025 Form 10-K, https://www.sec.gov/Archives/edgar/data/1626115/000119312526076969/pjt-20251231.htm (what the RSSG franchise says about itself). The chapter's reference module, `ch03_rfq_adverse_selection.py` (§3.8), which Chapter 18 extends with the hit-ratio multiplier.

<!-- STATUS: COMPLETE -->
