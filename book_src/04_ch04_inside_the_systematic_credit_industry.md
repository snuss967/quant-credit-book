# Chapter 4: Inside the Systematic Credit Industry

At 7:40 a.m. Ines Okafor puts six documents on Theo's desk in the order a dealer stacks a deck: Man Group's two papers on quantitative credit, BlackRock's note on systematic high yield, Nuveen's multi-asset credit framework, a long Barclays book, and two thin pages from Blackstone. "Tell me which of these desks we are," she says, "and which one is going to eat us."

Theo has read a thousand pitch books. He knows the genre. One slide shows the process as a funnel. One shows risk as a dial. One says "capacity" next to a number with no derivation and an asterisk. He opens the first paper and looks for the funnel.

Kaz rolls over with a laptop. "I already built the framework. Alpha model, risk model, optimizer. Backtested Sharpe of 3.1."

"Net of what?"

"Transaction costs are a parameter," Kaz says. "I set it to zero so it wouldn't bias the results."

Mags walks past with a coffee and doesn't slow down. "Four white papers, one memo. Buy cheap, don't get defaulted on, and for God's sake measure your costs. Back in my day we called that a desk, not a framework."

She is right about the memo. Every paper on the pile wants cheap bonds, improving bonds, bonds that won't default, and bonds that pay you to wait. Theo can read that in twenty minutes. What takes him the morning is that the papers *disagree* about nearly everything else. They disagree about what data you are allowed to know and when you knew it, how a forecast becomes a position, how the position gets filled, how big the book can grow before the book *is* the market, and which risks you hedge and which you are paid to hold. Kaz's Sharpe of 3.1 lives entirely in the gap between the memo and the plumbing.

By lunch Theo has a sheet of paper with six columns and a lot of blank cells. He looks at the blanks the way he used to look at a capital structure with a hole in the guarantor coverage. The hole is where the money is.

The question this chapter answers: **on which axes do systematic credit shops actually differ, and where on that map is there room for a desk that knows what the credit agreement says?**

By the end of this chapter you will be able to:

- name the five businesses that share the label "systematic credit" and say which constraint binds each one;
- explain, with dated numbers, why credit went systematic about twenty years after equities, and why it is still under 2% of the fixed-income universe;
- lay any manager's pitch book on a six-axis map (alpha families, data stack, portfolio construction, execution, capacity, risk) and find the cells it hides;
- show that every "value" signal in the industry is a gap between a risk-neutral and a physical loss rate;
- compute effective breadth under issuer clustering, break-even turnover, and capacity under square-root impact, and explain why at the manager's preferred size the client keeps one-third of the edge;
- specify a seeded engine that scores any row of the map, and name the empty cells where an ex-RSSG brain is scarce.

## 4.1 The Five Businesses Called "Systematic Credit"

In restructuring you learn early that "the creditors" is not a party. A first-lien term lender, a second-lien noteholder, a trade creditor and a CDS protection buyer all hold a claim on the same company, and they want four different things. "Systematic credit" works the same way. The phrase covers at least five businesses that share a vocabulary (factors, optimizers, transaction-cost models) and almost nothing else that matters: not the benchmark, the leverage, the client, or the constraint that decides whether they make money.

Acadian, which built a systematic credit business between 2022 and 2024, put it bluntly in June 2026: the term has become an "ambiguous catch-all label." Acadian's own narrow definition is "fundamentally driven, benchmark-relative corporate bond strategies that apply purely quantitative methods" (Acadian, *Credit's Systematic Shift*, June 2026). That is one of the five businesses below. It is a good definition and a bad census.

| # | Business | Benchmark and leverage | What it sells | Binding constraint | Examples (sourced) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| (i) | Benchmark-relative long-only quant managers | IG or HY index; no leverage; tracking-error budget of roughly 1–3% *(illustrative)* | Information ratio after fees, and a solver for client constraints | Capacity and transaction costs | Blackstone Corporate Bond Strategies, "over \$40 billion" (`Blackstone_Systematic_Credit p.1`); Robeco multi-factor credits (fund launched 2015, Funds Society, 18 June 2015); Acadian US HY (live Nov 2023, Acadian news, 19 Aug 2024); Man systematic long-only credit, \$3.1bn at 30 Sept 2026 (Man Group trading statement) |
| (ii) | Long/short quant credit hedge funds and pods | Cash-plus (SOFR-plus); levered | Uncorrelated return | Financing, short availability, crowding | Man's long/short credit at 4–5x leverage (`Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.11`); pod names and sizes CHECK |
| (iii) | Quant multi-asset credit allocators | Blended or absolute; mild leverage | Sector allocation across HY, loans, EM, private credit | Breadth (a handful of sectors) | Nuveen's index-level framework (`Nuveen_Multi_Asset_Credit_Quant_Framework p.3–6`) |
| (iv) | Rules-based and smart-beta credit ETFs | Index; no leverage | A cheap, transparent factor tilt | Rebalance predictability | iShares IGEB and HYDB, launched July 2017; about \$1.43bn and \$1.52bn in assets in October 2026 *(approx.; aggregator data, CHECK)* |
| (v) | Algorithmic dealers and non-bank liquidity providers | None; inventory P&L | Liquidity | Adverse selection and balance sheet | Non-bank liquidity providers earned about 10% of US credit market-making revenue in 2024 (Coalition Greenwich, January 2025); see Chapters 18–19 |

Two things in this table should change how you read every pitch book that follows.

First, the five businesses face different binding constraints, so they optimize different things and will tell you different stories about the same factor. A long-only manager running against the ICE BofA High Yield Index does not care much about whether value works as a standalone long/short spread. It cares whether value tilts can be carried at a 2% tracking error without paying away the edge in bid–offer. A long/short fund at four times leverage does not care about a benchmark at all. It cares whether it can borrow the bond it wants to short, and whether the six other funds running the same value signal will try to sell at the same moment. Same factor, different businesses, different answers.

Second, the column on the far right is thin for a reason. The industry is young, much of it sits inside larger firms that do not split out systematic assets, and the multi-strategy pods disclose almost nothing. Where this chapter says CHECK it means it: we will not invent a pod's AUM to make the table look full.

A sixth group hangs over all five: the "quant-assisted" discretionary manager. Barclays QPS estimates that funds using quantitative *screening* in IG and HY hold between \$90bn and \$140bn (Mateer et al., Barclays QPS & Credit Research, 2024, cited by Impax, 19 September 2025). That is several times the dedicated systematic pool. Most of the industry's quant money is not running a model. It is running a model *past* an analyst. Keep that number in your pocket next to the USB stick. It is the strongest evidence in this chapter that an RSSG-trained analyst is not obsolete. They are the other half of the most common product.

> **Desk Myth vs. Desk Reality.** *Myth:* Systematic credit is equity quant with the tickers swapped for CUSIPs. *Reality:* An equity quant trades a stock that exists once, prints every few milliseconds, and can be shorted by calling the prime broker. A credit quant trades one of the seven bonds a single issuer has outstanding, three of which printed last week. Shorting any of them means borrowing it in repo, and that bond may be cheapest-to-deliver into a CDS auction or held by an ad hoc group that is about to sign a cooperation agreement. The signal library transfers. The plumbing does not.

## 4.2 Why Credit Lagged Equities by Twenty Years

Equity quant had its industrial revolution in the 1990s and its reckoning in August 2007. Credit quant spent most of that time as a research topic. The reason is not that bond people are slower. The reason is that the four inputs a systematic process needs arrived late in credit, and some still have not fully arrived.

> **[SOURCE EXTRACTION]** *Dynkin_Systematic_Investing_in_Credit p.44:* "the successful implementation of a scientific investment approach generally requires four primary inputs: rich and relevant data availability, high breadth of investable instruments, sophisticated markets enabling long and short positioning, and a growing body of research"
>
> **Annotation.** This is the Barclays QPS team's diagnosis, and it reads like a checklist of credit's handicaps. On a 2026 desk each input has a specific status. *Data*: TRACE began in July 2002 and was not fully disseminated until years later, so a clean bond-level history starts in the mid-2000s, and even that history needs the bias corrections in §4.5. *Breadth*: high in bond count, much lower in independent bets, as §4.3 derives. *Long and short*: still the weakest input, because single-name CDS liquidity concentrated in a small set of names after 2008 and shorting cash bonds runs through repo. *Research*: the factor literature arrived in a rush between about 2013 and 2018, and part of it failed replication between 2023 and 2026. The modern desk departs from the passage in one way: it treats *execution data* as a fifth input. Without a transaction-cost model you can trust, the other four only tell you what you would have earned in a market that does not exist.

Take the four inputs in turn, through an RSSG lens.

**Data.** A restructuring banker lives on data that is excellent and late: a 10-K, a compliance certificate, a 13-week cash flow forecast that is accurate to the dollar and three weeks stale. Equity quants live on data that is mediocre and instant. Credit quant needs both, and for twenty years it had neither at scale. Bond prices came from dealer runs and matrix pricing. Fundamentals came from the same filings equity analysts used, but the bond-level details that matter in credit — which entity issued it, what it is guaranteed by, where it sits in the waterfall — were in offering memoranda, not databases. The security master is still the least glamorous and most valuable system on a quant credit desk.

**Breadth.** There are many more bonds than stocks. Man counts over 10,000 US corporate bonds from about 2,000 issuers, against roughly 100 US single-name CDS that trade regularly (`Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.10–11`). That ratio is the industry's founding argument for cash bonds over synthetics. It also hides a trap, which we derive in §4.3: five bonds of one issuer are not five bets.

> **[SOURCE EXTRACTION]** *Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.11:* "we believe that cash bonds will be the approach of choice for most quantitative investors, above all because breadth is key for quant strategies and is simply not available in synthetic form yet."
>
> **Annotation.** Man's argument is the fundamental law of active management (Grinold) in one sentence: the information ratio scales with the square root of breadth, and CDS has about a hundred liquid names while cash has thousands. Two things changed between 2022 and 2026. Listed credit-index futures (CME and ICE launched products in 2024; Cboe IBIG and IBHY block trades topped \$1bn a month in July and August 2026, per exchange-reported data in The DESK, 16 October 2026, CHECK) give systematic books a cheap *beta* layer, so the cash book can be built purely for selection. But the single-name breadth problem in synthetics is no better. The modern desk departs from the passage in reading "breadth" as *effective* breadth, which is much smaller than bond count once you account for issuer clustering. That correction moves every capacity and IR estimate in this chapter.

