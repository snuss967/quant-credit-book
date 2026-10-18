# Chapter 3-B: Your First Year on the Desk: The Day, the Week, the Quarter, and the Twelve Mistakes Ex-Bankers Make

> **Prerequisites.** Chapter 3, especially the markout (§3.3), the Edge Ledger (§3.5) and the information wall (§3.6.3). Every piece of mathematics in this chapter is introduced from scratch in a Math, Gently box, and each box points to the chapter that owns the full version. This chapter is Theo's year on one desk. The week in five different shops is Chapter 1-B, the pre-seat plan is `00_02`, and the mechanics of information walls live in §3.6.3. We point to them rather than repeat them.

## Cold Open: 6:47 a.m., Day One

*Tuesday, late September. The coffee machine is warming up, and so is the security master.*

The first thing Theo Marsh sees on his first morning on the systematic desk is not a price. It is a diff: the list of everything in the security master that changed overnight. Most of it is lint, a rating outlook here and a sector code there. One row is red. **Halvorsen Packaging 7.25% senior secured notes due 2029: new CUSIP.** (Halvorsen is fictional, and every number in this chapter is illustrative unless sourced.) The old line is still there, smaller, like a house after the extension has been sold. An A/B exchange closed overnight: holders swapped their 144A notes for identical registered notes. Nothing economic happened. Every system on the floor believes something did.

Under it, a second row: *vendor evaluated-price file: expected 06:45, received —.*

"It'll come," says Kaz, without turning around. "It's always late the week of a roll."

Ines Okafor puts a printout on Theo's desk. Yesterday's explain. "We're down forty and the model knows about twenty-eight."

"Forty what?"

"Basis points of capital. Four hundred thousand dollars, if you're still a banker. Find the other twelve. You have until the risk meeting."

"I wrote the model," says Kaz. "The model is fine."

"The model is always fine," says Ines. "That's why it needs a babysitter."

Mags Dunleavy reads the printout upside down on her way past. "Back in my day the explain was a phone call and a grudge. You asked the trader where the money went, he said 'the market,' and you held it against him until bonus season."

At 6:58 ROBO posts to the desk channel. On the train in, Theo had typed "build me a calendar." ROBO has subscribed the desk to every U.S. federal holiday and flagged Monday, 12 October, as a credit event.

Theo touches the USB stick in his pocket, the one with his 13-week cash flow model on it, for emotional support. He knows how to read an indenture in an afternoon, and nobody has asked him to. What he has been asked to do is find \$120,000 in a spreadsheet before 7:30, on a desk whose vendor is late and whose robot thinks Columbus sailed into default.

**The question this chapter answers: what does this desk actually do all day, and which parts of it can an ex-banker do on Tuesday?**

By the end of this chapter you will be able to: read a systematic credit desk as a set of nested clocks (the day, the week, the month and the quarter) and say which system fires at each hour; explain why two systems with two timestamps manufacture a fake P&L, and size it; turn the contract clocks a restructuring banker already knows (grace periods, record dates, consent deadlines, RSA milestones, NDA outside dates, cleansing 8-Ks) into dated features of a default intensity; treat an information wall as a dated interval rather than a permanent state; recognize the twelve mistakes ex-bankers make in their first year and the single confusion underneath all of them; compute how little forty bets can tell anyone about your skill, and what you will be measured on instead; and hand ROBO a specification for `desk_calendar.py`, the calendar the desk actually uses.

## 3B.1 The Day as a Timeline

A restructuring engagement runs on milestones that a lawyer has typed into a document. A systematic desk runs on milestones that a scheduler has typed into a cron table, and most of them fire before the market opens. Theo's first day is a tour of those milestones, mostly in the order in which they break.

**6:45, the feed diff.** The security master is the credit agreement of the system (§27.3): it says what each identifier is, what it pays, when, and what it can turn into. The overnight diff is the list of amendments. Theo's instinct is the right one: an A/B exchange is the kind of corporate action that produces phantom P&L, because the position system can see the move from the old CUSIP to the new one as a sale at one mark and a purchase at another. The stub left behind is illiquid, so its evaluated price drifts away from the new line within days, and any position still booked against it starts producing numbers. Theo spends forty minutes proving that the custodian moved the desk's \$12mm face across at the same price, that the stub belongs to other people, and that the exchange ties to the cent. It does. The twelve basis points are not there.

This is the first boring lesson, and it is a real one. Forty minutes spent proving that something is *not* the problem is not wasted on a desk. Ruling a suspect out is most of what an explain is.

**7:15, the explain.** The morning explain (§8.1, and the full production version in Chapter 8-C) splits yesterday's P&L into lines that each have a reason: coupon carry, rates by key rate, spread by factor, idiosyncratic moves by issuer, each hedge leg on its own line, and a residual called *unexplained*. Unexplained is not a line item. It is an accusation, and it stays open until somebody closes it. Desks set a tolerance, a few basis points of capital or a fixed dollar amount, beyond which the residual must be chased before the risk meeting. Twelve basis points is far outside any tolerance a desk would publish.

**7:30, the risk pack.** The risk pack sets the book's exposures against the limit sheet (Chapter 8-B): DTS by rating and sector cell, the CS01 ladder, key-rate DV01s, the ten largest issuer jump-to-default exposures, expected shortfall, and days to liquidate. Theo reads it the way he once read a compliance certificate, looking for the covenant that is about to trip. "A limit," Mags tells him, "is something you breach politely, in writing, before lunch." She is describing a soft limit, which can be overridden with an email and a reason. A hard limit cannot be, and the difference is the most important column on the sheet.

**8:30, the pre-open calendar.** New issues pricing today, calls and tenders settling, coupon and record dates, month-end index rebalances, CDX roll weeks, an FOMC afternoon. The calendar decides which names get a wider quote, which hedges need to be rolled and which signals should be ignored for a day because a known flow will swamp them. It is also the list ROBO tried to build.

**Intraday.** Three loops run while the market is open. The fills loop takes each execution from the order system (§27.4) through booking, risk and P&L. The hedge loop watches the drift between the book's DV01 and DTS and the hedges that were set against them this morning (§8.6). The RFQ loop watches the desk's hit ratio, its cover gaps and the clients whose requests it is winning too often (Chapter 18-B). None of this is glamorous. Most of it is a screen of numbers that should stay green.

> **View From Another Seat.** A systematic asset manager spends its intraday hours on a different loop: not "should we quote?" but "how should we trade what the model already wants?" Man Group's credit team describes the working day this way: execution means choosing "venue selection ... high touch or low touch," and in some circumstances "the best course of action is to trade voice"; a \$10–50mm block through one dealer "might not be the optimal way," and the alternative is to "slice it" and route to "the best venue and the best protocol" (Man Institute, "Extra Credit: Algorithmic Advantage," recorded March 2024, speech-recognition transcript). A dealer sees the same bond as inventory to be priced, and the asset manager sees it as an order to be worked. Theo's desk makes markets, so its intraday clock is the RFQ timer; the asset manager's is the cost curve (Chapter 2-B).

