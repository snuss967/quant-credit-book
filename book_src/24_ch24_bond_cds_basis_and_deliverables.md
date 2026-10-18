# Chapter 24: Bond-to-CDS Basis & Deliverable Obligation Mechanics

*7:41 a.m.* Theo had written the trade on a sticky note. On this desk that counted as either retro or a compliance event. *Buy \$10mm Halvorsen Packaging 6% Senior Notes due 2031 at 88. Buy \$10mm five-year Halvorsen CDS at 370 bp. Bond Z-spread: 480. Basis: −110.* (Halvorsen is fictional; all numbers illustrative.)

"A hundred and ten basis points of riskless carry," Kaz said. "If they default, the swap pays par minus recovery, the bond pays recovery, and we're flat. It's a tautology with a coupon."

"But what does the credit agreement say?" Theo asked.

"There is no credit agreement. It's a swap."

"Then what do the Definitions say?"

Kaz blinked. "Is a 'deliverable obligation' the one with free shipping?"

From the end of the row, without looking up, Mags said, "Back in my day the basis was free money too. In the autumn of 2008 it was free money at minus several hundred, and the people who owned it learned that a repo haircut is just a margin call that's been patient."

Ines put down her coffee. "What's the pot, what are the odds, and who at this table knows more than you? Start with the pot. Halvorsen files tomorrow. What do you make?"

Theo did it on the sticky note. "The bond drops from 88 to recovery, call it 40, so I lose 48 points. The swap pays 100 minus 40, so I make 60. Net plus twelve points on ten million." He frowned. "I'm over-hedged. The swap is a par instrument and my bond isn't at par."

"Good. Now suppose they don't file. Suppose they skip one coupon on one bond, on purpose, and the swap triggers anyway."

"Then the bonds don't accelerate and trade on their cash flows. Halvorsen has a 3% 2045 from the 2021 bubble. It's deliverable, it's at 52, and it would be the cheapest thing in the auction." Theo stopped. "So the swap pays 48 whether or not anybody actually loses anything."

"Somebody paid for that 48," Ines said. "Find out who before you buy their side of it."

Kaz was rereading the confirmation. "So the question isn't whether the bond and the swap disagree. It's which one of them is lying."

That is the question this chapter answers. *When the bond and the CDS of the same company disagree, which one is wrong, by how much, and what exactly does the swap pay when the company dies, or when someone arranges for it to look dead?*

By the end of this chapter you will be able to: price both legs of a CDS, compute the risky annuity, and convert between running spread and points upfront; compute four different "bases" for the same bond and say which one is honest; turn funding, haircuts and repo specialness into an arbitrage band and a return on equity; value the cheapest-to-deliver option and simulate the two-stage credit event auction; build a mean-reversion basis signal that survives transaction costs; run the successor arithmetic; and flag orphaning and manufactured-credit-event risk before the Determinations Committee rules on it.

## 24.1 Two Doctors, One Patient, and the Frictionless Lie

The Part VI opener described four doctors looking at one patient. This chapter is about the two who argue most: the cash bond and the credit default swap. In a frictionless world they cannot disagree, and the argument for that is short enough to write on Theo's sticky note.

> **[SOURCE EXTRACTION]** *Schmid_Credit_Risk_Pricing_Models p.254:* "We short the par issued defaultable floating rate note and invest the money in a par issued default-free floating rate note and hold this portfolio either until to maturity or a credit event occurs"
>
> **Annotation.** Our analysis: this is the founding argument of the basis, and the rest of the chapter is a list of the ways it fails. The portfolio pays a fixed spread every period and receives $1-R$ if the issuer defaults, which is exactly the protection buyer's side of a CDS. So the CDS spread must equal the floater's spread, and the basis must be zero. On a 2026 desk almost nothing in the argument survives intact. Few issuers have par floaters outstanding, so you compare a swap with fixed-coupon bonds at 88 or 104. Shorting a corporate bond means borrowing it in a repo market that may charge you for the privilege. "Invest the money" assumes you can fund at the risk-free rate with no haircut. And "a credit event occurs" assumes the bond and the swap agree on what a credit event is. Each assumption breaks in its own section of this chapter, and each break has a sign and a size you can model.

