# Chapter 1: The Anthology of the Desk & The Modern Quant Credit Landscape

**2:58 p.m., a Friday, Theo Marsh's third week.**

The RFQ arrives the way bad news always arrives on a credit desk: politely, in a grey box, with a countdown. *Client sells \$15mm, Halvorsen Building Products 7.25% senior unsecured notes due 2029, B3/B-, all-to-all, five dealers in competition. Respond in 00:14.* (Halvorsen is fictional. The lender call that ended at 2:00 p.m. today is, sadly, a genre.)

Theo's hand goes to his pocket, where the USB stick with his old 13-week cash flow model lives "for emotional support." With the other hand he opens the credit agreement: 350 pages, 2019 vintage, a definition of "Consolidated EBITDA" that runs to four pages and has never once been in a hurry.

"Engine has us at 91.40," says Kaz, without looking up. "Residual vol is normal. Inventory is flat. Let's just assume Gaussian."

"The engine wasn't on the call," says Mags.

Ines rolls her chair over. "What's the pot, what are the odds, and who at this table knows more than you?"

"But what does the credit agreement say?" Theo asks.

"Nothing it didn't say at 1:59," Ines says. "The question is what got said at 2:00, and whether the person hitting our bid was on the line when it got said."

The timer reads 00:11. Theo's 13-week model has thirteen columns. The RFQ has eleven seconds. Ines taps the screen. "One of those is going to be reborn as something useful. Guess which."

Theo does not answer, and in credit, not answering is also a price. The desk passes, another dealer prints the bonds at 91.25, and at 4:40 p.m. an 8-K announces a "comprehensive liability management transaction supported by an ad hoc group of lenders." The bonds open Monday at 78.

That is the whole chapter in one RFQ. Someone was selling. They were selling *now*. And the only question that mattered was not "is Halvorsen a good credit?" but **who is selling, why now, and what is that worth?**

By the end of this chapter you will be able to: (1) derive the market maker's bid from first principles and say which part of this book builds each of its three terms; (2) read the shelf (Ben Dor, Bohn–Stein, Schmid, Bolder, Veronesi, Dynkin, Paleologo, Moyer, Houlihan Lokey, and the five industry papers) as one argument about forced flows rather than fourteen unrelated textbooks; (3) draw the credit ecosystem as a **forced-seller flow graph**, with holders, triggers, response windows, and absorption capacity; (4) quote dated, sourced numbers on how that graph changed between 2018 and 2026; and (5) hand ROBO a specification precise enough that it builds the graph instead of a one-node diagram labeled "Everyone, March 2020."

## 1.1 The Epistemological Clash: PJT RSSG vs. The Automated Market Maker

Walk onto the restructuring floor at PJT Partners (RSSG) in Midtown Manhattan, and the unit of account is the **bespoke legal bottleneck**. An analyst spends 90 hours modeling a 13-week cash flow forecast, reading a 350-page Senior Secured Credit Agreement from 2019, calculating exact dollar capacity inside the *Available Amount* builder basket under Section 7.06, and determining whether an ad-hoc group holding $50.1\%$ of the Term Loan B can strip collateral coverage via an amendment and drop intellectual property into an unrestricted subsidiary. Time moves in weeks; alpha is extracted by structuring a private non-pro-rata transaction where your client captures a $20\text{-point}$ priming premium over left-behind minority lenders *(illustrative)*.

Now walk onto the quantitative credit and cross-asset market-making floor at Susquehanna International Group (SIG) in Bala Cynwyd, or a systematic credit pod at Citadel or DE Shaw. The unit of account is **conditional expected value per unit of inventory variance per day**. Nobody is reading a single indenture cover-to-cover during market hours. Instead, an automated pricing engine ingests real-time FINRA TRACE prints, CME Treasury futures ticks, OPRA single-stock option implied volatility surfaces, and HYG/LQD ETF creation-redemption baskets. When a client sends an all-to-all Request for Quote (RFQ) on MarketAxess asking for a bid on $\$15\text{ million}$ notional of a stressed $B3/B-$ high-yield bond, the desk has **a few seconds** to solve an adverse selection problem:

$$
\text{Quote Bid } B^* = \mathbb{E}[V_{t+\Delta t} \mid \mathcal{F}_t, \text{Order Flow } \mathcal{O}_t] - \frac{1}{2}\gamma \sigma^2_{\text{IDO}} (2q + \Delta q) - \Lambda_{\text{tox}}(\mathcal{O}_t)
$$

Where:

- $\mathbb{E}[V_{t+\Delta t} \mid \mathcal{F}_t, \mathcal{O}_t]$ is the posterior fair value of the bond (here $V$ is the bond's value, not the firm's assets; §1.3 renames it $m$ to keep the notation table honest) conditioned on public filtration $\mathcal{F}_t$ and the event that a counterparty is actively trying to sell size $\Delta q$.
- $\gamma$ is the desk's risk-aversion parameter, $\sigma^2_{\text{IDO}}$ is the unhedged idiosyncratic variance of the bond over the holding horizon after stripping Treasury duration and CDX beta, and $q$ is current desk inventory.
- $\Lambda_{\text{tox}}(\mathcal{O}_t)$ is the **Adverse Selection Penalty**: the probability that the seller has just left a lender call or analyzed a covenant trapdoor and knows an LMT or earnings miss is imminent, times the size of the move they know about.

Read the equation as three bets stacked on top of each other, because that is how the rest of this book is organized:

| Term | What it asks | Who on the desk owns it | Where the book builds it |
| :--- | :--- | :--- | :--- |
| Fair value $\mathbb{E}[\cdot]$ | What is this bond worth to a neutral holder? | Kaz (models), Mags (recoveries) | Part II (distributions, Merton, intensities), Part VI (vol surfaces, CDS basis) |
| Inventory skew $\tfrac12\gamma\sigma^2_{\text{IDO}}(2q+\Delta q)$ | What does it cost me to *hold* it until someone else wants it? | Ines (risk), the PM | Part III (stripping beta to get $\sigma_{\text{IDO}}$), Part V (microstructure), Part VIII (sizing) |
| Toxicity $\Lambda_{\text{tox}}$ | Does the seller know something I don't? | Theo, and everything he knows about credit agreements | Ch 3 (RFQ adverse selection), Part IV (LMTs), Part VII (NLP on dockets and documents) |

In the cold open, Kaz's engine got the first two terms right and set the third to zero. That is not a modeling error you can fix with more data. It is a modeling error you fix by knowing what a lender call is.

### Why the Hybrid PJT RSSG + Quant Architect Owns the Future

Pure quantitative researchers trained in equity stat-arb fail in distressed and high-yield credit because they treat CUSIPs as exchangeable time series. When a company executes a Serta-style uptier or a J.Crew trapdoor drop-down, historical price correlations break down instantaneously—a structural discontinuity occurs that a standard Kalman filter or GARCH model cannot anticipate.

Conversely, traditional fundamental restructuring analysts fail on a systematic desk because they treat every credit as an artisanal snowflake, refusing to codify their intuition into continuous probability distributions. **The ultimate alpha in modern credit belongs to the architect who can translate PJT RSSG legal and structural mechanics into state-space features that feed an automated pricing and risk engine.**

