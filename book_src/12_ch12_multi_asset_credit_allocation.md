# Chapter 12: Multi-Asset Credit Allocation

<!-- WRITER PLAN (sections appended in order as drafted; resume after the last complete "## 12.x" section):
12.0 Cold open; 12.1 MAC universe as a capital-structure map (TW-1); 12.2 The return identity;
12.3 Spread per unit of what? (+ Resource Graph); 12.4 Regimes: two-state HMM (TW-2);
12.5 Covariance you can trust: DTS, EWMA, shrinkage, desmoothing; 12.6 Optimization and the flat frontier;
12.7 Liquidity tiers as the binding constraint (TW-3, + Resource Graph); 12.8 Tactical overlays and the turnover budget (TW-4);
12.9 Case studies; 12.10 Specification for AI Implementation (cumulative python);
12.11 Desk Debrief, The Spec You Hand the Robot, Exercises; Deep-Dive Resource Graph. -->

## 12.0 Cold Open: Seven Piles, One Bet

The sleeve arrived on a Monday as a spreadsheet with eleven tabs and one comment: "Make it efficient. —PM."

Theo opened it the way he used to open a data room, looking for the tab somebody hoped he would skip. High yield. Leveraged loans. EM sovereigns, BB to B. EM corporates. CoCos. High-yield preferreds. ABS. CMBS BBB. CLO BBB to B. Credit-risk transfer. And at the bottom, in a different font, as if added by a different person: middle-market direct lending, held through a perpetual BDC.

Kaz had already run the optimizer. "Good news. Max Sharpe puts thirty-five percent in direct lending, which is the upper bound. Its volatility is one point nine percent. It is the best asset I have ever seen."

"Volatility of what?" Mags asked from two desks over, without turning around. "The quarterly letter?"

"Of the return series."

"The return series is a valuation committee with an appraisal model and a deadline. Back in my day we called that a mark. Now you call it a covariance matrix."

Ines rolled her chair over, looked at the eleven tabs, and did what she did with any new hand: she counted the players. "Seven piles of the same bet with different lawyers attached. HY, loans, CLO mezz, the BDC: same sponsors, same borrowers, different seats in the waterfall. EM and preferreds are the same bet in a different accent. So. What's the pot, what are the odds, and who at this table knows more than you?"

"The pot is about six percent," Theo said, scrolling. "The efficient frontier runs from five-eleven to six-twenty."

"And the error bars on your expected returns?"

Theo did not answer, which was the answer.

He took the USB stick out of his pocket, the one with the 13-week cash flow model, and set it on the desk like a chip. "In restructuring, nobody asked me which sector had the best yield. They asked what the claim recovers, where it sits, and how fast you can get out. That's three numbers. This spreadsheet has eleven tabs and none of the three."

"Then that's the job," Ines said.

The question this chapter answers: **how do you allocate across credit sectors when every input lies in its own way? The index yields include defaulted constituents, the volatilities are appraised, the correlations change with the weather, and one of the assets can only be sold once a quarter, five percent at a time.**

By the end of this chapter you will be able to: write a sector's forward return as an accounting identity and say which measure each term lives in; compare sectors by spread per unit of expected loss, DTS risk and liquidity cost instead of by yield; fit a two-state hidden Markov model to credit excess returns without leaking the future; build a covariance matrix from DTS, EWMA and shrinkage, and desmooth a private-credit return series before it reaches the optimizer; explain why the efficient frontier in multi-asset credit is nearly flat and what that implies for how much to trust it; impose liquidity tiers, a 15% illiquid cap, a days-to-liquidate budget and a tactical tilt budget as hard constraints; and hand ROBO a spec that builds the whole engine with sanity checks.

## 12.1 The MAC Universe as a Capital-Structure Map

The sell-side deck draws multi-asset credit (MAC) as a menu. Nuveen's version (Figure 1, Nuveen p.2) is a good one: yield targets of roughly 6–9% for high yield and leveraged loans, 5–11% for securitized credit, 5–9% for EM debt and preferreds, 9–11% for middle-market direct lending and 11–14% for middle-market junior capital, with a liquidity column running from "High" to "Illiquid." Read as a menu, the obvious order is by yield. Read the way a restructuring banker reads anything, it is a capital-structure map that has been sorted by the wrong column.

Every sector on the menu is a point in a four-dimensional space: **where it sits** (seniority and security), **what it recovers** (and who decides), **how it reprices** (fixed or floating, callable or perpetual), and **how fast you can leave** (settlement and liquidity tier). The yield is a function of those four coordinates plus a risk premium. Allocating by yield is like choosing a seat at the poker table by how much money is in front of the chair.

| Sector | Seat in the waterfall | Coupon | What drives recovery | Exit | Typical Rule 22e-4 bucket (desk judgment) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| HY bonds | Senior secured or unsecured notes | Fixed, callable | Collateral and documents; post-default value ~39% (FEDS 2024) | Dealer RFQ, portfolio trade, T+1 | Moderately liquid |
| Leveraged loans | First-lien term loan B | Floating (SOFR + spread) | First-lien claim; ~52% post-default value (FEDS 2024) | Assignment, T+7 target, often longer | Less liquid (settles after 7 days) |
| Direct lending | First-lien unitranche, club deal | Floating, often PIK-able | Lender group, sponsor support; ~33% post-default value (FEDS 2024) | None in the loan; the fund gates at 5% of NAV a quarter | Illiquid |
| CLO BBB to B | Mezzanine tranche of a loan pool | Floating | Waterfall: OC/IC tests and the CCC bucket | Dealer, BWIC | Less liquid |
| EM sovereign BB to B | Sovereign unsecured, collective action clauses | Fixed, USD | Negotiated haircut, IMF program | Dealer, T+1/T+2 | Moderately liquid |
| CoCos (AT1) | Deeply subordinated bank capital | Fixed-to-reset, perpetual | Can be zero at the point of non-viability | Dealer | Moderately liquid |
| HY preferreds | Junior to all debt | Fixed-to-float, deferrable | Low; equity-like | Exchange or OTC | Moderately liquid |
| CMBS BBB, ABS, CRT | Mezzanine tranches of property, consumer and mortgage pools | Fixed or floating | Collateral performance through the waterfall | Dealer, BWIC | Less liquid |

