## Chapter 26: AI Agents & LLMs on the Credit Desk

Six exercises: two on prices (the abstention bar and the scoring rule), two on probability (retries and pass$^k$), one on the calendar, and one on a document that lies about itself. Every number below was recomputed in Python from the chapter's inputs and from Listings 26.1 to 26.3 (Appendix F). Write your card before you read ours.

**Z.26.1: The price of a check**

**Answer:** $p^\ast = 1 - 250/150{,}000 = 1 - 1/600 \approx 0.9983$. At that bar the reader answers 31% and sends 69% to people, but the queue holds only 40%. So the **human queue binds**, and it is short by 29% of volume. Pay for the shortfall, don't move the bar to hide it. Buy the checks (29 more per 100 questions at \$250, or \$7,250 per 100 questions), work the queue in order of expected loss so that whatever is left over is the cheapest to leave, price $C_{\text{FP}}$ position by position (not every basket question carries a \$150,000 mistake), or defer what can wait. Lowering the threshold until coverage reaches 60% is the costliest of these options. Every claim it lets through below 0.9983 costs more in expectation than the \$250 check it replaces: at $p = 0.99$ the expected loss is \$1,500, the price of six checks.

**How:** Answering beats checking when $(1-p)\,C_{\text{FP}} < C_{\text{abs}}$, so the bar sits where the cost ratio puts it, here 600 to 1:

$$
p^\ast = 1 - \frac{C_{\text{abs}}}{C_{\text{FP}}} = 1 - \frac{250}{150{,}000} = 0.99833 .
$$

The queue needs $1 - \phi \le 0.40$, i.e. coverage $\phi \ge 0.60$, and the reader gives 0.31. The reader's coverage is a fact about the reader. The queue's 40% is the constraint, and it binds. For any claim with $p < p^\ast$, answering it unchecked costs $(1-p)C_{\text{FP}} - C_{\text{abs}} > 0$ in expectation, by the definition of $p^\ast$. A lower threshold therefore always loses money compared with buying the check, and the only open question is who pays. The \$250 is desk opex: it shows up in the analyst budget every month. The \$150,000 is an expected loss on the book: it belongs to the PM, and through the PM to the investors, and nobody sees it until it lands. Lowering the threshold moves cost from the visible line to the invisible one. So the person who owns the invisible line (the PM, with risk signing) has to sign the change, and it goes in the model inventory with the cost assumptions written down (§26.5's third point). When the queue still binds, the honest product is an order in which to read: check claims in descending order of $(1-p)\,C_{\text{FP}}$. (A sanity flag: under §26.12's toy reader, a bar of 0.9983 sits 5.5 standard deviations above the mean difficulty and coverage would be essentially zero. A 31% coverage already assumes the deterministic checks are carrying a lot of the load.)

**The trap:** "The reader binds, it only answers 31%, so lower the threshold until it answers 60%." That treats $p^\ast$ as a tuning knob when it is a price. Moving it quietly declares that a wrong basket costs less than \$150,000, without asking the person who pays for it. Smaller slips: inverting the ratio ($250/150{,}000 = 0.0017$, "answer everything"), and reusing the chapter's 0.95, which belongs to a 20-to-1 cost ratio. This one is 600 to 1.

**If you got this wrong, read:** §26.5, the cost version of Kalai's rule and the "three things go wrong" paragraph; then §26.3 at 11:40, where the bar is 99.5%, the queue binds and Theo's card turns the list into a reading order; and $J(\vartheta, \phi)$ in §26.6, "The bill and the frontier".

**Z.26.2: Lazarus, audited**

**Answer:** At $m = 2$ (two attempts, which means one retry), $\Pr(\text{right}\mid\text{accepted}) = 0.9526$ and coverage is $0.9439$, which matches the chapter's 0.953 and 0.944. For the whole path: $m = 1$ gives 0.9614 and 0.830, $m = 3$ gives 0.9479 and 0.9745, and $m \to \infty$ gives 0.9432 and 1. A Monte Carlo run of 2 million paths gives 0.9526 and 0.9436. With a single question type the posterior is $a_R/(a_R + a_W)$ for every $m$ (0.977 at $p = 0.9$). Retries still are not free: in the mixture, the answers that come back on the second try are right only 88.8% of the time, against 96.1% on the first.

**How:** Per attempt, $a_R = p(1-f)$, $a_W = (1-p)(1-d)$ and $r = 1 - a_R - a_W$. Easy questions have $(0.9025,\ 0.010,\ 0.0875)$ and hard ones $(0.38,\ 0.12,\ 0.50)$. A type is accepted within $m$ attempts with probability $1 - r^m$. Because $1 - r = a_R + a_W$, the geometric series cancels, and type $j$'s posterior is $\pi_j = a_{R,j}/(a_{R,j} + a_{W,j})$ (0.989 for easy, 0.760 for hard), with no $m$ in it. That is the single-type result. The mixture is a weighted average with weights that do depend on $m$:

