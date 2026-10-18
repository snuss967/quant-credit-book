# Chapter 17-B: Marking the Unmarked: Private Credit LMEs

> **Prerequisites.** §17.2 (the mark as a filter), §17.3 (implied markdowns, the non-accrual gap, the Medallia ledger and the PB-16 box), §17.4 (the Pluralsight replay), §17.6 (the run with a pro-rata cap, the backlog recursion and the runway $\mathcal{T}$), §17.8 (the `soi` table, the six features, the pending mark $\Pi$ and the mark gap $G$), §14.2 (competing risks), Chapter 8-D (the short-leg menu and the ledger) and Law 14 (censoring is the signal). The chapter ships two listings through Appendix F: `pc_queue.py` and `pc_lme_detector.py`.
>
> *Builds on:* §17.3, §17.4, §17.6.2, §17.8.2–17.8.3, §13.6, §13.8, §14.1–14.3, §7-B.1, Chapter 8-D, §8B.9, Chapter 12-B. *Used in:* §26.7 (ROBO's mirror-image backtest of PB-16), Chapter 28 (the pod's year-end review), Appendix B (EDGAR full-text search by borrower, Schedule TO-I/A), Appendix C (the dated rows of 2025–2026).

*What is invented, once for the whole chapter: Dov Adler's pod at Vantress Capital Management, Wen Zhao, Marcus Oyelaran, Danny Ostrowski's platform and its valuation committee, the third-party valuer in that room, Theo's desk and everyone on it, ROBO, and every position, mark, P&L figure, card and model output these people produce are fictional composites and illustrative. The borrowers (Pluralsight, Medallia, Zayo), the funds and BDCs, their filings, marks, request and fill percentages, and every dated event followed by a source are real. Where a figure rests on a press report or a secondary tracker, the text says so. Nobody real says anything in this chapter that they did not say in public.*

## 17B.0 Cold Open: The Hedge That Wasn't Short Software

*(From the pod's history: Wednesday 4 February 2026. Dov Adler's pod, its explain, its sizes and every P&L figure are fictional and illustrative; OBDC, HYG, the BIS figures and the dated events are real.)*

At 7:10 on Wednesday 4 February 2026 the morning explain for Dov Adler's pod arrives the way it always does, as a PDF nobody requested and everybody reads. Fourteen pairs, one page each, and on every page the same four line groups Chapter 8-C taught the platform to print: the market line, the leak, the friction and the idio. Dov reads it standing, coffee in the hand that is not on the mouse, on the theory that sitting down implies the news is good enough to take seriously.

PB-16 is page eleven. It is three months old, and on paper it is the quietest pair in the book: long \$20mm of Blue Owl Capital Corporation's shares, ticker OBDC, bought about 14% below the net asset value the manager reports; short \$26mm of HYG, the high-yield bond ETF, borrowed through the prime broker. The thesis sentence carries a date, as all of Dov's do: *OBDC's discount says the marks will fall further than the public data says they will; the overshoot narrows by August 2026.* Chapter 17 tells how it was written (§17.3, the PB-16 box).

Tuesday's page reads like a typo. OBDC down 4.8%. HYG down 0.15%. The long lost \$960,000 and the short made \$39,000. The market line, which is what the hedge exists for, is close to zero: 1.3 times a 0.15% fall in HYG is about 0.2% on the long, and the short paid for exactly that. Everything else, about \$920,000, the explain has dropped into the line labeled *idio*.

"That isn't idio," Dov says, to nobody in particular, which in the pod means Wen.

Wen Zhao already has the borrow sheet open, because the first thing she checks when a short misbehaves is whether someone has taken the bonds back. Nothing has moved. HYG is general collateral, the fee is where it was last week, there has been no recall, and the share of the lender's inventory out on loan is unremarkable. "The weather's fine," she says. "Your short is exactly where you put it."

She reads the trade press over his shoulder. A new set of AI tools, launched days earlier, automated the kind of legal, sales and data work that software companies sell, and software equities had been falling since. The lenders to those companies went with them. Chapter 17 has the trade-press percentages for the managers' vehicles and the BIS's cleaner count, which the BIS would publish a month later: software equities down almost 30% between October and February, BDC shares about 10%, the most software-heavy BDCs about five points worse (§17.3, Beat 3). OBDC is one of the large lenders to software companies. HYG holds the public bonds of companies that mostly make, mine, drill, lease or broadcast things.

"So the long is a software lender," Dov says, "and the short is a basket of companies that sell almost anything else."

"The ledger said so on the first day." Wen pulls up the row and reads the third item in the leak column aloud, in the voice the pod reserves for reading people's earlier statements back to them: *The proxy shorts the wrong thing: HYG holds public high-yield bonds, a different mix from middle-market software loans, so a software shock can hit the long and miss the short.* "It's written down."

"Written down isn't hedged." Dov crosses out *idio* on the printout and writes *software* above it.

At 7:31 Marcus Oyelaran's email arrives, a minute later than usual, which the pod has learned to read as a sign that he has been looking at something. It carries the platform's overnight x-ray, the risk manager's translation of every pod's names into factors (Chapter 8-B), and it asks the question it always asks: *What is the book long that it did not mean to be?* There is no orange line on PB-16 yet. Its software loading sits inside the sector cell, because the risk model's software factor is built from public stocks and bonds, and its estimate of OBDC's exposure to that factor was fitted over 2025, a year in which software lenders and software stocks moved together about as much as anything moved together, which was not much.

> **Math, Gently.** *A hedge that shorts the wrong thing.* A pair's return is the long's return minus the hedge ratio times the short's. Suppose the long responds to two things, high-yield spreads and software, and the short responds only to high-yield spreads. With loadings of 1.3 on high yield and 0.6 on software (both illustrative), and the short sized at 1.3, the pair's return is $(1.3-1.3)\times$ the high-yield move, plus $0.6\times$ the software move, plus the long's own noise. The hedge erases the first term. It cannot touch the second, because there is no software in the short. Over a calm year in which the software factor moved about 1% a month, the second term was worth about 0.6% a month, invisible beside the noise of a listed stock, so the risk model rated it small. Then the software factor falls 8% in a day, and the same term is $0.6\times(-8\%)=-4.8\%$ on the long and zero on the short. The covariance between the pair and software was there all along. It was small on paper because the window was quiet, and large on the day because the day was not. The full version, with the hedge matrix, is §8.6, and the comparison of the three rulers is §8D.3.

In the book's notation, with factor returns $F_{k,t}$, loadings $\beta_{i,k}$ and idiosyncratic returns $\epsilon_{i,t}$, the pair's return is

$$
r^{\text{pair}}_t = r^{L}_t - h\,r^{S}_t = \big(\beta_{L,\text{HY}}-h\,\beta_{S,\text{HY}}\big)F_{\text{HY},t} + \beta_{L,\text{SW}}\,F_{\text{SW},t} + \epsilon_{L,t}-h\,\epsilon_{S,t},
$$

