# Chapter 5: Probability Distributions in Distressed & High-Yield Credit

> *"Any quantitative analysis of credit begins with the skewed, non-normal return distributions typical of both individual credit exposures and portfolios of those exposures."* (Bohn_Stein_Active_Credit_Portfolio_Management p.18)

## Cold Open: The Fourteen-Sigma Tuesday

Theo's first risk report on the new desk is a thing of beauty. It is a single page. It has a heat map. It says that the desk's position in a B3 retail issuer's 8% senior notes, bought at 92, has an annualized volatility of 4.1%, computed from sixty days of TRACE marks, and that the probability of losing fifteen points over the next year is, under the normal distribution, about one in twenty-nine thousand.

"So it's safe," Theo says, in the tone of a man who has spent six years reading credit agreements and three weeks being told that is not a personality.

Mags does not look up from her screen. "It loses fifty-two points, once. It goes from 92 to 40 in an afternoon, after a lender call you weren't on. Your model calls that a fourteen-sigma event. We had three of those in the book last year."

"Let's just assume Gaussian," Kaz says, from behind two monitors and a whiteboard covered in Itô integrals. "For tractability. We can add jumps later."

Ines pulls a chair over and turns Theo's heat map face down, the way you turn over a card you have already read. "What's the pot, Theo? What are the odds? And who at this table knows more than you?" She taps the number 4.1%. "This isn't the hand. This is how much the chips wobble while nobody's betting. The hand is whether the dealer pays you par plus coupon, or 40 cents, or, if the sponsor has found a friend, 2.4 cents."

Theo opens his laptop and plugs in the USB stick with his old thirteen-week cash flow model, for emotional support. The model says the issuer has eleven weeks of liquidity. "Eleven weeks," he says. "That's not a volatility. That's a probability of not making it."

"Now you're pricing," Ines says. "Write it down so ROBO can't get it wrong."

ROBO, consulted, offers to minimize the portfolio's kurtosis. It proposes to sell everything and buy three-month bills, whose kurtosis is indeed zero. So is their credit spread. ROBO considers this a feature.

Theo, who has been told for three weeks that he is not a personality, decides to be one anyway. "Name one," he says. "One of the three."

"Ours are confidential, and compliance has feelings," Mags says. "I'll give you a public one. Better, really. Everybody has the filings, so nobody can tell you you're remembering it wrong." She swivels a monitor toward the group, the way she has been swivelling monitors toward junior people since monitors were beige. On it is a Bloomberg story from 18 November 2022 about Carvana, the online used-car retailer. Its bonds were quoted between 37 and 48 cents on the dollar, in what the reporters called a "collapsing bond stack." Fitch expected a default the following year; S&P said the liquidity would last through the end of 2023 *(Bloomberg, 18 Nov 2022, as republished by American Banker)*. Two rating agencies, one company, and a year's disagreement about the date of death.

"Don't read the story. Read the stack," Mags says. The unsecured notes came in five series, \$5,725mm in all: \$500mm of 5.625% notes due 2025, \$600mm of 5.500% due 2027, \$600mm of 5.875% due 2028, \$750mm of 4.875% due 2029, and \$3,275mm of 10.250% due 2030 *(Carvana 10-Q for the quarter ended 30 Sep 2023, debt note)*. "A three-year bond and an eight-year bond, coupons almost five points apart, and the market has them within a few points of each other. What does that tell you?"

Theo knows this one. It is the first thing a restructuring banker learns to see on a price sheet, before he learns to see anything else. "That nobody's pricing coupons any more. They're pricing the claim. In a bankruptcy the 2025s and the 2030s are both unsecured claims against the same box, and they get the same recovery per dollar of claim, give or take accrued. Maturity stops mattering when nobody thinks the maturity will be reached."

"So what is the bond?"

"A recovery with a coupon attached that you probably won't get."

"And a year earlier?" Mags scrolls. At 31 December 2021 the fair value of Carvana's notes was 99.5% of their carrying amount. At 31 December 2022, with the stack now more than twice as large, it was 44.8% *(Carvana 10-K, Level 2 fair-value disclosures; ratios computed from reported fair value and carrying amount)*. Over the same stretch the stock went from above \$370 at its August 2021 peak to a close under \$4 in the last week of December 2022 *(approx.; vendor daily bars restated to as-traded prices)*. "If you'd run your sixty days of marks in the autumn of 2021, you'd have got a number a lot like your 4.1%. Then you'd have got this."

Theo goes quiet in a way the desk will learn to recognize. He knows the name. When Carvana finally restructured its notes in the summer of 2023, PJT Partners was financial advisor to the noteholder group, according to the company's own 19 July 2023 release *(Carvana 8-K, Exhibit 99.1, 19 Jul 2023)*. He was not staffed on it, but he remembers the summer that deal ate, the way you remember a neighbour's renovation: from the noise, and the people who stopped coming to lunch.

Kaz, meanwhile, has done what Kaz does with any new object, which is compute its standard deviation. "Bond at 40," they announce, "moving two or three points a day. Call it six percent of price, daily. Annualized, that's a hundred and something. A hundred and four, with these numbers *(illustrative)*." They look pleased, and then less pleased. "Which means that under a normal distribution, a one-sigma bad year takes it from 40 to minus 1.6 cents."

"I have owned bonds like that," Mags says. "Not literally."

"About a one-in-six chance of a negative price," Kaz goes on, because it is true and Kaz finds it physically difficult to leave a true thing unsaid. "I'd like it minuted that this is the model's problem and not mine."

Ines has been waiting with the patience of someone who has watched a lot of people bet into a flush. "Same question as before. What's the pot?" Nobody answers fast enough, so she does. "From 92, Theo's bond had a small pot on top, a few points of carry and roll-down, and a big pot underneath, fifty-odd points down to a recovery. From 40, this one has the same two pots, and they've swapped places. Down is to whatever an unsecured claim on a used-car retailer is worth, and that floor isn't zero: there are cars, there's an auction business, there's a finance platform. Up is to par. Sixty points, if it lives." She holds her two hands at different heights. "Kaz's hundred and four percent is the noise the coin makes while it spins. It isn't the size of either pot."

"So which way is it skewed?" Theo asks.

"Ask me again in a section," Kaz says, and writes on the whiteboard, under the Itô integrals: *skew sign flips when?*

Mags scrolls forward to 22 March 2023. That day Carvana launched private exchange offers for its unsecured notes. It would issue up to \$1.0bn of new 9.0%/12.0% cash/PIK toggle senior secured second-lien notes due 2028. Total consideration per \$1,000 of old notes ran from \$632.50 for the 4.875% 2029s to \$808.75 for the 5.625% 2025s, each including a \$20 early premium. An acceptance priority served the shortest maturities first, and the whole thing needed at least \$500mm of participation to happen *(Carvana 8-K and press release, 22 Mar 2023)*. The release called the consideration "at a premium to current trading prices." The new notes would take a second lien on collateral where Ally, the floor-plan lender, already held the first.

"Look at what they paid for which bond," Theo says. "The market priced every series as the same claim. The company didn't. It offered the most for the 2025s, because that's the wall it has to climb first, and \$793.75 for the 10.25% 2030s, because that's the coupon it most wants to stop paying. The market sees a recovery. The issuer sees a cash-flow problem with five different interest rates."

There was a step before the offer, and Mags makes them read it twice. Before launch, Carvana designated ADESA US Auction, LLC, its wholesale auction business, an unrestricted subsidiary under the existing indentures. That released the ADESA subsidiaries from their guarantees of the old notes, and ADESA would not guarantee the new ones either. The company also planned to put its finance-platform intellectual property into a new finance subsidiary. The release said all of this was "permitted under its existing debt arrangements."

"There it is," Theo says, and actually stands up. "They moved the furniture out before they asked the tenants to leave. Designate the sub unrestricted, the guarantee falls away, and the unsecured holders now have a claim on a smaller box. *Then* you offer them a second lien on part of what's left at sixty-five cents and call it a premium. It's the unrestricted-subsidiary move from the loan market, done to a bond stack."

"Unrestricted," Kaz says slowly, testing it. "As in, no parental supervision?"

"As in, the covenants don't follow it home," Theo says. "Close enough, honestly."

"And what did the holders do?" Mags asks, in the voice of someone who already knows.

They waited. On 19 April the offer was extended to 3 May and the consideration for the 2025s raised to \$858.75 in total. On 3 May it was extended again. On 17 May it was pushed to 1 June, with the withdrawal deadline moved to 24 May. On 2 June 2023 Carvana announced that the offers had expired and been terminated because the \$500mm minimum had not been met, and every tendered note went back to its owner *(Carvana 8-Ks, 19 Apr, 17 May and 1 Jun 2023)*. A billion dollars of secured paper, priced by the company's own description above the market, and the holders would not hand over even half of it.

"Back in my day," Mags says, "you'd hear about that from a man at a bar who heard it from his brother-in-law, and the bar would be in Hoboken. Now it's on EDGAR by a quarter past four and the brother-in-law is an ad hoc group with a law firm." She shrugs. "It's better. I'm not saying it isn't better."

"Somebody was organized," Ines says. "A stack that size, three extensions and a sweetener, and the minimum never fills? That isn't apathy. That's a table where the other players already talked in the car park." She looks at Theo. "Who at this table knows more than you?"

"The holders who already said no together," Theo says. "Whoever they are."

"Good. Now sit in the chair."

Here is the hand, then, dated Friday, 2 June 2023. You own Carvana's 5.875% notes due 2028. In March the company offered you \$646.25 per \$1,000 of them in second-lien paper and called that a premium to where they traded, and at the end of March the whole note stack was carried at 53.8% of book *(Carvana 10-Q, quarter ended 31 Mar 2023; ratio computed)*. So call your bond somewhere in the mid-50s *(illustrative)*. The stock had roughly tripled from its January low, to about \$13 at the end of May *(approx.; vendor daily bars)*, which is either the equity market knowing something or the equity market being the equity market. The exchange has just failed. The company has the same cash it had this morning, the same stack, the same unrestricted ADESA, and a 10-K full of risk factors. The holders still have each other.

You have three choices, and each one is a claim about a distribution. You can sell into whatever bid shows up on a Friday afternoon after a failed exchange, which says the left pot is larger than you can stand. You can hold and wait to tender into the next, presumably better, offer, which says the holders' refusal has bargaining value and you are part of it. Or you can buy more, which says the right pot, the world where Carvana survives and the bond climbs toward par, is underpriced at 55.

Kaz is already writing. "One-year return. Two worlds. It survives and rolls toward par, or it defaults to a recovery. And now a third thing, the exchange, which is neither."

"Four things," Mags says. "Survive. Default. Exchange. And exchange-then-default-anyway. They come in that order more often than you'd like."

"Vote," Ines says. "Go round the table."

Theo goes first, because he is sure. "Sell. I know there was a deal in July, I'm telling you what I'd have done on the second of June. A failed exchange is a bankruptcy with extra steps. The company asked nicely, the holders said no, and the next ask won't be nice. I've watched this from the company's side of the table: when the out-of-court deal dies, you start drafting first-day declarations." He says it with the confidence of a man who has drafted several.

"You've watched it from the company's side," Mags says. "The company's side always thinks the next step is court, because that's where the company's advisers get paid. The holders' side thinks the next step is a better offer. I'd hold. I'm not buying more of a used-car dealer with an unrestricted subsidiary, but I'm not selling to whoever's bidding at four o'clock on the Friday they think I'm scared."

Kaz is honest about it. "My vol estimate says the bond is very risky. It doesn't say in which direction. So I'd reduce, and I know that isn't an answer."

"It isn't," Ines agrees. "It's a confession." She turns her own card over last. "I want to know who's selling to me before I decide whether I'm buying. If the seller is a fund that can't hold anything below sixty, that's a forced hand and the price is a discount for their rules, not a forecast. If the seller is someone who was in the group, that's a different hand altogether." She lets that sit. "Notice that none of you has told me the odds. Theo's thinks the coin is weighted toward default. Mags thinks the pots are lopsided toward the holders. Kaz thinks the coin is loud. Those are three different distributions and you've each priced one without writing it down."

Theo, it will turn out, is wrong, and he will be wrong in the way most restructuring bankers are wrong the first time they sit on the buy side: he priced the probability of the bad state from the side of the table where the bad state is the plan. The holders' refusal was not the end of the negotiation. It was the negotiation. Mags knows exactly how the rest of 2023 went and declines to say, which is the most teacherly thing she has done all week. On the afternoon of 2 June 2023, the market did not know either.

Theo looks at his own report, with its heat map and its 4.1% and its one in twenty-nine thousand, and then at the Carvana stack on Mags's screen, and realizes that the two documents disagree about what a bond *is*. His says a bond is a wobble. Hers says a bond is a coin, a pot, and a menu of ways for the coin to land, and the wobble is only what you hear while it spins.

"So what do I do on the second of June?" he asks.

"First you tell me the distribution," Ines says. "Then you tell me which way it leans. Then we can talk about what you do."

**The question this chapter answers:** *what is the right shape for a high-yield or distressed credit return, and how do you specify it precisely enough that a literal-minded coding agent cannot build the wrong one?*

By the end of this chapter, the second of June will have an answer, and so will the Tuesday report. Along the way Theo will write a high-yield bond's one-year return as a survive-or-jump mixture and compute its first four moments in closed form, which is where the slogan "skew is minus one over root PD" comes from. He will learn, the hard way, to keep the price, the spread and the return in three separate ledgers, because they have three different shapes. Kaz will sort the jump and Lévy machinery that earns its keep on a desk from the machinery that is decoration. Mags will insist that recovery is itself a random variable, a Beta conditioned on collateral, seniority, debt cushion and, since 2020, which side of the cooperation agreement you signed. Carvana's failed exchange will become a third component of the mixture, the distressed exchange, with its own re-default hazard. And the extreme-value tools everyone reaches for when a tail frightens them will be put where they belong, which is on books, indices and spread changes, and not on a single bond.

## 5.1 One Bond, Two Worlds: The Survive-or-Jump Mixture

### 5.1.1 Desk framing: two hands dealt from one deck

Ines's framing is the right one, and it is worth saying slowly. Over a one-year horizon, a high-yield bond does one of two different things. In the world where the issuer survives, the bond collects its coupon, rolls toward par, and its price wobbles as spreads move: a small, roughly symmetric, roughly Gaussian distribution of returns that sits a few points either side of the carry. In the world where the issuer defaults (or, in the 2020s, "executes a liability management transaction that the rating agencies classify as a distressed exchange"), the bond jumps to a recovery value, and the size of the jump has nothing to do with the wobble.

Theo's 4.1% is a perfectly good estimate of the first world's wobble. It is not an estimate of anything in the second world, because sixty days of TRACE marks on a bond that has not defaulted contain zero observations of a default. This is the most important sentence in the chapter, so here it is again in poker terms: *the volatility you measure while nobody is betting tells you nothing about the size of the pot.*

The RSSG reader already knows this. You have built recovery waterfalls for years. What you have not done is put both worlds into one random variable, with probabilities attached, and computed what that does to the mean, the variance, the skew, and the tail. That is what a desk risk system needs, and it is what ROBO will get wrong unless you write it down.

> **Math, Gently.** *What a distribution is, and what a mixture is.* Picture a deck of 100 cards. Ninety-six of them say "+7": the bond survives, you collect the coupon and a little roll, and you are up seven points. Four of them say "−57": the issuer defaults and the bond falls to its recovery. You draw one card a year. The *distribution* of your return is the whole deck: every card it could be, and how many copies of each there are. It is not the average card. The average here is $0.96 \times 7 + 0.04 \times (-57) = 4.44$, and no card in the deck says 4.44. A risk report that shows only the average, or only how much the +7 cards jiggle between +5 and +9, is describing the deck by its most common card. A *mixture* is what you get when the deck is really two decks shuffled together, one for each world, each with its own spread of values, and a coin that decides which deck you draw from. That coin is the default indicator $D$ of §5.1.2, and the coin's bias is the default probability $q$. The rest of the chapter is a tour of the shapes that turn up on a desk, each introduced in its own box when it first appears. The *normal* is the bell curve for things that wobble symmetrically, like a survival-world return over a quiet month. The *lognormal* (§5.2.3) is the normal moved into an exponent, for quantities that cannot go negative and grow in percentages, like spreads. The *Poisson* (§5.3.2) counts rare events in a window: defaults in a portfolio, jumps in a year. The *exponential* (§5.3.3) measures the waiting time until the next one. The *Beta* (§5.5.2) lives on a shelf between zero and one and is the natural home of a recovery rate. And the *fat-tailed* family (§5.7.2) is for losses whose extremes do not die off fast enough for a bell curve to describe them. The full version of the mixture is §5.1.2.

> **Math, Gently.** *Two kinds of probability: $\mathbb{P}$ and $\mathbb{Q}$.* A bookmaker's odds are not the true odds. If a horse truly wins one race in four, fair odds are three to one against, and the bookmaker quotes something shorter, say five to two, because the bookmaker wants paying for the risk of being wrong and for tying up money. Credit has the same two numbers, and the next section names both in its second sentence. $\mathbb{P}$, the *physical* measure, is the true-odds world: the probability that the issuer actually defaults, as estimated from history, fundamentals, or Theo's 13-week model. $\mathbb{Q}$, the *risk-neutral* measure, is the bookmaker's world: the probability that, plugged into a plain expected-value calculation, reproduces the price the market is actually charging. Tiny example: your best estimate is that the B3 issuer defaults with probability $q = 4\%$ over the year, but its spread, read through a crude "spread equals default probability times loss" rule, is charging for something like 5.5%. The 1.5 points between the two is not an error by either party. It is the price of fear plus the price of illiquidity, paid to whoever is willing to hold the risk. Risk management lives in $\mathbb{P}$, pricing lives in $\mathbb{Q}$, and mixing them up is how a desk ends up confidently wrong in both. The full version, with the change of measure written out, is in Chapter 6 and §6-B.6.