**Long and short.** In equities you short a stock by borrowing it. In credit you short a bond by borrowing it in repo, if anyone will lend it at a rate that does not eat your edge, or by buying single-name CDS, which exists for about a hundred names that trade regularly. Ironically, the only market where shorting credit is truly easy is the one RSSG bankers dread: distressed names where the CDS is liquid because everyone is waiting for the auction. A long/short quant credit book is therefore usually a long book of cash bonds, hedged with index products, plus a short book that is smaller, more expensive and more crowded than the long. That asymmetry matters for D6 in §4.9. A long-only manager can't express a negative view beyond underweighting to zero, so "defense" has to come from what you avoid.

**Research.** The canonical factor papers in credit are recent. Jostova, Nikolova, Philipov and Stahel's "Momentum in Corporate Bond Returns" appeared in the *Review of Financial Studies* in 2013. Houweling and van Zundert's "Factor Investing in the Corporate Bond Market" appeared in the *Financial Analysts Journal* in 2017. Israel, Palhares and Richardson's "Common Factors in Corporate Bond Returns" appeared in the *Journal of Investment Management* in 2018. By the standards of equity factor research, which has the Fama–French three-factor model from 1993, credit had about a fifteen-year research lag. Then, as §4.5 shows, part of the new literature turned out to rest on contaminated TRACE data.

Add the four lags together and you get an industry that was technically possible by about 2015, commercially credible by about 2020, and is still tiny relative to its universe.

> **[SOURCE EXTRACTION]** *Blackstone_Systematic_Credit p.2:* "While systematic strategies manage roughly 20% of global equities, they account for less than 2% of the fixed-income universe."
>
> **Annotation.** This is the single most quoted ratio in the industry, and it has held for at least five years: Bloomberg reported the same 20%-versus-under-2% split for 2025 (BBH, *Introducing Systematic Fixed Income*, 2 March 2026). A ratio that holds while assets grow tells you the denominator grew too. The fixed-income universe expanded with post-2020 issuance, so systematic credit has been running to stand still in share terms. For a desk this cuts both ways. A low penetration rate means the classic factors are less arbitraged than in equities, the early-mover argument (`Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.9`). It also means the evidence base for those factors is mostly simulated, and allocators know it. The modern desk departs from the pitch-book reading of this ratio. "Room to grow" is a fact about the market. It is not a fact about your strategy's capacity, which §4.8 computes separately and which is usually much smaller.

> **Trend Watch: How big is systematic credit, 2018–2026?**
>
> - **2018.** Man Numeric launches its credit business in autumn 2018 under two co-heads: its own head of corporate bond research and a quant researcher who joined from Apollo (as reported by Hedgeweek, 10 October 2018). Systematic credit is mostly a research claim and a handful of products. BlackRock's IGEB and HYDB ETFs, launched July 2017, are among the few live rules-based vehicles.
> - **2020.** About \$116.5bn traded on MarketAxess Open Trading via quant funds in the first three quarters of 2020, a 150% increase (Business Insider, December 2020, cited in `Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.8`). Blackstone agrees to buy DCI, a quant credit manager with about \$7.5bn of assets (terms undisclosed), on 30 November 2020 (Institutional Investor, 30 November 2020).
> - **2021.** eVestment counts on the order of \$50bn of actively managed quant credit, more than double five years earlier, and BlueCove estimates quant credit at about 0.4% of a roughly \$66trn investable fixed-income universe against about 15% for quant equity (per press reports, IFR, c. early 2022; date unconfirmed).
> - **2023.** "Systematic credit funds doubled in size in 2023" (Bloomberg, 20 May 2024, via BBH, 2 March 2026).
> - **2024.** Barclays QPS sizes quant-*screened* IG and HY funds at \$90–140bn (via Impax, 19 September 2025). Invesco's Global Systematic Investing Study reports 88% of surveyed managers using systematic methods in fixed income, up from 73% in 2023 (via BBH). a co-head of Man Numeric's credit business describes systematic fixed income as "still in a very low single digits of market share" (Man Group *Long Story Short* podcast, March 2024).
> - **2025.** Systematic strategies are about 20% of global equities and under 2% of the investable fixed-income universe (Bloomberg, 2 February 2026, via BBH).
> - **2025–2026.** At Man Group, which reports the split quarterly, systematic long-only credit rises from \$2.0bn (March 2025) to \$3.1bn (September 2026), while discretionary long-only credit rises from \$19.8bn to \$37.5bn over the same quarters (Man Group trading statements, Q1 2026 and Q3 2026).
>
> **What it means for the desk.** The plumbing has scaled faster than the dedicated capital. The money that *did* arrive went mostly to hybrids (quant screens feeding analysts) and to large credit platforms that bought a systematic engine rather than built one (§4.10–4.11). If you are pitching a pure systematic credit book in 2026, your competitor for the allocation is not another quant. It is a discretionary manager with a quant screen and a three-year record.

> **Poker Table.** Ines draws the penetration ratio on a napkin. "Two percent of the table is playing with a heads-up display and the other ninety-eight are playing by feel. The question isn't whether the HUD wins. It's how long before the ninety-eight notice, and how much smaller the pot gets when they do." Early-mover alpha is real, and it is a depreciating asset. The pot shrinks two ways. Competitors arrive and trade the same signals, so the gross edge $\alpha_0$ falls. And your own success grows your book until impact eats what is left. That second effect has a closed form, (4.2) in §4.8, and it is the one managers talk about least.

## 4.3 The Six-Axis Framework Map

Theo's sheet of paper has six columns because every systematic credit process, from a ten-person team to a \$40bn platform, has to answer the same six engineering questions:

1. **Alpha families.** Where does the forecast come from?
2. **Data stack.** What are you allowed to know, and when did you know it?
3. **Portfolio construction.** How does a forecast become a position?
4. **Execution.** How do you get filled, and what does it cost?
5. **Capacity.** How big can the book grow before the book is the market?
6. **Risk.** What do you hedge, and what are you paid to hold?

Lay the industry's framework papers and public descriptions on those six axes and you get the map below. Read it as a desk reads a pitch book: the full cells say what the manager wants you to see, and the empty cells say what it would rather you did not ask about.

| Framework (source) | Alpha families | Data stack | Portfolio construction | Execution | Capacity | Risk |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Man 2022**, *Quantitative Credit: Alpha Opportunities for Early Movers* | Value, momentum, quality, informed investor, combined into a "final" signal (p.24–28) | TRACE plus security master; equity data; alt data such as supply-chain links, bond short interest, text-mined analyst notes (p.31–32) | Three layers (guard rails, autopilot, GPS); DTS-adjusted statistical factor risk model; headroom for alpha uncertainty (p.15–18) | TC = inside spread + slippage + calibration of dealer quotes (p.21) | Qualitative; warns of negative selection into illiquid bonds (p.8) | Long-only, and long/short at 4–5x (p.11) |
| **Man 2023**, *The Revolutions in Credit Trading* | Unchanged | Venue and RFQ analytics | Unchanged | Over 90% electronic; RFQ routing on availability, participant quality, completion rate, size (p.3–5) | Execution as the capacity lever | 2022 portfolio-trading cost spike as a risk event (p.3) |
| **Blackstone BCBS** (`Blackstone_Systematic_Credit p.1–2`) | Structural-model value, carry, contrarian rebalancing | Structural default model; private-company database covering about 85% of private leveraged-loan issuers (Institutional Investor, 5 May 2021) | Optimizer aware of insurer (Solvency II) constraints | Cash plus TRS and CDS | "Over \$40 billion," the largest disclosed | Rebalancing as policy |
| **BlackRock systematic HY** (`BlackRock_Systematic_High_Yield_Credit p.3–6`) | Default avoidance via a PD model; default-adjusted spread (the IGEB/HYDB rules use PD, default-adjusted spread and volatility) | PD model on fundamentals and market data | Benchmark-relative | Silent | Silent (CHECK) | "Defense without beta," argued from capture ratios |
| **Nuveen MAC** (`Nuveen_Multi_Asset_Credit_Quant_Framework p.3–6`) | Forward-return identity per sector | Index yields, default and recovery forecasts | Index-level optimizer, recency-weighted covariance, sector bounds | Not modeled; left to PM judgment (p.3) | Very large; breadth tiny | Sector covariance |
| **Robeco multi-factor credits** (Houweling & van Zundert 2017; Funds Society, 18 June 2015) | Low-risk, value, momentum (size in the research) | Bond and equity data | 150–200 names; IG with up to 10% BB | Silent | Silent (CHECK) | Low-risk tilt |
| **Acadian** (Institutional Investor, 1 June 2023; Acadian news, 19 August 2024) | "Components," not factors: default rates, value, credit deterioration, rating migration | Reuses its equity data infrastructure; over 20,000 securities | Benchmark-relative | Silent | Silent (CHECK) | Not disclosed |
| **Barclays QPS** (`Dynkin_Systematic_Investing_in_Credit`) | Value, momentum, equity-to-credit momentum, fallen angels; no size premium (p.516, p.628) | LCS liquidity scores since 2009, over 20,000 securities, bond-level history from January 2007 (p.702) | DTS as the risk unit; turnover buffers and budgets (p.724) | LCS-based cost estimates (p.702, p.711) | Explicit method: hold at most 5% of an issuer's market value (p.207–208) | DTS-based |

Look at the columns, not the rows. The alpha column is crowded and repetitive: value, momentum, quality or low risk, carry, with one or two house specials. That is Mags's "one memo." The execution and capacity columns are mostly "silent." Only Man 2023 and Barclays treat them as first-class, and only Barclays gives a capacity *method* you could audit. This is the chapter's first aha for an RSSG reader. The quant shops compete less on math, which is published, than on plumbing: a cost model that is right about dealer fade, a security master that survives an LMT exchange, a router that can fill \$2mm clips in 400 names on a Tuesday. The math is the menu. The plumbing is the kitchen.

To score a row you need numbers, and the first number every pitch book gets wrong is breadth.

### Scoring the breadth column: the fundamental law with issuer clustering

Grinold's fundamental law of active management says that an information ratio is skill times the square root of the number of independent bets, scaled by how much of the forecast survives into the portfolio:

$$
IR = IC \cdot \sqrt{BR} \cdot TC,
$$

where $IC$ is the information coefficient (the correlation between forecast and realized residual return), $BR$ is breadth (independent bets per year), and $TC$ is the transfer coefficient (the correlation between the ideal and the actual active weights). The word doing the work is *independent*. Equity quants can mostly pretend that 3,000 stocks are 3,000 bets after removing factors. Credit cannot, because bonds come in families.

