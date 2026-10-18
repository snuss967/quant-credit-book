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
| **Open-End HY Funds & Bond ETFs (NAV-Redemption Sellers)** | iShares (HYG, LQD), SPDR (JNK), Vanguard and other HY mutual fund complexes | Daily liquidity to end-investors | Cheap beta delivery; daily liquidity on illiquid assets | Liquidity mismatch: they sell what is liquid, not what is expensive; ETF prices gap below NAV when authorized participants stop arbitraging | IG index funds sell fallen angels at the month-end rebalance and HY index funds buy them at inclusion; open-end funds meet redemptions within days. Clock: a known calendar date, or the day after a bad headline. |

Everyone in that table is smart. Most of them are not the problem. The problem is the last column: every row has a trigger that converts a rating, a test, or a redemption into a sale, at a time you can often predict and in a size you can often estimate. A forced sale is **information-free about the bond and information-rich about the seller**. The rest of this chapter is about telling those two kinds of information apart, at speed, for money.


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

**The Spec You Hand the Robot.** Implement (1.2) as `reservation_bid(S, q, dq, gamma, sigma_ido, h_years, pi, J, c)`. Units are part of the contract: points per 100 par for `S`, `J`, `c`; points per $\sqrt{\text{year}}$, *post-hedge*, for `sigma_ido`; \$mm par for `q`, `dq` (long positive; `dq > 0` means the client sells to us); $1/(\$\text{mm}\cdot\text{pt})$ for `gamma`; years for `h_years`. Raise on `dq <= 0`, `pi` outside $[0,1]$, `h_years <= 0`, or negative scale inputs. Never condition twice: if `S` already conditions on the RFQ, pass `pi = 0`. Never clip a short desk's bid above $S - c$; it is correct. Add `posterior_informed` (logit-form Bayes), a seeded `glosten_milgrom_markout` whose mean must equal $-\pi J$ within three standard errors, and `jump_penalty_ratio`, which must tend to 1 as $\gamma q\ell \to 0$ and rise with $q$.

