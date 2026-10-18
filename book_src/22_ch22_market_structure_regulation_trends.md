# Chapter 22: Market-Structure Regulation & the Forces Reshaping Liquidity

*Tuesday, 3:41 p.m., two business days before quarter-end.* The RFQ was ordinary in every way a model can see. *Client sells \$15mm Calloway Industrial 5.10% Senior Notes due 2033 (a fictional issuer; Baa2/BBB), four dealers in competition, two minutes to respond.* Same CDS level as last Tuesday. Same equity. Same news, which was none. And yet the auto-quoter bid three-eighths of a point lower than it had a week earlier, for the same bond in the same size.

"Something's broken," Theo said. "Nothing moved."

"Nothing moved in the features," said Kaz, scrolling. "Spread vol, inventory, the win curve. All flat. I assumed regulation was a constant."

"The pot didn't change," said Ines, without looking up. "The table did. Thursday is quarter-end, and every balance sheet on the Street is getting dressed for a photograph, ours included. Treasury sent the hurdle rate for the snapshot this morning. If we buy this, we're paying rent on it through the photo. And whoever we sell it to has to see our print inside fifteen minutes. Which, you'll be relieved to hear, is still fifteen."

Theo opened a new window out of habit. "But what does the credit agreement say?"

"There isn't one," Ines said. "There's the Federal Register."

"So it's a credit agreement with worse fonts and better enforcement."

"Back in my day," said Mags, from behind a stack of 10-Qs, "the regulator was a phone call from the Fed and a fax nobody read." She considered this. "The new way is better, honestly. The fax never told you the effective date."

Kaz had stopped scrolling. "So the rule is a feature."

"The rule is a price," Ines said. "And the day it changed is a date in every series you've ever trained on."

That is the question this chapter answers: *how do you put a price on a rule, and how do you know when a rule changed the data?*

By the end of this chapter you will be able to: decompose a dealer's quote into the three things regulation taxes (balance sheet, time, and information); add a regulatory cost-of-carry term to the Avellaneda–Stoikov quotes of Chapter 18 and compute the breakeven holding period below which principal market making beats agency; price a reporting delay as an option held by the block dealer, and back out the size distribution hidden behind TRACE's \$5mm and \$1mm caps; derive why T+1 cut clearing margin by roughly a quarter; compute how much balance sheet multilateral netting buys under the Treasury clearing mandate and why it stops helping when the market is one-way; read the capital-rule saga from Volcker to the 2026 Basel III re-proposal as a sequence of price changes; and build a dated regime table plus a difference-in-differences engine that tells you whether a rule moved your data or whether something else did.

## 22.1 A Rule Is a Price: Taxes on Balance Sheet, Time, and Information

A restructuring banker learns to read a credit agreement for the trapdoors: the basket that permits the drop-down, the definition that lets the sponsor add back synergies nobody will ever see. The skill transfers intact. An SEC adopting release has effective dates, phase-ins, carve-outs ("natural persons," "sovereign entities," "inter-affiliate"), and a compliance date that slips. Read it the way you read a covenant package and you find where the liquidity will and will not be.

The organizing idea of this chapter is that a dealer sells exactly three things, and every market-structure rule is a tax or a subsidy on one of them:

1. **Balance sheet.** The dealer lends its capital to the customer for as long as the inventory sits on its books. Leverage ratios, risk-based capital, and clearing and netting rules set the rent.
2. **Time.** The settlement cycle sets how long counterparty exposure lasts; Volcker's inventory limits set how long the dealer may wait for the other side; reporting delays set how long the dealer's private information stays private.
3. **Information.** TRACE and the security-based swap reporting regime (SBSR) decide who learns what, and when.

