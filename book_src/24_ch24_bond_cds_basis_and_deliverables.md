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