<!-- EXPLAIN: Listing 1.1 -->
> **Code Companion: Listing 1.1.** Dealer bid for buying dq ($mm par) from a client: eq. The full python listing is in [Appendix F, Listing 1.1](#code-1-1).

The numerical guards are deliberate. `np.expm1` keeps the jump penalty accurate when $\gamma q\ell$ is tiny (a naive `exp(x) - 1 - x` loses every significant digit below about $10^{-8}$), and `posterior_informed` refuses a prior of exactly 0 or 1, because a desk that is certain nobody is informed has already lost the hand.

### Deep-Dive Resource Graph

- **Podcasts.** *Flirting with Models* (Corey Hoffstein), https://www.flirtingwithmodels.com/ , systematic practitioners on process.
- **Practitioner Writing.** Man Institute (Robert Lam and Paul Kamenski), *The Revolutions in Credit Trading* (2023), https://www.man.com/insights/revolutions-in-credit-trading .
- **Academic Papers.** Glosten and Milgrom (1985), *Bid, Ask and Transaction Prices in a Specialist Market with Heterogeneously Informed Traders*, JFE. Ho and Stoll (1981), *Optimal Dealer Pricing under Transactions and Return Uncertainty*, JFE. Avellaneda and Stoikov (2008), *High-Frequency Trading in a Limit Order Book*, Quantitative Finance.
- **Data & Code.** FINRA TRACE, https://www.finra.org/filing-reporting/trace , the tape every markout is computed against.

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

<!-- EXPLAIN: Listing 1.2 -->
> **Code Companion: Listing 1.2.** Duration Times Spread in bp*years: D_spr in years, s_bp in basis points. The full python listing is in [Appendix F, Listing 1.2](#code-1-2).

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

> **Trend Watch: The execution revolution, 2018–2026.** *What changed:* US corporate bonds went from phone-and-chat to a market where half of IG volume trades electronically and portfolio trades are a standard protocol. *How big:* Coalition Greenwich put IG e-trading at 34% and HY at 25% in 2021 (its restated series) and at 48% and 33% in 2024, with average daily notional volume (ADNV) of \$46bn, up 21%, and daily turnover rising from 0.33% of outstanding (2021) to 0.44% (2024) (The DESK, 21 Jan 2025). In 2025 ADNV passed \$50bn for the first time, IG e-trading sat just under 50% and HY at 32%, and disclosed RFQ slipped to roughly 40% of electronic volume (Coalition Greenwich via The DESK, 30 Jan 2026). The single-day record of \$84.7bn on 30 Sep 2025 was 18% portfolio trades (Coalition Greenwich, 27 Jan 2026). Portfolio trading rose from 11% of US corporate bond volume in 2024 to 15% in 2025, peaking at 17% in July 2025 (Morgan Stanley via The DESK, 19 Feb 2026); Barclays counts a portfolio trade every few minutes in 2025, against roughly one every 40 minutes in 2020 (IFR, 2025). January 2026 then set another record, ADNV up more than 20% year on year (Coalition Greenwich, 17 Feb 2026). *What it means for the desk:* the cost term fell, so premia that were paper alpha in 2015 became tradable; and the RFQ in the cold open is now one of tens of thousands per day, which makes toxicity screening an automated, statistical job rather than a trader's hunch. Mags: "Back in my day a portfolio trade was a fax with forty CUSIPs and a prayer. Now it's four thousand line items and no prayer. The pricing is better. I hate it." (Tradeweb reported a single portfolio trade with several thousand line items; IFR, 2025.)

> **Trend Watch: The corporate bond factor replication crisis, 2019–2026.** *What changed:* the academic foundation under credit factors is being re-audited with cleaned TRACE data. Dickerson, Mueller and Robotti (2023, *Journal of Financial Economics*) found that previously proposed corporate bond factors add little beyond the bond market factor; the 2019 JFE factor paper by Bai, Bali and Wen was retracted in 2023 after a data-timing error surfaced in replication. On 9 April 2026, Dickerson, Robotti and Rossetti posted *The Corporate Bond Factor Replication Crisis* (arXiv:2604.07880), which tests 108 signals and finds that most previously documented factors lose statistical significance in bond-CAPM alphas once transaction-price measurement error and asymmetric ex-post return filtering are corrected. *What it means for the desk:* every backtested IR in this section, Man's included, should be re-estimated on error-corrected data before it earns capital (the Open Source Bond Asset Pricing project publishes such data). The flows in this chapter, fallen angels and forced sales, are more robust than the factor zoo for a structural reason: they are paid for by someone's mandate, not discovered in a regression. Chapter 9 runs the audit.

> **[SOURCE EXTRACTION]** *Paleologo_Advanced_Portfolio_Management p.111:* "Performance can be decomposed into systematic and idiosyncratic components. Most importantly, these components are investable." ... "your investors are not paying you to replicate the market, ride momentum, or short already shorted stocks."
>
> **Annotation.** Paleologo writes about equities; the logic transfers whole. Theo, proudly: "Fallen angels beat high yield by three percent a year." Kaz: "Strip the HY beta, the DTS, and the index-inclusion bid, then tell me." IDO or it didn't happen. Part of the fallen-angel premium is plain spread beta (fallen angels are long-duration BBs), part is the liquidity premium you are paid for being there on the rebalance date, and only the residual is skill. Paleologo's sharper version (p.139) is the desk motto's parent: "factors can find infinite ways to mar your performance, but cannot tell you how to be profitable." The bid equation's $\sigma_{\text{IDO}}$ is that decomposition applied to a single trade.

---

## 1.7 The Anthology, Part D: Where the Flows End Up (Moyer; Houlihan Lokey)

The last question: *when the company breaks, who is left holding what, and who has to sell it?* This is home turf for the reader, and Moyer's distressed-debt classic is honest about how far the quants had come when it was written.

> **[SOURCE EXTRACTION]** *Moyer_Distressed_Debt_Analysis p.275:* "As much as the quantitative approach of financial econometricians would suggest that investing is fundamentally a science, in distressed investing it is more of an art." ... "This is why knowledge of the process, experience, and judgment are often more critical to investment success than tedious hours of financial modeling."
>
> **Annotation.** This book agrees with every word and draws the opposite conclusion. "Knowledge of the process" is exactly what can be written down: exclusivity periods, voting thresholds, DIP roll-ups, plan classes, and which creditor has the hold-up value. Once written down, process knowledge becomes features, transition probabilities, and a prior over $J$ in the bid equation. What stays an art is the judgment about which features matter in *this* case, and that is the job description for the human in Man's quote from §1.1. Moyer also tells us where to look for mispricing: "when the news is very bad, the market often will trade down to the worst-case scenario valuations" (p.257), because sellers who need out meet buyers who demand a discount for uncertainty. That is a forced-seller edge with a docket number.

> **[SOURCE EXTRACTION]** *Moyer_Distressed_Debt_Analysis p.370:* "Banks and collateralized debt obligations (CDOs) are not natural holders of equity securities." ... "when such entities are known to be large holders of the postreorganization equity, other market participants will certainly consider their net sell disposition."
>
> **Annotation.** The forced-seller graph does not end at default; it rewires. Loans convert into post-reorganization equity, and the holders of those loans (CLOs, banks) are often barred from, or penalized for, holding equity. So the most predictable seller of a newly reorganized stock is its largest holder, and everybody knows it. Moyer's other forced seller is smaller and sadder: the trade creditor who "may not have the financial wherewithal to wait until the completion of a bankruptcy case to realize full value of the claim and thus is a forced seller" (p.310). Claims trading is that edge in pure form (Chapter 16).

> **[SOURCE EXTRACTION]** *Houlihan_Lokey_Distressed_MA p.35:* "Under Section 363, for example, a debtor with Court approval may sell assets free and clear of all liens, claims and encumbrances (which attach only to the proceeds of such sales)."
>
> **Annotation.** One clause, and it converts the *assets* of a broken firm into a clean asset sale while the *claims* follow the cash. For the flow graph, a 363 sale is a node where the holder set changes completely: the buyer gets the assets with no legacy creditors, and the old creditors get a claim on a pot whose size the auction sets. Pricing the claim means pricing the auction.

Kaz, reading over Theo's shoulder: "A fulcrum is where a lever balances. So the fulcrum security is the tranche with zero duration?" Mags: "It's the tranche that gets the equity and the lawsuits." (The fulcrum is the class whose recovery straddles the enterprise value: everything senior is covered, everything junior is out of the money, and the fulcrum becomes the new owner. It has more duration than anything, measured in years of litigation.)

---

## 1.8 The Ecosystem as a Forced-Seller Flow Graph

Put the four parts of the anthology together and the market stops looking like a crowd and starts looking like plumbing. Each holder type is a node. Each trigger (a downgrade to HY, a downgrade to CCC, a default, a redemption wave) opens a set of edges with a known direction, an estimable size, and a response window. Blackstone's systematic credit paper describes the machine built to sit at the end of those edges, in the vendor's own words: "The systematic optimizer naturally acts as a contrarian liquidity provider. When credit spreads widen aggressively (often due to market panic rather than fundamental deterioration), the model algorithmically increases credit exposure" (*Blackstone_Systematic_Credit p.1*). The parenthesis is the whole bet: that the seller is forced, not informed.

### 1.8.1 The model (measure: $\mathbb{P}$)

Let holder types be $i = 1,\dots,n$, bond segments $k$, and triggers $\tau$. Holdings $H_{k,i}$ are in \$bn of par; $f_i(\tau)\in[0,1]$ is the fraction holder $i$ must sell after trigger $\tau$, over a window $w_i(\tau)$ (insurers: quarters; index funds: the month-end rebalance; CLOs: the next test date; open-end funds: days). Natural absorbers $j$ have capacity $A_{k,j}(\tau)$: HY index funds that must *buy* at inclusion (Moyer p.35's "forced" buyers), fallen-angel programs, crossover and distressed funds, and dealers' balance sheets. Then

$$
Q^{\text{sell}}_k(\tau) = \sum_i H_{k,i}\,f_i(\tau), \qquad
I_k(\tau) = Q^{\text{sell}}_k(\tau) - \sum_j A_{k,j}(\tau). \tag{1.6}
$$

The positive part of the imbalance $I_k$ must be absorbed at a price concession. Model the price as a fundamental value $p^*$ minus a temporary pressure term that decays at rate $\theta$ (per day) after the trigger date $t_0$:

$$
p_t = p^* - \kappa\,\frac{\max(I_k,0)}{\text{ADV}_k}\,e^{-\theta(t-t_0)}, \qquad t \ge t_0, \tag{1.7}
$$

where $\text{ADV}_k$ is the segment's average daily volume and $\kappa$ is price impact in points per day of volume. The absorber who buys at $t_0$ and holds for $T$ days earns the recovered pressure, $\kappa\,(I_k^+/\text{ADV}_k)(1-e^{-\theta T})$. That is the drop-and-reversal that Ben Dor (p.349) and Dynkin (p.158) document for fallen angels, and that Ellul, Jotikasthira and Lundblad (2011) tie to insurers' regulatory constraints. Note what (1.7) leaves out: a *permanent* component. If the seller is informed, part of the drop never reverses, and that is the toxicity term $\pi J$ from (1.2). The forced-seller graph prices the temporary component; the RFQ model prices the permanent one. A desk needs both.

**Where this blows up.** Holders get double-counted (a loan inside a CLO is not also on the bank's books). Windows get misaligned (insurer selling is slow; index selling is a date). $\kappa$ is not stable across regimes. Above all, absorption capacity is *state-dependent*: it collapses exactly when supply peaks, because the absorbers are also being redeemed. A model with constant $A$ is a fair-weather model. Moyer (p.55) gives the CLO version of the trigger: "When an investment in the portfolio is downgraded to B– or CCC, the manager may be forced to sell something (again without regard to the portfolio manager's view of fair value) to remain in compliance with the CDO-ORs." A CLO is a buy-and-hold investor with a 7.5% allergy. It does not sell because it wants to; it sells because the indenture sneezes.

> **Trend Watch: Who holds credit now, 1993–2026.** *What changed:* the holder graph got more mechanical. CDOs and CLOs held about 3% of low-rated loans and bonds in 1993 and more than 20% by the early 2000s (*Moyer_Distressed_Debt_Analysis p.55*, Figure 2-18); by 2026 US CLOs held roughly \$1tn, about 65% of a roughly \$1.5tn institutional leveraged loan market (Maples/Nuveen Q&A, 13 Apr 2026). CLO ETF assets grew roughly ten-fold between 2023 and end-2024 (Deutsche Bank Flow, 11 Feb 2025). US fixed income ETF assets reached about \$2tn by mid-2025 (as reported by The Daily Upside, 2 Jul 2025). Life insurers' private placements rose from 14% (2016) to 22% (2024) of their corporate bond holdings (Chicago Fed Insights, May 2026), and privately placed bonds reached 48.4% of life-industry bonds at YE2025 against 37.4% five years earlier (S&P Global Market Intelligence via Insurance Business, 10 Aug 2026). Dealers, meanwhile, swung sharply *net short* in corporate bonds in early 2026 (Coalition Greenwich, 17 Feb 2026). And the fallen-angel pipeline reopened: tens of billions of dollars of fallen-angel supply arrived in 2026 through mid-year (Insight Investment/BNY, Aug 2026). *What it means for the desk:* more of the market sits with holders whose sales are triggered by rules (CLO tests, ETF flows, NAIC capital), and less with dealers whose balance sheet used to absorb them. More predictable forced supply, less natural absorption: that is a bigger $I_k$ for the same shock, and a bigger premium for whoever has the capacity.

### Specification for AI Implementation

**What ROBO built from the vague version.** Spec: "map the forced sellers." ROBO returned a graph with one node, labeled "Everyone, March 2020," and a self-loop.

**The Spec You Hand the Robot.** Build `ForcedSellerGraph(holdings, rules, capacity)`. `holdings`: a DataFrame, index = segment, columns = holder, values in \$bn par, all $\ge 0$. `rules`: `{holder: {trigger: (fraction, window_days)}}` with `0 <= fraction <= 1` and `window_days > 0`; a holder with no rule for a trigger sells nothing. `capacity`: `{trigger: DataFrame(index = segment, columns = absorber)}` in \$bn, all $\ge 0$. `run(trigger, segment, stress=False)` returns sells by holder, buys by absorber, `dealer_residual` (the positive imbalance), and a list of `(seller, buyer, size)` edges, allocating supply to absorbers pro rata to capacity and the remainder to `dealer_residual`. Assertions that must hold on every call: (a) **conservation**, total sells equal total buys plus `dealer_residual` to $10^{-9}$, and the edge sizes sum to total sells; (b) no holder sells more than it holds; (c) `price_path` per (1.7) returns to within 0.01 points of $p^*$ by `10/theta` days; (d) `stress=True` zeroes all capacity, and then `dealer_residual` equals forced supply exactly. All numbers in the demo are *illustrative*.

<!-- EXPLAIN: Listing 1.3 -->
> **Code Companion: Listing 1.3.** Holder x trigger forced-supply engine: eqs. The full python listing is in [Appendix F, Listing 1.3](#code-1-3).

### 1.8.2 Case Study A: Ford and the March 2020 Fallen-Angel Wave

March 2020 is the flow graph with every edge lit. More than \$90bn of debt fell from investment grade in that one month, nearly twice the prior monthly record of \$48bn set in 2005, and the first half of 2020 reached \$197bn, the largest on record (J.P. Morgan data via T. Rowe Price, Nov 2020). The headline was Ford: S&P cut it to BB+ on 25 March 2020 (as reported by Bloomberg), and with two high-yield ratings roughly \$36bn of Ford debt left the IG index at the month-end rebalance (T. Rowe Price). Man's paper describes the mechanism exactly: "When a company is downgraded to below investment grade status by the ratings agencies, it drops out of the index at the next monthly rebalancing and there is a significant wave of forced selling around the event" (*Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.38*).

Walk the graph. *Who sells, and when:* IG index funds and ETFs on the rebalance date (a date anyone could read off a calendar); IG active funds over weeks; insurers over quarters, because higher capital charges make holding costly but not impossible. *Who buys:* HY index funds, forced to add the bond at inclusion, which made Ford one of the largest issuers in HY indices overnight; fallen-angel programs; crossover funds. *What broke:* absorption capacity, because HY funds were themselves facing record outflows. *What changed it:* the Federal Reserve. The Secondary Market Corporate Credit Facility was established on 23 March 2020, and in April the Fed extended its corporate facilities to issuers that had been investment grade as of 22 March, which covered Ford. A forced-seller event became a forced-buyer event by announcement. In (1.6), a new absorber with very large $A$ appeared, and $I_k$ went from huge to manageable before most of the selling had happened.

*How a systematic desk would have flagged it:* distance to default collapsing through February and March as equity fell and equity volatility rose (§1.5); Ford's equity in the bottom momentum decile (§1.6); the rating-agency watch list giving the trigger date, and the index calendar giving the window. *How it would have traded it:* estimate $Q^{\text{sell}}$ by holder, stand ready to absorb at the rebalance with a bid that charged for inventory and cost but put $\pi$ near zero (index funds are the textbook uninformed seller), and size it with DTS rather than duration. IDO or it didn't happen: the profit that followed was mostly the Fed and spread beta, and a desk that booked it as alpha learned nothing.

### 1.8.3 Case Study B: 12 March 2020, LQD at a 5% Discount

On 12 March 2020, the iShares iBoxx \$ Investment Grade Corporate Bond ETF (LQD) closed at a 5.0% discount to its net asset value; the next day the discount was 0.19%, while VCIT and SPIB had shown discounts of 3.2% and 3.1% (WealthManagement.com, 16 Mar 2020). Kaz's first instinct was arbitrage: buy the ETF, short the basket, collect five points. The problem was the basket. The NAV was computed from evaluated bond prices that had not traded, so it was stale, and the ETF price was the only live price in the market. Authorized participants stopped closing the gap because they could not sell the underlying bonds at NAV either. The ETF was not mispriced; the NAV was.

In the bid equation, both the inventory term and the cost term exploded at once: $\sigma_{\text{IDO}}$ jumped because DTS-scaled volatility jumps in a crisis (Ben Dor p.26), and $c(\Delta q)$ jumped because the exit was the same crowded door. In the flow graph, open-end funds and ETFs became sellers of whatever was liquid, and the absorber of last resort arrived only by announcement: the SMCCF was established on 23 March 2020, began buying ETFs on 12 May 2020 (New York Fed, 11 May 2020) and corporate bonds in June, and ceased purchases on 31 December 2020 (Federal Reserve). Chapter 20 rebuilds the creation–redemption arbitrage band and shows why it widens exactly when you want to use it.

### Deep-Dive Resource Graph

- **Podcasts.** Bloomberg *Odd Lots* has covered fallen angels, credit ETFs and the March 2020 dash for cash in several episodes (search the archive by topic; we do not cite episode numbers).
- **Practitioner Writing.** T. Rowe Price, *Navigating the Fallen Angels in the Post-Coronavirus Landscape* (Nov 2020), https://www.troweprice.com/institutional/ch/en/insights/articles/2020/q4/navigating-fallen-angels-post-coronavirus-landscape.html . WealthManagement.com on IG ETF discounts (16 Mar 2020), https://www.wealthmanagement.com/etfs/under-market-stress-fixed-income-etfs-trade-with-wide-discount . Vontobel, *CLOs: Lessons from the Past* (20 Mar 2020), https://am.vontobel.com/insights/clos-lessons-from-the-past . Chicago Fed Insights on life insurers' interconnectedness (May 2026), https://www.chicagofed.org/publications/chicago-fed-insights/2026/assessing-life-insurers-interconnectedness . Insight Investment (BNY), *Hidden in Plain Sight: Seeking Opportunities in Fallen Angels* (Aug 2026), https://www.bny.com/investments/us/en/institutional/articles/fixed-income/hidden-in-plain-sight-seeking-opportunities-in-fallen-angels.html .
- **Academic Papers.** Ellul, Jotikasthira and Lundblad (2011), *Regulatory Pressure and Fire Sales in the Corporate Bond Market*, Journal of Financial Economics 101(3). Ambrose, Cai and Helwege (2008), *Forced Selling of Fallen Angels*, Journal of Fixed Income. Coval and Stafford (2007), *Asset Fire Sales (and Purchases) in Equity Markets*, Journal of Financial Economics. Haddad, Moreira and Muir (2021), *When Selling Becomes Viral: Disruptions in Debt Markets in the COVID-19 Crisis and the Fed's Response*, Review of Financial Studies. O'Hara and Zhou (2021), *Anatomy of a Liquidity Crisis: Corporate Bonds in the COVID-19 Crisis*, Journal of Financial Economics. Kargar, Lester, Lindsay, Liu, Weill and Zúñiga (2021), *Corporate Bond Liquidity during the COVID-19 Crisis*, Review of Financial Studies 34(11).
- **Data & Code.** Federal Reserve, Secondary Market Corporate Credit Facility, https://www.federalreserve.gov/monetarypolicy/smccf.htm . New York Fed SMCCF notice of 11 May 2020, https://www.newyorkfed.org/newsevents/news/markets/2020/20200511 . Federal Reserve Z.1 Financial Accounts (holders of corporate bonds by sector), https://www.federalreserve.gov/releases/z1/ .

---

## 1.9 Toxic Flow: When the Seller Knows

The forced-seller graph is the good news: flows you can see coming, from sellers who know nothing. The cold open was the bad news: a seller who knew everything. The difference between them is the permanent component that (1.7) leaves out and (1.2) charges for.

### 1.9.1 Case Study C: Serta Simmons, 2016–2026 (the Counterparty Who Knew)

> **Docket Diary.** *November 2016:* Serta Simmons Bedding borrows under a \$1.95bn first-lien term loan. *June 2020:* a majority group holding about 52.6% of the roughly \$1.887bn first-lien loans exchanges about \$992mm of them into about \$734mm of new super-priority "first lien second out" debt, alongside \$200mm of new money; the excluded lenders, about 47.4% (roughly \$895mm), are primed. *31 December 2024:* the Fifth Circuit holds that the exchange was not an "open market purchase" and that the excluded lenders' sacred right to pro rata sharing was breached. *7 July 2026:* on remand, the participating lenders are held liable for \$261.13mm of damages as of 22 June 2020, plus 9% New York prejudgment interest, with the cashless exchange treated as a "payment" (Mayer Brown, July 2026). The Ad Hoc Group, in unison: "We were represented by counsel. We were not, the Fifth Circuit has now clarified, represented in an open market."

The same day the Fifth Circuit ruled on Serta, New York's Appellate Division upheld Mitel's uptier, because Mitel's agreement let it "purchase" loans with no "open market" qualifier at all (Mayer Brown, May 2025); and in December 2025 a federal district court reversed the bankruptcy court and blessed the multi-step Wesco/Incora uptier (Mayer Brown, January 2026). Three courts, three documents, three outcomes. "Open market purchase" has become the most expensive three words in finance: on the Serta remand they were priced at \$261.13mm plus nine percent a year since June 2020, for a phrase nobody had defined.

**The market maker's version.** Forget the litigation and replay the RFQs. In the weeks before 22 June 2020, a sell RFQ on Serta first-lien paper could come from two kinds of account: a lender outside the negotiating group (uninformed, perhaps a CLO trimming a CCC name), or a lender *inside* it, offloading exposure it was about to prime, or that it knew would be left behind. The second is the purest toxic flow in credit: the jump $J$ is the priming loss, and the seller knows its sign and roughly its size. Equation (1.2) says the right bid depends on $\pi(\mathbf{x})$, and the Bayes step of §1.3.3 says $\pi$ is a function of *who is on the call*: membership in the group, Rule 2019 disclosures once a case is filed, the timing relative to lender meetings, the account's markout history. None of that is in the bond's price history. All of it is in the documents and the docket, which is where Theo comes in. Ines's hand history closes the loop: bucket every RFQ by those features, compute five-day markouts, and the average markout per bucket is your estimate of $-\pi J$. Chapter 3 builds the toxicity model; Chapter 13 builds the Priming Risk Score that feeds it.

> **Trend Watch: Liability management takes over the default statistics, 2024–2026.** *What changed:* most "defaults" are now negotiated. Distressed exchanges were more than 60% of default volume in 2024 through mid-December, the highest share since at least 2000; the 2024 HY default rate was 1.4% including distressed exchanges against 0.3% excluding them, and for loans 4.0% against 1.5% (Marquette Associates, 18 Dec 2024). Moody's (18 May 2026) put distressed restructurings at about 65% of 2025 corporate defaults, and in its sample of 1,173 borrowers with soft credit events since 1979, about one in four ended in a hard default, with more than 70% of eventual hard defaults after a distressed restructuring arriving within two years. *What it means for the desk:* the jump $J$ in the bid equation is increasingly a *negotiated* jump, timed by lender calls and documents rather than by a missed coupon, which makes counterparty state the dominant feature in $\pi(\mathbf{x})$ and makes "default" a poor label for anything you train on. Chapter 14 models the regime shift.

---

## 1.10 Desk Debrief

- **Every bid is three bets.** Fair value, inventory, toxicity: $B^* = S_t - \pi J - \tfrac12\gamma\sigma^2_{\text{IDO}}h(2q+\Delta q) - c$. Kaz's engine got two of them right; the third cost \$2mm.
- **A forced sale is information-free about the bond and information-rich about the seller.** Price the seller, not just the CUSIP.
- **$\pi$ is a function of who is on the call.** The Bayes step turns counterparty state into a logistic regression; markouts by feature bucket are how you estimate it.
- **Risk scales with spread.** Use DTS, not spread duration, and remember that the slope steepens in a crisis. Below about 70, stop quoting spreads and start modeling recoveries.
- **Calibrate, don't just rank.** A Gaussian DD of 4 says 0.003%; an empirical map says almost 1%. Feed only $\mathbb{Q}$ quantities into the credit triangle.
- **The holder graph is getting more mechanical.** CLOs (about 65% of loans), ETFs (about \$2tn), insurers' private placements (48% of life-industry bonds) and sharp dealer net shorts mean more rule-driven supply and less natural absorption.
- **Execution made it possible; replication will decide what survives.** Half of IG trades electronically and PT is 15% of volume, but most published bond factors fail on clean data. Flows paid for by someone's mandate are sturdier than factors found in a regression.
- **IDO or it didn't happen.**

### The Spec You Hand the Robot

> Build a Python module `desk_core` (numpy, pandas, scipy; seeded; no I/O). (1) `reservation_bid(S, q, dq, gamma, sigma_ido, h_years, pi, J, c)` per eq. (1.2), measure $\mathbb{P}$; units: points per 100 par, \$mm par (long positive; `dq > 0` = client sells), $1/(\$\text{mm}\cdot\text{pt})$, years; raise on `dq <= 0`, `pi` outside $[0,1]$, `h_years <= 0`, negative scale inputs; never clip a short desk's bid. (2) `posterior_informed(mu, log_lr)` in logit form; reject `mu` in $\{0,1\}$. (3) `dts_vol(D_spr, s_bp, sigma_rel)` per eq. (1.3), result in bp per period; `lcs()` with spread-quoted and price-quoted branches. (4) `ForcedSellerGraph(holdings, rules, capacity)` per eqs. (1.6)–(1.7) with pro rata absorption, a `dealer_residual` node, `edges`, and `price_path`. Mandatory assertions: comparative statics of the bid ($\partial B/\partial q<0$, $\partial B/\partial\pi<0$, $\partial B/\partial\Delta q<0$); simulated markout equals $-\pi J$ within 3 s.e.; lognormal Monte Carlo reproduces DTS·$\sigma_{\text{rel}}$ within 2%; conservation of flow to $10^{-9}$; stress toggle sends all supply to `dealer_residual`; price path reverts to within 0.01 points by `10/theta` days. Do not condition on the RFQ twice. Label every demo number illustrative.

### Exercises

1. **(Derivation.)** Derive the dealer's *ask* for a client buying $\Delta q$, and show that the bid–ask midpoint for a two-sided quote of size $\Delta q$ equals the reservation mid $r^{\text{res}} = m - \gamma\sigma^2_{\text{IDO}}h\,q$ when both sides carry the same $m$. What happens to the midpoint when the buy-side RFQ carries a different toxicity $\pi'$?
2. **(Bayes, with a poker face.)** The prior share of informed sellers is 3%. An account in a known ad hoc group sells 58 minutes after a lender call, which you estimate multiplies the likelihood ratio by 12, and shows the bond to five dealers, which multiplies it by 1.5. Compute $\pi$. At $J = 13$ points, how many points does toxicity take off the bid? Would you rather know the jump size or the counterparty?
3. **(DTS.)** A portfolio holds equal market values of a 10-year BBB at 140 bp and a 3-year CCC quoted at 68. Explain why DTS is meaningful for the first and not the second, and propose a single risk measure that covers both (hint: Ben Dor's two-branch LCS is a clue).
4. **(Flow graph.)** Re-run the Ford-sized example with the Fed added as an absorber with \$5bn of capacity from day 10. Modify `run` so capacity can arrive on a date, and show how the drop and the 60-day reversal change. Who earned the reversal: the desk, or the central bank?
5. **(ROBO literalism.)** Write the one-sentence vague spec that would make ROBO fit a toxicity model with a perfect in-sample markout and zero out-of-sample value. Then write the two clauses that prevent it (one concerns issuer-grouped cross-validation, Chapter 7; the other concerns the label window).
6. **(Courtroom quant.)** Using the Serta and Mitel facts, write a binary feature "credit agreement permits non-pro-rata purchases without an open-market qualifier," and argue whether it belongs in $\pi(\mathbf{x})$, in $J$, or in both.

### Deep-Dive Resource Graph

- **Podcasts.** Bloomberg *Odd Lots* episodes on corporate bond market structure, portfolio trading, liability management and private credit (search by topic; episode numbers deliberately omitted). *Flirting with Models* (Corey Hoffstein), https://www.flirtingwithmodels.com/ .
- **Practitioner Writing.** Coalition Greenwich, *U.S. corporate bond trading in 2025 by the numbers* (27 Jan 2026), https://www.greenwich.com/node/158274 , and *Dealer net short in corporate bonds sets record* (17 Feb 2026), https://www.greenwich.com/node/158326 . The DESK on 2025 credit e-trading (30 Jan 2026), https://www.fi-desk.com/?p=27374 , and on portfolio trading (19 Feb 2026), https://www.fi-desk.com/ig-credit-sees-portfolio-trading-plateau-while-hy-hits-records/ . IFR, *Portfolio trading continues dizzying growth* (2025), https://www.ifre.com/topic-codes/2293541/portfolio-trading-continues-dizzying-growth . Mayer Brown on Serta's damages ruling (Jul 2026), https://www.mayerbrown.com/en/insights/publications/2026/07/serta-simmons-bedding-the-fifth-circuits-uptier-decision-and-the-landmark-damages-ruling-on-remand , on Serta and Mitel (May 2025), https://www.mayerbrown.com/en/insights/publications/2025/05/serta-and-mitel-the-latest-major-court-decisions-on-uptier-transactions , and on Wesco (Jan 2026), https://www.mayerbrown.com/en/insights/publications/2026/01/the-state-of-play-on-uptiers-district-court-reversal-in-wesco-blesses-multistep-transactions . Proskauer, *The End of Non-Pro Rata Uptiers?* (2 Jan 2025), https://www.proskauer.com/alert/the-end-of-non-pro-rata-uptiers . Marquette Associates, *A Damsel in Distress* (18 Dec 2024), https://www.marquetteassociates.com/damsel-in-distress/ . Moody's, *Lend, extend, and then...* (18 May 2026), https://www.moodys.com/web/en/us/insights/credit-risk/private-credit/lend-extend-and-then.html . Matt Levine, *Money Stuff* (Bloomberg Opinion), on uptiers and "open market purchases"; *Petition* on restructuring.
- **Academic Papers.** Dickerson, Robotti and Rossetti (2026), *The Corporate Bond Factor Replication Crisis*, arXiv:2604.07880, https://arxiv.org/abs/2604.07880 . Dickerson, Mueller and Robotti (2023), *Priced Risk in Corporate Bonds*, Journal of Financial Economics 150(2). Jostova, Nikolova, Philipov and Stahel (2013), *Momentum in Corporate Bond Returns*, Review of Financial Studies 26(7). Kelly, Palhares and Pruitt (2023), *Modeling Corporate Bond Returns*, Journal of Finance 78(4). Houweling and van Zundert (2017), *Factor Investing in the Corporate Bond Market*, Financial Analysts Journal 73(2). Israel, Palhares and Richardson (2018), *Common Factors in Corporate Bond Returns*, Journal of Investment Management 16(2).
- **Data & Code.** Open Source Bond Asset Pricing (error-corrected TRACE and bond factors), https://openbondassetpricing.com/ . FINRA TRACE, https://www.finra.org/filing-reporting/trace . SEC EDGAR, https://www.sec.gov/edgar . CourtListener REST API, https://www.courtlistener.com/help/api/ .

<!-- STATUS: COMPLETE -->
