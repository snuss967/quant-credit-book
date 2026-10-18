# Chapter 9-B: The Bond Data Problem and the Replication Crisis

> **Builds on / used in.** *Builds on* Chapter 2 §2.2.2 (the TRACE caps as censoring), Chapter 4's rerun week (Kaz's Sharpe of 3.1 becoming 0.9), Chapter 7 §7.2 and §7.8–§7.9 (the replication history, false-discovery control, the deflated Sharpe ratio and the two biases derived), Chapter 8 §8.2 and §8.4 (duration-matched returns; the DTS-neutral pair) and Chapter 9 §9.9 (`obap_repro` and Hana's red build). *Used in* Chapter 10 §10.1 and §10.5 (which momentum is left to trade), Chapter 8-D (the short leg's price), Chapter 7-B (clustered residuals), Chapter 18 §18.8 and Chapter 22 §22.2 (decoding TRACE; the transparency ledger), Chapter 27 §27.2 and Appendix B §B.16 (the data-quality gates) and Appendix F, Listing 9B.1.

*What is invented, once for the whole chapter: the desk (Theo, Ines, Kaz, Mags, Hana and ROBO), its trade-reporting analyst Odile Brandt, its risk committee, Vantress Capital Management and its analyst Wen Zhao, the issuer Brambleworth Packaging, and every desk number, run, count, price and P&L in these scenes are fictional composites and illustrative. The papers, their numbers, the FINRA rules and the dated events are public and cited. Every number taken from Dickerson, Robotti and Rossetti (2026) is gross of trading costs, as is every alpha on their survivor list; the chapter repeats this where it matters, because it matters.*

## 9B.0 Cold Open: The Number That Moved by Itself

Tuesday, 10 November 2026, 7:40 a.m., Theo Marsh's eighth week. The factor library's nightly report arrives as a forty-page PDF that nobody reads past page three, and Kaz reads it standing up, coffee in the other hand, the way some people read a weather forecast for a city they are not visiting.

Page three carries the retired factors. The risk committee likes to keep them on the chart, the way a hospital keeps the file of a patient it has discharged, in case the patient comes back. Row 14 is six-month bond momentum, `mom6_1`, retired in Kaz's rerun week (Chapter 4) and kept as a reference line. On Monday's report its alpha was 0.46% a month, with a $t$-statistic of 2.4. This morning it is 0.22%, $t$ of 1.1.

Kaz put the coffee down. Kaz opened the repository and read its history back to Thursday. Nothing. Five thousand lines in the factor library, and not one of them had changed since the last time the number was 0.46. What had changed over the weekend was the quarterly WRDS refresh of the TRACE files, and a data ticket, DATA-3311, that repointed the library's input from the legacy vendor panel to the desk's new build.

"The code didn't move," Kaz said, "and the answer halved."

Theo had seen this shape before, in a data room. A cap table that changes between two drafts of a model nobody touched means the transfer agent re-ran the register. "Which line did it come from?"

"Wrong noun," Ines said, without looking up from her own screen. "Not which line. Which choice." She turned around. "The committee meets next Wednesday. They will ask what they always ask: why is this number different from yesterday? I would like an answer that isn't 'the data.'"

So that is the question this chapter answers: *how do you build a bond-return panel that cannot lie to you, and what is left of the factor literature when you have?* (Both of Kaz's numbers are the desk's own and fictional. That they equal, to the second decimal, two numbers in a published table is the clue, and §9B.5 cashes it.)

By the end of this chapter you will be able to read a TRACE row and say which of its fields a backtest inherits; build a bond-month panel in the published Stage 0 order and say what each filter protects against and what it could delete by mistake; write a month's bond return with its two prices and choose between a T-bill and a duration-matched Treasury as the benchmark; size the two biases that built the bond-factor zoo, and apply their fixes; read the 26 survivors of the 2026 audit beside a non-standard-error band and an honest trial count; and carry the survivor list through Chapter 9's cost curve to the short list a desk could actually trade.

## 9B.1 What a TRACE Row Actually Is

Theo's instinct, eight weeks out of a restructuring practice, was the one PJT had trained into him: when a number moves, go to the source document. At PJT the source document was the data room. On this desk it was two rows of desks away, in a corner that faces a wall, where Odile Brandt has cleared the desk's TRACE exceptions for nine years.

Odile's working day runs on a fifteen-minute clock. FINRA Rule 6730 requires a dealer to report a corporate-bond trade "as soon as practicable, but no later than within 15 minutes of the Time of Execution," and a report that misses the window goes in late, marked *as/of*. One late report is a nuisance. A pattern of them is, in FINRA's language, a possible violation of the just-and-equitable-principles rule, Rule 2010. So Odile's queue is the list of the desk's own prints that a system thinks are wrong: a capacity flag that says *principal* on a trade the desk did as agent, a contra-party code that does not match, a trade booked at 2:58 p.m. and reported at 3:19.

"Pick a bond," she said.

Theo picked the one he knew: Brambleworth Packaging's 8% notes due 2030, the book's fictional single-B issuer, the one the desk had bid at 85½ in his fourth week (Chapter 3). Odile pulled up the public tape for Monday, 9 November, merged with the desk's own reporting log, and turned the screen toward him. It looked like this *(every row illustrative)*:

| Time | Status | What the row says | Capacity | Size shown | Price |
| :-- | :-- | :-- | :-- | :-- | :-- |
| 09:47:12 | T | desk sells to a customer | P | 1MM+ | 85.250 |
| 10:41:09 | T | desk buys from a customer | A | 250,000 | 84.875 |
| 10:41:09 | T | desk sells to another dealer | A | 250,000 | 84.875 |
| 10:41:30 | T | other dealer buys from the desk | P | 250,000 | 84.875 |
| 11:58:02 | T | a third dealer sells to a customer | P | 40,000 | 8.5125 |
| 14:03:51 | C | cancels the 09:47 report (Prior Reference Number attached) | P | 1MM+ | 85.250 |
| 14:03:51 | R | replaces it, corrected | P | 1MM+ | 85.125 |
| 15:20:44 | Y | reverses a report of 29 September (As-Of flag R) | P | 500,000 | 86.000 |

Eight rows. Theo counted the trades that had actually happened on this bond that Monday and got three.

The first row is a real trade of \$3 million that the tape shows as `1MM+`, because FINRA disseminates high-yield sizes capped at \$1 million in real time (investment grade is capped at \$5 million, shown as `5MM+`). Chapter 2 (§2.2.2) treats the cap as what it is, censoring, and Chapter 22 (§22.2.2) prices what hides behind it, so the only point here is the one Theo wrote on a Post-it: *a VWAP built from capped sizes is an average in which the biggest trades have been turned down to a whisper.*

The next three rows are one trade. A customer sold \$250,000 of bonds; the desk, acting as agent, passed them straight to another dealer, which bought them as principal. The customer leg is reported by the desk with capacity `A`; the interdealer leg is reported by both dealers, once as a sale and once as a purchase. One economic event, three rows, and a backtest that sums volume, or averages prices weighted by it, counts the same bonds three times.

The fifth row is not the desk's. A third dealer sold \$40,000 to a customer at 8.5125, which is 85.125 with the decimal point in the wrong place, typed by a person at the end of a long morning. It is not on Odile's queue, because it is not the desk's print. It is not on anybody's queue, because the third dealer's system saw a valid price and a valid size. It will sit in the public tape for as long as there is a public tape.

"Not mine," Odile said. "Not my problem. Your problem."

The sixth and seventh rows are a correction. The desk's trader had keyed the 09:47 sale an eighth too high. FINRA's historic file layout records a correction as two rows: one with status `C` that cancels the original, carrying the Prior Reference Number of the report it kills, and one with status `R` that replaces it. The eighth row is the one Kaz, who had drifted over with a second coffee, put a finger on.

"Status Y. Reversal." Kaz held up a hand before anyone could speak. "I know. Not a factor (§7.9). I have been told. Is it the appellate kind, then?"

"Closer than the factor," Theo said, and was surprised to find that it was. In FINRA's layout a reversal is the cancellation of a trade report submitted more than twenty business days earlier, flagged with an As-Of indicator of `R`. Like an appeal, it undoes a judgement after the period for ordinary correction has run out, and it is matched to the judgement it overturns on a list of particulars: the CUSIP, quantity, price, execution date and time, buy or sell, and the contra-party indicator. This one reversed a \$500,000 sale at 86 that the desk had reported on 29 September against Brambleworth's 2030s when the bonds sold were the company's 2028s.

"Twenty-ninth of September," Theo said slowly. "That's inside September's last five business days."

"So what?" said Kaz, who knew exactly so what and wanted to hear Theo say it.

"So September's month-end price for this bond just changed. Six weeks after September ended. And September's return, and October's, because October's return starts from September's price." He looked at the screen. "The history moved. Nobody touched it, and it moved."

That is the first thing a TRACE row teaches, and Theo felt it in the stomach before he could say it cleanly. The tape is not the market. It is a regulatory filing, assembled under a fifteen-minute clock by people with other jobs, and amended for weeks afterwards by cancels, corrections and reversals, some of which arrive after the month they change is closed. A backtest built on it inherits the exception queue: the desk's own queue, which Odile clears, and every other dealer's, which nobody on this desk will ever see. A quarterly refresh of the TRACE files is, among other things, a delivery of other people's corrections to your history.

