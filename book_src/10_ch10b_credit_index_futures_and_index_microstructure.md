# Chapter 10-B: Credit Index Futures and Index Microstructure

> **Prerequisites.** §10.1.1 (index CDS as the futures-like leg, and Lucía Ferrer's roll-week Tuesday), §10.2.3 (a return series that never crosses two series), §8.6 (the hedge matrix and its Trend Watch on CME's credit futures), §8D.2 (the short-leg menu), §24.3 (four things people mean by "basis") and Appendix D §D.2 and §D.4 (margin, IMM dates, standard coupons). Nothing else. The chapter ships one engine, `index_micro.py`, through Appendix F.

*What is invented, once for the whole chapter: Ines Okafor's desk; Quarry Brook Trend Partners, a futures-only CTA; Lucía Ferrer's firm; the dealer bank's index desk; the bank credit desk of §10B.4; Dov Adler's pod at Vantress with Wen Zhao and Marcus Oyelaran; Kestrel and Halvorsen; and every position, quote, ticket, e-mail and P&L figure inside a scene, all fictional composites and illustrative. The exchanges, index providers, regulators, papers, filings, datasets and dated events followed by a source are real. Much of the public record on listed credit futures was published by the exchanges that earn from them, or in trade press they sponsor, and the chapter says so when it uses those numbers.*

## Cold Open: Four Pots

At 2:47 on Thursday 1 October 2026, ten days after the September roll, a chat window opened on Theo Marsh's second screen with a request he had not seen before. *IBHY, front month, client buys, 160 lots, block. Can you show?*

He did the conversion first, because it was the only part he was sure of. Cboe's iBoxx high-yield future is \$1,000 times the index, so at a level near 185 one contract is about \$185,000 of high-yield exposure and 160 contracts are about \$30 million *(illustrative level)*. The client, an outsourced investment office for a mid-sized pension, had added a line to the chat that Theo read twice: *we have no ISDA and want none.*

Then he looked for the market, and found four.

CDX HY, the new series that had started trading on Monday 21 September, at a price of about 106.9, a spread near 335 bp by the standard model. The IBHY order book, front month at 185.42 bid, thin. HYG at \$80.62, whose own page put its portfolio's option-adjusted spread near 285 bp. And last night's close for the Bloomberg US High Yield Very Liquid index, which CME's and Eurex's high-yield futures follow, at an OAS near 255 bp *(all four illustrative)*.

Three spreads, eighty basis points apart, and a fourth price that was not a spread at all. Theo wrote them on a pad in a column, which is what bankers do when numbers disagree, and the column did not help.

Ines Okafor rolled her chair over, looked at the pad and then at the chat.

"What's the pot?"

"Thirty million."

"Four pots," she said, tapping the column. "CDX is a hundred names in five-year CDS, equal-weighted, nobody's bonds. HYG is about thirteen hundred bonds weighted by size, in a wrapper that trades at a premium or a discount to its own NAV. The Very Liquid index is a thousand-odd bonds that passed somebody's liquidity screen, with a cap on each issuer. And the future you're being asked to sell settles to an index built from HYG's holdings, at one evaluated close on the first business day of the month. None of them is the market. Which one are you being asked to make?"

Theo had spent six years at PJT thinking of a price as a claim on a waterfall: who gets paid, in what order, from what assets, under which document. He saw where she was going and did not like it. "So the price is a claim on..."

"A rule," Ines said. "Somebody's rule. Read it before you quote it."

He quoted it as what it was, an ETF portfolio with a settlement date, hedged in HYG, and showed 185.55. The client paid it at 2:58, about \$20,000 to the desk if the hedge behaved *(illustrative)*, and the ticket left the question this chapter answers: **which rulebook is this price a claim on, and what does that rulebook do on the days you most need it?**

By the end of this chapter you will be able to say what a listed credit future is and who wants one; tell the four index families apart; read volume, open interest, blocks and turnover as a diagnostic; build a positioning feature from the CFTC file without trading a reclassification; price a roll as a series basis and an index against its constituents as a skew; explain the two-tier index market; and choose a pod's index hedge knowing what each choice leaks.

## 10B.1 Three Doors Into One Room

*Quarry Brook Trend Partners is a fictional futures-only CTA in Connecticut. Its people, its documents and its numbers are invented.*

Quarry Brook runs about \$4 billion across 140 futures markets *(illustrative)*, and in April 2025 it found out what it did not own. During tariff week Gil Navarro, the firm's head of research, watched credit spreads gap wider on a terminal he could not trade from. Quarry Brook owned rates, equity indices, currencies and commodities, and no credit, because every way into credit came with a document its compliance officer would not sign.

Gil spent the summer of 2025 trying the doors one at a time, and the order in which they closed explains why listed credit futures exist.

The first door was the ETF. Quarry Brook could short HYG through its prime broker like any stock, and for six weeks it did, in a small pilot. Then the stock-loan desk called: a lender wanted some shares back, most could be re-borrowed at a higher fee, and the rest would be bought in by Friday. Nothing had happened to high yield; something had happened to the supply of borrowable HYG (§8D.2 has the borrow, §20.2 the wrapper). Gil wrote in the pilot's log that the firm's credit position was now sized partly by a lender it had never met.

The second door was CDX itself, the standard instrument for credit trend (§10.1.1), unfunded, cleared and deep: the ISDA SwapsInfo review for the second quarter of 2026 puts average daily volume at \$29.3bn in CDX IG and \$7.6bn in CDX HY, and 99.3% of both cleared. Ruth Abernathy, Quarry Brook's general counsel, priced the door in calendar time: an ISDA and credit support annex with each dealer, a swaps clearing agreement, onboarding to a swap execution facility, and new derivatives policies for the board, because the fund's offering documents said "futures and forwards." Eight weeks, if everyone answered e-mail. It was not a no. It was a project, and Quarry Brook ran 140 markets with five operations staff because every one of them used the same plumbing.

