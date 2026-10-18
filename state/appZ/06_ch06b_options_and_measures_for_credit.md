## Z.6-B Chapter 6-B: Options for Credit People: Replication, Black–Scholes, Greeks, Jump-to-Default and the Two Measures

Four exercises, in one numbered list at the end of the chapter. None carries a [Read]/[Derive]/[Build] tag, so none appears below. The chapter prints a check value for Exercises 2 and 3 (both verified) and nothing to check against for 1 and 4. I recomputed every number in Python, using Listing 6-B.1 from Appendix F for the pricing (its self-test passes). Two things are unusual. Exercise 1 is about Larkspur Foam, whose second-lien notes and face amounts appear nowhere in the book, so I built an illustrative stack and say so. Exercise 4 leans on the cold open's vega, which does not survive a recomputation (see the NOTE under Z.6-B.4). Measure tags throughout: prices, put floors and CDS-implied numbers are $\mathbb{Q}$; the agency default rate and anything you size are $\mathbb{P}$.

**Z.6-B.1: Payoffs, the ladder and the uptier rung**

**Answer:** Write $F_1$ for the first-lien face, $F_2$ for the second-lien notes and $M$ for the new super-priority face (not $N$, which the chapter keeps for the normal CDF). The attachment points are $a_1=0$, $a_2=F_1$, $a_3=F_1+F_2$, and the three claims are

$$
\underbrace{(V_T-0)^+-(V_T-F_1)^+}_{\text{first lien}},\qquad
\underbrace{(V_T-F_1)^+-(V_T-F_1-F_2)^+}_{\text{second-lien notes}},\qquad
\underbrace{(V_T-F_1-F_2)^+}_{\text{equity}},
$$

which sum to $V_T$. After the uptier the rungs are $[0,M]$, $[M,M+F_1]$, $[M+F_1,M+F_1+F_2]$, and equity is struck at $M+F_1+F_2$. The tranche whose delta rises most is the **old first lien**, the excluded lenders' claim. The Ad Hoc Group became the **new bottom rung**, the one whose lower strike is zero.

The book gives Larkspur no stack beyond the 84 mark, so the numbers below are mine (illustrative, \$mm): $F_1=1{,}000$, $F_2=400$, enterprise value $V_0=1{,}200$, asset volatility 22%, three years, $r=4\%$, which prices the first lien at 84.0. Insert $M=100$ and hold $V_0$ fixed, since the exercise inserts a rung and adds nothing to the firm. Deltas are $\partial(\text{tranche})/\partial V$:

| Tranche | Delta before | Delta after | Change |
| :-- | --: | --: | --: |
| First lien | 0.163 | 0.232 | **+0.069** |
| Second-lien notes | 0.297 | 0.300 | +0.003 |
| Equity | 0.540 | 0.468 | −0.072 |
| New super-priority | none | 0.000 | |

Values move the same way: first lien 839.6 to 811.5, second lien 196.0 to 167.0, equity 164.4 to 132.9. Together the old claims lose \$88.7mm, which is exactly what the new rung is worth.

**How:** The delta of a rung is a difference of call deltas, $\Delta_j=N(d_1(a_j))-N(d_1(a_{j+1}))$, with $N(d_1(0))=1$ because a call struck at zero is the firm. For the old first lien the lower strike moves from 0 to $M$, where the call is so deep in the money that $N(d_1(M))=1.000$, so nothing changes at the bottom. The upper strike moves from 1,000 to 1,100, and $N(d_1)$ there falls from 0.837 to 0.768. The first lien's delta is the difference of the two ends, 1.000 minus that number, so it rises from 0.163 to 0.232. The second lien moves both strikes, and the two changes nearly cancel. Equity only loses, because its strike goes up. The deltas still add to 1 before and after, so the 0.072 that equity gives up is what the debt rungs pick up. The new rung has zero delta and zero vega: lower strike zero, deep in the money, what §6-B.1.5 calls "all concavity, short volatility everywhere." That is what the Ad Hoc Group now owns. They did not get a better first lien; they got the most senior and least option-like rung on the page, and the excluded lenders slid one rung up the ladder toward the money.