Write the argument out. Let $r_{t}$ be the floating rate (SOFR after the 2021–2023 Libor cessation), and let coupon dates be $t_1 < \dots < t_n = T$ with accrual fractions $\alpha_i$. A par defaultable floater pays $(r_{t_{i-1}} + s^{\text{FRN}})\alpha_i$ at $t_i$ while the issuer survives. A par default-free floater pays $r_{t_{i-1}}\alpha_i$. Short the first and buy the second. Both cost par, so the package costs nothing. While the issuer survives, the package pays $s^{\text{FRN}}\alpha_i$ each period, because the floating legs cancel. If default happens on a coupon date $t_i$, unwind: the default-free floater has just reset, so it is worth exactly 1, and the defaulted floater is worth its recovery $R$. You receive $1-R$.

A protection buyer in a CDS with spread $s^{\text{CDS}}$ pays $s^{\text{CDS}}\alpha_i$ per period while the issuer survives and receives $1-R$ at default. The two cash-flow streams are the same up to the spread, and both packages cost zero. No-arbitrage under $\mathbb{Q}$ then forces

$$
s^{\text{CDS}} = s^{\text{FRN}}, \qquad b \equiv s^{\text{CDS}} - s^{\text{bond}} = 0.
$$

That is the whole frictionless theory of the basis. The basis $b$ is defined as CDS minus bond, in bp, with the bond spread measured one of several ways (§24.3). A *negative basis* means the bond is cheap relative to the swap: buy the bond, buy protection. A *positive basis* means the bond is rich: short the bond, sell protection.

> **[SOURCE EXTRACTION]** *Schmid_Credit_Risk_Pricing_Models p.254:* "If we allow for default not only at coupon times we liquidate the portfolio at the coupon date immediately after default. Then the relationship Default Swap = Default-Free FRN - Defaultable FRN is only approximately valid."
>
> **Annotation.** Our analysis: this is the smallest crack, and it is worth seeing why it is small. Between coupon dates the default-free floater is worth $B(u, t_i)(1 + r_{t_{i-1}}\alpha_i)$ rather than 1, which differs from par by roughly the interest accrued since the last reset, $r\,(u - t_{i-1})$, a few bp of price on a quarterly reset. The CDS, meanwhile, settles on its own timetable (credit event, auction, settlement about a month later), with the accrued premium paid up to the event. The mismatch is real but second order, worth a basis point or so. It matters because it shows the method: write down the replicating package, then find each place where the real cash flows leave the textbook's. The big leaks, funding, deliverables, and the definition of default, are each worth tens to hundreds of bp.

So list the assumptions, and number them, because each one has been someone's entire P&L at some point:

1. **(A1) The bond is a par floater.** Real bonds are fixed-coupon and trade away from par, and a CDS is a par instrument. Comparing the two needs a convention, and the choice of convention moves the "basis" by 10–20 bp before any economics (§24.3).
2. **(A2) You can fund the long bond at the risk-free rate, with no haircut** (§24.4).
3. **(A3) You can short the bond for free,** at general collateral repo with no specialness or borrow fee (§24.4).
4. **(A4) Your counterparty survives your issuer** (§24.4).
5. **(A5) The swap pays $1-R$ on *this* bond.** It actually pays par minus the auction price of the cheapest deliverable obligation (§24.5–24.6).
6. **(A6) "Default" means the same thing to the bond and the swap.** Hovnanian, Windstream and every orphaning fight since have shown that it need not (§24.8).

The trading consequence is that the basis is never "free money." It is a price for bearing whichever of A1–A6 is currently broken, and the job is to know which one, and to know whether you are being paid enough for it. That leads to the desk motto. The negative basis on Halvorsen is not alpha until you strip out the funding term, the convention term and the deliverable term. IDO or it didn't happen.

There is also a reason the quant desk cares less about single-name CDS than its 2007 predecessor did, and it is a market-structure reason.

> **[SOURCE EXTRACTION]** *Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.11:* "we believe that cash bonds will be the approach of choice for most quantitative investors, above all because breadth is key for quant strategies and is simply not available in synthetic form yet."
>
> **Annotation.** Our analysis: this is the fundamental law of active management (Chapter 9) applied to instrument choice. With $\text{IR} \approx \text{IC}\sqrt{\text{BR}}$, an investable universe of thousands of bonds beats a few hundred liquid single names even if the per-name signal is weaker. The 2026 data (Trend Watch below) make Man's "yet" look optimistic: single-name liquidity has concentrated further since 2022. The departure is in what CDS is *for* on a systematic desk. It is no longer the main alpha instrument. It is a hedge, a source of information (CDS moves first in liquid names; §24.7), and a legal instrument whose payoff you must model as a contract rather than as a spread. The basis is where all three uses meet.