Suppose the universe has $N$ bonds issued by $M$ issuers, $m = N/M$ bonds per issuer, and the residual returns $\epsilon_i$ (after stripping rates, spread beta and factors, i.e. the IDO component) have unit variance, correlation $\rho$ between two bonds of the same issuer, and zero correlation across issuers. Take the equal-weighted average of all $N$ bets. Its variance is the sum of $N$ variances plus all the within-issuer covariances. Each issuer contributes $m(m-1)$ ordered pairs, each with covariance $\rho$, and there are $M$ issuers, so the covariance total is $Mm(m-1)\rho = N(m-1)\rho$:

$$
\operatorname{Var}\!\left(\frac{1}{N}\sum_{i=1}^{N} \epsilon_i\right) = \frac{1}{N^2}\Big[N + N(m-1)\rho\Big] = \frac{1+(m-1)\rho}{N}.
$$

A set of $N_e$ truly independent unit-variance bets averages to variance $1/N_e$. Matching the two gives the effective breadth:

$$
BR_{\text{eff}} = \frac{N}{1+(m-1)\rho}, \qquad IR = IC\,\sqrt{BR_{\text{eff}}}\;TC. \tag{4.1}
$$

Check the boundaries. If $\rho = 0$, bonds of the same issuer are independent and $BR_{\text{eff}} = N$. If $\rho = 1$, every bond of an issuer moves together and $BR_{\text{eff}} = N/m = M$: forty-seven bonds of one issuer are one bet with forty-seven CUSIPs. The formula is the design-effect correction from survey sampling, and it is the first thing ROBO gets wrong (see the spec box in §4.8).

A worked example *(illustrative)*. A US HY universe of $N = 1{,}800$ bonds from $M = 800$ issuers has $m = 2.25$. With within-issuer residual correlation $\rho = 0.7$, $BR_{\text{eff}} = 1{,}800/(1 + 1.25 \times 0.7) = 960$. With $IC = 0.03$ and $TC = 0.5$, the naive IR from bond count is $0.03 \times \sqrt{1{,}800} \times 0.5 = 0.64$. The honest one is $0.03 \times \sqrt{960} \times 0.5 = 0.46$. The difference is about 28% of the headline IR, and it comes from nothing but a family tree.

Three places this goes wrong in practice, each a line in the spec:

- **Using bond count as breadth.** Every capacity slide that says "a universe of 10,000 bonds" is quoting $N$, not $BR_{\text{eff}}$. Estimate $\rho$ from residual returns within issuer, and report both numbers.
- **Assuming $TC$ survives execution.** The transfer coefficient is computed on the portfolio you *hold*, not the one you *wanted*. In credit, where an RFQ can come back with no responses, fill probability below one lowers $TC$ directly. Man warns that an unfilled order leaves "unintended and potentially unmodelled risk exposures" (`Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.19`). A strategy with $IC = 0.03$ and a 60% fill rate on its most informative trades is not a $TC = 0.5$ strategy.
- **Assuming $IC$ is constant across breadth.** Adding the 1,801st bond usually adds a bond you know less about. Paleologo warns that skill is not uniform across the universe, so $IC$ falls as you widen it.

> **[SOURCE EXTRACTION]** *Paleologo_Advanced_Portfolio_Management p.149:* "The power of diversification is great. It is not a skill: it is a skill multiplier."
>
> **Annotation.** Paleologo writes for equity long/short pods, and his binomial version of the law, $IR = (2p-1)\sqrt{252\,N_e}$ with hit rate $p$ and $N_e = 1/\sum_i w_i^2$, is (4.1) dressed for daily bets. The sentence is the right mental model for credit with one amendment: in credit the multiplier is the *effective* number of bets, and issuer clustering shrinks it. Multiply zero skill by a large breadth and you get zero; multiply real skill by a breadth you overstated and you get a sizing error, because you will lever the book to a target volatility that assumed diversification you do not have. Where the modern credit desk departs from the equity version is the unit of the bet. It is the *issuer*, with bonds as noisy, partly redundant expressions of the same view, and the choice of which bond expresses the view is itself a decision (see "negative selection," §4.11).

## 4.4 Alpha Families: What Each Shop Thinks It Is Harvesting

The alpha column of the map reads like a restaurant chain's menu: the same dishes everywhere, renamed by each franchise. Here they are, with what each one actually harvests, because the frameworks disagree less about *which* signals to use than about *what those signals are paid for*.

Start with the signal everyone calls "value," because it organizes the rest of the chapter.

### Value is the gap between Q and P

The credit triangle says that a spread compensates for expected loss under the pricing measure. For a bond with risk-neutral default intensity $\lambda^{\mathbb{Q}}_i$ and loss given default $L_i = 1 - R_i$,

$$
s_i \approx \lambda^{\mathbb{Q}}_i L_i .
$$

A systematic manager builds its own estimate of default risk under the *physical* measure $\mathbb{P}$, from a structural model (Blackstone/DCI), a PD model (BlackRock), or rating-agency history. Call it $\lambda^{\mathbb{P}}_i$. The "default-adjusted spread" is what is left of the spread after paying for the losses you actually expect:

$$
V_i = s_i - \lambda^{\mathbb{P}}_i L_i \approx \big(\lambda^{\mathbb{Q}}_i - \lambda^{\mathbb{P}}_i\big) L_i = \underbrace{\text{risk premium}_i}_{\text{paid for bearing default risk}} + \underbrace{\text{liquidity}_i}_{\text{paid for immediacy}} + \underbrace{\text{mispricing}_i}_{\text{what you hope is there}} . \tag{4.5}
$$

That identity is the second aha of the chapter. **Every value signal in the industry is a Q-minus-P gap.** DCI's structural-model comparison, BlackRock's default-adjusted spread, Man's spread-to-leverage ratio and Barclays' spread-versus-peers are all estimates of (4.5) with different models for $\lambda^{\mathbb{P}}$ and different peer sets. The frameworks differ in which of the three pieces on the right they think they are harvesting. A manager who says it harvests *risk premium* is selling carry with a seatbelt, and should expect to lose money in a spread-widening crisis, because that is what a risk premium is paid for. A manager who says it harvests *mispricing* is claiming a better $\lambda^{\mathbb{P}}$ than the market's, and should be able to show it in default avoidance (§4.9). A manager who harvests *liquidity* is a part-time market maker and should be judged on the execution axis. Chapters 5–6 build $\lambda^{\mathbb{P}}$ and $\lambda^{\mathbb{Q}}$ properly. Chapter 9 turns (4.5) into a production signal.

A worked example *(illustrative)*. Bond A is a single-B issuer at $s = 380$bp with $\lambda^{\mathbb{P}} = 2.5\%$ a year and $L = 0.6$, so expected loss is 150bp and $V_A = 230$bp. Bond B is a BB issuer at $s = 210$bp with $\lambda^{\mathbb{P}} = 0.5\%$ and $L = 0.6$, so $V_B = 180$bp. On raw spread, A is 170bp cheaper. On default-adjusted spread, it is 50bp cheaper. After the next step, which compares each bond with its rating and sector peers, A might not be cheap at all.

That next step is cross-sectional neutralization. Man describes a three-step pipeline: raw value, then risk-adjusted, then peer-relative (`Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.24`). Regress the risk-adjusted score on a vector of exposures $\mathbf{x}_i$ (rating, sector, spread duration, size) and keep the residual:

$$
\tilde V_i = V_i - \hat{\boldsymbol{\beta}}^{\top}\mathbf{x}_i, \qquad \hat{\boldsymbol{\beta}} = \arg\min_{\boldsymbol\beta} \sum_i w_i \big(V_i - \boldsymbol\beta^{\top}\mathbf{x}_i\big)^2 .
$$

Neutralization is what turns "high yield is cheaper than investment grade" (a beta bet you could make with an ETF) into "this B2 retailer is cheap relative to other B2 retailers" (an IDO bet). IDO or it didn't happen.

Now the edge cases, because a value score is a ratio and ratios have denominators. Man's raw value measure takes the form $\text{OAS}_i / \max(\text{NetDebt}_i/\text{EBITDA}_i,\ 0.1)$ (`p.24`). The clip exists to stop division by zero. Consider what it does to three companies *(illustrative)*:

- a BB issuer at 4.0x leverage and 250bp scores $250/4 = 62.5$;
- a net-cash IG issuer at 90bp has negative net debt, so its leverage is clipped to 0.1 and it scores $900$;
- a CCC issuer with EBITDA of $-\$20$mm, net debt of \$600mm and an OAS of 1,500bp has leverage of $-30$x, also clipped to 0.1, and scores $15{,}000$.

Congratulations: the model's favorite bond is the one with a restructuring adviser. Theo, who has *been* that adviser, recognizes the name. A single clip has merged three populations that have nothing in common: very low leverage, net cash, and negative EBITDA. The spec has to split them into separate branches, and the negative-EBITDA branch belongs to a distressed model, not a value screen. Two other traps belong in the same spec. A $\lambda^{\mathbb{P}}$ backed out of equity volatility without the Merton leverage mapping (Chapter 6) is a volatility, not a default rate. And a $V_i$ that is mostly risk premium will look like alpha until the first widening, when it behaves exactly like beta.

### The rest of the menu

**Momentum and the equity-to-credit lead–lag.** Credit momentum on its own is weak and mostly a high-yield phenomenon (Jostova et al. 2013 find it in HY but not IG). The strong version is *cross-asset*: equity returns lead bond spread changes, because the equity market prices news about firm value first and bond prices, which trade less often, catch up. In regression form,

$$
\Delta s_{i,t+1} = -\beta\, r^{E}_{i,\,t-k:t} + \epsilon_{i,t+1}, \qquad \beta > 0,
$$

so a stock that rallied predicts the bond's spread will tighten. Barclays reports equity-momentum-in-credit long–short excess returns of 6.34% a year in IG and 15.9% in HY over 1993–2017, *before costs*, with information ratios above 1.5 (`Dynkin_Systematic_Investing_in_Credit p.628`). That is a large number, and it is momentum, the family with the highest turnover (`Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.19`). The cost model will take much of it back, as §4.7 shows. Chapters 9–10 own the full derivation.

**Quality and low risk.** Robeco's Patrick Houweling has run a Conservative Credits strategy built on the low-risk anomaly since 2012 (Funds Society, 18 June 2015): short-maturity, highly rated bonds of low-risk issuers earn more per unit of risk than the market. It is the credit cousin of the equity low-volatility anomaly, and it is the factor least likely to embarrass you in a crisis and most likely to embarrass you in a rally.

**Carry.** Koijen, Moskowitz, Pedersen and Vrugt ("Carry," *Journal of Financial Economics*, 2018) show that carry predicts returns across asset classes, and Man cites Sharpe ratios of roughly 0.4–0.5 for carry strategies (`Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.26`). In credit, carry is spread plus roll-down, and it is the purest risk-premium harvest on the menu: the $\text{risk premium}_i$ term of (4.5) with no pretense of mispricing.

