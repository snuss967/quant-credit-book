# Chapter 4-D: Getting the Seat: Interviews for Market-Making and Systematic Credit, From Probability Puzzles to the Thirty-Minute Credit Pitch, and the Portfolio That Proves It

> **Prerequisites.** The RFQ as a poker hand (§3.2) and the base-rate trap (§3.4.3); the five businesses called systematic credit (§4.1); Chapter 4-B for DV01, DTS and the hedge ratio. Everything else is pointed to, not assumed.

*Builds on:* §3.1–3.4 and §3.7, §4.1, §4B.5, §4C.3, §5.1.5, §7.6–7.7, §8.4 and §8.6, Chapter 8-D, §18.4–18.7, §28.2, §28.4 and §28.8. *Used in:* §3B.7 (how you will be measured, once you are measured), the Preface's "The cast" (how Theo got the seat), Chapter 8-D's exercises (the interview pair returns as someone else's pair), Chapter 26's study protocol (§26.9 item 8), Appendix A's phrasebook (§A.10), Appendix F (`interview_drills.py`).

*Theo Marsh, the shops, the interviewers and every question in this chapter are fictional composites. Real firms appear only through their public record, cited where they appear, in the sourced table of §4D.1, the Trend Watch and the View From Another Seat boxes; no question here is any real firm's question. The chapter is a labeled flashback to the week of Monday 22 June 2026, three months before Theo's first day on Ines's desk (Tuesday 22 September 2026).*

## Cold Open: Make Me a Market on the Page Count

Thursday, 8:40 a.m., a glass room on the trading floor of a non-bank credit market maker. The room had one table, two chairs, a whiteboard someone had cleaned with more optimism than solvent, and Ines Okafor, who sat with the particular stillness of a person who used to be paid to give nothing away. At her elbow lay a printed document, binder-clipped and face down. In Theo's jacket pocket was the USB stick holding his 13-week cash flow model, which he had carried to four interviews that week for emotional support and had not once been asked to produce.

"Serta Simmons," Ines said. "The 2016 first-lien term loan agreement. Make me a market on the page count."

Theo had read it. Everyone in restructuring had read it in the summer of 2020, the way everyone in a small town reads the police blotter the week after the bank robbery; §3.7 and Chapter 13 tell the story of the robbery. He had read it on a screen, though, and a screen has no thickness.

"One-eighty, two-sixty."

"I buy," Ines said, and wrote on a pad: *+1 @ 260*.

A banker's instinct is that the first trade is a courtesy, and Theo had a banker's instincts. He moved his market up a little, the way you nudge a fee proposal after the client says yes too quickly. "Two-twenty, three hundred."

"Buy." *+1 @ 300.*

The room was getting warmer, or he was. He did what felt prudent, which was to widen. "Two-twenty, three-forty."

"Buy." *+1 @ 340.*

He looked at the pad. Three lots, all lifted at his offer, all by the same person, and the same person had the document sitting by her coffee. He had been treating each purchase as noise, a random customer who happened to want pages, and every time he had paid her to correct him.

He said the next part out loud, which turned out to be the part that mattered. "You've bought three times, and you have the answer on the table. Either you think I'm cheap, or you know. If that's the conformed copy with the exhibits attached, the guarantee and collateral agreement, the forms, the schedules, then I've been pricing the wrong document. What's stapled to the back is the fact that moves my number, and it moves it up, a lot. So I'm not widening again. I'm moving." He thought for a second. "Three-sixty, four-forty."

Ines did not trade. She looked at him the way a dealer looks at a client who has finally asked the right question on the third call.

"What's the pot, what are the odds, and who at this table knows more than you?"

"The pot is three lots I'm short. The odds, I don't know. You know more than me. You have since the first trade."

"Since before the first trade. It's on the table." She tapped the document, still face down. "You quoted a number that has an answer, in a room where the answer was sitting next to my coffee, and then you kept paying me to tell you so. Then you stopped, and you said why." She made a note on the pad that he could not read upside down. "You'll do. You lost money the right way."

He never learned the page count. She slid the document into a drawer, and that was that. Months later, on the desk, he asked her. "That," Ines said, "was the most realistic part of the interview. Most hands never show you the cards."

This chapter is about what that room was testing. An ex-banker walks into an interview believing it measures what he knows. It measures how he loses. Every game a market-making or systematic credit shop plays has a live counterparty who trades against the candidate's answer, and the passing move, in every room Theo walked into that week, was the same one: update in the open. Narrow the market after being hit. Cut the Kelly fraction because the recovery is a document variable. Ask "which measure?" before saying a number. Deliver the credit pitch as a distribution with a horizon, a hedge and a markout instead of as a memo with a recommendation. None of it is new mathematics; every game is a section this book has already derived, and each section below opens a scene, works one number, and points home.

By the end of the chapter you will have watched Theo sit five interviews in five rooms and lose in each one in an instructive way, and you will be able to do the arithmetic he did on the train home: price a two-point bond in both measures, quote against someone who keeps buying, size a B3 bond with Kelly and then with a stop, defend a pair's hedge ratio by naming the state you are paid in, run a Fermi chain with error bars, join two tables without a time machine, break a Sharpe of 3.1, and turn a 13-week model into a pitch a trading desk can grade. You will also have a plan for the portfolio of projects that proves it.

## 4D.1 Sunday: Five Invitations and a Spreadsheet of Titles

The Sunday before, at a kitchen table with a cold coffee and five calendar invitations, Theo built the kind of spreadsheet he had built for every process at PJT: one row per counterparty, one column per thing he did not understand. The rows were a bank's credit-trading desk (Monday), a multi-strategy platform where a business-school classmate had passed his name along (Tuesday), a systematic asset manager (Wednesday), the market maker (Thursday) and a distressed fund (Friday). He had taken a week of vacation to do it, his first full week off in six years, and he was spending it in conference rooms.

The columns were the job titles, and the titles were the problem. *Co-head of credit systematic trading. Desk dev. Production engineer, rotation. Quantitative researcher, fixed income credit. Credit analyst, convertible arbitrage. Portfolio manager, pod.* At PJT a title told you who would be on the call and who would be blamed afterward. Here a title told you what the seat was paid to be right about, and the only way to read it was to find where the seat appeared in the public record and ask what it was doing there.

Five rooms are not quite §4.1's five businesses, and it helps to see how they line up. Section 4.1 sorts *strategies*: benchmark-relative long-only quants (i), long/short quant funds and pods (ii), multi-asset credit allocators (iii), rules-based credit ETFs (iv), and algorithmic dealers and non-bank liquidity providers (v). Theo's five rooms are *employers*, the five shop types of Chapter 1-B. Row (v) hires on the market maker's floor and, increasingly, on the bank desk's; row (ii) hires in the pod; rows (i), (iii) and (iv) hire at the systematic manager. The distressed fund belongs to none of §4.1's rows. It is on Theo's list because it is where his résumé is already a native language, and that turned out to matter on Friday.

What the public record says each seat is, as of the dates shown, is below. The table replaces the unsourced firm lists of §1.1 and the two open cells of §4.1 as the book's map of employers; those sections now point here.

| Business (room) | Seat titles in the public record (dated) | What the seat screens for | Where this book trains it |
| :--- | :--- | :--- | :--- |
| Bank credit-trading desk (Monday) | JPMorgan: "co-head of credit systematic trading" and "head of IG credit, public finance, short-term credit and alternative sales," both speaking on *Market Matters*, "A new era of credit portfolio trading?" (9 May 2025). Citi: a former head of US IG credit trading named global head of spread-products portfolio trading, electronic client connectivity and North America macro trading, with risk pricing described as the main responsibility (The TRADE, 15 Dec 2020, on an internal memo; paraphrase) | Pricing a list fast, warehousing what cannot be recycled, knowing which measure a number lives in | Part I (Ch 2, 4-B), Part V (Ch 18, 19) |
| Non-bank market maker (Thursday) | Citadel Securities: a COO of credit trading moved over from rates in October 2023, investment-grade traders hired from HSBC, Morgan Stanley and Deutsche Bank by January 2024 (The DESK, 4 Jan 2024), and a "global head of credit trading" by November 2025. Jane Street: "every desk across the firm has embedded desk devs" (*Signals and Threads*, Ep 29, 2 Sep 2026), and production engineers spend "between a quarter and a third" of their time on rotation (Ep 20, 7 Oct 2024) | Quoting under adverse selection, updating on fills, keeping a hand history | Ch 3, Ch 18, Ch 27 |
| Systematic asset manager (Wednesday) | Two Sigma postings: "Quantitative Researcher: Fixed Income Credit" (16 Feb 2023; "design sophisticated models," Python, "single-name credit" preferred) and "Credit Analyst - Convertible Arbitrage" (undated; "capital structure, liquidity, covenants"). DWS credit-trader posting (7 May 2026): execute PM orders "across multiple venues," "build automated solutions," Bloomberg, MarketAxess, Tradeweb, Python, SQL. Robeco: more than 20 fundamental analysts who "can challenge the model where downside risk is not adequately reflected" (7 Sep 2026) | Clean data, honest backtests, execution as a cost line, a human gate on the model | Ch 4, Ch 7, Ch 9, Part VII |
| Multi-strategy pod (Tuesday) | PM, analyst, platform risk (Chapter 8-B's three chairs). Credit PMs hired from banks and rival funds: Millennium (Hedgeweek, 2 Jun 2025), Jain Global (7 Aug 2026), Balyasny's IG long/short team (20 Aug 2026). Two-thirds of Citadel's fixed-income and macro PMs home-grown, and under 1% of applicants accepted (eFinancialCareers, 25 Feb 2026) | Isolating the idiosyncratic view, sizing to a stop, living inside scope | Ch 8, 8-B, 8-C, 8-D, Ch 28 |
| Distressed fund (Friday) | The restricted-list calendar, run by counsel and advisers to keep members trading as long as possible (Moyer, *Distressed Debt Analysis*, pp. 62–64). Man Group's purchase of Bardin Hill, a distressed and special-situations manager of about \$3bn and 48 people (Alternative Credit Investor, 30 Jul 2025) | Reading documents, valuing a plan, knowing your legal state | Part IV (Ch 12-B to 16), Ch 25 |

Theo's own version of this table was thinner (several entries above postdate his Sunday), and his first reading of it was that it listed jobs he was not qualified for. His second reading, near midnight, was better. Some of the rows were advertising for his résumé in other words. A Two Sigma credit analyst on a convertible-arbitrage book reads capital structure, liquidity and covenants so that a hedged, model-driven book is not blindsided, which is a restructuring banker's job description with the word "client" removed. That September, Robeco would put the same thought in print from the systematic side: its analysts exist for the bond that looks cheap while "a major lawsuit, regulatory issue, large acquisition or other event sits outside the model's scope," and a liability-management transaction is the purest example of an event outside a model's scope that the 2020s produced. The market maker and the pod were the rows where his résumé needed translating, and translating was what the week would be for.

> **Trend Watch.** *Who credit desks hired, 2023–2026, from postings and announced hires.* June 2023: Citadel Securities starts making markets in US investment-grade credit, streaming through MarketAxess and Tradeweb; its head of fixed-income distribution calls credit "a natural expansion" at "the nexus of our fixed income and ETF franchises" (The DESK, 19 Jul 2023). October 2023 to January 2024: the same firm moves its rates COO to credit and hires IG traders from three banks (The DESK, 4 Jan 2024). January 2024: a Goldman credit-trading partner describes about 8,000 portfolio trades for more than 300 clients in 2023, averaging about \$60mm across about 100 CUSIPs (Coalition Greenwich webinar; paraphrase). May 2025: JPMorgan puts its co-head of credit *systematic* trading on its podcast, recorded inside the April 2025 stress (*Market Matters*, 9 May 2025). June 2025: Millennium adds three credit hires, one of them a CDS and CMBS index trader (Hedgeweek, 2 Jun 2025). July 2025: Man Group, which wrote in 2023 that the future of credit investing is quantitative, agrees to buy a distressed manager (Alternative Credit Investor, 30 Jul 2025). May 2026: a buy-side credit-trader posting asks for Python and SQL alongside Bloomberg and the two big venues (DWS, 7 May 2026). August 2026: Jain Global hires a bank's London high-yield head (7 Aug), and Balyasny hires a BlackRock IG co-head to run a team that will "trade both long and short positions in US high-grade corporate bonds and pursue relative-value opportunities" (Hedgeweek, 20 Aug 2026). *What it means for the desk:* the titles moved toward electronic risk pricing on one side and toward documents and distress on the other, and the hybrid seat in the middle is the one this book trains. *What it does not show:* what any firm asks in an interview. No public interview guide was sourced for this box, so it tracks hiring, not questions, and the chapter prints no firm's questions.

Theo closed the laptop at 12:40 a.m. with one useful line written at the bottom of the spreadsheet, in the column he had labeled *What they will actually test*: "What I do when I'm wrong, at the speed they're wrong." He did not yet know how literally each room would take it.

![Figure 4-D.1: The funnel by business. Five columns (market maker, pod, systematic manager, bank desk, distressed fund) and six stages top to bottom (screen, puzzles, coding, pitch, portfolio, offer). Each cell names what that stage screens for in that business and the section of this book that trains it: for example, the market maker's puzzle stage screens for updating against a live counterparty (§3.2, §4D.3), the pod's pitch stage for naming the short leg and the ruler (§4D.6, Ch 8-D), the systematic manager's coding stage for point-in-time joins (§4D.8, §7.7), the bank desk's puzzle stage for "which measure?" (§4D.2), and the distressed fund's pitch stage for the plan as a distribution (§4D.10). Cells are shaded by how heavily each business weighs the stage *(illustrative composite; no firm's process)*.](assets/figures/ch04d_interview_funnel.png)

## 4D.2 Monday: "In Which Measure?"

The bank's credit-trading floor had the hum of a place that had been electronic for a decade and still kept a squawk box for sentimental reasons. The interview room's whiteboard had not been cleaned since someone's swap-spread trade, which was still there in three colors with an arrow labeled *why??* The interviewer ran high-yield flow, wore a fleece vest over a dress shirt, and opened without small talk.

"A bond pays 100 in a year or 40 if the company defaults. Nothing in between. The market says 85. What default probability is the market quoting?"

Theo did it in his head, the way he had done recovery math across a hundred boardroom tables. If $q$ is the default probability, the bond is worth $100(1-q) + 40q$, and setting that to 85 gives

$$
85 = 100 - 60\,q \quad\Longrightarrow\quad q = \frac{15}{60} = 25\%.
$$

"Twenty-five percent."

"In which measure?"

There was a pause long enough for the squawk box to say something about a new issue. In six years nobody had asked Theo which measure. At PJT a probability was a number you put in a sensitivity table, and the only question anyone asked about it was whether the client would accept it.

What the interviewer wanted was a single sentence, and Theo found it on the way home. The 25% is the probability that makes the price fair to someone who does not care about risk. It is a *risk-neutral*, or $\mathbb{Q}$, number: the weight that balances the bond's two outcomes at the market price, with rates set to zero and one period to run. The physical, $\mathbb{P}$, probability that the company actually defaults is lower, by whatever amount the market pays people for holding a bond that can lose 60 points overnight. If the historical default rate for bonds like this one were 10% *(illustrative)*, the expected payoff in the real world would be $0.9 \times 100 + 0.1 \times 40 = 94$, and a buyer at 85 would expect to make about 10.6% for carrying the jump. The gap between 25% and 10% is not a forecasting error. It is the price of the risk.

The interviewer added two follow-ups, and each one moved the number. "Rates are 4%." Then the 85 is a discounted value, and the undiscounted expectation is $85\,e^{0.04} = 88.47$, so $q = 11.53/60 = 19.2\%$: six points of "default probability" had been rates all along. "Now there's a third outcome. The company can do an exchange at 70." With three doors the price no longer pins down a default probability at all. Weights of 60% on par, 30% on the exchange and 10% on default also average to 85, and so do many other combinations. The two-point world called the bond a 25% default risk with a standard deviation of 26 points; this three-point world calls it a 10% default risk, a 40% chance of not being paid in full, and a standard deviation of 20 points (§3.1.1 and §3.1.2 do the variance bookkeeping). The price told Theo one number, the mean. Everything else was a model, and the model's most important input was whether an exchange door existed, which is a question about the credit agreement.

"That last part," said the interviewer, "is why we interview bankers." Then he moved on to portfolio trading, and Theo spent the next twenty minutes being polite about it.

> **Math, Gently.** *A distribution, and why one price has two sets of weights.* A distribution is a list of what can happen with a weight on each outcome, the weights adding to one. Picture a seesaw with a 40 at one end and a 100 at the other. Wherever the market puts the fulcrum, at 85, there is exactly one way to load the ends so that the seesaw balances there: three-quarters of the weight at 100 and a quarter at 40. Those balancing weights are the risk-neutral measure $\mathbb{Q}$. They are not a forecast. They are what the price *implies* if nobody needed paying for the risk. Your forecast of what will actually happen, the physical measure $\mathbb{P}$, is a second set of weights on the same two outcomes, and in credit it puts less weight on default than $\mathbb{Q}$ does, because the people who hold the jump want to be paid for it. One price, two loadings of the seesaw; the difference between them is the risk premium. Prices, hedges and relative value against CDS live in $\mathbb{Q}$; sizing, Kelly and your P&L forecast live in $\mathbb{P}$. The full version is in §5.1 and Chapter 6-B.

The judgment that matters on a desk is knowing which set of weights a question wants. When the question is "what does the CDS curve say this bond is worth?", the answer is a $\mathbb{Q}$ number, and mixing in a historical default rate produces a mispricing that is really a confusion. When the question is "how much of this bond should I own?", the answer needs $\mathbb{P}$, and §4D.5 shows what happens when a $\mathbb{Q}$ number sneaks in instead. Theo would make exactly that mistake in his first week on the desk anyway (Chapter 6 has the receipt). Knowing a distinction and having it in your hands are different stages of the same education.

## 4D.3 Monday, Continued: "I'll Sell You the Bond"

The interviewer erased the swap-spread trade, which felt like a liberty, and drew two dots.

"Forget the market. This bond is worth 100 or 40, fifty-fifty, and nobody knows which. Except some people do. One seller in five is informed and sells only if it's worth 40. Everyone else sells half the time for their own reasons: redemptions, rebalancing, a bad mood. I'm selling you the bond. What do you bid?"

This one Theo knew had a name, because Ines's desk had sent him a reading list and §3.2's Glosten–Milgrom model was on it. He reasoned it through anyway, because he had learned on Sunday that he was going to be asked to.

> **Math, Gently.** *Bayes as a posterior you can trade on.* Imagine a hundred days with this bond. On fifty of them it is secretly worth 40; on fifty it is worth 100. On a bad day the informed seller (one in five) always sells, and the uninformed sellers (four in five) sell half the time, so 20% + 40% = 60% of the time a sale arrives. On a good day only the uninformed sell, 40% of the time. Over the hundred days that is 30 sales on bad days and 20 on good ones. So when a sale arrives, it is a bad-day sale 30 times out of 50, or 60%, not the 50% you started with. The update came entirely from the fact that someone *chose* to sell to you. A dealer who bids the average value, 70, pays for that choice every time. The full version is in §3.2.1.

So the bid, the value of the bond given that someone is selling it, is

$$
b = 0.6 \times 40 + 0.4 \times 100 = 64,
$$

six points below the mid of 70, and by the same argument for buyers the ask is 76. The spread is 12 points, and none of it is a fee. The dealer here has no inventory cost, no risk aversion and no funding bill; in the notation of (3.1) the half-spread is $\pi\sigma_V = 0.2 \times 30 = 6$. Every point of it is insurance against the one seller in five who knows.

"Good. I sell you another one."

Theo said 64 again, and he heard the problem as he said it. He had updated on the second sale as if it were the first, starting again from fifty-fifty when he had just spent a minute establishing that the odds were now 60–40. Each sale multiplies the odds of the bad state by the same likelihood ratio, $0.6/0.4 = 1.5$. One sale takes the odds from 1 to 1.5; a second takes them to 2.25, a posterior of $2.25/3.25 = 69\%$, and a bid of

$$
b_2 = 100 - 60 \times 0.692 = 58.5 .
$$

Forgetting the first update is the base-rate trap of §3.4.3 run in reverse: instead of ignoring the prior, he had ignored the posterior. "Most people do that," the interviewer said, with the cheerfulness of a man who had watched most people do that. Then he asked the question Theo spent the train ride on: "Does it matter if it's the same seller both times?" It does, and the answer surprised him (Exercise 3 has it): a repeat sale from one counterparty carries less fresh news than sales from two strangers, because an informed seller would have sold twice anyway.

> **Poker Table.** Ines's version of this game, which Theo would hear on the desk in October, is shorter. "Every fill is a card face up. The hand history is the list of what you believed after each one." Figure 4-D.2 is that list for six sales. Against an informed seller who keeps selling, the posterior on the bad state climbs from 50% to 92% and the value of the bond falls from 70 to about 45. Against noise, sells and buys alternate and the posterior wanders around one-half. The part that surprises bankers is the width. The quote's spread is widest at fifty-fifty, where there is the most left to learn, and it *narrows* as the posterior heads toward certainty. Being hit should move the mid. It is not a reason to widen. Replay any hand on the desk's markout sheet (§3.3) and the same thing is visible: the dealer who widened after each fill paid the informed client at every step, and the dealer who moved the mid paid once.

![Figure 4-D.2: The live-counterparty update. Left panel: the posterior probability that the bond is worth 40 after each of six trades, for an informed seller who sells six times (0.60, 0.69, 0.77, 0.84, 0.88, 0.92) and for a noise path of sell, buy, sell, sell, buy, buy (0.60, 0.50, 0.60, 0.69, 0.60, 0.50). Right panel: the bid and ask the dealer would quote for the next trade on each path, with the mid falling toward 45 on the informed path and the bid–ask spread *narrowing* from 12 points as the posterior moves away from one-half. Setup as in §4D.3: values 100 or 40, prior one-half, one seller in five informed, uninformed traders sell or buy with probability one-half *(illustrative)*.](assets/figures/ch04d_live_counterparty_update.png)

## 4D.4 Thursday, Replayed Slowly: Make Me a Market

Replay the cold open with Monday in hand, and Theo's three markets become a hand history with a diagnosis attached.

His first market, 180–260, was a guess wearing a bid and an offer. A two-sided market on a number is a confidence interval with money on it, and the useful question is how often it should be wrong. The answer is not "never." An interval that never misses is too wide to trade on, and one that misses half the time is a coin toss with a spread. A reasonable target is an interval you expect to miss about one time in ten, and most people asked for one produce something much narrower. Psychologists have measured this for decades (Alpert and Raiffa's work in the 1970s and early 1980s is the classic): people's "90% intervals" miss far more often than one time in ten, because the interval feels like a claim of knowledge and narrowness feels like competence. For a document Theo had only seen on a screen, a page count he could defend at 90% would have run from something like 130 to 480 *(illustrative: a median of 250, uncertain by a factor of about 1.5 either way)*. That market is ugly. It is also honest, and an honest wide market loses less to someone who knows than a confident narrow one.

His second market moved up 40 pages after a buy. That was the right direction and the wrong size. Monday's arithmetic says a single trade from someone who might be informed is evidence, and in a two-sided game against a person holding the document, the informed fraction is not one in five. It is closer to one in one. His third market widened instead of moving, which was the instinct Monday had just disproved: being lifted is news about the *level*, and widening protects you against uncertainty you have already lost.

There is a second reason a market maker moves after being hit, and interviewers like to see a candidate separate it from the first. Avellaneda and Stoikov's dealer (§18.4) is risk-averse, and her reservation price slides with inventory,

$$
r^{\text{res}} = S_t - q\,\gamma\,\sigma^2\,(T - t),
$$

where $S_t$ is the mid, $q$ the inventory in lots, $\gamma$ risk aversion and $\sigma^2(T-t)$ the variance she expects to carry. Short two lots, $q = -2$, she quotes higher to get bought back in. With §18.4.2's bond numbers ($\gamma = 0.005$ per point-lot, $\sigma^2(T-t) = 1.27$ points squared for a one-week hold), two lots of inventory move the reservation price by $2 \times 0.005 \times 1.27 = 0.013$ points. That is pennies. The information update on Monday moved the value by six points on one trade. In a bond, inventory skew is the small correction and the client's information is the large one, which is why the formula needed §18.6 and §18.7 to be useful on a credit desk. A candidate who answers "make me a market" by skewing for inventory and not for information has the right formula for the wrong game.

The third variant is the trap at the other end. A candidate who has been burned widens until nobody trades with him, and a market nobody trades on loses no money and learns nothing. Desks have a name for this, because the RFQ world punishes it twice: clients stop sending requests to a dealer who never wins, and a dealer who never wins has no fills to learn from. Section 18.7 prices the cost of staying at the table as a hit-ratio constraint with a shadow price per RFQ, the coupon a desk pays itself for turning up. Ines's phrasing for candidates is shorter: move the mid before you widen, and keep quoting.

> **Ways This Blows Up.** *The number with a document answer.* Theo's real error in the cold open came before his first quote. A page count is not a random variable; it is a fact printed on a page, and the person asking may have the page. Credit desks meet this shape every week in a more expensive form: an RFQ on a bond whose indenture answers the question the price is asking (is the 2029 note structurally senior? does the exchange need the holder's consent?), sent by a client who has read it. The quote is a market on a number that has an answer, and the counterparty who keeps buying is telling you so. The defense is the sentence Theo eventually said out loud: name the fact that moves your number and which way, then go and read it.

> **Desk Myth vs. Desk Reality.** *Myth:* the interview tests what you know. *Reality:* it tests how you update. Every game in this chapter has an answer key, and the answer key is the less interesting part of the grade.

What Ines wrote on her pad, Theo found out in September, was four words: *moved late, moved right*. The desk's hiring notes, like its trade tickets, recorded the fill and the markout, and not much else.

