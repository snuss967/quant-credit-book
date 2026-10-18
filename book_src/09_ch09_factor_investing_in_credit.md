# Chapter 9: Factor Investing in Corporate Credit


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

Kaz was not ready to fold. "Value is in every paper. Barclays has it. AQR has it. Robeco has been running client money on it since 2015. I didn't invent cheap bonds beating rich bonds. I replicated it."

"Then you replicated their beta too," Ines said, without heat. She set the coffee down on the edge of Kaz's desk the way she used to set down a chip she intended to leave there. "Fine. Suppose we take the index out and something survives. I'll ask again. Who at this table knows more than you?"

Kaz gave the question the care they gave anything that sounded as if it might be about probability. "Nobody. It's a backtest. It knows everything."

"The dealer," Ines said. "Every month your long book buys the cheap decile and your short book sells the rich one. Somebody quotes you both sides of every one of those trades, and that somebody sets the bid and the offer. In this backtest you trade at mid. Nobody has ever bought a single-B bond at mid. The dealer sees your flow coming the way I used to see a man reach for his chips before it was his turn, and he prices you for being predictable."

"I can add a cost model."

"You can add a cost model," Ines agreed. "Then tell me what sign the Sharpe has."

Mags had stopped pretending to read her screen. She turned her chair a quarter of the way round, which for her was the same as standing up. "There's a third one, and nobody's said it." She pointed a pen at the column headed `px_month_end`. "Those month-end prices. Who made them?"

"The vendor," Kaz said. "Evaluated pricing. It's a composite."

"Evaluated by whom, from what? Half your cheap decile didn't trade that month. Somebody's model guessed, and back in my day we had a word for a guess with a decimal point in it. We called it a mark. I once watched a mark go from 62 to 41 in an afternoon because somebody finally had to sell the bond." She turned the chair back. "Marks. Find out who made them before you find out what they paid you."

Kaz opened their mouth, closed it, and wrote something on a sticky note. On this desk, Kaz writing something down is the closest anyone gets to a confession.

Theo had once spent a month of his PJT life on a retailer's lease rejections, which is how he knew that the most important question about a building is who is actually living in it. He looked at the 1.9 the way he would have looked at a rent roll. The index was paying most of the rent. The dealer had a key and had not yet sent the bill. Something in the month-end marks was moving the furniture at night. Three tenants, and the landlord had not checked whether anyone else was home.

He took the USB stick out of his pocket, looked at it, and put it back. His 13-week cash flow model could not help him here, but he liked knowing where it was.

"So what's left," he asked, "after you take the spread risk out?"

That is the question this chapter answers. A credit factor is a rule for sorting bonds. It is worth something only if, once you remove the one thing every spread-adjacent sort secretly loads on, it still makes money after transaction costs that run five to twenty times larger than in equities, measured on prices that are partly rumor.

A week from now the same strategy will be back on the same screen, and the number will be smaller and more honest: a Sharpe ratio of 0.9 gross and 0.7 net, with a beta of 0.02 *(illustrative)*. The road from 1.9 to 0.7 is the chapter. It runs through duration times spread (DTS), which turns out to *be* beta in credit and lets the desk build DTS-neutral long–short and DTS-matched long-only factor portfolios (§9.2); through the canonical credit factors, value, momentum, carry, low-risk, quality, size and the "informed investor," built the way Barclays, AQR, Robeco and Man build them, including where those four disagree (§9.3–9.6); through combining factors with information ratios and a correlation matrix, and the uncomfortable cases where the combination *loses* to the best single factor (§9.7); through a transaction-cost budget placed at the center of construction, with liquidity cost scores, turnover buffers, turnover caps and a factor's break-even cost (§9.4, §9.8); through the 2019–2026 replication debate, read as a desk and boiled down to five rules for a factor library (§9.9); and out the other side into a specification ROBO can rebuild on a synthetic universe, with sanity checks that fail loudly when the mathematics is wrong (§9.11).

## 9.1 What a Factor Is in Credit, and Why It Is Not What It Is in Equities

In equities, a factor is a characteristic (book-to-market, past twelve-month return, profitability) that sorts stocks into portfolios whose return spread is persistent, explainable, and not just the market in disguise. The word means the same thing in credit. The difficulty is that three facts about corporate bonds make every step harder, none of them with a clean equity analogue, and the desk ran into all three in the ten minutes after Kaz's backtest finished.

The first was Kaz's 0.6. Spread is both the signal and the risk. A value sort in equities is not a beta sort; cheap stocks do not have mechanically higher market betas. In credit, every signal built from the spread (value, carry, "cheapness" of any kind) is mechanically a sort on how much spread risk a bond carries, because a wide bond moves more than a tight one for the same market shock. Kaz had asked the data for cheap bonds and been handed, free of charge, a sort on beta. Section 9.2 makes this exact: under the empirical law that spread changes are proportional to spread levels, a bond's beta to the credit market is its DTS divided by the market's DTS. A dollar-neutral portfolio that is long wide bonds and short tight ones is therefore a long-beta portfolio in a hedge fund costume.

The second was the dealer, and Ines had met him on this desk before. The previous spring Kaz had brought her an equity-momentum strategy for credit with a gross information ratio that looked like a misprint and a monthly bill from the dealers that was larger. She replayed it as a hand history, trade by trade, and handed it back. "Congratulations," she said, "you've invented a very elaborate way to tip." The published version of that strategy fares no better: Barclays' top-decile equity-momentum-in-credit portfolio, which we meet in §9.4, made 6.34% a year over the index before costs, with an information ratio of 1.90, and lost money after them (Dynkin p.633). An equity quant who ignores transaction costs gets a backtest that is too optimistic. A credit quant who ignores them gets a backtest that is the wrong sign. Costs here are first-order, not a footnote, and factor investing in credit is a turnover-budgeting problem with a signal attached.

The third was Mags's question, and it takes longest to answer: who made the marks? A corporate bond trades a few times a week, if that. Its "price" on a given month-end is a composite of a stale print, a dealer run, and a pricing service's model. Her 62-to-41 afternoon is the extreme case. The ordinary case is a mark that is a point or two wrong in a random direction, which sounds harmless until you notice that the error enters both the signal you sort on and the return you measure, so the data lie, and they lie asymmetrically. The error is largest in exactly the small, illiquid, high-yield bonds where published factors claimed to find the most alpha. Chapter 7 told the story of how that error, plus some careless return filters, inflated an academic literature until a benchmark paper was retracted. Section 9.9 shows what it does to factor construction specifically.

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

Kaz, reading the table over Theo's shoulder, said the Value row was unkind. It is not unkind. It is an average, and somebody has measured the average.

> **View From Another Seat.** *A systematic factor manager looks under everyone else's hood.* AQR's Diogo Palhares and Scott Richardson did to a whole industry what Ines did to Kaz's backtest: they regressed active credit managers' returns on the market and on a set of systematic credit factors and asked what was left. Their answer, in *Looking Under the Hood of Active Credit Managers* (Financial Analysts Journal 76(2), 2020, pp. 82–102), is that "credit long/short managers tend to have high passive exposure to the credit risk premium," that high-yield long-only managers carry less exposure than their benchmarks, and that neither group shows "economically meaningful exposures to well-compensated systematic factors." Seen from AQR's chair, the cold open is not one quant's private embarrassment. It is the published average: the typical credit hedge fund is long the index in a costume, and the typical long-only manager is underweight risk without being overweight anything that pays for it. A firm that sells factor exposure for a living has an obvious commercial reason to say this, which is worth remembering; it is also the reason somebody bothered to measure it. The desk's ambition is narrower than AQR's. It does not need to grade the industry. It needs its own 1.9 not to become a data point in the next version of the paper.

The division of labor that would have caught Kaz's beta before Ines did has its cleanest statement in the equity long–short literature, not in credit's.

> **[SOURCE EXTRACTION]** *Paleologo_Advanced_Portfolio_Management p.27:* "To estimate 𝛼 as accurately as possible is the job of the fundamental investor. To estimate 𝛽, identify the correct benchmarks m, and the returns 𝜖 is the job of the quantitative risk manager."
>
> **Annotation.** Paleologo writes for equity long–short managers, but the division of labor he describes is the cleanest statement of why credit factor investing is hard. In equities you can let a risk model own $\beta$ and spend your life on $\alpha$, because the two are estimated from different information. In credit the same number, the spread, sits on both sides of the line. The spread level is the input to the "fundamental" judgment (is this bond cheap?) and also the main determinant of the bond's market beta (how much does it move?). If you hand the spread to the alpha model without first handing DTS to the risk model, the alpha model will happily rediscover beta and call it skill. The 2026 desk resolves this by order of operations, not by job title: the risk side defines DTS cells and a DTS-scaled covariance first, and the alpha side is allowed to rank bonds only *within* that structure. The RSSG reader, who has always been the $\alpha$ person, now also has to be the $\beta$ person, because nobody else on the desk knows that the widest bond in the cell is wide because of a drop-down basket the model cannot see.

How many desks are making Kaz's mistake, or avoiding it, depends on how large the systematic credit business has grown, and that number has moved faster since 2018 than in the twenty years before.

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

The morning after the backtest, Theo asked Kaz the question he would have asked of any number in a restructuring model: where does it come from? Why should a wide bond move more than a tight one, and why should "more" be something you can compute before the month starts? Kaz drew two boats on the whiteboard, which is not how Kaz usually answers anything.

> **Math, Gently.** *Relative change, and beta as a ratio.* **Part one: two boats on one tide.** Picture two bonds on the same bad morning. One sits at 100bp, the other at 300bp. The news is "credit is 10% wider," and both obey it: the first widens 10bp, the second 30bp. An absolute ruler ("spreads moved 5bp") would treat the two bonds as identical and be wrong by a factor of three. A relative ruler says each moved 10%, and then asks what that 10% costs you. The cost is spread duration times the absolute move: at five years of spread duration, 10bp is 0.5% of price and 30bp is 1.5%. Duration times spread, $5 \times 1\% = 5$ against $5 \times 3\% = 15$, carries the same factor of three. DTS is how much of your boat is in the water: the tide is the same for everyone, and DTS decides how far it lifts or sinks you. **Part two: beta is a ratio.** A beta answers "when the market moves one unit, how many units do I move?" The textbook formula, covariance over variance, reads in English as *how much of your move is the market's move, per unit of the market's move.* If every bond rides the same tide, a bond moves by its DTS times the tide and the market moves by the market's DTS times the same tide, so the tide cancels and the beta is the ratio of the two DTS numbers. A bond with DTS 12 in a market with DTS 8 has a beta of $12/8 = 1.5$; a bond with DTS 4 has $4/8 = 0.5$. No regression and no five years of history, just two numbers off the screen. The covariance algebra is next; Chapter 1's box on regression slopes has the general idea of a beta.

Put the two parts together and the whole result fits on one line:

$$
\beta_i \;\approx\; \frac{\text{DTS}_i}{\text{DTS}_m}. \tag{9.1}
$$

Equation (9.1) is the most useful line in this chapter. Beta in credit is not something you estimate with a five-year regression and a prayer. To first order it is a ratio you can read off the screen at the start of the month. Where the tide stops being one tide, the ratio stops being beta, and Mags is about to find that edge in §9.2.2.

#### The Full Derivation

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
\;=\; \frac{\text{DTS}_i}{\text{DTS}_m}.
$$

The tide cancels, and what remains is (9.1).

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

Look at what happens to the carry: $2.0\% \times 1 - 1.2\% \times 1.667 = 0.0\%$. When the two legs have the same duration, a DTS-neutral long–short has *exactly zero net carry*, because carry is $s$ and DTS is $D^{\text{spr}} s$, so matching DTS at equal duration matches spread. The cold open's Sharpe ratio was carry on borrowed beta. After DTS-matching, both are gone, and whatever is left is the signal. (In this illustration nothing is left, which is why Mags went back to her terminal.) The general version of this result, carry per unit of DTS equals $1/D^{\text{spr}}$, comes back in §9.5, where it turns the carry factor into the low-risk factor. Figure 9.1 shows the two books side by side.

![Figure 9.1: Matching the short leg's DTS to the long leg's closes the 4.8 gap (left) that gave the dollar-neutral book a beta of 0.6 and 0.8% a year of carry, leaving a book that neither moves with the index nor earns anything before a signal (right). Illustrative: the §9.2.2 worked example (leg DTS 12.0 and 7.2, market DTS 8.0, spreads 2.0% and 1.2%) with 84 simulated months of index returns and no signal.](assets/figures/ch09_kaz_book_dts_neutral.png)

Mags did not stay at her terminal long. When Kaz rebuilt the book cell by cell, she leaned over and put a pen on one line of the single-B energy cell: a bond at 2,500bp, sitting in the long leg with a DTS that made it the largest risk position in the cell, so that the short leg had been scaled up to match it. "If the market widens ten percent tomorrow, does this one widen ten percent?"

Kaz pulled its history. In the market's last bad week the index had widened 9% and this bond had dropped half a point *(illustrative)*.

"Because it isn't trading on spread," Mags said. "It's trading on what you get back. Forty cents, give or take, after the lawyers. Your ruler measures the tide, and this one is already on the beach."

Kaz conceded that it was priced to recovery, moved it out of the DTS scaling into a bucket of its own, and watched the cell's short leg give back the notional it had been carrying to hedge a tide the bond no longer rode.

> **[SOURCE EXTRACTION]** *Ben_Dor_Quantitative_Credit_Portfolio_Management p.34:* "just as spread duration is the sensitivity to an absolute change in spread (e.g., spreads widen by 5 bps), DTS (D · s) is the sensitivity to a relative change in spread."
>
> **Annotation.** This is the sentence that turned a portfolio-management heuristic into a risk model. Spread duration answers "what if spreads widen 5bp?", a question nobody should ask in high yield, where a 5bp move is a rounding error on Monday and a fantasy on the Friday before a lender call. DTS answers "what if spreads widen 10%?", which is the question the market actually poses, because spreads move in proportion to themselves. Barclays QPS introduced the measure with Robeco in 2005 (Dynkin p.729, note 11). It is now standard in index analytics. For factor investing the consequence is structural: the natural unit of exposure is DTS, so the natural neutrality condition is DTS-neutrality, and the natural cells for comparing bonds are cells of similar DTS. Two caveats separate the 2026 desk from the 2005 paper. First, proportionality weakens near distress, which is what Mags found in the single-B energy cell: a bond anchored to recovery does not ride the tide. Above roughly 1,000bp the desk switches from DTS to price-based or recovery-based risk (Chapters 5 and 14). Second, DTS is a bond-level number, and an issuer's bonds can diverge wildly when a liability-management transaction splits the capital structure into winners and losers, so issuer-level DTS-neutrality is not bond-level DTS-neutrality.

Ben Dor's sentence is the theory. Barclays later measured what ignoring it does to a value signal, in good markets and bad.

> **[SOURCE EXTRACTION]** *Dynkin_Systematic_Investing_in_Credit p.741:* "In the case of ESP, adjusting for DTS reduces correlations with US Corporate Index excess returns from 34% to –6% in drawdown episodes and from 44% to –22% in other (benign) periods."
>
> **Annotation.** This is the cold open measured on real data. ESP is Barclays' value signal (§9.3). Built naively, with long and short legs that differ in DTS, its correlation with the credit index is +44% in benign markets, so nearly half its variance is beta. DTS-match the legs and the sign *flips* to −22%: the genuine value signal is mildly *defensive*, because cheap-to-fundamentals bonds that are not simply wider are, on average, being mispriced by forced or panicked sellers. The practical lesson is in the drawdown numbers, 34% falling to −6%: a naive value book loses money exactly when the desk can least afford it, and a DTS-matched one does not. The 2026 desk reports every factor in both forms, because the gap between them is a direct measure of how much of the factor was beta. When a vendor shows you a credit-value backtest without saying how it handled DTS, assume the worse version.

Theo's first attempt to write any of this down for ROBO went the way first specifications usually go.

> **The Spec You Hand the Robot (what ROBO built from the vague version).** Theo's first specification said: "Neutralize spread exposure in both legs." ROBO, which never guesses, reduced each leg's DTS to zero by selling every corporate bond and buying two-year Treasuries. The book's spread exposure was perfectly neutral. So was its alpha. The precise version: "At the start of each month, using beginning-of-month OAS and OAS duration, scale each leg so that $\sum_{i \in \text{leg}} |w_i|\, D^{\text{spr}}_i s_i = 12$ (years × percent) within each rating × sector cell; if a cell has fewer than five bonds in a leg, pool it with the adjacent rating; never rescale with end-of-month DTS."

That last clause exists because of ROBO's second run, which used the month-end file because nobody had said which DTS to use. In the backtest's worst month the short leg grew after the fact to match spreads that had already widened, and the hedge looked flawless in exactly the month a real one would have failed.

> **Ways This Blows Up.** (1) *Units.* DTS in years × percent and years × basis points differ by a factor of 100. A DTS cap of 5 in one convention is a cap of 500 in the other, and a junior analyst will eventually enter the wrong one into the optimizer. Name the units in the variable name. (2) *Timing.* Scaling legs with end-of-month DTS is look-ahead: in a selloff, spreads widen, DTS rises, and the "neutral" short leg grows retroactively. Use beginning-of-month DTS only. (3) *Callables.* Use option-adjusted duration on callable high yield; modified duration on a bond trading to a 2027 call overstates its DTS and under-hedges it. (4) *Distress.* Cap DTS-based scaling for spreads above about 1,000bp or treat those names separately; a DTS-neutral short leg of three CCC bonds is not neutral to anything except the bankruptcy court's calendar. (5) *Leverage.* DTS-neutral legs need not be dollar-equal. A DTS-neutral book that is long short-dated A-rated paper and short long-dated BBBs can be levered several times on the long leg, and leverage has its own cost and its own drawdown (§9.5).

## 9.3 Value: ESP, SPiDER, and the Fair-Spread Family

Value is the factor an RSSG reader understands best and gets wrong most expensively. "This bond is cheap" is a statement about a spread *relative to something*. Every value model is a choice of the something.

### 9.3.1 Excess spread to peers (ESP)

Barclays' value measure is a monthly cross-sectional regression within peer groups. It is the chapter's first load-bearing residual, so it is worth slowing down for.

> **Math, Gently.** *A residual is the part the peers cannot explain.* Picture three BB chemicals bonds, all with about seven years to maturity, quoted at 180, 210 and 300bp. A regression inside that cell draws one fair line through it: spread as a function of leverage, coverage and the rest. Plug in the third bond's leverage and the line says it "should" trade at 220bp. It trades at 300. The residual is the difference, $300 - 220 = +80$bp: what the market is paying you that the bond's peers and its ratios do not account for. Everything in this section is a way of computing that 80, and most of the chapter after it is an argument about whether the 80 is a gift (a forced seller, a downgrade flow, a new issue priced to clear) or a warning (something the ratios cannot see). One refinement. The desk runs the regression on the logarithm of the spread rather than the spread itself, because on a log scale a residual of $\ln(300/220) \approx 0.31$ means "about 36% wider than fair" whether the fair line sits at 100bp or at 1,000bp. That is the relative ruler of the two boats in §9.2; measured in basis points instead, an 80bp residual is a shout at 220 and a whisper at 1,000. Chapter 1's box on regression slopes covers how the line itself gets drawn.