Mags had listened from her chair, which faces the other way. "Back in my day the print was a Post-it on the squawk box," she said, "and it was *also* wrong. But at least it didn't pretend to seven digits."

## 9B.2 Stage 0, or a Week Spent Cleaning TRACE

> **View From Another Seat.** *The dealer's operations desk.* To the quant, TRACE is a dataset. To the person in Odile's chair it is a compliance obligation with a timer on it, and the timer, not the price, is what gets reviewed. Her performance is measured in late reports and capacity errors, not in whether the price a third dealer printed at 11:58 was sensible, so the incentives that produce the tape and the incentives that clean it belong to different people at different firms. A dealer's operations seat also sees what the quant cannot: the trade booked to the wrong CUSIP, the agency pass, the as/of filed because a system was down at 2:40. A systematic desk that sits inside a dealer (as this one does) can ask; a fund that buys the tape from a vendor inherits the answers without the questions. The general practice is drawn from FINRA Rule 6730 and from public accounts of the work; the seat itself is described generically.

Ines made the decision on Tuesday evening, and like most of her decisions it arrived as a question. "If the vendor's panel had a filter in it we didn't choose, how many filters are in the new one that we didn't choose?"

Nobody knew. So the desk would build the panel itself, from the raw tape, in the order the public pipeline publishes (the Stage 0 README of the Open Bond Asset Pricing `trace-data-pipeline`, pinned at v4.2.1, the September 2026 release), and every filter would get a row in a table with three columns: what it removes, what it could remove by mistake, and the date on which the desk chose it. The third column was Ines's. It had to be filled in before anyone computed a single return.

"Ex-ante or it didn't happen," Kaz said, and for one chapter that became the desk's motto, standing in for "IDO or it didn't happen," which took the week off.

ROBO did the building. Theo wrote the specs, one filter at a time, and the reader can watch each filter earn its place, because that is how the week went: slowly, with a lot of looking at individual rows.

**Wednesday.** Wednesday was Veterans Day, for which the bond market's trade association, SIFMA, recommends a full close and the New York Stock Exchange does not, so the floor was quiet and the pipeline's NYSE calendar insisted it was a business day. ROBO flagged the day for "anomalously low print counts," which was accurate and useless.

Step 0 normalised the price scale, because a feed that quotes per \$100 of par and one that quotes per \$1,000, or as a decimal of par, will hand you 85, 850 and 0.85 for the same bond on the same morning. Step 1 was the cleaning procedure that Jens Dick-Nielsen published for TRACE in 2009 and for Enhanced TRACE in 2014. The desk worked from the description in Dickerson, Robotti and Rossetti (2026), who apply it to remove cancellations, corrections, reversals and agency-side duplicates; nobody on the desk had the 2014 paper's own text in front of them that week, and Theo wrote that in the spec's margin rather than pretend otherwise. On Brambleworth's Monday, ROBO's step 1 turned eight rows into three: the corrected 09:47 sale at 85.125, the agency pass once, the 8.5125, and nothing at all for the September trade that had been reversed. The 8.5125 survived, because nothing in step 1 knows what a sensible price is. That is step 2's job.

**Thursday.** Step 2 is the decimal-shift corrector, and it is a small piece of judgement written down as arithmetic. For each bond it keeps an anchor, the median of the last eleven unique prices. A print is tested only if it misses the anchor by more than 5%. A tested print is multiplied in turn by 0.1, 0.01, 10 and 100, and a candidate is accepted if the corrected price lands within 2% of the anchor, or within 8 points of it, or with both the corrected price and the anchor inside 15 points of par; and two further conditions hold the corrector back: the corrected error is at most a fifth of the raw error, and the corrected price lies between 5 and 300. The 8.5125 missed an anchor of about 85 by 90%. Multiplied by 10 it became 85.125, a miss of under a fifth of a percent, comfortably inside every bound, and ROBO wrote the corrected price into the panel with the raw one beside it.

Theo liked step 2 more than he expected to. It is what a good associate does with a data room: treat the typo as a typo only when the corrected number agrees with everything around it. Steps 3 to 6 went quickly. The intraday time window is off by default, the NYSE calendar is applied, and prices are kept only above 0 and at or below 1,000. A volume screen that would drop trades under \$10,000 exists and is off by default, because small trades print on the wrong side of the spread more often than not, and throwing them away is a choice with a sign; the user makes it and writes it in the table.

**Friday.** Step 7 is the bounce-back filter, which looks for a print that jumps far from its neighbours and comes straight back. Its baseline is the median of the five prior unique prices. It triggers on a move of 35 points, measured three ways (a one-step jump, a displacement from the baseline, or a spike to exactly 100 that sits at least 8.75 points from the baseline), and it calls the print a bounce if the price returns within five rows. It also flags runs of three or more consecutive prints at exactly par.

The par runs made Mags turn her chair around. "Back in my day," she said, "there was a pricing service, which I will not name because it no longer exists and I would like to keep it that way, that marked a bond at par for eleven months. Not near par. Par. Nobody had traded it since the spring, the model needed a number, and the number it had was the one it was issued at. It was a lovely bond on the risk report. Flat as a lake. Lowest volatility in the book." She paused. "It was a shipping company's second-lien bond, and when it finally traded, it traded at 31." She looked at the line in Theo's spec that flagged three consecutive prints at exactly 100, and read it twice, which for Mags is a standing ovation. "Fine. That would have caught it in March."

Steps 8 to 11 are the dull ones that each turned out to have a story behind them. Step 8 drops a trade whose price equals its yield, because somebody typed 8.42, the yield, into the price field. Step 9 drops a trade larger than half the bond's offering amount, which is almost never a trade and almost always a booking error or an allocation reported strangely. Step 10 drops trades reported after the bond matured. Step 11 drops a bond whose first three prints are followed by a 50-point move, because a new bond's first prints are sometimes when-issued noise or the wrong scale entirely.

**Monday.** The daily stage is for distressed bonds, where a typo and a price can look alike. Over a five-day window it flags an ultra-low print below 0.10 (or a suspiciously round one) when the surrounding median is at least three times higher; an upward spike above 5.0 that is at least three times the prior median and falls back to within twice it inside five days; a plateau of two or more identical days below 0.15 or at round numbers; and an intraday range above 75% of the day's mean price when any price that day is below 20. Theo read the list and recognised the market it describes. A bond quoted at two cents on the dollar and a price of 0.02 typed by mistake are, to a computer, the same object. To Mags they are not, and the daily stage is an attempt to write down why.

**Tuesday.** On the following Tuesday ROBO built its first monthly returns, and Kaz, wanting a quick look before the full run, sent it a one-line instruction: *remove outliers from the monthly returns before the first test.*

ROBO did exactly that. It computed the absolute value of every bond-month return in the panel, took the top half-percent, and deleted them. It did not complain and it did not guess. It produced, as asked, a file of the deleted rows.

Mags read the file. It took her a while, because it was long, and she read it the way she reads a docket. "This isn't a list of errors," she said. "This is a list of defaults." The largest negative returns in a high-yield panel are not, mostly, typos. They are missed coupons, distressed exchanges and Chapter 11 filings: months like Windstream's February 2019, when the company lost its indenture case to Aurelius and filed for bankruptcy ten days later. (Which rows ROBO deleted is the desk's fictional run; Windstream's ruling and filing are on the public record.) A panel that deletes those months has deleted the left tail of every high-carry, high-value portfolio in it, and a value strategy built on that panel will look like a strategy that has never met a default, because it hasn't.

Here Theo knew more than anyone at the table, and it was a pleasant feeling he had not had in eight weeks. He had spent years explaining to clients why a defaulted bond trades flat. The pipeline's treatment matches what a restructuring banker would write. Bonds stay in the panel through default; a bond counts as defaulted when its numeric rating code reaches the default grade (22 on the pipeline's S&P scale, 21 on its Moody's scale). In the month of default no coupon is paid, so the return is next month's clean price divided by this month's price plus accrued interest, minus one: the holder paid for the accrued interest and will not receive it. After that the bond trades flat, with no accrued interest at all, and its monthly return is the change in its clean price alone. The lawyers, as Mags says, come later. The return series does not wait for them; it just keeps the bond.

By Tuesday night the table had fourteen rows, every one with a date in the third column earlier than the date of the first return, and ROBO's instruction from Kaz had been replaced by a line Theo wrote in capitals at the top of the spec: *no filter is defined in terms of the returns it will be used to test.* It was not a new idea. It was Chapter 7's look-ahead bias (§7.9) written as a constraint on a build, which is the only place a constraint ever does any good.

> **Ways This Blows Up.** *Two filters that are right nine times in ten.* **The decimal shift that erases a crash.** Suppose a bond has traded near 90 for months and, on a Thursday afternoon, the issuer discloses something terrible and the next prints are 9, 9.5 and 8.75. To the corrector each of those prints misses an anchor of 90 by about 90%; multiplied by 10 each lands within 2% of the anchor, with both prices inside 15 points of par and well inside the 5-to-300 band. A rule of this shape accepts the correction, and the crash disappears from the panel until enough low prints have passed through the eleven-trade median to move the anchor. If the disclosure comes in the last week of a month, the default shows up in the following month's return, which is a timing error in exactly the observation a credit model most needs. *(Illustrative; the pipeline's further checks may catch a given case, and the desk keeps the raw price beside every corrected one and reviews by hand any correction applied to a bond whose price has moved more than 50 points in a week.)* **The bounce-back that deletes a liability-management gap.** A 35-point drop that comes back within five rows is usually a fat finger. Occasionally it is a non-pro-rata uptier announced at 4 p.m. and partly walked back the next morning when the excluded holders' counsel calls, and the round trip is the most informative pair of prints the bond will ever produce (Chapter 13 reads those events as games). A filter that cannot tell the two apart will delete the information along with the typo. Both failures have the same cure: filters flag, people review, and the review is logged, so that a filter's mistakes become rows in a table instead of holes in a backtest.

