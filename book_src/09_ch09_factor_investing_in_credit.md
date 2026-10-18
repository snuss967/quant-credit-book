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

## 9.3 Value: ESP, SPiDER, and the Fair-Spread Family

Value is the factor an RSSG reader understands best and gets wrong most expensively. "This bond is cheap" is a statement about a spread *relative to something*. Every value model is a choice of the something.

### 9.3.1 Excess spread to peers (ESP)

Barclays' value measure is a monthly cross-sectional regression within peer groups. For a peer group $g$ (rating × sector × maturity bucket), estimate

$$
s_{i,t} \;=\; a_{g(i),t} \;+\; b_{1,t}\,\text{Lev}_{i,t} \;+\; b_{2,t}\,\Big(\frac{\text{ND}}{\text{EBITDA}}\Big)_{i,t} \;+\; b_{3,t}\,\text{ICov}_{i,t} \;+\; \epsilon_{i,t},
$$

where $a_{g,t}$ is a peer-group intercept, $\text{Lev}$ is financial leverage, $\text{ND}/\text{EBITDA}$ is net debt to EBITDA, and $\text{ICov}$ is interest coverage. (Dynkin p.693 names exactly these three ratios; financials, whose EBITDA is not meaningful, use long-term debt to long-term assets instead.) The fitted residual $\hat\epsilon_{i,t}$ is the spread the market pays you beyond what the bond's peers and fundamentals justify. Rank it across the index into deciles:

$$
\text{ESP}_{i,t} \;=\; \operatorname{decile}\big(\hat\epsilon_{i,t}\big)\in\{1,\dots,10\}, \qquad \text{high} = \text{cheap}.
$$

In Barclays' results, measured against the index, the richest decile returned −1.10% a year (information ratio −0.27) and the cheapest +3.29% a year (IR 0.53) (Dynkin p.528), and the long–short spread has an IR above 1.5 (Dynkin p.545). The same page adds the condition that matters for 2026: the outperformance is larger when the cross-sectional dispersion of ESP is high. Value needs something to be cheap *relative to*; §9.10 returns to what happens when the whole market is tight.

Two implementation choices deserve a sentence each. First, the regression in §9.11 uses the *logarithm* of OAS rather than its level. That is our choice, not Barclays'. It follows from §9.2: if spreads move proportionally, log spread is the scale on which a residual of 0.2 means "20% cheap" for both a 90bp bond and a 400bp bond. Second, the regression's slopes $b_{k,t}$ are common across cells while the intercepts vary by cell. Letting every cell have its own slopes sounds more flexible and is, in practice, a way to fit noise in cells with eleven bonds.

> **[SOURCE EXTRACTION]** *Dynkin_Systematic_Investing_in_Credit p.524:* "We identify relative value as the portion of excess spread over peers unexplained by fundamental factors and call this measure excess spread to peers (ESP)."
>
> **Annotation.** The sentence is short, and every phrase in it is a modeling decision. "Over peers" means the comparison is always within a cell, never across the whole market, which is the first defense against the DTS problem of §9.2: within a rating × sector × maturity cell, spreads and durations are similar, so a residual is not just a disguised spread level. "Unexplained by fundamental factors" means three balance-sheet ratios stand in for what an RSSG analyst would call the credit story, which is a heroic compression. What the residual contains on a 2026 desk is the reason the RSSG reader matters. Part of it is genuine mispricing: forced selling after a downgrade, index-exclusion flows, a new issue priced to clear. Part of it is information the three ratios cannot see: a collateral-stripping drop-down, a priming threat from a cooperating majority, or an incremental-debt basket the size of a small country. A pure-quant ESP book buys both kinds. A desk that adds a document-risk regressor (the Priming Risk Score of Chapter 13) buys only the first kind.

### 9.3.2 SPiDER and Man's spread per turn of leverage

Regression residuals are opaque and their coefficients wander. Barclays' model-free alternative, SPiDER, divides the spread by a long-run leverage multiple:

$$
\text{SPiDER}_{i,t} \;=\; \frac{s_{i,t}}{\text{Debt}_{i,t}\,/\,\overline{\text{EBITDA}}^{\,\text{LT}}_{i,t}},
$$

