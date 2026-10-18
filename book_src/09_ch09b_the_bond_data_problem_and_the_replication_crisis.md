# Chapter 9-B: The Bond Data Problem and the Replication Crisis

> **Builds on / used in.** *Builds on* Chapter 2 §2.2.2 (the TRACE caps as censoring), Chapter 4's rerun week (Kaz's Sharpe of 3.1 becoming 0.9), Chapter 7 §7.2 and §7.8–§7.9 (the replication history, false-discovery control, the deflated Sharpe ratio and the two biases derived), Chapter 8 §8.2 and §8.4 (duration-matched returns; the DTS-neutral pair) and Chapter 9 §9.9 (`obap_repro` and Hana's red build). *Used in* Chapter 10 §10.1 and §10.5 (which momentum is left to trade), Chapter 8-D (the short leg's price), Chapter 7-B (clustered residuals), Chapter 18 §18.8 and Chapter 22 §22.2 (decoding TRACE; the transparency ledger), Chapter 27 §27.2 and Appendix B §B.16 (the data-quality gates) and Appendix F, Listing 9B.1.

*What is invented, once for the whole chapter: the desk (Theo, Ines, Kaz, Mags, Hana and ROBO), its trade-reporting analyst Odile Brandt, its risk committee, Vantress Capital Management and its analyst Wen Zhao, the issuer Brambleworth Packaging, and every desk number, run, count, price and P&L in these scenes are fictional composites and illustrative. The papers, their numbers, the FINRA rules and the dated events are public and cited. Every number taken from Dickerson, Robotti and Rossetti (2026) is gross of trading costs, as is every alpha on their survivor list; the chapter repeats this where it matters, because it matters.*

## 9B.0 Cold Open: The Number That Moved by Itself

Tuesday, 10 November 2026, 7:40 a.m., Theo Marsh's eighth week. The factor library's nightly report is a forty-page PDF that nobody reads past page three, and Kaz reads it standing up, coffee in the other hand.

Page three carries the retired factors. The risk committee likes to keep them on the chart, the way a hospital keeps the file of a patient it has discharged, in case the patient comes back. Row 14 is six-month bond momentum, `mom6_1`, retired in Kaz's rerun week (Chapter 4) and kept as a reference line. On Monday's report its alpha was 0.46% a month, with a $t$-statistic of 2.4. This morning it is 0.22%, $t$ of 1.1.

Kaz put the coffee down. Kaz opened the repository and read its history back to Thursday. Nothing. Five thousand lines in the factor library, and not one of them had changed since the last time the number was 0.46. What had changed over the weekend was the quarterly WRDS refresh of the TRACE files, and a data ticket, DATA-3311, that used the refresh to repoint the library's input from Kaz's legacy vendor panel to the public Open Bond Asset Pricing panel.

"The code didn't move," Kaz said, "and the answer halved."

Theo had seen this shape before, in a data room. A cap table that changes between two drafts of a model nobody touched means the transfer agent re-ran the register. "Which line did it come from?"

"Wrong noun," Ines said, without looking up from her own screen. "Not which line. Which choice." She turned around. "The committee meets next Wednesday. They will ask what they always ask: why is this number different from yesterday? I would like an answer that isn't 'the data.'"

So that is the question this chapter answers: *how do you build a bond-return panel that cannot lie to you, and what is left of the factor literature when you have?* (Both of Kaz's numbers are the desk's own and fictional. That they equal, to the second decimal, two numbers in a published table is the clue, and §9B.5 cashes it.)

By the end of this chapter you will be able to read a TRACE row and say what a backtest inherits from it; build a bond-month panel in the published Stage 0 order, knowing what each filter protects against and what it could delete by mistake; write a month's return with its two prices and the right benchmark; size and fix the two biases that built the bond-factor zoo; read the 26 survivors of the 2026 audit beside a non-standard-error band; and carry them through Chapter 9's cost curve to the short list a desk could trade.

## 9B.1 What a TRACE Row Actually Is

Theo's instinct, eight weeks out of a restructuring practice, was the one PJT had trained into him: when a number moves, go to the source document. At PJT the source document was the data room. On this desk it was two rows of desks away, in a corner that faces a wall, where Odile Brandt has cleared the desk's TRACE exceptions for nine years.

Odile's working day runs on a fifteen-minute clock. FINRA Rule 6730 requires a dealer to report a corporate-bond trade "as soon as practicable, but no later than within 15 minutes of the Time of Execution"; a report that misses the window goes in late, marked *as/of*, and a pattern of late reports can be a violation of FINRA Rule 2010. Odile's queue is the list of the desk's own prints that a system thinks are wrong: a capacity flag that says *principal* on an agency trade, a contra-party code that does not match, a trade booked at 2:58 p.m. and reported at 3:19.

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

The first row is a real trade of \$3 million that the tape shows as `1MM+`, because FINRA disseminates high-yield sizes capped at \$1 million in real time (investment grade at \$5 million, `5MM+`). Chapter 2 (§2.2.2) treats the cap as censoring and Chapter 22 (§22.2.2) prices what hides behind it; Theo's Post-it says the rest: *a VWAP built from capped sizes is an average in which the biggest trades have been turned down to a whisper.*

The next three rows are one trade. A customer sold \$250,000 of bonds; the desk, acting as agent, passed them straight to another dealer, which bought them as principal. The desk reports the customer leg with capacity `A`, and both dealers report the interdealer leg. One economic event, three rows, and a backtest that sums volume, or weights prices by it, counts the same bonds three times.

The fifth row is not the desk's. A third dealer sold \$40,000 to a customer at 8.5125, which is 85.125 with the decimal point in the wrong place. It is on nobody's queue: not Odile's, because it is not the desk's print, and not the third dealer's, because its system saw a valid price and a valid size. It will sit in the public tape for as long as there is a public tape.

"Not mine," Odile said. "Not my problem. Your problem."

The sixth and seventh rows are a correction: the desk's trader had keyed the 09:47 sale an eighth too high, and FINRA's historic file layout records the fix as a `C` row that cancels the original, carrying the Prior Reference Number of the report it kills, and an `R` row that replaces it (a plain cancellation, with no replacement, would carry status `X`). The eighth row is the one Kaz, who had drifted over with a second coffee, put a finger on.

"Status Y. Reversal." Kaz held up a hand before anyone could speak. "I know. Not a factor (§7.9). I have been told. Is it the appellate kind, then?"

"Closer than the factor," Theo said, and was surprised to find that it was. In FINRA's layout a reversal is the cancellation of a trade report submitted more than twenty business days earlier, flagged with an As-Of indicator of `R`. Like an appeal, it undoes a judgement after the period for ordinary correction has run out, and it is matched to the judgement it overturns on a list of particulars: the CUSIP, quantity, price, execution date and time, buy or sell, and the contra-party indicator. This one reversed a \$500,000 sale at 86 that the desk had reported on 29 September against Brambleworth's 2030s when the bonds sold were the company's 2028s.

"Twenty-ninth of September," Theo said slowly. "That's inside September's last five business days."

"So what?" said Kaz, who knew exactly so what and wanted to hear Theo say it.

"So September's month-end price for this bond just changed. Six weeks after September ended. And September's return, and October's, because October's return starts from September's price." He looked at the screen. "The history moved. Nobody touched it, and it moved."

That is the first thing a TRACE row teaches, and Theo felt it before he could say it cleanly. The tape is not the market. It is a regulatory filing, assembled under a fifteen-minute clock by people with other jobs and amended for weeks afterwards, sometimes after the month it changes has closed. A backtest built on it inherits the exception queue: the desk's own, which Odile clears, and every other dealer's, which nobody here will ever see. A quarterly refresh of the TRACE files is, among other things, a delivery of other people's corrections to your history.

Mags had listened from her chair, which faces the other way. "Back in my day the print was a Post-it on the squawk box," she said, "and it was *also* wrong. But at least it didn't pretend to seven digits."

## 9B.2 Stage 0, or a Week Spent Cleaning TRACE

> **View From Another Seat.** *The dealer's operations desk.* To the quant, TRACE is a dataset. To the person in Odile's chair it is a compliance obligation with a timer on it, and the timer, not the price, is what gets reviewed: her performance is measured in late reports and capacity errors, not in whether a third dealer's 11:58 print was sensible, so the incentives that produce the tape and those that clean it belong to different people at different firms. The operations seat also sees what the quant cannot: the trade booked to the wrong CUSIP, the agency pass, the as/of filed because a system was down at 2:40. A systematic desk inside a dealer (as this one is) can ask; a fund that buys the tape from a vendor inherits the answers without the questions. Described generically, from FINRA Rule 6730 and public accounts of the work.

