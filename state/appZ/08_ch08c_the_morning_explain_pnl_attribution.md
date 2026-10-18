## Z.8-C Chapter 8-C: The Morning Explain: P&L Attribution That Foots, From One Bond to the Book to the Signal

Eight exercises: the seven numbered Exercises 8C.1 to 8C.7 at the end of the chapter, plus one try-first prompt inside §8C.6, Morning (c), which comes first in the chapter's own order and so is Z.8-C.1 (Z.8-C.2 to Z.8-C.8 are Exercises 8C.1 to 8C.7, in order). None carries a [Read], [Derive] or [Build] tag and none asks for code, but Listing 8-C.1 (`pnl_explain.py`, Appendix F) has a function behind each of Z.8-C.2 to Z.8-C.7, and Listing 8-D.1's `capture` sits behind Z.8-C.8. I did not copy the printed checks: I reran every number in Python, including the listing, whose own asserts all pass. The checks are right in substance. The six NOTEs below are about one sign in the chapter's wording, one multiple, a lien description, two cross-references and one rule the companion listing does not implement. Everything here is realized (physical-measure) P&L bookkeeping on illustrative numbers, so no risk-neutral quantity appears. Money is in dollars, prices are per 100 face, and yields and spreads are in basis points unless I say otherwise.

**Z.8-C.1: PB-01's Tuesday in four numbers**

**Answer:** Idio $+\$132{,}900$; leak $-\$61{,}600$; friction $-\$26{,}860$; net $+\$44{,}440$; capture ratio $44{,}440/132{,}900 = 0.33$. The market line is priced on the hedge ratio the pair held *when the day began* (the 7:15 x-ray: 70,200 of long DTS against 98,000 of short DTS), not on the 4:00 ratio. The \$140,000 roll break goes nowhere in PB-01's explain: it stays on the book's page as a named line with a ticket.

**How:** Spreads closed 2% tighter, and at \$1 per unit of DTS per 1% move the market line on the open's positions is

$$
70{,}200 \times 2 - 98{,}000 \times 2 = +140{,}400 - 196{,}000 = -55{,}600 .
$$

Add the rates residue, about \$12,000 of net-long DV01 against Treasuries half a basis point higher, $-12{,}000 \times 0.5 = -\$6{,}000$, and the leak is $-\$61{,}600$. Idio is the issuers' own news: Kestrel $+\$62{,}900$ and Halvorsen $+\$70{,}000$ on the short, $+\$132{,}900$. Friction adds the custodian's and prime broker's facts and the model's pull, then the two trades:

$$
10{,}000 - 7{,}850 + 1{,}170 - 5{,}970 - 2{,}540 - 1{,}670 - 16{,}000 - 4{,}000 = -26{,}860 .
$$

The \$16,000 is the cover's day-one line, $(78.35 - 78.75) \times 4{,}000{,}000/100$, and the \$4,000 is the half-spread on the index sale. Net is $132{,}900 - 61{,}600 - 26{,}860 = 44{,}440$. The ratio is the open's because the 7:15 hedge is the one the morning's rally actually met; a trim at 2:40 cannot reach back and hedge ten o'clock. Realizing Dov's gain on the cover is a reclassification, not P&L. The roll break is the OMS and the FCM disagreeing about a date, which is an operations ticket and not a cost of holding Kestrel against Halvorsen. What PB-01 does own, from 2:40, is its slice of the index: that sale's factor line, its coupon and, each March and September, its series-roll line.

**The trap:** Using the 4:00 ratio, which is what the platform's default report does. The pair is flat at the close, so the market line is zero and the morning's $-\$55{,}600$ has nowhere to go but idio: idio $+\$77{,}300$, leak $-\$6{,}000$, net still $+\$44{,}440$, capture $0.57$. The arithmetic is fine and the lessons are wrong (the view looks smaller than it was, and the ruler looks fine). The default report also spreads the book's CDX lines, roll break included, across pairs in proportion to their DTS gaps, which would change the net as well.

**If you got this wrong, read:** §8D.6 ("The Ledger"), where the capture ratio is defined and the betas are fixed at the start of each day; §8C.3 for the day-one line; and the scene itself, §8C.6, "Morning (c): the pair, at Vantress".

**Z.8-C.2: Accrual versus pull**

**Answer:** Per 100 face on an ordinary weekday: accrual $0.0201$ points (2.0 bp of par); pull-to-par $0.0069$ points (0.7 bp) on a straight line, or $0.0060$ points (0.6 bp) at a constant yield of 10.24%. On a Monday all three triple: $0.0604$, $0.0208$ and $0.0179$ points.

