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

> **Trend Watch: dealer corporate-bond inventories, 2007–2026.** *What changed:* US primary dealers stopped warehousing corporate bonds. *How big:* Federal Reserve FR 2004 data put dealer corporate holdings at a peak of roughly \$235bn in 2007, cut by about three-quarters by 2012 *(approx.; the pre-2013 series lumps corporates with other credit, so treat the peak as an upper bound)*. Average long inventories were about \$16bn in 2017. Trade press citing Crisil Coalition Greenwich analysis of FR 2004 data reports that primary dealers have averaged a **net short** position of about \$4bn in US corporate bonds so far in 2026, "the first time in at least 25 years" *(approx.; check against the NY Fed primary dealer statistics before relying on it)*. In late 2024 Coalition Greenwich was already describing dealers as net short in longer-dated IG corporates *(late-2024 figure not independently verified)*. *What it means for the desk:* the inventory function has moved to the customer: all-to-all venues, ETF creation and redemption (Chapter 20), and portfolio trades (Chapter 19). The bank dealer is now a router with a risk budget, and its $\tau^{\text{hold}}$ is measured in hours. Your liquidity model's "dealer capacity" variable should say which kind of dealer it means.

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

## 22.2 TRACE, 2002–2027: The Transparency Ledger

Information is the third thing a dealer sells, and TRACE is the rule that decides how much of it the dealer gets to keep. Mags remembers the pre-TRACE world with the fondness people reserve for wars they survived. "Back in my day the tape was the guy at the next desk who'd heard something. You priced a bond by phone and by grudge." She will also tell you, grudgingly, that the distressed desk barely noticed TRACE for its first few years, and the shelf agrees with her.

> **[SOURCE EXTRACTION]** *Moyer_Distressed_Debt_Analysis p.416 (n.62):* "The National Association of Securities Dealers requires that trades in specified bonds, usually larger issue sizes or of large capitalization firms, be electronically recorded by broker-dealers into the Trade Reporting and Comparison Entry Source (TRACE). However, most of the securities required to be posted do not constitute distressed securities."
>
> **Annotation.** Our analysis: two things are dated in this footnote, and both are useful. The acronym is wrong (TRACE is the Trade Reporting and Compliance Engine), which tells you how much attention a distressed investor of the mid-2000s paid to it. More importantly, the coverage claim was true when Moyer wrote it: dissemination was phased in by issue size and rating, and immediate dissemination of *all* public TRACE-eligible corporate bonds began only on 2006-01-09 (FINRA TRACE FactBook 2025). For a systematic desk, this means any distressed-bond liquidity series that starts before 2006 has a selection problem baked in: the bonds you can see are the large, liquid ones, which is exactly the sample that does not default. Start the panel in 2006, or carry a dissemination-phase flag.

The ledger since then, as a quant needs it, is a list of dates on which the information set changed. Table 22.1 below is that list. The academic verdict on the original 2002–2006 rollout is unusually unanimous on costs and unusually split on volume. Bessembinder, Maxwell and Venkataraman (2006), Edwards, Harris and Piwowar (2007), and Goldstein, Hotchkiss and Sirri (2007) all found that trading costs fell for bonds that became transparent; the last of these was a literal controlled experiment on a set of BBB bonds, the regulatory event study in its purest form (§22.8). Asquith, Covert and Pathak (NBER w19417, 2013, revised 2019) found that costs fell across all bond types, with high-yield costs down 22.9%, and estimated total savings of about \$600mm a year. They also found that "trading activity does not increase and, by one measure, decreases," and that by that measure high-yield activity fell 71.1%. Transparency lowered the average price of liquidity and reduced the quantity dealers were willing to supply at the margin. That is not a paradox. It is what happens when you tax the dealer's information, and the derivation below shows where the tax lands.

> **[SOURCE EXTRACTION]** *Ben_Dor_Quantitative_Credit_Portfolio_Management p.162 (n.3):* "Trade Reporting and Compliance Engine (TRACE) ... disseminates trade-by-trade corporate bond execution information within 15 minutes to all market participants. At this time, TRACE data are censored at \$5 million for investment grade and \$1 million for high-yield securities."
>
> **Annotation.** Our analysis: "at this time" was 2010, and the striking fact for a 2026 desk is that both numbers in the sentence are still the rule. FINRA Regulatory Notice 25-17 (2025-12-04) retained the 15-minute outer limit and restated the caps: investment-grade trades above \$5mm print as "5MM+" and non-investment-grade trades above \$1mm as "1MM+," with uncapped sizes released in the Historic Corporate Bond Data Set six months after quarter-end. Fifteen years of electronification, two serious attempts to change the parameters (one from each direction, both in the case study below), and the market is still running on Ben Dor's footnote. When a parameter survives that much pressure from both sides, it is an equilibrium, and an equilibrium can be priced.

### 22.2.1 Derivation: the reporting delay is an option the block dealer holds

Work under $\mathbb{P}$ with Kyle-style linear impact (§18.3): once the market learns of a signed block of size $Q$, the mid moves against the dealer by $\lambda Q$, where $\lambda$ is impact per unit of size the market *infers*. A dealer buys a block of $Q$ (\$mm) at $t = 0$, earning a concession of $\tfrac{s_B}{2}$ (bp of price) per unit, and works it out linearly over an unwind time $T_u$, so its remaining inventory at $t$ is $Q(1 - t/T_u)$. The print becomes public after a delay $\Delta$: fifteen minutes today, one minute under the rule that died, end of day for on-the-run Treasuries.

The leak cost is the impact times the inventory still held at publication:

$$
\text{Leak}(\Delta) = \lambda Q \cdot Q\Big(1 - \frac{\Delta}{T_u}\Big)^+ .
$$

The inventory-risk cost is the mean-variance penalty on the unwind. With mid volatility $\sigma$ (bp per $\sqrt{\text{minute}}$), the P&L variance of a linear unwind is $\int_0^{T_u}\sigma^2 Q^2 (1 - t/T_u)^2\,dt = \sigma^2 Q^2 T_u/3$, so the penalty is $\tfrac12\gamma\sigma^2Q^2T_u/3$. Expected utility-adjusted P&L is

$$
\Pi(\Delta) = \frac{s_B}{2}\,Q - \lambda Q^2\Big(1-\frac{\Delta}{T_u}\Big)^+ - \frac{\gamma\sigma^2 Q^2 T_u}{6}.
\tag{22.5}
$$

Setting $\Pi = 0$ gives the competitive block half-spread and its sensitivity to the delay:

$$
\frac{s_B^\ast}{2}(\Delta) = \lambda Q\Big(1-\frac{\Delta}{T_u}\Big)^+ + \frac{\gamma\sigma^2 Q\,T_u}{6},
\qquad
\frac{\partial s_B^\ast}{\partial \Delta} = -\frac{2\lambda Q}{T_u} \quad (\Delta < T_u).
\tag{22.6}
$$

Three readings fall out. **Shorter delay, wider block spread**, with the effect proportional to block size $Q$. **The effect is concentrated where $\Delta$ and $T_u$ are comparable.** A riskless-principal trade, matched before it prints ($T_u \le \Delta$), pays no leak at fifteen minutes or at one; a block worked over three days barely notices the difference between one minute and fifteen. The trades that care are the risk-transfer blocks worked out in an hour or two through ETFs, CDS, and portfolio trades. **To protect a multi-day unwind, the delay must be measured in days**, which is why the 2019 block proposal paired higher caps with a 48-hour delay.

*Worked example (illustrative):* $\lambda = 0.5$bp per \$mm, $Q = 15$, $T_u = 120$ minutes, $\sigma = 2.5$bp$/\sqrt{\text{min}}$ (about 50bp of price a day, a 10-year BBB), $\gamma = 0.001$ per bp·\$mm. The inventory term is $0.001 \times 6.25 \times 15 \times 120/6 = 1.875$bp. At $\Delta = 15$ the leak term is $7.5 \times 0.875 = 6.56$bp, for a half-spread of 8.44bp; at $\Delta = 1$ it is $7.5 \times 0.992 = 7.44$bp, for 9.31bp. The one-minute rule would have widened this block by about 0.9bp, roughly 10%, which on a desk printing a few thousand such blocks a year is a line item someone would write a comment letter about.

### 22.2.2 Derivation: what hides behind "5MM+"

Printed size is $\tilde Q = \min(Q, C)$ plus a flag, with $C = 5$ (\$mm, IG) or $C = 1$ (HY). The market cannot see $Q$ above the cap, so it updates on $\mathbb{E}[Q \mid Q > C]$. Suppose sizes above the cap are Pareto with tail index $\alpha > 1$: $\mathbb{P}(Q > x \mid Q > C) = (C/x)^{\alpha}$ for $x \ge C$. Then

$$
\mathbb{E}[Q \mid Q > C] = \int_C^\infty x\,\frac{\alpha C^\alpha}{x^{\alpha+1}}\,dx = \frac{\alpha}{\alpha - 1}\,C \equiv m\,C,
\qquad
\alpha = \frac{m}{m-1}.
\tag{22.7}
$$

Every capped print therefore moves the market by the same $\lambda m C$, whatever its true size. Two consequences follow. The cap **pools** blocks: a \$25mm block is subsidized (the market infers less than the truth), and a \$6mm block just over the cap is taxed (the market infers more). And the dealer that did the trade knows $Q$, so it holds an information edge of $\lambda(Q - mC)$ until the uncapped historic file appears six months after quarter-end.

The shelf gives us $m$ directly, which is a pleasing accident.

> **[SOURCE EXTRACTION]** *Ben_Dor_Quantitative_Credit_Portfolio_Management p.364 (n.8):* "TRACE truncates the sizes of large transactions at \$1 million and \$5 million for high-yield and investment-grade bonds, respectively ... Alternative transaction caps can be imputed based on equating the sum of individual trades with the aggregate volume figures reported by TRACE. This procedure yields higher transaction limits of \$4 million and \$12.5 million"
>
> **Annotation.** Our analysis: Ben Dor and coauthors used the imputed caps to fix a volume series. We can use them to back out a tail index. Matching the sum of trades to aggregate volume is exactly estimating $\mathbb{E}[Q \mid Q > C]$, so $m_{\text{IG}} = 12.5/5 = 2.5$ and $m_{\text{HY}} = 4/1 = 4$. By (22.7) that gives $\alpha_{\text{IG}} = 5/3 \approx 1.67$ and $\alpha_{\text{HY}} = 4/3 \approx 1.33$. Both are below 2, so the variance of block size above the cap does not exist. That is why averaging capped sizes produces garbage, and why the median capped IG block ($C \cdot 2^{1/\alpha} \approx$ \$7.6mm) sits so far below the mean (\$12.5mm). The modern desk departs from the footnote in one respect: estimate $\alpha$ from the uncapped historic file, by rating bucket and year, rather than from a single 2010-era aggregate match. Portfolio trading has fattened the tail since then.