## 9B.3 Two Prices, One Month

On the Thursday of the cleaning week, while ROBO worked through step 2, Kaz took the whiteboard to define the thing the whole panel exists to produce: one bond's return over one month. It sounds like the easiest definition in finance. It took most of the afternoon.

Start with what a "month-end price" can mean for a bond that does not trade every day, which is nearly every bond. In 2022, by the count in Dickerson, Nozawa and Robotti (2025), about 70% of 29,543 bonds traded on ten or fewer days of the year, and 109 of them, 0.4%, traded every day. So the pipeline defines the month's price as the last daily volume-weighted average price in the month's final five NYSE business days. If a bond printed on the 30th, its month-end price is the 30th's VWAP; if it last printed on the 24th, the 24th's VWAP stands in for the month, already a few days old. A bond with no print in those five days has no month-end price, and no return that month.

Kaz wrote the return the way the pipeline does, with $P$ the clean price, $AI$ the accrued interest and $C$ any coupon paid during the month:

$$
r^{\text{End}}_{i,t+1} \;=\; \frac{P^{\text{end}}_{i,t+1} + AI_{i,t+1} + C_{i,t+1}}{P^{\text{end}}_{i,t} + AI_{i,t}} \;-\; 1 .
$$

Then Kaz wrote a second one, the *month-begin* return, which keeps the same ending price but starts from the first price observed in the first five business days of the new month, $P^{\text{bgn}}_{i,t+1}$, typically about one business day after the month-end price (the median gap in the 2026 audit is one business day):

$$
r^{\text{Bgn}}_{i,t+1} \;=\; \frac{P^{\text{end}}_{i,t+1} + AI_{i,t+1} + C_{i,t+1}}{P^{\text{bgn}}_{i,t+1} + AI^{\text{bgn}}_{i,t+1}} \;-\; 1 .
$$

Divide the first by the second and the ending price cancels. What is left is the gap: the move from the month-end price to the first price of the next month. To a close approximation,

$$
r^{\text{End}}_{i,t+1} \;\approx\; \underbrace{\frac{P^{\text{bgn}}_{i,t+1}}{P^{\text{end}}_{i,t}} - 1}_{\text{gap return}} \;+\; r^{\text{Bgn}}_{i,t+1} .
$$

> **Math, Gently.** *A return has two prices, and only one of them is yours.* A bond is marked at 98 at Friday's close. On Monday morning, the first moment anybody could act on Friday's information, it trades at 99. The following Friday it closes at 100. The Friday-to-Friday return is $100/98 - 1 = 2.04\%$. The Monday-to-Friday return is $100/99 - 1 = 1.01\%$. The difference is the weekend gap, $99/98 - 1 = 1.02\%$, and the pieces multiply back together: $1.0102 \times 1.0101 = 1.0204$. Now suppose your signal was computed from Friday's 98. You could not have bought at 98: by the time you knew the signal, the price on offer was 99. The 2.04% is the bond's return; the 1.01% is yours. A backtest that books the 2.04% has paid itself the gap, and if the gap is related to the signal (which, §9B.4 shows, it is whenever the signal is built from the same 98), it has paid itself a strategy. The full version, with noise, is the correlated-errors box in §9B.4 and the derivation in §7.9.

Theo had his USB stick on the desk, as he always does, and he plugged it in, because something on the whiteboard looked familiar. His 13-week cash flow model, the one from PJT, has a row called *cash at start of week* and a row called *cash at end of week*, and week two's opening balance is week one's closing balance, by formula, one cell doing two jobs.

"Same shape," he said. "The month-end price is September's closing balance and October's opening balance."

"Same shape," Kaz agreed. "Is your model ever wrong about it?"

"Never. It ties to the bank statement every Friday." He heard himself say it, and the sentence went on sounding in his head after he stopped talking.

The rest of the afternoon went on the benchmark, which is the second choice hidden inside "a bond's return." The 2026 audit's headline results subtract the one-month Treasury-bill rate, the convention borrowed from equities. Andreani, Palhares and Richardson (2024) argue that this is the wrong convention for bonds: a corporate bond's return has a rate component and a spread component, the two are negatively correlated, and subtracting a T-bill leaves the rate component in what you are calling the credit return, which contaminates inference most for investment grade and for anything measured through time. Van Binsbergen, Nozawa and Schwert (2025) propose the fix that most of the field now uses: subtract the return of a Treasury position with the same duration,

$$
r^{\text{ex,dur}}_{i,t+1} \;=\; r_{i,t+1} \;-\; r^{\text{TSY}}_{t+1}\!\big(D^{\text{mod}}_{i,t}\big),
$$

where $r^{\text{TSY}}_{t+1}(D)$ is built by interpolating key-rate Treasury returns linearly on the bond's modified duration at the start of the month. On that measure, they find, investment-grade bonds earn a small credit premium, about the size of a convenience yield, and the bond CAPM's apparent failures for IG largely go away. The Open Bond Asset Pricing site ships duration-matched Treasury returns contributed by Yoshio Nozawa, so the desk did not have to build its own. A tiny number makes the stakes concrete *(illustrative)*: in a year like 2022, a seven-year BBB bond can lose 10% while T-bills pay 1.5%. Against the T-bill its "excess return" is about −11.5%, nearly all of it the rate shock; against a seven-year Treasury that lost 9%, its excess return is about −1%, which is the part a credit model is supposed to explain. Chapter 8 (§8.2) makes the companion point about empirical duration: the rate sensitivity a bond actually shows in a sell-off is not always the one its cash flows promise.

One last piece of arithmetic answered a question Hana had asked on Monday. The panel runs from August 2002 to December 2024, which is 269 months of prices. The audit's return tables report $T = 268$, and the difference is not an error: 269 prices produce 268 returns, because the first month supplies only a starting price.

![Figure 9B.1: One bond, one month-end, two prices. The month's price is the last daily VWAP inside the final five NYSE business days (shaded); the signal price, in the gap version, is read one to ten business days earlier; the month-begin price is the first print in the next month's first five business days, a median of one business day later. The shaded wedge between the month-end price and the month-begin price is the gap return, which a month-end-to-month-end return books and a month-begin return does not. Illustrative prints; definitions from Dickerson, Robotti and Rossetti (2026), arXiv:2604.07880, and the trace-data-pipeline README.](assets/figures/ch09b_two_prices.png)

## 9B.4 The Noise in the Denominator

The sentence that kept sounding in Theo's head was *it ties to the bank statement*, and it finished itself that evening, while he was reading ROBO's draft schema for the panel.

The schema had a column called `prc_m`, the month price. It fed two other columns. One was `cs`, the credit spread, computed from the yield at `prc_m`, which is the input to every value signal on the desk, including the credit-spread value signal `val_ipr`, the one survivor Theo had decided in Chapter 4 to trust. The other was `ret_base`, the denominator of next month's return. One column, two jobs, exactly like the cell in his 13-week model.

The difference was the bank statement. In his model, the shared cell is fine, because the number in it is reconciled to an external truth every week; if the closing balance is wrong, the bank tells you on Monday. A bond's month-end price has no bank statement. Its error is never observed, only inherited. And an unobserved error that sits in the signal and in the return denominator does something specific: a bond whose month-end price is recorded too low looks cheap, so a value sort buys it; next month its return is measured from the too-low base, so it "earns" the error back as the next price is drawn fresh. The value signal and the return are not two measurements of the bond. They are one measurement, used twice, with opposite signs.

At PJT this would have been a familiar sin in another costume. You do not let the company's own projections be the evidence that the company's projections are reasonable, because then the question and the answer are the same document. Here the question (is this bond cheap?) and the answer (did it outperform?) were the same price.

He wrote it on a Post-it, *one price, two jobs*, and stuck it to Kaz's monitor. Kaz read it on Friday morning and wrote a second line underneath: *the noise in the denominator is the alpha in the numerator.*

Chapter 4 and Chapter 7 both drew the two-bond version of this on a whiteboard: true returns of zero, month-end noise of plus or minus half a percent, and a long-short return of 1.00% a month from nothing. What the desk needed on Friday was the version for a real sort of thousands of bonds, because the size of the bias in a decile portfolio is not the size of the bias in a pair, and Dickerson, Robotti and Rossetti's Theorem B.1 gives it.