> **Trend Watch: single names thin out while the index eats the market (2021–H1 2026).** *What changed:* ISDA's July 2026 study (*CDS Market Dynamics: Five Years of Activity and a Record 2025*, 29 Jul 2026) reports record global CDS traded notional of \$41.8tn in 2025, above the 2022 peak of \$38.7tn. Index CDS was 93.3% of it, and its share has been near 90% every year. Single-name notional peaked at \$3.3tn in 2023, the year of the regional-bank and Credit Suisse stress, and eased to \$2.8tn in 2025. *How concentrated:* only 20 of 751 single-name reference entities averaged ten or more trades a day in Q4 2025 (14 sovereigns, 6 others), against 69 in Q1 2023. The average single-name ticket was \$6.7mm in 2025, against \$54.3mm for index trades. Europe's Determinations Committee region accounted for 48.9% of single-name activity in 2025, and the Americas for 39.7%. *Stress signature:* relative to trailing four-quarter averages, single-name activity rose 84.8% in Q1 2023 (index +4.5%), while in the April 2025 tariff shock index activity rose 20.9% and single names *fell* 20.7%. Macro shocks go to the index and idiosyncratic shocks go to single names. ISDA's own line is that "higher traded notional does not mean deeper liquidity." *What it means for the desk:* a single-name basis signal exists for perhaps a few hundred names at any time, and the CDS leg of your basis trade may be the less liquid leg. Model the CDS bid–ask by name and by regime, not as a constant. And note that the April 2025 pattern means a negative-basis package hedged with single-name CDS can lose its hedge liquidity in exactly the macro shock that widens the basis.

## 24.2 Pricing the Swap: Two Legs and One Risky Annuity

Desk framing first. A single-name CDS on a North American corporate trades on standardized terms that date from the April 2009 "Big Bang" protocol. There is a fixed running coupon $c$ of 100 or 500 bp, quarterly payment dates on the 20th of March, June, September and December, a full first coupon with an accrual rebate, auction settlement hardwired into the contract, and, for the Standard North American Corporate (SNAC) contract, no Restructuring credit event. Because the coupon is fixed, the price discovered on the screen is *points upfront*. The par spread quoted next to it is a translation, made with an agreed model and a conventional 40% recovery for senior unsecured names. Theo's 370 bp Halvorsen swap actually trades as a 500 bp coupon plus a payment *to* the protection buyer at inception. Every basis calculation starts by inverting that translation correctly.

Kaz's version is shorter. "A CDS is a bond whose coupons stop when the issuer dies, plus a put on the issuer's death. The first leg is an annuity, the second is a lottery ticket, and the spread is the exchange rate between them."

### 24.2.1 Derivation

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