### 22.2.3 Case Study: The One-Minute Rule That Died (2022–2025), and the Block Pilot That Never Lived (2019)

*The approach from transparency.* FINRA proposed cutting the TRACE reporting outer limit from fifteen minutes to one in 2022 (Regulatory Notice 22-17). The formal filing, SR-FINRA-2024-004, followed in January 2024 and would "reduce the 15-minute TRACE reporting timeframe to one minute," with "exceptions for member firms with de minimis reporting activity and for manual trades." After an amendment, the SEC approved it in 2024 *(the approval order is dated in the autumn; check the exact date on the filing page)*. Then, on 2025-12-04, Regulatory Notice 25-17: "FINRA is not moving forward with its proposal to reduce the 15-minute TRACE reporting outer limit to one minute." The stated reason was that "firms raised additional concerns and questions in connection with aspects of the approved reduced reporting time regime," and the notice added the line every quant should frame: "While the Securities and Exchange Commission approved these amendments, they have not taken effect."

*The approach from size.* In 2019, FINRA Regulatory Notice 19-12 sought comment on a pilot, recommended by the SEC's Fixed Income Market Structure Advisory Committee, that would have raised the caps to \$10mm (IG) and \$5mm (HY) while delaying dissemination of trades above the caps by 48 hours. Some commenters warned that more size transparency would make dealers "even more reluctant to position bonds." The pilot was not adopted; the caps in Notice 25-17 are still \$5mm and \$1mm.

*What the model says happened.* Equation (22.6) says the one-minute rule taxed exactly one population: blocks unwound in an hour or two. The auto-ex RFQ engines that answer most tickets are riskless or near-riskless ($T_u \le \Delta$) and were indifferent. The block desks were not, and the manual-trade exception showed that FINRA knew it. The 2019 pilot attacked from the other side: more size information (a tax on the dealer) bought with a 48-hour delay (a subsidy sized to multi-day unwinds). Each proposal moved one parameter in the transparency advocates' favor and needed a compensating move in the block dealers' favor. Neither got one, and fifteen minutes and \$5mm/\$1mm survived.

*How a systematic desk would have handled it.* Carry a regime flag for every rule from the day it is *proposed*, not just the day it takes effect, because quoting behavior can move on the approval. Price blocks with (22.6) under both regimes and keep the switch ready. And when the rule died, record the non-event: 2025-12-04 is the best placebo date in this book, a rule that was approved and never took effect. If your event study (§22.8) finds a liquidity effect on that date, your event study is broken.

> **Poker Table.** Ines replays the cold open as a hand history. "We buy fifteen million. The print shows at minute fifteen as '5MM+ sell,' and the table assumes twelve and a half, not fifteen, so the cap just hid two and a half million of our size, worth about a basis point and a quarter of impact *(illustrative, at $\lambda = 0.5$bp per \$mm)*. By minute fifteen we've worked out an eighth of it. Markouts: flat at five minutes, down 4bp at thirty, down 6 at the close *(illustrative)*. Under a one-minute rule the thirty-minute markout comes at minute one, before we've sold anything. Same hand, worse position at the table. That's why the block desks folded the one-minute rule, and why nobody at this table will ever vote to lower the cap."

> **Trend Watch: TRACE and adjacent reporting regimes as a table of structural breaks (Table 22.1).** *What changed:* the information set, about once a year. *Sources:* FINRA TRACE FactBook 2025; FINRA Regulatory Notices 22-12, 25-17, 26-16; SEC releases as noted; dates marked *approx.* rest on secondary sources.
>
> | Effective | Change | What breaks in your data |
> | :--- | :--- | :--- |
> | 2002-07 | TRACE dissemination begins, phased by size and rating | Pre-2006 samples overweight large, liquid bonds |
> | 2006-01-09 | Immediate dissemination of all public TRACE-eligible corporates | Coverage break in any distressed liquidity series |
> | 2017-07-10 | Treasuries reportable (regulatory use only) | Treasury data exist from here, but not publicly |
> | 2022-02-14 | SBSR public dissemination of security-based swaps, including single-name CDS *(approx.; trade press)* | Single-name CDS prints become observable (§22.6) |
> | 2022-09-01 | Covered depository institutions report Treasury trades | Treasury coverage jumps |
> | 2023-05-15 | Portfolio-trade modifier mandatory (≥10 issues, single basket price) | PT prints separable; "price" of a PT line is not a bond-level price |
> | 2024-03-25 | End-of-day dissemination of individual on-the-run nominal Treasury trades *(approx.; FINRA Rule 6750 materials)* | Public Treasury trade data begin |
> | 2024-05-28 | T+1 settlement for corporates (§22.3) | Settlement-date fields shift by a day |
> | 2025-09-16 | One-minute reporting rescinded (SEC approved the rescission on 2025-09-16; FINRA announced it on 2025-12-04; the 2024 approval never took effect) | Nothing. Use it as a placebo |
> | 2026-06-08 | Optional aggregate allocation reports (Rule 6730.08) for dual BD/IA firms | Print counts fall for the same economic volume |
> | 2026-08-31 | Affiliate indicator extended to member affiliates, voluntary | Duplicate affiliate prints begin to be flagged |
> | 2027-08-02 | Affiliate indicator mandatory | Volume series de-inflates; one June 2026 industry estimate put duplicate affiliate prints at up to 8% of HG TRACE volume *(approx.)* |
>
> *What it means for the desk:* a liquidity feature built on raw TRACE volume from 2020 to 2027 crosses at least four definitional breaks. Volume did not change on those dates; the meaning of a print did.

> **Ways This Blows Up.** (1) *A liquidity model fit on 2020–2026 volume* straddles the PT modifier and the allocation-report change, so the fitted "trend in liquidity" is partly a trend in reporting conventions. (2) *Averaging capped sizes at the cap* understates IG block volume by a factor of $m = 2.5$ on the capped share; averaging them at \$12.5mm is right on average and wrong for every individual trade. (3) *Fitting $\alpha$ on the live feed* is impossible, since the live feed is censored by construction; use the historic file. (4) *PT prints as bond prices.* A portfolio-trade line carries a basket-level price allocated across bonds. Feed those prints to a bond-level fair-value model and it learns the dealer's allocation scheme. (5) *Setting `one_minute_rule = True` from the approval date* because the approval was in the news: the rule was approved and never took effect.

### Specification for AI Implementation (TRACE regime layer)

**The Spec You Hand the Robot.** *Vague version:* "clean TRACE and flag the regime changes." *What ROBO built:* a flag for every FINRA notice ever published, all of them set from the publication date, including a one-minute flag that switched on in 2024 and never switched off. *Precise version:* implement the block half-spread (22.6) with the positive-part guard, the censored-size impact and tail index (22.7), and a regime-flag layer driven by one dated table (`REGIME_DATES`) that every other chapter imports. Inputs: `trade_dt` timezone-aware (reject naive timestamps), `bond_id` (str, never a made-up CUSIP), `size_mm` as disseminated (\$mm), `side`, `price`, `rating_bucket` in {"IG", "HY"}. Flags compare the New York *calendar date* of the trade with the effective date. `one_minute_rule` is always False. Units are bp of price, \$mm, and minutes.

```python
def block_half_spread(lam, Q, delay, unwind_time, gamma, sigma, inferred_size=None):
    """Zero-profit block half-spread, bp of price (eq. 22.6). lam: bp per $mm the market infers;
    Q: true block size, $mm; delay, unwind_time: minutes; sigma: bp per sqrt(minute); gamma: per bp*$mm.
    inferred_size: what the market believes Q is (defaults to Q; use the censored mean above the cap)."""
    if Q <= 0 or unwind_time <= 0 or min(delay, lam, gamma, sigma) < 0:
        raise ValueError("need Q > 0, unwind_time > 0, and non-negative delay, lam, gamma, sigma")
    q_hat = Q if inferred_size is None else inferred_size
    leak = max(0.0, 1.0 - delay / unwind_time)                 # positive-part guard
    return lam * q_hat * leak + gamma * sigma**2 * Q * unwind_time / 6.0


def pareto_alpha_from_imputed_mean(cap, imputed_mean):
    """Tail index from the mean size above the cap (eq. 22.7): alpha = m / (m - 1), m = mean / cap."""
    m = imputed_mean / cap
    if m <= 1.0:
        raise ValueError("imputed mean must exceed the cap")
    return m / (m - 1.0)


def censored_impact(lam, cap, alpha):
    """Impact of any capped print: lam * alpha / (alpha - 1) * cap."""
    if alpha <= 1.0:
        raise ValueError("alpha must exceed 1 for a finite conditional mean")
    return lam * alpha / (alpha - 1.0) * cap


REGIME_DATES = {                      # New York calendar dates; imported by every later chapter
    "sbsr_public": "2022-02-14",
    "pt_modifier_live": "2023-05-15",
    "t_plus_1": "2024-05-28",
    "alloc_reports_live": "2026-06-08",
    "affiliate_ind_voluntary": "2026-08-31",
    "affiliate_ind_mandatory": "2027-08-02",
}
DISSEMINATION_CAP_MM = {"IG": 5.0, "HY": 1.0}


def trace_regime_flags(trades):
    """Add one boolean column per regime, plus size_capped and dup_risk. Rejects naive timestamps."""
    need = {"trade_dt", "bond_id", "size_mm", "side", "price", "rating_bucket"}
    missing = need - set(trades.columns)
    if missing:
        raise ValueError(f"missing columns: {sorted(missing)}")
    if not isinstance(trades["trade_dt"].dtype, pd.DatetimeTZDtype):
        raise ValueError("trade_dt must be timezone-aware (America/New_York)")
    if not trades["rating_bucket"].isin(list(DISSEMINATION_CAP_MM)).all():
        raise ValueError("rating_bucket must be 'IG' or 'HY'")
    out = trades.copy()
    ny_date = out["trade_dt"].dt.tz_convert("America/New_York").dt.tz_localize(None).dt.normalize()
    for flag, d in REGIME_DATES.items():
        out[flag] = ny_date >= pd.Timestamp(d)
    out["one_minute_rule"] = False    # approved by the SEC in 2024, never effective: FINRA Notice 25-17
    out["size_capped"] = out["size_mm"] >= out["rating_bucket"].map(DISSEMINATION_CAP_MM)
    out["dup_risk"] = ~out["affiliate_ind_mandatory"]    # affiliate duplicates not reliably flagged yet
    return out


# Sanity checks
lam, gam, sig = 0.5, 0.001, 2.5
s15 = block_half_spread(lam, 15.0, 15.0, 120.0, gam, sig)
s1 = block_half_spread(lam, 15.0, 1.0, 120.0, gam, sig)
s48h = block_half_spread(lam, 15.0, 48 * 60.0, 120.0, gam, sig)
assert abs(s15 - 8.4375) < 1e-9 and abs(s1 - 9.3125) < 1e-9          # worked example, 22.2.1
assert abs(s48h - gam * sig**2 * 15.0 * 120.0 / 6.0) < 1e-12          # delay >= unwind: inventory only
path = [block_half_spread(lam, 15.0, d, 120.0, gam, sig) for d in np.linspace(0.0, 240.0, 49)]
assert np.all(np.diff(path) <= 1e-12)                                  # non-increasing in the delay

alpha_ig = pareto_alpha_from_imputed_mean(5.0, 12.5)                   # Ben Dor p.364 imputed caps
alpha_hy = pareto_alpha_from_imputed_mean(1.0, 4.0)
assert abs(alpha_ig - 5.0 / 3.0) < 1e-12 and abs(alpha_hy - 4.0 / 3.0) < 1e-12
assert abs(censored_impact(lam, 5.0, alpha_ig) - lam * 12.5) < 1e-12
rng = np.random.default_rng(22)
capped_ig = 5.0 * (1.0 + rng.pareto(alpha_ig, 200_000))               # classical Pareto above $5mm
assert abs(np.median(capped_ig) - 5.0 * 2.0 ** (1.0 / alpha_ig)) < 0.05   # median ~ $7.6mm, mean $12.5mm

trades = pd.DataFrame({
    "trade_dt": pd.to_datetime(["2023-05-12 15:41", "2023-05-15 09:30", "2023-05-16 10:05"])
                  .tz_localize("America/New_York"),
    "bond_id": ["BBB_IND_2033", "B2_PKG_2029", "BBB_IND_2033"],
    "size_mm": [2.0, 1.0, 5.0], "side": ["S", "B", "S"], "price": [97.25, 91.10, 96.90],
    "rating_bucket": ["IG", "HY", "IG"],
})
flags = trace_regime_flags(trades)
flag_cols = list(REGIME_DATES) + ["one_minute_rule"]
assert [c for c in flag_cols if flags[c].iloc[0] != flags[c].iloc[-1]] == ["pt_modifier_live"]
assert flags["size_capped"].tolist() == [False, True, True] and flags["dup_risk"].all()
try:
    trace_regime_flags(trades.assign(trade_dt=trades["trade_dt"].dt.tz_localize(None)))
    raise AssertionError("naive timestamps must be rejected")
except ValueError:
    pass
```