**Size.** The literature disagrees. Houweling and van Zundert (2017) find a size premium: bonds of smaller issuers outperform. Barclays finds none in its own tests (`Dynkin_Systematic_Investing_in_Credit p.516`). A desk should read the disagreement as a liquidity question in disguise. Small issuers' bonds are less liquid, so any size premium is partly a liquidity premium, and whether you can harvest it depends on your execution axis, not your alpha axis.

**Informed investor.** Man's fourth family uses positioning data such as equity short interest (`p.27–28`). It is the closest thing on the menu to Ines's question, "who at this table knows more than you?" It is also the weakest family in Man's own simulation.

**Components, not factors.** Acadian deliberately avoids the word "factor." Its inputs are default rates, value, credit deterioration and rating migration (Institutional Investor, 1 June 2023). The rename is not cosmetic. A "factor" invites you to harvest a premium; a "component" invites you to forecast an outcome. Acadian is telling you it thinks it harvests the mispricing term.

Here is what the families look like in one manager's simulation, with a caveat in bold because the chart's footnotes are where pitch books hide their bodies.

| Family (Man 2022, US IG and HY) | Simulated annualized IR of decile portfolios |
| :--- | :--- |
| Value | 2.15 |
| Momentum | 1.69 |
| Quality | 1.55 |
| Informed investor | 0.79 |
| Final combination | 2.35 |

*Source: `Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.28`.* **These are gross, simulated, decile-portfolio information ratios. They are not net of transaction costs, not capacity-adjusted, and not live.** Treat them as $IC\sqrt{BR}$ before $TC$ and before the cost model.

The table holds a small puzzle that teaches something. If four strategies with information ratios $\theta_k$ have return correlation matrix $C$, the best mean–variance combination has

$$
IR_{\text{combo}}^2 = \boldsymbol\theta^{\top} C^{-1} \boldsymbol\theta ,
$$

