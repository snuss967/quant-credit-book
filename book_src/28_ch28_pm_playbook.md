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

## 28.3 Allocation Across Signal Horizons

Theo's four PMs run four different clocks. Priya *(fictional, as are all PMs in this chapter)* runs index trend on CDX (Chapter 10) and turns her book over every few weeks. Dov runs value, carry and quality in liquid cash bonds (Chapter 9) and holds for quarters. Rafe runs ETF creation/redemption and portfolio-trade arbitrage (Chapters 19–20) and holds for days. Sunita, ex-RSSG like Theo, runs LMT candidates, post-reorg equities and docket-driven events (Chapters 13–16) and holds until a judge rules. Theo's question is how to split the risk among them. The answer depends less on who has the best backtest than on a property of each signal that nobody puts in the pitch deck: how fast it dies, compared with how much it costs to trade.

> **[SOURCE EXTRACTION]** *Dynkin_Systematic_Investing_in_Credit p.520:* "However, limited liquidity in credit markets makes high‐turnover strategies less practical and necessitates long investment horizons consistent with fundamentally driven styles such as"
>
> **Annotation.** Dynkin and coauthors are describing cash bonds, and in cash bonds the sentence is a law. The 2026 desk's departure is that "credit" is no longer one instrument. Since about 2021 the index CDS market, credit ETFs, listed credit futures and portfolio trading have built a liquid layer on top of the cash market where turnover is cheap (see the Trend Watch below). The horizon constraint has not gone away. It has become a property of the *tier*, not of the asset class. Fast signals are viable if they are expressed in the liquid layer; slow signals belong in cash; and the desk head's job is to stop anyone trading a fast signal in a slow instrument.

### The break-even half-life

Model a signal as a forecast of excess return whose strength decays exponentially. At inception it predicts an expected return *rate* of $\alpha_0$ per year, and the rate decays as $\alpha(t) = \alpha_0 e^{-\phi t}$, where $\phi$ is the decay rate and $h = \ln 2/\phi$ the half-life. A position opened on the signal and held while the forecast lasts earns, in expectation,

$$
\int_0^\infty \alpha_0 e^{-\phi t}\,dt = \frac{\alpha_0}{\phi}.
$$

Let $c^{\text{RT}}$ be the round-trip cost in the instrument used to express the signal, as a fraction of price. In credit that is the liquidity cost score of Ben Dor et al. (§28.5): $\text{LCS} = D^{\text{spr}} \times$ bid-ask spread in spread terms. A signal that refreshes continuously turns its positions over about once per signal life, $\phi$ times a year, so its annual gross alpha is $\phi \cdot \alpha_0/\phi = \alpha_0$, its annual cost is $\phi\, c^{\text{RT}}$, and its net alpha is

$$
\alpha^{\text{net}} = \alpha_0 - \frac{\ln 2}{h}\,c^{\text{RT}}. \tag{28.7}
$$

Setting $\alpha^{\text{net}} = 0$ gives the shortest half-life a signal can have and still pay for itself in a given tier:

$$
h^{\ast} = \frac{\ln 2 \cdot c^{\text{RT}}}{\alpha_0}. \tag{28.8}
$$

Take a signal with $\alpha_0 = 3\%$ a year. In the index layer, with a round-trip cost of 0.05% of price *(illustrative)*, $h^\ast = 0.693 \times 0.0005/0.03 = 0.0116$ years, about three trading days. In liquid cash bonds at 0.6% *(illustrative)*, $h^\ast = 0.139$ years, about seven weeks. In stressed bonds at 2.5% *(illustrative)*, $h^\ast = 0.58$ years, seven months. Equation (28.8) explains in one line why trend lives in CDX and LMT alpha lives in bonds you hold until the court rules. Trend's half-life is weeks: viable in tier 0 and a money-loser in cash. The LMT trade's half-life is months, and its $\alpha_0$ is large enough to pay a stressed bid-ask.

Two refinements, both from the literature. First, Gârleanu and Pedersen (2013, *Journal of Finance*, "Dynamic Trading with Predictable Returns and Transaction Costs") show for quadratic costs that the optimal policy is to "aim in front of the target" and trade partially toward it, and that predictors with slower decay get more weight in the aim portfolio. Credit costs are mostly linear (half the bid-ask on every trade) with a size-dependent impact on top (§28.5), and linear costs produce a no-trade band rather than partial trading: do not trade a bond whose target position has moved less than the band. That is exactly Dynkin's "turnover buffer" (Dynkin p.707), and its alternative is a hard turnover budget with explicit exposure constraints (p.715), which avoids the large rebalancing events a buffer can store up. Second, fills are probabilistic. The trade a backtest assumes is a trade an RFQ may not fill, and the unfilled order leaves an exposure nobody modelled.

> **[SOURCE EXTRACTION]** *Man_Revolutions_in_Credit_Trading_2023 p.4:* "Liquidity modelling is essential too: an optimised portfolio is not optimal if you can't trade it. Furthermore, unfilled orders may create unintended and potentially unmodelled risk exposures in the portfolio."
>
> **Annotation.** The horizon ladder below is the desk-level response. A fill probability below one is a hidden cost in (28.7): if a fraction $1-\pi$ of intended trades fail, the realized position lags the target, so a fast signal decays further before it is expressed. Man's companion point (same page) is that with more than 90% of its flow electronic, it could make "more frequent, smaller trades," which lowers $c^{\text{RT}}$ for small tickets and so lowers $h^\ast$. Electronification moves signals *down* the ladder: a signal that needed tier 0 in 2015 may be viable in liquid cash in 2026, if the tickets are small.

> **[SOURCE EXTRACTION]** *Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.19:* "We cannot overstate the importance of transaction cost and liquidity modelling for quant credit participants" … "Momentum tends to have the highest turnover of any factor approach while both Size and Quality see the least churn."
>
> **Annotation.** Momentum is the canonical victim of (28.8). At our illustrative cash cost of 0.6% round trip, a cash-bond momentum signal with a two-month half-life needs $\alpha_0$ above $0.693 \times 6 \times 0.006 = 2.5\%$ a year to break even. That is a high bar for a factor whose long-only premium is usually quoted in tens of basis points. The modern answer is not to drop momentum but to stop trading it standalone: use it as a tie-breaker inside trades the slow signals were going to make anyway, where its marginal cost is zero, or express it in the index layer.

### The horizon ladder

| Tier | Instruments | Round-trip cost *(illustrative)* | Regulatory anchor | Signals that live here | Chapters |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 0 | CDX/iTraxx, credit index futures, HY/IG ETFs | 0.02–0.10% of price | Exchange or SEF liquidity; days to liquidate below one | Index trend, ETF premium/discount, beta overlay, hedges | 10, 19, 20 |
| 1 | Liquid IG/HY cash bonds, PT-eligible | 0.3–1.0% | FRTB liquidity horizon 40 days (IG corporate), 60 days (HY corporate) | Value, carry, quality, defensive HY, slow momentum tilts | 8, 9, 11, 12 |
| 2 | Stressed, LMT candidates, post-reorg equity and claims | 2–5% or more | FRTB 120 days ("other" credit spread); SEC Rule 22e-4 "illiquid" bucket | Covenant, docket, priming-risk and recovery alpha | 13–16, 25 |

The FRTB horizons are from the Basel Framework, MAR33.12 (in force 1 January 2023). They are regulatory anchors for a bank's trading book, not a hedge fund's liquidation plan, but they encode a consensus that a corporate HY position takes half again as long to exit as an IG one, and a stressed one twice as long again.

The ladder prescribes the allocation in three steps. First, each signal goes to the cheapest tier that can express it, and is dropped (or demoted to a tie-breaker) if (28.7) is negative there. Second, each tier gets a liquidity budget (days-to-liquidate and stressed LCS, §28.5), and the volatility budget follows from it, not the other way around. Third, the overlay in tier 0 hedges the beta that the slow books accumulate, so the slow books can hold their IDO without being forced to trade it every time spread beta moves. IDO or it didn't happen: the overlay is how a cash book keeps its idiosyncratic alpha without paying a cash bid-ask to manage its systematic exposure.

> **Poker Table.** Ines explains the ladder to Theo with chips. "Dov's value book is a big pair you slow-play. You don't raise every street, because every raise pays the rake, and in cash bonds the rake is half a point. Priya's trend sleeve is your table image: small bets, frequent, in the index, where the rake is a few cents. The table sees you trading all day and never notices you haven't touched the big pair in four months." Theo asks what happens when the trend sleeve and the value book disagree. "Then you're hedged, and you've paid the index rake to be hedged instead of the cash rake. That's the whole edge." The hand history agrees: in the desk's markouts *(illustrative)*, the value book's one-month markouts on new positions are flat and its six-month markouts carry the alpha, while the trend sleeve's markouts are the other way round. A desk that judged both at one horizon would fire one of them for the other's sins.

> **Trend Watch: The liquid overlay layer arrives, 2021–2026.** *What changed:* the tier-0 instruments that let a credit desk trade fast signals and hedge slow books cheaply grew to record size. *How big, with dates:* ISDA's research note of 29 July 2026 puts total CDS trading at \$41.8tn in 2025, with index products a record \$39.0tn (93.3% of the total; \$28.1tn in 2023), while single-name activity fell from a \$3.3tn peak in 2023 to \$2.8tn; H1 2026 activity was \$27.4tn, up 27.8% year on year. Clarus reports cleared USD CDX of \$3.94tn in March 2026, up 46% year on year. In listed credit, Cboe iBoxx futures block trades topped \$1bn a month for a second straight month in August 2026, and IBIG block activity overtook IBHY's for the first time (The DESK, 16 October 2026). In cash, March 2026 combined US IG and HY TRACE volume averaged \$70.2bn a day, up 14.7% year on year, with record portfolio-trading ADV of \$2.3bn at MarketAxess and a record \$10.3bn ADV at Trumid (The DESK, 9 April 2026). In 2022, Man's protocol mix was 42% disclosed RFQ, 16% anonymous RFQ, 13% session-based, 10% central limit order book, 10% portfolio trading and 9% streams (Man_Revolutions_in_Credit_Trading_2023 p.4). *What it means for the desk:* the cost of the overlay in (28.8) has fallen and its capacity has risen, so more of the desk's fast alpha can be moved into tier 0 and more of its beta management out of tier 1. It also means more of everyone's de-risking happens in the same few instruments on the same few days. The overlay is cheap until the day every pod uses it to cut gross at once.

### Specification for AI Implementation (Block 2): The Horizon Ladder

What ROBO built from the vague version ("put each signal where it makes the most money"): it ranked signals by gross backtest return and put all of them in the tier with the most bonds, tier 1, because that was where the most money had been made before costs.

The precise version: for each signal and each tier that can express it, compute the net alpha (28.7); assign the signal to the tier with the highest positive net alpha; flag signals with no positive tier as tie-breakers only. Report the break-even half-life (28.8) for each tier at a reference $\alpha_0$.

