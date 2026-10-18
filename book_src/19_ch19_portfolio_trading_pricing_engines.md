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

A table of guards is a promise, and a promise is worth what happens when somebody breaks it. At 2:58 p.m. the list arrives as a spreadsheet exported by a client whose operations team chose the units, and the engine has about ninety seconds to learn whether column D means 97.0 points or 0.97 of par before it multiplies a hundredfold error into a \$212mm bid. A human glances at the first few rows and decides they look right. A desk that wants the same answer at 3:02 p.m. next Friday, when the human is on a flight, writes the contract down once, as an object that refuses to exist if it is wrong, and makes every later calculation take that object as its only input.

Listing 19.1 does three jobs. First, `Basket` holds the inquiry as thirteen parallel arrays, one per row of the table, with the units written beside each field. Its `__post_init__` is the gate. It rejects ragged lengths, non-finite values in the ten numeric fields (`days_to_call` is exempt, because `inf` is how the engine says "no lender call on the calendar"), zero-notional lines, a `mid` outside (0, 1.5], a `print_frac` outside (0, 1], a negative `lcs`, a `prs` outside [0, 1] and a non-positive `sig_idio`. The `mv()` method returns unsigned market value, and `drop()` returns a freshly built, freshly validated `Basket` without the named lines, which is what the eviction loop of §19.6 will lean on. Second, `make_basket` manufactures the cold-open inquiry: 150 lognormal tickets around \$1mm, seeded so the numbers repeat, with line 42 hard-wired at \$18mm, forty days stale and printing on 5% of days, and line 117 at \$4mm, marked at 0.82, with a Priming Risk Score of 0.85, a lender call three days out, a live ad hoc group and a daily idiosyncratic volatility of 0.003 that looks perfectly calm. The other lines are rescaled so the gross lands on \$212mm exactly. Third, the closing block confirms the sizes, checks that multiplying `mid` by 100 raises an error, and runs the Monte Carlo test of the certainty equivalent from §19.2.1: 400,000 Gaussian P&L draws with mean \$100k and standard deviation \$300k should give \$55k, which is the mean minus \$45k of risk charge.

Use it as the single entry door to everything that follows, and do not mistake it for a security-master check. It tests ranges, not meaning. The edge case that bites is the gap between the table and the constructor: the table promises unique ids, non-negative `age`, sector codes in range and an ad hoc flag in {0, 1}, and the code enforces none of them. A sector code of -1 sails through and then, in Listing 19.3, points at the market column instead of a sector, so the line silently loses its sector exposure. Add the checks you need before the first live Friday.