> **Math, Gently.** *Correlated errors-in-variables, or why finer sorts find more noise.* An "errors-in-variables" problem is a measurement error in something you are using to explain something else; it is *correlated* when the same error also sits in the thing being explained. Here is the picture. Rank 6,000 bonds on a signal built from a noisy price, and cut the ranking into ten buckets. The top bucket is, partly, the bonds with the most negative noise, because negative noise makes a bond look cheap; the bottom bucket has the most positive noise. How extreme those buckets are depends on how finely you cut. If the signal is roughly bell-shaped, the average standardised score of the top bucket is about 1.09 for a three-way split, 1.40 for a five-way split and 1.75 for a ten-way split: finer sorts dig deeper into the tails, and the tails are where the noise lives. Call that average $\kappa$, call the correlation between the signal and the noise $\rho$, and call the size of the noise $\sigma_\delta$. The long bucket carries average noise of about $-\kappa\rho\sigma_\delta$ and earns it back next month; the short bucket carries $+\kappa\rho\sigma_\delta$ and gives it back. The long-short "premium" from noise alone is the difference. Tiny number *(illustrative)*: with $\sigma_\delta = 0.5\%$ and $\rho = 0.3$, a decile sort manufactures $2 \times 1.75 \times 0.3 \times 0.5\% \approx 0.53\%$ a month; a tercile sort, $0.33\%$. The two-bond whiteboard example is the special case where the signal is pure noise ($\rho = 1$) and each "bucket" sits exactly one noise unit from the middle ($\kappa = 1$): $2 \times 1 \times 1 \times 0.5\% = 1.00\%$. The paper's statement of the result is next; the covariance algebra behind it is in §7.9.

In the paper's notation the bias is

$$
\text{LIB} \;=\; 2\,\kappa\,\rho\,\sigma_\delta ,
$$