*Quant-shop life, a fictional composite: one week at a dealer's systematic credit desk, most of it spent looking at rows.*

Ines made the decision on Tuesday evening, and like most of her decisions it arrived as a question. "If the vendor's panel had a filter in it we didn't choose, how many filters are in the new one that we didn't choose?"

Nobody knew. So the desk would build the panel itself, from the raw tape, in the order the public pipeline publishes (the Stage 0 README of the Open Bond Asset Pricing `trace-data-pipeline`, pinned at v4.2.1, the September 2026 release), and every filter would get a row in a table with three columns: what it removes, what it could remove by mistake, and the date on which the desk chose it. The third column was Ines's. It had to be filled in before anyone computed a single return.

"Ex-ante or it didn't happen," Kaz said, and for one chapter that became the desk's motto, standing in for "IDO or it didn't happen," which took the week off.

ROBO did the building and Theo wrote the specs, one filter at a time, which is how the week went: slowly, with a lot of looking at individual rows.

**Wednesday.** Wednesday was Veterans Day, a full close for the bond market by SIFMA's recommendation and an ordinary day for the NYSE, so the floor was quiet and the pipeline's NYSE calendar insisted it was a business day; ROBO flagged it for "anomalously low print counts," which was accurate and useless.

Step 0 normalised the price scale, because feeds quoting per \$100 of par, per \$1,000 or as a decimal of par will hand you 85, 850 and 0.85 for the same bond. Step 1 was the cleaning procedure Jens Dick-Nielsen published for TRACE in 2009 and for Enhanced TRACE in 2014, which, as Dickerson, Robotti and Rossetti (2026) describe it, removes cancellations, corrections, reversals and agency-side duplicates (nobody on the desk had the 2014 paper's own text in front of them that week, and Theo wrote that in the spec's margin). On Brambleworth's Monday, step 1 turned eight rows into three: the corrected 09:47 sale, the agency pass once, and the 8.5125, which survived because nothing in step 1 knows what a sensible price is. That is step 2's job.

**Thursday.** Step 2 is the decimal-shift corrector, and it is a small piece of judgement written down as arithmetic. For each bond it keeps an anchor, the median of the last eleven unique prices. A print is tested only if it misses the anchor by more than 5%. A tested print is multiplied in turn by 0.1, 0.01, 10 and 100, and a candidate is accepted if the corrected price lands within 2% of the anchor, or within 8 points of it, or with both the corrected price and the anchor inside 15 points of par; and two further conditions hold the corrector back: the corrected error is at most a fifth of the raw error, and the corrected price lies between 5 and 300. The 8.5125 missed an anchor of about 85 by 90%. Multiplied by 10 it became 85.125, a miss of under a fifth of a percent, comfortably inside every bound, and ROBO wrote the corrected price into the panel with the raw one beside it.

Theo liked step 2 more than he expected to: it is what a good associate does with a data room, treating the typo as a typo only when the corrected number agrees with everything around it. Steps 3 to 6 went quickly. The intraday time window is off by default, the NYSE calendar is applied, prices are kept only above 0 and at or below 1,000, and a volume screen that would drop trades under \$10,000 is off by default, because small trades print on the wrong side of the spread more often than not and throwing them away is a choice with a sign.

**Friday.** Step 7 is the bounce-back filter, which looks for a print that jumps far from its neighbours and comes straight back. Its baseline is the median of the five prior unique prices. It triggers on a move of 35 points, measured three ways (a one-step jump, a displacement from the baseline, or a spike to exactly 100 that sits at least 8.75 points from the baseline), and it calls the print a bounce if the price returns within five rows. It also flags runs of three or more consecutive prints at exactly par.

The par runs made Mags turn her chair around. "Back in my day," she said, "a pricing service, which I will not name because it no longer exists, marked a bond at par for eleven months. Not near par. Par. Nobody had traded it since the spring, the model needed a number, and the number it had was the issue price. Lowest volatility in the book." She paused. "A shipping company's second-lien bond. When it finally traded, it traded at 31." She read the line in Theo's spec that flagged three consecutive prints at exactly 100 twice, which for Mags is a standing ovation. "Fine. That would have caught it in March."

Steps 8 to 11 are dull, and each has a story. Out goes a trade whose price equals its yield (somebody typed 8.42, the yield, into the price field), a trade larger than half the bond's offering amount (a booking error far more often than a trade), a trade reported after maturity, and any bond whose first three prints are followed by a 50-point move, the signature of when-issued noise or the wrong scale.

**Monday.** The daily stage is for distressed bonds, where a typo and a price look alike. Over five-day windows it flags a print below 0.10 (or a suspiciously round one) when the surrounding median is at least three times higher; an upward spike above 5.0, at least three times the prior median, that falls back within five days; a plateau of two or more identical days below 0.15 or at round numbers; and an intraday range above 75% of the mean when any price that day is below 20. A bond quoted at two cents on the dollar and a mistyped 0.02 are, to a computer, the same object; to Mags they are not, and the daily stage is an attempt to write down why.

**Tuesday.** On the following Tuesday ROBO built its first monthly returns, and Kaz, wanting a quick look before the full run, sent it a one-line instruction: *remove outliers from the monthly returns before the first test.*

ROBO did exactly that. It computed the absolute value of every bond-month return in the panel, took the top half-percent, and deleted them. It did not complain and it did not guess. It produced, as asked, a file of the deleted rows.

Mags read the file the way she reads a docket. "This isn't a list of errors," she said. "It's a list of defaults." The largest negative returns in a high-yield panel are mostly not typos but missed coupons, distressed exchanges and Chapter 11 filings: months like Windstream's February 2019, when the company lost its indenture case to Aurelius and filed for bankruptcy ten days later (the deleted rows are the desk's fictional run; the ruling and the filing are public record). A panel that deletes those months has deleted the left tail of every high-carry, high-value portfolio in it, and a value strategy built on it looks like a strategy that has never met a default, because it hasn't.

Here Theo knew more than anyone at the table: he had spent years explaining to clients why a defaulted bond trades flat, and the pipeline's treatment matches what a restructuring banker would write. Bonds stay in the panel through default, which is marked when the numeric rating code reaches the default grade (22 on the pipeline's S&P scale, 21 on its Moody's scale). In the default month no coupon is paid, so the return is next month's clean price over this month's price plus accrued interest, minus one: the holder paid for accrued interest it will not receive. After that the bond trades flat, and its return is the change in clean price alone. The lawyers, as Mags says, come later; the return series just keeps the bond.

By Tuesday night the table had fourteen rows, each dated before the first return, and Kaz's instruction to ROBO had been replaced by a line Theo wrote in capitals at the top of the spec: *no filter is defined in terms of the returns it will be used to test.* It was Chapter 7's look-ahead bias (§7.9) written as a constraint on a build, the only place a constraint does any good.

> **Ways This Blows Up.** *Two filters that are right nine times in ten.* **The decimal shift that erases a crash.** A bond has traded near 90 for months; on a Thursday afternoon the issuer discloses something terrible, and the next prints are 9, 9.5 and 8.75. Each misses an anchor of 90 by about 90%, and each, multiplied by 10, lands within 2% of the anchor with both prices inside 15 points of par. A rule of this shape accepts the correction, and the crash vanishes from the panel until enough low prints have moved the eleven-trade median; if the disclosure lands in a month's last week, the default shows up a month late, a timing error in exactly the observation a credit model most needs *(illustrative; the pipeline's other checks may catch a given case)*. **The bounce-back that deletes a liability-management gap.** A 35-point drop that comes back within five rows is usually a fat finger. Occasionally it is a non-pro-rata uptier announced at 4 p.m. and partly walked back the next morning when the excluded holders' counsel calls, and the round trip is the most informative pair of prints the bond will ever produce (Chapter 13 reads those events as games). Both failures have the same cure: filters flag, people review, and the review is logged, so that a filter's mistakes become rows in a table instead of holes in a backtest.

## 9B.3 Two Prices, One Month

On the Thursday of the cleaning week, while ROBO worked through step 2, Kaz took the whiteboard to define the thing the whole panel exists to produce: one bond's return over one month. It sounds like the easiest definition in finance. It took most of the afternoon.

Start with what a "month-end price" means for a bond that does not trade every day, which is nearly every bond: in 2022, by Dickerson, Nozawa and Robotti's (2025) count, about 70% of 29,543 bonds traded on ten or fewer days, and 109, 0.4%, traded every day. So the pipeline takes the month's price as the last daily volume-weighted average price in the month's final five NYSE business days. A bond that last printed on the 24th carries the 24th's VWAP as its month-end price, already a few days old; a bond with no print in those five days has no month-end price and no return that month.

Kaz wrote the return the way the pipeline does, with $P$ the clean price, $AI$ the accrued interest and $C$ any coupon paid during the month:

$$
r^{\text{End}}_{i,t+1} \;=\; \frac{P^{\text{end}}_{i,t+1} + AI_{i,t+1} + C_{i,t+1}}{P^{\text{end}}_{i,t} + AI_{i,t}} \;-\; 1 .
$$

Then Kaz wrote a second one, the *month-begin* return, which keeps the same ending price but starts from the first price observed in the first five business days of the new month, $P^{\text{bgn}}_{i,t+1}$, a median of one business day after the month-end price in the 2026 audit:

$$
r^{\text{Bgn}}_{i,t+1} \;=\; \frac{P^{\text{end}}_{i,t+1} + AI_{i,t+1} + C_{i,t+1}}{P^{\text{bgn}}_{i,t+1} + AI^{\text{bgn}}_{i,t+1}} \;-\; 1 .
$$

Divide the first by the second and the ending price cancels. What is left is the gap: the move from the month-end price to the first price of the next month. To a close approximation,

$$
r^{\text{End}}_{i,t+1} \;\approx\; \underbrace{\frac{P^{\text{bgn}}_{i,t+1}}{P^{\text{end}}_{i,t}} - 1}_{\text{gap return}} \;+\; r^{\text{Bgn}}_{i,t+1} .
$$

> **Math, Gently.** *A return has two prices, and only one of them is yours.* A bond is marked at 98 at Friday's close; on Monday morning, the first moment anybody could act on Friday's information, it trades at 99; the following Friday it closes at 100. Friday to Friday is $100/98 - 1 = 2.04\%$; Monday to Friday is $100/99 - 1 = 1.01\%$; the weekend gap is $99/98 - 1 = 1.02\%$, and $1.0102 \times 1.0101 = 1.0204$. If your signal was computed from Friday's 98, you could not have bought at 98: by the time you knew the signal, the price on offer was 99. The 2.04% is the bond's return; the 1.01% is yours. A backtest that books the 2.04% has paid itself the gap, and if the gap is related to the signal (as §9B.4 shows it is whenever the signal is built from the same 98), it has paid itself a strategy. The version with noise is §9B.4's box and the derivation in §7.9.

Theo had his USB stick on the desk, as he always does, and he plugged it in, because something on the whiteboard looked familiar. His 13-week cash flow model, the one from PJT, has a row called *cash at start of week* and a row called *cash at end of week*, and week two's opening balance is week one's closing balance, by formula, one cell doing two jobs.

"Same shape," he said. "The month-end price is September's closing balance and October's opening balance."

"Same shape," Kaz agreed. "Is your model ever wrong about it?"

"Never. It ties to the bank statement every Friday." He heard himself say it, and the sentence went on sounding in his head after he stopped talking.

The rest of the afternoon went on the benchmark, the second choice hidden inside "a bond's return." The audit's headline results subtract the one-month Treasury-bill rate, the equity convention. Andreani, Palhares and Richardson (2024) argue that for bonds this leaves the rate component, which is negatively correlated with the spread component, inside what you are calling the credit return, contaminating inference most for investment grade and for anything measured through time. Van Binsbergen, Nozawa and Schwert (2025) subtract instead the return of a Treasury position with the same duration,

$$
r^{\text{ex,dur}}_{i,t+1} \;=\; r_{i,t+1} \;-\; r^{\text{TSY}}_{t+1}\!\big(D^{\text{mod}}_{i,t}\big),
$$

where $r^{\text{TSY}}_{t+1}(D)$ is built by interpolating key-rate Treasury returns linearly on the bond's modified duration at the start of the month. On that measure investment-grade bonds earn a small credit premium, about the size of a convenience yield, and the bond CAPM's apparent failures for IG largely go away; the Open Bond Asset Pricing site ships Yoshio Nozawa's duration-matched Treasury returns. A tiny number *(illustrative)*: in a year like 2022 a seven-year BBB bond can lose 10% while T-bills pay 1.5%. Against the bill its "excess return" is about −11.5%, nearly all of it the rate shock; against a seven-year Treasury that lost 9% it is about −1%, the part a credit model is supposed to explain. Chapter 8 (§8.2) adds the companion point: the rate sensitivity a bond shows in a sell-off is not always the one its cash flows promise.

One last piece of arithmetic answered a question Hana had asked on Monday. The panel runs from August 2002 to December 2024, which is 269 months of prices. The audit's return tables report $T = 268$, and the difference is not an error: 269 prices produce 268 returns, because the first month supplies only a starting price.

![Figure 9B.1: One bond, one month-end, two prices. The month's price is the last daily VWAP inside the final five NYSE business days (shaded); the signal price, in the gap version, is read one to ten business days earlier; the month-begin price is the first print in the next month's first five business days, a median of one business day later. The shaded wedge between the month-end price and the month-begin price is the gap return, which a month-end-to-month-end return books and a month-begin return does not. Illustrative prints; definitions from Dickerson, Robotti and Rossetti (2026), arXiv:2604.07880, and the trace-data-pipeline README.](assets/figures/ch09b_two_prices.png)

## 9B.4 The Noise in the Denominator

The sentence that kept sounding in Theo's head was *it ties to the bank statement*, and it finished itself that evening, while he was reading ROBO's draft schema for the panel.

The schema had a column called `prc_m`, the month price, and it fed two others. One was `cs`, the credit spread computed from the yield at that price, the input to every value signal on the desk, including `val_ipr` (the fair-spread family of §9.3), the survivor Theo had decided in Chapter 4 to trust. The other was `ret_base`, the denominator of next month's return. One column, two jobs, exactly like the cell in his 13-week model.

The difference was the bank statement. In his model the shared cell is fine, because it is reconciled to an external truth every week. A bond's month-end price has no bank statement; its error is never observed, only inherited. A bond recorded too low looks cheap, so a value sort buys it, and next month its return is measured from the too-low base, so it "earns" the error back. The signal and the return are not two measurements of the bond. They are one measurement, used twice, with opposite signs.

At PJT this would have been a familiar sin in another costume. You do not let the company's own projections be the evidence that the company's projections are reasonable, because then the question and the answer are the same document. Here the question (is this bond cheap?) and the answer (did it outperform?) were the same price.

He wrote it on a Post-it, *one price, two jobs*, and stuck it to Kaz's monitor. Kaz read it on Friday morning and wrote a second line underneath: *the noise in the denominator is the alpha in the numerator.*

Chapters 4 and 7 drew the two-bond version on a whiteboard: noise of plus or minus half a percent, a true return of zero, a 1.00% long-short from nothing. The desk needed the version for a sort of thousands of bonds, and the audit's Theorem B.1 gives it.

> **Math, Gently.** *Correlated errors-in-variables, or why finer sorts find more noise.* An errors-in-variables problem is a measurement error in an explanatory variable; it is *correlated* when the same error also sits in the thing being explained. Rank 6,000 bonds on a signal built from a noisy price and cut the ranking into ten buckets. The top bucket is partly the bonds with the most negative noise, because negative noise makes a bond look cheap; the bottom bucket has the most positive. If the signal is roughly bell-shaped, the average standardised score of the top bucket is about 1.09 for a three-way split, 1.40 for five and 1.75 for ten: finer sorts dig deeper into the tails, where the noise lives. Call that average $\kappa$, the correlation between signal and noise $\rho$, and the noise's size $\sigma_\delta$. The long bucket carries average noise of about $-\kappa\rho\sigma_\delta$ and earns it back next month; the short bucket carries $+\kappa\rho\sigma_\delta$ and gives it back. Tiny number *(illustrative)*: with $\sigma_\delta = 0.5\%$ and $\rho = 0.3$, a decile sort manufactures $2 \times 1.75 \times 0.3 \times 0.5\% \approx 0.53\%$ a month, a tercile sort $0.33\%$. The two-bond whiteboard example is the special case $\rho = 1$, $\kappa = 1$: $2 \times 1 \times 1 \times 0.5\% = 1.00\%$. The covariance algebra is in §7.9.

In the paper's notation the bias is

$$
\text{LIB} \;=\; 2\,\kappa\,\rho\,\sigma_\delta ,
$$

