# Chapter 2: The Revolutions in Credit Trading

*Tuesday, 3:41 p.m. Nineteen minutes to the index mark. The desk smells like burnt espresso and somebody else's DV01.*

The ticket on Theo Marsh's screen is the first one that is entirely his: **buy \$4mm, Halvorsen Freight 7.125% senior notes due 2030, B2,** sent all-to-all. (Halvorsen is fictional. The chime is not.) Responders get two minutes. In the old world Theo would have called three dealers, waited for two of them to call back, and spent the wait rereading the restricted payments covenant. In this world eleven responses arrive before he has found the covenant: four banks, two non-bank market makers, three asset managers, a hedge fund, and something whose name is a string of capital letters.

He lifts the best offer. The cover, the second-best response, is three-eighths of a point behind. Done in forty seconds.

"Back in my day," says Marguerite "Mags" Dunleavy, without looking up, "I priced these by phone and by grudge. You called Steve, Steve gave you a number that punished you for something you did in 1997, and the print showed up on TRACE seventy-five minutes later, if it showed up at all."

"Seventy-five minutes?"

"July 2002. The regulator gave us transparency the way a casino gives you a free drink: about five hundred bonds, seventy-five minutes late."

Ines Okafor rolls her chair over and studies the eleven rows the way she once studied a final table. "Eleven players. Nice pot, tight cover. Now tell me which one of them just got off a lender call."

Theo knows exactly what a lender call does to an offer, and he reaches for the indenture out of habit. "But what does the credit agreement say about electronic trading?"

"Nothing, Theo." Dr. Kasimir "Kaz" Lind keeps typing. "The bond doesn't know how it was traded. The dataset does."

<!-- CHECK: fictional-issuer bible (state/reviews/ed1/engagement.md line 109). Halvorsen is "Building Products 7.25% 2029" in Ch 1 and "Freight 7.125% 2030" here; reconcile names, ratings and coupons when the bible is written. -->

Theo finds the forty seconds oddly satisfying, the way a closing dinner is satisfying, and he sits back to enjoy it. Then, because three weeks on a systematic desk have taught him that nothing has happened until it shows up somewhere as a row, he opens the TRACE window to watch his own trade arrive in public.

It is not there.

He refreshes at 3:43. The Halvorsen line shows the morning's prints and an odd lot from lunchtime. He refreshes at 3:47, and again at 3:50, and nothing on the screen looks like four million bonds changing hands at 3:41.

"It isn't broken," says Kaz, who has not looked up but has apparently heard him refresh. "Rule 6730. The reporting side has 'as soon as practicable, but no later than within 15 minutes of the Time of Execution.'" Kaz pronounces the quotation marks, with the small relish of someone quoting a rulebook they have actually read. "Most people report in seconds. Some people use the whole fifteen."

"Fifteen minutes," says Mags. "Luxury. In July 2002 it was seventy-five minutes, and the tape covered about five hundred and twenty bonds, none of which I owned. TRACE was a newspaper that only reported the weather in towns I didn't live in."

At 3:56 the print lands. Theo reads it twice. The price is his, to the sixteenth. The times are his: executed 15:41, reported 15:56, the counterparty having taken every one of its fifteen legal minutes. The size is not his. Where Theo bought \$4mm, the tape says `1MM+`.

"That's not what I bought."

"That's what the public is allowed to know you bought," Kaz says. "Halvorsen is B2. A high-yield trade over a million prints as `1MM+`; in investment grade the cap is `5MM+`. The idea is to protect whoever has to go and find your bonds before the whole street knows the size."

"So my own trade is a lower bound."

"Your own trade is a lower bound to everyone except you, your counterparty and FINRA."

Theo scrolls up the Halvorsen line, because a restructuring banker never reads a page without reading the page before it. At 2:38 p.m., an hour and three minutes before his fill, there is another print: `1MM+`, a customer selling to a dealer, about half a point below where he has just paid *(illustrative)*. He did not see it when it happened. He was rereading the restricted payments covenant. He cannot really see it now, either. The tape tells him that somebody sold at least a million Halvorsen bonds to a dealer an hour before he bought, and it declines to say whether that somebody sold one million or forty.

"Who was that?"

"Could be anyone," Ines says. "A mutual fund rebalancing. A CLO trimming its bucket. Someone who just got off a lender call. Or a dealer's customer, and then the same dealer offered those bonds back out to you on the all-to-all, three-eighths through the cover." She shrugs, the way she used to shrug at a river card. "Which one it was changes what you paid."

Theo looks at the two `1MM+` rows, his own and the ghost's, a screen apart. He has three questions, and he asks them in the order a banker would. "What did I actually pay for that bond? Who knew it before I did? And could a machine have told me in advance?"

"Better than the question you came in with," Ines says. "Here's the answer in one line, and the rest of the afternoon is evidence. Every basis point off a ticket buys more tickets, and more tickets is more edge. The math is at the end; the evidence is in between." She counts the evidence on her fingers, the way she counts outs. "First you date the seven changes that built this screen, TRACE and six revolutions after it, and you put a sourced 2018-to-2026 number on each one. Then you read those caps as what they are, a censoring problem, and you back the tail index of the hidden block sizes out of one published average. You fit the S-curve of electronic adoption and give it an honest ceiling, instead of letting it run to a hundred percent like a pitch book. You price your RFQ as an order-statistics problem, and you find out that your eleven responders, all watching the same composite, were worth about two independent ones. You compute Barclays LCS and Man's transaction-cost decomposition with the units right, which is harder than it sounds and more embarrassing when you get it wrong. You treat the choice between an RFQ, an all-to-all, a portfolio trade and an ETF as one cost-minimization problem instead of four habits. And at the end you show why a cheaper ticket raises the breadth, and so the information ratio, that a quant strategy can harvest."

"And the ghost?"

"The ghost," says Ines, "is the last page."

That exchange is the whole chapter. A bond's *value* lives in its documents. Its *tradability* lives in its data exhaust: how many prints it gets per day, how many dealers answer an RFQ for it, how far the cover sits from the winner, whether it sits in an ETF redemption basket, and which of its trades the public tape refuses to show you. Theo's three questions are the trader's version of a historian's one. **The question this chapter answers: what changed in the plumbing of credit trading between 2002 and 2026, how big was each change, and why did those changes, rather than any new factor, make systematic credit possible?**

The answer arrives in three movements. The tape (§2.2) made the cost of a trade knowable after the fact, and then censored exactly the trades Theo cares about. The wire (§2.3 to §2.8) made cost knowable at the moment of the trade and turned every fill, and every miss, into a labeled data point. The payoff (§2.9) is Ines's one line made precise: a lower cost per ticket buys more breadth, so the same signal becomes a better strategy, and the optimal net alpha scales like $1/c$. Each section closes by saying what its revolution did to the two numbers a systematic desk lives on, the probability that an order fills and the expected cost when it does.

A housekeeping note for Kaz: every expectation in this chapter is under the physical measure $\mathbb{P}$. Market-structure statistics record what traders actually did. A count of RFQ responses has no pricing measure.

> **Math, Gently.** *What "under $\mathbb{P}$" means, and what "risk-neutral" would mean.* There are two ways to put a number on an uncertain event, and they answer different questions. The first is a weather forecast: of all the days that looked like today, on how many did it rain? That is $\mathbb{P}$, the physical or real-world measure. Its probabilities are frequencies, and with enough history you could count them. The second is the price of rain insurance: how much would you pay this morning so that you no longer care whether it rains? That price contains the forecast, but it also contains how much you hate getting wet, and on a Saturday when every wedding in town is outdoors it goes up even though the forecast has not changed. Probabilities backed out of market prices, as though nobody minded risk, form the risk-neutral measure $\mathbb{Q}$. A tiny number: suppose an issuer defaults 2% of the time over some horizon, counted from history, while its CDS trades at a spread that implies 4% *(illustrative)*. Both numbers are true. The first says how often you will actually lose; the second says what the market charges so that you will not mind, and the gap between them is a risk premium. Nothing in this chapter is a price of risk. A fill rate, a print delay, the number of dealers who answered an RFQ: these are counts of what happened, so they are forecasts, not insurance, and they live under $\mathbb{P}$. Chapter 5 has the full version, and $\mathbb{Q}$ becomes a main character in Chapter 6.

## 2.1 The Desk View: Execution Certainty and a Modelable Cost

Seen from a market maker's chair, a systematic credit book looks like this. A quant credit strategy is a function from data to target weights. Every day, or every hour, it says "own more of these 400 bonds and less of those 300." The optimizer behind those targets makes an assumption it never states: that the bonds can actually be traded, at a cost it can predict.

For most of its history, credit broke that assumption. Man Group's systematic team put the barrier plainly:

> **[SOURCE EXTRACTION]** *Man_Revolutions_in_Credit_Trading_2023 p.2:* "The greatest barriers to systematic approaches breaking through in credit have traditionally been execution and the ability to model transaction costs and liquidity within decades-old manual processes."
>
> **Annotation.** Notice what is *not* on the list: signals. By 2023, credit factors (value, momentum, quality, low risk) had more than a decade of published evidence behind them (Chapters 9–12). What was missing was a way to turn a target weight into a fill. The sentence recasts the history of quant credit as a history of plumbing, and that is this chapter's frame. Where the 2026 desk departs: in liquid IG, "manual processes" no longer bind, because most small tickets are electronic and many are auto-executed. They still bind for high-yield blocks, stressed names and anything near a liability-management transaction (Chapters 13–14). The barrier did not disappear. It moved down the credit curve, into Theo's old neighborhood.

On the next page of the same paper, Man named the two conditions a systematic strategy needs:

> **[SOURCE EXTRACTION]** *Man_Revolutions_in_Credit_Trading_2023 p.4:* "Two of the key challenges for such systematic techniques are having a high certainty of execution and having a relatively good sense of the likely transaction costs, as quantitative approaches depend on being able to model accurately which securities can be traded and at what cost."
>
> **Annotation.** These are the two inputs a portfolio optimizer cannot do without. One is a *feasible set*: which bonds can be traded. The other is a *cost function*: at what price. Write them as $\Pr(\text{fill}\mid x)$ and $\mathbb{E}[c \mid \text{fill}, x]$, where $x$ is a vector of ticket features such as size, rating, age, recent prints, and the number of dealers who answered the last RFQ. Every revolution in this chapter improves one or both. TRACE made $\mathbb{E}[c]$ estimable after the fact. RFQ platforms made it measurable at the moment of trade. All-to-all and automation raised $\Pr(\text{fill})$ for small tickets. Portfolio trading and ETFs created fills for baskets that no single-bond RFQ could absorb. The modern departure is that by 2026 both quantities are *forecast*, not just measured, and §2.5 shows them feeding a router rather than a spreadsheet.

Man's earlier paper explains why this matters to an optimizer. The subject of the sentence is the optimizer's solution:

> **[SOURCE EXTRACTION]** *Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.19:* "is no longer really optimal if that bond is not available for purchase. In addition, unfilled orders can lead to unintended and potentially unmodelled risk exposures."
>
> **Annotation.** An optimal portfolio you cannot buy is not optimal, and an unfilled order is not a zero. It is an *unintended position*. If you sold the bond you meant to swap out of but failed to buy its replacement, you are now short beta you never chose. A modern desk logs every unfilled order, and the realized fill rate becomes a training label (§2.5). The desk motto applies to execution as much as to alpha: *IDO or it didn't happen*. A backtest that assumes every target fills is reporting the alpha of a market that does not exist.

Theo reads the three extractions and objects, which is how he learns. "At PJT we never had a fill problem," he says. "Nobody ever failed to buy a bond. When a client needed to own the fulcrum, they owned the fulcrum by Friday. We always got filled. We just paid."

"How much?" Ines asks.

He opens his mouth, and closes it. He knows roughly where the claims traded the week the plan went effective. He knows what the client's average cost was, because it was in the fund's letter. What he does not know, and has never known, is how far each of those purchases sat from what the bonds were worth at the moment they were bought, because nobody at the table ever wrote that number down. There was a price, and there was a story about the price, and the story was usually told by the dealer who had sold it.

"'Paid' was never written down," Ines says, "so it could never be a variable. You can't optimize against a number nobody records. That's the whole revolution, really. Not that people started getting filled. That somebody started writing down what it cost."

That is the RSSG translation. At PJT the unit of analysis was a document and a process. Prices arrived by phone, late, from a dealer who was also your counterparty. That world had one kind of liquidity information, which was whatever Steve said. A systematic desk needs liquidity to be a *variable*: measured for every bond every day, forecastable, and comparable across 10,000 CUSIPs. Electronification is the process that turned liquidity from a relationship into a variable. The rest of this chapter dates that process, sizes it, and shows where it has still not reached.

The framing has a natural home, and it is worth being honest about its edges before seven sections of evidence make it feel universal. A feasible set and a cost function earn their keep when there are many tickets, each small relative to the market in its bond, each a repeat of a situation the desk has watched thousands of times. A book of 700 IG lines rebalanced monthly is that world. If the model's fill probability for a \$1mm BBB ticket is off by ten points on a given day, the error is one of hundreds and mostly averages away, and next month's labeled RFQs correct it. Mags runs the opposite kind of book. Her distressed fund holds five positions, each a few percent of an issue, and when she wants out of one of them the useful question is not "what is the probability this fills?" but "who is the one buyer, and what does he know?" The answer is a name she can say out loud: the other member of the ad hoc group, the sponsor buying back paper at a discount, the fund that wants the fulcrum. A logistic regression trained on 10,000 investment-grade RFQs has nothing to say about that person, and a cost estimate averaged across bonds that trade daily is not an estimate of anything that matters to a bond that trades twice a quarter. Most real books sit in between. A high-yield book of 150 names holds a hundred lines that live comfortably in the feasible-set world and a dozen that never will, and the first thing a seasoned trader checks before trusting a cost model on a line is how many comparable fills the model actually saw. When that count is in the dozens rather than the thousands, the "variable" has quietly turned back into a relationship.

So before any of the revolutions, the two numbers looked like this: $\Pr(\text{fill})$ was close to one for anyone willing to pay, and $\mathbb{E}[c]$ was not small so much as unknowable. The story of the next seven sections is the second number being written down.

## 2.2 Revolution 0: TRACE, or the Dataset Appears

Before you can trade a bond on a model, the model needs training data. For US corporates that data is TRACE, FINRA's Trade Reporting and Compliance Engine. It underlies everything that follows, so we call it Revolution 0. It did not change how bonds traded. It changed what anyone could *know* about how they traded.

> **[SOURCE EXTRACTION]** *Bohn_Stein_Active_Credit_Portfolio_Management p.91:* "In the past, credit markets have been hampered by lack of transparency in pricing, making it difficult to mark a portfolio to market let alone hedge or trade a particular exposure."
>
> **Annotation.** Bohn and Stein wrote when TRACE was a few years old, and their footnote 6 on the same page dates its origin: in September 1998 the SEC asked the NASD (now FINRA) to provide more transparency in corporate debt. The sentence lists three uses in rising order of difficulty: mark, hedge, trade. A systematic desk needs all three every day for every bond in its universe. Where the 2026 desk departs: transparency is no longer the scarce input for the liquid half of the market. The scarce input is *clean* transparency, meaning duplicate prints, processed voice trades and capped sizes have all been dealt with. That is the subject of the rest of this section.

### 2.2.1 The dissemination timeline

TRACE did not arrive all at once. FINRA phased it in by issue size and rating and cut the reporting clock in steps. The dates below come from the FINRA TRACE Fact Book (2025 edition) and FINRA's reporting-timeframes page. The one-minute saga comes from SEC and FINRA releases.

