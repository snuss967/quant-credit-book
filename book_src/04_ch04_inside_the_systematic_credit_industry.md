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
> - **2018.** Man Numeric formally launches its credit business under two co-heads: its own head of corporate bond research and a quant researcher who joined from Apollo (Hedgeweek, 10 October 2018). Systematic credit is mostly a research claim and a handful of products. BlackRock's IGEB and HYDB ETFs, launched July 2017, are among the few live rules-based vehicles.
> - **2020.** About \$116.5bn traded on MarketAxess Open Trading via quant funds in the first three quarters of 2020, a 150% increase (Business Insider, December 2020, cited in `Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.8`). Blackstone agrees to buy DCI, about \$7.5bn, on 30 November 2020 (Institutional Investor, 30 November 2020).
> - **2021.** eVestment counts about \$52bn of actively managed quant credit, more than double five years earlier, and BlueCove estimates quant credit at about 0.4% of a roughly \$66trn investable fixed-income universe against about 15% for quant equity (IFR, c. early 2022; date CHECK).
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