with $\kappa$ a normal-tail constant that grows with the fineness of the sort and $\rho$ the strength of the link between noise and signal (reading $\kappa$ as the mean of the extreme bucket of a standard normal is this book's stylised reading). Three consequences follow, and the audit measures each. The bias belongs to price-based signals: a rating or an estimated beta has no month-end price inside it, and in the audit's placebo test (§7.2) the gap matters for far fewer non-price factors. The fix is cheap: read the signal from a price one to ten business days *before* month-end (a signal gap), or start the return from the month-begin price (a return gap). And the bias can be measured directly, because it is the gap return: the correlation between $r^{\text{End}} - r^{\text{Bgn}}$ and the estimated bias is 0.99 across factors (0.93 to 0.98 within firms). The wedge Kaz drew on Thursday *is* the bias, to two decimal places.

Then Theo put up the audit's Table 1 (value-weighted decile long-shorts, 2002–2024, monthly, gross of costs) and read it like a waterfall, in three columns: unadjusted, signal gap, return gap. Yield to maturity: 1.20%, 1.05%, 0.92%. Credit spread: 1.13%, 0.96%, 0.82%. Book-to-market: 0.93%, 0.75%, 0.66%. Six-month spread change: −1.02%, −0.50%, −0.46%. Houweling and van Zundert's value signal: 0.81%, 0.45%, 0.43%, its alpha down from 0.47% to 0.12% ($t$ of 1.13). And `val_ipr`, the Israel–Palhares–Richardson residual-spread signal Theo cared about: 0.96% falling to 0.51% under either gap, its CAPM-B alpha from 0.76% to 0.31% ($t$ of 2.12) and 0.33% ($t$ of 2.61). At the bottom sat short-term reversal, −0.99% falling to −0.09%, which Hana had met in person in §9.9. She looked at it anyway and said nothing, which on this desk is a form of solidarity.

Across the table the bias takes more than 80% of the reversal premium, 45–55% of the value and spread-change premia, and 20–50% of the yield and spread premia, and it is larger again in within-firm sorts. Value lost about half and lived. That was the good news, and Theo took it, with the reservation Ines added before he could get attached to it.

"The month-begin price is one business day later," Ines said. "Median. That's the earliest you could have traded, not the price you'd have got." That is the open half of the debate, and the audit concedes it: part of what it calls a bias is a real implementation wedge, since the month-end print was never executable, and the one-day gap is a floor on that wedge, not a measure of it. Dickerson, Nozawa and Robotti's delay costs (2025) finish the thought in §9B.9.

![Figure 9B.2: The same seven price-based factors three ways: unadjusted (signal and return share the month-end price), with a signal gap (signal read one to ten business days earlier) and with a return gap (return starts at the month-begin price). Short-term reversal collapses from −0.99% to −0.09% a month; the value and spread family loses roughly half; val_ipr keeps a significant alpha. Value-weighted decile long-short premia, monthly, US corporate bonds, TRACE, 2002–2024, gross of costs; t-statistics above the bars. Source: Dickerson, Robotti and Rossetti (2026), arXiv:2604.07880, Table 1.](assets/figures/ch09b_lib_waterfall.png)

> **Poker Table.** *The card in your hand and on the board.* "If the same card is in your hand and on the board," Ines said, "the deck is marked, and your two pair is one pair counted twice." A month-end price that sets the signal and starts the return is that card. Her hand history is the gap decomposition: deal the same hand again with the board turned one day later and see what is left. For reversal, almost nothing; for value, half. The difference between the two deals correlates 0.99 with the bias, a poker player's way of saying the difference *is* the bias. In Chapter 4 she called it "the part of your alpha that belonged to someone else." Here it is the part that was never anybody's.

## 9B.5 The Filter That Knew the Future

On Monday ROBO finished the first full run on the desk's own build, and six-month momentum came out at 0.22% a month, $t$ of 1.1: the public panel's number, reproduced from the raw tape. That settled which number was the panel's. It did not say where the old one had come from.

Mags asked, because she always asks. She is suspicious of anything called "adjusted," and the legacy panel's documentation used the word four times on its first page. "Somebody chose a ninety-nine-point-five," she said, pointing at a line in the vendor-panel README. "Who chose it, and when?"

Kaz had chosen it. Building the vendor panel last year, Kaz had winsorized returns at the 0.5th and 99.5th percentiles of the full sample, and in the rerun week of Chapter 4 had found and fixed that, in the research notebook. The production file the library read every night had been built once, a year earlier, with the winsorization baked into its stored returns. The library's five thousand lines never winsorized anything; the data arrived pre-trimmed. When DATA-3311 pointed the library at the public panel, the trimming disappeared, and the number moved.

"I fixed it in the notebook," Kaz said. "I never fixed the file."

It is the most ordinary sentence in quantitative finance, and the reason the risk committee asks its question. Then Theo put the two numbers next to the 2026 audit's Table 4, and they matched. For six-month momentum, value-weighted deciles, the audit reports a CAPM-B alpha of 0.46% a month ($t$ of 2.39) with full-sample winsorization and 0.22% ($t$ of 1.08) without. The desk had been rerunning a published table every night for a year, without knowing it, from the wrong side.

> **Math, Gently.** *Winsorizing with hindsight.* To winsorize at the 99.5th percentile is to replace every return above it with the percentile itself; to trim is to delete them. The trouble is the phrase *percentile of what*. The top half-percent of the panel's 1.8 million or so bond-months is set by its wildest months, the rebounds of 2009 and April 2020, so a threshold computed once over the whole sample clips a 2005 return with a ruler cut in 2020. An *ex-ante* filter decides which bonds to drop using only what was known on the formation date (the bond's price and its return up to that month) against thresholds fixed in advance; an *ex-post* filter edits the very return the signal is trying to predict, and a full-sample percentile is ex post twice over. Tiny number *(illustrative)*: if a past loser rebounds 60% in April 2009 and the full-sample 99.5th percentile is 25%, winsorizing turns a 60% loss on the short leg into a 25% loss, a gift of 35 points nobody trading in April 2009 could have received. The formal statement is in §7.9.

Kaz then did the thing the desk's harness now does for every candidate signal, and which the audit does in its Figure 6: rebuild six-month momentum under many trimming rules and draw the alpha as a function of the threshold. Four lines: screen out the right tail ex ante, on the return a bond had already earned by the formation date; the same for the left tail; then trim the right tail ex post, cutting extreme values of the holding-month return the signal is trying to predict; and the same for the left tail.

The two ex-ante lines lay on the floor. Under any ex-ante trimming of either tail, six-month momentum's alpha is statistically indistinguishable from zero. The ex-post right-tail line rose as the trimming tightened, to about 0.60% a month when every return above 10% in a month was cut. The ex-post left-tail line went the other way: the alpha turned negative, and it climbed back to zero only when the threshold was loosened to about −40%. *(The curves are the audit's, for March 2003 to December 2024, read from its Figure 6; the desk's run is fictional and drew the same shape.)*

Theo asked why the right tail, and the answer is the most intuitive thing in the chapter. A momentum portfolio is short last half-year's losers, and the biggest months a loser ever has are rebounds: the junk rally of spring 2009, the weeks after the Fed's facilities of March and April 2020. Those rebounds are the momentum crash; they land on the short leg, in the right tail. Trim the right tail after the fact and momentum never crashes. Trim the left tail after the fact and the strategy loses its losers' further collapses, the short leg's profit, and the premium turns negative. The audit's look-ahead bias for momentum sits in the short leg, spikes in 2008–09, 2011–12 and March 2020, rises more than proportionally with the VIX, and is two to three times larger in high yield than in investment grade. The filter knew the future best in exactly the months the strategy most needed not to know it.

Three- and twelve-month momentum tell the same story: premia of 0.33% and 0.26% a month winsorized, 0.17% and −0.13% without. That is the canonical claim of Jostova, Nikolova, Philipov and Stahel (2013), 59 bp a month across all bonds and 192 bp in high yield over 1991–2011, from TRACE combined with dealer quotes; the audit lists the paper among those using the 99.5th-percentile winsorization. Chapter 10 (§10.1, §10.5) inherits the conclusion: in TRACE-era data, cross-sectional price momentum does not survive an ex-ante filter, and the momentum that does survive is a different animal, met in §9B.7.

Risk factors have the opposite problem. Factors built on idiosyncratic volatility or downside risk are long the riskiest bonds, so their bias sits in the long leg, and their significance depends on trimming the *left* tail, which deletes the defaults those risky bonds were being paid to bear. In the audit's Table 4, an idiosyncratic-volatility factor has an alpha of 0.53% a month ($t$ of 2.58) winsorized and 0.18% ($t$ of 0.72) without; an expected-shortfall factor, 0.74% against 0.31% ($t$ of 1.42); a value-at-risk factor, 0.56% against 0.24% ($t$ of 1.42).

