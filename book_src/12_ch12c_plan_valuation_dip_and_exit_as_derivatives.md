# Chapter 12-C: Plan Value Is a Negotiated Random Variable: Valuation Fights, the DIP, Roll-Ups, Exit Financing and the Fulcrum Under Uncertainty

> **Prerequisites.** Read Chapter 12-B first, especially §12B.5 (the DIP and the roll-up transfer), §12B.6 (the waterfall as call spreads, the fulcrum and plan value, each defined once) and §12B.9 (the Halvorsen numbers, which this chapter reuses without change). From elsewhere: §13.3 (an LMT is the difference of two waterfalls), §13.7 (`waterfall_clearing`), §16.1 and §16.3 (the plan as a security factory; backstops), and §6-B.1 (payoffs and call spreads). Chapter 12-B gave you the machine, and this chapter puts a probability measure on its most argued-over input.

## Cold Open: Exhibit D First

*Thursday, 11:48 p.m.* Theo Marsh's docket alert chimes. Docket No. 412: *Disclosure Statement for the Joint Chapter 11 Plan of Reorganization of Halvorsen Packaging Holdings, Inc. and Its Debtor Affiliates*, 318 pages. (Halvorsen is fictional, and every number in this chapter is illustrative.)

Nobody should still be here. Kaz Lind's calibration run is on hour four. Mags Dunleavy says she sleeps better after a disclosure statement, "the way other people read Trollope." Ines Okafor is always here. And ROBO, which has no hours, has already been asked by the evening shift to "maximize plan value." Theo scrolls past the risk factors and forty pages on the history of corrugated packaging, and stops at Exhibit D.

"You skipped the valuation," Kaz says.

"The valuation is an argument. Exhibit D is the liquidation analysis. It's the only number in here that has to be a floor." He reads aloud: in a hypothetical Chapter 7, the first lien recovers 21.6%, general unsecured creditors recover nothing, and the case is administratively insolvent. "So the plan has to beat 21.6 for the first lien and zero for the bonds. Everything above that is negotiation."

Then Exhibit E: a total enterprise value of \$1,150mm to \$1,450mm, midpoint \$1,300mm, from a DCF, trading comparables and precedent transactions, weighted in a footnote nobody will read until the confirmation hearing.

"Why does one company have three values?" Kaz asks.

"The low end is for the fulcrum," Mags says, without looking up. "The high end is for the equity's lawyer. And the middle is for the judge."

"Then it's not a number. It's a distribution with a negotiating position on each tail." Kaz rubs their eyes. "Is plan value a Brownian motion or a Zoom call?"

"A Zoom call that a judge gets to end," Ines says. "Two experts, one judge, and the pot is the fulcrum. What's the pot, what are the odds, and who at this table knows more than you?" She looks around the room. "And who at this table has read Exhibit D?"

Theo raises a hand. Nobody else does.

ROBO posts its answer. It found the top of the comparables range (14.0x, a 2021 specialty-packaging deal) and applied it to the best year of the management projections. *Plan value: \$4,075mm. Every class paid in full in new common stock. Old equity retains 40%. Objections expected: none.*

"The most generous plan in history," Mags says, "and it pays everyone in a currency only ROBO accepts." The first lien would take shares "worth" its claim at \$4,075mm in a company the market will value at a third of that: a high plan value sells the senior class's equity to the juniors at a price nobody else would pay (§12B.6). Nobody told ROBO whose value to maximize.

The Ad Hoc Group's amended Rule 2019 statement lands four minutes later. *"We hold 58% of the first lien. We have retained three valuation experts. We are prepared to disclose the holdings of each."*

Mags finally looks up. "Price is what you pay. Plan value is what the banker says. Recovery is what you get, after the lawyers, and after the lawyers' lawyers."

**If plan value is negotiated, what is its distribution, and who gets paid if you know it?**

By the end of this chapter you will be able to read a valuation range and an expert fight as a mixture distribution on plan value; compute each class's fulcrum probability and recovery distribution; treat §1129 as flags and bounds on that distribution; decompose and price a DIP and a take-back note; read 363 sales, admin burn, KEIPs and the tax line as options and clocks; map three banker exhibits onto three desk models; and specify `plan_value_engine.py`.

## 12C.1 Three Values of One Company

A restructuring banker learns early that a valuation has an author, and the author has a client. You built the Exhibit E slide many times: a DCF, a comparables multiple, a precedents multiple, a football field, and a midpoint that becomes "plan value." Each method has honest latitude: a discount rate, a peer set, which deals you remember. For Halvorsen the advisor puts 2027 EBITDA at about \$186mm and the range at 6.2x to 7.8x; the midpoint is 7.0x. In a restructuring the latitude has owners, and the desk adds a question you were never paid to ask out loud: what is the probability that the judge confirms each answer?

Moyer said it plainly two decades ago, from the buy side.

> **[SOURCE EXTRACTION]** *Moyer_Distressed_Debt_Analysis p.355:* "if a distressed debt investor whose strategy is to control the postreorganization equity has purchased the secured debt, then there will be a strong bias for as conservative a valuation as possible."
>
> **Annotation.** In 2005 this described incentives; in 2026 it is a forecast you can trade. The fulcrum holder who wants the company wants a low $V^{\text{plan}}$, because each dollar of claim then buys more shares (§12B.6); the class below wants a high one for the same reason. Moyer calls the negotiation "similar to a zero-sum game" (p.252). The desk's departure is to give the bias a parameter: whose expert will the judge believe, and how far apart are they?

Here is how the fight usually runs. The debtor's advisor, whose plan carries the first-lien group's support agreement, testifies to the midpoint. The creditors' committee, which needs the first lien paid in full before it sees a dollar, hires an expert who arrives at \$1,900mm on a lower discount rate and a peer set with two fast-growing specialty names. The experts are deposed, and the judge adopts a number, usually close to one expert's figure and adjusted for whatever assumption the judge found least persuasive. The confirmed value is a draw from one of two distributions, chosen by a third party. That shape has a name.

