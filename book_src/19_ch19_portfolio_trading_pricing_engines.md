# Chapter 19: Portfolio Trading & Basket Pricing Engines

It is 2:58 p.m. on the Friday before a lender call, and the inquiry lands on Ines Okafor's screen with all the subtlety of a fire alarm. Client sells. One hundred and fifty lines of high yield, \$212mm of par, one price, all or none. Eight dealers in competition. Response window: three minutes.

"What's the pot, what are the odds, and who at this table knows more than you?" Ines says, to no one and everyone. "We have ninety seconds. The other ninety are for me to change my mind."

Kaz has already typed `cov = np.cov(returns)` into a notebook. The matrix is 150 by 150, and each bond has fourteen observed returns. "It's singular," Kaz reports, with the calm of someone who has been here before, "but if we just assume Gaussian..."

"Back in my day," says Mags Dunleavy from across the aisle, not looking up, "the basket was a fax. Forty pages. Page nine was always missing, and page nine was always where they'd put the bonds they actually wanted to sell."

Theo Marsh is scrolling the list. Line 42 is \$18mm of a bond that last printed eight weeks ago. Line 117 stops him cold. He knows that issuer. Two months ago, from his old seat, he watched its lenders hire counsel. There is a lender call on Monday. The 13-week cash flow model on his USB stick, the one he carries for emotional support, puts the end of the issuer's liquidity runway about a quarter out. "Before we price this," he says, "what does the credit agreement say about line 117?"

Ines looks at him for a full second, which on this desk is a long time. "That," she says, "is the right question asked in the wrong ninety seconds. Ask it faster."

The question this chapter answers is the one on Ines's screen: **what is one price for 150 bonds, how do you produce it in ninety seconds, and which two lines are paying for the whole trade?**

By the end of this chapter you will be able to:

- write the dealer's basket bid as a certainty equivalent with four terms: fair value, liquidation cost, residual risk after the hedge, and adverse selection;
- compute per-line liquidation cost from LCS at size without counting duration twice;
- collapse 150 lines into a hedge plus a residual, and build a residual covariance matrix that is not lying to you;
- run an eviction loop that tells the client which lines to take back;
- switch the engine into stress mode with a liquidity multiplier and a rank-one covariance spike;
- find the mystery box (the line the client knows something about) before you own it.

On the buy side, you will be able to decide when the portfolio-trade premium is worth paying, as a calculation rather than a mood.

## 19.1 What a Portfolio Trade Is (and Isn't)

A list RFQ is a buffet. A portfolio trade is a tasting menu: you eat the beet course or you go home. That one sentence carries most of the economics. In a list RFQ each line is priced separately, so every dealer bids the lines it likes, and the client's leftover is whatever nobody wanted. In a portfolio trade (PT), the client sends the list (identifiers, sides, sizes) to a handful of dealers. Each dealer returns one price for the whole basket, usually as a spread or a price-level concession against a reference composite. The winner takes every line as a single piece of risk. Nothing is cherry-picked. In 2019 roughly eight to ten dealers could price a basket this way, against the 70 to 80 that answered single-bond RFQs (The DESK, 2019-10-06, "The burgeoning portfolio trading business").

Three mechanical details matter for the engine.

1. **Spotting.** Counterparties agree a spread at, say, 13:30 and convert to prices at 15:00, so the Treasury hedges on the rate leg can be netted. Spotting clusters at 15:00, 15:30 and 16:00 (Meli & Todorova, 2023, "Portfolio Trading in Corporate Bond Markets"). The engine prices *credit* risk and spots the rate leg separately, which is why the derivations below have no $r$ in them.
2. **Reporting.** Since 2023-05-15, TRACE has carried a mandatory portfolio-trade modifier for trades between two parties covering at least ten unique issues at a single basket price (FINRA Regulatory Notice 22-12). Before that date, researchers had to reconstruct PTs from timestamp clusters, and any pre-2023 PT statistic should be read with that in mind.
3. **Anatomy.** The average PT that Barclays identified in 2021 TRACE had about 100 line items and about \$70mm notional, spread fairly evenly across bonds (The DESK, 2022-06-01, reporting Meli, Todorova, Mittal and Kelleher). Li's 2018 sample averages 112 unique CUSIPs from 80 issuers and \$57.9mm notional. About a third of her baskets mix dealer-buy and dealer-sell lines, and most mix IG and HY (Li, 2022, "Frictional Intermediation, Inventory Hedging, and the Rise of Portfolio Trading in the Corporate Bond Market"). So the engine must accept signed notionals, and the cold open's one-sided, all-HY \$212mm basket sits at the large and nasty end of the distribution.

Who sends them? In the Federal Reserve's June 2025 Senior Credit Officer Opinion Survey (SCOOS), about three-fifths of dealers active in credit PT named insurers and pensions or endowments as *frequent* users. More than four-fifths pointed to ETF managers and mutual funds, and about three-quarters to hedge funds, as occasional or frequent users. All of the active dealers said high-grade bonds frequently appear in baskets, and three-fifths said the same of high yield.

What a PT is not: it is not a list RFQ (above), and it is not an ETF creation or redemption, though the dealer may end up delivering part of the basket into one (Chapter 20). It is closest to the equity "risk bid" on a program trade: one price for a bundle, set by a dealer who means to hedge the bundle's market exposure and live with the rest.

> **[SOURCE EXTRACTION]** *Man_Revolutions_in_Credit_Trading_2023 p.2:* "2021 then became, in our view, the year of portfolio trading (Figure 2). We found that orders attracted high fill rates as competition for trades proliferated, not only among what we would consider tier-one counterparties but also those in the second tier, with aggressive pricing offered."
>
> **Annotation.** Read it as a statement about the *margin* term, not the cost terms. In the master equation of §19.2, a dealer's bid is its reservation price minus a margin $\pi$, and in a first-price auction among eight dealers $\pi$ is set by competition. The 2021 boom was second-tier dealers buying market share by bidding $\pi$ toward zero, and in some cases below the true reservation price. Man's next page (§19.6) records what happened in 2022 when they stopped. The modern desk's lesson: a PT hit rate is a function of your $\pi$ *and everyone else's balance sheet*. If you are winning everything, check whether you are the cheapest dealer or the most optimistic one. Those are different businesses, and only one survives the winner's curse (Chapter 18).