with $\kappa$ a normal-tail constant that grows with the fineness of the sort and $\rho$ the strength of the link between the noise and the signal. (Reading $\kappa$ as the mean of the extreme bucket of a standard normal, as the box does, is this book's stylised reading of the theorem.) Three consequences follow, and the 2026 audit measures each. The bias belongs to price-based signals: a signal built from a rating or an estimated beta has no month-end price inside it, and in the audit's placebo test (read in Chapter 7 §7.2) the gap matters for far fewer non-price factors. The fix is cheap: read the signal from a price one to ten business days *before* the month-end price (a signal gap), or start the return from the month-begin price (a return gap), and the sort and the return no longer share a draw of noise. And the bias can be measured directly, because it is the gap return. In the audit, the correlation between $r^{\text{End}} - r^{\text{Bgn}}$ and the estimated bias is 0.99 across factors (0.93 to 0.98 within firms). The thing Kaz drew on Thursday afternoon as a wedge between two prices *is* the bias, to two decimal places.

Then Theo put up Table 1 of the audit, value-weighted decile long-short portfolios over 2002–2024, monthly, gross of costs, and read it the way he used to read a waterfall, from the top down *(numbers from Dickerson, Robotti and Rossetti 2026, Table 1)*. Yield to maturity: a premium of 1.20% a month unadjusted, 1.05% with a signal gap, 0.92% with a return gap. Credit spread: 1.13%, 0.96%, 0.82%. Bond book-to-market (par over price): 0.93%, 0.75%, 0.66%. The six-month spread change: −1.02%, −0.50%, −0.46%. Houweling and van Zundert's value signal: 0.81%, 0.45%, 0.43%, with its alpha falling from 0.47% to 0.12% ($t$ of 1.13). And the one Theo cared about, `val_ipr`, the Israel–Palhares–Richardson residual-spread value signal: a premium of 0.96% falling to 0.51% under either gap, and a CAPM-B alpha falling from 0.76% to 0.31% ($t$ of 2.12) with the signal gap and to 0.33% ($t$ of 2.61) with the return gap. At the bottom of the page sat short-term reversal, −0.99% falling to −0.09%, which Hana had met in person in §9.9 and which she did not need to see again. She looked at it anyway, said nothing, and on this desk that is a form of solidarity.

Across the table the bias takes more than 80% of the reversal premium, 45–55% of the value and spread-change premia, and 20–50% of the yield and spread premia, and it is larger again in within-firm sorts. Value lost about half and lived. That was the good news, and Theo took it, with the reservation Ines added before he could get attached to it.

"The month-begin price is one business day later," she said. "Median. That's the earliest you could have traded, not the price you'd have got. If you'd taken a week to work the order, you'd have paid more of it away." That is the open half of the debate, and the audit says so: part of what it calls a bias is a real implementation wedge, because the month-end print was never executable, and the one-day gap is a floor on that wedge, not a measure of it. Dickerson, Nozawa and Robotti's work on trading delays (2025) finishes the thought, and §9B.9 applies it.

![Figure 9B.2: The same seven price-based factors three ways: unadjusted (signal and return share the month-end price), with a signal gap (signal read one to ten business days earlier) and with a return gap (return starts at the month-begin price). Short-term reversal collapses from −0.99% to −0.09% a month; the value and spread family loses roughly half; val_ipr keeps a significant alpha. Value-weighted decile long-short premia, monthly, US corporate bonds, TRACE, 2002–2024, gross of costs; t-statistics above the bars. Source: Dickerson, Robotti and Rossetti (2026), arXiv:2604.07880, Table 1.](assets/figures/ch09b_lib_waterfall.png)

> **Poker Table.** *The card in your hand and on the board.* Ines's version took one sentence. "If the same card is in your hand and on the board, the deck is marked, and your two pair is one pair counted twice." A month-end price that sets the signal and starts the return is that card. Her hand history, the replay she insists on for every adverse-selection lesson, is the gap decomposition: deal the same hand again with the board turned one day later, the month-begin price, and see what is left. For reversal almost nothing is left; for value, half. The difference between the two deals correlates 0.99 with the bias, which is a poker player's way of saying the difference *is* the bias. In Chapter 4 she called it "the part of your alpha that belonged to someone else." Here it is the part that was never anybody's.

## 9B.5 The Filter That Knew the Future

On Monday ROBO finished the first full run on the new build, and the reference line for six-month momentum came out at 0.22% a month with a $t$-statistic of 1.1, the number from the cold open. The new build had reproduced Tuesday's mystery. That told the desk the new number was the build's number. It did not tell them where the old one had come from.

Mags asked, because she always asks. She is suspicious of anything called "adjusted," and the legacy panel's documentation used the word four times on its first page. "Somebody chose a ninety-nine-point-five," she said, pointing at a line in the vendor-panel README. "Who chose it, and when?"

Kaz had chosen it. Last year, building the vendor panel, Kaz had winsorized returns at the 0.5th and 99.5th percentiles of the full sample, 2002 to 2025, and in the rerun week of Chapter 4 Kaz had found that and fixed it, in the research notebook. The production file the library read every night had been built once, a year earlier, with the winsorization baked into the stored returns. The library's five thousand lines never winsorized anything. They did not need to; the data arrived pre-trimmed. When DATA-3311 pointed the library at the new build, the trimming disappeared, and the number moved from the winsorized value to the untrimmed one.

"I fixed it in the notebook," Kaz said. "I never fixed the file."

It is the most ordinary sentence in quantitative finance, and the reason the risk committee asks its question. Then Theo put the two numbers next to the 2026 audit's Table 4, and they matched. For six-month momentum, value-weighted deciles, the audit reports a CAPM-B alpha of 0.46% a month ($t$ of 2.39) with full-sample winsorization and 0.22% ($t$ of 1.08) without. The desk had been rerunning a published table every night for a year, without knowing it, from the wrong side.

> **Math, Gently.** *Winsorizing with hindsight.* To winsorize a return series at the 99.5th percentile is to replace every return above that percentile with the percentile itself; to trim is to delete them instead. The trouble is the word *percentile of what*. The panel holds roughly 6,790 bonds a month for 268 months, about 1.8 million bond-months. The top half-percent of those is about 9,100 bond-months, and the threshold that separates them is set by whatever months were wildest, which in this sample means the rebounds of 2009 and of April 2020. Computing that threshold once, over the whole sample, and applying it to a return from 2005 means clipping 2005 with a ruler cut in 2020: a researcher in 2005 would have needed to know how big the 2020 returns were going to be. An *ex-ante* filter decides which bonds to drop using only what was known on the formation date (the bond's price and its return up to that month), judged against thresholds fixed in advance; an *ex-post* filter edits the very return the signal is trying to predict, and a full-sample percentile is ex post twice over. Tiny number *(illustrative)*: if a past loser rebounds 60% in April 2009 and the full-sample 99.5th percentile is 25%, a full-sample winsorization turns a 60% loss on the short leg into a 25% loss, a gift of 35 points that nobody trading in April 2009 could have received. The formal statement, the look-ahead bias as the trimmed amount summed over the long leg minus the short leg, is in §7.9.

Kaz then did the thing the desk's harness now does for every candidate signal, and which the audit does in its Figure 6: rebuild six-month momentum under many trimming rules and draw the alpha as a function of the threshold. Four lines: screen out the right tail ex ante, on the return a bond had already earned by the formation date; the same for the left tail; then trim the right tail ex post, cutting extreme values of the holding-month return the signal is trying to predict; and the same for the left tail.

The two ex-ante lines lay on the floor. Under any ex-ante trimming of either tail, six-month momentum's alpha is statistically indistinguishable from zero. The ex-post right-tail line rose as the trimming tightened, to about 0.60% a month when every return above 10% in a month was cut. The ex-post left-tail line went the other way: the alpha turned negative, and it climbed back to zero only when the threshold was loosened to about −40%. *(The curves are the audit's, for March 2003 to December 2024, read from its Figure 6; the desk's run is fictional and drew the same shape.)*

Theo asked why the right tail, and the answer is the most intuitive thing in the chapter. A momentum portfolio is short last half-year's losers. The biggest months a loser ever has are rebounds: the junk rally of spring 2009, the weeks after the Fed's facilities of March and April 2020. Those rebounds are the momentum crash, they land on the short leg, and they sit in the right tail of the return distribution. Trim the right tail after the fact and momentum never crashes. Trim the left tail after the fact and the strategy loses the losers' further collapses, which were its short leg's profit, and the premium turns negative. The audit's look-ahead bias for momentum sits in the short leg, spikes in 2008–09, 2011–12 and March 2020, rises more than proportionally with the VIX, and is two to three times larger in high yield than in investment grade. A filter that knew the future knew it best in exactly the months the strategy most needed not to know.

The same audit table holds the shorter momentum horizons and the longer one, and they tell the same story. Three-month momentum's premium is 0.33% a month winsorized and 0.17% without; twelve-month momentum's is 0.26% winsorized and −0.13% without, with alphas of 0.46% and 0.14% ($t$ of 1.60 and 0.51). This is the canonical claim of Jostova, Nikolova, Philipov and Stahel (2013), whose 1991–2011 momentum profits averaged 59 bp a month across all bonds and 192 bp in high yield, from a sample that combined TRACE with dealer quotes; the audit lists that paper among those using the 99.5th-percentile winsorization. Chapter 10 (§10.1 and §10.5) inherits the conclusion: in the TRACE era, price momentum in the cross-section of bonds does not survive an ex-ante filter, and the momentum that does survive is a different animal, which §9B.7 meets.

Risk factors have the opposite problem. Factors built on idiosyncratic volatility or downside risk are long the riskiest bonds, so their bias sits in the long leg, and their significance depends on trimming the *left* tail, which deletes the defaults those risky bonds were being paid to bear. In the audit's Table 4, an idiosyncratic-volatility factor has an alpha of 0.53% a month ($t$ of 2.58) winsorized and 0.18% ($t$ of 0.72) without; an expected-shortfall factor, 0.74% against 0.31% ($t$ of 1.42); a value-at-risk factor, 0.56% against 0.24% ($t$ of 1.42).

![Figure 9B.3: Six-month bond momentum's CAPM-B alpha as a function of the trimming threshold, four ways. Ex-ante trimming of either tail leaves the alpha indistinguishable from zero at every threshold; ex-post right-tail trimming lifts it to about 0.60% a month at a 10% monthly cut-off; ex-post left-tail trimming turns it negative, and it returns to zero only near a −40% cut-off. Value-weighted deciles, US corporate bonds, March 2003 to December 2024, gross of costs. Redrawn from Dickerson, Robotti and Rossetti (2026), arXiv:2604.07880, Figure 6 (pp. 25–27); only the anchor points stated in the text are taken from the paper, and the curves between them are schematic.](assets/figures/ch09b_mom6_trimming.png)

> **Desk Myth vs. Desk Reality.** *Myth:* the four-factor bond model of Bai, Bali and Wen (2019), in the *Journal of Financial Economics*, is the standard benchmark for corporate-bond alpha. *Reality:* it was retracted; the notice is *JFE* 150(3), article 103721, December 2023. By the account Alessandro Robotti gave in a Warwick Business School post of 10 September 2024, the factor data had "lead" errors in two of the factors and a "lag" error in a third, extreme losses had been filtered out after the fact, and once corrected the four-factor model added nothing beyond the bond CAPM; the post calls it the first retraction of its kind at the journal and notes that the paper had been cited more than 400 times. The book states the retraction and the errors and nothing about anyone's intent. For this section, the point is narrower: the downside-risk factors from that line of work, value-at-risk and expected shortfall, are on the audit's list of factors whose significance needs ex-post left-tail winsorization (alphas of 0.56% and 0.74% a month winsorized, 0.24% and 0.31% without). Open Bond Asset Pricing publishes the four factors rebuilt with the errors corrected, and the desk's `obap_repro` job (§9.9) reproduces them every night. A vendor or client "four-factor bond model" built on the original series is contaminated, whatever it is called in the pitch book.

By Monday evening Kaz had rebuilt the production file without the winsorization, filed DATA-3312 to delete the old one, and added a line to the panel's choice table: *return trimming: none in the stored panel; any trimming is ex ante and lives in the harness, where it is reported.* Mags read it and said nothing, which from her, about a sentence containing the word "trimming," is as close to approval as the language allows.

## 9B.6 The Zoo, Counted Honestly

The model review met on Wednesday at ten, in the room with the good chairs, and the minutes record its chair only by initials, which is how he prefers it. He asked the question. Theo answered in three sentences: the stored file had a full-sample winsorization in it that nobody had chosen this year; the new build has none, and records every filter with the date it was chosen; and the two numbers on page three are the published winsorized and unwinsorized alphas for six-month momentum, to the second decimal. The chair wrote for a while. Then he asked the question that matters more: "And the other hundred and seven?"

Chapter 4 put the audit's scoreboard on the screen (Figure 4.3): 108 signals built four ways, 432 specifications, 65 with a CAPM-B alpha $t$ above 1.96, 26 (6.0%) surviving the Benjamini–Hochberg false-discovery correction run within each of the four panels (the procedure is in the box in §7.2), 25 of the 26 within-firm sorts, and bond age, equal-weighted, the only survivor that sorts across the whole market. What the committee wanted was the list itself, with sizes, because a survivor is a number and not a word *(annualised CAPM-B alphas, gross of costs; Dickerson, Robotti and Rossetti 2026, Internet Appendix IA.3; an asterisk marks a signal whose sign is flipped so the premium is positive)*:

| Survivor (within-firm) | Weighting | Alpha, % a year | $t$ |
| :-- | :-- | :-- | :-- |
| Six-month spread change, `dcs6*` (a reversal within the issuer) | EW / VW | 2.46 / 2.66 | 6.77 / 4.98 |
| Residual-spread value, `val_ipr` | EW / VW | 2.30 / 2.22 | 5.03 / 4.25 |
| Residual-spread value within DTS quintiles, `val_ipr_dts` | EW / VW | 2.23 / 2.47 | 5.51 / 4.50 |
| Systematic 12-1 momentum, `sysmom12_1*` | EW | 2.20 | 3.04 |
| Residual 12-1 momentum, `idimom12_1` | EW | 1.55 | 2.94 |

The rest of the 26 are betas (to the market's up-moves, co-skewness, illiquidity, volatility and macro uncertainty), measures of the shape of a bond's own return distribution (skewness and jumps), a DTS-demeaned version of Houweling and van Zundert's value signal, plus yield and age. Three absences matter as much as the presences. Nothing from the illiquidity cluster survives (five direct measures of how illiquid a bond is show no alpha), and nothing from the credit-and-default cluster. The value-weighted single sort of `val_ipr`, the version a long-only desk could actually hold, earns 3.71% a year with a $t$ of 2.12: past the old bar of 1.96, short of the corrected one. And none of the seven price-based single sorts of §9B.4 has a significant adjusted alpha inside investment grade or inside high yield taken separately; the best is Houweling and van Zundert's value signal in high yield, 0.37% a month, $t$ of 1.91.

The chair's last question was the one the desk had come to answer. "How sure are they?" The honest reply is a second kind of error bar, and it is the most useful idea in the audit.

> **Math, Gently.** *Non-standard errors: the spread between careful people.* A standard error measures how much an estimate would wobble if history had dealt a different sample: it is uncertainty across *time*. A non-standard error measures how much the estimate wobbles when different careful researchers make different defensible choices on the *same* data: which tail to trim and how far, which price range to keep, which bounce filter to use, whether to weight by value or equally. Menkveld and coauthors (2024) measured it by handing one dataset and one set of hypotheses to 164 research teams and recording how far apart their answers landed. The 2026 audit adapts the idea: build each signal along many defensible paths and report the interquartile range of the resulting premia, the width of the middle half. Picture fifty analysts estimating the same premium; the standard error is how sure each of them is, and the non-standard error is how much they disagree. Tiny number: if the middle half of the paths spans 0.10% to 0.45% a month, the non-standard error is 0.35%, and a premium of 0.33% sits inside its own disagreement. The full construction is the paragraph after this box.

The audit builds two families of paths. The *data* paths vary only the cleaning: 108 ex-ante filters (48 return-trimming rules, sixteen thresholds applied to the left tail, the right tail or both; 30 price ranges; 30 bounce filters), each run equal- and value-weighted, on all bonds, investment grade only and high yield only: 648 paths per signal, 69,984 in all. Across them, the non-standard error of the premium averages 0.35% a month, against an average premium of 0.33%; for the alpha, 0.27% against 0.15%; and the non-standard error is 1.15 times the ordinary standard error. The *construction* paths vary the portfolio recipe (terciles, quintiles or deciles; breakpoints from all bonds, investment grade or large bonds; weighting; rating group; maturity bucket): 168 admissible paths per signal, 18,128 series. Their non-standard error is 0.31% against a mean premium of 0.22%, 1.45 times the standard error (from 1.02 for market-risk factors to 2.00 for spreads, yields and size). For 12 of the 36 top factors the premium changes sign somewhere along the paths, and for 29 the alpha does. In 94% of variations the baseline alpha does not improve. Value is the exception that keeps showing up: it is the one cluster with a detectable baseline premium and the one where cleaning choices often help (21% of the left-tail paths and 15% of the symmetric-trimming paths improve its alpha).

Kaz turned this into a sentence for the minutes that Chapter 7 had already earned. The deflated Sharpe ratio of §7.8 asks how many trials stand behind a result; for a bond factor built on TRACE, the honest count is at least the 648 data paths that a careful person could have walked, not 1. Law 12 of Appendix E, *count your trials*, has a number for credit now.

The committee did not leave pessimistic, and the desk did not want it to. Three results sat on the other side of the scale, and Theo put them up last. Jensen, Kelly and Pedersen (2023) find that most *equity* factors replicate, cluster into 13 themes and work out of sample across 93 countries; the bond problem is data quality, not the idea of factors. Ghaderi, Plante, Roussanov and Seo (NBER Working Paper 35578, August 2026) reconstruct 128 years of US corporate bonds and find a sizable, significant credit risk premium over the long sample, which suggests that 22 TRACE years have low power: a factor that fails in 268 months has not been proved absent. And Dick-Nielsen, Feldhütter, Pedersen and Stolborg, an independent team with different data and different cleaning (they review outliers one at a time and keep default returns), reach the same direction by a different road: in QuantPedia's summary of their paper, only 23% of literature-significant factors keep significant alphas in their framework, and they reject the bond CAPM that the 2026 audit uses as its benchmark. Two teams, two mechanisms, one direction, and a disagreement about the null that §9B.9 returns to.

> **View From Another Seat.** *The systematic asset manager.* The practitioner template for credit factors was published from inside one: Houweling and van Zundert, writing from Robeco, showed in 2017 (*Financial Analysts Journal*) that size, low-risk, value and momentum portfolios earned significant alphas and combined well. The 2026 audit's rebuild of their value leg is the clearest published haircut on that template: a premium of 0.81% a month falling to 0.45% ($t$ of 2.29) once the signal reads an earlier price, with the alpha down to 0.12% ($t$ of 1.13). How any manager's live portfolios have fared is that manager's business, and this book does not speak for Robeco. The seat's general advantage is worth naming, though. A manager that has traded a factor for years owns something no backtest has: its own fills, which are month-begin prices by construction. Its question about the audit is not "is the premium real?" but "did our executed prices look like $r^{\text{Bgn}}$ or like $r^{\text{End}}$?", and it can answer from its own blotter.

> **Trend Watch.** *The bond-data ledger, 2023–2026, dated.* **December 2023:** the Bai–Bali–Wen retraction notice, *JFE* 150(3), 103721. **23 July 2025:** Dickerson, Nozawa and Robotti, "Factor Investing with Delays," Hitotsubashi IER Discussion Paper A771: of 58 bond factors with significant gross returns, average alpha 0.28% a month falls to 0.09% (large trades) and 0.05% (small) after delay and bid–ask costs. **November 2025:** Open Bond Asset Pricing launches its open panels and factor files (Chapter 9 §9.9). **11 December 2025:** the pipeline's Stage 1 enters public beta. **6–9 April 2026:** "The Co-Pricing Factor Zoo" (arXiv:2604.04430), "Priced risk in corporate bonds" on arXiv (2604.05699) and the replication-crisis audit itself (arXiv:2604.07880, 9 April). **August 2026:** NBER Working Paper 35578, the 128-year bond panel. **September 2026:** pipeline v4.2.1 (MIT licence; about five hours and 5 GB end to end, with WRDS access to TRACE, FISD and ratings), and on **24 September** PyBondLab 0.3.0 (MIT, Python 3.11+), the portfolio-sorting library built around the same conventions. *What it means for the desk:* in three years the field went from a retracted benchmark to an open, versioned pipeline with its own test suite; the audit itself is under revise-and-resubmit and has not yet been reproduced end to end by a second team, so a desk pins the version it used and says so. One gap is still open: the OBAP site states no data licence, while the code repository is MIT.

## 9B.7 The Residual Is the Signal

*The scene below is a fictional composite. Vantress Capital Management, Wen Zhao, the pod's positions and the desk's runs are invented; the papers, their numbers and the borrow-market statistics are cited.*

Ines's desk had known Dov Adler's pod for two years as a stream of RFQs. On Thursday at 5:15 p.m. one of its analysts arrived in person, which is rarer than it should be. Wen Zhao had a printout of the audit's survivor list, forwarded by Marcus Oyelaran from the platform's risk team (Marcus and Ines are in contact, Chapter 28), and a second printout, which she called the weather: the pod's borrow sheet, one row per borrowed bond, with the lender, the fee, the share of the lender's inventory already out on loan, and a column no feed provides, two years of recall history.

"Your list and my sheet," she said, "have the same shape."

She was right, and it took the desk a minute to see why. A within-firm sort, the construction behind 25 of the 26 survivors, takes every issuer with at least two bonds outstanding, ranks that issuer's bonds against each other on the signal, goes long the top-ranked bond and short the bottom-ranked one, and then averages across issuers. Each issuer contributes a pair. The survivor list is a list of same-issuer pairs, equal-weighted, rebalanced monthly, and the pod's book, where it is not cross-issuer, is a book of same-issuer pairs held for a thesis.

The momentum survivors read differently once you see them as pairs. Residual 12-1 momentum, `idimom12_1`, is built by regressing each bond's returns on the bond market over a rolling 36 months (12 at minimum), the residual-momentum construction of Blitz, Huij and Martens, and summing the residuals over months $t-11$ to $t-1$. Within an issuer, the bond whose *own* part of its return has been strongest keeps outperforming its siblings: 1.55% a year, $t$ of 2.94, an information ratio of 0.87, equal-weighted. Its twin, systematic momentum `sysmom12_1`, sums the fitted market part instead, and the sign runs the other way: within an issuer, the bond that rode the market hardest underperforms, 2.20% a year once the sign is flipped. The strongest survivor of all, the six-month spread change, is not momentum but its opposite: within one issuer, the bond whose spread tightened most over six months earns less next month. Plain price momentum, industry momentum (a value-weighted single-sort alpha of 3.4–4.5% a year with a $t$ of 2.1–2.4) and short-term reversal fail the correction.

Theo said the obvious thing, because it had become obvious only as he said it. "Everything that survives is a residual. The issuer cancels, the market cancels, and what's left is one bond against its sibling. The literature's survivor is your trade."

"It's my trade gross," Wen said. "Show me the short leg."

The short leg is where the audit stops and the pod begins, and the paper says as much: every survivor is gross of costs, including the cost of shorting bonds and of running same-issuer pairs. A within-issuer residual-momentum short is the issuer's laggard, which is disproportionately the small, old, off-the-run bond. That is the profile of an expensive borrow. In the one large study of the bond loan market, Asquith, Au, Covert and Pathak (2013) find fees roughly flat near 30 bp until about 70% of a lender's inventory is on loan and rising steeply after, and 173 to 245 bp around bankruptcy filings; Nashikkar and Pedersen find fees highest for risky, low-rated, small and old bonds; and every loan is recallable on demand. Wen added her own column to the survivor list in pencil, recalls in two years on a bond like each issuer's short leg, and put a mark beside the ones she would not touch.

"So who can trade it?" Theo asked.

"Someone who already pays for the borrow for other reasons," Wen said. "We have a prime broker, a lender list and a weather sheet because of our other pairs. The survivor is cheap for us at the margin and expensive for anyone starting from zero." Then she asked her platform's question of it, the one Marcus asks every morning: what would forty of these pairs be long that they did not mean to be? Residuals are not as independent as their name suggests; Collin-Dufresne and coauthors found bond residuals highly cross-correlated, mostly through one latent factor (Chapter 7-B reads the test). In the desk's fictional run of the residual-momentum pairs, the long legs leaned toward the shorter bonds in each issuer more often than chance, which is a bet on the shape of issuers' curves wearing a residual's clothes. It was small. It was not zero.

> **View From Another Seat.** *The multi-strategy pod.* A pod reads the survivor list as a sourcing tool, not a strategy. The platform pays it for idiosyncratic P&L it could not buy through an index, and a within-firm sort removes the issuer and the market by construction, which is exactly what the platform wants to see on the x-ray. What the pod adds is the part the paper leaves out: a borrow it can find, a stop it can size to (Chapter 8-B), and a thesis sentence for the pairs it keeps, so that the residual it is paid for is one it can explain. Described generically; Vantress is a fictional composite.

> **The Pair.** *Pair Book PB-03, read as data, and an unnumbered within-issuer pair. Dov Adler's pod at Vantress Capital Management is a fictional composite; Brambleworth Packaging is a fictional issuer; PB-03's legs are the real Ford Motor Credit and GM Financial notes of the 2020 replay (Chapter 8 §8.4, closed in Chapter 24 §24.7); every price and P&L figure is illustrative.* **PB-03, the data lesson.** When Wen rebuilt PB-03's March 2020 history on the clean panel, nothing about the hedge changed and nothing about the idio changed. What changed was one day: the Ford Credit leg had printed a small lot several points low and the GM Financial leg a small lot several points high, and both had snapped back the next morning. On a long Ford, short GM pair, both prints register as losses, and both reversals as gains: two fake returns of opposite sign on two legs, adding up to one large fake round trip in the pair. A daily pair series built from such prints acquires manufactured mean reversion, and a half-life fitted to it (the Ornstein–Uhlenbeck fit of Chapter 7-B) comes out too short. The fix is the chapter's fix applied leg by leg: each leg gets its own signal price and its own return price, and neither is a print the bounce-back filter has flagged. **The within-issuer pair.** *Legs:* long \$10mm market value of Brambleworth's 8% 2030s at 85 (spread duration 3.4, spread 700 bp), the top-ranked bond on residual momentum; short Brambleworth's 2028s at 92 (spread duration 1.8, spread 600 bp), borrowed. *Sizing:* DTS-neutral as in §8.4, so the short is $10 \times (3.4 \times 7.00)/(1.8 \times 6.00) \approx$ \$22.0mm market value, about \$23.9mm face. *What the hedge removes:* Brambleworth's spread beta, to first order, and with it the market's. *What idio remains:* the 2030s' residual against their sibling, the thing the survivor list says persists. *What leaks:* three things. The issuer's curve shape, because DTS-neutral is not curve-neutral. The default jump, because the two bonds are pari passu and recover the same amount per unit of face, say 40: the long loses $11.8 \times (0.85 - 0.40) \approx$ \$5.3mm, the short gains $23.9 \times (0.92 - 0.40) \approx$ \$12.4mm, so the "neutral" pair is net short Brambleworth's default by about \$7mm (equal jumps would need only about \$10.2mm face short, which is no longer DTS-neutral; Chapter 12-B and 12-C own the switch of rulers near default). And carry: \$10mm earning 700 bp of spread against \$22mm paying 600 bp is about −\$0.62mm a year before the borrow fee, which is roughly \$70k at a 30 bp fee and \$0.4–0.6mm at the fees seen around bankruptcies. *Against what:* the survivor's gross edge, 1.55% a year in the paper's equal-dollar construction, is about \$155k on \$10mm. The paper's pairs are equal-dollar, not DTS-neutral, so they do not have this carry hole, and they carry more spread beta instead. Every choice of ruler moves the leak to a different column; none makes it vanish (§8D.3 compares the rulers). *Status:* not ledgered; Wen's pencil mark says why.

![Figure 9B.4: The two-leg bounce artifact. A long–short pair's daily P&L built from raw prints (grey) shows a sharp loss and a full reversal the next day, because a low print on the long leg and a high print on the short leg each register as a loss and then a gain; the same pair rebuilt from bounce-filtered prices with separate signal and return prices for each leg (black) shows neither. Illustrative, after the PB-03 replay of March 2020 (Chapter 8 §8.4); not real prints.](assets/figures/ch09b_two_leg_bounce.png)

Wen left at seven, with the survivor list folded into the weather. Theo walked her to the elevator and asked what she would do with it. "Read the pairs the paper likes and check whether we already own them for a reason," she said. "If we do, the paper is a second opinion. If we don't, it's a list of shorts I can't borrow." The elevator arrived. "Mostly the second."

## 9B.8 The Replication Harness

On Friday Theo wrote the spec for the thing the week had been building toward: a harness that every candidate signal passes through before it is allowed near the factor library. It is what the nightly `obap_repro` job of §9.9 now runs, and its first draft went the way first drafts to ROBO go.

*What ROBO built from the vague version.* The draft said *make the harness robust to outliers.* ROBO, which has read every statistics textbook and believes all of them, winsorized every holding-month return at the 0.5th and 99.5th percentiles of the full sample, the textbook default, and in doing so rebuilt, faithfully and without complaint, the exact filter that had moved the number in the cold open. Kaz looked at the output for a long moment and then laughed, which is the only correct response to a machine that has reproduced your mistake from first principles.

The precise spec is short. The harness takes one candidate signal and a panel in which every bond-month carries the signal read from the month-end price, the same signal read from a price one to ten business days earlier, the month-end and month-begin returns of the following month, the return the bond had already earned by the formation date, its market value, rating, issuer, and the dates of every price involved. It builds the long-short portfolio three ways: the contaminated reference (signal and return sharing the month-end price), the signal-gap version and the return-gap version. Its first gate refuses to run the second and third if any bond-month's signal price is dated on or after its return's starting price: *the signal price is never the entry price*, written as an exception rather than a hope. Its second gate allows only ex-ante screens, which act on what was known at formation; full-sample winsorization of the holding-month return appears in the harness exactly once, as a diagnostic that measures how much a signal leans on look-ahead, and never as a result. For each version it reports the mean premium, the CAPM-B alpha against the bond market factor with Newey–West standard errors using $\lfloor T^{1/4} \rfloor$ lags (four, for 268 months), the share of the premium the gap removes, and the interquartile range of the premium across a grid of ex-ante screens and weightings, the non-standard-error band that sits beside the $t$-statistic in every report the committee sees. The path count goes into the deflated Sharpe ratio of §7.8.

Why build it in plain pandas when PyBondLab 0.3.0 exists? Because the production job calls PyBondLab's `SingleSort`, `WithinFirmSort` and `DataUncertaintyAnalysis` classes (its panels need the columns `date`, `ID`, `ret`, `VW` and `RATING_NUM`), and a harness whose every step is visible is the only way to check that the library does what the desk thinks it does. Listing 9B.1 mirrors those conventions so the two can be run side by side, and it pins nothing: the production job pins the pipeline at v4.2.1 and the library at 0.3.0, and writes both into the header of every report. When to use it: on any signal built from bond prices, spreads or yields, and on any signal at all for the ex-ante gate, since a full-sample trim leaks the future whatever the signal is made of. When not to use it unchanged: daily signals, CDS-based signals and loan marks, where the gap and the screens have to be redefined for that instrument's clock (Duarte, Jones and Wang's 2024 work on option quotes is the precedent for porting the same logic to other quote-driven markets).

The edge case that bites is the universe. A month-begin return exists only for a bond that printed in the first five business days of the next month, and a gap signal exists only for a bond that printed a week or two before month-end. Both versions therefore drop illiquid bonds that the contaminated version keeps, and part of any "bias" measured by comparing them is a change of universe rather than a change of price. The listing reports the bond-month count beside each version so that a reader can see when the comparison is not like for like. The small synthetic demonstration at its end checks the arithmetic of §9B.4: a reversal signal on prices with half a percent of month-end noise and no true reversal earns roughly $2\kappa\rho\sigma_\delta$ in the contaminated version and nothing with the gap.

<!-- EXPLAINED -->
```python
# replication_harness.py -- Listing 9B.1 (Chapter 9-B)
# Two gates for a candidate bond signal: (1) the signal price is never the entry
# price; (2) every screen is ex ante. Reports premium, CAPM-B alpha (Newey-West t,
# floor(T**0.25) lags), gap share, a look-ahead diagnostic and a non-standard-error
# band across screening paths. A pandas mirror of the PyBondLab 0.3.0 workflow.
import numpy as np
import pandas as pd


def newey_west_t(y, x=None):
    """OLS of y on [1, x]; returns (coefficients, Newey-West t-stats)."""
    y = np.asarray(y, float)
    X = np.ones((len(y), 1)) if x is None else np.column_stack([np.ones(len(y)), np.asarray(x, float)])
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    u = y - X @ beta
    lags = int(np.floor(len(y) ** 0.25))
    Xu = X * u[:, None]
    S = Xu.T @ Xu
    for l in range(1, lags + 1):
        G = Xu[l:].T @ Xu[:-l]
        S += (1.0 - l / (lags + 1.0)) * (G + G.T)
    XtX_inv = np.linalg.inv(X.T @ X)
    se = np.sqrt(np.diag(XtX_inv @ S @ XtX_inv))
    return beta, beta / se


def check_gap(panel, sig_date, base_date):
    """Gate 1: refuse any bond-month that sorts and earns on the same price."""
    bad = (panel[sig_date] >= panel[base_date]).mean()
    if bad > 0:
        raise ValueError(f"{bad:.1%} of bond-months use the signal price as the entry price")


def exante_screen(panel, ret_cap=None, tail="both", px_range=None):
    """Gate 2: drop bond-months using only formation-date information:
    the return already earned in month t (ret_lag) and the formation price (prc)."""
    keep = pd.Series(True, index=panel.index)
    if ret_cap is not None:
        if tail in ("left", "both"):
            keep &= ~(panel["ret_lag"] < -ret_cap)
        if tail in ("right", "both"):
            keep &= ~(panel["ret_lag"] > ret_cap)
    if px_range is not None:
        keep &= panel["prc"].between(*px_range)
    return panel[keep]


def expost_winsorize(panel, ret, q=0.005):
    """Look-ahead DIAGNOSTIC only: clip the holding-month return at full-sample
    percentiles, to measure how much a result leans on the future."""
    lo, hi = panel[ret].quantile([q, 1 - q])
    out = panel.copy()
    out[ret] = out[ret].clip(lo, hi)
    return out


def long_short(panel, sig, ret, n=10, within_firm=False, weight="EW"):
    """Monthly top-minus-bottom return. Single sort: top bucket minus bottom bucket.
    Within firm: each issuer's top-ranked bond minus its bottom-ranked bond, averaged."""
    out = {}
    for d, g in panel.dropna(subset=[sig, ret]).groupby("date"):
        if within_firm:
            g = g[g.groupby("firm")[sig].transform("nunique") >= 2]
            if g.empty:
                continue
            top = g.loc[g.groupby("firm")[sig].idxmax()]
            bot = g.loc[g.groupby("firm")[sig].idxmin()]
            w = np.ones(len(top)) if weight == "EW" else top["VW"].to_numpy() + bot["VW"].to_numpy()
            out[d] = np.average(top[ret].to_numpy() - bot[ret].to_numpy(), weights=w)
        else:
            if len(g) < 5 * n:
                continue
            bucket = pd.qcut(g[sig].rank(method="first"), n, labels=False)

            def leg(x):
                w = np.ones(len(x)) if weight == "EW" else x["VW"].to_numpy()
                return np.average(x[ret].to_numpy(), weights=w)

            out[d] = leg(g[bucket == n - 1]) - leg(g[bucket == 0])
    return pd.Series(out).sort_index()


def harness(panel, mktb_end, mktb_bgn, n=10, within_firm=False, weight="EW",
            caps=tuple(np.round(np.arange(0.20, 0.951, 0.05), 2))):
    panel = panel.reset_index(drop=True)
    check_gap(panel, "sig_gap_px_date", "end_base_date")   # signal gap version
    check_gap(panel, "sig_px_date", "bgn_base_date")       # return gap version
    versions = {"reference (contaminated)": ("signal", "ret_end", mktb_end),
                "signal gap": ("signal_gap", "ret_end", mktb_end),
                "return gap": ("signal", "ret_bgn", mktb_bgn)}
    report = {}
    for name, (sig, ret, mkt) in versions.items():
        ls = long_short(panel, sig, ret, n, within_firm, weight)
        m = mkt.reindex(ls.index)
        ok = m.notna().to_numpy()
        (_,), (t_mu,) = newey_west_t(ls.to_numpy()[ok])
        (a, _), (t_a, _) = newey_west_t(ls.to_numpy()[ok], m.to_numpy()[ok])
        report[name] = {"premium": ls.mean(), "t_premium": t_mu, "alpha": a, "t_alpha": t_a,
                        "months": int(ok.sum()), "bond_months": int(panel[[sig, ret]].dropna().shape[0])}
    ref, gap = report["reference (contaminated)"]["premium"], report["return gap"]["premium"]
    report["gap_share"] = 1.0 - gap / ref if ref != 0 else np.nan
    wz = long_short(expost_winsorize(panel, "ret_bgn"), "signal", "ret_bgn", n, within_firm, weight)
    report["lookahead_diagnostic"] = wz.mean() - gap
    prem = [long_short(exante_screen(panel, c, tail), "signal", "ret_bgn", n, within_firm, w).mean()
            for c in caps for tail in ("left", "right", "both") for w in ("EW", "VW")]
    q25, q75 = np.nanpercentile(prem, [25, 75])
    report["nse"] = {"paths": len(prem), "iqr": q75 - q25, "median": float(np.nanmedian(prem))}
    return report


if __name__ == "__main__":
    # Synthetic check of section 9B.4: true returns i.i.d. (no reversal at all),
    # month-end marks carry 0.5% noise; month-begin and gap prices are fresh draws.
    rng = np.random.default_rng(7)
    months = pd.period_range("2005-01", periods=120, freq="M").to_timestamp(how="end").normalize()
    nb, sd = 600, 0.005
    true = np.cumsum(rng.normal(0.004, 0.02, (len(months) + 2, nb)), axis=0)
    ne, nb_, ng = (rng.normal(0, sd, true.shape) for _ in range(3))
    rows = []
    for k, d in enumerate(months, start=1):
        p_end_prev, p_end, p_end_next = true[k - 1] + ne[k - 1], true[k] + ne[k], true[k + 1] + ne[k + 1]
        p_gap, p_bgn = true[k] + ng[k], true[k] + nb_[k]
        ret_lag = p_end - p_end_prev
        rows.append(pd.DataFrame({
            "date": d, "ID": np.arange(nb), "firm": np.arange(nb) // 3,
            "signal": -ret_lag, "signal_gap": -(p_gap - p_end_prev),
            "ret_end": p_end_next - p_end, "ret_bgn": p_end_next - p_bgn, "ret_lag": ret_lag,
            "prc": 100 * np.exp(p_end - true[0]), "VW": 1.0 + rng.random(nb), "RATING_NUM": 15,
            "sig_px_date": d, "sig_gap_px_date": d - pd.Timedelta(days=3),
            "end_base_date": d, "bgn_base_date": d + pd.Timedelta(days=1)}))
    panel = pd.concat(rows, ignore_index=True)
    mkt_end, mkt_bgn = panel.groupby("date")["ret_end"].mean(), panel.groupby("date")["ret_bgn"].mean()
    rep = harness(panel, mkt_end, mkt_bgn, caps=(0.20, 0.50, 0.95))
    for key, val in rep.items():
        print(key, val)
    assert rep["reference (contaminated)"]["premium"] > 0.002      # about 2 x 1.75 x 0.24 x 0.5%
    assert abs(rep["return gap"]["premium"]) < 0.0015               # nothing left with the gap
```

## 9B.9 What a Desk May Still Trade, Net of Chapter 9

Late on Friday, Ines asked for one page, and the page was a table. Its rows are the survivors grouped into families; its gross numbers are the audit's; its cost column points to Chapter 9's cost curve (§9.8–§9.10), to Dickerson, Nozawa and Robotti's delay costs and to Ivashchenko and Kosowski's (2024) capacity estimates; and its last column is the desk's judgement, labelled as such.

| Family | Construction | Gross alpha (audit) | The cost that bites | What is honestly left *(desk's judgement, illustrative)* |
| :-- | :-- | :-- | :-- | :-- |
| Credit-spread value | within issuer (`val_ipr`, `val_ipr_dts`) | 2.2–2.5% a year | two half-spreads inside one issuer; borrow on the rich bond; delay cost of about 0.11% a month for spread factors, if it applies here | the best candidate: roughly 1% a year before borrow; low turnover, so capacity is the least of its problems |
| Credit-spread value | single sort, value-weighted (long-only can hold it) | 3.71% a year, $t$ 2.12, fails FDR | rebalancing half-spreads; the same delay class | a tilt to size as a tilt, not a factor |
| Spread reversal within issuer (`dcs6*`) | within issuer | 2.46–2.66% a year | a faster signal, so more turnover and more delay | thin; fast signals are the ones delays kill |
| Residual and systematic momentum within issuer | within issuer, equal-weighted | 1.55% and 2.20% a year | equal weights mean small bonds; borrow on the laggard sibling; a momentum-class delay cost near 0.11% a month | for a pod that already pays for borrow; near zero for anyone else |
| Bond age | single sort, equal-weighted | survives FDR | small bonds | a characteristic to control for, not to trade |
| Short-term reversal, price momentum, illiquidity, default risk | any | gone after correction | none needed | nothing |

The cost column rests on one paper more than any other. Of 341 bond factors, Dickerson, Nozawa and Robotti (2025) find 58 with significant gross returns, averaging 0.28% a month of alpha; once a realistic delay between signal and fill and the bid–ask spread are charged, the average falls to 0.09% for large trades and 0.05% for small ones, and two and one factors respectively stay significant. Delay costs a month run 0.11% for spread factors, 0.22% for equity-reversal factors, 0.11% for equity momentum and 0.06% for volatility and risk factors; nine machine-learning models with a pre-cost alpha of 0.82% a month keep about a third of it. Slicing orders, trading the fastest substitutes and holding for three months do not fix it. Ivashchenko and Kosowski add the second axis: market impact drives net returns to zero as a fund grows, quickly for high-turnover strategies and much more slowly for low-turnover, credit-risk-focused ones. The arithmetic in the first row is the desk's: 2.3% a year minus about 1.3% a year of spread-factor delay cost, before borrow.

*When it applies, and when it breaks.* Value survives correction, reversal does not, and momentum survives only inside an issuer; that is the short version, and it holds in TRACE-era US data with the bond CAPM as the benchmark. It breaks in three places. The null is contested: the bond CAPM of the audit, the duration-adjusted CAPM of van Binsbergen, Nozawa and Schwert, the five-factor IPCA model of Kelly, Palhares and Pruitt (2023), the Bayesian-averaged discount factor of Dickerson, Julliard and Mueller (2026, out-of-sample Sharpe ratio 1.5–1.8) and the outright CAPM rejection of Dick-Nielsen and coauthors would each produce a somewhat different list, and a survivor list is only as good as its null. The sample is short, which the 128-year panel makes vivid. And the survivors are mostly pairs, a different object from the long-only, sector-neutral portfolios most credit mandates hold. One diagnostic travels well: in options research, Duarte, Jones, Khorram, Mo and Wang (2026) show that filters using information unavailable at formation can inflate Sharpe ratios many times over, so a Sharpe ratio above about 2 on a monthly bond long-short is better read as a question about the filters than as a discovery.

> **Desk Myth vs. Desk Reality.** *Myth:* there are 108 bond factors. *Reality:* there are three families that survive correction (credit-spread value, a within-issuer spread reversal and residual momentum inside an issuer's own curve), every number on them is gross of costs, and two of the three are same-issuer pairs whose short leg is the bond nobody wants to lend.

> **View From Another Seat.** *The allocator.* An allocator meeting a systematic credit manager sees a short live record and a long backtest, the problem Chapter 4 describes from the manager's side. After 2026 the backtest has a second credential beside its Sharpe ratio: its lineage. Which pipeline version built the panel, which filters were chosen and when, whether the signal price and the return price differ, what the non-standard-error band is, and whether the factor reproduces the public corrected series. A manager who can answer in a page is offering a backtest that can be audited; one who cannot is offering a story. Described generically.