```python
# --- Block 2: the horizon ladder ------------------------------------------------
TIERS = pd.DataFrame(
    {"instruments": ["CDX/iTraxx, index futures, credit ETFs",
                     "liquid IG/HY cash, PT-eligible",
                     "stressed, LMT candidates, post-reorg"],
     "rt_cost": [0.0005, 0.006, 0.025]},          # round-trip cost, fraction of price (illustrative)
    index=pd.Index([0, 1, 2], name="tier"),
)

SIGNALS = pd.DataFrame(
    {"alpha0":       [0.05,    0.03,  0.02,   0.015, 0.012, 0.08],   # annual rate at inception (illustrative)
     "half_life_yr": [3 / 252, 1 / 12, 2 / 12, 0.75,  1.0,   0.5],
     "tiers":        [(0,),    (0, 1), (1,),   (1, 2), (1, 2), (2,)]},  # tiers able to express the signal
    index=pd.Index(["etf_premium", "index_trend", "momentum", "value", "carry", "lmt_event"],
                   name="signal"),
)


def break_even_half_life(rt_cost, alpha0):
    """Eq. (28.8): shortest half-life (years) that pays its own round-trip cost."""
    if alpha0 <= 0.0:
        return np.inf
    return np.log(2.0) * rt_cost / alpha0


def net_alpha(alpha0, half_life_yr, rt_cost):
    """Eq. (28.7): alpha0 - (ln 2 / h) * c_RT, annualized."""
    if half_life_yr <= 0.0:
        raise ValueError("half-life must be positive")
    return alpha0 - np.log(2.0) / half_life_yr * rt_cost


def horizon_ladder(signals, tiers):
    rows = []
    for name, sg in signals.iterrows():
        nets = {t: net_alpha(sg.alpha0, sg.half_life_yr, tiers.loc[t, "rt_cost"]) for t in sg.tiers}
        best = max(nets, key=nets.get)
        rows.append({"signal": name, "best_tier": best if nets[best] > 0 else None,
                     "net_alpha": nets[best], "tie_breaker_only": nets[best] <= 0,
                     **{f"net_t{t}": v for t, v in nets.items()}})
    return pd.DataFrame(rows).set_index("signal")


ladder = horizon_ladder(SIGNALS, TIERS)

assert ladder.loc["index_trend", "best_tier"] == 0               # trend lives in the index layer
assert ladder.loc["index_trend", "net_t1"] < 0 < ladder.loc["index_trend", "net_t0"]
assert ladder.loc["value", "best_tier"] == 1 and ladder.loc["value", "net_t2"] < 0
assert ladder.loc["lmt_event", "best_tier"] == 2 and ladder.loc["lmt_event", "net_alpha"] > 0.04
assert bool(ladder.loc["momentum", "tie_breaker_only"])          # cash momentum: tie-breaker only
assert break_even_half_life(0.0005, 0.03) * TRADING_DAYS < 5      # tier 0: under a week
assert 1.0 < break_even_half_life(0.006, 0.03) * 12 < 3.0         # tier 1: 1-3 months
```

Edge cases: a signal with $\alpha_0 \le 0$ has an infinite break-even half-life and is never traded; a half-life of zero is an error, not a very fast signal; and costs must be *stressed* costs when the ladder is used for the liquidity budget (§28.5), because a tier-1 bond at a 5× bid-ask is a tier-2 bond for as long as the stress lasts.

## 28.4 Kelly With Jump-to-Default

Kaz's 93% deserves a proper autopsy, because nothing in it is an arithmetic error. Kaz took one B3 bond with carry $c = 4.5\%$ a year, a one-year default probability of $q = 3.1\%$ read from a rating-agency table for B3 issuers, and a loss given default of $L = 0.6$ (the agency's average 40% recovery), and applied the Kelly criterion for a binary bet. The formula did what it was told.

> **[SOURCE EXTRACTION]** *Paleologo_Advanced_Portfolio_Management p.91:* "If your goal were to maximize expected returns and your expected returns forecasts were accurate, the investment decision would be straightforward: the portfolio would hold a single stock, the one with highest expected returns. Those who follow this rule need to read this book the most, but probably don't have enough money to buy it"
>
> **Annotation.** The credit version is "hold the one CCC with the fattest spread," and it is worse than the equity version, because the fattest spread is usually fattest for a reason the spread does not tell you: a maturity wall, a sponsor shopping for an uptier, a recovery that depends on whether the "first lien" is first. Kelly is the disciplined alternative to maximizing expected return: it maximizes expected *log* wealth, which penalizes the possibility of ruin infinitely. In credit, ruin has a precise address. It is the default of a position large enough that $f L \ge 1$.

### Discrete Kelly for a bond

Over one period, a fraction $f$ of NAV in the bond earns $+c$ with survival probability $p$ and loses $L$ with default probability $q = 1-p$ (excess returns over financing; pull-to-par and rolldown ignored). Expected log growth is

$$
g(f) = p\,\ln(1 + f c) + q\,\ln(1 - f L).
$$

Setting $g'(f) = pc/(1+fc) - qL/(1-fL) = 0$ and cross-multiplying, $pc(1 - fL) = qL(1 + fc)$, so $pc - qL = fcL(p+q) = fcL$, and

$$
f^\ast = \frac{pc - qL}{cL} = \frac{p}{L} - \frac{q}{c}. \tag{28.9}
$$

Three facts follow. The bet has positive edge, $pc - qL > 0$, if and only if $q < c/(c+L)$. The growth function is defined only for $f < 1/L$, the **ruin boundary**: at $f = 1/L$ a default takes wealth to zero and $\ln 0 = -\infty$. And for Kaz's inputs, $f^\ast = 0.969/0.6 - 0.031/0.045 = 1.615 - 0.689 = 0.926$. There is the 93%.

Now the sensitivities, which are where the ex-RSSG analyst earns a seat. Differentiating (28.9),

$$
\frac{\partial f^\ast}{\partial L} = -\frac{p}{L^2}, \qquad \frac{\partial f^\ast}{\partial q} = -\left(\frac{1}{L} + \frac{1}{c}\right).
$$

At Kaz's inputs these are $-2.69$ and $-23.9$. The fraction is nine times more sensitive to $q$ per unit, but the units are not equally uncertain. A one-year default probability for a B3 name is known to perhaps $\pm 1.5$ points, which moves $f^\ast$ by about 36 points of NAV; a recovery is known to perhaps $\pm 15$ points, which moves it by about 32. First-lien distressed-exchange recoveries alone went from 55% in 2023 to 71% at end-2024 in Moody's data (Bloomberg Law, 23 April 2025; see the Trend Watch in §5.5). The two uncertainties are of the same size, and only one of them can be shrunk by reading the credit agreement. The PhD takes $L$ from a table. The analyst who has read the intercreditor agreement knows whether the first lien is first.

### Continuous time, and the jump

Let a position of fraction $f$ in a bond have excess return $dP/P = c\,dt + \sigma\,dW_t - L\,dN_t$, where $\sigma$ is the diffusive (spread) volatility, $N_t$ a Poisson process with intensity $\lambda$ (the default intensity, under $\mathbb{P}$; see below), and the bond is replaced after default so the bet is stationary. Wealth follows $dX_t/X_{t^-} = f(c\,dt + \sigma\,dW_t - L\,dN_t)$. Itô's formula for a jump-diffusion gives

$$
d\ln X_t = \left(fc - \tfrac12 f^2\sigma^2\right)dt + f\sigma\,dW_t + \ln(1 - fL)\,dN_t,
$$

so the long-run growth rate is

$$
g(f) = fc - \tfrac12 f^2 \sigma^2 + \lambda \ln(1 - fL). \tag{28.10}
$$

With $\sigma = 0$, $g'(f) = c - \lambda L/(1-fL) = 0$ gives

$$
f^\ast = \frac{1}{L} - \frac{\lambda}{c}, \tag{28.11}
$$

the continuous twin of (28.9). With $\sigma > 0$, $g'(f) = c - f\sigma^2 - \lambda L/(1 - fL) = 0$. Multiply by $(1 - fL)$:

$$
\sigma^2 L\, f^2 - (cL + \sigma^2)\, f + (c - \lambda L) = 0. \tag{28.12}
$$

The left side is positive at $f = 0$ (when the edge $c - \lambda L$ is positive) and equals $-\lambda L < 0$ at $f = 1/L$, so exactly one root lies inside the ruin boundary, and it is the smaller one. In rationalized form, which avoids cancellation when $\sigma$ is small,

$$
f^\ast = \frac{2(c - \lambda L)}{(cL + \sigma^2) + \sqrt{(cL - \sigma^2)^2 + 4\sigma^2\lambda L^2}}.
$$

(The discriminant has been rewritten as a sum of squares, so it is never negative.) At Kaz's inputs with $\lambda = 0.031$ and $\sigma = 5\%$, $f^\ast \approx 0.94$.

Compare the shortcut Kaz almost used, Merton's diffusion fraction with the jump replaced by a diffusion of the same mean and variance, $\lambda L$ and $\lambda L^2$:

$$
f^{\text{M}} = \frac{c - \lambda L}{\sigma^2 + \lambda L^2} = \frac{0.0264}{0.0025 + 0.0112} = 1.93.
$$

Merton's approximation says to hold 193% of NAV in a bond whose default costs $1.93 \times 0.6 = 116\%$ of NAV. The approximation is excellent for small jumps and disastrous near the ruin boundary, because a diffusion never jumps over it. Bermin and Holm (2026, *Kelly trading when asset prices have jumps*; publication details CHECK) make the general point that the continuous approximation can badly underestimate bankruptcy risk when leverage is high. In credit, every default is a large jump, so the approximation is never safe for single names. Use (28.10).

### Fractional Kelly is full Kelly for people with standard errors

Near its maximum, any growth function is approximately quadratic, $g(f) \approx \mu f - \tfrac12 v f^2$, with $f^\ast = \mu/v$ and $g^\ast = \mu^2/(2v)$. Betting a multiple $\theta$ of Kelly gives

$$
g(\theta f^\ast) = \frac{\mu^2}{v}\left(\theta - \frac{\theta^2}{2}\right) = g^\ast\,(2\theta - \theta^2).
$$

Half Kelly keeps 75% of the growth at half the volatility, and double Kelly keeps none of it. Now suppose the edge is estimated with relative error $\varepsilon$, mean zero and standard deviation $s_\varepsilon$, so that the desk bets $\theta(1+\varepsilon)f^\ast$. Expected growth is

$$
\mathbb{E}\big[g\big(\theta(1+\varepsilon)f^\ast\big)\big] = g^\ast\left(2\theta - \theta^2(1 + s_\varepsilon^2)\right),
$$

which is maximized at

$$
\theta^\ast = \frac{1}{1 + s_\varepsilon^2}. \tag{28.13}
$$