| Rule (key date) | Input taxed (−) or subsidized (+) | Where it enters the quote | See |
| :--- | :--- | :--- | :--- |
| Supplementary leverage ratio and its enhanced version (eSLR); recalibrated effective 2026-04-01 | Balance sheet (−), the same rate on every dollar | Rent term $c_{\text{reg}}$; binds on low-risk assets | §22.5 |
| Basel III risk-based capital; endgame proposals 2023 and 2026 | Balance sheet (−), risk-weighted | Rent term on risky inventory | §22.5 |
| Volcker Rule (revised 2019, effective 2020-01-01) | Time (−): inventory must track expected customer demand | Caps the holding period $\tau^{\text{hold}}$ | §22.5 |
| T+1 settlement (2024-05-28) | Time (+ for margin, − for operations) | Margin scales like $\sqrt{H}$; fail probability | §22.3 |
| Treasury clearing mandate (cash 2026-12-31, repo 2027-06-30) | Balance sheet (+ via netting), liquidity (− via margin) | Netting factor $\phi(N)$ against IM funding | §22.4 |
| TRACE: 15-minute reporting; \$5mm IG and \$1mm HY dissemination caps | Information (+ for blocks) | Block spread falls with the delay and the cap | §22.2 |
| CDS index clearing (2013), SBSR public dissemination (2022-02-14) | Information and balance sheet | Cost of the CDS hedge | §22.6 |

A systematic desk does not "comply with" this table; compliance is the legal department's job. The desk *prices* it. Two consequences follow. First, every rule shows up as a term in the quote, so the market maker of Chapter 18 acquires a fifth component next to fear, greed, suspicion, and the value of tomorrow's flow: **rent**. Second, every rule has an effective date, and every effective date is a candidate structural break in every series the desk trains on. The chapter is therefore two machines: a pricing machine (§22.1–§22.6) and a dating machine (§22.2 and §22.8).

> **[SOURCE EXTRACTION]** *Bohn_Stein_Active_Credit_Portfolio_Management p.25:* "we view bank regulation similarly to financial accounting—something that has to be done, both for the sake of the bank and the broader financial system, but not something that should be the main driver of an institution's business decisions." Also: "financial institutions scramble to respond to (and sometimes try to arbitrage) the rules."
>
> **Annotation.** Our analysis: Bohn and Stein were writing about the gap between regulatory and economic capital in a bank's credit portfolio, and their advice for a portfolio manager still holds: do not let the regulatory number stand in for the risk number. For a dealer in 2026 the advice runs the other way. When the leverage ratio binds, the regulatory number *is* the economic cost of the marginal trade, because Tier 1 is the scarce input and the hurdle rate on it is real money. The second sentence is the more useful one for a former restructuring banker. "Scramble to respond to (and sometimes try to arbitrage)" describes the liability-management game of Chapter 13 played against a regulator instead of a lender group: find the basket, read the definition, time the phase-in. The quarter-end photograph in the cold open is the market's version of an EBITDA add-back.

### 22.1.1 Derivation: the regulatory cost of carry in the reservation price

Everything in this subsection is under the physical measure $\mathbb{P}$: inventory risk is a real-world variance, and capital ratios are accounting identities, not probabilities.

**Capital per unit of inventory.** A dealer holds signed inventory $q$ (lots) of a bond with mid $S_t$ (points per lot). The Tier 1 capital the position consumes is

$$
K(q) = |q|\,\bar S\,\kappa, \qquad \kappa = \max\!\big(\kappa_{\text{RWA}}\cdot \text{RW},\ \kappa_{\text{LR}}\big),
$$

where $\bar S$ is the price level, frozen at today's mid over a short horizon; $\kappa_{\text{RWA}}$ is the risk-based requirement including buffers (for example, 10.5% for total capital including the conservation buffer); $\text{RW}$ is the risk weight, or the market-risk charge per unit of notional written as an equivalent risk weight; and $\kappa_{\text{LR}}$ is the leverage requirement. Before 2026-04-01, $\kappa_{\text{LR}}$ was 5% for a US G-SIB holding company (the 3% SLR plus a fixed 2% buffer). Since then it has been 3% plus half the bank's Method 1 G-SIB surcharge. The absolute value matters: a short position also consumes balance sheet, through the reverse repo or securities borrow that delivers the bond.

**The rent rate.** Let $h$ be the hurdle: the annual return the bank demands on Tier 1 *in excess of* its funding rate. Funding is already in the carry of the bond, so $h$ must be the excess return or the funding cost gets counted twice. The regulatory cost of carry per dollar-year of gross inventory is

$$
c_{\text{reg}} = h\,\kappa = h\cdot\max\!\big(\kappa_{\text{RWA}}\,\text{RW},\ \kappa_{\text{LR}}\big).
\tag{22.1}
$$