```python
import numpy as np
import pandas as pd
from scipy.optimize import brentq

RNG = np.random.default_rng(24)
ACT360 = 365.0 / 360.0          # CDS premium accrues ACT/360: a year pays ~365/360 of the spread


def premium_schedule(T, freq=4):
    """Premium dates (years) and ACT/360 accrual fractions for a T-year CDS."""
    n = int(round(T * freq))
    if n < 1:
        raise ValueError("maturity shorter than one premium period")
    t = np.arange(1, n + 1, dtype=float) / freq
    alpha = np.full(n, ACT360 / freq)
    return t, alpha


def survival(t, lam):
    return np.exp(-lam * np.asarray(t, dtype=float))


def disc(t, r):
    """OIS discount factor B(t); not called D because D is reserved for duration."""
    return np.exp(-r * np.asarray(t, dtype=float))


def rpv01(lam, r, T, freq=4, accrued_on_default=True):
    """Risky annuity: Q-value of 1.0 (decimal) of running spread per year, paid quarterly."""
    t, a = premium_schedule(T, freq)
    S = survival(t, lam)
    S_prev = np.concatenate(([1.0], S[:-1]))
    value = np.sum(a * disc(t, r) * S)
    if accrued_on_default:                       # half a period of premium, on average
        value += np.sum(0.5 * a * disc(t - 0.5 / freq, r) * (S_prev - S))
    return float(value)


def protection_leg(lam, r, T, R):
    """(1-R) * int_0^T B(u) lam S(u) du, closed form for flat lam and r."""
    k = lam + r
    if abs(k) < 1e-12:
        return (1.0 - R) * lam * T
    return (1.0 - R) * lam / k * (1.0 - np.exp(-k * T))


def par_spread(lam, r, T, R):
    return protection_leg(lam, r, T, R) / rpv01(lam, r, T)


def hazard_from_spread(s, r, T, R):
    """Flat Q-hazard that reprices a quoted par spread s (decimal)."""
    return brentq(lambda x: par_spread(x, r, T, R) - s, 1e-10, 5.0)


def upfront(s_par, coupon, lam, r, T):
    """Fraction of notional the protection BUYER pays at trade (negative: buyer receives)."""
    return (s_par - coupon) * rpv01(lam, r, T)


# Sanity checks: the credit triangle, the bootstrap, and the upfront convention
r0, T0, R0, lam0 = 0.04, 5.0, 0.40, 0.05
s0 = par_spread(lam0, r0, T0, R0)
assert abs(s0 / (lam0 * (1.0 - R0) / ACT360) - 1.0) < 0.015    # s ~ lam(1-R), ACT/360-adjusted
assert abs(hazard_from_spread(s0, r0, T0, R0) - lam0) < 1e-9    # bootstrap round trip
assert abs(upfront(s0, s0, lam0, r0, T0)) < 1e-15               # par coupon: no upfront
pts_500 = 100.0 * upfront(s0, 0.05, lam0, r0, T0)
assert -9.0 < pts_500 < -7.5                                     # buyer RECEIVES about 8 points
assert rpv01(lam0, r0, T0, accrued_on_default=False) < rpv01(lam0, r0, T0)
```

The numbers are worth reading once. At $\lambda = 5\%$, $R = 40\%$ and $r = 4\%$, the five-year par spread is about 297 bp, slightly below the triangle's 300 bp because of the ACT/360 factor and slightly above the ACT/360-adjusted 296 bp because premiums are paid at the end of each quarter. The risky annuity is about 4.06 years. Against a 500 bp coupon, the buyer receives about 8.2 points upfront. Theo's 370 bp Halvorsen swap sits between those cases, and the same three functions price it.

## 24.3 Four Things People Mean by "Basis"

Theo's sticky note said "basis: −110." Ines's first question was "against what?", and it was the right question, because there are at least four honest answers and they can differ by more than the signal.

1. **Z-spread basis.** $b^{Z} = s^{\text{CDS}}(T) - Z$, where $Z$ is the constant spread over the OIS curve that reprices the bond's cash flows. It is the easiest to compute and the hardest to defend.
2. **Asset-swap basis.** $b^{\text{ASW}} = s^{\text{CDS}}(T) - A$, where $A$ is the par-par asset-swap spread. You pay par for the bond (whatever its price), swap its fixed coupons for floating plus $A$, and the upfront difference $P^{\text{rf}} - P$ is amortized over the swap's annuity: $A = (P^{\text{rf}} - P)/\text{PV01}^{\text{rf}}$, where $P^{\text{rf}}$ is the bond's price discounted on the risk-free curve. This is how a bank's treasury desk thinks about the bond, and it carries the same par-versus-price problem as $Z$.
3. **Par-equivalent CDS spread (PECS) basis.** $b^{\text{PE}} = s^{\text{CDS}}(T) - \text{PECS}$. Take the hazard curve bootstrapped from the CDS, shift it in parallel until the bond's model price under that curve, with the CDS's recovery, matches the market price, and read off the par CDS spread at the shifted curve. It is the only one of the four that compares like with like.
4. **Issuer-level basis.** One number per issuer, aggregating all its bonds. Dynkin's version is the one most systematic research uses.

> **[SOURCE EXTRACTION]** *Dynkin_Systematic_Investing_in_Credit p.216:* "We define the cash–CDS basis as the difference between the spread of a 5y CDS and the market value‐weighted OAS (computed relative to the Libor curve) of all unsecured bonds issued by the underlying reference entity."
>
> **Annotation.** Our analysis: this is an operational definition, built to give one basis per issuer across a large panel, and for cross-sectional research it is the right design. Note the three choices inside it, because each one becomes a parameter on a 2026 desk. "Relative to the Libor curve" now means relative to SOFR swaps or OIS, and the switch moves the level of every basis in the panel by the spread between the curves. "Market value-weighted" mixes bonds at 70 with bonds at 105, which, as the derivation below shows, mixes spurious positive and negative bases. "All unsecured bonds" excludes secured paper, correctly, since secured bonds are not what the swap is priced on, but it also excludes the loans that may be deliverable. A desk that trades the basis bond by bond should use PECS at the bond level. A desk that uses the basis as a feature can use Dynkin's definition, provided the same convention is used every month.

