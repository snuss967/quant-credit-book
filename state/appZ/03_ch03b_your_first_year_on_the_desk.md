## Z.3-B Chapter 3-B: Your First Year on the Desk: The Day, the Week, the Quarter, and the Twelve Mistakes Ex-Bankers Make

Seven exercises, all short calculations on the chapter's *Math, Gently* boxes and tables. None carries a [Read]/[Derive]/[Build] tag and none extends a listing, so there is no code to write, although Listing 3-B.1 (`desk_calendar.py`, Appendix F) reproduces the dates of Exercises 3 and 6 and the standard-error and Brier functions behind Exercises 1 and 5, and I ran it. I recomputed every number independently in Python, and all seven of the chapter's brief checks hold arithmetically. Three things are unusual. Exercises 2 and 7 are the same ghost (two photographs of one market) in DV01 units and in DTS units. Exercise 4 is the one §3B.6 points to ("Exercise 4 asks how far"). And Exercise 3's dates sit a week away from the dates in §12B, which I flag in a NOTE under Z.3-B.3. The chapter also has one embedded prompt, "write two things" after Wen's calendar strip in the Pair Book, but the text grades it itself (the missing row is the ratio's own date), so I have not numbered it. Write your answer down before you read ours.

**Z.3-B.1: Measurement, or how noisy a 55% hit rate is**

**Answer:** The standard error is 7.9 percentage points on 40 views and 2.5 points on 400. A 55% hit rate first sits two standard errors above 50% at 396 views, which is "about 400". Units: percentage points of hit rate. This is a physical-measure frequency of right calls, so no prices or risk-neutral probabilities are involved, and it assumes the views are independent.

**How:** The hit rate $\hat p$ is an average of $n$ coin tosses, so

$$
\text{SE}(\hat p)=\sqrt{\frac{p(1-p)}{n}}:\qquad \sqrt{\frac{0.2475}{40}}=0.0787,\qquad \sqrt{\frac{0.2475}{400}}=0.0249 .
$$

Ten times the views buys a $\sqrt{10}=3.16$ times smaller error, not a ten times smaller one. For the third part, set the five-point edge equal to two standard errors, $0.05=2\sqrt{0.2475/n}$, so $n=4(0.2475)/0.05^2=396$. If you use the null's standard error instead ($p=0.5$, variance $0.25$) you get exactly 400, which is why Figure 3-B.8 says "near 400". Now read the 40-view number honestly. The edge is $0.05/0.0787=0.64$ standard errors; the two-standard-error band runs from 39% to 71%; and the chance that a fair coin gives 22 or more right in 40 is 0.32 (exact binomial). "Two standard errors from zero" is also not the same as "reliably detected": to catch a true 55% with 80% power at the 5% level you need about 780 views.

**The trap:** Scaling the error linearly, so that 400 views gives $7.9/10=0.8$ points and 40 views already looks informative, or dropping the square root and getting a standard error of 0.6 points. Both make a year of forty bets look like evidence. The quieter slip is reading "55%, five points over a coin" as a result when the standard error is 7.9 points. A third, for later: the formula needs independent views, and two bonds of one issuer, or one sector in one sell-off, are not two views (Law 2), so the effective $n$ is smaller than the row count.

**If you got this wrong, read:** §3B.7 (the *Math, Gently* box and Figure 3-B.8); §28.2, "How noisy is your hit rate?" (equation 28.6) for the year-of-bets version; §7.8 for what happens to the standard error when you count how many things you tried.

**Z.3-B.2: The snap, or a perfectly hedged book that "loses" \$105,000**

**Answer:** Today's report shows a phantom loss of \$105,000. Tomorrow's shows a phantom gain of \$105,000, provided yields do not move between the two photographs tomorrow. True P&L is zero on both days. Units: dollars, with yields in basis points and DV01 counted positive for the long bonds, so yields up is a loss.

**How:** The bonds (DV01 \$35,000) are photographed at 4 p.m., after the 3 bp rise in yields. The short futures (DV01 equal and opposite) were photographed at 3 p.m., before it. The bond picture contains the loss and the hedge picture does not contain the matching gain. With the chapter's identity, $t_1$ = 3 p.m. for the futures and $t_2$ = 4 p.m. for the bonds,

$$
\Pi^{\text{book}}=-\text{DV01}_B\,\big(\Delta y_{t_2}-\Delta y_{t_1}\big)=-\$35{,}000\times 3=-\$105{,}000 .
$$

Tomorrow each leg is measured from its own yesterday mark, so the futures leg now carries the 3 bp it missed (a gain of \$105,000 on the short) while the bond leg carries only tomorrow's move. Add the two days and the ghost is gone. More precisely, tomorrow's phantom is $+\$105{,}000$ minus $\$35{,}000$ times tomorrow's own 3-to-4 p.m. yield move, so a fresh ghost is born every day and the old one dies. Nothing was traded, and a DV01-matched book valued at one common time loses nothing to a parallel move, which is why the true P&L is zero. The cure is one timestamp for risk and P&L (the 3 p.m. snap of Chapter 8-B).

**The trap:** Signing it as a gain ("yields rose, the book is short futures, so the hedge made money"). The hedge did make money, but its photograph was taken before the move, so the report shows only the bond's loss. The costlier slip is treating the \$105,000 as real: nobody should cut the position, and no stop should fire, on a number that reverses. But a stop that reads official P&L will fire anyway, which is why the snap is a treaty and not a nicety (the Pair Book makes the same point).

**If you got this wrong, read:** §3B.1 (the snap and the two *Math, Gently* boxes on DV01 and the random walk); §8C.3 (the timing line of the explain); §8.6 (the hedge matrix).

**Z.3-B.3: Halvorsen's event table, from §12B.9**

**Answer:** The missed coupon is \$18mm. The 30-calendar-day grace period ends on Sunday 13 December 2026 (Monday 14 December if the indenture rolls a weekend end forward). Day 28 is Friday 11 December 2026. Units: \$mm and calendar dates, with day 0 the missed date, as in §12B.9. No probabilities are involved, so the measure question does not arise.

**How:** The 6% notes pay semiannually, so the coupon is

$$
\$600\text{mm}\times\frac{0.06}{2}=\$18\text{mm}.
$$

Add 30 calendar days to Friday 13 November: 17 days take you to 30 November and 13 more to 13 December. Four whole weeks is 28 days, so day 28 lands on a Friday, 11 December, and two more days land on a Sunday. That Sunday is the interesting part. Whether a grace period that expires on a non-business day extends to Monday is a drafting question in the indenture, so `grace_end` in Listing 3-B.1 returns both dates (13 and 14 December) and refuses to choose. If it does not roll, the last business day of the grace period is Friday the 11th, which is the day the RSA is signed and the company files.

NOTE (for the editor): the dates here are a week away from the dates in §12B. The cold open of Chapter 12-B is Monday 23 November 2026 and says the coupon was missed "on Friday", which is 20 November, and §12B.9 puts day 28 on "the Friday before Christmas week", which is 18 December (20 November plus 28 days; the grace period would end on Sunday 20 December). This exercise, the Listing 3-B.1 test (`date(2026, 11, 13) + timedelta(days=28) == date(2026, 12, 11)  # day 28: RSA and petition (12B.9)`), Figure 3-B.4 and the Pair Book all use 13 November, 11 December and 13 December. The arithmetic is right in both chapters; they disagree by exactly seven days. Moving §3B's dates a week later (20 November, 18 December, 20 December, rolled to Monday 21 December) would reconcile them and would keep every weekday statement true (Friday, Friday, Sunday), though Figure 3-B.4 and the listing's tests would need a rerun. The exercise labels its date illustrative, but its heading and its check both tie day 28 to §12B.9, which places it elsewhere.

**The trap:** Four slips are common. Using the annual coupon (\$36mm). Reading "30-day" as 30 business days, which is 29 December, not 13 December. Counting 13 November as day 1, which puts day 28 on Thursday 10 December. And rolling the Sunday to Monday by reflex and reporting 14 December as *the* end: whether a weekend end rolls is a question for the indenture, not a default for the code.

**If you got this wrong, read:** §3B.4 (the list of contract clocks and the Halvorsen windows); §3B.11 (the edge case that bites, and `grace_end`); §12B.5 (the clock table); §12B.9 (the Halvorsen files and day 28).

**Z.3-B.4: JTD drift, or the right ruler on the wrong day**

**Answer:** The jump-neutral protection is now $(70-40)/(100-40)=0.5$ per unit of face, so \$5mm. Theo still holds \$8mm, so he is over-hedged by \$3mm of protection. If Halvorsen defaults at a 40% recovery, he makes \$1.8mm: \$4.8mm from the swap against a \$3.0mm loss on the bonds. Units: \$mm of notional, prices in points of par, default-day P&L. The 40% recovery is an assumed scenario value, not a probability, and no measure is involved.

**How:** The hedge ratio that leaves nothing to win or lose on the day of default is $N^{\text{JTD}}=(P-R)/(1-R)$ per unit of bond face. At 88 it is $48/60=0.8$, the \$8mm Theo bought. At 70 it is $30/60=0.5$. Check by the cash flows: the bonds lose $30\%\times\$10\text{mm}=\$3.0$mm (70 down to 40), and each \$1mm of protection pays 60 points, so \$5mm pays \$3.0mm and the book is flat; \$8mm pays \$4.8mm and the book is up

$$
\$8\text{mm}\times 0.60-\$10\text{mm}\times 0.30=+\$1.8\text{mm}=\$3\text{mm}\times 0.60 .
$$

So he holds a \$1.8mm bet that the company defaults, which he did not choose and which also costs him running premium on the extra \$3mm. It is a 40%-recovery statement, too: at 30% the same book makes \$1.6mm and at 50% it makes \$2.0mm (in \$mm the general form is $1+2R$), because the hedge is jump-neutral at one recovery only. Mistake 2 in §3B.6 ends on the right sentence: the ratio has a price in it, so it is a mark with a date.

**The trap:** Leaving the \$8mm in place because it was right at 88. The next-most-common answer is "he is over-hedged by \$3mm, so the extra bet pays \$3mm": protection pays par minus recovery, not par, so the extra \$3mm pays \$1.8mm. A third is rescaling by price, $8\times 70/88=6.4$, which has no basis in the payoff. And do not mix the two reference points: Figure 3-B.7's orange gap (\$5.0mm at 70) is measured against a \$10mm *face* hedge; this exercise measures against the \$8mm Theo actually holds.

**If you got this wrong, read:** §3B.6, mistake 2 and Figure 3-B.7; §24.3.1 (Theo's lunch ticket, "ten million cut to eight") and Listing 24.2's `jtd_hedge_ratio`; §12B.9 (PB-02, "hedge ratio is state-dependent").

**Z.3-B.5: Calibration, or saying 80% and being right 60% of the time**

**Answer:** Brier score 0.28 at the stated 80%, and 0.24 had he said 60%. Lower is better, the units are squared probability, and "50% every time" scores 0.25. The probabilities are Theo's subjective odds of being right, a physical-measure statement about his own calls, with no pricing measure anywhere.

**How:** A hit scores $(q-1)^2$ and a miss scores $q^2$. At $q=0.8$ a hit costs $0.04$ and a miss $0.64$, so

$$
\frac{3\times 0.04+2\times 0.64}{5}=\frac{1.40}{5}=0.28 .
$$

At $q=0.6$ a hit costs $0.16$ and a miss $0.36$, so $(3\times0.16+2\times0.36)/5=1.20/5=0.24$. Read the two numbers together. Three right out of five is better than a coin, yet 0.28 is *worse* than the coin's 0.25, because Theo said 80 and the world said 60. The score splits into the base-rate term $\bar y(1-\bar y)=0.6\times0.4=0.24$ plus a calibration term $(0.8-0.6)^2=0.04$, and 0.24 + 0.04 = 0.28. Saying 60% removes the calibration term. That is where honesty ends, though. He knows 60% only because he has seen the outcomes, so 0.24 is a benchmark and not a score he could have earned in advance (mistake 8 in miniature). And with five views the hit rate itself has a standard error of $\sqrt{0.6\times0.4/5}=0.22$, so the gap between 0.28 and 0.25 is not something a review can act on; log more views.

**The trap:** Scoring with absolute error, $(3\times0.2+2\times0.8)/5=0.44$, or forgetting to square. A second slip is reading the Brier score as "share wrong" (0.4). The third is the verdict: because the best constant forecast was 60%, concluding that Theo "should have said 60" is hindsight, and the review is asking whether his 80s come true about 80% of the time over a sample large enough to tell.

**If you got this wrong, read:** §3B.7 (the Brier box, and the calibration paragraph above it); §7-B.3 (calibration: is 4% really 4%?); §3.5 for the Edge Ledger that records the stated probability on the day it is formed.

**Z.3-B.6: ROBO's revenge, or what Columbus Day costs**

**Answer:** About \$5,556 (exactly \$5,555.56). Columbus Day is not a credit event, but it is a calendar event that costs money, so ROBO was wrong about the label and right that it mattered. Units: dollars, a 5% annual funding rate on ACT/360, one calendar day.

**How:** Monday 12 October 2026 is Columbus Day. SIFMA recommends a full close and the NYSE is open, so on a T+1 cycle the ETF shares settle Monday and the bonds settle Tuesday 13 October (the `settle_date` calls in Listing 3-B.1 return exactly those two dates for a Friday 9 October trade). The legs of one position are one day apart, so someone finances the value for the difference:

$$
C^{\text{gap}}=\text{Cash}\times r^{\text{fund}}\times\frac{\Delta d}{360}=\$40{,}000{,}000\times0.05\times\frac{1}{360}=\$5{,}555.56 .
$$

Who pays is whoever's leg settles first. In a redemption the AP hands over the shares on Monday and receives the bonds on Tuesday, so the AP is out the \$40mm for the day; in a creation the direction flips and the fund finances it. Appendix D's one-liner, "whoever delivers cash first", is the same idea in cash terms, and here both legs are securities. Veterans Day (11 November 2026) does the same thing, and a model that sets every settlement date equal to its trade date books this cost as zero.

**The trap:** Two ways to miss. One is the label: following ROBO and flagging 12 October as a credit event, when nothing about any issuer changed. The other is arithmetic: forgetting the day fraction (\$40mm at 5% is \$2mm a year), counting the weekend and getting a three-day gap (the gap is Monday to Tuesday, one day), or using 365 and reporting \$5,479, a \$76 difference that is the convention talking. The costs per event are small. The danger is the break, not the dollars.

**If you got this wrong, read:** §3B.10 (holidays that differ by venue, and ROBO's mistake); Appendix D §D.1 (the settlement gap and its formula); §20.6.1 (the settlement gap and the liquidity runway in an ETF).

**Z.3-B.7: The pair's two photographs**

**Answer:** Today's explain shows a phantom loss of \$120,000 for the pair from that hour. Tomorrow's shows a phantom gain of \$120,000, provided spreads do not move between the two photographs tomorrow. The hour's true P&L is zero, because the pair is DTS-neutral. Units: dollars, with DTS in the chapter's units (face in \$mm $\times$ price/100 $\times$ spread duration $\times$ spread in bp), so one unit of DTS is worth \$1 per 1% relative move in spreads. These are realized market moves, not probabilities.

**How:** Let $m_t$ be the move in spreads as a fraction of their level since yesterday's snap. A spread move $m$ changes a leg's value by $-100\,\text{DTS}\times m$ dollars (a long leg loses when spreads widen, a short leg gains). The short leg is photographed at $t_1$ = 3:00 and the long at $t_2$ = 4:00, so the report carries

$$
\Pi^{\text{phantom}}_{\text{pair}}=-100\,\text{DTS}_S\,\big(m_{t_2}-m_{t_1}\big)=-100\times 60{,}000\times 0.02=-\$120{,}000 .
$$

In words: the long, marked at 4:00, shows its \$120,000 loss from the widening, and the short, marked at 3:00, has not yet shown its matching \$120,000 gain. Mark both at 4:00 and the two cancel, which is the true P&L of zero. Tomorrow the short's photograph catches up and the sign flips, with a fresh ghost of its own if spreads wander between 3:00 and 4:00 again. The formula uses the DTS of the early-photographed leg and is a statement about timing only. If the legs were not DTS-neutral, the hour would also carry a real P&L of $-100\,(\text{DTS}_L-\text{DTS}_S)\,m_{t_2}$, and that part does not reverse. The chapter's own use of the formula is the same arithmetic at 85,000 of DTS and a 1% move: the $-\$85{,}000$ of the Pair Book's last hour.

**The trap:** Dropping the 100 and getting \$1,200, or using 2 for 2% and getting \$12 million. The conceptual trap is Exercise 2's: thinking the loss is real because both legs are marked and the report foots. It is a timing artefact and it reverses, which is also why it must not be allowed to trip a stop that reads official P&L. A subtler slip is the sign: the number missing from the report is the short's gain, so the pair shows a loss, not a gain.

**If you got this wrong, read:** §3B.4, "The Pair Book: Two of Every Clock" (the phantom formula and the calendar strip); §3B.1 (the same ghost with DV01); §1B.2 and §8D.3 (the DTS ruler); §8C.3 (the timing line of the explain) and §8C.6, morning (c) (the pair at Vantress).

<!-- STATUS: COMPLETE -->
