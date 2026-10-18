# Chapter 28: What a Desk Head / Senior PM Must Know to Extract Maximum Alpha

<!-- WRITER PLAN (sections appended in order as drafted; resume after the last complete "## 28.x" section):
28.0 Cold open; 28.1 Risk, not capital (+ Trend Watch: the platform operating system); 28.2 Effective breadth when issuers cluster (code block 1);
28.3 Allocation across signal horizons (+ Trend Watch: the liquid overlay layer; code block 2); 28.4 Kelly with jump-to-default
(+ Case Study / Trend Watch: the 2026 CCC decompression; code block 3); 28.5 LVaR, days-to-liquidate and the 5x problem
(Case Study: Third Avenue 2015; code block 4); 28.6 Drawdown control and marking to bid (Case Study: March 2020 and March 2026; code block 5);
28.7 The leverage band and the kappa problem (code block 6); 28.8 Running ex-RSSG analysts alongside PhDs (Case Study: aligned signals; code block 7);
28.9 The PM dashboard (full Specification for AI Implementation, final block); 28.10 Desk Debrief, Spec You Hand the Robot, Exercises;
28.11 Deep-Dive Resource Graph. -->

## 28.0 Cold Open: The Keys to the Table

Thursday, 15 October 2026, 4:05 p.m. The ICE BofA US High Yield index has closed at an option-adjusted spread of 323 bp. Its CCC-and-lower subindex has closed at 1,278 bp, a day after its widest level in at least three years (FRED). The index looks bored. Its basement is on fire.

Ines drops a lanyard on Theo's keyboard. It says RISK, in a font chosen by Compliance.

"You're not an analyst anymore. You have four PMs, a \$2bn gross book, and a risk officer who marks to bid. What's the pot?"

Theo starts to say "two billion," hears how wrong it is on the way out, and stops. Ines nods. It is the first good thing he has done as a desk head.

Kaz rolls over with a laptop. "I ran Kelly on the book. Good news: it's very confident. It wants 93% of capital in one B3 name."

"Which name?"

"The one with the fattest spread."

Mags, from the corner, without looking up: "Back in my day the stop-loss was a phone call from the CFO. You could hear the drawdown in his breathing."

ROBO has posted to the desk channel. Asked last night to "maximize the book's Sharpe ratio," it has found the highest-Sharpe asset in the building: a 2027 IG bond whose matrix-priced mark has not moved in eleven weeks, because nobody has traded it. Realized volatility 0.4%, Sharpe 11. ROBO proposes moving the whole book into it. The arithmetic is fine. The volatility has not gone away. It is sitting in the mark, waiting for the first trade.

Theo puts his hand on the USB stick with the 13-week cash flow model on it, for emotional support, and asks the only question he trusts. "But what does the credit agreement say?"

"There isn't one," says Ines. "That's the job. You write it. How much risk, in which horizon, in which names, for how long, and with whom?"

By the end of this chapter you will be able to: set a leverage band for a credit book from its effective breadth, its DTS-scaled volatility and its liquidity cost; put each signal in the horizon and instrument tier where it survives its own transaction costs; size a default bet with Kelly when the bet has a jump, a recovery and a ruin boundary; compute liquidity-adjusted VaR and days-to-liquidate for a book of RFQ-traded bonds; run a drawdown rule you can defend, with the mark-to-bid shock budgeted inside the rule rather than discovered on top of it; and build a team whose breadth survives contact with its own hit rate.

## 28.1 Risk, Not Capital: The Desk Head's Accounting Identity

Theo's first instinct, inherited from four years of sources-and-uses tables, is to hand out dollars: \$500mm of gross to each of his four PMs, done by lunch. It is the wrong unit. A PM cannot spend dollars. A PM can only spend risk: volatility while the position is alive, drawdown when it goes wrong, and liquidity when it has to be sold. Dollars are what you get when you divide a risk budget by how risky the instrument is, and in credit that divisor changes by a factor of ten between a three-year A-rated bond and a CCC with a lender call on Monday.

