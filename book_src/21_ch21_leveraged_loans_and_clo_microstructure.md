# Chapter 21: Leveraged Loans, CLOs & Loan-Market Microstructure

Mags Dunleavy dropped a trade ticket on Theo's desk the way other people drop subpoenas. "Twenty-three business days," she said. "We bought seven million of a B2 term loan B on the eleventh of last month. It has not settled. The agent wants a \$3,500 transfer fee and our KYC packet. Again. Back in my day we settled these by fax, and the fax machine at least had the decency to jam where you could see it."

Theo read the ticket. Trade price 99.75. Settlement date: blank. "Delayed comp should have been running since T+7," he said. "Unless we didn't sign the assignment by T+5. Then it's our fault and nobody owes us anything."

Ines rolled her chair over. "Hand history, please. What is the position worth right now?"

"Easy," said Kaz, without looking up. "It's a floating-rate bond with a slightly odd call. Give me the curve and ten minutes."

"It's a loan," Theo said. "Nobody has a price. There's a mark. The mark is a composite of dealer quotes that may or may not include the dealer we bought it from. Nothing has printed since we traded, because nothing prints. There is no TRACE for loans."

"Then what do you use?"

"Whatever the CLOs are doing," said Mags.

A headline crossed all four screens: well over half the loan index bid above par, January repricing launches at a record pace, three more launched before lunch.

Kaz frowned. "If everything is above par, why does everyone look unhappy?"

"Because above par," said Ines, "is where the borrower takes chips off the table. A loan at 100.5 is about to be handed back to you at 100 with fifty basis points less coupon. You are long a bond and short its upside. And two-thirds of the players at this table use house rules that tell them exactly when they must fold."

Theo took the USB stick with his 13-week cash flow model out of his pocket, looked at it, and put it back. This one was going to need a different model.

The question this chapter answers: **who sets the price of a leveraged loan when two-thirds of its holders cannot freely choose what they buy, the borrower can call it at par, and the trade settles in three weeks?**

By the end of this chapter you will be able to:

- price a loan as a credit-risky floater that is short a par call;
- compute a CLO's overcollateralization (OC) test with its CCC, defaulted and discount haircuts, and derive the cure trade a manager is pushed into;
- size a loan fund's liquidity buffer as a queue whose service time is the settlement cycle;
- build a CLO Forced-Sale Pressure Index and a repricing-hazard carry signal;
- correct stale loan marks before you mistake smoothing for momentum;
- read a CLO indenture the way you used to read a credit agreement, because the indenture now decides who is a forced seller under the credit agreement.

The PJT bridge in one line: at RSSG you asked, "What does the credit agreement say?" Here you also ask, "What does the *CLO indenture* say?"

## 21.1 The Leveraged Loan as an Instrument: A Floater That Is Short a Call

At RSSG the term loan B was the top of the capital structure: first lien, secured, the tranche whose recovery you fought over and whose lenders you organized. That view is right in distress. For the large majority of loans on the large majority of days, when nobody is distressed, it misses where the price comes from. A performing leveraged loan's price is set by three things that are not financial covenants. (There usually aren't any: more than 90% of the index is covenant-lite.) The three things are a floating coupon, a borrower call at par, and a holder base dominated by vehicles that follow rules.

The instrument, as a desk sees it:

- **Coupon.** Term SOFR plus a margin $m$, reset monthly or quarterly. Legacy loans converted from LIBOR may carry a credit spread adjustment (CSA). Many loans have a base-rate floor. Interest accrues ACT/360.
- **Security and covenants.** First-lien senior secured. Covenant-lite: no maintenance tests for the term loan. The revolver may keep a springing leverage test.
- **Amortization.** Roughly 1% per year, with a bullet at maturity *(typical; check the agreement)*.
- **Call.** Prepayable at par at any time, except that a "101 soft call" usually applies for six months after closing or after a repricing. During that window, a *repricing* transaction (not every prepayment) costs the borrower one point.
- **Transfer.** Assignment, not a book-entry transfer. It needs the agent's consent, often the borrower's consent (frequently deemed given after a set number of days), a check against the disqualified-lender list, and an entry in the agent's register. This is the root cause of §21.2.
- **Legal status.** Not a security. In *Kirschner v. J.P. Morgan Chase Bank, N.A.* (2d Cir., 24 August 2023), the court held that syndicated term loans are not securities under the *Reves* test. So no T+1 mandate, no DTC settlement, and no securities-law disclosure regime are coming to rescue the plumbing.

Kaz read the list twice and asked whether "soft call" meant the borrower phones the lenders and asks nicely. It means something close to that. The borrower's arranger phones the lenders, tells them the new margin, and lets anyone who objects be taken out at par.

### 21.1.1 Derivation: carry, price, and the two durations

Let $b_t$ be the base rate (term SOFR) and $m$ the contractual margin, both decimals per year. Quote the price $P_t$ in points per 100 of par. Over an accrual period of length $\Delta$ (ACT/360, so $\Delta = \text{days}/360$), the holding-period return splits into two parts:

$$
r_{t,t+\Delta} \;=\; \underbrace{\frac{100\,(b_t + m)\,\Delta}{P_t}}_{\text{interest (carry)}} \;+\; \underbrace{\frac{P_{t+\Delta} - P_t}{P_t}}_{\text{market value}} . \tag{21.1}
$$

The index providers publish exactly this split. Here is why it matters. In 2022 the Morningstar LSTA US Leveraged Loan Index returned **−0.6%**, while US high yield lost more than 11%. The market-value component was **−6.2%**, the worst since 2008. The interest component made up the difference: about +5.6% by subtraction, and a monthly interest return that rose to a two-decade high of 0.73% *(Morningstar Indexes; LSTA citing Citi Research)*. Rising rates destroyed bond prices and *raised* loan coupons. A loan's return is mostly carry. Price is a bounded nuisance until it isn't.

Next, value the loan ignoring the call. Under a recovery-of-market-value convention, a credit-risky floater that pays exactly $b + s$ and is discounted at $b + s$ is worth par at every reset date. Here $s$ is the spread the market currently requires, called the discount margin. This is the standard reset argument: on a reset date the next coupon is set to the then-current rate, so the remaining cash flows are worth par, and by backward induction so is the whole note. Our loan pays $b + m = (b + s) + (m - s)$, so it is worth par plus an annuity of the margin difference. With expected life $T$ (a common quoting convention assumes a three-year life) and discount rate $y = b + s$ taken as flat:

$$
P^{\text{nc}} \;=\; 100\left[\,1 + (m - s)\,a(T;y)\right], \qquad a(T;y) = \int_0^T e^{-yu}\,du = \frac{1 - e^{-yT}}{y}. \tag{21.2}
$$

Two durations follow immediately. The **rate duration** is the time to the next reset, at most $\tfrac{1}{12}$ or $\tfrac14$ of a year, because the coupon re-fixes and the $b$ terms cancel. The **spread duration** comes from differentiating (21.2) with respect to $s$, holding $a$ fixed to first order:

$$
D^{\text{spr}} \;=\; -\frac{1}{P}\frac{\partial P}{\partial s} \;\approx\; \frac{100\,a(T;y)}{P}.
$$

With $T = 3$ and $y = 7.5\%$, $a = (1 - e^{-0.225})/0.075 \approx 2.69$, so a loan at par has a spread duration of about 2.7 years and a rate duration of about 0.1. It is a bond for credit and a money-market fund for rates. That combination is why allocators hold it.

Now add the call. If $s$ falls below $m$, (21.2) says the loan should trade above par. But the borrower can prepay at par (or at 101 inside the soft call) and refinance at $s$. So the upside of (21.2) belongs to the borrower, and the price is capped:

$$
P_t \;\lesssim\; \min\!\left(P^{\text{nc}}_t,\; K_t + \epsilon_t\right), \qquad K_t \in \{100, 101\},
$$

where $\epsilon_t$ is the small premium that survives because exercise is not instantaneous (§21.5 derives it). On the way down the loan has the full 2.7 years of spread duration. On the way up it has almost none. **A par loan is a short call struck at 100.** Its return distribution is left-skewed by construction, and §21.7 shows what that does to momentum.