The recovery column is sourced (Cai and Haque, FEDS Notes, February 23, 2024: post-default value of about 33% for direct loans, 52% for syndicated loans and 39% for HY bonds). The bucket column is *illustrative*: each fund classifies its own holdings, and a 2% position in a liquid HY issue is a different animal from 2% of a 144A orphan.

Two things fall out of the map immediately. First, five of the eleven tabs in Theo's spreadsheet are claims on the same population of sponsor-backed, single-B, floating-rate American companies: the HY bond, the term loan, the CLO tranche that owns the term loan, the direct loan to the company one size smaller, and the BDC that owns the direct loan. Diversification across them is diversification across lawyers. Second, the column that decides what the investor gets back in a bad year (recovery) and the column that decides whether they can get out (liquidity) are exactly the two that index-level yield ignores.

> **Desk Myth vs. Desk Reality.** *Myth:* sector rotation is where multi-asset credit earns its fee. *Reality:* AQR regressed 445 Core/Core-Plus, 44 Global Aggregate and 114 Global Unconstrained bond managers on traditional risk premia (November 1997 to June 2018) and got R² of 90%, 61% and 77%, a credit-loading t-statistic of 14.9 for US Aggregate managers, and residual alphas of 0.10%, 0.01% and 0.09% a year, none significant (AQR, *Alternative Thinking* 4Q18, Exhibit 3; published as Brooks, Gould and Richardson, *Active Fixed Income Illusions*, Journal of Fixed Income, 2020). The fee was paid for credit beta with extra steps. "IDO or it didn't happen" applies to sectors too: a sector tilt is alpha only after you strip the DTS beta it carries (Chapter 8).

> **Trend Watch: The HY Index That Stopped Growing (2004–2026).** *What changed:* public high yield got smaller relative to the rest of leveraged finance, and better rated. Martin Fridson reported the HY index's face value at about \$1.4 trillion in April 2025, essentially unchanged over ten years, with the BB share at 53.55% against a 1996–2024 average of 44.53% (Fridson, CFA Institute *Enterprising Investor*, June 2025). Nuveen's own number: 51% BB at year-end 2024 against 37% in 2004 (Nuveen p.4). *Where the growth went:* institutional leveraged loans reached \$1,549bn at 2025Q4 (9.2% growth over the year), private credit about \$1.4tn, "about one-third of total below-investment-grade debt, excluding bank loans," against \$1,772bn of HY and unrated bonds (Federal Reserve, *Financial Stability Report*, May 2026, citing PitchBook LCD). *What it means for the desk:* the HY index's spread history is a history of a different index. A 2007 spread and a 2025 spread are not the same random variable, because the composition changed under them (§12.3). And the weakest borrowers did not disappear; they moved to the two sleeves that mark least often.

> **[SOURCE EXTRACTION]** *Nuveen p.4:* "the U.S. high yield index has improved in quality over time. At year-end 2024, 51% of the index was rated BB, compared to 37% in 2004"
>
> **Annotation.** This sentence is the most important caveat in the paper, and it sits in the middle of a paragraph about z-scores. A z-score compares today's spread with a historical mean. If the index's rating mix moved from 37% BB to 51% BB, the historical mean belongs to a riskier portfolio, and a "two standard deviations tight" reading is partly a composition artifact. The modern desk responds in two ways: compute valuation on a fixed-mix, composition-adjusted spread (reweight the BB, B and CCC bucket spreads to constant weights), and model the buckets separately whenever their spreads diverge, which in 2026 they did by more than 1,000 bp (§12.9). Nuveen states the problem; the engine in §12.10 makes the fix mandatory.

> **[SOURCE EXTRACTION]** *Ben_Dor p.85:* "Historically, the pricing of this asset class has resembled that of corporate bonds in that it has been driven mainly by spreads rather than rates."
>
> **Annotation.** Ben Dor and coauthors are describing EM hard-currency debt, and the point generalizes to the whole MAC menu: once the Treasury component is hedged or stripped, EM sovereigns, CoCos, preferreds and CMBS mezzanine are all spread instruments whose risk scales with DTS. That is what licenses a common risk unit across sectors (§12.5). The departure: EM sovereigns carry a jump the corporate model lacks, because an index constituent can default for fiscal or political reasons unrelated to the global spread factor, and the index yield then includes a bond trading at 40 (§12.3).

## 12.2 The Return Identity: Four Terms and Two Measures

Nuveen's capital market assumptions start from an identity, not an opinion.