*The full listing is [Listing 19.1 in Appendix F](#code-19-1).*

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

Equation (19.3) is one line of algebra, which is exactly why it ends up typed four different ways in four different notebooks, and why one of the four multiplies by duration a second time. A desk writes the line once, gives it a name and a set of refusals, and lets the rest of the engine call it. The point is not that the arithmetic is hard. The point is that line 42 is about to be priced, and nobody wants an argument at 3:01 p.m. over which notebook's rake is the real one.

Listing 19.2 is `handling_cost`, equation (19.3) vectorized over the whole basket. It takes the `Basket`, the handling share `omega` (default 0.5), the size exponent `eta` (default 0.75, halfway between the square-root and linear impact laws), the standard size `X_STD` of \$4mm, and a liquidity multiplier `m` that sits at 1 in calm markets and is the dial §19.7 turns in stress. It refuses an `omega` outside (0, 1], an `eta` outside [0.5, 1] and a non-positive `m`, so a typo cannot quietly produce a free lunch. Step by step, it expresses each line's size in units of standard size, takes the larger of that and one, raises it to `eta`, and multiplies by half of `lcs`, the mid, the absolute notional, `omega` and `m`. The output is one non-negative dollar cost per line. The sign of `x` is ignored, because handling a bond costs the same whichever way the client trades it. The asserts then check the flat region below \$4mm, the \$18mm multiple of 4.5 to the power 0.75 (about 3.1), and a comparison with the 25 cheapest lines.

Use it for the handling share only, and keep all variance in the covariance matrix of §19.5. The edge case that bites is `lcs` itself. The function trusts the field to be a fraction of price at standard size, and the `Basket` gate checks only that it is not negative. A spread-quoted score that someone already multiplied by duration, or a dealer-quote score carried over from an index bond to an off-index line, flows straight through and comes out the other end as a precise dollar figure.

*The full listing is [Listing 19.2 in Appendix F](#code-19-2).*

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

Kaz's notebook failed because it tried to learn 11,325 covariances from fourteen observations. The cure in the derivation is to stop learning and start assuming: bonds move together because they share a few spread factors, and the hedge exists to remove exactly those. That leaves four matrices to build before the dealer can say how much of the \$212mm is one lump and how much is 150 small arguments: the loadings $B$, the factor covariance $\Omega_T$, the hedge loadings $A$ and the basis covariance $U$. The hedge ratio is also the number the trader will read aloud to the ETF desk, and it had better be the same number the risk term uses. So the desk builds the matrices, runs the solve and proves the two agree in one place, before anyone is allowed to type a price.

Listing 19.3 does exactly that. `loadings` turns each bond into a row of `B` with the DTS rule: price change per unit relative spread move is minus the mid times OAS duration times OAS. A bond loads that amount on the market factor and the same amount on its own sector's factor, and on nothing else. `factor_cov` returns a diagonal $\Omega_T$, with illustrative daily volatilities of 1.5% for the market and 0.8% for each sector, scaled by the five-day horizon. `hedge_book` returns `A` for two instruments, an HY ETF with index DTS 0.16 and CDX HY with 0.14, each spread equally across the sectors, and `U`, the basis covariance, whose `basis_scale` argument is the stress dial. `joint_cov` assembles $\Sigma_{xx}=B\Omega_TB^\top+D$, $\Sigma_{xf}$ and $\Sigma_{ff}$, and stops if the hedge block's condition number passes $10^8$. `residual` forms the Schur complement of (19.4) with a linear solve rather than an inverse, and `min_var_hedge` returns the dollar hedge, positive meaning sell risk. The closing block runs the cold-open basket before any staleness is added: the hedge sells about \$80mm of the ETF and \$157mm of CDX, and the standard deviation of P&L falls from about \$1.37mm to about \$0.52mm *(illustrative)*. Two asserts follow. The residual quadratic form must equal the hedged variance computed by hand, and the hedge must remove more than half the variance.

Use it when the hedge menu is a handful of linear instruments and the factors are stable. Do not use it for options-based hedges, or when the factor covariance was estimated in a calm window and you are about to trade in a loud one. The edge case that bites is in `hedge_book`. The two rows of `A` are exactly proportional, so the ETF and CDX are distinguished only by their basis noise, and `U` alone keeps $\Sigma_{ff}$ invertible. Let a calm-window estimate push `basis_scale` toward zero and the guard fires, which is the right outcome: the engine stops instead of handing the trader a hedge that rests on a basis variance of nothing.

*The full listing is [Listing 19.3 in Appendix F](#code-19-3).*

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

## 19.5 Residual Covariance for 150 Stale Bonds

Kaz's `np.cov` is not just singular. It is lying with confidence. One hundred and fifty bonds with fourteen observed returns each give a sample matrix of rank at most 13, so 137 of its eigenvalues are exactly zero. Those are directions in which the basket appears to carry *no risk at all*. Any optimizer that touches the inverse (the hedge solve, the eviction loop) will find those directions and bet the desk on them. "Fine," says Kaz, "we regularize. While we're at it, Theo, is a springing lien a kind of jump process?" Theo thinks about it. "It springs when a covenant trips." "So it's a stopping time," Kaz says, satisfied. It sort of is, and it does not belong in the covariance matrix. It belongs in §19.8.

### 19.5.1 Derivation: factor structure, staleness, shrinkage

*Structure.* Write $\Sigma_{xx}=B\,\Omega_T\,B^\top+D$. Here $B\in\mathbb{R}^{N\times K}$ holds the loadings on $K\approx10$–$30$ factors (rating × sector × duration-bucket excess-return factors, DTS-scaled as in Chapters 8–9). $\Omega_T$ is the $K\times K$ factor covariance, estimated on the *whole* universe of several thousand bonds, so it is well conditioned. $D=\operatorname{diag}(d_i)$ holds the idiosyncratic variances, the only part estimated from each line's own sparse history. This cuts the parameter count from $N(N+1)/2=11{,}325$ to $K(K+1)/2+N$, and every one of those parameters is estimated on data that exists.

*Staleness is variance.* Let $\widehat P_i$ be a composite last anchored by a print $a_i$ business days ago. Evaluated-pricing services move a stale bond with its comparables, so the *factor* part of its drift since the last print is captured. The idiosyncratic part is not. If a share $\kappa\in(0,1]$ of the idiosyncratic variance escapes the evaluator's matrix pricing, then $\operatorname{Var}(\widehat P_i-P_i^{\text{true}})\approx\kappa\,\sigma^2_{\epsilon,i}\,a_i$, where $\sigma^2_{\epsilon,i}$ is the daily idiosyncratic variance. This error is still unresolved at the moment the dealer buys, so it adds to the horizon variance.

*Non-synchronous trading.* A bond that prints on a fraction $\phi_i$ of days has smoothed observed returns, and its estimated $\sigma^2_{\epsilon,i}$ is biased down. Correct with summed lagged betas (Dimson; Scholes–Williams; Chapter 8) and inflate by $\phi_i^{-\xi}$, where $\xi\in[0.5,1]$ is calibrated on bonds whose print frequency changed.

*Shrinkage.* Ledoit & Wolf (2004, "A Well-Conditioned Estimator for Large-Dimensional Covariance Matrices," *JMVA* 88(2)) shrink the sample matrix $S$ toward a target $F$: $\Sigma^{\text{LW}}=(1-\delta)S+\delta F$, with optimal intensity

$$
\delta^\star=\max\Big\{0,\min\Big\{1,\;\frac{\hat\pi-\hat\rho}{\hat\zeta\,T_{\text{obs}}}\Big\}\Big\}.
$$

Here $\hat\pi$ sums the asymptotic variances of the entries of $S$, $\hat\rho$ is their covariance with the target, and $\hat\zeta=\lVert S-F\rVert_F^2$ is the misspecification. Ledoit and Wolf call that last quantity $\gamma$; we rename it because $\gamma$ is risk aversion. With the factor model as the target, shrinkage amounts to a ridge $\tau^2$ on the idiosyncratic block. Putting the pieces together, the idiosyncratic variance over the horizon is

$$
d_i \;=\; \sigma^2_{\epsilon,i}\,\big(T+\kappa\,a_i\big)\,\phi_i^{-\xi}\;+\;\tau^2 .
\tag{19.5}
$$

For line 42 ($a=40$, $\phi=0.05$, $\kappa=\xi=0.5$, $T=5$) the bracket and the inflation multiply the naive $\sigma^2_\epsilon T$ by $(25/5)\times\sqrt{20}\approx22$. The engine is not saying line 42 is a bad bond. It is saying nobody knows what line 42 is worth, and pricing that ignorance.

> **[SOURCE EXTRACTION]** *Paleologo_Advanced_Portfolio_Management p.186:* "It is possible to obtain the same solution starting from different assumptions. The first one is the linear Ledoit-Wolf shrinked covariance matrix approach [Ledoit and Wolf, 2003]."
>
> **Annotation.** Paleologo's point is that several roads (linear shrinkage, a ridge penalty, a Bayesian prior on idiosyncratic variance) lead to the same regularized matrix. For a PT engine that is a licence to choose the road that can be *audited*. A ridge $\tau^2$ that rises with a line's staleness is something a trader can read and challenge ("why is line 42's $\tau$ so big?"), while a global $\delta^\star$ is not. The equity setting has daily closes for every name. Credit has 150 lines and a dozen prints, so the factor target carries most of the weight, and the shrinkage intensity for the median HY line is close to one.

> **[SOURCE EXTRACTION]** *Bohn_Stein_Active_Credit_Portfolio_Management p.48:* "Developing these strategies in the context of portfolio trades helps reduce the idiosyncratic impact of inexplicable behaviors of particular securities. A portfolio perspective complemented with quantitative systems sets the stage for generating high Sharpe… and Vasicek (return per unit of tail-risk contribution or return per unit of capital) ratios."
>
> **Annotation.** Two ideas for the risk term. First, diversification: the idiosyncratic block of $\mathbf{x}^\top\Sigma^{\text{res}}\mathbf{x}$ grows like $N$ while the notional grows like $N$, which is why the basket's per-dollar risk charge is far below the average line's standalone charge. Second, the Vasicek ratio names the right denominator for $\gamma$: capital, or tail-risk contribution. If the desk's capital is $z\,\sigma_W$ at a hurdle $\rho$ per year, matching $\tfrac12\gamma\sigma_W^2$ to the capital cost $\rho z\sigma_W T/252$ gives $\gamma=2\rho zT/(252\,\sigma_W)$. On illustrative numbers ($\rho=15\%$, $z=2.33$, $T=5$, $\sigma_W=\$500$k) that is about $3\times10^{-8}$ per dollar, roughly thirty times smaller than the $10^{-6}$ this chapter uses. The gap is what desks mean by "balance-sheet appetite." It is why $\gamma$ is backed out of won and lost PTs (the revealed-preference bid), not out of the capital plan. It is also why $\gamma$ jumps in stress, when SCOOS dealers cite balance-sheet availability as a very important decline reason.

> **Ways This Blows Up.** (1) A trader bumps one line's volatility by hand, and a negative eigenvalue appears. Re-project to positive semi-definite (PSD) and recheck the condition number after *every* edit. (2) A bond downgraded last week still carries last month's IG-sector loading. Refresh $B$ on rating-change events, not on a calendar. (3) Kaz's Gaussian: inflating line 117's $\sigma_\epsilon$ to "account for the LMT risk" both under-charges the jump (variance is the wrong moment) and over-hedges it (the hedge solve now thinks line 117 is noisy, not toxic). Jumps go in $\text{AS}$.

### Specification for AI Implementation (residual covariance)

The argument of §19.5 ends on a promise: nobody knows what line 42 is worth, and the engine should price that ignorance instead of hiding it. The usual hiding place is a haircut, a flat number a trader types into a spreadsheet at 3:00 p.m. that survives, unsourced, until the model review where the risk committee asks why one bond's price has a mystery in it. The alternative is to let staleness enter where uncertainty belongs, in the variance, through a formula a skeptic can read and challenge, and to build the result into a matrix that is guaranteed to be invertible. This is the matrix the hedge solve and the eviction loop will touch most often, so it is where the desk wants its guards.

Listing 19.4 turns equation (19.5) and the factor model of Listing 19.3 into the covariance matrix the rest of the chapter uses. `idio_var` takes each line's daily idiosyncratic variance and multiplies it by the horizon plus half the line's staleness in business days (`kappa_stale`, 0.5), then by the inverse square root of its print frequency (`xi`, 0.5), then adds a ridge `tau2` that defaults to zero. `build_residual_cov` feeds that vector into `joint_cov`, forms the Schur complement, passes it through `psd_project`, and refuses to return a matrix whose condition number exceeds $10^6$. `psd_project` symmetrizes, takes an eigendecomposition, lifts any eigenvalue below $10^{-10}$ of the largest up to that floor, rebuilds, and symmetrizes again. The inputs are a `Basket` plus the horizon, basis scale and staleness parameters. The outputs are $\Sigma_{xx}$, $\Sigma_{xf}$, $\Sigma_{ff}$ and the guarded $\Sigma^{\text{res}}$.

The asserts check four things. Every eigenvalue is positive. Line 42's residual variance is more than five times its naive value, which is the section's claim that staleness is variance and not a haircut. Every diagonal entry of $\Sigma^{\text{res}}$ is at least that line's own idiosyncratic variance. And Kaz's matrix, built from 14 observations on 150 bonds, has rank at most 13. On the synthetic basket, line 42 carries about three-fifths of the residual variance on 8.5% of the notional, and the risk charge at $\gamma=10^{-6}$ rises from about \$133k to about \$293k once staleness is priced *(illustrative)*.

Use it whenever the history is shorter than the book, which in credit is always. Do not ask it for jumps: line 117's lender call is not in this matrix, and §19.8 is where it gets charged. The edge case that bites is the projection. On a clean build it is a no-op up to rounding, because a Schur complement of a valid matrix is already valid. It earns its keep after a human edits the matrix by hand. Once it clips anything, `Sres` is no longer exactly the Schur complement, and the promise that $\mathbf{x}^\top\Sigma^{\text{res}}\mathbf{x}$ is the optimally re-hedged variance holds only approximately. Edit the inputs and rebuild. Do not edit the output.

*The full listing is [Listing 19.4 in Appendix F](#code-19-4).*

## 19.6 Eviction: Which Lines to Kick Out, and the Price of Keeping Them

The dealer's best tool is not a better bid. It is a counter-proposal. "Clients may get better pricing if they accept suggested portfolio tweaks," as IFR put it in 2021 (Whittall, "US banks reap boom in bond portfolio and algo trading"). Translated: *take back lines 42 and 117 and I'll pay you more for the other 148.* The ex-RSSG reader knows this move from the other side of the table. It is the plan sponsor carving the fulcrum class to get the vote. The engine's job is to find the carve in under a second.

### 19.6.1 Derivation: marginal cost, exact removal saving, greedy loop

Total cost of carrying the basket, collecting (19.2)'s cost terms:

$$
\mathcal{C}(\mathbf{x})=\sum_i c_i(x_i)+\tfrac12\gamma\,\mathbf{x}^\top\Sigma^{\text{res}}_T\mathbf{x}+\sum_i \text{AS}_i,
\qquad
\text{MC}_i\equiv\frac{\partial\mathcal{C}}{\partial x_i}=c_i'(x_i)+\gamma\big(\Sigma^{\text{res}}_T\mathbf{x}\big)_i+\frac{\partial\,\text{AS}_i}{\partial x_i}.
\tag{19.6}
$$

$\text{MC}_i$ is the vector inventory skew. Eviction is discrete, though, so we want the *exact* saving from setting $x_j$ to zero. Write $\mathbf{x}'=\mathbf{x}-x_j\mathbf{e}_j$ and expand the quadratic:

$$
\tfrac12\gamma\big(\mathbf{x}^\top\Sigma\mathbf{x}-\mathbf{x}'^\top\Sigma\mathbf{x}'\big)=\gamma\,x_j(\Sigma\mathbf{x})_j-\tfrac12\gamma\,\Sigma_{jj}x_j^2 ,
$$

so

$$
\Delta_j \;=\; c_j+\text{AS}_j+\gamma\,x_j\big(\Sigma^{\text{res}}_T\mathbf{x}\big)_j-\tfrac12\gamma\,\Sigma^{\text{res}}_{jj}\,x_j^2 .
\tag{19.7}
$$

The gradient term double-counts the line's own variance, and the $-\tfrac12\gamma\Sigma_{jj}x_j^2$ correction removes it. Because $\Sigma^{\text{res}}$ is the re-hedged covariance (§19.4), $\Delta_j$ already includes the re-optimized hedge.

*The greedy step is a descent step.* Let $M=\sum_i \text{MV}_i$ be gross market value. Evicting $j$ lowers the per-dollar cost $\mathcal{C}/M$ if and only if $(\mathcal{C}-\Delta_j)/(M-\text{MV}_j)<\mathcal{C}/M$, i.e. $\Delta_j/\text{MV}_j>\mathcal{C}/M$. Summing (19.7) over $j$ gives

$$
\sum_j\Delta_j=\mathcal{C}+\tfrac12\gamma\sum_{i\ne j}x_i\Sigma^{\text{res}}_{ij}x_j .
$$

When the off-diagonal risk is nonnegative (a one-sided basket of positively correlated bonds), $\sum_j\Delta_j\ge\mathcal{C}$. The MV-weighted average of the ratios $\Delta_j/\text{MV}_j$ is then at least $\mathcal{C}/M$, so the largest ratio is too, and the best eviction always helps. The loop: rank by $\Delta_j/\text{MV}_j$, evict the top line, update $\Sigma\mathbf{x}\leftarrow\Sigma\mathbf{x}-\Sigma_{:,j}x_j$ in $O(N)$ (the coupling term changes after every eviction, so never sort once), and stop when $\mathcal{C}/M$ reaches the competitive target $\kappa^\star$, when evicted notional reaches the client's tolerance $\alpha$, or when the count reaches $k_{\max}$. The exact problem is a knapsack. Greedy is the 90-second answer, and with $k_{\max}\le10$ it is usually the right one.

*The buy-side mirror is the sweetener.* Adding a liquid, ETF-heavy line with $\Delta/\text{MV}$ below the basket average lowers $\mathcal{C}/M$, by the same inequality run backwards. That is Meli & Todorova's "crowd-sourcing liquidity": even among illiquid PTs, the median share of liquid bonds is 37%, so "the more liquid bonds cross-subsidize the less liquid bonds." Barclays found 49% of IG PTs but only 18% of HY PTs fit the crowd-sourcing pattern, because HY portfolios "need many more liquid bonds to offset illiquid ones, because the far tail of the LCS distribution is thicker in HY" (The DESK, 2022-06-01).

> **[SOURCE EXTRACTION]** *Dynkin_Systematic_Investing_in_Credit p.704:* "TES blend LCS and trading volume of a bond into a single relative score that reflects both the cost and flow. Bonds with higher trading volume and lower LCS per unit of duration have lower TES."
>
> **Annotation.** The Trade Efficiency Score is a ready-made prior for the eviction ranking. A high-TES line is expensive *and* rarely traded, which describes the residual nobody wants to own for five days. On the same page Dynkin notes that LCS varies widely across bonds even at a single date, "so rebalancing costs… greatly depend on its composition." That is the fat tail of §19.3 restated as a portfolio fact. Our $\Delta_j$ improves on TES in two ways. It prices *covariance with the rest of the basket* (a high-TES line that hedges the others is worth keeping), and it carries the AS term, which no liquidity score can see. Sorting by TES alone evicts line 42 and keeps line 117, which is exactly the mistake the next section is about.

### 19.6.2 Case Study: The H1 2022 Reversal

2021 had been PT's coming-out party. Then 2022 brought higher volatility, quantitative tightening, and a dealer community that had bought market share and now wanted margin back.

> **[SOURCE EXTRACTION]** *Man_Revolutions_in_Credit_Trading_2023 p.3:* "The new market environment of higher volatility and quantitative tightening may also have left dealers inclined to commit less of their balance sheets to bond trading. The loss of customised baskets for the ETF creation/redemption process is likely to have been another aggravating factor."
>
> **Annotation.** Man's p.3 opens the story: "transaction costs for portfolio trading generally increased through the first half of the year… ultimately pricing backed off." Read it as three terms of (19.2) moving together. Balance sheet withdrawn means $\gamma$ up, so the risk term grows. The loss of custom creation baskets closes the dealer's outlet for illiquid residue, so $c_i$ for the tail rises (Koont, Ma, Pástor and Zeng show bond ETFs tilt creation/redemption baskets toward illiquid bonds, so losing customization hits exactly those lines). Competition easing means $\pi$ rises. A dealer running this chapter's engine in Q1 2022 would have seen its eviction loop hit the $\alpha$ budget before reaching $\kappa^\star$ on HY baskets: the machine's way of saying *decline, or quote wide and lose*.

How a systematic desk would have read it in real time: hit rates on HY PTs falling at constant $\pi$ (competitors widening), the ETF-to-cash ratio and creation-basket composition shifting, and the ranking $\Delta_j/\text{MV}_j$ fattening in its top decile. The buy side adapted the other way. Man routed flow back to electronic RFQ (§19.9), which is the client's own eviction decision applied to the whole protocol. The SCOOS weights confirm the dealer side four years later. Composition is "very important" to four-fifths of active dealers, market conditions to two-thirds, and relationship and balance sheet to about one-half each. Composition is the eviction term, market conditions are $m$ and $\gamma$ (§19.7), and balance sheet is $\gamma$ again.

### Specification for AI Implementation (greedy eviction)

The counter-proposal has to be on Ines's screen before the response window closes, and it has to be right, because the client will take back exactly the lines the engine names. By feel, a trader can carve five lines out of a list of twenty. At 150 lines the cost of any one bond depends on all the others through the hedge residual, so the ranking changes after every removal. Sorting once and striking the top ten is wrong, and re-solving the whole hedge for each candidate is too slow for ninety seconds. The derivation gives an exact saving for each line and a cheap way to update the ranking after each eviction. What is left is a loop, which a desk automates precisely so that nobody argues about it while the clock runs.

Listing 19.5 is `evict_greedy`. It takes the `Basket`, the residual covariance from Listing 19.4, a vector `as_vec` of per-line adverse-selection charges in dollars, and the policy knobs: risk aversion `gamma`, the handling parameters, the liquidity multiplier `m`, a tolerance `alpha` for evicted market value (15% of gross), a cap `k_max` of ten lines and a cost target of 45bp of market value. Zeros are a legal value for `as_vec`, which is the trap the paragraph after the listing walks into. The function computes handling costs once, caches the coupling vector `Sres @ x`, and then loops. Each pass evaluates equation (19.7) for every line, divides by market value, masks out lines already evicted and lines too large for the tolerance still unspent, and picks the largest ratio. It stops if nothing is eligible or if the best ratio no longer beats the basket's current cost per dollar. Otherwise it subtracts one scaled column of `Sres` from the coupling vector, an $O(N)$ update, zeroes the line and recomputes. An assert inside the loop demands that the realized fall in total cost equals the predicted saving, so a later edit that breaks the algebra fails loudly. The outputs are the evicted indices in order and the path of cost per dollar. On the cold-open basket with no adverse-selection model, one eviction is enough: line 42 goes, and cost per dollar falls from about 55bp to about 32bp, under target *(illustrative)*.

Use it to build the counter-proposal before quoting, and on the buy side to see which lines you are paying the dealer to take. It is a greedy answer to a knapsack, which is fine at ten lines or fewer. The edge case that bites is the sign structure. The guarantee that the best eviction always helps assumes non-negative off-diagonal risk, a one-sided basket, and about a third of real baskets mix buys and sells. In a mixed basket, offsetting lines hedge each other, and a removal can raise the cost per dollar. The stop rule exists for that case. When it fires early, the engine is telling you the basket is cheaper whole than carved.

*The full listing is [Listing 19.5 in Appendix F](#code-19-5).*

Hold on to that last assert. The engine, run without an AS model, evicts the stale \$18mm line and is satisfied: the basket is now below its 45bp target, and line 117 stays in. Line 117 looks like a model citizen. Its realized volatility is ordinary, its LCS is unremarkable, and it diversifies nicely. Everything the covariance matrix can see about it is fine. That is the point.

## 19.7 Stress Liquidity Commonality: When Every $c_i$ Moves Together

In calm markets the four terms of (19.2) are small and nearly independent. In stress they collapse into one term. "In October 2008," Mags says, "we priced baskets by phone and by grudge, and the grudge was the only thing with a bid." Grudging respect follows: "Your matrix at least knows which bonds it can't sell. We had to find out one call at a time."

### 19.7.1 Derivation: a common multiplier in costs, a rank-one spike in risk

Let each line's cost carry a common liquidity multiplier: $c_{i,t}=\bar c_i\,m_t+\varepsilon_{i,t}$, with $m_t>0$, $m\approx1$ in calm markets, and $\log m_{t+1}=\varphi\log m_t+\xi_{t+1}$. The basket's liquidation cost is $L=m\sum_i\lvert x_i\rvert\bar c_i+\sum_i\lvert x_i\rvert\varepsilon_i$, with independent $\varepsilon_i$, so

$$
\operatorname{Var}(L)=\Big(\sum_i\lvert x_i\rvert\,\bar c_i\Big)^2\sigma_m^2+\sum_i x_i^2\,\sigma^2_{\varepsilon,i}.
\tag{19.8}
$$

The first term grows like $N^2$ and the second like $N$. **The liquidity factor does not diversify.** Adding lines to a basket dilutes idiosyncratic cost noise and leaves the common multiplier exactly where it was. The same shock moves prices: illiquid bonds fall more when $m$ jumps, by about $g_i=-\theta\,\text{LCS}_i\widehat P_i$ per unit of $m$. Nothing in the hedge menu spans $m$ (§19.4), so it survives into the residual as a rank-one spike:

$$
\Sigma^{\text{res}}_{\text{stress}}=\Sigma^{\text{res}}_{\text{calm}}+\sigma_m^2\,\mathbf{g}\mathbf{g}^\top .
\tag{19.9}
$$

Because $\mathbf{x}^\top\mathbf{g}\mathbf{g}^\top\mathbf{x}=(\mathbf{g}^\top\mathbf{x})^2$, a one-sided basket of illiquid bonds has the spike at full strength. A mixed buy/sell basket nets it, which is one more reason dealers love two-way baskets. The persistence parameter comes from recovery half-lives $h$ in weeks, $\varphi=2^{-1/h}$. The March 2026 episode's 4–14-week half-lives (below) give weekly $\varphi\in[0.84,0.95]$. So stress lasts longer than any PT unwind horizon, and the dealer cannot simply wait it out.

> **[SOURCE EXTRACTION]** *Ben_Dor_Quantitative_Credit_Portfolio_Management p.112:* "Over this time period, the LCS for the IG Index ranged from 0.59% to 3.40%. Although the spike in illiquidity that occurred in October 2008 is painfully clear, the index's LCS values had already doubled between June 2007 and September 2007, in the very early stages of the credit crisis."
>
> **Annotation.** Here are two calibration targets and one warning. The range $3.40/0.59\approx5.8$ is the empirical ceiling for $m$ at the *index* level, and the regime map below hits exactly 5.8 at its cap. With the LCS–VIX correlation of 0.90 (p.166), it licenses a one-factor liquidity model keyed to observable stress. The warning is the second sentence: LCS doubled *months before* the obvious crisis. A regime trigger keyed only to headline volatility arrives late. Key it to the cost data itself (bid–ask percentiles, ETF discounts) and expect $m$ to drift up before it jumps. Cotelioglu (2024, *Journal of Empirical Finance* 78) adds the mechanism a 2026 desk must respect: ETF ownership raises liquidity *commonality* in IG bonds. The plumbing that makes the lump cheap to hedge in calm markets also makes the residue's costs move together in stress.

> **Trend Watch: PT in four stresses.** *March 2020:* Meli & Todorova's initial results show PTs "did not have lower transaction costs during March 2020, when volatility spiked due to the Covid-19 outbreak, and flows were one-sided." Bond ETF tracking error exceeded 200bp against a 0.7bp average (Todorov, BIS, 2021). *H1 2022:* PT costs rose as dealers committed less balance sheet and custom creation baskets disappeared (Man_Revolutions_in_Credit_Trading_2023 p.3; §19.6.2). *April 2025:* the tariff shock produced record volume days with 12% of 2025-04-08 volume via PT, and \$99bn of fixed income ETFs traded on 2025-04-07. On net, only one-fifth of active PT dealers said their willingness to do PT (relative to single-name market making) "decreased somewhat" (SCOOS, June 2025). *March 2026:* EUR IG bid–ask spiked 64% above its January average. Recovery took about 4 weeks in EUR IG, 6 in US HY, 8 in US IG, 13 in EUR HY and 14 or more in EM (MarketAxess data via The DESK, 2026-10-01). *What it means:* each episode is a jump in $m$ and $\gamma$, and the protocol's resilience has improved. In 2020 PT lost its cost edge outright. In 2025 most dealers kept quoting, with wider parameters.

### 19.7.2 Case Study: March 2020 and the April 2025 Tariff Week

In **March 2020** all three stress channels fired at once. Flows were one-sided, so the spike in (19.9) hit at full strength, with no two-way netting. The ETF basis that the hedge relied on became the largest residual ($\sigma_u$ in §19.4 went from negligible to dominant). Dealer $\gamma$ jumped with balance-sheet constraints. The result is the Meli–Todorova finding above: the protocol's cost advantage vanished in exactly the weeks clients most wanted certainty. A desk running this engine would have watched its regime score hit the cap, its eviction loop exhaust the $\alpha$ budget on every HY basket, and its quotes widen until they stopped winning. That is the correct outcome. A PT engine that keeps winning in March 2020 at calm-market prices is subsidizing its clients' exits with its own capital.

**April 2025** was the first stress the mature PT infrastructure came through. Volume set records, PT kept a double-digit share of the record day, and ETFs absorbed the price-discovery role on 2025-04-07. In SCOOS terms, a *net* one-fifth of dealers pulled back somewhat: a dent, not a collapse. Two differences from 2020 show up in the engine's inputs. First, the hedge stack was deeper (CDX, TRS and, soon after, listed credit futures), so the basis variance did not have to sit in a single ETF. Second, buy-side automation stayed on with "stress parameters" rather than switching off, so baskets kept arriving two-way enough to net part of the spike. The upstream lesson for the engine is that $m$, $\gamma$ and the basis multiplier must move *together* from one regime score. Calibrating them separately produces an engine that is calm about costs and panicked about risk, or the reverse, and either one is wrong.

### Specification for AI Implementation (regime and stress covariance)

The case studies end on a rule that sounds easy and is not: the cost multiplier, the dealer's risk aversion and the ETF basis must move together, from one regime score. The org chart works against it. The execution team owns the cost dial, the risk team owns the risk-aversion dial and the ETF desk owns the basis dial, each calibrated in a different quarter by a different person, and the quote that comes out is calm about costs and panicked about risk, or the reverse. A model review cannot tie three free dials to anything the committee can look at. So the desk builds one score from two things anybody can read off a screen at 3 p.m. without calling a counterparty: how deep the credit ETFs trade below their NAV, and where today's bid-ask sits in its own history. One score, three multipliers, no argument about whose dial it is.

Listing 19.6 has two functions. `regime` maps the ETF discount z-score and the bid-ask percentile to a stress score $s\in[0,2]$. The ETF channel is zero until the z-score falls below $-1$ and then adds one third per standard deviation, reaching 1 at $-4$. The bid-ask channel is zero until the percentile passes 80% and then rises linearly to 1 at the 100th. The two add, capped at 2. The score drives three multipliers, each a straight line in $s$: liquidity `m = 1 + 2.4 s`, risk aversion `1 + 1.5 s` and basis `1 + 2 s`. At the cap, `m` is 5.8, the ratio of Ben Dor's 3.40% to 0.59% IG LCS range *(illustrative calibration)*. The example in the asserts, a discount of 2.5 standard deviations and a 90th-percentile spread, scores exactly 1, which means `m` of 3.4, risk aversion 2.5 times calm and basis 3 times calm.

`stress_cov` implements (19.9). It builds the vector $g=-\theta\,\text{LCS}\times\text{mid}$ with $\theta=0.8$ *(illustrative)* and adds $(0.25s)^2\,gg^\top$ to the calm residual covariance, so the liquidity shock's volatility grows with the score. The result is the calm matrix plus exactly one rank. The asserts check that the spike is rank one and that it does not diversify. At $s=1$ on the cold-open basket it makes up about 28% of the basket's variance but only about 2% of the sum of the line variances, which is equation (19.8) in two numbers.

Use it to widen the quote continuously instead of flipping a stress switch, and remember that it is a thermometer, not a forecast. The edge case that bites is the dead zone. Below a one-sigma discount and the 80th percentile, `regime` returns exactly 1.0 on every multiplier, and a premium never counts at all. Ben Dor's warning in §19.7.1 is that LCS doubled months before the obvious crisis, so a map with flat floors will sit calm while the cost data drifts up. Move the thresholds, or add a slow-moving cost input, before relying on it.

*The full listing is [Listing 19.6 in Appendix F](#code-19-6).*

## 19.8 Adverse Selection in Baskets: The Mystery Box

> **Poker Table.** "In a single-name RFQ," Ines says, "the player chose to bet. In a basket the player also chose *which cards to put face down among 150 face up*. You can't see the face-down cards. You can count how often this player has shown you a hand like this, and where it cost you." A PT is a bundle of 148 face-up cards that pay for the privilege of hiding two. The client is not cheating. That is the game. The dealer's edge is knowing which seats at the table hide cards, and what the cards usually are.

Glosten–Milgrom (Chapter 18) says the dealer's bid for one bond is $\mathbb{E}[V_i\mid\text{client sells }i]$. In a basket, the conditioning event is richer: the client sold *this bundle*, and chose to include line $i$. The good news is in the evidence. Li (2022) finds that PT-versus-voice cost differentials in IG do not respond to private-information proxies, so in IG baskets the inclusion signal is weak and a small AS charge suffices. The bad news is HY, where a line with an ad hoc group forming and a lender call on Monday is exactly the kind of card a well-informed seller hides in a stack of 149 others. For the ex-RSSG reader this is home turf. The toxicity features are Chapter 13's Priming Risk Score, the docket and the credit agreement.

### 19.8.1 Derivation: the inclusion model and the AS charge

Let $I_i$ indicate that line $i$ was included *because* the client holds adverse information. Model $\Pr(I_i\mid\mathbf{z}_i)=\sigma(\mathbf{w}^\top\mathbf{z}_i)$, logistic in observable toxicity features $\mathbf{z}_i$: PRS, proximity to a lender call, a live ad hoc group or Rule 2019 statement, log size relative to the basket median, and (in production) the client's own markout history in the name. Conditional on $I_i$, the expected informed move is $J_i$ (fraction of par), and otherwise zero. Then

$$
\mathbb{E}^{\mathbb{P}}\big[\widetilde P_{i,T}\mid i\in\mathcal{B},\mathbf{z}_i\big]=\widehat P_i-\Pr(I_i\mid\mathbf{z}_i)\,J_i\,\widehat P_i ,
\qquad
\text{AS}(\mathcal{B})=\sum_{i\in\mathcal{B}}\text{MV}_i\,\Pr(I_i\mid\mathbf{z}_i)\,J_i .
\tag{19.10}
$$

This is the first moment of the jump that Step 2 of §19.2 warned mean–variance would miss. Put the jump in the mean and the skew stops hiding. For a dealer *sell* (the client buys), the informed move is up, and the same charge applies with the sign of $J_i$ flipped. Two cautions. Charge AS to the *flagged tail*, not uniformly: a uniform AS charge kills the quote and still under-charges the one line that matters. And winner's-curse shading in $\pi$ is a separate, basket-level adverse-selection term (other dealers' information about the *whole* basket). Do not fold one into the other.

*The hand history.* The diagnostic is the by-line markout, net of the hedge:

$$
\text{MO}_i(\tau)=x_i\big(\widehat P_{i,t+\tau}-p_i\big),\qquad \tau\in\{1,5,20\}\ \text{business days},
$$

measured on the residual after the factor and hedge P&L are stripped out. IDO or it didn't happen: a basket-level markout averages away the two lines that matter, and an unhedged markout is mostly the market. The "two cards face-down" signature is realized AS concentrated in one or two lines, at a scale far outside their idiosyncratic volatility.

### 19.8.2 Case Study: The Mystery Box at Line 117 (illustrative)

Every number in this case is *illustrative*. The mechanics are anchored in the real liability-management transactions of Chapter 13, such as the Serta Simmons 2020 uptier, in which a majority group exchanged into new super-priority debt under the agreement's "open market purchase" language (the most expensive three words in finance) and excluded lenders' first-lien paper repriced sharply. Chapter 13 has the sourced price path. Our line 117 is a fictional issuer with the same fact pattern: PRS 0.85, an ad hoc group with a live 2019 statement, and a lender call in three business days. Theo's 13-week model, now a liquidity-runway input to PRS, puts the cash cliff about a quarter out.

The engine's inclusion model puts $\Pr(I_{117})\approx0.75$, against a median line's 1%. With $J_{117}=1\%+15\%\times0.85\approx13.75$ points, the AS charge is about $3.28\text{mm}\times0.75\times0.1375\approx\$0.34$mm. That is roughly 16bp of the whole basket's market value, from a line with 1.6% of it. Add the stale line 42 and two lines with about 10% of the market value carry, by hand arithmetic, more than half of the basket's total cost: roughly 74bp all in, falling to about 35bp once both are evicted. (These are hand estimates on the synthetic basket. Your run will differ in the second digit.) These are the two lines paying for the whole trade.

The counter-proposal writes itself: *we bid the 148 at a 35bp concession; lines 42 and 117 we will work separately, or not at all.* The client's response is itself information. A client who says "fine, keep the rest" was rebalancing. A client who says "all or none, final" may be telling you which card is face down. Five business days later, the hand history settles it.

### Specification for AI Implementation (adverse selection and hand history)

Everything the covariance matrix knows about line 117 is reassuring, and everything Theo knows about it is in his head, the credit agreement and a docket. That is a bad place to keep a number the desk charges for. When Theo is on vacation, the engine has to ask the same question he would ask, in dollars, in under a second. And afterward, when the basket has settled, the desk needs a record of whether the suspicion paid off, because a suspicion that is never scored cannot be calibrated. The charge before the trade and the markout after it are two halves of one control loop, and a desk that builds only the first has an opinion, not a model.

Listing 19.7 has those two halves. `as_charge` implements equation (19.10) in three steps. It first turns the toxicity features into inputs: PRS, a `call_soon` term equal to $e^{-\text{days}/5}$ (zero when no call is on the calendar and approaching one as the call nears), the ad hoc flag, and the log of the line's size relative to the basket median. A logistic function with hand-set weights then gives the probability that the line is in the basket because the client knows something. The constant of $-5$ puts a quiet line below 1%. Finally the probability is multiplied by market value and by an informed move of one point plus fifteen points times PRS. It returns the dollar charge and the probability for every line. The weights are *illustrative*, and nothing in the listing fits them. On the cold-open basket line 117 comes out at a probability of 0.75 against a median of 1%, and a charge of about \$339k, which is 81% of the basket's total. Hand that vector to the loop in Listing 19.5 and the order flips: line 117 is evicted first, then line 42, and cost per dollar falls from about 76bp to 59bp to 36bp *(illustrative)*.

`markouts` is the second half. For each line and each horizon of 1, 5 and 20 business days it returns signed notional times the later mid minus the traded price. The example draws 149 lines of noise scaled to their own idiosyncratic volatility, drops line 117 by 1, 5 and 14 points, and asserts that line 117 has the worst per-dollar markout at 20 days.

Use the charge before quoting, the markout after settling, and the pile of markouts to refit the weights by client. The edge case that bites is in the docstring: `markouts` takes its mid path as given and strips nothing out. It assumes the factor and hedge P&L are already removed. Feed it raw mids and the market's own moves swamp the one line that matters, and you will conclude that the client is fine and the hedge is broken.

*The full listing is [Listing 19.7 in Appendix F](#code-19-7).*

Replayed through the markouts, Ines's hand history reads the way she expected: 149 lines of noise and one line with a 17% per-dollar loss at 20 days. The basket-level markout, averaged over \$200mm, would have called it a mildly unlucky week.

### Deep-Dive Resource Graph

**Practitioner Writing**

- IFR (2021), Christopher Whittall, "US banks reap boom in bond portfolio and algo trading": https://www.ifre.com/bonds/1968608/us-banks-reap-boom-in-bond-portfolio-and-algo-trading

**Academic Papers**

- Li, O'Hara, Rapp & Zhou (2023), "Bond Market Illiquidity: Is Portfolio Trading the Solution?" (SMU Scholar record): https://scholar.smu.edu/business_finance_research/251
- Koont, Ma, Pástor & Zeng, "Steering a Ship in Illiquid Waters: Active Management of Passive Funds," NBER WP 30039; *Review of Financial Studies* (2025): https://www.nber.org/papers/w30039
- Cotelioglu (2024), "Do mutual funds and ETFs affect the commonality in liquidity of corporate bonds?" *Journal of Empirical Finance* 78: https://ideas.repec.org/a/eee/empfin/v78y2024ics0927539824000550.html
- Glosten & Milgrom (1985), "Bid, Ask and Transaction Prices in a Specialist Market with Heterogeneously Informed Traders," *Journal of Financial Economics*.

**Data & Code**

- scikit-learn `LedoitWolf` reference: https://scikit-learn.org/stable/modules/generated/sklearn.covariance.LedoitWolf.html

## 19.9 The Buy Side: When to Use a PT, and How to Build One the Dealer Will Love

Here is the second aha. **The PT premium is the shadow price of all-or-none certainty.** Man moved its flow *into* PTs in 2021 and *back out* to RFQs in 2022–23, and both decisions were right.

> **[SOURCE EXTRACTION]** *Man_Revolutions_in_Credit_Trading_2023 p.4:* "Two of the key challenges for such systematic techniques are having a high certainty of execution and having a relatively good sense of the likely transaction costs, as quantitative approaches depend on being able to model accurately which securities can be traded and at what cost. Furthermore, unfilled orders may create unintended and potentially unmodelled risk exposures in the portfolio."
>
> **Annotation.** The second sentence is the whole buy-side case for PT, and it can be priced. A partially filled rebalance leaves a random residual portfolio that the optimizer never chose. Its risk is real, and its cost is measured in tracking error, not bid–ask. The modern quant buy side therefore runs *both* routes through the same transaction-cost model and lets an inequality pick, rather than a relationship or a habit. Man's own p.5 verdict ("The vast majority of our trades are now sent as RFQs") is that inequality evaluated on a book whose electronic fill rates had risen.

### 19.9.1 Derivation: the all-or-none inequality

Take a target program $\mathbf{x}$. The RFQ route fills line $i$ with probability $\phi_i$ at cost $c^{\text{RFQ}}_i$, leaving a random unfilled residual $u_i=(1-\mathbb{1}_i)x_i$, with $\mathbb{1}_i\sim\text{Bernoulli}(\phi_i)$ independent. The PT route fills everything at $\sum_i c^{\text{RFQ}}_i+\Pi$. With the buy side's own risk aversion $\gamma_B$ and covariance $\Sigma$ over the time to re-trade, $\mathbb{E}[u_iu_j]=x_ix_j(1-\phi_i)(1-\phi_j)$ for $i\neq j$ and $x_i^2(1-\phi_i)$ for $i=j$. So

$$
\mathbb{E}[\mathbf{u}^\top\Sigma\mathbf{u}]=\sum_{i\ne j}x_ix_j(1-\phi_i)(1-\phi_j)\Sigma_{ij}+\sum_i x_i^2(1-\phi_i)\Sigma_{ii},
$$

and the PT is worth it if and only if

$$
\Pi\;\le\;\tfrac12\gamma_B\,\mathbb{E}[\mathbf{u}^\top\Sigma\mathbf{u}]\;+\;\sum_i(1-\phi_i)\,c^{\text{retry}}_i\;+\;\text{Leak}(N),
\tag{19.11}
$$

where $c^{\text{retry}}_i$ is the expected extra cost of re-trading an unfilled line and $\text{Leak}(N)$ is the information cost of showing $N$ separate RFQs to the street (Chapter 18). As $\phi_i\to1$ the right-hand side goes to zero and no premium is worth paying. That is 2022–23, when electronic RFQ fill rates and no-touch execution rose (Trumid reports 88% of eligible RFQ line items executed fully no-touch, The DESK, 2025-10-08). In 2021, $\Pi$ was competed toward zero (§19.1), and the inequality held almost everywhere. Man's switch is (19.11) flipping sign, a calculation and not a mood.

*Build the basket the dealer will love.* Every lever moves a term of (19.2). Hedgeability: an interquartile increase in a portfolio's correlation with LQD improves PT execution by 12%, and an interquartile increase in ETF ownership by 15% (Meli & Todorova). Sweeteners: liquid lines lower $\mathcal{C}/M$ (§19.6). Timing: month-end and index-rebalance flow is standardized basket demand. On MarketAxess in 2022 year-to-date, PT share was 7% higher in the last three days of the month, and 67% higher in 2021 (The DESK, 2022-11-08). Competition: send to enough dealers to compress $\pi$, but not so many that the basket leaks. BlueBay's Campbell put the cost of a lost PT bluntly: "one house now knows my intentions" (The DESK, 2019-10-06). And keep the best-execution file per line. Amundi's Minieri, in the same piece: "every line needs to be justified." The engine's per-line $\Delta_j$ is that justification, already computed.

## 19.10 Engineering for 90 Seconds

Here is the third aha. **"Ninety seconds" is a data-architecture statement, not a compute statement.** The product $\mathbf{x}^\top\Sigma\mathbf{x}$ for $N=150$ is 22,500 multiply-adds, which a phone does in microseconds. The ninety seconds go to *staleness*: whether line 83's composite is from today, whether its LCS applies at this size, whether its loading still reflects last week's downgrade, whether the hedge basis is quoted *now*. Everything $O(N^2)$ over the universe, or $O(\text{universe})$, is precomputed overnight and refreshed on events. The live path is lookups, one Schur complement, one quadratic form, a $2\times2$ to $5\times5$ hedge solve and a greedy loop. Pricing a PT in 90 seconds is 89 seconds of precomputation and human judgment, and one second of linear algebra. (The 90-second figure is this book's design target, not a sourced market statistic.)

| Step | Where it lives | Cost | Budget |
| :--- | :--- | :--- | :--- |
| Resolve 150 ids against the security master | precomputed index | $O(N)$ lookups | < 50 ms |
| Composite mid, `age`, `print_frac` | intraday cache, event-refreshed | $O(N)$ | < 50 ms |
| LCS at size, loadings $B$, $d_i$, PRS features | overnight + rating/docket events | $O(NK)$ | < 10 ms |
| $\Sigma^{\text{res}}$: Schur complement, PSD projection, condition guard | live | $O(N^2K+N^3)$ | < 50 ms |
| Hedge solve, AS model, greedy eviction ($k\le10$) | live | $O(H^3+kN^2)$ | < 30 ms |
| Human review: the flagged lines only | Theo and Ines | – | about 60 s |
| Slack for re-pulling stale composites and re-quoting | desk | – | about 25 s |

> **Trend Watch: from 30 minutes to 90 seconds.** *2019:* a dealer could return a live, executable basket quote in about 30 minutes, and about eight to ten dealers could price baskets at all (The DESK, 2019-10-06). *2021:* "A client can sell hundreds of securities, sometimes over US\$2bn in an hour." Morgan Stanley's algorithmic pricing engine, live since 2017, had grown from about 500 bonds to more than 10,000 (IFR, 2021). *2024:* investors "expect near-instant liquidity, so dealers must price and quote faster than a human can by point-and-click" (Coalition Greenwich, 2024-06-11). *2025–26:* Trumid executed 88% of eligible RFQ line items fully no-touch (September 2025). Buy-side desks such as Vanguard automate about 70% of traded volume but switch the robots to "stress parameters" when markets gap (The DESK, October 2026). *What it means:* about a 20× compression in six years, delivered almost entirely by precomputation and cached fair values, not by faster arithmetic. The binding constraint now is data freshness and the kill switch.

**What ROBO built from the vague version.** Theo asked ROBO to "price the basket fast." ROBO cached yesterday's composites, skipped the staleness fields because they slowed the parse, and returned a confident bid in four milliseconds. Eleven lines had not printed in a month. It was fast. It was also an answer to a question nobody had asked.

**The precise spec** adds kill switches. Refuse to auto-quote if more than 20% of gross MV has `age > 10`. Require human sign-off if regime score $s\ge1$, if any line has $\text{PRS}>0.7$, or if any line carries more than 25% of total cost. Refuse outright if the condition guard fails. Log the four-term decomposition for every quote, won or lost, because losing quotes are how $\gamma$ and $\pi$ get calibrated.

### Specification for AI Implementation (the full engine)

Seven listings in, the engine is still a parts bin. The product the desk sells is one call: the inquiry and two readings off the tape go in, and a price, a list of lines to hand back, a hedge and a reason come out, all inside the budget in the table above while Theo and Ines review the flagged lines. That call also has to leave a record. The quotes the desk loses are the only data it will ever get on $\gamma$ and $\pi$, so every quote, won or lost, gets its four-term decomposition logged. The last listing is therefore deliberately dull. It calls everything above in order, and the interesting part is what it hands back.

Listing 19.8 is `price_pt`, which runs the chain in the order the chapter built it. It reads the regime from the ETF discount and the bid-ask percentile, and scales risk aversion and the liquidity multiplier by it. It builds the residual covariance with the regime's basis multiplier (Listing 19.4), adds the liquidity spike if the score is above zero (19.6), computes the adverse-selection charges (19.7) and runs the greedy loop unless told not to (19.5). It then drops the evicted lines, re-solves the hedge on the survivors, and assembles the four terms of (19.2) in dollars: handling, risk, adverse selection and hedge half-spread. The output is a dictionary with the cash for the kept basket (fair value less cost), each term, the cost in basis points of kept gross market value, the hedge, the evicted ids, a `hit_target` flag, the regime and the elapsed milliseconds.

The asserts walk the whole chapter. The bid sits below fair value, and the four terms sum to the cost. The calm run evicts L117 and then L042 and meets the target, and the counter-proposal costs less per dollar than the full basket. The same basket at a regime score of 1 costs more than twice as much. The client-buys mirror image has an identical cost and an ask above fair value. On the cold-open basket, the full list costs about \$1.56mm, or 76bp: \$829k of handling, \$420k of adverse selection, \$293k of risk and \$16k of hedge. Without lines 117 and 42 it costs about \$0.67mm, or 37bp *(illustrative)*.

Use it as the core of the live path and as the replay engine for lost quotes. The edge case that bites is that the listing ends at the number. Of the kill switches in the spec above, only the condition guard is coded, and it raises. Nothing refuses a quote on stale composites, a PRS above 0.7 or a regime score of 1. The function reports them through `hit_target` and `regime`, then returns a confident cash figure anyway. In stress, ten evictions are not enough, `hit_target` goes false, and the number still arrives with a straight face. Adverse selection and the hedge half-spreads are also not scaled by the regime. A wrapper must read those flags and decline or escalate.

*The full listing is [Listing 19.8 in Appendix F](#code-19-8).*

### Deep-Dive Resource Graph

**Practitioner Writing**

- Coalition Greenwich (2024-06-11), Kevin McPartland, "Corporate Bond Dealers Focus on Trade Automation": https://www.greenwich.com/node/150811
- Coalition Greenwich (2026-02-17), Kevin McPartland, "Dealer net short in corporate bonds sets record": https://www.greenwich.com/node/158326

**Data & Code**

- MarketAxess monthly volume release, May 2026, with the estimated share of US credit portfolio trading: https://s201.q4cdn.com/767283836/files/doc_news/2026/06/05_2026_Volume_Release-Final.pdf

## 19.11 Desk Debrief

- **A PT bid is four terms plus a margin:** fair value, minus liquidation cost, minus residual risk *after the hedge*, minus adverse selection, minus $\pi$. Every term is in dollars until the very last line.
- **You are pricing one lump and a residual.** The hedge turns $\Sigma$ into $\Sigma^{\text{res}}$, and $\Sigma^{\text{res}}$ is the re-hedged covariance for *any* basket, so eviction re-hedges for free.
- **LCS is a standalone price.** Use only its handling share inside a basket, scale it for size, and never multiply it by duration again.
- **Staleness is variance, not a haircut.** Line 42 is not a bad bond; nobody knows what it is worth, and that ignorance is what the engine prices.
- **Evict on exact removal savings, and recompute after every eviction.** Liquidity scores evict line 42. Only the AS term evicts line 117.
- **The liquidity factor does not diversify.** In stress, one regime score must move $m$, $\gamma$ and the basis together.
- **The hand history is by line and net of the hedge.** A basket-level markout averages away the two cards that were face down. IDO or it didn't happen.
- **Ninety seconds is 89 seconds of precomputation and judgment, and one second of linear algebra.**

### The Spec You Hand the Robot

> Build `price_pt(inquiry, model_state, market_state) -> Quote`. **Inputs:** a struct-of-arrays inquiry ($N\le500$ lines: id, signed par \$, composite mid as a fraction of par, age in business days, print fraction, LCS at \$4mm, OASD, OAS, sector, daily idiosyncratic vol, PRS, days to lender call, ad hoc flag). Also: overnight loadings $B$ $(N,K)$, factor covariance $\Omega$ $(K,K)$, hedge loadings $A$ $(H,K)$ and basis covariance $U$ $(H,H)$, plus live ETF discount z-score and bid–ask percentile. **Compute (all under $\mathbb{P}$, all in dollars):** handling cost (19.3); idiosyncratic variance with staleness, print-frequency inflation and ridge (19.5); $\Sigma^{\text{res}}$ by Schur complement (19.4), PSD-projected, with $\operatorname{cond}\le10^6$; the stress spike (19.9) from one regime score that also scales $\gamma$ and the basis; the AS charge (19.10) from a logistic inclusion model; greedy eviction on exact removal savings (19.7), stopping at the target cost per dollar, $\alpha$ of MV, or $k_{\max}$ lines; and the minimum-variance hedge of the kept basket. **Return:** cash, cost in \$ and in bp of gross MV, the four-term decomposition, hedge notionals, evicted ids, a `hit_target` flag and latency. **Refuse** if mids look like points, if more than 20% of MV has age $>10$, or if a guard fails. **Escalate to a human** if $s\ge1$, if any $\text{PRS}>0.7$, or if one line carries more than 25% of cost. **Tests:** CE matches Monte Carlo under Gaussian P&L; hedged variance equals the Schur form; costs are side-symmetric; eviction strictly lowers cost per dollar; stress cost is at least 2× calm on the reference basket; the live path runs in under 1 s.

### Exercises

1. **Find the two lines.** Using `price_pt(b0, evict=False)`, attribute total cost to lines with the exact removal savings (19.7). Show that their sum exceeds $\mathcal{C}$, and explain the excess using the off-diagonal term in §19.6. Then find the two lines with the largest $\Delta_j/\text{MV}_j$ without reading the cold open.
2. **The ETF goes to a 5% discount.** Suppose HYG trades at a 5% discount to NAV with a z-score of $-4$. Run the engine with `etf_disc_z=-4.0, bidask_pct=0.97`. Which term of (19.2) grows most? Does eviction still reach the 45bp target within $\alpha=15\%$? If not, what should the desk tell the client, and is "decline" a valid quote?
3. **ROBO and the stale universe.** Set every line's `age` to 30 and `print_frac` to 0.05, and price the basket. ROBO returns a number. Write the kill-switch test that should have stopped it, and decide whether it belongs in `Basket.__post_init__` or in `price_pt`.
4. **Kaz's springing lien.** Kaz proposes modelling line 117's priming risk by multiplying its `sig_idio` by 10 instead of using the AS term. Compare the two quotes and the two hedges. Explain, with Step 2 of §19.2, why the variance version both under-charges the jump and distorts $\mathbf{h}^\star$.
5. **Flip the inequality.** For a 150-line IG program with RFQ fill probabilities $\phi_i=0.9$, $\gamma_B=5\times10^{-7}$ per dollar, and $\Sigma$ from §19.5 over a one-day re-trade horizon, compute the maximum PT premium $\Pi$ the buy side should pay under (19.11), ignoring leakage. Then lower $\phi_i$ to 0.6 and recompute. Which year, 2021 or 2023, does each number describe?
6. **The mixed basket.** Make 50 of the 150 lines client *buys*. Show that the stress spike $(\mathbf{g}^\top\mathbf{x})^2$ shrinks, and explain why a dealer should bid tighter for a two-way basket even when every line's LCS is unchanged.

### Deep-Dive Resource Graph

**Podcasts**

- Bloomberg Professional, *Market Dialogues* (2025-07-07), "How is portfolio trading changing the fixed income landscape?" with David Krein, Anna Han and Shahaan Kazi: https://professional.content.cirrus.bloomberg.com/professional2023/insights/markets/how-is-portfolio-trading-changing-the-fixed-income-landscape/

**Practitioner Writing**

- Man Group (2023), *Revolutions in Credit Trading* (shelf: `Man_Revolutions_in_Credit_Trading_2023`).
- The DESK (2019-10-06), "The burgeoning portfolio trading business": https://www.fi-desk.com/trading-protocols-portfolio-trading-lynn-strongin-dodds/
- The DESK (2022-06-01), "Barclays: Portfolio trading 8% of US credit market volume": https://www.fi-desk.com/barclays-portfolio-trading-8-of-us-credit-market-volume/
- IFR (2021), "US banks reap boom in bond portfolio and algo trading": https://www.ifre.com/bonds/1968608/us-banks-reap-boom-in-bond-portfolio-and-algo-trading
- Meli & Todorova (2022), "Portfolio Trading: Part III — In Crisis and Calm," Barclays Research (title only).

**Academic Papers**

- Meli & Todorova (2023), "Portfolio Trading in Corporate Bond Markets": https://www.aeaweb.org/conference/2024/program/paper/a7z3SGGN
- Li, J. S. (2022), "Frictional Intermediation, Inventory Hedging, and the Rise of Portfolio Trading in the Corporate Bond Market": http://www.aeaweb.org/conference/2023/program/paper/9TfsndSa
- Li, O'Hara, Rapp & Zhou (2023), "Bond Market Illiquidity: Is Portfolio Trading the Solution?": https://scholar.smu.edu/business_finance_research/251
- Koont, Ma, Pástor & Zeng, "Steering a Ship in Illiquid Waters: Active Management of Passive Funds": https://www.nber.org/papers/w30039
- Cotelioglu (2024), "Do mutual funds and ETFs affect the commonality in liquidity of corporate bonds?": https://ideas.repec.org/a/eee/empfin/v78y2024ics0927539824000550.html
- Ledoit & Wolf (2004), "A Well-Conditioned Estimator for Large-Dimensional Covariance Matrices," *Journal of Multivariate Analysis* 88(2), 365–411.
- Almgren & Chriss (2000), "Optimal Execution of Portfolio Transactions," *Journal of Risk* 3(2).
- Dick-Nielsen, Feldhütter & Lando (2012), "Corporate Bond Liquidity Before and After the Onset of the Subprime Crisis," *Journal of Financial Economics* 103(3).

**Data & Code**

- Federal Reserve SCOOS, June 2025 (special questions on credit portfolio trading): https://www.federalreserve.gov/data/scoos/files/scoos_202506.pdf
- FINRA TRACE: Regulatory Notice 22-12 (portfolio-trade modifier, effective 2023-05-15) and Regulatory Notice 26-16 (affiliate indicator), via https://www.finra.org/
- scikit-learn `LedoitWolf`: https://scikit-learn.org/stable/modules/generated/sklearn.covariance.LedoitWolf.html
- MarketAxess monthly volume releases (estimated share of US credit portfolio trading): https://s201.q4cdn.com/767283836/files/doc_news/2026/06/05_2026_Volume_Release-Final.pdf

<!-- STATUS: COMPLETE -->