$$
\Pr(\text{right}\mid\text{acc}) = \frac{\sum_j w_j\,\pi_j\,(1 - r_j^m)}{\sum_j w_j\,(1 - r_j^m)}, \qquad \text{coverage} = \sum_j w_j\,(1 - r_j^m).
$$

At $m = 2$ the easy questions contribute $0.8(1 - 0.0875^2) = 0.7939$ and the hard ones $0.2(1 - 0.5^2) = 0.15$. So coverage is 0.9439 and precision is $(0.7939 \times 0.989 + 0.15 \times 0.76)/0.9439 = 0.9526$. The point for Kaz is that $m$ moves the weights toward the type with the high $r$, which is the hard type with the low $\pi$. Hard questions go from 12.0% of accepted answers to 15.9%, and the 11.4 points of extra coverage arrive at 88.8% precision. The option is exercised by the questions you get wrong. Even in the one-type case the retries cost tokens and latency. And the i.i.d. assumption flatters them: a second draw from the same model is correlated with the first, so the answer that finally gets past a same-family verifier is selected for that verifier's blind spot. That is Ines's rebuy.

**The trap:** Two numerical ones. If you weight the per-type posteriors by the prior shares, $0.8 \times 0.989 + 0.2 \times 0.76 = 0.943$, you have computed the $m \to \infty$ limit, whatever $m$ you meant, because only infinite retries accept every question. If you read $m$ as a count of retries rather than attempts, so that $m = 2$ means three attempts, you get the chapter's $m = 3$ row (0.948, 0.974). The conceptual trap is Kaz's: "the posterior doesn't depend on $m$, so retries are free". That holds for one question type, and a desk never has one.

**If you got this wrong, read:** §26.6, "Verifiers, retries and the Lazarus rate" and its Full Derivation; the *A checker, in odds* box for the one-type posterior; and `verified_closed_form` and `simulate_verified` in Listing 26.3 (Appendix F), which this exercise reruns at $m = 2$.

**Z.26.3: ROBO, scored**

**Answer:** Score a right answer $+1$, an abstention $0$ and a wrong answer $-w$, with $w = (C_{\text{FP}} - C_{\text{abs}})/C_{\text{abs}}$. Answering is then worth $p - (1-p)w$, which is positive if and only if $p > w/(1+w) = 1 - C_{\text{abs}}/C_{\text{FP}} = p^\ast$. That is Kalai et al.'s rule with $t = p^\ast$. On the §26.12 reader at 20 to 1 ($w = 19$): answer-everything scores $-3.61$ per question, abstain-everything scores 0, and the honest reader scores $+0.012$ (it answers 4.3% of questions and gets 3.7% of those wrong). At 5 to 1 ($w = 4$) the three scores are $-0.15$, 0 and $+0.21$, with 51% answered and 11.8% of those wrong. A reader with no power that answers the same share scores $-0.16$ and $-0.08$, so honesty without eyesight loses too. When a vendor reports a single accuracy number $a$, the rule collapses to one point. It can score only answer-everything, at $(a - t)/(1 - t)$ (86% at $t = 0.95$ scores $-1.8$ per question), and it says nothing about the policy you would actually run.

**How:** Start from the desk's costs: a right answer costs 0, an abstention $-C_{\text{abs}}$, a wrong answer $-C_{\text{FP}}$. Add $C_{\text{abs}}$ and divide by $C_{\text{abs}}$. That is a positive affine map, so it changes no decision, and it gives $+1$, $0$ and $-(C_{\text{FP}} - C_{\text{abs}})/C_{\text{abs}}$. With $t = p^\ast$, $t/(1-t) = (C_{\text{FP}} - C_{\text{abs}})/C_{\text{abs}} = w$, which is Kalai's penalty. The honest policy (answer iff $p > t$) is optimal question by question. It beats answer-everything by $\mathbb{E}\big[((1-p)w - p)^+\big]$, which is positive as soon as some questions have $p < t$. It beats abstain-everything by $\mathbb{E}\big[(p - (1-p)w)^+\big]$, which is positive as soon as some have $p > t$. It can act on that split only if its $\hat p$ separates the two groups, which is what power means. In risk–coverage terms the score per question at threshold $\theta$ is

$$
\text{score}(\theta) = \phi(\theta)\Big[1 - \frac{R(\theta)}{1 - t}\Big],
$$

which is positive if and only if the selective risk satisfies $R < 1 - t = C_{\text{abs}}/C_{\text{FP}}$. A vendor's single accuracy number is the point $\phi = 1$, $R = 1 - a$. Scoring the honest policy needs $\phi$ and $R$ at *your* $t$, and that means the curve. If the vendor's number is accuracy on answered questions with no coverage beside it, abstaining on everything but one sure question posts 100%, which is ROBO's 0.0% at 0.0% again.