**How:** Accrual is the contract: the coupon is 30/360, so one day earns $7.25/360 = 0.020139$ points, and the custodian can confirm it to the cent. Pull-to-par is a forecast and comes in two flavours. Straight-line, the eight points to par spread over 3.2 years are $8/3.2 = 2.5$ points a year, and $2.5/360 = 0.006944$ a day. At a constant yield, solve the semiannual yield on a clean 92 with 3.2 years left (0.6 of a coupon period has elapsed, so a dirty 94.175 sits behind the quote): $y = 10.24\%$. Reprice one day later at that yield and the clean price is $92.00598$, so the pull is $0.00598$. The chapter's first-order formula agrees: $\theta = yP - 100c = 0.1024 \times 92 - 7.25 = 2.168$ points a year, which is $0.00602$ a day. Accrual plus pull is $0.0261 \approx yP/360$, the "carry earns the yield" statement of §8.1. The two pull numbers differ by $0.09$ bp, and that gap is a choice of model. On a Monday, Saturday and Sunday accrue and time passes, so all three are multiplied by three (30/360 weekends that straddle a month-end are the custodian's file to settle).

**The trap:** One carry line, about $0.026$ points (yield times price over 360). It is right as a sum and useless as a control, because a missed coupon would vanish into the model's half. The runner-up is accruing on 365: $7.25/365 = 0.01986$ is not what the indenture pays.

