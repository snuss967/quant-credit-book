# App Z editor notes (chapter-text discrepancies found while solving)

### 01_ch01b_a_week_in_five_quant_shops

NOTE (for the editor): §1B.4 and the Desk Debrief both say "a mark is a choice made inside the bid-ask spread," but the scene's composite is 77 bid, 78.50 offered, and Hal marks at 79. That is 0.50 above the offer and 1.25 above the 77.75 mid, so the mark is outside the spread, not inside it. The \$75,000 and the "about 70 bp of spread" (my check: 1.25 points on \$6mm is \$75,000, and \$75,000 / \$1,076 a bp is 69.7 bp) are right for a 79 mark; it is the sentence about the spread that fails. Either the composite's offer needs to be at least 79 or the senior trader's instruction needs to be at most 78.50.

### 02_ch02b_transaction_cost_analysis_for_credit

NOTE (for the editor): This exercise is titled "Ninety minutes on one leg," but the text says the long leg fills "45 minutes before the short," and the chapter's check (\$42,500 and \$28,100) uses 45. The 90 comes from the April PB-01 opening in §2B.7, where the pod was one-legged from 9:50 to 11:20. At 90 minutes the same inputs give \$60,048 unhedged and \$39,718 with the 0.75 bridge. The check values are right for 45 minutes; the title should say "Forty-five minutes" or the text should say 90.

### 02_ch02b_transaction_cost_analysis_for_credit

NOTE (for the editor): §2B.6 concludes that "nearly all of Mags's jump was the market getting smaller on paper," using an 8% cut: $18.6\% / 0.92 = 20.2\%$, which is 1.6 of the 1.7 points observed (95%). But 8% is the top of MarketAxess's "up to 8%" for June 2026, and FINRA's own baseline is up to 5.7% (in trades, not dollars). At 5.7%, 18.6% becomes 19.7%, only 1.1 points or 66% of the jump, and September's like-for-like reading is 19.1%, not 18.6%. "Inflated by up to 8%" can also mean reported volume was 1.08 times true, which is 7.4% removed and gives 20.1%. Consider "most of" in place of "nearly all," or say which reading of the 8% is used.


### 03_ch03b_your_first_year_on_the_desk

NOTE (for the editor): the dates here are a week away from the dates in §12B. The cold open of Chapter 12-B is Monday 23 November 2026 and says the coupon was missed "on Friday", which is 20 November, and §12B.9 puts day 28 on "the Friday before Christmas week", which is 18 December (20 November plus 28 days; the grace period would end on Sunday 20 December). This exercise, the Listing 3-B.1 test (`date(2026, 11, 13) + timedelta(days=28) == date(2026, 12, 11)  # day 28: RSA and petition (12B.9)`), Figure 3-B.4 and the Pair Book all use 13 November, 11 December and 13 December. The arithmetic is right in both chapters; they disagree by exactly seven days. Moving §3B's dates a week later (20 November, 18 December, 20 December, rolled to Monday 21 December) would reconcile them and would keep every weekday statement true (Friday, Friday, Sunday), though Figure 3-B.4 and the listing's tests would need a rerun. The exercise labels its date illustrative, but its heading and its check both tie day 28 to §12B.9, which places it elsewhere.

### 04_ch04b_bond_math_for_the_desk

NOTE (for the editor): §4B.6 says that on an upward-sloping curve a high-coupon bond has "$Z > G$," and the Trend Watch in §4B.7 says the 2022–24 inversion "flipped the sign of $Z - G$ for high-coupon bonds." In the book's own continuous convention, the real 23 March 2020 curve (clearly upward-sloping) gives $Z - G = 809.4 - 824 = -14.6$bp, not a positive number, because the +4.9bp shape term is smaller than the $-19.5$bp compounding gap. The sentence is true of the shape term alone, or of Z quoted in the bond's own compounding (828.9 against 824). It is true of the full $Z - G$ only when the curve is steep enough: a 6.5% ten-year priced at $G = 400$bp has $Z - G = +5.4$bp on 31 March 2021 (2s10s +158bp) and $-15.9$bp on 3 July 2023 (2s10s −108bp). Consider "the shape term in $Z - G$ changes sign," or a clause naming the convention.

### 04_ch04b_bond_math_for_the_desk