**The trap:** Grading only one side of the trade-off. Grade accuracy alone and answer-everything wins; grade hallucination rate alone and abstain-everything wins. Those are ROBO's two bosses. The quieter trap is a round-number penalty such as $-1$, which puts $t$ at 0.5 and lets the reader bluff on every 60% claim, when a wrong basket costs twenty checks. The penalty has to be the cost ratio.

**If you got this wrong, read:** the start of §26.5 (Kalai et al., the cost version, and ROBO's two failures); then §26.4, "Calibration and selective prediction", for $\phi$, $R$ and why power cannot be added after the fact; then the Paleologo annotation in §26.3 on vendor numbers.

**Z.26.4: Prove it**

**Answer:** For $p \in [0,1]$ and $k \ge 1$, $p^k \le p \le 1 - (1-p)^k$, with equality only at $k = 1$ or $p \in \{0, 1\}$. Both $\binom{c}{k}/\binom{n}{k}$ and $1 - \binom{n-c}{k}/\binom{n}{k}$ are unbiased, because each is an average of an indicator over all $\binom{n}{k}$ subsets of attempts. Put pass$^k$ in the model-risk report. pass@$k$ is in the vendor deck because it is the bigger number (0.998 against 0.168 at $p = 0.7$, $k = 5$), and because it quietly assumes an oracle that picks out the attempt that worked.

**How:** The bounds take one line each: $p^k = p \cdot p^{k-1} \le p$, and $(1-p)^k \le 1 - p$ gives $1 - (1-p)^k \ge p$. For unbiasedness, let $X_1, \dots, X_n$ be i.i.d. Bernoulli($p$). Among the $k$-subsets $S$, exactly $\binom{c}{k}$ contain only successes, so

$$
\frac{\binom{c}{k}}{\binom{n}{k}} = \frac{1}{\binom{n}{k}} \sum_{|S| = k}\ \prod_{i \in S} X_i , \qquad \mathbb{E}\Big[\prod_{i \in S} X_i\Big] = p^k ,
$$

and the average of terms with mean $p^k$ has mean $p^k$. Replace $X_i$ by $1 - X_i$: $\binom{n-c}{k}/\binom{n}{k}$ is unbiased for $(1-p)^k$, so one minus it is unbiased for pass@$k$. Both need $k \le n$, because otherwise there are no $k$-subsets to average over, and that is why the listing returns NaN. A worked case: with 14 successes in 20, the pass$^5$ estimate is $2002/15504 = 0.129$ and the pass@5 estimate is $1 - 6/15504 = 0.9996$. Averaged over $c \sim \text{Bin}(20, 0.7)$, the first comes to exactly $0.7^5 = 0.16807$. On the report: the desk asks the same clause every quarter and acts on every answer, so the event that costs money is "wrong at least once", and pass$^k$ is its complement. pass@$k$ is best-of-$k$ with a perfect picker. In a coding benchmark the unit test does the picking. On a desk, if you had a perfect picker you would not need the reader.

**The trap:** Using the plug-in $(c/n)^k$. Because $x^k$ is convex, Jensen gives $\mathbb{E}[(c/n)^k] \ge p^k$. At $n = 20$, $p = 0.7$, $k = 5$ the plug-in averages 0.204 against a true 0.168, overstating consistency by about a fifth. (The pass@$k$ plug-in errs the other way: it is concave, and it averages 0.9940 against 0.9976.) The other trap is returning 0 when $k > n$. A zero averages into a dashboard as "this agent never works". NaN says "not measured".

**If you got this wrong, read:** §26.6, "The arithmetic of chains" and "The Full Derivation: the unbiased pass^k estimator", with the *Reliability multiplies; attempts add* box; then `pass_hat_k` and `pass_at_k` in Listing 26.3 (Appendix F).

**Z.26.5: The melting ice cube**

**Answer:** **9 clean months** (April to December 2026) for any feature the new model computes, down from 18 (July 2025 to December 2026) under the June 2025 cutoff. The other 27 months, January 2024 to March 2026, are inadmissible for new-model features. The feature history computed with the old model is still usable, and keeps its 18 clean months, but only if its outputs were logged when they were made, with each value keyed by prompt hash, model id, sampling parameters and timestamp. The model version must also have been pinned for the whole stretch, with no silent vendor update; check that $\hat\kappa$ and the cross-family disagreement rate stay flat across it. And the prompt must have been frozen before July 2025. Recomputing "with the old model" later counts only if the vendor still serves the pinned weights and your $\hat\kappa$ on a fixed prompt set shows they have not moved. The stakes are measurable: a Sharpe ratio's standard error is about $1/\sqrt{0.75} = 1.15$ over 9 months and $1/\sqrt{1.5} = 0.82$ over 18, so a true Sharpe of 2 is 1.7 standard errors from zero in one case and 2.4 in the other. The vendor's update cost you the ability to measure the feature.

**How:** The admissible set for a generator with cutoff $T_c$ is

$$
\mathcal{T}_{\text{adm}} = \{\, t : t > T_c \,\},
$$

and the cutoff that matters is the cutoff *of the model that produced each value*. On 36 month-start dates from January 2024, $T_c$ = 30 June 2025 admits 18 dates (Listing 26.3 asserts exactly this), and $T_c$ = 31 March 2026 admits 9. Kaz's springing lien: a springing lien attaches when a trigger written into the document fires, and it binds collateral from then on. Nothing attaches to values you have already logged. What moves is $T_c$, and it moves only in the admissible set of features the *new* model computes. That model has read July 2025 to March 2026, so its knowledge reaches back over nine months that used to be clean. Going forward, either stay on the pinned old version or bring the new one in as a challenger scored on an overlap of post-March months. Do not splice old-model values before the switch onto new-model values after it without a version column, because a level shift on the switch date is a feature of the vendor, not of the covenant.

**The trap:** There are two, and they point in opposite directions. "The update contaminates everything, so throw the old history away" is wrong, because a value produced by a model that had not read the future stays clean, provided you can prove which model produced it. "Nothing changed, rerun the backtest with the new model, still 18 months" is wrong, because the new model has read the ending of nine of those months. The off-by-one: counting March 2026 as clean (10 months). A cutoff stated as a month means the model may have read any day of it.

**If you got this wrong, read:** §26.7, the admissible window and the melting-ice-cube paragraph, and Long Scene B at 11:05 (seven clean months, standard error 1.3); then §26.9's replay contract (stochastic outputs are stored as point-in-time data and never re-run) and §26.8's vendor row (every update enters as a challenger).

**Z.26.6: The technical amendment**

**Answer:** The test is a section-scoped diff of operative text, and it runs before the reader does. **Inputs:** (1) the conformed copy $C$, as amended through the day before the amendment, in the store's canonical normalized text, with its hash; (2) the amendment: every character in the PDF's text layer, whatever its colour, size or position, normalized the same way, together with the post-amendment text $C'$ it produces (its conformed exhibit, or its "is hereby amended" instructions applied in code); (3) the section index, which maps section ids such as 6.08(b)(xii) to character ranges in $C$ and $C'$. **Output:** the set $\Delta$ of section ids whose text changed, each with its old and new SHA-256 and the changed lines. Any claim of the form "does not modify §$X$" fails when $X \in \Delta$, and the capacity column cannot stay put until a human signs. On §26.10's document, $\Delta$ contains 6.08(b)(xii) with eleven changed lines, and the white-text claim fails. **The failure mode:** a change routed through a definition. Amend "Consolidated EBITDA" (an uncapped add-back, like "Automatable Services" in §26.3) or "Available Amount" in Article I and leave §6.08 byte-identical. A section-scoped diff then excludes 6.08 from $\Delta$, "this amendment does not modify Section 6.08" is literally true and economically false, and the test passes the malicious document along with it.

**How:** Normalize $C$ and $C'$ the same way (ligatures, hyphenation, whitespace), slice both by the section index, compare hashes section by section, and emit line diffs wherever they differ. Visibility never enters the test: it reads the same bytes whether they render black, white or at half a point. That is why it beats a "find the white text" detector, which an attacker defeats by switching to a tiny font or putting the text behind an image. Its strength is that it never trusts what the document says about itself. Its weakness is its scope: it compares text inside sections, while a basket's economics live in the definitions the section uses. Close the gap by diffing the whole agreement and pushing $\Delta$ through the definition graph of Chapter 25, so that §6.08 is flagged whenever any defined term in its transitive closure changes. What is left after that is the one thing no diff can check, its own baseline. If the conformed copy came from the borrower's counsel, or already absorbed an earlier "technical" amendment, the diff measures change from the wrong base. So the conformed copy needs provenance of its own: who prepared it, as of what date, and its hash.

**The trap:** Trusting the citation contract or a second reader. The white sentence earns $V = 1$ and $S = 1$, because the document really does say it, and a second model family reading the same text layer reads the same instruction. Provenance proves that the document said it, not that the document is honest. The smaller trap is to write the test as "detect hidden text". That catches this attack and not the next one, and it raises alarms on harmless white boilerplate.

**If you got this wrong, read:** §26.10, the *Ways This Blows Up* box and Theo's Thursday; §26.4 for what $V$ and $S$ do and do not prove; and Chapter 25's definition graph for the transitive closure.

<!-- STATUS: COMPLETE -->
