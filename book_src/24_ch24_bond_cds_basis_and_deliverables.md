# Chapter 24: Bond-to-CDS Basis & Deliverable Obligation Mechanics

*Fiction label: the desk, Halvorsen Packaging, its bonds, its swap and every number in this scene are invented (illustrative).*

*Tuesday 20 October 2026, 7:41 a.m., Theo's fifth week.* Theo had written the trade on a sticky note. On this desk that counted as either retro or a compliance event. *Buy \$10mm Halvorsen Packaging 6% Senior Notes due 2031 at 88. Buy \$10mm five-year Halvorsen CDS at 370 bp. Bond Z-spread: 480. Basis: −110.*

"A hundred and ten basis points of riskless carry," Kaz said. "If they default, the swap pays par minus recovery, the bond pays recovery, and we're flat. It's a tautology with a coupon."

"But what does the credit agreement say?" Theo asked.

"There is no credit agreement. It's a swap."

"Then what do the Definitions say?"

Kaz blinked. "Is a 'deliverable obligation' the one with free shipping?"

Theo did not answer, because he had already opened the trade confirmation in one window and Halvorsen's debt schedule in the other, the way he used to open a credit agreement beside its third amendment and wait for the two to disagree. The confirmation ran to eleven pages, most of them incorporating other documents by reference, which made it feel like home. Reference Entity: Halvorsen Packaging Holdings, Inc. Credit Events: Bankruptcy, Failure to Pay. Deliverable Obligation Characteristics: Not Subordinated, Specified Currency, Transferable, Maximum Maturity 30 years, and a few more that he read twice. Nothing in it mentioned his 6% 2031s. The swap did not care which Halvorsen bond he owned. It cared which ones existed.

So he went down the other window line by line, the way you read a debt schedule when you suspect management put the interesting item on the last page. The 7.25% notes due 2029. His 6% 2031s. A secured term loan, which the swap's "senior unsecured" reference would not let him lean on. And at the bottom, issued in the spring of 2021, when anyone with a ticker could borrow for twenty-four years at three percent, a 3% senior unsecured note due 2045: same issuer, same guarantors, ranked equally with his bond. Nineteen years left, inside thirty. Not subordinated. Dollars. Transferable. He pulled the last print and wrote it at the bottom of the sticky note, under the basis: *3% 2045 — 52?* Then he drew a box around it.

"You drew a box," Kaz said.

"At PJT a box meant the number was going on page one of the board deck."

From the end of the row, without looking up from her run sheets, Mags said, "Bottom of the schedule. It's always the bottom of the schedule."

Ines put down her coffee. "What's the pot, what are the odds, and who at this table knows more than you? Start with the pot. Halvorsen files tomorrow. What do you make?"

Theo did it on the sticky note. "The bond drops from 88 to recovery, call it 40, so I lose 48 points. The swap pays 100 minus 40, so I make 60. Net plus twelve points on ten million." He frowned. "I'm over-hedged. The swap is a par instrument and my bond isn't at par."

"Good. Now suppose they don't file. Suppose they skip one coupon on one bond, on purpose, and the swap triggers anyway."

Theo looked at the box. "Then the bonds don't accelerate and trade on their cash flows. Halvorsen has a 3% 2045 from the 2021 bubble. It's deliverable, it's at 52, and it would be the cheapest thing in the auction." Theo stopped. "So the swap pays 48 whether or not anybody actually loses anything."

"Somebody paid for that 48," Ines said. "Find out who before you buy their side of it."

Theo turned the sticky note over, because the front was full. On the back he wrote the three numbers the trade now seemed to depend on, none of which had been on the front: the price of a bond he did not own, the date of a coupon he had not read, and the name of whoever decided what counted as a default. The 110 basis points had not moved. What they were a price *for* had.

Kaz pulled the bond's screen and the swap's screen side by side, as if they might be persuaded to agree by proximity. The bond said 480. The swap said 370. Both had traded that morning, both were quoted by the same three dealers, and both claimed to be the market's best estimate of how likely Halvorsen was to fail and how much it would hurt.

Kaz was rereading the confirmation. "So the question isn't whether the bond and the swap disagree. It's which one of them is lying."

That is the question this chapter answers. *When the bond and the CDS of the same company disagree, which one is wrong, by how much, and what exactly does the swap pay when the company dies, or when someone arranges for it to look dead?*

By the end of this chapter you will be able to price both legs of a CDS, translate a running spread into points upfront, compute four different "bases" for the same bond and say which one is honest, and turn funding, haircuts and repo specialness into an arbitrage band with a return on equity attached. You will also be able to value the cheapest-to-deliver option, simulate the two-stage credit event auction, build a mean-reversion basis signal that survives its costs, run the successor arithmetic, and flag orphaning and manufactured-credit-event risk before the Determinations Committee rules on it.

## 24.1 Two Doctors, One Patient, and the Frictionless Lie

The Part VI opener described four doctors looking at one patient. This chapter is about the two who argue most: the cash bond and the credit default swap. In a frictionless world they cannot disagree, and the argument for that is short enough to write on Theo's sticky note.

> **[SOURCE EXTRACTION]** *Schmid_Credit_Risk_Pricing_Models p.254:* "We short the par issued defaultable floating rate note and invest the money in a par issued default-free floating rate note and hold this portfolio either until to maturity or a credit event occurs"
>
> **Annotation.** Our analysis: this is the founding argument of the basis, and the rest of the chapter is a list of the ways it fails. The portfolio pays a fixed spread every period and receives $1-R$ if the issuer defaults, which is exactly the protection buyer's side of a CDS. So the CDS spread must equal the floater's spread, and the basis must be zero. On a 2026 desk almost nothing in the argument survives intact. Few issuers have par floaters outstanding, so you compare a swap with fixed-coupon bonds at 88 or 104. Shorting a corporate bond means borrowing it in a repo market that may charge you for the privilege. "Invest the money" assumes you can fund at the risk-free rate with no haircut. And "a credit event occurs" assumes the bond and the swap agree on what a credit event is. Each assumption breaks in its own section of this chapter, and each break has a sign and a size you can model.

The sticky-note version of Schmid's argument leans on one idea a restructuring banker does not use every day, and it is worth slowing down for.

> **Math, Gently.** *Replication, and the "probability" that is really a price.* Picture two vending machines side by side that dispense the same can. If one charges a dollar and the other a dollar twenty, somebody buys from the first and sells beside the second until the prices meet, and nobody has to agree on whether the can is any good. Replication is that argument with cash flows: two packages that pay the same amount in every state of the world must cost the same today. Now a tiny bond. It matures in one year and pays 100 if the issuer survives and 40 if it defaults; cash earns 4%. Suppose the market prices it as if default had a 5% chance. The "average" payoff is $0.95 \times 100 + 0.05 \times 40 = 97$, worth $97/1.04 \approx 93.3$ today, a yield of about 7.2% and a spread of about 3% over cash. That 3 is the 5% chance times the 60 points lost, give or take compounding. Here is the twist. The 5% is nobody's forecast. It is the number that makes the replication price come out equal to the price on the screen, which is why it lives under its own letter, $\mathbb{Q}$, and why a swap insuring the same 60 points has to charge the same 3 points a year: feed both machines the same 5% and they must agree. The forecast, the physical $\mathbb{P}$ probability, might be 2%, with the other point being what investors charge for carrying the risk. Chapter 6-B (§6-B.2 and §6-B.6) owns the full story; here we only need the vending machines.

Here is the argument in symbols. Let $r_{t}$ be the floating rate (SOFR after the 2021–2023 Libor cessation), and let coupon dates be $t_1 < \dots < t_n = T$ with accrual fractions $\alpha_i$. A par defaultable floater pays $(r_{t_{i-1}} + s^{\text{FRN}})\alpha_i$ at $t_i$ while the issuer survives. A par default-free floater pays $r_{t_{i-1}}\alpha_i$. Short the first and buy the second. Both cost par, so the package costs nothing. While the issuer survives, the package pays $s^{\text{FRN}}\alpha_i$ each period, because the floating legs cancel. If default happens on a coupon date $t_i$, unwind: the default-free floater has just reset, so it is worth exactly 1, and the defaulted floater is worth its recovery $R$. You receive $1-R$.

A protection buyer in a CDS with spread $s^{\text{CDS}}$ pays $s^{\text{CDS}}\alpha_i$ per period while the issuer survives and receives $1-R$ at default. The two cash-flow streams are the same up to the spread, and both packages cost zero. No-arbitrage under $\mathbb{Q}$ then forces

$$
s^{\text{CDS}} = s^{\text{FRN}}, \qquad b \equiv s^{\text{CDS}} - s^{\text{bond}} = 0.
$$

That is the whole frictionless theory of the basis. The basis $b$ is defined as CDS minus bond, in bp, with the bond spread measured one of several ways (§24.3). A *negative basis* means the bond is cheap relative to the swap: buy the bond, buy protection. A *positive basis* means the bond is rich: short the bond, sell protection.

> **[SOURCE EXTRACTION]** *Schmid_Credit_Risk_Pricing_Models p.254:* "If we allow for default not only at coupon times we liquidate the portfolio at the coupon date immediately after default. Then the relationship Default Swap = Default-Free FRN - Defaultable FRN is only approximately valid."
>
> **Annotation.** Our analysis: this is the smallest crack, and it is worth seeing why it is small. Between coupon dates the default-free floater is worth $B(u, t_i)(1 + r_{t_{i-1}}\alpha_i)$ rather than 1, which differs from par by roughly the interest accrued since the last reset, $r\,(u - t_{i-1})$, a few bp of price on a quarterly reset. The CDS, meanwhile, settles on its own timetable (credit event, auction, settlement about a month later), with the accrued premium paid up to the event. The mismatch is real but second order, worth a basis point or so. It matters because it shows the method: write down the replicating package, then find each place where the real cash flows leave the textbook's. The big leaks, funding, deliverables, and the definition of default, are each worth tens to hundreds of bp.

Each assumption hiding inside the frictionless argument has been somebody's entire P&L at some point, and the rest of the chapter cites them by label.

| Label | The assumption | Who broke it | Where |
| :--- | :--- | :--- | :--- |
| **A1** | The bond is a par floater. | Every fixed-coupon bond at 88 or 104 compared with a par instrument; the choice of convention moves the "basis" by 10–20 bp before any economics. | §24.3 |
| **A2** | You can fund the long bond at the risk-free rate, with no haircut. | The prime brokers of autumn 2008 and March 2020. | §24.4 |
| **A3** | You can short the bond for free, at general collateral repo with no specialness or borrow fee. | Any bond that goes special when everyone wants to be short it. | §24.4 |
| **A4** | Your counterparty survives your issuer. | The 2008 dealers whose own CDS widened alongside their clients' bonds. | §24.4 |
| **A5** | The swap pays $1-R$ on *this* bond. It actually pays par minus the auction price of the cheapest deliverable obligation. | Halvorsen's 3% 2045s in the cold open; Hovnanian's 5% 2040s for real. | §24.5–24.6 |
| **A6** | "Default" means the same thing to the bond and the swap. | Hovnanian, Windstream and every orphaning fight since. | §24.8 |

A5 is the one Theo found before he had a name for it. His package rested on a picture in which, if Halvorsen failed, his 6% 2031s and the swap would both be marked off the same recovery, so the two legs would cancel up to the over-hedge he had already spotted. In a bankruptcy that picture is nearly right, because a filing turns every senior unsecured bond into the same claim. In Ines's other world, one skipped coupon and no filing, his 2031s keep paying and keep trading near where they were, while the auction looks for the cheapest bond anyone can deliver and finds the 2045s at 52. The swap then pays 48 points on a company whose bonds, including his, have barely moved. His "hedge" would have turned into a bet on a bond he did not own, and the bet would have paid. Somebody, as Ines said, would have paid for it. He wrote "A5" next to the box on the sticky note, which was by now more box than note. §24.5 turns his discovery into an option with a price.

So the basis is not "free money," whatever the sticky note says. It is a price for bearing whichever of A1–A6 is currently broken, and the interesting work is finding out which one, and whether the price is high enough. That is the desk motto in another costume. The negative basis on Halvorsen is not alpha until you strip out the funding term, the convention term and the deliverable term. IDO or it didn't happen.

There is also a reason the quant desk cares less about single-name CDS than its 2007 predecessor did, and it is a market-structure reason.

> **[SOURCE EXTRACTION]** *Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.11:* "we believe that cash bonds will be the approach of choice for most quantitative investors, above all because breadth is key for quant strategies and is simply not available in synthetic form yet."
>
> **Annotation.** Our analysis: this is the fundamental law of active management (Chapter 9) applied to instrument choice. With $\text{IR} \approx \text{IC}\sqrt{\text{BR}}$, an investable universe of thousands of bonds beats a few hundred liquid single names even if the per-name signal is weaker. The 2026 data (Trend Watch below) make Man's "yet" look optimistic: single-name liquidity has concentrated further since 2022. The departure is in what CDS is *for* on a systematic desk. It is no longer the main alpha instrument. It is a hedge, a source of information (CDS moves first in liquid names; §24.7), and a legal instrument whose payoff you must model as a contract rather than as a spread. The basis is where all three uses meet.

> **Trend Watch: single names thin out while the index eats the market (2021–H1 2026).** *What changed:* ISDA's July 2026 study (*CDS Market Dynamics: Five Years of Activity and a Record 2025*, 29 Jul 2026) reports record global CDS traded notional of \$41.8tn in 2025, above the 2022 peak of \$38.7tn. Index CDS was 93.3% of it, and its share has been near 90% every year. Single-name notional peaked at \$3.3tn in 2023, the year of the regional-bank and Credit Suisse stress, and eased to \$2.8tn in 2025. *How concentrated:* only 20 of 751 single-name reference entities averaged ten or more trades a day in Q4 2025 (14 sovereigns, 6 others), against 69 in Q1 2023. The average single-name ticket was \$6.7mm in 2025, against \$54.3mm for index trades. Europe's Determinations Committee region accounted for 48.9% of single-name activity in 2025, and the Americas for 39.7%. *Stress signature:* relative to trailing four-quarter averages, single-name activity rose 84.8% in Q1 2023 (index +4.5%), while in the April 2025 tariff shock index activity rose 20.9% and single names *fell* 20.7%. Macro shocks go to the index and idiosyncratic shocks go to single names. ISDA's own line is that "higher traded notional does not mean deeper liquidity." *What it means for the desk:* a single-name basis signal exists for perhaps a few hundred names at any time, and the CDS leg of your basis trade may be the less liquid leg. Model the CDS bid–ask by name and by regime, not as a constant. And note that the April 2025 pattern means a negative-basis package hedged with single-name CDS can lose its hedge liquidity in exactly the macro shock that widens the basis.

## 24.2 Pricing the Swap: Two Legs and One Risky Annuity

A single-name CDS on a North American corporate trades on standardized terms that date from the April 2009 "Big Bang" protocol. There is a fixed running coupon $c$ of 100 or 500 bp, quarterly payment dates on the 20th of March, June, September and December, a full first coupon with an accrual rebate, auction settlement hardwired into the contract, and, for the Standard North American Corporate (SNAC) contract, no Restructuring credit event. Because the coupon is fixed, the price discovered on the screen is *points upfront*. The par spread quoted next to it is a translation, made with an agreed model and a conventional 40% recovery for senior unsecured names. Theo's 370 bp Halvorsen swap actually trades as a 500 bp coupon plus a payment *to* the protection buyer at inception. Every basis calculation starts by inverting that translation correctly.

Kaz's version is shorter. "A CDS is a bond whose coupons stop when the issuer dies, plus a put on the issuer's death. The first leg is an annuity, the second is a lottery ticket, and the spread is the exchange rate between them."

Theo asked for the exchange rate in numbers, and Kaz drew two pictures on the whiteboard instead.