> **Math, Gently.** *A mixture distribution.* A distribution is a list of what can happen and how likely each outcome is, drawn as a curve whose area is one. A *mixture* is what you get when a coin decides which of two curves you draw from. Flip a coin that lands heads 70% of the time; on heads, draw a plan value from a curve centered at \$1,300mm, and on tails, from a curve centered at \$1,900mm. The resulting curve has two humps, a tall one at 1,300 and a shorter one at 1,900, and a valley between them. Three things follow, and each surprises someone every case. The *mean* is $0.7 \times 1{,}300 + 0.3 \times 1{,}900 = 1{,}480$ (a little more once each hump's own spread is counted), which sits in the valley where the judge is least likely to land. The *median* is about 1,375, not the debtor's 1,300. And the debtor's midpoint is the most likely single region but not the expected value. A position sized on "the midpoint" is a bet that the coin lands heads. The full version, with the formulas, is in §12C.2; Chapter 5 introduced mixtures with a deck of cards (§5.1.2) and the lognormal shape used for each hump (§5.2.3), and §14.4 treats recovery itself as a mixture.

Each hump is lognormal: plan values cannot be negative, and experts argue about multiples and discount rates, which act as percentages of value. Each hump gets a median (the expert's number) and a log-volatility (how far the judge might adjust it). Reading the debtor's range as about one standard deviation either side of its midpoint gives $\sigma_1 \approx 0.10$; the committee's wider sensitivity table gives $\sigma_2 \approx 0.12$. The weight $w$ on the debtor's expert is the judge's propensity. In the contested fights we have read the debtor's figure has carried the day more often than not, so $w = 0.7$ is a round prior, and Chapter 13-B's courts table is where you would start fitting it.

**When the market sets the weight.** In Hertz, two sponsor groups bid for the right to fund the plan, and the auction that closed on 11 May 2021 replaced the choice between experts with a price (§16.6). A market test collapses the mixture onto a point, which is why the party expecting to lose the expert fight asks for one.

**The regularity, and its mechanism.** Moyer's incentive story predicts what Chapter 16 sees in post-reorganization trading: when the fulcrum controls the process, the confirmed value tends to sit below where the new securities trade months later. Gilson, Hotchkiss and Ruback (2000) found large valuation errors in both directions, leaning the way claimants' incentives pointed, and Envision is the dated instance (§12C.11). In symbols:

$$
\mathbb{E}^{\mathbb{P}}\!\left[V^{\text{mkt}}_{+6\text{m}}\right] > V^{\text{conf}} \quad \text{when the fulcrum controls the plan.}
$$

It is a tendency with a mechanism, not a law. It breaks under a market test (Hertz), when the business deteriorates after emergence (Hotchkiss (1995) found that many emerged firms kept losing money and restructured again), and when the junior class wrote the plan.

Used in / builds on: §12B.6 (plan value as a price and the sign of $\partial R_j/\partial V^{\text{plan}}$), §16.1.1 (plan equity value as a negotiated number, which now points here), §14.4 (recovery as a mixture), §16.6 (Hertz's auction), Ch 13-B (the courts table that would fit $w$).

## 12C.2 The Fulcrum as a Random Variable

Chapter 12-B defined the fulcrum once and gave it a delta. This section gives it a distribution, and the payoff picture you already know does almost all of the work.

> **Math, Gently.** *A call spread.* A call option struck at $K$ pays $(V - K)^+$, which is shorthand for "$V - K$ if that is positive, otherwise zero": a hockey stick that is flat until $V$ reaches $K$ and then rises one-for-one. Buy a call struck at 400 and sell one struck at 900, and you own a *call spread*: nothing below 400, a rising ramp between 400 and 900, and a flat 500 above 900. That is exactly what a class of claims with 500 of face owns when 400 of claims sit ahead of it. Below 400 it gets nothing; between 400 and 900 it gets every marginal dollar; above 900 it is paid in full and extra value goes to someone else. The full version, with replication and Greeks, is in §6-B.1.

Order the classes by priority with allowed claims $C_j$ and cumulative claims $K_j = \sum_{i \le j} C_i$. We keep Chapter 12-B's letters: $K_{j-1}$ is the class's **attachment point** (the value that must be exceeded before it sees a dollar) and $K_j$ its **detachment point** (the value at which it is whole). We avoid $D$ for detachment because $D$ is duration, and we will need duration in §12C.5. Class $j$ recovers

$$
R_j(V) = \frac{(V - K_{j-1})^+ - (V - K_j)^+}{C_j},
$$

and the fulcrum is the class whose spread contains $V$. Under a distribution $f_V$ for plan value, the probability that class $j$ is the fulcrum is the probability mass sitting between its strikes:

$$
\pi_j = \mathbb{P}\big(K_{j-1} \le V < K_j\big) = \int_{K_{j-1}}^{K_j} f_V(v)\,dv .
$$

That one line changes how a restructuring professional talks. "The unsecured are the fulcrum" becomes "the unsecured are the fulcrum with probability 17%," and the remaining 83% has a name, too.

The intuition first. A class's recovery is a ramp between two strikes. If $V$'s distribution is narrow and sits mid-ramp, the expected recovery is the recovery at the midpoint. If it is wide, or has humps on either side of a strike, the expectation bends: mass above the detachment point is capped at par and mass below the attachment point is floored at zero. That bending is convexity, and it is where the valuation fight's money lives.

**The expected recovery.** Write $\mathbb{E}[(V - K)^+]$ for the expected payoff of a call struck at $K$. Then

$$
\mathbb{E}^{\mathbb{P}}[R_j] = \frac{\mathbb{E}^{\mathbb{P}}\big[(V - K_{j-1})^+\big] - \mathbb{E}^{\mathbb{P}}\big[(V - K_j)^+\big]}{C_j},
$$

which is just the call-spread identity with an expectation taken on both sides. For a lognormal hump with median $m$ and log-volatility $\sigma$, the mean is $\bar m = m\,e^{\sigma^2/2}$, and each call is given by Black's formula without discounting:

$$
\mathbb{E}\big[(V - K)^+\big] = \bar m\,\Phi(d_1) - K\,\Phi(d_2), \qquad d_{1,2} = \frac{\ln(\bar m/K) \pm \tfrac12\sigma^2}{\sigma},
$$

where $\Phi$ is the standard normal distribution function. For the two-hump mixture, apply the formula to each hump and weight by $w$ and $1-w$. The fulcrum probabilities come out the same way:

$$
\pi_j = \sum_{i=1}^{2} w_i\left[\Phi\!\left(\frac{\ln K_j - \ln m_i}{\sigma_i}\right) - \Phi\!\left(\frac{\ln K_{j-1} - \ln m_i}{\sigma_i}\right)\right], \qquad w_1 = w,\ w_2 = 1 - w .
$$

Here $\sigma_i$ is the log-volatility of *plan* value, not the asset volatility $\sigma_V$ of a structural model. And $f_V$ is a $\mathbb{P}$ object, the desk's forecast of a judge; compared with a price, it meets a belief plus a risk premium (Law 4). Figure 12-C.1 draws the pieces together: Halvorsen's waterfall as stacked call spreads, with the mixture and the fulcrum probabilities beneath it on the same value axis.

![Figure 12-C.1: The Halvorsen waterfall as stacked call spreads (top), with the plan-value mixture beneath it on the same value axis (bottom). Each band is one class's recovery ramp, from its attachment point to its detachment point, in \$mm of plan value. The mixture density of confirmed plan value (debtor's expert at 1,300 with weight 0.7; committee's expert at 1,900 with weight 0.3) is shaded by fulcrum: about 83% of the probability lies below the first lien's detachment point, where the first lien is the fulcrum, and 17% between that point and the unsecured pool's. Illustrative: the mixture of §12C.1 and the waterfall of §12C.10.](assets/figures/ch12c_call_spreads.png)

**Why the strikes move.** A disclosure statement prints one waterfall; a case runs many. DIP priming shifts every attachment point at and below the primed class up by the DIP's size, $M(1+\kappa)$ for new money $M$ and roll-up ratio $\kappa$. Adequate-protection claims (§507(b)) do the same by an amount unknown until the end. The administrative burn $\phi$ raises the strikes with time (§12B.7, §12C.7). Post-petition interest grows an oversecured class's face (§506(b)) and, for a solvent debtor, the unsecured class's too (Hertz, §16.6). And rulings move value between silos: a successful lien challenge (§12B.9's three plant mortgages) or an LMT decision, as in Incora (§12C.5). A desk that marks a claim off the disclosure statement's single waterfall is marking a path-dependent option at one point on one path.

**Kaz's question.** "If the 6s and the 3% 2045s are in the same class, why does the 2045 trade two points lower?" Same priority, different claim, Theo says: a bond's claim is principal plus interest accrued to the petition date (§502(b)(2)), and the 6s missed an \$18mm coupon. Duration stopped mattering on the petition date. Two bonds fourteen years apart in maturity now differ by a few points of accrued interest.

**The delta, again.** Chapter 12-B showed that a class's expected sensitivity to value is $\pi_j/C_j$. A mixture adds a second sensitivity, to the distance between the experts (a cousin of vega). Halvorsen's unsecured pool has a small fulcrum probability and most of its value in the committee's hump, so moving the committee's expert from 1,900 to 1,800 costs it more than moving the debtor's from 1,300 to 1,200 (§12C.10).

Used in / builds on: §12B.6 (the call-spread identity and $\pi_j/C_j$), §6-B.1 and §6-B.3 (payoffs and Greeks), §5.5.1 (the waterfall as a distribution), §13.3 (an uptier as the difference of two waterfalls, which is what a DIP is in court), §14.6 (the court as a random variable), Law 16.

## 12C.3 The §1129 Constraint Set

At PJT the confirmation requirements were a checklist that counsel ran in the last month of the case. On the desk they are something more useful: a set of constraints that cut the distribution of plan outcomes into a feasible region and an infeasible one. A plan outcome that violates a constraint does not happen. It gets litigated, re-cut or withdrawn, and each of those is a different state of the machine in §12B.5.

ROBO's second attempt makes the point. Told after the cold open to "minimize objections," it found the one plan nobody objects to: every class unimpaired and paid in full in cash on the effective date. The plan needs \$2.8bn of exit financing for a company worth \$1.3bn. Nobody votes against it, because unimpaired classes are deemed to accept (§1126(f)), and nobody can confirm it, because §1129(a)(11) requires that confirmation not be likely to be followed by liquidation or a further reorganization. "It's feasible," Kaz says, "in the sense that the plan is feasible to type."

> **Math, Gently.** *What a constraint does to a distribution.* Take a distribution of outcomes and a rule that says "nothing below 20 is allowed." Two different things can happen to the probability that used to sit below 20. If outcomes below 20 are simply impossible, because the plan would be redrawn until it pays at least 20, that probability piles up *at* 20: the curve gets a spike, a *point mass*, at the floor. If outcomes below 20 instead mean the plan fails and something else happens (conversion, a new plan), that probability leaves the picture and has to be reported on its own line. The first is *censoring at a floor*, the second is *truncation*. Recovery models get this wrong in both directions: they draw a smooth curve through a floor that the statute guarantees, or they put mass at a floor that really belongs to a different state. Example: if 10% of the plan-value draws would give a class 15 when its liquidation value is 20, the engine reports "10% of paths fail best interests" and does not quietly mark those paths at 20. Chapter 5's inflated Beta (§5.5.3) is the general machinery.

Here are the constraints in the order a plan meets them, each with what it does to the engine.

**Classification and impairment (§1122, §1124).** Claims may be placed in one class only if they are substantially similar, which still leaves the proponent room to split similar claims for a reason other than manufacturing a vote. A class is *unimpaired* if its rights are left unaltered or, under §1124(2), if defaults are cured and the debt is *reinstated* at its original maturity and terms. Reinstatement is the cheapest exit financing ever invented: the debtor keeps a pre-crisis coupon in a post-crisis market, and the lender, being unimpaired, does not vote. When the lender objects and loses, practitioners call it *cram-up*. Charter Communications did it in 2009 with its senior bank debt, over the agent's objection. In the engine, reinstatement is a flag that sets a class's recovery to par in cash-equivalent terms while the *value* of what it holds is its old coupon discounted at today's spread, which can be well below par.

**Voting (§1126).** A class accepts if holders of at least two-thirds in amount and more than one-half in number of the allowed claims *actually voting* vote yes. The court may designate (disqualify) votes not cast in good faith under §1126(e). The Second Circuit's *DBSD* decision (2011) did both things that matter to a desk: it upheld the designation of the votes of a strategic buyer that had bought claims to gain control, and it held that a senior class may not "gift" value to old equity past an objecting intermediate class. Turnout is a position (§12B.3), and so is a blocking stake, as long as the court agrees you bought it to get paid.

**Best interests (§1129(a)(7)).** Every holder in an impaired class who did not accept must receive at least what it would get in a Chapter 7 liquidation. This is a floor *per holder*, not per class, and the liquidation analysis in the disclosure statement is where it is published.

> **[SOURCE EXTRACTION]** *Moyer_Distressed_Debt_Analysis p.104:* "The liquidation analysis generally does not play a very important role. The concept of the 'best interests test' is that no creditor should receive less in a reorganization than it would have in a liquidation — which is usually easily satisfied since the test typically is prepared using very conservative 'fire-sale' liquidation assumptions." (Footnote markers omitted.)
>
> **Annotation.** For a banker writing a plan, Moyer is right: the floor rarely binds. For the desk, "rarely binds" is the point. Exhibit D is a free, audited, adversarially reviewed lower bound on every class's recovery, published months before any recovery is paid. It gives the Beta recovery model of §5.5 the hard left edge it never had, and it is the recovery in the "conversion to Chapter 7" state of 12-B's chain. Its known bias (fire-sale assumptions) makes it a conservative floor, which is the right kind of floor for a model of the left tail.

**Administrative claims and the cash wall (§1129(a)(9)).** Administrative and priority claims, including 503(b)(9) goods claims and every professional's fees, must be paid in full in cash on the effective date unless the holder agrees otherwise; certain priority taxes may be paid over five years from the petition. That is a hard cash requirement, and when it cannot be met the case is administratively insolvent. In the engine it is a flag: exit cash plus exit financing must cover the wall, or the path does not confirm.

**Feasibility (§1129(a)(11)).** The court must find the plan unlikely to be followed by liquidation or another reorganization. In practice that is five years of projections, a capital structure the projections can service, and an expert who says so. Feasibility is the 13-week model's older sibling: the same question, "does the cash run out?", asked over sixty months instead of thirteen weeks, with less granularity and more optimism. In the engine it is a proxy test: projected free cash flow against exit debt service under a downside case.

**Cramdown (§1129(b)).** If a class rejects, the plan can still be confirmed if at least one impaired class accepts (not counting insiders, §1129(a)(10)), the plan does not discriminate unfairly against the dissenting class, and it is fair and equitable to it. "Fair and equitable" means something different for each type of class:

- *Secured classes* (§1129(b)(2)(A)) must keep their liens and receive deferred payments with a present value at least equal to their collateral, or receive the proceeds of a sale (subject to credit bidding), or receive the "indubitable equivalent." The present-value test makes the cramdown interest rate a strike (§12B.6 and §12C.5).
- *Unsecured classes* (§1129(b)(2)(B)) must be paid in full in present value, or no junior class may receive or retain anything on account of its claims. That is the absolute priority rule.
- *Equity* (§1129(b)(2)(C)) gets the same rule one level down.

Three refinements decide real cases. The **§1111(b) election** lets an undersecured class elect to have its whole claim treated as secured; it then must receive payments totaling the full claim, with present value at least equal to its collateral. It is the lender's defense against a lowball valuation: if the collateral is later sold for more than the cramdown value, the lien still secures the full claim, so the election is a call on the valuation being wrong. The **new-value corollary** lets old equity keep an interest by contributing new money, but after *203 North LaSalle* (1999) only if the opportunity is exposed to a market test. And **unfair discrimination** is a horizontal test: two classes of equal priority cannot be treated materially differently without a reason. The Third Circuit's *Tribune* decision (2020) applied it to contractual subordination and asked whether the difference in recoveries was material, not whether it existed.

**Releases after *Purdue*.** On 27 June 2024 the Supreme Court held in *Harrington v. Purdue Pharma L.P.* that the Bankruptcy Code does not authorize a plan to release claims against non-debtors without the consent of the affected claimants. Since then the fights have moved to what counts as consent: opt-out forms, opt-in forms, and whether silence on a ballot is agreement. Courts have not answered the same way in every district. For the desk, a plan whose economics depend on third-party releases (a sponsor contributing cash in exchange for being released, say) now carries a confirmation-risk jump: a ruling date with a binary outcome, which is Law 16 in its purest form.

Each test becomes one line of the engine's output. Best interests is a floor per class, reported as the fraction of paths that would breach it. The cash wall and feasibility are Boolean flags. The cramdown tests are bounds on what a dissenting class can be forced to take, and the transfer a cramdown rate creates is computed explicitly (§12C.5). No flag may silently pass when an input is missing. A missing liquidation analysis returns "unknown," not "pass," because ROBO, unprompted, will treat an empty floor as a floor of zero, and a floor of zero always passes.

Used in / builds on: §12B.5 (confirmation requirements as edges), §12B.3 (voting and turnout), §12B.6 (absolute priority, *DBSD* and *203 North LaSalle*), §5.5.3 (inflated Beta), §5.1.5 and §11.4 (the 13-week model as hazard and runway), Ch 13-B (the *Purdue* jump and the opt-out fights), App A §A.9 (cram-up and the absolute priority rule).

## 12C.4 The DIP as a Package of Derivatives

Here is the transaction you used to put on a single slide titled "DIP Summary of Terms": a super-priority term loan, a margin, some fees, a roll-up, milestones and a conversion feature. The desk decomposes it into pieces, prices each, and adds them up, because the pieces have different owners and the coupon turns out to be the smallest of them.

Halvorsen's DIP, provided by the first-lien ad hoc group (illustrative terms): \$150mm of new money at SOFR plus 800bp, a 3% upfront fee taken as original issue discount, a 2% exit fee, a 1:1 roll-up of \$150mm of the group's own prepetition term loans, milestones (a disclosure statement approved by day 100, confirmation by day 160, effective date by day 190), and an option to convert the DIP into the exit term loan. Expected tenor: six months.

> **Math, Gently.** *Adding up a fee stack.* A fee paid once on a short loan is a large rate. Pay 3% up front on a loan that lasts six months and you have earned 3% in half a year, which is roughly 6% a year. Add a 2% exit fee over the same six months and that is another 4% a year. Add the margin and the base rate, about 11.5% a year in our example (SOFR at 3.5% plus 800bp), and the all-in rate is roughly $11.5\% + 6\% + 4\% \approx 21.5\%$ a year before compounding. This is the *internal rate of return* in its simplest form: the one rate that makes what you paid out equal to what you got back. The shorter the loan, the more a one-time fee is worth per year, which is why DIP lenders like fees and milestones that shorten the case. The full version, cash flow by cash flow, is the yield calculation of §4B.2.

**Piece 1: the loan.** A \$300mm super-priority priming claim against term collateral worth \$960mm at plan value is a loan at about 31% loan-to-value with a court order in front of it. Its default risk is small. The new money's coupon, for six months, earns about \$8.6mm. (We assume that only the new money earns the DIP margin; where the rolled loans earn it too, add that interest to the roll-up line below.)

**Piece 2: the fees.** \$4.5mm up front and \$3.0mm at exit. Together with the coupon, about \$16mm on \$150mm of new money in six months: the 21.5% annual rate of the box.

**Piece 3: the roll-up.** Chapter 12-B derived the transfer. With tranche face $F$, value available $W$, new money $M$ and roll-up ratio $\kappa$, the holders who stay behind lose

$$
R - R' = \frac{\kappa M\,(F - W)}{F\,(F - \kappa M)} ,
$$

which for Halvorsen ($F = 1{,}400$, $W = 910$, $M = 150$, $\kappa = 1$) is 4.2 points. Count dollars instead of points, because conservation is the check that keeps everyone honest. Without the roll-up, the \$150mm of rolled loans would have recovered 65.0%. With it, they are paid in full, a gain of \$52.5mm. That gain is paid by the 1,250 of first-lien claims left behind, at 4.2 points each, also \$52.5mm. The group holds 662 of those 1,250, so it pays \$27.8mm of the bill to itself. The other \$24.7mm comes from first-lien holders outside the group. The group's net gain from the roll-up, \$24.7mm, is larger than its coupon and fees combined. Figure 12-C.2 shows that ledger, and how the left-behind recovery falls as the roll-up grows.

![Figure 12-C.2: A roll-up pays the rolled holders out of the holders left behind, dollar for dollar (left: \$52.5mm, or 4.2 points on the 1,250 of first-lien claims left behind), and the cost to those left behind accelerates as the roll-up grows (right: 9.5 points at 2:1). Illustrative: the roll-up formula of §12C.4 with tranche face 1,400 and value available 910.](assets/figures/ch12c_rollup_transfer.png)

That is the sense in which **the DIP is an uptier with a judge's signature.** Chapter 13 showed that an uptier is the difference of two waterfalls, one before and one after the participants' claims are promoted (§13.3). A roll-up is the same subtraction with §364 in place of the credit agreement's amendment section. The difference is that a judge signs the order after a hearing, which is why the transfer is smaller, disclosed and occasionally litigated rather than large, sudden and litigated always.

Two variants matter. A *creeping* roll-up promotes prepetition claims in proportion to each draw, so the transfer accrues as the DIP is drawn rather than on day one. And the guard in the formula matters: it applies only while $W \ge \kappa M$. If the rolled claims exceed the value the class would receive, the roll-up is taking value from somewhere else (usually the unsecured pool, through a lien on previously unencumbered assets), and the formula understates the transfer. The engine refuses to compute it rather than report a wrong number.

**Piece 4: the conversion option.** If the DIP lender may convert its DIP claim into the exit term loan, it holds a put: it can stay invested at terms set during the case when the reorganized company's credit is good, and take cash (from exit financing someone else provides) when the terms look thin. If the option belongs to the debtor, it is a call that removes refinancing risk at the effective date. Who holds the option is the first thing to look up in the DIP credit agreement. In Incora (§12C.5) the DIP was exchanged into exit notes.

**Piece 5: milestones.** Missing a milestone is a DIP default, and a DIP default lets the lender push the case toward a sale. Milestones therefore shorten the maturity of every class's option on plan value. The classes holding out-of-the-money calls (the unsecured, old equity) lose time value, and the classes that are short calls (the senior lenders, who are capped at par) gain. Shortening the case also cuts the administrative burn (§12C.7), which the fulcrum pays. A milestone is a put the debtor writes on its own optionality, and the juniors pay the premium.

**Piece 6: the backstop.** When the DIP or the exit financing includes an equity rights offering, the parties who backstop it are paid a premium, often in shares at a discount. That is the put priced in §16.3, and after the 2025 *ConvergeOne* ruling (below) it is also a test of equal treatment.

Add the pieces for the group: about \$16mm of coupon and fees, \$24.7mm of net roll-up transfer, a conversion option, and control of the calendar. On \$150mm for six months, the coupon is the least interesting number.

> **View From Another Seat.** *Four seats at the DIP hearing.* **The DIP lender** (an opportunistic credit fund seat) sees the safest loan it will make all year and the cheapest way to defend a first-lien position: if it does not lend, someone else may prime it. Apollo's public description of its own capital ladder (apollo.com, Hybrid Value page: "Credit" at 0–50% loan-to-value, described as "dislocation-driven," and "Hybrid Value" at 50–80%) is a useful map even for funds that never do a DIP: a DIP is the bottom of the 0–50% band with a court order attached. **The first-lien holder outside the group** sees the same loan as a 4.2-point tax, and its only levers are the objection deadline, the adequate-protection package and the local rule that requires the debtor to flag the roll-up for the court. **The CLO manager** often cannot write the new-money check at all: many CLO indentures restrict buying new obligations of a defaulted borrower, and the manager runs its portfolio inside a set of tests that a non-income-earning or non-qualifying asset breaks (§16.1, §21.8). It is the holder most likely to be left behind by a roll-up, through no view on the credit. **The official committee** sees a DIP whose milestones shorten its challenge period and whose liens may reach unencumbered assets, and it bargains for a carve-out, a longer challenge window and an exclusion of avoidance actions from the DIP collateral, which is where its recovery lives (§12B.9).

> **Docket Diary.** *Revlon: the roll-up priced, then the class bought (sources: Revlon 2020 10-K; Second Circuit No. 21-487; Davis Polk; dates as filed).*
> - **7 May 2020.** Out of court, a BrandCo credit agreement provides \$815mm of new-money term loans and a \$950mm roll-up commitment that lets 2016 term lenders swap into the new paper at par; \$846mm of 2016 loans are rolled. Brand IP moves to BrandCo subsidiaries that do not guarantee the 2016 loan. Roughly a dollar of roll-up for each dollar of new money: a $\kappa \approx 1$ deal, with no judge.
> - **August 2020.** The 2016 loan trades at 20 to 30, per the Second Circuit. Excluded lenders authorize a suit; it is never served.
> - **15 June 2022.** Chapter 11 in the Southern District of New York.
> - **21 February 2023.** The restructuring support agreement is amended to add 2016 lenders holding more than 94% of their class.
> - **3 April 2023.** Plan confirmed. Equity and a \$670mm rights offering are distributed 82% to BrandCo B-2 lenders and 18% to 2016 and B-3 lenders; the offering is backstopped 82% by B-2 lenders; non-electing 2016 and B-3 lenders share \$56mm in cash; accepting unsecured classes share a \$44mm settlement pool; B-1 lenders take take-back term loans (Davis Polk).
>
> *The Ad Hoc Group, represented by counsel, notes that the 2016 lenders' 18% was the price of a signature, and that a class which sues you is a class whose vote you can buy.*

The Revlon arithmetic is the roll-up formula run backwards. The 2020 transaction promoted the participants' claims out of court; the 2023 plan paid the left-behind class a negotiated share of value to settle its challenge and deliver its vote. What the desk could have modeled in 2020 was the size of the transfer. What it could have modeled in 2022 was the price of a settlement as an option on the litigation (§12B.9's challenge clock), which is what the 18% turned out to be.

> **Trend Watch.** *The roll-up moves to the center of the DIP, 2020–2026.* In 2005 Moyer described the roll-up as something prepetition lenders are "sometimes" able to do (Moyer p.98, quoted in §12B.5). Since 2020 it has become the main economic term of many DIPs, because the groups that led out-of-court uptiers are the natural DIP lenders in the cases that follow. The dated markers: Revlon's 2020 roll-up of \$846mm at roughly 1:1 (above); Incora's \$300mm DIP, exchanged into exit notes at emergence on 31 January 2025 (Davis Polk); Saks Global's \$1.75bn DIP in January 2026, with a \$1bn new-money first-out piece at SOFR plus 11% PIK and a final order on 20 February 2026 (The Fashion Law's case timeline). On the other side of the ledger, in September 2025 the district court in *ConvergeOne* reversed a confirmation because an exclusive backstop for majority lenders violated the equal-treatment rule of §1123(a)(4), and minority lenders' recoveries were about 30% lower within the same class (Harvard Law School Bankruptcy Roundtable, 25 November 2025); the ruling is on appeal. And in July 2026 the *Serta* remand put a price on an out-of-court promotion gone wrong: \$261.13mm plus 9% interest against the participating lenders (Mayer Brown, July 2026). What it means for the desk: the in-court roll-up and backstop are now priced against a litigation tail that did not exist in 2020, and the equal-treatment question has moved from the credit agreement to the plan.

Used in / builds on: §12B.5 (the roll-up formula and §364's ladder), §13.3 (the uptier as a difference of waterfalls), §13.5 (co-ops and RSAs), §16.3 (backstops), §21.8 (CLOs inside the case), Law 8.

## 12C.5 Exit Financing and the Take-Back Note

A plan pays most classes in paper, and the paper has a coupon somebody chose. When a secured class rejects and is crammed down, the court chooses. When the class accepts, the plan proponent chooses, and the class's vote ratifies it. The arithmetic is the same either way; only the referee differs.

> **Math, Gently.** *Duration as a price-to-yield exchange rate.* Modified duration $D^{\text{mod}}$ answers one question: if the yield on a bond rises by one percentage point, by roughly what percent does its price fall? A five-year bond with $D^{\text{mod}} \approx 3.8$ loses about 3.8% of its price for each point of yield. Now notice that a coupon set two points *below* the market rate is economically the same as a bond whose yield is two points too high for its coupon: it is worth about $2 \times 3.8 = 7.6\%$ less than face. The full version, with convexity, is §4B.3.

So the first-order value of a take-back note with face $F^{\text{tb}}$, priced $\Delta s$ below the market spread for that risk, is face minus a transfer:

$$
\text{Transfer} \approx F^{\text{tb}} \, D^{\text{mod}} \, \Delta s .
$$

Chapter 12-B's exact version is $P/S = 1 - (y - c)\,a_n(y)$. For an annual-pay bond priced at par, the annuity factor $a_n(y)$ and modified duration are the same number, so the two agree to the decimal for small gaps; for large gaps or long notes, use the exact price (§4B.2). The transfer does not vanish. It goes to whoever owns the residual, which is usually the class receiving the equity.

**Who sets $\Delta s$.** In a cramdown of a secured class, §1129(b)(2)(A) requires deferred payments whose present value equals the collateral value, so the court must pick a discount rate. The Supreme Court's plurality in *Till* (2004, a Chapter 13 case) endorsed a formula: prime plus a risk adjustment, typically one to three points. In *Momentive* (2d Cir. 2017) the Second Circuit held that in Chapter 11 the market rate applies where an efficient market exists, with the formula as the fallback. Every cramdown rate fight is a fight over $\Delta s$, and the first-order transfer tells you, before the hearing, how many dollars each basis point is worth. For a \$500mm note with duration 4, it is \$200,000 per basis point.

**Halvorsen's take-back, and a transfer inside one class.** The plan gives the first lien \$350mm of five-year take-back notes and the new equity. Each holder may elect more notes and less equity, or the reverse, within the \$350mm cap. The CLOs in the class elect notes, because their documents treat equity badly (§16.1); the ad hoc group elects equity. The plan proponents (the same ad hoc group) set the coupon at 8.0% when comparable exit first-lien paper yields 10.0%. With $a_5(10\%) = 3.791$, the notes are worth $1 - 0.02 \times 3.791 = 92.4$ per 100, and the transfer is \$26.5mm. At the plan's 59.2% recovery, the note electors surrendered \$591mm of claims for \$350mm of notes now worth \$323.5mm, a realized 54.7%. The equity electors' \$659mm of claims receive equity worth \$390mm plus the \$26.5mm the company no longer pays in interest, a realized 63.2%. One class, one plan, one election offered to everyone, and an 8.5-point gap between the two halves. Every holder was treated equally in the sense of §1123(a)(4), because every holder had the same choice. The price of the choice was set by the holders who chose the other side.

That is the same economics as the roll-up of §12C.4, moved from the front of the case to the exit: a within-tranche transfer from the holders who cannot take one form of consideration to the holders who wrote the terms of the other. The desk that owns first-lien loans next to a CLO-heavy register should model the election, not the class.

**Reinstatement as the zero-coupon-gap case.** If the legacy debt's coupon is below today's market rate, reinstating it under §1124(2) is a take-back note with a *negative* $\Delta s$ from the debtor's point of view: the estate keeps cheap debt it could never issue today. That is why "nobody gets crammed down who could have been crammed up." Exercise 4 makes it precise.

**The solvent branch.** When value covers every claim, the waterfall's last strike moves: unsecured creditors may be owed post-petition interest before equity sees anything, and the question becomes at what rate. Hertz is the canonical case (§16.6), and the make-whole and post-petition-interest circuit split lives in §15.1 and §16.6.

> **Docket Diary.** *Incora/Wesco: the DIP becomes the exit, and the ruling moves the split (sources: Wesco district court opinion, 8 Dec 2025; Octus; Davis Polk; Milbank).*
> - **1 June 2023.** Chapter 11 in the Southern District of Texas, with a same-day adversary proceeding over the March 2022 uptier.
> - **10 July 2024.** Oral ruling: the 2026 indenture was breached and the liens on all 2026 notes survive. The pre-ruling plan had given the uptier participants 96.5% of the equity (Octus).
> - **27 December 2024.** A consensual plan is confirmed, built on the rulings, with appellate rights preserved.
> - **31 January 2025.** Emergence. Secured noteholders receive 98.4% of the equity plus \$420mm of take-back notes; unsecured creditors about 1.6% and \$7.5mm; the \$300mm DIP is exchanged into exit notes alongside \$100mm of new money (Davis Polk; Milbank).
> - **8 December 2025.** The district court sustains the participants and dismisses the contract claims. The minority noteholders give notice of appeal in early January 2026 (press reports).
>
> *The Ad Hoc Group, represented by counsel, observes that it was the fulcrum before lunch and the second lien after it.*

Read Incora through this chapter's lens and three things stand out. The DIP's conversion into exit notes is Piece 4 of §12C.4 exercised. The take-back notes are §12C.5's paper. And the equity split moved because a ruling moved attachment points: whose liens survived decided which holders sat in the fulcrum class. A plan confirmed with appellate rights preserved is a security whose terms are a contingent claim on an appeal, which is Law 16 with a CUSIP.

Used in / builds on: §12B.6 (the cramdown price), §4B.2–4B.3 (price, yield and duration), §16.1 (who can hold equity), §16.6 (Hertz and the solvent debtor), §15.1 (the make-whole split), Ch 13-B (the Incora litigation).

## 12C.6 363 Sales, Stalking Horses and Credit Bids as Options

Sometimes the cleanest way to find out what a company is worth is to sell it. Section 363 lets the debtor sell assets free and clear, with liens attaching to the proceeds, and the auction replaces the expert fight with bids. But the auction has rules, and the rules are written in the bid-procedures order weeks before anyone bids.

**The stalking horse.** The first bidder signs a purchase agreement at price $S$ and, in return, gets a break-up fee $b$ and expense reimbursement $e$ if it is topped. A rival must bid at least $S + b + e$ plus a minimum overbid increment $m^{\text{ob}}$. If $B$ is the most a rival will pay, the estate receives

$$
\Pi = S + (B - S - b - e)\,\mathbf{1}\{B \ge S + b + e + m^{\text{ob}}\}.
$$

That is a floor at $S$ plus what option traders call a *gap call* on the rival's bid: it pays nothing until the rival clears the trigger, and then pays the rival's excess over $S + b + e$. The estate pays for the floor only in the states where it did not need it, which is why break-up fees of a few percent survive objection: the fee buys a public, binding floor from the one bidder willing to go first (§12B.5).

**The credit bid.** Under §363(k) a secured lender may bid its claim instead of cash. Think about what an extra dollar of bid costs it. If the lender is owed $F_s$ against collateral worth less, bidding a dollar more reduces its deficiency claim by a dollar, and that deficiency would have recovered only the unsecured rate $r_u$. So the marginal cost of a credit bid is $r_u$ per dollar, not one dollar, and when $r_u$ is near zero the lender's reservation price is its face, whatever the market thinks the assets are worth. Cash bidders must beat a number that costs the lender almost nothing. The Supreme Court held in *RadLAX* (2012) that a plan sale free of liens must allow the secured creditor to credit bid; courts may still limit a credit bid "for cause," and *Fisker* (Bankr. D. Del. 2014) capped one near what the bidder had paid for the claim rather than its face, to keep a cash auction alive.

**The melting ice cube.** Debtors seeking a fast sale argue that value is decaying (customers leaving, vendors tightening terms). The argument is often true and always convenient: speed shortens every junior option's maturity (§12C.4, Piece 5) and limits the time for a rival to do diligence. The desk point is about timing. Junior paper gaps on the **bid-procedures order**, which fixes $S$, $b$, $e$, $m^{\text{ob}}$, the credit-bid rights and the calendar. By the sale hearing the option has been written and mostly priced.

Used in / builds on: §12B.5 (the sale path; *Jevic*), §16.6 (an auction for the plan sponsor role), §25.6 (the bid-procedures order as a docket event).

## 12C.7 Admin Burn, KEIPs and the Clock

Every day of a case is paid for, in cash, ahead of every prepetition class. Chapter 12-B priced that with a resolvent. Here is the same idea as an option Greek.

> **Math, Gently.** *Theta.* An option's *theta* is how much its value changes as one day passes with nothing else changing. A long-dated call usually loses value as time passes, because it has less time to get lucky. Bankruptcy equity has a second, cruder source of theta: its strike rises every day by the fees the estate pays. A call whose strike drifts up by \$5mm a month loses value even if the company does not change at all. The full version of the Greeks is §6-B.3.

Old equity in a Chapter 11 case is a call on value struck at *every* claim ahead of it, administrative and priority claims included, plus the fees still to be incurred before the effective date. Write the strike as $K(T) = \sum_j C_j + \text{Adm}_0 + \phi T$. The derivative of the call's value with respect to its strike is minus the probability that it finishes in the money, so the burn alone costs the equity

$$
\frac{\partial E}{\partial T}\bigg|_{\text{burn}} = -\phi\;\mathbb{P}\big(V > K(T)\big)
$$

per year, on top of the ordinary time decay. In words: admin burn costs old equity the fee rate times its chance of being paid. For the fulcrum, which pays the burn dollar for dollar while it remains the fulcrum, the same logic gives $\phi\,\pi_j/C_j$: at Halvorsen's \$60mm a year, each month of valuation fight costs the first lien about 0.4 points while it is the fulcrum, and its fulcrum probability is 83%. The committee's expert, deposition and two hearing days are administrative claims too (§330, §503(b)). The first lien is paying for the report that argues it is overpaid.

**KEIPs as free forecasts.** Since 2005, §503(c)(1) has made retention payments to insiders very hard to approve, so management compensation in a case is written as an incentive plan with metrics, and the metrics must be hard enough to survive an objection from the U.S. Trustee that the plan is retention in disguise. That constraint makes the key employee incentive plan motion an unusually honest document. Management must propose targets that are neither a lay-up nor out of reach, under oath, with its own pay at stake. Halvorsen's KEIP pays at threshold, target and stretch EBITDA of \$175mm, \$190mm and \$205mm. At the debtor's 7.0x those are values of about \$1,225mm, \$1,330mm and \$1,435mm: management's bonus plan brackets the debtor's range almost exactly and puts no weight near the committee's \$1,900mm. In a sale case the KEIP tiers are written on sale proceeds instead, which discloses management's view of the auction. Either way the desk parses the motion as data (§25.6) and treats it as one more expert, with a known incentive.

Used in / builds on: §12B.7 (the fee burn as a resolvent), §6-B.3 (theta), §16.6 (Hertz's equity during the case), §25.6 (the KEIP motion and other docket events).

## 12C.8 The Tax Line, Worked

A disclosure statement's tax section is forty pages written to be skipped. Two of its numbers move recoveries: how much cancellation-of-debt income the plan creates, and how much of the company's net operating losses survive it. (This section is the tax appendix's interim home.)

**The mechanics, in the order they bite.** Forgiven debt is income (§61(a)(11)). A debtor in a title 11 case excludes it entirely (§108(a)(1)(A)); outside bankruptcy, an insolvent debtor excludes it only to the extent it is insolvent (§108(a)(1)(B), (a)(3)). Excluded income is not free: under §108(b) the debtor reduces its tax attributes by the excluded amount, NOLs first, after computing the year's tax, and then other attributes including asset basis. When the debtor issues stock for debt, it is treated as paying the debt with cash equal to the stock's fair market value (§108(e)(8)), so the cancellation income depends on the same valuation the experts are fighting about. Then §382: if 5% shareholders increase their ownership by more than 50 percentage points over three years, the company has an *ownership change*, and its annual use of pre-change NOLs is limited to the value of its stock times the long-term tax-exempt rate. Two bankruptcy branches modify that. Under §382(l)(6) the value is measured *after* creditors' claims are converted, so the limit is roughly $\ell = \rho^{\text{LT}} \times E^{\text{conf}}$. Under §382(l)(5) there is no annual limit if historic shareholders and "qualified" creditors (broadly, long-term holders and ordinary-course creditors) end up with at least half the stock, but the NOLs are cut by interest deducted on the converted debt in the prior three years, and a second ownership change within two years eliminates them.

That last branch is why debtors file an **NOL trading order** on the first day: it restricts anyone from becoming a holder of 4.5% or more of the stock (and, for (l)(5) cases, of certain claims) without notice. It is a docket event that tells you the debtor thinks the NOLs are worth protecting (§25.6).

> **Math, Gently.** *Present value of a tax shield.* An NOL is not cash. It is the right to skip paying tax on future income, so its value is the tax you skip, discounted. With a 21% tax rate, \$100mm of NOL used in full next year saves \$21mm next year, worth about \$19mm today at a 10% discount rate. The same \$100mm used at \$10mm a year for ten years saves \$2.1mm a year, worth about \$12.9mm today. A limit on the *speed* of use, which is all §382 is, cuts value without cutting the face. The full version is the annuity arithmetic of §4B.2.

Write $\chi$ for the corporate tax rate (we avoid $\tau$, which is the default time) and $N_t$ for the NOL used in year $t$. Then

$$
\text{PV(NOL)} = \sum_{t \ge 1} \chi \,\min\!\big(\ell,\ \text{NOL}_{t-1},\ \text{TI}_t\big)\,(1 + r)^{-t}, \qquad \text{NOL}_t = \text{NOL}_{t-1} - N_t ,
$$

where $\text{TI}_t$ is taxable income, $N_t$ is the minimum in the sum, and $\ell = \infty$ when no limit applies. (Post-2017 NOLs also cannot offset more than 80% of taxable income; the engine applies that cap inside $\text{TI}_t$.)

**Halvorsen, worked.** Say the company carries \$600mm of NOLs and expects taxable income of about \$87mm a year before using them; take $\chi = 21\%$, $r = 10\%$ and an illustrative long-term tax-exempt rate of 3.5%.

| Route | Cancellation income | NOL after §108(b) | Annual limit | PV of the shield |
| :--- | ---: | ---: | ---: | ---: |
| Out of court: \$850mm of notes for \$510mm of new notes, no stock | 340 | 260 | none | about 45 |
| Out of court, with an ownership change (stock issued) | 340 | 260 | 3.5% × old equity of 30 = 1.05 | about 2 |
| In court, (l)(6), *if* cancellation income were 340 | 340 | 260 | 3.5% × 390 = 13.7 | about 24 |
| **The actual plan** | **1,495** | **0** | — | **0** |

*(Illustrative; \$mm. The first route is the sponsor's failed exchange of §12B.9 had it reached its minimum. Cancellation income in the plan is \$510mm on the first lien, which receives \$740mm for \$1,250mm, plus \$985mm on the unsecured class, which receives \$35mm for \$1,020mm.)*

The table explains two things a banker sees and rarely writes down. A sponsor prefers an out-of-court exchange below the ownership-change threshold because it keeps the surviving NOL at full speed, while an out-of-court ownership change measures the limit off a nearly worthless old equity. And in a deeply impaired plan, attribute reduction eats the NOL before §382 can limit it: Halvorsen's \$1,495mm of excluded income wipes out the \$600mm of NOLs and then reduces asset basis (no lower than the liabilities that remain, under §1017(b)(2)). The tax benefit that survives lives in depreciation, not in the NOL row. **Do the attribute reduction before you do the §382.** The NOL trading order still gets filed, because if the committee's expert wins, the cancellation income shrinks and the question reopens.

Used in / builds on: §12C.1 (the valuation fight, which is also a tax fight through §108(e)(8)), §12B.9 (the sponsor's exchange), §16.1 (the post-reorg equity whose value sets $\ell$), §25.6–25.8 (the NOL order and the claims register as docket data).

## 12C.9 Three Banker Models, Three Desk Models

The aha of this chapter, in one table. You already built the inputs. The desk's version of your old job is your old job with a probability measure attached.

| Banker model (disclosure-statement exhibit) | What it becomes on the desk | Where it lives in the book | File and function |
| :--- | :--- | :--- | :--- |
| 13-week cash flow model; five-year projections (Exhibit C) | The runway covariate in the hazard model; the feasibility test (§1129(a)(11)) | §5.1.5, §11.4, §12C.3 | Listing 11.3's `runway` feature; `plan_value_engine.feasibility_proxy()` |
| Liquidation analysis (Exhibit D) | The best-interests floor; the left edge of the recovery Beta; the recovery in the conversion state | §5.5, §12B.7, §12C.3 | `plan_value_engine.best_interests_flags()` |
| Recovery waterfall at plan value (Exhibit E and the plan's treatment table) | The waterfall run under $f_V$ with moving strikes: fulcrum probabilities and recovery distributions | §12B.6, §13.7, §12C.2 | `plan_value_engine.fulcrum_probabilities()` on 12-B's `silo_waterfall` and Ch 13's `waterfall_clearing` |
| Sources and uses at exit | The overhang schedule of who receives what they cannot hold; the take-back transfer | §16.2, §12C.5 | Listing 16.5's `ForcedSellerOverhang`; `plan_value_engine.takeback_note_transfer()` |

Theo's USB stick appears in the first row, for the last time in Part IV. When Exhibit C posts, he recognizes the column widths: the debtor's advisors use the same 13-week template he used for four years, conditional formatting and all. "Congratulations," Kaz says. "The USB stick is now evidence."

## 12C.10 The Halvorsen Files, Part III: The Plan Under Uncertainty

The structure is §12B.9's, unchanged: ABL 150; a first-lien class of 1,400 (TLB 900 and 7.25% secured notes 500, pari passu); unsecured notes 850; trade 150, of which 40 are 503(b)(9) goods; lease rejection 60. The DIP is \$150mm of new money with a 1:1 roll-up, so 1,250 of first-lien claims remain. The day-71 settlement is in the numbers: the first lien hands \$20mm to the unsecured pool, which is \$35mm at plan value. Value splits as in 12-B, with ABL collateral at 250 and the rest divided 32:3 between term collateral and unencumbered value. On those terms, per dollar of claim,

$$
R_{1\text{L}}(V) = \min\!\left(\frac{\tfrac{32}{35}(V - 250) - 220}{1{,}250},\ 1\right), \qquad
R_{\text{U}}(V) = \frac{\tfrac{3}{35}(V - 250) - 55 + \tfrac{32}{35}\,(V - V^\star)^+}{1{,}020},
$$

where $V^\star \approx 1{,}858$ is the plan value at which the first lien is paid in full. (The 220 is the DIP's 300 less the 100 of ABL residual, plus the \$20mm settlement; the 55 is administrative claims of 75 less the same \$20mm.) Both are call spreads, scaled by the share of value each class can reach. At $V = 1{,}300$ they give 59.2% and 3.4%, which is where 12-B left them.

Now put the mixture of §12C.1 on $V$: the debtor's expert at 1,300 with $\sigma_1 = 0.10$ and weight 0.7, the committee's at 1,900 with $\sigma_2 = 0.12$ and weight 0.3. With the formulas of §12C.2 and a normal table, by hand:

| Output | First lien (outside the group) | Unsecured pool |
| :--- | ---: | ---: |
| Fulcrum probability | 82.8% | 17.2% |
| Expected recovery, mixture | 70.3% | 8.3% |
| Expected recovery if the debtor's expert wins | 59.7% | 3.5% |
| Expected recovery if the committee's expert wins | 95.2% | 19.4% |
| 5th / 95th percentile | 46.2% / 100% | 1.9% / 35.2% |
| Paths below the best-interests floor (21.6% and 0%) | 0.0% | 0.0% |

*(Illustrative. Old equity's fulcrum probability rounds to zero; it needs $V$ above \$2,795mm.)* Three flags complete the report. The best-interests floor never binds, as Moyer predicted, and the engine says so rather than assuming it. The cash wall binds below about \$1,125mm, where unencumbered value no longer covers the \$75mm of administrative claims and the first lien's settlement money starts paying them instead of the pool: about 5% of paths. Feasibility passes on the downside projections with exit debt of \$800mm.

Look at the shape before the numbers. The first lien's distribution has a hump around 60 and a spike at 100: it is a short call capped at par, and almost a third of its expected value comes from the committee's hump, where it is paid in full. The unsecured pool's distribution has a hump around 3 and a long right tail that lives entirely in the committee's scenario. Moving the committee's expert from 1,900 to 1,800 costs the unsecured about 1.8 points of expected recovery; moving the debtor's from 1,300 to 1,200 costs about 0.6. The unsecured class is short the *distance* between experts, not the level of either. Figure 12-C.3 draws both distributions.

![Figure 12-C.3: Under the plan-value mixture the first lien's recovery has a hump near 60 and a spike at par (17.2% of paths), while the unsecured pool's has a hump near 3 and a long right tail that comes almost entirely from the committee's expert; the means are 70.3% and 8.3%. Illustrative: the mixture and class formulas of §12C.10, with each bar split by which expert the judge adopts (dark: the debtor's; light: the committee's).](assets/figures/ch12c_recovery_distributions.png)

**What the market said.** On the night of the cold open the 6s traded at 14. The table's two conditional recoveries, 3.5 and 19.4, imply that 14 is priced as if the committee's expert wins about two times in three. The first lien at 66 is within a risk premium and nine months of carry of the model's 70.3. The desk's view is about $w$, and it is a view about a judge (Law 16).

**The DIP moves the fulcrum; the roll-up does not.** Generalize the DIP to new money $M$ with roll-up ratio $\kappa$. The first lien is whole when term collateral covers the DIP, its remaining claims and the settlement, which happens at $\tfrac{32}{35}(V - 250) = 1{,}320 + M$. The roll-up ratio cancels: rolled claims are paid either way, only earlier. New money that is spent inside the estate raises the strike, so every \$100mm of new money moves $V^\star$ up by about \$109mm. Figure 12-C.4 plots the result. The unsecured class's fulcrum probability falls from about 25% with no new money to 17% at \$150mm and to 10% at about \$280mm. The roll-up decides who inside the first lien gets paid; the new money decides whether the first lien gets paid at all.

![Figure 12-C.4: Fulcrum probability by class as DIP new money varies, Halvorsen, roll-up ratio 1:1 (the curves are identical for any ratio). The unsecured class's probability falls from about 25% with no new money to about 17% at the actual \$150mm and 10% near \$280mm; the first lien takes the rest. Illustrative: the mixture of §12C.1 with the first-lien strike $V^\star(M)$ of §12C.10.](assets/figures/ch12c_fulcrum_prob_vs_dip.png)

**The take-back, priced.** The \$350mm of five-year notes at 8% against a 10% market transfers \$26.5mm from note electors to equity electors (§12C.5). The CLOs that elect notes are, almost to the dollar, the first-lien holders outside the ad hoc group. They lose 4.2 points to the roll-up at the start of the case and 4.5 points to the coupon at the end, for being the holders who could not fund new money or hold equity. Figure 12-C.5 draws the transfer against the coupon gap.

![Figure 12-C.5: The take-back transfer as a function of the coupon gap $\Delta s$, for Halvorsen's \$350mm five-year note: the first-order line $F^{\text{tb}} D^{\text{mod}} \Delta s$ (grey, dashed; about \$13.3mm per 100bp) and the exact annuity price of §12B.6 (blue), which agree closely below 300bp. The plan coupon is held at 8.0%, so the market yield is 8.0% plus the gap, and the marked point is the plan's 200bp gap, \$26.5mm. Illustrative.](assets/figures/ch12c_takeback_transfer.png)

### When to apply it, and when it breaks

The engine is built for a contested plan with a published disclosure statement, identifiable experts and strikes that will not move much before confirmation. It works best in the six weeks before a valuation hearing, when $w$ is the only thing anyone is arguing about.

It breaks in recognizable ways. When value is set by a **market test**, the mixture is the wrong object: price the bids (Hertz, §16.6). When a **ruling can move liens**, the strikes themselves are random, and the engine needs a regime variable on the attachment points, not just on $V$ (Incora). When the business's value is **binary** (a license renewal, a mass-tort settlement, a single customer contract), a lognormal hump hides the jump; add a Bernoulli component, as in §5.1. When the plan pays in **warrants, rights or deathtrap consideration**, recovery at plan value is not recovery, and §16.3–16.4 must price the paper. And a $w$ fitted on a dozen cases is a story, not an estimate (Law 12). What a seasoned practitioner checks first is none of the math: who holds the fulcrum class, whether they want to own the company, and whether the debtor's valuation is attached to a support agreement with them.

Used in / builds on: §12B.9 (the structure and the challenge settlement), §12C.2–12C.8 (every piece above), §16.1–16.4 (Halvorsen's new equity and warrants), §28.9 (the dashboard row for a restructuring position).

## 12C.11 Case Study: Envision, the Plan Value With a Date on It

"You want the regularity with a date on it," Mags says, the week after the Halvorsen disclosure statement. "Envision." She has the plan open on one screen and a 2025 press report on the other, and she tells it the way she tells everything, out of order and correctly.

Here is the record in order. KKR bought Envision Healthcare in 2018, in a deal reported at roughly \$10bn. By 2022 the company was two businesses in one capital structure: the physician-staffing business, which carried most of the debt and most of the trouble, and AmSurg, the ambulatory surgery centers, which carried most of the value. In April 2022 a drop-down moved AmSurg out of the reach of Envision's lenders: a new AmSurg first-lien facility of about \$1.3bn, about \$1.1bn of proceeds paid up to Envision, and AmSurg designated an unrestricted subsidiary. Between June and August 2022 AmSurg raised about \$1.3bn of second-lien money, lent it to Envision, and Envision repurchased about \$1.9bn of its own debt at a discount; participants were prioritized and the rest went to a "fourth-out" position. Octus puts participation at about 91% (a figure we have not confirmed). By November 2022, by one report, AmSurg debt traded around 98 while Envision's first lien traded around 25 (an advocacy source; treat as approximate). One company, two silos, two prices seventy points apart.

On 15 May 2023 Envision filed in the Southern District of Texas (No. 23-90342, before Judge Christopher Lopez), with two silos and **no DIP**. That last fact matters for this chapter. With no new money and no roll-up, the strikes barely moved during the case; the uncertainty was almost entirely in value and in the litigation over the 2022 transactions. A dissenting lender group's adversary proceeding was dismissed with prejudice on 9 November 2023. An independent director, Gary Begeman, reported on 15 September 2023 that the 2022 transactions had produced about \$1.7bn of quantified benefit and found no fraud. The creditors' committee settled for \$35mm in cash and 1.5% of the reorganized Envision equity for noteholders.

The plan was confirmed on 11 October 2023 and went effective on 3 November 2023. On the AmSurg side the revolver and the first lien were paid in full. The AmSurg second-lien lenders, who had funded the 2022 transactions, took 100% of the reorganized AmSurg equity, together with a \$300mm rights offering priced at a 30% discount, for a projected recovery of 73%. On the Envision side the second-out lenders took the equity and the unsecured notes took warrants. Total debt fell by more than 70%.

Then the date. On 17 June 2025 Ascension agreed to buy AmSurg for a reported \$3.9bn, about \$250mm above the top of the plan's valuation range, and Octus estimated a return of more than 1.3 times for the drop-down lenders.

"So the fulcrum wanted the company," Theo says, "and the fulcrum got a value that let it own all of it."

"And a rights offering at a 30% discount on top," Mags says. "Which only the fulcrum could buy. Read §16.3 and tell me what the put was worth."

Kaz has drawn it as this chapter would. AmSurg is a single silo with the first lien paid in full and the second lien as fulcrum; the plan value sets how many shares the second lien's claim buys, and the plan value was low enough that the claim bought all of them. A high plan value would have left room above the second lien's detachment point for someone else, and nobody below the second lien in that silo was strong enough to argue for one. "The judge didn't pick from two humps," Kaz says. "There was one hump, and it belonged to the people who were going to own the company."

That is the cleanest version of the regularity in §12C.1. When the class that will own the company also writes the plan and faces no credible expert on the other side, the confirmed value sits at the conservative end of the debtor's range, and the market, given time and a buyer, pays the difference to the new owners. The 73% "projected recovery" was a recovery at plan value. The realized recovery, measured at Ascension's price, was something else.

What could a desk have modeled in 2023? Not the Ascension bid, which nobody could forecast. It could have modeled the shape: one silo, one strong fulcrum holder, no DIP, no competing expert, a discounted rights offering reserved for the fulcrum. Under this chapter's engine that is a mixture with $w$ near one on a low hump, and a recovery on the reorganized equity whose physical-measure expectation sits above the plan's 73%. The trade was to own the fulcrum's paper, or the post-reorganization equity once it could be bought, and to be patient. Chapter 16's overhang machinery says why patience paid: the natural holders of AmSurg's new equity were the funds that wanted it, not CLOs that had to sell it.

What could not be modeled from the documents: whether the sponsor-era litigation would survive (it did not), and whether healthcare-services multiples would hold up through 2024 (they did). The desk's edge in Envision was not a better DCF. It was knowing that the number in Exhibit E had an owner.

Used in / builds on: §12C.1 (the regularity), §13.6 (the drop-down as collateral leakage), §16.1–16.3 (post-reorg equity, overhang and rights offerings), Ch 13-B (the Envision docket diary and the 2022 transactions).

> **From the Shop Floor (fictional composite).** *A bank's distressed claims desk, a Tuesday in month eight.* The risk committee meets at 4:15, and the first question is the one it always asks: why is this number different from yesterday? The Halvorsen trade-claims mark has gone from 3.4 to 3.2 overnight. Priya, the desk's claims analyst, has the answer, and it took her most of the morning. Nothing traded. The claims agent's register, which she downloads every night as a CSV that changes its column order without warning, shows a new \$74mm contract-rejection claim from a former resin supplier, filed on the bar date. The unsecured denominator went from 1,020 to 1,094; \$35mm over 1,094 is 3.2%. The committee asks whether the claim will be allowed. Priya says the debtor will object, that objections take months, and that the desk's model now carries the claim at 60% expected allowance with a distribution, which is why the mark is 3.2 and not 3.3 or 3.1. The second item is worse. The desk's books show \$4.12mm face of trade claims bought from three vendors; the register shows \$4.07mm. The missing \$50,000 is a 503(b)(9) portion the debtor has reclassified as administrative, which is *good* news (it will be paid in cash at par), but the assignment agreement's recourse clause means the vendor may owe the desk a refund on the reclassified piece, or may not, depending on a definition on page 11. Priya spends an hour matching Rule 3001(e) notices to assignment agreements, one of which was scanned sideways. Nobody on the committee asks about plan value. It is, she reflects, the most important number in the case, and the least of her problems this week.

## 12C.12 Specification for AI Implementation: `plan_value_engine.py`

**What ROBO built from the vague version.** "Maximize plan value" produced the cold open's \$4,075mm, with everyone paid in full and old equity keeping 40%. "Minimize objections" produced a plan needing \$2.8bn of exit financing for a \$1.3bn company. Both were literal answers to instructions that never said whose value, under which measure, and subject to which constraints. The specification below fixes all three.

**The problem it solves at this point in the story.** By now the reader can price each piece of a contested plan by hand: the mixture on value, the call spreads, the roll-up, the take-back, the burn, the floor, the tax line. Doing that for every class, every DIP size and every expert weight by hand is how §12C.10 took an afternoon. The engine does it in one pass, keeps the pieces separate so each can be audited, and refuses to report a flag it could not compute.

**What it computes, and why it is built this way.** It draws confirmed plan values from a lognormal mixture (one component per expert, weights for the judge), truncated at zero, with a fixed seed so a risk committee can reproduce yesterday's number. For each draw it runs the class waterfall: collateral silos first, then administrative claims against unencumbered value (the cash wall), then the unsecured pool with any waived deficiencies removed. That ordering is 12-B's `silo_waterfall`, re-implemented here only because a plan's deficiency waiver and settlement transfers are not in 12-B's function; the self-test checks that the two agree when there is no waiver, and checks a single-silo stack against Chapter 13's `waterfall_clearing`. The DIP enters as a priming claim of $M(1+\kappa)$ ahead of the primed class, with the rolled claims removed from that class. Recoveries are recorded per class per draw, so that fulcrum probabilities, means, percentiles and floor breaches all come from the same paths.

**Inputs.** A claims register: classes with faces, ranks within each collateral silo, and which classes share the unsecured pool. Silo values as a function of $V$ (fixed amounts plus shares of the remainder). DIP terms: new money $M$, roll-up ratio $\kappa$, upfront and exit fees, expected tenor, base rate and margin. The mixture: medians, log-volatilities and weights. The liquidation analysis: a recovery floor per class, or `None` if not yet filed. Exit terms: take-back face, coupon, tenor and the market yield for comparable paper. Administrative claims at plan, the burn rate $\phi$ and the expected time to the effective date. Optional tax inputs: NOLs, cancellation income, the long-term tax-exempt rate, tax rate, taxable income, discount rate. All money in \$mm, rates as annual decimals, recoveries as fractions of allowed claim.

**Outputs.** `fulcrum_probabilities()`: probability that each class is the fulcrum, with old equity as the last entry. `recovery_distribution()`: per class, mean, median, 5th and 95th percentiles, and the fraction of paths below its best-interests floor. `best_interests_flags()`, `cash_wall_flag()` and `feasibility_proxy()`: each returns `True`, `False` or `None`, and `None` means an input was missing. `dip_package_value()`: coupon, fees, and the roll-up's gross transfer and net gain to the lender group, with a conservation check. `takeback_note_transfer()`: the exact and first-order transfers. `nol_value()`: the present value of the surviving NOL under the chosen §382 branch, after attribute reduction.

**When to use it, and when not.** Use it for a contested plan before confirmation, and to ask "what if" about DIP size, expert weights and coupon gaps. Do not use it to value the enterprise: $V$ is an input with an author. Do not use it once a market test has set value, or where a pending ruling can move liens, unless you add a regime variable on the strikes (§12C.10).

**The edge case that bites.** The roll-up formula assumes the rolled claims are covered by the value the class receives, $W \ge \kappa M$. When they are not, the roll-up is taking value from outside the class and the closed form understates the transfer; the engine raises an error instead of returning a number. The second bite is the boundary $V = K_j$, inherited from 12-B: the class is whole and the next class is the fulcrum at zero, so the comparison must be strict. And a missing floor must never become a zero floor.

*The full python listing is [Listing 12-C.1 in Appendix F](#code-12c-1).*

Used in / builds on: §12B.10 (`restructuring_state_machine.py`, whose `Silo`, `silo_waterfall`, `rollup_transfer` and `cramdown_price` it imports), §13.7 (`waterfall_clearing`), §16.8 (the post-reorg book that consumes its recovery distributions), §25.6–25.8 (the docket and claims feeds that update its inputs), §28.9 (the dashboard).

## 12C.13 Desk Debrief

The valuation opinion arrives on a Friday at 4:52 p.m., as they do. The judge adopts \$1,300mm, finding the committee's discount rate "unsupported by the record" and its peer set "aspirational." The 6s, which traded at 14 the night of the cold open, open Monday at 4. The holders who bought them at 14 had paid for a two-in-three chance that the committee's expert would win; Theo's mixture had given it three in ten. Theo's distribution put 83% on the first lien as the fulcrum, and the first lien's paper, 59.2 at plan value, trades six months after emergence at the equivalent of about 71, because the market values the reorganized Halvorsen near the top of the debtor's range. Envision, again, in miniature.

Mags reads the opinion twice. "Before anyone takes a bow for the first lien, half of that rally was the whole distressed tape. Strip it out. IDO or it didn't happen."

Kaz is staring at Figure 12-C.1. "So the judge is the measure change," they say. They are not wrong: the confirmation order maps a mixture onto a point, and every claim in the case is repriced at once.

- **Plan value is a negotiated random variable. Trade the distribution, not the midpoint.** The mean sits in the valley between the experts, the median is not the midpoint, and the price tells you the market's weight on each expert. (Laws 4, 16)
- **The fulcrum is a probability, and its strikes move.** DIP priming, adequate protection, the burn, post-petition interest and rulings all shift attachment points while the case runs. (Law 7)
- **The DIP is an uptier with a judge's signature.** New money moves the fulcrum; the roll-up moves recovery inside the class; the coupon is the least interesting line. (Law 8)
- **Best interests is a floor you can read for free.** Exhibit D is the left edge of every recovery distribution, published months early. A missing floor is unknown, never zero. (Law 11)
- **Admin burn is the theta of bankruptcy equity, and the fulcrum pays for both experts.**
- **Nobody gets crammed down who could have been crammed up.** Reinstatement is the cheapest exit financing ever invented, and a take-back coupon is a transfer you can price before the hearing.
- **Do the attribute reduction before you do the §382.**

**The Spec You Hand the Robot.** "Implement `plan_value_engine.py` per §12C.12: draw confirmed plan values from a seeded lognormal mixture (medians, log-vols, weights summing to one); run a silo waterfall per draw with the DIP priming at $M(1+\kappa)$, administrative claims paid before the pool, and settlement gifts that stop once the source is whole; report fulcrum probabilities with a strict whole test, recovery mean, median, 5th and 95th percentiles and best-interests breaches per class; return `None`, never `True`, for any flag whose input is missing; price the DIP package with a conservation assertion and refuse the roll-up formula when $W < \kappa M$; price take-back transfers exactly and to first order; value NOLs after §108(b) attribute reduction. \$mm, annual decimals, fractions of allowed claim, measure $\mathbb{P}$. Self-test against §12B.9 (60.8%, 1.5%), §12C.10 (59.2%, 3.4%; 83/17) and Chapter 13's `waterfall_clearing`."

### Exercises

1. *(The roll-up at 2:1.)* Recompute Halvorsen's roll-up transfer with $\kappa = 2$, holding $M = 150$, $F = 1{,}400$ and $W = 910$. *Solution:* $\kappa M = 300 \le W$, so the formula applies: $300 \times 490/(1{,}400 \times 1{,}100) = 9.5$ points, more than double the 1:1 case, because the denominator shrinks as well. Non-participants recover $610/1{,}100 = 55.5\%$.
2. *(How much DIP is too much?)* Using §12C.10's mixture, find the new money $M$ at which the unsecured class's fulcrum probability falls to 5%. *Solution:* $0.3\,[1 - \Phi(z)] = 0.05$ gives $z = 0.967$, so $V^\star = 1{,}900\,e^{0.116} \approx 2{,}134$; then $\tfrac{32}{35}(2{,}134 - 250) = 1{,}320 + M$ gives $M \approx$ \$400mm. The roll-up ratio does not enter.
3. *(The take-back.)* Price the transfer on a \$500mm take-back note set 300bp below market with modified duration 4. Then do it exactly for a five-year annual-pay note at 7% when the market yields 10%. *Solution:* $500 \times 4 \times 0.03 = $ \$60mm to first order; exactly, $500 \times 0.03 \times a_5(10\%) = 500 \times 0.03 \times 3.791 = $ \$56.9mm.
4. *(Crammed up.)* Show that reinstating legacy debt beats a crammed note for the residual owner whenever the legacy coupon is below the court's rate, and price \$800mm of 5% debt with four years left when the market yields 9%. *Solution:* each transfers $F(y - c)\,a_n(y)$ with its own $c$, so the lower coupon transfers more, and reinstatement needs no vote. Here $800 \times 0.04 \times a_4(9\%) = 800 \times 0.04 \times 3.240 \approx$ \$104mm moves from the lender to the equity.
5. *(Theta.)* A solvent-looking debtor burns \$120mm a year of fees, and old equity finishes in the money with probability 0.6. What does a three-month delay cost the equity through the burn alone? *Solution:* $\phi\,\mathbb{P}(V > K) = 120 \times 0.6 = $ \$72mm a year, so about \$18mm for three months.
6. *(ROBO's plan, marked to market.)* Under ROBO's \$4,075mm plan, what does the first lien actually recover if the market values the company at \$1,300mm, and which test does the plan fail? *Solution:* equity at plan is \$3,200mm, of which the first lien holds 900/3,200 = 28.1%. At market the equity is worth $1{,}300 - 800 - 75 = 425$, so the first lien gets $350 + 0.281 \times 425 \approx 470$, or 37.6%. That clears its 21.6% liquidation floor and fails the absolute priority rule, since old equity receives about \$170mm while the first lien is short. It passes best interests and fails fairness.

### Deep-Dive Resource Graph

- **Podcasts:** *Cloud 9fin*, "The In-Court Report with Cat Corey: The latest on backstop fees in rights offerings and DIP financings," with Vince Buccola (9 Dec 2025), https://share.transistor.fm/s/ad684efa : backstop and DIP fees after *ConvergeOne*. *Cloud 9fin*, "Eat, sleep, drive: Breaking down the Del Monte, Serta & American Tire trifecta" (21 Jul 2026), https://share.transistor.fm/s/1c4df313 : roll-ups and pro rata language in 2026 DIP fights. *Cloud 9fin*, "Unjustice for all" (21 Aug 2024), https://share.transistor.fm/s/70cc3e30 : *Purdue* and what a plan can release. *The Octus Download*, "EP 22 | Judge Michael B. Kaplan, Vegas Squeeze & the First Brands Conspiracy" (23 Dec 2025), https://share.transistor.fm/s/aaf0387e : a sitting judge on feasibility and aggressive DIPs. *Cloud 9fin*, "It Hertz you to see it," with Max Frumes (26 Jun 2024), https://share.transistor.fm/s/d607390a . Bloomberg *Odd Lots*, "Inside the Blood Sport of Creditor-on-Creditor Violence," with Sujeet Indap (25 Nov 2024), https://omny.fm/shows/odd-lots/inside-the-blood-sport-of-creditor-on-creditor-vio . *Capital Allocators*, "Max Frumes and Sujeet Indap: Inside the Sausage Factory of the Caesar's Restructuring" (EP.209, 16 Aug 2021), https://www.capitalallocators.com/podcast/inside-the-sausage-factory-of-the-caesars-restructuring/ .
- **Practitioner Writing:** Moyer, *Distressed Debt Analysis* (Moyer_Distressed_Debt_Analysis pp. 98, 104, 252, 355, 369). Davis Polk, "Revlon Chapter 11 plan confirmed," https://www.davispolk.com/experience/revlon-chapter-11-plan-confirmed ; Davis Polk, "Incora emerges from Chapter 11," https://www.davispolk.com/experience/incora-emerges-chapter-11 ; Octus, "Court Opinion Review: July 2025" (Envision and AmSurg), https://octus.com/resources/articles/court-opinion-review-july-2025/ ; Harvard Law School Bankruptcy Roundtable on *ConvergeOne* (25 Nov 2025), https://bankruptcyroundtable.law.harvard.edu/2025/11/25/outnumbered-not-outplayed-minority-lenders-successfully-challenge-exclusive-backstop-agreement-on-equal-treatment-grounds-in-convergeone/ ; Cleary Gottlieb, "Recent Developments in DIP Financing," *GRR Americas Restructuring Review 2024*, https://www.clearygottlieb.com/-/media/files/grr-americas-restructuring-review-2024--recent-developments-in-dip-financing.pdf ; The Fashion Law, "Saks Global's Chapter 11: A Running Timeline," https://www.thefashionlaw.com/saks-globals-chapter-11-a-running-timeline-of-the-bankruptcy-case/ ; Mayer Brown on the *Serta* remand (July 2026), https://www.mayerbrown.com/zh-hans/insights/publications/2026/07/serta-simmons-bedding-the-fifth-circuits-uptier-decision-and-the-landmark-damages-ruling-on-remand .
- **More Episodes and Posts:**
  - **How Bankruptcy Really Works: Inside the System with Josh Sussberg** (*The Octus Download*, EP 21, 10 Dec 2025). A Kirkland & Ellis restructuring partner on how the 2005 amendments shortened exclusivity and pushed negotiation earlier, the institutional source of the clock that §12C.7 prices as theta. https://share.transistor.fm/s/81750469
  - **Shall I compare thee to an English restructuring?** (*Cloud 9fin*, Linklaters' Michael Torkin and James Warboys with Will Macadam, 14 Oct 2026). English plans as the foreign cramdown that US-listed borrowers now weigh against Chapter 11, a useful contrast to the §1129 constraint set in §12C.3. https://share.transistor.fm/s/f41535d8
  - **EP 29 | Spirit's Final Flight, AMC Hangs On & The Parent Trap** (*The Octus Download*, 7 May 2026). The DIP lenders' veto in practice: the episode reports a floated \$500mm federal bailout evaporating when they said no, which is the "control of the calendar" piece of §12C.4 seen from outside. https://share.transistor.fm/s/18e1e6ed
  - **The Backstop Party** (Vincent S.J. Buccola, Adi Marcovich Gross and Matthew R. McBrady, *American Bankruptcy Law Journal* Vol. 100, Issue 1, 10 Apr 2026). Data on 49 bankruptcies since 2016 for pricing the backstop as a put; the authors report that in 18 of the 19 deals with an arm's-length value estimate, the securities sold exceeded the exercise price. Read it beside Piece 6 in §12C.4 and the Envision rights offering in §12C.11. https://www.ablj.org/the-backstop-party-vol-100-issue-1-html/
  - **Restructuring Trend: The Ultrafast Prepack for Private Credit Deals** (Proskauer, David M. Hillman, 4 Nov 2019). FullBeauty Brands (24 hours) and Sungard Availability Services (19 hours) show the case clock collapsing to under a day, the limit of the burn argument in §12C.7. https://www.proskauer.com/pub/restructuring-trend-the-ultrafast-prepack-for-private-credit-deals
- **Academic Papers:** Gilson, Hotchkiss and Ruback (2000), *Valuation of Bankrupt Firms*, Review of Financial Studies; Hotchkiss (1995), *Postbankruptcy Performance and Management Turnover*, Journal of Finance; Weiss (1990), *Bankruptcy Resolution: Direct Costs and Violation of Priority of Claims*, JFE.
- **Data & Code:** `plan_value_engine.py` (§12C.12, Appendix F); Title 11, https://www.law.cornell.edu/uscode/text/11 ; Hertz's 8-K/A on the plan sponsor auction (14 May 2021) and 8-K on the effective date (7 Jul 2021), linked in §16.6.

Used in: §13.3 and §13.5 (the in-court sequel to the uptier and the RSA), §14.4 and §14.6 (recovery as a mixture; rulings as regime switches), §16.1–16.4 and §16.8 (the plan's securities and the post-reorg book), §25.6–25.8 (the docket events this chapter reads: disclosure statements, KEIP motions, NOL orders, bid procedures, claims registers), §28.9 (the dashboard), App E Laws 4, 7, 8, 11, 16.

<!-- STATUS: COMPLETE -->