> **[SOURCE EXTRACTION]** *Paleologo_Advanced_Portfolio_Management p.88:* "Return on GMV is performance relative to a capital budget. But the real scarce resource is not capital; it is risk."
>
> **Annotation.** Paleologo writes this for an equity long/short book, where it is already true. In credit it is truer, for two reasons. First, the dollar size of a position is a poor proxy for its risk, because a bond's volatility scales with its spread and its spread duration (DTS), so \$50mm of a 5-year BB and \$50mm of a 2-year CCC are different animals that happen to weigh the same. Second, credit has a third risk budget the equity book barely notices, which is liquidity: the cost and the time of getting out. A 2026 desk head allocates three numbers per PM (a volatility budget, a drawdown budget, and a liquidity budget expressed in days-to-liquidate and liquidation cost) and lets the dollars fall out. The rest of this chapter computes each of the three.

> **Desk Myth vs. Desk Reality.** *Myth:* "We allocate \$200mm to the HY PM." *Reality:* "We allocate the HY PM 6% annualized volatility on \$200mm of allocated capital, which is \$12mm of vol, a 7.5% drawdown limit, which is \$15mm, and no more than 20% of the book beyond 20 days to liquidate *(all illustrative)*. The \$200mm is the denominator the investor letter prints."

### The identity, and why credit needs three substitutions

A notational warning first. Paleologo writes $s$ for the Sharpe ratio and $L$ for leverage. In this book $s$ is a credit spread and $L = 1 - R$ is loss given default, and both letters are busy in this chapter. We write $\text{SR}$ for the book's Sharpe ratio and $G$ for gross leverage, $G = \text{GMV}/\text{NAV}$, and use these throughout.

Let the book have net asset value (allocated capital) $K$ and gross market value $\text{GMV} = G K$. Split the GMV into $N$ positions with GMV shares $w_i$, $\sum_i |w_i| = 1$. Let $\sigma_i$ be the annualized idiosyncratic volatility of position $i$, as a fraction of its market value. If the $N$ bets are independent and equal, $w_i = 1/N$ and $\sigma_i = \sigma$, the volatility of the book per dollar of GMV is

$$
\sigma_{\text{GMV}} = \sqrt{\sum_{i=1}^{N} w_i^2 \sigma_i^2} = \frac{\sigma}{\sqrt{N}}.
$$

The book earns its Sharpe ratio on that volatility, so its return on GMV is $\text{SR}\,\sigma/\sqrt{N}$, and its return on NAV is $G$ times that:

$$
r_{\text{NAV}} = G \cdot \text{SR} \cdot \frac{\sigma}{\sqrt{N}}. \tag{28.1}
$$

This is Paleologo's equation (10.1) in our letters. Rearranged, a desk that must earn at least $r_{\min}$ on NAV needs leverage of at least

$$
G \;\ge\; \frac{\sqrt{N}}{\sigma}\cdot\frac{r_{\min}}{\text{SR}}. \tag{28.2}
$$

Read (28.2) as a sentence: a well-diversified book of low-volatility bets needs a lot of leverage to pay anyone's salary. Diversification lowers the risk per dollar of GMV, and so it lowers the return per dollar of GMV, and the only way to earn the hurdle is to own more GMV. That is why the platforms run what they run (see the Trend Watch below), and why the ceiling on $G$ in §28.7 matters more than the floor.

Credit forces three substitutions into (28.1)–(28.2). Each gets a section.

1. **$\sigma \to \sigma_{\text{DTS}}$.** A bond's excess return over a short horizon is approximately $-D^{\text{spr}}_i\,\Delta s_i = -D^{\text{spr}}_i s_i\,(\Delta s_i/s_i)$. If relative spread changes $\Delta s_i/s_i$ have annualized volatility $\sigma_{\text{rel}}$, then