*Further reading for this section:* Asquith, Covert and Pathak (2013/2019); Goldstein, Hotchkiss and Sirri (2007); FINRA Regulatory Notices 19-12, 22-12, 22-17, 25-17 and 26-16; FINRA Rule 6730 (links at the end of the chapter).

## 22.3 T+1 and the Settlement Clock

Time is the second thing a dealer sells, and the settlement cycle is the most literal clock in the business: the number of days between the handshake and the money. The SEC adopted T+1 on 2023-02-15, moving most broker-dealer securities transactions from two business days to one, and the industry switched on 2024-05-28, the Tuesday after Memorial Day. The rule also required same-day affirmation "as soon as technologically practicable and no later than the end of trade date," made investment advisers keep records of allocations, confirmations and affirmations, and required central matching service providers to adopt straight-through-processing policies. The SEC chair at the time said it "will reduce latency, lower risk, and promote efficiency." Treasuries were never part of this: as exempt securities they already settled T+1 by market convention.

To a restructuring banker, a settlement cycle looks like plumbing. To a risk manager it is a horizon, and horizons are where square roots live.

### 22.3.1 Derivation: why T+1 cut margin by about a quarter

A clearing agency's margin covers the loss on a member's open positions between trade and close-out. If the member defaults, the clearing agency is exposed from the trade until settlement, and then for however long it takes to liquidate, so the horizon is $H = T_{\text{settle}} + T_{\text{co}}$ days. Under $\mathbb{P}$, with daily price changes independent and of volatility $\sigma$, the loss over $H$ days has standard deviation $\sigma\sqrt{H}$. A value-at-risk-style margin at a fixed confidence level scales the same way, $\text{IM} = z_{\alpha}\,\sigma\sqrt{H}\cdot|\text{position}|$. The confidence multiplier, the volatility, and the position all cancel in the ratio:

$$
\frac{\text{IM}_{T+1}}{\text{IM}_{T+2}} = \sqrt{\frac{1 + T_{\text{co}}}{2 + T_{\text{co}}}} =
\begin{cases} 0.707 & (T_{\text{co}} = 0):\ -29\% \\ 0.816 & (T_{\text{co}} = 1):\ -18\% \end{cases}
\tag{22.8}
$$

The two brackets correspond to whether liquidation is instantaneous or takes a day. Now the published numbers. According to the DTCC/SIFMA/ICI after-action reporting, NSCC's clearing fund fell from \$12.8bn under T+2 to \$9.1bn in an early snapshot (−29%) and to \$9.8bn on a three-month average basis (−23%) *(approx.; DTCC, 2024)*. Both land inside the bracket, with the more durable average close to the middle. A one-line derivation, a published number, and an honest fit rather than a cherry-pick: the empirical ratio is in the range the theory allows, and it would have been embarrassing if it weren't.

*Error-prone spots.* NSCC margin has a volatility component plus add-ons (mark-to-market, liquidity, concentration, backtesting) that do not scale with $\sqrt{H}$, so apply (22.8) to the volatility component only. The square root also assumes independent daily changes. In a trending, autocorrelated market the horizon effect is closer to linear, so a T+1 saving computed in calm data overstates the saving in a crisis. The clock helps least when you need it most, a theme that will recur.

### 22.3.2 Fails, and the identity hiding in the fails charge

A shorter cycle shrinks the *window* of counterparty exposure and raises the *probability* of a fail, because there is less time to locate the bond. The cost of failing has a clean identity. A seller who fails to deliver does not receive the cash until it does, so it forgoes interest at roughly the short rate $r^{\text{ref}}$. The Treasury Market Practices Group (TMPG) fails charge adds $\max(0,\ 3\% - r^{\text{ref}})$ per year, accrued as $\text{Par}\times\text{rate}\times\text{days}/360$. Adding the two, and taking the reference rate as the seller's reinvestment rate:

$$
\text{cost of failing (per year)} = r^{\text{ref}} + \max\!\big(0,\ 3\% - r^{\text{ref}}\big) = \max\!\big(r^{\text{ref}},\ 3\%\big).
\tag{22.9}
$$

The charge is a floor on the cost of failing. Above 3% it is zero and the market's own interest rate disciplines fails. Below 3%, without it, failing at zero rates is free, which is exactly what happened in 2008–2009. Check the TMPG's current definition of the reference rate before using (22.9) in production; the structure is what matters here.

> **[SOURCE EXTRACTION]** *Veronesi_Fixed_Income_Securities p.57:* "Starting May 1, 2009, the Federal Reserve imposed a penalty charge of 3% over its Fed funds rate for failing to deliver the bonds in the repo transactions the Federal Reserve conducts daily in its open market operations." And: "on May 1, 2009, the repo rate for some Treasury securities that were on special became negative."
>
> **Annotation.** Our analysis: Veronesi's textbook records the moment a fails penalty changed the sign of an interest rate. With the policy rate near zero, a bond on special could not trade below a 0% repo rate as long as failing was free; once failing cost 3%, lenders of cash would accept a negative repo rate to get the bond rather than fail. (The Fed's own penalty in the quotation was set relative to the fed funds rate; the industry fails charge in (22.9) is stated as 3% *minus* a reference rate. Both put a floor under the cost of failing.) The 2026 desk departs from 2009 in the regime: with reference rates above 3% for most of 2023–2025 *(approx.)*, the charge has been near zero and fails have been disciplined by carry, not by penalty. The day rates fall back toward zero, the charge wakes up, specials can again go negative, and any short-financing model calibrated on 2023–2025 will be wrong in exactly that direction.

The 2024 fail data matched the identity's prediction of "not much changes": the continuous net settlement (CNS) fail rate was 1.90% on the first T+1 day against a May 2024 T+2 average of 2.01%, and averaged 2.12% in July 2024 *(approx.; DTCC after-action reporting)*. The cost moved to the operations desk, which now affirms on trade date, and to the people whose other legs did not move: a non-US buyer funding in FX that settles on a T+2 spot convention must pre-fund or trade FX for same-day settlement; an ETF authorized participant matching creation baskets against bonds settling T+1 runs a funding gap whenever the fund's own cycle differs (Chapter 20); and a loan trade still settles in days to weeks, so a CLO that sells bonds to buy loans is short cash for the gap (Chapter 21). The EU and UK plan their move to T+1 for 2027-10-11 *(ESMA and FCA announcements; approx.)*, which will move the FX-mismatch problem from New York to London.

### 22.3.3 Case Study: May 28–29, 2024, the Weekend the Clock Moved

*Setup.* Monday 2024-05-27 was Memorial Day, so T+2 trades from Friday 2024-05-24 settled on Wednesday 2024-05-29 under the old cycle, and so did the first T+1 trades from Tuesday the 28th. Wednesday was therefore a "double settlement" day, with two days of trades settling together. Affirmation had been the industry's worry: only about 73% of transactions were affirmed by the DTC cutoff at end-January 2024.

*What happened.* On 2024-05-29, 94.55% of transactions were affirmed by the 9:00 p.m. ET DTC cutoff. The CNS fail rate was 1.90% on the first T+1 day, against a May 2024 T+2 average of 2.01%. NSCC's clearing fund fell by \$3.0bn (23%) on a three-month average basis *(all approx.; DTCC/SIFMA/ICI after-action reporting, 2024)*. Nothing broke, and the most interesting number on the day was a rise of more than 20 points in affirmation rates in four months, achieved because there was a date. Theo recognized the mechanism at once: nothing gets a borrower's reporting package delivered on time like a covenant with a hard test date.

*How a systematic desk would have handled it.* Flag `t_plus_1` from 2024-05-28 (Table 22.1) and shift every settlement-date field in the training data; a carry or accrual calculation that uses a settlement offset of two days after that date is off by one day of accrual on every trade. Expect lower clearing-fund calls for broker-dealer affiliates and slightly higher fail *probabilities* for hard-to-borrow shorts. And, most usefully, treat the double-settlement day as a known liquidity-supply shock in the event-study calendar (§22.8), not as noise.

### Specification for AI Implementation (settlement clock)