> **Trend Watch.** **The reporting clock, 2002–2026: a twenty-four-year countdown that stopped at fifteen minutes.**
>
> | Date | Change | Source |
> | :-- | :-- | :-- |
> | Sept 1998 | SEC asks NASD for corporate-debt transparency | `Bohn_Stein p.91`, fn. 6 |
> | July 1, 2002 | TRACE launches with 75-minute reporting. Phase I disseminates IG issues of \$1bn or more plus the "FIPS 50" HY names: about 520 securities by end-2002 | FINRA TRACE Fact Book 2025 |
> | Mar 3 and Apr 14, 2003 | Phase IIa (AAA/AA/A issues of \$100mm or more) and Phase IIb (120 BBB plus 50 HY names): about 4,650 bonds | Fact Book |
> | Oct 1, 2003 | Clock cut to 45 minutes | Fact Book |
> | Oct 1, 2004 | Phase IIIa; clock cut to 30 minutes | Fact Book |
> | Feb 7, 2005 | Phase IIIb: about 99% of public transactions and 95% of par value disseminated immediately | Fact Book |
> | July 1, 2005 | Clock cut to 15 minutes | Fact Book |
> | Jan 9, 2006 | Immediate dissemination of all public TRACE-eligible corporates | Fact Book |
> | June 30, 2014 | Rule 144A corporate trades disseminated | Fact Book |
> | May 15, 2023 | Portfolio-trade modifier required on corporate bond reports | Fact Book; FINRA RN 22-12 |
> | Jan 11, 2024 | FINRA files SR-FINRA-2024-004 to cut the 15-minute outer limit to one minute | SEC Rel. 34-101121 |
> | Sept 20, 2024 | SEC approves the one-minute rule | SEC Rel. 34-101121 |
> | Early 2025 | FINRA signals it will not set an effective date | Mayer Brown, *Free Writings*, Feb 10, 2025 (as reported); FINRA RN 25-17, fn. 9 |
> | Dec 4, 2025 | FINRA "is not moving forward"; the 15-minute standard stays | FINRA RN 25-17 |
> | June 8, 2026 | Optional aggregate allocation reporting begins | FINRA RN 25-17 |
> | Aug 31, 2026 | Expanded affiliate-principal indicator becomes available on a voluntary basis (mandatory Aug 2, 2027) | FINRA RN 26-16 |
>
> **What it means for the desk.** The headline clock (75, then 45, 30 and 15 minutes) understates how fast the market actually is. FINRA's own statistics, summarized in the SEC's 2024 approval order, show that in 2022, 82.9% of trades executed between 8:00 a.m. and 6:15 p.m. ET were already reported within one minute, and 90.6% within three. The rule would have accelerated "up to 16.4% of current annual trading volume, or up to 6.1 million trades and 20 trillion dollars in par value" (SEC Rel. 34-101121). So FINRA spent 2022 to 2025 trying to make the market report in one minute, found that 83% of it already did, and dropped the rule. It was the most TRACE-like thing TRACE has ever done: the information arrived, late, and changed nothing. For a quant, the interesting number is the remaining 17%. The trades that still report slowly are the manual ones, and manual trades are where blocks and distressed names live.

Mags's seventy-five minutes and Theo's fifteen are the outer limits. The interesting object is what happens inside them, and it needs one idea from statistics first.

> **Math, Gently.** *What a distribution is, and what a mixture is.* Picture the arrivals hall of an airport with two passport queues. One is the row of automated gates: scan, beep, through in seconds. The other is the human desk, where an officer reads every page and the wait runs to minutes. Stand at the exit with a stopwatch and write down, for every passenger, how long they took. The list of times, together with how often each one turned up, is a **distribution**: a description of which values a quantity takes and how likely each one is. Draw it as a histogram, with the waiting time along the bottom and the number of passengers in each small bin up the side, and this one has two humps, a tall narrow one near zero and a low wide one out at several minutes. Two humps are the signature of a **mixture**: two different distributions poured into one bag, with a weight $\pi$ on the first and $1-\pi$ on the second. If almost every gate passenger is out within a minute and almost no desk passenger is, then the share of *all* passengers out within a minute is approximately $\pi$ itself. A tiny number: if 83 of every 100 passengers use the gates and the desk never takes less than three minutes, then 83% are out within one minute, and a single count has told you $\pi \approx 0.83$. TRACE's print delays are the same hall. Straight-through electronic reports are the gates, manually booked voice trades are the desk, and FINRA's 82.9% reported within one minute is the stopwatch count that pins down the fast-queue share. Chapter 5 builds mixtures properly, starting with the survive-or-jump mixture inside every bond price (§5.1).

Written down, the print delay $\ell$ is a two-component mixture:

$$
\Pr(\ell \le u) = \pi\,F_{\text{fast}}(u) + (1-\pi)\,F_{\text{slow}}(u), \qquad 0 \le u \le 15 \text{ min}.
$$

Here $F_{\text{fast}}$ is the delay distribution of straight-through electronic reports (seconds), $F_{\text{slow}}$ is the delay distribution of manually booked voice trades (minutes), and $\pi$ is the weight on the electronic component. FINRA's 2022 statistic pins down one point of the mixture: $\Pr(\ell \le 1\text{ min}) = 0.829$. What matters for feature design is that $\pi$ is *not constant across bonds*. It is lowest exactly where the information is richest: large, stressed, voice-traded tickets. So a feature like "minutes since last print" means different things in different bonds. In an IG bond a stale print means nobody traded. In a CCC bond it may mean somebody traded big and the ticket is still being booked.

The airport also has a third queue, and it closes at night. A trade executed after 6:30 p.m. or before 8:00 a.m. ET is not disseminated when it happens; it waits for the system and appears the next morning (Farshid Abdi, with Marco Rossi and Botao Wu, "Overnight Corporate Bond Trading," The Microstructure Exchange, 15 Sept 2026). Rule 6730 treats the edges of the day the same way: trades before 8:00 a.m. ET, or within 15 minutes of the close, are reported after the next open. In the mixture above, the overnight regime is a third component that lives entirely outside the 0-to-15-minute window, a lump of probability parked at "tomorrow, after the open," and that is why the SEC's 82.9% is quoted only for trades between 8:00 a.m. and 6:15 p.m. A "minutes since last print" feature computed at 8:05 a.m. therefore blends three different situations: bonds nobody traded, bonds whose voice tickets are still being booked, and bonds that changed hands while New York slept and have not been shown yet. Abdi, Rossi and Wu's subject is the overnight market itself. For whoever builds the feature, the point is narrower and more boring: a timestamp has a regime, and the regime belongs in its own column.

### 2.2.2 The caps: censoring as a data problem

Two strings in the TRACE feed matter more to a credit quant than any others: `5MM+` and `1MM+`. FINRA disseminates the exact size of an IG trade only up to \$5mm and of an HY trade only up to \$1mm, and anything larger prints as the capped string. The cap is the bond market's version of "a source familiar with the matter": you know something big happened, but not how big.

> **Math, Gently.** *Censored, missing and truncated are three different things.* Picture a bathroom scale that only goes up to 300 pounds. A heavy friend steps on and the display says "300+". That reading is **censored**: it is not a blank, and it is not 300. It is a lower bound, and a lower bound is information. Now picture a different problem: the scale's battery died on Tuesday, so Tuesday has no reading at all. That observation is **missing**, and it tells you nothing about anyone's weight, only about the battery. And picture a third: a gym that only lets people under 300 pounds through the door, so the heavy friend never appears in the log in the first place. That sample is **truncated**: the big values are not hidden, they are absent, and nothing in the data warns you. TRACE's `5MM+` is the first kind. Dropping it treats a lower bound as a dead battery; replacing it with 5 treats a lower bound as a measurement. Both understate. (Ben Dor's two notes below use "censored" once and "truncates" once for the same fact; the first word is the right one.) To see how much they understate, it helps to know a trick for averages. The mean of any nonnegative quantity equals its survival probabilities stacked up: the chance it exceeds 0, plus the chance it exceeds 1, plus the chance it exceeds 2, and so on. A tiny number: if a trade size is equally likely to be 1, 2 or 3, the chance it exceeds 0 is 1, exceeds 1 is $2/3$, exceeds 2 is $1/3$, and exceeds 3 is zero. Stack them: $1 + 2/3 + 1/3 = 2$, which is exactly the mean, $(1+2+3)/3$. Now cap the sizes at 2. The stack loses its top layer, the $1/3$ above the cap, and the average capped size is $5/3$. The stack is the picture behind every number in this section. The full version is the derivation at the end of it.

> **[SOURCE EXTRACTION]** *Ben_Dor_Quantitative_Credit_Portfolio_Management p.162 (note 3):* "disseminates trade-by-trade corporate bond execution information within 15 minutes to all market participants. At this time, TRACE data are censored at \$5 million for investment grade and \$1 million for high-yield securities."
>
> **Annotation.** The Barclays authors use the right word: *censored*. A censored observation is not missing data. It tells you the true value is at least the cap, which is information, so you should neither drop it nor treat it as equal to the cap. The caps have not moved since this was written. FINRA still disseminates `5MM+` for IG and `1MM+` for HY, and RN 25-17 applies the same caps to the new allocation reports. The *ticket* has moved: average trade size fell from about \$560k to about \$360k over the four years to 2024 (IFR, citing MarketAxess data), so a larger share of trades now prints uncapped. The capped minority is the part of the market an RSSG veteran knows best.

Stacked survival probabilities make the bias easy to see. The capped size $\min(X, c)$ keeps every layer of the stack below the cap and loses every layer above it, so volume summed from capped prints biases turnover *down*, by the area under the size distribution's tail beyond the cap. Ben Dor and coauthors flag exactly this:

> **[SOURCE EXTRACTION]** *Ben_Dor_Quantitative_Credit_Portfolio_Management p.364 (note 8):* "TRACE truncates the sizes of large transactions at \$1 million and \$5 million for high-yield and investment-grade bonds, respectively, which may cause our estimates of turnover to be downward biased."
>
> **Annotation.** The same note then gives the fix. Capped trades are assigned larger sizes, chosen so that the sum of individual trades matches TRACE's aggregate volume figures, which "yields higher transaction limits of \$4 million and \$12.5 million for high-yield and investment-grade bonds, respectively." That is a moment-matching estimator, and below we use it to extract a structural fact about block sizes. Where the modern desk departs: academic and enhanced TRACE files with uncapped sizes are released with a lag (Appendix B), so a backtest can use true sizes, but a live model sees only the capped feed. Train on what you will see at decision time. Otherwise your turnover feature is look-ahead bias in a lab coat.

The imputation can be made to tell us something, and it is worth watching Kaz find out what. Kaz reads the note, gets as far as "\$4 million and \$12.5 million," and stops. "Those are averages of the trades above the cap. If I knew the shape of the tail, I could get the average from the cap. So if I know the average, I get the shape." Getting there needs a vocabulary for shapes.

> **Math, Gently.** *How distributions differ on a desk.* A distribution is a shape, and each shape is the natural model for a different object, so a desk meets several of them before lunch. The **normal** is what many small, independent nudges add up to: symmetric, thin-tailed, the wobble of dealers' quotes around a composite mid, which is where §2.3.2's quote noise begins. The **exponential** describes a positive distance or waiting time with no memory: given that a quote is already some way from mid, the extra distance has the same distribution as the original one, which is the property §2.3.2 uses to price the cover. The **Poisson** counts events that arrive at a steady average rate, such as the number of prints a bond gets in a day; a bond that averages three prints shows zero on about one day in twenty. The **lognormal** describes quantities that grow by multiplying rather than adding, and it fits the body of the ticket-size distribution: lots of \$200k and \$500k trades, fewer \$2mm ones, never a negative one. And the **Pareto** describes the tail where the giants live, block sizes beyond the cap, where the chance of a block at least twice as big falls by the same fraction however big you start. Its single parameter, the tail index $\alpha$, sets how fat that tail is. When $\alpha$ is below 2 the distribution has *infinite variance*, which has a concrete meaning on a desk: however many trades you average, one block keeps showing up large enough to dominate the average, and the sample mean never settles down the way it would for a normal. A tiny number: with $\alpha = 5/3$ and the IG cap at \$5mm, the average hidden block is $5 \times (5/3)/(2/3) = 12.5$, which is precisely Ben Dor's imputed IG figure. The same arithmetic with $\alpha = 4/3$ and the HY cap at \$1mm gives 4, Ben Dor's HY figure. Chapter 5 gives each shape its full treatment, and §5.7 fits fat tails properly.

So Kaz runs the arithmetic backwards. Suppose block sizes above the cap follow a Pareto tail, the standard model for heavy-tailed sizes. Then the average capped trade is a fixed multiple of the cap, $\alpha/(\alpha-1)$, and a published average pins down $\alpha$. For investment grade, an average of 12.5 against a cap of 5 means the tail index is 5/3, about 1.67. For high yield, 4 against a cap of 1 means 4/3, about 1.33. Two numbers in a footnote, written to fix a turnover estimate, turn out to contain a structural fact about how large trades are distributed.

Read that slowly, because it is the book's first quant "aha" for an RSSG reader. Both tail indices are below 2, so the implied block-size distribution has *infinite variance*. (Kaz, who was going to assume Gaussian, now regrets it.) The HY tail is also fatter. Relative to its cap, the average hidden HY block is four times the cap, against two and a half times in IG, so `1MM+` hides proportionally more of HY than `5MM+` hides of IG. The trades the tape conceals most completely are large HY and stressed trades, the ones where knowing who sold, and how much, is worth the most. The RSSG skill set is most valuable exactly where the data exhaust is thinnest.

#### The Full Derivation: the tail index from one moment

Every TRACE-based turnover model rests on the following identity. Let $X$ be the true size of a trade, with CDF $G$, and let the cap be $c$. TRACE shows $\tilde X = \min(X, c)$. For any nonnegative random variable, $\mathbb{E}[X] = \int_0^\infty \Pr(X > x)\,dx$, so

$$
\mathbb{E}[\tilde X] = \int_0^{c} \big(1 - G(x)\big)\,dx, \qquad \mathbb{E}[X] - \mathbb{E}[\tilde X] = \int_c^{\infty} \big(1 - G(x)\big)\,dx \;\ge\; 0 .
$$

Volume summed from capped prints therefore biases turnover *down*, by the area under the size distribution's tail beyond the cap.

Next, the imputation. Suppose block sizes above the cap follow a Pareto tail, the standard model for heavy-tailed sizes:

$$
\Pr(X > x \mid X > c) = \left(\frac{x}{c}\right)^{-\alpha}, \qquad x \ge c,\quad \alpha > 1 .
$$

Then the mean size of a capped trade is

$$
\mathbb{E}[X \mid X > c] = c + \int_c^\infty \left(\frac{x}{c}\right)^{-\alpha} dx = c + \frac{c}{\alpha - 1} = \frac{c\,\alpha}{\alpha - 1}.
$$

Ben Dor's imputed limit $m$ is this conditional mean. Set $m = c\alpha/(\alpha-1)$ and solve for the tail index:

$$
\hat\alpha = \frac{m}{m - c}.
$$

For IG, $c = 5$ and $m = 12.5$, so $\hat\alpha = 12.5/7.5 = 5/3 \approx 1.67$. For HY, $c = 1$ and $m = 4$, so $\hat\alpha = 4/3 \approx 1.33$.

(A caveat for the exercises: a Pareto tail fitted from one moment is a sketch, not an estimate. Chapter 22 fits the tail directly from the uncapped academic file.)

> **Ways This Blows Up.** *The riskless-principal echo.* Kaz once asked whether a "riskless principal" trade involved a principal with no risk, "like a tenured professor." Close. It is a dealer who buys from one customer and sells to another at nearly the same moment. The dealer carries no inventory risk, and one economic trade can generate two TRACE reports. Affiliated desks reporting to each other add more echoes. MarketAxess reported that duplicate trade reports inflated US high-grade TRACE volume by up to 8% in June 2026. FINRA's expanded affiliate-principal indicator exists to suppress them (voluntary from Aug 31, 2026, mandatory Aug 2, 2027; RN 26-16). A volume-based liquidity score fitted on 2020–2026 data therefore has a structural break built in. Tag the regime and deduplicate before you fit anything.