$$
\sigma_i \approx D^{\text{spr}}_i\, s_i\, \sigma_{\text{rel}} = \text{DTS}_i \cdot \sigma_{\text{rel}}.
$$

This is the empirical regularity of Ben Dor et al., below: the volatility of a bond scales with its DTS, not with its duration or its spread alone. A 5-year HY bond at 350 bp has $D^{\text{spr}} \approx 4.2$ years and $s = 0.035$, so $\text{DTS} \approx 0.147$; at $\sigma_{\text{rel}} = 0.35$ a year *(illustrative)*, $\sigma_i \approx 5.1\%$ of market value per year.

2. **$N \to N_{\text{eff}}$.** Three hundred bonds are not three hundred bets when they come from sixty issuers in eleven sectors (§28.2).

3. **The drawdown budget includes liquidity.** The ceiling on $G$ (§28.7) is set by how much the book can lose, and in credit a book can lose money with no change in any issuer's fundamentals, simply because the bid moves away from the mid (§28.5–§28.6).

> **[SOURCE EXTRACTION]** *Ben_Dor_Quantitative_Credit_Portfolio_Management p.50:* "a portfolio with a weighted spread of 200 bps and spread duration of two years is equally risky as a portfolio with a spread of 100 bps and spread duration of four years"
>
> **Annotation.** This is DTS doing in one sentence what a rating-bucket risk system needs a page of tables to approximate. Ben Dor and coauthors show that excess-return volatility rises roughly linearly in DTS, with a slope equal to the volatility of relative spread changes, which is why $\sigma_{\text{DTS}} = \text{DTS}\times\sigma_{\text{rel}}$ is the volatility we put into every sizing formula in this chapter. The modern departure is in the slope. $\sigma_{\text{rel}}$ is not a constant: it jumps in stress, and in 2026 it has been visibly higher for CCCs than for the rest of the index (§28.4). Estimate it by bucket and by regime, and carry the stress multiplier as a parameter ($\kappa$, §28.7). For a distressed issuer, the same authors note that managing DTS contributions becomes roughly equivalent to managing market weights (p.63): once the spread is large enough, the bond trades on price and recovery, and the DTS approximation hands the job over to the jump model of §28.4.

> **Trend Watch: The platform becomes the operating system, 2024–2026.** *What changed:* the multi-manager platform, with centrally set drawdown rules, pass-through costs and very large gross books, became the main buyer of idiosyncratic risk and the main employer of the people who produce it. *How big, with dates:* Cambridge Associates' review of 2024 audited statements (published 10 October 2025) found that "all reviewed multi-manager platforms" pass through additional expenses, ranging from 0.87% to 12.99% of assets with a median of 4.53%. For 2025, Millennium returned about 10.5%, Citadel's flagship about 10.2%, ExodusPoint about 18% and Schonfeld's flagship about 12.5%, against 16.5% for the S&P 500 (Hedgeweek relaying the FT, 5 January 2026). Point72 returned 18% and had expanded to 190 pods per Bloomberg, and HFR put industry capital at a record \$5.15trn, up \$642.8bn in 2025 (The Daily Upside, 23 February 2026). In March 2026, the Iran-war shock forced an unwind of crowded positions, and ExodusPoint, Balyasny, Citadel and Millennium gave up all or part of their January–February gains (Bloomberg, 2 April 2026). The Fed's May 2026 *Financial Stability Report* described hedge-fund leverage as "stable at record-high levels," concentrated in a small number of large funds. In September 2026 a Goldman Sachs prime-insights head said multi-strategy managers had attracted about \$500bn of additional assets over the past year, roughly 25% growth, while sector headcount rose only 10–11%, and cited a JPMorgan estimate of 645% average multi-strategy leverage (Hedgeweek, 15 September 2026). The drawdown convention is commonly reported rather than disclosed: per the WSJ as relayed by eFinancialCareers (5 December 2025), Millennium PMs who lose 5% of allocated capital "typically" have it halved, and those who lose another 2.5% are "usually" let go; the firm declined to comment. *What it means for the desk:* about a quarter more capital chasing about a tenth more PMs means each PM's risk is rationed by rule, and the rule binds before the alpha does. A rule shared across firms also produces shared behaviour: when everyone's 5% line is hit in the same week, everyone sells the same bonds. The engineering in this chapter is about making the alpha and the rule compatible *before* the week arrives.