**The Spec You Hand the Robot.** *Vague version:* "estimate the margin saving from T+1." *What ROBO built:* the ratio $1/2$, because one day is half of two days, and a report claiming margin had halved. *Precise version:* implement (22.8) as `margin_ratio(t_old, t_new, closeout_days)` with the square root applied to the horizon *including* close-out, reject negative day counts, and check that DTCC's published ratios fall inside the $T_{\text{co}} \in \{0, 1\}$ bracket. Implement (22.9) returning both the total cost of failing and the charge, as annual decimals.

```python
from math import erf, exp, pi, sqrt


def margin_ratio(t_old, t_new, closeout_days):
    """IM_new / IM_old = sqrt((t_new + closeout) / (t_old + closeout)) for the volatility component (eq. 22.8)."""
    if min(t_old, t_new, closeout_days) < 0 or t_old + closeout_days <= 0:
        raise ValueError("day counts must be non-negative and the old horizon positive")
    return sqrt((t_new + closeout_days) / (t_old + closeout_days))


def fail_cost_annual(r_ref, floor=0.03):
    """(total annual cost of failing, fails charge) per $1 of proceeds (eq. 22.9); decimals."""
    charge = max(0.0, floor - r_ref)
    return r_ref + charge, charge


assert abs(margin_ratio(2, 1, 0) - 0.70711) < 1e-5 and abs(margin_ratio(2, 1, 1) - 0.81650) < 1e-5
dtcc = {"snapshot": 9.1 / 12.8, "three_month_avg": 9.8 / 12.8}        # NSCC clearing fund, $bn (approx.)
assert all(margin_ratio(2, 1, 0) <= v <= margin_ratio(2, 1, 1) for v in dtcc.values())
assert fail_cost_annual(0.0) == (0.03, 0.03) and fail_cost_annual(0.045) == (0.045, 0.0)
assert margin_ratio(2, 1, 0) != 0.5                                      # ROBO's linear answer
```

*Further reading for this section:* SEC press release 2023-29 (T+1 adoption); the DTCC/SIFMA/ICI T+1 after-action report (2024); TMPG best-practice materials on fails charges (title only).

## 22.4 The Treasury Clearing Mandate: Netting, Margin, and the Price of a Very Large Market

Why does a credit desk care about Treasury clearing? Three reasons, in increasing order of how much they cost when ignored. Every IG bond the desk owns is hedged with Treasuries or Treasury futures. Every bond the desk owns is financed in repo. And the same dealer balance sheet intermediates both, so when Treasury intermediation consumes the balance sheet, the corporate desk's rent goes up. March 2020 (the case study below) was a Treasury event that became a corporate bond event in about four days.

**The rule.** The SEC adopted amendments to Rule 17ad-22 on 2023-12-13. Covered clearing agencies must require their members to clear (i) all Treasury repo and reverse repo the member enters into, with exceptions for state and local governments, other clearing organizations, and inter-affiliate trades; and (ii) cash Treasury purchases and sales where the member is an interdealer broker, or between a clearing member and a registered broker-dealer or government securities dealer. Central banks, sovereigns, international financial institutions, and natural persons are exempt. At adoption the SEC chair described the Treasury market as "\$26 trillion" and said that "70 to 80 percent of the Treasury funding market is uncleared, and at least 80 percent of the cash market is uncleared." On 2025-02-25 the SEC extended the compliance dates by a year, to 2026-12-31 for cash and 2027-06-30 for repo. Trade press and an FIA paper report SEC approval of CME Securities Clearing as a second Treasury clearing house in December 2025 and of ICE in early 2026 *(approx.; check the SEC orders)*; FICC remains the incumbent.

"And done-away trades?" Theo asked, reading the Treasury Borrowing Advisory Committee's list of open issues.

"If they've been done away with," said Kaz, "why are we still clearing them?"

"Done-away means you execute with one dealer and clear through another," Theo said. "Like buying a car at one dealership and getting it serviced at a different one. Except the second one is allowed to say it's too busy."

That is the access problem in one line. A mandate is only as good as the customer's ability to reach a clearing member who will take the trade on terms that do not depend on who executed it.

### 22.4.1 Derivation: what multilateral netting buys, and when it stops

Dealer $i$ faces $N - 1$ counterparties, with signed exposure $x_{ij}$ to counterparty $j$. Assume, under $\mathbb{P}$, $x_{ij} = m + \sigma_x z_{ij}$ with $z_{ij}$ i.i.d. standard normal: $m$ is a common directional component (everyone on the same side), and $\sigma_x$ the idiosyncratic scale. Bilaterally, the dealer's gross exposure is $G_i = \sum_{j \ne i}|x_{ij}|$. Novated to a central counterparty, the exposures net to a single position $|\sum_{j \ne i} x_{ij}|$. The **netting factor** is

$$
\phi(N) = \frac{\mathbb{E}\,\big|\sum_{j\ne i} x_{ij}\big|}{\mathbb{E}\,\sum_{j\ne i} |x_{ij}|}.
$$

*No direction ($m = 0$).* The sum of $N-1$ independent $N(0, \sigma_x^2)$ is $N(0, (N-1)\sigma_x^2)$, and $\mathbb{E}|Z| = \sqrt{2/\pi}$ for a standard normal, so

$$
\phi(N) = \frac{\sqrt{N-1}\,\sigma_x\sqrt{2/\pi}}{(N-1)\,\sigma_x\sqrt{2/\pi}} = \frac{1}{\sqrt{N-1}}, \qquad \phi(25) = 0.204 .
\tag{22.10}
$$

With 25 symmetric counterparties, clearing shrinks the exposure to a fifth of its gross.

*With direction ($m \ne 0$).* The numerator is now $\mathbb{E}|(N-1)m + \sqrt{N-1}\,\sigma_x Z| \approx (N-1)|m|$ for large $N$, while the denominator is $(N-1)\,\mathbb{E}|m + \sigma_x Z|$. The netting factor converges to a floor:

$$
\phi(N) \xrightarrow[N\to\infty]{} \phi_\infty = \frac{|m|}{\mathbb{E}|m + \sigma_x Z|},
\qquad
\mathbb{E}|m + \sigma_x Z| = \sigma_x\sqrt{\tfrac{2}{\pi}}\,e^{-m^2/2\sigma_x^2} + m\,\operatorname{erf}\!\Big(\frac{m}{\sigma_x\sqrt 2}\Big).
\tag{22.11}
$$

For $m = \sigma_x$, $\phi_\infty = 0.857$: netting saves only 14%. **Netting stops helping exactly when the market is one-way**, which is the basis-trade case (every leveraged fund long cash Treasuries and short futures against the same dealers) and the March 2020 case (everyone selling). The balance sheet that clearing "creates" in calm markets disappears in the state of the world where it was supposed to help.

A back-of-envelope calibration *(illustrative)*: DTCC reported that its Sponsored Service peaked at \$2.48trn on 2025-06-30 and provided "\$1.14 trillion in balance sheet capacity" *(approx.; DTCC press release)*. Read as a netting factor, that is $\phi \approx 1 - 1.14/2.48 = 0.54$, which in (22.11) corresponds to a directional component about half the idiosyncratic scale, plausible for a market where money funds lend and hedge funds borrow.

**The mandate as a trade.** Balance sheet saved per dealer per year is $(1 - \phi)\,G\,\kappa_{\text{LR}}\,h$, using the rent of (22.1). The price is initial margin, funded at a spread $f$, plus the annual cost of the default-fund contribution, $\text{DF}$. The mandate pays when

$$
(1 - \phi)\,G\,\kappa_{\text{LR}}\,h \;>\; \text{IM}\cdot f + \text{DF}.
\tag{22.12}
$$

The left side shrinks as the market turns directional; the right side grows, because IM is procyclical. Clearing converts counterparty risk into liquidity risk, and buys back balance sheet with netting, at a price that is lowest in calm markets and highest in stress. *Error-prone spots:* done-with and done-away trades may land in different netting sets; cross-margining between FICC and CME changes IM, not $\phi$; and sponsored repo already nets at the sponsor, which is why DTCC says it clears "nearly half" of the repo the mandate covers, and why the marginal gain from the mandate is smaller than the gross numbers suggest.

### 22.4.2 Derivation: dealer capacity as a convex state variable