NOTE (for the editor): the last make-whole assert in Listing 4-B.1 (`lattice_price(flows_fa, dt_fa, rates_fa, z_mar, mw_calls, 0.005) - lattice_price(flows_fa, dt_fa, rates_fa, z_mar)`) runs after the `for d, (y_b, y_t) in dates.items()` loop, so `flows_fa`, `dt_fa` and `rates_fa` are the tree left over from the last iteration, 30 June (0.66% curve), while `z_mar` is the 23 March spread (804.5bp). I checked: the leftover tree equals the 0.66% tree, not the 0.76% one. The assert passes either way (the difference is 0.0), and the in-loop OAS assert already covers each date, but the line reads as if it tests 23 March. Moving it inside the loop, with `table[d]["Z"]`, would make it test all three dates, as the exercise asks.

### 04_ch04b_bond_math_for_the_desk

NOTE (for the editor): the inline solution says "YTW jumping when the workout date changes." Yield-to-worst is a minimum of continuous functions of price, so it kinks but does not jump. On Brambleworth it is 9.253% at a price of 99.99 and 9.247% at 100.01, while the workout moves from year 5 to year 4. What jumps is the workout date and, with it, the benchmark Treasury and the duration, so a spread-to-worst (YTW minus the Treasury at the workout date) falls 19bp on the 3 July 2023 curve as the price crosses 100. Consider "spread-to-worst jumping when the workout date changes."


### 04_ch04c_other_seats_at_the_table

There are six exercises, all at the end of §4C.10; each already has a one-paragraph solution printed beside it, none carries a [Read]/[Derive]/[Build] tag, and none is embedded elsewhere in the chapter. Exercises 1 to 3 are arithmetic on the chapter's Math, Gently boxes; 4 asks you to name the leaks in the PB-02 pair and has more than one defensible answer; 5 is a definition with a small numerical check; 6 is conceptual and points at Listing 4-C.1 in Appendix F without asking you to extend it. Nothing here uses a risk-neutral probability: every number is a price in cents on the dollar, a dollar amount in \$mm, or a rule from an indenture or a capital table, so $\mathbb{P}$ versus $\mathbb{Q}$ never comes up. The printed solutions hold up on the arithmetic; where the chapter's text or listing disagrees with my computation I say so in a NOTE (for the editor).

### 04_ch04c_other_seats_at_the_table

NOTE (for the editor): The printed solution says the pair "was sized jump-to-default flat, not spread flat, and lost about \$200,000 on day 12." The \$196,000 is right, but the chapter's own "What leaks" paragraph attributes only about \$33,000 of it to the ruler; about \$163,000 is the CLO month-end landing on one leg. As worded, the solution sends the reader to the wrong cause. Suggest: "a flow that hits one leg before default (\$163,000 of the \$196,000 on day 12) and the ruler (\$33,000)".

### 04_ch04c_other_seats_at_the_table

NOTE (for the editor): In the same "What leaks" paragraph the long's implied move is "about three and a half" points and the remainder "a point and a half, about \$163,000". The scaling is $8 \times 40/95 = 3.37$ points, which leaves $5 - 3.37 = 1.63$ points, and 1.63 points on \$10mm is \$163,000; "a point and a half" on \$10mm would be \$150,000. The dollar figure is right and the two roundings are not. Suggest "about three and a third" and "about a point and two-thirds".

### 04_ch04c_other_seats_at_the_table

NOTE (for the editor): The chapter says "On day 8, before the downgrade, Halvorsen's version of that number was already high" (§4C.4) and that "the day-8 `forced_pressure` reading had flagged" the CLO selling (the PB-02 box). The listing returns 0.0 whenever `rated_ccc` is false, and Halvorsen's loan was not cut to Caa1 until day 9. I ran Listing 4-C.1 on five illustrative CLO records: day-8 result 0.0 with `rated_ccc=False`, 0.0515 with `rated_ccc=True`. Even then the cushion used would be the reported one (Rachel's flagship at 7.3% against 7.5%, slack +0.2 points, tightness 0.90), when the pro-forma slack after the loan's own downgrade is $7.5\% - 7.9\% = -0.4$ points. To make the day-8 claim true the gate needs "one notch from CCC or on negative watch" (compare "Ways This Blows Up" (3) in §21.4.3) and a pro-forma slack field. Otherwise the text should say "day 9".

### 04_ch04c_other_seats_at_the_table