**The trap:** Three tempting wrong answers, all confusing level with change. "The new tranche," because it is new: its delta is zero. "Equity," because it lost the most dollars: its delta fell. "The second lien," because it is the fulcrum with the highest delta: it barely moves. A subtler trap is to add the \$100mm to $V_0$ as new cash as well. Then the three changes are +0.010, −0.022 and +0.012, and equity edges the first lien, because you have changed two things at once. The exercise changes one; say which version you did.

**If you got this wrong, read:** §6-B.1.4 (the capital structure as a ladder of call spreads), §6-B.1.5 (Wolfspeed, where a document moves the strikes and the rungs are tagged for vega), and §13.3 (the uptier as a recovery transfer).

NOTE (for the editor): Exercise 1 asks for Larkspur's "second-lien notes," but Chapter 13 gives Larkspur only a 2029 first-lien term loan (marked 84), an Ad Hoc Group holding 51.3% of it, and no second lien, no face amounts and no enterprise value; the \$1.95bn and \$450mm are Serta's. A reader cannot check an answer against the book. I used \$1,000mm, \$400mm, \$1,200mm, 22% and three years, calibrated to the 84 mark. Suggest the exercise state a stack, and say whether the inserted tranche's face is also added to $V$ (new money) or not: with $V$ fixed the old first lien's delta rises most (+0.069), and with the face added to $V$ the three changes are +0.010, −0.022 and +0.012.

**Z.6-B.2: Measures, the 9% that was already risk-neutral**

**Answer:** The naive multiplier is **$\xi\approx2.31$**. The 9% is a $\mathbb{Q}$ probability and the 4% a $\mathbb{P}$ one (I take both as one-year; the ratio of hazards is the same for any common horizon), so the hazards are $\lambda^{\mathbb{Q}}=-\ln0.91=9.43\%$ and $\lambda^{\mathbb{P}}=-\ln0.96=4.08\%$ a year, and $0.96^{2.31}=0.910$ closes the check. The ratio of the probabilities, $9/4=2.25$, is close only because both are small; (6B.4) multiplies hazards, not probabilities. Neither number is a premium ratio. One sentence for ROBO: *`to_q` raised because the 9% is already a $\mathbb{Q}$ number, backed out of a spread at an assumed 40% recovery, and `to_q` converts only a $\mathbb{P}$ probability, so multiplying a premium onto it would charge the premium twice.*

**How:** Run the screen backwards. A 9% one-year probability at 40% recovery is a spread of $0.0943\times0.60=566$ bp. A spread identifies only the product $\lambda^{\mathbb{Q}}L^{\mathbb{Q}}$ (6B.5), and the premium ratio is $\text{PR}=\xi\,L^{\mathbb{Q}}/L^{\mathbb{P}}$, so three things stand between 2.31 and a premium. First, the recovery convention: 40% is a quoting convention, not a forecast. If the market's recovery were Halvorsen's 21 cents ($L^{\mathbb{Q}}=0.79$), the same 566 bp is a hazard of 7.2% and $\xi=1.75$. Second, $\lambda_D$: the agency rate counts distressed exchanges, and standard North American CDS generally does not (§14.1). Moody's June 2025 rate was 5.8% with them and 2.1% without; scale the bucket's 4% the same way (my assumption) and it is about 1.45%, and $\xi$ jumps to about 6.5. Third, liquidity: if 100 bp of the 566 is a liquidity premium (illustrative), the hazard falls to 7.8% and $\xi=1.90$. The three corrections do not share a sign, so you cannot net them in your head, and each is an assumption you must state.

**The trap:** Calling 2.25 "the hazard multiplier" and using it. The two common versions are converting another bucket's 3% agency rate as $3\%\times2.25$ (the right conversion is $1-0.97^{\,2.31}=6.8\%$) and running the 9% through `to_q` again. The ratio of probabilities drifts away from the ratio of hazards as the numbers grow: 50% against 20% is 2.5 on probabilities and 3.1 on hazards. The deeper trap is calling any $\mathbb{Q}$ over $\mathbb{P}$ quotient a premium before checking that the top and bottom count the same event with the same loss.

**If you got this wrong, read:** §6-B.6.3 (the hazard multiplier and (6B.4)), §6-B.6.4 (the three-part spread and the Bohn–Stein identification caveat), §6-B.6.6 (say which measure you are in), and §14.1 (two default rates, two recovery rates).

