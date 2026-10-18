# Chapter 12: Multi-Asset Credit Allocation


## 12.0 Cold Open: Seven Piles, One Bet

*(The desk, the sleeve, its weights and every line of dialogue are fictional. The recovery figures Mags quotes are the Federal Reserve's, cited in §12.1.)*

The sleeve arrived on a Monday as a spreadsheet with eleven tabs and one comment: "Make it efficient. —PM."

It was Monday 12 October 2026, the start of Theo's fourth week, and the sleeve was not a proposal. It was a live multi-asset credit book that the platform ran for an outside client, and its weights column already summed to one hundred.

Theo opened it the way he used to open a data room, looking for the tab somebody hoped he would skip. High yield. Leveraged loans. EM sovereigns, BB to B. EM corporates. CoCos. High-yield preferreds. ABS. CMBS BBB. CLO BBB to B. Credit-risk transfer. And at the bottom, in a different font, as if added by a different person: middle-market direct lending, held through a perpetual BDC. Its current weight was thirty-five percent *(illustrative)*.

Kaz had already run the optimizer. "Good news. Max Sharpe puts thirty-five percent in direct lending, which is the upper bound. Its volatility is one point nine percent. It is the best asset I have ever seen."

"So the optimizer agrees with whoever bought it," Theo said.

"Volatility of what?" Mags asked from two desks over, without turning around. "The quarterly letter?"

"Of the return series."

"The return series is a valuation committee with an appraisal model and a deadline. Back in my day we called that a mark. Now you call it a covariance matrix."

"It is the data," Kaz said, a little stiffly. "Twenty-six quarters of it. One negative quarter, minus forty basis points, in 2022 *(illustrative)*. I did not make it up."

"Nobody said you made it up," said Ines. "What's it made of?"

Kaz looked at the column as if it might answer for itself. "Net asset value per share, quarterly, from the fund's filings."

"And who makes the net asset value?"

That one Theo knew, because he had spent six years on the other side of it. "The adviser marks the loans. A valuation firm reviews some of the marks. The board signs. Then the filing comes out about six weeks after the quarter ends." He shrugged. "At PJT, when a lender group sent us its marks, the first question anybody asked was which lender had a fund to raise."

Ines rolled her chair over, looked at the eleven tabs, and did what she did with any new hand: she counted the players. "Seven piles of the same bet with different lawyers attached. HY, loans, CLO mezz, the BDC: same sponsors, same borrowers, different seats in the waterfall. EM and preferreds are the same bet in a different accent. So. What's the pot, what are the odds, and who at this table knows more than you?"

Theo did not answer that yet. He did what he had done every Monday morning for six years, which was to read a capital structure aloud from the top, as if it were one company. It was not one company, but the habit was stronger than the facts.

"Leveraged loans. First-lien term loan B, floating rate, sponsor-backed."

"Fifty-two," Mags said, still facing her own screens. "Post-default value, cents on the dollar. The high-yield bonds below them in the same kind of company, thirty-nine."

"CLO, BBB to B. A mezzanine slice of a pool of those same term loans."

"Whatever the waterfall leaves after the coverage tests have finished eating. Ask me the vintage and I'll tell you how hungry they were."

"Direct lending, through the BDC. First-lien unitranche, to the company one size smaller."

"Direct loan, thirty-three," said Mags, "and that is the Fed's number, not mine."

Kaz frowned. "Thirty-three for a first lien? Below the unsecured bonds?"

"First lien on less," said Mags. "Smaller companies, thinner interest coverage, fewer people who want the assets on the day you need to sell them. Seniority is a seat. It is not a guarantee that the room has anything in it."

Theo kept going. "EM sovereigns, BB to B. Unsecured, collective action clauses."

"Whatever the IMF program says, after two years of meetings."

"CoCos."

"Zero, if a regulator decides so on a Sunday," Mags said, and nobody on the desk needed the date (it was 19 March 2023, and the bank was Credit Suisse).

"Preferreds."

"Equity that pays a coupon until it doesn't."

"ABS, CMBS BBB, credit-risk transfer."

"Collateral through a waterfall. Ask me after the trustee report."

Theo had written the answers in a column down the left margin of his notebook. Eleven tabs had produced perhaps five distinct seats, and several of them were the same population of sponsor-backed, single-B, mostly floating-rate American companies seen through different documents. He drew a bracket around the bonds, the loans, the CLO tranche and the BDC and wrote *one borrower set* next to it.

"Here is what bothers me," he said. "The PM wrote 'make it efficient' on a book that already holds thirty-five percent of the BDC. So the question isn't whether to buy it. We own it."

"Then the question is whether to stay in line," said Ines. She had the fund's tender terms open already, which meant she had been waiting for someone to ask. "It buys back up to five percent of its shares a quarter. If more than five percent of the holders want out in the same quarter, everyone gets a slice of what they asked for. You don't own an asset with a volatility of one point nine. You own a place in a queue, and the length of the queue is set by people you've never met."

"The pot is about six percent," Theo said, scrolling. "The efficient frontier runs from five-eleven to six-twenty."

"And the error bars on your expected returns?"

Theo did not answer, which was the answer.

He took the USB stick out of his pocket, the one with the 13-week cash flow model, and set it on the desk like a chip. "In restructuring, nobody asked me which sector had the best yield. They asked what the claim recovers, where it sits, and how fast you can get out. That's three numbers. This spreadsheet has eleven tabs and none of the three."

"Then that's the job," Ines said.

The question this chapter answers: **how do you allocate across credit sectors when every input lies in its own way? The index yields include defaulted constituents, the volatilities are appraised, the correlations change with the weather, and one of the assets can only be sold once a quarter, five percent at a time.**

The answer comes in three movements. The inputs turn out to be an accounting identity with four terms, each owned by a different person and each wrong in its own direction (§12.2–12.3); the covariance and the regime are estimates whose error bars are wider than the differences the optimizer is choosing between, so the objective is nearly flat and the constraints decide (§12.4–12.6); and the constraint that binds is the exit door, whose width depends on what everyone else is doing (§12.7–12.9). The Finder table at the top of the Desk Debrief (§12.11) lists each tool the chapter builds, with the box that explains it, the scene that tests it and the listing that implements it.

*Before reading on: which of the eleven tabs would you cap, and what single number would you demand for each?*

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

On Monday afternoon Ines printed the table, put it next to Theo's eleven tabs and walked it with a pen, one row at a time, the way she would replay a hand. At the HY row she wrote 39 in the margin, and at the loan row 52, and at the direct-lending row 33, and she said where the numbers came from before anyone asked: a Federal Reserve note that had put the three side by side (Cai and Haque, FEDS Notes, February 23, 2024: post-default value of about 33% for direct loans, 52% for syndicated loans and 39% for HY bonds). Then she drew two arrows. One ran from the CLO row to the loan row, because a CLO tranche is a slice of a pool of term loans. The other ran from the BDC to the direct-lending row, because the fund owns the loans and the client owns the fund.

"Five of these are the same company wearing different lawyers," she said. The HY bond, the term loan, the CLO tranche that owns the term loan, the direct loan to the company one size smaller, and the BDC that owns the direct loan: "five, if you count the fund separately from the loans inside it, which you should, because it has its own lawyers and its own exit." Diversifying across them diversifies seats and documents, not borrowers. The sketch she left on Theo's desk is Figure 12.1.

At the bucket column Theo asked where the labels had come from, since nobody publishes a liquidity classification for a sector. "Desk judgment," Ines said, and wrote *illustrative* across the header. Each fund classifies its own holdings under the SEC's liquidity rule (§12.7), and a 2% position in a liquid HY issue is a different animal from 2% of a 144A orphan. She lingered longest at the CLO row, because it is the one where the same instrument sits in the most portfolios for the most different reasons.

> **View From Another Seat.** *The life insurer: the same CLO tranche, priced in capital rather than in spread.* Picture the same CLO BBB tranche on the investment committee agenda of a life insurer writing annuities (a generic seat; no firm is described). The committee's first question is not "how wide is it?" but "how much capital does it consume per unit of spread?", because the binding constraint is the NAIC's risk-based capital formula, not a benchmark. That formula moved in 2026. Per a Sidley client note (9 July 2026), the NAIC in June 2026 adopted new C-1 factors for CLOs effective for year-end 2026 reporting: the 45% charge on residual tranches stays, and below-investment-grade tranches of broadly syndicated CLOs that are 4% thick or thinner, measured on the latest trustee report, carry an added 11.77% pretax surcharge. The seat had been built on the arithmetic those factors target. Federal Reserve economists found that life insurers' CLO holdings reached "a record \$212 billion by the end of 2023," and that "insurers holding a portfolio of B-rated loans can cut their risk-based capital charges by two-thirds if they package those loans into a CLO and purchase the entire CLO capital stack" (Carlino, Foley-Fisher, Heinrich and Verani, FEDS Notes, 21 March 2025). So the insurer holds through a five-point price move without blinking and sells when a designation, a rating or a factor table changes the charge. For the MAC desk that is a different kind of counterparty: demand that is slow, sticky and rule-driven, with its discontinuities on regulatory calendar dates rather than on spread levels. The same tranche that Theo's table files under "less liquid" is, to this seat, liquid enough to hold forever and expensive enough to sell on a date the rulebook chooses.

"So the same bond has a price for each seat," Theo said.

"And the index yield has one number for all of them," said Ines, and circled two columns. The column that decides what the investor gets back in a bad year (recovery) and the column that decides whether they can get out to collect it (exit) are exactly the two that an index-level yield ignores.

![Figure 12.1: Five of the eleven tabs are claims on one population of sponsor-backed single-B borrowers, and the CLO and the BDC simply hold the term loan and the direct loan, so diversifying across them diversifies seats and lawyers, not borrowers. Source: post-default values from Cai and Haque, FEDS Notes, February 23, 2024; the ownership structure is Illustrative (the schematic of §12.1).](assets/figures/ch12_same_bet_ownership.png)

The sketch has an uncomfortable corollary for anyone who sells sector rotation for a fee.

> **Desk Myth vs. Desk Reality.** *Myth:* sector rotation is where multi-asset credit earns its fee. *Reality:* AQR regressed 445 Core/Core-Plus, 44 Global Aggregate and 114 Global Unconstrained bond managers on traditional risk premia (November 1997 to June 2018) and got R² of 90%, 61% and 77%, a credit-loading t-statistic of 14.9 for US Aggregate managers, and residual alphas of 0.10%, 0.01% and 0.09% a year, none significant (AQR, *Alternative Thinking* 4Q18, Exhibit 3; published as Brooks, Gould and Richardson, *Active Fixed Income Illusions*, Journal of Fixed Income, 2020). The fee was paid for credit beta with extra steps. "IDO or it didn't happen" applies to sectors too: a sector tilt is alpha only after you strip the DTS beta it carries (Chapter 8).

Two sentences in the research the desk reads say the same thing from the inside, one about the index's history and one about what a "spread asset" is.

> **[SOURCE EXTRACTION]** *Nuveen p.4:* "the U.S. high yield index has improved in quality over time. At year-end 2024, 51% of the index was rated BB, compared to 37% in 2004"
>
> **Annotation.** This sentence is the most important caveat in the paper, and it sits in the middle of a paragraph about z-scores. A z-score compares today's spread with a historical mean. If the index's rating mix moved from 37% BB to 51% BB, the historical mean belongs to a riskier portfolio, and a "two standard deviations tight" reading is partly a composition artifact. The modern desk responds in two ways: compute valuation on a fixed-mix, composition-adjusted spread (reweight the BB, B and CCC bucket spreads to constant weights), and model the buckets separately whenever their spreads diverge, which in 2026 they did by more than 1,000 bp (§12.9). Nuveen states the problem; the engine in §12.10 makes the fix mandatory.

> **[SOURCE EXTRACTION]** *Ben_Dor p.85:* "Historically, the pricing of this asset class has resembled that of corporate bonds in that it has been driven mainly by spreads rather than rates."
>
> **Annotation.** Ben Dor and coauthors are describing EM hard-currency debt, and the point generalizes to the whole MAC menu: once the Treasury component is hedged or stripped, EM sovereigns, CoCos, preferreds and CMBS mezzanine are all spread instruments whose risk scales with DTS. That is what licenses a common risk unit across sectors (§12.5). The departure: EM sovereigns carry a jump the corporate model lacks, because an index constituent can default for fiscal or political reasons unrelated to the global spread factor, and the index yield then includes a bond trading at 40 (§12.3).

Nuveen's 37-to-51 is one frame of a longer film about where the weakest borrowers went.

> **Trend Watch: The HY Index That Stopped Growing (2004–2026).** *What changed:* public high yield got smaller relative to the rest of leveraged finance, and better rated. Martin Fridson reported the HY index's face value at about \$1.4 trillion in April 2025, essentially unchanged over ten years, with the BB share at 53.55% against a 1996–2024 average of 44.53% (Fridson, CFA Institute *Enterprising Investor*, June 2025). Nuveen's own number: 51% BB at year-end 2024 against 37% in 2004 (Nuveen p.4). *Where the growth went:* institutional leveraged loans reached \$1,549bn at 2025Q4 (9.2% growth over the year), private credit about \$1.4tn, "about one-third of total below-investment-grade debt, excluding bank loans," against \$1,772bn of HY and unrated bonds (Federal Reserve, *Financial Stability Report*, May 2026, citing PitchBook LCD). *What it means for the desk:* the HY index's spread history is a history of a different index. A 2007 spread and a 2025 spread are not the same random variable, because the composition changed under them (§12.3). And the weakest borrowers did not disappear; they moved to the two sleeves that mark least often.

## 12.2 The Return Identity: Four Terms and Two Measures

Nuveen's capital market assumptions start from an identity, not an opinion.

> **[SOURCE EXTRACTION]** *Nuveen p.3:* "Forward return estimates = yield – estimated credit loss – ∆rates MTM – ∆spread MTM"
>
> **Annotation.** Every MAC shop has some version of this line; the value is in being explicit about it. Each term has a different owner and a different failure mode: the yield comes from the index (and includes whatever is defaulting inside it), the credit loss comes from a default forecast and a recovery assumption (the restructuring banker's variable), and the two mark-to-market terms come from rate and spread views. The modern desk keeps the identity and audits each term: it states the measure, uses the right duration for each term, and replaces the recovery-table lookup with a seat-in-the-waterfall estimate. The derivation below shows where each audit item comes from.

On Tuesday morning Theo came in at seven with the Nuveen paper printed, three pencils and no intention of opening a laptop until he had rebuilt Figure 3 by hand. It was a restructuring habit: before you believe a sources-and-uses table, you add it up yourself, because the person who built it had a reason to build it that way. The line had four terms, and two of them, "∆rates MTM" and "∆spread MTM," were the same bond's price moving for two different reasons. Kaz, who had come in early to rerun something, read over his shoulder for a while and then took the printout and drew a hill on the back of it.

> **Math, Gently.** *A bond's price is a hill, and duration is how steep it is where you stand.* Put yield on the horizontal axis and price on the vertical. The curve slopes down, because a higher yield discounts every future coupon more, and it bends upward like the side of a bowl. Duration is the slope where you stand, in percent of price per point of yield. With duration $D = 4$, a yield rise of one percentage point costs about $4 \times 1\% = 4.0\%$ of price. Convexity is the bend: the slope flattens as you walk down the hill, so the true loss is a little smaller than the straight-line guess. With convexity $C = 20$ the correction is $\tfrac12 \times 20 \times (0.01)^2 = 0.001$, a tenth of a percent given back, and the move costs about 3.9%. The second part is the one this chapter leans on: *one instrument can stand on two hills at once.* A leveraged loan pays SOFR plus a fixed spread, reset every quarter. If Treasury yields jump, the coupon catches up at the next reset, so the loan's rate duration is only the time to that reset, $D^{\text{mod}} \approx 0.25$. The spread, though, is locked until the loan refinances, perhaps four years out, so if spreads on similar loans widen, the price has to fall far enough to make the locked spread competitive: spread duration $D^{\text{spr}} \approx 4$. The same loan feels a 100 bp spread shock sixteen times as hard as a 100 bp rate shock ($4/0.25 = 16$). For a fixed-rate bond the two durations are nearly equal, which is why people forget there are two. The identity needs both, and the expansion that produces it comes next.

Theo wrote "yield 6.97" at the top of the page and "expected credit loss 2.55" under it, and Kaz put a finger on the second line. "Expected by whom?"

"By Nuveen. A default rate times a loss given default."

"Which default rate? There are two in this building. The one the CDS desk is charging for, and the one the rating agencies count."

Theo had made exactly this mistake in his first week, in the other direction, when he sold protection with a vendor default probability against a market hazard (Chapter 6), and he did not enjoy the reminder.

> **Math, Gently.** *The bookmaker's odds and the horse's chances.* A bookmaker's odds on a horse are not the horse's chance of winning; they are the chance, plus the bookmaker's margin, plus whatever the crowd is afraid of. Credit has the same two numbers. The default odds read from market prices live in what quants call the risk-neutral measure, $\mathbb{Q}$; the default rate you would forecast from history and fundamentals lives in the physical measure, $\mathbb{P}$. Take a CDS at 300 bp with loss given default $L = 0.6$. The credit triangle says the market is charging for a default intensity of $\lambda^{\mathbb{Q}} = 0.03/0.6 = 5\%$ a year. If the agency forecast for that rating is a 2% default rate, the difference, $(5\% - 2\%) \times 0.6 = 1.8\%$ a year, is what a buyer of the credit risk is paid for bearing it, the premium the whole allocation exercise is trying to harvest. Now put the 5% into the loss term of Nuveen's identity. The loss you subtract equals the compensation the yield contains, and the premium comes out zero by construction, however generously the market is paying. Chapter 6 owns the full story; this chapter only needs the sign.

Put together, the hill and the two measures give the identity its precise form. Equation (12.1) says that a sector's expected return, per year, is its yield, minus the expected loss from defaults (a *physical* default intensity times the loss given default for that seat in the waterfall), minus rate duration times the expected rise in Treasury yields, minus spread duration times the expected widening, plus a convexity term that almost nobody bothers with. The yield is a market price and so carries $\mathbb{Q}$-compensation; subtracting a $\mathbb{P}$ loss leaves the credit risk premium, the liquidity premium and the term premium, and nothing else. The derivation, the excess-return decomposition and the horizon arithmetic for the mark-to-market terms follow.

#### The Full Derivation

Take a sector proxy with price $P(y)$ and yield-to-worst $y = y^{\text{TSY}} + s$, held for a period $\Delta t$ (years). If it does not default, a second-order expansion of the price gives the holding-period return

$$
r^{\text{no default}} \approx y\,\Delta t \;-\; D^{\text{mod}}\,\Delta y^{\text{TSY}} \;-\; D^{\text{spr}}\,\Delta s \;+\; \tfrac12\,C\,(\Delta y)^2 ,
$$

where $y\,\Delta t$ is the accrual at an unchanged yield (coupon plus pull to par), $D^{\text{mod}}$ is the rate duration, $D^{\text{spr}}$ the spread duration and $C$ the convexity. Two durations appear because they differ, as the loan on Kaz's two hills showed: $D^{\text{mod}} \approx 0.25$ against $D^{\text{spr}} \approx 4$.

Now add default. With physical default intensity $\lambda^{\mathbb{P}}$, the bond defaults within $\Delta t$ with probability $\text{PD}^{\mathbb{P}} \approx \lambda^{\mathbb{P}}\Delta t$, and on default the holder loses the fraction $L = 1 - R$ of the bond's value (recovery of market value; under recovery of face, replace the loss with $(1 - R/P)$ per unit of price). Taking the physical expectation and dividing by $\Delta t$:

$$
\mathbb{E}^{\mathbb{P}}[r] \;\approx\; y \;-\; \underbrace{\lambda^{\mathbb{P}}\,(1-R)}_{\text{expected credit loss}} \;-\; D^{\text{mod}}\,\frac{\mathbb{E}^{\mathbb{P}}[\Delta y^{\text{TSY}}]}{\Delta t} \;-\; D^{\text{spr}}\,\frac{\mathbb{E}^{\mathbb{P}}[\Delta s]}{\Delta t} \;+\; \tfrac12\,C\,\frac{\mathbb{E}^{\mathbb{P}}[(\Delta y)^2]}{\Delta t}. \tag{12.1}
$$

Nuveen's Figure 2 is (12.1) with the convexity term dropped. Here is what each term is made of.

*The yield* is a market price, so it embeds $\mathbb{Q}$-compensation. By the credit triangle, $s \approx \lambda^{\mathbb{Q}}L + \ell$, where $\ell$ is a liquidity spread. Subtract the cash rate $r$ from (12.1), ignore the mark-to-market terms, and the forward *excess* return is

$$
\mathbb{E}^{\mathbb{P}}[r] - r \;\approx\; \underbrace{(\lambda^{\mathbb{Q}} - \lambda^{\mathbb{P}})\,L}_{\text{credit risk premium}} \;+\; \underbrace{\ell}_{\text{liquidity premium}} \;+\; \text{term premium}.
$$

So the identity is a risk-premium forecast wearing an accounting costume, and that is where its first error hides. If someone fills the loss term with a CDS-implied default probability, a $\mathbb{Q}$ object, the credit risk premium cancels by construction, and the forecast says the sector earns cash plus its liquidity premium. The loss term has to be physical: an agency default forecast, a structural model (Chapter 5) or the desk's own hazard model, multiplied by a *physical* recovery for that seat in the waterfall.

*The loss term* is where the RSSG reader has an edge. A rating-table recovery of 40% applied to everything ignores the FEDS numbers in §12.1: a direct loan that recovers 33% instead of 52% has a 40% larger loss given default ($0.67/0.48 \approx 1.40$) for the same default rate. For CLO tranches the loss is a waterfall output (it depends on the CCC bucket, the OC cushions and the reinvestment period; see Chapter 21), not a table lookup. For an index containing a sovereign in default, the "yield" partly prices that one bond's recovery, and the loss term must too.

*The mark-to-market terms* need horizon care. Nuveen's example is a five-year forecast. If the expected yield change $\Delta$ arrives gradually, linearly over horizon $h$, the yield path is $y_t = y_0 + (\Delta/h)\,t$ and the cumulative return with constant duration is $\int_0^h y_t\,dt - D\,\Delta = y_0 h + \Delta h/2 - D\Delta$. Annualized,

$$
\bar r \;\approx\; y_0 \;-\; \Big(\frac{D}{h} - \frac12\Big)\Delta .
$$

So reinvestment at the higher yield offsets half the move per year, and at $D \approx h/2$ a gradual rate rise costs nothing over the horizon. Subtracting $D\Delta/h$ without the $+\Delta/2$ overstates the drag; subtracting $D\Delta$ in a single year double-counts it. For floating-rate sectors the rates term is nearly zero but the yield term moves: the loan's coupon follows the forward SOFR path, so its "yield" in (12.1) is properly the forward-rate-implied coupon, not today's.

#### Theo's Tuesday rebuild

By a quarter to eight Theo had the five numbers in a column. Nuveen's Figure 3 (Nuveen p.3; Bloomberg US Corporate High Yield Index, as of November 19, 2025) prints five numbers, 6.97, 2.55, 0.37, 0.49 and 3.56, and they satisfy $6.97 - 2.55 - 0.37 - 0.49 = 3.56$. The arithmetic tied on the first pass. The labels did not. The text layer of the PDF lists the labels in the reverse of the value order, so the assignment of 2.55 and 0.49 between "expected credit loss" and "∆spread MTM" cannot be read off the extraction, and Theo, who had once spent a weekend reconciling a lender presentation whose footnotes had been renumbered by a paralegal, recognized the genre.

Economics decides it. An expected loss of 2.55% a year at 40% recovery implies a physical default rate of about 4.25% a year, which is in the range of long-run speculative-grade experience (approx.). An expected loss of 0.49% implies about 0.8%, implausible for an index that is about half single-B and below. Meanwhile 2.55% a year of spread mark-to-market over five years, at a spread duration near 3.2, would require roughly 400 bp of widening. The consistent reading is: yield 6.97%, expected credit loss 2.55%, rates MTM 0.37%, spread MTM 0.49%, forward return 3.56%. Theo wrote the reason under the reading in the margin, the way he used to annotate a model before a partner saw it: *a chart is data and a guess is not.* And the 2.55 passed Kaz's test, because 4.25% is a horse's chance, not a bookmaker's.

Kaz did the next part, because it involved dividing. Nuveen's Figure 6 reports forward returns, volatilities and forward Sharpe ratios for six efficient portfolios. If the ratio is (return − cash)/volatility, each row implies a cash rate: $5.11 - 0.26 \times 5.50 = 3.68$, $6.20 - 0.40 \times 6.29 = 3.68$, and the other four land between 3.65% and 3.70%. That is our inference, not Nuveen's statement (the paper's endnote defines the ratio, and a careful reader checks it before quoting this). If it holds, high yield's five-year forward return of 3.56% sits *below* cash.

"Then why does the optimizer hold any?" Kaz asked.

Theo turned to Figure 5. The 20% minimum on HY in Nuveen's constraint table (Nuveen p.6) is then not something the optimizer wants; it is something the client wants, and the optimizer pays for it with every other weight. That is fine. It is also exactly the sort of thing a spec should make visible, and §12.10 prints the shadow price. Figure 12.2 draws the identity beside that implied cash rate.

![Figure 12.2: Nuveen's identity for the high-yield index: a 6.97% yield becomes a 3.56% five-year forward return after credit loss and mark-to-market drags, just under the 3.68% cash rate implied by Nuveen's Figure 6. Source: Nuveen (Zheng), Multi-asset credit investing, Figures 3 and 6, data as of November 19, 2025; the assignment of 2.55 and 0.49 to the loss and spread terms and the cash rate are the inferences of §12.2.](assets/figures/ch12_return_identity_waterfall.png)

Kaz looked at the hill again before giving the printout back. "Your expansion assumes the bond keeps its shape while the yield moves. It works for a plain bullet bond in a normal week. Three things on the PM's list can change shape when you push them, and one of them has already changed shape before you start." Kaz wrote them on a sticky note, and the sticky note became the box below.

> **Ways This Blows Up.** *Callable bonds and preferreds:* yield-to-worst already assumes the issuer calls when it is optimal to do so, and a spread MTM computed with yield-to-maturity duration overstates the price sensitivity of a bond that is about to be called. Use option-adjusted spread duration. *Perpetuals and CoCos:* the yield is a yield-to-call, and the extension risk is the trade; a CoCo whose call is skipped becomes a much longer instrument overnight. *Defaulted constituents:* an index yield averaged over bonds at 40 is a recovery forecast you didn't make (§12.3).

## 12.3 Spread per Unit of What? Cross-Sector Valuation

Theo's first instinct was right: yield is the wrong ranking variable. But "spread" is not the right one either, because a spread is compensation for three different things.

> **[SOURCE EXTRACTION]** *Ben_Dor p.168:* "We model a bond's OAS (to Treasuries) with three variables: a variable reflecting expected default cost, a variable reflecting expected liquidity cost, and a market-wide variable unrelated to the bond's attributes representing the market-wide risk premium demanded by investors."
>
> **Annotation.** This is the decomposition a MAC valuation should run sector by sector: $s = \text{EL} + \ell + \pi$, with expected default cost (the loss term of §12.2), expected liquidity cost (the LCS of Ben Dor chapter 5, a round-trip transaction cost amortized over the holding period) and the market-wide risk premium $\pi$. Only $\pi$ is the reward for bearing systematic spread risk. The modern desk departs in two places: it estimates EL at the seat level, not from a sector average, and it lets the liquidity term switch on in stress, because Ben Dor finds (p.177) that "liquidity cost provides additional explanatory power for the cross-sectional variation in high-yield spreads only during periods of market stress."

The decomposition suggests three ratios, each answering a different question, and the desk found all three on Thursday 15 October without meaning to, because three people looked at the same spreadsheet and each asked the question their old job had trained into them.

#### Three people, three ratios

Kaz had sorted the eleven tabs by spread, widest first, and the evening marks put a new name at the top. The CCC & lower OAS closed at 12.78% (ICE BofA via FRED, series BAMLH0A3HYC), its widest since 2023. "Twelve seventy-eight," Kaz said. "If we are ranking by compensation, that is the most compensation on the sheet."

"Compensation for what?" Mags asked. "What does it recover?"

"The sheet doesn't say."

"Call it thirty-five," she said, *illustrative*, a number she would have argued about for a week on a real name and conceded in a second for a bucket. She did the division without looking for a calculator. The *break-even default rate* is the annual default rate at which the spread exactly pays for losses:

$$
\lambda^{\text{BE}} \;=\; \frac{s}{1 - R}.
$$

It is the credit triangle solved for the intensity, and it is the number Mags computes in her head: $\lambda^{\text{BE}} = 0.1278/0.65 \approx 19.7\%$ a year. "So the question isn't whether twelve seventy-eight is wide," she said. "The question is whether a fifth of them will default every year. If you think fewer, you're paid. If you think more, you're the one paying, at a very attractive yield." The excess spread $s - \text{EL}$ and the coverage ratio $s/\text{EL}$ are the same idea in other units.

Ines was not interested in the CCC bucket on its own. She wanted to know what each tab paid per unit of risk, and she had a ruler for risk that worked across sectors. In DTS units (Chapter 8; Ben Dor p.50), a sector's excess-return volatility is $\sigma(r^x) \approx \text{DTS}\cdot\sigma(\Delta s/s)$, where $\text{DTS} = D^{\text{spr}}s$ and $\sigma(\Delta s/s)$ is the volatility of *relative* spread changes. Its annual excess carry is roughly $s - \text{EL}$. Divide:

$$
\frac{s - \text{EL}}{D^{\text{spr}}\,s\,\sigma(\Delta s/s)} \;=\; \frac{1 - \text{EL}/s}{D^{\text{spr}}\,\sigma(\Delta s/s)}.
$$

She circled the spread in the numerator and the spread in the denominator and crossed both out. The spread level cancels. If relative spread volatility is roughly common across sectors (the empirical content of DTS), then carry per unit of risk is set by spread duration and by the share of the spread that is eaten by expected loss, not by how wide the spread is. Short-dated, high-recovery paper wins on this ratio, which is the same conclusion the short-maturity HY literature reaches by a longer road. "A wider spread is not a better deal," Ines said. "It's a bigger bet of the same quality. Same odds, more chips."

> **[SOURCE EXTRACTION]** *Ben_Dor p.50:* "a portfolio with a weighted spread of 200 bps and spread duration of two years is equally risky as a portfolio with a spread of 100 bps and spread duration of four years."
>
> **Annotation.** Both portfolios have DTS of $4 \times 0.01 = 2 \times 0.02 = 0.04$ years, so their excess-return volatility is the same if relative spread changes have the same volatility. For MAC this is the license to put a floating-rate loan (short rate duration, four-year spread duration), a CLO BBB tranche and an EM sovereign on one risk axis. The modern caveat: DTS was estimated on corporate bonds. For tranches, relative spread changes are not proportional across the capital structure in stress (mezzanine tranche spreads gap), and for direct lending the "spread change" is never observed at all, so the risk unit must be imported from a proxy (§12.5).

Theo's question was the one a banker learns to ask about fees, which is what is left after everyone has been paid. He had found it on the CMBS BBB tab, where the dealer runs showed a bid and an offer two points apart. A sector with round-trip liquidity cost $\text{LCS}$ (decimal of price; Ben Dor p.111 defines liquidity as "the cost of a roundtrip institutional-size transaction in a bond") held for $T_{\text{hold}}$ years pays $s - \text{EL} - \text{LCS}/T_{\text{hold}}$ per year. A 2-point round trip on CMBS BBB held for two years costs 100 bp a year, which can be more than its excess spread over EL. "So if the PM rotates this sleeve every quarter," Theo said, "the round trip is charged four times a year and the spread is paid once." For a desk that rotates sectors quarterly, this is the ratio the P&L sees, and the other two are opinions about what it might have seen.

The same three questions, asked of one risk wrapped two ways, are a pod's trade.

> **The Pair.** *Pair Book entry PB-13, Dov Adler's pod at Vantress Capital Management (fictional composite; a replay written as of late February 2020, before the stress; sizes illustrative).* **Thesis.** An investment-grade bond ETF and the bonds it holds are one risk with two prices. In a calm month the ETF trades within a few cents of its net asset value; in a disorderly one it can trade at a discount, because the ETF is the only part of the market still printing while the NAV is computed from evaluated bond prices that lag. A discount is a chance to buy the wrapper cheaply against the risk inside it, so Dov wrote the pair into the ledger with a trigger rather than a fill: long LQD if it trades at a discount to NAV wider than its usual range, hedged with CDX IG protection. **Legs.** Long \$50mm of LQD; buy protection on the on-the-run 5-year CDX IG, sized so the two legs' spread DV01s match, with Treasury futures taking out the rate DV01 the index leaves behind. Because LQD's bonds are longer than five years, matching spread DV01 means roughly \$90mm of index notional against \$50mm of ETF. **What the hedge removes.** The investment-grade spread factor, which both legs carry, and the Treasury curve. Wen Zhao's note on the entry adds that no bond is borrowed, which is the reason the short leg is an index: shorting a basket of a few thousand cash bonds is a recall waiting to happen (Chapter 8 has the short-leg menu). **What idio remains.** The wrapper: the gap between LQD's price and the NAV of its holdings, which is the pair's whole thesis and the reason it has no business being on in February. **What leaks.** The NAV itself. It is an evaluated price, an opinion produced by a pricing service from quotes that may be stale, so a "discount" can be the ETF telling the truth early rather than being cheap; if the NAV later falls to meet the price, the convergence arrives as a loss on the bonds that the CDX leg offsets only partly, because the cash–CDS basis tends to widen in the same week (Chapter 24). Then the maturity mismatch: an index of 125 five-year names does not move one for one with a basket of longer, more BBB-heavy bonds. Dov's rule for the explain is that the ETF's premium or discount gets its own line, never folded into "spread." **What it costs to carry and to short.** The long earns LQD's distribution yield less its fee and its funding; the short pays the index's running premium on \$90mm, a few basis points a week; the futures cost their roll. In a calm month the pair carries close to nothing and earns close to nothing, which is the honest price of holding an option on someone else's forced sale. The fill, the stress and the close are Chapter 20's, in the week of 12–23 March 2020.

**Mean reversion and the z-score.** Nuveen is careful here:

> **[SOURCE EXTRACTION]** *Nuveen p.4:* "A commonly used metric for assessing credit relative value is the z-score, which indicates the number of standard deviations from the historical average. However, relying solely on this measure is insufficient"
>
> **Annotation.** The derivation below shows why the z-score is necessary but not sufficient: it is a sufficient statistic only if the long-run mean is constant, and the HY index's long-run mean moved when the index's rating mix moved (§12.1). Nuveen supplements z-scores with spread transition probabilities and fundamentals; the modern desk adds the composition adjustment and a regime model (§12.4), because the speed of mean reversion is itself regime-dependent.

"Two standard deviations from what, though?" Theo asked, and Kaz went back to the whiteboard.

> **Math, Gently.** *The drunk, and the drunk on a leash.* A random walk is a path built from independent steps: tomorrow's level is today's plus a fresh coin flip, scaled. It has no memory of where it started and no home it is pulled toward, so after a year it can be anywhere within about one year's worth of volatility of where it began, and after four years within twice that. Picture a drunk leaving a bar. Now tie the drunk to a lamppost with an elastic leash. He still staggers at random, but the farther he wanders, the harder the leash pulls him back. That is the Ornstein–Uhlenbeck process, the standard model for a spread that mean-reverts: the pull is proportional to the distance from home, at a speed $\kappa$ per year, and $\kappa = 0$ is the drunk with no leash at all. Speed converts into a half-life, the time to close half of any gap: with $\kappa = 0.35$, the half-life is $\ln 2 / 0.35 \approx 1.98$, about two years. Now suppose a sector sits two standard deviations wide of its long-run mean, $z = +2$, and those standard deviations are $\sigma_s = 150$ bp, so the gap is 300 bp. Over one year the leash closes the fraction $1 - e^{-0.35} \approx 0.30$ of it, so the expected tightening is about $300 \times 0.30 \approx 89$ bp, not 300. The z-score told you where the drunk is; it did not tell you how strong the leash is. One technical note for readers who have met Itô's lemma: no $\tfrac12\sigma^2$ correction appears here, because the OU process is linear in the spread; that tax belongs to lognormal prices and spreads (§5.2.3). The formulas are next.

In one line: the expected change in the spread over a horizon $h$ is the z-score times the stationary volatility times the fraction of the gap the leash closes in $h$, with the sign that pulls the spread home, and that is exactly the number the spread term of (12.1) asks for.

#### The Full Derivation

Model the spread as Ornstein–Uhlenbeck under $\mathbb{P}$: $ds_t = \kappa(\theta - s_t)\,dt + \sigma\,dW_t$, with speed $\kappa$ (per year), long-run mean $\theta$ and volatility $\sigma$. Then

$$
\mathbb{E}^{\mathbb{P}}[s_h \mid s_0] = \theta + (s_0 - \theta)\,e^{-\kappa h}, \qquad \operatorname{Var}(s_\infty) = \frac{\sigma^2}{2\kappa}, \qquad t_{1/2} = \frac{\ln 2}{\kappa}.
$$

Define the stationary z-score $z = (s_0 - \theta)/\sigma_s$ with $\sigma_s = \sigma/\sqrt{2\kappa}$. The expected spread change over the horizon, which is exactly the input to the spread MTM term of (12.1), is

$$
\mathbb{E}^{\mathbb{P}}[\Delta s] \;=\; -\,z\,\sigma_s\,\big(1 - e^{-\kappa h}\big).
$$

So a z-score becomes a return forecast only after you multiply by three things it does not contain: the stationary volatility, the reversion speed and the horizon. A $z = -2$ in a sector with a four-year half-life barely moves a one-year forecast. And all of it is conditional on $\theta$ being the right mean. Nuveen's "credit spread transition probability" is the discrete version: bucket spreads into states, estimate $P_{ij} = \Pr(s_{t+1} \in j \mid s_t \in i)$, and read the $h$-step distribution from $P^h$. It inherits the same assumption.

#### The ruler whose zero moved

"Conditional on theta being the right mean" was the clause Mags had been waiting for. She asked Kaz to hold the bucket spreads still and move only the weights, which is the oldest trick in her book for catching an index lying about itself.

**The composition adjustment.** Hold the bucket spreads fixed at their 2025 year-end levels (ICE BofA via FRED: BB 169 bp, B 301 bp, CCC 885 bp) and change only the weights. A 2004-style mix of 37% BB, 45% B and 18% CCC gives $0.37(169) + 0.45(301) + 0.18(885) \approx 357$ bp. A 2025-style mix of 53% BB, 36% B and 11% CCC gives about 295 bp. The actual index printed 281 bp. The B and CCC weights here are *illustrative* (only the BB shares are sourced), but the lesson is not: about 60 bp of "tightness" against long history is composition, not valuation. Fridson made the complementary point about tails: applying March 2020's category spreads to the April 2025 ratings mix still produces about +1,093 bp, against the actual +1,087 bp peak of March 23, 2020 (Fridson, CFA Institute *Enterprising Investor*, 2025). A better-rated index has a lower mean; it does not have a thinner tail.

"So when somebody tells me high yield is two standard deviations tight," Mags said, "I ask them which high yield. A z-score is a ruler. This one's zero moved, because the index stopped holding the same companies. Put the ruler on a fixed-mix spread, BB against BB, and it measures something. Put it on an index that just added a defaulted sovereign, or dropped one, and it measures the index committee." Theo wrote the second half of that down, because it was the half he would have missed: the EM sovereign tab was exactly that kind of index.

Ines put it in her terms. "Comparing today's HY spread to 2007's is comparing a poker room to the same room after they banned half the drunks. The pots are smaller. The bad beats are not."

> **Ways This Blows Up.** ROBO is told to "maximize yield subject to 6% volatility." It buys the EM sovereign index at a 9% yield, which is 9% because one country in the index is in default and its bonds trade at 40. Nuveen warns about exactly this (Nuveen p.7): "A compelling yield on the emerging markets sovereign debt index could be a result of distressed bonds from a single country experiencing a significant fiscal or currency crisis." The precise spec computes sector yields ex-distressed (constituents below a price of 50 removed and modeled separately with their own recovery), caps single-issuer DTS share, and reports the yield contribution of the top five issuers.

### Deep-Dive Resource Graph (§12.1–12.3)

**Podcasts**

- **BlackRock Says CLOs Are Among Best Relative Value Picks in Credit** (*The Credit Edge*, Bloomberg Intelligence, guest James Turner, BlackRock, 25 Sep 2025). A cross-sector relative-value claim ("a very good spread and deal pickup") that the spread-per-unit-of-DTS comparison in §12.3 should be able to confirm or refute. https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/blackrock-says-clos-are-among-best-relative-value-picks-in-credit
- **Fridson Sees High Yield Going Distressed in Recession** (*The Credit Edge*, Bloomberg Intelligence, guest Martin Fridson, Fridson Vision High Yield Strategy, 1 May 2025). A dated, falsifiable tail call ("high confidence" that the index returns to 1,000bp at the worst point of the next recession) from the author of the 1,000 bp article listed below; the spoken companion to the composition and tail argument in §12.3. https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/fridson-sees-high-yield-going-distressed-in-recession

**Practitioner Writing**

- Nuveen (Mark Zheng), *Multi-asset credit investing: A quantitative framework*, Q4 2025 (on the shelf; data as of November 19, 2025).
- **Multi-asset credit investing: A quantitative framework** (Nuveen, Mark Zheng, portfolio manager, 19 Dec 2025). The public web form of the framework this chapter works from: more than 20 sectors from high yield to private credit, capital-market assumptions, risk modelling and optimization. Read it beside §12.2 and §12.6 to see what a house publishes versus what the chapter derives. https://www.nuveen.com/global/insights/fixed-income/multi-asset-credit-investing
- **Ruminating on Asset Allocation** (Howard Marks, Oaktree memo, 22 Oct 2024). Asset allocation from a risk target, the balance of ownership and debt, and the role of debt in today's portfolios: the qualitative statement of what the capital-structure map in §12.1 allocates across. https://www.oaktreecapital.com/insights/memo/ruminating-on-asset-allocation
- **High-Yield Bonds: Not Your Parents' Market** (Brookfield, Sheldon Stone and David Rosenberg, co-PMs of US high-yield bonds, Feb 2026). Reads "tight" spreads (around 300bp) against a market that is now over 55% BB, with CCC-and-below at 12.1% versus a 17.2% long-term average: the composition effect behind the adjustment in §12.3. https://privatewealth.brookfield.com/sites/default/files/2026-02/high-yield-bonds-not-your-parents-market.PDF
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

A regime model is built from two ideas older than any desk: a coin that decides, each month, whether the weather changes, and a bell curve that only holds inside one kind of weather. Kaz's model on Wednesday got the second idea right and the first one wrong, and the difference is easiest to see before the model has a name.

> **Math, Gently.** *Part (a): the weather coin.* Suppose that at the end of every month a coin is tossed, and the weather changes only if it lands tails. If the coin lands heads with probability $P_{kk}$, the chance that the current weather lasts exactly $n$ months is the chance of $n-1$ heads followed by one tail. That is the **geometric distribution**, and its average is $1/(1 - P_{kk})$. A coin with $P_{kk} = 0.97$ keeps the weather for 33 months on average; a coin with $P_{kk} = 0.5$ keeps it for two. The coin has no memory: a calm spell that has already lasted three years is exactly as likely to end next month as one that began last month. The geometric is the monthly, counted cousin of the exponential waiting time for defaults (§1.5 and §6.1.4): the same memoryless clock, ticking in whole months instead of continuously. *Part (b): weather inside the weather.* Within one regime, monthly returns are modeled as a bell curve, the normal distribution, which is symmetric and has thin tails: moves beyond three standard deviations are rare enough to ignore. Kaz says "Let's just assume Gaussian" in every chapter of this book and regrets it in most of them; here, for once, the assumption is defensible, because it is made *inside* a state, not across all of history. The trick is what happens when you mix two bell curves. Take a calm regime 95% of the time with mean $+0.5\%$ and volatility $1.5\%$ a month, and a stress regime 5% of the time with mean $-4\%$ and volatility $5\%$. The mixture's overall volatility is about $2.1\%$ (its variance is 4.35). A single bell curve with that volatility puts the chance of a month worse than $-6\%$ at about 0.13%, once in sixty-four years. The mixture puts it at about 1.7%, once in five years: thirteen times as often. Two thin-tailed curves, mixed, make a fat tail. And of the total variance of 4.35, about 0.96 comes from nothing but not knowing which regime you are in, the gap between the two means weighted by how often each occurs. Keep that piece in mind; it is the second term of (12.2), and the derivation below puts it in matrix form.

Kaz fit the regime model on Tuesday and presented it on Wednesday. "Two states. The calm state is ninety-seven percent persistent. The stress state lasts, on average, one month."

"So your model thinks a bad month is a typo," Ines said.

She was right, and the reason is a one-line derivation. In a Markov chain, the probability of staying in state $k$ for exactly $n$ periods is $P_{kk}^{\,n-1}(1 - P_{kk})$, a geometric distribution, so the expected duration of a visit is

$$
\mathbb{E}[\text{duration}_k] \;=\; \sum_{n \ge 1} n\,P_{kk}^{\,n-1}(1-P_{kk}) \;=\; \frac{1}{1 - P_{kk}} .
$$

Kaz's calm state is the box's 33-month coin; a stress state with $P_{kk} = 0$ lasts one month, which means the model has learned that stress is an outlier, not a state. April 2025 says otherwise: the HY OAS went from 259 bp on January 22 to 461 bp on April 7, the VIX closed at 52.33 on April 8, and the drawdown in the HY total-return index ran from February 28 to April 7 (ICE BofA and CBOE via FRED). That is a regime with a beginning, a middle and an end, spread over two months. A model that calls it a typo will be fully invested in the beginning and fully hedged in the end.

> **[SOURCE EXTRACTION]** *Bolder p.524:* "In the finance and macroeconomic setting, they are used to describe business-cycle and high and low volatility state mechanics."
>
> **Annotation.** Bolder is introducing Markov chains for credit-risk work, where the usual object is a rating-transition matrix observed directly. In MAC allocation the chain is *hidden*: nobody publishes the regime, so it must be inferred from returns. Every formula below is the rating-migration machinery with one extra layer, a likelihood that turns observed returns into probabilities over unobserved states. The modern departure is about use, not math: the regime probability is an input to capital market assumptions and to a tilt budget (§12.8), not a switch that moves the whole book.

Ines's objection was to one parameter, not to the machine, and Theo wanted to know what the machine actually did each night when a new month of returns arrived. "It guesses the weather from the people walking in with umbrellas," Kaz said, "and it does it the way Bayes does in Chapter 1."

> **Math, Gently.** *The filter is Bayes, every evening.* Odds are the cleanest way to see it, as in §1.3.3 and Chapter 5. Suppose that, going into this month, the model gives stress odds of 1 to 9: a 10% chance of stress. Then the month's returns arrive, and they look like stress: the HY bucket down three points, CCCs down more, loans and CLO mezzanine following. The filter asks how likely those returns would be under each regime's bell curve, and suppose the answer is eight times likelier under stress than under calm. That ratio, the **likelihood ratio**, multiplies the odds: $1{:}9 \times 8 = 8{:}9$, which is a stress probability of $8/17 \approx 47\%$. That is the **update** step. The **predict** step happens overnight, before next month's returns arrive: the transition matrix blurs tonight's belief through the weather coin. With the coins of the previous box, a stress state that persists half the time ($P_{\text{ss}} = 0.5$) and a calm state that breaks 3% of the time, next month starts at $0.47 \times 0.5 + 0.53 \times 0.03 \approx 25\%$. Half the alarm has evaporated overnight, not because anything calmed down but because the model believes stress does not last. Make $P_{\text{ss}}$ smaller, as Kaz's fit did, and the alarm evaporates almost completely; that is Ines's typo, in arithmetic. The filter, the smoother that reruns it backward, and the estimation loop that learns the coins and the bell curves follow.

In words, then: the filter turns each month's returns into a probability over the two hidden regimes by multiplying yesterday's odds by today's evidence and then letting the weather coin pull them back toward the long-run mix; the estimation step learns the coins and each regime's mean and covariance from those probabilities; and the predictive moments for allocation, equation (12.2), average the two regimes' means and covariances by the probability of being in each over the horizon, plus one extra term for not knowing which regime it will be. That extra term is Part (b)'s 0.96, and it is the reason correlations rise together in a stress.

#### The Full Derivation: Filter, Smoother, EM

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

Each iteration raises the likelihood. It converges to a local maximum, so it needs a sensible start (the code labels the worst 20% of months by cross-sectional average return as stress) and a label alignment at the end (state 1 is the one with the higher mean excess return), because EM is indifferent to which state it calls "1."

**From regimes to capital market assumptions.** Given today's filtered probabilities $\xi_{t\mid t}$, the regime distribution $j$ months ahead is $(P^{\top})^j \xi_{t\mid t}$; average over the horizon to get $\bar\pi^{(h)} = \tfrac1h \sum_{j=1}^{h} (P^{\top})^j \xi_{t\mid t}$. The predictive mean and covariance of next-period returns follow from the laws of total expectation and total variance:

$$
\mu^{(h)} = \sum_k \bar\pi^{(h)}_k\,\mu_k, \qquad
\Sigma^{(h)} = \sum_k \bar\pi^{(h)}_k\,\Sigma_k \;+\; \sum_k \bar\pi^{(h)}_k\,(\mu_k - \mu^{(h)})(\mu_k - \mu^{(h)})^{\top}. \tag{12.2}
$$

The second term matters. When the two regimes have very different means, uncertainty about *which* regime you are in is itself a source of covariance, and it loads on every sector in the same direction: it is the correlation-goes-to-one effect, derived instead of asserted. As $h \to \infty$, $\bar\pi^{(h)}$ converges to the stationary distribution $\pi^{\star}$ solving $\pi^{\star\top} = \pi^{\star\top}P$, and (12.2) collapses to the unconditional moments, which is the strategic allocation's view. The tactical overlay is the difference between the two. (One caveat for long horizons: regime persistence makes monthly returns serially correlated, so the variance of an $h$-month cumulative return exceeds $h\,\Sigma^{(h)}$. Equation (12.2) is the per-period predictive distribution, which is what a one-year tilt needs.)

The second term has teeth only if the two regimes' means really are far apart, and the corporate index says they are.

> **[SOURCE EXTRACTION]** *Dynkin p.617:* "While the corporate index has average returns of –8.07%/yr in drawdown episodes and 4.12%/yr in recovery times, the EMC strategy performed well in both regimes: 11.53%/yr in credit drawdowns and 4.30%/yr in recoveries."
>
> **Annotation.** Dynkin and coauthors are reporting the regime-conditional performance of an equity-momentum-in-credit strategy (EMC), and the first half of the sentence is the input this section needs: the corporate index's mean return differs by about 12 percentage points a year across drawdown and recovery regimes. That gap is what makes $\mu_1 \ne \mu_2$ estimable and what gives the mixture term in (12.2) its bite. The second half is a preview of §12.8: a signal that works in both regimes is worth more to a MAC book than one that works only in calm, because the regime filter will always be a month late.

#### Quant-shop life (fictional composite): the month-end refresh

*Hana, the platform's junior quant (Chapter 5), the multi-sector credit team, its tickets, its overlay and every number in this vignette are invented; the routine is a composite of how systematic asset managers describe a capital-market-assumption refresh.*

Regime models rarely fail in a dramatic way. They fail in the refresh, which on the platform's multi-sector credit team is a job that runs on the Tuesday after the first BDC filing of each quarter, and which Hana inherited from someone who had left a README and a warning: *it always runs; that is the problem.*

The August refresh started at 6:40 a.m. and finished at 6:52, which was the first bad sign, because it usually took twenty-five minutes. The log said 312 months of returns for eleven sectors, a re-fitted two-state model, a new covariance matrix and a tactical overlay of +1.5% of NAV into loans and CLO mezzanine *(illustrative)*. Hana opened the inputs before she opened the outputs, which is a habit nobody teaches and everybody eventually learns.

The BDC column had changed in two places. The second-quarter NAV had finally arrived, about six weeks after the quarter ended, as it always does, and the first-quarter NAV, which the model had used in May, had been restated in the same filing. So the series the model had been fitted on in May no longer existed. The platform keeps a point-in-time archive for exactly this reason, every vintage of every series stored with the date it arrived, and Hana spent forty minutes diffing the May vintage against the August one to write down what the model had known and when. Then she noticed what the BDC column did to the regime fit. A series that never moves looks to a Gaussian likelihood like a sector that is always calm, so the calm state had quietly absorbed the private sleeve and was telling the overlay that private credit had no regime at all. The fix was already in the design notes and had never been switched on in production: leave the appraisal-smoothed series out of the regime model, and let the sleeve inherit the regime through its factor loading after desmoothing (§12.5).

At 8:15 the covariance step raised an assertion: minimum eigenvalue $-1.0 \times 10^{-7}$. Overnight the vendor had backfilled the credit-risk-transfer series three years further into the past, without a notice, and the weighted matrix, assembled from pairs of series with different start dates, was no longer a covariance matrix of anything. It implied a portfolio with negative variance, which is the optimizer's favorite kind. The assertion stopped the run, which is what it was for (§12.5 explains the repair). Hana opened ticket DATA-3107, "CRT backfill without notice," and linked it to DATA-2840, the February ticket asking the vendor for backfill notices, which was 187 days old and assigned to someone who had since joined a different team.

The worst thing she found had been wrong since June. The overlay's sign. The June re-fit had swapped the labels, so the state the code called "stress" now had the *higher* mean excess return, and the production refresh, unlike the research notebook, had no alignment step after EM. For two months the overlay had leaned the wrong way. It was small enough that the attribution showed it as a few basis points of "tactical" in each monthly report, and nobody reads the line in a report that is a few basis points. Hana added the alignment, reran June and July, and wrote the sentence that went into the change log: *a regime label is a name EM chose this morning.*

At 4:55 the PM emailed. The investment committee met Thursday; could the deck show the regime overlay's backtest, and could the model get a third state "for the 2026 CCC thing"? Hana answered the second question first, because it was arithmetic. Three hundred monthly observations support two states with full covariance in a handful of dimensions; with eleven sectors each state's covariance has 66 free entries, and three states with full covariance is about 200 parameters. $K = 2$, or $K = 2$ with the DTS factor structure of §12.5 imposed on each $\Sigma_k$, was what the data could carry.

The backtest was harder, because the one in last quarter's deck was beautiful. It had de-risked in the last week of February 2020 and bought back in on the Monday after the March bottom. Hana read the code and found why: it traded on the smoothed probabilities $\gamma_t$, which use returns *after* $t$. The backtest knew March 2020 was the bottom because it had read April. She reran it on the filtered $\xi_{t\mid t}$ and acted with a one-month delay, and the Sharpe ratio of the overlay fell by about half *(illustrative)*. What she put in the deck was the honest version of the claim, and it had a citation: Nystrup's 2014 DTU thesis (*Regime-Based Asset Allocation: Do Profitable Strategies Exist?*) tested exactly this, and a two-state Gaussian HMM still beat static rebalancing out of sample after costs and with an action delay. Smaller, real, and a month late, which is what a regime overlay is.

DATA-2840 was still open when the committee met.

Two-state Gaussian HMMs for asset allocation have a respectable lineage: Hamilton (1989) for the filter; Ang and Bekaert (2002) and Guidolin and Timmermann (2007) for regime-switching allocation; Kritzman, Page and Turkington (2012) for the practitioner case; Nystrup, Hansen, Madsen and Lindström (2015) and Nystrup, Madsen and Lindström (2018) for adaptive estimation; and Bernis, Carassus, Docq and Scotti (2015) for credit allocation specifically, with a two-state hidden chain driving a credit benchmark. Bohn and Stein state the motivation in one sentence (Bohn_Stein p.492): "the processes that drive credit risk during times of extreme stress may be quite different than those that drive credit risk during normal or even 'pretty bad' times."

That sentence is about why the regimes exist. The market in October 2026 supplied a reason to doubt which regimes the desk was measuring.

> **Trend Watch: The 2026 CCC Decompression.** *What changed:* the high-yield market split in two while its headline spread stayed calm. ICE BofA option-adjusted spreads (FRED): the CCC & lower OAS went from 7.46% at year-end 2024 to 8.85% at year-end 2025 and 12.78% on October 15, 2026, a post-2023 high. Over the same dates the BB OAS went 1.86%, 1.69%, 1.97%, and the overall HY OAS sat at 3.23%. The CCC/BB spread ratio rose from 4.0 to 5.2 to 6.5; the CCC−BB gap widened from 560 bp to 716 bp to 1,081 bp. Year-to-date total returns to October 15, 2026: CCC −5.21%, BB +0.33%, HY index +0.15%. Around it, the 10-year Treasury yield was 5.10% and the effective fed funds rate had moved from 3.62% (May 19) to 3.88% (September 17) (FRED, DGS10 and DFF). The Federal Reserve's May 2026 *Financial Stability Report* noted that software had become the largest sector in private-credit portfolios and that secondary leveraged-loan spreads rose, "reflecting a high concentration of leveraged loan borrowers in the software industry." *What it means for the desk:* a two-state model on the HY *index* reads October 2026 as calm, because the index spread is near its average. A model on the BB, B and CCC *vector* sees a different regime: low common-factor volatility, very high dispersion. That is why the reference implementation plants regimes that differ in idiosyncratic volatility, not only in means (§12.10). The dispersion regime is where the loss term of (12.1) diverges across buckets, and where index-level MAC models lose the plot.

## 12.5 Covariance You Can Trust: DTS Structure, EWMA, Shrinkage and Desmoothing

The covariance matrix is where MAC models fail quietly. Expected returns are argued about in investment committee; covariances are taken from the risk system and nobody asks. They deserve the same argument, because the covariance of eleven credit sectors is mostly one number (the common spread factor's variance) multiplied by things that change: spread levels, durations and the marking practices of the people who report the returns.

**Step 1: structure it with DTS.** From §12.3, a sector's excess return is $r^x_i \approx -D^{\text{spr}}_i\,\Delta s_i = -\text{DTS}_i\,u_i$ with $u_i = \Delta s_i/s_i$ the relative spread change. Stack the sectors, let $\Omega = \operatorname{Cov}(u)$, and

$$
\Sigma^{x} = \operatorname{diag}(\text{DTS})\;\Omega\;\operatorname{diag}(\text{DTS}). \tag{12.3}
$$

For total returns add the rates block and its cross term. Let $\rho_{y,s}$ be the correlation between yield changes and relative spread changes, the same object that sets empirical duration in §8.2. A sector's total return is $-\text{DTS}_i\,u_i - D^{\text{mod}}_i\,\Delta y$, so

$$
\Sigma = \Sigma^x + \sigma_{y}^2\,D^{\text{mod}}D^{\text{mod}\top} + \rho_{y,s}\,\sigma_y\,\big(a\,D^{\text{mod}\top} + D^{\text{mod}}a^{\top}\big), \qquad a_i = \text{DTS}_i\sqrt{\Omega_{ii}},
$$

where $\sigma_y$ is the volatility of yield changes. Setting $\rho_{y,s}=0$ gives the shortcut of treating the Treasury factor as independent of the spread factor, and the shortcut is an approximation that hides a bet on a sign. When rates move on growth news and spreads move against them, $\rho_{y,s}$ is negative, the cross term subtracts, and the result flatters long-duration IG while doing little for floating-rate loans, which carry almost no rate duration for the term to act on. When rates move on inflation, as in 2022, $\rho_{y,s}$ is positive and the same term adds to the variance of the long-duration book. Chapter 8 shows the sign changing twice since 2021 (§8.2, §8.7), so a covariance with $\rho_{y,s}$ hard-coded at zero contradicts the chapter that taught the desk to hedge with it. In this engine $\rho_{y,s}$ is a regime input from §12.4, one value per state of the chain, not a hard-coded zero; how it is estimated is in the Full Derivation below.

The reason to estimate $\Omega$ instead of $\Sigma$ directly is stability: relative spread changes have far more stable volatility across spread levels than absolute changes do, which is the empirical finding behind DTS. When spreads double, (12.3) doubles every sector's volatility automatically through $\text{DTS}$, rather than waiting three years for the sample covariance to notice.

> **[SOURCE EXTRACTION]** *Ben_Dor p.63:* "Traditionally, investment-grade credit portfolios are managed based on contributions to duration, while high-yield portfolios are managed based on market value weights. Using contributions to DTS across both markets could help bring consistency to this portfolio construction process."
>
> **Annotation.** Ben Dor and coauthors wrote this about core-plus mandates combining IG and HY, and MAC is the same problem with eleven markets instead of two. Market-value weights treat 10% in CLO BBB and 10% in ABS as the same bet; DTS contributions show the CLO tranche carrying several times the spread risk. The modern desk sets risk budgets in DTS contributions (§12.6) and reports market-value weights only to the client. The caveat for securitized sleeves: tranche DTS is a local measure, and mezzanine tranches gap in stress (their spread change is not proportional), so the DTS-implied volatility of a CLO BBB is a floor.

**Step 2: weight recent observations.** Nuveen does this explicitly:

> **[SOURCE EXTRACTION]** *Nuveen p.4:* "At Nuveen, we use a weighted covariance matrix, which gives more importance to more recent observations."
>
> **Annotation.** The standard implementation is the exponentially weighted moving average below. The paper does not give its decay parameter, which is the parameter that matters: it sets how fast the matrix forgets 2020 and how fast it learns April 2025. The modern desk chooses the decay by out-of-sample likelihood rather than taste, applies it to relative spread changes rather than returns, and shrinks the result (step 3), because a fast-decaying estimator has a small effective sample.

"More importance to more recent observations," Theo read aloud. "How much more?"

"That," said Kaz, "is the only question."

> **Math, Gently.** *Part (a): a covariance matrix is a seating chart with a memory.* Write the eleven sectors along the top of a table and down its side. Each cell answers one question: when the row sector has a bad month, how bad, on average, is the column sector's month? The diagonal cells are each sector's own wobble, its variance; the others say who moves with whom. That table is the covariance matrix, and it is how the optimizer decides which bets cancel and which pile up. Every cell is estimated from history, so the real question is how much history to believe. An exponentially weighted average answers with a memory that fades: with $\lambda = 0.97$, each observation keeps 97% of its weight for every month that passes, losing 3% a month, compounded. After 22.8 months an observation carries half its original weight, which is the half-life, and the whole memory is worth about 66 months of equally weighted data, the effective sample. Now count the cells: eleven variances and 55 distinct pairs, 66 numbers to estimate from 66 months' worth of memory. One observation per number. An estimate built that way is mostly noise, and an optimizer reads noise as opportunity. *Part (b): shrinkage is averaging your estimate with a simpler one you trust.* Suppose the sample says HY and loans had a correlation of 0.9, and a one-factor model, in which every sector moves only through one common credit factor, says 0.6. Neither is the truth. Shrinkage takes a weighted average, $\delta$ of the simple answer and $1 - \delta$ of the sample: with $\delta = 0.3$, $0.3 \times 0.6 + 0.7 \times 0.9 = 0.81$. The noisy estimate keeps most of its say, but every cell is pulled a little toward a structure that cannot invent a free lunch. The clever part, which Ledoit and Wolf worked out, is choosing $\delta$ from the data itself: more shrinkage when the sample is noisy, less when the target is badly wrong. The recursion and the shrinkage come next, and the formula for $\delta$ waits in the Full Derivation.

The EWMA recursion on monthly relative spread changes $u_t$ is

$$
\Omega_t = \lambda\,\Omega_{t-1} + (1-\lambda)\,u_t u_t^{\top}, \qquad 0 < \lambda < 1 ,
$$

with weights $(1-\lambda)\lambda^j$ on the observation $j$ months back. The weights sum to one; the effective number of observations is about $(1+\lambda)/(1-\lambda)$ and the half-life is $\ln 2 / \ln(1/\lambda)$. At $\lambda = 0.97$ monthly, the half-life is about 23 months and the effective sample about 66 months, the box's numbers.

Mags watched Kaz tune the decay. "Back in my day we did multi-asset credit too. It was called 'whatever the dealer had left on Friday.' The covariance matrix was me remembering which dealers stopped answering the phone in 1998." She paused. "Your thing does that automatically. With a half-life. Fine."

**Step 3: shrink it.** Eleven sectors have $11 \times 12/2 = 66$ distinct covariance entries, so a 66-month effective window leaves the box's one observation per parameter, the regime in which sample covariance matrices produce optimizers that bet heavily on noise. The repair is to shrink toward a structured target (Ledoit and Wolf 2004):

$$
\hat\Omega = \delta\,F + (1 - \delta)\,S, \qquad 0 \le \delta \le 1 ,
$$

where $S$ is the sample (or EWMA) matrix and $F$ is a one-factor target: with market factor $m$ (the equal-weighted average of the $u_i$), $F_{ij} = \beta_i\beta_j\sigma_m^2$ off the diagonal and $F_{ii} = S_{ii}$. Why the mixture stays a valid covariance matrix, how the intensity $\delta$ is chosen, and how the rate–spread correlation of Step 1 is estimated state by state are the next subsection.

#### The Full Derivation

*The target is positive semidefinite.* The target is positive semidefinite because each residual variance $S_{ii} - \beta_i^2\sigma_m^2$ is nonnegative by Cauchy–Schwarz, and a convex combination of PSD matrices is PSD.

*The shrinkage intensity.* The Ledoit–Wolf intensity is

$$
\delta^{\star} = \max\!\Big(0,\; \min\!\Big(1,\; \frac{\hat\pi - \hat\rho}{\hat\gamma\,T}\Big)\Big),
$$

with $\hat\pi = \sum_{ij}\widehat{\operatorname{AVar}}(\sqrt{T}s_{ij})$ the estimation noise in $S$, $\hat\gamma = \|F - S\|_F^2$ the misspecification of the target, and $\hat\rho$ the covariance between target and sample errors. The reference code uses the diagonal part of $\hat\rho$ only (the target's diagonal equals the sample's, so those terms carry no shrinkage benefit) and drops the off-diagonal $\hat\rho$ terms. That is a documented simplification which errs toward slightly more shrinkage, the safe direction for an optimizer.

*The rate–spread correlation as a regime input.* The chain of §12.4 already supplies the states, so the engine estimates a $\rho_k$ for each state beside $\mu_k$ and $\Sigma_k$. The chain itself stays fitted on sector excess returns, which contain no yield changes, so $\hat\rho_k$ is a weighted statistic and not a fitted parameter: the correlation of $\Delta y_t$ with the common spread factor's relative change, weighted by the smoothed probabilities $\gamma_t(k)$ in the same form as the M-step moments. Each $\rho_k$ goes inside that state's total-return covariance $\Sigma_k$, and (12.2) does the mixing with today's filtered probabilities. Averaging $\rho$ across states and dropping the average into one covariance would lose something real, because the mixture term in (12.2) is what carries the uncertainty about which state you are in, and the cross term belongs inside it. Three cautions apply. A common $\rho_{y,s}$ applied to every sector can break positive semidefiniteness when sector correlations are low and $|\rho_{y,s}|$ is large, so the engine checks the smallest eigenvalue after substitution and shrinks $|\rho_{y,s}|$, or estimates it sector by sector, if the check fails. The stress state has few months behind it, so $\hat\rho_k$ is shrunk toward its full-sample value and carries an interval. And a calm/stress chain built on spreads may not separate a growth-scare stress from an inflation stress; if it cannot, $\hat\rho_k$ averages the two signs and shrinks toward zero without announcing it, and the fallback is the rolling-correlation flag of §8.7. Estimating on smoothed probabilities is an in-sample act; acting on the result uses the filtered ones, with the delay of §12.4.

**Step 4: desmooth the private sleeve.** Nuveen confronts the absence of an honest return series for direct lending directly:

> **[SOURCE EXTRACTION]** *Nuveen p.9:* "Middle market direct lending (Private Credit): Proxy Index using S&P UBS Leveraged Loan B Index."
>
> **Annotation.** This is the right instinct: when the asset's own return series is a sequence of appraisals, import the risk from the closest traded thing. The modern desk treats the proxy as a *floor* rather than an estimate. Middle-market borrowers are smaller than single-B syndicated borrowers, with a mean interest coverage of about 2.0x against 2.7x for leveraged-loan borrowers and a post-default value of about 33% against 52% (Cai and Haque, FEDS Notes, 2024). The same spread move costs a direct-lending book more. When the sleeve's own NAV series must be used (for a BDC, say), desmooth it.

Kaz still had the BDC's 1.9% on the screen from Monday. "Measured by the fund," Mags asked, "or by the fund's lawyer?"

> **Math, Gently.** *A thermometer with a lag.* Picture a thermometer that, each hour, reports half of the true change and half of what it said last hour. Feed it a true series of $+3, -3, +3, -3$ and it reports $1.5, -0.75, 1.1, -0.9$: the wiggles come out about a third of their true size, and anyone estimating volatility from the report concludes the room is calm. Nothing is lost, only delayed. A single true move of $-6$ followed by quiet comes out as $-3, -1.5, -0.75, -0.4$ and so on, which adds up to $-6$ in the end: the same loss, spread so thin that no single reading looks alarming. Appraisal-based marks behave the same way, because a valuation committee anchors on last quarter's mark and moves only part of the way toward the new evidence. The persistence parameter $\phi$ is how much weight the old mark keeps; the thermometer has $\phi = 0.5$. At this chapter's $\phi = 0.8$, the measured variance shrinks to $\xi = (1-\phi)/(1+\phi) = 1/9$ of the true one, so the true volatility is $\sqrt 9 = 3$ times the reported one, and Kaz's 1.9% is about 5.7%, close to the traded loan proxy. The year's sum is not where the lie is; the annualization is, because it treats a delay as calm. The algebra follows.

In words: if the reported return is a moving average of true returns, the reported volatility, beta and correlation are each understated by a different factor, the long-horizon variance is not understated at all, and in the common AR(1) case each factor has a closed form, along with the one-line recursion that recovers the true returns.

#### The Full Derivation

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

At $\phi = 0.8$, which is not an exotic level of persistence for appraisal-based marks, $\xi = 1/9$: true volatility is three times reported, true beta five times reported contemporaneous beta, and the correlation is understated by 40%. That is the thermometer's 5.7% in matrix form. Mags's question has an answer, and it is the formula's: $\sigma_{\text{true}} = \sigma_{\text{reported}}/\sqrt{\sum_j \theta_j^2}$, whoever measured it.

#### The listed twin

On Friday morning, 16 October, Theo arrived with the objection that a banker raises against any expensive analysis: somebody else had already done it, and for free. He had the listed BDCs on one screen. By one market-data aggregator's count, the externally managed ones traded that day at a median of about 0.76 times book value, a basket of the same kind of sponsor loans, with a share price that prints every second the market is open.

"That's the market's own desmoothing," he said. "The NAV says a dollar. The people who can sell tomorrow say seventy-six cents."

"Then why desmooth anything?" Kaz asked.

"Because the client owns the non-traded one, and the NAV is what's in the spreadsheet. Desmooth the NAV to get its risk into the covariance. Read the listed discount as a separate number, about what the marks will do next." He tapped the screen. "And the listed price stays out of the recursion entirely."

"Back in my day," said Mags, "the discount was the only honest number in the sector, and nobody put it in a covariance matrix either." She considered it. "This is better."

> **Ways This Blows Up.** *Desmoothing the wrong series.* A listed BDC's share price is marked by the market every day; desmoothing it inflates a volatility that was never smoothed. Desmooth the NAV series and treat the price-to-NAV discount as a separate liquidity signal (Chapter 20). *Mixing frequencies.* Desmoothing a quarterly NAV series and dropping it into a monthly covariance matrix aligns nothing; aggregate the public series to quarterly first. *Non-invertible fits.* The moving-average weights are identified only up to reversal ($\theta$ and its mirror image give the same autocorrelations); the recursion that recovers true returns explodes for the non-invertible one. The code checks the roots and refuses rather than guesses.

## 12.6 Optimization: Mean-Variance, Risk Budgets, and Why the Frontier Is Flat

Nuveen's optimizer (Nuveen pp.5–6) takes a five-year horizon, a 6.00% minimum return target and the sector bounds of Figure 5 (HY 20–60%, leveraged loans 5–25%, EM sovereign and EM corporate HY 2–15% each, CoCos and HY preferreds 2–10% each, ABS, CMBS BBB, CLO BBB to B and CRT 0–10% each, middle-market direct lending 0–35%), and produces six efficient portfolios. Forward returns run from 5.11% to 6.20%, volatilities from 5.50% to 6.29%, forward Sharpe ratios from 0.26 to 0.40 (Figure 6).

> **[SOURCE EXTRACTION]** *Nuveen p.6:* "portfolio six has the optimal allocation, with a return of 6.20%. While portfolio six represents an optimal allocation under the given assumptions and constraints, it should be viewed as a starting point for discussion."
>
> **Annotation.** This is the most honest sentence a vendor of optimizers can write, and the math below explains why it is also correct. The six portfolios are 110 bp apart in return and 79 bp apart in volatility, and the inputs that produced them (a five-year expected loss, a spread path, a covariance) each carry error bars wider than that. The modern desk keeps the optimizer and changes its job: it searches for the region of allocations that are near-optimal under perturbed inputs (resampling, shrinkage of means, or a robust objective) and lets the binding constraints, which are known exactly, do the rest.

Ines looked at Figure 6 for about four seconds. "Six portfolios, 110 basis points apart, and you want to argue about number four versus number five? That's not a hand. That's a tip."

**Why the frontier is flat.** Suppose every sector loads on one common spread factor $f$ with volatility normalized to one: excess return $x_i + a_i f + \epsilon_i$, with expected excess return $x_i = \mu_i - r$, factor exposure $a_i = \text{DTS}_i\,\sigma(u)\,b_i > 0$ and idiosyncratic noise $\epsilon_i$. For a long-only portfolio $w \ge 0$, the variance is $(w^{\top}a)^2 + \sum_i w_i^2\sigma^2_{\epsilon,i} \ge (w^{\top}a)^2$, so

$$
\text{SR}(w) \;=\; \frac{w^{\top}x}{\sqrt{w^{\top}\Sigma w}} \;\le\; \frac{\sum_i w_i x_i}{\sum_i w_i a_i} \;=\; \sum_i \underbrace{\frac{w_i a_i}{\sum_j w_j a_j}}_{\text{risk share}}\;\frac{x_i}{a_i} \;\le\; \max_i \frac{x_i}{a_i}.
$$

The middle expression is the mediant inequality: the portfolio's return per unit of factor exposure is a weighted average of the sectors' *systematic Sharpe ratios* $x_i/a_i$, weighted by factor-risk share. Once idiosyncratic risk is diversified, every long-only credit portfolio's Sharpe ratio lies between the smallest and the largest systematic Sharpe in the menu. If spreads are priced to the common factor, as they roughly are, those ratios cluster, and the frontier is flat. Nuveen's 0.26–0.40 is that cluster seen through constraints.

A flat objective is an amplifier for input error. Chopra and Ziemba (1993) showed that errors in expected returns cost a mean-variance investor far more certainty-equivalent wealth than errors in variances, which in turn matter more than errors in covariances; the oft-quoted multiples (roughly an order of magnitude for means versus variances) depend on risk tolerance, so quote the paper, not the folklore. DeMiguel, Garlappi and Uppal (2009) found that sample-based mean-variance portfolios did not reliably beat equal weighting out of sample in their datasets, because the estimation window needed to beat $1/N$ is far longer than the data. In MAC terms: when every portfolio on the frontier has the same Sharpe within the error bars, the optimizer's choice among them is decided by noise in $\mu$, and its weights swing by tens of points when an expected-loss assumption moves by 25 bp. Figure 12.3 runs that experiment on the reference engine's inputs.

![Figure 12.3: The same mean-variance optimizer with 25 bp of random error in each sector's forward return: with only a budget and long-only, the average draw moves 30% of NAV away from the median weights, and with Nuveen's bounds, the 15% illiquid cap, the liquid floor and the days budget it moves 3.5%. Illustrative: Listing 12.1 inputs and the engine of Listings 12.3 and 12.5, 400 draws, risk aversion 8; lines show the 5th to 95th percentile of each weight and circles the median.](assets/figures/ch12_constraints_decide.png)

**Three formulations.** All three are in the reference code.

*Mean-variance with bounds:* $\max_w\; w^{\top}\mu - \tfrac{\gamma}{2}w^{\top}\Sigma w$ subject to $\mathbf{1}^{\top}w = 1$, $l \le w \le u$, and optionally $w^{\top}\mu \ge \mu^{\star}$. With bounds inactive, the maximum-Sharpe (tangency) solution is $w \propto \Sigma^{-1}(\mu - r\mathbf{1})$, which is the unit test.

*Risk budgeting:* choose $w$ so that each sector's contribution to variance equals a budget $b_i$ ($\sum_i b_i = 1$):

$$
\text{RC}_i(w) = \frac{w_i(\Sigma w)_i}{w^{\top}\Sigma w} = b_i .
$$

This system is nonlinear, but it is the first-order condition of a convex problem (Maillard, Roncalli and Teiletche 2010; Bruder and Roncalli 2012): $\min_{y>0}\; \tfrac12 y^{\top}\Sigma y - \sum_i b_i \ln y_i$. Setting the gradient to zero gives $(\Sigma y)_i = b_i/y_i$, so $y_i(\Sigma y)_i = b_i$; summing, $y^{\top}\Sigma y = 1$; and $w = y/\mathbf{1}^{\top}y$ inherits $\text{RC}_i = b_i$ because risk contributions are scale-free. Newton's method on this objective converges in a handful of steps. Budgets set in DTS contributions are the MAC version of Ben Dor's consistency argument (§12.5), and they need no expected returns at all, which is a feature when the expected returns are the least reliable input.

*The beta share.* Paleologo's rule (Paleologo p.124) is "The higher your Sharpe, the lower the exposure to the market." Derive it: combine a credit-beta stream with Sharpe $\text{SR}_\beta$ and an uncorrelated alpha overlay with Sharpe $\text{SR}_\alpha$. Mean-variance sizes each at $x_k \propto \text{SR}_k/\sigma_k$, so each stream's variance contribution is proportional to $\text{SR}_k^2$, and the share of the variance budget given to beta is

$$
\frac{\text{SR}_\beta^2}{\text{SR}_\alpha^2 + \text{SR}_\beta^2} \;=\; \frac{1}{1 + (\text{SR}_\alpha/\text{SR}_\beta)^2}.
$$

With a strategic credit beta at a Sharpe of 0.35 and a sector-rotation overlay that also runs at 0.35, beta gets half the risk budget. If the overlay's Sharpe is really 0.1, which is what the AQR residual alphas in §12.1 suggest for the median manager, beta should get over 90% and the overlay should be small. The rotation desk's risk budget is a measured quantity, not a political one.

> **[SOURCE EXTRACTION]** *Dynkin p.67:* "when adding the same credit index to a 60/40 equities/Treasuries benchmark, the portfolio Sharpe ratio will increase if credit replaces equities but will decrease if credit replaces Treasuries."
>
> **Annotation.** The value of a credit sleeve depends on what it is funded from, and the same is true inside MAC: a tilt into CLO BBB funded from HY is a different trade from one funded from ABS, even with the same target weight. The modern desk specifies every tactical tilt as a *pair* (into, out of) with a DTS-neutral or DTS-targeted funding leg, so the risk change is known before the trade, not discovered in the attribution.

## 12.7 Liquidity Tiers as the Binding Constraint

"Liquidity tiers," Theo said, pointing at the constraint table.

"Liquidity *tears*?" Kaz asked. "Is that the technical term for March 2020?"

"It is now," said Mags.

The optimizer's bounds come from the client; the liquidity constraints come from the law and from the exit door, and they bind harder than either the return target or the risk budget. The US template is SEC Rule 22e-4, adopted October 13, 2016. It requires open-end funds to classify each investment into one of four buckets by how quickly it can be converted to cash (or sold) without significantly changing its market value: *highly liquid* (convertible to cash in three business days or less), *moderately liquid* (more than three but no more than seven calendar days), *less liquid* (can be sold within seven calendar days, but settlement is expected to take longer), and *illiquid* (cannot be sold within seven calendar days without significantly moving the price). A fund may not acquire an illiquid investment if afterwards more than 15% of net assets would be illiquid, and it must set a highly liquid investment minimum. On August 28, 2024 the SEC adopted amendments to Forms N-PORT and N-CEN and guidance on the rule, without adopting the 2022 swing-pricing and hard-close proposal; compliance began November 17, 2025, or May 18, 2026 for fund groups under \$1bn (Sullivan & Cromwell memo, September 2024). The "less liquid" bucket exists largely because of leveraged loans, whose assignments routinely settle after seven days: a loan can be *sold* on Monday and still not be *cash* two weeks later.

**The constraint set.** Let $\mathcal{T}_{\text{IL}}$ be the illiquid sectors, $\mathcal{T}_{\text{L}}$ the highly and moderately liquid sectors, $\tau_i$ the days needed to liquidate sector $i$ at an acceptable participation rate, and $\text{LCS}_i$ its round-trip cost:

$$
\sum_{i \in \mathcal{T}_{\text{IL}}} w_i \le 0.15, \qquad
\sum_{i \in \mathcal{T}_{\text{L}}} w_i \ge h_{\min}, \qquad
\sum_i w_i\,\tau_i \le \bar\tau, \qquad
\text{cost}(w) = \sum_i |w_i - w^{\text{ref}}_i|\,\frac{\text{LCS}_i}{2}. \tag{12.4}
$$

The days budget prices what the cap does not: 15% in direct lending at $\tau = 180$ days contributes 27 days to the portfolio's weighted liquidation time on its own. A position-level $\tau_i = \text{position}_i / (\text{participation} \times \text{ADV}_i)$ is better than a sector constant when you have the volume data (Chapter 17 and Chapter 19).

The KKT conditions say what the cap costs. If $\eta \ge 0$ is the multiplier on the illiquid cap in the mean-variance problem, then at an interior optimum in sector $i \in \mathcal{T}_{\text{IL}}$, $\mu_i - \gamma(\Sigma w)_i - \eta = \nu$, the common multiplier on the budget constraint. The illiquidity premium has to beat $\eta$, the shadow price of the cap, before another dollar of private credit is worth buying. When the reference code reports $\eta$ for Kaz's allocation, it is the number to bring to the investment committee instead of "direct lending yields 10%."

> **[SOURCE EXTRACTION]** *Ben_Dor p.296:* "risk-averse investors demand additional spread, a risk premium, beyond the expected default and liquidity costs, to compensate them for the possibility that the credit bond may have to be sold exactly during economic times when both default and liquidity costs are high."
>
> **Annotation.** This is the economic content of the liquidity tier: the cost of an illiquid asset is not its average round-trip cost but its cost in the state where you need to sell. For a perpetual BDC that state is literal. The gate (5% of NAV per quarter) is a contractual statement that you cannot sell in the bad state. The modern desk models it as a tier with a state-dependent exit time. If redemption requests total $Q$ of NAV against a gate $g$, each redeemer receives $g/Q$ of its request per quarter, so with $Q = 15\%$ and $g = 5\%$ a full exit takes at least three quarters, and longer if the queue keeps growing.

The 13-week model came back, as it always does. Theo rebuilt it on Thursday as a redemption-coverage ledger for the BDC: inflows, loan repayments, undrawn bank lines and cash on one side; 5% of NAV per quarter of redemptions on the other; thirteen weeks at a time. The Fed had done the same exercise at the industry level: the ten largest perpetual BDCs, holding about 80% of sector assets, could cover at least three quarters of 5% redemptions from bank lines and cash (Federal Reserve, *Financial Stability Report*, May 2026, Box 4.1). "Same spreadsheet," Theo said. "Bigger borrower."

> **Trend Watch: Private Credit's First Redemption Cycle (September 2025 to Q1 2026).** *What changed:* the semi-liquid wrappers that brought private credit to wealth channels met their first sustained redemption wave. By the Fed's count, semi-liquid vehicles held \$425bn gross (\$241bn net) of assets, about 20% of private-credit vehicle net assets: perpetual-life BDCs \$306bn gross (\$161bn net) and interval funds \$119bn gross (\$80bn net). Redemption requests rose in 2025Q4 and "accelerated further in the first quarter of 2026, when a number of funds received requests that were much larger than 5 percent of NAV"; most managers capped payouts at 5%; and "accepted redemption requests somewhat exceeded new inflows in the first quarter of 2026, the first time this has occurred since these vehicles were created" (Federal Reserve, *Financial Stability Report*, May 2026, Box 4.1). Six months earlier the November 2025 report had judged the First Brands and Tricolor bankruptcies to "so far appear to be isolated events" while noting that they "highlight that unexpected losses could arise from opaque off-balance-sheet funding arrangements." *What it means for the desk:* the 5% gate is a liquidity tier that the optimizer must see, and its exit time is a function of everyone else's behavior. A MAC model that treats a BDC sleeve as a "less liquid" credit allocation with a 1.9% volatility is long a queue position it has not priced.

### Deep-Dive Resource Graph (§12.4–12.7)

**Podcasts**

- **Goldman Sachs Sees 'Uncomfortable Tension' in Credit Markets** (*The Credit Edge*, Bloomberg Intelligence, guest Amanda Lynam, Goldman Sachs chief credit strategist, 4 Jun 2026). Spreads tight to prewar levels while the facts worsen, "the yield-based buyer is really in the driver's seat", plus CCC underperformance and structured-product value: a dated regime reading to run through the two-state model of §12.4. https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/goldman-sachs-sees-uncomfortable-tension-in-credit-markets
- **Antti Ilmanen - Understanding Return Expectations (S7E21)** (*Flirting with Models*, host Corey Hoffstein, 15 Sep 2025). Ilmanen on how investors form return expectations, from objective versus subjective views to capital market assumptions: the input-error problem behind the flat frontier of §12.6 and the regime-to-assumptions step of §12.4. https://www.flirtingwithmodels.com/episodes/O2AWOMGEWHH
- **Credit Microcycles at Diameter** (*Capital Allocators*, host Ted Seides, guest Jonathan Lewinsohn, Diameter Capital, 2 Feb 2026). The discretionary counterpart to a regime model: how a credit portfolio manager frames short cycles inside the long cycle, as a contrast to the filtered-probability approach of §12.4. https://www.capitalallocators.com/podcast/credit-microcycles-at-diameter/
- **Dimensional Says High-Yield Public Debt Has the Edge Over Private** (*The Credit Edge*, Bloomberg Intelligence, guest Savina Rizova, Dimensional, 29 May 2025). A factor house's prior ("There is no outperformance relative to high-yield public bonds"), with better liquidity and transparency as the public-market offset: it sets the illiquidity-premium prior for the liquidity tiers of §12.7. https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/dimensional-says-public-debt-has-the-edge-over-private

**Practitioner Writing**

- **A Look Under the Hood** (Howard Marks, Oaktree memo, 28 Oct 2025). Marks's notes from a meeting with a state pension fund on risk posture and portfolio construction: the allocator's side of the table for the risk-budget discussion in §12.6. https://www.oaktreecapital.com/insights/memo/a-look-under-the-hood
- Federal Reserve, *Financial Stability Report* (November 2025; May 2026, Box 4.1 on semi-liquid private-credit vehicles): https://www.federalreserve.gov/publications/financial-stability-report.htm
- Sullivan & Cromwell, memo on the 2024 amendments to Forms N-PORT and N-CEN and liquidity-rule guidance: https://www.sullcrom.com/insights/memo/2024/September/Amendments-Forms-N-PORT-N-CEN-Liquidity-Rule-Guidance

**Academic Papers**

- Getmansky, Lo and Makarov (2004), *An Econometric Model of Serial Correlation and Illiquidity in Hedge Fund Returns*, Journal of Financial Economics 74(3); NBER w9571: https://www.nber.org/papers/w9571
- Kritzman, Page and Turkington (2012), *Regime Shifts: Implications for Dynamic Strategies*, Financial Analysts Journal 68(3): https://rpc.cfainstitute.org/research/financial-analysts-journal/2012/regime-shifts-implications-for-dynamic-strategies-corrected
- Nystrup (2014), *Regime-Based Asset Allocation: Do Profitable Strategies Exist?*, DTU M.Sc. thesis: https://www2.imm.dtu.dk/pubdb/pubs/6808-full.html
- Bernis, Carassus, Docq and Scotti (2015), *Optimal Credit Allocation Under Regime Uncertainty With Sensitivity Analysis*, IJTAF 18(1): https://ideas.repec.org/a/wsi/ijtafx/v18y2015i01ns0219024915500028.html
- Hamilton (1989), *A New Approach to the Economic Analysis of Nonstationary Time Series and the Business Cycle*, Econometrica; Ledoit and Wolf (2004), *Honey, I Shrunk the Sample Covariance Matrix*, Journal of Portfolio Management; Maillard, Roncalli and Teiletche (2010), *On the Properties of Equally-Weighted Risk Contributions Portfolios*; Chopra and Ziemba (1993), *The Effect of Errors in Means, Variances, and Covariances on Optimal Portfolio Choice*, Journal of Portfolio Management; DeMiguel, Garlappi and Uppal (2009), *Optimal Versus Naive Diversification*, Review of Financial Studies.

**Data & Code**

- SEC Rule 22e-4 adopting release (2016): https://www.sec.gov/rules-regulations/2016/10/investment-company-liquidity-risk-management-programs ; rule text at Cornell LII: https://www.law.cornell.edu/cfr/text/17/270.22e-4

## 12.8 Tactical Overlays and the Turnover Budget

The strategic allocation answers "what should we own over five years?" The tactical overlay answers "what should we change this year?", which Nuveen frames as a shorter, one-year horizon applied to the same framework (Nuveen pp.3 and 7). The engineering question is how much the overlay may move the book. Write the tilt budget as an $\ell_1$ constraint, $\|w - w^{\text{SAA}}\|_1 \le \kappa$, and linearize it with split variables: $w = w^{\text{SAA}} + d^{+} - d^{-}$ with $d^{\pm} \ge 0$ and $\mathbf{1}^{\top}(d^{+} + d^{-}) \le \kappa$. Because each unit of $d^{+}$ and $d^{-}$ also costs $\text{LCS}_i/2$ in the objective, the optimizer never sets both positive for the same sector, so $d^{+} + d^{-} = |w - w^{\text{SAA}}|$ at the solution and the constraint is exactly the turnover budget.

Three signals feed the overlay's expected returns, and they disagree in exactly the months that matter.

*Carry.* Across sectors, carry is the yield-minus-expected-loss term of (12.1) and it has a long record as a premium.

> **[SOURCE EXTRACTION]** *Man_2022 p.26:* "Koijen et al. find that the Carry factor has, on average, positive returns, with Sharpe ratios between 0.4 and 0.5. Over the long run, Carry appears to offer a significant premium, but with incredibly high volatility of returns."
>
> **Annotation.** Koijen, Moskowitz, Pedersen and Vrugt (2018) measured carry across asset classes, including credit; the MAC application is cross-sector carry per unit of DTS (Ratio 2 of §12.3). "Incredibly high volatility" is the regime problem in two words: carry pays steadily in calm and gives it back in a stress month, because high-carry sectors are high-DTS sectors. The modern desk scales the carry tilt by the filtered calm-state probability, which is a regime hedge bought at the price of being a month late.

*Mean reversion.* The OU forecast of §12.3 buys after spreads widen. Blackstone's systematic credit description says it plainly (Blackstone p.1): "When credit spreads widen aggressively (often due to market panic rather than fundamental deterioration), the model algorithmically increases credit exposure."

*Regime.* The HMM of §12.4 does the opposite in the same month: the stress probability rises and the regime-mixture means in (12.2) fall.

The reconciliation is about timing, and the sign of the error matters. In the first weeks of a widening, the regime signal is right and the mean-reversion signal is early. After the peak, the reversion signal is right and the regime filter, still reading stress, is late. BlackRock's warning about defensive tilts is the cost of being late (BlackRock p.5): "In many cases, these managers gave up more excess return in subsequent 'Very Positive' regimes than was mitigated on the downside during 'Very Negative' regimes." A practical overlay therefore uses the regime probability to *size* the tilt budget (smaller $\kappa$ in stress, so that neither signal can move the book much while it is least reliable) and the valuation signal to *direct* it. Equity momentum in credit, which Dynkin and coauthors found positive in both drawdown and recovery regimes (§12.4; Dynkin p.617), is the one signal in the set that does not need the reconciliation.

> **Trend Watch: April 2025 as a Transition Test.** *What happened:* a regime transition in about 26 trading days of drawdown (February 28 to April 7). The HY OAS moved from 259 bp (January 22) to 461 bp (April 7); peak-to-trough total returns were HY −3.83% (February 28 to April 7), CCC −7.80%, B −4.21%, BB −2.83%, IG −3.03% (March 3 to April 11), EM corporate −2.37% and EM HY corporate −3.79% (ICE BofA indices via FRED). HY mutual funds and ETFs saw −\$10.9bn of flows in April and +\$18.5bn from May to September, and by the end of September 2025 the HY spread-to-worst was 299 bp, "only 22 bps wider than the post-2008 tights reached earlier in 2025," after 12 straight quarterly gains, the longest run since 1997 (MacKay Shields, *High Yield 4Q 2025 Outlook*, October 2025). *What it means for the desk:* the drawdowns lined up by DTS and quality, as (12.3) predicts, and the snap-back was faster than any monthly regime filter. A book that de-risked on the filtered stress probability in mid-April would have sold near the wides and paid round-trip LCS to own less of the recovery. The private-credit sleeve's marks did not move at all, by construction, which made it look like the best diversifier of the quarter. That is the desmoothing lesson of §12.5, delivered in real time.

## 12.9 Case Studies: Three Stress Tests of the Framework

### Case Study A: April 2025, a Regime Transition in 25 Trading Days

The tape is in the Trend Watch of §12.8: HY OAS from 259 bp to 461 bp, VIX at 52.33, sector drawdowns ordered by DTS and quality from CCC (−7.80%) to EM corporates (−2.37%), then a recovery that left HY spreads near their post-2008 tights by September. Three things a systematic MAC desk should have seen. *First*, the filtered stress probability rises only after the first bad month has printed. A monthly filter with a one-month action delay acts in May, after the trough. A weekly filter on the BB/B/CCC vector would have acted in mid-March, near the start. *Second*, cross-sector correlation went to one exactly as the DTS-scaled factor model predicts. With (12.3), doubling the factor variance raises every pairwise correlation toward one without any change to $\Omega$'s structure, so the model's stress covariance was right before the fact; only its *probability* was late. *Third*, the private-credit sleeve did not move. A desk that rebalanced to target weights in April mechanically *sold* public credit near the wides to stay at its private-credit weight, because private credit had "outperformed." The fix is in the spec: rebalance on desmoothed weights, or not at all, inside a stress regime. Figure 12.4 shows the tape and what a month-end sample of it looks like.

![Figure 12.4: The April 2025 peak fell between month-ends: the daily HY OAS peaked at 461 bp on April 7, the highest month-end print of the half-year is 394 bp on April 30, 23 days later, and the losses by bucket rise from 2.83% for BB to 7.80% for CCC. Source: ICE BofA US High Yield OAS and total-return indices via FRED (BAMLH0A0HYM2, BAMLHYH0A0HYM2TRIV, BAMLHYH0A1BBTRIV, BAMLHYH0A2BTRIV, BAMLHYH0A3CMTRIV), pulled October 18, 2026; losses run from each index's high since February 1 to its April 7 low.](assets/figures/ch12_april_2025_daily_vs_month_end.png)

### Case Study B: First Brands, Tricolor and the First BDC Redemption Cycle

First Brands, an auto-parts supplier with about \$5.5bn of leveraged loans and no HY bonds, filed for Chapter 11 in September 2025; its term loan, rated B1/B+ that month, traded at \$96 on September 4 and \$11 on October 14. Tricolor, a subprime auto lender, filed for Chapter 7; AAA tranches of its ABS traded in the \$70s and a lower tranche fell from \$105 to \$12.50 (MacKay Shields, *High Yield 4Q 2025 Outlook*, October 2025). Both cases involved allegations about collateral, including receivables pledged more than once. JPMorgan took a charge of about \$170mm on Tricolor, and Jamie Dimon said on the October 14 earnings call, "When you see one cockroach, there are probably more" (CNN Business, October 16, 2025). Cambridge Associates (November 2025) noted that the losses fell on banks, CLOs and public ABS, not only on private lenders, and cited a KBRA direct-lending default forecast of 1.5% for 2025 against roughly 3.8% for broadly syndicated loans.

For the RSSG reader, double-pledged receivables are a collateral-perfection problem: the UCC search and the lien review, not a macro forecast. No allocation model would have predicted either failure. What the framework *does* control is the damage. A single-issuer DTS cap limits it. A recovery assumption set by the seat in the waterfall prices it: a fraud recovers far less than the 52% syndicated-loan average. And the liquidity tier caps the second-round effect. Through the Fed's two reports, "isolated events" (November 2025) became "accepted redemption requests somewhat exceeded new inflows" (May 2026). The hit to private credit came through the gate, not through the marks. Kaz's 35% allocation would have met that queue at the head of the line.

### Case Study C: The 2026 CCC/BB Split

By October 15, 2026, the HY index OAS was 323 bp, unremarkable. Inside it, CCC was at 1,278 bp and BB at 197 bp, a 1,081 bp gap; CCC returned −5.21% year to date against +0.33% for BB (FRED). An index-level MAC engine reads "HY at 323, fair, hold the strategic weight." A bucket-level engine sees two markets. The break-even default rate on CCC is about 19.7% a year at a 35% recovery (*illustrative*; §12.3), and the expected-loss term of (12.1) for the CCC bucket depends almost entirely on which issuers enter liability management transactions and at what recovery (Chapter 13). CCC risk also arrives through the back door. CLO BBB to B tranches are levered to the CCC bucket through the overcollateralization tests (typical documents haircut CCC holdings above about 7.5% of the pool to market value), and the Fed's May 2026 report put software at the top of private-credit sector exposure. The systematic response is to split the HY sleeve into BB, B and CCC sub-sleeves with their own loss terms, to compute CLO tranche loss as a function of the CCC bucket rather than the rating, and to fit the regime model on the bucket vector, where a dispersion regime is visible as rising idiosyncratic variance even while the index is calm. Figure 12.5 shows the split.

![Figure 12.5: On October 15, 2026 the HY index OAS (323 bp) looked ordinary while CCC stood at 1,278 bp against 197 bp for BB, and CCC had lost 5.21% year to date against a 0.33% gain for BB. Source: ICE BofA US High Yield OAS and total-return indices via FRED (BAMLH0A0HYM2, BAMLH0A1HYBB, BAMLH0A2HYB, BAMLH0A3HYC; BAMLHYH0A0HYM2TRIV, BAMLHYH0A1BBTRIV, BAMLHYH0A2BTRIV, BAMLHYH0A3CMTRIV), pulled October 18, 2026; returns from December 31, 2025.](assets/figures/ch12_ccc_bb_split.png)

## 12.10 The MAC Engine: A Reference Implementation

### Specification for AI Implementation

**The Spec You Hand the Robot.** What ROBO built from the vague version ("maximize Sharpe across our credit sectors"): a portfolio at the 35% direct-lending bound, a claimed volatility it computed from appraisal marks, and an EM sovereign allocation sized on an index yield that included a defaulted country. It never complains and never guesses; it did exactly what it was asked. The precise version follows.

*Inputs.* Sector table, one row per sector: `{sector: str, yld, pd, rec: decimal, dmod, dspr: years, spread: decimal, dspread_h: decimal change over the horizon, tier in {HL, ML, LL, IL}, days: float, lcs_bp: float, w_min, w_max: decimal}`. Return panel `R: (T, n)` monthly excess returns (decimal), relative spread changes `U: (T, n)`. Horizon `h` in years. All rates are decimals per year; the code raises if anything looks like a percent.

*Pipeline.* (1) forward returns by (12.1) with physical PD and seat-level recovery; (2) desmooth any appraisal-marked series (GLM weights, invertibility check) or build its risk from a proxy via `smoothed_view`; (3) $\Omega$ by EWMA on relative spread changes, shrunk to a one-factor target, then $\Sigma$ by (12.3); (4) two-state HMM on the bucket-level excess-return vector, filtered probabilities only; (5) regime-mixture moments by (12.2); (6) strategic allocation by mean-variance with the tiers of (12.4), with shadow prices of the binding constraints reported; (7) tactical tilt with an $\ell_1$ budget and LCS costs.

*Edge cases and guards.* Log-space densities with a max-shift before exponentiating; ridge $10^{-10}$ on regime covariances; label alignment after every fit; refuse non-invertible smoothing weights; feasibility check on bounds before optimizing; every optimizer output is re-checked against every constraint by assert, not trusted from the solver's success flag.

The five blocks run in order in one interpreter; each ends in asserts that are the acceptance tests.

Every allocation engine begins with a table nobody enjoys typing. Theo's has eleven rows, one per sector, and a dozen columns that each mean something different: a yield, a physical default probability, a recovery, two durations, a spread, an expected spread move, a liquidity tier, days to liquidate, a round-trip cost and a pair of weight bounds. In a spreadsheet this table is right on Monday and wrong by Friday, when someone pastes 6.97 into a column that wanted 0.0697 and the optimizer discovers a sector yielding 697%. The desk automates this first step for the dullest reason there is: the forward return is the number every later block inherits, so a unit error here is a unit error everywhere, and it is cheapest to catch before anything has been optimized.

Block 1 turns the table into the two vectors the rest of the chapter runs on. The inputs are illustrative decimals per year, durations in years, and weight bounds read from Nuveen's Figure 5. Three small functions implement (12.1) term by term. `expected_loss` multiplies the physical default probability by one minus recovery. `mtm_drag` multiplies a duration by an expected yield or spread change over the horizon and divides by the horizon, so a 50 bp rise over five years costs a 3.2-duration sector 32 bp a year. `forward_return` subtracts those drags from the yield. Spread duration drives the spread term and modified duration drives the rates term, which is why loans, CLOs and direct lending carry a quarter-year of rate duration and three to four years of spread duration. The outputs are `MU`, the forward return by sector (3.62% for HY corporates and 6.53% for CLO BBB to B on these inputs), and `DTS`, spread duration times spread, which Block 3 uses to scale risk.

The asserts are the acceptance tests. Feeding the function Nuveen's own HY inputs must return 3.56%. The six portfolios of Figure 6 must each imply a cash rate between 3.60% and 3.75% when computed as return minus Sharpe times volatility, which checks that the vendor's table is at least consistent with itself. The CCC break-even must come out near 19.7%, and a spread duration of two at 200 bp must carry the same DTS as four at 100 bp.

Use it as the front door for any sector-level forecast, and not where yields move in a clearly nonlinear path: `mtm_drag` is the plain $D\Delta/h$ of Nuveen's identity and leaves out the reinvestment offset of §12.2, so it overstates the drag a little. The edge case that bites is the unit guard. `_decimal` raises when any magnitude exceeds 1.0, which catches 6.97 but waves through 0.75 typed for 75 bp, a perfectly legal 75% a year.

*The full listing is [Listing 12.1 in Appendix F](#code-12-1).*

Block 2 desmooths (§12.5). The planted profile $\theta = (0.5, 0.3, 0.2)$ has $\xi = 0.38$.

Here is the problem as Kaz meets it. The direct-lending sleeve reports a return every month, but the return is a sequence of appraisals: it moves a little, it moves late, and each month's change is correlated with the previous month's for reasons that have nothing to do with the economy. Mags would ask whether the number was measured by the fund or by the fund's lawyer. An optimizer fed that series concludes the sleeve is nearly riskless and buries the book in it. The cure of §12.5 is to estimate how much averaging the appraisals are doing and undo it. A desk automates the cure because it has to be re-run every quarter on every appraisal-marked series, and because the one way it fails, an unstable inverse, produces garbage that looks exactly like data.

The listing has four working parts. `acf` computes sample autocorrelations at lags one through k. `_ma_rho` computes the autocorrelations that a given weight vector would produce if the true returns were serially uncorrelated. `fit_smoothing` finds the weights that make the second match the first, searching over an unconstrained vector passed through `_softmax`, which forces the weights to be nonnegative and to sum to one, the Getmansky–Lo–Makarov constraints, so the search never has to enforce them. It returns the weights and $\xi=\sum_j\theta_j^2$, the share of true variance that survives in the reported series; reported volatility divided by $\sqrt{\xi}$ is the true volatility. `desmooth` inverts the averaging one period at a time: take the reported return, subtract the weighted true returns already recovered, divide by $\theta_0$. `ar1_profile` supplies the truncated geometric weights of the AR(1) smoothing model for when you would rather assume a persistence than estimate one.

The test is a planted-parameter test. It builds 6,000 months of true returns at 2% monthly volatility, smooths them with weights $(0.5, 0.3, 0.2)$, drops the first ten months as burn-in, and demands that the fit recover $\xi$ near 0.38 (it prints 0.379), recover the true volatility within 10%, reproduce the true series to $10^{-10}$ when handed the true weights, and give $\xi=(1-\phi)/(1+\phi)$ for the AR(1) profile.

Use it on a NAV series sampled at the frequency of the appraisals, with enough history to pin down k autocorrelations. Do not use it on a listed BDC's share price, which the market marks daily and which was never smoothed. The edge case that bites is the mirror image: a weight vector and its reverse have identical autocorrelations, but only one of them inverts stably. The decreasing starting point steers the search toward the invertible one, which is a heuristic and not a guarantee, so `desmooth` checks the roots of the weight polynomial and raises rather than return a series that explodes.

*The full listing is [Listing 12.2 in Appendix F](#code-12-2).*

Block 3 builds the DTS covariance, the smoothed view an optimizer would see, and a synthetic regime panel: 3,000 months, which is 250 years, longer than the HY market by about two centuries, because a planted-parameter test needs power that real history does not have.

A covariance matrix is the quietest way for an allocation engine to go wrong. Eleven sectors have 66 distinct covariances, a few years of monthly data supply roughly one effective observation per parameter, and an optimizer handed that sample matrix will find the noise and bet on it. The structural answer of §12.5 is to stop estimating eleven volatilities and estimate one covariance of relative spread changes instead, scale it by each sector's spread duration times spread, and shrink what remains toward a one-factor shape. A desk automates this because the matrix is rebuilt every month, and because somebody has to build, beside it, the matrix an optimizer would see for the appraisal-marked sleeve, so the investment committee can see for itself what the smoothing hides.

The listing does three jobs. First, `dts_cov` implements (12.3): the elementwise product of the outer product of `DTS` with $\Omega$, the covariance of relative spread changes, plus $\sigma_y^2$ times the outer product of modified durations for the Treasury factor. That rates block is the independent base case, $\rho_{y,s}=0$; the cross term and the per-regime $\rho_k$ of §12.5 are the extension, and the listing does not include them. The "true" $\Omega$ is built from per-sector volatilities and a one-factor correlation with loadings `B_LOAD`, and the yield volatility is 80 bp. Second, `smoothed_view` rewrites row and column $i$ the way a GLM-smoothed sector would report: covariances with every other sector are scaled by $\theta_0$ and the own variance by $\theta^\top\theta$. With the AR(1) profile at $\phi=0.8$ the direct-lending volatility prints 6.30% true against 2.10% reported. Third, it simulates the regime panel: a two-state Markov chain with persistence 0.95 and 0.80, a common spread factor whose mean and volatility switch with the state, sector loadings on that factor, and idiosyncratic noise that is also larger in stress. Monthly excess returns are the spread divided by 12 minus DTS times the relative spread change.

The estimator comes last. `ewma_cov` runs the recursion at $\lambda=0.97$, seeded with the first 24 months and assuming zero mean. `one_factor_target` builds the factor matrix from an equal-weighted market portfolio, keeping the sample diagonal. `lw_delta` computes the Ledoit–Wolf intensity with the diagonal-$\rho$ simplification flagged in §12.5. The final $\hat\Omega$ blends the EWMA with its target on the last 300 months, annualizes by 12, and goes back through `dts_cov` to give `SIGMA_HAT`. The asserts require the intensity to lie in $[0,1]$, the matrix to be positive semidefinite, and the DTS scaling to hold for the first sector's spread-only volatility.

The edge case that bites is the intensity itself. On this planted panel `delta` prints 1.000, the ceiling, because the data really are one-factor and the target is the truth. On a real panel an intensity pinned at 1 means the target is doing all the work, which is the cue to check the window length before trusting the matrix.

*The full listing is [Listing 12.3 in Appendix F](#code-12-3).*

Block 4 is the regime engine (§12.4): log-space forward–backward, EM, label alignment, and the mixture moments of (12.2).

Spreads do not wander; they lurch. Between January 22 and April 7, 2025, the HY OAS went from 259 bp to 461 bp (§12.9), and a covariance matrix estimated on the quiet months before it said nothing about the loud ones after. Ines would put it simply: the table changed, and your estimates were fitted to a different game. A regime model asks the one question an allocator can act on, which state are we in right now, and it has to answer using only what had printed by today. The desk automates this because the answer is a probability that must be updated after every print, and because the arithmetic fails silently, with eleven-dimensional densities rounding to zero and the likelihood quietly turning into nonsense.

`mvn_logpdf` evaluates a multivariate normal log density through a Cholesky factor, which gives the quadratic form and the log determinant in one pass. `forward_backward` takes a T-by-2 array of log densities and subtracts each row's maximum before exponentiating, the underflow guard. Its forward pass is the filter: the filtered probabilities $\xi_{t\mid t}$ use data to date and nothing later. Its backward pass produces the smoothed probabilities $\gamma_t$, which use the whole sample, and the expected transition counts; it also returns the log-likelihood, with the shifts added back. `hmm2_em` is the fit. It starts from the worst 20% of months by cross-sectional average return, then alternates weighted means and covariances (with a $10^{-10}$ ridge) with a forward-backward pass, updates the transition matrix from the expected counts, and stops when the likelihood gain falls below tolerance. States are then sorted by average mean return so that label 0 is calm. `stationary` solves $\pi P=\pi$ by least squares. `regime_cma` is (12.2): it rolls the current state probabilities forward, averages them over the horizon, and returns the mixture mean and the mixture covariance, which is the probability-weighted regime covariances plus the spread of regime means around the mixture mean.

The asserts require the fitted diagonal of $P$ to sit within 0.05 of the planted one and filtered accuracy above 85%. It prints 98.2% filtered against 99.0% smoothed; the gap is the price of lateness, and only the filtered number is available to a trader. The fitted durations print as 21.9 and 5.7 months. Starting from stress with a 12-month horizon, the mixture still gives stress only 43% of the weight, because stress lasts under six months. At a 600-month horizon the weights must match the stationary distribution to within two points.

Use filtered probabilities for decisions and smoothed ones for research. The edge case that bites is labeling. Sorting by mean return works when regimes differ in mean, as they do here, but when they differ mainly in dispersion, as in the CCC story of §12.9, the means can sit close together and the labels can flip between fits. The 20% start also happens to equal the planted stress share, which real data will not oblige. And a state that claims fewer months than there are sectors has a covariance the ridge keeps invertible but cannot make meaningful.

*The full listing is [Listing 12.4 in Appendix F](#code-12-4).*

Block 5 is the optimizers (§12.6–12.8): tangency and ERC unit tests, the flat frontier, Kaz's allocation on reported versus desmoothed risk, the tiered strategic allocation with shadow prices, and the tactical tilt.

Everything so far produced inputs. The allocation is where inputs meet constraints, and where a desk discovers that the constraints make more of the decisions than the inputs do. Ines would say you cannot size a bet until you know what you are allowed to lose and how fast you can leave the table. The same problem has to be solved over and over: under reported risk and under desmoothed risk, under a 15% illiquid cap and under 16%, in calm and in stress. The desk automates it because a committee that asks "what if" expects the answer before the coffee cools, and because every answer must be checked against every constraint, every time.

The listing is a toolbox with one workhorse. `feasible_start` builds a point satisfying the budget and the bounds and refuses if the bounds cannot sum to one. `max_sharpe` and `min_var` wrap SLSQP with analytic gradients; `max_return_under_bounds` fills the highest-return sectors to their caps, which is the exact answer to a linear problem; `frontier` spaces six return targets from the minimum-variance return to 95% of the way to that maximum. `optimize_erc` solves the risk-budget problem by Newton's method with a backtracking line search on $\tfrac12 y^\top\Sigma y-b^\top\ln y$. `risk_contrib`, `beta_variance_share` and `utility` are one-liners the tests lean on.

`optimize_tiered` is the engine. It maximizes $w^\top\mu-\tfrac{\gamma}{2}w^\top\Sigma w$ subject to full investment, the bounds, the 15% illiquid cap, a 35% floor on highly and moderately liquid sectors, and a days-to-liquidate budget of 32, the constraint set of (12.4). Given a reference portfolio and a tilt budget, it adds a buy and a sell variable per sector, caps their total at the budget, and charges half the round-trip LCS on each unit traded. The script then runs the checks: tangency against the closed form, ERC to $10^{-8}$, and the beta share at 0.5. It prints the flat frontier, with Sharpe ratios from 0.21 to 0.35. It repeats Kaz's allocation on reported and desmoothed risk, where the reported-risk book pins direct lending at its 35% bound, claims 3.02% volatility and carries 4.56%. It takes shadow prices of the cap and the HY floor by finite difference, relaxing each by one point of NAV. Finally it applies the tactical tilt, using the annualized difference between the stress-mixture and stationary means as the overlay.

The edge case that bites is that SLSQP does not promise feasibility and the result's success flag is not evidence. Hence the asserts: sums, bounds, caps and the liquid floor are re-checked directly on the weights. Two smaller traps travel with it. The finite-difference prices are one-point steps, not derivatives, and can straddle a change in which constraint binds. And a 10% $\ell_1$ tilt budget lets only 5% of NAV change hands, five out and five in.

*The full listing is [Listing 12.5 in Appendix F](#code-12-5).*

Two notes on reading the output. The asserts check what is a theorem or a tolerance: the frontier's volatility rises with its target, the reported-risk portfolio is riskier than it claims, relaxing a constraint cannot reduce utility, and the caps hold. The *weights* are printed rather than asserted, because they depend on illustrative inputs. The useful exercise is to change one expected-loss assumption by 25 bp and watch how far they move (§12.6).

## 12.11 Desk Debrief

Friday afternoon. Kaz's direct-lending weight had fallen from the 35% bound to whatever the 15% cap and the days budget allowed. The PM's comment on the new spreadsheet said "Why?" Theo answered it with three numbers, and none of them was a yield.

- **The forward return is an identity with two measures in it.** Yield is a market ($\mathbb{Q}$-flavored) quantity; the loss term must be physical. A CDS-implied default probability in the loss term forecasts a zero risk premium by construction.
- **Expected credit loss is the restructuring banker's variable.** Set recovery by the seat in the waterfall (about 33% for direct loans, 52% for syndicated loans, 39% for HY bonds per FEDS 2024), not by a rating table. A 33% recovery has a 40% larger loss given default than a 52% one.
- **Rank sectors by spread per unit of something.** Break-even default $s/(1-R)$, carry per unit of DTS risk $(1 - \text{EL}/s)/(D^{\text{spr}}\sigma(\Delta s/s))$, and spread net of LCS. A wider spread is a bigger bet, not a better one.
- **Composition moves the mean, not the tail.** The HY index went from 37% BB to 51–54% BB. Z-scores against raw history mostly measure that change. Use fixed-mix spreads and bucket-level models.
- **Desmooth before you optimize.** $\sigma_{\text{true}} = \sigma_{\text{reported}}/\sqrt{\sum_j\theta_j^2}$; contemporaneous beta is understated by $\theta_0$. At AR(1) $\phi = 0.8$, volatility is understated threefold and beta fivefold.
- **The frontier is flat by the mediant inequality.** Long-only credit Sharpe ratios are weighted averages of sectors' systematic Sharpes. When the optimizer's choice sits inside the error bars, the constraints, not the objective, decide the allocation.
- **Liquidity tiers bind first.** The 15% illiquid cap, the liquid-sleeve minimum and the days-to-liquidate budget are known exactly; expected returns are not. Report shadow prices, and remember that a 5% quarterly gate is a queue position.
- **Regimes size the tilt; valuation directs it.** Trade on filtered probabilities with a delay, never smoothed ones. Expect the filter to be a month late into stress and a month late out of it, as in April 2025.

### The Spec You Hand the Robot

```text
ROBO: build mac_engine, a multi-asset credit allocator. Implement exactly this; where anything is
unspecified, stop and ask. Do not guess.

INPUTS (decimals per year; durations in years; point-in-time)
  sectors[n]: yld (yield-to-worst EX-DISTRESSED: drop constituents priced < 50, model them separately),
              pd (PHYSICAL annual default rate; never CDS-implied), rec (by seat in the waterfall),
              dmod, dspr (OAS duration for callables), spread, dspread_h (expected change over horizon),
              tier in {HL, ML, LL, IL} (Rule 22e-4 style), days (to liquidate), lcs_bp (round trip),
              w_min, w_max, smoothed (bool: appraisal-marked series?)
  R[T,n] monthly excess returns at bucket level (BB, B, CCC split); U[T,n] relative spread changes
  h horizon (years), cash rate, gamma (risk aversion)
PIPELINE
  1 mu_i = yld - pd*(1-rec) - dmod*d_rates/h - dspr*dspread_h/h   (eq. 12.1; raise on percent inputs)
  2 smoothed series: fit GLM theta (k=2, theta>=0, sum 1, invertible or REFUSE); vol /= sqrt(sum theta^2);
    covariances with others /= theta_0 (i.e. use the true-risk view, never the reported one)
  3 Omega = EWMA(U, lam chosen by out-of-sample likelihood), shrink to one-factor target (LW delta);
    Sigma = diag(DTS) Omega diag(DTS) + sig_y^2 dmod dmod'; assert min eigenvalue >= -1e-10
    (base case rho_ys = 0; total-return extension adds rho_k cross term inside each Sigma_k, section 12.5)
  4 HMM: K=2, full covariance, log-space forward-backward, EM; align labels (state 0 = higher mean);
    act on FILTERED probabilities with a one-month delay; never use smoothed ones in a backtest
  5 regime CMA: horizon-averaged mixture (eq. 12.2); overlay = mixture mean - stationary mean
  6 SAA: max w'mu - gamma/2 w'Sigma w  s.t. sum w = 1, w_min <= w <= w_max, sum_IL w <= 0.15,
    sum_{HL,ML} w >= liquid_min, w'days <= tau_max; report shadow prices of every binding constraint
  7 TAA: same, plus ||w - w_saa||_1 <= kappa via split variables, cost sum |dw| * lcs/2;
    kappa shrinks as the filtered stress probability rises
  8 single-issuer DTS share <= cap; report top-5 issuer yield contribution per sector
ACCEPTANCE TESTS: the asserts in Section 12.10, plus: every constraint re-checked after the solver
returns; weights printed with and without desmoothing; a 25bp perturbation to any el moves no
weight by more than the stated tolerance or the run is flagged "fragile".
```

### Exercises

1. **Read the chart.** Nuveen's Figure 3 prints 6.97, 2.55, 0.37, 0.49 and 3.56. Compute the default rate implied by each possible assignment of 2.55 and 0.49 to expected credit loss at 40% recovery. Which assignment survives? What would you need from the PDF itself to settle it without economics?
2. **The appraisal discount.** A perpetual BDC reports quarterly NAV returns with volatility 1.8% annualized and a lag-1 autocorrelation of 0.6. Under AR(1) smoothing, compute $\xi$, the true volatility and the factor by which its contemporaneous HY beta is understated. Then explain to the valuation committee, politely, why the annualization was the problem and not the arithmetic.
3. **Kaz's typo.** Kaz's HMM has $P_{11} = 0.97$ and $P_{22} = 0.10$. Compute the expected duration of each regime and the stationary distribution. Show that a filter acting with a one-month delay cannot, on average, act on this stress state at all. Then propose a reparameterization (weekly data, or a prior on $P_{22}$) and say what it costs.
4. **Two-asset ERC.** Show that for $n = 2$ the equal-risk-contribution weights are $w_i \propto 1/\sigma_i$ for any correlation. Apply this to HY (DTS 0.096) and CLO BBB to B (DTS 0.22) at a common $\sigma(\Delta s/s)$, and compare with 50/50 market-value weights.
5. **The gate as a queue.** A BDC has a 5% quarterly gate. Redemption requests are 15% of NAV this quarter and will be 10% of the remaining NAV in each later quarter. How many quarters until an investor who requested a full exit this quarter is fully paid, assuming pro-rata fills? What days-to-liquidate $\tau$ should the optimizer use, and why is a constant the wrong answer?
6. **ROBO literalism.** You tell ROBO to "minimize the number of regime switches the model reports." What does it build, and which single line in the spec above prevents it?

### Deep-Dive Resource Graph

**Podcasts**

- **Hedge Fund Andromeda Warns of 'Titanic' Debt Disaster as Yields Soar** (*The Credit Edge*, Bloomberg Intelligence, guest Alberto Gallo, Andromeda Capital, 10 Sep 2026). High government yields as a threat to corporate debt ("let long-term yields go up ... or let the currency depreciate"), AI borrowing and private-credit contagion: the macro-regime input to the tactical overlay of §12.8. https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/hedge-fund-andromeda-warns-of-titanic-debt-disaster-as-yields-soar
- **Dan Ivascyn Is Excited About a New Era in Fixed Income** (*Odd Lots*, Bloomberg, guest Dan Ivascyn, Pimco CIO, 8 Dec 2025). The discretionary multi-sector allocator's view: yield is back, with worries about data-center financing and "dangerous" inflated credit ratings; the contrast case for the framework's verdicts in §12.9. https://omny.fm/shows/odd-lots/dan-ivascyn-is-excited-about-a-new-era-in-fixed-income
- **EP 28 | BDC Trust Gap, Carl's Jr. Collapse & The Pitt** (*The Octus Download*, guest Mark Fischer, head of financial research, Octus, 22 Apr 2026). The "first genuine stress test" for semi-liquid private credit: floating-rate loans repricing into distress, BDC marks on the same asset 40 points apart by holder, and a technology BDC facing repurchase requests on 40% of shares against a 5% limit (the episode's own numbers). The gate as a queue, for §12.7 and Case Study B. https://share.transistor.fm/s/b845e0e3
- **Boaz Weinstein** (*Money Stuff: The Podcast*, hosts Matt Levine and Katie Greifeld, guest Boaz Weinstein, Saba Capital, 19 Mar 2026). Tenders for semi-liquid funds, reflexivity, private-credit NAVs and "volatility laundering": the trader's version of the appraisal smoothing in §12.5 and the redemption cycle in Case Study B. https://omny.fm/shows/money-stuff-the-podcast/boaz-weinstein
- **TCW Chops Credit Risk to Lowest in 30 Years as CCCs "Cry Uncle"** (*The Credit Edge*, Bloomberg Intelligence, guest Bryan Whalen, TCW CIO, 15 Oct 2026). CCC as "the weakest borrower, and they cry uncle first", then single-B, then double-B: a live quote for the CCC/BB split of Case Study C. https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/tcw-chops-credit-risk-to-lowest-in-30-years-as-cccs-cry-uncle

**Practitioner Writing**

- **Cockroaches in the Coal Mine** (Howard Marks, Oaktree memo, 6 Nov 2025). Marks on the recent string of well-publicised credit problems as a reminder of what the yield premium in sub-investment-grade credit is paid for; read it beside Case Study B and the "cockroach" remark cited below. https://www.oaktreecapital.com/insights/memo/cockroaches-in-the-coal-mine
- MacKay Shields, *High Yield 4Q 2025 Outlook* (October 2025): https://www.nylim.com/mackay-shields/insights/specialty-fixed-income-outlooks-4q25/high-yield-4q-2025-outlook
- Cambridge Associates, "Do the Recent Bankruptcies of First Brands and Tricolor Suggest Trouble Ahead in Private Credit?" (November 2025): https://www.cambridgeassociates.com/insight/do-the-recent-bankruptcies-of-first-brands-and-tricolor-suggest-trouble-ahead-in-private-credit/
- CNN Business, on the "cockroach" remark (October 16, 2025): https://abc17news.com/money/cnn-business-consumer/2025/10/16/why-jamie-dimon-is-warning-of-cockroaches-in-the-us-economy/
- Morningstar Indexes, on the Morningstar LSTA US Leveraged Loan Index (June 2024): https://indexes.morningstar.com/insights/analysis/blt17eb4431bd8a16bb/morningstar-lsta-us-leveraged-loan-index-highlights-a-growing-asset-class-popular-with-credit-investors
- Macquarie Asset Management, *Outlook 2026: Private Credit*: https://www.macquarie.com/at/en/about/company/macquarie-asset-management/insights/outlook/private-credit.html
- Pensions Age, on the Aeon Investments survey of MAC allocation plans (October 2023): https://www.pensionsage.com/pa/Nine-out-of-ten-investors-set-to-increase-allocations-to-multi-asset-credit-strategies.php
- On the shelf: Nuveen (Zheng), *Multi-asset credit investing: A quantitative framework* (pp. 2–9); Ben Dor et al., *Quantitative Credit Portfolio Management* (pp. 50, 63, 85, 111, 168, 177, 296); Dynkin et al., *Systematic Investing in Credit* (pp. 62, 67, 617); Paleologo, *Advanced Portfolio Management* (pp. 124, 149); Bolder (p. 524); Bohn and Stein (p. 492); BlackRock, *Systematic High Yield Credit* (p. 5); Blackstone, *Systematic Credit* (p. 1); Man Group 2022 (p. 26).

**Academic Papers**

- Ang and Bekaert (2002), *International Asset Allocation with Regime Shifts*, Review of Financial Studies 15(4): https://doi.org/10.1093/rfs/15.4.1137
- Guidolin and Timmermann (2007), *Asset Allocation under Multivariate Regime Switching*, Journal of Economic Dynamics and Control.
- Koijen, Moskowitz, Pedersen and Vrugt (2018), *Carry*, Journal of Financial Economics 127(2).
- Nystrup, Hansen, Madsen and Lindström (2015), *Regime-Based Versus Static Asset Allocation: Letting the Data Speak*, Journal of Portfolio Management 42(1); Nystrup, Madsen and Lindström (2018), Quantitative Finance (title not verified here).
- Bruder and Roncalli (2012), *Managing Risk Exposures Using the Risk Budgeting Approach*; Asness, Frazzini and Pedersen (2012), *Leverage Aversion and Risk Parity*, Financial Analysts Journal 68(1).
- Dimson (1979), *Risk Measurement When Shares Are Subject to Infrequent Trading*, Journal of Financial Economics.
- Books: Roncalli, *Introduction to Risk Parity and Budgeting* (2013); Ilmanen, *Expected Returns* (2011).

**Data & Code**

- FRED, ICE BofA OAS and total-return indices (HY, IG, BBB, BB, B, CCC, EM corporate, EM HY corporate, Euro HY), DGS10, DFF and VIXCLS: https://fred.stlouisfed.org/series/BAMLH0A3HYC
- Federal Reserve, *Financial Stability Report*: https://www.federalreserve.gov/publications/financial-stability-report.htm
- SEC Rule 22e-4: https://www.sec.gov/rules-regulations/2016/10/investment-company-liquidity-risk-management-programs ; text at https://www.law.cornell.edu/cfr/text/17/270.22e-4

<!-- STATUS: COMPLETE -->
