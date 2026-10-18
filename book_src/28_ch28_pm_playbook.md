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
