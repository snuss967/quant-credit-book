# Chapter 11: Defensive Systematic High Yield


## 11.0 Cold Open: The Bow Tie

*Fiction label: the desk, Theo, Ines, Kaz and Mags, and every word they say are invented. The two spreads are the published ICE BofA closes for that day (FRED), and the CCC returns and capture ratios are real figures, sourced where they return in §11.1 and §11.2.*

Thursday, 15 October 2026, 4:05 p.m. The close came up on Theo's second monitor as two numbers that did not look like they belonged to the same asset class. ICE BofA US High Yield Index option-adjusted spread: 323bp. ICE BofA CCC & Lower: 1,278bp.

Ines rolled her chair over without being asked, which was how Theo knew he was about to be taught something.

"What's the pot, Theo?"

"The index says it's a quiet Thursday."

"And the CCC tier?"

"The CCC tier says something happened and nobody told the index."

"So who at this table knows more than you?" She tapped the screen. "Not the index. The index is more than half double-B. It's wearing a 323 basis point bow tie. The CCCs are wearing a 1,278 basis point necktie. Same companies' cousins, different dress code."

Theo reached for the USB stick on his lanyard. The 13-week cash flow model had been his companion through four restructurings and one divorce of a client from its sponsor. It did not cover 2,000 issuers. It covered one, very well, for thirteen weeks.

He had once spent a whole Saturday on a single question: could one company make one February interest payment? The CCC tier was a crowd of companies asking that question at the same time, and the 1,278 on the screen was the market's average answer for all of them. Averages, he was beginning to learn, were what the desk sold to people who did not want to read the documents.

Kaz looked up from a rating-agency release. "This says the issuer is in *selective default*. Selective like a university?"

"Selective like the sponsor chose which lenders got paid," Theo said.

"You'll meet a famous one on Friday," Ines said. "Thirteen months from new issue to courtroom. The bonds knew about halfway through. The default label found out at the end."

Kaz wrote *selective = ?* in the corner of the whiteboard, which was as close as Kaz came to applause.

Mags did not look up at all. "Back in my day, CCCs did minus 30.6% in 2000 and plus 50.8% in 2003, and nobody called either one a regime. We called the first one 'the year' and the second one 'the other year.' The people who avoided all the defaults in 2000 were too scared to buy in 2003. They were very well protected. They were also very poor."

Ines pulled up a single slide from a BlackRock white paper: the average high yield manager, eVestment data, 2005 to 2025. Downside capture 89.56%. Upside capture 92.24%.

"That's a player who folds ten percent of every hand," she said. "Including the ones they would have won. A capture ratio is a hand history, not a skill. Your job is to fold the hands that lose and play the hands that win. That is a different job from playing ten percent smaller."

Theo looked at the bow tie and the necktie. "So the question is how you avoid the defaults without missing the rebounds."

"That," said Ines, "is the whole game."

Theo thought of it as a trap with two jaws. The first jaw was 2000, which bit the people who stayed in the CCCs. The second was 2003, which bit the people who had left. The slide on Ines's screen was the industry's answer, and as far as he could tell it was a way of being bitten gently by both.

Ines peeled a yellow Post-it off the pad by her keyboard and wrote on it before anyone had opened a model, in the small square hand that had once filled in tournament scorecards. She stuck it to the bezel of Theo's monitor, directly under the necktie.

*By Friday: which CCC names would you drop, what do you replace the carry with, and what do you do when they rally?*

"Tomorrow?"

"Next Friday. Tomorrow is the replay." She picked up her coffee. "Three questions, and they come in that order for a reason. You can't answer the first one by looking at a rating. The tier is a crowd, and you're buying one person in it, so you need a price on the person, plus an honest test of whether that price would have picked the right people at the rate you'd actually throw them out."

"And the second?" Kaz asked.

"Whatever you drop, you put the risk back somewhere else, so the beta stays at one and the defense comes from who you hold, not from how little. What's left in the dangerous tier you size by what it can lose, not by how it makes you feel." She set the cup down like a chip. "The third is the one the dimmer switch gets wrong. When the spread blows out and the market starts paying too much for risk, you add. And before any of it, you work out how much money the trick can take before the costs eat it."

Mags finally looked up. "That's three answers to one question."

"It's one answer," Ines said, "said three times, the way people learn things."

Theo looked at the Post-it, then at the USB stick. Three questions he could not answer for 2,000 issuers. He could answer all three, slowly, for one. It would turn out to be the right place to start.

## 11.1 The Asymmetry: Why High Yield Needs a Defense at All

Ines frames high yield the way a poker player frames selling insurance. "You collect the ante every hand. Most hands, nobody calls. Then one hand, somebody calls, and you pay out the whole pot. A high yield bond is a short put that sends you a coupon." The RSSG reader knows the second half of the sentence from the inside: the restructuring is the hand where the put gets exercised, and the recovery waterfall is the payout schedule.

### 11.1.1 The mixture return and where the skew comes from

Theo's first move, on the Thursday of the bow tie, was to ask Kaz for the CCC tier's volatility. Kaz had a number inside a second, and Mags waved it away before Kaz had finished saying it. "Volatility is for things that wiggle," she said. "These don't wiggle. They clip coupons and then one day they fall off a table." She was describing a shape. The upside of a bond is capped near par (call schedules make it worse: a callable B bond trading at 103 is a bond whose issuer is waiting for you to get comfortable). The downside is a jump to recovery. The question for this section is how much of the distribution that jump owns, and the answer is "more than its probability suggests."

> **Math, Gently. A bell with a lonely spike.** A *distribution* is a picture of where the outcomes pile up: imagine a hundred possible years for one bond, drop each year's return into a bin, and the heights of the bins are the distribution. Most risk talk on a desk ("vol is 4%", "that was a two-sigma month") quietly assumes the pile is *normal*, the symmetric bell whose whole shape is fixed by its middle and its width. Now draw the hundred years of a single-B bond with a 3% chance of default, carry of 3.3%, and a 60% price loss if it defaults. Ninety-seven years land in a tight bell around +3.3%, nudged left or right by whatever spreads did. Three years land on one spot far away at −60%, with nothing in between. That is two shapes sharing one axis, a bell and a spike, and the stack is called a *mixture*. Its mean fits in the margin: $0.97 \times 3.3\% - 0.03 \times 60\% = 3.20\% - 1.80\% = 1.40\%$, so three bad years spend more than half of ninety-seven good years' carry. The lopsidedness has a number, the *skew*, which says how far the long tail stretches on one side; a normal bell has a skew of zero by construction, and the spike alone has $-(1-2\times0.03)/\sqrt{0.03\times0.97} = -0.94/0.171 \approx -5.5$. "Normal" is the wrong word for this bond because a normal distribution has no way to say "three years out of a hundred, all at once, over there," and "a 4% vol asset" describes the ninety-seven years and is silent on the three that decide the trade. The full version, variance and skew derived, is next.

Here is that bond written down properly. Fix a horizon $h$ (one year). Under the physical measure $\mathbb{P}$, a bond either survives or defaults. If it survives, its excess return over duration-matched Treasuries is carry $c$ minus spread duration times the spread change, $c - D^{\text{spr}}\Delta s$. If it defaults, it jumps from price $P_0$ to recovery $R$ (in price points). Let $J = \mathbb{1}_{\tau \le h}$ be the default indicator with $\mathbb{P}(J=1)=p$, and define the *price-based* loss

$$
L_P \equiv \frac{P_0 - R}{P_0}.
$$

The one-period excess return is the mixture

$$
r = (1-J)\,Y + J\,(-L_P), \qquad Y \equiv c - D^{\text{spr}}\Delta s,
$$

where $Y$ has mean $m$ and variance $v$ and we take $J$ independent of $Y$ (a simplification: in practice spreads widen before default, which only makes the left tail worse). The first moment is immediate:

$$
\mathbb{E}^{\mathbb{P}}[r] = (1-p)\,m - p\,L_P.
$$

For the variance, compute the second moment, $\mathbb{E}[r^2] = (1-p)(v+m^2) + pL_P^2$, and subtract the squared mean $(1-p)^2m^2 - 2p(1-p)mL_P + p^2L_P^2$. Collecting terms, $(1-p)m^2 - (1-p)^2m^2 = p(1-p)m^2$ and $pL_P^2 - p^2L_P^2 = p(1-p)L_P^2$, so

$$
\operatorname{Var}^{\mathbb{P}}[r] = (1-p)\,v + p(1-p)\,(m + L_P)^2 .
$$

The second term is the jump. Its size is set by $m + L_P$, the distance between "survive and clip the coupon" and "default and lose the price," which for a high yield bond is an order of magnitude larger than $\sqrt{v}$.

Now isolate the jump component, $-L_P J$. A Bernoulli variable has skewness $(1-2p)/\sqrt{p(1-p)}$, and multiplying by the negative constant $-L_P$ flips the sign:

$$
\operatorname{Skew}[-L_P J] = -\frac{1-2p}{\sqrt{p(1-p)}}.
$$

At $p = 2\%$ the skew is $-0.96/0.14 = -6.9$; at $p = 5\%$ it is $-0.90/0.218 = -4.1$; at $p = 20\%$ it is $-0.60/0.40 = -1.5$.

That little table is the counterintuitive part. The *safer* the bond, the *more* skewed its default component. A double-B bond's risk is a rare disaster: small, frequent coupons and one catastrophic outcome that almost never happens. A deep CCC bond's default is common enough that its distribution starts to look like an ordinary, very volatile, merely lopsided asset. This is the precise sense in which a CCC bond is an equity option that wears a tie to work: as $p$ rises the bond's payoff converges on the shape of the residual claim on the firm, and the tie is the coupon. It also tells you why the two halves of high yield need different defenses. In the BB tier the job is to avoid the rare jump; in the CCC tier the jump is the base case and the job is to price it. Figure 11.1 draws both the mixture and the skew curve.

