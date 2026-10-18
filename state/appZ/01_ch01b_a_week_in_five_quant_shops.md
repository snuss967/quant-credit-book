## Z.1-B Chapter 1-B: A Week in Five Quant Shops

Six exercises, all short calculations on the chapter's *Math, Gently* boxes. None carries a [Read]/[Derive]/[Build] tag, and none extends the week-log listing in Appendix F (Listing 1-B.1), so there is no code to run. I recomputed every number in the chapter's brief solutions and they all hold; the places to be careful are signs, units (points versus dollars, face versus market value) and one scene detail that I flag in a NOTE under Z.1-B.5. Write your answer down before you read ours.

**Z.1-B.1: The river on a passed trade**

**Answer:** The trade the engine did not do has a markout of $+\$45{,}000$, which is $+187.5$ bp of price. I read "an RFQ to buy" the way the chapter's own box does: the engine would have been the dealer paying 80. Dollars, one-hour horizon, measured against the composite mid. One rally does not convict the pass.

**How:** The markout of a buy is $\text{markout}_h = (S_{t+h} - P^{\text{fill}})\,n/100$, so

$$
(81.50 - 80)\times\frac{3{,}000{,}000}{100} = +\$45{,}000 ,
$$

and in §3.3.1's units, $1.5/80\times 10^4 = 187.5$ bp. Positive means the pass left money on the table. Now ask what you would want before calling it a mistake. First, strip the tide: if the market's own move explains, say, 1.0 of the 1.5 points *(illustrative)*, the IDO markout is $0.5\times 30{,}000 = \$15{,}000$, and the engine was mostly unlucky about beta (§3.3.3). Second, the counterfactual fill is the *winning* price, 80, not the engine's own lower bid, because the engine's bid lost the auction; and a thin bond's one-hour composite is partly a model, so net off the exit half-spread (a 0.50 half-spread would cut this to \$30{,}000, illustrative). Third, a pass is a decision about inventory and hedge cost, not a forecast, so grade passes as a class: a month of passes, logged with their reasons, against a month of fills, at the 1-, 5- and 20-day horizons of §3.3.1.

**The trap:** Two slips travel together. One is the sign: the chapter's worked example has the price *falling* after the pass ($-\$15{,}000$, so the pass was right), and copying that sign here says the pass "saved" \$45,000 when the price rose. The other is the verdict: treating $+\$45{,}000$ as proof that the engine is broken. One passed hand, with no beta strip and no sample of other passes, cannot tell you that. (If the client were buying *from* the engine, the engine would have sold at 80 and the same move would be $-\$45{,}000$ for the trade not done; read the direction of the RFQ before you sign the number.)

**If you got this wrong, read:** §3.3.1 (sign convention), §3.3.3 (IDO markouts) and §3.3.5 (only fills have markouts); the *Math, Gently* box in §1B.1.

**Z.1-B.2: A pair that keeps working**

**Answer:** $N \approx \$27.9$mm face of Halvorsen short (27.86 to two decimals), down from \$39mm at inception, which is about \$19.5mm of market value. Units: as in the Pair box, DTS here is face in \$mm $\times$ price/100 $\times$ spread duration $\times$ spread in bp, so 70,200 is in \$mm-bp. No probabilities are involved, so the measure question does not arise.

**How:** Per \$1mm of face, the short now carries $0.70\times 2.0\times 1{,}800 = 2{,}520$ of DTS. Set it equal to the long's 70,200:

$$
N\times 2{,}520 = 70{,}200 \quad\Rightarrow\quad N = 27.86 .
$$

The ruler has moved a long way since April, when \$1mm of face carried $0.90\times 3.4\times 600 = 1{,}836$. Keeping the April size would leave $39\times 2{,}520 = 98{,}280$ against 70,200, a short of 40% of a leg, the same orange line as Tuesday. One more thing worth seeing: nearly all of that shrinkage had happened by Tuesday. At 78, 1,400 bp and 2.3 the unit DTS is 2,512, so the matched size was already \$27.95mm; the further fall to 70 moves it by about \$0.1mm, because a lower price and a shorter spread duration almost cancel the wider spread. Dov trimmed to \$35mm and sold CDX HY protection to add back the rest ($35\times 2{,}512\approx 87{,}900$ against 70,200). Either way, matching DTS removes market beta only; the exchange-offer jump is still there.

