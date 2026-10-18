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
