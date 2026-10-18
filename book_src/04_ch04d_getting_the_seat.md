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

This chapter is about what that room was testing. An ex-banker walks into an interview believing it measures what he knows. It measures how he loses. Every game a market-making or systematic credit shop plays has a live counterparty who trades against the candidate's answer, and the passing move, in every room Theo walked into that week, was to update in the open: narrow the market after being hit, cut the Kelly fraction because the recovery is a document variable, ask "which measure?" before saying a number, and deliver the credit pitch as a distribution with a horizon, a hedge and a markout rather than a memo with a recommendation. None of it is new mathematics. Every game is a section this book has already derived, and each section below opens a scene, works one number, and points home.

By the end of the chapter you will have watched Theo sit five interviews in five rooms and lose in each one in an instructive way, and you will be able to do the arithmetic he did on the train home: price a two-point bond in both measures, quote against someone who keeps buying, size a B3 bond with Kelly and then with a stop, defend a pair's hedge ratio by naming the state you are paid in, run a Fermi chain with error bars, join two tables without a time machine, break a Sharpe of 3.1, and turn a 13-week model into a pitch a trading desk can grade. You will also have a plan for the portfolio of projects that proves it.

## 4D.1 Sunday: Five Invitations and a Spreadsheet of Titles

The Sunday before, at a kitchen table with a cold coffee and five calendar invitations, Theo built the kind of spreadsheet he had built for every process at PJT: one row per counterparty, one column per thing he did not understand. The rows were a bank's credit-trading desk (Monday), a multi-strategy platform where a business-school classmate had passed his name along (Tuesday), a systematic asset manager (Wednesday), the market maker (Thursday) and a distressed fund (Friday). He had taken a week of vacation to do it, his first full week off in six years, and he was spending it in conference rooms.

The columns were the job titles, and the titles were the problem. *Co-head of credit systematic trading. Desk dev. Production engineer, rotation. Quantitative researcher, fixed income credit. Credit analyst, convertible arbitrage. Portfolio manager, pod.* At PJT a title told you who would be on the call and who would be blamed afterward. Here a title told you what the seat was paid to be right about, and the only way to read it was to find where the seat appeared in the public record and ask what it was doing there.

Five rooms are not quite §4.1's five businesses. Section 4.1 sorts *strategies*: benchmark-relative long-only quants (i), long/short quant funds and pods (ii), multi-asset credit allocators (iii), rules-based credit ETFs (iv), and algorithmic dealers and non-bank liquidity providers (v). Theo's five rooms are *employers*, the five shop types of Chapter 1-B. Row (v) hires on the market maker's floor and, increasingly, on the bank desk's; row (ii) hires in the pod; rows (i), (iii) and (iv) hire at the systematic manager. The distressed fund belongs to none of §4.1's rows. It is on Theo's list because his résumé is already its native language, which mattered on Friday.

What the public record says each seat is, as of the dates shown, is below. The table replaces the unsourced firm lists of §1.1 and the two open cells of §4.1 as the book's map of employers; those sections now point here.