> **Shop Life: the TRACE loader.** *A fictional composite; the dates and rule changes are real.* A systematic asset manager, the kind with four hundred bonds in a book and nine people in a room called "Data." Wednesday, 7 October 2026, 8:20 a.m. The portfolio manager's morning dashboard has a chart called *IG market activity*, and on Tuesday's bar the chart has dipped. The PM has written one line in the team channel: "Why is Tuesday's IG volume 9% below Monday's? Tuesday was much busier. Three new deals and the index rebalance." The line is addressed to nobody, which on a data team means it is addressed to the most junior person, who this year is Femi, eleven months out of a statistics master's and still young enough to find the question interesting.
>
> Femi starts where everyone starts, by assuming the market is right and the code is wrong. He pulls Tuesday's raw TRACE file and counts rows: more prints than Monday, not fewer. He sums par in the raw file by hand, in a notebook, the way his manager says to do it once before trusting any pipeline, and Tuesday comes out *above* Monday. So the loss is inside the loader. He diffs the loader's commits and finds a tidy pull request merged on Monday evening by a colleague who was cleaning up warnings. The old code read the size column as text and had a special case for `5MM+` and `1MM+`. The new code casts the column to a number with errors coerced, which turns `5MM+` into a blank, and four steps later a `dropna()` removes the blanks. Nobody wrote "drop the biggest trades." The code simply stopped knowing what the biggest trades were. Tuesday, being the busier day, had more blocks above the cap, so Tuesday lost more volume. The capped prints were not treated as lower bounds or even floored at the cap. They were treated as dead batteries.
>
> That explains most of the gap, and Femi could stop. He does not, because the dashboard's other chart, month over month, has been bothering him for a week. September's high-grade TRACE volume on the dashboard looks soft against June's. He goes to the platforms' monthly reports to cross-check and finds Tradeweb's September 2026 report, published that Tuesday, with a footnote: the affiliate-principal change "lowered reported U.S. High Grade TRACE volumes," and "[we] have not restated prior periods and therefore these amounts may not be comparable." He reads it twice. FINRA's expanded affiliate-principal indicator became available on a voluntary basis on 31 August 2026; when a dealer flags the inter-affiliate leg of a trade, TRACE suppresses it and disseminates only the trade with the outside customer. So September is cleaner than June, not quieter. And June was dirtier than it looked: MarketAxess had reported duplicate trade reports inflating US high-grade volume by up to 8% that month. The dashboard was comparing a month with echoes to a month with fewer echoes and calling the difference a market. Nobody can say exactly how big the break is, because the footnote does not size it, and the indicator stays voluntary until August 2027, so each dealer flips its own switch on its own day.
>
> By now it is 11:40, and Femi has the slightly dangerous feeling of someone on a roll. He opens the feature store to see what else touches TRACE and finds the portfolio-trading share feature, which the cost model uses. Before 15 May 2023 it is exactly zero, every day, for every bond. FINRA only began requiring the portfolio-trade modifier on 15 May 2023, so before that date the tape cannot say which trades were in portfolio trades. A zero claims to know there were none, in 2021, the year dealers were bidding baskets most aggressively. The honest value before the modifier exists is "unknown," a NaN, and a model that sees NaN can be told to ignore the feature for those years instead of learning that 2021 had no portfolio trading.
>
> The fix takes forty minutes and is almost insultingly small. The loader gets back its special case, now written as a flag: `size_capped = True` and `size = cap`, so a downstream model can choose to floor, impute or censor-model the block as it likes. The table gets one new column, `trace_regime`, with three values: before the portfolio-trade modifier, after it, and after the affiliate indicator. The schema document gets one paragraph that begins "TRACE sizes are censored, not missing." Femi reruns Tuesday. It is now 4% above Monday *(illustrative)*, which is what the PM had assumed all along. No model was retrained. No signal changed. At the Friday meeting the PM says "good catch" in the voice people use for plumbing, and moves on to the agenda item about the new office chairs. It is, by any measure that matters to a systematic fund, the most valuable thing anyone on the floor did that week.

Last, a period piece from the shelf, included because it explains why some of Mags's habits survive:

> **[SOURCE EXTRACTION]** *Moyer_Distressed_Debt_Analysis p.416 (note 62):* "However, most of the securities required to be posted do not constitute distressed securities."
>
> **Annotation.** Moyer was writing in TRACE's phased-in early years, when dissemination mostly covered larger issues, and the same note expands the acronym as "Trade Reporting and Comparison Entry Source," an artifact of its vintage. For the distressed investor of that era, the new tape was something that happened to other people. Today every public TRACE-eligible corporate is disseminated, stressed ones included. But the caps and the slow manual component from §2.2.1 still make distressed trading the least transparent corner of a transparent market. That is why Mags still prices some things by grudge, and why she is still, irritatingly, right about some of them.

So Revolution 0 left $\Pr(\text{fill})$ exactly where it was and made $\mathbb{E}[c]$ estimable after the fact, for every trade except the large ones, which it recorded only as lower bounds.

### Deep-Dive Resource Graph

**Podcasts.** *Bloomberg Odd Lots* has covered bond-market structure several times. We list no specific episodes because we could not verify titles and dates for this edition.

**Practitioner Writing.** FINRA, *TRACE Fact Book 2025*: https://www.finra.org/sites/default/files/2026-02/TRACE_FactBook_2025.pdf. FINRA, *TRACE Reporting Timeframes*: https://www.finra.org/filing-reporting/trade-reporting-and-compliance-engine-trace/trace-reporting-timeframes. Mayer Brown, *Free Writings* (Feb 10, 2025), on the one-minute effective date: https://www.freewritings.law/2025/02/finra-will-not-set-an-effective-date-for-amendments-to-trace-rules-establishing-one-minute-reporting-requirement-finra-to-prepare-new-filing-for-public-comment/

**Academic Papers.** Bessembinder, Maxwell & Venkataraman (2006), *Market transparency, liquidity externalities, and institutional trading costs in corporate bonds* (JFE). Edwards, Harris & Piwowar (2007), *Corporate bond market transaction costs and transparency* (JF). Goldstein, Hotchkiss & Sirri (2007), *Transparency and liquidity: a controlled experiment on corporate bonds* (RFS). Harris (2015), *Transaction costs, trade throughs, and riskless principal trading in corporate bond markets*.

**Data & Code.** SEC Release 34-101121 (one-minute approval): https://www.sec.gov/files/rules/sro/finra/2024/34-101121.pdf. FINRA Regulatory Notice 22-12 (portfolio-trade modifier): https://www.finra.org/rules-guidance/notices/22-12. FINRA Regulatory Notice 25-17: https://www.finra.org/rules-guidance/notices/25-17. FINRA Regulatory Notice 26-16 (affiliate indicator): https://www.finra.org/rules-guidance/notices/26-16.

## 2.3 Revolution 1: From Phone to RFQ

Mags has a war story for every protocol, and this one begins with a run. "A run," she tells Theo, who has received several hundred and never been told what one is, "is a dealer's list of bonds and levels. It goes out at 8 a.m., is stale by 8:05, and binds nobody. It's a menu where every price says 'market.'"

Man's 2022 paper describes the market the electronic RFQ was built to replace:

> **[SOURCE EXTRACTION]** *Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.19:* "the bond market is structured around a Request for Quotation (RFQ) process that has hardly changed for decades. Corporate bond bid/ask prices are indicated by dealer runs that are not firm and actionable"
>
> **Annotation.** Two phrases carry the weight. "Hardly changed for decades" means the protocol still runs request, quote, accept. Electronification did not abolish the RFQ. It put it on a wire, sent it to many dealers at once and timestamped every answer. "Not firm and actionable" separates an *indication* from a *price*. A run is an indication. A TRACE print is a fact about a trade somebody else already did. Neither is a firm price for the trade you want now. An electronic RFQ is: $n$ dealers answer the same question at the same moment, each answer is binding for the response window, and the client can execute against the best one or walk away. Each RFQ therefore leaves a labeled record behind it: how many dealers were invited, how many answered, every quote, the winner, the cover, the timestamps, and whether it traded. Where the 2026 desk departs: the RFQ is now being split into variants (request-for-market, session-based auctions, streaming, one-click). Buy-side panelists at FILS Europe in 2026 predicted that the RFQ "in its current form" would become obsolete (The DESK, Oct 2026). If that happens, the request-quote-accept structure will have lasted most of a century. It would be the most durable thing in this chapter.

> **View From Another Seat.** *The dealer desk (a generic bank seat; no bank is named).* From the dealer's chair the run and the RFQ are two halves of one business, and they feel nothing alike. The run is advertising. A flow trader sends it at 8 a.m. to a few hundred clients so that, when one of them has a bond to move, the bank's name is the first one they think of. It costs nothing, binds nobody, and the trader knows most of its levels will be stale by the first coffee. The RFQ is the moment a client asks the bank to stand behind its advertising, in size, for two minutes, against rivals it cannot see. That is the asymmetry the dealer lives with all day. The client sees eleven answers. Each dealer sees its own answer and, afterward, whether it won. The client learns the market eleven numbers at a time; the dealer learns it one bit at a time. The published evidence from the run side is humbling for anyone who thinks the tightest quote takes the trade: in Hendershott, Li, Livdan, Schürhoff and Venkataraman (2026), the best-quoting dealer wins only 15% of trades, and 16% to 40% of trades print worse than the best available quote (§2.4). Relationships, timing and the client's own constraints all get a vote. A dealer desk reads those numbers two ways at once. They are a reason to keep sending runs, because a dealer's quote improves client execution by 6 to 7 bp just by being present, and presence is how a bank stays on the client's list. They are also a reason not to spend capital being the tightest name on every line. And when Theo lifts the best of eleven offers, the dealer that wins learns one thing: it was the most aggressive of a crowd it never saw. That is exactly the news a dealer least wants, and §2.3.2 turns it into the winner's curse.

Here is why a pre-RFQ quant could not build the obvious cost model directly from TRACE:

> **[SOURCE EXTRACTION]** *Ben_Dor_Quantitative_Credit_Portfolio_Management p.120:* "Although it is possible to capture transaction spread data via TRACE, for most bonds the time between a broker-dealer buy and sell transaction for a given CUSIP can be very long, so it is difficult to calculate an accurate bid-ask spread using TRACE."
>
> **Annotation.** A bid-ask spread is a statement about two prices *at the same moment*. TRACE gives you two prices at *different* moments, a dealer buy on Tuesday and a dealer sell on Friday, with three days of spread moves mixed into the difference. Measured that way, a bond's "spread" is mostly volatility. This is why Barclays built its Liquidity Cost Score from trader quotes (§2.9.1), and why RFQ data is the better cost instrument: an RFQ records competing quotes for the same bond within the same two-minute window. Where the 2026 desk departs: composites such as MarketAxess CP+ and Tradeweb Ai-Price (which covers about 30,000 US corporates, per Tradeweb's FY2025 10-K) now provide a continuous estimated mid. The remaining problem is not getting a mid. It is checking whether the composite deserves your trust (§2.3.2).

The first large academic look at the new protocol is Hendershott and Madhavan (2015), *Click or Call? Auction versus Search in the Over-the-Counter Market* (*Journal of Finance*). They study every US corporate bond transaction from January 2010 to April 2011, about 4.6 million trades. Electronic auctions account for 467,614 trades in 5,528 bonds and voice for 4,153,611 trades in 11,122 bonds, so about one trade in ten was electronic. Auctions lasted 5 to 20 minutes, and they turned out to be a workable source of liquidity even in bonds that rarely trade. The paper also carries a warning this book repeats often: traders choose the venue. Easy tickets go electronic and hard tickets go to the phone, so a raw comparison of "electronic cost" with "voice cost" flatters the wire. Every venue-choice model in Chapter 19 inherits that selection.