> **Desk Myth vs. Desk Reality.** *Myth:* PTs are always cheaper than trading the lines one by one. *Reality:* they are cheaper *for the bonds that go into them*. Meli & Todorova find a PT line costs 6.0bp less than the same bond traded by RFQ, against an average RFQ effective half-spread of 14.5bp: a 41.7% saving, rising to 55.2% (8bp) for illiquid bonds and falling to 19.3% (2.8bp) for liquid ones. Yet Man Numeric moved most of its flow back to electronic RFQ in 2022–23 and reports "significant savings in transaction costs versus portfolio trades" (Man_Revolutions_in_Credit_Trading_2023 p.5). Both are true. The PT saving is largest exactly where single-line RFQs work worst. For a book of liquid lines with a high electronic fill rate, the certainty you buy with a PT costs more than it is worth. §19.9 turns this into an inequality.

> **Trend Watch: the basket protocol, 2018–2026.** *What changed:* PT went from a curiosity to standard risk-transfer plumbing. *How big:* about 1% of IG volume in 2018 and 7% in 2021 (Meli & Todorova, December 2023 version). PT was a record 5.4% of US corporate transactions in January 2021, against 2.2% a year earlier (Tradeweb data via IFR, 2021). Barclays' own PT desk went from "virtually zero" in 2018 to more than 2,000 inquiries and \$175bn in 2021, with PT about 8% of US credit volume by mid-2022 (The DESK, 2022-06-01). In 2024 PT was about 10% of IG and 8% of HY volume, and electronic PT averaged \$3.3bn a day, up 76% (Coalition Greenwich, January 2025). In March 2025 about 25% of institutionally sized US IG risk trades went via PT, up from just over 20% in January (Bloomberg *Market Dialogues*, 2025-07-07). PT was 12% of the \$89.7bn traded on 2025-04-08 (Coalition Greenwich, citing Trumid) and 18% of the \$84.7bn traded on 2025-09-30, which Coalition Greenwich's 2025 review lists as the record day. (The two "record" claims rest on different volume definitions. Chapter 22 untangles them.) The platform race is now a PT race. MarketAxess held about 13% of electronic PT in 2024, against Tradeweb's more than two-thirds (Coalition Greenwich, January 2025). It reported an estimated 20.9% share of US credit portfolio trading in January 2026 and 22.0% in May 2026 (MarketAxess monthly volume releases). *Dealer side:* nearly two-thirds of SCOOS dealers are active in PT, four-fifths of those increased PT provision after January 2023, and about four-fifths expect to do more (SCOOS, June 2025). *What it means for the desk:* PT share depends on the denominator (share of TRACE volume, about 10–18%, versus share of institutional risk trades, about 25%). Whoever owns the basket engine sets the marginal price of IG risk transfer, and increasingly HY.

## 19.2 The Master Equation: Four Terms, One Price

Here is the first aha for the ex-RSSG reader. **The dealer is not pricing 150 bonds. The dealer is pricing one ETF-shaped lump plus a residual, and the residual is where everything you learned at PJT lives.** Meli & Todorova find that the average IG PT has a 30-day return correlation of 0.85 with LQD. On average 60% of its bonds are held by LQD, even though LQD holds only about 30% of index bonds. The lump can be hedged in the same minute with ETF shares, index CDS, total return swaps or credit futures (§19.4). What cannot be hedged is the 12 off-index lines, the two names with ad hoc groups forming, and the \$18mm line in a bond that last printed eight weeks ago. Math PhDs price the lump well. The reader prices the residual well. This chapter's job is to put both in one engine.

### 19.2.1 Derivation: the basket bid as a certainty equivalent

**State this once, loudly: every expectation in this chapter is under the physical measure $\mathbb{P}$.** The dealer is pricing its own P&L over a few days, not replicating a claim. ROBO, left alone, will discount at $r$ under $\mathbb{Q}$ and call it rigor.

*Setup.* Let $\mathbf{x}\in\mathbb{R}^N$ be the signed par notional of the basket $\mathcal{B}$, in dollars, with $x_i>0$ meaning the dealer buys line $i$ (the client sells). The dealer pays $p_i$ per unit of par, holds and unwinds over a horizon of $T$ business days, and line $i$ is worth $\widetilde P_{i,T}$ (fraction of par) at the end. Liquidation costs total $C^{\text{liq}}(\mathbf{x})$ dollars. Terminal P&L is

$$
W \;=\; \sum_{i=1}^{N} x_i\big(\widetilde P_{i,T}-p_i\big)\;-\;C^{\text{liq}}(\mathbf{x}).
$$

*Assumptions.* (i) The composite mid is unbiased over the horizon: $\mathbb{E}^{\mathbb{P}}[\widetilde P_{i,T}\mid\mathcal{F}_t]=\widehat P_i$. The rate leg is spotted and hedged, and carry is second order for $T\le 10$ days. (ii) $\operatorname{Cov}^{\mathbb{P}}(\widetilde{\mathbf P}_T\mid\mathcal{F}_t)=\Sigma_T$, measured in (fraction of par)$^2$ over the horizon. (iii) The dealer has CARA utility $u(W)=-e^{-\gamma W}$ with absolute risk aversion $\gamma$ in units of $\$^{-1}$.

*Step 1 (certainty equivalent).* The CE is the sure amount with the same utility: $u(\text{CE})=\mathbb{E}^{\mathbb{P}}[u(W)]$, so

$$
\text{CE} \;=\; -\frac{1}{\gamma}\log \mathbb{E}^{\mathbb{P}}\big[e^{-\gamma W}\big].
$$

*Step 2 (cumulant expansion).* Write $\log\mathbb{E}[e^{-\gamma W}]=\sum_{n\ge1}\kappa_n(-\gamma)^n/n!$, where $\kappa_n$ are the cumulants of $W$. Then

$$
\text{CE} \;=\; \kappa_1 \;-\; \tfrac12\gamma\,\kappa_2 \;+\; \tfrac16\gamma^2\kappa_3 \;-\;\cdots
$$