| Business (room) | Seat titles in the public record (dated) | What the seat screens for | Where this book trains it |
| :--- | :--- | :--- | :--- |
| Bank credit-trading desk (Monday) | JPMorgan: "co-head of credit systematic trading" and "head of IG credit, public finance, short-term credit and alternative sales," both speaking on *Market Matters*, "A new era of credit portfolio trading?" (9 May 2025). Citi: a former head of US IG credit trading named global head of spread-products portfolio trading, electronic client connectivity and North America macro trading, with risk pricing described as the main responsibility (The TRADE, 15 Dec 2020, on an internal memo; paraphrase) | Pricing a list fast, warehousing what cannot be recycled, knowing which measure a number lives in | Part I (Ch 2, 4-B), Part V (Ch 18, 19) |
| Non-bank market maker (Thursday) | Citadel Securities: a COO of credit trading moved over from rates in October 2023, investment-grade traders hired from HSBC, Morgan Stanley and Deutsche Bank by January 2024 (The DESK, 4 Jan 2024), and a "global head of credit trading" by November 2025. Jane Street: "every desk across the firm has embedded desk devs" (*Signals and Threads*, Ep 29, 2 Sep 2026), and production engineers spend "between a quarter and a third" of their time on rotation (Ep 20, 7 Oct 2024) | Quoting under adverse selection, updating on fills, keeping a hand history | Ch 3, Ch 18, Ch 27 |
| Systematic asset manager (Wednesday) | Two Sigma postings: "Quantitative Researcher: Fixed Income Credit" (16 Feb 2023; "design sophisticated models," Python, "single-name credit" preferred) and "Credit Analyst - Convertible Arbitrage" (undated; "capital structure, liquidity, covenants"). DWS credit-trader posting (7 May 2026): execute PM orders "across multiple venues," "build automated solutions," Bloomberg, MarketAxess, Tradeweb, Python, SQL. Robeco: more than 20 fundamental analysts who "can challenge the model where downside risk is not adequately reflected" (7 Sep 2026) | Clean data, honest backtests, execution as a cost line, a human gate on the model | Ch 4, Ch 7, Ch 9, Part VII |
| Multi-strategy pod (Tuesday) | PM, analyst, platform risk (Chapter 8-B's three chairs). Credit PMs hired from banks and rival funds: Millennium (Hedgeweek, 2 Jun 2025), Jain Global (7 Aug 2026), Balyasny's IG long/short team (20 Aug 2026). Two-thirds of Citadel's fixed-income and macro PMs home-grown, and under 1% of applicants accepted (eFinancialCareers, 25 Feb 2026) | Isolating the idiosyncratic view, sizing to a stop, living inside scope | Ch 8, 8-B, 8-C, 8-D, Ch 28 |
| Distressed fund (Friday) | The restricted-list calendar, run by counsel and advisers to keep members trading as long as possible (Moyer, *Distressed Debt Analysis*, pp. 62–64). Man Group's purchase of Bardin Hill, a distressed and special-situations manager of about \$3bn and 48 people (Alternative Credit Investor, 30 Jul 2025) | Reading documents, valuing a plan, knowing your legal state | Part IV (Ch 12-B to 16), Ch 25 |

Theo's own version of this table was thinner (several entries above postdate his Sunday), and his first reading of it was that it listed jobs he was not qualified for. His second reading, near midnight, was better. A Two Sigma credit analyst on a convertible-arbitrage book reads capital structure, liquidity and covenants so that a hedged, model-driven book is not blindsided, which is a restructuring banker's job description with the word "client" removed. The market maker and the pod were the rows where his résumé needed translating, and translating was what the week would be for.

> **Trend Watch.** *Who credit desks hired, 2023–2026, from postings and announced hires.* June 2023: Citadel Securities starts making markets in US investment-grade credit, streaming through MarketAxess and Tradeweb; its head of fixed-income distribution calls credit "a natural expansion" at "the nexus of our fixed income and ETF franchises" (The DESK, 19 Jul 2023). October 2023 to January 2024: the same firm moves its rates COO to credit and hires IG traders from three banks (The DESK, 4 Jan 2024). May 2025: JPMorgan puts its co-head of credit *systematic* trading on its podcast, recorded inside the April 2025 stress (*Market Matters*, 9 May 2025). June 2025: Millennium adds three credit hires, one of them a CDS and CMBS index trader (Hedgeweek, 2 Jun 2025). July 2025: Man Group, which wrote in 2023 that the future of credit investing is quantitative, agrees to buy a distressed manager (Alternative Credit Investor, 30 Jul 2025). August 2026: Jain Global hires a bank's London high-yield head (7 Aug), and Balyasny hires a BlackRock IG co-head to run a team that will "trade both long and short positions in US high-grade corporate bonds and pursue relative-value opportunities" (Hedgeweek, 20 Aug 2026). *What it means for the desk:* the titles moved toward electronic risk pricing on one side and toward documents and distress on the other, and the hybrid seat in the middle is the one this book trains. *What it does not show:* what any firm asks in an interview. No public interview guide was sourced for this box, so it tracks hiring, not questions, and the chapter prints no firm's questions.

Theo closed the laptop at 12:40 a.m. with one useful line written at the bottom of the spreadsheet, in the column he had labeled *What they will actually test*: "What I do when I'm wrong, and how fast." He did not yet know how literally each room would take it.

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

The judgment that matters on a desk is knowing which set of weights a question wants. "What does the CDS curve say this bond is worth?" wants $\mathbb{Q}$; mixing in a historical default rate produces a mispricing that is really a confusion. "How much of this bond do I own?" wants $\mathbb{P}$, and §4D.5 shows what happens when a $\mathbb{Q}$ number sneaks in. Theo would make exactly that mistake in his first week on the desk anyway (Chapter 6 has the receipt). Knowing a distinction and having it in your hands are different stages of the same education.

## 4D.3 Monday, Continued: "I'll Sell You the Bond"

The interviewer erased the swap-spread trade, which felt like a liberty, and drew two dots.

"Forget the market. This bond is worth 100 or 40, fifty-fifty, and nobody knows which. Except some people do. One seller in five is informed and sells only if it's worth 40. Everyone else sells half the time for their own reasons: redemptions, rebalancing, a bad mood. I'm selling you the bond. What do you bid?"

This one Theo knew had a name, because the market maker had sent him a reading list and Glosten and Milgrom's 1985 paper was on it (§3.2 derives it). He reasoned it through anyway, because he had learned on Sunday that he was going to be asked to.

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

> **Poker Table.** Ines's version of this game, which Theo would hear on the desk in October, is shorter. "Every fill is a card face up. The hand history is the list of what you believed after each one." Figure 4-D.2 is that list for six sales. Against an informed seller who keeps selling, the posterior on the bad state climbs from 50% to 92% and the bond's value falls from 70 to about 45; against noise, it wanders around one-half. The part that surprises bankers is the width. The spread is widest at fifty-fifty, where there is the most left to learn, and it *narrows* as the posterior heads toward certainty. Being hit moves the mid; it is not a reason to widen. Replay any hand on the desk's markout sheet (§3.3) and it shows: the dealer who widened after each fill paid the informed client at every step, and the dealer who moved the mid paid once.

![Figure 4-D.2: The live-counterparty update. Left panel: the posterior probability that the bond is worth 40 after each of six trades, for an informed seller who sells six times (0.60, 0.69, 0.77, 0.84, 0.88, 0.92) and for a noise path of sell, buy, sell, sell, buy, buy (0.60, 0.50, 0.60, 0.69, 0.60, 0.50). Right panel: the bid and ask the dealer would quote for the next trade on each path, with the mid falling toward 45 on the informed path and the bid–ask spread *narrowing* from 12 points as the posterior moves away from one-half. Setup as in §4D.3: values 100 or 40, prior one-half, one seller in five informed, uninformed traders sell or buy with probability one-half *(illustrative)*.](assets/figures/ch04d_live_counterparty_update.png)

## 4D.4 Thursday, Replayed Slowly: Make Me a Market

Replay the cold open with Monday in hand, and Theo's three markets become a hand history with a diagnosis attached.

His first market, 180–260, was a guess wearing a bid and an offer. A two-sided market on a number is a confidence interval with money on it, and the useful question is how often it ought to miss. An interval that never misses is too wide to trade on; a reasonable target misses about one time in ten. People asked for a "90% interval" miss far more often than that (Alpert and Raiffa's 1982 report on training probability assessors is the classic), because narrowness feels like competence. For a document Theo had only seen on a screen, a page count he could defend at 90% would have run from something like 130 to 480 *(illustrative: a median of 250, uncertain by a factor of about 1.5 either way)*. That market is ugly. It is also honest, and an honest wide market loses less to someone who knows than a confident narrow one.

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

## 4D.5 Tuesday: Kelly With a Trapdoor

*Vantress Capital Management is the invented multi-manager platform of Chapters 4-C and 8-D. The PM who interviewed Theo ran a third credit pod on the floor, neither Dov Adler's nor Owen Achterberg's, and is a composite; so is the risk manager who joins in §4D.6.*

Owen Achterberg had passed Theo's name along with a one-line email that Theo was never shown and that, Owen said later, read in full: "Knows documents. Has never been stopped out, because he has never had a P&L." The floor held forty pods and one coffee machine. The PM who interviewed him had a monitor covered in sticky notes, one of which said *SCOPE* in capitals, and he asked his question while looking at something else.

"B3 bond. Carry 4.5% a year over financing. One-year default probability 3.1%, recovery 40. How much of your book do you put in it?"

Theo knew this one too, or knew its formula, which is not the same thing. For a bet that earns $c$ with probability $p$ and loses $L$ with probability $q_D = 1-p$, the fraction of wealth that maximizes long-run growth is the Kelly fraction (§28.4; we write $q_D$ for the default probability so that $q$ stays free for inventory, as in §4D.4),

$$
f^\ast = \frac{p}{L} - \frac{q_D}{c} = \frac{0.969}{0.6} - \frac{0.031}{0.045} = 1.615 - 0.689 = 0.926 .
$$

"Ninety-three percent," Theo said, and then heard himself say it. Ninety-three percent of a fund in one B3 bond. The PM looked up from his screen for the first time.

> **Math, Gently.** *Why Kelly maximizes the log, and where the floor gives way.* Bet half your money on a coin and win, and you have 150; lose the next toss and you have 75. Up 50% then down 50% is not flat; it is down a quarter, because losses and gains compound by multiplication. What grows over many rounds is the *average log* of each round's multiplier, and Kelly is the fraction that makes that average as large as possible. The log has one more property that matters in credit. If a single loss can take wealth to zero, the log of zero is minus infinity, and no amount of carry outweighs it. A bond that loses $L$ on default creates exactly that cliff at $f = 1/L$: with $L = 0.6$, a position of $1/0.6 = 167\%$ of the fund is wiped out by one default. That is the *ruin boundary*. Kelly is always inside it, but it only knows where the boundary is if you have told it the right $L$. The full version, with jumps and a random recovery, is in §28.4.

The PM's next question was the one the formula could not answer. "How sure are you about the 3.1 and the 40?" Theo did the derivatives on the whiteboard. The fraction moves by $-p/L^2 = -2.69$ per unit of loss-given-default and by $-(1/L + 1/c) = -23.9$ per unit of default probability. A B3 default probability is known to perhaps a point and a half either way; moving it to 4.6% takes the fraction from 93% to 57%. A recovery fifteen points worse, 25 instead of 40, takes it to 60%. The two uncertainties are the same size, and only one of them can be shrunk by reading.

That was the trapdoor, and Theo found it before the PM had to point. The 40 was an agency's average recovery for bonds like this one. Whether *this* bond recovers 40 depends on whether its first lien is first, whether the agreement permits an uptier or a drop-down, and what sits ahead of it on the day it matters. If the documents allow a non-pro-rata uptier, the worst-case recovery for a holder left outside is near zero, $L$ goes toward 1, and the ruin boundary falls from 167% of the fund to 100%. The intercreditor agreement is the ruin boundary, priced in leverage. Theo said a version of that, and the PM wrote something on a sticky note for the first time.

"Fine. Now the real answer."

The real answer at a pod comes before Kelly is consulted. The pod's capital is allocated, and the allocation comes with a drawdown line: in the shape press reports attribute to one large platform, capital halved after a 5% loss and the pod closed after 7.5% (eFinancialCareers, 5 Dec 2025, citing the WSJ; reported for one firm, never disclosed by it, and not to be generalized). On \$200mm of allocated capital, a high-yield bond at 98 that recovers 40 loses 58 points on default. The largest single long that does not breach the 7.5% line on its own default is

$$
\frac{\$15\text{mm}}{0.58} = \$25.9\text{mm},
$$

and a pod that will not let one default cost more than 2.5% of capital, \$5mm, stops at \$8.6mm. Kelly's 93% is \$185mm. The stop arrives at a number twenty times smaller without being told anything about carry, default probability or recovery, because the stop does not care why the P&L moved.

So where does Kelly fit? It fits as a ceiling on conviction, and the honest version is a fraction of it. Section 28.4 shows that a desk which knows its edge only to within a relative standard error $s$ does best betting $1/(1+s^2)$ of full Kelly; an edge known to within 100% of itself, generous for one credit, gives one-half. "Half Kelly," Theo said, "is full Kelly for someone with a standard error. And the stop is smaller than half, so the stop wins." The PM nodded at the sticky note marked *SCOPE*, which Theo took as approval and which may have been a reminder about something else.

Months later, on the desk, Theo admitted to Ines that he had once said 93% in a pod. "People call that aggressive," she said. "It's not aggressive. It's a resignation letter." Kaz would reach the same 93% from the same agency table in October (§28.4 has the autopsy), which tells you the number is not a personality trait. It is what the formula says to anyone who feeds it three numbers from three different worlds.

> **View From Another Seat.** *The same B3 bond, sized by three other chairs.* A **long-only systematic manager** (Chapter 4's row (i)) sizes it by its share of a tracking-error budget measured in DTS (§8.4): a bond with twice the index's average DTS spends as much budget at a 1% overweight as an average bond does at 2%, and default enters only through the spread. A **dealer** sizes it by inventory: §18.5's bounds cap how many lots the desk will hold before its own quotes skew toward getting out, and the regulatory capital line sits behind that. A **long/short credit fund** outside the pod world has said its rule on the record: "Maximum position size (% of NAV) = loss budget / downside in points," so a 50 bp loss budget against a 35-point downside caps the position at 1.4% of NAV; and for shorts, it added, the loss budget stops setting the size, because "how many bonds you can borrow does" (Ironshield Capital, *Fixed + Floating* E18, "Inside a Long/Short Credit Hedge Fund," 4 Aug 2026). All three, like the pod, put the downside in the numerator's place and the conviction somewhere further down the page.

![Figure 4-D.3: Kelly with a trapdoor. The Kelly fraction $f^\ast = (1-q_D)/L - q_D/c$ as a surface over default probability $q_D$ (1% to 6%) and loss given default $L$ (0.3 to 1.0) at carry $c = 4.5\%$, with the ruin line $f = 1/L$ drawn across it and the pod's dollar stop drawn as a flat ceiling at \$25.9mm on \$200mm of capital (12.9% of the book), with the 2.5% single-default line at 4.3%. Theo's 93% at $(3.1\%, 0.6)$ is one dot; the same dot at $L = 1$ (the non-participating lender after an uptier) shows how far a document can move the floor *(illustrative)*.](assets/figures/ch04d_kelly_trapdoor.png)

## 4D.6 Tuesday, Continued: Pitch Me a Pair

Twenty minutes in, a second man came in, sat down without introducing himself, and opened a laptop. He was from platform risk. He said nothing for ten minutes and then asked one question, which Theo later learned was the question everyone in platform risk at Vantress asked: "What is this book long that it did not mean to be?"

The setup was the PM's. "Pitch me a pair. Long one credit, short another, and tell me what you're left with." He gave Theo the numbers, which were illustrative and which the reader will meet again as someone else's pair in Chapter 8-D's exercises. Long \$40mm of issuer A, spread 380 bp, spread duration 4.2. Short issuer B, a peer, at 520 bp and 4.6. Theo's thesis was the kind he had written in a hundred lender presentations: A has covenant room and B has a 2027 maturity it cannot comfortably refinance, so A should outperform B whatever the market does. The question was how much B to short.

Theo matched duration, because that was the formula he knew from Chapter 4-B: \$40mm × 4.2 / 4.6 = \$36.5mm of B. The PM asked for two other rulers. Matching DTS, duration times spread, gives \$40mm × (4.2 × 380) / (4.6 × 520) = \$26.7mm. Matching an empirical beta of 0.60 from a trailing regression of A's spread changes on B's gives \$40mm × 4.2 × 0.60 / 4.6 = \$21.9mm. Three rulers, three shorts, and a spread between them as wide as the trade.

Then the PM drew the table that every pod draws, with four states of the world down the side.

| P&L in \$mm (long \$40mm A) | Short by duration (\$36.5mm) | Short by DTS (\$26.7mm) | Short by beta (\$21.9mm) |
| :--- | ---: | ---: | ---: |
| Both widen 10% (A +38 bp, B +52 bp) | +0.24 | 0.00 | −0.11 |
| Both widen 50 bp in parallel | 0.00 | −0.23 | −0.34 |
| Idio: A tightens 15 bp | +0.25 | +0.25 | +0.25 |
| Idio: B widens 20 bp | +0.34 | +0.25 | +0.20 |

"Which row are you paid in?" the PM asked. Theo pointed at the two idio rows. "And how big are they compared with the rows you're not paid in?" The alpha in the third row is \$0.25mm. The ruler error in the first two rows runs from \$0.11mm to \$0.34mm. The thing Theo wanted to be paid for was the same size as the thing his choice of formula would pay or charge him by accident.

What Theo learned in the next five minutes was that idio is not a property of a trade. It is whatever the hedge model leaves behind, and choosing the model is choosing what you will call alpha afterward. "Because it is the formula" had no answer to the first row: when spreads widen in proportion, which is what high-yield spreads mostly do (§8.4), a duration hedge leaves the pair net short the market: it makes money in a proportional sell-off and gives it back in a rally, a view he had not meant to hold. DTS is built for that week. It fails in the second row, the parallel shift, which is what a rates-driven or technical move looks like. Beta is the empirical answer and drifts with the window it was fitted on. The PM's version: say which ruler, say which state it is wrong in, and say why that state is the one you can live with.

The risk manager's question had a concrete answer once the ruler was chosen, and it came in sizes rather than adjectives. On the DTS hedge the book is long nothing on an ordinary day, loses about \$0.23mm in a 50 bp parallel widening, and is long A's default, which is where the morning's stop came back: \$40mm of A loses \$23.2mm if A defaults, through the firing line on its own, and B's short does not help that day. The single-default line puts the long at \$8.6mm; if the prime broker can find only \$12mm of B to lend *(illustrative)*, the DTS ratio caps it at \$18mm. Size to the stop and to the borrow at once, and the smaller number wins: \$8.6mm long, \$5.7mm short. At that size, fifteen basis points of A outperforming is worth \$54,000, the honest size of the alpha in a pitch that started at \$40mm.

> **The Pair.** *Interview exercise, not a Pair Book entry (illustrative numbers; issuers A and B are generic).* **Thesis.** A, with covenant room, outperforms B, a peer with a 2027 maturity it cannot comfortably refinance, over six months; the date Theo agrees in advance to be wrong is B's refinancing announcement. **Legs.** Long A (380 bp, spread duration 4.2); short B (520 bp, 4.6), borrowed through the prime broker. **What the hedge removes.** At the DTS ratio of 0.667, the proportional market move that dominates most high-yield weeks (§8.4). **What idio remains.** A's tightening and B's widening relative to the sector, worth about \$54,000 per 15 bp of outperformance at the final size. **What leaks.** A parallel widening (−\$0.23mm per \$40mm of long), the ruler's drift if A and B stop moving in proportion, and A's jump to default, which no spread ratio hedges (Chapter 5, Chapter 8-D §8D.4). **What it costs.** At \$40mm, A's spread earns \$1.52mm a year and the short pays away \$1.39mm of B's, and a 75 bp borrow fee on \$26.7mm takes the spread carry to about −\$0.07mm a year, before financing, rebate and two half-spreads in and out on both legs. **Size.** The smaller of the stop (\$8.6mm long at a 2.5% single-default line on \$200mm) and the borrow (\$18mm), so \$8.6mm. Chapter 8-D owns the short-leg menu and the full ruler comparison, and Chapter 8-B owns the stop.

The risk manager closed his laptop. "Long A's jump," he said. "That's what it's long that it didn't mean to be. Write it on the ticket." It was the only sentence he said in the interview, apart from the question. Theo wrote it on the back of his hand, which is not a ticket, but it was what he had.

## 4D.7 Wednesday: Fermi With Credit Numbers

The systematic manager's office was quiet in the way a library is quiet, which is to say full of people concentrating and slightly resentful of footsteps. The researcher who interviewed Theo had a kitchen timer shaped like a tomato, set it to ninety seconds per question, and explained that the timer was not there to rush him but to make sure she stopped talking.

The questions were estimates, and each had a true number somewhere in the public record, which she had in a folder. What she was grading was the chain, not the endpoint.

*DV01 on \$10mm of a ten-year bond.* Theo used Chapter 4-B's arithmetic without knowing yet that it was Chapter 4-B's: a modified duration near 8, a price near 108, so about \$8 per \$1mm per basis point per point of duration times 1.08, or roughly \$8,800 per \$10mm. The anchor in her folder was the stylized 4.50% ten-year note of Table 4B.1 on 20 February 2020: \$8,785.

*How much trades on TRACE in a day?* He guessed "fifty to a hundred billion," and she asked "which TRACE?", which was the real question. The DESK put average daily volume at \$70.2bn in March 2026 (Appendix C), and FINRA's monthly volume files split the tape by product: investment grade and high yield, agencies, securitized products. Before quoting a daily volume in a room, it pays to know which of those the source counted. The definition is part of the error bar.

*How many firms print a block on an average day?* He had no idea and said so, then reasoned from the number of dealers he had seen on a closing call. The folder said 24.51 firms reported at least one trade of \$25mm or more on an average day in 2025, up from 17.27 in 2023 (FINRA TRACE Fact Book, Table C12; §2.8).

*What does one non-bank trade?* IFR's estimate, via Rupak Ghose, put Citadel Securities at about \$2bn of corporate bonds a day in 2025 (§2.8). Jane Street's own pages say it traded "more than \$900 billion with clients globally in 2025" and prices "more than 25,000 bonds." Theo divided \$900bn by 252 trading days, got \$3.6bn a day, and was about to conclude that Jane Street traded nearly twice what Citadel Securities did when the researcher held up a hand. One number is corporate bonds from an estimate; the other is all fixed income with clients, globally, from the firm. The comparison was a units error with a nice round answer.

*What does a portfolio trade look like?* A Goldman credit-trading partner described about 8,000 portfolio trades for more than 300 clients in 2023, averaging about \$60mm across about 100 CUSIPs (Coalition Greenwich webinar, January 2024; paraphrase). That is about \$480bn a year, roughly \$1.9bn a trading day, in lines averaging \$0.6mm each: the small tickets of a big trade.

*How much balance sheet does it take to make markets in high yield?* There is no true number here, and the researcher said so, which Theo liked. He built one *(illustrative)*: quote 300 names in \$2mm clips, let inventory run to five clips either way before the quotes lean hard (§18.5's bounds), and the worst case is \$3bn of gross inventory. Hedges and netting bring the typical day to perhaps a quarter of that, and at a 10% capital haircut the desk needs something like \$75mm of capital at risk. For scale, an ETP market maker reported EUR 771m of trading capital for its whole business at 31 March 2020 (Flow Traders, Q1 2020 trading update). Two more chains came the same way, both illustrative: a high-yield index position with a risky duration near 4.2 has a DV01 of about \$420,000 per basis point per \$1bn, and a venue with \$9.6bn of average daily volume (Trumid, June 2026) in lines near \$1mm handles something like ten thousand lines a day, most of them untouched by a human (88% no-touch on eligible RFQ lines; The DESK, October 2025).

> **Math, Gently.** *Why a Fermi chain's errors add up in logs.* A Fermi estimate is a product of ratios: names times clip times inventory limit times netting times haircut. Each factor is known only roughly, say "within a factor of two." Take logs and the product becomes a sum, $\ln(\text{answer}) = \sum_i \ln(\text{factor}_i)$, so the errors add in log space too. If four factors are each off by up to a factor of two and their errors are independent, the log errors combine like independent noise, in quadrature: $\sqrt{4} \times \ln 2 \approx 1.39$, a combined factor of about 4. If they all err in the same direction, the errors stack, $4 \ln 2$, a factor of 16. The interviewer wants to see the chain, a range for each link, and a sentence on which link is the widest. The habit transfers directly to sizing a trade, where the widest link is usually the recovery. The full version of error propagation through products is in §28.2's treatment of noisy hit rates.

## 4D.8 Wednesday Afternoon: The Coding Screen

After lunch the researcher opened a laptop with a file that looked like TRACE and was not quite: twelve thousand prints, some cancelled, some corrected, some reported late "as/of," and a column of ratings. There were three tasks, forty-five minutes, and a Python environment with pandas.

The first was to tidy the tape: drop cancelled prints, replace corrected ones with their corrections, and keep the late reports at their trade time rather than their report time. FINRA's Rule 6730 is why the file looked like that. A dealer has fifteen minutes from execution to report a corporate bond trade, and anything reported later is flagged "as/of"; a back-test inherits every cancel, correction and late print the operations desk ever cleared. Appendix B's tidy-panel specification (§B.16) is the long version.

The second task was the join, and it was where Theo lost. Each print needed the issuer's rating attached. He merged the tape to the ratings table on issuer ID, the ratings table carried each issuer's rating *as of today*, and every trade in 2024 now knew about every downgrade that happened in 2025. His back-test of "sell on downgrade" looked wonderful. The researcher let him finish, then asked what date the rating column belonged to. He looked at the column for a long time. Jane Street's Eric Mannes put the general case on the firm's podcast: a back-test is "simulating what you would've done if you had a time machine," and the defense is to "save all the data that we have access to along with the time we received it" (*Signals and Threads*, Ep 29, "Wrestling the World into Rows," 2 Sep 2026). The fix is an as-of join that, for each trade, takes the latest rating *published before* the trade. It is one line of pandas once you know to want it.

> **Math, Gently.** *Why a join needs two clocks.* Every fact in a credit database has two times attached: when it was true, and when you could have known it. A downgrade is "effective" on one date and appears on a screen at a particular minute; a 10-Q covers a quarter that ended weeks before the filing; a TRACE print reported as/of was executed earlier than it was reported. A back-test that joins on the first clock alone quietly lets the past read the future. Picture two transparent sheets, one per clock, laid over a calendar: a fact may enter a trade's row only if it is to the left of the trade on *both* sheets. The full version is the point-in-time discipline of §7.7 and §7.9.

The third task was cross-validation for a model predicting bond returns: purged, embargoed and grouped by issuer. Theo knew the words because the same reading list had included López de Prado's chapter on cross-validation in finance, and he knew why each mattered. Purging drops training labels whose windows overlap the test period; the embargo drops a buffer after it, because returns are serially correlated; grouping by ultimate parent keeps an issuer's eleven bonds from appearing on both sides of the split, which is §7.6's forty-seven hats in another costume. Ten lines, written slowly, with one bug the researcher pointed out (he grouped by ticker, and two of the tickers were the same company).

#### Quant-Shop Life: The Feedback Form, Wednesday, 5:10 p.m.

*A fictional composite of a systematic asset manager's hiring process; no firm's form or rubric.*

Theo's afternoon ended at four. The researcher's ended at 6:20, and most of what happened in between was a web form. The applicant-tracking system wanted four scores from one to four (probability, estimation, coding, communication), a recommendation from a drop-down (*strong no, no, yes, strong yes*), and a free-text box that could not be left empty and could not exceed 1,500 characters. She wrote 1,488. She gave the join a 2 and then changed it to a 3, because he had found the bug himself once asked the right question, and the rubric said "recovers from error with prompting" was a 3. She spent eleven minutes on whether "communication" meant how he spoke or how he wrote his code, decided it meant both, and averaged. At 5:40 the system logged her out for inactivity while she was looking up how many firms print a block a day, to check that her own folder was right, and she retyped the box from memory. Thursday at 5:30 there would be a calibration meeting, where four interviewers would discover that one colleague's 3 was everyone else's 2 and spend forty minutes on it. Nobody would mention the tomato timer. It was, she thought, the best-calibrated instrument in the building.

Theo later wrote his own drill set from the week, partly to stop replaying the join in his head. The problem it solves is the one every candidate has after a week like this: the games are learnable, but only by doing them under a clock with an answer key you did not write after seeing the question. `interview_drills.py` is a seeded generator of the §4D.2–§4D.7 puzzles. Each drill draws its inputs from a small menu with a random-number generator fixed by a seed, so a session can be repeated exactly and a different seed gives new numbers to keep you from memorizing answers. Each drill returns three things: the question as text, the answer computed from the formula in its home section, and a checker that accepts a reply within a tolerance suited to mental math (half a point of probability, a quarter of a point of price, a tenth of a million dollars of size). The answer key is the formula, not a stored number, which is the design choice that makes the drills trustworthy. The inputs are a seed and a count; the output is a list of (question, answer, checker) triples, and running the file checks the chapter's own anchors before printing a session: 25% and 19.2% for §4D.2, 64 for §4D.3, 0.926 for §4D.5, \$25.9mm for the stop, \$26.7mm for the DTS short, and the 4-B DV01.

It is for speed and for catching this chapter's slips: the second sale treated as the first, the forgotten rate, the duration ruler where DTS was asked. It will not teach judgment. No drill asks "which measure?" in a form a checker can grade, and the pitch of §4D.10 has no answer key at all. The edge case that bites is the Kelly drill when there is no edge. If the default probability exceeds $c/(c+L)$, the formula returns a negative fraction, and a naive drill would ask you to "size" a short you never chose to make; this one returns `None`, meaning *no bet*, and the checker expects you to say so. The listing is [Listing 4-D.1 in Appendix F](#code-4D-1).

<!-- EXPLAINED -->
```python
"""interview_drills.py: seeded drills for Chapter 4-D (illustrative numbers).

Each drill returns (question, answer, check); check(x) is True when x is within
the drill's tolerance of the answer. Home sections are in the docstrings.
"""
import math
import random


def _check(answer, tol):
    return lambda x: x is not None and abs(x - answer) <= tol


def measure_drill(rng):
    """§4D.2: two-point bond, risk-neutral default probability, with a rate."""
    hi, lo = 100.0, rng.choice([20.0, 30.0, 40.0, 50.0])
    price = rng.choice([80.0, 85.0, 88.0, 92.0])
    r = rng.choice([0.0, 0.02, 0.04])
    q = (hi - price * math.exp(r)) / (hi - lo)   # undiscounted mean under Q
    text = (f"Pays {hi:.0f} or {lo:.0f} in one year; price {price:.0f}; "
            f"rate {r:.0%} continuous. Q-default probability?")
    return text, q, _check(q, 0.005)


def gm_drill(rng):
    """§4D.3 and §3.2: value after n sells from new sellers, two-point prior."""
    hi, lo = 100.0, rng.choice([30.0, 40.0, 60.0])
    pi = rng.choice([0.1, 0.2, 0.3])
    n = rng.randint(1, 4)
    p_sell_bad, p_sell_good = pi + (1 - pi) / 2, (1 - pi) / 2
    odds = (p_sell_bad / p_sell_good) ** n       # prior odds 1: fifty-fifty
    post_bad = odds / (1 + odds)
    value = post_bad * lo + (1 - post_bad) * hi
    text = (f"Worth {hi:.0f} or {lo:.0f}, fifty-fifty; {pi:.0%} of sellers "
            f"informed. Value after {n} sells from new sellers?")
    return text, value, _check(value, 0.25)


def kelly_drill(rng):
    """§4D.5 and §28.4: discrete Kelly for a bond; None means no edge, no bet."""
    c = rng.choice([0.03, 0.045, 0.06])
    q_d = rng.choice([0.01, 0.031, 0.05, 0.08])
    loss = rng.choice([0.4, 0.6, 0.8, 1.0])
    f = (1 - q_d) / loss - q_d / c
    text = (f"Carry {c:.1%}, PD {q_d:.1%}, LGD {loss:.0%}. "
            f"Full-Kelly fraction of NAV (None if no edge)?")
    if f <= 0:
        return text, None, lambda x: x is None
    return text, f, _check(f, 0.01)


def stop_drill(rng):
    """§4D.5 and §8D.5: largest long that one default cannot push past a line."""
    capital = rng.choice([100.0, 200.0, 400.0])               # $mm
    line = rng.choice([0.025, 0.05, 0.075])
    price, recovery = rng.choice([(98.0, 40.0), (90.0, 30.0), (75.0, 25.0)])
    size = capital * line / ((price - recovery) / 100.0)
    text = (f"Capital ${capital:.0f}mm; one default may cost {line:.1%}. "
            f"Bond at {price:.0f}, recovery {recovery:.0f}. Largest long, $mm?")
    return text, size, _check(size, 0.1)


def ruler_drill(rng):
    """§4D.6 and §8D.3: short size under the duration, DTS or beta ruler."""
    long_mv = rng.choice([20.0, 40.0, 60.0])
    s_a, d_a = rng.choice([(380, 4.2), (300, 5.0), (450, 3.8)])
    s_b, d_b = rng.choice([(520, 4.6), (600, 4.0), (410, 5.2)])
    beta = rng.choice([0.5, 0.6, 0.8])
    ruler = rng.choice(["duration", "dts", "beta"])
    short = {"duration": long_mv * d_a / d_b,
             "dts": long_mv * d_a * s_a / (d_b * s_b),
             "beta": long_mv * d_a * beta / d_b}[ruler]
    text = (f"Long ${long_mv:.0f}mm of A ({s_a}bp, spread duration {d_a}); "
            f"short B ({s_b}bp, {d_b}); beta {beta}. Short by {ruler}, $mm?")
    return text, short, _check(short, 0.1)


def dv01_drill(rng):
    """§4D.7 and §4B.5: DV01 per $10mm = D_mod x dirty price x face x 1e-6."""
    d_mod = rng.choice([3.9, 4.2, 6.5, 8.11])
    price = rng.choice([92.39, 100.0, 108.38])
    dv01 = d_mod * price * 10_000_000 * 1e-6
    text = f"Modified duration {d_mod}, dirty price {price}. DV01 per $10mm?"
    return text, dv01, _check(dv01, 0.05 * dv01)              # mental-math band


DRILLS = [measure_drill, gm_drill, kelly_drill, stop_drill, ruler_drill,
          dv01_drill]


def session(seed, k=6):
    """A reproducible set of k drills: same seed, same questions."""
    rng = random.Random(seed)
    return [rng.choice(DRILLS)(rng) for _ in range(k)]


if __name__ == "__main__":
    # The chapter's anchors, recomputed from the drill formulas.
    assert abs((100 - 85) / 60 - 0.25) < 1e-12                    # §4D.2
    assert abs((100 - 85 * math.exp(0.04)) / 60 - 0.192) < 1e-3   # §4D.2, 4%
    assert abs(0.6 * 40 + 0.4 * 100 - 64.0) < 1e-12               # §4D.3
    assert abs(0.969 / 0.6 - 0.031 / 0.045 - 0.926) < 1e-3        # §4D.5
    assert abs(15 / 0.58 - 25.86) < 0.01                          # §4D.5 stop
    assert abs(40 * 4.2 * 380 / (4.6 * 520) - 26.69) < 0.01       # §4D.6 DTS
    assert abs(8.11 * 108.38 * 10 - 8789.6) < 1.0   # §4D.7 (4-B prints $8,785)
    for text, answer, check in session(seed=2026):
        print(text)
        assert check(answer)
```

## 4D.9 Thursday Afternoon: Kaz Asks Theo to Break It

"You'll do," it turned out, meant "you'll do the next room." At 1:30 Theo was shown into a smaller glass room where Dr. Kasimir Lind, whom everyone called Kaz, sat behind a laptop with a slide already up. Kaz was not in the morning's market; Kaz was the afternoon's model.

The slide was a backtest Kaz had built for interviews, on purpose, to be broken. A high-yield long/short signal, 6.2% a year of gross alpha at 2% tracking error, an information ratio of 3.1. "Why is my Sharpe 3.1?" Kaz asked, sounding genuinely curious, as if the number had arrived in the mail.

Theo asked the questions he would have asked of a CIM. How many companies? What does it cost to trade? Kaz answered the second cheerfully: turnover eight times a year one way, transaction costs "set to zero so they wouldn't bias the results." That is sixteen dollars traded per dollar of book a year. To keep an information ratio of 0.5, net alpha has to stay at 1%, so costs can eat 5.2% a year, 32.5 bp per dollar traded; at 38.75 bp the whole 6.2% is gone (Chapter 4, Exercise 2). A high-yield half-spread on an institutional ticket runs to an eighth or a quarter of a point on a liquid bond, and more on the bonds a cheap-decile signal likes *(illustrative)*. At 25 bp the IR is 1.1, not 3.1. "Your Sharpe," Theo said, "is mostly the bid–offer you didn't pay."

Kaz's second question was the issuer count, posed as a puzzle. "The US high-yield index had 784 issuers on 31 May 2018, 576 with public equity. My panel has forty thousand bond-months. How many independent observations a month?" Theo answered as a banker: at most 784, fewer by ultimate parent, fewer again for anything needing an equity price, and next month's cross-section is mostly this month's companies a month older. Rows are not observations; issuers are, and slowly (§7.6 makes this a number, $N_{\text{eff}}$). Kaz looked pleased. It is worth recording that Kaz asked exactly the right question in June and failed it on their own slide in October (§7.0), which is the most common way quants know things.

Near the end Kaz closed the laptop and asked a question that was not on any rubric. "Is a *fulcrum* the thing you hang the hedge from?"

Theo started to explain that the fulcrum is the class where the value runs out: the class that is impaired but still in the money, the one that ends up owning the reorganized company. Halfway through the sentence he stopped, because Kaz was half right. In the pod's version of an RSSG trade (§3.7), long the fulcrum and short the class junior to it, sized so that a default costs nothing, the hedge does hang from the fulcrum. "In a capital-structure pair," he said, "yes. Everywhere else, no." Kaz wrote it down. Theo did not know until his second week on the desk that Kaz writing something down was the highest compliment the desk offered.

## 4D.10 Friday: The Thirty-Minute Credit Pitch

The distressed fund occupied half a floor of an older building and had the furniture to prove it. On the conference-room wall hung the restricted-list calendar, colored bars one per company, which is how a fund on a creditor committee tracks when it can trade: information goes first to the committee's advisers and counsel so members stay unrestricted as long as possible, and a restricted holder is freed only when the information is public or stale (Moyer, *Distressed Debt Analysis*, pp. 62–64). Theo had spent six years on the other side of those bars, deciding who could be told what and when.

The PM had been buying bonds since before TRACE, and said so in the first minute. "We interviewed by phone and by grudge," she said, and Theo laughed because he thought it was a joke. Months later he heard Mags Dunleavy use the same words about pricing bonds and realized that either the two of them had overlapped somewhere or the phrase was older than both. He never asked which.

"Thirty minutes. Pitch me something."

He pitched the second-lien notes of a sponsor-owned building-products company he called Company A on his single page *(fictional; every number illustrative)*, because PJT had trained him to call everything Company A. The notes were at 62. He gave it as a memo: a recommendation (buy), a thesis (the sponsor would rather exchange than file, and the exchange math worked for second-lien holders at 70), a downside case (a filing with second-lien recovery in the mid-30s), and three comparable situations. It was a good memo. The PM asked to see the liquidity forecast behind it, and Theo took the USB stick out of his jacket for the first time all week and plugged it into her laptop. The 13-week model opened, all forty tabs of it. She scrolled through the cash roll with the expression of someone reading a letter from an old friend.

"This," she said, "is the first thing anyone has shown me this year that I believe." She offered him the seat before the half hour was up, starting whenever PJT would let him go.

Then she did something he did not expect. "Now give it to me the way the people you saw yesterday would want it. I've lost two analysts to market makers this year, and I'd like to know what they were told."

So he pitched it again, and the second version is the one this book has been building toward. The 13-week model became a hazard, crudely: he counted the weeks until the downside case crossed the minimum-liquidity floor and called it a survival curve with one path (§5.1.5 turns one path into thousands and a curve into a hazard rate). The horizon became six months, not "through the restructuring" (§3.1.3: the desk does not hold to resolution). The outcome became three doors with his own physical-measure weights on them, the RSSG downside case promoted from a scenario to a tail:

| Door at six months | Price | His weight ($\mathbb{P}$) |
| :--- | ---: | ---: |
| Refinanced or amended | 85 | 0.45 |
| Exchange into new notes | 70 | 0.35 |
| Filing | 35 | 0.20 |

The mean is $0.45(85) + 0.35(70) + 0.20(35) = 69.75$, about 7.75 points above the 62 price, and the standard deviation is about 18.6 points. That is the pitch in one line: an expected gain of 12.5% over six months with a typical swing more than twice as large. A desk can grade that. A desk cannot grade "buy."

The hedge made it a pair, which is what the pod had taught him on Tuesday and what the market maker would ask of every position he ever took. A short in a high-yield index sized by the bond's beta removes the part of the 7.75 points that is just the market (§8.6's hedge matrix), so what is left is the question of which door, which is the part he actually knew something about. He named the short (index protection, because no lender would lend him Company A's peers in size), the ruler (DTS while the notes traded above 70, market value below, as Chapter 8-D does it), the stop size (the filing door costs 27 points, so a 2.5%-of-capital single-name line caps the position at 9.3% of capital), and the markout horizon: twenty trading days, the desk's own clock (§3.3). Then he gave the date he agreed in advance to be wrong, the habit Dov Adler's thesis sentences are built on (§8D.1): "If the company hasn't launched an exchange by 30 September, I'm wrong about the door, and I'm out."

Last came the markout test. On Tuesday's train home he had gone back through nine situations from his PJT years, anonymized and numbered, using only public prices: at each public milestone, what his downside case had said, and where the bonds traded on TRACE twenty days later. The case had the direction right six times; in five of those six, the price had moved before the case was written. "So my edge," he said, "was in knowing what would happen, not in knowing it first." The PM looked at him for a long moment. "That's the most expensive sentence anyone's said in this room this year."

The memo won the room. The distribution would win the desk. The PM had offered him a seat on the strength of the first pitch and was, he could tell, slightly irritated by the second, the way a craftsman is irritated by a machine that does half her job adequately.

He declined on Monday, and the reason fits in a paragraph. The distressed fund already knew what he knew: it had a calendar on the wall and a PM who had read more credit agreements than he had. He would have been a good analyst there and learned nothing he could not have learned at PJT. The market maker did not know what he knew. Its people could price adverse selection in three seconds and had never been inside a lender call; Kaz had asked about the fulcrum and meant it. A seat where your knowledge is scarce is worth more to you, and to them, than a seat where it is the furniture.

> **View From Another Seat.** *The same pitch, heard in three other rooms of Chapter 4-C.* A **direct lender** would skip the price table and ask about the documents: can it hold the loan to maturity, who controls an amendment, what the sponsor has promised. A hold-to-maturity book marks to a model, so the six-month distribution matters to it mostly as a covenant conversation. A **CLO manager** would ask first whether the notes are, or will soon be, rated CCC, because a CCC bucket over its limit gets haircut in the overcollateralization test (§4C.4), and the pitch's best door, the exchange, can be the worst one for the manager if the new notes are rated lower. An **insurer** would ask about the regulatory designation and the capital charge before the return (§4C.5); a 7.75-point expected gain on a security with a punitive charge can be a loss on capital. Each hears a different pitch in the same thirty minutes, because each is paid in a different unit.

What Theo wrote on the train home, in the notebook he would bring to the desk in September, was a translation table for his own résumé. It belongs in Appendix A's phrasebook (§A.10), where the full dictionary lives, but its first rows are his:

| On the RSSG résumé | On the desk | Where the book trains it |
| :--- | :--- | :--- |
| Built 13-week cash flow forecasts | Built a weekly liquidity-runway series and turned it into a hazard rate | §5.1.5 |
| Ran downside cases | Estimated a left tail at a stated horizon | §3.1, Ch 5 |
| Covenant cushion analysis | Distance to a barrier | Ch 6 |
| Mapped the lender group | Built a holder vector from Rule 2019 statements | §13.2, §25.7 |
| Advised on liability management | Priced seniority as a document variable with a date | Ch 13, §13.8 |
| Recovery waterfalls | Recovery distributions with a floor set by the documents | §5.5, Ch 12-C |
| "The lenders will never agree" | A vote as a probability, updated on each signing | §13.4, Ch 14 |

The last thing on the page was a note on how he wanted to be judged, because §3B.7 would later tell him he would be measured whether he asked or not. Year-one P&L is mostly noise: forty calls with a 55% hit rate have a standard error of $\sqrt{0.55 \times 0.45 / 40} \approx 7.9$ points, so a 55% year is statistically indistinguishable from a coin (§28.2). The fairer measures are calibration (do his 70% calls come true about 70% of the time?), the correlation of his calls with the price factors (low is good: it means he is adding information the index does not have), and the hit rate with its standard error printed next to it. Section 28.8 makes the same argument from the desk head's chair.

## 4D.11 The Portfolio: Twelve Projects That Prove It

On Saturday ROBO offered to build all twelve.

ROBO was the coding agent Theo had been paying for himself since the spring. He had given it a list of twelve projects that, together, would show a desk he could do the job, and within a minute it replied that it could have all twelve done by Sunday night, without enthusiasm or doubt, as it said everything.

Theo declined, and his reason was the study protocol the ramp at the front of this book describes. The core of each project, the part a desk head will ask about (Tier 2: derive it and build it by hand), he would do himself. The plumbing (Tier 3: loaders, plots, file handling) ROBO could build, and then Theo would break it on purpose and see whether its tests caught him. The asserts are the grade: acceptance tests written before the code, which fail when the code is wrong, are evidence; a project that merely runs is not. He had a number to keep him honest: in METR's 2025 randomized trial, experienced open-source developers allowed AI tools were 19% *slower* on real issues and afterward believed they had been about 20% faster (§26.9, item 8). One real market maker's recruiting pages say that at the firm "feedback on successes and failures is quick and tangible" (Jane Street, firm culture pages). A portfolio is the candidate's attempt to make his own feedback tangible before anyone hires him to.

| # | Project and question | Public data · engine | Acceptance test | The one figure, and what a desk head reads in four minutes | By hand first, then ROBO |
| :-- | :-- | :-- | :-- | :-- | :-- |
| 1 | TRACE panel and the Roll spread by trade size: how wide is the market for whom? | TRACE (App B §B.1, §B.16) · Roll estimator (§18.2) | Cancels and corrections netted; as/of prints kept at trade time; Roll spread non-negative after the fix | Spread by size bucket; whether small tickets pay more | The cleaning rules; ROBO the loader |
| 2 | Priming Risk Score on fifty EDGAR credit agreements: which documents permit an uptier? | EDGAR exhibits · PRS (§13.8, §25.3) | Hand-labeled ten agree with the score's top flags | Score against later LMT events; the false positives explained | Label ten agreements yourself |
| 3 | Rule 2019 holder panel: who owns the case? | Court dockets (§25.7) | Holdings sum to the class within stated rounding | Holder concentration over time | Read three statements first |
| 4 | RFQ quoting game with a hand history: does the desk lose to the informed tier? | Synthetic RFQs · §18.7, Ch 18-B | Markouts by tier recover the planted toxicity | Markout curve by client tier | The win curve's likelihood |
| 5 | March 2020 ETF premium decomposition | ETF NAV and price · §20.2–20.5 | Components sum to the discount each day | Discount, split into its parts, 9–23 March 2020 | The NAV-staleness term |
| 6 | DD→PD map with issuer-grouped CV | Equity and filings · §6.4, §7.7, §11.3 | No issuer in both train and test folds | Calibration curve, in-sample against out | The grouping key (ultimate parent) |
| 7 | Fallen-angel overhang: how long does forced selling last? | Index and TRACE · §16.2 | Event window excludes the downgrade's own day | Price path after downgrade, with the overhang | The event definition |
| 8 | CDS bootstrap and basis monitor | Public CDS quotes · §6.8, §24.7 | Survival curve monotone; repricing within a basis point | Bond–CDS basis for one issuer over a year | The bootstrap |
| 9 | Two-state regime filter on FRED OAS, April 2025 out of sample | FRED HY OAS · §12.4 | Filtered, not smoothed, probabilities in the backtest | Regime probability through April 2025 | The filter recursion |
| 10 | The re-default clock | Public distressed-exchange lists · §14.3 | Each company counted once per exchange | Survival after exchange against after emergence | The censoring |
| 11 | Definition graph and the add-back fixed point for one agreement | One credit agreement · §25.2–25.3 | Fixed point reached; cycle reported if none | The definition graph with the add-backs that move EBITDA | Read the definitions article |
| 12 | Your own 13-week model as a hazard, with a markout test | Your anonymized model, public prices · §5.1.5, §3.3 | Hazard from simulated paths, not one downside case | Hazard curve, and markouts after each milestone | All of it |

Each business weighs the twelve differently, and a candidate with limited weekends can choose accordingly *(illustrative weighting, built from §4D.1's table)*:

| Business | Projects it weighs most |
| :--- | :--- |
| Market maker | 1, 4, 5 |
| Multi-strategy pod | 8, 12, and any pair built on 2 or 11 |
| Systematic asset manager | 1, 6, 9 |
| Bank credit-trading desk | 1, 5, 8 |
| Distressed fund | 2, 3, 10, 11 |

Theo built three before September: the first, the fourth and the twelfth. The fourth taught him the most, because the synthetic informed tier he planted kept winning against his own quoting rule for two weekends, until he moved the mid before he widened.

## 4D.12 Sixty Tagged Problems

The week, broken into sixty problems. Tags: [Read] means the answer is in the home section; [Derive] means pencil; [Build] means code, with tests first. Times are minutes for a prepared reader. Solutions are in Appendix Z.

| # | Tag | Min | Problem | Home |
| --: | :-- | --: | :-- | :-- |
| 1 | Read | 5 | Bond pays 100 or 40; price 85; zero rates. $\mathbb{Q}$-default probability? | §4D.2 |
| 2 | Derive | 5 | The same at a 4% continuous rate. | §4D.2 |
| 3 | Derive | 10 | Add an exchange door at 70; give two weightings that price at 85. | §3.1.2 |
| 4 | Derive | 10 | Physical PD 10%: expected return at 85, and what it pays for. | §5.1 |
| 5 | Read | 5 | Which measure for a CDS hedge, a Kelly size, a P&L forecast? | §4D.2 |
| 6 | Derive | 5 | Spread 300 bp, recovery 40%: hazard rate by the credit triangle. | Ch 6 |
| 7 | Derive | 15 | Variance of the two-point and three-point bonds at the same price. | §3.1.1–3.1.2 |
| 8 | Build | 20 | $\mathbb{Q}$-PD across recoveries 20–60 at a price of 85. | §4D.2 |
| 9 | Derive | 5 | Values 100/40, one seller in five informed: bid and ask. | §3.2.1 |
| 10 | Derive | 5 | The bid after a second sale from a new seller. | §4D.3 |
| 11 | Derive | 10 | The bid after a second sale from the same seller. | Exercise 3 |
| 12 | Derive | 10 | How many sales from new sellers push the value below 50? | §4D.3 |
| 13 | Read | 5 | Why does the spread narrow as the posterior moves? | §4D.3 |
| 14 | Derive | 15 | Informed fraction uniform on 0–0.4: the bid. | §3.2.2 |
| 15 | Derive | 15 | The winner's curse with three dealers. | §3.2.3 |
| 16 | Build | 30 | Simulate fifty RFQs and plot the hand history of posteriors. | §3.3 |
| 17 | Read | 5 | A 90% interval for the number of US HY index issuers in May 2018. | §7.6 |
| 18 | Derive | 10 | Reservation-price shift at $q = -2$, $\gamma = 0.005$, $\sigma^2\tau = 1.27$. | §18.4.2 |
| 19 | Derive | 10 | The greed term at $k = 3$, $\gamma = 0.005$. | §18.4.2 |
| 20 | Read | 5 | Name a quote whose number has a document answer. | §4D.4 |
| 21 | Derive | 15 | A 25% hit-ratio target: what does its shadow price buy? | §18.7 |
| 22 | Derive | 15 | Four of your ten "90%" intervals missed. How surprised should you be? | §4D.4 |
| 23 | Build | 30 | The page-count game against an informed buyer, scored by markouts. | §4D.4 |
| 24 | Derive | 10 | Jump-to-default in the reservation price of a B3 bond. | §18.6 |
| 25 | Derive | 5 | Kelly at carry 4.5%, PD 3.1%, recovery 40%. | §28.4 |
| 26 | Derive | 10 | Its sensitivities to $L$ and to PD. | §28.4 |
| 27 | Derive | 5 | The ruin boundary at $L = 0.75$ and at $L = 1$. | §28.4 |
| 28 | Derive | 10 | Largest long on \$200mm at a 7.5% line, bond at 98, recovery 40. | §8D.5 |
| 29 | Derive | 10 | Fractional Kelly with a 50% relative error in the edge. | §28.4 |
| 30 | Read | 5 | Why a $\mathbb{Q}$ default intensity makes Kelly zero. | §28.4 |
| 31 | Derive | 5 | Loss budget 50 bp, downside 35 points: maximum size. | §4D.5 |
| 32 | Build | 30 | Plot $f^\ast$ over (PD, $L$) with the ruin line and a dollar stop. | Fig 4-D.3 |
| 33 | Derive | 10 | Three rulers: long \$40mm A (380, 4.2), B (520, 4.6), beta 0.6. | §8D.3 |
| 34 | Derive | 10 | The four-state P&L for each ruler. | §4D.6 |
| 35 | Derive | 10 | Spread carry net of a 75 bp borrow at the DTS ratio. | §4D.6 |
| 36 | Derive | 10 | Size to the stop and to \$12mm of available borrow. | §4D.6 |
| 37 | Read | 5 | What is the §4D.6 book long that it did not mean to be? | §4D.6 |
| 38 | Derive | 15 | Jump-neutral short for \$20mm first lien at 98 (recovery 70) against a second lien at 70 (recovery 20). | §3.7, Ch 12-B |
| 39 | Derive | 15 | Capture ratio from idio, leak and friction lines. | Ch 8-C |
| 40 | Build | 30 | The three-ruler comparison on two real spread series. | Ch 8-D |
| 41 | Derive | 5 | DV01 per \$10mm at modified duration 8.11, dirty price 108.38. | §4B.5 |
| 42 | Read | 5 | Which products does a TRACE daily-volume figure count? | App B §B.1 |
| 43 | Derive | 10 | Portfolio-trade dollars a year from 8,000 trades at \$60mm. | §4D.7 |
| 44 | Derive | 10 | High-yield index DV01 per \$1bn at a risky duration of 4.2. | §4D.7 |
| 45 | Derive | 15 | Capital to quote 300 HY names in \$2mm clips. | §18.5 |
| 46 | Derive | 10 | Error bar of a four-link chain, each link within a factor of two. | §4D.7 |
| 47 | Derive | 10 | \$900bn a year with clients: per day, and why it is not comparable to \$2bn. | §4D.7 |
| 48 | Derive | 10 | Lines a day on a venue with \$9.6bn of daily volume. | §4D.7 |
| 49 | Build | 20 | Net cancels and corrections in a TRACE-like file. | App B §B.16 |
| 50 | Build | 15 | As-of join of ratings to prints. | §7.9 |
| 51 | Build | 20 | Purged, embargoed, issuer-grouped CV in ten lines. | §7.7 |
| 52 | Read | 5 | Name the two clocks on a 10-Q. | §4D.8 |
| 53 | Build | 20 | Flag prints reported more than fifteen minutes after execution. | App B §B.1 |
| 54 | Build | 30 | Group CUSIPs by ultimate parent and compute $N_{\text{eff}}$. | §7.6 |
| 55 | Derive | 10 | IR at 8× turnover and 25 bp cost, from 6.2% alpha at 2% tracking error. | Ch 4, Ex 2 |
| 56 | Read | 10 | Rows against issuers: 40,000 bond-months, 784 issuers. | §7.6 |
| 57 | Derive | 15 | Deflate a Sharpe ratio chosen as the best of 100 backtests. | §7.8 |
| 58 | Derive | 15 | Mean and standard deviation of the three-door pitch. | §4D.10 |
| 59 | Derive | 10 | Standard error of a 55% hit rate on 40 calls. | §28.2 |
| 60 | Build | 45 | Your own pitch: a distribution, a hedge, a stop, a markout horizon and a date. | §4D.10 |

## 4D.13 Desk Debrief

On Sunday 28 June, back at the kitchen table, Theo filled in the column he had labeled a week earlier, *What they will actually test*. Monday: which world a number lives in, and whether he could update on a second trade without forgetting the first; a quote's width is what is left to learn, so being hit moves the mid. Tuesday: whether he sized from the downside or from conviction (Kelly said 93%, the stop said \$8.6mm, and the recovery was a document variable), and whether he could say what a hedge leaves behind and which state he was paid in. Wednesday: error bars on estimates and timestamps on joins. Thursday: losing money out loud while naming the fact that moved his number, and breaking a Sharpe of 3.1 by counting trades and issuers. Friday: turning his best skill into a distribution, a hedge and a date, and telling a room where his knowledge was furniture from one where it was scarce.

He looked at the column and saw it was one test in six costumes: how do you lose, and how fast do you change your mind when you do? Then he wrote to Ines to accept, and to PJT to resign, in that order, because the order was the only part of the week that had a document answer.

### The Spec You Hand the Robot

*Vague version:* "Help me practice for quant credit interviews." *What ROBO built:* sixty questions with the answers printed directly beneath each one, as asked. *The precise version:* "Implement `interview_drills.py` per §4D.8. Six drill families (measure, Glosten–Milgrom posterior, Kelly, stop size, hedge rulers, DV01), each returning (question, answer, checker). Inputs drawn from fixed menus by `random.Random(seed)`; the same seed reproduces a session. Answers computed from the home-section formula, never stored. Tolerances: 0.005 in probability, 0.25 points in price, \$0.1mm in size, 5% in DV01. Kelly returns `None` when $(1-q_D)c \le q_D L$. Run as a script, assert the chapter's anchors (25%, 19.2%, 64, 0.926, \$25.9mm, \$26.7mm, 8,790)."

### Exercises

1. **Two measures before breakfast.** A bond pays 100 or 30 in a year; the price is 80 and the continuous rate is 3%. Find the $\mathbb{Q}$-default probability. If the physical default probability is 8%, what one-year return does a buyer at 80 expect, and what is it paying for? *Check:* $q = (100 - 80e^{0.03})/70 = 17.56/70 \approx 25.1\%$. Expected payoff under $\mathbb{P}$ is $0.92(100) + 0.08(30) = 94.4$, about 18% over 80: the premium for holding a 70-point jump, not a forecast error.
2. **The trapdoor opens.** Take Theo's B3 bond (carry 4.5%, PD 3.1%) but suppose the agreement allows a non-pro-rata uptier, so a holder left outside recovers nothing. Recompute full Kelly and the largest long under a 2.5% single-default line on \$200mm with the bond at 98. *Check:* $f^\ast = 0.969/1 - 0.031/0.045 = 0.28$, with the ruin boundary at 100% of the fund; the stop gives $\$5\text{mm}/0.98 = \$5.1$mm, against \$8.6mm when recovery was 40.
3. **The same seller twice.** In §4D.3, a single counterparty sells twice; each time an uninformed seller sells with probability one-half, independently. Find the posterior on the bad state and the value, and compare with two sales from new sellers. *Check:* $P(\text{two sells} \mid 40) = 0.2 + 0.8 \times 0.25 = 0.4$ and $P(\text{two sells} \mid 100) = 0.2$, so the posterior is $2/3$ and the value 60, against 69% and 58.5 for two strangers. An informed seller would have sold twice anyway, so the repeat carries less fresh news.
4. **When the downside case is the bull case.** Hold the ratio of the refinance and exchange weights in §4D.10 at 45 : 35. What weight on the filing door makes the expected gain at 62 exactly zero? *Check:* the two good doors average $(45 \times 85 + 35 \times 70)/80 = 78.44$, so $78.44 - 43.44\,w = 62$ gives $w \approx 0.38$. A 38% filing probability is where the trade stops paying, which is the number the pitch has to defend.

### Deep-Dive Resource Graph

**Podcasts**

- *Odd Lots*, "How You Get and Actually Keep a Job at a Multi-Strat Hedge Fund" (Brian Yelvington), 7 Jul 2025: <https://omny.fm/shows/odd-lots/how-you-get-and-actually-keep-a-job-at-a-multi-strat-hedge-fund>. Scope, stops and how a credit PM is judged; paraphrased here from a machine transcript, so listen before quoting.
- *Odd Lots*, "How Hedge Funds Discover the Next Superstar Trader" (Joe Peta), 5 Sep 2024: <https://omny.fm/shows/odd-lots/how-hedge-funds-discover-the-next-superstar-trader>. Talent selection from the allocator's side of the table.
- *Odd Lots*, "How to Succeed at Multi-Strategy Hedge Funds" (Giuseppe Paleologo), 20 May 2024: <https://omny.fm/shows/odd-lots/how-to-succeed-at-multi-strategy-hedge-funds>. The factor x-ray and the risk manager's three jobs.
- *Signals and Threads*, Ep 20, "Solving Puzzles in Production" (Liora Friedberg), 7 Oct 2024: <https://signalsandthreads.com/solving-puzzles-in-production/>. What a production rotation is, from inside a market maker.
- *Signals and Threads*, Ep 29, "Wrestling the World into Rows" (Eric Mannes), 2 Sep 2026: <https://signalsandthreads.com/wrestling-the-world-into-rows/>. The time machine, the vendor's "whoops," and saving data with the time it arrived (§4D.8).
- J.P. Morgan *Making Sense*, Market Matters, "A new era of credit portfolio trading?", 9 May 2025: <https://www.jpmorgan.com/insights/podcast-hub/market-matters/new-era-credit-portfolio-trading>. A co-head of credit systematic trading inside the April 2025 stress.
- *Fixed + Floating*, E18, "Inside a Long/Short Credit Hedge Fund: Sizing, Shorts and LME Risk" (Ironshield), 4 Aug 2026: <https://podcasters.spotify.com/pod/show/fixedfloating/episodes/Inside-a-LongShort-Credit-Hedge-Fund-Sizing--Shorts-and-LME-Risk--Frits-Lieuw-Kie-Song-Ironshield-Capital-e3mncab>. The loss-budget sizing rule of §4D.5.

**Practitioner Writing**

- Optiver, "A day in the life of a quant trader intern": <https://www.optiver.com/join-us/stories/day-in-the-life-quant-trader-intern/>. Recruiting copy from equity options, useful by analogy for the market maker's rhythm, including the end-of-day review of trades not done.
- The DESK, "Citadel Securities new hires are reinforcing US credit market expansion," 4 Jan 2024: <https://www.fi-desk.com/citadel-securities-new-hires-are-reinforcing-us-credit-market-expansion/>. The market maker's build-out, row by row.
- Hedgeweek, Balyasny's investment-grade long/short team, 20 Aug 2026: <https://www.hedgeweek.com/balyasny-taps-former-blackrock-credit-chief/>; eFinancialCareers on home-grown PMs, 25 Feb 2026: <https://www.efinancialcareers.com/news/hedge-fund-junior-jobs>.
- Coalition Greenwich, "The Present and Future State of Corporate Bond Portfolio Trading": <https://www.greenwich.com/market-structure-technology/present-and-future-state-corporate-bond-portfolio-trading>. The 8,000 portfolio trades of §4D.7.
- METR, "Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity," 10 Jul 2025: <https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/>. Why the portfolio's core is built by hand.

**Academic Papers and Books**

- Glosten and Milgrom (1985), *Bid, Ask and Transaction Prices in a Specialist Market with Heterogeneously Informed Traders*, Journal of Financial Economics. The model behind §4D.3.
- Avellaneda and Stoikov (2008), *High-Frequency Trading in a Limit Order Book*, Quantitative Finance. The reservation price of §4D.4.
- Kelly (1956), *A New Interpretation of Information Rate*, Bell System Technical Journal. The log-growth criterion of §4D.5.
- Alpert and Raiffa (1982), *A Progress Report on the Training of Probability Assessors*, in Kahneman, Slovic and Tversky (eds.), *Judgment Under Uncertainty*. Why "90% intervals" miss so often.
- Derman, *My Life as a Quant* (Wiley, 2004): on candidates who "tried to use the Quantitative Strategies Group I ran as a conduit into trading" (text verified from a scanned copy; printed page to be confirmed). The quant seat as a route to the desk, a generation earlier.
- Moyer, *Distressed Debt Analysis* (shelf), pp. 62–64: the restricted-list calendar on Friday's wall.
- Zhou, *A Practical Guide to Quantitative Finance Interviews* (2008), and Mosteller, *Fifty Challenging Problems in Probability with Solutions* (1965). The puzzle canon, for practice; neither is about credit, which is what §4D.2–4D.7 add.

**Data & Code**

- FINRA, TRACE monthly volume files: <https://www.finra.org/finra-data/trace-monthly-volume-files>. The product split behind "which TRACE?"
- FINRA Rule 6730, TRACE reporting: <https://www.finra.org/rules-guidance/rulebooks/finra-rules/6730>. The fifteen-minute clock and as/of prints.
- `interview_drills.py`: [Listing 4-D.1 in Appendix F](#code-4D-1).

