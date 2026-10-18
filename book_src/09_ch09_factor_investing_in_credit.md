# Chapter 9: Factor Investing in Corporate Credit

<!-- WRITER PLAN (sections appended in order as drafted; resume after the last complete "## 9.x" section):
9.0 Cold open; 9.1 What a credit factor is (TW: systematic credit's share); 9.2 DTS, the hidden beta;
9.3 Value; 9.4 Momentum; 9.5 Carry and low-risk; 9.6 Quality, size, informed investor;
9.7 Combining factors (Case Study: one telecom, four factors); 9.8 Construction under costs (TW: cost curve);
9.9 The replication debate; 9.10 Crowding, capacity, drawdowns (Case Study: March 2020; TW: the tight-spread regime);
9.11 Specification for AI Implementation (cumulative python); 9.12 Desk Debrief, Spec You Hand the Robot, Exercises;
Deep-Dive Resource Graph. -->

## 9.0 Cold Open: Sharpe 1.9, Beta 0.6

The backtest finished at 6:40 p.m., which on a systematic desk is the hour when good news is most suspicious.

"One point nine," Kaz said, turning the monitor toward Theo with both hands. "Value long–short, US investment grade and high yield, twenty years. Long the cheapest decile on spread per turn of leverage, short the richest decile. A hundred million long, a hundred million short. Sharpe ratio of 1.9." *(All numbers in this scene are illustrative.)*

Theo had built leveraged-buyout returns that made 1.9 look shy, so he knew what to ask. "What's in the long book?"

"Cheap bonds."

"Cheap why?"

Kaz took this as a philosophical question and did not answer it.

Ines Okafor walked past with a coffee, stopped, and read the screen the way she used to read a river card. "What's the pot, what are the odds, and who at this table knows more than you?" She tapped the long leg. "What's the beta?"

Kaz ran it. The strategy's regression on the credit index came back at 0.6.

"So for every hundred million you're long, you're carrying sixty million of index," Ines said. "Right now the answer to my third question is: the index."

Mags Dunleavy, half hidden behind a Bloomberg terminal older than some of the interns, did not look up. "You bought the wide bonds, shorted the tight bonds, and spreads ground tighter for most of twenty years. Congratulations. You built the index with extra steps and called it alpha."

"It's market-value neutral," Kaz said.

"It's dollar neutral," Ines said. "Risk isn't measured in dollars. A hundred million of a 200bp six-year bond and a hundred million of a 120bp six-year bond are not the same bet. When the market sneezes, one of them catches a much worse cold."

Theo took the USB stick out of his pocket, looked at it, and put it back. His 13-week cash flow model could not help him here, but he liked knowing where it was.

"So what's left," he asked, "after you take the spread risk out?"

That is the question this chapter answers. A credit factor is a rule for sorting bonds. It is worth something only if, once you remove the one thing every spread-adjacent sort secretly loads on, it still makes money after transaction costs that run five to twenty times larger than in equities, measured on prices that are partly rumor.

By the end of this chapter you will be able to:

- explain why duration times spread (DTS) *is* beta in credit, and build DTS-neutral long–short and DTS-matched long-only factor portfolios;
- define and construct the canonical credit factors (value, momentum, carry, low-risk, quality, size, and the "informed investor") the way Barclays, AQR, Robeco, and Man build them, and say where they disagree;
- combine factors using information ratios and a correlation matrix, and know when combining *loses* to the best single factor;
- put a transaction-cost budget at the center of construction (liquidity cost scores, turnover buffers, turnover caps) and compute a factor's break-even cost;
- read the 2019–2026 replication debate as a desk, and turn it into five rules for your own factor library;
- hand ROBO a specification that rebuilds all of this on a synthetic universe with sanity checks that fail loudly when the mathematics is wrong.

## 9.1 What a Factor Is in Credit, and Why It Is Not What It Is in Equities

In equities, a factor is a characteristic (book-to-market, past twelve-month return, profitability) that sorts stocks into portfolios whose return spread is persistent, explainable, and not just the market in disguise. The word means the same thing in credit. The difficulty is that three facts about corporate bonds make every step harder, and none of them has a clean equity analogue.

**Fact one: spread is both the signal and the risk.** A value sort in equities is not a beta sort; cheap stocks do not have mechanically higher market betas. In credit, every signal built from the spread (value, carry, "cheapness" of any kind) is mechanically a sort on how much spread risk a bond carries, because a wide bond moves more than a tight one for the same market shock. Section 9.2 makes this exact: under the empirical law that spread changes are proportional to spread levels, a bond's beta to the credit market is its DTS divided by the market's DTS. A dollar-neutral portfolio that is long wide bonds and short tight ones is therefore a long-beta portfolio in a hedge fund costume, as Kaz just found out.

**Fact two: costs are first-order, not a footnote.** An equity quant who ignores transaction costs gets a backtest that is too optimistic. A credit quant who ignores them gets a backtest that is the wrong sign. Barclays' top-decile equity-momentum-in-credit portfolio, which we meet in §9.4, made 6.34% a year over the index before costs, with an information ratio of 1.90, and lost money after them (Dynkin p.633). Factor investing in credit is a turnover-budgeting problem with a signal attached.

**Fact three: the data lie, and they lie asymmetrically.** A corporate bond trades a few times a week, if that. Its "price" on a given month-end is a composite of a stale print, a dealer run, and a pricing service's model. Measurement error in that price enters both the signal you sort on and the return you measure, and it is largest in exactly the small, illiquid, high-yield bonds where published factors claimed to find the most alpha. Chapter 7 told the story of how that error, plus some careless return filters, inflated an academic literature until a benchmark paper was retracted. Section 9.9 shows what it does to factor construction specifically.

For a reader coming from a restructuring seat, the good news is that the core judgment is one you already make. At PJT RSSG you decided whether *one* bond was cheap given its covenant package, its collateral, its guarantor coverage, and the sponsor's appetite for an uptier. A credit factor model makes the same judgment on ten thousand CUSIPs at once. The covenant read is replaced by three ratios (leverage, net debt to EBITDA, interest coverage), and "comparable situations" are replaced by a peer cell (rating × sector × maturity). The residual of that model, the spread the market is paying you that the fundamentals do not explain, is your old day job written as $\epsilon_i$. The rest of this chapter is about two things: when that residual is a reward for risk the market will eventually stop charging for, and when it is information you do not have (a springing lien, a guarantor gap, an unrestricted subsidiary with all the good assets in it). The second case is where an RSSG reader has an edge nobody else's regression contains. Hold that thought until §9.3 and Chapter 13.

Here is the factor menu, with the honest one-line verdict for each. We build all of them in this chapter.

| Factor | Canonical credit definition | What it is secretly loaded on | Status on a 2026 desk |
| :--- | :--- | :--- | :--- |
| Value | Spread versus fundamentals inside a peer cell (ESP, SPiDER, structural fair spread) | DTS: "cheap" usually means "wide" | Survives once DTS is controlled and prices are clean |
| Momentum | Issuer equity momentum (EMC); trailing bond excess return, which works mainly in high yield | Turnover; equity's information lead | Strong before costs; costs are the whole fight |
| Carry | Option-adjusted spread, plus roll-down if you insist | DTS, almost entirely | Not a separate factor once DTS is matched (§9.5) |
| Low-risk (defensive) | Short maturity, high rating, low leverage, high profitability | Duration, and the leverage needed to hold it | Survives; hungry for leverage when DTS-neutral |
| Quality | Profitability, coverage, default probability | Default risk, so mostly a high-yield effect | A high-yield factor and a near non-factor in investment grade |
| Size | Small issuers by debt outstanding | Illiquidity and price noise | Disputed; mostly a cost and data artifact (§9.6) |
| Informed investor | Equity short interest, options positioning, bond borrow | Equity-market information flow | Weak alone, useful in combination |

> **[SOURCE EXTRACTION]** *Paleologo_Advanced_Portfolio_Management p.27:* "To estimate 𝛼 as accurately as possible is the job of the fundamental investor. To estimate 𝛽, identify the correct benchmarks m, and the returns 𝜖 is the job of the quantitative risk manager."
>
> **Annotation.** Paleologo writes for equity long–short managers, but the division of labor he describes is the cleanest statement of why credit factor investing is hard. In equities you can let a risk model own $\beta$ and spend your life on $\alpha$, because the two are estimated from different information. In credit the same number, the spread, sits on both sides of the line. The spread level is the input to the "fundamental" judgment (is this bond cheap?) and also the main determinant of the bond's market beta (how much does it move?). If you hand the spread to the alpha model without first handing DTS to the risk model, the alpha model will happily rediscover beta and call it skill. The 2026 desk resolves this by order of operations, not by job title: the risk side defines DTS cells and a DTS-scaled covariance first, and the alpha side is allowed to rank bonds only *within* that structure. The RSSG reader, who has always been the $\alpha$ person, now also has to be the $\beta$ person, because nobody else on the desk knows that the widest bond in the cell is wide because of a drop-down basket the model cannot see.

> **Trend Watch.** *Systematic credit's share of the market, 2018–2026: small, growing, and suddenly institutional.*
>
> - **The penetration gap.** Blackstone's systematic credit paper puts it in one line: systematic strategies manage roughly 20% of global equities but "less than 2% of the fixed-income universe" (Blackstone p.2; the paper is undated on the page, so treat the figure as a recent snapshot rather than a time series).
> - **The "uncrowded space" claim, around 2020.** The Barclays team's book, written as electronic trading took hold, describes scientific credit investing as standing "where scientific equity investing stood at the turn of the century: in an uncrowded space and on the threshold of considerable secular growth" (Dynkin p.45). Its stated reasons are more fixed-income data, better price transparency, and "established quantitative insights from the equity markets" (Dynkin p.49–50).
> - **The size of the pool, 2024.** Barclays QPS and Credit Research (Mateer et al., 2024, *QPS & Credit Research: Better Together*), as cited by Impax on 19 September 2025, estimate between US\$90bn and US\$140bn of assets in funds using quantitative screening in investment grade and high yield, growing faster than fixed income overall.
> - **Conversions, not just launches.** State Street converted two US high-quality corporate strategies to a fully systematic process effective 31 December 2023 (SSGA SAFI Q3 2025 commentary, 25 November 2025).
> - **Live track records now exist.** Robeco QI Global Multi-Factor Credits (launched 15 June 2015) held EUR 1,039mm at 30 September 2026, with realized transaction costs of 0.20% a year (three-year average), per the fund page. Section 9.10 uses its attribution as the honest counterweight to every backtest in this chapter.
> - **The plumbing.** Man notes that prime brokers now provide daily borrow availability across the cash-bond universe, so the short leg of a long–short credit factor is a spreadsheet rather than a favor (Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.11).
>
> *What it means for the desk.* At under 2% penetration, credit factors are not yet arbitraged the way equity factors were by 2007. But the pool is already large enough for the crowding questions of §9.10 to be real, and the people running it are no longer small specialist shops. The window Dynkin called "uncrowded" is open, but it is closing.

## 9.2 DTS: The Beta You Did Not Know You Had

Every factor in this chapter is built on one identity. Get it wrong and every later table is contaminated by beta. Get it right and the cold open's 1.9 Sharpe ratio comes apart into its pieces: what was carry, what was beta, and what, if anything, was a signal.

### 9.2.1 From proportional spread changes to beta

Let $r^{xs}_{i,t+1}$ be the one-period excess return of bond $i$ over duration-matched Treasuries, $s_{i,t}$ its spread (decimal), $D^{\text{spr}}_{i,t}$ its spread duration (years), and $\Delta t$ the period length in years. To first order,

$$
r^{xs}_{i,t+1} \;\approx\; s_{i,t}\,\Delta t \;-\; D^{\text{spr}}_{i,t}\,\Delta s_{i,t+1} \;+\; \text{(convexity and default-jump terms)}.
$$

The first term is carry: what you earn if nothing moves. The second is the price effect of a spread change. Ben Dor and coauthors documented that spread changes are approximately *proportional* to spread levels: a 300bp bond widens about three times as much as a 100bp bond in the same market move. Write that law as

$$
\Delta s_{i,t+1} \;=\; s_{i,t}\,\eta_{i,t+1}, \qquad \eta_{i,t+1} \equiv \frac{\Delta s_{i,t+1}}{s_{i,t}},
$$

where $\eta$ is the *relative* spread change, a dimensionless number such as $+0.10$ for "spreads widened 10%." Substituting,

$$
r^{xs}_{i,t+1} \;\approx\; s_{i,t}\,\Delta t \;-\; \text{DTS}_{i,t}\,\eta_{i,t+1}, \qquad \text{DTS}_{i,t} \equiv D^{\text{spr}}_{i,t}\, s_{i,t}.
$$

If relative spread changes have roughly the same volatility $\sigma_\eta$ across bonds, then excess-return volatility is proportional to DTS:

$$
\sigma\!\left(r^{xs}_{i}\right) \;\approx\; \text{DTS}_{i}\,\sigma_\eta .
$$

Ben Dor's empirical version of this is a near-perfect line: excess-return volatility regressed on DTS across buckets of bonds fits with an $R^2$ of about 98%, with a slope of about 8.8% a month in that sample (Ben_Dor_Quantitative_Credit_Portfolio_Management p.51). The slope is $\sigma_\eta$: relative spreads moved about 9% a month.

Now decompose the relative move into a common part and an idiosyncratic part, $\eta_{i,t+1} = \eta_{m,t+1} + \tilde\eta_{i,t+1}$, with $\tilde\eta_i$ uncorrelated with $\eta_m$. The market's excess return, ignoring carry (which is nearly constant over a month), is $r^{xs}_{m} \approx -\text{DTS}_m\,\eta_m$, where $\text{DTS}_m$ is the market-value-weighted DTS of the index. The beta of bond $i$ to the credit market under $\mathbb{P}$ is then

$$
\beta_i \;=\; \frac{\operatorname{Cov}^{\mathbb{P}}\!\left(r^{xs}_i,\, r^{xs}_m\right)}{\operatorname{Var}^{\mathbb{P}}\!\left(r^{xs}_m\right)}
\;=\; \frac{\text{DTS}_i\,\text{DTS}_m\,\sigma^2_{\eta_m}}{\text{DTS}_m^2\,\sigma^2_{\eta_m}}
\;=\; \frac{\text{DTS}_i}{\text{DTS}_m}. \tag{9.1}
$$

Equation (9.1) is the most useful line in this chapter. Beta in credit is not something you estimate with a five-year regression and a prayer. To first order it is a ratio you can read off the screen at the start of the month.

### 9.2.2 Why a dollar-neutral spread sort is long beta

Take a long–short portfolio with \$1 in each leg, equal-weighted within legs. Its beta is the difference of the legs' betas:

$$
\beta_{LS} \;=\; \frac{\text{DTS}_L - \text{DTS}_S}{\text{DTS}_m}.
$$

Any sort correlated with spread puts wider bonds in the long leg, so $\text{DTS}_L > \text{DTS}_S$ and $\beta_{LS} > 0$. Here is Kaz's portfolio with illustrative numbers. The long leg averages a 2.0% spread and 6.0 years of spread duration, so $\text{DTS}_L = 12$ (years × percent). The short leg averages 1.2% and 6.0 years, so $\text{DTS}_S = 7.2$. The market sits at $\text{DTS}_m = 8$. Then

$$
\beta_{LS} = \frac{12 - 7.2}{8} = 0.6,
$$

exactly Ines's number. The portfolio's carry is $2.0\% - 1.2\% = 0.8\%$ a year. In a sample where credit excess returns were positive on average, that is 0.8% of carry plus 0.6 of the index's excess return, *before any signal has done anything*. Mags was right: Kaz built the index with extra steps.

### 9.2.3 DTS-neutral construction

The fix is to equalize *risk*, not dollars. Choose weights so that each leg contributes the same DTS:

$$
\sum_{i\in L} w_i\,\text{DTS}_{i,t} \;=\; \sum_{i\in S} |w_i|\,\text{DTS}_{i,t} \;=\; \text{DTS}^{\ast},
$$

using beginning-of-month DTS, and ideally imposing it within each rating × sector cell rather than across the whole book. Barclays scales both legs to a common target of 12, "the time average DTS of the credit index" (Dynkin p.739). In Kaz's example, keeping \$100mm long, the short leg becomes $100 \times 12/7.2 = \$166.7$mm. The beta is now zero by construction.

Look at what happens to the carry: $2.0\% \times 1 - 1.2\% \times 1.667 = 0.0\%$. When the two legs have the same duration, a DTS-neutral long–short has *exactly zero net carry*, because carry is $s$ and DTS is $D^{\text{spr}} s$, so matching DTS at equal duration matches spread. The cold open's Sharpe ratio was carry on borrowed beta. After DTS-matching, both are gone, and whatever is left is the signal. (In this illustration nothing is left, which is why Mags went back to her terminal.) The general version of this result, carry per unit of DTS equals $1/D^{\text{spr}}$, comes back in §9.5, where it turns the carry factor into the low-risk factor.

> **[SOURCE EXTRACTION]** *Ben_Dor_Quantitative_Credit_Portfolio_Management p.34:* "just as spread duration is the sensitivity to an absolute change in spread (e.g., spreads widen by 5 bps), DTS (D · s) is the sensitivity to a relative change in spread."
>
> **Annotation.** This is the sentence that turned a portfolio-management heuristic into a risk model. Spread duration answers "what if spreads widen 5bp?", a question nobody should ask in high yield, where a 5bp move is a rounding error on Monday and a fantasy on the Friday before a lender call. DTS answers "what if spreads widen 10%?", which is the question the market actually poses, because spreads move in proportion to themselves. Barclays QPS introduced the measure with Robeco in 2005 (Dynkin p.729, note 11). It is now standard in index analytics. For factor investing the consequence is structural: the natural unit of exposure is DTS, so the natural neutrality condition is DTS-neutrality, and the natural cells for comparing bonds are cells of similar DTS. Two caveats separate the 2026 desk from the 2005 paper. First, proportionality weakens near distress: a 2,500bp bond does not widen 10% when the market does, because its price is anchored to recovery rather than to spread. Above roughly 1,000bp the desk switches from DTS to price-based or recovery-based risk (Chapters 5 and 14). Second, DTS is a bond-level number, and an issuer's bonds can diverge wildly when a liability-management transaction splits the capital structure into winners and losers, so issuer-level DTS-neutrality is not bond-level DTS-neutrality.

> **[SOURCE EXTRACTION]** *Dynkin_Systematic_Investing_in_Credit p.741:* "In the case of ESP, adjusting for DTS reduces correlations with US Corporate Index excess returns from 34% to –6% in drawdown episodes and from 44% to –22% in other (benign) periods."
>
> **Annotation.** This is the cold open measured on real data. ESP is Barclays' value signal (§9.3). Built naively, with long and short legs that differ in DTS, its correlation with the credit index is +44% in benign markets, so nearly half its variance is beta. DTS-match the legs and the sign *flips* to −22%: the genuine value signal is mildly *defensive*, because cheap-to-fundamentals bonds that are not simply wider are, on average, being mispriced by forced or panicked sellers. The practical lesson is in the drawdown numbers, 34% falling to −6%: a naive value book loses money exactly when the desk can least afford it, and a DTS-matched one does not. The 2026 desk reports every factor in both forms, because the gap between them is a direct measure of how much of the factor was beta. When a vendor shows you a credit-value backtest without saying how it handled DTS, assume the worse version.

> **The Spec You Hand the Robot (what ROBO built from the vague version).** Theo's first specification said: "Neutralize spread exposure in both legs." ROBO, which never guesses, reduced each leg's DTS to zero by selling every corporate bond and buying two-year Treasuries. The book's spread exposure was perfectly neutral. So was its alpha. The precise version: "At the start of each month, using beginning-of-month OAS and OAS duration, scale each leg so that $\sum_{i \in \text{leg}} |w_i|\, D^{\text{spr}}_i s_i = 12$ (years × percent) within each rating × sector cell; if a cell has fewer than five bonds in a leg, pool it with the adjacent rating; never rescale with end-of-month DTS."

> **Ways This Blows Up.** (1) *Units.* DTS in years × percent and years × basis points differ by a factor of 100. A DTS cap of 5 in one convention is a cap of 500 in the other, and a junior analyst will eventually enter the wrong one into the optimizer. Name the units in the variable name. (2) *Timing.* Scaling legs with end-of-month DTS is look-ahead: in a selloff, spreads widen, DTS rises, and the "neutral" short leg grows retroactively. Use beginning-of-month DTS only. (3) *Callables.* Use option-adjusted duration on callable high yield; modified duration on a bond trading to a 2027 call overstates its DTS and under-hedges it. (4) *Distress.* Cap DTS-based scaling for spreads above about 1,000bp or treat those names separately; a DTS-neutral short leg of three CCC bonds is not neutral to anything except the bankruptcy court's calendar. (5) *Leverage.* DTS-neutral legs need not be dollar-equal. A DTS-neutral book that is long short-dated A-rated paper and short long-dated BBBs can be levered several times on the long leg, and leverage has its own cost and its own drawdown (§9.5).