NOTE (for the editor): §4C.9 says "Chapter 21 uses the score as `forced_pressure` (§21.4, §21.7)". The string `forced_pressure` does not appear in Chapter 21; the index there is the Forced-Sale Pressure Index (FSPI) of §21.4.3, which weights each CLO by a logistic function of junior cushion and CCC excess, not by $e^{-s/0.02}$. Either rename or add a sentence saying that the two are the same idea with different functional forms.

### 04_ch04c_other_seats_at_the_table

NOTE (for the editor): The cold open says the carry line reads "+\$2,417, three days of coupon on \$12mm under 30/360". Annual coupon on \$12mm at 7.25% is \$870,000, which is \$2,416.67 per 30/360 day; three days is \$7,250. \$2,417 is one day. Either say "one day of coupon" or make the line +\$7,250 (Friday to Monday is three 30/360 days).

### 04_ch04c_other_seats_at_the_table

NOTE (for the editor): The seat table in §4C.9 gives the dealer's check as "Daily; committee on day 3". The text puts the risk committee on Wednesday, which is day 4 (the cold open fixes day 3 as Tuesday), and has Dana selling on Tuesday ahead of it. As I read it the table should say "committee on day 4; sold ahead of it on day 3".


### 04_ch04d_getting_the_seat

NOTE (for the editor): §28.4 pairs the slope $-2.69$ with "a recovery is known to perhaps $\pm 15$ points, which moves it by about 32". Multiplying 2.69 by 0.15 gives 40, not 32. The 32 is the exact move to $L = 0.75$ ($0.969/0.75 - 0.969/0.6 = -0.323$), which is smaller because $f^*$ is convex in $L$. The 36 for PD, by contrast, is slope times change. One clause in §28.4 saying the recovery figure is the exact change would stop a careful reader from checking it against the slope. §4D.5's "takes it to 60%" is exact and fine.

### 06_ch06b_options_and_measures_for_credit

NOTE (for the editor): Exercise 1 asks for Larkspur's "second-lien notes," but Chapter 13 gives Larkspur only a 2029 first-lien term loan (marked 84), an Ad Hoc Group holding 51.3% of it, and no second lien, no face amounts and no enterprise value; the \$1.95bn and \$450mm are Serta's. A reader cannot check an answer against the book. I used \$1,000mm, \$400mm, \$1,200mm, 22% and three years, calibrated to the 84 mark. Suggest the exercise state a stack, and say whether the inserted tranche's face is also added to $V$ (new money) or not: with $V$ fixed the old first lien's delta rises most (+0.069), and with the face added to $V$ the three changes are +0.010, −0.022 and +0.012.

### 06_ch06b_options_and_measures_for_credit

NOTE (for the editor): The cold open multiplies $-0.199$ by 200,000 hundreds of face to get $-\$39{,}800$ and calls the figure "per 100 face." But $-0.199$ is the §6-B.3.4 table's figure for the §6.2.4 firm's debt, whose face is 80 (a bond worth 75.22). Per 100 face the vega is $-0.199\times100/80=-0.249$, which matches the table's own spread vega: 26.5 bp per vol point times a price of 94.03 per 100 face. Twenty million of face is then $-\$49{,}900$ per vol point, 122% of the −\$41k rather than 97%, and the other forty bonds and the CDX would net to about +\$8.9k, not −\$1.2k. Two repairs: size the double-B at about \$16mm of face ($0.249\times160{,}000=\$39{,}900$), or keep \$20mm and change the book total, the "ninety-seven percent" and the "minus twelve hundred dollars."


### 07_ch07b_statistics_for_credit_panels

NOTE (for the editor): The printed solution says the monthly grid "converges to about 17.1%", a 5.9-point bias, "about 70 standard errors", with a standard error of 0.084 points. The 17.1% is the Broadie–Glasserman–Kou shifted-barrier approximation of §7-B.8, $2\Phi(-1.37)$, which that section labels approximate. The actual 12-date discrete-monitoring probability is 17.58% (numerical integration of the kernel), and the listing's naive simulation lands there too. That agrees with the Figure 7-B.5 caption ("understates the exact 23.0% by 5.4 points at monthly dates") and with Listing 7-B.2's "the naive grid gives 0.176", and it disagrees with the solution's 5.9. At 17.6% the bias is 5.4 points, the standard error is 0.085 points and the miss is about 64 standard errors. Either quote 17.6% and 5.4 points, or say that 17.1% and 5.9 points are the approximation.

### 08_ch08b_the_risk_model_and_the_limit_sheet