For Gaussian $W$ every cumulant past the second vanishes, so $\text{CE}=\mathbb{E}[W]-\tfrac12\gamma\operatorname{Var}[W]$ exactly. Otherwise the truncation drops the skew term, and a line with jump-to-default risk has $\kappa_3<0$, which *lowers* the CE. Mean–variance therefore under-charges the line Theo is worried about. That missing term is exactly what the adverse-selection charge of §19.8 puts back.

*Step 3 (moments).* With $C^{\text{liq}}$ treated as deterministic for now (§19.7 makes it random), $\mathbb{E}[W]=\sum_i x_i(\widehat P_i-p_i)-C^{\text{liq}}(\mathbf{x})$ and $\operatorname{Var}[W]=\mathbf{x}^\top\Sigma_T\mathbf{x}$.

*Step 4 (indifference).* Write the basket's dollar price as $P^{\text{PT}}=\sum_i x_i p_i$. The dealer's reservation basket price sets $\text{CE}=0$:

$$
P^{\text{PT}}_{\text{res}} \;=\; \sum_i x_i\widehat P_i \;-\; C^{\text{liq}}(\mathbf{x}) \;-\; \tfrac12\gamma\,\mathbf{x}^\top\Sigma_T\,\mathbf{x}.
\tag{19.1}
$$

Only the *basket* price is pinned down. How the bid is split across lines is a reporting choice, which matters for best-execution files (§19.9), not an economic one.

*Step 5 (the master equation).* In §19.4 the dealer hedges and $\Sigma_T$ is replaced by the residual covariance $\Sigma^{\text{res}}_T$. In §19.8 the inclusion of informed lines adds an adverse-selection charge $\text{AS}(\mathcal{B})$. Competition subtracts a margin $\pi\ge0$:

$$
P^{\text{PT}}_{\text{bid}} \;=\; \underbrace{\sum_i x_i\widehat P_i}_{\text{fair value}} \;-\; \underbrace{\sum_i c_i(x_i)}_{\text{liquidation cost}} \;-\; \underbrace{\tfrac12\gamma\,\mathbf{x}^\top\Sigma^{\text{res}}_T\mathbf{x}}_{\text{residual risk}} \;-\; \underbrace{\text{AS}(\mathcal{B})}_{\text{mystery box}} \;-\;\pi .
\tag{19.2}
$$

With $n$ dealers in competition, the winner is the highest bidder in a first-price, common-value auction, so $\pi$ must include winner's-curse shading (the BWIC derivation in Chapter 18).

*Boundary checks.* With $N=1$, the risk term's gradient $\gamma(\Sigma^{\text{res}}_T\mathbf{x})_i$ is the vector version of the Avellaneda–Stoikov inventory skew in $r^{\text{res}}$ (Chapter 18), and the basket engine collapses to a single-name quote. Flipping $\mathbf{x}\to-\mathbf{x}$ (the client buys) flips the fair-value term, but the cost terms stay positive, so the dealer's ask is fair value *plus* costs. Setting $\gamma\to0$ leaves a risk-neutral dealer who still pays liquidation cost and still gets picked off. Risk neutrality is not a cure for adverse selection.

*Units, the most common bug.* $x_i$ is in dollars of par, $\widehat P_i$ in fraction of par, $\Sigma^{\text{res}}_T$ in (fraction of par)$^2$ over the horizon, and $\gamma$ in $\$^{-1}$. So $\gamma\,\mathbf{x}^\top\Sigma\mathbf{x}$ has units $\$^{-1}\cdot\$^2=\$$. Every term in (19.2) is in dollars. Convert to basis points of gross market value only at the very end.

> **[SOURCE EXTRACTION]** *Man_Revolutions_in_Credit_Trading_2023 p.2:* "We attribute this to a combination of the growth of bond ETF trading and the advances made by algorithmic market-making desks on fixed income. These developments helped dealers become more comfortable in their ability to price debt securities in near real time and in greater size, initially in investment grade and then eventually within high yield too."
>
> **Annotation.** The two technologies map onto two terms of (19.2). Bond ETFs (and later index derivatives) shrink the risk term by replacing $\Sigma_T$ with $\Sigma^{\text{res}}_T$. Algorithmic market making shrinks the *latency* of the fair-value term: an auto-pricer that already holds a live $\widehat P_i$ for 10,000 bonds turns a 150-line basket into lookups. Note the order Man gives, "investment grade and then eventually within high yield": HY baskets correlate less with HYG and JNK than IG baskets do with LQD, so their residual is larger and their adverse-selection tail fatter. The 2026 desk prices HY PTs routinely, but runs a different $\gamma$, a different eviction target and a far more paranoid $\text{AS}$ model for them.

### Specification for AI Implementation

**What ROBO built from the vague version.** Theo asked for "the basket's cost in bp." ROBO computed handling cost in basis points of par, risk in dollars and adverse selection in price points, summed them, and returned 412. That number is correct in no unit known to science. ROBO never complains and never guesses, so it did not ask.

**The precise spec.** The inquiry is a struct of arrays, one entry per line, all shape $(N,)$, plus model inputs from the overnight build: loadings $B\in\mathbb{R}^{N\times K}$, factor covariance $\Omega\in\mathbb{R}^{K\times K}$, hedge loadings $A\in\mathbb{R}^{H\times K}$ and hedge basis covariance $U\in\mathbb{R}^{H\times H}$.

| Field | Shape | Units | Guard |
| :--- | :--- | :--- | :--- |
| `ids` | $(N,)$ | security-master id | unique; must resolve; examples use synthetic ids, never real CUSIPs |
| `x` | $(N,)$ | \$ par, signed, $+$ = dealer buys | nonzero; $\lvert x_i\rvert\le$ amount outstanding |
| `mid` | $(N,)$ | composite mid, fraction of par | $(0,1.5]$; reject `97.0` (points sent as fraction) |
| `age` | $(N,)$ | business days since a print anchored the composite | $\ge0$; flag $>10$ |
| `print_frac` | $(N,)$ | share of last 60 business days with a print | $(0,1]$ |
| `lcs` | $(N,)$ | round-trip LCS at standard size, fraction of price | $\ge0$ |
| `oasd`, `oas` | $(N,)$ | years; decimal | finite |
| `sector` | $(N,)$ int | code in $[0,K-1)$ | |
| `sig_idio` | $(N,)$ | daily idiosyncratic price vol, fraction of par | $>0$ |
| `prs` | $(N,)$ | Priming Risk Score (Chapter 13) | $[0,1]$ |
| `days_to_call` | $(N,)$ | business days to next lender call | `inf` if none |
| `ad_hoc` | $(N,)$ | live ad hoc group or Rule 2019 statement | $\{0,1\}$ |