NOTE (for the editor): §8C.1 says Chapter 4-B gives the constant-yield $\theta_i = y_i P_i - 100\,c_i$ and the roll-down term. I cannot find either in §4B; the nearest text is §8.1, "The thirty-seven cents, itemized" (pull is $y\,\Delta t - c\,\Delta t/P$), so the pointer probably wants to be §8.1. Separately, the formula is first-order: for this exercise's bond it is within 1% of the exact drift ($0.00593$ at 10.2%, against $0.00598$ exact), but in the Math, Gently box a bond exactly five years out on a coupon date drifts \$494 a day on \$10mm at a constant 9.04%, against the box's \$530 (the formula at the box's rounded 9.0% gives \$533). The \$530 is right for a bond about 4.87 years out. A clause saying where in the coupon cycle the box's bond sits would settle it.

**If you got this wrong, read:** §8.1, "The thirty-seven cents, itemized" (the carry row split into accrual and pull); §4B.1, "Clean, dirty, accrued"; and the first Math, Gently box of §8C.1.

**Z.8-C.3: The phantom**

**Answer:** The book reports $+\$20{,}000$ today. Nothing was earned and nothing was traded. It reverses tomorrow, when the futures' next settlement catches up with the 4 bp rally and books $-\$20{,}000$ on a day the bond had no matching move. On a shared 3 p.m. snap it is zero.

**How:** The bond is marked at $t_2$ (4:00) and the futures at $t_1$ (3:00), so only the yield move between the two photographs matters:

$$
\Pi^{\text{phantom}} = -\text{DV01}_B\,\big(\Delta y_{t_2} - \Delta y_{t_1}\big) = -5{,}000 \times (-4 - 0) = +\$20{,}000 .
$$

The rally after 3:00 is in the bond's 4:00 mark (a \$20,000 gain on the long) and not yet in the hedge's 3:00 settlement (the matching \$20,000 loss on the short futures). The exchange's variation margin is exactly right; it is the report that mixes two clocks. Tomorrow's settlement carries the whole move, while the bond's 4:00-to-4:00 change does not, so the books show $-\$20{,}000$ with no market behind it, and the pair nets to zero over the two days. For scale, the chapter's one-sigma hour is about 2.4 bp of yield, so this book's typical phantom is $5{,}000 \times 2.4 \approx \$12{,}000$ and 4 bp is a 1.7-sigma hour. The fix is a shared snap, or a timing line computed from the hedge's intraday price at the snap time so it never sits in the residual. Listing 8-C.1's `phantom(5_000, 0.0, -4.0)` returns 20,000.

**The trap:** "Zero, because it's hedged DV01-for-DV01." The hedge is neutral to a yield move at one time, not to two photographs an hour apart. The sign slip is the other common wrong answer: $-\$20{,}000$ is the hedge's loss alone, and that loss is precisely what the report has not booked yet.

**If you got this wrong, read:** §8C.3, the "timing" paragraph at the end; §3B.1, "The Day as a Timeline" (the phantom's two Math, Gently boxes); and §8B.3 for the shared 3 p.m. snap.

**Z.8-C.4: The cross-term**

**Answer:** The interaction is $2.6 - 1.2 - 0.8 = +0.6$ (all in \$mm). Sequential with A first gives A 1.2 and B 1.4; with B first, B 0.8 and A 1.8. Equal split and Shapley agree for two signals: A 1.5, B 1.1. "B last" hands B 1.4 instead of 1.1.

**How:** The characteristic function is $v(\varnothing) = 0$, $v(A) = 1.2$, $v(B) = 0.8$, $v(AB) = 2.6$, each value the P&L of a book the optimizer would have built from that set. The interaction is $v(AB) - v(A) - v(B) = +0.6$; here netting saved costs, so the pair beats the sum of its parts. Sequential gives the first signal its standalone value and the second its increment. Equal split is standalone plus half the interaction: $1.2 + 0.3$ and $0.8 + 0.3$. Shapley averages the two orders,

$$
\phi_A = \tfrac12\,(1.2 + 1.8) = 1.5, \qquad \phi_B = \tfrac12\,(0.8 + 1.4) = 1.1,
$$

and with two players that is always the equal split of the surplus. Every convention sums to 2.6. With a positive interaction the signal listed last collects all of it, so B-last pays B 0.3 more than Shapley and A 0.3 less (B up by 27%); "alphabetical" is the beneficiary's rationale. With a negative interaction, as in September's \$2.4mm book, the same trick makes the last signal absorb the loss. Listing 8-C.1's `sequential` and `shapley` reproduce all four numbers.

**The trap:** Reading the standalone numbers as the attribution and wondering where 0.6 went (they add to 2.0, not 2.6), or defending the sequential split because "B added 1.4 on top of A". The order is a free parameter that moves 0.6 of P&L between two authors, and that is why the report header names the convention before the month starts.

NOTE (for the editor): §8C.5 says equal split gives each signal "its standalone value *minus* half the interaction: momentum $3.0 - 1.3 = 1.7$", but the interaction is defined one line earlier as $2.4 - 3.0 - 2.0 = -2.6$, so the rule as written gives $3.0 + 1.3 = 4.3$ and $2.0 + 1.3 = 3.3$ (summing to 7.6, not 2.4). The 1.7 and 0.7 are right (and equal Shapley); the wording should say "plus half the signed interaction" or "minus half the overlap of 2.6". This exercise's check, 1.5 and 1.1, uses the "plus" form.

**If you got this wrong, read:** §8C.5, "Which Signal Made the Money?", from the second Math, Gently box on.

**Z.8-C.5: Halvorsen's effective date**

**Answer:** The desk receives \$2.8mm face of takeback notes and new equity with \$3.28mm of plan value. The corporate-action line is zero. The market line is $-\$496{,}000$: the package marks at \$5.504mm (55.04 per 100 of old face) against \$6.0mm carried. The old notes' accrual line is zero, because they have traded flat since the petition, and the takeback notes start accruing from the effective date.

**How:** §12B.9's plan gives each \$1,250 of first-lien claims \$350 of takeback notes and \$410 of new equity at plan value ($760/1{,}250 = 60.8\%$). The desk's \$10mm is $10{,}000/1{,}250 = 8$ units, so

$$
8 \times 350 = 2{,}800, \qquad 8 \times 410 = 3{,}280 \quad (\$\text{thousand}).
$$

The exchange is booked at carrying value, $10 \times 0.600 = \$6.0$mm, with zero P&L. Allocate that across the two new instruments however the books specify (pro rata to plan value gives \$2.763mm and \$3.237mm; Listing 8-C.1's `corporate_action` returns a zero line and refuses allocations that do not sum to the carrying value). The first marks then give

$$
2.8 \times 0.97 + 3.28 \times 0.85 - 6.0 = 2.716 + 2.788 - 6.0 = -0.496 \quad (\$\text{mm}).
$$

The allocation only decides how the \$496,000 splits across the two lines ($-\$47{,}000$ and $-\$449{,}000$ on the plan-value split); the total is the same. It is a real market loss against the last mark of 60.0, not an accounting artefact. On a \$100mm NAV it is about 50 bp, so it needs to carry its name, because left in the residual it would be fifty times the \$10,000 tolerance.

**The trap:** Reading the swap as a sale of the old notes and a purchase of the new ones at different marks. Sold at the plan's 60.8 it shows a fake gain of \$80,000 on one line and a fake loss of \$576,000 on the other (the \$6.08mm plan value against the \$5.504mm first mark), and the two net to the same \$496,000 while telling two stories nobody traded. The mirror error is to file the \$496,000 as a corporate-action break; the exchange itself is zero, and the loss belongs on the market line.

NOTE (for the editor): this exercise calls the 7.25% 2029s "secured notes", which matches §12B.9 (senior secured, pari passu with the term loan B, and the arithmetic needs them in the first-lien class). §8C.6, Morning (c), and §1B call the same notes "senior unsecured", and the pod's short in PB-01 is that bond. One of the two descriptions has to change, and the choice decides whether PB-01's short sits in the first-lien class that ends up with the takeback notes.

NOTE (for the editor): §8C.8 (and the "Builds on" line) says "Appendix B §B.16 lists the evidence to keep for each [corporate] action". §B.16 is "Specification for AI Implementation: The Tidy Bond Panel", and Appendix B does not mention corporate actions or exchange offers at all. The pointer needs a new target, or the evidence list needs writing.

**If you got this wrong, read:** §8C.8, the "Corporate actions" paragraph (the swap at carrying value); §12B.9 for the plan's consideration; and §16.6 (Hertz) for the same swap on a real effective date.

**Z.8-C.6: Tolerance at scale**

**Answer:** A 6 bp mark tolerance on \$45mm of CS01 permits $45 \times 6 = \$270$mm of P&L discretion on that one line. This desk's policy on a book with \$20bn of NAV and a 1-day ES of \$400mm allows $\min(\$2\text{mm},\ \$20\text{mm}) = \$2$mm of unexplained for the *whole book*, 135 times less than the one CIO line, and 0.5% of the book's ES where the line's \$270mm is two-thirds of it.

**How:** The CS01 comes from the case: \$100bn of five-year index notional times a risky duration of 4.5 times one basis point is $100 \times 10^{9} \times 4.5 \times 10^{-4} = \$45$mm per bp. A tolerance in spread points converts to dollars by multiplying through the CS01: $\$45\text{mm} \times 6 = \$270$mm. The desk's rule is dollar-denominated and size-aware:

$$
\text{tol} = \min\big(1\ \text{bp of NAV},\ 5\%\ \text{of ES}_{1d}\big) = \min\big(10^{-4} \times 20\text{bn},\ 0.05 \times 400\text{mm}\big) = \min(2\text{mm},\ 20\text{mm}) .
$$

The NAV term binds. Neither term depends on how much notional the book holds in a name, so growing a position never grows the allowance, whereas a per-instrument tolerance in basis points grows with the position, fastest exactly when the position is becoming impossible to exit. For scale, \$270mm is 1.35% of \$20bn of NAV, against the policy's 1 bp. Listing 8-C.1's `tolerance(20e9, 400e6)` returns 2,000,000.

**The trap:** Forgetting that a basis-point tolerance needs a CS01 under it. $6\ \text{bp} \times \$100\text{bn}$ of notional is \$60mm, short by the 4.5 of risky duration. The second slip is the opposite unit error, \$45mm $\times\, 6 \times 10^{-4} = \$27{,}000$, which treats the CS01 as if it were still per unit of spread. For the policy half, taking the larger term (\$20mm) misses why there are two: the rule is a minimum, so the smaller one binds.

NOTE (for the editor): §8C.6(b) says the Corriveau true-up of $-\$240{,}000$ is "24 bp of NAV, two and a half times the day's tolerance". With the §8C.4 policy on \$100mm of NAV and \$1.5mm of ES the tolerance is \$10,000, so $240{,}000/10{,}000 = 24$ times (and 3.2 times even the 5%-of-ES term of \$75,000). "Two and a half" matches neither; "twenty-four times" is what the chapter's own policy gives.

**If you got this wrong, read:** §8C.4, "The Foot" (the tolerance and the expected-shortfall Math, Gently box); §8C.7, the second of the four ideas; and §8B.6 for the ES on the mixture.

**Z.8-C.7: ROBO, again**

**Answer:** The first guard in `foot`, the `PLUG_NAMES` check (`market` is in the set), raises a `ValueError` before any arithmetic, so the report is refused. A cleverer ROBO that calls the line *liquidity premium* with source `risk_model` passes both guards, because the name is not on the list and the source is on `SOURCES`. Only `suspicious_zero` catches it: $U$ comes back as zero (to rounding), `breach` is `False` and `suspicious_zero` is `True`. That is a flag in the returned dictionary, not an exception, so someone has to read it.

**How:** I ran Listing 8-C.1 on Monday's twelve lines plus a plug equal to the residual. Named `market`, with source `market` or `risk_model`, `foot` refuses it. Named `liquidity premium`, source `risk_model`, it returns `{'U': 0, 'tol': 10000.0, 'breach': False, 'suspicious_zero': True}`. Forty per-bond plugs that sum to the residual give $U \approx 2 \times 10^{-10}$ and the same flag, because `suspicious_zero` is $|U| < 0.005$. The lesson is in what each guard really tests. The name list catches only a lazy ROBO. The source field is a label that ROBO can type. The zero flag catches a perfect plug and nothing smarter: a plug sized to leave \$37 gives $U = 37$ and `suspicious_zero: False`. So the real defense is structural, as the chapter says. A line computed from the mark it explains is a plug whatever it is called, so line values are built only from sensitivities times moves, or from facts (custodian, clearing, blotter), and the code that builds them never sees the official marks. The foot is then an identity with a meaningful $U$.

**The trap:** "Renaming it gets past the check." It does get past the first guard, but the foot's second tripwire fires. The costlier mistake is the next one, believing the two tripwires are the defense. They are alarms for the sloppy plug. Two checks are cheap to add (recompute every line from raw inputs through an independent path; refuse any line that equals minus a position's residual to the cent), but the answer remains a design rule, not a filter.

**If you got this wrong, read:** §8C.10, "What ROBO built from the vague versions" and "Why it is built this way"; §8C.4 (the foot is a definition, not a model); and §8C.1, the paragraph that begins "Each line of a production explain answers one counterfactual question".

**Z.8-C.8: The morning's ratio**

**Answer:** On the start-of-day ratio the market line (the leak) is $-\$45{,}000$, net is $40{,}000 - 45{,}000 - 12{,}000 = -\$17{,}000$, and the capture ratio is $-17{,}000/40{,}000 = -0.43$ (exactly $-0.425$). On the 4:00 ratio the pair is flat, the leak is zero, idio becomes $-\$5{,}000$, net is still $-\$17{,}000$, and the "capture ratio" is $-17{,}000/-5{,}000 = +3.4$, which means nothing. The second report tells the PM the view lost money and the hedge was perfect. Both statements are wrong.

**How:** At the open the pair is long 50,000 and short 65,000 of DTS, a net $-15{,}000$. Spreads tighten 3% before noon, and at \$1 per unit of DTS per 1% move the long gains $50{,}000 \times 3 = \$150{,}000$ and the short loses $65{,}000 \times 3 = \$195{,}000$:

$$
(50{,}000 - 65{,}000) \times 3 = -\$45{,}000 .
$$

The 1:00 trim is after the move, so it cannot undo any of this. Net is idio plus leak plus friction, $40{,}000 - 45{,}000 - 12{,}000 = -17{,}000$, and a net that is negative on a positive idio line gives $\kappa = -0.43$: the view paid and the ruler lost more. Price the same day on the 4:00 ratio, 50,000 against 50,000, and the market line is zero, so the \$45,000 has nowhere to go but idio: $40{,}000 - 45{,}000 = -\$5{,}000$. Net is unchanged (the same lines, regrouped), so $\kappa = -17{,}000/-5{,}000 = 3.4$. A ratio above 1 reads as "kept 340% of the view" when in truth the view made \$40,000. The ledger therefore prints the lines and leaves the ratio blank whenever idio is not positive.

**The trap:** Pricing the market line on the close, and then trusting the ratio. The 4:00 report prices a hedge that did not exist at 10 a.m., so it tells the PM to cut a thesis that paid \$40,000 and to leave a ruler that was 15,000 DTS out of balance for the whole morning, which is the §8C.6 lesson in miniature. The second slip is celebrating a ratio of 3.4.

NOTE (for the editor): the printed check says "when the idio line is negative, the ledger prints the lines and leaves the ratio blank". I cannot find that rule anywhere else in §8C or §8D.6, and the companion listing does not implement it: Listing 8-D.1's `capture(idio, leak, friction)` is `(idio + leak + friction) / idio` with no guard, so this exercise's 4:00 case returns 3.4 and an idio of exactly zero raises `ZeroDivisionError`. Either state the rule in §8D.6 and add the guard (`None` when `idio <= 0`), or drop the sentence from the check.

**If you got this wrong, read:** §8C.6, "Morning (c): the pair, at Vantress", from "The default report's numbers were not bad arithmetic" on; and §8D.6, "The Ledger" (the capture ratio and the start-of-day betas).

<!-- STATUS: COMPLETE -->