> **[SOURCE EXTRACTION]** *Nuveen_Multi_Asset_Credit_Quant_Framework p.9:* Leveraged loans are benchmarked to the "S&P UBS Leveraged Loan Index (Formerly Credit Suisse Leveraged Loan Index)," and private credit is proxied by the "S&P UBS Leveraged Loan B Index."
>
> **Annotation.** This is how an allocator sees the sleeve: an index return series with an allocation band. On p.6 the same framework constrains leveraged loans to 5–25% of a multi-asset credit portfolio and CLO BBB–B to 0–10%. Using single-B loans as a proxy for private credit is a joke that teaches. Both markets now refinance each other (more than \$30bn moved each way in 2025, per William Blair's Q4-2025 newsletter), so the proxy is better than it looks. But a monthly index return hides the three things this chapter is about: a capped price, a holder base that sells by rule, and a settlement lag. Chapter 12's optimizer consumes these sleeves. This chapter supplies the inputs it should be fed: carry net of expected repricing loss, a forced-flow drawdown term, and a liquidity horizon set by settlement, not by the trading screen.

> **Trend Watch: from bank asset to CLO asset, 2018–2026.**
> *Size.* At end-2018, US CLOs outstanding were \$617bn, "approximately half of U.S. leveraged loans outstanding" (Fed FEDS Note, "Who Owns U.S. CLO Securities?", 2019). That implies a loan market of roughly \$1.2tn. By 2025:Q4, institutional leveraged loans were \$1,549bn, with 12.6% average annual growth since 2000, the fastest of any asset class in the Fed's table (Fed *Financial Stability Report*, 8 May 2026, Table 1.1).
> *Holders.* CLOs hold about two-thirds of outstandings and buy "nearly three-quarters" of new issue (Deutsche Bank Flow, 7 Oct 2025; approx.). Bank-loan mutual funds shrank 21% to \$71bn over 2019–2025, and their median liquidity ratio fell from about 10% (2021) to about 4.5% (Fed FEDS Note, 19 Aug 2026).
> *Coupon.* USD LIBOR panels ended on 30 June 2023. The ARRC's fallback CSAs were 11.448/26.161/42.826 bp (1m/3m/6m), but loan practice often used a "10/15/25" curve or a flat 10 bp, and the 2024–2025 repricing wave stripped many CSAs entirely (law-firm surveys; approx.).
> *Recycling, not growth.* In 2025 gross loan issuance of about \$400bn produced only about \$106bn of net new loans against \$294bn of repayments (Eagle Point Income Co, Form N-CSR FY2025).
> *What it means for the desk.* The marginal buyer of a performing loan is a rule-bound vehicle. Model its rulebook before you model the borrower.

## 21.2 Plumbing: Settlement, Marks, and the Arrival of E-Trading

"In bonds," Ines told Theo, "the hand history is TRACE. In loans, the hand history is a rumor someone told a pricing service." Every systematic idea in this chapter has to survive that sentence.

**Marks, not prints.** No public trade tape exists for loans. Prices come from dealer-quote composites (LSTA/LSEG mark-to-market, IHS Markit, now S&P Global). A composite is an average of indications that may be stale, may cluster, and may include the dealer who is your counterparty. In June 2025 the average LSTA/LSEG bid-ask was **72 bp**, the median **50 bp**, and both were flat year on year. The average trade level was 97.2 and the median 99.6. Turnover, annual volume divided by average outstandings, reached **65%** over the trailing twelve months, a five-year best equal to 2020 *(LSTA, "2Q25 Secondary Trading Monthly Executive Summary," 24 Jul 2025)*. Compare that to a TRACE-eligible bond: a print within fifteen minutes, a public tape, and a T+1 settlement.

> **[SOURCE EXTRACTION]** *Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.41:* "funds targeting opportunities in leveraged loans and, particularly, convertible bonds, where we see the potential for significant alpha. While loans and other private credit instruments are obviously problematic from a data availability perspective at present... Already both Refinitiv and IHS Markit are providing daily pricing on 6,500 loan facilities."
>
> **Annotation.** "Daily pricing" means daily *marks*. That distinction is the whole data problem. A daily mark built from quotes is a smoothed, partly stale estimate of an unobserved price, and its errors are autocorrelated. §21.7 shows that naive momentum on such marks partly rediscovers the smoother. The 2026 desk has two things Man did not have in 2022. The first is electronic venue data (Octaura's inquiry and trade flow, below), which adds real executable prints for a growing share of volume. The second is CLO trustee data (holdings, prices and test results by deal), which tells you who *must* trade before they do. The modern desk combines the three sources: composite marks for coverage, venue prints for truth where they exist, and trustee holdings for flow. It does not trust any one of them alone.

### 21.2.1 Settlement: the slowest thing in credit

> **[SOURCE EXTRACTION]** *Moyer_Distressed_Debt_Analysis p.322:* "For loans of healthy borrowers (referred to as the par loan market), the settlement convention typically is 10 days (T+10), but modest delays are common... The settlement convention in the distressed bank debt market is 30 days, but delays (sometimes of up to 120 days) are fairly common."
>
> **Annotation.** Moyer wrote this in 2004, when bonds settled T+3. Since then bonds went to T+2 (2017) and T+1 (28 May 2024). Loans moved their *convention* to T+7 for par and T+20 for distressed, but barely moved their *reality*. Moyer's page also notes an agent transfer fee of "\$2500–\$5000" and that loan holders can be identified from amendment signature pages. Both are still true, and the second is why holder-base modeling (§21.8) is possible. The modern departure is legal: after *Kirschner*, nothing forces loans onto securities rails. The ledger stays with the agent bank, and every trade is an assignment with consents.

Why is it slow? A par trade needs a confirmation, an assignment agreement, agent consent, borrower consent (or the passage of a deemed-consent period), KYC on the buyer, a disqualified-lender check, a funding memo, and an update to the agent's register. Each step involves a different party, and none of them is paid for speed. Over the decade to January 2025 the LSTA's own chart puts the average par settlement time at about **20 days** against the T+7 convention *(LSTA, April 2025 conference slides, via search; CHECK before print)*. Vendors describe averages "upwards of 20 days" for many firms. The LSTA's quarterly settlement studies with exact medians are members-only.

The one well-documented policy experiment is instructive. Before September 2016, delayed compensation (defined below) was paid to the buyer whether or not the buyer had done its paperwork. That meant a buyer could sit on an unsigned assignment and collect the loan's coupon, financed at the base rate, with no capital tied up. In effect the LSTA had written every buyer a free repo option. The delayed-compensation protocol (Phase I for trades from 1 September 2016, Phase II from 1 November 2016) made compensation "requirements-based." Under it, the buyer must execute the documents by T+5 and pick a settlement date of T+7 or earlier, or it loses compensation for the delay. Median par settlement fell from T+12 (January–August 2016) to T+9 (September 2016), and the share settling within T+7 rose from 23% to 37% *(Markets Media, 2 Nov 2016)*. When you take away a free option, people stop exercising it. This is the most reliable law in finance.

### 21.2.2 Derivation: delayed compensation is a forced repo

Let a buyer purchase par $n$ at price $P$ (points) on trade date $T$. The settlement date is the random variable $T + \ell$, measured in business days. In stylized form (the LSTA Standard Terms and Conditions govern the details), delayed compensation starts on day $T+7$ if the buyer has met its obligations. From then until settlement, the seller pays the buyer the interest accruing on the loan, and the buyer pays the seller a cost of carry on the purchase price at a benchmark rate, which we write as the base rate $b$. The net daily transfer to the buyer, for $u \in (T+7, T+\ell]$, is

$$
\text{DC}_u \;=\; \frac{n}{360}\left[(b_u + m) \;-\; b_u\,\frac{P}{100}\right].
$$

Read it as positions. From $T+7$ the buyer has the loan's full economics: price risk (which passed on trade date) plus coupon. It pays $b$ on the purchase price while its own cash, still undelivered, earns roughly $b$ in a money fund. The buyer therefore owns the loan, financed at $b$ flat. The seller still carries the loan on its balance sheet, funded at its own rate $f_S$, collects $b$ on the price, and passes the coupon through. Its daily cost is

$$
\text{cost}^{\text{seller}}_u \;=\; \frac{n\,P}{100 \cdot 360}\,\big(f_S - b_u\big) \;+\; \text{capital and operational charges}.
$$

So **every late loan trade is a short-dated repo that the seller is forced to provide at the base rate flat.** For a dealer funding at $b + 50$ bp, carrying \$10mm at 99 for 13 extra days costs about $10{,}000{,}000 \times 0.99 \times 0.005 \times 13/360 \approx$ \$1,800 *(illustrative)*. That is small per trade and large across a book with \$1tn of annual volume. The bigger costs are elsewhere. Counterparty exposure lives for $\ell$ days instead of one. A seller that needed *cash* (a loan fund meeting redemptions) does not get it for $\ell$ days, which is §21.6. And between $T$ and $T+7$ nobody compensates anybody, so the first week is a dead zone in which the buyer's cash and the seller's loan both sit idle.

For a pricing engine, $\ell$ is a distribution, not a constant. Model it by regime (par vs distressed), by agent bank, by whether borrower consent is required, and by calendar (quarter-ends and CLO effective dates congest the queue). A shifted negative binomial in business days is a reasonable first fit. Chapter 19's portfolio-trading engine should price a loan line with $\mathbb{E}[\ell]$ and its tail, not with T+1.

### 21.2.3 E-trading arrives, two decades late

Octaura, a dealer-backed platform that began life as "Project Octopus," launched loan trading in April 2023 with three dealers and 34 buy-side firms. By April 2026 it had about 30 dealers and more than 170 buy-side firms. Its share of LSTA-reported secondary volume went from 1% (April 2024) to 6.4% (July 2025) to 7.7% (January 2026). It reports a record \$19.6bn traded in Q1 2026 and its CFO says it exited June 2026 at 7.51% *(Octaura blog posts, 2025–2026; Pulse 2.0 interview, 29 Jul 2026; vendor-reported)*. It added a CLO platform in September 2025 and a "Live Feedback" auction protocol for CLO BWICs in February 2026. Separately, Versana, a consortium of agent banks, put amendment and consent voting on a live digital platform in October 2026. For Part IV readers that is the real headline: liability management transactions are consent games, and the consent machinery is now an API.

The inquiry tape is already a signal. In March 2025, 70% of Octaura inquiry was customer selling. In April it was balanced (55% sellers). By June, 72% was buying. In May 2025 the platform's estimated cost to sell fell from 23 cents to 9 cents, against 13 cents to buy *(Octaura, "On the Blotter: 2025 in review")*. A buy/sell imbalance that a venue publishes monthly is a crude flow factor, but it is a real, timestamped one, which is more than loans have ever had.

> **Trend Watch: settlement and e-trading, 2004–2026.**
> *Settlement.* T+10 par / T+30 distressed conventions with delays to 120 days (`Moyer_Distressed_Debt_Analysis p.322`, 2004) → median T+12 falling to T+9 after the September 2016 delayed-comp protocol (Markets Media, Nov 2016) → a ten-year average near 20 days to January 2025 (LSTA slides; CHECK). Over the same period bonds went T+3 → T+2 (2017) → T+1 (May 2024).
> *Volume.* Secondary loan trading was \$824bn in 2022 (then a record), \$821.4bn in 2024, and a record **\$971bn** in 2025. Trailing-twelve-month volume passed **\$1tn** in Q1 2026, then Q2 2026 fell back as volatility subsided (LSTA; size of the decline to be checked).
> *Electronification.* Octaura share 0% (April 2023) → 1% (April 2024) → 6.4% (July 2025) → about 7.5–7.7% (H1 2026), vendor-reported.
> *What it means.* Execution is getting faster while settlement is not. The gap between the two is a balance-sheet cost (the forced repo above) and a liquidity mismatch (§21.6), and both scale with turnover, which is at a record.

### Deep-Dive Resource Graph (21.2)

- **Practitioner Writing.** LSTA, "2Q25 Secondary Trading Monthly Executive Summary" (24 Jul 2025): https://www.lsta.org/content/lsta-secondary-trading-monthly-executive-summary-2q25-secondary-loan-trading-volumes-spike-again-to-a-record-262-billion/ · LSTA quarterly settlement-study index (members-only decks): https://www.lsta.org/content-category/quarterly-secondary-settlement-data-study/ · Markets Media, "LSTA's Delayed Comp Protocol Shows Encouraging Progress" (2016): https://www.marketsmedia.com/lstas-delayed-comp-protocol-shows-encouraging-progress-moves-phase-ii/ · Octaura, "On the Blotter: 2025 in review": https://news.octaura.com/on-the-blotter-2025-in-review · Simpson Thacher on *Kirschner* (25 Aug 2023): https://www.stblaw.com/about-us/publications/view/2023/08/25/second-circuit-holds-that-kirschner-syndicated-term-loans-are-not-securities
- **Data & Code.** Versana: https://www.versana.io/ · LSTA/LSEG and S&P Global loan pricing (commercial; no public API).

## 21.3 CLO Anatomy and the Arbitrage

Mags's definition: "A CLO is a bank that the rating agencies designed and the equity investors rent." It is a bankruptcy-remote special-purpose vehicle, usually Cayman-incorporated, with a trustee, a collateral manager, and an indenture. It buys about 200–400 broadly syndicated loans and funds them with a stack of floating-rate notes. A typical US broadly syndicated (BSL) CLO stack is AAA 60–63%, AA 10–13%, A 7–9%, BBB 4–6%, BB 4–6%, sometimes a sliver of single-B at 1–2%, and equity 8–10% *(Barings, "What is a CLO," June 2025; approx.)*. The AAA's subordination, which is its credit enhancement, is typically 35–40%. At issue the deal has a reinvestment period of roughly four to five years, during which the manager trades the pool, and a non-call period of about two years, after which the equity can refinance the notes.

The life cycle runs warehouse → pricing → ramp → effective date → reinvestment → amortization. The equity holds a call on the liabilities. It can *refinance* (reprice some tranches and keep the dates) or *reset* (reprice everything and extend the reinvestment period and maturity). That call has become the liability-side twin of the borrower's repricing call. US CLO new issuance set records of \$202bn in 2024 and \$209bn in 2025. Resets were \$223bn and \$232bn, and refinancings \$84bn and \$105bn *(Eagle Point Credit Co and Eagle Point Income Co, Forms N-CSR, FY2024 and FY2025)*. In H1 2026, new issue was only about 35% of roughly \$230bn of activity *(Dechert OnPoint, 4 Aug 2026; Eagle Point N-CSRS)*. JPMorgan, via Maples, called *net* new supply "near-anaemic." Most of the CLO market's activity is the same deals refinancing themselves, the way most of the loan market's activity is the same loans repricing themselves. It is turtles all the way down, and every turtle has a call option.

> **[SOURCE EXTRACTION]** *Bohn_Stein_Active_Credit_Portfolio_Management p.14:* In his June 2008 foreword Darrell Duffie wrote that "by mid-2008 the issuance of bank-loan collateralized loan obligations (CLOs) has fallen off significantly," and that CLOs are "well suited to transferring credit risk... to buy-and-hold investors who are less crucial to the provision of liquidity."
>
> **Annotation.** Both halves aged in interesting ways. The issuance collapse of 2008 became, by 2024–2025, back-to-back records above \$200bn a year. The "buy-and-hold" description survives as the most expensive half-truth in the asset class. A CLO's *liabilities* are held by buy-and-hold investors: banks, insurers and, since 2020, retail through AAA CLO ETFs (§21.6). Its *assets* are traded under a rulebook that turns rating changes into sales. A CLO is buy-and-hold until a rating agency moves. After that it is the most predictable seller in credit. That predictability is the alpha in §21.4.

### 21.3.1 Derivation: the arbitrage and its 11× gearing

Work per unit of collateral par. Let liability class $k = 1,\dots,K$ have size $w_k$ (as a fraction of collateral par) and spread $s_k$ over the base rate $b$. The equity is $w_E = 1 - \sum_k w_k$. The assets earn $b + \text{WAS}$, where WAS is the weighted-average spread. Annual fees are $f$ (senior and subordinated management fees plus administration), and expected annual credit loss is $\text{EL} = \text{PD} \cdot L$, with $L = 1 - R$. The equity's annual cash yield is what is left after paying the notes, divided by the equity's size:

$$
y_E \;=\; \frac{(b + \text{WAS}) - \sum_k w_k\,(b + s_k) - f - \text{EL}}{w_E}
\;=\; b \;+\; \frac{\text{WAS} - \sum_k w_k s_k - f - \text{EL}}{w_E}. \tag{21.3}
$$

The second equality uses $b\,(1 - \sum_k w_k) = b\,w_E$: the equity earns the base rate on its own slice, so CLO equity is a floating-rate instrument too. The gearing is

$$
\frac{\partial y_E}{\partial\, \text{WAS}} = \frac{1}{w_E} \approx 11 \quad (w_E = 9\%).
$$

So a 50 bp repricing across the pool takes about 5.6 points a year off the equity's yield. TwentyFour Asset Management put the same arithmetic in one sentence: "a 50 bp reduction in spreads means a potential 5% reduction in [CLO] equity returns." Every repricing wave in §21.5 is therefore a transfer from CLO equity to borrowers, levered 11×, and the equity's only defence is its own call on the liabilities.

Compare two vintages. Moyer's 2004 worked example uses collateral at 535 bp and investment-grade tranches (87% of the structure) at about 88 bp. The BB/B tranches are at 750 bp, which gives blended funding of about 110 bp and a net spread of about 425 bp to a 10% equity (`Moyer_Distressed_Debt_Analysis p.53–54`). Before fees and losses, that is about 42% a year on the equity, by our division. Now an illustrative 2025 deal. Take WAS = 319 bp, the index's nominal spread at year-end 2025 *(Loomis Sayles, "Loomis on Loans Q4 2025")*, and AAA at 130 bp (Eagle Point puts year-end AAA at 133 bp). Put AA at 175, A at 210, BBB at 310 and BB at 575 bp, with weights 62/11/8/5/5% *(mezzanine spreads illustrative)*. Then $\sum_k w_k s_k \approx 161$ bp, and the excess spread is about 158 bp. Subtract 45 bp of fees and 75 bp of expected loss *(illustrative)* and 38 bp remains, which is about 4.2% on a 9% equity, plus the base rate. The 2004 arbitrage paid for a lot of mistakes. The 2025 arbitrage pays for very few. That is why managers fight for every basis point of par build, buying loans at 97 rather than 100, and why the CCC haircut in §21.4 bites so hard.

> **[SOURCE EXTRACTION]** *Moyer_Distressed_Debt_Analysis p.53:* CDOs "frequently face purchase and sale pressures not driven by return maximization."
>
> **Annotation.** Moyer wrote this when CDOs held "over 20%" of the low-rated loan and bond market (p.55). The share is now about two-thirds of loans outstanding. The sentence has moved from a curiosity in a chapter on market participants to the first-order fact about loan price formation. The modern desk turns it into code. "Pressures not driven by return maximization" become a set of indicator functions on ratings and prices (the tests below), and each one is a predictable flow.

### 21.3.2 Derivation: why every CLO owns the same 200 names

Rating agencies require diversity, and Moody's measures it with the binomial expansion technique (BET). BET replaces a pool of correlated credits with a smaller number of *independent* credits that match the first two moments of the loss distribution. `Schmid_Credit_Risk_Pricing_Models p.183–184` gives the general formulas. Here is the homogeneous case, which is all the intuition needs. Take $J$ obligors, each with par $n_0$, default probability $P$ over the horizon, loss given default $L$, and pairwise default correlation $\rho$. The pool loss has mean and variance

$$
\mathbb{E}[\text{Loss}] = J n_0 L P, \qquad
\operatorname{Var}[\text{Loss}] = n_0^2 L^2 P(1-P)\,\big[J + J(J-1)\rho\big].
$$

The BET pool has $\text{DS}$ independent obligors with par $n_0 J/\text{DS}$ each, which preserves total par, so its mean is the same. Its variance is $(n_0 J/\text{DS})^2 L^2 P(1-P)\,\text{DS}$. Setting the two variances equal and solving gives

$$
\text{DS} \;=\; \frac{J}{1 + (J-1)\rho}. \tag{21.4}
$$

(Schmid calls this number the "diversity score of the collateral pool." We write it DS to keep $n$ free for par and $D$ free for duration.) With $J = 250$ and $\rho = 0.03$, $\text{DS} \approx 29.5$. As $J \to \infty$, $\text{DS} \to 1/\rho$. Adding names beyond about a hundred buys almost nothing, so managers meet the diversity test and then compete for the same large, liquid, B2/B-rated names that also satisfy the WARF (weighted-average rating factor) and WAS tests and can be sold if needed. The result is heavy overlap. Elkamhi and Nozawa's working-paper title said it plainly: "Too Big to Diversify." The test that makes each CLO diversified makes the CLO *sector* concentrated. When one large borrower is downgraded, it hits many CLO tests at once. §21.4 turns that correlation into a price.

## 21.4 The Tests as an Option Book

Theo, on day one: "At RSSG, CLOs were the lenders who couldn't fund the new money." Ines, on day two: "Here they're the players who must fold when the board shows a CCC. Learn which card makes which player fold, and you don't need to read faces."

> **[SOURCE EXTRACTION]** *Schmid_Credit_Risk_Pricing_Models p.175:* "There are two types of tests (so called coverage tests) that are intended as a warning if the cash flows from the collateral pool are running short to cover interest and/or principal payments to the tranches. If the coverage tests fail, the cash flows from the collateral are redirected. They are used to repay the outstandings on the tranches according to their seniority."
>
> **Annotation.** On p.176 Schmid gives the textbook OC ratio: collateral par divided by the par of the tranche and everything senior to it. He adds that the OC test "is done for every single tranche but the equity tranche." The 2026 indenture keeps the structure and changes the numerator. Par becomes *adjusted* par, with haircuts that depend on prices and ratings. Post-crisis US deals test a combined AAA/AA class and each class down to BB, usually with no test for a single-B tranche *(Creditflux CLO Guide, ch. 6)*. The modern departure is that the haircuts make a par test price-sensitive in exactly the tail of the portfolio where prices are least reliable.

### 21.4.1 Derivation: the adjusted numerator

Index the pool's loans by $j$, with par $n_j$ and price $p_j$ as a fraction of par. Define four disjoint sets: defaulted loans $\mathcal{D}$; discount obligations $\mathcal{O}$ (bought below a threshold, often 80–85, and carried at purchase price $p^0_j$ until the loan trades above about 90 for 30 days, per Kundu 2023); non-defaulted, non-discount CCC loans $\mathcal{C}$ (Caa1/CCC+ or below, deal-specific); and everything else. Let $n^{\text{nd}} = \sum_{j \notin \mathcal{D}} n_j$ be non-defaulted par and $\bar c$ the CCC limit (typically 7.5%; some deals use 5%). The CCC excess is

$$
X = \Big(\sum_{j \in \mathcal{C}} n_j - \bar c\, n^{\text{nd}}\Big)^{+}.
$$

Sort the CCC loans by price, $p_{(1)} \le p_{(2)} \le \cdots$. The **excess set** $\mathcal{X}$ is the cheapest loans whose par adds up to $X$ (the last one taken partially). Let $p^{\ast}$ be the price of the last loan taken, the *marginal* CCC. The adjusted collateral principal amount (ACPA), plus principal cash $\text{Cash}$, is

$$
\text{ACPA} = \sum_j n_j + \text{Cash}
\;-\; \underbrace{\sum_{j\in\mathcal{D}} n_j\big(1 - \min(p_j, R^{\text{ag}}_j)\big)}_{\text{defaulted}}
\;-\; \underbrace{\sum_{j\in\mathcal{O}} n_j\,(1 - p^0_j)}_{\text{discount}}
\;-\; \underbrace{\sum_{(k)\in\mathcal{X}} n_{(k)}\,(1 - p_{(k)})}_{\text{CCC excess}} , \tag{21.5}
$$

where $R^{\text{ag}}_j$ is the rating agency's assumed recovery. The OC ratio and cushion of class $k$, with note balances $B_l$ ordered from senior to junior and trigger $\underline{\text{OC}}_k$, are

$$
\text{OC}_k = \frac{\text{ACPA}}{\sum_{l \le k} B_l}, \qquad \kappa_k = \text{OC}_k - \underline{\text{OC}}_k .
$$

When $\kappa_k < 0$, interest that would have gone to classes junior to $k$, to the subordinated fees and to the equity is diverted to pay down the most senior notes until the test is cured. The interest diversion (reinvestment OC) test triggers earlier and diverts interest into *buying collateral*. That raises the numerator instead of shrinking the denominator. The IC test (interest proceeds after senior fees divided by interest due on the class and those senior to it) is computed similarly and "historically rarely failed" (Creditflux). Once a test fails, "maintain or improve" rules forbid trades that make it worse.

**Why it is an option book.** Write each haircut as a payoff on prices:

- *Defaulted:* $\min(p_j, R^{\text{ag}}_j) = R^{\text{ag}}_j - (R^{\text{ag}}_j - p_j)^{+}$. The CLO is short a put on each defaulted loan, struck at the agency recovery.
- *Discount:* the carrying value jumps from $p^0_j$ to 1 when the price stays above the threshold long enough. That is a barrier digital on par.
- *CCC excess:* minus the sum of $(1 - p)$ over the *lowest order statistics* of the CCC price vector. The CLO is short the cheapest tail of its own CCC book.

The price sensitivities follow directly from (21.5):

$$
\frac{\partial\,\text{ACPA}}{\partial p_j} \;=\; n_j\,\mathbf{1}\{j \in \mathcal{X}\} \;+\; n_j\,\mathbf{1}\{j \in \mathcal{D},\ p_j < R^{\text{ag}}_j\}, \qquad \text{and } 0 \text{ for every performing par loan}.
$$

The OC test cannot see the price of 90% of the book and is hypersensitive to the cheapest few percent. Now the **cliff**. Treat CCC par $C$ as the variable:

$$
\frac{\partial\,\text{ACPA}}{\partial C} \;=\;
\begin{cases}
0, & C < \bar c\, n^{\text{nd}} \quad \text{(bucket not full)},\\[2pt]
-(1 - p^{\ast}), & C > \bar c\, n^{\text{nd}} \quad \text{(bucket full)}.
\end{cases}
$$

A downgrade into a full bucket marks *some other loan*, the marginal cheap CCC, from par to market. Kundu (2023) finds the average CCC/Caa1 loan in CLOs priced at 85 cents but the cheapest CCC in each CLO at 58 cents on average. So the slope past the cliff is about $-0.42$: each dollar of fresh CCC beyond the bucket costs about 42 cents of numerator, *whatever the downgraded loan itself is worth*. Kaz, reading this, asked whether the cheapest loan had done anything wrong. It hadn't. It was standing at the edge of the cliff when someone else was pushed.

### 21.4.2 The cure-trade theorem

Suppose the bucket is full ($X > 0$). The manager sells par $\Delta n$ of a CCC loan $i$ at $p_i$ and buys a performing loan at par with the proceeds. Two things happen. The trade burns par of $(1 - p_i)\,\Delta n$, because cash $p_i \Delta n$ buys only $p_i \Delta n$ of new par. And the excess shrinks.

**Claim.** Let loan $i$ lie above the excess set ($p_i \ge p^{\ast}$), and let the trade be small enough that the excess stays positive. Then

$$
\Delta\text{ACPA} \;\ge\; \Delta n\,\Big[(p_i - p^{\ast}) \;-\; \bar c\,(1 - p^{\ast})(1 - p_i)\Big]. \tag{21.6}
$$

If instead $i$ lies inside the excess set, then $-\bar c\,(1 - p_i)\,\Delta n \le \Delta\text{ACPA} \le 0$.

**Proof.** *Case 1: $i$ above the excess set.* CCC par falls by $\Delta n$. Non-defaulted par falls by the par burn, so the bucket limit falls by $\bar c(1 - p_i)\Delta n$. The excess therefore falls by $\Delta n\,[1 - \bar c(1 - p_i)]$. The par leaving the excess set comes off its *top*: loans priced at or below $p^{\ast}$, each with haircut rate $(1 - p) \ge (1 - p^{\ast})$. So the CCC haircut falls by at least $(1 - p^{\ast})\,\Delta n\,[1 - \bar c(1 - p_i)]$. Subtract the par burn $(1 - p_i)\Delta n$ and rearrange to get (21.6).

*Case 2: $i$ inside the excess set.* Selling it realizes exactly the haircut it was already carrying: the par burn $(1-p_i)\Delta n$ equals the haircut removed. The only residual is the bucket-limit effect. The limit shrinks by $\bar c(1-p_i)\Delta n$, which pulls up to that much par back into the excess at haircut rates of at most 1. So $\Delta\text{ACPA} \in [-\bar c(1-p_i)\Delta n,\, 0]$. $\blacksquare$

Ignoring the small $\bar c$ term, the OC-optimal cure is to **sell the highest-priced CCC loan**. The gain per unit of par is $p_i - p^{\ast}$. Selling the cheap ones is OC-neutral at best: it just turns a haircut into a realized loss. Kundu calls this "contractual arbitrage." Notice what it means for the market. The highest-priced CCC in a CLO is usually the *freshly downgraded* one: yesterday a B− at 92, today a CCC+ at 88, still well above the 58-cent tail. So the theorem predicts exactly what Elkamhi and Nozawa (2022) measure. Constrained CLOs sell recently downgraded loans, those loans' prices fall temporarily, and because diversity rules make CLOs overlap (§21.3.2), the selling is correlated across deals. **The forced seller sells its best CCC, which is the one a fundamental buyer most wants.** The ex-RSSG reader knows that loan cold: a decent business, a bad quarter, a fresh downgrade, and a capital structure that is not yet a restructuring.

The magnitudes are large enough to trade. Elkamhi and Nozawa find that loans widely held by constrained CLOs earn 3.4% lower cumulative abnormal returns over the 20 weeks leading to the downgrade, and that the fire-sale price impact of CCC-downgraded loans is −3.35%. Over three months the unconditional probability that a CLO sells a downgraded loan is 13.27%. A one-standard-deviation (3.26%) drop in junior OC slack raises that probability by 1.56 pp. Average downgrade-week price impact was 17.31% in 2008–09, 1.26% in 2010–19 and 4.41% in 2020. Kundu (2023) finds that the median CLO operates within 4% of its most stringent covenant. After the 2014 oil-and-gas shock, she finds, each extra percentage point of a firm's CLO-routed oil-and-gas exposure lowered the secondary price of that firm's *unrelated* loan by 61 bp (IV estimates 81–254 bp). Selling \$1mm moved prices 180–404 bp on an Amihud measure. Loumioti and Vasvari (2019) add the manager's other lever: discretionary fair values and strategic trading around monthly tests. Strategic trading, but not fair-value discretion, predicts worse future CLO performance.

> **[SOURCE EXTRACTION]** *Moyer_Distressed_Debt_Analysis p.55:* "CDO-ORs typically limit the percentage of the CDO's portfolio that can be rated in the lowest rating categories. When an investment in the portfolio is downgraded to B– or CCC, the manager may be forced to sell something (again without regard to the portfolio manager's view of fair value) to remain in compliance with the CDO-ORs."
>
> **Annotation.** "Sell something" is the entire chapter in two words. Moyer's 2004 insight was qualitative: rating-based rules create involuntary selling, which a distressed investor should expect and exploit. Equation (21.6) makes it specific. The "something" is the highest-priced CCC, the timing is the next test date, and the size depends on the bucket's overshoot and the junior cushion. Two departures from 2004 matter. First, the rulebook is now haircut-based rather than a hard ban, so the pressure is graded, not binary. Second, the CLO share of the market went from about 20% to about 65%, so the forced seller is no longer a corner of the market. It is the market.

> **Desk Myth vs. Desk Reality.** *Myth:* "CLOs are buy-and-hold investors, so they stabilize the loan market." *Reality:* CLO *liabilities* are held by buy-and-hold investors. CLO *assets* are traded by a rulebook that turns a downgrade of one borrower into sales of that borrower and, through the cliff, of others. In 2020 BSL CLO exposure to CCC-range companies peaked at 12.31% (S&P, Apr 2023), against a 7.5% bucket. A stabilizer would not have needed a cure trade.

> **Poker Table.** "Most of poker is reading people," Ines said. "This isn't. When a CCC hits the board, the CLO with a 0.9% junior cushion must fold its best CCC hand before the next payment date. I don't need to read its face. I need its trustee report, and I need to know what it holds that is priced highest. The pot is the temporary discount, three points or so. The odds are the reversal rate. Who knows more than you? Nobody: the seller *told* you it was selling, in its indenture, years ago." Then the hand history, as always, through markouts. Buy on the downgrade week at the fire-sale discount. The markout is negative at day 1 because the other constrained CLOs are still selling, flat at week 2, and positive by week 8 if the reversal Elkamhi and Nozawa document arrives. *IDO or it didn't happen*: strip the loan's carry and its beta to the loan index before you call the week-8 markout alpha.

### 21.4.3 The CLO Forced-Sale Pressure Index

Let CLO $c$ hold par $n_{i,c}$ of loan $i$, whose outstanding amount is $O_i$. Let $\pi_{c,t}$ be the probability that CLO $c$ sells a downgraded holding within three months, given its junior cushion $\kappa^{\text{jr}}_{c,t}$ and its CCC excess $X_{c,t}$ as a fraction of par:

$$
\pi_{c,t} = \sigma\!\left(a - b_{\kappa}\,\kappa^{\text{jr}}_{c,t} + d\,\frac{X_{c,t}}{n^{\text{nd}}_{c,t}}\right), \qquad \sigma(z) = \frac{1}{1 + e^{-z}},
$$

$$
\text{FSPI}_{i,t} = \frac{1}{O_i}\sum_c n_{i,c}\,\pi_{c,t} \;\in\; [0,\ \text{CLO share of } i].
$$

FSPI is the expected fraction of loan $i$ that constrained CLOs will sell. It is Kundu's Bartik-style exposure (holder weights times holder constraints) turned into a live signal. Calibrate $a$ and $b_{\kappa}$ so that $\pi = 13.27\%$ at a 4% cushion and a one-SD (3.26%) drop in cushion adds 1.56 pp, matching Elkamhi and Nozawa. Because $\sigma'(z) = \sigma(1-\sigma)$, that requires $b_{\kappa} = (0.0156/0.0326)/[0.1327 \times 0.8673] \approx 4.16$ per unit of cushion. The CCC-excess loading $d$ is illustrative until you fit it on trustee data. The trade is liquidity provision: buy high-FSPI loans after CCC downgrades or LME rating events, conditional on a fundamental view, sized by the expected reversal, and exit as the reversal completes. Before month-end test dates, fade the relative price of the highest-priced CCCs in CLO-heavy names, because those are what constrained managers will sell.

> **Ways This Blows Up.** (1) *Stale trustee data.* Trustee reports are monthly and lag by weeks, so your cushion is last month's cushion. Nowcast it with the prices of the deal's CCC tail, which (21.5) says is all the numerator can see. (2) *Wrong "market value."* Each indenture defines market value: pricing-service bid, average of dealer bids, or, failing those, the manager's own estimate. If you use a composite mid, you are computing a different test from the one the trustee runs. (3) *Rating mapping.* The CCC classification may use the lower of two agencies' ratings, include B3/B− on negative watch, or treat a selective default differently. Parse the indenture. Do not guess. (4) *Discretion.* Loumioti and Vasvari show that managers move marks and trade strategically around tests. Your model of a deal can be right on the documents and wrong on the manager. (5) *Crowding.* If every desk runs the same FSPI, the reversal is bought before the forced sale completes, and the signal becomes a timing bet against other quants.

### Case Study: COVID-19 2020 and the 2022–2023 Junior-OC Failures

**March 2020.** The S&P/LSTA index's weighted-average bid fell from 95.18 on 29 February to 76.23 on 23 March. March's return was −12.4%, second only to October 2008's −13.2%. The distress ratio peaked at 57%. On 19 March the LSTA reported record volumes and bid-ask spreads that had "widened beyond 300 basis points" *(S&P Global LCD 1Q20 review; LSTA)*. The index rebounded to 82.9 by 31 March. Then the downgrades arrived, and the cliff did the rest. BSL CLO exposure to CCC-range companies peaked at 12.31% and the average junior OC cushion fell to 1.13% *(S&P Global Ratings, 28 Apr 2023)*. Elkamhi and Nozawa's 2020 downgrade-week price impact was 4.41%, more than three times the 2010–19 average. A systematic desk running FSPI in April 2020 would have seen pressure concentrated in recently downgraded, CLO-heavy names. By (21.6), those were exactly the highest-priced CCCs. The trade was to buy them from the forced sellers and hold through the reversal, sized against the risk that the downgrades kept coming.

**2022–2023: one deal, autopsied.** An April 2023 Academy Securities note counted 42 CLO deals failing their junior OC test, based on trustee reports. Cushions ranged from −3 bp (SRANC 2014-2A, just failing class E) to −104.7 bp (HLA 2012-1A, failing class C since August 2022) *(Academy Securities, "OC Triggers," 4 Apr 2023)*. Take ZAIS6 2017-1A. Its required OC ratios ran from 122.6% (class A/B) to 103.7% (class E). The class E ratio was 103.56%, a failure by 14 bp. The haircuts were: defaulted −\$13.5mm, deferring −\$0.12mm, discount zero, and excess CCC −\$5.0mm, for a total of 5.72% of aggregate principal. The notes were A-1-R \$146.6mm, A-2 \$25mm, B-R \$45mm, C-R \$30mm, D \$25mm and E \$25mm, so \$296.6mm in total. Now do the arithmetic the note invites (ours). A class E ratio of 103.56% implies an ACPA of about \$307.2mm. Total haircuts of about \$18.6mm at 5.72% imply aggregate principal of about \$325.5mm. Without haircuts the class E ratio would be about 109.7%, a six-point cushion. **The par was there. The option book failed the test.** The CCC excess alone was worth about 1.7 points of class E OC, and without it the deal would have passed at about 105.2%. ZCCP 2019-1A, another deal in the note, breached class E in February 2023 and cured the following month through cash diversion: the waterfall working exactly as Schmid's p.175 describes it.

### Specification for AI Implementation

**The Spec You Hand the Robot (OC engine).** *What ROBO built from the vague version ("cure the OC test"):* it sold the entire CCC bucket, cheapest first, because "cheapest" sounded like "least valuable." By (21.6) the first sales were OC-neutral: they turned haircuts into realized losses. Every sale after the bucket dropped below its limit simply burned par. On the synthetic deal below, ROBO took about \$10mm off the numerator and about two points off the junior OC ratio it had been asked to improve. It did exactly what it was told. The precise spec:

- **Inputs.** `pool`: one row per loan, with `par` (\$mm, ≥0), `price` (fraction of par, in (0, 1.2]), `is_ccc`, `is_default`, `agency_rec` (fraction), `is_discount`, `purchase_px` (fraction). `balances`: (K,) note balances, senior to junior, \$mm. `triggers`: (K,) required OC ratios as decimals. `cash`: principal cash, \$mm. `ccc_limit`: decimal (default 0.075).
- **Outputs.** ACPA and its three haircuts; CCC share, excess and marginal price $p^{\ast}$; OC ratios and cushions per class; for each candidate sale, $\Delta$ACPA from an exact recompute, never from the linearization.
- **Rules.** Excess is assigned cheapest-first. The haircut is $\max(0, 1-p)$ (no gains above par). Defaulted loans are excluded from both the CCC base and the CCC queue. Discount obligations are excluded from the CCC queue in this reference version. Real indentures apply the single most punitive treatment "without duplication," so implement the deal's actual priority.
- **Guards.** Raise on missing columns, negative par, or prices outside (0, 1.2]. Return NaN for $p^{\ast}$ when there is no excess. Never divide by a zero base.
- **Sanity checks.** With all flags off, ACPA equals total par (Schmid's textbook ratio). A downgrade below the limit changes nothing. A downgrade into a full bucket costs at most par × (1 − cheapest CCC price). Selling the richest CCC satisfies (21.6). Selling the cheapest lies in $[-\bar c(1-p)\Delta n, 0]$.

A specification is a promise about behavior, and a promise is worth what you can check it against. The one above tells ROBO what to build, but it leaves Theo with a practical problem that no careful reading of the indenture solves. The trustee reports the OC ratio once a month, weeks late, and says only where the deal stood. It cannot say where the deal stands at this morning's marks, what tomorrow's downgrade would do, or which CCC a manager should sell before the test date. Those are questions about a function, with prices and ratings going in and the adjusted numerator coming out, and the function has a cliff in the middle of it. Below the bucket limit another CCC costs nothing. Above it, another CCC costs forty-odd cents on the dollar, billed to a different loan. Theo's USB stick holds a 13-week cash flow model that is excellent at many things and has no concept of a bucket that charges you for someone else's downgrade. So the desk builds the engine once, as an answer key: a reference implementation that ROBO's output must reproduce to the penny before anything it writes touches a live deal.

Two functions carry the load. `ccc_excess_haircut` takes the CCC loans' par and prices plus the bucket size in dollars, floors the excess at zero, sorts the loans cheapest first, and takes par down the list until the excess is used up, charging each slice `max(0, 1 - price)` so nothing earns a gain above par. It returns the haircut, the excess and the marginal price $p^{\ast}$, or NaN when there is no excess. `acpa` wraps it. It refuses missing columns, negative par or prices outside (0, 1.2], then splits the pool into defaulted, discount and CCC loans: defaulted loans belong to neither of the other sets, and discount loans stay out of the CCC queue. Defaulted loans are carried at the lower of price and agency recovery, and the bucket is `ccc_limit` times non-defaulted par. It returns ACPA, the three haircuts, the excess, `p_marg` and the CCC share. `oc_test` divides ACPA by cumulative note balances and subtracts the triggers.

The rest is the answer key. `make_pool` builds a synthetic \$500mm deal of 250 loans at \$2mm: 21 CCCs priced evenly from 50 to 92, two defaults at 40, three discount obligations bought at 80. CCC par is \$42mm against a \$37.2mm limit, so the \$4.8mm excess swallows the three cheapest loans (the third in part) for a haircut near \$2.3mm. ACPA is about \$494.1mm and the junior class sits at 107.41% against a 104% trigger. The assertions replay the specification's sanity checks. With every flag off, ACPA equals par. The marginal CCC is the third cheapest. The bucket is flat below its limit and costly above it. And `sell_and_rebuy_par`, which sells at market and reinvests at par, confirms (21.6): selling the richest CCC adds about \$0.78mm, selling the cheapest loses about \$0.03mm.

Candidates are scored by full recompute, never by the linearization, which fails exactly where the cliff is. Use the engine to nowcast a cushion from today's marks, to rank cures, and to feed the pressure index below. Do not use it to replace the trustee: it applies one priority (defaulted, then discount, then CCC) and one limit, and your indenture may define market value, ratings and "without duplication" differently. The edge case that bites is the cliff. On the synthetic deal, downgrading a performing \$2mm loan priced at 97.7 into the full bucket costs about \$0.90mm of numerator, and none of it lands on the loan that was downgraded.

*The full listing is [Listing 21.1 in Appendix F](#code-21-1).*

The OC engine answers a question about a deal: how thin is this CLO's cushion this morning? The trade, though, is in a loan, and a loan sits in thirty or forty deals at once (§21.3.2), each with its own cushion and its own temper. Theo's instinct from RSSG is to ask who is in the lender group and how they will vote. The loan-level version asks what fraction of this loan is held by hands that must fold if the borrower is downgraded. That is a weighted sum over holders, and nobody wants to rebuild it in a spreadsheet for every name in the index each morning after the trustee files land. So it becomes a function: cushions and holdings in, one pressure number per loan out, ready to sort.

The top of the listing is calibration, written as named constants so the provenance stays visible. `P0` and `K0` pin the level: a 13.27% three-month sale probability at a 4% junior cushion. `DP_PER_SD` and `SD_K` pin the slope: 1.56 points for each 3.26-point drop in cushion. A logistic's slope is its coefficient times $\sigma(1-\sigma)$, so `B_FS` is the probability slope per unit of cushion divided by `P0 * (1 - P0)`, about 4.16, and `A_FS` is then solved so the curve passes exactly through `P0` at `K0`. `D_FS`, the loading on CCC excess, is illustrative, and the listing says so.

`sale_prob` is the logistic itself. It takes junior cushions and CCC excess as a fraction of par, both in decimals, floors the excess at zero so a deal inside its bucket feels no extra push, and returns one probability per CLO. `fspi` takes a (CLO by loan) matrix of par held and each loan's outstanding amount. It rejects a malformed matrix, or a loan that the CLOs together hold more of than exists. It multiplies the probability vector into the holdings matrix and divides by outstanding, which gives, for each loan, the expected fraction sold by constrained CLOs. That fraction cannot exceed the CLOs' share of the loan.

The tests check both calibration targets, then run 40 synthetic CLOs over 60 loans that are each 65% CLO-owned. Median FSPI is 9.4%. Thin every cushion by two points and raise every excess by one, and it becomes 11.0%, with every loan higher.

Use it conditionally. The probability describes a CLO that holds a *downgraded* loan, so the index measures pressure after a downgrade or an LME rating event, not a forecast for names nobody has touched. Fit `D_FS` on trustee data before sizing anything. The edge case that bites is units. A cushion typed as 3.8 instead of 0.038 goes through a coefficient of 4.16 and returns a probability of about zero, and a CCC excess typed as 1 for one percent saturates the curve at nearly one. Neither raises an error. Both look like a market that has made up its mind.

*The full listing is [Listing 21.2 in Appendix F](#code-21-2).*

### Deep-Dive Resource Graph (21.4)

- **Academic Papers.** Elkamhi, R. and Nozawa, Y. (2022), "Fire-Sale Risk in the Leveraged Loan Market," *Journal of Financial Economics* 146(3), 1120–1147: https://ideas.repec.org/a/eee/jfinec/v146y2022i3p1120-1147.html · Kundu, S. (2023), "The Externalities of Fire Sales: Evidence from Collateralized Loan Obligations," ESRB Working Paper No. 141: https://www.esrb.europa.eu/pub/pdf/wp/esrb.wp.141.en.pdf · Loumioti, M. and Vasvari, F. (2019), "Portfolio Performance Manipulation in Collateralized Loan Obligations," *Journal of Accounting and Economics* 67(2–3), 438–462 (accepted manuscript: https://lbsresearch.london.edu/id/eprint/1014) · Cordell, Roberts and Schwert, "CLO Performance" (*Journal of Finance*, 2023; check volume and pages).
- **Practitioner Writing.** Creditflux CLO Guide, ch. 6, "Understanding the Tests": https://cloguide.creditflux.com/6-understanding-the-tests · Academy Securities, "OC Triggers: Subtle Thresholds Come to the Fore as Collateral Distress Builds Up" (Apr 2023) · S&P Global Ratings, "Scenario Analysis: How Rising U.S. BSL CLO 'CCC' Baskets Could Affect Junior Overcollateralization Test Cushions" (28 Apr 2023).
- **Data & Code.** CLO trustee reports via commercial vendors (CLO-i/Creditflux, Intex, Octus); TRACE for CLO tranches; Elkamhi–Nozawa replication package (Mendeley Data).

## 21.5 Repricing Waves: The Borrower Exercises

"Upside in a loan," Ines said, "is a chip the borrower can take back whenever it likes, as long as it waits six months." A repricing is an amendment, not new money. The arranger proposes a lower margin, and often the removal of the legacy CSA. Lenders who consent keep the loan at the new coupon. Lenders who object are taken out at par, or at 101 inside the soft call. For a CLO the loan simply starts paying less, and by (21.3) the equity pays for it at 11×. In January 2025 banks were pitching repricings timed to soft-call expiries and offering to run them for free *(Bloomberg, 30 Jan 2025)*. The fee was not in the arranger fee. It was in the next deal.

### 21.5.1 Derivation: the price of a loan under a repricing hazard

Keep (21.2), but let the borrower reprice at a random time with intensity $h_t$ (per year) whenever the call is in the money ($m > s$). We use $h$ rather than $\lambda$ because $\lambda$ is reserved for default intensity in this book. At repricing the lender either receives par or keeps a loan paying the market margin $s$. Both are worth par, so after repricing nothing is left above par. Before repricing the lender earns the excess margin $m - s$. At time $u$ that excess is received with probability $e^{-hu}$ (no repricing yet) and is discounted by $e^{-yu}$. So, with constant $h$:

$$
P \;=\; 100\left[\,1 + (m - s)\int_0^T e^{-(y + h)u}\,du\right] \;=\; 100\left[\,1 + (m-s)\,a(T;\,y + h)\right], \qquad m > s. \tag{21.7}
$$

For $m \le s$ the call is out of the money and (21.2) applies with $a(T; y)$. Three consequences follow.

**The ceiling.** When $(y+h)T$ is large, $a(T;y+h) \approx 1/(y+h)$ and the premium over par is about $100(m - s)/(y + h)$. Take $m - s = 50$ bp, $y = 6.65\%$ and $T = 3$. With $h = 0$ (soft call in force, or no one bothers) the loan is worth 101.36. With $h = 1$ (a repricing expected within about a year) it is worth 100.45. With $h = 4$ (the window is open and arrangers are calling) it is worth 100.12. *That* is where the 100.5 ceiling comes from: it is the price at which the market expects a repricing within roughly a year. And 101 is the cap during the soft call, because the borrower would have to pay that point to exercise.

**Negative convexity, measured.** At par, the one-sided spread durations are

$$
D^{\text{spr}}_{\uparrow s} = a(T; y) \approx 2.72, \qquad D^{\text{spr}}_{\downarrow s} = a(T; y + h) \approx 0.25 \quad (h = 4).
$$

The loan loses 2.7 points per 100 bp of widening and gains about a quarter of a point per 100 bp of tightening. It is the bond you would design if you wanted to sell someone convexity and keep the premium.

**Expected carry loss.** Over a horizon $H$, the margin lost at time $u$ is $(m-s)$ if repricing has happened by $u$, which has probability $1 - e^{-hu}$. Averaging over $[0, H]$ gives the annualized expected give-up:

$$
\mathbb{E}[\text{carry lost}] \;=\; (m - s)\left[1 - \frac{1 - e^{-hH}}{hH}\right]. \tag{21.8}
$$

With $h = 4$ and $H = 1$, about 75% of the 50 bp excess margin, roughly 38 bp, is expected to disappear within the year. Quoted carry on an above-par loan in an open window is mostly fiction.

**The hazard itself.** Model repricing as a discrete-time hazard on loan-months. Fit a logit on PitchBook LCD repricing records with these features: price minus par (points); a soft-call-expired indicator and months since expiry; the market's share of loans bid above par, which is the window state; rating (BBs reprice first: 11 of 15 deals in May 2026 month to date were BB, per PitchBook LCD); sponsor ownership; and arranger activity. Treat margin $m$ and CSA as *separate* state variables, because a repricing can cut both: $\Delta c = \Delta m + \text{CSA}$. The CLO equity's exposure follows from (21.3). If a fraction $\varphi$ of the pool reprices by $\delta$, then $\Delta y_E = -\varphi\,\delta / w_E$. In 2025 roughly half the market repriced, but the average nominal coupon fell only about 20 bp *(Loomis Sayles, Q4 2025)*, so the equity lost about $0.20\%/0.09 \approx 2.2$ points of yield a year. Guggenheim estimated that the 2024 repricings cut contractual spreads by 53 bp each, and CreditSights put the typical cut at 40–50 bp.

> **Trend Watch: the repricing machine, 2024–2026.**
> *2024.* Repricing volume **\$756.8bn**. US institutional loan volume including repricings and extensions was "almost \$1.4 trillion," a record by far (William Blair, *Leveraged Finance Newsletter*, citing PitchBook LCD). About 62% of loans traded above par at year-end (Guggenheim, citing LCD/BofA).
> *Jan 2025.* A record \$215bn month, with repricings 52% of year-to-date volume (Matrix CMG, citing LCD). At its peak the cycle averaged \$52.5bn a month and touched 632 borrowers, 57% of index borrowers (PitchBook LCD, May 2026).
> *Q2 2025.* Repricing fell to a multiyear low of \$28.5bn after the tariff shock. The share of trading activity priced above par was 8% in April and 37% in June (LSTA).
> *FY2025.* Repricing **\$503.6bn**, second only to 2024, and refinancing \$191.8bn. B− new-issue spreads fell to 354 bp in Q4, "the lowest level since the Global Financial Crisis" (William Blair Q4-2025). 58% of loans were bid above par at year-end (Loomis Sayles).
> *2026.* \$108bn of repricings in January. Then February–April produced only \$11.8bn as a software sell-off froze the window. The share of BB− loans at or above par went 13% (end-March) → 59% (end-April) → 76% (11 May) (PitchBook LCD via Yahoo Finance, 15 May 2026).
> *What it means.* Repricing is a regime with two states, window open and window shut, and the share of the index above par is a good proxy for which state you are in. A carry model that ignores the state is wrong by up to 75% of the excess margin, per (21.8).

### Case Study: The January–April 2025 Round Trip, and the 2026 Replay

**The open window.** In December 2024 about 62% of loans were above par. January 2025 set a monthly volume record of \$215bn, about half of it repricings, and Octaura's secondary volume rose 83% month on month. In the model's terms, the window share was high, $h$ was large for every loan past its soft call, and (21.7) pinned above-par loans to roughly 100.1–100.5. Quoted carry overstated realized carry by most of the excess margin.

**The window shuts.** Activity "came to a halt in March." Octaura's March inquiry was 70% customer selling. April's tariff shock produced \$109.2bn of secondary volume, the second-busiest month on record after March 2020's \$119.3bn. Octaura saw loan prices fall 1.85 points in the first week with the VIX in the mid-40s, and the index's daily average bid "fluctuated 3.5% from crest to trough" *(LSTA; Octaura)*. The above-par share of trading fell to 8%. Now look at (21.7) from the other side. Once prices fall below par the call goes out of the money, the loan gets its full 2.7 years of spread duration back, and the excess-carry give-up (21.8) drops to zero. A buyer in mid-April bought a floater that was temporarily *long* convexity relative to its January self. It earned the recovery at full duration and kept its coupon until the window reopened.

**The window reopens.** By June the above-par share was back to 37%, refinancing and repricing activity was a four-month high of \$45bn, and the index average bid recovered to 97.6 by 24 July, a "V-shaped recovery" *(LSTA 2Q25 summary)*. A desk running the hazard model would have cut its expected carry loss sharply in April, added duration to performing B2/B loans that forced sellers were dumping (FSPI was also elevated), and handed the convexity back in June as the window state turned.

**The 2026 replay.** January 2026 repriced \$108bn. Then the "SaaS-pocalypse" arrived: AI-disruption fears hit the software sector, which is more than 5% of the loan index *(Loomis Sayles)* and more than 30% of many middle-market CLOs *(Octus; CHECK)*. February–April repricing was only \$11.8bn, the index average bid hit a low of 94.17 in early March, and new-issue spreads were about 50 bp wider than in January. By 11 May, 76% of BB− loans were back at or above par and \$47.2bn of repricings were lined up *(PitchBook LCD via Yahoo Finance)*. The Fed's May 2026 *Financial Stability Report* noted secondary spreads that "increased moderately, reflecting a high concentration of leveraged loan borrowers in the software industry." It was the same machine with a sector-shaped shock, and the same two signals mattered: the window state for repricing, and FSPI for forced sales of downgraded software names.

### Specification for AI Implementation (repricing engine)

*What ROBO built from "price the loan with its call":* a Black-style option on the loan with a strike of 100 and a volatility taken from the bond market. The result priced every loan at 99.7, including ones whose soft call had three months left to run. The precise spec: price = (21.7) when $m > s$ and (21.2) otherwise. The hazard is annualized from a monthly logit with documented features. Margin and CSA are separate. Spread durations are reported one-sided. Asserts check par at $m = s$, the ceiling ordering, and the duration asymmetry.

Theo knows an amendment from the lender group's side of the table. What he never had to do is price that side for several thousand loans before the arranger's email arrives. A screen that ranks loans by quoted spread will happily put first the names about to be repriced away, because the spread that looks fattest is the one the borrower is keenest to cut. For each name the desk needs four numbers: a price that knows about the call, a hazard that says how likely the call is this month, the share of the carry that will survive the year, and what a cut does to a CLO equity holder, who pays for it at eleven to one. ROBO's Black-style option produced none of them, which is how every loan came back at 99.7. The reference chain below is the corrective, and it is short enough to audit in one sitting.

The listing is a short chain in which each function feeds the next. `annuity` is $a(T;\text{rate})$ from (21.2), with a series expansion near zero so a zero rate does not divide by nothing. `loan_price` implements (21.7). It discounts the excess margin at base plus market spread and adds the hazard $h$ to the discount rate only while $m > s$, so with $h = 0$ it collapses to (21.2). `spread_duration` bumps the market spread a hair in one chosen direction and reports the percentage price change per unit of spread. `monthly_reprice_prob` is a logit on price minus par, a soft-call-expired flag, the above-par share of the market and a BB flag, with illustrative coefficients in `THETA`. `annual_hazard` turns a monthly probability into a continuous annual hazard through $-12\ln(1-q)$. `expected_carry_loss` is (21.8), floored at zero when the market spread exceeds the margin. `clo_equity_yield` is (21.3).

The assertions tie the chain to the text. At $m = s$ the price is par. With a 50 bp margin gap and a 6.65% discount rate, the price is 100.12 at $h = 4$, 100.45 at $h = 1$ and 101.36 at $h = 0$. Spread duration at par is 2.72 on widening and 0.25 on tightening. A hot loan (priced 100.5, soft call expired, 60% of the market above par) gets a 38% monthly hazard, a cold one under 0.1%. Expected carry loss at $h = 4$ is about 38 bp of the 50. A 22.5 bp fall in WAS takes 2.5 points off the equity yield, which is the 11× gearing.

Use the chain to price above-par loans, to net expected repricing out of quoted carry, and to read the window state. Do not use the hazard until `THETA` is fit on loan-months, and do not trust the price inside a soft call: the function applies no 101 cap, so at $h = 0$ it returns 101.36 and you must clip it yourself. The edge case that bites is the kink at $m = s$. The call switches on the instant the market spread drops below the margin, so the price has a corner at par. That is why `spread_duration` takes a `side`. A central difference averages the 2.72 and the 0.25 into a duration of about 1.5, which is wrong for a widening and wrong for a tightening.

*The full listing is [Listing 21.3 in Appendix F](#code-21-3).*

## 21.6 Loan ETFs vs CLO ETFs: Where Liquidity Transformation Lives

Chapter 20 owns the authorized-participant (AP) mechanics and March 2020. This section owns the loan-side *cause*. Theo's 13-week cash flow model makes its comeback here, reborn as a 20-business-day cash queue. A loan fund is a company whose receivables (sale proceeds) arrive in about twenty days and whose payables (redemptions) are due tomorrow. Theo has seen that company before. It hired PJT.

The wrappers, as of 2026: SRLN (State Street Blackstone Senior Loan ETF) had \$5.38bn of net assets on 15 October 2026, 731 holdings and a 0.70% gross expense ratio. Its holdings are reported on a trade-date basis *including unsettled positions*, which is an ETF wrapper's way of admitting what is inside it *(SSGA fund page)*. BKLN was about \$6.7–6.8bn in mid-2026 *(aggregators; approx.)*. Bank-loan mutual funds held \$71bn at end-2025. Meanwhile US CLO ETFs passed **\$50bn** around the start of July 2026 *(BofA via Octus)*, and JAAA alone passed **\$30bn** on 13 August 2026 *(Janus Henderson)*. Retail money did not leave loans. It left the *loan* and bought the *tranche*, and the reason is settlement.

### 21.6.1 Derivation: the buffer is a queue

Normalize NAV to 1. Let $f_t$ be day $t$'s net redemption as a fraction of NAV (positive means outflow). Redemptions are paid in about a day. To raise cash, the fund sells loans on day $t$, and the proceeds arrive $\ell$ business days later. Starting from a cash buffer $b_0$, cash on day $t$ is the buffer, minus everything paid out, plus the proceeds that have arrived:

$$
\text{cash}_t \;=\; b_0 - \sum_{u \le t} f_u + \sum_{u \le t - \ell} f_u \;=\; b_0 - S^{(\ell)}_t, \qquad S^{(\ell)}_t = \sum_{u = t-\ell+1}^{t} f_u .
$$

The fund stays liquid without borrowing if and only if $b_0 \ge \max_t S^{(\ell)}_t$. That is Little's law with the settlement cycle as service time: cash in transit equals the redemption rate times $\ell$. Now let flows follow a Gaussian AR(1), $f_t - \mu = \phi(f_{t-1} - \mu) + \sigma\varepsilon_t$, with stationary variance $\sigma_f^2 = \sigma^2/(1-\phi^2)$ and autocovariances $\sigma_f^2\phi^k$. The variance of the $\ell$-day window is

$$
\operatorname{Var}\big(S^{(\ell)}\big) \;=\; \sigma_f^2\left[\ell + 2\sum_{k=1}^{\ell-1}(\ell - k)\,\phi^k\right], \tag{21.9}
$$

and the buffer that covers a single window at one-sided confidence $z_\alpha$ is

$$
b^{\ast}_\alpha(\ell) \;=\; \ell\mu + z_\alpha\sqrt{\operatorname{Var}\big(S^{(\ell)}\big)} .
$$

(The running maximum over many windows is larger; simulate it.) The scaling is the point. With i.i.d. flows ($\phi = 0$) the buffer grows like $\sqrt{\ell}$. With persistent flows ($\phi \to 1$), which is what you get in a sell-off, it grows like $\ell$. A T+20 loan fund therefore needs between $\sqrt{20} \approx 4.5$ and 20 times the buffer of a T+1 bond fund facing the same flows. The Fed's August 2026 note puts the median bank-loan fund liquidity ratio at about 4.5% since 2024, down from about 10% in 2021. In 2–9 April 2025, bank-loan funds with above-median liquidity lost 4.2% of assets and those below median lost 2.7%. That difference is not significant, and it contrasts with March 2020's −6.7% vs −14.2%, which was significant at 1% *(Fed FEDS Note, 19 Aug 2026)*. A week of April 2025 outflows was roughly the size of the median buffer. The rest was covered by credit lines, by dealers willing to settle quickly, and by a quiet trick: unsettled *purchases* leave cash in the fund until they settle, so a loan fund's real cash is larger than its trade-date books show.

This is the queue behind the SEC's November 2022 proposal (File S7-26-22). The proposal would have removed the "less liquid" category, where most loans sit, so that loans would likely become "illiquid investments" capped at 15% of an open-end fund. The LSTA said this "effectively shuts down open-end loan funds" and proposed a standardized expedited settlement arrangement (ESA) that would give dealer-to-fund trades settlement certainty by T+3. The ICI noted that in roughly 25 years no bank-loan fund had suspended redemptions. Whether the proposal was formally withdrawn in the SEC's 2025 clean-out of pending rules is not confirmed here; check before you rely on either outcome.

**The ETF arbitrage band.** An AP that buys ETF shares at a discount $d$ to NAV and redeems them in kind receives loans. It can sell them at once, paying half the bid-ask spread $c/2$ and funding the position until settlement. Or it can warehouse them and bear price risk with annualized volatility $\sigma_L$. The discount it needs before it will act is roughly

$$
d^{\ast} \;\approx\; f_{\text{AP}}\,\frac{\ell}{360} \;+\; \min\!\left(\frac{c}{2},\; z\,\sigma_L\sqrt{\ell/252}\right).
$$

For loans in a March-2020-style stress ($c$ above 300 bp, $\ell = 20$, $\sigma_L = 15\%$), $d^{\ast}$ is at least 1.8% before the bid for size disappears entirely. For an AAA CLO note settling like a bond ($\ell = 1$), it is mostly the half-spread. If loans could move in kind as easily as bonds, the first term would shrink. They cannot, because every in-kind loan transfer is an assignment with consents, so loan ETFs redeem largely in cash and inherit the fund queue (21.9). AAA CLO notes are DTC-eligible securities, so a CLO ETF can redeem in kind and hand the bonds to the AP.

> **Ways This Blows Up.** Take a loan ETF with 4.5% cash that faces outflows of 25% of NAV in one week *(illustrative)*. With $\ell = 20$, it must sell about 20% of NAV in loans whose cash arrives a month later, so it draws its credit line on day 2 and spends the next three weeks as a leveraged loan fund. Its sales are public: the ETF basket and the dealers' axes show them, so every other holder of the same 100 index names front-runs the flow. The fire-sale discount from §21.4 then appears in the *index* names, not the CCCs. This is one reason the March 2020 loan-ETF discounts in Chapter 20 read as a settlement event as much as a credit event.

### Case Study: JAAA, April–May 2025

On 4 April 2025, two days after the tariff announcement, US-listed CLO ETFs swung to discounts averaging more than 1%. JAAA, then about \$20bn and the largest CLO ETF, traded more than 1% below NAV. It recorded its largest one-day outflow, about \$600mm (etf.com's daily flows put 8 April at \$585mm). Janus Henderson said the redemptions were absorbed with "very little impact," which is the manager's framing. In May JAAA took in about \$850mm, the "vast majority" as in-kind creations, and Barclays counted \$663mm into AAA CLO ETFs in a single May week. Total CLO-ETF assets stayed below their Q1 peak for a while *(etf.com, Octus, ETF Trends)*. Then the stack kept growing: more than \$50bn by July 2026, with JAAA about 88% of an eight-fund cohort and holding 62.1% *reset* paper *(Octus, 7 Jul 2026)*.

Read it through the band. A greater-than-1% discount on a T+1 AAA wrapper is not a settlement problem. It is a dealer balance-sheet problem: the AP's half-spread on AAA CLO paper widened for a few days. In-kind redemption let APs take the bonds instead of forcing the fund to sell, so the queue (21.9) never formed. In the same week bank-loan *funds* lost about 3–4% of assets with a 20-day queue and a 4.5% median buffer. Same asset class, same week, different settlement cycle, different plumbing outcome. There is a second-order loop too. JAAA's reset-heavy book means ETF inflows are effectively a bid for CLO resets. Resets lower the equity's cost of liabilities and keep the CLO bid for loans alive, so the ETF stack feeds back, through the AAA spread, into the loan repricing machine of §21.5. Test the cascade (CLO ETF flows → AAA spread → reset count → loan secondary bid) at 2–8 week lags before you trade it. It is a hypothesis, not a result.

> **Trend Watch: the retail wrapper moved up the stack, 2019–2026.** Bank-loan mutual funds fell 21% to \$71bn, with \$23bn of net outflows over 2019–2025 (Fed FEDS Note, Aug 2026). SRLN was \$5.38bn (Oct 2026) and BKLN about \$6.8bn (mid-2026, approx.). US CLO ETFs grew from about \$38bn (Sep 2025, Deutsche Bank Flow) to above \$50bn (Jul 2026, BofA via Octus), and JAAA passed \$30bn (13 Aug 2026). The first European CLO ETF listed in September 2024. *What it means:* daily liquidity is now being offered on the asset that settles like a bond, and the loan itself is funded by CLOs. The liquidity transformation moved to where the plumbing can carry it.

### Specification for AI Implementation (liquidity queue)

*What ROBO built from "make sure the fund can meet redemptions":* a buffer equal to the largest one-day outflow in the history file. That is correct for a T+1 fund and wrong by a factor of up to $\ell$ for this one. The precise spec: compute (21.9) analytically, check it against a seeded simulation of AR(1) flows, report the buffer for $\ell \in \{1, 7, 20\}$, and report the arbitrage band for loan and CLO wrappers.

ROBO's buffer, the largest one-day outflow in the history file, is the kind of number that looks conservative and is not. It answers the question a T+1 fund asks, how much leaves tomorrow. A loan fund's question is how much leaves before the first sale settles, which is twenty tomorrows in a row, with outflows that cluster because a sell-off is the one time redemptions are positively correlated. The desk wants that number every morning for the wrappers it trades against, with the settlement cycle as a parameter instead of an assumption. It also wants the closed form checked against a brute-force simulation, because a formula with a double sum of autocovariances is where sign errors go to live. The same listing carries the other half of the section, the discount an authorized participant demands before it will arbitrage the wrapper. So the buffer and the band sit side by side: how much can leave, and how far the price may drift before somebody steps in.

Five small functions and a test harness. `window_var` is (21.9): the stationary variance $\sigma^2/(1-\phi^2)$ times $\ell$ plus twice the autocovariance sum with weights $\ell - k$. It raises unless $|\phi| < 1$, because no stationary variance exists at a unit root. `buffer_needed` is $\ell\mu$ plus $z$ standard deviations of that window sum, with $z$ defaulting to 2.326, a 99% one-sided cut. `simulate_flows` draws seeded stationary AR(1) paths, each started from its stationary distribution so there is no burn-in. `rolling_window_sums` gets every $\ell$-day sum from one cumulative sum. `etf_discount_bound` is the arbitrage band: the AP's funding cost over $\ell$ days plus the smaller of the half-spread and $z\sigma\sqrt{\ell/252}$, the price of warehousing instead of selling.

With illustrative flows (5 bp of NAV a day on average, 40 bp standard deviation, persistence 0.4), the buffers are 1.07% at $\ell = 1$, 4.16% at 7 and 7.77% at 20. The 20-day standard deviation is 6.7 times the one-day, between $\sqrt{20}$ and 20, as the scaling argument says. Simulating 2,000 paths of 260 days and pooling the 241 windows on each, the 99th percentile is 7.86%, within about 1% of the formula. For a loan (1.5% half-spread, 15% volatility, 20 days) the band is 1.78%, and the half-spread is what binds. For an AAA CLO note (0.5% half-spread, 3% volatility, one day) it is 0.32%, and one day of price risk is cheaper than the half-spread.

Use it to size a fund's cash against a settlement cycle, to judge whether a wrapper's discount is wide enough to pull in an AP, and to stress $\phi$, since persistence estimated in a quiet year understates the week that matters. Do not read the buffer as a probability of ruin. The edge case that bites is the window. The buffer covers the 99th percentile of one $\ell$-day window, not the worst window in a year. The simulation check pools windows, so it validates the formula and says nothing about the running maximum, which is larger and grows with the horizon. Add a margin, or simulate the maximum.

*The full listing is [Listing 21.4 in Appendix F](#code-21-4).*

### Deep-Dive Resource Graph (21.6)

- **Practitioner Writing.** Fed FEDS Note, "Liquidity Transformation Risks in U.S. Bank Loan and High-Yield Mutual Funds: A 2026 Update" (19 Aug 2026): https://www.federalreserve.gov/econres/notes/feds-notes/liquidity-transformation-risks-in-u-s-bank-loan-and-high-yield-mutual-funds-a-2026-update-20260819.html · Janus Henderson, JAAA passes \$30bn (13 Aug 2026): https://www.janushenderson.com/en-us/advisor/press-releases/janus-hendersons-aaa-clo-etf-jaaa-the-worlds-largest-clo-etf-surpasses-30-billion-in-assets-under-management/ · Octus, "Portfolio Analytics Wrap: CLO ETF Manager Strategies Diverge as Total Assets Surpass \$50B" (7 Jul 2026): https://octus.com/resources/articles/portfolio-analytics-wrap-clo-etf-manager-strategies-diverge-as-total-assets-surpass-50b/
- **Data & Code.** SSGA SRLN fund page (daily holdings, trade-date basis): https://www.ssga.com/us/en/intermediary/etfs/spdr-blackstone-senior-loan-etf-srln · SEC comment file S7-26-22: https://www.sec.gov/comments/s7-26-22/ · SEC EDGAR (N-PORT holdings; quarterly reporting from Nov 2027 for large funds): https://www.sec.gov/edgar

## 21.7 Trend and Momentum in Loans: Smoothing, Ceilings, and Forced Sellers

Kaz ran a three-month momentum backtest on daily loan marks and got a Sharpe ratio he described as "suspicious in a good way." Ines asked what the marks were made of. "Let's just assume they're prices," Kaz said, and immediately regretted it.

The best academic evidence is real. Beyhaghi and Ehsani (2017) find that a momentum strategy with a three-month formation period earns a premium of 122 bp a month in the secondary loan market. The premium is concentrated in loans of the lowest-rated borrowers. Expected loan returns *decrease* with default beta, and loan and stock momentum are correlated across markets but each carries independent information *(hypothetical, backtested; sample period to CHECK)*. Mählmann reports that value and momentum in industry- and country-level loan indexes predict credit excess returns. Chapter 10 owns time-series trend in general. Three loan-specific corrections apply before you trade any of it.

### 21.7.1 Derivation: what smoothing does to a mark

Let the true return be $r_t$ (i.i.d., variance $\sigma^2$) and let the mark follow the Geltner smoothing model $\tilde r_t = (1 - \phi)\,r_t + \phi\,\tilde r_{t-1}$ with $0 \le \phi < 1$. Iterating gives $\tilde r_t = (1-\phi)\sum_{k \ge 0}\phi^k r_{t-k}$, so

$$
\operatorname{Var}(\tilde r) = \frac{(1-\phi)^2\sigma^2}{1-\phi^2} = \sigma^2\,\frac{1-\phi}{1+\phi}, \qquad \operatorname{Corr}(\tilde r_t, \tilde r_{t-1}) = \phi. \tag{21.10}
$$

With $\phi = 0.5$, marked volatility is $\sqrt{1/3} \approx 58\%$ of true volatility and the Sharpe ratio is inflated by about 1.7×. Positive autocorrelation appears in a series with none, and short-horizon momentum on raw marks partly rediscovers the smoother. The contemporaneous beta to an unsmoothed factor $F_t$ is $\beta(1-\phi)$. Summing slopes over $K$ lags (Dimson 1979) recovers $\beta(1 - \phi^{K+1})$. Inverting the filter, $\hat r_t = (\tilde r_t - \hat\phi\,\tilde r_{t-1})/(1 - \hat\phi)$, desmooths the series. **Desmooth, then test momentum. If the premium survives, use executable prints (venue trades) to confirm it before you size it.**

**The ceiling truncates winners.** By (21.7), a loan near 100.5 in an open window has almost no price upside. Its "momentum" is carry. Condition the winner leg on headroom $(K_t - P_t)^{+}$, and expect winner momentum to live mostly in discount loans that are far from the call.

**Forced sellers extend losers, then reverse.** Elkamhi and Nozawa's −3.4% CAR over the 20 weeks *before* a downgrade, followed by a temporary fire-sale impact, is a momentum-then-reversal pattern created by CLO rules. It fits Beyhaghi and Ehsani's finding that momentum concentrates in the lowest ratings. The trading rule writes itself: ride loser momentum in high-FSPI names into the downgrade, then flip to the reversal once the forced sale is done. *IDO or it didn't happen*: strip carry, the loan-index beta and the equity lead–lag (stock momentum leads loans; see Chapter 10) before calling what is left alpha.

**Capacity.** With a 72 bp mean bid-ask (50 bp median) and 65% annual turnover market-wide, a monthly-rebalanced long-short that turns over half its book pays roughly 36 bp a month in half-spreads against a 122 bp gross premium *(illustrative)*. And it spends most of every holding period unsettled.

> **[SOURCE EXTRACTION]** *Schmid_Credit_Risk_Pricing_Models p.177:* "The quality of the collateral manager is one of the most important but unfortunately only badly predictable factors."
>
> **Annotation.** Schmid cites S&P's 2002 surveillance. Top-decile CDO managers held 0.10% defaulted securities against 13.91% for the bottom decile, with recoveries of 49.49% against 2.55%. For a loan momentum strategy, that dispersion is a cross-sectional factor hidden inside the forced-flow channel. The same downgrade produces different selling depending on *which* managers hold the loan: their cushions, their habits around test dates (Loumioti and Vasvari), and their vintage. Pre-pandemic reinvesting CLOs averaged a 2.76% junior cushion and 7.08% CCC in April 2025, against 3.94% and 5.70% for post-pandemic vintages *(S&P CLO Insights, via search; CHECK)*. Manager quality is still "badly predictable." Manager *constraints* are not, and FSPI is built from constraints.

### Specification for AI Implementation (stale marks)

*What ROBO built from "compute momentum on loan prices":* twelve-month returns on composite marks, with an impressive Sharpe that came mostly from the smoother. The precise spec: estimate $\hat\phi$ by lag-1 autocorrelation, desmooth, report the Dimson beta with $K$ lags, and require that any momentum statistic be computed on the desmoothed series.

ROBO's momentum backtest had an impressive Sharpe, and the first person to ask where it came from will be the risk officer at the model review, who has met a smoothed series before. A composite loan mark is a polled price, refreshed when enough dealers bother to update their runs. It moves like someone walking through water: late, smooth, and in the same direction as a moment ago. Smooth a return series and you manufacture two things at once, lower volatility and positive autocorrelation, and momentum lives on autocorrelation. So before any backtest runs, the desk needs a small, boring routine that estimates how stale the marks are, undoes it, and measures beta in a way that does not depend on the staleness. It is boring in the way the broken vendor feed is boring. Nobody notices it when it works, and everybody notices when the Sharpe collapses in production.

Four functions and a simulation. `smooth_marks` applies the recursion $\tilde r_t = (1-\phi)r_t + \phi\tilde r_{t-1}$ to a true return series, starting the first mark at the first true return. The desk never needs it in production, but it keeps the test honest, because here the truth is known. `lag1_autocorr` demeans a series and divides the lag-one cross product by the sum of squares, which by (21.10) estimates $\phi$. `geltner_desmooth` inverts the filter. It raises unless $0 \le \hat\phi < 1$, passes the first observation through, and returns $(\tilde r_t - \hat\phi\tilde r_{t-1})/(1-\hat\phi)$ for the rest. `dimson_beta` regresses the marks on the factor today and on its previous `n_lags` values, with an intercept, and returns the sum of the slopes.

The test draws 5,000 weekly returns: a factor with 2% volatility, a true beta of 0.8, 1% idiosyncratic noise, and smoothing of 0.5. The estimate $\hat\phi$ comes out at 0.49. Marked volatility is 57% of the true figure, the $\sqrt{1/3}$ of (21.10), which for an unchanged mean is the 1.7× Sharpe inflation. After desmoothing, volatility is 98% of true and the lag-one autocorrelation is about zero, so the spurious momentum is gone. The same-week beta of the marks is 0.40, which is $\beta(1-\phi)$, about half the truth. Summing slopes over eight lags gives 0.82.

Run it on every mark series before any momentum, volatility or beta number is reported, then confirm with venue prints. Two limits apply. One $\hat\phi$ describes the whole series, so a loan unquoted for three weeks and one repriced daily are treated alike. And lag-one autocorrelation cannot tell a stale mark from real momentum, so desmoothing strips some genuine effect along with the artifact, which makes the test conservative, the right way to err. The edge case that bites is the divisor. The filter divides by $1-\hat\phi$, and in a stress marks stiffen. At $\hat\phi = 0.9$ any error in $\hat\phi$ or in a single mark is magnified tenfold, and the desmoothed series is mostly noise.

*The full listing is [Listing 21.5 in Appendix F](#code-21-5).*

## 21.8 CLOs Inside the LMT

This is Theo's home turf, seen from the other side of the table. At RSSG he built uptier math for a majority group. On this desk he has to ask which seats at that table *can't* sign.

> **[SOURCE EXTRACTION]** *Moyer_Distressed_Debt_Analysis p.150:* A lender's ability to act depends on whether the agent "has syndicated the loan to other participants (particularly collateralized loan obligations) or if the loan has changed hands."
>
> **Annotation.** In 2004 this was a caution about who you would be negotiating with. In 2026 it is a feature in a model. The CLO share of a tranche decides who can fund new money, who can accept equity or a long-dated loan, and who needs the reinstated debt rated above CCC. Moyer's p.322 note that holders can be read off amendment signature pages is still the cheapest holder-identification method, now joined by trustee reports, Rule 2019 statements and, since October 2026, agent-bank voting data on Versana.

What a CLO can and cannot do in a restructuring, per Weil, "CLOs as Restructuring Participants" (May 2024):

- "The vast majority of a CLO portfolio – typically in excess of 90% – is required to consist of senior secured debt obligations."
- The manager's "primary driver" is to get the reinstated first-lien debt rated high enough "to keep it out of the 'CCC' buckets, which are typically set at 7.5%." Any excess is haircut in the OC tests and may trigger trading restrictions.
- Equity received in a restructuring "may be discounted entirely," or face punitive treatment as a loss-mitigation loan. HoldCo PIK paper must fit a "PIK Security" bucket of "up to a maximum of 5%." Fixed-rate buckets are "typically sized at 10-15%." Long-dated buckets range "from 2.5-7.5%," with haircuts.
- Investors now demand transparency on "snooze-drag" provisions. Kaz asked whether that was a sleep study. It is the family of amendment terms that count a lender's silence as consent or drag a minority along with the majority, which is how a CLO that cannot vote for a maturity extension gets extended anyway, often through a scheme or plan.
- Post-2020 indentures let CLOs buy "loss mitigation" or workout loans tied to an existing position, often funded from interest proceeds. The principal used for rescue financing is typically capped around 1–3% and carries extra OC haircuts *(law-firm notes; approx.)*.

**The CLO seat as a state variable.** For tranche $i$, let $\theta_i$ be the CLO share of holdings, $\bar\kappa_i$ the holder-weighted junior cushion, and $\psi_i$ the share of CLO holders whose CCC bucket is already full. A non-pro-rata uptier (Chapter 13) needs a required-lender majority that can both *sign* and *fund*. If $1 - \theta_i > 0.5$, a non-CLO majority is feasible without the CLOs. The excluded minority is then likely to be CLO-heavy, and the Priming Risk Score should rise for that minority. If $\theta_i$ is large, the majority must include CLOs. The deal then has to be "CLO-friendly": a rated first-lien exchange, new money within LML and PIK buckets, and maturity inside the long-dated bucket. A high $\psi_i$ with a thin $\bar\kappa_i$ means the CLOs will accept a worse economic deal in exchange for a better *rating* outcome. Carry $(\theta_i, \bar\kappa_i, \psi_i)$ as inputs to the PRS (Chapter 13) and to the default/recovery mixture (Chapter 14). The ad hoc group, represented by counsel, says in unison that it has always known this. (Cooperation agreements signed in this book so far: the counter overflowed in Part IV. Add one anyway. The CLOs signed this one subject to their indentures.)

> **Docket Diary.** *Serta Simmons Bedding.* In June 2020 Serta completed a non-pro-rata uptier with a majority of its first-lien lenders (autopsy in Chapter 13). Excluded lenders sued, including in a federal case captioned *LCM XXII Ltd. v. Serta Simmons Bedding, LLC* (S.D.N.Y.). The lead plaintiff's name is a CLO's name, which tells you who was left out. Serta filed for chapter 11 in January 2023 in the Southern District of Texas. On 31 December 2024 the Fifth Circuit held that the 2020 transaction was not an "open market purchase." Those three words remain the most expensive in finance. For this chapter, the point is the holder base. A tranche held largely by rule-bound vehicles produces a majority that can be assembled from the vehicles with the fewest rules, and an excluded minority that cannot respond by funding new money.

### Case Study: Two Holder Bases, One Uptier Proposal

The numbers here are *illustrative*. Take two \$1bn first-lien term loans with identical fundamentals. Both face an uptier proposal that requires \$150mm of new super-priority money.

- **Loan A: 70% CLOs, 30% hedge funds.** The hedge funds cannot form a majority alone. Any majority needs CLOs, but the CLOs' rescue-financing capacity is small: at a 2% cap on, say, \$400mm average deal size, about \$8mm each. The structure that clears is an exchange into a rated super-priority first lien, with the new money funded mostly by the hedge funds and a small CLO allocation through LML buckets. Expected outcome: near-pro-rata participation and a smaller excluded minority. The PRS for a CLO holder is moderate. The *forced-sale* risk is high if the exchange is rated SD and then CCC, because the CLOs then hit the cliff in §21.4.
- **Loan B: 30% CLOs, 70% hedge funds and SMAs.** A 51% non-CLO majority is feasible, funds the \$150mm itself, and has no need to include CLOs. Expected outcome: a non-pro-rata uptier that excludes most CLO holders. The PRS for a CLO holder is high. The CLO's subordinated claim may be marked as a discount or CCC asset and sold. That sale is the fundamental buyer's entry point, by (21.6) at the highest-priced end of the CCC book.

A systematic desk ranks every LME candidate by $(\theta_i, \bar\kappa_i, \psi_i)$ and by the non-CLO concentration. Then it asks the RSSG question the model cannot answer: *what does the credit agreement say about open market purchases, pro rata sharing and sacred rights?* The indenture says who must sell. The credit agreement says who can be primed.

### Deep-Dive Resource Graph (21.8)

- **Practitioner Writing.** Weil, Gotshal & Manges, "CLOs as Restructuring Participants" (May 2024) · Fitch Ratings, "U.S. CLO Indenture Features Explained" · Versana digital voting: https://www.versana.io/
- **Academic Papers.** DeMarco, Liu and Schmidt-Eisenlohr (2020), "Who Owns U.S. CLO Securities? An Update by Tranche," FEDS Notes: https://www.federalreserve.gov/econres/notes/feds-notes/who-owns-us-clo-securities-an-update-by-tranche-20200625.html

## 21.9 Desk Debrief

- **A performing loan is a floater that is short a par call.** Its spread duration is about 2.7 on the way down and about 0.25 on the way up when the repricing window is open (21.7). Quote carry net of the expected repricing loss (21.8), or you are quoting fiction.
- **The OC test is an option book written by the CLO equity.** It cannot see performing-loan prices and is short the cheapest tail of the CCC book (21.5). Past the 7.5% cliff, each dollar of new CCC costs about $(1 - p^{\ast})$, around 42 cents at Kundu's 58-cent average, through *other* loans.
- **The cure is deterministic: sell the richest CCC** (21.6). Forced sellers sell the freshly downgraded loan, which is the one fundamental buyers want. FSPI tells you who must sell, and the reversal pays the liquidity provider.
- **Every repricing costs CLO equity about 11× the spread cut** (21.3). The ETF bid for AAA resets is the equity's counter-move.
- **Settlement is a risk factor, not a back-office detail.** About 20 days on average; delayed compensation is a forced repo at the base rate; a loan fund's buffer scales between $\sqrt{\ell}$ and $\ell$ (21.9).
- **Retail liquidity moved to the tranche because the tranche settles like a bond.** JAAA could redeem in kind in April 2025. A loan ETF cannot.
- **Desmooth the marks before you believe a momentum backtest** (21.10). Then condition winners on headroom and losers on FSPI.
- **Ask two questions.** What does the credit agreement say? What does the CLO indenture say? The second decides who is a forced seller under the first.

**The Spec You Hand the Robot.** Build `loan_clo_engine` with five deterministic, seeded modules and the asserts from Blocks 1–5:

1. `acpa(pool, cash, ccc_limit)` implements (21.5): cheapest-first CCC excess, $\max(0, 1-p)$ haircuts, defaulted loans at $\min(p, R^{\text{ag}})$, discount loans at purchase price, and indenture priority "without duplication."
2. `cure_candidates(pool)` ranks CCC sales by exact recomputed ΔACPA and checks the bound (21.6).
3. `fspi(holdings, outstanding, cushion, excess)` returns, for each loan, the expected fraction sold. It uses the logistic calibrated to $\pi = 13.27\%$ at a 4% cushion with $+1.56$ pp per $-3.26\%$ of cushion, and it checks that holdings never exceed outstanding.
4. `loan_price(m, s, base, T, h)` implements (21.2)/(21.7), with a monthly-logit hazard converted by $h = -12\ln(1-q)$, margin and CSA kept as separate state, one-sided spread durations, and (21.8) carry loss.
5. `buffer_needed` and `etf_discount_bound` implement (21.9) and the band, cross-checked by simulation within 8%. Desmoothing implements (21.10) with a Dimson beta.

Units: prices as fractions of par in code and points in reports, spreads as decimals, \$mm for par, business days for $\ell$. Never infer a CCC classification, a market-value source or a test trigger: read it from the parsed indenture, or raise.

### Exercises

1. **The cure, by hand.** A CLO has \$400mm of non-defaulted par, 9% CCC, its cheapest CCC loans at 55 and its richest at 90. Using (21.6), compute the minimum ΔACPA from selling \$4mm of the richest CCC and reinvesting at par. Then do the same for \$4mm of the cheapest. Explain to an ex-RSSG colleague why the second trade "realizes a loss without curing anything."
2. **The 85.01 trade.** ROBO is told to "maximize the junior OC cushion" and is given a universe of performing B3 loans priced between 80 and 100, with a discount-obligation threshold of 85. Show that, under (21.5), ROBO buys the cheapest loans priced just above 85. Then explain which other indenture test (WARF, WAS or the CCC bucket) exists to stop it.
3. **The ceiling.** Prove that (21.7) tends to par as $h \to \infty$ for any $m > s$. Derive the soft-call version, in which exercise costs one point. At what $m - s$ does a borrower with $h = 2$ prefer to wait for the soft call to expire?
4. **Queue stress.** Using (21.9) with $\phi = 0.7$, $\sigma = 0.5\%$ and $\ell = 20$, compute the 99% buffer. Compare it with a 4.5% median liquidity ratio and with the 2–9 April 2025 bank-loan fund outflows. How large a credit line does the fund need?
5. **Smoothing tax.** Derive (21.10). Show that the Sharpe ratio of smoothed marks is inflated by $\sqrt{(1+\phi)/(1-\phi)}$, and compute how much of Beyhaghi and Ehsani's 122 bp a month could survive a $\phi = 0.3$ smoother (state your assumptions).
6. **Read the holder base.** A tranche is 65% CLO-held, with an average junior cushion of 1.2% and 60% of CLO holders over the CCC limit. Design the uptier that wins the CLO votes, and say which bucket (PIK, long-dated, LML, fixed-rate) binds first.

### Deep-Dive Resource Graph

**Podcasts**

- Bloomberg *Odd Lots*. Search its archive for episodes on CLOs, leveraged loans and private credit. We do not cite an episode we have not verified.

**Practitioner Writing**

- LSTA secondary-trading summaries and settlement-study index: https://www.lsta.org/content-category/quarterly-secondary-settlement-data-study/
- Creditflux CLO Guide, ch. 6: https://cloguide.creditflux.com/6-understanding-the-tests
- Octaura, "Octaura's Loan Platform Turns 3" (28 Apr 2026): https://www.octaura.com/blog/octauras-loan-platform-turns-3-lessons-milestones-and-whats-next
- Loomis Sayles, "Loomis on Loans Q4 2025": https://loomissayles.com/wp-content/uploads/2026/01/Loomis-on-Loans-Q4-2025-Final.pdf
- PitchBook LCD (M. Lukatsky) on the post-SaaS-pocalypse repricing market, via Yahoo Finance (15 May 2026): https://finance.yahoo.com/markets/options/articles/market-enters-post-saas-pocalypse-103621347.html
- William Blair, *Leveraged Finance Newsletter* Q4-2025, "Going for Gold" (PitchBook LCD data)
- Weil, "CLOs as Restructuring Participants" (May 2024); Academy Securities, "OC Triggers" (Apr 2023)
- Sidley, "Regulatory Update: NAIC Adopts New RBC Charges for Collateral Loans and CLOs" (Jul 2026): https://www.sidley.com/en/insights/newsupdates/2026/07/regulatory-update-naic-adopts-new-rbc-charges-for-collateral-loans-and-clos
- Federal Reserve, *Financial Stability Report* (May 2026): https://www.federalreserve.gov/publications/files/financial-stability-report-20260508.pdf

**Academic Papers**

- Beyhaghi, M. and Ehsani, S. (2017), "The Cross-Section of Expected Returns in the Secondary Corporate Loan Market," *Review of Asset Pricing Studies* 7(2), 243–277: https://academic.oup.com/raps/article/7/2/243/2966151
- Elkamhi, R. and Nozawa, Y. (2022), "Fire-Sale Risk in the Leveraged Loan Market," *JFE* 146(3): https://ideas.repec.org/a/eee/jfinec/v146y2022i3p1120-1147.html
- Kundu, S. (2023), ESRB Working Paper No. 141: https://www.esrb.europa.eu/pub/pdf/wp/esrb.wp.141.en.pdf
- Loumioti, M. and Vasvari, F. (2019), *Journal of Accounting and Economics* 67(2–3): https://lbsresearch.london.edu/id/eprint/1014
- Liu, E. and Schmidt-Eisenlohr, T. (2019), "Who Owns U.S. CLO Securities?", FEDS Notes: https://www.federalreserve.gov/econres/notes/feds-notes/who-owns-us-clo-securities-20190719.htm
- Dimson, E. (1979), "Risk Measurement When Shares Are Subject to Infrequent Trading," *Journal of Financial Economics*
- Geltner, D. (1993), "Estimating Market Values from Appraised Values without Assuming an Efficient Market," *Journal of Real Estate Research*
- Getmansky, M., Lo, A. and Makarov, I. (2004), "An Econometric Model of Serial Correlation and Illiquidity in Hedge Fund Returns," *Journal of Financial Economics*
- Shelf: `Moyer_Distressed_Debt_Analysis` pp.53–55, 150, 322; `Schmid_Credit_Risk_Pricing_Models` pp.175–177, 183–184; `Bohn_Stein_Active_Credit_Portfolio_Management` p.14; `Nuveen_Multi_Asset_Credit_Quant_Framework` pp.6, 9; `Man_Quantitative_Credit_Alpha_Early_Mover_2022` p.41

**Data & Code**

- SEC EDGAR (CLO-fund N-CSR/N-PORT filings, e.g., Eagle Point): https://www.sec.gov/edgar · Eagle Point Income Co N-CSR FY2025: https://www.sec.gov/Archives/edgar/data/1754836/000199937126004310/eic_ncsr-123125.htm
- CLO trustee data (CLO-i/Creditflux, Intex, Octus; commercial), FINRA TRACE securitized-products data for CLO tranches, Octaura venue data, and the Morningstar LSTA / PitchBook LCD index constituents (commercial)

<!-- STATUS: COMPLETE -->