NOTE (for the editor): The "Math, Gently" box in §8B.8 says of the likelihood ratio and the $\chi^2$ distribution "The full version is §7-B.2", and the "Builds on" line lists §7-B.2. Section 7-B.2 is "Overlapping Returns, Autocorrelation and Newey–West": it has no likelihood-ratio test, no binomial counting and no $\chi^2$ test, and a search of all of Chapter 7-B finds no $\chi^2$ anywhere (the nearest material is the maximum-likelihood logit of §7-B.3 and the survival likelihood of §7-B.4). Kupiec and Christoffersen are named nowhere in the book outside Chapter 8-B and its Appendix F listing. Either a short box on likelihood-ratio tests belongs in Chapter 7-B, or the pointer should go.

### 08_ch08b_the_risk_model_and_the_limit_sheet

NOTE (for the editor): §8B.8 says Basel's yellow zone (five to nine exceptions in 250 days) is "the same verdict in another dialect". It matches only at seven. By my computation Kupiec's LR is 1.96 at five exceptions (p = 0.16) and 3.56 at six (p = 0.059), so it does not reject at 5% where Basel already says yellow; it first rejects at 5% at seven (5.50) and at 1% at eight (7.73, p = 0.005), nine gives 10.23 (p = 0.001), where Basel is still yellow. The Basel zones come from cumulative binomial probability (89.2% at four, 95.9% at five, 99.975% at nine, 99.995% at ten), a one-sided rule with its own cut-offs. "A neighbouring verdict" would be accurate; the exercise's check line ("the yellow zone of Basel's traffic light") leans on the same equivalence.

### 08_ch08b_the_risk_model_and_the_limit_sheet

NOTE (for the editor): The exercise sends the reader to §12B.9 as "the issuer whose bankruptcy §12B.9 follows", but the two chapters disagree about the paper. Section 12B.9's table has the 7.25% notes due 2029 as \$500mm of *senior secured* notes, pari passu with the term loan, priced at 61 on 23 November and recovering 60.8% under the plan; the unsecured bonds are the 6% 2031s (price 9, plan recovery 1.5%) and the 3% 2045s, and there is no junior note at 31. Chapter 8-B treats the same 7.25% 2029s as a senior unsecured bond (the "40 every senior unsecured bond gets", cut to 15). If the exercise's recovery for the notes were §12B.9's 60.8%, their JTD would be $12(0.78 - 0.608) = 2.06$, that is \$2.06mm, and nothing would need clearing. The October 15% is the desk's pre-petition view, so the numbers can both stand, but the exercise should say the junior note is a stand-in rather than a §12B.9 claim, and the name differs too: Halvorsen Building Products in the cold open, Halvorsen Packaging in §8B.9 and Chapter 12-B.

### 08_ch08b_the_risk_model_and_the_limit_sheet

NOTE (for the editor): The printed solution says ES is "computed on end-of-day positions at the 15:00 New York snap". ROBO buys back at 3:59 p.m., which is after 15:00, so if that phrase is read as the position held at 15:00 then ROBO's book is flat at the snap (ES zero) and the plan passes; it works only if "end-of-day positions" means positions carried overnight, valued at the 15:00 prices. The sentence also has no stopping rule: "the trades of least expected cost" lets ROBO sell everything if that is the cheapest way to remove ES. Suggest "on the positions carried overnight, marked at the 15:00 New York snap" and "reducing only as far as the soft line".

### 08_ch08c_the_morning_explain_pnl_attribution