> **Trend Watch.** **Electronic share of US corporate bond trading, 2015–2026: IG crossed the halfway line, HY parked at a third.**
>
> | Period | US IG e-share | US HY e-share | Source and definition |
> | :-- | :-- | :-- | :-- |
> | 2015 | ≈20% | ≈6% | Coalition Greenwich (McPartland, June 10, 2025); notional *(approx.; as reported, not independently verified)* |
> | 2021 | ≈34% | ≈25% | Greenwich, *U.S. corporate bond trading in 2024 by the numbers* (Jan 2025); chart reading, CHECK |
> | 2022 | ≈41% | ≈31% | Same; chart reading, CHECK |
> | 2023 | 45% | 33% | Same |
> | Feb 2024 | 45% | 29% | Greenwich via The DESK (Mar 19, 2024) |
> | 2024 (full year) | 48% | 33% | Greenwich (Jan 2025); overall 44%, ADNV \$46.2bn, 125,723 trades/day, average ticket \$381k |
> | Feb 2025 | n/a | 30% | Greenwich Data Spotlight (Mar 17, 2025) |
> | June 2025 | 52% | n/a | Greenwich Data Spotlight (July 14, 2025) |
> | 2023 / 2024 / 2025 | ≈45% / 50% / 60% | ≈30% each year | MarketAxess 10-K estimates, as reported (company definition, above Greenwich's; not independently verified) |
>
> Protocol mix inside US e-volume: disclosed RFQ was 48.3% (2021), 42.3% (2022), 47.2% (2023) and 44.0% (2024) (Greenwich, Jan 2025). One systematic shop's own order flow shows the same shift more sharply. Man moved from "roughly 30% of our order flow in high yield and 60% in investment grade going through electronic venues, to over 90%" as of May 1, 2023 (`Man_Revolutions_in_Credit_Trading_2023 p.3`).
>
> **What it means for the desk.** IG crossed the halfway line on at least one definition in 2025, while HY has been stuck near a third for four years. The gap between them is the structural fact. Everything else in the table is an exercise in reading definitions, and the desk works through it below.

Theo's first instinct with a table like this is a banker's: find the biggest number and put it on a slide. Ines takes the mouse away from him. "Read it like a hand history, not a headline. Start with the gap." She points at the two columns. "IG went over half on somebody's definition in 2025. HY has sat around a third since 2022, four years. That isn't a slow adopter. That's a ceiling, and you want to know why before you draw a line through it."

"Fine. IG is 48%."

"Or about 60%. Or around half. Which?" She scrolls to the source column. Greenwich says 48% for full-year 2024. MarketAxess's own 10-K estimates, on the company's definition, say about 50% for the same year and about 60% for 2025. Barclays, as reported in September 2025, puts it around or above half on broader definitions. "Same market, same year. The difference is the word 'electronic.'" She counts its meanings on her fingers. *Fully electronic*: negotiated and executed on a venue. *Processed*: negotiated by voice or chat, booked electronically afterward. *Auto-executed*: no human touched it at all. "And then the denominator: notional, ticket count or customer volume. A ticket-count share runs higher than a notional share, because the wire got the small tickets first. Kaz won't touch a series until somebody has written on it which 'electronic' it means and what it divides by. This week, that somebody is you."

Theo looks at the HY column again. 29% in February 2024, 30% in February 2025, against 33% for full-year 2024. "So HY went backwards?"

"HY went *harder*. When trading gets difficult the hard tickets go back to the phone, so the e-share falls. A monthly HY number is partly a difficulty indicator. That makes it useful for a router, and it makes it a terrible input to an adoption curve, which is why Kaz fits those on annual points only." She hands the mouse back. "Now you can put a number on a slide."

### 2.3.1 The adoption S-curve, with an honest ceiling

Asked to "project HY electronic share to 2030," ROBO fit a constant growth rate to the move from 6% (2015) to 33% (2024), compounded it six more years and returned
$$
0.33 \times \left(\frac{0.33}{0.06}\right)^{6/9} \approx 1.03,
$$
so 103% of HY would trade electronically by 2030. Nobody told it that $K \le 1$. ROBO has discovered a market in which more bonds trade electronically than trade.

The honest model is a logistic with a ceiling, and the intuition behind it is older than any bond market.

> **Math, Gently.** *Odds and the S-curve.* Picture a rumor loose in a school of 1,000 pupils. On the first morning ten of them know it. Each one who knows passes it on at a steady rate, but only to pupils who have not heard it yet. So at the start the rumor spreads slowly, because there are few tellers, and at the end it spreads slowly, because there is almost nobody left to tell. It spreads fastest when half the school knows, and a plot of "share who know" against time is an S. The top of the S is the size of the school, not infinity. There is a ceiling, $K$, and in a bond market the ceiling is set by the tickets that will never leave the phone. (ROBO's 103% is what happens when a model forgets the school has walls.) The trick that tames the S is to stop watching the share and watch the **odds**: those who know divided by those still to be told, $e/(K-e)$. On a logistic S-curve the odds grow by the same *percentage* every year, so their logarithm, the **log-odds**, rises in a straight line, and a straight line can be drawn with a ruler and two points. A tiny number: US IG electronic share was about 20% in 2015 and 48% in 2025 (Greenwich). With $K = 1$ the odds went from $0.20/0.80 = 0.25$ to $0.48/0.52 \approx 0.92$, multiplying by about 3.7 in ten years. That is a growth rate of $r \approx 0.131$ a year, and odds that grow at rate $r$ double every $\ln 2/r \approx 0.693/0.131 \approx 5.3$ years. The full version is the derivation below.

The same ruler through the HY points gives a steeper line, with odds doubling every 3.5 years, because HY started from 6%. Projected to 2030 with a ceiling of 100%, IG reaches 64% and HY 56%. These are *illustrative extrapolations*, not forecasts, and the projection is the least interesting thing the arithmetic says.

Two things sit inside that arithmetic, and both are better than the numbers.

*The ceiling is not identified from two points.* Each choice of $K$ gives a different line through the same two observations. Redo the fit with $K = 0.80$, roughly the ceiling Barclays has suggested for electronic execution (via The DESK, Jan 2025), and the IG slope rises from 0.131 to 0.150 a year while the 2030 projection falls from 64% to 61%; HY moves to a slope of 0.211 and a 2030 value of 53%. A lower ceiling means a *faster* implied adoption rate, because the same observed share is closer to the ceiling than it looked. You need curvature to estimate $K$, meaning at least three points with the curve visibly bending. The only bend in the US IG series is 2024 to 2025 (48% to 48%), a single year that could just as well be noise. In practice, $K$ comes from outside evidence, and here the outside evidence is blunt: in December 2023 about 90% of block trades (IG of \$5mm or more, HY of \$1mm or more) were still done by phone or chat (Greenwich, Dec 7, 2023). Section 2.8 returns to those blocks.

*Fit the right object.* If you fit all three parameters by least squares on the levels, an optimizer given the IG points $\{0.20, 0.48, 0.48\}$ is free to set $K$ at about 0.48, make $r$ as steep as its bounds allow and report that US IG electronification was over by about 2017. The fit is perfect, and meaningless. Kaz tried this. Kaz now treats a fitted ceiling equal to the latest observation as a diagnostic, not a result. The code in §2.9 prints a warning when it happens.

So when does the curve earn its place? It is a good way to *frame* a projection. It lets a desk say "if the ceiling is 80%, here is how fast the remaining gap closes," and it shows a PM that "electronification is finished" and "electronification has decades to run" are both claims about $K$, not about $r$. It is a poor way to *estimate* $K$, for the reasons Kaz learned the hard way. A practitioner gets the ceiling from the anatomy of the market instead. About 90% of blocks still went by phone or chat in December 2023, and blocks carry a large share of notional, which puts a lid well below 100% on any notional-weighted series. HY has sat near a third for four years, which is either a ceiling or a very long plateau, and no curve fitted to those points can say which. Before trusting a projection, an experienced hand checks three things: whether the series' definition changed partway (the box below), whether a stress year sits in the sample (HY e-share falls when trading gets hard), and whether the fitted ceiling equals the latest observation. And the curve breaks outright when the mechanism changes. Portfolio trading (§2.6) put blocks on the wire as baskets, which moves the ceiling itself, and a logistic with a fixed $K$ has no way of noticing.

#### The Full Derivation: fitting a ceiling from two points

Let $e_t \in (0, K)$ be the electronic share of notional in a segment at time $t$ (years):

$$
e_t = \frac{K}{1 + \exp\{-r\,(t - t_0)\}}, \qquad 0 < K \le 1,\; r > 0 .
$$

Here $K$ is the ceiling, the share that will eventually trade electronically (blocks that never leave the phone keep it below 1), $r$ is the adoption rate per year, and $t_0$ is the midpoint, where $e_{t_0} = K/2$. (This $r$ is an adoption rate, not the interest rate; the context never mixes them, but we flag it once.) Rearranging,

$$
\frac{e_t}{K - e_t} = \exp\{r\,(t - t_0)\} \quad\Longrightarrow\quad z_t(K) \equiv \ln\frac{e_t}{K - e_t} = r\,(t - t_0).
$$

For a fixed $K$, the generalized logit $z_t(K)$ is *linear in time*. Two dated observations therefore give a closed-form slope and midpoint:

$$
\hat r(K) = \frac{z_{t_2}(K) - z_{t_1}(K)}{t_2 - t_1}, \qquad \hat t_0(K) = t_1 - \frac{z_{t_1}(K)}{\hat r(K)} .
$$

Since $e_t/(K-e_t)$ is the odds of "electronic" relative to the ceiling, and those odds grow like $e^{rt}$, they double every $\ln 2/\hat r$ years.

Now plug in Greenwich's 2015 and 2025 numbers with $K = 1$. For IG, $z = \ln(0.20/0.80) = -1.3863$ in 2015 and $\ln(0.48/0.52) = -0.0800$ in 2025, so $\hat r_{IG} = 1.3063/10 = 0.131$ per year and the odds double every $0.6931/0.131 = 5.3$ years. For HY, $z = \ln(0.06/0.94) = -2.7515$ and $\ln(0.32/0.68) = -0.7538$, so $\hat r_{HY} = 0.200$ per year, with odds doubling every 3.5 years. Projected to 2030 with $K=1$, IG reaches $1/(1+e^{-0.573}) = 64\%$ and HY reaches $1/(1+e^{-0.245}) = 56\%$. These are *illustrative extrapolations*, not forecasts.

The ceiling-sensitivity fit works the same way. With $K = 0.80$, the IG slope rises to $\hat r_{IG}(0.8) = [\ln(0.48/0.32) - \ln(0.20/0.60)]/10 = 0.150$, and the 2030 projection falls to $0.8/(1 + e^{-1.158}) = 61\%$. HY becomes $\hat r = 0.211$ with a 2030 value of 53%.

> **Ways This Blows Up.** *Splicing denominators.* Greenwich reports notional share of total market volume. MarketAxess reports its own estimate of the electronic share. Bondwave reports portfolio trading as a share of *customer* volume. A platform reports its share of TRACE, which includes interdealer prints. Splice two of these into one series and your fitted $r$ partly measures the change of definition. The rule: one series per source, and the source and denominator go in the dataframe schema (§2.9), not in a footnote.

### 2.3.2 The RFQ as an auction: why eleven anchored dealers are worth about two

Back to the cold open. Theo got eleven responses, and the instinct is that eleven is great. Order statistics say how great, and then say why the instinct is too generous.

> **Math, Gently.** *Order statistics, and the effective number of dealers.* An **order statistic** is what you get when you sort a handful of random draws and keep one of them by its rank: the smallest, the second smallest, the largest. The best offer in an RFQ is the smallest of the dealers' distances from fair value, and the cover is the second smallest. Picture eleven friends each guessing the fair price of a used car, and you get to buy at the lowest guess. More friends help, because with more draws one of them is likelier to land low; with independent guesses of the kind used below, doubling the friends roughly halves how far the best guess sits from the true price. But that only works if the friends guess independently. If all eleven have just read the same online listing, their guesses cluster around the listing, the listing's own error is shared by everyone, and no number of extra friends removes it. Eleven friends reading one listing are worth only a few independent ones, and the arithmetic that says how few gives the **effective number** of guessers. One more property makes the cover easy to think about. If the distances are *exponential*, the memoryless shape from the distribution box in §2.2.2, then once you know the best quote, each of the others sits above it by a fresh exponential amount with the same mean as before. So the cover is to the winner what the winner is to mid: the gap from winner to cover is, on average, about as big as the winner's own distance from fair. A tiny number: eleven responders whose quotes share an anchor worth 45% of their average distance from fair ($\phi = 0.45$) have an effective count of $11/(1 + 10 \times 0.45) = 11/5.5 = 2$. The full version follows.

Run Theo's ticket through that machinery and the cold open looks different. If the eleven quotes were independent exponentials, the best offer would sit about an eleventh of the typical quote distance from fair, and the cover gap would be about as large as the winner's own distance. Theo's three-eighths cover then suggests his winner was also roughly three-eighths from fair *(illustrative)*, and the best quote improves like $1/n$, which is the arithmetic behind every platform's claim that more responders means better prices.

The correction is the interesting part. In 2026 most dealers that answer a small RFQ do so with an auto-quoter, and every auto-quoter starts from a composite mid, so whatever error the composite carries, every responder carries too. Split each quote's distance into a part shared by everybody (the composite's error, a common hedging cost) and a part that is each dealer's own, and call the shared fraction $\phi$, the *anchoring share*. Competition can only compete away the dealer's own part; the shared part is there whether one dealer answers or fifty. At an anchoring share of 0.45, Theo's eleven responders were worth two independent ones, and no number of responders gets past $1/\phi$, about 2.2. The formula is the same one that gives the effective number of independent bets in an equicorrelated portfolio, and the resemblance is not a coincidence: the same algebra comes back as breadth in §2.9.

The framing also makes sense of a number from a bad day. On April 9, 2025, in the tariff shock, MarketAxess reported that average prices per US high-grade RFQ "dropped from 13.2 to 6.6," then "rebounded to 11.3 within a week" (MarketAxess, *AxessPoint*, 14 July 2025). Half the responders vanished in a morning. Had the dealers been independent, halving $n$ would have doubled the expected distance of the best quote. Anchored at $\phi = 0.45$, the effective count fell only from about 2.0 to about 1.9, and the damage of the day had to come from somewhere else: from $\theta$, the scale of every quote, or from $\phi$ itself moving as the composites stopped deserving trust. The desk argues about which one, live, in §2.9.3.

#### The Full Derivation: best-of-$n$ with a common anchor

Let $\delta_j \ge 0$ be dealer $j$'s quote distance from fair mid, for $j = 1, \dots, n$. For Theo's buy order this is the dealer's offer minus fair mid, in points of price. Suppose first that the $\delta_j$ are i.i.d. with CDF $F$ on $[0, \infty)$. The best quote is the minimum, $\delta_{(1)} = \min_j \delta_j$. It exceeds $x$ only if every quote exceeds $x$, so $\Pr(\delta_{(1)} > x) = \big(1 - F(x)\big)^n$, and by the tail-integral identity used in §2.2.2,

$$
\mathbb{E}\big[\delta_{(1)}\big] = \int_0^\infty \big(1 - F(x)\big)^n \, dx .
$$

For exponential distances with mean $\theta$, $1 - F(x) = e^{-x/\theta}$, so $(1-F(x))^n = e^{-nx/\theta}$ and

$$
\mathbb{E}\big[\delta_{(1)}\big] = \frac{\theta}{n}.
$$

The *cover* is the second-best quote, $\delta_{(2)}$. Because the exponential is memoryless, once the best quote is known the other $n-1$ quotes exceed it by i.i.d. exponential amounts with mean $\theta$. The gap from winner to cover is the minimum of those $n-1$ excesses:

$$
\mathbb{E}\big[\delta_{(2)} - \delta_{(1)}\big] = \frac{\theta}{n-1}, \qquad \frac{\mathbb{E}[\delta_{(2)} - \delta_{(1)}]}{\mathbb{E}[\delta_{(1)}]} = \frac{n}{n-1}.
$$

In this model the expected cover gap is about as large as the winner's own distance from mid. Theo's three-eighths cover suggests his winner was also roughly three-eighths from fair, which is plausible for a B2 bond *(illustrative)*. The best quote improves like $1/n$, which is the arithmetic behind every platform's claim that more responders means better prices.

Now the correction. In 2026 most dealers that answer a small RFQ do so with an auto-quoter, and every auto-quoter starts from a composite mid. Write each quote distance as a common part plus an idiosyncratic part:

$$
\delta_j = A + \varepsilon_j, \qquad A \ge 0,\;\; \mathbb{E}[A] = \phi\,\theta, \qquad \varepsilon_j \overset{\text{i.i.d.}}{\sim} \text{Exp}\big(\text{mean } (1-\phi)\,\theta\big),
$$

with $A$ independent of the $\varepsilon_j$ and $\phi \in [0,1]$ the *anchoring share*: the fraction of the average quote distance shared by every responder, such as the composite's own error or a common hedging cost. The minimum of $A + \varepsilon_j$ is $A + \min_j \varepsilon_j$, so

$$
\mathbb{E}\big[\delta_{(1)}\big] = \phi\,\theta + \frac{(1-\phi)\,\theta}{n}, \qquad \mathbb{E}\big[\delta_{(2)} - \delta_{(1)}\big] = \frac{(1-\phi)\,\theta}{n-1}.
$$

Competition can only compete away the idiosyncratic part. Define the *effective number of dealers* $n_{\text{eff}}$ as the number of independent dealers ($\phi = 0$) that would give the same expected best quote, so $\theta/n_{\text{eff}} = \phi\theta + (1-\phi)\theta/n$:

$$
n_{\text{eff}} = \frac{n}{1 + (n-1)\,\phi}, \qquad \lim_{n \to \infty} n_{\text{eff}} = \frac{1}{\phi}.
$$

This is the same formula as the effective number of independent bets in an equicorrelated portfolio, and the resemblance is not a coincidence. Set $n = 11$ and $\phi = 0.45$: $n_{\text{eff}} = 11/(1 + 4.5) = 2$. Eleven responders anchored to one composite at $\phi \ge 0.45$ are worth no more than two independent ones, and no number of responders gets you past $1/\phi$. That is the result the chapter opening promised.

Three caveats turn this from a slogan into a model. First, the cover gap measures only the idiosyncratic part. Tradeweb's median distance to cover hit a record low in 2024 (The DESK, Jan 29, 2025), which is what more competition predicts, but it is *also* what more anchoring predicts. To tell them apart, measure the winning quote against an independent fair value, not against the cover. Second, non-response is censoring, not a zero. A dealer who declines to quote is telling you $\delta_j$ exceeded what they were willing to show. Chapter 18 models response probability jointly with the quote. Third, the common-value problem, which gets its own box.

> **Poker Table.** Ines puts it in a sentence: "Eleven responders is a big table. Order statistics say the best quote improves like $1/n$. The winner's curse says the one guy who knows you just left a lender call improves it like minus $1/n$." This is the common-value auction. When the bond's value is uncertain and the request itself carries information, each dealer has to ask what the bond is worth *given that it won*, and winning against more rivals is worse news. A rational dealer facing a possibly informed client shades more as $n$ grows, so on toxic flow the best quote can *worsen* with competition. The hand history is the markout: compare the fill to the composite five minutes, one hour and one day later, grouped by $n$. If markouts against the winner grow with $n$, the table is telling you who is informed. In most cases that is the client. Chapter 3 builds this as a counterparty-type model. For Theo, the practical rule: if the RFQ name is anywhere near a liability-management transaction, eleven responders are not eleven independent opinions. They are eleven people deciding how much they believe you.

So the RFQ on a wire did two things to the desk's numbers. It made $\mathbb{E}[c]$ measurable at the moment of the trade, as a winner and a cover inside the same two minutes, and it turned every request, filled or not, into a labeled observation of $\Pr(\text{fill})$.

## 2.4 Revolution 2: All-to-All, or the Buy Side Learns to Quote

Kaz reads "all-to-all" as graph theory and asks, with real interest, whether the corporate bond market is now a complete graph. "It's a graph where the edges have prices," says Ines, "and half the nodes are lying about their degree." That is a fair one-line summary of what all-to-all trading changed. Anyone on the platform can respond to an RFQ, not only the dealers the client invited, and the anonymity that makes that safe for responders also hides which nodes are informed.

MarketAxess launched Open Trading, the largest all-to-all pool, in 2013 according to its own FY2025 10-K. Several slide decks you will see on the desk say 2012. If your model's first feature is the launch date of its own data source, check the 10-K. The protocol is simple. A client's RFQ goes to its chosen dealers *and* to an anonymous pool of other participants, including asset managers, hedge funds, non-bank market makers and other dealers, and the platform stands between the two sides so neither has to take the other's credit. The effect was to turn the buy side from price takers into occasional price makers, and quants were among the first to take the other side:

> **[SOURCE EXTRACTION]** *Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.6:* "larger players in quant credit have begun to make markets on the all-to-all electronic platforms, meaning that they are price makers as well as price takers."
>
> **Annotation.** This sentence changes what a quant credit fund *is*. A price taker needs a cost model. A price maker needs an *adverse-selection* model, because every time it answers an RFQ it is selling an option to whoever sent it. Man's primer put the scale at \$116.5bn of quant-fund volume on Open Trading in the first three quarters of 2020, up 150% year on year (Man, *Quant Credit: A Primer*, 2021). Where the 2026 desk departs: all-to-all has settled as a large structural minority, not a takeover. Open Trading carried 35.2%, 35.0% and 37.0% of eligible MarketAxess credit volume in 2023, 2024 and 2025, with about 1,800 participating firms (MarketAxess 10-Ks), and all-to-all was about 11% of total US market volume in April 2025 (Greenwich). The quant that answers RFQs is now an ordinary participant. What remains open is whether its quotes are smart enough to survive the RFQs it would rather not have answered.

The economics show up in two places. For liquidity *takers*, MarketAxess estimates 2025 price improvement on Open Trading of \$324.9mm, plus \$171.6mm for liquidity *providers*, \$496.4mm in total, measured against its CP+ composite (FY2025 10-K). The comparable totals were \$701.9mm in 2023 and \$488.8mm in 2024. For the market as a whole, Kozora, Mizrach, Peppe, Shachar and Sokobin (2020), *Alternative Trading Systems in the Corporate Bond Market* (NY Fed Staff Report 938), find that dealer participation on ATSs lowers customer trading costs by 24 to 32 bp, and that ATS trades are smaller, more often IG, and concentrated in older, less active issues. The last finding matters: all-to-all helps most in exactly the bonds where the dealer you invited was least interested.

Third, there is direct evidence that quotes from outside the relationship move prices. Hendershott, Li, Livdan, Schürhoff and Venkataraman (2026), *Quote Competition in Corporate Bonds* (*Journal of Finance* 81(4)), study dealer runs on about 24,000 bonds. A dealer's quote improves client execution by 6 to 7 bp just by being present. The best-quoting dealer wins only 15% of trades, and 16% to 40% of trades print worse than the best available quote. Non-relationship dealers handle 23% of trades when they quote, against 11% when they do not. The authors call quoting "not a zero-sum game." For a systematic desk, the 16%–40% trade-through range is a reminder that a best quote on a screen is not a fill, which is why §2.5 trains on fills.

Which brings the chapter to Ines's favorite object.

> **Math, Gently.** *A markout is a hand history.* After a poker hand, a serious player replays it: what did I know, what did they know, and what did the cards that came afterward say about who was right? A markout is the same replay for a trade. When you provide liquidity, you take a small edge at the moment of the fill, the price improvement you charged against the composite. Then you watch where the composite goes over the next five minutes, hour or day. If it moves against you, the person who traded with you knew something, or was early to something, and the move is what you paid for not knowing it. Your expected profit is the edge minus the expected adverse move, and both halves are averages over many hands, not a verdict on any single one. A tiny number: a provider buys at 3 bp better than the composite, and an hour later the composite has fallen 4 bp. The provider showed an edge of 3 and played a hand worth $3 - 4 = -1$ bp. It paid one basis point to be told, an hour late, what the other side already knew. Repeat that across a thousand fills and the platform's "price improvement" statistic will still report the 3. The full version follows.

The hand history, written down for a liquidity provider: let $h$ be the edge at the fill, the provider's price improvement relative to the composite, in bp of price. Let $m_H$ be the adverse markout at horizon $H$, how far the composite moves against the provider in the $H$ after the fill. The provider's expected P&L per unit notional, before hedging costs and under $\mathbb{P}$, is

$$
\mathbb{E}\big[\Pi^{\text{LP}}\big] = \mathbb{E}[h] - \mathbb{E}[m_H].
$$

The \$171.6mm in the 10-K is $\sum h$ summed over all provider fills. It is the edge the provider showed, not the hand it played. A provider whose markouts eat that edge has paid 1,800 firms for the privilege of being the last one to learn what they knew. Chapter 3 conditions $\mathbb{E}[m_H]$ on counterparty type and RFQ timing, which is where Theo's lender-call instinct becomes a feature.

> **View From Another Seat.** *The systematic fund as liquidity provider, in its own published words.* Put a systematic credit manager on the far side of Theo's all-to-all ticket and the RFQ looks like one row in a very long table. It arrives anonymous, with a size, a rating, an age, a time since the last print, and the fund's quoting engine prices it on those features within the response window, or declines. It is not trying to win every hand. It is trying to win the hands whose markouts it can live with, across thousands of small fills, so that no single informed seller can hurt it much. That seat also knows its limits, and the clearest public account comes from Man Numeric's Robert Lam and Paul Kamenski on Man's *Long Story Short* podcast ("Extra Credit: Algorithmic Advantage," recorded March 2024; quotations from the speech-recognition transcript). They describe execution as a daily choice of "venue selection," "high touch or low touch," including "circumstances where the best course of action is to trade voice." And on size: a 10–50 million block sent through a single dealer "might not be the optimal way"; the alternative is to "slice it" and route each piece to "the best venue and the best protocol." Read from Theo's chair, that is a warning as much as a description. The fund quoting tight on his \$4mm Halvorsen ticket may be the same fund slicing a block in Halvorsen across three venues that afternoon, and its quote on his RFQ is one of the slices. The anonymity that let it answer him is the anonymity that kept him from knowing.

> **Desk Myth vs. Desk Reality.** *Myth:* All-to-all means the dealer is dead. *Reality:* Dealers are among the most active responders in all-to-all pools, disclosed RFQ to chosen dealers still carried 44% of US e-volume in 2024 (Greenwich), and the client still picks dealers by hand: more than two-thirds of buy-side traders hand-pick their RFQ dealers, and about 80% say relationships drive venue choice (Greenwich, Dec 2023). All-to-all added nodes. It did not delete the relationships, and it gave them a measurable price.

All-to-all, then, raised $\Pr(\text{fill})$ for small tickets in exactly the bonds the invited dealers liked least, and it put the buy side on the other side of $\mathbb{E}[c]$, where one firm's cost of a fill is another firm's edge minus its markout.

### Deep-Dive Resource Graph

**Podcasts.** None listed for §§2.3–2.4: we could not verify specific episode titles and dates for this edition.

**Practitioner Writing.** Coalition Greenwich, Kevin McPartland, blog post on ten years of fixed-income market-structure evolution (June 10, 2025): https://www.greenwich.com/blog/ten-years-fixed-income-market-structure-evolution. Coalition Greenwich, press release on block trades as the next frontier for electronic execution (Dec 7, 2023): https://www.greenwich.com/press-release/block-trades-next-frontier-electronic-execution-corporate-bonds. Coalition Greenwich, *U.S. corporate bond trading in 2024 by the numbers* (Jan 2025): https://coalitiongreenwich.crisil.com/content/dam/coalition-greenwich/MarketViews/2025/US-corporate-bond-trading-2024-numbers-25-C4001.pdf. The DESK, Lucy Carter, on Greenwich's full-year 2024 e-trading data (Jan 21, 2025): https://www.fi-desk.com/coalition-greenwich-e-trading-boom-to-outpace-market-growth-in-2025/. Man Institute, *Quant Credit: A Primer* (2021): https://www.man.com/maninstitute/quant-credit-primer.

**Academic Papers.** Hendershott & Madhavan (2015), *Click or Call? Auction versus Search in the Over-the-Counter Market*, JF 70(1), DOI 10.1111/jofi.12164. Hendershott, Li, Livdan, Schürhoff & Venkataraman (2026), *Quote Competition in Corporate Bonds*, JF 81(4), DOI 10.1111/jofi.70048. Kozora, Mizrach, Peppe, Shachar & Sokobin (2020), *Alternative Trading Systems in the Corporate Bond Market*, NY Fed Staff Report 938: https://www.newyorkfed.org/research/staff_reports/sr938. Hendershott, Livdan & Schürhoff, *All-to-All Liquidity in Corporate Bonds* (working paper). O'Hara & Zhou (2021), *The electronic evolution of corporate bond dealers* (JFE).

**Data & Code.** MarketAxess 10-K FY2025 (Open Trading share, price improvement, automation counts): https://www.sec.gov/Archives/edgar/data/1278021/000119312526067009/mktx-20251231.htm. Canonical root for later filings: https://www.sec.gov/edgar.

## 2.5 Revolution 3: Automation, or Algos Answering Algos

Theo's eleven responses came back in under two minutes, and several came back in about a second. "Those weren't traders," says Ines. "They were parameters. Somebody set a size limit, a spread tolerance around the composite and a list of names to stay away from, and then went to lunch."

Automation is the revolution hidden inside the word "electronic." On the buy side, about 60% of credit participants used some form of automated execution by late 2024, up from about 40% (Barclays survey via The DESK, Jan 2025; Man's 2025 *Systematic Credit: A New Frontier* cites the same 60%). MarketAxess counted 204, 245 and 261 client firms using its automated and algorithmic tools in 2023, 2024 and 2025, and dealers sent 32.5 million algorithmic responses in 2023 and 40.9 million in 2024 (10-Ks). On Trumid, 75% of RFQs executed "no-touch" in Q4 2024 (The DESK, Jan 10, 2025), and 88% of eligible RFQ line items did by September 2025 (The DESK, Oct 8, 2025). Tradeweb's AiEX handled more than 40% of its institutional trades in 2025, against 30% in 2021 (FY2025 10-K). Vanguard automates about 70% of its traded volume, up from about 40%, and still sends nothing without a trader watching (The DESK, Oct 2026). FINRA's own 2022 statistic from §2.2.1, that 82.9% of trades were already reported within one minute, is the regulator's view of the same thing: a print that arrives in seconds was never touched by a human booking clerk.

What automation needs is a router that decides, for each line, which protocol to try and in what order. Man described the inputs to theirs:

> **[SOURCE EXTRACTION]** *Man_Revolutions_in_Credit_Trading_2023 p.5:* "We can see whether a security is actually available for RFQ, filtering to only high-quality RFQ participants as well as on the frequency of RFQs, the rate of completed trades, and whether a given trade size is digestible in RFQ form."
>
> **Annotation.** Read it as a feature list. "Available for RFQ" is the feasible set from §2.1. "High-quality RFQ participants" is a dealer-level score built from response rates, quote quality and markouts. "Frequency of RFQs" and "rate of completed trades" are a bond-level fill-rate history. "Digestible" trade size is a size-dependent fill probability. Every item is estimated from venue logs, and none of them existed before the venues did. Where the 2026 desk departs: in 2023 this was a filter that removed bad candidates before a trader decided. On a 2026 desk, the same features feed a model that *chooses* the protocol and the order of attempts. It still keeps a human on the kill switch, because the parameters that work on a calm Tuesday are not the ones you want on a gap day.

Man also named the dataset that makes the router trainable:

> **[SOURCE EXTRACTION]** *Man_Revolutions_in_Credit_Trading_2023 p.4:* "Electronic venues give us greater insight into these imbalances – such as realised prints, bid/ask spreads, or trades that were attempted but not executed – and thus greater confidence in identifying and quantifying liquidity and costs."
>
> **Annotation.** The key phrase is "trades that were attempted but not executed." A voice market records only the trades that happened. An electronic market also records the ones that failed: the RFQ nobody answered, the quote that was too wide, the order that was pulled. Those failures are the negative labels a fill-probability model needs. Without them you are fitting $\Pr(\text{fill})$ on a sample in which every trade filled, which gives you a model that is always optimistic. On a 2026 desk this is the most valuable table in the execution database, and also the one most often dropped because it "has no trades in it."

### 2.5.1 The router as a cost-minimization problem

Let $p$ index protocols (all-to-all RFQ, disclosed RFQ to chosen dealers, session or mid-match, inclusion in a portfolio trade, voice). For a line with features $x$, define:

- $\pi_p(x) = \Pr(\text{fill} \mid x, p)$, the fill probability, usually a logistic model fitted on attempted-and-failed labels;
- $c_p(x) = \mathbb{E}[c \mid \text{fill}, x, p]$, the expected one-way cost given a fill, in bp of price relative to fair mid;
- $\kappa(x)$, the cost of *not* filling: the expected cost of the next attempt plus the price of carrying the unintended position from §2.1 until then. A simple form is $\kappa = c^{\text{next}} + \tfrac{\gamma}{2}\,\sigma_\epsilon^2\, T^{\text{wait}} + \alpha^{\text{decay}}$, with $\gamma$ risk aversion, $\sigma_\epsilon^2$ the line's residual variance per year, $T^{\text{wait}}$ the expected wait in years, and $\alpha^{\text{decay}}$ the signal lost while waiting.

All expectations are under $\mathbb{P}$. The expected all-in cost of a single attempt is

$$
J_p(x) = \pi_p(x)\,c_p(x) + \big(1 - \pi_p(x)\big)\,\kappa(x),
$$

and the one-shot router picks $p^\star = \arg\min_p J_p(x)$. Real routers try protocols *in sequence*, and a failed attempt has a price of its own: information leakage, $\chi_p \ge 0$, the adverse move caused by showing the order and not trading. Trying all-to-all first and falling back to disclosed RFQ costs

$$
J_{A \to R} = \pi_A c_A + (1 - \pi_A)\big(\chi_A + J_R\big).
$$

Subtract this from $J_R$ and rearrange. Trying all-to-all first is better if and only if $\pi_A (J_R - c_A) > (1 - \pi_A)\chi_A$, or, assuming $J_R > c_A$,

$$
\frac{\pi_A}{1 - \pi_A} \;>\; \frac{\chi_A}{J_R - c_A}.
$$

The odds of filling must exceed the ratio of leakage cost to savings. Take a \$2mm line of a 7-year BBB *(all numbers illustrative)*: $c_A = 4$ bp, $\pi_A = 0.55$, $J_R = 0.90 \times 7 + 0.10 \times 20 = 8.3$ bp (with $\kappa = 20$ bp), and $\chi_A = 1.5$ bp. The threshold is $1.5/4.3 = 0.35$. The fill odds are $0.55/0.45 = 1.22$, so the router tries all-to-all first, at an expected cost of $J_{A\to R} = 2.2 + 0.45 \times 9.8 = 6.6$ bp against 8.3 bp for going straight to dealers. Now make the name a stressed HY credit two weeks before an exchange offer: $\chi_A$ jumps because the anonymous pool is full of people who read the same 8-K, $\pi_A$ falls, and the inequality flips. The router sends it to a trader. It turns out the formula agrees with Mags.

> **Ways This Blows Up.** *Fair-weather parameters.* Every number in the router was estimated on 2023–2025 data, mostly in calm markets. In stress, dealers widen their algorithm parameters or switch them off, fill rates fall and leakage rises, and all of it happens at once. Buy-side traders at FILS Europe in 2026 said platforms and electronic liquidity providers "help mainly in normal markets" (The DESK, Oct 2026). In March 2026, median EUR IG bid-ask rose to 64% above its January average, and it took 4 weeks (EUR IG), 6 (US HY), 8 (US IG) and 13 (EUR HY) to normalize (MarketAxess data via The DESK, Oct 1, 2026). A router trained on the calm sample will be most confident on exactly the day it is most wrong. Condition $\pi_p$, $c_p$ and $\chi_p$ on a stress regime variable (§2.7 offers one: the ETF–NAV basis), and give the kill switch to a human.

## 2.6 Revolution 4: Portfolio Trading

"A portfolio trade," says Mags, "is a mystery box, except the dealer gets to look inside before paying, and the index closes at four so everyone gets to be surprised at the same time."

A portfolio trade (PT) is one negotiation and one price for a basket of many bonds, sometimes hundreds of lines and sometimes a mix of buys and sells, executed all-or-none with a single dealer. The dealer prices the basket as a whole, hedges its systematic risk at once (a Tradeweb executive described a 1,000-line PT hedged with at most seven Treasury trades; The DESK, Jan 29, 2025) and works off the idiosyncratic residue over days. Tradeweb says it offered the first corporate-bond PT in 2019 (FY2025 10-K). FIMSAC recommended a TRACE flag for portfolio trades in February 2020. FINRA's portfolio-trade modifier became mandatory on May 15, 2023, for trades between two parties, in at least ten unique issues, at a single basket price (FINRA RN 22-12). Before that date nobody could measure PT share from public data. After it, everybody could, and everybody used a different denominator.

Man's account of the first boom:

> **[SOURCE EXTRACTION]** *Man_Revolutions_in_Credit_Trading_2023 p.2:* "We found that orders attracted high fill rates as competition for trades proliferated, not only among what we would consider tier-one counterparties but also those in the second tier, with aggressive pricing offered."
>
> **Annotation.** This describes 2021, which Man called "the year of portfolio trading." For a systematic book, high fill rates on a basket solve the §2.1 problem at once: a 300-line rebalance either fills completely or does not fill at all, so there is no half-executed portfolio to carry. The second-tier dealers matter too, because they meant more effective competitors in the sense of §2.3.2. Where the 2026 desk departs: the boom did not last. In the first half of 2022, Man reports, PT pricing worsened as dealers pulled balance sheet and the custom ETF baskets that made baskets cheap to recycle were lost (pp.2–3). Man moved most of its flow back to single-line electronic RFQ. Fill rates are a property of dealer balance sheets, and balance sheets change.

### 2.6.1 What a dealer bids for a basket

Let $w$ be the vector of signed notionals in the basket ($w_i > 0$ if the dealer buys line $i$), $P_i^{\text{mid}}$ each line's fair mid, and $c_i^{\text{line}}$ its standalone half-spread. A skeleton for the dealer's bid, with the full engine in Chapter 19, is

$$
B_{\text{PT}} = \sum_i w_i P_i^{\text{mid}} \;-\; \sum_i |w_i|\, c_i^{\text{line}} \;+\; \Pi(w) \;-\; \frac{\gamma}{2}\, T_{\text{liq}}\; w^\top \Sigma_\epsilon\, w .
$$

The first term is fair value. The second is the sum of single-line costs. $\Pi(w) \ge 0$ is the *netting credit*: the value of being able to net lines against existing inventory or deliver them into an ETF creation basket. The last term is the risk charge on the residual after the hedge, with $\gamma$ the dealer's risk aversion, $T_{\text{liq}}$ the liquidation horizon in years and $\Sigma_\epsilon$ the residual covariance of returns per unit notional per year.

Here is why baskets are cheaper than blocks. Take $N$ equal lines of notional $w$, total $M = Nw$, with residual variance $\sigma^2$ per line and a common residual correlation $\rho_\epsilon$. Then $w^\top \Sigma_\epsilon w = w^2\sigma^2\,[N + N(N-1)\rho_\epsilon]$, and the risk charge per dollar of basket is

$$
\frac{\gamma}{2}\,T_{\text{liq}}\,\sigma^2 M \cdot \frac{1 + (N-1)\rho_\epsilon}{N}.
$$

A single-name block of the same size $M$ carries the factor 1 in place of the fraction. So a \$100mm, 200-line basket with uncorrelated residuals carries $1/200$ of the idiosyncratic risk charge of a \$100mm block in one bond *(illustrative)*. The fraction $(1 + (N-1)\rho_\epsilon)/N$ is $1/n_{\text{eff}}$ from §2.3.2 again. Diversification across lines, like competition across dealers, cannot get past the common component. With $\rho_\epsilon = 0.1$, no basket goes below one-tenth of the block charge.

The 2022 episode is now readable in the formula: $\Pi(w)$ collapsed when custom ETF baskets disappeared, and $\gamma$ rose as dealers cut balance sheet. Mags's mystery box is the term the formula leaves out, which is adverse selection. The client knows which lines it most wants to get rid of, and a basket priced on average line costs invites the client to stuff it with the worst ones. Dealers respond by pricing line by line and adding a charge for the basket's composition. Chapter 19 estimates that charge, and the trend research suggests screening lines on the Priming Risk Score of Chapter 13 before the desk prices a basket. A 150-line HY basket can hide two or three liability-management candidates, and spotting them is an RSSG skill.

> **Trend Watch.** **Portfolio trading, 2021–2026: from novelty to infrastructure, measured with at least three denominators.**
>
> | Period | Measure | Value | Source |
> | :-- | :-- | :-- | :-- |
> | 2021 → 2022 | PT share of US e-volume (protocol mix) | ≈7% → ≈10% | `Man_Revolutions p.4`, Fig. 4, Greenwich MarketView; chart reading, CHECK |
> | 2023 | PT share of TRACE | ≈7–8% | Tradeweb's Ted Husveth, via The DESK (Jan 29, 2025) |
> | 2023 | PT share of *customer* volume | ≈5% | Bondwave, "A Market Transformed" (May 20, 2026) |
> | 2024 | PT share of IG / HY volume | 10% / 8%; near 13% of IG in December | Greenwich (Jan 2025) |
> | 2024 | Electronic PT ADNV | \$3.3bn (+76%); ≈85% of all PT; Tradeweb more than 2/3 | Greenwich (Jan 2025) |
> | Dec 2024 | PT share of TRACE | 11.4% | The DESK (Jan 29, 2025) |
> | Apr 8, 2025 | PT share of a \$89.7bn peak-volatility day (Trumid basis) | 12% | Greenwich, citing Trumid (Apr 14, 2025) |
> | Sept 30, 2025 | PT share of a \$84.7bn record day | 18% | Greenwich, *2025 by the numbers* (Jan 27, 2026) |
> | Q1 2026 | PT share of customer volume | 19.8% | Bondwave (May 20, 2026) |
> | Q1 2026 | Share of all corporate volume printing at the index mark | 15.5% (5% in 2016; 9.3% in 2021) | Bondwave (May 20, 2026) |
> | Q2 2026 | MarketAxess PT ADV and its share of US credit PT | \$1.97bn (+33%); about 20% | MarketAxess Q2 2026 release |
>
> **What it means for the desk.** "PT is about 11–12% of the market" and "PT is about 20% of the market" are both true. The first uses TRACE, which includes interdealer prints, as the denominator. The second uses customer volume. Pick one and label it. Index-time clustering is now a structural feature: nearly half of PT volume prints at or after the index pricing time (Bondwave), so cost models need a time-of-day term, and a backtest that fills rebalances at the 4 p.m. mark is assuming the most crowded fill of the day. The basket arbitrage is also compressing. Bondwave's PT execution-quality percentile drifted from 57.3 (May 2023) to 50.3 (February 2026), toward the median, which is what competition does to an edge.

### 2.6.2 Case Study: The Portfolio-Trading Cycle, 2021–2026

**2021, the boom.** ETF growth and algorithmic dealer pricing made baskets cheap. Man moved most of its order flow from voice into portfolio trades and reports high fill rates and aggressive pricing from second-tier dealers (`Man_Revolutions p.2`).

**H1 2022, the reversal.** Rates rose and spreads widened. Dealers pulled balance sheet and custom ETF baskets disappeared, so PT pricing worsened (`Man_Revolutions pp.2–3`). This was a bad year for the strategy class as a whole: eVestment data cited by IFR show systematic credit funds down about 15% on average in 2022, with assets down 27% to about \$52bn, and transaction costs more than doubled (IFR, "Quant credit rebounds after tough period"). Man's response was to move more than 90% of flow onto electronic venues, mostly as single-line RFQs:

> **[SOURCE EXTRACTION]** *Man_Revolutions_in_Credit_Trading_2023 p.5:* "The vast majority of our trades are now sent as RFQs, leading to significant savings in transaction costs versus portfolio trades."
>
> **Annotation.** This is the router of §2.5.1 run on a whole book. When $\Pi(w)$ collapses and $\gamma$ rises, $J_{\text{PT}}$ climbs above $\sum_i J_{\text{RFQ},i}$, and a cost-minimizing desk unbundles the basket. Note what Man did *not* conclude: it did not decide that PT was a fad. It changed protocol because the costs changed, and the same logic sends flow back to PT when the costs reverse. Where the 2026 desk departs: today the PT-versus-RFQ decision is made line by line and day by day, inside the router. In 2023 it was an allocation decision made by people.

**2023–2026, the resurgence.** The TRACE modifier made PT measurable from May 2023. Costs fell: MarketAxess's median IG bid-ask went from 0.19 points in 2022 to 0.11 in 2024 (IFR), and the average ticket fell from about \$560k to about \$360k over four years. PT share then climbed through every denominator in the Trend Watch above, to 18% of the record day on September 30, 2025 and 19.8% of customer volume in Q1 2026.

**What a systematic desk would have flagged.** (i) The PT-minus-RFQ cost spread on comparable lines, measured by markouts, as a regime variable. It turned in early 2022, months before the annual statistics showed it. (ii) ETF creation and redemption activity as an input to $\Pi(w)$. (iii) The index-mark concentration as a cost of crowding. **How it would have traded.** Route rebalances by $\min\{J_{\text{PT}}, \sum_i J_{\text{RFQ},i}\}$ every day. Add liquid "sweetener" lines to baskets, because the dealer prices them cheaply and they lower the basket's average cost, and remove illiquid lines that raise $\gamma$. Treat protocol share as **regime-switching, not a trend**: a two-state model driven by dealer balance sheet and ETF-basket economics fits 2021–2026 better than any S-curve.

## 2.7 Revolution 5: ETFs as the Liquidity Backbone

Bond ETFs did something the cash market could not do for itself. They gave credit an exchange-traded, continuously priced, penny-wide instrument whose underlying is a basket of bonds that might not trade all week. Global bond ETF assets went from under \$10bn in 2009 to more than \$1.2tn in 2020 (Todorov, *BIS Quarterly Review*, March 2021) and about \$2.6tn at the end of 2024, when ETFs took about 40% of fixed-income fund flows (iShares, Apr 23, 2025). US bond ETFs held \$1.8tn at end-2024, 17% of US ETF assets (ICI 2025 Fact Book). BlackRock projects \$6tn globally by 2030, which is a forecast by the largest issuer and should be read that way.

The structural change was regulatory. The SEC adopted Rule 6c-11 on September 26, 2019 (press release 2019-190), allowing ETFs to use *custom* creation and redemption baskets under written policies. That turned the ETF into a tool for moving baskets of bonds. An authorized participant (AP) can now assemble a creation basket from bonds it wants to get rid of, or accept a redemption basket of bonds a dealer wants to buy. The result is what Todorov's anatomy shows: US corporate-bond ETF creation baskets cover only about 20% of holdings and redemption baskets about 35%, the holdings' bid-ask is about 17 times the ETF's (against about 5 times for equity ETFs), and for the largest bond ETF a basket can be as small as about 3% of holdings. Koont, Ma, Pástor and Zeng (NBER w30039; *RFS* 2025 with Sialm) show that ETFs actively manage these baskets, trading off index tracking against liquidity transformation, and that basket inclusion improves a bond's liquidity, except when creation or redemption imbalances are large.

### 2.7.1 The ETF discount as the price of immediacy

Let $P^{\text{ETF}}_t$ be the ETF's price, $\mathrm{NAV}_t$ its published net asset value per share (built from evaluated bond prices, often at the bid), $\mathcal{C}^{\text{red}}_t$ and $\mathcal{C}^{\text{cr}}_t$ the AP's per-share cost of liquidating a redemption basket or assembling a creation basket, and $f$ the fixed fee per share. An AP who buys a share, redeems it and sells the basket earns $\mathrm{NAV}_t - \mathcal{C}^{\text{red}}_t - f - P^{\text{ETF}}_t$. An AP who buys a basket, creates and sells the share earns $P^{\text{ETF}}_t - \mathrm{NAV}_t - \mathcal{C}^{\text{cr}}_t - f$. With no arbitrage, both are nonpositive, which gives the band

$$
\mathrm{NAV}_t - \mathcal{C}^{\text{red}}_t - f \;\le\; P^{\text{ETF}}_t \;\le\; \mathrm{NAV}_t + \mathcal{C}^{\text{cr}}_t + f .
$$

The band assumes $\mathrm{NAV}_t$ is the true value of the basket. It is not. Evaluated prices lag, so write true basket value as $\mathrm{NAV}_t + \eta_t$, where $\eta_t$ is the information the ETF price has and the stale marks do not. Under selling pressure, the price sits at the lower edge of the band around the *true* value:

$$
P^{\text{ETF}}_t - \mathrm{NAV}_t \;\approx\; -\,\mathcal{C}^{\text{red}}_t \;+\; \eta_t \qquad (\text{with } f \text{ absorbed}).
$$

In a sell-off both terms are negative. Liquidating the redemption basket is expensive, and the marks have not caught up with a falling market. A measured discount is therefore partly the price of immediacy and partly the NAV being wrong. Neither is a free lunch for the buyer: the first is a cost you are paid to bear, and the second goes away when the marks catch up. In March 2020, bond-ETF tracking errors exceeded 200 bp against a historical average of 0.7 bp (Todorov), and Haddad, Moreira and Muir (2021, *RFS*) found that safer bonds and IG ETFs were discounted *more* than HY. That inverted ranking is what you would expect if dealer balance sheet, not credit risk, was the scarce input. Chapter 1 (§1.8.3) shows the LQD episode. Chapter 20 builds the full engine.

The discount is the cleanest real-time stress variable a credit desk has. It is observable every second, it combines the cost of immediacy with information about stale marks, and it is the regime input the router in §2.5.1 was asking for. On a calm day the ETF is an inexpensive hedge. On a stressed day it becomes the place where prices are discovered, and on April 7, 2025, US fixed-income ETFs traded a record \$98.9bn, 3.4 times the 2025 year-to-date daily average, while ETF bid-ask spreads held at one cent through April 1–8 (iShares). As a share of cash bond volume, though, credit ETFs *shrank* in calm markets: the ETF-to-cash ratio fell from 23.2% in 2022 to 16.6% in 2024 (Greenwich), as portfolio trading took over part of the basket risk transfer. ETFs, PTs and cash bonds are now three routes for the same basket risk, and credit index futures are becoming a fourth (Cboe iBoxx futures block trades topped \$1bn a month in mid-2026; The DESK, Oct 2026).

And then there is the Fed. The Secondary Market Corporate Credit Facility, announced March 23, 2020, was allowed to buy IG bonds and US-listed ETFs giving broad exposure to IG corporates, and was expanded on April 9. The New York Fed began "certain" SMCCF purchases on May 12, 2020, and those first purchases were ETFs; "additional" purchases, the individual bonds, began on June 16 (NY Fed SMCCF page). So for about five weeks in 2020 the most powerful central bank on earth was trading credit through the same ticker as a dentist in Scottsdale. The more important lesson, from Haddad, Moreira and Muir, is that the *announcements* did most of the work: discounts closed well before the Fed bought much. Purchase authority expired December 31, 2020, ETF sales began June 7, 2021 and bond sales July 12, 2021, and by August 31, 2021 all holdings had been sold or had matured (NY Fed). Section 2.9.3 compares March 2020 with April 2025.

### Deep-Dive Resource Graph

**Podcasts.** None listed for §§2.5–2.7: episode titles and dates on portfolio trading and bond ETFs (for example on *Bloomberg Odd Lots*) were not verified for this edition.

**Practitioner Writing.** Man Institute, *The Revolutions in Credit Trading* (June 2023): https://www.man.com/insights/revolutions-in-credit-trading. Bondwave, Paul Daley, "A Market Transformed" (May 20, 2026): https://bondwave.com/a-market-transformed/. The DESK, on record portfolio-trading volumes (Jan 29, 2025): https://www.fi-desk.com/record-volumes-but-room-to-grow-in-portfolio-trading/. The DESK, on the Barclays automation survey (Jan 2025): https://www.fi-desk.com/fixed-income-automation-surge-60-of-credit-traders-now-use-robots/. The DESK, FILS Europe coverage of buy-side views on platforms and ELPs in stress (Oct 2026): https://www.fi-desk.com/dont-rely-on-platforms-or-elps-in-stressed-markets-buyside-traders-say/. iShares, on bond ETF innovation and the April 2025 volume record (Apr 23, 2025): https://www.ishares.com/us/insights/bond-etf-innovation-opportunity. IFR, Christopher Whittall, "Quant credit rebounds after tough period": https://www.ifre.com/story/4857744/quant-credit-rebounds-after-tough-period-qq6zcqq1mt.

**Academic Papers.** Todorov (2021), "The anatomy of bond ETF arbitrage," *BIS Quarterly Review*: https://www.bis.org/publ/qtrpdf/r_qt2103d.htm. Koont, Ma, Pástor & Zeng, *Steering a Ship in Illiquid Waters: Active Management of Passive Funds* (NBER w30039): https://www.nber.org/papers/w30039. Haddad, Moreira & Muir (2021), *When Selling Becomes Viral: Disruptions in Debt Markets in the COVID-19 Crisis and the Fed's Response* (RFS; NBER w27168). Meli & Todorova (Barclays), *Portfolio trading in corporate bond markets* (year to be confirmed). Shim & Todorov, *ETFs, illiquid assets, and fire sales*.

**Data & Code.** FINRA Regulatory Notice 22-12 (PT modifier): https://www.finra.org/rules-guidance/notices/22-12. SEC press release 2019-190 (Rule 6c-11): https://www.sec.gov/news/press-release/2019-190. New York Fed SMCCF page: https://www.newyorkfed.org/markets/secondary-market-corporate-credit-facility. Federal Reserve SMCCF page: https://www.federalreserve.gov/monetarypolicy/smccf.htm. Tradeweb 10-K FY2025 (AiEX, Ai-Price, first PT): https://www.sec.gov/Archives/edgar/data/1758730/000175873026000015/tw-20251231.htm. ICI 2025 Investment Company Fact Book: https://www.ici.org/system/files/2025-05/2025-factbook.pdf.

## 2.8 Revolution 6: Non-Bank Liquidity Providers, and the Blocks That Stayed on the Phone

The capital-letters responder in Theo's RFQ was probably a non-bank liquidity provider: a firm that makes markets with its own capital, prices with models rather than relationships, and hedges with ETFs, CDX and futures. Their arrival is the most recent revolution and the least well measured, so every number below carries its source and a self-reported flag where one applies.

- **Jane Street** entered corporate bonds through its bond-ETF franchise. As an AP and ETF market maker it was already pricing the baskets, and pricing the individual bonds followed naturally. IFR reports it as a top-five liquidity provider in corporate bonds on Bloomberg (via Rupak Ghose, Mar 27, 2026).
- **Citadel Securities** began trading corporate bonds in mid-2023. It traded about \$2bn a day in 2025, and IFR estimates about a 15% share of blocks over \$5mm with more than seven years to maturity (same source). In 2026 the firm itself reported a 14.2% share of IG credit block risk transfer (The DESK, Oct 2026; self-reported, CHECK).
- **Hudson River Trading** extended its push into debt in late 2025, according to a Bloomberg report of Dec 1, 2025 (title only; not verified here).
- **Across the market**, non-banks earned about 10% of credit market-making revenue in 2024 (Greenwich, Jan 2025) and about 13% of global credit market-making revenue in 2025 (Greenwich, June 2025). Over the same period, BCG estimates that big banks' global flow-credit revenues fell 26% from 2019 (via Ghose).

The dealer economics explain why the banks let this happen. Electronic channels carried 48% of US IG activity in 2024 but only about a fifth to a quarter of dealer IG revenue: 20% in The DESK's summary, 26% in Greenwich's full report. In HY the split was 33% of activity against 10% of revenue (Greenwich, Jan 2025). Electronification is *dealer-permitted*. Banks let the small, liquid, low-margin flow move to the wire and kept voice for the blocks, where the margin is. The platforms consolidated too. On July 29, 2026, ICE agreed to buy MarketAxess for \$167 a share in cash, an enterprise value of about \$5.7bn, with closing expected in the first half of 2027 (ICE 8-K). By Q2 2026, Tradeweb's *fully electronic* US high-grade TRACE share (19.0%) had passed MarketAxess's *total* high-grade share (17.5%) (company releases). MarketAxess has also stopped publishing monthly volumes, so one of the series in the Trend Watch boxes above has stopped updating. The trend report puts it plainly: whoever owns the composite owns the benchmark for best execution, price improvement and the PT reference price.

For the RFQ model of §2.3.2, the non-banks bring a lower $\theta$, because they quote tighter, and plausibly a higher $\phi$, because they all start from the same composites and hedge in the same ETFs. Whether that combination raises $n_{\text{eff}}$ is an empirical question, and your own logs can answer it.

Now the part of the market none of this reached. In December 2023, about 90% of block trades (IG of \$5mm or more, HY of \$1mm or more) were still done by phone or chat. Only about 10% of buy-side block orders went electronic, and market-wide electronic growth had been "roughly flat over the past two years" (Greenwich, Dec 7, 2023). Man's Kamenski told IFR that single-name electronic costs were at "some of the lowest transaction cost levels we've ever seen," while voice blocks were "oftentimes twice as expensive or more." Pintér, Wang and Zou (2022, Bank of England SWP 970) explain why size is hard to model. Across clients, larger trades get *better* prices (a size discount), because the clients who trade large are the sophisticated ones with relationships. For a given client, larger trades cost *more* (a size penalty). A cost model fitted without client identity mixes the two effects and can get the sign of the size coefficient wrong.

This is the ceiling $K < 1$ from §2.3.1, seen from the trading floor. It is also where Theo's training pays. The `5MM+` world of §2.2.2 is the world of hidden block sizes, stressed names, ad hoc groups and liability-management candidates. In that world the prices are least transparent, the router hands control to a person, and the person who has read the credit agreement knows more than the composite does. The electronic market is the market for boring risk. Theo's edge is in the rest of it.

## 2.9 Why This Made Systematic Credit Possible: The Data-Exhaust Theorem

Blackstone's systematic team states the size of the gap:

> **[SOURCE EXTRACTION]** *Blackstone_Systematic_Credit p.2:* "While systematic strategies manage roughly 20% of global equities, they account for less than 2% of the fixed-income universe."
>
> **Annotation.** A factor of ten, which the rest of this section explains as a cost problem. Equity quants have traded at fractions of a basis point on public order books for two decades. Credit quants traded through the protocol of §2.3 and the dealers of §2.8. The next sentence on the same page credits "the proliferation of electronic bond trading" with making credit factor investing possible. Where the 2026 desk departs: the 2% is a stock, not a flow, and our trend data say the flow has turned. The gap closes as quickly as the cost function below falls, and in HY blocks it hardly falls at all.

Man adds the operational point, that systematic credit needs "larger amounts of smaller-sized trades compared to discretionary approaches" (`Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.7`). Many small tickets are exactly what automation made cheap. The question is how much cheaper tickets are worth.

### 2.9.1 Units first: LCS and the Man decomposition

Barclays defines liquidity "as the cost of a roundtrip institutional-size transaction in a bond" (`Ben_Dor_Quantitative_Credit_Portfolio_Management p.111`) and measures it with the Liquidity Cost Score:

> **[SOURCE EXTRACTION]** *Dynkin_Systematic_Investing_in_Credit p.702:* "For bonds quoted on spread, LCS is calculated as a product of bid–offer spread and spread duration. For lower‐quality bonds traded on price, LCS is calculated as the difference between offer and bid prices divided by the bid price."
>
> **Annotation.** Two conventions, one quantity, and the derivation below shows they agree. Three points about units cause most errors in practice. LCS is a *round trip*, so the one-way cost is $\mathrm{LCS}/2$. The spread must be in decimal, not bp, inside the formula. And the duration is *spread* duration, not modified duration, which differs for floaters and callables. Where the 2026 desk departs: Barclays built LCS from trader quotes because TRACE could not give a contemporaneous bid-ask (§2.3). A 2026 desk can also estimate it from RFQ quotes and composites, and should check that the two agree before trusting either.

For a spread-quoted bond, the price is a function of the spread, $P(s)$, with $\Delta P/P \approx -D^{\text{spr}}\,\Delta s$. The bid side is the *higher* spread, so $s^{\text{bid}} > s^{\text{ask}}$ and $P^{\text{bid}} = P(s^{\text{bid}}) < P^{\text{ask}}$. Then

$$
\frac{P^{\text{ask}} - P^{\text{bid}}}{P^{\text{bid}}} \;\approx\; \frac{-P\,D^{\text{spr}}\,(s^{\text{ask}} - s^{\text{bid}})}{P} \;=\; D^{\text{spr}}\,\big(s^{\text{bid}} - s^{\text{ask}}\big) \;\equiv\; \mathrm{LCS}^{\text{spr}} \;>\; 0,
$$

with error of order $D^{\text{spr}}\,(s^{\text{bid}} - s^{\text{ask}})/2$ relative to LCS, from dividing by $P^{\text{bid}}$ rather than the mid. For a bond with $D^{\text{spr}} = 5$ and a 10 bp bid-offer in spread, $\mathrm{LCS} = 5 \times 0.0010 = 0.50\%$ of price round trip, or 25 bp one way.

Man's actionable cost has three parts: "TC = Inside Market Spread + Slippage + Spread Calibration" (`Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.21`). The inside market spread is the best quoted bid/offer. Slippage is the extra cost of the trade itself, accounting for bond characteristics and for information leakage while the order is worked. Spread calibration measures whether dealers' actual prints fade or improve on their quoted levels, estimated from TRACE. All three must be in the same unit, bp of price one way, before you add them. Calibration can be negative, when dealers print better than their runs. Exercise 4 is about the classic mistake, adding a round-trip LCS to a one-way slippage.

### 2.9.2 The theorem: cost sets breadth, and breadth sets the information ratio

Grinold's fundamental law says $\mathrm{IR} \approx \mathrm{IC}\sqrt{\mathrm{BR}}$, with BR the number of independent bets per year. Suppose each unit of annual one-way turnover $\mathrm{TO}$ buys a proportional number of fresh bets, $\mathrm{BR} \propto \mathrm{TO}$. Then gross alpha per unit of gross exposure scales as $\alpha^{\text{gross}}(\mathrm{TO}) = k\sqrt{\mathrm{TO}}$, where $k > 0$ combines IC, active risk and the bets-per-turnover constant. With one-way cost $c$ (a fraction of notional), net alpha is

$$
\alpha^{\text{net}}(\mathrm{TO}) = k\sqrt{\mathrm{TO}} - c\,\mathrm{TO}.
$$

This is concave in $\mathrm{TO}$. Setting the derivative to zero, $k/(2\sqrt{\mathrm{TO}}) = c$, gives

$$
\mathrm{TO}^\star = \frac{k^2}{4c^2}, \qquad \alpha^{\text{net}\,\star} = k\cdot\frac{k}{2c} - c\cdot\frac{k^2}{4c^2} = \frac{k^2}{4c}.
$$

**Optimal turnover scales as $1/c^2$, and optimal net alpha scales as $1/c$.** The breadth a strategy can afford, $\mathrm{BR}^\star \propto 1/c^2$, rises faster than cost falls. Man reports that trading costs fell from 12 to 7.5 bp per million, with Amihud illiquidity down 37% since 2023, trade counts growing about 15% a year and about \$1.1tn of bonds moving from the illiquid to the liquid bucket over five years (Man, *Systematic Credit: A New Frontier*, data as at Sept 30, 2025). Put $c$ from 12 to 7.5 bp: $\mathrm{TO}^\star$ rises by $(12/7.5)^2 = 2.56$ times and $\alpha^{\text{net}\,\star}$ by $12/7.5 = 1.6$ times. As an illustration, a signal with $k = 0.0048$ goes from 4 turns a year and 48 bp of net alpha to 10.2 turns and 77 bp. That is the data-exhaust theorem in one line: **the same signal, on cheaper plumbing, is a better strategy.** Momentum, the highest-turnover credit factor (`Man_2022 p.19`), gains the most (Chapter 10).

Kaz insists on the caveats. Bets are not independent, so $\mathrm{BR} \propto \mathrm{TO}$ holds only until you run out of distinct ideas, and the universe size caps it. Costs are not constant: $c$ rises with ticket size and with crowding, which is what the 4 p.m. index-mark clustering in §2.6 costs. And $c$ must be the *one-way* cost if $\mathrm{TO}$ is one-way turnover. With those caveats, the direction holds: what made systematic credit possible was not a new factor but a lower $c$.

### 2.9.3 Case Study: Two Shocks, Five Years Apart (March 2020 and April 2025)

**March 2020, the old plumbing under load.** From late February to March 23, 2020, the cash market seized. Kargar, Lester, Lindsay, Liu, Weill and Zúñiga (2021, *RFS*; NBER w27355) estimate that customers' willingness to pay for immediacy rose by about 200 bp per dollar at the peak, and that trades shifted from risky-principal to agency as dealers stopped committing capital. Bond-ETF tracking errors exceeded 200 bp (Todorov), and IG and Treasury ETFs were discounted *more* than HY (Haddad, Moreira and Muir). The Fed announced the PMCCF and SMCCF on March 23 and expanded the facilities on April 9 (to up to \$850bn together with TALF). Its first SMCCF purchases, of ETFs, came only on May 12. The announcements did most of the stabilizing. Electronic share rose during the crisis, as Man observed:

> **[SOURCE EXTRACTION]** *Man_Revolutions_in_Credit_Trading_2023 p.5:* "2022 was the year of electronic trading. Interestingly and perhaps intuitively, though, some of the biggest jumps in electronic trading have come during the most stressful times in credit trading, such as 2020 and 2022."
>
> **Annotation.** This looks like a paradox, given that HY e-share falls in hard months (§2.3) and the robots widen in stress (§2.5). It is not one. When dealer voice capacity disappears, clients who still need to trade go to wherever anyone is still answering, which is the all-to-all pool and the ETF. Stress pushes the *marginal* liquidity provider onto the wire even as the *hardest* tickets go back to the phone. Where the 2026 desk departs: in 2020 this was an emergency migration. By 2025 the electronic routes already existed for the shock to use, as the second half of this case shows.

**April 2025, the new plumbing under load.** The tariff shock was the same type of event: a sudden, macro-driven rush for liquidity. The plumbing behaved differently. US fixed-income ETFs traded a record \$98.9bn on April 7, with spreads held at one cent (iShares). US corporates traded \$89.7bn on the peak-volatility day of April 8 (Trumid basis), 12% of it through portfolio trades (Greenwich, citing Trumid). Treasuries traded \$2.4tn on April 9, and all-to-all carried about 11% of April market volume (Greenwich, McPartland). By June, 52% of IG was trading electronically (Greenwich). There was no facility, no emergency rate cut, and no March-2020 style ETF discount spiral. A Fed note of Aug 19, 2026 adds that outflows in the tariff week did not concentrate in illiquid funds (FEDS Note).

**What a systematic desk would have flagged.** In 2020: the ETF–NAV basis as a regime switch, a jump in Man-style spread calibration (dealers fading their runs), and rising fill-failure rates in the attempted-but-not-executed table. In 2025: the same indicators moved, but by much less and with faster recovery, and PT share *rose* on the worst days. **How it would have traded.** Shrink tickets, route to all-to-all and PT first under the odds threshold of §2.5.1, use the ETF as the hedge and as a price signal rather than an exit, and slow rebalancing until markouts normalize. **The lesson.** The trend is real. The same type of shock, five years later, cleared through electronic channels. But the March 2026 EUR IG episode in §2.5 is a reminder that "cleared" is a statement about one market in one shock. Chapter 28 builds the stress playbook for the day it does not clear.

### Specification for AI Implementation

Asked to "route every line to the cheapest protocol," ROBO sent the whole book to all-to-all, because the spec never said an unfilled order costs anything. Half the book did not fill, and the desk ended up short beta it never chose (§2.1). What follows is the spec that prevents that, with $\kappa$ included.

**Module.** `ch02_electronification_trend.py`, four cumulative blocks that run in order in one interpreter on numpy, scipy and pandas, seeded with `SEED = 7`.

**Schemas and shapes.** `OBS: DataFrame[year: float, segment: str, share: float in (0,1), source: str]`, one row per *sourced* observation, one source series per segment (§2.3 Ways This Blows Up). `fit_adoption(years, shares, K)` takes two `(N,)` arrays and returns a dict `{K, r, t0, odds_doubling_years, logit_resid, projection, note}`, where `projection: DataFrame[year: int, share_hat: float, K: float]` covers 2026–2030. `rfq_best_of_n(theta, n, phi)` returns Monte Carlo and closed-form best quote, cover gap and $n_{\text{eff}}$. Quote distances are in points of price. `lcs_*` return a round-trip fraction of price. `man_tc_bp` returns one-way bp of price. `route(lines, kappa_bp)` takes `DataFrame[line_id: str, protocol: str, pi_fill: float in [0,1], c_fill_bp: float]` and returns the best protocol per line together with the full $J$ table.

**Edge cases and guards.** Shares at 0 or 1 are clipped to $[10^{-4}, 1-10^{-4}]$ with a warning, and the logarithm only ever sees clipped values. A single observation returns `None`. A ceiling $K$ at or below the largest observed share raises an error. A non-increasing series raises an error, and a non-monotone one is fitted with its logit residuals reported. The three-parameter fit runs `curve_fit` with bounds $K \in [0.05, 1]$, $r \in (0, 2]$, `maxfev=10000` and `p0 = (0.9, r_ols, t0_ols)`. If it fails, the code falls back to logit-OLS, and it attaches a "not identified" note when $\hat K$ lands on the last observation or $\hat r$ hits its bound. Years are centered on 2015 so the optimizer is not asked to resolve $t_0 \approx 2025$ to $10^{-6}$ in absolute terms. Monte Carlo uses $2\times 10^5$ draws, which gives a standard error of about 0.2% on each mean.

Every budget cycle someone asks the question ROBO answered with 103%: what share of high yield will trade electronically by 2030, and so how many tickets can the automation carry? The honest answer is a curve through three or four published data points from sources that do not agree on what a "share" is. Fit it by hand in a spreadsheet and it drifts. This quarter's version uses the Greenwich denominator, next quarter's uses the platform's, and nobody remembers which. A desk automates the fit for the same reason it automates a reconciliation: to write the ceiling, the units and the refusals down once, so the next analyst cannot quietly fit a market of 103%.

The first block sets the scaffolding: a seed, a clip level of $10^{-4}$, 2015 as the reference year, and a `check` function that appends each test to a table and halts the run if the test fails. `OBS` then holds six rows, three for US IG and three for US HY, each with its source, as §2.3.1 demanded.

`fit_adoption` does the work. It returns `None` for fewer than two points, clips shares into $[10^{-4}, 1-10^{-4}]$ with a warning, and subtracts 2015 from the years so the optimizer is never asked to locate a midpoint near 2025 to six decimals. It then takes the generalized logit of each share against the ceiling, which for a fixed ceiling is a straight line in time, and a degree-one `np.polyfit` returns the slope $r$ and the midpoint $t_0$. Last, it projects 2026 to 2030 through the logistic and returns the rate, the midpoint, the odds-doubling time $\ln 2 / r$ and the line's residuals in logit space. The default `K=None` means a ceiling of 1, a float fixes a ceiling taken from outside evidence such as 0.80, and the string `"fit"` runs a bounded `curve_fit` on the levels, started from the OLS rate, as a diagnostic only. If the optimizer fails, the function keeps the OLS fit and says so in `note`.

The checks tie the code to the text. The OLS slope equals the closed-form two-point slope, a two-parameter `curve_fit` at $K=1$ lands on the same curve, and every projection rises inside $(0, K)$. IG reaches about 64% in 2030, HY odds double in about 3.5 years, a lower ceiling raises the implied rate, and ROBO's constant-growth rule, run for contrast, exceeds 1.

Use it as a planning input for a segment with at least two points from one source series and an outside view of the ceiling. Do not use it to estimate the ceiling, to forecast, or on a series spliced from two sources. The edge case that bites is the one Kaz found. Hand `"fit"` the IG points 20%, 48% and 48%, and it returns $K = 0.48$, a perfect fit and a `note` saying the ceiling is not identified. The function warns and carries on, so a pipeline that reads `K` and ignores `note` will pass along a market whose electronification is already over.

*The full listing is [Listing 2.1 in Appendix F](#code-2-1).*

Theo's eleven responders had all glanced at the same composite before answering, and the question at the top of every RFQ is how many dealers to ask. The platform's slide says more. The chapter's answer is a closed form, $n_{\text{eff}} = n/(1+(n-1)\phi)$, and Ines would call a closed form a read, not a result, until it has been dealt out a few hundred thousand times. A desk automates the test because the formula is about to sit inside a dealer-selection rule, and nobody wants a rule resting on algebra that was only checked on a whiteboard. The same function then becomes the test bed for the day your own logs deliver a $\phi$.

`rfq_best_of_n(theta, n, phi, n_sims, seed)` simulates the RFQ as a one-line auction and returns the numbers the text derived. It rejects `theta <= 0`, fewer than two dealers and an anchoring share outside $[0, 1)$. For each of `n_sims` simulated RFQs it then draws one common anchor from an exponential distribution with mean $\phi\theta$, shaped as a single column so that it broadcasts across all $n$ dealers: inside one RFQ every dealer shares the anchor, and across RFQs the anchor changes. To each dealer it adds an independent exponential with mean $(1-\phi)\theta$. `np.partition` at position 1 puts the best quote in column 0 and the cover in column 1 without sorting the row. The function returns the simulated mean best quote and mean winner-to-cover gap, the closed forms $\phi\theta + (1-\phi)\theta/n$ and $(1-\phi)\theta/(n-1)$, and $n_{\text{eff}}$, all in the units of `theta`, points of price. The seed defaults to `SEED`, so a repeated call returns identical numbers. Pass another seed to see the Monte Carlo noise, about 0.2% on each mean at $2\times 10^5$ draws.

The checks come in three parts. At $\phi=0$ and $n$ of 3, 5, 8 and 12, simulation and closed form must agree within 2%, and they do within about a quarter of a percent. `n_eff` for eleven dealers at $\phi = 0.45$ must equal 2, and that check passes `n_sims=10` because it needs no draws. Eleven dealers anchored at $\phi = 0.5$ must also post a worse mean best quote, about $0.545\theta$, than two independent dealers at $0.5\theta$. Note that the simulation meets the closed form only at $\phi=0$. The anchored case rests on the algebra and on that ordering test.

Use it to sanity-check a platform's claim about more responders, to size a dealer list, and as the test bed once your logs yield a $\phi$. Do not use it on toxic flow: the winner's curse, which can make the best quote worse as $n$ grows, is not in the model, and neither are non-responses, which are censored quotes and not zeros. The edge case that bites is the cover gap. Read the closed form and the common anchor has dropped out: the gap is $(1-\phi)\theta/(n-1)$, so it shrinks when more dealers join and it shrinks when the dealers anchor harder. A record-tight cover is therefore consistent with competition and with herding, and the function will happily produce either.

*The full listing is [Listing 2.2 in Appendix F](#code-2-2).*

Pull one BBB bond's cost from three sources on the same morning and you get three dialects: a 10 bp bid-offer in spread from the trader's run, a bid and an offer in points of price from the platform, and a round-trip liquidity cost score from the index provider. A cost model that adds them is not off by a rounding error. It is off by a factor of two, or ten thousand, in whichever direction looks prudent. Exercise 4 asks you to find that bug, and the desk's answer is to make it hard to commit: one function per convention, each named for its unit, each refusing inputs that cannot be real, and everything forced into one-way basis points of price before the cost model sees it.

`bond_price` values a fixed-coupon bullet on a coupon date. It takes `round(maturity * freq)` periods, pays `100 * coupon / freq` each period plus 100 at the end, and discounts each flow at $(1+y/\text{freq})^{-\text{freq}\cdot t}$. There is no accrued interest on a coupon date. `spread_duration` bumps the total yield (Treasury yield plus spread) by $\pm 10^{-5}$, takes the central difference of the price and divides by the base price, giving percent of price per unit of spread, in years. It uses one flat Treasury yield for every cash flow and has no optionality, so it is right for this bullet and wrong for a floater or a callable.

Three small functions carry the conventions. `lcs_spread_quoted` multiplies spread duration by the bid spread minus the ask spread, in decimal, and raises an error if the order is reversed, since a bid is the higher spread. `lcs_price_quoted` divides offer minus bid price by the bid price, the form for bonds quoted on price, and rejects an ask below the bid or a non-positive bid. `man_tc_bp` adds the inside spread, slippage and calibration in basis points of price, one way. It rejects a negative inside spread or slippage and accepts a negative calibration, because dealers sometimes print better than their runs.

The demo is an illustrative BBB: a 5% coupon, 5.5 years, a 4.0% Treasury yield, a 120 bp spread and a 10 bp bid-offer in spread. Spread duration comes out near 4.7 years. The two LCS conventions agree to about a quarter of a percent, the round trip costs about 47 bp of price, and the one-way cost is half of that, 23.7 bp, inside the 10 to 40 bp range the check enforces. A Man cost of 6, 2.5 and $-1$ bp sums to 7.5.

Use these functions as the front door for every cost source before it reaches a router or a turnover calculation. Do not use `spread_duration` for anything with optionality or a floating coupon. The edge case that bites is that the guards police order, not scale or sidedness. Feed `lcs_spread_quoted` spreads in bp and the order check passes happily, with an answer 10,000 times too big. Feed `man_tc_bp` a round-trip LCS and it adds it to a one-way slippage without comment. Only the explicit halving and the range check in the demo stand in the way. A float has no idea what it measures.

*The full listing is [Listing 2.3 in Appendix F](#code-2-3).*

The week the cost report says tickets got cheaper, two questions land on the desk. The PM asks what that does to the strategy, and the head trader asks what ROBO should do with each line tomorrow morning. They look unrelated. They are the same cost function seen from the top and from the bottom: cheaper execution lets a signal afford more turnover, and the router decides where each line goes now that failing to fill has a price. Both answers are small formulas, and both need rerunning every quarter, when the inputs move. The listing computes both and checks the first against a brute-force search and the second against the worked example in §2.5.1, because a formula that looks right on a whiteboard at 1 a.m. is how desks get surprised at 9:30.

`optimal_turnover(k, c)` returns $k^2/4c^2$ and $k^2/4c$, the turnover and the net alpha at the peak of $k\sqrt{\mathrm{TO}} - c\,\mathrm{TO}$, and rejects a non-positive $k$ or $c$. The cost $c$ is the one-way cost as a fraction of notional, so 7.5 bp enters as `7.5e-4`. With $k = 0.0048$, cutting $c$ from 12 to 7.5 bp moves the optimum from 4.0 to 10.24 turns and net alpha from 48 to 76.8 bp. The code verifies the closed form against a grid of 300,001 turnover values between 0.01 and 30, and the ratios 2.56 and 1.6 hold to nine decimals.

`route` then handles the lines. It validates that fill probabilities lie in $[0,1]$, computes $J = \pi c + (1-\pi)\kappa$ for every protocol row using one scalar $\kappa$ in bp, and picks the minimum per `line_id`, returning both the winners and the full table. For the demo's 7-year BBB line, all-to-all costs 11.2 bp, disclosed RFQ 8.3 and voice 12.16, so the one-shot router picks the RFQ. `try_a2a_first` applies the sequential rule. It returns False if the RFQ cost does not exceed the all-to-all cost, since there is nothing to save, and True if the fill is certain. Otherwise it compares the fill odds with leakage divided by savings. Here the odds of 1.22 beat the threshold of 0.35, so the desk opens in all-to-all for an expected 6.61 bp against 8.3 bp for going straight to dealers. For the stressed name, with a fill probability of 0.25 and leakage of 6 bp, the rule says no. The closing table of checks prints only if every `check` passed.

Use the turnover formula for direction, not for point estimates, because it assumes bets scale with turnover and cost does not rise with size, and both give out. Use the router only with parameters conditioned on the market regime. The edge case that bites is that the two routers define failure differently. The one-shot $J$ charges a miss the full $\kappa$ of 20 bp, which leaves all-to-all behind the RFQ at 11.2 bp against 8.3. The sequential rule charges a miss only the 1.5 bp of leakage plus a second attempt, which makes the same venue the best opener. Apply the one-shot score to a venue you would try before a fallback and you will under-use it, which is how a router ends up ignoring the cheapest liquidity on the screen.

*The full listing is [Listing 2.4 in Appendix F](#code-2-4).*

## 2.10 Desk Debrief

- **Liquidity used to be a relationship and is now a variable.** A bond's value lives in its documents, and its tradability lives in its data exhaust. A systematic strategy needs both certainty of execution and a cost it can model (`Man_Revolutions p.4`), and each revolution improved one or both.
- **TRACE is censored, not missing.** `5MM+` and `1MM+` hide the blocks. Ben Dor's imputed caps imply Pareto tail indices of about 5/3 (IG) and 4/3 (HY), both with infinite variance. Train on the capped feed you will see live, and deduplicate affiliate echoes before fitting anything.
- **Fit adoption with a ceiling, and get the ceiling from outside the data.** Two points cannot identify $K$, and a fitted $K$ equal to the last observation is a warning, not a result. IG is around half electronic and HY has been near a third for four years. The gap between them is the structural fact.
- **Eleven anchored dealers are worth about two.** $n_{\text{eff}} = n/(1 + (n-1)\phi)$, capped at $1/\phi$. A falling cover gap is consistent with competition and with herding, so measure the winner against an independent fair value.
- **Route on all-in cost, including the cost of failing.** $J_p = \pi_p c_p + (1-\pi_p)\kappa$. Try all-to-all first only when the fill odds exceed leakage divided by savings. Near an LMT, leakage jumps and the formula agrees with Mags.
- **Protocol share is a regime, not a trend.** PT went from boom (2021) to bust (2022) to infrastructure (19.8% of customer volume, Q1 2026). Label every share with its denominator, and treat the ETF–NAV basis as the regime switch.
- **Cheaper plumbing makes the same signal a better strategy.** $\mathrm{TO}^\star \propto 1/c^2$ and $\alpha^{\text{net}\,\star} \propto 1/c$. Cutting cost from 12 to 7.5 bp is worth 2.56 times the turnover and 1.6 times the net alpha.
- **Theo's edge lives where the exhaust is thinnest.** About 90% of blocks still trade by phone or chat. The `5MM+` world of stressed names and ad hoc groups is where the router hands control to a person, and that person should have read the credit agreement.

### The Spec You Hand the Robot

Build `ch02_electronification_trend.py` with four functions and one sanity table. (1) `fit_adoption(years, shares, K=None|float|"fit")`: generalized-logit OLS for a fixed ceiling, plus a bounded three-parameter `curve_fit` diagnostic ($K \in [0.05,1]$, $r \in (0,2]$, `maxfev=10000`, logit-OLS fallback, a "not identified" note). Clip shares to $[10^{-4}, 1-10^{-4}]$, refuse a single point, reject $K \le \max(\text{share})$, center years on 2015, and return a 2026–2030 projection inside $(0, K)$. (2) `rfq_best_of_n(theta, n, phi)`: seeded Monte Carlo ($2\times10^5$ draws) of best quote and cover gap with anchoring share $\phi$, checked against $\phi\theta + (1-\phi)\theta/n$ and $(1-\phi)\theta/(n-1)$ within 2%, and returning $n_{\text{eff}} = n/(1+(n-1)\phi)$. (3) `lcs_spread_quoted`, `lcs_price_quoted` and `man_tc_bp`: spreads in decimal, LCS round trip, TC one way in bp, agreement within 5% for a 5.5-year bond with a 10 bp bid-offer. (4) `optimal_turnover(k, c)` returning $(k^2/4c^2,\ k^2/4c)$, verified by grid search, and `route(lines, kappa_bp)` minimizing $J = \pi c + (1-\pi)\kappa$ per line, plus the sequential odds rule. Every number in the demo is either sourced in `OBS.source` or labeled illustrative. Every check is an `assert`, collected and printed as a table.

### Exercises

1. **(Censoring.)** Suppose 10% of HY trades print as `1MM+`, uncapped HY trades average \$0.3mm, and the hidden tail is Pareto with $\hat\alpha = 4/3$. Show that TRACE's displayed volume is $(0.1 \times 1 + 0.9 \times 0.3)/(0.1 \times 4 + 0.9 \times 0.3) \approx 55\%$ of true volume. Then find the tail index at which the displayed share would be 80%. (Interpret it in terms of how much a desk can see.)
2. **(The ceiling.)** For observations $e_1 < e_2 < K$, prove that $\hat r(K)$ from §2.3.1 is decreasing in $K$. Compute $\hat r$ and the 2030 projection for US HY with $K \in \{0.5, 0.6, 0.8, 1.0\}$, and explain to ROBO, in one spec line, why $K = 0.5$ is not free.
3. **(Order statistics.)** Show that for i.i.d. Uniform$[0, b]$ quote distances, $\mathbb{E}[\delta_{(1)}] = b/(n+1)$. Then Kaz asks how many anchored dealers with $\phi = 0.6$ it takes to match two independent ones. Prove the answer is "none," and say what that implies about paying for a twelfth platform connection.
4. **(Units.)** A junior adds a 50 bp round-trip LCS to 3 bp of one-way slippage and 2 bp of calibration and gets "TC = 55 bp." Fix it. Then use $\mathrm{TO}^\star \propto 1/c^2$ to compute by how much the error was shrinking the strategy's optimal turnover.
5. **(The router and Mags.)** With $c_A = 4$ bp, $J_R = 8.3$ bp and $\chi_A = 1.5$ bp, find the smallest $\pi_A$ at which all-to-all goes first. Now the name is three weeks from an uptier and $\chi_A = 6$ bp. Find the new threshold, and write the one-sentence note Theo leaves for ROBO explaining where the 6 came from.
6. **(Data-exhaust theorem.)** Re-derive $\mathrm{TO}^\star$ and $\alpha^{\text{net}\,\star}$ when cost rises with turnover through crowding, $c(\mathrm{TO}) = c_0 + c_1\,\mathrm{TO}$. Show that optimal turnover now responds *less* than $1/c_0^2$ to a fall in $c_0$, and connect $c_1$ to the 4 p.m. index-mark clustering in §2.6.

### Deep-Dive Resource Graph

**Podcasts.** We list no episodes for this chapter because none were verified this edition. Candidates for Edition 2, to be checked before listing: *Bloomberg Odd Lots* on bond electronification, portfolio trading and bond ETFs in March 2020. *Flirting with Models* (Corey Hoffstein) and *Capital Allocators* episodes with systematic-credit managers.

**Practitioner Writing.** Man Group, Russell Korgaonkar, *Systematic Credit: A New Frontier* (data as at Sept 30, 2025): https://www.man.com/insights/systematic-credit-new-frontier. Rupak Ghose, on Citadel Securities and the HFT industry (Mar 27, 2026): https://rupakghose.substack.com/p/citadel-securities-and-hft-industry. Coalition Greenwich, *US corporate bond trading: 2025 by the numbers*: https://www.greenwich.com/market-structure-technology/us-corporate-bond-trading-2025-numbers. The DESK, on December 2025 platform shares versus TRACE (Jan 14, 2026): https://www.fi-desk.com/marketaxess-and-tradeweb-beat-trace-in-december-slowdown/. Bloomberg, "High-Speed Trader Hudson River Steps Up Battle With Citadel Securities, Jane Street" (Dec 1, 2025; title only).

**Academic Papers.** Kargar, Lester, Lindsay, Liu, Weill & Zúñiga (2021), *Corporate Bond Liquidity During the COVID-19 Crisis* (RFS; NBER w27355). Pintér, Wang & Zou (2022), *Size discount and size penalty: trading costs in bond markets*, BoE SWP 970: https://www.bankofengland.co.uk/working-paper/2022/size-discount-and-size-penalty-trading-costs-in-bond-markets. Bessembinder, Jacobsen, Maxwell & Venkataraman (2018), *Capital commitment and illiquidity in corporate bonds* (JF). Dick-Nielsen & Rossi (2019), *The cost of immediacy for corporate bonds* (RFS). Bessembinder, Spatt & Venkataraman (2020), *A survey of the microstructure of fixed-income markets* (JFQA). Grinold & Kahn, *Active Portfolio Management* (the fundamental law).

**Data & Code.** ICE 8-K Exhibit 99.1 on the MarketAxess acquisition (July 2026): https://www.sec.gov/Archives/edgar/data/0001571949/000119312526324909/d116245dex991.htm. MarketAxess Q2 2026 results: https://investor.marketaxess.com/news/news-details/2026/MarketAxess-Reports-Second-Quarter-2026-Financial-Results/default.aspx. Tradeweb Q2 2026 Exhibit 99.1: https://www.sec.gov/Archives/edgar/data/1758730/000175873026000132/tw-2026xq2xex991.htm. SIFMA US corporate bond statistics: https://www.sifma.org/resources/research/statistics/us-corporate-bonds-statistics/. FINRA Rule 6730 (TRACE reporting, including the PT modifier): https://www.finra.org/rules-guidance/rulebooks/finra-rules/6730. Federal Reserve FEDS Note on bank-loan and HY fund liquidity (Aug 19, 2026): https://www.federalreserve.gov/econres/notes/feds-notes/liquidity-transformation-risks-in-u-s-bank-loan-and-high-yield-mutual-funds-a-2026-update-20260819.html.

<!-- STATUS: COMPLETE -->