> **[SOURCE EXTRACTION]** *Nuveen p.3:* "Forward return estimates = yield – estimated credit loss – ∆rates MTM – ∆spread MTM"
>
> **Annotation.** Every MAC shop has some version of this line; the value is in being explicit about it. Each term has a different owner and a different failure mode: the yield comes from the index (and includes whatever is defaulting inside it), the credit loss comes from a default forecast and a recovery assumption (the restructuring banker's variable), and the two mark-to-market terms come from rate and spread views. The modern desk keeps the identity and audits each term: it states the measure, uses the right duration for each term, and replaces the recovery-table lookup with a seat-in-the-waterfall estimate. The derivation below shows where each audit item comes from.

**Derivation.** Take a sector proxy with price $P(y)$ and yield-to-worst $y = y^{\text{TSY}} + s$, held for a period $\Delta t$ (years). If it does not default, a second-order expansion of the price gives the holding-period return

$$
r^{\text{no default}} \approx y\,\Delta t \;-\; D^{\text{mod}}\,\Delta y^{\text{TSY}} \;-\; D^{\text{spr}}\,\Delta s \;+\; \tfrac12\,C\,(\Delta y)^2 ,
$$

where $y\,\Delta t$ is the accrual at an unchanged yield (coupon plus pull to par), $D^{\text{mod}}$ is the rate duration, $D^{\text{spr}}$ the spread duration and $C$ the convexity. Two durations appear because they differ: a floating-rate loan has $D^{\text{mod}} \approx 0.25$ (its coupon resets quarterly) but $D^{\text{spr}} \approx 4$ (its spread is fixed until it refinances).

Now add default. With physical default intensity $\lambda^{\mathbb{P}}$, the bond defaults within $\Delta t$ with probability $\text{PD}^{\mathbb{P}} \approx \lambda^{\mathbb{P}}\Delta t$, and on default the holder loses the fraction $L = 1 - R$ of the bond's value (recovery of market value; under recovery of face, replace the loss with $(1 - R/P)$ per unit of price). Taking the physical expectation and dividing by $\Delta t$:

$$
\mathbb{E}^{\mathbb{P}}[r] \;\approx\; y \;-\; \underbrace{\lambda^{\mathbb{P}}\,(1-R)}_{\text{expected credit loss}} \;-\; D^{\text{mod}}\,\frac{\mathbb{E}^{\mathbb{P}}[\Delta y^{\text{TSY}}]}{\Delta t} \;-\; D^{\text{spr}}\,\frac{\mathbb{E}^{\mathbb{P}}[\Delta s]}{\Delta t} \;+\; \tfrac12\,C\,\frac{\mathbb{E}^{\mathbb{P}}[(\Delta y)^2]}{\Delta t}. \tag{12.1}
$$

Nuveen's Figure 2 is (12.1) with the convexity term dropped. Here is what each term is made of.

*The yield* is a market price, so it embeds $\mathbb{Q}$-compensation. By the credit triangle, $s \approx \lambda^{\mathbb{Q}}L + \ell$, where $\ell$ is a liquidity spread. Subtract the cash rate $r$ from (12.1), ignore the mark-to-market terms, and the forward *excess* return is

$$
\mathbb{E}^{\mathbb{P}}[r] - r \;\approx\; \underbrace{(\lambda^{\mathbb{Q}} - \lambda^{\mathbb{P}})\,L}_{\text{credit risk premium}} \;+\; \underbrace{\ell}_{\text{liquidity premium}} \;+\; \text{term premium}.
$$

So the identity is a risk-premium forecast wearing an accounting costume. That tells you the first error. If someone fills the loss term with a CDS-implied default probability, a $\mathbb{Q}$ object, the credit risk premium cancels by construction, and the forecast says the sector earns cash plus its liquidity premium. The loss term must be physical: an agency default forecast, a structural model (Chapter 5) or your own hazard model, multiplied by a *physical* recovery for that seat in the waterfall.

*The loss term* is where the RSSG reader has an edge. A rating-table recovery of 40% applied to everything ignores the FEDS numbers in §12.1: a direct loan that recovers 33% instead of 52% has a 40% larger loss given default ($0.67/0.48 \approx 1.40$) for the same default rate. For CLO tranches the loss is a waterfall output (it depends on the CCC bucket, the OC cushions and the reinvestment period; see Chapter 21), not a table lookup. For an index containing a sovereign in default, the "yield" partly prices that one bond's recovery, and the loss term must too.

*The mark-to-market terms* need horizon care. Nuveen's example is a five-year forecast. If the expected yield change $\Delta$ arrives gradually, linearly over horizon $h$, the yield path is $y_t = y_0 + (\Delta/h)\,t$ and the cumulative return with constant duration is $\int_0^h y_t\,dt - D\,\Delta = y_0 h + \Delta h/2 - D\Delta$. Annualized,

$$
\bar r \;\approx\; y_0 \;-\; \Big(\frac{D}{h} - \frac12\Big)\Delta .
$$

So reinvestment at the higher yield offsets half the move per year, and at $D \approx h/2$ a gradual rate rise costs nothing over the horizon. Subtracting $D\Delta/h$ without the $+\Delta/2$ overstates the drag; subtracting $D\Delta$ in a single year double-counts it. For floating-rate sectors the rates term is nearly zero but the yield term moves: the loan's coupon follows the forward SOFR path, so its "yield" in (12.1) should be the forward-rate-implied coupon, not today's.

**The worked example.** Nuveen's Figure 3 (Nuveen p.3; Bloomberg US Corporate High Yield Index, as of November 19, 2025) prints five numbers, 6.97, 2.55, 0.37, 0.49 and 3.56, and they satisfy $6.97 - 2.55 - 0.37 - 0.49 = 3.56$. The text layer of the PDF lists the labels in the reverse of the value order, so the assignment of 2.55 and 0.49 between "expected credit loss" and "∆spread MTM" cannot be read off the extraction. Economics decides it. An expected loss of 2.55% a year at 40% recovery implies a physical default rate of about 4.25% a year, which is in the range of long-run speculative-grade experience (approx.). An expected loss of 0.49% implies about 0.8%, implausible for an index that is about half single-B and below. Meanwhile 2.55% a year of spread mark-to-market over five years, at a spread duration near 3.2, would require roughly 400 bp of widening. The consistent reading is: yield 6.97%, expected credit loss 2.55%, rates MTM 0.37%, spread MTM 0.49%, forward return 3.56%. We state the reading and the reason, because a chart is data and a guess is not.

Now the uncomfortable part. Nuveen's Figure 6 reports forward returns, volatilities and forward Sharpe ratios for six efficient portfolios. If the ratio is (return − cash)/volatility, each row implies a cash rate: $5.11 - 0.26 \times 5.50 = 3.68$, $6.20 - 0.40 \times 6.29 = 3.68$, and the other four land between 3.65% and 3.70%. That is our inference, not Nuveen's statement (the paper's endnote defines the ratio; check it before you quote it). If it holds, high yield's five-year forward return of 3.56% sits *below* cash. The 20% minimum on HY in Nuveen's constraint table (Figure 5, Nuveen p.6) is then not something the optimizer wants; it is something the client wants, and the optimizer pays for it with every other weight. That is fine. It is also exactly the sort of thing a spec should make visible, and §12.10 prints the shadow price.

> **Ways This Blows Up.** *Callable bonds and preferreds:* yield-to-worst already assumes the issuer calls when it is optimal to do so, and a spread MTM computed with yield-to-maturity duration overstates the price sensitivity of a bond that is about to be called. Use option-adjusted spread duration. *Perpetuals and CoCos:* the yield is a yield-to-call, and the extension risk is the trade; a CoCo whose call is skipped becomes a much longer instrument overnight. *Defaulted constituents:* an index yield averaged over bonds at 40 is a recovery forecast you didn't make (§12.3).

## 12.3 Spread per Unit of What? Cross-Sector Valuation

Theo's first instinct was right: yield is the wrong ranking variable. But "spread" is not the right one either, because a spread is compensation for three different things.

> **[SOURCE EXTRACTION]** *Ben_Dor p.168:* "We model a bond's OAS (to Treasuries) with three variables: a variable reflecting expected default cost, a variable reflecting expected liquidity cost, and a market-wide variable unrelated to the bond's attributes representing the market-wide risk premium demanded by investors."
>
> **Annotation.** This is the decomposition a MAC valuation should run sector by sector: $s = \text{EL} + \ell + \pi$, with expected default cost (the loss term of §12.2), expected liquidity cost (the LCS of Ben Dor chapter 5, a round-trip transaction cost amortized over the holding period) and the market-wide risk premium $\pi$. Only $\pi$ is the reward for bearing systematic spread risk. The modern desk departs in two places: it estimates EL at the seat level, not from a sector average, and it lets the liquidity term switch on in stress, because Ben Dor finds (p.177) that "liquidity cost provides additional explanatory power for the cross-sectional variation in high-yield spreads only during periods of market stress."

The decomposition suggests three ratios, each answering a different question.

**Ratio 1: what are you paid for the loss?** The *break-even default rate* is the annual default rate at which the spread exactly pays for losses:

$$
\lambda^{\text{BE}} \;=\; \frac{s}{1 - R}.
$$

It is the credit triangle solved for the intensity, and it is the number Mags computes in her head. Take the CCC & lower OAS on October 15, 2026, 12.78% (ICE BofA via FRED, series BAMLH0A3HYC), and a 35% recovery, *illustrative*: $\lambda^{\text{BE}} = 0.1278/0.65 \approx 19.7\%$ a year. The question is no longer "is 1,278 bp wide?" but "will more than a fifth of these issuers default every year?" The excess spread $s - \text{EL}$ and the coverage ratio $s/\text{EL}$ are the same idea in other units.

**Ratio 2: what are you paid per unit of risk?** In DTS units (Chapter 8; Ben Dor p.50), a sector's excess-return volatility is $\sigma(r^x) \approx \text{DTS}\cdot\sigma(\Delta s/s)$, where $\text{DTS} = D^{\text{spr}}s$ and $\sigma(\Delta s/s)$ is the volatility of *relative* spread changes. Its annual excess carry is roughly $s - \text{EL}$. Divide:

$$
\frac{s - \text{EL}}{D^{\text{spr}}\,s\,\sigma(\Delta s/s)} \;=\; \frac{1 - \text{EL}/s}{D^{\text{spr}}\,\sigma(\Delta s/s)}.
$$

The spread level cancels. If relative spread volatility is roughly common across sectors (the empirical content of DTS), then carry per unit of risk is set by spread duration and by the share of the spread that is eaten by expected loss, not by how wide the spread is. Short-dated, high-recovery paper wins on this ratio, which is the same conclusion the short-maturity HY literature reaches by a longer road. A wider spread is not a better deal; it is a bigger bet of the same quality.

> **[SOURCE EXTRACTION]** *Ben_Dor p.50:* "a portfolio with a weighted spread of 200 bps and spread duration of two years is equally risky as a portfolio with a spread of 100 bps and spread duration of four years."
>
> **Annotation.** Both portfolios have DTS of $4 \times 0.01 = 2 \times 0.02 = 0.04$ years, so their excess-return volatility is the same if relative spread changes have the same volatility. For MAC this is the license to put a floating-rate loan (short rate duration, four-year spread duration), a CLO BBB tranche and an EM sovereign on one risk axis. The modern caveat: DTS was estimated on corporate bonds. For tranches, relative spread changes are not proportional across the capital structure in stress (mezzanine tranche spreads gap), and for direct lending the "spread change" is never observed at all, so the risk unit must be imported from a proxy (§12.5).

**Ratio 3: what is left after you trade?** A sector with round-trip liquidity cost $\text{LCS}$ (decimal of price; Ben Dor p.111 defines liquidity as "the cost of a roundtrip institutional-size transaction in a bond") held for $T_{\text{hold}}$ years pays $s - \text{EL} - \text{LCS}/T_{\text{hold}}$ per year. A 2-point round trip on CMBS BBB held for two years costs 100 bp a year, which can be more than its excess spread over EL. A desk that rotates sectors quarterly should rank sectors on this ratio, not on spread, because it is the one the P&L sees.

**Mean reversion and the z-score.** Nuveen is careful here:

> **[SOURCE EXTRACTION]** *Nuveen p.4:* "A commonly used metric for assessing credit relative value is the z-score, which indicates the number of standard deviations from the historical average. However, relying solely on this measure is insufficient"
>
> **Annotation.** The derivation below shows why the z-score is necessary but not sufficient: it is a sufficient statistic only if the long-run mean is constant, and the HY index's long-run mean moved when the index's rating mix moved (§12.1). Nuveen supplements z-scores with spread transition probabilities and fundamentals; the modern desk adds the composition adjustment and a regime model (§12.4), because the speed of mean reversion is itself regime-dependent.

Model the spread as Ornstein–Uhlenbeck under $\mathbb{P}$: $ds_t = \kappa(\theta - s_t)\,dt + \sigma\,dW_t$, with speed $\kappa$ (per year), long-run mean $\theta$ and volatility $\sigma$. Then

$$
\mathbb{E}^{\mathbb{P}}[s_h \mid s_0] = \theta + (s_0 - \theta)\,e^{-\kappa h}, \qquad \operatorname{Var}(s_\infty) = \frac{\sigma^2}{2\kappa}, \qquad t_{1/2} = \frac{\ln 2}{\kappa}.
$$

Define the stationary z-score $z = (s_0 - \theta)/\sigma_s$ with $\sigma_s = \sigma/\sqrt{2\kappa}$. The expected spread change over the horizon, which is exactly the input to the spread MTM term of (12.1), is

$$
\mathbb{E}^{\mathbb{P}}[\Delta s] \;=\; -\,z\,\sigma_s\,\big(1 - e^{-\kappa h}\big).
$$

So a z-score becomes a return forecast only after you multiply by three things it does not contain: the stationary volatility, the reversion speed and the horizon. A $z = -2$ in a sector with a four-year half-life barely moves a one-year forecast. And all of it is conditional on $\theta$ being the right mean. Nuveen's "credit spread transition probability" is the discrete version: bucket spreads into states, estimate $P_{ij} = \Pr(s_{t+1} \in j \mid s_t \in i)$, and read the $h$-step distribution from $P^h$. It inherits the same assumption.

**The composition adjustment.** Hold the bucket spreads fixed at their 2025 year-end levels (ICE BofA via FRED: BB 169 bp, B 301 bp, CCC 885 bp) and change only the weights. A 2004-style mix of 37% BB, 45% B and 18% CCC gives $0.37(169) + 0.45(301) + 0.18(885) \approx 357$ bp. A 2025-style mix of 53% BB, 36% B and 11% CCC gives about 295 bp. The actual index printed 281 bp. The B and CCC weights here are *illustrative* (only the BB shares are sourced), but the lesson is not: about 60 bp of "tightness" against long history is composition, not valuation. Fridson made the complementary point about tails: applying March 2020's category spreads to the April 2025 ratings mix still produces about +1,093 bp, against the actual +1,087 bp peak of March 23, 2020 (Fridson, CFA Institute *Enterprising Investor*, 2025). A better-rated index has a lower mean; it does not have a thinner tail.

Ines put it in her terms. "Comparing today's HY spread to 2007's is comparing a poker room to the same room after they banned half the drunks. The pots are smaller. The bad beats are not."

> **Ways This Blows Up.** ROBO is told to "maximize yield subject to 6% volatility." It buys the EM sovereign index at a 9% yield, which is 9% because one country in the index is in default and its bonds trade at 40. Nuveen warns about exactly this (Nuveen p.7): "A compelling yield on the emerging markets sovereign debt index could be a result of distressed bonds from a single country experiencing a significant fiscal or currency crisis." The precise spec computes sector yields ex-distressed (constituents below a price of 50 removed and modeled separately with their own recovery), caps single-issuer DTS share, and reports the yield contribution of the top five issuers.

### Deep-Dive Resource Graph (§12.1–12.3)

**Podcasts**

- *Bloomberg Odd Lots* has run several conversations on the growth of private credit relative to public high yield. No specific episode was verified for this edition; search the archive by topic rather than relying on a citation here.

**Practitioner Writing**

- Nuveen (Mark Zheng), *Multi-asset credit investing: A quantitative framework*, Q4 2025 (on the shelf; data as of November 19, 2025).
- Martin Fridson, "Think We've Seen the Last 1,000 bps High-Yield Spread? Think Again," CFA Institute *Enterprising Investor* (2025): https://rpc.cfainstitute.org/blogs/enterprising-investor/2025/think-weve-seen-the-last-1000-bps-high-yield-spread-think-again
- AQR, *Alternative Thinking* 4Q18, "The Illusion of Active Fixed Income Alpha": https://www.aqr.com/-/media/AQR/Documents/Alternative-Thinking/Alternative-Thinking-4Q18-Illusion-of-Active-Fixed-Income-Alpha.pdf

**Academic Papers**

- Brooks, Gould and Richardson (2020), *Active Fixed Income Illusions*, Journal of Fixed Income 29(4): https://lbsresearch.london.edu/1510
- Cai and Haque (2024), *Private Credit: Characteristics and Risks*, FEDS Notes: https://www.federalreserve.gov/econres/notes/feds-notes/private-credit-characteristics-and-risks-20240223.html
- Ben Dor, Dynkin, Hyman and Phelps, *Quantitative Credit Portfolio Management* (shelf: pp. 50, 85, 111, 168, 177).

**Data & Code**

- ICE BofA OAS series on FRED (BAMLH0A0HYM2, BAMLH0A1HYBB, BAMLH0A2HYB, BAMLH0A3HYC): https://fred.stlouisfed.org/series/BAMLH0A0HYM2
- Federal Reserve, *Financial Stability Report* index: https://www.federalreserve.gov/publications/financial-stability-report.htm

## 12.4 Regimes: A Two-State Hidden Markov Model for Credit

Kaz fit the regime model on Tuesday and presented it on Wednesday. "Two states. The calm state is ninety-seven percent persistent. The stress state lasts, on average, one month."

"So your model thinks a bad month is a typo," Ines said.

She was right, and the reason is a one-line derivation. In a Markov chain, the probability of staying in state $k$ for exactly $n$ periods is $P_{kk}^{\,n-1}(1 - P_{kk})$, a geometric distribution, so the expected duration of a visit is

$$
\mathbb{E}[\text{duration}_k] \;=\; \sum_{n \ge 1} n\,P_{kk}^{\,n-1}(1-P_{kk}) \;=\; \frac{1}{1 - P_{kk}} .
$$

Kaz's 97% calm state lasts 33 months on average; a stress state with $P_{kk} = 0$ lasts one month, which means the model has learned that stress is an outlier, not a state. April 2025 says otherwise: the HY OAS went from 259 bp on January 22 to 461 bp on April 7, the VIX closed at 52.33 on April 8, and the drawdown in the HY total-return index ran from February 28 to April 7 (ICE BofA and CBOE via FRED). That is a regime with a beginning, a middle and an end, spread over two months. A model that calls it a typo will be fully invested in the beginning and fully hedged in the end.

> **[SOURCE EXTRACTION]** *Bolder p.524:* "In the finance and macroeconomic setting, they are used to describe business-cycle and high and low volatility state mechanics."
>
> **Annotation.** Bolder is introducing Markov chains for credit-risk work, where the usual object is a rating-transition matrix observed directly. In MAC allocation the chain is *hidden*: nobody publishes the regime, so it must be inferred from returns. Every formula below is the rating-migration machinery with one extra layer, a likelihood that turns observed returns into probabilities over unobserved states. The modern departure is about use, not math: the regime probability is an input to capital market assumptions and to a tilt budget (§12.8), not a switch that moves the whole book.

**The model.** Let $z_t \in \{1, 2\}$ be the hidden regime in month $t$ with transition matrix $P$, $P_{jk} = \Pr(z_{t+1} = k \mid z_t = j)$. The observation is the vector of sector excess returns $r_t \in \mathbb{R}^n$, and conditional on the regime it is Gaussian: $r_t \mid z_t = k \sim \mathcal{N}(\mu_k, \Sigma_k)$. Write $f_t = \big(\phi(r_t; \mu_1, \Sigma_1),\, \phi(r_t; \mu_2, \Sigma_2)\big)^{\top}$ for the two conditional densities and $\xi_{t\mid s}$ for the vector of regime probabilities at $t$ given information $\mathcal{F}_s$.

*Filter (Hamilton 1989).* Predict, then update:

$$
\xi_{t \mid t-1} = P^{\top}\,\xi_{t-1 \mid t-1}, \qquad
\xi_{t \mid t} = \frac{\xi_{t \mid t-1} \odot f_t}{\mathbf{1}^{\top}\big(\xi_{t \mid t-1} \odot f_t\big)},
$$

where $\odot$ is the elementwise product. The denominator is the one-step predictive density of $r_t$, so the log-likelihood is $\ell(\Theta) = \sum_t \ln \mathbf{1}^{\top}(\xi_{t\mid t-1} \odot f_t)$. In code, compute $\ln f_t$, subtract its maximum over states before exponentiating, and add the maximum back into the likelihood; otherwise an eleven-dimensional density in a stress month underflows to zero and the filter divides by it.

*Smoother.* The backward pass gives $\gamma_t(k) = \Pr(z_t = k \mid \mathcal{F}_T)$ and the pairwise probabilities $\xi_t(j, k) = \Pr(z_t = j, z_{t+1} = k \mid \mathcal{F}_T)$.

*EM (Baum–Welch).* Given the smoothed quantities, the M-step is weighted counting and weighted moments:

$$
\hat P_{jk} = \frac{\sum_{t<T} \xi_t(j,k)}{\sum_{t<T} \gamma_t(j)}, \qquad
\hat\mu_k = \frac{\sum_t \gamma_t(k)\, r_t}{\sum_t \gamma_t(k)}, \qquad
\hat\Sigma_k = \frac{\sum_t \gamma_t(k)\,(r_t - \hat\mu_k)(r_t - \hat\mu_k)^{\top}}{\sum_t \gamma_t(k)} .
$$

Each iteration raises the likelihood. It converges to a local maximum, so initialize sensibly (the code labels the worst 20% of months by cross-sectional average return as stress) and align labels at the end (state 1 is the one with the higher mean excess return), because EM is indifferent to which state it calls "1."

**From regimes to capital market assumptions.** Given today's filtered probabilities $\xi_{t\mid t}$, the regime distribution $j$ months ahead is $(P^{\top})^j \xi_{t\mid t}$; average over the horizon to get $\bar\pi^{(h)} = \tfrac1h \sum_{j=1}^{h} (P^{\top})^j \xi_{t\mid t}$. The predictive mean and covariance of next-period returns follow from the laws of total expectation and total variance:

$$
\mu^{(h)} = \sum_k \bar\pi^{(h)}_k\,\mu_k, \qquad
\Sigma^{(h)} = \sum_k \bar\pi^{(h)}_k\,\Sigma_k \;+\; \sum_k \bar\pi^{(h)}_k\,(\mu_k - \mu^{(h)})(\mu_k - \mu^{(h)})^{\top}. \tag{12.2}
$$

The second term matters. When the two regimes have very different means, uncertainty about *which* regime you are in is itself a source of covariance, and it loads on every sector in the same direction: it is the correlation-goes-to-one effect, derived instead of asserted. As $h \to \infty$, $\bar\pi^{(h)}$ converges to the stationary distribution $\pi^{\star}$ solving $\pi^{\star\top} = \pi^{\star\top}P$, and (12.2) collapses to the unconditional moments, which is the strategic allocation's view. The tactical overlay is the difference between the two. (One caveat for long horizons: regime persistence makes monthly returns serially correlated, so the variance of an $h$-month cumulative return exceeds $h\,\Sigma^{(h)}$. Equation (12.2) is the per-period predictive distribution, which is what a one-year tilt needs.)

> **[SOURCE EXTRACTION]** *Dynkin p.617:* "While the corporate index has average returns of –8.07%/yr in drawdown episodes and 4.12%/yr in recovery times, the EMC strategy performed well in both regimes: 11.53%/yr in credit drawdowns and 4.30%/yr in recoveries."
>
> **Annotation.** Dynkin and coauthors are reporting the regime-conditional performance of an equity-momentum-in-credit strategy (EMC), and the first half of the sentence is the input this section needs: the corporate index's mean return differs by about 12 percentage points a year across drawdown and recovery regimes. That gap is what makes $\mu_1 \ne \mu_2$ estimable and what gives the mixture term in (12.2) its bite. The second half is a preview of §12.8: a signal that works in both regimes is worth more to a MAC book than one that works only in calm, because the regime filter will always be a month late.

**What goes wrong.** Four errors account for most of the regime models that look brilliant in backtests and do nothing live.

1. *Leakage through smoothing.* The smoothed $\gamma_t$ uses returns after $t$. A backtest that trades on $\gamma_t$ knows that March 2020 was the bottom. Trade on the filtered $\xi_{t\mid t}$, and act with a one-period delay. Nystrup's 2014 DTU thesis (*Regime-Based Asset Allocation: Do Profitable Strategies Exist?*) tested exactly this: a two-state Gaussian HMM still beat static rebalancing out of sample after costs and with an action delay, which is the honest version of the claim.
2. *Too many states.* Three hundred monthly observations support two states with full covariance in a handful of dimensions. With eleven sectors, each state's covariance has 66 free entries; three states with full covariance is about 200 parameters. Use $K = 2$, or impose the DTS factor structure of §12.5 on each $\Sigma_k$.
3. *Label switching* between re-fits, which silently flips the sign of the tactical overlay. Align labels every time.
4. *Smoothed inputs.* Fit the HMM on an appraisal-smoothed private series and the calm state absorbs it: the series never moves, so the model concludes it is always calm. Desmooth first (§12.5), or leave the private sleeve out of the regime model and let it inherit the regime through its factor loading.

Two-state Gaussian HMMs for asset allocation have a respectable lineage: Hamilton (1989) for the filter; Ang and Bekaert (2002) and Guidolin and Timmermann (2007) for regime-switching allocation; Kritzman, Page and Turkington (2012) for the practitioner case; Nystrup, Hansen, Madsen and Lindström (2015) and Nystrup, Madsen and Lindström (2018) for adaptive estimation; and Bernis, Carassus, Docq and Scotti (2015) for credit allocation specifically, with a two-state hidden chain driving a credit benchmark. Bohn and Stein state the motivation in one sentence (Bohn_Stein p.492): "the processes that drive credit risk during times of extreme stress may be quite different than those that drive credit risk during normal or even 'pretty bad' times."

> **Trend Watch: The 2026 CCC Decompression.** *What changed:* the high-yield market split in two while its headline spread stayed calm. ICE BofA option-adjusted spreads (FRED): the CCC & lower OAS went from 7.46% at year-end 2024 to 8.85% at year-end 2025 and 12.78% on October 15, 2026, a post-2023 high. Over the same dates the BB OAS went 1.86%, 1.69%, 1.97%, and the overall HY OAS sat at 3.23%. The CCC/BB spread ratio rose from 4.0 to 5.2 to 6.5; the CCC−BB gap widened from 560 bp to 716 bp to 1,081 bp. Year-to-date total returns to October 15, 2026: CCC −5.21%, BB +0.33%, HY index +0.15%. Around it, the 10-year Treasury yield was 5.10% and the effective fed funds rate had moved from 3.62% (May 19) to 3.88% (September 17) (FRED, DGS10 and DFF). The Federal Reserve's May 2026 *Financial Stability Report* noted that software had become the largest sector in private-credit portfolios and that secondary leveraged-loan spreads rose, "reflecting a high concentration of leveraged loan borrowers in the software industry." *What it means for the desk:* a two-state model on the HY *index* reads October 2026 as calm, because the index spread is near its average. A model on the BB, B and CCC *vector* sees a different regime: low common-factor volatility, very high dispersion. That is why the reference implementation plants regimes that differ in idiosyncratic volatility, not only in means (§12.10). The dispersion regime is where the loss term of (12.1) diverges across buckets, and where index-level MAC models lose the plot.

## 12.5 Covariance You Can Trust: DTS Structure, EWMA, Shrinkage and Desmoothing

The covariance matrix is where MAC models fail quietly. Expected returns are argued about in investment committee; covariances are taken from the risk system and nobody asks. They should, because the covariance of eleven credit sectors is mostly one number (the common spread factor's variance) multiplied by things that change: spread levels, durations and the marking practices of the people who report the returns.

**Step 1: structure it with DTS.** From §12.3, a sector's excess return is $r^x_i \approx -D^{\text{spr}}_i\,\Delta s_i = -\text{DTS}_i\,u_i$ with $u_i = \Delta s_i/s_i$ the relative spread change. Stack the sectors, let $\Omega = \operatorname{Cov}(u)$, and

$$
\Sigma^{x} = \operatorname{diag}(\text{DTS})\;\Omega\;\operatorname{diag}(\text{DTS}). \tag{12.3}
$$

For total returns add the rates block, $\Sigma = \Sigma^x + \sigma_{y}^2\,D^{\text{mod}}D^{\text{mod}\top}$, treating the Treasury factor as independent of the spread factor (an approximation; in risk-off months the correlation is negative, which flatters long-duration IG and does little for floating-rate loans). The reason to estimate $\Omega$ instead of $\Sigma$ directly is stability: relative spread changes have far more stable volatility across spread levels than absolute changes do, which is the empirical finding behind DTS. When spreads double, (12.3) doubles every sector's volatility automatically through $\text{DTS}$, rather than waiting three years for the sample covariance to notice.

> **[SOURCE EXTRACTION]** *Ben_Dor p.63:* "Traditionally, investment-grade credit portfolios are managed based on contributions to duration, while high-yield portfolios are managed based on market value weights. Using contributions to DTS across both markets could help bring consistency to this portfolio construction process."
>
> **Annotation.** Ben Dor and coauthors wrote this about core-plus mandates combining IG and HY, and MAC is the same problem with eleven markets instead of two. Market-value weights treat 10% in CLO BBB and 10% in ABS as the same bet; DTS contributions show the CLO tranche carrying several times the spread risk. The modern desk sets risk budgets in DTS contributions (§12.6) and reports market-value weights only to the client. The caveat for securitized sleeves: tranche DTS is a local measure, and mezzanine tranches gap in stress (their spread change is not proportional), so the DTS-implied volatility of a CLO BBB is a floor.

**Step 2: weight recent observations.** Nuveen does this explicitly:

> **[SOURCE EXTRACTION]** *Nuveen p.4:* "At Nuveen, we use a weighted covariance matrix, which gives more importance to more recent observations."
>
> **Annotation.** The standard implementation is the exponentially weighted moving average below. The paper does not give its decay parameter, which is the parameter that matters: it sets how fast the matrix forgets 2020 and how fast it learns April 2025. The modern desk chooses the decay by out-of-sample likelihood rather than taste, applies it to relative spread changes rather than returns, and shrinks the result (step 3), because a fast-decaying estimator has a small effective sample.

The EWMA recursion on monthly relative spread changes $u_t$ is

$$
\Omega_t = \lambda\,\Omega_{t-1} + (1-\lambda)\,u_t u_t^{\top}, \qquad 0 < \lambda < 1 ,
$$

with weights $(1-\lambda)\lambda^j$ on the observation $j$ months back. The weights sum to one; the effective number of observations is about $(1+\lambda)/(1-\lambda)$ and the half-life is $\ln 2 / \ln(1/\lambda)$. At $\lambda = 0.97$ monthly, the half-life is about 23 months and the effective sample about 66 months.

Mags watched Kaz tune the decay. "Back in my day we did multi-asset credit too. It was called 'whatever the dealer had left on Friday.' The covariance matrix was me remembering which dealers stopped answering the phone in 1998." She paused. "Your thing does that automatically. With a half-life. Fine."

**Step 3: shrink it.** Eleven sectors have $11 \times 12/2 = 66$ distinct covariance entries. A 66-month effective window gives you roughly one effective observation per parameter, which is the regime in which sample covariance matrices produce optimizers that bet heavily on noise. Shrink toward a structured target (Ledoit and Wolf 2004):

$$
\hat\Omega = \delta\,F + (1 - \delta)\,S, \qquad 0 \le \delta \le 1 ,
$$

where $S$ is the sample (or EWMA) matrix and $F$ is a one-factor target: with market factor $m$ (the equal-weighted average of the $u_i$), $F_{ij} = \beta_i\beta_j\sigma_m^2$ off the diagonal and $F_{ii} = S_{ii}$. The target is positive semidefinite because each residual variance $S_{ii} - \beta_i^2\sigma_m^2$ is nonnegative by Cauchy–Schwarz, and a convex combination of PSD matrices is PSD. The Ledoit–Wolf intensity is

$$
\delta^{\star} = \max\!\Big(0,\; \min\!\Big(1,\; \frac{\hat\pi - \hat\rho}{\hat\gamma\,T}\Big)\Big),
$$

with $\hat\pi = \sum_{ij}\widehat{\operatorname{AVar}}(\sqrt{T}s_{ij})$ the estimation noise in $S$, $\hat\gamma = \|F - S\|_F^2$ the misspecification of the target, and $\hat\rho$ the covariance between target and sample errors. The reference code uses the diagonal part of $\hat\rho$ only (the target's diagonal equals the sample's, so those terms carry no shrinkage benefit) and drops the off-diagonal $\hat\rho$ terms. That is a documented simplification which errs toward slightly more shrinkage, the safe direction for an optimizer.

**Step 4: desmooth the private sleeve.** Nuveen confronts the absence of an honest return series for direct lending directly:

> **[SOURCE EXTRACTION]** *Nuveen p.9:* "Middle market direct lending (Private Credit): Proxy Index using S&P UBS Leveraged Loan B Index."
>
> **Annotation.** This is the right instinct: when the asset's own return series is a sequence of appraisals, import the risk from the closest traded thing. The modern desk treats the proxy as a *floor* rather than an estimate. Middle-market borrowers are smaller than single-B syndicated borrowers, with a mean interest coverage of about 2.0x against 2.7x for leveraged-loan borrowers and a post-default value of about 33% against 52% (Cai and Haque, FEDS Notes, 2024). The same spread move costs a direct-lending book more. When the sleeve's own NAV series must be used (for a BDC, say), desmooth it.

Getmansky, Lo and Makarov (2004) model the reported return as a moving average of true returns:

$$
r^o_t = \sum_{j=0}^{k} \theta_j\, r_{t-j}, \qquad \theta_j \ge 0, \qquad \sum_{j=0}^{k} \theta_j = 1 .
$$

If true returns are serially uncorrelated with variance $\sigma^2$ and $r_t = \beta m_t + e_t$ for a market factor $m_t$, then

$$
\operatorname{Var}(r^o_t) = \sigma^2 \sum_j \theta_j^2 \equiv \xi\,\sigma^2, \qquad
\operatorname{Cov}(r^o_t, m_t) = \theta_0\,\beta\,\sigma_m^2, \qquad
\operatorname{Corr}(r^o_t, m_t) = \frac{\theta_0}{\sqrt{\xi}}\,\operatorname{Corr}(r_t, m_t).
$$

Three consequences, each of which an optimizer will exploit. Reported volatility is understated by $\sqrt{\xi} \le 1$. Reported contemporaneous beta is understated by $\theta_0$, a bigger factor; summing betas on current and lagged market returns (Dimson 1979) recovers $\beta\sum_j\theta_j = \beta$. And reported correlation is understated by $\theta_0/\sqrt{\xi}$. The long-horizon variance is *not* understated: because $\sum_j\theta_j = 1$, a year of reported returns adds up to about a year of true returns. The naive annualization $\sqrt{12}\,\sigma_{\text{monthly}}$ is what lies, because it assumes the serial correlation that smoothing created is zero.

For the common AR(1) smoothing model $r^o_t = (1 - \phi)\,r_t + \phi\,r^o_{t-1}$, the weights are $\theta_j = (1-\phi)\phi^j$, so

$$
\xi = \frac{(1-\phi)^2}{1 - \phi^2} = \frac{1-\phi}{1+\phi}, \qquad \theta_0 = 1 - \phi, \qquad \frac{\theta_0}{\sqrt{\xi}} = \sqrt{1 - \phi^2}, \qquad \hat r_t = \frac{r^o_t - \phi\,r^o_{t-1}}{1 - \phi} .
$$

At $\phi = 0.8$, which is not an exotic level of persistence for appraisal-based marks, $\xi = 1/9$: true volatility is three times reported, true beta five times reported contemporaneous beta, and the correlation is understated by 40%. Kaz's 1.9% becomes about 5.7%, close to the loan proxy. Mags's verdict on the original number: "Measured by the fund or by the fund's lawyer?" The formula's verdict: $\sigma_{\text{true}} = \sigma_{\text{reported}}/\sqrt{\sum_j \theta_j^2}$, whoever measured it.

> **Ways This Blows Up.** *Desmoothing the wrong series.* A listed BDC's share price is marked by the market every day; desmoothing it inflates a volatility that was never smoothed. Desmooth the NAV series and treat the price-to-NAV discount as a separate liquidity signal (Chapter 20). *Mixing frequencies.* Desmoothing a quarterly NAV series and dropping it into a monthly covariance matrix aligns nothing; aggregate the public series to quarterly first. *Non-invertible fits.* The moving-average weights are identified only up to reversal ($\theta$ and its mirror image give the same autocorrelations); the recursion that recovers true returns explodes for the non-invertible one. The code checks the roots and refuses rather than guesses.