### 5.1.2 The mixture and its moments

Fix a horizon of $h$ years and measure everything per unit of par. Let $P_0$ be the full price today. Let $D \sim \text{Bernoulli}(q)$ be the default indicator over the horizon, where

$$
q = 1 - S^{\mathbb{P}}(h)
$$

is the **physical** default probability. (We are building a risk distribution, so $\mathbb{P}$; Chapter 6 does pricing under $\mathbb{Q}$, and §5.5.6 explains why mixing them is the most common expensive mistake in this chapter.)

In the survival world, the rates-hedged excess return is

$$
X = s\,h + \text{roll} - D^{\text{spr}}\,\Delta s + \tfrac{1}{2}C^{\text{spr}}(\Delta s)^2,
$$

where $s$ is the spread (decimal), $D^{\text{spr}}$ the spread duration, $C^{\text{spr}}$ the spread convexity, and $\Delta s$ the spread change over the horizon. Ben Dor's Duration Times Spread result says spread changes scale with the spread level, so a natural specification is $\sigma_{\Delta s} = \kappa\,s\,\sqrt{h}$ with $\kappa$ the annualized volatility of *relative* spread changes (see Chapter 8 for the DTS machinery). Call the survival leg's mean, variance, third central moment, and fourth central moment $\mu_X$, $\sigma_X^2$, $\mu_{3,X}$, $\mu_{4,X}$.

In the default world, the bond is worth its recovery $R$ (fraction of par), so the return is

$$
Y = \frac{R}{P_0} - 1, \qquad R \sim \text{Beta}(a, b) \text{ (refined in §5.5)},
$$

with moments $\mu_Y$, $\sigma_Y^2$, $\mu_{3,Y}$, $\mu_{4,Y}$. Note the denominator. A bond bought at 60 that recovers 40 lost a third of its value, not 60%. ROBO, asked for "the loss given default," will return $1 - R$ every time unless told otherwise, which is why the spec in §5.9 names the price basis explicitly.

The horizon return is the mixture

$$
R_h = (1 - D)\,X + D\,Y.
$$

> **Math, Gently.** *The law of total variance: wobble plus coin.* How spread out is a mixture? There are two sources of spread, and they add. The first is the wobble *inside* each world: on the survival side the bond lands somewhere between +3 and +11, on the default side somewhere between a bad and a terrible recovery. The second is the coin *between* the worlds: even if neither world wobbled at all, you would still be uncertain which of two very different numbers you were going to get. The variance of a coin that lands on one of two values a distance $J$ apart, with probability $q$ on one side, is $q(1-q)J^2$. For Theo's bond the centers of the two worlds are about 64 points apart ($J = 0.64$ in return space) and $q = 0.04$, so the coin alone contributes $0.04 \times 0.96 \times 0.64^2 = 0.0157$ of variance. Take the square root and the coin, all by itself, has a standard deviation of 12.5%, three times Theo's 4.1%, and that is before either world has wobbled at all. Sixty days of marks on a surviving bond can only ever see the wobble. The full version is the variance formula just below.

Define the **jump size** $J \equiv \mu_X - \mu_Y$, the distance between the centers of the two worlds. Conditioning on $D$ and using the law of total expectation and total variance:

$$
\mathbb{E}[R_h] = (1-q)\mu_X + q\mu_Y = \mu_X - qJ,
$$

$$
\operatorname{Var}[R_h] = \underbrace{(1-q)\sigma_X^2 + q\sigma_Y^2}_{\text{within-world}} + \underbrace{q(1-q)J^2}_{\text{between-world}}.
$$

The second term is the one Theo's report missed. It is the variance of a coin flip whose two faces are $J$ apart. For a high-yield bond it is usually the largest term.

The third and fourth central moments follow from the same conditioning, by centering each world at the mixture mean and expanding; the algebra is moved, unchanged, to *The Full Derivation: third and fourth central moments of the mixture* at the end of §5.1.4, and its one load-bearing term, $-q(1-q)(1-2q)J^3$, is the whole of §5.1.3.

Skewness is $\mu_3/\operatorname{Var}^{3/2}$ and excess kurtosis is $\mu_4/\operatorname{Var}^2 - 3$. Two checks you should always run on formulas like these, and should make ROBO run too: at $q = 0$ they collapse to the survival world's moments, and at $q = 1$ to the default world's. Both hold here by inspection.

### 5.1.3 Skew is minus one over root PD

> **Math, Gently.** *Skewness and kurtosis are shape numbers.* The mean says where a distribution sits and the standard deviation says how wide it is. Skewness and kurtosis say what it *looks like*, and both are scaled so that they do not care about units or about the size of the bet. Think of a seesaw balanced at the mean. Ninety-six children sit just to the right of the pivot, close in; one child sits far out on the left. The seesaw balances, because that is what the mean is, but it is lopsided in a way the balance point does not show. Skewness measures that lopsidedness: negative when the long arm is on the loss side, as it is for a bond, and zero for a symmetric bell. Kurtosis measures how much of the variance comes from that one far-out child rather than the crowd near the pivot; a normal distribution scores 3, so desks quote *excess* kurtosis, kurtosis minus 3, and a normal's excess is zero. The tiny numbers for this section: a bond with a 4% default probability has a skew of about $-4.7$ and an excess kurtosis of about 20. Make the bond much safer, a 0.05% default probability, and the skew goes to about $-45$: the child is now astonishingly far out on a very long plank, and almost never gets on. The full version is the pair of formulas just below.

Now strip the mixture to its skeleton. Let both worlds be points: $\sigma_X = \sigma_Y = 0$ and no higher moments. Then $R_h = \mu_X - J\,D$, an affine function of a Bernoulli, and the moment formulas reduce to

$$
\text{skew}(R_h) = -\frac{1 - 2q}{\sqrt{q(1-q)}} \approx -\frac{1}{\sqrt{q}}, \qquad \text{exkurt}(R_h) = \frac{1 - 6q(1-q)}{q(1-q)} \approx \frac{1}{q}.
$$

At a 1% default probability the skew is about $-9.8$ and the excess kurtosis about $95$. At 4% they are $-4.7$ and $20$. Notice what is *not* in these formulas: $J$. The size of the jump sets the variance, but the shape of the distribution (its skew and kurtosis) is pinned by the default probability alone. Safer bonds are *more* skewed, not less. An A-rated bond with a 0.05% annual default probability has a skew of roughly $-45$. It almost never surprises you, and when it does, it surprises you completely.

This is why Kaz's "let's just assume Gaussian" is not a simplification but a different asset. A Gaussian has a skew of zero and a kurtosis of three, at every default probability. It is a fine description of the survival world. It is a description of the wrong bond.

> **Desk Myth vs. Desk Reality.** *Myth:* "Investment-grade bonds have well-behaved, nearly normal returns; it's high yield that is fat-tailed." *Reality:* Per bond, the opposite. Skew scales like $-1/\sqrt{q}$, so the lower the default probability, the more extreme the shape. IG *portfolios* look well-behaved because they hold hundreds of names with low default correlation and the $1/\sqrt{N}$ of diversification goes to work on the jump term (§5.7.4). The bond did not get more normal. The book got bigger.

**When the skeleton is the right tool, and when it breaks.** The formula $-(1-2q)/\sqrt{q(1-q)}$ is a ranking device and a smoke alarm. It is the right tool for comparing shapes across ratings, because it tells you, without any recovery assumption, that a BB bond is more lopsided than a CCC one, and it is the right tool for sanity-checking a risk system: if the system reports a skew of $-0.3$ on a single B3 bond, it has measured the wobble and not the bond, and somebody should find out why before the next Tuesday. It breaks in two places. The first is when the survival world is not a point but a wide or lopsided lump of its own. A callable bond trading near its call price has its upside capped and its survival leg skewed to the left by itself (§5.2.2), and a bond with a long duration in a volatile spread regime has a survival leg wide enough that the $3q(1-q)J(\sigma_X^2 - \sigma_Y^2)$ cross term in the full third moment starts to matter. The second is when $q$ approaches one half. There the skeleton's skew passes through zero, and the formula says nothing useful about the shape; what decides the lean is how far the price sits from the expected recovery, which is §5.2.4's sign-flip and the Carvana decision of the cold open. A seasoned risk manager, handed a skew number on a distressed name, checks one thing before quoting it: the price relative to expected recovery. If the bond trades within a few points of what the recovery model says it is worth in default, most of the "skew" is a statement about the right tail, not the left.

### 5.1.4 The fourteen-sigma Tuesday, priced