**Z.6-B.3: Corridors, how deep is deep enough?**

**Answer:** All in $\mathbb{Q}$, strikes in dollars on a \$6 stock, $r=4\%$, $\lambda=14.5\%$, $T=1$. By the (6B.2) bound, the largest strike whose corridor leak is under 1% of $U^{\text{Eur}}$ is **\$0.49 at 80% volatility** and **\$2.04 at 40%**. The exact leak, $\text{Put}_{\text{BS}}(6,B,1,\sigma,0.185)/B$, allows **\$0.75** and **\$2.72**. The bound is the safe answer to the question as asked; the exact figure is how far you can push if you compute the leak instead of bounding it. Both agree with the chapter's check.

**How:** First $U^{\text{Eur}}=e^{-0.04}\big(1-e^{-0.145}\big)=0.1297$, so 1% of it is 0.001297. (That is a 1.1% error in the hazard you read: 14.5% would come back as 14.66%.) The bound says $e^{-0.185}N(-\tilde d_2(B))\le0.001297$, so $N(-\tilde d_2)\le0.00156$ and $\tilde d_2(B)\ge2.9556$. Unwrap $\tilde d_2$ with its drift $r+\lambda-\tfrac12\sigma^2$:

$$
\ln\frac6B\;\ge\;2.9556\,\sigma+\tfrac12\sigma^2-0.185\quad\Longrightarrow\quad B\le6e^{-2.4995}=0.493\ (\sigma=0.8),\qquad B\le6e^{-1.0772}=2.043\ (\sigma=0.4).
$$

For the exact version, solve $\text{Put}_{\text{BS}}(6,B,1,\sigma,0.185)=0.001297\,B$ by bisection (`corridor_leak` in Listing 6-B.1): 0.746 and 2.724. The bound is looser because it drops the $-S\,N(-d_1)$ term; at \$0.49 the true leak is 0.19% of $U^{\text{Eur}}$. The leak depends on $\ln(S/B)/(\sigma\sqrt T)$, the strike's distance in standard deviations. A \$2 strike on the \$6 stock is 1.4 of them away at 80% and 2.7 at 40%, so halving $\sigma$ lifts the usable strike from 8% of spot to 34%. That is why low-vol names are the better instruments, and why nobody wants their puts: a stock that moves 40% a year rarely has a 14.5% hazard (the exercise holds $\lambda$ fixed to isolate $\sigma$). At $\lambda=1\%$ the default claim is 0.96 cents per dollar of strike, so a clean \$2 put carries two cents of default claim, about what you pay in spread to trade it. The volume sits in the distressed 80%-vol names, where the clean strikes are under \$0.75, below the \$1 put the desk trades. Halvorsen's \$1 put leaks 2.8% of $U^{\text{Eur}}$ (12% by the bound), the 3% behind the chapter's "97% default claim."

**The trap:** Dropping the drift term and setting $\ln(S/B)/(\sigma\sqrt T)=2.9556$ directly. That gives \$0.56 and \$1.84, too generous at 80% (the bound is \$0.49) and too stingy at 40% (\$2.04), because the $r+\lambda-\tfrac12\sigma^2$ term pushes in opposite directions at the two vols. The second trap is the one the exercise is built to catch: reading the put per dollar of strike as a pure default claim at any out-of-the-money strike, without checking the leak.

**If you got this wrong, read:** §6-B.5.4 (Corollary 1, the Carr–Wu corridor with an error term, and its worked example), the Full Derivation at the end of §6-B.5.5 (the proof of the bound), §6-B.8 Step 1 (the \$1 put on Halvorsen), and §23.3 (puts versus CDS, the American statement).

**Z.6-B.4: Kaz hedges the vega**

**Answer:** Mostly no. The calls hedge one line of the eleven, the diffusive vega, and 40 of the 41 hedges go where there is no vega to hedge, because the cold open's vega is essentially one bond and the other forty already net to about zero against the CDX. The calls do not hedge JTD; they make it worse, since a call is worth zero at default. They also add delta to a book that is already long the firms. On the day an uptier crushes the bonds while the stocks rally, the calls do pay, but how much is set by the deal's terms and not by vega: in my illustrative run they replaced between 4% and 64% of the bond's loss. Vega and call prices are $\mathbb{Q}$ objects; the JTD line and the uptier loss are what happens, not what is priced.