An edge known to within 100% of itself, which is generous for a single credit, gives $\theta^\ast = \tfrac12$. Half Kelly is not timidity. It is the full Kelly of a PM who is honest about the standard error of her edge, and the hit-rate arithmetic of §28.2 says that standard error is large.

### Which measure, and which loss

Kelly needs the physical default intensity $\lambda^{\mathbb{P}}$, never the risk-neutral $\lambda^{\mathbb{Q}}$ bootstrapped from CDS in Chapter 6. The reason is a one-line proof. Under $\mathbb{Q}$ the credit triangle holds, $c \approx \lambda^{\mathbb{Q}} L$, so the edge $c - \lambda^{\mathbb{Q}} L$ is zero and (28.11) gives $f^\ast = 0$: the risk-neutral measure is the measure in which nobody has an edge, by construction. The edge that Kelly sizes is $c - \lambda^{\mathbb{P}}L$, the credit risk premium plus whatever your information adds. That is why mixing sources is dangerous. Kaz's $c$ came from the market, his $q$ from a long-run agency cohort, and his $L$ from an agency average, and the 93% is the product of three numbers from three different worlds.

Recovery is not a constant either. Let $L = L_{\max} U$ with $U \sim \text{Beta}(a, b)$ (the recovery model of Chapter 5). The growth rate becomes

$$
g(f) = fc - \tfrac12 f^2\sigma^2 + \lambda\,\mathbb{E}\big[\ln(1 - fL)\big],
$$

defined for $f < 1/L_{\max}$. Two consequences. Because $x \mapsto x/(1 - fx)$ is convex, Jensen's inequality gives $\mathbb{E}[L/(1 - fL)] > \mathbb{E}[L]/(1 - f\,\mathbb{E}[L])$, so a random $L$ lowers $f^\ast$ below the constant-$L$ value at the same mean. And the **ruin boundary is set by the worst recovery, not the average one**. If the analyst's reading of the collateral package and the intercreditor shows a 25% recovery floor, $L_{\max} = 0.75$ and the boundary is $1.33\times$ NAV. If the documents permit a non-pro-rata uptier (Chapter 13), the worst case for a non-participating lender is close to zero recovery, $L_{\max} \to 1$, and the boundary falls to $1.0\times$, the unlevered position. The Priming Risk Score is, among other things, an estimate of where the ruin boundary is. Kelly in credit is the intercreditor agreement, priced in leverage.

### Many names, one recession