![Figure 9B.3: Six-month bond momentum's CAPM-B alpha as a function of the trimming threshold, four ways. Ex-ante trimming of either tail leaves the alpha indistinguishable from zero at every threshold; ex-post right-tail trimming lifts it to about 0.60% a month at a 10% monthly cut-off; ex-post left-tail trimming turns it negative, and it returns to zero only near a −40% cut-off. Value-weighted deciles, US corporate bonds, March 2003 to December 2024, gross of costs. Redrawn from Dickerson, Robotti and Rossetti (2026), arXiv:2604.07880, Figure 6 (pp. 25–27); only the anchor points stated in the text are taken from the paper, and the curves between them are schematic.](assets/figures/ch09b_mom6_trimming.png)

> **Desk Myth vs. Desk Reality.** *Myth:* the four-factor bond model of Bai, Bali and Wen (2019, *Journal of Financial Economics*) is the standard benchmark for corporate-bond alpha. *Reality:* it was retracted (notice: *JFE* 150(3), 103721, December 2023). By Alessandro Robotti's account in a Warwick Business School post of 10 September 2024, the factor data had "lead" errors in two factors and a "lag" error in a third, extreme losses had been filtered out after the fact, and once corrected the model added nothing beyond the bond CAPM; the post calls it the first retraction of its kind at the journal and notes more than 400 citations. Nothing here concerns anyone's intent. The point for this section is narrower: value-at-risk and expected-shortfall factors from that line of work are on the audit's list of factors whose significance needs ex-post left-tail winsorization (0.56% and 0.74% a month winsorized, 0.24% and 0.31% without). Open Bond Asset Pricing publishes the four factors corrected, and `obap_repro` (§9.9) reproduces them nightly; a "four-factor bond model" built on the original series is contaminated, whatever the pitch book calls it.

By Monday evening Kaz had rebuilt the production file without the winsorization, filed DATA-3312 to delete the old one, and added a line to the panel's choice table: *return trimming: none in the stored panel; any trimming is ex ante and lives in the harness, where it is reported.* Mags read it and said nothing, which from her, about a sentence containing the word "trimming," is as close to approval as the language allows.

## 9B.6 The Zoo, Counted Honestly

The model review met on Wednesday at ten, in the room with the good chairs; the minutes record its chair only by initials, which is how he prefers it. He asked the question, and Theo answered in three sentences: the stored file carried a full-sample winsorization nobody had chosen this year; the new build has none and dates every filter; and the two numbers on page three are the published winsorized and unwinsorized alphas for six-month momentum. The chair wrote for a while, then asked the question that matters more: "And the other hundred and seven?"

Chapter 4 put the audit's scoreboard on the screen (Figure 4.3): 432 specifications, 65 with a CAPM-B alpha $t$ above 1.96, 26 surviving the Benjamini–Hochberg correction (the box in §7.2), 25 of them within-firm, and equal-weighted bond age the only survivor sorted across the whole market. The committee wanted the list itself, with sizes *(annualised CAPM-B alphas, gross of costs; Dickerson, Robotti and Rossetti 2026, Internet Appendix IA.3; an asterisk marks a signal whose sign is flipped so the premium is positive)*:

| Survivor (within-firm) | Weighting | Alpha, % a year | $t$ |
| :-- | :-- | :-- | :-- |
| Six-month spread change, `dcs6*` (a reversal within the issuer) | EW / VW | 2.46 / 2.66 | 6.77 / 4.98 |
| Residual-spread value, `val_ipr` | EW / VW | 2.30 / 2.22 | 5.03 / 4.25 |
| Residual-spread value within DTS quintiles, `val_ipr_dts` | EW / VW | 2.23 / 2.47 | 5.51 / 4.50 |
| Systematic 12-1 momentum, `sysmom12_1*` | EW | 2.20 | 3.04 |
| Residual 12-1 momentum, `idimom12_1` | EW | 1.55 | 2.94 |

The rest of the 26 are betas (to the market's up-moves, co-skewness, illiquidity, volatility and macro uncertainty), measures of the shape of a bond's own return distribution, a DTS-demeaned version of Houweling and van Zundert's value signal, yield and age. Three absences matter as much. Nothing from the illiquidity cluster survives (five direct measures of illiquidity show no alpha), and nothing from the credit-and-default cluster. The value-weighted single sort of `val_ipr`, the version a long-only desk could actually hold, earns 3.71% a year with a $t$ of 2.12: past the old bar of 1.96, short of the corrected one. And none of the seven price-based single sorts of §9B.4 has a significant adjusted alpha inside investment grade or high yield taken separately; the best, Houweling and van Zundert's value in high yield, earns 0.37% a month with a $t$ of 1.91.

The chair's last question was the one the desk had come to answer. "How sure are they?" The honest reply is a second kind of error bar, and it is the most useful idea in the audit.

> **Math, Gently.** *Non-standard errors: the spread between careful people.* A standard error measures how much an estimate would wobble if history had dealt a different sample: it is uncertainty across *time*. A non-standard error measures how much the estimate wobbles when different careful researchers make different defensible choices on the *same* data: which tail to trim and how far, which price range to keep, which bounce filter to use, whether to weight by value or equally. Menkveld and coauthors (2024) measured it by handing one dataset and one set of hypotheses to 164 research teams and recording how far apart their answers landed; the 2026 audit builds each signal along many defensible paths and reports the interquartile range of the premia, the width of the middle half. Picture fifty analysts estimating the same premium: the standard error is how sure each of them is, the non-standard error how much they disagree. Tiny number: if the middle half of the paths spans 0.10% to 0.45% a month, the non-standard error is 0.35%, and a premium of 0.33% sits inside its own disagreement.

The audit builds two families of paths. The *data* paths vary only the cleaning: 108 ex-ante filters (48 return screens at sixteen thresholds on the left tail, the right tail or both; 30 price ranges; 30 bounce filters), each run equal- and value-weighted on all bonds, investment grade and high yield: 648 paths per signal. Their non-standard error averages 0.35% a month against an average premium of 0.33% (for alphas, 0.27% against 0.15%), 1.15 times the ordinary standard error. The *construction* paths vary the portfolio recipe (bucket count, breakpoints, weighting, rating group, maturity bucket): 168 per signal, with a non-standard error of 0.31% against a mean premium of 0.22%, 1.45 times the standard error. For 12 of the 36 top factors the premium changes sign somewhere along the paths, for 29 the alpha does, and in 94% of variations the baseline alpha does not improve. Value is the exception that keeps showing up: the one cluster with a detectable baseline premium, and the one where cleaning often helps (21% of left-tail and 15% of symmetric-trimming paths improve its alpha).

Kaz turned this into a sentence for the minutes that Chapter 7 had already earned. The deflated Sharpe ratio of §7.8 asks how many trials stand behind a result; for a bond factor built on TRACE, the honest count is at least the 648 data paths that a careful person could have walked, not 1. Law 12 of Appendix E, *count your trials*, has a number for credit now.

The committee did not leave pessimistic, and the desk did not want it to. Jensen, Kelly and Pedersen (2023) find that most *equity* factors replicate, cluster into 13 themes and work out of sample across 93 countries, so the bond problem is data quality, not the idea of factors. Ghaderi, Plante, Roussanov and Seo (NBER Working Paper 35578, August 2026) reconstruct 128 years of US corporate bonds and find a sizable, significant credit risk premium over the long sample: 22 TRACE years have low power, and a factor that fails in 268 months has not been proved absent. And Dick-Nielsen, Feldhütter, Pedersen and Stolborg, independently and with different data and cleaning (outliers reviewed one at a time, default returns kept), reach the same direction by another road: in QuantPedia's summary, only 23% of literature-significant factors keep significant alphas, and they reject the bond CAPM that the 2026 audit uses as its benchmark. Two teams, two mechanisms, one direction, and a disagreement about the null that §9B.9 returns to.

> **View From Another Seat.** *The systematic asset manager.* The practitioner template for credit factors was published from inside one: Houweling and van Zundert, writing from Robeco, showed in 2017 (*Financial Analysts Journal*) that size, low-risk, value and momentum portfolios earned significant alphas and combined well. The audit's rebuild of their value leg is the clearest published haircut on that template: 0.81% a month falling to 0.45% ($t$ of 2.29) once the signal reads an earlier price, the alpha down to 0.12% ($t$ of 1.13). How any manager's live portfolios have fared is its own business, and this book does not speak for Robeco. The seat's general advantage is that a manager who has traded a factor for years owns its fills, which are month-begin prices by construction; its question is not "is the premium real?" but "did our executed prices look like $r^{\text{Bgn}}$ or like $r^{\text{End}}$?", and its blotter answers it.

> **Trend Watch.** *The bond-data ledger, 2023–2026.* **December 2023:** the Bai–Bali–Wen retraction notice. **23 July 2025:** "Factor Investing with Delays" (Hitotsubashi IER Discussion Paper A771), the delay-cost paper of §9B.9. **November 2025:** Open Bond Asset Pricing launches its open panels and factor files. **11 December 2025:** the pipeline's Stage 1 enters public beta. **6–9 April 2026:** "The Co-Pricing Factor Zoo" (arXiv:2604.04430), "Priced risk in corporate bonds" (arXiv:2604.05699) and the audit itself (arXiv:2604.07880). **August 2026:** NBER Working Paper 35578, the 128-year panel. **September 2026:** pipeline v4.2.1 (MIT; about five hours and 5 GB end to end, with WRDS access to TRACE, FISD and ratings), and on **24 September** PyBondLab 0.3.0 (MIT, Python 3.11+). *What it means for the desk:* in three years the field went from a retracted benchmark to an open, versioned pipeline; the audit is under revise-and-resubmit and not yet reproduced end to end by a second team, so a desk pins the version it used and says so. One gap is open: the OBAP site states no data licence, while the code repository is MIT.

## 9B.7 The Residual Is the Signal

*The scene below is a fictional composite. Vantress Capital Management, Wen Zhao, the pod's positions and the desk's runs are invented; the papers, their numbers and the borrow-market statistics are cited.*

Ines's desk had known Dov Adler's pod for two years as a stream of RFQs. On Thursday at 5:15 p.m. one of its analysts arrived in person. Wen Zhao carried the audit's survivor list, forwarded by Marcus Oyelaran of the platform's risk team (Marcus and Ines are in contact, Chapter 28), and the printout she calls the weather: the pod's borrow sheet, one row per borrowed bond, with lender, fee, share of the lender's inventory on loan, and a column no feed provides, two years of recall history.

"Your list and my sheet," she said, "have the same shape."

She was right. A within-firm sort, the construction behind 25 of the 26 survivors, ranks each issuer's bonds against each other (issuers with at least two), goes long the top-ranked bond and short the bottom-ranked one, and averages across issuers. The survivor list is a list of same-issuer pairs, equal-weighted and rebalanced monthly; the pod's book, where it is not cross-issuer, is a list of same-issuer pairs held for a thesis.

The momentum survivors read differently as pairs. Residual 12-1 momentum, `idimom12_1`, regresses each bond's returns on the bond market over a rolling 36 months (12 at minimum), the residual-momentum construction of Blitz, Huij and Martens, and sums the residuals over months $t-11$ to $t-1$. Within an issuer, the bond whose *own* part of its return has been strongest keeps outperforming its siblings: 1.55% a year, $t$ of 2.94, information ratio 0.87, equal-weighted. Its twin, systematic momentum `sysmom12_1`, sums the fitted market part instead, and the sign runs the other way: the bond that rode the market hardest underperforms its siblings, 2.20% a year once the sign is flipped. The strongest survivor of all, the six-month spread change, is momentum's opposite: within one issuer, the bond whose spread tightened most over six months earns less next month. Plain price momentum, industry momentum (a value-weighted single-sort alpha of 3.4–4.5% a year, $t$ of 2.1–2.4) and short-term reversal fail the correction. (Chapter 10, §10.5.4, meets the same idea one market over: residual *equity* momentum as a bond signal.)

Theo said the obvious thing, because it had become obvious only as he said it. "Everything that survives is a residual. The issuer cancels, the market cancels, and what's left is one bond against its sibling. The literature's survivor is your trade."

"It's my trade gross," Wen said. "Show me the short leg."

The short leg is where the audit stops and the pod begins; the paper is explicit that its survivors are gross of the cost of shorting bonds and of running same-issuer pairs. A within-issuer residual-momentum short is the issuer's laggard, disproportionately the small, old, off-the-run bond: the profile of an expensive borrow. Asquith, Au, Covert and Pathak (2013), the one large study of the bond loan market, find fees near 30 bp until about 70% of a lender's inventory is on loan, rising steeply after, and 173 to 245 bp around bankruptcy filings; Nashikkar and Pedersen find fees highest for risky, low-rated, small and old bonds; and every loan is recallable on demand. Wen pencilled in her own column, recalls in two years on a bond like each issuer's short leg, and marked the ones she would not touch.

"So who can trade it?" Theo asked.

"Someone who already pays for the borrow for other reasons," Wen said. "We have a prime broker, a lender list and a weather sheet because of our other pairs. For us the survivor is cheap at the margin; for anyone starting from zero it's expensive." Then she asked the platform's question, the one Marcus asks every morning: what would forty of these pairs be long that they did not mean to be? Residuals are less independent than their name suggests; Collin-Dufresne and coauthors found bond residuals highly cross-correlated, mostly through one latent factor (Chapter 7-B reads the test). In the desk's fictional run, the residual-momentum pairs' long legs leaned toward the shorter bonds in each issuer more often than chance: a bet on the shape of issuers' curves wearing a residual's clothes. It was small. It was not zero.

> **View From Another Seat.** *The multi-strategy pod.* A pod reads the survivor list as a sourcing tool, not a strategy. A within-firm sort removes the issuer and the market by construction, which is what the platform's x-ray wants to see; the pod adds what the paper leaves out: a borrow it can find, a stop it can size to (Chapter 8-B), and a thesis sentence for each pair it keeps. Described generically; Vantress is a fictional composite.

> **The Pair.** *Pair Book PB-03, read as data, and an unnumbered within-issuer pair. Dov Adler's pod at Vantress Capital Management is a fictional composite; Brambleworth Packaging is a fictional issuer; PB-03's legs are the real Ford Motor Credit and GM Financial notes of the 2020 replay (Chapter 8 §8.4, closed in Chapter 24 §24.7); every price and P&L figure is illustrative.* **PB-03, the data lesson.** When Wen rebuilt PB-03's March 2020 history on the clean panel, the hedge and the idio were unchanged. One day was not: the Ford Credit leg had printed a small lot several points low and the GM Financial leg a small lot several points high, and both snapped back the next morning. On a long Ford, short GM pair both prints register as losses and both reversals as gains: two fake returns of opposite sign, one large fake round trip. A daily pair series built from such prints acquires manufactured mean reversion, and the Ornstein–Uhlenbeck half-life of Chapter 7-B comes out too short. The fix is the chapter's fix, leg by leg: each leg gets its own signal price and its own return price, and neither is a flagged bounce. **The within-issuer pair.** *Legs:* long \$10mm market value of Brambleworth's 8% 2030s at 85 (spread duration 3.4, spread 700 bp), the top-ranked bond on residual momentum; short Brambleworth's 2028s at 92 (spread duration 1.8, spread 600 bp), borrowed. *Sizing:* DTS-neutral as in §8.4, so the short is $10 \times (3.4 \times 7.00)/(1.8 \times 6.00) \approx$ \$22.0mm market value, about \$23.9mm face. *What the hedge removes:* Brambleworth's spread beta, to first order, and the market's with it. *What idio remains:* the 2030s' residual against their sibling, the thing the survivor list says persists. *What leaks:* the issuer's curve shape, since DTS-neutral is not curve-neutral; the default jump, since pari passu bonds recover the same per unit of face, say 40, so the long loses $11.8 \times (0.85 - 0.40) \approx$ \$5.3mm while the short gains $23.9 \times (0.92 - 0.40) \approx$ \$12.4mm, leaving the "neutral" pair net short Brambleworth's default by about \$7mm (equal jumps need only about \$10.2mm face short; Chapters 12-B and 12-C own the switch of rulers near default); and carry, \$10mm earning 700 bp of spread against \$22mm paying 600 bp, about −\$0.62mm a year before a borrow fee of roughly \$70k at 30 bp, or \$0.4–0.6mm at the fees seen around bankruptcies. *Against what:* the survivor's gross edge, 1.55% a year in the paper's equal-dollar construction, is about \$155k on \$10mm. Equal-dollar pairs avoid this carry hole and carry more spread beta instead; every ruler moves the leak to a different column, and none makes it vanish (§8D.3). *Status:* not ledgered; Wen's pencil mark says why.

![Figure 9B.4: The two-leg bounce artifact. A long–short pair's daily P&L built from raw prints (grey) shows a sharp loss and a full reversal the next day, because a low print on the long leg and a high print on the short leg each register as a loss and then a gain; the same pair rebuilt from bounce-filtered prices with separate signal and return prices for each leg (black) shows neither. Illustrative, after the PB-03 replay of March 2020 (Chapter 8 §8.4); not real prints.](assets/figures/ch09b_two_leg_bounce.png)

Wen left at seven, with the survivor list folded into the weather. Theo walked her to the elevator and asked what she would do with it. "Read the pairs the paper likes and check whether we already own them for a reason," she said. "If we do, the paper is a second opinion. If we don't, it's a list of shorts I can't borrow." The elevator arrived. "Mostly the second."

## 9B.8 The Replication Harness

On Friday Theo wrote the spec for the thing the week had been building toward: a harness that every candidate signal passes through before it is allowed near the factor library. It is what the nightly `obap_repro` job of §9.9 now runs, and its first draft went the way first drafts to ROBO go.

*What ROBO built from the vague version.* The draft said *make the harness robust to outliers.* ROBO, which has read every statistics textbook and believes all of them, winsorized every holding-month return at the 0.5th and 99.5th percentiles of the full sample, the textbook default, and in doing so rebuilt, faithfully and without complaint, the exact filter that had moved the number in the cold open. Kaz looked at the output for a long moment and then laughed, which is the only correct response to a machine that has reproduced your mistake from first principles.

The precise spec is short. Every bond-month in the panel carries the signal read from the month-end price and from a price one to ten business days earlier, the following month's month-end and month-begin returns, the return already earned by the formation date, market value, rating, issuer, and the date of every price involved. The harness builds the long-short three ways: the contaminated reference, the signal-gap version and the return-gap version. Its first gate refuses to run the last two if any bond-month's signal price is dated on or after its return's starting price: *the signal price is never the entry price*, written as an exception rather than a hope. Its second gate allows only ex-ante screens; full-sample winsorization of the holding-month return appears once, as a diagnostic of how much a signal leans on look-ahead, never as a result. For each version it reports the premium, the CAPM-B alpha with Newey–West standard errors at $\lfloor T^{1/4} \rfloor$ lags (four, for 268 months), the share of the premium the gap removes, and the interquartile range of the premium across a grid of ex-ante screens and weightings: the non-standard-error band that sits beside the $t$-statistic in every report, with a path count that feeds the deflated Sharpe ratio of §7.8.

Why plain pandas when PyBondLab 0.3.0 exists? The production job does call PyBondLab's `SingleSort`, `WithinFirmSort` and `DataUncertaintyAnalysis` (whose panels need the columns `date`, `ID`, `ret`, `VW` and `RATING_NUM`) and pins it at 0.3.0, with the pipeline at v4.2.1, in every report's header; a harness whose every step is visible is how the desk checks the library, so Listing 9B.1 mirrors its conventions and the two run side by side. It applies to any signal built from bond prices, spreads or yields, and its ex-ante gate to any signal at all, since a full-sample trim leaks the future whatever the signal is made of. Daily signals, CDS-based signals and loan marks need the gap and the screens redefined for their own clock (Duarte, Jones and Wang's 2024 work on option quotes is the precedent for porting the logic to other quote-driven markets).

The edge case that bites is the universe. A month-begin return exists only for a bond that printed in the next month's first five business days, and a gap signal only for one that printed a week or two before month-end, so both versions drop illiquid bonds the contaminated version keeps, and part of any measured "bias" is a change of universe. The listing reports bond-month counts beside each version to show when the comparison is not like for like. Its synthetic demonstration checks §9B.4's arithmetic: a reversal signal on prices with half a percent of month-end noise and no true reversal earns roughly $2\kappa\rho\sigma_\delta$ contaminated and nothing with the gap.

*The full python listing is [Listing 9-B.1 in Appendix F](#code-9b-1).*

## 9B.9 What a Desk May Still Trade, Net of Chapter 9

Late on Friday Ines asked for one page, and the page was a table: the survivors grouped into families, the audit's gross numbers, a cost column pointing to Chapter 9's cost curve (§9.8–§9.10), to Dickerson, Nozawa and Robotti's delay costs and to Ivashchenko and Kosowski's (2024) capacity estimates, and a last column of the desk's judgement, labelled as such.

| Family | Construction | Gross alpha (audit) | The cost that bites | What is honestly left *(desk's judgement, illustrative)* |
| :-- | :-- | :-- | :-- | :-- |
| Credit-spread value | within issuer (`val_ipr`, `val_ipr_dts`) | 2.2–2.5% a year | two half-spreads inside one issuer; borrow on the rich bond; delay cost of about 0.11% a month for spread factors, if it applies here | the best candidate: roughly 1% a year before borrow; low turnover, so capacity is the least of its problems |
| Credit-spread value | single sort, value-weighted (long-only can hold it) | 3.71% a year, $t$ 2.12, fails FDR | rebalancing half-spreads; the same delay class | a tilt to size as a tilt, not a factor |
| Spread reversal within issuer (`dcs6*`) | within issuer | 2.46–2.66% a year | a faster signal, so more turnover and more delay | thin; fast signals are the ones delays kill |
| Residual and systematic momentum within issuer | within issuer, equal-weighted | 1.55% and 2.20% a year | equal weights mean small bonds; borrow on the laggard sibling; a momentum-class delay cost near 0.11% a month | for a pod that already pays for borrow; near zero for anyone else |
| Bond age | single sort, equal-weighted | survives FDR | small bonds | a characteristic to control for, not to trade |
| Short-term reversal, price momentum, illiquidity, default risk | any | gone after correction | none needed | nothing |

The cost column rests on one paper more than any other. Of 341 bond factors, Dickerson, Nozawa and Robotti (2025) find 58 with significant gross returns, averaging 0.28% a month of alpha; charge a realistic delay between signal and fill plus the bid–ask spread and the average falls to 0.09% for large trades and 0.05% for small ones, with two and one factors still significant. Delay costs run 0.11% a month for spread factors, 0.22% for equity reversal, 0.11% for equity momentum and 0.06% for volatility and risk; nine machine-learning models keep about a third of a 0.82% pre-cost alpha. Ivashchenko and Kosowski add capacity: market impact drives net returns to zero as a fund grows, fast for high-turnover strategies and slowly for low-turnover, credit-risk-focused ones. The first row's arithmetic is the desk's: 2.3% a year minus about 1.3% of spread-factor delay cost, before borrow.

*When it applies, and when it breaks.* Value survives correction, reversal does not, and momentum survives only inside an issuer: that holds in TRACE-era US data with the bond CAPM as the benchmark, and it breaks in three places. The null is contested: the audit's bond CAPM, the duration-adjusted CAPM of van Binsbergen, Nozawa and Schwert, the five-factor IPCA model of Kelly, Palhares and Pruitt (2023), the Bayesian-averaged discount factor of Dickerson, Julliard and Mueller (2026, out-of-sample Sharpe ratio 1.5–1.8) and Dick-Nielsen and coauthors' outright rejection of the CAPM would each give a different list, and a survivor list is only as good as its null. The sample is short, as the 128-year panel makes vivid. And the survivors are mostly pairs, a different object from the long-only portfolios most credit mandates hold. One diagnostic travels well: in options research, Duarte, Jones, Khorram, Mo and Wang (2026) show that filters using information unavailable at formation can inflate Sharpe ratios many times over, so a Sharpe ratio above about 2 on a monthly bond long-short is better read as a question about the filters than as a discovery.

> **Desk Myth vs. Desk Reality.** *Myth:* there are 108 bond factors. *Reality:* there are three families that survive correction (credit-spread value, a within-issuer spread reversal and residual momentum inside an issuer's own curve), every number on them is gross of costs, and two of the three are same-issuer pairs whose short leg is the bond nobody wants to lend.

> **View From Another Seat.** *The allocator.* An allocator meeting a systematic credit manager sees a short live record and a long backtest, the problem Chapter 4 describes from the manager's side. After 2026 the backtest has a second credential beside its Sharpe ratio: its lineage. Which pipeline version built the panel, which filters were chosen and when, whether the signal price and the return price differ, what the non-standard-error band is, and whether the factor reproduces the public corrected series. A manager who can answer in a page is offering a backtest that can be audited; one who cannot is offering a story. Described generically.

## 9B.10 Desk Debrief

At 6:10 on Friday the committee's chair sent a one-line email: *Accepted. Which version?* Theo answered with the report's header: pipeline v4.2.1, PyBondLab 0.3.0, a choice table with fourteen dated rows, and the harness with its two gates. Kaz wiped *ex-ante or it didn't happen* off the whiteboard, wrote *IDO or it didn't happen* back in its old place, then added the first one underneath. "Both apply." Mags pronounced the choice table better than Lenny at the pricing service, which from her is a citation. No cooperation agreement was signed this week, so the counter does not move; the Ad Hoc Group, asked for comment, stated through counsel that it is not a party to any TRACE print.

The desk added one line to the list that Appendix E keeps: *the signal price is never the entry price.*

- **The tape is a filing, not a market.** Cancels, corrections and reversals rewrite history weeks after a month closes, and a backtest inherits every dealer's exception queue, including the ones nobody on your desk can see. [L11, L14]
- **Every filter is a choice with a date, and the date comes before the first return.** Defaults stay in the panel; the default month loses its accrued interest, and the bond trades flat afterwards. [L11]
- **A month's return has two prices.** When the signal and the return share the month-end price, the gap return is the bias (correlation 0.99 in the audit); a signal gap or a month-begin return removes it, and price-based value keeps about half its premium. [L9]
- **Full-sample trimming is look-ahead.** Ex-ante screens act only on what was known at formation; six-month momentum's premium lived in the losers' rebounds that an ex-post trim deletes. [L12]
- **Report the non-standard error beside the standard error.** A band of 0.35% a month around an average premium of 0.33% means the cleaning choice moves the answer more than the answer, and the trial count for a deflated Sharpe ratio is at least 648. [L12]
- **What survives is the pod's trade.** Credit-spread value, a within-issuer spread reversal and residual momentum inside an issuer's curve, all gross of costs, mostly as same-issuer pairs whose short leg is the hard one to borrow. [L1, L10]

### The Spec You Hand the Robot

```text
ROBO: build replication_harness (Listing 9B.1) as a gate for every candidate bond signal.
Inputs: panel at formation date t with date, ID, firm, signal, signal_gap, ret_end, ret_bgn,
ret_lag, prc, VW, RATING_NUM, sig_px_date, sig_gap_px_date, end_base_date, bgn_base_date;
bond-market factor returns on both return conventions.
Gate 1: raise if any gated bond-month has signal price date >= return base price date.
Gate 2: screens may use only ret_lag, prc and formation-date flags; full-sample winsorization
of the holding-month return is a diagnostic, reported separately, never a result.
Output per version (reference, signal gap, return gap): premium, NW t, CAPM-B alpha, NW t
(lags = floor(T**0.25)), months, bond-months; gap share; look-ahead diagnostic;
NSE = IQR of premia across ex-ante paths, with the path count.
Header: pipeline version, PyBondLab version, choice-table hash. Stop and ask if unspecified.
```

### Exercises

1. **Eight rows.** In Odile's Brambleworth table (§9B.1), how many economic trades happened in that bond on Monday, and which row changes a return that was already published? *Solution.* Three: the 09:47 sale (as corrected), the agency pass (three rows, one trade) and the third dealer's 11:58 sale (after the decimal fix). The `Y` row removes a 29 September print from September's last-five-day window, so it changes September's month-end price and with it both September's and October's returns.
2. **Finer sorts, more noise.** With month-end noise $\sigma_\delta = 0.4\%$ and $\rho = 0.5$, what latent implementation bias does the §9B.4 formula give for terciles, quintiles and deciles? *Solution.* $2\kappa\rho\sigma_\delta$ with $\kappa \approx 1.09, 1.40, 1.75$: about 0.44%, 0.56% and 0.70% a month. Finer sorts select more extreme noise, which is why the most "significant" decile spreads deserve the most suspicion.
3. **The trimming band.** Using Listing 9B.1 on the clean panel, rebuild six-month momentum under four rules (ex-ante left, ex-ante right, ex-post left, ex-post right) at several thresholds, and report the band. What shape should the four lines have, and which number belongs in the report? *Solution.* The ex-ante lines stay near zero; ex-post right-tail trimming climbs toward about 0.60% a month at a 10% cut-off; ex-post left-tail trimming is negative until the cut-off is loosened to about −40% (§9B.5). The reported number is the ex-ante result with its interquartile band and path count; the ex-post lines are the look-ahead diagnostic.
4. **Change the ruler.** Re-size the Brambleworth pair of §9B.7 to be jump-neutral at a recovery of 40. What happens to the DTS hedge and the carry? *Solution.* The short becomes about \$10.2mm face (\$9.4mm market value). Its DTS is $9.4 \times 1.8 \times 6.00 \approx 101$ against the long's $10 \times 3.4 \times 7.00 = 238$, so about 58% of the long's spread beta is now unhedged, while carry turns positive, about $+\$0.14$mm a year. The leak moved from the default column to the beta column; it did not leave.
5. **Kaz's clever idea.** Kaz proposes building value from the vendor's *evaluated* month-end price, "which has no bid–ask bounce." Does the latent implementation bias go away? *Solution.* No. An evaluated price is still an estimate with an error, shared by the signal and the return's denominator, so the correlated error remains; it is merely smoother, and staler (Law 9: a mark is a moving average of the truth). The gap is still the fix, and Mags will want to know whether any of the marks sat at par for eleven months.

### Deep-Dive Resource Graph

**Podcasts.**

- **Ralph Smith: Scientific Investing in Fixed Income (S5E7)** (*Flirting with Models*, 11 Jul 2022). Breadth, liquidity and a bond's assumed availability as backtest inputs (§9B.2). https://www.flirtingwithmodels.com/episodes/kAEkSoYuRwd
- **Jeff Rosenberg: The Past, Present, and Future of Systematic Fixed Income (S7E19)** (*Flirting with Models*, 18 Aug 2025). "Characteristic specificity" in fixed income (§9B.9). https://www.flirtingwithmodels.com/episodes/8V74zBaN4jN
- **Greg Obenshain: Quantitative Credit (S4E12)** (*Flirting with Models*, 19 Jul 2021). "Even just acquiring data may be an edge": a statement about Stage 0. https://www.flirtingwithmodels.com/episodes/nQBct6plzWH

**Practitioner Writing.**

- Warwick Business School, "Flaw in data" account of the Bai–Bali–Wen retraction (10 Sep 2024), as told by Robotti (§9B.5). https://wbs.ac.uk/news/flaw-data-corporate-bond-investors
- QuantPedia, summary of Dick-Nielsen, Feldhütter, Pedersen and Stolborg, "Corporate Bond Factors: Replication Failures and a New Framework", the independent second audit (§9B.6). https://quantpedia.com/corporate-bond-factors-replication-failures-and-a-new-framework/
- FINRA, TRACE reporting timeframes, and the historic TRACE data file layout, for §9B.1. https://www.finra.org/filing-reporting/trade-reporting-and-compliance-engine-trace/trace-reporting-timeframes and https://www.finra.org/filing-reporting/trace/historic-data-file-layout-post-2612-files

**Academic Papers.**

- Dickerson, Robotti and Rossetti (2026), "The Corporate Bond Factor Replication Crisis," arXiv:2604.07880, and the 94-page version with the Internet Appendix (Tables 1 and 4, Figure 6, IA.3, IA.VIII–IA.XI). https://arxiv.org/abs/2604.07880 ; https://openbondassetpricing.com/wp-content/uploads/2026/04/corp-bond-replication-crisis-dickerson.pdf
- Dickerson, Nozawa and Robotti (2025), "Factor Investing with Delays," Hitotsubashi IER Discussion Paper A771: the delay-cost column of §9B.9. https://www.ier.hit-u.ac.jp/Common/publication/DP/DPS-A771.pdf
- Dickerson, Mueller and Robotti (2023), "Priced risk in corporate bonds," *JFE* 150(2), 103707 (arXiv:2604.05699), and the Bai–Bali–Wen retraction notice, *JFE* 150(3), 103721 (record: https://ideas.repec.org/a/eee/jfinec/v150y2023i3s0304405x23001617.html).
- Andreani, Palhares and Richardson (2024), "Computing corporate bond returns: a word (or two) of caution," *Review of Accounting Studies* 29(4); van Binsbergen, Nozawa and Schwert (2025), "Duration-Based Valuation of Corporate Bonds," *RFS* 38(1): the benchmark of §9B.3.
- Menkveld et al. (2024), "Nonstandard Errors," *Journal of Finance* 79(3); Jensen, Kelly and Pedersen (2023), "Is There a Replication Crisis in Finance?", *Journal of Finance* 78(5); Ghaderi, Plante, Roussanov and Seo, NBER Working Paper 35578 (Aug 2026), https://www.nber.org/papers/w35578: the error bar and the balance of §9B.6.
- Jostova, Nikolova, Philipov and Stahel (2013), "Momentum in Corporate Bond Returns," *RFS* 26(7); Asquith, Au, Covert and Pathak (2013), "The market for borrowing corporate bonds," *JFE* 107(1) (NBER version: https://nber.org/papers/w16282): the claim of §9B.5 and the short leg of §9B.7.

**Data & Code.**

- Open Bond Asset Pricing (panels, the 108-factor zoo, corrected Bai–Bali–Wen factors, Nozawa's duration-matched Treasury returns): https://openbondassetpricing.com
- `trace-data-pipeline` (v4.2.1, MIT) and its Stage 0 README, the filter order of §9B.2: https://github.com/Alexander-M-Dickerson/trace-data-pipeline
- PyBondLab 0.3.0 package metadata (24 Sep 2026, MIT): https://pypi.org/pypi/PyBondLab/json
- In this book: Listing 9B.1 (`replication_harness.py`) in Appendix F; the data-quality gates of Appendix B §B.16 and Chapter 27 §27.2; the `obap_repro` job of §9.9.


<!-- STATUS: COMPLETE -->