**Frozen-inventory value with rent.** Take the Avellaneda–Stoikov setup of §18.4: the mid follows $dS_t = \sigma\,dW_t$, the dealer has cash $x$ and exponential utility with risk aversion $\gamma$, and the horizon is $T$. If the dealer holds $q$ to $T$ without trading, its terminal wealth is $x + qS_T$ minus the rent paid along the way, $c_{\text{reg}}\bar S|q|(T-t)$. Taking the expectation of $-\exp(-\gamma\,\cdot)$ over the Gaussian $S_T$ gives

$$
v(x,s,q,t) = -\exp\!\Big(-\gamma\big[x + qs - c_{\text{reg}}\bar S\,|q|\,(T-t)\big]\Big)\exp\!\Big(\tfrac12\gamma^2 q^2\sigma^2 (T-t)\Big).
$$

**Indifference prices.** The reservation bid $r^b$ is the price at which the dealer is indifferent to buying one more lot, $v(x - r^b, s, q+1, t) = v(x, s, q, t)$. The reservation ask $r^a$ solves $v(x + r^a, s, q-1, t) = v(x, s, q, t)$. Take logs, cancel the common terms, and use $(q\pm1)^2 - q^2 = \pm 2q + 1$:

$$
r^b(q) = s - \tfrac12(2q+1)\,\gamma\sigma^2(T-t) - c_{\text{reg}}\bar S\,(T-t)\,\big(|q+1| - |q|\big),
$$

$$
r^a(q) = s - \tfrac12(2q-1)\,\gamma\sigma^2(T-t) + c_{\text{reg}}\bar S\,(T-t)\,\big(|q-1| - |q|\big).
$$

The absolute value puts a kink at $q = 0$, so the two cases behave differently.

*Flat dealer ($q = 0$).* Then $|q+1| - |q| = 1$ and $|q-1| - |q| = 1$, so the bid falls and the ask rises by the full rent:

$$
r^a(0) - r^b(0) = \gamma\sigma^2(T-t) + 2\,c_{\text{reg}}\bar S\,(T-t).
$$

*Long dealer ($q \ge 1$).* Then $|q+1| - |q| = 1$ but $|q-1| - |q| = -1$: buying adds rent and selling saves it. Both indifference prices shift down by the same amount, so the spread is unchanged and the midpoint moves:

$$
r^{\text{res}}(q) = \tfrac12\big(r^a + r^b\big) = s - q\,\gamma\sigma^2(T-t) - \operatorname{sgn}(q)\,c_{\text{reg}}\bar S\,(T-t),
\tag{22.2}
$$

with $\operatorname{sgn}(0) = 0$. The short case is the mirror image. The Avellaneda–Stoikov first-order condition from §18.4 still places each quote at the indifference price plus the markup $\tfrac{1}{\gamma}\ln(1 + \tfrac{\gamma}{k})$, because the rent enters only through $r^a$ and $r^b$. Replace $T - t$ with the expected holding period, as in the worked example of §18.4; we write it $\tau^{\text{hold}}$, with the superscript keeping it apart from the default time $\tau$. A flat dealer's quoted spread is then

$$
\delta^a + \delta^b = \underbrace{\gamma\sigma^2\tau^{\text{hold}}}_{\text{fear}} + \underbrace{\tfrac{2}{\gamma}\ln\!\big(1+\tfrac{\gamma}{k}\big)}_{\text{greed}} + \underbrace{2\,c_{\text{reg}}\bar S\,\tau^{\text{hold}}}_{\text{rent}}.
\tag{22.3}
$$

The kink is the useful part. A flat dealer widens both sides by the rent, because either fill opens a new position. A long dealer does not widen at all; it *skews*, because a sale shrinks a position it is already paying rent on. That is a dealer subletting a room it already rents: it will happily take less for the sublet. It is also why a desk running near its balance-sheet limit quotes a sharp offer and a sullen bid.

**Breakeven holding period.** Principal market making pays only if the half bid-ask covers the rent over the hold. In bp of notional, with $c_{\text{reg}}$ in bp per year and $\tau^{\text{hold}}$ in years, the breakeven is

$$
\tau^\ast = \frac{s_{\text{ba}}/2}{c_{\text{reg}}},
\tag{22.4}
$$