For a peer group $g$ (rating × sector × maturity bucket), estimate

$$
s_{i,t} \;=\; a_{g(i),t} \;+\; b_{1,t}\,\text{Lev}_{i,t} \;+\; b_{2,t}\,\Big(\frac{\text{ND}}{\text{EBITDA}}\Big)_{i,t} \;+\; b_{3,t}\,\text{ICov}_{i,t} \;+\; \epsilon_{i,t},
$$

where $a_{g,t}$ is a peer-group intercept, $\text{Lev}$ is financial leverage, $\text{ND}/\text{EBITDA}$ is net debt to EBITDA, and $\text{ICov}$ is interest coverage. (Dynkin p.693 names exactly these three ratios; financials, whose EBITDA is not meaningful, use long-term debt to long-term assets instead.) The fitted residual $\hat\epsilon_{i,t}$ is the spread the market pays you beyond what the bond's peers and fundamentals justify. Rank it across the index into deciles:

$$
\text{ESP}_{i,t} \;=\; \operatorname{decile}\big(\hat\epsilon_{i,t}\big)\in\{1,\dots,10\}, \qquad \text{high} = \text{cheap}.
$$

In Barclays' results, measured against the index, the richest decile returned −1.10% a year (information ratio −0.27) and the cheapest +3.29% a year (IR 0.53) (Dynkin p.528), and the long–short spread has an IR above 1.5 (Dynkin p.545). The same page adds the condition that matters for 2026: the outperformance is larger when the cross-sectional dispersion of ESP is high. Value needs something to be cheap *relative to*; §9.10 returns to what happens when the whole market is tight.

The regression in §9.11 uses the *logarithm* of OAS rather than its level, for the reason in the box, and that is our choice, not Barclays'. If spreads move proportionally, log spread is the scale on which a residual of 0.2 means "20% cheap" for a 90bp bond and a 400bp bond alike. Its slopes $b_{k,t}$ are common across cells while the intercepts vary by cell. Letting every cell have its own slopes sounds more flexible and is, in practice, a way to fit noise in cells with eleven bonds.

> **[SOURCE EXTRACTION]** *Dynkin_Systematic_Investing_in_Credit p.524:* "We identify relative value as the portion of excess spread over peers unexplained by fundamental factors and call this measure excess spread to peers (ESP)."
>
> **Annotation.** The sentence is short, and every phrase in it is a modeling decision. "Over peers" means the comparison is always within a cell, never across the whole market, which is the first defense against the DTS problem of §9.2: within a rating × sector × maturity cell, spreads and durations are similar, so a residual is not just a disguised spread level. "Unexplained by fundamental factors" means three balance-sheet ratios stand in for what an RSSG analyst would call the credit story, which is a heroic compression. What the residual contains on a 2026 desk is the reason the RSSG reader matters. Part of it is genuine mispricing: forced selling after a downgrade, index-exclusion flows, a new issue priced to clear. Part of it is information the three ratios cannot see: a collateral-stripping drop-down, a priming threat from a cooperating majority, or an incremental-debt basket the size of a small country. A pure-quant ESP book buys both kinds. A desk that adds a document-risk regressor (the Priming Risk Score of Chapter 13) buys only the first kind.

### 9.3.2 SPiDER and Man's spread per turn of leverage

Regression residuals are opaque and their coefficients wander. Barclays' model-free alternative, SPiDER, divides the spread by a long-run leverage multiple:

$$
\text{SPiDER}_{i,t} \;=\; \frac{s_{i,t}}{\text{Debt}_{i,t}\,/\,\overline{\text{EBITDA}}^{\,\text{LT}}_{i,t}},
$$

where $\overline{\text{EBITDA}}^{\,\text{LT}}$ is a long-term average EBITDA. It is spread per turn of leverage, which is how a leveraged-finance banker already prices a deal. Man's raw value signal is the same idea, written schematically as `OAS / (Net Debt/EBITDA).clip(lower=0.1)`, then risk-adjusted for size, default probability, and volatility and compared within rating and sector (Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.24).

Take the floor literally for a moment. An issuer with negative EBITDA has a *negative* net-debt-to-EBITDA ratio, which the floor converts to 0.1×, so its spread is divided by 0.1 and it becomes the cheapest bond in the universe. Man's later risk adjustment presumably catches this. An implementation that leans on "presumably" will one day show a cash-burning issuer as its top value pick, and the person who has to explain that to a client will not enjoy the word. The code in §9.11 assigns negative-EBITDA issuers a punitive 15× multiple before any floor is applied; excluding them works too. The floor exists to stop division by a number near zero, not to promote companies that are losing money.

Dynkin p.553 lays out the menu. Regression fair spreads control many characteristics at once but overfit. Structural models are parameter-hungry and opaque. SPiDER is neither, and it aggregates cleanly across sectors and time.

> **[SOURCE EXTRACTION]** *Dynkin_Systematic_Investing_in_Credit p.553:* "While a regression is able to control for multiple risk characteristics at the same time, it is vulnerable to statistical problems, such as overfitting and instability in coefficients."
>
> **Annotation.** Every desk discovers this the second month it runs ESP live. The coefficient on interest coverage, positive last month, is negative this month because three energy names had a bad quarter and the cell has 23 bonds. The ranking barely moves, but the portfolio manager sees a "value model" whose logic has reversed, and asks a fair question. The 2026 answers are standard statistics, not new ideas. Shrink each month's slopes toward a trailing average or toward a pooled estimate (Chapter 8's shrinkage machinery). Pool any cell with fewer than about 15 bonds into a coarser one. Winsorize residuals at the 1st and 99th percentiles before ranking. And run SPiDER alongside ESP as a model-free control: when the two disagree violently on a name, a human should look at it, which is the "quantamental" loop of §9.6.

### 9.3.3 The structural fair spread, and the measure trap

The third family builds a fair spread from a structural model and calls the bond cheap when its market spread exceeds the fair one (Correia, Richardson, and Tuna, 2012, *Value Investing in Credit Markets*). The step that trips people up is the change of measure, so we do it carefully.

> **Math, Gently.** *The bell, its dial, and the bookmaker's odds.* **Part one: the normal distribution and its two dials.** Picture a hill of sand, highest in the middle and thinning out evenly on both sides. That is the standard normal distribution, the shape you get when many small, independent pushes add up. Put a firm's distance to default on the horizontal axis, measured in standard deviations: how many typical bad years its assets can absorb before they fall through the debt. The function $N(x)$ answers "how much of the sand lies to the left of $x$?", which here means "how likely is it that the firm ends up at least that far below where it is expected to be?" Two values are worth knowing by heart: $N(-1) \approx 16\%$ and $N(-2) \approx 2.3\%$. A firm two standard deviations from the line has about a 2.3% chance of crossing it. The inverse, $N^{-1}$, runs the dial backward: hand it a probability and it hands you the distance, so $N^{-1}(2.3\%) \approx -2$. **Part two: risk-neutral in one breath.** A bookmaker who means to stay in business does not quote the horse's true odds; he shades every price so that the outcomes that hurt him cost more. The bond market does the same with bad states of the world. It prices default as if it were likelier than it is, because defaults arrive in recessions, when a lost dollar hurts most. The risk-neutral ($\mathbb{Q}$) probability is the physical ($\mathbb{P}$) one with the dial turned toward default by $\theta\sqrt{T}$, where $\theta$ is the extra return the firm's assets earn per unit of risk. A tiny number: a four-year physical PD of 1% sits at $N^{-1}(0.01) = -2.326$; with $\theta = 0.2$ the shift is $0.2 \times \sqrt{4} = 0.4$, and the risk-neutral PD is $N(-2.326 + 0.4) = N(-1.93) \approx 2.7\%$. Same firm, same assets, nearly three times the default probability, and the difference is a price, not a forecast. The $\tfrac12\sigma^2$ that appears in the formula below is the tax a lognormal pays for being measured in logs. Chapter 6 owns the full version of both ideas (§6.1 for the tax, §6.3 for the change of measure), and Chapter 5's box on the lognormal draws the picture.

Written as one line, the whole change of measure is

$$
\text{PD}^{\mathbb{Q}}_T \;=\; N\!\left(N^{-1}\!\big(\text{PD}^{\mathbb{P}}_T\big) + \theta\sqrt{T}\right),
\qquad \theta \equiv \frac{\mu - r}{\sigma_V}. \tag{9.2}
$$

Run a five-year bond through it, and through the fair-spread formula in the derivation below, with a physical default probability of 2%, an asset Sharpe ratio $\theta = 0.25$ and a loss given default of 0.6, and the fair spread comes out at 83bp. Skip the step and the same bond's fair spread is 24bp.

That gap is the **measure trap**. A desk that uses physical default probabilities as if they were risk-neutral finds that every bond in the market is cheap by about 60bp, buys all of them, and has rediscovered the credit risk premium, which is to say the index. A cross-sectional *rank* survives a monotone mapping from $\mathbb{P}$ to $\mathbb{Q}$, but only within a cell where $T$ and $\theta$ are the same. Across maturities, or across issuers with different asset correlations to the market, the mapping is not common, and any comparison of *levels*, such as "spread per unit of expected loss," is simply wrong without it.

#### The Full Derivation

In the Merton model (Chapter 6, §6.2), assets follow $dV_t = \mu V_t\,dt + \sigma_V V_t\,dW_t$ under $\mathbb{P}$, and default occurs at $T$ if $V_T < F$. The physical default probability is

$$
\text{PD}^{\mathbb{P}}_T \;=\; N\!\left(-\text{DD}^{\mathbb{P}}\right), \qquad
\text{DD}^{\mathbb{P}} \;=\; \frac{\ln(V_0/F) + (\mu - \tfrac12\sigma_V^2)\,T}{\sigma_V\sqrt{T}},
$$

where $N(\cdot)$ is the standard normal distribution function and DD is distance to default. Under $\mathbb{Q}$ the drift $\mu$ is replaced by $r$, so

$$
\text{DD}^{\mathbb{Q}} \;=\; \text{DD}^{\mathbb{P}} - \frac{\mu - r}{\sigma_V}\sqrt{T}
\quad\Longrightarrow\quad
\text{PD}^{\mathbb{Q}}_T \;=\; N\!\left(N^{-1}\!\big(\text{PD}^{\mathbb{P}}_T\big) + \theta\sqrt{T}\right),
\qquad \theta \equiv \frac{\mu - r}{\sigma_V}.
$$

Here $\theta$ is the asset Sharpe ratio; under the CAPM it equals $\rho_{V,m}$ times the market Sharpe ratio. (We call it $\theta$ rather than the $\lambda$ some papers use, because $\lambda$ is reserved in this book for default intensity.) With recovery of a fraction $R$ of face paid at maturity (the recovery-of-Treasury convention), the zero-coupon price is $e^{-rT}\big(1 - \text{PD}^{\mathbb{Q}}_T L\big)$ with $L = 1 - R$, and the fair spread is

$$
s^{\text{fair}}_i \;=\; -\frac{1}{T}\,\ln\!\left(1 - \text{PD}^{\mathbb{Q}}_T\,L\right), \qquad \text{value}_i = s_i - s^{\text{fair}}_i .
$$

A worked example, with illustrative inputs: five-year physical PD of 2%, $\theta = 0.25$, $L = 0.6$. Then $N^{-1}(0.02) = -2.054$, the shift is $0.25\sqrt5 = 0.559$, and $\text{PD}^{\mathbb{Q}}_5 = N(-1.495) = 6.75\%$. The fair spread is $-\tfrac15\ln(1 - 0.0405) = 83$bp. Skip the change of measure and you get $-\tfrac15\ln(1 - 0.012) = 24$bp, the two numbers the measure trap above is built on.

### 9.3.4 The residual is cheapness or it is information

Here is the most important practical fact about value in credit, and the one the RSSG reader is best placed to exploit.

*The desk's fictional run; the numbers are illustrative.*

The Monday after the 1.9, Theo came in at seven with a printout of the ESP specification, which was one line long, and a question he had been holding since Friday. "Three ratios," he said to Kaz. "Leverage, net debt to EBITDA, coverage. Where's weeks of liquidity?"

"Because nobody put it in the panel," Kaz said.

So Theo put it in the panel. The runway from his 13-week cash flow model, cash plus undrawn revolver divided by the trailing weekly burn, had lived on the USB stick for six years as a habit; now it had to become a column. Most of the morning went into the dull part: mapping his issuer names to the desk's identifiers, discovering that two vendors disagreed about which entity was the parent of a third of the high-yield universe, and lagging every number by a quarter so that the regression could not read a 10-Q before it had been filed. By lunch the column existed. By two it was in the regression.

In single-A it did nothing. The coefficient was a rounding error, which was the right answer: in single-A nobody runs out of cash, and the column was a list of numbers in the hundreds of weeks. In the single-B and CCC cells it was the largest coefficient after the cell intercept, and it pulled a fifth of the names out of the cheap decile.

One of them he recognized. Not from a deal, from a pitch book: a sponsor-owned business-services company his old team had once pitched for a mandate PJT never won, built, as pitch books are, entirely from public filings. The pitch had been about a revolver that would go current in eighteen months. The regression had ranked the company's bonds third-cheapest in their cell. The column ranked them as a company about four quarters from a phone call to its lenders. Nothing in it was secret. It was the same 10-Q everybody had, read in weeks instead of turns.

Those were not cheap bonds. They were bonds pricing an event the three ratios could not see.

> **View From Another Seat.** *A long-only systematic manager with analysts standing behind the model.* Robeco has done quantitative fixed income since 1995 and has run its QI Global Multi-Factor Credits fund since 2015, and on 7 September 2026 two of its quants, Lodewijk van der Linden and Patrick Houweling, described how that seat handles Theo's problem. The design aim is "to keep first-order risks, such as rates and credit beta, close to the benchmark, so that relative returns are driven primarily by credit returns from bottom-up issuer and bond selection," which is §9.2 written as a mandate. The model ranks about 1,600 issuers in global high yield and 2,600 in investment grade, and before a ranking becomes a trade, "portfolio managers and fundamental credit analysts can challenge the model where downside risk is not adequately reflected"; more than twenty analysts screen the buy candidates. Their own example of when the challenge matters is a bond that looks cheap because spreads widened while "a major lawsuit, regulatory issue, large acquisition or other event sits outside the model's scope." That is the residual-as-information problem, stated by the people whose live record §9.10 leans on, and their answer is a human gate. Theo's column is the other answer: move some of what the analyst would have caught into the panel, so that the gate has less to catch. The two are complements. A runway fits in a column; a drop-down basket, for now, mostly does not, and that is the part Chapter 13 tries to score.

Man's research team found the same ambiguity one level further down, inside a single capital structure.

> **[SOURCE EXTRACTION]** *Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.25:* "Value stands out as being particularly CUSIP-specific, that is to say that within the same capital structure, even after accounting for liquidity, subordination, duration, etc., mispricing can remain."
>
> **Annotation.** Man's observation is that value lives at the bond level, not only at the issuer level: two bonds of the same company, after controlling for the obvious differences, can be priced inconsistently. For a pure quant, that is a statement about breadth: more CUSIPs, more independent bets. For an RSSG reader it is an invitation, because the "etc." in that sentence is where the credit agreement lives. Within one capital structure, the 2029 notes and the 2031 notes may differ in guarantor coverage, in whether they sit at an entity that can be stripped by a drop-down, or in whether they are the obvious target of a non-pro-rata exchange. A residual that a pure-quant model calls "CUSIP-specific mispricing" is sometimes exactly that, and sometimes the market correctly pricing a document risk that the model cannot read. The 2026 desk resolves the ambiguity by adding document features as regressors (Chapter 13's Priming Risk Score; Chapter 25's covenant-capacity variables). Whatever value survives *that* regression is cheapness. Whatever it removes was information, and you are better off having known it before you bought.

Most of the ways a value book goes wrong in practice have less to do with what the residual means than with the plumbing that produces it.

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

A momentum signal is a perishable good, and the right way to measure how perishable comes from the kitchen.

> **Math, Gently.** *Half-life, or how fast the coffee goes cold.* A cup of coffee does not lose a fixed number of degrees a minute; it loses a fixed *fraction* of its excess heat over the room each minute. That is exponential decay, and its natural yardstick is the half-life, the time it takes for half the excess to be gone, which is the same whether the cup started scalding or lukewarm. A signal's top decile cools the same way. Suppose that each month 80% of the bonds in the top decile are still there a month later. After one month 80% remain, after two $0.8^2 = 64\%$, after three $0.8^3 \approx 51\%$: a half-life of about three months. One logarithm turns any monthly survival rate $p$ into a half-life, $\tau_{1/2} = \ln 2 / \ln(1/p)$, here $0.693/0.223 \approx 3.1$ months. A signal like that can be traded quarterly and still be warm when you drink it. Chapter 1 cooled the same cup to show price pressure fading after a forced sale; here the thing cooling is the reason you bought the bond.

Barclays reports a three-month transition matrix of EMC deciles in which an issuer in the top decile "has only a 17% probability of remaining top ranked after three months" (Dynkin p.610). Treat the decile rank as a Markov chain with monthly stay probability $p_1$ for the top decile, ignoring re-entry. Then $p_1^3 \approx 0.17$, so the monthly stay probability is $p_1 = 0.17^{1/3} \approx 0.55$, much colder than the box's 0.8, and the half-life $\tau_{1/2}$ of membership solves $p_1^{\tau_{1/2}} = \tfrac12$:

$$
\tau_{1/2} \;=\; \frac{\ln \tfrac12}{\ln p_1} \;=\; \frac{3\,\ln \tfrac12}{\ln 0.17} \;=\; \frac{3 \times (-0.693)}{-1.772} \;\approx\; 1.2 \text{ months}.
$$

Half the top decile is gone in about five weeks. If you rebalance quarterly, you are drinking cold coffee. Returns decay on the same clock: the outperformance is 35bp in month one, 22bp in month two, and 19bp in month three, and 95bp over six months, so about 80% arrives in the first quarter (Dynkin p.611). Monthly rebalancing is barely fast enough to harvest it, and every rebalance costs money. Figure 9.2 shows both clocks.

![Figure 9.2: Only 17% of the top decile is still top-ranked after three months, a half-life of about 1.2 months (left), and the outperformance of the above-median equity-momentum cohort over the below-median one fades on the same clock, with 76 of the 95bp over six months earned in the first quarter (right). Source: Dynkin et al., p.610–611, as quoted in §9.4.1; the survival curve is the one-parameter Markov chain (no re-entry) fitted to the 17% figure, and the months 4–6 bar is the remainder of the 95bp six-month total.](assets/figures/ch09_momentum_decay_clock.png)