where $\overline{\text{EBITDA}}^{\,\text{LT}}$ is a long-term average EBITDA. It is spread per turn of leverage, which is how a leveraged-finance banker already prices a deal. Man's raw value signal is the same idea, written schematically as `OAS / (Net Debt/EBITDA).clip(lower=0.1)`, then risk-adjusted for size, default probability, and volatility and compared within rating and sector (Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.24).

Take the floor literally for a moment. An issuer with negative EBITDA has a *negative* net-debt-to-EBITDA ratio, which the floor converts to 0.1×, so its spread is divided by 0.1 and it becomes the cheapest bond in the universe. Man's later risk adjustment presumably catches this. Your implementation should not rely on "presumably." Before applying any floor, assign negative-EBITDA issuers a punitive multiple (the code in §9.11 uses 15×) or exclude them. The floor exists to stop division by a number near zero, not to promote companies that are losing money.

Dynkin p.553 lays out the menu. Regression fair spreads control many characteristics at once but overfit. Structural models are parameter-hungry and opaque. SPiDER is neither, and it aggregates cleanly across sectors and time.

> **[SOURCE EXTRACTION]** *Dynkin_Systematic_Investing_in_Credit p.553:* "While a regression is able to control for multiple risk characteristics at the same time, it is vulnerable to statistical problems, such as overfitting and instability in coefficients."
>
> **Annotation.** Every desk discovers this the second month it runs ESP live. The coefficient on interest coverage, positive last month, is negative this month because three energy names had a bad quarter and the cell has 23 bonds. The ranking barely moves, but the portfolio manager sees a "value model" whose logic has reversed, and asks a fair question. The 2026 answers are standard statistics, not new ideas. Shrink each month's slopes toward a trailing average or toward a pooled estimate (Chapter 8's shrinkage machinery). Pool any cell with fewer than about 15 bonds into a coarser one. Winsorize residuals at the 1st and 99th percentiles before ranking. And run SPiDER alongside ESP as a model-free control: when the two disagree violently on a name, a human should look at it, which is the "quantamental" loop of §9.6.

### 9.3.3 The structural fair spread, and the measure trap

The third family builds a fair spread from a structural model and calls the bond cheap when its market spread exceeds the fair one (Correia, Richardson, and Tuna, 2012, *Value Investing in Credit Markets*). The step that trips people up is the change of measure, so we do it carefully.

In the Merton model (Chapter 5), assets follow $dV_t = \mu V_t\,dt + \sigma_V V_t\,dW_t$ under $\mathbb{P}$, and default occurs at $T$ if $V_T < F$. The physical default probability is

$$
\text{PD}^{\mathbb{P}}_T \;=\; N\!\left(-\text{DD}^{\mathbb{P}}\right), \qquad
\text{DD}^{\mathbb{P}} \;=\; \frac{\ln(V_0/F) + (\mu - \tfrac12\sigma_V^2)\,T}{\sigma_V\sqrt{T}},
$$

where $N(\cdot)$ is the standard normal distribution function and DD is distance to default. Under $\mathbb{Q}$ the drift $\mu$ is replaced by $r$, so

$$
\text{DD}^{\mathbb{Q}} \;=\; \text{DD}^{\mathbb{P}} - \frac{\mu - r}{\sigma_V}\sqrt{T}
\quad\Longrightarrow\quad
\text{PD}^{\mathbb{Q}}_T \;=\; N\!\left(N^{-1}\!\big(\text{PD}^{\mathbb{P}}_T\big) + \theta\sqrt{T}\right),
\qquad \theta \equiv \frac{\mu - r}{\sigma_V}. \tag{9.2}
$$

Here $\theta$ is the asset Sharpe ratio; under the CAPM it equals $\rho_{V,m}$ times the market Sharpe ratio. (We call it $\theta$ rather than the $\lambda$ some papers use, because $\lambda$ is reserved in this book for default intensity.) With recovery of a fraction $R$ of face paid at maturity (the recovery-of-Treasury convention), the zero-coupon price is $e^{-rT}\big(1 - \text{PD}^{\mathbb{Q}}_T L\big)$ with $L = 1 - R$, and the fair spread is

$$
s^{\text{fair}}_i \;=\; -\frac{1}{T}\,\ln\!\left(1 - \text{PD}^{\mathbb{Q}}_T\,L\right), \qquad \text{value}_i = s_i - s^{\text{fair}}_i .
$$