### 24.3.1 Derivation: why a par swap and a discount bond disagree even when nothing is wrong

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

*(Hand calculation, continuous coupons, illustrative; the semiannual code below reproduces the signs and sizes.)* All three bonds are priced exactly off the CDS hazard. There is no mispricing anywhere in the table, and yet the Z-spread reports a positive basis on the discount bond and a negative basis on the premium bond. The intuition is RFV against RMV. The 4% bond at 88 loses $88 - 40 = 48$ points at default, 55% of its value. The 10% bond at 112 loses 72 points, 64% of its value. A constant Z-spread charges both the same proportional loss, so it understates the discount bond's spread and overstates the premium bond's. In a market where coupons set in 2020–2021 are trading at 85 and coupons set in 2023–2024 are trading at 103 (illustrative), the Z basis has a vintage pattern built into it that a careless signal will read as alpha.

> **[SOURCE EXTRACTION]** *Schmid_Credit_Risk_Pricing_Models p.159:* "A default swap is a par product: it does not completely hedge the loss on an asset that is currently trading away from par. If the asset is trading at a discount, a default swap overhedges the credit risk and vice-versa."
>
> **Annotation.** Our analysis: this is Theo's sticky-note arithmetic, and it has two consequences the desk must keep separate. The first is *valuation*: comparing a par instrument with a bond at 88 requires PECS or an equivalent, or you read the table above as a trade. The second is *hedging*: the jump-to-default-neutral notional is not the bond's face. The bond loses $P - R$ at default and the swap pays $1 - R$, so the JTD-neutral CDS notional per unit of bond face is $N^{\text{JTD}} = (P - R)/(1-R)$. For Halvorsen at 88 with $R = 40\%$, that is $48/60 = 0.8$: \$8mm of protection on \$10mm of bonds. A desk that buys \$10mm is also long \$2mm of a jump-to-default bet, which is fine if intended and a hidden position if not. The modern departure is that $R$ itself is uncertain, so $N^{\text{JTD}}$ has a recovery delta. The package is flat at default only if the auction's recovery equals the bond's, which is the subject of §24.5.

Two more conventions move the measured basis before any economics enters.

> **[SOURCE EXTRACTION]** *Bohn_Stein_Active_Credit_Portfolio_Management p.578:* "Our own research and that of our colleagues suggests that CDS premia can be interpreted as implicit spreads over a corporate default-risk borrowing curve, which is typically 10 to 20 basis points below the dollar swap curve."
>
> **Annotation.** Our analysis: the discount curve is a basis input, and choosing it is a decision, not a default setting. Bohn and Stein were writing about the Libor-swap world, in which the "risk-free" curve itself contained bank credit. Since the Libor cessation the desk has SOFR OIS, a cleaner risk-free proxy, and the gap between that curve and the curve at which a levered basis trader actually funds is now the repo spread $\phi$ of §24.4. The rule for the specifier is mechanical: compute the bond's Z-spread or PECS and the CDS's hazard curve off the *same* curve, store the curve's name and date with every basis observation, and treat a switch of curve as a structural break in the time series.

The second convention is seniority and security. The CDS references senior unsecured obligations; if most of an issuer's bonds are secured, the bonds trade rich to the swap for reasons that have nothing to do with mispricing.

> **[SOURCE EXTRACTION]** *Dynkin_Systematic_Investing_in_Credit p.220:* "all issuers but one in the Airlines and Railroad industry had positive bases, reflecting the fact that debt in these industries is largely secured and bonds typically trade rich relative to CDS."
>
> **Annotation.** Our analysis: this is a deliverable-quality effect showing up in a basis table, and it is a good bridge to §24.5. A secured equipment bond pays a high recovery in default. The CDS pays par minus the auction price of whatever senior unsecured obligation is cheapest. The two are not claims on the same loss, so the basis is structurally positive. For a 2026 desk this matters most in sectors where liability management transactions have created layers of secured debt above the unsecured bonds that remain deliverable (Chapter 13). There, the basis between a new super-priority bond and the swap tells you very little about mispricing and a great deal about where the CDS will settle.

