# Ch 10 App Z editor-note log (numbers editor)

Three NOTE (for the editor) paragraphs in state/appZ/10_ch10_trend_and_time_series_momentum.md. All three deleted from the solutions file. Throwaway scripts in /tmp/ed10 (Listing 10.1-10.6 concatenated and run on the cached FRED BAMLH0A0HYM2 series; Figure 10.1 cache tools/figures/data/ch10_hy_hurdle.csv). No figure script needed a change: Figure 10.1's printed counts (534 days, 150 spread-rule short, 13 return-rule short) reproduce exactly.

## Note 1 (Z.10.4): p(1-p)beta^ce is a simple-regression slope, not the VAR coefficient

Note: in the VAR of 10.5.3 / Listing 10.6(a) the own lag is correlated with equity and acts as a suppressor, so the equity coefficient is p(1-p)beta/(1 - p^2 R2_ce), peaking near p = 0.66, not 1/2.

Recomputation: listing parameters beta_ce = 0.2, sd(eq) = 0.025, sd(e) = 0.003 give R2_ce = 0.735. Derivation: Cov(dm_{t+1}, dm_t) = 0 (G_t is nonzero only when no print at t), Cov(dm_t, r_t) = p beta Var(r), Var(dm_t) = Var(dP) so corr^2 = p^2 R2_ce; hence b_eq = p(1-p)beta/(1 - p^2 R2_ce). Formula vs 2,000,000-week simulation (VAR with own lag / simple regression): p = 0.2: 0.0330 vs 0.0333 / 0.0323; p = 0.5: 0.0613 vs 0.0611 / 0.0498 (simple formula 0.050); p = 0.66: 0.0660 vs 0.0658 / 0.0446; p = 0.9: 0.0445 vs 0.0444 / 0.0179 (simple formula 0.018). Grid peak of the VAR coefficient at p = 0.660. The note is right. The chapter's covariance derivation and the peak at p = 1/2 are correct for a simple regression; the chapter's sentence read as if it described the VAR just written down.

Ruling: FIXED (qualifier added, one sentence of scaling added; formula, peak, 0.075 and 0.027 examples unchanged).

Old -> new, 10.5.3 Math, Gently box:
- "The size of the fake lead turns out to be $p(1-p)\beta^{\text{ce}}$, where $p$ is" -> "The size of the fake lead, in a simple regression, turns out to be $p(1-p)\beta^{\text{ce}}$, where $p$ is"

Old -> new, 10.5.3 text after the covariance display:
- "Equity "leads" the bond mark with a coefficient of about $p(1-p)\beta^{\text{ce}}$ even though nothing leads anything." -> "Equity "leads" the bond mark with a simple-regression coefficient of about $p(1-p)\beta^{\text{ce}}$ even though nothing leads anything. (In the VAR above, the own lag is correlated with equity and rescales this by $1/(1-p^2R^2_{\text{ce}})$, where $R^2_{\text{ce}}$ is the share of the bond's true move that equity explains. The rescaling matters only when that share is large.)"

Solution Z.10.4 "How": appended after the covariance formula "That is the slope of a simple regression; in the VAR of §10.5.3 the own lag is correlated with equity and rescales it by $1/(1-p^2R^2_{\text{ce}})$, which matters only when equity explains most of the bond's true move." The note's claim that real bonds have low R2_ce is not in any repo source, so it was not put in the chapter.

## Note 2 (Z.10.5): coda says "about ten days", exercise check says "roughly eight trading days"

Recomputation: T/4 = 1.5/4 = 0.375 months = 0.375 x 21 = 7.9 trading days = 0.375 x 30.44 = 11.4 calendar days. "About ten days" matches neither unit; the exercise check (7.9 trading days) and Figure 10.4's "two-week lag breaks even at T = 2 months" (0.5 months) are consistent with the 21-day month. The note is right.

Ruling: FIXED.

Old -> new, 10.7 Coda, cut two:
- "any signal lagging by more than a quarter of that, about ten days, loses money" -> "any signal lagging by more than a quarter of that, about eight trading days, loses money"

Solution Z.10.5 already says "about 8 trading days, or 11 calendar days"; no edit beyond deleting the note.

## Note 3 (Z.10.5): fast sleeve "one session from flipping short" and slow sleeve "carry hurdle doing its job" vs the chapter's own tape

Note: Listing 10.6 on BAMLH0A0HYM2 (D = 4) shows the tanh crossover already short on 2 April and the 12-month return rule flipping short on 4 April, not held long by the hurdle.

Recomputation (Listing 10.6(d) code on the cached FRED series; sleeve signal = 0.5 x ensemble sign + 0.5 x tanh crossover):
- Tanh 20/120 crossover: -0.001 on 17 March, negative from 18 March, -0.736 on 2 April, -0.854 on 3 April, -0.938 on 4 April. Combined signal -0.618 on 2 April (62% of full risk), weight -1.33. A plain 20/120 simple-average gap also turns negative on 17 March (-7 bp of index, -108 bp by 2 April). Confirmed.
- 12-month return rule (Figure 10.1 definition, and the sign of the 252-day summed excess return): 12-month OAS change +59 bp on 3 April against a hurdle of 75.7 bp (return-based hurdle 73.7 bp), sum of 12-month returns +58.7 bp, so long; +106 bp on 4 April, sum -129 bp, so short. The 13 short days in Figure 10.1 are 4, 7-11, 14-17, 21, 22 and 30 April 2025, and no other days in the 534. Short from the 4 April close at 4.45% it was long again at the 23 April close (3.75%); the sign rule at unit notional lost about 3.0% from 4 to 22 April on the V's recovery. Confirmed.

Ruling, two parts.
(a) Fast sleeve "one session from flipping short": NOTE WRONG as an edit request, nothing changed. The sentence reports "the desk's fictional run" on a CDX HY sleeve, a labelled invented model output; Listing 10.6 runs a different construction (EWMA tanh, blended with a sign ensemble) on the cash-index OAS, and the chapter nowhere says the listing reproduces the coda's sleeve. Changing it would rewrite story beats (Theo's "let the fast sleeve flip", Kaz's "full risk on the flip", cut two's "flipped short into it, near the wides"). The tape fact is recorded here for the next reader: on the cash index a 20/120 crossover was short from mid-March.
(b) Slow sleeve "the carry hurdle doing its job in a week when nothing else did": FIXED. This is a claim about the real mechanism on the real tape, and the chapter's own Figure 10.1 (13 short days, all in April 2025) shows the 12-month return rule flipped short one session after Theo's card and was whipsawed. Theo's statement on the 3 April close stays true (59 bp against about 75), so the grade keeps its beat ("best line on the card") and loses only the overclaim.

Old -> new, 10.7 Coda, "Grading the cards":
- "because it was the carry hurdle doing its job in a week when nothing else did. The reader's card" -> "because it was the carry hurdle doing its job, for one session: at the next close the twelve-month rule cleared the hurdle (106 bp of widening against about 75, up from 59) and was whipsawed, which is the 13 short days of Figure 10.1, all in April 2025. The reader's card"

Solution Z.10.5 quotes neither the fast-sleeve nor the slow-sleeve line, so only the NOTE was deleted. Its numbers (-1.33 to -0.53 weight, 0.88% / 0.66% / 1.7%) were not touched and were not re-audited here.

## Summary
Notes handled: 3. Fixed: 3 (note 1 in full, note 2 in full, note 3 slow-sleeve part). Ruled wrong in part: 1 (note 3 fast-sleeve part, fictional CDX run, left as written).
<!-- STATUS: COMPLETE -->