A worked example, with illustrative inputs: five-year physical PD of 2%, $\theta = 0.25$, $L = 0.6$. Then $N^{-1}(0.02) = -2.054$, the shift is $0.25\sqrt5 = 0.559$, and $\text{PD}^{\mathbb{Q}}_5 = N(-1.495) = 6.75\%$. The fair spread is $-\tfrac15\ln(1 - 0.0405) = 83$bp. Skip the change of measure and you get $-\tfrac15\ln(1 - 0.012) = 24$bp.

That gap is the **measure trap**. A desk that uses physical default probabilities as if they were risk-neutral finds that every bond in the market is cheap by about 60bp, buys all of them, and has rediscovered the credit risk premium, which is to say the index. A cross-sectional *rank* survives a monotone mapping from $\mathbb{P}$ to $\mathbb{Q}$, but only within a cell where $T$ and $\theta$ are the same. Across maturities, or across issuers with different asset correlations to the market, the mapping is not common, and any comparison of *levels*, such as "spread per unit of expected loss," is simply wrong without it.

### 9.3.4 The residual is cheapness or it is information

Here is the most important practical fact about value in credit, and the one the RSSG reader is best placed to exploit.

Two weeks into his first ESP run, Theo asked why the regression had three ratios and no "weeks of liquidity." Kaz said, "Because nobody put it in the panel." Theo put it in the panel: the runway from his 13-week cash flow model, reborn as a column. It added nothing in single-A, where nobody runs out of cash. In B and CCC it shrank the cheap decile by a fifth, removing names whose spreads were wide because they were about to need a rescue financing. Those were not cheap bonds. They were bonds pricing an event the three ratios could not see. *(Illustrative.)*

> **[SOURCE EXTRACTION]** *Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.25:* "Value stands out as being particularly CUSIP-specific, that is to say that within the same capital structure, even after accounting for liquidity, subordination, duration, etc., mispricing can remain."
>
> **Annotation.** Man's observation is that value lives at the bond level, not only at the issuer level: two bonds of the same company, after controlling for the obvious differences, can be priced inconsistently. For a pure quant, that is a statement about breadth: more CUSIPs, more independent bets. For an RSSG reader it is an invitation, because the "etc." in that sentence is where the credit agreement lives. Within one capital structure, the 2029 notes and the 2031 notes may differ in guarantor coverage, in whether they sit at an entity that can be stripped by a drop-down, or in whether they are the obvious target of a non-pro-rata exchange. A residual that a pure-quant model calls "CUSIP-specific mispricing" is sometimes exactly that, and sometimes the market correctly pricing a document risk that the model cannot read. The 2026 desk resolves the ambiguity by adding document features as regressors (Chapter 13's Priming Risk Score; Chapter 25's covenant-capacity variables). Whatever value survives *that* regression is cheapness. Whatever it removes was information, and you are better off having known it before you bought.

> **Ways This Blows Up.** (1) *Point-in-time fundamentals.* Use fundamentals as they were available at the time, lagged at least three months after the fiscal period end, with no restatements; otherwise the regression knows the next quarter's EBITDA. (2) *OAS versus Z-spread.* On callable high yield, a Z-spread includes the option value, so a value model built on Z-spreads finds "cheapness" in every bond with a valuable call. (3) *Tiny cells.* A rating × sector × maturity cell with eight bonds produces residuals that are mostly estimation error; pool or shrink. (4) *Negative EBITDA.* See §9.3.2. (5) *The value trap is a default.* The cheapest decile is where the next defaults are. Keep default-month returns in the backtest (recovery minus the last price), or your value factor will look better than any value factor has ever been.

## 9.4 Momentum: Bonds, Equities, and the Decay Clock

Momentum in credit comes in two kinds, and they tell different stories.

**Bond momentum** sorts on a bond's own trailing excess return. Israel, Palhares, and Richardson (2018) use the trailing six-month bond excess return,

$$
\text{MOM}^{\text{cr}}_{i,t} \;=\; \sum_{k=0}^{5} r^{xs}_{i,t-k},
$$