where $s_{\text{ba}}$ is the bid-ask in bp of price. Hold the bond for less than $\tau^\ast$ and principal market making beats agency; hold it longer and you are an unpaid warehouse.

**Numerics** *(illustrative; hurdle $h = 12\%$, 7-calendar-day hold, ACT/365)*:

| Position | Binding constraint | $\kappa$ | $c_{\text{reg}}$ (bp/yr) | 1-week rent (bp) | Half bid-ask (bp of price) | $\tau^\ast$ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2y on-the-run Treasury, eSLR before 2026 | Leverage, $\kappa_{\text{LR}} = 5\%$ | 5.0% | 60 | 1.15 | ~0.5 | ~3 days |
| Same, after 2026-04-01 (3% + ½ × 1.5% surcharge) | Leverage | 3.75% | 45 | 0.86 | ~0.5 | ~4 days |
| 10y BBB industrial, equivalent RW 100% | Risk-based, $10.5\% \times 1.0$ | 10.5% | 126 | 2.42 | ~12.5 | ~36 days |

The table explains a decade of market structure. For the corporate bond, rent is a rounding error against a quarter-point market: the dealer can sit on it for a month. For the Treasury, rent *is* the market: three days of inventory eats the half-spread. That single inequality explains why dealers went agency in Treasuries first, why the Federal Reserve's first market-structure tool in March 2020 was a leverage-ratio exclusion (§22.4), and why the November 2025 eSLR rule was sold as relief for "Treasury market intermediation" (§22.5). The risk weight does not tell you what a Treasury costs to hold. The leverage ratio does.

> **Ways This Blows Up.** (1) *Units.* $c_{\text{reg}}$ is annual and $\tau^{\text{hold}}$ is in years; ROBO once fed a holding period of seven days into the year slot and concluded that a week in Treasuries costs 4.2% of notional, which would make every repo desk on the Street a charity. (2) *Using $q$ instead of $|q|$.* A short pays rent too, through the borrow. A signed formula says shorting a bond *releases* capital, and the optimizer gets very excited about shorts. (3) *Double counting funding.* $h$ is the excess return over funding. (4) *Gross versus net.* Leverage charges apply to gross positions and risk charges to net-of-hedge positions, so a hedged book is cheap under risk-based capital and expensive under the leverage ratio. Run both and take the max *per legal entity*, not per trade. (5) *Calendar.* $\kappa$ and $h$ are effectively higher around reporting snapshots for some dealers. Model them as calendar features, not constants, or the quarter-end in the cold open becomes an unexplained residual.

> **[SOURCE EXTRACTION]** *Schmid_Credit_Risk_Pricing_Models p.163:* "the cost of the trade will depend mainly on the funding cost of the total return payer and any regulatory capital charge incurred ... If the total return payer is a bank, it also depends on the BIS risk weight of the asset, with 20% for OECD bank debt and 100% for corporate debt."
>
> **Annotation.** Our analysis: this is (22.1) in its 2004 form. Schmid prices a total return swap as funding plus a capital charge driven by the Basel I risk weight, and the logic carries over to a dealer's inventory one for one. What changed is the *max*. In Schmid's world the risk weight was the only constraint, so a Treasury, with a zero weight, was free to hold, and corporate debt at 100% was the expensive asset. Since the leverage ratio arrived, every asset carries the floor $\kappa_{\text{LR}}$, and for low-risk assets the floor binds. The modern desk keeps Schmid's decomposition, funding plus capital times hurdle, and replaces the risk weight with $\max(\kappa_{\text{RWA}}\text{RW}, \kappa_{\text{LR}})$. One more departure: a TRS desk in 2026 also asks whether the trade is cleared, because clearing changes the counterparty term and the margin term (§22.4, §22.6).