which for uncorrelated strategies is $\sum_k \theta_k^2$. With Man's four IRs, $\sqrt{2.15^2 + 1.69^2 + 1.55^2 + 0.79^2} = \sqrt{10.51} = 3.24$. The reported combination is 2.35. So either the families are substantially correlated, or the "final" signal is not weighted mean–variance optimally, or both. Under the simplest assumption, equal weights on four equal-volatility portfolios with a common pairwise correlation $c$, the combination's IR is $\sum_k \theta_k / \sqrt{4 + 12c}$. Setting that equal to 2.35 gives $\sqrt{4 + 12c} = 6.18/2.35 = 2.63$, so $c \approx 0.24$ *(our inference under stated assumptions, not Man's number)*. That is plausible for credit factors, which share a common exposure to the credit cycle. Henke, Kaufmann, Messow and Fang-Klingler (*Journal of Index Investing*, 2020) estimate pairwise credit factor correlations directly. The desk lesson is that diversification across *factors* is limited by the same thing that limits diversification across *bonds*: a common driver you cannot fully strip out.

Before you build the most sophisticated version of all this, note a survey Man cites. PGGM's survey of credit factor managers after the 2020 shock split them into "KISS" managers and sophisticated ones (`Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.30`). Keep It Simple, Stupid is a philosophy that has never once been applied to a credit agreement. It is, however, a good prior for a factor model fitted on fifteen years of sparse TRACE data, which brings us to the data stack.

## 4.5 The Data Stack and the Replication Crisis

Restructuring bankers have a sense of time that equity quants lack. A 10-Q for the quarter ending 30 June is not known on 30 June. It is known when EDGAR timestamps the filing, typically 40 to 45 days later. The compliance certificate arrives when the credit agreement says it arrives. The 13-week cash flow forecast is as of a Friday and wrong by the next one. Theo has spent a career asking "as of when?" It turns out to be the most valuable question in quantitative credit, and the one a large part of the academic literature forgot to ask.

Man's sketch of the data a quant credit process needs (`Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.31–32`) runs from TRACE and a security master, through equity data, to alternative data such as supply-chain linkages (Revere), bond short interest and text-mined analyst notes. Each layer has its own trap. TRACE public dissemination caps the reported size of large trades (an IG print over \$5mm shows as "5MM+", an HY print over \$1mm as "1MM+"), so a block happened but you are not told how big it was. The security master must map every CUSIP to its issuer, its guarantors and its place in the waterfall, and it must keep doing so after a drop-down moves the collateral. Equity data arrive fast and clean but describe a different claim. Alt data arrive with vendor load dates that have nothing to do with when anyone could have traded on them.

The discipline that ties them together fits in one line. Give every field $x$ an event time $t^{\text{ev}}(x)$ (the quarter end, the trade time) and a knowledge time $t^{\text{kn}}(x)$ (the EDGAR acceptance timestamp, the TRACE dissemination time, the vendor's load time). A signal used to trade at $t$ must be $\mathcal{F}_t$-measurable, which in database terms means

$$
s_{i,t} = f\Big(\{\,x : t^{\text{kn}}(x) \le t - \ell\,\}\Big),
$$

for a processing lag $\ell \ge 0$. There are two ways to break it. A *lead error* joins on event time when it should join on knowledge time. An *ex-post filter* drops observations because of returns realized after $t$. The second is subtler, so let us derive what it does.

Suppose a bond's monthly return $r$ has mean $\mu$ and standard deviation $\sigma$, and a "data-cleaning" rule deletes the worst fraction $q$ of next-month returns as presumed errors. For a normal distribution with lower quantile $z_q = \Phi^{-1}(q)$, the mean of what survives is

$$
\mathbb{E}\big[r \mid r > \mu + z_q\sigma\big] = \mu + \sigma\,\frac{\varphi(z_q)}{1-q},
$$

where $\varphi$ is the standard normal density. For $q = 1\%$, $z_q = -2.326$ and $\varphi(z_q) = 0.0267$, so the bias is $0.027\sigma$. With a bond-level monthly volatility of 4% *(illustrative, HY)*, that is about 11bp a month, or 1.3% a year, of return created by deleting things. Credit returns are not normal. The left tail holds the defaults and distressed exchanges, so the true bias is larger. Nor is the bias symmetric across a factor. Trim the left tail of every bond and you help the leg with more left tail, which in a "downside risk" or "high-minus-low credit risk" factor is the long leg. The filter does not just add noise. It manufactures the premium.

### Case Study: The Day the Factor Zoo Got Audited (2019–2026)

In 2019 Bai, Bali and Wen published "Common risk factors in the cross-section of corporate bond returns" in the *Journal of Financial Economics*. It proposed a four-factor model for bonds, was cited more than four hundred times, and became a standard benchmark for quant credit research. Alexander Dickerson, Philippe Mueller and Cesare Robotti then tried to replicate it. They found that two of the factors had been built with a one-month lead error, one with a lag error, and that left-tail losses had been trimmed ex post (Warwick Business School, 9–10 September 2024). Their own paper, "Priced risk in corporate bonds" (*JFE* 150(2), 2023), concluded that beyond traded liquidity the proposed bond factors add nothing to the bond market factor. It won the Fama–DFA Prize. The *JFE* retracted the original paper, which Warwick described as the first retraction of its kind at the journal.

The audit then went wholesale. In April 2026, Dickerson, Robotti and Rossetti ("The Corporate Bond Factor Replication Crisis," arXiv:2604.07880) re-examined 108 bond signals in nine clusters. They report that "the majority of previously documented factors do not produce statistically significant bond CAPM alphas after correction" for TRACE price measurement error and asymmetric ex-post return filtering. Their Open Source Bond Asset Pricing project now publishes the corrected TRACE panel and the bias-corrected factors, so any desk can rerun its backtests on the cleaned data.

In equities a one-month timestamp error is a bug. In credit it was a four-factor model, four hundred citations, and a prize for the people who found it.

"So the factors knew next month's returns," Kaz says.

"At PJT, knowing next month's numbers took a wall-crossing and two lawyers," Theo says. "In a backtest it takes a join on the wrong date column."

**How a systematic desk reads it.** The episode is not a scandal about one paper. It is a measurement of how fragile credit factor evidence is when prints are sparse and stale. It also moves the competitive frontier. If the published factors mostly vanish after cleaning, a manager's edge cannot be the factor list. It has to be the cleaning, the costs and the implementation, which is the plumbing argument of §4.3 again. Three rules go into every spec in this book:

1. Every field carries $t^{\text{kn}}$, and every join is an as-of join on knowledge time, never on event time.
2. No filter may condition on returns realized after the portfolio-formation date. Price errors are flagged only with prints known at the decision time, and every factor is reported both before and after cleaning.
3. Every performance number is labeled gross or net, simulated or live. The table in §4.4 is gross and simulated, and it says so.

## 4.6 Portfolio Construction: Guard Rails, Autopilot, GPS

A recommendation becomes a plan of reorganization only after it survives the constraints: absolute priority, the voting thresholds, the cash actually in the account. Portfolio construction is the same step for a quant book. The alpha model says what you would like to own. The constraints decide what gets confirmed.

### The risk unit: DTS

Every framework on the map budgets risk in Duration Times Spread. Here is why. A bond's excess return from a spread move is, to first order, $r_i \approx -D^{\text{spr}}_i\,\Delta s_i$. If spread changes are proportional to spread levels, $\Delta s_i = s_i\,\delta_i$, where the relative change $\delta_i$ has a volatility $\sigma_\delta$ that is roughly common across bonds, then

$$
\sigma(r_i) \approx D^{\text{spr}}_i\,s_i\,\sigma_\delta = \text{DTS}_i\,\sigma_\delta ,
\qquad
\sigma\Big(\sum_i w_i r_i\Big) \approx \sigma_\delta \sum_i w_i\,\text{DTS}_i \quad \text{when the } \delta_i \text{ move together.}
$$

Systematic spread risk adds up in DTS, so DTS is the unit you budget in. Man's statistical factor risk model is DTS-adjusted (`Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.15`), and Barclays uses DTS as its risk unit throughout.

> **[SOURCE EXTRACTION]** *Ben_Dor_Quantitative_Credit_Portfolio_Management p.50:* "a portfolio with a weighted spread of 200 bps and spread duration of two years is equally risky as a portfolio with a spread of 100 bps and spread duration of four years."
>
> **Annotation.** The arithmetic is $200 \times 2 = 100 \times 4 = 400$ bp-years, and the claim behind it is the proportional-spread-change model above. For an RSSG reader it overturns an instinct. A short-dated B3 bond at 400bp *(illustrative)* feels riskier than a ten-year BBB at 150bp, but with spread durations of 2 and 7 its DTS is 800 against 1,050, so in a broad widening the BBB loses more. The modern desk departs from the passage at both ends of the spread distribution. At very tight spreads, moves are closer to parallel than proportional, so DTS understates the risk of the tightest bonds. At distressed levels, bonds stop trading on spread and start trading on price and expected recovery, so spread duration loses its meaning. That is one more reason the distressed cell of the map is empty (§4.11).

### Man's three layers, and the cost of changing your mind

Man describes its process in three layers (`Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.17`). The **guard rails** are hard and soft constraints on volatility, rating, sector and issuer exposure. The **autopilot** is an objective function that pushes the portfolio toward the efficient frontier while minimizing concentration risk, unintended factor exposures and transaction costs. The **GPS** is the ongoing process that refines the portfolio over time, keeping it diversified and limiting the sources of risk. In symbols, the autopilot solves something like

$$
\max_{\mathbf{w}\in\mathcal{C}} \;\; \hat{\boldsymbol\alpha}^{\top}\mathbf{w} \;-\; \frac{\gamma}{2}\,(\mathbf{w}-\mathbf{w}^{b})^{\top}\Sigma\,(\mathbf{w}-\mathbf{w}^{b}) \;-\; \sum_i c_i\,\lvert w_i - w^{0}_i\rvert ,
$$

where $\mathbf{w}^{b}$ is the benchmark, $\mathbf{w}^{0}$ the current holdings, $\Sigma$ a DTS-scaled factor covariance plus issuer-level specific risk, $c_i$ the one-way cost per unit traded, $\gamma$ the risk aversion, and $\mathcal{C}$ the guard rails.

The last term is where Man's "headroom" for alpha uncertainty lives: the objective "differentiate[s] whether the security is already held or not" (`p.17`). Take the simplest decision, swapping a held bond $j$ for a candidate $k$, with $\hat\alpha$ measured over the expected holding period. The swap pays in expectation only if $\hat\alpha_k - \hat\alpha_j > c_j + c_k$. But $\hat\alpha_k - \hat\alpha_j$ is an estimate with standard error $\sigma_\Delta$, so add a headroom of $z\,\sigma_\Delta$. If the true difference is zero, the probability that you trade anyway is

$$
\mathbb{P}\big(\hat\alpha_k - \hat\alpha_j > c_j + c_k + z\,\sigma_\Delta\big) = 1 - \Phi\!\left(\frac{c_j + c_k}{\sigma_\Delta} + z\right).
$$

With round-trip costs of 60bp and $\sigma_\Delta = 50$bp *(illustrative, HY)*, a desk with no headroom ($z = 0$) makes a pure-noise swap 11.5% of the time. With $z = 1$ that falls to 1.4%. Barclays reaches the same answer with rules rather than a formula: turnover buffers and turnover budgets (`Dynkin_Systematic_Investing_in_Credit p.724`). Either way, the cheapest trade in credit is the one you talk yourself out of.

### Nuveen's identity, or the 13-week model with a covariance matrix

The multi-asset allocator works one level up, at the sector index, and its forecast is an accounting identity.

> **[SOURCE EXTRACTION]** *Nuveen_Multi_Asset_Credit_Quant_Framework p.3:* "Forward return estimates = yield – estimated credit loss – ∆rates MTM – ∆spread MTM"
>
> **Annotation.** Nuveen defines yield as yield to worst where available, credit loss from default-rate forecasts and expected recoveries, and the two MTM terms from forecast rate and spread changes using sector duration and spread duration. Its worked example for US high yield (five-year forward, as at 19 November 2025, Bloomberg US Corporate High Yield Index) reads, in our reading of the figure, $6.97 - 2.55 - 0.37 - 0.49 = 3.56\%$. The components sum exactly. The modern desk departs from the identity in two places. Yield to worst already prices the issuer's call option, so a spread-MTM term that assumes bullet behavior double counts the optionality in callable HY. And the high yield index is not the same animal over time (51% BB at year-end 2024 against 37% in 2004, `p.4`), so a spread "mean" estimated over twenty years mixes two different indices.

Written with the book's notation, for sector $j$ over horizon $h$ years, annualized,

$$
\mathbb{E}^{\mathbb{P}}[R_j] \approx y_j \;-\; \underbrace{\lambda^{\mathbb{P}}_j L_j}_{\text{expected credit loss}} \;-\; \frac{D^{\text{mod}}_j\,\Delta y^{\text{TSY}} + D^{\text{spr}}_j\,\Delta s_j}{h},
\qquad
\Delta s_j = \big(1 - e^{-\kappa_j h}\big)(\bar s_j - s_j), \tag{4.4}
$$

where $\kappa_j$ is the speed at which spreads revert to their long-run level $\bar s_j$ (the expected path of an Ornstein–Uhlenbeck spread, so the forecast cannot overshoot the mean however long $h$ is). Note the measures. The yield is a market quantity. The loss rate must be *physical*. Plug in the risk-neutral loss rate backed out of the spread and every sector's forecast excess return becomes zero by construction, which is a correct answer to a question nobody asked.

Theo reads the identity twice and laughs. Yield in, losses out, mark-to-market on top: it is his 13-week model, with a five-year horizon and a covariance matrix. He puts the USB stick back in his pocket, slightly vindicated.

Nuveen then feeds these forecasts and a recency-weighted sector covariance into an index-level optimizer with sector bounds. Its best efficient portfolio has a forward Sharpe ratio of 0.40, at a 6.20% return and 6.29% volatility, with high yield constrained to 20–60% and direct lending to 0–35% (`p.5–6`). That implies a cash assumption near 3.7% (our arithmetic). Nuveen leaves execution to the portfolio managers' judgment, including liquidity and "scalability limits" (`p.3`). That is the right call for a sector allocator. It is also why row (iii) of §4.1 has huge capacity and almost no breadth: there are only a handful of sectors to be right about.

## 4.7 Execution: The Revolution That Made the Industry

A dealer run is a price the way a restaurant's menu is a meal. Man says it directly: runs "are not firm and actionable" (`Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.19`). A credit backtest priced off runs or composites is therefore a backtest of a market where every menu price is guaranteed, the kitchen never runs out, and the waiter does not notice that you only order the specials. Man breaks the realized cost of a trade into three pieces (`p.21`):

$$
\text{TC}_i = \tfrac12\big(P^{\text{ask}}_i - P^{\text{bid}}_i\big) + \text{slip}_i(\text{size}, \text{characteristics}) + \text{calib}_i(\text{dealer fade}),
$$

the inside half-spread, the slippage that grows with clip size and bond characteristics, and a calibration term for the gap between the quotes a model sees and the levels dealers actually honor. The third term is the one an equity quant forgets. It is the dealer reading your order flow, the hand history Ines keeps telling Theo about.

> **[SOURCE EXTRACTION]** *Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.19:* "We cannot overstate the importance of transaction cost and liquidity modelling for quant credit participants, particularly in a market where spreads are at such universally tight levels and where transaction costs can easily wipe out the potential profitability of a trade."
>
> **Annotation.** This sentence explains the silent cells in the execution column of the map. A shop that says nothing about costs either has no cost model or considers it its moat, and in credit the second is often true. The modern desk departs from the passage in one respect: costs are no longer a constant to estimate but a state variable to forecast. They rise in stress, when dealers pull balance sheet and the electronic liquidity layer thins, which is exactly when a contrarian systematic book wants to trade. Man also notes that the bid–ask estimates still used in many academic papers, Chen, Lesmond and Wei's 25bp for AAA and 180bp for CCC (2007), are stale (`p.20`). A 2026 cost model starts from the desk's own fills, not from a 2007 table.

### Break-even turnover

Let $T$ be one-way annual turnover: the fraction of the book sold, and replaced, each year. Every dollar of turnover is a sale and a purchase, so with average cost $\bar c$ per dollar traded the annual cost drag is $2T\bar c$, and

$$
\alpha_{\text{net}} = \alpha_{\text{gross}} - 2T\bar c \;\ge\; 0 \quad\Longleftrightarrow\quad T \;\le\; T_{\max} = \frac{\alpha_{\text{gross}}}{2\,\bar c}. \tag{4.6}
$$

Boundary checks: with free trading, $T_{\max} = \infty$, and with no edge, $T_{\max} = 0$. Barclays gives a realistic calibration. Its combined value and equity-momentum IG book earns 2.66% a year gross and 1.78% a year net of rebalancing costs over 2007–2019, so costs take 0.88% a year, about a third of the edge. Tracking error barely moves (`Dynkin_Systematic_Investing_in_Credit p.711`), so the information ratio falls in proportion, from $2.66/1.41 = 1.89$ to $1.78/1.41 = 1.26$. Costs were 1.15% a year in 2007–2012 and 0.64% in 2013–2019. The signals did not change between the two periods. The market got cheaper to trade.

Now apply (4.6) to the momentum family, which has the highest turnover on the menu (`Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.19`). A long-only HY momentum tilt with 4% gross alpha and $\bar c = 40$bp *(illustrative)* breaks even at $T_{\max} = 0.04/0.008 = 5$, or 500% one-way a year. A monthly-rebalanced signal with short holding periods can turn over more than that. This is how the 15.9% before-cost figure in §4.4 becomes a much smaller number, or a negative one, in a live book.

### Case Study: Man Numeric's Execution Migration, 2021–2023

The cleanest public record of a firm moving along the execution axis is Man's own. In its telling, 2021 was the year of portfolio trading: tier-one and tier-two dealers offered high fill rates and aggressive pricing on lists. In the first half of 2022, as quantitative tightening and volatility hit, portfolio-trading costs rose. Dealers pulled balance sheet, and the custom ETF creation baskets that had let them warehouse lists cheaply were no longer available. Electronic venues held up best (`Man_Revolutions_in_Credit_Trading_2023 p.2–5`).

> **[SOURCE EXTRACTION]** *Man_Revolutions_in_Credit_Trading_2023 p.3:* "We have therefore moved from having roughly 30% of our order flow in high yield and 60% in investment grade going through electronic venues, to over 90% of our order flow going through electronic-trading venues."
>
> **Annotation.** Note what did *not* change: the signals. Man's alpha families are the same in the 2023 paper as in the 2022 one. What changed was the router and the cost model, and that moved the firm further along the execution axis than any signal research could have. The routing analytics Man describes score each RFQ counterparty on availability, participant quality, completion rate and the size it can digest (`p.5`). That is a markout table with a business card attached. The modern desk departs from the passage on one point. A shift that was rational in the calm of 2023 must be stress-tested, because buy-side traders now report that platform and non-bank liquidity "help more in quiet markets" and that flow returns to the banks in stress (The DESK, 14–15 October 2026).

Ines reads the routing list and nods. "Availability, quality, completion, size. That's how you seat a poker table. Who shows up, who's good, who folds, and how big a pot they can stand. The difference is that the dealers are keeping the same notes on you."

> **Trend Watch: Protocol mix and platform share, 2021–2026.**
>
> - **2021.** US IG e-trading reaches 34% and HY 25% of volume (Coalition Greenwich, *U.S. corporate bond trading in 2024 by the numbers*, January 2025). Portfolio trading is the protocol of the year (`Man_Revolutions_in_Credit_Trading_2023 p.5`: "2021 was the year of portfolio trading; 2022 was the year of electronic trading").
> - **2021→2022.** In Greenwich data reproduced by Man, disclosed RFQ falls from about 48% to 42% of IG+HY electronic volume, while portfolio trading rises from 7% to 10% and streaming and click-to-engage from 7% to 9% (`Man_Revolutions_in_Credit_Trading_2023 p.4`; figure column order CHECK).
> - **May 2023.** Man Numeric routes over 90% of its credit order flow electronically (`p.3`).
> - **2024.** IG and HY e-trading reach 48% and 33%; average daily notional volume is \$46.2bn (+21%); non-bank liquidity providers earn about 10% of US credit market-making revenue; Tradeweb carries more than two-thirds of electronic portfolio trading (Coalition Greenwich, January 2025).
> - **2025.** US corporate bond trading averages over \$50bn a day for the first time (Coalition Greenwich, 27 January 2026). MarketAxess reports a record \$1.4bn of portfolio-trading ADV (+48%) and a 19% share of US credit portfolio trading (FY2025 results). In September 2025 MarketAxess, Tradeweb and Trumid each do roughly \$8.5–8.8bn of electronic credit ADV, a three-way tie at about 15% of TRACE each (The DESK, 8 October 2025).
> - **March 2026.** Combined US IG+HY TRACE ADV is \$70.2bn (+14.7% year on year); MarketAxess portfolio-trading ADV hits a record \$2.3bn; Trumid reaches a record \$10.3bn ADV (The DESK, 9 April 2026).
> - **July 2026.** ICE agrees to acquire MarketAxess for \$167 a share in cash, about \$6.0bn of equity value, with closing expected in the first half of 2027 (MarketAxess 8-K, Exhibit 99.1).
> - **October 2026.** Vanguard reports that automated low- and no-touch trading is about 70% of its fixed-income desk volume, up from about 40% (The DESK, 14 October 2026).
>
> **What it means for the desk.** The plumbing that made systematic credit possible is now built and is consolidating. Protocol choice is itself a cost decision, and portfolio trading, all-to-all RFQ and streaming each have a different fill model and a different stress behavior. Model the cost of each protocol as a function of market state, not as a constant, and assume that the cheapest protocol in a calm month is the first to disappear in a bad one.

## 4.8 Capacity: How Big Before You Are the Market

Alpha is a hot tub. The more people in it, the less it is about the water. Every pitch book has a capacity slide, and almost none has a capacity derivation. Here is one.

Let $\alpha_0$ be gross alpha per dollar per year, $T$ one-way annual turnover, $c_0$ the half-spread cost per dollar traded, and let market impact per dollar traded be $\eta\sqrt{2TA/\mathcal{L}}$. Here $A$ is AUM, $2TA$ is the dollar volume the strategy trades in a year, and $\mathcal{L}$ is the annual dollar liquidity available *in the names the signal actually selects*, so $2TA/\mathcal{L}$ is the participation rate and $\eta$ is the square-root impact coefficient. Net alpha and dollar alpha are

$$
\alpha(A) = \alpha_0 - 2T\Big[c_0 + \eta\sqrt{2TA/\mathcal{L}}\Big], \qquad \Pi(A) = A\,\alpha(A).
$$

Write $g \equiv \alpha_0 - 2Tc_0$ for the gross alpha left after the spread, which is what a very small book earns. Then $\Pi(A) = gA - 2T\eta\sqrt{2T/\mathcal{L}}\,A^{3/2}$. Setting $\Pi'(A) = g - 3T\eta\sqrt{2T/\mathcal{L}}\,A^{1/2} = 0$ gives

$$
A^{*} = \frac{\mathcal{L}\,g^{2}}{18\,T^{3}\eta^{2}}, \qquad \alpha(A^{*}) = \frac{g}{3}. \tag{4.2}
$$

The second result follows because impact at $A^{*}$ is $2T\eta\sqrt{2TA^{*}/\mathcal{L}} = 2T\eta \cdot g/(3T\eta) = 2g/3$. Three readings follow, and each is a question to ask a manager.

1. **The one-third rule.** At the size that maximizes total dollar alpha, the client keeps one-third of the spread-net edge. A manager paid a share of dollar alpha chooses $A^{*}$. A manager paid only on assets is happy to grow past it, all the way to where net alpha hits zero. That happens when impact equals $g$, at $A_0 = \tfrac94 A^{*}$. The client, who cares about net alpha per dollar, would prefer $A \to 0$. That principal–agent gap sits behind every "capacity" asterisk.
2. **The cube of turnover.** Holding $g$ fixed, capacity scales as $T^{-3}$: double the turnover and the book can be one-eighth the size. This is why the high-turnover momentum family is a small-capacity business even when its gross numbers are spectacular.
3. **The right $\mathcal{L}$.** Index ADV is the wrong denominator. Signals select the bonds that are cheap, which skews toward bonds that are cheap *because* they are hard to trade. Paleologo warns that liquidity can invalidate a sizing analysis (`Paleologo_Advanced_Portfolio_Management p.145`). In credit that is the default, not the exception.

A worked example *(illustrative)*. An HY long/short multi-factor book has $\alpha_0 = 150$bp, $T = 0.6$, $c_0 = 25$bp, $\eta = 0.02$ and $\mathcal{L} = \$20$bn a year. Then $g = 120$bp, $A^{*} = 20{,}000 \times 0.012^2 / (18 \times 0.216 \times 0.0004) \approx \$1.85$bn, net alpha at $A^{*}$ is 40bp, and net alpha reaches zero at about \$4.2bn. Give the same universe an equity-momentum signal with $\alpha_0 = 4\%$ and $T = 2.5$ and $g = 2.75\%$, more than twice as much, yet $A^{*}$ falls to about \$134mm. The hot tub got hotter and much smaller.

Barclays offers a discrete method you can audit, which is rarer than it should be.

> **[SOURCE EXTRACTION]** *Dynkin_Systematic_Investing_in_Credit p.207:* "we assume that the dollar holding in any issuer is no more than 5% of its market value while the sizes of the fallen angels' portfolios vary from \$125mn to \$2bn."
>
> **Annotation.** Write the rule as weights. With $n$ eligible issuers, an issuer limit $w_{\max}$ and a cap of $c$ times issuer market value $MV_i$,
>
> $$w_i = \min\!\Big(\tfrac{1}{n},\; w_{\max},\; \tfrac{c\,MV_i}{A}\Big), \qquad f_{\text{cash}}(A) = 1 - \sum_i w_i . \tag{4.3}$$
>
> The portfolio depends on $c/A$ alone, so a \$500mn book at a 5% cap is the same book as a \$250mn one at 2.5%. As $A$ grows, the book drifts from equal weights toward market-value weights and the uninvested fraction rises. Barclays finds a \$1bn three-month-reversal fallen-angel book only 53% invested in August 2004, against 98% for a buy-all version (`p.207–208`). The modern desk departs from the passage in one respect. The 5% cap is a holdings constraint, and (4.2) is a trading-cost constraint, and a real book hits both. The cap also binds hardest in exactly the issuers where an RSSG reader would want to be large: small, stressed and mispriced.

### Specification for AI Implementation

**What ROBO built from the vague version.** Spec: "maximize breadth." ROBO bought all 47 bonds of one issuer, reported $BR = 47$, and filed a note that diversification was excellent. Precise spec: breadth is $BR_{\text{eff}}$ from (4.1), with $\rho$ estimated from within-issuer residual returns, and both $N$ and $BR_{\text{eff}}$ are reported.

**Module:** `capacity_breadth_engine.py`, numpy only, seeded, four blocks that run in order. It scores any row of the §4.3 map.

- **Units.** Money in \$mm. Rates, alphas and costs are annual decimals (0.015 is 150bp). `turnover` is one-way. `cost0` is the half-spread per dollar traded. `eta` is impact per dollar traded at 100% participation. `liquidity` is annual dollar volume in the names the signal selects, not index ADV.
- **Shapes.** `mv: float64[n]` issuer market values; `aum_grid: float64[G]`; curve functions return dicts of arrays of length `G`.
- **Guards.** Raise if `n_bonds < n_issuers` or `rho` is outside $[0, 1]$; floor `liquidity` and `aum` at `1e-12`; take `sqrt(max(., 0))`; return $A^{*} = 0$ when $g \le 0$ (costs eat the edge at any size); combine caps with `np.minimum.reduce`; floor $f_{\text{cash}}$ at zero against rounding.
- **Sanity asserts.** (a) $\rho = 1$ gives $BR_{\text{eff}} = M$ and $\rho = 0$ gives $N$. (b) The numeric argmax of $\Pi(A)$ is within 1% of (4.2), and $\alpha(A^{*}) = g/3$ to 1e-9. (c) $\alpha(A \to 0) \to g$. (d) Tiny AUM gives equal weights and no cash; huge AUM gives weights proportional to market value. (e) Weights depend only on $c/A$.

<!-- EXPLAIN: Listing 4.1 -->
> **Code Companion: Listing 4.1.** BR_eff = N / (1 + (m - 1) * rho), with m = N / M bonds per issuer. The full python listing is in [Appendix F, Listing 4.1](#code-4-1).

<!-- EXPLAIN: Listing 4.2 -->
> **Code Companion: Listing 4.2.** alpha(A) = alpha0 - 2T [c0 + eta * sqrt(2 T A / L)], with T one-way. The full python listing is in [Appendix F, Listing 4.2](#code-4-2).

<!-- EXPLAIN: Listing 4.3 -->
> **Code Companion: Listing 4.3.** w_i = min(1/n, w_max, cap_frac * MV_i / A); f_cash = 1 - sum(w). The full python listing is in [Appendix F, Listing 4.3](#code-4-3).

<!-- EXPLAIN: Listing 4.4 -->
> **Code Companion: Listing 4.4.** block 4 of 4: score rows of the six-axis map (all parameters illustrative, not the firms' numbers). The full python listing is in [Appendix F, Listing 4.4](#code-4-4).

Read the output by column, as you read the map. The IG long-only row has modest IR and a capacity in the tens of billions, which is why the largest pure-play shop on the map is an IG-heavy, insurer-facing platform (§4.10). The momentum row has the best gross IR and the smallest $A^{*}$. The allocator has almost unlimited capacity and a breadth of eight. No row wins on every column. That is the point: the six axes trade off against each other, and a pitch book that claims to win on all of them is hiding a cell.

## 4.9 Risk: Defense Without Beta

Every HY manager claims to be defensive. BlackRock's systematic HY note checks the claim with capture ratios. Define upside and downside capture over months $t$ in which the market return $r_{m,t}$ is positive or negative:

$$
UC = \frac{\sum_{t:\,r_{m,t}>0} r_{p,t}}{\sum_{t:\,r_{m,t}>0} r_{m,t}}, \qquad DC = \frac{\sum_{t:\,r_{m,t}<0} r_{p,t}}{\sum_{t:\,r_{m,t}<0} r_{m,t}} .
$$

Let the manager earn $r_{p,t} = a + \beta r_{m,t}$, where $a$ is selection alpha per month. With $n_u$ up months averaging $\bar u > 0$ and $n_d$ down months averaging $-\bar d < 0$,

$$
UC = \beta + \frac{a}{\bar u}, \qquad DC = \beta - \frac{a}{\bar d}, \qquad \mathbb{E}[r_p - r_m] = a + (\beta - 1)\,\mathbb{E}[r_m]. \tag{4.7}
$$

A pure beta tilt ($a = 0$) has $UC = DC = \beta$. It looks defensive in every down month and loses $(1-\beta)\mathbb{E}[r_m]$ on average, because a positive credit premium means up months win the long run. Defense that survives the rebound has to come from $a$, which in HY mostly means not owning the defaulters.

> **[SOURCE EXTRACTION]** *BlackRock_Systematic_High_Yield_Credit p.3:* "the average manager tended to participate in 89.56% of down markets and 92.24% of up markets."
>
> **Annotation.** Feed the two numbers into (4.7). The paper's window (2005–2025) has 168 up months and 72 down months (`p.3–4`). Assume average up and down months of +1.3% and −1.9% *(illustrative)*. Subtracting the capture equations gives $a(1/\bar u + 1/\bar d) = 0.0268$, so $a \approx 2.1$bp a month and $\beta \approx 0.91$. The market averages about 0.34% a month on those assumptions, so the beta drag is about 3.2bp a month and the average manager nets roughly −1bp a month against the index. The modern desk reads the passage as BlackRock intends: the average active HY manager's "defense" is mostly a smaller long. A 0.9 beta is not defense. Strip it out and see what is left. IDO or it didn't happen.

The selection that is left, in BlackRock's telling, is default avoidance. Its PD model "has successfully identified 77% of the defaulted bonds in the ICE BofA High Yield Index within 24 months of its default since 2010" (`BlackRock_Systematic_High_Yield_Credit p.6`). Theo reads this the way he would read a lender's recovery analysis: 77% is a *recall*. A screen that flags every bond in the index has a recall of 100% and costs you the whole spread of the innocent. The number you need next is the flag rate, the share of non-defaulters excluded, because every innocent excluded is carry forgone. Ask for both before being impressed.

Blackstone adds a third idea that belongs on the risk axis, not the alpha axis: contrarian rebalancing (`Blackstone_Systematic_Credit p.1`). An optimizer with fixed risk targets mechanically adds spread risk after spreads gap wider and trims it after they tighten. That is a policy, not a forecast, and what it harvests is the liquidity term of (4.5): the premium for buying when forced sellers are selling. It is also a crowded trade, because every systematic book with a DTS budget wants to rebalance on the same day.

## 4.10 Case Study: From KMV to Blackstone Corporate Bond Strategies (1990s–2026)

The largest disclosed row on the map started as a default model.

> **[SOURCE EXTRACTION]** *Bohn_Stein_Active_Credit_Portfolio_Management p.123:* "In the early 1990s, Stephen Kealhofer, John Andrew ("Mac") McQuown, and Oldrich Vasicek extended this model framework and provided a practical implementation of it."
>
> **Annotation.** "This model framework" is Merton's: equity as a call on firm assets, default when assets fall below the debt. KMV turned it into a commercial expected default frequency, which is a $\lambda^{\mathbb{P}}$ in the language of (4.5), estimated from equity prices and balance sheets rather than from spreads. That makes the default model the natural engine of a *value* strategy: compare the market's $\lambda^{\mathbb{Q}}$ with your structural $\lambda^{\mathbb{P}}$ and buy the gap. The modern desk departs from the 1990s version in calibration, not concept. Chapter 6 maps equity volatility to asset volatility properly, and the private-company problem below is where the concept needed new data.

The timeline, with dates and sizes as reported:

- **Early 1990s.** Kealhofer, McQuown and Vasicek build KMV's commercial implementation. Moody's acquires KMV in 2002 (`Bohn_Stein_Active_Credit_Portfolio_Management p.123`).
- **2004.** Kealhofer and McQuown, with David Solo, found DCI to run systematic corporate credit portfolios (Institutional Investor, 30 November 2020).
- **30 November 2020.** Blackstone agrees to acquire DCI, which manages about \$7.5bn across IG, HY and EM corporate credit, long-only and long/short. Blackstone Credit then manages about \$135bn (Institutional Investor, 30 November 2020).
- **May 2021.** The rationale, as reported: scale liquid credit without proportionally more analysts, and apply the model to private issuers using a Blackstone database that covers about 85% of the private leveraged-loan issuer universe. Roughly 40% of the HY market consists of private companies (Institutional Investor, 5 May 2021).
- **Today.** Blackstone describes the business as "currently the largest pure-play quantitative credit operation in the world, with over \$40 billion in assets under management" (`Blackstone_Systematic_Credit p.1`; as-of date CHECK). Its parent segment, Blackstone Credit & Insurance, reports \$443.0bn of AUM at 31 December 2025 and lists systematic strategies within liquid corporate credit (Blackstone FY2025 10-K).
- **Coda, 2025–2026.** The template repeats. Ares agrees in late October 2025 to buy all of BlueCove, a systematic fixed-income manager founded in 2018 with about \$5.5bn of AUM and about 60 staff at 30 September 2025, and to rebrand it Ares Systematic Credit, citing insurance distribution (Alternative Credit Investor, 30 October 2025; The DESK). Completion is reported for early February 2026 (CHECK).

**How a systematic desk reads it.** Three things scaled DCI from \$7.5bn to over \$40bn, and none of them was a better factor. The first is the engine. A physical default model is what makes "default-adjusted spread" a measurable quantity rather than a slogan. The second is distribution. An insurance-heavy credit platform wants liquid, rating- and capital-aware corporate books, and an optimizer that respects Solvency II charges is a product an insurer will buy at size (`Blackstone_Systematic_Credit p.1–2`). In §4.8 terms, IG-heavy long-only books have the largest $A^{*}$ of any security-selection row, and that is where this platform sits. The third is data. If 40% of HY issuers are private, the moat is not TRACE, which everyone has. It is private financials and covenants, which almost nobody can feed to a model. An RSSG analyst has read more private-company credit agreements than most quant teams have parsed.

## 4.11 The Genealogy of Quant Credit and the Empty Cells

The industry's family tree is short and visible. KMV begat DCI, which Blackstone bought. Man Numeric's credit business launched in 2018 with a co-head from Apollo's quant research (Hedgeweek, 10 October 2018). Acadian hired a former AQR fixed-income co-head and BGI alumnus to build its systematic credit business, announced in July 2022 (Acadian news, 19 August 2024). One of the two authors of Robeco's factor paper is now listed with Cubist Systematic Strategies, Point72's quant arm (SSRN author listing). BlueCove became Ares Systematic Credit. The people move between asset managers, pods and platforms. The six axes move with them.

What does not move is the set of cells nobody fills. Start with the one Man names outright.

> **[SOURCE EXTRACTION]** *Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.42:* "Quant credit is yet to move into distressed debt – this is a high-touch asset class that requires a significant degree of human intervention, but further data capture and analysis around restructurings and recovery may make this possible."
>
> **Annotation.** This is the empty cell with a sign on it. The "further data capture" Man asks for is a docket, a cooperation agreement, a priming basket and a recovery waterfall turned into features, which is the program of Parts IV and VII of this book. Moyer makes the discretionary case: "As much as the quantitative approach of financial econometricians would suggest that investing is fundamentally a science, in distressed investing it is more of an art" (`Moyer_Distressed_Debt_Analysis p.275`). The modern desk departs from both by refusing the choice. It does not try to automate the art. It specifies the parts of the art that are repeatable, such as LMT exposure, fulcrum location and liquidity runway, so that the humans spend their time on the parts that are not.

Kaz reads "fulcrum security" in Theo's notes and starts drawing a lever arm.

"It's the class that gets the equity," Theo says.

"So it's a torque problem."

It is, in a sense. The fulcrum is where enterprise value runs out in the waterfall, and a model that does not know the waterfall cannot find it. No framework paper on the map has a feature for it.

The other empty cells, each handed to a later chapter:

- **LMT-aware signals.** None of the frameworks on the map lists covenant terms or liability-management exposure among its inputs. A bond's spread can be "cheap" because its holders are about to be primed. Chapter 13 builds the Priming Risk Score.
- **Loans and private credit.** These are data problems first. Blackstone's private-issuer database is the exception that proves the rule (Chapters 17 and 21).
- **Sovereign, quasi-sovereign and securitized credit.** On Man's March 2024 *Long Story Short* episode, its credit co-heads named these as the next areas for systematic methods. Man 2022's own forward list adds loans, converts, EM, LDI and capital-structure arbitrage (`p.41–42`).
- **Event-driven credit.** A fallen angel is a forced-seller event, not a factor exposure, and the trade is the index exit, not the downgrade (Chapters 9 and 14).

The last empty cell lives *inside* the full ones.

> **[SOURCE EXTRACTION]** *Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.8:* "there could be an element of negative selection in the construction of quant credit portfolios whereby the least liquid bonds of an issuer are referenced."
>
> **Annotation.** An issuer-level signal has to be expressed through one of the issuer's bonds, and an optimizer that ranks bonds on cheapness will tend to pick the cheapest one. In a capital structure the cheapest bond is often cheap for a reason: it is the least liquid, the most structurally subordinated, sitting at the entity that is about to lose its guarantee, or carrying the covenant package that permits the drop-down. This is cheapest-to-deliver into your own optimizer. The modern desk departs from the passage by treating bond choice within an issuer as a separate decision with its own model. That model is a capital-structure model, and building one is what RSSG analysts do for a living.

## 4.12 Desk Debrief

- **"Systematic credit" is five businesses with five binding constraints:** capacity and costs for long-only, financing and crowding for long/short, breadth for allocators, rebalance predictability for ETFs, and adverse selection for algorithmic dealers. Ask which constraint binds before you ask about factors.
- **The alpha column is one memo. The money is in the plumbing.** Every value signal is a Q-minus-P gap (4.5). Know whether you are harvesting risk premium, liquidity or mispricing, because each one loses money in a different crisis.
- **Bonds are not bets; issuers are.** $BR_{\text{eff}} = N/(1+(m-1)\rho)$. Forty-seven bonds of one issuer are one bet with forty-seven CUSIPs.
- **Costs decide.** Break-even turnover is $\alpha_{\text{gross}}/(2\bar c)$. Barclays' realistic IG book gave up a third of its edge to costs, and the momentum family gives up more.
- **At the manager's favorite size the client keeps a third.** Capacity scales with $\mathcal{L}g^2/T^3$, and net alpha is zero at $\tfrac94 A^{*}$. Ask which size the capacity slide is quoting.
- **A 0.9 beta is not defense.** It is a smaller long. A default screen's recall is half a number until you know its flag rate.
- **Much of the published factor zoo did not survive cleaning.** Pin every field to its knowledge time, ban ex-post filters, and label every number gross or net, simulated or live.
- **The empty cells are distressed, LMT-aware signals, loans and private credit, securitized, and bond choice within the issuer.** They are where an RSSG brain is scarce.

### The Spec You Hand the Robot

> Build `capacity_breadth_engine.py` (numpy only, seed 404, units \$mm and annual decimals, turnover one-way). (1) `effective_breadth(n_bonds, n_issuers, rho)` returns $N/(1+(m-1)\rho)$; raise on `n_bonds < n_issuers` or `rho` outside $[0,1]$; `fundamental_law_ir(ic, br_eff, tc)`. (2) `net_alpha(aum, alpha0, turnover, cost0, eta, liquidity)` returns $\alpha_0 - 2T[c_0 + \eta\sqrt{2TA/\mathcal{L}}]$, where `liquidity` is the annual volume of the *selected* names; `aum_star_closed_form` returns $\mathcal{L}g^2/(18T^3\eta^2)$, or 0 if $g \le 0$. (3) `dynkin_cap_weights(mv, aum, cap_frac=0.05, w_max=None)` returns $\min(1/n, w_{\max}, c\,MV_i/A)$ and the uninvested fraction, floored at zero. (4) `framework_score(name, row)` returns $BR_{\text{eff}}$, gross IR, net IR at the row's AUM (scaled by net over gross alpha, tracking error held fixed), $A^{*}$ and cash drag. Assert: $\rho=1 \Rightarrow BR_{\text{eff}}=M$; numeric argmax of $A\alpha(A)$ within 1% of $A^{*}$; $\alpha(A^{*}) = g/3$; $\alpha(\tfrac94A^{*}) = 0$; tiny AUM gives equal weights; weights depend only on $c/A$. Never report bond count as breadth. Never use index ADV as $\mathcal{L}$. Label every output illustrative unless its inputs are sourced.

### Exercises

1. **Effective breadth.** A universe has 2,400 bonds from 600 issuers with within-issuer residual correlation $\rho = 0.6$. Compute $BR_{\text{eff}}$. What IC gives an IR of 0.5 with $TC = 0.5$? *(Answer: $BR_{\text{eff}} = 2{,}400/2.8 \approx 857$; $IC \approx 0.034$.)*
2. **Kaz's Sharpe of 3.1.** Kaz's backtest earns 6.2% a year of gross alpha at 2% tracking error, with one-way turnover of 8 times a year and transaction costs "set to zero so they wouldn't bias the results." Find the average cost per dollar traded at which the IR falls to 0.5, and the cost at which it hits zero. Compare both with a realistic HY half-spread and state, in one sentence, what Kaz should tell Ines. *(Answer: about 32.5bp and 38.75bp.)*
3. **The fee-adjusted hot tub.** Using (4.2), add a management fee $f$ per dollar of AUM. Find the AUM at which the client's net alpha after fees is zero, and show that it is below $\tfrac94 A^{*}$ for any $f > 0$. Which size does a manager paid only on assets prefer, and why does the answer depend on whether flows chase performance?
4. **Split the clip.** Rewrite Man's raw value score $\text{OAS}_i/\max(\text{NetDebt}_i/\text{EBITDA}_i,\ 0.1)$ as a branching rule with separate branches for low positive leverage, net cash and negative EBITDA. Specify what the negative-EBITDA branch hands to the distressed model, and write one assert that would have caught the 15,000 score in §4.4.
5. **Capture-ratio forensics.** A manager reports 105% upside capture and 85% downside capture. With average up and down months of +1.3% and −1.9%, solve (4.7) for $a$ and $\beta$. Is this defense, beta, or a back-test with regime bins defined after the fact? Name the data you would need to tell.
6. **The 10-Q join.** A backtest joins quarterly fundamentals to bond returns on fiscal quarter end. Estimate the information lead in days for a typical non-accelerated filer, say which rule of §4.5 it breaks, and explain why the bias is larger for the deteriorating credits a value screen likes most.

### Deep-Dive Resource Graph

**Podcasts**

- Man Group, *Long Story Short*, "Extra Credit: Algorithmic Advantage – Systematic Investing in Credit," with Man Numeric's credit co-heads, recorded March 2024: https://www.man.com/maninstitute/extra-credit-algorithmic-advantage
- Bloomberg *Odd Lots*, "A Longstanding Fear About The Corporate Debt Market May Finally Be Coming True," with Chris White (Viable Markets), 23 March 2020 (title only).
- Bloomberg *Odd Lots*, "The Next Stage of the Credit Cycle with Oaktree's Poli," 19 September 2024 (title only).

**Practitioner Writing**

- Man Institute, *Quantitative Credit: Alpha Opportunities for Early Movers* (2022) and *The Revolutions in Credit Trading* (2023) (on the shelf; cite by page).
- Acadian, *Credit's Systematic Shift* (June 2026): https://www.acadian-asset.com/investment-insights/credit/credits-systematic-shift
- BBH Capital Partners, Jorge Aseff, *Introducing Systematic Fixed Income* (2 March 2026): https://www.bbh.com/us/en/insights/capital-partners-insights/introducing-systematic-fixed-income.html
- Impax, Ahmed Abdullah, *Quant meets credit* (19 September 2025): https://impaxam.com/insights-and-news/blog/quant-meets-credit-enhancing-fundamental-analysis-through-systematic-screening/
- Institutional Investor on the DCI deal (Whyte, 30 November 2020): https://www.institutionalinvestor.com/article/b1pgy3wmwtl8l6/Blackstone-Puts-a-Quantitative-Spin-on-Its-Credit-Business ; and its rationale (Segal, 5 May 2021): https://www.institutionalinvestor.com/article/b1rpwxsmz7rxl9/Why-Traditional-Bond-Managers-Should-Pay-Attention-to-This-Blackstone-Deal
- Institutional Investor on Acadian's build (McElhaney, 1 June 2023): https://www.institutionalinvestor.com/article/2bstrc8107qz1gcb7jdvk/corner-office/how-acadian-built-out-a-systematic-credit-strategy
- Warwick Business School on the replication and retraction (September 2024): https://www.wbs.ac.uk/news/research-bond-market-wins-fama-dfa-prize/ and https://www.wbs.ac.uk/news/flaw-data-corporate-bond-investors/
- The DESK platform tallies: https://www.fi-desk.com/trumids-us-electronic-credit-volume-in-sight-of-marketaxess-and-tradewebs/ (8 October 2025) and https://www.fi-desk.com/marketaxess-leads-in-record-march-electronic-credit-trading/ (9 April 2026)
- Coalition Greenwich, Kevin McPartland (19 May 2025): https://www.greenwich.com/market-structure-technology/all-all-trading-continues-shine-volatile-markets
- Bloomberg, "It's PhDs Against MBAs in Credit Investing as Quants Jump In" (20 May 2024) and "The race to bring quant strategies to corporate bond markets" (2 February 2026) (title only).

**Academic Papers**

- Houweling, P., and J. van Zundert (2017), "Factor Investing in the Corporate Bond Market," *Financial Analysts Journal* 73(2): https://rpc.cfainstitute.org/research/financial-analysts-journal/2017/factor-investing-in-the-corporate-bond-market
- Israel, R., D. Palhares and S. Richardson (2018), "Common Factors in Corporate Bond Returns," *Journal of Investment Management* 16(2): https://joim.com/article/common-factors-in-corporate-bond-returns/
- Dickerson, A., P. Mueller and C. Robotti (2023), "Priced risk in corporate bonds," *Journal of Financial Economics* 150(2): https://econpapers.repec.org/RePEc:eee:jfinec:v:150:y:2023:i:2:s0304405x23001393 ; replication data: https://data.mendeley.com/datasets/n66rp59tr7
- Dickerson, A., C. Robotti and G. Rossetti (2026), "The Corporate Bond Factor Replication Crisis," arXiv:2604.07880: https://arxiv.org/abs/2604.07880
- Kelly, B., D. Palhares and S. Pruitt (2023), "Modeling Corporate Bond Returns," *Journal of Finance* 78, DOI 10.1111/jofi.13233.
- Bai, J., T. G. Bali and Q. Wen (2019), "Common risk factors in the cross-section of corporate bond returns," *Journal of Financial Economics* (retracted), DOI 10.1016/j.jfineco.2018.08.002.
- Jostova, G., S. Nikolova, A. Philipov and C. Stahel (2013), "Momentum in Corporate Bond Returns," *Review of Financial Studies* 26(7).
- Koijen, R., T. Moskowitz, L. Pedersen and E. Vrugt (2018), "Carry," *Journal of Financial Economics* 127(2).
- Chen, L., D. Lesmond and J. Wei (2007), "Corporate Yield Spreads and Bond Liquidity," *Journal of Finance* 62(1).
- Ben Dor, A., L. Dynkin, J. Hyman, P. Houweling, E. van Leeuwen and O. Penninga (2007), "DTS (Duration Times Spread)," *Journal of Portfolio Management*.

**Data & Code**

- Open Source Bond Asset Pricing (corrected TRACE panel, bias-corrected factors): https://openbondassetpricing.com/
- FINRA (TRACE): https://www.finra.org
- SEC EDGAR (filings and knowledge-time stamps): https://www.sec.gov/edgar
- MarketAxess FY2025 results: https://investor.marketaxess.com/news/news-details/2026/MarketAxess-Reports-Fourth-Quarter-and-Full-Year-2025-Financial-Results/default.aspx
- MarketAxess 8-K on the ICE agreement (Exhibit 99.1): https://www.sec.gov/Archives/edgar/data/1278021/000119312526324933/d159148dex991.htm


<!-- STATUS: COMPLETE -->