combined with the issuer's six-month equity return. The academic evidence (Jostova, Nikolova, Philipov, and Stahel, 2013, *Momentum in Corporate Bond Returns*) puts bond momentum mainly in non-investment-grade bonds, not investment grade (Man p.25). It is also the momentum most exposed to stale prices, for reasons §9.9 makes precise.

**Equity momentum in credit (EMC)** sorts bonds on their issuer's *stock* return. Barclays scales each horizon to a monthly rate and averages:

$$
\text{EMC}_{i,t} \;=\; \frac13 \sum_{h\in\{1,3,6\}} \frac{R^{E}_{j(i),\,t-h\to t}}{h},
$$

where $R^E_{j,t-h\to t}$ is the $h$-month equity return of issuer $j(i)$; the score is ranked into deciles at the issuer level (Dynkin p.693). Over 1993–2017, the weakest-equity-momentum decile returned −4.7% a year in excess return and the strongest +4.01% (Dynkin p.606). The economic story is information flow: equity markets are faster, deeper, and more continuously traded than bond markets, so news reaches the stock first and the bond later. Chordia, Goyal, Nozawa, Subrahmanyam, and Tong (2017) find the same lead in a broad sample: past equity returns positively predict bond returns. Chapter 3 treated this lead–lag as information flow at the trade level; Chapter 10 treats time-series trend, which is a different object (the market's own past return, not one issuer's relative return).

### 9.4.1 The decay clock

A momentum signal is a perishable good. Barclays reports a three-month transition matrix of EMC deciles in which an issuer in the top decile "has only a 17% probability of remaining top ranked after three months" (Dynkin p.610). Treat the decile rank as a Markov chain with monthly stay probability $p_1$ for the top decile, ignoring re-entry. Then $p_1^3 \approx 0.17$, and the half-life $\tau_{1/2}$ of membership solves $p_1^{\tau_{1/2}} = \tfrac12$:

$$
\tau_{1/2} \;=\; \frac{\ln \tfrac12}{\ln p_1} \;=\; \frac{3\,\ln \tfrac12}{\ln 0.17} \;=\; \frac{3 \times (-0.693)}{-1.772} \;\approx\; 1.2 \text{ months}.
$$

Half the top decile is gone in about five weeks. Returns decay on the same clock: the outperformance is 35bp in month one, 22bp in month two, and 19bp in month three, and 95bp over six months, so about 80% arrives in the first quarter (Dynkin p.611). Monthly rebalancing is barely fast enough to harvest it, and every rebalance costs money.

### 9.4.2 Break-even turnover

Let $\text{TO}$ be one-way turnover per month as a fraction of the portfolio, and $c$ the round-trip transaction cost as a fraction of value. Replacing a fraction $\text{TO}$ of the book means selling $\text{TO}$ and buying $\text{TO}$, each at half the round-trip cost, so the monthly cost drag is $\text{TO}\cdot c$ and

$$
\mathbb{E}^{\mathbb{P}}\!\left[r^{\text{net}}\right] \;=\; \mathbb{E}^{\mathbb{P}}\!\left[r^{\text{gross}}\right] \;-\; \text{TO}\cdot c,
\qquad
c^{\ast} \;=\; \frac{\mathbb{E}^{\mathbb{P}}[r^{\text{gross}}]}{\text{TO}}, \qquad
\text{TO}^{\ast} \;=\; \frac{\mathbb{E}^{\mathbb{P}}[r^{\text{gross}}]}{c}. \tag{9.3}
$$

Now plug in Barclays' top-decile EMC portfolio: turnover of 73% a month, and 6.34% a year in excess of the index before costs (Dynkin p.633). The break-even round-trip cost is

$$
c^{\ast} \;=\; \frac{6.34\%/12}{0.73} \;=\; 0.72\%.
$$

Any average round-trip cost above 72bp turns the strategy negative. The investment-grade index average liquidity cost score was 0.4% in 2007, 2.8% in 2008, and 0.6% in 2018–2019 (Dynkin p.703), and momentum churns into names that just moved, which are rarely the cheapest to trade. Barclays' verdict was that the strategy lost money after costs. Run (9.3) the other way: a signal earning 2.5% a year gross at a 0.6% round-trip cost can afford one-way turnover of $(2.5\%/12)/0.6\% \approx 35\%$ a month and no more.