and a hedge sized at $h=\beta_{L,\text{HY}}/\beta_{S,\text{HY}}$ sets the first bracket to zero and leaves the software term in full. (Here $h$ is the hedge ratio of Chapter 8-D, not the haircut of §17.6.) The term was never hidden. It was priced at the variance of a quiet year.

Dov does not unwind. A thesis about marks is not wrong because software had a bad Tuesday, and selling a discounted asset into a sector panic is the trade the thesis was written to take the other side of. What he does is the pod's version of an apology. Under the thesis sentence on the whiteboard he writes the date and four words, *4 Feb 2026: the leak is the P&L*, and under that, two questions. The first is the one this chapter answers: *what can a desk that trades only public things know about a private mark before the mark moves?* The second is shorter and worse: *if the long is really long the mark's lag, what is short the mark?* Section 17B.5 answers that one, and the answer is the pair's epitaph.

*Card. 7:40 a.m., Wednesday 4 February 2026. Write three lines before reading on: what PB-16 is long that it did not mean to be; whether you add a short, and in what; and what would have to be true by August for the thesis sentence to pay. The cards are graded in §17B.7.*

Chapter 17 named the features a desk can compute on the schedules of investments, wrote down the queue's recursion and opened PB-16. This chapter fits the features, backtests them on the two borrowers whose stories are public enough to test on, estimates the queue from the funds' own filings, and follows the pair through the spring. By the end of it you will be able to read one private loan across every public vehicle that holds it and turn the disagreement into a feature, with the valuers clustered; put a private default or non-accrual number on a stated basis before comparing it with anything; de-duplicate a redemption series into the part that is new belief and the part that is last quarter's line coming back, and fit it with the censoring written into the likelihood; build a multi-state hazard model from PIK amendments to the keys and evaluate it on Pluralsight, Medallia and Zayo; and say, with arithmetic, why a pod that wants to be short a private mark has no instrument that does it.

## 17B.1 The Second Ledger: Pluralsight, by Holder

*(A replay told from the direct lender's chair. Danny Ostrowski, his platform, its committee, the third-party valuer, the platform's position in the loan and every mark the committee discusses for itself are fictional composites; the platform is not one of the BDCs in any public tally. Pluralsight's terms, the other holders' marks, the sponsor's marks and the dated events are from the BDCs' filings, KBRA's commentary, Goodwin's client alert and the press reports cited, and where reports differ the text says so. Cut-off for the committee: the afternoon of Thursday 25 April 2024.)*

Danny Ostrowski tells the story to Theo over a sandwich in October 2026, the week Theo finishes the Medallia ledger (§17.3.3), because Theo shows him the spreadsheet and Danny recognizes the shape of it. "We had that table in 2024," he says. "Except we read it down instead of across."

The room is a conference room on the 31st floor of a direct lender's platform, on the last Thursday of April 2024, at four in the afternoon, which is when quarterly valuation committees meet because the morning is for investment committees and the evening is for regret. The agenda is 214 positions, of which 190 will take thirty seconds each. Position 87 is a \$40mm piece of a first-lien term loan to Pluralsight, held in the platform's institutional drawdown fund, which files nothing public. Danny's slide has four rows of facts, and he has checked every one of them.

The loan is a \$1.175 billion first-lien term loan of the recurring-revenue kind, alongside a \$100mm revolver, put in place when Vista Equity Partners took the company private in April 2021. It pays SOFR plus 800, which was 13.56% all-in at the end of 2023, and it matures in April 2027 (ARCC 10-Q schedules). An ARR loan, as lenders call it, is sized on subscription revenue and liquidity rather than on EBITDA, which means that trouble arrives first as a renewal problem and only much later as a missed coupon. In the first quarter of 2023 the borrower needed covenant relief, which the lenders granted, and the sponsor put in about \$75mm of new equity (press reports; the lenders in the room knew because they had signed the amendment). The platform marked the loan at 95 at the end of December *(fictional)*.

The second slide is the one the third-party valuer built, and it is the one that goes wrong. The valuer's range is 92 to 95 *(fictional)*, and it rests on two legs. One is a yield analysis: discount the loan's cash flows at a rate taken from comparable unitranche loans, which come out near par for a loan paying SOFR plus 800 that has not missed anything. The other is what the report calls *market calibration*: the marks that other holders of the same loan published in their December 10-Ks, which arrived in late February and early March. Seven business development companies show the loan, and KBRA's tally of their December marks runs from 89.0 to 99.0. Ares Capital carried its piece, about \$106mm of cost, at 89.0. Blue Owl's BDC carried the same loan, same coupon, same maturity, at 96.8 (ARCC and OBDC 10-K schedules; KBRA).

"So the market says mid-nineties," says the committee's chair.

Danny has a sentence prepared for this, and he uses it. "The market is seven other committees. Each of them had a valuer, and each valuer calibrated to the others' September marks." He has the chart: seven lines that move together from quarter to quarter, close enough to look like consensus. "If they're anchored on each other, the average is an echo. The interesting number is the one that broke ranks. Ares is seven point eight points below Blue Owl, on one first-lien loan, before anything public has happened."

The valuer says that differences between holders usually reflect methodology: different comparables, a different weight on the yield approach, a different view of the call protection. All of which is true, and none of which explains a 7.8-point gap on one loan with one coupon. The chair asks the question that the slide was built to prevent. "Where is the sponsor marking its equity?"

Nobody knows. The platform is not a limited partner in Vista's funds, the sponsor's quarterly reports go to the people who are, and the packet has no row for it. There is a row for the sponsor's *support*, the \$75mm of 2023, which reads as good news. There is no row for what the sponsor thinks its equity is now worth, which is the one number in the capital structure that answers the committee's question directly: if the equity is worth something, the loan is covered and the mark is about the coupon; if the equity is worth nothing, the loan is the company.

The committee marks the loan at 93 *(fictional)*, a point below the bottom of the valuer's range, and Danny writes in the minutes that the cross-holder gap was discussed. It is a defensible mark. It is also the average of a set of numbers that were not independent of each other, nudged by one man's discomfort.

> **Math, Gently.** *How many valuers is seven?* Seven marks of one loan look like seven opinions, and averaging seven opinions should cut the noise by a factor of about $\sqrt7\approx2.6$. That arithmetic assumes the opinions are independent. Suppose instead that every pair of valuers shares some of the same information or the same anchor, so that their errors have a correlation $\rho$. Then seven marks are worth as much as $n_{\text{eff}}=7/\big(1+6\rho\big)$ independent ones. At $\rho=0.5$ that is $7/4=1.75$: seven committees, fewer than two opinions. And if two of the seven are the same committee, as the two Blackstone vehicles in the Medallia ledger are (§17.3.3), the count starts at six before the correlation is applied. The same arithmetic runs backwards, and that is the useful direction. When valuers anchor on each other, any disagreement that survives the anchoring is unlikely to be noise; it is a committee that saw something and was willing to be the outlier. A 7.8-point gap among herding valuers is worth more than the same gap among independent ones. The full version, with clustered standard errors and the design effect, is §7-B.1 and §7-B.6.