### 9.4.2 Break-even turnover

A signal that goes cold in five weeks has to be refreshed every month, and in credit every refresh is a trip to the dealer. Ines's question from the cold open, who at this table knows more than you, now has a price attached, and the price is per unit of distance travelled.

> **Math, Gently.** *Turnover is a meter, and the break-even cost is where it runs out.* Think of a taxi meter that charges by how far your portfolio travels rather than by the mile. Turnover is the distance: the fraction of the book you replace each month. Replace half of it and you have sold 50% and bought 50%, and each of those trades pays half the round-trip cost (the gap between where you can buy and where you can sell), so the month's bill is turnover times the round trip. At 50% one-way turnover and a 1% round trip that is 0.5% a month, 6% a year, which is more than most credit signals earn before costs in a good year. The break-even cost turns the question around: given what the signal earns gross, how expensive can a round trip be before the meter eats all of it? Divide the monthly gross return by the turnover. A signal earning 2.4% a year that replaces a fifth of the book each month can afford round trips up to $(2.4\%/12)/0.20 = 1\%$, and not a basis point more. The formula comes next, and then Barclays' numbers, which are less forgiving.

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

Any average round-trip cost above 72bp turns the strategy negative. The investment-grade index average liquidity cost score was 0.4% in 2007, 2.8% in 2008, and 0.6% in 2018–2019 (Dynkin p.703), and momentum churns into names that just moved, which are rarely the cheapest to trade. Barclays' verdict was that the strategy lost money after costs. Run (9.3) the other way: a signal earning 2.5% a year gross at a 0.6% round-trip cost can afford one-way turnover of $(2.5\%/12)/0.6\% \approx 35\%$ a month and no more. Figure 9.3 draws the rule.

![Figure 9.3: At 73% turnover a month the top-decile momentum portfolio's 6.34% gross edge breaks even at a 0.72% round-trip cost, barely above the 0.6% average investment-grade cost of 2018–19 but below the 0.94% of high yield in July 2019 and the 2.8% of 2008, and any cost above the curve turns it negative. Source: equation (9.3) applied to the Barclays figures quoted in §9.4.2 (Dynkin et al., p.633), with the Barclays Liquidity Cost Scores (the cost of an immediate round trip, p.702–703) as the horizontal lines; the dashed 2.5%-a-year curve is the section's worked example.](assets/figures/ch09_breakeven_cost.png)

> **[SOURCE EXTRACTION]** *Dynkin_Systematic_Investing_in_Credit p.633:* "Turnover is very high (73% per month) and performance before transaction costs is also very high (return of 7.31%/yr, or 6.34%/yr in excess of the index, with information ratio of 1.90 over the index) but transaction costs are so large that, once accounted for, both absolute and relative performance becomes negative."
>
> **Annotation.** Ines ran this one as a hand history. Kaz's version of the strategy showed the same pattern on the desk's data: a beautiful gross IR and a monthly bill from the dealers that exceeded it, and her verdict on it is in §9.1. IDO or it didn't happen, and in this case it didn't. The lesson is not that equity momentum fails in credit. It is that momentum in credit cannot be harvested as a stand-alone, high-turnover top-decile portfolio. Barclays' own response, and the 2026 desk's, is to use momentum as one input to a combined score (§9.7), to trade it with a buffer (§9.8) so that a bond sliding from the 95th to the 88th percentile is held rather than sold, and to trade it through portfolio trades and all-to-all protocols where the marginal cost is lower (Chapter 20). Momentum's gross alpha is real. Its *net* alpha is a property of your execution stack.

The other Barclays number that decides momentum's fate is the one the coffee began with.

> **[SOURCE EXTRACTION]** *Dynkin_Systematic_Investing_in_Credit p.610:* "an issuer with equity momentum in the top 10% (D10) has only a 17% probability of remaining top ranked after three months"
>
> **Annotation.** One number fixes three design choices. It fixes the *rebalancing frequency*: a signal with a five-week half-life needs at least monthly rebalancing, and quarterly rebalancing gives away most of the alpha. It fixes the *turnover budget*: by (9.3), a fast signal can be held only if its gross alpha per unit of turnover clears the cost, which in credit is a high bar. And it fixes the *combination weight*: a factor with fast decay deserves less weight in a composite traded slowly. The 2026 refinement is to stop treating the decile as the state. A continuous score with a smooth tilt (rather than in or out of decile 10) lets a portfolio decay toward a signal rather than jump in and out of it, which is the same idea as the buffer in §9.8 written in a nicer language.

Even the definition of the signal is contested, and the contest is a small lesson in how two careful desks can both be right.

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
> which falls as spreads rise whenever the expected-loss share of the spread, $\lambda^{\mathbb{P}}_i L/s_i$, rises with $s_i$. Empirically it does, steeply: in the synthetic universe of §9.11 it is about 4% for single-A and 42% for CCC *(illustrative calibration)*, and the real-world pattern runs the same way. That is the low-risk premium in credit: not a behavioral puzzle but the shape of a capped payoff. Where the modern desk departs from the simple story is leverage. A DTS-neutral low-risk book is long short-dated, high-grade paper levered several times against short long-dated, low-grade paper. In §9.11's synthetic universe the long leg is levered several times over to match the short leg's DTS (the leg-DTS series `dL` and `dS` print the exact multiple). That leverage is the price of the premium, as in Frazzini and Pedersen's (2014) *Betting Against Beta*, and the factor's drawdowns are funding events.

### 9.5.3 Two live reminders that low-risk is a duration bet

Factor returns in this chapter are *excess* returns: duration-matched Treasuries are subtracted, so rates do not enter the factor's return. A client's total-return statement does not subtract anything. The distance between those two statements has a year named after it.

#### Long Scene: 2022, the Year Low-Risk Looked Like Genius

*A replay, Ines's ritual. The cast, their cards, the pension client and its letter are fictional, and the sleeve and its returns are illustrative. The tape is cut at the close of Friday 30 December 2022; index returns, cost evidence and the 2023 and 2026 facts are real and cited where they appear.*

Ines ran it on a Friday at four, which is when she runs the replays she wants people to take home with them.

"Close of business, Friday the thirtieth of December, 2022," she said. "The tape stops there. You know nothing about 2023. You know nothing about anything after New Year's Eve." She handed each of them a single sheet, face down, the way she used to hand out seat assignments.

The year on the sheet was short to describe and long to live through. On 16 March 2022 the Federal Reserve raised rates for the first time since 2018, and then kept raising them, in what BlackRock's high-yield team would later call "the Federal Reserve's fastest rate hiking campaign in decades." By the last trading day of the year the S&P 500 had fallen over 18%, US high yield was down over 11%, and the Bloomberg US Aggregate, the index investors think of as ballast, had fallen over 13% (BlackRock_Systematic_High_Yield_Credit p.3). Nobody's bonds had protected anybody.

"You run a low-risk credit sleeve for a pension client," Ines said. "Long-only, benchmarked to US high yield, built exactly the way §9.5.2 builds it: shorter maturities, higher ratings, low leverage, high profitability. Each rating cell is rescaled so its DTS matches the benchmark's, so the sleeve carries the same spread risk as the index, and the weight left over sits in Treasuries. The spec said Treasuries. It didn't say which, so the sleeve parked the residual in bills."

Theo turned his sheet over. The sleeve had lost about 5% for the year in total return. The benchmark had lost over 11%. Six points ahead, in the worst year for bonds that anyone at the table had traded through.

Stapled to the sheet was a letter from the client's chief investment officer. It was warm in the way such letters are warm when a manager has made a committee look clever. *We have been delighted with the sleeve's resilience in a very difficult year. The investment committee would like to discuss doubling the allocation at its January meeting.*

The last item was the trading log, and it was the only part of the year that had gone worse than expected. Every month the sleeve rebalanced toward its targets, and every month the rebalancing cost more than the model said it should. Man Numeric's credit team described the same weather in their own book a few months later: "transaction costs for portfolio trading generally increased through the first half of the year," higher volatility and quantitative tightening "may also have left dealers inclined to commit less of their balance sheets to bond trading," and "the loss of customised baskets for the ETF creation/redemption process is likely to have been another aggravating factor" (Man_Revolutions_in_Credit_Trading_2023 p.3). In a later talk the same co-heads put it more bluntly, saying in effect that the change to ETF creation and redemption made it harder for the portfolio-trading desks to recycle risk, and that costs went up substantially. The sleeve's cost line for the year was nearly double its 2021 level. Nobody reading the client letter had noticed, because six points of outperformance hides a lot of commission.

Kaz had not said anything yet. Kaz had, without asking, put a second chart on the big screen: the same sleeve, the same year, but measured the way this chapter measures factors, as excess return over duration-matched Treasuries, minus the benchmark's own excess return.

The line was flat. It wobbled a little in June and again in October, when spreads gapped and the sleeve's higher-rated names held up slightly better than their DTS said they should, and it finished the year at about plus a tenth of a percent. You could have levelled a table with it.

Theo looked from his sheet to the screen and back. "One of these is wrong."

"Neither," Kaz said.

Theo did what he would have done with a borrowing-base certificate that did not tie: he wrote down sources and uses. A bond's total return is its excess return plus the return on a Treasury of the same duration. The excess-return chart said the sleeve's credit choices, once the spread risk was matched, had earned almost exactly what the benchmark's had. So the six points had to be in the other line. The sleeve's bonds were short, a couple of years of rate duration against the benchmark's four or so, and the bills had none at all. In a year when Treasury yields at those maturities rose by more than two percentage points, a duration gap of a couple of years is worth several points on its own, and the arithmetic did not need anything else to get to six.

"So the sleeve," Theo said slowly, "is two strategies. A credit one that matched the index. And a rates one that nobody wrote down."

"That's equation (9.4) wearing a client letter," Kaz said. "Per unit of DTS, carry is one over duration. A low-risk sort *is* a duration sort. Measure it in excess returns and the duration is hedged away, and you see the credit part, which is small. Measure it in total returns and you see the duration, which this year was enormous."

Mags had been reading the client letter. She put it down on the desk, face up, and tapped the word *resilience* with her pen.

"You didn't pick credits," she said. "You were short duration in a year the Fed hiked. Send the client a thank-you note to Powell."

"It's a defensive factor," Kaz said. "Some of the six points is defense."

"A tenth of a point is defense. The rest is a rates bet that happened to be facing the right way." Mags leaned back. "A defensive tilt is two bets stapled together. One is credit, and that's the one you get paid for over time. The other is rates, and that's the one you get famous for, until the year it points the other way. Back in my day a fund would have put this year on the cover of its pitch book and then spent three years explaining it."

"So what do I tell the client?" Theo asked.

Ines picked up her coffee. "That," she said, "is the card."

She handed out index cards. *Write three things. What you tell the client the factor earned. Whether you accept the doubled allocation. And how you would hedge the rates leg if you did.*

Write yours before you read theirs.

Theo wrote fast, in the hand he had used for six years of board materials. *Earned: six points ahead of benchmark, mostly from defensive duration positioning; say so plainly. Accept the doubling. No rates hedge: the Fed is still hiking, inflation is still high, and the short duration is working.* It was honest on the first line and a forecast on the third, and he knew it as he wrote it, and he left it.

Kaz wrote: *Earned: +0.1% excess, i.e., nothing distinguishable from zero. Six points of total return came from a duration gap the mandate did not ask for. Decline the doubling until the rates leg is hedged. Hedge: Treasury futures across the curve to bring the sleeve's key-rate durations to the benchmark's, sized monthly from start-of-month durations, residual weight moved from bills to duration-matched Treasuries.*

Mags wrote: *Earned: Powell. Take half the new money, hedged per Kaz. Tell them the half we didn't take was the half that was rates.*

Ines turned the tape forward.

In 2023 high yield returned over 13% and the Aggregate over 5% (BlackRock p.3). The defensive posture that had looked like skill in 2022 gave its lead back to the upside: BlackRock's eVestment numbers show the average US high-yield manager beating its benchmark by 0.47% in 2022 and lagging it by 0.68% in 2023, in a year when the market rose over 13% (BlackRock p.4). The industry had run the same round trip as the sleeve, only with less leverage on the story. For the sleeve itself, 2023 delivered neither the rates rout Theo's card was betting on nor the encore the client was hoping for. Treasury yields climbed into the autumn and came back down by December, ending the year not far from where they began, and the sleeve's six-point lead simply stopped growing on the day yields stopped rising. A committee that doubled in January bought a rates position at the price of a rates position that had already paid.

Then Ines skipped to the present. Robeco's QI Global Multi-Factor Credits fund, the longest live multi-factor record in this chapter, published its attribution as of 30 September 2026. It names the low-risk/quality factor as the largest detractor, "driven by an underweight in longer-dated bonds," as the long end rallied (Robeco fund page). Same tilt, other direction. In 2022 the duration underweight made a defensive book look like genius in total return; in 2025–26 it made a defensive book the biggest drag in its own report. Both are correct readings of a defensive tilt. Neither is the factor premium.

"Grade," Ines said.

"Theo. Line one is right, and I'd frame it. Line three is a rates forecast inside a credit mandate, which is the one bet nobody hired you to make. You were not wrong about 2022. You were wrong about what you are paid for. If the long end had rallied in 2023 the way it did in 2026, your card would have handed the client six points back with your name on it.

"Kaz. Full marks on every line, and you lose the client, because the committee stops reading after the word *nothing*. Your hedge is the right hedge. Your first sentence needs to be one a pension trustee can repeat to another pension trustee.

"Mags. You take the chips, you hedge the part of the pot that isn't yours, and you tell them which part that is. That's the hand."

She turned to the reader's side of the table, which in a replay is everyone who was not in the room. If your first line had a percentage in it and no word *duration* next to it, you wrote the client's next letter for them. If your second line said yes and your third line was blank, you accepted a rates mandate by accident. If your third line named futures sized from the start-of-month key-rate gap and moved the bills into matched Treasuries, you wrote Kaz's card; now rewrite its first sentence for a trustee. And if you priced what it would cost to put the doubled allocation to work, you were the only one at the table who read the trading log. The following April, Jamie Dimon's shareholder letter would say that "many of the new 'shadow bank' market makers are fair-weather friends — they do not step in to help clients in tough times" (JPMorgan Chase 2022 shareholder letter, 4 April 2023, pp. 22–23). That is a dealer bank's view of who else would have been on the other side of the new money, offered by a firm with its own stake in the answer. The cost line was going to scale with the allocation either way.

Ines collected the cards. "Next time anyone on this desk shows a factor number," she said, "the first two words out of your mouth are *excess* or *total*, and the next sentence says who hedged the duration."

## 9.6 Quality, Size, and the Informed Investor

### 9.6.1 Quality is a high-yield factor

Quality in credit means profitability, coverage, low leverage, and, most directly, a low probability of default. Its value depends on where you stand. In investment grade, default risk is too small and too similar across issuers to sort on, and Henke, Kaufmann, Messow, and Fang-Klingler (2020, *Factor Investing in Credit*), as summarized by Man, find quality only weakly related to performance there (Man p.26–27). In high yield, quality is default avoidance, and default avoidance is most of the game: BlackRock reports that its probability-of-default signal identified 77% of the defaulted bonds in the ICE BofA High Yield Index within 24 months of default since 2010 (BlackRock_Systematic_High_Yield_Credit p.6). Chapter 11 builds that engine. One caution on signs: Chordia et al. (2017) find profitability *negatively* related to bond returns unconditionally, which is not a contradiction of Israel, Palhares, and Richardson's positive premium for gross profitability, because they compare bonds *within* DTS quintiles. Unconditionally, profitable issuers have tight spreads and low carry. Within a DTS bucket, a profitable issuer is a safer bond for the same pay.

Ratings-based quality has its own structural flows. When Kaz first heard "fallen angel," they asked which Greek letter it was. Mags explained: "It's the bond an insurance company sells you at 11 a.m. because one policy says it can't hold high yield, and buys back from you at 2 p.m. because another policy says it must hold the index." Index and ratings constraints create forced sellers, and forced sellers create premia that look like factors. Dynkin's Part II covers them; for this chapter, note that a quality factor built on ratings is partly a bet against those constraints.

### 9.6.2 Size, the factor that isn't

In equities, small is beautiful. In credit, small is a bond nobody will quote you, whose price is a rumor, whose return is the rumor's variance.

> **[SOURCE EXTRACTION]** *Dynkin_Systematic_Investing_in_Credit p.679:* "Our findings generally do not support the existence of a size factor that could be exploited by credit investors the same way many equity investors systematically favor smaller‐capitalization stocks with a view to enhance returns."
>
> **Annotation.** This is the one place where the major practitioner sources openly disagree. Barclays says no. Man has "seen little evidence to suggest that Size is a meaningful factor in quant credit, especially after transaction costs" (Man p.26), and Israel, Palhares, and Richardson leave size out because "the corporate bond market is notoriously expensive to trade." Houweling and van Zundert (2017) include it, define it as small issuers by debt outstanding, and find it survives their cost assumptions. The reconciliation is liquidity and data. Small issuers' liquidity cost scores run more than 50% higher than large issuers' (Dynkin p.659), so any premium must clear a higher cost bar. And small, rarely traded bonds have the noisiest prices, which by the Blume–Stambaugh mechanism of §9.9 inflates their measured returns. A size premium measured on noisy month-end marks and charged a large-issuer cost is a premium the desk cannot collect. The 2026 position: treat size as a liquidity exposure to be priced and controlled, not a factor to be harvested, unless your own clean data and your own fills say otherwise.

### 9.6.3 The informed investor

Man's fourth style factor reads positioning rather than fundamentals.

> **[SOURCE EXTRACTION]** *Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.27:* "The Informed Investor style factor looks to exploit information about investor activity to drive investment decisions, working along a 'wisdom of crowds' thesis. This harnesses data points such as short interest and call/put positioning to build a picture of investor activity across markets."
>
> **Annotation.** The canonical inputs are equity short interest (ESI) and bond short interest (BSI):
>
> $$
> \text{ESI}_{j,t} = \frac{\text{shares on loan}_{j,t}}{\text{shares outstanding}_{j,t}}, \qquad
> \text{BSI}_{i,t} = \frac{\text{par on loan}_{i,t}}{\text{par outstanding}_{i,t}}.
> $$
>
> Barclays finds that high equity short interest, within rating, predicts downgrades over the next 3 to 12 months and index underperformance, that bond short interest is subsumed by equity short interest, and that "bond short interest is not a useful indicator in the IG space as IG bonds are likely shorted as part of market‐making activity" (Dynkin p.794). In investment grade, a borrowed bond usually means a dealer sold a client something it did not own, which is information about the dealer's inventory rather than the issuer's prospects. The Bayesian reading links this to Chapter 3's Glosten–Milgrom model: short interest raises the posterior probability that informed traders are present, so the *change* in ESI, not its level, is the news. Man's simulated stand-alone information ratio for this factor is 0.79, the lowest of its four (Man p.28), yet Barclays reports that ESI combined with ESP "achieves almost twice the risk-adjusted return" of either alone (Dynkin p.794). It is a combination factor: weak alone, useful as a filter on value, because it flags the cheap bonds whose equity holders already know why they are cheap.