> **[SOURCE EXTRACTION]** *Dynkin_Systematic_Investing_in_Credit p.633:* "Turnover is very high (73% per month) and performance before transaction costs is also very high (return of 7.31%/yr, or 6.34%/yr in excess of the index, with information ratio of 1.90 over the index) but transaction costs are so large that, once accounted for, both absolute and relative performance becomes negative."
>
> **Annotation.** Ines ran this one as a hand history. Kaz's version of the strategy showed the same pattern on the desk's data: a beautiful gross IR and a monthly bill from the dealers that exceeded it. "Congratulations," she said, "you've invented a very elaborate way to tip." IDO or it didn't happen, and in this case it didn't. The lesson is not that equity momentum fails in credit. It is that momentum in credit cannot be harvested as a stand-alone, high-turnover top-decile portfolio. Barclays' own response, and the 2026 desk's, is to use momentum as one input to a combined score (§9.7), to trade it with a buffer (§9.8) so that a bond sliding from the 95th to the 88th percentile is held rather than sold, and to trade it through portfolio trades and all-to-all protocols where the marginal cost is lower (Chapter 20). Momentum's gross alpha is real. Its *net* alpha is a property of your execution stack.

> **[SOURCE EXTRACTION]** *Dynkin_Systematic_Investing_in_Credit p.610:* "an issuer with equity momentum in the top 10% (D10) has only a 17% probability of remaining top ranked after three months"
>
> **Annotation.** One number fixes three design choices. It fixes the *rebalancing frequency*: a signal with a five-week half-life needs at least monthly rebalancing, and quarterly rebalancing gives away most of the alpha. It fixes the *turnover budget*: by (9.3), a fast signal can be held only if its gross alpha per unit of turnover clears the cost, which in credit is a high bar. And it fixes the *combination weight*: a factor with fast decay deserves less weight in a composite traded slowly. The 2026 refinement is to stop treating the decile as the state. A continuous score with a smooth tilt (rather than in or out of decile 10) lets a portfolio decay toward a signal rather than jump in and out of it, which is the same idea as the buffer in §9.8 written in a nicer language.

> **Desk Myth vs. Desk Reality.** *Myth:* "Use residual equity momentum: strip the stock's market beta first, and the credit signal improves." *Reality:* It depends on whose desk you are on. Haesen, Houweling, and van Zundert (2017, *Momentum Spillover from Stocks to Corporate Bonds*) find that residual equity momentum improves the risk properties of the spillover strategy. Barclays tests the same idea and finds that it does *not* improve EMC (Dynkin p.631). Both can be true: the two studies differ in universe, period, and how the credit leg is neutralized. When two careful desks disagree, the right response is not to pick a side but to run both definitions through your own clean data and your own cost model, and to give the tie to the simpler one.

## 9.5 Carry and Low-Risk: One Risk Sort in Two Costumes

### 9.5.1 Carry is the price of DTS

Koijen, Moskowitz, Pedersen, and Vrugt (2018, *Carry*) define carry as the return you earn if prices do not change. For a corporate bond over a period $\Delta t$,

$$
\text{carry}_{i} \;=\; s_i\,\Delta t \;+\; \text{roll-down}_i, \qquad \text{roll-down}_i \;\approx\; -D^{\text{spr}}_i\,\frac{\partial s_i}{\partial T}\,(-\Delta t),
$$

where the roll-down term is the spread tightening a bond earns as it ages down an upward-sloping issuer curve. Israel, Palhares, and Richardson use OAS alone, arguing that curve fitting adds opacity for little gain. In their sample (US investment grade and high yield, January 1997 to April 2015), carry is the one characteristic without a $t$-statistic of 3 or more, and its top-minus-bottom quintile Sharpe ratio is only 0.35.

Equation (9.1) explains why. Divide carry by risk:

$$
\frac{\text{carry}_i}{\text{DTS}_i} \;=\; \frac{s_i\,\Delta t}{D^{\text{spr}}_i\,s_i} \;=\; \frac{\Delta t}{D^{\text{spr}}_i}. \tag{9.4}
$$

The spread cancels. Per unit of spread risk, carry depends *only on duration*. A DTS-neutral carry sort, long high-carry-per-unit-of-risk and short low, is a sort on short versus long duration and nothing else. Before DTS-neutralization, carry is mostly beta. After DTS-neutralization, carry is a duration tilt, which is to say it has become a low-risk factor.