**How:** Take the double-B on the §6.2.4 firm ($V=100$, $F=80$, $\sigma_V=25\%$, one year). Its bond vega is $-V\phi(d_1(F))\sqrt T=-0.199$ per point of *asset* volatility. A call on the stock that expires with the debt, struck at the stock's forward (25.79), is a call on $V_T$ struck at $F+K_E=105.8$: one more rung of the §6-B.1.4 ladder, above the bond's own, with vega $+0.398$ and delta 0.52 (the bond's delta is 0.12). So 0.50 calls offset one bond, and they bring 0.26 of delta, 2.2 times the bond's own, for a premium of 4.6 on a bond worth 75.2. Units bite as well: the screen quotes the call's vega per point of *stock* volatility, and one asset-vol point is $\Omega=VN(d_1)/E=3.55$ of them here (the stock trades near 89%). Long bonds plus long calls is the firm twice, so every ordinary bad day loses on both legs. JTD is the part no call can touch. By §6-B.5.3 a call is $C_{\text{BS}}(r+\lambda)$ and is worth zero at default, so the line becomes $(R-P)\times\text{face}$ on the bond minus the calls' premium. On a distressed cousin of Exercise 1's stack (enterprise value \$900mm, $\sigma_V=30\%$, first lien at 71, \$10mm held, calls sized to its vega) that is −\$3.10mm on the bond at a 40 recovery and another −\$0.79mm on the calls, 25% worse. Only a put or a put spread pays.

Now an uptier on that stack: \$100mm of first-out money, and 51.3% of the first lien exchanged at 74 into second-out. The excluded rung moves from $[0,1000]$ up to $[480,967]$, and the equity strike falls from 1,400 to 1,367 because the haircut (133) exceeds the new money (100). The excluded loan goes from 71 to 58 (−\$1.29mm), the stock gains 6.6% and the calls gain \$0.05mm. If the new cash also stays in the firm, the loan loses 7 points (−\$0.70mm), the stock gains 54% and the calls gain \$0.45mm. The calls pay because the document moved the two strikes in opposite directions, which is a different sentence from "calls are long vega."

**The trap:** "Yes: bonds are short vega, calls are long vega, and the calls even help on the uptier day because the stock rallies." Every clause is true and the conclusion is wrong. Vega is one line of six. The calls are long delta (double exposure to $V$), they are worse on JTD, they buy volatility on forty names that did not need it, they are sized in the wrong volatility's units, and on a junior rung the bond's own vega flips sign (§6-B.1.4), at which point the calls double the exposure instead of cancelling it. The day they pay is the one day the book's two legs, which normally move together, come apart, and a hedge you can only collect on by luck of the terms is not a hedge.

**If you got this wrong, read:** §6-B.1.4 (the ladder, and why a rung is long volatility below its midpoint and short above it), §6-B.3.4 and §6-B.3.5 (Merton debt Greek by Greek, and the risk report line by line), §6-B.5.3 (one formula for calls and puts, and the SVB week), and §6-B.5.6 (one instrument, two risks).

NOTE (for the editor): The cold open multiplies $-0.199$ by 200,000 hundreds of face to get $-\$39{,}800$ and calls the figure "per 100 face." But $-0.199$ is the §6-B.3.4 table's figure for the §6.2.4 firm's debt, whose face is 80 (a bond worth 75.22). Per 100 face the vega is $-0.199\times100/80=-0.249$, which matches the table's own spread vega: 26.5 bp per vol point times a price of 94.03 per 100 face. Twenty million of face is then $-\$49{,}900$ per vol point, 122% of the −\$41k rather than 97%, and the other forty bonds and the CDX would net to about +\$8.9k, not −\$1.2k. Two repairs: size the double-B at about \$16mm of face ($0.249\times160{,}000=\$39{,}900$), or keep \$20mm and change the book total, the "ninety-seven percent" and the "minus twelve hundred dollars."


<!-- STATUS: COMPLETE -->
