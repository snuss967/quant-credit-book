# Chapter 21: Leveraged Loans, CLOs & Loan-Market Microstructure

*Wednesday 14 October 2026, live. The desk, the loan, its borrower, the selling dealer and the two CLOs are fictional; the market figures on the screens are real and cited where they appear.*

Mags Dunleavy dropped a trade ticket on Theo's desk the way other people drop subpoenas. "Twenty-three business days," she said. "We bought seven million of a B2 term loan B on the eleventh of last month. It has not settled. The agent wants a \$3,500 transfer fee and our KYC packet. Again. Back in my day we settled these by fax, and the fax machine at least had the decency to jam where you could see it."

Theo read the ticket. Trade price 99.75. Settlement date: blank. "Delayed comp should have been running since T+7," he said. "Unless we didn't sign the assignment by T+5. Then it's our fault and nobody owes us anything."

He turned the ticket over, as if the back might be more forthcoming. It was his fourth Wednesday on the desk, and he had learned that the quickest way to find the edge of what he knew was to ask the question that sounded stupid. "Fine. What's it worth?"

Ines rolled her chair over. "Hand history, please. What is the position worth right now?"

"Easy," said Kaz, without looking up. "It's a floating-rate bond with a slightly odd call. Give me the curve and ten minutes."

"It's a loan," Theo said. "Nobody has a price. There's a mark. The mark is a composite of dealer quotes that may or may not include the dealer we bought it from. Nothing has printed since we traded, because nothing prints. There is no TRACE for loans."

"Then what do you use?"

"Whatever the CLOs are doing," said Mags.

Theo looked from one to the other. "That's three answers."

"It's one hand nobody has shown," said Ines. "Kaz is telling you what the cards would be worth face up. Mags is telling you who else is sitting at the table. You're telling me the dealer has been dealing with the lights off. All three are true at once. The risk system has us at 99.40 this morning *(illustrative)*, and I would not bet lunch on the second decimal. Or the first."

A headline crossed all four screens, and three more stacked up behind it. September's CLO tally was out: \$41.1bn of activity across 92 deals, of which only \$13.8bn was new issue, and refinancings had beaten resets for the first time since April *(Trepp, via CRE Daily, 14 Oct 2026)*. Voya's Monday note called the previous week a ratings decompression, BBs firm and CCCs weaker *(Voya IM, 12 Oct 2026)*. And the share of loans bid above par, 58% at New Year, had fallen to about a fifth by midyear *(21.7% at end-June; Eagle Point Credit Co, N-CSRS, 2026)*.

Kaz frowned at the numbers. "Only a fifth of the market above par, and the CLOs would rather refinance themselves than buy anything new. Is that good news or bad?"

"Depends which side of par you're sitting on," said Ines. "Above par is where the borrower takes chips off the table. Fifty-eight percent at year-end, and look what January did to them: a hundred and eight billion of repricings in one month. A loan at 100.5 is about to be handed back to you at 100 with fifty basis points less coupon. You are long a bond and short its upside. And two-thirds of the players at this table use house rules that tell them exactly when they must fold."

Hana had been listening from the next desk, which as the owner of the risk-data pipeline she did most of the day, since every problem on the floor eventually arrived there as a missing field. "The dealer said where it came from," she said. "On the September call. 'Out of two CLO accounts.' I wrote down the shelf names." She pulled both deals' August trustee reports from the desk's CLO data vendor and put them side by side on her second screen.

The first deal was dull in the way a healthy CLO is dull: CCC bucket 3.9%, junior overcollateralization cushion 4.2% *(both illustrative)*. The second was not. Its CCC bucket sat at 8.4% against a 7.5% limit, and its junior OC cushion was 1.1% *(illustrative)*, one bad downgrade from shutting off the cash to its equity.

Kaz leaned over to read the indenture summary Hana had opened beside the reports. "Interest diversion test. OC test." They frowned. "Is the OC test optical character recognition? Do they scan the loans?"

"Overcollateralization," Theo said. "Loans, valued the way the indenture says, divided by the notes. If the ratio drops below its trigger, cash stops flowing to the bottom of the structure and goes to pay down the top."

"So it's a covenant on the lender."

"It's a covenant the lender wrote on itself."

"That's why the dealer had it to sell," said Mags.

Theo shook his head. "It's a B2 at par. Selling it does nothing for their test. It isn't one of their CCCs."

"Nobody said it was the problem. It was the cash." Mags tapped the 1.1% on Hana's screen. "A deal with a one-point cushion sells whatever it can sell near par and buys whatever its indenture counts at par for less. Seven million at 99.75 buys a bit over eight million of something in the mid-eighties that still counts at full par *(illustrative)*. The numerator goes up a million. That isn't a view on your borrower. It's arithmetic on theirs."

Theo sat with that for a moment. At PJT a seller had always been someone with a view: wrong, scared, or knowing something. This seller had none of the three. It had a ratio.

"So we paid a price set by someone else's rulebook," he said.

"Everyone in this market does," said Ines. "The question is whether it was a good price." She tore a sheet off her pad and slid it across, the same way she had for the Kroger replay three weeks earlier. "Card. Write three things: what the loan is worth to us today, what it was worth to the seller yesterday, and why those are different numbers."

Theo took the USB stick with his 13-week cash flow model out of his pocket, looked at it, and put it back. This one was going to need a different model. He wrote the first line of the card, crossed it out, and said, mostly to himself, "At RSSG I read the credit agreement. Here I read the indenture of the lender."

The question this chapter answers: **who sets the price of a leveraged loan when two-thirds of its holders cannot freely choose what they buy, the borrower can call it at par, and the trade settles in three weeks?**

The rest of the chapter is the answer key to Theo's card, assembled in the order the desk learned it. The loan is a credit-risky floater that is short a par call, and §21.1 prices it that way. Its price is a composite of opinions, delivered through a settlement pipe about three weeks long (§21.2). Two-thirds of its holders are CLOs, whose overcollateralization tests, with their CCC, defaulted and discount haircuts, turn one borrower's downgrade into a sale whose direction can be derived and whose size can be read in a trustee report; the desk compresses that into a Forced-Sale Pressure Index (§21.3–21.4). The borrower owns the call and exercises it in waves, which a repricing hazard prices and a carry signal can trade (§21.5). A loan fund that promises daily cash on a T+20 asset is running a queue, and the buffer the queue needs can be sized (§21.6). Marks are smoothed before they reach a backtest, so loan momentum has to survive desmoothing before anyone believes it (§21.7). And the last page, the one a restructuring banker already knows, is that the CLO indenture decides who is a forced seller under the credit agreement, and therefore who can sign and fund an uptier (§21.8). At RSSG the question was "What does the credit agreement say?" Here it is also "What does the *CLO indenture* say?"

## 21.1 The Leveraged Loan as an Instrument: A Floater That Is Short a Call

At RSSG the term loan B was the top of the capital structure: first lien, secured, the tranche whose recovery you fought over and whose lenders you organized. That view is right in distress. For the large majority of loans on the large majority of days, when nobody is distressed, it misses where the price comes from. A performing leveraged loan's price is set by three things that are not financial covenants. (There usually aren't any: more than 90% of the index is covenant-lite.) The three things are a floating coupon, a borrower call at par, and a holder base dominated by vehicles that follow rules.

*Same Wednesday, later that morning. The loan's terms below are the fictional ticket's; the market conventions and the court case are real.*

Kaz wanted the term sheet before the curve, which Theo took as progress. He printed the loan's two-page summary from the agent's portal and walked Kaz through it the way he would once have walked a client through a first-day declaration, one clause at a time, saying out loud why each one mattered.

"Coupon," he said. "Term SOFR plus a margin, 325 basis points on this one *(illustrative)*, reset monthly. ACT/360. There's a floor on the base rate at fifty basis points, which nobody has cared about since 2022 and everybody will care about the day SOFR goes back near zero. Some older loans still carry a credit spread adjustment from the LIBOR conversion. Ours was repriced in January, and the arranger stripped it."

"So the coupon follows the base rate. Fine. That's a floater."

"Security: first-lien, senior secured. Covenants: none, for the term loan. It's covenant-lite, like more than ninety percent of the index. The revolver keeps a springing leverage test, which only wakes up if the revolver is drawn past a threshold, and the term lenders can't enforce it anyway." Theo turned the page. "Amortization one percent a year, bullet at maturity. That's typical, but you check the agreement every time, because 'typical' is how people get surprised."

"And the call?"

"Prepayable at par at any time. Except for the soft call: for six months after closing, or after a repricing, a *repricing* costs the borrower one point. Not every prepayment, only one done to cut the margin. So it's 101 inside the window and 100 outside it. Ours was repriced on 23 January *(illustrative)*, so the window shut in July."

Kaz read the definition twice. "Soft call. Does that mean the borrower phones the lenders and asks nicely?"

"Close," said Theo. "The borrower's arranger phones the lenders, tells them the new margin, and anyone who objects gets taken out at par. Asking nicely, with a door."

"Transfer," Kaz said, reading ahead. "Assignment and Assumption. That's not a security transfer."

"It isn't a security at all. That's the last line." Theo pointed. "Every trade is an assignment. The agent bank has to consent. The borrower usually has to consent too, and that consent is deemed given if the borrower says nothing for a set number of business days. Someone checks the buyer against the disqualified-lender list. Then the agent writes the new name in its register, and only then do we own it. There's no book entry and no DTC. That's why our ticket has a blank where the settlement date goes."

"Why not just make it a security?"

"Somebody tried, in court." In *Kirschner v. J.P. Morgan Chase Bank, N.A.* (2d Cir., 24 August 2023), the Second Circuit held that syndicated term loans are not securities under the *Reves* test. So no T+1 mandate, no DTC settlement and no securities-law disclosure regime are coming to rescue the plumbing. "The plumbing is the plumbing," Theo said, and §21.2 follows it pipe by pipe.

Kaz put the page down. "So: a floater I understand, a call I understand, and a transfer I don't. Price the first two."

### 21.1.1 Derivation: carry, price, and the two durations

> **Math, Gently.** *Why a floater sits at par, what an extra 50 bp is worth, and why the loan has two durations.* Part one is a picture. Imagine a flat let on a lease whose rent resets every month to whatever the flat would fetch on the open market that month. What is the lease itself worth, over and above the flat? Nothing. Whatever rents do, next month's rent will be the market rent, so nobody would pay a premium to take over the lease and nobody would demand a discount to hand it back. A loan whose coupon resets to "SOFR plus exactly the spread the market now demands" is that lease, and on every reset date it is worth par for the same reason. Now suppose the lease pays 50 bp a year *more* than the market, locked in for the three years the tenant is expected to stay. That extra is a small annuity: half a point a year per 100 of par. Undiscounted it is 1.5 points; discounted at 7.5%, three years of payments are worth about 2.69 years' worth, so the extra is worth $0.50 \times 2.69 \approx 1.35$ points, and the loan "should" trade near 101.35. Hold that thought, because the borrower has an opinion about it.
>
> Part two asks the same loan two different questions. If SOFR jumps 100 bp tomorrow, the price barely moves: the coupon catches up at the next reset, a month away, so the rate duration is about a twelfth of a year. If instead the spread the market demands for *this borrower* jumps 100 bp, the coupon never catches up, because the margin is fixed for life. The annuity now runs the other way, about one point a year for 2.69 discounted years, and the price falls about 2.7 points. Rate duration 0.1, spread duration 2.7: a money-market fund for rates and a three-year bond for credit, in one instrument. The full version is next.

In symbols, a loan's return is carry plus price change, equation (21.1), and a loan without its call is worth par plus an annuity of the margin difference, equation (21.2). The derivation builds both, then takes the call away.

#### The Full Derivation

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

> **Math, Gently.** *A bond with a lid.* Draw the loan's price on the vertical axis and the spread the market demands for this borrower on the horizontal, wide on the left and tight on the right. A plain bond's line keeps climbing to the right: every 100 bp of tightening adds about 2.7 points, forever. Now hand the borrower a call struck at 100. To the left of the strike nothing changes, because no borrower prepays a loan that is cheap to keep. To the right, the line rises to about par and then bends flat, like a ceiling it cannot get through. That bend is the whole instrument: long a bond, short a call on it. Here is the tiny number. The first box priced our loan, with 50 bp of excess margin, at 101.35 without a call. With the call, the borrower's arranger phones, the loan is handed back at 100, and whoever stays in holds a new loan at par with 50 bp less coupon. The 1.35 points moved from the lender's pocket to the borrower's. A buyer who paid 100.5 the week before loses the half-point on the day the call is exercised. Why would anyone pay 100.5 at all? Because the borrower does not exercise instantly, and §21.5 turns that delay into a hazard rate and the half-point into a forecast.

Kaz drew the bent line on the whiteboard and wrote "negative convexity, but with lawyers" underneath it. Theo did not correct it. An allocator, reading the same loan off a monthly index, sees neither the lid nor the lawyers:

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

The dealer who sold Mags the loan was, that Wednesday, probably one of the quotes inside the composite that marked it, and it was certainly still carrying the loan. When Theo called its loan desk about the KYC packet, he got the other half of the ticket.

> **View From Another Seat.** *The selling dealer's loan desk (a generic seat; the ticket is the cold open's illustrative one).* From the dealer's chair, Mags's twenty-three-day ticket is a position it has already sold and still owns. Price risk passed to the buyer on 11 September, but the loan sits on the dealer's balance sheet until the agent records the assignment, funded at the dealer's own rate. Since T+7, delayed compensation has paid the dealer only the base rate flat on the purchase price while it passes the coupon through, and its treasury charges more than that, so each extra day costs the funding spread plus a capital charge that appears on no ticket. The KYC packet is the buyer's to deliver, and the dealer's closer has asked for it three times. The \$3,500 assignment fee is split by convention, and the dealer will dispute its half on the grounds that the delay is the buyer's fault. None of this shows on a screen. What shows is the dealer's next quote, and the quote carries all of it. Its head of loan trading would explain the asymmetry with a venue's own numbers. During May 2025, as the tariff-week sellers thinned out, Octaura estimated that the cost to sell a loan fell from 23 cents to 9, while the cost to buy was 13 *(Octaura, "On the Blotter: 2025 in review")*. A dealer charges the side the crowd is on, because the crowd's paper is the paper it will warehouse, fund and chase signatures on for three weeks. A buyer in a selling month gets the cheaper half of the spread, and a counterparty who would very much like the trade to settle.

Theo hung up with a new respect for the dealer and no KYC answer. The marks the desk had to work with were no better than the people quoting them, which is the problem the first quant credit managers ran into when they looked at loans at all:

> **[SOURCE EXTRACTION]** *Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.41:* "funds targeting opportunities in leveraged loans and, particularly, convertible bonds, where we see the potential for significant alpha. While loans and other private credit instruments are obviously problematic from a data availability perspective at present... Already both Refinitiv and IHS Markit are providing daily pricing on 6,500 loan facilities."
>
> **Annotation.** "Daily pricing" means daily *marks*. That distinction is the whole data problem. A daily mark built from quotes is a smoothed, partly stale estimate of an unobserved price, and its errors are autocorrelated. §21.7 shows that naive momentum on such marks partly rediscovers the smoother. The 2026 desk has two things Man did not have in 2022. The first is electronic venue data (Octaura's inquiry and trade flow, below), which adds real executable prints for a growing share of volume. The second is CLO trustee data (holdings, prices and test results by deal), which tells you who *must* trade before they do. The modern desk combines the three sources: composite marks for coverage, venue prints for truth where they exist, and trustee holdings for flow. It does not trust any one of them alone.

### 21.2.1 Settlement: the slowest thing in credit

> **[SOURCE EXTRACTION]** *Moyer_Distressed_Debt_Analysis p.322:* "For loans of healthy borrowers (referred to as the par loan market), the settlement convention typically is 10 days (T+10), but modest delays are common... The settlement convention in the distressed bank debt market is 30 days, but delays (sometimes of up to 120 days) are fairly common."
>
> **Annotation.** Moyer wrote this in 2004, when bonds settled T+3. Since then bonds went to T+2 (2017) and T+1 (28 May 2024). Loans moved their *convention* to T+7 for par and T+20 for distressed, but barely moved their *reality*. Moyer's page also notes an agent transfer fee of "\$2500–\$5000" and that loan holders can be identified from amendment signature pages. Both are still true, and the second is why holder-base modeling (§21.8) is possible. The modern departure is legal: after *Kirschner*, nothing forces loans onto securities rails. The ledger stays with the agent bank, and every trade is an assignment with consents.

*Same Wednesday, 2:30 p.m. The ticket's stops and the desk's paperwork are fictional; the LSTA protocol and its numbers are real.*

By the afternoon Theo had given up on the phone and taken the problem to the whiteboard, which on this desk meant erasing half of one of Kaz's stochastic integrals and promising to put it back. He drew the life of a single par loan trade as a line of nine stops and wrote under each one who owned it.

Stop one was the trade itself, agreed on the phone on 11 September. Stop two, the confirmation, went out that afternoon. Stop three was the assignment agreement that buyer and seller both sign; the desk's closer had signed it on T+3, the first good news of the day, because it meant delayed compensation had been running since T+7 and the dealer owed the desk the loan's economics for every day since. Stop four was the agent's consent. Stop five was the borrower's, which this credit agreement deems given after five business days of silence *(illustrative)*; the borrower had been silent, which in this market counts as enthusiasm. Stop six was KYC on the buyer at the agent bank. Stop seven was the check against the disqualified-lender list. Stop eight was the funding memo that tells each side how much cash moves, net of accrued interest and delayed compensation. At stop nine the agent writes the buyer's name in its register, and the trade has settled.

He put a red magnet on stop six. "Here. The agent wants our beneficial-ownership certification refreshed. Ours expired in August. Nobody told anybody, because the form lives in compliance and the trade lives here."

Kaz studied the line. "Nine parties, nine queues, and nobody is paid for speed. It's a tandem queue. The whole thing runs at the pace of its slowest server."

"The slowest server," said Mags, "is always the one that isn't paid."

How slow the whole line runs is surprisingly hard to see from outside. The LSTA's own chart puts the decade average to January 2025 at roughly 20 days against the T+7 convention. Vendors describe averages "upwards of 20 days" for many firms. The LSTA's quarterly settlement studies, the ones with exact medians, are members-only.

"There was one autumn," Ines said, "when somebody made it faster on purpose." She told it as a hand, which is how she told everything. Before September 2016, delayed compensation (§21.2.2 defines it) was paid to the buyer whether or not the buyer had done its paperwork. A buyer could leave an assignment unsigned in a drawer and collect the loan's coupon, financed at the base rate, with no capital tied up. "The LSTA had dealt every buyer a free repo option. The buyers did what anyone does with a free option. They held it." The delayed-compensation protocol (Phase I for trades from 1 September 2016, Phase II from 1 November 2016) made compensation "requirements-based." Under it, the buyer must execute the documents by T+5 and pick a settlement date of T+7 or earlier, or it loses compensation for the delay. Median par settlement fell from T+12 (January–August 2016) to T+9 (September 2016), and the share settling within T+7 rose from 23% to 37% *(Markets Media, 2 Nov 2016)*. "When you take away a free option, people stop exercising it," Ines said. "This is the most reliable law in finance. Three days off the median, and all anyone changed was who gets paid when."

Theo was already sketching a column header. "So we model the lag for every loan. A distribution by agent bank, by regime, by whether the borrower has to consent..."

"For whom?" Ines asked. It was the question she asked when she wanted him to find the answer himself, so he tried. A CLO buying to hold barely notices the twenty days: it did not need the cash, and the coupon accrues to it either way. The dealer he had just spoken to notices them as funding cost. A loan fund that sold to meet a redemption notices nothing else, because the cash it needs is the thing that has not arrived, which is §21.6. And the desk itself notices the tail. On a forty-line portfolio trade, the one line that settles on day sixty is the one that sets the counterparty exposure and the balance-sheet charge for the whole package.

"So the lag is worth modeling exactly in proportion to how badly the holder needed the cash," Theo said.

Ines picked up her coffee. "Or the balance sheet. Write that down."

He wrote it under the nine stops, took the red magnet off stop six and went to find compliance.

### 21.2.2 Derivation: delayed compensation is a forced repo

> **Math, Gently.** *Delayed compensation is a repo you did not agree to.* Picture two ledgers side by side, the buyer's and the seller's, starting on T+7 for the cold open's ticket: \$7mm of par bought at 99.75, so \$6.98mm of purchase price, on a loan paying the base rate plus 325 bp *(illustrative)*. On the buyer's ledger, every day the seller hands over the coupon the loan earned, and the buyer hands back the base rate on \$6.98mm. Meanwhile the buyer's own \$6.98mm, which has not been delivered, sits in a money fund earning about the base rate. Net, the buyer has the loan's coupon and the loan's price risk and has paid the base rate flat to finance it: it owns the loan on borrowed money. On the seller's ledger, the loan is still on its balance sheet, its treasury charges it, say, the base rate plus 50 bp to fund \$6.98mm, and the buyer pays it only the base rate. The seller is lending the buyer the purchase price, secured by the loan, at a rate it did not choose and for a term nobody can tell it. That is a repo. Now the tiny number: 50 bp a year on \$6.98mm is about \$97 a day on a 360-day year, and the twenty-two calendar days from T+7 to this Wednesday come to about \$2,100 *(illustrative)*. Small, and nobody budgeted for it. The full version, with the general formula, is next.

In symbols, the daily transfer $\text{DC}_u$ below hands the buyer the loan's economics from T+7, and the seller's cost is the gap between its funding rate $f_S$ and the base rate.

#### The Full Derivation

Let a buyer purchase par $n$ at price $P$ (points) on trade date $T$. The settlement date is the random variable $T + \ell$, measured in business days. In stylized form (the LSTA Standard Terms and Conditions govern the details), delayed compensation starts on day $T+7$ if the buyer has met its obligations. From then until settlement, the seller pays the buyer the interest accruing on the loan, and the buyer pays the seller a cost of carry on the purchase price at a benchmark rate, which we write as the base rate $b$. The net daily transfer to the buyer, for $u \in (T+7, T+\ell]$, is

$$
\text{DC}_u \;=\; \frac{n}{360}\left[(b_u + m) \;-\; b_u\,\frac{P}{100}\right].
$$

Read it as positions. From $T+7$ the buyer has the loan's full economics: price risk (which passed on trade date) plus coupon. It pays $b$ on the purchase price while its own cash, still undelivered, earns roughly $b$ in a money fund. The buyer therefore owns the loan, financed at $b$ flat. The seller still carries the loan on its balance sheet, funded at its own rate $f_S$, collects $b$ on the price, and passes the coupon through. Its daily cost is

$$
\text{cost}^{\text{seller}}_u \;=\; \frac{n\,P}{100 \cdot 360}\,\big(f_S - b_u\big) \;+\; \text{capital and operational charges}.
$$

So **every late loan trade is a short-dated repo that the seller is forced to provide at the base rate flat.** For a dealer funding at $b + 50$ bp, carrying \$10mm at 99 for 13 extra days costs about $10{,}000{,}000 \times 0.99 \times 0.005 \times 13/360 \approx$ \$1,800 *(illustrative)*. That is small per trade and large across a book with \$1tn of annual volume. The bigger costs are elsewhere. Counterparty exposure lives for $\ell$ days instead of one. A seller that needed *cash* (a loan fund meeting redemptions) does not get it for $\ell$ days, which is §21.6. And between $T$ and $T+7$ nobody compensates anybody, so the first week is a dead zone in which the buyer's cash and the seller's loan both sit idle. Figure 21.1 lays the clock out in business days.

![Figure 21.1: Bonds settle in one day and par loans by convention in seven but in practice in about twenty, and every day after T+7 is a forced repo that the seller funds at the base rate. Source: Moyer, Distressed Debt Analysis, p.322 (2004 conventions); LSTA delayed-compensation protocol medians via Markets Media (2 Nov 2016); the roughly 20-day average is read off an LSTA chart (April 2025 slides, approximate, as flagged in §21.2.1).](assets/figures/ch21_settlement_clock.png)

For a pricing engine, $\ell$ is a distribution, not a constant. Model it by regime (par vs distressed), by agent bank, by whether borrower consent is required, and by calendar (quarter-ends and CLO effective dates congest the queue). A shifted negative binomial in business days is a reasonable first fit. Chapter 19's portfolio-trading engine should price a loan line with $\mathbb{E}[\ell]$ and its tail, not with T+1.

### 21.2.3 E-trading arrives, two decades late

Octaura, a dealer-backed platform that began life as "Project Octopus," launched loan trading in April 2023 with three dealers and 34 buy-side firms. By April 2026 it had about 30 dealers and more than 170 buy-side firms. Its share of LSTA-reported secondary volume went from 1% (April 2024) to 6.4% (July 2025) to 7.7% (January 2026). It reports a record \$19.6bn traded in Q1 2026 and its CFO says it exited June 2026 at 7.51% *(Octaura blog posts, 2025–2026; Pulse 2.0 interview, 29 Jul 2026; vendor-reported)*. It added a CLO platform in September 2025 and a "Live Feedback" auction protocol for CLO BWICs in February 2026. Separately, Versana, a consortium of agent banks, put amendment and consent voting on a live digital platform in October 2026.

The inquiry tape is already a signal. In March 2025, 70% of Octaura inquiry was customer selling. In April it was balanced (55% sellers). By June, 72% was buying, and in May the cost to sell had collapsed from 23 cents to 9, the asymmetry the dealer seat above reads off the same tape *(Octaura, "On the Blotter: 2025 in review")*. A buy/sell imbalance that a venue publishes monthly is a crude flow factor, but it is a real, timestamped one.

Ines put it in her own terms when Theo showed her the monthly series. "That's the first hand history this market has ever kept with a clock on it. Crude, monthly, one venue's worth of hands, and still more than anyone had in 2022." Then she pointed at the Versana announcement on his other screen. "And that one is the part you used to bill for. Every uptier you ever worked on was a consent game. The consent machinery just became an API, which means somebody, soon, will know who voted before the press release does." (Part IV's liability-management chapters are where that matters.)

> **Trend Watch: settlement and e-trading, 2004–2026.**
> *Settlement.* T+10 par / T+30 distressed conventions with delays to 120 days (`Moyer_Distressed_Debt_Analysis p.322`, 2004) → median T+12 falling to T+9 after the September 2016 delayed-comp protocol (Markets Media, Nov 2016) → a ten-year average near 20 days to January 2025 (LSTA slides; approx.). Over the same period bonds went T+3 → T+2 (2017) → T+1 (May 2024).
> *Volume.* Secondary loan trading was \$824bn in 2022 (then a record), \$821.4bn in 2024, and a record **\$971bn** in 2025. Trailing-twelve-month volume passed **\$1tn** in Q1 2026, then Q2 2026 fell back as volatility subsided (LSTA; size of the decline to be checked).
> *Electronification.* Octaura share 0% (April 2023) → 1% (April 2024) → 6.4% (July 2025) → about 7.5–7.7% (H1 2026), vendor-reported.
> *What it means.* Execution is getting faster while settlement is not. The gap between the two is a balance-sheet cost (the forced repo above) and a liquidity mismatch (§21.6), and both scale with turnover, which is at a record.

### Deep-Dive Resource Graph (21.2)

- **Practitioner Writing.** LSTA, "2Q25 Secondary Trading Monthly Executive Summary" (24 Jul 2025): https://www.lsta.org/content/lsta-secondary-trading-monthly-executive-summary-2q25-secondary-loan-trading-volumes-spike-again-to-a-record-262-billion/ · LSTA quarterly settlement-study index (members-only decks): https://www.lsta.org/content-category/quarterly-secondary-settlement-data-study/ · Markets Media, "LSTA's Delayed Comp Protocol Shows Encouraging Progress" (2016): https://www.marketsmedia.com/lstas-delayed-comp-protocol-shows-encouraging-progress-moves-phase-ii/ · Octaura, "On the Blotter: 2025 in review": https://news.octaura.com/on-the-blotter-2025-in-review · Simpson Thacher on *Kirschner* (25 Aug 2023): https://www.stblaw.com/about-us/publications/view/2023/08/25/second-circuit-holds-that-kirschner-syndicated-term-loans-are-not-securities
- **Episodes & Posts.**
  - **Tackling the complex terrain of CLO secondary trading** (Vitaliy Kozak, Octaura, 2025-09-22). A vendor's diagnosis of the CLO e-trading gap: most secondary trading runs through BWICs with "very low probability of trading for bidders", manual email and phone workflows and no central price visibility. Read it as the problem statement for §21.2.3, not as evidence. https://news.octaura.com/tackling-the-complex-terrain-of-clo-secondary-trading
  - **Citi Warns of Private Debt Risk as 'Tourists' Are Forced to Sell** (*The Credit Edge*, Bloomberg Intelligence, guest Mickey Bhatia of Citi, 2026-04-30). Rookie lenders selling "below the economic value" and, per the page, the expansion of electronic trading to CLOs; it ties the e-trading arrival of §21.2.3 to the forced-seller schedule of §21.4. https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/citi-warns-of-private-debt-risk-as-tourists-are-forced-to-sell
  - **Investor Diversity and Liquidity in the Secondary Loan Market** (NY Fed *Liberty Street Economics*, 2017-08-09). The secondary loan market moved from banks and insurers trading occasionally to CLOs, loan funds and hedge funds trading actively, with the average number of investor types per term loan rising from two (1991) to five (2013). Loan liquidity is a function of who holds the paper, the premise of §21.2. https://libertystreeteconomics.newyorkfed.org/2017/08/investor-diversity-and-liquidity-in-the-secondary-loan-market/
  - **Private Credit and Leveraged Loan Markets: Similarities, Differences, and Substitution** (Banegas, Castelo, Degerli, Dobridge and Kennedy, Federal Reserve Board FEDS Note, 2026-08-11). The two markets serve similar industries and credit profiles but differ in structure, liquidity and funding, and larger middle-market firms substitute between them; the official statement of the public-private substitution that §21.1 assumes. https://www.federalreserve.gov/econres/notes/feds-notes/private-credit-and-leveraged-loan-markets-similarities-differences-and-substitution-20260811.html
- **Data & Code.** Versana: https://www.versana.io/ · LSTA/LSEG and S&P Global loan pricing (commercial; no public API).

## 21.3 CLO Anatomy and the Arbitrage

Mags's definition: "A CLO is a bank that the rating agencies designed and the equity investors rent." It is a bankruptcy-remote special-purpose vehicle, usually Cayman-incorporated, with a trustee, a collateral manager, and an indenture. It buys about 200–400 broadly syndicated loans and funds them with a stack of floating-rate notes. A typical US broadly syndicated (BSL) CLO stack is AAA 60–63%, AA 10–13%, A 7–9%, BBB 4–6%, BB 4–6%, sometimes a sliver of single-B at 1–2%, and equity 8–10% *(Barings, "What is a CLO," June 2025; approx.)*. The AAA's subordination, which is its credit enhancement, is typically 35–40%. At issue the deal has a reinvestment period of roughly four to five years, during which the manager trades the pool, and a non-call period of about two years, after which the equity can refinance the notes.

The life cycle runs warehouse → pricing → ramp → effective date → reinvestment → amortization. The equity holds a call on the liabilities. It can *refinance* (reprice some tranches and keep the dates) or *reset* (reprice everything and extend the reinvestment period and maturity). That call has become the liability-side twin of the borrower's repricing call. US CLO new issuance set records of \$202bn in 2024 and \$209bn in 2025. Resets were \$223bn and \$232bn, and refinancings \$84bn and \$105bn *(Eagle Point Credit Co and Eagle Point Income Co, Forms N-CSR, FY2024 and FY2025)*. In H1 2026, new issue was only about 35% of roughly \$230bn of activity *(Dechert OnPoint, 4 Aug 2026; Eagle Point N-CSRS)*. JPMorgan, via Maples, called *net* new supply "near-anaemic." Most of the CLO market's activity is the same deals refinancing themselves, the way most of the loan market's activity is the same loans repricing themselves. It is turtles all the way down, and every turtle has a call option.

> **[SOURCE EXTRACTION]** *Bohn_Stein_Active_Credit_Portfolio_Management p.14:* In his June 2008 foreword Darrell Duffie wrote that "by mid-2008 the issuance of bank-loan collateralized loan obligations (CLOs) has fallen off significantly," and that CLOs are "well suited to transferring credit risk... to buy-and-hold investors who are less crucial to the provision of liquidity."
>
> **Annotation.** Both halves aged in interesting ways. The issuance collapse of 2008 became, by 2024–2025, back-to-back records above \$200bn a year. The "buy-and-hold" description survives as the most expensive half-truth in the asset class. A CLO's *liabilities* are held by buy-and-hold investors: banks, insurers and, since 2020, retail through AAA CLO ETFs (§21.6). Its *assets* are traded under a rulebook that turns rating changes into sales. A CLO is buy-and-hold until a rating agency moves. After that it is the most predictable seller in credit. That predictability is the alpha in §21.4.

### 21.3.1 Derivation: the arbitrage and its 11× gearing

> **Math, Gently.** *Why 50 bp becomes 5.6 points.* Take Mags's bank literally. On one side of its balance sheet sits a dollar of loans. On the other sit 91 cents of notes, owed to the AAA-through-BB investors at spreads fixed in the indenture, and 9 cents of equity that gets whatever is left over. Now let the loans' spread fall by 10 bp. The noteholders do not notice, because their spreads do not move. So the whole loss, 10 bp a year on a full dollar, which is a tenth of a cent, lands on 9 cents of equity. A tenth of a cent out of 9 cents is about 1.1% of the equity's money a year. That ratio of a dollar of exposure to 9 cents of capital is the gearing, $1/0.09 \approx 11$, and every basis point of collateral spread reaches the equity multiplied by it. Scale the repricing up to 50 bp, a busy January's worth, and the equity loses about $11 \times 0.50 \approx 5.6$ points of yield a year. The lever works upward too, which is why managers fight for every cheap point of par. The general version, with fees and losses in it, is next.

Formally, the equity's yield is the base rate plus the pool's excess spread divided by the equity's thickness, equation (21.3), and the gearing is that equation's derivative.

#### The Full Derivation

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

Compare two vintages. Moyer's 2004 worked example uses collateral at 535 bp and investment-grade tranches (87% of the structure) at about 88 bp. The BB/B tranches are at 750 bp, which gives blended funding of about 110 bp and a net spread of about 425 bp to a 10% equity (`Moyer_Distressed_Debt_Analysis p.53–54`). Before fees and losses, that is about 42% a year on the equity, by our division. Now an illustrative 2025 deal. Take WAS = 319 bp, the index's nominal spread at year-end 2025 *(Loomis Sayles, "Loomis on Loans Q4 2025")*, and AAA at 130 bp (Eagle Point puts year-end AAA at 133 bp). Put AA at 175, A at 210, BBB at 310 and BB at 575 bp, with weights 62/11/8/5/5% *(mezzanine spreads illustrative)*. Then $\sum_k w_k s_k \approx 161$ bp, and the excess spread is about 158 bp. Subtract 45 bp of fees and 75 bp of expected loss *(illustrative)* and 38 bp remains, which is about 4.2% on a 9% equity, plus the base rate. The 2004 arbitrage paid for a lot of mistakes. The 2025 arbitrage pays for very few. That is why managers fight for every basis point of par build, buying loans at 97 rather than 100, and why the CCC haircut in §21.4 bites so hard. Figure 21.2 draws the stack and the waterfall for this deal.

![Figure 21.2: In the worked 2025 deal the 319 bp of collateral spread leaves only 38 bp for the 9% equity slice, so a 50 bp repricing turns +4.2% over SOFR into −1.3%. Illustrative: the worked deal of §21.3.1; the 319 bp WAS (Loomis Sayles, year-end 2025) and the 130 bp AAA spread are sourced, while the other spreads, 45 bp of fees and 75 bp of expected loss are assumptions stated in the text.](assets/figures/ch21_clo_arbitrage.png)

> **[SOURCE EXTRACTION]** *Moyer_Distressed_Debt_Analysis p.53:* CDOs "frequently face purchase and sale pressures not driven by return maximization."
>
> **Annotation.** Moyer wrote this when CDOs held "over 20%" of the low-rated loan and bond market (p.55). The share is now about two-thirds of loans outstanding. The sentence has moved from a curiosity in a chapter on market participants to the first-order fact about loan price formation. The modern desk turns it into code. "Pressures not driven by return maximization" become a set of indicator functions on ratings and prices (the tests below), and each one is a predictable flow.

### 21.3.2 Derivation: why every CLO owns the same 200 names

> **Math, Gently.** *Two hundred and fifty coins that like to agree.* A distribution is a list of what could happen and how likely each outcome is, and two numbers summarize most of what a rating agency wants from one: the mean, the average outcome, and the variance, the average squared miss from that mean (its square root, the standard deviation, is the typical miss in dollars). Here is the building block. A fair coin that pays \$1 on heads has a mean of 50 cents and a variance of 0.25. Flip 250 independent coins and both add up: the mean is \$125 and the variance is $250 \times 0.25 = 62.5$, so the typical miss is about \$7.90, around 6% of the mean. Independence lets the misses cancel. Now make the coins slightly sticky, so that any two land the same way a little more often than chance: a correlation of 3%. Each pair adds a sliver of extra variance, and there are $250 \times 249$, about 62,000, ordered pairs. The variance becomes $62.5 \times (1 + 249 \times 0.03) \approx 62.5 \times 8.47 \approx 529$, and the typical miss is \$23. How many independent coins, each made bigger so the stake still totals \$250, would wobble by that same \$23? About $250 / 8.47 \approx 29.5$. That is the diversity score: 250 sticky coins carry the risk of about 30 honest ones. Add another thousand coins at the same stickiness and the score creeps toward $1/0.03 \approx 33$ and stops. Correlation puts a ceiling on diversification, because it makes the variance of a sum bigger than the sum of the variances. (Chapter 5 is where distributions in general live; this chapter needs only the mean, the variance and that one fact.)

The derivation runs the same arithmetic for loans, with par, default probability and loss given default in place of the coin's dollar, and arrives at equation (21.4).

#### The Full Derivation

Rating agencies require diversity, and Moody's measures it with the binomial expansion technique (BET). BET replaces a pool of correlated credits with a smaller number of *independent* credits that match the first two moments of the loss distribution. `Schmid_Credit_Risk_Pricing_Models p.183–184` gives the general formulas. Here is the homogeneous case, which is all the intuition needs. Take $J$ obligors, each with par $n_0$, default probability $P$ over the horizon, loss given default $L$, and pairwise default correlation $\rho$. The pool loss has mean and variance

$$
\mathbb{E}[\text{Loss}] = J n_0 L P, \qquad
\operatorname{Var}[\text{Loss}] = n_0^2 L^2 P(1-P)\,\big[J + J(J-1)\rho\big].
$$

The BET pool has $\text{DS}$ independent obligors with par $n_0 J/\text{DS}$ each, which preserves total par, so its mean is the same. Its variance is $(n_0 J/\text{DS})^2 L^2 P(1-P)\,\text{DS}$. Setting the two variances equal and solving gives

$$
\text{DS} \;=\; \frac{J}{1 + (J-1)\rho}. \tag{21.4}
$$

(Schmid calls this number the "diversity score of the collateral pool." We write it DS to keep $n$ free for par and $D$ free for duration.) The coins carry over exactly: with $J = 250$ and $\rho = 0.03$, $\text{DS} \approx 29.5$, and as $J \to \infty$, $\text{DS} \to 1/\rho$. Adding names beyond about a hundred buys almost nothing, so managers meet the diversity test and then compete for the same large, liquid, B2/B-rated names that also satisfy the WARF (weighted-average rating factor) and WAS tests and can be sold if needed. The result is heavy overlap. Elkamhi and Nozawa's working-paper title said it plainly: "Too Big to Diversify." The test that makes each CLO diversified makes the CLO *sector* concentrated. When one large borrower is downgraded, it hits many CLO tests at once. §21.4 turns that correlation into a price.

## 21.4 The Tests as an Option Book

Theo, on day one: "At RSSG, CLOs were the lenders who couldn't fund the new money." Ines, on day two: "Here they're the players who must fold when the board shows a CCC. Learn which card makes which player fold, and you don't need to read faces."

> **[SOURCE EXTRACTION]** *Schmid_Credit_Risk_Pricing_Models p.175:* "There are two types of tests (so called coverage tests) that are intended as a warning if the cash flows from the collateral pool are running short to cover interest and/or principal payments to the tranches. If the coverage tests fail, the cash flows from the collateral are redirected. They are used to repay the outstandings on the tranches according to their seniority."
>
> **Annotation.** On p.176 Schmid gives the textbook OC ratio: collateral par divided by the par of the tranche and everything senior to it. He adds that the OC test "is done for every single tranche but the equity tranche." The 2026 indenture keeps the structure and changes the numerator. Par becomes *adjusted* par, with haircuts that depend on prices and ratings. Post-crisis US deals test a combined AAA/AA class and each class down to BB, usually with no test for a single-B tranche *(Creditflux CLO Guide, ch. 6)*. The modern departure is that the haircuts make a par test price-sensitive in exactly the tail of the portfolio where prices are least reliable.

#### Long Scene A: The Cliff, March–April 2020

*Replay, run on Friday 16 October 2026 after the close. Ines cuts the tape at Friday 20 March 2020, then again at the end of April. The desk, its synthetic CLO, the cast's cards and the desk's model runs are fictional; the index levels, the LSTA's reports and the S&P figures are real and cited.*

Ines ran her replays the same way every time, which was part of the point. She printed the tape up to the cut date, blacked out everything after it with a marker that she guarded like a chip stack, and handed each player the documents they would have had on the morning of the cut and nothing else. For this one the documents were a loan index history, two weeks of LSTA market commentary, and a stack of CLO trustee reports with February determination dates. Hana had pulled them from the vendor that morning and stapled them by deal, because the vendor's PDF export put the CCC schedule of one deal behind the cover page of the next.

"Friday, 20 March 2020," Ines said. "Markets close in an hour. You run a loan book. Go."

Mags pushed her chair back from the table. "I was there. I'm not allowed to play." In March 2020 she had been on a bank's distressed desk, and she remembered the month mostly as noise. "I'll keep score."

**Beat one: the tape.** The first page was easy to read and hard to believe. On 29 February the S&P/LSTA index's weighted-average bid had been 95.18. Three weeks later it was in free fall. On 19 March the LSTA reported record volumes and bid-ask spreads that had "widened beyond 300 basis points" *(S&P Global LCD 1Q20 review; LSTA)*. Three hundred basis points of bid-ask on a loan is three points of price between what a dealer would pay and what it would charge, on paper that a month earlier had traded inside half a point. The share of the index priced below 80, the distress ratio, had gone from a rounding error to a large fraction of the market. Theo knew it was a large fraction because he could see the marker strokes where the end-of-month number should be.

In March 2020 Theo had been in his first spring at PJT, and he remembered it as the month the phones never stopped. Every client wanted to know how long its revolver draw would last. Nobody had asked him who was selling the term loan.

"Volume at a record," he said, reading. "So somebody is selling a lot of loans to somebody. Who's selling?"

"That's the right first question," said Ines. "Hold it."

**Beat two: Theo's instinct.** He did what six years of restructuring work had trained him to do in a crash, which was to look for the cheapest paper of a decent business. He went down the trustee reports' CCC schedules with a pencil and circled every loan marked in the forties and low fifties. Retailers, a cinema chain, two energy services names, an airline caterer. Some of them would file. Some would not. All of them were, in his language, fulcrum candidates: the tranche whose recovery would decide who owned the company afterwards.

"These," he said. "If you think the business survives, the cheapest secured paper is where the restructuring value lives. The CLOs hold a lot of it, the CLOs are panicking, so the CLOs sell it to me at forty."

"Are the CLOs panicking?" Ines asked.

"The index is down twenty points."

"I didn't ask about the index."

**Beat three: Kaz's run.** Kaz had stopped listening some time before and was typing. They had the OC engine open, the reference implementation the desk keeps as an answer key (its specification closes this section), loaded with the desk's synthetic deal: \$500mm of par in 250 loans of \$2mm each, 21 CCCs priced evenly from 50 to 92 cents, a CCC bucket of \$42mm against a \$37.2mm limit, so already a little past its 7.5%, and a junior class sitting at 107.41% against a 104% trigger *(the desk's fictional deal; illustrative)*. They marked the whole book to March: every performing loan down about eighteen points, every CCC down twelve.

"Theo's premise is wrong," Kaz said. "Look." The pool had lost about \$85mm of market value. The adjusted collateral numerator had lost about \$0.6mm. "The test can't see the crash. Performing loans are carried at par no matter where they trade. The only prices it reads are the cheapest CCCs, the ones already in the excess, and they got a bit cheaper. The junior cushion went from 3.4 points to 3.3. Nobody is forced to sell anything. The CLOs are fine."

Theo frowned at the screen. "Then why the record volume?"

"Mutual funds, probably. Redemptions." Kaz shrugged. "Not CLOs."

"And when the rating agencies catch up with the prices?" Ines asked.

Kaz had not modeled that, so they did it on the spot, half to prove the point. They moved fifteen of the deal's performing loans, \$30mm of par priced between 80 and 90, into the CCC bucket, the way a wave of downgrades would. Then they reran the numerator and stopped talking.

CCC par went from \$42mm to \$72mm against an unchanged limit, so the excess jumped from \$4.8mm to \$34.8mm. The engine charged that excess cheapest-first, at one minus price, to the loans already sitting at the bottom of the bucket, the ones in the high thirties and forties. The numerator fell by about \$12.7mm. The junior OC ratio fell from 107.3% to about 104.5%, and the cushion from 3.3 points to about half a point *(the desk's fictional run; illustrative)*. None of the \$12.7mm was charged to the fifteen loans that had been downgraded. Every cent of it landed on loans that had done nothing new.

"Huh," said Kaz, which from Kaz was a paragraph.

They had set out to prove that the CLOs would not be forced to sell, and they had proved, by accident, the thing that mattered: the test is blind to prices across almost the whole book and hypersensitive to two things, the cheapest few CCCs and the rating calendar. In a crash, prices fall first. The downgrades come later, in batches, and they arrive at a bucket that is already full.

"So the CLOs weren't selling in March," Theo said slowly. "They'll be selling in April."

Mags, keeping score, said nothing, which Theo had learned meant yes.

**Beat four: the downgrades.** Ines uncapped her marker, crossed out the black bar over the rest of March and handed round the second cut. The index's average bid had bottomed at 76.23 on Monday 23 March, the next trading day after the first cut. March's return was −12.4%, second only to October 2008's −13.2%, and the distress ratio peaked at 57%. Then came the bounce, to 82.9 by 31 March, which a fund that had sold the lows would remember for the rest of its career *(S&P Global LCD 1Q20 review)*.

And then, through April, the downgrades arrived. The rating agencies moved on borrower after borrower whose revenue had just fallen off a cliff for reasons no model had in it. BSL CLO exposure to CCC-range companies climbed toward the peak S&P later measured at 12.31%, against a bucket of 7.5% in most deals, and the average junior OC cushion fell to 1.13% *(S&P Global Ratings, 28 Apr 2023)*. Kaz's half-point synthetic deal was thinner than the average, but not by much, and a meaningful number of real deals were thinner still.

Ines put an exhibit on the table, a trustee-report page she had built for the replay with the deal's name cut out *(illustrative)*, and tapped one line: junior OC cushion 1.1%. Below it, the CCC schedule. At the top of the price column sat a loan that had been rated B− the week before and was now CCC+. It was marked at 88. Below it, in a long tail, were loans in the fifties and forties, the ones Theo had circled.

"Card," she said, and slid one to each of them. "Which loan does a CLO with a 1.1% cushion sell on Monday, at what discount, and who is on the other side? Write the trade, the size and the exit."

Theo wrote fast, because he had been writing the same answer for an hour. *Buy the cheapest CCC from the forced sellers, around 45. Five million. Hold through the restructuring; exit at plan value.* He underlined "forced sellers".

Kaz wrote more slowly. *The deal is charged on its cheapest loans, so it dumps the cheapest loans to get rid of the charge. Buy those. Size small. Exit when the cushion recovers.* Then, after a moment, they added a second line: *Unless selling the cheapest does nothing. Check.*

Mags, who was not playing, wrote something on a napkin, folded it and put it under her coffee cup.

"The reader gets a card too," Ines said to nobody in particular, which was what she said when she wanted Theo to imagine someone watching. "Same three things. The trade, the size, the exit." She collected the cards and put them face down. "We grade them when we've done the arithmetic. Kaz's second line is the arithmetic."

Back at his desk, Theo looked at the loan at 88 for a long time. At RSSG it would have been the least interesting line on the page: a decent business with a bad quarter, a fresh downgrade, a capital structure nowhere near a restructuring. Nobody hires a restructuring banker for that loan. He had a feeling that was exactly why it mattered here.

### 21.4.1 Derivation: the adjusted numerator

> **Math, Gently.** *The test as an option book.* Picture the OC numerator as a landscape drawn over the deal's loans, sorted from richest to cheapest. For the first nine-tenths of the walk it is perfectly flat: a performing loan counts at par whether it trades at 99 or 79, which is why Kaz's March run barely moved. Then, at the bottom of the CCC list, the ground turns into a staircase. Each of the cheapest few CCCs takes away one minus its price, and only as many of them as the bucket overflows. An option trader reads that landscape as a book of short options: a short put on each defaulted loan, struck at the agency's assumed recovery; a digital on each discount obligation, which snaps back to par if its price stays above a threshold for long enough; and a short position in the cheapest tail of the deal's own CCC book. Now a tiny number. A \$100 deal with a 7.5% bucket holds exactly \$7.50 of CCCs, so the bucket is full. One more \$1 loan is downgraded, and it trades at 88. Nothing is charged to that loan. The \$1 of excess goes to the cheapest CCC already in the book, and if that one trades at 58, the numerator loses 42 cents. A slope of zero before the cliff and of minus 0.42 after it, and the price of the loan that actually fell off never appears. The derivation, next, writes the landscape out.

Formally, the adjusted collateral principal amount is total par plus principal cash less three haircuts, equation (21.5), and each class's OC ratio divides it by the notes at and above that class.

#### The Full Derivation

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

**Why it is an option book.** Write each haircut as a payoff on prices. A defaulted loan is carried at $\min(p_j, R^{\text{ag}}_j) = R^{\text{ag}}_j - (R^{\text{ag}}_j - p_j)^{+}$, so the CLO is short a put on each defaulted loan, struck at the agency recovery. A discount obligation's carrying value jumps from $p^0_j$ to 1 when the price stays above the threshold long enough, which is a barrier digital on par. The CCC excess subtracts $(1 - p)$ summed over the *lowest order statistics* of the CCC price vector, so the CLO is short the cheapest tail of its own CCC book.

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

Ignoring the small $\bar c$ term, the OC-optimal cure is to **sell the highest-priced CCC loan**. The gain per unit of par is $p_i - p^{\ast}$. Selling the cheap ones is OC-neutral at best: it just turns a haircut into a realized loss. Kundu calls this "contractual arbitrage." Notice what it means for the market. The highest-priced CCC in a CLO is usually the *freshly downgraded* one: yesterday a B− at 92, today a CCC+ at 88, still well above the 58-cent tail. So the theorem predicts exactly what Elkamhi and Nozawa (2022) measure. Constrained CLOs sell recently downgraded loans, those loans' prices fall temporarily, and because diversity rules make CLOs overlap (§21.3.2), the selling is correlated across deals. **The forced seller sells its best CCC, which is the one a fundamental buyer most wants.** The ex-RSSG reader knows that loan cold: a decent business, a bad quarter, a fresh downgrade, and a capital structure that is not yet a restructuring. Figure 21.3 shows the cliff on the left and the cure trade on the right.

![Figure 21.3: The OC numerator is flat until the CCC bucket fills and then loses 1 − p* per extra dollar of CCC par, charged to the cheapest CCCs already held (left), so the OC-optimal cure is to sell the richest CCC and not the cheapest (right). Illustrative: the synthetic \$500mm deal of Listing 21.1 (right), and a \$500mm deal with no defaults whose \$2mm CCC loans are priced evenly from 50 to 92 cents and arrive cheapest first (left).](assets/figures/ch21_ccc_cliff_and_cure.png)

The magnitudes are large enough to trade. Elkamhi and Nozawa find that loans widely held by constrained CLOs earn 3.4% lower cumulative abnormal returns over the 20 weeks leading to the downgrade, and that the fire-sale price impact of CCC-downgraded loans is −3.35%. Over three months the unconditional probability that a CLO sells a downgraded loan is 13.27%. A one-standard-deviation (3.26%) drop in junior OC slack raises that probability by 1.56 pp. Average downgrade-week price impact was 17.31% in 2008–09, 1.26% in 2010–19 and 4.41% in 2020. Kundu (2023) finds that the median CLO operates within 4% of its most stringent covenant. After the 2014 oil-and-gas shock, she finds, each extra percentage point of a firm's CLO-routed oil-and-gas exposure lowered the secondary price of that firm's *unrelated* loan by 61 bp (IV estimates 81–254 bp). Selling \$1mm moved prices 180–404 bp on an Amihud measure. Loumioti and Vasvari (2019) add the manager's other lever: discretionary fair values and strategic trading around monthly tests. Strategic trading, but not fair-value discretion, predicts worse future CLO performance.

On Monday morning Ines turned the three cards from Long Scene A face up next to (21.6), which by then Kaz had written on the whiteboard where the stochastic integral used to be.

Theo's card went first. *Buy the cheapest CCC from the forced sellers, around 45.* By the theorem's second case, a CLO that sells a loan inside its excess set gains nothing on the test: it realizes in cash exactly the haircut the numerator was already charging. A deal with a 1.1% cushion is therefore under no pressure at all to sell its forties, and any CLO that sold them to Theo did so for its own reasons, at a price with no fire-sale discount in it. "You realized someone else's haircut," Ines said. "They had already paid it on the test. You paid it in cash." Some of Theo's names did recover, and his restructuring instincts about which ones were real. But as a trade against the CLO rulebook his card had no edge, because there was no forced seller on the other side of it.

Kaz's first line made the same mistake for a different reason, and their second line, *unless selling the cheapest does nothing; check*, was the theorem. Half marks, which Kaz accepted with visible relief.

Mags took the napkin out of her notebook, where it had spent the weekend, and unfolded it. *The B− that was 92 last week. Buy it in downgrade week from every thin deal at once. Size to what they have to sell, not to what you like. Out in two months.*

That is the answer, and the theorem says why. The richest CCC in a thin deal is almost always the freshly downgraded one, yesterday a B− at 92 and today a CCC+ at 88, and selling it is the only trade that both shrinks the excess and frees the cheapest loans from their haircut. Every thin-cushion CLO that holds it faces the same arithmetic in the same week, and the diversity rules of §21.3.2 have made sure that many of them hold it. So the other side of the trade is not another CLO; it is a buyer with no rulebook. A systematic desk running FSPI in April 2020 would have seen pressure concentrated in recently downgraded, CLO-heavy names. By (21.6), those were exactly the highest-priced CCCs. The trade was to buy them from the forced sellers and hold through the reversal, sized against the risk that the downgrades kept coming. The discount on offer was the 4.41% downgrade-week impact of 2020 measured above, more than three times the 2010–19 average, and the exit was the reversal, which the Poker Table below times at about eight weeks. If your own card said "the richest CCC, in downgrade week, out by midsummer," give yourself Mags's marks. If it said "the cheapest," you have Theo's.

"So the theorem tells us exactly what they'll sell," Theo said. "We can be there before every test date."

"On paper it's deterministic," Mags said. "In practice it's discretionary." She ticked it off on the napkin. Managers are not robots: Loumioti and Vasvari's managers moved marks and traded strategically around test dates, so a deal can sit on a breach for a month or cure it with a trade nobody expected. Every indenture defines "market value" its own way, as a pricing-service bid, an average of dealer bids, or failing both the manager's own estimate, so the test the trustee runs is not quite the one the desk computes. And a downgrade can land the week after a determination date, which buys the manager a month. "The theorem tells you the direction of the forced sale," she said. "The trustee report tells you whether it's this month. Back in my day we had neither, and we found out from the dealer, who found out first." She refolded the napkin. "This is better."

Moyer's 2004 book, which sat on Mags's shelf with a broken spine, had made the same point in two words:

> **[SOURCE EXTRACTION]** *Moyer_Distressed_Debt_Analysis p.55:* "CDO-ORs typically limit the percentage of the CDO's portfolio that can be rated in the lowest rating categories. When an investment in the portfolio is downgraded to B– or CCC, the manager may be forced to sell something (again without regard to the portfolio manager's view of fair value) to remain in compliance with the CDO-ORs."
>
> **Annotation.** "Sell something" is the entire chapter in two words. Moyer's 2004 insight was qualitative: rating-based rules create involuntary selling, which a distressed investor should expect and exploit. Equation (21.6) makes it specific. The "something" is the highest-priced CCC, the timing is the next test date, and the size depends on the bucket's overshoot and the junior cushion. Two departures from 2004 matter. First, the rulebook is now haircut-based rather than a hard ban, so the pressure is graded, not binary. Second, the CLO share of the market went from about 20% to about 65%, so the forced seller is no longer a corner of the market. It is the market.

The sentence new arrivals to loans say most often is the one Moyer's page was already arguing against.

> **Desk Myth vs. Desk Reality.** *Myth:* "CLOs are buy-and-hold investors, so they stabilize the loan market." *Reality:* CLO *liabilities* are held by buy-and-hold investors. CLO *assets* are traded by a rulebook that turns a downgrade of one borrower into sales of that borrower and, through the cliff, of others. In 2020 BSL CLO exposure to CCC-range companies peaked at 12.31% (S&P, Apr 2023), against a 7.5% bucket. A stabilizer would not have needed a cure trade.

Ines, as always, finished with the hand.

> **Poker Table.** "Most of poker is reading people," Ines said. "This isn't. When a CCC hits the board, the CLO with a 0.9% junior cushion must fold its best CCC hand before the next payment date. I don't need to read its face. I need its trustee report, and I need to know what it holds that is priced highest. The pot is the temporary discount, three points or so. The odds are the reversal rate. Who knows more than you? Nobody: the seller *told* you it was selling, in its indenture, years ago." Then the hand history, as always, through markouts. Buy on the downgrade week at the fire-sale discount. The markout is negative at day 1 because the other constrained CLOs are still selling, flat at week 2, and positive by week 8 if the reversal Elkamhi and Nozawa document arrives. *IDO or it didn't happen*: strip the loan's carry and its beta to the loan index before you call the week-8 markout alpha.

### 21.4.3 The CLO Forced-Sale Pressure Index

The napkin answers the question for one loan in one deal. A desk needs it for every loan in the index, every morning the trustee files land, which means turning "how likely is this deal to sell?" into a number.

> **Math, Gently.** *The logistic as a probability dial.* A probability has to live between 0 and 1, but the things that drive it, such as a cushion or an overshoot, can be any size. The logistic function $\sigma(z) = 1/(1 + e^{-z})$ is the dial that connects them: feed it any number $z$ and it returns something strictly between 0 and 1. At $z = 0$ the dial reads 50%. Turn $z$ far negative and it creeps toward 0; far positive and it creeps toward 1. It is steepest in the middle and nearly flat at the ends, and its slope at any reading $\sigma$ is simply $\sigma(1 - \sigma)$. Here is a tiny number. At a reading of 50%, a nudge of 0.1 in $z$ moves the dial by $0.25 \times 0.1 = 2.5$ points. At a reading of 13%, the same nudge moves it by about $0.13 \times 0.87 \times 0.1 \approx 1.1$ points. At 99% it moves it by a tenth of a point. So a deal that is already very likely to sell, or very unlikely, barely notices a small change in its cushion, and the deals that react most are the ones in the middle. The FSPI writes $z$ as a straight line in the cushion and the CCC excess, and the calibration, next, chooses that line's slope so the dial matches what Elkamhi and Nozawa measured.

#### The Full Derivation

Let CLO $c$ hold par $n_{i,c}$ of loan $i$, whose outstanding amount is $O_i$. Let $\pi_{c,t}$ be the probability that CLO $c$ sells a downgraded holding within three months, given its junior cushion $\kappa^{\text{jr}}_{c,t}$ and its CCC excess $X_{c,t}$ as a fraction of par:

$$
\pi_{c,t} = \sigma\!\left(a - b_{\kappa}\,\kappa^{\text{jr}}_{c,t} + d\,\frac{X_{c,t}}{n^{\text{nd}}_{c,t}}\right), \qquad \sigma(z) = \frac{1}{1 + e^{-z}},
$$

$$
\text{FSPI}_{i,t} = \frac{1}{O_i}\sum_c n_{i,c}\,\pi_{c,t} \;\in\; [0,\ \text{CLO share of } i].
$$

FSPI is the expected fraction of loan $i$ that constrained CLOs will sell. It is Kundu's Bartik-style exposure (holder weights times holder constraints) turned into a live signal. Calibrate $a$ and $b_{\kappa}$ so that $\pi = 13.27\%$ at a 4% cushion and a one-SD (3.26%) drop in cushion adds 1.56 pp, matching Elkamhi and Nozawa. Because $\sigma'(z) = \sigma(1-\sigma)$, that requires $b_{\kappa} = (0.0156/0.0326)/[0.1327 \times 0.8673] \approx 4.16$ per unit of cushion. The CCC-excess loading $d$ is illustrative until you fit it on trustee data. The trade itself is Mags's napkin, scaled up by the index: liquidity provision, bought from the forced sellers and sized by the expected reversal. FSPI adds two refinements. It fires on LME rating events as well as CCC downgrades, always conditional on a fundamental view of the borrower, and ahead of month-end test dates it points at the relative price of the highest-priced CCCs in CLO-heavy names, which is what constrained managers will sell and therefore what to fade.

> **Ways This Blows Up.** (1) *Stale trustee data.* Trustee reports are monthly and lag by weeks, so your cushion is last month's cushion. Nowcast it with the prices of the deal's CCC tail, which (21.5) says is all the numerator can see. (2) *Wrong "market value."* Each indenture defines market value: pricing-service bid, average of dealer bids, or, failing those, the manager's own estimate. If you use a composite mid, you are computing a different test from the one the trustee runs. (3) *Rating mapping.* The CCC classification may use the lower of two agencies' ratings, include B3/B− on negative watch, or treat a selective default differently. Parse the indenture. Do not guess. (4) *Discretion.* Loumioti and Vasvari show that managers move marks and trade strategically around tests. Your model of a deal can be right on the documents and wrong on the manager. (5) *Crowding.* If every desk runs the same FSPI, the reversal is bought before the forced sale completes, and the signal becomes a timing bet against other quants.

### Case Study: COVID-19 2020 and the 2022–2023 Junior-OC Failures

**March 2020** is Long Scene A at the top of this section: the tape, the cliff, the downgrades and the card, graded in §21.4.2. What follows is its coda, three years later, when the same cliff ran in slow motion and one deal's trustee report shows exactly how much of a failure the haircuts can manufacture.

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
- **Episodes & Posts.**
  - **Bull Run in Loans Slams CLO Equity Buyers, Says Eagle Point's Majewski** (*The Credit Edge*, Bloomberg Intelligence, guest Tom Majewski of Eagle Point Credit Management, 2026-07-16). CLOs "face a second straight year of equity losses", and Majewski says "the bigger issue was the bull market" rather than credit problems, i.e. repricing and resets; the 2026 voice for the refinance-or-reset call of §21.3. https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/bull-run-in-loans-slams-clo-equity-buyers-says-eagle-point-s-majewski
  - **Empty Rooms: Masterclass on CLOs at Eagle Point Credit Management (EP.284)** (*Capital Allocators*, Ted Seides with Thomas Majewski, 2022-12-01). A long master class on CLO mechanics and the asset's performance history from the founder of Eagle Point, whom the page credits as likely the first person to refinance a CLO; the 2022 baseline to hear beside the 2026 episode above. https://www.capitalallocators.com/podcast/empty-rooms-masterclass-on-clos-at-eagle-point-credit-management/
  - **Tranche Talk - Navigating CLO trading technicals with Performance Trust's Alex Navin** (*Cloud 9fin*, 2026-03-20). Per the page: how tranches trade in the macro backdrop, triple-A liquidity, the influence of vintage, US-Europe relative value, "uncovered double-B MVOCs" and CLO equity hedges, in a volatility pocket "different to anything we've seen since 2020". A dealer-side read of the secondary tape for §21.4 and §21.5. https://share.transistor.fm/s/3ce13d98
- **Data & Code.** CLO trustee reports via commercial vendors (CLO-i/Creditflux, Intex, Octus); TRACE for CLO tranches; Elkamhi–Nozawa replication package (Mendeley Data).

## 21.5 Repricing Waves: The Borrower Exercises

"Upside in a loan," Ines said, "is a chip the borrower can take back whenever it likes, as long as it waits six months." A repricing is an amendment, not new money. The arranger proposes a lower margin, and often the removal of the legacy CSA. Lenders who consent keep the loan at the new coupon. Lenders who object are taken out at par, or at 101 inside the soft call. For a CLO the loan simply starts paying less, and by (21.3) the equity pays for it at 11×. Ines's replay of the 2025 window, below, shows the machine running at full speed and then stopping.

#### Long Scene B: The Window, January–April 2025

*Replay, run on Friday 23 October 2026. Ines cuts the tape at the close on Monday 7 April 2025. The desk, the loan, the chat log and every desk number are fictional, as is Dov Adler's pod at Vantress Capital Management, a composite client the desk quotes most weeks; the market figures are real and cited.*

"Last week the forced seller was a CLO," Ines said, handing out the folders. "This week it's the borrower. Same table, other side of the felt."

The folders were thinner than the trustee reports had been. A loan index history from December 2024 to the cut. PitchBook LCD's headlines, cut with scissors. Octaura's monthly blotters through March. And two pages Theo had not expected: a printout of the desk's own chat log with Dov Adler's pod, from the third week of January 2025.

**Beat one: the open window.** The tape began at a party. At the end of December 2024 about 62% of the loan market was bid above par. January 2025 then set a monthly record, \$215bn of volume, and about half of it was repricings. Octaura's secondary volume rose 83% on the month. Behind the headline numbers was the sales pitch: banks were calling sponsors with repricings timed to the day each loan's soft call expired, and offering to run them for free *(Bloomberg, 30 Jan 2025)*.

"Free," said Mags, "the way a casino's drinks are free."

"The fee wasn't in the arranger fee," Ines agreed. "It was in the next deal."

The chat log was short. Dov's pod had asked the desk for an offer on \$10mm of a B2 term loan, margin 350 over SOFR, soft call expired in December, and the desk had offered it at 100.4 *(illustrative)*. Dov's last line, sent at 4:12 p.m., was the kind of thing every desk receives fifty times a week: *350 over on a par loan, floating, B2. Carry is beautiful. Done.*

Theo read it twice. "How much of that carry is real?"

"Say more."

"He's quoting the margin. Three-fifty. But the loan's at 100.4 in a month when the banks are offering to reprice everything for free. If the borrower cuts the margin by fifty in March, he doesn't earn three-fifty for a year. He earns three-fifty for six weeks and three hundred after that. And he paid the 0.4 for the privilege."

"So what's the carry?" asked Kaz.

"Something less than three-fifty," Theo said. "I don't know how much less."

"Good," said Ines. "Hold it. That's the question the borrower is asking, too, and it has better information than Dov does."

Kaz had already started writing on a sticky note, which was a sign of interest. *Excess margin times the probability nobody has repriced yet, integrated.* They stuck it on the edge of Theo's screen and said nothing else, which Theo took to mean the integral was coming whether he wanted it or not.

**Beat two: the window shuts.** February looked like January with less noise. Then the headlines changed tone. Repricing activity, in the phrase the quarter's market reviews used, "came to a halt in March." Octaura's March blotter showed 70% of customer inquiry on the sell side. The loans that had sat at 100.25 and 100.5 all winter drifted down through par, slowly at first, the way a party empties: nobody leaves, and then everyone has.

"Who's selling?" Theo asked, because last week that had been the right first question.

"Read the blotter," said Ines.

He did. It did not say. The venue reported a side, buy or sell, not a reason, so Theo reasoned it through out loud. The CLOs had no reason to sell performing B2 loans that were still B2; nothing had been downgraded yet. The sellers in March, he guessed, were the holders with a reason that was not a rating: loan mutual funds and ETFs meeting redemptions, and anyone who had bought above par for carry and now saw the carry and the price going the same way.

Kaz looked at the index line, which had fallen through par and kept going. "So the call expired."

"The call didn't expire," Theo said. "It went out of the money. The borrower still has it. It's just not worth exercising when the loan's below par, because nobody refinances at a wider spread to pay off a loan that's cheap."

"Which means the lender has its upside back," Kaz said. Then, frowning: "On a loan nobody wants."

**Beat three: tariff week.** On Wednesday 2 April 2025 the United States announced its tariff schedule, and the second folder began. Ines read the first week off Octaura's blotter: loan prices down 1.85 points in the first week, with the VIX in the mid-40s. Loan funds were reporting outflows. The ETF wrappers, which settle in one day, were trading loans that settle in twenty.

Mags put her pen down. "This is where I'd want to know which funds have cash and which ones have credit lines."

"You'll get that after the card," said Ines. She crossed out the rest of April with her marker. "Close on Monday the seventh. Dov's loan is at 97." She slid the cards across. "Write what you bid, what duration you think you now own, and what you'll do when the window reopens."

Theo thought about the January chat. Dov had paid 100.4 for a loan that the borrower could take back at 100, which meant, in the language of §21.1, that Dov had bought the bond with the lid on. Now the loan was at 97. Below the lid. He tried to see the bent line Kaz had drawn on the whiteboard a week ago and found that he could: the loan was on the left side of the bend now, where the line was steep.

He wrote: *Bid 96.75 for 5mm. Duration: the full 2.7 on spread, because the call is out of the money and the borrower won't touch a loan below par. Carry: the full 350, because nobody reprices a loan at 97. When the window reopens: the duration gets taken away again above par, so sell into it or stop counting the upside.*

Kaz wrote: *97. Duration 0.25: it's a loan; we computed the one-sided duration in January. Carry 350.* They looked at it, crossed out nothing, and handed it in.

Mags wrote: *95, and more lower down if the funds keep selling. Duration is whatever the redemptions say it is. Exit: when the ETF flows turn.*

Ines collected the three cards without comment and put them under her coffee cup, face down. "And the reader's," she said. "Bid, duration, exit."

"You keep doing that," said Theo.

"Someone's always watching the hand," said Ines.

On the way out, Kaz peeled the sticky note off Theo's screen, looked at it, and put it back. The integral was still coming.

### 21.5.1 Derivation: the price of a loan under a repricing hazard

Kaz's sticky note was still on Theo's screen on Monday: *excess margin times the probability nobody has repriced yet, integrated.* It needs one idea from Part II to become a price.

> **Math, Gently.** *A hazard is a clock that can ring at any moment.* Chapters 5 and 6 drew a survival curve for a borrower that might default: a line that starts at 100% and slopes down, where the steepness at each moment is the hazard, the chance per unit of time that the event happens now given that it has not happened yet. Here the roles flip. The event is the borrower repricing, and the one who loses is the lender, who loses the excess margin. Picture an alarm clock with no hands. It can ring at any moment, and at a constant hazard it has no memory: if it has not rung by June, it is no more likely to ring in July than it was in January. With a hazard of $h$ per year, the chance it has not rung after $t$ years is $e^{-ht}$, and the average wait is $1/h$ years. Now the tiny numbers. At $h = 1$ the chance of still collecting the extra margin after six months is $e^{-0.5} \approx 61\%$, after a year 37%, and the average wait is a year. At $h = 4$, the rate of a wide-open window, the average wait is three months and the chance of still collecting after a year is under 2%. The extra margin is an annuity that stops when the clock rings, so it is worth roughly the margin times the expected time before the ring, discounted. (Chapter 5 owns the exponential distribution and intensities in general; this box borrows them.) The derivation is next, and it turns these clocks into prices.

Formally, the hazard simply adds to the discount rate inside the annuity of (21.2), which gives equation (21.7), and its expected cost to quoted carry is equation (21.8).

#### The Full Derivation

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

The loan loses 2.7 points per 100 bp of widening and gains about a quarter of a point per 100 bp of tightening. It is the bond you would design if you wanted to sell someone convexity and keep the premium. Figure 21.4 draws the kink at par.

![Figure 21.4: A loan gives up 2.7 points per 100 bp of widening but gains only 0.9 or 0.25 points per 100 bp of tightening once a repricing is expected, so the borrower owns the upside. Illustrative: equations (21.2) and (21.7) with expected life T = 3 years, a flat discount rate of 6.65% and the chapter's three worked prices at m − s = 50 bp.](assets/figures/ch21_loan_short_call.png)

**Expected carry loss.** Over a horizon $H$, the margin lost at time $u$ is $(m-s)$ if repricing has happened by $u$, which has probability $1 - e^{-hu}$. Averaging over $[0, H]$ gives the annualized expected give-up:

$$
\mathbb{E}[\text{carry lost}] \;=\; (m - s)\left[1 - \frac{1 - e^{-hH}}{hH}\right]. \tag{21.8}
$$

With $h = 4$ and $H = 1$, about 75% of the 50 bp excess margin, roughly 38 bp, is expected to disappear within the year. Quoted carry on an above-par loan in an open window is mostly fiction.

**The hazard itself.** *(A fictional desk task; the LCD, Loomis Sayles, Guggenheim and CreditSights figures are real.)* Hana had fitted the desk's version in May 2026, as the window was reopening, and the fit is mostly a story about what she had to throw away. She set it up as a discrete-time hazard on loan-months: one row per loan per month, a 1 in the month it repriced, a logit on PitchBook LCD repricing records. The features were the ones the replay had just walked through: price minus par in points; a soft-call-expired indicator and months since expiry; the market's share of loans bid above par, which is the window state; the rating; sponsor ownership; and arranger activity. The window state did most of the work, as the replay suggests it should. The surprise was how much the rating did after it: BBs reprice first, and the fit kept saying so. The tape agreed: in May 2026, month to date, 11 of 15 repricings were BB *(PitchBook LCD)*. Her first run had one column for the coupon, and it could not tell a repricing that cut the margin from one that stripped a legacy CSA, so she split them into *separate* state variables, because a repricing can cut both: $\Delta c = \Delta m + \text{CSA}$. The CLO equity's exposure then follows from (21.3). If a fraction $\varphi$ of the pool reprices by $\delta$, then $\Delta y_E = -\varphi\,\delta / w_E$. In 2025 roughly half the market repriced, but the average nominal coupon fell only about 20 bp *(Loomis Sayles, Q4 2025)*, so the equity lost about $0.20\%/0.09 \approx 2.2$ points of yield a year. Guggenheim estimated that the 2024 repricings cut contractual spreads by 53 bp each, and CreditSights put the typical cut at 40–50 bp.

### Case Study: The January–April 2025 Round Trip, and the 2026 Replay

*The cards from Long Scene B, turned over on Monday 26 October 2026.*

Ines lifted the coffee cup off the three cards and, before turning them, uncapped her marker and read out the rest of April. The month produced \$109.2bn of secondary volume, the second-busiest on record after March 2020's \$119.3bn, and the index's daily average bid "fluctuated 3.5% from crest to trough" *(LSTA; Octaura)*. The share of trading done above par fell to 8%. Underneath, the loan funds were doing what Mags had wanted to know about: in the second week of April they lost several percent of their assets to outflows, against a median cash-like buffer of about 4.5% (§21.6.1 has the Fed's numbers). A week of redemptions had eaten most of a typical fund's cushion, and §21.6 is about what that does to a fund whose loans take twenty days to turn into cash. Then the recovery. By June the above-par share was back to 37%, refinancing and repricing activity hit a four-month high of \$45bn, and the index average bid recovered to 97.6 by 24 July, a "V-shaped recovery" *(LSTA 2Q25 summary)*.

Now the grade, with (21.7) and (21.8) on the board. In January the window share was high, $h$ was large for every loan past its soft call, and (21.7) pinned above-par loans to roughly 100.1–100.5. Quoted carry overstated realized carry by most of the excess margin. That answers Theo's January question about Dov's chat: the base rate and the market spread were real, and the margin above the market spread, the part Dov called beautiful, was the part the borrower was about to take back; at $h = 4$, (21.8) expects three-quarters of it gone within the year. In April the arithmetic ran the other way. Once prices fall below par the call goes out of the money, the loan gets its full 2.7 years of spread duration back, and the excess-carry give-up of (21.8) drops to zero. A buyer in mid-April bought a floater that was temporarily *long* convexity relative to its January self. It earned the recovery at full duration and kept its coupon until the window reopened.

Theo's card said exactly that, and Ines gave it full marks without ceremony, which Theo later realized was the ceremony. Kaz's card had carried January's 0.25 into April. "The one-sided duration isn't a property of loans," Ines said. "It's a property of the window." Kaz wrote *(21.7) is state-dependent* on the whiteboard, underlined it, and did not erase it for a month. Mags's card had the best bid and the right seller: the March and April selling came from wrappers and funds with redemptions, not from rating rules, and her "more lower down if the funds keep selling" is the queue logic of §21.6 in one line. A desk running the hazard model would have cut its expected carry loss sharply in April, added duration to performing B2/B loans that forced sellers were dumping (FSPI was also elevated), and handed the convexity back in June as the window state turned. If your card bid below par, claimed the full spread duration and planned to give the upside back when the loan crossed 100 again, you played Theo's hand. Dov's pod, as it happens, played the wrapper version of it that same week, long a loan ETF against a high-yield ETF, and §21.6 opens that page of his book.

**The 2026 replay.** January 2026 repriced \$108bn. Then the "SaaS-pocalypse" arrived: AI-disruption fears hit the software sector, which is more than 5% of the loan index *(Loomis Sayles)* and, by press reports, more than 30% of many middle-market CLOs *(Octus)*. February–April repricing was only \$11.8bn, the index average bid hit a low of 94.17 in early March, and new-issue spreads were about 50 bp wider than in January. By 11 May, 76% of BB− loans were back at or above par and \$47.2bn of repricings were lined up *(PitchBook LCD via Yahoo Finance)*. The Fed's May 2026 *Financial Stability Report* noted secondary spreads that "increased moderately, reflecting a high concentration of leveraged loan borrowers in the software industry." It was the same machine with a sector-shaped shock, and the same two signals mattered: the window state for repricing, and FSPI for forced sales of downgraded software names.

The replay is told from the lender's chair. The same window looks different from the desk of the manager whose deal holds Dov's loan.

> **View From Another Seat.** *A CLO manager (a generic seat, with one public voice).* To a CLO manager the repricing window is not a ceiling on a price; it is a tax on its equity. Every borrower that reprices 50 bp lower takes, by (21.3), about 5.6 points a year off the yield of the 9-cent slice its equity investors bought, and the manager cannot refuse: a lender that objects is taken out at par and then has to reinvest the cash at the new, lower spread. Its answer is to exercise its own call. Once a deal is past its non-call period, the manager refinances the notes or resets the whole structure (§21.3), cutting the liability spreads the equity pays so that the arbitrage survives the asset spreads the borrowers have just cut. That is why record resets followed record repricings, and why the CLO ETFs became a natural home for the paper: in July 2026, 62.1% of JAAA's collateral by deal vintage was reset deals, 9.0% refinanced-not-reset and 28.9% new issue *(Octus, 7 Jul 2026)*, so the largest ETF's inflows were in good part a bid for exactly the paper that repricing waves create. The manager's own worry sits at the other end of the window. When it shuts, the borrowers that could not reprice are often the ones that cannot refinance either. Loomis Sayles, a large loan manager, wrote in its Q4 2025 loan letter that "we do believe the risk of liability management exercises will remain elevated as not all these maturities are refinanceable." From this seat the borrower's call has two prices: the one it exercises in an open window, and the one it cannot exercise in a shut one, which reaches the CLO as a liability-management exercise and, through §21.8, as a vote.

### Specification for AI Implementation (repricing engine)

*What ROBO built from "price the loan with its call":* a Black-style option on the loan with a strike of 100 and a volatility taken from the bond market. The result priced every loan at 99.7, including ones whose soft call had three months left to run. The precise spec: price = (21.7) when $m > s$ and (21.2) otherwise. The hazard is annualized from a monthly logit with documented features. Margin and CSA are separate. Spread durations are reported one-sided. Asserts check par at $m = s$, the ceiling ordering, and the duration asymmetry.

Theo knows an amendment from the lender group's side of the table. What he never had to do is price that side for several thousand loans before the arranger's email arrives. A screen that ranks loans by quoted spread will happily put first the names about to be repriced away, because the spread that looks fattest is the one the borrower is keenest to cut. For each name the desk needs four numbers: a price that knows about the call, a hazard that says how likely the call is this month, the share of the carry that will survive the year, and what a cut does to a CLO equity holder, who pays for it at eleven to one. ROBO's Black-style option produced none of them, which is how every loan came back at 99.7. The reference chain below is the corrective, and it is short enough to audit in one sitting.

The listing is a short chain in which each function feeds the next. `annuity` is $a(T;\text{rate})$ from (21.2), with a series expansion near zero so a zero rate does not divide by nothing. `loan_price` implements (21.7). It discounts the excess margin at base plus market spread and adds the hazard $h$ to the discount rate only while $m > s$, so with $h = 0$ it collapses to (21.2). `spread_duration` bumps the market spread a hair in one chosen direction and reports the percentage price change per unit of spread. `monthly_reprice_prob` is a logit on price minus par, a soft-call-expired flag, the above-par share of the market and a BB flag, with illustrative coefficients in `THETA`. `annual_hazard` turns a monthly probability into a continuous annual hazard through $-12\ln(1-q)$. `expected_carry_loss` is (21.8), floored at zero when the market spread exceeds the margin. `clo_equity_yield` is (21.3).

The assertions tie the chain to the text. At $m = s$ the price is par. With a 50 bp margin gap and a 6.65% discount rate, the price is 100.12 at $h = 4$, 100.45 at $h = 1$ and 101.36 at $h = 0$. Spread duration at par is 2.72 on widening and 0.25 on tightening. A hot loan (priced 100.5, soft call expired, 60% of the market above par) gets a 38% monthly hazard, a cold one under 0.1%. Expected carry loss at $h = 4$ is about 38 bp of the 50. A 22.5 bp fall in WAS takes 2.5 points off the equity yield, which is the 11× gearing.

Use the chain to price above-par loans, to net expected repricing out of quoted carry, and to read the window state. Do not use the hazard until `THETA` is fit on loan-months, and do not trust the price inside a soft call: the function applies no 101 cap, so at $h = 0$ it returns 101.36 and you must clip it yourself. The edge case that bites is the kink at $m = s$. The call switches on the instant the market spread drops below the margin, so the price has a corner at par. That is why `spread_duration` takes a `side`. A central difference averages the 2.72 and the 0.25 into a duration of about 1.5, which is wrong for a widening and wrong for a tightening.

*The full listing is [Listing 21.3 in Appendix F](#code-21-3).*

> **Trend Watch: the repricing machine, 2024–2026.**
> *2024.* Repricing volume **\$756.8bn**. US institutional loan volume including repricings and extensions was "almost \$1.4 trillion," a record by far (William Blair, *Leveraged Finance Newsletter*, citing PitchBook LCD). About 62% of loans traded above par at year-end (Guggenheim, citing LCD/BofA).
> *Jan 2025.* A record \$215bn month, with repricings 52% of year-to-date volume (Matrix CMG, citing LCD). At its peak the cycle averaged \$52.5bn a month and touched 632 borrowers, 57% of index borrowers (PitchBook LCD, May 2026).
> *Q2 2025.* Repricing fell to a multiyear low of \$28.5bn after the tariff shock. The share of trading activity priced above par was 8% in April and 37% in June (LSTA).
> *FY2025.* Repricing **\$503.6bn**, second only to 2024, and refinancing \$191.8bn. B− new-issue spreads fell to 354 bp in Q4, "the lowest level since the Global Financial Crisis" (William Blair Q4-2025). 58% of loans were bid above par at year-end (Loomis Sayles).
> *2026.* \$108bn of repricings in January. Then February–April produced only \$11.8bn as a software sell-off froze the window. The share of BB− loans at or above par went 13% (end-March) → 59% (end-April) → 76% (11 May) (PitchBook LCD via Yahoo Finance, 15 May 2026).
> *What it means.* Repricing is a regime with two states, window open and window shut, and the share of the index above par is a good proxy for which state you are in. A carry model that ignores the state is wrong by up to 75% of the excess margin, per (21.8).

## 21.6 Loan ETFs vs CLO ETFs: Where Liquidity Transformation Lives

Chapter 20 owns the authorized-participant (AP) mechanics and March 2020. This section owns the loan-side *cause*. Theo's 13-week cash flow model makes its comeback here, reborn as a 20-business-day cash queue. A loan fund is a company whose receivables (sale proceeds) arrive in about twenty days and whose payables (redemptions) are due tomorrow. Theo has seen that company before. It hired PJT.

The wrappers, as of 2026: SRLN (State Street Blackstone Senior Loan ETF) had \$5.38bn of net assets on 15 October 2026, 731 holdings and a 0.70% gross expense ratio. Its holdings are reported on a trade-date basis *including unsettled positions*, which is an ETF wrapper's way of admitting what is inside it *(SSGA fund page)*. BKLN was about \$6.7–6.8bn in mid-2026 *(aggregators; approx.)*. Bank-loan mutual funds held \$71bn at end-2025. Meanwhile US CLO ETFs passed **\$50bn** around the start of July 2026 *(BofA via Octus)*, and JAAA alone passed **\$30bn** on 13 August 2026 *(Janus Henderson)*. Retail money did not leave loans. It left the *loan* and bought the *tranche*, and the reason is settlement.

### 21.6.1 Derivation: the buffer is a queue

> **Math, Gently.** *Twenty coin flips against twenty days of the same bad news.* A random walk is the running total of steps that do not remember each other. Flip a coin twenty times, adding a dollar for heads and losing one for tails. The total wanders, but heads and tails keep cancelling, and its typical distance from zero after twenty flips is not twenty dollars but $\sqrt{20} \approx 4.5$. That square root is the signature of independence: the spread of a sum of $\ell$ independent steps grows like $\sqrt{\ell}$. Now replace the coin with a fund's daily redemptions in a sell-off. Bad news on Monday does not cancel on Tuesday; it repeats, because the same investors read the same headlines and redeem again. If every one of the twenty days brings the same dollar out, the total is twenty dollars and nothing cancels: the spread grows like $\ell$ itself. Real flows sit between the two, and the persistence of the bad news decides where. One more building block, Little's law, gives the average part for free: cash in transit equals the rate at which it leaves times the time it takes to come back. Redemptions of 0.5% of NAV a day *(illustrative)* with a twenty-day settlement cycle mean about 10% of NAV is always on its way back to the fund and unavailable to pay anyone. The fund's buffer has to cover that average plus the wobble, and the wobble is somewhere between $\sqrt{20}$ and 20 times a single day's. The full version is next.

Formally, a fund's cash on any day is its starting buffer minus the outflows of the last $\ell$ days, so the buffer it needs is set by the variance of an $\ell$-day window sum, equation (21.9).

#### The Full Derivation

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

(The running maximum over many windows is larger; simulate it.) The scaling is the point. With i.i.d. flows ($\phi = 0$) the buffer grows like $\sqrt{\ell}$. With persistent flows ($\phi \to 1$), which is what you get in a sell-off, it grows like $\ell$. Applied to a fund, the box's range says a T+20 loan fund needs between $\sqrt{20} \approx 4.5$ and 20 times the buffer of a T+1 bond fund facing the same flows. The Fed's August 2026 note puts the median bank-loan fund liquidity ratio at about 4.5% since 2024, down from about 10% in 2021. In 2–9 April 2025, bank-loan funds with above-median liquidity lost 4.2% of assets and those below median lost 2.7%. That difference is not significant, and it contrasts with March 2020's −6.7% vs −14.2%, which was significant at 1% *(Fed FEDS Note, 19 Aug 2026)*. A week of April 2025 outflows was roughly the size of the median buffer. The rest was covered by credit lines, by dealers willing to settle quickly, and by a quiet trick: unsettled *purchases* leave cash in the fund until they settle, so a loan fund's real cash is larger than its trade-date books show (the Quant-Shop Life vignette later in this section watches an operations team rediscover it). Figure 21.5 plots the buffer against the settlement lag.

![Figure 21.5: With daily flow volatility held fixed, the cash buffer a fund needs grows with the settlement lag, faster the more persistent the outflows, and at the observed lag of about T+20 every curve exceeds the 4.5% median liquidity ratio of bank-loan funds. Illustrative: equation (21.9) with 5 bp of NAV mean daily outflow, 0.40% innovation volatility at φ = 0.4 and a 99% one-sided cut; the 4.5% median is from the Fed FEDS Note of 19 Aug 2026.](assets/figures/ch21_buffer_queue.png)

This is the queue behind the SEC's November 2022 proposal (File S7-26-22). The proposal would have removed the "less liquid" category, where most loans sit, so that loans would likely become "illiquid investments" capped at 15% of an open-end fund. The LSTA said this "effectively shuts down open-end loan funds" and proposed a standardized expedited settlement arrangement (ESA) that would give dealer-to-fund trades settlement certainty by T+3. The ICI noted that in roughly 25 years no bank-loan fund had suspended redemptions. The proposal's fate in the SEC's 2025 withdrawal of pending rulemakings is outside what this chapter verified, and the queue is the same either way.

**The ETF arbitrage band.** An AP that buys ETF shares at a discount $d$ to NAV and redeems them in kind receives loans. It can sell them at once, paying half the bid-ask spread $c/2$ and funding the position until settlement. Or it can warehouse them and bear price risk with annualized volatility $\sigma_L$. The discount it needs before it will act is roughly

$$
d^{\ast} \;\approx\; f_{\text{AP}}\,\frac{\ell}{360} \;+\; \min\!\left(\frac{c}{2},\; z\,\sigma_L\sqrt{\ell/252}\right).
$$

For loans in a March-2020-style stress ($c$ above 300 bp, $\ell = 20$, $\sigma_L = 15\%$), $d^{\ast}$ is at least 1.8% before the bid for size disappears entirely. For an AAA CLO note settling like a bond ($\ell = 1$), it is mostly the half-spread. If loans could move in kind as easily as bonds, the first term would shrink. They cannot, because every in-kind loan transfer is an assignment with consents, so loan ETFs redeem largely in cash and inherit the fund queue (21.9). AAA CLO notes are DTC-eligible securities, so a CLO ETF can redeem in kind and hand the bonds to the AP.

> **Ways This Blows Up.** Take a loan ETF with 4.5% cash that faces outflows of 25% of NAV in one week *(illustrative)*. With $\ell = 20$, it must sell about 20% of NAV in loans whose cash arrives a month later, so it draws its credit line on day 2 and spends the next three weeks as a leveraged loan fund. Its sales are public: the ETF basket and the dealers' axes show them, so every other holder of the same 100 index names front-runs the flow. The fire-sale discount from §21.4 then appears in the *index* names, not the CCCs. This is one reason the March 2020 loan-ETF discounts in Chapter 20 read as a settlement event as much as a credit event.

### Case Study: JAAA, April–May 2025

On 4 April 2025, two days after the tariff announcement, US-listed CLO ETFs swung to discounts averaging more than 1%. JAAA, then about \$20bn and the largest CLO ETF, traded more than 1% below NAV. It recorded its largest one-day outflow, about \$600mm (etf.com's daily flows put 8 April at \$585mm). Janus Henderson said the redemptions were absorbed with "very little impact," which is the manager's framing. In May JAAA took in about \$850mm, the "vast majority" as in-kind creations, and Barclays counted \$663mm into AAA CLO ETFs in a single May week. Total CLO-ETF assets stayed below their Q1 peak for a while *(etf.com, Octus, ETF Trends)*. Then the stack kept growing: more than \$50bn by July 2026, with JAAA about 88% of an eight-fund cohort and holding 62.1% *reset* paper *(Octus, 7 Jul 2026)*.

Read it through the band. A greater-than-1% discount on a T+1 AAA wrapper is not a settlement problem. It is a dealer balance-sheet problem: the AP's half-spread on AAA CLO paper widened for a few days. In-kind redemption let APs take the bonds instead of forcing the fund to sell, so the queue (21.9) never formed. In the same week bank-loan *funds* lost about 3–4% of assets with a 20-day queue and a 4.5% median buffer. Same asset class, same week, different settlement cycle, different plumbing outcome. There is a second-order loop too. JAAA's reset-heavy book means ETF inflows are effectively a bid for CLO resets. Resets lower the equity's cost of liabilities and keep the CLO bid for loans alive, so the ETF stack feeds back, through the AAA spread, into the loan repricing machine of §21.5. Test the cascade (CLO ETF flows → AAA spread → reset count → loan secondary bid) at 2–8 week lags before you trade it. It is a hypothesis, not a result.

#### The Pair: PB-17, BKLN Against HYG (April 2025)

Ines kept the JAAA tape and Dov's pod's April book in the same folder, because they were the same week seen through two wrappers. In the replay of the window, Theo's card had been the loan bid at 97 with the full 2.7 years of spread duration. Dov's pod had put on the version a platform can trade in size on a Tuesday: the loan market against the bond market, each in its exchange-traded wrapper.

> **The Pair.** *Pair Book entry PB-17, Dov Adler's pod at Vantress Capital Management (fictional composite), opened at the close on Tuesday 8 April 2025 and replayed here as Ines's ritual; sizes, ratios, carry and P&L are illustrative, and the spread and Treasury levels are FRED's as Chapters 8 and 10 report them.* **Legs.** Long \$50mm of BKLN; short HYG, sized to match duration times spread on market value. The loan leg's spread duration is about 2.7 now that the call is out of the money (§21.5.1), at a loan discount margin of about 520 bp; HYG's bonds carry a spread duration of about 3.2 at the high-yield OAS of 461 bp printed the day before. That is roughly 1,400 against 1,475 bp-years per dollar, so the short is a little smaller than the long: about \$47.5mm of HYG against the \$50mm of BKLN. **What the hedge removes.** US high-yield spread beta: the part of April that both markets shared, which a platform can buy for a few basis points through an index and will not pay a pod to hold. **The idio that remains.** Loans against bonds in one sell-off, and that is three things at once. A floating coupon against a fixed one. A long whose lid sits at par, out of play in April but back in play the moment the recovery reaches 100, against a short whose bonds' call prices sit well above where they trade, so its upside has no lid to speak of. And two settlement cycles under two NAVs, the loans settling in twenty days and the bonds in one. **What leaks.** First, rates, which Dov left open on purpose because floating against fixed was part of the view. HYG carries a Treasury duration of about three years and BKLN almost none, so the pair is short rates, and the week was violent: the 10-year yield fell 19 bp from 2 to 4 April and then rose 33 bp from 7 to 11 April (Chapter 8, Table 8.3, on FRED's DGS10). Opened on the 8th, the pair caught most of the sell-off and was paid something like half a point to a point on the short leg's Treasury duration, for a reason that had nothing to do with loans *(illustrative)*; a pair opened on the 2nd would have been charged for the rally first. Second, the marks. BKLN's NAV is built from composite loan marks that lag the market (§21.7 shows how much), so the platform's overnight x-ray, which estimated the loan leg's volatility from NAV history, saw a calmer asset than the one the pod owned, and the pair looked better hedged than it was. Third, the wrapper. When the loan queue of (21.9) forms, a loan ETF's price can run below its NAV, which is the settlement lag showing up in a T+1 wrapper; Chapter 20 owns that band. Every day the pod's explain had to choose between price and NAV for the long leg, and the choice moved the "idio" line by more than the day's real idio. **What it costs to carry and to short.** The long earns BKLN's distribution yield, about 8% *(illustrative)*, roughly \$4.0mm a year on \$50mm; the short owes HYG's distributions to whoever lent the shares, about 6%, roughly \$2.85mm a year on \$47.5mm. BKLN's expense ratio is already inside its distribution. HYG sits in a large lending pool and borrows cheaply, tens of basis points a year *(illustrative)*, say \$0.14mm at 30 bp, against a rebate on the short proceeds that roughly pays for the long's financing. Net, about \$1mm a year, or \$80,000 a month, before two half-spreads in and two out on a one-month horizon, which in a week like that one cost a few basis points each on \$50mm. The carry pays the pod to wait a quarter, not a year. **Outcome, graded.** By June the loan index's above-par share was back to 37%, and by 24 July the average bid was 97.6; the high-yield OAS had fallen to 2.96% by 30 June. Both legs rallied together, which is what a DTS hedge is for, and the spread leg roughly washed. What the pod kept was mostly the floating-against-fixed leg it had chosen to leave open, which paid in the second week of April and was not, strictly, the loan view it had written down. What leaked was the week its NAV was wrong: the explain booked the gap between BKLN's price and its lagging NAV as idio on the way down and handed it back on the way up. "IDO or it didn't happen," Ines said, reading the ledger. "Most of what you kept was rates. Write that in the thesis column, or next time it'll be rates against you." The ledger entry, PB-17, is opened, stressed and closed in this chapter.

#### Quant-Shop Life: The Cash That Was Not Spent

*A fictional composite: a systematic asset manager running a loan sleeve inside a multi-asset credit fund. Ilse Varga, her colleagues, the fund, its tickets and every number are invented; the LSTA's delayed-compensation requirements are real.*

Thursday 8 October 2026, 7:40 a.m. Ilse Varga is sixteen months into her first job, as a risk analyst at a systematic asset manager whose multi-asset credit fund holds a loan sleeve of about \$900mm. Every morning at 7:30 the custodian's cash file lands, and at 7:40 a script compares it with the fund's own books. Most mornings the difference is a few thousand dollars of interest booked on different days, which the script labels "timing" and nobody reads. This morning the loan sleeve is off by \$12.46mm, and it is the custodian that has *more* cash.

The runbook says to assume the books are right and the custodian is wrong. Ilse spends forty minutes proving the opposite. The fund keeps its books on trade date: the moment a loan purchase is agreed, the system moves the price out of cash and into the position. The custodian keeps cash on settlement date: the money leaves when the agent bank records the assignment and not a day earlier. Four loan purchases from the second half of September have not settled, and their combined price is \$12.46mm. The fund owns those loans, carries their price risk and accrues delayed compensation on them from T+7, but it has not paid for them, so the money is still sitting in the custodian's sweep account earning the base rate, exactly as the ledgers of §21.2.2 say it should. In cash, the fund is richer than its own report.

Tracing the four, she finds a fifth trade with the opposite problem. A purchase from 3 September, settled last Friday, has had a delayed-compensation receivable of \$31,200 accruing against it since T+7. The agent's funding memo shows zero. The fund's closer signed the assignment on T+6, one day past the T+5 the LSTA's requirements-based rules ask of a buyer, so the seller owes nothing for the delay. The accounting system accrues delayed compensation from T+7 on every purchase without checking who signed when, and for three weeks it has been carrying an asset that does not exist.

At 8:50 she sees why any of this matters before 9:00. The risk committee's morning pack shows the sleeve's liquidity buffer, cash and T-bills as a share of the sleeve, and the buffer is built from the custodian's settlement-date cash: 6.1% this morning. On the trade-date books the same buffer is 4.7%, because the \$12.46mm is already promised to four sellers. Both are right, for different questions. The custodian's number is the cash that could pay a redemption today; the books' number is the cash left once the purchases settle, which they will, in about the time it takes sold loans to turn into cash. And the 4.5% median the Fed publishes for bank-loan funds is built from regulatory filings, whose cash line Ilse has never seen reconciled to either. Three cash numbers for one fund, and the committee has only ever been shown one.

She does not trade anything. She writes the reversal of the \$31,200 for the accounting team, who ask her to resubmit it on the other form. Then she opens ticket OPS-4471, *Liquidity buffer: report trade-date and settlement-date cash side by side; delayed-comp accrual to check assignment signature date against T+5*, and assigns it to the systems team, where it joins a queue that already holds a 2025 request to make the custodian file arrive before 7:30. At 9:00 the committee reads 6.1% and moves on. At 9:04 her manager forwards the ticket with one word: *good*.

### Specification for AI Implementation (liquidity queue)

*What ROBO built from "make sure the fund can meet redemptions":* a buffer equal to the largest one-day outflow in the history file. That is correct for a T+1 fund and wrong by a factor of up to $\ell$ for this one. The precise spec: compute (21.9) analytically, check it against a seeded simulation of AR(1) flows, report the buffer for $\ell \in \{1, 7, 20\}$, and report the arbitrage band for loan and CLO wrappers.

ROBO's buffer, the largest one-day outflow in the history file, is the kind of number that looks conservative and is not. It answers the question a T+1 fund asks, how much leaves tomorrow. A loan fund's question is how much leaves before the first sale settles, which is twenty tomorrows in a row, with outflows that cluster because a sell-off is the one time redemptions are positively correlated. The desk wants that number every morning for the wrappers it trades against, with the settlement cycle as a parameter instead of an assumption. It also wants the closed form checked against a brute-force simulation, because a formula with a double sum of autocovariances is where sign errors go to live. The same listing carries the other half of the section, the discount an authorized participant demands before it will arbitrage the wrapper. So the buffer and the band sit side by side: how much can leave, and how far the price may drift before somebody steps in.

Five small functions and a test harness. `window_var` is (21.9): the stationary variance $\sigma^2/(1-\phi^2)$ times $\ell$ plus twice the autocovariance sum with weights $\ell - k$. It raises unless $|\phi| < 1$, because no stationary variance exists at a unit root. `buffer_needed` is $\ell\mu$ plus $z$ standard deviations of that window sum, with $z$ defaulting to 2.326, a 99% one-sided cut. `simulate_flows` draws seeded stationary AR(1) paths, each started from its stationary distribution so there is no burn-in. `rolling_window_sums` gets every $\ell$-day sum from one cumulative sum. `etf_discount_bound` is the arbitrage band: the AP's funding cost over $\ell$ days plus the smaller of the half-spread and $z\sigma\sqrt{\ell/252}$, the price of warehousing instead of selling.

With illustrative flows (5 bp of NAV a day on average, 40 bp standard deviation, persistence 0.4), the buffers are 1.07% at $\ell = 1$, 4.16% at 7 and 7.77% at 20. The 20-day standard deviation is 6.7 times the one-day, between $\sqrt{20}$ and 20, as the scaling argument says. Simulating 2,000 paths of 260 days and pooling the 241 windows on each, the 99th percentile is 7.86%, within about 1% of the formula. For a loan (1.5% half-spread, 15% volatility, 20 days) the band is 1.78%, and the half-spread is what binds. For an AAA CLO note (0.5% half-spread, 3% volatility, one day) it is 0.32%, and one day of price risk is cheaper than the half-spread.

Use it to size a fund's cash against a settlement cycle, to judge whether a wrapper's discount is wide enough to pull in an AP, and to stress $\phi$, since persistence estimated in a quiet year understates the week that matters. Do not read the buffer as a probability of ruin. The edge case that bites is the window. The buffer covers the 99th percentile of one $\ell$-day window, not the worst window in a year. The simulation check pools windows, so it validates the formula and says nothing about the running maximum, which is larger and grows with the horizon. Add a margin, or simulate the maximum.

*The full listing is [Listing 21.4 in Appendix F](#code-21-4).*

> **Trend Watch: the retail wrapper moved up the stack, 2019–2026.** Bank-loan mutual funds fell 21% to \$71bn, with \$23bn of net outflows over 2019–2025 (Fed FEDS Note, Aug 2026). SRLN was \$5.38bn (Oct 2026) and BKLN about \$6.8bn (mid-2026, approx.). US CLO ETFs grew from about \$38bn (Sep 2025, Deutsche Bank Flow) to above \$50bn (Jul 2026, BofA via Octus), and JAAA passed \$30bn (13 Aug 2026). The first European CLO ETF listed in September 2024. *What it means:* daily liquidity is now being offered on the asset that settles like a bond, and the loan itself is funded by CLOs. The liquidity transformation moved to where the plumbing can carry it.

### Deep-Dive Resource Graph (21.6)

- **Practitioner Writing.** Fed FEDS Note, "Liquidity Transformation Risks in U.S. Bank Loan and High-Yield Mutual Funds: A 2026 Update" (19 Aug 2026): https://www.federalreserve.gov/econres/notes/feds-notes/liquidity-transformation-risks-in-u-s-bank-loan-and-high-yield-mutual-funds-a-2026-update-20260819.html · Janus Henderson, JAAA passes \$30bn (13 Aug 2026): https://www.janushenderson.com/en-us/advisor/press-releases/janus-hendersons-aaa-clo-etf-jaaa-the-worlds-largest-clo-etf-surpasses-30-billion-in-assets-under-management/ · Octus, "Portfolio Analytics Wrap: CLO ETF Manager Strategies Diverge as Total Assets Surpass \$50B" (7 Jul 2026): https://octus.com/resources/articles/portfolio-analytics-wrap-clo-etf-manager-strategies-diverge-as-total-assets-surpass-50b/
- **Episodes & Posts.**
  - **The anatomy of bond ETF arbitrage** (Karamfil Todorov, *BIS Quarterly Review*, 2021-03-01). Creation and redemption baskets for bond ETFs differ systematically from each other and overlap little with actual holdings; this decoupling weakens arbitrage forces but lets ETFs absorb shocks. The shortest primary source for the AP mechanics that §21.6 hands to Chapter 20. https://www.bis.org/publications/anatomy-bond-etf-arbitrage
  - **New Insights from N-CEN: Liquidity Management at Open-End Funds and Primary Market Concentration of ETFs** (Federal Reserve Board FEDS Note, 2023-01-11). Finds a high degree of AP concentration, especially for fixed-income ETFs, at about four active APs per ETF; the empirical count of dealers behind the discount band of the §21.6.1 liquidity queue. https://www.federalreserve.gov/econres/notes/feds-notes/new-insights-from-n-cen-liquidity-management-at-open-end-funds-and-pmc-of-etfs-20230111.html
  - **Janus Is Skeptical of Private Credit's Push Into ETFs** (*The Credit Edge*, Bloomberg Intelligence, guest John Kerschner of Janus Henderson, 2025-04-03). Kerschner says the "skepticism there should be real" about ETFs holding direct-lending assets that are less liquid and untested in a credit downturn, and discusses CLOs and securitized relative value; the wrapper question behind the JAAA case study. https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/janus-is-skeptical-of-private-credit-s-push-into-etfs
  - **Claude Code shook credit. What breaks next?** (*Cloud 9fin*, Dan Mika, Anna Russi and Samantha Stokes, 2026-07-02). Per the page, a software sell-off "still reshaping private credit, BSL and distressed debt", with lenders wary of long-dated refinancings because AI risk "remains hard to price"; the audio companion to the 2026 replay of §21.5. https://share.transistor.fm/s/7a979a47
- **Data & Code.** SSGA SRLN fund page (daily holdings, trade-date basis): https://www.ssga.com/us/en/intermediary/etfs/spdr-blackstone-senior-loan-etf-srln · SEC comment file S7-26-22: https://www.sec.gov/comments/s7-26-22/ · SEC EDGAR (N-PORT holdings; quarterly reporting from Nov 2027 for large funds): https://www.sec.gov/edgar

## 21.7 Trend and Momentum in Loans: Smoothing, Ceilings, and Forced Sellers

Kaz ran a three-month momentum backtest on daily loan marks and got a Sharpe ratio they described as "suspicious in a good way." Ines asked what the marks were made of. "Let's just assume they're prices," Kaz said, and immediately regretted it.

The best academic evidence is real. Beyhaghi and Ehsani (2017) find that a momentum strategy with a three-month formation period earns a premium of 122 bp a month in the secondary loan market. The premium is concentrated in loans of the lowest-rated borrowers. Expected loan returns *decrease* with default beta, and loan and stock momentum are correlated across markets but each carries independent information *(hypothetical, backtested)*. Mählmann reports that value and momentum in industry- and country-level loan indexes predict credit excess returns. Chapter 10 owns time-series trend in general. Between that 122 bp and a trade stand three corrections that only loans need, and the first is the one Ines had just asked about.

### 21.7.1 Derivation: what smoothing does to a mark

> **Math, Gently.** *Smoothing makes a calm series out of a wild one.* Imagine a mark that is half today's news and half yesterday's mark, the way a composite moves when only some dealers bother to update their runs. Feed it a wild true series that alternates +4 and −4 points. The marks come out +2, −1, +1.5, −1.25: the same market, at about a third of the swing. Now feed it a single shock, +6 points once and then nothing: the marks read +3, +1.5, +0.75, +0.375, a run of four straight gains from one piece of news. Two things have happened, and both flatter a backtest. The volatility has shrunk, so any return divided by it looks better; and the one jump has been smeared into a trend, which a momentum signal will happily buy. Neither came from the market. Both came from the pricing service's memory. The full version, which puts exact numbers on the shrinkage and the fake trend and shows how to run the filter backwards, is next.

Formally, a mark that is a weighted average of today's return and yesterday's mark has a lower variance and a lag-one autocorrelation equal to the weight, equation (21.10), and both can be undone.

#### The Full Derivation

Let the true return be $r_t$ (i.i.d., variance $\sigma^2$) and let the mark follow the Geltner smoothing model $\tilde r_t = (1 - \phi)\,r_t + \phi\,\tilde r_{t-1}$ with $0 \le \phi < 1$. Iterating gives $\tilde r_t = (1-\phi)\sum_{k \ge 0}\phi^k r_{t-k}$, so

$$
\operatorname{Var}(\tilde r) = \frac{(1-\phi)^2\sigma^2}{1-\phi^2} = \sigma^2\,\frac{1-\phi}{1+\phi}, \qquad \operatorname{Corr}(\tilde r_t, \tilde r_{t-1}) = \phi. \tag{21.10}
$$

With $\phi = 0.5$, marked volatility is $\sqrt{1/3} \approx 58\%$ of true volatility and the Sharpe ratio is inflated by about 1.7×. Positive autocorrelation appears in a series with none, and short-horizon momentum on raw marks partly rediscovers the smoother. The contemporaneous beta to an unsmoothed factor $F_t$ is $\beta(1-\phi)$. Summing slopes over $K$ lags (Dimson 1979) recovers $\beta(1 - \phi^{K+1})$. Inverting the filter, $\hat r_t = (\tilde r_t - \hat\phi\,\tilde r_{t-1})/(1 - \hat\phi)$, desmooths the series.

**The ceiling truncates winners.** By (21.7), a loan near 100.5 in an open window has almost no price upside. Its "momentum" is carry. Condition the winner leg on headroom $(K_t - P_t)^{+}$, and expect winner momentum to live mostly in discount loans that are far from the call.

**Forced sellers extend losers, then reverse.** Elkamhi and Nozawa's −3.4% CAR over the 20 weeks *before* a downgrade, followed by a temporary fire-sale impact, is a momentum-then-reversal pattern created by CLO rules. It fits Beyhaghi and Ehsani's finding that momentum concentrates in the lowest ratings. The trading rule writes itself: ride loser momentum in high-FSPI names into the downgrade, then flip to the reversal once the forced sale is done. *IDO or it didn't happen*: strip carry, the loan-index beta and the equity lead–lag (stock momentum leads loans; see Chapter 10) before calling what is left alpha.

**Capacity.** With a 72 bp mean bid-ask (50 bp median) and 65% annual turnover market-wide, a monthly-rebalanced long-short that turns over half its book pays roughly 36 bp a month in half-spreads against a 122 bp gross premium *(illustrative)*. And it spends most of every holding period unsettled.

*(The desk's backtest and its numbers are fictional.)* Kaz brought the desmoothed backtest to Ines two days later, with the expression of someone delivering a smaller fish than promised. The Sharpe ratio had gone from 2.4 to 1.1 *(illustrative)*. "The marks had $\hat\phi$ of about 0.45," they said. "Most of the first number was the pricing service remembering last week."

"And the 1.1?" Ines asked. "Is that the market, or a better-behaved opinion of the market?"

Kaz did not know, so Hana pulled the venue tape. Octaura's prints covered only a slice of the names, which is what 7.5% of volume buys you, but on that slice the desmoothed winners and losers moved the way the backtest said, at a little over half the backtest's size. Theo, meanwhile, had done the arithmetic nobody had asked him for: at 36 bp a month of half-spreads against a 122 bp gross premium, the strategy kept about two-thirds of its gross before anyone counted the cost of carrying loans that had not settled.

"Now it's a strategy," Ines said. "Before, it was a pricing service's memory with a Sharpe ratio. Desmooth it, find a print that agrees, and pay the rake before you size it. In that order, because each step is cheaper than the one after it." Kaz wrote all three on the whiteboard, under *(21.7) is state-dependent*, and initialed them.

Manager quality is the fourth thing hiding in the loser leg, and the textbooks have been saying so for twenty years.

> **[SOURCE EXTRACTION]** *Schmid_Credit_Risk_Pricing_Models p.177:* "The quality of the collateral manager is one of the most important but unfortunately only badly predictable factors."
>
> **Annotation.** Schmid cites S&P's 2002 surveillance. Top-decile CDO managers held 0.10% defaulted securities against 13.91% for the bottom decile, with recoveries of 49.49% against 2.55%. For a loan momentum strategy, that dispersion is a cross-sectional factor hidden inside the forced-flow channel. The same downgrade produces different selling depending on *which* managers hold the loan: their cushions, their habits around test dates (Loumioti and Vasvari), and their vintage. Pre-pandemic reinvesting CLOs averaged a 2.76% junior cushion and 7.08% CCC in April 2025, against 3.94% and 5.70% for post-pandemic vintages, as S&P's April 2025 CLO index put it *(S&P CLO Insights)*. Manager quality is still "badly predictable." Manager *constraints* are not, and FSPI is built from constraints.

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

*Thursday 22 October 2026, late afternoon. The scene is the fictional desk's; every quoted phrase and percentage is from Weil, Gotshal & Manges, "CLOs as Restructuring Participants" (May 2024), except the rescue-financing cap, which is from law-firm notes and approximate.*

Theo had printed the Weil memo, "CLOs as Restructuring Participants," because Mags refused to read law-firm memos on a screen ("they're written to be billed, not skimmed"). He read it aloud. She translated each paragraph into the only question she cared about: what can a CLO say yes to?

"'The vast majority of a CLO portfolio – typically in excess of 90% – is required to consist of senior secured debt obligations.'"

"So it can say yes to anything that comes out as a first lien," Mags said, "and no to almost everything else. Write that at the top."

"The manager's 'primary driver' is to get the reinstated first-lien debt rated high enough 'to keep it out of the 'CCC' buckets, which are typically set at 7.5%.' Any excess is haircut in the OC tests and may trigger trading restrictions."

"It votes for a rating, not a recovery. You give a CLO a B− with a worse recovery and a CCC+ with a better one, it takes the B−. You've met that loan." Theo had: it was the one at the top of the price column in Long Scene A.

"Equity received in a restructuring 'may be discounted entirely,' or face punitive treatment as a loss-mitigation loan."

"It can take the equity. It just has to pretend the equity is worth nothing on the test. So it says yes and hates it."

"HoldCo PIK paper must fit a 'PIK Security' bucket of 'up to a maximum of 5%.' Fixed-rate buckets are 'typically sized at 10-15%.' Long-dated buckets range 'from 2.5-7.5%,' with haircuts."

"Five percent of PIK, and the bucket doesn't care how good the PIK is. Ten to fifteen of fixed rate, so a fixed-rate exchange note is a maybe. Long-dated two and a half to seven and a half, haircut. So an amend-and-extend is a yes until the bucket is full, and then it's a no that the indenture says for them."

"Investors now demand transparency on 'snooze-drag' provisions."

Kaz, who had been pretending not to listen, looked up. "Snooze-drag. Is that a sleep study?"

"Close," said Theo. It is the family of amendment terms that count a lender's silence as consent, or drag a minority along with the majority, which is how a CLO that cannot vote for a maturity extension gets extended anyway, often through a scheme or plan. "It's how you get a yes out of someone whose rules say no."

"Last one. Post-2020 indentures let CLOs buy 'loss mitigation' or workout loans tied to an existing position, often funded from interest proceeds. The principal used for rescue financing is typically capped around 1–3%, with extra OC haircuts."

"New money," said Mags. "One to three percent of principal, with an OC haircut for their trouble. That's the whole answer to who funds the super-priority tranche. Mostly not the CLOs."

Theo put the memo down. At RSSG he had built uptier math for majority groups, and he had always counted votes. He had never once counted who could *fund* as well as sign, or whose indenture would turn a yes into a forced sale three weeks later. "So when we built a majority," he said, "we were counting funds that could write a cheque and CLOs that could only sign one."

"And the CLOs knew it," said Mags. "Read the caption on the Serta suit."

**The CLO seat as a state variable.** For tranche $i$, let $\theta_i$ be the CLO share of holdings, $\bar\kappa_i$ the holder-weighted junior cushion, and $\psi_i$ the share of CLO holders whose CCC bucket is already full. A non-pro-rata uptier (Chapter 13) needs a required-lender majority that can both *sign* and *fund*. If $1 - \theta_i > 0.5$, a non-CLO majority is feasible without the CLOs. The excluded minority is then likely to be CLO-heavy, and the Priming Risk Score should rise for that minority. If $\theta_i$ is large, the majority must include CLOs. The deal then has to be "CLO-friendly": a rated first-lien exchange, new money within LML and PIK buckets, and maturity inside the long-dated bucket. A high $\psi_i$ with a thin $\bar\kappa_i$ means the CLOs will accept a worse economic deal in exchange for a better *rating* outcome. Carry $(\theta_i, \bar\kappa_i, \psi_i)$ as inputs to the PRS (Chapter 13) and to the default/recovery mixture (Chapter 14). The ad hoc group, represented by counsel, says in unison that it has always known this. (Cooperation agreements signed in this book so far: the counter overflowed in Part IV. Add one anyway. The CLOs signed this one subject to their indentures.)

The CLO is not the only rule-bound holder in the stack. Above it, buying its AAA and mezzanine notes, sits a holder whose rulebook is published by a regulator, on a calendar.

> **View From Another Seat.** *A life insurer's CLO desk (a generic seat; the rules are the NAIC's, as law firms summarized them).* An insurer buying CLO notes sees the holder-base question from the top of the stack. On 23 June 2026 the NAIC's risk-based-capital investment working group adopted new C-1 factors for CLO tranches, keyed to rating and tranche thickness; its task force followed on 30 June and the Financial Condition (E) Committee on 8 July, effective with year-end 2026 RBC. Under them a AAA CLO tranche carries about a quarter of the pre-tax charge on a AAA corporate bond, while a BB+ tranche carries about 4.8 times the charge on a BB+ bond, 15.1% against 3.15%. A broadly syndicated tranche rated NAIC 2.C or below and 4% thick or less picks up an extra 11.77 points, and its thickness is measured on the deal's latest trustee report; middle-market CLOs are excluded, and residual equity stays at 45% *(Sidley, Jul 2026; Mayer Brown, 1 Jul 2026)*. From this seat the trustee report is a capital document. The same monthly file a desk reads for junior cushions and CCC buckets to build FSPI now decides, at 31 December, whether a thin BB+ costs an insurer about 15 points of capital or about 27. That makes the insurer a rule-bound holder too, on a calendar rather than a downgrade, and if the incentive works as designed the rebalancing of thin below-investment-grade tranches bunches ahead of year-end. For an LMT, the insurer's seat adds a second layer of rules above the CLO's: a restructuring that pushes a CLO's loans into the CCC bucket thins its cushions, and the people who notice first are the ones who own its notes.

Serta is where the CLO seat stopped being theory.

> **Docket Diary.** *Serta Simmons Bedding.* In June 2020 Serta completed a non-pro-rata uptier with a majority of its first-lien lenders (autopsy in Chapter 13). Excluded lenders sued, including in a federal case captioned *LCM XXII Ltd. v. Serta Simmons Bedding, LLC* (S.D.N.Y.). The lead plaintiff's name is a CLO's name, which tells you who was left out. Serta filed for chapter 11 in January 2023 in the Southern District of Texas. On 31 December 2024 the Fifth Circuit held that the 2020 transaction was not an "open market purchase." Those three words remain the most expensive in finance. For this chapter, the point is the holder base. A tranche held largely by rule-bound vehicles produces a majority that can be assembled from the vehicles with the fewest rules, and an excluded minority that cannot respond by funding new money.

### Case Study: Two Holder Bases, One Uptier Proposal

The numbers here are *illustrative*. Take two \$1bn first-lien term loans with identical fundamentals. Both face an uptier proposal that requires \$150mm of new super-priority money.

**Loan A** is 70% held by CLOs and 30% by hedge funds. The hedge funds cannot form a majority alone, so any majority needs CLOs, but the CLOs' rescue-financing capacity is small: at a 2% cap on, say, a \$400mm average deal, about \$8mm each. The structure that clears is an exchange into a rated super-priority first lien, with the new money funded mostly by the hedge funds and a small CLO allocation through the loss-mitigation buckets. The likely outcome is near-pro-rata participation and a smaller excluded minority. The PRS for a CLO holder is moderate. The *forced-sale* risk is high if the exchange is rated SD and then CCC, because the CLOs then hit the cliff of §21.4.

**Loan B** is the mirror: 30% CLOs, 70% hedge funds and SMAs. A 51% non-CLO majority is feasible, funds the \$150mm itself, and has no need to include the CLOs. The likely outcome is a non-pro-rata uptier that excludes most CLO holders. The PRS for a CLO holder is high. The CLO's subordinated claim may be marked as a discount or CCC asset and sold, and that sale is the fundamental buyer's entry point, by (21.6) at the highest-priced end of the CCC book.

A systematic desk ranks every LME candidate by $(\theta_i, \bar\kappa_i, \psi_i)$ and by the non-CLO concentration. Then it asks the RSSG question the model cannot answer: *what does the credit agreement say about open market purchases, pro rata sharing and sacred rights?* The indenture says who must sell. The credit agreement says who can be primed.

#### The Pair: PB-15, Trinseo's Loan Against Its Notes (2023–2026)

*Replay, run on Tuesday 27 October 2026, with two cuts: Friday 8 September 2023 and Friday 17 January 2025. Dov Adler's pod at Vantress Capital Management is a fictional composite and an outside holder, in no group on either side; its sizes, prices and P&L are illustrative, because the desk had no loan or bond prints for these dates. Trinseo's filings, the disclosure statement's recoveries and the excluded lenders' account are real and cited, and that account is an allegation, not a finding. Chapter 13 §13.7.1 tells Trinseo's claims in full; this replay borrows only what the pair needs.*

Loan A and Loan B were Ines's chalk. "Now a real one," she said, "with two holder bases inside one issuer." She put Dov's pod's August 2023 ticket on the table. The pod had paired Trinseo's two most different holder bases: long \$20mm of the OpCo term loans due 2028 at 90, a broadly syndicated loan that the desk's trustee-report model put about two-thirds in CLOs, and short \$8mm face of the senior unsecured notes due 2029 at 60, paper that sat mostly with funds *(all illustrative)*. The sizing was jump-neutral at the pod's assumed recoveries of 70 for the secured loan and 10 for the unsecured notes: a default would cost the long \$4mm and pay the short \$4mm.

The first cut was the 8-K. On 8 September 2023, two SPVs borrowed "a senior secured term loan facility of \$1,077 million," and \$948mm of it was on-lent to OpCo as term loans under the 2017 credit agreement, pari passu with the 2028 loans. No existing lender's consent was required *(8-K, Sept 2023; Ch 13 §13.7.1)*. Theo read the structure twice and drew it, as he would have at PJT, as a claim that counted twice: once through the guarantee and once through the intercompany note, both pari with the pod's long.

Ines slid the card across. "September 2023. The pair is on. Do you keep it after the 8-K? Write what the pair now isolates."

Theo wrote that the pair no longer isolated secured against unsecured recovery. It isolated the 2028 lenders' share of a pari pool that had just admitted a claim counting twice, which was a question about documents and about who would challenge them, and he would cut the long. Kaz wrote that default timing was still hedged, so the pair still did its job, and kept it. Mags wrote one line: *Close it. The trade you wrote down is gone; what's left is a bet on a lawsuit you're not party to.*

The second cut came sixteen months later. On 17 January 2025, about \$447mm of Trinseo's unsecured notes became second-lien notes, the intercompany loan grew by about \$494.5mm to roughly \$1.5bn, and the SPV's intercompany term loans counted as votes toward the majority that approved the changes *(Debtwire's account of the excluded lenders' complaint; Ch 13 §13.7.1)*. The pod's short leg had changed seniority under it. Notes that become secured usually trade up toward the exchange's terms, which is exactly the move a short does not want; the desk had no print to say by how much. Then Ines took the marker off the end of the tape. Trinseo filed on 26 May 2026. The disclosure statement estimated recoveries of 2–9% on the OpCo 2028 term loans, 0% on the 7.625% notes due 2029, the paper the old unsecured notes had become, and 60–78% on the Super HoldCo first-lien term loans. The restructuring support agreement had about 86% of the OpCo term loans, while CastleKnight's excluded group, about 40% of the 2028 loans, sued *(dossier `case_lmt_autopsies_us_2020_2026` §7)*. The two percentages do not fit one denominator, and that is the lesson in miniature: which loans count is the denominator question of Chapter 13 §13.2.

> **The Pair.** *Pair Book entry PB-15, Dov Adler's pod at Vantress Capital Management (fictional composite; outside holder; illustrative sizes, prices and P&L).* **Legs.** Long \$20mm of Trinseo's OpCo term loans due 2028 at 90 (CLO-heavy by the desk's model); short \$8mm face of the senior unsecured notes due 2029 at 60 (fund-held), borrowed through the platform's prime broker. Jump-neutral on recovery-weighted market value at assumed recoveries of 70 and 10, with the CLO Forced-Sale Pressure Index as a covariate on the loan leg, since a downgrade would push CLOs to sell it. **What the hedge removes.** Trinseo's default timing: whenever the filing came, the long's loss and the short's gain were sized to cancel. **The idio that remains.** Relative recovery, secured against unsecured, which the 2023 double-dip turned into a document variable. **What leaks.** The long was diluted by a pari claim that counted twice, so its recovery was no longer a property of Trinseo's assets but of a claim graph the pod could not vote on. The short changed seniority mid-trade, unsecured to second lien in January 2025, gapping against the pod, and still recovered zero. The loan's price came to depend on whether its holder sat inside the 86% that signed the support agreement or the 40% that sued, which is coalition, not credit, and the pod was in neither. And the loan leg's markouts arrived twenty business days late, so the explain saw the dilution weeks after the bond leg had priced it. **What it costs to carry and to short.** The long earned a floating coupon of roughly 8% on \$18mm of market value; the short owed the notes' coupon on \$8mm face and a borrow fee that, in the literature, averages 173 bp in the thirty days before a bankruptcy filing and 245 bp after (Asquith, Au, Covert and Pathak, 2013); financing the long ate most of the rest. Thin positive carry for two years, then negative as the filing approached *(illustrative)*. **Outcome, graded.** On the disclosure statement's numbers the pair *won on paper*: the long recovered 2–9 and the short recovered 0, so the ranking held. In dollars it lost about \$12mm before carry: the long fell from 90 to the low single digits, about \$16–18mm, and the short made \$4.8mm, because the hedge had been sized for a recovery of 70 that went to the Super HoldCo lenders instead. The value was there; it sat in the one leg the pod could not buy.

Ines turned the three cards over. Theo's and Mags's said the same thing in different registers; Kaz's had kept a hedge on a risk that was no longer the risk. "Default timing was hedged," Kaz said. "That part worked."

"It worked perfectly," said Mags. "You were long the fulcrum. The fulcrum moved buildings."

### Deep-Dive Resource Graph (21.8)

- **Practitioner Writing.** Weil, Gotshal & Manges, "CLOs as Restructuring Participants" (May 2024) · Fitch Ratings, "U.S. CLO Indenture Features Explained" · Versana digital voting: https://www.versana.io/
- **Academic Papers.** DeMarco, Liu and Schmidt-Eisenlohr (2020), "Who Owns U.S. CLO Securities? An Update by Tranche," FEDS Notes: https://www.federalreserve.gov/econres/notes/feds-notes/who-owns-us-clo-securities-an-update-by-tranche-20200625.html
- **Episodes & Posts.**
  - **Acadian Sees Quants Moving to Loans, CLOs** (*The Credit Edge*, Bloomberg Intelligence, guest Scott Richardson of Acadian Asset Management, 2026-02-19). Systematic credit expanding into leveraged loans with an issuer-based selection approach that could extend to CLOs, plus alternative data and low-cost portfolio construction; the desk context for the loan-momentum test of §21.7. https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/acadian-sees-quants-moving-to-loans-clos
  - **Boaz Weinstein** (*Money Stuff: The Podcast*, Saba Capital, 2026-03-19). Tenders for OBDC II and SREIT, "private credit NAVs", public versus private BDC discounts and "volatility laundering": the same loans marked smooth in one wrapper and discounted in the other, the live case for desmoothing marks before testing momentum in §21.7. https://omny.fm/shows/money-stuff-the-podcast/boaz-weinstein
  - **CLOs Are Tough to Blow Up, Crescent Says** (*The Credit Edge*, Bloomberg Intelligence, guest John Fekete of Crescent Capital Group, 2025-10-02). Fekete: "You have to work really hard to blow those structures up"; the episode also covers leveraged-loan relative value and the impact of liability management exercises on credit, a practitioner counterpoint to the LME holder-base question of §21.8. https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/clos-are-tough-to-blow-up-crescent-says
  - **Private Credit and Leveraged Loan Markets: Similarities, Differences, and Substitution** (Banegas, Castelo, Degerli, Dobridge and Kennedy, Federal Reserve Board FEDS Note, 2026-08-11). Larger middle-market firms substitute between private credit and the syndicated loan market while smaller ones less so; the official statement of the public-private substitution that §21.8 assumes. https://www.federalreserve.gov/econres/notes/feds-notes/private-credit-and-leveraged-loan-markets-similarities-differences-and-substitution-20260811.html

## 21.9 Desk Debrief

The Finder below maps each idea to where the chapter builds it: the equation, the box that gives the intuition, the scene where someone has to use it, and the listing in Appendix F.

| Concept | Equation | Intuition (box) | Judgment (scene) | Code |
| :-- | :-- | :-- | :-- | :-- |
| Floater short a par call, repriced by a hazard | (21.1), (21.2), (21.7), (21.8) | Math, Gently: *Why a floater sits at par…*, *A bond with a lid* (§21.1.1) and *A hazard is a clock…* (§21.5.1) | Long Scene B, *The Window*, and its graded cards (§21.5); Hana's logit (§21.5.1) | [Listing 21.3](#code-21-3) |
| Delayed comp as forced repo | $\text{DC}_u$ (§21.2.2) | Math, Gently: *Delayed compensation is a repo you did not agree to* | Dealer seat (§21.2); the nine stops (§21.2.1) | — |
| CLO equity gearing | (21.3) | Math, Gently: *Why 50 bp becomes 5.6 points* (§21.3.1) | CLO-manager seat (§21.5) | — |
| Diversity and overlap | (21.4) | Math, Gently: *Two hundred and fifty coins…* (§21.3.2) | Long Scene A, *The Cliff* (§21.4) | — |
| OC test as option book | (21.5) | Math, Gently: *The test as an option book* (§21.4.1) | Long Scene A, *The Cliff* (§21.4) | [Listing 21.1](#code-21-1) |
| Cure trade | (21.6) | Math, Gently: *The test as an option book* (§21.4.1) | Mags's napkin and her judgment (§21.4.2) | [Listing 21.1](#code-21-1) |
| Forced-Sale Pressure Index | logistic, FSPI (§21.4.3) | Math, Gently: *The logistic as a probability dial* (§21.4.3) | Poker Table (§21.4.2) | [Listing 21.2](#code-21-2) |
| Liquidity queue | (21.9) | Math, Gently: *Twenty coin flips…* (§21.6.1) | Quant-Shop Life, *The Cash That Was Not Spent*; PB-17 (§21.6) | [Listing 21.4](#code-21-4) |
| Smoothed marks | (21.10) | Math, Gently: *Smoothing makes a calm series…* (§21.7.1) | Ines and Kaz's desmoothed backtest (§21.7) | [Listing 21.5](#code-21-5) |
| Holder base in an LMT | $(\theta_i, \bar\kappa_i, \psi_i)$ (§21.8) | Insurer seat (§21.8) | The Weil memo read to Mags; PB-15 Trinseo (§21.8) | — |

*Friday 30 October 2026, 6:05 p.m., on the fictional desk.* The loan from the first Wednesday settled on day twenty-seven, after compliance found the beneficial-ownership certification in a folder labeled *2025 – misc*. Theo pinned Ines's card above his screen, all three lines finally filled in. *Worth to us today: the mark, 99.40, plus or minus a half-point nobody prints; a floater short a call that is out of the money below par; plus the delayed comp the dealer has owed us since T+7. Worth to the seller yesterday: less than the 99.75 it took, because a CLO with a 1.1% cushion counts the cash as more test than the loan, and in that currency the loan was worth what its indenture let it buy with the proceeds. Why different: we have no indenture. The gap is the price of someone else's rule, and it is the edge.* Mags read it twice, which from her was applause. Under the three lines Theo had added one more, for himself: *At RSSG I read the credit agreement. Here I read the indenture of the lender.*

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

- **Bull Run in Loans Slams CLO Equity Buyers, Says Eagle Point's Majewski** (*The Credit Edge*, Bloomberg Intelligence, guest Tom Majewski of Eagle Point Credit Management, 2026-07-16). The start-here episode for the chapter: CLOs "face a second straight year of equity losses" because of the bull market in loans, i.e. repricing and resets (§21.3, §21.5). Pair it with his 2022 master class, *Capital Allocators* EP.284, "Empty Rooms: Masterclass on CLOs at Eagle Point Credit Management" (2022-12-01): https://www.capitalallocators.com/podcast/empty-rooms-masterclass-on-clos-at-eagle-point-credit-management/ https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/bull-run-in-loans-slams-clo-equity-buyers-says-eagle-point-s-majewski
- **Tranche Talk - Navigating CLO trading technicals with Performance Trust's Alex Navin** (*Cloud 9fin*, 2026-03-20). A dealer-side read of how CLO tranches trade: triple-A liquidity, vintage, US-Europe relative value, "uncovered double-B MVOCs" and equity hedges (§21.4, §21.5). https://share.transistor.fm/s/3ce13d98
- **Citi Warns of Private Debt Risk as 'Tourists' Are Forced to Sell** (*The Credit Edge*, Bloomberg Intelligence, guest Mickey Bhatia of Citi, 2026-04-30). Forced sellers below "the economic value" and the spread of e-trading to CLOs (§21.2.3, §21.4). https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/citi-warns-of-private-debt-risk-as-tourists-are-forced-to-sell
- **Acadian Sees Quants Moving to Loans, CLOs** (*The Credit Edge*, Bloomberg Intelligence, guest Scott Richardson of Acadian Asset Management, 2026-02-19). Systematic, issuer-based selection moving into leveraged loans and CLOs, the quant-desk frame for §21.7. https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/acadian-sees-quants-moving-to-loans-clos

**Practitioner Writing**

- LSTA, "2Q25 Secondary Trading Monthly Executive Summary" (24 Jul 2025): https://www.lsta.org/content/lsta-secondary-trading-monthly-executive-summary-2q25-secondary-loan-trading-volumes-spike-again-to-a-record-262-billion/ · settlement-study index: https://www.lsta.org/content-category/quarterly-secondary-settlement-data-study/
- **Tackling the complex terrain of CLO secondary trading** (Vitaliy Kozak, Octaura, 2025-09-22). A vendor's problem statement for CLO e-trading (BWIC-driven, manual workflows, no central price visibility); not evidence (§21.2.3). https://news.octaura.com/tackling-the-complex-terrain-of-clo-secondary-trading
- **Investor Diversity and Liquidity in the Secondary Loan Market** (NY Fed *Liberty Street Economics*, 2017-08-09). Average investor types per term loan rose from two (1991) to five (2013); loan liquidity depends on who holds the paper (§21.2, §21.7). https://libertystreeteconomics.newyorkfed.org/2017/08/investor-diversity-and-liquidity-in-the-secondary-loan-market/
- **Private Credit and Leveraged Loan Markets: Similarities, Differences, and Substitution** (Banegas, Castelo, Degerli, Dobridge and Kennedy, Federal Reserve Board FEDS Note, 2026-08-11). The official account of the public-private substitution assumed in §21.1 and §21.8. https://www.federalreserve.gov/econres/notes/feds-notes/private-credit-and-leveraged-loan-markets-similarities-differences-and-substitution-20260811.html
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