Return to Theo's bond with illustrative inputs. Price $P_0 = 0.92$; survival leg Gaussian with $\mu_X = 7\%$ (coupon carry plus pull to par, net of expected spread drift) and $\sigma_X = 4.1\%$, Theo's number, now correctly labeled as the *survival-world* volatility; physical one-year default probability $q = 4\%$; recovery Beta with mean 40% and standard deviation 27.5% (the Moody's senior unsecured moments reproduced on Schmid p.103, which we use again in §5.5). All numbers are *illustrative*; the moments are the author's arithmetic from the formulas above, and the Monte Carlo in §5.9 reproduces them.

> **Math, Gently.** *VaR and expected shortfall.* Value-at-Risk answers a narrow question: "on a bad day, but not the worst, how much do I lose?" The 95% VaR is the loss you exceed only one year in twenty; you find it by lining up every possible outcome from worst to best and reading off the one at the 5% mark. Expected shortfall asks the follow-up nobody wants to ask: "and *when* I am past that mark, how bad is it on average?" It averages everything beyond the line instead of standing on it. For a bell curve the two tell the same story, a little apart. For a mixture they can tell completely different stories. In Theo's bond the default world holds only 4% of the outcomes, so the 5% mark falls *inside* the survival world, among the ordinary wobbles, and the 95% VaR is a loss of 2.2%. Average over the worst 1% instead and you are averaging defaults: the 99% expected shortfall is a loss of 92%. VaR here is a speedometer that reads perfectly below the speed limit and has no numbers above it. Expected shortfall is the passenger who keeps asking what happens if the brakes fail. The full version is the table below, and the quantile algebra for tails is in §5.7.2.

| Quantity | Theo's Gaussian | Survive-or-jump mixture |
| :--- | ---: | ---: |
| Mean one-year return | 7.0% | 4.5% |
| Volatility | 4.1% | 14.4% |
| Skewness | 0 | $-5.1$ |
| Excess kurtosis | 0 | 28 |
| $\Pr(\text{lose} > 15 \text{ points})$ | 1 in 29,000 | 1 in 29 |
| 95% one-year VaR (return) | $+0.3\%$ (a gain) | $-2.2\%$ |
| 99% one-year VaR (return) | $-2.5\%$ | $-83\%$ |
| 99% expected shortfall | $-3.9\%$ | $-92\%$ |
| $\Pr(\text{return} > \text{mean})$ | 50% | 70% |

Four rows deserve a sentence each.

The **volatility** more than triples, and about four-fifths of the increase comes from the between-world term $q(1-q)J^2$, which is 75% of the total variance. The survival leg's own variance, the only thing Theo's report measured, contributes about 8%.

The **probability of losing fifteen points** is off by a factor of about a thousand. Mags's "three of those last year" in a book of a hundred such names is not bad luck; it is the mixture's expected count.

The **95% VaR is blind.** With $q = 4\% < 5\%$, the 5th percentile of the mixture sits inside the survival world, so VaR at 95% reports a loss of 2.2% on a bond with a 4% chance of losing 57%. Move to 99% and VaR falls off a cliff to $-83\%$. A VaR model on high-yield credit is a speedometer that works perfectly below the speed limit. This is why every serious credit risk system in this book reports expected shortfall and jump-to-default (JTD) exposure alongside VaR.

The **last row** is Bohn and Stein's unintuitive result in miniature: most of the time, you beat the average.

> **[SOURCE EXTRACTION]** *Bohn_Stein_Active_Credit_Portfolio_Management p.513:* "There is always a large probability of relatively small losses, and a small probability of rather large losses. This skewness leads to an unintuitive result: A very high percentage of the time (say 80 percent), the actual losses will be less than the average loss (expected loss)."
>
> **Annotation.** Bohn and Stein are writing about portfolio loss distributions at a bank, but the statement is exact for a single bond too, and it is the source of a specific behavioral failure on systematic desks. A strategy that harvests a credit risk premium will, most months, beat its expected return, and the people running it will conclude that they are skilled. Our worked bond beats its mean 70% of the time. If you evaluate a credit PM or a credit signal on hit rate, you are rewarding the person who sold the most jump risk. The desk fix is to evaluate on IDO (carry, rates, and factor beta stripped; Chapter 8) *and* on a JTD-adjusted denominator. The modern departure from the bank-portfolio framing: on a trading desk, the "small probability of rather large losses" is no longer a single default event but a menu of events (hard default, distressed exchange, non-pro-rata uptier), each with its own recovery distribution. §5.6 turns the Bernoulli into a categorical variable.

> **View From Another Seat.** *A multi-strategy relative-value pod.* Put the same bond in a pod at a multi-strategy platform and the 70% in the last row of the table stops being a statistical curiosity and becomes a career incentive. A pod is typically scored monthly: on P&L against a drawdown limit, on hit rate, on a Sharpe ratio computed from monthly returns, and the drawdown limit is usually tight enough that a bad quarter ends the pod. A strategy that is long carry in B3 paper beats its mean seven months in ten and posts a beautiful monthly Sharpe for as long as no name in it defaults. The portfolio manager who sells the most jump risk looks like the most skilled one in the building, right up to the month that ends the comparison. Pods that survive the incentive tend to do two things the rest of this chapter recommends anyway: they hedge jump-to-default explicitly, usually with single-name or index CDS, so that the strategy's monthly Sharpe is measured on a book whose default world is small; and the platform's risk team sizes the pod on stressed expected shortfall rather than volatility, which is the platform's way of saying it has read Bohn and Stein too. The seat sees the same mixture as everyone else. What it changes is who gets paid while the coin is still in the air.

> **Poker Table.** Ines plays it as a hand. "You're in a pot with ninety-six percent equity. The board pays you seven. The other four percent of the time it costs you fifty-seven. Your expected value is plus four and a half, and you'll win most nights, and you will feel like a genius right up until the river. The pros don't ask whether they're winning. They ask whether they're getting paid enough for the river." The required spread is a pot-odds calculation: under $\mathbb{P}$, the expected cost of the river is $qJ$ in return space, about 2.5 points a year here, and the rest of the 5.5% spread is the risk premium plus liquidity premium plus the price of being wrong about $q$. Hand history: replay the trade through markouts against the five-day CDS move, and you will see that the bonds clients were keenest to sell you were the ones whose $q$ had just gone up.

#### The Full Derivation: third and fourth central moments of the mixture

For the higher moments, center each world at the mixture mean. The survival world's center sits $+qJ$ above the mixture mean and the default world's sits $-(1-q)J$ below it. Expanding $(X - \mathbb{E}R_h)^3$ and $(Y - \mathbb{E}R_h)^3$ around those offsets and collecting terms gives the third central moment

$$
\mu_3 = -q(1-q)(1-2q)J^3 + 3q(1-q)J\left(\sigma_X^2 - \sigma_Y^2\right) + (1-q)\mu_{3,X} + q\,\mu_{3,Y},
$$

and the fourth central moment

$$
\mu_4 = (1-q)\left[q^4J^4 + 6q^2J^2\sigma_X^2 + 4qJ\mu_{3,X} + \mu_{4,X}\right] + q\left[(1-q)^4J^4 + 6(1-q)^2J^2\sigma_Y^2 - 4(1-q)J\mu_{3,Y} + \mu_{4,Y}\right].
$$

These are the formulas behind the skewness and kurtosis in the §5.1.4 table, and the ones the §5.9 lab checks against Monte Carlo. Run the same two checks on them as on the mean and variance: at $q = 0$ every term involving the default world vanishes and $\mu_3 = \mu_{3,X}$, $\mu_4 = \mu_{4,X}$; at $q = 1$ the survival terms vanish and the default world's moments are all that is left.

### 5.1.5 The 13-week model, reborn as a hazard rate

Theo's USB stick deserves a formal promotion, because it is a physical-measure survival model in disguise. Thirteen weekly ending cash balances $C_1, \dots, C_{13}$ under a base case, plus a downside case, define a first-passage time

$$
\hat{\tau} = \min\{w : C_w < C_{\min}\},
$$

where $C_{\min}$ is the minimum liquidity covenant or the operating cash floor. If you run the cash model under a distribution of revenue and collections shocks instead of a single base case (Theo's downside case is one sample from that distribution), the fraction of paths with $\hat{\tau} \le w$ is an empirical estimate of $1 - S^{\mathbb{P}}(w/52)$, and the conditional probabilities of hitting the floor in week $w$ given survival to $w-1$ are a discrete-time hazard curve. The 13-week model is a hazard rate with a spreadsheet problem. Chapter 6 turns that curve into an intensity $\lambda_t$; here it gives us $q$ for the mixture.

> **Math, Gently.** *Survival curves and hazard rates.* A survival curve answers "what is the chance the company is still standing at week $w$?" It starts at 100% today and can only go down. A hazard rate answers a more useful question, the one a doctor asks: "given that the patient made it to Monday, what is the chance they do not make it to Friday?" It is the chance of dying *this* week, conditional on having survived every week before. The two are the same information in two forms: multiply together the weekly chances of surviving, one minus each week's hazard, and you have the survival curve. A tiny example, the one Exercise 5 uses: suppose Theo's shocked cash model says the weekly hazard is 0.2% for the first eight weeks, while the revolver still has room, and 1.5% for the last five, once it does not. The chance of surviving all thirteen weeks is $0.998^8 \times 0.985^5 \approx 0.984 \times 0.927 \approx 0.9125$, so the 13-week default probability is about 8.75%. Notice what the hazard view gives you that the single number does not: *when* the danger arrives. A desk can hedge a hazard that jumps in week nine very differently from one that is flat. In continuous time the weekly hazard becomes an intensity $\lambda_t$ and the product becomes $S(t) = \exp(-\int_0^t \lambda_u\,du)$; the full version is in Chapter 6.

Theo, pleased with his promotion, runs the downside case on his own model and gets a $q$ he likes. Then, out of habit, he runs the lender case too, the RSSG ritual of taking management's base case and haircutting it until a creditor would believe it, because the cash model is a $\mathbb{P}$ object built by management and management's base case has a well-documented optimism bias. The lender case is crude, but it is a useful haircut, and his $q$ goes up. He is about to type it into the mixture when Mags leans over. "Eleven weeks of liquidity," she says, "sponsor-backed, and you told me this morning the credit agreement is permissive. When was the last time a company like that filed in week eleven? It doesn't run out of money. It runs out of patience, in about week six, and does an LMT." She is right, and it is a structural point rather than a quibble: a liquidity runway is not the only exit, and a sponsor-backed borrower with eleven weeks of liquidity and a permissive credit agreement is at least as likely to execute a liability management transaction as to file. A single first-passage time cannot represent two different ways of leaving. The survival model needs a competing-risks structure, with one clock for the filing and another for the exchange, and that is §5.6.

### Deep-Dive Resource Graph

- **Podcasts:** Bloomberg *Odd Lots* episodes on high-yield defaults and liability management (2023–2025; titles to be confirmed before linking).
- **Practitioner Writing:** Man Group, *Quantitative Credit Alpha: An Early Mover Advantage* (2022), on the asymmetric nature of jump risk in credit (shelf: Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.16, p.26).
- **Academic Papers:** Merton (1974), *On the Pricing of Corporate Debt: The Risk Structure of Interest Rates*, Journal of Finance; Ben Dor, Dynkin, Hyman, Houweling, van Leeuwen, Penninga (2007), *DTS (Duration Times Spread)*, Journal of Portfolio Management; Giesecke, Longstaff, Schaefer, Strebulaev (2011), *Corporate Bond Default Risk: A 150-Year Perspective*, Journal of Financial Economics.
- **Data & Code:** FRED, ICE BofA US High Yield OAS (series BAMLH0A0HYM2), https://fred.stlouisfed.org/series/BAMLH0A0HYM2 ; the `mixture_moments` reference implementation in §5.9.

## 5.2 Price, Spread, Return: Three Distributions That Are Not the Same

### 5.2.1 Desk framing: three people, three ledgers

On a credit desk, three people look at the same bond and see three different random variables. The trader quotes **price**, because that is what the RFQ asks for and what TRACE prints. The PM and the hedger think in **spread**, because spread is what CDX and the factor model are denominated in and what DTS scales. The investor, and the risk system that answers to the investor, eats **return**. These three distributions have different supports, different skews, and different tails, and most of the bugs that reach production in credit risk systems come from computing a moment in one ledger and reporting it in another.

### 5.2.2 Price: a bounded interval with a cap and a floor

A bond's price lives on a bounded interval. On the left, the floor is recovery: no matter how bad the news, a senior claim on a company with assets is worth something, and in the limit $P \to R$ at default. On the right, for a callable bond (most high-yield bonds are callable after a non-call period), the price is capped near the call price $K_{\text{call}}$:

$$
P(s) = P^{\text{straight}}(s) - C^{\text{call}}(s), \qquad \lim_{s \downarrow 0} P(s) \approx K_{\text{call}}, \qquad \lim_{s \downarrow 0} \frac{\partial P}{\partial s} = 0.
$$

The issuer's call option $C^{\text{call}}$ gains value exactly when spreads tighten, so the bond's upside is sold to the issuer. That is negative convexity, the same mechanism as mortgage prepayment in Veronesi's treatment of MBS, and it means the right tail of the price distribution is truncated. "The bond is 102 bid; what's my upside?" is a question with a cap: about a point and a half to a 103.5 first call, plus carry.

> **[SOURCE EXTRACTION]** *Veronesi_Fixed_Income_Securities p.669:* "the distribution is heavily negatively skewed, meaning that the probability of large losses is higher than the probability of symmetrically large gains."
>
> **Annotation.** Veronesi is describing the profit-and-loss distribution of a range note, a structured product in which the investor implicitly sells an option in exchange for yield enhancement. A callable high-yield bond is the same trade in a cheaper suit: the investor is short the issuer's call (which caps the right tail) and short the issuer's default put (which opens the left tail), and is paid for both in the coupon. Veronesi's general lesson, that a sold option produces a negatively skewed P&L whose risk VaR understates and expected shortfall captures, is the operating principle of high-yield risk management. Where the modern desk departs: in Veronesi's range note the sold option is priced off a liquid rate surface; in high yield, the default put has no listed market, and its "implied vol" has to be backed out of the CDS curve, the equity options surface (Chapter 23), or a structural model (Chapter 6), each of which disagrees with the others in exactly the names you care about.

Over a long horizon, then, the price distribution of a single bond looks like a Beta on the shifted interval $[R_{\min}, K_{\text{call}}]$, with a point mass near par (the bond survives and is called or matures) and a recovery lump at the bottom. The chapter's code (§5.9) simulates it this way rather than as a lognormal price, which would allow a high-yield bond to trade at 140.

### 5.2.3 Spread: right-skewed, roughly lognormal

Kaz's whiteboard, under *skew sign flips when?*, now carries the chapter's first stochastic differential equation, and Theo, who has read a great many credit agreements and no stochastic calculus, asks what the little $d$'s are for. It is a fair question, and it gets a fair answer before the equation does.

> **Math, Gently.** *Random walks, the lognormal, and Itô's half-sigma-squared.* A random walk is a drunk leaving a bar: each step is a coin flip, left or right, and the position after many steps is the sum of all the flips. Add up enough small independent steps and the sum is approximately normal, the bell curve, centered where the drunk started, spreading out like the square root of the number of steps. Brownian motion $W_t$ is that walk with infinitely many infinitely small steps, and $dW_t$ is one of the steps. The trouble with letting a spread do a random walk directly is that the drunk can wander through zero, and a negative spread is a company that pays you to lend it money. The fix is to let the drunk walk in the *exponent*: put the bell curve inside $e^{(\cdot)}$ and the result, the *lognormal*, can get as large as it likes but never reaches zero, and it moves in percentages, so a 500 bp spread moves five times as many basis points as a 100 bp one, which is exactly the DTS fact. There is one tax to pay. Because $e^{x}$ curves upward, the average of $e^{X}$ is always bigger than $e$ raised to the average of $X$ (this is Jensen's inequality in one line: a convex function of an average is less than the average of the convex function). So if the walk in the exponent is centered at zero, the spread drifts *up* on average just from the curvature. Itô's lemma is the bookkeeping that catches this: to keep the expected spread at today's $s_0$, the exponent must be centered at $-\tfrac12\kappa^2 h$ rather than at zero. With a relative spread vol of $\kappa = 0.35$ over $h = 1$ year, the correction is $-\tfrac12 \times 0.35^2 = -0.061$, which moves the median spread about 6% below today's level to pay for the upward pull of the curvature, while the mean stays exactly at $s_0$; and the resulting distribution has a skew of about $+1.1$: spreads gap wider more often and further than they gap tighter. The full version, with $(dW_t)^2 = dt$ and the volatility tax derived, is §6.1; Chapter 6-B puts it to work on options.

Spreads live on $(0, \infty)$ and, by the DTS result, their changes scale with their level: $\sigma(\Delta s) \propto s$. If relative spread changes have constant volatility $\kappa$, the natural model is

$$
\frac{ds_t}{s_t} = \kappa\, dW_t \quad\Longrightarrow\quad s_h = s_0 \exp\!\left(-\tfrac{1}{2}\kappa^2 h + \kappa\sqrt{h}\,Z\right), \quad Z \sim N(0,1),
$$

the lognormal, whose skewness is

$$
\text{skew}(s_h) = \left(e^{\kappa^2 h} + 2\right)\sqrt{e^{\kappa^2 h} - 1}.
$$

With $\kappa = 0.35$ and $h = 1$ (an *illustrative* relative spread vol in the range the DTS literature reports), the spread distribution has skewness of about $+1.1$. Spreads gap wider more than they gap tighter, even in the survival world.

### 5.2.4 Return: left-skewed in the survival world, sign-flipping in distress

Because the return is approximately $-D^{\text{spr}}\Delta s$ plus carry, a right-skewed spread produces a **left-skewed return** of about $-1.1$ from the survival world alone. Positive spread convexity pushes back a little for non-callable bonds; negative convexity from the call pushes the other way and makes the left skew worse. Then the default world adds the $-1/\sqrt{q}$ term of §5.1.3 on top.

Now the twist that every distressed investor knows and every Gaussian risk model gets backwards. The Bernoulli skew formula

$$
\text{skew} = -\frac{1 - 2q}{\sqrt{q(1-q)}}
$$

**changes sign at $q = \tfrac{1}{2}$**. A bond whose default probability is above one-half, trading near its expected recovery, has a *right-skewed* return: the downside is a few points to the recovery floor, and the "jump" that matters is the survival world, a rally from 35 to par if the company refinances. Dynkin's discount-bond observation is the price-space version of the same fact.

> **[SOURCE EXTRACTION]** *Dynkin_Systematic_Investing_in_Credit p.426:* "bonds trading at a discount are better shielded from default risk by recovery values."
>
> **Annotation.** Dynkin and coauthors make the point in the context of coupon effects and empirical duration: a low-coupon bond trading at a discount has less distance to fall before it hits the recovery floor, so its spread is lower and its sensitivity to rates is asymmetric. Read it as a statement about the mixture and it becomes the most important regime boundary in high yield. As $P_0 \to \mathbb{E}[R]$, the jump size $J$ in return space shrinks on the downside and grows on the upside, and at some point the bond stops being a credit and becomes an option on the enterprise. This is why a CCC bond is an equity option that wears a tie to work, and why a systematic HY book that ranks on spread will mechanically load on the names where the shape of the return distribution has flipped. The desk departure from Dynkin's framework: post-2020, "shielded by recovery values" assumes the recovery value is a property of the bond. In an LMT world it is a property of the bond *and* of your seat at the negotiating table (§5.5.5).

Which brings the desk back to Friday, 2 June 2023, and the Carvana 5.875% 2028s in the mid-50s. Kaz redraws the hand on the whiteboard with the sign flip in mind, and the picture is unrecognizable next to their hundred-and-four-percent Gaussian. From somewhere between 40 and 55 cents, the downside pot was perhaps fifteen points, to a recovery floor for an unsecured claim on a company with cars, an auction business and a finance platform *(illustrative)*. The upside pot was par: forty-five to sixty points if the company survived, refinanced, or paid up in an exchange. Read the price the way the market was reading it, with a recovery of 35 and no time value, and a price of 50 implies a default probability of $(100-50)/(100-35) \approx 77\%$ *(illustrative, and a $\mathbb{Q}$ number, premia included)*. Above one half. The skeleton skew at $q = 0.77$ is $+(1.54-1)/\sqrt{0.77 \times 0.23} \approx +1.3$: the bond was right-skewed, and the surprise that mattered was the survival world. Kaz's symmetric bell had put one chance in six on a negative price and given equal weight to rallies and collapses of the same size; the actual shape was a short, hard floor on the left and a long arm reaching toward par on the right.

Then the market showed which tail it had. At 31 March 2023 the note stack was carried at 53.8% of book. At 30 June, four weeks after the exchange failed and before any deal had been announced, it was 74.0%. At 30 September, by then mostly the new secured notes, it was 77.7%, and at 31 December 2023 it was 84.7% *(Carvana 10-Q and 10-K Level 2 fair values; ratios computed from reported fair value and carrying amount)*. A bond stack marked at 45 cents at the end of 2022 was marked at 85 a year later. Theo's vote to sell was not stupid; it was a $\mathbb{P}$ estimate of the bad state made from the side of the table where the bad state is the plan, and selling at 55 bought protection against a fifteen-point fall by giving up what turned out to be a thirty-point rise. What happened in July, and why the old 10.25% 2030s did better than everyone else, is the payoff in §5.6.2. The point for this section is narrower: on the second of June, the question "what is the distribution of this bond's one-year return?" had an answer, the answer was right-skewed, and no amount of trailing volatility could have told you so. The price relative to expected recovery could.

The practical rule for the specifier: the risk model must carry the **price level relative to expected recovery** as a state variable, because it determines the sign of the skew. A model that estimates one skew per rating bucket will be wrong in both directions at once, too optimistic on the B3 bond at 92 and too pessimistic on the Caa3 bond at 38.

> **Ways This Blows Up.** *The stale-price smoother.* TRACE prints on high-yield bonds are sparse, and evaluated prices fill the gaps with smooth interpolations. A volatility computed from evaluated marks is biased down, and the bias is worst exactly in the names approaching distress, where trading dries up before the jump. Theo's 4.1% was computed from sixty days of marks, of which (on inspection) eleven were trades. Chapter 7 and Chapter 8 treat stale-price betas formally (Dimson and Scholes–Williams lag sums); for this chapter, the rule is that a survival-world volatility estimated from marks is a lower bound, and the default-world parameters cannot be estimated from the bond's own history at all.

**Quant-shop life (fictional composite): eleven trades in sixty marks.** A systematic asset manager, the Tuesday of the risk report, 2:15 p.m. The 4.1% did not come from Theo; it came from the risk-data pipeline, and the pipeline belongs to a junior quant named Hana, eighteen months out of a master's program, who sits two rows behind the desk and whose name appears on the report only in the footer, as the owner of the `vol_60d` field. Ines has sent her a one-line message: "How many of the sixty are trades?" Hana does not know, which is the honest answer and also the reason she spends the rest of the afternoon finding out.

The job is not glamorous. She pulls the bond's TRACE history from the firm's licensed feed and lines it up, row by row, against the sixty daily marks the volatility was computed from. The marks come from an evaluated-pricing vendor, which produces a price for every bond every day whether or not anybody traded it. The trades come from TRACE, which only knows about trades. Eleven of the sixty days have at least one print. The other forty-nine are the vendor's evaluated price, which on a quiet bond is a smooth function of the vendor's spread curve for the sector and rating, and so moves the way the sector moves, gently. The 4.1% is mostly the volatility of a curve, not of the bond.

Even the eleven days take an hour to trust. FINRA Rule 6730 requires a dealer to report a corporate bond trade "as soon as practicable, but no later than within 15 minutes of the Time of Execution," and a trade done in the last fifteen minutes of the session, or before 8:00 a.m., rolls to after the next open. So two of Hana's eleven prints are stamped with one day's date and reported on the next, and one is an "as/of" report filed late, with an execution time three days before its report time. One print was cancelled and replaced with a corrected price twenty minutes later; the firm's feed carries both rows, with a status code that her loader had been ignoring. Somewhere in the operations group, someone at a dealer had cleared that correction from an exception queue on a Thursday morning, and Hana's back-test had inherited it a year later as a ninety-second round trip of four points that never happened. She removes it and writes it down.

Then the part that makes her put her headphones on. The vendor's evaluated price for one week in the window has changed since she last pulled it. Not the trades; the marks. The vendor restated the column, as vendors do, after its own evaluator caught something, and the history she downloaded today is not the history the risk system saw when it produced yesterday's report. On Jane Street's *Signals and Threads* podcast (episode 29, 2 September 2026), Eric Mannes describes the same species of problem in commodities, vendors who "tell you, whoops, made a mistake," and a firm that saves "all the data ... along with the time we received it" so that it never needs "a time machine." Hana's firm keeps the time it received the trades. It does not keep the time it received the marks. It keeps the latest version, which is a different thing.

At 5:40 p.m. she sends Ines a table with three columns: date, source (trade or evaluated), and price, plus a recomputed volatility from the eleven trade days only, using the lag-sum correction that Chapters 7 and 8 formalize. It comes to 6.8% *(illustrative)*, two-thirds higher than the 4.1%, and still, as she writes underneath, "a survival-world number. This bond has never defaulted, so none of these rows can tell us what default looks like." Ines replies with a thumbs-up, which in Ines's grammar is a full paragraph of praise.

Wednesday at 10:00 a.m. is model review. The firm's model-risk group follows bank practice, which is to say it follows the Federal Reserve's SR 11-7 guidance even though nobody here is a bank, because the firm's largest allocators asked whether it did. The guidance divides validation into three parts, "conceptual soundness," "ongoing monitoring, including process verification and benchmarking," and "outcomes analysis, including back-testing," and it expects "change control procedures" under which "all changes are logged and can be audited." The risk committee, five people and a speakerphone, has two reports in front of it. Monday's says the B3 position's 99% VaR is $-2.5\%$. Tuesday's, the reissued one with two worlds and a coin, says its 99% expected shortfall is $-92\%$. The first question, as it always is, comes from the person who has to sign: "Why is this number different from yesterday?"

The honest answer takes twenty minutes, and most of it is not about distributions. It is about which field changed, who changed it, whether the change was approved before or after the report went out (after, it turns out, which earns a polite note in the minutes), and whether the old report's VaR would have been breached in any back-test window (no, because the bond has not defaulted, which is exactly the problem a back-test of a survival-world model cannot find). The chair asks whether the 4% default probability is a model output or an override. Theo says it came from his 13-week model's lender case. The chair asks whether the 13-week model is in the model inventory. It is not. There is a short silence in which everyone looks at the USB stick.

Nobody trades anything. The meeting ends at 10:47 with three action items, and by noon Hana has opened the ticket: *RISK-2291. `vol_60d` computed on evaluated marks for bonds with fewer than 25% trade days; add `trade_day_share` to the risk record; switch to trade-only lag-sum estimator below threshold; snapshot vendor evaluated prices with receive-time daily (point-in-time); register 13-week cash model in the model inventory as a $\mathbb{P}$ hazard input, owner T. Marsh. Priority: medium.* It sits in the backlog behind a broken holiday calendar for the Canadian feed for eleven days.

> **Trend Watch.** *Dispersion: the mixture weight moved to the bottom of the stack (2023–2026).* On October 15, 2026, the ICE BofA US High Yield Index OAS was 323 bp, the BB sub-index 197 bp, the single-B 326 bp, and the CCC & Lower sub-index 1,278 bp (FRED series BAMLH0A0HYM2, BAMLH0A1HYBB, BAMLH0A2HYB, BAMLH0A3HYC; fetched October 17, 2026). Over the three years FRED currently serves for these series (from October 17, 2023), the CCC-to-HY OAS ratio rose from a low of 2.24 (October 20, 2023) to a high of 4.06 (September 11, 2026); at quarter-ends it was 2.66 (December 2023), 2.55 (December 2024), 3.15 (December 2025), 3.53 (June 2026), and 3.78 (September 2026). The BB OAS touched 150 bp on August 28, 2026, while the CCC OAS hit 1,282 bp on October 14, 2026: the top of the high-yield market priced near its tightest levels of the window at the same time the bottom priced its widest. The index-level peak in the window, 461 bp on April 7, 2025, came with the April 2025 tariff shock. *(Ratios, extremes, and quarter-end values are the author's computations from the FRED series.)* What it means for the mixture: run the credit triangle of Chapter 6 backwards with a 40% recovery convention and the CCC sub-index spread implies a risk-neutral annual default intensity of roughly $0.1278/0.6 \approx 21\%$, against about 3% for BB (author's arithmetic; $\mathbb{Q}$-measure, so it includes risk and liquidity premia). An index spread of 323 bp is therefore not a statement about a typical bond. It is a weighted average of a BB carry trade and a CCC jump lottery, and the weight on the lottery's bad outcome is concentrated in loan-only, sponsor-backed capital structures, which is where Moody's located the distress in 2025 (Moody's Analytics, *US Credit Review & Outlook*, 7 August 2025). For a systematic desk this is a regime signal (Chapter 12 uses the CCC/HY ratio as a mixture-weight indicator) and a reminder that "the market" has no single return distribution.

### Deep-Dive Resource Graph

- **Podcasts:** Bloomberg *Odd Lots* coverage of high-yield bifurcation and CCC stress (2025–2026; episode titles to be confirmed).
- **Practitioner Writing:** Dynkin, Hyman, and coauthors, *Systematic Investing in Credit* (Wiley), chapters on coupon effects and empirical duration (shelf: Dynkin_Systematic_Investing_in_Credit p.426); Veronesi, *Fixed Income Securities*, on negative convexity and option-induced skew (shelf: Veronesi_Fixed_Income_Securities p.669).
- **Academic Papers:** Ben Dor, Dynkin, Hyman, Houweling, van Leeuwen, Penninga (2007), *DTS (Duration Times Spread)*, Journal of Portfolio Management; Dimson (1979), *Risk Measurement When Shares Are Subject to Infrequent Trading*, Journal of Financial Economics.
- **Data & Code:** FRED ICE BofA OAS series: https://fred.stlouisfed.org/series/BAMLH0A0HYM2 and https://fred.stlouisfed.org/series/BAMLH0A3HYC ; FINRA TRACE (see Appendix B for access and dissemination caps).

## 5.3 Jumps in Continuous Time: Merton, Kou, and the Short End

### 5.3.1 Desk framing: the bond does not care how long it has left

The mixture of §5.1 is a one-period object. Desks need a continuous-time version for three reasons: to price instruments of different maturities consistently, to simulate paths for risk (a bond can default in month 2 or month 11, and you collect different coupons), and to get the short end of the credit curve right. That last reason is the one Kaz cares about.

> **[SOURCE EXTRACTION]** *Dynkin_Systematic_Investing_in_Credit p.465:* "Jump to defaults would typically trigger price to expected recovery values with little relationship to the maturity of the bond."
>
> **Annotation.** Dynkin and coauthors make this remark while explaining why downgrade losses do not scale cleanly with duration across maturity buckets. Its implication for risk systems is sharper than it first looks. A jump to default takes every bond of the issuer, short or long, to roughly the same recovery (they are typically pari passu claims of the same face in bankruptcy, accrued interest aside), so the jump-to-default loss on bond $i$ is $P_i - R$ *in points*, independent of duration. The 2-year bond at 98 has more JTD exposure per unit of face than the 8-year bond at 85, even though the 8-year has four times the spread duration. Two consequences for the desk: a duration-neutral curve trade (long the short bond, short the long bond, DTS-matched) is not JTD-neutral, and is in fact long default risk in points; and any risk model that represents a bond only by DTS has no column in which to put its JTD. Chapter 28's limit framework carries JTD as a separate risk axis for exactly this reason.

### 5.3.2 Merton (1976): Gaussian diffusion plus compound Poisson jumps

A notation collision first. The book reserves $\lambda$ for the default intensity. In a structural jump model, the asset value jumps at some rate, and only some jumps cause default; we write the asset-jump arrival rate as $\lambda^{V}$ and keep $\lambda$ for the resulting default intensity, which we derive below.

> **Math, Gently.** *Poisson processes, compound Poisson, and jump-diffusion.* Sit in a parked car in light rain and count the drops that hit a square of windshield. You are not measuring anything continuous; you are counting. Drops arrive independently, at a steady average rate, and the number that land in a minute is random. That count is a *Poisson process* $N_t$, and its rate, the average number of arrivals per unit of time, is the single number that describes it. With a rate of $\lambda^{V} = 0.5$ jumps a year, the chance of no jump in a year is $e^{-0.5} \approx 60.7\%$, of exactly one is $0.5\,e^{-0.5} \approx 30.3\%$, and of exactly two is $\tfrac{0.5^2}{2}e^{-0.5} \approx 7.6\%$; the general recipe is $e^{-\lambda T}(\lambda T)^n/n!$. Now let each drop have a random size, some big and some small: that is a *compound Poisson* process, which counts arrivals and adds up a random amount for each one. A *jump-diffusion* is the windshield in mixed weather: a steady drizzle that wets it a little all the time (the Brownian part, $\sigma_V\,dW_t$, from §5.2.3's random walk), plus occasional hailstones of random size that each make a dent (the compound Poisson part). For a firm's asset value, the drizzle is the ordinary week-to-week news and the hail is the lawsuit, the lost contract, the fraud. The full version is the equation just below and the density in *The Full Derivation* after §5.3.3.

Merton's jump-diffusion for firm asset value is

$$
\frac{dV_t}{V_{t^-}} = \left(\mu - \lambda^{V} k\right)dt + \sigma_V\, dW_t + \left(e^{Y} - 1\right)dN_t,
$$

where $N_t$ is a Poisson process with rate $\lambda^{V}$, each jump multiplies $V$ by $e^{Y}$ with $Y \sim N(\mu_J, \sigma_J^2)$ i.i.d., and $k = \mathbb{E}[e^{Y} - 1] = e^{\mu_J + \sigma_J^2/2} - 1$ is the mean proportional jump, subtracted from the drift so that $\mu$ remains the total expected return. Conditional on the number of jumps, the log-return is Gaussian, so the unconditional distribution is a Poisson-weighted mixture of Gaussians: §5.1's mixture with infinitely many worlds, one for each possible count of hailstones. Over horizons of a year or less, the zero-jump and one-jump worlds carry nearly all the weight (with the box's numbers, 91% between them), which is why the one-period mixture is a good approximation. The density itself, and the truncation rule ROBO needs before it sums an infinite series, are in *The Full Derivation: the Merton density and its truncation*, after §5.3.3.

### 5.3.3 Kou (2002): double-exponential jumps, and why memorylessness is a gift

Merton's Gaussian jump sizes make first-passage problems (default when $V$ hits a barrier $B$) intractable. Kou's double-exponential jumps fix this. The log-jump $Y$ has density

$$
f_Y(y) = p\,\eta_1 e^{-\eta_1 y}\,\mathbf{1}_{\{y \ge 0\}} + (1 - p)\,\eta_2 e^{\eta_2 y}\,\mathbf{1}_{\{y < 0\}}, \qquad \eta_1 > 1,\; \eta_2 > 0,
$$

so an upward jump is exponential with mean $1/\eta_1$ and a downward jump is exponential with mean $1/\eta_2$; $p$ is the probability that a jump is upward. The condition $\eta_1 > 1$ keeps $\mathbb{E}[e^{Y}] = p\eta_1/(\eta_1 - 1) + (1-p)\eta_2/(\eta_2 + 1)$ finite. The exponential distribution's memorylessness is the key: if a downward jump has to exceed a distance $d$ to cross the barrier, then given that it does, the *overshoot* beyond the barrier is again exponential with the same rate.

Two results fall out, and both are worth deriving because they are the cleanest bridge between structural models and the recovery distribution.

**Result 1: jump-to-default intensity and a non-zero short spread.** Let the firm sit at $V > B$, with log-distance to default $d = \ln(V/B)$. In the next instant $dt$, the diffusion cannot reach the barrier (the probability is exponentially small in $d^2/dt$, so it is $o(dt)$). A jump arrives with probability $\lambda^{V}dt$; it is downward with probability $1-p$; and it crosses the barrier if its size exceeds $d$, which for an exponential with rate $\eta_2$ has probability $e^{-\eta_2 d} = (B/V)^{\eta_2}$. Therefore the instantaneous default intensity is

$$
\lambda = \lambda^{V}(1 - p)\left(\frac{B}{V}\right)^{\eta_2}.
$$

Under $\mathbb{Q}$, the short-maturity credit spread is intensity times loss, $s(0^{+}) = \lambda^{\mathbb{Q}} L^{\mathbb{Q}}$, which is *strictly positive*. The diffusion-only Merton (1974) model, by contrast, gives a short spread of zero, a famous embarrassment that Chapter 6 treats in detail: a firm one day from maturity with a positive distance to default cannot diffuse into default fast enough to matter, so the model says one-week paper of a CCC issuer should trade at Treasuries. Kaz once asked, reasonably, whether the market could simply be wrong about this. It cannot. The market is pricing the jump.

**Result 2: recovery given a jump default, in closed form.** At default, the asset value is the barrier times an exponential undershoot: $V_\tau = B\,e^{-U}$ with $U \sim \text{Exp}(\eta_2)$ by memorylessness. Hence

$$
\mathbb{E}\!\left[\frac{V_\tau}{B}\right] = \mathbb{E}\!\left[e^{-U}\right] = \frac{\eta_2}{1 + \eta_2}.
$$

If creditors recover the post-default asset value net of a proportional bankruptcy cost $\alpha$, per unit of face $F$, the expected recovery given a jump default is

$$
\mathbb{E}[R \mid \text{jump default}] = (1 - \alpha)\,\frac{B}{F}\,\frac{\eta_2}{1 + \eta_2}.
$$

Now look at what one parameter does. Fatter downward jumps (smaller $\eta_2$) raise the default intensity through $(B/V)^{\eta_2}$ *and* lower the recovery through $\eta_2/(1+\eta_2)$. The model produces **PD–LGD correlation for free**, from a single structural assumption: the shocks that kill firms are the shocks that destroy asset value. That is the micro-foundation of the downturn-LGD effect that Altman and coauthors measure in the data (§5.5.4).

*Illustrative numbers* (author's arithmetic). Take $V/B = 1.5$, $\lambda^{V} = 0.5$ per year, $p = 0.4$, $B = F$, $\alpha = 0.3$:

| $\eta_2$ (mean down-jump $1/\eta_2$ in log terms) | Jump-default intensity $\lambda$ | $\mathbb{E}[R \mid \text{jump default}]$ | Short spread $\lambda L$ |
| :--- | ---: | ---: | ---: |
| 4 (25%) | 5.9% | 56.0% | 261 bp |
| 3 (33%) | 8.9% | 52.5% | 422 bp |
| 2 (50%) | 13.3% | 46.7% | 711 bp |

Moving $\eta_2$ from 4 to 2 more than doubles the default intensity and costs nine points of recovery. A desk that models PD and recovery as independent, with recovery fixed at 40%, will price the 711 bp name as though it were cheap relative to the 260 bp name by a ratio that ignores half the story.

#### The Full Derivation: the Merton density and its truncation

Start from Merton's equation in §5.3.2. Conditional on $n$ jumps in $[0, T]$, the log-return $x = \ln(V_T/V_0)$ is Gaussian, so the unconditional density is a Poisson-weighted mixture of Gaussians:

$$
f(x) = \sum_{n=0}^{\infty} \frac{e^{-\lambda^{V} T}\left(\lambda^{V} T\right)^n}{n!}\;\phi\!\left(x;\; \left(\mu - \tfrac{1}{2}\sigma_V^2 - \lambda^{V} k\right)T + n\mu_J,\;\; \sigma_V^2 T + n\sigma_J^2\right),
$$

with $\phi(x; m, v)$ the normal density with mean $m$ and variance $v$. Read it as §5.1's mixture with infinitely many worlds: zero jumps, one jump, two jumps, each a Gaussian with its own center. For credit, the $n = 0$ and $n = 1$ terms carry nearly all the weight over horizons of a year or less, which is why the one-period mixture is a good approximation.

**Implementation note for the specifier.** Truncate the sum at $n_{\max}$ where the Poisson tail mass $1 - \sum_{n \le n_{\max}} \Pr(N_T = n)$ is below $10^{-12}$, compute the Poisson weights in log space (`scipy.stats.poisson.logpmf`), and never let ROBO pick $n_{\max} = 10$ "because it looked converged" on a parameter set with $\lambda^{V}T = 30$.

### 5.3.4 What the jump model is for on a desk, and what it is not

The jump-diffusion's job on a desk is threefold: (i) it gives a consistent term structure from the short end out, which matters for pricing two-year paper against CDS; (ii) it gives a path simulator for JTD and expected shortfall in which recovery and default timing are joint outputs; and (iii) it lets the desk map an equity-options skew to a credit view (Chapter 23), because jumps are what make deep out-of-the-money puts expensive.

Its job is *not* to be calibrated from a single bond's price history. Bohn and Stein make the point bluntly when surveying structural models with jumps: implementation founders on the instability of the jump-risk parameters, because credit data are rare-event data and the estimates move a lot with the sample (Bohn_Stein_Active_Credit_Portfolio_Management p.182, paraphrased). The desk resolution is a division of labor: estimate $\lambda^{V}$, $p$, $\eta_2$ from cross-sections and liquid markets (CDS curves, equity option surfaces, index tranches), and then *condition* on issuer features. Never estimate a jump intensity from one issuer's sixty days of TRACE marks, which contain, as noted, zero jumps.

> **[SOURCE EXTRACTION]** *Bolder_Credit_Risk_Modelling p.45:* "Default is a binary event. It either happens or it doesn’t. Once it happens, default is also typically a permanent state. After arrival in default, exit is, in general, a slow and messy process."
>
> **Annotation.** Bolder's three sentences are the specification of the default state in a Markov chain: an absorbing state, entered by a jump, exited slowly if at all. Two things have changed since this framing became standard, and both matter for the code. First, the "binary" event is no longer binary. A distressed exchange is a default for rating-agency purposes but not for the bond's cash flows in the way a bankruptcy is, and the issuer frequently re-enters the default state later; Moody's 2026 study of 1,173 soft-event borrowers found that roughly one in four ended in a hard default (§5.6). The default state is therefore absorbing only for the *hard* default; the soft default is a transient state with a high outbound hazard. Second, "slow and messy" exit is where the RSSG reader's process knowledge (exclusivity periods, DIP roll-ups, plan valuation fights) becomes a recovery model input: the time to emergence is a random variable correlated with the recovery itself, and the post-default trading price is a $\mathbb{Q}$-expectation over that whole messy process (§5.5.6).

> **Ways This Blows Up.** *Three classic jump-model failures.* (1) *Measure confusion:* jump intensities calibrated to CDS spreads are $\mathbb{Q}$ quantities that embed a jump-risk premium; using them in a $\mathbb{P}$ risk simulation overstates expected losses and makes every long look terrible. Keep `lambda_Q` and `lambda_P` as different fields, never one field with a comment. (2) *Discretization bias:* simulating first passage on a weekly grid misses diffusive barrier crossings between grid points; the Brownian-bridge correction (Chapter 6) fixes the diffusion part, while the jump part needs exact jump times drawn from the Poisson process, not "a jump this week with probability $\lambda^{V}\Delta t$." (3) *Identification:* with only a CDS curve, $\lambda^{V}$, $p$, and $\eta_2$ are not separately identified; ROBO will happily return a minimum on a flat ridge and report three significant figures for each.

### Deep-Dive Resource Graph

- **Podcasts:** Corey Hoffstein, *Flirting with Models* (episodes on tail risk and jump hedging; titles to be confirmed).
- **Practitioner Writing:** Bohn and Stein, *Active Credit Portfolio Management in Practice* (Wiley), structural models with jumps (shelf: Bohn_Stein_Active_Credit_Portfolio_Management p.182).
- **Academic Papers:** Merton (1976), *Option Pricing When Underlying Stock Returns Are Discontinuous*, Journal of Financial Economics; Kou (2002), *A Jump-Diffusion Model for Option Pricing*, Management Science; Kou and Wang (2003), *First Passage Times of a Jump Diffusion Process*, Advances in Applied Probability; Zhou (2001), *The Term Structure of Credit Spreads with Jump Risk*, Journal of Banking & Finance; Chen and Kou (2009), *Credit Spreads, Optimal Capital Structure, and Implied Volatility with Endogenous Default and Jump Risk*, Mathematical Finance.
- **Data & Code:** `simulate_kou_jd` and its short-maturity intensity check in §5.9.

## 5.4 Lévy Processes: What Is Useful and What Is Decoration

Kaz loves the variance gamma process. Ines's question about any model is the same: "What does it change about the bid?" This section answers her, briefly, because the honest answer for single-name high yield is "not much," and the honest answer for indices, ETFs, and options is "quite a lot."

A **Lévy process** is any process with independent, stationary increments. Its characteristic function has the Lévy–Khintchine form $\mathbb{E}[e^{iuX_t}] = e^{t\psi(u)}$ with

$$
\psi(u) = i b u - \tfrac{1}{2}\sigma^2 u^2 + \int_{\mathbb{R}\setminus\{0\}} \left(e^{iux} - 1 - iux\,\mathbf{1}_{\{|x|<1\}}\right)\Pi(dx),
$$

a drift, a Gaussian part, and a jump measure $\Pi$ that says how many jumps of each size arrive per unit time. Merton and Kou are the *finite-activity* case: $\Pi$ has finite total mass $\lambda^{V}$, so jumps are rare events you can count. The *infinite-activity* models put infinite mass near zero: infinitely many tiny jumps, which replace the diffusion.

**Variance gamma** (Madan and Seneta 1990; Madan, Carr, and Chang 1998) runs a Brownian motion with drift on a random gamma clock: $X_t = \theta G_t + \sigma W_{G_t}$, where $G_t$ is a gamma process with mean $t$ and variance rate $\nu$ (a VG parameter, not to be confused with anything else in this chapter). Its characteristic function is $(1 - iu\theta\nu + \tfrac{1}{2}\sigma^2\nu u^2)^{-t/\nu}$, its variance is $(\sigma^2 + \theta^2\nu)t$, and for $\theta = 0$ its excess kurtosis is $3\nu/t$. **Normal inverse Gaussian** (Barndorff-Nielsen 1997) does the same with an inverse-Gaussian clock and has closed-form moments: with $\gamma_{\text{NIG}} = \sqrt{\alpha^2 - \beta^2}$, skewness $3\beta/(\alpha\sqrt{\delta\gamma_{\text{NIG}}})$ and excess kurtosis $3(1 + 4\beta^2/\alpha^2)/(\delta\gamma_{\text{NIG}})$ per unit time. (The subscript avoids a collision with the book's risk-aversion $\gamma$.)

> **[SOURCE EXTRACTION]** *Bolder_Credit_Risk_Modelling p.229:* "Since neither the gamma nor the generalized inverse-Gaussian laws possess a power tail, sadly these models do not exhibit positive tail dependence."
>
> **Annotation.** Bolder is discussing normal-variance-mixture threshold models for portfolio default, in which a common mixing variable scales every obligor's latent variable. His point, stated two pages earlier in the same chapter, is that tail dependence (the probability that two names default together in the extreme) comes from a *power-tailed* mixing variable, as in the $t$ distribution, and not from leptokurtosis as such. VG and NIG have fat-looking, thin-waisted densities and plenty of kurtosis, but their tails decay exponentially, so they do not make joint extreme defaults more likely in the limit. For the desk this is a specification rule: if the purpose of the model is portfolio jump-to-default clustering, choose the mixing law for its tail, not its kurtosis. The departure: practitioners now calibrate dependence to observed default clustering by sector and sponsor (Chapter 14), and a sponsor's portfolio of loan-only borrowers is a cluster that no symmetric mixing variable captures.

Two more facts settle the verdict. The excess kurtosis of VG decays like $1/t$, so a model fitted to daily returns says almost nothing about the quarterly horizon at which a credit book actually takes its losses. And infinite-activity models need dense, clean price data to calibrate, which CDX options, HYG and JNK, and equity option surfaces have, and which single-name high-yield bonds, with their stale TRACE prints, do not.

| Model | Use it for | Decoration when used for |
| :--- | :--- | :--- |
| Gaussian diffusion | Survival-world spread wiggle, short horizons | Anything that includes default |
| Compound Poisson + Gaussian (Merton) | Single-name return mixtures, JTD simulation | Fitting a single bond's daily history |
| Kou double-exponential | Analytic first passage, short-end spreads, PD–LGD link | Precise calibration of $\eta_1$ from bond data |
| VG / NIG | CDX option skews, ETF daily returns, equity-to-credit vol maps | Single-name HY bond returns from TRACE |
| $t$ or power-tailed mixtures | Portfolio tail dependence, default clustering | Recovery modeling (bounded support) |

Kaz's summary, after an afternoon of trying to calibrate VG to a B2 bond with nine trades in a month: "It fits beautifully. It fits anything. That's the problem."

## 5.5 Recovery as a Random Variable: Beta Models Conditioned on Collateral and Seniority

### 5.5.1 Desk framing: the waterfall was always a distribution

"Price is what you pay," Mags says. "Recovery is what you get, eventually, after the lawyers." She means that recovery is uncertain in three dimensions at once: how much, when, and in what currency (cash, new debt, or post-reorg equity of uncertain value).

The RSSG reader's aha is that you have been building recovery distributions for years and calling them waterfalls. Moyer's plan-outcome tables are recovery *functions*: choose an enterprise value multiple, run absolute priority, read off recovery by class.

> **[SOURCE EXTRACTION]** *Moyer_Distressed_Debt_Analysis p.251:* "Again, note that the valuation assumption determines the total amount of recovery, particularly to junior classes. This should reinforce why the issue of valuation is so hotly contested in the plan negotiation."
>
> **Annotation.** Moyer's tables compare plan outcomes under low and high valuations and show junior classes swinging from near zero to meaningful recoveries. The quant's recovery model is the same object with one more step: put a probability distribution on $\text{EV}$ and integrate the waterfall over it. Recovery for class $j$ is then $R_j = W_j(\text{EV})$, a piecewise-linear, monotone function of a random variable, and its distribution inherits a point mass at zero (EV below the class's attachment point), a point mass at one (EV above its detachment point), and a continuous middle. Moody's loss-given-default methodology (August 2006) did exactly this, drawing firm-wide recovery from a Beta distribution on $[0, 1.2]$ of liabilities with mean 50.21% and standard deviation 26.46% and pushing it through the priority-of-claims waterfall. The modern departure is that "priority" is no longer fixed at issuance: in an uptier, the waterfall itself is redrawn, and the attachment point of your class becomes a random variable too.

Kaz, reading over Theo's shoulder, asks what the "debt cushion" line is, and whether it is an ergonomic benefit. Mags: "It's the junior debt that gets wiped out before you do. There used to be some." The debt cushion (the share of the capital structure junior to your claim) is the single best predictor of a class's recovery in most empirical studies, and its disappearance is the subject of this section's Trend Watch.

### 5.5.2 The Beta distribution and the method of moments

The Beta density on $(0,1)$ is

$$
f(r; a, b) = \frac{r^{a-1}(1-r)^{b-1}}{B(a,b)}, \qquad a, b > 0,
$$

with mean $\mu = a/(a+b)$ and variance $\sigma^2 = \mu(1-\mu)/(a+b+1)$. Inverting gives the method-of-moments estimator

$$
a = \mu\left[\frac{\mu(1-\mu)}{\sigma^2} - 1\right], \qquad b = (1-\mu)\left[\frac{\mu(1-\mu)}{\sigma^2} - 1\right],
$$

which exists only if $\sigma^2 < \mu(1-\mu)$, the variance of a Bernoulli with the same mean. A recovery sample whose variance is at or above that bound is telling you it is all-or-nothing, and the code must raise, not clip.

> **[SOURCE EXTRACTION]** *Bohn_Stein_Active_Credit_Portfolio_Management p.297:* "Note the characteristic U-shape of the ultimate recoveries, suggesting that in many cases, recovery can be an all-or-nothing process."
>
> **Annotation.** Bohn and Stein are describing Moody's data on ultimate (settlement) recoveries, which pile up near zero and near par, unlike 30-day post-default trading prices, which are more hump-shaped because the market averages over the outcomes it cannot yet see. The U-shape is what a waterfall integrated over a wide EV distribution produces: most classes are either in the money or out of it. The Beta family can produce a U (both $a, b < 1$), a J at either end (one parameter below one), or a hump (both above one), which is why Bohn and Stein call it the common choice for LGD (p.313) and Bolder notes that its support, like default severity, is the unit interval (Bolder_Credit_Risk_Modelling p.84). The departure for 2026: the LMT era adds a *third* lump in the middle of the first-lien distribution, the excluded lender's recovery, which a single Beta cannot produce. §5.6 handles it as a mixture of Betas.

Three method-of-moments fits show the range (*author's arithmetic from stated moments; illustrative*):

| Population | Mean, s.d. | $(a, b)$ | Shape |
| :--- | :--- | :--- | :--- |
| Senior unsecured bonds, Moody's 1970–2002Q2 (Schmid p.103) | 40.07%, 27.50% | (0.87, 1.30) | Spike at zero |
| First-lien loan book (illustrative) | 70%, 30% | (0.93, 0.40) | U-shape, heavy at par |
| Moody's family recovery, rescaled from $[0, 1.2]$ | 50.21%, 26.46% | (1.68, 2.33) | Interior hump |

### 5.5.3 Beta regression and inflated masses: conditioning on what the RSSG reader knows

A table of Betas by seniority is a lookup table, and Schmid's complaint about lookup tables applies: recovery is "estimated by appealing to historical averages although the extreme range of the historical data makes one doubt about its use" (Schmid_Credit_Risk_Pricing_Models p.96). The fix is to let the Beta's mean depend on covariates. In the Ferrari and Cribari-Neto (2004) parameterization, $r_i \sim \text{Beta}(\mu_i\phi, (1-\mu_i)\phi)$ with precision $\phi > 0$ and

$$
\operatorname{logit}(\mu_i) = x_i^{\top}\beta,
$$

so the per-observation log-likelihood is

$$
\ell_i = \ln\Gamma(\phi) - \ln\Gamma(\mu_i\phi) - \ln\Gamma\big((1-\mu_i)\phi\big) + (\mu_i\phi - 1)\ln r_i + \big((1-\mu_i)\phi - 1\big)\ln(1 - r_i).
$$

The covariate vector $x_i$ is where the RSSG seat pays. A pure quant has seniority and industry. You have: collateral coverage (collateral value over claim, continuous), debt cushion (share of the stack junior to the claim), loan-only flag, cov-lite flag, sponsor flag, prior-LMT flag, industry-distress indicator (Acharya, Bharath, and Srinivasan 2007 show defaulted firms in distressed industries recover less), the trailing speculative-grade default rate, jurisdiction, and, since 2020, **participation status** in the last LMT. A loan-only, cov-lite, sponsor-backed "first lien" with no debt cushion is a senior unsecured bond wearing a name tag that says FIRST LIEN, and the regression should be allowed to read the name tag and then ignore it.

Exact zeros and ones break the plain Beta: $\ln r_i = -\infty$ at $r_i = 0$. The **zero-one-inflated Beta** (Ospina and Ferrari 2010) adds point masses:

$$
\Pr(r = 0) = \pi_0, \qquad \Pr(r = 1) = \pi_1, \qquad r \mid r \in (0,1) \sim \text{Beta}\big(\mu\phi, (1-\mu)\phi\big),
$$

with $(\pi_0, \pi_1)$ modeled by a multinomial logit on the same covariates. Bohn and Stein describe the two-stage industrial version: a probit for whether the loss is positive, then a regression for its size (p.316). An FDIC working paper comparing LGD models (Li, Zhang, and Zhao 2018) found that mean predictions are similar across OLS, fractional response, and Beta-family models, but that the models that respect bimodality win clearly on the *predicted distribution*, which is the object a mixture risk model consumes.

### 5.5.4 Downturn recovery: PD and LGD share a factor

Recoveries fall when defaults rise. Schmid summarizes Altman, Brady, Resti, and Sironi (2005): "one can explain 51% of the variation in the annual recovery rates with the level of default rates in a linear model, and approximately 60% with logarithmic and power relationships" (Schmid_Credit_Risk_Pricing_Models p.103), and the Moody's table on the same page shows mean recoveries of 27.85% in recessions versus 43.10% in expansions. The specification is a shared systematic factor $Z_t$ that drives both default and recovery,

$$
\operatorname{logit}(\mu_{i,t}) = x_i^{\top}\beta - \kappa_R Z_t, \qquad \Pr(D_{i,t} = 1 \mid Z_t) = \Phi\!\left(\frac{\Phi^{-1}(q_i) + \sqrt{\rho}\,Z_t}{\sqrt{1-\rho}}\right),
$$

in the spirit of Frye's "collateral damage" model, where $Z_t > 0$ is a bad state, $\rho$ the asset correlation, and $\kappa_R > 0$ the recovery loading (the subscript separates it from the DTS $\kappa$ of §5.1). Kou's model in §5.3.3 gave the same correlation structurally. Ignore it and your portfolio's 99th-percentile loss is too small twice: too few defaults in the bad state, each too cheap.

### 5.5.5 Participation status: the covariate with the biggest coefficient

In a non-pro-rata uptier, two lenders holding the same tranche, with the same collateral and the same seniority label, end up with different claims. The covariate "participant in the last LMT" therefore has a coefficient that, in the cases that reached court, is larger than seniority's. The Case Study in §5.6.2 puts numbers on it.

### 5.5.6 $\mathbb{P}$ recovery, $\mathbb{Q}$ recovery, and the 40% that is neither

> **[SOURCE EXTRACTION]** *Bohn_Stein_Active_Credit_Portfolio_Management p.300:* "When using post-default prices of recovery, either in a look-up table or through the use of a model, the predicted value is a risk-neutral measure of the expected discounted future recovery."
>
> **Annotation.** This is the sentence that keeps two datasets out of one regression. The 30-day post-default trading price is a market price, so it is a $\mathbb{Q}$-expectation of the discounted ultimate recovery, net of a risk premium for the messy, slow exit Bolder described. The ultimate discounted recovery is a $\mathbb{P}$ realization. They differ systematically, and a model fitted to one and used as the other will be biased in a direction that depends on the cycle. The spec in §5.9 makes `target` a required argument and refuses to fit a panel that mixes the two. The modern departure: on a desk, the post-default price is also the price at which a forced seller (a CLO with a CCC bucket problem, a ratings-constrained insurer) sells to you, so it contains a liquidity discount that is a trading opportunity, not a forecast.

And the famous 40%? Dynkin is candid about what it is: "A representative average recovery rate of 40% is assumed, such that a loss of 60% is assumed to be incurred with the specified probability" (Dynkin_Systematic_Investing_in_Credit p.354). In CDS, the standard model uses a fixed recovery to convert running spreads into upfronts (Chapter 24); it is a conversion convention. A CDS spread identifies only the product $\lambda^{\mathbb{Q}}L^{\mathbb{Q}}$ (the credit triangle, Chapter 6), and separating the two requires recovery locks, digital CDS, or term-structure restrictions (Pan and Singleton 2008; Doshi, Elkamhi, and Ornthanalai 2018). Mags remembers the old days: "We assumed 40 because the bonds were actually senior to something. Now the first lien is senior to the other first lien, depending on counsel."

> **Trend Watch.** *Recovery compression and the death of the debt cushion (2019–2026).* Long-run baselines, Moody's data as reproduced by the Bermuda Monetary Authority (September 5, 2024): trading-price recoveries 1983–2023 of approximately 65% for first-lien bank loans, 55% for first-lien bonds, and 38% for senior unsecured bonds; ultimate recoveries 1987–2023 of approximately 87% for revolvers, 71% for term loans, 62% for senior secured bonds, and 47% for senior unsecured bonds. The same report cites S&P that first-lien and priority debt now make up more than 75% of total debt in typical structures. Fitch's 2023 *Annual Manual* (March 30, 2023) put first-lien institutional leveraged loan 30-day post-default prices for 2007–2022 at an average of 59.5% (median 62.8%), with recovery ratings migrating down "as companies increasingly relied on first-lien heavy structures." S&P (*CreditWeek*, February 20, 2025, via search summary) reported that its first-lien recovery ratings had fallen to the mid-to-low 60% range over six years, against long-term realized averages of 75%–80%, citing higher leverage, shrinking junior debt cushions, and cov-lite structures. Moody's data reported by Bloomberg Law (April 23, 2025) put first-lien distressed-exchange recoveries at 71% at end-2024, up from 55% in 2023, and Moody's September 22, 2026 *Corporate Defaults and Recoveries* report (via American Banker, September 28, 2026) projected first-lien loan recoveries "declining to 55%." What it means for the model: the long-run 71%–76% first-lien ultimate recovery is a property of a capital structure that had a junior cushion. The Beta regression's debt-cushion and loan-only coefficients are not static; refit them on post-2019 defaults, and treat any recovery prior drawn from pre-2015 data as an upper bound for sponsor-backed, loan-only borrowers.

### Deep-Dive Resource Graph

- **Podcasts:** Bloomberg Intelligence, *The Credit Edge* (episodes on recoveries and LMEs; titles to be confirmed).
- **Practitioner Writing:** Moody's, *Loss Given Default Rating Methodology* (August 2006), mirror at https://care-mendoza.nd.edu/assets/152347/loss-given-default-rating-methodology.pdf ; Bermuda Monetary Authority, *Private Credit: Deep Dive on Direct Loans, CLOs and Private Placements* (September 5, 2024), https://cdn.bma.bm/documents/2024-09-05-11-50-00-Private-Credit---Deep-dive-on-Direct-Loans-CLOs-and-Private-Placements.pdf ; Fitch, *The 2023 Annual Manual: A Primer on the U.S. Leveraged Finance Market* (March 30, 2023).
- **Academic Papers:** Ferrari and Cribari-Neto (2004), *Beta Regression for Modelling Rates and Proportions*, Journal of Applied Statistics; Ospina and Ferrari (2010), *Inflated Beta Distributions*, Statistical Papers; Altman, Brady, Resti, and Sironi (2005), *The Link between Default and Recovery Rates*, Journal of Business, https://ideas.repec.org/a/ucp/jnlbus/v78y2005i6p2203-2228.html ; Acharya, Bharath, and Srinivasan (2007), *Does Industry-Wide Distress Affect Defaulted Firms?*, Journal of Financial Economics; Jankowitsch, Nagler, and Subrahmanyam (2014), *The Determinants of Recovery Rates in the US Corporate Bond Market*, Journal of Financial Economics; Altman and Kalotay (2014), *Ultimate Recovery Mixtures*, Journal of Banking & Finance; Frye (2000), *Collateral Damage*, Risk; Li, Zhang, and Zhao (2018), *Modeling Loss Given Default*, FDIC CFR WP 2018-03, https://www.fdic.gov/analysis/cfr/working-papers/2018/cfr-wp2018-03.pdf ; Berd (2005), *Recovery Swaps*, Journal of Credit Risk, https://arxiv.org/abs/1001.0783 .
- **Data & Code:** Moody's Default & Recovery Database and Ultimate Recovery Database (subscription); `beta_mom` and `fit_beta_regression` in §5.9.

## 5.6 The Default Is Now a Negotiation: Distressed Exchanges, Re-Default, and Regime Mixtures

### 5.6.1 The Bernoulli becomes a categorical variable

"We are represented by counsel," says the Ad Hoc Group, in unison. "Our recovery is seventy-three point seven to one hundred. Yours is a rounding error."

The chorus is quoting a real plan (§5.6.2), and it is telling the modeler that the default leg of §5.1 is itself a mixture. Replace the Bernoulli $D$ with a categorical event $E \in \{\text{survive}, \text{DE}, \text{HD}\}$, where DE is a distressed exchange or LMT classified as a default and HD is a hard default (payment default or bankruptcy), with probabilities $(1 - q_{\text{DE}} - q_{\text{HD}}, q_{\text{DE}}, q_{\text{HD}})$. A DE is not absorbing: it moves the issuer into a transient state with a front-loaded re-default hazard. Moody's 2026 re-default study supplies a calibration. If a fraction $\pi_{\text{re}} \approx 0.25$ of soft events end in hard default, and more than 70% of those arrive within two years, an exponential re-default clock with rate $\theta$ satisfying $1 - e^{-2\theta} = 0.7$ gives $\theta \approx 0.60$ per year and

$$
\Pr(\text{HD by } t \mid \text{DE at } 0) = \pi_{\text{re}}\left(1 - e^{-\theta t}\right) \approx 0.25\left(1 - e^{-0.60\,t}\right)
$$

(*author's calibration, illustrative*). The DE leg's recovery is then a mixture too: the exchange value $R_{\text{DE}}$ if the issuer cures, and a second, lower recovery on the *new* paper if it re-defaults, with Moody's noting that recoveries "tend to decline further" in that case. For participants and non-participants in the same tranche, $R_{\text{DE}}$ is two different random variables, which is why the recovery leg needs a two-component Beta mixture,

$$
f_R(r) = w_{\text{in}}\,\text{Beta}(r; a_{\text{in}}, b_{\text{in}}) + (1 - w_{\text{in}})\,\text{Beta}(r; a_{\text{out}}, b_{\text{out}}),
$$

where $w_{\text{in}}$ is the probability that your tranche ends up inside the deal. For a passive holder of a widely held loan with a permissive credit agreement, $w_{\text{in}}$ is not the share of lenders who participate; it is the probability that *you* are invited, which is a function of your position size, your relationships, and whether you are already in the group. Regime-switching versions, in which the Beta parameters move with a hidden credit-cycle state, follow Bruche and González-Aguado (2010).

> **Trend Watch.** *The distressed exchange became the modal default (2022–2026).* Fitch's 2023 *Annual Manual* reported that distressed debt exchanges "accounted for 45% and 50% of the 2022 defaults in volume and count, respectively." S&P (as cited by FTI Consulting, October 9, 2026) found DDEs at about half of rated US corporate defaults for three consecutive years, against 32% for 2010–2023. Moody's Analytics (*US Credit Review & Outlook*, 7 August 2025) reported that distressed exchanges were 64% of defaults in the first half of 2025, "about the same pace as all of 2024, which itself was the highest annual share on record," and that the June 2025 high-yield issuer default rate of 5.8% fell to 2.1% once 51 distressed restructurings were removed. Moody's (*Lend, Extend, and Then?*, May 18, 2026) put distressed exchanges at about 65% of 2025 corporate defaults and, in a study of 1,173 soft-event borrowers from 1979 to 2026, found that roughly one in four ended in a hard default and that more than 70% of eventual hard defaults came within two years. Moody's September 22, 2026 report (via American Banker) put DEs and LMEs at "roughly 70% of defaults since early 2022," with the default rate at 5.3% in August 2026. What it means for the model: a default probability with no event type attached is now an ambiguous number. The 5.8%-versus-2.1% gap is the difference between two definitions of $q$, and a backtest trained on one and scored on the other will look either brilliant or broken.

> **Docket Diary.** *Rulings that moved recovery distributions.* March 28, 2023: the Serta bankruptcy court (S.D. Tex.) grants summary judgment that the 2020 uptier fell within "open market purchase." December 31, 2024: the Fifth Circuit reverses (125 F.4th 555, revised February 14, 2025), holding that the privately negotiated exchange was not an open market purchase and excising the plan's indemnity for participating lenders. Same day, the New York Appellate Division, First Department, permits the Mitel uptier (*Ocean Trails CLO VII v. MLN Topco*). January 2025: the Wesco/Incora bankruptcy court finds that the 2022 transactions violated the 2026 notes indenture; December 8, 2025: the district court reverses. September 2025: in ConvergeOne, the district court reverses plan confirmation because an exclusive backstop for majority lenders violated §1123(a)(4). July 2026: on remand in Serta, participating lenders are held liable for \$261.13mm plus prejudgment interest, with the excluded loans valued at \$0.25 (Mayer Brown, July 2026). The Ad Hoc Group, through counsel, notes its disappointment. (Cooperation agreements signed in this book so far: 0. Part IV will fix that.)

### 5.6.2 Case Study: Serta Simmons and Hertz, the two ends of the recovery distribution

**Serta Simmons (2020–2026): recovery conditioned on a signature.** In June 2020, a majority group of Serta's first- and second-lien lenders provided about \$200mm of new-money first-out debt and exchanged their existing loans into roughly \$875mm of second-out super-priority debt, leaving the non-participating first-lien lenders subordinated to more than \$1bn of new priming debt (Proskauer, January 2, 2025). Serta filed Chapter 11 in January 2023. The proposed plan offered participating lenders recoveries of 73.7%–100% and non-participating lenders and other unsecured creditors 0.6%–2.4% (Norton Rose Fulbright, Q3 2023). Same original tranche, same collateral, same seniority label: two recovery distributions separated by a factor of thirty or more. In Beta-regression terms (§5.5.3), the participation coefficient swamps everything else in $x_i$, and a model with only seniority and collateral would have assigned both groups the same mean.

What a systematic desk could have flagged *before* June 2020, using the RSSG reader's conditioning set: the credit agreement permitted debt buybacks via "open market purchase" (the most expensive three words in finance) with only majority-lender consent for the relevant amendments; the borrower was sponsor-owned with a single-B-or-lower rating and pandemic-hit revenue; and competing lender groups were reported to be organizing. Each is a feature in the Priming Risk Score of Chapter 13, and together they shift $w_{\text{in}}$ for a small passive holder sharply down. Ines replays the hand through markouts: "The week before the uptier, who was buying the loan, and who was quietly selling it to you? The group that knew it was getting the 73.7 was not selling."

**Hertz (2020–2026): the right tail, where $R > 1$.** Hertz filed in May 2020, and the used-car market and an equity rally then made it a solvent debtor. The plan paid unsecured noteholders in full and delivered about \$1.1bn of value to old equity; the noteholders then litigated for make-whole premiums and post-petition interest at the contract rate. The Third Circuit (2024, 120 F.4th 1181) held that the make-wholes were unmatured interest disallowed under §502(b)(2) but that, because the debtor was solvent, the noteholders were entitled to the premium amounts and contract-rate interest anyway, worth more than a quarter of a billion dollars; the Supreme Court denied certiorari on January 12, 2026 (Nelson Mullins, April 10, 2026). For the model, Hertz is a recovery above par in an unsecured class, driven by a systematic factor, which is why Moody's put family recovery on $[0, 1.2]$ rather than $[0, 1]$ and why the spec allows `support_max > 1`. It is also a reminder that the recovery of an unsecured claim on a cyclical business is a call option on the cycle.

### Deep-Dive Resource Graph

- **Podcasts:** Bloomberg *Odd Lots* episodes on "creditor-on-creditor violence" and liability management (2023–2025; titles to be confirmed); Octus and Petition coverage of the Serta and Mitel rulings.
- **Practitioner Writing:** Moody's, *Lend, Extend, and Then?* (May 18, 2026), https://www.moodys.com/web/en/us/insights/credit-risk/private-credit/lend-extend-and-then.html ; Moody's Analytics, *US Credit Review & Outlook* (7 August 2025), https://www.moodys.com/web/en/us/insights/resources/us-report-july-2025.pdf ; Norton Rose Fulbright, *Liability Management Transactions* (2023), https://www.nortonrosefulbright.com/en-us/knowledge/publications/e245aa48/liability-management-transactions ; Holwell Shuster & Goldberg, *Liability Management Exercises and the Courts in 2025* (December 22, 2025), https://www.hsgllp.com/about-news-Liability-Management-Exercises-and-the-Courts-in-2025 ; Octus, *The Year in LMEs* (January 8, 2026), https://octus.com/resources/articles/the-year-in-lmes/ ; Matt Levine, *Money Stuff* columns on Serta and "open market purchase" (Bloomberg Opinion).
- **Academic Papers:** Bruche and González-Aguado (2010), *Recovery Rates, Default Probabilities, and the Credit Cycle*, Journal of Banking & Finance; Calabrese (2014), *Downturn Loss Given Default: Mixture Distribution Estimation*, European Journal of Operational Research.
- **Data & Code:** CourtListener REST API, https://www.courtlistener.com/help/api/ (dockets for Serta, Wesco/Incora, ConvergeOne); SEC EDGAR, https://www.sec.gov/edgar (credit agreements as 8-K and 10-K exhibits).

## 5.7 Tails: Hill, Peaks-over-Threshold, and Why Single Bonds Have No Power Tail

### 5.7.1 Desk framing: which objects have tails worth estimating

> **[SOURCE EXTRACTION]** *Paleologo_Advanced_Portfolio_Management p.76:* "Factor returns are heavier-tailed than the norm."
>
> **Annotation.** Paleologo shows this with a momentum factor's quantile plot, whose left tail sits well below the Gaussian line. The sentence is the reason extreme-value theory belongs in a credit risk stack: factor returns, index returns, ETF returns, and spread *changes* are unbounded or nearly so, and their tails are heavier than normal in a way that a power law describes well. The credit-specific departure is what the sentence does *not* cover: a single bond's loss is bounded by $1 - R_{\min}/P_0 \le 1$, and a bounded variable has no power tail. Applying EVT to one bond is like fitting a Pareto distribution to the number of floors in a building.

### 5.7.2 Hill and peaks-over-threshold

Sort losses $X_{(1)} \ge X_{(2)} \ge \dots \ge X_{(n)}$. If the tail is Pareto, $\Pr(X > x) \sim C x^{-\alpha}$, the Hill (1975) estimator of the tail index from the top $k$ order statistics is

$$
\hat{\alpha}_k = \left[\frac{1}{k}\sum_{i=1}^{k} \ln\frac{X_{(i)}}{X_{(k+1)}}\right]^{-1}, \qquad \hat{\xi}_k = 1/\hat{\alpha}_k.
$$

Peaks-over-threshold fits a generalized Pareto distribution (GPD) with shape $\xi$ and scale $\beta_{\text{GPD}}$ to the $N_u$ exceedances over a threshold $u$, giving (for $\xi < 1$, $\xi \ne 0$)

$$
\text{VaR}_p = u + \frac{\beta_{\text{GPD}}}{\xi}\left[\left(\frac{n}{N_u}(1-p)\right)^{-\xi} - 1\right], \qquad \text{ES}_p = \frac{\text{VaR}_p}{1-\xi} + \frac{\beta_{\text{GPD}} - \xi u}{1-\xi}.
$$

(The subscript on $\beta_{\text{GPD}}$ keeps it apart from factor loadings.) It is called a Hill plot because you climb it, look around, and still cannot see the threshold: $\hat{\alpha}_k$ is plotted against $k$, and you look for a plateau, which in real data is a matter of faith.

### 5.7.3 The bounded-support trap

Extreme-value theory (Fisher–Tippett–Gnedenko for maxima, and its threshold counterpart Pickands–Balkema–de Haan, which is what justifies the GPD) sorts distributions into three domains by $\xi$: Fréchet ($\xi > 0$, power tail), Gumbel ($\xi = 0$, exponential-type tails), and Weibull ($\xi < 0$, bounded support). A single bond's loss is bounded, so it is in the Weibull domain. Run Hill on it and $\hat{\alpha}_k$ drifts with $k$: for small $k$ it is measuring the spread of recoveries within the default lump; for $k$ near $nq$ it is measuring the gap between the lump and the survival world. Neither is a tail index. The spec in §5.9 makes `hill_estimator` refuse, with a warning, when the sample maximum sits at the support bound.

### 5.7.4 Diversification eats skew, correlation feeds it back

For the average return of $N$ independent, identical bonds, cumulants add, so

$$
\text{skew}(\bar{R}) = \frac{\text{skew}(R)}{\sqrt{N}}, \qquad \text{exkurt}(\bar{R}) = \frac{\text{exkurt}(R)}{N}.
$$

A single bond with skew $-10$ becomes a 1,000-name portfolio with skew $-0.32$. Correlation stops the decay: with a common factor (§5.5.4), conditional on $Z_t$ the names are independent, but $Z_t$ itself moves every default probability and every recovery at once, so the portfolio inherits the skew of the *mixture over* $Z_t$. Bolder's verdict on threshold models makes the point.

> **[SOURCE EXTRACTION]** *Bolder_Credit_Risk_Modelling p.222:* "even in the case of a Gaussian joint distribution for the risk factor, the loss distribution is no longer Gaussian. In fact, it is highly skewed and heavily fat-tailed."
>
> **Annotation.** Bolder shows that a Gaussian copula with modest correlation already produces a strongly skewed, fat-tailed portfolio default-loss distribution; the Gaussian factor is not the Gaussian outcome. The desk lesson: portfolio loss tails are where EVT and copula choice belong, and Bolder's further point (p.227) is that only a power-tailed mixing variable, such as the $t$-copula's, produces *tail dependence*. For a $t$-copula with correlation $\rho$ and $\nu$ degrees of freedom, the coefficient of tail dependence is $\lambda_U = 2\,t_{\nu+1}\!\left(-\sqrt{(\nu+1)(1-\rho)/(1+\rho)}\right)$, where $t_{\nu+1}$ is the Student-$t$ distribution function (and $\lambda_U$ is a tail-dependence coefficient, not an intensity; the subscript marks it). For the Gaussian copula it is zero. The departure: in 2026 the cluster that matters is often the sponsor or the lender group rather than the industry, so the dependence structure should be specified on those graphs (Chapter 14).

The FRED data agree with the algebra. Using daily ICE BofA total-return indices from October 17, 2023 to October 15, 2026 (series BAMLHYH0A0HYM2TRIV, BAMLHYH0A3CMTRIV, BAMLHYH0A1BBTRIV; *author's computation from FRED data*), the High Yield index had daily skewness of about $+0.1$ and excess kurtosis of about 7.3; the CCC & Lower index had skewness of $-0.5$ (weekly $-0.9$) and excess kurtosis of 9.4. All three indices had their worst day of the window on April 4, 2025 (HY $-1.2\%$, CCC $-2.1\%$). The index is nearly symmetric because diversification ate the single-name skew; it is still fat-tailed because common shocks, such as the April 2025 tariff week, hit everything at once. The CCC index keeps its negative skew because its constituents' default probabilities are high and correlated. That is the object on which Hill and GPD earn their fee.

> **Ways This Blows Up.** *Fake thin tails and fake fat ones.* (1) Stale evaluated prices smooth returns, thinning the empirical tail and inflating autocorrelation; estimate tails on traded indices, CDX, or ETFs, not on marks. (2) Volatility clustering inflates kurtosis: de-GARCH first and run Hill on standardized residuals, or you are estimating the tail of the volatility regime, not of the shock. (3) Thresholds chosen after looking at the answer: fix $k$ or $u$ by rule (for example, the top 5% of observations) in the spec, and report sensitivity, not a single number.

### Deep-Dive Resource Graph

- **Podcasts:** *Flirting with Models* episodes on tail hedging and crisis alpha (titles to be confirmed).
- **Practitioner Writing:** Paleologo, *Advanced Portfolio Management* (Wiley), factor return tails (shelf: Paleologo_Advanced_Portfolio_Management p.76); Bolder, *Credit-Risk Modelling* (Springer), threshold models and tail dependence (shelf: Bolder_Credit_Risk_Modelling p.222, p.227, p.229).
- **Academic Papers:** Hill (1975), *A Simple General Approach to Inference About the Tail of a Distribution*, Annals of Statistics; McNeil, Frey, and Embrechts (2015), *Quantitative Risk Management*, 2nd ed., Princeton University Press; Embrechts, Klüppelberg, and Mikosch (1997), *Modelling Extremal Events*, Springer.
- **Data & Code:** FRED ICE BofA total-return series (search the series IDs above at https://fred.stlouisfed.org/); `hill_estimator`, `gpd_var_es`, and `t_copula_tail_dep` in §5.9.

## 5.8 Choosing the Shape: Five Objects, Five Distributions

By the end of the week Theo has stopped asking for "the distribution" and started asking "the distribution of *what*?", which Ines says is the first question a good player asks about any pot. The chapter's results fit on one table, and the table is the router that the §5.9 code implements.

| Object | Support | Model that earns its keep | What it replaces | Tail tool | Measure |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Single-bond horizon return (§5.1, §5.6) | Bounded below by $-1$, capped above by the call | Survive-or-jump mixture: DTS survival leg, inflated-Beta recovery leg, categorical events (HD, DE) for LMT-exposed names | Gaussian with trailing vol | ES and JTD; no Hill | $\mathbb{P}$ |
| Single-bond horizon price (§5.2) | $[0, K_{\text{call}}]$ | Capped survival price plus a recovery lump | Lognormal price | None needed: the bounds are the tails | $\mathbb{P}$ |
| Spread change (§5.2–5.3) | Unbounded above in practice | Lognormal-ish relative changes (DTS); jump-diffusion at the short end | Gaussian basis-point changes | Hill or GPD on de-GARCHed relative changes | $\mathbb{P}$ for risk, $\mathbb{Q}$ for pricing |
| Recovery (§5.5–5.6) | $[0, 1]$, or $[0, 1.2]$ when post-petition interest is in play | Zero-one-inflated Beta regression; Beta mixture by participation status | Constant 40% | Not applicable: it *is* the tail | $\mathbb{P}$ (ultimate) or $\mathbb{Q}$ (trading price), never pooled |
| Index, ETF, or portfolio return (§5.4, §5.7) | Bounded only at 100% of the book, far beyond any quantile you will estimate | Factor or $t$-copula mixture of the single-name mixtures; VG or NIG for daily index and option data | Gaussian copula with Gaussian margins | GPD peaks-over-threshold; $t$-copula tail dependence | $\mathbb{P}$ |

Three questions route every request. *What object?* A price, a spread, a return, a recovery, or a book. *What support?* If the sample maximum sits on a bound, the tail is a lump, not a power law. *Which measure?* If the inputs came off a CDS curve they are $\mathbb{Q}$ quantities, and the risk report has just been handed the market's fear instead of its forecast. Kaz notes, with some dignity, that the Gaussian survives in exactly one cell, as the survival leg of row one, which is where it belonged all along. It was not fired. It was demoted to a component.

Mags reads the table twice. "Back in my day we had one distribution for everything. You called the other desk, asked what they'd pay, and the tails were whatever they said after lunch." She taps the recovery row. "That participation column, though. We'd have paid real money for that column."

## 5.9 The Credit Mixture Lab: A Reference Implementation

Every function this chapter has promised lives here, in one file, in the order the chapter introduced the ideas. The spec is written for ROBO, which means it is written for the most literal reader in the building. Ines's rule for a spec is the poker rule: name the pot (the object and its units), the odds (the measure), and the opponent (the edge case that will take your money).

> **What ROBO built from the vague version.** Asked to "fit a Beta to our recoveries," ROBO wrote a Beta log-likelihood, met $\ln 0 = -\infty$ at the recoveries that were exactly zero, propagated NaN gradients through the optimizer, and returned $(a, b) = (\text{nan}, \text{nan})$ with the message "optimization terminated successfully." Asked to "estimate the tail index of the book's bonds," it ran Hill on single-bond losses, got $\hat{\alpha}$ well above 100 at $k = 1{,}000$ and between 3 and 4 at $k = 20{,}000$, averaged them, and reported that high yield is thin-tailed. Both answers are exactly what was asked for. Neither is what was meant.

### 5.9.1 One last derivation: exact moments of the DTS survival leg

Section 5.1.4 handed the survival leg a Gaussian with Theo's 4.1%. The code should build it from the bond instead. Let $\Delta s \sim N(0, v)$ with $v = \kappa^2 s^2 h$ (the DTS scaling of §5.1.2), and write $c = \tfrac{1}{2}C^{\text{spr}}$ and $x_0 = s\,h + \text{roll}$, so that

$$
X = x_0 - D^{\text{spr}}\,\Delta s + c\,(\Delta s)^2.
$$

Put $W = (\Delta s)^2 - v$. Then $\mathbb{E}[X] = x_0 + c\,v$ and $X - \mathbb{E}[X] = -D^{\text{spr}}\Delta s + c\,W$. Every term carrying an odd power of $\Delta s$ has zero expectation. The variable $W/v$ is a centered $\chi^2_1$, whose second, third, and fourth central moments are 2, 8, and 60, and the Gaussian moments $\mathbb{E}[(\Delta s)^4] = 3v^2$ and $\mathbb{E}[(\Delta s)^6] = 15v^3$ give $\mathbb{E}[(\Delta s)^2 W] = 2v^2$ and $\mathbb{E}[(\Delta s)^2 W^2] = 10v^3$. Expanding the binomials and keeping the even terms:

$$
\sigma_X^2 = (D^{\text{spr}})^2\,v + 2c^2v^2,
$$

$$
\mu_{3,X} = 6\,(D^{\text{spr}})^2\,c\,v^2 + 8c^3v^3,
$$

$$
\mu_{4,X} = 3\,(D^{\text{spr}})^4\,v^2 + 60\,(D^{\text{spr}})^2 c^2 v^3 + 60\,c^4 v^4.
$$

At $c = 0$ these are the Gaussian's moments, as they must be. The sign of $\mu_{3,X}$ is the sign of the convexity. A callable high-yield bond trading near its call has negative spread convexity, so its survival leg is *already* left-skewed before anyone defaults: the issuer's call takes the rallies and leaves you the sell-offs. Negative convexity also lowers the mean by $|c|\,v$, a convexity tax collected whether spreads go up or down. That is the §5.2 cap, now in a formula. (The code's $C^{\text{spr}} = -8$ is an *illustrative* near-the-call value, in decimal-spread units per unit of price, not a calibration.)

### Specification for AI Implementation

**Module.** `credit_mixture_lab.py`; numpy, scipy, and pandas only; every random draw flows from `numpy.random.default_rng(seed)`; the five blocks below run in order in one interpreter, and each ends in seeded asserts.

**Schemas.**

- `RecoverySpec` (frozen dataclass): `a, b > 0`; `pi0, pi1 >= 0` with `pi0 + pi1 < 1` (masses at exactly zero and exactly par); `support_max` in $[1.0, 1.5]$ (a Moody's-style 1.2 is allowed for Hertz-type outcomes, §5.6.2); `convention` in `{RFV, RMV, RT}`, named, never implied.
- Bond inputs to `mixture_moments`: `q`, the **physical** horizon default probability; `price0`, the full price per 1.0 of par, in $(0, 1.5]$; and the survival leg as a 4-tuple `(mean, var, mu3, mu4)` from `gaussian_moments` or `survival_moments_dts(spread, h, spr_dur, spr_conv, kappa, roll)`, with spread in decimal and horizon in years.
- `RecoveryPanel` (pandas): `issuer_id, instrument_id, default_date, seniority, collateral_cov, debt_cushion` (in $[0,1]$), `loan_only, cov_lite, sponsor, prior_lmt, participant` (`in`, `out`, `na`), `industry_distress, trailing_dr, rec_trading_30d, rec_ultimate_disc`. Categorical fields are dummy-encoded before fitting (`first_lien`, `participant_out`, and so on). The two recovery columns live under different measures (§5.5.6); `fit_beta_regression` takes exactly one of them as `target` and refuses anything else.

**Shapes.** Simulations return `(n,)` float64 arrays and `(n,)` boolean flags; copula draws are `(n, 2)`; regression fits return `pandas.Series` of coefficients and standard errors indexed by covariate name.

**Guards.** The Beta method of moments raises when $\sigma^2 \ge \mu(1-\mu)$; the plain Beta regression raises on exact zeros or ones; the Kou simulator raises unless $\eta_1 > 1$; `hill_estimator` returns NaN with a warning when the sample maximum sits at a declared support bound; `gpd_var_es` raises when $\hat{\xi} \ge 1$ (infinite ES) or when there are fewer than 50 exceedances. Monte Carlo used to *test* the closed form is stratified on $D$; Monte Carlo used for *risk* must draw $D$ (see Ways This Blows Up below).

Block 1 is §5.1 and §5.2 in code: the recovery spec, the closed-form mixture moments, a Monte Carlo that reproduces them, the table in §5.1.4, and the capped horizon value.

Section 5.1.4 was done by hand, and it shows. Every number in the table came from a formula in §5.1.2 and a calculator, which is how Theo's fourteen-sigma Tuesday got priced exactly once, for one bond, at one default probability. The desk's problem is that inputs move every morning: the price drifts, research revises $q$, the survival leg's volatility comes off a fresh DTS fit, and a risk committee member asks why the 99% expected shortfall differs from yesterday's. A table nobody can regenerate is a table nobody believes. So the formulas get written down once, in a form that refuses nonsense, and a simulation that shares none of the algebra stands next to them and has to agree.

The listing builds the table in four layers. First, the recovery. `RecoverySpec` is a frozen dataclass, the code equivalent of an executed credit agreement, and its constructor rejects non-positive Beta parameters, inflation masses that sum to one or more, a `support_max` outside 1.0 to 1.5, and any convention other than RFV, RMV or RT, so a recovery never travels without naming its measure. `beta_mom` backs a Beta out of a mean and standard deviation after rescaling by `support_max`, and refuses when the variance reaches the Bernoulli bound $\mu(1-\mu)$, because those moments describe a coin, not a Beta. `recovery_moments` returns the exact mean, variance, and third and fourth central moments of the inflated, rescaled recovery.

Second, the survival leg arrives as a four-tuple of moments, from `gaussian_moments` for Theo's version or `survival_moments_dts` for the callable of §5.9.1. Third, `mixture_moments` converts recovery into return space (recovery over price, minus one), measures the jump $J$ between the two worlds' mean returns, and applies the §5.1.2 formulas to give the mean, volatility, skewness and excess kurtosis in closed form. Fourth, the witness: `simulate_mixture` draws the survival returns and the recoveries separately, fixes the number of defaults at exactly `round(q*n)`, and returns the returns with their default flags. `var_es` reads the lower tail, and `horizon_value` turns returns into value per 1.0 of par, where a default pays exactly the recovery and a call caps the clean price but not the coupons already collected.

The asserts do the arguing. The closed form must reproduce the §5.1.4 table, collapse to the survival leg at $q = 0$ and to the Beta's own skewness at $q = 1$, and match the textbook Bernoulli skew and kurtosis when both legs are pinned to points. The simulation must then agree to within a few percent.

Use it for the horizon distribution of one bond. Do not use it as a portfolio engine: one Bernoulli has no common factor, and it knows nothing of distressed exchanges until §5.6 widens the categories. The edge case that bites is `q`. The function accepts any probability and cannot tell a physical default probability from a risk-neutral one backed out of spreads. Feed it the latter and the risk premium already sitting in the survival leg's carry is taxed a second time, producing a beautifully consistent distribution of someone else's problem.

*The full listing is [Listing 5.1 in Appendix F](#code-5-1).*

The VaR and ES checks deserve a sentence. With $q = 4\%$, the 1% quantile of the mixture is the 25% quantile of the recovery lump, so the 99% VaR is $F_R^{-1}(0.25)/P_0 - 1$ and the 99% ES uses the Beta identity $\mathbb{E}[R\,\mathbf{1}\{R \le r\}] = \tfrac{a}{a+b}\,I_r(a+1, b)$, where $I_r$ is the regularized incomplete Beta function. Those two lines reproduce the $-83\%$ and $-92\%$ in the §5.1.4 table without a single simulated path, and the simulation agrees.

Block 2 is §5.5 in code. The zero-one-inflated likelihood factorizes into a multinomial logit for the masses and a Beta regression on the interior observations, because the two pieces share no parameters, so each is fitted on its own with an analytic gradient and a numerical Hessian for standard errors.

Section 5.5.3 ended on a promise: let the Beta's mean read the name tag on the loan. Promises are cheap on a whiteboard. On a desk the same promise means a panel of a few thousand defaulted instruments, a handful of covariates, and two likelihoods that generic regression software handles badly: a Beta with a logit mean, and a three-way split among exact zeros, exact pars and everything in between. It also means a model-review meeting at which someone asks why the participation coefficient moved since last quarter, and "the spreadsheet trendline changed" is not an answer. So the fit is automated, returns a standard error with every coefficient, and refuses the inputs that would make those standard errors meaningless.

The listing fits the two pieces of the zero-one-inflated Beta separately, which the factorization above allows. `_beta_nll` is the Beta part, with a logit mean and a log precision as in Ferrari and Cribari-Neto. It returns the negative log-likelihood together with its analytic gradient, built from digamma functions. A log-scale precision stays positive without constraints. `_mnl_nll` is the mass part: a multinomial logit over interior, exact zero and exact par, with the interior class as the base, so each covariate carries two coefficients. `_mle` hands either one to BFGS with the gradient, warns rather than raises if the optimizer does not report success, and takes the inverse of a symmetrized central-difference Hessian of the analytic gradient as the covariance matrix.

`fit_beta_regression` is the front door, and most of it is refusal. The `target` must be one of the two named recovery columns, ultimate discounted or 30-day trading, never a bare "recovery"; a recovery column cannot double as a covariate; rows with a missing target are dropped; fewer than twenty observations per coefficient stops the fit; recoveries must already sit in $[0,1]$; and with `inflate=True` it wants at least five exact zeros and five exact pars. The Beta part sees interior rows only. The output is a dictionary of pandas Series: `mass` and `mass_se` indexed by `zero:` and `one:` plus covariate names, and `beta` and `beta_se` ending in `log_phi`.

The check plants known coefficients in a synthetic panel of 6,000 defaults, fits them back, confirms that out-of-deal lenders recover less and are likelier to get nothing, and confirms that both bad targets are refused. Two details of the test come right after the code.

Use it on a defaults panel with enough exact zeros and pars to identify the masses; do not use it on thin data or to blend measures. The edge case that bites is independence. The standard errors treat every row as its own draw. The synthetic panel carries an `issuer_id` but draws outcomes independently, so the check passes; in a real panel several instruments of one issuer share a bankruptcy, a judge and a plan, their recoveries move together, and the standard errors come out too small. The participation coefficient will look braver than it is until the errors are clustered by issuer, which this listing does not do.

*The full listing is [Listing 5.2 in Appendix F](#code-5-2).*

Two details are deliberate. The tolerance is four standard errors, not two: with sixteen coefficients under test, a two-standard-error band would fail on roughly half of all seeds through no fault of the code, which is Chapter 7's multiple-testing lesson applied to a unit test. And the test's `eps=1e-9` keeps genuine Beta draws near zero from being misfiled as exact zeros; on real data, recoveries are reported to a tenth of a point or so, and `eps` should match that rounding.

Block 3 is §5.3 in code: a first-passage simulator for Kou's model, checked against both closed-form results.

Section 5.3.3 produced two closed forms: a jump-to-default intensity that gives a one-week CCC bond a spread above zero, and an expected undershoot that ties recovery to the same parameter that drives default. Closed forms are lovely until someone asks a question they do not cover. What is the one-year default probability under a fatter downward-jump parameter? What does the joint distribution of default time and recovery look like? How many names cross the barrier, and how far below it do they land? A desk answers those by simulation, and a simulation that has never been checked against the results we already know is how a bug becomes a position. So the model gets a path simulator, and the first job of the simulator is to reproduce the two formulas.

`kou_jump_sizes` draws the log-jumps: upward with probability $p$ and an exponential size with mean $1/\eta_1$, otherwise downward with mean $1/\eta_2$. `simulate_kou_jd` tracks $x = \ln(V/B)$, the log-distance to the barrier, for `n` firms over `n_steps` steps, and a firm defaults the first time $x \le 0$. Each step has two moves, in order. First the diffusion: a Gaussian increment with drift $\mu - \tfrac12\sigma^2 - \lambda\zeta$, where $\zeta = \mathbb{E}[e^Y] - 1$ is the compensator that keeps the asset's expected growth at $\mu$ despite the jumps. Paths at or below zero are logged as diffusive defaults with `ratio` set to 1.0. Then the survivors draw a Poisson number of jumps, the sizes are summed per path, and any path now at or below zero is a jump default, flagged in `via_jump`, with `ratio` equal to $e^{x}$, the asset value over the barrier at the moment of default. That is the undershoot of §5.3.3, the recovery proxy. The function returns flags, default times (infinity for survivors) and ratios, and refuses a start at or under the barrier or an $\eta_1 \le 1$, which would make $\mathbb{E}[e^Y]$ infinite.

Sanity check 3 asks three questions of a one-week, four-step run. Does the default rate, annualized, land within 10% of the 5.9% intensity formula? Are at least 99% of defaults jump-driven, as they must be when the barrier is a dozen diffusive standard deviations away? Does the mean undershoot sit within 0.025 of $\eta_2/(1+\eta_2) = 0.8$? Then it runs a year at $\eta_2 = 4$ and again at $\eta_2 = 2$ and requires the fatter-jump world to show more defaults and lower undershoot: the PD-LGD correlation from one parameter, as an assert.

Use it for a physical-measure risk run on a single issuer, when you need the joint draw of default time and recovery. Do not use it to price spreads, whose drift and intensity are risk-neutral, or as a book simulator, since one firm has no common factor. The edge case that bites is the `ratio` array. It is `nan` for survivors, so a plain mean over all paths returns `nan`, and it is 1.0 for diffusive hits, so a mean over all defaulters blends two different recovery stories. Slice by `via_jump`, as the check does. Because the barrier is checked only twice per step, dips between steps go unseen; that bias is the second item in the box below.

*The full listing is [Listing 5.3 in Appendix F](#code-5-3).*

Block 4 is §5.7 in code. The Hill estimator gets a refusal mode, and the test runs it twice: once on Student-$t$ draws with $\alpha = 3$, where it should find three, and once on Theo's bond, where it should refuse and, if forced, drift.

The tail argument of this chapter has two halves, and the code has to honor both. Where a tail is real (an index return, a spread change, the residuals of a factor model), Hill and peaks-over-threshold are the right tools, and a desk wants them as functions it can run nightly on any series. Where a tail is a wall (one bond's loss, capped at 100% of price), the same functions will cheerfully return a number, because an estimator has no way to know it is being asked a question with no answer. Ines would call that a player who cannot fold. So the Hill estimator is written to fold.

`hill_estimator` sorts the losses from largest to smallest, keeps only the positive ones, and returns the reciprocal of the average log-ratio of the top `k` losses to the $(k+1)$th, which is the formula of §5.7.2. Before it computes anything it asks whether the caller declared a `support_max` and whether the largest loss sits within `tol` of it; if so it warns and returns NaN, because a sample that piles up against its ceiling holds a lump, not a power law. `hill_table` runs the estimator across a list of `k` values and returns a pandas Series, which is the Hill plot with the plotting taken out.

`gpd_var_es` is peaks-over-threshold. It takes the exceedances over `u`, insists on at least 50, fits a generalized Pareto with the location pinned at zero, and raises if the fitted shape $\hat{\xi}$ reaches 1, where expected shortfall is infinite. It converts the confidence level into a tail probability using the empirical exceedance rate, so it wants the whole loss sample, gains included; trimming to positive losses first would overstate that rate. It returns VaR and ES as losses, switching to the exponential-tail limit when $\hat{\xi}$ is essentially zero.

The first half of the check shows the machinery working on a genuine power tail. On half a million Student-$t$ draws with three degrees of freedom, Hill lands between 2.5 and 3.5 at three choices of `k`, the fitted shape sits between 0.2 and 0.5 (the truth is one third), and the 99.9% VaR and ES match the exact $t$ values to within 10% and 15%.

Use it on indices, spread changes and factor residuals, and use the table of `k` values rather than a single one. The edge case that bites is that the refusal is opt-in. `support_max` defaults to `None`, which switches the guard off, and the guard fires only when the sample maximum actually reaches the bound. A caller who forgets to declare the cap gets a confident-looking number from a bond's loss, and a bounded variable that has not yet touched its ceiling passes the test.

*The full listing is [Listing 5.4 in Appendix F](#code-5-4).*

The drift is the vague-version ROBO result reproduced on purpose. At $k = 1{,}000$ the top losses are all near-zero recoveries piled against the 100% cap, the log-spacings are tiny, and $\hat{\alpha}$ is enormous; at $k = 20{,}000$ the order statistics span the whole recovery lump and $\hat{\alpha}$ falls to single digits. There is no Hill, only a cliff at $1 - R/P_0$, which is the joke in §5.7 with an assert attached.

Block 5 is the copula check from §5.7.4, with one subtlety that the naive version of the test gets wrong, flagged in the box after the code.

Section 5.7.4 made a claim that every credit desk repeats and few verify: the Gaussian copula has no tail dependence, the $t$ copula has plenty, and that is why the same book of correlated names looks calm under one and alarming under the other. A claim that decides the shape of a portfolio loss distribution deserves a test it cannot pass by accident. A reviewer who asks whether the dependence module really clusters defaults should get a number, not a nod. The test has two jobs: evaluate the closed form for $\lambda_U$, and simulate both copulas to see what a finite sample makes of it.

`t_copula_tail_dep` evaluates the coefficient from §5.7.4, twice the Student-$t$ distribution function with $\nu + 1$ degrees of freedom at $-\sqrt{(\nu+1)(1-\rho)/(1+\rho)}$, after checking that $\rho$ lies strictly between $-1$ and 1 and that $\nu$ is positive. `simulate_copula_pairs` builds the dependence the way the theory describes it. A Cholesky factor of the two-by-two correlation matrix turns independent normals into a correlated Gaussian pair, and for finite $\nu$ each pair is multiplied by $\sqrt{\nu/\chi^2_\nu}$, one chi-square draw per row, shared by both coordinates. That shared scale is the whole mechanism: a small chi-square shocks both names at once, so extremes arrive together. Passing `nu=np.inf` skips the scaling and returns the Gaussian. The draws are latent variables rather than uniforms, which is harmless because `conditional_exceedance` works with empirical quantiles within each column. It computes $\hat{\chi}$ at a given level: among the rows where the first coordinate is above its own quantile, the fraction in which the second is above its own.

Sanity check 5 sets $\rho = 0.5$. It requires the $t$ copula with four degrees of freedom to land between 0.2 and 0.3, and the nearly Gaussian case with $\nu = 10{,}000$ to fall below one in a million. Then, with two million pairs per copula, it measures $\hat{\chi}$ at the 99.9th percentile and requires the $t$ estimate to sit within 0.08 of theory and the Gaussian estimate to be positive but at least 0.08 below the $t$. That positive Gaussian number is the subtlety the box below takes apart.

Use it to confirm that a dependence module does what its documentation says before its output reaches a capital or sizing conversation; do not use it to estimate tail dependence from data. The edge case that bites is sample size. At level 0.999 the estimator conditions on about one row in a thousand, which leaves roughly two thousand rows from two million draws, a comfortable sample. Three years of daily data are about 750 rows and leave exactly one, so the function returns exactly 0 or exactly 1. Neither is evidence of anything.

*The full listing is [Listing 5.5 in Appendix F](#code-5-5).*

> **Ways This Blows Up.** *Three ways the lab lies to you.* (1) *The stratified sampler is a test fixture, not a risk engine.* Fixing the default count at exactly $qn$ removes binomial noise so the closed form can be checked to 2%; in a risk run it also removes the scenario in which more names default than expected, which is the scenario you are paying for. Production simulation draws $D$, and for a book it draws $D$ conditional on the common factor $Z_t$ of §5.5.4. (2) *Discrete monitoring misses diffusive defaults.* Checking the barrier once a step lets paths dip below and recover unseen, which biases the default probability down. Conditional on log-distances $x_t > 0$ and $x_{t+\Delta t} > 0$, the probability that the diffusion touched the barrier in between is $\exp\!\left(-2x_t\,x_{t+\Delta t}/(\sigma^2\Delta t)\right)$ (the Brownian-bridge correction); draw a uniform against it each step. The one-week test above does not need it, because the barrier sits about twelve diffusive standard deviations away; a one-year run with weekly steps does. (3) *Finite-level exceedance is not tail dependence.* The Gaussian copula has $\lambda_U = 0$, yet at the 99.9th percentile with $\rho = 0.5$ its conditional exceedance rate is still several percent, and sanity check 5 prints it. Zero is a limit, approached slowly. A desk that "verifies" tail independence from a few years of daily data has verified nothing, and a desk that reads any positive $\hat{\chi}$ as proof of a $t$-copula has made the opposite mistake.

### Deep-Dive Resource Graph

- **Podcasts:** *Flirting with Models* (Corey Hoffstein), episodes on systematic credit and tail risk (titles to be confirmed).
- **Practitioner Writing:** Li, Zhang, and Zhao (2018), *Modeling Loss Given Default*, FDIC Center for Financial Research Working Paper 2018-03, https://www.fdic.gov/analysis/cfr/working-papers/2018/cfr-wp2018-03.pdf ; Bohn and Stein, *Active Credit Portfolio Management in Practice* (Wiley), LGD modeling (shelf: Bohn_Stein_Active_Credit_Portfolio_Management p.313–316).
- **Academic Papers:** Ferrari and Cribari-Neto (2004), *Beta Regression for Modelling Rates and Proportions*, Journal of Applied Statistics; Ospina and Ferrari (2010), *Inflated Beta Distributions*, Statistical Papers; Kou (2002), *A Jump-Diffusion Model for Option Pricing*, Management Science; Kou and Wang (2003), on first-passage times of a double-exponential jump-diffusion; Hill (1975), Annals of Statistics.
- **Data & Code:** `credit_mixture_lab.py` (this section); SciPy's `stats.genpareto`, `stats.beta`, and `special.digamma` for the fits; numpy's `default_rng` for every draw.

## 5.10 Desk Debrief

On Monday Theo reissues the risk report. It is still one page. It now has two columns, *survival world* and *default world*, and a coin between them labeled $q = 4\%$ ($\mathbb{P}$, from the 13-week model, lender case). Kaz's Gaussian sits in the left column with a footnote explaining that it describes the bond on the days nothing happens. The bottom line reads: 99% expected shortfall $-92\%$; jump-to-default 52 points per 100 of par.

Mags reads the bottom line, says "Ninety-two. That's about what I'd have guessed by phone," and goes back to her screen, which is how Mags says *good*. Ines turns the heat map face up again. "Now it's a hand," she says. "Pot, odds, river. Hand history Friday." ROBO receives the spec and, for once, has no questions.

- **A high-yield return is two worlds and a coin.** $R_h = (1-D)X + DY$. The between-world term $q(1-q)J^2$ is most of the variance, and trailing price volatility measures only the world in which nothing happens.
- **Skew is minus one over root PD.** Excess kurtosis is about $1/q$. The safer the bond, the stranger its shape; investment-grade books look normal because they are big, not because their bonds are.
- **95% VaR is blind whenever $q < 5\%$.** Report expected shortfall and jump-to-default, $P_0 - \mathbb{E}[R]$ per unit of par, next to any VaR, or the risk report is a speedometer that only works below the speed limit.
- **Keep three ledgers.** Price lives on $[0, K_{\text{call}}]$, spread changes are right-skewed and DTS-scaled, and returns are left-skewed. Negative convexity skews a callable's survival leg left before anyone defaults.
- **Jumps earn their keep at the short end.** Kou's model gives a non-zero short spread, $\lambda^{\mathbb{Q}}L^{\mathbb{Q}}$, and PD–LGD correlation from a single parameter. Infinite-activity Lévy fits to single-name high-yield bonds are decoration.
- **Recovery is a U, not a bell, and 40% is a convention.** Fit a zero-one-inflated Beta regression on the covariates the RSSG seat knows cold. Participation status carries the biggest coefficient. Never pool trading-price and ultimate recoveries in one fit.
- **Default is a menu now.** Hard default, distressed exchange, and re-default are separate mixture components with separate recovery distributions, and $w_{\text{in}}$ is the probability that *you* get the call, not the share of lenders who do.
- **EVT belongs to unbounded objects.** Run Hill and GPD on spread changes, indices, ETFs, and books. On a single bond the sample maximum sits at the cap, and the "tail index" is the jump mass.

### The Spec You Hand the Robot

This is the version that fits in a prompt. Everything in it is defined in §5.9; the point of the compact form is that every noun has a unit, every probability has a measure, and every edge case has an instruction.

```text
TASK: build credit_mixture_lab.py (numpy, scipy, pandas; all randomness via numpy.random.default_rng(seed)).
OBJECT: horizon-h excess return of one high-yield bond, per 1.0 of par, under the PHYSICAL measure P.
MODEL: R_h = (1 - D) * X + D * Y, with D ~ Bernoulli(q) and q = 1 - S_P(h).
  - q must be physical (from a hazard model or the 13-week cash model); refuse inputs tagged as CDS-implied.
  - X = s*h + roll - D_spr*ds + 0.5*C_spr*ds^2, ds ~ N(0, (kappa*s)^2 * h); use exact moments incl. convexity.
  - Y = R / price0 - 1 (price basis, NOT 1 - R). R is zero-one-inflated Beta on [0, support_max];
    name the recovery convention (RFV, RMV or RT).
OUTPUTS: mean, vol, skew, excess kurtosis (closed form AND Monte Carlo); 99% VaR and 99% ES; JTD = price0 - E[R].
RECOVERY FITS: zero-one-inflated Beta regression, logit mean, log precision, multinomial logit for the masses.
  target is exactly one of {rec_ultimate_disc, rec_trading_30d}; refuse anything else; never pool them.
  covariates: seniority, collateral coverage, debt cushion, loan-only, cov-lite, sponsor, prior LMT,
  participation status, industry distress, trailing default rate.
TAILS: Hill and GPD only on unbounded objects (spread changes, index or ETF returns, portfolio losses).
  If the sample maximum sits at a declared support bound, return NaN and warn.
DEPENDENCE: report the t-copula lambda_U; never infer tail independence from a finite-level exceedance rate.
TESTS (seeded asserts): closed form vs Monte Carlo (vol and skew within 2%, kurtosis within 5%);
  q = 0 and q = 1 limits; Bernoulli skeleton skew = -(1 - 2q) / sqrt(q(1 - q));
  Beta-regression parameter recovery within 4 standard errors; Kou short-maturity default rate within 10%
  of lam * (1 - p) * (B / V)^eta2 and mean V_tau/B within 0.025 of eta2 / (1 + eta2);
  Hill on t(3) draws in [2.5, 3.5]; t-copula exceedance above the Gaussian's.
NEVER: use trailing price volatility as total risk; report 95% VaR alone when q < 5%; minimize kurtosis.
```

### Exercises

1. **Two bonds, one VaR.** A BB name has a physical one-year default probability of 0.8%; a CCC name has 12%. (a) Compute the Bernoulli-skeleton skew and excess kurtosis of each. (Check: about $-11.0$ and $120$ for the BB; about $-2.34$ and $3.5$ for the CCC.) (b) For each bond, say whether a 95% VaR ever sees the default world. (c) A kurtosis screen ranks the CCC as the "safer" bond. Explain in one sentence what the screen is actually measuring.

2. **The convexity tax.** Using §5.9.1 with $s = 550$ bp, $\kappa = 0.35$, $h = 1$, $D^{\text{spr}} = 3.5$, and $C^{\text{spr}} = -8$, compute $\sigma_X$, the survival-leg skew, and the convexity tax $|c|\,v$. (Check: $\sigma_X \approx 6.7\%$, skew $\approx -0.13$, tax $\approx 15$ bp.) Then flip the sign of $C^{\text{spr}}$, show that the survival leg of a non-call bond is right-skewed, and explain why the mixture is still left-skewed overall.

3. **Find the jump.** In Kou's model with $V/B = 1.5$, $\lambda^{V} = 0.5$ per year, and $p = 0.4$, find the $\eta_2$ that produces a jump-to-default intensity of 10% per year. Compute $\mathbb{E}[V_\tau/B]$ and the expected recovery given a jump default with $B = F$ and bankruptcy cost $\alpha = 0.3$. (Check: $\eta_2 = \ln 3/\ln 1.5 \approx 2.71$; $\mathbb{E}[V_\tau/B] \approx 0.73$; recovery $\approx 51\%$.) Then add the Brownian-bridge correction from the Ways This Blows Up box to `simulate_kou_jd` and measure how much the one-year default probability rises under weekly steps.

4. **ROBO minimizes kurtosis.** ROBO is told to "maximize yield subject to single-name excess kurtosis of at most 10." Using the Bernoulli skeleton, show that the constraint is equivalent to $q(1-q) \ge 1/16$, that is, $q \ge (1 - \sqrt{3}/2)/2 \approx 6.7\%$, so the kurtosis limit is a mandate to own distressed paper. Show that at $q = 1/2$ the bond attains excess kurtosis $-2$, the minimum for *any* distribution, and explain why ROBO's ideal holding is a coin flip with a coupon. Rewrite the constraint as a 99% expected-shortfall or jump-to-default limit that does what the PM meant.

5. **The 13-week model, one more time.** Theo's cash model, run under shocks, gives weekly conditional hazards of 0.2% for weeks 1 through 8 and 1.5% for weeks 9 through 13. (a) Compute the 13-week default probability. (Check: about 8.75%.) (b) Compute the Bernoulli-skeleton skew at that $q$ and say whether a 95% VaR sees the default world. (c) Theo asks, "But what does the credit agreement say?" It permits a non-pro-rata uptier with a simple majority. Split the 8.75% into hard-default and distressed-exchange components using §5.6.1, assign each component a recovery distribution (including the participant and non-participant Betas), and write the resulting categorical mixture.

### Deep-Dive Resource Graph

- **Podcasts:** Bloomberg *Odd Lots*, episodes on liability management exercises and "creditor-on-creditor violence" (2023–2025; titles to be confirmed); Bloomberg Intelligence *The Credit Edge*, episodes on recoveries and LMEs (titles to be confirmed); *Flirting with Models* (Corey Hoffstein), episodes on systematic credit and tail risk.
- **Practitioner Writing:** Octus, "The Year in LMEs" (January 8, 2026), https://octus.com/resources/articles/the-year-in-lmes/ ; Holwell Shuster & Goldberg, "Liability Management Exercises and the Courts in 2025" (December 22, 2025), https://www.hsgllp.com/about-news-Liability-Management-Exercises-and-the-Courts-in-2025 ; Moody's, *Loss Given Default Rating Methodology* (August 2006), mirror at https://care-mendoza.nd.edu/assets/152347/loss-given-default-rating-methodology.pdf ; Matt Levine, *Money Stuff*, columns on Serta, "open market purchase," and the Hertz make-wholes (no link).
- **Academic Papers:** Altman, Brady, Resti, and Sironi (2005), *The Link between Default and Recovery Rates: Theory, Empirical Evidence, and Implications*, Journal of Business; Altman and Kalotay (2014), *Ultimate Recovery Mixtures*, Journal of Banking & Finance; Bruche and González-Aguado (2010), *Recovery Rates, Default Probabilities, and the Credit Cycle*, Journal of Banking & Finance; Merton (1976), *Option Pricing When Underlying Stock Returns Are Discontinuous*, Journal of Financial Economics; Berd, *Recovery Swaps*, Journal of Credit Risk, preprint at https://arxiv.org/abs/1001.0783 ; Giesecke, Longstaff, Schaefer, and Strebulaev (2011), *Corporate Bond Default Risk: A 150-Year Perspective*, Journal of Financial Economics.
- **Data & Code:** FRED, https://fred.stlouisfed.org/ (ICE BofA OAS and total-return series); SEC EDGAR, https://www.sec.gov/edgar (credit agreements and 8-Ks for the recovery covariates); CourtListener REST API, https://www.courtlistener.com/help/api/ (plans and disclosure statements for realized recoveries); Moody's Default & Recovery Database and Ultimate Recovery Database (subscription, no link); `credit_mixture_lab.py` in §5.9.


<!-- STATUS: COMPLETE -->