The industry says so itself, in writing, on our shelf. Man Group's 2022 survey of the field ends its tour of quant credit with a confession:

> **[SOURCE EXTRACTION]** *Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.42:* "Quant credit is yet to move into distressed debt – this is a high-touch asset class that requires a significant degree of human intervention, but further data capture and analysis around restructurings and recovery may make this possible."
>
> **Annotation.** Read that sentence as a job description. "Human intervention" is the reader: someone who knows which basket in the negative covenants is the trapdoor and which "sacred right" is load-bearing. "Further data capture and analysis around restructurings and recovery" is Parts IV and VII of this book: the Priming Risk Score (Ch 13), regime-switching default and recovery distributions (Ch 14), and parsers that turn credit agreements and dockets into features (Ch 25). The 2022 boundary Man describes is not a law of nature. It is a backlog. Notice also *where* the boundary sits: precisely where the third term of the bid equation, toxicity, dominates the other two. In IG, the fair-value and inventory terms do most of the work and quants have been competitive for a decade. In distressed, $\Lambda_{\text{tox}}$ is most of the bid, and nobody has yet built a machine that reads a cooperation agreement. The modern desk departs from Man's 2022 framing in one respect: it does not wait for the data to be "captured" by someone else. It hires the person who already knows where the data is buried.

---

## 1.2 Evaluating the Market Set in Quantitative Credit

To extract maximum alpha and isolate pure Idiosyncratic Return (**IDO**), a Desk Head or Portfolio Manager must first map the structural players in the ecosystem and understand their mechanical constraints. The last column is the one that matters most for this chapter: it says what each player is *contractually or regulatorily forced* to do, and on what clock.

| Strategy / Desk Archetype | Representative Firms | Holding Horizon | Primary Edge | Structural Vulnerability (How You Arb Them) | Forced to Do What, and When |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Automated OTC Market Makers & PT Desks** | SIG, Jane Street, Citadel Securities, Flow Traders | Milliseconds to 10 Days | ETF Creation/Redemption loops, Portfolio Trading (PT) pricing speed, cross-asset latency | Exposed to **toxic fundamental flow** on bespoke LMTs, covenant priming, and bankruptcy docket surprises | Flatten inventory against risk and balance-sheet limits; widen or pull quotes when toxicity spikes. Clock: intraday to days. |
| **Systematic Factor Credit Pods** | AQR, Man Numeric, BlackRock Systematic, Two Sigma | 1 to 6 Months | Cross-sectional factor harvesting (Value, Equity-to-Credit Momentum, Carry, Quality) across 2,000+ issuers | Slow to react to discrete structural breaks (M&A CoC waivers, drop-down rumors); mechanical rebalancing creates predictable flow | Rebalance on schedule and de-gross on drawdown or gross-leverage limits. Clock: the rebalance date, which other people can also read. |
| **Capital Structure & Volatility Arbitrage** | DE Shaw, Saba Capital, Elliott (Trading), Millennium pods | 5 Days to 6 Months | Merton-model dislocations, Equity Put Skew vs. High-Yield Spreads, CDS-to-Bond Basis, Orphan CDS | Vulnerable to squeeze dynamics in repo/borrow markets and basis blowouts during liquidity crunches | Unwind when borrow is recalled, margin rises, or the basis breaches a stop. Clock: days, and always at the worst time. |
| **CLO Vehicles (Par-Constrained Institutional Buyers)** | Blackstone, Carlyle, Palmer Square, Ares | Buy-and-Hold (Reinvestment Period) | Structural leverage via AAA-to-Equity tranche arbitrage | **Forced mechanical sellers** when CCC buckets exceed $7.5\%$ or upon default; cannot easily fund new-money post-reorg equity rights offerings | Carry CCC excess at market value in OC tests; divert cash to senior notes on breach; sell or stop reinvesting to cure. Clock: the next test or payment date. |
| **Insurers & Annuity Writers (Ratings- and Capital-Constrained)** | MetLife, Prudential, Athene, Corebridge | Hold to maturity (liability-matched, 5 to 30 years) | Liability-matched spread capture; illiquidity premium from private placements | Capital charges jump at the IG/HY line, so downgrades produce slow, concentrated selling of the same bonds by many holders | Sell, or hold more capital, after a downgrade to speculative grade. Clock: quarters, not days. |
| **Open-End HY Funds & Bond ETFs (NAV-Redemption Sellers)** | iShares (HYG, LQD), SPDR (JNK), Vanguard and other HY mutual fund complexes | Daily liquidity to end-investors | Cheap beta delivery; daily liquidity on illiquid assets | Liquidity mismatch: they sell what is liquid, not what is expensive; ETF prices gap below NAV when authorized participants stop arbitraging | Index funds sell fallen angels at the month-end rebalance and buy them at HY index inclusion; open-end funds meet redemptions within days. Clock: a known calendar date, or the day after a bad headline. |

Everyone in that table is smart. Most of them are not the problem. The problem is the last column: every row has a trigger that converts a rating, a test, or a redemption into a sale, at a time you can often predict and in a size you can often estimate. A forced sale is **information-free about the bond and information-rich about the seller**. The rest of this chapter is about telling those two kinds of information apart, at speed, for money.

> **[AGENT EXPANSION DIRECTIVE FOR NEXT ITERATION]:** Pull cited excerpts from `/state/pdf_pages/Ben_Dor_Quantitative_Credit_Portfolio_Management/` on DTS (Duration Times Spread) and empirical duration, `/state/pdf_pages/Bohn_Stein_Active_Credit_Portfolio_Management/` on structural default models, and `/state/pdf_pages/Moyer_Distressed_Debt_Analysis/` on the distressed investing process. Expand Section 1.3 into a 6,000-word compilation of foundational texts with full mathematical commentary.

---

## 1.3 The Bid Equation, Derived

The seed equation in §1.1 looks like something a vendor would put on a slide. It is better than that: it is the reservation price of a risk-averse dealer, plus one application of Bayes' rule, plus a cost. Derive it once and every later chapter becomes a commentary on one of its terms.

### 1.3.1 Setup and units (measure: $\mathbb{P}$, the desk's own beliefs)

Everything in this section is a physical-measure object. The mid $S_t$ may come out of a risk-neutral ($\mathbb{Q}$) model, but the question "will I lose money on this trade over the next week?" is a $\mathbb{P}$ question, and the markout that answers it is measured in $\mathbb{P}$.

- $S_t$: the desk's mid for the bond, in **price points per 100 of par**.
- $q$: current inventory in **\$mm of par** (long positive). $\Delta q > 0$: the size the client wants to sell to us.
- $h$: the expected holding horizon in **years** (five trading days is $h = 5/252$).
- $\sigma_{\text{IDO}}$: the standard deviation of the bond's price change *after* the hedges (Treasury futures for rates, CDX or an ETF for spread beta), in **points per $\sqrt{\text{year}}$**. Chapter 8 is entirely about getting this number right.
- P&L is measured in **\$mm·points**: one point on \$1mm of par is one unit, which is \$10,000. The risk aversion $\gamma$ is then in units of $1/(\$\text{mm}\cdot\text{pt})$.