For independent jumps, (28.10) is additive across names and each $f_i^\ast$ is computed alone. Defaults are not independent. Add a common Poisson process with intensity $\lambda_c$ that defaults all $n$ names of a cluster together (a sector, a sponsor, a CLO's weakest bucket). For $n$ symmetric names each held at $f$,

$$
g(f) = n f c - \tfrac12 n f^2 \sigma^2 + n\lambda_i\ln(1 - fL) + \lambda_c\ln(1 - n f L),
$$

and the first-order condition (with $\sigma = 0$) is

$$
c = \frac{\lambda_i L}{1 - fL} + \frac{\lambda_c L}{1 - n f L}, \qquad 0 < f < \frac{1}{nL}. \tag{28.14}
$$

The right-hand side is larger than in the single-name problem at the same total intensity, so each $f$ is smaller, and the cluster as a whole obeys $\sum_j f_j L_j < 1$. A desk that computes forty single-name Kelly fractions and adds them up has computed a number with no meaning. The binding constraint is the cluster ruin bound.

> **Ways This Blows Up.** *Kelly on a $\mathbb{Q}$ hazard:* gives zero or a negative fraction, which fails safe, and so tempts someone to "fix" it by mixing a market spread with a historical default rate and an agency recovery, which is how you get 93%. *Kelly on a smoothed mark:* ROBO's favourite IG bond had a realized volatility of 0.4% because its matrix mark had not moved; fed into (28.12), it produces leverage limited only by the ruin boundary, and the volatility arrives with the first trade. Estimate $\sigma$ from traded prices or from a DTS model, never from the mark. *Kelly on correlated CCCs:* individually optimal fractions summed across a sector breach (28.14). *Kelly on yesterday's $L$:* the recovery distribution moved between 2023 and 2026 (§5.5); a static $L$ calibrated on pre-2015 defaults is an upper bound on recovery for sponsor-backed, loan-only borrowers.

### Case Study: The 2026 CCC Decompression

> **Trend Watch: The CCC decompression, January–October 2026.** *What changed:* the bottom of the high-yield market repriced while the index barely moved. *How big, with dates (ICE BofA option-adjusted spreads, FRED series BAMLH0A0HYM2, BAMLC0A0CM and BAMLH0A3HYC, fetched 17 October 2026):* US HY went from 2.83% on 2 January to a low of 2.64% on 22 January, peaked at 3.46% on 30 March during the Iran-war shock, and stood at 3.23% on 15 October. US IG went from 0.79% to 0.73%, 0.94% (16 March) and 0.84%. The CCC-and-lower subindex went from 8.88% to a low of 8.38% (28 January), 10.20% (30 March) and 12.78% on 15 October, after 12.82% on 14 October, its widest since at least October 2023. The CCC-to-HY spread ratio rose from about 3.1× in January to about 4.0× in October. Recovery expectations moved the same way: Moody's September 2026 *Corporate Defaults and Recoveries* report projected first-lien loan recoveries "declining to 55%" (via American Banker, 28 September 2026). *What it means for the desk:* a book sized on index-level risk saw a calm year. A book sized on name-level $\lambda$ and $L$ saw the two inputs of (28.11) moving against each other while the headline spread looked boring, which is the setting where Kelly earns its keep.

How a systematic desk would have read it. Take a representative CCC bond at the January low, with $c \approx 8.4\%$ (the subindex OAS), and illustrative physical inputs $\lambda^{\mathbb{P}} = 6\%$ a year and $L = 0.55$. Equation (28.11) gives $f^\ast = 1/0.55 - 0.06/0.084 = 1.82 - 0.71 = 1.10$: Kelly would lever it. By mid-October, with $c \approx 12.8\%$, suppose the hazard model of Chapter 14 (re-defaults in the 2024 LMT cohort) has $\lambda^{\mathbb{P}}$ at 10% and the recovery model has $L$ at 0.70 *(both illustrative)*. The edge has risen, from $0.084 - 0.033 = 5.1\%$ to $0.128 - 0.070 = 5.8\%$ a year, so a spread screen says buy. But (28.11) gives $f^\ast = 1.43 - 0.78 = 0.65$, a 40% *cut*. The spread said the bucket got cheaper. Kelly says it got cheaper and more dangerous, and the danger grew faster: the ruin boundary moved in from 1.82 to 1.43 as $L$ rose, and $\lambda/c$ rose from 0.71 to 0.78.

Three refinements turn this into a trade. First, apply (28.13): with a relative standard error on the edge of about 1, bet half of each fraction. Second, cap each name at the ruin boundary implied by its *documents*, $1/L_{\max}$, which for LMT-permissive credits is $1.0$ or less, not $1/\mathbb{E}[L]$. Third, impose (28.14) on each cluster: the CCC bucket of one sector, or the issuers of one sponsor, share a common jump. What survives is a book that leaned into CCC carry in January, cut it as $\lambda$ and $L$ rose through the summer, and concentrated what remained in names where the analyst's reading of the documents put a floor under recovery. That last step is not quant. It is the RSSG seat, sized.

### Specification for AI Implementation (Block 3): Kelly With Jumps

What ROBO built from the vague version ("size positions by Kelly"): it computed $\mu/\sigma^2$ per bond from three months of marks, found the matrix-priced IG bond, and requested 4,000% of NAV in it.

The precise version: implement (28.9), (28.10)–(28.12) with the rationalized root, Merton's approximation (for comparison only, never for sizing), the fractional multiplier (28.13), the random-loss growth rate with a Beta recovery and a ruin boundary at $1/L_{\max}$, and the cluster solver (28.14). Inputs are physical-measure intensities. Long-only: return zero when the edge is not positive.

```python
# --- Block 3: Kelly with jump-to-default ----------------------------------------
def kelly_binary(p_surv, carry, loss):
    """Eq. (28.9): f* = p/L - q/c, floored at zero (long-only)."""
    q = 1.0 - p_surv
    return max(p_surv / loss - q / carry, 0.0)


def growth_binary(f, p_surv, carry, loss):
    if f * loss >= 1.0:
        return -np.inf
    return p_surv * np.log1p(f * carry) + (1.0 - p_surv) * np.log1p(-f * loss)


def growth_jump(f, carry, lam, loss, sigma=0.0):
    """Eq. (28.10): g(f) = f c - f^2 sigma^2 / 2 + lam ln(1 - f L). lam is P-measure."""
    diffusive = f * carry - 0.5 * f * f * sigma * sigma
    if lam <= 0.0:
        return diffusive
    if f * loss >= 1.0:
        return -np.inf
    return diffusive + lam * np.log1p(-f * loss)


def kelly_jump(carry, lam, loss, sigma=0.0):
    """Eqs. (28.11)-(28.12): the root of the FOC inside the ruin boundary 1/L."""
    edge = carry - lam * loss
    if edge <= 0.0:
        return 0.0
    if lam <= 0.0:                                     # no jump: Merton's mu / sigma^2
        return edge / sigma ** 2 if sigma > 0.0 else np.inf
    b = carry * loss + sigma ** 2
    disc = (carry * loss - sigma ** 2) ** 2 + 4.0 * sigma ** 2 * lam * loss ** 2
    return 2.0 * edge / (b + np.sqrt(disc))


def kelly_merton_approx(carry, lam, loss, sigma):
    """Diffusion approximation (comparison only): (c - lam L) / (sigma^2 + lam L^2)."""
    return max((carry - lam * loss) / (sigma ** 2 + lam * loss ** 2), 0.0)


def kelly_multiplier(rel_se_edge):
    """Eq. (28.13): optimal fraction of Kelly when the edge has relative s.e. s."""
    return 1.0 / (1.0 + rel_se_edge ** 2)


def growth_random_loss(f, carry, lam, a, b, loss_max, sigma=0.0):
    """g(f) with L = loss_max * Beta(a, b). Defined for f < 1 / loss_max."""
    if f * loss_max >= 1.0:
        return -np.inf
    dist = stats.beta(a, b)
    e_log, _ = integrate.quad(lambda u: np.log1p(-f * loss_max * u) * dist.pdf(u), 0.0, 1.0, limit=200)
    return f * carry - 0.5 * f * f * sigma * sigma + lam * e_log


def kelly_random_loss(carry, lam, a, b, loss_max, sigma=0.0):
    upper = (1.0 - 1e-6) / loss_max
    res = optimize.minimize_scalar(
        lambda f: -growth_random_loss(f, carry, lam, a, b, loss_max, sigma),
        bounds=(0.0, upper), method="bounded", options={"xatol": 1e-8})
    return float(res.x)


def kelly_cluster(n_names, carry, lam_idio, lam_common, loss):
    """Eq. (28.14): per-name fraction for n symmetric names with one common default jump."""
    def foc(f):
        return (carry - lam_idio * loss / (1.0 - f * loss)
                - lam_common * loss / (1.0 - n_names * f * loss))
    if foc(0.0) <= 0.0:
        return 0.0
    hi = (1.0 - 1e-12) / (n_names * loss)
    return optimize.brentq(foc, 0.0, hi, xtol=1e-14)


# Kaz's 93%: c = 4.5%, q = 3.1%, L = 0.6
f_kaz = kelly_binary(0.969, 0.045, 0.60)
assert abs(f_kaz - 0.926) < 1e-3
step = 1e-6
dg = (growth_binary(f_kaz + step, 0.969, 0.045, 0.6)
      - growth_binary(f_kaz - step, 0.969, 0.045, 0.6)) / (2 * step)
assert abs(dg) < 1e-6 and f_kaz < 1.0 / 0.6                   # FOC holds, inside the ruin boundary
q_star = 0.045 / (0.045 + 0.6)                                 # edge condition q < c / (c + L)
assert kelly_binary(1 - q_star + 1e-4, 0.045, 0.6) > 0.0
assert kelly_binary(1 - q_star - 1e-4, 0.045, 0.6) == 0.0

# Continuous time: closed form, FOC, and Merton's approximation crossing the ruin boundary
assert abs(kelly_jump(0.045, 0.031, 0.6) - (1 / 0.6 - 0.031 / 0.045)) < 1e-12
f_j = kelly_jump(0.045, 0.031, 0.6, sigma=0.05)
assert abs(0.045 - f_j * 0.05 ** 2 - 0.031 * 0.6 / (1 - f_j * 0.6)) < 1e-12
assert 0.93 < f_j < 0.95
f_m = kelly_merton_approx(0.045, 0.031, 0.6, 0.05)
assert f_m * 0.6 > 1.0 > f_j * 0.6                             # one default wipes out the Merton bettor
g_star = growth_jump(f_j, 0.045, 0.031, 0.6, 0.05)
assert g_star > growth_jump(0.9 * f_j, 0.045, 0.031, 0.6, 0.05)
assert g_star > growth_jump(1.1 * f_j, 0.045, 0.031, 0.6, 0.05)

# The Q-measure proof: under the credit triangle there is no edge
assert kelly_jump(0.045, 0.045 / 0.6, 0.6) < 1e-9

# Fractional Kelly: exact 75% at half Kelly for quadratic growth; Monte Carlo check of (28.13)
f_d = kelly_jump(0.03, 0.0, 0.6, sigma=0.10)                   # pure diffusion: mu / sigma^2 = 3
assert abs(f_d - 3.0) < 1e-12
assert abs(growth_jump(0.5 * f_d, 0.03, 0.0, 0.6, 0.10) / growth_jump(f_d, 0.03, 0.0, 0.6, 0.10) - 0.75) < 1e-12
eps = RNG.normal(0.0, 1.0, size=200_000)                       # relative s.e. of the edge = 100%
thetas = np.linspace(0.05, 1.5, 146)
ratio = [np.mean(2 * t * (1 + eps) - (t * (1 + eps)) ** 2) for t in thetas]
assert abs(thetas[int(np.argmax(ratio))] - kelly_multiplier(1.0)) < 0.03

# Random recovery: Jensen lowers f*, and the worst recovery sets the boundary
f_const = kelly_jump(0.045, 0.031, 0.6)
f_loose = kelly_random_loss(0.045, 0.031, 3.0, 2.0, 1.00)      # mean L = 0.6, docs allow L -> 1
f_tight = kelly_random_loss(0.045, 0.031, 8.0, 2.0, 0.75)      # mean L = 0.6, recovery floor 25%
assert f_loose < f_tight < f_const
assert f_loose < 1.0 and f_tight < 1.0 / 0.75

# Clusters: a common jump shrinks every name, and the cluster obeys sum f L < 1
f_alone = kelly_jump(0.084, 0.04 + 0.02, 0.55)
f_clu = kelly_cluster(5, 0.084, 0.04, 0.02, 0.55)
assert 0.0 < f_clu < f_alone and 5 * f_clu * 0.55 < 1.0
assert kelly_cluster(5, 0.084, 0.04, 0.03, 0.55) < f_clu

# The 2026 CCC case: the edge rose while Kelly fell
f_jan, f_oct = kelly_jump(0.084, 0.06, 0.55), kelly_jump(0.128, 0.10, 0.70)
assert (0.128 - 0.10 * 0.70) > (0.084 - 0.06 * 0.55) and f_oct < 0.6 * f_jan
```

Edge cases ROBO must handle: an edge of exactly zero returns zero, not a division by zero; `lam = 0` falls back to the diffusion fraction and is the only case where the ruin boundary does not apply; a Beta recovery with $a < 1$ or $b < 1$ has an unbounded density at an endpoint, which `quad` integrates but slowly, so the spec requires $a, b \ge 1$ for production fits; and every output fraction is a fraction of NAV *before* the cluster cap, the fractional multiplier and the leverage band of §28.7 are applied, in that order.

## 28.5 LVaR, Days-to-Liquidate and the 5× Problem

The risk officer marks to bid. Theo thinks this is a technicality until Ines explains what it does to his P&L on the day the bid moves. A long bond marked at the bid loses money when the bid-ask widens, whether or not anything has happened to the issuer. A short bond marked at the offer loses money too. On a gross book the bid-ask is a short volatility position, and it is short exactly the volatility that arrives with every stress.

> **[SOURCE EXTRACTION]** *Ben_Dor_Quantitative_Credit_Portfolio_Management p.112:* "We define LCS as the bond's OASD multiplied by this spread. Consequently, a bond's LCS can be interpreted as the cost, in percentage points, of immediately executing a roundtrip transaction." … "Over this time period, the LCS for the IG Index ranged from 0.59% to 3.40%."
>
> **Annotation.** The period is January 2007 to June 2009, and the move from 0.59% (January 2007) to 3.40% (November 2008) is a 5.8× widening of the round-trip cost of the US IG index. The same page notes that the index's LCS had already doubled between June and September 2007, more than a year before Lehman, and the next page that the HY-minus-IG gap went from about 40 bp to more than 400 bp. So "bid-ask widens 5×" is not a stress scenario somebody made up for a risk committee. It is the 2007–2008 base case for investment grade, and HY was worse. The modern departure is speed: in March 2020 IG costs roughly tripled in three weeks (below), and in March 2026 EUR IG spreads rose 64% above their January average in days. The multiplier is a parameter, and it has to sit inside the sizing before the stress, because afterwards it sits inside the P&L.

### From Bangia's LVaR to a credit LVaR

Bangia, Diebold, Schuermann and Stroughair (1998/99, *Modeling Liquidity Risk, With Implications for Traditional Market Risk Measurement and Management*) add the cost of liquidation to parametric VaR. For a position of value $P$ with daily log-return volatility $\sigma$,

$$
\text{VaR} = P\left[1 - e^{-2.33\,\sigma}\right], \qquad \text{COL} = \tfrac12 P\left(\bar S + a\,\tilde\sigma\right), \qquad \text{LVaR} = \text{VaR} + \text{COL}, \tag{28.15}
$$

where $S = (\text{Ask} - \text{Bid})/\text{Mid}$ is the relative spread, $\bar S$ and $\tilde\sigma$ are its mean and volatility, and the multiplier $a$ "ranges from 2.0 to 4.5 depending on the instrument" (they measured 2.5 for JPY and 3.5 for THB in 1997–98). The factor $\tfrac12$ is there because liquidating at the bid costs half the bid-ask. Two translations make it a credit formula.

First, for a spread-quoted bond the relative bid-ask in price terms *is* the LCS, so $\text{COL}_i = \tfrac12 |\text{MV}_i| \cdot \text{LCS}_i^{\text{stress}}$, and shorts pay at the offer just as longs pay at the bid. Second, the $\bar S + a\tilde\sigma$ form does not reach 5× in practice. To get from 0.59% to 3.40% you need $a\tilde\sigma = 2.81$ points; a calm-window $\tilde\sigma$ of 0.10–0.20 points *(illustrative)* would need $a$ between 14 and 28, four to ten times Bangia's FX range. Credit liquidity does not wiggle around a mean. It jumps between regimes. So the desk carries a multiplicative stress factor $m$ instead:

$$
\text{COL}_i^{\text{exo}} = \tfrac12\, m\, \overline{\text{LCS}}_i\, |\text{MV}_i|, \qquad m \in \{1.64,\ 3,\ 5.8,\ 6\},
$$

with the menu calibrated to EUR IG in March 2026 (+64%), IG costs in March 2020 (about 3×), the IG index in 2007–2008 (5.8×), and IG blocks in March 2020 (more than 6×), all sourced in this section.

Bangia's model covers only *exogenous* liquidity, the market-wide spread. The *endogenous* part is that your own size moves the price. Man's modelled HY transaction costs by ticket size, \$1mm to \$20mm, span roughly 0.5% to 4.0% of price over 2004–2021 (Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.22, read from a chart), so the cost of a ticket is a function of the ticket. We use the simplest form that respects that evidence:

$$
\text{COL}_i = \tfrac12\, m\, \overline{\text{LCS}}_i\, |\text{MV}_i| \left(1 + \eta \sqrt{\frac{|\text{MV}_i|}{\text{ADV}_i}}\right), \tag{28.16}
$$

with $\eta$ fitted to the desk's own markouts by ticket size *(functional form illustrative)*. Because (28.16) grows faster than linearly in position size, the liquidity cost of the whole book grows faster than linearly in leverage, and that is what turns the leverage ceiling of §28.7 into a fixed point.

### Days-to-liquidate, and the regulatory clocks

A position of $q_i$ dollars in a bond that trades $\text{ADV}_i$ a day, sold at a participation rate $\pi$, takes

$$
T_i = \frac{q_i}{\pi\,\text{ADV}_i} \tag{28.17}
$$

days to exit. Paleologo's example (p.126) is a position of two days' volume at 4% participation: 50 days. For a HY bond that trades \$5mm a day, a \$25mm position at 10% participation is also 50 days *(illustrative)*, which is to say most of a quarter. VaR over a liquidation horizon scales the one-day risk by roughly $\sqrt{T_i}$, and the Basel FRTB rules make that scaling explicit. With base horizon $T = 10$ days and liquidity horizons $LH_j \in \{10, 20, 40, 60, 120\}$, the liquidity-adjusted expected shortfall is

$$
\text{ES} = \sqrt{\text{ES}_T(P)^2 + \sum_{j \ge 2}\left(\text{ES}_T(P, j)\sqrt{\frac{LH_j - LH_{j-1}}{T}}\right)^2}, \tag{28.18}
$$

where $\text{ES}_T(P, j)$ is the 10-day ES from shocking only the risk factors with horizon at least $LH_j$ (Basel Framework MAR33.4; horizons in MAR33.12). A book whose risk is all HY corporate spread (60 days) has $\text{ES} = \text{ES}_T\sqrt{1 + 1 + 2 + 2} = \text{ES}_T\sqrt{6} = \text{ES}_T\sqrt{60/10}$, which is the square-root-of-time rule recovered as a sanity check. For a registered fund, the clock is SEC Rule 22e-4: "highly liquid" means convertible to cash within three business days, "illiquid" means not reasonably expected to be sold in seven calendar days without significantly changing the market value, and illiquid holdings are capped at 15% of net assets.

Which bonds do you sell first? Ben Dor's answer is counterintuitive.

> **[SOURCE EXTRACTION]** *Ben_Dor_Quantitative_Credit_Portfolio_Management p.112:* "a strategy of selling illiquid bonds at the beginning of a liquidity crisis may be more productive than selling liquid bonds first."
>
> **Annotation.** The logic is the cost of waiting. If the LCS of the illiquid bucket widens faster as the crisis deepens, every day you hold it raises its exit cost, so you sell it while the bid exists. In March 2020 most investors did the opposite and sold their most liquid bonds first (O'Hara and Zhou, 2021, *Anatomy of a Liquidity Crisis: Corporate Bonds in the COVID-19 Crisis*, *Journal of Financial Economics*), because that was where the bids were. For a fund with redeemable shares the choice has a second edge: selling liquid bonds first to meet early redemptions leaves the illiquid ones for the investors who stay, which rewards running. That is the next case.

### Case Study: Third Avenue Focused Credit Fund, December 2015

The facts are from the SEC's temporary order (Investment Company Act Release No. 31943, 16 December 2015). The Focused Credit Fund had "\$1.1 billion in estimated net outflows for the year to date through December 9, 2015, which was more than 145% of its remaining net asset value at that date," which puts the remaining NAV near \$0.75bn. Net redemptions in November alone were \$317mm, and the institutional NAV per share fell from \$7.81 to \$7.08 that month. By early December the fund had raised cash to "over \$200 million." On 9 December its board adopted a plan of liquidation, sales of shares were suspended from 10 December, and the SEC's order under §22(e)(3) permitted the suspension of redemptions. The SEC noted that institutional holders would otherwise have redeemed first, to the detriment of retail investors. The unwind took roughly a year.

Now run Theo's 13-week model on the *fund*. Cash of about \$200mm against a burn of about \$73mm a week (\$317mm over November's 4.3 weeks) is a runway of about 2.7 weeks. In the RSSG seat, a borrower with under one quarter of liquidity runway is a going-concern question and a first-day-of-engagement conversation. The fund was the borrower, its redemptions were the debt service, and its portfolio of distressed and stressed bonds was the collateral that could not be sold at the mark in seven calendar days. A systematic desk would have flagged it from public data: a fund-level runway under 13 weeks, a high share of tier-2 holdings, NAV falling while outflows accelerated, and a liquidation cost under (28.16) that was a large fraction of NAV. It would then have done two things. It would not have bought what the fund was certain to sell until the fund had sold it, and it would have been ready with capacity to provide liquidity after the gate, when the price of immediacy was highest and the information content of the selling was lowest (forced, not informed). Ines calls this "the only hand where you know the other player has to fold."

The 13-week model, it turns out, was never about the borrower. It was about the gap between when cash leaves and when assets can be sold, and every leveraged book has that gap.

### Specification for AI Implementation (Block 4): LVaR, Days-to-Liquidate and Runway

What ROBO built from the vague version ("compute liquidity risk"): the average bid-ask over the last year, times the book. It reported \$4mm. The stressed figure was \$23mm *(illustrative)*, and ROBO's comment field read "liquidity is fine on average."

```python
# --- Block 4: LVaR, days-to-liquidate, FRTB scaling, runway ---------------------
STRESS_MULTIPLIERS = {"eur_ig_mar2026": 1.64, "ig_costs_mar2020": 3.0,
                      "ig_index_2007_08": 3.40 / 0.59, "ig_blocks_mar2020": 6.0}
FRTB_LH = np.array([10, 20, 40, 60, 120])                 # MAR33.12 liquidity horizons, days


def parametric_var(value, sigma_1d, z=2.33):
    """Bangia eq. (3): P [1 - exp(-z sigma)]."""
    return value * (1.0 - np.exp(-z * sigma_1d))


def bangia_col(value, spread_mean, spread_sd, a):
    """Bangia eq. (4): 0.5 P (S_bar + a sigma_S). Spreads are relative (fraction of mid)."""
    return 0.5 * value * (spread_mean + a * spread_sd)


def credit_col(mv, lcs_mean, adv, mult=1.0, eta=0.0):
    """Eq. (28.16): exogenous stress multiple times an endogenous size term. Longs AND shorts pay."""
    mv = np.abs(np.asarray(mv, dtype=float))
    adv = np.maximum(np.asarray(adv, dtype=float), 1.0)          # guard: no zero-ADV division
    return 0.5 * mult * np.asarray(lcs_mean) * mv * (1.0 + eta * np.sqrt(mv / adv))


def days_to_liquidate(position, adv, participation):
    """Eq. (28.17)."""
    if participation <= 0.0:
        raise ValueError("participation must be positive")
    return np.abs(position) / (participation * np.maximum(adv, 1.0))


def frtb_liquidity_es(es_by_bucket, horizons=FRTB_LH, base=10):
    """Eq. (28.18). es_by_bucket[j] = 10-day ES shocking factors with LH >= horizons[j]."""
    es = np.asarray(es_by_bucket, dtype=float)
    widths = np.diff(horizons)
    return float(np.sqrt(es[0] ** 2 + np.sum((es[1:] * np.sqrt(widths / base)) ** 2)))


def runway_weeks(cash, liquid_sleeve, weekly_burn, haircut=0.0):
    """Theo's 13-week model, pointed at the fund: (cash + haircut liquid sleeve) / burn."""
    if weekly_burn <= 0.0:
        return np.inf
    return (cash + (1.0 - haircut) * liquid_sleeve) / weekly_burn


# Paleologo's example: two days of volume at 4% participation takes 50 days
assert abs(days_to_liquidate(2.0, 1.0, 0.04) - 50.0) < 1e-12
# FRTB: all risk in HY corporate spread (LH 60) recovers sqrt(60 / 10)
assert abs(frtb_liquidity_es([1, 1, 1, 1, 0]) - np.sqrt(6.0)) < 1e-12
assert abs(frtb_liquidity_es([1, 0, 0, 0, 0]) - 1.0) < 1e-12
# Bangia's a-sigma form cannot reach the 2008 multiple with a calm-window sigma
implied_a = (3.40 - 0.59) / 0.15                              # sigma_S = 0.15 points (illustrative)
assert implied_a > 4.5 * 3
# The 5x problem on a $2bn gross IG book at 0.6% LCS
col_calm = credit_col([2e9], [0.006], [1e12])[0]
col_2008 = credit_col([2e9], [0.006], [1e12], mult=STRESS_MULTIPLIERS["ig_index_2007_08"])[0]
assert abs(col_calm - 6e6) < 1.0 and abs(col_2008 / col_calm - 3.40 / 0.59) < 1e-12
# Endogenous size term: cost per dollar rises with size
small = credit_col([5e6], [0.01], [5e6], eta=0.5)[0] / 5e6
large = credit_col([25e6], [0.01], [5e6], eta=0.5)[0] / 25e6
assert large > small
# Third Avenue, December 2015: about 2.7 weeks of runway, far inside 13
ta_runway = runway_weeks(cash=200e6, liquid_sleeve=0.0, weekly_burn=317e6 / (30 / 7))
assert 2.5 < ta_runway < 3.0 and ta_runway < 13.0
```

Edge cases: zero ADV (a bond that has not traded in the window) is floored at \$1 so the size term is enormous rather than infinite, which is the right sign; a negative weekly burn (net inflows) gives infinite runway; and `credit_col` deliberately takes absolute values, because a short pays the offer just as a long pays the bid.

## 28.6 Drawdown Control: The Two-Threshold Rule, the PM Option and Marking to Bid

The platforms' drawdown rule, as commonly reported, is two numbers: lose 5% of allocated capital and your capital is halved; lose another 2.5% and you are out (WSJ via eFinancialCareers, 5 December 2025; the firm did not comment). Theo's four PMs know the rule better than they know their own positions. The desk head's job is to understand what the rule is for, what it costs, and how a credit book can trip it without anything going wrong.

> **[SOURCE EXTRACTION]** *Paleologo_Advanced_Portfolio_Management p.164:* "Stop-loss rules are a partial hedge for the PM call option. … it is in the interest of the manager to run with the highest possible volatility, independently of her skill."
>
> **Annotation.** A PM paid a fraction $\varphi$ of positive annual P&L $\Pi$ holds a call. If $\Pi \sim N(\mu, \sigma^2)$, the payout is worth $\varphi\left[\mu\,\Phi(\mu/\sigma) + \sigma\,\phi(\mu/\sigma)\right]$, and its derivative with respect to $\sigma$ is $\varphi\,\phi(\mu/\sigma) > 0$ for every $\mu$, skilled or not. The stop-loss caps how much volatility the PM can harvest before the option is taken away. In credit there is a second, sneakier volatility: concentration in names with jump-to-default. A PM can sell default insurance, collect carry for three years, and look like a low-volatility genius until the jump. The stop-loss does not hedge that, because the jump arrives in one print. The Kelly cluster bound of §28.4 does.

### Setting the stop with drift

Model the PM's cumulative P&L as a fraction of allocated capital, $X_t = \mu t + \sigma W_t$ with $\mu = \text{SR}\cdot\sigma$. The probability of touching $-x$ before time $T$ is the classical first-passage result for Brownian motion with drift,

$$
\Pr\left(\min_{t \le T} X_t \le -x\right) = \Phi\!\left(\frac{-x - \mu T}{\sigma\sqrt{T}}\right) + e^{-2\mu x/\sigma^2}\,\Phi\!\left(\frac{-x + \mu T}{\sigma\sqrt{T}}\right), \tag{28.19}
$$

and as $T \to \infty$ the lifetime probability is $e^{-2\mu x/\sigma^2} = e^{-2\,\text{SR}\,x/\sigma}$. Inverting gives the stop that a desk head would set for a target lifetime stop-out probability $P$:

$$
x = \frac{\sigma\,\ln(1/P)}{2\,\text{SR}}. \tag{28.20}
$$

A PM running 6% volatility with a Sharpe of 1, held to a 10% lifetime stop-out probability, gets $x = 0.06 \times 2.303/2 = 6.9\%$, close to the reported 7.5%. At 7.5%, the lifetime probability is $e^{-2.5} = 8.2\%$, and the one-year probability from (28.19) is about 4.5%. A PM with a Sharpe of 0.5 at the same volatility and stop faces a lifetime probability of $e^{-1.25} = 29\%$. The rule is the same for both, and its price is not.

> **[SOURCE EXTRACTION]** *Paleologo_Advanced_Portfolio_Management p.167:* "a two-threshold one (cut capital in half when loss reaches (x/2)%, and liquidate at x% loss). To approximate heavy-tailed returns … returns distribution in the simulation is not Gaussian, but a Student with 6 degrees of freedom." … "The price of safety is higher for lower-Sharpe PMs than higher-Sharpe ones."
>
> **Annotation.** This is the platform rule, simulated. Because the cuts are decided on past P&L and returns are independent of the past, expected P&L under the rule is exactly $\mu$ times expected capital-time, so the price of safety is $\mu$ times the capital-time the rule takes away. Low-Sharpe PMs lose more capital-time, because they hit the first threshold more often. Paleologo's companion line (p.166) is the one to read aloud at the risk committee: "Stop-loss exists to ensure survival of a firm, not to improve the performance of a strategy. There is a price to pay." Block 5 reproduces the simulation and its ranking.

Two credit-specific notes on the rule. First, Grossman and Zhou (1993, *Optimal Investment Strategies for Controlling Drawdowns*) show that the smooth version of the rule keeps exposure proportional to the cushion above the drawdown floor, $\text{exposure}_t = k\,(X_t - (1-x)M_t)$ with $M_t$ the running maximum, which never breaches the floor in continuous time. The two-threshold rule is a two-step approximation of that policy, and it is the approximation the platforms can audit. Second, do not use ratings as stop-losses. Dynkin et al. find that rating-based stop-loss rules "lead to lower portfolio returns" at every threshold they test, with risk reductions much smaller than the returns given up, because downgraded bonds tend to outperform their new rating peers (Dynkin p.419). Use rating as an entry rule, not an exit rule.

### The stop-loss you don't know you have

Paleologo writes (p.163) that "there is the stop-loss that you have, and the one you don't know you have." In credit, the one you don't know you have is the mark. Let a book with gross leverage $G$ be marked to bid on longs and offer on shorts, with average round-trip cost $\overline{\text{LCS}}$. When the bid-ask widens by a factor $m$, the marks move by half the change, and the drawdown in NAV, with no change in any issuer, is

$$
\Delta^{\text{mark}} = \tfrac12\,(m - 1)\,\overline{\text{LCS}}\;G. \tag{28.21}
$$

Theo's desk: $\overline{\text{LCS}} = 0.6\%$, $G = 5$, and the 2007–2008 multiple $m = 5.8$ give $\Delta^{\text{mark}} = 0.5 \times 4.8 \times 0.006 \times 5 = 7.2\%$ of NAV. That is through the 5% cut and within 30 bp of the 7.5% exit, from marks alone. The effective stop is $x - \Delta^{\text{mark}}$. If it is not budgeted before the stress, the rule fires at the bottom, on the day the price of immediacy is highest, and forces the desk to sell to the people who budgeted for it.

> **[SOURCE EXTRACTION]** *BlackRock_Systematic_High_Yield_Credit p.5:* "these managers gave up more excess return in subsequent "Very Positive" regimes than was mitigated on the downside during "Very Negative""
>
> **Annotation.** BlackRock's sample covers the 2013 taper tantrum, 2018, 2020 and 2022, and its finding is that the defensive HY managers who de-risked on the way down lost more on the rebound than they saved. A forced de-risking caused by marks is the worst version of this, because it sells for a reason unrelated to the forecast. Blackstone's systematic credit description states the mirror image: "When credit spreads widen aggressively (often due to market panic rather than fundamental deterioration), the model algorithmically increases credit exposure" (Blackstone_Systematic_Credit p.1). That is possible only for a book whose drawdown budget survived the marks.

### Case Study: March 2020 and March 2026

*March 2020.* The Fed's own retrospective (Sharpe and Zhou, FEDS Notes, 7 October 2020) has IG transaction costs rising from about 30 bp in February to nearly 90 bp in mid-March, IG block-trade costs from 24 bp to over 150 bp by 23 March, and bond mutual fund outflows above \$250bn in March, about 5% of assets. Kargar et al. (NBER WP 27355; *Review of Financial Studies* 2021) estimate that customers' willingness to pay for immediacy rose by about 200 bp per dollar traded at the peak. On 23 March the Fed announced the Secondary Market Corporate Credit Facility. Treat the block-cost numbers as round-trip LCS *(an assumption)*, and (28.21) puts the mark-to-bid hit on a 5× IG book at $\tfrac12 \times (1.50\% - 0.24\%) \times 5 = 3.2\%$ of NAV, two-thirds of the way to the first threshold with no default anywhere. A desk whose rule ignored the marks was cut in the week the Fed announced it would buy. A desk that had budgeted (28.21) kept its gross, and was among the buyers.

*March 2026.* The Iran-war shock forced an unwind of crowded positions, and ExodusPoint, Balyasny, Citadel and Millennium all posted March declines, giving up all or part of their gains from the first two months (Bloomberg, 2 April 2026). HY OAS peaked at 3.46% on 30 March (FRED). EUR IG bid-ask rose to 64% above its January average, and normalizing took 4 weeks in EUR IG, 6 in US HY, 8 in US IG, 13 in EUR HY and more than 14 in EM (MarketAxess data via The DESK, 1 October 2026). The lesson is about correlation of rules, not of assets. When many pods at many firms share a 5% line and similar positions, their stops are one stop. A desk head should estimate, from positioning data and crowding measures (Chapter 9), how much of the book's exposure belongs to trades that other people will be forced out of at the same threshold, and treat that share as having a higher $m$.

### Specification for AI Implementation (Block 5): Stops, Hitting Probabilities and the Mark-to-Bid Shock

What ROBO built from the vague version ("minimize drawdown"): it held cash, as it always does, and reported a maximum drawdown of zero and a Sharpe ratio of "undefined, but excellent."

```python
# --- Block 5: drawdown rules ----------------------------------------------------
def prob_hit(x, mu, sigma, horizon):
    """Eq. (28.19): P(min X_t <= -x by T) for X_t = mu t + sigma W_t."""
    s = sigma * np.sqrt(horizon)
    return (stats.norm.cdf((-x - mu * horizon) / s)
            + np.exp(-2.0 * mu * x / sigma ** 2) * stats.norm.cdf((-x + mu * horizon) / s))


def stop_for_lifetime_prob(prob, sharpe, sigma):
    """Eq. (28.20): x = sigma ln(1/P) / (2 SR)."""
    return sigma * np.log(1.0 / prob) / (2.0 * sharpe)


def mark_to_bid_shock(gross_leverage, lcs_mean, mult, already_at_bid=True):
    """Eq. (28.21): NAV drawdown from bid-ask widening alone, as a fraction of NAV."""
    widen = (mult - 1.0) if already_at_bid else mult
    return 0.5 * widen * lcs_mean * gross_leverage


def mc_prob_hit(x, mu, sigma, horizon, n_paths, n_steps, rng):
    """Brownian-bridge Monte Carlo of (28.19): exact for continuous monitoring."""
    dt = horizon / n_steps
    incr = mu * dt + sigma * np.sqrt(dt) * rng.standard_normal((n_paths, n_steps))
    path = np.concatenate([np.zeros((n_paths, 1)), np.cumsum(incr, axis=1)], axis=1)
    d = path + x                                           # distance above the barrier
    below = (d <= 0.0).any(axis=1)
    d0, d1 = np.maximum(d[:, :-1], 0.0), np.maximum(d[:, 1:], 0.0)
    survive = np.prod(1.0 - np.exp(-2.0 * d0 * d1 / (sigma ** 2 * dt)), axis=1)
    survive[below] = 0.0
    return 1.0 - survive.mean()


def simulate_two_threshold(sharpe, sigma, x, shocks):
    """Paleologo's rule: halve capital at loss x/2, liquidate at loss x (on initial capital).
    shocks: (n_paths, n_days) unit-variance Student-t(6) draws, reused across Sharpes."""
    n_paths, n_days = shocks.shape
    mu_d, sd_d = sharpe * sigma / n_days, sigma / np.sqrt(n_days)
    r = mu_d + sd_d * shocks
    cap, pnl = np.ones(n_paths), np.zeros(n_paths)
    for t in range(n_days):
        pnl += cap * r[:, t]
        cap = np.where(pnl <= -x, 0.0, np.where(pnl <= -x / 2.0, np.minimum(cap, 0.5), cap))
    free = r.sum(axis=1)
    price_of_safety = 1.0 - pnl.mean() / free.mean()       # share of expected P&L given up
    return {"mean_pnl": pnl.mean(), "p_out": float(np.mean(cap == 0.0)),
            "price_of_safety": price_of_safety}


# The reported 7.5% stop is what (28.20) gives a Sharpe-1, 6%-vol PM at ~8% lifetime odds
assert abs(stop_for_lifetime_prob(np.exp(-2.5), 1.0, 0.06) - 0.075) < 1e-12
p1 = prob_hit(0.075, 0.06, 0.06, 1.0)
assert 0.040 < p1 < 0.050
p1_mc = mc_prob_hit(0.075, 0.06, 0.06, 1.0, 10_000, 252, RNG)
assert abs(p1_mc - p1) < 0.01, (p1_mc, p1)

# Paleologo's ranking: the price of safety falls with the Sharpe ratio (t6 shocks, common draws)
t6 = stats.t.rvs(df=6, size=(20_000, TRADING_DAYS), random_state=RNG) / np.sqrt(6.0 / 4.0)
pos = [simulate_two_threshold(sr, 0.06, 0.075, t6)["price_of_safety"] for sr in (0.5, 1.0, 2.0)]
assert pos[0] > pos[1] > pos[2] >= 0.0, pos

# Theo's desk: G = 5, LCS 0.6%, the 2007-08 multiple -> through the 5% line on marks alone
shock = mark_to_bid_shock(5.0, 0.006, 3.40 / 0.59)
assert 0.05 < shock < 0.075
assert abs(mark_to_bid_shock(5.0, 0.006, 5.8) - 0.072) < 1e-12
```

Edge cases: `prob_hit` requires $\sigma > 0$ and $T > 0$; a negative $\mu$ is allowed (a losing PM) and the formula still holds; `stop_for_lifetime_prob` is undefined for a non-positive Sharpe ratio, for which every stop is eventually hit; and the two-threshold simulation must measure loss on *initial* allocated capital, as Paleologo specifies, because measuring it on current capital after the cut silently moves the exit.

## 28.7 The Leverage Band and the κ Problem

Every term is now on the table, and they assemble into the one equation to tape to the monitor. The floor is (28.2). The ceiling comes from the drawdown limit. Let the book's annual NAV return be $G(\mu_{\text{GMV}} + \kappa\,\sigma_{\text{GMV}} Z)$, with $\sigma_{\text{GMV}} = \sigma_{\text{DTS}}/\sqrt{N_{\text{eff}}}$, $\mu_{\text{GMV}} = \text{SR}\,\sigma_{\text{GMV}}$, $Z$ a standardized shock with distribution $F$, and $\kappa \ge 1$ the factor by which realized volatility exceeds predicted volatility in a drawdown. Require $\Pr(\text{loss} > \text{DD}_{\max}) \le p_{\text{loss}}$ (we write $\text{DD}_{\max}$, not $D_{\max}$, because $D$ is duration). With $z_p = -F^{-1}(p_{\text{loss}})$, the condition is $G\sigma_{\text{GMV}}(\kappa z_p - \text{SR}) \le \text{DD}_{\max}$. In credit the drawdown budget must also absorb the liquidation and mark-to-bid cost $\text{COL}(G)$, as a fraction of NAV, which arrives in the same tail event. So

$$
\frac{\sqrt{N_{\text{eff}}}}{\sigma_{\text{DTS}}}\cdot\frac{r_{\min}}{\text{SR}} \;\le\; G \;\le\; \frac{\sqrt{N_{\text{eff}}}}{\sigma_{\text{DTS}}}\cdot\frac{\text{DD}_{\max} - \text{COL}(G)}{\kappa z_p - \text{SR}}. \tag{28.22}
$$

The ceiling is a fixed point, because $\text{COL}$ grows with $G$. With the linear mark-to-bid cost of (28.21), $\text{COL}(G) = c_1 G$ with $c_1 = \tfrac12(m-1)\overline{\text{LCS}}$, and writing $A = \sqrt{N_{\text{eff}}}/(\sigma_{\text{DTS}}(\kappa z_p - \text{SR}))$,

$$
G_{\max} = \frac{A\,\text{DD}_{\max}}{1 + A\,c_1} \;<\; \frac{\text{DD}_{\max}}{c_1} = \frac{2\,\text{DD}_{\max}}{(m-1)\,\overline{\text{LCS}}}. \tag{28.23}
$$

The right-hand bound is the **liquidity speed limit**: no amount of breadth, Sharpe or model confidence takes a credit book's leverage above it, because as $A \to \infty$ the ceiling converges to it. At $\text{DD}_{\max} = 7.5\%$, $m = 5.8$ and $\overline{\text{LCS}} = 0.8\%$, the speed limit is $0.15/0.0384 = 3.9\times$.

> **[SOURCE EXTRACTION]** *Paleologo_Advanced_Portfolio_Management p.175–176:* "we … assume that realized portfolio volatility is inflated by a positive factor κ … with values between 1 (if we really believe in models) and 3 (if we are skeptical)." … "In practice, we want to set −κF⁻¹(p_loss) between 4 and 6."
>
> **Annotation.** In credit, $\kappa$ has an observable cousin: the ratio of stressed to calm relative-spread volatility, $\sigma_{\text{rel}}$ in a stress window over $\sigma_{\text{rel}}$ in the calibration window. Estimate it by bucket, because the CCC ratio in 2026 is not the IG ratio. And note that credit has two stress multipliers, not one: $\kappa$ inflates the volatility, and $m$ inflates the bid-ask. They hit together, which is why (28.22) charges both in the same tail.

Theo's HY PM: $N_{\text{eff}} = 40$, $\sigma_{\text{DTS}} = 5\%$, $\text{SR} = 2$, $\kappa z_p = 4$, $\text{DD}_{\max} = 7.5\%$ and $r_{\min} = 5\%$ *(all illustrative)*. Without liquidity, the band is $[3.16,\ 4.74]$. Charge the 2008 mark-to-bid with $\overline{\text{LCS}} = 0.8\%$ and the ceiling falls to $4.74/(1 + 63.2 \times 0.0192) = 2.14$, below the floor. **The band is empty.** The liquidity term closed it. The desk head has four levers, and all of them are in this chapter: cut $\overline{\text{LCS}}$ (route beta management to the overlay, use smaller tickets and PT, §28.3), lower the PM's hurdle $r_{\min}$, buy a wider drawdown limit with a lower $p_{\text{loss}}$ elsewhere on the platform, or raise $\text{SR}$ by adding uncorrelated signals (§28.8). Halving the LCS and accepting a 4% hurdle reopens the band at about $[2.5,\ 3.0]$.

> **Desk Myth vs. Desk Reality.** *Myth:* "A higher-Sharpe PM needs less leverage." *Reality:* a higher Sharpe *requires* less (the floor falls) and *permits* more (the ceiling rises, because $\kappa z_p - \text{SR}$ shrinks). Paleologo makes the same point about the idiosyncratic share of variance, $p_{\text{idio}}$ (p.178): "When the percentage idio p_idio increases, it works its magic on both sides of the equation: the lower admissible leverage decreases and the highest admissible leverage increases." IDO or it didn't happen, in leverage form: idiosyncratic risk is the only risk that widens the band from both ends.

### Specification for AI Implementation (Block 6): The Leverage Band

What ROBO built from the vague version ("use as much leverage as is safe"): the ceiling without the floor, and without COL. It reported 4.74× and the word "safe."

```python
# --- Block 6: the leverage band -------------------------------------------------
def leverage_floor(n_eff, sigma, r_min, sharpe):
    """Eq. (28.2)."""
    return np.sqrt(n_eff) / sigma * r_min / sharpe


def leverage_ceiling(n_eff, sigma, dd_max, sharpe, kappa_z, col_fn=None):
    """Eq. (28.22): fixed point G = A (DD_max - COL(G)); COL(G) is a fraction of NAV, increasing."""
    if kappa_z <= sharpe:
        raise ValueError("kappa * z_p must exceed the Sharpe ratio")
    a = np.sqrt(n_eff) / (sigma * (kappa_z - sharpe))
    if col_fn is None:
        return a * dd_max
    h = lambda g: g - a * (dd_max - col_fn(g))
    hi = a * dd_max
    return hi if h(hi) <= 0.0 else optimize.brentq(h, 0.0, hi, xtol=1e-12)


def liquidity_speed_limit(dd_max, lcs_mean, mult):
    """Eq. (28.23), right-hand side: 2 DD / ((m - 1) LCS)."""
    return 2.0 * dd_max / ((mult - 1.0) * lcs_mean)


m08 = 5.8
c1 = 0.5 * (m08 - 1.0) * 0.008
lo = leverage_floor(40, 0.05, 0.05, 2.0)
hi_dry = leverage_ceiling(40, 0.05, 0.075, 2.0, 4.0)
hi_wet = leverage_ceiling(40, 0.05, 0.075, 2.0, 4.0, col_fn=lambda g: c1 * g)
a_band = np.sqrt(40) / (0.05 * 2.0)
assert abs(lo - 3.162) < 1e-3 and abs(hi_dry - 4.743) < 1e-3
assert abs(hi_wet - a_band * 0.075 / (1 + a_band * c1)) < 1e-9     # closed form (28.23)
assert hi_wet < lo < hi_dry                                        # liquidity closes the band
assert leverage_ceiling(10**8, 0.05, 0.075, 2.0, 4.0, lambda g: c1 * g) < liquidity_speed_limit(0.075, 0.008, m08)
assert abs(liquidity_speed_limit(0.075, 0.008, m08) - 0.075 / c1) < 1e-12
c1_half = 0.5 * (m08 - 1.0) * 0.004                                # halve LCS, accept a 4% hurdle
assert leverage_floor(40, 0.05, 0.04, 2.0) < leverage_ceiling(40, 0.05, 0.075, 2.0, 4.0, lambda g: c1_half * g)
```

Edge cases: $\kappa z_p \le \text{SR}$ means the PM's Sharpe exceeds the stress quantile and the formula has no ceiling, which is a sign the inputs are wrong, so the function raises; `col_fn` must be increasing in $G$ for the fixed point to be unique; and the floor uses the *forecast* Sharpe, so a floor computed from a backtest Sharpe is a floor computed from the wrong number (deflate it, Chapter 26).

## 28.8 Running Ex-RSSG Analysts Alongside PhDs

Sunita is explaining a fulcrum analysis to Kaz. Kaz, delighted, asks whether the fulcrum security is "the one at the pivot of the lever, where a small force moves a large load." Sunita says yes, actually: it is the class where value breaks, so a small change in enterprise value moves its recovery the most. Kaz has, for once, read a legal term correctly by reading it as physics. It is the right picture of the team: two vocabularies for one sensitivity.

The team is a production function. Two signals with information coefficients $\text{IC}_1$, $\text{IC}_2$ and correlation $\rho$, combined optimally (regress the forward return on both standardized signals), have a combined IC equal to the multiple correlation,

$$
\text{IC}_c^2 = \mathbf{ic}^{\top} C^{-1}\, \mathbf{ic} = \frac{\text{IC}_1^2 + \text{IC}_2^2 - 2\rho\,\text{IC}_1\text{IC}_2}{1 - \rho^2}. \tag{28.24}
$$

Two signals with IC 0.05 each combine to 0.056 if they correlate at 0.6 (another price factor), 0.071 if they are uncorrelated (a docket or covenant signal), and 0.079 at $\rho = -0.2$. The value of an ex-RSSG analyst to a quant book is mostly the $\rho$, not the IC: documents, dockets and process are information the price factors do not contain.

Breadth has a cost the formula hides. Suppose a PM's edge per bet dilutes as coverage grows, $e(N) = e_0 N_c/(N + N_c)$, with $N_c$ the coverage at which attention halves the edge. Then $\text{IR} \propto e(N)\sqrt{N} \propto \sqrt{N}/(N + N_c)$, whose derivative vanishes where $N + N_c = 2N$:

$$
N^\ast = N_c. \tag{28.25}
$$

Optimal coverage equals the dilution scale. Past it, each new name lowers the IR. A team helps only by adding coverage at the *new* member's own $N_c$, not by stretching the PM's.

> **[SOURCE EXTRACTION]** *Paleologo_Advanced_Portfolio_Management p.149:* "The power of diversification is great. It is not a skill: it is a skill multiplier." … "Beyond a certain threshold, coverage and breadth increase at the expense of accuracy."
>
> **Annotation.** Equation (28.25) is the second sentence, made precise. Its credit corollary is the hiring rule: an analyst is worth adding when her names are ones the book does not cover and her hit rate on them, measured with the standard error of (28.6), is at least the PM's. Paleologo also warns (p.131) that a platform run "as a fund of funds" pays "the opportunity cost of not adopting more advanced techniques": pods that never share signals cannot combine them through (28.24).

### Case Study: Aligned Signals, and the Hybrid Shop

Barclays' QPS and credit research teams, as reported by Impax (19 September 2025), measured the effect directly in US investment grade. The issuer-level hit rate was about 58% overall, about 66% when analyst and quant signals agreed, and about 52% when they conflicted. Concentrating on aligned decisions lifted excess return from 2.0% to 3.7% a year and the IR from 1.09 to 1.71, and doubling exposure to aligned signals gave 4.1% with an IR of 1.83. The industry has priced the same conclusion: in late October 2025, Ares agreed to buy BlueCove, a systematic fixed-income manager with about \$5.5bn of AUM and about 60 staff, and to rebrand it Ares Systematic Credit (Alternative Credit Investor, 30 October 2025; see Chapter 4). The design rule that follows is a division of labour. Analysts own $L$, $L_{\max}$ and the document features (PRS, Chapter 13); PhDs own $\lambda^{\mathbb{P}}$, $\sigma_{\text{DTS}}$ and the covariance; and every analyst view is logged in the Edge Ledger (Chapter 3) with timestamp, horizon and confidence, so that its IC, its $\rho$ and its hit rate are measured rather than remembered. The ROBO spec is the contract between the two cultures: if a view cannot be written as a field with units, it is not yet a view.

```python
# --- Block 7: the team production function --------------------------------------
def combined_ic(ics, corr):
    """Eq. (28.24): sqrt(ic' C^{-1} ic)."""
    ics = np.asarray(ics, dtype=float)
    return float(np.sqrt(ics @ np.linalg.solve(np.asarray(corr, dtype=float), ics)))


def optimal_coverage(n_c, e0=0.01, n_grid=None):
    """Eq. (28.25) by brute force: argmax of e(N) sqrt(N) with e(N) = e0 n_c / (N + n_c)."""
    n = np.arange(1, 20 * n_c + 1) if n_grid is None else n_grid
    ir = 2.0 * e0 * n_c / (n + n_c) * np.sqrt(TRADING_DAYS * n)
    return int(n[np.argmax(ir)])


for rho, target in ((0.6, 0.0559), (0.0, 0.0707), (-0.2, 0.0791)):
    two = np.sqrt((0.05 ** 2 * 2 - 2 * rho * 0.05 ** 2) / (1 - rho ** 2))
    assert abs(combined_ic([0.05, 0.05], [[1, rho], [rho, 1]]) - two) < 1e-12
    assert abs(two - target) < 1e-4
assert optimal_coverage(35) == 35
```

## 28.9 The PM Dashboard: The 13-Week Model, Reborn

Theo's USB stick finally earns its keep. The PM dashboard asks the question the 13-week model always asked (do we make it to the other side of the quarter?) about the desk instead of the borrower, and answers it with every formula in this chapter on one screen. Mags reads it top to bottom and asks who adjusted it. Theo points to the equation number next to each line.

| Panel | Metric | Formula | Alarm *(illustrative thresholds)* |
| :--- | :--- | :--- | :--- |
| Leverage | $G$ against floor, ceiling and speed limit | (28.2), (28.22), (28.23) | $G$ above the ceiling, or band empty |
| Breadth | $N_{\text{eff}}$, $1/H$ on issuers, ES share of top decile | (28.4), Procedure 8.1 | $N_{\text{eff}} < 25$ |
| Horizon | Net alpha by signal and tier | (28.7) | Any signal traded with negative net alpha |
| Sizing | Capped half-Kelly vs actual, by issuer and cluster | (28.11)–(28.14) | Actual above cap; cluster $\sum fL \ge 1$ |
| Liquidity | Stressed COL, days-to-liquidate, FRTB-style ES | (28.16)–(28.18) | More than 20% of gross beyond 20 days |
| Drawdown | Realized loss plus $\Delta^{\text{mark}}$ against $x/2$ and $x$ | (28.21) | Budget used above 80% of $x/2$ |
| Runway | Weeks of cash against margin and redemption burn | Block 4 | Under 13 weeks |
| Team | Hit rate and SE by signal and analyst | (28.6) | Hit rate within one SE of 50% after a year |

### Specification for AI Implementation: `pm_playbook_engine`

**Input schema (one row per bond; internal identifiers only, never a CUSIP the spec did not supply).**

| Column | Type | Units | Notes |
| :--- | :--- | :--- | :--- |
| `bond_id`, `issuer_id`, `sector` | str / int | — | Net to `issuer_id` before breadth and Kelly |
| `tier` | int | 0, 1, 2 | §28.3 ladder |
| `mv_usd` | float64 | USD | Signed; marked at bid (long) or offer (short) |
| `spr_dur`, `spread` | float64 | years, decimal | $D^{\text{spr}}$ and OAS ($s$) |
| `sigma_rel` | float64 | decimal / yr | Relative spread volatility |
| `lcs`, `adv_usd` | float64 | decimal, USD/day | Calm round-trip LCS; trailing ADV |
| `lam_p`, `lgd_mean`, `lgd_max` | float64 | 1/yr, decimal | $\lambda^{\mathbb{P}}$ (never $\mathbb{Q}$); $L$ and its document-implied worst case |

Desk parameters (NAV, $\text{DD}_{\max}$, $\kappa z_p$, SR, $r_{\min}$, $m$, the two stop levels, realized drawdown, cash, liquid sleeve, weekly burn, participation, $\rho_w$, $\rho_a$, the Kelly edge s.e.) are a dictionary with units in the key names. The engine is pure: no I/O, no clock, seeded.

```python
# --- Final block: pm_playbook_engine --------------------------------------------
def make_demo_book(rng, n_issuers=60, bonds_per=5, nav=4e8):
    iss = np.repeat(np.arange(n_issuers), bonds_per)
    n = iss.size
    tier = np.where(iss < 48, 1, 2)
    side = np.where(rng.random(n_issuers) < 0.8, 1.0, -1.0)[iss]        # same sign within issuer
    spread = np.where(tier == 1, rng.uniform(0.008, 0.045, n), rng.uniform(0.06, 0.14, n))
    return pd.DataFrame({
        "bond_id": [f"B{i:04d}" for i in range(n)], "issuer_id": iss, "sector": iss % 11,
        "tier": tier, "mv_usd": side * rng.uniform(4e6, 10e6, n),
        "spr_dur": rng.uniform(2.0, 6.0, n), "spread": spread, "sigma_rel": rng.uniform(0.25, 0.45, n),
        "lcs": np.where(tier == 1, 0.006, 0.025), "adv_usd": rng.uniform(2e6, 2e7, n),
        "lam_p": np.where(tier == 1, 0.5, 0.8) * spread / 0.6,              # P-hazard below Q (illustrative)
        "lgd_mean": np.where(tier == 1, 0.6, 0.7), "lgd_max": np.where(tier == 1, 0.8, 1.0),
    })


def pm_playbook_engine(book, desk):
    gross = float(book.mv_usd.abs().sum())
    g = gross / desk["nav_usd"]
    sig = (book.spr_dur * book.spread * book.sigma_rel).to_numpy()
    cov = issuer_block_cov(book.issuer_id.to_numpy(), sig, desk["rho_within"], desk["rho_across"])
    w = book.mv_usd.to_numpy() / gross
    n_eff = effective_breadth(w, cov)
    by_iss = book.groupby("issuer_id").mv_usd.sum()
    sigma_book = float(np.sqrt(w @ cov @ w) * np.sqrt(n_eff))           # per-bet vol consistent with N_eff
    lcs_bar = float(np.average(book.lcs, weights=book.mv_usd.abs()))
    c1 = 0.5 * (desk["mult"] - 1.0) * lcs_bar
    floor = leverage_floor(n_eff, sigma_book, desk["r_min"], desk["sharpe"])
    ceil = leverage_ceiling(n_eff, sigma_book, desk["dd_max"], desk["sharpe"], desk["kappa_z"],
                            col_fn=lambda x: c1 * x)
    iss = book.groupby("issuer_id").agg(carry=("spread", "mean"), lam=("lam_p", "mean"),
                                        lgd=("lgd_mean", "mean"), lgd_max=("lgd_max", "max"))
    theta = kelly_multiplier(desk["edge_rel_se"])
    kelly = np.array([theta * kelly_jump(r.carry, r.lam, r.lgd) for r in iss.itertuples()])
    kelly_cap = np.minimum(kelly, (1.0 - 1e-9) / iss.lgd_max.to_numpy())
    actual = by_iss.reindex(iss.index).abs().to_numpy() / desk["nav_usd"]
    dtl = days_to_liquidate(book.mv_usd.to_numpy(), book.adv_usd.to_numpy(), desk["participation"])
    col = credit_col(book.mv_usd, book.lcs, book.adv_usd, mult=desk["mult"], eta=desk["eta"]).sum()
    used = desk["realized_dd"] + mark_to_bid_shock(g, lcs_bar, desk["mult"])
    return pd.Series({
        "gross_leverage": g, "lev_floor": floor, "lev_ceiling": ceil,
        "lev_speed_limit": liquidity_speed_limit(desk["dd_max"], lcs_bar, desk["mult"]),
        "band_empty": floor > ceil, "lev_breach": g > ceil,
        "n_eff": n_eff, "issuer_herfindahl_n": herfindahl_breadth(by_iss.to_numpy()),
        "names_over_kelly_cap": int(np.sum(actual > kelly_cap)),
        "stressed_col_pct_nav": col / desk["nav_usd"],
        "pct_gross_over_20d": float(book.mv_usd.abs()[dtl > 20].sum() / gross),
        "dd_budget_used_pct_of_cut": used / desk["stop_half"],
        "runway_weeks": runway_weeks(desk["cash_usd"], desk["liquid_sleeve_usd"],
                                     desk["weekly_burn_usd"], haircut=0.1),
        "hit_rate_se_1y": hit_rate_se(0.51, n_eff),
    })


DESK = {"nav_usd": 4e8, "dd_max": 0.075, "kappa_z": 4.0, "sharpe": 2.0, "r_min": 0.05, "mult": 5.8,
        "eta": 0.5, "stop_half": 0.05, "realized_dd": 0.01, "cash_usd": 6e7, "liquid_sleeve_usd": 1.5e8,
        "weekly_burn_usd": 8e6, "participation": 0.10, "rho_within": 0.9, "rho_across": 0.01,
        "edge_rel_se": 1.0}
dash = pm_playbook_engine(make_demo_book(np.random.default_rng(28)), DESK)

assert 1.0 < dash.n_eff < dash.issuer_herfindahl_n <= 60.0 + 1e-9    # correlation shrinks breadth
assert dash.lev_ceiling < dash.lev_speed_limit
assert dash.lev_breach == (dash.gross_leverage > dash.lev_ceiling)
assert 0.0 <= dash.pct_gross_over_20d <= 1.0 and dash.stressed_col_pct_nav > 0.0
assert dash.runway_weeks > 13.0                                      # the desk survives the quarter
assert dash.dd_budget_used_pct_of_cut > DESK["realized_dd"] / DESK["stop_half"]   # marks count
print(dash.to_string())
```

The one non-obvious line is `sigma_book`. Equation (28.22) is written for $N_{\text{eff}}$ equal, independent bets of volatility $\sigma_{\text{DTS}}$, so the engine backs out the per-bet volatility that, with the measured $N_{\text{eff}}$, reproduces the book's actual volatility per dollar of GMV: $\sigma_{\text{DTS}} = \sigma_{\text{GMV}}\sqrt{N_{\text{eff}}}$. Feeding the average bond volatility instead would double-count the diversification that $N_{\text{eff}}$ already removed.