## 28.2 Effective Breadth When Issuers Cluster

Theo's book has 300 bonds. Kaz's breadth calculation therefore says 300. Ines looks at the issuer column and asks how many hands Theo is actually playing. The answer turns out to be about forty, and the gap between 300 and 40 is the difference between an information ratio of 2.7 and one of 1.0 at the same 50.5% hit rate.

### The Fundamental Law in hit-rate form

Start where Paleologo starts. Each day, each of $N$ independent, equal-sized bets earns $+1$ unit with probability $p$ (the hit rate) and $-1$ with probability $1-p$. One bet has mean $2p-1$ and variance $1-(2p-1)^2$. Equal-weighted across $N$ independent bets, the book's daily return has mean $2p-1$ and variance $[1-(2p-1)^2]/N$. Annualizing with 252 days,

$$
\text{IR} = \frac{(2p-1)\sqrt{252\,N}}{\sqrt{1-(2p-1)^2}} \;\approx\; (2p-1)\sqrt{252\,N}, \tag{28.3}
$$

where the approximation drops a term that is within 0.1% of one for any hit rate a human will achieve ($p = 0.52$ gives $\sqrt{1-0.04^2} = 0.9992$). The right-hand side is Grinold's law with $\text{IC} = 2p-1$ and breadth $\text{BR} = 252N$.

> **[SOURCE EXTRACTION]** *Paleologo_Advanced_Portfolio_Management p.148:* "(Inf. Ratio) = [2 × (hitting probability) − 1] × √(252 × (effective number of stocks))"
>
> **Annotation.** The phrase that does the work is "effective number." In an equity book of 150 single names, the effective number is close to the Herfindahl count of positions. In credit it is not, because the unit of independent information is the issuer, not the bond, and issuers in the same sector default in the same recession. A hit rate of 52% across 300 bonds would give an IR of $0.04\sqrt{252 \times 300} = 11$, a number that should make any risk officer reach for the phone. Across 40 effective bets it gives $0.04\sqrt{252\times 40} = 4.0$, and across 6 effective bets (a book that is really six views on six sectors) it gives 1.6. The second and third numbers are the ones a credit desk has seen.

### Two definitions of effective breadth

Paleologo's practical measure is the Herfindahl of GMV weights.

> **[SOURCE EXTRACTION]** *Paleologo_Advanced_Portfolio_Management p.150 (Procedure 8.1):* "H = sum[%GMV²(stock i)] … (effective number of stocks) = 1/H"
>
> **Annotation.** $1/H$ answers "how many equal positions would have the same concentration as mine?" It ignores correlation, which is harmless when residual correlations are near zero, as they are after a good equity factor model. In credit, residual correlation is not near zero inside an issuer (five bonds of one capital structure move together because they share one default time $\tau$) and it is not zero across issuers in the same sector and rating bucket. Use $1/H$ on issuer-netted weights as the floor of your breadth reporting, and the covariance-aware measure below as the number that goes into (28.2) and (28.3).