Here is what happened after the committee, as the filings and the press recorded it. In early May the BDCs filed their March 10-Qs. KBRA's tally of the seven holders' marks now ran from 83.4 to 97.0, a spread of 13.6 points; Ares had moved to 84.9 and Blue Owl to 83.5, a move of 13.3 points by Blue Owl in a single quarter (BDC schedules; KBRA). Vista's own fund documents, as reported later by the press, had marked its Pluralsight equity at \$2.3 billion in the first quarter of 2023 and \$1.5 billion at the end of 2023, had warned of "liquidity challenges" in an update of 15 April 2024, and valued the equity at zero in an update dated 28 May 2024. Over the late spring and early summer the company's intellectual property moved into a new restricted subsidiary, with about \$50mm from Vista funding an interest payment; reports differ on whether that money came as a loan or as preferred equity. KBRA described the steps as "reasonable and allowable stopgap measures," and creditors reportedly disputed the value of what had moved. On 3 June Bloomberg reported that Vista was in talks to hand the company to its lenders. At 30 June the BDCs carried the loan near 47 to 48: Ares at 48.0, Blue Owl at 47.0.

Around 22 August a lender group led by Blue Owl and Ares took ownership, with about \$275mm of new money and about \$1.2 billion of debt converted to equity, lenders at about 85% and management at about 15%; Vista and its co-investors lost about \$4 billion (Bloomberg). Goodwin's client alert, written before signing, had described different terms (lenders at 100% and \$250mm), so the terms moved late. Goodwin called it "one of, if not, the first sponsor funded LME" in private credit. From the first press report of talks to the change of control took about 2.6 months, against a median of about 4.5 months from pact to close across the European and private cases of Chapter 13-B (Figure 13-B.3; §13B.3 keeps the Pluralsight Docket Diary, entry by entry).

The Ad Hoc Group, represented by counsel, arrived at the edge of the timeline to file its Rule 2019 statement and found nothing to file it in. No petition, no docket, no court, no objection deadline, no excluded holder with standing to complain to a judge: seven managers, a sponsor and a phone. *(Cooperation agreements signed in this chapter: 0. The Ad Hoc Group asks that the record reflect it was not invited, and notes that there is no record.)*

The loan did not stop at the keys. At 30 September 2024 Ares held \$54.7mm of new paper at cost, a first-lien piece at SOFR plus 450 with 1.5% PIK, a second tranche at SOFR plus 750 paid in kind, and common units, against the \$106.5mm of old cost, and it booked about \$60mm of realized loss (ARCC 10-Q, September 2024). Then the restructured position kept falling. Ares's schedules carried it at a fair value of \$52.1mm in June 2025, \$46.5mm in September, \$40.1mm in December, \$23.1mm in March 2026 and \$21.8mm in June 2026, about 20.5% of the original \$106.5mm (computed from the ARCC schedules). By then only the first-lien piece, cut to SOFR plus 300 all in cash, sat near par; the second tranche and the equity were at zero. By press accounts, Ares and Oaktree wrote the new equity to zero in February 2026, and another holder had put its first-lien piece on non-accrual at the end of 2025. A restructured loan, in Mags's phrase from §17.4, is a loan that gets to default twice, and §14.3 owns the clock that times the second one.

![Figure 17-B.1: One loan, read by holder. Ares Capital's and Blue Owl's marks on Pluralsight's first-lien term loan, December 2023 to June 2024 (89.0, 84.9, 48.0 and 96.8, 83.5, 47.0), with KBRA's seven-holder range as a band (89.0–99.0 in December 2023, 83.4–97.0 in March 2024); then Ares's restructured position as a share of its original \$106.5mm cost, June 2025 to June 2026 (about 49%, 44%, 38%, 22% and 20.5%). Ticks mark the sponsor's equity marks (\$2.3bn, \$1.5bn, zero on 28 May 2024, public only later), the IP move, the 3 June 2024 report of talks, the change of control around 22 August 2024 and the press-reported equity write-off of February 2026. Source: ARCC and OBDC 10-Q and 10-K schedules of investments; KBRA; Bloomberg; press reports as labeled.](assets/figures/ch17b_pluralsight_by_holder.png)

<!-- FIGURE: ch17b_pluralsight_by_holder.png (two panels sharing a time axis. Left, Dec-23/Mar-24/Jun-24: ARCC 89.0, 84.9, 48.0; OBDC 96.8, 83.5, 47.0; band 89.0–99.0 (Dec-23), 83.4–97.0 (Mar-24). Right, ARCC position FV / original cost: Jun-25 48.9%, Sep-25 43.7%, Dec-25 37.7%, Mar-26 21.7%, Jun-26 20.5%. Event ticks: Q1-23 sponsor equity 2.3bn; Q4-23 1.5bn; 2024-05-28 zero (dashed: public later); 2024-06-03 talks; ~2024-08-22 keys; Feb-26 equity to zero (press).) -->

Danny's committee was not ahead of any of this. In July it marked the loan at 50 *(fictional)*, the same week everyone else did, and the minutes of April, with their sentence about the cross-holder gap, became the sort of document that is read aloud only at the next year's offsite.

"So what would you have needed?" Theo asks.

"Two columns," Danny says. "One for every other holder's mark, read across instead of down, with the ones that share a valuer counted once. One for the sponsor's equity mark, wherever it surfaces." He thinks about it. "And a third for what the credit agreement let them move. Which nobody in that room had read since closing."

That third column is Theo's, and the book has it elsewhere: Chapter 12-B for which document governs a drop-down, §13.6 for the collateral-leakage arithmetic, and §13B.3 for the docket the Pluralsight lenders never needed. The first two columns are this chapter's. They are the second ledger, the one that reads a private loan by holder rather than by quarter, and the first thing Theo writes when he gets back to the desk is a feature name with a date in it: *dispersion, clustered by adviser, level not slope, 25 Apr 2024 cut-off.*

> **View From Another Seat.** *The direct lender's committee.* From the chair at the end of Danny's table, a mark is not a forecast. It is a decision with consequences that arrive the next morning. A markdown changes the fund's reported return and, through it, the incentive fee and the fundraising slide; for a vehicle with a credit line it changes what the bank will lend against the loan; and in a club deal it is read by the other lenders and, sooner or later, by the sponsor, both of whom are about to be across a negotiating table. A lender marking to 50 in April would have been right, and would also have been the first holder to tell the sponsor what it thought the company was worth. The seat's honest defence is the one Ares Capital's president Jim Miller gave on the firm's fourth-quarter 2025 call (4 February 2026), describing first-lien loan-to-values across Ares's portfolio "in the high 30% to low 40% range" (§17.1): a first-lien lender with sixty cents of equity beneath it can be patient, because it expects to own the company before it loses money. The arithmetic of that defence is also its limit. Patience is priced on the equity cushion, and the equity cushion is the sponsor's mark, which is precisely the column the room did not have. When the cushion goes to zero, the loan is the company, and patience becomes ownership.