Duffie, Fleming, Keane, Nelson, Shachar and Van Tassel (2023), *Dealer Capacity and U.S. Treasury Market Functionality* (NY Fed Staff Report 1070), measure dealer balance-sheet utilization $U_t \in [0,1]$ from weekly FR 2004 dealer-level positions (risk-adjusted gross fixed-income positions relative to a sample-record scale). They find that yield volatility explains most of the time variation in Treasury illiquidity, but that when utilization is high, "liquidity is much worse than predicted by yield volatility alone." A stylized hinge captures the shape *(our representation, not the paper's specification)*:

$$
\text{Illiq}_t = a + b\,\sigma^{y}_t + c\,\big(U_t - U^\ast\big)^+ + \epsilon_t .
\tag{22.13}
$$

Two of their sentences pin down $c$ and $U^\ast$. "When dealer capacity utilization rises from 40% to 80%, Treasury illiquidity is estimated to increase by roughly three standard deviations beyond the level of illiquidity predicted by volatility," so if the kink lies below 40%, $c \times 0.4 = 3$ and $c = 7.5$ standard deviations per unit of utilization. "When dealer capacity utilization is 60%, Treasury illiquidity is predicted to be about two standard deviations above the level predicted by contemporaneous volatility," so $7.5\,(0.6 - U^\ast) = 2$ and $U^\ast = 1/3$, consistent with the assumption. On 2020-03-12 utilization hit its sample record of 96%, where the hinge predicts about 4.7 standard deviations of excess illiquidity. The paper reports the first principal component of Treasury illiquidity at 5.4 standard deviations above its mean that day, volatility included.

For the desk, $U_t$ is a slow state variable, not a trade trigger: it is weekly and published with a lag. Proxy it with FR 2004 positions, FICC volumes, and your own RFQ hit-rate decay, and make the liquidity-cost model of Chapter 19 convex in it. Rent (22.1) is the price of balance sheet when the balance sheet has room. The hinge is the price when it doesn't.

### 22.4.3 Case Study: The March 2020 Dash for Cash

*The setup.* Foreign official holders, leveraged basis traders, and mutual funds meeting redemptions all sold Treasuries in the same two weeks. In the language of (22.11), $m$ went from small to enormous: every counterparty was on the same side.

*The price path.* On 2020-03-12, dealer utilization reached its sample record of 96% and Treasury illiquidity hit 5.4 standard deviations above its mean (Duffie et al., 2023). The safest asset in the world became expensive to sell, and because IG bonds are hedged and financed through the same dealer balance sheets, corporate bond markets dislocated in the days that followed; corporate bond ETFs traded at deep discounts to NAV (Chapter 20).

*The policy response, as a sequence of price changes.* On 2020-03-23 the Federal Reserve established the Secondary Market Corporate Credit Facility (SMCCF), which bought US-listed corporate bond ETFs and individual bonds and "ceased purchasing eligible assets on December 31, 2020." On 2020-04-01 the Fed issued an interim final rule excluding "U.S. Treasury securities and deposits at Federal Reserve Banks" from the holding-company SLR "until March 31, 2021," which it said would "temporarily decrease tier 1 capital requirements of holding companies by approximately 2 percent in aggregate," because "liquidity conditions in Treasury markets have deteriorated rapidly." The exclusion expired on schedule. In the notation of §22.1, the Fed set $\kappa_{\text{LR}}$ to zero for Treasuries and reserves, collapsing the rent term for exactly the asset where (22.4) said rent was the whole business. It was the first time the leverage ratio was used as a market-structure tool, and the November 2025 eSLR rule (§22.5) made a milder version permanent.

*How a systematic desk would have flagged it.* Three slow signals were visible before 2020-03-12: rising Treasury volatility, rising dealer positions in the FR 2004 data, and collapsing RFQ hit rates on the desk's own Treasury and IG bids. Fed into (22.13), they put the desk on the steep side of the hinge. The trade was not a directional bet but a sizing decision: halve block sizes, widen block quotes by the convex term, and stop treating the ETF discount as an arbitrage until the balance sheet that would arbitrage it reappeared. The facilities then re-opened the warehouse. The desk that had the regime table flagged 2020-03-23 and 2020-04-01 as structural breaks, and did not train its post-crisis liquidity model on a period when the central bank was the marginal buyer.

> **Trend Watch: Treasury clearing volumes and the compliance path, 2023–2026.** *What changed:* central clearing of Treasuries went from a dealer convenience to a legal requirement with a moving date. *Path:* adopted December 2023 (cash 2025-12-31, repo 2026-06-30) → extended 2025-02-25 (cash 2026-12-31, repo 2027-06-30; margin separation enforced from 2025-09-30) → second and third clearing houses approved, CME in December 2025 and ICE in early 2026 *(approx.)* → no further delay found as of October 2026 *(check before relying on it)*. *How big:* FICC's Government Securities Division cleared a peak of \$11.8trn on 2025-06-30 (prior peak \$11.4trn on 2025-04-09), and Sponsored Service activity hit a record \$2.48trn the same day *(approx.; DTCC press releases)*. Money-market-fund FICC-cleared reverse repo rose by \$132bn (11%) to \$1.3trn in June 2026 *(approx.; OFR data via trade press)*. *What it means for the desk:* repo financing of the bond book is migrating to cleared, margined, netted structures, so your financing cost becomes a function of IM and the netting set, not just a repo rate. Model the compliance dates as structural breaks, and give each one a placebo twin in case it slips again.

### Specification for AI Implementation (netting and capacity)

**The Spec You Hand the Robot.** *Vague version:* "simulate how much clearing saves." *What ROBO built:* a simulation with $N = 2$, where netting saves nothing and ROBO recommended against clearing. *Precise version:* Monte Carlo the netting factor for $N$ counterparties with a common directional component $m$ and idiosyncratic scale $\sigma_x$; return the simulated factor, the no-direction theory $1/\sqrt{N-1}$, and the large-$N$ floor (22.11). Provide a bisection that maps an observed netting factor to the implied $m$; implement (22.12); and calibrate the hinge (22.13) from two published sentences. Seeded; at least 1,000 simulations; reject $N < 2$.

```python
def folded_normal_mean(m, s=1.0):
    """E|m + s Z| for standard normal Z (eq. 22.11)."""
    return s * sqrt(2.0 / pi) * exp(-m * m / (2.0 * s * s)) + m * erf(m / (s * sqrt(2.0)))


def netting_factor_mc(n_dealers, n_sims, seed, common_component=0.0, scale=1.0):
    if n_dealers < 2 or n_sims < 1000 or scale <= 0:
        raise ValueError("need n_dealers >= 2, n_sims >= 1000, scale > 0")
    rng = np.random.default_rng(seed)
    x = common_component + scale * rng.standard_normal((n_sims, n_dealers - 1))
    mc = np.abs(x.sum(axis=1)).mean() / np.abs(x).sum(axis=1).mean()
    m = abs(common_component)
    return {"mc": float(mc), "theory": 1.0 / sqrt(n_dealers - 1),
            "directional_floor": m / folded_normal_mean(m, scale)}


def implied_common_component(phi_target, scale=1.0, lo=1e-9, hi=50.0, tol=1e-12):
    """Directional component m at which the large-N floor equals phi_target (bisection; floor rises in m)."""
    if not 0.0 < phi_target < 1.0:
        raise ValueError("phi_target must lie in (0, 1)")
    f = lambda m: m / folded_normal_mean(m, scale) - phi_target
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        lo, hi = (lo, mid) if f(lo) * f(mid) <= 0 else (mid, hi)
        if hi - lo < tol:
            break
    return 0.5 * (lo + hi)


def mandate_net_benefit(gross, phi, kappa_lr, hurdle, im, funding_spread, default_fund_cost=0.0):
    """Left minus right side of eq. 22.12, per year, in the units of gross (e.g. $bn)."""
    if not 0.0 <= phi <= 1.0:
        raise ValueError("phi must lie in [0, 1]")
    return (1.0 - phi) * gross * kappa_lr * hurdle - (im * funding_spread + default_fund_cost)


def capacity_hinge(u_lo=0.4, u_hi=0.8, delta_sd=3.0, u_mid=0.6, level_sd=2.0):
    """Calibrate c and U* in eq. 22.13 from two statements in Duffie et al. (2023)."""
    c = delta_sd / (u_hi - u_lo)            # valid only if the kink lies below u_lo
    u_star = u_mid - level_sd / c
    if u_star > u_lo:
        raise ValueError("kink above u_lo: the two-point calibration is invalid")
    return c, u_star


nf = netting_factor_mc(25, 20_000, seed=7)
assert abs(nf["theory"] - 0.2041) < 1e-4 and abs(nf["mc"] / nf["theory"] - 1.0) < 0.02
nd = netting_factor_mc(25, 20_000, seed=7, common_component=1.0)
assert abs(nd["directional_floor"] - 0.857) < 1e-3 and abs(nd["mc"] - nd["directional_floor"]) < 0.01
m_implied = implied_common_component(1.0 - 1.14 / 2.48)                 # DTCC sponsored figures (approx.)
assert 0.4 < m_implied < 0.6
calm = mandate_net_benefit(100.0, 0.54, 0.05, 0.12, im=2.0, funding_spread=0.005, default_fund_cost=0.02)
one_way = mandate_net_benefit(100.0, 0.857, 0.05, 0.12, im=4.0, funding_spread=0.01, default_fund_cost=0.02)
assert calm > one_way                                                     # netting fades, IM rises
c_h, u_star = capacity_hinge()
assert abs(c_h - 7.5) < 1e-12 and abs(u_star - 1.0 / 3.0) < 1e-12
assert abs(c_h * max(0.96 - u_star, 0.0) - 4.70) < 0.01                  # 2020-03-12, excess over volatility
```

*Further reading for this section:* SEC press release 2023-247 (clearing mandate); Duffie et al. (2023), NY Fed Staff Report 1070; Duffie (2020), *Still the World's Safe Haven?* (Hutchins Center); Federal Reserve releases of 2020-03-23 (SMCCF) and 2020-04-01 (SLR exclusion).

## 22.5 Dealer Capital: Volcker, the Leverage Ratio, and the Endgame

Three capital rules, three different taxes. Risk-based capital taxes *risk*, the leverage ratio taxes *size*, and the Volcker Rule taxes *time*. Section 22.1 put the first two inside a max. The switching point between them is the equivalent risk weight at which they tie:

$$
\text{RW}^\dagger = \frac{\kappa_{\text{LR}}}{\kappa_{\text{RWA}}}, \qquad \text{leverage binds for } \text{RW} < \text{RW}^\dagger .
\tag{22.14}
$$

For the illustrative G-SIB of §22.1, $\text{RW}^\dagger = 0.05/0.105 = 47.6\%$ before 2026-04-01 and $0.0375/0.105 = 35.7\%$ after. Every asset below the switching point costs the same rent, whatever its risk. The 2026 eSLR rule did two things in this picture: it cut the rent on everything below the line by a quarter, and it moved the line down, so a band of short-dated, high-grade assets became risk-bound and cheaper still.

The Volcker Rule enters differently. Its market-making exemption requires inventory designed not to exceed the reasonably expected near-term demand of clients, customers, and counterparties (RENTD, in the acronym every Volcker compliance officer can say in their sleep). In the language of Chapter 18, that is a constraint $|q| \le \bar\Lambda\,\bar{Q}\,\tau^{\text{hold}}_{\max}$: inventory no larger than expected customer flow (arrival rate times average size) over a permitted horizon. It caps $\tau^{\text{hold}}$ directly, so it binds hardest exactly when customer demand on one side vanishes, in stress, which is the finding of Bao, O'Hara and Zhou (2018), *The Volcker Rule and Corporate Bond Market Making in Times of Stress* (*Journal of Financial Economics*): around rating downgrades, Volcker-affected dealers supplied less liquidity, and other dealers did not fully replace them (see the paper for magnitudes). The 2019 revision ("Volcker 2.0," adopted 2019-10-08, effective 2020-01-01) tiered compliance so that "firms with significant trading activity will have more stringent compliance requirements," while "the universe of trades that are considered prohibited proprietary trading will remain generally the same."

> **[SOURCE EXTRACTION]** *Bolder_Credit_Risk_Modelling p.329:* "The Basel IRB approach ... is a broad, formulaic, one-size-fits-all methodology for the computation of default-risk capital requirements. Its underlying assumption of portfolio invariance ... is nevertheless not particularly well suited for serious risk management and assessment."
>
> **Annotation.** Our analysis: Bolder means this as a criticism, and as risk management it is one. For a trading desk it is a specification. A rule that is "formulaic" (Bolder p.317 calls for "a simplified, formulaic approach to determining appropriate levels of regulatory capital") can be coded, which means its marginal cost can be computed before the trade, which is what (22.1) does. "Portfolio invariance" means the capital for a position does not depend on what else the bank holds, so concentration is free in regulatory terms and diversification earns no credit. Wherever the regulatory function ignores something the economic function cares about, a desk will find the gap; that is Bohn and Stein's "sometimes try to arbitrage" with a formula attached. The modern departure is that the binding constraint for market making is rarely the IRB default charge. It is the leverage ratio or the market-risk charge, and both are even more formulaic.

### 22.5.1 Case Study: The Basel III Endgame Saga, 2023–2026

*Act I: up 16%.* On 2023-07-27 the Federal Reserve, FDIC and OCC proposed standardizing credit, market, operational and CVA risk for banks with \$100bn or more of assets, which they estimated as "an aggregate 16 percent increase in common equity tier 1 capital requirements for affected bank holding companies," "principally affecting the largest and most complex banks" (the widely quoted figure of about 19% for G-SIBs comes from the agencies' impact analysis; *approx.*). For a risk-bound bond book, rent scales with the requirement: the BBB of §22.1 would go from 126bp a year to about 146bp *(illustrative)*, with larger increases for high-yield and less liquid bonds under standardized market-risk charges.

*Act II: up 9%.* On 2024-09-10 Vice Chair for Supervision Barr recommended a re-proposal that "would increase aggregate common equity tier 1 capital requirements for the G-SIBs" by 9%, would "facilitate banks' ability to use internal models" for market risk, largely carve out banks between \$100bn and \$250bn except for recognition of unrealized securities gains and losses (AOCI), and would "not adopt the proposed changes to capital requirements associated with client clearing."

*Interlude: the leverage ratio.* On 2025-11-25 the agencies finalized the eSLR rule, effective 2026-04-01 (optional from 2026-01-01). The holding-company buffer became 50% of the Method 1 G-SIB surcharge instead of a fixed 2%, and depository subsidiaries' buffer was capped at 1% ("no more than four percent" in total). Tier 1 requirements for the affected holding companies fall "by less than two percent" in aggregate, depository subsidiaries see greater reductions, and the stated aim was to reduce disincentives to "lower-risk activities, such as intermediating in U.S. Treasury markets."

*Act III: down, modestly.* On 2026-03-19 the agencies released a revised proposal implementing "the final components of the Basel III agreement," under which overall capital would "modestly decrease," and "the market risk aspect of the framework would apply only to banks with significant trading activity," with a separate Fed proposal on G-SIB surcharge measurement. Comments were due 2026-06-18. As of October 2026 it is a proposal, not a final rule *(check before relying on it)*.

*How a systematic desk would have traded it.* Not by forecasting the politics, but by pricing each act as a change in $\kappa$ and asking which inventories were risk-bound and which leverage-bound. Act I raised the rent on risk-bound inventory (HY and long-dated IG) and left Treasuries alone. The eSLR interlude cut the rent on leverage-bound inventory (Treasuries, repo, short IG) and left HY alone. A desk that priced balance sheet by asset class saw dealer appetite for each move in the predicted direction; a desk that tracked only "regulation, hawkish or dovish" saw noise. The Man research team captured the 2022 version of the same mechanism when it noted that "the new market environment of higher volatility and quantitative tightening may also have left dealers inclined to commit less of their balance sheets to bond trading" (`Man_Revolutions_in_Credit_Trading_2023 p.3`): capital is the rent, volatility is the risk, and both feed the same quote.

> **Poker Table.** "A two-year Treasury is the ante," Ines said. "You can't sit at this table without one. You hedge with them, you finance with them, your clients want them. The leverage ratio made the ante expensive, so the big stacks stopped playing small pots. The eSLR rule cut the ante by a quarter. It didn't change who's good at poker; it changed how many players can afford to sit down. Watch the number of dealers answering your Treasury RFQs. That's the tell."

> **Trend Watch: the capital-rule timeline, 2013–2026, and what each step did to dealer inventories.** Volcker final rule (December 2013; *approx.*) and the US eSLR final rule (2014, effective 2018; *approx.*): the warehouse shrinks, inventories fall about three-quarters from the 2007 peak (§22.1). Volcker 2.0 (2019-10-08; effective 2020-01-01): compliance tiering, prohibited activity "generally the same." SLR exclusion (2020-04-01 to 2021-03-31): Treasuries briefly rent-free. Basel III endgame proposal (2023-07-27, +16% CET1), Barr re-proposal outline (2024-09-10, +9% for G-SIBs), eSLR final (2025-11-25, effective 2026-04-01, holding-company Tier 1 down "less than two percent"), endgame re-proposal (2026-03-19, "modestly decrease"). Over the same span, dealer corporate inventories went from roughly \$16bn long in 2017 to net short in 2026 *(approx.; §22.1)*. *What it means for the desk:* the capital timeline is a list of dated changes in $\kappa$; put each one in the regime table with the asset classes it hits.

## 22.6 CDS: From the Index Clearing Mandate to SBSR, Rule 9j-1, and the Dealer Rule That Wasn't

If TRACE is the rule that taxed dealers' information, the swaps rules are the ones that *created* a public information set where there was none. They also explain why credit's most liquid instrument is a cleared, publicly reported index swap.

**The timeline.** On 2012-11-28 the CFTC issued its first clearing determination, covering CDX.NA.IG (3Y, 5Y, 7Y, 10Y), CDX.NA.HY (5Y), iTraxx Europe (5Y, 10Y), iTraxx Crossover (5Y) and iTraxx HiVol (5Y), together with major interest-rate swaps. Compliance began 2013-03-11 for swap dealers and active private funds, 2013-06-10 for other financial entities, and 2013-09-09 for third-party managed accounts and ERISA plans. Single-name CDS are security-based swaps under SEC jurisdiction and have never been subject to a clearing mandate; they clear because margin and capital rules make clearing cheaper. Public dissemination of security-based swap trades under Regulation SBSR began on 2022-02-14 *(approx.; trade press)*. On 2023-06-07 the SEC adopted Rule 9j-1, an antifraud and anti-manipulation rule for security-based swaps that reaches conduct "in connection with the execution, early termination, assignment or similar transfer of, or extinguishing of any rights or obligations under, a security-based swap," aimed among other things at manufactured credit events. Proposed Rule 10B-1, large position reporting for security-based swaps, was not adopted.

"Manufactured credit event," Kaz read aloud. "Where's the factory?"

"Usually in the indenture," said Mags, "next to the subsidiary that agrees to miss a coupon. Chapter 24 has the tour."

**The dealer rule that wasn't.** On 2024-02-06 the SEC adopted Rules 3a5-4 and 3a44-2, further defining when a firm trades "as a part of a regular business" and must register as a dealer, aimed at principal trading firms and some funds that provide liquidity like dealers. The SEC chair said that "Congress did not intend for registration and regulatory requirements to apply to some dealers and not to others." On 2024-11-21 the Northern District of Texas vacated the rules, and in early 2025 the SEC dropped its appeal *(per law-firm client alerts; approx.)*. Non-bank liquidity providers therefore remain outside dealer registration, with their own $\gamma$, their own $k$, and none of the bank capital rules of §22.5, which is a competitive fact as much as a regulatory one (§22.7).

### 22.6.1 Derivation: when clearing a CDS is cheaper than not

This is the one place in the chapter where the risk-neutral measure $\mathbb{Q}$ appears, because counterparty credit valuation adjustment is a price. Uncleared, a protection buyer bears CVA on the dealer and posts or receives bilateral initial margin under the uncleared-margin rules. Cleared, CVA is replaced by exposure to the clearing house's default fund, and initial margin is set by the CCP over a multi-day margin period of risk (check the CCP's current methodology). Per dollar of notional per year, clearing is cheaper when

$$
\underbrace{(1-R^{\text{cp}})\int_0^T \mathbb{E}^{\mathbb{Q}}\big[\text{EE}(t)\big]\,d\text{PD}^{\text{cp}}(t)}_{\text{CVA, annualized}} \;+\; \text{IM}^{\text{bil}}\,f \;>\; \text{IM}^{\text{CCP}}\,f + \text{DF} + \text{fee},
\tag{22.15}
$$

where $R^{\text{cp}}$ is the counterparty's recovery, $\text{EE}(t)$ the expected positive exposure, $\text{PD}^{\text{cp}}(t)$ the counterparty's cumulative risk-neutral default probability, and $f$ the funding spread on margin. The CCP side wins most for a dealer that holds the index *and* its constituents at one clearing house, because portfolio margining nets the index against the single names and lowers $\text{IM}^{\text{CCP}}$. That, plus the mandate, is why the clearing rates in the Trend Watch below differ by fifteen points. The full CVA machinery lives in Chapter 24; the inequality is all this chapter needs.

### 22.6.2 Case Study: Two Stresses, Two Instruments (Q1 2023 and April 2025)

*The data.* ISDA's analysis of DTCC swap-data-repository data, *CDS Market Dynamics: Five Years of Activity and a Record 2025* (2026), shows two stresses with mirror-image signatures. In the first quarter of 2023, during the regional-bank failures and the Credit Suisse rescue, single-name CDS activity rose 84.8% while index activity rose 4.5%. In April 2025, after the sudden increase in US tariffs, index activity rose 20.9% against its trailing average while single-name activity *fell* 20.7%. In ISDA's words, "During the 2020 pandemic and following the sudden increase in US tariffs in 2025, index CDS activity increased more than single-name CDS trading."

*The reading.* An idiosyncratic stress makes people want protection on *specific* names, so single-name volume spikes. A systematic stress makes them want a macro hedge in the most liquid instrument, so index volume spikes and single names are abandoned. The index-to-single-name volume multiple, 15.7× in 2022, 8.5× in 2023, 13.8× in 2025 and 15.1× in the first half of 2026, is therefore a stress-type classifier that did not exist before public reporting.

*How a systematic desk would have used it.* Build the multiple weekly from public SBSR and swap-data-repository prints and feed it to the hedging engine. When it falls, single-name hedges are liquid and index basis trades are risky; when it rises, hedge with the index and expect single-name CDS bid-asks to widen. In both 2023 and 2025 the signal was visible within days, and both regimes are now in the training data because the regulators made the data public.

> **Trend Watch: CDS activity and clearing, 2021–H1 2026.** *What changed:* index CDS set records while single names stayed small. *How big (ISDA, 2026; DTCC SDR data):* global CDS activity reached "a record \$41.8 trillion in 2025, surpassing the previous peak of \$38.7 trillion in 2022"; index CDS accounted for 93.3% of 2025 activity (a record \$39.0trn), while single-name activity peaked at \$3.3trn in 2023 and eased to \$2.8trn in 2025. The first half of 2026 reached \$27.4trn, up 27.8% year on year. "In 2025, 78.1% of index credit derivatives traded notional reported in the US was cleared, along with 63.1% of single-name CDS traded notional." Breadth is thin: "only 20 of 751 reference entities" averaged 10 or more trades a day in the fourth quarter of 2025. ICE Clear Credit reported record USD single-name clearing of \$2.57trn in 2025, up from \$2.17trn, and more than \$28trn of USD index *(approx.; ICE press release, 2026-01-06)*; ICE Clear Europe had ceased CDS clearing in October 2023. *What it means for the desk:* the hedge you can count on in stress is the index; the single-name hedge exists for about twenty names a day. Size single-name hedging strategies to that breadth, not to the notional headline.

## 22.7 The Regulated Venue: Consolidation, Tapes, and the Non-Bank Question

The last force is the venue itself. ICE agreed to acquire MarketAxess for \$167 a share in cash, about \$6.0bn of equity value, announced around 2026-07-30 with closing expected in the first half of 2027 (MarketAxess 8-K, Exhibit 99.1). In Europe, ESMA selected Ediphy (fairCT) as the first bond consolidated tape provider on 2025-07-03, and the UK's new bond transparency regime took effect on 2025-12-01 *(both approx.; ESMA and FCA announcements)*. On the supply side, Citadel Securities reports a 14.2% share of IG credit block risk transfer in 2026 so far and argues publicly for regulation tailored to non-bank market makers *(self-reported; trade press, 2026-10-08)*, a debate that the vacatur of the dealer rule (§22.6) left open. Each of these changes who answers an RFQ and what they see before answering, and so each belongs in the regime table.

The customer's regulation moves flow too, and a systematic desk should model it as carefully as the dealer's.

> **[SOURCE EXTRACTION]** *Blackstone_Systematic_Credit p.2:* "dynamically adjust portfolios to minimize capital charges for insurance clients under regulatory frameworks like Solvency II"
>
> **Annotation.** Our analysis: this is the buy-side mirror of (22.1). An insurer pays rent on its holdings too, through Solvency II in Europe and NAIC risk-based capital in the US, and its rent jumps at rating boundaries. Nuveen's framework makes the same point, describing the need to "limit exposure to certain sectors due to regulatory capital requirements" (`Nuveen_Multi_Asset_Credit_Quant_Framework p.5`). The flow consequence is predictable selling: fallen angels sold by insurers, CCC buckets cured by CLOs, and sector limits enforced at quarter-ends. A dealer that knows the customer's capital function knows when the customer is a forced seller, which in Ines's vocabulary is the most valuable thing at the table: an opponent who must fold. Where the modern desk departs from the asset manager's framing is in the direction of the optimization: Blackstone minimizes the client's charge, and the market maker prices the trades that minimization forces.

## 22.8 The Regulatory Event-Study Engine

Every section of this chapter ended in a date. This section turns the dates into a tool that answers the second half of the cold-open question: *did the rule change the data, or did something else?*

### 22.8.1 Derivation: difference-in-differences around an effective date

Let $y_{it}$ be an outcome for bond $i$ on business day $t$ (an effective half-spread in bp, a TRACE volume, a dealer hit rate), $D_i \in \{0,1\}$ mark the bonds the rule touches (treated), and $\text{Post}_t = \mathbf{1}\{t \ge t_0\}$ mark the dates on or after the effective date $t_0$. The two-way fixed-effects model is

$$
y_{it} = \alpha_i + \mu_t + \delta\,D_i\,\text{Post}_t + \epsilon_{it},
\tag{22.16}
$$

with $\alpha_i$ a bond effect (its permanent liquidity level), $\mu_t$ a date effect (everything that hits all bonds at once: rates, the VIX, quarter-end, the healing after the March 2023 bank stress), and $\delta$ the effect of the rule. Average each bond over the pre-window and the post-window, and take the difference $d_i = \bar y_i^{\text{post}} - \bar y_i^{\text{pre}}$. In a balanced panel, $\alpha_i$ cancels within the bond and $\bar\mu^{\text{post}} - \bar\mu^{\text{pre}}$ is common to every bond, so

$$
\hat\delta = \bar d_{\text{T}} - \bar d_{\text{C}} = \delta + \big(\bar{\Delta\epsilon}_{\text{T}} - \bar{\Delta\epsilon}_{\text{C}}\big),
\tag{22.17}
$$

which is unbiased if the treated and control groups would have moved in parallel without the rule, $\mathbb{E}[\Delta\epsilon_i \mid D_i = 1] = \mathbb{E}[\Delta\epsilon_i \mid D_i = 0]$. That parallel-trends assumption is the whole identification, and it is testable only indirectly: with pre-trend checks and with **placebo dates**, fake effective dates on which $\hat\delta$ should be zero. Errors are correlated within a bond over time, so the standard error comes from a cluster bootstrap that resamples whole bonds.

A before-and-after comparison with no control group is the regulatory version of reporting raw returns. It attributes $\bar\mu^{\text{post}} - \bar\mu^{\text{pre}}$, the market, to the rule. IDO or it didn't happen.

*Worked example.* The PT modifier went live on 2023-05-15. Treated bonds: issues that appear often in portfolio trades (index-eligible, recently issued, high PT share in 2022). Controls: matched bonds by rating, maturity, and size that rarely appear in PTs. Outcome: TRACE-measured effective half-spread. The obvious confounder is that market-wide liquidity was healing after the March 2023 stress, which pushes every bond's measured costs down at the same time; the control group absorbs it, and a naive before-and-after on the treated bonds alone would report the healing as a rule effect. Placebos: two pre-event dates, plus the best placebo in the book, 2025-12-04, when the one-minute rule was abandoned without ever having taken effect.

### Specification for AI Implementation (event-study engine)

**The Spec You Hand the Robot.** *Vague version:* "measure the effect of the new rule." *What ROBO built:* the mean of $y$ after the date minus the mean before it, on the treated bonds only, which correctly attributed the 2023 recovery in bank stocks to a FINRA reporting modifier. *Precise version:* implement (22.17) on a panel `[date (datetime64, New York calendar), bond_id (str), treated (bool), y (float)]`; the window is in business days relative to $t_0$, with the event day counted as post; use only bonds observed on both sides; return the 2×2 table of means, $\hat\delta$, and a cluster-bootstrap standard error (resample bonds within the treated and control groups, seeded); and provide `placebo(panel, dates, **kw)`. Reject panels with fewer than two treated or control bonds. Validate on a synthetic panel with a known effect and a concurrent market-wide shock.

```python
def event_study_did(panel, event_date, window=(-60, 60), n_boot=500, seed=0,
                    treated_col="treated", y_col="y"):
    """Difference-in-differences around an effective date (eq. 22.17), cluster bootstrap by bond."""
    need = {"date", "bond_id", treated_col, y_col}
    missing = need - set(panel.columns)
    if missing:
        raise ValueError(f"missing columns: {sorted(missing)}")
    t0 = np.datetime64(pd.Timestamp(event_date).date())
    rel = np.busday_count(t0, panel["date"].to_numpy().astype("datetime64[D]"))
    keep = (rel >= window[0]) & (rel <= window[1])
    df = panel.loc[keep, ["bond_id", treated_col, y_col]].copy()
    df["post"] = rel[keep] >= 0                                   # event day counts as post
    cell = df.groupby(["bond_id", treated_col, "post"])[y_col].mean().unstack("post")
    if False not in cell.columns or True not in cell.columns:
        raise ValueError("the window must contain pre and post observations")
    cell = cell.dropna()                                          # bonds seen on both sides only
    d = (cell[True] - cell[False]).to_numpy()
    tmask = cell.index.get_level_values(treated_col).to_numpy(dtype=bool)
    d_t, d_c = d[tmask], d[~tmask]
    if d_t.size < 2 or d_c.size < 2:
        raise ValueError("need at least two treated and two control bonds")
    rng = np.random.default_rng(seed)
    boots = np.array([rng.choice(d_t, d_t.size).mean() - rng.choice(d_c, d_c.size).mean()
                      for _ in range(n_boot)])
    table = pd.DataFrame({"pre": [cell[False][tmask].mean(), cell[False][~tmask].mean()],
                          "post": [cell[True][tmask].mean(), cell[True][~tmask].mean()]},
                         index=["treated", "control"])
    table["change"] = table["post"] - table["pre"]
    return {"table": table, "did": float(d_t.mean() - d_c.mean()), "se": float(boots.std(ddof=1)),
            "n_treated": int(d_t.size), "n_control": int(d_c.size)}


def placebo(panel, dates, **kwargs):
    """DiD estimate on each fake effective date; all should be near zero."""
    return pd.Series({pd.Timestamp(d): event_study_did(panel, d, **kwargs)["did"] for d in dates})


# Synthetic PT-modifier panel: +2bp on treated bonds from 2023-05-15, and a concurrent
# market-wide improvement of 3bp (the post-March-2023 healing) that a naive study would misread.
rng = np.random.default_rng(2023)
dates = pd.bdate_range("2022-10-03", "2023-09-29")
n_t = n_c = 40
ids = np.array([f"T{i:02d}" for i in range(n_t)] + [f"C{i:02d}" for i in range(n_c)])
is_t = np.r_[np.ones(n_t, dtype=bool), np.zeros(n_c, dtype=bool)]
post = np.asarray(dates >= pd.Timestamp("2023-05-15"))
fe = rng.normal(0.0, 20.0, ids.size)                                # bond-level cost, bp
market = np.cumsum(rng.normal(0.0, 0.05, dates.size)) - 3.0 * post  # market-wide cost, bp
y = (fe[None, :] + market[:, None] + rng.normal(0.0, 1.0, (dates.size, ids.size))
     + 2.0 * (post[:, None] & is_t[None, :]))
panel = pd.DataFrame({"date": np.repeat(dates.to_numpy(), ids.size), "bond_id": np.tile(ids, dates.size),
                      "treated": np.tile(is_t, dates.size), "y": y.ravel()})

res = event_study_did(panel, "2023-05-15", window=(-60, 60), n_boot=400, seed=1)
assert abs(res["did"] - 2.0) < max(4.0 * res["se"], 0.1) and res["se"] < 0.2
naive = res["table"].loc["treated", "change"]                       # before-after, no control group
assert naive < 0.0 < res["did"]                                     # naive says costs fell; they rose
plac = placebo(panel, ["2023-01-17", "2023-02-15"], window=(-40, 40), n_boot=200, seed=2)
assert (plac.abs() < 0.25).all()                                    # nothing happened on fake dates
```

## 22.9 Desk Debrief

- **A dealer sells balance sheet, time, and information, and every rule is a tax or a subsidy on one of them.** The desk does not comply with rules; it prices them, and it dates them.
- **Rent is $h\cdot\max(\kappa_{\text{RWA}}\text{RW}, \kappa_{\text{LR}})\cdot\tau^{\text{hold}}$.** A flat dealer widens both sides; a long dealer skews. For a 2-year Treasury, rent is the whole spread (breakeven hold of three to four days); for a BBB, it is a rounding error (about a month). That inequality explains why Treasuries went agency first.
- **A reporting delay is an option the block dealer holds**, worth $2\lambda Q/T_u$ of spread per unit of delay. The fifteen-minute, \$5mm/\$1mm equilibrium has survived attacks from both sides since 2019. It is priced into every block you quote.
- **Behind "5MM+" is a Pareto tail** with $\alpha \approx 1.67$ for IG and $1.33$ for HY, so block-size variance does not exist. Use the historic file, medians, and rating-specific tails; never average at the cap.
- **Square roots and floors.** T+1 cut the volatility component of margin by between $1-\sqrt{2/3}$ and $1-\sqrt{1/2}$, and DTCC's 23–29% landed inside the bracket. Netting shrinks exposure by $1/\sqrt{N-1}$ in a two-way market and by almost nothing in a one-way market, which is the only market in which you need it.
- **Dealer capacity is a hinge:** rent in calm markets, convex in stress, with the kink near a third of utilization. Make the liquidity model's dealer term a slow state variable, not a constant.
- **Capital rules are dated changes in $\kappa$.** For each one, ask which inventories are leverage-bound and which are risk-bound; the 2023–2026 endgame saga moved them in opposite directions.
- **Every effective date is a structural break, and every abandoned rule is a placebo.** No control group, no effect: IDO or it didn't happen.

### The Spec You Hand the Robot

*Vague version:* "make the models regulation-aware." *What ROBO built:* a dummy variable for every page of the Federal Register since 2002, a model with more regulatory features than bonds, and a perfect in-sample fit. *Precise version (prompt-ready):*

> Build `reg_cost_engine.py` (numpy and pandas only; every random draw seeded). (1) `regulatory_carry_bp(kappa_rwa, risk_weight, kappa_lr, hurdle, holding_days)`: $10^4\,h\,\max(\kappa_{\text{RWA}}\text{RW}, \kappa_{\text{LR}})\,\text{days}/365$, decimals only, reject ratios outside [0, 1] and non-positive days; `breakeven_holding_days` per (22.4); `carry_table` over a positions frame using $|$notional$|$. (2) `block_half_spread` per (22.6) with the positive-part guard and an optional inferred size; `pareto_alpha_from_imputed_mean` and `censored_impact` per (22.7), with $\alpha > 1$ enforced. (3) `margin_ratio` per (22.8) on the horizon including close-out; `fail_cost_annual` per (22.9). (4) `netting_factor_mc` returning simulated, theoretical ($1/\sqrt{N-1}$) and directional-floor (22.11) factors; `mandate_net_benefit` per (22.12); `capacity_hinge` calibrated from two published sentences. (5) `REGIME_DATES` as the single dated table, and `trace_regime_flags`, which rejects naive timestamps, compares New York calendar dates, keeps `one_minute_rule` False forever, and flags capped sizes by rating bucket. (6) `event_study_did` per (22.17) with a cluster bootstrap by bond, and `placebo`. Acceptance tests: the asserts in this chapter, unchanged, including: Treasury rent 1.15bp a week at 5% and 12%; margin ratios 0.7071 and 0.8165 bracketing DTCC's 0.71 and 0.77; netting factor within 2% of 0.204 at $N = 25$; a synthetic +2bp rule effect recovered within four standard errors despite a −3bp concurrent market move; placebo estimates below 0.25bp. Do not invent bond identifiers; use descriptive `bond_id` strings.

### Exercises

1. **The ante.** A 5-year on-the-run Treasury trades 0.5bp of price wide. With $h = 12\%$, compute the breakeven holding period at $\kappa_{\text{LR}} = 5\%$ and at $3.75\%$. A dealer's average holding period in Treasuries is two days. Is it a principal market maker or an agent with extra steps? *(Answer sketch: $\tau^\ast = 0.25/60$ years, about 1.5 days, and 0.25/45 years, about 2.0 days; the eSLR rule moved this dealer from losing money on the hold to breaking even.)*
2. **Pooling at the cap.** Using (22.6) and (22.7) with the IG parameters of §22.2, find the block size $Q$ at which the cap neither helps nor hurts the dealer, and show that for $C < Q < mC$ the cap *widens* the competitive block spread. Explain, as Ines would, why small-block dealers and large-block dealers lobby differently on the caps.
3. **Negative specials.** Using (22.9), show that a short seller who can either fail or borrow the bond in repo at the special rate $r^{\text{sp}}$ is indifferent when $r^{\text{sp}} = \min(0,\ r^{\text{ref}} - 3\%)$. Compute the floor for $r^{\text{ref}} = 0.25\%$ and $r^{\text{ref}} = 4\%$, and reconcile the first number with Veronesi's account of May 2009.
4. **When does netting give up?** For $m = 0.5\sigma_x$, compute $\phi(N)$ by simulation for $N \in \{5, 10, 25, 100\}$ and find the $N$ at which it is within 5% of the floor (22.11). What does that say about the benefit of adding more clearing members in a one-way market?
5. **Kaz's event date.** Kaz proposes studying the Treasury clearing mandate with an event date of 2025-12-31, "because that's the date in the release." Explain what is wrong with this, design a treated and control set and a placebo set for the actual cash compliance date (2026-12-31, or whatever it has become by the time you read this), and say what result would make you distrust your own estimate.
6. **ROBO maximizes transparency.** ROBO is told to "maximize transparency" and sets $\Delta = 0$ and $C = \infty$. Using (22.6), describe the block market it builds, which trades survive, and which protocols (Chapters 19 and 20) absorb the rest. Then cite the empirical result from Asquith, Covert and Pathak that would most worry ROBO's sponsor.

### Deep-Dive Resource Graph

**Podcasts**
- Bloomberg *Odd Lots* (Joe Weisenthal and Tracy Alloway), episodes on Treasury market plumbing, the basis trade, and the March 2020 dash for cash *(search the archive; title only)*.
- *Macro Musings* (David Beckworth), conversations on Treasury market resilience and central clearing *(title only)*.

**Practitioner Writing**
- FINRA Regulatory Notice 25-17 (2025-12-04; one-minute rule dropped, allocation reports, caps restated): https://www.finra.org/rules-guidance/notices/25-17
- FINRA Regulatory Notice 19-12 (block-size dissemination pilot): https://www.finra.org/rules-guidance/notices/19-12
- FINRA Regulatory Notice 22-12 (PT modifier): https://www.finra.org/rules-guidance/notices/22-12
- FINRA Regulatory Notice 22-17 (one-minute proposal): https://www.finra.org/rules-guidance/notices/22-17
- FINRA Regulatory Notice 26-16 (affiliate indicator): https://www.finra.org/rules-guidance/notices/26-16
- FINRA rule filing SR-FINRA-2024-004: https://www.finra.org/rules-guidance/rule-filings/sr-finra-2024-004
- SEC press release 2023-247 (Treasury clearing mandate): https://www.sec.gov/news/press-release/2023-247
- SEC press release 2023-29 (T+1 adoption): https://www.sec.gov/news/press-release/2023-29
- SEC press release 2024-14 (dealer rule): https://www.sec.gov/news/press-release/2024-14
- SEC press release 2025-43 (Treasury clearing compliance extension, 2025-02-25) *(title only)*.
- Federal Reserve, Basel III endgame proposal (2023-07-27): https://www.federalreserve.gov/newsevents/pressreleases/bcreg20230727a.htm
- Federal Reserve, Barr speech on the capital re-proposal (2024-09-10): https://www.federalreserve.gov/newsevents/speech/barr20240910a.htm
- Federal Reserve, eSLR final rule (2025-11-25): https://www.federalreserve.gov/newsevents/pressreleases/bcreg20251125b.htm
- Federal Reserve, Basel III re-proposal (2026-03-19): https://www.federalreserve.gov/newsevents/pressreleases/bcreg20260319a.htm
- Federal Reserve, SLR temporary exclusion (2020-04-01): https://www.federalreserve.gov/newsevents/pressreleases/bcreg20200401a.htm
- Federal Reserve, Volcker Rule revisions (2019-10-08): https://www.federalreserve.gov/newsevents/pressreleases/bcreg20191008a.htm
- Federal Reserve, Secondary Market Corporate Credit Facility: https://www.federalreserve.gov/monetarypolicy/smccf.htm
- CFTC press release 6429-12 (first swap clearing determination, 2012-11-28): https://www.cftc.gov/PressRoom/PressReleases/6429-12
- ISDA research portal (including *CDS Market Dynamics: Five Years of Activity and a Record 2025*): https://www.isda.org/category/research/
- ESMA, consolidated tape providers: https://www.esma.europa.eu/esmas-activities/markets-and-infrastructure/consolidated-tape-providers
- MarketAxess 8-K Exhibit 99.1 (ICE transaction announcement, 2026): https://www.sec.gov/Archives/edgar/data/1278021/000119312526324933/d159148dex991.htm
- DTCC, SIFMA and ICI, T+1 after-action report (2024) *(title only)*; FINRA TRACE FactBook 2025 *(title only)*; Matt Levine, *Money Stuff*, on TRACE, Treasury clearing, and manufactured credit events *(title only)*.

**Academic Papers**
- Asquith, Covert and Pathak (2013, rev. 2019), *The Effects of Mandatory Transparency in Financial Market Design: Evidence from the Corporate Bond Market*, NBER w19417: https://www.nber.org/papers/w19417
- Duffie, Fleming, Keane, Nelson, Shachar and Van Tassel (2023), *Dealer Capacity and U.S. Treasury Market Functionality*, NY Fed Staff Report 1070: https://www.newyorkfed.org/research/staff_reports/sr1070
- *Title only:* Bessembinder, Maxwell and Venkataraman (2006), *Market Transparency, Liquidity Externalities, and Institutional Trading Costs in Corporate Bonds*; Edwards, Harris and Piwowar (2007), *Corporate Bond Market Transaction Costs and Transparency*; Goldstein, Hotchkiss and Sirri (2007), *Transparency and Liquidity: A Controlled Experiment on Corporate Bonds*; Bao, O'Hara and Zhou (2018), *The Volcker Rule and Corporate Bond Market Making in Times of Stress*; Duffie (2012), *Market Making Under the Proposed Volcker Rule*; Duffie (2020), *Still the World's Safe Haven?*; Avellaneda and Stoikov (2008), *High-Frequency Trading in a Limit Order Book*; Kyle (1985), *Continuous Auctions and Insider Trading*.

**Data & Code**
- NY Fed primary dealer statistics (FR 2004): https://www.newyorkfed.org/markets/counterparties/primary-dealers-statistics
- FINRA Rule 6730 (TRACE reporting): https://www.finra.org/rules-guidance/rulebooks/finra-rules/6730
- FINRA Rule 6750 (TRACE dissemination, including Treasuries): https://www.finra.org/rules-guidance/rulebooks/finra-rules/6750
- SEC EDGAR: https://www.sec.gov/edgar
- FRED (Federal Reserve Economic Data): https://fred.stlouisfed.org/
- This chapter's `REGIME_DATES` table, which Chapters 19, 20, 24 and Appendix C import as the single dated source for regulatory structural breaks.

<!-- STATUS: COMPLETE -->