Assume the desk evaluates a position with a mean–variance certainty equivalent, $\text{CE}(X) = \mathbb{E}^{\mathbb{P}}[X] - \tfrac12\gamma\,\mathrm{Var}^{\mathbb{P}}(X)$. This is exact for exponential (CARA) utility with Gaussian P&L, and it is the standard first-order approximation otherwise (the "otherwise" is the Ways This Blows Up box below). Let $m = \mathbb{E}^{\mathbb{P}}[S_{t+h}\mid\mathcal{F}_t, \mathcal{O}_t]$ be the fair value **conditional on the fact that this RFQ arrived**. That conditioning is the whole game, and we will come back to it.

### 1.3.2 The inventory term

The desk is indifferent between not trading and buying $\Delta q$ at price $B$ when the certainty equivalents match. Holding $q + \Delta q$ until $t+h$ is worth $(q+\Delta q)\,m$ in expectation, costs $B\,\Delta q$ in cash today, and carries variance $(q+\Delta q)^2\sigma^2_{\text{IDO}}h$:

$$
(q+\Delta q)\,m \;-\; B\,\Delta q \;-\; \tfrac12\gamma\,\sigma^2_{\text{IDO}}h\,(q+\Delta q)^2 \;=\; q\,m \;-\; \tfrac12\gamma\,\sigma^2_{\text{IDO}}h\,q^2 .
$$

Cancel $q\,m$ from both sides and expand $(q+\Delta q)^2 - q^2 = \Delta q\,(2q+\Delta q)$:

$$
\Delta q\,(m - B) \;=\; \tfrac12\gamma\,\sigma^2_{\text{IDO}}h\,\Delta q\,(2q+\Delta q).
$$

Divide by $\Delta q > 0$:

$$
B^{\text{res}} \;=\; m \;-\; \tfrac12\,\gamma\,\sigma^2_{\text{IDO}}\,h\,(2q+\Delta q). \tag{1.1}
$$

Three things fall out immediately. First, the bid falls one-for-one in $q$: a desk that is already long is a worse buyer, by $\gamma\sigma^2_{\text{IDO}}h$ per \$mm of existing inventory. Second, the bid falls in the client's size, by $\tfrac12\gamma\sigma^2_{\text{IDO}}h$ per \$mm; this is the "block discount," and it is the term most often dropped by people who linearize too early. Third, letting $\Delta q \to 0$ gives the reservation mid $r^{\text{res}} = m - \gamma\sigma^2_{\text{IDO}}h\,q$, which is the Avellaneda–Stoikov reservation price with the trading horizon $T-t$ replaced by the expected holding period $h$. (The notation table reserves $r$ for interest rates, so the reservation price wears a superscript.) The same algebra for a client *buying* $\Delta q$ from us gives the ask $A^{\text{res}} = m' + \tfrac12\gamma\sigma^2_{\text{IDO}}h\,(\Delta q - 2q)$, where $m'$ conditions on a buy RFQ: a long desk is a keen seller.

### 1.3.3 The toxicity term: Bayes on the RFQ

Now the conditioning. Suppose RFQ senders come in two types. An **uninformed** seller (a fund meeting redemptions, an insurer selling a downgraded bond, a CLO curing a test) carries no news: $\mathbb{E}^{\mathbb{P}}[S_{t+h}\mid\text{uninformed}] = S_t$, where $S_t$ already prices everything public. An **informed** seller knows the price is going to $S_t - J$, for a jump $J > 0$ points (the post-LMT mark, the earnings miss, the docket filing). Let $\pi = \mathbb{P}(\text{informed}\mid\text{this RFQ},\mathbf{x})$ be the posterior that this particular seller is informed, given observable features $\mathbf{x}$. Then

$$
m \;=\; \pi\,(S_t - J) + (1-\pi)\,S_t \;=\; S_t - \pi J .
$$

Where does $\pi$ come from? From Bayes' rule, and this is the step that turns an RSSG banker's instincts into a model. Let $\mu$ be the prior share of informed senders, and let $a_I(\mathbf{x})$ and $a_U(\mathbf{x})$ be the likelihoods that an informed or uninformed account would send *this* RFQ: this size, this bond, at 2:58 p.m., 58 minutes after a lender call, five dealers in competition. Then

$$
\pi(\mathbf{x}) \;=\; \frac{\mu\,a_I(\mathbf{x})}{\mu\,a_I(\mathbf{x}) + (1-\mu)\,a_U(\mathbf{x})}
\quad\Longleftrightarrow\quad
\operatorname{logit}\pi(\mathbf{x}) \;=\; \operatorname{logit}\mu \;+\; \ln\frac{a_I(\mathbf{x})}{a_U(\mathbf{x})} .
$$

If the log-likelihood ratio is (approximately) additive across features, $\ln(a_I/a_U) = \theta^\top\mathbf{x}$, the posterior is exactly a logistic regression, $\pi(\mathbf{x}) = (1+e^{-\theta_0-\theta^\top\mathbf{x}})^{-1}$ with $\theta_0 = \operatorname{logit}\mu$. That is why every RFQ toxicity model on the Street is, under the hood, a logistic regression or a tree ensemble pretending not to be one. The features worth paying for are the ones with large likelihood ratios: minutes since a lender call or an amendment request, days to earnings, whether the account sits in a known ad hoc group (Rule 2019 statements, Ch 25), the account's own past markouts, size relative to the issue, and how many dealers were put in competition. A seller who shows the bond to one dealer at a time and a seller who blasts it to twenty are telling you different things.