Positive bases are not only structural. In early 2016, as European bank credit sold off, investors hedged with CDS faster than they sold bonds, and IHS Markit's commentary of 31 March 2016 showed bases on several bank names in positive territory, Deutsche Bank's 1.25% notes due September 2021 among them, at 95 bp in February tightening to 73 bp in March. When everyone wants protection at once, the swap leads, and the positive basis is the hedging queue.

### Specification for AI Implementation (bond-level basis: Z, PECS and JTD hedge ratio)

**What ROBO built from the vague version.** Told to "compute the basis," ROBO subtracted the bond's *yield* from the CDS spread, reported a basis of −580 bp on every bond in the universe, and recommended buying all of them. When asked, it pointed out that this was what had been asked.

**The precise spec.** Inputs: coupon `c` (decimal, semiannual 30/360), maturity `T` (years from a coupon date; no accrued in this sketch), market price per unit face, flat OIS rate `r`, recovery `R`, and the CDS par spread from §24.2. Outputs: `z_spread` (decimal), `pecs` (decimal, with the implied flat hazard), the bases $b^{Z}$ and $b^{\text{PE}}$ in bp, and `jtd_hedge_ratio` (CDS notional per unit face). Guards: refuse a PECS when the price is outside the model's range, typically a bond trading below the assumed recovery, and say so instead of returning a root at the bracket edge. With a term structure, shift the bootstrapped piecewise hazard curve in parallel rather than replacing it with a flat one. Sanity: a bond priced off the CDS hazard has a PECS basis of zero to $10^{-9}$, while its Z basis is positive for a discount bond and negative for a premium bond.

```python
def bond_cashflows(c, T, freq=2):
    """Coupon dates (years) and cash flows per 1.0 face; 30/360 semiannual coupons."""
    n = int(round(T * freq))
    t = np.arange(1, n + 1, dtype=float) / freq
    cf = np.full(n, c / freq)
    cf[-1] += 1.0
    return t, cf


def bond_price_hazard(c, T, lam, r, R, freq=2):
    """Q-price per 1.0 face: survival-weighted cash flows plus recovery of face R at default."""
    t, cf = bond_cashflows(c, T, freq)
    k = lam + r
    rec = R * lam * T if abs(k) < 1e-12 else R * lam / k * (1.0 - np.exp(-k * T))
    return float(np.sum(cf * np.exp(-k * t)) + rec)


def z_spread(price, c, T, r, freq=2):
    """Constant spread over the flat continuous OIS curve that reprices the bond."""
    t, cf = bond_cashflows(c, T, freq)
    return brentq(lambda z: np.sum(cf * np.exp(-(r + z) * t)) - price, -0.05, 3.0)


def pecs(price, c, T, r, R, freq=2):
    """Par-equivalent CDS spread: par CDS spread at the flat hazard that reprices the bond."""
    lo, hi = 1e-10, 5.0
    p_hi, p_lo = bond_price_hazard(c, T, hi, r, R, freq), bond_price_hazard(c, T, lo, r, R, freq)
    if not p_hi < price < p_lo:
        raise ValueError("price outside the model's range: is the bond below the assumed recovery?")
    lam_star = brentq(lambda x: bond_price_hazard(c, T, x, r, R, freq) - price, lo, hi)
    return par_spread(lam_star, r, T, R), lam_star


def jtd_hedge_ratio(full_price, R):
    """CDS notional per 1.0 bond face that is flat on an instantaneous default."""
    return (full_price - R) / (1.0 - R)


s_cds = par_spread(lam0, r0, T0, R0)
rows = []
for cpn in (0.04, 0.07, 0.10):                    # discount, near-par, premium bonds
    P = bond_price_hazard(cpn, T0, lam0, r0, R0)
    s_pe, _ = pecs(P, cpn, T0, r0, R0)
    z = z_spread(P, cpn, T0, r0)
    rows.append({"coupon": cpn, "price": 100.0 * P, "Z_bp": 1e4 * z, "PECS_bp": 1e4 * s_pe,
                 "basis_Z_bp": 1e4 * (s_cds - z), "basis_PECS_bp": 1e4 * (s_cds - s_pe)})
    assert abs(s_pe - s_cds) < 1e-9               # priced off the CDS hazard: PECS basis is zero
basis_table = pd.DataFrame(rows)
assert basis_table.Z_bp.iloc[0] < 1e4 * s_cds < basis_table.Z_bp.iloc[2]   # ...the Z basis is not
assert abs(jtd_hedge_ratio(0.88, 0.40) - 0.80) < 1e-12                     # Theo's sticky note
```