Mags met bond borrow with the usual war story. "In 1998, shorting a bond meant calling a man named Sal and asking nicely."

Asking nicely had a price, and she itemized it. A bond from Sal cost a favour, repaid later at a moment of Sal's choosing, usually by taking the other side of something his desk could not get rid of. It cost a week, because Sal had to find the bonds in somebody's custody account and the somebody had to say yes. And it came with a recall, which in her experience arrived on exactly the morning the short started working, because the lender had read the same news she had and wanted the bonds back in time to vote them.

"Now your prime broker emails you a spreadsheet every morning." It does: Man notes that prime brokers now provide daily borrow availability across the cash-bond universe (Man p.11). Then she read the spreadsheet. It told her what could be borrowed, how much, and at what fee, today. It did not tell her who else had borrowed the same bonds yesterday, or why, and the fee is the only hint, which is why Chapter 22 treats it as the closest thing credit has to a crowding gauge.

"Fine. The spreadsheet is better than Sal." She put it down. "Sal used to tell you when you weren't the first person to call."

There is a human version of the informed investor, too. Barclays' QPS and credit research teams, as reported by Impax (19 September 2025), found that in US investment grade the issuer-level hit rate rose from about 58% to about 66% when analyst and quant signals agreed and fell to about 52% when they conflicted. Concentrating on aligned decisions lifted excess return from 2.0% to 3.7% a year and the IR from 1.09 to 1.71. Doubling exposure to aligned signals gave 4.1% with an IR of 1.83. The analyst is an informed investor whose positioning you already have access to, if you write it down.

## 9.7 Combining Factors: Correlations, Weights, and Effective Breadth

### 9.7.1 The combination formula

Kaz's instinct, the morning after the cold open, was to throw every row of the factor menu into one score and let diversification do the rest. Ines asked how many rowers the boat could take before it slowed down, which Kaz assumed was a metaphor and which turned out to be arithmetic.

> **Math, Gently.** *Correlation, and two rowers.* Correlation is a number between −1 and +1 that says how much two things move together: +1 is lockstep, 0 is no relation, −1 is one zigging whenever the other zags. In a blend of factors it decides how much of their wobble cancels. Picture two rowers in one boat, each pulling with the same average strength (an IR of 1.0 each), with strokes that wobble at random. If their wobbles are unrelated they partly cancel: the boat gets twice the pull but only $\sqrt{2}$ times the wobble, so the pair's IR is $2/\sqrt{2} = \sqrt{2} \approx 1.41$. If their wobbles are correlated 0.5 they cancel less, the wobble grows to $\sqrt{1 + 1 + 2 \times 0.5} = \sqrt{3}$, and the IR falls to $2/\sqrt{3} \approx 1.15$. Now go back to the uncorrelated pair and add a third, weaker rower, IR 0.2, unrelated to the other two, with an oar the same size as theirs. The pull rises to 2.2, the wobble rises to $\sqrt{3}$, and the boat's IR falls from 1.41 to $2.2/\sqrt{3} \approx 1.27$. He is pulling forward and still slowing the boat down, because at equal weight his wobble costs more than his pull adds. Give him a smaller oar and he helps; the formula next says how small. Chapter 8-B's box on variance adding in quadrature has the long version of the wobble arithmetic.

The whole result, with the optimal oar sizes, is

$$
\text{IR}_{\text{combo}}(w) \;=\; \frac{w^\top \text{IR}}{\sqrt{w^\top \rho\, w}}, \qquad
w^{\ast} \;\propto\; \rho^{-1}\,\text{IR}, \qquad
\text{IR}_{\text{combo}}(w^{\ast}) \;=\; \sqrt{\text{IR}^\top \rho^{-1}\,\text{IR}} \;\ge\; \max_k |\text{IR}_k| , \tag{9.5}
$$

where $\rho$ is the factor correlation matrix. The optimal blend never loses to its best single factor in-sample. Equal-risk weights $w = \mathbf{1}/K$ carry no such promise: with three uncorrelated factors of IR 3.0, 0.5, and 0.5, the equal-risk combination has IR $4/\sqrt3 = 2.31$ and loses to the best single factor, which is the box's third rower at a larger scale. Equal weights earn their place when the component IRs are similar and the correlations low, because then the estimation error in $\rho^{-1}\text{IR}$ would cost more than its precision buys. When one factor is much stronger than the rest, the optimal weights pay for themselves, and the desk shrinks them toward equal weights because both inputs are estimated with error.

#### The Full Derivation

Scale each factor's return series $f_{k,t}$ to unit volatility, so its mean is its information ratio $\text{IR}_k$. A combination with weights $w$ has mean $w^\top \text{IR}$ and variance $w^\top \rho\, w$, so its information ratio is $\text{IR}_{\text{combo}}(w) = w^\top \text{IR} / \sqrt{w^\top \rho\, w}$. The ratio does not change when $w$ is scaled, so maximize $w^\top \text{IR}$ subject to $w^\top \rho\, w = 1$. The Lagrangian's first-order condition, $\text{IR} = 2\nu\,\rho\, w$ for a multiplier $\nu$, gives $w^\ast \propto \rho^{-1}\text{IR}$, and substituting back gives $\text{IR}_{\text{combo}}(w^\ast) = \sqrt{\text{IR}^\top \rho^{-1}\,\text{IR}}$. The inequality in (9.5) follows from Cauchy–Schwarz and holds in-sample for the optimal weights; the plain-language version is that putting all the weight on the best factor is one of the choices the optimizer could have made, so its optimum can do no worse. It does *not* hold for equal-risk weights.

Run the formula backward on published numbers. Israel, Palhares, and Richardson's quintile-spread Sharpe ratios are carry 0.35, defensive 1.11, momentum 0.85, and value 1.75, and their equal-risk combination is 2.19. With four equal weights, $2.19 = 4.06/\sqrt{4 + 12\bar\rho}$ implies an average pairwise correlation $\bar\rho \approx -0.05$. Man's simulated IRs (Value 2.15, Momentum 1.69, Quality 1.55, Informed Investor 0.79, Final 2.35; Man p.28) imply $\bar\rho \approx 0.24$ under the same equal-risk assumption. Treat both as back-of-the-envelope figures, since neither firm necessarily combines at the return level with equal weights. The direction still teaches something: diversification across credit factors is real but not free, and the correlations that matter are the ones *after* DTS neutralization. The pairwise matrix from Henke et al. that Man reproduces for investment grade (Man p.27) shows the expected structure: Value–Carry +0.52 (two spread-adjacent sorts), Value–Momentum 0.00, Value–Quality −0.04, Value–Size −0.10, Momentum–Quality −0.07, Momentum–Carry +0.02, Quality–Carry −0.21. Figure 9.4 plots equation (9.5) for both sets of published numbers.