**The trap:** Staying at the April face ratio of 0.65 (\$39mm), as though "matched in April" meant "matched". The second slip is arithmetic: dropping the price factor gives $70{,}200/(2.0\times 1{,}800) = 19.5$, which looks like an answer but is the short's *market value*, not its face. Divide by 0.70 to get the \$27.9mm of face you actually have to hold short.

**If you got this wrong, read:** §9.2.3 (DTS-neutral construction) and the *Math, Gently* box and Pair box in §1B.2; §8D.3 for the three rulers a pod can use.

**Z.1-B.3: The PM's option**

**Answer:** The PM's expected pay is \$0.5mm under A and \$2.0mm under B. The platform's expected P&L under B is $-\$2.0$mm without a stop and $+\$2.0$mm with a stop at a \$12mm loss. All figures are \$mm per year under the stated 50/50 odds (a physical-measure expectation, no discounting).

**How:** Pay is $0.2\max(\Pi, 0)$, so

$$
\mathbb{E}[\text{pay}_A] = 0.5\times 0.2\times 5 = 0.5, \qquad \mathbb{E}[\text{pay}_B] = 0.5\times 0.2\times 20 = 2.0 .
$$

The platform keeps 80% of a gain and all of a loss. Under B, $0.5\times 16 - 0.5\times 20 = -2.0$; because the gross expected P&L is zero, the platform's expected P&L is simply minus the PM's expected pay (under A that is $-0.5$). With the stop, the losing branch is cut at 12 and the winning branch is untouched: $0.5\times 16 - 0.5\times 12 = +2.0$. Notice what the sketch did: the gross expected P&L went from 0 to $+4$ because the stop clipped only losses and never a winner. That is the "provided" in the chapter's solution. A real stop also exits paths that would have recovered (the premium on the insurance), and a gap goes straight through it, which is why Dov worries about Halvorsen's jump more than its beta.

**The trap:** Paying 20% of *expected* P&L, which is $0.2\times 0 = 0$ for both strategies, and concluding that the PM is indifferent between A and B. Pay is $0.2\max(\Pi,0)$, a call, and a call's value rises with volatility: four times the size, four times the pay. The second slip is to read the stop's $+\$2.0$mm as a free lunch rather than as the output of an assumption about how the loss arrives.

**If you got this wrong, read:** the *Math, Gently* box in §1B.2 and §28.6 (the PM option and the two-threshold stop); §6-B.1 for the payoff-as-hockey-stick picture.

**Z.1-B.4: One bad print**

**Answer:** Before the correction, Monday is $-7.4\%$ and Tuesday is $+7.4\%$. After it, Monday is $-0.2\%$ and Tuesday is $-0.3\%$ (more precisely $-0.21\%$ and $-0.32\%$). Simple one-day returns on Friday's close of 95. For the back-test you need *both* pairs, in different jobs: the model's inputs are the as-known pair, because that is what it saw on Tuesday; its outcomes are measured on the corrected pair, because that is what the market did.

**How:** With $r_t = P_t/P_{t-1} - 1$:

$$
\frac{88}{95}-1 = -7.37\%,\quad \frac{94.50}{88}-1 = +7.39\%;\qquad \frac{94.80}{95}-1 = -0.21\%,\quad \frac{94.50}{94.80}-1 = -0.32\% .
$$

The two-day return is $94.50/95 - 1 = -0.53\%$ in both versions: the correction moves the *split*, not the total, so a buy-and-hold P&L would not care, but a daily volatility, a z-score, a reversal signal or a stop trigger would. The "before" pair is exactly the fake reversal a short-term reversal signal is built to buy. So ask which question you are answering. "What did we know when we decided?" takes the as-known version (the model really did see $-7.4\%$ on Tuesday and may have traded on it). "What did the market do?" takes the corrected one. An honest back-test decides on the first and books the P&L on the second; otherwise it either never makes the mistake production made, or it books a bounce from a price nobody could trade at. That needs the archive to keep both versions with the time each became known, which is the bitemporal read of Listing 1-B.1 (`as_known`, Appendix F).

**The trap:** Running the back-test on the corrected tape alone and concluding that on Tuesday the model ranked this bond on a mild decline. It did not; it ranked it on a 7% crash. The mirror error is to keep only the raw tape, so that the strategy that bought the 88 books a fake $+7.4\%$ the next day.