Adding a cost $c(\Delta q)$ for the hedge half-spread and expected liquidation cost (Ben Dor's liquidity cost score is one estimate, §1.4) gives the full bid:

$$
B^* \;=\; S_t \;-\; \underbrace{\pi(\mathbf{x})\,J}_{\Lambda_{\text{tox}}} \;-\; \underbrace{\tfrac12\gamma\,\sigma^2_{\text{IDO}}\,h\,(2q+\Delta q)}_{\text{inventory}} \;-\; \underbrace{c(\Delta q)}_{\text{cost}} . \tag{1.2}
$$

This is the seed's equation from §1.1 with the per-horizon variance written out. Its comparative statics are the unit tests: $\partial B^*/\partial\pi = -J < 0$; $\partial B^*/\partial q = -\gamma\sigma^2_{\text{IDO}}h < 0$; $\partial B^*/\partial\Delta q = -\tfrac12\gamma\sigma^2_{\text{IDO}}h - c'(\Delta q) < 0$; and with $\gamma = 0$ and $\pi = 0$, $B^* = S_t - c$.

**The cold open, in numbers** *(illustrative)*. Take $S_t = 91.97$, $q = +5$, $\Delta q = 15$, $\sigma_{\text{IDO}} = 8$ points per $\sqrt{\text{yr}}$, $h = 5/252$, $\gamma = 0.02$, $c = 0.25$. Then $\sigma^2_{\text{IDO}}h = 1.270$ pt², the inventory term is $0.01 \times 1.270 \times 25 = 0.317$ points, and with $\pi = 0$ the bid is $91.97 - 0.317 - 0.25 = 91.40$. That is Kaz's engine. Now let Theo's features in: the account was in the lender group (large likelihood ratio), the call ended 58 minutes ago (large), and the bond went to five dealers at once (moderate). Suppose those push $\pi$ to $0.6$, and the plausible jump is $J = 13$ points. The toxicity term is $7.8$ points and $B^* = 83.60$. A desk that can only show 91.40 or nothing should show nothing. Passing was the right trade; Theo just did not know why yet.

> **Poker Table.** "An RFQ from a lender who was on the 2 p.m. call is a raise from a player who just looked at the river card," Ines says. "You don't need to know what he saw. You need to know he saw it." The lesson is in the Bayes step: $\pi$ is a function of observable *counterparty state*, not of the bond. Two identical RFQs on the same CUSIP can deserve bids ten points apart because of who sent them and when. Ines's hand history, replayed through markouts, is the test: if you had bought at 91.40, your five-day markout would have been $78 - 91.40 = -13.4$ points on \$15mm, or about \$2.0mm. Across a thousand such hands the average markout on each feature bucket *is* $-\pi J$, and that is how you estimate $\pi$ without ever reading anyone's mind.

> **Ways This Blows Up.** *Kaz: "Let's just assume Gaussian."* The mean–variance certainty equivalent treats a 50-point jump to default as if it were a lot of small wiggles. Do the exact CARA calculation instead. Let the hedged price change be $\sigma_{\text{IDO}}\sqrt{h}\,Z - \ell\,(N_h - \lambda h)$, where $N_h$ is a Poisson count with default intensity $\lambda$ and $\ell = P - 100R$ is the jump-to-default in points (the compensator $\lambda h$ keeps the mean in $m$). For a position $q$, the exact certainty equivalent is
>
> $$
> \text{CE} = \mathbb{E}^{\mathbb{P}}[X] - \tfrac12\gamma q^2\sigma^2_{\text{IDO}}h - \frac{\lambda h}{\gamma}\Big(e^{\gamma q \ell} - 1 - \gamma q \ell\Big),
> $$
>
> whose last term equals the Gaussian-style $\tfrac12\gamma\lambda h q^2\ell^2$ only when $\gamma q\ell \ll 1$. At $\gamma q\ell = 0.6$ the Gaussian version under-charges the jump by about 19%; at $\gamma q\ell = 3$ it under-charges by a factor of about 3.6, and the gap grows exponentially in size. Large blocks in jumpy names are exactly where this matters, which is why real desks cap jump-to-default exposure with hard limits rather than trusting a quadratic penalty. Kaz: "...I regret it already." Chapter 18 rebuilds the market maker's problem with a jump term, and Chapter 28 turns the limit into a sizing rule.

### Specification for AI Implementation

**What ROBO built from the vague version.** Spec: "write a function that gives a fair bid for an RFQ." ROBO returned `return mid`, with a docstring noting that the mid is, by construction, fair. It is. It is also the price at which the cold open loses \$2mm.

**The Spec You Hand the Robot.** Implement equation (1.2) as `reservation_bid(S, q, dq, gamma, sigma_ido, h_years, pi, J, c)`. Units are part of the contract: `S`, `J`, `c` in price points per 100 par; `sigma_ido` in points per $\sqrt{\text{year}}$, *post-hedge*; `q`, `dq` in \$mm par, long positive, `dq > 0` meaning the client sells to us; `gamma` in $1/(\$\text{mm}\cdot\text{pt})$; `h_years` in years. Raise `ValueError` on `dq <= 0`, `pi` outside $[0,1]$, `h_years <= 0`, or negative `gamma`, `sigma_ido`, `J`, `c`. Do **not** condition twice: if `S` already comes from a model that conditions on the RFQ, pass `pi = 0`. Implement `posterior_informed(mu, log_lr)` as the logit-additive Bayes update. Implement `glosten_milgrom_markout(pi, J, sigma_ido, h_years, n, seed)` as a seeded simulation of seller types whose mean markout must equal $-\pi J$ within three standard errors. Implement `jump_penalty_ratio(gamma, q, ell)`, the exact CARA jump penalty divided by its quadratic approximation, and assert that it tends to 1 as $\gamma q\ell \to 0$ and increases in $q$. Edge cases: a short desk ($q < 0$) may bid above $S - c$, which is correct and must not be clipped; `pi = 1` is legal and means "the bid is $S - J$ minus costs."

```python
import numpy as np
import pandas as pd

RNG_SEED = 20261017


def reservation_bid(S, q, dq, gamma, sigma_ido, h_years, pi, J, c=0.0):
    """Dealer bid for buying dq ($mm par) from a client: eq. (1.2), measure P.

    S, J, c, sigma_ido in price points per 100 par (sigma_ido per sqrt(year), post-hedge);
    q, dq in $mm par (long positive; dq > 0 means the client sells to us);
    gamma in 1/($mm * pt) of P&L; h_years in years.
    """
    if dq <= 0:
        raise ValueError("dq must be > 0: the client sells dq to the desk")
    if not 0.0 <= pi <= 1.0:
        raise ValueError("pi must lie in [0, 1]")
    if h_years <= 0:
        raise ValueError("h_years must be > 0")
    if min(gamma, sigma_ido, J, c) < 0:
        raise ValueError("gamma, sigma_ido, J and c must be non-negative")
    m = S - pi * J                                   # Glosten-Milgrom posterior mean
    inventory = 0.5 * gamma * sigma_ido**2 * h_years * (2.0 * q + dq)
    return m - inventory - c


def posterior_informed(mu, log_lr):
    """Bayes in logit form: logit(pi) = logit(mu) + log(a_I / a_U)."""
    if not 0.0 < mu < 1.0:
        raise ValueError("prior mu must lie strictly inside (0, 1)")
    z = np.log(mu / (1.0 - mu)) + log_lr
    return 1.0 / (1.0 + np.exp(-z))


def glosten_milgrom_markout(pi, J, sigma_ido=8.0, h_years=5 / 252, n=200_000, seed=7):
    """Simulated markout (points) of buying at mid from a seller who is informed w.p. pi."""
    rng = np.random.default_rng(seed)
    informed = rng.random(n) < pi
    noise = sigma_ido * np.sqrt(h_years) * rng.standard_normal(n)
    markout = -J * informed + noise                  # S_{t+h} - S_t from the buyer's side
    return markout.mean(), markout.std(ddof=1) / np.sqrt(n)


def jump_penalty_ratio(gamma, q, ell):
    """Exact CARA jump penalty / quadratic approximation (common factor lambda*h cancels)."""
    x = gamma * q * ell
    exact = (np.expm1(x) - x) / gamma
    quadratic = 0.5 * gamma * (q * ell) ** 2
    return exact / quadratic


# --- the cold open, in numbers (illustrative) ---
base = dict(S=91.97, q=5.0, dq=15.0, gamma=0.02, sigma_ido=8.0, h_years=5 / 252, c=0.25)
engine_bid = reservation_bid(pi=0.0, J=13.0, **base)
theo_bid = reservation_bid(pi=0.6, J=13.0, **base)
assert abs(engine_bid - 91.40) < 0.01, engine_bid
assert abs(theo_bid - 83.60) < 0.01, theo_bid

# --- comparative statics are the unit tests ---
assert reservation_bid(**{**base, "q": 6.0}, pi=0.1, J=13.0) < reservation_bid(**base, pi=0.1, J=13.0)
assert reservation_bid(**base, pi=0.2, J=13.0) < reservation_bid(**base, pi=0.1, J=13.0)
assert reservation_bid(**{**base, "dq": 20.0}, pi=0.1, J=13.0) < reservation_bid(**base, pi=0.1, J=13.0)
assert reservation_bid(**base, pi=0.1, J=13.0) <= base["S"]          # q >= 0 never bids above mid
zero = reservation_bid(S=91.97, q=0.0, dq=15.0, gamma=0.0, sigma_ido=8.0, h_years=0.02, pi=0.0, J=13.0, c=0.25)
assert abs(zero - (91.97 - 0.25)) < 1e-12
short_desk = reservation_bid(**{**base, "q": -20.0, "c": 0.0}, pi=0.0, J=0.0)
assert short_desk > base["S"]                                        # a short desk pays up to cover

# --- Bayes and the hand history ---
assert abs(posterior_informed(0.05, 0.0) - 0.05) < 1e-12              # uninformative features
assert posterior_informed(0.05, np.log(30.0)) > 0.6                   # 'was on the call' LR of 30
mean_mo, se_mo = glosten_milgrom_markout(pi=0.3, J=13.0)
assert abs(mean_mo - (-0.3 * 13.0)) < 3 * se_mo, (mean_mo, se_mo)

# --- Kaz's Gaussian regret ---
r_small = jump_penalty_ratio(0.02, 0.01, 30.0)
r_mid = jump_penalty_ratio(0.02, 1.0, 30.0)
r_big = jump_penalty_ratio(0.02, 5.0, 30.0)
assert abs(r_small - 1.0) < 1e-2 and 1.0 < r_mid < r_big
print(f"engine bid {engine_bid:.2f} | toxicity-aware bid {theo_bid:.2f} | "
      f"jump under-charge x{r_mid:.2f} at 1mm, x{r_big:.2f} at 5mm")
```

The numerical guards are deliberate. `np.expm1` keeps the jump penalty accurate when $\gamma q\ell$ is tiny (a naive `exp(x) - 1 - x` loses every significant digit below about $10^{-8}$), and `posterior_informed` refuses a prior of exactly 0 or 1, because a desk that is certain nobody is informed has already lost the hand.

### Deep-Dive Resource Graph

- **Podcasts.** Bloomberg *Odd Lots* has run several conversations on how corporate bonds actually trade (search the show's archive for its corporate-bond market-structure and portfolio-trading episodes; we do not cite episode numbers). *Flirting with Models* (Corey Hoffstein), https://www.flirtingwithmodels.com/ , for systematic-investing practitioners talking process.
- **Practitioner Writing.** Man Institute, Robert Lam and Paul Kamenski, *The Revolutions in Credit Trading* (2023), https://www.man.com/insights/revolutions-in-credit-trading , on why execution, not ideas, was the binding constraint. Matt Levine, *Money Stuff* (Bloomberg Opinion), passim on information and dealer inventory.
- **Academic Papers.** Glosten and Milgrom (1985), *Bid, Ask and Transaction Prices in a Specialist Market with Heterogeneously Informed Traders*, Journal of Financial Economics. Ho and Stoll (1981), *Optimal Dealer Pricing under Transactions and Return Uncertainty*, Journal of Financial Economics. Avellaneda and Stoikov (2008), *High-Frequency Trading in a Limit Order Book*, Quantitative Finance. Guéant, Lehalle and Fernandez-Tapia (2013), *Dealing with the Inventory Risk: A Solution to the Market Making Problem*, Mathematics and Financial Economics.
- **Data & Code.** FINRA TRACE, https://www.finra.org/filing-reporting/trace , the post-trade tape every markout is computed against.

---

## 1.4 The Anthology, Part A: Measuring the Risk You Catch (Ben Dor; Veronesi)

Here is how to read the shelf. Every book on it answers one question about the forced seller on the other side of your bid. Ben Dor answers the first: *if I catch this flow, how much risk did I just buy?* The intuitive answer, "spread duration times the spread move," is correct and useless, because it leaves open which spread move. Ben Dor's team at Barclays spent a decade showing that the answer is *a move proportional to the spread you already have*.

> **[SOURCE EXTRACTION]** *Ben_Dor_Quantitative_Credit_Portfolio_Management p.61:* "we demonstrate that spread changes are proportional to the level of spread. Systematic changes in spread across a sector tend to follow a pattern of relative spread change, in which bonds trading at wider spreads experience larger spread changes."
>
> **Annotation.** This is the single most useful empirical regularity in corporate credit, and it is the reason the inventory term of (1.2) cannot use a single $\sigma$ for every bond. The derivation is two lines. A bond's excess return over duration-matched Treasuries is, to first order, $r^{\text{xs}} \approx -D^{\text{spr}}\,\Delta s$. If spread changes are proportional, $\Delta s = s\,\varepsilon$ with $\varepsilon$ a relative change whose volatility $\sigma_{\text{rel}}$ is roughly common across bonds, then
>
> $$
> \sigma(r^{\text{xs}}) \;\approx\; D^{\text{spr}}\,s\,\sigma_{\text{rel}} \;=\; \text{DTS}\cdot\sigma_{\text{rel}}, \qquad \text{DTS}_i = D^{\text{spr}}_i\,s_i . \tag{1.3}
> $$
>
> Units: with $D^{\text{spr}}$ in years and $s$ in bp, DTS is in bp·years and (1.3) gives excess-return volatility in bp per period of $\sigma_{\text{rel}}$. A BBB bond at 120 bp with a seven-year spread duration has DTS 840; a single-B bond at 450 bp with a four-year duration has DTS 1,800 *(illustrative)*. Spread duration says the BBB is the riskier bond (7 versus 4). DTS says the single-B is more than twice as risky, and DTS is right. A portfolio's exposure to a sector-wide relative move is $\sum_i w_i\,\text{DTS}_i$, which is why Ben Dor's issuer limits are written on DTS: a cap of 5 on market-value % × spread (in %) × duration lets a 100 bp, five-year bond be 1% of the portfolio but holds a 150 bp, ten-year bond to 0.33% (same page).

> **[SOURCE EXTRACTION]** *Ben_Dor_Quantitative_Credit_Portfolio_Management p.39:* "absolute spread volatility is highly unstable and tends to rise with increasing spread. Computing volatilities based on relative spread change generates a more stable time series."
>
> **Annotation.** Stability is the property a specifier should care about most, because a parameter that moves is a parameter the model will mis-estimate exactly when it matters. On the same page Ben Dor reports sector relative volatilities "quite tightly clustered, ranging from 5% to a bit over 10%" per month, against absolute volatilities from 5 bp to more than 20 bp per month. For the desk this means one number, $\sigma_{\text{rel}}$, plus each bond's DTS, gives a first-pass $\sigma_{\text{IDO}}$ prior for thousands of CUSIPs that never trade, before any bond-specific data arrives. Chapter 8 replaces the prior with a posterior.

> **[SOURCE EXTRACTION]** *Ben_Dor_Quantitative_Credit_Portfolio_Management p.26:* "We find that the relationship between spread and spread volatility remains strongly linear, albeit with a steeper slope."
>
> **Annotation.** This is the out-of-sample test through 2007–2009, and the "albeit" is where the money is. The *shape* survives a crisis; the *slope*, $\sigma_{\text{rel}}$, does not. A book that is DTS-neutral in calm markets is not crisis-neutral, because $\sigma_{\text{rel}}$ jumps for everyone at once, and it jumps exactly when forced sellers arrive. In the bid equation, that is the moment the inventory term and the cost term explode together (Case Study B, §1.8).

**Empirical duration: the CCC bond that wears a tie.** The rates hedge has the same problem from the other side. Analytical (modified) duration says a five-year bond loses about five points per 100 bp rise in Treasury yields. Empirically, high-yield bonds barely care, and sometimes move the wrong way, because rates tend to rise on good economic news that also tightens spreads. Ben Dor estimates empirical duration by regressing price returns on Treasury yield changes, $\Delta P/P = -D^{\text{emp}}\,\Delta y^{\text{TSY}} + \epsilon$, and finds it falls with spread level: "when Ba spreads topped 600 bps in 2002, the corresponding empirical duration was as low as −2" (*Ben_Dor_Quantitative_Credit_Portfolio_Management p.200*). A CCC bond is an equity option that wears a tie to work: it has a coupon and a maturity date, and it trades on the equity's mood. Hedge it with Treasury futures at its analytical duration and you have not removed rates risk; you have added a short Treasury position. That error goes straight into $\sigma_{\text{IDO}}$ and inflates the inventory charge. Chapter 8 builds the hedge ratios properly.

> **[SOURCE EXTRACTION]** *Ben_Dor_Quantitative_Credit_Portfolio_Management p.112:* "We define LCS as the bond's OASD multiplied by this spread. Consequently, a bond's LCS can be interpreted as the cost, in percentage points, of immediately executing a roundtrip transaction."
>
> **Annotation.** The liquidity cost score is the $c(\Delta q)$ term of (1.2) for a normal-sized trade: the bid–ask spread quoted in spread terms, times option-adjusted spread duration, gives a round-trip cost as a percentage of price. Ben Dor's formal definition (p.118) has a second branch that matters more to this book than the first: for a bond that is **price-quoted**, LCS is simply (ask − bid)/bid. Bonds switch from spread quotes to price quotes when they become distressed, and at that moment DTS stops being the right risk measure, because "spread" has stopped meaning anything. Mags's version: "Below 70, nobody quotes you a spread. They quote you a recovery and a grudge." The risk moves to price-and-recovery space, which is where Part IV lives.

> **[SOURCE EXTRACTION]** *Veronesi_Fixed_Income_Securities p.120:* "We will rarely use the variation in the semi-annually compounded yield to maturity for risk management purposes, and rather use the variation in the continuously compounded spot curve."
>
> **Annotation.** A sentence about conventions is the most important sentence on the shelf for anyone directing a coding agent. "Duration" is not one number; it is a derivative with respect to *some* curve under *some* compounding. If the Treasury hedge is sized off a spot-curve duration and the bond's risk is computed off a semi-annual yield-to-maturity duration, the residual is a phantom position that nobody chose. The spec must name the curve, the compounding, and the bump (parallel, key-rate, or empirical). ROBO will not guess, which is good, because it would guess differently each time.

> **Desk Myth vs. Desk Reality.** *Myth:* "Spread duration is the risk measure; a seven-year bond is riskier than a four-year bond." *Reality:* Spread changes scale with spread, so the risk measure is DTS, and below about 70 points the bond stops being a spread instrument at all. The four-year single-B is the riskier bond, and the four-year CCC is mostly an equity claim with a coupon.

```python
def dts(D_spr, s_bp):
    """Duration Times Spread in bp*years: D_spr in years, s_bp in basis points."""
    return D_spr * s_bp


def dts_vol(D_spr, s_bp, sigma_rel):
    """Eq. (1.3): excess-return volatility in bp per period of sigma_rel (unitless)."""
    return dts(D_spr, s_bp) * sigma_rel


def lcs(bid, ask, oasd=None, price_quoted=False):
    """Ben Dor liquidity cost score in % of price.

    Spread-quoted: bid/ask are spreads in bp (bid spread > ask spread), LCS = OASD * (bid - ask) / 100.
    Price-quoted: bid/ask are prices, LCS = 100 * (ask - bid) / bid.
    """
    if price_quoted:
        return 100.0 * (ask - bid) / bid
    if oasd is None:
        raise ValueError("spread-quoted LCS needs OASD")
    return oasd * (bid - ask) / 100.0


# BBB at 120bp, 7y versus single-B at 450bp, 4y (illustrative)
v_bbb, v_b = dts_vol(7.0, 120.0, 0.08), dts_vol(4.0, 450.0, 0.08)
assert v_b > 2.0 * v_bbb                       # DTS: the short single-B is the riskier bond

# Monte Carlo check: lognormal relative spread moves reproduce DTS * sigma_rel within 2%
rng = np.random.default_rng(RNG_SEED)
for sigma_rel in (0.05, 0.10):
    z = rng.standard_normal(200_000)
    ds = 450.0 * (np.exp(sigma_rel * z - 0.5 * sigma_rel**2) - 1.0)   # bp
    r_xs = -4.0 * ds                                                    # bp of excess return
    assert abs(r_xs.std() / dts_vol(4.0, 450.0, sigma_rel) - 1.0) < 0.02

# Ben Dor p.61 issuer limit: MV% x spread(%) x duration <= 5
assert abs(5.0 / (1.00 * 5.0) - 1.0) < 1e-12 and abs(5.0 / (1.50 * 10.0) - 0.3333) < 1e-3
assert abs(lcs(bid=455.0, ask=445.0, oasd=4.0) - 0.40) < 1e-12      # 10bp wide x 4y = 0.40%
assert abs(lcs(bid=62.0, ask=64.0, price_quoted=True) - 100 * 2 / 62) < 1e-12

---

## 1.5 The Anthology, Part B: Pricing the Default You Might Be Catching (Bohn–Stein; Schmid; Bolder; BlackRock)

The second question about the forced seller: *if the seller is not informed, what is the bond actually worth?* That is the fair-value term, and the shelf offers two families of answers that have been arguing since the 1970s.

> **[SOURCE EXTRACTION]** *Bohn_Stein_Active_Credit_Portfolio_Management p.128:* "we need only stipulate that the market is attempting to fairly value a firm, most typically through its equity."
>
> **Annotation.** This is the structural model's entire philosophical cost, and it is cheap. If the equity market is trying to value the firm, then equity is a call option on the assets struck at the debt, $E_t = V_t N(d_1) - F e^{-r(T-t)} N(d_2)$, and the bond is the assets minus that call. Replace the risk-free drift with the physical asset drift $\mu_V$ and you get the distance to default, the number of asset-volatility standard deviations between the firm and its default point:
>
> $$
> \text{DD}_t = \frac{\ln(V_t/F) + (\mu_V - \tfrac12\sigma_V^2)(T-t)}{\sigma_V\sqrt{T-t}}, \qquad \text{PD}^{\mathbb{P}}_{\text{Gauss}} = N(-\text{DD}). \tag{1.4}
> $$
>
> $V_t$ and $\sigma_V$ are not observed; they are backed out of equity value and equity volatility using $\sigma_E E_t = \sigma_V V_t N(d_1)$ (Chapter 6 and Chapter 23 do it properly). The default point $F$ is a convention; the KMV choice commonly reported is short-term liabilities plus half of long-term debt. The desk use is immediate: equity trades every millisecond and the bond trades twice a week, so the equity market gives you a fresh fair-value input for the bid between bond prints.

> **[SOURCE EXTRACTION]** *Bohn_Stein_Active_Credit_Portfolio_Management p.138:* "under MKMV's empirical distribution and using the VK model described later in this chapter, a DD of 4 converts into an EDF of almost 1 percent."
>
> **Annotation.** Under the Gaussian map, $N(-4) \approx 0.003\%$. Under the empirical map, it is almost $1\%$: a factor of roughly 300. Kaz, on hearing this: "Let's just assume Gaussian... I regret it already." The lesson for a specifier is that the structural model is excellent at *ranking* firms and terrible at *calibrating* them, so production systems keep the DD and replace $N(\cdot)$ with an empirically fitted, monotone map from DD to default frequency. If ROBO is told to "compute PD from Merton," it will use $N(-\text{DD})$, and every IG name in the book will look immortal.

> **[SOURCE EXTRACTION]** *Schmid_Credit_Risk_Pricing_Models p.128:* "the default time is unpredictable and therefore the behavior of credit spreads for short maturities can be captured more realistically." ... "their main draw-back is the missing link between firm value and corporate default."
>
> **Annotation.** The other family. Intensity (reduced-form) models skip the balance sheet and let default arrive as the first jump of a Poisson process with intensity $\lambda_t$. Their virtue is that a pure diffusion can never default by surprise tomorrow, so structural models imply near-zero short-dated spreads, which the market flatly contradicts. With a constant $\lambda$ under $\mathbb{Q}$, a flat rate $r$, recovery $R$ of par paid at default, and a continuously paid premium $s$, equate the two legs of a CDS:
>
> $$
> s\int_0^T e^{-(r+\lambda)t}\,dt \;=\; (1-R)\int_0^T \lambda\,e^{-(r+\lambda)t}\,dt \quad\Longrightarrow\quad s = \lambda\,(1-R). \tag{1.5}
> $$
>
> The integrals are identical, so they cancel exactly, at every maturity: this is the credit triangle. With quarterly ACT/360 premium accrual it becomes an approximation. Two errors to forbid in every spec: feeding a physical EDF into (1.5), which is a $\mathbb{Q}$ relation (risk-neutral intensities run well above physical ones for IG, which Chapter 6 derives); and treating "40% recovery" as a fact about the bond rather than a CDS quoting convention (Chapter 5).

> **[SOURCE EXTRACTION]** *Bolder_Credit_Risk_Modelling p.597:* "If one assumes independence of default, then default risk is entirely idiosyncratic." ... "Relaxing this unrealistic choice, however, is the source of most of the complexity in this field."
>
> **Annotation.** For a desk catching forced flow, correlation is not a portfolio-risk nicety; it is the reason forced sellers arrive in herds. The one-factor threshold model makes it concrete: firm $i$ defaults when $\sqrt{\rho}\,Y + \sqrt{1-\rho}\,\varepsilon_i < N^{-1}(p)$, with a common factor $Y$ and idiosyncratic $\varepsilon_i$, both standard normal. Conditional on the factor, defaults are independent with probability
>
> $$
> p(Y) = N\!\left(\frac{N^{-1}(p) - \sqrt{\rho}\,Y}{\sqrt{1-\rho}}\right),
> $$
>
> so a bad draw of $Y$ moves *every* PD at once, and with it every downgrade, every CCC bucket, and every redemption. Bolder's chapter opens with Richard Feynman's line, "What I cannot create, I do not understand," which belongs on the wall of anyone who specifies models for a coding agent: if you cannot write the simulation, you do not understand the model, and neither will ROBO.

> **[SOURCE EXTRACTION]** *BlackRock_Systematic_High_Yield_Credit p.6:* "Our proprietary probability of default signal that has underpinned all of our credit strategies for over 20 years has successfully identified 77% of the defaulted bonds in the ICE BofA High Yield Index within 24 months of its default since 2010."
>
> **Annotation.** This is the structural lineage in production, reported by the manager about its own signal (treat it as a self-reported hit rate, not an audited one, and note that a hit rate without a false-positive rate is half a confusion matrix). The point for Chapter 1 is what the signal is *for*: in high yield, avoiding the default you might be catching is worth more than any factor tilt, because a 50-point jump to default erases years of carry. Chapter 11 builds the defensive book around it.

```python
from scipy.integrate import trapezoid
from scipy.stats import norm


def distance_to_default(V, F, mu_V, sigma_V, T=1.0):
    """Eq. (1.4): physical distance to default (unitless)."""
    return (np.log(V / F) + (mu_V - 0.5 * sigma_V**2) * T) / (sigma_V * np.sqrt(T))


def credit_triangle_check(lam=0.03, R=0.40, r=0.04, T=5.0, n=200_001):
    """Numerically integrate both CDS legs (measure Q) and return the par spread."""
    t = np.linspace(0.0, T, n)
    disc_surv = np.exp(-(r + lam) * t)
    prem_annuity = trapezoid(disc_surv, t)
    protection = (1.0 - R) * trapezoid(lam * disc_surv, t)
    return protection / prem_annuity


dd = distance_to_default(V=150.0, F=100.0, mu_V=0.06, sigma_V=0.10)   # illustrative IG-like firm
assert dd > 4.0 and norm.cdf(-dd) < 1e-4                               # Gaussian: 'immortal'
assert abs(credit_triangle_check() - 0.03 * 0.60) < 1e-10              # s = lambda (1 - R)

# One-factor threshold model: Monte Carlo default rate matches p; tails fatten with rho
rng = np.random.default_rng(RNG_SEED + 1)
p, rho, n_sims, n_firms = 0.02, 0.20, 20_000, 500
Y = rng.standard_normal(n_sims)
p_cond = norm.cdf((norm.ppf(p) - np.sqrt(rho) * Y) / np.sqrt(1.0 - rho))
loss_frac = rng.binomial(n_firms, p_cond) / n_firms
assert abs(loss_frac.mean() - p) < 4 * loss_frac.std() / np.sqrt(n_sims)
assert np.quantile(loss_frac, 0.99) > 5 * p                            # herds, not coin flips
```

---

## 1.6 The Anthology, Part C: Which Flows Are Harvestable (Dynkin; Man; Paleologo)

The third question: *is there a systematic way to be on the other side of forced flow, often enough, at a price that pays?* Dynkin, Ben Dor and the Barclays QPS team answer yes, and the cleanest example is the fallen angel.

> **[SOURCE EXTRACTION]** *Ben_Dor_Quantitative_Credit_Portfolio_Management p.349:* "The primary driver of this phenomenon does not seem to be overreaction to information, but rather the structural inefficiency stemming from the segmentation between the investment and non-investment-grade markets."
>
> **Annotation.** Read "segmentation" as "a graph edge with a capacity limit." When a bond crosses from BBB- to BB+, the holders whose mandates end at the IG line must sell, and the holders whose mandates begin there are fewer, smaller, and not in a hurry. The price falls below its equilibrium level and then reverses as the bond finds its new owners. That reversal is a *liquidity provision premium*, not a forecast of fundamentals, which is why it survives: you cannot arbitrage it away by being smarter, only by having a balance sheet that does not care about ratings. Dynkin adds the conditional version: forced selling "should not uniformly affect all issuers. Poor performers during the formation period were more likely to be subject to forced selling and, therefore, to experience a subsequent reversal, unlike top performers" (*Dynkin_Systematic_Investing_in_Credit p.158*). The reversal is concentrated where the forced supply is.

> **[SOURCE EXTRACTION]** *Dynkin_Systematic_Investing_in_Credit p.361:* "For Baa‐rated debt, the probability that a forced sale will occur at some time over the five‐year horizon is 23.7% if forced to sell upon any downgrade to Ba or lower, and 7.2% under the less aggressive policy of selling upon a downgrade to B or lower."
>
> **Annotation.** This is the RSSG banker's favorite kind of number: a contractual trigger, converted into a probability over a horizon. It is also the forced-supply function of §1.8 for one holder type, one trigger, and one cohort. A 23.7% five-year chance of being a forced seller is a cost the IG-only investor pays every year in the form of selling at the bottom. Dynkin's broader point (p.135) is that "the long‐term risk/return performance of a given asset class is determined in part by the sell discipline that is in place for the portfolio." The sell rule is part of the asset class, which means somebody else's sell rule is part of your opportunity set.

**Equity momentum: the flow you can see coming.** The second harvestable flow is slower. Equity markets digest bad news faster than bond markets (more trading, more short sellers, more analysts), so bond prices lag equity prices. Dynkin's decile sorts show it plainly: the bottom equity-momentum decile of US HY "delivered negative average excess return of –4.7% per year between 1993 and 2017. In contrast, the average excess return of the top decile portfolio (D10), with the strongest equity momentum, was +4.01% per year" (*Dynkin_Systematic_Investing_in_Credit p.606*). Man's own factor research finds the same: "the only spill-over to achieve meaningful statistical significance is equity Momentum, which generates a higher alpha than corporate bond Momentum itself" (*Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.31*). In the language of the bid equation, equity momentum is a public feature that updates the fair-value term before the bond trades. Man's backtested factor ladder (p.28) reports information ratios of 2.15 for value, 1.69 for momentum, 1.55 for quality, and 0.79 for its "informed investor" signal, combining to 2.35; those are model returns from the manager's own backtest, and the Trend Watch below explains why a 2026 reader should haircut them.

> **[SOURCE EXTRACTION]** *Man_Revolutions_in_Credit_Trading_2023 p.2:* "The greatest barriers to systematic approaches breaking through in credit have traditionally been execution and the ability to model transaction costs and liquidity within decades-old manual processes."
>
> **Annotation.** Every premium above is a premium *before* costs, and in 2015 the costs ate most of them. What changed is plumbing. Once a manager can send a 400-line list to a portfolio-trading desk and get a single price in minutes, the cost term $c(\Delta q)$ of the bid equation falls for the *buyer of liquidity*, and the systematic investor can finally harvest premia that were always there on paper. The same paper puts it as an aphorism: "an optimised portfolio is not optimal if you can't trade it" (p.4). It also notes that Man Numeric moved from roughly 30% of its HY and 60% of its IG order flow on electronic venues to over 90% (p.3).

> **Trend Watch: The execution revolution, 2018–2026.** *What changed:* US corporate bonds went from phone-and-chat to a market where half of IG volume trades electronically and portfolio trades are a standard protocol. *How big:* Coalition Greenwich put IG e-trading at 37% and HY at 27% in 2021 (via IFR); at 48% and 33% in 2024, with average daily notional volume (ADNV) of \$46bn, up 21%, and daily turnover rising from 0.33% of outstanding (2021) to 0.44% (2024) (The DESK, 21 Jan 2025). In 2025 ADNV passed \$50bn for the first time, IG e-trading sat just under 50% and HY at 32%, and disclosed RFQ fell to 38.6% of electronic volume (Coalition Greenwich via The DESK, 30 Jan 2026). The single-day record of \$84.7bn on 30 Sep 2025 was 18% portfolio trades (Coalition Greenwich, 27 Jan 2026). Portfolio trading rose from 11% of US corporate bond volume in 2024 to 15% in 2025, peaking at 17% in July 2025 (Morgan Stanley via The DESK, 19 Feb 2026); Barclays counted a portfolio trade every six minutes in H1 2025, against one every 41 minutes in 2020 (IFR, 2025). January 2026 then set a new record, ADNV up 22% year on year to \$61bn (Coalition Greenwich, 17 Feb 2026). *What it means for the desk:* the cost term fell, so premia that were paper alpha in 2015 became tradable; and the RFQ in the cold open is now one of tens of thousands per day, which makes toxicity screening an automated, statistical job rather than a trader's hunch. Mags: "Back in my day a portfolio trade was a fax with forty CUSIPs and a prayer. Now it's four thousand line items and no prayer. The pricing is better. I hate it." (Tradeweb reported a single portfolio trade with more than 4,000 line items; IFR, 2025.)

> **Trend Watch: The corporate bond factor replication crisis, 2019–2026.** *What changed:* the academic foundation under credit factors is being re-audited with cleaned TRACE data. Dickerson, Mueller and Robotti (2023, *Journal of Financial Economics*) found that previously proposed corporate bond factors add little beyond the bond market factor; the 2019 JFE factor paper by Bai, Bali and Wen was retracted in 2023 after a data-timing error surfaced in replication. On 9 April 2026, Dickerson, Robotti and Rossetti posted *The Corporate Bond Factor Replication Crisis* (arXiv:2604.07880), which tests 108 signals and finds that most previously documented factors lose statistical significance in bond-CAPM alphas once transaction-price measurement error and asymmetric ex-post return filtering are corrected. *What it means for the desk:* every backtested IR in this section, Man's included, should be re-estimated on error-corrected data before it earns capital (the Open Source Bond Asset Pricing project publishes such data). The flows in this chapter, fallen angels and forced sales, are more robust than the factor zoo for a structural reason: they are paid for by someone's mandate, not discovered in a regression. Chapter 9 runs the audit.

> **[SOURCE EXTRACTION]** *Paleologo_Advanced_Portfolio_Management p.111:* "Performance can be decomposed into systematic and idiosyncratic components. Most importantly, these components are investable." ... "your investors are not paying you to replicate the market, ride momentum, or short already shorted stocks."
>
> **Annotation.** Paleologo writes about equities; the logic transfers whole. Theo, proudly: "Fallen angels beat high yield by three percent a year." Kaz: "Strip the HY beta, the DTS, and the index-inclusion bid, then tell me." IDO or it didn't happen. Part of the fallen-angel premium is plain spread beta (fallen angels are long-duration BBs), part is the liquidity premium you are paid for being there on the rebalance date, and only the residual is skill. Paleologo's sharper version (p.139) is the desk motto's parent: "factors can find infinite ways to mar your performance, but cannot tell you how to be profitable." The bid equation's $\sigma_{\text{IDO}}$ is that decomposition applied to a single trade.