> **Desk Myth vs. Desk Reality.** *Myth:* "Carry is a factor." *Reality:* Carry is the price of DTS. If your carry factor still has alpha after DTS-matching, you have found either a short-duration factor (see below) or a value factor, and you should rename it before compliance does.

### 9.5.2 Low-risk and defensive

The low-risk factor in credit buys bonds with low duration, high ratings, low leverage, and high profitability. Houweling and van Zundert (2017) define it as short maturity and high rating. Israel, Palhares, and Richardson define "defensive" as low market leverage (net debt over net debt plus equity), high gross profitability, and low duration, and they explicitly *exclude* beta and volatility as characteristics, because in credit those are DTS, and DTS mixes duration (which they want) with spread (which is carry). Their defensive quintile spread has a Sharpe ratio of 1.11.

Equation (9.4) gives the duration part of the story a mechanism. Barclays documents it in the data: information ratios of corporate excess returns fall almost monotonically with maturity over 1994–2019 (Dynkin p.454–456), and the authors decompose the effect into roll-down, bear-steepening of credit curves in selloffs, and downgrade drift, which hurts long bonds more because they spend longer exposed to it. The rating part of the story is about default asymmetry, and Man states it best.

> **[SOURCE EXTRACTION]** *Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.26:* "the tightening of a bond on the upside to risk free rates is typically asymmetrically smaller than the jump to recovery in situations of distress."
>
> **Annotation.** A bond's best case is that its spread goes to zero; its worst case is recovery. The upside is capped and the downside is a cliff, so as spreads rise, more of the spread is payment for the cliff and less is excess reward. A one-period calculation makes it precise. With physical default intensity $\lambda^{\mathbb{P}}_i$ and loss $L$, $\mathbb{E}^{\mathbb{P}}[r^{xs}_i] \approx (s_i - \lambda^{\mathbb{P}}_i L)\,\Delta t$, while the variance is roughly $\big(\text{DTS}_i^2\sigma_\eta^2 + \lambda^{\mathbb{P}}_i L^2\big)\Delta t$. The reward per unit of risk is
>
> $$
> \frac{\mathbb{E}^{\mathbb{P}}[r^{xs}_i]}{\sigma(r^{xs}_i)} \;\approx\; \frac{s_i - \lambda^{\mathbb{P}}_i L}{\sqrt{\text{DTS}_i^2\,\sigma_\eta^2 + \lambda^{\mathbb{P}}_i L^2}}\,\sqrt{\Delta t},
> $$
>
> which falls as spreads rise whenever the expected-loss share of the spread, $\lambda^{\mathbb{P}}_i L/s_i$, rises with $s_i$. Empirically it does, steeply: in the synthetic universe of §9.11 it is about 4% for single-A and 42% for CCC *(illustrative calibration)*, and the real-world pattern runs the same way. That is the low-risk premium in credit: not a behavioral puzzle but the shape of a capped payoff. Where the modern desk departs from the simple story is leverage. A DTS-neutral low-risk book is long short-dated, high-grade paper levered several times against short long-dated, low-grade paper. In §9.11's synthetic universe, the long leg needs roughly ten times leverage to match the short leg's DTS. That leverage is the price of the premium, as in Frazzini and Pedersen's (2014) *Betting Against Beta*, and the factor's drawdowns are funding events.

### 9.5.3 Two live reminders that low-risk is a duration bet

Factor returns in this chapter are *excess* returns: duration-matched Treasuries are subtracted, so rates do not enter the factor's return. A client's total-return statement does not subtract anything. In 2022, when the Bloomberg US Aggregate fell about 13% and high yield about 11% (BlackRock_Systematic_High_Yield_Credit p.3), a low-risk book that held short-duration bonds *without* hedging rates looked brilliant in total return for reasons that had nothing to do with credit. The reverse happened in 2025–2026. Robeco's attribution for its Multi-Factor Credits fund, as of 30 September 2026, names the low-risk/quality factor as the largest detractor, "driven by an underweight in longer-dated bonds," as the long end rallied (Robeco fund page). Both are correct readings of a defensive tilt. Neither is the factor premium. A desk that reports factor performance must say, every time, whether the number is an excess return or a total return, and how the duration was hedged.