Note what the code's table adds to the hand calculation: the CDS leg here is ACT/360, so even the near-par bond shows a Z basis of a few bp. That is the day-count term from §24.2 appearing in a P&L, and it is a reason to run this table on every new data vendor before trusting its basis field.

## 24.4 Funding, Repo, and the Counterparty: Why a Negative Basis Is Not Free

Mags tells the 2008 story without names. "We owned bonds at a spread of six hundred and protection at three hundred on the same names. Minus three hundred of basis. Riskless, everyone said. Then the prime broker raised the haircut from ten to twenty-five, the basis went to minus five hundred, and the riskless trade had to be sold to the only people with balance sheet, who were the people who'd raised the haircut." It is a war story, and it is also a derivation, because each of its clauses is a term in the carry equation.

### 24.4.1 Derivation: the carry of each package and the arbitrage band

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

**Mark-to-market.** The package is long the basis, so for a small move its value changes by $\Delta V \approx D^{\text{spr}}\,\Delta b$ per unit face. Per unit of equity this is $D^{\text{spr}}\,\Delta b / h$. If the basis widens from −100 to −250 bp with $D^{\text{spr}} = 4.5$, the package loses $0.0150 \times 4.5 = 6.75$ points, which is 45% of a 15-point haircut. Convergence is guaranteed only at maturity or default, and only up to the deliverable and recovery terms of §24.5. The trader has to survive until then, and the haircut and the basis are both driven by the same thing, the cost of balance sheet. That is Mags's story in two equations: the carry falls when $h$ rises, and the mark-to-market loss is divided by $h$.

> **Poker Table.** "A negative basis is a hand you can't lose at showdown," Ines says. "Hold it to maturity and it pays. The problem is that you don't get to see the showdown if you can't cover the bets on the turn. Your stack is the haircut. The other players are the people who set it. Before you play this hand, ask how much it costs to stay in, and who decides."

**Counterparty risk.** The last friction concerns the other side of the swap.

> **[SOURCE EXTRACTION]** *Bohn_Stein_Active_Credit_Portfolio_Management p.577:* "Note that buying protection is similar in form to shorting a loan or bond. While the value of the position may behave similarly to a short-loan or short-bond position, the presence of this joint default probability issue makes the CDS analysis a little more involved."
>
> **Annotation.** Our analysis: protection is only worth what the protection seller can pay. Write $\tau_c$ for the seller's default time. The protection leg the buyer actually owns is $(1-R)\,\mathbb{E}^{\mathbb{Q}}\big[B(\tau)\,\mathbf{1}\{\tau \le T,\ \tau_c > \tau\}\big]$ plus whatever the buyer recovers from the seller, and with positive correlation between $\tau$ and $\tau_c$ (wrong-way risk) it is worth noticeably less than the clean leg. A buyer who prices that in pays a lower spread, so counterparty risk is a *negative*-basis driver, and in 2008 it was a large one, with dealers' own CDS widening alongside their clients' bonds. Central clearing changed the term but did not remove it. The counterparty is now a clearinghouse, and the cost moves into initial margin, which is a funding cost and enters through $\phi$. In 2025, 63.1% of US-reported single-name notional and 78.1% of index notional was cleared (ISDA, July 2026), so the uncleared remainder still needs a CVA charge in the basis engine.

Two more pieces of evidence shape how the desk uses the band. Choi, Shachar and Shin (2019, *Management Science*) find that over 2005–2009 dealers on average traded *against* a widening bond–CDS gap, stabilizing it, until their balance-sheet constraints bound and the stabilization stopped. Oehmke and Zawadowski (2015, "Synthetic or Real? The Equilibrium Effects of Credit Default Swaps on Bond Markets," *Review of Financial Studies* 28(12)) model the CDS as a cheaper way to take credit exposure, which pulls some demand away from bonds while also making room for levered basis traders who bridge the two markets. Both point the same way. The negative basis is a price for balance sheet, and its tails come when balance sheet is scarce.