*Builds on:* §17.3.3 (the Medallia ledger), §17.4 (the Pluralsight replay and its three cards), §7-B.1 (clustered errors), §12B.4 (the out-of-court menu), §13.6 (drop-down leakage). *Used in:* §17B.4 (the dispersion and sponsor-mark features), §17B.5 (why the pod could not short it), §14.3 (the re-cut).

## 17B.2 PIK as a Hidden Default, Measured

#### Quant-Shop Life: The Reconciliation That Would Not Tie

*(A fictional composite of month-end on a systematic credit desk. The desk, its people, its tables, its tickets and its dialogue are invented; every BDC figure is from the company releases and filings cited, and the arithmetic on them is the desk's.)*

The last day of September 2026 is a Wednesday, which on Theo's desk means month-end, which means the risk committee's pack, which means that by four o'clock every number on page nine has to agree with the number its source published. Page nine is new. It is the private-credit page, and it has one chart: the share of each large BDC's loans on non-accrual, measured two ways, cost and fair value, over four quarters. Theo volunteered to own it in his second week, on the theory that a man who has reconciled a claims register to a proof-of-claim docket can reconcile anything. Kaz agreed to write the code, on the theory that anything Theo reconciles by hand will eventually need to be reconciled by a machine.

The desk's own number comes from the `soi` table of §17.8, every facility in every schedule of investments, one row per facility per quarter, with a flag for loans the schedule marks as on non-accrual. Sum the flagged rows, divide by the total, and the ratio should match what the BDC's earnings release says. At 10:15 it matches for none of the seven.

The misses are small and boring, which is the worst kind, because small and boring misses get waved through and then become the number. One BDC's release divides by total investments including equity and the desk divides by debt only. Another reports first-lien non-accruals in one table and everything else in another, and the parser read the first table. A third shows a loan on non-accrual in a footnote rather than with the marker beside the row, and the parser, which looks for the marker, did not see it. By 1:40 Theo has six of the seven within a tenth of a point and a ticket for the seventh. By 2:20 he has a list of every loan that appears in more than one BDC's schedule, which is the part nobody does, and finds what he half expected: loans flagged as non-accrual at one holder and accruing at another, in the same quarter.

Kaz looks at the list with the expression of someone whose model has just been told that the data have opinions. "So non-accrual is a legal event? Like an event of default under the credit agreement?"

"It's an accounting decision," Theo says. "The lender stops booking interest income it no longer expects to collect. The credit agreement can say the borrower is fine, and the lender can still decide it doesn't believe the borrower."

"So the default is whenever the CFO says so?"

"Welcome to private credit," Mags says from two chairs down, without looking up.

The list is not an anecdote. Octus, adjusting sector non-accruals for loans held by several BDCs, found that the figure rose from 1.45% to 2.18% of cost, and that widely held stressed loans showed "pricing gaps of nearly 40 points as measured by fair value divided by par" (Octus, 16 April 2026; §17.3.3). A loan that one committee has stopped believing in and another still accrues is the cross-holder dispersion of §17B.1 in a second unit, a flag rather than a price, and it goes into the detector of §17B.4 the same way: per valuer, clustered.

By 3:30 the chart on page nine has two lines per BDC, and the gap between them is the point.

> **Math, Gently.** *A ratio of two rulers.* Every BDC reports its non-accrual loans twice: as a share of the portfolio at what the loans cost, and as a share at what the manager now says they are worth. If the bad loans are 2.8% of cost but only 0.8% of fair value, the manager is carrying them at a fraction of what was paid, and the fraction is roughly the ratio of the two shares, $0.8/2.8\approx0.29$, times the whole portfolio's fair value over cost (about 0.98 here), so about 28 cents on the dollar. Two rulers, one bucket of loans, and the ratio between the readings is a mark the release never prints. That is OBDC's June 2026 quarter, and §17.3.3 derives it in full. The part that matters for a series is what happens when the rulers drift apart: a falling fair-value share with a rising cost share means new bad loans are arriving already marked down hard, so the headline improves while the hole deepens.

Here is the table that went to the committee, every BDC's second quarter of 2026 on the same two rulers:

| BDC | Non-accrual, % of fair value | Non-accrual, % of cost | Cost share ÷ FV share | FV share ÷ cost share |
| :-- | --: | --: | --: | --: |
| Ares Capital (ARCC) | 1.4 | 2.4 | 1.7x | 0.58 |
| Blue Owl Capital Corp (OBDC) | 0.8 | 2.8 | 3.5x | 0.29 |
| FS KKR (FSK) | 3.8 | 7.1 | 1.9x | 0.54 |
| Blackstone Secured Lending (BXSL) | 1.8 | 3.6 | 2.0x | 0.50 |
| Goldman Sachs BDC (GSBD) | 2.9 | 5.0 | 1.7x | 0.58 |
| Oaktree Specialty Lending (OCSL) | 1.8 | 4.2 | 2.3x | 0.43 |
| BCRED (non-traded) | 1.1 | 2.2 | 2.0x | 0.50 |

*Source: second-quarter 2026 earnings releases and reports; the two right-hand columns are computed. The last column, times each BDC's portfolio fair value over cost, is the implied carrying value of its bad loans (§17.3.3).*

Read across the last column and the seven managers are carrying their bad loans at between about 29 and 58 cents, before the portfolio adjustment. That is not a statement about whose loans are worse. A BDC that puts loans on non-accrual early, while they are still marked in the eighties, will show a high last column; one that waits until a loan has been marked to the forties will show a low one. Kaz's question had the chapter's argument folded inside it: when the flag is a decision, the flag's timing is a feature of the manager, and a ratio built on it carries the manager's habits along with the loans.

The same desk had a second series to reconcile that afternoon, and it did not tie either, for the same reason at a larger scale. In 2026 a reader asking how many private loans had defaulted got answers from 2.5% to 19%, depending on whom they asked:

| Measure | Level | As of | What is counted | PIK amendments and extensions |
| :-- | --: | :-- | :-- | :-- |
| Proskauer Private Credit Default Index | 2.51% | Q2 2026 | 716 loans in its index | as the index defines a default |
| KBRA middle-market measure | 3.5% | Aug 2026 | KBRA's forward-looking rate | — |
| Moody's, middle-market CLO obligors | 4.0% / 5.8% | 2026 | 607 obligors in 47 CLOs (as published) | excluded / included |
| Fitch private credit default rate | 6.3% | Aug 2026 | as reported in the trade press | included: PIK and deferrals were 47% of events |
| PIMCO shadow default rate | about 19% | 31 Mar 2026 | BDC loans, PIMCO's construction | broadest |

Every number is right about something. Mags put it in §17.8.2 as a menu, the same menu as the LMT chapters, moved into a market with no docket, and Chapter 14 (§14.1) has the general version: a default rate is a choice of what counts, and in a decade of liability management a choice of what counts is most of the answer. What changed on the desk at 3:45 is smaller and more useful. Theo added three columns to the default series in the desk's data store, beside every observation: *count or dollars*, *cost or fair value*, *PIK and extensions in or out*. "A default rate without its basis," he said, "is a bond price without a day count." Nobody wrote it on the whiteboard, which on this desk is how a sentence becomes permanent.

Mags, reading over Kaz's shoulder, finds the line in Medallia's schedules that makes the third column matter. Through 2025 the loan carried a coupon of SOFR plus 6.50%, of which 4% was paid in kind: added to the principal rather than paid in cash. In the December 2025 schedules the PIK component is gone and the coupon reads SOFR plus 6.00%, all in cash (BDC 10-K schedules; §17.3.3). The total spread fell by half a point, which looks like good news, and the cash the borrower owed rose from SOFR plus 2.50% to SOFR plus 6.00%, an extra \$3.5mm a year on every \$100mm of loan, which was not. One quarter later the two Blackstone vehicles carried the loan on non-accrual.

"Back in my day," Mags says, "a PIK was a confession with a deferral. You knew it when the coupon changed, because the borrower's lawyer called you to ask for it." She watches Kaz type *Medallia* into EDGAR's full-text search, restrict it to 10-Q filings and get seven holders' schedules in four minutes. "In 1998 that took a week, a fax machine and a favor." A pause. "Fine. That's good."

The PIK that lapsed is the mirror image of the PIK that §17.8.2 calls bad: one is a borrower who could not pay cash and a lender who preferred not to call it a default, and the other is a borrower who was allowed to defer until the deferral ran out. Both are visible in the schedules as a change in the coupon's composition, and both carry information a total spread hides. The desk ends the day with two derived columns on every facility-quarter, `pik_on_by_amendment` (a PIK component that was not there when the loan first appeared) and `pik_cliff` (a PIK component that disappears, raising the cash coupon), and a note that BCRED's PIK income was 5.6% of its total in the second quarter of 2026, the quarter its distribution rate went from 10.0% to 9.1% (BCRED reports). Whether the Fed's 25-basis-point rise of 17 September turns some of that PIK into non-accrual is a question the third-quarter schedules will answer in November, and it is on the Trend Watch of §17B.6.

The seventh BDC's ticket is still open at 5:30. It turns out to be a loan that moved from one line of the schedule to another between quarters, keeping its fair value and changing its name, and it takes until the following Tuesday to close. Nobody outside the desk ever knows.

*Builds on:* §14.1 (two default rates), §17.3.3 (the non-accrual gap), §17.8.2 (bad PIK; the six features). *Used in:* §17B.4 (the PIK states of the detector), §17B.6 (the Fed's hike and PIK), Appendix C (the default ladder, dated).

## 17B.3 The Queue, Estimated

*(Theo's desk, Thursday 15 October 2026. The desk, its dialogue, ROBO's output and the desk's nowcasts are fictional and illustrative. Every request, fill, backlog and quoted phrase is from the funds' Schedule TO-I/A filings and letters, the Federal Reserve and the IMF, or a tracker or press report where the text says so; "computed" marks the desk's arithmetic on those figures.)*

The week before, Kaz had asked ROBO to "forecast redemptions for the non-traded BDCs." ROBO returned a tidy table: every fund, every quarter from the fourth quarter of 2026 through 2028, 5.0%. It had done exactly what was asked. It had found, for each fund, the line in the 10-Q cash-flow statement for shares repurchased, divided it by shares outstanding, fitted the series, and observed correctly that for the last three quarters almost every number in it was the cap. ROBO had forecast the fills. It was right about the fills. It had learned nothing whatever about how many people wanted to leave, because the series it learned from could not show a number above five.

Theo spends Thursday morning building the series that can. Chapter 17's table of the 2026 queue (§17.6, Long Scene 2) has the request percentages from fund letters and press; he wants them from the filings, final amendment by final amendment, for ten funds and three cycles. A tender offer by a non-traded BDC is filed as a Schedule TO-I. The fund amends it as the offer runs, and the last amendment reports the result: shares tendered, shares accepted, the proration factor. By eleven he has thirty filings open in thirty tabs and has stopped seeing them as tender offers.

"It's a docket," he says to Kaz.

"It's a tender offer."

"It's a docket. Numbered entries, filed with a public authority, in order, each one amending the last, and the final one tells you who got paid how much." He scrolls. "And the 10-Q is the claims register. Every holder of a loan files its claim on it every quarter, in a schedule anyone can read. The restructuring I used to run from a data room is all here, late and in pieces, filed by seven different lenders who disagree with each other." He stops, because the next sentence is the one he has been circling since Danny's story. "And the disagreement is the signal."

It is the aha of this chapter, and it arrives with a filing index. The private market has no tape, but every large private loan sits in several public vehicles, and every semi-liquid vehicle has to publish what its holders asked for. The asset class without prices leaves a paper trail dense enough to build on. The trail is late, it is quarterly, and it is written by people with reasons to write it a particular way, all of which is also true of a bankruptcy docket.

> **Math, Gently.** *A censored series.* Imagine weighing people on a bathroom scale that stops at five. Anyone lighter than five shows their weight; anyone heavier shows five. Average the readings and you will badly underestimate how heavy people are, and if every reading for the last three days was five, a model trained on the readings will predict five forever. That is ROBO's table. A fund's repurchases are the bathroom scale: when requests are below the cap, repurchases show demand exactly; when requests are above it, repurchases show the cap. To see past five you need a second instrument, and the funds supply one when they report requests or a proration factor alongside the payment. OTIC, Blue Owl's software-focused fund, reported requests for 40.4% of its shares in the first cycle of 2026 and a fill of 14.4%, so it repurchased about 5.8% and left about 34.6% of its shares in the line (computed). A forecast built on the 5.8% says next quarter looks like this quarter. A forecast built on the 34.6% says most of next quarter's requests are already known. Law 14 has the likelihood that uses both readings at once, and the full version for the queue is below.

Theo's first table is the one anyone would build, requests and fills by fund and cycle. His second is the one his thirteen-week model on the USB stick has been asking for since Chapter 1: a beginning balance, the new arrivals, the amount served, an ending balance carried to the next period. The model refuses to die again, this time as a queue. The arrival rate is new requests; the service rate is the cap, 5% of shares a quarter, and what that service costs the fund in cash is the cap less whatever new subscriptions arrive, the row that used to say *revolver draws*; the backlog is the line. Kaz recognizes it as Chapter 17's recursion (§17.6.2) and points out, correctly, that the recursion takes the new arrivals as an input. Theo's job is to recover them.

The algebra is three lines, in Chapter 17's notation: $a_t$ is the share of the fund's shares tendered in cycle $t$, $f_t$ the fill, $c$ the cap, and the share actually repurchased is $p_t=a_tf_t$, which equals $\min(a_t,c)$ when the cap is applied as written. Let $\xi$ be the share of last cycle's unfilled requests that come back, and $\iota_t$ the shares issued between the two offers as a fraction of last cycle's shares. Then the returning line, as a share of this cycle's shares, and the share of holders not already in line who joined it are

$$
b_t=\xi\,\frac{a_{t-1}-p_{t-1}}{1-p_{t-1}+\iota_t},
\qquad
a^{\text{new}}_t=\frac{a_t-b_t}{1-b_t}.
$$

The second expression is Chapter 17's $a^{\text{new}}$, the fraction of non-queued shares that request, recovered from published numbers instead of assumed. Setting $\xi=1$ and $\iota_t=0$ says every prorated holder resubmits and nobody new subscribes, which makes $a^{\text{new}}_t$ a lower bound on new demand. The bound can be checked against the one fund that published the other side. Morgan Stanley's North Haven fund (NHPIF) asked for 11.6% in the second cycle and filled 43.0%, then drew 11.4% in the third. With $\xi=1$ the returning line is about 7.0% of shares, which would make resubmissions about 61% of the third cycle's requests (computed). Its letter says nearly two thirds were (NHPIF letter, third cycle of 2026). On the one fund that reports both sides, the assumption that almost everyone comes back is almost right.

Here is the panel with the line taken out *(computed; requests and fills from Schedule TO-I/A final amendments unless noted; joiners are lower bounds under $\xi=1$, $\iota=0$)*:

| Fund | Requests, % of shares (Q1 / Q2 / Q3 2026) | Fill (Q1 / Q2 / Q3) | Joiners $a^{\text{new}}$, Q2 | Joiners $a^{\text{new}}$, Q3 |
| :-- | :-- | :-- | --: | --: |
| OTIC (Blue Owl, technology) | 40.4 / 38.1 / — | 14.4% / 13.1% / — | 2.2% | — |
| OCIC (Blue Owl) | 21.9 / 18.8 / 16.8 | 22.8% / 26.6% / about 30% | 1.2% | 2.7% |
| ADS (Apollo) | 11.0 / 16.8 / pending | 45.2% / 29.8% / — | 11.2% | — |
| HLEND (HPS) | 9.2 / 13.3 / pending | 54.0% / 37.6% / — | 9.3% | — |
| ASIF (Ares) | 11.6 / 14.4 / 13.1 | 43.1% / 34.7% / 38.2% | 8.0% | 3.6% |
| BPCC (Blackstone, private credit) | 11.3 / 10.9 / 10.7 | 44.3% / 46.0% / 46.8% | 4.6% | 4.8% |
| NHPIF (Morgan Stanley) | 10.9 / 11.6 / 11.4 | 45.8% / 43.0% / 43.8% | 5.7% | 4.8% |
| BCRED (Blackstone) | about 7.9 / about 10 / about 10 | upsized to 7%, paid / about half / 5% of shares | about 10% | about 5% |

*BCRED's first-cycle request is a press figure; its first cycle was paid in full after Blackstone and its employees put about \$400mm into a feeder fund, and its later cycles are from its letters (\$4.5 billion requested and about half paid in the second, a \$2.3 billion backlog, about \$4.3 billion requested and 5% of shares repurchased in the third). ADS and HLEND had not filed third-cycle results by 18 October 2026.*

Kaz reads the table twice and then reads it out, which on this desk is the beginning of a change of mind. "OTIC had forty percent of its shares in line two quarters running, and the headline said the run was continuing. But the joiners were two percent. The line is long and it isn't lengthening. Same at OCIC." He moves his finger down. "ADS and HLEND are the opposite. Their headlines were smaller. Their joiners in the second quarter were ten percent. That's new belief arriving, at funds that weren't in the news."

"And by the third quarter," Theo says, "everything that reported has joiners at or under five percent. Under the cap. If that holds, the lines stop growing and start draining." He does not say *the run is over*, because the joiners are lower bounds and because the arithmetic of draining is slower than the word suggests.

> **Math, Gently.** *How long is the line, really?* A queue has three numbers: how fast people arrive, how fast they are served, and how many are waiting. If arrivals are slower than service, the line drains; if faster, it grows without limit, until someone changes the rules. A rule from operations research, Little's law, links the three on average: the typical wait equals the length of the line divided by the rate at which it is served. OTIC after its second cycle had about 35% of its shares in line and served 5% a quarter, so a holder at the back of a first-come-first-served line would wait about $35/5=7$ quarters. But a tender line is not first come, first served. It is pro rata: everyone in line gets the same fraction each quarter, so a holder who tenders everything every quarter at OTIC's 13.1% fill gets 13.1% out in the first quarter and 13.1% of the remainder in the next. After $n$ quarters the share still trapped is $(1-0.131)^n$. Half is out after 5 quarters; 90% is out after 17, more than four years (computed, at a constant fill). Pro rata is fair to everyone in line and slow for all of them, and the tail is longer than the average suggests. The fill rises as the line drains, so the 17 quarters is a ceiling for OTIC as of the second cycle, not a forecast. The full version, the recursion with a backlog, is §17.6.2.

The nowcast the desk builds that afternoon is two parts, and the honest thing about it is that one part is nearly arithmetic and the other is nearly a guess. Next cycle's requests are the returning line plus the joiners. The returning line comes straight out of this cycle's filing: requests minus repurchases, carried to the new share count. The joiners need a model. Kaz fits the simplest one the panel can bear, the logarithm of joiners against the drawdown of the median listed BDC over the tender window, with the cycles where only a payout at the cap was published entering the likelihood as lower bounds rather than exact numbers, the survival term of Law 14. On twenty-odd fund-cycles the slope comes out positive and the interval around it is nearly as wide as the slope *(illustrative)*. Theo writes beside it: *joiners rise when the listed sibling falls; the panel cannot say by how much.*

The two pending funds make the point concrete. ADS repurchased about 5% of its shares in the second cycle out of 16.8% requested, so its third-cycle line starts at about 12.4% of shares before anyone new asks. If its joiners fall back to 5%, third-cycle requests will be about 16.8%; if they stay at the second cycle's 11.2%, about 22.2%. HLEND's line starts at about 8.7%, and the same two cases give about 13.3% and 17.2% *(computed; the desk's illustrative nowcast as of 15 October 2026, before either fund reported)*. The range is the joiners. The floor is arithmetic.

"So what can it forecast?" Ines asks at the end of the day, standing behind them with her coat on.

"The part that's already in line," Theo says. "Almost perfectly. The part that's new, badly. And the part that matters most, not at all: what the sponsor does about it." He has the letters open in the other window. "That's not in the queue. It's in the board minutes."

Blue Owl's letter to OCIC's holders after the third cycle says that "the vast majority" of the requests came from holders who had tendered before; it is the same fact North Haven reported with a fraction. The Federal Reserve had put the year's turn in one sentence in May: accepted redemptions at perpetual BDCs "somewhat exceeded new inflows in the first quarter of 2026, the first time this has occurred since these vehicles were created" (Fed *Financial Stability Report*, 8 May 2026). The IMF's runway arithmetic, 9 to 11 quarters of 5% redemptions in mild stress and 5 to 7 in a moderate shock, is the denominator of §17.6.2's $\mathcal{T}$, and §4C.6 has the same arithmetic from inside a direct lender whose own fund drew 8% against its cap. Chapter 12 (§12.7) has the allocator's version: a sleeve whose exit is a pro rata fill belongs in a liquidity tier of its own.

> **View From Another Seat.** *The sponsor.* From the chair of the firm that runs a semi-liquid fund, the queue is a problem with five known tools, and in 2026 the sponsors used all five (§17.6, Long Scene 2). What the sponsor's seat sees and the investor's often does not is that every tool moves value between the holders who leave and the holders who stay, in a direction that depends on whether the marks are right. *Upsizing the cap with house money*, as Blackstone did for BCRED in the first quarter, buys leavers' shares at NAV: if the marks are right, the sponsor has bought a fair asset and signalled confidence; if they are high, the sponsor has paid the leavers' premium out of its own pocket rather than the stayers'. *Return of capital in place of tenders*, as OBDC II did in February, pays everyone pro rata; it ends the race to the door, because there is no door, but it turns every holder into a leaver on the sponsor's schedule. *Selling loans at par to fund the exit*, as Blue Owl did on 18 February, is fair to the stayers only if the loans sold were average; the buyer chose what it bought, so the slices left behind are, on average, no better than the slices sold (§17.9's second warning). *Buying back the listed sibling below NAV*, as OBDC did at 86% of book, moves value the other way, from the sellers to the holders who stay, and is the one tool on the list that pays stayers. *Cutting the distribution*, as BCRED did from 10.0% to 9.1%, keeps cash in the fund and taxes the holders who came for income, who are often the ones most likely to leave. The IMF's reading of the gate as "discretionary," with managers who "either accommodated redemptions above the 5 percent limit or gated them despite apparent balance sheet capacity" (IMF *Global Financial Stability Report*, April 2026), is the same observation from the regulator's chair. None of the five appears in the queue's recursion, and all five change it.

Theo's thirteen-week model went home that evening on the same USB stick it arrived on, now with three new rows and a Little's-law cell that someone had labeled *wait (qtrs)* in red.

The listing below is what the afternoon's arithmetic became. At this point in the story the desk has thirty final amendments a quarter, a press figure here and there, and a nowcast that has to be re-run the morning each new amendment lands, for every fund at once. One quarter on a calculator is easy; three cycles of de-duplication across ten funds is where hand arithmetic stops tying, and a forecast that is half mechanical and half belief is exactly the kind that gets quietly re-typed wrong.

`split_requests` takes last cycle's requests and fill and this cycle's requests, all as fractions of shares, plus the resubmission share $\xi$ and any new subscriptions, and returns four numbers: the returning line $b_t$, new requests as a share of all shares, the joiners $a^{\text{new}}_t$, and the resubmission share a fund letter would report. It is built around the fill a fund actually achieved, not the cap it advertised, so an upsized quarter like BCRED's first one carries its real repurchase forward. When the returning line computed under $\xi$ would exceed this cycle's requests, it caps the line at the requests and reports zero new demand; that floor binding is a message that $\xi$ is too high for this fund, usually because prorated holders gave up. `nowcast_requests` adds the returning line to a low and a high case for joiners and returns next cycle's range. `prorata_quarters` counts the quarters a holder needs to get a target share out at a constant pro rata fill, and `littles_wait` is the first-come-first-served average for comparison. `fit_censored_lognormal` fits log joiners on a covariate by maximum likelihood, with cycles known only as lower bounds entering through the normal survival function, which is Law 14's likelihood with a cap in place of TRACE's.

The checks reproduce the table: OTIC's 2.2% joiners, OCIC's 2.7%, ADS's 11.2%, North Haven's 61% resubmission share, the 5- and 17-quarter pro rata clocks, Little's 7 quarters, and the ADS range of 16.8% to 22.2%. A seeded simulation then shows the censored fit recovering a known slope and spread while a naive fit that treats capped rows as exact gets both too small, which is ROBO's table in miniature.

It fits any fund that publishes requests and fills, and funds that publish only payouts once the censoring flag is set. It does not forecast what a board will do, and a cycle in which the sponsor changed the rules (an upsized cap, a switch to return of capital, a suspension) belongs outside the fit, as an event, not inside it as an observation. The edge case that bites is the word *fill*. Some filings and letters report the fill as a share of requests and others as a share of shares outstanding, and the dossier's own note on OCIC's third cycle reads "5% filled" in the second sense. Passing 0.05 as `f_prev` there would make the repurchase 0.84% of shares instead of 5%, and next cycle's returning line about four points too long, with nothing raised to warn you.

<!-- EXPLAINED -->
```python
# pc_queue.py: the redemption queue, de-duplicated and nowcast (Chapter 17-B, §17B.3)
import numpy as np
from scipy import optimize, stats


def paid_share(a, f):
    """Share of shares outstanding repurchased this cycle, p = a * f (decimals)."""
    if not (0.0 <= a <= 1.0 and 0.0 <= f <= 1.0):
        raise ValueError("requests a and fill f must be decimals in [0, 1]")
    return a * f


def split_requests(a_prev, f_prev, a_now, xi=1.0, subs=0.0):
    """Split this cycle's requests into the returning line and new joiners.

    a_prev, f_prev: last cycle's requests and fill (fill as a share of REQUESTS),
                    both as fractions of last cycle's shares.
    a_now: this cycle's requests, as a fraction of this cycle's shares.
    xi: share of last cycle's unfilled requests that come back (1.0 = all of them).
    subs: shares issued between the two offers, as a fraction of last cycle's shares.

    Returns a dict:
      returning  b_t, the resubmitted line, as a fraction of this cycle's shares;
      new_share  a_t - b_t, new requests as a fraction of all shares;
      joiners    (a_t - b_t) / (1 - b_t), Chapter 17's a^new;
      resub      b_t / a_t, the resubmission share a fund letter would report.
    With xi = 1 and subs = 0, joiners is a lower bound and resub an upper bound."""
    if not (0.0 <= xi <= 1.0) or subs < 0.0:
        raise ValueError("xi must be in [0, 1] and subs >= 0")
    p = paid_share(a_prev, f_prev)
    b = xi * (a_prev - p) / (1.0 - p + subs)
    b = min(b, a_now)  # the floor: more returning than requested means xi is too high here
    joiners = (a_now - b) / (1.0 - b) if b < 1.0 else np.nan
    resub = b / a_now if a_now > 0 else np.nan
    return {"returning": b, "new_share": a_now - b, "joiners": joiners, "resub": resub}


def nowcast_requests(a_now, f_now, joiners_lo, joiners_hi, xi=1.0, subs=0.0):
    """Next cycle's requests: the returning line (arithmetic) plus a range of joiners (belief).
    Returns (returning, low, high) as fractions of next cycle's shares."""
    p = paid_share(a_now, f_now)
    b = xi * (a_now - p) / (1.0 - p + subs)
    lo = b + joiners_lo * (1.0 - b)
    hi = b + joiners_hi * (1.0 - b)
    return b, min(lo, 1.0), min(hi, 1.0)


def prorata_quarters(fill, target=0.5):
    """Quarters for a holder who tenders everything every cycle to get `target` of the shares
    out at a constant pro rata fill: the smallest n with 1 - (1 - fill)**n >= target."""
    if not (0.0 < fill <= 1.0) or not (0.0 < target < 1.0):
        raise ValueError("fill must be in (0, 1] and target in (0, 1)")
    if fill == 1.0:
        return 1
    return int(np.ceil(np.log(1.0 - target) / np.log(1.0 - fill)))


def littles_wait(backlog, throughput):
    """Average wait, in quarters, in a first-come-first-served line: W = L / throughput."""
    return np.inf if throughput <= 0 else backlog / throughput


def fit_censored_lognormal(y, censored, x):
    """Maximum likelihood for log(y) = mu0 + mu1 * x + sigma * eps, eps ~ N(0, 1).

    Rows with censored=True are lower bounds (the filing says only that the cap bound)
    and contribute log P(Y >= y), the survival term of Law 14, instead of a density."""
    y = np.asarray(y, float)
    x = np.asarray(x, float)
    c = np.asarray(censored, bool)
    if y.shape != x.shape or y.shape != c.shape:
        raise ValueError("y, censored and x must have the same length")
    if np.any(y <= 0):
        raise ValueError("y must be positive: drop or floor zero rows before fitting")
    ly = np.log(y)

    def nll(theta):
        mu0, mu1, log_s = theta
        z = (ly - mu0 - mu1 * x) / np.exp(log_s)
        ll_obs = stats.norm.logpdf(z[~c]) - log_s - ly[~c]
        ll_cen = stats.norm.logsf(z[c])
        return -(ll_obs.sum() + ll_cen.sum())

    x0 = np.array([ly.mean(), 0.0, np.log(ly.std() + 1e-3)])
    res = optimize.minimize(nll, x0, method="Nelder-Mead",
                            options={"xatol": 1e-6, "fatol": 1e-7, "maxiter": 20000})
    mu0, mu1, log_s = res.x
    return {"mu0": float(mu0), "mu1": float(mu1), "sigma": float(np.exp(log_s)),
            "n": int(y.size), "n_censored": int(c.sum()), "converged": bool(res.success)}


# --- sanity checks: the chapter's numbers (computed; xi = 1, no subscriptions) ---
otic = split_requests(0.404, 0.144, 0.381)
assert abs(otic["new_share"] - 0.0138) < 5e-4 and abs(otic["joiners"] - 0.022) < 1e-3
assert abs(split_requests(0.188, 0.266, 0.168)["joiners"] - 0.027) < 1e-3     # OCIC, Q3
assert abs(split_requests(0.110, 0.452, 0.168)["joiners"] - 0.112) < 1e-3     # ADS, Q2
assert 0.58 < split_requests(0.116, 0.430, 0.114)["resub"] < 0.64             # NHPIF: "nearly two thirds"
assert split_requests(0.20, 0.25, 0.04)["new_share"] == 0.0                     # the floor binds
assert prorata_quarters(0.131, 0.5) == 5 and prorata_quarters(0.131, 0.9) == 17
assert abs(littles_wait(0.35, 0.05) - 7.0) < 1e-12
_, lo, hi = nowcast_requests(0.168, 0.298, 0.05, 0.112)                          # ADS, pending Q3
assert abs(lo - 0.168) < 2e-3 and abs(hi - 0.222) < 2e-3

# --- the censored fit recovers known parameters; the naive fit shrinks them ---
rng = np.random.default_rng(1702)
n = 2000
x = rng.normal(0.0, 1.0, n)
y_true = np.exp(np.log(0.04) + 0.3 * x + 0.5 * rng.normal(0.0, 1.0, n))
cap = 0.08
cens = y_true > cap
y_obs = np.where(cens, cap, y_true)
fit = fit_censored_lognormal(y_obs, cens, x)
naive = fit_censored_lognormal(y_obs, np.zeros(n, bool), x)
assert fit["converged"] and abs(fit["mu1"] - 0.3) < 0.05 and abs(fit["sigma"] - 0.5) < 0.05
assert naive["mu1"] < fit["mu1"] and naive["sigma"] < fit["sigma"]
print({k: (round(v, 3) if isinstance(v, float) else v) for k, v in fit.items()})
```

![Figure 17-B.2: The queue with the line taken out. Left: requests against fills for the funds in the table, three cycles of 2026, with the curve $f=c/a$ at a 5% cap drawn through them (OTIC near 40% and 14%, OCIC near 20% and 25%, the middle of the pack between 9% and 17% requested, a tracker's Golub, Goldman Sachs and Fidelity vehicles at 3% to 5% and paid in full), and an inset of BCRED's second and third cycles as bars (\$4.5 billion requested, about half paid, a \$2.3 billion backlog, about \$4.3 billion requested). Right: for each fund and cycle, the headline request share beside the joiners $a^{\text{new}}$ once the returning line is removed (lower bounds, $\xi=1$). Source: Schedule TO-I/A final amendments; BCRED letters; a secondary tracker for the paid-in-full funds; computed columns as in the table.](assets/figures/ch17b_queue_requests_fills.png)

<!-- FIGURE: ch17b_queue_requests_fills.png (left scatter: (40.4,14.4),(38.1,13.1) OTIC; (21.9,22.8),(18.8,26.6),(16.8,~30) OCIC; ADS (11.0,45.2),(16.8,29.8); HLEND (9.2,54.0),(13.3,37.6); ASIF (11.6,43.1),(14.4,34.7),(13.1,38.2); BPCC (11.3,44.3),(10.9,46.0),(10.7,46.8); NHPIF (10.9,45.8),(11.6,43.0),(11.4,43.8); tracker: GCRED (4.8,100), GS PCC (3.2,100), Fidelity (2.9,100); curve f = min(1, 5/a). Inset bars BCRED Q2 4.5bn req / ~2.25bn paid / 2.3bn backlog; Q3 ~4.3bn req. Right paired bars headline vs joiners: OTIC Q2 38.1 vs 2.2; OCIC Q2 18.8 vs 1.2, Q3 16.8 vs 2.7; ADS Q2 16.8 vs 11.2; HLEND Q2 13.3 vs 9.3; ASIF Q2 14.4 vs 8.0, Q3 13.1 vs 3.6; BPCC Q2 10.9 vs 4.6, Q3 10.7 vs 4.8; NHPIF Q2 11.6 vs 5.7, Q3 11.4 vs 4.8.) -->

*Builds on:* §17.6.2 (the run with a pro-rata cap, the backlog recursion, the runway), Law 14, §4C.6 (the direct lender's 8% quarter), §12.7 (liquidity tiers). *Used in:* §17B.4 (the holder's own queue as a feature), §17B.5 (OBDC II's return of capital), §17B.6 (Trend Watch: the pending ADS and HLEND results), Appendix B (Schedule TO-I/A as a data source).