**3:00 p.m., the snap.** At one agreed moment the desk photographs everything: positions, risk factors, hedges, marks. The photograph is the snap, and it exists because of a fact so dull that every new hire underestimates it: different instruments stop moving at different times, and different vendors photograph them at different times. Treasury futures settle in the early afternoon Chicago time, around 3 p.m. in New York. Evaluated bond prices are struck mid-to-late afternoon, equities close at 4 p.m., and CDX end-of-day marks come later still (§8.6, *approx.; check each venue's methodology*).

> **Math, Gently.** *DV01, and why two photographs make a ghost.* A bond's DV01 is the dollars it gains when its yield falls by one basis point (0.01%). For \$50mm face of a five-year bond with a modified duration of 4.4, DV01 is $50{,}000{,}000 \times 4.4 \times 0.0001 = \$22{,}000$ per basis point. Hedge it with Treasury futures of equal and opposite DV01, and a parallel move in yields should leave the pair flat. Now photograph the bond at 4:00 and the futures at 3:00. If Treasuries rally 4 bp between the two photographs, the bond's picture shows the rally and the hedge's picture does not. The pair appears to have made $4 \times \$22{,}000 = \$88{,}000$, and tomorrow, when the hedge's next photograph catches up, it will appear to lose it. Nobody traded. Nothing happened. The full version is the explain's timing line in Chapter 8-C.

The algebra is three lines, and it is worth doing once, because it tells you what the ghost looks like. Let $\Delta y_t$ be the change in the yield, in basis points, measured from yesterday's snap to time $t$ today. With the sign convention of the box, a position with DV01 $\text{DV01}_B$ marked at time $t$ makes $-\text{DV01}_B\,\Delta y_{t}$. If the bond is marked at $t_2$ and the hedge, with $\text{DV01}_H = -\text{DV01}_B$, is marked at $t_1$, the book reports

$$
\Pi^{\text{book}} = -\text{DV01}_B\,\Delta y_{t_2} - \text{DV01}_H\,\Delta y_{t_1} = -\text{DV01}_B\,\big(\Delta y_{t_2} - \Delta y_{t_1}\big).
$$

The true P&L of a perfectly hedged book is zero, so everything on the right-hand side is phantom. It has two properties. It reverses: tomorrow's report contains the same term with the opposite sign, so it is zero on average over two days. And it is noisy every single day, with a size set by how far yields can wander between the two photographs.

> **Math, Gently.** *A random walk, and why an hour is not a seventh of a day.* A random walk is a quantity that takes independent steps: today's step tells you nothing about tomorrow's. Its variance (the average squared distance from where it started) grows in proportion to time, so its standard deviation, the typical distance, grows with the *square root* of time. If Treasury yields move about 6 bp in a typical day *(illustrative)* and a trading day is six and a half hours, one hour is $1/6.5$ of the day's variance but $1/\sqrt{6.5} \approx 0.39$ of its typical move: about 2.4 bp, not 0.9. Risk adds up in squares, and that is why short gaps are bigger than they look. The full version, with the price of a stale quote, is §27.6.2.

Put the two boxes together. The phantom's daily standard deviation is $\text{DV01}_B \times \sigma\sqrt{t_2 - t_1}$, or about $\$22{,}000 \times 2.4 \approx \$52{,}000$ for one hour on one \$50mm position *(illustrative)*. That is a fake P&L with a daily swing larger than the honest alpha on most single trades, produced by two clocks that disagree by sixty minutes. The snap is the cure: one timestamp for risk and P&L, agreed in advance, with every vendor's mark either taken at that time or adjusted to it. A snap is a treaty between risk and P&L, and like any treaty it matters most to the parties who would otherwise be shooting at each other.

**4:00 to 6:00 p.m., marks.** After the close, the desk marks its positions, reviews the vendor's evaluated prices, and decides which ones to dispute. A mark is a choice inside the bid-ask spread, and the best public record of what happens when the choice drifts is not a textbook but a Senate report. The 2013 staff report on JPMorgan's Chief Investment Office synthetic credit book describes a junior trader marking positions each day, a spreadsheet kept for a week in March 2012 that compared the booked marks with mid-market marks (a reported year-to-date loss of \$161mm against \$593mm at mids), and independent price-testing tolerances that let the investment-grade index mark sit up to 6 bp from the midpoint (U.S. Senate Permanent Subcommittee on Investigations, *JPMorgan Chase Whale Trades*, 15 March 2013, pp. 5 and 112). The lesson Theo takes from it is not a scandal. It is that the mark is a forecast with an author (Law 9), and the 5 p.m. dispute with the pricing vendor is where the desk decides whose forecast to believe.

![Figure 3B.1: The desk's day as a timeline. Each band is a system that fires at a fixed hour (feed diff and security master at 6:45, the explain at 7:15, the risk pack at 7:30, the pre-open calendar at 8:30, the fills, hedge and RFQ loops through the session, the snap at 3:00, marks and disputes from 4:00), with the vendor and venue clocks that feed it drawn underneath: Treasury futures settlement around 3:00 New York, evaluated bond prices mid-to-late afternoon, equity close at 4:00, CDX marks later still. Illustrative schedule.](assets/figures/ch03b_day_timeline.png)

There is one more clock in the day, and it is the one the ex-banker never sees in a model: the hedge's own clock. Chapter 8 argued that a desk should usually *hedge less* than the minimum-variance ratio, because hedges carry basis risk and cost (§8.6). The same logic has a time dimension.

> **Math, Gently.** *The no-trade band.* Rebalance a hedge every time the book's DV01 drifts and you pay the bid-ask spread all day. Never rebalance and the drift turns into variance. Between the two lies a band: do nothing while the mismatch is inside it, trade back to the edge when it leaves. Whalley and Wilmott (1997) showed, for an option hedged with proportional costs, that the optimal band's width grows with the *cube root* of the ratio of cost to risk aversion. Halve your trading cost and the band narrows by only about a fifth ($2^{-1/3} \approx 0.79$), not by half. The desk's translation: a hedge that is rebalanced on every wiggle is being managed by anxiety, not by arithmetic. The full version, with the band built into the limit sheet, is Chapter 8-B.

*Builds on:* §3.3 (markouts), §8.1 and §8.6 (the explain and the hedge matrix), §27.2–§27.4 (feeds, the security master, the order state machine). *Used in:* Chapter 8-B (the limit sheet), Chapter 8-C (the explain's timing and series-roll lines), Chapter 18-B (the RFQ loop), §28.9 (the dashboard).

## 3B.2 The Week

Some questions cannot be answered in a day because a day does not contain enough data. The week is the first clock long enough to say anything about the desk's own behavior, and Friday afternoon is when the desk says it.

**Friday markouts.** Every fill the desk did that week is marked against where the bond traded one, five and twenty days later (§3.3), and the results are cut two ways: by counterparty, which tells the desk who knows more than it does, and by signal, which tells the desk which of its own ideas are paying. Ines calls the Friday review the hand history, and she reads it the way she used to read her own poker hands on the drive home: not "did I win?" but "given what I could see, was the bet right?" Before any markout is read, the market's move is subtracted.

> **Math, Gently.** *Beta: the part of a move that was not about you.* If high yield as a whole falls 1.2 points in a week, a bond that falls 1.3 points did not tell you much about itself. Beta is the number that says how much of the market's move a bond usually carries: a beta of 1.1 means the bond typically moves 1.1 points for every point the index moves. Suppose Theo sold a bond at 95 and it traded at 93.5 five days later. The raw markout is a 1.5-point win for the seller. The index fell 1.2 points, so beta explains $1.1 \times 1.2 = 1.32$ of it, and the idiosyncratic markout is only 0.18 points. Theo did not read the room; he read the weather. The full version is §3.3.3 and §8.1, where this subtraction becomes the desk's motto (Law 1).

**Hit ratios and cover gaps.** The RFQ log gives two more weekly numbers: the share of requests the desk won in each client tier, and the distance between the desk's price and the cover (the second-best price) when it won. A hit ratio that creeps up while cover gaps widen means the desk is paying clients to trade with it, which is fine if intended and a leak if not (Chapter 18-B builds the engine that targets both).

**Model monitoring.** Every production model on the desk carries assertions: inputs inside their ranges, outputs that reconcile, features that are not stale. The weekly review asks which assertions fired, which were snoozed, and which closed themselves. The last category is the dangerous one. Jane Street's production engineers describe building a tool to ask exactly that: "What percentage of alerts are we actually actioning? ... snoozing or close themselves?", because pages that "open and close and you did nothing to resolve them" end up "taking up mental space" (*Signals and Threads*, Ep. 20, Liora Friedberg, 7 October 2024). The credit version is the stale-mark alarm that fires every morning at 6:45 because the vendor is always a little late, until the morning it is late for a reason.

**Monday research.** The week ends on Friday's numbers and restarts on Monday's question, which on a good desk is "what did we learn?" and on a bad one is "what do we think?" The difference is whether anyone can be wrong. A view logged on Monday with a probability and a horizon (§3B.7) can be wrong by Friday. An opinion expressed with conviction in a meeting cannot be wrong ever, which is why it is worth nothing. Market makers say this out loud: Optiver's account of a trader's day ends with "close to an hour digging into our trades: what we did, why we did it ... what we didn't do" (Optiver, recruiting story on a day in the life of a Chicago quant trader intern). The trades a desk passed on are data too (Law 14: censoring is the signal).

*Builds on:* §3.3 (markouts, the hand history), §3.3.3 (stripping beta). *Used in:* Chapter 18-B (hit ratios and cover), §27.8 (alert hygiene), §3B.7 (how you are measured).

## 3B.3 The Month and the Quarter

The longer clocks are quieter, and they are where the big numbers hide.

**Month-end** brings three events. The first is index rebalancing. Bonds that were downgraded, matured or called leave the indices on the last business day, and the funds that track those indices sell them on schedule, whatever the price (§16.2 treats this as a supply process; Law 15). A desk that knows the rebalance list can see a wave of selling coming several days out. The second is the evaluated-price true-up. The fund administrator's official month-end marks replace the desk's own, so every bond the desk marked differently from the vendor produces a gap that must be explained or disputed (Chapter 8-C's dispute process; the three-point true-up on a bond that never traded is its second worked morning). The third is the factor review: loadings re-estimated, covariances refreshed, and the risk numbers of the morning pack quietly changed underneath everyone.

**Twice a year**, on 20 March and 20 September, the credit indices roll. A new CDX or iTraxx series is launched with refreshed constituents, liquidity migrates to it within days, and the old series becomes off-the-run (Chapter 10-B). A hedge that was perfectly liquid on the 19th becomes, on the 21st, the second-most-liquid version of itself, and some pricing feeds keep publishing a mark for the old series long after anyone has traded it. Kaz's remark in the cold open, "it's always late the week of a roll," was a better clue than he meant it to be.

**Eight times a year** the Federal Open Market Committee meets, and the desk's rates hedges earn their keep. **Every quarter** comes earnings season, when, in the words of Man Group's credit team, "a supplier company reporting before a customer company" moves the signal for names that have not reported yet, "multiply that by hundreds of issuers" (Man Institute, "Extra Credit," March 2024). Quarter-end also brings business development company (BDC) marks and the semi-liquid funds' redemption-request prints, which are the best public belief series private credit produces (Chapter 17 and Chapter 17-B).

![Figure 3B.2: The year as four nested clocks. Innermost, the day (feed diff, explain, risk pack, snap, marks); then the week (Friday markouts, model monitoring, Monday research); then the month (index rebalance, evaluated-price true-up, factor review); outermost, the quarter and half-year (earnings season, BDC marks and redemption requests, the 20 March and 20 September index rolls, eight FOMC meetings). Contract clocks (grace periods, consent deadlines, RSA milestones, NDA outside dates) are drawn as issuer-specific arcs that cut across all four rings. Illustrative.](assets/figures/ch03b_year_clocks.png)

*Builds on:* §16.2 (rebalance as supply). *Used in:* Chapter 8-C (true-up, series-roll basis), Chapter 10-B (rolls), Chapter 17-B (quarterly marks and redemption queues).

## 3B.4 Clocks With Contracts Attached

By the end of his second week Theo has noticed something about the calendar. The desk's clocks are generic: every issuer has a month-end, and every hedge has a roll. But the clocks that move single names are specific, written into documents, and almost entirely absent from the desk's models. Nobody had typed them in.

Kaz is the first to ask. "What's a record date? Is that a vinyl thing?"

"It's the day the trustee looks at the register to decide who gets the coupon," Theo says. "If you buy after it, the seller gets paid."

Kaz writes this down. Over the next month Kaz quietly builds the best event-feature table on the floor: every coupon, record date, call date and maturity for nine hundred issuers, with grace periods and notice periods attached. Asked where the grace periods came from, Kaz refuses to say. They came from a new tab in a 13-week cash flow model on a USB stick, which is now the most-used spreadsheet on the desk and the only one with a tab called "Calendar (do not sort)."

Here is the list Theo typed in, and why each item is a clock rather than a fact.

A **grace period** starts when a payment is missed: often 30 days for bond interest, a few business days for loan interest, and none for principal (§12B.5's transition table). A **notice period** starts when a trustee or a group of holders formally notifies the issuer of a covenant default, and the cure period it opens is often sixty days. A **record date** decides who is paid, and a **consent deadline** or **early-tender date** decides who is paid more. A tender offer must stay open at least twenty business days (Exchange Act Rule 14e-1), so its expiration is knowable on the day it launches. **Call dates and make-wholes** (Chapter 4-B) put a ceiling on a bond's price that moves on a schedule. **RSA milestones and joinder deadlines** (§13.5) are dates by which a plan must be filed or a holder must sign. **NDA outside dates and cleansing 8-Ks** (§3.6.3, and §3B.5 below) decide when a restricted name comes back. **Rule 3001(e) transfer notices** give a claim's seller 21 days to object (§25.8). Each one is a date written into a contract, with a consequence attached to the date.

> **Math, Gently.** *A hazard rate is a Poisson process with an appointment book.* A Poisson process counts events that arrive at random, at a steady average rate, with no memory: the chance of an arrival in the next small interval does not depend on how long you have waited. The waiting time to the first arrival is then exponential. If defaults arrive at 4% a year, the chance of surviving one year is $e^{-0.04} \approx 96.1\%$, and the average wait is $1/0.04 = 25$ years. The default intensity $\lambda_t$ (the hazard rate) is that rate, allowed to change over time. Credit's twist is that the rate is not steady: it jumps on dates somebody wrote down. A grace period that is running multiplies the near-term chance of default, and a refinancing that has closed divides it. The full version is §5.1.5 (where the 13-week model becomes a hazard rate) and Chapter 6.

The appointment book becomes mathematics in two lines. For contract event $k$ due at date $T_k$, define a window indicator and a countdown,

$$
x_k(t) = \mathbf{1}\{0 \le T_k - t \le w\}, \qquad d_k(t) = \max(T_k - t,\, 0),
$$

so that $x_k$ switches on $w$ business days before the event and $d_k$ counts down to it. The desk's physical-measure intensity then multiplies a baseline by a factor for each window that is open:

$$
\lambda^{\mathbb{P}}(t) = \lambda_0 \exp\!\big(\beta^{\top} x(t)\big).
$$

The exponential keeps the intensity positive and makes each coefficient a multiplier: with $\beta_{\text{grace}} = 1.2$, an open grace window multiplies the baseline by $e^{1.2} \approx 3.3$ *(illustrative)*. These are exactly the event-calendar features that §18.6.2 feeds into the market maker's jump-to-default charge, and Halvorsen's grace-period clock from §12B.9 is one such $x_k$. The banker's contribution is not the formula. It is the list of $T_k$, which no vendor sells complete and no model invents.

That is why the Edge Ledger of §3.5 needs two more rows and one more column. The rows are the skills the ledger had missed because they are not about any single credit. The column is the one a new hire's manager actually cares about.

| RSSG skill | Codable feature | Data source | Refresh | Decay horizon | Who else has it | Time to first compute on the new desk |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Model audit (asking "what does the document say?" of every number) | Assertion coverage; reconciled-input share; open-unexplained count | The desk's own logs and explains | Daily | Never | Anyone who bothers | Week 1 |
| Process clocks | `days_to_next_contract_event`, window indicators $x_k(t)$ by event type | Indentures, credit agreements, 8-Ks, dockets, exchange-offer documents | On each filing | Days | Distressed funds, partially; almost no systematic models | Weeks 3–6 |
| 13-week cash flow model (from §3.5) | `liquidity_runway_weeks` | 10-Q/10-K, 8-K, compliance certificates | Quarterly and on events | Months | Rating agencies, equity analysts | Months 2–3 |

The last column is honest about the order in which things happen. Model audit can start on day one, because it needs nothing but suspicion. Process clocks take a few weeks because the documents have to be found and read. The 13-week model, the skill Theo is proudest of, takes longest, because it needs data plumbing that does not exist yet.

### Case Study: Saks Global, Seen From the Calendar

The Saks Global liability-management fight has its dated Docket Diary in Chapter 13-B. Here we use only what the calendar would have seen, and the lesson is in the first date. All facts are from the dossier `case_lmt_autopsies_us_2020_2026` §8 and its sources.

On 23 December 2024 Saks Global completed its purchase of Neiman Marcus at a \$2.7bn enterprise value, funded in part by \$2.2bn of 11.000% senior secured notes due 2029, a \$1.8bn ABL, \$275mm of seller financing and about \$1.5bn of equity. To a security master this arrives as a fresh CUSIP with a fresh label: *new issue*. A new issue is the kind of line a first-year analyst assumes is safe, because nothing can have gone wrong yet. By 16 May 2025, under five months later, the notes were quoted at 47.5 (Debtwire, as cited in the dossier), and a holder group of about 51% was weighing new financing that could leapfrog the rest.

The calendar had something to say before the price did. The first coupon was due at the end of June, and its size, about \$121mm, is exactly $2{,}200 \times 11\% / 2$: a number the event table computes on the day of issue. A coupon that large, against a retailer's liquidity, is a contract clock with a dollar figure attached, and it is the kind of input a liquidity-runway feature would have flashed (§3.5). The exchange offer launched on 21 July 2025 and settled early on 8 August, with about 98% tendered. Every one of its dates, from early tender to expiration, was knowable on the first morning (Chapter 13-B has the structure).

The second year ran on the same kind of clocks. In December 2025 about \$126mm of interest went unpaid, and the ABL's minimum-availability covenant stepped up from \$200mm to \$375mm on 1 December and to \$500mm on 16 December: two contract dates, written in advance, each tightening the runway by a known amount. S&P moved the company to SD on 7 January 2026, and the Chapter 11 petition followed on 13 January. The plan was confirmed on 5 June, and the company emerged on 26 June 2026 as Exemplar Luxury Group.

What would a first-year analyst have typed? Not a forecast of the LME, which needed judgment and documents (Chapter 13). But a row for every dated obligation, from the June 2025 coupon to each December 2025 covenant step, with $x_k(t)$ switching on as each approached. One caution belongs in the row itself: the exact payment dates and grace terms are in the indentures, not the press, and a grace-period feature built from a news summary is a training label with a typo in it. Check the document before the date becomes a feature.

Incora's 28 March 2022 transaction, also told in Chapter 13-B, adds one more feature to the table: four steps in one day, so "the amendment and the issuance share a date" is itself an event type.

*Builds on:* §3.5 (the Edge Ledger), §5.1.5 and §18.6.2 (event features in $\lambda^{\mathbb{P}}$), §12B.5 and §12B.9 (the grace-period clock). *Used in:* §3B.11 (`desk_calendar.py`), Chapter 13 (the runway input to the Priming Risk Score), Chapter 13-B (the dated Saks and Incora diaries).

## 3B.5 The Wall, as a Scene

*A Thursday in March. 10:02 a.m.*

The call comes to Mags, not to Theo. Brambleworth Packaging's financial adviser wants to talk to a handful of holders of the 9.25% senior secured notes about "a potential refinancing transaction." Talking means signing a confidentiality agreement and receiving the company's projections. Mags has done this perhaps three hundred times. "I have been restricted," she says, "on names that no longer exist."

The desk has a decision to make, and it is not Mags's alone. The information barrier on this floor is drawn around the whole credit desk, so if anyone on it goes over the wall, the desk stops quoting Brambleworth. The PM agrees, because the fund holds enough of the notes to care how the refinancing is shaped. Compliance designates one person to receive the information. It is Theo, because he has read four hundred of these agreements, and because his RSSG years make him, in the compliance officer's words, "the only person here who already knows what not to say."

At 10:14 the name goes on the restricted list. At 10:15 the auto-quoter stops quoting it: every Brambleworth RFQ now gets an automatic decline, because the restricted-list check sits in the order gateway, ahead of the pricing model. The desk's market in a bond it has made markets in for a year simply ends. Three clients notice by lunchtime.

Theo learns the rest in order. The first lesson is that **private side and public side** are a property of people and information, not of instruments. Lenders in a syndicated loan receive private information by default, so a holder who wants to keep trading makes a **public-only election** on the loan platform and receives only what has been disclosed. The second is that a **big-boy letter**, the acknowledgment and waiver a restricted holder can ask a counterparty to sign before trading, settles the question between the two parties to the trade. It does not bind a regulator, who is not a party to it, and it does not turn a restricted name back into a quotable one. The third is the **outside date**. Brambleworth's agreement says that the company will publicly disclose the material information it shared, or confirm that talks have ended, by a date thirty days out. Restriction has an expiry date written into the contract.

> **[SOURCE EXTRACTION]** *Moyer_Distressed_Debt_Analysis p.80:* "once members receive nonpublic information, they will become restricted and cannot become unrestricted until the information becomes public, usually through the filing of a Form 8-K, 10-Q, or 10-K, or the information becomes nonmaterial."
>
> **Annotation.** Moyer is writing about bondholder committees in the mid-2000s, and the sentence is a trading rule in disguise. If restriction ends when the information becomes public, then the end of restriction is an event with a date, and a desk can forecast it. The modern practice adds the contract term Moyer only implies: an NDA outside date that obliges the company to cleanse by a fixed day whether or not a deal is reached. The departure for a systematic desk is that the wall is not only a constraint on Theo. It is also a feature of every *other* counterparty (§3.6.3): a large holder who goes silent has probably signed one too.

> **Math, Gently.** *Restriction is an interval, and an interval has an expected length.* The name is restricted from the wall-cross until the earlier of two dates: the day a deal is announced and cleansed, or the outside date $H$. If you think a deal arrives at a random time with an exponential wait of average 20 days (rate $\mu = 1/20$ per day), the expected restricted period is $(1 - e^{-\mu H})/\mu$. With $H = 30$ days that is $(1 - e^{-1.5}) \times 20 \approx 15.5$ days, about half the outside date. The exponential's lack of memory makes the arithmetic short. Real negotiations have memory (they speed up near deadlines), so treat this as a first guess the desk should replace with its own history of wall-crosses. The full version, with deadlines that bunch events, is §12B.7's clock algebra.

On day nineteen the talks produce a deal. On day twenty, at 7:05 a.m., the cleansing 8-K is filed under Item 7.01, Regulation FD Disclosure, attaching the company's term sheet, the holders' counterproposal and the projections Theo has been staring at for three weeks. At 7:40 compliance lifts the restriction. At 7:41 the auto-quoter's first Brambleworth quote is wider than usual, because the desk's information about the name has just been made identical to everybody else's, and the first hour after a cleansing is when the people who were *not* restricted read the projections for the first time.

The Ad Hoc Group, which has formed in the corner as usual, files a Rule 2019 statement disclosing its holdings and, for completeness, the desk's seating chart. (Cooperation agreements signed in this book so far: still 1. Theo was asked to sign one and did not.)

> **View From Another Seat.** The same phone call means three different things in three seats. A *distressed or opportunistic credit fund* usually wants to be restricted: the projections and the seat at the table are worth more to it than three weeks of liquidity, and it plans its position before it crosses. A *systematic fund* usually declines every wall-cross, because one restricted name is a hole in a book of eight hundred and its edge is breadth, not access; it sees the same event only as a counterparty that has suddenly stopped trading. A *CLO manager* holding the loan is a lender with information rights it may not want, so it often elects public-only status and votes on amendments without the private data (Moyer p.81 describes the public-side lender's disadvantage when asked to vote). None of the three is wrong. They have priced liquidity, information and influence differently.

*Builds on:* §3.6.3 (the wall's mechanics and the Sound Point and Marathon orders), §12B.7 (clocks). *Used in:* §3B.6 (mistake 11), §3B.11 (`in_cleansing_window`), Chapter 25 (8-K monitoring).

## 3B.6 The Twelve Mistakes

Theo makes most of these himself in his first year. The others he watches colleagues make, which is cheaper. They look like twelve different errors, and they are one: in each, a banker's object is mistaken for a desk's object that has the same name. A composite is mistaken for a price, face for jump-to-default exposure, a risk-neutral probability for a real one, a memo for a logged view. Appendix A's glossary (§A.9) is the dictionary between the two languages, and this section is the list of words that look identical in both.

**1. The composite treated as a price.** A salesperson asks Theo where Halvorsen's 7.25s are. He reads the vendor composite off the screen: 92. The desk's bid is 89½, and the client, who has been told 92, is now annoyed with the desk rather than with the bond. A composite is a weighted average of recent quotes and trades, some of them stale, some of them indications nobody would honor. It is a prior about where the bond might trade, not a price at which anybody will (§20.2 calls the ETF version "NAV is an opinion"; Chapter 17-B shows the private-credit version, where the mark is a moving average of the truth). In a banker's comps page "price" means the last number anyone wrote down. On a desk it means a number someone will trade at, now, in size.

**2. Hedged to face, not to jump-to-default.** Theo buys \$10mm of protection against \$10mm of Halvorsen bonds at 88, because ten matches ten.

> **Math, Gently.** *JTD: hedge what you would lose on the day.* If Halvorsen defaults tomorrow and recovers 40, the bond falls from 88 to 40, a loss of 48 points. The swap pays par minus recovery, 60 points per unit of notional. To be flat on the day of default you need protection of $48/60 = 0.8$ per unit of bond face, so \$8mm, not \$10mm: $N^{\text{JTD}} = (P - R)/(1 - R)$. Buying \$10mm leaves Theo with an extra \$2mm bet that the company defaults. It is not wrong to hold that bet, only wrong to hold it without knowing. The full version, including what happens when $R$ itself is uncertain, is §24.3.

**3. The long-protection sign.** "We're long the Brambleworth CDS," Theo tells the risk manager, meaning the desk owns protection. The risk system's convention is that *long* means long credit risk, which is what a protection *seller* has. For a day the risk pack shows the desk's hedge with the wrong sign, and the DTS cell looks twice as full as it is. The desk now says "bought protection, short risk" in full, every time, like a pilot reading back a clearance (the premium and protection legs, and who pays the upfront, are in §6.8).

**4. A spread parsed as a price.** On a manual fallback ticket during a platform outage, Theo types "105" into a field he believes holds a spread over the ten-year Treasury. It holds a price. A bid of 105 points for a bond trading near 95 is a ten-point gift, and it is stopped only by the price collar in the gateway's first tier of checks (§27.4 calls this the classic credit gateway bug, "a fat finger made by a parser"). The lesson is Law 11: a number without its unit is not a number.

**5. Researching one name while the book needs breadth.** Theo spends forty hours on Brambleworth's fulcrum, and the analysis is excellent. The PM's question is how many other names got no hours that week.

> **Math, Gently.** *The fundamental law, in one line.* A strategy's information ratio is roughly its skill per bet times the square root of the number of independent bets: $\text{IR} \approx \text{IC}\sqrt{\text{BR}}$. One superb bet with an information coefficient of 0.3 gives $0.3 \times \sqrt{1} = 0.3$. Two hundred modest bets at 0.05 give $0.05 \times \sqrt{200} \approx 0.71$, more than twice as much. The catch is the word *independent*: bonds of the same issuer, or the same sector in a sell-off, are not separate bets (Law 2). The full version, with effective breadth when issuers cluster, is §28.2.

The banker's instinct, that depth is the job, is right for a single engagement and wrong for a book. The desk needs Theo's depth on the names where depth changes the answer, and breadth everywhere else.

**6. Exercising the PM option in a drawdown.** Theo's Brambleworth view is down two points, and he asks to double the position "while it's cheap." A portfolio manager paid a share of positive P&L holds a call option on the book, and a call is worth more when volatility is higher, whether or not the manager is skilled (§28.6). Doubling a losing position to get back to even is buying volatility with somebody else's capital. Mags has seen this before: "The bond doesn't know you own it, and it certainly doesn't know what you paid." The desk's answer is the two-threshold drawdown rule of §28.6, which exists to take the decision away from the person least able to make it.

**7. Risk-neutral default probabilities used to size a real bet.** Theo backs a default probability out of a spread and plugs it into a Kelly sizing sheet. The sheet tells him to hold nothing.

> **Math, Gently.** *Two measures: the world's odds and the market's prices.* A spread pays for expected default losses *and* for bearing the risk of them. Divide a 500 bp spread by a loss given default of 60% and you get $\lambda^{\mathbb{Q}} \approx 0.05/0.6 \approx 8.3\%$ a year. That is the *risk-neutral* intensity, the default rate that would make the bond fairly priced to someone who demanded no reward for risk. The *physical* rate, how often such bonds actually default, might be 3% *(illustrative)*. Use $\lambda^{\mathbb{Q}}$ as if it were $\lambda^{\mathbb{P}}$ and the expected excess return $s - \lambda L$ is zero by construction, so every bond looks like a fair coin and Kelly sizes it at zero. The model says credit pays nothing, and it is wrong by exactly the risk premium the desk exists to earn. The full version is Chapter 6-B, and the rule is Law 4: say which measure you are in.

**8. Retuning in a drawdown.** Kaz's momentum sleeve is down for three weeks, and Theo suggests shortening its lookback from sixty days to forty. Over the last month the forty-day version would have done better, which is exactly why it proves nothing: a parameter chosen after watching the outcome has been fitted to the outcome. Each retune is another trial, and trials have to be counted and deflated (Law 12; §7.8). Chapter 27's deployment discipline (§27.8) puts every change through the same ladder (replay, then paper, then small live size) for a reason that is more psychological than technical. The middle of a drawdown is the worst possible time to learn something about a model, because it is the time you most want to.

**9. Raw markouts, beta still in.** In a week when high yield sold off two points, Theo flags a client as toxic: everything it sold the desk went down afterwards. Everything *everyone* sold went down afterwards. Strip the index move with the bond's beta (§3B.2's box) and the client's idiosyncratic markout is indistinguishable from zero (§3.3.3). Accusing a counterparty of knowing more than you, when what it knew was the weather, is the fastest way to lose a client who was paying for the desk's coffee.

**10. Trusting anything called "adjusted."** Theo's old models ran on adjusted EBITDA, and he still says the phrase without flinching. Mags flinches for him. In Chapter 25's arithmetic, an add-back dollar of EBITDA can buy several dollars of debt capacity once the leverage multiple is applied to it (§25.3). On the desk the word moves from the income statement to the performance report: "adjusted Sharpe," "adjusted markout," "adjusted spread." The question is the same in both places: what was adjusted, by whom, against what benchmark, and was the adjustment decided before or after the result was known?

**11. The wall, after years on the private side.** Theo's first error here is the opposite of everyone else's. A public 8-K about a former client arrives, and he will not trade on it, because he "saw something like it" at PJT. Public is public: once information is cleansed, it is the same for everyone, and refusing to use it is a cost, not a virtue. His real exposure is elsewhere. Compliance has his list of prior engagements and keeps those names on his *personal* restricted list for a period, because a banker's memory is not cleansed by a change of employer. The rule he learns in §3B.5 applies to himself as well: restriction is an interval with a start date, an end date and a reason, not a permanent state of mind.

**12. The forty-page memo where the desk wanted five lines.** Theo writes forty pages on Brambleworth's refinancing options. They are very good pages. The PM reads the first one and asks, "So what's the trade?" A desk wants an Edge Ledger entry (§3.5): the view, with a probability; the horizon; the size and the hedge; the condition that would make the view wrong; and the date on which it will be checked. Five lines. The memo is still useful, as the appendix that justifies line one. Mistake twelve is the hinge to the next section, because what gets logged in five lines is what can be measured, and what stays in a forty-page memo cannot.

*Builds on:* §3.3, §3.5, §6.8, §7.8, §20.2, §24.3, §25.3, §27.4, §28.2, §28.6, Chapter 6-B. *Used in:* App A §A.9 (the dictionary), App E (Laws 1, 2, 4, 11, 12).

## 3B.7 How You Will Be Measured

Theo's first review is in December, three months in. He has a P&L number, and Ines tells him to ignore it.

"Forty bets," she says. "You won twenty-two. That's 55%. Tell me how sure you are that you're better than a coin."

> **Math, Gently.** *How noisy is a hit rate?* Each view is a coin toss with an unknown bias $p$, the chance it is right. After $n$ independent views the observed share right, $\hat p$, wanders around $p$ with a standard error of
>
> $$
> \text{SE}(\hat p) = \sqrt{\frac{p(1-p)}{n}}.
> $$
>
> At $p = 0.55$ and $n = 40$, that is $\sqrt{0.2475/40} \approx 0.079$, about 7.9 percentage points. The edge, five points over a coin, sits inside one standard error. At $n = 400$ the standard error falls to about 2.5 points, and only then is the edge two standard errors from zero. Precision improves with the square root of the sample, so to halve the noise you need four times the views. The full version, for a PM's year of daily bets, is equation (28.6) in §28.2, and the version that also counts how many strategies you tried is §7.8.

So a first-year analyst cannot be measured on outcomes, because outcomes cannot measure anything yet. "The first year you are playing for information," Ines says. "Chips come later, and only if the hand history says so." What gets measured instead is what can be measured on forty views.

![Figure 3B.3: The standard error of a measured hit rate against the number of logged views, for a true hit rate of 55%. The shaded band is plus and minus two standard errors; the horizontal line marks the five-point edge over a coin. At 40 views the band spans roughly 39% to 71%; it first excludes 50% at about 400 views. Logging every view, including the ones not traded, moves an analyst along the horizontal axis faster than trading does.](assets/figures/ch03b_hit_rate_se.png)

**Calibration.** Every logged view carries a stated probability. Group the views by what was stated and compare with what happened: if the 70% calls come true about 70% of the time, the analyst is calibrated.

> **Math, Gently.** *The Brier score: a ruler for probabilities.* For views with stated probabilities $q_i$ and outcomes $y_i$ (1 if right, 0 if wrong), the Brier score is $\frac{1}{n}\sum_i (q_i - y_i)^2$, lower being better. Theo logs ten views at 70%, and six come true. Each right call scores $(0.7 - 1)^2 = 0.09$ and each wrong one $(0.7 - 0)^2 = 0.49$, so his score is $(6 \times 0.09 + 4 \times 0.49)/10 = 0.25$, exactly what an analyst who said "50%" every time would score. Had he said 60% about the same ten views, he would have scored 0.24, better than the coin. Same views, same outcomes, and an honest probability turns a tie into a win. The score splits into *calibration* (are your 70s really 70s?) and *resolution* (do your probabilities move away from the base rate when they should?); Chapter 7-B owns the decomposition.

**Correlation with the price factors.** If Theo's calls go long credit whenever spreads have been tightening, his hit rate is the market's momentum factor wearing his name. The review regresses his views on the desk's factor returns and asks what is left. §28.8 shows why the residual is the whole point: an analyst's value to a quant book is mostly the *low correlation* of his signal with the price factors the book already has, because two signals of equal skill add far more when they disagree. If your alpha is beta, say so before the review does.

**The Edge Ledger as a daily artifact.** Every view goes in on the day it is formed, with its five lines, and markouts at one, five and twenty days are filled in automatically, beta stripped. The ledger is the analyst's hand history. Over a year it becomes a few hundred rows, which is the first sample large enough to say anything.

> **View From Another Seat.** A multi-strategy pod measures its people faster and harder than Theo's desk does, because the platform's risk function sees every book every day. Giuseppe Paleologo, who has run risk at multi-strategy platforms, described on *Odd Lots* (20 May 2024; machine transcript, CHECK before print) platforms that "observe the performance of PMs ... from a very close distance," books that are "purely market neutral and factor neutral," and a bought factor model used as a real-time "x-ray." A pod analyst's alpha is judged net of factors from the first week, and capital moves on drawdowns well before a hit rate could be measured (§28.6). The ex-banker who lands in a pod should expect the first-year measure to be risk discipline, not P&L.

*Builds on:* §3.5, §28.2 (equation 28.6), §28.8. *Used in:* Chapter 7-B (calibration), §28.9 (the dashboard), App E (Law 12).

## 3B.8 The First Ninety Days on the Seat

The pre-seat plan, the ninety days *before* day one, is in `00_02`. This is the ninety days after, and it is shorter than Theo expected, because the desk does not want a plan from him. It wants evidence that he can be given a clock.

In **days 1–30** he reads: the feed diff, the security master, the explain and the risk pack, every morning, until he can predict the unexplained line before he sees it. In **days 31–60** he owns something small and real: one clock (the contract-event features of §3B.4, for one sector) and one evaluated-price dispute, from first email to resolution. In **days 61–90** he ships one feature through the first rung of the deployment ladder (replay, then paper, §27.8) and presents one hand history at the Friday review, with the beta stripped. None of it is a trade idea. All of it is the work that earns the right to have one.

## 3B.9 Quant-Shop Life, Two Vignettes

*Both vignettes are fictional composites. The shops, people and numbers are invented; the mechanics are the ones described in this chapter's sources.*

**The reconciliation that does not tie** *(a systematic asset manager, a Wednesday)*. At 9:10 the custodian's cash report shows \$412,500 arriving in the fund's account against a bond position that has not changed: no trade, no coupon date, no call. The reconciliation analyst opens a break ticket and the morning explain shows the receipt as unexplained income, which nobody believes. By 11:00 three people have ruled out a misbooked trade, a coupon paid early and another fund's cash. By 2:30 the corporate-actions team finds it: a consent fee, \$2.50 per \$1,000 on \$165mm face, for a consent solicitation the portfolio manager had answered through the custodian three weeks earlier, entered nowhere the explain could see it. The fee was real. The process that should have expected it did not exist. Operations are a position, and the largest reconciliation break of the modern era makes the point at scale: on 11 August 2020 Citibank, as agent, mistakenly sent about \$894mm of principal to Revlon's 2016 term lenders (canonical home Chapter 27 §27.7; `case_lmt_autopsies_us_2020_2026` §1). The analyst's fix is a row in the event table: `consent_fee_expected`, keyed to the instrument, dated to the settlement of the solicitation.

**The model review** *(a bank credit-trading desk, a Thursday)*. The risk committee has one question for the desk's quant: why did the BB DTS cell rise 11% overnight when nothing traded? The quant has spent the morning building the answer as a reconciliation of the cell: trades (none), price moves (small), model changes (none), and migrations. The migration is the whole story. One agency downgraded an issuer with forty bonds outstanding, the index rating rule (the middle of the agencies' ratings) moved the issuer from BBB to BB, and forty bonds walked from one limit cell to another with their DTS unchanged. "Will it move back?" asks the committee. The quant says that depends on the other two agencies, both of which have the issuer on watch, and adds the watch dates to the calendar. The meeting takes twelve minutes. Preparing for it took four hours, which is the usual ratio. The limit sheet is a function of a label (Law 13: the label is the model).

## 3B.10 When to Apply It, and When It Breaks

The calendar is a model too, and it fails in the places models usually fail: where its inputs are wrong and nobody checks.

It breaks on **holidays that differ by venue**. The bond market keeps SIFMA's calendar, not the stock exchange's or the federal government's: SIFMA recommends a full close on Columbus Day and Veterans Day while the NYSE is open (App D), so a T+1 bond trade done on the Friday before Columbus Day settles on Tuesday while a T+1 ETF trade settles on Monday. ROBO was wrong to call 12 October a credit event, and right that it mattered. It breaks on **settlement cycles**: T+1 for U.S. corporate bonds; T+7 for par loans, which is the day delayed compensation starts rather than the day cash moves; and T+20 for distressed loans, which can take months (App D). It breaks on **corporate actions nobody entered**, like the consent fee above. And it breaks on the day a bond stops accruing: once a bond trades flat, without accrued interest, every carry line in the explain that assumed a coupon is wrong by the coupon.

U.S. securities moved from T+2 to T+1 settlement on 28 May 2024 (App D), the Tuesday after Memorial Day. The calendar arithmetic is a small trap of its own: a trade done on Friday 24 May under T+2 and a trade done on Tuesday 28 May under T+1 both settled on Wednesday 29 May (computed from the holiday calendar), so one day carried two days of settlements. Every calendar in the shop that hard-coded "T+2" was wrong by a day for every trade after that, and the ones that hard-coded the transition were wrong for the Friday.

What does a seasoned practitioner check first? Not the formula. The provenance of each date: which document it came from, when the desk learned it, and whether it has moved since. A consent deadline extended three times is three different features, and a backtest that uses the last version on every day is reading tomorrow's newspaper (§27.3's bitemporal master).

> **Trend Watch.** *When the tape's denominator moves (2026–2027).* On 24 July 2026 the SEC approved FINRA's affiliate-principal transaction indicator (Release No. 34-105991). TRACE now suppresses the inter-affiliate leg of a trade between affiliated members so that only the trade with the outside counterparty is disseminated. Use is voluntary from 31 August 2026 and mandatory from 2 August 2027 (FINRA Regulatory Notice 26-16, 26 August 2026). FINRA's economic baseline put such transactions at up to about 5.7% of 2025 corporate, agency, ELN and foreign-sovereign transactions, an upper bound counted in trades, not dollars (SR-FINRA-2026-009, pp. 19–21). The first month showed up in public data at once: Tradeweb's September 2026 report footnoted that the rule "lowered reported U.S. High Grade TRACE volumes" and that prior periods were not restated (sources in `trend_part_v_market_structure_2026`). For the calendar this is two new rows, 31 August 2026 and 2 August 2027, and a structural-break dummy in every feature that counts prints: volumes, participation rates, platform shares.

*Builds on:* App D (settlement and holidays), §27.3 (the bitemporal master). *Used in:* Chapter 22 (reporting rules), App C (the dated row table).

## 3B.11 The Engine: `desk_calendar.py`

### Specification for AI Implementation

**The Spec You Hand the Robot.** *Vague version:* "build me a calendar." *What ROBO built:* every U.S. federal holiday, with Columbus Day flagged as a credit event. Asked the next week to "remind me before anything important," it paged Theo at 3:04 a.m. about a Treasury auction scheduled for 1:00 p.m. The auction was important, and 3:04 a.m. was before it. ROBO implemented exactly what was asked, which is the problem with asking vaguely.

*The problem it solves, at this point in the story.* By the end of his first quarter Theo has a tab in a spreadsheet that the whole desk uses and nobody can audit: contract dates typed by hand, holiday rules remembered rather than loaded, and a consent deadline that has been overwritten three times so that nobody can say what the desk believed on any given day. The module replaces the tab with something a backtest can trust. It has to answer three questions for any instrument on any date: what contract events are coming, and how many business days away are they on the right calendar; is the desk in a window that should change how it quotes or hedges (a contract window, a cleansing window, a roll week); and how does a view get logged so that it can be scored later.

*What it computes, and why it is built this way.* Four pieces. First, **venue calendars**: business-day arithmetic on a named holiday table, SIFMA for bonds and NYSE for ETF shares, so that settlement dates and countdowns are computed where the instrument actually settles. The holiday sets in the listing are illustrative subsets for 2026; production loads the published tables. Second, **contract events as versioned rows**. Every event carries a logical `event_id`, the instrument's surrogate key (never a CUSIP, because an A/B exchange changes the CUSIP but not the instrument), the event date, and `known_at`, the date the desk learned that version. An extension is a new row, not an edit. The `as_of` read returns, for each logical event, the latest version known on a date, which is the bitemporal rule of §27.3 applied to a calendar. Third, **features**: `days_to_next_contract_event`, a window indicator that is the $x_k(t)$ of §3B.4, `in_cleansing_window` and `in_roll_week`. Fourth, **the Edge Ledger schema** with the two scoring functions of §3B.7, the hit rate with its standard error and the Brier score.

*Inputs and outputs.* Inputs are a list of `ContractEvent` rows (from indentures, credit agreements, 8-Ks, exchange-offer documents and dockets, each with its `source`), a CUSIP-to-instrument crosswalk, the holiday tables and a settlement table by instrument class. Outputs are settlement dates, grace-period end dates (both the raw date and the rolled-forward one, because whether a weekend end rolls is a question for the indenture, not the code), a feature dictionary per instrument and date, and ledger entries with their scores.

*When to use it, and when not.* Use it to drive the pre-open calendar, to feed the event features into $\lambda^{\mathbb{P}}$ (§18.6.2), and to schedule when a restricted name comes back. Do not use `in_cleansing_window` as an alpha feature on a name the desk is restricted on: it exists so the quoting engine knows when to return, and while the wall is up the desk may not trade the name at all (§3B.5). Do not use it as a legal calendar either. It computes dates from the terms it is given, and the terms come from documents a person has read.

*The edge case that bites.* The moving deadline. Halvorsen's consent deadline in the tests is extended three times, and a naive table that stores only the latest date tells a backtest on 13 October that the deadline is 5 November, three weeks after the desk could have known it. The `as_of` read is the guard, and the tests check it on two dates. The second edge case is the weekend: Halvorsen's thirty-day grace period from Friday 13 November 2026 ends on Sunday 13 December, and the function returns both that date and Monday the 14th so the user must choose, with the indenture open.

*Tests.* Columbus Day settlement for a bond and an ETF; the \$18mm Halvorsen coupon, the Sunday grace end and day 28 of §12B.9; the A/B exchange crosswalk; the moving consent deadline read on two dates; the September 2026 roll falling on a Sunday; and the measurement numbers of §3B.7 (55% on 40 views with a standard error near 7.9 points, a Brier score of 0.25 and 0.24, and a seeded synthetic year of 400 views).

<!-- EXPLAINED -->
```python
# desk_calendar.py (Chapter 3-B): venue calendars, versioned contract clocks, event features, Edge Ledger.
# Dates are datetime.date. Windows and countdowns are business days on the named venue calendar.
# Holiday sets are illustrative 2026 subsets; load the published SIFMA and NYSE tables in production.
import math
import random
from dataclasses import dataclass, field
from datetime import date, timedelta
from typing import Optional

random.seed(2026)  # only the synthetic ledger in the tests uses randomness

HOLIDAYS = {
    # SIFMA recommends full closes on Columbus Day and Veterans Day while the NYSE is open (App D).
    "SIFMA": {date(2026, 9, 7), date(2026, 10, 12), date(2026, 11, 11),
              date(2026, 11, 26), date(2026, 12, 25)},
    "NYSE": {date(2026, 4, 3), date(2026, 9, 7), date(2026, 11, 26), date(2026, 12, 25)},
}
SETTLEMENT = {  # class -> (calendar, business-day offset); loan offsets are targets, not cash dates (App D)
    "corp_bond": ("SIFMA", 1), "etf": ("NYSE", 1), "par_loan": ("SIFMA", 7), "distressed_loan": ("SIFMA", 20),
}
CONTRACT_KINDS = {"coupon", "record", "grace_end", "notice_cure_end", "consent_deadline", "early_tender",
                  "call", "maturity", "rsa_milestone", "nda_outside", "claim_transfer_objection"}


def is_business_day(d, cal):
    return d.weekday() < 5 and d not in HOLIDAYS[cal]


def roll_forward(d, cal):
    """Following convention: the first business day on or after d."""
    while not is_business_day(d, cal):
        d += timedelta(days=1)
    return d


def add_business_days(d, n, cal):
    step, k = (1 if n >= 0 else -1), 0
    while k < abs(n):
        d += timedelta(days=step)
        if is_business_day(d, cal):
            k += 1
    return d


def business_days_between(a, b, cal):
    """Business days in (a, b]; negative when b is before a."""
    if b < a:
        return -business_days_between(b, a, cal)
    n, d = 0, a
    while d < b:
        d += timedelta(days=1)
        n += int(is_business_day(d, cal))
    return n


def settle_date(trade_date, instrument_class):
    cal, k = SETTLEMENT[instrument_class]
    return add_business_days(trade_date, k, cal)


def grace_end(missed_payment_date, days=30, basis="calendar", cal="SIFMA"):
    """Last day of a grace period, raw and rolled forward. Which one applies is in the indenture."""
    if basis == "business":
        end = add_business_days(missed_payment_date, days, cal)
        return end, end
    end = missed_payment_date + timedelta(days=days)
    return end, roll_forward(end, cal)


def index_roll_dates(year, cal="SIFMA"):
    """CDX/iTraxx roll on 20 March and 20 September, moved to the next business day (proxy calendar)."""
    return [roll_forward(date(year, 3, 20), cal), roll_forward(date(year, 9, 20), cal)]


@dataclass(frozen=True)
class ContractEvent:
    event_id: str      # one logical event across all its versions, e.g. 'HALV-consent'
    instrument: str    # surrogate key, never a CUSIP: an exchange changes CUSIPs, not instruments
    kind: str
    event_date: date
    known_at: date     # when the desk learned this version of the date
    source: str        # 'indenture', '8-K', 'docket', 'vendor', 'desk'


def as_of(events, t):
    """Bitemporal read: the latest version of each logical event known on or before t."""
    best = {}
    for e in events:
        if e.known_at <= t and (e.event_id not in best or e.known_at > best[e.event_id].known_at):
            best[e.event_id] = e
    return list(best.values())


CROSSWALK = {}  # cusip -> instrument surrogate key


def instrument_of(cusip):
    return CROSSWALK[cusip]


def features(events, instrument, t, cal="SIFMA", window=10):
    live = [e for e in as_of(events, t) if e.instrument == instrument and e.event_date >= t]
    contract = [business_days_between(t, e.event_date, cal) for e in live if e.kind in CONTRACT_KINDS]
    nda = [business_days_between(t, e.event_date, cal) for e in live if e.kind == "nda_outside"]
    since_roll = [business_days_between(r, t, cal) for r in index_roll_dates(t.year, cal)]
    return {
        "days_to_next_contract_event": min(contract) if contract else None,
        "in_contract_window": int(bool(contract) and min(contract) <= window),
        "in_cleansing_window": int(bool(nda) and min(nda) <= window),  # scheduling input only (3B.5)
        "in_roll_week": int(any(0 <= g < 5 for g in since_roll)),
    }


@dataclass
class LedgerEntry:
    view_id: str
    logged_at: date
    instrument: str
    direction: int          # +1 long credit risk, -1 short credit risk ("bought protection" is -1)
    prob: float             # stated probability that the view is right at the horizon
    horizon_bd: int
    size_and_hedge: str
    kill_condition: str
    decay_class: str        # 'days', 'weeks', 'months', 'never'
    ido_markout_bp: dict = field(default_factory=dict)  # {1: x, 5: y, 20: z}, beta stripped, filled later
    outcome: Optional[int] = None                        # 1 right, 0 wrong, None while open


def hit_rate_se(outcomes):
    n = len(outcomes)
    p = sum(outcomes) / n
    return p, math.sqrt(p * (1 - p) / n)


def brier(probs, outcomes):
    return sum((q - y) ** 2 for q, y in zip(probs, outcomes)) / len(probs)


if __name__ == "__main__":
    # 1. Columbus Day: a T+1 bond trade on Friday 9 Oct 2026 settles Tuesday; a T+1 ETF trade settles Monday.
    assert settle_date(date(2026, 10, 9), "corp_bond") == date(2026, 10, 13)
    assert settle_date(date(2026, 10, 9), "etf") == date(2026, 10, 12)

    # 2. Halvorsen 6s: an $18mm coupon (600 x 6% / 2) missed on Friday 13 Nov 2026 (illustrative date).
    assert abs(600 * 0.06 / 2 - 18.0) < 1e-12
    end, rolled = grace_end(date(2026, 11, 13))
    assert end == date(2026, 12, 13) and end.weekday() == 6 and rolled == date(2026, 12, 14)
    assert date(2026, 11, 13) + timedelta(days=28) == date(2026, 12, 11)  # day 28: RSA and petition (12B.9)

    # 3. The A/B exchange: two CUSIPs, one instrument. A consent deadline extended three times.
    CROSSWALK.update({"HALV144A0": "HALV-7.25-2029", "HALVREG00": "HALV-7.25-2029"})
    assert instrument_of("HALV144A0") == instrument_of("HALVREG00")
    versions = [(date(2026, 10, 15), date(2026, 10, 1)), (date(2026, 10, 22), date(2026, 10, 14)),
                (date(2026, 10, 29), date(2026, 10, 21)), (date(2026, 11, 5), date(2026, 10, 28))]
    ev = [ContractEvent("HALV-consent", "HALV-7.25-2029", "consent_deadline", d, k, "8-K") for d, k in versions]
    f13 = features(ev, instrument_of("HALV144A0"), date(2026, 10, 13))
    f20 = features(ev, instrument_of("HALVREG00"), date(2026, 10, 20))
    assert f13["days_to_next_contract_event"] == 2  # sees 15 Oct, not the 5 Nov it could not yet know
    assert f20["days_to_next_contract_event"] == 2 and f20["in_contract_window"] == 1

    # 4. The roll: 20 September 2026 is a Sunday, so the roll week starts Monday 21 September.
    assert index_roll_dates(2026)[1] == date(2026, 9, 21)
    assert features([], "ANY", date(2026, 9, 25))["in_roll_week"] == 1
    assert features([], "ANY", date(2026, 9, 28))["in_roll_week"] == 0

    # 5. Measurement (3B.7): 22 of 40 is 55% with SE near 7.9 points; ten 70% calls, six right, score 0.25.
    p40, se40 = hit_rate_se([1] * 22 + [0] * 18)
    assert abs(p40 - 0.55) < 1e-12 and abs(se40 - 0.0787) < 1e-3
    outcomes = [1] * 6 + [0] * 4
    random.shuffle(outcomes)  # order does not matter to the score
    assert abs(brier([0.7] * 10, outcomes) - 0.25) < 1e-12
    assert abs(brier([0.6] * 10, outcomes) - 0.24) < 1e-12

    # 6. A seeded synthetic year of 400 views at a true 55%: the standard error is about 2.5 points.
    year = [int(random.random() < 0.55) for _ in range(400)]
    p400, se400 = hit_rate_se(year)
    assert abs(se400 - 0.0249) < 0.003
    entry = LedgerEntry("TM-0001", date(2026, 10, 20), "BRAM-9.25-SSN", -1, 0.6, 20,
                        "$5mm, DTS-hedged in CDX HY", "refinancing launched at or above par", "days")
    assert entry.outcome is None and entry.ido_markout_bp == {}
    print(f"40 views: {p40:.3f} +/- {se40:.3f}; 400 views: {p400:.3f} +/- {se400:.3f}")
```

*Builds on:* §3.5 (the Edge Ledger), §3B.4 (event windows), §12B.9 (Halvorsen's grace clock), §27.3 (the bitemporal master), App D (holidays and settlement). *Used in:* §18.6.2 (event features in the jump charge), Chapter 8-C (the explain's corporate-action lines), §28.9 (the dashboard's calendar panel).

## 3B.12 Desk Debrief

*7:29 a.m., Day One, one minute before the risk meeting.*

Theo finds the twelve basis points with ninety seconds to spare, and they are where Kaz's offhand remark said they would be. The desk owns \$40mm of protection on the high-yield index, bought on the old series. The roll on Monday moved the market to the new series, and the pricing feed kept publishing Friday's mark for the old one, because nobody was quoting it anymore. High yield sold off about 0.3 points on Monday, so the protection made about \$120,000, and the official P&L, marked on a stale price, never saw it. The model, which computed the hedge's gain from the factor move, did. Down forty was really down twenty-eight. (Chapter 8-C works this morning line by line as its first worked example.)

"I wrote the model," says Kaz. "The model was fine."

"The model was fine," Ines agrees. "The mark wasn't." She turns to Theo. "You found twelve basis points nobody was looking for. That's the job for a year."

Mags, passing again: "Back in my day we'd have found it at bonus time." A pause. "Fine. Yours is faster."

- **The desk is a calendar with a P&L attached.** Most of a first year is servicing a clock on time: the 6:45 diff, the 7:15 explain, the 3:00 snap, Friday markouts, month-end true-ups, the 20 March and 20 September rolls.
- **A snap is a treaty between risk and P&L.** Two timestamps manufacture a phantom of $\text{DV01}\cdot(\Delta y_{t_2} - \Delta y_{t_1})$ that reverses tomorrow and is noisy today (Law 9).
- **Which clock has a contract attached? That one is yours.** Grace periods, record dates, consent deadlines, RSA milestones and NDA outside dates are features of $\lambda^{\mathbb{P}}$ that only someone who has read the documents can type in (Law 8).
- **Restriction is an interval, not a state.** It starts with a signature and ends with a cleansing 8-K or an outside date, and both ends can be forecast.
- **Every banker's mistake on a desk is a word that means two things.** Composite and price, face and JTD, $\mathbb{Q}$ and $\mathbb{P}$, memo and ledger entry (Law 4).
- **Forty bets measure your hit rate to about eight points; log the view, not just the P&L.** Year one is measured on calibration, process and the ledger, because outcomes cannot yet measure anything (Law 12).
- **IDO or it didn't happen,** including in the Friday hand history (Law 1).
- **The memo is five lines or it is not read.** View, probability, horizon, size and hedge, kill condition (Law 11).

### The Spec You Hand the Robot

> Build `desk_calendar.py`. **Calendars:** business-day arithmetic on named holiday tables (SIFMA for bonds, NYSE for ETF shares), following convention for rolls; settlement offsets per instrument class, with loan offsets labelled as targets. **Events:** versioned rows with `event_id`, instrument surrogate key, kind, `event_date`, `known_at` and `source`; extensions are new rows; an `as_of(t)` read returns the latest version known at `t`; a CUSIP crosswalk maps every identifier, including stubs left by exchanges, to one instrument. **Features:** `days_to_next_contract_event`, `in_contract_window`, `in_cleansing_window` (scheduling only, never alpha on a restricted name) and `in_roll_week`, all in business days. **Ledger:** view, date, instrument, direction, stated probability, horizon, size and hedge, kill condition, decay class, beta-stripped markouts at 1, 5 and 20 days, outcome; score with the hit rate and its standard error and the Brier score. **Never:** store only the latest version of a moving date, key an event to a CUSIP, or decide by code whether a weekend grace end rolls.

### Exercises

1. *(Measurement.)* Compute the standard error of a 55% hit rate on 40 and on 400 independent views, and the number of views at which 55% first sits two standard errors above 50%. **Check:** about 7.9 points; about 2.5 points; about 396 views.
2. *(The snap.)* A book with \$35,000 of DV01 is hedged DV01-for-DV01 in Treasury futures. Futures are marked at the 3 p.m. settlement and the bonds at a 4 p.m. composite. Yields rise 3 bp between the two. What does today's report show, and tomorrow's? **Check:** a phantom loss of \$105,000 today and a phantom gain of \$105,000 tomorrow; true P&L zero on both days.
3. *(Halvorsen's event table, from §12B.9.)* The 6% notes due 2031 are \$600mm face, and the coupon is missed on Friday 13 November 2026 *(illustrative date)*. Compute the coupon, the end of a 30-calendar-day grace period, and the date of day 28. **Check:** \$18mm; Sunday 13 December 2026 (read the indenture's business-day clause before rolling it to Monday the 14th); Friday 11 December, the day the RSA is signed and the company files.
4. *(JTD drift.)* Theo hedged \$10mm of Halvorsen bonds at 88 with \$8mm of protection, assuming 40% recovery. The bonds fall to 70. What is the JTD-neutral notional now, and what does Theo hold? **Check:** $(70 - 40)/60 = 0.5$, so \$5mm; he is over-hedged by \$3mm, a bet that pays about \$1.8mm on default.
5. *(Calibration.)* Theo states 80% on five views, and three come true. Compute his Brier score, and the score he would have earned by saying 60%. **Check:** 0.28 and 0.24.
6. *(ROBO's revenge.)* Was ROBO right about Columbus Day? A \$40mm in-kind ETF redemption delivers bonds that settle Tuesday against ETF shares that settle Monday. At 5% funding on ACT/360, what does the one-day gap cost? **Check:** about \$5,556, paid by whoever delivers cash first (App D). Not a credit event; a calendar event that costs money.

### Deep-Dive Resource Graph

**Podcasts**

- *Odd Lots*, "How to Succeed at Multi-Strategy Hedge Funds" (20 May 2024), with Giuseppe Paleologo: stop-losses, factor-neutral books and how platforms watch PMs; the measurement regime of §3B.7. https://omny.fm/shows/odd-lots/how-to-succeed-at-multi-strategy-hedge-funds
- *Odd Lots*, "How the Hottest Hedge Funds on Wall Street Really Manage Risk" (25 July 2024): leverage on the residual, not the beta. https://omny.fm/shows/odd-lots/how-the-hottest-hedge-funds-on-wall-street-really
- *Odd Lots*, "The Math That Explains How Multi-Strategy Hedge Funds Make Money" (7 October 2024), with Dan Morillo: breadth and the fundamental law behind mistake 5. https://omny.fm/shows/odd-lots/100724-odd-lots-dan-morillo-master
- *Odd Lots*, "Giuseppe Paleologo on Quant Investing at Multi-Strat Hedge Funds" (21 June 2025). https://omny.fm/shows/odd-lots/giuseppe-paleologo-on-quant-investing-at-multi-strat-hedge-funds
- *Capital Allocators*, "Jonathan Lewinsohn – Credit Microcycles at Diameter (EP.484)" (2 February 2026): a credit platform's calendar of opportunity, from the discretionary side. https://www.capitalallocators.com/podcast/credit-microcycles-at-diameter/
- *Cloud 9fin*, "LME Doomscrolling — Just because you can, doesn't mean you should" (31 August 2026), with Bill Derrough: a restructuring banker's view of the contract clocks of §3B.4. https://share.transistor.fm/s/6a6999bb
- *Signals and Threads*, Ep. 20, with Liora Friedberg (7 October 2024): production support rotas and alert hygiene, the boring half of §3B.2. https://signalsandthreads.com/solving-puzzles-in-production/

**Practitioner Writing**

- U.S. Senate Permanent Subcommittee on Investigations, *JPMorgan Chase Whale Trades: A Case History of Derivatives Risks and Abuses* (15 March 2013): daily marks, the mid-versus-booked spreadsheet and price-testing tolerances. https://www.hsgac.senate.gov/wp-content/uploads/imo/media/doc/REPORT%20-%20JPMorgan%20Chase%20Whale%20Trades%20(3-15-13).pdf
- Board of Governors of the Federal Reserve System and OCC, *Supervisory Guidance on Model Risk Management* (SR 11-7, 4 April 2011): effective challenge, change logs and outcomes analysis, the rules behind §3B.9's model review. https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107a1.pdf
- Man Institute, "Extra Credit: Algorithmic Advantage" (recorded March 2024): a systematic credit manager's day as execution choices. https://www.man.com/maninstitute/extra-credit-algorithmic-advantage
- FINRA, Rule 6730 (TRACE reporting within 15 minutes of execution). https://www.finra.org/rules-guidance/rulebooks/finra-rules/6730
- FINRA, SR-FINRA-2026-009 (filed April 2026), pp. 19–21: the economic baseline for the affiliate-principal indicator. https://www.finra.org/sites/default/files/2026-04/SR-FINRA-2026-009.pdf ; and FINRA Regulatory Notice 26-16 (26 August 2026), the effective dates.
- Moyer, *Distressed Debt Analysis*, pp. 62–64 printed (shelf pp. 79–81): signing "confi," restriction, ethical walls and big-boy letters.

**Academic Papers**

- Whalley, A. E., and P. Wilmott (1997), "An Asymptotic Analysis of an Optimal Hedging Model for Option Pricing with Transaction Costs," *Mathematical Finance* 7(3): the cube-root no-trade band.
- Brier, G. W. (1950), "Verification of Forecasts Expressed in Terms of Probability," *Monthly Weather Review* 78(1): the score of §3B.7.
- Murphy, A. H. (1973), "A New Vector Partition of the Probability Score," *Journal of Applied Meteorology* 12: calibration and resolution.
- Grinold, R. C. (1989), "The Fundamental Law of Active Management," *Journal of Portfolio Management* 15(3): $\text{IR} \approx \text{IC}\sqrt{\text{BR}}$.

**Data & Code**

- SIFMA holiday and early-close recommendations (canonical root): https://www.sifma.org/
- SEC EDGAR full-text search, for cleansing 8-Ks filed under Item 7.01: https://www.sec.gov/edgar/search/
- `desk_calendar.py`, this chapter's listing in Appendix F, and its neighbours `restructuring_state_machine.py` (Chapter 12-B) and `pnl_explain.py` (Chapter 8-C).