**If you got this wrong, read:** §27.2 (the provenance rule and the two timestamps, §27.2.2); §9B.2 and §9B.3 for cleaning TRACE and keeping two prices; the *Math, Gently* box in §1B.3 (the same cancel-and-replace with the chapter's 71 and 77).

**Z.1-B.5: Leaning inside the tolerance**

**Answer:** Up to \$300,000 of P&L can be moved without breaching a single tolerance. If the twelve errors are honest coin flips, the chance that all twelve fall on the favourable side is $0.5^{12} = 1/4096 \approx 0.024\%$ (about 0.02%); if you count "all twelve the same way, either way," it is $0.049\%$. Units: tolerance in points of price, P&L in dollars.

**How:** A tolerance of 0.75 points is 0.75% of face, and it is the same for every bond, so how the \$40mm splits across the twelve does not matter:

$$
0.75\times\frac{40{,}000{,}000}{100} = \$300{,}000 .
$$

(That is \$25,000 a bond on an average \$3.3mm.) Each mark passes its own test, so the breach report is silent. The signs are where the information is. If honest errors fall either side of the independent mid with equal odds, the number of favourable ones is Binomial$(12, \tfrac12)$: all twelve has probability $1/4096$, and even ten or more has $(66+12+1)/4096 = 79/4096 \approx 1.9\%$. "Favourable" means the long marks above the independent price and the short marks below it. The assumption doing the work is independence: a stale vendor that leans every price one way makes the pattern innocent, which is why the sign pattern is a screen that starts a conversation, not a verdict.

**The trap:** Reasoning bond by bond: "no mark breaches, so nothing is wrong." A tolerance is a budget for honest disagreement, and the budget can be spent one bond at a time. A numeric trap sits next to it: 0.75 is *points of price*, so forgetting the division by 100 gives \$30mm, a 100-fold overstatement.

NOTE (for the editor): §1B.4 and the Desk Debrief both say "a mark is a choice made inside the bid-ask spread," but the scene's composite is 77 bid, 78.50 offered, and Hal marks at 79. That is 0.50 above the offer and 1.25 above the 77.75 mid, so the mark is outside the spread, not inside it. The \$75,000 and the "about 70 bp of spread" (my check: 1.25 points on \$6mm is \$75,000, and \$75,000 / \$1,076 a bp is 69.7 bp) are right for a 79 mark; it is the sentence about the spread that fails. Either the composite's offer needs to be at least 79 or the senior trader's instruction needs to be at most 78.50.

**If you got this wrong, read:** §8C.4 (a tolerance is a policy, stated in dollars) and §8C.7 (the price test and the shadow explain); §8B.9 for the limit sheet; the *Math, Gently* box in §1B.4.

**Z.1-B.6: Kaz's small-boy letter**

**Answer:** Receiving the reply moves the probability that the name is in private talks from 5% to about 7.3% (posterior odds 0.079, likelihood ratio 1.5). It is a conditional probability on the stated frequencies, treating "restricted" and "in private talks" as the same event, as the chapter does.

**How:** Bayes in odds form: posterior odds are prior odds times the likelihood ratio,

$$
\frac{p}{1-p} = \frac{0.05}{0.95}\times\frac{0.9}{0.6} = 0.0526\times 1.5 = 0.0789, \qquad p = \frac{0.0789}{1.0789} = 7.3\% .
$$

The direct count agrees: $\dfrac{0.05\times 0.9}{0.05\times 0.9 + 0.95\times 0.6} = \dfrac{0.045}{0.615} = 7.3\%$. Set it beside the chapter's silence, which has a ratio of 8 ($50{:}950$ to $40{:}95$) and takes the same 5% to about 30%; a ratio of 1.5 is a nudge, not a leak. But it is still a leak: two such replies would multiply the odds by 2.25, and a reader who collects them over a hundred names learns the restricted list. The general counsel's boring sentence works only because its ratio is exactly one. There is no small-boy letter, because a letter whose use depends on the state of the world is a signal.

**The trap:** Reading the 90% as the answer, "there is a 90% chance they are restricted," which swaps $\mathbb{P}(\text{reply}\mid\text{restricted})$ for $\mathbb{P}(\text{restricted}\mid\text{reply})$. A milder slip is "5% times 1.5 is 7.5%": close, because the prior is small, but it multiplies a probability instead of the odds and will fail badly once the prior is large. And "it's the standard reply, so it tells you nothing" is true only when the two rates are equal.

**If you got this wrong, read:** §3.4.2 (the update in odds form) and §3.4.3 (the base-rate trap); §3.6.3 (the information wall is a feature); the *Math, Gently* box in §1B.5.

<!-- STATUS: COMPLETE -->