![Figure 11.1: A high yield bond's one-year return is a tight bell plus a lonely jump (left), and the jump is most skewed for the safest bonds: −6.9 at a 2% default probability, −4.1 at 5% and −1.5 at 20% (right). Illustrative: the §11.1.1 mixture with survive-case return N(3.3%, 4.0%), where 3.3% is the 326bp single-B OAS of 15 October 2026 (FRED BAMLH0A2HYB) used as carry, default probability 3% and price loss 60% (left); the skewness formula −(1 − 2p)/√(p(1 − p)) (right).](assets/figures/ch11_mixture_skew.png)

### 11.1.2 The credit triangle, with the measure stated

Shrink the mixture's mean to one line and you get the most quoted formula in credit, which is also the most abused, because it comes in two versions that look identical on a whiteboard.

> **Math, Gently. Bookmaker's odds versus true odds.** Every default probability on a desk comes in one of two flavors, and the flavor is called a *measure*. $\mathbb{P}$ is the true-odds world: how often issuers like this one actually default. $\mathbb{Q}$ is the bookmaker's world: the default probability that, dropped into a plain expected-value sum, gives back the price on the screen, which means the bookmaker's margin (fear, illiquidity, the cost of tying up capital) is already baked into the odds. Picture a CDS quoted at 300bp on a name that would lose 60% in default. Read through "spread equals default rate times loss," the market is implying a $\mathbb{Q}$ default rate of $300/60 = 5\%$ a year. Suppose the honest $\mathbb{P}$ rate, from history and from somebody's 13-week model, is 3%. The protection seller collects 300bp and expects to pay out $3\% \times 60\% = 180$bp, so the expected excess return is $300 - 180 = +120$bp a year. Run the same sum with the bookmaker's 5% and you get $300 - 300 = 0$, on this name and on every name, because the 5% was manufactured to make that sum come out at zero. A $\mathbb{Q}$ probability tells you what a bond costs; it cannot tell you whether the bond is cheap. Chapter 5 (§5.1.1) met the two measures at the racetrack and Chapter 6 (§6.3) writes out the change of measure; the one-line version this chapter needs is next.

For small $p$, with carry approximately equal to spread ($c \approx s$) and no expected spread change ($m \approx s$), the mean collapses to the credit triangle written under $\mathbb{P}$:

$$
\mathbb{E}^{\mathbb{P}}[r^{xs}] \approx s - \lambda^{\mathbb{P}} L,
$$

with $\lambda^{\mathbb{P}}$ the physical default intensity and $L$ the loss. The break-even physical default rate is $\lambda^\ast = s/L$. Under the recovery-of-market-value (RMV) convention the risk-neutral version $s = \lambda^{\mathbb{Q}} L_P$ holds exactly in continuous time, and that is why $L$ is measured from *price*.

The line looks too simple to get wrong. Kaz got it wrong three ways in one afternoon, with help. Kaz pulled CDS-implied hazard rates for every index name that had a CDS, ran $s - \lambda^{\mathbb{Q}}L$ down the whole column, and turned the screen around. "Expected excess return of US high yield: zero, plus or minus rounding. High yield has no expected return. I have been wasting everyone's time."

"You priced it with the bookmaker's odds," Ines said. "The CDS hazard already has the risk premium in it. Of course it nets to zero. That's the sum that made the spread."

Kaz swapped in physical PDs. Mags leaned over and put a finger on the recovery column, which said 40% on every row. "That's the CDS convention, not a recovery. Moody's 1970–2002 mean was 43.10% in expansions and 27.85% in recessions" (Schmid p.103). "Defaults come in recessions. Weight by when people actually default and you're near the second number."

Theo found a CCC line priced at 70 with an assumed recovery of 28. "And that loss is measured from par. You paid 70 and get back 28. You lose 60% of what you paid, not 72%."

Kaz changed three columns. The zero went away, and in its place was a number that differed by tier, which was the first honest thing the spreadsheet had said all day.

Here is what break-even looks like on the cold-open close, with spreads from FRED for 15 October 2026 (BB 197bp, B 326bp, CCC & lower 1,278bp) and two loss assumptions:

| Tier | OAS (bp) | $\lambda^\ast$ at $L=0.60$ | $\lambda^\ast$ at $L=0.72$ | S&P one-year default rate, 1980–2002 (Schmid p.28) |
| :--- | ---: | ---: | ---: | ---: |
| BB | 197 | 3.3% | 2.7% | 1.53% |
| B | 326 | 5.4% | 4.5% | 6.95% |
| CCC | 1,278 | 21.3% | 17.8% | 31.58% |

*(Break-even rates are our computation; the historical column is the NR-adjusted S&P table reproduced in Schmid.)* On the 1980–2002 table, which contains three recessions, both single-B and CCC would be negative-expectation bets at today's spreads. On Moody's forward one-year PD of 3.2% for the average US high yield company in Q1 2026 (Moody's Analytics, *Lend, extend, and then…*, 18 May 2026), the index as a whole is comfortably paid. Which number applies to the bond in front of you is the subject of the rest of this chapter. The tier average is not the answer, because the tier is a crowd and you are buying one person in it.

> **[SOURCE EXTRACTION]** *Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.26:* "the tightening of a bond on the upside to risk free rates is typically asymmetrically smaller than the jump to recovery in situations of distress. Low-risk factor signals target shorter-dated, higher-rated bonds."
>
> **Annotation.** Man Group puts the whole chapter into two sentences: the asymmetry is the reason a low-risk factor exists at all. The first sentence is the mixture derivation in words: the upside is bounded by the spread you can tighten toward zero, the downside by the price you can lose. The second sentence is a design choice, and it is where a 2026 desk should push back gently. "Shorter-dated, higher-rated" is a proxy for low PD, chosen because ratings and maturity are free and universal. A desk with a calibrated PD can target the thing itself, and the difference matters in exactly the cases an RSSG banker cares about: a short-dated single-B bond with a maturity wall in fourteen months is not low-risk, it is a refinancing event with a coupon, and a long-dated double-B issued by a sponsor-owned company with a large unrestricted-subsidiary basket is higher-rated than its priming risk deserves (Chapter 13). Use the proxy as a fallback feature, not as the definition.

Mags's numbers from the cold open have a source too, and it says the same thing from the distressed side of the table.

> **[SOURCE EXTRACTION]** *Moyer_Distressed_Debt_Analysis p.25:* "If CCC-rated bonds are, for convenience, used as a proxy for distressed, then the negative market returns for this group over the 1999–2002 period, shown in Table 1-2, illustrate the dangers, while 2003 returns demonstrate the opportunity."
>
> **Annotation.** Moyer's Table 1-2 (CSFB data) is Mags's war story in print: CCC returns of −3.0% in 1999, −30.6% in 2000, −2.1% in 2001, −12.7% in 2002, and +50.8% in 2003. Compound the five years and a dollar becomes about \$0.87: four years of losing, then one year that recovered most of it. Now run the two classic "defensive" responses through it. Exclude CCC entirely and you sidestep 2000 and 2002 but forfeit 2003, and whether that wins the round trip depends entirely on where you parked the money and whether you had the nerve to come back in January 2003 (nobody did). Exclude the CCCs that *default* and you keep most of 2003, because the 2003 rally was earned by the survivors repricing from distressed to merely leveraged. The lesson for a systematic desk is that the tier is the wrong unit of decision. The PD-ranked issuer is the right one, and the rest of this chapter builds it.

The industry's answer to the asymmetry is on one slide, and Ines had already put it on Theo's screen.

## 11.2 The Average Manager's Dimmer Switch: Capture Ratios and the Beta-Tilt Diagnosis

BlackRock's 2025 white paper on systematic high yield opens with a diagnosis that should make every long-only HY allocator slightly uncomfortable. Across eVestment data from 2005 to 2025, net of fees, the average US high yield manager captured 89.56% of down markets and 92.24% of up markets; the top-quartile manager captured 92.00% of the down and 99.00% of the up (BlackRock p.3). The paper's verdict on the average manager is that the defense came "largely" from a lower beta. Ines's verdict is shorter: "A dimmer switch is not a strategy. It's a strategy with the lights turned down."

### 11.2.1 The capture-ratio identity

Theo's first question about Ines's slide was the one every allocator asks and almost nobody answers: is 89.56% against 92.24% good, and if it is, good at what?

> **Math, Gently. The gap is alpha, the level is beta.** Draw a square: downside capture along the bottom, upside capture up the side, and a diagonal from corner to corner. A manager who simply holds less of the index, say 91% of it with the rest in cash, lands *on* the diagonal at (91%, 91%). It catches 91% of every rally and 91% of every fall, because holding less scales both by the same number. Now give that manager some real skill: a small fixed amount of extra return every month, rain or shine. In an up month the extra adds to the gain, so upside capture rises; in a down month it shrinks the loss, so downside capture falls. The same monthly amount moves the two ratios by different distances, because each ratio divides by a different average month. Take up months averaging +1.6% and down months averaging −2.0%. An extra $\alpha$ a month moves upside capture by $\alpha/0.016$ and downside capture by $\alpha/0.020$, so the gap opens by $\alpha \times (62.5 + 50) = 112.5\,\alpha$. A manager whose ratios sit 2.68 points apart (92.24% against 89.56%) therefore has $\alpha = 0.0268/112.5 = 0.000238$: about 2.4bp a month, or 29bp a year. The gap measured the skill; the midpoint, about 91%, measured how much index the manager held. The exact statement is next.

Split benchmark months into up months $\mathcal{U} = \{t : r_{b,t} > 0\}$ and down months $\mathcal{D} = \{t : r_{b,t} < 0\}$. Using arithmetic means (eVestment uses annualized geometric means; the algebra is the same to first order), upside and downside capture are

$$
U = \frac{\bar r_p^{\,\mathcal{U}}}{\bar r_b^{\,\mathcal{U}}}, \qquad D = \frac{\bar r_p^{\,\mathcal{D}}}{\bar r_b^{\,\mathcal{D}}}.
$$

If the portfolio follows a single-index model with alpha $\alpha$ and beta $\beta$, the gap between the two ratios is alpha scaled by the two regime means,

$$
U - D = \alpha\left(\frac{1}{\bar r_b^{\,\mathcal{U}}} + \frac{1}{\lvert \bar r_b^{\,\mathcal{D}} \rvert}\right),
$$

which is positive if and only if $\alpha > 0$. That one line does most of the work on a due-diligence call. A pure beta tilt ($\alpha = 0$) gives $U = D = \beta$, so every point of downside "protection" is paid for with a point of upside; and the *level* $(U + D)/2$ is roughly beta.

#### The Full Derivation: the capture identity

Suppose the portfolio follows a single-index model $r_{p,t} = \alpha + \beta r_{b,t} + \epsilon_t$ with residuals averaging to zero within each regime. Averaging over up months gives $\bar r_p^{\,\mathcal{U}} = \alpha + \beta\,\bar r_b^{\,\mathcal{U}}$, so

$$
U = \beta + \frac{\alpha}{\bar r_b^{\,\mathcal{U}}}, \qquad D = \beta + \frac{\alpha}{\bar r_b^{\,\mathcal{D}}}.
$$

Because $\bar r_b^{\,\mathcal{D}} < 0$, a positive alpha raises $U$ above $\beta$ and pushes $D$ below it. Subtracting the second expression from the first gives the identity above.

With the box's regime means *(illustrative; the paper reports only the capture ratios)*, the two managers BlackRock reports decompose as follows.

| Manager (BlackRock p.3) | $U$ | $D$ | Implied $\alpha$ (per year) | Implied $\beta$ |
| :--- | ---: | ---: | ---: | ---: |
| Average | 92.24% | 89.56% | $\approx 29$bp | $\approx 0.91$ |
| Top quartile | 99.00% | 92.00% | $\approx 75$bp | $\approx 0.95$ |

*(Our decomposition under the illustrative regime means.)* The average manager is a 0.91-beta portfolio with a small net alpha. The top-quartile manager is better on both counts, but still a sub-one beta: even the good players fold some winning hands. Figure 11.2 plots both managers against the diagonal of pure beta tilts.

![Figure 11.2: The average manager's defense is mostly a slide down the diagonal toward lower beta (β ≈ 0.91) with a small step off it (α ≈ 29bp a year), and the top-quartile manager steps much farther off (α ≈ 75bp) from β ≈ 0.95. Source: capture ratios from BlackRock (2025) p.3 (eVestment, 2005–2025, net of fees); the α–β split applies the §11.2.1 identity with the illustrative regime means of +1.6% and −2.0% a month.](assets/figures/ch11_capture_plane.png)

Why does a 0.91 beta cost money over a cycle? Because high yield's excess return is positive on average and the regimes are lopsided. BlackRock buckets monthly ICE BofA HY Constrained returns at $\pm1.5\%$ and counts 168 positive months against 72 negative ones (BlackRock p.4). A beta of $\beta$ forfeits $(1-\beta)$ of the risk premium in every one of the 168, and recovers $(1-\beta)$ of the losses in each of the 72. Unless the down months are much deeper than the up months are frequent, the dimmer switch loses the round trip.

### 11.2.2 Convexity: the asymmetric-beta regression

Real defense means the portfolio responds *less* to down months than to up months, and the capture identity has no way to say so: it gives the manager one beta for both kinds of month. Kaz's fix was to stop asking for one slope.

> **Math, Gently. A line with a kink.** Plot each month as a dot: the index's return along the bottom, the portfolio's up the side. A beta tilt puts every dot near one straight line through the origin, slope 0.9 on both sides, so the portfolio keeps 90% of the good months and suffers 90% of the bad. A real defender's dots follow a line that *bends* at zero: slope 1.0 to the right, 0.9 to the left. Run a down-then-up pair through each. With $\beta^{+} = 1.0$ and $\beta^{-} = 0.9$, a −5% month costs 4.5% and a +5% month pays the full 5%, so the pair compounds to $0.955 \times 1.05 - 1 = +0.28\%$ while the index compounds to $0.95 \times 1.05 - 1 = -0.25\%$. The straight 0.9 line also loses only 4.5% in the bad month, but it earns only 4.5% back, and $0.955 \times 1.045 - 1 = -0.20\%$. Same defense on the way down, different bill on the way up. In symbols, the kinked line is two slopes, one for the positive part of the index return and one for the negative part, and the regression that estimates both is next.

Write the Henriksson–Merton style asymmetric regression

$$
r_{p,t} = \alpha + \beta^{+}\max(r_{b,t}, 0) + \beta^{-}\min(r_{b,t}, 0) + \epsilon_t .
$$

Averaging within regimes as before, $U = \beta^{+} + \alpha/\bar r_b^{\,\mathcal{U}}$ and $D = \beta^{-} + \alpha/\bar r_b^{\,\mathcal{D}}$. "Good defense" is $\beta^{-} < \beta^{+}$: positive convexity in the active return. Where can convexity come from in a long-only bond portfolio? Only two places. One is security selection that avoids the jump, because defaults and distress cluster in down months, so a portfolio that holds fewer of the bonds that jump has a lower down-beta without a lower up-beta. The other is regime-aware exposure that adds risk after spreads overshoot (§11.8). A uniform beta tilt cannot produce it; it scales both betas together.

Theo found out how easily those numbers go wrong in his second week. A pension consultant (fictional, like the manager in question) forwarded a pitch deck that said "defensive" in forty-point type and showed a downside capture with a footnote in six-point type, plus twenty years of monthly returns in a spreadsheet. Theo, new and thorough, built capture on three tabs, and by 10:40 the three tabs described three different managers. The first sorted months by the *portfolio's* sign, so every month the manager happened to lose money was a down month by definition, and the manager looked worst exactly where it had been unlucky. The second used total returns, and 2022 turned the manager into a genius, because a short duration had dodged the rate selloff: a Treasury bet wearing a credit badge. The third ran the consultant's preferred trailing year, which held three down months, one of them a benchmark dip of 0.3bp. The down-month mean was nearly zero, and $D$ printed at 212% *(illustrative)*.

Ines read the three tabs over his shoulder. "Three tabs, three managers. Which one went to the pension board?" Nobody knew. "One definition, then. Excess returns, the benchmark's months, a floor under the down mean, and the counts printed next to every ratio. Then it can only be wrong one way."

> **[SOURCE EXTRACTION]** *BlackRock_Systematic_High_Yield_Credit p.3:* "Figure 1 shows the average manager tended to participate in 89.56% of down markets and 92.24% of up markets. This illustrates how the average U.S. high yield manager was building a “defensive” exposure largely by creating a portfolio that has a lower beta than the broad index."
>
> **Annotation.** The quotation marks around "defensive" are BlackRock's, and they are doing honest work. Our identity says the paper's numbers are consistent with a beta of about 0.91 and a small alpha, which is a polite way of saying the industry's defense is mostly cash drag, short duration, and an underweight in the riskiest tier. Two cautions before you repeat the number in a pitch. eVestment figures are net of fees, so the gross alpha of the average manager is larger than our 29bp, and the sample has survivorship in it, because managers who closed are not in the 2025 cross-section. And a sub-one beta is not *wrong* for a client who wants lower volatility; it is wrong for a client who is paying active fees for something they could get by holding 9% cash. The modern desk's response is to make beta a separately managed exposure (index, CDX HY, or ETF overlay, see Chapter 8) and to demand that the active book earn its keep through $\beta^{-} < \beta^{+}$.

The same paper then measures what the dimmer switch costs over a full round trip.

> **[SOURCE EXTRACTION]** *BlackRock_Systematic_High_Yield_Credit p.5:* "In many cases, these managers gave up more excess return in subsequent “Very Positive” regimes than was mitigated on the downside during “Very Negative” regimes."
>
> **Annotation.** This is the round-trip cost measured, not argued. BlackRock pairs adjacent regimes (June/July 2013, December 2018/January 2019, March/April 2020, June/July 2022, September/October 2022) and shows the average manager giving back on the rebound what it saved on the drop. In poker terms the hand history shows a player who folds the river every time the flop looks scary, including on the hands where the scary flop was followed by a winning card. The point for a systematic builder is that the defense must be evaluated on *pairs* of regimes, not on down months alone, because a model that looks heroic in March 2020 and is underinvested in April 2020 is a model that has learned fear. Build the evaluation set as regime pairs and you will reject that model before a client does.

### 11.2.3 Case Study 1: The 2022–2023 Round Trip

*A replay, Ines's ritual: the cast and their cards are fictional, and the three portfolios are stylized (illustrative). The benchmark returns are BlackRock's (p.4–5, Figure 3), and the tape is cut at the close of Thursday 30 June 2022.*

Ines ran a short one before anyone went home on the Thursday of the bow tie. She called it a palate cleanser, which meant it would take an hour.

"June 2022," she said, and put up one number: the high yield benchmark, −6.8% for the month. "Rates are going up in three-quarter-point steps, the word on every call is *recession*, and the year to date is already the worst first half most of you have seen. It's the last day of June. You each run one portfolio. Here is how your June went."

She dealt them by monitor. Theo's was the plain index-weight book, beta one, which had lost the full 6.80%. Kaz's was the industry's dimmer switch, a 0.91 beta built from cash and a light CCC underweight, which had lost 6.19%. Mags got the third, a book that held beta at one in up months but had spent the spring dropping the issuers whose default probabilities were climbing, so the bonds that gapped in June were mostly bonds it did not own. Its down-beta for the month came out at 0.90 and its June loss at 6.12%.

"July," Ines said. "Write three things on the card: your beta for the month, what you sell or buy, and why."

Theo looked at his 6.80% and felt the room the way he had felt a hundred lender calls: the committee would want to see that somebody had done something. He wrote *0.8. Cut a fifth of the risk. Protect what's left until the Fed stops.* It was, he would later admit, exactly the card the investment committee of a long-only fund writes at the end of a bad month, and he wrote it in the committee's handwriting.

Kaz wrote *0.91, unchanged*, and under it, *the tilt is the strategy; changing it after a loss is timing, and nobody has shown me a timing model that works*. This was true and also, as Mags pointed out, the most Kaz sentence ever written on an index card.

Mags wrote two words. *Which bonds?*

"That's not a beta," Theo said.

"It's the only question," Mags said. "My beta's one. It stays one. I want to know which names moved their PD in June and which ones just moved their price. The first lot I sell. The second lot I keep, because they're the ones that come back."

Ines flipped the tape forward. July 2022: the benchmark returned +6.0%, the first leg of the bear-market rally that BlackRock pairs with June as one of its regime pairs.

Theo's book, at 0.8, made 4.80%. Over the two months it compounded to −2.33% against the benchmark's −1.21%, a 112bp *loss* to the index it had been trying to protect itself from. It had taken the whole down month at full size and only four-fifths of the up month.

Kaz's tilt made 5.46%, for a two-month −1.07% and a 14bp win. Kaz looked pleased for about a second, until Ines pointed out where the 14bp came from: compounding on a down-then-up path. Hold 0.91 through an up-then-down pair instead and the same arithmetic hands the 14bp back. The dimmer switch had not defended anything. It had been lucky about the order of the months.

Mags's book, with its beta back at one for the rally, made the full 6.00%. Two months: −0.49%, a 72bp win. Nothing about July had been predicted. The 72bp had been earned in May and June, in a spreadsheet of default probabilities, before anybody knew the rally was coming.

"Grade the cards," Ines said. "Theo, you sold the bottom. That's the nervous committee, and it's the most common card in the industry; BlackRock's average manager finished 2022 ahead and 2023 behind, with a net giveback over the two years (p.4), and you just did the same thing in two months. Kaz, you held a tilt that can't lose a round trip by much and can't win one either. Mags asked the right question." Mags did not look up, which meant she had heard. September and October 2022 ran the pattern a second time, −4.0% and then +2.8% for the benchmark, and the replay's three cards would have come back in the same order.

Theo turned his card over. "Mags didn't know July was coming."

"Nobody did. That's the point," Ines said. "Her book's edge isn't a forecast of the market. It's a forecast of *which bonds* fall more than their spread duration says they should, and that's a default and distress forecast. Build that, and you never have to guess the month." That is what §11.3 through §11.5 build.

> **Trend Watch: The Whipsaw Years, 2022–2026.** *What changed:* high yield stopped trending and started reversing, which is the regime where a beta tilt does worst. *When and how big:* 2022, US HY "down over 11%"; 2023, "up over 13%" (BlackRock p.3, Bloomberg data as of 31 March 2024). The average manager beat the benchmark by 0.47% in 2022 and lagged by 0.68% in 2023 (BlackRock p.4), giving back more than it saved. In 2024 the pattern repeated at a smaller scale: +0.35% versus benchmark in Q1, −0.37% over the rest of the year (BlackRock p.5). The ICE BofA US High Yield total return index returned +8.20% in calendar 2024 and +8.50% in 2025, then fell 3.83% from 28 February to 7 April 2025 on the tariff shock and regained its prior peak on 12 May 2025, a ten-week V; in 2026 it fell 2.87% from 27 August to 1 October and stood +0.15% year-to-date on 15 October *(our computations from FRED series BAMLHYH0A0HYM2TRIV)*. *What it means for the desk:* shallow, fast V-shaped drawdowns are the worst environment for a strategy that de-risks on price, and the best environment for one that de-risks on default probability, because PDs barely move in a ten-week V while prices move a lot. The whipsaw years are the empirical case for issuer-level defense.

### Specification for AI Implementation

**The Spec You Hand the Robot (vague version, and what ROBO built).** Theo's first message was "Build a defensive high yield strategy that avoids defaults." ROBO sold every bond rated below BB and bought Treasury bills. Realized defaults: zero. Downside capture: 0%. Upside capture: 0%. Tracking error to the HY index: roughly the index's own volatility. Clients: also zero. ROBO did exactly what was asked. The precise version says what "defensive" is measured against: *report $U$, $D$, $\beta^{+}$, $\beta^{-}$ on benchmark-defined regimes, on excess returns, with a floor on the down-month mean; the portfolio must hold $w^\top \text{DTS}$ within 2% of the benchmark's.* The code below is the first of six cumulative blocks; later blocks reuse its imports and functions.

**Schema.** `rp`, `rb`: `float64` arrays of shape `(T,)`, monthly excess returns in decimal, aligned by month. `T >= 24`, at least 3 up and 3 down benchmark months. Output of `capture_ratios`: tuple `(U, D)` as decimals. Output of `asymmetric_beta`: dict with `alpha` (per month), `beta_up`, `beta_dn`.

At 10:40 three tabs disagreed about one manager, and the listing exists so that a fourth tab cannot: the definition becomes a function that refuses to answer when the question is ill-posed. It has two functions and a block of self-checks. `capture_ratios` takes aligned monthly excess-return arrays for the portfolio and the benchmark, splits the months by the *sign of the benchmark* (strictly positive is up, strictly negative is down, exactly zero belongs to neither), and returns the ratio of the portfolio's mean to the benchmark's mean within each regime. It raises an error rather than answering if the arrays are not aligned one-dimensional vectors, if either regime has fewer than three months, or if either regime's benchmark mean is smaller in magnitude than the `floor` of one basis point a month, because a capture ratio is a quotient and a quotient with a near-zero denominator is a random number with a ratio's dignity. `asymmetric_beta` runs the ordinary least squares regression of §11.2.2 on a constant, the positive part of the benchmark return and the negative part, and returns `alpha` (per month), `beta_up` and `beta_dn`. Read `beta_dn` as the portfolio's loss per unit of benchmark loss; good defense is `beta_dn` below `beta_up`.

The self-checks are the point of the exercise. A synthetic benchmark of 240 months, seeded, is run through four tests: a pure 0.9 tilt must return $U = D = 0.9$; adding a monthly alpha must open the gap; the gap must equal the identity of §11.2.1 to within $10^{-12}$; and a noisy portfolio built with up-beta 1.0 and down-beta 0.8 must come back from the regression with `beta_dn` at least 0.1 below `beta_up`. The first three are exact and catch coding errors; the fourth is statistical and shows the regression can see convexity.

The function does not clean your data, and that is the gap the 10:40 scene did not show: a missing portfolio month turns the affected mean into NaN, the regression has no opinion about gaps at all, and forward-filling converts a missing month into a zero-return month, which is a beta of zero in disguise. Alignment and pairwise dropping happen before the call. Zero-benchmark months are also treated differently by the two functions: they are excluded from capture but remain in the regression, where they pull on `alpha` only.

*The full listing is [Listing 11.1 in Appendix F](#code-11-1).*

**Edge cases for ROBO.** Months where the benchmark return is exactly zero belong to neither regime; they are excluded, not assigned. Missing portfolio months are dropped pairwise, never forward-filled (a forward-filled month is a month of zero return, which is a beta of zero in disguise). Report regime counts alongside every capture ratio.

## 11.3 Default Avoidance I: The Structural PD

Theo's first instinct was the right one, at the wrong scale. An RSSG banker decides whether a company will default by building its liabilities, its liquidity, and its enterprise value, then asking whether the value covers the claims. Merton (1974) is the same judgment written as an option, and its industrial descendant, the KMV expected default frequency, is how firms like BlackRock and Blackstone run the judgment on every issuer every night. BlackRock's signal "centers on a simple economic assumption that default occurs when the value of a firm's assets fall below the value of its liabilities" (BlackRock p.6). That sentence is Merton's model, and also, Theo noted, the first page of every fairness opinion he ever drafted.

> **[SOURCE EXTRACTION]** *Blackstone_Systematic_Credit p.1:* "By relying on these proprietary, computationally derived default probabilities rather than sluggish rating agency downgrades or upgrades, the algorithm can objectively compare creditworthiness across the entire global corporate universe"
>
> **Annotation.** Blackstone's systematic credit platform grew out of its late-2020 acquisition of DCI, whose co-founders created the KMV model (Blackstone p.1–2), so this is the structural-model lineage speaking about itself. The two words that matter are "sluggish" and "compare." Ratings move late (Ben Dor p.288: a spread-based indicator registers deterioration "much faster" than a ratings-based one) and they are ordinal, so a B2 in software and a B2 in retail are not the same risk. A PD is cardinal: it can be multiplied by a loss and subtracted from a spread, which is what the credit triangle of §11.1.2 needs. The modern caution is the word "entire." The structural model needs a traded equity, and a large share of US high yield issuers are sponsor-owned with no listed stock. For those names the "computationally derived" PD is either bond-implied (circular, since you are using the spread to forecast the spread) or accounting-only (slow). Flag which regime each PD came from and let the model treat the flag as a feature.

### 11.3.1 Equity as a call, solved backward

At PJT, Theo had valued a company by building it up from the bottom: cash flows, a multiple, an enterprise value, and then the waterfall. The structural model runs the same building in reverse, from the top. It starts with the one number the market prints every second, the stock price, and asks what the assets underneath must be worth and how much they must wobble for the stock to trade there. Two ideas make that possible.

> **Math, Gently. Part 1: random walk, then compounding, then the half-sigma-squared.** A *random walk* is a path built from coin flips: each step goes up or down by a random amount, and nobody, including the coin, knows the next one. Asset values walk, but they walk by *multiplying*, not adding: a good year is +40%, a bad year is −40%. Start at 100 and flip twice. The four equally likely paths end at $100 \times 1.4 \times 1.4 = 196$, at 84 (twice, up-then-down or down-then-up), and at $100 \times 0.6 \times 0.6 = 36$. Their *average* is $(196 + 84 + 84 + 36)/4 = 100$, exactly where you started. Their *typical* outcome, the middle one, is 84. The average path is held up by the rare lucky one; the path a real firm usually walks sags. That sag has a size: with volatility $\sigma_V$, the typical (median) path grows at $\mu - \tfrac12\sigma_V^2$ instead of $\mu$. At $\sigma_V = 40\%$ over one year the drag is $\tfrac12 \times 0.40^2 = 8$ points a year, which is why a volatile firm with a respectable expected return can still be drifting, typically, toward its debt. Chapter 6 (§6.1) derives the $\tfrac12\sigma^2$ properly, as Itô's lemma.
>
> **Part 2: equity is the call, read backward.** Shareholders own the assets but owe the debt, so equity behaves like a call option on the firm: worth $V - F$ when things go well and zero when they do not. A call moves less than its underlying in dollars (its delta, $N(d_1)$, is below one) but a lot more in percent, because it is a thin slice on top of the assets. Running that backward is the trick. Suppose the stock is worth $E = 2$ (billion), the assets $V = 6$, the delta $N(d_1) = 0.8$, and the stock's volatility is 60%. A 1% move in assets moves equity by $0.8 \times 0.06 = 0.048$, which is 2.4% of $E$, so the assets must move $1/2.4$ as much as the stock: $\sigma_V = 0.6 \times 2/(0.8 \times 6) = 25\%$. Pile on more debt and $E$ shrinks against $V$, and the gap between the scary equity volatility and the calmer asset volatility widens. The two equations that do this exactly are next.

Let the firm's assets $V_t$ follow a geometric Brownian motion under $\mathbb{P}$ with drift $\mu$ and volatility $\sigma_V$, and let debt be a single zero with face $F$ due at $T$. Equity is a European call on the assets:

$$
E = V\,N(d_1) - F e^{-rT} N(d_2), \qquad d_{1,2} = \frac{\ln(V/F) + \left(r \pm \tfrac12\sigma_V^2\right)T}{\sigma_V\sqrt{T}} .
$$

We observe $E$ (market capitalization) and $\sigma_E$ (equity volatility), not $V$ and $\sigma_V$. The second equation comes from Itô's lemma. Write $E = f(V,t)$; then $dE = f_V\,dV + (\ldots)\,dt$, so the diffusion term of $dE$ is $f_V\,\sigma_V V\,dW_t$. Dividing by $E$, the equity volatility is $\sigma_E = f_V \sigma_V V/E$, and since the call's delta is $f_V = N(d_1)$,

$$
\sigma_E\,E = N(d_1)\,\sigma_V\,V .
$$

Two equations, two unknowns, and they always have an answer. The leverage effect is visible in it: $\sigma_V = \sigma_E E/(V N(d_1)) < \sigma_E$, and the more debt, the bigger the gap between the two volatilities.

#### The Full Derivation: inverting for $V$ and $\sigma_V$

For a fixed $\sigma_V$, the call value is strictly increasing in $V$, so $V(\sigma_V)$ is found by a bracketed root search on $[E,\, E + 2F]$: at $V = E$ the call is worth less than $E$, and at $V = E + 2F$ it is worth at least $V - Fe^{-rT} > E$. Then search over $\sigma_V \in (0, \sigma_E]$ for the root of $\sigma_V V(\sigma_V) N(d_1) - \sigma_E E$. The upper end works because $E \le V N(d_1)$, so the gap is non-negative at $\sigma_V = \sigma_E$; the lower end works because the gap tends to $-\sigma_E E$. Both brackets hold for every firm with positive equity, which is why the solver in Listing 11.2 can promise an answer instead of hoping for one.

Distance-to-default is the number of asset standard deviations between expected asset value and the default point at the horizon, under the *physical* drift:

$$
\text{DD}_T = \frac{\ln(V/F) + \left(\mu - \tfrac12\sigma_V^2\right)T}{\sigma_V\sqrt{T}} .
$$

Under $\mathbb{Q}$ the same expression with $r$ in place of $\mu$ is $d_2$, and $N(-d_2)$ is the risk-neutral default probability that belongs in pricing, not in a PD forecast. For a firm with coupon debt of many maturities, the Vasicek–Kealhofer convention sets the default point to short-term debt plus half of long-term debt, $F = \text{STD} + \tfrac12\text{LTD}$, an empirical compromise reflecting that long-dated debt does not have to be paid this year but does constrain the firm's ability to borrow.

### 11.3.2 The normal-distribution trap

Kaz ran the model on the cross-section and announced the result with the confidence of someone who has assumed Gaussian. "The median public firm has a distance-to-default above four. $N(-4) = 3.2\times10^{-5}$. So the median public firm has a default probability of three in a hundred thousand."

Mags did not look up. "The median public firm has not been informed."

What Mags meant was that Kaz had done the arithmetic right in the wrong world. Distance-to-default counts sigmas, and how much a sigma is worth depends on the shape of the bell it is counted on.

> **Math, Gently. Four sigmas in two worlds.** Draw two crowds of firms lined up by distance-to-default, both with the same middle and the same spread, and walk out four sigmas to the left of each. In the first crowd, shaped like a normal bell, the curve has fallen almost flat by the time you get there: the share of firms out at four sigmas or worse is $N(-4) = 0.003\%$, about three in a hundred thousand. The second crowd has *fat tails*: near the middle it looks almost the same, but its edges thin out slowly, so four sigmas out there are still people standing around. Moody's KMV measured that second crowd on real firm-years, and a DD of 4 turns out to default at almost 1% a year (Bohn–Stein p.138). Line up a hundred thousand firms at DD 4: the bell says three of them default this year, the history says nearly a thousand. Same ruler, two worlds, a factor of about 300. The fix is to keep DD as the ruler, because it ranks firms well, and to read the probability off the history instead of off the bell, $\text{PD} = g(\text{DD})$. Chapter 5 (§5.7) explains why tails get fat, and Chapter 6 (§6.4.3) builds the empirical map; the evidence is the extraction below.

Bohn and Stein put the evidence in two sentences.

> **[SOURCE EXTRACTION]** *Bohn_Stein_Active_Credit_Portfolio_Management p.138:* "This convenient distributional assumption is clearly unrealistic. This becomes clear when we observe that empirically the majority of publicly traded firms have DDs greater than 4."
>
> **Annotation.** Bohn and Stein are describing why Moody's KMV never used $N(-\text{DD})$: the tails of realized asset returns are far fatter than Gaussian, so DD is a good *ranking* and a terrible *probability*. The fix is an empirical map $\text{PD} = g(\text{DD})$, estimated by bucketing firm-years into DD cohorts and recording realized default frequencies; under their map a DD of 4 converts to an EDF of almost 1%, about 300 times the Gaussian answer (p.138). The calibration needs data: "at least 1,000 defaults, with a minimum of 400" (p.163). That threshold is an uncomfortable fact for a desk that wants a high-yield-only model, because the US HY universe produces a few dozen issuer defaults in a benign year. The 2026 answer is to calibrate the map on the broadest default history you can license (all rated and unrated corporates, multiple decades, the NUS Credit Research Initiative as a public benchmark) and to fit HY-specific *adjustments* on top, not to fit a fresh map on 300 HY defaults and call it bespoke.

Figure 11.3 draws the gap between the Gaussian answer and an empirical map, with the sponsor-levered issuer of Listing 11.2 marked.

![Figure 11.3: Distance-to-default ranks issuers well, but N(−DD) is not a probability: at DD = 4 the Gaussian says 0.003% while the empirical map says about 1%, roughly 300 times larger, and the sponsor-levered B issuer (DD 2.44) is 4.6%, not 0.74%. Illustrative: the placeholder map PD = exp(−0.718 − 0.9718 DD), capped at 35%, from Listing 11.2 against N(−DD); the DD = 4 conversion to almost 1% is Bohn–Stein (p.138), and the shaded region is the DD > 4 zone where they find most listed firms.](assets/figures/ch11_dd_pd_map.png)

The bell is not the only place the structural PD breaks in high yield. It also breaks when there is no stock to invert, when a liability management transaction moves the default point without moving the DD, when book equity has gone negative after years of dividend recaps (which matters for accounting covariates but not for Merton, which uses market values), and when equity volatility is stale for a thinly traded small cap, which makes $\sigma_E$ too low and DD too high. The first two, which have cost people the most money, happened to one issuer in thirteen months, and §11.4.3 tells it.

### Specification for AI Implementation

**Schema.** Per issuer-date: `E` (market cap, \$mm, `> 0`), `sigma_E` (annualized decimal equity vol, `> 0`), `STD`, `LTD` (\$mm), `r` (continuously compounded, decimal), `mu` (physical asset drift, decimal), `T = 1.0` years. Output: `V`, `sigma_V`, `DD`, `PD` (12-month, $\mathbb{P}$). Issuers with `E <= 0` or no listed equity raise in the solver and must be routed to the accounting-only model with `no_equity_flag = 1`.

Everything in §11.3.1 is a judgment Theo could make on one issuer with a pencil and a bad night's sleep. The desk's version of the same judgment runs for every issuer with a listed stock, every evening, before anyone is awake to argue with it. At that scale the inversion stops being an equation and becomes a supply chain. Two nested root searches have to converge on every name, including the ones whose stock stopped trading on Thursday, and when one does not converge it must fail loudly and send the issuer to the accounting-only model rather than quietly poison the cross-section with a number that looks like a PD. That is the job of this block.

The listing builds the chain from the bottom. `_merton_call` prices equity as a call on assets and returns the call value with $d_1$ and $d_2$. `merton_solve` is the two-equation inversion: for a trial asset volatility, an inner bracketed search finds the asset value $V$ that reproduces the observed market cap on the interval from $E$ up to $E + 2F$; an outer bracketed search then adjusts the asset volatility until the Itô relation $\sigma_E E = N(d_1)\sigma_V V$ holds, searching between a hair above zero and $\sigma_E$ itself. If the debt is so small that the gap is already non-positive at $\sigma_E$, it returns the equity volatility as the asset volatility and moves on. `kmv_default_point` sets $F$ to short-term debt plus half of long-term debt, `distance_to_default` applies the physical drift $\mu$, and `empirical_pd` maps DD to a one-year PD with a monotone exponential, clipped to a floor of one basis point and a cap of 35%. Its constants are illustrative, built so that a DD of 4 maps to about 1%.

The self-checks start from known $(V, \sigma_V)$, generate the $(E, \sigma_E)$ a market would show, and require the solver to give the originals back within a millionth, with asset volatility below equity volatility every time. They also check that the map is monotone and that $N(-4)$ is still Kaz's three in a hundred thousand. On the sponsor-levered B issuer ($E = \$2{,}000$mm, $\sigma_E = 55\%$, $F = \$2{,}100$mm) the listing prints $V \approx \$4{,}016$mm, $\sigma_V \approx 27.5\%$, DD of 2.44, an empirical PD of 4.6% against a Gaussian 0.74%.

The solver earns its keep where the equity trades daily and the capital structure is mostly one layer of debt. On sponsor-owned names it correctly raises on an absent $E$ (Saks, in §11.4.3, is the example), and its placeholder constants are no substitute for the empirical map's calibration. The quiet failure is in the validation guard: it rejects non-positive `E`, `sigma_E`, `F` and `T`, but not a stale `sigma_E` that is tiny and positive. Feed the issuer above a 2% equity volatility, the kind a stock that has not traded in a week produces, and the solver converges happily to a DD above 70 and a PD pinned at the one-basis-point floor.

*The full listing is [Listing 11.2 in Appendix F](#code-11-2).*

**Edge cases for ROBO.** Stale prices give `sigma_E = 0`: raise, do not divide. Equity vol must be annualized from daily returns with the same day count every time ($\sqrt{252}$), and estimated over a window long enough to be stable (one year) but short enough to see a crisis. Never feed equity vol in as asset vol. Never use `N(-DD)` as a PD.

## 11.4 Default Avoidance II: Hazard Models, Labels, and Gradient Boosting

If you asked Theo to list the covariates in his last distress memo, he would give you twenty: leverage, interest coverage, the springing covenant cushion, the revolver availability, the sponsor's fund vintage, the ABL borrowing base, the maturity wall, and the 13-week cash flow. The empirical literature's answer to "which of these predict default" is humbling. Shumway (2001), using a hazard model on bankruptcies, found that market size, past stock returns, and idiosyncratic return volatility are strongly related to bankruptcy, and that about half of the classic accounting ratios are statistically insignificant once those are in. Chava and Jarrow (2004) found that monthly data improves prediction substantially and that accounting variables add little once market variables are included. Campbell, Hilscher and Szilagyi (2008) built the canonical modern specification and found, as a bonus, that distressed stocks earn anomalously *low* returns, the equity cousin of the low-risk effect in §11.7.

The equity market, in other words, is running Theo's memo every day for free, and the price is the conclusion. The RSSG edge is not in the covariates the market already sees. It is in the label, in the structure, and in the forced sellers, which is where this section and §11.6 go.

### 11.4.1 Altman's Z, and the units trap

> **[SOURCE EXTRACTION]** *Moyer_Distressed_Debt_Analysis p.183:* "Z = 0.012 X1 + 0.014 X2 + 0.033 X3 + 0.006 X4 + 0.999 X5" … "Z-scores of <1.81 have been shown as highly predictive of a bankruptcy as long as two years in advance."
>
> **Annotation.** Altman's (1968) discriminant function: working capital, retained earnings, and EBIT over total assets, market equity over book liabilities, and sales over total assets. Moyer prints the original coefficients, which assume $X_1$ through $X_4$ are entered as *percentages* (so 12% is 12) and $X_5$ as a ratio. ROBO, handed the printed formula and a data feed of decimal ratios, built a model in which every firm's Z-score was 0.999 times its asset turnover plus rounding error. "The dominant factor is sales over assets," Kaz observed, "so the model's main question is whether the company does things." The familiar 1.2, 1.4, 3.3, 0.6, 1.0 version is the same model for decimal inputs. The modern desk keeps Altman for two reasons: as a fast accounting-only fallback for private issuers, and as a reminder that any model handed over without units will be implemented without units. Neither use justifies the 1968 cutoffs on a 2026 sponsor-owned balance sheet, where negative retained earnings are a capital-structure choice, not a symptom.

### 11.4.2 From static logit to the dynamic hazard

> **[SOURCE EXTRACTION]** *Bohn_Stein_Active_Credit_Portfolio_Management p.236:* "this class of discrete-choice models will produce biased estimates since they ignore the periods prior to default when a defaulting firm did not default but may have had a similar financial profile."
>
> **Annotation.** This is Shumway's critique as Bohn and Stein summarize it. A static model takes one observation per firm, usually the last year before default for defaulters, and throws away every earlier year in which the same firm looked just as sick and survived. The model then over-attributes default to whatever a sick firm looks like, and its PDs are too high for sick survivors. The fix is to use every firm-period as an observation. On a 2026 desk the lesson generalizes: any sample that selects on the outcome (one row per default, matched to a "similar" survivor) will flatter the model, which is Bohn and Stein's paired-sample warning at p.226 in another costume.

Shumway's fix needs a different question. A static model asks "is this a firm that defaults?" The hazard model asks, every month, "given that this firm is still alive this month, how likely is it to fail before the next one?"

> **Math, Gently. A hazard is the chance of failing this month, given you made it to this month.** Actuaries have kept this table for three centuries. A life table does not say "40% of people die at 80"; it says, for each age, what share of the people *alive at the start of that year* die before the end of it. That conditional rate is a *hazard*, and it is the natural way to think about a company that is still filing compliance certificates: the question is never whether it will ever die, only whether this is the month. Hazards compound into the probabilities a desk quotes. A firm with a hazard of 0.3% a month survives each month with probability 0.997, so it survives a year with probability $0.997^{12} = 0.965$, and its one-year default probability is $1 - 0.965 = 3.5\%$, a little less than $12 \times 0.3\% = 3.6\%$ because a firm cannot die twice. The model below lets the hazard change with the firm's covariates each month and squeezes it between 0 and 1 with a logit (Chapter 5, §5.5.3, explains the squeeze; §5.1.5 met the hazard first, as Theo's 13-week model). The formula is next.

The discrete-time hazard for issuer $i$ in month $t$, given covariates observed $\ell$ months earlier, is

$$
h_i(t \mid x_{i,t-\ell}) = \mathbb{P}\big(\tau_i \in (t, t+1] \mid \tau_i > t,\, \mathcal{F}_{t-\ell}\big) = \frac{1}{1 + \exp\!\big(-(\alpha_0 + \beta^\top x_{i,t-\ell})\big)} .
$$

Shumway's equivalence result is that the likelihood of this hazard model is the likelihood of a logit estimated on firm-months, so a standard logit routine estimates it, with one correction: because each firm contributes many dependent rows, the logit's test statistics are overstated, and Shumway divides the chi-squared statistics by the average number of firm-periods per firm (Bohn–Stein p.237). The modern equivalent is an issuer-clustered sandwich covariance, which the code below uses. A 12-month PD is then either the compounded monthly hazard, $1 - \prod_{j=1}^{12}(1 - h_{i,t+j})$, or a logit fit directly to a 12-month-ahead label; the second is simpler but its overlapping windows make clustering mandatory.

Kaz read the Campbell–Hilscher–Szilagyi covariates aloud from the paper, one at a time, and Theo, who had promised himself he would stop doing this, translated each one into a line of his 13-week model.

"Net income over market-valued total assets, averaged."

"Burn."

"Total liabilities over market-valued total assets."

"Leverage at market. Which is the only kind a court cares about."

"Excess equity return over the index, averaged."

"The market's running verdict on the forecast."

"Idiosyncratic equity volatility."

"How much nobody agrees with the forecast."

"Relative size."

"Whether a lender will take the call."

"Cash over market assets."

"The numerator of runway."

"Market-to-book."

"How much of the value is a story." Theo hesitated on the last one.

"Log price," Kaz said.

"Whether it's become a penny stock. Which is what a lender call does to a stock." Theo looked at the list. Eight market-scaled covariates, and every one of them was a page of his model that the equity market had already read. One line of the model was not on the list. To these the RSSG desk adds one covariate the literature does not have:

$$
x^{\text{runway}}_{i,t} = \min\!\left(13,\; \text{weeks until projected liquidity falls below the minimum-liquidity covenant}\right).
$$

"Why cap it at 13?" Kaz asked.

"Because that's a quarter," Theo said.

"Of what?"

"Of the year, Kaz." The 13-week model, reborn as a hazard covariate, turns out to be informative precisely where market covariates are blind: private issuers whose liquidity is visible in lender reporting and compliance certificates but not in an equity price.

If the model is fit on a sample whose default rate $\pi_s$ differs from the population rate $\pi$ (oversampled defaults, or a 2008-heavy window), shift the intercept:

$$
\operatorname{logit} \hat p^{\,\text{pop}} = \operatorname{logit} \hat p^{\,s} + \ln\frac{\pi\,(1 - \pi_s)}{\pi_s\,(1 - \pi)} .
$$

In odds, the correction is one multiplication (Chapter 1, §1.3.3, does Bayes in that form): a model fit on a sample with 10% defaults, applied to a population with 3%, has its odds multiplied by $(0.03/0.97)/(0.10/0.90) = 0.28$, so a sample PD of 20%, odds of one to four, becomes odds of $0.25 \times 0.28 = 0.07$ and a population PD of 6.5%.

#### The Full Derivation: the intercept shift

This follows from Bayes' rule: resampling changes the prior odds of default by the factor $\frac{\pi/(1-\pi)}{\pi_s/(1-\pi_s)}$ and leaves the likelihood ratio, and therefore the ranking, untouched. Bohn and Stein's point that "a poorly calibrated PD model can still be useful for ranking obligors as long as the model has predictive power" (p.247) is the same statement read the other way: power and calibration are separate repairs.

### 11.4.3 The label is the model

Here the RSSG reader stops being a student and becomes the teacher. In 2025, 65% of all corporate defaults counted by Moody's were distressed exchanges, not hard defaults (Moody's Analytics, *Lend, extend, and then…*, 18 May 2026). A distressed exchange is a default that files its own press release as "liability management." If your training set calls it survival, the model learns that the way never to default is to default softly, and every sponsor-owned issuer with a drop-down basket becomes, in the model's eyes, a survivor.

Kaz read the rating-agency definition aloud, more or less: an exchange in which holders receive a diminished financial obligation, undertaken to help the issuer avoid a default.

"So the purpose of the default is to avoid default," Kaz said.

The Ad Hoc Group, in unison, represented by counsel: "We object to the characterization."

#### Long Scene: Saks Global, a default in four dates

*A replay, Ines's ritual, run on Friday 16 October 2026 with the tape cut at each date in turn. The cast, their cards and every word they say are invented. The desk never held the notes, never sat in or spoke to any group, and every model output below is the desk's fictional run. The dates, amounts and terms are public: the company's press releases of 21 July and 8 August 2025, press and court-tracker accounts of the Chapter 11 case, and S&P actions as reported in the trade press, each cited where it appears. Named firms and advisers appear only as those sources report them, and nobody outside the desk is given a word to say.*

Ines had promised Kaz a selective default on Friday, and on Friday she delivered one in a manila folder with four dates on the tab.

"Same rules as always," she said. "I cut the tape at a date. You see what the market saw that day and nothing after. You write a card. Then I move the tape." She opened the folder. "Monday, 23 December 2024."

**Beat 1: the new issue.** The first page was a deal summary any RSSG associate could have written in their sleep. Saks Global was buying Neiman Marcus at an enterprise value of \$2.7bn. The money came from \$2.2bn of 11.000% senior secured notes due 2029, with Jefferies as initial purchaser; a \$1.8bn asset-based revolver; \$275mm of seller financing; and about \$1.5bn of equity from new investors, among them Amazon, Authentic and Salesforce (Latham & Watkins deal announcement, December 2024; company press release, July 2025). Two department-store chains, one balance sheet, an 11% coupon on the secured paper.

Kaz had the structural model of §11.3 open before Ines finished the sentence, and closed it again a moment later. "Nothing to invert. There's no stock. `no_equity_flag` equals one; it goes to the accounting model." Kaz scrolled. "This is not unusual, by the way. Chapter 7 has the count: on 31 May 2018 the US high yield index had 784 issuers, and 576 of them were public (Dynkin p.651). This is one of the other quarter."

"So what's your clock?" Ines asked.

Theo already had a pencil out. At PJT this was the page he would have turned to first. "The revolver. An asset-based loan lends against inventory and receivables, and it comes with an availability test: if what you can still draw falls below a floor, the lenders get control of the cash. That floor is the minimum-liquidity line on my 13-week model. It's the runway covariate of §11.4.2, except here the lenders draw it for you." He tapped the summary. "And the coupon. Eleven percent on \$2.2bn is about \$121mm every six months. Those are the only two clocks this company has that I can see from outside."

Nobody wrote a card on the first date. Ines did not ask for one. "Nothing happens for five months," she said, and turned the page.

**Beat 2: 47.5.** "Friday, 16 May 2025."

The page had one price on it: the 11% secured notes due 2029, quoted at 47.5 (Debtwire, 16 May 2025; a vendor indication, not a TRACE print). Below it, the trade press of that week, which a desk could have read the same morning. A holder group of about 51% of the notes, with Lord Abbett, MacKay Shields, Arena and BlackRock named in the reports and Paul Weiss and Lazard advising, was weighing new financing that could rank ahead of the rest. A \$121mm coupon was due at the end of June. And the flagship store, mortgaged for \$1.25bn, sat in an unrestricted subsidiary, outside the entities whose covenants and collateral the notes could reach (Debtwire, May 2025).

Kaz read the last sentence twice. "Unrestricted," Kaz said, before Theo could open his mouth. "Not released for good behavior. I was told. It means the covenants can't see it."

"It means the collateral can't see it," Theo said. "Which is worse."

Mags had stopped pretending to read her own screen. "A secured bond at 47 and a half, five months after it was issued. Back in my day we didn't have a word for that. We had a look."

#### Decision point: the card at 47.5, 16 May 2025

Ines dealt the cards. "Three things. The date this issuer becomes a 1 in your training set. The feature you wish you'd had on 16 May. And what you do with the bond at 47.5."

They wrote in silence, which on this desk took about four minutes.

Kaz went first, as usual, because Kaz always believed the first answer. *Label: bankruptcy filing. So far, nothing; it's a 0 until a court says otherwise. Feature: equity volatility, which doesn't exist. Bond: hold. The accounting model's PD is 9% (the desk's fictional run), and at 47.5 the bond is pricing far more than that. Cheap.*

Theo's card was neater than usual, which meant he had rewritten it. *Label: the announcement date of whatever exchange is coming, because something is coming, and its terms are the default. Feature: the revolver's availability test, as a time series. Bond: bid only if I can work out what holders outside the 51% get. Today I can't.*

Mags wrote one line in the middle of the card and underlined it. *It defaulted the day the flagship went into the unsub.* Under it, smaller: *Feature: every designation of an unrestricted subsidiary, dated. Bond: sell it to anyone who'll pay 47.5. I'm not in that group, and nobody's going to ask me.*

Ines wrote her own card last, as she always did, and turned it face down. "Before I move the tape," she said, "one question for the table. What did 47.5 know?"

Nobody answered, which was the answer she wanted.

**Beat 3: the exchange.** "Monday, 21 July 2025."

The exchange offer came as a press release with a grid in it, and Theo read it the way he used to read a term sheet at 2 a.m., which is to say twice, the second time with a calculator. Holders were asked to fund \$600mm of new notes issued through a special-purpose vehicle. For every \$1,000 of old notes, a holder who had pre-funded the new money received \$106 of the SPV notes plus \$894 of new second-out notes. A holder who joined the new-money funding later received \$550 of second-out plus \$250 of third-out. A holder who did neither received \$750 of third-out. About 91.9% of holders had already committed, and their consents stripped the old notes' covenants (Saks Global press release, 21 July 2025). S&P cut the issuer from CCC+ to CC the same month, called the deal tantamount to a default, and said it expected to lower the rating to SD or D once the exchange closed (as reported by Retail TouchPoints, July 2025).

Theo drew the new capital structure on the whiteboard as a stack. "A holder who sits it out keeps an old note with no covenants under everything new. A holder who takes the worst option gets 75 cents of face in the third-out, behind the SPV notes and the second-out. Nobody missed a payment. It's a default."

"Selective," said Kaz, writing it next to *selective = ?* from Thursday.

"Selective like Thursday," Theo said. "The issuer chose which lenders got the better seat. Now there's a grid to prove it."

"Friday, 8 August," Ines said. About 98% of the notes had tendered. The issuer's US subsidiary issued \$462.5mm of SPV notes, for \$300mm of cash, along with \$1,439.2mm of second-out and \$440.7mm of third-out notes, and the company put the discount it captured at about \$115mm (Saks Global press release, 8 August 2025). Case trackers put the old notes left outside at only about \$51mm. Around the settlement S&P moved the issuer to selective default (as WWD reported in August 2025), and afterward re-rated it in the CCC category, the rating it would be cut from again in January (Retail Dive).

Kaz looked at the whiteboard for a long time. Kaz's notes on the structural model had a made-up example in them, "\$800mm of new super-priority debt" put ahead of the bonds by a liability management transaction. Here was the real thing: nearly half a billion of new paper and \$1.44bn of second-out ahead of the third-out, which changed what an outside holder would recover without moving anything a structural model could see. "If we'd had a DD, it wouldn't have moved," Kaz said.

"No," Theo said. "That's what Chapter 13's Priming Risk Score is for." He did not re-derive the exchange; Chapter 14 does that, with the arithmetic of who gains and who pays. He drew a second box beside the stack instead: one company, and now four bond lines (the SPV notes, the second-out, the third-out, and the stub of old notes). "In a bond-level panel this is four defaults. If this ends in a courtroom, it's four bankruptcy claims. It's one issuer."

"One issuer, one default," Ines said. "A company with forty-seven bonds is one default, not forty-seven. Fit on bonds and the model learns that defaults happen in big capital structures, which is true and useless."

**Beat 4: the courtroom.** "December 2025."

The last pages went quickly, because by then the company was doing what companies do in the last month: running out. More than \$100mm of interest due on 30 December went unpaid (Bloomberg Law, as reported; one case summary puts the figure at \$126mm). The revolver's minimum-availability covenant, Theo's runway line, was raised from \$200mm to \$375mm on 1 December and to \$500mm on 16 December. S&P cut the issuer to SD again on 7 January 2026, down from CCC (Retail Dive, 8 January 2026). On 13 January 2026 Saks Global filed for Chapter 11 in the Southern District of Texas (No. 26-90103, Judge Alfredo Perez) with about \$3.4bn of funded debt and about \$1.75bn of financing commitments, most of it from an ad hoc group of senior secured bondholders (press accounts differ on the split into tranches and on the pricing). A restructuring support agreement followed on 2 April with \$500mm of exit financing. The plan was confirmed on 5 June 2026: debt cut from about \$3.4bn to about \$1.2bn, the old equity, the 2024 investors' included, cancelled, junior creditors owed about \$1.5bn left with a \$20mm litigation trust, and, by the case trackers' accounts, a class of old notes that voted against the plan crammed down. The company emerged on 26 June 2026 as Exemplar Luxury Group (The Fashion Law case timeline; Financier Worldwide, 9 June 2026).

"Thirteen months from new issue to courtroom," Ines said. "Five from the exchange." She turned over her own card. It said: *Label: the price. Feature: the price. Bond: ask who's selling it to you and why.*

"That's not a model," Kaz said.

"No. It's what your model has to learn to beat."

**Grading the cards.** Kaz's label fired on 13 January 2026, eight months after the bonds traded at 47.5 and five months after the exchange closed. A model trained on that label spends the whole of 2025 learning that this issuer is a survivor, and because 65% of 2025's defaults were exchanges like this one, it learns the same lesson from most of the year's casualties. Kaz's trade, holding a "cheap" bond on a 9% PD, was the trade a hard-default model is built to make, and a holder who simply held ended at the bottom of the stack Theo drew, with a stripped note under everything new, in a case where even the junior creditors, owed about \$1.5bn, were left with a \$20mm trust.

Theo's label fired on 21 July 2025, two months after 47.5 and almost six months before the courtroom. It is codable: an announcement date, a press release, a grid. It is also the date the information existed, which is why the label is stamped at announcement and not at the 8 August settlement; a model that learns from August has learned from news it could not have had in July. His feature, the availability test as a time series, would have shown nothing in May and everything in December, which is a fair description of most liquidity covariates.

Mags's label cannot be coded. Nobody outside the company could have dated the moment the flagship's value left the bondholders' reach, and a label you cannot date is a feeling. But it points at a feature that can be coded: the designation of unrestricted subsidiaries and the investment capacity that allows it, which the basket-parsing of Chapter 25 extracts and the Priming Risk Score of Chapter 13 prices. Her trade, selling at 47.5, was the best card on the table.

Ines graded her own card last, and harshly. The price had known. It had not known *when*, or how, and a desk that sells everything at 47.5 also sells the bonds that come back. That is the jaw of 2003 in the cold open, and the reason the desk builds a PD at all instead of a price screen.

There was one more fact on the last page, and it is the reason the label matters beyond Saks. A distressed exchange is not the end of the story; it is a change of clock. Moody's found that about 46% of 2023's distressed exchanges had already re-defaulted by April 2025, most of them inside a year (Bloomberg Law, 23 April 2025), and its longer study, in the Docket Diary of §11.6.1, puts more than 70% of eventual hard defaults within two years of the soft one. Saks took five months.

Theo put his card back in the folder. "So the purpose of a default label isn't to record the day the company died," he said. "It's to tell the model which day it should have been scared." He looked at the four boxes on the whiteboard. "The label is the model."

The desk label that came out of the replay is *any* of: missed payment beyond grace, bankruptcy filing, distressed exchange, or an LME that impairs the holder (uptier, drop-down with guarantee release, par-reducing exchange), within the horizon, stamped at announcement and counted once per issuer.

### 11.4.4 What machine learning adds, measured honestly

Alanis, Chava and Shah (2022, *Benchmarking Machine Learning Models to Predict Corporate Bankruptcy*, arXiv:2212.12051) run the cleanest horse race available: 2,585 bankruptcies from 1990 to 2019, walk-forward one-year-ahead prediction, out-of-sample AUC. With distance-to-default and industry only, a LASSO logit scores 0.551 while a random forest scores 0.833 and XGBoost 0.837: trees extract the nonlinearity in DD that a linear logit cannot. Adding accounting variables lifts XGBoost to 0.907, adding market variables to 0.916, and macro variables add nothing (0.915). Excess stock returns, idiosyncratic risk, and relative size are the most important features (Shumway's three, twenty years later), and text features from 10-K filings do not improve performance materially. The lesson is not "use XGBoost." It is that the step from a linear DD score to a nonlinear multi-covariate model is worth about 8 points of AUC, and every further idea has to fight for the next half point.

> **Ways This Blows Up.** *Paired samples:* matching each defaulter to a healthy survivor makes the test easy, because "it is easier to tell the difference between a Aaa and a defaulting firm than between a lower-quality firm and a defaulter" (Bohn–Stein p.226). *Look-ahead on filing dates:* a 10-K for fiscal year 2025 is dated 31 December 2025 in most databases and filed in March 2026; lag every accounting feature to its filing date. *Survivorship via exchanges:* bonds that leave the index through a distressed exchange vanish from a bond-return panel, so a backtest built on index constituents never sees the loss. *Forty-seven bonds per issuer:* one issuer, one observation (Chapter 7). *Regime calibration:* a model calibrated on 2010–2019, a benign decade with few hard defaults, deployed into 2026's soft-default regime, ranks well and is calibrated wrong.

The look-ahead item in that box has a cousin that lives in the label rather than the features, and it is usually found by someone who was not looking for it.

**Quant-shop life (fictional composite): what we knew when.** *The shop, Marisol and her colleagues are invented, a composite of a systematic credit asset manager; the AUC figures and counts are illustrative. The Saks dates are the real ones from the scene above.*

Tuesday, 7 July 2026, 9:10 a.m. Marisol had been a data engineer at the shop for fourteen months, long enough to know that the worst emails carry the subject line "Minor methodology update." This one had come from the default-event vendor at 7:48 the previous evening, after everyone had gone home. Effective with the overnight file, `event_date` for distressed exchanges would mean the date an exchange *settled*, not the date it was *announced*, "to align with prevailing market convention," and the full history had been restated to match. The overnight job had rebuilt the issuer-month panel from the new file, as it always did. Nobody had told it not to.

By 9:40 she had the diff: 212 issuers whose events had moved, almost all of them exchanges, almost all of them later by two to eight weeks *(illustrative)*. By 10:20 she had the consequence. The walk-forward AUC of the house hazard model, 0.912 on Monday's report, was 0.904 on Tuesday's.

The 11:00 model review was in the small room with the broken blind. The head of risk had Monday's and Tuesday's one-pagers side by side, and she asked the question risk committees exist to ask: why is this number different from yesterday? Marisol said the model had not changed; the labels had. A portfolio manager asked whether 0.904 was worse. Marisol said it was a different question: Monday's number scored the model against announcement dates and Tuesday's against settlement dates, and until every label said which date it was, neither number meant what the one-pager said it meant. "Which one goes in the board deck?" the head of risk asked. Nobody enjoyed the answer, which was "neither, yet." The meeting ended, as they do, with an action item.

The action item was the afternoon, and it was the least glamorous six hours of her quarter. She added four columns to the event table, `announced_at`, `settled_at`, `source` and `as_of`, and changed the loader so that it never overwrote a row: a restatement became a new row with a new `as_of`, and the old row stayed where it was. She rebuilt the panel from point-in-time snapshots, so that in any backtest month the model saw only the events the shop could have known about at that month-end. She wrote a test that failed if any label carried a date earlier than its `as_of`. At 5:50 she rebuilt Monday's run from Monday's snapshot and got 0.912 back to the third decimal, which was the first time that week anyone could say why a number was what it was. She sent the email at 6:05. It was read on Thursday.

The row she used as her example was Saks Global's. On Monday its exchange was dated July 2025, the month it was announced, which is the month the replay's label says the information existed. On Tuesday it was dated August 2025, when it settled. Nobody at the shop had decided that. A vendor had, at 7:48 p.m.

### Specification for AI Implementation

**Schema.** Panel, one row per `issuer_id`–`month` (int, int): `DD` (float, observed with noise), `runway` (weeks, float in $[0, 13]$), `exret` (monthly excess equity return proxy, decimal), `default_12m` (int 0/1: any default event in months $[t, t+12)$), `de_flag` (int 0/1: that event was a distressed exchange). Rows whose 12-month window extends past the sample end are dropped (censored). Features enter lagged by `lag` months within issuer. Cross-validation folds are issuer-disjoint and time-purged with a 12-month embargo (Chapter 7, §7.7).

The row that moved was Saks's, and the question the head of risk asked at 11:00 (is the new number worse, or only different?) cannot be settled on the real default history, which is small, expensive and full of labeling arguments: it is a poor place to find out whether an estimator, its standard errors and its cross-validation are honest. Every default model looks brilliant the first time someone runs it, and a risk committee that asks "why is the out-of-sample AUC 0.99?" is not paying a compliment; it is asking what leaked. The desk's habit is to build a world where the truth is known, run the whole pipeline through it, and only then point it at the real thing. A flight simulator is not a flight, but it is where you discover that the landing gear is optional.

The listing is that simulator plus the machinery under test. `simulate_hy_universe` builds 600 issuers over 120 months. Each has a latent distance-to-default that mean-reverts around its own level, shaken by an idiosyncratic shock and by one shock common to every issuer, which is what makes defaults cluster. Observed `DD` is the latent value plus noise; `runway` is a random walk capped at 13 weeks and pulled up by healthy DD; `exret` is an equity-return proxy that moves with changes in DD. The true monthly hazard is a logistic function of latent DD and runway, issuers leave the panel when they default, and the 12-month label marks any default in months $[t, t+12)$. About 30% of defaults are tagged as distressed exchanges, and the last twelve months are dropped because their labels are censored. `lag_features` shifts the covariates within issuer. `fit_logit` is Newton–Raphson with step-halving and an issuer-clustered sandwich covariance. `prior_shift` applies the intercept correction of §11.4.2. `auc` is the rank-based Mann–Whitney form, returning NaN when a fold has no defaults. `purged_group_cv` tests each fold on one group of issuers in one block of months and trains only on other issuers whose months sit more than twelve months from that block.

The checks do the arguing. The signs on DD and runway must be negative. Clustering must widen the DD standard error, and it does, by a factor of about 2.8 in the run. Out-of-sample AUC must clear 0.75 and comes in near 0.89. A feature that peeks at the label must produce an AUC above 0.97, to show what leakage looks like. Treating distressed exchanges as survival must cut the average predicted PD below 90% of the true rate.

The harness runs before anyone touches vendor data and again after every pipeline change of the kind Marisol's Tuesday forced. Its AUC is not a forecast of live performance, because the simulator's hazard is logistic by construction. And `lag_features` shifts by *rows*, not calendar months: the simulated panel has no gaps, so it works, while a real panel with a missing month turns a three-month lag into a four-month one, silently.

*The full listing is [Listing 11.3 in Appendix F](#code-11-3).*

**Edge cases for ROBO.** A cross-validation fold with no defaults in its test block has an undefined AUC: skip it and log it, never score it as 0.5. Aggregate bonds to the issuer before fitting. Lag accounting features to the filing date, not the period end. Keep the distressed-exchange flag as a separate column so the label definition can be audited and changed without rebuilding the panel.

## 11.5 Validation: Power Curves and What "77% Within 24 Months" Means

Every systematic HY pitch book contains a sentence like BlackRock's. The sentence is true, and it is also a single point on a curve whose other coordinate is not printed. Ines reads such sentences the way she reads a player who says he won 77% of his showdowns. "Great. How many hands did you fold to get there?"

> **[SOURCE EXTRACTION]** *BlackRock_Systematic_High_Yield_Credit p.6:* "Our proprietary probability of default signal that has underpinned all of our credit strategies for over 20 years has successfully identified 77% of the defaulted bonds in the ICE BofA High Yield Index within 24 months of its default since 2010."
>
> **Annotation.** The footnote dates the statistic (BlackRock and ICE BofA data, as of 31 March 2024, since January 2010), and the same page tells you the model's horizon is a forward 12-month PD built from accounting, equity and bond market data, ratings, and macro variables. Three things are not on the page, and a diligent allocator asks for all three. First, the exclusion rate: what fraction of the index was flagged to catch the 77%? Second, the unit: "defaulted bonds" is a bond count, and a capital structure with 47 bonds counts 47 times. Third, the horizon mismatch: a 12-month PD scored against a 24-month window gets two years to be right. None of this makes the claim weak; a modern PD with an accuracy ratio around 0.7 would produce numbers like this honestly. It makes the claim *incomplete*, and the rest of this section shows how to complete it.

### 11.5.1 CAP, ROC, and an identity worth knowing

To answer Ines's question, a desk needs a way of scoring a ranking that does not depend on where you draw the line, and it turns out there is a version of that score a poker player can price in her head.

> **Math, Gently. AUC is a bet.** Take last year's issuers and put every defaulter in one hat and every survivor in another. Draw one name from each and ask the model which is riskier. If it is right, you win the bet. The *area under the ROC curve*, AUC, is nothing more than the long-run share of those bets the model wins: 0.5 is a coin flip, 1.0 is clairvoyance. You can count it by hand. Suppose four issuers defaulted and ten survived, so there are $4 \times 10 = 40$ possible defaulter-survivor pairs. If the model ranks the defaulter above the survivor in 34 of them, $\text{AUC} = 34/40 = 0.85$. The other score you will meet, the *accuracy ratio*, rescales the same bet so that a coin flip scores zero instead of one-half: $\text{AR} = 2\,\text{AUC} - 1$, so 0.85 becomes $2 \times 0.85 - 1 = 0.70$. A pitch book that says "AR of 0.7" and one that says "AUC of 0.85" are describing the same model. Neither says how much of the index the model throws out to catch its defaults; that is the question Ines asked, and it is the next subsection's. The curves behind the two scores, and why the rescaling is exact, are next.

Sort issuers from riskiest to safest by model score. The cumulative accuracy profile (CAP) plots, for each cutoff, the fraction of *all* issuers flagged ($x$) against the fraction of *defaulters* flagged ($Y(x)$). The ROC curve plots the same defaulter fraction against the fraction of *survivors* flagged ($x'$). With $d$ defaulters among $n$ issuers and base rate $f = d/n$, the accuracy ratio is the area between the model's CAP and the diagonal, divided by the same area for a perfect model:

$$
\text{AR} = \frac{\int_0^1 Y(x)\,dx - \tfrac12}{\tfrac12(1-f)} = \frac{2\int_0^1 Y(x)\,dx - 1}{1-f} .
$$

The area under the ROC is a probability (Bohn–Stein p.410, below): $\text{AUC} = \mathbb{P}(\text{score}_D > \text{score}_{ND})$, the Mann–Whitney statistic. The two measures are not merely related; they are the same number in two units, $\text{AR} = 2\,\text{AUC} - 1$, exactly, for scores without ties, as Engelmann, Hayden and Tasche showed in 2003. Report either. An AR from one universe and an AR from another universe with a different base rate are not comparable, and the difference between them is not skill (Bohn–Stein p.426).

#### The Full Derivation: why AR = 2 AUC − 1

Every step down the sorted list moves $x$ by $1/n$, and $1/n$ splits exactly as $dx = f\,dY + (1-f)\,dx'$, because a defaulter step has $dY = 1/d$ and a survivor step has $dx' = 1/(n-d)$. Integrating $Y$ against both pieces, $\int Y\,dY = \tfrac12$ and $\int Y\,dx' = \text{AUC}$, so

$$
\int_0^1 Y(x)\,dx = \tfrac{f}{2} + (1-f)\,\text{AUC} \quad\Longrightarrow\quad \text{AR} = 2\,\text{AUC} - 1
$$

exactly, for scores without ties. Substitute the first expression into the definition of AR and the $(1-f)$ cancels, which is why the identity does not depend on the base rate even though each curve does.

Bohn and Stein give the bet its formal name.

> **[SOURCE EXTRACTION]** *Bohn_Stein_Active_Credit_Portfolio_Management p.410:* "The quantity A, the area under the ROC, is equivalent to the probability that a randomly chosen defaulting loan will be ranked worse than a randomly chosen nondefaulting loan by a specific model"
>
> **Annotation.** This is the most useful sentence in model validation, because it converts an abstract area into a bet anyone at the desk can price. Pick one defaulter and one survivor at random; AUC is the chance your model ranks them correctly. Alanis, Chava and Shah's 0.916 means the model gets that coin flip right eleven times in twelve. Two cautions. "Randomly chosen" must mean randomly chosen *issuers*, or the 47-bond capital structure turns one correct ranking into 47. And AUC is a ranking statistic, blind to calibration: a model that ranks perfectly and says every PD is 50% scores 1.0 and would destroy you in the credit triangle. Validate power with AUC, calibration with realized-versus-predicted default rates by PD bucket, and do both on issuer-disjoint, time-purged folds.

### 11.5.2 From a hit rate to a return

A ranking score tells you the model is good at the bet. It does not tell you whether acting on the model makes money, because acting on it means throwing names out, and most of the names you throw out were never going to default.

> **Math, Gently. Base rates.** Line up 1,000 issuers in a year when 3% of them default: 30 defaulters and 970 survivors. A good model flags the riskiest 200 and catches 23 of the 30, a 77% hit rate. Now look inside the flagged pile. It holds 23 defaulters and 177 survivors, so a flagged name defaults at $23/200 = 11.5\%$, about four times the base rate and still nowhere near a sure thing. Those 177 survivors are 18% of every survivor in the index, and their carry goes to whoever bought them from you. Make the model sloppier, so that it needs to flag 400 names to catch the same 23, and a flagged name defaults at $23/400 = 5.8\%$, while 377 survivors walk out of the door. When the thing you are hunting is rare, even a sharp test fills its net mostly with the innocent; that is the *base-rate* effect, and Chapter 3 (§3.4.3) met it as a medical test. Whether the trade pays depends on whether 11.5% of a loss beats the spread on 200 names, and the formula that settles it is next.

Let the model exclude a fraction $q$ of the index (set $X$) and keep the rest ($K$, weight $1-q$), and let the defensive portfolio hold $K$ scaled to full weight. Its active return against the index is $r_K - [q\,r_X + (1-q)\,r_K] = q\,(r_K - r_X)$. Apply the credit triangle to each set, $\mathbb{E}^{\mathbb{P}}[r] \approx s - \pi L$ with $\pi$ the set's default rate:

$$
\mathbb{E}^{\mathbb{P}}[r_{\text{active}}] \approx q\Big[(\pi_X - \pi_K)\,L - (s_X - s_K)\Big].
$$

Default avoidance pays if and only if the excluded set's *excess default loss* exceeds its *excess spread*. Now plug in the BlackRock-style claim on a universe with a 3% default rate. If the 77% hit rate came from excluding $q = 20\%$, the flagged set defaults at $\pi_X = 0.77 \times 3\%/0.20 = 11.6\%$ and the kept set at $\pi_K = 0.23 \times 3\%/0.80 = 0.86\%$. With $L = 0.6$ and an excess spread of 420bp in the excluded set, the active return is $0.2 \times (6.41\% - 4.20\%) \approx +44$bp a year. If the same 77% required $q = 40\%$, then $\pi_X = 5.8\%$, $\pi_K = 1.15\%$, and against a 300bp excess spread the active return is $0.4 \times (2.78\% - 3.00\%) \approx -9$bp *(all inputs illustrative)*. Same hit rate, opposite sign. And the base-rate trap is visible in the first case: even the good model flags 17.7% of the index that does not default, which is 18% of all survivors, whose carry you have handed to someone else. Figure 11.4 draws the two cases against one curve.

![Figure 11.4: The same 77% hit rate pays or costs depending on how much of the index it flags: flagging 20% avoids 6.4% a year of default loss for 4.2% of spread given up (+44bp a year), while flagging 40% avoids 2.8% for 3.0% given up (−9bp a year). Illustrative: the §11.5.2 credit-triangle arithmetic with a 3% universe default rate, loss given default 0.6 and the chapter's two excess-spread inputs (420bp at q = 20%, 300bp at q = 40%); the curve holds the hit rate at 77% for every q.](assets/figures/ch11_exclusion_pays.png)

Theo learned where those numbers hide on his first vendor call, three days into the job. The vendor (fictional, and unnamed here because it is a composite of several) had a deck with one number on the cover: its default signal had caught 81% of defaulted bonds in the US high yield index within two years *(illustrative)*. Theo had prepared three questions, the three the BlackRock annotation above says are not on the page, and he asked them in order.

"What fraction of the index did you flag to catch the 81%?"

The line went quiet for long enough that Theo checked the mute button. The sales lead said the exclusion rate was "dynamic." The quant on the call said he would have to check. Theo wrote *q = ?* on his pad and underlined it twice, because the silence was the answer: a vendor who knows that number leads with it.

"Is that 81% of bonds or of issuers?" Bonds, it turned out, and two capital structures with more than forty lines each were in the sample. "And the horizon of the signal?" Twelve months, scored against a twenty-four-month window.

Ines had listened from the next desk with one earbud in. When the call ended she took it out. "Ask them for the curve, not the point. Every point on it is a hit rate." She drew a line on his pad from the bottom-left corner to the top-right. "A model that flags everyone catches 100% of defaults," Ines said. "That is not defense. That is leaving the casino."

> **Trend Watch: The Soft-Default Regime, 2024–2026.** *What changed:* the definition of default drifted from "missed a coupon" toward "agreed to be paid less," and the default rate split by market. *When and how big:* S&P put the US trailing-12-month speculative-grade default rate near 5% at the end of 2024 and put distressed exchanges at well over 60% of defaults in early 2025 *(approx.; S&P reports via search summaries, primary pages not accessed)*. Moody's counted distressed exchanges as 65% of all corporate defaults in 2025 and put the average forward one-year PD for US high yield companies at 3.2% in Q1 2026 (Moody's Analytics, 18 May 2026). Fitch forecast 2026 default rates of 2.5–3.0% for US high yield and 4.5–5.0% for US leveraged loans (Investment Executive, 3 December 2025), and its US private credit default rate hit a record 6% in April 2026 (The DESK, 27 May 2026). UBS put the 2025 USD HY default expectation at 4.8%, but 3.1% excluding two large distressed capital structures (UBS AM, 17 January 2025). *What it means for the desk:* a par-weighted default rate is driven by a handful of large names, so breadth beats tier; private credit is now the leading indicator for the public CCC tier; and any PD model trained on hard defaults alone is calibrated to a world in which two-thirds of today's defaults would have counted as survival.

### Specification for AI Implementation

**Schema.** `score`: float array, higher means riskier (a PD). `default`: int 0/1 array, issuer-level, aligned. `q`: exclusion fraction in $(0,1)$. Outputs: CAP points, AUC, AR, hit rate $\text{HR}(q) = Y(q)$, and the active-return decomposition.

The number missing from the vendor's cover was `q`, and the listing is built so that it can never be missing again. A 77% hit rate that required flagging a fifth of the index is a good model; the same 77% after flagging two-fifths is a good model that loses money, so the automation does not report the hit rate as a loose number. It makes the exclusion fraction `q` a required argument, puts the CAP curve and its summary statistics next to it, and ends in the one line the portfolio manager actually cares about, which is basis points per year.

The listing has four small functions. `cap_curve` sorts the issuers from riskiest score to safest, using a stable sort, and returns the cumulative share of names screened against the cumulative share of defaults caught, starting at the origin; it raises if the sample contains no defaults. `accuracy_ratio` integrates that curve by the trapezoid rule and normalizes it to $(2A - 1)/(1 - f)$, where $f$ is the sample default rate, so that a perfect ranking scores 1 and a coin flip scores about 0. `hit_rate` reads the curve at a chosen `q` by linear interpolation. `exclusion_active_return` is the formula of §11.5.2: the excluded fraction times the excess default loss of the flagged set net of its excess spread, with everything in decimals per year under $\mathbb{P}$.

The checks prove three things. The accuracy ratio equals $2\,\text{AUC} - 1$ to ten decimals on untied scores, which ties the CAP language to the AUC of Listing 11.3. A perfect ranking scores 1, and random scores average within 0.05 of zero over twenty seeds. And the worked example reproduces the sign flip: $+44$bp at $q = 20\%$ and $-9$bp at $q = 40\%$ for the same 77% hit rate. Applied to the in-sample panel from Listing 11.3, it prints an accuracy ratio of 0.773 and hit rates of 60%, 84% and 90% at 10%, 20% and 30%.

The listing's job is to turn a validation claim into money before anyone argues about the model, and that printed panel result is not validation: it is in-sample, and its rows are issuer-months with overlapping twelve-month labels, so one default is counted in up to twelve rows. Ties are the quieter trap. The stable sort breaks them by input order, so a score with a capped PD or a twenty-notch rating produces a CAP that moves when you re-sort the table, while the AUC, which gives ties half credit, does not. Aggregate to issuers first, and keep the exclusion arithmetic honest: it is a first-order credit-triangle approximation that assumes the excluded and kept sets differ only in default rate and spread.

*The full listing is [Listing 11.4 in Appendix F](#code-11-4).*

**Edge cases for ROBO.** Tied scores (a capped PD, or a rating-based score with 20 notches) make the CAP depend on sort order; break ties by averaging, or report the AUC, which the rank formula already tie-corrects. Score at the issuer level. State the horizon of the score and the horizon of the hit window in the output, and refuse to compare them when they differ.

## 11.6 The CCC Problem

The tier where all of this is tested is the one wearing the necktie.

"CCC is where the defaults live and where the rallies live," Mags said, "which is the same sentence." She meant that the tier's return is a bet on which of its members survive, and that both the 2000 disaster and the 2003 rally were the same population answering the same question differently.

The tier is also the index's risk budget. Wellington put CCC-rated bonds at 13% of the high yield index in a note dated 30 September 2026, and Loomis Sayles found that at year-end 2024 CCCs accounted for nearly 25% of the index's OAS. A tier that is an eighth of the market value and a quarter of the spread is where most of the index's credit risk is concentrated, and where any defensive strategy will place most of its bets, whether it means to or not.

### 11.6.1 Why tier exclusion is the wrong tool

Mags kept a photocopy of one row of a transition matrix in her desk drawer, the way other people keep a photograph of their children. She read it aloud to Theo after the Saks folder was closed, as if it were the replay's epilogue. "S&P, 1980 to 2002, the CCC row" (Schmid p.28). "Default within a year: 31.58%. Still CCC a year later: 55.82%." She put the paper down. "Everybody reads the first number. The second one is the business. More than half of them are sitting right where they were a year later, collecting." The tier is sticky: a CCC bond is usually still a CCC bond twelve months on, clipping its coupon.

The number that had surprised her came in 2004, when CSFB's study of default rates by rating *at issuance* for 1993–2003 crossed her desk (Moyer p.44 reprints it): B at 4.23%, CCC at 4.28%. "Almost identical. I'd spent eight years pricing new-issue CCCs as if they were fallen ones." Moyer flags the same result with mild surprise. The rating at issuance separates CCC from B much less than the rating after a downgrade does, because a newly issued CCC has fresh money and a fallen CCC has a problem. The third thing she knew without a table, though Schmid has one (p.103, the expansion and recession recoveries of §11.1.2): recoveries are cyclical, so the same CCC default costs more in a recession, exactly when the tier's spread is widest. Three facts, and each one is a reason not to treat CCC as one asset.

The structure of the right tool follows from Bolder.

> **[SOURCE EXTRACTION]** *Bolder_Credit_Risk_Modelling p.324:* "if a credit counterparty has a large default probability, then much of its inherent default risk is idiosyncratic and, as such, it is less highly correlated with other credit counterparties. Conversely, very low risk counterparties predominately face systematic risk"
>
> **Annotation.** Bolder is explaining why the Basel IRB asset correlation falls as PD rises, from 0.24 for the safest obligors toward 0.12 for the riskiest. The insight for a CCC book is that high-PD risk diversifies. A CCC company defaults mostly because of *its own* problems (a maturity wall, a lost contract, a sponsor that stopped writing checks), and those problems are largely uncorrelated with the next CCC company's. That is the formal case for breadth: 150 CCC issuers at 0.1% each are a far safer bucket than 15 at 1% each, even with the same average PD, because the idiosyncratic part of the default variance shrinks as $1/n$. It is also why the BB tier is the place to fear the cycle: its rare defaults arrive together. A systematic desk takes the opposite of the instinctive position: concentrated and careful in BB, broad and quantitative in CCC.

Sizing by expected loss rather than by fear then becomes a one-line rule. Set an annual expected-loss budget $\text{EL}^{\max}$ for the portfolio (for example 1.0%, illustrative). Fill the CCC bucket in descending order of default-adjusted carry per unit of risk, $(s_i - \hat\lambda_i L_i)/\text{DTS}_i$, subject to

$$
\sum_{i \in \text{CCC}} w_i\,\hat\lambda_i\,L_i \;\le\; \text{EL}^{\max} - \sum_{i \notin \text{CCC}} w_i\,\hat\lambda_i\,L_i, \qquad w_i \le w^{\max}_{\text{issuer}} .
$$

The bucket's size is an *output*: large when the model finds CCC names whose spread overpays their PD, small when the tier's spread is all default. There is no 5% CCC limit in the rule.

That alarmed the risk committee the first time Theo presented it *(a fictional committee; the cap and the slide are illustrative)*. The chair, a former bank credit officer, found the gap in the slide in about four seconds. "Where's the CCC limit?"

"There isn't one," Theo said. "There's a budget for expected loss. The CCC bucket gets whatever the BBs and Bs leave of it."

He put up the second slide: no single issuer above 0.5% of the book, so the worst single CCC default, at a recession-sized loss, costs the portfolio about a third of a percent. "That's the limit," he said. "It's per person, not per crowd."

"And if recoveries do what they did in 2000?"

Theo had expected that one. The loss inputs already used the recession recovery from §11.1.2, not the 40% convention, so a 2000-style year was inside the budget rather than on top of it. "Then the bucket shrinks, because the rule shrinks it. When the tier's spread is all default, there's nothing left in the budget to spend there."

The chair wrote something down. Nobody on the desk could tell whether that was good, which, Ines said afterward, is how you know a risk committee is working.

One flow fact belongs next to the model. Most CLOs face a limit of roughly 7.5% on CCC assets, above which the excess is carried at the lower of market value and par in the overcollateralization tests (Chapter 21). A wave of downgrades into CCC therefore produces forced sellers who care about rating, not PD. When the model says "avoid" and the seller is a CLO manager defending an OC test, the open question is whether the model is seeing distress or seeing the flow. Ines put it more simply: "When someone *has* to fold, buy their chips."

> **View From Another Seat. The CLO manager.** *A generic seat, not any one firm; the facts are cited.* The CLO manager looks at the same CCC loan Theo's model is pricing and asks a different question. Not "what is its PD?" but "does owning it keep my deal inside its numbers?" A reinvesting CLO lives inside about seven of them: the CCC basket, the senior and junior overcollateralization tests, the interest-coverage test, the weighted-average rating factor, the weighted-average spread and the diversity score. A downgrade to CCC can hit several at once. Breaching the basket is common; failing the test it feeds is not. Across S&P's index of 554 reinvesting US broadly syndicated CLOs in 2023, 42% had CCC exposure above the 7.5% threshold, but just over 1% were failing their junior OC test (S&P Global Ratings, CLO Insights, 29 September 2023). The few close to the edge are the ones that sell: Elkamhi and Nozawa (*Journal of Financial Economics* 146, 2022) find that CLOs with little OC slack are significantly more likely to sell loans downgraded to CCC within three months, and that the prices of those loans fall temporarily. Vintage is a state variable. In April 2025 S&P put pre-pandemic reinvesting CLOs at an average junior OC cushion of 2.76% and a CCC basket of 7.08%, against 3.94% and 5.70% for post-pandemic deals (CLO Insights, 29 April 2025). And the rule picks which loan gets sold. Excess CCCs are haircut at the prices of the cheapest CCCs in the pool, so a manager over the limit helps its test most by selling a *higher*-priced CCC: Kundu (ESRB Working Paper 141, 2023) finds the average CCC loan priced at 85 while the cheapest CCC in each CLO averages 58. From this seat a CCC loan at 85 with a low PD is a problem to be solved by Friday, and the systematic desk buying it is buying exactly the loan the rule told the CLO to sell.

Not every soft default ends in a forced sale, and the ones that do not have a long tail of their own, which Moody's has now measured.

> **Docket Diary. After the soft default, 1979–2026.** Moody's Analytics studied 1,173 borrowers that went through a distressed exchange or similar soft credit event between 1979 and 2026 (Moody's Analytics, David Hamilton, *Lend, extend, and then…*, 18 May 2026). Roughly two-thirds avoided a hard default or a repeat event within a decade; about one in four ended in a hard default; and more than 70% of eventual hard defaults following a distressed restructuring occurred within the first two years. The same note puts Moody's private credit default proxy at 1.6% excluding distressed exchanges and 4.7% including them. *For the model:* an LME is not the end of the story; it resets the hazard clock to a higher level for about 24 months, and "months since last LME" belongs in the feature set. *The Ad Hoc Group, represented by counsel:* "The transaction was value-maximizing for all stakeholders who were invited."

### 11.6.2 Case Study: The 2026 CCC Decompression

Friday, 16 October 2026, 8:15 a.m., before the replay. Theo had the Post-it on his bezel and three years of FRED on his screen, which is all FRED now serves, and he was trying to answer the first question on the Post-it with the second monitor instead of the first.

On 15 October 2026 the ICE BofA US High Yield OAS closed at 323bp, BB at 197bp, single-B at 326bp, and CCC & lower at 1,278bp, one day after a three-year high of 1,282bp (FRED series BAMLH0A0HYM2, BAMLH0A1HYBB, BAMLH0A2HYB, BAMLH0A3HYC). On 17 October 2023, the first day of the window, the CCC spread had been 2.28 times the index's. The ratio of CCC OAS to index OAS, using month-end values, went from 2.61 in January 2025 to 2.54 in April 2025 (the tariff shock widened everything, so the ratio briefly *compressed*), then 3.15 in December 2025, 3.53 in June 2026, and 3.96 in August and October 2026 *(our computation from FRED)*. The index is calm because it is mostly double-B and short: State Street's global high yield universe was 62% BB-rated with a 3.1-year duration at year-end 2025, and Nuveen puts the BB share of the US index at 51% at year-end 2024, against 37% in 2004 (Nuveen p.4). The tier is not calm. Figure 11.5 shows the tiers and the ratio.

![Figure 11.5: The index and the single-B tier sit near 325bp while CCC & lower has decoupled to 1,278bp, so the ratio of CCC spread to index spread has climbed from 2.61 in January 2025 to 3.96 in October 2026, after compressing briefly in the April 2025 tariff shock. Source: FRED series BAMLH0A0HYM2 (index), BAMLH0A1HYBB (BB), BAMLH0A2HYB (B) and BAMLH0A3HYC (CCC & lower), ICE BofA US High Yield indices, daily, 17 October 2023 to 15 October 2026 (the three-year window FRED serves); the ratio uses month-end values, with October 2026 the 15 October close (our computation).](assets/figures/ch11_tier_oas.png)

Theo then did the thing the Post-it was really asking for, which was to separate a calmer market from a different one. Regressing the index's daily total return on its three rating buckets' returns over a rolling 126 days gives the weights the index is behaving as if it holds: BB/B/CCC of 53.4/34.0/12.6% in December 2024 and 60.1/31.8/8.1% on 15 October 2026 *(our regression estimate, not an ICE weight; reported CCC shares depend on the index definition, from Wellington's 13% in §11.6's opening to 7.35% in the iBoxx index behind HYG on 15 October 2026, per iShares)*. Hold the December 2024 weights fixed and the index's 15 October spread would have been about 377bp instead of 323bp *(our computation)*. Roughly 54bp of the headline calm was not calm at all. It was the CCCs leaving the room, by default, by exchange and by downgrade out of the index, and the BBs taking their seats.

The backdrop is a private credit default rate at a Fitch record of 6% in April 2026, distressed exchanges at 94% of downgrades to default or selective default in the twelve months to February 2026 by a rating-agency count reported in The DESK (27 May 2026), and Morgan Stanley forecasting high yield defaults of 3.5%. Any story about *why* the tier decompressed (software issuers facing AI disruption, private-credit stress spilling into public CCC capital structures) is interpretation, and we label it so.

How three desks would have traded it *(illustrative)*. The tier excluder sold its CCCs in 2025 and looks brilliant in October 2026; its exposure to a 2003-style rebound is zero, and if the rebound comes, it will look exactly as brilliant as Mags's friends who sat out 2003. The beta-tilter held 90% of everything, including the 10% of CCC names that will default, and earned 90% of a bad year. The PD-ranked selector excluded the CCC names whose model PD exceeded their spread-implied break-even (§11.1.2), kept the CCCs whose spread overpaid their PD (often the sticky, newly issued, sponsor-supported ones), sized the bucket by expected loss, and used the 2026 widening to *add* to survivors as their spreads crossed the break-even line. Only the third desk has a plan for the rebound.

Mags read the three-desks note over Theo's shoulder and said the first desk was not the only one selling. "Somebody big said on a podcast yesterday they're the most defensive they've been in thirty years. They're not wrong. They're just answering a different question."

> **View From Another Seat. The large active fixed-income manager.** *A real firm's publicly stated view, quoted from the published episode description; nothing beyond those words is attributed to it.* On the day of the bow tie, Bloomberg Intelligence's *The Credit Edge* released an episode with Bryan Whalen, chief investment officer of TCW's \$160 billion fixed-income group, which, the description says, "has slashed credit risk to the lowest in three decades amid valuation and contagion concerns." Whalen's reasoning runs down the ratings ladder: CCCs are "the weakest borrower, and they cry uncle first," and "your single B borrower is going to feel it next, and then your double B borrowers" (*The Credit Edge*, 15 October 2026). That is the top-down seat. It holds a view on valuation and on contagion, expresses it by cutting the whole risk budget, and is judged on whether the contagion arrives and how far up the ladder it climbs. The systematic seat of this chapter starts from the other end. It needs no view on whether contagion arrives, because it sizes each CCC by expected loss against its own spread and lets the bucket shrink or grow name by name; its bet is that the tier is a crowd whose members will not all cry uncle on the same day. The two seats can both be right. If the ladder runs the way Whalen describes, the top-down seat is out early and the expected-loss budget does the same shrinking later and more slowly. If the tier stays decoupled from the index, as it has for a year, the systematic seat keeps the survivors' carry and the top-down seat keeps its powder dry for the 2003 jaw.

Across town, on a platform the desk knew only through its RFQs, a pod met the decompression from the short side, because the bond it was short had just started trading like a member of the crowd.

> **The Pair.** *Pair Book entry PB-01, Dov Adler's Kestrel/Halvorsen pair (Chapter 1-B, box 1B-1), stressed by the CCC problem on Friday 16 October 2026. Dov's pod and its platform are fictional composites, Kestrel Roofing is invented and Halvorsen is the book's fictional issuer; positions, prices, scenario and P&L are illustrative. The tier spreads are FRED's.* **Thesis.** Unchanged since April: two single-B building-products credits on one housing cycle, one with covenant room, one with a 2027 revolver and an aggressive sponsor. **Legs.** Long \$60mm Kestrel 6% 2030 at 96 (350bp, spread duration 3.6); short Halvorsen 7.25% 2029, cut to \$35mm face in Tuesday's trim and paired with a small CDX HY sale (Chapter 1-B). Halvorsen is still rated B3, but at about 1,400bp it trades wider than the whole CCC tier's 1,278: the market moved it into the necktie before the agencies did. **What the hedge removes.** The market, measured in DTS. The platform's risk manager asked Dov for the pair after the agencies catch up, so he ran the bonds to 74 and about 1,650bp at a spread duration of 2.3. Halvorsen's DTS per dollar of market value becomes $2.3 \times 1{,}650 = 3{,}795$, three times Kestrel's $3.6 \times 350 = 1{,}260$, so matching the long's $60 \times 0.96 \times 3.6 \times 350 \approx 72{,}600$ needs a short of about \$19mm of market value, \$26mm of face: a third of the long's \$57.6mm. **What idio remains.** Quality within one cycle: Kestrel's documents against Halvorsen's. **What leaks.** Everything a DTS ruler cannot see across buckets. At a recovery of 40, a Kestrel default still costs \$33.6mm, while a Halvorsen default now pays only $26 \times (0.74 - 0.40) \approx \$8.8$mm. The pair is a long with a hat on: matched in beta, unmatched in jump, and the short is too small to earn enough on the very default the thesis predicts. The short leg also now carries the CCC tier's own factor, the ratio that went from 2.28 to 3.96 in three years; a 2003-style CCC rally hits it and not the B-rated long. And an exchange offered at a premium would gap the short *up* (Chapter 14). **What it costs** *(illustrative)*. Carry: \$3.6mm a year of Kestrel coupon against \$1.9mm owed on a \$26mm Halvorsen short, and a pair that pays to hold is the first tell that it is a long. Borrow: the fee on the short is starting to climb as other pods find the same CCC short (Chapter 22 follows it). Financing the long net of the short's cash rebate: about \$0.3mm a year. Half-spreads: re-trimming pays three-quarters of a point on Halvorsen in a lender-call week, about \$70,000 on \$9mm of face, and the eventual exit adds a quarter-point on Kestrel's \$60mm, \$150,000, which over a six-month horizon annualizes to about \$0.44mm of friction on the two legs together. **Dov's note on the ledger.** "DTS-neutral is not jump-neutral across buckets. Keep the default leg sized by recovery, accept the beta residue in CDX, and say so." Chapter 8-D (§8D.3) compares the rulers; the default-matched sizing is Chapter 3-B's jump-to-default hedge.

Theo, who saw the pair only as two RFQs from a pod on the other side of his screen, would have recognized the shape. It was §11.2's dimmer switch with the knob on the short leg instead of the long: a position that looked hedged on the slide and was a bet on the crowd underneath.

## 11.7 Quality and Low-Risk Tilts

Kaz had a theory, delivered with the serenity of someone who has never read a credit agreement. "The low-volatility anomaly is just leverage aversion. Investors who can't borrow buy risky assets to get return, so risky assets are overpriced and safe ones are cheap. Frazzini and Pedersen. Done."

"In equities," Theo said. "In high yield the risky assets also have a lawyer."

Both are right. Frazzini and Pedersen (2014) find alphas declining in beta across equities, Treasuries, credit, and futures; Houweling and van Zundert (2017) define the credit low-risk factor as short maturity and high rating and find significant alpha. Kaz's story explains why the effect exists everywhere. Theo's explains why it is *stronger* in high yield: the riskiest bonds carry jump risk that their spreads systematically underprice relative to their volatility, which is the asymmetry of §11.1 showing up in the cross-section.

> **[SOURCE EXTRACTION]** *Dynkin_Systematic_Investing_in_Credit p.59:* "two in particular are responsible for the majority of credit return outperformance over the replicating portfolio: equity and bond volatility risk premia (VRP) and the low risk anomaly."
>
> **Annotation.** Dynkin and coauthors decompose credit returns against a replicating portfolio of equities and Treasuries and ask what is left that only credit pays. Two things: selling volatility, and the low-risk anomaly. Read that as a job description for defensive HY. The VRP part is the short put you cannot avoid owning; the low-risk part is the one premium you can harvest *by being defensive*, which is why a well-built defensive book need not be a lower-return book. Dynkin p.95 adds the maturity version ("Short-maturity bonds had better risk-adjusted and even non-risk-adjusted performance than long-maturity bonds"). The 2026 caveat: the HY index is now majority BB and short, so the low-risk trade is crowded at exactly the front end where it lives. Measure your low-risk exposure relative to the index, not in absolute terms.

### 11.7.1 Why low risk wins, in one line of DTS

Theo's line about lawyers can be made exact with one tool the book has already built. DTS, duration times spread, is a bond's spread duration multiplied by its spread, the right ruler for credit risk because spreads tend to move in percent of their level rather than in basis points (Chapter 8, §8.4, builds it and has the Math, Gently box). Ben Dor's DTS framework rests on a Merton result: spread volatility is nearly proportional to spread (Ben Dor p.104), $\sigma(\Delta s_i) \approx k\,s_i$. A bond's excess-return volatility is then $D^{\text{spr}}_i\,k\,s_i = k\,\text{DTS}_i$. Divide the credit triangle by it:

$$
\frac{\mathbb{E}^{\mathbb{P}}[r^{xs}_i]}{\sigma(r^{xs}_i)} \approx \frac{s_i - \lambda_i L_i}{k\,D^{\text{spr}}_i\,s_i} = \frac{1}{k\,D^{\text{spr}}_i}\left(1 - \frac{\lambda_i L_i}{s_i}\right).
$$

Two predictions drop out. Risk-adjusted return falls with spread duration, even though the spread curve slopes upward: Dynkin's finding that information ratios decline with maturity (Dynkin p.454–457). And it falls as the share of the spread that is expected loss, $\lambda_i L_i/s_i$, rises. On the 1980–2002 default table at October 2026 spreads with $L = 0.6$, that share is 0.47 for BB, 1.28 for B, and 1.48 for CCC *(our computation; the historical table is pessimistic, as §11.1.2 showed)*: rising down the rating scale under any default table you choose. Low risk is not an anomaly in this framing; it is the credit triangle divided by DTS.

### 11.7.2 The long-only contradiction, and three ways out

The textbook betting-against-beta portfolio in credit levers the low-risk leg and delevers the high-risk leg to equal DTS:

$$
r^{\text{BAB}}_t = \frac{\text{DTS}_{\text{mkt}}}{\text{DTS}_L}\,r^{xs}_{L,t} - \frac{\text{DTS}_{\text{mkt}}}{\text{DTS}_H}\,r^{xs}_{H,t} .
$$

A long-only HY fund cannot short and is usually forbidden to lever. Tilt it toward short, high-rated bonds on a market-value basis and its DTS falls below the benchmark's, which means its beta falls, which means you have rebuilt the dimmer switch and called it a factor. "IDO or it didn't happen," Ines said, looking at a market-value-neutral backtest with a beta of 0.85 and a beautiful Sharpe ratio. Run DTS-neutral, the alpha halved. "And half of it didn't."

Nobody wanted to be the one who had built the dimmer switch, so everyone at the screen proposed a way out of it.

Kaz went first. "Overlay. Keep the low-risk book and buy back the missing DTS with CDX HY or a total-return swap on the index" (Chapter 8). "Beta goes back to one, the fifteen points of missing beta cost a few basis points a year *(illustrative)*, and what's left in the active book is pure selection."

"The mandate says no derivatives," Theo said. "So don't buy the beta back. Re-spend it. Keep the DTS budget equal to the benchmark's, but spend it on the spread of *low-PD* issuers: longer maturities of good BB and B credits. You give up some of the maturity effect, and in exchange you stay away from the default tail."

Mags had a third answer, the one nobody in a pitch meeting ever gives. "Or accept the beta and say so in the factsheet. In type a client can read without glasses. People who want 0.85 exist. They should know that's what they're paying for."

Ines let all three sit there for a moment. "All honest. All with the same hole in them." She quoted it from memory, the way she quoted pot odds: "If we make a mistake of 5% in the expected return forecast on a low-volatility stock, we pay a much higher cost than if we make the same mistake on the high-volatility one" (Paleologo p.99). Risk-based sizing puts the most weight where a forecast error costs the most. Kaz's overlay levers up the safest names, Theo's re-spend crowds into the BBs that look safest, and even Mags's honest factsheet portfolio is heaviest in the names the model is surest about. "Cap issuer weights," Ines said. "Then pick whichever exit your client can read."

Part of the reason the safe end is crowded is that some of the people standing in it are not there for the low-risk premium at all.

> **View From Another Seat. The life insurer.** *A generic seat; the rules are cited, and no firm's view is implied.* A life insurer writing annuities holds bonds to maturity against fixed liabilities, and the constraint that binds it is risk-based capital. Every bond carries a capital charge set by its NAIC designation, and the charge steps up as the rating falls, so the question at the investment committee is spread per unit of capital charge, not spread per unit of DTS. On that ruler a bond near the investment-grade line can beat a single-B with more spread, and a BBB− private placement at T+250 with a clean designation can beat a BB public bond at T+300 *(illustrative)*. The seat is patient in a way a mutual fund is not: it does not sell because a bond moved five points. It sells when a downgrade, a designation change or a rule change raises the charge, and the rules move. In June 2026 the NAIC adopted new C-1 capital factors for CLO tranches, based on rating plus tranche thickness and effective with year-end 2026 capital, including an 11.77% pretax surcharge on below-investment-grade broadly syndicated CLO tranches 4% thick or thinner (Sidley, 9 July 2026). For a defensive high yield desk the seat matters twice. Its demand is part of what makes the safest high yield bonds expensive, so the low-risk premium is thinnest where the capital-driven buyers shop. And its selling is discontinuous: a fallen angel or a designation change produces flow that has nothing to do with PD, which is the chapter's forced-seller opportunity seen from the seller's chair.

The insurer's ruler and the desk's ruler disagree most about one family of signals, the ones that look defensive because of what they quietly hold.

Equity momentum belongs here too, because it is a default-avoidance signal in disguise. Dynkin reports a top-minus-bottom quintile return of 15.9% a year with an information ratio of 1.74 for equity momentum in HY credit over January 1993 to May 2017, and calls it "a highly informative signal for lower quality names" (Dynkin p.609).

> **[SOURCE EXTRACTION]** *Dynkin_Systematic_Investing_in_Credit p.739:* "top‐EMC portfolios tend to have lower credit exposures than their bottom counterparts during volatile episodes when safer, low‐OAS issuers tend to have less negative equity momentum."
>
> **Annotation.** This is the trap inside the good signal. Equity momentum in credit (EMC) works in drawdowns partly because, in a selloff, the stocks that fall least belong to the safest issuers, so a top-EMC portfolio quietly becomes a low-beta portfolio exactly when beta is being punished. Some of its "alpha" in 2008 or March 2020 is the dimmer switch again. Dynkin's remedy is to match the long and short legs on DTS so that the signal is measured net of its credit exposure, and the same page reports that EMC and its companion signal still work in drawdowns once matched. For a defensive HY book the lesson is procedural: every defensive signal must be tested DTS-neutral before it is credited with skill, or you will pay active fees for a beta you could have bought for two basis points.

### Specification for AI Implementation

**The Spec You Hand the Robot.** "Exclude the worst PD quintile, tilt toward default-adjusted carry per unit of DTS, hold $w^\top\text{DTS}$ within 1% of the benchmark, long-only, fully invested, issuer cap 3%." **Schema.** One cross-section: `pd_hat` (12m PD, decimal), `spread` (OAS, decimal), `dur` ($D^{\text{spr}}$, years), `bench_w` (sums to 1). Defaulted issuers enter with DTS set to zero and are excluded before optimization. Output: weights `w` (same order), `keep` mask, solver result.

A PD model hands the portfolio manager a ranking and, on its own, nothing else. The tempting next step is to drop the worst names, tilt toward the best, and send the backtest to marketing. That portfolio is built from short, high-rated, low-spread bonds, so its DTS sits well below the benchmark's, its beta follows, and the Sharpe ratio that made everyone smile is the dimmer switch from §11.2 with a better wardrobe. Ines's "IDO or it didn't happen" has to be a property of the construction code, not a footnote to the backtest. And since the PDs refresh every night for a thousand-odd issuers, the construction has to run unattended, which means it has to know when to refuse.

`defensive_portfolio` takes a cross-section of PDs, spreads, spread durations and benchmark weights, and works in six steps. It computes each issuer's DTS as duration times spread, and the benchmark's DTS as the weighted sum over the full universe. It excludes the issuers above the 80th percentile of PD, the worst fifth by default. It scores the survivors by default-adjusted carry per unit of DTS, spread minus PD times loss given default, divided by DTS, which is the credit triangle of §11.1.2 divided by the risk budget. It standardizes those scores, clips them at two standard deviations, and tilts the benchmark weights by the exponential of the clipped score, giving the market-value tilt `w0`. It checks that the benchmark's DTS lies between the smallest and largest DTS among the survivors and raises if it does not. Finally, SLSQP finds the weights closest to `w0` in squared distance that sum to one, hold exactly the benchmark's DTS, and sit between zero and the issuer cap of 3%. It returns the weights, the mask, `w0` and the DTS vectors.

The part to notice is the gap between `w0` and the final weights. The benchmark's DTS includes the excluded names, the widest ones, so the survivors must carry more DTS per dollar than they would on their own. That gap is the DTS budget being re-spent on low-PD names with long maturities, the second exit of §11.7.2. The demo runs five cross-sections from the Listing 11.3 panel and asserts that the final book is DTS-neutral within 1%, long-only, fully invested and empty in the excluded set, that `w0` alone falls below 95% of the benchmark's DTS, and that the held book carries fewer realized defaults than the benchmark, in-sample, since the model was fitted on the same panel. By default each cross-section is a systematic sample of 100 issuers (every fourth or fifth, by id), so the whole block runs in well under half a minute; the full cross-sections hold 480 to 550 issuers, and SLSQP then takes minutes per date, which is what `FULL_GRID = True` buys. A sample cannot shrink much further: at 80 issuers the 3% cap and the DTS target conflict, and the assertions fail, which is the feasibility failure described below.

The construction is for the case where the benchmark is the mandate and beta is not for sale. It does nothing for turnover, because the objective pulls toward `w0`, not toward yesterday's book. Feasibility is where it can fail without saying so. The range check passes whenever the benchmark's DTS sits between the survivors' extremes, but it ignores the 3% issuer cap, so the solver can still fail inside that range. The function never inspects the solver's status and returns whatever the last iterate was. The demo's assertions on the output catch this; a production job must check the status and the realized DTS ratio before it trades.

*The full listing is [Listing 11.5 in Appendix F](#code-11-5).*

**Edge cases for ROBO.** If the benchmark DTS cannot be reached long-only within issuer caps, raise; never "solve" it with negative weights or leverage. Recompute DTS after every spread update; a bond that has defaulted carries zero DTS, or a 5,000bp spread will dominate the neutrality constraint. Turnover: penalize changes from yesterday's weights, not from the benchmark, in production.

## 11.8 Defense Without Sacrificing Offense: Regime-Aware Exposure

BlackRock's paper says the quiet part plainly: "it is not always prudent to be looking for safety, irrespective of the macro-economic environment" (BlackRock p.6). Blackstone's systematic credit book describes contrarian rebalancing when spreads widen without fundamental deterioration (Blackstone p.1). Both are describing the second source of convexity from §11.2.2: adding risk when the market overpays for it.

The signal is the gap between the spread the market charges and the spread the PD justifies. Let $\hat s_i = s_0 + m\,\widehat{\text{PD}}_i\,L_i$ be a model spread (expected loss times a risk-premium multiple $m$, plus a liquidity floor $s_0$), and define the residual and its DTS-weighted aggregate

$$
z_i = \ln\frac{s_i}{\hat s_i}, \qquad \bar z_t = \frac{\sum_i w_i\,\text{DTS}_i\,z_i}{\sum_i w_i\,\text{DTS}_i} .
$$

The portfolio's DTS target scales with the residual relative to its own history, bounded:

$$
\text{DTS}^{\text{target}}_t = \text{DTS}^{\text{bench}}_t \cdot \operatorname{clip}\!\big(1 + \kappa(\bar z_t - \bar z^{\text{ref}}),\; 0.9,\; 1.2\big), \qquad \text{DTS}^{\text{target}}_t \le \text{DTS}^{\max}_t ,
$$

where $\text{DTS}^{\max}_t$ is the largest DTS a long-only, capped portfolio can hold: the no-leverage guard. If spreads and PDs widen together, $z_i$ is unchanged and the budget stays at one. If spreads gap while PDs sit still, $\bar z$ jumps and the budget rises.

### 11.8.1 Case Study: The April 2025 Tariff Shock, a Ten-Week V

#### Long Scene: Ten weeks in 2025, replayed blind

*A replay, Ines's ritual, run on Friday 16 October 2026 with the tape cut at the close of Monday 7 April 2025. The cast, their cards, the desk's books and every word they say are invented, and the desk's DTS multipliers and P&L are illustrative. The spreads are ICE BofA closes from FRED, the index returns are our computations from the FRED total-return series, the ETF premiums are iShares's published history and the trading volumes are FINRA's monthly TRACE reports, each cited where it appears.*

At 4:30, with the Saks folder closed and Mags's photocopy back in its drawer, Ines produced a second folder. It was thinner. "The Post-it has three questions," she said. "Saks was the first. This is the third: what you do when they rally. The trouble with the third question is that you never know you're being asked it until afterward."

**Beat 1: the floor.** She started in January. On Wednesday 22 January 2025 the high yield index OAS closed at 259bp, and the next day the CCC tier closed at 690bp, both the tightest levels in the three-year window FRED still serves (FRED BAMLH0A0HYM2, BAMLH0A3HYC). Theo looked at the two numbers and saw a market priced for nothing in particular going wrong. "At 259 and a sixty percent loss," he said, doing the §11.1.2 arithmetic on the back of the folder, "the index breaks even at a 4.3% default rate. It's paid, but not by much."

"Remember that number," Ines said. "You'll want it in a minute."

**Beat 2: the gap.** She turned the page to the end of March. The index was at 355bp on Monday 31 March, already a hundred basis points wider on a quarter of growth worries. On Wednesday 2 April, after the close, the United States announced its tariff schedule. By Friday 4 April the index was at 445bp. Nobody at the table needed to be told what that weekend had felt like; all four of them had spent it somewhere, watching futures.

Kaz said that on that weekend the model builder's question had been whether to switch the model off. Theo said the RSSG question had been whose 13-week model had just changed. He had once spent a Saturday at PJT on a company whose single largest input came from one country, and a tariff on that country would have gone straight through its cost line into its liquidity runway. No spread index would have told him which of two thousand issuers that company was. "That's the PD's job," Ines said. "It's slower than the spread. Some weekends that's its virtue." Mags, who had spent March 2020 on a dealer's distressed desk, said that the second weekend of a selloff is always quieter than the first and more expensive, because by the second weekend the people who have to sell have found out that they have to.

#### Decision point: the card at the 7 April 2025 close

**Beat 3: the card.** "Monday, 7 April 2025. The close." The page had five spreads on it: high yield 461bp, BB 306bp, single-B 486bp, CCC 1,137bp, investment grade 120bp (FRED). The VIX had closed at 46.98 (FRED VIXCLS). In ten weeks the index spread had risen 78% and the CCC tier's by about two-thirds. The total return index was down 3.83% from its 28 February level *(our computation from FRED BAMLHYH0A0HYM2TRIV)*, which on a ten-week chart looked like a cliff and on a ten-year chart would look like a pothole, and nobody on 7 April knew which chart they were in.

"Three things," Ines said. "Tomorrow's DTS multiplier, from the rule in §11.8. The names you add, if any. And what would make you wrong."

Kaz had the z-signal open before the sentence ended, and the arithmetic took less time than the writing. *Spreads up from 259 to 461 while balance-sheet PDs, which move with quarterly filings and equity-implied leverage, have barely had time to move. Against the January reference, $\bar z$ jumps by about $\ln(461/259) = 0.58$. With $\kappa = 0.5$ the rule wants $1 + 0.29 = 1.29$; the cap binds. Multiplier: 1.2. Names: the rule's, by default-adjusted carry per unit of DTS. Wrong if: the PDs catch up with the spreads.*

Theo wrote slowly, and he knew as he wrote it which replay his card would be compared with. *Multiplier: 0.9.* Then, because he did not want to be the nervous committee of §11.2.3 without a reason, he wrote the reason. *This is not June 2022. A tariff is a cost shock to earnings, and the PDs haven't moved because the filings that move them come out in May and August. The spread is ahead of the PD, not wrong about it. Names: none until the first-quarter numbers. Wrong if: the policy reverses before the filings arrive.*

Mags did not write a multiplier at all. *Multiplier: whatever my names add up to. Names: the ones whose PD did not move and whose documents I have read. Not the cheapest; the cheapest are cheap because someone has read their documents too. Wrong if: I've read the documents wrong.* She had drawn a small gate next to the second line, which on her cards meant the Priming Risk Score of Chapter 13.

Ines priced the pot out loud, on the whiteboard, under the 4.3% from January. "At 461 and a sixty percent loss the index breaks even at a 7.7% default rate over the next year. Theo, what default rate do you need to believe to sell here?"

Theo thought about it honestly. "More than seven and a half. I believe in maybe four or five, if the tariffs stick."

"Then you're still paid at your own number. You're not selling because the bet is bad. You're selling because the pot got big." She did not put a number on what each card would make, because the honest answer on 7 April was that nobody knew whether the next ten weeks ran to 350 or to a thousand. She put up the asymmetry instead: the 1.2 card was long more of a spread that paid for a default rate nearly twice the one Theo himself believed, and the 0.9 card had given up that spread to avoid a default rate he did not believe. "Kaz is betting on the price of fear. Theo is betting against his own forecast. Mags is betting on her reading. Only one of those is a bet I'd make with my own chips, and it isn't Theo's."

"It's mine," said Mags, who did not need to be told.

**Beat 4: the ten weeks.** Ines moved the tape one day at a time for the first three days, because the first three days were where the cards were decided.

Tuesday 8 April: spreads stayed near the wides. The VIX closed at 52.33, its high, one day *after* the high yield spread had peaked (FRED VIXCLS). HYG, one of the largest high yield ETFs, closed at a 0.66% discount to its net asset value: sellers were paying two-thirds of a point to get out through the wrapper rather than wait for the bonds (iShares premium/discount history). "That's somebody's committee," Mags said.

Wednesday 9 April: a 90-day pause on the higher country-specific tariffs, China excepted, was announced in the early afternoon, and HYG closed at a 1.49% *premium* to NAV. The two closes were the year's extremes of each sign, on consecutive days (iShares). The wrapper that had been dumped at a discount on Tuesday was bought at a premium on Wednesday, by buyers who could not get the bonds fast enough. Ines circled the two numbers. On an ordinary day HYG's premium is close to a rounding error, +0.135% on average over the 448 days of history iShares publishes. "Two days. More than two points from the bottom of the discount to the top of the premium, on the instrument everyone uses as their hedge."

The rest of the ten weeks went quickly. April's TRACE volume described a market in which fewer people were willing to stand in front of anything: average daily corporate par fell to \$62.1bn from \$77.2bn in March, and the share executed on alternative trading systems fell to 5.8% from 7.4% (FINRA monthly TRACE reports, our computation). The venue share fell exactly when a systematic book would have wanted it most, a fact Chapter 2 and Chapter 19 both have opinions about. The index's total return regained its 28 February peak on 12 May 2025 *(our computation)*. Calendar 2025 finished at +8.50%, and State Street put the trailing global high yield default rate at 1.6% at year-end.

**Grading the cards.** *(Illustrative; the PD stability is our inference, since no vendor's aggregate PD series is sourced here.)* Theo's 0.9 sold at 461bp and, by the logic of its own reason, waited for the first-quarter filings before buying anything back. The filings came, they did not move the PDs nearly as far as 461 had implied, and by then the index had regained its peak. The price-based de-risker sold on 7 April and bought back in May above where it sold. It is the nervous committee of §11.2.3, the same card in a different year, and its reason, which was a good reason, did not change the arithmetic.

Kaz's 1.2 added DTS into the low and was right. The PD-based desk earned the rebound on a fifth more spread exposure than the benchmark, and it did so by rule, at the close, without anyone having to feel brave.

Mags's card graded best on what did not happen. Her names were the subset of Kaz's whose PDs had not moved and whose documents had no priming capacity worth worrying about. Over ten weeks that cost her a little of the rebound in the cheapest names, which is the price of the gate, and the box at the end of this section says why the gate stays on.

Ines read the hand history back through the markouts, the way she always did. "Same cards, same flop. One player folded because the pot got big. The other called because the odds got good."

Theo turned his card over. "Kaz was right."

"Kaz was right and also lucky," Ines said, "and the difference matters, because next time the pause doesn't come." Kaz's card had said it would be wrong if the PDs caught up with the spreads. It never asked whether the PDs *should* already have moved by the time Kaz computed $\bar z$. Dynkin's answer is that they should.

> **[SOURCE EXTRACTION]** *Dynkin_Systematic_Investing_in_Credit p.384:* "we set our downgrade scalar to 2 (and upgrade scalar to 0.5) and adjust probabilities of unchanged ratings (along the diagonal) such that each row sums to 100%."
>
> **Annotation.** Dynkin conditions the rating transition matrix on the spread environment: in a wide-spread regime downgrades are scaled up and upgrades down, and the diagonal absorbs the difference so each row remains a probability distribution. That is the honest version of "spreads are wide, so buy": wide spreads *do* forecast more downgrades, and a model that ignores that will overbuy. The z-signal above should therefore be computed with spread-conditioned PDs, not PDs frozen at their calm-market values. The residual that survives the conditioning is the overpayment worth buying.

On 7 April 2025 the conditioned PDs would have been higher than the frozen ones, $\bar z$ smaller than 0.58, and the multiplier somewhere below the cap. Kaz's card would still have added risk, only less of it, and the part of Kaz's 1.2 that the conditioning removes is the part that was luck. Mags's gate catches the other way the residual lies.

> **Ways This Blows Up.** *Cheap because it is about to be primed.* A bond whose spread exceeds its PD-implied spread may be pricing something the PD cannot see: a drop-down basket, an uptier-permissive amendment provision, a sponsor that has hired restructuring counsel. The z-signal flags it as overcompensated; the credit agreement flags it as next. Gate every z-driven purchase on the Priming Risk Score of Chapter 13, and treat a high PRS with a high z as a short, not a long.

Theo had watched the 1.2 card win, and as Ines put the folder away he asked the question that follows every strategy that wins a replay.

## 11.9 Capacity of Systematic HY

"If this works," Theo asked, "why isn't it a trillion dollars?" Blackstone's answer is that systematic strategies run about 20% of global equities but less than 2% of the fixed income universe (Blackstone p.2). Part of the gap is data and history; part is capacity, which is a cost curve. The curve rests on one empirical regularity, that the price impact of a trade grows with the square root of its size rather than in proportion to it, so doubling the money costs about $\sqrt2$, or 41% more, per dollar traded (Chapter 4, §4.8, has the Math, Gently box).

Let $\alpha_0$ be gross annual alpha, $\text{TO}$ annual turnover, $V_{\text{ADV}}$ the relevant average daily volume, $H$ the days over which the strategy trades, and $\kappa$ a square-root impact coefficient. Net alpha at capital $C$ and the capacity $C^\ast$ at which it falls to a hurdle $\alpha_{\min}$ are

$$
\alpha_{\text{net}}(C) = \alpha_0 - \kappa\,\text{TO}\sqrt{\frac{C}{V_{\text{ADV}}\,H}}, \qquad C^\ast = V_{\text{ADV}}\,H\left(\frac{\alpha_0 - \alpha_{\min}}{\kappa\,\text{TO}}\right)^{2}.
$$

The square means capacity is brutally sensitive to turnover: halve $\text{TO}$ and capacity quadruples.

Theo did not let go of his question. "So which parts of this chapter are the trillion-dollar parts?"

Kaz answered by turnover, because the formula said turnover was the lever. "Default avoidance is an *exclusion* rule. You decide once a month whom not to own, and most months the list barely changes. Low turnover, so it scales. The low-risk tilt lives in the most liquid part of high yield, the short BBs, so it scales too."

"And the parts that made money in the replays?"

"Those are the problem," Ines said. "CCC reversal and fallen-angel buying need high turnover in the least liquid bonds at the worst moments. April 2025 was the trade, and April 2025 was also the month corporate TRACE volume fell by a fifth." Mags added the part nobody puts in a capacity model: liquidity is state-dependent, and Ben Dor finds that liquidity costs show up in HY spreads mainly in stress (p.177), which is when the defensive signal fires. "The day the model says buy is the day the bid-ask says please don't."

"So the trillion-dollar version," Theo said, "is the boring half."

"The boring half is the core," Ines said. "The interesting half is a satellite. You size it from the curve, not from the replay." Dynkin published one of the few curves there are.

> **[SOURCE EXTRACTION]** *Dynkin_Systematic_Investing_in_Credit p.209:* "the Sharpe ratio decreases to 0.95 (from 1.14) for a portfolio size of \$2bn, well above that of the High Yield Index (0.65)."
>
> **Annotation.** This is a rare published capacity curve for a HY niche: Dynkin's fallen-angel strategy, net of transaction costs, losing about a sixth of its Sharpe ratio as it grows to \$2bn, and still beating the index. Two readings. The optimistic one: niche HY strategies are not as capacity-constrained as folklore says, because the forced sellers are large. The realistic one: \$2bn is a single sleeve at a large manager, so the fallen-angel and CCC-reversal components of a defensive book should be sized as satellites around a core that scales: exclusion plus DTS-neutral low risk. The trading-cost inputs have also improved since that study, which the Trend Watch below quantifies.

Mags, whose first high yield trades went through by phone, read the next numbers twice, which on this desk counts as applause.

> **Trend Watch: Electronic HY and the Systematic Share, 2019–2026.** *What changed:* HY execution became electronic enough that a systematic book can trade hundreds of line items without a phone. *How big:* Man Numeric moved from roughly 30% of its HY and 60% of its IG order flow on electronic venues to over 90% of all order flow by May 2023 (Man 2023 p.3). Total US corporate bond ADV reached \$66.7bn through September 2026, up 13.4% year on year, with \$12.1tn outstanding at 2Q26 (SIFMA, US Corporate Bonds Statistics, page dated 14 October 2026). Sizes in the wild: Blackstone's systematic credit platform manages more than \$40bn across IG, HY and EM (Blackstone p.1–2); the iShares High Yield Systematic Bond ETF (HYDB), launched July 2017 and selected and weighted by a systematic default-risk model, held \$1.52bn at a 0.35% expense ratio (stockanalysis.com, checked 17 October 2026). *What it means:* the cost coefficient $\kappa$ fell, so capacity rose with its square; but systematic HY is still a small share of a large market, which is good news for capacity and a warning about how short the live track records are. Portfolio trading's role in this shift is Chapter 19's story.

### Specification for AI Implementation

**Schema.** Cross-section arrays `spread`, `s_hat`, `dts`, `w` (decimals; weights sum to 1); scalars `z_ref`, `kappa`, band `(lo, hi)`, `dts_max_ratio` (largest achievable long-only DTS over benchmark DTS). Capacity inputs in decimals per year and dollars; `adv` is \$ per day.

The ten-week V of April 2025 makes a satisfying story, and a story is exactly what a risk committee will not accept as a rule. The questions arrive in order. Why did the book add DTS on the day the price-based limits told everyone else to sell? Would the same rule have added DTS in a quarter when spreads and PDs both blew out together, which is the quarter that ends careers? And, from the chief investment officer at the end of the table, if this works, how large can it get before the cost of trading it eats the alpha? Each answer has to exist as a function before the meeting, with a test that shows it behaving, because nobody wants to improvise the answer to "what does the model do if spreads double?" with the model open on a laptop.

The listing answers all three. `model_spread` is the market's expected price of the PD: a liquidity floor plus a risk-premium multiple times PD times loss given default. `dts_multiplier` takes the cross-section's spreads, model spreads, DTS and weights, forms the log residual for each issuer, averages it with DTS weights into $\bar z$, and returns one number: one plus `kappa` times the move in $\bar z$ from its reference level, clipped to the band of 0.9 to 1.2, then capped at `dts_max_ratio`, the most DTS a long-only, issuer-capped book can actually hold. It returns the multiplier and $\bar z$ together. `alpha_net` is the square-root impact curve, and `capacity_closed_form` and `capacity_numeric` find the capital at which net alpha falls to the hurdle, one by the formula of §11.9 and the other by a bracketed root search that widens its upper bracket fourfold until alpha is below the hurdle.

The regime test reuses the last cross-section from Listing 11.5 and replays April 2025 by scaling spreads and DTS by 461/259. With the reference set to the calm cross-section, the multiplier is 1.00. When spreads gap and the model spread stays put, it hits the 1.20 cap. When spreads and model spreads widen together, because the fundamentals deteriorated, the residual does not move and the multiplier stays at 1.00. With a no-leverage guard of 1.05, it returns 1.05. The capacity test confirms that the closed form and the root search agree to eight digits, and puts a high-turnover satellite at about \$1.2bn against about \$49bn for the low-turnover core, with every input illustrative.

The multiplier is a budget, not a trigger, and the satellite is sized from the capacity curve rather than from enthusiasm. Where the function goes quietly wrong is the reference level `z_ref`. The demonstration sets it to the calm cross-section's own $\bar z$, which makes the multiplier equal to one by construction; in production it must come from history, computed with the same `m` and `s0`, because the level of $\bar z$ depends on those constants and a reference built with other ones is silently stale. A close second is a hurdle above gross alpha. The root search raises an error, while the closed form squares a negative number and returns a small positive capacity, which is why the numeric version is the check.

*The full listing is [Listing 11.6 in Appendix F](#code-11-6).*

*(The capacity inputs, including HY ADV of about \$14bn a day, are illustrative; SIFMA publishes the high yield split in its downloadable statistics, which we did not verify. With them the core sleeve's capacity is about \$49bn and the satellite's about \$1.2bn, the same order of magnitude as Blackstone's platform and Dynkin's \$2bn fallen-angel curve.)*

## 11.10 Desk Debrief

The chapter, findable. Each row is one idea, where its equation lives, the box that builds the intuition, the scene where somebody had to use it, and the listing that runs it.

| Concept | Equation | Intuition (box) | Judgment (scene) | Code (listing) |
| :--- | :--- | :--- | :--- | :--- |
| The mixture return and its skew | $\operatorname{Skew}[-L_P J] = -(1-2p)/\sqrt{p(1-p)}$ (§11.1.1) | "A bell with a lonely spike" (§11.1.1) | Mags waves away the CCC volatility (§11.1.1) | — |
| The credit triangle, with the measure stated | $\mathbb{E}^{\mathbb{P}}[r^{xs}] \approx s - \lambda^{\mathbb{P}} L$ (§11.1.2) | "Bookmaker's odds versus true odds" (§11.1.2) | Kaz finds zero expected return, three times (§11.1.2) | — |
| The capture identity | $U - D = \alpha\,(1/\bar r_b^{\,\mathcal{U}} + 1/\lvert \bar r_b^{\,\mathcal{D}} \rvert)$ (§11.2.1) | "The gap is alpha, the level is beta" (§11.2.1) | The 30 June 2022 replay (§11.2.3) | [Listing 11.1](#code-11-1) |
| Asymmetric beta | $r_{p} = \alpha + \beta^{+}\max(r_b, 0) + \beta^{-}\min(r_b, 0) + \epsilon$ (§11.2.2) | "A line with a kink" (§11.2.2) | Three tabs, three managers, 10:40 (§11.2.2) | [Listing 11.1](#code-11-1) |
| Distance-to-default and the empirical map | $\sigma_E E = N(d_1)\sigma_V V$; $\text{DD}_T$; $\text{PD} = g(\text{DD})$ (§11.3) | "Random walk ... equity is the call, read backward" (§11.3.1); "Four sigmas in two worlds" (§11.3.2) | Saks, beat 1: nothing to invert (§11.4.3) | [Listing 11.2](#code-11-2) |
| The hazard and the label | $h_i(t \mid x) = 1/(1+e^{-(\alpha_0 + \beta^\top x)})$; the intercept shift (§11.4.2) | "A hazard is the chance of failing this month" (§11.4.2) | Saks Global, a default in four dates (§11.4.3); Marisol's Tuesday (§11.4) | [Listing 11.3](#code-11-3) |
| Power: AR and AUC | $\text{AR} = 2\,\text{AUC} - 1$ (§11.5.1) | "AUC is a bet" (§11.5.1) | 0.912 against 0.904, and why (§11.4) | [Listing 11.4](#code-11-4) |
| Exclusion arithmetic | $\mathbb{E}^{\mathbb{P}}[r_{\text{active}}] \approx q[(\pi_X - \pi_K)L - (s_X - s_K)]$ (§11.5.2) | "Base rates" (§11.5.2) | The vendor's missing $q$ (§11.5.2) | [Listing 11.4](#code-11-4) |
| Expected-loss sizing, low risk and the z-budget | the EL constraint (§11.6.1); the DTS Sharpe line (§11.7.1); $z_i$ and $\text{DTS}^{\text{target}}_t$ (§11.8) | DTS: Chapter 8, §8.4; square-root impact: Chapter 4, §4.8 | The risk committee and the issuer cap (§11.6.1); three exits (§11.7.2); ten weeks in 2025 (§11.8.1); PB-01, a long with a hat on (§11.6.2) | [Listing 11.5](#code-11-5), [Listing 11.6](#code-11-6) |

Theo unplugged the USB stick at 7:40 p.m. The 13-week model had become a covariate, capped at 13, and was now one of three features in a hazard function that covered 2,000 issuers. It seemed to be taking the demotion well.

Across the desk Kaz was still reading the Saks docket, which Ines had left on the table as homework, and got up to cross out *selective = ?* on the whiteboard. "So *selective*," Kaz said, "meant they selected January."

- **High yield is a short put that pays a coupon.** The default jump carries skew of $-(1-2p)/\sqrt{p(1-p)}$: about $-6.9$ at a 2% PD, $-1.5$ at 20%. BB defense is tail avoidance; CCC defense is pricing.
- **$U = D = \beta$ is a dimmer switch.** A pure beta tilt gives equal capture ratios, and only alpha opens the gap. The average manager's 92.24%/89.56% reads as roughly a 0.91 beta with a small net alpha. Real defense is $\beta^{-} < \beta^{+}$, tested on pairs of regimes.
- **DD is a ranking, not a probability.** Map it to PD empirically, never with $N(-\text{DD})$, and send no-equity issuers to a separate, flagged model.
- **The label is the model.** With distressed exchanges at 65% of 2025 defaults, a PD trained on hard defaults is calibrated to a world that no longer exists. Label at the issuer, date it at announcement, and include LMEs that impair the holder.
- **A hit rate without an exclusion rate is half a sentence.** Default avoidance pays when $(\pi_X - \pi_K)L > s_X - s_K$; the same 77% can be +44bp or −9bp depending on how much of the table you folded.
- **CCC is a crowd, not a person.** Size the bucket by expected loss, choose inside it by PD, diversify it with breadth (high-PD risk is mostly idiosyncratic), and buy from forced sellers whose problem is a rating, not a balance sheet.
- **IDO or it didn't happen.** Every defensive signal is tested DTS-neutral first; a market-value-neutral low-risk tilt is beta wearing a factor's name tag.
- **Capacity is a square.** Halve turnover and capacity quadruples: exclusion and low risk scale into tens of billions, CCC reversal and fallen angels into low single-digit billions.

### The Spec You Hand the Robot

"Build an issuer-month panel from the security master, one row per ultimate parent per month. Label equals 1 if any of {payment default beyond grace, bankruptcy filing, distressed exchange, LME that impairs the holder} is *announced* in months $[t, t+12)$; drop rows whose window runs past the data. Features: empirically mapped distance-to-default (with `no_equity_flag`), CHS market and accounting covariates lagged to filing date, liquidity runway in weeks capped at 13, months since last LME, and the Chapter 13 PRS. Fit a calibrated dynamic logit with issuer-clustered errors and a gradient-boosted model, both with issuer-disjoint, 12-month-embargoed cross-validation; report AUC, AR (assert $\text{AR} = 2\,\text{AUC} - 1$ on untied scores), hit rate at 10/20/30% exclusion, and realized-versus-predicted default rates by PD decile. Portfolio: exclude the worst-PD quintile, tilt toward $(s_i - \hat\lambda_i L_i)/\text{DTS}_i$, hold $w^\top\text{DTS}$ within 1% of the benchmark times a regime multiplier in $[0.9, 1.2]$ driven by the DTS-weighted spread-to-model-spread residual, issuer cap 3%, long-only, no leverage. Report $U$, $D$, $\beta^{+}$, $\beta^{-}$ on benchmark regimes. Halt and alert if portfolio DTS deviates from target by more than 2%, if any weight is negative, if the target DTS is unreachable without leverage, or if a z-signal purchase has a PRS above threshold."

ROBO acknowledged the spec. It did not ask what "impairs the holder" meant, because the spec now had a list.

### Exercises

1. **The top-quartile hand history.** The top-quartile manager captured 99.00% of up markets and 92.00% of down markets (BlackRock p.3). With regime means of +1.6% and −2.0% a month, recover $\alpha$ and $\beta$ from the identity in §11.2.1. Then find the zero-alpha asymmetric portfolio ($\beta^{+}, \beta^{-}$) that produces the same two capture ratios, and explain to a consultant why the two portfolios are indistinguishable on capture ratios and very different on a regime-pair test.
2. **Skew by tier.** Show that $-\frac{1-2p}{\sqrt{p(1-p)}}$ is increasing in $p$ on $(0, \tfrac12)$, that is, the jump component gets *less* negatively skewed as the PD rises. Compute it at 1% and 10%. Write one paragraph on what this implies for the size of a BB position versus a CCC position at equal expected loss.
3. **Ines's question, answered.** Assume a binormal score model: defaulters' scores are $N(\mu, 1)$, survivors' $N(0, 1)$, with base rate 3% and AUC 0.85. Using $\text{AUC} = \Phi(\mu/\sqrt2)$, find the exclusion fraction $q$ at which the hit rate is 77%. (You should get about 25%.) Then compute the active return from §11.5.2 with $L = 0.6$ and an excess spread of 400bp in the excluded set, and state whether the claim is good news.
4. **The soft-default world.** Re-run Block 3 with `de_share=0.65`, Moody's 2025 share. Train on the hard-default label, score against the full label, and report the calibration error by PD decile. Can the prior-shift formula of §11.4.2 repair it? (It repairs the level. Explain why it cannot repair the ranking when distressed exchanges are concentrated in sponsor-owned issuers with drop-down capacity, and add a feature that can.)
5. **ROBO, defensively.** Theo's next spec reads "minimize realized defaults while beating the index." List three portfolios ROBO could build that satisfy the sentence literally and that you would never run (hint: one involves holding a single BB bond, one involves leverage, one involves the definition of "default"), and write the constraint that rules each one out.
6. **Capacity is a square.** Prove from the formula of §11.9 that halving turnover multiplies capacity by four. Compute the niche sleeve's capacity at a turnover of 1.0 instead of 2.0, and then explain why, in practice, cutting turnover in a CCC-reversal strategy also cuts $\alpha_0$, so the quadrupling never fully arrives.

### Deep-Dive Resource Graph

**Podcasts**
- **TCW Chops Credit Risk to Lowest in 30 Years as CCCs "Cry Uncle"** (*The Credit Edge*, Bloomberg Intelligence, guest Bryan Whalen, TCW CIO, 15 Oct 2026). A \$160bn fixed-income group says CCC is "the weakest borrower, and they cry uncle first", then single-B, then double-B: the contagion ladder of §11.6 as a live quote. https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/tcw-chops-credit-risk-to-lowest-in-30-years-as-cccs-cry-uncle
- **Seix Fears More Zombie Borrower Distress as Interest Rates Stay High** (*The Credit Edge*, Bloomberg Intelligence, guest George Goudelias, Seix, 22 Jan 2026). B3/B- and CCC "credit zombies" with weak interest coverage and zero free cash flow: the feature profile a default-avoidance screen is meant to exclude. For §11.4 (hazard-model features) and §11.6. https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/seix-fears-more-zombie-borrower-distress-as-interest-rates-stay-high
- **Fridson Sees High Yield Going Distressed in Recession** (*The Credit Edge*, Bloomberg Intelligence, guest Martin Fridson, Fridson Vision High Yield Strategy, 1 May 2025). A dated, falsifiable call ("high confidence" that the index returns to 1,000bp at the worst point of the next recession) from the field's long-time default scholar, plus ratings trends and liability management; for §11.1 and §11.5, and worth scoring against the realized path. https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/fridson-sees-high-yield-going-distressed-in-recession
- **High Yields and Low Risk at Polen Capital (EP.405)** (*Capital Allocators*, guest Dave Breazzano, Polen Capital, 12 Sep 2024). A high-yield investor since the early 1980s on the market's history and the "myths" his strategy exploits: the fundamental-quality counterpart to a systematic low-risk tilt. For §11.7. https://www.capitalallocators.com/podcast/high-yields-and-low-risk-at-polen-capital/
- **Blissfully Buying BB Bonds with Greg Obenshain of Verdad Capital** (*The Derivative*, RCM Alternatives, host Jeff Malec, 23 Sep 2021). How a quant HY model assigns its own ratings (and why they differ from the agencies'), the data problem (no central exchange or shared order book) and the "sweet spot between BBB and B". For §11.7 and §11.4. https://www.rcmalternatives.com/2021/09/blissfully-buying-bb-bonds-with-greg-obenshain-of-verdad-capital/

**Practitioner Writing**
- **High-Yield Bonds: Not Your Parents' Market** (Brookfield, Sheldon Stone and David Rosenberg, co-PMs of US high-yield bonds, Feb 2026). Reads "tight" spreads (around 300bp) against a market that is now over 55% BB, with CCC-and-below at 12.1% versus a 17.2% long-term average: the composition effect any capture-ratio or DTS comparison has to net out. For §11.2 and §11.9. https://privatewealth.brookfield.com/sites/default/files/2026-02/high-yield-bonds-not-your-parents-market.PDF
- **Cockroaches in the Coal Mine** (Howard Marks, Oaktree memo, 6 Nov 2025). Marks on a string of well-publicised credit problems as a reminder of what the yield premium in sub-investment-grade credit is paid for: the frame for why a defensive screen exists. For §11.1. https://www.oaktreecapital.com/insights/memo/cockroaches-in-the-coal-mine
- **Gimme Credit** (Howard Marks, Oaktree memo, 6 Mar 2025). Answers "what about credit spreads?" by comparing the spread to credit losses: the discretionary statement of the asymmetry that §11.1 derives from the mixture return. For §11.1 and §11.8. https://www.oaktreecapital.com/insights/memo/gimme-credit
- BlackRock (Parker, Radell, Aguiar, Kang), *A systematic approach to high yield credit* (December 2025): https://www.blackrock.com/gls-download/literature/whitepaper/systematic-high-yield-credit.pdf
- Moody's Analytics (David Hamilton), *Lend, extend, and then…* (18 May 2026): https://www.moodys.com/web/en/us/insights/credit-risk/private-credit/lend-extend-and-then.html
- State Street Investment Management, *Global high yield—2025 in review and 2026 outlook*: https://www.ssga.com/library-content/assets/pdf/global/fixed-income/2026/2025-global-high-yield-update-fixed-income.pdf
- Loomis Sayles, *Quarterly Credit Update 4Q24*: https://info.loomissayles.com/hubfs/FD%20Quarterly%20Credit%20Update_4Q24%20FINAL.pdf
- Wellington, *CCC junk bonds appear undervalued and overlooked*: https://www.wellington.com/en/insights/ccc-junk-bonds-appear-undervalued-and-overlooked
- UBS Asset Management, *2025 fixed income default study* (17 January 2025): https://www.ubs.com/us/en/assetmanagement/insights/asset-class-perspectives/fixed-income/articles/2025-fixed-income-default-study.html
- The DESK (Dan Barnes), *Defaults creep higher in leveraged credit markets* (27 May 2026): https://www.fi-desk.com/defaults-creep-higher-in-leveraged-credit-markets/
- Investment Executive, *U.S. leveraged loan defaults to ease in 2026: Fitch* (3 December 2025): https://www.investmentexecutive.com/news/u-s-leveraged-loan-defaults-to-ease-in-2026-fitch/
- Title only: Robeco research on low-risk and conservative credits; Barclays QPS notes on equity momentum in credit; S&P Global Ratings *Default, Transition, and Recovery* series; Fitch *U.S. Leveraged Finance Default Insight*.

**Academic Papers**
- Shumway, T. (2001), *Forecasting Bankruptcy More Accurately: A Simple Hazard Model*, Journal of Business 74(1): https://ideas.repec.org/a/ucp/jnlbus/v74y2001i1p101-24.html
- Chava, S. and Jarrow, R. (2004), *Bankruptcy Prediction with Industry Effects*, Review of Finance 8(4): https://ideas.repec.org/a/oup/revfin/v8y2004i4p537-569..html
- Campbell, J., Hilscher, J. and Szilagyi, J. (2008), *In Search of Distress Risk*, Journal of Finance 63(6); NBER WP 12362: https://www.nber.org/papers/w12362
- Alanis, E., Chava, S. and Shah, A. (2022), *Benchmarking Machine Learning Models to Predict Corporate Bankruptcy*: https://arxiv.org/abs/2212.12051
- Houweling, P. and van Zundert, J. (2017), *Factor Investing in the Corporate Bond Market*, Financial Analysts Journal 73(2): https://papers.ssrn.com/abstract=2516322
- Frazzini, A. and Pedersen, L. H. (2014), *Betting Against Beta*, Journal of Financial Economics 111(1); and Dick-Nielsen, J., Feldhütter, P., Pedersen, L. H. and Stolborg, C., *Corporate Bond Factors: Replication Failures and a New Framework* (both listed at https://www.lhpedersen.com/research)
- Title only: Altman (1968), *Financial Ratios, Discriminant Analysis and the Prediction of Corporate Bankruptcy*; Merton (1974), *On the Pricing of Corporate Debt*; Bharath and Shumway (2008), *Forecasting Default with the Merton Distance to Default Model*; Duan, Sun and Wang (2012), *Multiperiod Corporate Default Prediction: A Forward Intensity Approach*; Engelmann, Hayden and Tasche (2003), *Testing Rating Accuracy*; Israel, Palhares and Richardson (2018), *Common Factors in Corporate Bond Returns*.

**Data & Code**
- FRED, ICE BofA US High Yield OAS and tiers: https://fred.stlouisfed.org/series/BAMLH0A0HYM2, https://fred.stlouisfed.org/series/BAMLH0A1HYBB, https://fred.stlouisfed.org/series/BAMLH0A2HYB, https://fred.stlouisfed.org/series/BAMLH0A3HYC (CSV via `https://fred.stlouisfed.org/graph/fredgraph.csv?id=<SERIES>`; ICE series carry a rolling three-year history on FRED).
- Open Source Bond Asset Pricing (TRACE panels, bond factors, ML predictor panel): https://openbondassetpricing.com/
- NUS Credit Research Initiative (free PD term structures for listed firms, a public benchmark for your model): https://nuscri.org/en/
- SIFMA US Corporate Bonds Statistics: https://www.sifma.org/resources/research/statistics/us-corporate-bonds-statistics/
- iShares HYDB summary data: https://stockanalysis.com/etf/hydb/
- SEC EDGAR (credit agreements and indentures for covenant and basket features): https://www.sec.gov/edgar

<!-- STATUS: COMPLETE -->
