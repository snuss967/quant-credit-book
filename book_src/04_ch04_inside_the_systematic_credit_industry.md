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