> **Trend Watch: the basis in three stresses, and the clearinghouse in the middle (2008–2025).** *2008:* Bai and Collin-Dufresne's working-paper figures (as summarized in our research dossier; secondary) put the investment-grade basis, normally a few bp positive, at about −250 bp at the 2008 trough, and the high-yield basis at about −650 bp. *March 2020:* Risk.net reported the US high-yield bond–CDS basis at about −401 bp, roughly eight times its weekly average since mid-2010, and the US investment-grade basis at about −186 bp (secondary; magnitudes depend on the index and definition). The move unwound after the Federal Reserve announced its corporate credit facilities on 23 March 2020, which is consistent with the band: the facilities lowered $\phi$ and $k^{-}$, the cost of holding bonds, and the negative edge moved back in. *2023:* the regional-bank and Credit Suisse stress was a single-name event. ISDA reports single-name traded notional up 84.8% in Q1 2023 against its trailing four-quarter average, with \$161bn in financials, while index activity rose only 4.5%. *Clearing:* ICE Clear Credit reported a record \$2.57tn of USD single-name CDS cleared in 2025, against \$2.17tn in 2024 (ICE press release, 6 Jan 2026; secondary), and ICE Clear Europe stopped clearing CDS in October 2023, moving more than \$400bn of open interest (ISDA, July 2026). *What it means for the desk:* every large negative basis since 2008 has been a funding event first and a credit event second. Make the basis model regime-aware: a −150 bp basis with funding conditions calm is a signal, and the same basis with repo haircuts rising is a warning about the people already holding it.

### Specification for AI Implementation (basis package carry and stress)

**The precise spec.** Inputs: the basis in bp ($s^{\text{CDS}} - s^{\text{bond}}$, negative for a negative basis), the repo funding spread $\phi$ in bp over the floating rate, the haircut $h \in (0,1]$, and the spread duration. Outputs: annual excess ROE on equity, and mark-to-market on equity for a given move in the basis. Guards: reject $h \le 0$. Never report an ROE without the haircut that produced it, and run the same position at the stressed haircut (at least double the current one) beside the base case. Sanity: the 4.4%, 2.4% and −45% figures above, and negative carry for a basis inside the band.

```python
def basis_package_roe(basis_bp, repo_spread_bp, haircut):
    """Annual excess carry per unit of equity for a near-par negative-basis package."""
    if not 0.0 < haircut <= 1.0:
        raise ValueError("haircut must be in (0, 1]")
    carry_bp = -basis_bp - repo_spread_bp * (1.0 - haircut)
    return carry_bp / 1e4 / haircut


def basis_mtm_on_equity(d_basis_bp, spread_duration, haircut):
    """Mark-to-market on equity when the basis moves by d_basis_bp (package is long the basis)."""
    return d_basis_bp / 1e4 * spread_duration / haircut


assert abs(basis_package_roe(-100.0, 40.0, 0.15) - 0.044) < 1e-12     # calm
assert abs(basis_package_roe(-100.0, 40.0, 0.30) - 0.024) < 1e-12     # haircut doubles
assert abs(basis_mtm_on_equity(-150.0, 4.5, 0.15) + 0.45) < 1e-12     # basis -100 -> -250
assert basis_package_roe(-30.0, 40.0, 0.15) < 0.0                     # inside the band: pays to hold
```

> **Ways This Blows Up.** (1) *ROE without the haircut process.* A backtest at a constant 15% haircut overstates the Sharpe ratio, because the haircut rises exactly when the basis widens. Model $h_t$ as a function of a funding-stress index, or at least backtest at the stressed haircut. (2) *JTD drift.* $N^{\text{JTD}} = (P-R)/(1-R)$ changes as the bond price moves. A package set up flat at 95 is materially over-hedged at 70. Rebalance the CDS notional on a price band, and charge the rebalancing to the trade. (3) *Maturity mismatch.* A 4.3-year bond hedged with the 5-year standard swap leaves a curve position. Interpolate the CDS curve to the bond's maturity for the basis, and hedge with the two adjacent standard maturities. (4) *Treating the clearinghouse as free.* Initial margin on the CDS leg is funded. Put it in $\phi$, or the cleared package looks better than the bilateral one by exactly the amount you forgot.