The covariance-aware measure asks a sharper question: how many independent, equal-volatility bets would have the same ratio of *undiversified* to *diversified* risk as my book? Let $\Sigma$ be the idiosyncratic covariance matrix (the residual after the factor model of Chapter 8 strips rates, spread beta and the credit factors; IDO or it didn't happen), $\sigma_i = \sqrt{\Sigma_{ii}}$, and $w$ the vector of position weights. Define

$$
N_{\text{eff}} = \frac{\left(\sum_i |w_i|\,\sigma_i\right)^2}{w^{\top}\Sigma\, w}. \tag{28.4}
$$

The numerator is the variance the book would have if every position moved in lockstep; the denominator is the variance it actually has. Two checks. If all $N$ positions are independent with equal weight and volatility, the numerator is $N^2 w^2\sigma^2$ and the denominator $N w^2\sigma^2$, so $N_{\text{eff}} = N$. If they are perfectly correlated, numerator and denominator are equal and $N_{\text{eff}} = 1$.

Now add issuer structure. Suppose $N$ bonds come from $J$ issuers with $m = N/J$ bonds each, equal weights and volatilities, residual correlation $\rho_w$ between bonds of the same issuer and $\rho_a$ between bonds of different issuers. Each bond has $m-1$ same-issuer partners and $N-m$ other-issuer partners, so

$$
w^\top\Sigma w = w^2\sigma^2\big[N + N(m-1)\rho_w + N(N-m)\rho_a\big],
$$

and (28.4) becomes

$$
N_{\text{eff}} = \frac{N}{1 + (m-1)\rho_w + (N-m)\rho_a}. \tag{28.5}
$$

Theo's book: $N = 300$ bonds, $J = 60$ issuers of $m = 5$ bonds, $\rho_w = 0.9$ (bonds of one issuer share a default time), and a residual cross-issuer correlation of $\rho_a = 0.01$ *(illustrative)*. The denominator is $1 + 3.6 + 2.95 = 7.55$, and $N_{\text{eff}} \approx 39.7$. Two limits explain the number. With $\rho_a = 0$, $N_{\text{eff}} = 300/4.6 \approx 65$: the issuer count, slightly inflated because bonds of one issuer are not perfectly correlated. And as $N \to \infty$ with $m$ fixed, $N_{\text{eff}} \to 1/\rho_a = 100$: a residual correlation of one percent caps the breadth of any credit book at a hundred bets, however many CUSIPs it owns. Kaz calls this the "speed of light" of credit diversification. It is the reason a bigger book is not a better book after the first hundred issuers, and the reason the platform pays more for a new *signal* than for a new *name* (§28.8).

### How noisy is your hit rate?

The same binomial arithmetic tells you how long it takes to know whether a PM is any good. A year of daily hits on $N_{\text{eff}}$ independent bets is $252\,N_{\text{eff}}$ Bernoulli draws, so the standard error of the measured hit rate is

$$
\text{SE}(\hat p) = \sqrt{\frac{p(1-p)}{252\,N_{\text{eff}}}}. \tag{28.6}
$$

> **[SOURCE EXTRACTION]** *Paleologo_Advanced_Portfolio_Management p.150:* "The standard error associated to this yearly hitting rate is 0.33%. This is a very large value, comparable to the 'edge' of 0.5%."
>
> **Annotation.** Equation (28.6) reproduces the 0.33% with about 90 effective names and $p \approx 0.505$. For a credit PM with 40 effective bets, the standard error over a year is 0.50%, the same size as the edge itself: a year of P&L cannot tell a 50.5% PM from a coin. This is the quiet scandal under every drawdown rule in §28.6. The rule is a decision about skill made on a sample too small to measure skill, which is defensible only because its real job is survival, not inference. It is also the best argument for instrumenting hit rates *by signal and by analyst* (the Edge Ledger of Chapter 3), where the sample is larger and the attribution is sharper than one PM's annual P&L.

### Concentration is not rewarded in debt

The ex-RSSG instinct is to concentrate: you did the work, you read the intercreditor, you know the fulcrum. The shelf disagrees, politely and then not politely.

> **[SOURCE EXTRACTION]** *Bohn_Stein_Active_Credit_Portfolio_Management p.489:* "Unlike equities, however, debt has no upside potential to offset the potential for large losses … there are no practical circumstances under which an investor or counterparty can be rewarded for taking on concentrations of default risk."
>
> **Annotation.** The payoff of a bond is capped at par plus coupons and floored at recovery, so the right tail that rewards a concentrated equity bet does not exist. A concentrated credit bet earns the same spread as a diversified one and carries more default variance. The modern desk keeps the principle and adds an exception the authors would recognize: when the PM's information is genuinely about $L$ rather than about $\lambda$ (a recovery the market has mispriced because it has not read the documents), the bet is less a default bet than a recovery bet, and §28.4 sizes it with Kelly. Even then, the single-name cap comes from the ruin boundary, not from conviction.

> **[SOURCE EXTRACTION]** *Bolder_Credit_Risk_Modelling p.391:* "One half of the total risk can … be allocated to the 16 largest obligors"
>
> **Annotation.** Bolder's example is a 100-obligor one-factor portfolio, and the punchline generalizes: tail risk concentrates far faster than position count suggests. On the same pages Bolder argues for expected shortfall over VaR as the economic-capital measure, because ES contributions are stable with feasible simulation sizes while VaR contributions are not. On a desk this becomes a dashboard column (§28.9): ES contribution by issuer, ranked, with the top decile of names flagged when they carry more than half the tail.

How should conviction enter sizing, then? Paleologo's evidence is that the simple rule beats the clever one.

> **[SOURCE EXTRACTION]** *Paleologo_Advanced_Portfolio_Management p.100 (Insight 6.2):* "Using target positions that are proportional to the forecasted expected returns of a stock beats other common methods."
>
> **Annotation.** In credit, with covariance matrices built from sparse, stale, issuer-clustered data (Chapter 8), full mean-variance inverts noise and produces positions nobody can trade. Proportional sizing on factor-neutralized alphas (Paleologo's Procedure 6.3 regresses the alphas on the factor loadings and sizes the standardized residuals) is robust to all of that. Our credit amendment is to make the proportionality *per unit of DTS-scaled volatility*: target $w_i \propto \alpha_i/\sigma_{\text{DTS},i}^2$ per issuer, then cap each issuer at the Kelly ruin bound of §28.4, then net to issuer before computing $N_{\text{eff}}$.

### Specification for AI Implementation (Block 1): Effective Breadth and the Hit-Rate Law

What ROBO built from the vague version ("compute breadth"): `len(book)`. It returned 300, and it was correct about the length.

The precise version: compute $1/H$ on issuer-netted GMV weights, $N_{\text{eff}}$ from (28.4) on the idiosyncratic covariance, the closed form (28.5) for equal issuer blocks as a regression test, the IR from (28.3) in both exact and approximate form, and the hit-rate standard error (28.6). Check the hit-rate law by Monte Carlo. All blocks in this chapter run in order in one interpreter.

```python
import numpy as np
import pandas as pd
from scipy import stats, optimize, integrate

RNG = np.random.default_rng(2028)
TRADING_DAYS = 252


def herfindahl_breadth(gmv_weights):
    """1/H on absolute GMV weights. Net positions to issuer level BEFORE calling."""
    w = np.abs(np.asarray(gmv_weights, dtype=float))
    total = w.sum()
    if total <= 0.0:
        raise ValueError("book has no gross exposure")
    w = w / total
    return 1.0 / np.sum(w ** 2)


def effective_breadth(weights, cov):
    """Eq. (28.4): (sum |w_i| sigma_i)^2 / (w' Sigma w), on the IDIOSYNCRATIC covariance."""
    w = np.asarray(weights, dtype=float)
    cov = np.asarray(cov, dtype=float)
    sig = np.sqrt(np.clip(np.diag(cov), 0.0, None))
    num = float(np.abs(w) @ sig) ** 2
    den = float(w @ cov @ w)
    if den <= 1e-18 * max(num, 1e-300):
        raise ValueError("near-zero book variance: hedged pairs? net to issuer first")
    return num / den


def issuer_block_cov(issuer_ids, sigma, rho_within, rho_across):
    """Residual covariance with one correlation inside an issuer and another across issuers."""
    ids = np.asarray(issuer_ids)
    same = ids[:, None] == ids[None, :]
    corr = np.where(same, rho_within, rho_across).astype(float)
    np.fill_diagonal(corr, 1.0)
    sig = np.asarray(sigma, dtype=float)
    return corr * np.outer(sig, sig)


def n_eff_equal_blocks(n_bonds, bonds_per_issuer, rho_within, rho_across):
    """Eq. (28.5), closed form for equal issuer blocks."""
    m = bonds_per_issuer
    return n_bonds / (1.0 + (m - 1) * rho_within + (n_bonds - m) * rho_across)


def ir_from_hit_rate(p, n_eff, periods=TRADING_DAYS, exact=False):
    """Eq. (28.3). exact=True keeps the sqrt(1-(2p-1)^2) term."""
    edge = 2.0 * p - 1.0
    ir = edge * np.sqrt(periods * n_eff)
    return ir / np.sqrt(1.0 - edge ** 2) if exact else ir


def hit_rate_se(p, n_eff, periods=TRADING_DAYS):
    """Eq. (28.6): standard error of one year's measured hit rate."""
    return np.sqrt(p * (1.0 - p) / (periods * n_eff))


# --- Theo's book: 300 bonds, 60 issuers x 5 bonds -------------------------------
issuers = np.repeat(np.arange(60), 5)
sig_bond = np.full(300, 0.051)                       # DTS 0.147 x sigma_rel 0.35 (illustrative)
cov_book = issuer_block_cov(issuers, sig_bond, rho_within=0.9, rho_across=0.01)
w_book = np.full(300, 1.0 / 300)

neff_num = effective_breadth(w_book, cov_book)
neff_cf = n_eff_equal_blocks(300, 5, 0.9, 0.01)
assert abs(neff_num - neff_cf) < 1e-8, (neff_num, neff_cf)
assert 39.0 < neff_cf < 40.5                          # "300 bonds, 60 issuers, 40 bets"
assert abs(herfindahl_breadth(w_book) - 300.0) < 1e-9 # 1/H ignores correlation entirely
assert abs(n_eff_equal_blocks(10**7, 5, 0.9, 0.01) - 100.0) < 0.01  # speed-of-light limit 1/rho_a

# Independent and perfectly correlated limits of (28.4)
assert abs(effective_breadth(np.full(50, 0.02), np.eye(50) * 0.04) - 50.0) < 1e-9
assert abs(effective_breadth(np.full(50, 0.02), np.full((50, 50), 0.04)) - 1.0) < 1e-9

# Paleologo's 0.33% standard error: about 90 effective names at p = 0.505
assert abs(hit_rate_se(0.505, 91) - 0.0033) < 1e-4
assert abs(hit_rate_se(0.505, 40) - 0.0050) < 2e-4   # a 40-bet credit PM: SE equals the edge

# Monte Carlo check of the hit-rate law: daily wins ~ Binomial(N, p), return = (2W - N)/N
p_hit, n_bets, n_days = 0.52, 40, TRADING_DAYS * 400
wins = RNG.binomial(n_bets, p_hit, size=n_days)
daily = (2.0 * wins - n_bets) / n_bets
ir_mc = daily.mean() / daily.std(ddof=1) * np.sqrt(TRADING_DAYS)
ir_exact = ir_from_hit_rate(p_hit, n_bets, exact=True)
assert abs(ir_mc - ir_exact) < 0.15, (ir_mc, ir_exact)          # MC SE ~ 0.05
assert abs(ir_exact / ir_from_hit_rate(p_hit, n_bets) - 1.0) < 1e-3
```

The edge cases ROBO must handle: a long/short pair in two bonds of the same issuer (a basis or curve trade) makes the denominator of (28.4) nearly zero and $N_{\text{eff}}$ explode, which is why the function refuses and the spec says to net to issuer first; a book with no gross exposure raises; and negative variance from a non-positive-definite estimated covariance is clipped on the diagonal but should be repaired upstream (shrinkage, Chapter 8), not here.