Basket-level fields: response deadline (seconds), number of dealers in competition, spotting time, and the client's identity, which keys the markout history in §19.8. All costs are returned in dollars, with a bp-of-gross-MV view computed last. The python blocks in this chapter run in order in one interpreter.

```python
import time
import numpy as np
from dataclasses import dataclass, replace

RNG = np.random.default_rng(19)
N_SECTORS = 8

@dataclass
class Basket:
    """Struct-of-arrays PT inquiry. All arrays shape (N,). Units in comments."""
    ids: np.ndarray           # synthetic line ids (never real CUSIPs in examples)
    x: np.ndarray             # signed par notional, $; + = dealer buys (client sells)
    mid: np.ndarray           # composite mid, fraction of par (0.97 = 97.00)
    age: np.ndarray           # business days since a print anchored the composite
    print_frac: np.ndarray    # share of last 60 business days with a print, in (0, 1]
    lcs: np.ndarray           # round-trip LCS at standard size, fraction of price
    oasd: np.ndarray          # spread duration, years
    oas: np.ndarray           # OAS, decimal (0.045 = 450bp)
    sector: np.ndarray        # int sector code in [0, N_SECTORS)
    sig_idio: np.ndarray      # daily idiosyncratic price vol, fraction of par
    prs: np.ndarray           # Priming Risk Score in [0, 1] (Ch 13)
    days_to_call: np.ndarray  # business days to next lender call; np.inf if none
    ad_hoc: np.ndarray        # 1.0 if an ad hoc group / Rule 2019 statement is live

    def __post_init__(self):
        n = len(self.x)
        for name, arr in self.__dict__.items():
            if len(arr) != n:
                raise ValueError(f"{name}: length {len(arr)} != {n}")
        numeric = [self.x, self.mid, self.age, self.print_frac, self.lcs, self.oasd,
                   self.oas, self.sig_idio, self.prs, self.ad_hoc]
        if not all(np.all(np.isfinite(a)) for a in numeric):
            raise ValueError("non-finite numeric field")
        if np.any(self.x == 0):
            raise ValueError("zero-notional line")
        if np.any((self.mid <= 0) | (self.mid > 1.5)):
            raise ValueError("mid must be a fraction of par in (0, 1.5]: was 97.0 sent?")
        if np.any((self.print_frac <= 0) | (self.print_frac > 1)):
            raise ValueError("print_frac must lie in (0, 1]")
        if np.any(self.lcs < 0) or np.any((self.prs < 0) | (self.prs > 1)):
            raise ValueError("need lcs >= 0 and prs in [0, 1]")
        if np.any(self.sig_idio <= 0):
            raise ValueError("sig_idio must be positive")

    @property
    def n(self):
        return len(self.x)

    def mv(self):
        """Unsigned market value of each line, $."""
        return np.abs(self.x) * self.mid

    def drop(self, idx):
        keep = np.ones(self.n, dtype=bool)
        keep[np.asarray(idx, dtype=int)] = False
        return Basket(**{k: v[keep] for k, v in self.__dict__.items()})


def make_basket(n=150, total=212e6, seed=19):
    """Synthetic all-HY client-sell basket matching the cold open (illustrative)."""
    rng = np.random.default_rng(seed)
    size = rng.lognormal(mean=np.log(1.0e6), sigma=0.6, size=n)
    others = np.ones(n, dtype=bool)
    others[[41, 116]] = False
    size[41], size[116] = 18e6, 4e6                      # line 42 and line 117 (1-based)
    size[others] *= (total - 22e6) / size[others].sum()  # hit the $212mm ticket exactly
    mid = np.clip(rng.normal(0.97, 0.04, n), 0.70, 1.06)
    age = rng.exponential(1.5, n)
    pf = rng.uniform(0.15, 0.80, n)
    lcs = np.clip(rng.lognormal(np.log(0.010), 0.45, n), 0.003, 0.06)
    oasd = rng.uniform(2.5, 6.0, n)
    oas = rng.uniform(0.025, 0.060, n)
    sector = rng.integers(0, N_SECTORS, n)
    sig = 0.0025 * rng.uniform(0.6, 1.6, n)
    prs = rng.beta(1.0, 9.0, n)
    dtc = np.full(n, np.inf)
    adhoc = np.zeros(n)
    # line 42: big, stale, wide ("last printed eight weeks ago")
    age[41], pf[41], lcs[41], mid[41], sig[41] = 40.0, 0.05, 0.025, 0.95, 0.003
    # line 117: the name Theo recognizes; note its realized vol looks perfectly calm
    mid[116], oas[116], lcs[116], sig[116] = 0.82, 0.090, 0.012, 0.003
    prs[116], dtc[116], adhoc[116] = 0.85, 3.0, 1.0
    ids = np.array([f"L{i + 1:03d}" for i in range(n)])
    return Basket(ids, size, mid, age, pf, lcs, oasd, oas, sector, sig, prs, dtc, adhoc)


b0 = make_basket()
assert b0.n == 150 and abs(np.abs(b0.x).sum() - 212e6) < 1.0
assert np.all(b0.x > 0)                      # client sells everything: dealer buys
try:                                         # the points-vs-fraction guard fires
    replace(b0, mid=b0.mid * 100.0)
    raise AssertionError("guard failed")
except ValueError:
    pass

# Sanity (DER A): mean-variance CE is exact for CARA utility and Gaussian P&L
gam_t, mu_t, sd_t = 1e-6, 1.0e5, 3.0e5       # 1/$, $, $
W = RNG.normal(mu_t, sd_t, 400_000)
ce_mc = -np.log(np.mean(np.exp(-gam_t * W))) / gam_t
assert abs(ce_mc - (mu_t - 0.5 * gam_t * sd_t**2)) < 2_000.0
```