> **Math, Gently.** *Part one: survival is a candle.* Picture a thousand candles, each with the same small chance of guttering out in any instant, no matter how long it has already burned. If that chance runs at a rate $\lambda = 5\%$ a year, then after one year $e^{-0.05} = 95.1\%$ of them are still lit, and after five years $e^{-0.25} = 77.9\%$. That curve, $S(t) = e^{-\lambda t}$, is the survival curve, and the waiting time until a given candle goes out has the exponential distribution that Chapter 5 (§5.3.3) and Chapter 6 (§6.1.4) introduce properly. *Part two: the risky annuity is a coupon that stops when the candle goes out.* Promise 1 bp a year, paid at each year-end for five years, but only if the candle is still lit, and discount at 4%. Each payment is worth survival times discount, $e^{-(0.05+0.04)t}$, so the five are worth $0.914 + 0.835 + 0.763 + 0.698 + 0.638 \approx 3.85$ bp today. Paid quarterly, with the premium accrued up to a default included, the same promise is worth about 4.06, the risky annuity of the next subsection. Kaz's lottery ticket is the other leg: it pays the 60 points lost at default, if default comes within five years, and at these numbers it is worth about 12.1 points. The exchange rate is $12.1/4.06 \approx 2.97\%$, the 297 bp par spread computed at the end of this section. And Theo's swap: the hazard that produces a 370 bp spread is about 6.2%, the annuity shrinks a little to about 3.95, and the 130 bp a year the buyer overpays by handing over the standard 500 bp coupon instead of 370 comes back to him at inception: $1.30 \times 3.95 \approx 5.1$ points upfront. The full version is next.

The two pictures are all the derivation needs. In symbols, the par spread is whatever running coupon makes the annuity leg worth exactly the lottery ticket, $s_{\text{par}} = \text{DL}/\text{RPV01}$, and the points upfront are what is left over when the coupon is fixed at 100 or 500 bp instead.

### 24.2.1 The Full Derivation: two legs, par spread and upfront

Work under the risk-neutral measure $\mathbb{Q}$ throughout this section. Let $\tau$ be the default time with deterministic intensity $\lambda_t$, so that survival is

$$
S(t) = \mathbb{Q}(\tau > t) = \exp\!\Big(-\int_0^t \lambda_u\,du\Big),
$$

and $-dS(t) = \lambda_t S(t)\,dt$ is the density of default at $t$. Let $B(t) = e^{-\int_0^t r_u\,du}$ be the OIS discount factor. We write $B$ rather than $D$ because $D$ is reserved for duration in this book. Assume rates and default are independent under $\mathbb{Q}$, so that expectations of products factor. Let premium dates be $t_0 = 0 < t_1 < \dots < t_n = T$ with ACT/360 accrual fractions $\alpha_i$; a 91-day quarter has $\alpha_i = 91/360 \approx 0.2528$.

**Premium leg.** The protection buyer pays $s\,\alpha_i$ at $t_i$ if the name survives to $t_i$. If default happens at $u \in (t_{i-1}, t_i]$, the buyer also owes the premium accrued from $t_{i-1}$ to $u$. The value of a running spread $s$ is $s \times \text{RPV01}(T)$, where the risky annuity is

$$
\text{RPV01}(T) = \sum_{i=1}^{n}\alpha_i\,B(t_i)\,S(t_i)\;+\;\sum_{i=1}^{n}\int_{t_{i-1}}^{t_i}\alpha_i\,\frac{u-t_{i-1}}{t_i-t_{i-1}}\,B(u)\,\big(-dS(u)\big).
$$

The first sum is a coupon annuity weighted by survival. The second sum is the accrued-on-default term. If default is roughly uniform within a period, the accrued fraction averages one half, and

$$
\int_{t_{i-1}}^{t_i}\alpha_i\,\frac{u-t_{i-1}}{t_i-t_{i-1}}\,B(u)\,\big(-dS(u)\big)\;\approx\;\frac{\alpha_i}{2}\,B\!\Big(\frac{t_{i-1}+t_i}{2}\Big)\,\big[S(t_{i-1})-S(t_i)\big].
$$

This is the approximation the reference code uses. Leaving out the second sum overstates the par spread by roughly $\tfrac12\lambda\alpha$ in relative terms, about 0.6% at $\lambda = 5\%$, or 2 bp on a 300 bp name. That error is small, persistent, and always in the same direction, which makes it a fake signal for a basis model.

> **[SOURCE EXTRACTION]** *Schmid_Credit_Risk_Pricing_Models p.159:* "Current market standards for banks and corporates require that the protection buyer pays the accrued premium to the credit event; sovereign default swaps do not require a payment of accrued premium."
>
> **Annotation.** Our analysis: the accrued term in RPV01 is a contract term, not a modeling choice. The quotation also records something that has since changed. The sovereign exception belongs to an older generation of confirmations. Today's standard contracts, sovereign and corporate, pay accrued premium to the event date. The lesson for a specifier is general. A pricing library that hard-codes market practice from the textbook it was written from will be wrong when the practice moves. Put every such convention (accrual on default, day count, step-in date, coupon, recovery for quoting) in a versioned contract-terms table, and have the pricer read it, so that a protocol change is a data change rather than a code change.

**Protection leg.** The protection seller pays $1-R$ (per unit notional) at default, if default occurs before $T$:

$$
\text{DL}(T) = (1-R)\int_0^T B(u)\,\big(-dS(u)\big) = (1-R)\int_0^T B(u)\,\lambda_u\,S(u)\,du.
$$

With flat $r$ and flat $\lambda$ this has a closed form:

$$
\text{DL}(T) = (1-R)\,\frac{\lambda}{\lambda+r}\,\Big(1-e^{-(\lambda+r)T}\Big).
$$

**Par spread.** The par spread equates the two legs:

$$
s_{\text{par}}(T) = \frac{\text{DL}(T)}{\text{RPV01}(T)}.
$$

**The credit triangle.** Pass to continuous premium payment with accrual on default, so the annuity becomes $\int_0^T B(u)S(u)\,du = \big(1-e^{-(\lambda+r)T}\big)/(\lambda+r)$ for flat curves. The ratio collapses to

$$
s_{\text{par}} = \lambda\,(1-R).
$$

The spread is the expected loss rate: the probability of default per unit time multiplied by the loss given default. This is the most useful identity in the chapter, and also the most abused, because it holds only under flat curves, continuous payment, a fixed recovery known in advance, and the 365/365 day count of a mathematician. On ACT/360 the quoted spread is lower by the factor $360/365$, about 4 bp on a 300 bp name. That is 4 bp of "basis" against a 30/360 bond that has nothing to do with credit.

**Points upfront.** With a fixed coupon $c$, the protection buyer pays at inception (per unit notional, before the accrual rebate)

$$
U = \big(s_{\text{par}} - c\big)\,\text{RPV01}(T).
$$

When $U$ is negative, as for Halvorsen at $s_{\text{par}} = 370$ bp and $c = 500$ bp, the buyer *receives* $|U|$. Two boundary conditions are worth turning into tests. At $c = s_{\text{par}}$, $U = 0$. As $\lambda \to \infty$, RPV01 goes to 0 and the upfront tends to $1-R$, which makes sense, since a contract on an issuer certain to default at once is worth the loss given default. The market uses a piecewise-flat hazard curve bootstrapped from the term structure of quotes, rather than our single flat $\lambda$, and the industry's standard upfront calculator (the ISDA CDS Standard Model) fixes these conventions so that both counterparties compute the same cash amount. Your basis engine should reproduce it to the cent before you trust anything it says about the basis.

> **[SOURCE EXTRACTION]** *Schmid_Credit_Risk_Pricing_Models p.255:* "Sometimes the default swap contract is specified such that the protection buyer must pay the default swap premium that has accrued since the last coupon date."
>
> **Annotation.** Our analysis: "sometimes" has become "always" for standard contracts, but the passage marks the place where the FRN replication of §24.1 meets the swap's own cash flows. The replicating package has accrued coupon at default (the floater's coupon since the last reset), and the swap has accrued premium at default. When both are present they largely offset. When a model includes one and not the other, the result is a systematic bias of order $\tfrac12 s\alpha$ per default. A specifier should test that both legs agree on whether accrual is paid: the sanity check in the code below does exactly this.

> **Ways This Blows Up.** (1) *Recovery used twice, differently.* The 40% used to quote upfront is a convention. The recovery you believe is a forecast. A basis model that bootstraps $\lambda$ with $R = 40\%$ and then values a bond with $R = 25\%$ has created a basis out of nothing. Bootstrap and value with the same $R$, and carry recovery uncertainty as a separate risk. (2) *$\lambda$ from a spread that isn't there.* For the more than 700 names that average fewer than ten trades a day (Trend Watch, §24.1), the "quote" is often a composite of stale runs. Carry a staleness timestamp with every CDS input and refuse to compute a basis from a CDS mark older than the bond print. (3) *Day-count drift.* Mixing ACT/360 premium, 30/360 coupons and continuous-compounding Z-spreads without converting is worth about 4 bp at 300 bp of spread, which is large compared with a 20 bp basis signal.

### Specification for AI Implementation (CDS legs, par spread and upfront)

**What ROBO built from the vague version.** Asked to "price a CDS," ROBO discounted the premium leg at the risk-free rate with no survival weighting. The swap came out worth the same on Halvorsen as on the US Treasury, and ROBO noted, accurately, that both counterparties had agreed to pay each other.

**The precise spec.** Inputs: flat $\mathbb{Q}$-hazard `lam` (per year, decimal), flat continuously compounded OIS rate `r`, maturity `T` in years, recovery `R` (fraction of par), quarterly ACT/360 premium. Outputs: `rpv01` (years, per unit notional), `protection_leg` (fraction of notional), `par_spread` (decimal), `hazard_from_spread` (inverse), and `upfront` (fraction of notional, positive when the buyer pays). Guards: maturity of at least one premium period; flat-curve closed form with a $\lambda + r \to 0$ branch; root bracket $[10^{-10}, 5]$. Sanity: the credit triangle within 1.5% after the ACT/360 adjustment, an exact bootstrap round trip, zero upfront at the par coupon, and the 500 bp coupon producing a payment to the buyer.

The legs, the par spread and the upfront are all derived above, so the listing is those formulas with the conventions nailed down (quarterly ACT/360 premiums, accrual on default, a closed-form protection leg, and a root-finder that turns a quoted spread back into a hazard), plus assertions that reproduce the numbers in the next paragraph rather than merely assert them. One edge bites: `premium_schedule` rounds the maturity to the nearest quarter while `protection_leg` runs to the exact `T`, so a 5.1-year input prices at about 302 bp where a flat curve should give nearly the same 297 bp, a 5 bp phantom basis, and maturities should be snapped to standard roll dates before they get here.