> **Trend Watch: dealer corporate-bond inventories, 2007–2026.** *What changed:* US primary dealers stopped warehousing corporate bonds. *How big:* Federal Reserve FR 2004 data put dealer corporate holdings at a peak of roughly \$235bn in 2007, cut by about three-quarters by 2012 *(approx.; the pre-2013 series lumps corporates with other credit, so treat the peak as an upper bound)*. Average long inventories were about \$16bn in 2017. Trade press citing Crisil Coalition Greenwich analysis of FR 2004 data reports that primary dealers have averaged a **net short** position of about \$4bn in US corporate bonds so far in 2026, "the first time in at least 25 years" *(approx.; check against the NY Fed primary dealer statistics before relying on it)*. In late 2024 Coalition Greenwich already described dealers as short about \$3.8bn of IG corporates longer than five years, and the market as "agency (or at most, riskless principal)." *What it means for the desk:* the inventory function has moved to the customer: all-to-all venues, ETF creation and redemption (Chapter 20), and portfolio trades (Chapter 19). The bank dealer is now a router with a risk budget, and its $\tau^{\text{hold}}$ is measured in hours. Your liquidity model's "dealer capacity" variable should say which kind of dealer it means.

> **[SOURCE EXTRACTION]** *Dynkin_Systematic_Investing_in_Credit p.348 (n.1):* "Konstantinovsky and Phelps (2012) document the decline in US corporate bond market liquidity as dealer inventories have fallen since 2008 in response to various regulatory changes. They estimate that the inventory decline led to an 18% drop in illiquidity, which translates to approximately 13bp/year in additional transaction cost for a portfolio with 100% yearly turnover."
>
> **Annotation.** Our analysis: thirteen basis points a year is the first serious price tag anyone put on post-crisis regulation from the buy side, and it is a useful prior even now. Read the units carefully: 13bp a year *at 100% turnover*. A systematic credit strategy with 200% turnover pays twice that, and a quarterly-rebalanced factor portfolio of the kind in Chapter 9 pays perhaps half. The modern desk departs from the 2012 estimate in two ways. First, the cost did not stay with the dealer; it moved into new protocols (portfolio trades, all-to-all) whose costs are lower on average and lumpier in stress. Second, the "18% drop in illiquidity" averages over calm and stressed regimes, and §22.4 shows that the regulatory cost is convex in dealer utilization: small in calm markets, very large when balance sheets fill.

> **Desk Myth vs. Desk Reality.** *Myth:* "Post-crisis regulation killed bond-market liquidity." *Reality:* It re-priced balance sheet and moved the warehouse. By most published measures, average costs for small and mid-sized IG tickets fell over the decade as electronic venues and dealer competition (§22.2) did their work, while the cost of moving a large block in a stressed week rose *(qualitative; see the dealer-capacity evidence in §22.4)*. "Liquidity" was never one number. Regulation raised the price of the dealer's balance sheet and left the price of matching buyers to sellers alone, so every protocol that matches without warehousing grew. A desk that measures liquidity by the median ticket thinks regulation helped. A desk that measures it by the 99th-percentile block in March 2020 thinks regulation broke the market. Both are right about their own sample.

### Specification for AI Implementation

**The Spec You Hand the Robot.** *Vague version:* "minimize regulatory capital." *What ROBO built:* a desk with zero inventory, zero capital consumption, and zero revenue, which ROBO reported as a 100% improvement. *Precise version:* compute the balance-sheet rent of each position as (22.1) times the holding period, in bp of $|$notional$|$ and in dollars, with decimals for every ratio (5% is `0.05`), calendar days on ACT/365, and $\kappa$ taken as the max of the risk-based and leverage charges. Compute the breakeven holding period (22.4) from a bid-ask in bp of price. Reject negative ratios, ratios above one, non-positive holding periods, and a zero binding capital rate in the breakeven. Every block in this chapter runs in order in one interpreter; this first block defines the imports.