The Monte Carlo check is not decoration. If someone later swaps the Gaussian P&L for a jump-to-default mixture, the same check fails, and the size of the failure is the $\tfrac16\gamma^2\kappa_3$ term from Step 2: the skew that mean–variance ignores and that §19.8 charges for explicitly.

## 19.3 Per-Line Liquidation Cost: LCS, Size, and the Fat Tail

Ines calls the per-line cost "the rake": the house's cut of each hand, small, boring, and the reason the house still exists. For an ex-RSSG banker the instinct is to see line 83 as a claim with a recovery. The engine sees it first as a number, the cost of getting out, and the canonical seed for that number is Barclays' Liquidity Cost Score.

> **[SOURCE EXTRACTION]** *Ben_Dor_Quantitative_Credit_Portfolio_Management p.112:* "We define LCS as the bond's OASD multiplied by this spread. Consequently, a bond's LCS can be interpreted as the cost, in percentage points, of immediately executing a roundtrip transaction."
>
> **Annotation.** The spread-quoted branch is $\text{LCS}_i=D^{\text{spr}}_i\,(s^{\text{ask}}_i-s^{\text{bid}}_i)$, which is *already in price space*: a 4-year spread duration times a 25bp bid–ask is 1.00% of price. Every desk has a junior quant who multiplies it by duration again to "convert to price," producing a 4% round-trip cost and a PT bid that never wins. For HY and distressed lines quoted on price, the branch is $(P^{\text{ask}}-P^{\text{bid}})/P^{\text{bid}}$ (Ben_Dor p.118; Dynkin_Systematic_Investing_in_Credit p.702 gives the same two branches). Ben Dor also pins the size: LCS is the cost "for a 'normal-sized' transaction amount (e.g., \$3 to \$5 million par)" (p.118). On a 2026 desk the gap is coverage. LCS is a dealer-quote-based score built for index constituents, while a PT drags in off-index lines, so the engine needs a fallback cost model for lines without a score: TRACE-derived effective spreads (Chapter 18's Roll and Kyle estimators) with an explicit staleness flag.

### 19.3.1 Derivation: from a standalone score to a basket cost

*Step 1 (one way).* LCS is a round trip at standard size $x^{\text{std}}$. The dealer buying the basket pays half of it on the way out, so the naive one-way cost of line $i$ in dollars is $\tfrac12\,\text{LCS}_i\,\widehat P_i\,\lvert x_i\rvert$.

*Step 2 (do not charge risk twice).* LCS is a *standalone* price. A dealer quoting one bond alone charges for handling (search, balance-sheet usage, operational cost) and for holding that bond unhedged and undiversified. Write the standalone half-spread as handling plus a standalone inventory charge. Inside a basket, (19.2) already prices inventory risk at the portfolio level through $\tfrac12\gamma\,\mathbf{x}^\top\Sigma^{\text{res}}_T\mathbf{x}$. Charging the full half-LCS *and* the risk term counts the inventory charge twice. So the cost term keeps only the handling share $\omega\in(0,1]$:

$$
c_i(x_i) \;=\; \omega\cdot\tfrac12\,\text{LCS}_i\;\widehat P_i\;\lvert x_i\rvert\;\max\!\Big(1,\frac{\lvert x_i\rvert}{x^{\text{std}}}\Big)^{\eta},
\qquad \eta\in[\tfrac12,1].
\tag{19.3}
$$

*Step 3 (size).* The bracket is flat below standard size, because an institutional half-spread does not get cheaper for smaller tickets (odd lots, if anything, pay more), and it steepens above it. The exponent $\eta$ brackets the two canonical impact models. With linear temporary impact (Almgren & Chriss, 2000, "Optimal Execution of Portfolio Transactions"), a linear unwind of $X$ over $T$ costs $\varepsilon X+\tfrac12\theta_0X^2+\theta_1X^2/T$ in expectation, where $\varepsilon$ is the fixed half-spread and $\theta_0$, $\theta_1$ are permanent and temporary impact coefficients. Per dollar this grows linearly in $X$, so $\eta=1$. With square-root impact (below) the total cost grows like $X^{3/2}$, so the per-dollar cost grows like $X^{1/2}$ and $\eta=\tfrac12$. For line 42, \$18mm against $x^{\text{std}}=\$4$mm, the per-dollar cost is $4.5^{\eta}$ times the standard rate, between 2.1× and 4.5×.

*Step 4 (calibrating $\omega$).* Meli & Todorova's 41.7% saving says an IG PT line costs on average about 58% of its RFQ half-spread, all in. That all-in figure includes risk and adverse selection, so the pure handling share sits below it. We use $\omega=0.5$ in the HY example *(illustrative)*. On your own data, regress realized PT line costs, measured as markouts to the next composite, on half-LCS at size, with the residual-risk contribution $\gamma x_i(\Sigma^{\text{res}}_T\mathbf{x})_i$ as a control.

*Step 5 (horizon).* Almgren–Chriss also hands us $T$. Optimal schedules trade off impact against variance, and Li (2022) finds PT bonds "stay in dealer inventories for 5.3 days longer" than voice bonds, because a hedged lump is cheap to hold. So $T\approx5$ business days for residual lines is empirically grounded. **All variance lives in $\Sigma^{\text{res}}_T$** (§19.4–19.5). Almgren–Chriss contributes only the expected cost and the choice of $T$. Put $\sigma_i^2$ in both places and you have charged it twice, which is the variance version of the duration mistake.

> **[SOURCE EXTRACTION]** *Paleologo_Advanced_Portfolio_Management p.193:* "TC : market impact model. TC(x) = κ Σ_i σ_i^β (|x_i|/v_i)^γ where v_i is the average daily trading volume (in dollars), σ_i the volatility, β ≃ 1, γ ≃ 3/2 and κ > 0 a region-calibrated constant."
>
> **Annotation.** Paleologo's exponent $\gamma\simeq3/2$ is our $1+\eta$ with $\eta=\tfrac12$. We rename it because $\gamma$ is risk aversion in this book. The equity law scales size by average daily volume $v_i$, which in credit is the weakest number on the screen. Most bonds do not trade daily, TRACE volume includes the PT prints themselves, and MarketAxess reported that duplicate trade reports "inflated U.S. high-grade TRACE volumes by up to 8% in June 2026" (Q2-2026 results). So credit swaps the denominator to $x^{\text{std}}$ and the volatility to LCS, a dealer-quote-based object that already embeds the bond's riskiness. Volume survives as a *feature* of the cost model: Ben Dor notes that "LCS is negatively related to a bond's trading volume" (Ben_Dor p.128). It should not be the cost itself.

Composite fair values (dealer-composite and evaluated-pricing services) make the first term of (19.2) a lookup. They also create *composite reflexivity*: when the auto-quoter, the price-improvement benchmark and the PT reference all key off the same composite, a composite error becomes a correlated execution error across every line that uses it. The engine therefore treats a stale composite as a source of *variance* (§19.5), not as a fixed haircut. A stale price is not a wrong price. It is a price with a confidence interval that nobody printed.

> **Ways This Blows Up.** (1) **Duration twice:** LCS for a spread-quoted bond is already a fraction of price. (2) **Size ignored:** LCS at \$4mm applied unscaled to a \$25mm line understates its cost by $6.25^{\eta}$, between 2.5× and 6.25×. (3) **Stale fair value:** an evaluated price for a bond that last traded 40 days ago enters the bid at full confidence unless `age` feeds the covariance. (4) **Contaminated volume:** liquidity features built on raw TRACE volume pick up duplicate affiliate prints and the basket's own PT prints, so the bond looks liquid *because it was in last month's PT*. Deduplicate with the affiliate indicator (voluntary from 2026-08-31, mandatory 2027-08-02, per FINRA Regulatory Notice 26-16) and strip PT-flagged prints. (5) **Points as fractions:** a mid of `97.0` instead of `0.97` raises fair value a hundredfold. The `Basket` guard catches it, and that guard is not optional.

### Specification for AI Implementation (handling cost)

```python
X_STD = 4e6   # LCS standard size, $ par (Ben_Dor p.118: "$3 to $5 million")

def handling_cost(b, omega=0.5, eta=0.75, x_std=X_STD, m=1.0):
    """Eq. 19.3: one-way handling cost per line, $. m = liquidity regime multiplier (19.7)."""
    if not (0.0 < omega <= 1.0 and 0.5 <= eta <= 1.0 and m > 0):
        raise ValueError("omega in (0,1], eta in [0.5,1], m > 0")
    u = np.abs(b.x) / x_std
    return m * omega * 0.5 * b.lcs * b.mid * np.abs(b.x) * np.maximum(1.0, u) ** eta

c0 = handling_cost(b0)
assert np.all(c0 >= 0)
small = np.abs(b0.x) <= X_STD                     # at or below standard size: flat
assert np.allclose(c0[small], 0.25 * b0.lcs[small] * b0.mv()[small])
# line 42 ($18mm) pays (18/4)^0.75 ~ 3.1x the standard per-dollar rate
assert np.isclose(c0[41] / (0.25 * b0.lcs[41] * b0.mv()[41]), 4.5 ** 0.75)
# line 42 alone costs more to handle than the 25 cheapest lines combined
assert c0[41] > np.sort(c0)[:25].sum()
```

The last assert is the fat tail in one line. Line 42 has about 8% of the notional and, by hand arithmetic on this synthetic basket, roughly 40% of the handling cost *(illustrative)*. Section 19.6 will want to talk to it.

## 19.4 The Hedge: Collapsing 150 Lines into One Lump

"You do not own 150 bonds," Ines tells Theo. "You own one ETF you can't sell and 150 small arguments." The hedge is how the dealer gets rid of the ETF. The menu, and what each item kills:

- **ETF shares** (LQD for IG; HYG, JNK and USHY for HY): systematic spread risk, at a 1–2bp half-spread in calm markets, with a premium/discount basis that becomes the main risk in stress.
- **Index CDS** (CDX IG, CDX HY): systematic spread risk with no cash basis but a CDS–bond basis, and no help with the cash bonds' liquidity.
- **iBoxx total return swaps**, standardized from 2015 (Li, 2022), and options on corporate bond ETFs.
- **Cboe iBoxx credit futures** (IBIG, IBHY): listed, blockable, and growing (Trend Watch below).
- **Treasury futures** for the spotted rate leg, which the engine treats as already done.

> **[SOURCE EXTRACTION]** *Ben_Dor_Quantitative_Credit_Portfolio_Management p.166:* "To hedge default-related risks at the issuer level, investors may use the issuer's CDS. For hedging systemic liquidity risks, VIX futures might be a more appropriate instrument… the correlation between LCS and VIX from January 2007 to April 2009 was 0.90."
>
> **Annotation.** This is the hedge menu sorted by *which term of (19.2) it touches*. Index instruments attack the systematic part of $\Sigma_T$. Single-name CDS could attack line 117's jump, if it trades, if it is not itself being manufactured by the same ad hoc group (Chapter 24), and if you can buy protection in 90 seconds, which you cannot. Nothing on the menu hedges the *liquidity* term: the 0.90 LCS–VIX correlation says the cost multiplier of §19.7 is one systematic factor, and the engine has no instrument that pays off when it rises. The 2026 desk proxies it with ETF discounts and VIX, and prices what it cannot hedge.

### 19.4.1 Derivation: the minimum-variance hedge and the residual

Let $\mathbf{r}\in\mathbb{R}^N$ be bond price changes over the horizon (fraction of par) and $\mathbf{f}\in\mathbb{R}^H$ the returns of $H$ hedge instruments per dollar notional, with joint covariance

$$
\operatorname{Cov}^{\mathbb{P}}\begin{pmatrix}\mathbf{r}\\ \mathbf{f}\end{pmatrix}=\begin{pmatrix}\Sigma_{xx} & \Sigma_{xf}\\ \Sigma_{fx} & \Sigma_{ff}\end{pmatrix},\qquad \Sigma_{fx}=\Sigma_{xf}^\top .
$$

The dealer is long $\mathbf{x}$ and sells $\mathbf{h}$ dollars of hedges, so the hedged P&L is $\mathbf{x}^\top\mathbf{r}-\mathbf{h}^\top\mathbf{f}$ with variance

$$
V(\mathbf{h}) \;=\; \mathbf{x}^\top\Sigma_{xx}\mathbf{x} \;-\; 2\,\mathbf{h}^\top\Sigma_{fx}\mathbf{x} \;+\; \mathbf{h}^\top\Sigma_{ff}\mathbf{h}.
$$

*First-order condition.* $\nabla_{\mathbf h}V=-2\Sigma_{fx}\mathbf{x}+2\Sigma_{ff}\mathbf{h}=0$. Since $\Sigma_{ff}\succ0$, this is a minimum and

$$
\mathbf{h}^\star=\Sigma_{ff}^{-1}\Sigma_{fx}\mathbf{x},\qquad
V(\mathbf{h}^\star)=\mathbf{x}^\top\underbrace{\big(\Sigma_{xx}-\Sigma_{xf}\Sigma_{ff}^{-1}\Sigma_{fx}\big)}_{\Sigma^{\text{res}}}\mathbf{x}.
\tag{19.4}
$$

$\Sigma^{\text{res}}$ is the Schur complement of $\Sigma_{ff}$. Under joint Gaussianity it is the conditional covariance $\operatorname{Cov}(\mathbf{r}\mid\mathbf{f})$, which has a useful consequence: **$\mathbf{x}^\top\Sigma^{\text{res}}\mathbf{x}$ is the optimally re-hedged variance for any basket $\mathbf{x}$.** When §19.6 evicts a line, the hedge re-optimizes for free, with no second solve. The hedge's own cost, $c_h=\sum_j\lvert h^\star_j\rvert\,\text{hs}_j$ with $\text{hs}_j$ the half-spread per dollar notional, is added to (19.2). It is small for LQD and CDX and not small for a futures block in a thin month.

*The one-factor case, and why basis attenuates the hedge.* Let $r_i=\beta_i g+\epsilon_i$, with $\beta_i=-\widehat P_i\,\text{DTS}_i$ the price sensitivity to a common relative-spread move $g$ (the DTS model of Chapters 8–9), and one hedge with return $f=\beta_h g+u$, where $u$ is basis noise with variance $\sigma_u^2$. Then

$$
h^\star=\frac{\beta_h\sigma_g^2}{\beta_h^2\sigma_g^2+\sigma_u^2}\sum_i x_i\beta_i,
\qquad
\Sigma^{\text{res}}_{ij}=\beta_i\beta_j\,\frac{\sigma_g^2\,\sigma_u^2}{\beta_h^2\sigma_g^2+\sigma_u^2}+\delta_{ij}\,\sigma^2_{\epsilon,i}.
$$

With no basis ($\sigma_u\to0$), $h^\star=\sum_i x_i\beta_i/\beta_h$, the DTS-matched hedge, and the residual is purely idiosyncratic. Its variance grows like $N$ while the basket's dollar size grows like $N$, so the risk per dollar falls like $1/\sqrt{N}$. That is the one-line reason a dealer can quote a diversified, hedgeable basket *inside* the sum of its line half-spreads. With basis, the hedge ratio shrinks (classic errors-in-variables attenuation), and a rank-one systematic residual survives that does *not* diversify. In March 2020 bond ETF tracking error exceeded 200bp against a 0.7bp average (Todorov, BIS Quarterly Review, March 2021, "The anatomy of bond ETF arbitrage"). In the formula above, $\sigma_u$ went from a rounding error to the dominant term.

*Two theories of why PT works, both in this equation.* Meli & Todorova link PT's cost advantage to the ETF ecosystem: baskets that are "closer" to ETFs are cheaper, both because ETFs give real-time prices and hedges and because creation/redemption is an outlet for less liquid bonds. Li (2022) finds that only 20–30% of PT bonds overlap with realized ETF creation/redemption baskets, that voice costs respond to dealer inventory shocks while PT costs do not, and attributes the rise of PT to inventory hedging with index derivatives. The SCOOS answers split the difference. About four-fifths of active dealers call trading the individual constituents through other protocols a *very important* way to work off PT inventory. ETF creation/redemption and offsetting PTs are at least somewhat important for about three-quarters and one-half respectively. Three-fifths "frequently hedge credit portfolio trades with credit ETFs," and about half use CDS in at least a few situations. In engine terms, Li is about $\Sigma_{ff}$ (the hedge shrinks the risk term) and Meli–Todorova is partly about $c_i$ (the creation/redemption window lowers the liquidation cost of the residue). Both terms are in (19.2), so you do not have to pick a side.

> **Ways This Blows Up.** (1) $\Sigma_{ff}$ estimated from ETF *price* returns in a calm window carries a basis variance near zero, so the engine over-hedges in exactly the week the basis explodes. Model the basis as its own regime-dependent variance (`basis_scale` below). (2) A dealer that is not an authorized participant cannot deliver residue into a creation basket, so its $T$ is longer and its $c_i$ higher. (3) HY baskets correlate less with HYG and JNK, and less stably, than IG baskets with LQD. Meli–Todorova's 0.85 is an IG number. (4) Two nearly collinear hedges (an HY ETF and CDX HY) make $\Sigma_{ff}$ ill-conditioned, and $\mathbf{h}^\star$ becomes a large long–short position in two instruments that differ only by their basis noise. Guard the condition number.

> **Trend Watch: the hedge stack, 2015–2026.** *What changed:* the instruments that turn a basket into "one lump plus a residual" multiplied, and the ETF lost its monopoly. *When and how big:* standardized iBoxx TRS from 2015 and corporate bond ETF options gave dealers index hedges for cash inventory (Li, 2022). The credit-ETF-to-cash volume ratio fell from 23.2% in 2022 to 16.6% in 2024 as PT absorbed risk transfer that used to route through ETFs (Coalition Greenwich, January 2025). On stress days ETFs re-dominate: \$99bn of fixed income ETFs traded on 2025-04-07, about 60% of it in iShares (The DESK, 2025-06-10). In the June 2025 SCOOS, three-fifths of active PT dealers said they frequently hedge with credit ETFs and about half used CDS in at least a few situations. By August 2026, Cboe iBoxx credit futures block trades topped \$1bn a month for the second month running, and IBIG block volume passed IBHY for the first time (Cboe sponsored content in The DESK, 2026-10-16; treat as vendor-reported). *What it means:* $H$ in (19.4) is now 3–5 instruments, not 1. The hedge solve chooses among them by basis risk and cost, and the engine must carry each instrument's basis as its own variance.

### Specification for AI Implementation (factor model and hedge)

Shapes: $B$ is $(N,K)$ with $K=1+8$ (market plus eight sectors), $\Omega_T$ is $(K,K)$, $A$ is $(H,K)$ with $H=2$ (an HY ETF and CDX HY, both in the long-risk convention, so a positive $h$ sells risk), and $U$ is $(H,H)$. All covariances are over the horizon $T$. Factor and basis volatilities are *illustrative*.

```python
T_DAYS = 5.0          # unwind horizon, business days (Li 2022: ~5.3 extra days in inventory)
SIG_MKT_D = 0.015     # daily vol of the market relative-spread factor (illustrative)
SIG_SEC_D = 0.008     # daily vol of each sector relative-spread factor (illustrative)
HEDGE_HALF_SPREAD = np.array([1e-4, 0.5e-4])   # $ per $ notional: ETF, CDX (illustrative)

def loadings(b):
    """B (N, K): price change (fraction of par) per unit relative spread move.
    DTS model: dP = -P * D_spr * ds,  ds = s * g  =>  B = -P * DTS."""
    dts = b.oasd * b.oas
    B = np.zeros((b.n, 1 + N_SECTORS))
    B[:, 0] = -b.mid * dts
    B[np.arange(b.n), 1 + b.sector] = -b.mid * dts
    return B

def factor_cov(T=T_DAYS):
    """Omega_T (K, K): independent market and sector factors over the horizon."""
    return np.diag(np.r_[SIG_MKT_D**2, np.full(N_SECTORS, SIG_SEC_D**2)]) * T

def hedge_book(T=T_DAYS, basis_scale=1.0):
    """A (H, K) loadings per $ notional; U (H, H) basis covariance. Index DTS 0.16 / 0.14."""
    A = np.zeros((2, 1 + N_SECTORS))
    A[0, 0], A[1, 0] = -0.16, -0.14
    A[0, 1:], A[1, 1:] = -0.16 / N_SECTORS, -0.14 / N_SECTORS   # equal sector weights
    U = np.diag([0.0015**2, 0.0010**2]) * T * basis_scale**2
    return A, U

def joint_cov(b, d, T=T_DAYS, basis_scale=1.0, cond_max=1e8):
    """Sxx (N,N), Sxf (N,H), Sff (H,H); d = (N,) idiosyncratic variance over T."""
    B, Om = loadings(b), factor_cov(T)
    A, U = hedge_book(T, basis_scale)
    Sxx = B @ Om @ B.T + np.diag(d)
    Sxf = B @ Om @ A.T
    Sff = A @ Om @ A.T + U
    if np.linalg.cond(Sff) > cond_max:
        raise ValueError("hedges nearly collinear: drop one or model the basis")
    return Sxx, Sxf, Sff

def residual(Sxx, Sxf, Sff):
    """Eq. 19.4: Schur complement = optimally re-hedged covariance for any basket."""
    return Sxx - Sxf @ np.linalg.solve(Sff, Sxf.T)

def min_var_hedge(x, Sxf, Sff):
    """h* = Sff^{-1} Sfx x, $ notional per hedge (positive = sell risk)."""
    return np.linalg.solve(Sff, Sxf.T @ x)

d_naive = b0.sig_idio**2 * T_DAYS                    # no staleness yet (that is 19.5)
Sxx, Sxf, Sff = joint_cov(b0, d_naive)
Sres_naive = residual(Sxx, Sxf, Sff)
h0 = min_var_hedge(b0.x, Sxf, Sff)
v_unh = b0.x @ Sxx @ b0.x
v_res = b0.x @ Sres_naive @ b0.x
v_chk = v_unh - 2.0 * h0 @ (Sxf.T @ b0.x) + h0 @ Sff @ h0
assert np.isclose(v_res, v_chk, rtol=1e-8)          # Schur complement == hedged variance
assert v_res < 0.5 * v_unh                           # the hedge kills most of the lump
```

### Deep-Dive Resource Graph

**Podcasts**

- Bloomberg Professional, *Market Dialogues*, "How is portfolio trading changing the fixed income landscape?" (2025-07-07; recorded at the Pricing & Valuations Summit): https://professional.content.cirrus.bloomberg.com/professional2023/insights/markets/how-is-portfolio-trading-changing-the-fixed-income-landscape/

**Practitioner Writing**

- Man Group (2023), *Revolutions in Credit Trading* (on the shelf as `Man_Revolutions_in_Credit_Trading_2023`).
- The DESK (2019-10-06), Lynn Strongin Dodds, "The burgeoning portfolio trading business": https://www.fi-desk.com/trading-protocols-portfolio-trading-lynn-strongin-dodds/
- The DESK (2022-06-01), Dan Barnes, "Barclays: Portfolio trading 8% of US credit market volume": https://www.fi-desk.com/barclays-portfolio-trading-8-of-us-credit-market-volume/
- Todorov (2021), "The anatomy of bond ETF arbitrage," *BIS Quarterly Review*, March 2021.

**Academic Papers**

- Meli & Todorova (2023), "Portfolio Trading in Corporate Bond Markets," AEA 2024 program: https://www.aeaweb.org/conference/2024/program/paper/a7z3SGGN
- Li, J. S. (2022), "Frictional Intermediation, Inventory Hedging, and the Rise of Portfolio Trading in the Corporate Bond Market," AEA 2023 program: http://www.aeaweb.org/conference/2023/program/paper/9TfsndSa
- Almgren & Chriss (2000), "Optimal Execution of Portfolio Transactions," *Journal of Risk* 3(2).

**Data & Code**

- FINRA Regulatory Notice 22-12 (TRACE portfolio-trade modifier) and Regulatory Notice 26-16 (affiliate indicator), via the FINRA notices index.
- Federal Reserve SCOOS, June 2025, special questions on credit portfolio trading: https://www.federalreserve.gov/data/scoos/files/scoos_202506.pdf