![Figure 9.4: An equal-risk blend of four factors beats the best single one only while their average correlation stays below about 0.12 for the Israel–Palhares–Richardson set and about 0.36 for Man's, and the published blends sit at correlations of −0.05 and 0.24. Source: the Sharpe and information ratios quoted in §9.7.1 (Israel, Palhares, and Richardson, 2018, Table 4, quintile spreads, January 1997–April 2015; Man Group, 2022, p.28, simulated back-test, January 2005–December 2020; both before trading costs), with the curves from equation (9.5) for equal weights and one common pairwise correlation.](assets/figures/ch09_equal_risk_vs_best_single.png)

> **[SOURCE EXTRACTION]** *Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.28:* "These results do not directly account for liquidity, transaction costs, and borrow costs."
>
> **Annotation.** This footnote sits under the chart showing a combined IR of 2.35 (simulated, January 2005 to December 2020), and it deserves equal billing with the chart. Every IR in §9.7.1 is gross. Combination changes the cost picture in two directions. It helps, because trades net out: when momentum wants to sell a bond that value wants to buy, the combined portfolio does nothing, and doing nothing is free. It hurts if it raises the weight on fast signals. The correct object is therefore not $\text{IR}_{\text{combo}}$ but the IR of the *traded* combined portfolio after the optimizer of §9.8 has priced every trade. A desk that combines gross IRs and then applies an average cost has assumed the netting away.

### 9.7.2 Effective breadth: forty-seven hats again

By the fundamental law, $\text{IR} \approx \text{IC}\sqrt{\text{BR}}$: skill per bet times the square root of the number of independent bets, which Chapter 4 derives with issuer clustering and Chapter 7 dresses in hats. In credit, breadth is not the bond count. With $N$ bonds from issuers holding $\bar n$ bonds each, and within-issuer return correlation $\bar\rho_w$,

$$
\text{BR}_{\text{eff}} \;\approx\; \frac{N}{1 + (\bar n - 1)\,\bar\rho_w}.
$$

Man's universe of more than 10,000 bonds from about 2,000 issuers (Man p.10–11) has $\bar n \approx 5$. At $\bar\rho_w = 0.8$, effective breadth is $10{,}000/4.2 \approx 2{,}400$ per cross-section, not 10,000: forty-seven bonds from one issuer are one data point wearing forty-seven hats (Chapter 7). That is still an enormous advantage over CDS, where only around 100 US single names trade regularly (Man p.10–11), and it is the reason serious credit factor investing is done in cash bonds. Bond-level value (§9.3.4) is the one signal that recovers some of the lost breadth, because it is the one that differs across an issuer's bonds.

Hats are not only a bond-level problem. They can be sewn into a book of trades that each look independent.

*Dov Adler's pod and the Vantress platform are fictional composites, and the loadings and shares below are illustrative; the factor definitions are this chapter's.*

On the last Tuesday of September, Marcus Oyelaran, the platform's risk manager for the credit pods, ran the overnight x-ray on Dov Adler's Pair Book a second way. The usual way regresses the pod's P&L on CDX HY and the rate curve and asks what the book is long that it did not mean to be. On that test Dov's dozen pairs passed, as they always did: each was matched on market-value DTS leg by leg, so the hedge had removed the market. The second way regressed the same P&L on five of this chapter's factors, each built DTS-neutral: value, momentum, carry, low-risk and quality.

The value loading came back at 0.7. Marcus walked the sheet over himself, which on a platform is how you know a number is serious.

"Twelve pairs," he said. "Twelve theses, each a sentence with a date in it. In every one of them the long leg is the cheaper name in its cell on spread per turn of leverage." He let Dov read it. "You don't have twelve views. You have one view, twelve times. It's a value factor with extra steps."

Nobody had noticed because cheaper is not the same as wider. In Kestrel against Halvorsen, the book's anchor pair, the long leg is the *tighter* bond; it is cheaper per turn of leverage, which is exactly what a value sort would have bought. Dov read his thesis sentences down the page. Every one was a reason the cheaper credit deserved a better price, and none of them said so.

The arithmetic of isolation was now explicit. The DTS hedge had removed the market. It had not removed the factor, so on any month the value factor lost, all twelve residuals would lose together, and the book's effective breadth on that axis was one hat. What idio remained once the value loading was taken out was about a third of the book's P&L variance on Marcus's sheet. What leaked was the rest, and it leaked through the one door the pod could not lock with a CDX trade, because nobody sells a short position in a credit value factor for a few basis points. Neutralising it meant resizing pairs against the value score, which gives up expected P&L while the financing on the longs and the borrow fees on the shorts keep running on whatever gross remains; admitting it meant the platform would charge the loading as factor risk, at the price of something it could buy elsewhere for less.

Dov did both. He kept full size on the four pairs whose thesis really was cheapness and said so in their ledger lines, and he cut the other eight until the book's value loading read 0.2. The platform, as Chapter 8 §8.8 and Chapter 28 argue at length, pays for the residual. It is not in the market for its own factors sold back to it.

### Case Study: One Telecom, Four Factors (Man Numeric, 2016–2017)

Man's paper includes the only shelf example that shows the four style factors disagreeing and then agreeing on a single issuer, an anonymized telecom (Man p.29–30). In 2016 the company stabilized customer retention, relieved liquidity concerns, and announced about \$500mm of cost cuts. In 2017 it reached free-cash-flow breakeven, with EBITDA margins rising from about 25% to about 30%. The signals moved in sequence. Value and quality strengthened from distressed levels first: the spread still priced a credit the fundamentals no longer described. The informed-investor signal turned cautiously positive as bond and equity short interest fell. Cross-asset momentum turned positive as the equity began to rerate. The combined signal went from strongly positive to *monetizing* as the bond's OAS travelled from roughly 1,200bp toward the tights *(approximate, read from Man's chart)*.

Read it as an RSSG reader would. Each signal is a witness who saw a different part of the event. Value saw a balance sheet that was better than its price. Quality saw margins. Informed investor saw the shorts leave. Momentum saw the equity market agree. No single witness justified a full position at 1,200bp; together they did, and the position was sized up as they agreed and sold as the spread compressed and the value signal faded. Two facts keep the example honest. It is a backtest narrative of a winner, chosen by the author after the fact. And at 1,200bp the bond was in the zone where §9.2 says DTS stops being a good risk measure, so a desk would have sized it on price and recovery rather than DTS. Section 9.10 pairs it with two dated, named, live results.

## 9.8 Portfolio Construction Under Costs

Four witnesses agreed on the telecom, and the position was still a trade somebody had to execute at 1,200bp, in size, through a dealer who could see it coming. The signal tells you what you would like to own. Construction tells you what you can afford to own. In credit the second question is the larger one.

### 9.8.1 The optimizer

Let $w$ be portfolio weights, $w_0$ current holdings, $\alpha$ the combined expected active return, $\Sigma$ a covariance matrix, $\gamma$ risk aversion, and $c_i$ the one-way cost of trading bond $i$. The construction problem is

$$
\max_{w}\;\; \alpha^\top w \;-\; \frac{\gamma}{2}\, w^\top \Sigma\, w \;-\; \sum_i c_i\,\lvert w_i - w_{0,i}\rvert
$$

subject to constraints that, on a real desk, arrive one person at a time. Collected in one place, with who owned each on the morning described below:

| Constraint | Form | Who owned it | Source |
| :--- | :--- | :--- | :--- |
| DTS cell matching | $\sum_{i \in g} w_i\,\text{DTS}_i = \text{DTS}^{\text{bm}}_g$ for every rating × sector cell $g$, so active bets are expressed as DTS contributions; in practice a band around the target | The risk manager | Ben Dor p.33–34 |
| Key-rate durations | Matched to the benchmark, so that rates do not leak into an excess-return mandate | The rates desk | Man p.10 |
| Issuer cap in DTS | $w_j D^{\text{spr}}_j s_j \le \kappa$ | Theo, reading Ben Dor aloud | Ben Dor p.61 |
| Share of issue outstanding | No more than a few percent of any one tranche | Theo | Desk rule *(illustrative)* |
| Liquidity | Barclays' Trade Efficiency Score TES ≤ 3, the more liquid end of its scale | The trader | Dynkin p.710 |
| Minimum ticket and lots | No ticket below the desk's minimum; trades rounded to tradeable lots | The trader | Desk rule |
| Turnover | $\tfrac12\sum_i \lvert w_i - w_{0,i}\rvert \le \text{TO}^{\max}$, for example 10% a month as in Israel, Palhares, and Richardson | The client's investment agreement | Israel, Palhares, and Richardson (2018) |
| Long-only | $w \ge 0$ where the mandate requires it | Compliance | Mandate |
| Borrow (long–short books) | Short only what the prime broker shows as available, at a fee the alpha clears | The borrow sheet | Man p.11 |
| Cash and financing | A cash buffer for client flows; financing for any levered long leg | Operations | Desk rule |

*The desk's fictional paper rebalance; the numbers are illustrative.*

Kaz ran the optimizer on the rebuilt value book with nothing but the objective and a budget, the way a cook tastes a sauce before seasoning it. The first answer was what first answers always are. It put 9% of the book in one BB chemicals issuer whose residual was the widest in the universe, spread most of the rest across fourteen CCCs, ran two years short of the benchmark's rate duration, and turned over 64% of the book in a month.

The risk manager vetoed it in a one-line email: active bets are DTS contributions, cell by cell. Kaz pinned every cell to its benchmark DTS exactly, and the problem went infeasible on the spot, because a long-only book cannot hit an exact DTS target in a cell of six bonds, two of which fail the liquidity screen. So the cells became bands, and the order in which bands widen and thin cells pool when the problem is infeasible went into the spec in writing, so that the optimizer would never again decide it alone and in silence.

Theo read the issuer cap out of Ben Dor aloud, because it was the first optimizer constraint he had met that a restructuring banker might have written himself. Under a cap on DTS contribution, an issuer with a 100bp spread and five-year duration "could be up to 1% of portfolio market value," while one with a 150bp spread and ten-year duration "would be limited to 0.33%" (Ben Dor p.61). A cap measured in risk, not in dollars. Then he added one of his own, on the share of any single tranche the desk could own. "Hold more than a third of a class and you can block a plan," he said. "Then everybody wants to have lunch with you, and you can't sell anything until they've finished eating."

Ines, reading the trade list as the trader who would have to execute it, found a \$340,000 ticket in a bond that trades in millions. An odd lot prices off nothing on the screen, and the optimizer had computed its cost as if it were a round lot. Two lines further down, the optimizer wanted 4% of the book in a new issue. "You'll be allocated a fifth of what you ask for," she said, "and the syndicate desk will remember that you asked." The optimizer's cost term, she added, had been told that $c_i$ was a number. It is a function of the ticket's size and the month's regime, and §9.10 shows what it does in a bad month.

The client's agreement capped turnover at 10% a month, and here Kaz asked the most useful question of the morning: what is that cap costing us? The way to answer it is to soften the constraint into a penalty with a price per unit of turnover and read off its shadow price, the gain in expected return from one more point of allowed turnover. A small shadow price means the cap is cheap insurance against the desk's own enthusiasm. A large one is a conversation to have with the client, with a number in hand. Chapter 12 uses the same vocabulary for the shadow price of an illiquid-asset cap (§12.7), and the two numbers belong on the same page of a committee pack.

The final answer looked like a portfolio a person would own, and it kept about a third of the first answer's expected alpha. That is the price of being able to trade it.

One piece of the objective still needs a trick before a solver will touch it.

> **Math, Gently.** *The hinge.* The absolute value $\lvert x\rvert$ has a kink at zero, like a door hinge, and solvers that slide smoothly downhill catch on kinks. Write every trade as a buy part and a sell part, both non-negative: a sale of 3 is $u^{+} = 0$, $u^{-} = 3$, and then $\lvert x \rvert = u^{+} + u^{-}$ is a straight line in each piece, so the hinge disappears and an ordinary quadratic-programming solver takes over.

The absolute-value cost term makes the objective non-smooth. The standard fix is to split each trade into a buy and a sell, $w = w_0 + u^{+} - u^{-}$ with $u^{\pm} \ge 0$, so that the cost becomes the linear term $\sum_i c_i(u^{+}_i + u^{-}_i)$ and the problem is a quadratic program. For $\Sigma$, Man's approach normalizes bond returns by DTS, extracts statistical factors, fills new issues from issuer-level loadings, and rescales by current DTS (Man p.15). With ten thousand bonds and two thousand issuers, an unshrunk $\Sigma$ invites the optimizer to find the eigenvector with the smallest estimated variance and put the whole book in it, which is why the desk shrinks it first (Chapter 8).

### 9.8.2 What a trade costs

*A fictional morning at a systematic asset manager across town, a composite; the bond, the sizes and the fills are invented.*

At 8:10 on a Wednesday the rebalance file lands in the execution trader's queue, and its largest line is a sale: \$20mm of a seven-year BBB industrial the model no longer likes. She has three ways to do it and about twenty minutes to choose. She can call one dealer and offer the block, which is quick and private and priced by someone who knows she has to sell. She can slice it into pieces and send each to a different venue and protocol, which is cheaper on average and tells everyone watching the prints what she is doing. Or she can tuck it into the afternoon's portfolio trade, where it vanishes among two hundred other lines and is priced as part of a basket. The pre-trade cost model gives her three numbers. She slices, and spends the rest of the morning reconciling fills against the estimate, because two of the five pieces went out "if filled" and came back unfilled, leaving the fund still long \$7mm of a bond its own model had sold.

That routine is most of the job now. Man Numeric's credit co-heads reported moving from roughly 30% of their order flow in high yield and 60% in investment grade through electronic venues to over 90% (Man_Revolutions_in_Credit_Trading_2023 p.3, as of 1 May 2023), with "the vast majority of our trades" sent as RFQs (p.5); in a 2024 talk they described the daily decision as one of venue, protocol and touch, high or low, with some days on which voice still wins. Their firm's earlier paper had already named the unfilled piece for what it is: "it is something of an indictment of the market that there exists the notion of 'if filled' trades" (Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.19).

> **View From Another Seat.** *The dealer who receives the RFQ.* From the other side of the screen, the 8:10 sale looks different. A dealer answering a systematic manager's RFQ knows three things the manager would rather the dealer did not. The order is one of hundreds the manager will send this month, so it is small relative to the dealer's day. It is in competition with several other dealers, so winning it is a mild warning in itself. And it is predictable: a momentum or value book that sold this name today will very likely sell its cousins tomorrow, which is Ines's cold-open point seen from the chair that profits from it. Man describes the buy side's frustration in its own words: bid and ask prices "are indicated by dealer runs that are not firm and actionable" (Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.19). To the dealer, a run that is not firm is not a defect. It is an advertisement, and the RFQ is the moment the advertisement gets priced against the dealer's inventory and whatever the dealer has learned about who else is selling. "If filled" is, from that seat, an option the dealer keeps: the right not to trade when the inventory or the information says no. The cost model on the manager's screen is an estimate of how that option will be exercised.

Barclays' cost measure, which every factor desk in this chapter borrows, starts from the dealer's quote and stops before the dealer's option.

> **[SOURCE EXTRACTION]** *Ben_Dor_Quantitative_Credit_Portfolio_Management p.118:* "A bond's LCS, therefore, represents the roundtrip cost, as a percent of the bond's value, of immediately executing a standard institutional transaction."
>
> **Annotation.** For a spread-quoted bond, Barclays' liquidity cost score is the bid–ask spread *in spread terms* times OAS duration, $\text{LCS}_i = (\text{ask} - \text{bid})_{s}\times D^{\text{OAS}}_i$; for a price-quoted bond it is $(P^{\text{ask}} - P^{\text{bid}})/P^{\text{bid}}$ (Ben Dor p.118). The one-way cost in the optimizer is $c_i = \tfrac12\text{LCS}_i$. Notice the duration in that formula: an 8bp bid–ask on a 15-year bond costs more than an 8bp bid–ask on a three-year bond, so long-duration bonds are expensive to trade for the same reason they are risky to hold. Two features of the 2026 desk go beyond the definition. First, LCS measures the cost of a *standard* institutional trade; a \$50mm block of a \$300mm issue is not standard, and Man's decomposition, "TC = Inside Market Spread + Slippage + Spread Calibration" (Man p.21), adds the size and market-impact terms that LCS leaves out. Second, credit fills are probabilistic. An RFQ may go unfilled, and an unfilled order leaves an exposure the optimizer did not plan (Man p.19). The construction loop must re-optimize on what was actually filled, not on what was sent.

### 9.8.3 Buffers: doing nothing on purpose

A turnover buffer is hysteresis. Buy a bond when its score rises above $\theta_B$; sell it only when the score falls below $\theta_S < \theta_B$; hold it in between. A bond that slides from the 95th percentile to the 88th is held, not sold and replaced with a slightly better one at the cost of two bid–asks. Barclays shows the gross cost of the buffer honestly: the IR falls from 1.52 to 1.31 to 1.20 as the buffer widens from 0 to 10% to 15%, *before* transaction costs (Dynkin p.538). After costs, the picture improves, because the buffer removes the trades whose expected alpha was smaller than their cost. The code in §9.11 reproduces both effects.

> **[SOURCE EXTRACTION]** *Dynkin_Systematic_Investing_in_Credit p.711:* "Accounting for the rebalancing costs reduces relative returns from 2.66%/yr to 1.78%/yr, while the tracking error volatility remains virtually unchanged at 1.41%/yr."
>
> **Annotation.** This is a liquid ESP-plus-EMC strategy portfolio, and the arithmetic is the chapter in miniature: about a third of the gross outperformance goes to the dealers, and the risk is unchanged, so the IR falls by a third too. The more striking number sits on the same page: the cost drag was about 1.15% a year in 2007–2012 and about 0.64% a year in 2013–2019. The cost of running the same strategy fell by nearly half in a decade, which is why systematic credit grew when it did. For the long-only case, Israel, Palhares, and Richardson's optimized portfolio with turnover capped at 10% a month earned 5.72% a year gross and 5.26% net, with an active net return of 2.20% a year, tracking error of 2.56%, and an IR of 0.86. It had a net Sharpe ratio of 1.03 against the benchmark's 0.69. These numbers are achievable, and none of them looks like the cold open's 1.9.

Put Barclays' two decades of cost numbers next to Robeco's live one and the curve is worth seeing whole, including the year it went the wrong way.

> **Trend Watch.** *The cost curve, 2007–2026.*
>
> - **2007 (the academic baseline).** Chen, Lesmond, and Wei (2007) estimated bid–ask spreads of about 25bp for AAA bonds and 180bp for CCC. Man notes that "Both of these figures would be markedly tighter in the current market," yet academic papers still use them (Man p.20).
> - **2007–2019 (Barclays LCS, investment-grade index average).** 0.4% in 2007, 2.8% in 2008, then down to 0.6% in 2018–2019 (Dynkin p.703). In July 2019: IG 0.608%, HY 0.941%, Treasuries 0.028% (Dynkin p.703).
> - **2007–2012 versus 2013–2019.** The cost drag on Barclays' liquid ESP+EMC strategy fell from about 1.15% a year to about 0.64% a year (Dynkin p.711).
> - **February–March 2020.** Man's 20-day average high-yield bid–ask spread spiked and then normalized within months (Man p.20; levels are shown only in a chart, so we describe the shape, not the numbers).
> - **2023–2026 (live).** Robeco's Multi-Factor Credits fund reports realized transaction costs of 0.20% a year, as a three-year average to 30 September 2026 (fund page).
>
> *What it means for the desk.* The cost of trading credit factors fell by roughly half per decade, but not monotonically: in a stress episode it can rise several-fold within months (Barclays IG LCS: 0.4% in 2007, 2.8% in 2008). Construction must use a *state-dependent* cost (LCS today, not the average), and the turnover budget must be set for the stress state, because that is when the signals fire hardest.

## 9.9 The Replication Debate, Read as a Desk

Chapter 7 told the 2019–2026 story in full: the Bai–Bali–Wen (2019) factor model, its retraction after Dickerson, Mueller, and Robotti found a timing misalignment in the data, Dick-Nielsen, Feldhütter, Pedersen, and Stolborg's finding that only 23% of significant literature factors keep significant alphas in a clean framework, and Dickerson, Robotti, and Rossetti's April 2026 audit of 108 signals, most of which have no bond-CAPM alpha after correction. When Kaz learned that the benchmark paper behind half their reading list had been retracted, they asked whether a journal could file under Chapter 11. Mags said, "It did an out-of-court restructuring. The creditors were Dickerson, Mueller, and Robotti." (No cooperation agreement was signed, so the counter does not move.) Here we need only the mechanics that matter for constructing factors.

> **Math, Gently.** *Two ways a backtest flatters itself.* **Part one: Jensen, for a bad mark.** Suppose a bond's true price is 100 and its month-end mark is wrong by 10% at random, half the time 110 and half the time 90. The average mark is 100, exactly right. But a return is the next price divided by this one, so what the calculation really averages is one over the mark, and the average of $1/1.1$ and $1/0.9$ is $(0.9091 + 1.1111)/2 = 1.0101$, not 1. The error averages to zero; its reciprocal averages to about $1 + \sigma^2$, here $1 + 0.1^2$. The average of the reciprocals is bigger than the reciprocal of the average (Jensen's inequality, for any curve that bends upward the way $1/x$ does), and the backtest pockets the difference as return that nobody earned. **Part two: false discovery.** Test 100 signals that are all useless at the usual 5% threshold and about five of them will pass by luck. Report only those five and you have a factor zoo. Dickerson, Robotti, and Rossetti tested 432 specifications of 108 bond signals; after a false-discovery cut that keeps the expected share of lucky winners small, 26 survived, and 25 of the 26 were within-firm sorts, which compare bonds of the same issuer with each other (their Internet Appendix IA.3). Chapter 7's lottery box walks through the procedure; the formula for the first trap is next.

In symbols, the first trap is

$$
\mathbb{E}\big[\tilde r_{t+1}\big] \;\approx\; \mathbb{E}\big[r_{t+1}\big] \;+\; \sigma_u^2 , \tag{9.6}
$$

where $\tilde r$ is the return computed from noisy prices and $\sigma_u$ is the size of the pricing error. The second trap comes from the same error appearing twice, in the signal with a plus sign and in the next return with a minus sign, so that a sort on a noisy price buys the error and then collects its correction. Both are derived next.

#### The Full Derivation

**Mechanism 1: noisy prices raise average returns.** Let the observed price be $\tilde P_t = P_t(1 + u_t)$ with $u_t$ independent over time, $\mathbb{E}[u_t] = 0$, and $\operatorname{Var}(u_t) = \sigma_u^2$. The computed return is $\tilde r_{t+1} = (1 + r_{t+1})\,(1+u_{t+1})/(1+u_t) - 1$. Because $\mathbb{E}[1/(1+u_t)] \approx 1 + \sigma_u^2$ by a second-order expansion,

$$
\mathbb{E}\big[\tilde r_{t+1}\big] \;\approx\; \mathbb{E}\big[r_{t+1}\big] \;+\; \sigma_u^2 ,
$$

which is the bias identified by Blume and Stambaugh (1983, *Biases in Computed Returns*). At $\sigma_u = 3\%$, a plausible pricing error for a small, rarely traded high-yield bond, the bias is 9bp a month, about 1.1% a year, earned by whoever sorts toward noisy bonds. That is the size factor of §9.6.2 explained without any economics.

**Mechanism 2: sorting on a noisy price manufactures a premium.** To first order, $\tilde r_t \approx r_t + u_t - u_{t-1}$ and $\tilde r_{t+1} \approx r_{t+1} + u_{t+1} - u_t$, so

$$
\operatorname{Cov}\!\left(\tilde r_t,\, \tilde r_{t+1}\right) \;\approx\; \operatorname{Cov}\!\left(r_t,\, r_{t+1}\right) \;-\; \sigma_u^2 .
$$

The same error $u_t$ appears in the signal (with a plus sign) and in the next return (with a minus sign). Sort on last month's noisy return and you buy bonds whose price was marked too low; their next return recovers the error, and you call it short-term reversal. Sort on a noisy *price level* (any value signal that uses a price-implied spread) and the same thing happens: a bond that looks cheap because of a bad mark "earns" the correction. Dickerson, Robotti, and Rossetti call this correlated errors-in-variables: the error sits in both the sort and the return denominator. In the §9.11 lab, a lag-one reversal sort on noisy prices shows a large, highly significant "alpha" that disappears once the signal skips a month. Figure 9.5 runs the experiment in miniature.

![Figure 9.5: Independent pricing errors alone lift the average computed return by σ_u² a month (left), and a reversal sort on last month's computed return then earns about 1.1% a month on returns that have no reversal in them, while a sort that skips a month earns nothing (right). Illustrative: the §9.9 price-noise model, with true monthly returns i.i.d. with mean 0.4% and standard deviation 3%, pricing error σ_u = 1% in the right panel, 1,000 bonds, about 240 months and decile long–short sorts; error bars are ±2 standard errors.](assets/figures/ch09_noisy_price_premium.png)

#### Filters, survivors, and the build that went red

**Mechanism 3: filters that peek, and defaults that vanish.** Dropping returns above some threshold, or dropping "bounce-backs" that reverse within days, is conditioning on the future when the filter is applied after seeing the return. Dropping defaulted bonds removes the left tail of exactly the high-carry, high-value portfolios. Both make factors look better than any portfolio could have done.

What survived the cull is small but not zero, and it matches what practitioners actually run: equity-derived signals (momentum spillover, profitability and quality), value built on clean prices with DTS control, and low-risk or short duration. What died was mostly built on noisy price levels: short-term reversal, naive illiquidity, and "downside risk" measured from bond return histories. The academic retreat and the desk's practice turn out to be the same conclusion, reached from opposite ends. Dickerson, Julliard, and Mueller (2026, *The Co-Pricing Factor Zoo*) add the deeper point: once Treasury term-structure risk is priced, equity and nontradable factors explain bond premia, which makes much of the separate bond-factor literature redundant for pricing, although a model-averaged stochastic discount factor over dozens of factors still reaches an out-of-sample Sharpe ratio of 1.5–1.8.

*A fictional week at a systematic asset manager: the desk's own week, with its people, the signal and the timings invented. Open Bond Asset Pricing's pipeline details and the SEC's Two Sigma order are public facts.*

The continuous-integration job that guards the desk's factor library has a name nobody chose, `obap_repro`, and a schedule nobody remembers agreeing to. Every night, and every time anyone proposes a new signal, it rebuilds the four corrected Bai–Bali–Wen factors that Open Bond Asset Pricing publishes and compares the desk's numbers with the public ones to the fourth decimal. Kaz wrote it the week the project launched and has maintained it since the way people maintain a smoke alarm, which is mostly by being annoyed at it.

Monday was the boring part, and Theo, who had asked to "see how the factor library works," got all of it. The public pipeline has five stages. Stages 0 and 1 run on WRDS, because they need the licensed TRACE, FISD and ratings files; stages 2 to 4 run locally. The public Stage 1 download leaves the rating columns out, so the job pulls ratings from the desk's own WRDS subscription and joins them back on, and most of Monday morning went into a join that had silently dropped every bond whose issuer had changed its name since 2019. End to end the run takes about five hours and about five gigabytes. The job pins the pipeline at v4.2.1, the September 2026 release, because the code is still changing and the paper behind it is still under review; an unpinned run would have upgraded itself overnight and failed for a reason that had nothing to do with anybody's signal. Theo asked why anyone would sit through five hours to reproduce numbers somebody else had already published. Kaz said that was the point: if the desk's plumbing could not reproduce a public, corrected factor, nothing it said about a private one was worth reading.

On Tuesday the job went red.

The proposal was Hana's, a short-term reversal signal on high-yield bonds sorted on last month's return, with a backtest that made a quiet room of people lean toward a screen. It earned about 1.1% a month. The job runs every candidate through two gates before it gets near the library. The first is the replication check, which passed. The second is a placebo: the same signal run on the lab's simulated universe of §9.11, where true returns are drawn independently each month with no reversal in them and month-end prices carry 1% of random marking error. A real reversal signal has nothing to find there. Hana's found about 1.1% a month, the right-hand panel of Figure 9.5. The build log said, in red, that the signal's alpha in a world with no alpha was indistinguishable from its alpha in the real one.

It took her twenty minutes to find the cause, which is fast. The signal had been computed from the month-end price, and the return it was graded on had been computed from the same month-end price. A bond marked too low on the last day of the month looked like a loser, got bought, and "earned" its correction the next month. Mags's question from the cold open, who made the marks, had just been answered by a build server. With a month skipped between the signal's price and the return's price, the alpha fell to nothing.

Theo had been reading over her shoulder. "Why wasn't the test written before the signal?" he asked. "At PJT nobody built the model first and decided afterwards what a covenant breach looked like."

Kaz answered with a public document instead. On 16 January 2025 the SEC announced settled charges against Two Sigma. According to the SEC, employees had identified model vulnerabilities in or before March 2019, the firm waited until August 2023 to address them, and it had failed to supervise an employee who made unauthorized changes to more than a dozen models; the firm agreed to a \$90 million penalty and had repaid \$165 million to affected funds and accounts. "Read it as a story about a ticket," Kaz said. "Something known, sitting in a backlog for four years. The test exists so that the ticket doesn't."

On Wednesday Hana rebuilt the signal with a skip month. It earned nothing, and she logged it next to the original, because the desk keeps its failures in the library too. On Thursday nobody touched the job and it ran green: five hours, five gigabytes, four factors to four decimals. On Friday Kaz wiped the whiteboard beside the build monitor and wrote five lines on it, and nobody has erased them since:

1. **Signal and return never share a price.** A different source for each (a composite mid for the signal, executable levels for the return), or a month skipped between them.
2. **No ex-post filters.** Cleaning rules are written before the returns are seen, and extreme outliers are reviewed one at a time, never dropped automatically.
3. **Defaults stay in.** The default-month return is recovery minus the last price, and the bond leaves the panel the following month, never retroactively.
4. **Double-sort on DTS or rating.** Every factor is reported within DTS buckets or rating groups, so beta cannot pose as alpha.
5. **Replicate in continuous integration.** Open Bond Asset Pricing (launched November 2025) publishes cleaned TRACE panels, the 108-signal set, and corrected Bai–Bali–Wen factors, and the library reproduces those public series as an automated test before anyone trusts it with a new signal.

## 9.10 Crowding, Capacity, and the Drawdowns That Matter

> **[SOURCE EXTRACTION]** *Paleologo_Advanced_Portfolio_Management p.71:* "If you think of the extreme case in which every hedge fund holds a copy of the same portfolio, then this factor is a measure of “crowding”."
>
> **Annotation.** Paleologo is describing an equity factor built from hedge-fund holdings, and the next lines on his page describe the deleveraging cycle: consensus positions are bid up in calm markets, and when an adverse shock forces some holders to sell, prices fall, others' risk limits are hit, and the selling feeds on itself. Credit adds two accelerants. Long–short credit books run leverage that, in Man's words, "starts at 4-5x" (Man p.11), so a modest loss forces a large sale. And the exit is narrower: a crowded equity factor sells into an exchange, while a crowded credit factor sells into dealer balance sheets that shrink in exactly the same stress. The 2026 desk measures crowding directly rather than waiting to find out. Useful measures (all ours, numbers illustrative): holdings overlap with known factor ETFs and published model portfolios; a *factor valuation spread*, the ratio of the average spread of the cheap leg to the rich leg within DTS-matched cells, which compresses as a value trade gets crowded; short interest in the bonds and stocks of the short leg; and the share of TRACE volume concentrated in top-decile names. Robeco's credit team put the intuition plainly in its *Guide to Credits* (c. 2017): it is "wary of crowded trades where investors stretch the models."

Ines, who had played enough tournaments to know what a crowded exit looks like, put it more simply.

> **Poker Table.** Ines drew it on a napkin. "Four players. Same hand history, same model, same stack, same rule: if you're down two percent, you fold. One of them gets a bad card. He folds. His fold moves the pot against everyone else, and now they're all down two percent." She pushed the napkin across. "Everyone at this table has the same exit. That isn't an edge, it's a fire drill. Your edge is knowing where the door is before they do, or not being at the table."

### Case Study: March 2020 Through the Factor Lens

Ines's napkin describes a fire drill in the abstract. The desk ran a real one.

#### Long Scene: March 2020, the Factor Book in a Fire Drill

*A replay, Ines's ritual. The desk's factor book, its positions and P&L, and the cast's cards are fictional and illustrative. The tape is cut at the close of Thursday 19 March 2020; dated market facts are real and cited where they appear. Chapter 1's quarterly replay of the same month (§1.8.2) followed the forced sellers and Chapter 20 (§20.5) owns the ETF-discount timeline, so this one follows only the factor book.*

"We did March," Mags said, when Ines wrote the date on the whiteboard.

"We did the sellers," Ines said. "Today we do the factor book. Same month, different seat. Close of business, Thursday the nineteenth of March, 2020. The tape stops there."

**The book.** She dealt it out on one sheet. The desk was running the strategy the cold open had turned into: a composite of ESP value and equity momentum, long the top of the score and short the bottom, DTS-neutral inside every rating × sector cell, rebalanced monthly with a buffer. The legs had been sized on the first business day of March from start-of-month DTS, exactly as ROBO's spec now insisted. The turnover budget had been set the previous autumn for a world in which an investment-grade round trip cost about 0.6%, the index average Barclays reported for 2018–2019 (Dynkin p.703), and a high-yield one about 0.94%.

**The tape to the nineteenth.** Spreads had been widening for three weeks at a pace nobody at the table had seen outside 2008, and in the second week of March the oil-price collapse had turned every energy credit into a question. Ines put up one fact she was not strictly entitled to on the nineteenth, because BlackRock only reported it on its first-quarter call in April: on 12 March the iShares investment-grade ETF, LQD, traded almost 90,000 times, while its five largest bond holdings traded an average of 37 times (Salim Ramji, BlackRock Q1 2020 call, 16 April 2020). By the middle of the month the Bank of England was recording some of the largest investment-grade and high-yield ETFs at more than 5% below the value of the bonds inside them; Chapter 20 tells that part. The bid–ask spread on high-yield bonds had spiked along with everything else (Man's 20-day average shows the shape, Man p.20).

"Your P&L," Ines said, and turned the sheet over.

The book was flat on direction. Its long and short legs had moved almost exactly against each other, which is what DTS-neutral is for. It was down a little under 2% for the month *(illustrative)*, and almost all of that was two lines: the cost of the first rebalance, which had gone through on 2 March at nearly twice the modeled cost, and the marks on the short leg's high-yield bonds, which had been marked down less than they would have traded.

"Flat on direction, down on cost," Kaz said. "That's the right answer."

"It's the right answer so far," Ines said. "Now look at what your model wants to do tomorrow."

**What the signals wanted.** Kaz put up the score. It had never looked better. The cross-sectional dispersion of ESP was the widest in the desk's sample, and Barclays' own finding is that value's outperformance "is larger when there is a high dispersion in ESP" (Dynkin p.545). Momentum was even louder. In a flight to quality, the issuers with the worst equity momentum were the energy names and anything with a leveraged balance sheet, and EMC wanted to sell every one of them it held and buy more of what had held up. The optimizer's proposal for the next morning was to turn over about 40% of the book *(illustrative)*.

Theo did the arithmetic from §9.4.2 on the back of the sheet, because it was the only arithmetic he trusted that week. Call the composite's gross edge 4% a year *(illustrative)*, a third of a percent a month. At 40% turnover the break-even round trip is $(4\%/12)/0.40 \approx 0.83\%$. That was below the July 2019 high-yield average of 0.94% (Dynkin p.703) before a single basis point of March's widening had been priced into it. "It's under water at last summer's prices," he said. "And it isn't last summer."

It was worse than that, and the evidence would arrive three months later. Kargar, Lester, Lindsay, Liu, Weill and Zuniga (NBER Working Paper 27355, June 2020) found that in March "the cost of trading immediately via risky-principal trades increased dramatically," which pushed customers into slower agency trades. Immediacy, the thing a monthly rebalance buys, had become the most expensive thing in the market. The signals fire hardest exactly when the spreads are most dispersed, and the spreads are most dispersed exactly when trading costs the most. A turnover budget set for an average month had been breached on the first day of this one.

There was a second problem, and Mags found it. "Your hedge is three weeks old," she said. The short leg had been scaled to match the long leg's DTS on 2 March. Since then spreads in the long leg, which held the wider, cheaper names, had risen proportionally more than in the short leg, so the long leg's DTS had grown faster. The book that was DTS-neutral on the second was, by the nineteenth, long a slice of the market it had been built not to own. "You're flat on direction because the first two weeks happened to wash. You won't be flat next week."

**What the screen meant.** Mags had spent that month on a dealer's distressed loan-and-bond desk (Chapter 1), and Theo asked her what the screen prices had meant. "They meant somebody had typed a number," she said. "In a normal week a run is an advertisement with some size behind it. That week it was an advertisement with nothing behind it. You'd call on a bid you saw on the screen and get a different number, smaller size, and a pause while somebody asked risk whether they were allowed to buy anything at all. The only price you could trust was the ETF's, because it was the only thing actually trading." Chapter 20 calls that week the one in which the ETF was the only price in town.

Theo was looking at a different part of the sheet: the cells above 1,000bp, where §9.2 says DTS stops being a ruler. "What does the credit agreement say?" he asked, and for once nobody laughed. Many of the issuers in those cells had drawn their revolvers to the limit or were about to, because treasurers everywhere were hoarding cash that month. A drawn revolver ranks ahead of the bonds in most of those structures, and nothing in a DTS ratio knows that. "Those aren't factor names any more," he said. "They're recovery names. The risk is where the bonds sit after the bank lines are full, not how far the spread moves."

**The card.** Ines handed them out. *Write three things. How much turnover you allow this month. Whether you trade toward the new signal or let the buffer widen. And what you do with the cells whose DTS has stopped meaning anything.*

Write yours before you read theirs.

Kaz wrote: *Turnover: the optimizer's 40%. Trade toward the signal: dispersion is at a record and value pays most when dispersion is high. Cells above 1,000bp: keep them in DTS scaling, cap each name at half its normal weight.*

Theo wrote: *Turnover: 5%. Let the buffer widen as far as it needs to. Above 1,000bp: out of DTS, sized on price and recovery, revolver draws read name by name.*

Mags wrote: *Turnover: whatever the bid side allows, which is about nothing. Don't chase the signal; let it come to you. Above a thousand: give them to me.*

**What happened.** Ines turned the tape forward.

On Monday 23 March the Federal Reserve announced its corporate credit facilities. Four days later, on 27 March, the New York Fed signed Terms of Assignment with BlackRock's Financial Markets Advisory unit to run the secondary-market facility, with conflict rules for a manager that sells the ETFs the facility could buy. On 9 April the programs were expanded to support up to \$850 billion of credit, and Kargar and coauthors would later find that the facilities "had a positive effect on market liquidity." From late February to late March US investment-grade spreads had roughly tripled to nearly 400bp and high-yield spreads had passed 1,000bp; by the end of the year most of the move had retraced *(levels approximate)*. Man's chart of the same months shows what a systematic credit fund launched in January 2020 lived through: a large mark-to-market loss in March, recovered by year-end (Man p.12). Its 20-day high-yield bid–ask spread was back to normal within months (Man p.20).

Then the factor record. Barclays ran its own drawdown analysis from January 1993 through March 2020, and it reads like a grade sheet for the cards (Dynkin p.739–741). Without DTS matching, ESP value was *pro-cyclical*: its long leg was wider and higher-DTS, so it lost money in the drawdown. Raw equity momentum was *contra-cyclical*, because in a flight to quality the issuers with the strongest equity momentum are the safe ones, so the long leg's DTS fell below the short leg's and the factor profited from the selloff. With DTS matching, both "delivered strong performance during all drawdown episodes," and their market correlations collapsed. So the desk's book was built right. In a month like March 2020 the P&L of a factor book is mostly its *net DTS*, not its signals, and a book that was DTS-neutral lost on liquidity and cost, not on direction.

"Kaz," Ines said. "Your signal was right and your card was wrong. Trading 40% into a market where immediacy had become the most expensive thing on the screen would have paid March's prices for a signal whose edge you'd already shown was under water at last summer's. And you kept the 1,000bp cells on a ruler that had stopped measuring anything.

"Theo. Five percent and a wide buffer is the right size: trade *less*, let the buffer widen, and let the drifting portfolio decay toward the new signal instead of buying it at the worst prices of the decade. Your third line is the best line on the table. But you didn't say what the five percent was *for*, and Mags just told you. Your hedge was three weeks stale.

"Mags. You get the third line, and I'll give you the names. But 'about nothing' leaves the stale hedge stale. The one trade worth paying March's prices for was the one that put the book back to DTS-neutral. That's a risk trade, not an alpha trade, and in a fire drill they are not the same thing."

She turned to the reader's side of the table. If your turnover number came from the optimizer, you wrote Kaz's card. If it came from a budget and you spent the budget on the signal, you were half right. If you spent it on re-neutralizing DTS with start-of-month numbers recomputed that week, and let the buffer absorb the signal, you wrote the card the desk wishes it had written. And if your third line moved the cells above 1,000bp out of DTS and onto price and recovery, you read §9.2 and Chapter 5 the way they were meant to be read.

Two other seats saw the same month from opposite sides, and both are useful. AQR's published credit work finds "only limited evidence of a liquidity premium in the cross section of corporate bonds" (Palhares and Richardson, *Journal of Fixed Income*, Winter 2019), and its white paper on systematic credit simulated a book traded through standardized CDS and CDS indices rather than cash bonds; read from those papers, not from any account of its March, that is the price taker's seat, which trades less and trades what still trades. D. E. Shaw's own note describes the opposite seat: over March and April it bought "in excess of \$400 million in CAS and STACR bonds at a significant discount to par" from holders "put under stress by redemption requests and margin calls," having judged 2001 rather than 2008 the better analogue (Chapter 4-C tells the whole story). The price taker shrinks its turnover; the patient capital is the other side of the forced seller. A monthly factor book sits between them, and March 2020 is the month it learns which one it resembles.

The plumbing decided how much all of this cost. The cost drag on Barclays' liquid ESP-plus-EMC strategy fell from about 1.15% a year in 2007–2012 to about 0.64% in 2013–2019 (Dynkin p.711), and that decade of electronification is why a liquidity shock of March's size was survivable for credit factor books. In 2008, with the average investment-grade liquidity cost score at 2.8% (Dynkin p.703), the same shock would have cost several times as much to trade through. The quants did trade through it, and mostly on screens: Man reports \$116.5 billion traded on MarketAxess's Open Trading platform by quant funds in the first three quarters of 2020, a 150% increase on the same period a year earlier (Man p.8). The investors who hired them split afterwards. A 2020 survey of credit factor managers by the Dutch pension fund PGGM, reported by IPE as *Will corona be a watershed moment for credit factor investing?*, divided them into a keep-it-simple camp and a sophisticated one (Man p.30).

Ines collected the cards. "In a fire drill," she said, "you spend the turnover on the hedge, not on the signal."

> **View From Another Seat.** *The insurer-backed credit platform, which is buying the engines.* A forced seller in March 2020 was somebody with a redemption queue or a margin call. An insurance balance sheet has neither in the same form: its liabilities run for decades, it holds most of its bonds to maturity, and it does not mark its book to the screen in order to survive the week, so a month like that one is a month in which it can choose to buy. That seat now owns factor engines too. Blackstone bought DCI, a quantitative credit manager, in 2020 and lists it among the acquisitions behind its goodwill (Blackstone FY2025 Form 10-K). Ares took a minority stake in BlueCove, a London systematic fixed-income manager founded in 2018, in 2023; on 29–30 October 2025 it agreed to buy the whole firm, by then about \$5.5bn of assets and about 60 people, and to run it as Ares Systematic Credit under BlueCove's chief executive, Alex Khein, citing insurance distribution and "increased interest in systematic credit" (The DESK and Alternative Credit Investor, 30 October 2025). Ares announced the completion in early February 2026 (Business Wire, 2 February 2026). Read against Ines's napkin, the point is who sits at the table. The four players who all fold at minus two percent were funds with the same model, the same stack and the same exit. A systematic book inside an insurer-backed platform can have the same model and a different exit, or no need of one. Whether that makes the next fire drill calmer, or only moves the crowding somewhere harder to see, is a question nobody yet has a live record to answer.

Who sits at the table matters most when the table is crowded, and in 2025 and 2026 it was crowded at the tightest spreads in a generation.

> **Trend Watch.** *The tight-spread regime and the first live track records, 2024–2026.*
>
> - **The tights.** US investment-grade OAS moved from about 77bp (4 July 2025) to about 72bp (September 2025), which State Street described as "the tightest since 1998" (SSGA SAFI Q3 2025 commentary, 25 November 2025).
> - **What tight spreads do to value.** Barclays finds that ESP's outperformance "is larger when there is a high dispersion in ESP" (Dynkin p.545). At record tights, dispersion compresses, so the value opportunity set shrinks just as more capital arrives to harvest it.
> - **A good live start.** State Street's two systematic high-quality corporate strategies (systematic since 31 December 2023) report Q3 2025 value contributions of +14bp (intermediate) and +43bp (long), momentum roughly flat to +4bp, a maximum relative drawdown since January 2024 of −5bp against a peer average of −44bp, roughly flat net performance through the March–April 2025 credit drawdown while the average manager lagged by about 35bp, and since-inception IRs of 2.89 and 2.63 (SSGA, 25 November 2025). The sample is under two years.
> - **A long live record.** Robeco QI Global Multi-Factor Credits (launched June 2015), as of 30 September 2026, annualized and net of fees against the Bloomberg Global Aggregate Corporates (hedged): 1 year −2.69% against −2.77%; 3 years 3.14% against 3.45%; 5 years −2.00% against −1.64%; since inception 0.63% against 0.87%. Attribution: value slightly positive, low-risk/quality the largest detractor (the long-end underweight of §9.5.3), momentum neutral, size slightly negative (Robeco fund page).
>
> *What it means for the desk.* The backtests in this chapter run from an IR of 0.5 to 2.4. A decade of live, net, multi-factor credit returns from a careful manager is close to the benchmark, with a defensive tilt that cost money in the latest period. A desk that budgets for a 2.0 IR is budgeting for a backtest. Budget for something like 0.5 net, demand the DTS-neutral decomposition every quarter, and treat any two-year live IR above 2 as a sample that has not yet met its first bad year.

## 9.11 The Credit Factor Lab: A Reference Implementation

When Hana's reversal signal went red that Tuesday in §9.9, the world it failed in was this one: the synthetic universe below is the placebo the CI job runs before it lets any new signal near the library, so it is the first thing the lab builds and the first thing a new desk should be able to rebuild from the specification alone.

### Specification for AI Implementation

**What ROBO builds.** `credit_factor_lab`: a synthetic corporate-bond universe whose data-generating process obeys the DTS law of §9.2 exactly, plus the full factor pipeline of §9.3–§9.9: signals, dollar-neutral versus DTS-neutral long–short portfolios, costs, buffers, a DTS-matched long-only tilt with a turnover cap, factor combination, and the price-noise module. Everything is numpy and pandas, seeded, and runs in seconds. The seven blocks below run in order in one interpreter. Every number the code prints is *illustrative*: the point is to verify the mechanics, not to estimate a premium.

**Data-generating process (monthly, $T = 240$).** There are $J = 400$ issuers and about 2,000 bonds (one plus Poisson(4) per issuer). Issuer log spreads are a fair value (rating base, leverage, net debt to EBITDA, coverage, and a *hidden priming-risk* flag that the market prices but the three ratios cannot see) plus a common market factor $M_t$, sector factors $S_{g,t}$, and an issuer residual $c_{j,t}$ that mean-reverts (this is the planted value alpha) and absorbs equity news with a one-month lag (the planted momentum alpha). The bond excess return is $s_{i,t}/12 - D^{\text{spr}}_i s_{i,t}\,\Delta\log s_{i,t+1}$ plus CUSIP noise, so $\beta_i = \text{DTS}_i/\text{DTS}_m$ holds by construction. Defaults are issuer-level with rating-dependent intensity (tripled for hidden-risk issuers) and a 40% recovery.

**Schemas and shapes.**

| Object | Shape / type | Units and meaning |
| :--- | :--- | :--- |
| `bonds` | DataFrame, $N$ rows | `issuer`, `rating` (0=A … 4=CCC), `sector`, `mat` (years), `dur` (spread duration, years), `lcs` (round-trip cost, fraction of value), `mbucket` (0: <5y, 1: 5–10y, 2: >10y) |
| `s` | `(T+1, N)` float | OAS at the start of month $t$, decimal, floored at 1bp |
| `xs` | `(T, N)` float | excess return over month $t \to t+1$, decimal; NaN when not held |
| `held` | `(T, N)` bool | bond in the universe at the start of month $t$ (true through its default month) |
| `DTS` | `(T, N)` float | $D^{\text{spr}} \cdot s \cdot 100$, years × percent, start of month |
| signal | `(T, N)` float | higher = buy; NaN = ineligible |
| `backtest(...)` | dict of `(T,)` arrays | `gross`, `cost`, `to` (one-way turnover), `dL`, `dS` (leg DTS) |

**Edge cases ROBO must handle exactly as stated.** A rating cell with fewer than 30 bonds is skipped in the ESP regression (production: pool into the adjacent rating). A defaulting bond earns recovery minus par in its default month, then leaves the universe; its exit is free, and it is never removed retroactively. New momentum history is NaN for the first six months and excluded from momentum but not from value. Negative-EBITDA issuers get `NDE_CAP = 15` turns *before* the 0.1 floor. OAS is floored at 1bp so DTS is never zero or negative. All leg scaling uses start-of-month DTS.

**Acceptance tests (asserts).** (1) The dollar-neutral DTS-sorted long–short has OLS beta within 10% of its DTS-implied beta, and the DTS-neutral version has $|\beta| < 0.05$. (2) Excess-return volatility is linear in DTS across 30 buckets ($R^2 > 0.9$, positive slope). (3) Dollar-neutral ESP has beta above 0.1 (the cold open), and every DTS-neutral factor has $|\beta| < 0.10$. (4) Turnover falls strictly as the buffer widens. (5) The long-only tilt has nonnegative weights and matches benchmark DTS in every rating cell to $10^{-9}$. (6) The combination formula (9.5) reproduces the directly computed combo IR to $10^{-8}$, and the max-IR combination beats every single factor in-sample. (7) The Blume–Stambaugh bias (9.6) is measured within ±20% of $\sigma_u^2$, and the lag-one reversal sort on noisy prices has $t > 5$. Weaker statistical expectations are printed as PASS or WARN, not asserted.

Everything in this chapter so far has been argued from other people's numbers: Barclays' index history, Man's simulations, the replication audits. That is fine for reading and useless for debugging. The cold open's 1.9 Sharpe came apart the moment Ines asked for the beta, and Mags's verdict was that Kaz had built the index with extra steps. A desk that wants to catch the next one automatically has a problem: real bond data comes with no answer key. Quotes are stale, fundamentals arrive late, and the premium you are hunting is smaller than the noise you are hunting it in, so when a test fails you cannot tell whether the code is wrong or the market is. The fix is to build a market where you wrote the answer key yourself. Plant a value alpha, plant a momentum alpha, build the DTS law of §9.2 into the arithmetic, and then ask whether the pipeline finds exactly what was planted and nothing else. Ines, who has opinions about marked cards, would want it noted that here the marking is the point.

Listing 9.1 builds that world in three functions and a handful of derived arrays. `build_issuers` draws 400 issuers across five ratings (A through CCC) and eight sectors, gives each leverage, net debt to EBITDA, and interest coverage scattered around its rating's typical level, and flags about 15% of the B and CCC names as carrying a hidden priming risk. That flag is the planted trap: the market prices it into fair spread, default intensity triples for it, and the three ratios cannot see it. About 2% of issuers get negative EBITDA, and their net debt ratio is replaced by a cap of 15 turns before it enters fair value. `build_bonds` gives each issuer one plus Poisson(4) bonds, with maturities of 2–10 years in high yield and 1–20 in investment grade, a spread-duration proxy from a 5% annuity, and a round-trip cost equal to the bid–ask in spread times duration. `simulate` then runs 240 months. Each bond's log spread is its fair value plus a persistent market factor, a sector factor, and an issuer residual that mean-reverts slowly (the planted value alpha). Equity news moves that residual, mostly in the same month and a sliver a month later (the planted momentum alpha). Monthly excess return is carry, spread divided by twelve, minus duration times spread times the change in log spread, plus bond-level noise, so beta is proportional to DTS by construction. Defaults are issuer-level coin flips with rating-dependent intensity and a 40% recovery.

The outputs are the arrays every later block consumes: OAS `s`, excess returns `xs`, the `held` mask, start-of-month `DTS`, and the equal-weight market return `r_mkt`. Use this block before you trust any real-data pipeline, and again after every change to the signal code. Do not use it to estimate a premium, because the numbers are illustrative, and remember that it cannot validate the DTS law itself: the law is built in, so passing here proves the code, while §9.2 supplies the evidence from real data. The edge case that bites is the default month. A bond that defaults in row t stays in `held` for that row, earns recovery minus par, and only then turns to NaN, and because defaults are issuer-level every bond of that issuer dies together. Build the universe from survivors and the loss never happens, which is how a value factor learns to look brilliant.

*The full listing is [Listing 9.1 in Appendix F](#code-9-1).*

Section 9.2 made three claims that sound too tidy to be true: beta is a ratio of DTS you can read off the screen, scaling both legs to the same DTS removes it, and volatility rises in a straight line with DTS. A restructuring banker who has watched a "stable" capital structure rearrange itself in a weekend is entitled to distrust tidy claims. The cure is to make the claims falsifiable on the desk's own machinery. That needs one backtest engine that every signal in the lab runs through, with the long and short legs built the same way, the same costs charged, and the only difference between the dollar-neutral and DTS-neutral versions being a single scaling factor. If the engine is the same, any difference in the output is the scaling. If the engine differs, you are comparing two programmers.

Listing 9.2 supplies the engine and then spends it on §9.2. `backtest` takes a score matrix (higher means buy, NaN means ineligible) and each month ranks the eligible bonds by percentile. The long leg is the top `q` and the short leg the bottom `q`, with an optional `buffer` that keeps an existing holding until it drifts out past `q` plus the buffer. In `"mv"` mode each leg is \$1 spread equally. In `"dts"` mode each leg is scaled so its portfolio DTS equals 12 years times percent, which means the leg with the tighter bonds is simply bigger in dollars. Turnover is one-way trading as a share of the gross book, and the cost of each trade is its size times half the round-trip `lcs`. The block then runs three tests. A DTS-sorted dollar-neutral book should show a regression beta on the equal-weight market that matches the beta DTS implies, within 10%. The DTS-neutral version should show a beta near zero. And per-bond volatility, grouped into 30 DTS buckets, should be linear in DTS with a slope that estimates $\sigma_\eta$, the volatility of proportional spread changes.

Use `backtest` for any rule that sorts bonds into long and short tails. It is not the tool for the long-only tilt of §9.8, which needs weights, not tails. One edge case bites. Every leg scale uses the DTS at the *start* of the month. Scale with end-of-month DTS and the scaling factor correlates with the very spread move it was meant to hedge, so the neutrality test would be passing on information no trader had. A smaller trap: a bond that defaults this month is still eligible this month, and its previous weight is zeroed afterward at no cost, because the exit is a court date, not a trade.

*The full listing is [Listing 9.2 in Appendix F](#code-9-2).*

When Ines asked "cheap why?" in the cold open, Kaz took it for philosophy. On a desk it is a regression. A bond is cheap only relative to what its peers, with the same sector, similar maturity, and similar leverage and coverage, are paid to carry. Sections 9.3 through 9.6 define five ways of asking that question: excess spread to peers, spread per turn of leverage, equity momentum, low risk, and a blend. Each is easy to state in a sentence and easy to get subtly wrong in code, usually with a floor applied in the wrong order or a window that peeks. The desk's answer is to write each signal exactly once, give every one the same output (a months-by-bonds matrix, higher means buy, NaN means ineligible), and let the engine of Listing 9.2 treat them interchangeably. A signal that cannot be swapped in with one line is a signal nobody will back-test fairly.

Listing 9.3 is that signal library. `esp_score` is the workhorse. For every month and every rating cell it regresses the log OAS of the held bonds on sector intercepts, two maturity-bucket shifts, and the three ratios (leverage, net debt to EBITDA, coverage), and returns the residual, winsorized at the 1st and 99th percentiles. A positive residual means the bond pays more than its peers' fundamentals explain, so it ranks as cheap. A cell with fewer than 30 bonds is skipped. With `with_prs=True` the regression also gets the priming-risk score, giving the `ESP+PRS` variant. `spider_score` divides spread by net debt to EBITDA, takes logs, and z-scores within rating. `emc_score` averages issuer equity returns over one, three, and six months, each expressed per month, and needs six months of history. `low_risk_score` adds the z-scores of duration and rating and flips the sign. `Composite` averages the available z-scores of `ESP+PRS`, `EMC`, and `LowRisk`, so a bond missing one signal is not dropped for it.

The last two lines are a diagnostic, not a signal: they report how many bonds in ESP's top decile carry the hidden risk compared with the universe, which is §9.3.4 in one number. Use this library when the question is cross-sectional ranking within a snapshot. Do not read the fundamentals as realistic, since they are static here, while production data is point-in-time and lagged at least three months. The edge case that bites is the negative-EBITDA issuer. Its ratio was replaced by a 15-turn cap in Listing 9.1, and `spider_score` floors at 0.1 *after* that. Floor first and a bankrupt-looking credit divides its spread by 0.1, becomes the cheapest bond per turn of leverage in the universe, and lands in the long book.

*The full listing is [Listing 9.3 in Appendix F](#code-9-3).*

A factor presentation has one slide that matters. It is a table with a row for each signal and columns for gross return, net return, volatility, information ratio, beta, and turnover, and it is the slide on which the risk committee asks why this number differs from yesterday's. Producing it by hand is a week of spreadsheets and a month of arguments about which version of the cost assumption went into which cell. Producing it by code takes seconds and puts both constructions of §9.2, dollar-neutral and DTS-neutral, next to each other for every signal, so that the reader can see which premium survives the change and which was the market all along. Mags, who distrusts any column headed "adjusted," will be pleased to find none: there is gross, there is net, and the difference between them is what the dealers charged.

Listing 9.4 loops over every signal in `SIG` and both constructions (`"mv"` and `"dts"`), runs each through `backtest` with the default decile tails, and passes the result to `summarize`. That function turns a return series into annualized gross and net percent returns, annualized volatility, gross and net information ratios (annualized mean over annualized volatility), the OLS beta to the equal-weight market, and average monthly turnover. The assertions come in two kinds. The hard ones are structural: dollar-neutral ESP must carry a market beta above 0.1, which is the cold open reproduced in a machine; every run must have nonnegative costs that sum to something positive; and every DTS-neutral run must have an absolute beta under 0.10. The statistical expectations are soft, printed as `PASS` or `WARN`. The first is whether the priming-risk regressor lifts the ESP information ratio, as §9.3.4 predicts. A 240-month synthetic sample can miss a true effect by chance, and a warning is more honest than an assertion that fails for no reason.

The second half runs the momentum signal `EMC` through four buffer widths (0, 5, 10, and 20 percentage points) and tabulates gross return, cost, net return, and turnover. Turnover must fall strictly as the buffer widens, which is a hard assert, while the net-of-cost win for a 10% buffer is soft, which is §9.8.3 as a table. Use this block as the template for any new signal: add it to `SIG`, read the row. Do not compare `IR_gross` between a dollar-neutral row and a DTS-neutral row as if they were measuring the same thing, because the first includes beta. The edge case that bites is that a buffered leg is no longer a decile. A bond stays in until it falls below the wider threshold, so the held set can swell past `q`, and because each leg is rescaled to the same DTS, the extra names dilute the weight on the best ones. That dilution is where the gross alpha goes.

*The full listing is [Listing 9.4 in Appendix F](#code-9-4).*

Most of the money that could buy a credit factor cannot short a bond. An insurer's separate account has a benchmark, a tracking-error budget, and an investment policy statement that treats the word "short" the way a lender treats the word "waiver." For that client the long–short factors of Listing 9.4 are a research instrument and not a product. The product is a tilt: hold the benchmark, lean toward the cheap and the trending, and do it without changing the account's exposure to the market, because the client already owns that exposure and did not hire a factor manager to renegotiate it. Three constraints pull against each other here. The tilt wants weight in the best bonds, the turnover cap forbids reaching it all at once, and the DTS match wants every rating cell to keep the benchmark's spread risk. Done by hand each month, the three would be reconciled differently by different people on different days. That is the argument for writing the order of operations down once, in code, where it can be asserted.

Listing 9.5 builds the benchmark as the equal-weight held universe and walks forward month by month. The target weight of each bond is its benchmark weight times `1 + k z`, floored at zero so that no position goes short, where `z` is the signal (the lab runs it on `Composite`) and `k` is 0.5. The code then measures the one-way turnover that would take the book from last month's weights to this target and, if it exceeds the `to_cap` of 10%, scales the trade back proportionally. After that, within each of the five rating cells, it rescales the weights until the cell's DTS contribution equals the benchmark's, which is the Ben Dor construction cited in the code. Weight that does not sit in bonds is assumed to sit in duration-matched Treasuries with zero excess return. The outputs are the monthly active return against the benchmark, the cost, realized turnover, the largest DTS-matching error, and the smallest weight ever held.

Use it when the mandate is benchmark-relative and the signal is mostly cross-sectional. Do not expect it to deliver a long–short Sharpe ratio, because the tilt is small, a long-only book cannot short the expensive bonds it dislikes, and the cap slows it. The edge case that bites is the order of the last two steps. The turnover cap is applied before the rating-cell re-match, so the DTS adjustment can push realized turnover a little above 10%, and a cell where the tilt zeroed every bond falls back to its benchmark weights. The asserts check the two properties the construction promises, no negative weights and cell DTS matched to $10^{-9}$, and leave the turnover cap as an approximate budget, not an exact one.

*The full listing is [Listing 9.5 in Appendix F](#code-9-5).*

Every factor presentation ends on the same slide, titled "Diversification," and the same question follows it: by how much? Kaz's first answer is usually to assume the factors are uncorrelated, which makes the arithmetic beautiful and the portfolio imaginary. Equation (9.5) is the grown-up answer, and it has the property that a formula should have before anyone trades on it: it can be checked. The combined information ratio depends on only two things, the vector of single-factor IRs and the correlation matrix of the factor returns. If the code computes the same number from the raw return series that the formula computes from those two summaries, the formula is right and so is the plumbing. If the two disagree by even a hair, something in the pipeline is not what the committee thinks it is, and it is much better to learn that on a synthetic desk than in the minutes of the risk committee.

Listing 9.6 takes the DTS-neutral gross return series of four factors from Block 4 (`ESP+PRS`, `SPiDER`, `EMC`, `LowRisk`) and drops the first six months, the momentum warm-up, so that every factor is estimated on the same dates. It computes each factor's annualized IR and the correlation matrix. Then it builds the equal-risk combination two ways: directly, by dividing each return series by its own volatility and averaging, and by formula (9.5) from the IRs and correlations. It also solves for the maximum-IR weights, proportional to the inverse correlation matrix times the IR vector, and reports the resulting combined IR. It prints the matrix, the four IRs, and both combined IRs. The two hard asserts are that the direct and formula results agree to $10^{-8}$, which is an algebraic identity in-sample and therefore a plumbing check, and that the maximum-IR combination is at least as good as the best single factor in absolute value. A final warning fires if the correlations are all low and equal weighting still loses to the best single factor, which is the "IRs too unequal" case that §9.7.1 predicts.

Use the block to size the benefit of adding a factor before building it. It combines *return series*, so it does not capture the netting that happens when signals are blended before trading, which is why the lab's `Composite` is built at the signal level. The edge case that bites is the in-sample optimum. The assertion is guaranteed by Cauchy–Schwarz, so it proves nothing about the future. With four noisy IRs and correlated factors, the inverse-correlation weights lean hard on small differences, and a factor with a modest negative sample IR can end up with a negative weight even if you believe it earns a positive premium. Shrink the weights toward equal before anyone calls them a strategy.

*The full listing is [Listing 9.6 in Appendix F](#code-9-6).*

Section 9.9 made a claim that is easy to nod along to and hard to feel: a premium can be nothing but a pricing error, because the same bad mark sits in the signal and in the next return. Theo's reaction, reasonably, was to ask how large such a thing could be. "Large" is not a number a desk can act on. The desk needs to see the artifact on its own pipeline, with a known amount of noise injected into otherwise perfect prices, so that the next time a reversal backtest prints a t-statistic of eight, someone can run the same test on prices known to be wrong and see whether the number is the market or the marks. Kaz, who has never read a credit agreement but has read every errors-in-variables paper, volunteered. The lab is where the desk's rule one, that signal and return never share a price, stops being a rule and becomes an experiment.

Listing 9.7 starts with `noisy_returns`, which turns the simulation's excess returns into a clean price path for every bond, then multiplies each month's price by `1 + u` with `u` independent and normal, and recomputes returns from both versions. The first experiment sets the pricing error to 1% for every bond and measures the average gap between noisy and clean returns over held, non-default observations. Equation (9.6) says the gap is $\sigma_u^2$, which is 1bp a month at this noise level, and the assert requires the measured bias to be within 20% of it. The second experiment makes high-yield marks three times noisier than investment-grade ones, then runs two long–short sorts on the noisy returns through the Listing 9.2 engine: last month's loser is the buy (lag one), and the loser from two months ago is the buy (lag two). The lag-one sort shares a price with the return it is trying to forecast, and the assert requires a t-statistic above 5. The lag-two sort shares no price, and the soft check expects a t-statistic near zero. The "alpha" is the pricing error, giving itself back.

Use this module as a regression test for any signal built from returns or price-implied spreads: run it on noisy prices and see whether it still "works." Do not read the 1% as calibrated, since both noise levels are illustrative. The edge case that bites is the word *independent*. Here the errors are independent across months, so skipping one month removes them completely. Real marks go stale, and a stale quote repeats its error for weeks, so a one-month skip clears only part of it. This block also reuses the `not_def` mask from Block 2 and draws its noise from separate seeds, so run it after the others, not on its own.

*The full listing is [Listing 9.7 in Appendix F](#code-9-7).*

The first time Theo ran the whole lab he read the output the way he used to read a first-day declaration, looking for the few numbers that would matter in court. The `[mv]` and `[dts]` rows sat side by side for every signal: the dollar-neutral value rows carried a large positive beta and the low-risk rows a negative one, and DTS-neutralization removed both, which is §9.2 in a table. The `share of hidden-risk bonds` line told him how many of ESP's "cheapest" bonds were fairly priced bonds carrying a risk the three ratios could not see, and the `ESP+PRS` row showed what a document-risk regressor bought back, which was his runway column's argument made by a machine. And the momentum buffer table reproduced §9.4 and §9.8 together: gross alpha that is real, turnover that is not affordable, and a buffer that trades some of the first for much less of the second.

## 9.12 Desk Debrief

The finder below is for the reader who comes back looking for one thing: where each idea is stated, where it is built gently, where a character finds out when it breaks, and where the code lives.

| Concept | Equation | Intuition (box) | Judgment (scene) | Code |
| :--- | :--- | :--- | :--- | :--- |
| DTS is beta | (9.1) | *Relative change, and beta as a ratio* (§9.2.1) | Mags at the 1,000bp line (§9.2.3) | Listing 9.2 |
| Value as a residual in a peer cell | ESP regression (§9.3.1) | *A residual is the part the peers cannot explain* (§9.3.1) | Theo's runway column (§9.3.4) | Listing 9.3 |
| The measure trap | (9.2) | *The bell, its dial, and the bookmaker's odds* (§9.3.3) | The 83bp against 24bp payoff (§9.3.3) | Listing 9.3 |
| Break-even cost | (9.3) | *Turnover is a meter* (§9.4.2) | Long Scene A, the grading (§9.10) | Listing 9.4 |
| Carry is the price of DTS | (9.4) | §9.5.1 | Long Scene B, 2022 (§9.5.3) | Listing 9.4 |
| Combining factors | (9.5) | *Correlation, and two rowers* (§9.7.1) | The telecom case and the Pair Book's value loading (§9.7) | Listing 9.6 |
| Noisy prices | (9.6) | *Two ways a backtest flatters itself* (§9.9) | Hana's red build (§9.9) | Listing 9.7 |
| The five library rules | — | *Two ways a backtest flatters itself* (§9.9) | Kaz's whiteboard (§9.9) | Listing 9.7 |
| Buffers and constraints | §9.8.1, §9.8.3 | *The hinge* (§9.8.1) | Long Scene A, the card (§9.10) | Listing 9.5 |
| Live IR | §9.10 | Trend Watch, tight spreads (§9.10) | Long Scene B, the Robeco coda (§9.5.3) | Listing 9.6 |

A week after the cold open, Kaz put the value strategy back on the screen, rebuilt with DTS-neutral legs inside rating × sector cells, start-of-month DTS, default months kept, and a skip-month rule between the price used for the signal and the price used for the return. The Sharpe ratio was 0.9 gross and 0.7 net. The beta was 0.02 *(illustrative)*.

"It's less," Kaz said.

"It's *yours*," Ines said. "Last week sixty percent of it belonged to the index. Now replay the hand: what did the cheap decile cost to trade, and how much of it was cheap because somebody at the table knew something?"

Theo had the answer to the second half. He had added two columns to the ESP regression: the 13-week model's liquidity runway and a crude document-risk flag for drop-down capacity. In B and CCC they pulled a fifth of the names out of the cheap decile. Most of the names they removed had widened further over the next six months. IDO or it didn't happen, and this time some of it had.

Mags read the new tear sheet twice, which for her is applause. "Back in my day, the value factor was a guy who bought what everybody else was selling and had a strong stomach. Yours has a cost model and a lawyer." A pause. "Fine. Yours is better than the guy."

- **Beta in credit is $\text{DTS}_i/\text{DTS}_m$.** A dollar-neutral spread sort is a long-beta portfolio. Report every factor both dollar-neutral and DTS-neutral; the gap is how much of it was beta.
- **Carry is the price of DTS.** Per unit of DTS, carry is $1/D^{\text{spr}}$, so a DTS-neutral carry factor is a short-duration factor and belongs with low-risk.
- **Value is a residual within a peer cell, on clean prices.** The residual is either cheapness or information you lack. Document-risk features (Chapter 13) separate the two, and that is where the RSSG reader's edge lives.
- **Momentum is real gross and perishable.** A top-decile half-life of about 1.2 months and the break-even rule $c^\ast = \mathbb{E}[r^{\text{gross}}]/\text{TO}$ decide whether you can keep it. At 73% monthly turnover you need round-trip costs below 72bp.
- **Size is mostly liquidity and price noise; the informed investor is a filter.** Neither is a stand-alone engine.
- **Combine with $\rho^{-1}\text{IR}$, shrunk toward equal weights.** Equal-risk weights can lose to the best single factor, and trade netting exists only in the traded portfolio.
- **Signal and return never share a price, defaults stay in, filters are written before the data are seen, and the library replicates Open Bond Asset Pricing in CI.**
- **Budget for a live net IR near 0.5, not 2.** Ten years of live multi-factor credit returns sit near the benchmark; the backtests do not.

### The Spec You Hand the Robot

Paste the block below into ROBO's prompt. The seven Python blocks in §9.11 are the executable reference, and their asserts are the acceptance tests.

```text
ROBO: build credit_factor_engine, a DTS-aware cross-sectional credit factor pipeline.
Implement exactly this. Where something is unspecified, stop and ask; do not guess.

INPUTS (point-in-time; every field carries available_at; monthly rebalance at start of month t)
  oas[t,i] decimal (OAS, never Z-spread, on callables); oasd[t,i] years; DTS = oasd*oas*100 (yrs x %)
  rating[t,i] in {A,BBB,BB,B,CCC}; sector[t,i]; maturity bucket {<5y, 5-10y, >10y}
  fundamentals[t,j]: leverage, net_debt/EBITDA, interest coverage; lag >= 3 months, no restatements
  equity_ret[t,j]; esi[t,j]; prs[t,j] (Chapter 13, optional); lcs[t,i] round-trip cost, fraction
  ultimate_parent[i]; default_month[i]; recovery[i]

SIGNALS (higher = buy; NaN = ineligible)
  ESP: monthly OLS of log OAS on cell intercepts + 3 ratios (+ prs if present), by rating;
       cells < 30 bonds pool to the adjacent rating; winsorize residuals 1/99; negative EBITDA -> 15x
  SPiDER: z-score within rating of log(OAS / max(ND/EBITDA_fixed, 0.1))
  EMC: mean over h in {1,3,6} of equity return(h)/h; NaN until 6 months of history
  LowRisk: -(z(duration) + z(rating index))
  Composite: mean of available z-scores of ESP(+PRS), EMC, LowRisk

PORTFOLIOS
  L/S: top vs bottom decile; legs scaled to DTS 12 (yrs x %) per leg using START-of-month DTS
  Long-only: bm * max(1 + 0.5*z, 0); one-way turnover cap 10%/month; then rescale each rating
       cell so that sum(w*DTS) equals the benchmark's; residual weight sits in Treasuries
  Buffer: enter at decile 10, exit below percentile 0.90 - buffer
  Issuer cap: w_j * D_j * s_j <= kappa (state kappa and units); exclude s > 1,000bp from DTS scaling

COSTS
  cost_t = sum_i |dw_i| * lcs_i / 2 ; report gross, cost, net, turnover, beta to the market

DATA RULES
  signal and return never share a price (skip a month or use separate sources)
  defaults: return = recovery - last price in the default month; drop the bond next month only
  no ex-post return filters; log every outlier reviewed

OUTPUT
  table per factor x {mv, dts}: gross %, net %, vol %, IR gross, IR net, beta, turnover %/month
  correlation matrix; equal-risk and rho^-1 IR combination IRs; buffer table; noise-bias table

ACCEPTANCE TESTS (fail loudly)
  dollar-neutral DTS sort: |beta / ((DTS_L - DTS_S)/DTS_m) - 1| < 0.10; DTS-neutral |beta| < 0.05
  every DTS-neutral factor |beta| < 0.10; long-only weights >= 0; cell DTS error < 1e-9
  combo IR formula equals direct computation to 1e-8; max-IR combo >= best single factor
  turnover strictly decreasing in buffer; noisy-price bias within 20% of sigma_u^2
```

### Exercises

1. **Kaz's hedge, two ways.** The long leg has DTS 12, the short leg 7.2, and the market 8. (a) Compute the dollar-neutral beta and the DTS-neutral short notional per \$100mm long. (b) Now let the legs differ in duration: long $D^{\text{spr}} = 4$ at 3.0% spread, short $D^{\text{spr}} = 8$ at 0.9%. Both legs have the same DTS as before. Compute the DTS-neutral book's net carry, and explain the answer using equation (9.4). Which factor have you actually built?
2. **Can you afford it?** A signal earns 3.0% a year gross with one-way turnover of 40% a month. Using Barclays' July 2019 liquidity cost scores (IG 0.608%, HY 0.941%; Dynkin p.703), decide whether it survives in investment grade, in high yield, or neither. Then find the turnover cap at which it survives in high yield, and say what a buffer would have to do to the gross return to make that cap worth it.
3. **The measure trap.** A three-year bond has a physical default probability of 1%, an asset Sharpe ratio $\theta = 0.3$, and loss given default 0.6. Compute the fair spread with and without the $\mathbb{P}\to\mathbb{Q}$ step of equation (9.2). The bond trades at 65bp. Is it cheap? Is it cheap to a desk that skipped the step?
4. **ROBO literalism.** Theo's draft spec says: "Buy cheap bonds, avoid momentum crashes, and keep costs low." List three things ROBO could build that satisfy the sentence and lose money (one of them should involve Treasuries), then rewrite the spec with units, timing, and boundary conditions.
5. **Extend the lab.** Add bond momentum (trailing six-month excess return) and an equity-short-interest signal with a planted link to future spread widening. Run both on clean and noisy prices. Which one does the Blume–Stambaugh mechanism inflate more, and why does your answer depend on whether the signal is built from bond prices or equity data?
6. **First-day declaration.** Kaz wants the retracted factor model to "file under Chapter 11." Write its first-day declaration in one page: the cause of distress (identify the data errors of §9.9), the debtor-in-possession financing (what clean data would replace it), and the plan of reorganization (your five library rules). The Ad Hoc Group of Replicators, represented by counsel, will object to anything vague.

### Deep-Dive Resource Graph

**Podcasts**

- **Jeff Rosenberg - The Past, Present, and Future of Systematic Fixed Income (S7E19)** (*Flirting with Models*, Corey Hoffstein, 18 Aug 2025). BlackRock's systematic fixed-income head on why factor investing exists mainly in credit, why "characteristic specificity" matters in fixed income, and whether the pod-shop model fits quant credit. Read it alongside §9.1 and §9.10. https://www.flirtingwithmodels.com/episodes/8V74zBaN4jN
- **Greg Obenshain - Quantitative Credit (S4E12)** (*Flirting with Models*, 19 Jul 2021). A fundamental high-yield PM turned quant (Verdad) argues that excess return comes from separating improving from declining credits and that "even just acquiring data may be an edge", with the dimensionality problem stated plainly. Companion to §9.3 (value) and §9.6 (quality). https://www.flirtingwithmodels.com/episodes/nQBct6plzWH
- **Ralph Smith - Scientific Investing in Fixed Income (S5E7)** (*Flirting with Models*, 11 Jul 2022). Breadth and liquidity differ between credit and rates, and the assumption about a bond's availability materially moves a backtest: the practitioner version of the replication problem. For §9.8 (costs) and §9.9. https://www.flirtingwithmodels.com/episodes/kAEkSoYuRwd
- **Extra Credit: Algorithmic Advantage - Systematic Investing in Credit** (*Long Story Short*, Man Group; Robert Lam and Paul Kamenski of Man Numeric with host Danilo Rippa; recorded March 2024, page gives no publication date). The one first-party Man discussion of what quant credit is, how it is being adopted and what systematic bond trading may look like; it pairs with the Man 2022 informed-investor paper behind §9.3 (spread per turn of leverage) and §9.6. https://www.man.com/insights/extra-credit-algorithmic-advantage
- **Acadian Sees Quants Moving to Loans, CLOs** (*The Credit Edge*, Bloomberg Intelligence, guest Scott Richardson of Acadian, 19 Feb 2026). Systematic credit has room to expand into leveraged loans, structured finance and EM: where the next factor sleeves get built, and the capacity question for §9.10 and §9.11. https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/acadian-sees-quants-moving-to-loans-clos

**Practitioner Writing**

- **The case for systematic investing in credit** (State Street Global Advisors, Arkady Ho, 25 Aug 2026). A large incumbent's current pitch: factor-based credit, signal-driven excess returns and diversification from active managers, helped by electronic and portfolio trading. Read it as the "what the buyer is told" counterpoint to §9.9, and for §9.1 and §9.8. https://www.ssga.com/ca/en/institutional/insights/case-systematic-investing-credit
- **The flaw in the data that led corporate bond investors astray** (Warwick Business School, on Cesare Robotti's findings, 10 Sep 2024). A readable account of how a data error survived in a published four-factor bond model and what it did to the evidence; the news-level companion to the retraction discussed in §9.9. https://www.wbs.ac.uk/news/flaw-data-corporate-bond-investors/
- **Common pitfalls in the evaluation of corporate bond strategies** (Cesare Robotti, Finance Seminar, Aarhus University, 11 Apr 2024; seminar abstract). The abstract's claim is that large abnormal returns from many bond strategies mostly stem from microstructure noise in transaction prices and ad hoc winsorization, the same noisy-price argument as the 2026 arXiv paper listed under Academic Papers. For §9.9. https://econ.au.dk/research/finance/seminars/vis/artikel/finance-seminar-cesare-robotti-warwick
- Impax, "Quant meets credit: enhancing fundamental analysis through systematic screening" (19 September 2025), which reports the Barclays QPS US\$90–140bn estimate and the "Better Together" hit-rate results: https://impaxam.com/insights-and-news/blog/quant-meets-credit-enhancing-fundamental-analysis-through-systematic-screening/
- State Street Global Advisors, SAFI Q3 2025 commentary (25 November 2025): https://www.ssga.com/us/en/institutional/insights/fixed-income-q3-2025-safi-commentary
- Robeco QI Global Multi-Factor Credits, fund page with performance and attribution: https://www.robeco.com/en-int/products/funds/isin-lu1235145304/robeco-qi-global-multi-factor-credits-fh-eur
- Robeco, *Guide to Credits* (c. 2017): https://www.robeco.com/files/docm/docu-guide-to-credits.pdf
- Robeco, "A prudent route to effective factor timing" (12 July 2023; equity evidence on factor timing after costs): https://www.robeco.com/en-us/insights/2023/07/a-prudent-route-to-effective-factor-timing
- Quantpedia's summary of Dick-Nielsen, Feldhütter, Pedersen, and Stolborg: https://quantpedia.com/corporate-bond-factors-replication-failures-and-a-new-framework/
- Title only: Barclays QPS, Mateer et al. (2024), *QPS & Credit Research: Better Together*; AQR, *Alternative Thinking* (October 2017), "The Illusion of Active Fixed Income Alpha"; IPE (2020), "Will corona be a watershed moment for credit factor investing?" (the PGGM survey); Robeco (June 2022), "Ten years of successful factor investing in credit markets."
- Shelf: Dynkin et al., *Systematic Investing in Credit* (Dynkin p.45, 524–553, 606–633, 679, 693–711, 739–741, 794); Ben Dor et al., *Quantitative Credit Portfolio Management* (Ben_Dor p.33–34, 51, 61, 118); Man Group, *Quantitative Credit Alpha: Early Mover* (2022) (Man p.10–30); Paleologo, *Advanced Portfolio Management* (Paleologo p.27, 71); BlackRock, *Systematic High Yield Credit* (p.3, 6); Blackstone, *Systematic Credit* (p.2).

**Academic Papers**

- Dickerson, Robotti, and Rossetti (2026), "The Corporate Bond Factor Replication Crisis," arXiv:2604.07880: https://arxiv.org/abs/2604.07880
- Dickerson, Mueller, and Robotti (2023), "Priced Risk in Corporate Bonds," *Journal of Financial Economics* 150(2); arXiv posting: https://arxiv.org/abs/2604.05699
- Dickerson, Julliard, and Mueller (2026), "The Co-Pricing Factor Zoo," arXiv:2604.04430: https://arxiv.org/abs/2604.04430 ; project origin, Inquire Europe (26 November 2023): https://www.inquire-europe.org/news/new-reseach-started-the-corporate-bond-factor-zoo/
- Dick-Nielsen, Feldhütter, Pedersen, and Stolborg (2023), "Corporate Bond Factors: Replication Failures and a New Framework," SSRN 4586652; AQR working-paper page: https://www.aqr.com/Insights/Research/Working-Paper/Corporate-Bond-Factors-Replication-Failures-and-a-New-Framework
- Bai, Bali, and Wen (2019), "Common risk factors in the cross-section of corporate bond returns," *Journal of Financial Economics* 131(3): 619–642; retraction notice, *JFE* 150(3), DOI 10.1016/j.jfineco.2023.103721: https://econpapers.repec.org/article/eeejfinec/v_3a150_3ay_3a2023_3ai_3a3_3as0304405x23001617.htm
- Houweling and van Zundert (2017), "Factor Investing in the Corporate Bond Market," *Financial Analysts Journal* 73(2), DOI 10.2469/faj.v73.n2.1: https://rpc.cfainstitute.org/research/financial-analysts-journal/2017/factor-investing-in-the-corporate-bond-market
- Israel, Palhares, and Richardson (2018), "Common Factors in Corporate Bond Returns," *Journal of Investment Management* 16(2): 17–46: https://www.aqr.com/-/media/AQR/Documents/Journal-Articles/Common-Factors-in-Corporate-Bond-Returns.pdf
- Chordia, Goyal, Nozawa, Subrahmanyam, and Tong (2017), "Are Capital Market Anomalies Common to Equity and Corporate Bond Markets?" *Journal of Financial and Quantitative Analysis* 52(4): 1301–1342: https://www.cambridge.org/core/product/identifier/S0022109017000515/type/journal_article
- Title only: Kelly, Palhares, and Pruitt (2023), "Modeling Corporate Bond Returns," *Journal of Finance*; Jostova, Nikolova, Philipov, and Stahel (2013), "Momentum in Corporate Bond Returns," *Review of Financial Studies* 26(7); Haesen, Houweling, and van Zundert (2017), "Momentum Spillover from Stocks to Corporate Bonds," *Journal of Banking & Finance* 79; Correia, Richardson, and Tuna (2012), "Value Investing in Credit Markets," *Review of Accounting Studies* 17(3); Koijen, Moskowitz, Pedersen, and Vrugt (2018), "Carry," *Journal of Financial Economics*; Henke, Kaufmann, Messow, and Fang-Klingler (2020), "Factor Investing in Credit"; Frazzini and Pedersen (2014), "Betting Against Beta," *Journal of Financial Economics*; Blume and Stambaugh (1983), "Biases in Computed Returns," *Journal of Financial Economics*; Chen, Lesmond, and Wei (2007), "Corporate Yield Spreads and Bond Liquidity," *Journal of Finance*; Dick-Nielsen and Rossi (2019), "The Cost of Immediacy for Corporate Bonds," *Review of Financial Studies* 32(1); Asquith, Au, Covert, and Pathak (2013), "The Market for Borrowing Corporate Bonds," *Journal of Financial Economics*; Alquist, Israel, and Moskowitz (2018), "Fact, Fiction, and the Size Effect," *Journal of Portfolio Management*; van Binsbergen, Nozawa, and Schwert, "Duration-Based Valuation of Corporate Bonds," *Review of Financial Studies* (forthcoming).

**Data & Code**

- Open Bond Asset Pricing: cleaned TRACE panels, the 108-signal set, the 341-factor set, corrected Bai–Bali–Wen factors, and duration-matched Treasury returns: https://openbondassetpricing.com/
- Lasse H. Pedersen's data page, which links the Dick-Nielsen–Feldhütter–Pedersen–Stolborg factor data: https://www.lhpedersen.com/data
- SEC EDGAR, for point-in-time fundamentals: https://www.sec.gov/edgar
- Title only: FINRA TRACE specifications; WRDS Bond Returns.
- This book: §9.11 (`credit_factor_lab`), Chapter 7 (purged cross-validation and the replication audit), Chapter 8 (shrinkage and empirical duration), Chapter 13 (the Priming Risk Score as a value regressor), and Appendix B (data feeds).

<!-- STATUS: COMPLETE -->