```python
import numpy as np
import pandas as pd

BP = 1e4  # basis points per unit of notional


def capital_rate(kappa_rwa, risk_weight, kappa_lr):
    """Binding Tier 1 per $1 of gross inventory: max(kappa_rwa * RW, kappa_lr). Decimals, not percent."""
    k_rwa, rw, k_lr = (np.asarray(v, dtype=float) for v in (kappa_rwa, risk_weight, kappa_lr))
    if np.any((k_rwa < 0) | (k_rwa > 1)) or np.any((k_lr < 0) | (k_lr > 1)):
        raise ValueError("capital ratios must be decimals in [0, 1]; 5% is 0.05, not 5")
    if np.any(rw < 0):
        raise ValueError("risk_weight must be non-negative")
    return np.maximum(k_rwa * rw, k_lr)


def regulatory_carry_bp(kappa_rwa, risk_weight, kappa_lr, hurdle, holding_days):
    """Balance-sheet rent over the holding period, in bp of |notional| (eq. 22.1 times the hold).
    hurdle: excess annual return on Tier 1 over the funding rate. holding_days: calendar days, ACT/365."""
    hd = np.asarray(holding_days, dtype=float)
    h = np.asarray(hurdle, dtype=float)
    if np.any(hd <= 0):
        raise ValueError("holding_days must be positive")
    if np.any(h < 0):
        raise ValueError("hurdle must be non-negative")
    return BP * h * capital_rate(kappa_rwa, risk_weight, kappa_lr) * hd / 365.0


def breakeven_holding_days(bid_ask_bp, hurdle, kappa_lr, kappa_rwa=0.0, risk_weight=0.0):
    """Holding period (calendar days) at which rent equals the half bid-ask (eq. 22.4)."""
    if hurdle <= 0:
        raise ValueError("hurdle must be positive")
    c_bp_per_year = BP * hurdle * capital_rate(kappa_rwa, risk_weight, kappa_lr)
    if np.any(c_bp_per_year <= 0):
        raise ValueError("binding capital rate is zero: the breakeven is infinite")
    return 365.0 * (np.asarray(bid_ask_bp, dtype=float) / 2.0) / c_bp_per_year


def carry_table(positions, kappa_rwa, kappa_lr, hurdle):
    """positions: DataFrame [bond_id, notional ($, signed), rw, holding_days]. Adds carry_bp, carry_usd."""
    need = {"bond_id", "notional", "rw", "holding_days"}
    missing = need - set(positions.columns)
    if missing:
        raise ValueError(f"missing columns: {sorted(missing)}")
    out = positions.copy()
    out["carry_bp"] = regulatory_carry_bp(kappa_rwa, out["rw"], kappa_lr, hurdle, out["holding_days"])
    out["carry_usd"] = out["notional"].abs() * out["carry_bp"] / BP   # shorts pay rent too
    return out


# Sanity checks: the numerics table of 22.1.1
ust = regulatory_carry_bp(0.105, 0.0, 0.05, 0.12, 7)         # Treasury: RW 0, leverage binds
bbb = regulatory_carry_bp(0.105, 1.0, 0.05, 0.12, 7)         # corporate: risk-based binds
ust_2026 = regulatory_carry_bp(0.105, 0.0, 0.0375, 0.12, 7)  # 3% + half of a 1.5% surcharge
assert abs(ust - 1.1507) < 1e-3 and abs(bbb - 2.4164) < 1e-3 and abs(ust_2026 - 0.8630) < 1e-3
assert abs(breakeven_holding_days(1.0, 0.12, 0.05) - 3.042) < 1e-2                  # 2y UST, 1bp wide
assert abs(breakeven_holding_days(1.0, 0.12, 0.0375) - 4.056) < 1e-2
assert abs(breakeven_holding_days(25.0, 0.12, 0.05, 0.105, 1.0) - 36.21) < 1e-1     # BBB, a quarter wide

book = pd.DataFrame({"bond_id": ["UST_2Y_OTR", "BBB_IND_2033", "BBB_IND_2033_SHORT"],
                     "notional": [1e8, 15e6, -15e6], "rw": [0.0, 1.0, 1.0], "holding_days": [7, 7, 7]})
tab = carry_table(book, kappa_rwa=0.105, kappa_lr=0.05, hurdle=0.12)
assert tab["carry_usd"].iloc[1] == tab["carry_usd"].iloc[2]      # |q|, not q
assert abs(tab["carry_usd"].iloc[0] - 11507.0) < 5.0              # $100mm of 2y, one week
try:
    regulatory_carry_bp(10.5, 1.0, 5.0, 0.12, 7)                   # percent instead of decimals
    raise AssertionError("percent inputs must be rejected")
except ValueError:
    pass
```

*Further reading for this section:* Duffie (2012), *Market Making Under the Proposed Volcker Rule*; Konstantinovsky and Phelps (2012) as summarized in Dynkin et al.; the NY Fed's primary dealer statistics (links in the Deep-Dive Resource Graph at the end of the chapter).