*The full listing is [Listing 24.1 in Appendix F](#code-24-1).*

The numbers are worth reading once. At $\lambda = 5\%$, $R = 40\%$ and $r = 4\%$, the five-year par spread is about 297 bp, slightly below the triangle's 300 bp because of the ACT/360 factor and slightly above the ACT/360-adjusted 296 bp because premiums are paid at the end of each quarter. The risky annuity is about 4.06 years. Against a 500 bp coupon, the buyer receives about 8.2 points upfront. Theo's 370 bp Halvorsen swap sits between those cases, and the same three functions price it.

## 24.3 Four Things People Mean by "Basis"

Theo's sticky note said "basis: −110." Ines came back from the morning meeting, read it upside down, and asked, "Against what?" It was the right question, because the four people within earshot gave four different answers, all of them honest, and the answers differed by more than the signal.

Theo went first, because the number was his. "Against the Z-spread. The constant spread over the OIS curve that reprices the bond's cash flows. Four-eighty on the bond, three-seventy on the swap, so $b^{Z} = s^{\text{CDS}}(T) - Z = -110$." It was the easiest of the four to compute and, as the next twenty minutes established, the hardest to defend.

Mags answered from the years she had spent sitting next to a bank's treasury desk. "Treasury never asked for a Z-spread. They asset-swapped everything par-par. You pay par for the bond, whatever it actually costs, swap its fixed coupons for floating plus a spread $A$, and the upfront difference $P^{\text{rf}} - P$ gets amortized over the swap's annuity, so $A = (P^{\text{rf}} - P)/\text{PV01}^{\text{rf}}$, with $P^{\text{rf}}$ the bond discounted on the risk-free curve. The basis is $b^{\text{ASW}} = s^{\text{CDS}}(T) - A$." She turned a page of her run sheet. "It's how a balance sheet sees a bond. It has the same disease as Theo's, because you just paid par for something that costs 88."

Kaz had been waiting for this. "Neither of those compares like with like. Take the hazard curve bootstrapped from the swap, shift it in parallel until the bond's model price under that curve, with the swap's own recovery, matches the 88 on the screen, and read off the par CDS spread at the shifted curve. That's the par-equivalent CDS spread, and the basis is $b^{\text{PE}} = s^{\text{CDS}}(T) - \text{PECS}$. Same curve, same recovery, same units. It's the only one of the four that subtracts two things of the same kind."

"And the research desk," Ines said, "will email you a fourth number this afternoon. One basis per issuer, aggregating all of Halvorsen's bonds, because they run a panel of hundreds of names every month and nobody fits PECS on all of them by Friday. That's Dynkin's definition, and it's the one most systematic research uses." She put the sticky note back on Theo's monitor. "So which one is minus a hundred and ten?"

Nobody had computed the honest one yet. Kaz said they would have the PECS by lunch, and Theo wrote *against what?* on a fresh note and stuck it under the old one.

> **[SOURCE EXTRACTION]** *Dynkin_Systematic_Investing_in_Credit p.216:* "We define the cash–CDS basis as the difference between the spread of a 5y CDS and the market value‐weighted OAS (computed relative to the Libor curve) of all unsecured bonds issued by the underlying reference entity."
>
> **Annotation.** Our analysis: this is an operational definition, built to give one basis per issuer across a large panel, and for cross-sectional research it is the right design. Note the three choices inside it, because each one becomes a parameter on a 2026 desk. "Relative to the Libor curve" now means relative to SOFR swaps or OIS, and the switch moves the level of every basis in the panel by the spread between the curves. "Market value-weighted" mixes bonds at 70 with bonds at 105, which, as the derivation below shows, mixes spurious positive and negative bases. "All unsecured bonds" excludes secured paper, correctly, since secured bonds are not what the swap is priced on, but it also excludes the loans that may be deliverable. A desk that trades the basis bond by bond should use PECS at the bond level. A desk that uses the basis as a feature can use Dynkin's definition, provided the same convention is used every month.

Which of the four a number actually is can take weeks to find out, and the weeks are rarely glamorous.

**Quant-shop life (fictional composite): a systematic asset manager onboards a pricing vendor.** *The shop, the vendor, Ruth and every number here are invented (illustrative).* The firm had bought a new evaluated-pricing feed for its credit book, and the feed came with a column the PM liked the look of, labeled `basis_bp`, for 3,100 bonds. Ruth, the data lead, was given three weeks to "reconcile it to our own table," which meant three weeks of a spreadsheet with 3,100 rows and a ticket queue. The first week went on identifiers: 212 bonds mapped to the wrong reference entity because a merger had closed in the vendor's security master on a different day from the firm's, and 40 had a 4 p.m. price in one file and a 3 p.m. price in the other. The second week went on the vendor's methodology document, version 4.2, which defined the field in one sentence ("CDS spread less bond spread, market convention") and was otherwise mostly about the vendor. The weekly call with the vendor's account manager was pleasant and resolved nothing.

The third week produced a pattern. Against the firm's own PECS table, the vendor's column was off by a few bp on most bonds and by 40 to 60 bp on one group: almost every low-coupon bond issued in 2021, all of them "cheap," all of them showing a negative basis the firm's table did not see. The PM wanted to know whether that was a vintage effect worth trading. Ruth sorted the sheet by an obscure column called `px_src`, and the pattern split cleanly in two. Bonds the vendor priced from dealer runs carried a Z basis over a swap curve. Bonds it priced by matrix, from a second upstream source, carried the CDS spread minus a yield spread over a benchmark curve that the second source had loaded on some earlier day, with no curve name and no date attached. Rates had risen since that day, so the stale curve sat below the market, every yield spread measured against it came out too wide, and every bond priced off it looked cheap. The 2021 low coupons were long-dated and rarely traded, so nearly all of them were matrix-priced. The vintage effect was a source effect, and the source effect was a curve date.

Nobody lost money. The cost was three weeks, a "do not use" flag on a column the firm was paying for, and a line added to the onboarding checklist that every new feed now passes through the bond-level table of Listing 24.2 before anyone looks at its basis field. The vendor's mistake was a politer cousin of the one ROBO makes in the Spec below. What the desk says now is shorter than the checklist: no curve, no basis.

### 24.3.1 Why a par swap and a discount bond disagree even when nothing is wrong

Before lunch Kaz explained why the PECS would not match the Z basis, using a shopping analogy that Mags said was the first time she had heard a quant mention a jacket.

> **Math, Gently.** *Recovery of face versus recovery of market value, or "forty back on what?"* Picture two shoppers who each insured a jacket for "forty dollars back if it's ruined." One paid 88 for hers, the other paid 112. When both jackets are ruined, both collect 40. The first has lost 48 of her 88, which is 55%; the second has lost 72 of his 112, which is 64%. That is recovery of face value (RFV): the payout is fixed per unit of face, whatever you paid, and it is how a CDS settles. A Z-spread quietly measures a bond's loss the other way, as a fraction of the bond's own price, the recovery-of-market-value (RMV) convention. The swap charges for losing 60 points of par, the 60% a par bond loses. Measured as a fraction of price, the discount bond only stands to lose 55%, so its Z-spread comes out below the swap's spread although both are priced off exactly the same default risk, and the subtraction reports a phantom basis of about +15 bp. The premium bond stands to lose 64%, and its phantom is about −13. Nothing is mispriced; the yardstick has a slope. Chapter 6 (§6.6.3) lays the recovery conventions side by side, and the vintage arithmetic comes next.

In one line: for a par bond the Z-spread and the CDS spread coincide, $Z_{\text{par}} = \lambda(1-R) = s^{\text{CDS}}$, and away from par they drift apart with price even when every price comes from the same hazard.

#### The Full Derivation: the vintage pattern

Stay under $\mathbb{Q}$ with flat $\lambda$ and $r$, and use recovery of face value (RFV): at default, a bond of face 1 is worth $R$, whatever its coupon or price. This is the convention that matches CDS settlement, since the swap pays par minus a price quoted per unit of face. A bond with coupon $c$ paid semiannually at $t_j$, maturing at $T$, is worth

$$
P(\lambda) = \sum_{j} \frac{c}{2}\,B(t_j)\,S(t_j) \;+\; B(T)\,S(T) \;+\; R\int_0^T B(u)\,\lambda\,S(u)\,du .
$$

The Z-spread is defined by a different equation, with no explicit default:

$$
P^{\text{mkt}} = \sum_j \text{CF}_j\, e^{-(r+Z)t_j}.
$$

Discounting at $r + Z$ is what you would do if default destroyed a constant *fraction of market value*, the recovery-of-market-value (RMV) convention. Under RMV with fractional loss $L^{\text{MV}}$, the spread would be $\lambda L^{\text{MV}}$. Under RFV, the fractional loss of market value for a bond at price $P$ is roughly $(P-R)/P$, which depends on price. So a Z-spread computed from an RFV-consistent price drifts with price, while the CDS spread does not.

To see the size, use continuous coupons, which makes the algebra exact. Write $k = r + \lambda$ and $a(k) = (1-e^{-kT})/k$. Then

$$
P(\lambda) = c\,a(k) + e^{-kT} + R\,\lambda\,a(k).
$$

*Par bond.* Setting $P = 1$ gives $c\,a(k) + R\lambda\,a(k) = 1 - e^{-kT} = k\,a(k)$, so $c = r + \lambda(1-R)$. The Z-spread of a par bond with continuous coupon $c$ is $c - r$, hence

$$
Z_{\text{par}} = \lambda(1-R) = s^{\text{CDS}}.
$$

For a par bond the Z-spread basis is zero, which is the FRN argument of §24.1 in fixed-coupon clothing.

*Discount and premium bonds.* Take $r = 4\%$, $\lambda = 5\%$, $R = 40\%$, $T = 5$, so that $s^{\text{CDS}} = 300$ bp before the ACT/360 adjustment. Then $e^{-0.45} = 0.6376$, $a = 4.026$, and the recovery term is $R\lambda a = 0.0805$.

| Coupon | Model price $P(\lambda)$ | Z-spread | PECS | $b^{Z}$ | $b^{\text{PE}}$ |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 4% | 87.92 | ≈ 285 bp | 300 bp | ≈ +15 bp | 0 |
| 7% | 100.00 | 300 bp | 300 bp | 0 | 0 |
| 10% | 112.08 | ≈ 313 bp | 300 bp | ≈ −13 bp | 0 |

*(Hand calculation, continuous coupons, illustrative; the semiannual code below reproduces the signs and sizes.)* All three bonds are priced exactly off the CDS hazard. There is no mispricing anywhere in the table, and yet the Z-spread reports a positive basis on the discount bond and a negative basis on the premium bond: the two jackets of the box, at 48 points lost on 88 and 72 on 112. In a market where coupons set in 2020–2021 are trading at 85 and coupons set in 2023–2024 are trading at 103 (illustrative), the Z basis has a vintage pattern built into it that a careless signal will read as alpha. Figure 24.1 shows that pattern across coupons, next to the jump-to-default hedge ratio derived just below.

![Figure 24.1: A bond priced exactly off the CDS hazard shows a positive Z-spread basis at a discount and a negative one at a premium while its par-equivalent (PECS) basis stays at zero (left), and the CDS notional that is flat at default falls to 0.80 of face for Halvorsen's bond at 88 (right). Illustrative: Listing 24.2 with r = 4%, hazard 5%, recovery 40%, five years and semiannual coupons from 2% to 12%; the Z basis crosses zero near a price of 95 rather than 100 because the ACT/360 CDS spread (297 bp) sits below the 303 bp Z-spread of a par semiannual bond.](assets/figures/ch24_z_basis_vintage.png)

> **[SOURCE EXTRACTION]** *Schmid_Credit_Risk_Pricing_Models p.159:* "A default swap is a par product: it does not completely hedge the loss on an asset that is currently trading away from par. If the asset is trading at a discount, a default swap overhedges the credit risk and vice-versa."
>
> **Annotation.** Our analysis: this is Theo's sticky-note arithmetic, and it has two consequences the desk must keep separate. The first is *valuation*: comparing a par instrument with a bond at 88 requires PECS or an equivalent, or you read the table above as a trade. The second is *hedging*: the jump-to-default-neutral notional is not the bond's face. The bond loses $P - R$ at default and the swap pays $1 - R$, so the JTD-neutral CDS notional per unit of bond face is $N^{\text{JTD}} = (P - R)/(1-R)$. For Halvorsen at 88 with $R = 40\%$, that is $48/60 = 0.8$: \$8mm of protection on \$10mm of bonds. A desk that buys \$10mm is also long \$2mm of a jump-to-default bet, which is fine if intended and a hidden position if not. The modern departure is that $R$ itself is uncertain, so $N^{\text{JTD}}$ has a recovery delta. The package is flat at default only if the auction's recovery equals the bond's, which is the subject of §24.5.

Kaz brought the PECS back at lunch, written on a napkin, which Mags counted as progress. Against the par-equivalent spread the Halvorsen basis was about −135 bp, not −110 *(illustrative)*: the Z-spread had been understating how cheap a bond at 88 was, in exactly the direction the table predicts. Theo cared less about the extra 25 bp than about the number Kaz had written underneath it, 0.8. "So if I buy ten million of protection, I'm long two million of jump-to-default that nobody asked me to own." He changed the protection ticket to eight million before he finished his sandwich. "Hedge the loss, not the face." Ines, walking past, said it was the first thing he had said all day that a poker player would have said, and kept walking before he could decide whether that was a compliment.

Two more conventions move the measured basis before any economics enters.

> **[SOURCE EXTRACTION]** *Bohn_Stein_Active_Credit_Portfolio_Management p.578:* "Our own research and that of our colleagues suggests that CDS premia can be interpreted as implicit spreads over a corporate default-risk borrowing curve, which is typically 10 to 20 basis points below the dollar swap curve."
>
> **Annotation.** Our analysis: the discount curve is a basis input, and choosing it is a decision, not a default setting. Bohn and Stein were writing about the Libor-swap world, in which the "risk-free" curve itself contained bank credit. Since the Libor cessation the desk has SOFR OIS, a cleaner risk-free proxy, and the gap between that curve and the curve at which a levered basis trader actually funds is now the repo spread $\phi$ of §24.4. So the specification computes the bond's Z-spread or PECS and the CDS's hazard curve off the *same* curve, stores the curve's name and date with every basis observation, and treats a switch of curve as a structural break in the time series.

The second convention is seniority and security. The CDS references senior unsecured obligations; if most of an issuer's bonds are secured, the bonds trade rich to the swap for reasons that have nothing to do with mispricing. Mags had traded airline paper in the years when airlines went bankrupt in alphabetical order. "Equipment trust certificates were never what the swap was insuring," she said. "The swap was insuring the unsecured notes nobody wanted. Of course the certificates looked rich against it."

> **[SOURCE EXTRACTION]** *Dynkin_Systematic_Investing_in_Credit p.220:* "all issuers but one in the Airlines and Railroad industry had positive bases, reflecting the fact that debt in these industries is largely secured and bonds typically trade rich relative to CDS."
>
> **Annotation.** Our analysis: this is a deliverable-quality effect showing up in a basis table, and it is a good bridge to §24.5. A secured equipment bond pays a high recovery in default. The CDS pays par minus the auction price of whatever senior unsecured obligation is cheapest. The two are not claims on the same loss, so the basis is structurally positive. For a 2026 desk this matters most in sectors where liability management transactions have created layers of secured debt above the unsecured bonds that remain deliverable (Chapter 13). There, the basis between a new super-priority bond and the swap tells you very little about mispricing and a great deal about where the CDS will settle.

Positive bases are not only structural. In early 2016, as European bank credit sold off, investors hedged with CDS faster than they sold bonds, and IHS Markit's commentary of 31 March 2016 showed bases on several bank names in positive territory, Deutsche Bank's 1.25% notes due September 2021 among them, at 95 bp in February tightening to 73 bp in March. When everyone wants protection at once, the swap leads, and the positive basis is the hedging queue.

### Specification for AI Implementation (bond-level basis: Z, PECS and JTD hedge ratio)

**What ROBO built from the vague version.** Told to "compute the basis," ROBO subtracted the bond's *yield* from the CDS spread, reported a basis of −580 bp on every bond in the universe, recommended buying all of them, and pointed out, when asked, that this was what had been asked.

**The precise spec.** Inputs: coupon `c` (decimal, semiannual 30/360), maturity `T` (years from a coupon date; no accrued in this sketch), market price per unit face, flat OIS rate `r`, recovery `R`, and the CDS par spread from §24.2. Outputs: `z_spread` (decimal), `pecs` (decimal, with the implied flat hazard), the bases $b^{Z}$ and $b^{\text{PE}}$ in bp, and `jtd_hedge_ratio` (CDS notional per unit face). Guards: refuse a PECS when the price is outside the model's range, typically a bond trading below the assumed recovery, and say so instead of returning a root at the bracket edge. With a term structure, shift the bootstrapped piecewise hazard curve in parallel rather than replacing it with a flat one. Sanity: a bond priced off the CDS hazard has a PECS basis of zero to $10^{-9}$, while its Z basis is positive for a discount bond and negative for a premium bond.

Ruth's third week is why this listing exists. The three-row table above is a hand calculation with continuous coupons, enough to see the sign of the problem and useless on the Thursday when somebody needs the Z basis, the par-equivalent basis and the jump-to-default hedge for every bond in a universe of a few thousand, with coupon dates that do not drift by a day each time somebody inserts a spreadsheet row. So the table gets built as code, once, with the semiannual 30/360 conventions fixed, and it becomes the yardstick that a vendor's `basis_bp` column is held against.

`bond_cashflows` lays out the coupons of `c/2` on a half-year grid and adds par to the last one. `bond_price_hazard` then does what the hazard model says: it weights every cash flow by survival and discounting together, `exp(-(lam + r) t)`, and adds the value of recovering `R` of face at default, using the same closed-form integral as the protection leg in Listing 24.1. Given a market price, `z_spread` finds the single constant spread over the OIS curve that reprices the bond, by a root-finder bracketed between -5% and 300%. `pecs` does something different and more useful. It finds the flat hazard that reprices the bond under the same recovery, then runs that hazard through `par_spread`, so the answer comes out in the units of a CDS quote and can be subtracted from one. `jtd_hedge_ratio` is a single line of algebra, `(P - R)/(1 - R)`, the CDS notional per unit of face that leaves nothing to win or lose on an instantaneous default. The closing block prices a 4%, 7% and 10% bond off the CDS hazard and tabulates both bases. The PECS basis is zero to rounding by construction, since the bond was priced from the hazard the swap implies. The Z basis is not zero, and it slides from positive on the discount bond to negative on the premium bond.

PECS earns its keep whenever bond and swap sit at different dollar prices; near par the Z-spread tells the same story more cheaply. The sketch has no accrued interest, so it belongs on coupon dates, and it fits a flat hazard, so a name whose curve slopes steeply needs the production version that shifts a bootstrapped curve instead. The guard in `pecs` is where a careful user still gets misled. The model can only reach prices from just above recovery, at a hazard of 500%, up to the riskless value, about 113 for the 7% five-year bond. Outside that range the function raises, but its message blames a bond trading below recovery, so a rich, high-coupon bond priced above its riskless value is sent to the wrong diagnosis. The desk catches the error, labels the name "out of range," and leaves it out of the basis table, which beats a root parked at the edge of the bracket.

*The full listing is [Listing 24.2 in Appendix F](#code-24-2).*

Note what the code's table adds to the hand calculation: the CDS leg here is ACT/360, so even the near-par bond shows a Z basis of a few bp. That is the day-count term from §24.2 turning up in a P&L, a few bp that Ruth's reconciliation had to explain on every bond before it could see the 40 to 60 that mattered.

## 24.4 Funding, Repo, and the Counterparty: Why a Negative Basis Is Not Free

Section 24.3 established that "−110" was really closer to −135 once the yardstick stopped sloping. That still leaves the question Kaz asked in the cold open, which assumed the basis was free money. The quickest way to see why it is not is to watch somebody try to hold one through a month when money itself became expensive.

#### Long Scene A: The Haircut Call, March 2020 (a replay)

*Fiction label: Ines's desk, its 2020 position, its prime broker and repo terms, and this Friday replay are invented (illustrative). The March 2020 market figures, the Federal Reserve's dates and the academic findings are real and sourced.*

*Friday 23 October 2026, 3:05 p.m.* Ines's Friday replays have one rule: the blotter is real, the cards are blank, and nobody looks at what happened next until they have written down what they would have done. This Friday she put a single page on the projector, her own desk's financing blotter from the first quarter of 2020, with the issuer's name blacked out in marker, the way she blacks out every name on a replay sheet, "so nobody trades the ticker instead of the hand."

The position took up one line. *Long \$50mm senior unsecured notes, BBB-minus chemicals issuer, price 99. Long \$50mm five-year CDS protection, same name. Bond spread 230 bp, CDS 130 bp, basis −100. Haircut 15%. Repo spread 40 bp. Booked 24 Jan 2020* *(illustrative)*. Beside it, in the handwriting that used to fill in tournament scorecards, Ines had written the carry the way her desk had worked it out that January: 100 bp of basis, less 40 bp of funding on the 85% of the bond the repo desk lent against, is 66 bp a year on the face, and 66 bp on a 15-point deposit is 4.4% over cash. "One bad quarter," she said. "The bonds cheapened faster than the swap. The kind of basis you're supposed to be paid to wait for."

Mags read the line twice, which on her scale was applause, and said she had seen the same line in 2008 from the other end of the phone. It is the one time this book has her tell that story, and she tells it without names. "I was at a bank. A fund we financed owned bonds at six hundred over and protection at three hundred on the same names. Minus three hundred of basis. Riskless, everyone said, including us, and we lent against it at a ten-point haircut. Then our repo desk raised the haircut to twenty-five, the same week every other repo desk did, the basis went to minus five hundred, and the riskless trade had to be sold. The only people with balance sheet to buy it were the people who'd raised the haircut." She put the page down. "So we bought it. I'm not proud of the timing. I am proud of the price."

"Every clause of that is a term in an equation," Kaz said.

"Every clause of that is a phone call. The equations come later, from people who weren't on the call."

Theo had spent March 2020 at PJT building thirteen-week cash flow forecasts for companies whose revenue had just become a rumor, and he had never seen that month from a seat that had to mark anything to market. He asked the question a restructuring banker asks first about any position: who lent the money, and on what terms? Ines said that was a good question and that she would answer it after the cards.

*Thursday 12 March 2020.* Ines moved the replay forward seven weeks. The day before, the World Health Organization had called the outbreak a pandemic, and on the 12th the cash bond market did something the desk's models had no column for: it stopped printing. A month later, on BlackRock's first-quarter earnings call (16 April 2020), the head of iShares said that LQD, the largest investment-grade bond ETF, had traded almost 90,000 times that day while its five largest holdings had traded an average of 37 times each. Chapter 20 (§20.5) tells that day from the ETF's side. From the basis desk's side it meant the bond leg of the package had no price anyone had paid, only dealer runs that said "indicative" in a smaller font than usual, while the CDS leg traded all day, because buying protection was the one way to sell credit risk that did not need a buyer for a bond.

The blotter marked the package at −180 that evening *(illustrative)*. Nothing about the issuer's chance of default had moved eighty basis points in a week. What had moved was who wanted to own a bond. Investment-grade funds facing redemptions sold what had a bid, hedgers bought protection because it was there, and the two legs of a "riskless" package drifted apart in exactly the direction that cost the package money. Across the market the drift was enormous. Risk.net later put the US high-yield bond–CDS basis at about −401 bp in the March stress, roughly eight times its weekly average since mid-2010, and the US investment-grade basis at about −186 bp (secondary; magnitudes depend on the index and the definition). For an IG basis, normally a few basis points either side of zero, −186 is not a wider version of normal. It is a different market.

"At the bank," Mags said, "the repo desk was thirty feet from me. By eleven o'clock that Thursday they'd stopped picking up. Not because they were busy. Because every call was somebody asking to borrow more against something worth less."

*Friday 20 March 2020, 4:40 p.m.* The prime broker's email arrived at the hour such emails always arrive, late enough on a Friday that nobody could negotiate. The haircut on the line's overnight financing would go from 15% to 30%, effective at Monday's open *(illustrative)*. The package was marked at −250.

Kaz did the mark on the whiteboard while Ines waited. A package long the basis gains or loses roughly its spread duration times the move in the basis, so a widening of 150 bp at a spread duration of 4.5 is $0.0150 \times 4.5 = 6.75$ points. On \$50mm of face that is about \$3.4mm, against a deposit of \$7.5mm. "Forty-five percent of the equity," Kaz said. "Gone. On a position that converges to zero at maturity." They kept going without being asked. At a 30% haircut the same \$50mm of bonds needs \$15mm of equity behind it. The desk had about \$4.1mm left in the trade. The difference, roughly \$11mm, was due by Monday's open, or the position was the prime broker's to sell.

> **Poker Table.** "A negative basis is a hand you can't lose at showdown," Ines says. "Hold it to maturity and it pays. The problem is that you don't get to see the showdown if you can't cover the bets on the turn. Your stack is the haircut. The other players are the people who set it. Before you play this hand, ask how much it costs to stay in, and who decides."

She handed out index cards. "It is 4:40 on Friday 20 March 2020. You don't know what the Fed will do on Monday. Write three things: do you add, hold or cut; at what haircut would you be forced out; and who decides that number."

*Write your own card before reading on: add, hold or cut, the haircut that forces you out, and whose number it is.*

Kaz wrote *add* and underlined it. "The band says a negative basis this deep is outside its edge by a hundred and fifty basis points. Carry at minus two-fifty and a 30% haircut is two-fifty less twenty-eight of funding, over thirty: seven point four percent. The expected return has never been higher." Forced out at: *a haircut the desk cannot fund.* Who decides: *the band.*

Mags wrote *cut half*. "The band assumes you're still in the game. I've watched what happens to people who are right about the price and wrong about Monday." Forced out at: *whatever it is on Tuesday.* Who decides: *a man at the prime broker who is not answering his phone.*

Theo wrote *hold, if we can*, and then, where the haircut should have gone, a question. "Forced out at depends on the agreement. Does the prime broker have to give notice before it changes the haircut? Is all of this overnight money? Who decides is whoever the repo agreement says decides. What does it say?"

*Monday 23 March 2020.* Ines turned the page. Before the US open the Federal Reserve announced two facilities to support corporate credit, the Primary Market Corporate Credit Facility, which would lend to investment-grade companies, and the Secondary Market Corporate Credit Facility, which would buy their bonds and bond ETFs in the secondary market. On 27 March the New York Fed's terms of assignment named BlackRock's Financial Markets Advisory unit to manage the secondary facility, under a set of conflict-of-interest rules about its own ETFs that ran to several paragraphs. Chapter 20 has the ETF prices that day. The basis is this chapter's: across the market the move unwound after the announcement, which is what the band predicts, because the facilities lowered the cost of holding bonds, $\phi$ and $k^{-}$ in the next derivation, and the negative edge moved back in. Ines's package was back at −140 by the end of April *(illustrative)*.

Then the cards were graded.

Kaz's card was right about the price and lucky about the reason. The basis did come back, but because a buyer of last resort announced itself on a Monday, and the secondary facility did not begin buying ETFs until 12 May or individual bonds until 16 June. The market moved on a promise. Had the promise arrived three weeks later, the desk that added on 20 March would have needed another \$15mm of equity for the new size at the new haircut, and the people it would have had to sell to were the people Mags had described.

Mags's card paid about \$1.7mm, the realized loss on the half she cut at −250 *(illustrative)*, to be safe, and she said she would write the same card tomorrow. "I didn't know what the Fed would do on Monday. Neither did you. Neither did the Fed, until Sunday."

Theo's card was the only one the band could not grade, and it turned out to be the one that mattered. Ines put up the second page of the blotter, the financing confirmations. Half of the \$50mm had been financed in a three-month term repo struck on 24 January with the haircut fixed at 15% until 24 April; only the other half was overnight. The 20 March email applied to \$25mm, not \$50mm. The desk had to post an extra 15 points on \$25mm, about \$3.75mm, which it had. It posted, held, and was paid on the convergence it had been promised in January.

"Why term?" Theo asked.

"Term cost five basis points more on half the position. Twelve and a half thousand dollars a year *(illustrative)*. In January it looked like a tax." Ines picked up her coffee. "At a card table you never sit down with chips somebody else can take off the table. The money was the hand. The basis was just the cards."

And the reader's card? If it said *add*, it was right only if it also said where the extra equity came from. If it said *cut*, it was safe and poorer, which is a respectable outcome in March. If it asked for the financing documents, it found the only fact in the room that was not a price.

The academic record says the same thing about the whole market that the blotter says about one line. Choi, Shachar and Shin (2019, *Management Science*) find that over 2005–2009 dealers on average traded *against* a widening bond–CDS gap, buying the cheap leg and stabilizing the basis, until their own balance-sheet constraints bound and the stabilization stopped. Oehmke and Zawadowski (2015, "Synthetic or Real? The Equilibrium Effects of Credit Default Swaps on Bond Markets," *Review of Financial Studies* 28(12)) model the CDS as a cheaper way to take credit exposure, which pulls some demand away from bonds while also making room for levered basis traders who bridge the two markets. Both point where the replay pointed. A negative basis is a price for balance sheet, and its tails arrive when balance sheet is scarce, which is also when the people who own the balance sheet are deciding how much of it you may use.

Kaz, who had been right about the price, wanted the afternoon written down as algebra before anyone went home. Theo asked for it as a house first.

> **Math, Gently.** *Leverage is a divisor, and the haircut is a process.* Picture a \$400,000 house bought with 15% down: \$60,000 of your money and \$340,000 of the bank's. If the house rises 4%, it gains \$16,000, and that is a 27% return on your \$60,000, because every dollar the house earns is divided by the small deposit before it reaches you. If it falls 4%, you lose 27% of your deposit the same way, and if the bank insists that you always hold 15% equity, it now wants about \$13,600 more from you to bring the deposit back up. That is leverage as a divisor. Now suppose the bank, frightened by the fall, says it wants 30% down from now on: on a house worth \$384,000 you need \$115,200 of equity and you have \$44,000. Nothing about the house changed to cause that second call. The lender changed its mind. That is the haircut as a process, set by someone else, and it tends to rise exactly when prices fall. A basis package is the house. Ines's earned 66 bp a year of net "rent" on a 15-point deposit, which is $0.0066/0.15 = 4.4\%$, and the email on 20 March was the bank asking for 30% down. The full version, with symbols, comes next.

In one line: the negative-basis package carries the basis less the funding on the borrowed part, $\pi^{-} = -b - \phi\,(1-h)$, its equity earns that carry divided by $h$, and both packages together give a band inside which the basis can wander without paying anyone to close it.

### 24.4.1 The Full Derivation: the carry of each package and the arbitrage band

Work per unit of bond face for a bond near par, so that $N^{\text{JTD}} \approx 1$ and the asset-swap spread $A$, the Z-spread and PECS approximately coincide; call the bond's spread $s^{\text{bond}}$, so $b = s^{\text{CDS}} - s^{\text{bond}}$. Rates are annual, in excess of the floating rate $r$.

**The negative-basis package** (long bond, long protection). The bond, asset-swapped, earns $r + s^{\text{bond}}$. The trader posts a haircut $h$ of equity and borrows $1-h$ in repo at $r + \phi$, where $\phi$ is the funding spread. The equity has opportunity cost $r$. Protection costs $s^{\text{CDS}}$. The excess carry is

$$
\pi^{-} = s^{\text{bond}} - s^{\text{CDS}} - \phi\,(1-h) = -b - \phi\,(1-h).
$$

**The positive-basis package** (short bond, short protection). The trader borrows the bond through a reverse repo, lending cash and earning the repo rate on it. If the bond is special, that rate is below general collateral by the specialness $\ell$. The trader pays the bond's coupon, worth $r + s^{\text{bond}}$, and receives $s^{\text{CDS}}$ for selling protection, so

$$
\pi^{+} = s^{\text{CDS}} - s^{\text{bond}} - \ell = b - \ell.
$$

Adding transaction and capital costs $k^{-}$ and $k^{+}$, each expressed as an annual running rate, neither package earns anything inside the band

$$
-\phi\,(1-h) - k^{-} \;\le\; b \;\le\; \ell + k^{+}.
$$

This is the frictional version of $b = 0$. The basis can move freely inside the band and is pushed back only at its edges, and the edges move with funding conditions. The band is also asymmetric. The negative edge is set by the cost of *financing* a long position, the positive edge by the cost of *borrowing* a short one, and in a crisis it is the first that blows out.

> **[SOURCE EXTRACTION]** *Schmid_Credit_Risk_Pricing_Models p.255:* "One may be forced in a special repo, i.e. one may be forced to offer a repo rate that is substantially below the general collateral rate (GCR). Then the default swap spread should be increased by the difference between the GCR and the special repo rate"
>
> **Annotation.** Our analysis: this is the $\ell$ in the positive edge of the band, stated as an adjustment to the fair CDS spread. If the bond is hard to borrow, a positive basis up to $\ell$ is not an opportunity, because the short leg pays it away. The 2026 desk can measure $\ell$ directly, from securities-lending fee data and the repo desk's quotes, and should store it per bond as a time series. Bai and Collin-Dufresne (2019, *Financial Management* 48(2)) find the empirical counterpart: across bonds, the basis is more negative where the bond lending fee is higher and where trading liquidity, funding cost, counterparty risk and collateral quality impose larger frictions. The departure from Schmid's framing is that we no longer "adjust the spread." We put the friction on the edge of the band and let the signal live inside it.

**Return on equity.** The negative-basis package's excess return on the trader's equity is

$$
\text{ROE}^{-} = \frac{-b - \phi\,(1-h)}{h}.
$$

With $b = -100$ bp, $\phi = 40$ bp and $h = 15\%$ *(illustrative)*, the carry is $100 - 34 = 66$ bp of face, and $\text{ROE}^{-} = 0.0066/0.15 = 4.4\%$ a year over cash. If the haircut doubles to 30%, ROE falls to $(100-28)/30 = 2.4\%$.

**Mark-to-market.** The package is long the basis, so for a small move its value changes by $\Delta V \approx D^{\text{spr}}\,\Delta b$ per unit face. Per unit of equity this is $D^{\text{spr}}\,\Delta b / h$. If the basis widens from −100 to −250 bp with $D^{\text{spr}} = 4.5$, the package loses $0.0150 \times 4.5 = 6.75$ points, which is 45% of a 15-point haircut. Convergence is guaranteed only at maturity or default, and only up to the deliverable and recovery terms of §24.5. The trader has to survive until then, and the haircut and the basis are both driven by the same thing, the cost of balance sheet. That is Mags's 2008 story and Ines's blotter in two equations: the carry falls when $h$ rises, and the mark-to-market loss is divided by $h$. Figure 24.2 plots both.

![Figure 24.2: Doubling the haircut from 15% to 30% cuts the return on a −100 bp negative-basis package from 4.4% to 2.4% a year (left), while a widening from −100 to −250 bp costs 45% of equity at a 15% haircut and half that at 30% (right), so a thin haircut buys return at the price of fragility. Illustrative: Listing 24.3 with a repo spread of 40 bp and a spread duration of 4.5.](assets/figures/ch24_haircut_roe_mtm.png)

**Counterparty risk.** The last friction concerns the other side of the swap.

> **[SOURCE EXTRACTION]** *Bohn_Stein_Active_Credit_Portfolio_Management p.577:* "Note that buying protection is similar in form to shorting a loan or bond. While the value of the position may behave similarly to a short-loan or short-bond position, the presence of this joint default probability issue makes the CDS analysis a little more involved."
>
> **Annotation.** Our analysis: protection is only worth what the protection seller can pay. Write $\tau_c$ for the seller's default time. The protection leg the buyer actually owns is $(1-R)\,\mathbb{E}^{\mathbb{Q}}\big[B(\tau)\,\mathbf{1}\{\tau \le T,\ \tau_c > \tau\}\big]$ plus whatever the buyer recovers from the seller, and with positive correlation between $\tau$ and $\tau_c$ (wrong-way risk) it is worth noticeably less than the clean leg. A buyer who prices that in pays a lower spread, so counterparty risk is a *negative*-basis driver, and in 2008 it was a large one, with dealers' own CDS widening alongside their clients' bonds. Central clearing changed the term but did not remove it. The counterparty is now a clearinghouse, and the cost moves into initial margin, which is a funding cost and enters through $\phi$. In 2025, 63.1% of US-reported single-name notional and 78.1% of index notional was cleared (ISDA, July 2026), so the uncleared remainder still needs a CVA charge in the basis engine.

Mags, who had spent March 2020 at a bank, said the replay had one seat missing, and it was the one she had been sitting in.

> **View From Another Seat.** *The bank credit-trading desk (a generic seat; no firm is described).* From a dealer's floor the haircut is not a verdict on the client's trade. It is the price of the dealer's own balance sheet, which is rationed by capital and leverage rules measured at quarter-ends, by internal limits that tighten when volatility rises, and by a treasury that charges the trading desks for every dollar they hold. In calm markets that balance sheet is cheap, and the dealer is the natural basis trader: Choi, Shachar and Shin (2019) find dealers on average traded against a widening bond–CDS gap over 2005–2009, buying the cheap leg, until their own constraints bound. In a stress the same constraint runs the other way. The financing desk raises haircuts because its balance sheet is full, the trading desk would like to buy the cheap package but has no room either, and the basis widens until somebody with spare balance sheet arrives. Mags's 2008 story is the rare case where the dealer had room on one desk and used it, which is why she is proud of the price and not of the timing. The dealer also sees something the client cannot: whose packages are financed with it, at what haircuts, and therefore who will be selling on Monday. Clearing changed the swap leg more than the bond leg. The CDS side of the package increasingly sits at a clearinghouse with initial margin (the cleared shares are in the annotation above), while the bond side still sits on someone's balance sheet, financed overnight.

### Specification for AI Implementation (basis package carry and stress)

**The precise spec.** Inputs: the basis in bp ($s^{\text{CDS}} - s^{\text{bond}}$, negative for a negative basis), the repo funding spread $\phi$ in bp over the floating rate, the haircut $h \in (0,1]$, and the spread duration. Outputs: annual excess ROE on equity, and mark-to-market on equity for a given move in the basis. Guards: reject $h \le 0$. Never report an ROE without the haircut that produced it, and run the same position at the stressed haircut (at least double the current one) beside the base case. Sanity: the 4.4%, 2.4% and −45% figures above, and negative carry for a basis inside the band.

At 4:40 on 20 March the mark was done on a whiteboard, and Ines's January carry was done in the margin of a blotter. This listing is those two calculations, so that the next time an email arrives on a Friday the desk is not doing arithmetic while it decides. The two functions are the two equations above and nothing more, which is the point of keeping them small: an ROE that is a one-line function of three inputs has nowhere to hide an assumption, and the assertions pin it to the 4.4%, 2.4% and −45% worked above. The mistake it invites is a sign. `basis_bp` is the CDS spread minus the bond spread, so a negative-basis trade enters as a negative number; type the basis as a positive 100 and the function reports a negative carry, which reads like a flaw in the strategy when it is a flaw in the call. The habit the replay left behind is in the output: every position appears twice, at the haircut on the confirmation and at double.

*The full listing is [Listing 24.3 in Appendix F](#code-24-3).*

> **Ways This Blows Up.** (1) *ROE without the haircut process.* A backtest at a constant 15% haircut overstates the Sharpe ratio, because the haircut rises exactly when the basis widens. Model $h_t$ as a function of a funding-stress index, or at least backtest at the stressed haircut. (2) *JTD drift.* $N^{\text{JTD}} = (P-R)/(1-R)$ changes as the bond price moves. A package set up flat at 95 is materially over-hedged at 70. Rebalance the CDS notional on a price band, and charge the rebalancing to the trade. (3) *Maturity mismatch.* A 4.3-year bond hedged with the 5-year standard swap leaves a curve position. Interpolate the CDS curve to the bond's maturity for the basis, and hedge with the two adjacent standard maturities. (4) *Treating the clearinghouse as free.* Initial margin on the CDS leg is funded. Put it in $\phi$, or the cleared package looks better than the bilateral one by exactly the amount you forgot.

The replay also leaves a longer record than one blotter can, and it is the same record in every stress since 2008.

> **Trend Watch: the basis in three stresses, and the clearinghouse in the middle (2008–2025).** *2008:* Bai and Collin-Dufresne's working-paper figures (as summarized in our research dossier; secondary) put the investment-grade basis, normally a few bp positive, at about −250 bp at the 2008 trough, and the high-yield basis at about −650 bp. *March 2020:* the second stress is Scene A's, told there with Risk.net's −401 bp and −186 bp. *2023:* the regional-bank and Credit Suisse stress was a single-name event. ISDA reports single-name traded notional up 84.8% in Q1 2023 against its trailing four-quarter average, with \$161bn in financials, while index activity rose only 4.5%. *Clearing:* ICE Clear Credit reported a record \$2.57tn of USD single-name CDS cleared in 2025, against \$2.17tn in 2024 (ICE press release, 6 Jan 2026; secondary), and ICE Clear Europe stopped clearing CDS in October 2023, moving more than \$400bn of open interest (ISDA, July 2026). *What it means for the desk:* every large negative basis since 2008 has been a funding event first and a credit event second. Make the basis model regime-aware: a −150 bp basis with funding conditions calm is a signal, and the same basis with repo haircuts rising is a warning about the people already holding it.

## 24.5 The Cheapest-to-Deliver Option

Assumption A5 said the swap pays $1-R$ on *this* bond. It doesn't. It pays par minus the price of whatever the market can deliver most cheaply, and the gap between those two is an option that someone owns and someone else has sold.

> **[SOURCE EXTRACTION]** *Schmid_Credit_Risk_Pricing_Models p.159:* "Note that the contract usually specifies a basket of obligations that are ranked pari passu that may be delivered in place of the reference asset. Actually, the protection buyer who has chosen physical delivery is effectively long a 'cheapest to deliver' option."
>
> **Annotation.** Our analysis: one sentence that contains the whole deliverables problem. Since 2009 almost every standard trade has settled in cash at the auction price, so it might seem that physical delivery, and the option, went away. They did not. In the auction, the participants who sell bonds deliver the cheapest one they can, so the final price is set on the cheapest deliverable, and the option now sits inside the auction price. Every famous fight in §24.8 is a fight about what belongs in Schmid's "basket": Hovnanian's new 5% 2040 notes, Sears's consent-required loans, and, in August 2026, whether the registered forms of two DISH DBS note series belonged on the Final List.

Mags remembers the old system. "Back in my day you had to find the bond. On some names there was more protection outstanding than bonds to deliver, and settling meant everybody chasing the same paper up in price. Delphi in 2005 was the famous one. They invented the auction so we'd stop doing that to each other." A pause. "It's better now. Now we do it to each other on a published timetable."

Delphi, the auto-parts maker spun out of General Motors, filed for Chapter 11 in October 2005, and the problem Mags describes was arithmetic. Press reports at the time put the protection written on Delphi at many times the roughly \$2bn of bonds that could be delivered against it, by one count \$27.5bn against \$2.2bn. Every protection buyer who settled physically needed a bond to hand over, and many of them did not own one, because they had bought protection as a view or as a hedge of something else. So the bankruptcy that should have pushed the bonds down pulled them up, as buyers of protection bid for paper in order to deliver it, and a contract designed to pay the loss on default paid less than the loss because of the scramble to collect. Dealers ran an auction under an ISDA protocol that fixed a single price for index and tranche trades, 63.375, and let those trades settle in cash. "I was at a bank," Mags said. "I watched people who had been right about Delphi for a year lose money on the week it filed. That's when I learned the swap doesn't pay you for being right. It pays you for whatever's on the list."

The list is the whole subject of this section, so it is worth seeing why choosing from a list is worth money at all.

> **Math, Gently.** *The minimum over a set is an option.* Picture a shop that has promised to buy back, at full price, any one item from a shelf of things it sold you. You will bring back the cheapest thing on the shelf, every time. If every item on the shelf is worth the same, your choice is worth nothing. If one item has quietly lost half its value, your choice is worth half the price, and whoever made the promise has sold you that choice whether they meant to or not. That is the protection buyer's position: the swap pays par minus the *lowest* price on the deliverable list, $1 - \min_j P_j$, and a minimum over a set is a bond plus an option to swap it for something cheaper, worth more the more the prices on the list spread out. Why would two bonds of the same issuer be worth very different amounts? Because a bond whose coupon is below the yield the market now demands is short that difference every year it has left. A bond paying 8% when the market wants 11% is three points a year short for a year and a half, which, discounted, is about four points below par. A bond paying 5% is six points a year short, for twenty-two years, which adds up after discounting to roughly 49 points below par. Same issuer, same default, and a 45-point gap between the two items on the shelf. Next, the exact prices and the two regimes that decide whether the shelf has one price or many.

In one line: the swap pays $1 - \min_{j\in\mathcal{D}} P_j(\tau)$, so the cheapest-to-deliver option is worth the expected gap between the reference bond and the cheapest deliverable, and that gap is near zero after a bankruptcy and can be half of par after a failure to pay without acceleration.

### 24.5.1 The Full Derivation: when the option is worth nothing and when it is worth half of par

Let $\mathcal{D}$ be the set of deliverable obligations at the event, with post-event prices $P_j(\tau)$ per unit of outstanding principal. Under physical settlement the buyer delivers face 1 of any $j \in \mathcal{D}$ and receives par, so the payoff is $1 - \min_{j\in\mathcal{D}} P_j(\tau)$. Under auction settlement it is $1 - \text{FP}$, and FP tracks $\min_j P_j$ up to the auction effects of §24.6. Against a hypothetical swap that paid $1 - P_k$ on one reference bond $k$, the cheapest-to-deliver option is worth

$$
\Omega^{\text{CTD}} = \mathbb{E}^{\mathbb{Q}}\Big[B(\tau)\,\mathbf{1}\{\tau \le T\}\,\Big(P_k(\tau) - \min_{j\in\mathcal{D}} P_j(\tau)\Big)\Big] \;\ge\; 0 .
$$

Its value depends entirely on how dispersed the deliverables' prices are *after* the event, and that depends on the kind of event.

**Regime 1: bankruptcy, with acceleration.** A filing accelerates the debt. Every senior unsecured obligation becomes a claim for principal plus accrued interest, ranked pari passu, and recovers the same amount per dollar of claim. So $P_j(\tau) \approx \tilde{R}\,(1 + \text{AI}_j)$ for a common recovery $\tilde{R}$. The only dispersion is accrued interest, and $\Omega^{\text{CTD}}$ is a fraction of a point. This is the regime in which "recovery" means what Theo's training says it means.

**Regime 2: failure to pay without acceleration.** One obligation is in default; the others are performing and trade on their remaining cash flows at the issuer's yield $y$:

$$
P_j(y) = \sum_{m=1}^{2T_j}\frac{c_j/2}{(1+y/2)^m} + \frac{1}{(1+y/2)^{2T_j}} .
$$

When $y > c_j$, $P_j$ falls as maturity lengthens and as the coupon falls. So the cheapest deliverable is the longest, lowest-coupon one, and both of those are features an issuer chooses when it issues a bond. At $y = 11\%$ *(illustrative)*, an 8% bond due in 1.5 years is worth 95.95 and a 5% bond due in 22 years is worth 50.63. The swap pays $100 - 50.63 \approx 49.4$ points if the 22-year bond is deliverable, and about 4 points if only the short bond is. The issuer is solvent, nobody has lost half their money, and the protection buyer collects half of par. That is the Hovnanian blueprint (§24.8.2), written as a bond-math identity. Figure 24.3 sets the two regimes side by side.

![Figure 24.3: In bankruptcy every deliverable recovers about 30 and the swap pays 69.4 or 69.6 whichever is delivered (left), but after a failure to pay without acceleration the performing 5% 22-year bond trades at 50.6 against 96.0 for the 8% 1.5-year bond, so the same swap pays 49.4 or 4 points depending on what is deliverable (right). Illustrative: Listing 24.4 with an event yield of 11% and, in bankruptcy, a 30% recovery per unit of claim plus a quarter-year of accrued interest.](assets/figures/ch24_ctd_deliverable_prices.png)

The contract has fences against this, and they are worth knowing by name. For the Standard North American Corporate contract the deliverable obligation characteristics are, roughly: Bond or Loan; Not Subordinated; Specified Currency; Not Contingent; Assignable Loan; Consent Required Loan; Transferable; Maximum Maturity of 30 years; Not Bearer. Check them against the confirmation and the Physical Settlement Matrix of the trade date before trusting this list. The 30-year limit is why nobody manufactures a 99-year 1% deliverable. It does not stop anyone manufacturing a 22-year 5% one. The Modified and Modified-Modified Restructuring variants used outside North America limit the maturity of deliverables after a Restructuring for the same reason. And the 2019 NTCE amendments added an Outstanding Principal Balance provision aimed at deliverables engineered to trade at a deep discount (Quinn Emanuel, May 2019; secondary).

> **[SOURCE EXTRACTION]** *Bohn_Stein_Active_Credit_Portfolio_Management p.578:* "These valuations depend critically on the nature of the contract terms with respect to what is delivered in the event of default. For some contracts, a fixed amount is promised. For other contracts, an actual security—sometimes the cheapest to deliver—is promised."
>
> **Annotation.** Our analysis: Bohn and Stein were classifying contracts for portfolio valuation; the systematic desk reads the passage as a data-model requirement. The deliverable set $\mathcal{D}$ is a time-varying attribute of each reference entity and belongs in the security master, with each obligation's seniority, maturity, coupon, currency, transferability flags and current price. From it, compute $\Omega^{\text{CTD}}$ daily under both regimes. A jump in the regime-2 value, for example when an issuer prints a long, low-coupon bond, is a signal that the swap has become more valuable to protection buyers, whatever its spread says.

### Specification for AI Implementation (CTD under the two default regimes)

**The precise spec.** Inputs: deliverables as a mapping from name to post-event price per unit face; for regime 2, coupon, remaining maturity and an event yield; for regime 1, a common recovery per unit of claim and each bond's accrued interest. Outputs: the cheapest deliverable and the swap payout $1 - \min_j P_j$. Guards: raise an error for an empty deliverable set rather than returning a payout of zero, and price on coupon dates only in this sketch (accrued handling is a separate function in production). Sanity: the 95.95 and 50.63 prices, the long bond as CTD, and a regime-1 CTD option below one point.

The listing turns the two regimes into two small dictionaries and a `min`. Regime 2 prices each deliverable as a performing bond at the event yield with `price_at_yield`, regime 1 gives every claim the same recovery on par plus a quarter-year of accrued interest, and `ctd` returns the cheapest name and the swap payout `1 - min`, which is how a 22-year 5% bond turns a solvent issuer into a half-par payout while the regime-1 option stays under a point. Two things bite: `price_at_yield` is valid on coupon dates only, so a live version needs the accrued-interest function, and `ctd` raises on an empty deliverable set rather than returning a zero payout, because an orphaned swap (§24.8) is exactly the case where "nothing to deliver" must not be read as "pays nothing."

*The full listing is [Listing 24.4 in Appendix F](#code-24-4).*

## 24.6 The Two-Stage Auction

Section 24.5 ended with the swap paying par minus the cheapest thing on the list. The list, it turns out, is only half of it. The other half is who has to buy the cheapest thing, how many of it exist, and what happens to its price on the one afternoon when everyone needs it at once.

#### The Sears Afternoon, 17 January 2019 (a replay on the clock)

*Fiction label: the drill, the cast's cards and the \$50mm of protection on the reader's card are invented (illustrative). Every Sears date, vote, price and dollar figure comes from the public Determinations Committee and auction record (creditfixings.com and the DC's Sears decisions) or from the sources named.*

*Tuesday 27 October 2026, 9:45 a.m.* Ines runs auction replays on the clock. Each number is released at the minute it was first published, so the desk sits through the same dead time the market sat through, and nobody gets the final price before 2:00 p.m. "Real auctions are mostly waiting," she said. "If you can't wait, you'll trade the waiting."

She had already put the background on the screen, in order, the way a docket reads. Sears Holdings had filed on 15 October 2018, and two days later the Americas Determinations Committee voted 15 to 0 that Sears Roebuck Acceptance Corp., the group's financing arm and the reference entity for most Sears swaps, had suffered a Bankruptcy Credit Event. Then the argument about the list began. On 13 November a challenger warned the Committee that intercompany paper "can be created merely at the stroke of a pen." On 19 November the Committee excluded \$3.0bn of medium-term notes of the series called NOTZ, along with two commercial-paper programs, 15 to 0, for thin documentation; split 7 to 8 on \$525mm of second-lien loans, which sent the question to External Review; and the next day admitted the remaining intercompany notes, 12 to 3. Between 19 and 21 December a three-member External Review panel answered "Yes": the loans were deliverable as Consent Required Loans, and the panel added that this was not a situation "such as might arise through a 'manufactured' set of facts."

The Final List of 8 January 2019 was the strangest shopping shelf Theo had ever seen. Seven Sears bonds with coupons between 6.5% and 7.5%. A PIK-toggle note. The \$525mm of loans, whose agent's address was care of ESL Investments, Sears's largest shareholder. And seven series of intercompany medium-term notes with a combined face of \$11.6bn, issued inside the group to itself. An anonymous submission to the Committee asked for a delay and said two things that turned out to matter: that the scarce unsecured deliverables were trading "40 points above" second-lien notes that could not be delivered, and that free trading in deliverable paper was under \$1mm a day. The auction went ahead. Ines added one line from a secondary source, keeping its wording exactly: the estate had sold notes in a way that "effectively allowed it to set the price of credit default swap contracts on Sears," and the buyer, a hedge fund "widely believed to have sold considerable CDS protection," paid \$82.5mm on condition that Sears sell no more (Sidley Austin, December 2019).

Kaz read the list twice. "Eleven point six billion of intercompany notes. Is that a deliverable or a mirror?"

"In bankruptcy, it's a claim," Theo said. "A claim that can be set off, recharacterized, or sold only if the estate agrees. Most of it can't leave the building." He had spent six years watching intercompany balances get argued about in first-day declarations. "Eleven point six billion on the list is not eleven point six billion on the street."

*10:30 a.m.* Ines released stage one. Nine dealers had submitted two-way markets, from 45/50 at Citi to 59/64 at Morgan Stanley, a fourteen-point spread between the lowest and highest midpoints for paper that was supposed to have one price. The Inside Market Midpoint came out at 55.625. Then she read the physical settlement requests aloud, slowly. "Seventy point one million to buy bonds. Twenty-five point one to sell. Net open interest: forty-four point nine million to buy." She let that sit. "Against a free float the anonymous letter put under a million a day."

She handed out cards. "It is 10:30 on 17 January 2019. You sold \$50mm of protection on Sears. Write three things: what you do in stage two, at what price you think it ends, and what the cap does for you."

*Write your own card before reading on: your stage-two move, your guess at the final price, and what the cap does for you.*

Kaz went first, as Kaz usually does when a mechanism has a parameter. "There's a Cap Amount of one point. So the final price is within a point of 55.625. Our payout is about 44.4 points on \$50mm, call it \$22mm, and stage two is noise. I'd buy back some protection now, before the price is set, while it's still a credit trade."

Mags wrote her card without looking at anyone. "Find the paper. Any deliverable I can buy before stage two, I buy, and I offer it in stage two at 75. Forty-five million has to come from somewhere, and somewhere doesn't have much."

Theo had pulled up the auction terms rather than the list, which on this desk had become his reputation. He read the Cap Amount clause twice and then read it aloud. With open interest to buy, offers *below* the midpoint minus the Cap Amount are treated as if they were at that floor, 54.625. Nothing in the clause says anything about offers above the midpoint. "The cap's a floor," he said. "It stops the price being dragged *down* when everyone's buying. It doesn't stop it being dragged up. Today it does nothing for us, because everything's going our way. It's the protection buyers who have nothing. So: we don't offer bonds into stage two, and if we owned any, we wouldn't sell them near 56." His guess at the final price was "higher than anyone wants to write down," which Ines refused to accept as a number until he wrote 70.

*2:00 p.m.* The final price was 79.875.

The grading took longer than the auction. Protection buyers were paid 100 − 79.875 = 20.125 points instead of the 44.375 the midpoint implied, so on every \$100mm of notional \$24.25mm moved from protection buyers to protection sellers in one afternoon, set by a net demand of \$44.9mm for bonds that barely traded. On the card's \$50mm, the payout was about \$10.1mm, not \$22.2mm. Kaz's card would have bought back protection at a price that assumed the bigger payout, paying for a loss the auction was about to cancel. Kaz said "I treated the cap as symmetric because the formula looked symmetric," wrote that down, and on this desk Kaz writing something down is the highest compliment a mistake can receive.

Mags's card was the best trade on paper and the hardest to do. A fund that bought \$10mm of face near the 55.625 midpoint and delivered it into the stage-two book at 79.875 made about \$2.4mm. Mags circled the condition herself: *if it could find the paper.* Under a million a day of free float means the trade on her card was mostly a trade that could not be filled.

Theo's card was right about the direction and too modest about the size, which Ines said was the normal way for a banker's card to be wrong. The reader's card gets the same grade it would get at the table. If it said the cap protects the price, it read a one-sided rule as two-sided. If it said "don't sell into stage two," it was right. If it said 80, it is either lucky or knew someone.

"What should a desk have seen at 10:30?" Ines asked, and answered it herself, because the answer was on the screen. "Two numbers. The sign of the open interest, and its size against the paper that can actually be delivered. When the open interest is to buy, nothing caps the upside. When the free float is a rounding error next to the open interest, the book walks." She turned off the projector. "The swap paid twenty points because of how many bonds could be found on one afternoon, not because of what Sears's creditors would eventually get. That's not recovery. That's inventory."

The rulebook that produced that afternoon is short, and the desk now keeps it as code.

When a credit event is declared, the regional Determinations Committee, made up of dealers and buy-side firms, resolves that the event occurred, publishes a list of deliverable obligations, and sets the auction terms. ISDA's description of the process sets out the steps. The DC decides by simple majority whether to hold an auction (Restructuring is handled differently). An initial deliverables list follows within days, members have two days to add obligations and three to challenge them, and a challenged obligation needs an 80% supermajority to be included or excluded, failing which the question goes to External Review. Then the auction runs in two stages on a published timetable.

The Windstream Services auction is a good worked set of parameters, all from the DC's 6 March 2019 decision, which was approved 15–0: Bankruptcy Credit Event; auction on 18 March 2019 (a dealer email vote on 11 March moved it to 3 April, 9 to 1, and the settlement date with it, to the later of T+3 and 8 April); at least eight valid initial market submissions; Initial Market Quotation Amount of \$2mm; maximum bid–offer spread of 3 points; Cap Amount of 1 point; pricing increment of 1/8; initial bidding from 9:45 to 10:00 a.m., with the Inside Market Midpoint published at 10:30; subsequent bidding from 12:45 to 1:00 p.m., with the final price published at 2:00; and settlement on the later of T+3 and 21 March 2019.

In one line: the IMM is nothing grander than an average of the better half of the dealers' non-crossing markets, rounded to an eighth (the rounding is where ROBO slips, in the Spec below), and the final price is where the open interest stops when it walks the limit-order book, clipped by the cap only on the side the open interest is not pushing.

### 24.6.1 The Full Derivation: the inside market midpoint and the final price

**Stage 1.** Each of $K$ dealers submits a two-way market $(b_k, o_k)$ with $o_k - b_k \le M$ (3 points for Windstream) in the quotation amount, together with any physical settlement request. A request must be in the same direction as the submitter's net CDS position and no larger than it. Sort bids in descending order, $b_{(1)} \ge b_{(2)} \ge \dots$, and offers in ascending order, $o_{(1)} \le o_{(2)} \le \dots$. The first $n^{\text{tr}}$ pairs with $b_{(i)} \ge o_{(i)}$ are *tradeable* (touching or crossing) and are discarded. From the remaining $K - n^{\text{tr}}$ pairs keep the best half, $h = \lceil (K-n^{\text{tr}})/2 \rceil$, and average:

$$
\text{IMM} = \operatorname{round}_{1/8}\!\left(\frac{1}{2h}\sum_{i=n^{\text{tr}}+1}^{n^{\text{tr}}+h}\big(b_{(i)} + o_{(i)}\big)\right).
$$

A dealer whose tradeable quote sits on the wrong side of the IMM pays an Adjustment Amount, $(b - \text{IMM})^{+}$ or $(\text{IMM} - o)^{+}$ times the quotation amount. That is the price of a quote that crosses the market. The open interest is the net of all physical settlement requests, $\text{OI} = \sum_k \text{PSR}_k$, positive for a net demand to buy bonds.

**Stage 2.** Participants submit limit orders on the side opposite the open interest, and the stage-1 quotes carry over as limit orders. If OI is to sell, fill it against bids from the highest down; if to buy, against offers from the lowest up. With $p^{*}$ the last price matched,

$$
\text{FP} =
\begin{cases}
\min\big(p^{*},\ \text{IMM} + \text{Cap}\big) & \text{OI} < 0 \text{ (net sellers)},\\[2pt]
\max\big(p^{*},\ \text{IMM} - \text{Cap}\big) & \text{OI} > 0 \text{ (net buyers)},\\[2pt]
\text{IMM} & \text{OI} = 0,
\end{cases}
$$

with FP $= 0$ if selling open interest exhausts the bids, and par if buying open interest exhausts the offers (for auction-formed trades the fallback is the highest offer). The cap limits how far a final price can sit on the wrong side of the IMM relative to the open interest. Without it, a large protection seller facing net selling could post a few very high bids, buy a small amount of bonds expensively, and lift the price at which its much larger swap book settles. ISDA's own description notes that the "value of Limit Orders is far below aggregate notional of CDS," and that asymmetry is the reason the auction is a game rather than a price discovery mechanism. Figure 24.4 shows the final price as a function of the open interest, for the eight-dealer book in the code below.

![Figure 24.4: The final price walks down the bids as net selling grows and up the offers as net buying grows, and the Cap Amount stops a net-selling price from sitting more than one point above the 26.875 IMM (left); one rogue 30.0 bid for \$10mm would lift the price to 30.0 without the cap, for net selling of up to \$10mm, but only to 27.875 with it (right). Illustrative: the eight-dealer book of Listing 24.5 (two-point-wide markets, \$2mm quotation amount) and its limit orders, with the rogue bid added in the right panel.](assets/figures/ch24_auction_final_price.png)

> **Poker Table.** "Stage one is everybody posting a blind and then turning one card face up," Ines says. "The physical settlement requests are public. The open interest tells the whole table who has to sell bonds and how many. Stage two is the only real betting round, and the players who aren't in the open interest know exactly how desperate the ones who are can be. Replay the hand history and you'll see it: when open interest is a large sell, the final price comes in low, and the bonds bounce once the forced sellers are gone."

The hand history exists. Chernov, Gorbenko and Makarov (2013, "CDS Auctions," *Review of Financial Studies* 26(3)) show that strategic bidding by CDS holders can push the final price above or below the bonds' fair value, and they find that on average auctions undervalue the bonds by about 6% on auction day. Du and Zhu (2017, "Are CDS Auctions Biased and Inefficient?", *Journal of Finance* 72(6)) show that the two-stage design produces biased prices and inefficient allocations, and propose a double auction in its place. For the desk this is an event strategy. Before the auction, estimate the direction and size of the open interest from positioning and deliverable supply. After it, price the bounce.

Most auctions are duller than Sears, and the dull ones teach the same mechanism at a lower volume. Windstream's, held on 3 April 2019, also had open interest to buy, \$68.2mm, and cleared at 29.5 against a 26.75 midpoint, higher than bond levels had implied, amid big physical settlement orders (Creditflux; secondary). Buying open interest walks up the offer book, and the final price ends above the IMM, by 2.75 points rather than 24.25. In January 2025 Intrum's auction settled at 76, a 24-point payout reported as largely in line with secondary bond prices (Risk.net and Bloomberg Law; secondary). So the game can also produce a dull result.

### Specification for AI Implementation (two-stage auction simulator)

**What ROBO built from the vague version.** Asked to "round the midpoint to an eighth," ROBO called `round()`, which in Python and numpy rounds halves to the even neighbor. On a midpoint of exactly 26.8125 it published 26.75 instead of 26.875. That is one-eighth of a point on every swap in the auction, and the test below exists to catch it.

**The precise spec.** Inputs: matched dealer bid and offer lists in points; the quotation amount; open interest in \$mm (positive = buy bonds); limit orders as (price, size) pairs; Cap Amount in points. Outputs: IMM, the tradeable quotes, Adjustment Amounts in dollars, and the final price. Guards: matched pairs only; raise an error if every market is tradeable; rounding with halves going up; a book-exhaustion fallback to 0 or par. Sanity: the hand-computed IMM of 26.875 with one crossing pair, a \$22,500 adjustment, a final price of 23.0 for \$50mm of selling, 0 when the bids run out, the cap binding against a rogue high bid, 30.0 for \$30mm of buying, and final prices that fall as selling open interest rises.

At 2:00 p.m. on the Sears replay the desk could watch the final price arrive but could not reproduce it, and a price the desk cannot reproduce is a price it cannot trade around the next time. The derivation is a procedure, and a procedure is what a desk wants as code. `inside_market` pairs the i-th best bid with the i-th best offer, discards the touching and crossing pairs, averages the best half and rounds, `adjustment_amounts` bills the dealers who crossed, and `final_price` walks the book against the open interest, applies the cap, and falls back to 0 or par if the book runs dry. The rounding is where the code most easily lies, because `round()` sends halves to the even neighbor, which is how ROBO turned 26.8125 into 26.75. `round_half_up` is exact when quotes are multiples of an eighth, but a tie that arrives as 26.8124999 after a decimal round trip falls the wrong way again, so keep quotes as integer eighths or round the input first.

*The full listing is [Listing 24.5 in Appendix F](#code-24-5).*

## 24.7 Trading the Basis Systematically

*Wednesday 28 October 2026, 8:15 a.m.* Kaz arrived with a chart and the expression of someone who had found order in the universe. It showed the desk's panel of market-adjusted bases, a few hundred names, each a wobbly line, and Kaz had fitted a spring to every one of them *(the desk's fictional run)*. "Once the frictions are priced, what's left is a spread that wanders off and comes home," Kaz said. "Pull it away from where it lives and it comes back, faster the further you pull. That's a mean-reverting process, and a mean-reverting process is a trade."

"Comes home to where?" Theo asked. "And how fast?"

> **Math, Gently.** *A spring, and its half-life.* Picture a weight on a spring whose resting point is a basis of −40 bp. Somebody drags it down to −200 and lets go, and the spring pulls back with a force proportional to how far it has been stretched, so the 160 bp gap closes quickly at first and more slowly as it shrinks. A stiffness of $\kappa = 1.39$ a year means the gap halves every $\ln 2/1.39 \approx 0.5$ years: you expect the basis at −120 after six months, −80 after a year, −60 after eighteen months, each half-life taking half of whatever gap is left. In symbols, the expected basis after a horizon $H$ is $\mathbb{E}^{\mathbb{P}}[b_{t+H}] = \theta + (b_t - \theta)\,e^{-\kappa H}$, with $\theta$ the resting point. Now shake the weight while it moves; that is the noise term, and it is why any single path wanders around the expected one instead of following it. One thing is missing that you might expect from Chapter 6. A lognormal price pays Itô's $\tfrac12\sigma^2$ "volatility tax" (§6.1) because the noise enters through an exponential. Here the noise is simply added to a linear pull, so the expected path is the noiseless one and no correction appears. Chapter 4 (§4.6) met the same process as a drunk on a leash and Chapter 12 (§12.3) uses it on spreads; the exact transition and the regression that estimates $\kappa$ are in §24.7.1.

Kaz's answer to both questions was a table of fitted $\theta$, $\kappa$ and half-lives, most between three months and a year. Ines read down it and said the research desk did not trade springs at all. They sorted on the same number. Kim, Li and Zhang (2016, *Journal of Empirical Finance* 38) find that the *residual* basis, net of counterparty, funding and liquidity frictions, strongly predicts bond excess returns with a negative sign: a more negative residual basis means higher subsequent bond returns. Their 2017 paper in the *Journal of Futures Markets* (37(8)) finds that a low-minus-high basis factor carries a premium of about 3% a year in investment-grade bonds. Kaz, not to be outdone, pointed out that the spring has a direction as well as a speed. Lee, Naranjo and Sirmans (2021, "CDS Momentum: Slow-Moving Credit Ratings and Cross-Market Spillovers," *Review of Asset Pricing Studies* 11(2)) report CDS return momentum of 7.1% a year and cross-market spillovers, with past CDS performance producing alphas of 10.3% a year in stocks and 7.3% in bonds, concentrated in liquid names whose spreads move ahead of slow rating changes. In the names where the swap trades, it is the faster of the two doctors.

"Slow rating changes," Theo said. "So who stretches the spring? If the big dislocations come from downgrades, is a downgrade something you can see coming?" Often, it turned out, with a rating-migration model (Chapter 9), and the downgrade that stretches the spring hardest is the one that makes somebody sell. The cleanest evidence comes from forced sellers.

> **[SOURCE EXTRACTION]** *Dynkin_Systematic_Investing_in_Credit p.213:* "The forced selling of fallen angels' bonds is not accompanied by a similar dynamic in the CDS referencing these issuers. As a result, CDS spreads generally widen after the downgrade but to a lesser extent than those of bonds, and the basis exhibits mean reversion"
>
> **Annotation.** Our analysis: this is the cleanest flow-driven basis signal in the literature, because the cause is a rule rather than a view. Investment-grade mandates must sell a bond downgraded to high yield, and nobody is required to sell the swap. So the bond cheapens relative to the CDS, the basis goes negative, and it reverts as the bonds find high-yield owners. Dynkin et al. report the size on their 2004–2010 sample: the basis "widened consistently from about 40bp to more than 100bp in the rating-event month and rose even further, to almost 225bp, three months after the downgrade" (p.161), magnitudes of a negative basis. The 2026 departure is that the event is now forecastable. Rating-migration models (Chapter 9) give a downgrade probability before the event, so the desk can pre-position, or, more usefully, avoid being the forced seller's only bid in the first week.

Whether the reversion is worth trading is a question of costs, and the same study answers it plainly.

> **[SOURCE EXTRACTION]** *Dynkin_Systematic_Investing_in_Credit p.224:* "The shorter holding period compared with the 'Buy All' strategy (14 vs. 24 months, respectively) resulted in an almost quadrupling of the net Sharpe ratio to 0.97, although transaction costs were unchanged."
>
> **Annotation.** Our analysis: read it with the base case on p.223, where "Buy All" earned 0.5% a month with a gross Sharpe ratio of 1.05 and a "net Sharpe Ratio of 0.26 (based on an average bid‐ask estimate of 4.9%)." Costs took three-quarters of the Sharpe. Across the four formulations in their Table 3.13 (pp.224–225), gross Sharpe ratios of 1.05, 2.04, 2.38 and 3.30 become 0.26, 0.97, 1.30 and 1.74 net. Exit rules account for the difference, not entry rules. The signal is the same in every formulation. What changes is how long capital stays tied up after most of the reversion has happened. For a 2026 desk the lesson is to specify the exit as carefully as the entry, and to model costs per name and per regime, since a 4.9% average conceals both the bonds that trade at a point and those that trade at five.

### 24.7.1 Derivation: a mean-reverting basis and the cost threshold

Model the market-adjusted basis of name $i$ as an Ornstein–Uhlenbeck process under the physical measure $\mathbb{P}$. This is a forecasting model, not a pricing model, so $\mathbb{Q}$ plays no part:

$$
db_t = \kappa\,(\theta - b_t)\,dt + \sigma\,dW_t .
$$

Here $\kappa$ is the speed of reversion (per year), $\theta$ the long-run level (bp), and $\sigma$ the volatility (bp per $\sqrt{\text{yr}}$). The exact solution over a step $\Delta$ is

$$
b_{t+\Delta} = \theta + (b_t-\theta)\,e^{-\kappa\Delta} + \sigma\sqrt{\frac{1-e^{-2\kappa\Delta}}{2\kappa}}\;\varepsilon_{t+\Delta}, \qquad \varepsilon \sim N(0,1),
$$

so the basis is an AR(1) with coefficient $\phi^{\text{AR}} = e^{-\kappa\Delta}$ (the superscript keeps it apart from the funding spread $\phi$ of §24.4), half-life $\ln 2/\kappa$, and stationary standard deviation $\sigma/\sqrt{2\kappa}$. Estimation is a regression of $b_{t+\Delta}$ on $b_t$, with $\hat\kappa = -\ln\hat\phi^{\text{AR}}/\Delta$. If $\hat\phi^{\text{AR}} \ge 1$ there is no reversion to trade, and the code must say so rather than return a negative half-life. "Market-adjusted" means $\tilde{b}_{i,t} = b_{i,t} - \beta_i\,\bar{b}_t$, with $\bar{b}_t$ the index-level basis. The common component is funding (§24.4), and IDO or it didn't happen.

Enter the negative-basis package at $b_0 < \theta$ and hold for $H$. The expected mark-to-market gain is $D^{\text{spr}}(\theta - b_0)(1-e^{-\kappa H})$, carry adds about $\int_0^H(-\mathbb{E}^{\mathbb{P}}[b_t] - \phi)\,dt$, and the round-trip cost $c^{\text{rt}}$ comes off the top. Ignoring carry, the trade is worth entering only if

$$
\theta - b_0 \;>\; \frac{c^{\text{rt}}}{D^{\text{spr}}\,\big(1 - e^{-\kappa H}\big)} .
$$

If Dynkin's 4.9% is read as a round-trip cost in price terms, at $D^{\text{spr}} = 5$ it equals 98 bp of basis at full convergence. If the half-life equals the holding period, so that only half the gap closes, the threshold doubles to 196 bp, close to the full fallen-angel dislocation. That is why "Buy All" barely clears its costs, and why an exit rule that sells once most of the reversion is in, then redeploys the capital, multiplies the net Sharpe.

### Specification for AI Implementation (OU basis signal, net of costs)

**The precise spec.** Inputs: a weekly market-adjusted basis series in bp; entry and exit z-scores; spread duration; repo spread in bp; one-way cost in bp of notional. Outputs: fitted $(\kappa, \theta, \sigma)$, the half-life, and weekly gross and net P&L in bp of notional, with the number of entries. Guards: an error if the AR coefficient is not in $(0,1)$; decisions at $t$ use only data up to $t$, and P&L runs from $t$ to $t+\Delta$; costs charged on every change of position. Sanity: recovery of known parameters from a seeded simulation (5,200 weeks: either a century of one name or, more honestly, a hundred names for a year each, if you pretend they are independent), and a net Sharpe below the gross.

Dynkin's numbers leave a trader with an awkward question. The entry signal is the same in all four formulations, and the net Sharpe ratio runs from 0.26 to 1.74 depending on when you leave, so the thing worth studying is the exit, and real basis histories are far too short and too dirty to study it on. The quant shop's answer is the unglamorous one. Simulate a basis whose parameters are known, run the whole estimate-and-trade pipeline on it, and check that the pipeline recovers the truth and that costs bite in the direction the theory says. Only then does anyone point it at vendor data, where nothing is known and everything arrives late.

`simulate_ou` draws the path with the exact transition from the derivation, `theta + (b - theta) * phi + sd * eps`, rather than an Euler step, so the weekly grid does not bias the answer. `fit_ou` runs the AR(1) regression of next week's basis on this week's, reads `kappa` off the slope, `theta` off the intercept and `sigma` off the residual spread, and refuses a slope outside (0, 1) instead of reporting a negative half-life. `basis_strategy` is a two-state machine. It goes long the negative-basis package when the basis drops below `theta - z_in * sd`, goes flat when it climbs back above `theta - z_out * sd`, and otherwise holds. The position at week i is decided from `b[i]` alone, and that week's P&L is the position times spread duration times the change in the basis, plus carry of `(-b - repo) * dt`, minus `cost_bp` on every change of position. The test run recovers the known parameters, finds a half-life near twelve weeks, and watches the Sharpe ratio fall from roughly 0.7 gross to roughly 0.2 net.

Use it as a plumbing test, an exit-rule laboratory, and a way to size how much history you need. Do not read it as evidence about any real basis. Note that `kappa` is the hard parameter, since the test tolerates 35% error on it with 5,200 weeks of data, against 10 bp on `theta` and 10% on `sigma`. The edge that bites is in the demonstration rather than the functions: it fits `theta` and `sd_stat` on the whole series and then trades that same series, so the thresholds know the future. On a real basis, refit on an expanding window and hand the strategy only the parameters that existed on the day.

*The full listing is [Listing 24.6 in Appendix F](#code-24-6).*

## 24.8 When the Legal Layer Breaks: Successors, Orphans and Manufactured Credit Events

Assumption A6 was that "default" means the same thing to the bond and the swap. The bond defaults under its indenture. The swap triggers under the ISDA Definitions, as decided by a committee. Most of the time the two coincide. This section is about the times they don't.

> **[SOURCE EXTRACTION]** *Schmid_Credit_Risk_Pricing_Models p.158:* "The credit event triggers the payment. It can either be bankruptcy, failure to pay, obligation acceleration, repudiation, restructuring and others."
>
> **Annotation.** Our analysis: that list describes the menu of the late 1990s. The standard North American corporate contract has since cut it to two items, Bankruptcy and Failure to Pay, with no Restructuring. The 2014 Definitions added Governmental Intervention and asset-package delivery for financials, after the 2013 expropriation of SNS Reaal's subordinated debt showed that a bail-in could wipe out deliverables. A short menu is easier to administer and easier to game. If Failure to Pay is the only non-bankruptcy trigger, then whoever controls whether a coupon is paid controls whether the swap pays, and §24.5 showed how much it can pay when the issuer is solvent. The modern desk treats the credit event definition as a contract with counterparties who read it closely, not as a fact of nature.

Three kinds of engineering exploit the gap. A *manufactured default* triggers Failure to Pay at a solvent issuer, ideally after creating a cheap deliverable. A *manufactured non-default* arranges rescue financing so that a swap expires untriggered (RadioShack's CDS expiring on 20 December 2014, which a rescue financing kept from triggering, is the standard example; Quinn Emanuel, May 2019; secondary). *Orphaning* moves the debt so that the reference entity has nothing left to default on or to deliver. Kaz, on hearing the last term, asked whether an orphaned swap is assigned a guardian ad litem. "It gets a hedge fund," Mags said, "and it's always the one that sold the protection."

### 24.8.1 Derivation: the successor arithmetic

When debt moves to new entities through a spin-off, merger, exchange or drop-down, the swap follows according to thresholds in the Definitions. Let $w_e$ be the fraction of the reference entity's Relevant Obligations that entity $e$ succeeds to, and $w_0 = 1 - \sum_e w_e$ the fraction retained. In simplified form:

1. If some $w_e \ge 75\%$, entity $e$ is the sole Successor.
2. If one or more entities have $w_e > 25\%$ and $w_0 \le 25\%$, each of them is a Successor.
3. If one or more entities have $w_e > 25\%$ and $w_0 > 25\%$, each of them *and* the original entity are Successors.
4. If no $w_e$ exceeds 25% and the original survives, nothing changes. If it does not survive, the entity with the largest share is the Successor.

With $m$ Successors the swap splits into $m$ new swaps, each with notional $1/m$. The thresholds are discontinuous, and discontinuities are where engineering happens: moving 25.0% of the debt does nothing, moving 25.1% halves your swap. Orphaning is the limiting case that the rules do not cover. If debt is *repaid* rather than assumed, nothing succeeds to it, and the swap keeps referencing an entity whose deliverable set is shrinking toward empty. As $\mathcal{D} \to \varnothing$ the protection leg goes to zero, since the auction has nothing to price and there is nothing left to fail to pay. The protection seller keeps collecting premium on a contract that no longer protects anything. In 2018 Chatham's planned refinancing of McClatchy would have placed \$418.5mm of new secured term loans at a *new* entity, using the proceeds to repurchase bonds, so that swaps referencing McClatchy would be left on a hollow shell (Sidley Austin, December 2019; secondary). Octus noted in May 2025 that in liability management exercises the form matters: a clean par refinancing can orphan a swap, while an exchange, an amend-and-extend, or a discounted exchange tends to let it "travel" to a continuing obligation (secondary). Figure 24.5 draws the thresholds as a map.

![Figure 24.5: Moving 25.0% of a reference entity's debt to one new entity leaves the swap untouched, moving 25.1% splits it in half, and 75% or more hands all of it over (left); with two new entities one swap can become one, two or three, with cliffs wherever a new entity's share, or the share the original keeps, crosses 25% (right). Illustrative: the simplified thresholds of Listing 24.7, a desk screen and not a legal determination.](assets/figures/ch24_successor_cliffs.png)

### 24.8.2 Case Study: Hovnanian, Sunrise Trails and the Coupon Nobody Wanted Paid (2017–2018)

> **Docket Diary.** *Early 2017:* GSO Capital Partners (Blackstone) reportedly built about \$333mm of CDS protection on Hovnanian, the homebuilder, ahead of roughly \$700mm of 2017 maturities (K&L Gates, 31 May 2018, citing press reports). *28 Dec 2017:* Hovnanian launched an exchange offer in which K. Hovnanian's 8% notes due 2019 could be exchanged for cash, new 13.5% notes due 2026, and new **5% notes due 2040**: a 22-year bond with a below-market coupon that some expected to trade around 50. GSO tendered up to \$170mm of its \$236mm of 8% 2019s, and provided a 5% unsecured facility to refinance all \$132.5mm of the 7% 2019 notes and up to \$80mm of untendered 8% notes. A Hovnanian subsidiary, Sunrise Trails, bought \$26mm of the tendered 8% 2019s. The 5% 2040 indenture *committed Hovnanian to default* on the interest owed to Sunrise Trails, starting 1 May 2018. *Early 2018:* Solus Alternative Asset Management, a protection seller, went to court in the Southern District of New York. The DC's archive indexes a district court opinion of 29 January 2018, and K&L Gates describes claims of securities fraud, tortious interference, breach of the 8% 2019 indenture, and a declaratory judgment that Sunrise Trails had waived the default. *13–15 Mar 2018:* a general-interest question put to the Americas DC, with the litigation papers attached, was rejected within two days. *20 Apr 2018:* the DC declined a request to use discretionary authority to exclude a deliverable that would produce an artificially low auction price (K&L Gates). *24 Apr 2018:* CFTC staff issued their statement (below). *30 May 2018:* settlement. GSO agreed to amend the 5% 2040 indenture so that Hovnanian could cure the default, which it did the same day, and agreed not to support future failure-to-pay events at Hovnanian. A stipulation of dismissal followed on 31 May. **No credit event ever occurred.** *(The Ad Hoc Group, represented by counsel, notes for the record that this was the rare restructuring in which every party's lawyers were busier than the company's.)*

Put §24.5's machinery on it. The transaction did three things. It created a long, low-coupon deliverable (regime 2: the 5% 2040s near 50). It arranged a failure to pay *without acceleration*, owed to an affiliate who would not enforce it. And it paid the issuer for its cooperation through below-market financing. If the 2040s had been the cheapest deliverable at about 50, protection of the reported size would have paid on the order of \$165mm *(illustrative arithmetic on reported figures)* from an issuer that was not in distress. Every term of that sentence is a feature the desk can compute in advance: deliverable dispersion, the identity of the payee, and the issuer's liquidity runway.

The last of those is Theo's. His 13-week cash flow model has already become a survival curve, a state-space feature and a liquidity runway variable earlier in this book. Here it becomes evidence. The 2019 fix (below) asks whether a failure to pay resulted from a deterioration in creditworthiness, and a 13-week model showing 80 weeks of runway answers that question more directly than anything else the desk owns. Theo was very pleased. Kaz asked whether this meant the USB stick was now a regulatory document.

> **[SOURCE EXTRACTION]** *Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.11:* "CDS has run into trouble with the legal definition of default, such that several hedge funds have manufactured credit events that create distortions between the fundamentals of the companies and the traded credit spreads."
>
> **Annotation.** Our analysis: an industry research framework saying plainly that the legal layer broke the synthetic market's usefulness for quants, and this is one reason Man's authors conclude that cash bonds are the better instrument (§24.1). "Distortions between the fundamentals ... and the traded credit spreads" is a precise statement of the problem: a spread model built on $s = \lambda(1-R)$ assumes the payoff depends on fundamentals, and an engineered event breaks that. The departure is that a 2026 desk can price the distortion rather than avoid it. Estimate a manufactured-event probability from the observable flags, multiply by the regime-2 CTD payout, and subtract the result from the fundamental spread to get a fair spread. Names where that term is large, typically stressed but liquid issuers with concentrated CDS positions and flexible documents, are names where the swap is a position on lawyers.

### 24.8.3 Case Study: Windstream (2015–2019): One Sale-Leaseback, Two Successor Answers, One Auction

On 24 April 2015 Windstream spun off Communications Sales & Leasing (later Uniti) and leased its network back. On 20 May 2015 the Americas DC resolved that under the **2014 Definitions** both CS&L and Windstream Services LLC were Successors, while under the **2003 Definitions** there was no Successor. The same transaction gave two different answers, depending on which version of the contract a trade was written on. In the threshold rules this is case 3: a new entity takes more than 25% and the original keeps more than 25%.

The second act came from bond land. Aurelius, a holder of Windstream's 2023 notes, argued that the sale-leaseback violated the indenture. On 15 February 2019 Judge Jesse Furman of the Southern District of New York agreed and entered a judgment of roughly \$310.5mm plus interest (press reports; secondary). Windstream filed for Chapter 11 on 25 February. On 26 February the DC resolved that *no* Failure to Pay Credit Event had occurred, so the swap triggered on the Bankruptcy instead. The auction was held on 18 March 2019 on the terms in §24.6 and settled at 29.5 with heavy physical settlement buying (Creditflux; secondary). Theo can now answer his own question about what the credit agreement says: in the wake of cases like this, loan documents began adding "net short lender" provisions that strip voting rights from lenders whose CDS protection outweighs their loans. That is the empty-creditor problem of Bolton and Oehmke (2011, *Review of Financial Studies* 24(8)) written into a contract. Creditors who can insure their claims over-insure, and they push for default more often than is efficient.

Sears in 2018 completed the set, and its afternoon is told in §24.6: the Consent Required Loan question that went to External Review, the estate's \$82.5mm note sale, and an auction on 17 January 2019 that cleared 24.25 points above its midpoint. In each of these cases, the fight was about the deliverable set.

### 24.8.4 The patch, and what it does not reach

Regulators spoke first. On 24 April 2018, three CFTC divisions stated: "Manufactured credit events may constitute market manipulation and may severely damage the integrity of the CDS markets." A joint SEC–CFTC–FCA statement on "opportunistic strategies" followed on 24 June 2019 (Sidley; secondary). ISDA's fix was the 2019 Narrowly Tailored Credit Event Supplement to the 2014 Definitions (15 July 2019). It adds a Credit Deterioration Requirement, under which a failure to pay is not a credit event if it "does not directly or indirectly result from, or result in, a deterioration in the creditworthiness or financial condition" of the Reference Entity (as summarized by Simmons & Simmons and Macfarlanes; secondary), and it adds Outstanding Principal Balance provisions aimed at engineered deliverables. The protocol was published on 27 August 2019, adherence opened on 16 September, and the changes took effect in early 2020. Quinn Emanuel's critique is the right one for a model builder. The amendments work through Failure to Pay, so they do not reach manufactured non-defaults or orphaning. The engineering moved to successor and refinancing structures, and so did the DC's docket.

> **Trend Watch: the legal layer, patched and then busy (2018–2026).** *Governance:* ISDA commissioned Linklaters in December 2023 to review the Determinations Committees because "the number of firms willing to serve on the DCs has declined steadily." The review (13 May 2024) proposed up to three independent members, a separate governance body and fewer dealer seats, and the BCG-run consultation (results 19 September 2024) found "broad market support" for a governance body, transparency measures and independent members. *The docket:* the EMEA DC found a Failure to Pay at Altice France Holding (decided 25 June 2025, event date 14 June 2025, 11 votes to 0), then announced *no auction*, because "the Relevant Transaction 300/5 Criteria were not satisfied," meaning too few outstanding trades and dealers. Intrum's auction (16 January 2025) was set after the holidays on purpose. A November 2024 exchange in which NFE Financing LLC assumed more than 25% of New Fortress Energy's debt went to the DC as a Successor question (decided February 2025). In 2026, Liberty Interactive (QVC's parent, a high-yield index constituent) went to auction on 13 May, and DISH DBS, after a prepackaged restructuring, went to auction on 4 August, with the DC adding the registered forms of its 7.375% 2028 and 5.125% 2029 notes to the Final List on auction day. As of 17 October 2026, Successor questions for Discovery Global Holdings (arising from the Warner Bros. Discovery and Paramount Skydance transactions) and Picard Bondco were both scheduled for DC meetings on 19 October 2026 (all from cdsdeterminationscommittees.org). *What it means:* the questions that move single-name P&L are now mostly successor and deliverable questions arising from M&A and LMEs, not "did they default?" The desk needs a successor engine and a deliverables tracker that run before the DC does.

### Specification for AI Implementation (successor map and manufactured-event flags)

**The precise spec.** Inputs: the fractions of Relevant Obligations succeeded to, by entity; whether the original entity survives; for event screening, a dictionary of observable features (event type, whether the payee is an affiliate, liquidity runway in weeks from the 13-week model, financing conditioned on the default, a newly issued long low-coupon deliverable). Outputs: a map from Successor to notional fraction, and a list of flags. Guards: shares must be non-negative and sum to at most 1; "more than 25%" is strict and "75% or more" is not; the screen is a desk heuristic, not a legal determination, and must be labeled as one. Steps Plans, the Successor Backstop Date and the "assumption" tests are out of scope and must be routed to counsel.

Everything in this section comes down to two questions a desk wants answered before the Determinations Committee answers them. After this spin-off, what is my swap? And does this default look like a default, or like a performance? Neither is a job for a chat thread. The successor rules are arithmetic with cliffs, and engineered events leave observable fingerprints, so both belong in functions that run on the deal announcement rather than on the committee's calendar.

`successors` takes the fraction of the reference entity's Relevant Obligations that each entity has succeeded to and applies the four rules in order. An entity at 75% or more takes the whole swap. Otherwise the entities strictly above 25% are Successors, joined by the original entity if more than a quarter of the debt stayed behind, and each of the m heirs inherits a 1/m slice of every CDS. With no entity above 25%, nothing changes unless the original has disappeared, in which case the largest holder inherits. The output is a dictionary from entity to the fraction of each swap it now owns. `manufactured_event_flags` is deliberately dumber. It turns the case-study features into plain-English flags: a failure to pay owed to an affiliate, more than 52 weeks of runway in the 13-week model, financing conditioned on the default, and a freshly minted long low-coupon deliverable. It returns the list rather than a score, because a risk committee needs the sentence that explains the worry, and because the real test is legal, which the docstring says in so many words.

Use both as screens that route a name to counsel, never as the answer. The edge that bites is the data feeding them. The comparison is strict at 25% and inclusive at 75%, so a share that arrives as 0.2500000001 from a float pipeline turns "nothing happens" into "half your swap"; compute shares from principal amounts and compare them as exact fractions. Likewise a missing `liquidity_runway_weeks` defaults to zero, which reads as "no runway worth mentioning," so the flag stays silent exactly when the field is blank.

*The full listing is [Listing 24.7 in Appendix F](#code-24-7).*

## 24.9 Desk Debrief

- **A CDS is a par instrument; your bond is not.** Compare them with PECS, or expect a Z-spread basis of ±15 bp on bonds priced perfectly, plus a few bp of day-count noise.
- **Hedge to jump-to-default, not to face.** $N^{\text{JTD}} = (P-R)/(1-R)$. At 88 and 40% recovery, \$10mm of bonds needs \$8mm of protection.
- **A negative basis is a funding trade with a default option.** Its ROE is divided by the haircut, and the haircut rises when the basis widens. Price the haircut process, not today's haircut.
- **The swap doesn't pay recovery. It pays par minus the auction price of the cheapest deliverable.** In bankruptcy that is close to recovery. In a failure to pay without acceleration it can be half of par from a solvent company.
- **The auction is a poker hand with the cards face up.** Read the open interest, respect the cap, and expect bonds to bounce after a large sell imbalance.
- **Exits make the Sharpe.** On the fallen-angel basis, transaction costs took three-quarters of the gross Sharpe until the exit rule cut the holding period.
- **Successors are arithmetic with cliffs.** At 25.0% nothing happens and at 25.1% your swap splits. Run the thresholds before the DC does.
- **The definition of default is a risk factor.** Flag affiliate payees, conditional financing, new long low-coupon deliverables and refinancings that orphan the swap, and use the 13-week model as evidence.

### The Spec You Hand the Robot

> Build `basis_engine` for one reference entity and its deliverable bonds. **Inputs:** an OIS curve (named and dated); CDS quotes by tenor with coupon and quoting recovery; a contract-terms table (day count, accrual on default, credit events, deliverable characteristics, Definitions vintage); bonds with coupon, maturity, seniority, price and timestamp; repo spread, haircut and borrow fee per bond. **Steps:** (1) bootstrap a piecewise-flat $\mathbb{Q}$-hazard curve and reproduce the standard upfront to the cent; (2) per bond, compute $Z$, ASW, PECS and the JTD hedge ratio, reporting $b^{Z}$ and $b^{\text{PE}}$ in bp; (3) compute the arbitrage band and ROE at current and doubled haircuts; (4) compute the regime-1 and regime-2 CTD payout over the deliverable set; (5) fit an OU model to the market-adjusted basis and emit entry and exit signals net of per-name costs; (6) run the successor map on any announced transaction and the manufactured-event flags on any missed payment. **Guards:** refuse a basis if the CDS mark is older than the bond print; raise an error on an empty deliverable set ("possible orphan"); round auction prices with halves going up; label every flag a heuristic. **Tests:** every assert in this chapter, in order. **Never:** use the bond's yield as its spread, use $R = 40\%$ for quoting and a different $R$ for valuation, or report an ROE without its haircut.

## 24.10 Exercises

1. **The over-hedge.** A bond at 72 with a 35% expected recovery. Compute the JTD-neutral CDS notional per \$10mm face. Then compute the P&L at default if the auction instead recovers 25%, and explain why the recovery delta of the package does not vanish.
2. **Vintage alpha that isn't.** Using the §24.3 code, build a bond universe with coupons from 2% to 10%, all priced exactly off one CDS hazard. Regress the Z basis on price and show that a "cheap-bond" signal appears with a perfect $t$-statistic and zero economic content.
3. **The band in March 2020.** With $\phi$ moving from 30 to 150 bp and $h$ from 10% to 35%, compute the negative edge of the arbitrage band before and after. Did a −186 bp IG basis lie inside or outside it?
4. **ROBO rounds the IMM.** Construct an auction in which banker's rounding moves the IMM and the cap binds, so that the final price differs by a full eighth. Compute the total payout difference on \$5bn of CDS outstanding *(illustrative)*.
5. **Design a drop-down (on paper).** A reference entity has \$4bn of Relevant Obligations. Design a transaction that moves as much debt as possible to a new subsidiary without making it a Successor, then one that leaves the original entity as one of two Successors. Explain which of these is the more dangerous for a protection buyer, and why the "assumption" test, which our code ignores, decides the real case.
6. **Kaz writes a credit event.** Kaz proposes a contract in which the credit event is "the 13-week model shows less than four weeks of liquidity." List three ways an issuer could manufacture or avoid that event, and say whether this is better or worse than Failure to Pay.

### Deep-Dive Resource Graph

**Podcasts**
- **Ardagh CDS and the empty glass paradox** (*Cloud 9fin*, Distressed Diaries, host Bianca Boorer with 9fin's Dan Alderson, 21 Jan 2026). The indenture side of a live case: Arini argued that notes already marked for equitisation had a zero outstanding principal balance and so could not be deliverable, and the EMEA Determinations Committee rejected the challenge in a split vote after failing to reach a supermajority on the trigger itself. The 2026 companion to §24.8. https://share.transistor.fm/s/903a348d
- **Boaz Weinstein on Credit Investments** (*Masters in Business*, Bloomberg, 13 May 2022). The practitioner voice for §24.7: from founding Saba Principal Strategies inside Deutsche Bank in 1998 to being on the other side of the index-CDS trade from the London Whale, which is the index-versus-single-name relationship in person. https://omny.fm/shows/masters-in-business/boaz-weinstein-on-credit-investments A second episode on the same career (24 Nov 2022): https://omny.fm/shows/masters-in-business/boaz-weinstein-on-investors-unknown-risk
- No *Odd Lots* or *Credit Edge* episode in the feeds checked on 18 Oct 2026 is about the basis or deliverable-obligation mechanics (CDS appears only in passing), so none is listed.

**Practitioner Writing**
- K&L Gates (31 May 2018), "By Indirections Find Directions Out: CDS and the Hovnanian Exchange Offer."
- Sidley Austin (December 2019), "Regulatory Scrutiny of Manufactured Credit Events," Bloomberg Law.
- Quinn Emanuel (May 2019), "ISDA's Proposed Rules Aimed at Manufactured Defaults."
- Kramer Levin, "Nonconventional CDS Credit Events Part 1: the iHeart case," and "Opportunistic CDS Strategies Available to CDS Protection Sellers Part II: McClatchy and Sears."
- Macfarlanes, "The ISDA 2019 NTCE Protocol: what you need to know."
- **"Blackstone May Do Its Cleverest CDS Trade Again"** (Matt Levine, *Money Stuff*, Bloomberg Opinion, 17 Nov 2017, date from the URL). Levine on GSO's proposed trigger-and-refinance structure for Hovnanian, modelled on its earlier Codere trade: the setup for the manufactured-event problem that §24.8.2 dissects. https://www.bloomberg.com/opinion/articles/2017-11-17/blackstone-may-do-its-cleverest-cds-trade-again
- **ISDA Board Statement on Narrowly Tailored Credit Events** (ISDA, 11 Apr 2018, date from the URL). The Board's response to arrangements "narrowly tailored to trigger a credit event... while minimizing the impact on the corporation", restating that the Determinations Committees (10 sell-side and five buy-side members each) decide whether any such arrangement is a credit event. The official origin of §24.8's manufactured-event problem. https://www.isda.org/2018/04/11/isda-board-statement-on-narrowly-tailored-credit-events/
- **ISDA Launches NTCE Protocol for Adherence** (ISDA, 16 Sep 2019, date from the URL). The Narrowly Tailored Credit Event Supplement amends the 2014 Definitions' "outstanding principal balance" and "failure to pay" and adds a guidance memo; the protocol lets parties amend legacy trades. Read it beside the Ardagh episode, because the 2026 dispute turned again on outstanding principal balance. §24.8.4. https://www.isda.org/2019/09/16/isda-launches-ntce-protocol-for-adherence/
- **Windstream: When a Credit Derivatives Determinations Committee and a Court Disagree** (Jones Day, March 2019). A court found that Windstream failed to pay accelerated notes in December 2017, yet the Committee had found no Failure to Pay Credit Event, partly because of the Credit Event Backstop lookback; the February 2019 bankruptcy then paid current protection holders but not those whose protection had already expired. The legal-layer half of §24.8.3. https://www.jonesday.com/en/insights/2019/03/windstream-credit-derivatives-determinations
- **The Effects of Entering and Exiting a Credit Default Swap Index** (Jennie Bai and Or Shachar, NY Fed *Liberty Street Economics*, 30 Mar 2015). How the CDX.NA.IG roll swaps constituents and what that implies for pricing if dealers exit single-name CDS: the post for the index-versus-intrinsic and roll mechanics that §24.3 and §24.7 lean on. https://libertystreeteconomics.newyorkfed.org/2015/03/the-effects-of-entering-and-exiting-a-credit-default-swap-index/ Companion: Or Shachar, "Is There a Future for Credit Default Swap Futures?" (22 Dec 2014): https://libertystreeteconomics.newyorkfed.org/2014/12/is-there-a-future-for-credit-default-swap-futures/
- ISDA (29 Jul 2026), "CDS Market Dynamics: Five Years of Activity and a Record 2025": https://www.isda.org/a/Pa0iE/CDS-Market-Dynamics-Five-Years-of-Activity-and-a-Record-2025.pdf
- ISDA, "The Credit Event Process" (auction mechanics): https://www.isda.org/a/cKwEE/TheCreditEventProcess.pdf
- ISDA SwapsInfo, "Full Year 2025 and the Fourth Quarter of 2025 Review": https://www.isda.org/a/mpdgE/SwapsInfo-Full-Year-2025-and-the-Fourth-Quarter-of-2025-Review.pdf
- CFTC Divisions, "Statement on Manufactured Credit Events" (24 Apr 2018): https://www.cftc.gov/PressRoom/SpeechesTestimony/divisionsstatement042418
- Clarus Financial Technology, "Volumes and most active names in credit derivatives" (July 2025).

**Academic Papers**
- Bai, J. and Collin-Dufresne, P. (2019), "The CDS-Bond Basis," *Financial Management* 48(2), 417–439: https://ideas.repec.org/a/bla/finmgt/v48y2019i2p417-439.html
- Kim, G. H., Li, H. and Zhang, W. (2017), "The CDS-Bond Basis Arbitrage and the Cross Section of Corporate Bond Returns," *Journal of Futures Markets* 37(8), 836–861: https://ideas.repec.org/a/wly/jfutmk/v37y2017i8p836-861.html
- Kim, G. H., Li, H. and Zhang, W. (2016), "CDS-Bond Basis and Bond Return Predictability," *Journal of Empirical Finance* 38, 307–337.
- Choi, J., Shachar, O. and Shin, S. S. (2019), "Dealer Liquidity Provision and the Breakdown of the Law of One Price: Evidence from the CDS-Bond Basis," *Management Science*.
- Oehmke, M. and Zawadowski, A. (2015), "Synthetic or Real? The Equilibrium Effects of Credit Default Swaps on Bond Markets," *Review of Financial Studies* 28(12); and (2017), "The Anatomy of the CDS Market," *Review of Financial Studies*.
- Chernov, M., Gorbenko, A. and Makarov, I. (2013), "CDS Auctions," *Review of Financial Studies* 26(3), 768–805: https://discovery.ucl.ac.uk/id/eprint/10104960
- Du, S. and Zhu, H. (2017), "Are CDS Auctions Biased and Inefficient?", *Journal of Finance* 72(6).
- Bolton, P. and Oehmke, M. (2011), "Credit Default Swaps and the Empty Creditor Problem," *Review of Financial Studies* 24(8), 2617–2655 (NBER Working Paper 15999).
- Lee, J., Naranjo, A. and Sirmans, S. (2021), "CDS Momentum: Slow-Moving Credit Ratings and Cross-Market Spillovers," *Review of Asset Pricing Studies* 11(2), 352–401: https://ideas.repec.org/a/oup/rasset/v11y2021i2p352-401..html

**Data & Code**
- Credit Derivatives Determinations Committees (decisions, deliverable lists, auction terms; the Windstream, Hovnanian, Sears, Altice France Holding, Intrum, DISH DBS and Liberty Interactive pages cited above): https://www.cdsdeterminationscommittees.org/cds/
- **Ardagh Packaging Finance PLC** (Credit Derivatives Determinations Committees, EMEA question 2025081102, requested 11 Aug 2025). The Committee's own record of whether a Restructuring Credit Event occurred (it met on 12 and 13 August 2025; status Closed). It covers the credit-event question, not the later deliverable-obligation challenge in the *Cloud 9fin* episode above; pull that statement from the same site before naming the members who dissented. https://www.cdsdeterminationscommittees.org/cds/ardagh-packaging-finance-plc/
- BIS OTC derivatives statistics (semiannual; CDS outstanding): https://data.bis.org/topics/OTC_DER
- SEC EDGAR (8-Ks for exchange offers, spin-offs and supplemental indentures that drive Successor questions): https://www.sec.gov/edgar
- CourtListener REST API (dockets such as *U.S. Bank N.A. v. Windstream Services, LLC*, SDNY): https://www.courtlistener.com/help/api/

<!-- STATUS: COMPLETE -->