NOTE (for the editor): §8C.1 says Chapter 4-B gives the constant-yield $\theta_i = y_i P_i - 100\,c_i$ and the roll-down term. I cannot find either in §4B; the nearest text is §8.1, "The thirty-seven cents, itemized" (pull is $y\,\Delta t - c\,\Delta t/P$), so the pointer probably wants to be §8.1. Separately, the formula is first-order: for this exercise's bond it is within 1% of the exact drift ($0.00593$ at 10.2%, against $0.00598$ exact), but in the Math, Gently box a bond exactly five years out on a coupon date drifts \$494 a day on \$10mm at a constant 9.04%, against the box's \$530 (the formula at the box's rounded 9.0% gives \$533). The \$530 is right for a bond about 4.87 years out. A clause saying where in the coupon cycle the box's bond sits would settle it.

### 08_ch08c_the_morning_explain_pnl_attribution

NOTE (for the editor): §8C.5 says equal split gives each signal "its standalone value *minus* half the interaction: momentum $3.0 - 1.3 = 1.7$", but the interaction is defined one line earlier as $2.4 - 3.0 - 2.0 = -2.6$, so the rule as written gives $3.0 + 1.3 = 4.3$ and $2.0 + 1.3 = 3.3$ (summing to 7.6, not 2.4). The 1.7 and 0.7 are right (and equal Shapley); the wording should say "plus half the signed interaction" or "minus half the overlap of 2.6". This exercise's check, 1.5 and 1.1, uses the "plus" form.

### 08_ch08c_the_morning_explain_pnl_attribution

NOTE (for the editor): this exercise calls the 7.25% 2029s "secured notes", which matches §12B.9 (senior secured, pari passu with the term loan B, and the arithmetic needs them in the first-lien class). §8C.6, Morning (c), and §1B call the same notes "senior unsecured", and the pod's short in PB-01 is that bond. One of the two descriptions has to change, and the choice decides whether PB-01's short sits in the first-lien class that ends up with the takeback notes.

### 08_ch08c_the_morning_explain_pnl_attribution

NOTE (for the editor): §8C.8 (and the "Builds on" line) says "Appendix B §B.16 lists the evidence to keep for each [corporate] action". §B.16 is "Specification for AI Implementation: The Tidy Bond Panel", and Appendix B does not mention corporate actions or exchange offers at all. The pointer needs a new target, or the evidence list needs writing.

### 08_ch08c_the_morning_explain_pnl_attribution

NOTE (for the editor): §8C.6(b) says the Corriveau true-up of $-\$240{,}000$ is "24 bp of NAV, two and a half times the day's tolerance". With the §8C.4 policy on \$100mm of NAV and \$1.5mm of ES the tolerance is \$10,000, so $240{,}000/10{,}000 = 24$ times (and 3.2 times even the 5%-of-ES term of \$75,000). "Two and a half" matches neither; "twenty-four times" is what the chapter's own policy gives.

### 08_ch08c_the_morning_explain_pnl_attribution

NOTE (for the editor): the printed check says "when the idio line is negative, the ledger prints the lines and leaves the ratio blank". I cannot find that rule anywhere else in §8C or §8D.6, and the companion listing does not implement it: Listing 8-D.1's `capture(idio, leak, friction)` is `(idio + leak + friction) / idio` with no guard, so this exercise's 4:00 case returns 3.4 and an idio of exactly zero raises `ZeroDivisionError`. Either state the rule in §8D.6 and add the guard (`None` when `idio <= 0`), or drop the sentence from the check.

### 08_ch08d_the_pair_book_long_one_credit_short_another

NOTE (for the editor): The Cold Open gives the lender's inventory as \$300 million *face* and the short as \$60 million market value (about \$61 million face), but §8D.5 says the 20% cap "on \$300 million is \$60 million, exactly the current short", and Listing 8-D.1 documents `inventory` as "lendable market value, \$mm". In one unit the two do not match. In face the cap is \$60.0mm against a current short of \$61.2mm face, so the pod is already \$1.2mm over; in market value the cap is \$58.8mm against \$60.0mm. The borrow-based size is then \$26.1mm rather than \$26.7mm. The stop still binds at \$22.5mm, so nothing downstream moves. Suggest stating the unit once and saying "about the current short".

### 08_ch08d_the_pair_book_long_one_credit_short_another

NOTE (for the editor): §8D.4 calls a \$23.2 million loss "5.8% of capital" that is "past the first of the two lines" (5% and 7.5%). Dov's own first line is \$24 million (§1B.2), which is 6.0% of \$400 million, not 5% (\$20 million). From a flat book \$23.2mm leaves \$0.8mm of room under \$24mm; it breaches only because the book is already \$11mm down (the distance is \$13mm). Either say "past the 5% line of the press-reported template" or give Vantress a \$20mm first line.

### 08_ch08d_the_pair_book_long_one_credit_short_another

NOTE (for the editor): The §8D.3 scenario table (\$85.6mm; +138, +205 and +385 in \$000) is built on the rounded ratio 2.14. At the unrounded 2.142857 that Listing 8-D.1's `scenarios` and self-check use, the same cells read \$85.7mm, +139, +206 and +386. The listing's own assert (0.2057 at `atol=1e-3`) passes either way. One clause ("at a ratio rounded to 2.14") would stop a reader who reproduces the table from missing by \$1,000.

### 09_ch09b_the_bond_data_problem_and_the_replication_crisis

NOTE (for the editor): The printed solution, and Theo's "September's month-end price for this bond just changed" in §9B.1, hold only on an assumption the scene does not state. Under the pipeline's rule (the last daily VWAP inside the final five business days), deleting the 29 September print moves the month-end price only if the 29th was the bond's last printing day in that window. If the bond also printed on the 30th, the 30th sets the price and nothing changes. If the \$500,000 sale was the only print in the window, September has no month-end price at all, so September's and October's returns do not move, they vanish. Suggest "can change" or one clause saying the 29th was the bond's last print. The sale also belonged to the 2028s, so presumably a corrected as-of report lands in that bond's September window and moves its history too.

### 09_ch09b_the_bond_data_problem_and_the_replication_crisis

NOTE (for the editor): The exercise asks for four lines "using Listing 9B.1", but the listing supplies only two of them. `exante_screen` gives the ex-ante left and right lines, while `expost_winsorize(panel, ret, q)` clips both tails at percentiles, so it cannot give a one-sided ex-post line or a threshold in return units (10%, $-40\%$). A reader must write the one-sided trim, as I did. Because the harness's look-ahead diagnostic is the symmetric version, it can net the two tails to almost nothing (it read $-0.09\%$ in my synthetic panel while the one-sided lines were $+0.47\%$ and $-0.43\%$). Suggest a `tail` argument on `expost_winsorize` or a one-line remark in §9B.8.

### 09_ch09b_the_bond_data_problem_and_the_replication_crisis

NOTE (for the editor): The listing's default grid is `caps` of 0.20 to 0.95 in steps of 0.05, which is 16 thresholds, times three tails, times two weightings: 96 paths. That is the audit's 48 return screens times two weightings, a subset of the 648 data paths (108 filters, including 30 price ranges and 30 bounce filters, times equal and value weighting, times all bonds, investment grade and high yield). §9B.8 says the path count "feeds the deflated Sharpe ratio" and §9B.6 says the honest trial count is "at least the 648", so a reader who copies the harness's `paths: 96` into the deflated Sharpe ratio under-counts. Suggest one sentence in §9B.8 saying the default grid is 96 of the 648 and the trial count should be the full grid's.

### 09_ch09b_the_bond_data_problem_and_the_replication_crisis

NOTE (for the editor): The Pair box in §9B.7 puts the borrow fee on face. Thirty bp on \$23.9mm of face is \$72k ("roughly \$70k"), and 173 to 245 bp on face is \$0.41mm to \$0.59mm ("\$0.4–0.6mm"). Securities-lending fees accrue on the loan's value, which is market value (the PB-03 entry in §8.4 charges 35 bp on \$36mm of market value). On the \$22.0mm market value the figures are \$66k and \$0.38mm to \$0.54mm, so "\$0.4–0.5mm". The gap is small, but a reader who recomputes the jump-neutral short's fee on its \$9.4mm market value gets \$28k at 30 bp and \$0.16mm to \$0.23mm at bankruptcy-era fees, and will wonder which base the chapter used. The unrounded face of the DTS short is \$23.95mm, its gain \$12.46mm and the net default exposure \$7.16mm, so "about \$7mm" stands.

### 27_ch27_system_architecture_and_asics

NOTE (for the editor): The exercise says "rerun block 3 with $c_s^2 = 1$." Block 3 (Listing 27.3) hard-codes the $c_s^2 = 4$ answers, so with `CS2 = 1.0` it stops at its first assert, `abs(ew - 233.33) < 0.01`, because the mean wait is now 93.3 ms; the p99-sojourn assert (1,000 to 2,400 ms) would fail as well, at about 610 ms. Suggest adding "and update the asserts," or readers will think they broke the listing.

### 27_ch27_system_architecture_and_asics

NOTE (for the editor): §27.7.2 says that to first order $\text{ARL}_1 \approx \ln(\text{ARL}_0)/\mathcal{K}$. As an asymptote that is right, but at the chapter's own example ($\delta = 1$, $c = 5$, $\text{ARL}_0 = 938$) it gives 13.7 fills against the 10.3 quoted in the same paragraph, and at this exercise's $\delta = 0.75$ it gives 29.7 against Siegmund's 21.6. The next-order form $\big(\ln(\mathcal{K}\,\text{ARL}_0) - 1\big)/\mathcal{K}$ gives 10.3 and 21.6. Suggest using it, or adding "overstates the delay by about a third at these settings."