The third door was the one Gil had walked past twice: a listed future on a credit index. It cleared through the FCM the firm already used. It margined in the same account as its Treasury futures, and at CME it margined against them, with offsets the exchange computes automatically (CME's launch announcement, 23 April 2024, as reported by Finadium and The DESK). It needed no ISDA, no borrow to short and no new policy language, because it was a future. What it offered was not a better price. It was a different bundle of frictions.

Credit now has three doors into the same room: a basket of a thousand bonds, an ISDA and CDX, or a listed future. The room is roughly the same, an exposure to the spread of a broad set of corporate issuers. What differs is everything around it: whether a document is negotiated, whether a lender can take the short away, whether the exposure is one leg or two (a total return swap is two, a future one), whether the margin nets against the rest of the book, and what single print the contract settles to. A futures-only CTA does not care that CDX trades fifty times the volume. It cares that CDX has a door it cannot open.

> **Math, Gently.** *What a futures price on a bond index is.* A credit index future is a promise about a number. On a stated date, the exchange will look up the index's official closing level, and the two sides will settle in cash the difference between that level and the price they agreed when they traded, times a multiplier. Cboe's IBHY contract is \$1,000 times the iBoxx index level, the minimum tick is 0.01 (\$10 a contract), and final settlement is at the index close on the first business day of the contract month (Cboe contract specifications). Until then, gains and losses settle in cash every evening as variation margin. Theo's 160 contracts at 185.42 are $160 \times \$1{,}000 \times 185.42 \approx \$29.7$ million of exposure; a fall of one full point in the level costs the holder $160 \times \$1{,}000 = \$160{,}000$, paid that night. There is no coupon leg. Whatever the bonds pay is handled inside the index's own arithmetic and reaches the holder only through the level. That is why the futures price is not the index level. Holding the bonds ties up cash; holding the future does not. So the future's fair price is roughly the index grown at the financing rate to the settlement date, less any income the index level leaves out: $F \approx I\,\big(1 + (r - q)\,T\big)$. For an index that reinvests its coupons, $q$ is zero. With the index at 180.00, three months to settlement and financing at 4%, $F \approx 180 \times (1 + 0.04 \times 0.25) = 181.80$. A trader who compares that future with the index and sees a 1.8-point "premium" has discovered the interest rate. The full version is Appendix D §D.2.

Gil's arrival had been forecast in public. In May 2024 Susquehanna's Andreas McGrath told The DESK that Eurex had approached the firm in 2021 to make markets in its euro investment-grade future, and that he expected users in three phases: asset managers replacing credit beta, then CTAs, then bank CVA and XVA desks hedging under the new trading-book capital rules (The DESK, "The credit futures market," 28 May 2024). By October 2026 the first phase is plainly underway (§10B.5 shows asset managers as the large holders of CME's contracts); the second is Gil's; the third has no public evidence yet. A market maker's forecast is also the order in which it hopes to be paid, which does not make it wrong.

> **View From Another Seat.** *The futures-only CTA (a generic seat; Quarry Brook is fictional).* To this seat the question "is the future a good credit instrument?" is upside down. The trend model wants one more roughly independent market whose price trends, on the same plumbing as the other 140. A CDX contract two basis points tighter that needs eight weeks of documents loses to a future that is wider and thinner but settles like a Treasury contract. The seat also sees a risk the credit specialist misses: an index close it cannot watch being made, from evaluated prices, on a contract whose volume is partly paid for by the exchange (§10B.3). A CTA has lived through contracts that died, and it sizes a new one the way a careful guest eats at a new restaurant: a little, and watching the kitchen.

Gil's first allocation, in October 2025, was 2% of the trend book's risk. The memo justifying it did not mention price once. It listed the documents the firm did not have to sign.

## 10B.2 Four Exchanges, Four Index Philosophies

*Ines Okafor's desk, its model review and ROBO are fictional; the index families, their sizes and their launch dates are real and sourced.*

The Monday after the IBHY block, 5 October, the desk's model review had one item: a request Theo had sent ROBO on Thursday evening, while the block was still fresh. *Build a credit future tracking series so we can see how the future moves against what we hedge it with.*

ROBO had built four.

Kaz Lind had put them on the whiteboard as four columns, and stood beside them like someone handed a menu in a language they had studied but never spoken. ROBO had not misunderstood. Four exchanges list credit index futures in the United States and Europe, and each picked a different index family to settle against, so each sells a slightly different room through its door.

**Cboe** was first, listing IBHY and IBIG on its futures exchange in September and October 2018 (Cboe contract specifications). Its indices are iBoxx benchmarks intersected with the actual holdings of HYG and LQD, so the future tracks the ETF's portfolio. In effect it is the ETF's basket with a settlement date and no premium or discount, since the index is computed from bond prices rather than from the ETF's trading price. Cboe added an emerging-markets sovereign contract, IEMD, in July 2024.

**CME** launched on 17 June 2024, alongside its Treasury complex, with futures on the Bloomberg US Corporate index (investment grade) and the Bloomberg US High Yield Very Liquid index. **Eurex**, which had listed euro investment-grade credit futures since the third quarter of 2021 and euro high yield since late 2022, added US dollar contracts on the same two Bloomberg indices in September 2024. Its deck gives the size of what those indices hold: the US Corporate index had 8,611 bonds from 1,147 issuers, \$7.3 trillion of debt, an OAS of 0.76% and a duration of 6.88; the HY Very Liquid index had 1,102 bonds from 632 issuers, \$1.0 trillion, an OAS of 2.48%, a duration of 2.89 and a 2% cap on any one issuer (Eurex, "Global Credit Index Futures" presentation, October 2026).

**ICE** came last, in December 2024, with four futures on MSCI MarketAxess Tradable Corporate Bond indices (US dollar and euro, investment grade and high yield), whose bonds are chosen from MSCI's broader indices by MarketAxess's Relative Liquidity Scores, with the stated aim of cutting tracking error (ICE press release, December 2024; The DESK, 13 December 2024). In July 2026 ICE agreed to buy MarketAxess for \$167 a share in cash (ICE Form 8-K, 30 July 2026), so the liquidity scores that pick the bonds in ICE's index belong to a company ICE has agreed to own.

Kaz read the third column twice. "Is 'Very Liquid' a defined term?"

"It's an index name," Theo said.

"So nobody can breach it. Liquidity is a state of the world, but 'Very Liquid' is a state of Bloomberg." Kaz underlined it. "Like 'Material Adverse Effect'. It means exactly what the document says and nothing you would guess."

That was, in fairness, correct. The phrase is defined only in Bloomberg's methodology, by size and age screens, and a bond that fails them leaves the index whatever the market thinks of its liquidity that day. It was the first time Kaz's habit of reading market vocabulary as law had been right.

The desk spent most of the hour on why the four columns matter, and the answer is that **index design is the microstructure**. Each design decides three things a trader feels directly.

The first is tracking. A future on the ETF's own holdings (Cboe) tracks the ETF's portfolio and inherits its choice of bonds; a future on a broad Bloomberg index tracks a wider, less liquid set, a better benchmark for an insurer and a worse hedge for an ETF trader; a liquidity-scored index (ICE) narrows the set by a rule that reacts to trading. No independent tracking study exists. CME's own note puts its contracts' annualized tracking error against their indices between roughly 1.6% and 2.5%: the exchange's numbers, unaudited.

The second is forced flow. Each index has a calendar on which bonds enter and leave. The Bloomberg and iBoxx indices rebalance monthly; Cboe's indices follow HYG's and LQD's holdings, so they move when the ETFs' portfolios move; CDX swaps names only at the next semiannual series. A fallen angel leaves an investment-grade bond index at its next monthly rebalance, while a downgraded CDX IG name stays in its series and is simply left out of the next one at the roll. The flows around those dates are mechanical and dated, and a reader who spent years watching bonds between downgrade and default can see them coming. The cleanest published estimate is about CDX: Jennie Bai and Or Shachar at the New York Fed found that an issuer added to CDX.NA.IG widened by about 12 basis points, cumulative and abnormal, over the seven days around its entry (Liberty Street Economics, 30 March 2015). One plausible mechanism is the hedge: dealers who sell index protection buy single-name protection on the constituents, so a new member acquires protection buyers who do not care about its credit.

The third is the hedge you did not choose. CME also lists duration-hedged versions of both contracts, DHB and DHY, which follow Bloomberg duration-hedged indices: the parent index plus short positions in Treasury futures (2-, 5-, 10- and 30-year and Ultra), matched by key rate so that the package has zero option-adjusted duration, as CME describes it. A holder is long carry and spread with the rates stripped out, and in August 2026 DHB was about 60% of CME's credit futures volume (The DESK, 17 September 2026). Kaz asked the obvious question.

"Duration-hedged by whom?"

"By the index provider," Ines said. "It's a rule, Kaz. Nobody holds the hedge. The index says what it would have held."

"Then who owns the part the rule gets wrong?"

Nobody had an answer that was not "you," and that was the answer. The duration-hedged index is a hedge ratio chosen by a methodology document, the object §8.2 warns about: it removes the rate risk the index's analytical duration predicts and leaves the holder the convexity and the regime-dependent rate-spread link of Table 8.2, which no public source measures. §8.6's Trend Watch has the launch history; Exercise 4 measures the residual.

Theo finished the review by adding a fifth column to the whiteboard, headed *CDX*, and one row underneath all five: *settles to*. Under the futures he wrote *an index close, built from evaluated prices*. Under CDX he wrote *the ISDA standard model, a dealer composite and, on default, an auction*. Kaz looked at the row for a while and said it was the first time anyone had shown them the legal layer of an index on one line.

<!-- FIGURE: ch10b_four_families.png (a five-column comparison graphic: Cboe IBHY/IBIG, CME IQB/HYB and DHB/DHY, Eurex USD and EUR, ICE MSCI MarketAxess, and CDX; rows: index family, constituents and weighting, rebalance calendar, what it settles to, launch date. Caption: Four doors, five rulebooks. Sources: Cboe specifications; Eurex deck (Oct 2026); ICE (Dec 2024); CME (Jun 2024, as reported); S&P DJI CDX rules.) -->

## 10B.3 Volume Is Not Liquidity

*Lucía Ferrer's firm (§10.1.1), its PM, overlay and e-mails are fictional; the exchange figures are The DESK's reports of exchange data.*

The e-mail arrived at 3:20 on Friday 9 October, from the PM who had replied "thanks" to Lucía's roll-week ticket in September (§10.1.1). It had a link to a trade-press headline about CME's credit futures volume rising elevenfold in a year, and one line: *Can the overlay's HY beta leg move from CDX to futures now?*

Lucía had learned in September that the first answer to a question about a series is a question about how it was built, so she started with two numbers the headline had left out: average daily volume, the flow of contracts traded each day, and open interest, the stock still held overnight. She put them side by side by exchange, for the month the trade press had been most excited about and the latest month it had reported.

| Exchange | Feb 2026: ADV / OI | Turnover | Aug 2026: ADV / OI | Turnover |
| :-- | :-- | :-- | :-- | :-- |
| CME (IQB, HYB, DHB, DHY) | \$522m / \$689m | 0.76 | \$253m / \$1.61bn (average) | 0.16 |
| Cboe (IBHY, IBIG) | \$435m / \$1.99bn | 0.22 | \$407m / \$2.17bn | 0.19 |
| Eurex (euro contracts) | EUR 110m / EUR 3.1bn | about 0.04 | EUR 105m / EUR 3.44bn | about 0.03 |

*Sources: The DESK, 20 March 2026 and 17 September 2026, reporting exchange data. CME's November 2025 ADV of \$458m was the "11x" headline.*

> **Math, Gently.** *Turnover, or the parking garage.* Think of open interest as the cars parked in a garage overnight and daily volume as the cars that drive in during the day. Turnover is the ratio, $\text{ADV}/\text{OI}$, and its inverse is roughly how many days the average parked car stays. CME in February: $522/689 = 0.76$, so a position lasted about $1/0.76 \approx 1.3$ days on average. Cboe: $435/1{,}990 \approx 0.22$, about four and a half days. Eurex: about 0.04, close to a month, which fits a market described as mostly RFQ and block-sized. None of these numbers is good or bad on its own. A high ratio beside a deep, tight order book is an active market. A high ratio beside a thin top of book, where the size quoted at the best price is small, means the same cars are being driven round the block, and somebody is paying for the petrol. §10B.10's engine computes it by exchange and month.

The DESK's reporting of February was unusually direct. Market sources attributed CME's turnover, and the thin top of book beside it, to rebates paid to market makers; CME declined to specify its incentives and had filed a FOIA confidential-treatment request covering them (The DESK, 20 March 2026). By August the picture had changed shape: CME's ADV had halved and its average open interest had risen about 240% on the year. Lucía read that as the healthier of the two months. Fewer cars were driving in, and far more were parked.

Exchanges paying for liquidity is not a scandal; most new futures contracts are launched that way, and the programs are filed with the regulator. The question for a user is which part of the volume would survive the payments stopping.

> **[SOURCE EXTRACTION]** *CBOT Submission No. 26-429, Exhibit 1, "Credit Futures APAC Market Maker Program" (filed with the CFTC, 31 August 2026):* "In order to be eligible to receive the incentives, participants must quote two-sided markets in the Products, at predetermined average bid/ask spreads and minimum quote sizes during a certain percentage of time-in-market." ... "Upon meeting the obligations, as determined by the Exchange, participants will receive predetermined incentives."
>
> **Annotation.** A price list with the prices removed: the filing says what is bought (two-sided quotes, within some spread, above some size, for some share of the session) and that payment is "predetermined," but not how much. The program runs from 1 October 2026 to 31 May 2027 in designated electronic trading hours, covers CME's credit futures and their Basis Trade at Index Close except the leveraged-loan contract, and cannot be combined with the existing Credit Futures Market Maker Program, which tells you there is one. The start date is an event to study, in the hours covered and the hours not; the end date is a liquidity forecast with a date in it.

Lucía found one more data point she could not explain, and wrote it down instead. Cboe publishes every contract's daily volume and open interest since launch in a plain file (`cfevoloi.csv`, Appendix B). IBHY traded 276,893 contracts in 2022 and 72,429 in 2023, about 26% of the year before; IBIG fell to 49%. No release, article or paper she could find says why. The contract recovered, to 141,817 contracts in 2025 and 168,798 by 15 October 2026, but a market that can lose three-quarters of its volume in a year without a note is a market whose volume is not, by itself, evidence of anything.

So her diagnostic became four numbers instead of one. **Open interest**, because it counts people who chose to hold the risk overnight. **Block share**, because it shows where size actually trades (§10B.4). **Quoted width**, from the exchanges' own sponsored pieces until the desk measures its own: Cboe reported average IBHY and IBIG bid-offers of about 0.05% of price in May 2025, and Susquehanna's 2024 description of the euro IG future put its order book near 10 price basis points against 6.7 for the most liquid euro IG ETF. And **turnover**, as the check on whether the volume was rented.

Her reply went at 5:05. It did not say no. It said the overlay could move a quarter of its HY leg into Cboe IBHY, entering in the week before the quarterly expiry when the contract's volume is thickest (§10B.6), with the desk's own fills measured against the iBoxx close for two quarters before anyone decided about the rest. The PM replied at 5:11: *Why Cboe and not CME, if CME has the volume?* She answered with the table, and the PM did not reply again, which at that firm meant yes.

> **Desk Myth vs. Desk Reality.** *Myth:* Volume up elevenfold means the futures are liquid. *Reality:* Volume is partly a policy variable of the exchange. A turnover of 0.76 beside a thin top of book is flow somebody paid for, and it may leave when the payments do; open interest, block share and quoted width are the market's own vote, and in August 2026 they said the market was real, growing and still small.

> **Trend Watch: Listed Credit Futures, 2018–2026.** *What changed.* Cboe listed IBHY and IBIG in September and October 2018. Eurex listed euro IG futures in the third quarter of 2021 and euro HY in the fourth quarter of 2022. CME launched IG and HY Very Liquid futures on 17 June 2024, with a duration-hedged IG contract (DHB) beside them and a duration-hedged HY contract (DHY) from March 2025. Eurex added US dollar contracts in September 2024, and ICE launched four MSCI MarketAxess contracts in December 2024 (sources in §10B.2). Eurex started a Credit Index Derivatives Partnership Program on 1 August 2025, with Santander, BNP Paribas, Flow Traders, Goldman Sachs, Jane Street, JP Morgan, Morgan Stanley and Susquehanna named as quoters (FOW, 4 September 2025). CBOT's APAC market-maker program runs from 1 October 2026 to 31 May 2027 (CBOT Submission 26-429). *How big.* US dollar listed ADV grew from about \$56m in January 2024 (Cboe alone) to \$398m in August 2025 and about \$660m in August 2026 (Cboe plus CME); open interest from about \$190m to about \$3.8bn, with Eurex adding EUR 3.4–4.0bn (The DESK, monthly reports, exchange data). Part of that growth is new venues arriving rather than the same contracts growing. *What it means for the desk.* Listed credit beta now exists for anyone with a futures account, it is cheap to hold and thin to trade, and every growth figure above was published by, or for, an exchange that earns from it. Appendix C carries the dated entries.

<!-- FIGURE: ch10b_turnover.png (ADV/OI by exchange and month, CME, Cboe and Eurex, Jan 2024 to Aug 2026, with vertical lines at Eurex's program start 2025-08-01 and CBOT's 2026-10-01; CME's Feb 2026 spike at 0.76 annotated. Caption: Turnover by exchange: the cars parked and the cars driven round the block. Source: The DESK monthly reports of exchange data; Eurex in EUR.) -->

*Builds on:* §10.1.1 (Lucía's firm), Appendix B (`cfevoloi.csv`). *Used in:* §10B.9 (capacity), §10B.10 (`turnover`), Appendix C.

## 10B.4 Where the Size Goes: Blocks, the Close and the Basis

*The bank credit desk below, its traders and its client are a fictional composite; the contract rules and block statistics are real and sourced.*

The bank's credit-trading floor keeps its ETF trader and its credit-futures trader at adjacent desks with one P&L between them, an arrangement that turns every client ticket into a negotiation between two people who sit close enough to hear each other sigh. On Thursday 8 October Yusuf Adeyemi, on the ETF side, took a call from an asset manager who wanted to swap \$100 million of HYG into IBHY and wanted the swap priced at the index close, so that the fund's benchmark and its position would be marked at the same instant.

Clara Lindqvist, on futures, did the arithmetic before Yusuf hung up: some 540 IBHY contracts, against a quiet month's 6,900 to 11,000 in total, a few hundred a day (Cboe daily file). The ticket was more than a whole quiet day's lit volume, and walking it through the order book would have been a public announcement with a price impact attached.

So it did not go through the order book, and neither does most size in this market. On Cboe's futures exchange it went as an exchange of contract for related position, in which the client hands the bank its HYG and takes 540 futures at an agreed difference. Cboe's rules require the related leg to be an ETF or a total return swap, and a block needs at least 50 contracts (Cboe rules, 2023). CME offers the same service as a Basis Trade at Index Close, in which the two sides agree a basis now and let the index close set the price. Eurex calls its versions Trade at Index Close and EFP-I, an exchange of futures for an ETF or a bond basket. Yusuf's desk would sell or redeem the HYG; Clara's would own the short futures until the basis converged.

The block statistics come almost entirely from exchange-sponsored pieces. Cboe reported blocks above \$1 billion a month in July and August 2026, about a third of IBHY volume and just under 40% of IBIG; its "electronic" bucket does not add up to IBHY's \$5.4 billion traded that month, so its split is partial (The DESK, sponsored, 2026). Eurex reported 1,604 blocks worth over EUR 41 billion through September 2026, with 47% of euro IG block notional printed within 2.5 cents of mid (Eurex-sponsored piece, The DESK, 12 October 2026). CME's February 2026 blocks were three, under 1.5% of \$4.4 billion of notional, which fits the paid-for order-book turnover of §10B.3.

Then Clara made the point the ticket was really about. Every contract on every exchange settles to one number: the index provider's closing level, built from evaluated bond prices at the end of the day. The swap at the close was priced off that number. So was the fund's benchmark, so was the final settlement of every future, and so, for the bank, was the P&L of the basis it had just taken on. One print, made once a day, from prices that are partly models.

How good is the print? Andreas Rapp, Sean Shin, Xing Zhou and Qifei Zhu ("When Delayed Spotting Meets Delayed Reporting: Distortions in the Corporate Bond Index Close," SSRN, December 2025) study trades agreed as a spread whose dollar price is fixed only later, when the Treasury yield underneath is "spotted". Those trades execute at stale prices, about 19 basis points away from trades done at the same time without the delay, and because they are reported late they bias the end-of-day price estimates that index providers' evaluated prices are built on. The distortion grows with intraday volatility and moves together across bonds, which is the worst possible property for an index close: it does not average away inside a basket of a thousand bonds. A desk that settles futures, swaps ETFs and marks a basis to that close holds a small, correlated position in the quality of its construction.

Yusuf priced a few cents of extra width for exactly that, and the client accepted, which told both traders it had read the same paper. Chapter 20 has the ETF's arbitrage band (§20.3) and monitor (§20.7); the futures corner of that triangle has no public band data, and building one starts with §10B.10's settlement series.

*Builds on:* §20.2–§20.3 (NAV and the band), §22.2 (TRACE reporting). *Used in:* §10B.8 (the futures leg of a pair settles here), §10B.9.

## 10B.5 Reading the CFTC File

*Lucía's firm, Bram Velde, the feature, the backtest and the e-mails are fictional; the CFTC positions are from the public dataset, and the reclassification reading is the book's inference from them.*

Until 2026 the listed credit market had no public positioning data. Then the CFTC's weekly Traders in Financial Futures report, which splits each contract's open interest into dealers, asset managers, leveraged funds and others, started carrying CME's two outright credit contracts: "Bloomberg HY Credit Futures" (HYB) from the report of 31 March and "Bloomberg IG Credit Futures" (IQB) from 5 May (CFTC public reporting API, dataset `gpe5-46if`). Cboe's iBoxx contracts are not in it under any name, and neither is CME's duration-hedged pair.

Bram Velde, the data engineer who sits beside Lucía, spent the week of 12 October doing what that sentence hides. The report is dated Tuesday and published the following Friday, so a feature built on it is three days stale on the day it exists. The API pages at a thousand rows, and the field names are long enough that Bram kept a dictionary of them taped to his monitor. Credit contracts appear in the file only while enough large traders hold them, and the HY contract simply stops after the report of 15 September, so the feature has a hole where the most recent month should be. Twenty to twenty-five reportable traders sit behind each contract (The DESK counted 24 and 23 on 7 July), which means a single fund can move a category.

The file shows a pairing of hedgers and levered funds. On 5 May, in IQB, asset managers held 1,369 contracts long and 6,656 short; leveraged funds held 3,006 long and 1,026 short; dealers were net long about 3,400; open interest was 7,924. By 13 October asset managers were 1,734 long and 4,296 short and leveraged funds 4,874 long and 2,835 short, with dealers about flat. In HYB the May pairing (asset managers net short about 3,200, leveraged funds net long 3,054) had unwound by September, with leveraged funds net short from mid-July and dealers holding a small net long (all from the CFTC dataset).

Bram's feature was the asset managers' net short as a share of open interest, and his first backtest, on the twenty-three weekly observations IQB had produced, came back with a correlation to the next week's index return that made him walk the laptop over to Lucía's desk. She asked to see the best week first, because the best week is where a backtest keeps its secrets.

It was 14 July. In that report about 4,400 contracts of IQB net short left the asset-manager bucket and appeared in the dealer bucket, while open interest barely moved. Nobody had sold anything. A trader, or a few, had been reclassified: the CFTC assigns each reportable trader to one category by its predominant business, and when the assignment changes, the whole position walks across the table in one week. The feature had read a change of label as a change of mind, and the following week's return had happened to cooperate.

The fix was a structural-break filter. A week in which one category's position jumps by more than a set share of open interest, an opposite jump of similar size appears in another category, and open interest itself moves by less than a few percent is flagged as a probable reclassification, and the feature is spliced across it rather than differenced through it. Lucía recognised the shape at once. It was her September roll-date phantom (§10.1.1) in a different file: two things with the same label on either side of a date, and a pipeline that subtracted one from the other.

At 4:40 she wrote the e-mail.

*Positioning feature from the CFTC file (IQB, HYB): not ready. The backtest's best week, 14 July, is a reclassification of about 4,400 contracts from asset managers to dealers with open interest unchanged, not trading. With a break filter the sample correlation falls to roughly zero on 23 weeks, which is also what 23 weeks can tell us. HYB has no reports after 15 September. Cboe's contracts are not in the file. Proposal: keep collecting, filter breaks, revisit at 52 weeks. No position affected.*

The PM wrote back "thanks," which was progress: in September the reply had come with a question.

> **View From Another Seat.** *The insurer or asset manager that is net short in the file (a generic seat).* A crowding model that reads "asset managers short 6,656 IQB contracts" as a bearish bet has the motive backwards. An insurer or long-only manager holding \$5 billion of investment-grade bonds who sells futures is hedging what it already owns, often for a quarter, often around cash it has not yet invested. Its short is a temporary reduction of a long, and when the hedge comes off its buying says nothing about its view either. The leveraged-fund longs opposite may be directional, one leg of a basis against CDX or an ETF, or relative value; the file cannot tell them apart. A positioning signal here is a signal about who is hedging: real information about future flow, almost none about future value.

The same week, on Ines's desk, Theo pulled the same public file up for Mags Dunleavy, because he thought she would enjoy the reclassification. She did.

"Back in my day positioning was what a salesman told you at dinner," she said, "and he was lying, and you knew he was lying, and you still paid for dinner." She scrolled to the dealer bucket. "This one lies once a week, in public, with a date on it, and you can catch it." She handed the phone back. "That's an improvement. Don't tell anyone I said so."

> **Ways This Blows Up.** *(1) The index close as a single point of failure.* Every futures contract, every swap at the close and every basis the desk marks to it settles to one evaluated print a day; a correlated distortion in that print (about 19 bp on the delayed-spot trades Rapp, Shin, Zhou and Zhu study) is a loss shared by every position the desk thought was hedged. *(2) The duration-hedged residual nobody measures.* DHB and DHY remove the rate risk their methodology predicts; convexity and the moving rate-spread correlation of §8.2 stay with the holder, and no public source sizes them. *(3) The reclassification jump.* A 4,400-contract move between categories with open interest unchanged is a label, not a trade; a pipeline that differences through it will find its best signal on the day the regulator tidied its records.

*Builds on:* §10.1.1 (the roll-date phantom), Appendix B (the CFTC API). *Used in:* §10B.9 (crowding), §10B.10 (`tff_net`), Appendix C.

## 10B.6 The Roll: Twice a Year the Index Changes Identity

*The dealer bank, its index desk and Rafael Quist are a fictional composite; the roll dates, clearing volumes and research findings are real and sourced.*

On Monday 21 September 2026 Rafael Quist got to the dealer's index desk at 6:10, because roll day starts before the market does. The index administrator, S&P Dow Jones Indices, had dated the September roll for Monday, the 20th having fallen on a Sunday, and the new series of CDX IG and CDX HY, the forty-seventh of each, started trading that morning (S&P DJI, CDX roll notices for September 2026).

A protection buyer who wants to stay on the run sells the old series and buys the new one, and so does every other holder that morning. Rafael's job was to quote that switch as a single price, the roll, and absorb whatever the clients did not net out among themselves. On a normal day his scarce input is attention. On roll day it is balance sheet: every client roll he takes leaves him long one series and short the other until somebody takes the other side, and the clearing house charges initial margin on both legs while he waits.

The roll is a price because the two series are different instruments. The old series, launched in March, matures on 20 June 2031; the new one on 20 December 2031, six months longer on a curve that normally slopes upward. And its names differ: issuers that no longer qualify (a downgrade out of the index's rating band, a merger, a default) are left out and replacements come in under the administrator's published rules. So the new series trades at a different spread from the old one on the same morning, and the difference has a name, the **series basis**.

> **Math, Gently.** *The series basis: six months of curve plus a change of guests.* Picture the index as a dinner table with a hundred seats and a reservation that ends on a fixed date. On roll day a new table is set: the reservation runs six months longer and a few guests have been replaced. Each change has a price. First, the curve. If five-year protection on the average high-yield name costs about 15 bp more for each extra half-year of maturity *(illustrative)*, the new series is about 15 bp wider on that account alone. Second, the guests. Suppose one name trading at 1,200 bp leaves and a replacement at 350 bp joins, each with a one-hundredth weight. The index loses $(1{,}200 - 350)/100 = 8.5$ bp of spread. The new series is about $15 - 8.5 = 6.5$ bp wider than the old *(illustrative)*. In investment grade the same arithmetic is smaller: perhaps 3 bp of curve, and a 250 bp name replaced by an 80 bp one at a weight of 1/125 for $-1.4$ bp, a series basis near $+1.6$ bp. The roll quote is this number plus the dealer's charge for absorbing the imbalance; §24.2 has the index's legs.

By 7:30 Rafael's screens showed what clearing data always shows: index volume comes in waves around the roll. In 2025 Clarus found cleared USD CDX volume peaking on 22 September, five days after the 17 September IMM date (Clarus, "CRD volumes at the end of Q3 2025," 5 November 2025). ICE Clear Credit's largest week since its launch came at the September 2021 roll: over \$3 trillion of notional, counting both sides, in the week ending 24 September, \$1.3 trillion of it for clients. Against the \$9.2 trillion ICE reported for the quarter that looks like about a third, though the two figures may not count the same things (ICE, CDS clearing 3Q 2021 update), so treat "about a third" as a shape, not a statistic. Chapter 10 §10.2.3 cites 25–50% of quarterly notional for the roll window; we found no source for that range, and the ICE week should stand in its place.

The listed futures have a calendar of their own. Cboe's quarterly contracts settle on the first business day of the month, and volume piles into the week before: it clustered on 24 August 2026, 26–27 May 2026 and 24–25 November 2025 (Cboe daily file). Eurex's credit futures settle at the index close on the third Friday, which in September 2026 was the 18th, the last business day before the CDX roll, and its roll months run about three times other months' volume (Eurex deck). The cheapest weeks to move credit beta in size are the weeks everyone else is rolling, and the dealer balance sheet is the one input they all share.

<!-- FIGURE: ch10b_roll_window.png (daily IBHY and IBIG volume from Cboe's cfevoloi.csv, Jan 2025 to Oct 2026, with quarterly expiries and the 20 Mar / 21 Sep CDX roll dates as vertical lines; shading on the five business days before each expiry. Caption: Liquidity has a calendar: listed credit volume clusters in the week before quarterly expiry, near but not on the CDX roll. Source: Cboe cfevoloi.csv, computed.) -->

> **View From Another Seat.** *The dealer's index desk in roll week (a generic seat).* The client sees the roll as a chore with a bid-offer. The dealer sees a week in which every client wants the same trade at the same time, made possible only by its capital, its CCP margin and its risk limits. The roll price carries a charge for that balance sheet which has nothing to do with credit, largest when clients are most one-sided, as after a sell-off when protection buyers roll and few sellers do. A dealer that quotes the roll tight on Monday to win the flow is betting it can lay the imbalance off by Wednesday. Some years it can.

Old-series positions do not disappear at the roll; they go quiet, and their marks come from fewer quotes. Chapter 8-C's stale-series morning (§8C.6) is what that looks like on the explain, and Lucía's spliced history (§10.1.1) is what it looks like in a backtest: a series basis booked as a market move.

ROBO supplied a third version the week after the cold open. Theo asked it to rebuild the desk's CDX HY hedge P&L over the last ten rolls and, at each roll date, to "roll the position." ROBO closed the old series and opened the same notional in the new one at the same spread, because the spec said nothing about the spread being different, and booked the series basis times the risky duration at every roll: \$410,000 of P&L that had never existed *(illustrative)*. The spec that replaced it names the series on every row, takes the roll date from the administrator's notice, rolls at the observed old and new prices, and carries a separate *series basis* line on roll day (§8C.2).

Under the series basis sits an older gap, between the index and its own ingredients: an index CDS is economically a portfolio of single-name contracts, so its fair spread can be rebuilt from theirs.

> **Math, Gently.** *Intrinsic value, and the skew.* If the index is a portfolio of names, its fair spread is an average of their spreads, but not a simple one. A name trading at 400 bp has a shorter risky duration than one at 60 bp (it is more likely to stop paying early), so each basis point of its spread is worth less. Weight each spread by its risky duration $D_i$: $s^{\text{intr}} = \sum_i D_i\,s_i \big/ \sum_i D_i$. Take a five-name toy index with equal notionals, spreads 60, 80, 100, 150 and 400 bp and risky durations 4.6, 4.5, 4.4, 4.2 and 3.6. The products are 276, 360, 440, 630 and 1,440, which sum to 3,146; the durations sum to 21.3; so $s^{\text{intr}} = 3{,}146/21.3 \approx 147.7$ bp, below the simple average of 158 bp, because the widest name carries the least duration. If the index itself is quoted at 143 bp, the **skew** is $143 - 147.7 = -4.7$ bp: the index is tighter than its ingredients. A desk that buys index protection at 143 and sells protection on all five names at their own spreads would lock that gap in, less five bid-offers, six margin calls and the risk that the gap widens before it closes. §24.3 places it among the other meanings of basis.

> **[SOURCE EXTRACTION]** *Bai and Shachar, "The Effects of Entering and Exiting a Credit Default Swap Index," Liberty Street Economics, Federal Reserve Bank of New York (30 March 2015):* "the value of a replicated portfolio will be the duration-weighted average of the constituents' spreads" ... "the basis usually teeters around zero" ... "the difference reached 60 basis points in absolute value" ... "Yet the spread of the index 'jumps' at the time of the roll."
>
> **Annotation.** Three desk facts in four fragments. The skew sits near zero because index arbitrage keeps it there when dealers have balance sheet; it reached 60 bp in 2008–09 because they did not; and the roll is a discontinuity in the generic series, which is why §10.2.3 builds returns inside one series. A 2026 desk adds the futures: a bond-index future has its own "intrinsic," the index close, and its own skew to CDX, and nobody publishes either.

Mags had a view, as she does on anything with a methodology document. "Back in my day," she told Theo when he showed her the roll notices a week later, "the index was a fax from a dealer with the names crossed out in pen. At least you knew who crossed them out." She looked at the S&P notice for a while. "This is better. It's still somebody crossing out names."

The most famous skew of the last fifteen years belonged to one position. In the spring of 2012 the financial press reported that one bank's trading in an old investment-grade series had pulled that series away from its constituents, and that hedge funds were trading the gap against it; the Senate's case history (*JPMorgan Chase Whale Trades*, 15 March 2013) is read as an explain in §8C.7. The skew is usually a few basis points of plumbing. When it is not, somebody's balance sheet is the reason, and the skew measures how large that balance sheet has grown against the market's capacity to arbitrage it.

<!-- FIGURE: ch10b_index_vs_intrinsic.png (stylised skew series for the chapter's five-name toy index: duration-weighted intrinsic against a quoted index level over a year, with a roll-day jump and an inset of a 2008-style 60 bp blow-out. Caption: An index and its ingredients: usually a few basis points apart, 60 bp apart in 2008–09. Illustrative; magnitudes from Bai and Shachar (2015).) -->

*Builds on:* §10.1.1 and §10.2.3 (the spliced series), §8C.2 and §8C.6 (the series-basis line; the stale old-series mark), §24.2 (the index's legs). *Used in:* §10B.8 (PB-01's roll line), §24.3 (the fifth basis), Appendix D §D.4 (IMM dates).

## 10B.7 Two Tiers and the Few-Dealer RFQ

*Ines's desk, the client and every price below are fictional and illustrative; the two papers and the swaption statistics are real.*

Later on the afternoon of the IBHY block, a real-money client with an ISDA sent an RFQ for \$25 million of CDX HY protection to three dealers. Ines's desk won it, selling protection at an index price of 106.80. In the same minute the interdealer screen showed the series trading at 106.86. He put the two numbers side by side and asked why a client pays six cents more than a dealer for the same risk.

> **Poker Table.** "Same cards, different player," Ines said. "When a dealer sells to a dealer, the buyer is usually rebalancing its own inventory, and the price goes back where it was. When a client buys protection, the client often knows something about its own flow: there is more of it coming, or it is the first of several funds doing the same thing. Its trade moves the price, and the price stays moved." That is the finding of Pierre Collin-Dufresne, Benjamin Junge and Anders Trolle ("Market Structure and Transaction Costs of Index CDSs," *Journal of Finance*, 2020): dealer-to-client index trades cost more than interdealer trades because client trades have larger and more lasting price impact. Lynn Riggs, Esen Onur, David Reiffen and Haoxiang Zhu ("Swap Trading after Dodd-Frank: Evidence from Index CDS," *Journal of Financial Economics*, 2020) find that on the two largest dealer-to-customer swap execution facilities a typical customer asks only a few dealers for a quote. Asking more would buy competition and sell information, because every losing dealer now knows a client wants protection, and a dealer who wins against many rivals has probably mispriced. "Three players at the table," Ines said. "Each one knows the other two saw your hand."

Theo replayed the hand, as Ines insists every hand be replayed. Five minutes after the trade the index was at 106.78; an hour later 106.70; at the close 106.62 *(illustrative)*. The desk had charged the client six cents, \$15,000 on \$25 million, and its long-risk position had then lost eighteen, \$45,000, before the hedge caught up. "The client didn't pay more than the dealer," Ines said. "It paid less than its information was worth." The markouts are the two-tier result in one afternoon, and Chapter 18 (§18.3, §18.7) gives the general version: the RFQ hit rate and the price of staying at the table are Kyle's model with a chat window.

The fastest-growing slice of the index market is options on the index. Cleared CDX swaptions reached \$52.9 billion in March 2026, up 80% on a year earlier, and all swaptions reported to swap data repositories that month came to about 12% of USD index notional (Clarus, June 2026); yet only 33.9% of the "other" index products, mostly swaptions and tranches, were cleared in the second quarter, against 99.3% of CDX (ISDA SwapsInfo, H1 2026). The cheapest place to express a view about a jump is also the least visible and least cleared. Index options also carry a skew, with options to buy protection (payers) priced richer than options to sell it (receivers) the same distance away, because spreads jump wider more readily than they jump tighter; Chapter 23 (§23.1–§23.4) builds the surface, and Chapter 6-B places the gamma.

## 10B.8 The Pod's Cheapest Short Leg

*Dov Adler's pod at Vantress Capital Management, Wen Zhao, Marcus Oyelaran, Kestrel Roofing and Halvorsen Packaging are fictional composites (Chapter 1-B, Chapter 8-D). Every position, margin, price and P&L figure is illustrative. The margin percentages are from Eurex's own presentation comparing its futures with CDX, a vendor comparison that is not like-for-like.*

At 8:20 on Thursday 15 October, Marcus Oyelaran's e-mail had a new kind of question in it. The x-ray was grey; PB-01, Dov's Kestrel-against-Halvorsen pair, had been flat to the market since Tuesday's 2:40 trim. What Marcus wanted to know was why the pod's initial-margin line had risen by about a million dollars that week.

Wen knew before she opened the clearing statement. The trim had added a third leg to PB-01: about \$13 million of CDX HY protection, sold to offset the 17,700 of DTS by which the trimmed Halvorsen short still outweighed the Kestrel long (§1B.2, §8C.6). Selling protection is long risk, and a clearing house margins long risk in high yield as what it is, a position that loses heavily if a constituent defaults. Eurex's own comparison puts initial margin on long CDX HY (on an older series) at 8.12% of notional, against 2.46% for a long position in its US dollar high-yield future (Eurex, "Global Credit Index Futures" presentation). On \$13 million that is about \$1.06 million against \$0.32 million.

Wen called the FCM, asked for the futures route's actual numbers, and priced the switch on a pad. The margin would fall by about \$0.74 million. Funded at a spread of about 60 bp over what the clearing house pays on posted cash *(illustrative)*, that saving is worth about \$4,400 a year. PB-01's standing costs run to about \$2.5 million a year (§8C.6). The margin was real, and it was a rounding error.

Then she wrote down what the switch would buy along with the saving, and that list was longer. The future is a funded bond-index contract with about 2.9 years of rate duration inside it, roughly \$3,800 of DV01 on \$13 million that CDX never had, to be hedged in Treasury futures or handed to CME's DHY and its rule (§10B.2). Its basket is about 1,100 bonds capped at 2% per issuer, while the x-ray measures the pair's beta against CDX HY, a hundred equal-weighted CDS names; the difference would arrive in the explain every morning as a leak with no name. And the futures–CDX basis, the price of the gap between those two baskets, is not published anywhere Wen could find; trade press has called trading it an arbitrage, without a number (The DESK, December 2025).

She wrote the sentence that went on the ledger: *A short leg with no published basis is a short leg whose basis you are about to discover.* Dov kept the CDX.

> **The Pair.** *Pair Book PB-01, Dov Adler's pod at Vantress (fictional composites); Kestrel and Halvorsen are fictional issuers; every figure is illustrative.* **Thesis.** Unchanged since April: Kestrel's covenant room against Halvorsen's 2027 revolver and sponsor (§1B.2). **Legs.** Long \$60mm Kestrel 6% 2030; short \$35mm Halvorsen 7.25% 2029, the bonds borrowed through the prime broker; and, since 13 October, about \$13mm of CDX HY protection sold, the beta trim. **What the hedge removes.** The pair's residual high-yield beta, measured against CDX HY, the same factor the x-ray uses. **What idio remains.** Kestrel against Halvorsen, unchanged. An index leg adds no idio by construction, which is the point of it. **What leaks.** The roll on Monday 22 March 2027 moves the leg into a series six months longer with different names, so its DTS jumps and the gap it was sized to fill is no longer the gap; the index's skew to its intrinsics, a few basis points in calm and not in stress; and, if the leg ever moves to a future, a futures–CDX basis nobody publishes plus 2.9 years of rate duration CDX never had. **What it costs.** Sold protection carries the par spread (§10.2.3), about \$435,000 a year at 335 bp on \$13mm, which the pair counts as the hedge's carry; initial margin of about \$1.06mm, funded at about \$6,400 a year; a SEF half-spread in and out and a roll bid-offer twice a year. The futures route would save about \$4,400 a year of that funding and buy an unmeasured basis (Chapter 24).

At 11:05 Dov rang Ines's desk anyway, for an IBHY indication, because a pod that has decided against an instrument still wants to know its price. Theo took the call and, three weeks into the desk's motto, could not resist. "IDO or it didn't happen?"

"Not on a hedge," Dov said. "An index has no idio. That's what I'm paying it for. When it has some, it's called basis, and I'd rather not own any."

*Builds on:* §1B.2, §8C.6, §8D.2 (the short-leg menu, whose "credit index futures" row this section fills in), §10.2.3 (index carry). *Used in:* §24.3, §24.7 (the basis as a trade), §28.8 (the pod's year).

## 10B.9 What the Contracts Do to the Trend Sleeve's Cost Curve

*Quarry Brook is fictional; the market sizes are real, from different months, and are compared as orders of magnitude only.*

In mid-October 2026 Gil Navarro's research team asked to raise credit from 2% to 5% of Quarry Brook's trend risk, and the risk committee asked the question every CTA asks of a new market: how big can we get before we are the market?

Cboe and CME together traded about \$660 million a day of US dollar credit futures in August 2026; CDX IG and HY traded \$36.9 billion a day in the second quarter (ISDA). The listed layer is roughly 2% of the swap market's flow. Combined US listed open interest of about \$3.8 billion is about 0.1% of the \$3.08 trillion of cleared CDS open interest (Clarus, as of 30 June 2026). An average CDX HY trade of \$21.5 million is about 115 IBHY contracts, a third of a quiet day's volume. A trend sleeve carrying more than about \$50 million of high-yield beta is therefore a block customer, not a lit-book taker (§10B.4), and its rolls land in the same week before expiry as everyone else's (§10B.6).

Gil's team wrote an extrapolation into the memo and labeled it as one. If listed ADV grows 50% a year and CDX stays near \$37 billion, listed ADV reaches about \$1.5 billion by August 2028, about 4% of CDX; open interest growing 60% a year would reach about \$9.7 billion, a quarter of one percent of cleared CDS open interest. Five things could break the line: incentive programs ending, a fragile index close, four index families splitting liquidity, the spread of the same model into loans (CME's leveraged-loan future), and a CFTC file that might show the users leaving.

Two dated tests show when the contracts work. In the April 2025 tariff week the Cboe pair printed about 1,400 to 2,150 contracts a day, a few tenths of a billion dollars, against a swap market moving tens of billions: the contracts traded, but a fund the size of Quarry Brook would have been most of the market. In March 2026, the nearest thing to a stress month since, Eurex posted a record EUR 742 million a day while Cboe's ADV fell from \$435 million to \$240 million (The DESK, 14 April 2026). Only the exchanges have called either venue resilient. The contracts work as a cheap, small, calendared beta for a sleeve that sizes to them. They break when the sleeve is large relative to a quiet day, when the trade is in the same direction as everyone's, and when the index close is the thing in doubt.

The committee approved 3.5%, not 5%, and asked for the turnover table monthly.

> **View From Another Seat.** *The bank XVA desk (a generic seat; this is Susquehanna's forecast phase three, and there is no public evidence yet that it has arrived).* A CVA desk hedges the credit risk in its derivative counterparties, and the capital rules reward hedges that look like the risk. An index future with no ISDA, cleared margin and automatic offsets against rates is, on paper, a clean way to hedge the spread component of a counterparty book. In practice the desk's exposures are to named counterparties, the futures' baskets are bond indices chosen for liquidity, and the regulatory treatment of a bond-index future as a CVA hedge is a question for the desk's own capital lawyers. If this seat arrives, it arrives as a large, steady seller of futures, and open interest would show it before anyone announced it.

Chapter 10 asked whether credit trend is just beta (§10.6.3). The futures do not change that answer. They make the beta cheaper to reach for a fund that could not reach it before, which is a different thing from making it different.

*Builds on:* §10.6.3, §10.8 (turnover and costs), §10B.3–§10B.6. *Used in:* §28.3 (capacity), Appendix C.

## 10B.10 The Index Microstructure Engine

### Specification for AI Implementation

*The problem it solves.* Every scene in this chapter ended with somebody computing a number on a pad: Lucía's turnover table, Bram's break filter, Rafael's series basis, the five-name intrinsic. Nobody without a stake in the answer publishes those numbers, so a desk that uses the index as a hedge, a trend leg or a short leg measures them itself. `index_micro.py` is those pads as a few small functions on public files.

*What it computes, and why it is built this way.* `turnover` is ADV over OI by venue and month, with the implied holding period, and a gap rather than an infinity when OI is zero. `roll_window_share` sums volume across contract months each day and reports the share of each quarter's volume traded in the last few days before expiry (§10B.6). `tff_net` builds net positions by CFTC category for one contract code and flags a probable reclassification: one category jumps by more than a set share of OI, another moves the other way, and OI barely changes; `spliced_change` then blanks that week so a feature splices across it. `intrinsic` and `skew` are §10B.6's duration-weighted average and the quote's distance from it; `series_basis_line` is §8C.2's roll-day line. Each function is pure and takes plain tables, because the inputs come from three public sources with three schemas, and each number can be checked by hand against the chapter.

*Inputs and outputs.* In: volume and OI (contracts or \$mm, consistently), dates and expiries, raw CFTC API rows, constituent spreads in bp with risky durations in years, index prices per 100, notionals in \$mm. Out: ratio tables, roll-window shares by expiry, weekly nets with a `reclass_flag`, spreads and skews in bp, a roll-day line in \$mm.

*When to use it, and when not.* It is a measurement kit. It tells a desk whether the volume is rented, where the calendar is, who is hedging and how far an index sits from its ingredients. It is not a trading signal: twenty-three weeks of CFTC data cannot validate a positioning strategy, and a skew of a few basis points is usually somebody else's balance sheet, not free money. The CFTC field names sit in a dictionary at the top of the file, to be checked against the dataset's metadata on first use.

*The edge case that bites.* Timestamps. An intrinsic built from constituent quotes snapped at 4:00 and compared with an index marked at 4:45 manufactures a skew out of forty-five minutes of market, which on a volatile afternoon is larger than the real one. A second one bites in `roll_window_share`: Cboe's file has one row per contract month per day, and the expiring and next contracts trade side by side in exactly the week being measured, which is why the function sums across months before it counts.

<!-- EXPLAINED -->
```python
"""index_micro.py (Chapter 10-B): four small measurements of the index market.

turnover / roll_window_share  volume against open interest, and the expiry calendar
tff_net / spliced_change      CFTC positioning by category, with a reclassification flag
intrinsic / skew              duration-weighted intrinsic spread and the quote's distance from it
series_basis_line             the roll-day explain line (Section 8C.2)

Units: volume and OI in contracts or $mm (consistently); spreads in bp; risky
durations in years; index prices per 100; notionals in $mm. Demo numbers are the
chapter's illustrative ones except where a comment cites a source.
"""
import numpy as np
import pandas as pd


def turnover(adv, oi):
    """ADV / OI and the implied average holding period in trading days."""
    adv = pd.Series(adv, dtype=float)
    oi = pd.Series(oi, dtype=float)
    ratio = adv / oi.where(oi > 0)              # NaN, not inf, when OI is zero
    return pd.DataFrame({"turnover": ratio, "hold_days": 1.0 / ratio})


def roll_window_share(daily, expiries, window=5):
    """Share of each quarter's volume traded in the last `window` trading days
    (days with a row in the file) before each expiry.

    daily: DataFrame with 'date' and 'volume' for ONE product, any number of
    rows per date (Cboe's file has one per contract month); they are summed.
    """
    d = daily.assign(date=pd.to_datetime(daily["date"]))
    d = d.groupby("date")["volume"].sum().sort_index()
    rows, start = [], d.index.min()
    for exp in sorted(pd.to_datetime(list(expiries))):
        q = d[(d.index >= start) & (d.index < exp)]
        start = exp
        if q.empty:
            continue
        w, tot = q.iloc[-window:].sum(), q.sum()
        rows.append({"expiry": exp, "window_vol": w, "quarter_vol": tot,
                     "share": w / tot if tot > 0 else np.nan})
    cols = ["expiry", "window_vol", "quarter_vol", "share"]
    return pd.DataFrame(rows, columns=cols).set_index("expiry")


# Traders in Financial Futures column names as published; check them against the
# dataset's metadata (publicreporting.cftc.gov, dataset gpe5-46if) on first use.
TFF_FIELDS = {
    "date": "report_date_as_yyyy_mm_dd",
    "code": "cftc_contract_market_code",
    "oi": "open_interest_all",
    "dealer_long": "dealer_positions_long_all",
    "dealer_short": "dealer_positions_short_all",
    "am_long": "asset_mgr_positions_long",
    "am_short": "asset_mgr_positions_short",
    "lev_long": "lev_money_positions_long",
    "lev_short": "lev_money_positions_short",
}


def tff_net(rows, code, fields=TFF_FIELDS, jump=0.25, oi_tol=0.05):
    """Weekly net (long - short) by category for one contract code, with a flag
    for probable reclassifications: one category's net moves by more than `jump`
    x last week's OI, another moves the opposite way by more than half that, and
    OI changes by less than `oi_tol`."""
    df = pd.DataFrame(rows)
    df = df[df[fields["code"]].astype(str) == str(code)].copy()
    df["date"] = pd.to_datetime(df[fields["date"]])
    for k in ("oi", "dealer_long", "dealer_short", "am_long", "am_short",
              "lev_long", "lev_short"):
        df[k] = pd.to_numeric(df[fields[k]], errors="coerce")
    df = df.sort_values("date").set_index("date")
    net = pd.DataFrame({
        "dealer": df["dealer_long"] - df["dealer_short"],
        "asset_mgr": df["am_long"] - df["am_short"],
        "lev_funds": df["lev_long"] - df["lev_short"],
    })
    rel = net.diff().div(df["oi"].shift(1), axis=0)
    up, dn = rel.max(axis=1), rel.min(axis=1)
    big = (up > jump) | (dn < -jump)
    opposite = (up > jump / 2) & (dn < -jump / 2)
    flat_oi = df["oi"].pct_change().abs() < oi_tol
    out = net.assign(oi=df["oi"], am_short_share=df["am_short"] / df["oi"])
    out["reclass_flag"] = (big & opposite & flat_oi).fillna(False)
    return out


def spliced_change(series, flag):
    """Week-on-week change with flagged weeks set to NaN: splice, do not difference."""
    ch = series.diff()
    ch[flag.astype(bool)] = np.nan
    return ch


def intrinsic(spreads_bp, durations, weights=None):
    """Duration-weighted intrinsic spread, bp. Drop defaulted names first."""
    s = np.asarray(spreads_bp, dtype=float)
    dur = np.asarray(durations, dtype=float)
    w = np.ones_like(s) if weights is None else np.asarray(weights, dtype=float)
    if not np.all(np.isfinite(s)) or np.any(dur <= 0):
        raise ValueError("each constituent needs a finite spread and a positive duration")
    return float(np.sum(w * dur * s) / np.sum(w * dur))


def skew(index_bp, spreads_bp, durations, weights=None):
    """Quoted index spread minus intrinsic, bp (negative: index tighter than its names).
    Quotes and constituents must share one snapshot time."""
    return index_bp - intrinsic(spreads_bp, durations, weights)


def series_basis_line(p_new, p_old, notional_mm, long_risk=True):
    """Roll-day line for a price-quoted index, $mm: (P_new - P_old) x N / 100,
    N positive for long risk. A change of instrument, not P&L (Section 8C.2)."""
    sign = 1.0 if long_risk else -1.0
    return sign * (p_new - p_old) * notional_mm / 100.0


if __name__ == "__main__":
    # Section 10B.3 (The DESK, exchange data): ADV and OI in $m.
    adv = pd.Series({("CME", "2026-02"): 522, ("CME", "2026-08"): 253,
                     ("Cboe", "2026-02"): 435, ("Cboe", "2026-08"): 407})
    oi = pd.Series({("CME", "2026-02"): 689, ("CME", "2026-08"): 1610,
                    ("Cboe", "2026-02"): 1990, ("Cboe", "2026-08"): 2170})
    print(turnover(adv, oi).round(2))            # CME 0.76 then 0.16; Cboe 0.22, 0.19
    # Section 10B.6 toy index: intrinsic 147.7 bp; skew -4.7 bp at a quote of 143.
    sp, du = [60, 80, 100, 150, 400], [4.6, 4.5, 4.4, 4.2, 3.6]
    assert abs(intrinsic(sp, du) - 147.70) < 0.01
    print(round(skew(143.0, sp, du), 1))
    # Exercise 5: $13mm long risk, old series 106.10, new 105.20 -> -0.117, named, not P&L.
    print(round(series_basis_line(105.20, 106.10, 13.0), 3))
```

## 10B.11 Desk Debrief

On Friday 16 October Theo found the pad from the cold open under a stack of model-review printouts. The column of four prices was still there, eighty basis points of disagreement in his own handwriting. Over two weeks he had added a second column beside it, headed *settles to*, and a third, headed *what it does on a bad day*. The third had taken the rest of the chapter: a paid-for order book that might thin out, a calendar that put everyone's size in the same week, an evaluated close that was partly a model, a positioning file that sometimes relabelled its own traders, a roll that changed the instrument's identity twice a year, and a basis between the futures and CDX that nobody publishes. Mags read it over his shoulder and said it was the first index document she had seen that listed its own failure modes, and that it was a pity it was handwritten.

- **A credit index price is a claim on a rulebook:** what it settles to, what its basket is and when the basket changes come before whether it is cheap.
- **The futures sell frictions, not price:** no ISDA, no borrow, one leg, margin that nets against rates. For a futures-only fund that is the whole product; for a desk with an ISDA it is a basis to be measured.
- **Volume is partly the exchange's policy.** Open interest, block share, quoted width and turnover are the market's own vote; a ratio near 1 beside a thin book is rented.
- **Liquidity has a calendar:** roll weeks and the week before expiry are cheap for everyone at once, because everyone shares the dealer's balance sheet then.
- **An index has a skew to its ingredients and a jump at every roll.** Near zero in calm, 60 bp in 2008–09; build returns inside one series and carry the series basis as its own line.
- **Clients pay more than dealers for index risk because their trades carry information;** a few-dealer RFQ trades competition against leakage, and the hand history says whether the charge was enough.
- **The index is the pod's cheapest short leg by margin and its dirtiest by basis,** and the basis is worst when the hedge is needed. A short leg with no published basis is a short leg whose basis you are about to discover.

### The Spec You Hand the Robot

*Vague version:* "roll the position." *What ROBO built:* a close of the old series and an open of the new at the same spread, booking \$410,000 of P&L that never existed, as specified. *The precise version:* "Implement `index_micro.py` per §10B.10. Every index row carries `series_id`; returns are computed within one series; on the administrator's roll date the position rolls at the observed old and new prices and the explain carries `series_basis_line` separately. Turnover by venue and month from ADV and OI; roll-window share after summing contract months; TFF net positions with `reclass_flag` and spliced changes; intrinsic and skew from constituents snapped at the index's own timestamp, defaulted names excluded, and a refusal if any duration is non-positive. Units: contracts or \$mm, bp, years, prices per 100."

### Exercises

**1. Rented or real?** *[turnover]* In August 2026 Cboe's IBIG traded \$140m a day against open interest of \$741m; CME's credit futures traded \$522m a day against \$689m in February. Compute each turnover and holding period and say which number you would want to see beside each before trusting it. *Solution.* $140/741 = 0.19$, about 5.3 days; $522/689 = 0.76$, about 1.3 days. Beside the second you want the size at the best bid and offer, and whether the volume survives the end of an incentive program; beside the first, the block share, because a third or more of the volume may never touch the book.

**2. The interest rate, discovered.** *[futures pricing]* An index stands at 182.40, settlement is two months away, financing is 4.2% and the index reinvests its coupons. What is the fair futures price, and how many contracts at \$1,000 a point give \$50mm of exposure? *Solution.* $F \approx 182.40 \times (1 + 0.042 \times 2/12) \approx 183.68$; $50{,}000{,}000/(1{,}000 \times 183.68) \approx 272$ contracts. The 1.28-point gap to the index is financing, not a view.

**3. The skew on three names.** *[intrinsic]* Equal-weighted names at 300, 500 and 900 bp with risky durations 4.3, 4.0 and 3.4; the index quotes 530 bp. Compute the intrinsic, the skew and the trade that would lock it in. *Solution.* $(1{,}290 + 2{,}000 + 3{,}060)/11.7 \approx 542.7$ bp, below the simple average of 566.7. Skew $= 530 - 542.7 = -12.7$ bp: buy index protection at 530 and sell protection on the three names, earning about 12.7 bp before three sets of bid-offers, margin on four positions and the risk that the gap widens before it closes.

**4. Who owns the residual?** *[build; Kaz's question]* Regress a year of daily DHB returns on changes in the 2-, 5-, 10- and 30-year Treasury yields and in CDX IG's spread. What should the yield coefficients be if the methodology's hedge were perfect, and what would non-zero coefficients in a rate sell-off tell you? *Solution sketch.* Zero; the package is built to zero option-adjusted duration. Non-zero coefficients that grow in large moves are convexity and the moving rate-spread correlation of §8.2, the part the rule gets wrong and the holder owns; their sign changes with the regime.

**5. The phantom roll.** *[series basis]* A desk is long risk \$13mm of CDX HY. On roll day the old series is at 106.10 and the new at 105.20. What does a generic "on-the-run" ticker show, what does ROBO's same-price roll book, and what line names it? *Solution.* The ticker shows $(105.20 - 106.10) \times 13/100 = -\$0.117$mm, a change of instrument. ROBO's roll at one price books the same \$117,000 as a market loss the first time the new series is marked, or as a gain if the desk is long protection. The explain's series-basis line, $(P^{\text{new}} - P^{\text{old}})\,N/100 = -\$0.117$mm, names the jump as a change of instrument, so it lands in neither the market line nor the residual (§8C.2), and the next day's return is computed inside the new series.

### Deep-Dive Resource Graph

**Podcasts**

- *Odd Lots*, "Why the True Price of a Bond Can Still Be Hard To Know" (Maciej Kowara and Eric Jacobson of Morningstar), 5 April 2021: <https://omny.fm/shows/odd-lots/why-the-true-price-of-a-bond-can-still-be-hard-to>. Evaluated prices as opinions: the raw material of every index close in §10B.4.
- *Masters in Business*, "Boaz Weinstein on Credit Investments," 13 May 2022: <https://omny.fm/shows/masters-in-business/boaz-weinstein-on-credit-investments>. A career on the index-versus-single-name relationship, including the 2012 skew of §10B.6.
- *Flirting with Models*, S7E19, "Jeff Rosenberg: The Past, Present, and Future of Systematic Fixed Income," 18 August 2025: <https://www.flirtingwithmodels.com/episodes/8V74zBaN4jN>. The view from the firm behind HYG and LQD, whose holdings Cboe's contracts track.

**Practitioner Writing**

- Bai and Shachar, "The Effects of Entering and Exiting a Credit Default Swap Index," *Liberty Street Economics*, 30 March 2015: <https://libertystreeteconomics.newyorkfed.org/2015/03/the-effects-of-entering-and-exiting-a-credit-default-swap-index>. Intrinsic value, the 60 bp skew, the 12 bp entry effect, the roll jump.
- The DESK, "The credit futures market" (Susquehanna's three phases), 28 May 2024: <https://www.fi-desk.com/the-credit-futures-market/>.
- The DESK, "Competition in credit futures heating up with ICE/MarketAxess/MSCI launch," 13 December 2024: <https://www.fi-desk.com/competition-in-credit-futures-heating-up-with-ice-marketaxess-msci-launch/>.
- The DESK, "Cboe: block trading has arrived in credit index futures" (sponsored), 2026: <https://www.fi-desk.com/cboe-block-trading-has-arrived-in-credit-index-futures-2/>.
- The DESK, "Eurex: five questions every investment committee should ask about credit index futures" (sponsored): <https://www.fi-desk.com/eurex-five-questions-every-investment-committee-should-ask-about-credit-index-futures/>.
- FOW, "Goldman, JP Morgan, Morgan Stanley join Eurex credit programme," 4 September 2025: <https://www.fow.com/insights/goldman-jp-morgan-morgan-stanley-join-eurex-credit-programe>.
- Clarus FT, March 2026 credit derivatives volumes (swaptions, cleared CDX): <https://www.clarusft.com/us-firms-powered-march-2026-itraxx-swaps-volume-growth/>; and "CRD volumes at the end of Q3 2025," 5 November 2025 (by title; the IMM-date peaks).
- Eurex, "Global Credit Index Futures" presentation, October 2026: <https://www.eurex.com/resource/blob/4018980/3fed7a77845c591c5f2908c8ed818b00/data/presentation-global-credit-index-futures.pdf>. Index sizes, launch dates, the margin comparison (vendor, not like-for-like).

**Academic Papers**

- Collin-Dufresne, P., B. Junge and A. B. Trolle (2020), "Market Structure and Transaction Costs of Index CDSs," *Journal of Finance* 75(5), 2719–2763, doi:10.1111/jofi.12953. The two tiers of §10B.7.
- Riggs, L., E. Onur, D. Reiffen and H. Zhu (2020), "Swap Trading after Dodd-Frank: Evidence from Index CDS," *Journal of Financial Economics* 137(3), 857–886: <https://ideas.repec.org/a/eee/jfinec/v137y2020i3p857-886.html>. The few-dealer RFQ.
- Rapp, A. C., S. S. Shin, X. Zhou and Q. Zhu (2025), "When Delayed Spotting Meets Delayed Reporting: Distortions in the Corporate Bond Index Close," SSRN 5986474: <https://papers.ssrn.com/ab_id=5986474>. The index close as a single point of failure.

**Data & Code**

- Cboe contract specifications for IBHY and IBIG: <https://cdn.cboe.com/resources/futures/iboxx-ishares-contract-specs.pdf>; daily volume and open interest since launch: <https://cdn.cboe.com/data/us/futures/market_statistics/historical_data/cfevoloi.csv>.
- CFTC Traders in Financial Futures API (HYB code 221605, IQB 221606): <https://publicreporting.cftc.gov/resource/gpe5-46if.json>; CBOT Submission No. 26-429: <https://www.cftc.gov/filings/orgrules/rules08312622792.pdf>.
- ISDA SwapsInfo, First Half of 2026 and Second Quarter of 2026 Review: <https://www.isda.org/a/Uh0iE/SwapsInfo-First-Half-of-2026-and-the-Second-Quarter-of-2026-Review.pdf>.
- S&P Dow Jones Indices, CDX IG timelines for the September 2026 roll: <https://www.spglobal.com/spdji/en/documents/index-news-and-announcements/20260827-cdx-ig-timelines-september-2026.pdf>.
- ICE, CDS clearing 3Q 2021 update (the September 2021 roll week): <https://images.e.theice.com/Web/IDC/%7Bdf361826-c9bd-432d-8fec-f358203f79c0%7D_ICE_CDS_Clearing_3Q_2021.pdf>.

*Used in / builds on.* Builds on §10.1.1, §10.2.3, §8.6, §8C.2, §8C.6, §8D.2, §18.3, §18.7, §20.2–§20.3 and Appendix D §D.2, §D.4. Used in §8D.2 (the futures row), §24.3 and §24.7 (the futures–CDX basis as a fifth basis), §20.7 (the futures corner of the monitor), §22.6 (index clearing, 99.3% of CDX), §28.3 (capacity), Appendix B (`cfevoloi.csv`, `gpe5-46if`) and Appendix C.

<!-- STATUS: COMPLETE -->
